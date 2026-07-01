---
name: S62 All Results
description: S62 consolidated -- cutoff-london PASS, Higgs BCS/sigma INFO, BDG gauge fraction INFO, Pati-Salam INFO
type: project
---

## S62 Gate Results

### CUTOFF-LONDON-62: PASS (2/6 families)
- Gaussian: gamma_opt=0.488, f_0=9.817, f_2=2.34, f_4=0.558, alpha_GUT=1/25. PASS.
- Exponential: gamma_opt=0.345, f_4=1.673. PASS.
- Erfc/Poly: outside [0.10,0.50]. INFO.
- Lorentzian/Butterworth: f_4 < 0.413. FAIL.
- Structural: f_0 free (normalization), f_2 fixes gamma, Cauchy-Schwarz f_4>=f_2^2/f_0 auto-exceeds threshold.
- **Canonical**: Gaussian gamma=0.488, f_0=9.817, f_2=2.34, f_4=0.558 for downstream computations.

### HIGGS-BCS-THRESHOLD-62: INFO
- Tree m_H=134 -> 190 GeV after 2-loop RG (reproduces CCM overshoot). BCS screening 3583x too small.
- delta_BCS(direct)=7.46e-5. For m_H=125: delta=0.267 (27% g_3 reduction needed).
- Conclusion: KK threshold corrections required, not BCS screening.

### HIGGS-SIGMA-62: INFO
- r^2=1.7435 (tachyonic ALL tau). BCS correction 2.60e-4 (negligible).
- V(sigma) monotonically increasing (discriminant=-78.44). Classical KK moduli problem.
- Stabilization needs Casimir or flux (beta<=4 works with c_Cas~6.5).

### BDG-GAUGE-FRACTION-62: INFO
- gauge/gravity = 2.723. S61 error found (R/12->5R/12 in a_4 cross-term).
- Formula: (a_2/a_4)*[5R/12 + (1/2)*<|D|^4>/<|D|^2>]. Linear 74.6%, quadratic 25.4%.
- Cutoff-independent (Gilkey coefficients). Nambu doubling cancels in ratio.

### PATI-SALAM-EXTENSION-62: INFO
- a_4^PS/a_4^SM = 1.404. Fold stability maintained (36x margin). Gauge: 12 SM + 9 PS quadratic.
- m_H tree: PS 96.3 GeV (= SM/sqrt(2)). sin^2 1-loop: 0.207 (10% off, 2-loop needed).
- PS does NOT break monotonicity wall, NOT fix order-one 4.000. DOES embed 169 quadratic directions.
