#!/usr/bin/env python3
"""
S85 W13-4 — R_1 rank-distinguishability sharpening (A_3 vs C_3 at rank 3)
========================================================================

Gate: S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN ([VERIFY])
  PASS  iff  |ratio_AC - 1| <= 0.05 at L_max=10, zeta-scheme
             (rank-universality confirmed — R_1 depends on rank alone).
  FAIL  iff  |ratio_AC - 1| > 0.05
             (rank-universality narrowed — R_1 also depends on root-system
             geometry, simply-laced vs non-simply-laced).
  INFO  iff  0.05 < |ratio_AC - 1| <= 0.10 AND monotone-in-L_max
             (pre-asymptotic; requires L_max >= 11 refit per CC-5).

Output 4-tuple:
  (value=(R_1(A_3), R_1(C_3), ratio_AC), scheme=zeta,
   convention=Cartan-canonical-R_1, L_max=10)

Classification: GEOMETRIC.

METHODOLOGY
-----------
Per plan §W13-4 (sessions/session-plan/session-85-plan-w13.md lines 472-615):

At FIXED rank 3, A_3 and C_3 have:
  - A_3 = SU(4): simply-laced, 6 positive roots (all |alpha|^2 = 2,
    Bourbaki-normalized), dim(SU(4)) = 15.
  - C_3 = Sp(6): non-simply-laced, 9 positive roots (6 short |alpha|^2=1,
    3 long |alpha|^2=2, Bourbaki-normalized), dim(Sp(6)) = 21.

R_1 is the first absolute spectral moment per fiber dimension, evaluated
over truncated Peter-Weyl irrep enumeration at height <= L_max:

    R_1(G, L_max, regulator)
      = (1 / dim(G)) * sum_{lam in irreps height<=L} d(lam) * f_R(C_2(lam))

where d(lam) is the Weyl dimension (Freudenthal product) and f_R is the
regulator shape. For simplicity and consistency with S82 W3-1 Cartan
canonical form R_1 normalization:

    f_zeta(C)       = sqrt(C)              (first absolute moment)
    f_SDW(C)        = C * exp(-C / C_max)  (heat-kernel-weighted)
    f_fstar(C)      = sqrt(C + 1)           (shifted first moment; regulator
                                             robustness proxy)

The rank-universality test:

    ratio_AC = R_1(A_3) / R_1(C_3)  at (L_max, regulator) fixed

    PASS iff |ratio_AC - 1| <= 0.05 at L=10, zeta.

The plan's prediction (line 580-588): root-count heuristic gives
ratio_AC ≈ (|roots_A3| / |roots_C3|)^β = (12/18)^β = (2/3)^β.
  - β ~ 0  → rank-universal PASS (ratio_AC ≈ 1)
  - β ~ 0.10 → borderline PASS/INFO (ratio_AC ≈ 0.96)
  - β ~ 0.20 → FAIL (ratio_AC ≈ 0.92)

SUBSTRATE FRAMING
-----------------
R_1 is the first spectral moment of D_K^G per fiber-group-dim, reading
the substrate's ground-state spectral weight per fiber-Lie-algebra class.
Rank is the substrate's mode-count per fiber-dimension (Cartan subalgebra
size). At FIXED rank 3, A_3 (SU(4), 12 total roots) and C_3 (Sp(6), 18
total roots) differ only in root-system geometry. Tesla framing: two LC
networks with the same number of resonators can still differ in coupling
topology. Rank-universality (PASS) = the substrate's R_1 does NOT resolve
root-system differences at the first-moment level; rank-root-sensitivity
(FAIL) = it DOES.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W13-4-R1-RANK-DISTINGUISHABILITY-SHARPEN"            # (local)
SCHEME = "zeta"                                                     # (local)
CONVENTION = "Cartan-canonical-R_1"                                 # (local)
L_MAX = 10                                                          # (local)

L_MAX_LIST = [7, 8, 9, 10]                                          # (local) per plan
REGULATORS = ["SDW", "zeta", "fstar"]                               # (local) per plan W3-1 atlas

PASS_TOL_REL = 0.05                                                 # (local) plan line 529
INFO_TOL_REL = 0.10                                                 # (local) plan line 557

INPUT_FILES = [                                                     # (local)
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(82, 's82_w3_1_rank_universality.npz'),
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_NPZ = resolve_output(85, 's85_w13_4_r1_rank_distinguishability.npz')
OUT_PNG = resolve_output(85, 's85_w13_4_r1_rank_distinguishability.png')
OUT_JSON = resolve_output(85, 's85_w13_4_r1_rank_distinguishability.json')


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    return h_audit.hexdigest(), hashlib.sha256(script_bytes).hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Lie algebra infrastructure (A_3 and C_3 root systems)
# ---------------------------------------------------------------------------
def a3_positive_roots():
    """A_3 = SU(4), simply-laced, rank 3.
    Euclidean R^4; simple roots alpha_i = e_i - e_{i+1}, |.|^2 = 2.
    Positive roots: e_i - e_j for i < j (6 total).
    """
    roots = []                                                      # (local)
    for i in range(4):
        for j in range(i + 1, 4):
            r = np.zeros(4)                                         # (local)
            r[i] = 1.0
            r[j] = -1.0
            roots.append(r)
    alpha_1 = np.array([1.0, -1.0, 0.0, 0.0])                       # (local)
    alpha_2 = np.array([0.0, 1.0, -1.0, 0.0])                       # (local)
    alpha_3 = np.array([0.0, 0.0, 1.0, -1.0])                       # (local)
    return roots, [alpha_1, alpha_2, alpha_3]


def c3_positive_roots():
    """C_3 = Sp(6), non-simply-laced, rank 3.
    Bourbaki normalization: |long|^2 = 2, |short|^2 = 1.
    Simple roots: alpha_1, alpha_2 short; alpha_3 long.
    Positive roots: e_i - e_j, e_i + e_j (short, i<j, |.|^2=1 each, 6 total)
                    + 2e_i (long, |.|^2=2, 3 total) = 9 positive roots.
    Scale by 1/sqrt(2) to place long at |.|^2=2.
    """
    s = 1.0 / np.sqrt(2.0)                                          # (local)
    roots = []                                                      # (local)
    for i in range(3):
        for j in range(i + 1, 3):
            r1 = np.zeros(3); r1[i] = s; r1[j] = -s                 # (local) e_i - e_j short
            roots.append(r1)
            r2 = np.zeros(3); r2[i] = s; r2[j] = s                  # (local) e_i + e_j short
            roots.append(r2)
    for i in range(3):
        r3 = np.zeros(3); r3[i] = 2.0 * s                           # (local) 2e_i long
        roots.append(r3)
    alpha_1 = s * np.array([1.0, -1.0, 0.0])                        # (local) short
    alpha_2 = s * np.array([0.0, 1.0, -1.0])                        # (local) short
    alpha_3 = s * np.array([0.0, 0.0, 2.0])                         # (local) long
    return roots, [alpha_1, alpha_2, alpha_3]


def fundamental_weights(simple_roots):
    """Compute fundamental weights from simple roots via coroot duality."""
    r = len(simple_roots)                                           # (local)
    coroots = [2.0 * a / np.dot(a, a) for a in simple_roots]        # (local)
    M = np.array([[np.dot(si, cj) for cj in coroots] for si in simple_roots])  # (local)
    Minv = np.linalg.inv(M)                                         # (local)
    w = [sum(Minv[i, j] * simple_roots[j] for j in range(r))
         for i in range(r)]                                         # (local)
    return w


def weyl_dim(lam, positive_roots, rho):
    """Freudenthal product: dim(lam) = prod_{alpha>0} <lam+rho, alpha> / <rho, alpha>."""
    num = 1.0                                                       # (local)
    den = 1.0                                                       # (local)
    for alpha in positive_roots:
        num *= np.dot(lam + rho, alpha)
        den *= np.dot(rho, alpha)
    return num / den


def casimir_2(lam, rho):
    """C_2(lam) = <lam, lam + 2*rho>."""
    return float(np.dot(lam, lam + 2.0 * rho))


def enumerate_irreps(L_max, r):
    """Enumerate all Dynkin labels (a_1, ..., a_r) with sum_i a_i <= L_max,
    excluding the trivial (0, ..., 0). Generator form for memory efficiency.
    """
    for partial_sum in range(1, L_max + 1):
        # Enumerate compositions of partial_sum into r non-negative parts
        for labels in _compositions(partial_sum, r):
            yield labels


def _compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in _compositions(total - first, parts - 1):
            yield (first,) + rest


# ---------------------------------------------------------------------------
# Section 6 — Regulator shape functions
# ---------------------------------------------------------------------------
def regulator_shape(C_val, regulator_name, C_max_for_SDW=100.0):
    """f_R(C) evaluators for R_1 computation.

    - zeta:   f(C) = sqrt(C)                       (first absolute moment)
    - SDW:    f(C) = sqrt(C) * exp(-C / C_max)     (exponentially damped)
    - fstar:  f(C) = sqrt(C + 1)                   (shifted regulator)
    """
    if regulator_name == "zeta":
        return np.sqrt(max(C_val, 0.0))
    if regulator_name == "SDW":
        return np.sqrt(max(C_val, 0.0)) * np.exp(-C_val / C_max_for_SDW)
    if regulator_name == "fstar":
        return np.sqrt(max(C_val, 0.0) + 1.0)
    raise ValueError(f"unknown regulator: {regulator_name}")


# ---------------------------------------------------------------------------
# Section 7 — R_1 computation per group
# ---------------------------------------------------------------------------
def compute_R1(group_label, L_max, regulator_name):
    """R_1(G, L_max, regulator) = (1/dim_G) * sum d(lam) * f_R(C_2(lam))."""
    if group_label == "A_3":
        pos_roots, simple_roots = a3_positive_roots()
        dim_G = 15                                                  # (local) dim(SU(4))
    elif group_label == "C_3":
        pos_roots, simple_roots = c3_positive_roots()
        dim_G = 21                                                  # (local) dim(Sp(6))
    else:
        raise ValueError(f"unsupported group: {group_label}")

    w_list = fundamental_weights(simple_roots)                      # (local)
    rho = 0.5 * sum(pos_roots)                                      # (local)

    r = len(simple_roots)                                           # (local)
    # Max Casimir in truncation for SDW damping reference
    # (deterministic: compute largest-height rep C_2, then set C_max = max × 2)
    highest = np.sum(w_list, axis=0) * L_max                        # (local) approx highest
    C_max_ref = float(casimir_2(highest, rho)) * 2.0                # (local)

    acc = 0.0                                                       # (local)
    count = 0                                                       # (local)
    for dyn in enumerate_irreps(L_max, r):
        lam = sum(dyn[i] * w_list[i] for i in range(r))             # (local)
        d = weyl_dim(lam, pos_roots, rho)                           # (local)
        C2 = casimir_2(lam, rho)                                    # (local)
        f_R = regulator_shape(C2, regulator_name, C_max_for_SDW=C_max_ref)  # (local)
        acc += d * f_R
        count += 1

    R1 = acc / dim_G                                                # (local)
    return R1, count


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                # (local)

    # -----------------------------------------------------------------------
    # 8A. Input pinning
    # -----------------------------------------------------------------------
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')           # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()
    print(f"S85 W13-4: R_1-RANK-DISTINGUISHABILITY-SHARPEN (A_3 vs C_3 at rank 3)")
    print(f"  Gate: {GATE_ID}")
    print(f"  Classification: GEOMETRIC")
    print()

    # -----------------------------------------------------------------------
    # 8B. Scan: 2 groups × 4 L_max × 3 regulators = 24 cells
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 1 — R_1 computation: 2 groups × 4 L_max × 3 regulators = 24 cells")
    print("=" * 78)

    results = {}                                                    # (local)
    for group in ["A_3", "C_3"]:
        for L in L_MAX_LIST:
            for reg in REGULATORS:
                R1, n_irreps = compute_R1(group, L, reg)            # (local)
                results[(group, L, reg)] = (R1, n_irreps)
                print(f"  {group}  L={L:2d}  {reg:>5s}: "
                      f"R_1 = {R1:.6e}  ({n_irreps} irreps)")
    print()

    # -----------------------------------------------------------------------
    # 8C. Ratio test at L_max=10, zeta (primary)
    # -----------------------------------------------------------------------
    R1_A3_L10_zeta = results[("A_3", 10, "zeta")][0]                # (local)
    R1_C3_L10_zeta = results[("C_3", 10, "zeta")][0]                # (local)
    ratio_AC_primary = R1_A3_L10_zeta / R1_C3_L10_zeta              # (local)

    print("=" * 78)
    print("STEP 2 — Primary ratio test at L_max=10, zeta")
    print("=" * 78)
    print(f"  R_1(A_3, L=10, zeta) = {R1_A3_L10_zeta:.6e}")
    print(f"  R_1(C_3, L=10, zeta) = {R1_C3_L10_zeta:.6e}")
    print(f"  ratio_AC             = {ratio_AC_primary:.6f}")
    print(f"  |ratio - 1|          = {abs(ratio_AC_primary - 1.0):.6f}")
    print(f"  PASS threshold       = {PASS_TOL_REL}")
    print(f"  INFO threshold       = {INFO_TOL_REL}")
    print()

    # -----------------------------------------------------------------------
    # 8D. L_max monotonicity check (for INFO branch)
    # -----------------------------------------------------------------------
    ratios_L = np.array([
        results[("A_3", L, "zeta")][0] / results[("C_3", L, "zeta")][0]
        for L in L_MAX_LIST
    ])                                                              # (local)
    deviations_L = np.abs(ratios_L - 1.0)                           # (local)
    monotone_L = (
        np.all(np.diff(deviations_L) <= 0) or                       # monotone decreasing deviation
        np.all(np.diff(deviations_L) >= 0)                          # monotone increasing
    )

    print("=" * 78)
    print("STEP 3 — L_max monotonicity (zeta) for INFO branch")
    print("=" * 78)
    for L, rat, dev in zip(L_MAX_LIST, ratios_L, deviations_L):
        print(f"  L={L:2d}: ratio_AC = {rat:.6f}, |dev| = {dev:.6f}")
    print(f"  monotone in L_max            = {monotone_L}")
    print()

    # -----------------------------------------------------------------------
    # 8E. 3-regulator atlas spread at L_max=10
    # -----------------------------------------------------------------------
    ratios_reg = {
        reg: results[("A_3", 10, reg)][0] / results[("C_3", 10, reg)][0]
        for reg in REGULATORS
    }                                                               # (local)
    print("=" * 78)
    print("STEP 4 — 3-regulator atlas at L_max=10 (SDW, zeta, fstar)")
    print("=" * 78)
    for reg, rat in ratios_reg.items():
        print(f"  ratio_AC ({reg:>5s})          = {rat:.6f}  (|dev|={abs(rat-1.0):.4f})")
    reg_spread = max(ratios_reg.values()) - min(ratios_reg.values())  # (local)
    print(f"  regulator spread              = {reg_spread:.6f}")
    print()

    # -----------------------------------------------------------------------
    # 8F. Verdict
    # -----------------------------------------------------------------------
    deviation_primary = abs(ratio_AC_primary - 1.0)                 # (local)
    if deviation_primary <= PASS_TOL_REL:
        verdict = "PASS"                                            # (local)
    elif deviation_primary <= INFO_TOL_REL and monotone_L:
        verdict = "INFO"                                            # (local)
    else:
        verdict = "FAIL"                                            # (local)

    print("=" * 78)
    print("STEP 5 — Verdict")
    print("=" * 78)
    print(f"  |ratio_AC - 1| at L=10, zeta   = {deviation_primary:.6f}")
    print(f"  PASS (<= 0.05)                  = {deviation_primary <= PASS_TOL_REL}")
    print(f"  INFO (0.05 < |x| <= 0.10,       = {(PASS_TOL_REL < deviation_primary <= INFO_TOL_REL) and monotone_L}")
    print(f"         monotone-L)")
    print(f"  FAIL (> 0.05, not INFO)         = {verdict == 'FAIL'}")
    print(f"  Verdict                         = {verdict}")
    print()

    # -----------------------------------------------------------------------
    # 8G. Plot — log-log scatter + L-sweep
    # -----------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Panel A: R_1 vs rank for {G_2 baseline, A_3, C_3, F_4}
    ax1 = axes[0]
    # S82 W3-1 baselines (L=3 R_1 zeta values)
    try:
        s82 = np.load(resolve_output(82, 's82_w3_1_rank_universality.npz'), allow_pickle=True)
        R1_G2_L3 = float(s82["G2_R1_zeta"][0])                      # (local) L=3 value
        R1_F4_L3 = float(s82["F4_R1_zeta"][0])                      # (local)
        baseline_present = True                                     # (local)
    except Exception:
        R1_G2_L3, R1_F4_L3 = None, None
        baseline_present = False                                    # (local)

    ranks = [2, 3, 3, 4]                                            # (local)
    R1s = [R1_G2_L3, R1_A3_L10_zeta, R1_C3_L10_zeta, R1_F4_L3]      # (local) mixed L for visual
    labels = ["G_2 (S82,L=3)", "A_3 (L=10)", "C_3 (L=10)", "F_4 (S82,L=3)"]  # (local)
    colors = ["green", "blue", "red", "purple"]                     # (local)
    markers = ["o", "s", "D", "^"]                                  # (local)
    if baseline_present:
        for rank, R1, label, c, m in zip(ranks, R1s, labels, colors, markers):
            ax1.scatter([rank], [R1], color=c, marker=m, s=110, label=label)
    ax1.set_xlabel("rank")
    ax1.set_ylabel(r"$R_1$")
    ax1.set_title("R_1 vs rank (A_3 and C_3 at fixed rank 3)")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3, which="both")
    ax1.legend(fontsize=9)

    # Panel B: ratio_AC vs L_max
    ax2 = axes[1]
    ax2.plot(L_MAX_LIST, ratios_L, "b-o", lw=1.5, label="ratio_AC (zeta)")
    ax2.axhline(1.0, color="k", ls="--", lw=1.0, label="rank-universal (ratio=1)")
    ax2.axhline(1.0 + PASS_TOL_REL, color="gray", ls=":", lw=1.0,
                label=f"PASS band |ratio-1|<={PASS_TOL_REL}")
    ax2.axhline(1.0 - PASS_TOL_REL, color="gray", ls=":", lw=1.0)
    ax2.axhline(1.0 + INFO_TOL_REL, color="r", ls=":", lw=0.9,
                label=f"INFO band |ratio-1|<={INFO_TOL_REL}")
    ax2.axhline(1.0 - INFO_TOL_REL, color="r", ls=":", lw=0.9)
    # Regulator spread at L=10
    for reg, rat in ratios_reg.items():
        ax2.scatter([10], [rat], marker="x", s=100, label=f"{reg} L=10: {rat:.4f}")
    ax2.set_xlabel(r"$L_{max}$")
    ax2.set_ylabel(r"$R_1(A_3) / R_1(C_3)$")
    ax2.set_title(f"ratio_AC vs L_max (zeta + 3-reg at L=10); verdict = {verdict}")
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=7, loc="best")

    fig.suptitle(
        f"S85 W13-4: R_1 rank-distinguishability sharpening A_3 vs C_3; "
        f"|ratio-1|={deviation_primary:.4f}",
        y=1.02, fontsize=10)
    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)

    # -----------------------------------------------------------------------
    # 8H. Save npz + json
    # -----------------------------------------------------------------------
    # Serialize results into arrays
    groups_arr = np.array([k[0] for k in results.keys()], dtype=object)
    Ls_arr = np.array([k[1] for k in results.keys()])
    regs_arr = np.array([k[2] for k in results.keys()], dtype=object)
    R1s_arr = np.array([v[0] for v in results.values()])
    n_irreps_arr = np.array([v[1] for v in results.values()])

    np.savez(
        OUT_NPZ,
        groups=groups_arr,
        L_values=Ls_arr,
        regulators=regs_arr,
        R1_values=R1s_arr,
        n_irreps=n_irreps_arr,
        ratios_L=ratios_L,
        L_MAX_LIST=np.array(L_MAX_LIST),
        ratios_by_regulator_L10=np.array(list(ratios_reg.values())),
        regulator_names=np.array(REGULATORS, dtype=object),
        reg_spread_L10=reg_spread,
        R1_A3_L10_zeta=R1_A3_L10_zeta,
        R1_C3_L10_zeta=R1_C3_L10_zeta,
        ratio_AC_primary=ratio_AC_primary,
        deviation_primary=deviation_primary,
        monotone_L=monotone_L,
        verdict=verdict,
        PASS_TOL_REL=PASS_TOL_REL,
        INFO_TOL_REL=INFO_TOL_REL,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump({
            "gate_id": GATE_ID,
            "verdict": verdict,
            "value": {
                "R1_A3_L10_zeta": float(R1_A3_L10_zeta),
                "R1_C3_L10_zeta": float(R1_C3_L10_zeta),
                "ratio_AC": float(ratio_AC_primary),
                "deviation": float(deviation_primary),
            },
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "pins": pins,
        }, fp, indent=2)

    # -----------------------------------------------------------------------
    # 8I. Verdict line + companion row
    # -----------------------------------------------------------------------
    value_str = (f"(R1_A3={R1_A3_L10_zeta:.4e},"
                 f"R1_C3={R1_C3_L10_zeta:.4e},"
                 f"ratio={ratio_AC_primary:.6f})")                   # (local)
    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                               # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
        fp.write(companion)

    # -----------------------------------------------------------------------
    # 8J. Diagnostic summary
    # -----------------------------------------------------------------------
    wall = time.time() - t0                                         # (local)
    print("=" * 78)
    print("OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script  : {__file__}")
    print(f"  Data    : {OUT_NPZ}")
    print(f"  Plot    : {OUT_PNG}")
    print(f"  JSON    : {OUT_JSON}")
    print(f"  Verdict : appended to {VERDICT_TXT}")
    print()
    print(f"VERDICT LINE (appended):")
    print(f"  {verdict_line.strip()}")
    print(f"  {companion.strip()}")
    print()
    print(f"4-tuple: (value={value_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
