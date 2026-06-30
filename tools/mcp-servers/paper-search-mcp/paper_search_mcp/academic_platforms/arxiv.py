# paper_search_mcp/sources/arxiv.py
from typing import List, Optional, Dict
from datetime import datetime
import re
import requests
import feedparser
from bs4 import BeautifulSoup, NavigableString
from ..paper import Paper
from PyPDF2 import PdfReader
import os

class PaperSource:
    """Abstract base class for paper sources"""
    def search(self, query: str, **kwargs) -> List[Paper]:
        raise NotImplementedError

    def download_pdf(self, paper_id: str, save_path: str) -> str:
        raise NotImplementedError

    def read_paper(self, paper_id: str, save_path: str) -> str:
        raise NotImplementedError

class ArxivSearcher(PaperSource):
    """Searcher for arXiv papers"""
    BASE_URL = "http://export.arxiv.org/api/query"
    HTML_BASE = "https://arxiv.org/html"

    def search(self, query: str, max_results: int = 10) -> List[Paper]:
        params = {
            'search_query': query,
            'max_results': max_results,
            'sortBy': 'relevance',
            'sortOrder': 'descending'
        }
        response = requests.get(self.BASE_URL, params=params)
        feed = feedparser.parse(response.content)
        papers = []
        if not feed.entries:
            print(f"[arXiv] No results for query: {query}")
        for entry in feed.entries:
            try:
                authors = [author.name for author in entry.authors]
                published = datetime.strptime(entry.published, '%Y-%m-%dT%H:%M:%SZ')
                updated = datetime.strptime(entry.updated, '%Y-%m-%dT%H:%M:%SZ')
                pdf_url = next((link.href for link in entry.links if link.type == 'application/pdf'), '')
                papers.append(Paper(
                    paper_id=entry.id.split('/')[-1],
                    title=entry.title,
                    authors=authors,
                    abstract=entry.summary,
                    url=entry.id,
                    pdf_url=pdf_url,
                    published_date=published,
                    updated_date=updated,
                    source='arxiv',
                    categories=[tag.term for tag in entry.tags],
                    keywords=[],
                    doi=entry.get('doi', '')
                ))
            except Exception as e:
                print(f"Error parsing arXiv entry: {e}")
        return papers

    def download_pdf(self, paper_id: str, save_path: str) -> str:
        pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"
        response = requests.get(pdf_url)
        output_file = f"{save_path}/{paper_id}.pdf"
        with open(output_file, 'wb') as f:
            f.write(response.content)
        return output_file

    def fetch_html(self, paper_id: str) -> Optional[Dict[str, str]]:
        """Fetch arXiv's experimental LaTeXML HTML rendering.

        Returns a dict with 'text' (markdown-ish, equations as $...$/$$...$$ from
        each <math>'s alttext) and 'url' on success. Returns None when HTML is
        unavailable for this paper -- LaTeXML conversion failed, paper too old,
        non-200 response, etc. Coverage is roughly 2023-onward; older papers
        and a minority of recent ones with unusual TeX have no HTML build.

        The version suffix in paper_id is honored if present (e.g., '2511.07517v3').
        Without it, arXiv serves the latest version.
        """
        url = f"{self.HTML_BASE}/{paper_id}"
        try:
            resp = requests.get(url, timeout=30, allow_redirects=True)
        except requests.RequestException:
            return None
        if resp.status_code != 200 or 'ltx_document' not in resp.text:
            return None
        soup = BeautifulSoup(resp.content, 'html.parser')
        article = soup.find('article', class_='ltx_document')
        if article is None:
            return None
        # Drop chrome that get_text would otherwise pull in.
        for tag in article.find_all(['nav', 'script', 'style', 'footer', 'button']):
            tag.decompose()
        # Replace <math> with LaTeX from alttext. Display math wraps with $$,
        # inline with $; orphan <math> without alttext is dropped.
        for math in article.find_all('math'):
            alttext = (math.get('alttext') or '').strip()
            if not alttext:
                math.decompose()
                continue
            if math.get('display') == 'block':
                math.replace_with(f"\n\n$$ {alttext} $$\n\n")
            else:
                math.replace_with(f" ${alttext}$ ")
        # Convert headings to ATX markdown.
        for level in range(1, 7):
            for h in article.find_all(f'h{level}'):
                heading_text = h.get_text(' ', strip=True)
                h.replace_with(f"\n\n{'#' * level} {heading_text}\n\n")
        # Force breaks after block elements that get_text would otherwise run together.
        for block in article.find_all(['p', 'li', 'figcaption', 'tr']):
            block.insert_after(NavigableString('\n\n'))
        text = article.get_text('')
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r' *\n *', '\n', text)
        text = re.sub(r'\n{3,}', '\n\n', text).strip()
        return {'text': text, 'url': url}

    def read_paper(self, paper_id: str, save_path: str = "./downloads") -> str:
        """Read a paper and return its text.

        Tries the LaTeXML HTML build first (no PDF download, equations preserved
        as LaTeX). Falls back to PDF download + PyPDF2 extraction when HTML is
        unavailable. The returned string is prefixed with a single tag line:

            [arxiv-paper-source: html url=...]
            [arxiv-paper-source: pdf path=...]

        so the caller can tell which path was taken (HTML output is materially
        cleaner, especially for math-heavy papers).
        """
        html = self.fetch_html(paper_id)
        if html is not None:
            return f"[arxiv-paper-source: html url={html['url']}]\n\n{html['text']}"
        # Fallback: PDF
        pdf_path = f"{save_path}/{paper_id}.pdf"
        if not os.path.exists(pdf_path):
            os.makedirs(save_path, exist_ok=True)
            pdf_path = self.download_pdf(paper_id, save_path)
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return f"[arxiv-paper-source: pdf path={pdf_path}]\n\n{text.strip()}"
        except Exception as e:
            print(f"Error reading PDF for paper {paper_id}: {e}")
            return ""

if __name__ == "__main__":
    # 测试 ArxivSearcher 的功能
    searcher = ArxivSearcher()
    
    # 测试搜索功能
    print("Testing search functionality...")
    query = "machine learning"
    max_results = 5
    try:
        papers = searcher.search(query, max_results=max_results)
        print(f"Found {len(papers)} papers for query '{query}':")
        for i, paper in enumerate(papers, 1):
            print(f"{i}. {paper.title} (ID: {paper.paper_id})")
    except Exception as e:
        print(f"Error during search: {e}")
    
    # 测试 PDF 下载功能
    if papers:
        print("\nTesting PDF download functionality...")
        paper_id = papers[0].paper_id
        save_path = "./downloads"  # 确保此目录存在
        try:
            os.makedirs(save_path, exist_ok=True)
            pdf_path = searcher.download_pdf(paper_id, save_path)
            print(f"PDF downloaded successfully: {pdf_path}")
        except Exception as e:
            print(f"Error during PDF download: {e}")

    # 测试论文阅读功能
    if papers:
        print("\nTesting paper reading functionality...")
        paper_id = papers[0].paper_id
        try:
            text_content = searcher.read_paper(paper_id)
            print(f"\nFirst 500 characters of the paper content:")
            print(text_content[:500] + "...")
            print(f"\nTotal length of extracted text: {len(text_content)} characters")
        except Exception as e:
            print(f"Error during paper reading: {e}")