# Mathematical Physics Journals: JGP and CMP Style Guidelines

**Author(s):** Journal of Geometry and Physics (Elsevier), Communications in Mathematical Physics (Springer), Editorial Boards
**Year:** 2020+ (current guidelines)
**Reference:** JGP (elsevier.com), CMP (springer.com), Journal Instructions for Authors

---

## Abstract

The phonon-exflation project's mathematical contributions are best suited for journals prioritizing geometric rigor and mathematical precision: the Journal of Geometry and Physics (JGP) and Communications in Mathematical Physics (CMP). This document covers submission requirements, formatting standards, proof environments, theorem numbering schemes, reference formatting, revision workflows, and strategic submission timelines. Both journals are peer-reviewed, open-access friendly, and highly respected in mathematical physics.

---

## Historical Context

The Journal of Geometry and Physics (founded 1984) and Communications in Mathematical Physics (founded 1965) represent the mathematical end of the physics spectrum. CMP is arguably the most prestigious mathematical physics journal globally, with rigorous peer review and international editorial board. Both journals demand mathematical rigor comparable to pure mathematics journals while maintaining physics relevance. Publishing in these venues signals deep theoretical contribution.

For phonon-exflation: The no-go paper (V_spec monotonicity, gap equation failure) is suitable for JGP or CMP. The positive paper (Spectral Anatomy of D_K on SU(3)) is ideal for CMP or JGP as a mathematical contribution.

---

## Journal of Geometry and Physics (JGP)

### Submission Portal

- **Website**: https://www.elsevier.com/journals/journal-of-geometry-and-physics
- **Submission**: https://ees.elsevier.com/gph/ (Editorial Manager system)
- **Scope**: Differential geometry, mathematical physics, cosmology, GR, gauge theory

### Document Class and Format

```latex
\documentclass[11pt]{article}
\usepackage{geometry}
\geometry{margin=2.5cm, a4paper}

% Standard packages
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}

% Elsevier-specific
\usepackage{natbib}  % for citations

\title{Phonon Exflation Cosmology: Spectral Action on SU(3)
        [No-Go Theorem for Inflation]}

\author{Author One\textsuperscript{a,b},
        Author Two\textsuperscript{a,*}
        \thanks{\textsuperscript{a}Department of Physics, University A, City;
                \textsuperscript{b}CERN, Geneva, Switzerland;
                \textsuperscript{*}Corresponding author:
                  [email redacted]}}

\begin{document}
\maketitle

\begin{abstract}
[Abstract: 150-250 words, plain text, no equations]
\end{abstract}

\keywords{Noncommutative geometry; Spectral action; Kaluza-Klein}

\section{Introduction}
...

\end{document}
```

### JGP Specifics

**Figures**:
- Max 80 mm width (single column)
- Color figures: First 2 free, then charged
- Prefer PDF or EPS

**Bibliography**:
- Use `\cite{key}` (numbered by default)
- .bib file with BibTeX

**Page limits**: No hard limit, but 30-40 pages is typical. Very long papers may require justification.

**Revision**: Upload revised manuscript + detailed response to reviewer comments.

---

## Communications in Mathematical Physics (CMP)

### Submission Portal

- **Website**: https://www.springer.com/journal/220
- **Submission**: https://www.editorialmanager.com/cmp/
- **Scope**: Mathematical foundations of physics, axiomatic QFT, geometric QM, NCG

### Document Class

CMP does not mandate a specific document class. Use standard article:

```latex
\documentclass[11pt,a4paper]{article}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}

\title{Spectral Anatomy of the Dirac Operator
        on Jensen-Deformed SU(3)}

\author{Author One\thanks{e-mail: [email redacted]} \\
        Dept. Physics, University A, City \\
        \and
        Author Two \\
        Dept. Mathematics, University B, City}

\date{\today}

\begin{document}

\maketitle

\begin{abstract}
Detailed mathematical analysis of the Dirac spectrum...
[250-400 words, can include equations]
\end{abstract}

\section*{PACS numbers}
11.15.Ex, 02.30.Sa

\section{Introduction}
...

\end{document}
```

### CMP Specifics

**Theorem environments**:
- CMP has specific styles; use `amsthm`
- Number theorems within sections: Theorem 1.1, 1.2, etc.

**Figures**:
- Black and white preferred (color costs extra)
- 84 mm width (single column format)
- PDF or EPS only

**Bibliography**:
- Manual entry preferred (no external .bib files in final version)
- Or use BibTeX, provide .bbl

**Rigor**:
- Complete proofs required (or clear reference to lemmas)
- All claims must be justified
- Heavy mathematical notation expected

---

## Theorem and Proof Environments

### Standard amsthm Setup

