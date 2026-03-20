# ArXiv Submission Workflow and Best Practices

**Author(s):** ArXiv (Cornell University), Physics Community
**Year:** 1991+ (ArXiv founding), 2020+ (current practices)
**Reference:** ArXiv Help (arxiv.org/help), ArXiv Submission Guidelines

---

## Abstract

ArXiv.org is the primary repository for preprints in physics, mathematics, and computer science. This document covers ArXiv submission procedures: account setup, file preparation (.bbl compilation, figure inclusion), metadata entry (title, abstract, categories), submission workflow, versioning (v1, v2, v3...), and cross-listing strategy. For the phonon-exflation project, ArXiv posting is essential for establishing priority and disseminating results before formal journal publication.

---

## Historical Context

Paul Ginsparg created ArXiv (originally arXiv.org) in 1991 as a preprint server for high-energy physics. It has grown to encompass all of physics, mathematics, statistics, and related fields. ArXiv assigns permanent identifiers (e.g., 2305.12345) that never change, even if a paper is later published elsewhere. Posting to ArXiv is standard practice: physicists post simultaneously with journal submission or before, and journals typically accept ArXiv versions.

For phonon-exflation: ArXiv posting establishes priority for the no-go result (V_spec monotone, gap equation failure) and the positive theorem (block-diagonality, KO-dimension=6).

---

## Setting Up Your ArXiv Account

### Registration

1. Visit https://arxiv.org/
2. Click "User" (top right) -> "Register"
3. Provide email address, password
4. Verify email (click link in confirmation message)
5. Complete profile: name, affiliation, subject areas

### Subject Area Classification

Select your primary and secondary categories:

- **hep-th**: High Energy Physics - Theory (suitable for spectral action, QFT)
- **gr-qc**: General Relativity and Quantum Cosmology (for cosmological aspects)
- **math-ph**: Mathematical Physics (for NCG, spectral theory)
- **math.DG**: Differential Geometry (secondary, for KK geometry)

---

## File Preparation

### Critical: Compile Bibliography to .bbl

ArXiv does not allow external packages like BibLaTeX to run during compilation. You must pre-compile your bibliography:

```bash
# Step 1: LaTeX compilation
pdflatex paper.tex

# Step 2: BibTeX (generates paper.bbl)
bibtex paper.aux

# Step 3: Create .bbl file
# The .bbl file is now in your directory
ls paper.bbl
```

### Directory Structure for Submission

Create a clean submission directory:

```bash
mkdir paper_arxiv
cd paper_arxiv

# Copy files
cp paper.tex .
cp paper.bbl .
cp fig_spectrum.pdf .
cp fig_phase.pdf .
cp fig_metrics.pdf .

# Do NOT include these:
# rm paper.aux
# rm paper.log
# rm *.synctex.gz
# rm *~

ls -la
# Shows:
# paper.tex
# paper.bbl
# fig_spectrum.pdf
# fig_phase.pdf
# fig_metrics.pdf
```

### LaTeX Header Modification

In your `.tex` file, replace:
```latex
\bibliography{phonon_exflation}
```

with:
```latex
\begin{thebibliography}{99}
\end{thebibliography}
```

Then embed the `.bbl` contents. Alternatively, use `\input{paper.bbl}`:

```latex
% In paper.tex, replace \bibliography line with:
\input{paper.bbl}
```

### Alternative: Use Ancillary Files

ArXiv allows "ancillary files" (data, code, supplementary PDFs) that are not part of the paper but are archived:

```bash
# Create anc/ directory for supplementary files
mkdir anc
cp simulation_data.npz anc/
cp README.md anc/
```

---

## Figure Inclusion

### Supported Formats

- **PDF** (vector, preferred)
- **EPS** (Encapsulated PostScript, legacy)
- **PNG** (raster, acceptable but not ideal)
- **JPEG** (raster, acceptable for photos only)

### Inline PGF Figures

If you use `.pgf` files:

```latex
\usepackage{pgf}
% Include directly:
\input{spectrum.pgf}
```

The `.pgf` file must be in your submission directory.

### Pdflatex or Latex?

- **Use pdflatex**: Modern standard, generates PDF directly
- **Avoid latex**: Creates DVI, requires conversion (deprecated)

ArXiv will attempt pdflatex. If your file uses packages incompatible with pdflatex, it will fail.

