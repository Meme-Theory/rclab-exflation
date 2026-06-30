---
name: inv12-modular-selection-fail
description: INV12-W1-1 FAIL — the faithful-normal modular weight omega does NOT extremize S_modular at tau_fold; the 5th failed substrate-derived functional-selection principle
metadata:
  type: project
---

INV12-W1-1-MODULAR-FUNCTIONAL-EXTREMIZATION closed **FAIL** (investigation-12, 2026-06-17). The candidate substrate-derived SELECTION principle for the spectral functional — does the framework's own faithful normal modular weight ω (§VII.BZ / K12, S105 STAGE-3-PERMANENT) extremize S_modular(τ) = Tr(D_K(τ)² ρ_ω) at τ_fold = 0.190? — is **falsified**: S_modular is MONOTONE INCREASING through the fold (dS/dτ|_fold = +0.7821, |dS/dτ|/S_scale = 0.552 ≈ 552× the 1e-3 PASS-band, sign +1 on BOTH sides, no sign-change bracket).

**Why this matters**: this is the FIFTH failed substrate-derived functional-selection principle. The four of F-STAR-SELF-CONSISTENCY (S76) + the modular weight ω of this gate. The framework's commitment of the n_s functional to pure √x (S103) remains **cornered-by-elimination, NOT forced** — no substrate principle yet selects it. The G-L1 selection gap stays open.

**How to apply**: cite this whenever a future gate proposes "the modular weight selects the functional / the fold" or revives the GGE-ENTROPY-FUNCTIONAL-as-V.P. channel (session-84 OPEN; §W8a-85 ran only the Chamseddine-Connes meta-reformulation, NOT the modular V.P.). The modular-weight corridor is now closed. Consistent with S106 GEM: ω' is bulk-faithful but carries no area-clock (2b INFO) — "no area-clock" and "no V.P. stationarity at the fold" are the same structural fact (modular flow does not pin τ_fold).

**Classification (permanent)**: the FAIL is **scheme/regulator-PERMANENT**, not scheme-dependent. The stationarity test reads the sign of the ω-weighted eigenvalue-velocity sum Σ_k |λ_k| |λ_k|′ w_k; on this branch every |λ_k|′ > 0 (eigenvalues uniformly grow with τ), so the sum is strictly positive regardless of the modular weight's normalization. Changing the regularization does not flip a sign that is forced by the eigenvalue trajectory monotonicity. The modular weight w_k = ρ_ω diagonal is the BdG occupation f ∈ (0.1572, 0.4345) (faithful, 0<f<1) on the 4 horizon blocks (0,0)/(1,0)/(0,1)/(1,1); it is read OFF the substrate (S105 npz), zero free parameters — and still does not extremize at the fold.

**Artifacts**: `computations/investigation-12/inv12_w1_1_modular_functional_extremization.py/.npz/.png`; verdict (canonical, latest non-superseded) `audit_sha256=c36c0754b542a00038e1b4efaac59da64ce397554a880ee31bcc98ec38553bd8` in `computations/investigation-12/inv12_gate_verdicts.txt` (supersedes b5f27b2f after a SHA-only recompute from a `print_verdict_payload` rename; physics identical). Feeds INV12-W4-2 (SA-effective-action diagnosis) as the lizzi-side evidence that the modular fix does NOT select.

Plan-text-drift note: the D_K cache is canonically `computations/session-84/s84_spectrum_cache_L12_tau019.npz`, NOT the plan-pinned `computations/_shared/...`; resolved at runtime per substrate-first-canonical-sourcing.md §(ii.B) (same drift INV12-W3-1 corrected). Trajectory cross-checks bit-faithful to the cache (machine-ε at τ=0.19). Related: [[permanent_theorems]] (zeta-not-physical / functional-selection lineage), [[sessions_s74_s77_results]] (F-STAR-SELF-CONSISTENCY).
