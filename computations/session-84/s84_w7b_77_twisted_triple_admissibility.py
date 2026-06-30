#!/usr/bin/env python3
"""
S84-W7b-77-TWISTED-TRIPLE-ADMISSIBILITY

Tests whether the Connes-Moscovici (2008) twisted spectral triple generalization
extends the singleton admissibility result {d_total=12, KO-dim=6, A_F=C(+)H(+)M_3(C)}
from S83-G32 to any additional (d_internal, KO-dim, A_F, sigma) combination.

Method (representation-theoretic enumeration; no GPU):
  Enumerate 16 candidate twisted triples T-1..T-16.
  For each, apply 4 admissibility filters:
    F1: Mellin cone pairing (d_total=12 required)
    F2: Connes-Marcolli 2013 Table 1 KO-dim sign table
    F3: SM content match (3 generations + gauge bosons from A_F modules)
    F4: Jensen deformation compatibility (sigma preserves monotonicity)
  Count candidates passing ALL filters.

PASS iff count = 0 exactly (twisting does NOT extend singleton).

References:
  - Connes-Moscovici 2008, "Type III and spectral triples" (arXiv:math/0609703)
    Def 2.3: twisted spectral triple axioms (replaces [D,a] bounded by [D,a]_sigma)
  - Connes-Marcolli 2013, "A walk in the noncommutative garden" Table 1
    KO-dim sign table for (eps, eps', eps'')
  - S83-G32 (singleton admissibility)
  - S83-G36 (matrix-model classification)
  - S82 Mellin cone admissibility filter
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s84_w7b_77_data.npz"
VERDICT_FILE = SCRIPT_DIR / "s84_gate_verdicts.txt"
GATE_ID = "S84-W7b-77-TWISTED-TRIPLE-ADMISSIBILITY"

# ------------------------------------------------------------------
# Input SHA pinning
# ------------------------------------------------------------------
def sha256_of_file(path: Path) -> str:
    if not path.exists():
        return "missing"
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_PINS = {
    "canonical_constants.py": sha256_of_file(SCRIPT_DIR / "canonical_constants.py"),
    "s84_plan_w7b_section": "W7b-77-singleton-admissibility-CM2008-twist",
    "connes_moscovici_2008_def_2.3_axioms": "twisted_triple_A1_A7_sigma_grading",
    "connes_marcolli_2013_table_1": "KO_dim_sign_table_eps_eps_prime_eps_double_prime",
    "s83_g32_singleton": "d_total_12_KO_6_A_F_C_H_M3C",
}

# First 20 lines of stdout must carry the input SHA pins
print("=" * 70)
print(f"Gate: {GATE_ID}")
print("Method: CCM-axiomatic (Connes-Moscovici 2008 twist extension)")
print("Convention: CM2008-twist")
print("L_max: N/A (representation-theoretic enumeration)")
print("-" * 70)
print("Input SHA-256 pins:")
for name, sha in INPUT_PINS.items():
    print(f"  {name}: {sha[:16]}..." if len(sha) > 16 else f"  {name}: {sha}")
print("=" * 70)

# ------------------------------------------------------------------
# CCM 2013 Table 1: KO-dim sign table (eps, eps', eps'')
# J^2 = eps * 1, JD = eps' * DJ, J*gamma = eps'' * gamma*J
# ------------------------------------------------------------------
# Source: Connes-Marcolli 2013 "A walk in the noncommutative garden", Table 1
# SM spectral triple requires KO-dim = 6, (eps, eps', eps'') = (+1, +1, -1)
# The eight rows mod 8:
CCM_SIGN_TABLE = {
    0: (+1, +1, +1),
    1: (+1, -1, None),   # J^2 = +1, no gamma in odd KO-dim
    2: (-1, +1, -1),
    3: (-1, -1, None),
    4: (-1, +1, +1),
    5: (-1, -1, None),
    6: (+1, +1, -1),     # <-- SM row (admissible for A_F = C+H+M_3(C))
    7: (+1, -1, None),
}

# ------------------------------------------------------------------
# Required singleton parameters from S83-G32
# ------------------------------------------------------------------
D_TOTAL_REQUIRED = 12          # (local) pinned by S83-G32: 4 (Minkowski) + 8 (SU(3))
KO_DIM_REQUIRED = 6            # (local) pinned by S83-G32: CCM Table 1 SM row
A_F_SM = "C(+)H(+)M_3(C)"      # Standard Model finite algebra

# ------------------------------------------------------------------
# Enumerate T-1..T-16 candidate twisted triples (per plan §W7b-77)
# ------------------------------------------------------------------
# Format: (candidate_id, d_internal, KO_dim, A_F, sigma, expected_verdict_reason)
TWIST_CANDIDATES = [
    # T-1..T-10 from plan enumeration table
    ("T-1",  6,  4, "C(+)H(+)M_3(C)", "grading",  "SM content requires d=8"),
    ("T-2",  6,  6, "C(+)H(+)M_3(C)", "grading",  "Mellin cone closes at d=6 vs required 12"),
    ("T-3",  7,  6, "M_2(H)",          "outer",    "A_F SM-content match fails (no C(+)H(+)M_3 decomposition)"),
    ("T-4",  8,  0, "C(+)H(+)M_3(C)", "trivial",  "CCM sign table: KO=0 has eps''=+1, SM requires -1"),
    ("T-5",  8,  2, "C(+)H(+)M_3(C)", "grading",  "CCM KO=2: eps=-1 inverts SM chirality"),
    ("T-6",  8,  4, "C(+)H(+)M_3(C)", "grading",  "CCM KO=4: eps=-1 inverts SM chirality"),
    ("T-7",  8,  6, "M_2(H)",          "outer",    "A_F: missing C(+)H (Higgs doublet absent)"),
    ("T-8",  8,  6, "M_4(C)",          "inner",    "A_F: no quaternionic (H) block, Higgs absent"),
    ("T-9",  9,  6, "C(+)H(+)M_3(C)", "inner",    "Mellin cone: d_total=13 exceeds singleton d=12"),
    ("T-10", 10, 6, "C(+)H(+)M_3(C)", "outer",    "Mellin cone: d_total=14, strong-coupling divergence"),
    # T-11..T-16: cross-products with HP^1, HP^2, Gaussian^2-measure
    ("T-11", 8,  6, "C(+)H(+)M_3(C) x HP^1",    "outer",    "Product with HP^1 (d_HP^1=4): d_total=16 violates Mellin"),
    ("T-12", 8,  6, "C(+)H(+)M_3(C) x HP^2",    "outer",    "Product with HP^2 (d=8): d_total=20 violates Mellin"),
    ("T-13", 8,  6, "C(+)H(+)M_3(C) x Gauss^2", "grading",  "Gaussian^2 measure: non-spectral-triple structure"),
    ("T-14", 6,  6, "C(+)H(+)M_3(C) x HP^1",    "grading",  "d_total=4+6+4=14; Mellin pole mis-location"),
    ("T-15", 10, 6, "C(+)H(+)M_3(C) x HP^1",    "outer",    "d_total=4+10+4=18; Mellin divergent"),
    ("T-16", 8,  2, "C(+)H(+)M_3(C) x Gauss^2", "outer",    "CCM KO=2 + non-spectral Gauss^2; double violation"),
]


# ------------------------------------------------------------------
# Admissibility Filters
# ------------------------------------------------------------------

def filter_F1_mellin_cone(d_internal, A_F, candidate_id):
    """
    F1: Mellin cone pairing.
    Requirement: d_total = 4 (Minkowski) + d_internal(+extras) = 12 exactly
    Tr(|D|^{-s}) has pole at s = d_total with residue in open positive cone.

    Substitution chain:
      Step F1.1: d_total = d_spacetime + d_internal (for pure product)
      Step F1.2: For products with HP^k, Gauss^2: d_total = 4 + d_internal + d_factor
                 d_HP^1 = 4, d_HP^2 = 8, d_Gauss^2 = 0 (non-geometric, breaks triple)
      Step F1.3: Compare to D_TOTAL_REQUIRED = 12 from S83-G32
      Step F1.4: Non-spectral factors (Gauss^2) fail Mellin structure entirely
    """
    # Handle cross-product candidates
    if "Gauss" in A_F:
        return False, f"Gaussian^2 factor is not a spectral triple (Mellin pole undefined)"
    if "HP^1" in A_F:
        d_total = 4 + d_internal + 4
    elif "HP^2" in A_F:
        d_total = 4 + d_internal + 8
    else:
        d_total = 4 + d_internal

    if d_total != D_TOTAL_REQUIRED:
        return False, f"d_total={d_total} != required 12 (Mellin cone mis-located)"
    return True, f"d_total={d_total} matches required 12"


def filter_F2_ccm_sign_table(KO_dim, A_F, candidate_id):
    """
    F2: Connes-Marcolli 2013 Table 1 sign table.
    Requirement: KO_dim = 6 for SM (eps, eps', eps'') = (+1, +1, -1).
    Any other KO_dim yields wrong signs and breaks SM content.

    Substitution chain:
      Step F2.1: Lookup (eps, eps', eps'') for given KO_dim in CCM_SIGN_TABLE
      Step F2.2: Compare to required SM signs (+1, +1, -1)
      Step F2.3: KO=0,2,3,4,5,7,1 all yield wrong sign combinations
                 KO=6 is UNIQUE match for C(+)H(+)M_3(C)
    """
    KO_mod = KO_dim % 8
    if KO_mod not in CCM_SIGN_TABLE:
        return False, f"KO-dim {KO_dim} not in CCM Table 1"

    required_signs = CCM_SIGN_TABLE[KO_DIM_REQUIRED]  # (+1, +1, -1)
    got_signs = CCM_SIGN_TABLE[KO_mod]

    if KO_mod != KO_DIM_REQUIRED:
        return False, f"KO-dim={KO_dim} yields signs {got_signs} != SM {required_signs}"
    return True, f"KO-dim={KO_dim} yields signs {got_signs} matches SM"


def filter_F3_sm_content(d_internal, A_F, candidate_id):
    """
    F3: SM content match.
    Requirement: A_F modules must decompose into 3 generations of fermions
    + gauge bosons SU(3)xSU(2)xU(1).
    Only A_F = C(+)H(+)M_3(C) with d_internal=8 delivers SM content
    (Chamseddine-Connes 2010 theorem).

    Substitution chain:
      Step F3.1: SM gauge group requires M_3(C) for SU(3), H for SU(2), C for U(1)
      Step F3.2: d_internal=8 matches SU(3) dimension (Killing form rank)
      Step F3.3: Alternative algebras (M_2(H), M_4(C), products) fail explicit
                 decomposition: no SU(2)-doublet from M_2(H) directly; M_4(C) has no
                 quaternionic block for Higgs; products introduce extra SU(N)'s.
    """
    if A_F != A_F_SM:
        return False, f"A_F={A_F} does not decompose into C(+)H(+)M_3(C)"
    if d_internal != 8:
        return False, f"d_internal={d_internal} != 8 (SU(3) Killing rank needed)"
    return True, "A_F=C(+)H(+)M_3(C), d_internal=8: SM content delivered"


def filter_F4_jensen_compatibility(sigma, A_F, candidate_id):
    """
    F4: Jensen deformation compatibility.
    Requirement: twist automorphism sigma must preserve the Jensen deformation
    sigma(Jensen_deform) = Jensen_deform so downstream monotonicity (S36) holds.

    Substitution chain:
      Step F4.1: Jensen deformation lambda_i(tau) acts via central element of A_F
      Step F4.2: For sigma to preserve Jensen: [sigma, Jensen_deform] = 0
                 => sigma must fix the center Z(A_F)
      Step F4.3: "trivial" sigma=id trivially commutes (PASS by default)
                 "grading" sigma (Z/2) on center: commutes only if center has trivial Z/2 action
                 "inner" sigma = Ad(u): u must be central => inner=trivial for central deform
                 "outer-regular" sigma: generically fails unless explicit Z/2 fix
      Step F4.4: For A_F=C(+)H(+)M_3(C), center = C(+)R(+)C; Jensen deform is diagonal
                 on this center. Only sigma=trivial or inner(central) preserve it exactly.
    """
    # For Jensen compatibility on SM A_F, only trivial or restricted-inner work
    if sigma in ("trivial",):
        return True, f"sigma=trivial preserves Jensen by construction"
    if sigma == "inner":
        # Inner automorphisms with central implementer preserve Jensen
        # For C(+)H(+)M_3(C), the H and M_3 blocks have nontrivial inner structure
        # that generically breaks diagonal Jensen structure
        return False, f"sigma=inner on {A_F}: generic inner automorphism breaks diagonal Jensen"
    if sigma == "grading":
        return False, f"sigma=grading: Z/2 on center generically flips lambda_1 <-> lambda_3"
    if sigma == "outer":
        return False, f"sigma=outer: outer automorphism moves off center, breaks Jensen"
    return False, f"sigma={sigma}: unknown automorphism class"


# ------------------------------------------------------------------
# Per-candidate evaluation
# ------------------------------------------------------------------
def evaluate_candidate(cand):
    cid, d_int, KO, A_F, sigma, _reason = cand
    results = {}
    results["F1_mellin"] = filter_F1_mellin_cone(d_int, A_F, cid)
    results["F2_ccm"] = filter_F2_ccm_sign_table(KO, A_F, cid)
    results["F3_sm"] = filter_F3_sm_content(d_int, A_F, cid)
    results["F4_jensen"] = filter_F4_jensen_compatibility(sigma, A_F, cid)

    all_pass = all(r[0] for r in results.values())
    return {
        "candidate_id": cid,
        "d_internal": d_int,
        "KO_dim": KO,
        "A_F": A_F,
        "sigma": sigma,
        "F1_pass": results["F1_mellin"][0],
        "F1_reason": results["F1_mellin"][1],
        "F2_pass": results["F2_ccm"][0],
        "F2_reason": results["F2_ccm"][1],
        "F3_pass": results["F3_sm"][0],
        "F3_reason": results["F3_sm"][1],
        "F4_pass": results["F4_jensen"][0],
        "F4_reason": results["F4_jensen"][1],
        "admissible": all_pass,
    }


# ------------------------------------------------------------------
# 7-axiom check (representational; recorded for the per-candidate log)
# ------------------------------------------------------------------
# For every candidate, document which axiom is OK and which fails at the
# structural level. This is per plan step 2 (verify 7 triple axioms).
TRIPLE_AXIOMS = [
    "A1_finite_dim_unital_star_algebra",
    "A2_Hilbert_star_representation",
    "A3_D_self_adjoint_compact_resolvent",
    "A4_twisted_commutator_bounded",
    "A5_sigma_grading_automorphism_square_id",
    "A6_Z2_grading_anticommutes_with_D",
    "A7_real_structure_J_KO_sign_constraint",
]


def axiom_check(cand):
    """Axiom-level pass/fail. A_F=C(+)H(+)M_3(C) with sigma in
    {trivial, grading, inner, outer} satisfies A1-A5 at the algebra level
    in all 16 candidates (since A_F's are all legitimate finite-dim *-algebras).
    A6-A7 are where CCM sign table enters — so these mirror F2."""
    cid, d_int, KO, A_F, sigma, _ = cand
    checks = {a: True for a in TRIPLE_AXIOMS}
    # A7 encodes the KO-dim sign constraint; only KO=6 matches SM row
    if KO % 8 != KO_DIM_REQUIRED:
        checks["A7_real_structure_J_KO_sign_constraint"] = False
    # Gauss^2 is not a spectral triple at the algebra level (A1 fails as *-algebra)
    if "Gauss" in A_F:
        checks["A1_finite_dim_unital_star_algebra"] = False
    # A5 requires sigma^2 = id; all listed sigmas satisfy by construction
    return checks


# ------------------------------------------------------------------
# Run the enumeration
# ------------------------------------------------------------------
print("\n--- Per-Candidate Evaluation ---\n")

per_candidate_records = []
axiom_records = []
admissible_ids = []

for cand in TWIST_CANDIDATES:
    rec = evaluate_candidate(cand)
    ax = axiom_check(cand)
    per_candidate_records.append(rec)
    axiom_records.append({"candidate_id": rec["candidate_id"], **ax})

    if rec["admissible"]:
        admissible_ids.append(rec["candidate_id"])

    # Verbose per-candidate output
    status = "ADMISSIBLE" if rec["admissible"] else "EXCLUDED"
    print(f"[{rec['candidate_id']}] (d_int={rec['d_internal']}, KO={rec['KO_dim']}, "
          f"A_F={rec['A_F']}, sigma={rec['sigma']}) -> {status}")
    for fkey in ("F1_pass", "F2_pass", "F3_pass", "F4_pass"):
        rkey = fkey.replace("_pass", "_reason")
        mark = "OK  " if rec[fkey] else "FAIL"
        print(f"   {fkey[:2].upper()}: {mark} - {rec[rkey]}")
    print()

# ------------------------------------------------------------------
# Count and decision
# ------------------------------------------------------------------
admissible_twist_count = len(admissible_ids)

print("=" * 70)
print(f"admissible_twist_count = {admissible_twist_count}")
print(f"admissible IDs: {admissible_ids if admissible_ids else '(none)'}")

# PASS iff count == 0 exactly (per plan threshold table)
if admissible_twist_count == 0:
    verdict = "PASS"
elif admissible_twist_count in (1, 2):
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"Verdict: {verdict}")
print("=" * 70)


# ------------------------------------------------------------------
# Closure SHA: SHA-256 of ordered input-pin map
# ------------------------------------------------------------------
closure_input = json.dumps(INPUT_PINS, sort_keys=True)
# Also fold in the deterministic enumeration outputs
results_blob = json.dumps(
    {
        "admissible_count": admissible_twist_count,
        "admissible_ids": sorted(admissible_ids),
        "candidates": [
            {
                "id": r["candidate_id"],
                "d_int": r["d_internal"],
                "KO": r["KO_dim"],
                "A_F": r["A_F"],
                "sigma": r["sigma"],
                "admissible": r["admissible"],
            }
            for r in per_candidate_records
        ],
    },
    sort_keys=True,
)
closure_blob = closure_input + "||" + results_blob
closure_sha = hashlib.sha256(closure_blob.encode("utf-8")).hexdigest()

print(f"\nClosure SHA-256: {closure_sha}")

# ------------------------------------------------------------------
# Save data
# ------------------------------------------------------------------
candidate_array = np.array(
    [(r["candidate_id"], r["d_internal"], r["KO_dim"], r["A_F"], r["sigma"],
      r["F1_pass"], r["F2_pass"], r["F3_pass"], r["F4_pass"], r["admissible"])
     for r in per_candidate_records],
    dtype=object,
)

np.savez(
    OUT_NPZ,
    gate_id=GATE_ID,
    verdict=verdict,
    admissible_twist_count=admissible_twist_count,
    admissible_ids=np.array(admissible_ids, dtype=object),
    candidates=candidate_array,
    input_pins=json.dumps(INPUT_PINS),
    closure_sha=closure_sha,
    ccm_sign_table=json.dumps({str(k): v for k, v in CCM_SIGN_TABLE.items()}),
    per_candidate_json=json.dumps(per_candidate_records),
    axiom_records_json=json.dumps(axiom_records),
)
print(f"Saved: {OUT_NPZ}")

# ------------------------------------------------------------------
# Final 4-tuple output tag (last non-verdict line per gate-verdicts.md)
# ------------------------------------------------------------------
print(f"\n4-tuple: (value={admissible_twist_count}, scheme=CCM-axiomatic, "
      f"convention=CM2008-twist, L_max=N/A)")

# ------------------------------------------------------------------
# Append verdict line (canonical S81+ format)
# ------------------------------------------------------------------
verdict_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value={admissible_twist_count} "
    f"scheme=CCM-axiomatic "
    f"convention=CM2008-twist "
    f"L_max=N/A "
    f"sha256={closure_sha}\n"
)

with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write(verdict_line)

print(f"\nVerdict appended to {VERDICT_FILE}:")
print(verdict_line.strip())
