---
name: tau0-operator-is-levi-civita
description: S100b W3-2 — framework D_K at tau=0 is the LEVI-CIVITA (t=1/2) Dirac of the Lai-Teh family, NOT the Kostant cubic (t=1/3); conversion formulas + closed forms for all future bi-invariant comparisons
metadata:
  type: project
---

# Framework τ=0 operator = Levi-Civita point (t=1/2), NOT Kostant cubic (t=1/3)

S100b-TAU0-LAITEH-REDUCTION FAILed its cubic-point pre-registration with the STRUCTURED sub-case proven at machine epsilon (verdict: `computations/session-100b/s100b_gate_verdicts.txt`, audit bea5401ae1ac3c4d…; WP §W3-2 of `sessions/session-100b/session-100b-w3-workingpaper.md`).

**Why:** `dirac_spectrum.py` Module 3 builds the Levi-Civita spin connection: Ω = −(1/8)Σf̃_abcγγγ exactly (Kostant cubic needs −1/12). Three independent t=1/2 identifications: per-sector Thm-2.3 closed-form match 8.9e-15 (28 sectors), trivial-sector 27t² → t̂=0.500000000000, operator α=−1/8 exact. Cubic control Ω→(2/3)Ω passes Lai-Teh Thm 2.2 at ~7e-15 with κ=1/9 (eigensolver machinery itself is CORRECT).

**How to apply (forward rules for me):**
1. NEVER anchor framework τ=0 spectra on Lai-Teh Thm 2.2 (cubic). The correct τ=0 closed form is Thm 2.3 at t=1/2: on V_μ ⊂ S⊗V_(p,q) (S = 2V_ρ; μ per Lemma 2.6; block mult 2dim μ): `eig_LT = ½[poly(μ)+poly(V)] + 9/4` in (ρ,ρ)=3 units, frame units = LT/9; poly = p²+q²+pq+3p+3q = 3·C₂.
2. λ² = n/36 (PROVEN, atlas-07) is DERIVED: n = 2[poly(μ)+poly(V)]+9. Session-22's "λ² = C₂+3/4" = the μ=(p,q)-component row in 3× frame units.
3. At the cubic point a₂=a₄=a₆ ≡ 0 EXACTLY (single Λ⁸ heat term; Res_{z=4}ζ = 8√3π/243, r₃=r₂=r₁=0 exact rationals) — a cubic-point substrate has NO Einstein-Hilbert/Yang-Mills moment at τ=0. The framework's LC choice (twist (3t−1)(3t−2)|_{1/2} = −1/4) is what gives the fiber its a₂/a₄ channels. Load-bearing physics, not a defect.
4. Lai-Teh arXiv:1209.3812v2 Thm 2.1 printed row 8 carries a spurious +3(3t−1)(3t−2) away from t=1/3 and a wrong parameter range (p,q∈N vs Lemma 2.6's p,q≥1) — verified numerically (Thm-2.3 component matches at 2e-15; printed row off by 1.9e-2). Build per-sector references from Thm 2.3 + Lemmas 2.5/2.6, never from the printed Thm 2.1 row 8.
5. `compute_killing_form` returns +3I (= −Tr(adX adY)); its docstring "−3δ" is a sign slip; only |B| feeds the metric.
6. τ>0 catalog (s84 cache + downstream) = Jensen-deformed LC-family spectra — internally consistent, but flagged UNTRUSTED-as-cubic; LC-vs-cubic canonicity adjudication is a Q1-workshop carry-forward (S100b W3-2 CF).
7. Module conventions: D anti-Hermitian (eigenvalues ±i|λ|, γ₉ forces ± symmetry, per-sign block mult = 8dim exact); Lai-Teh counts the HALF-spinor module (their mult = 8dim² = 2u²v²(u+v)²; full-spinor = 2×); label map (u,v)=(p+1,q+1) with u²+uv+v² = 3C₂+3 exact.
