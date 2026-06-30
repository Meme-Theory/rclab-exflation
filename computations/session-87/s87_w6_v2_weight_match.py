"""
S87 W6 §W6-2 — S87-V2-WEIGHT-MATCH-FORWARD-GATE
=================================================

GATE_ID: S87-V2-WEIGHT-MATCH-FORWARD-GATE
TRIGGER: VERIFY
CLASSIFICATION: GEOMETRIC (substrate-physics forward gate on Josephson-array
combinatorial decomposition vs A_F = C ⊕ H ⊕ M_3(C) Connes-Marcolli real-dim)

HYPOTHESIS (per session-87-plan-w6.md §W6-2 lines 184-185)
----------------------------------------------------------
The Josephson-array's edge-count × per-edge-multiplicity decomposition,
computed on the framework's Jensen-deformed SU(3) spectrum at tau_fold,
reproduces the A_F = C ⊕ H ⊕ M_3(C) real-dimension ratio (1:4:18) at
machine epsilon. This is the V2-weight match validating the S86 W-6
workshop's Pair-2 / Pair-3 SUB-CLUSTER NEAR-IDENTITY (cross-cluster gap
remains explicit per W-6 Verdict row 7).

PRE-REGISTERED DECOMPOSITION FORMULA (plan §W6-2 lines 187-195)
---------------------------------------------------------------
    V2_weight(branch) = edge_count[branch] × per_edge_multiplicity[branch]
    target_ratio       = (V2_weight[C] : V2_weight[H] : V2_weight[M_3(C)])
                       = (1 : 4 : 18)
                       = (real_dim(C) : real_dim(H) : real_dim(M_3(C)))

Convention (Connes-Marcolli 2008 Thm 11.1; matches s84_w8a uniqueness theorem):
  dim_R(A_F) = 1 + 4 + 18 = 23. The C-summand contributes real_dim 1
  (J-real-structure projects the complex line to one real DoF in the
  spectral-triple cohomology); H = 4 (quaternions); M_3(C) = 18 (3×3 complex
  matrices, full real-dim 2×9).

OPERATIONAL DEFINITION — SPECTRUM-DERIVED (NON-TAUTOLOGICAL)
------------------------------------------------------------
The substrate's Josephson-array IS the connectivity graph of the Jensen-
deformed SU(3) spectrum at tau_fold. SU(3) sectors (p,q) partition into A_F
branches by the canonical Connes-Chamseddine A_F ↪ Cl(SU(3)) embedding:

    S_C = {(0,0)}                         — trivial / singlet
    S_H = {(1,0), (0,1)}                   — rank-1 fundamental + conjugate
    S_M = all (p,q) with min(p,q) ≥ 1
            OR (max(p,q) ≥ 2 AND min(p,q) = 0)
                                          — rank-≥2 (M_3(C) summand)

Spectrum-derived (substrate-IS) quantities per branch:

    edge_count[b]              = #{(p,q) ∈ S_b}             (sector count)
    per_edge_multiplicity[b]   = mean dim(p,q) over (p,q) ∈ S_b
                               = dim_sum[b] / edge_count[b]

    V2_weight[b]               = edge_count[b] × per_edge_multiplicity[b]
                               = sum_{(p,q) ∈ S_b} dim(p,q)
                               = dim_sum[b]

The TEST is whether the substrate's spectrum at L_max=12 produces
dim_sum[b] in the canonical (1 : 4 : 18) ratio. The construction is
NON-TAUTOLOGICAL: per_edge_multiplicity is read off the spectrum
(mean irrep dim per branch sector), not back-calculated from the target.

THRESHOLD (plan §W6-2 lines 200-203)
-------------------------------------
PASS: max |V2_weight_computed[b] / sum_b V2_weight_computed[b]
            − V2_weight_target[b] / sum_b V2_weight_target[b]| < 1e-10
INFO: 1e-10 ≤ max ratio-deviation < 1e-6
FAIL: max ratio-deviation > 1e-6

(All weights normalized to dimensionless ratio against total-weight sum, since
the absolute V2_weight scale is convention-dependent; only the ratio is
substrate-IS canonical.)

Tolerance rule: RATIO.

EXPECTED OUTPUT 4-TUPLE (plan §W6-2 lines 237-239)
--------------------------------------------------
(value=max_branch_relative_deviation,
 scheme=zeta-regulated-Seeley-DeWitt,
 convention=cyclic-fold-V_4,
 L_max=12)

INPUTS
------
- computations/session-84/s84_spectrum_cache_L12_tau019.npz (Jensen-deformed
  SU(3) spectrum at canonical tau_fold; 90 sectors at p+q ≤ 12,
  166,896 abs_eval entries, structural invariant n_evals = 16 × dim
  per sector)
- computations/_shared/canonical_constants.py (tau_fold, M_KK)
- .claude/rules/regulator-pin-discipline.md (a_n^{ζ} regulator-tag
  enforcement; this gate's machinery scheme is zeta-regulated
  Seeley-DeWitt)

OUTPUTS
-------
- computations/session-87/s87_w6_v2_weight_match.npz
- computations/session-87/s87_w6_v2_weight_match.png
- verdict line appended to computations/session-87/s87_gate_verdicts.txt
  with W9a-99 dual-SHA companion row + S87 schema-v2 3-tuple annotation

PROVENANCE
----------
Plan: sessions/session-plan/session-87-plan-w6.md §W6-2 lines 173-282
Owner: lizzi-spectral-functional-theorist (W6-2 PRIMARY)
Co-signer: volovik-superfluid-universe-theorist (Josephson-array authority)
Substitution chain: this docstring §"OPERATIONAL DEFINITION" + plan §W6-2 lines 207-214
"""
import hashlib
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Cap CPU thread contention for parallel-agent friendliness
os.environ.setdefault("OMP_NUM_THREADS", "8")

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "computations"))

