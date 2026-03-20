# BibLaTeX: Modern Bibliography Management for LaTeX

**Author(s):** Philipp Lehman (author), Philip Kime (lead maintainer), Audrey Boruvka, Joseph Wright (co-maintainers)
**Year:** 2008 (original), 2020+ (modern updates)
**Reference:** BibLaTeX Manual (ctan.org), CTAN BibLaTeX Package

---

## Abstract

BibLaTeX is a modern replacement for the older BibTeX system, offering superior formatting flexibility, built-in citation styles, and integration with INSPIRE-HEP (the high-energy physics literature database). This document covers BibLaTeX package setup, citation commands, .bib file format, citation styles (numeric, alphabetic, author-year), cross-referencing, and INSPIRE-HEP integration for physics papers. BibLaTeX is recommended for the phonon-exflation project's multi-author, multi-venue publication strategy.

---

## Historical Context

BibTeX (1985) revolutionized bibliography management by introducing a separate data format (.bib files) independent of LaTeX. However, BibTeX has limitations: inflexible citation formats, weak support for cross-referencing, and poor handling of modern publication venues (e.g., arXiv). BibLaTeX (2008) addresses these limitations by moving formatting logic into the LaTeX layer, enabling dynamic citation styles, rich metadata fields, and easier customization.

For theoretical physics: BibLaTeX supports INSPIRE-HEP entries directly, making it ideal for citing preprints and journal articles across the high-energy physics literature.

---

## Basic Setup

Load BibLaTeX with backend specification:

```latex
\usepackage[
  style=numeric,
  backend=biber,
  sorting=none
]{biblatex}

\addbibresource{phonon_exflation.bib}
\addbibresource{connes_ncg.bib}
```

Key options:
- **backend=biber**: Modern, recommended (replaces bibtex)
- **style=numeric**: Citation style (others: alphabetic, authoryear, verbose)
- **sorting=none**: Keep citations in order of appearance (use sorting=nty for alphabetical)

### Compilation with Biber

```bash
pdflatex paper.tex
biber paper.bcf          # Use biber, not bibtex!
pdflatex paper.tex
pdflatex paper.tex
```

---

## Citation Commands

### Basic Citation Styles

```latex
% Numeric style (most common for physics)
\cite{Connes2006}              % [1]
\cite{Connes2006,Wald1984}     % [1, 2]

% Author-year style (activate with authoryear)
\cite{Connes2006}              % Connes 2006
\citep{Connes2006}             % (Connes 2006)
\citet{Connes2006}             % Connes (2006)

% Textual citations
\citeauthor{Connes2006}        % Connes
\citeyear{Connes2006}          % 2006
\citedate{Connes2006}          % 2006

% Full citation
\fullcite{Connes2006}          % Full bibliographic entry

% Footnote citation
\footcite{Connes2006}          % Full citation in footnote
```

---

## .bib File Format

### Standard Physics Entries

```bibtex
@article{Connes2006,
  author = {Alain Connes},
  title = {Noncommutative Geometry and Physics},
  journal = {Reviews of Modern Physics},
  volume = {79},
  pages = {976--1041},
  year = {2006},
  doi = {10.1103/RevModPhys.79.976}
}

@inproceedings{Chamseddine2007,
  author = {Chamseddine, Ali H. and Connes, Alain},
  title = {A Unified Framework for Noncommutative Geometry},
  booktitle = {Proceedings of Symposia in Pure Mathematics},
  volume = {77},
  pages = {121--156},
  year = {2007},
  publisher = {American Mathematical Society},
  doi = {10.1090/pspum/077/2459867}
}

@book{Wald1984,
  author = {Wald, Robert M.},
  title = {General Relativity},
  publisher = {University of Chicago Press},
  year = {1984}
}
```

### ArXiv and Preprint Entries

```bibtex
@article{Paasch2023,
  author = {Paasch, G. F.},
  title = {Phonon-Exflation and Mass Quantization},
  journal = {arXiv preprint},
  eprint = {2305.12345},
  year = {2023},
  archiveprefix = {arXiv}
}

% Alternative format (works with INSPIRE export)
@article{Paasch2023alt,
  author = {Paasch, G. F.},
  title = {Phonon-Exflation and Mass Quantization},
  eprint = {2305.12345},
  archiveprefix = {arXiv},
  primaryclass = {hep-th},
  year = {2023}
}
```

### Websites and Online Resources

```bibtex
@online{MathWorldDirac,
  author = {Weisstein, Eric W.},
  title = {Dirac Equation},
  year = {2024},
  url = {https://mathworld.wolfram.com/DiracEquation.html},
  urldate = {2024-02-21}
}

@misc{PyFFTWDocs,
  title = {pyFFTW Documentation},
  url = {https://pyfftw.readthedocs.io},
  year = {2024}
}
```

---

## Custom Fields in .bib

BibLaTeX supports extended metadata:

```bibtex
@article{Baptista2022,
  author = {Baptista, José M. and others},
  title = {Kaluza-Klein Geometry and Mass Spectrum},
  journal = {Journal of Geometry and Physics},
  volume = {180},
  pages = {104654},
  year = {2022},
  doi = {10.1016/j.geomphys.2022.104654},

  % Optional fields
  abstract = {We investigate KK geometry on compact spaces...},
  keywords = {Kaluza-Klein, Mass quantization, NCG},
  url = {https://example.com/paper.pdf},
  arXiv = {2207.01234},
  note = {Critical for phonon-exflation framework}
}
```

---

## Citation Styles

### Numeric (Default for Physics)

```latex
\usepackage[style=numeric]{biblatex}
```

Output: [1], [1, 2], etc.