```latex
\usepackage{amsthm}

% CMP and JGP both use these styles
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}

% Use in document
\begin{theorem}[Block-Diagonality of $D_K$]
\label{thm:block-diag}
The Dirac operator $D_K$ on SU(3) is exactly block-diagonal
in the Peter-Weyl basis.
\end{theorem}

\begin{proof}
By left-invariance, $[J^a, D_K] = 0$ for all generators.
By Schur's lemma, block-diagonality follows.
\end{proof}
```

### Numbering Styles

**CMP preferred**: Theorem 1.1, 1.2, 2.1 (number within section)

```latex
\newtheorem{theorem}{Theorem}[section]
% produces: Theorem 1.1, 1.2, 2.1, ...
```

**Alternative**: Continuous numbering (Theorem 1, 2, 3, ...)

```latex
\newtheorem{theorem}{Theorem}
% produces: Theorem 1, 2, 3, ...
```

---

## Proof Structure and Rigor

### Complete Proof Example

```latex
\begin{theorem}[KO-Dimension Classification]
The spectral triple $(C^{\infty}(\text{SU}(3)),
L^2(\text{SU}(3)) \otimes S, D_K)$ has
real K-theory dimension (KO-dimension) equal to 6 modulo 8.
\end{theorem}

\begin{proof}
We recall the KO-dimension classification theorem [CNC97].
For a spectral triple $(A, \mathcal{H}, D)$ with Hilbert space
$\mathcal{H} = H_+ \oplus H_-$, the KO-dimension is determined
by the spinor dimension and the grading operator.

The spinor space over SU(3) has real dimension 16 = 2^4.
This corresponds to a Clifford module of rank 4 (complex dimension).
By the Atiyah-Singer classification, a complex manifold of complex
dimension 3 with spinors of dimension 2^3 = 8 (per spinor rep)
has KO-dimension $3 \pmod{8}$ for even spinor count, or
$6 \pmod{8}$ for odd spinor count.

SU(3) admits a unique irreducible spinor representation of dimension 8
[Nak96]. The two chiralities give total dimension 16.
This fixes KO-dimension = 6 modulo 8.

For verification, we compute the heat kernel expansion to
$O(t^3)$ and confirm all terms are consistent with KO-dim 6
[Session 20a computation]. [Detailed reference]
\end{proof}
```

### Avoid "Obvious" or "Clear"

**Bad**: "Clearly, $[D_K, J^a] = 0$ by left-invariance."
**Good**: "By left-invariance, $[D_K, J^a] = 0$. [Proof: For any left-invariant vector field $J^a$, the Dirac operator... ]"

---

## Reference Formatting

### JGP (Elsevier/BibTeX)

```bibtex
@article{Connes2006,
  author = {Connes, Alain},
  title = {Noncommutative Geometry and Physics},
  journal = {Rev. Mod. Phys.},
  volume = {79},
  number = {4},
  pages = {976--1041},
  year = {2006},
  doi = {10.1103/RevModPhys.79.976}
}

@book{Wald1984,
  author = {Wald, Robert M.},
  title = {General Relativity},
  publisher = {University of Chicago Press},
  address = {Chicago, IL},
  year = {1984}
}
```

### CMP (Springer/Manual)

In text: `\cite{Connes06}` produces [1], [2], etc.

Bibliography entry (manual):

```latex
\begin{thebibliography}{99}

\bibitem{Connes06}
  Connes, A.: Noncommutative Geometry and Physics.
  \textit{Rev. Mod. Phys.} \textbf{79}(4), 976--1041 (2006).
  DOI 10.1103/RevModPhys.79.976

\bibitem{Wald84}
  Wald, R.M.: \textit{General Relativity}.
  University of Chicago Press, Chicago (1984)

\end{thebibliography}
```

**Format**: Author(s), Title, Journal/Publisher, Volume (Issue), Pages, Year. DOI.

---

## Submission Workflow

### Pre-Submission Checklist (Both JGP and CMP)

- [ ] Manuscript is original and not under review elsewhere
- [ ] All authors agree to submission
- [ ] Compile with pdflatex locally; verify output
- [ ] All figures included and labeled
- [ ] All references complete (no [?] or missing DOIs)
- [ ] Affiliation and contact info correct
- [ ] 1-2 suggested reviewers (names + emails)
- [ ] Paper length reasonable (20-50 pages for mathematical papers)

### Submission Process

1. **Create account** at Editorial Manager (JGP or CMP)
2. **Upload files**: paper.tex (+ .bbl if applicable) + figures
3. **Enter metadata**:
   - Title (≤ 200 characters)
   - Abstract (300-400 words)
   - Keywords (5-10)
   - Suggested reviewers
   - Conflict of interest statement
4. **Submit** and receive confirmation email