### Verify Compilation Locally

Before uploading, test locally:

```bash
# Create a test directory
mkdir test_arxiv
cd test_arxiv
cp ../paper.tex ../paper.bbl ../fig_*.pdf .

# Compile exactly as ArXiv would
pdflatex paper.tex
# Check output
ls paper.pdf
open paper.pdf  # or your PDF viewer
```

---

## Metadata Entry

### Title

- **Max 200 characters** (including spaces)
- **Descriptive, searchable**: Include key terms (NCG, Dirac spectrum, cosmology)
- **Avoid symbols**: Use "SU(3)" not "$\mathrm{SU}(3)$"

Good title:
"Spectral Action on Noncommutative SU(3): A No-Go Theorem for Starobinsky Inflation"

Bad title:
"On the Cosmology of Noncommutative Geometry"

### Abstract

- **200-300 words** (ArXiv limit is 1920 characters)
- **Concise, complete**: State problem, method, results
- **No citations** (except arXiv references: "arXiv:1234.5678")
- **Plain text**: No LaTeX commands ($\tau$ becomes "tau" in plain text)

Example abstract:

"We investigate the spectral action principle on the Jensen-deformed SU(3) manifold, a framework for extracting physical constants from geometry. Using noncommutative geometry, we compute the Seeley-DeWitt coefficients exactly and find that the quadratic curvature term (a_4) dominates the linear term (a_2) by a factor of 1000 at the base scale. This prevents Starobinsky inflation from emerging. We prove a no-go theorem: any Starobinsky-type mechanism fails on compact Lie groups of dimension greater than 4 with the spectral action. We discuss implications for alternative inflation models and the role of non-perturbative physics."

### Categories

Select primary (required) and up to 5 secondary categories:

```
Primary:     hep-th
Secondary:   gr-qc
             math-ph
             math.DG
```

### Keywords

Optional. ArXiv extracts keywords from abstract, but you can add:

"noncommutative geometry; spectral action; cosmological inflation; Dirac spectrum; Kaluza-Klein"

---

## Submission Process

### Step 1: Upload Files