from canonical_constants import tau_fold, M_KK  # noqa: E402

# =============================================================================
# 1. CONSTANTS & PRE-REGISTERED PINS
# =============================================================================
GATE_ID = "S87-V2-WEIGHT-MATCH-FORWARD-GATE"
SCHEME = "zeta-regulated-Seeley-DeWitt"
CONVENTION = "cyclic-fold-V_4"
L_MAX = 12                                          # (local) — matches s84_spectrum_cache_L12_tau019.npz

# Connes-Marcolli 2008 Thm 11.1 — A_F = C ⊕ H ⊕ M_3(C) real-dim breakdown
TARGET_REAL_DIM = {"C": 1, "H": 4, "M_3(C)": 18}    # (local) — pre-registered Connes-Marcolli target

# PASS / INFO / FAIL bands per plan §W6-2 lines 200-203
PASS_THRESHOLD = 1e-10                              # (local) — pre-registered
INFO_BAND_HIGH = 1e-6                               # (local) — pre-registered

# Branch partition rule (Connes-Chamseddine A_F ↪ Cl(SU(3)) algebra-summand action):
#   S_C = {(0,0)}; S_H = {(1,0),(0,1)}; S_M = remaining
def assign_branch(pq):  # noqa: N802
    p, q = pq
    if (p, q) == (0, 0):
        return "C"
    if (p, q) in [(1, 0), (0, 1)]:
        return "H"
    return "M_3(C)"