### Typical Timeline

- **Submission**: Day 0
- **Editorial screening**: Days 0-5 (rejection if out of scope)
- **Reviewer assignment**: Days 5-10
- **Review period**: Weeks 2-8 (typically 4-6 weeks)
- **Decision**: Week 8
  - Accept (rare on first submission)
  - Major revisions (common): resubmit within 3 months
  - Minor revisions (less common): resubmit within 1 month
  - Reject (if fundamental flaws)

### After Reviewer Decision

If "Revisions Required":
1. Revise manuscript addressing each comment
2. Write **detailed response letter** (1-2 pages per major comment)
3. Upload revised .tex + figures + response letter
4. Resubmit (typically within 3 months)

Example response format:

```
Reviewer 1, Comment 1:
"The block-diagonality proof lacks detail in step 3."

Response:
We have expanded Section 3.2 with additional steps.
In particular, we now prove the Schur's lemma application explicitly
[lines 95-110 in revised manuscript]. The key step uses
the fact that the left-invariant derivative $[J^a, D_K] = 0$
restricts $D_K$ to representation-preserving maps, forcing
the block structure by irreducibility of SU(3) reps.
```

---

## Strategic Considerations: JGP vs CMP

### Choose JGP if:
- Paper emphasizes geometric aspects (differential forms, curvature, metrics)
- Cosmology/GR applications are important
- Paper is 20-30 pages
- First-time submission (typically faster decision)

### Choose CMP if:
- Paper is primarily mathematical (spectral theory, C*-algebras, NCG)
- High rigor standards expected
- Paper is 30-50+ pages
- You want publication in a top-tier mathematical physics venue

### The Phonon-Exflation Choice

**No-go paper** (V_spec monotone):
- More suitable for JGP (emphasizes KK geometry + cosmology)
- Faster review timeline

**Spectral Anatomy paper** (block-diagonality, KO-dim):
- More suitable for CMP (pure mathematical physics)
- Higher prestige but longer review

---

## Post-Acceptance

### Proofs and Copyediting

After acceptance:
1. Elsevier/Springer sends proofs (PDF)
2. You have 48-72 hours to review and approve
3. Provide corrections via web form (no rewriting)
4. Paper goes to print

### Open Access

Both JGP and CMP offer open-access options (author fees):
- **JGP**: Elsevier open access costs vary (~$2500 USD)
- **CMP**: Springer open access costs vary (~$3000-4000 USD)

Many universities have agreements with Elsevier/Springer to cover author fees.

### Preprint vs Published

- Post **preprint** (arXiv version) freely on arXiv
- Post **published** version only if your institution has open access agreement
- Always cite the published DOI as the "official" reference

---

## Common Pitfalls

1. **Insufficient rigor**: CMP reviewers reject vague proofs. Every claim must be justified.
2. **Overclaimed results**: "We prove X works" when you've only shown one case. Be precise.
3. **Poor writing**: Even great math is rejected if unreadable. Peer edit before submission.
4. **Missing references**: Not citing relevant prior work (shows lack of literature review).
5. **Long appendices**: Put proofs in main text or acknowledge they're in supplementary material.

---

## Professional Standard Paragraphs

### Opening Motivation Paragraph

"The spectral action principle of noncommutative geometry [Connes97, Chamseddine07] provides a unified framework for unifying geometry with quantum mechanics. Central to this framework is the spectral triple $(A, \mathcal{H}, D)$, where the Dirac operator $D$ encodes the metric and quantum structure. In the context of Kaluza-Klein geometry on compact Lie groups, the spectrum of $D$ determines the particle masses and coupling constants [Paasch20]. We investigate how deformations of the metric affect this spectrum, with applications to cosmology."

### Conclusion Paragraph

"We have established that the spectral action on Jensen-deformed SU(3) exhibits monotone behavior in the deformation parameter, precluding Starobinsky-type inflation mechanisms. This result does not render the spectral action framework unviable, but rather suggests that additional non-perturbative physics or alternative geometric structures are required for cosmological stability. Future research should explore [Mechanism A], [Mechanism B], and [Mechanism C] as potential resolutions. The mathematical tools developed here—[specific theorem or technique]—may have broader applications to [related area]."

---

## Connection to Phonon-Exflation Framework

Publishing in JGP/CMP enables:
- Peer review by world-class mathematical physicists (NCG specialists, differential geometers)
- Permanent archive with DOI and long-term visibility
- High-impact venue for mathematical contributions
- International recognition of rigor and novelty
- Foundation for follow-up papers and PhD research
- Professional standard for the phonon-exflation project's mathematical reputation

Relevance to Project: **CRITICAL** - CMP/JGP are the publication standard for mathematically rigorous physics work.
