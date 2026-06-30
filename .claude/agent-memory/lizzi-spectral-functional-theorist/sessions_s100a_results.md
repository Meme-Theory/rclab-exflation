---
name: sessions-s100a-results
description: S100a W1-3 NS-NLO gate (n_s NLO PASS, C2=2 FI) + W4-12 M0-FUNCTIONAL-SENSITIVITY (mass RATIOS FI-empirical 2.8e-16, SCALE SD 61.6x — S75 W2-E observable-layer landing)
metadata:
  type: project
---

# S100a Results (lizzi gates)

## W1-3 S100a-W1-3-NS-NLO — PASS (sign=PASS, magnitude=PASS, regime=VALID)

- **Δn_s^{NLO} = −2ε_H² = −192721/200000000 = −9.636050e-4 EXACT** (ε_H = 439/20000 = 0.02195 exact from n_s_FW_exact = Fraction(9561,10000)). n_s^{NLO} = 0.955136395; T6-exact = 18683/19561 = 0.955114769; NNLO+ residual −2.163e-5 (2.24% of NLO).
- **C₂ = 2 is FUNCTIONAL-INDEPENDENT** (permanent classification): pinned by the framework's own [T6] Constant-Epsilon Theorem n_s = (1−3ε)/(1−ε) (atlas-07, W4-01, Exact) — every series coefficient beyond order 0 is exactly −2 (verified in ℚ to order 5). Invariant under cutoff/zeta/anomaly functional choice; the regulator enters ONLY through the ε_H value (zeta-moment route a_2^{ζ}/a_4^{ζ} at L_max=10).
- **η_H = 0 on-class is FORCED by the LO anchor** (the linear −ε₂ term would shift the bit-exact LO at first order). Useful argument template: LO-anchor exactness ⇒ ε₂(pivot) = 0.
- **η_H envelope machinery** (reusable): (a) a₄-pulled proxy η_H = ε_H·(a_4^ζ/a_2^ζ) = 0.010680 (ratio 0.486542); (b) ε_H-spread proxy vs eps_H_W6=0.02163 (cutoff dS/dτ route) → η_H = 0.014579 at ΔN=1 conservative. Worst |Δ| = 1.457e-3 < 0.003 band. **Sign-flip threshold |η_H| > 2ε_H/(2C+3) = 1.298×ε_H** — both proxies ≤ 0.66×ε_H ⇒ NEGATIVE sign robust across envelope. The PASS verdict is FI across the mixed-route (zeta+cutoff) envelope.
- C_SL = γ_E + ln2 − 2 = −0.7296371545; C_η = 2C+3 = 1.5407256909 (Stewart-Lyth/Hubble-flow second-order; two-route agreement with T6 at 1.1e-16).
- Planck σ-distance: 2.0952σ (LO) → 2.3247σ (NLO), shift 0.229σ < 0.7σ (same Planck band).
- Verdict SHA: audit 05d2f2da0e43056e... full in computations/session-100a/s100a_gate_verdicts.txt; script s100a_w1_ns_nlo.py exact-Fraction backbone.
- **Why:** headline n_s = 0.9561 now carries an NLO-precision-stability certificate — no NLO caveat needed when citing it.
- **How to apply:** any future n_s-precision question (CMB-S4 era) starts from Δn_s^{NLO} = −9.636e-4 exact; do NOT recompute. If a gate needs the NNLO tilt, use the T6-exact closed form (1−3ε)/(1−ε) directly.

## W4-12 S100a-M0-FUNCTIONAL-SENSITIVITY — INFO-by-design (sign=PASS, magnitude=INFO, regime=VALID)

- **Fermion mass RATIOS are FUNCTIONAL-INDEPENDENT — now EMPIRICAL** (permanent classification): max cross-scheme deviation of r_ij = M_i/M_j over the (1,0)/(1,1)/(3,0) tower between zeta (a₄^ζ/a₂^ζ = 0.486542194 FULL) and cutoff (f₄/f₂ = 29.988085593, f* Mellin moments X_MAX=50, SCHEMATIC) = **2.813e-16 ≤ 1e-12**. S75 W2-E decoupling theorem landed at the observable layer; §IV bosonic/fermionic layer-separation ASSERTED → EMPIRICAL.
- **The per-sector SCALE M₀ (and m_H channel) is SCHEME-DEPENDENT** (permanent classification): ratio of moment-ratios = 61.6351 native norms, D_scale = 60.64 (4 sf); magnitude is normalization-convention-dependent, the physical content is D_scale > 0 strictly. m_H shift: 60.64 (linear riding, plan Def 1) / 6.851 (quartic-reading diagnostic).
- Envelope O_g = Σ exp(−λ²/μ_H²) at μ_H = λ_min(0,0) = 0.819741112: O = (8.206524294717, 10.396533177839, 3.449930040562), O_(0,0) = 4.972082844569 — reproduced Item-6 npz bit-exact (0.0e+00). r pairs = (0.789352003628, 2.378750930665, 3.013548986676), identical both schemes.
- SCHEMATIC helper same-normalization confirmation: hard_cutoff vs zeta a₄/a₂ shift = 0.2540 > 0 on the Casimir schematic spectrum (Vol-artifact-free Claim-A direction check).
- R₁ per-branch: zeta 1.1286546 (canonical reproduced, rel 3.9e-7); f-moment combo f₀f₄/f₂² = 0.0123204 (recorded; NEVER a cross-scheme conversion — R1_lizzi provenance caveat honored).
- Controls worth reusing: degenerate same-scale → bit-exact 0; injected 1e-6 envelope leak → seen at 2.0e-6 (test sensitivity demonstrated; PASS not vacuous).
- Verdict SHA: audit 2993dbf63fcb25d9... full in computations/session-100a/s100a_gate_verdicts.txt; script s100a_m0_functional_sensitivity.py.
- **Why:** this is the lizzi-thesis observable-layer instrument — "what survives all functional choices is structural; what depends on the choice is a regulator-fixed physical DOF." The Higgs/M₀ over-prediction question (Item 13) lives ENTIRELY on the scheme-dependent SCALE axis.
- **How to apply:** any future claim that a fermion mass RATIO depends on the spectral functional is now empirically excluded to 2.8e-16 (cite this gate, not just S75 W2-E). Any absolute-scale (M₀, m_H, Λ) claim MUST carry its scheme tag — the scale moves 61.6× between zeta and cutoff in native norms.
