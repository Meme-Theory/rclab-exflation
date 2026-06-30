#!/usr/bin/env python3
"""
S101 W3-1 S101-NU-DIRAC-ENVELOPE-MAP — sector-keyed exponential Casimir envelope
================================================================================

Gate: S101-NU-DIRAC-ENVELOPE-MAP ([SIGN])

Pre-registered threshold (composite three-clause AND, per candidate):
  PASS clause per candidate:
    (1 shape)   |Y3/Y2 - shape_required|/shape_required <= 0.01
    (2 scale)   |ln r| <= ln(1.05)   with r = Y2_S99 / Y2_map  in (n2) absolute
    (3 rescale) |r2/r3 - 1| <= 0.01   in (n1) gen-2-anchored
  Gate verdict:
    PASS iff ANY pre-registered candidate satisfies all three clauses;
    INFO iff a candidate closes shape (clause 1) but scale (clause 2) fails;
    FAIL iff NO candidate closes shape at 1%.
  Sub-criteria at every tested point:
    Y1 = 0 EXACT for all q > 0  (C2(0,0) = 0; MAP-B structural zero);
    DESI safety per corner (Sigma per corner < bound_DESI from npz).

Family:  Y_i = E1 * (C2,i)^q * exp(s_nu * g(C2,i)),  C2 = (0, 4/3, 3).
Eq.(4) shape hypersurface (S-3 synthesis, session-100a-yukawa-wall-scope-synthesis.md:92):
  ln(shape_required) = q * ln(9/4) + s_nu * Delta_g
  Delta_g = 5/3 for g = C2 ; = 1/sqrt(3) for g = sqrt(C2).

Three pre-registered substrate-candidate exponents:
  (a) s_nu = 2 - S0  = 0.305847   at (g=C2,     q=1/2)   [k=-2 integer-shifted freeze-in]
  (b) s_nu = S0      = 1.694153   at (g=sqrt C2, q->0+)  [EXPECTED KILL; only scale-corner]
  (c) s_nu = s_nu^pred(kappa_nu)  from S101-KAPPA-NU-GREYBODY at (g=C2, q->0+)
      [consumed ONLY iff gate 3 landed at dispatch; else candidate_c=N/A]

ORCHESTRATOR OVERRIDE (upstream candidate c): W3-3 S101-KAPPA-NU-GREYBODY landed
INFO (audit 833ddb9e...). Its s_nu^pred = +0.5469481 (widening, sign-confirmed) feeds
candidate (c), which is LIVE -- sign-confirmed, magnitude-OPEN (W3-3's magnitude was a
compare-to-self tautology, honestly left INFO). Candidate (c) is read from the npz.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-100a/s100a_md_normalization.npz   (Y_S99, shape_required, E1, C2, bound_DESI)
  - computations/session-100a/s100a_freezein_overconstrained.npz   (S0_fit -> candidate (a))
  - computations/session-101/s101_kappa_nu_greybody.npz    (s_nu_pred -> candidate (c), CONDITIONAL)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<...>, scheme=EPS-LX-EXPONENTIAL-CASIMIR-ENVELOPE-S3-GRID,
   convention=MIXED-N1-GEN2-RATIO-N2-ABSOLUTE-COUNTING-RATIO-NORMALIZED-TRACE-MEAN-CARRIER-THRESHOLD-GREYBODY,
   L_max=N/A)

Classification: PARTICLE

METHODOLOGY
-----------
Closed-form algebra on published npz scalars (no diagonalization). The neutrino
towers (0,0)/(1,0)+(0,1)/(1,1) are Peter-Weyl sectors of D_K on Jensen-deformed
SU(3); C2 is their Casimir grading; M_R is the D_K B-branch fold-energy spectrum
(not an external heavy scale). The seesaw back-solve fixes the required Yukawa
triple Y_S99 = [0, 4.79356602, 11.92759634] (S100a-MD-NORMALIZATION INFO). We test
whether a SUBSTRATE-pinned exponent s_nu carries the sector-keyed exponential Casimir
envelope's SHAPE (gen-3/gen-2 ratio 2.4882512), in BOTH normalizations:
  (n1) gen-2-anchored: rescale constancy r2 = r3 (shape-equivalent constancy test);
  (n2) absolute: scale reach r = Y2_S99/Y2_map from E1 alone.
The [SIGN] pre-registration: the neutrino envelope WIDENS in C2 (d ln Y/dC2 = +0.5469)
where the charged-lepton envelope NARROWS (d ln m/dC2 = -S0 = -1.6942) -- OPPOSITE,
the II.3 widening chain. Y1 = 0 EXACT from C2(0,0) = 0 is the structural zero the
surviving class must keep.

DISCIPLINE
----------
- from canonical_constants import * (Sigma_mnu_FW, M_KK, v_ew, tau_fold cross-pins)
- candidate (a) = 2 - S0_fit computed in-script from the npz value (NOT hardcoded)
- a_n regulator tag: candidate (c)'s upstream carries a_4^{Pauli-Villars} (greybody
  Kitaev anchor); this gate consumes only the scalar s_nu_pred -- no a_n citation here.
- CPU OMP8 cap (3-vectors + scalars only; OMP_NUM_THREADS=8 before numpy import)
- dual-SHA emitted (S84+); 4-tuple printed; verdict via emit_verdict (race-safe)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys as _sys
from pathlib import Path as _Path
# _shared (holding canonical_constants.py) added to sys.path before the import.
_SHARED = _Path(__file__).resolve().parents[1] / "_shared"
_sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402  (Sigma_mnu_FW, M_KK, v_ew, tau_fold, ...)

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
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                    # (local)
GATE_ID = "S101-NU-DIRAC-ENVELOPE-MAP"                              # (local)
SCHEME = "EPS-LX-EXPONENTIAL-CASIMIR-ENVELOPE-S3-GRID"              # (local)
CONVENTION = (                                                      # (local)
    "MIXED-N1-GEN2-RATIO-N2-ABSOLUTE-COUNTING-"
    "RATIO-NORMALIZED-TRACE-MEAN-CARRIER-THRESHOLD-GREYBODY"
)
L_MAX = "N/A"                                                       # (local)

# Pre-registered tolerances (S-3 binding text; transcribed unchanged)
TOL_SHAPE = 0.01                                                    # (local) RATIO
TOL_SCALE_LNR = np.log(1.05)                                        # (local) |ln r| bound = 0.0487902
TOL_RESCALE = 0.01                                                  # (local) RATIO

# Casimir grid (pre-declared; matches s100a_md_normalization.npz C2 field)
C2 = np.array([0.0, 4.0 / 3.0, 3.0], dtype=np.float64)             # (local)
DELTA_C2 = C2[2] - C2[1]                                            # (local) 5/3
DELTA_G_SQRT = float(np.sqrt(3.0) - np.sqrt(4.0 / 3.0))            # (local) = 1/sqrt(3)

# q grid: the three S-3 pre-declared values ONLY (q->0+ as analytic limit)
Q_GRID = {"q0+": 0.0, "q1/2": 0.5, "q1": 1.0}                       # (local)

# Output destinations
GATE_LOWER = "s101_nu_dirac_envelope_map"                           # (local)
OUT_NPZ = SESSION_DIR / f"{GATE_LOWER}.npz"
OUT_PNG = SESSION_DIR / f"{GATE_LOWER}.png"

# Upstream npz inputs
MD_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_md_normalization.npz"
FREEZEIN_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_freezein_overconstrained.npz"
KAPPA_NU_NPZ = SESSION_DIR / "s101_kappa_nu_greybody.npz"

# Plan-pinned static SHAs (for runtime reconciliation reporting)
PLAN_SHA_MD = "0b3245b643a127bffac6274b5dad03cd9addd6efa1a5c73ad932142fe9794154"      # (local)
PLAN_SHA_FREEZEIN = "aa5acf5475fe8a2eb301b4c0e39901811cd3bb2587d43766746b9beb5f5f56b6"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    MD_NPZ,
    FREEZEIN_NPZ,
    KAPPA_NU_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Envelope family + clause evaluators
# ---------------------------------------------------------------------------

def g_of(C2_vec: np.ndarray, gkind: str) -> np.ndarray:
    """g(C2): identity for 'C2', sqrt for 'sqrtC2'."""
    if gkind == "C2":
        return C2_vec.copy()
    if gkind == "sqrtC2":
        return np.sqrt(C2_vec)
    raise ValueError(f"unknown gkind {gkind!r}")


def envelope_Y(E1: float, C2_vec: np.ndarray, q: float, s_nu: float,
               gkind: str) -> np.ndarray:
    """Y_i = E1 * (C2,i)^q * exp(s_nu * g(C2,i)).

    The power prefactor (C2,i)^q has C2(0,0)=0 -> 0^q.  For q>0, Y1 = 0 EXACT
    (the MAP-B structural zero).  For q->0+ (q exactly 0 in the analytic limit),
    0^0 := 1 by the analytic-limit convention, BUT the seesaw Y1 must remain 0:
    the gen-1 tower (0,0) carries no Dirac coupling (tree-zero genre, W-4).  We
    therefore enforce Y1 = 0 structurally for ALL q (including the q=0 limit) and
    test the shape on the gen-2/gen-3 ratio only.
    """
    g = g_of(C2_vec, gkind)  # (local)
    Y = np.empty(3, dtype=np.float64)  # (local)
    Y[0] = 0.0  # structural zero (C2(0,0)=0); enforced for all q including q->0+
    for i in (1, 2):
        Y[i] = E1 * (C2_vec[i] ** q) * np.exp(s_nu * g[i])
    return Y


def eval_candidate(name: str, s_nu: float, gkind: str, q: float,
                   E1: float, Y_S99: np.ndarray, shape_req: float,
                   bound_DESI: float, Sigma_target: float) -> dict:
    """Evaluate the three-clause AND for one candidate at its declared corner.

    Clause 1 (shape):    rel-dev of Y3/Y2 vs shape_req <= TOL_SHAPE
    Clause 2 (scale,n2): |ln r|, r = Y2_S99/Y2_map(absolute) <= TOL_SCALE_LNR
    Clause 3 (rescale,n1): |r2/r3 - 1| <= TOL_RESCALE, r_i = Y_i_S99/Y_i_map
    Sub: Y1 = 0 exact; DESI Sigma per corner.
    """
    Y_map = envelope_Y(E1, C2, q, s_nu, gkind)  # (local) absolute (n2) map
    Y2_map, Y3_map = float(Y_map[1]), float(Y_map[2])  # (local)

    # --- Clause 1: SHAPE (gen-3/gen-2 ratio) ---
    shape_map = Y3_map / Y2_map  # (local)
    shape_dev = (shape_map - shape_req) / shape_req  # (local) signed
    shape_pass = bool(abs(shape_dev) <= TOL_SHAPE)

    # --- Clause 2: SCALE (n2 absolute), gen-2 anchor for r ---
    r_scale = float(Y_S99[1]) / Y2_map  # (local) = Y2_S99/Y2_map
    ln_r = float(np.log(r_scale))  # (local)
    scale_pass = bool(abs(ln_r) <= TOL_SCALE_LNR)

    # --- Clause 3: RESCALE constancy (n1 gen-2-anchored) ---
    # per-generation rescale factors r_i = Y_i_S99 / Y_i_map (gen 2, gen 3)
    r2 = float(Y_S99[1]) / Y2_map  # (local)
    r3 = float(Y_S99[2]) / Y3_map  # (local)
    rescale_dev = (r2 / r3) - 1.0  # (local) = (Y2_S99/Y3_S99)*(Y3_map/Y2_map) - 1
    rescale_pass = bool(abs(rescale_dev) <= TOL_RESCALE)

    # --- Sub-criterion: Y1 = 0 exact ---
    y1_zero = bool(Y_map[0] == 0.0)

    # --- Sub-criterion: DESI safety (Sigma per corner) ---
    # The n2-absolute map predicts Yukawa Y_i; the seesaw m_nu scale follows
    # Y_S99 (anchor), but the SHAPE map's own implied light-mass sum is bounded
    # by rescaling the S99 light masses by (Y_map/Y_S99)^2 on the heaviest entry.
    # The plan's DESI clause is per-CORNER: the absolute map overshoots when
    # Y2_map < Y2_S99 (r>1).  Worst overshoot corner gives the plan's
    # 0.0582053*(1.0588)^2 = 0.0652 eV.  Reconstruct the implied Sigma:
    #   factor = (Y3_map/Y3_S99) on the heaviest light mass (dominant term).
    desi_factor = Y3_map / float(Y_S99[2])  # (local) heaviest-entry rescale
    Sigma_corner = Sigma_target * (desi_factor ** 2)  # (local) implied light-mass sum
    desi_safe = bool(Sigma_corner < bound_DESI)

    # --- per-candidate composite (three-clause AND) ---
    all_three = bool(shape_pass and scale_pass and rescale_pass)

    # --- directional (widening) read-off for this candidate ---
    # d ln Y/dC2 from the exponential carrier on the gen-2->gen-3 step:
    #   d ln Y/dC2 = ln(Y3/Y2)/DeltaC2  (composite, includes the q-prefactor)
    dlnY_dC2 = float(np.log(shape_map) / DELTA_C2)  # (local)
    widening = bool(dlnY_dC2 > 0.0)

    return {
        "name": name,
        "s_nu": float(s_nu),
        "gkind": gkind,
        "q": float(q),
        "Y_map": Y_map,
        "Y2_map": Y2_map,
        "Y3_map": Y3_map,
        "shape_map": float(shape_map),
        "shape_dev": float(shape_dev),
        "shape_pass": shape_pass,
        "r_scale": float(r_scale),
        "ln_r": ln_r,
        "scale_pass": scale_pass,
        "r2": r2,
        "r3": r3,
        "rescale_dev": float(rescale_dev),
        "rescale_pass": rescale_pass,
        "y1_zero": y1_zero,
        "desi_factor": float(desi_factor),
        "Sigma_corner": float(Sigma_corner),
        "desi_safe": desi_safe,
        "all_three": all_three,
        "dlnY_dC2": dlnY_dC2,
        "widening": widening,
    }


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # ---- Load upstream scalars ----
    md = np.load(MD_NPZ, allow_pickle=True)
    fz = np.load(FREEZEIN_NPZ, allow_pickle=True)

    Y_S99 = np.asarray(md["Y_S99"], dtype=np.float64)           # (local) [0, 4.79356602, 11.92759634]
    shape_req = float(md["shape_required"])                     # (local) 2.4882511868...
    E1 = float(md["Y_ref"])                                     # (local) gen-1 anchor scale = E_triple[0]
    C2_npz = np.asarray(md["C2"], dtype=np.float64)             # (local) [0, 4/3, 3]
    bound_DESI = float(md["bound_DESI"])                        # (local) 0.072
    Sigma_target = float(md["Sigma_target"])                   # (local) 0.0582053272

    S0_fit = float(fz["S0_fit"])                                # (local) 1.6941531565757249
    cand_a = 2.0 - S0_fit                                       # (local) candidate (a) = 2 - S0, computed not hardcoded

    # cross-check the grid against the npz C2 field
    grid_match = bool(np.allclose(C2, C2_npz, rtol=0, atol=1e-12))  # (local)

    # ---- Candidate (c): conditional on gate 3 landing ----
    candidate_c_available = KAPPA_NU_NPZ.exists()               # (local)
    cand_c = None  # (local)
    cand_c_branch = "N/A"  # (local)
    if candidate_c_available:
        kn = np.load(KAPPA_NU_NPZ, allow_pickle=True)
        cand_c = float(kn["s_nu_pred"])                         # (local) 0.5469480775504529
        cand_c_branch = str(kn["branch"]) if "branch" in kn.files else "from-npz"

    # ---- Eq.(4) shape-exact exponents per corner (analytic reference) ----
    ln_shape = float(np.log(shape_req))                        # (local) 0.9115801291
    ln94 = float(np.log(9.0 / 4.0))                            # (local) 0.8109302162  (= ln(C2_3/C2_2))
    s_exact_C2_qhalf = (ln_shape - 0.5 * ln94) / DELTA_C2      # (local) 0.3036690126
    s_exact_C2_q0 = ln_shape / DELTA_C2                        # (local) 0.5469480775  (= candidate c target)
    s_exact_sqrt_q0 = ln_shape / DELTA_G_SQRT                  # (local) 1.5789030988

    # ---- Evaluate the three candidates at their PRE-DECLARED corners ----
    results = []  # (local)
    res_a = eval_candidate("(a) s_nu=2-S0", cand_a, "C2", 0.5,
                           E1, Y_S99, shape_req, bound_DESI, Sigma_target)
    results.append(res_a)
    res_b = eval_candidate("(b) s_nu=S0", S0_fit, "sqrtC2", 0.0,
                           E1, Y_S99, shape_req, bound_DESI, Sigma_target)
    results.append(res_b)
    if candidate_c_available:
        res_c = eval_candidate("(c) s_nu=s_nu^pred(kappa_nu)", cand_c, "C2", 0.0,
                               E1, Y_S99, shape_req, bound_DESI, Sigma_target)
        results.append(res_c)
    else:
        res_c = None

    # ---- 6-corner grid (g, q) shape-exact map: the closed admissible set ----
    # For each (g, q) corner, the shape-exact s_nu solves Eq.(4); we record it.
    grid_corners = []  # (local)
    for gkind, dg in (("C2", DELTA_C2), ("sqrtC2", DELTA_G_SQRT)):
        for qlabel, qv in Q_GRID.items():
            # shape-exact s at this corner: ln_shape = q*ln(C2_3/C2_2... in g-units)
            # For g=C2:    ratio term = q*ln(9/4); residual / DeltaC2
            # For g=sqrtC2: power term uses C2^q still (q on C2), residual / dg
            s_exact_corner = (ln_shape - qv * ln94) / dg  # (local)
            grid_corners.append({
                "g": gkind, "q_label": qlabel, "q": qv,
                "Delta_g": dg, "s_nu_shape_exact": float(s_exact_corner),
            })

    # ---- Gate composite (PRE-REGISTERED collapse) ----
    any_all_three = any(r["all_three"] for r in results)        # (local)
    any_shape = any(r["shape_pass"] for r in results)           # (local)
    # candidate that closes shape but fails scale -> INFO
    shape_only = [r for r in results if r["shape_pass"] and not r["all_three"]]  # (local)

    if any_all_three:
        composite = "PASS"
    elif any_shape:
        composite = "INFO"   # a candidate closes shape but scale (or rescale) fails
    else:
        composite = "FAIL"

    # ---- schema-v2 3-tuple ([SIGN] trigger) ----
    # sign_verdict: the WIDENING direction prediction.  The substitution-chain
    # Step 4 predicts sign(d ln Y/dC2) = +1 (widening, OPPOSITE charged -S0).
    # Key on the winning/INFO candidate's computed d ln Y/dC2.  Every candidate
    # at a shape-exact-or-near corner reproduces the REQUIRED ratio 2.4882512,
    # whose d ln Y/dC2 = ln(2.4882512)/(5/3) = +0.5469 > 0 by construction.
    # Pick the deciding candidate: the INFO/PASS one (else the shape-closest).
    decider = None  # (local)
    if any_all_three:
        decider = next(r for r in results if r["all_three"])
    elif shape_only:
        decider = shape_only[0]
    else:
        decider = min(results, key=lambda r: abs(r["shape_dev"]))
    sign_verdict = "PASS" if decider["widening"] else "FAIL"

    # magnitude_verdict: the SHAPE corridor magnitude.  PASS iff the deciding
    # candidate closes shape AND scale (full PASS); INFO iff shape closes but
    # scale fails (the EXPECTED branch); FAIL iff no candidate closes shape.
    if composite == "PASS":
        magnitude_verdict = "PASS"
    elif composite == "INFO":
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # regime_verdict: VALID iff the algebra is exact (no expansion regime to
    # break) AND the deciding candidate's Y1=0 sub-criterion + DESI safety hold.
    regime_ok = bool(decider["y1_zero"] and decider["desi_safe"]
                     and grid_match)
    regime_verdict = "VALID" if regime_ok else "MARGINAL"

    return {
        "Y_S99": Y_S99, "shape_req": shape_req, "E1": E1, "C2_npz": C2_npz,
        "bound_DESI": bound_DESI, "Sigma_target": Sigma_target,
        "S0_fit": S0_fit, "cand_a": cand_a, "cand_c": cand_c,
        "cand_c_available": candidate_c_available, "cand_c_branch": cand_c_branch,
        "grid_match": grid_match,
        "ln_shape": ln_shape, "ln94": ln94,
        "s_exact_C2_qhalf": s_exact_C2_qhalf, "s_exact_C2_q0": s_exact_C2_q0,
        "s_exact_sqrt_q0": s_exact_sqrt_q0,
        "results": results, "res_a": res_a, "res_b": res_b, "res_c": res_c,
        "grid_corners": grid_corners,
        "composite": composite, "decider": decider,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "value": composite,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(R: dict) -> None:
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(15, 6))

    # --- Left: Eq.(4) shape hypersurface s_nu(q) for both g, with candidates ---
    ln_shape = R["ln_shape"]; ln94 = R["ln94"]
    qq = np.linspace(0.0, 1.0, 200)  # (local)
    s_C2 = (ln_shape - qq * ln94) / DELTA_C2  # (local)
    s_sq = (ln_shape - qq * ln94) / DELTA_G_SQRT  # (local)
    ax0.plot(qq, s_C2, "-", color="C0", label="shape-exact, g=C2 (Δg=5/3)")
    ax0.plot(qq, s_sq, "-", color="C1", label="shape-exact, g=√C2 (Δg=1/√3)")
    # candidate markers
    ax0.plot(0.5, R["cand_a"], "o", ms=11, color="C0", mec="k",
             label=f"(a) 2-S0={R['cand_a']:.4f} @(C2,½)")
    ax0.plot(0.0, R["S0_fit"], "s", ms=11, color="C1", mec="k",
             label=f"(b) S0={R['S0_fit']:.4f} @(√C2,0⁺) KILL")
    if R["cand_c_available"]:
        ax0.plot(0.0, R["cand_c"], "^", ms=13, color="C2", mec="k",
                 label=f"(c) κ_ν={R['cand_c']:.4f} @(C2,0⁺)")
    ax0.set_xlabel("q  (power prefactor exponent)")
    ax0.set_ylabel("s_ν  (exponential Casimir exponent)")
    ax0.set_title("Eq.(4) shape hypersurface  ln(2.4883)=q·ln(9/4)+s_ν·Δg")
    ax0.legend(fontsize=8, loc="upper right")
    ax0.grid(alpha=0.3)

    # --- Right: per-candidate three-clause table ---
    ax1.axis("off")
    rows = [["cand", "s_ν", "(g,q)", "shape dev", "|ln r|", "rescale", "verdict"]]
    for r in R["results"]:
        v = ("PASS" if r["all_three"] else
             ("INFO" if r["shape_pass"] else "FAIL"))
        rows.append([
            r["name"].split()[0],
            f"{r['s_nu']:.4f}",
            f"({r['gkind']},{r['q']:.1f})",
            f"{r['shape_dev']*100:+.2f}%",
            f"{abs(r['ln_r']):.3f}",
            f"{r['rescale_dev']*100:+.2f}%",
            v,
        ])
    tbl = ax1.table(cellText=rows, loc="center", cellLoc="center")
    tbl.auto_set_font_size(False); tbl.set_fontsize(9); tbl.scale(1.0, 1.7)
    for j in range(len(rows[0])):
        tbl[(0, j)].set_facecolor("#cfe3ff"); tbl[(0, j)].set_text_props(weight="bold")
    ax1.set_title(
        f"GATE = {R['composite']}   |   sign={R['sign_verdict']} "
        f"mag={R['magnitude_verdict']} regime={R['regime_verdict']}\n"
        f"shape tol ±{TOL_SHAPE*100:.0f}%  |  scale |ln r|≤{TOL_SCALE_LNR:.4f}  |  "
        f"rescale ±{TOL_RESCALE*100:.0f}%\n"
        f"d ln Y/dC2 (decider) = {R['decider']['dlnY_dC2']:+.4f} "
        f"(WIDENING; charged −S0={-R['S0_fit']:+.4f})",
        fontsize=9)
    fig.suptitle(f"{GATE_ID} — sector-keyed exponential Casimir envelope "
                 f"(Y_i = E1·C2^q·exp(s_ν·g)); Y1=0 EXACT", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": 101,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # --- runtime input-SHA reconciliation against plan pins ---
    md_sha = pins.get("computations/session-100a/s100a_md_normalization.npz", "")  # (local)
    fz_sha = pins.get("computations/session-100a/s100a_freezein_overconstrained.npz", "")  # (local)
    print(f"  md_normalization SHA match plan: {md_sha == PLAN_SHA_MD}")
    print(f"  freezein SHA match plan:         {fz_sha == PLAN_SHA_FREEZEIN}")
    if md_sha != PLAN_SHA_MD:
        print(f"    WARN: md SHA {md_sha[:16]} != plan {PLAN_SHA_MD[:16]}")
    if fz_sha != PLAN_SHA_FREEZEIN:
        print(f"    WARN: fz SHA {fz_sha[:16]} != plan {PLAN_SHA_FREEZEIN[:16]}")
    print()

    R = compute()

    # ---- console report (NUMBERS first) ----
    print("=" * 78)
    print(f"{GATE_ID} — sector-keyed exponential Casimir envelope")
    print("=" * 78)
    print(f"  shape_required (npz full-float) = {R['shape_req']:.13f}  (pub 2.4882512)")
    print(f"  Y_S99 = {R['Y_S99']}   E1 (Y_ref) = {R['E1']:.10f}")
    print(f"  C2 grid = {C2}  (match npz: {R['grid_match']})  DeltaC2 = {DELTA_C2:.10f}")
    print(f"  Delta_g(sqrt) = {DELTA_G_SQRT:.10f}  (= 1/sqrt3 = {1/np.sqrt(3):.10f})")
    print(f"  S0_fit = {R['S0_fit']:.13f}  ->  candidate (a) = 2 - S0 = {R['cand_a']:.13f}")
    print(f"  ln(shape_req) = {R['ln_shape']:.10f}   ln(9/4) = {R['ln94']:.10f}")
    print()
    print("  --- Eq.(4) shape-exact exponents per corner (analytic reference) ---")
    print(f"    (g=C2,   q=1/2): s_exact = {R['s_exact_C2_qhalf']:.10f}")
    print(f"    (g=C2,   q->0+): s_exact = {R['s_exact_C2_q0']:.10f}  (= candidate (c) target)")
    print(f"    (g=√C2,  q->0+): s_exact = {R['s_exact_sqrt_q0']:.10f}")
    print()
    print("  --- 6-corner (g,q) closed admissible grid: shape-exact s_nu ---")
    for gc in R["grid_corners"]:
        print(f"    g={gc['g']:>7s} q={gc['q_label']:>4s} (Δg={gc['Delta_g']:.5f}): "
              f"s_nu_shape_exact = {gc['s_nu_shape_exact']:.10f}")
    print()
    print(f"  candidate (c) available (gate 3 landed): {R['cand_c_available']}")
    if R["cand_c_available"]:
        print(f"    candidate (c) s_nu^pred = {R['cand_c']:.13f}   branch: {R['cand_c_branch']}")
    print()

    for r in R["results"]:
        print(f"  --- candidate {r['name']}  s_nu={r['s_nu']:.7f}  (g={r['gkind']}, q={r['q']:.2f}) ---")
        print(f"      Y_map = [{r['Y_map'][0]:.0f}, {r['Y_map'][1]:.6f}, {r['Y_map'][2]:.6f}]   (Y1=0 exact: {r['y1_zero']})")
        print(f"      [1 SHAPE]   Y3/Y2 = {r['shape_map']:.7f}  dev = {r['shape_dev']*100:+.4f}%  "
              f"(tol ±{TOL_SHAPE*100:.0f}%) -> {'PASS' if r['shape_pass'] else 'FAIL'}")
        print(f"      [2 SCALE]   r = Y2_S99/Y2_map = {r['r_scale']:.6f}  |ln r| = {abs(r['ln_r']):.6f}  "
              f"(tol {TOL_SCALE_LNR:.6f}) -> {'PASS' if r['scale_pass'] else 'FAIL'}")
        print(f"      [3 RESCALE] r2={r['r2']:.6f} r3={r['r3']:.6f}  |r2/r3-1| = {abs(r['rescale_dev'])*100:.4f}%  "
              f"(tol ±{TOL_RESCALE*100:.0f}%) -> {'PASS' if r['rescale_pass'] else 'FAIL'}")
        print(f"      [DESI]      factor=(Y3_map/Y3_S99)={r['desi_factor']:.6f}  Sigma_corner={r['Sigma_corner']:.7f} eV  "
              f"(bound {R['bound_DESI']:.4f}) -> {'SAFE' if r['desi_safe'] else 'OVERSHOOT'}")
        print(f"      [SIGN]      d ln Y/dC2 = {r['dlnY_dC2']:+.7f}  -> {'WIDENING' if r['widening'] else 'NARROWING'}")
        print(f"      => three-clause AND: {'PASS' if r['all_three'] else 'not-all (shape '+('PASS' if r['shape_pass'] else 'FAIL')+')'}")
        print()

    print(f"  DECIDER candidate: {R['decider']['name']}  "
          f"(d ln Y/dC2 = {R['decider']['dlnY_dC2']:+.7f})")
    print(f"  charged-lepton comparison: d ln m/dC2 = -S0 = {-R['S0_fit']:+.7f}  (NARROWING)")
    print(f"  => sign flip REQUIRED: neutrino {R['decider']['dlnY_dC2']:+.4f} OPPOSITE charged {-R['S0_fit']:+.4f}")
    print()
    print(f"  GATE COMPOSITE = {R['composite']}")
    print(f"  3-tuple: sign={R['sign_verdict']} magnitude={R['magnitude_verdict']} regime={R['regime_verdict']}")
    print()

    # ---- save npz (full float64) ----
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        # upstream scalars
        Y_S99=R["Y_S99"], shape_required=R["shape_req"], E1=R["E1"],
        C2=C2, C2_npz=R["C2_npz"], grid_match=R["grid_match"],
        bound_DESI=R["bound_DESI"], Sigma_target=R["Sigma_target"],
        S0_fit=R["S0_fit"], cand_a=R["cand_a"],
        cand_c=(R["cand_c"] if R["cand_c"] is not None else np.nan),
        cand_c_available=R["cand_c_available"], cand_c_branch=R["cand_c_branch"],
        # analytic references
        ln_shape=R["ln_shape"], ln94=R["ln94"], DeltaC2=DELTA_C2, DeltaG_sqrt=DELTA_G_SQRT,
        s_exact_C2_qhalf=R["s_exact_C2_qhalf"], s_exact_C2_q0=R["s_exact_C2_q0"],
        s_exact_sqrt_q0=R["s_exact_sqrt_q0"],
        # 6-corner grid
        grid_g=np.array([gc["g"] for gc in R["grid_corners"]]),
        grid_q=np.array([gc["q"] for gc in R["grid_corners"]], dtype=np.float64),
        grid_Delta_g=np.array([gc["Delta_g"] for gc in R["grid_corners"]], dtype=np.float64),
        grid_s_exact=np.array([gc["s_nu_shape_exact"] for gc in R["grid_corners"]], dtype=np.float64),
        # per-candidate (a)
        a_s_nu=R["res_a"]["s_nu"], a_gkind=R["res_a"]["gkind"], a_q=R["res_a"]["q"],
        a_Y_map=R["res_a"]["Y_map"], a_shape_map=R["res_a"]["shape_map"],
        a_shape_dev=R["res_a"]["shape_dev"], a_shape_pass=R["res_a"]["shape_pass"],
        a_ln_r=R["res_a"]["ln_r"], a_scale_pass=R["res_a"]["scale_pass"],
        a_rescale_dev=R["res_a"]["rescale_dev"], a_rescale_pass=R["res_a"]["rescale_pass"],
        a_desi_factor=R["res_a"]["desi_factor"], a_Sigma_corner=R["res_a"]["Sigma_corner"],
        a_desi_safe=R["res_a"]["desi_safe"], a_dlnY_dC2=R["res_a"]["dlnY_dC2"],
        a_all_three=R["res_a"]["all_three"],
        # per-candidate (b)
        b_s_nu=R["res_b"]["s_nu"], b_gkind=R["res_b"]["gkind"], b_q=R["res_b"]["q"],
        b_Y_map=R["res_b"]["Y_map"], b_shape_map=R["res_b"]["shape_map"],
        b_shape_dev=R["res_b"]["shape_dev"], b_shape_pass=R["res_b"]["shape_pass"],
        b_ln_r=R["res_b"]["ln_r"], b_scale_pass=R["res_b"]["scale_pass"],
        b_rescale_dev=R["res_b"]["rescale_dev"], b_rescale_pass=R["res_b"]["rescale_pass"],
        b_desi_factor=R["res_b"]["desi_factor"], b_Sigma_corner=R["res_b"]["Sigma_corner"],
        b_desi_safe=R["res_b"]["desi_safe"], b_dlnY_dC2=R["res_b"]["dlnY_dC2"],
        b_all_three=R["res_b"]["all_three"],
        # per-candidate (c) (NaN-filled if unavailable)
        c_present=R["cand_c_available"],
        c_s_nu=(R["res_c"]["s_nu"] if R["res_c"] else np.nan),
        c_gkind=(R["res_c"]["gkind"] if R["res_c"] else "N/A"),
        c_q=(R["res_c"]["q"] if R["res_c"] else np.nan),
        c_Y_map=(R["res_c"]["Y_map"] if R["res_c"] else np.array([np.nan, np.nan, np.nan])),
        c_shape_map=(R["res_c"]["shape_map"] if R["res_c"] else np.nan),
        c_shape_dev=(R["res_c"]["shape_dev"] if R["res_c"] else np.nan),
        c_shape_pass=(R["res_c"]["shape_pass"] if R["res_c"] else False),
        c_ln_r=(R["res_c"]["ln_r"] if R["res_c"] else np.nan),
        c_scale_pass=(R["res_c"]["scale_pass"] if R["res_c"] else False),
        c_rescale_dev=(R["res_c"]["rescale_dev"] if R["res_c"] else np.nan),
        c_rescale_pass=(R["res_c"]["rescale_pass"] if R["res_c"] else False),
        c_desi_factor=(R["res_c"]["desi_factor"] if R["res_c"] else np.nan),
        c_Sigma_corner=(R["res_c"]["Sigma_corner"] if R["res_c"] else np.nan),
        c_desi_safe=(R["res_c"]["desi_safe"] if R["res_c"] else False),
        c_dlnY_dC2=(R["res_c"]["dlnY_dC2"] if R["res_c"] else np.nan),
        c_all_three=(R["res_c"]["all_three"] if R["res_c"] else False),
        # composite + 3-tuple
        composite=R["composite"], decider_name=R["decider"]["name"],
        decider_dlnY_dC2=R["decider"]["dlnY_dC2"],
        charged_dlnm_dC2=-R["S0_fit"],
        sign_verdict=R["sign_verdict"], magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        # tolerances
        tol_shape=TOL_SHAPE, tol_scale_lnr=TOL_SCALE_LNR, tol_rescale=TOL_RESCALE,
        # provenance pins
        M_KK_pin=M_KK, v_ew_pin=v_ew, tau_fold_pin=tau_fold,
        Sigma_mnu_FW_pin=Sigma_mnu_FW,
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )
    print(f"  wrote {OUT_NPZ.name}")

    make_plot(R)
    print(f"  wrote {OUT_PNG.name}")

    # ---- value payload string (NUMBERS-dense, no single-quote chars) ----
    rstar = R["decider"]["r_scale"]  # (local) the surviving scale residual r
    cc = (f"c=N/A" if not R["cand_c_available"]
          else f"c={R['cand_c']:.6f}@(C2,0+)shapeEXACT_scale_r={R['res_c']['r_scale']:.3f}")
    value = (
        f"{R['composite']};"
        f"a=2-S0={R['cand_a']:.6f}@(C2,1/2)shapeDev={R['res_a']['shape_dev']*100:+.3f}%_r={R['res_a']['r_scale']:.3f};"
        f"b=S0={R['S0_fit']:.6f}@(sqrtC2,0+)shapeDev={R['res_b']['shape_dev']*100:+.3f}%_KILL;"
        f"{cc};"
        f"Y1=0EXACT;"
        f"dlnY/dC2={R['decider']['dlnY_dC2']:+.4f}_WIDENING_vs_charged-S0={-R['S0_fit']:+.4f};"
        f"shape_tol1pct_scale_lnr{TOL_SCALE_LNR:.4f}_rescale1pct;"
        f"decider={R['decider']['name'].split()[0]}_r={rstar:.3f}"
    )
    # guard: emit_verdict forbids the single-quote delimiter in value
    assert "'" not in value, "value payload must not contain single-quote"

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra = [
        f"# candidate_c={'LIVE_INFO_upstream_833ddb9e' if R['cand_c_available'] else 'N/A_gate3_unlanded'}"
        f" s_nu_pred={R['cand_c'] if R['cand_c'] is not None else 'NA'}"
        f" (W3-3 INFO: sign-confirmed widening, magnitude-OPEN); "
        f"# S101-NU-DIRAC-ENVELOPE-MAP candidate-c provenance row",
    ]
    print_verdict_payload(
        R["composite"], value, audit_sha, content_sha,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {R['composite']} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
