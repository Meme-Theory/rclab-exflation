---
name: s114-as-functional-selection
description: S114 W4-1 — A_s magnitude is FUNCTIONAL-PLURALISM PERMANENT (physical d.o.f. like CC ratio); sub-test d|beta|^2/d(a_0/a_2)=0 EXACT; plan-chain aH|_fold correction. S115 W3-2 WIDENS it on {maxent, Connes} axis-basis (no collapse; axes PARTITION sudden↔adiabatic ends)
metadata:
  type: project
---

# CF-S114-AS-FUNCTIONAL-SELECTION (S114 W4-1, FAIL = PLURALISM-PERMANENT, informative)

**audit_sha256** = `395f6800c8d143e440f5ad3ca54e14c902cfad1ec1f62ae8d465f1d2dc43cd71`
**content_sha256** = `c3b007e002ab539252320a45236cf1ee703e8f0bd6980e1fd96e59011e5e76d1`
Artifacts: `computations/session-114/s114_cf_as_functional_selection.{py,npz,png}`. Composite **FAIL**; 3-tuple **sign=PASS / magnitude=FAIL / regime=VALID**; dual-prior posterior **0.10/0.90 → Track B (PLURALISM-PERMANENT)**.

The A_s **Object-2** decider (the magnitude-as-a-Planck-comparison-NUMBER, left open by S113 WS-5 AS-HTILDE). Closes the WS-5 question: does the substrate SELECT one spectral functional for the produced-relic A_s, or is functional-choice a physical d.o.f. (lizzi-signature)? **Answer: PLURALISM — no substrate-canonical selector; A_s magnitude is a physical d.o.f. like the a_0/a_2 CC ratio.** §EVOI.BF goes "open, may converge" → **"open, structurally"**.

## Part (A) — structural sub-test [SIGN/CHAIN]: d|β_k̂|²/d(a_0/a_2 horizon-exit) = 0 EXACT

PERMANENT structural result: the box-delta sudden Bogoliubov |β_k̂|² (S100b) is a closed form in **fold-transit/UV quantities ONLY** — `Ω_z_on=1.2872, Ω_z_off=−1.2885, V_box=1.9028, Δη=0.00113, ξ_KZ`. NONE contains the horizon-exit a_0/a_2 ratio. By chain rule `d|β|²/d(a_0/a_2) = Σ(∂f/∂input)·0 = 0` (computed = `0.000e+00`, floor 1e-12). The 181× SDW/Zubarev a_0/a_2 split (S82 Obs 6.3, `a_0_FW_zeta=6440.0`, `a_2_FW_zeta=2776.165389`, poleconv-A-double, a_0 n=0/s=4, a_2 n=2/s=3) lives on the **horizon-exit H̃ carrier** the impulse-quench floor never reads. ⇒ **openness CONFINED to the UNIFIED-AS-79 route**, does NOT propagate to the floor POINT. The sub-test SIGN and the SELECTION verdict run in OPPOSITE directions (both end-states FAIL SELECTION); PASS would need a SEPARATE substrate-canonical collapse of the spread, which did not occur.

## PLAN-CHAIN CORRECTION (in-session, disclosed; STRENGTHENED the result)

Plan §W4-1 chain Step 1 wrote `aH|_fold = H_fold/Λ_rescale` — **DROPS the fold scale-factor a_fold_raw** (that combination = 0.00253 M_KK, rel-dev 0.997, WRONG). Correct conformal relation is the standard `aH = a(τ)·H(τ)`:
- `aH|_fold = a_fold_raw·H_fold/Λ_rescale = 386.024·586.527/232125.155 = 0.9753935188` (**rel-dev 0.0 EXACT** vs npz `aH_target`)
- INDEPENDENT route: `aH|_fold = k_pivot/(k/aH)|_fold = 14.3111/14.6721 = 0.9753935188` (**rel-dev 0.0 EXACT**)
Both fold-passage kinematics; neither contains a_0/a_2 ⇒ aH|_fold TRANSIT-TRAJECTORY-FIXED. Recorded in verdict-line companion row. **Lesson for future fold-conformal-pump derivations**: aH is `a(τ)·H(τ)`, NOT `H/Λ` — always carry the scale factor a_fold_raw.

## Part (B) — cross-functional spread = 1.2590 OOM (5sf), none in Planck ±5% band

Three defensible spectral functionals of the SAME D_K-derived occupation spectrum, vs Planck A_s=2.1e-9:
| functional | A_s | OOM | in-band? |
|:--|:--|:--|:--|
| impulse-quench (floor POINT, `A_s_FW`) | 1.536706e-08 | **+0.86437** | No |
| UNIFIED-AS-79 (slow-roll) | 3.297762e-09 | +0.196 | No |
| Parker-adiabatic | 5.987138e-08 | +1.455 | No |
spread = +1.455−(+0.196) = **1.2590 OOM** (impulse +0.864 sits between). Planck in-band threshold `log10(1.05)=0.02119` (DIAGNOSTIC-only — NOT a Planck-comparison gate). No substrate-canonical selector (sudden/slow-roll/adiabatic are all physical; exit-greybody filter itself fitted, inv12 W3-4) ⇒ spread persists ⇒ SELECTION FAILS.

