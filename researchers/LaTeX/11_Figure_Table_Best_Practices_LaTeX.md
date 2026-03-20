# Professional Figures and Tables in LaTeX

**Author(s):** Matplotlib developers, pgf/pgfplots community, Figure Best Practices
**Year:** 2020+ (contemporary standards)
**Reference:** Matplotlib documentation, pgfplots manual, "Effective Scientific Figure Design" (Franconeri et al.)

---

## Abstract

Publication-quality figures and tables are essential for communicating quantitative results. This document covers figure preparation: matplotlib-to-pgf pipeline, subfigures, color-blind-safe palettes, publication resolution, table formatting with booktabs and siunitx, units and precision display, and journal-specific requirements. Emphasis is placed on embedding figures into LaTeX reproducibly and ensuring accessibility for all readers.

---

## Historical Context

Early scientific figures were printed photographs or hand-drawn illustrations. Modern computational science produces figures from data files. The challenge: generate figures at publication quality, reproducibly, and in a format that integrates seamlessly with LaTeX. matplotlib (2003-) became the standard for scientific Python plotting. The pgf backend (2008+) allows matplotlib to export directly to LaTeX-compatible PGF format, enabling publication figures that match the document's fonts and typography.

For phonon-exflation: Eigenvalue spectra, phase diagrams, and numerical results require high-quality figures suitable for review by mathematicians (CMP, JGP) and physicists (PRD, JHEP).

---

## Matplotlib-to-PGF Pipeline

### Python Script Setup

```python
import matplotlib
matplotlib.use('Agg')  # or 'pgf' for direct PGF export
import matplotlib.pyplot as plt
import numpy as np

# Data
tau = np.linspace(0, 0.5, 100)
lambda_1 = 1.207 + 0.3 * tau  # simplified eigenvalue flow
lambda_2 = 0.3 + 0.15 * tau

# Figure with PGF backend
plt.rcParams['pgf.texsystem'] = 'pdflatex'
plt.rcParams['pgf.preamble'] = r'\usepackage{amsmath}\usepackage{amssymb}'
plt.rcParams['font.serif'] = ['Computer Modern']

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(tau, lambda_1, 'b-', linewidth=2, label=r'$\lambda_1(\tau)$')
ax.plot(tau, lambda_2, 'r--', linewidth=2, label=r'$\lambda_2(\tau)$')

ax.set_xlabel(r'Deformation parameter $\tau$', fontsize=12)
ax.set_ylabel(r'Eigenvalue $\lambda_n(\tau)$', fontsize=12)
ax.set_title(r'Dirac Spectrum on SU(3)', fontsize=14)
ax.legend(fontsize=11)
ax.grid(True, alpha=0.3)

# Export to PGF (LaTeX-compatible)
fig.savefig('spectrum.pgf', bbox_inches='tight')
# or to PDF for submission
fig.savefig('spectrum.pdf', bbox_inches='tight', dpi=300)

plt.close()
```

### Compiling PGF Figures in LaTeX

```latex
\usepackage{pgf}
\usepackage{pgfplots}

\begin{figure}
\centering
\input{spectrum.pgf}
\caption{Eigenvalue flow with PGF-embedded matplotlib figure.}
\label{fig:spectrum}
\end{figure}
```

The `.pgf` file contains all LaTeX commands; fonts and math are rendered by LaTeX, ensuring consistency.

---

## Color-Blind-Safe Palettes

Approximately 8% of males and 0.5% of females have color blindness (red-green most common).

### Standard Color Blindness-Safe Palette

```python
# Okabe-Ito palette (universally recommended)
okabe_ito = {
    'orange': '#E69F00',
    'sky_blue': '#56B4E9',
    'green': '#009E73',
    'yellow': '#F0E442',
    'blue': '#0072B2',
    'vermillion': '#D55E00',
    'purple': '#CC79A7'
}

plt.plot(tau, lambda_1, color=okabe_ito['blue'], linewidth=2)
plt.plot(tau, lambda_2, color=okabe_ito['vermillion'], linewidth=2)
```

### Python: Colorblind-Safe Plotting

```python
import matplotlib as mpl
from colorspacious import cspace_convert

def colorblind_palette(n, colorspace='sRGB255'):
    """Generate n colors safe for color-blind vision."""
    hues = np.linspace(0, 360, n+1)[:-1]
    colors = []
    for hue in hues:
        rgb = cspace_convert({'HSV': [hue, 70, 70]}, 'HSV255', 'sRGB255')
        colors.append(tuple(c/255 for c in rgb))
    return colors

# Usage
colors = colorblind_palette(4)
for i, (tau_val, lambda_val) in enumerate(data):
    plt.plot(tau_val, lambda_val, color=colors[i])
```