### Alphabetic

```latex
\usepackage[style=alphabetic]{biblatex}
```

Output: [Con06], [CW84], etc.

### Author-Year (Chicago style)

```latex
\usepackage[style=authoryear]{biblatex}
```

Output: Connes (2006); Connes and Wald (1984).

### Verbose (Full citation on first use)

```latex
\usepackage[style=verbose]{biblatex}
```

Output: Alain Connes, "Noncommutative Geometry and Physics,"
Reviews of Modern Physics, vol. 79, no. 4, pp. 976–1041, 2006
[first occurrence]; Connes 2006 [subsequent occurrences].

---

## INSPIRE-HEP Integration

INSPIRE-HEP is the high-energy physics literature database. Export citations directly:

### Export from INSPIRE-HEP

1. Go to https://inspirehep.net/
2. Search for paper (e.g., "Connes noncommutative geometry")
3. Click "Export" -> "BibTeX"
4. Copy entry to .bib file

### Example INSPIRE Entry

```bibtex
@article{Connes:2005xx,
  author = {Connes, A.},
  title = {Noncommutative Geometry and Physics},
  journal = {Rev. Mod. Phys.},
  volume = {79},
  pages = {976--1041},
  year = {2006},
  eprint = {hep-th/0510603},
  archiveprefix = {arXiv},
  primaryclass = {hep-th},
  doi = {10.1103/RevModPhys.79.976}
}
```

---

## Cross-Referencing and Entry Reuse

### Related Entry (Manual)

```bibtex
@article{Author2024,
  author = {Author, A.},
  title = {Main Paper},
  journal = {Journal},
  year = {2024},
  note = {Related work: see also \cite{Related2023}}
}
```

### InCollection (Chapter in Edited Book)

```bibtex
@incollection{Connes2013,
  author = {Connes, Alain},
  title = {Geometry and Physics},
  booktitle = {Noncommutative Geometry and Physics: A Renaissance},
  editor = {Marcolli, Matilde and Seatley, David},
  publisher = {Springer},
  year = {2013},
  pages = {1--45}
}
```

---

## Sorting and Formatting Options

### Sorting Options

```latex
% Numeric order (default for numeric style)
\usepackage[sorting=none]{biblatex}

% Alphabetical by author
\usepackage[sorting=nty]{biblatex}  % name, title, year

% Chronological (most recent first)
\usepackage[sorting=ydnt]{biblatex}  % year, author, title (descending)
```

### Bibliography Printing

At end of document:

```latex
\section*{References}
\printbibliography

% Or with custom heading
\printbibliography[heading=bibintoc, title={References}]
```

---

## Advanced: Multiple Bibliographies

```latex
\usepackage[
  refsegment=section,
  backend=biber
]{biblatex}

\addbibresource{phonon_exflation.bib}
```

Print bibliography per section:

```latex
\section{Introduction}
...
\printbibliography[segment=1, title={References for Section 1}]

\section{Methods}
...
\printbibliography[segment=2, title={References for Section 2}]
```

---

## BibLaTeX vs BibTeX Comparison

| Feature | BibTeX | BibLaTeX |
|---------|--------|----------|
| Flexibility | Limited | Extensive |
| Citation styles | 10-20 (fixed) | 50+ (customizable) |
| INSPIRE-HEP support | Manual | Native |
| URL/DOI handling | Weak | Strong |
| Cross-references | Basic | Advanced |
| Backend | bibtex | biber |
| Modern markup | No | Yes |
| Learning curve | Easy | Moderate |

**Recommendation for phonon-exflation project**: Use BibLaTeX with biber backend.

---

## Common Pitfalls

1. **Forgetting to run biber**: Use `biber`, not `bibtex`. BibLaTeX requires biber backend.
2. **Unmatched braces in titles**: Protect titles with braces: `{NCG}` not `NCG`. Capitalize as intended: `{Noncommutative Geometry}`.
3. **Missing DOI**: Always include if available (use `doi` field, not `url`).
4. **ArXiv versioning**: For preprints, include `eprint` field with identifier.
5. **Author name format**: Use "Last, First" format in .bib for reliable parsing (e.g., `{Connes, Alain}`). "First Last" works for simple names but can misparse multi-word surnames.

---

## Workflow for Phonon-Exflation Papers

### Create Master .bib File

```bash
# Organize by topic
phonon_exflation.bib
  - Connes and NCG entries
  - Baptista and KK entries
  - Paasch and mass quantization
  - Einstein, Schwarzschild, related GR
  - Cosmology and expansion
```

### Compilation Sequence

```bash
pdflatex paper.tex    # Initial pass
biber paper.bcf       # Process bibliography
pdflatex paper.tex    # Integrate references
pdflatex paper.tex    # Final pass (hyperlinks resolved)
```

### Maintenance

- Keep .bib file version-controlled in git
- Share .bib across all phonon-exflation papers (consistency)
- Export from INSPIRE-HEP for all HEP papers (automatic DOI/arXiv integration)
- Manual entry for non-indexed papers (e.g., Baptista preprints)

---

## Connection to Phonon-Exflation Framework

BibLaTeX enables:
- Centralized bibliography management across multiple journals (JHEP, PRD, CMP, JGP)
- INSPIRE-HEP integration for seamless citation of HEP literature
- Flexible citation styles (numeric for journals, author-year for books)
- Cross-referencing between phonon-exflation papers
- Version-controlled .bib files for reproducible manuscript preparation
- Professional handling of preprints (arXiv identifiers and DOIs)

Relevance to Project: **HIGH** - Essential for managing citations to Connes, Baptista, Paasch, and supporting literature across multiple submission venues.
