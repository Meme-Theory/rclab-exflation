---
name: s92-lqg-narrow-path
description: S92 LQG x phonon-first workshop — §IX.7 narrow-path feasibility verdict; structural identification of Reading (b) HKR-Cheeger-Simons bridge map; substrate-likely Regime II structural failure
metadata:
  type: project
---

# S92 LQG x Phonon-First Workshop — §IX.7 Narrow-Path Operationalization

**Verbatim provenance**: 2-agent iterative workshop with loop-quantum-gravity-theorist, 2 rounds, 4 turns, closed 2026-05-23. Workshop document: `sessions/archive/session-92/session-92-lqg-phonon-first-workshop.md` (1300+ lines). Source comparison document: `sessions/archive/session-92/session-92-loop-quantum-gravity-phonon-exflation-comparison.md` §IX.7 lines 733-753.

**Why this memory exists**: The §IX.7 narrow path is the only structurally-coherent route by which canonical loop-quantum-gravity kinematical observables (area operator, Wilson lines, spin networks) could enter the framework as DERIVED emergent shadows of the substrate `(A_K, H_K, D_K)`. Future cross-framework integration questions will route back to the workshop's verdict.

## What the workshop established

1. **The §IX.7 narrow path is a derivation procedure (not an embedding)** with five steps: (1) substrate primary; (2) `g_M` from `a_2^{ζ}`; (3) 3-slicing of `g_M`; (4) Peter-Weyl projection onto Σ; (5) area-spectrum matching. Steps 1, 3 well-defined; Step 2 structural-theorem level but locally under-specified; Steps 4, 5 structurally under-specified at substrate-mechanism layer.

2. **The narrow path reduces to a single empirical question**: `α_bridge ≈ 4.81 × 10⁻³` from substrate physics → narrow path closes (Regime I, `γ_emergent = γ_BH = 0.2375`); `α_bridge ∼ O(1)` → narrow path FAILS structurally (Regime II, `γ_emergent ∼ 50`, ~200× too large). Q2 confirms γ does NOT admit cutoff running per Paper 03 §VII — Regime II has no recovery mechanism.

