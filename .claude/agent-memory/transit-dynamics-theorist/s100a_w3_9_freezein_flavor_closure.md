---
name: s100a-w3-9-freezein-flavor-closure
description: S100a W3-9 FAIL — transit squeezed-vacuum freeze-in is NOT an over-constrained predictor of SM flavor; corridor closed cleanly (Track B 0.90); structural reasons + fitted S0=1.6942 pinned
metadata:
  type: project
---

# S100a W3-9 — FREEZEIN-OVERCONSTRAINED: dynamical-freeze-in flavor corridor CLOSED

**Verdict**: FAIL (sign=PASS / magnitude=FAIL / regime=VALID), Track B 0.90. audit_sha256=78ee1d5677d75dc8…

**Why:** the S99 fermion-mass panel's falsifiable core ([[d,w],[w*,d]] freeze-in block, d_i = exp(−S0·C2), C2=(4/3,3,6) on (1,0)/(1,1)/(3,0)) was fit {S0,|w|} to lepton ratios + arg(w) to |V_us| and the ~12 held-out observables broke with gross misses in all three classes.

**Structural reasons (both forced, not numerical accidents):**
1. **J-conjugacy collision**: the ONLY zero-new-parameter up/down distinction is M_d = M_u* (BDI conjugate towers) ⟹ up/down spectra IDENTICAL (dev 0.0 exact) ⟹ m_u/m_d = m_c/m_s = m_t/m_b = 1 vs PDG 0.46→41.3. The mechanism that enables CKM (conjugate phases ±Θ) kills the up/down mass split.
2. **|w| hierarchy-vs-mixing tension**: hierarchy-preserving root needs |w| = 2.215e-4 ≪ d2 = e^{−3S0} = 6.2e-3; mixing angle t ≈ |w|/(d2−d3) = 0.036 caps |V_us| ≤ 2t|sinΘ| = 0.0717 < 0.225 (3.14× shortfall; anchor UNREACHABLE — Stage-B fit converges to π/2 boundary of achievable set).

**Fitted values (npz s100a_freezein_overconstrained.npz; HARD input of W3-10/W3-11):** S0_fit = 1.694153, |w|_fit = 2.215474e-4, arg_w_fit = +1.570918 (≈π/2). Diag-limit legs S0(μ/e) = 1.7772, S0(τ/μ) = 1.6934 — ONE S0 on the (4/3,3,6) grading reproduces BOTH lepton log-gaps to 5% (widening 9/5 = 1.800 vs observed 1.889), exactly with |w|. The lepton-sector SHAPE is the surviving strength.

**Near-hits worth remembering:** θ13 = 0.243° vs 0.219° (1.87σ — smallest CKM angle lands closest, pure conjugate-phase mismatch); m_c/m_u = 206.5 vs 589 (0.455 dex, in band); m_u/m_d in band. Sign-PASS: hierarchy DIRECTION correct in every tower (heavier rep = larger C2 = deeper freeze = lighter fermion; m_t/m_u_pred = 3473).

**Seed mismatch (diagnostic):** freeze-in |w| is 1843× smaller than the W2 static Yukawa-overlap |w| = 1/√6 — the dynamical inter-sector Bogoliubov coefficient is NOT the geometric overlap off-diagonal. min|Δθ| vs Z3 = π/6 exact.

**How to apply:** any future flavor-from-transit proposal must supply (a) an up/down distinction that is NOT pure J-conjugation (else spectrum-degenerate), and (b) a second mixing scale decoupled from the hierarchy-preserving |w|. The plan's FAIL_meaning routes the SHAPE carrier to geometric multiplicity-bundle distance (Item 8 lineage). Canonical structure D1–D5 (full-pairing 3x3, C2-descending mass map, lepton self-conjugate Z3 point, Λ_u=Λ_d J-locked, smallest-|w| root) is in the script docstring — reuse the declaration pattern.

**Method note:** the 2+1 split fit protocol (leptons → {S0,|w|}; |V_us| → arg w) REQUIRES w_lepton real (self-conjugate Z3 point π); a complex lepton w couples the system into a joint 3D solve. [[s77-synthesis]] for the A_s inversion analog of pre-registered FAIL = corridor map.