### Alternative: Use Different Line Styles

Instead of relying on color alone:

```python
plt.plot(tau, lambda_1, 'b-', linewidth=2.5, label=r'$\lambda_1$')
plt.plot(tau, lambda_2, 'b--', linewidth=2.5, label=r'$\lambda_2$')  # dashed
plt.plot(tau, lambda_3, 'b:', linewidth=2.5, label=r'$\lambda_3$')   # dotted
```

Combine color + line style + marker combinations.

---

## Figure Resolution and Format

### Resolution Standards

- **Screen/PDF viewing**: 96-150 DPI (sufficient)
- **Print (journal submission)**: 300 DPI minimum, 600 DPI for line art
- **arXiv/preprint**: 150-300 DPI acceptable

```python
# High-resolution export
fig.savefig('spectrum.pdf', dpi=600, bbox_inches='tight')
fig.savefig('spectrum.png', dpi=300, bbox_inches='tight')  # avoid PNG for paper
```

### Preferred Formats

| Format | Use Case | Notes |
|--------|----------|-------|
| PDF | Primary (vector) | Lossless, scalable, publication standard |
| EPS | Legacy, journal requirements | Encapsulated PostScript |
| PNG | Web/presentations | Lossy if compressed |
| PGF | LaTeX integration | Vector, embedded directly in .tex |
| TIFF | High-resolution archive | 300-600 DPI for long-term storage |

---

## Subfigures and Layouts

### Using subcaption Package

```latex
\usepackage{subcaption}

\begin{figure}
\centering
\begin{subfigure}{0.45\textwidth}
  \includegraphics[width=\textwidth]{round_spectrum.pdf}
  \caption{(a) Round metric}
  \label{fig:round}
\end{subfigure}
\hfill
\begin{subfigure}{0.45\textwidth}
  \includegraphics[width=\textwidth]{jensen_spectrum.pdf}
  \caption{(b) Jensen-deformed metric}
  \label{fig:jensen}
\end{subfigure}
\caption{Eigenvalue spectra for two metric choices on SU(3).
  The Jensen deformation increases the first eigenvalue gap
  by approximately 28\% at $\tau = 0.2$.}
\label{fig:metrics-comparison}
\end{figure}
```

### Gridded Layout

```latex
\begin{figure}
\centering
\begin{tabular}{cc}
  \includegraphics[width=0.45\textwidth]{fig_a.pdf} &
  \includegraphics[width=0.45\textwidth]{fig_b.pdf} \\
  (a) Round metric & (b) Jensen-deformed \\
  \includegraphics[width=0.45\textwidth]{fig_c.pdf} &
  \includegraphics[width=0.45\textwidth]{fig_d.pdf} \\
  (c) Block-diagonal D_K & (d) Eigenvalue flow \\
\end{tabular}
\caption{Summary of spectral properties...}
\end{figure}
```

---

## Table Formatting with booktabs

The `booktabs` package provides professional table formatting:

```latex
\usepackage{booktabs}

\begin{table}
\centering
\begin{tabular}{lrrrr}
\toprule
$\tau$ & $\lambda_1(\tau)$ & $\lambda_2(\tau)$ & Gap & $a_4/a_2$ \\
\midrule
0.00 & 1.207 & 0.325 & 0.882 & 1000.0 \\
0.10 & 1.310 & 0.375 & 0.935 & 950.5 \\
0.20 & 1.531 & 0.405 & 1.126 & 920.1 \\
0.30 & 1.644 & 0.480 & 1.164 & 915.2 \\
0.40 & 1.750 & 0.520 & 1.230 & 912.8 \\
\bottomrule
\end{tabular}
\caption{Spectral data and Seeley-DeWitt ratio. Data computed with
  $N=200$ basis functions and 500 mesh points on SU(3).}
\label{tab:spectral-data}
\end{table}
```

### Key booktabs Features

```latex
\toprule      % top border (thicker than normal)
\midrule      % mid border
\bottomrule   % bottom border
% No vertical lines (cleaner appearance)
```

---

## Units and Precision with siunitx

The `siunitx` package formats numbers consistently:

```latex
\usepackage{siunitx}

\begin{table}
\centering
\sisetup{round-mode=figures, round-precision=3}
\begin{tabular}{lS[table-format=1.3] S[table-format=3.0]}
\toprule
Parameter & \multicolumn{1}{c}{Value} & \multicolumn{1}{c}{Unit} \\
\midrule
Mass (electron) & 9.1093837015e-31 & kg \\
Planck constant & 6.62607015e-34 & J·s \\
Fine structure & 0.00729735256 & (dimensionless) \\
\bottomrule
\end{tabular}
\end{table}

% In text:
The fine structure constant is \SI{1/137}{\dimensionless}.
The electron mass is \SI{0.511}{\mega\electronvolt\per\clight\squared}.
```

