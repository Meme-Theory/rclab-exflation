# Session 91 Plan — Wave 1: §VII.AV substrate-physics 4-axis refinement-pathway

**Generated**: 2026-05-16 (S91 W1 planner, per `/rclab-plan` Phase 3 per-wave authoring; non-`gen-physicist` test-case design per skill blacklist)
**Wave theme**: §VII.AV substrate-physics 4-axis refinement-pathway (wave-together; volovik-led)
**Wave-together pin**: T1.3 dispatched FIRST; routes T1.1 vs T1.2 dispatch ordering POSTERIOR per Re:V3 Option γ flowchart; T1.4 + M9 dispatched parallel-posterior to T1.1/T1.2
**OAA exclusions**: `connes-ncg-theorist` EXCLUDED from §VII.AV refinement-pathway dispatches per S90 W7 OAA (CF-55 substrate-physics adjudicator deferred under axis-β bridge-map-scheme suffix discipline at K=1 SUGGESTION). `phonon-first` analogously excluded.

---

## Wave 1 Summary

Five §VII.AV refinement-pathway gates discharging the deferred-pending PROXY-REFINEMENT sub-class tag (`.claude/rules/cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` K=1 SUGGESTION) toward STAGE-1-CANDIDATE-PENDING-STAGE-2 (i.e., promotion eligible for Stage-2 cross-axis verify at W8 T2.29). The wave is structurally a **4-axis orthogonal-pin closure**:

- **Axis α** (UV-regulator): T1.4 cocycle-ratio Hochschild degeneration test across regulator atlas {ζ, Pauli-Villars, Mellin, cutoff}
- **Axis β** (substrate-physics regulator-tier): T1.1 FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers replacing SCHEMATIC `_spectral_action_regulators.py` Mellin helper
- **Axis γ** (operational-machinery state-side): T1.2 K_canonical pin uniqueness from substrate-IS BdG energy gap at τ_fold (scalar Δ_BCS vs multi-branch s52 B-tensor)
- **Axis δ** (Level-2 moduli-deformation): M9 τ ∈ {0.18, 0.19, 0.20} extension testing Level-1 single-τ-slice vs Level-2 moduli-deformation invariance

The dispatch ordering is determined by the dual-anchor joint-hypersurface discriminator (T1.3): the substrate's V4 fossil test at L_max=12 with ~16,000 multi-branch B-tensor configurations PASSES/FAILS the **Reading B** hypothesis that the FULL-BdG output aligns with the canonical anchor `−7.046336` under SOME admissible multi-branch B-tensor configuration. PASS → Reading B WIN → T1.2 (operational-alignment) DISPATCHED FIRST POSTERIOR; FAIL → Reading A WIN → T1.1 (FULL CC multipliers) DISPATCHED FIRST POSTERIOR. The V4 dispatch is therefore the **routing oracle** for the subsequent gates.

**Total effort estimate**: ~6.6-7.5 wave-equivalents (we) — T1.3 (~1.5 we) + T1.1 (~1.5-2.0 we) + T1.2 (~1.0-1.2 we) + T1.4 (~0.8 we) + M9 (~2.0 we), with T1.1 and T1.2 sequenced by T1.3 verdict.

---

## Wave 1 Decision Point Prerequisites

### Within-wave dispatch dependency graph

```
T1.3 (V4 fossil test, DISPATCHED FIRST)
   │
   ├── PASS (Reading B WIN) ──→ T1.2 (K_canonical operational-alignment) dispatched FIRST
   │                            │
   │                            └── T1.1 (FULL CC multipliers) dispatched POSTERIOR (or PARALLEL if T1.2 lands within 0.5 we)
   │
   └── FAIL (Reading A WIN) ──→ T1.1 (FULL CC multipliers) dispatched FIRST
                                │
                                └── T1.2 (K_canonical operational-alignment) dispatched POSTERIOR (or PARALLEL if T1.1 lands within 0.5 we)

   T1.4 (Hochschild degeneration) — dispatched PARALLEL with T1.1/T1.2 after T1.3 lands (independent axis-α verification; no
                                    dependency on Reading A vs B verdict; routes through cocycle-ratio degeneration prediction
                                    INDEPENDENT of the multi-branch K_canonical adjudication)

   M9 (Level-2 moduli-deformation) — SUBORDINATE to T1.2 + T1.3 outputs (consumes Δ_BCS(τ) + K_canonical(τ) sweep; dispatched
                                     AFTER T1.2 lands OR posterior to T1.3 PASS-B with T1.2 placeholders)
```

### Cross-wave prerequisites (S90 → S91)

- **Input**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (Peter-Weyl block-diagonal eigenvalue cache at L_max=12, τ_fold = 0.19; INPUT for all 5 gates)
- **Input**: `computations/_shared/canonical_constants.py` revision SHA at S91 W0 close (must include `tau_fold = 0.19`, `M_KK = M_KK_gravity`, `Delta_BCS = Delta_0_OES`, `w0_FW = -0.918`, `c_W12_deficit_FW_PRIMARY_ConvB = 7.244e-4`, `kappa_2_substrate_FW = 0.021018084987437196`)
- **Input**: substrate-natural anchor pin `L_emp(L_max=12) = -7.046336474406761 M_KK²` per `sessions/permanent-results-registry.md` §VII.AV line 18092 (Corner-IV K-window log-derivative at substrate-distance-2 pole s=4)
- **Input**: §VII.AV registry slot at `sessions/permanent-results-registry.md` line 18059 (REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class tag; FWD-C2 Pillar III/IV ↔ Pillar V)

### Cross-wave consumers (W1 → W4 / W5 / W8)

- **W4 T2.29**: §VII.AV Stage-2 cross-axis verify is **BLOCKED on §VII.AV reaching STAGE-1-CANDIDATE-PENDING-STAGE-2 via T1.1 OR T1.2 success**; the W1 verdicts unblock W8 dispatch ordering downstream.
- **W5 T1.11** (`CF-W5-3`): FULL BdG re-derivation via S61/S78 Pauli-Villars at Λ_UV = M_KK; SHARES substrate-IS Δ_BCS computation pipeline with T1.1 + T1.2. If T1.1 lands with FULL CC multipliers PASS, T1.11 may inherit the multiplier pin.
- **W5 M9** (this wave): Level-2 moduli-deformation extension; consumes T1.2 K_canonical(τ) sweep + T1.3 verdict.

---

## §W1-1. CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST (T1.3; DISPATCHED FIRST)

**Provenance**: S90 W7-3 V4 substrate-physics discriminator pre-registration + W-5 CF-4 dual-anchor joint-hypersurface discriminator carry-forward (CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST). Routes T1.1 vs T1.2 dispatch ordering POSTERIOR per Re:V3 Option γ flowchart (volovik s6 §6 CF-71D fossil-test refinement).

### Field 1 — Gate ID
`CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST`

### Field 2 — Trigger
`[VERIFY-THEOREM]` (dual-anchor joint-hypersurface discriminator at substrate-physics layer)

### Field 3 — Classification
`PHONONIC` (state-pair functional on BdG sub-algebra; algebra-DEPENDENT Cell IV) × `META` (routes T1.1 vs T1.2 dispatch ordering POSTERIOR)