# =============================================================================
# 2. INPUT-PIN MAP & SHA HARNESS
# =============================================================================
SPEC_CACHE = REPO / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANON_PATH = REPO / "computations" / "_shared" / "canonical_constants.py"
REG_RULE_PATH = REPO / ".claude" / "rules" / "regulator-pin-discipline.md"
PLAN_PATH = REPO / "sessions" / "session-plan" / "session-87-plan-w6.md"


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map):
    """SHA-256 over canonicalized JSON of the input-pin map (S82 W1 helper pattern)."""
    blob = json.dumps(input_pin_map, sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


# =============================================================================
# 3. LOAD SUBSTRATE SPECTRUM
# =============================================================================
print("=" * 78)
print(f"GATE: {GATE_ID}")
print(f"  scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX}")
print(f"  tau_fold={tau_fold}, M_KK={M_KK:.6e}")
print("=" * 78)

sha_spec = file_sha256(SPEC_CACHE)
sha_canon = file_sha256(CANON_PATH)
sha_rule = file_sha256(REG_RULE_PATH)
sha_plan = file_sha256(PLAN_PATH)
print("\n[INPUT-PIN MAP]")
print(f"  s84_spectrum_cache_L12_tau019.npz  = {sha_spec}")
print(f"  canonical_constants.py             = {sha_canon}")
print(f"  regulator-pin-discipline.md        = {sha_rule}")
print(f"  session-87-plan-w6.md              = {sha_plan}")

data = np.load(SPEC_CACHE, allow_pickle=True)
SE = data["sector_evals"].item()
print(f"\n[SPECTRUM CACHE LOADED]")
print(f"  total sectors (p+q <= {L_MAX}): {len(SE)}")
total_abs_eval_entries = sum(len(SE[k]["abs_evals"]) for k in SE)
print(f"  total abs_eval entries          : {total_abs_eval_entries}")

# =============================================================================
# 4. STRUCTURAL CHECK — CYCLIC-FOLD V_4 × DIRAC-SPINOR INVARIANT
# =============================================================================
ratios = []                                                # (local)
for pq in SE:
    d = SE[pq]["dim"]; n_e = len(SE[pq]["abs_evals"])
    ratios.append(n_e / d)
unique_ratios = sorted(set(ratios))                        # (local)
assert len(unique_ratios) == 1 and abs(unique_ratios[0] - 16.0) < 1e-12, (
    f"Cyclic-fold V_4 × Dirac-spinor invariant violated: ratios={unique_ratios}"
)
CYCLIC_FOLD_DIRAC = 16                                    # (local) — V_4 (4) × Dirac-spinor (4)
print(f"\n[CYCLIC-FOLD V_4 × DIRAC-SPINOR STRUCTURAL CHECK]")
print(f"  unique n_evals/dim ratios        : {unique_ratios}")
print(f"  cyclic-fold × Dirac-spinor factor: {CYCLIC_FOLD_DIRAC}")

# =============================================================================
# 5. BRANCH PARTITION & SPECTRUM-DERIVED V2_WEIGHT
# =============================================================================
# Spectrum-derived quantities per branch (NON-TAUTOLOGICAL):
#   edge_count[b]            = #{(p,q) in S_b}
#   per_edge_multiplicity[b] = mean dim(p,q) over (p,q) in S_b
#   V2_weight[b]             = edge_count × per_edge_mult = sum dim(p,q) over S_b
branch_data = {b: {"sectors": [], "dims": [], "n_evals": 0}
               for b in TARGET_REAL_DIM}                  # (local)
for pq, payload in SE.items():
    b = assign_branch(pq)
    d = int(payload["dim"])                                # (local)
    n_e = len(payload["abs_evals"])                        # (local)
    branch_data[b]["sectors"].append(pq)
    branch_data[b]["dims"].append(d)
    branch_data[b]["n_evals"] += n_e

print(f"\n[SPECTRUM-DERIVED BRANCH DECOMPOSITION (substrate-IS canonical)]")
results = {}
for b, target in TARGET_REAL_DIM.items():
    bd = branch_data[b]
    edge_count = len(bd["sectors"])                       # (local) — sector count
    if edge_count == 0:
        per_edge_mult = 0.0                               # (local) — empty-branch fallback
    else:
        per_edge_mult = float(np.mean(bd["dims"]))        # (local) — mean irrep dim per sector
    v2_computed = edge_count * per_edge_mult              # (local) = dim_sum[b]
    results[b] = {
        "edge_count": edge_count,
        "per_edge_multiplicity": per_edge_mult,
        "V2_weight_computed": v2_computed,
        "V2_weight_target": target,
        "n_sectors": edge_count,
        "n_evals": bd["n_evals"],
        "dim_sum": int(sum(bd["dims"])),
    }
    print(f"  branch {b:8s} | edge_count = {edge_count:4d} | per_edge_mult = "
          f"{per_edge_mult:10.4f} | V2_weight = {v2_computed:12.4f} | "
          f"target = {target:3d}")

# =============================================================================
# 6. NORMALIZED-RATIO TEST AGAINST (1:4:18)
# =============================================================================
sum_computed = sum(r["V2_weight_computed"] for r in results.values())   # (local)
sum_target = sum(r["V2_weight_target"] for r in results.values())       # (local)
print(f"\n[NORMALIZED RATIO TEST]")
print(f"  sum V2_weight_computed = {sum_computed}")
print(f"  sum V2_weight_target   = {sum_target}  (=1+4+18 = 23, Connes-Marcolli)")

deviations = {}
for b in results:
    frac_computed = results[b]["V2_weight_computed"] / sum_computed   # (local)
    frac_target = results[b]["V2_weight_target"] / sum_target         # (local)
    dev = abs(frac_computed - frac_target)                             # (local)
    deviations[b] = dev
    results[b]["deviation"] = dev
    results[b]["frac_computed"] = frac_computed
    results[b]["frac_target"] = frac_target
    print(f"  branch {b:8s} | frac_computed = {frac_computed:.10e} | "
          f"frac_target = {frac_target:.10e} | abs_deviation = {dev:.6e}")

max_dev = max(deviations.values())                        # (local)
print(f"\n  max absolute fraction-deviation : {max_dev:.6e}")

# =============================================================================
# 7. INDEPENDENT CROSS-CHECK — Hilbert-weight per branch
# =============================================================================
# n_evals_predicted[b] = 16 × edge_count[b] × per_edge_mult[b] = 16 × V2_weight[b]
# This is a STRUCTURAL CHECK (independent of A_F target) on the cache invariant.
print(f"\n[CROSS-CHECK: substrate Hilbert-weight per branch]")
crosscheck_pass = True                                    # (local)
for b in TARGET_REAL_DIM:
    bd = branch_data[b]
    dim_sum_b = sum(bd["dims"])                           # (local)
    n_e_predicted = CYCLIC_FOLD_DIRAC * dim_sum_b         # (local)
    n_e_actual = bd["n_evals"]                            # (local)
    match = (n_e_predicted == n_e_actual)
    crosscheck_pass &= match
    print(f"  branch {b:8s} | dim_sum = {dim_sum_b:5d} | n_evals_predicted = "
          f"{n_e_predicted:6d} | n_evals_actual = {n_e_actual:6d} | match = {match}")
assert crosscheck_pass, "Substrate Hilbert-weight cross-check failed"
print("  cross-check                    : PASS (n_evals = 16 × dim_sum per branch)")

# =============================================================================
# 8. VERDICT COMPOSITION (per plan §W6-2 lines 200-203)
# =============================================================================
if max_dev < PASS_THRESHOLD:
    verdict = "PASS"
elif max_dev < INFO_BAND_HIGH:
    verdict = "INFO"
else:
    verdict = "FAIL"
value_str = f"{max_dev:.6e}"                              # (local)
print(f"\n[VERDICT]")
print(f"  {GATE_ID}: {verdict} -- value={value_str}")
print(f"  PASS threshold = {PASS_THRESHOLD}, INFO band = [{PASS_THRESHOLD}, {INFO_BAND_HIGH})")

# =============================================================================
# 9. PERSIST RESULTS — NPZ + PNG
# =============================================================================
OUT_NPZ = REPO / "computations" / "session-87" / "s87_w6_v2_weight_match.npz"
OUT_PNG = REPO / "computations" / "session-87" / "s87_w6_v2_weight_match.png"

branches_ordered = ["C", "H", "M_3(C)"]
edge_count_arr = np.array([results[b]["edge_count"] for b in branches_ordered])
per_edge_mult_arr = np.array([results[b]["per_edge_multiplicity"] for b in branches_ordered])
v2_weight_arr = np.array([results[b]["V2_weight_computed"] for b in branches_ordered])
target_ratio_arr = np.array([results[b]["V2_weight_target"] for b in branches_ordered])
deviation_arr = np.array([results[b]["deviation"] for b in branches_ordered])
frac_computed_arr = np.array([results[b]["frac_computed"] for b in branches_ordered])
frac_target_arr = np.array([results[b]["frac_target"] for b in branches_ordered])
n_sectors_arr = np.array([results[b]["n_sectors"] for b in branches_ordered])
n_evals_arr = np.array([results[b]["n_evals"] for b in branches_ordered])

np.savez(
    OUT_NPZ,
    gate_id=GATE_ID,
    scheme=SCHEME,
    convention=CONVENTION,
    L_max=L_MAX,
    tau_fold=tau_fold,
    M_KK=M_KK,
    branches=np.array(branches_ordered, dtype=object),
    edge_count=edge_count_arr,
    per_edge_multiplicity=per_edge_mult_arr,
    V2_weight=v2_weight_arr,
    target_ratio=target_ratio_arr,
    frac_computed=frac_computed_arr,
    frac_target=frac_target_arr,
    deviation=deviation_arr,
    n_sectors=n_sectors_arr,
    n_evals=n_evals_arr,
    cyclic_fold_dirac_factor=CYCLIC_FOLD_DIRAC,
    sum_V2_computed=sum_computed,
    sum_V2_target=sum_target,
    max_deviation=max_dev,
    verdict=verdict,
    pass_threshold=PASS_THRESHOLD,
    info_band_high=INFO_BAND_HIGH,
    sha_spec_cache=sha_spec,
    sha_canonical=sha_canon,
    sha_rule=sha_rule,
    sha_plan=sha_plan,
)
print(f"\n  data saved                     : {OUT_NPZ}")

# Plot: fractional V2_weight (computed vs target) per branch
fig, ax = plt.subplots(figsize=(9, 5.5))
x = np.arange(3)                                          # (local)
width = 0.36                                              # (local)
ax.bar(x - width/2, frac_computed_arr, width,
       label="V2_weight / Σ V2_weight (computed, spectrum-derived)",
       color="tab:blue", edgecolor="black")
ax.bar(x + width/2, frac_target_arr, width,
       label="real_dim / 23 (Connes-Marcolli target)",
       color="tab:orange", edgecolor="black")
ax.set_xticks(x)
ax.set_xticklabels(branches_ordered, fontsize=11)
ax.set_ylabel("Fractional V2-weight")
ax.set_title(f"{GATE_ID}\nL_max={L_MAX}, tau_fold={tau_fold}\n"
             f"scheme={SCHEME}, convention={CONVENTION}")
for i, b in enumerate(branches_ordered):
    ax.text(i - width/2, frac_computed_arr[i] + 0.01,
            f"{frac_computed_arr[i]:.4f}", ha="center", fontsize=8)
    ax.text(i + width/2, frac_target_arr[i] + 0.01,
            f"{frac_target_arr[i]:.4f}", ha="center", fontsize=8)
ax.legend(loc="upper left", fontsize=9)
ax.text(0.98, 0.95,
        f"max abs fraction-deviation = {max_dev:.3e}\n"
        f"PASS threshold = {PASS_THRESHOLD:.0e}\n"
        f"verdict = {verdict}",
        transform=ax.transAxes, fontsize=10, ha="right",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85),
        verticalalignment="top")
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=140)
plt.close()
print(f"  plot saved                     : {OUT_PNG}")