---

## Caption Strategy

### Good Caption

Complete, self-contained, readable without the figure:

```latex
\caption{Eigenvalue spectrum $\lambda_n(\tau)$ of the Dirac operator
  $D_K$ on SU(3) as function of Jensen deformation parameter
  $\tau \in [0, 0.5]$. (a) Round metric: $\lambda_1$ (blue solid)
  increases from 1.207 to 1.800. (b) Fermionic vs bosonic spectrum:
  ratio $\lambda_{\text{ferm}}/\lambda_{\text{bos}}$ (red dashed)
  decreases, indicating fermion-dominated gap at $\tau > 0.2$.
  Data computed at $N=200$ with $\Delta \tau = 0.001$.
  Block-diagonality of $D_K$ (proven in Theorem 1)
  enables sector-specific analysis.}
\label{fig:spectrum-flow}
```

### Bad Caption

Vague or incomplete:

```latex
\caption{Eigenvalue plot.}  % Unclear what is plotted
```

---

## Journal-Specific Figure Requirements

### Physical Review D (PRD)

- **Format**: PDF preferred, EPS acceptable
- **Resolution**: 300 DPI for final submission
- **Size**: Single-column ≤ 3.5 inches, two-column ≤ 7 inches
- **Fonts**: Use standard fonts (Computer Modern, Times)
- **Color**: Accepted, but should be readable in B/W

### JHEP (Springer)

- **Format**: PDF, EPS, TIFF
- **Resolution**: 300 DPI minimum
- **Size**: Up to 80 mm width
- **Captions**: Below figure (standard); table captions above
- **Color**: Accepted

### Journal of Geometry and Physics (Elsevier)

- **Format**: PDF, EPS, JPEG
- **Resolution**: 300 DPI
- **Size**: Single-column only (≤ 8 cm)
- **Color**: First 2 color figures free, additional charged

### Communications in Mathematical Physics (Springer)

- **Format**: PDF, EPS
- **Resolution**: 600 DPI for line art
- **Captions**: Below figure
- **Color**: B/W preferred; color figures charged

---

## Advanced: Automated Figure Generation

### Python Script with Data File Input

```python
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import sys

# Read data file
data = np.loadtxt('spectrum_data.txt', skiprows=1)
tau = data[:, 0]
lambda_1 = data[:, 1]
lambda_2 = data[:, 2]

# Create figure
plt.rcParams['pgf.texsystem'] = 'pdflatex'
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(tau, lambda_1, 'b-', linewidth=2.5, label=r'$\lambda_1(\tau)$')
ax.plot(tau, lambda_2, 'r--', linewidth=2.5, label=r'$\lambda_2(\tau)$')

ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Eigenvalue', fontsize=12)
ax.legend()

fig.savefig('spectrum_auto.pdf', bbox_inches='tight', dpi=300)
print("Figure saved: spectrum_auto.pdf")
```

Run before LaTeX compilation:
```bash
python3 generate_figures.py
pdflatex paper.tex
```

---

## Common Pitfalls

1. **Low resolution**: Submitting 72 DPI PNG instead of 300 DPI PDF.
2. **Tiny fonts**: Figure fonts too small relative to caption text.
3. **Color-blind inaccessibility**: Using red-green only to distinguish data.
4. **Missing captions**: Figures referenced but not explained.
5. **Large file sizes**: Uncompressed TIFF instead of compressed PDF.
6. **Inconsistent styling**: Fonts, colors, line widths vary across figures in same paper.

---

## Checklist Before Submission

- [ ] All figures in PDF format at 300 DPI (600 for line art)
- [ ] Fonts in figures match document fonts (Computer Modern)
- [ ] Color palette is color-blind safe (Okabe-Ito or distinct line styles)
- [ ] Captions are complete and self-contained
- [ ] Figure numbers referenced in text ("see Figure 1")
- [ ] All axes labeled with units
- [ ] Legend present where needed
- [ ] File sizes reasonable (<5 MB per figure)
- [ ] PGF figures embed correctly in PDF preview

---

## Connection to Phonon-Exflation Framework

Professional figure preparation enables:
- High-quality publication of eigenvalue spectra and phase diagrams
- Color-blind accessibility for broad physics community
- Automated figure regeneration if numerical data updates
- Reproducible science (figures generated from code and data, not WYSIWYG editors)
- Consistent styling across multi-author papers
- Professional appearance in peer review process
- Acceptance by all major journals (PRD, JHEP, CMP, JGP)

Relevance to Project: **HIGH** - Figures are often the first thing reviewers examine; quality figures improve acceptance probability.