1. Log in to https://arxiv.org/ -> "Submit"
2. Select "New Submission"
3. Choose upload method:
   - **Single file (PDF, DVI)**: Upload paper.pdf directly (don't do this)
   - **Upload tar/zip** (recommended): Create `.tar.gz` or `.zip`

```bash
# Create submission archive
cd paper_arxiv
tar -czf paper_arxiv.tar.gz *.tex *.bbl *.pdf
# Upload paper_arxiv.tar.gz
```

Or on Windows (using 7-Zip or similar):
```bash
# Create .zip with all files
paper.tex
paper.bbl
fig_spectrum.pdf
fig_phase.pdf
```

### Step 2: Enter Metadata

After uploading files:
1. **Title**: Enter title
2. **Abstract**: Paste abstract (plain text, no LaTeX)
3. **Categories**: Select primary + secondary
4. **Authors**: Add all author names (Last, First, Affiliation optional)
5. **Comments**: Version info, e.g., "20 pages, 5 figures"
6. **Journal Reference**: Leave blank (added after journal acceptance)
7. **DOI**: Leave blank (assigned by journal)

### Step 3: Verify

1. ArXiv extracts and previews your PDF
2. **Check carefully**: Look for:
   - Correct fonts
   - Figure placement
   - Math rendered correctly
   - Bibliography appears
3. If issues, go back and fix `.tex` / recompile locally

### Step 4: Submit

Click "Submit" after verification.

---

## Post-Submission

### Confirmation and Identifier

Within 1-2 hours, you receive confirmation email with ArXiv identifier:

- **Format**: YYMM.DDDDD (e.g., 2302.14159)
- **Use this identifier** to cite your preprint: "arXiv:2302.14159"

### Versioning

To update your paper (corrections, new results):

1. Log in to ArXiv
2. Find your submission
3. Click "Replace"
4. Upload new files (same process as initial submission)
5. Enter change summary (what changed, why)

New version becomes `v2`, `v3`, etc.:
- arXiv:2302.14159 (v1)
- arXiv:2302.14159v2 (updated version)

**Note**: All versions remain publicly available and citable.

### Revision Strategy

- **v1**: Initial submission to ArXiv + journal
- **v2**: After reviewer feedback, before journal acceptance (optional if minor)
- **v3**: Major revisions after journal acceptance (if journal allows)

---

## Cross-Listing to Multiple Categories

If your paper spans hep-th AND gr-qc (cosmology + quantum field theory):

During submission:
1. Choose **primary category**: hep-th (or gr-qc if stronger emphasis)
2. Add **secondary categories**: Include the other one (gr-qc or hep-th)

This appears in abstract as:
```
hep-th (primary), gr-qc (cross-list), math-ph (optional secondary)
```

---

## Journal Submission After ArXiv

### Timeline

1. **ArXiv posting**: Day 0 (establish priority)
2. **Journal submission**: Day 0-3 (same time or shortly after)
3. **Reference in journal**: Include ArXiv identifier
   - "This work was submitted to arXiv: arXiv:2302.14159"

### Journal Instructions

Many journals now say: "Preprints on arXiv are acceptable. Cite the ArXiv identifier in your submission."

### Submission Letter

Include in journal submission (e.g., to JHEP):

"We submit our manuscript 'Spectral Action on SU(3): No-Go Theorem for Starobinsky Inflation' for consideration in Journal of High Energy Physics. The manuscript has been posted to the preprint archive arXiv:2302.14159. All authors agree to this submission. We certify that this work has not been published elsewhere and is not under review by other journals."

---

## Deactivating or Withdrawing

If you need to remove a paper:

1. Log in -> Find submission
2. Click "Withdraw" (removes from public listing but identifier remains)

**Note**: Withdrawal is permanent and rare. Use only if:
- Major error discovered before acceptance
- Work scooped and you want to pursue different angle

Most papers remain on ArXiv indefinitely.

---

## Common Submission Errors

1. **Bibliography not compiled**: .bbl file missing. ArXiv compilation fails with "! LaTeX Error: File `phonon_exflation.bib' not found."
   - **Fix**: Use `\input{paper.bbl}` or pre-compile bibtex

2. **Figures not embedded**: Figure files missing from tar/zip. PDF shows blank spaces.
   - **Fix**: Verify all `.pdf` files included in archive

3. **Hyperref issues**: Links in PDF don't work or cause errors.
   - **Fix**: Add to preamble: `\usepackage[hidelinks]{hyperref}`

4. **Non-ASCII characters**: Author names with accents cause encoding errors.
   - **Fix**: Use LaTeX commands (`\'e` for é) in author list

5. **pdflatex not working**: Paper uses deprecated packages (old versions of tikz).
   - **Fix**: Test locally with `pdflatex paper.tex` before uploading

---

## ArXiv Guidelines Summary

| Item | Requirement |
|------|-------------|
| Title | ≤ 200 characters, no symbols |
| Abstract | ≤ 1920 characters, plain text |
| Categories | 1 primary + up to 5 secondary |
| Files | .tex + .bbl + figures (.pdf), in tar/zip |
| Compilation | pdflatex (no external package runs) |
| Figures | PDF, EPS, or PNG (≤ 10 MB total) |
| Fonts | Standard (Computer Modern, Times) |

---

## Timeline for Phonon-Exflation Papers

### Session 25 Preliminary (Post-24b)

**Before arXiv posting**:
- Write paper (no-go + Spectral Anatomy both candidate papers)
- Compile bibliography
- Create figures (spectrum, phase diagrams)
- Test local pdflatex compilation
- Register ArXiv account (if not done)

**ArXiv posting**:
- Create identifier (YYMM.DDDDD)
- Post to hep-th (primary), gr-qc + math-ph (secondary)

**Journal submission** (follow within 1 week):
- JHEP (primary target)
- CMP, JGP (secondary targets, if splitting into two papers)
- PRD (if emphasizing cosmology)

---

## Connection to Phonon-Exflation Framework

ArXiv submission enables:
- Permanent public record of research (establishes priority)
- Rapid dissemination to physics community before journal review
- Free, open access (vs. paywalled journals)
- Cross-listing across theoretical physics categories (hep-th, gr-qc, math-ph)
- Standard preprint identifier for citations
- Versioning for rapid correction and updates
- Professional dissemination channel for no-go and positive results

Relevance to Project: **CRITICAL** - ArXiv posting is essential for modern physics publication workflow.
