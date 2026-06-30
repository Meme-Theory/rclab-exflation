#!/usr/bin/env python3
"""
S86 W9-3 — S86-R-PROTECTION-MELLIN-CRITERION (C44, lizzi-track)
================================================================

Gate: S86-R-PROTECTION-MELLIN-CRITERION ([VERIFY-THEOREM])
Plan: sessions/session-plan/session-86-plan-w9.md §W9-3 (lines 427-676)

Pre-registered thresholds (plan §9):
  PASS  iff  concordance >= 0.95  AND per-class concordance >= 0.85 EVERY class
                              AND |concordance(L=10) - concordance(L=8)| <= 0.05
  FAIL  iff  concordance < 0.80
  INFO  iff  0.80 <= concordance < 0.95   (banded; partial validity)
  INFO-DEFER if budget defer (NOT applicable here -- DO NOT DEFER per dispatch)

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-80/s80_w09_canonical_classification.py  (CLASSIFICATION dict)
  - computations/session-86/s86_gate_verdicts.txt                (T10 + W4 closure SHAs)

Output 4-tuple:
  (value=<concordance in [0.0,1.0]>, scheme="Mellin-moment-criterion-test",
   convention="criterion-vs-empirical", L_max=10)

Classification: GEOMETRIC (R-protection is a property of the substrate's
spectral-functional ledger under the 5-regulator atlas).

METHODOLOGY
-----------
The lizzi S-1 §IV.5 criterion proposes:
  "Observable O is R-protected on the 5-atlas {zeta, Zubarev, SDW, cutoff_sqrt,
   anomaly} iff its Mellin moments m_n^O = 0 for all n in {0, 2, 6}."

Empirical comparator (S80 W0-9 184-entry catalog):
  RATIO + ABSOLUTE -> R-protected         (181 / 184)
  MIXED            -> NOT R-protected     (  3 / 184)

Mellin-moment instantiation under SCALAR-pin observables (no per-O spectrum
is available in the catalog; the W0-9 entries are scalar canonical pins, not
multi-eigenvalue densities). The substrate-correct treatment: each scalar pin
v_O is represented by its Dirac-delta spectral density f_O(t) = delta(t-|v_O|).
Then m_n^{O,r} = |v_O|^(n-1) * w_r(|v_O|) where w_r is the atlas regulator
weight at t = |v_O|.

Atlas regulator weights (substrate-canonical):
  w_zeta(t)        = 1                                  [pure Mellin]
  w_Zubarev(t)     = exp(-t)                            [thermal Zubarev]
  w_SDW(t)         = sqrt(t)                            [Seeley-DeWitt root-bias]
  w_cutoff_sqrt(t) = Theta(L_cut - t)                   [hard sharp cutoff]
  w_anomaly(t)     = 1/(1 + t^2)                        [Schwinger anomaly weight]

Substitution chain (full proof in WP §W9-3):
  m_n^{O,r} = 0 within ABS tol iff v_O is STRUCTURALLY ZERO OR the joint
  vanishing across n in {0,2,6} forces |v_O|^{-1} < tol AND |v_O|^5 < tol,
  whose intersection is empty for any v_O > 0. Therefore criterion
  classifies-as-R-protected only observables with v_O = 0 EXACTLY.

DISCIPLINE
----------
- `from canonical_constants import *`
- All locals tagged `# (local)`
- 552 = 184 * 3 Mellin-moment instantiations; vectorized via numpy
  (no GPU needed -- delta-density Mellin reduces to scalar arithmetic)
- SHA-256 of all inputs logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Verdict appended to computations/session-86/s86_gate_verdicts.txt (canonical)
- Per .claude/rules/math-scripts.md: exit 0 regardless of PASS/FAIL/INFO

Per plan §11: PASS validates the 3-Mellin-moment characterization (~10x speedup
on R-protection checks). FAIL refutes the lizzi S-1 §IV.5 criterion as a
3-moment compact characterization on the scalar-pin observable space; the
counter-example CSV becomes S87 substrate to refine (multi-moment, atlas
restriction, or non-Mellin characterization).

Substrate framing: the W0-9 catalog is the substrate's scalar pin ledger;
the Mellin criterion proposes a 3-moment compact diagnostic. Whether it
captures empirical R-protection IS the test. Result is GEOMETRIC.
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 -- CPU thread cap (small problem; no GPU needed for delta densities)
# -----------------------------------------------------------------------------
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
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# -----------------------------------------------------------------------------
# Section 2 -- Canonical constants (MANDATORY first import)
# -----------------------------------------------------------------------------
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc

# Import the W0-9 CLASSIFICATION dict directly (canonical empirical baseline)
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location(
    "s80_w09_canonical_classification",
    resolve_script(80, 's80_w09_canonical_classification.py'),
)
_w09 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(_w09)
CLASSIFICATION = _w09.CLASSIFICATION  # {name: (cls, sub, dim, note)}

# -----------------------------------------------------------------------------
# Section 3 -- Standard imports
# -----------------------------------------------------------------------------
import csv
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 4 -- Pre-registration block (machinery pin per plan §7)
# -----------------------------------------------------------------------------
SESSION = "S86"                                     # (local)
GATE_ID = "S86-R-PROTECTION-MELLIN-CRITERION"       # (local)
SCHEME = "Mellin-moment-criterion-test"             # (local)
CONVENTION = "criterion-vs-empirical"               # (local)
L_MAX = 10                                          # (local) primary
L_MAX_CROSS = 8                                     # (local) cross-check

# Plan §7 pins
MOMENT_ORDERS = (0, 2, 6)                           # (local) lizzi S-1 §IV.5
MOMENT_ZERO_TOL = 1e-8                              # (local) ABS, plan §7
PASS_CONCORD = 0.95                                 # (local) plan §7
INFO_LOW = 0.80                                     # (local) plan §7
PASS_PER_CLASS = 0.85                               # (local) plan §9
PASS_LMAX_STAB = 0.05                               # (local) plan §9
RANDOM_SEED = 0                                     # (local) plan §7

ATLAS_REGULATORS = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")  # (local)

# Output destinations
OUT_NPZ = resolve_output(86, 's86_w9_C44_criterion_test.npz')
OUT_PNG = resolve_output(86, 's86_w9_C44_concordance.png')
OUT_CSV = resolve_output(86, 's86_w9_C44_counterexamples.csv')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(80, 's80_w09_canonical_classification.py'),
    resolve_output(86, 's86_gate_verdicts.txt'),
]

# -----------------------------------------------------------------------------
# Section 5 -- SHA-256 dual-pin block (S84+ schema)
# -----------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# -----------------------------------------------------------------------------
# Section 6 -- Upstream pin verification (T10, W4)
# -----------------------------------------------------------------------------

class MissingUpstreamPinError(RuntimeError):
    pass


def verify_upstream_pins():
    """Read T10 + W4 from s86_gate_verdicts.txt; raise + exit 2 if T10 absent."""
    txt = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    t10_line = None  # (local)
    w4_line = None   # (local)
    for line in txt.splitlines():
        if line.startswith("S86-FI-RD-PERMANENT-REGISTRY:"):
            t10_line = line
        if line.startswith("S86-W-4-CUTOFF-SQRT-ADJUDICATION:"):
            w4_line = line
    if t10_line is None:
        raise MissingUpstreamPinError(
            "T10 S86-FI-RD-PERMANENT-REGISTRY not found in s86_gate_verdicts.txt"
        )
    # Extract closure SHAs
    def extract_sha(line, key="audit_sha256"):  # (local helper)
        for tok in line.split():
            if tok.startswith(f"{key}="):
                return tok.split("=", 1)[1]
        return ""
    t10_sha = extract_sha(t10_line)  # (local)
    w4_sha = extract_sha(w4_line) if w4_line else "ABSENT"  # (local)
    print(f"  upstream T10 (S86-FI-RD-PERMANENT-REGISTRY) audit_sha256 = {t10_sha[:16]}...")
    print(f"  upstream W4 (S86-W-4-CUTOFF-SQRT-ADJUDICATION) audit_sha256 = {w4_sha[:16]}...")
    # W4 verdict outcome -- determine atlas size
    if w4_line is None or "REQUIRES-S86-GATE" in w4_line or "GENUINELY-PHYSICAL" in w4_line:
        atlas_used = ATLAS_REGULATORS  # 5-regulator default
        print(f"  atlas: 5-regulator (W4 not STRUCTURALLY-EXCLUDED)")
    elif "STRUCTURALLY-EXCLUDED" in w4_line:
        atlas_used = tuple(r for r in ATLAS_REGULATORS if r != "cutoff_sqrt")
        print(f"  atlas: 4-regulator (W4 STRUCTURALLY-EXCLUDED cutoff_sqrt)")
    else:
        atlas_used = ATLAS_REGULATORS
        print(f"  atlas: 5-regulator (W4 outcome unrecognized; default)")
    return t10_sha, w4_sha, atlas_used


# -----------------------------------------------------------------------------
# Section 7 -- Atlas regulator weights w_r(t)
# -----------------------------------------------------------------------------

def regulator_weight(reg_name, t_array, L_cut):
    """w_r(t) for atlas regulator reg_name. t_array is positive 1-D array.

    L_cut is the sharp-cutoff scale (used only for w_cutoff_sqrt).

    Each weight is the substrate-canonical Mellin-integrand multiplier:
      zeta:        identity (pure Mellin)
      Zubarev:     thermal exp(-t)
      SDW:         Seeley-DeWitt sqrt(t)
      cutoff_sqrt: hard sharp cutoff Theta(L_cut - t)
      anomaly:     1/(1 + t^2)  (Schwinger BCS-anomaly Mellin weight)
    """
    if reg_name == "zeta":
        return np.ones_like(t_array)
    elif reg_name == "Zubarev":
        return np.exp(-t_array)
    elif reg_name == "SDW":
        return np.sqrt(np.abs(t_array))
    elif reg_name == "cutoff_sqrt":
        return (t_array <= L_cut).astype(float)
    elif reg_name == "anomaly":
        return 1.0 / (1.0 + t_array * t_array)
    else:
        raise ValueError(f"Unknown regulator: {reg_name}")


# -----------------------------------------------------------------------------
# Section 8 -- Empirical-classification load + Mellin moment compute
# -----------------------------------------------------------------------------

def load_empirical_184(L_max_label):
    """Load 184-entry W0-9 empirical classification into ordered observables.

    Returns:
      names        : list of 184 observable names (CLASSIFICATION dict order)
      values       : np.ndarray (184,) scalar pin values from canonical_constants
      cls          : list of 184 classifications {RATIO, ABSOLUTE, MIXED}
      empirical_R  : np.ndarray (184,) bool True iff RATIO or ABSOLUTE
      sub_buckets  : list of 184 sub-bucket strings
      dims         : list of 184 dim_in_M_KK markers (int / "obs" / "conv")

    L_max_label is informational only -- the catalog is L_max-independent
    (each entry is a scalar pin, not an L-truncated spectrum). For the
    L=10 vs L=8 cross-check we induce a small structural perturbation by
    rescaling the SLOT_DEPENDENT_RATIO entries by a known L-truncation ratio
    derived from the s73B truncation table (modeled as 1.0 at L=10, 1.04 at
    L=8 per S73B canonical drift; this is the only L-dependent input).
    """
    names, values, classes, sub_buckets, dims = [], [], [], [], []  # (local x5)
    module_consts = {
        k: v for k, v in vars(cc).items()
        if isinstance(v, (int, float)) and not k.startswith("_")
        and k not in ("AUDIT_PATTERNS", "AUDIT_PATTERNS_COMPILED")
    }
    # S73B canonical drift for SLOT_DEPENDENT_RATIO entries (L=10 -> L=8)
    LMAX_DRIFT_L8 = 1.04   # (local) +4% truncation drift; S73B table
    LMAX_DRIFT_L10 = 1.00  # (local)
    drift = LMAX_DRIFT_L10 if L_max_label == 10 else LMAX_DRIFT_L8  # (local)

    for name, (cls_, sub, dim, _note) in CLASSIFICATION.items():
        v = module_consts.get(name, None)  # (local)
        if v is None:
            continue
        # Apply L-truncation drift only to SLOT_DEPENDENT_RATIO
        v_eff = float(v) * drift if sub == "SLOT_DEPENDENT_RATIO" else float(v)  # (local)
        names.append(name)
        values.append(v_eff)
        classes.append(cls_)
        sub_buckets.append(sub)
        dims.append(dim)
    values_arr = np.array(values)  # (local)
    empirical_R = np.array([c in ("RATIO", "ABSOLUTE") for c in classes])  # (local)
    return names, values_arr, classes, empirical_R, sub_buckets, dims


def compute_mellin_moments(values, atlas_used):
    """Compute m_n^{O,r} = |v_O|^(n-1) * w_r(|v_O|) for all 184 obs x 3 orders
       x len(atlas_used) regulators.

    Substitution chain (plan §10):
      Step 1: m_n^O = integral_0^inf t^(n-1) * delta(t - |v_O|) * w_r(t) dt
      Step 2:       = |v_O|^(n-1) * w_r(|v_O|)
      Step 3 (n=0): = |v_O|^(-1) * w_r(|v_O|)
            (n=2): = |v_O|^( 1) * w_r(|v_O|)
            (n=6): = |v_O|^( 5) * w_r(|v_O|)

    Returns dict { reg: { 'm0': arr, 'm2': arr, 'm6': arr } }.

    For v_O == 0 EXACTLY (structural zero), m_n is set to 0 by convention
    (the delta is at the origin; integrand vanishes for n >= 1; for n=0 it
    diverges but we adopt the regulated value 0 as the structural-zero
    interpretation -- structural zeros mean "no spectral weight at all").
    """
    abs_v = np.abs(values)  # (local)
    L_cut = 10.0 * float(np.max(abs_v))  # (local) cutoff scale = 10x max |v|
    moments = {}  # (local)
    for reg in atlas_used:
        w_at = regulator_weight(reg, abs_v, L_cut)  # (local) w_r(|v_O|)
        # n=0:  |v|^{-1} * w   (with structural-zero -> 0 by convention)
        with np.errstate(divide='ignore', invalid='ignore'):
            m0 = np.where(abs_v > 0, w_at / abs_v, 0.0)
        m2 = abs_v * w_at                      # |v|^1 * w
        m6 = abs_v**5 * w_at                   # |v|^5 * w
        moments[reg] = {"m0": m0, "m2": m2, "m6": m6}
    return moments, L_cut


def criterion_classify(moments, atlas_used, tol):
    """Per plan §6 Step 2:
       criterion_R_protected_i = AND_{r in atlas, n in {0,2,6}} ( |m_n^{O_i,r}| < tol )

    Returns np.ndarray (184,) bool.
    """
    n_obs = len(next(iter(moments.values()))["m0"])  # (local)
    pred = np.ones(n_obs, dtype=bool)  # (local) initialize True; AND-conjunct
    for reg in atlas_used:
        mr = moments[reg]
        cond = (np.abs(mr["m0"]) < tol) & (np.abs(mr["m2"]) < tol) & (np.abs(mr["m6"]) < tol)
        pred = pred & cond
    return pred


def compute_concordance(criterion_R, empirical_R, classes):
    """Concordance (plan §6 Step 4) + per-class breakdown + confusion matrix."""
    agree = (criterion_R == empirical_R)                       # (local)
    concord_total = float(agree.mean())                        # (local)
    classes_arr = np.array(classes)                            # (local)
    per_class = {}                                             # (local)
    for c in ("RATIO", "ABSOLUTE", "MIXED"):
        mask = (classes_arr == c)
        if mask.any():
            per_class[c] = float(agree[mask].mean())
        else:
            per_class[c] = float("nan")
    # Confusion matrix
    TP = int(((criterion_R == True)  & (empirical_R == True)).sum())   # (local)
    TN = int(((criterion_R == False) & (empirical_R == False)).sum())  # (local)
    FP = int(((criterion_R == True)  & (empirical_R == False)).sum())  # (local)
    FN = int(((criterion_R == False) & (empirical_R == True)).sum())   # (local)
    return concord_total, per_class, (TP, TN, FP, FN)


# -----------------------------------------------------------------------------
# Section 9 -- Compute (main pipeline)
# -----------------------------------------------------------------------------

def compute_full(atlas_used):
    """Run the full criterion test at L=10 and L=8; return all diagnostics."""
    np.random.seed(RANDOM_SEED)

    # L=10 (primary)
    names10, vals10, cls10, empR10, subs, dims = load_empirical_184(10)
    moments10, L_cut10 = compute_mellin_moments(vals10, atlas_used)
    crit10 = criterion_classify(moments10, atlas_used, MOMENT_ZERO_TOL)
    conc10, per_class10, conf10 = compute_concordance(crit10, empR10, cls10)

    # L=8 (cross-check stability)
    names8, vals8, cls8, empR8, _, _ = load_empirical_184(8)
    moments8, L_cut8 = compute_mellin_moments(vals8, atlas_used)
    crit8 = criterion_classify(moments8, atlas_used, MOMENT_ZERO_TOL)
    conc8, per_class8, conf8 = compute_concordance(crit8, empR8, cls8)

    # Zeta-only sanity (CC2)
    crit_zeta = criterion_classify(moments10, ("zeta",), MOMENT_ZERO_TOL)
    conc_zeta, _, _ = compute_concordance(crit_zeta, empR10, cls10)

    return {
        "names": names10,
        "values": vals10,
        "classes": cls10,
        "sub_buckets": subs,
        "dims_marker": dims,
        "empirical_R": empR10,
        "moments_L10": moments10,
        "moments_L8": moments8,
        "criterion_L10": crit10,
        "criterion_L8": crit8,
        "criterion_zeta_only": crit_zeta,
        "concordance_L10": conc10,
        "concordance_L8": conc8,
        "concordance_zeta_only": conc_zeta,
        "per_class_L10": per_class10,
        "per_class_L8": per_class8,
        "confusion_L10": conf10,
        "confusion_L8": conf8,
        "L_cut": L_cut10,
        "atlas_used": atlas_used,
    }


def evaluate_gate(diag):
    """Plan §9 banded threshold."""
    c10 = diag["concordance_L10"]                         # (local)
    c8 = diag["concordance_L8"]                           # (local)
    pc = diag["per_class_L10"]                            # (local)
    stab = abs(c10 - c8)                                  # (local) CC1
    pc_min = min(v for v in pc.values() if not np.isnan(v))  # (local)

    # PASS: concordance >= 0.95 AND every class >= 0.85 AND stab <= 0.05
    if (c10 >= PASS_CONCORD) and (pc_min >= PASS_PER_CLASS) and (stab <= PASS_LMAX_STAB):
        return "PASS"
    # FAIL: concordance < 0.80
    if c10 < INFO_LOW:
        return "FAIL"
    # INFO: in band
    return "INFO"


# -----------------------------------------------------------------------------
# Section 10 -- Outputs (NPZ, PNG, CSV)
# -----------------------------------------------------------------------------

def save_npz(diag, closure_sha):
    """Persist the full diagnostic to NPZ per plan §6 OUTPUT spec."""
    # Flatten moments dicts to 2-D arrays (regulators x 184)
    atlas = diag["atlas_used"]                            # (local)
    n_obs = len(diag["names"])                            # (local)
    m0 = np.zeros((len(atlas), n_obs))                    # (local)
    m2 = np.zeros((len(atlas), n_obs))                    # (local)
    m6 = np.zeros((len(atlas), n_obs))                    # (local)
    for i, reg in enumerate(atlas):
        m0[i] = diag["moments_L10"][reg]["m0"]
        m2[i] = diag["moments_L10"][reg]["m2"]
        m6[i] = diag["moments_L10"][reg]["m6"]
    TP, TN, FP, FN = diag["confusion_L10"]                # (local)
    np.savez(
        OUT_NPZ,
        names=np.array(diag["names"]),
        values=diag["values"],
        classes=np.array(diag["classes"]),
        sub_buckets=np.array(diag["sub_buckets"]),
        empirical_R=diag["empirical_R"],
        atlas_regulators=np.array(atlas),
        m_0_per_observable=m0,
        m_2_per_observable=m2,
        m_6_per_observable=m6,
        criterion_classification_L10=diag["criterion_L10"],
        criterion_classification_L8=diag["criterion_L8"],
        criterion_zeta_only=diag["criterion_zeta_only"],
        concordance_total=diag["concordance_L10"],
        concordance_L8=diag["concordance_L8"],
        concordance_zeta_only=diag["concordance_zeta_only"],
        concordance_RATIO=diag["per_class_L10"]["RATIO"],
        concordance_ABSOLUTE=diag["per_class_L10"]["ABSOLUTE"],
        concordance_MIXED=diag["per_class_L10"]["MIXED"],
        confusion_matrix_TP_TN_FP_FN=np.array([TP, TN, FP, FN]),
        L_max_primary=10,
        L_max_cross=8,
        moment_orders=np.array(MOMENT_ORDERS),
        moment_zero_tolerance=MOMENT_ZERO_TOL,
        L_cut=diag["L_cut"],
        closure_sha256=closure_sha,
    )


def save_png(diag, verdict):
    """3-panel: confusion matrix heatmap | per-class concordance bars | scatter."""
    TP, TN, FP, FN = diag["confusion_L10"]                # (local)
    cm = np.array([[TP, FP], [FN, TN]])                   # (local)
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Panel 1: Confusion matrix heatmap
    ax = axes[0]
    im = ax.imshow(cm, cmap="Blues", aspect="auto")
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xticklabels(["empirical R", "empirical NOT R"])
    ax.set_yticklabels(["criterion R", "criterion NOT R"])
    for i in range(2):
        for j in range(2):
            ax.text(j, i, str(cm[i, j]), ha="center", va="center", fontsize=14,
                    color="white" if cm[i, j] > cm.max() * 0.5 else "black")
    ax.set_title(f"Confusion (verdict={verdict}, conc={diag['concordance_L10']:.3f})")
    plt.colorbar(im, ax=ax, fraction=0.046)

    # Panel 2: per-class concordance bars
    ax = axes[1]
    classes = list(diag["per_class_L10"].keys())          # (local)
    vals = [diag["per_class_L10"][c] for c in classes]    # (local)
    bars = ax.bar(classes, vals, color=["#4477AA", "#EE6677", "#228833"])
    ax.axhline(PASS_CONCORD, color="green", ls="--", label=f"PASS={PASS_CONCORD}")
    ax.axhline(INFO_LOW, color="orange", ls="--", label=f"INFO_low={INFO_LOW}")
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Concordance")
    ax.set_title("Per-class concordance (L=10)")
    ax.legend()
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.02,
                f"{val:.3f}", ha="center", fontsize=10)

    # Panel 3: scatter m_2^O vs |value|, colored by class
    ax = axes[2]
    cmap_class = {"RATIO": "#4477AA", "ABSOLUTE": "#EE6677", "MIXED": "#228833"}
    abs_v = np.abs(diag["values"])                        # (local)
    m2_zeta = diag["moments_L10"]["zeta"]["m2"]           # (local)
    for c in ("RATIO", "ABSOLUTE", "MIXED"):
        mask = np.array([cls == c for cls in diag["classes"]])
        if mask.any():
            ax.scatter(abs_v[mask] + 1e-30, np.abs(m2_zeta[mask]) + 1e-30,
                       c=cmap_class[c], label=f"{c} (n={int(mask.sum())})",
                       alpha=0.6, s=20)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("|value(O)|")
    ax.set_ylabel(r"$|m_2^{O,zeta}|$")
    ax.set_title("m_2^O scatter by empirical class")
    ax.legend()

    plt.suptitle(
        f"{GATE_ID} -- L_max=10, atlas={len(diag['atlas_used'])}-regulator", fontsize=12)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110)
    plt.close()


def save_counterexamples_csv(diag):
    """Per plan §6 Step 6: FP + FN observables with full diagnostic.

    CSV columns:
      name | empirical_class | criterion_R | empirical_R | error_type
      | value | m_0_zeta | m_2_zeta | m_6_zeta
    """
    crit10 = diag["criterion_L10"]
    empR = diag["empirical_R"]
    rows = []  # (local)
    m0z = diag["moments_L10"]["zeta"]["m0"]
    m2z = diag["moments_L10"]["zeta"]["m2"]
    m6z = diag["moments_L10"]["zeta"]["m6"]
    for i, name in enumerate(diag["names"]):
        if crit10[i] != empR[i]:
            err_type = "FP" if (crit10[i] and not empR[i]) else "FN"  # (local)
            rows.append({
                "name": name,
                "empirical_class": diag["classes"][i],
                "sub_bucket": diag["sub_buckets"][i],
                "criterion_R": int(crit10[i]),
                "empirical_R": int(empR[i]),
                "error_type": err_type,
                "value": float(diag["values"][i]),
                "m_0_zeta": float(m0z[i]),
                "m_2_zeta": float(m2z[i]),
                "m_6_zeta": float(m6z[i]),
            })
    fieldnames = ["name", "empirical_class", "sub_bucket", "criterion_R",
                  "empirical_R", "error_type", "value",
                  "m_0_zeta", "m_2_zeta", "m_6_zeta"]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fp:
        w = csv.DictWriter(fp, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    return len(rows)


# -----------------------------------------------------------------------------
# Section 11 -- Verdict line emission (S84+ dual-SHA schema)
# -----------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict, value, audit_sha, content_sha):
    """Atomic append; canonical line + dual-SHA companion comment row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256 companion row: {GATE_ID} "
        f"audit={audit_sha[:16]} content={content_sha[:16]} "
        f"verdict_band=PASS|FAIL|INFO concord_PASS={PASS_CONCORD} "
        f"INFO_band=[{INFO_LOW},{PASS_CONCORD}) atlas=5-regulator "
        f"moment_orders={list(MOMENT_ORDERS)} tol={MOMENT_ZERO_TOL}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# -----------------------------------------------------------------------------
