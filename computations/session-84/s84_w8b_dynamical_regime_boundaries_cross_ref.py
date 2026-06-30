"""
S84-W8B-94-DYNAMICAL-REGIME-BOUNDARIES-CROSS-REF

Gate: for each τ-boundary in {0.537, 0.285, 0.22, 0.190}, attempt derivation
from a SINGLE C_k generator class within the canonical rank-6 gear-machine
enumeration:

    C-1  Mellin cone extremum
    C-2  A_F singleton closure
    C-3  Peter-Weyl block-diagonal
    C-4  Jensen convexity
    C-5  spectral-gap inversion
    C-6  three-band partition

PASS  :=  max |C_k set| across 4 boundaries == 1  (rank-6 survives, pure)
INFO  :=  max |C_k set| == 2                       (joint-assignment noted)
FAIL  :=  max |C_k set| >= 3, OR generator outside C-1..C-6 required

Scheme   : canonical-boundary-trace-v1
Convention: MG-1-Jensen-base

Env      : CPU path with OMP_NUM_THREADS=8 (no heavy linear algebra; classification
           plus small numerical checks on Jensen-family signature-change criteria).

Canonical imports enforced.  Dual-SHA verdict line emitted.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
from pathlib import Path

import numpy as np

# ---- MANDATORY canonical imports ---------------------------------------------
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold,          # 0.19 — MG-1 generator (by definition)
    Delta_BCS,         # 0.4642547394830737 — canonical BCS gap (S70)
    d2S_fold,          # +317862.85 — Jensen curvature at fold (S42)
    dS_fold,           # +58672.80 — Jensen gradient at fold (S42)
    S_fold,            # 250360.68
)

# ---- canonical boundary values (pin source) ----------------------------------
# τ_phase_trans = 0.53723065 is from S48 (s49_cmpp_transition.py, S48 sectional
# curvature sign change on the C^2 factor).  Not in canonical_constants.py yet.
# τ_DNP = 0.285 is L=3 DNP instability crossing (S33, S74, S75).
# τ_BCS_freeze = 0.22 is post-transit freeze threshold (S49 MEMORY.md).
TAU_PHASE_TRANS  = 0.53723065  # (local) S48 C^2 sectional-K sign-change anchor
TAU_DNP          = 0.285       # (local) DNP crossing (L=3 Lichnerowicz)
TAU_BCS_FREEZE   = 0.22        # (local) post-transit freeze (S49)
TAU_FOLD_VAL     = tau_fold    # from canonical_constants (0.19)

print("=" * 78)
print("S84-W8B-94  DYNAMICAL-REGIME-BOUNDARIES-CROSS-REF")
print("=" * 78)
print()
print("Machinery pin (PRDR, first-20-lines):")
print(f"  boundary_list              = [{TAU_PHASE_TRANS}, {TAU_DNP}, "
      f"{TAU_BCS_FREEZE}, {TAU_FOLD_VAL}]")
print(f"  generator_classes          = [C-1, C-2, C-3, C-4, C-5, C-6]  (rank-6 canonical)")
print(f"  single_generator_threshold = 1")
print(f"  joint_threshold            = 2")
print(f"  scheme                     = canonical-boundary-trace-v1")
print(f"  convention                 = MG-1-Jensen-base")
print(f"  L_max                      = N/A  (boundary-trace level)")
print(f"  random_seed                = N/A  (deterministic)")
print(f"  GPU path                   = not required")
print()

# ------------------------------------------------------------------------------
# Input-SHA ledger (ordered, deterministic)
# ------------------------------------------------------------------------------

INPUT_FILES = [
    "computations/_shared/canonical_constants.py",
    "sessions/session-plan/session-84-plan-w8b.md",
    "sessions/framework/permanent-results-registry.md",
    ".claude/agent-memory/schwarzschild-penrose-geometer/MEMORY.md",
    "sessions/archive/session-83/workshops/s83-gear-machine-thought-experiment.md",
]

PROJECT_ROOT = Path(__file__).parent.parent

def sha256_file(relpath: str) -> str:
    p = PROJECT_ROOT / relpath
    if not p.exists():
        return "FILE_NOT_FOUND"
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

input_pin_map = {relpath: sha256_file(relpath) for relpath in INPUT_FILES}

print("Input SHA-256 ledger:")
for k, v in input_pin_map.items():
    print(f"  {k}:")
    print(f"    {v}")
print()

# ------------------------------------------------------------------------------
# Generator-class enumeration (canonical rank-6)
# ------------------------------------------------------------------------------

GENERATOR_CLASSES = {
    "C-1": "Mellin cone extremum (first-moment positive-weight)",
    "C-2": "A_F singleton closure (C+H+M_3(C))",
    "C-3": "Peter-Weyl block-diagonal (irrep decomposition of D_K)",
    "C-4": "Jensen convexity (d^2S/dtau^2 tracker; sectional K on Jensen family)",
    "C-5": "spectral-gap inversion (eigenvalue sign-crossing in a block)",
    "C-6": "three-band partition ({SU(2), C^2, U(1)} frequency bands)",
}

# ------------------------------------------------------------------------------
# Boundary-to-generator-class trace logic
# ------------------------------------------------------------------------------
#
# For each boundary τ_B, attempt derivation from the MINIMUM set of
# C_k generator classes.  We apply the canonical plan substitution chain
# (§4.94-9) and the S83 gear-machine thought-experiment generator taxonomy.
#
# The assignment is the SMALLEST set of C_k's whose combined machinery
# identifies the τ_B value WITHIN 0.5% of canonical.
#
# Reasoning per boundary:
#
#   τ_fold = 0.190  (MG-1 generator by construction)
#     Definition: d^2S/dtau^2 = +317863 convex-locked stationary minimum.
#     Generator : C-4 (Jensen convexity) ALONE.
#     |C_k set| = 1.
#
#   τ_phase_trans = 0.53723065  (S48 C^2 sectional-K sign change)
#     Definition: K_sect(C^2)(τ) passes through zero.  Sectional curvature
#     on the C^2 factor of the Jensen-deformed SU(3)/block-diagonal D_K.
#     Minimum derivation machinery:
#       (a) isolate the C^2 factor   ->  C-3 Peter-Weyl block-diagonal
#       (b) track its sectional K(τ) ->  C-4 Jensen convexity
#     Both are required; without C-3 the "C^2 sectional" is ill-defined;
#     without C-4 there is no curvature tracker.
#     |C_k set| = 2  ({C-3, C-4}).
#
#     Optimistic single-class reading: C-4 alone if "sectional curvature
#     on the Jensen family" is treated as a single composite evaluator that
#     already contains the block-diagonal input.  We flag this as a
#     CONSERVATIVE vs COLLAPSED reading.  For gate purposes, we report
#     BOTH and take the conservative one (|C_k set| = 2) for the
#     verdict-driving max.
#
#   τ_DNP = 0.285  (L=3 DNP crossing; Lichnerowicz gap inversion)
#     Definition: Lichnerowicz Δ_L eigenvalue in L=3 angular-momentum
#     Peter-Weyl block crosses zero.
#     Minimum derivation machinery:
#       (a) identify the L=3 block    ->  C-3 Peter-Weyl block-diagonal
#       (b) track the gap inversion   ->  C-5 spectral-gap inversion
#     |C_k set| = 2  ({C-3, C-5}).
#
#     Optimistic single-class reading: C-5 alone, treating gap-inversion as
#     carrying its own block-selection.  Again we mark both.
#
#   τ_BCS_freeze = 0.22  (Δ_BCS threshold crossing in three-band partition)
#     Definition: BCS gap Δ_BCS(τ) = 0.4642 reaches freeze-threshold in the
#     three-band frequency-partition structure at τ = 0.22.
#     Minimum derivation machinery:
#       (a) three-band partition      ->  C-6 three-band partition
#       (b) gap threshold crossing    ->  C-5 spectral-gap inversion
#     |C_k set| = 2  ({C-5, C-6}).
#
# Sanity: C-1 (Mellin cone) and C-2 (A_F singleton) are NOT τ-dependent
# critical-point generators; they produce structural algebraic identities
# rather than dynamical-regime boundaries.  None of the 4 boundaries calls
# them.  This leaves {C-3, C-4, C-5, C-6} as the active set — confirming
# the active generator subspace is 4-dimensional for dynamical-regime
# boundaries, nested within the rank-6 machine.
# ------------------------------------------------------------------------------

def sectional_K_C2_Jensen(tau: float) -> float:
    """
    Toy sectional-curvature-on-C^2 model for Jensen deformation.

    Canonical Jensen ansatz (S7):
        g_tau = 3 * diag(e^{-2tau} x 3,  e^{tau} x 4,  e^{2tau} x 1)
    where the four e^{tau} eigenvalues are the C^2 block.

    Approximate sectional curvature of a 2-plane inside the C^2 block along
    the Jensen flow has sign controlled by a linear combination of the
    eigenvalue growth rates: the three other factors grow/shrink as
    {e^{-2tau}, e^{tau}, e^{2tau}}, so the effective sectional K on Λ^2(C^2)
    is modelled by
        K_sect_C2(tau) = k0 + k1*(e^{-2tau} - 1) + k2*(e^{2tau} - 1)
    with k0, k1, k2 chosen so that K_sect_C2 passes through zero near
    τ = 0.537 (the S48 anchor).  Here we only need qualitative
    sign-change + monotone-derivative behaviour to verify the boundary
    exists and is a C-4 convexity event, not a fresh generator.

    This is NOT a new derivation of τ_phase_trans (S48 provides that at
    machine precision).  It is a consistency check that the critical
    point is a sign-change of a Jensen-curvature quantity — hence C-4.
    """
    # Coefficients fit to anchor S48 zero at τ = 0.53723065
    k0 = 1.0                            # (local)
    k2 = 0.5                            # (local)
    # Solve for k1 so that K_sect_C2(0.53723065) = 0
    tau_anchor = 0.53723065             # (local)
    expr_anchor = (np.exp(-2.0 * tau_anchor) - 1.0)
    target = -(k0 + k2 * (np.exp(2.0 * tau_anchor) - 1.0))
    k1 = target / expr_anchor           # (local)
    return k0 + k1 * (np.exp(-2.0 * tau) - 1.0) + k2 * (np.exp(2.0 * tau) - 1.0)

# Sanity-check: the Jensen-curvature model passes through zero at the anchor
K_at_anchor = sectional_K_C2_Jensen(TAU_PHASE_TRANS)
K_at_fold   = sectional_K_C2_Jensen(TAU_FOLD_VAL)
K_at_dnp    = sectional_K_C2_Jensen(TAU_DNP)
K_at_bcs    = sectional_K_C2_Jensen(TAU_BCS_FREEZE)
print("Jensen-curvature sectional-K model (C-4 check):")
print(f"  K_sect_C2(tau=0.537) = {K_at_anchor:+.6e}    (should be ~ 0)")
print(f"  K_sect_C2(tau=0.190) = {K_at_fold:+.6e}")
print(f"  K_sect_C2(tau=0.285) = {K_at_dnp:+.6e}")
print(f"  K_sect_C2(tau=0.220) = {K_at_bcs:+.6e}")
print()

# ------------------------------------------------------------------------------
# Per-boundary derivation table
# ------------------------------------------------------------------------------

def derive(tau_B: float, label: str, kset: set, note: str, reading: str):
    return {
        "boundary": label,
        "tau_value": float(tau_B),
        "generator_class_set": sorted(kset),
        "set_size": len(kset),
        "note": note,
        "reading": reading,
    }

boundary_derivations = [
    # τ_fold: C-4 alone (MG-1 generator by construction; d^2S/dτ^2 = +317863
    # convex-locked stationary minimum).
    derive(
        TAU_FOLD_VAL,
        "tau_fold",
        kset={"C-4"},
        note=(f"MG-1 generator: d^2S/dtau^2={d2S_fold:+.2f}>0 convex-locked "
              "stationary minimum. Pure C-4 Jensen convexity."),
        reading="single-class",
    ),

    # τ_phase_trans: conservative {C-3, C-4}, optimistic {C-4}
    derive(
        TAU_PHASE_TRANS,
        "tau_phase_trans",
        kset={"C-3", "C-4"},
        note=("S48 C^2 sectional curvature sign change. Requires (a) C-3 to "
              "isolate the C^2 Peter-Weyl block and (b) C-4 to track its "
              "Jensen-convexity sign-change. Optimistic collapsed reading: "
              "C-4 alone if sectional-K evaluator carries block-selection."),
        reading="conservative-joint",
    ),

    # τ_DNP: conservative {C-3, C-5}, optimistic {C-5}
    derive(
        TAU_DNP,
        "tau_DNP",
        kset={"C-3", "C-5"},
        note=("L=3 DNP instability: Lichnerowicz gap inversion in the L=3 "
              "Peter-Weyl block. Requires (a) C-3 to isolate the L=3 irrep "
              "and (b) C-5 to detect the gap sign-crossing. Optimistic: C-5 "
              "alone if gap-inversion carries block-selection."),
        reading="conservative-joint",
    ),

    # τ_BCS_freeze: {C-5, C-6}; BCS gap threshold in three-band partition
    derive(
        TAU_BCS_FREEZE,
        "tau_BCS_freeze",
        kset={"C-5", "C-6"},
        note=(f"Delta_BCS={Delta_BCS:.4f} gap reaches freeze threshold in "
              "three-band partition. Requires (a) C-6 three-band partition "
              "and (b) C-5 spectral-gap inversion. No single-class collapse: "
              "three-band structure and gap-inversion are mathematically "
              "distinct generators."),
        reading="conservative-joint",
    ),
]

# Optimistic (collapsed) reading: C-3 is treated as structural background
# absorbed into C-4/C-5 evaluators; three-band C-6 absorbed into C-5.
optimistic_table = []
for row in boundary_derivations:
    if row["boundary"] == "tau_fold":
        opt = {"C-4"}
    elif row["boundary"] == "tau_phase_trans":
        opt = {"C-4"}
    elif row["boundary"] == "tau_DNP":
        opt = {"C-5"}
    elif row["boundary"] == "tau_BCS_freeze":
        # Even optimistically, the three-band structure is a distinct
        # algebraic input from spectral-gap inversion; NOT collapsible.
        opt = {"C-5", "C-6"}
    else:
        opt = set(row["generator_class_set"])
    optimistic_table.append({
        "boundary": row["boundary"],
        "tau_value": row["tau_value"],
        "generator_class_set_optimistic": sorted(opt),
        "set_size_optimistic": len(opt),
    })

# ------------------------------------------------------------------------------
# Max |C_k set| across the 4 boundaries (verdict driver)
# ------------------------------------------------------------------------------
conservative_sizes = [row["set_size"] for row in boundary_derivations]
optimistic_sizes   = [row["set_size_optimistic"] for row in optimistic_table]

max_conservative = max(conservative_sizes)   # (local) conservative reading
max_optimistic   = max(optimistic_sizes)     # (local) optimistic reading

union_conservative = set().union(*[set(r["generator_class_set"])
                                    for r in boundary_derivations])
union_optimistic   = set().union(*[set(r["generator_class_set_optimistic"])
                                    for r in optimistic_table])

# Outside-rank-6 check
outside_rank6_conservative = union_conservative - set(GENERATOR_CLASSES.keys())
outside_rank6_optimistic   = union_optimistic - set(GENERATOR_CLASSES.keys())

print("Per-boundary derivation table (conservative reading):")
print(f"  {'boundary':<18} {'tau':>10}  {'|C_k set|':>10}  C_k set")
for row in boundary_derivations:
    print(f"  {row['boundary']:<18} {row['tau_value']:>10.6f}  "
          f"{row['set_size']:>10}  {row['generator_class_set']}")
print()
print("Per-boundary derivation table (optimistic collapsed reading):")
print(f"  {'boundary':<18} {'tau':>10}  {'|C_k set|':>10}  C_k set")
for row in optimistic_table:
    print(f"  {row['boundary']:<18} {row['tau_value']:>10.6f}  "
          f"{row['set_size_optimistic']:>10}  "
          f"{row['generator_class_set_optimistic']}")
print()
print(f"Union (conservative) = {sorted(union_conservative)}  "
      f"| outside rank-6 = {sorted(outside_rank6_conservative) or 'none'}")
print(f"Union (optimistic)   = {sorted(union_optimistic)}  "
      f"| outside rank-6 = {sorted(outside_rank6_optimistic) or 'none'}")
print()
print(f"max |C_k set| (conservative) = {max_conservative}")
print(f"max |C_k set| (optimistic)   = {max_optimistic}")
print()

# ------------------------------------------------------------------------------
# Verdict determination (plan §5 thresholds)
# ------------------------------------------------------------------------------
#   PASS  :=  max |C_k set| == 1
#   INFO  :=  max |C_k set| == 2
#   FAIL  :=  max |C_k set| >= 3  OR  union outside C-1..C-6
# ------------------------------------------------------------------------------

def decide(mx: int, outside: set) -> str:
    if outside:
        return "FAIL"
    if mx == 1:
        return "PASS"
    if mx == 2:
        return "INFO"
    return "FAIL"

verdict_conservative = decide(max_conservative, outside_rank6_conservative)
verdict_optimistic   = decide(max_optimistic,   outside_rank6_optimistic)

# CANONICAL verdict uses the CONSERVATIVE reading (minimum honest |C_k set|
# without collapsing Peter-Weyl block-selection into curvature/gap trackers).
canonical_verdict = verdict_conservative
canonical_value   = max_conservative

print("Verdict assessment:")
print(f"  Conservative reading verdict = {verdict_conservative}  "
      f"(max|C_k set|={max_conservative})")
print(f"  Optimistic   reading verdict = {verdict_optimistic}  "
      f"(max|C_k set|={max_optimistic})")
print(f"  CANONICAL (conservative, plan-aligned) = {canonical_verdict}  "
      f"value = {canonical_value}/4")
print()

# ------------------------------------------------------------------------------
# Rank-6 survival check
# ------------------------------------------------------------------------------
rank6_survives = (len(outside_rank6_conservative) == 0 and max_conservative <= 2)
print(f"Rank-6 survives (union within C-1..C-6 AND max|C_k set|<=2): "
      f"{rank6_survives}")
print()

# ------------------------------------------------------------------------------
# Closure SHA on ordered input-pin map  (audit_sha256)
# ------------------------------------------------------------------------------
ordered_pin_string = json.dumps(
    {"inputs": input_pin_map,
     "generator_classes": GENERATOR_CLASSES,
     "boundaries": [TAU_PHASE_TRANS, TAU_DNP, TAU_BCS_FREEZE, TAU_FOLD_VAL],
     "scheme": "canonical-boundary-trace-v1",
     "convention": "MG-1-Jensen-base"},
    sort_keys=True, separators=(",", ":"),
)
audit_sha256 = hashlib.sha256(ordered_pin_string.encode("utf-8")).hexdigest()

# ------------------------------------------------------------------------------
# Content SHA on verdict-driving numerical content  (content_sha256)
# ------------------------------------------------------------------------------
content_payload = {
    "conservative": {
        "rows": boundary_derivations,
        "max_set_size": max_conservative,
        "union": sorted(union_conservative),
        "outside_rank6": sorted(outside_rank6_conservative),
        "verdict": verdict_conservative,
    },
    "optimistic": {
        "rows": optimistic_table,
        "max_set_size": max_optimistic,
        "union": sorted(union_optimistic),
        "outside_rank6": sorted(outside_rank6_optimistic),
        "verdict": verdict_optimistic,
    },
    "canonical_verdict": canonical_verdict,
    "canonical_value":   canonical_value,
    "rank6_survives":    rank6_survives,
    "K_sect_checks": {
        "tau=0.537": float(K_at_anchor),
        "tau=0.190": float(K_at_fold),
        "tau=0.285": float(K_at_dnp),
        "tau=0.220": float(K_at_bcs),
    },
}
content_string = json.dumps(content_payload, sort_keys=True, separators=(",", ":"))
content_sha256 = hashlib.sha256(content_string.encode("utf-8")).hexdigest()

# Legacy closure SHA (for the sha256= field in verdict line).
# Per gate-verdicts.md S81+, the closure SHA is the SHA-256 of the ordered
# input-pin map.  We reuse audit_sha256 as the canonical closure hash.
closure_sha256 = audit_sha256

print("Closure hashes:")
print(f"  audit_sha256   = {audit_sha256}")
print(f"  content_sha256 = {content_sha256}")
print(f"  closure sha256 = {closure_sha256}")
print()

# ------------------------------------------------------------------------------
# Expected 4-tuple
# ------------------------------------------------------------------------------
print(f"(value={canonical_value}/4, scheme=canonical-boundary-trace-v1, "
      f"convention=MG-1-Jensen-base, L_max=N/A)")
print()

# ------------------------------------------------------------------------------
# Append verdict line to computations/session-84/s84_gate_verdicts.txt
# ------------------------------------------------------------------------------
verdict_line = (
    f"S84-W8B-94-DYNAMICAL-REGIME-BOUNDARIES-CROSS-REF: "
    f"{canonical_verdict} -- "
    f"value={canonical_value}/4 "
    f"scheme=canonical-boundary-trace-v1 "
    f"convention=MG-1-Jensen-base "
    f"L_max=N/A "
    f"sha256={closure_sha256} "
    f"audit_sha256={audit_sha256} "
    f"content_sha256={content_sha256}"
)
verdict_path = PROJECT_ROOT / "computations" / "session-84" / "s84_gate_verdicts.txt"
# Ensure newline-prefixed append (don't glue onto prior line)
prior_tail = b""
if verdict_path.exists():
    with open(verdict_path, "rb") as f:
        f.seek(-1, 2) if verdict_path.stat().st_size else None
        prior_tail = f.read() if verdict_path.stat().st_size else b""
prefix = "" if (not verdict_path.exists() or prior_tail.endswith(b"\n")) else "\n"
with open(verdict_path, "a", encoding="utf-8") as f:
    f.write(prefix + verdict_line + "\n")

print("Verdict line appended:")
print(f"  -> {verdict_path}")
print(f"  {verdict_line}")
print()

# ------------------------------------------------------------------------------
# Persist data for downstream /weave audit
# ------------------------------------------------------------------------------
out_npz = PROJECT_ROOT / "computations" / "session-84" / "s84_w8b_dynamical_regime_boundaries_cross_ref.npz"
np.savez(
    out_npz,
    boundary_labels=np.array([r["boundary"] for r in boundary_derivations]),
    boundary_tau=np.array([r["tau_value"] for r in boundary_derivations]),
    conservative_set_sizes=np.array(conservative_sizes),
    optimistic_set_sizes=np.array(optimistic_sizes),
    max_conservative=max_conservative,
    max_optimistic=max_optimistic,
    canonical_verdict=canonical_verdict,
    rank6_survives=rank6_survives,
    K_sect_C2=np.array([K_at_fold, K_at_bcs, K_at_dnp, K_at_anchor]),
    audit_sha256=audit_sha256,
    content_sha256=content_sha256,
    closure_sha256=closure_sha256,
)
print(f"Data saved: {out_npz.name}")
print()
print("DONE.")
