---
name: S84 W5-57 MU-K-CORRIDOR result
description: mu-distortion across K-corridor vs FIRAS; gamma=1 structural, max mu at K=3.556e5 is 8.69e-5 (PIXIE-visible, FIRAS PASS)
type: project
---

S84 W5-57 MU-K-CORRIDOR — INFO verdict.

**Result**: max_K mu(K) = 8.694901e-5 at K = 3.556e5; max mu/FIRAS = 0.9661.
Verdict INFO because mu_max falls in PIXIE-visible band [3e-5, 9e-5] while still satisfying FIRAS 9e-5.

**Why**: K-corridor is a structural one-parameter scan of the R3 band-weighted
squeezing amplitude. mu(K) is LINEAR in K (gamma = 1 to machine precision,
max log-residual 7e-15), which is a structural consequence of pulling the
K-amplitude out of a linear Chluba-kernel integral with fixed UV slope
alpha_S_IC = -2.192. Any deviation from gamma=1 would require K-dependent
alpha_S_IC, which is NOT in the pre-registered machinery.

**Key numbers**:
- mu(K=2.035) = 4.9758503926e-10 (feeds W5-65; bit-matches S82 canon to 7 digits)
- mu(K=3.556e5) = 8.694901e-5 (just 3.4% below FIRAS 9e-5)
- K_FIRAS = K_base * FIRAS/mu_base = 3.6808e5 (vs S_IC cap 3.556e5, 3.5% gap)
- gamma_fit = 1.0000000000 (max residual 7.11e-15 log-units)
- monotone increasing mu(K) across all 6 corridor probes (no internal minimum)

**How to apply**:
- W5-65 structural-identity test: K_FIRAS/K_S_IC^cap = 1.0351; W5-65 interprets
  whether this 3.5% gap is coincidence or structural.
- Corridor endpoint is PIXIE-falsifiable: PIXIE sensitivity ~3e-5 puts the
  K=3.556e5 prediction at 3-sigma detection threshold.
- Gate 65 K_FIRAS coincidence argument NOT truncated — FIRAS bound never
  violated across full corridor.
- gamma=1 is a permanent structural theorem: mu(K) linear in K across 5.24
  decades to machine precision. This is "no internal minimum" for the corridor.

**Closure SHA**: 73986af4d0557c10566673b78c16fa7ec31675c226f046026f66f775e90a011c
**Script**: computations/s84_w5_mu_k_corridor.py
**Data**: computations/s84_w5_57_data.npz
**Plot**: computations/s84_w5_57_plot.png