# Section 12 -- Main
# -----------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...")

    # 2. Verify upstream T10 + W4 pins
    try:
        t10_sha, w4_sha, atlas_used = verify_upstream_pins()
    except MissingUpstreamPinError as e:
        print(f"FATAL: {e}", file=sys.stderr)
        return 2

    # 3. Compute dual-SHA
    script_path = Path(__file__).resolve()
    canonical_path = resolve_script(None, 'canonical_constants.py')
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 4. Mapping pin protocol report (per plan §7)
    print(f"  RATIO/ABSOLUTE/MIXED -> R-protected mapping (plan §6 Step 3):")
    print(f"    RATIO    -> R-protected  (per W0-9 closeout)")
    print(f"    ABSOLUTE -> R-protected  (per W0-9 closeout)")
    print(f"    MIXED    -> NOT R-protected  (per W11-3 NCG-Structural-Exclusion)")
    print(f"  No mapping discrepancy with plan §6 default; no override.")
    print()

    # 5. Compute pipeline
    print("=== compute pipeline ===")
    diag = compute_full(atlas_used)
    n_obs = len(diag["names"])  # (local)
    print(f"  observables: {n_obs}")
    print(f"  atlas: {atlas_used}")
    print(f"  Mellin integrals computed: {n_obs} obs x {len(MOMENT_ORDERS)} orders x "
          f"{len(atlas_used)} regulators = {n_obs * 3 * len(atlas_used)}")
    print()

    print("=== concordance ===")
    print(f"  concordance (L=10, full atlas) = {diag['concordance_L10']:.6f}")
    print(f"  concordance (L=8, full atlas)  = {diag['concordance_L8']:.6f}")
    print(f"  concordance (L=10, zeta-only)  = {diag['concordance_zeta_only']:.6f}")
    print(f"  L=10 vs L=8 stability          = {abs(diag['concordance_L10']-diag['concordance_L8']):.6f}")
    print()
    print("  per-class concordance (L=10):")
    for c, v in diag["per_class_L10"].items():
        print(f"    {c:9s} = {v:.6f}")
    print()
    TP, TN, FP, FN = diag["confusion_L10"]
    print(f"  confusion matrix (L=10): TP={TP} TN={TN} FP={FP} FN={FN}")
    print()

    # 6. Evaluate gate
    verdict = evaluate_gate(diag)
    value = diag["concordance_L10"]  # (local)

    # 7. Save outputs
    save_npz(diag, closure)
    save_png(diag, verdict)
    n_counter = save_counterexamples_csv(diag)
    print(f"  counter-examples (FP+FN): {n_counter} rows -> {OUT_CSV.name}")
    print()

    # 8. Emit 4-tuple + verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 9. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (concordance={value:.4f}; wall {wall:.1f}s) ===")
    # Per .claude/rules/math-scripts.md: exit 0 regardless of PASS/FAIL/INFO
    return 0


if __name__ == "__main__":
    sys.exit(main())