3. **Reading (b) (Hochschild-cocycle evaluation) is the structurally honest reading of Step 4**: bridge-map class is HKR (Hochschild-Kostant-Rosenberg) image with `-Cheeger-Simons` scheme suffix (foliation-aware) per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`. Lives at the cohomology-class layer (regulator-invariant per Three-Level ladder Level 1); preserves background-independence; uses existing framework Hochschild-cocycle infrastructure (the §VII.W bridge theorem template).

4. **L3 obstruction relaxes; the gravitational SU(2) is frame-rotation on the emergent tetrad bundle**: NOT a second algebraic SU(2) from `A_K`. A_F-Birkhoff uniqueness constrains the substrate algebra but is silent about the emergent-tetrad-bundle layer. The §IX.3 obstruction was applied at the wrong layer.

5. **Kinematical-Hilbert-space reading of S74 Two-Manifold Non-Embedding**: S74 operates at the EMERGENT-METRIC layer only; at the kinematical-`H_K` layer, `Π̂_S^{pre}` and `Π̂_S^{post}` live on the same Hilbert space related by the substrate-side Bogoliubov U_B (S38 PROVEN, P_exc=1.000, 59.8 GGE pairs). Bogoliubov-covariance becomes a design constraint on the Step 4 projection operator.

6. **Acoustic white hole exit horizon at τ~0.16 is the substrate-IS distinguished 2-surface** for Step 4 (P2 Reading (b) + Re:L6 O7 + lqg's E2). The a_4 BCS-condensation kinematics enters the cocycle representative's algebraic form. Workshop 6's first test case is `[S_exit-horizon]^♯`, not generic `[S_generic]^♯`.

## Joint cross-framework pre-falsification

**E1' Item 8 (Wave 1 highest-EVOI test)**: the JOINT structural pre-flight test substrate-side `F_0·F_2 ≥ F_1²` ∧ loop-quantum-gravity-side area-volume uncertainty band at canonical j ≤ 3 spin-network configurations. If required `α_bridge ≈ 4.81×10⁻³` violates EITHER inequality, Regime I is structurally pre-forbidden BEFORE Step 4's projection operator is built. Executable on `s84_spectrum_cache_L12_tau019.npz` at <0.1 wave-equivalents with zero new machinery.

## 14 substrate-side primitives for Step 4

P1 enumerated 14 primitives the framework has on disk for the Step 4 construction. Critical ones:
- Primitive 9: B1 acoustic dispersion `ω_B(λ_n) = 0.0019 + 7.0415·λ_n` (z=2 exact, residual 7e-15) — limit-case validation for `Π̂_S`
- Primitive 10: Strutinsky-NCG = O'Neill A-tensor decomposition (smooth-base + oscillating-fiber, gradient ratio 0.71 at fold) — candidate route to local `g_M(x)` reconstruction
- Primitive 13: GGE relic Bogoliubov U_B (S38 PROVEN) — Bogoliubov-covariance design constraint
- Primitive 14: Six-Layer Causal Structure with acoustic white hole — exit horizon at τ~0.16 carries a_4 BCS-condensation kinematics

The framework HAS the algebraic primitives; LACKS the specific assembly into `Π̂_S : H_K → H_S`.

## Substrate-side prior on regime selection

The substrate-side N_e=2.92 anchor (post-fold acoustic e-folds count, the only existing landed instance of a substrate-side bulk-to-surface reduction at landing magnitude) places the substrate-side prior on Regime II (`α_bridge ∼ O(1)`, structural failure), NOT Regime I. Absent contrary evidence, the prior assigns ≥0.6 mass to Regime II and ≤0.3 to Regime I. The narrow path's likely outcome is structural failure; Workshop 6's effort would then re-route to characterizing the substrate's OWN narrow-path effective theory rather than canonical loop-quantum-gravity matching.

## S93 next-session work plan (workshop carry-forwards)

Seven carry-forward computations queued (see workshop document § "Carry-Forward Computations"). Wave 1 dispatches:
1. CF-S93-W1-NARROW-PATH-EIGENVALUE-INVENTORY (<0.02 wave-equivalents)
2. CF-S93-W1-NARROW-PATH-CASIMIR-TABLE (<0.05 wave-equivalents)
3. CF-S93-W1-NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT (Item 8, highest-EVOI, <0.1 wave-equivalents) — the workshop's primary deliverable
4. CF-S93-W1-NARROW-PATH-DIMENSIONAL-PREFACTOR-PIN (<0.05 wave-equivalents)
5. CF-S93-W1-NARROW-PATH-WORKSHOP-1-GATE-PREREG (<0.1 wave-equivalents)

Wave 2-3:
6. CF-S93-W2-NARROW-PATH-PRE-POST-BOGOLIUBOV-RATIO (0.3-0.5 wave-equivalents)
7. CF-S93-W3-NARROW-PATH-WORKSHOP-6-DISPATCH (~1-2 wave-equivalents) — gated on Item 8 verdict

## Closing line (workshop final verdict)

The §IX.7 narrow path's empirical question reduces to a single joint Cauchy-Schwarz / area-volume uncertainty pre-flight test executable on the L_max=12 substrate cache at <0.1 wave-equivalents BEFORE any new machinery is built — feasibility is a one-gate question, not a multi-session program, and the substrate-side prior favors structural failure.

## S93 W8-2 result — substrate area-spectrum √(C_2) built; (0,0)-singlet Step-5 obstruction

S93-W8-2-NARROW-PATH-CASIMIR-TABLE = **INFO** (verdict file `computations/session-93/s93_gate_verdicts.txt:168`, `audit_sha256=49beb93ef19a5a0e...`; supersedes a first-emission FAIL `4c1b1eacf2049e31...` that was a Class-8.3 float-cancellation-floor artifact — literal `==0.0` on a float64 evaluation-ORDER diff; fixed by computing the bit-precision claim over the EXACT-RATIONAL form, Option-A supersedes tag).

- **Casimir table bit-exact (PASS conditions all hold)**: `casimir_su3(p,q) = (p²+pq+q²+3(p+q))/3` ≡ LQG-spec `(p²+pq+q²)/3+(p+q)` IDENTICALLY (Sage symbolic `helper−lqg=0`; QQ-exact lattice max = 0 over all 90 sectors, p+q≤12). √(C_2) joined to per-sector min|λ| — the substrate-side area-spectrum ledger half is built. Friedrich-Bär scaling `min|λ| = 0.4754·√(C_2+1) − 0.0036`, R²=0.9934, Spearman(min|λ|,√C_2)=0.9963 (strong monotone — √(C_2) tracks the lowest mode tightly).
- **The (0,0)-singlet area-matching obstruction (INFO trigger; Step-5 constraint)**: the trivial irrep has **C_2=0 EXACTLY** (√C_2=0, a candidate emergent j=0 / zero-area LQG state) but carries a **nonzero floor eigenvalue 0.82 M_KK** (the fiber-embedding ground mode), so it sits OFF the Casimir-scaling envelope (η_FB=0.82 vs median 0.47, rel-dev 0.74 — the sole sector outside the ±25% band). Structural meaning: **the substrate has NO zero-eigenvalue mode to map onto the LQG j=0 zero-area state**. The substrate's lowest area-gap candidate is GAPPED even where the candidate area vanishes. Any Step-5 area-matching (W8-3 onward) that wants √(C_2(p,q)) → √(j(j+1)) must reconcile this: the LQG spectrum HAS a j=0 zero-area state; the substrate does not. This is a candidate cross-pillar falsifier seed (the gap is a substrate-IS fact, not a truncation artifact — C_2(0,0)=0 is exact at all L_max).
- **Forward (S94 candidate)**: Step-5 area-matching must specify whether the LQG j=0 state is (a) excluded from the emergent shadow (the singlet does not project onto the 2-surface), or (b) mapped to the substrate's gapped floor mode (area-spectrum offset by the singlet gap). Either choice is a structural commitment the narrow path's Step-5 currently leaves open.

## Cross-links

- Workshop document: `sessions/archive/session-92/session-92-lqg-phonon-first-workshop.md`
- S93 W8-2 artifacts: `computations/session-93/s93_w8_2_narrow_path_casimir_table.{py,npz,png}`; WP §W8-2 `sessions/archive/session-93/session-93-w8-workingpaper.md`
- Comparison document §IX.7: `sessions/archive/session-92/session-92-loop-quantum-gravity-phonon-exflation-comparison.md:733-753`
- Bridge-map class registry entry: `sessions/framework/correspondence/lqg-narrow-path-bridge-class.md`
- Required-`α_bridge` canonical pin: `computations/_shared/canonical_constants.py` (`alpha_bridge_required_FW`)
- Substrate spectrum cache: `computations/session-84/s84_spectrum_cache_L12_tau019.npz`
- Reading (b) bridge-map class: HKR with `-Cheeger-Simons` scheme suffix per `.claude/rules/cross-pillar-bridge-anatomy.md`
- Substrate-first direction: [[s92-lqg-narrow-path]] inherits the IS-not-IN discipline from `.claude/rules/phononic-framing.md`