# =============================================================================
# 10. APPEND VERDICT LINE — S87+ schema-v2 (dual-SHA + 3-tuple companion row)
# =============================================================================
verdict_path = REPO / "computations" / "session-87" / "s87_gate_verdicts.txt"

input_pin_map = {
    "_gate_id": GATE_ID,
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_L_max": L_MAX,
    "_wp_id": "S87-W6-2",
    "spec_cache_sha256": sha_spec,
    "canonical_constants_sha256": sha_canon,
    "regulator_rule_sha256": sha_rule,
    "plan_sha256": sha_plan,
    "tau_fold": tau_fold,
    "M_KK": M_KK,
    "target_real_dim": TARGET_REAL_DIM,
    "pass_threshold": PASS_THRESHOLD,
    "info_band_high": INFO_BAND_HIGH,
}
audit_sha = closure_hash(input_pin_map)

content_blob = {
    "verdict": verdict,
    "value": value_str,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max": L_MAX,
    "edge_count": edge_count_arr.tolist(),
    "per_edge_multiplicity": per_edge_mult_arr.tolist(),
    "V2_weight": v2_weight_arr.tolist(),
    "target_ratio": target_ratio_arr.tolist(),
    "frac_computed": frac_computed_arr.tolist(),
    "frac_target": frac_target_arr.tolist(),
    "deviation": deviation_arr.tolist(),
    "max_deviation": max_dev,
}
content_sha = closure_hash(content_blob)

canonical_line = (
    f"{GATE_ID}: {verdict} -- value='{value_str}' "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
    f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n"
)
companion_dual_sha = (
    f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
)
mag = "PASS" if max_dev < PASS_THRESHOLD else ("INFO" if max_dev < INFO_BAND_HIGH else "FAIL")
companion_3tuple = (
    f"# sign_verdict=N/A magnitude_verdict={mag} regime_verdict=VALID "
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
)

with open(verdict_path, "a", encoding="utf-8") as f:
    f.write(canonical_line)
    f.write(companion_dual_sha)
    f.write(companion_3tuple)

print(f"\n[VERDICT LINE APPENDED] -> {verdict_path}")
print(f"  audit_sha256   = {audit_sha}")
print(f"  content_sha256 = {content_sha}")
print(f"  composite verdict = {verdict}")

sys.exit(0)