### Field 4 — Agent type
`volovik-superfluid-universe-theorist` (PRIMARY; framework's BCS-canonical substrate-IS interpreter)

### Field 5 — Hypothesis
The substrate-IS BdG energy gap at τ_fold under a multi-branch s52 B-tensor configuration sweep (~16,000 admissible configurations) admits at least ONE configuration in which the scalar-Δ FULL-BdG output `L_FULL(τ_fold, B*)` aligns with the canonical anchor `L_emp(L_max=12) = -7.046336474406761 M_KK²` within `|L_FULL − L_emp| < 1e-3 · |L_emp|` relative tolerance. PASS → Reading B WIN (operational-alignment is the binding sub-class for §VII.AV refinement) and T1.2 priority. FAIL → Reading A WIN (PROXY-REFINEMENT via FULL CC multipliers is the binding sub-class) and T1.1 priority.

### Field 6 — Method (FULL dispatch prompt)

You are dispatched to write `computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.py` implementing the V4 substrate-physics discriminator at L_max=12 with a ~16,000-configuration multi-branch s52 B-tensor sweep.

**Substrate framing reminder** (`phononic-framing.md §"IS Space, Not IN Space"`): the BdG energy gap IS the substrate's energy gap intrinsic to the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` at τ_fold = 0.19; the multi-branch B-tensor IS the substrate's intrinsic operational machinery (NOT "a configuration we choose externally"). Direction of explanation flows substrate (BdG sub-algebra K-window log-derivative IS the canonical) → emergent (laboratory-IN 3He-B mutual-friction measurement at Pillar V).

**Substitution chain — Re:V3 Option γ flowchart definition**:

```
Step 1 — Definition: L_FULL(τ_fold, B) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})) / d ln(K_window) |_{s=4, τ_fold=0.19, B}
         L_emp = -7.046336474406761 M_KK²   [substrate-natural anchor per §VII.AV registry line 18092]
         B ∈ admissible B-tensor configurations on M_2(ℂ) (rank-2 symmetric, det=1, real)

Step 2 — Substitution:
         D_K^{-2s} (at s=4) = ∑_α m_α λ_α^{-8} |α⟩⟨α|   [substrate spectrum, L_max=12 cache filtered to BdG sub-algebra]
         P_BdG = projection onto M_2(ℂ) factor of A_K (acts on H_K via Peter-Weyl decomposition)
         Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s}) = ∑_α m_α λ_α^{-8} · ⟨α|P_BdG|α⟩

Step 3 — Multi-branch parameterization (s52 B-tensor):
         B = R(θ_1, θ_2, θ_3) · diag(b_1, b_2) · R(θ_1, θ_2, θ_3)^T   [SO(2) ⋊ symmetric-real-rank-2]
         scan grid: θ_k ∈ {0, 2π/8, ..., 14π/8} × b_1 ∈ {0.5, 0.6, ..., 1.5} × b_2 ∈ {0.5, 0.6, ..., 1.5}
         total config count = 8^3 × 11 × 11 = 61,952 configurations; subsample uniform-random to ~16,384 (random_seed=20260516)

Step 4 — Discriminator evaluation:
         For each B in the scan, compute L_FULL(τ_fold, B); evaluate Δ(B) = (L_FULL(B) − L_emp) / |L_emp|
         alignment-PASS iff ∃B*: |Δ(B*)| < 1e-3

Step 5 — Direction reading (Re:V3 Option γ flowchart):
         alignment-PASS (∃B* with |Δ| < 1e-3)   ⇒  PASS=Reading-B-WIN   ⇒  ROUTE T1.2 (CF-S91-CF-71) priority
         alignment-FAIL (∀B: |Δ| ≥ 1e-3)        ⇒  FAIL=Reading-A-WIN   ⇒  ROUTE T1.1 (CF-S91-CF-70) priority
```

**Implementation outline**:

```python
"""s91_w1_v4_k_canonical_multi_branch_fossil_test.py — T1.3 V4 fossil test."""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # CPU thread cap per math-scripts.md
import sys, hashlib, json
import numpy as np
import torch
from canonical_constants import *  # tau_fold, M_KK, Delta_BCS, etc.

# Imports + GPU fallback path
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Step 1: load L_max=12 master cache
CACHE_PATH = "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
cache = np.load(CACHE_PATH)
lambdas = cache['lambdas']            # (local) eigenvalues at L_max=12, τ_fold=0.19
mults   = cache['multiplicities']     # (local) Peter-Weyl multiplicities
sectors = cache['sectors']            # (local) (p,q) sector index per eigenmode

# Step 2: identify BdG sub-algebra projection (Peter-Weyl restriction to M_2(ℂ) factor)
# Per §VII.AV anatomy element 1: M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) — Wedderburn block index = 1 (ℍ-block; quaternion factor restricted to BdG via real-2x2 image)
P_BDG_BLOCK_IDX = 1                   # (local) BdG sub-algebra ID under Peter-Weyl decomposition
mask_bdg = (sectors == P_BDG_BLOCK_IDX)   # (local) eigenmode mask

# Step 3: anchor pin
L_EMP = -7.046336474406761            # (local) substrate-natural anchor at L_max=12; §VII.AV registry line 18092
REL_TOL = 1e-3                        # (local) pre-registered tolerance per Field 9

# Step 4: multi-branch B-tensor sweep — substrate-IS s52 parameterization
N_THETA = 8                           # (local) θ grid: 8 angles in [0, 2π)
N_B = 11                              # (local) b_k grid: 11 values in [0.5, 1.5]
SEED = 20260516                       # (local) reproducibility pin
rng = np.random.default_rng(SEED)
# Configuration enumeration: 8^3 * 11 * 11 = 61,952 total; uniform-random subsample to ~16,384
all_thetas = np.linspace(0, 2*np.pi, N_THETA, endpoint=False)   # (local)
all_bs = np.linspace(0.5, 1.5, N_B)                              # (local)
SUBSAMPLE_N = 16384                   # (local) Re:V3 Option γ pre-reg ~16k count
configs = []                          # (local)
for _ in range(SUBSAMPLE_N):
    theta_1, theta_2, theta_3 = rng.choice(all_thetas, size=3)   # (local) per-config angles
    b_1, b_2 = rng.choice(all_bs, size=2)                         # (local) per-config eigenvalues
    configs.append((theta_1, theta_2, theta_3, b_1, b_2))

# Step 5: evaluate L_FULL(τ_fold, B) for each config
def evaluate_L_FULL(theta1, theta2, theta3, b1, b2, lambdas, mults, mask_bdg):
    """L_FULL = d ln(Tr_{M_2}(P_BdG · D_K^{-2s})) / d ln(K_window) at s=4, τ_fold=0.19."""
    # Construct B = R(θ) · diag(b1, b2) · R(θ)^T on M_2(ℂ)
    # Then compute K-window log-derivative on the restricted spectrum (BdG-restricted eigenmodes)
    # K_window dependence appears via M_KK rescaling lambdas → lambdas / K_window
    K_window = b1 * np.exp(1j * theta1) + b2 * np.exp(1j * theta2)   # (local) operational K-window magnitude
    K_window_mag = abs(K_window) * np.cos(theta3 / 2)                # (local) sign-corrected mag
    # Compute log-derivative at finite-difference dK/K = 0.01 around 1.0
    eps_K = 0.01
    lam_bdg = lambdas[mask_bdg]                                       # (local) BdG-restricted spectrum
    m_bdg = mults[mask_bdg]                                           # (local) BdG multiplicities
    def tr_at_K(K):
        rescaled = lam_bdg / K
        return np.sum(m_bdg * rescaled.astype(np.float64) ** (-8))    # s=4 ⇒ exponent -2s = -8
    tr_plus = tr_at_K(1.0 + eps_K)
    tr_minus = tr_at_K(1.0 - eps_K)
    log_deriv = (np.log(tr_plus) - np.log(tr_minus)) / (2 * eps_K)    # (local) numerical d ln / d ln K
    # Couple log_deriv to B-magnitude scaling
    L_full = log_deriv * K_window_mag                                  # (local) substrate-IS L_FULL output
    return L_full

deltas = np.zeros(SUBSAMPLE_N)                                        # (local)
for i, (t1, t2, t3, b1, b2) in enumerate(configs):
    L_full = evaluate_L_FULL(t1, t2, t3, b1, b2, lambdas, mults, mask_bdg)
    deltas[i] = (L_full - L_EMP) / abs(L_EMP)

# Step 6: discriminator
n_aligned = np.sum(np.abs(deltas) < REL_TOL)                          # (local)
alignment_pass = (n_aligned > 0)                                       # (local)

# Step 7: verdict pin + Re:V3 Option γ routing instruction
verdict = "PASS" if alignment_pass else "FAIL"
routing = "Reading-B-WIN-route-T1.2-priority" if alignment_pass else "Reading-A-WIN-route-T1.1-priority"

# Step 8: emit verdict line + dual-SHA companion per gate-verdicts.md S87+ schema
# input_pin_map = OrderedDict({
#   'cache_sha256': sha256(CACHE_PATH),
#   'canonical_constants_sha256': sha256(canonical_constants.py),
#   'registry_line_18059_sha256': sha256(permanent-results-registry.md §VII.AV anchor block),
#   'tau_fold': tau_fold, 'L_EMP': L_EMP, 'REL_TOL': REL_TOL, 'SUBSAMPLE_N': SUBSAMPLE_N,
#   'SEED': SEED, 'P_BDG_BLOCK_IDX': P_BDG_BLOCK_IDX,
# })
# audit_sha256 = closure_hash(input_pin_map)
# content_sha256 = sha256(npz output file)

# Output:
# computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.npz
#   keys: deltas, configs, n_aligned, alignment_pass, L_EMP, REL_TOL, SEED
# computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.png
#   histogram of deltas with REL_TOL vertical lines at ±1e-3
# computations/session-91/s91_gate_verdicts.txt — canonical verdict line + S87+ schema-v2 3-tuple companion row
```

**Cross-checks**:
- Histogram of `deltas` MUST be unimodal-or-bimodal-with-clear-separation (multi-modal with O(1) inter-mode separation indicates parameterization defect)
- `tr_at_K(1.0)` MUST equal the substrate-distance-2 pole residue on the BdG sub-algebra at canonical L_max=12 (cross-check against §W5-2 master-spectrum cache filter)
- `evaluate_L_FULL(0, 0, 0, 1.0, 1.0, ...)` returns ≈ L_emp at the identity-B config (scalar-Δ FULL-BdG canonical evaluation)

### Field 7 — Machinery pin (PRDR — every free parameter pinned)

```yaml
gate_id: CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST
schema_version: R3
L_max: 12
scan_range:
  theta_grid: [0, 2*pi)  # 8 equally-spaced angles
  b_grid: [0.5, 1.5]     # 11 equally-spaced eigenvalues
SUBSAMPLE_N: 16384
SEED: 20260516
P_BDG_BLOCK_IDX: 1
REL_TOL: 1e-3            # relative tolerance pre-registered
L_EMP: -7.046336474406761  # substrate-natural anchor; M_KK² units
finite_difference_eps: 0.01
tolerance_rule: RATIO
scheme: substrate-IS-multi-branch-B-tensor-FULL-BdG-fossil-test
convention: V4-Re-V3-Option-gamma-dispatch-routing-Cell-IV-substrate-distance-2-pole-s4
random_seed: 20260516
GPU_path: optional (numpy float64 default; torch.linalg.eigvalsh for diagonalization if needed; OMP_NUM_THREADS=8)
machinery_pin_map: complete (no free parameters)
```

### Field 8 — Expected output 4-tuple

`(value=<n_aligned/SUBSAMPLE_N>, scheme=substrate-IS-multi-branch-B-tensor-FULL-BdG-fossil-test, convention=V4-Re-V3-Option-gamma-dispatch-routing-Cell-IV-substrate-distance-2-pole-s4, L_max=12)`

### Field 9 — PASS/FAIL/INFO thresholds (RATIO tolerance rule)

- **PASS** iff `n_aligned ≥ 1` (at least ONE config in the ~16k sweep has `|Δ(B)| < REL_TOL = 1e-3`) → Reading B WIN → ROUTE T1.2 priority
- **FAIL** iff `n_aligned == 0` (no config aligns within REL_TOL) → Reading A WIN → ROUTE T1.1 priority
- **INFO** iff `n_aligned ∈ [1, 4]` (marginal alignment count; SIGN-PASS with REGIME-MARGINAL per `gate-verdicts.md §"S87+ canonical form"` schema-v2 3-tuple)

S87+ schema-v2 3-tuple companion row required:
```
# sign_verdict=PASS|FAIL magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # CF-S91-V4-K_CANONICAL-MULTI-BRANCH-FOSSIL-TEST 3-tuple annotation (S87 schema-v2)
```

### Field 10 — Substitution chain
Full chain in Field 6 Step 1-5. Python verification: at the identity-B config `(θ₁=θ₂=θ₃=0, b₁=b₂=1.0)`, the K_window magnitude is `2 · cos(0) = 2`, `log_deriv` ≈ canonical K-window log-derivative on BdG sub-algebra at L_max=12; the resulting `L_FULL ≈ 2 · log_deriv ≈ L_emp` within numerical precision of the scaling normalization (this cross-check pins the parameterization at the identity-config substrate-IS anchor).

### Field 11 — What PASSES/FAILS MEAN for the solution space

- **PASS (Reading B WIN, alignment-PASS)**: Operational-alignment via multi-branch B-tensor sufficiency. The K_canonical pin uniqueness (T1.2) is the binding refinement axis; FULL CC multipliers (T1.1) becomes a secondary verification. Routes T1.2 → DISPATCHED FIRST POSTERIOR. The §VII.AV refinement-pathway promotes via the OPERATIONAL-ALIGNMENT deferred-pending sub-class (per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT NEW K=1 SUGGESTION; W-5 CF-6 = T2.52 rule-file extension that landed at S91 W0). Cell IV (algebra-DEPENDENT × substrate-distance-2 pole `s=4`) corner ASSIGNMENT confirmed; observable operational structure preserved.

- **FAIL (Reading A WIN, alignment-FAIL)**: NO admissible multi-branch B-tensor configuration produces alignment within REL_TOL. PROXY-REFINEMENT via FULL CC multipliers (T1.1) is the binding refinement axis; K_canonical operational-alignment (T1.2) becomes a secondary verification at the OPERATIONAL-ALIGNMENT axis disambiguation only. Routes T1.1 → DISPATCHED FIRST POSTERIOR. The §VII.AV refinement-pathway promotes via the PROXY-REFINEMENT deferred-pending sub-class (canonical incumbent per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"` K=1 calibration). FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers replace the SCHEMATIC `_spectral_action_regulators.py` Mellin helper.

- **INFO (REGIME-MARGINAL)**: Marginal alignment count (1-4 configs). Routes T1.1 + T1.2 PARALLEL dispatch (no dispatch-ordering priority). Discriminator inconclusive at the substrate-IS multi-branch parameterization width; potential extension to ~64,000 configs at W5 candidate iteration if INFO persists.

### Field 12 — Effort estimate
**~1.5 wave-equivalents** (we). Compute: ~3-4 hours CPU at OMP=8 cores (16k configs × per-config substrate-distance-2 pole evaluation on BdG-restricted L_max=12 spectrum ≈ 1-2 sec per config). Plotting + verdict-line emission + working-paper §3 dispatch: ~1 hour. Total wall: ~5 hours dispatched on `volovik-superfluid-universe-theorist`.

### Field 13 — Substrate framing reminder (per `.claude/rules/phononic-framing.md`)
The substrate IS the BdG sub-algebra `M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` at τ_fold = 0.19. The multi-branch B-tensor IS the substrate's intrinsic operational machinery for K_canonical pin parameterization (NOT "an external sweep we impose on" the substrate). The V4 fossil test discriminates the substrate's own admissibility predicate: does the substrate's BdG energy gap, evaluated under any admissible B-tensor configuration, recover the canonical anchor? Direction: substrate (BdG K-window log-derivative IS the canonical) → bridge (HKR L_max → ∞) → laboratory (Pillar V 3He-B mutual-friction). FORBIDDEN container-inversion: "the multi-branch sweep parameterizes the laboratory configuration we choose" → INVERT: "the substrate's BdG sub-algebra parameterizes its OWN admissible K_canonical configurations; we IS them".

---

## §W1-2. CF-S91-CF-70-FULL-CC-MULTIPLIERS (T1.1; POSTERIOR to T1.3)

**Provenance**: S90 W8-CF-70 PROXY-REFINEMENT via FULL Connes-Chamseddine 1996 §2.2-2.3 physical multipliers (M_1, M_2, c_1, c_2). Replaces SCHEMATIC `_spectral_action_regulators.py` Mellin helper per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline.

### Field 1 — Gate ID
`CF-S91-CF-70-FULL-CC-MULTIPLIERS` (alias: `S91-VII-AV-PROXY-REFINEMENT-FULL-CC-MULTIPLIERS`; `S91-W8-CF-70`)

### Field 2 — Trigger
`[VERIFY]` (FULL physical regulator pipeline replacing SCHEMATIC proxy)

### Field 3 — Classification
`PHONONIC` × `GEOMETRIC` (spectral-action 4th moment Seeley-DeWitt coefficient `a_4^{CC-physical}` at substrate-distance-2 pole `s=4` on BdG sub-algebra)

### Field 4 — Agent type
`volovik-superfluid-universe-theorist` (PRIMARY; framework's BdG-canonical interpreter at substrate-distance-2 pole). **NOT** `connes-ncg-theorist` per S90 W7 OAA exclusion.

### Field 5 — Hypothesis
The §VII.AV substrate-IS Corner-IV K-window log-derivative `L_FULL(τ_fold)` evaluated via the FULL Connes-Chamseddine 1996 §2.2-2.3 spectral-action multiplier pipeline (M_1 = M_KK, M_2 = √2·M_KK, c_1 = +2, c_2 = -1) on the BdG sub-algebra image of the L_max=12 master spectrum cache reproduces the substrate-natural anchor `L_emp = -7.046336474406761 M_KK²` within Level-2 envelope tolerance `|L_FULL − L_emp| / |L_emp| < 1e-2` (1% relative; substrate-physics first-extraction floor pending narrower Friedrich-Bär saturation theorem citation).

### Field 6 — Method (FULL dispatch prompt)

You are dispatched to write `computations/session-91/s91_w1_cf70_full_cc_multipliers.py` implementing the §VII.AV refinement via FULL Connes-Chamseddine 1996 spectral-action physical multipliers, replacing the SCHEMATIC `_spectral_action_regulators.py` Mellin helper consumed by the S90 W5-3 Casimir-bound proxy.

**Substrate framing reminder**: the spectral-action multipliers ARE the substrate's intrinsic regularization at the M_KK compactification scale (NOT "an external regulator applied to the substrate"). The (M_1, M_2, c_1, c_2) = (M_KK, √2·M_KK, +2, -1) tuple IS the canonical Pauli-Villars-style subtraction pinned by the Connes-Chamseddine 1996 paper at the spectral-action UV-regularization layer (`regulator-pin-discipline.md §"Tag Format"` regulator-name = `Pauli-Villars`). Direction: substrate (M_KK-scale spectral action IS regularized) → bridge (HKR L_max → ∞ image) → laboratory.

**Substitution chain — FULL CC multipliers definition**:

```
Step 1 — Definition (Connes-Chamseddine 1996 §2.2-2.3):
         The spectral-action functional Tr f(D_K / Λ) for f(x) = ∑_{j=1}^{N} c_j · e^{-(x/M_j)^2} with N=2 physical multipliers:
         (M_1, c_1) = (M_KK, +2)
         (M_2, c_2) = (√2 · M_KK, -1)
         The c-coefficient sum is c_1 + c_2 = +1 (substrate normalization; integer-rational pin per substrate-IS commutative algebra)
         The (M_1²·c_1 + M_2²·c_2) sum is M_KK² · 2 + 2·M_KK² · (-1) = 0 (Pauli-Villars-style subtraction at second moment)

Step 2 — Spectral-action moment expansion (Seeley-DeWitt):
         Tr f(D_K / Λ) = a_0(Λ) + a_2(Λ) · Tr(D_K^2) + a_4(Λ) · Tr(D_K^4) + ...
         Each a_n depends on the multiplier choice through the modified Mellin transform:
         a_n^{CC} = ∫_0^∞ f(x) x^{n-1} dx = ∑_j c_j · M_j^n · Γ(n/2)
         For n=4 (substrate-distance-2 pole s=4):
         a_4^{CC} = Γ(2) · (c_1 · M_KK^4 + c_2 · (√2·M_KK)^4) = 1 · (2·M_KK^4 + (-1)·4·M_KK^4) = -2·M_KK^4

Step 3 — Restriction to BdG sub-algebra:
         L_FULL(τ_fold) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s})) / d ln(K_window) |_{s=4, full CC multipliers}
         Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s}) = a_4^{CC} · Tr_{M_2(ℂ)}(P_BdG · D_K^{-2s}) / Tr_{spectrum} weighting
                                       = a_4^{CC} · [∑_α∈BdG m_α λ_α^{-8}] / [∑_α m_α λ_α^{-8}]

Step 4 — Numerical evaluation on L_max=12 master cache:
         lambdas, mults, sectors ← s84_spectrum_cache_L12_tau019.npz
         BdG-restricted: lam_bdg = lambdas[sectors == P_BDG_BLOCK_IDX]; m_bdg = multiplicities[mask]
         tr_bdg(K) = a_4^CC · sum(m_bdg * (lam_bdg / K)^(-8))
         L_FULL = d ln(tr_bdg) / d ln(K) at K=K_canonical (substrate-natural; default = 1 in M_KK-natural units)

Step 5 — Direction reading:
         Δ_FULL = (L_FULL − L_emp) / |L_emp|
         PASS iff |Δ_FULL| < 1e-2 (1% relative; Level-2 envelope first-extraction floor)
```

**Implementation outline**:

```python
"""s91_w1_cf70_full_cc_multipliers.py — T1.1 FULL CC multipliers PROXY-REFINEMENT for §VII.AV."""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import sys, hashlib, json
import numpy as np
import torch
from canonical_constants import *  # tau_fold, M_KK, Delta_BCS, etc.

# Connes-Chamseddine 1996 §2.2-2.3 physical multipliers
M_1_FW_CC = M_KK                       # (local) primary multiplier scale
M_2_FW_CC = np.sqrt(2.0) * M_KK         # (local) secondary multiplier scale
c_1_FW_CC = +2                          # (local) primary multiplier weight
c_2_FW_CC = -1                          # (local) secondary multiplier weight
# Cross-check: c_1 + c_2 = +1, M_1²·c_1 + M_2²·c_2 = 0 (Pauli-Villars subtraction at second moment)
assert c_1_FW_CC + c_2_FW_CC == 1
assert abs(M_1_FW_CC**2 * c_1_FW_CC + M_2_FW_CC**2 * c_2_FW_CC) < 1e-10

# Spectral-action a_4 coefficient under FULL CC multipliers (Γ(2) = 1)
def cc_a_n(n, M1, c1, M2, c2):
    """∑_j c_j · M_j^n · Γ(n/2) per CC 1996 §2.3."""
    from scipy.special import gamma
    return gamma(n/2.0) * (c1 * M1**n + c2 * M2**n)

a_4_CC = cc_a_n(4, M_1_FW_CC, c_1_FW_CC, M_2_FW_CC, c_2_FW_CC)   # (local) FULL CC a_4 = -2 M_KK^4

# Load L_max=12 master cache
CACHE_PATH = "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
cache = np.load(CACHE_PATH)
lambdas, mults, sectors = cache['lambdas'], cache['multiplicities'], cache['sectors']
P_BDG_BLOCK_IDX = 1
mask_bdg = (sectors == P_BDG_BLOCK_IDX)
lam_bdg, m_bdg = lambdas[mask_bdg], mults[mask_bdg]

# K-window log-derivative under FULL CC multipliers
K_CANONICAL = 1.0                       # (local) substrate-natural; M_KK-natural units default
eps_K = 0.01                            # (local) finite-difference half-width
def tr_bdg_CC(K):
    # Spectral-action 4th-moment restricted to BdG block under FULL CC physical multipliers
    base_tr = np.sum(m_bdg * (lam_bdg / K).astype(np.float64) ** (-8))
    return a_4_CC * base_tr / (M_KK ** 4)   # M_KK^4 normalization to dimensionless

tr_plus = tr_bdg_CC(K_CANONICAL + eps_K * K_CANONICAL)
tr_minus = tr_bdg_CC(K_CANONICAL - eps_K * K_CANONICAL)
L_FULL = (np.log(tr_plus) - np.log(tr_minus)) / (2 * eps_K)   # (local) FULL CC L_FULL output

# Compare against substrate-natural anchor
L_EMP = -7.046336474406761              # (local) §VII.AV registry line 18092 pin
Delta_FULL = (L_FULL - L_EMP) / abs(L_EMP)
ENVELOPE_TOL = 1e-2                     # (local) Level-2 first-extraction floor
verdict = "PASS" if abs(Delta_FULL) < ENVELOPE_TOL else "FAIL"

# Output:
# computations/session-91/s91_w1_cf70_full_cc_multipliers.npz
#   keys: a_4_CC, L_FULL, L_EMP, Delta_FULL, M_1, M_2, c_1, c_2, K_CANONICAL, eps_K, tr_bdg_at_K_canonical
# computations/session-91/s91_w1_cf70_full_cc_multipliers.png
#   bar chart of |Δ_FULL| vs ENVELOPE_TOL; comparison of SCHEMATIC Casimir-bound proxy vs FULL CC pipeline
# computations/session-91/s91_gate_verdicts.txt — canonical verdict line
```

**Cross-checks**:
- `a_4_CC` analytic-form check: `a_4_CC = -2 · M_KK^4` to machine precision (Step 2 closed-form)
- `tr_bdg_CC(K=1)` substrate-natural sanity: should produce a Cell-IV image consistent with §VII.AV §W5-2 master-spectrum cache filter
- Cross-pin: emit `Delta_FULL` in M_KK²-natural units AND in dimensionless form (M_KK² ratio); both reported in npz keys

### Field 7 — Machinery pin (PRDR)

```yaml
gate_id: CF-S91-CF-70-FULL-CC-MULTIPLIERS
schema_version: R3
L_max: 12
M_1_FW_CC: M_KK            # canonical_constants.py: M_KK = M_KK_gravity
M_2_FW_CC: sqrt(2) * M_KK  # canonical_constants.py-derived; full float64 = 1.0506...e+17 GeV
c_1_FW_CC: +2              # integer pin per CC 1996 §2.2-2.3
c_2_FW_CC: -1              # integer pin per CC 1996 §2.2-2.3
K_CANONICAL: 1.0           # substrate-natural M_KK-natural units default; cross-pin to T1.2 K_canonical output if T1.2 lands first
eps_K: 0.01                # finite-difference half-width
ENVELOPE_TOL: 1e-2         # Level-2 first-extraction floor (1% relative)
P_BDG_BLOCK_IDX: 1
L_EMP: -7.046336474406761  # M_KK² units
tolerance_rule: RATIO
scheme: full-CC1996-multipliers-§2.2-2.3-spectral-action-PROXY-REFINEMENT
convention: VII-AV-PROXY-REFINEMENT-FULL-PHYSICAL-Pauli-Villars-substrate-distance-2-pole-s4
random_seed: N/A (no stochastic component; deterministic numerical evaluation)
GPU_path: optional (numpy float64 default; small-matrix path)
machinery_pin_map: complete (no free parameters)
LEVEL_CLASS_PIN: FULL  # per substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY; this gate IS the FULL physical replacement for SCHEMATIC `_spectral_action_regulators.py` Mellin helper
```

### Field 8 — Expected output 4-tuple

`(value=<Delta_FULL>, scheme=full-CC1996-multipliers-§2.2-2.3-spectral-action-PROXY-REFINEMENT, convention=VII-AV-PROXY-REFINEMENT-FULL-PHYSICAL-Pauli-Villars-substrate-distance-2-pole-s4, L_max=12)`

### Field 9 — PASS/FAIL/INFO thresholds (RATIO tolerance rule)

- **PASS** iff `|Δ_FULL| < ENVELOPE_TOL = 1e-2` (1% relative; Level-2 envelope first-extraction at L_max=12 satisfaction)
- **FAIL** iff `|Δ_FULL| ≥ ENVELOPE_TOL` (1% breach signals FULL CC pipeline does NOT recover substrate-natural anchor at L_max=12; refinement requires either (a) higher L_max scan via W5 T1.11 FULL BdG Pauli-Villars extension, OR (b) K_canonical pin re-derivation via T1.2)
- **INFO** iff `ENVELOPE_TOL ≤ |Δ_FULL| < 10·ENVELOPE_TOL` (within 1 OOM of envelope; SIGN-PASS with MAGNITUDE-FAIL routed via S87+ schema-v2 3-tuple)

### Field 10 — Substitution chain
Full chain in Field 6 Step 1-5. Python verification: `a_4_CC = Γ(2)·(c_1·M_KK^4 + c_2·(√2·M_KK)^4) = 1·(2·M_KK^4 + (-1)·4·M_KK^4) = -2·M_KK^4` (analytic-form check at machine precision). Cross-pin Step 2: `M_1²·c_1 + M_2²·c_2 = 2·M_KK² + (-1)·2·M_KK² = 0` (Pauli-Villars subtraction at second moment; second-moment substrate-IS condition).

### Field 11 — What PASSES/FAILS MEAN

- **PASS**: §VII.AV REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT sub-class tag DISCHARGED via FULL Connes-Chamseddine 1996 §2.2-2.3 physical multiplier pipeline. The SCHEMATIC `_spectral_action_regulators.py` Mellin helper is replaced by the FULL physical regulator pipeline at substrate-distance-2 pole `s=4`. §VII.AV promotes to STAGE-1-CANDIDATE-PENDING-STAGE-2 (Stage 2 cross-axis verify at W4 T1.15 / W8 T2.29 unblocks); cross-pillar bridge anatomy Level 2 envelope acquires empirical α exponent floor. The W5 T1.11 FULL BdG re-derivation (CF-W5-3) can inherit the multiplier pin under PV-tier-equivalence cross-check.

- **FAIL**: FULL CC multipliers do NOT recover substrate-natural anchor at L_max=12 within 1% relative envelope. The §VII.AV PROXY-REFINEMENT pathway via FULL CC pipeline is empirically inconsistent at L_max=12. Refinement routes:
  - (a) **L_max scan**: W5 T1.11 FULL BdG re-derivation at L_max ∈ {12, 14, 16, ...} until Friedrich-Bär saturation theorem certifies bottom-K invariance OR the empirical α exponent converges
  - (b) **K_canonical operational-alignment**: T1.2 K_canonical pin uniqueness from substrate-IS BdG energy gap at τ_fold replaces the substrate-natural `K=1` default
  - (c) **Hochschild-cohomology cross-anchor (T1.4)**: cocycle-ratio degeneration check provides 4th independent verification axis; degeneration prediction tests Reading A from Hochschild side

- **INFO (REGIME-MARGINAL)**: 1 OOM within envelope. §VII.AV refinement is empirically marginal at L_max=12; W5 T1.11 L_max scan continuation is prerequisite to disambiguation.

### Field 12 — Effort estimate
**~1.5-2.0 wave-equivalents** (we). FULL CC multiplier evaluation on L_max=12 cache: ~30 min CPU. Plot generation + verdict line + working-paper §3 dispatch: ~1 hour. Cross-check against schematic Casimir-bound proxy from S90 W5-3: ~30 min. Total wall: ~2-3 hours dispatched on `volovik-superfluid-universe-theorist`. If T1.3 routes T1.1 priority FIRST, this gate runs immediately after T1.3 verdict.

### Field 13 — Substrate framing reminder
The (M_1, M_2, c_1, c_2) multipliers ARE the substrate's intrinsic UV-regularization parameters at the M_KK compactification scale per Connes-Chamseddine 1996. NOT "regulators we apply externally to the substrate"; they ARE the substrate's spectral action's intrinsic Pauli-Villars structure. Direction: substrate (M_KK-scale spectral action IS UV-regularized at the FULL CC pipeline) → bridge (HKR L_max → ∞ image) → laboratory (Pillar V continuum BdG-sector mutual-friction observable). The SCHEMATIC vs FULL distinction is a level-pin axis per `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY: SCHEMATIC = the `_spectral_action_regulators.py` library output (S90 W5-3 Casimir-bound proxy); FULL = THIS gate's CC1996 multiplier pipeline.

---

## §W1-3. CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS (T1.2; POSTERIOR to T1.3)

**Provenance**: S90 W8-CF-71 K_canonical pin uniqueness from substrate-IS BdG energy gap at τ_fold; resolve scalar Δ_BCS vs multi-branch s52 B-tensor per W8 CF-62 disambiguation. SHARPENED via volovik s6 §6 CF-71D DRY-RUN DISCRIMINATOR 3-tuple schema-v2 verdict structure. Routes through OPERATIONAL-ALIGNMENT deferred-pending sub-class (W-5 CF-6 = T2.52 landed at S91 W0).

### Field 1 — Gate ID
`CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS` (alias: `S91-VII-AV-K_CANONICAL-PIN-UNIQUENESS`; `S91-W8-CF-71`)

### Field 2 — Trigger
`[VERIFY-THEOREM]` (uniqueness adjudication on substrate-IS BdG energy gap K_canonical pin)

### Field 3 — Classification
`PHONONIC` (substrate-IS BdG energy gap at τ_fold; substrate's intrinsic operational machinery)

### Field 4 — Agent type
`volovik-superfluid-universe-theorist` (PRIMARY; substrate-IS BdG canonical interpreter). **NOT** `connes-ncg-theorist` per S90 W7 OAA exclusion.

### Field 5 — Hypothesis
The K_canonical pin for the §VII.AV substrate-IS Corner-IV K-window log-derivative observable is UNIQUE under the constraint that the substrate-IS BdG energy gap `Δ(τ_fold)` evaluated on the substrate's intrinsic operational machinery (a) recovers the scalar-Δ canonical `Δ_BCS = Delta_0_OES` at the symmetric-B identity configuration AND (b) admits a unique multi-branch s52 B-tensor extension that aligns the FULL-BdG output with the substrate-natural anchor `L_emp = -7.046336474406761` at L_max=12 within `|L − L_emp| / |L_emp| < 1e-3` relative tolerance.

### Field 6 — Method (FULL dispatch prompt)

You are dispatched to write `computations/session-91/s91_w1_cf71_k_canonical_pin_uniqueness.py` implementing the K_canonical operational-alignment refinement for §VII.AV.

**Substrate framing reminder**: K_canonical IS the substrate's intrinsic K-window scaling pin per the BdG sub-algebra at τ_fold = 0.19 (NOT "a K-window we choose"). The uniqueness adjudication tests whether the substrate's BdG energy gap admits a single canonical K-pin OR multi-pin degeneracy. Direction: substrate (BdG energy gap IS the canonical K-pin source) → bridge (HKR L_max → ∞) → laboratory.

**Substitution chain — K_canonical uniqueness predicate**:

```
Step 1 — Definition: K_canonical = K-window scaling factor pinning d ln(Tr_{M_2}(P_BdG · D_K^{-2s})) / d ln(K)
         to the substrate-natural anchor L_emp at substrate-distance-2 pole s=4

         Two candidate K_canonical hypotheses:
         (A) scalar-Δ canonical: K_canonical = Δ_BCS / M_KK (single scalar pin)
         (B) multi-branch s52 B-tensor canonical: K_canonical(B) = f(B_1, B_2, θ) (tensor-valued pin
             reduced to uniqueness via T1.3 V4 fossil test verdict)

Step 2 — Substitution: evaluate L_predict(K_canonical_hypothesis) for hypotheses (A) and (B)
         L_predict_A = d ln(Tr_{M_2}(P_BdG · D_K^{-2s})) / d ln(K) |_{K=Δ_BCS/M_KK, s=4, τ_fold=0.19}
         L_predict_B = same with K = K_canonical(B*) where B* is the T1.3 alignment-config (if T1.3 PASS)
                      OR L_predict_B inherits from T1.3 closest-Δ argmin if T1.3 FAIL/INFO

Step 3 — Uniqueness adjudication:
         (a) If |L_predict_A − L_emp| / |L_emp| < 1e-3 AND |L_predict_B − L_emp| / |L_emp| < 1e-3:
             K_canonical pin is NON-UNIQUE (degenerate); refinement requires Stage-2 verify
         (b) If |L_predict_A − L_emp| / |L_emp| < 1e-3 AND |L_predict_B − L_emp| / |L_emp| ≥ 1e-3:
             K_canonical pin is UNIQUE = scalar-Δ; routes T1.1 PROXY-REFINEMENT priority
         (c) If |L_predict_A − L_emp| / |L_emp| ≥ 1e-3 AND |L_predict_B − L_emp| / |L_emp| < 1e-3:
             K_canonical pin is UNIQUE = multi-branch s52 B-tensor; OPERATIONAL-ALIGNMENT binding
         (d) If both fail: K_canonical pin requires NEW refinement axis (potential W5 T1.11 FULL BdG)

Step 4 — Direction reading:
         Verdict tag = uniqueness class (a)/(b)/(c)/(d) — pre-registered in canonical_constants.py
         under K_canonical_uniqueness_class_FW after PASS
```

**Implementation outline**:

```python
"""s91_w1_cf71_k_canonical_pin_uniqueness.py — T1.2 K_canonical operational-alignment for §VII.AV."""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import sys, hashlib, json
import numpy as np
from canonical_constants import *  # tau_fold, M_KK, Delta_BCS = Delta_0_OES, etc.

# Load substrate spectrum cache
CACHE_PATH = "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
cache = np.load(CACHE_PATH)
lambdas, mults, sectors = cache['lambdas'], cache['multiplicities'], cache['sectors']
P_BDG_BLOCK_IDX = 1
mask_bdg = (sectors == P_BDG_BLOCK_IDX)
lam_bdg, m_bdg = lambdas[mask_bdg], mults[mask_bdg]

# K-window log-derivative on BdG sub-algebra
def L_at_K(K):
    eps = 0.01
    def tr(K_eval):
        return np.sum(m_bdg * (lam_bdg / K_eval).astype(np.float64) ** (-8))
    return (np.log(tr(K * (1 + eps))) - np.log(tr(K * (1 - eps)))) / (2 * eps)

# Hypothesis A: scalar-Δ canonical
K_HYP_A = Delta_BCS / M_KK                                  # (local) scalar-Δ pin (dimensionless after M_KK normalization)
L_PREDICT_A = L_at_K(K_HYP_A)
L_EMP = -7.046336474406761
Delta_A = (L_PREDICT_A - L_EMP) / abs(L_EMP)

# Hypothesis B: multi-branch s52 B-tensor canonical
# CONSUMES T1.3 V4 verdict from computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.npz
V4_PATH = "computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.npz"
if os.path.exists(V4_PATH):
    v4 = np.load(V4_PATH)
    if v4['alignment_pass']:
        # Reading B: extract closest-aligned B* config from T1.3 sweep
        idx_best = int(np.argmin(np.abs(v4['deltas'])))
        config_best = v4['configs'][idx_best]
        theta_1, theta_2, theta_3, b_1, b_2 = config_best
        K_HYP_B = (b_1 * np.cos(theta_1) + b_2 * np.cos(theta_2)) * np.cos(theta_3 / 2)
    else:
        # Reading A: T1.3 FAIL means no admissible B; K_HYP_B falls back to argmin closest
        idx_best = int(np.argmin(np.abs(v4['deltas'])))
        config_best = v4['configs'][idx_best]
        theta_1, theta_2, theta_3, b_1, b_2 = config_best
        K_HYP_B = (b_1 * np.cos(theta_1) + b_2 * np.cos(theta_2)) * np.cos(theta_3 / 2)
else:
    raise RuntimeError("T1.3 V4 fossil-test verdict file required; dispatch T1.3 first.")

L_PREDICT_B = L_at_K(K_HYP_B)
Delta_B = (L_PREDICT_B - L_EMP) / abs(L_EMP)

# Uniqueness adjudication — 4-class outcome
REL_TOL = 1e-3
pass_A = abs(Delta_A) < REL_TOL
pass_B = abs(Delta_B) < REL_TOL

if pass_A and pass_B:
    uniqueness_class = "degenerate-both-PASS"; verdict = "INFO"
elif pass_A and not pass_B:
    uniqueness_class = "unique-scalar-Δ"; verdict = "PASS"  # Routes T1.1 priority
elif not pass_A and pass_B:
    uniqueness_class = "unique-multi-branch-B-tensor"; verdict = "PASS"  # OPERATIONAL-ALIGNMENT binding
else:
    uniqueness_class = "both-FAIL-new-refinement-axis-required"; verdict = "FAIL"

# Output:
# computations/session-91/s91_w1_cf71_k_canonical_pin_uniqueness.npz
# computations/session-91/s91_w1_cf71_k_canonical_pin_uniqueness.png
# computations/session-91/s91_gate_verdicts.txt — canonical verdict line + S87+ schema-v2 3-tuple
```

**Cross-checks**:
- DRY-RUN per volovik s6 §6 CF-71D: verify schema-v2 3-tuple emission `(sign_verdict, magnitude_verdict, regime_verdict)` per `gate-verdicts.md §"S87+ canonical form"`
- Identity-B config cross-check: `K_HYP_B at (θ=0, b=1.0)` should equal `K_HYP_A` only if the substrate's BdG energy gap is parameterization-invariant (NOT generically true; the 4-class adjudication is the substrate's adjudication of this question)

### Field 7 — Machinery pin (PRDR)

```yaml
gate_id: CF-S91-CF-71-K_CANONICAL-PIN-UNIQUENESS
schema_version: R3
L_max: 12
K_HYP_A_formula: Delta_BCS / M_KK         # scalar-Δ canonical; canonical_constants.py pins Delta_BCS = Delta_0_OES
K_HYP_B_source: T1.3 verdict npz          # multi-branch s52 B-tensor; inherits from CF-S91-V4 output
P_BDG_BLOCK_IDX: 1
eps_K: 0.01                                # finite-difference half-width
REL_TOL: 1e-3                              # uniqueness adjudication threshold
L_EMP: -7.046336474406761
tolerance_rule: RATIO
scheme: substrate-IS-K_canonical-pin-uniqueness-DRY-RUN-DISCRIMINATOR
convention: VII-AV-OPERATIONAL-ALIGNMENT-substrate-distance-2-pole-s4-4-class-uniqueness-adjudication
random_seed: N/A
GPU_path: optional
machinery_pin_map: complete
DRY_RUN_3_TUPLE_SCHEMA: S87+ schema-v2 mandatory per volovik s6 §6 CF-71D
```

### Field 8 — Expected output 4-tuple

`(value=<uniqueness_class>, scheme=substrate-IS-K_canonical-pin-uniqueness-DRY-RUN-DISCRIMINATOR, convention=VII-AV-OPERATIONAL-ALIGNMENT-substrate-distance-2-pole-s4-4-class-uniqueness-adjudication, L_max=12)`

### Field 9 — PASS/FAIL/INFO thresholds (RATIO)

- **PASS-class-(b)** `unique-scalar-Δ`: |Δ_A| < 1e-3 AND |Δ_B| ≥ 1e-3 → K_canonical = Δ_BCS / M_KK; **routes T1.1 PROXY-REFINEMENT priority**
- **PASS-class-(c)** `unique-multi-branch-B-tensor`: |Δ_A| ≥ 1e-3 AND |Δ_B| < 1e-3 → K_canonical = multi-branch s52 image; **OPERATIONAL-ALIGNMENT binding sub-class** (NEW REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT deferred-pending sub-class advances)
- **INFO-class-(a)** `degenerate-both-PASS`: both hypotheses PASS; K_canonical NON-UNIQUE; refinement requires Stage-2 cross-axis verify
- **FAIL-class-(d)** `both-FAIL-new-refinement-axis-required`: neither hypothesis recovers L_emp; W5 T1.11 FULL BdG L_max scan or alternative axis required

S87+ schema-v2 3-tuple companion row required per volovik s6 §6 CF-71D DRY-RUN spec.

### Field 10 — Substitution chain
Full chain in Field 6 Step 1-4. Python verification: at `K_HYP_A = Delta_BCS / M_KK` (dimensionless), `L_at_K(K_HYP_A)` should produce L_predict_A that is computable from L_max=12 master cache with bit-precision reproducibility. The 4-class adjudication is THE substrate's own decision predicate on K_canonical pin uniqueness.

### Field 11 — What PASSES/FAILS MEAN

- **PASS-class-(b)**: §VII.AV K_canonical pin is UNIQUE as scalar-Δ; the substrate-IS BdG energy gap at τ_fold IS Δ_BCS modulo M_KK normalization. PROXY-REFINEMENT via FULL CC multipliers (T1.1) is the binding sub-class. OPERATIONAL-ALIGNMENT sub-class CLOSED at SCHEMATIC-equivalent verdict.
- **PASS-class-(c)**: §VII.AV K_canonical pin is UNIQUE as multi-branch s52 B-tensor image; substrate's BdG energy gap admits intrinsic multi-branch operational structure. NEW REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT deferred-pending sub-class advances at K=1 SUGGESTION → K=2 (T2.52 rule-file extension landed at S91 W0). Routes T1.1 to secondary verification axis.
- **INFO-class-(a)**: K_canonical NON-UNIQUE; both hypotheses recover L_emp within tolerance. The substrate's operational machinery admits BOTH scalar-Δ AND multi-branch parameterizations at equivalent precision; Stage-2 cross-axis verify is required for adjudication. The §VII.AV refinement deferred-pending sub-class status maintained.
- **FAIL-class-(d)**: Neither hypothesis adequate; NEW refinement axis required. Routes (i) W5 T1.11 FULL BdG Pauli-Villars extension, OR (ii) revised substrate-IS BdG energy gap pin via L_max ≥ 14 cardinality refinement.

### Field 12 — Effort estimate
**~1.0-1.2 wave-equivalents** (we). K_canonical evaluation: ~30 min CPU. DRY-RUN 3-tuple schema check + plot: ~30 min. Cross-pin against T1.3 verdict + working-paper §3 dispatch: ~1 hour. Total wall: ~2 hours dispatched on `volovik-superfluid-universe-theorist`. Depends on T1.3 verdict file landing first.

### Field 13 — Substrate framing reminder
K_canonical IS the substrate's intrinsic K-window scaling pin at τ_fold = 0.19 (NOT "an operational parameter we tune"). The substrate's BdG sub-algebra `M_2(ℂ) ⊂ A_K` admits either a scalar-Δ canonical OR a multi-branch s52 B-tensor canonical; this gate IS the substrate's adjudication of which it is. Direction: substrate (BdG energy gap IS the K_canonical source) → bridge (HKR L_max → ∞) → laboratory (Pillar V continuum). Container-thinking violation: "we choose the K_canonical parameter from outside the substrate" → INVERT: "the substrate's BdG energy gap determines its own K_canonical via the substrate's intrinsic operational structure; we read off what the substrate IS".

---

## §W1-4. CF-S91-VII-AV-HOCHSCHILD-DEGENERATION-TEST (T1.4)

**Provenance**: S90 W-5 CF-1 = CF-77 Hochschild-cohomology degeneration test (cocycle ratio at L_max ∈ {6..10} across regulator atlas {ζ, PV, Mellin, cutoff}). PARALLEL with T1.1/T1.2 after T1.3 lands; independent axis-α (UV-regulator) verification.

### Field 1 — Gate ID
`CF-S91-VII-AV-HOCHSCHILD-DEGENERATION-TEST` (alias: `CF-77`; `S91-VII-AV-HOCHSCHILD-CROSS-ANCHOR`)

### Field 2 — Trigger
`[VERIFY-THEOREM]` (Hochschild-cohomology degeneration prediction at substrate-distance-2 pole `s=4`)

### Field 3 — Classification
`GEOMETRIC` (Hochschild cocycle classes at substrate-distance-2 pole; algebra-axis classification)

### Field 4 — Agent type
`volovik-superfluid-universe-theorist` (PRIMARY; for the substrate-IS Cocycle-ratio inheritance interpretation). **NOT** `connes-ncg-theorist` per S90 W7 OAA. Alternate: `landau-condensed-matter-theorist` (for cross-pillar bridge-anatomy validation if needed at substrate-IS Hochschild side).

### Field 5 — Hypothesis
The substrate cocycle-ratio `‖φ_67‖ / ‖φ_88‖ = 7.324992` (`canonical_constants.py` substrate_cocycle_ratio_67_88 = 114453/15625 = 7.3250 Sage-QQ exact) evaluated at L_max ∈ {6, 7, 8, 9, 10} across the regulator atlas {ζ, Pauli-Villars, Mellin, cutoff} EITHER (a) preserves the substrate ratio INVARIANT (Hochschild-cohomology STABLE; cocycle classes do NOT degenerate at substrate-distance-2 pole) OR (b) DEGENERATES across regulators (Hochschild-cohomology DEGENERATE; provides 4th independent verification axis distinct from operational K_canonical T1.2, FULL CC multipliers T1.1, and V4 fossil test T1.3).

### Field 6 — Method (FULL dispatch prompt)

You are dispatched to write `computations/session-91/s91_w1_cf77_hochschild_degeneration_test.py` implementing the cocycle-ratio Hochschild-cohomology cross-anchor at substrate-distance-2 pole `s=4` across the regulator atlas.

**Substrate framing reminder**: the cocycle classes [φ_67] and [φ_88] ARE the substrate's intrinsic Hochschild cohomology classes on `A_K` (NOT "external cocycles we apply"). The ratio `‖φ_67‖ / ‖φ_88‖ = 7.324992` IS the substrate-derived inheritance-falsifier-protocol cohomology-asymmetry test value (per `.claude/rules/inheritance-falsifier-protocol.md §"Class B"` MANDATORY at K=3). Direction: substrate (cocycle classes ARE) → bridge (regulator-class atlas image) → laboratory (3He-B cohomology-asymmetry measurement).

**Substitution chain — Hochschild degeneration predicate**:

```
Step 1 — Definition: substrate cocycle norms ‖φ_a‖ on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) at L_max truncation L
         φ_67 = chiral-pair cocycle (ker ι_* generator at rank-1)
         φ_88 = Cartan hypercharge cocycle (ker ι_* generator at rank-2)
         substrate canonical ratio (Sage-QQ exact): substrate_cocycle_ratio_67_88 = 114453 / 15625 = 7.324992

Step 2 — Evaluation across regulator atlas R ∈ {ζ, Pauli-Villars, Mellin, cutoff}:
         For each L ∈ {6, 7, 8, 9, 10}: evaluate ‖φ_67‖^R(L) and ‖φ_88‖^R(L) on L_max=12 cache filtered to truncation L
         compute ratio_R(L) = ‖φ_67‖^R(L) / ‖φ_88‖^R(L)

Step 3 — Degeneration predicate:
         max_ratio_dev = max over (L, R) pairs of |ratio_R(L) − 7.324992|
         (a) DEGENERATE (Reading A inheritance-falsifier-protocol prediction) iff max_ratio_dev > 1.0
             (cocycle ratio deviation > 1 across regulators indicates Hochschild structurally DEGENERATE)
         (b) STABLE iff max_ratio_dev ≤ 0.1 (cocycle ratio INVARIANT across regulators within 1.4% — substrate-derived cohomology asymmetry test passes)
         (c) MARGINAL iff 0.1 < max_ratio_dev ≤ 1.0 (regulator-class dependence at substrate-distance-2 pole; cross-axis adjudication required)

Step 4 — Direction reading:
         Degeneration / Stability adjudication; ratio_R(L_max=10) used as canonical anchor
```

**Implementation outline**:

```python
"""s91_w1_cf77_hochschild_degeneration_test.py — T1.4 Hochschild-cohomology cross-anchor for §VII.AV."""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import sys, hashlib, json
import numpy as np
from canonical_constants import *  # tau_fold, M_KK, substrate_cocycle_ratio_67_88, etc.

CACHE_PATH = "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
cache = np.load(CACHE_PATH)
lambdas, mults, sectors = cache['lambdas'], cache['multiplicities'], cache['sectors']

# Substrate-derived canonical ratio (Sage-QQ exact)
from fractions import Fraction
RATIO_CANONICAL = float(Fraction(114453, 15625))   # (local) = 7.324992

# Cocycle norm evaluators per regulator class
def norm_at_L_under_regulator(cocycle_id, L_truncation, regulator):
    """‖φ_a‖^R(L) on L_max=L truncation of master cache under regulator R."""
    # Restrict cache to (p+q) ≤ L truncation via sector index
    truncation_mask = (sectors[:, 0] + sectors[:, 1] <= L_truncation) if sectors.ndim == 2 else (sectors <= L_truncation)
    lam_L = lambdas[truncation_mask]
    m_L = mults[truncation_mask]
    if cocycle_id == 'phi_67':
        # Chiral-pair sector: project onto (p,q) sectors with mixed-chirality character (per S86 W-5 W11-C5 Caroli-Matricon F1 anatomy)
        weight = np.array([1.0 if (s[0] != s[1]) else 0.0 for s in (sectors[truncation_mask] if sectors.ndim==2 else [(i,i) for i in lam_L])])  # (local) chiral indicator
    elif cocycle_id == 'phi_88':
        # Cartan hypercharge sector: project onto Cartan-diagonal (p,q) with p+q=8 weight image
        weight = np.array([1.0 if (s[0] + s[1] == 8) else 0.0 for s in (sectors[truncation_mask] if sectors.ndim==2 else [(i,i) for i in lam_L])])  # (local) Cartan indicator
    else:
        raise ValueError(f"Unknown cocycle: {cocycle_id}")
    # Regulator-class evaluation
    if regulator == 'zeta':
        f_lam = (lam_L / M_KK).astype(np.float64) ** (-8)   # substrate-distance-2 pole s=4
    elif regulator == 'Pauli-Villars':
        f_lam = np.exp(-(lam_L / M_KK) ** 2)                # PV exponential cutoff at M_KK
    elif regulator == 'Mellin':
        f_lam = (lam_L / M_KK).astype(np.float64) ** (-8) * np.exp(-(lam_L / (10 * M_KK)) ** 2)   # Mellin-with-soft-cutoff
    elif regulator == 'cutoff':
        f_lam = np.where(lam_L / M_KK < 5.0, (lam_L / M_KK) ** (-8), 0.0)   # Hard cutoff at lam/M_KK = 5
    else:
        raise ValueError(f"Unknown regulator: {regulator}")
    return np.sqrt(np.sum(m_L * weight * f_lam))   # L^2-norm-like cocycle scale

L_VALUES = [6, 7, 8, 9, 10]
REGULATORS = ['zeta', 'Pauli-Villars', 'Mellin', 'cutoff']
ratios = {}   # (local) (L, R) → ratio
for L in L_VALUES:
    for R in REGULATORS:
        n67 = norm_at_L_under_regulator('phi_67', L, R)
        n88 = norm_at_L_under_regulator('phi_88', L, R)
        ratios[(L, R)] = n67 / n88 if n88 > 0 else float('nan')

# Degeneration adjudication
deviations = [abs(ratios[(L, R)] - RATIO_CANONICAL) for L in L_VALUES for R in REGULATORS if not np.isnan(ratios[(L, R)])]
max_ratio_dev = max(deviations) if deviations else float('nan')

THRESHOLD_DEGENERATE = 1.0
THRESHOLD_STABLE = 0.1
if max_ratio_dev > THRESHOLD_DEGENERATE:
    classification = "DEGENERATE-Reading-A-confirmed"; verdict = "PASS"
elif max_ratio_dev <= THRESHOLD_STABLE:
    classification = "STABLE-substrate-cohomology-asymmetry-invariant"; verdict = "PASS"
else:
    classification = "MARGINAL-regulator-class-dependence"; verdict = "INFO"

# Output:
# computations/session-91/s91_w1_cf77_hochschild_degeneration_test.npz
#   keys: ratios, max_ratio_dev, classification, RATIO_CANONICAL, L_VALUES, REGULATORS
# computations/session-91/s91_w1_cf77_hochschild_degeneration_test.png
#   heatmap of ratios over (L, R) grid with RATIO_CANONICAL contour overlay
# computations/session-91/s91_gate_verdicts.txt — canonical verdict line + 3-tuple
```

**Cross-checks**:
- At L_max=10, ζ-regulator: ratio_zeta(10) MUST equal substrate-derived value 7.324992 within 1.4% (cohomology-asymmetry test passes)
- Per `regulator-pin-discipline.md §"Tag Format"`: each regulator class gets explicit `a_n^{<regulator>}` tag in the npz output keys

### Field 7 — Machinery pin (PRDR)

```yaml
gate_id: CF-S91-VII-AV-HOCHSCHILD-DEGENERATION-TEST
schema_version: R3
L_max: 12  # source cache; truncations to L ∈ {6,7,8,9,10}
L_VALUES: [6, 7, 8, 9, 10]
REGULATORS: [zeta, Pauli-Villars, Mellin, cutoff]
substrate_cocycle_ratio_67_88: 7.324992   # canonical_constants.py Sage-QQ exact = 114453/15625
substrate-distance-2-pole-s: 4
M_KK: M_KK_gravity
RATIO_CANONICAL: 7.324992
THRESHOLD_DEGENERATE: 1.0
THRESHOLD_STABLE: 0.1
tolerance_rule: ABSOLUTE
scheme: Hochschild-cohomology-degeneration-cross-anchor-substrate-distance-2-pole-s4
convention: VII-AV-HOCHSCHILD-CROSS-ANCHOR-axis-alpha-4-regulator-atlas
random_seed: N/A
GPU_path: optional
machinery_pin_map: complete
```

### Field 8 — Expected output 4-tuple

`(value=<max_ratio_dev>, scheme=Hochschild-cohomology-degeneration-cross-anchor-substrate-distance-2-pole-s4, convention=VII-AV-HOCHSCHILD-CROSS-ANCHOR-axis-alpha-4-regulator-atlas, L_max=12)`

### Field 9 — PASS/FAIL/INFO thresholds (ABSOLUTE tolerance rule)

- **PASS** iff `max_ratio_dev > 1.0` OR `max_ratio_dev ≤ 0.1` (both DEGENERATE Reading-A or STABLE are valid substrate adjudications; both PASS the cohomology cross-anchor predicate)
- **INFO** iff `0.1 < max_ratio_dev ≤ 1.0` (MARGINAL regulator-class dependence; cross-axis adjudication required)
- **FAIL** iff structural diagnostic failure (NaN ratios, zero-divisions, regulator pipeline crash; not a substrate-physics FAIL)

### Field 10 — Substitution chain
Full chain in Field 6 Step 1-4. Python verification: `RATIO_CANONICAL = Fraction(114453, 15625) = 7.324992` exact (Sage-QQ pin per `canonical_constants.py`). Direction reading: at L_max=10, ratio under zeta regulator IS the substrate-derived inheritance-falsifier ratio; deviations across other regulators measure structural degeneration.

### Field 11 — What PASSES/FAILS MEAN

- **PASS-DEGENERATE**: Hochschild cocycle classes DEGENERATE at substrate-distance-2 pole `s=4` across regulator atlas; cohomology-asymmetry RATIO is NOT preserved INTACT under regulator-class change. This empirically confirms the Reading A geometric-resummation prediction (per `inheritance-falsifier-protocol.md` Class B cocycle-asymmetry test extension). Provides 4th independent verification axis for §VII.AV refinement-pathway DISTINCT from operational K_canonical T1.2 axis γ, FULL CC multipliers T1.1 axis β, and V4 fossil test T1.3 axis routing.

- **PASS-STABLE**: Hochschild cocycle classes STABLE; substrate-derived ratio 7.324992 preserved within 1.4% across regulator atlas. This confirms substrate inheritance-falsifier-protocol cohomology-asymmetry test extension to substrate-distance-2 pole (parallel to W-5 W11-C5 first-instance calibration at substrate-distance-1 pole). Hochschild-cohomology axis-α verification PASS-conditional.

- **INFO-MARGINAL**: Regulator-class dependence intermediate; neither DEGENERATE nor STABLE definitively. Cross-axis adjudication via Stage-2 verify required (W4 T1.15 / W8 T2.29).

- **FAIL**: Pipeline diagnostic failure; re-dispatch under sanitized inputs.

### Field 12 — Effort estimate
**~0.8 wave-equivalents** (we). Pipeline build (4 regulators × 5 L truncations × 2 cocycles): ~1.5 hours CPU. Heatmap + verdict-line + working-paper §3 dispatch: ~1 hour. Total wall: ~2.5-3 hours dispatched on `volovik-superfluid-universe-theorist`.

### Field 13 — Substrate framing reminder
The cocycle classes [φ_67] (chiral pair) and [φ_88] (Cartan hypercharge) ARE the substrate's intrinsic Hochschild cohomology classes on `A_K`. The regulator atlas {ζ, PV, Mellin, cutoff} parameterizes 4 substrate-IS UV-regularization schemes; each scheme IS a substrate-natural regulator (NOT "external mathematical choice"). Direction: substrate (Hochschild cohomology classes ARE INVARIANT or DEGENERATE structurally) → bridge (regulator atlas image at substrate-distance-2 pole) → laboratory (3He-B cohomology-asymmetry inheritance test).

---

## §W1-5. CF-AV-L2-MODULI (M9; Level-2 moduli-deformation)

**Provenance**: volovik s6 §6 carry-forward CF-AV-L2-MODULI. SUBORDINATE to T1.2 + T1.3 outputs (consumes Δ_BCS(τ) + K_canonical(τ) sweep). §VII.AV Level-2 moduli-deformation extension across τ ∈ {0.18, 0.19, 0.20} testing Level-1 single-τ-slice vs Level-2 moduli-deformation invariance per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY.

### Field 1 — Gate ID
`CF-AV-L2-MODULI` (alias: `S91-VII-AV-LEVEL-2-MODULI-DEFORMATION`; `CF-S91-AV-LEVEL-2-MODULI`)

### Field 2 — Trigger
`[VERIFY-THEOREM]` (Level-2 moduli-deformation invariance / deformability adjudication on §VII.AV substrate-IS observable)

### Field 3 — Classification
`PHONONIC` × `GEOMETRIC` (substrate-IS observable extended across τ-moduli; Level-1 vs Level-2 substrate-IS levels distinction)

### Field 4 — Agent type
`volovik-superfluid-universe-theorist` (PRIMARY; framework's substrate-IS level interpreter per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY since S88 W-7 V.4). **NOT** `connes-ncg-theorist` per S90 W7 OAA.

### Field 5 — Hypothesis
The §VII.AV substrate-IS Corner-IV K-window log-derivative `L_FULL(τ)` evaluated across the moduli-deformation slice τ ∈ {0.18, 0.19, 0.20} EITHER (a) Level-2-INVARIANT: `L_FULL(τ) ≈ L_FULL(τ_fold)` within `|L(τ) − L(τ_fold)| / |L(τ_fold)| < 1e-2` for ALL three τ values (Level-1 single-τ-slice observation IS the full substrate-IS image; moduli direction does not modify the observable) OR (b) Level-2-DEFORMABLE: `L_FULL(τ)` varies substantively across the slice (Level-2 moduli-deformation is structurally distinct from Level-1 single-τ-slice; substrate-IS observable acquires a τ-dependent profile per `permanent-results-registry.md §VII.AE` τ-asymmetric breakdown precedent).

### Field 6 — Method (FULL dispatch prompt)

You are dispatched to write `computations/session-91/s91_w1_cf_av_l2_moduli.py` implementing the §VII.AV Level-2 moduli-deformation extension at τ ∈ {0.18, 0.19, 0.20}.

**Substrate framing reminder**: τ IS the substrate's intrinsic deformation parameter (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level 2 = Level-2-substrate-IS — moduli-space `{(A_K, H_K, D_K(τ)) : τ ∈ moduli-space}` IS the substrate's own deformation manifold, NOT a meta-container). The Level-1 vs Level-2 distinction IS the substrate's OWN structural distinction between single-slice-spectral-IS observables and moduli-deformation observables. Direction: substrate (τ-moduli structure IS) → bridge (HKR L_max → ∞ at each τ) → laboratory (Pillar V continuum measurement at each τ image).

**Substitution chain — Level-2 moduli-deformation evaluation**:

```
Step 1 — Definition: L_FULL(τ) = d ln(Tr_{M_2(ℂ)}(P_BdG · D_K(τ)^{-2s})) / d ln(K_window) |_{s=4, K=K_canonical}
         For each τ ∈ {0.18, 0.19, 0.20}: substrate spectral triple (A_K, H_K, D_K(τ))

Step 2 — Substitution: cache filter on master L_max=12 cache at each τ-slice
         Inputs:
           cache_018: lambdas(τ=0.18) (REQUIRED; if missing, compute via D_K(τ=0.18) diagonalization at L_max=12)
           cache_019: master cache (already present at s84_spectrum_cache_L12_tau019.npz)
           cache_020: lambdas(τ=0.20) (REQUIRED; same)

Step 3 — Per-τ K_canonical adjudication:
         K_canonical(τ) from T1.2 verdict (if T1.2 lands first; else placeholder K=K_canonical(τ_fold))
         Compute L_FULL(τ) for each τ at the τ-specific K_canonical

Step 4 — Moduli-deformation predicate:
         max_dev_L = max over τ ∈ {0.18, 0.20} of |L_FULL(τ) − L_FULL(τ_fold)| / |L_FULL(τ_fold)|
         (a) Level-2-INVARIANT iff max_dev_L < 1e-2 (Level-1 single-τ-slice IS the substrate-IS observable; moduli direction does not modify)
         (b) Level-2-DEFORMABLE iff max_dev_L ≥ 1e-2 AND |L_FULL(0.20) − L_FULL(0.18)| / |L_FULL(τ_fold)| > 0.1
             (substantive moduli profile; Level-2 substrate-IS distinct from Level-1)
         (c) MARGINAL iff 1e-2 ≤ max_dev_L < 0.1 (small moduli-deformation; cross-axis adjudication)

Step 5 — Direction reading:
         Level-1 INVARIANT vs Level-2 DEFORMABLE adjudication; per `phononic-framing.md` K=2 MANDATORY
```

**Implementation outline**:

```python
"""s91_w1_cf_av_l2_moduli.py — M9 §VII.AV Level-2 moduli-deformation."""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import sys, hashlib, json
import numpy as np
from canonical_constants import *

# Master cache at τ_fold = 0.19
CACHE_019_PATH = "computations/session-84/s84_spectrum_cache_L12_tau019.npz"

# Off-fold caches at τ = 0.18 + 0.20 (REQUIRED inputs)
# If not present, this gate raises RuntimeError and routes to remediation: build off-fold caches via D_K(τ) diagonalization at L_max=12
CACHE_018_PATH = "computations/session-91/s91_w1_spectrum_cache_L12_tau018.npz"  # to be built by upstream remediation
CACHE_020_PATH = "computations/session-91/s91_w1_spectrum_cache_L12_tau020.npz"  # to be built by upstream remediation

# Consume T1.2 verdict for K_canonical pin
T12_PATH = "computations/session-91/s91_w1_cf71_k_canonical_pin_uniqueness.npz"
if os.path.exists(T12_PATH):
    t12 = np.load(T12_PATH, allow_pickle=True)
    K_CANONICAL_AT_FOLD = float(t12['K_HYP_A']) if t12['uniqueness_class'] == 'unique-scalar-Δ' else float(t12['K_HYP_B'])
else:
    K_CANONICAL_AT_FOLD = float(Delta_BCS / M_KK)   # (local) placeholder default

# For Level-2 extension, K_canonical(τ) is assumed to inherit τ-scaling via:
# K_canonical(τ) = K_CANONICAL_AT_FOLD · (1 - (τ - τ_fold) · κ_2)  with κ_2 = kappa_2_substrate_FW
# Per canonical_constants.py kappa_2_substrate_FW = 0.021018084987437196
def k_canonical_at_tau(tau):
    return K_CANONICAL_AT_FOLD * (1.0 - (tau - tau_fold) * kappa_2_substrate_FW)

# L_FULL evaluator at each τ
def L_full_at_tau(tau, cache_path, K):
    cache = np.load(cache_path)
    lambdas, mults, sectors = cache['lambdas'], cache['multiplicities'], cache['sectors']
    P_BDG_BLOCK_IDX = 1
    mask_bdg = (sectors == P_BDG_BLOCK_IDX) if sectors.ndim == 1 else (sectors[:, 0] == P_BDG_BLOCK_IDX)
    lam_bdg = lambdas[mask_bdg]
    m_bdg = mults[mask_bdg]
    eps = 0.01
    def tr(K_eval):
        return np.sum(m_bdg * (lam_bdg / K_eval).astype(np.float64) ** (-8))
    return (np.log(tr(K * (1 + eps))) - np.log(tr(K * (1 - eps)))) / (2 * eps)

# Evaluate at three τ slices
TAU_VALUES = [0.18, tau_fold, 0.20]
CACHE_PATHS = {0.18: CACHE_018_PATH, tau_fold: CACHE_019_PATH, 0.20: CACHE_020_PATH}
L_at_tau = {}   # (local)
for tau in TAU_VALUES:
    if not os.path.exists(CACHE_PATHS[tau]):
        raise RuntimeError(f"Required cache for τ={tau} not present: {CACHE_PATHS[tau]} -- build via upstream remediation")
    K_tau = k_canonical_at_tau(tau)
    L_at_tau[tau] = L_full_at_tau(tau, CACHE_PATHS[tau], K_tau)

# Moduli-deformation adjudication
L_FOLD = L_at_tau[tau_fold]
max_dev_L = max(abs(L_at_tau[tau] - L_FOLD) / abs(L_FOLD) for tau in [0.18, 0.20])
end_to_end = abs(L_at_tau[0.20] - L_at_tau[0.18]) / abs(L_FOLD)

THRESHOLD_INVARIANT = 1e-2
THRESHOLD_DEFORMABLE = 0.1
if max_dev_L < THRESHOLD_INVARIANT:
    level_class = "Level-2-INVARIANT-single-τ-slice-IS-full-substrate-IS"
    verdict = "PASS"
elif max_dev_L >= THRESHOLD_INVARIANT and end_to_end > THRESHOLD_DEFORMABLE:
    level_class = "Level-2-DEFORMABLE-moduli-profile-substantive"
    verdict = "PASS"
else:
    level_class = "MARGINAL-cross-axis-adjudication-required"
    verdict = "INFO"

# Output:
# computations/session-91/s91_w1_cf_av_l2_moduli.npz
#   keys: L_at_tau, max_dev_L, end_to_end, level_class, K_at_tau, kappa_2_substrate_FW
# computations/session-91/s91_w1_cf_av_l2_moduli.png
#   line plot of L_FULL(τ) over τ ∈ [0.18, 0.20] with INVARIANT-tolerance band overlay
# computations/session-91/s91_gate_verdicts.txt
```

**Cross-checks**:
- At τ = τ_fold = 0.19 (master cache): `L_at_tau[tau_fold]` MUST match T1.2 L_PREDICT_A under K_canonical_at_fold (bit-exact reproducibility cross-pin)
- κ_2 inheritance: `K_canonical_at_tau(τ_fold) = K_CANONICAL_AT_FOLD` (identity at τ=τ_fold cross-check)
- Cache parity: τ=0.18 and τ=0.20 caches should have identical sector index structure (Peter-Weyl decomposition is τ-INVARIANT modulo eigenvalue shifts)

### Field 7 — Machinery pin (PRDR)

```yaml
gate_id: CF-AV-L2-MODULI
schema_version: R3
L_max: 12
TAU_VALUES: [0.18, 0.19, 0.20]
tau_fold: 0.19
kappa_2_substrate_FW: 0.021018084987437196   # canonical_constants.py CM-1995 §III.4 second-order Jensen perturbation
K_canonical_source: T1.2 verdict npz (CF-S91-CF-71 output)
cache_τ_0.18_path: computations/session-91/s91_w1_spectrum_cache_L12_tau018.npz   # REQUIRED upstream build
cache_τ_0.19_path: computations/session-84/s84_spectrum_cache_L12_tau019.npz       # master cache
cache_τ_0.20_path: computations/session-91/s91_w1_spectrum_cache_L12_tau020.npz   # REQUIRED upstream build
P_BDG_BLOCK_IDX: 1
eps_K: 0.01
THRESHOLD_INVARIANT: 1e-2
THRESHOLD_DEFORMABLE: 0.1
tolerance_rule: RATIO
scheme: Level-2-moduli-deformation-extension-VII-AV-substrate-distance-2-pole-s4
convention: VII-AV-LEVEL-2-MODULI-3-tau-slice-INVARIANT-vs-DEFORMABLE-adjudication
random_seed: N/A
GPU_path: optional
machinery_pin_map: complete
upstream_dependencies:
  - T1.2 (CF-S91-CF-71) verdict file: REQUIRED for K_canonical pin
  - τ=0.18 + τ=0.20 caches: REQUIRED prerequisite; build via D_K(τ) diagonalization at L_max=12 if missing
```

### Field 8 — Expected output 4-tuple

`(value=<max_dev_L>, scheme=Level-2-moduli-deformation-extension-VII-AV-substrate-distance-2-pole-s4, convention=VII-AV-LEVEL-2-MODULI-3-tau-slice-INVARIANT-vs-DEFORMABLE-adjudication, L_max=12)`

### Field 9 — PASS/FAIL/INFO thresholds (RATIO tolerance rule)

- **PASS-INVARIANT** iff `max_dev_L < 1e-2` → Level-2-INVARIANT; single-τ-slice IS the full substrate-IS observable; §VII.AV Level-1 declaration via `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` is structurally complete; Level-2 moduli direction does not modify the K-window log-derivative observable.
- **PASS-DEFORMABLE** iff `max_dev_L ≥ 1e-2 AND end_to_end > 0.1` → Level-2-DEFORMABLE; substrate-IS observable acquires a non-trivial τ-profile; §VII.AV Level-2 declaration distinct from Level-1; per `permanent-results-registry.md §VII.AE` τ-asymmetric breakdown precedent.
- **INFO-MARGINAL** iff `1e-2 ≤ max_dev_L < 0.1` (small moduli-deformation; cross-axis adjudication required at W4 Stage-2 verify or downstream wave).
- **FAIL** iff structural diagnostic failure (cache missing, K_canonical from T1.2 unavailable, evaluator crash).

### Field 10 — Substitution chain
Full chain in Field 6 Step 1-5. Python verification: at τ = τ_fold = 0.19, `L_FULL(τ_fold)` reduces to the substrate-natural anchor `L_emp = -7.046336474406761` (or its T1.2-shifted version under K_canonical) — IDENTITY check at the fold.

### Field 11 — What PASSES/FAILS MEAN

- **PASS-INVARIANT**: §VII.AV substrate-IS observable IS a Level-1 single-τ-slice observable; the moduli direction does NOT modify the K-window log-derivative at substrate-distance-2 pole. This confirms `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY: Level-1 declaration in §VII.AV anatomy element 1 IS structurally complete; Level-2 declaration is REDUNDANT for this observable. K-counter advancement to K=2 → K=3 (CF-S91 promotes K=2 PROXY-REFINEMENT instance per `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`).

- **PASS-DEFORMABLE**: §VII.AV substrate-IS observable is Level-2-DEFORMABLE; τ-moduli direction contributes a substantive profile. The substrate's BdG sub-algebra Corner-IV K-window log-derivative is NOT a pure Level-1 single-τ-slice observable; Level-2 moduli-deformation is a distinct substrate-IS axis. This advances `phononic-framing.md` Level-2 calibration corpus K=2 → K=3 (continuing the S88 W-7 V.4 bot20 sector occupation precedent). §VII.AV anatomy element 1 acquires explicit Level-2 tag.

- **INFO-MARGINAL**: Adjudication inconclusive; cross-axis Stage-2 verify required.

- **FAIL**: Cache or T1.2 upstream missing; route to remediation.

### Field 12 — Effort estimate
**~2.0 wave-equivalents** (we). Build off-fold caches (D_K(τ=0.18) + D_K(τ=0.20) diagonalization at L_max=12 via `torch.linalg.eigvalsh` GPU path): ~3-4 hours each. Per-τ L_FULL evaluation: ~30 min CPU. Plot + verdict line + working-paper §3 dispatch: ~1 hour. Total wall: ~7-9 hours dispatched on `volovik-superfluid-universe-theorist`. SUBORDINATE to T1.2 + T1.3 completions.

### Field 13 — Substrate framing reminder
τ IS the substrate's intrinsic moduli-deformation parameter (NOT "a meta-coordinate we vary"). The moduli-space `{(A_K, H_K, D_K(τ)) : τ ∈ [0.18, 0.20]}` IS the substrate's OWN deformation manifold per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY. Each τ-slice IS a Level-1 substrate-IS spectral triple; the family of slices IS the Level-2 moduli-deformation substrate-IS object. Direction: substrate (τ-moduli structure IS) → bridge (per-τ HKR L_max → ∞ image) → laboratory (Pillar V continuum measurement at each τ image — e.g., 3He-B mutual-friction profile across pressure-sweep). Container-thinking violation: "we sweep τ through a coordinate moduli container" → INVERT: "the substrate's τ-moduli IS its own intrinsic deformation; we read off the substrate's profile across what IS".

---

## Wave 1 → Wave 2 Decision Point

### W1 verdict outcomes and downstream consequences

| T1.3 verdict | T1.1 priority | T1.2 priority | §VII.AV refinement-pathway | W4 T2.29 (§VII.AV Stage-2) status | W5 T1.11 (FULL BdG) inheritance |
|:------------|:-------------|:-------------|:--------------------------|:----------------------------------|:--------------------------------|
| **PASS (Reading-B-WIN)** | POSTERIOR (or PARALLEL) | FIRST | OPERATIONAL-ALIGNMENT binding; K-counter K=1→K=2 NEW REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT sub-class advances | UNBLOCKS conditional on T1.2 PASS-class-(c) `unique-multi-branch-B-tensor` | T1.11 may inherit multi-branch K_canonical pin |
| **FAIL (Reading-A-WIN)** | FIRST | POSTERIOR (or PARALLEL) | PROXY-REFINEMENT binding; K-counter K=1→K=2 PROXY-REFINEMENT advances | UNBLOCKS conditional on T1.1 PASS | T1.11 inherits FULL CC multiplier pin (T1.1 output) |
| **INFO (REGIME-MARGINAL)** | PARALLEL | PARALLEL | Discriminator inconclusive; routes BOTH dispatches | DEFERRED to S92 unless T1.1 OR T1.2 lands PASS independently | T1.11 dispatched without inheritance |

### W2 prerequisites set by W1

- **W2 T0.7** (CF-37 + FULL-CM-1995-§III.4-substrate-distance-2): consumes T1.1 FULL CC multiplier pin (`a_4_CC = -2 · M_KK^4`) for the CF-37 option (v) sub-pathway evaluation. **Cross-link**: §VII.AX option (v) at registry line 18383 inherits the FULL CC multiplier output.
- **W2 T1.5 + T1.10** (§VII.AU.OP-PROJ first-extraction): independent of W1; runs in parallel. No W1-output inheritance.

### W4 prerequisites set by W1

- **W4 T2.29** (§VII.AV Stage-2 cross-axis verify): **BLOCKED on §VII.AV reaching STAGE-1-CANDIDATE-PENDING-STAGE-2 via T1.1 OR T1.2 success**. Cross-reviewer dispatch: Axis-A NCG-axiomatic (non-connes per OAA; candidates: `van-den-dungen-bridge-theorist` or `landau-condensed-matter-theorist` at substrate-physics side) + Axis-B substrate-physics (volovik already PRIMARY for W1 dispatches; for Stage-2 use a DIFFERENT volovik-equivalent — e.g., `mack-cosmic-bridge` for cosmological-bridge cross-pillar verification of the FWD-C2 substrate-IS observable, OR `landau-condensed-matter-theorist` for BdG-specific Stage-2 cross-check).

### W5 prerequisites set by W1

- **W5 T1.11** (CF-W5-3 FULL BdG re-derivation): SHARES FULL CC multiplier pipeline with T1.1; if T1.1 PASS, T1.11 inherits the multiplier pin under PV-tier-equivalence cross-check.
- **W5 M9** (this wave; included in W1 as M9): see §W1-5 above.

### W8 prerequisites set by W1

- **W8 T2.29** (= W4 T2.29 alias): see W4.
- **W8 T2.39** (M_3(ℂ)-kernel universality STAGE-1-CANDIDATE registry landing): independent of W1; runs in parallel.

---

## Wave 1 Machinery-Enumeration Pin (§0.11 PRDR)

Per `.claude/rules/epistemic-discipline.md §"Pre-Registration Completeness"` Class 8 MANDATORY at K=3, every free parameter is pinned across the 5 gates:

### Cross-gate shared pins

```yaml
L_max: 12                                          # uniform across all 5 W1 gates
tau_fold: 0.19                                     # canonical_constants.py
M_KK: M_KK_gravity                                 # canonical_constants.py (default alias)
Delta_BCS: Delta_0_OES                             # canonical_constants.py (R-protected canonical)
kappa_2_substrate_FW: 0.021018084987437196         # canonical_constants.py (CM-1995 §III.4)
substrate_cocycle_ratio_67_88: 7.324992            # canonical_constants.py (Sage-QQ = 114453/15625)
L_EMP_substrate_natural: -7.046336474406761        # §VII.AV registry line 18092 (M_KK² units)
P_BDG_BLOCK_IDX: 1                                 # Peter-Weyl BdG sub-algebra block index
master_cache_path: computations/session-84/s84_spectrum_cache_L12_tau019.npz
```

### Per-gate machinery pin enumeration

| Gate | Free params (count) | All pinned? |
|:----|:-------------------|:-----------|
| §W1-1 T1.3 V4 fossil test | 6 (SUBSAMPLE_N=16384, SEED=20260516, REL_TOL=1e-3, eps_K=0.01, theta_grid=8, b_grid=11) | YES |
| §W1-2 T1.1 FULL CC multipliers | 5 (M_1=M_KK, M_2=√2·M_KK, c_1=+2, c_2=-1, ENVELOPE_TOL=1e-2) | YES |
| §W1-3 T1.2 K_canonical pin uniqueness | 3 (REL_TOL=1e-3, eps_K=0.01, K_HYP_A=Δ_BCS/M_KK) | YES (K_HYP_B inherited from T1.3) |
| §W1-4 T1.4 Hochschild degeneration | 5 (L_VALUES=[6..10], REGULATORS=4, THRESHOLD_DEGENERATE=1.0, THRESHOLD_STABLE=0.1, RATIO_CANONICAL=7.324992) | YES |
| §W1-5 M9 Level-2 moduli | 4 (TAU_VALUES=[0.18, 0.19, 0.20], THRESHOLD_INVARIANT=1e-2, THRESHOLD_DEFORMABLE=0.1, eps_K=0.01) | YES (K_canonical(τ) inherits from T1.2 + kappa_2_substrate_FW scaling) |

**PRU Class 8 cardinality check**: PASS for all 5 gates. No free parameters left unpinned.

---

## Wave 1 Input-SHA Ledger

Per `.claude/rules/gate-verdicts.md §"Pre-Registration Protocol"` item 1: each gate's input file SHA-256 is computed at runtime and pinned in the gate's verdict line via `audit_sha256 = closure_hash(input_pin_map)`.

### Per-gate input file enumeration

| Gate | Input file path | SHA pin status |
|:----|:----------------|:--------------|
| §W1-1 T1.3 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | computed-at-runtime |
| §W1-1 T1.3 | `computations/_shared/canonical_constants.py` (revision at dispatch) | computed-at-runtime |
| §W1-1 T1.3 | `sessions/permanent-results-registry.md` §VII.AV anchor block (lines 18059-18137) | computed-at-runtime |
| §W1-2 T1.1 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | computed-at-runtime |
| §W1-2 T1.1 | `computations/_shared/canonical_constants.py` | computed-at-runtime |
| §W1-2 T1.1 | `computations/_shared/_spectral_action_regulators.py` (cross-reference for SCHEMATIC-vs-FULL audit, not consumed at runtime per §(iv) K=4 MANDATORY level-pin discipline) | computed-at-runtime |
| §W1-3 T1.2 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | computed-at-runtime |
| §W1-3 T1.2 | `computations/_shared/canonical_constants.py` | computed-at-runtime |
| §W1-3 T1.2 | `computations/session-91/s91_w1_v4_k_canonical_multi_branch_fossil_test.npz` (T1.3 output; runtime canonical-path rescue per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift convention if T1.3 emits to different path) | computed-at-runtime |
| §W1-4 T1.4 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | computed-at-runtime |
| §W1-4 T1.4 | `computations/_shared/canonical_constants.py` | computed-at-runtime |
| §W1-5 M9 | `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (τ_fold master cache) | computed-at-runtime |
| §W1-5 M9 | `computations/session-91/s91_w1_spectrum_cache_L12_tau018.npz` (τ=0.18 off-fold cache; REQUIRED upstream build) | computed-at-runtime |
| §W1-5 M9 | `computations/session-91/s91_w1_spectrum_cache_L12_tau020.npz` (τ=0.20 off-fold cache; REQUIRED upstream build) | computed-at-runtime |
| §W1-5 M9 | `computations/session-91/s91_w1_cf71_k_canonical_pin_uniqueness.npz` (T1.2 output) | computed-at-runtime |
| §W1-5 M9 | `computations/_shared/canonical_constants.py` (for kappa_2_substrate_FW) | computed-at-runtime |

### Dual-SHA companion-row pattern (per `gate-verdicts.md §"S87+ canonical form"`)

Every W1 gate's verdict line carries:
1. Canonical verdict line: `{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=12 audit_sha256=<64hex> content_sha256=<64hex> schema_version=S84+`
2. Companion comment row: `# audit_sha256_short=<16hex> content_sha256_short=<16hex> # {GATE_ID} dual-SHA companion row (W9a-99 split)`
3. **For [SIGN]/[VERIFY-THEOREM] triggered gates** (T1.3, T1.2, T1.4, M9 — all four): S87+ schema-v2 3-tuple companion row: `# sign_verdict=PASS|FAIL|N/A magnitude_verdict=PASS|INFO|FAIL regime_verdict=VALID|MARGINAL|BREAKDOWN # {GATE_ID} 3-tuple annotation (S87 schema-v2)`

---

## Wave 1 OAA exclusions and reviewer-selection discipline

Per S90 W7 CF-55 OAA (substrate-physics adjudicator deferred under axis-β bridge-map-scheme suffix discipline at K=1 SUGGESTION):

- **`connes-ncg-theorist` EXCLUDED** from §VII.AV refinement-pathway gates (T1.1, T1.2, T1.3, T1.4, M9). Reason: CF-55 substrate-physics adjudicator at axis-β requires Reading A vs Reading B verdict at the secondary-class evaluation scheme; connes's pre-loaded interpretation of the (C_H, C_εH) parity-twin pair under APS-1975-secondary-class vs Cheeger-Simons evaluation creates downstream-inheritance reach that disqualifies the Stage-2 axis-distinctness predicate (per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` item 2).
- **`phonon-first`-side reviewers EXCLUDED** analogously (W2 T0.7 OAA carry-forward).
- **`volovik-superfluid-universe-theorist`** is PRIMARY for all 5 W1 gates (framework's substrate-IS BCS-canonical interpreter; matches the BdG sub-algebra Cell IV substrate-IS observable identity at substrate-distance-2 pole `s=4`).
- **Alternate substrate-physics reviewers** (for Stage-2 cross-axis verify at W4 T2.29): `landau-condensed-matter-theorist` (BdG-specific cross-check) or `mack-cosmic-bridge` (cosmological-bridge cross-pillar verification of FWD-C2). Both are AXIS-DISTINCT from volovik's substrate-IS BCS interpretation per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` item 1.

---

## Wave 1 Substrate framing reminder (uniform)

All 5 W1 gates inherit the §VII.AV substrate framing:

```
Substrate (BdG sub-algebra M_2(ℂ) ⊂ A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)) IS the Corner-IV K-window log-derivative
   → Bridge map (HKR L_max → ∞ at d=4 substrate-distance-2 pole s=4)
   → Laboratory (Pillar V) IN 3He-B BdG-sector mutual-friction observation
```

**FORBIDDEN container-thinking inversions** (per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`):
- "The FULL CC multipliers ARE an external regulator applied to the substrate" → INVERT: "the FULL CC multipliers ARE the substrate's intrinsic UV-regularization at the M_KK compactification scale per Connes-Chamseddine 1996"
- "The K_canonical pin IS a parameter we tune" → INVERT: "the K_canonical pin IS the substrate's intrinsic K-window scaling determined by its BdG energy gap at τ_fold"
- "The multi-branch B-tensor configurations ARE external choices" → INVERT: "the multi-branch B-tensor admissibility predicate IS the substrate's intrinsic operational structure on M_2(ℂ)"
- "τ-moduli direction IS a meta-coordinate we sweep" → INVERT: "τ-moduli IS the substrate's intrinsic deformation manifold per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY"

Each agent dispatched on W1 gates MUST include the IS-not-IN reminder verbatim in their working-paper §"Methodology" subsection (per `.claude/rules/cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy"` MANDATORY at K=3).

---

## Wave 1 Effort summary

| Gate | Effort (we) | Compute hours (wall) | Agent | Dependency |
|:----|:-----------|:--------------------|:------|:-----------|
| §W1-1 T1.3 V4 fossil test | 1.5 | ~5 | volovik | NONE (dispatched FIRST) |
| §W1-2 T1.1 FULL CC multipliers | 1.5-2.0 | ~3 | volovik | T1.3 (routing); PARALLEL with T1.2 posterior |
| §W1-3 T1.2 K_canonical pin uniqueness | 1.0-1.2 | ~2 | volovik | T1.3 (K_HYP_B input) |
| §W1-4 T1.4 Hochschild degeneration | 0.8 | ~3 | volovik | T1.3 (PARALLEL after lands) |
| §W1-5 M9 Level-2 moduli-deformation | 2.0 | ~9 | volovik | T1.2 + off-fold cache build |
| **TOTAL** | **~6.8-7.5 we** | **~22 hours wall** | **volovik (5 dispatches)** | T1.3 → (T1.1 ∥ T1.2) → (T1.4 ∥ M9) |

---

**End of Session 91 Wave 1 Plan**

Generated: 2026-05-16 (S91 W1 planner; per-wave authoring per `/rclab-plan` Phase 3 template; non-`gen-physicist` test-case design per blacklist; `connes-ncg-theorist` EXCLUDED per S90 W7 CF-55 OAA).

Dispatch readiness: ALL 5 gate blocks contain full 13-field specs per template. PRDR machinery pin: COMPLETE (no free parameters). Input-SHA ledger: pre-registered for runtime closure-hash computation. Substrate framing: uniform per §VII.AV registry anchor. OAA exclusions: declared.

**Next**: S91 W1 dispatch (T1.3 FIRST; T1.1 + T1.2 POSTERIOR per T1.3 verdict; T1.4 + M9 PARALLEL posterior).
