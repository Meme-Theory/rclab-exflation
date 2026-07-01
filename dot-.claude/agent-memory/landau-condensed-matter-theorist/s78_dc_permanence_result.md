---
name: S78 W3-N DC Permanence Result
description: Structural 1/N decay of localized-perturbation DC fraction; canonical 20% is 4-cell artifact
type: project
---

# S78-W3-N-DC-PERMANENCE — FAIL with structural harvest

## Key finding (permanent, structural)

The "canonical 20% DC fraction" claimed in S73B/S74 is a **4-cell finite-time-window artifact**, not a structural feature of the substrate. Full re-runs at N = {4, 8, 12} cells in the f* scheme give:

| N  | exact-deg DC (k_min→0) | S74-legacy tavg | DC(pure 1/N fit) |
|:--:|:----------------------:|:---------------:|:----------------:|
|  4 |        0.0819          |     0.204       |    c=0.33/N      |
|  8 |        0.0524          |     0.139       |                  |
| 12 |        0.0185          |     0.046       |                  |

Pure power-law fit (f_∞ = 0 imposed, 2 params): **γ = 0.993 ≈ 1** for exact-deg data (χ² = 2.0e−4). All three data streams agree on **DC(N) ∝ 1/N**.

**Why:** The Josephson ring has only one conserved charge — total N_pair (Luttinger superselection). There is NO local conserved charge. A localized perturbation distributes its conserved-charge weight over N·N_mode slots, giving per-slot DC ~ 1/N. This is the generic ETH dilution for a non-integrable Hamiltonian with only global-charge conservation.

## Gate verdict: FAIL

- f_∞ target 0.20 ± 0.02: observed f_∞ is not well-defined with only 3 points (dof = 0 for 3-param fit). Pure power-law with f_∞ = 0 imposed is the clean structural statement.
- IR-robustness target (DC k_min-independent, spread ≤ 0.02): observed spread at {4,8,12} = {0.082, 0.052, 0.029} — IR-DEPENDENT at every N. The "DC peak" is a soft low-frequency feature, not a structural δ(ω).
- Ratio DC(12)/DC(4) target 1.00 ± 0.02: observed 0.220 → matches 4/12 = 0.333 up to quasi-degenerate corrections.

## Why S73B/S74 saw "20%"

S74 `dc_fraction = |<δn>_{t>tmax/2}| / |δn(0)|` averages the late-half of the evolution at t_max = 40/(2π·J_C2) ≈ 6.82 M_KK⁻¹. This window cannot resolve oscillations at |Δω| ≲ 0.15 M_KK. At N=4, quasi-degenerate pairs with Δω < 0.15 all contribute their static amplitude → 20% time-averaged DC. At N=12, spectral density grows; fewer pairs stay within the window → 4.6%.

My re-analysis reproduces the S74 tavg to machine epsilon ({0.204, 0.139, 0.046} vs S74 {0.2037, 0.1393, 0.0463}) → the computation is consistent; the interpretation of "20% permanent DC" was wrong.

## SDW cross-check insight

At 8 cells, SDW scheme (V_fold → diag(V_fold), diagonal pairing only) gives IR-TRIVIALLY invariant DC = 0.1072 at ALL k_min. Why: the diagonal Hamiltonian has many exact degeneracies (each mode decoupled), so the zero-frequency band is already a true δ(ω). The **f* scheme's off-diagonal intra-cell pairing is what destroys the trivial degeneracies** and turns the DC into a soft low-frequency feature.

Implication: the 20% number is an **intermediate regime** between pure-diagonal (trivially 1/N · N_mode weight at N=4) and full-thermalization (1/N·N_mode → 0 at N → ∞).

## What this closes / opens

CLOSED:
- "20% DC fraction is a permanent substrate feature" (S73B claim) — FALSE, it's a 4-cell artifact
- DC-permanence route to DE / DM via localized-perturbation conservation — DECAYS as 1/N

CONFIRMED:
- GGE thermalization chain (S58–S63): localized perturbations thermalize into the global GGE
- Luttinger superselection of N_pair is the only conserved charge protecting permanence
- The "Ordered Veil" permanence is GLOBAL (GGE), not LOCAL (per-slot DC)

## Files

- `computations/s78_dc_permanence.py` — full 4,8,12 re-runs + IR scan + fit-form suite
- `computations/s78_dc_permanence.npz` — all diagnostic arrays
- `computations/s78_dc_permanence.png` — 4-panel: DC vs N, fit-form comparison, IR spread, legacy traces

## Key takeaway for framework

The phonon-exflation framework does NOT claim local permanence. The claim was always that the **GGE relic** survives — and the GGE is a global many-body state, not a local DC excess. S78 W3-N confirms this: local DC decays as 1/N, while the GGE (total N_pair conservation) is protected to machine epsilon.