## What is UNTOUCHED by this FAIL
The floor-amplitude POINT `A_s_FW=1.5367e-08` (TD impulse-quench source, S111-CF-AS3a, see [[s114_as_functional_selection]] parent context in MEMORY.md A_s closure block) and the floor INEQUALITY `A_s ≥ A_s^BD` (permanent, 3 axes, S111 WS-AS-1 LIZ2-1) stand. The >3-OOM liability is re-localized to cross-functional + exit-greybody-filter openness. Forward (FAIL branch): capstone A_s down-tag LANDS "open, structurally" (designated-writer, capstone-hygiene Q3 → housekeeping); mack updates falsifier Row #12 / §EVOI.BF. No CF emitted (CF-S115-AS-FUNCTIONAL-REGIME is INFO-only). Runtime canonical_constants SHA drift `a4b8b679442de533` vs plan-pin `9ee1a113b200f2ad` (sibling S114 promotion; substrate-first §(ii.B) capture; consumed quantities all ≤S111).

## S115 W3-2 follow-up — CF-S115-AS-NEWAXIS-SELECTOR (FAIL = PLURALISM WIDENED on a fresh axis-basis)

**audit_sha256** = `b07deb9ba49159b5f39d5c44c0738843b3058a91041df9981707d6e9c550059a`; **content_sha256** = `ad4855b77e637012a5634a3e576f5884915b49c1a8c936b613265e25c934c5f9`. Artifacts `computations/session-115/s115_as_newaxis_selector.{py,npz,png}`. Composite **FAIL**; 3-tuple **sign=FAIL / magnitude=FAIL / regime=VALID**; SELECTION=**COINCIDENCE-ONLY**; dual-prior **0.05/0.95 → Track B**. OPTIONAL (planner-discretion, EVOI-last); verdict was OPEN (prior 0.10 PASS / 0.90 FAIL), computed not pre-judged.

Tested TWO new physical axes OUTSIDE {impulse, UNIFIED, Parker} for a spread-collapse. PASS criterion (strict): an axis must land ≤0.10 OOM of impulse AND ≥1 OTHER functional (collapse the 1.2590 spread to one typed value).
- **AXIS-1 maxent/Jaynes**: Bose `n_k=1/(exp(λ_N+λ_E ω_k)−1)`, `(λ_N,λ_E)=(14.8856, 0.004312)` via fsolve on `<N>=Σ|β|²=2.081e-5`, `<E>=Σω_k|β|²=2.501e-4` (ω_k=k, box-delta s100b); converged to machine ε. Pivot occ ratio to raw = **1.0588** (near-flat squeezed spectrum redistributes only ~6%). `A_s^maxent = 1.400596e-8` (k̂=1/ξ_KZ norm), **OOM +0.8241** → 0.040 from impulse, coincides with **impulse ONLY**.
- **AXIS-2 Connes-distance**: diagonal-sub-triple Connes DIAMETER `d_C = 1/(λ_max−λ_min) = 1/(5.418937−0.819741) = 0.217429` on L12 D_K cache (166,896 evals; GPU RX 9070 XT extremal dev **0.000e+00**). `A_s^Connes = |β_k̂|²/(2π²·d_C) = A_s_FW/0.2174 = 7.067612e-8`, **OOM +1.5271** → 0.072 from Parker, coincides with **Parker ONLY**. (x-checks: inv-max-gap d_C=11.87→OOM −0.21; FS vacuum angle 4.562e-3→OOM +3.21 off-scale; diameter is the canonical unique-extremal reading.)

`min_collapse_dist = 0.62809 OOM ≫ 0.10` → no collapse. **PERMANENT structural content (the finding, not just FAIL)**: the two substrate-canonical principles PARTITION the spread by mechanism — maxent (occupation-redistribution) → **sudden/diabatic end** (impulse); Connes-distance (spectral-geometry normalization) → **adiabatic end** (Parker). They land on OPPOSITE ends. ⇒ the 1.259-OOM spread reflects a REAL physical axis (sudden↔adiabatic), not three arbitrary functional choices; even maxent + NCG-metric principles cannot collapse it. The substrate does NOT type its own A_s on this wider axis-basis. §EVOI.BF "A_s magnitude = physical d.o.f." headline STANDS, broadened. No mack routing (that is the PASS path). **Method note**: A_s_FW gives `|β_k̂|² = 2π²·A_s_FW = 3.0333e-7`; box-delta pivot `beta2_pivot_closed_form=3.0454e-7` → `/(2π²)=1.5428e-8` (ratio 1.004 to A_s_FW); spectrum near-flat to first RT zero k≈2779 so k̂=53.30 (>grid-max 50) is a flat extrapolation. Connes-distance on a finite triple = resistance/path metric on the eigenvalue line; the DIAMETER (extremal states, optimal a saturating ‖[D,a]‖=1) is the unique substrate-intrinsic dimensionless scale.
