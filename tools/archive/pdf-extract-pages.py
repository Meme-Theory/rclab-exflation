#!/usr/bin/env python3
"""Extract specific pages from a PDF into a new clean file.

Workaround for anthropics/claude-code#30819: the Read tool's `pages`
parameter is broken on Windows — it reports ALL PDFs as
"password-protected" when pages are requested. The error has nothing
to do with passwords; the page-splitting code path is broken.

Fix: extract the pages you need into a small new PDF, then use the
Read tool WITHOUT the pages parameter.

The Read tool accepts up to 10 pages without the `pages` parameter.
For larger ranges, use --batch to split into 10-page chunks.

Usage:
    python pdf-extract-pages.py INPUT.pdf PAGES [OUTPUT.pdf]
    python pdf-extract-pages.py INPUT.pdf --batch [OUTDIR]

PAGES format:
    "1-5"       pages 1 through 5
    "3"         page 3 only
    "1-5,8,12"  pages 1-5, 8, and 12

--batch mode:
    Splits the entire PDF into 10-page chunks in OUTDIR (default: same dir).
    Produces INPUT_p001-010.pdf, INPUT_p011-020.pdf, etc.

If OUTPUT is omitted in single mode, writes to INPUT_p{PAGES}.pdf
"""

import sys
import re
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF not installed. Run: pip install PyMuPDF", file=sys.stderr)
    sys.exit(1)

CHUNK_SIZE = 10  # Max pages the Read tool accepts without `pages` param


def parse_pages(spec: str, total: int) -> list[int]:
    """Parse page spec like '1-5,8,12' into 0-based page indices."""
    pages = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            start, end = part.split("-", 1)
            start, end = int(start), int(end)
            if start < 1 or end > total:
                print(f"ERROR: page range {start}-{end} out of bounds (1-{total})", file=sys.stderr)
                sys.exit(1)
            pages.extend(range(start - 1, end))  # convert to 0-based
        else:
            p = int(part)
            if p < 1 or p > total:
                print(f"ERROR: page {p} out of bounds (1-{total})", file=sys.stderr)
                sys.exit(1)
            pages.append(p - 1)
    return pages


def extract_pages(input_path: str, page_spec: str, output_path: str | None = None) -> str:
    src = Path(input_path)
    if not src.exists():
        print(f"ERROR: {src} not found", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open(str(src))
    total = len(doc)

    if doc.needs_pass:
        print("ERROR: PDF requires a password to open.", file=sys.stderr)
        doc.close()
        sys.exit(1)

    pages = parse_pages(page_spec, total)
    print(f"Source:  {src.name} ({total} pages)")
    print(f"Extract: {page_spec} → {len(pages)} page(s)")

    if len(pages) > CHUNK_SIZE:
        print(f"WARNING: {len(pages)} pages exceeds Read tool limit of {CHUNK_SIZE}. "
              f"Use --batch mode or request ≤{CHUNK_SIZE} pages.", file=sys.stderr)

    # Create fresh document with selected pages
    new_doc = fitz.open()
    # Always use individual inserts for correctness with any page selection
    for p in pages:
        new_doc.insert_pdf(doc, from_page=p, to_page=p)
    doc.close()

    # Determine output path
    if output_path is None:
        safe_spec = re.sub(r"[,\s]+", "_", page_spec)
        dst = src.with_stem(f"{src.stem}_p{safe_spec}")
    else:
        dst = Path(output_path)

    new_doc.save(str(dst), garbage=3, deflate=True)
    new_doc.close()

    print(f"Output:  {dst} ({len(pages)} pages, {dst.stat().st_size:,} bytes)")
    return str(dst)


def batch_split(input_path: str, out_dir: str | None = None) -> list[str]:
    src = Path(input_path)
    if not src.exists():
        print(f"ERROR: {src} not found", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open(str(src))
    total = len(doc)

    if doc.needs_pass:
        print("ERROR: PDF requires a password to open.", file=sys.stderr)
        doc.close()
        sys.exit(1)

    dst_dir = Path(out_dir) if out_dir else src.parent
    dst_dir.mkdir(parents=True, exist_ok=True)

    print(f"Source:  {src.name} ({total} pages)")
    print(f"Chunks:  {CHUNK_SIZE} pages each → {(total + CHUNK_SIZE - 1) // CHUNK_SIZE} files")
    print(f"Output:  {dst_dir}/")
    print()

    outputs = []
    for start in range(0, total, CHUNK_SIZE):
        end = min(start + CHUNK_SIZE, total)
        chunk_doc = fitz.open()
        chunk_doc.insert_pdf(doc, from_page=start, to_page=end - 1)

        # 1-based labels for filenames
        label = f"p{start+1:03d}-{end:03d}"
        dst = dst_dir / f"{src.stem}_{label}.pdf"

        chunk_doc.save(str(dst), garbage=3, deflate=True)
        chunk_doc.close()

        size_kb = dst.stat().st_size / 1024
        print(f"  {dst.name}  ({end - start} pages, {size_kb:.0f} KB)")
        outputs.append(str(dst))

    doc.close()
    print(f"\n{len(outputs)} chunks written.")
    return outputs


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(0)

    input_path = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2] == "--batch":
        out_dir = sys.argv[3] if len(sys.argv) > 3 else None
        batch_split(input_path, out_dir)
    elif len(sys.argv) >= 3:
        page_spec = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else None
        extract_pages(input_path, page_spec, output_path)
    else:
        print("ERROR: specify PAGES or --batch", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
