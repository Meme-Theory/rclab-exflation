"""S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY — W7-6.

[AUDIT] gate: validity audit of the Mukhanov-Sasaki pump operator
across the K-corridor from K_R5 = 1.9222 to K_crit + 0.5. Classifies
each K-grid point as VALID, MARGINAL, or BREAKDOWN per plan step 3
ratio bands.

Hypothesis (plan §W7-6 step 5):
  Mukhanov-Sasaki (v″_k + [k² − z″/z] v_k = 0, z = a·√(2ε)·M_Pl_eff)
  is VALID when |z″/z| ≫ k²_pivot (superhorizon adiabaticity). Across
  the K-corridor, M_Pl_eff(K) scales as K_R5/K (canonical dispersion),
  so the ratio z″/z / k²_pivot × (M_Pl_eff(K_R5)/M_Pl_eff(K))² scales
  as (K_R5/K)². The audit classifies each K.

Substitution chain (plan §W7-6 step 10):

  Step 1 (definitions):
    z = a·sqrt(2·ε_H)·M_Pl_eff                    [Mukhanov variable]
    z″/z ≈ a²·H²·(2 − ε_H)                         [leading S76 WS R1]
    Mukhanov-validity: |z″/z| ≫ k²_pivot           [superhorizon k ≪ aH]
    K = substrate phonon-dispersion control parameter
    K_R5 = 1.9222 (W1-G1 canonical lower endpoint)
    K_crit = 91.5 (S84 W5-55 inflationary sub-corridor upper endpoint)

  Step 2 (substitution — ratio vs K):
    ratio(K) = (z″/z) / k²_pivot
    In canonical M_Pl_eff(K) = M_Pl_red · (K_R5/K) scaling:
    ratio(K) = ratio_0 · (K_R5/K)²  where ratio_0 = ratio(K_R5) = 100
    (VALID anchor at W1-G1 canonical K_R5; superhorizon deep regime)

  Step 3 (simplification — classification bands, plan §7):
    ratio > 10           → VALID (Mukhanov-Sasaki survives)
    1 ≤ ratio ≤ 10       → MARGINAL (sub-leading ε_H flow matters)
    ratio < 1            → BREAKDOWN (substrate-native required)

  Step 4 (direction):
    At K_R5 = 1.9222:    ratio = 100 × 1 = 100 → VALID
    At K_substrate = 2.035: ratio = 100 × (1.9222/2.035)² = 89.3 → VALID
    At K = 6.077 (first MARGINAL boundary): ratio = 10
    At K = 19.22 (first BREAKDOWN boundary): ratio = 1
    At K_crit = 91.5:    ratio = 100 × (1.9222/91.5)² = 0.044 → BREAKDOWN
    Direction: PASS iff VALID in [K_R5, K_substrate] AND MARGINAL/BREAKDOWN
    at K_crit (expected phononic-to-inflationary transition).

PASS/FAIL/INFO (plan §W7-6 step 9):
  PASS: all K in [K_R5, K_substrate=2.035] VALID AND K_crit MARGINAL/BREAKDOWN
  FAIL: any K in [K_R5, K_substrate] BREAKDOWN
  INFO: K_crit VALID (no inversion at corridor endpoint — re-audit)

Machinery pin (plan §7):
  L_max=10, scheme=z-gauge-MS, convention=M_Pl_eff-canonical,
  K_grid=64 points log-spaced on [K_R5, K_crit+0.5], random_seed=42,
  GPU path=scalar arithmetic (not required at this gate).

Outputs:
  computations/session-85/s85_w7_k_corridor_mukhanov_validity.npz
  computations/session-85/s85_w7_k_corridor_mukhanov_validity.png
Verdict: computations/session-85/s85_gate_verdicts.txt with dual-SHA.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from canonical_constants import (  # noqa: E402
    K_R5,
    K_crit,
    M_Pl_reduced,
    M_KK_gravity,
    dS_fold,
    d2S_fold,
    tau_fold,
    PI,
)


# ----------------------------------------------------------------------------
# Section 0 — input-pin map and closure SHA
# ----------------------------------------------------------------------------
def _file_sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_PINS: dict[str, str] = {}

_static_files = [
    _HERE / "canonical_constants.py",
    _HERE / "s78_pre_fold_vacuum.npz",
    _HERE / "s85_w7_cc6_parker_residue.npz",
]
for _sf in _static_files:
    if _sf.exists():
        INPUT_PINS[_sf.name] = _file_sha(_sf)
    else:
        INPUT_PINS[_sf.name] = "MISSING"

# Machinery pins (plan §7)
L_max = 10  # (local)
scheme = "z-gauge-MS"  # (local) plan §8
convention = "M_Pl_eff-canonical"  # (local) plan §8
N_K = 64  # (local) plan §7 K-grid resolution
K_substrate = 2.035  # (local) plan §7 secondary anchor (not yet canonical)
K_upper = K_crit + 0.5  # (local) plan §7 UV bound (91.5 + 0.5 = 92.0)
ratio_0 = 100.0  # (local) plan step 4 VALID anchor at K_R5
ratio_valid_thresh = 10.0  # (local) plan §7 VALID > 10
ratio_breakdown_thresh = 1.0  # (local) plan §7 BREAKDOWN < 1
random_seed = 42  # (local)

INPUT_PINS["L_max"] = f"{L_max:d}"
INPUT_PINS["scheme"] = scheme
INPUT_PINS["convention"] = convention
INPUT_PINS["N_K"] = f"{N_K:d}"
INPUT_PINS["K_R5"] = f"{K_R5:.10e}"
INPUT_PINS["K_substrate"] = f"{K_substrate:.10e}"
INPUT_PINS["K_crit"] = f"{K_crit:.10e}"
INPUT_PINS["K_upper"] = f"{K_upper:.10e}"
INPUT_PINS["ratio_0_VALID_anchor"] = f"{ratio_0:.6f}"
INPUT_PINS["ratio_valid_thresh"] = f"{ratio_valid_thresh:.6f}"
INPUT_PINS["ratio_breakdown_thresh"] = f"{ratio_breakdown_thresh:.6f}"
INPUT_PINS["random_seed"] = f"{random_seed:d}"
INPUT_PINS["M_Pl_reduced_GeV"] = f"{M_Pl_reduced:.10e}"
INPUT_PINS["M_KK_gravity_GeV"] = f"{M_KK_gravity:.10e}"

CLOSURE_INPUT = json.dumps(INPUT_PINS, sort_keys=True, separators=(",", ":"))
CLOSURE_SHA = hashlib.sha256(CLOSURE_INPUT.encode("utf-8")).hexdigest()

print("=" * 78)
print("S85 W7-6: K-CORRIDOR-MUKHANOV-VALIDITY — ratio classification across K")
print("=" * 78)
print(f"closure SHA-256 (64 char): {CLOSURE_SHA}")
print(f"closure SHA-256 (16 head): {CLOSURE_SHA[:16]}")
print()
print("--- input pin SHAs and values ---")
for _k, _v in INPUT_PINS.items():
    print(f"  {_k:<32s}: {_v}")
print()


# ----------------------------------------------------------------------------
# Section 1 — K-grid + ratio computation
# ----------------------------------------------------------------------------
# K-grid log-spaced on [K_R5, K_crit + 0.5]
K_grid = np.logspace(np.log10(K_R5), np.log10(K_upper), N_K)  # (local)

# Canonical M_Pl_eff(K) scaling: M_Pl_eff(K) = M_Pl_red · (K_R5/K)
# Ratio(K) = (z″/z)/(k²) inherits (M_Pl_eff(K_R5)/M_Pl_eff(K))² factor:
# ratio(K) = ratio_0 · (K_R5/K)²
ratio = ratio_0 * (K_R5 / K_grid) ** 2  # (local)

# Classification
classification = np.where(
    ratio > ratio_valid_thresh,
    "VALID",
    np.where(ratio >= ratio_breakdown_thresh, "MARGINAL", "BREAKDOWN"),
)  # (local) string array

# Boundary K-values
K_boundary_valid_marginal = K_R5 * np.sqrt(ratio_0 / ratio_valid_thresh)  # (local)
K_boundary_marginal_breakdown = K_R5 * np.sqrt(ratio_0 / ratio_breakdown_thresh)  # (local)

print("--- K-grid and classification ---")
print(f"  K_R5                            = {K_R5:.4f}  (VALID anchor, ratio = {ratio_0:.1f})")
print(f"  K_substrate                     = {K_substrate:.4f}  (secondary anchor)")
print(f"  K_crit                          = {K_crit:.4f}  (upper corridor endpoint)")
print(f"  K_upper (= K_crit + 0.5)         = {K_upper:.4f}  (conservative UV)")
print(f"  N_K grid points                 = {N_K}")
print(f"  VALID→MARGINAL boundary         = {K_boundary_valid_marginal:.4f}")
print(f"  MARGINAL→BREAKDOWN boundary      = {K_boundary_marginal_breakdown:.4f}")
print()

# Per-anchor evaluation
ratio_at_K_R5 = ratio_0 * (K_R5 / K_R5) ** 2  # (local) = ratio_0 = 100
ratio_at_K_substrate = ratio_0 * (K_R5 / K_substrate) ** 2  # (local)
ratio_at_K_crit = ratio_0 * (K_R5 / K_crit) ** 2  # (local)

def _classify(r: float) -> str:
    if r > ratio_valid_thresh:
        return "VALID"
    elif r >= ratio_breakdown_thresh:
        return "MARGINAL"
    else:
        return "BREAKDOWN"

class_at_K_R5 = _classify(ratio_at_K_R5)
class_at_K_substrate = _classify(ratio_at_K_substrate)
class_at_K_crit = _classify(ratio_at_K_crit)

print("--- per-anchor classification ---")
print(f"  K = K_R5       = {K_R5:.4f}: ratio = {ratio_at_K_R5:.4e}  →  {class_at_K_R5}")
print(f"  K = K_substrate= {K_substrate:.4f}: ratio = {ratio_at_K_substrate:.4e}  →  {class_at_K_substrate}")
print(f"  K = K_crit     = {K_crit:.4f}: ratio = {ratio_at_K_crit:.4e}  →  {class_at_K_crit}")
print()


# ----------------------------------------------------------------------------
# Section 2 — PASS criteria (plan §9)
# ----------------------------------------------------------------------------
# [1] all K in [K_R5, K_substrate] VALID
mask_corridor = (K_grid >= K_R5) & (K_grid <= K_substrate)  # (local)
classes_in_corridor = classification[mask_corridor]  # (local)
all_corridor_valid = bool(np.all(classes_in_corridor == "VALID"))  # (local)

# [2] K_crit MARGINAL or BREAKDOWN
crit_marginal_or_breakdown = class_at_K_crit in ("MARGINAL", "BREAKDOWN")  # (local)

# [3] no BREAKDOWN inside [K_R5, K_substrate]
no_breakdown_in_corridor = bool(not np.any(classes_in_corridor == "BREAKDOWN"))

# Verdict per plan §9
if all_corridor_valid and crit_marginal_or_breakdown:
    verdict = "PASS"
elif not no_breakdown_in_corridor:
    verdict = "FAIL"
elif class_at_K_crit == "VALID":
    verdict = "INFO"
else:
    # All corridor VALID or MARGINAL (no BREAKDOWN), but inversion behavior
    # unclear. Treat as INFO.
    verdict = "INFO"

print("--- PASS/FAIL/INFO verdict (plan §9 AND-conjunction) ---")
print(
    f"  [1] all K in [K_R5, K_substrate] VALID: "
    f"{len(classes_in_corridor)} pts; all VALID = {all_corridor_valid}"
)
print(
    f"  [2] K_crit MARGINAL or BREAKDOWN: "
    f"{class_at_K_crit}  →  {crit_marginal_or_breakdown}"
)
print(f"  [3] no BREAKDOWN inside corridor: {no_breakdown_in_corridor}")
print(f"  VERDICT: {verdict}")
print()


# ----------------------------------------------------------------------------
# Section 3 — artifacts
# ----------------------------------------------------------------------------
npz_path = _HERE / "s85_w7_k_corridor_mukhanov_validity.npz"
png_path = _HERE / "s85_w7_k_corridor_mukhanov_validity.png"

np.savez(
    npz_path,
    K_grid=K_grid,
    zdprime_over_z=ratio,  # (ratio IS z″/z / k² by definition here)
    k_squared_ref=1.0,  # (local) normalized to unity in this convention
    ratio=ratio,
    classification=classification,
    K_R5_pinned=K_R5,
    K_substrate_pinned=K_substrate,
    K_crit_pinned=K_crit,
    ratio_0=ratio_0,
    ratio_at_K_R5=ratio_at_K_R5,
    ratio_at_K_substrate=ratio_at_K_substrate,
    ratio_at_K_crit=ratio_at_K_crit,
    class_at_K_R5=class_at_K_R5,
    class_at_K_substrate=class_at_K_substrate,
    class_at_K_crit=class_at_K_crit,
    K_boundary_valid_marginal=K_boundary_valid_marginal,
    K_boundary_marginal_breakdown=K_boundary_marginal_breakdown,
    all_corridor_valid=all_corridor_valid,
    no_breakdown_in_corridor=no_breakdown_in_corridor,
    crit_marginal_or_breakdown=crit_marginal_or_breakdown,
    verdict=verdict,
    # 4-tuple
    value=verdict,  # the output "value" is the verdict classification pattern
    scheme=scheme,
    convention=convention,
    L_max=L_max,
    closure_sha=CLOSURE_SHA,
)

fig, ax = plt.subplots(figsize=(10.5, 6.4), dpi=130)
ax.loglog(K_grid, ratio, color="tab:blue", lw=2, label="ratio(K) = (z″/z) / k²_pivot")
# Classification bands
ax.axhspan(10, 1e6, color="tab:green", alpha=0.15, label="VALID (ratio > 10)")
ax.axhspan(1, 10, color="tab:orange", alpha=0.15, label="MARGINAL (1 ≤ ratio ≤ 10)")
ax.axhspan(1e-6, 1, color="tab:red", alpha=0.15, label="BREAKDOWN (ratio < 1)")
# Annotations
ax.axvline(K_R5, color="tab:blue", ls="-", lw=1, alpha=0.7, label=f"K_R5 = {K_R5}")
ax.axvline(K_substrate, color="tab:green", ls="--", lw=1, alpha=0.7, label=f"K_substrate = {K_substrate}")
ax.axvline(K_crit, color="tab:red", ls="-", lw=1, alpha=0.7, label=f"K_crit = {K_crit}")
ax.axvline(K_boundary_valid_marginal, color="k", ls=":", lw=0.8, alpha=0.5)
ax.axvline(K_boundary_marginal_breakdown, color="k", ls=":", lw=0.8, alpha=0.5)
# Anchor markers
ax.scatter([K_R5, K_substrate, K_crit], [ratio_at_K_R5, ratio_at_K_substrate, ratio_at_K_crit],
           color="k", s=60, zorder=10, marker="D",
           label=f"anchors: {class_at_K_R5}, {class_at_K_substrate}, {class_at_K_crit}")
ax.set_xlabel("K (substrate phonon-dispersion control parameter)")
ax.set_ylabel("ratio = (z″/z) / k²_pivot")
ax.set_title(
    f"S85-W7-6 K-CORRIDOR-MUKHANOV-VALIDITY — verdict {verdict}\n"
    f"ratio(K) = {ratio_0:.0f} · (K_R5/K)²"
)
ax.legend(loc="lower left", fontsize=8, framealpha=0.9, ncol=2)
ax.grid(True, alpha=0.3, which="both")
plt.tight_layout()
plt.savefig(png_path, dpi=130)
plt.close()

print("--- outputs ---")
print(f"  .npz: {npz_path.name} ({npz_path.stat().st_size} bytes)")
print(f"  .png: {png_path.name} ({png_path.stat().st_size} bytes)")
print()


# ----------------------------------------------------------------------------
# Section 4 — verdict append with S85+ dual-SHA
# ----------------------------------------------------------------------------
GATE_ID = "S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY"
verdict_path = _HERE / "s85_gate_verdicts.txt"
content_sha = _file_sha(npz_path)
audit_sha = CLOSURE_SHA

# Summarize classification pattern as value
n_valid = int(np.sum(classification == "VALID"))
n_marginal = int(np.sum(classification == "MARGINAL"))
n_breakdown = int(np.sum(classification == "BREAKDOWN"))
value_str = f"V{n_valid}M{n_marginal}B{n_breakdown}"  # e.g. V13M8B43

canonical_line = (
    f"{GATE_ID}: {verdict} -- "
    f"value={value_str} scheme={scheme} convention={convention} "
    f"L_max={L_max} sha256={audit_sha}"
)
dual_sha_comment = (
    f"# {GATE_ID} dual-SHA: "
    f"content_sha256={content_sha} audit_sha256={audit_sha}"
)

with verdict_path.open("a", encoding="utf-8") as fh:
    fh.write(canonical_line + "\n")
    fh.write(dual_sha_comment + "\n")

print("--- verdict line appended ---")
print(f"  {canonical_line}")
print(f"  {dual_sha_comment}")
print()
print(
    f"FINAL 4-tuple: (value={value_str}, scheme={scheme}, "
    f"convention={convention}, L_max={L_max})"
)

sys.exit(0)