**W-3 carrier-workshop R2 outcome (2026-06-07, R2-transit landed; connes R2-B = final turn pending):** T2 double-counting audit ACCEPTED — √(d₁d₂) scaling is fit-structural (w² = shift·(d₂−d₁)·d₁, shift = 0.20677); off-diagonal's independent content = ONE number, coherence coefficient c_meas = 0.4533 vs Weingarten 1/√6 (+11%, zero params); "3.27 OOM → 1.37%" retired from verdict. Leg-A spec = connes cross-face assembly ℓ_geo = T_acoustic/(3τ_fold) = 0.196491 ALONE (my τ_fold form = pin-proximity shadow: 3τ_fold² ≈ T_acoustic, 3.3% miss; exits band under J-tilt). s̄-space PASS window [0.31615, 0.34956] M_KK²/C₂ — razor +0.13% above scalar-channel J(τ_fold)/3 = upper edge IS a Dirac-vs-scalar channel-universality test. NEW rank-one theorem: dressed texture M = (1+c)·diag(d) − c·uu†, u_i = √d_i e^{iφ_i}; secular eq 1 = c·Σd_i/((1+c)d_i−λ); triangle cocycle Σθ_ij ≡ π ⟹ Z₃ phase menu = {all-π (lepton), {π,±2π/3} (quark)}; within-block phases = coboundaries ⟹ retro-explains arg(w) π/2 boundary-pinning. Deep-sudden predicts frozen c = bare c (no decoherence window, R_therm = 5252) ⟹ Leg-B ratio approaches 1 FROM ABOVE; upper-side miss has NO mechanism (purity-monotone). Leg B canonical form: {S₀,c} exact 2×2, all-π pin, bare-d_i. Quark partial prior pinned: C₂-descending per component + κ-triple (1.89/1.29/0.78) heavy-gen order; gen-1 inversion m_u/m_d = 0.46 = named burden. Verdict headline: Reading A twice-scoped = ONE OBJECT, THREE CHARTS.

**W-3 carrier-workshop R1 addendum (superseded by R2 above where they differ; T1–T6 anchors still valid):**
- **Dressing bridge (new, canonicity-UNCONDITIONAL inputs)**: |w|_fit = |w|_geom·√(d_gen1·d_gen2)×1.110 — i.e. C̄₂_eff = −ln(|w|_fit/|w|_geom)/S0_fit = 4.438 vs mean Cabibbo-pair Casimir (6+3)/2 = 4.5, dev 1.37%. The 1843× seed-vs-fit gap is production-coherence dressing (√(n_i n_j) two-mode-squeezed structure), NOT two objects. Bridge lives in C₂-graded variables; fails 3–5 OOM in floor-distance variables (additive 4.3e-9, Pythagorean 5.5e-7 vs measured 5.43e-4).
- **Pre-registered band (T1.0)**: zero-fit Connes-route S₀^geo PASS iff ∈ [1.609, 1.779] (±5% of S0_fit; = W3-11 tolerance = the freeze-in's own 4.95% leg spread); INFO ±5–15%. Floor stratum CLOSED for the test (per-leg ℓ_required split 0.022442/0.156632 = 6.979 = the fold compression); only tracial stratum live; τ=0 trace-mean slope = 1/3 frame-units EXACT ⇒ S₀^geo(τ=0) = (1/3)/ℓ_geo; ℓ_geo = τ_fold ⇒ 1.754 (+3.6%, in-band).
- **Knob degeneracy (T4)**: candidates (i) 4/3 (+0.65%) and (iii) τ_fold/T_acoustic = 95/56 (+0.13%) BOTH inside the S101-W3-S0-KNOB 0.01 band (degenerate because 2πτ_fold = 1.1938 ≈ 1.2); splitter is the graded-vs-scalar ω binary ((iii) ⟺ ω_g = C₂·τ_fold, resolves the W3-10 straddle; (i)/(ii) keep scalar Δω). E_A = 2π·S0_threshold IDENTITY ⇒ W3-10/W3-11 = ONE straddle vote.
- **Wall escape (T3)**: per-component functional splitting (Baptista eq 2.17; Ω^D = (8/3)I₃ ≠ Ω^c = (4/3)I₃ exact, W2-1) evades BOTH walls and is [J,D_K]=0-compatible (split is in functionals-of-towers, not operator conjugation). Quark envelope on that route UNCOMPUTED — routing: geometric per-component route owns quark/CKM; transit owns the dressed-texture zero-amplitude test (pair-resolved w_ij = (1/√6)√(d_i d_j)e^{iθ_ij}; today's single-w ratio 1.110, two-sided risk).
- **Regime argument**: deep-sudden (δt/T_L = 1.25e-5) ⇒ Bogoliubov = static symplectic overlaps ⇒ "dynamical vs geometric" is functional-choice on ONE operator pair, not a mechanism dichotomy (S100b W5-1 switch-dominance + W5-2 RANGE-controlled corroborate). ε_LX scope: carrier adjudication revises ENTRY provenance only, never the [[d,w],[w*,d]] FORM (W4-14 max_C = 0.0 protected).
