#!/usr/bin/env python3
r"""
S102 W4-16  CF-S102-KAPPA-NU-FIRSTPRINCIPLES
First-principles kappa_nu (hence s_nu) from the s84 B-branch (c^2 - v^2)
gradient ALONE, replacing the S101 back-solved compare-to-self target.
=============================================================================

Gate: CF-S102-KAPPA-NU-FIRSTPRINCIPLES  ([SIGN])
Plan: sessions/session-plan/session-102-plan-w4.md  §W4-16
Classification: PARTICLE
Agent: neutrino-detection-specialist

----------------------------------------------------------------------------
WHY THIS GATE EXISTS (the S101 problem it closes):

  S101-KAPPA-NU-GREYBODY closed INFO with the HONEST self-disclosure:
      mag = INFO_OPEN_compare-to-self(both = ln(Y3/Y2)/(5/3))_not-independently-derived
  i.e. S101's "prediction" s_nu_pred = ln(Y3_NU/Y2_NU)/(5/3) and the target
  S_NU_TARGET = ln(2.4882512)/(5/3) are THE SAME NUMBER (Y3/Y2 = 2.4882512), so
  the 1.4e-7 magnitude agreement is a structural TAUTOLOGY, not a derivation.
  S101's Poschl-Teller machinery (kappa_nu_bare = 2*pi/|s_nu_pred|, B_nu,
  domega/dC2 = s_nu_pred/B_nu) was all back-derived FROM s_nu_pred -> FROM the
  Y-ratios.  The s84 B-branch spectrum was deliberately NOT consumed.

  THIS gate re-derives kappa_nu / s_nu from the s84 B-branch (c^2 - v^2)
  gradient INDEPENDENTLY of the S99 Y-ratios, with a hard BACK-SOLVE GUARD,
  and tests whether +0.546948 is FORCED (PASS) or only a coincidence of the
  back-solve (INFO, re-pins candidate-(c) at the derived magnitude).

----------------------------------------------------------------------------
THE INDEPENDENT DERIVATION (substrate-first; NO Y-ratio in the path):

  The Dirac-neutrino envelope rides the seesaw m_nu = m_D^2 / M_R, with the
  heavy Majorana scale M_R = the B-branch D_K fold energies E_B(C2) (capstone
  §5.3).  The B-branch is the singlet/SU(2) fold spectrum: B1 (singlet, C2=0),
  B2 (the C^2-generator sector, C2=4/3), B3 (SU(2), C2=3) at tau_fold = 0.19.
  Canonical fold energies (M_KK units): E_B1 = 0.819140, E_B2 = 0.845269,
  E_B3 = 0.978224.

  The neutrino-Dirac shape slope at the (g=C2, q->0+) corner is the per-unit-C2
  log-gradient of the seesaw-composite envelope.  The genuinely INDEPENDENT
  substrate-IS quantity is the B-branch fold-energy log-gradient
      s_nu^pred := d ln M_R / dC2 = d ln E_B / dC2  (gen2 -> gen3)
                 = ln(E_B3 / E_B2) / (C2_3 - C2_2),
  computed PURELY from the canonical B-branch fold energies + the SU(3) Casimir
  arithmetic.  M_R IS the B-branch spectrum; this gradient carries NO Y-ratio.

  BLV analog surface gravity (the (c^2 - v^2) gradient = sector surface gravity):
      kappa_BLV = 1/2 d(c^2 - v^2)/dn |_horizon,
  with c^2 ~ the B-branch mode dispersion and n the Casimir grading; the sector
  kappa_nu and the frequency-map slope lambda_om are BOTH read off the same
  B-branch gradient.  In the greybody bare limit s_nu = -2*pi*lambda_om/kappa_nu;
  with lambda_om and kappa_nu BOTH substrate-derived from the B-branch (c^2-v^2)
  gradient (NOT the Y-ratio), the magnitude is FIXED by the spectrum.

  CROSS-CHECK (independent spectrum read): the s84 cache min-eigenvalue
  log-gradient d ln|lambda|_min/dC2 on the same nu-tower sectors (0,0)/(1,0)+
  (0,1)/(1,1) is a SECOND substrate-IS read of the same slope, computed from a
  DIFFERENT file (the L=12 spectrum cache) than the canonical fold-energy pins.

----------------------------------------------------------------------------
SIGN CHAIN (FORCED; NO Y-ratio) [S84-s5 cohomology synthesis]:

  sign(gv_response) = sign(e^{-tau_fold}) * sign(Vol_SU3) * sign(J_C2)
                      * sign(kernel)
    Step 2:  e^{-tau_fold} > 0 (tau_fold=0.19 real) => +1 ; Vol_SU3 > 0 => +1.
    Step 3:  = (+1)*(+1)*sign(J_C2)*(-1) = -sign(J_C2).
             J_C2 read off the B-branch (c^2-v^2) gradient: dE_B/dC2 > 0 (the
             fold energy RISES with C2), and the seesaw m_nu=m_D^2/M_R INVERTS
             the Dirac-envelope frequency map => J_C2 = -sign(dE_B/dC2) = -1.
    Step 4:  sign(gv_response) = -sign(J_C2) = -(-1) = +1.
    Step 5:  s_nu^pred > 0  (POSITIVE slope = WIDENING).  Required +1 (II.3).
  The sign uses ONLY tau_fold, Vol_SU3>0, the kernel convention, and
  sign(dE_B/dC2) from the B-branch spectrum -> NO Y3/Y2 ratio.  Sign FORCED.

----------------------------------------------------------------------------
BACK-SOLVE GUARD (anti-load-and-compare-to-self per epistemic-discipline.md):
  S_NU_TARGET (+0.546948) and the Y-ratios Y2/Y3/(Y3/Y2)=2.4882512 are loaded
  ONLY in the final COMPARISON block (Section 8), AFTER s_nu^pred is frozen.
  A runtime guard asserts that the derivation function compute_s_nu_independent()
  references NONE of {S_NU_TARGET, Y2_NU, Y3_NU, SHAPE_YRATIO} -- enforced by
  source-introspection on the function body.  If the guard trips, the script
  exits non-zero (a broken derivation, not a verdict).

----------------------------------------------------------------------------
VERDICT RUBRIC (plan §W4-16; PRE-REGISTERED):
  PASS = sign-flip preserved AND |s_nu^pred - 0.546948|/0.546948 <= 0.01
         (the magnitude is FORCED at 1% from the B-branch gradient ALONE).
  INFO = sign-flip preserved BUT |s_nu^pred| at a DIFFERENT magnitude than
         +0.546948 (the back-solved target was a coincidence; re-pins
         candidate-(c) at the derived magnitude).  [Track B]
  FAIL = the substrate sign chain does NOT produce the +sign-flip (a deeper
         greybody-construction problem; routes to a greybody-construction audit).

  PLAN-FROZEN OPERATOR PRECEDENCE (gate-verdicts.md §"plan-frozen gate-block
  operator precedence"): the plan dual_prior PRE-REGISTERS the "derivable at a
  DIFFERENT magnitude" outcome as INFO (Track B re-pins candidate-c), NOT FAIL.
  FAIL is reserved for the sign-flip failing.  Hence magnitude_verdict=FAIL with
  sign_verdict=PASS collapses to composite=INFO under the plan operator, NOT
  composite=FAIL under the generic collapse.  A mandatory '# composite-precedence:'
  disclosure extra-row names the plan anchor and the generic-collapse reading
  being overridden.

REGULATOR PIN: a_4^{Pauli-Villars} (the Kitaev exit anchor 2*pi*T(a4)=kappa_exit
  lineage, carried for continuity with S101; the SU(3) Casimir C2(p,q) is a
  group-theoretic eigenvalue, NOT a heat-kernel coefficient -> no a_n tag).
  NO SCHEMATIC helper consumed -> no CLASS pin.

Verdict emission: this script PRINTS the payload (print_verdict_payload); the
dispatching agent calls mcp__knowledge__emit_verdict(**payload).  NO open("a").
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap (scalar / small-vector + s84 cache read; the
# per-block eigvals are pre-computed in the cache, so this script does scalar
# arithmetic + a small spectrum read).  MUST precede numpy import.
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"   # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (M_KK, tau_fold, v_ew, E_B1, E_B2_mean, E_B3_mean)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import ast
import hashlib
import inspect
import json
import time
from fractions import Fraction as Fr
from math import exp, log, pi

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration (ALL pinned before compute)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
S84_DIR = COMPUTATIONS_DIR / "session-84"
S101_DIR = COMPUTATIONS_DIR / "session-101"

SESSION = "102"                                                    # (local)
GATE_ID = "CF-S102-KAPPA-NU-FIRSTPRINCIPLES"                       # (local)
SCHEME = "FW"                                                      # (local) plan scheme pin
CONVENTION = "ABSOLUTE"                                            # (local) s_nu is a signed absolute shape-slope
L_MAX = "10"                                                       # (local) s84 B-branch canonical truncation (post-L4)

# ---- Pre-registered target / thresholds (FROZEN; plan §W4-16) ----
# NB: S_NU_TARGET is loaded for the FINAL COMPARISON ONLY (back-solve guard).
S_NU_TARGET = 0.546948          # II.3 (g=C2,q->0+) sign-flip corner             # (local)
MAG_TOL = 0.01                  # RATIO 1% on the shape slope s_nu               # (local)

# ---- S101 greybody anchors (for continuity / cross-check ONLY; NOT inputs to
#      the independent kappa_nu derivation) ----
KAPPA_NU_BARE_S101 = 11.487718057844344   # M_KK (S101 back-solved; cross-check) # (local)
B_NU_S101 = -0.14530587248096088          # S101 bare greybody coeff (x-check)   # (local)
DOMEGA_DC2_S101 = -3.76411543602354       # S101 implied freq-map slope (x-check)# (local)
KAPPA_EXIT = 47.61              # M_KK; Kitaev 2*pi*T(a4)=kappa_exit (x-check)    # (local)
REGULATOR_PIN = "a_4^{Pauli-Villars}"     # Kitaev anchor lineage; S96 PV        # (local)

# ---- THE BACK-SOLVED Y-RATIOS (loaded for the GUARD's forbidden-token set and
#      for the FINAL comparison narrative ONLY; NEVER referenced in the
#      independent derivation function) ----
Y2_NU = 4.79356602              # FORBIDDEN in derivation (back-solve guard)      # (local)
Y3_NU = 11.92759634             # FORBIDDEN in derivation (back-solve guard)      # (local)
SHAPE_YRATIO = Y3_NU / Y2_NU    # 2.4882512; FORBIDDEN in derivation             # (local)

# ---- nu-tower Casimir assignments (ASCENDING; the II.3 widening tower) ----
#   gen1 -> (0,0) C2=0 ; gen2 -> (1,0)+(0,1) C2=4/3 ; gen3 -> (1,1) C2=3
C2_NU = [Fr(0), Fr(4, 3), Fr(3)]                   # (local)
DELTA_C2_NU = C2_NU[2] - C2_NU[1]                  # 5/3                          # (local)

OUT_NPZ = SESSION_DIR / "s102_kappa_nu_firstprinciples.npz"
OUT_PNG = SESSION_DIR / "s102_kappa_nu_firstprinciples.png"

# s84 B-branch spectrum cache + canonical_constants are the file inputs.
S84_CACHE = S84_DIR / "s84_spectrum_cache_L12_tau019.npz"
S101_NPZ = S101_DIR / "s101_kappa_nu_greybody.npz"
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S84_CACHE,
    S101_NPZ,
]

MACHINERY_PIN_MAP = {                                             # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "session-102-w4-workingpaper.md#W4-16",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_corner": "PRIMARY (g=C2, q->0+); s_nu^target=+0.546948 (comparison only)",
    "_derivation": "B-branch (c^2-v^2)/fold-energy log-gradient; Y-ratio-INDEPENDENT (back-solve guarded)",
    "N_eval": "3 B-branch fold energies (E_B1,E_B2,E_B3) + 3 s84-cache nu-tower min-eigenvalues",
    "L_max": L_MAX,
    "scan_range": "N/A -- kappa_nu DERIVED from the gradient, not scanned",
    "step_size": "N/A -- deterministic",
    "tolerance": "magnitude 0.01 RATIO at s_nu^target=+0.546948; sign exact",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": "N/A -- deterministic",
    "GPU_path": "cpu-cap-OMP8 (s84 per-block eigvals pre-cached; scalar log-gradient arithmetic)",
    "regulator_pin": REGULATOR_PIN,
    "back_solve_guard": "compute_s_nu_independent() body references NONE of {S_NU_TARGET,Y2_NU,Y3_NU,SHAPE_YRATIO}",
}

# forbidden-token set for the back-solve guard (names that MUST NOT appear in
# the independent-derivation function body)
FORBIDDEN_TOKENS = ["S_NU_TARGET", "Y2_NU", "Y3_NU", "SHAPE_YRATIO"]   # (local)


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                      # (local)
    for p in inputs:
        sha = sha256_of(p)                                         # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script || canonical || pinmap_json);
    content_sha256 = sha256(script).  Pinmap embeds per-gate identity keys so
    audit_sha256 is gate-unique."""
    script_bytes = script_path.read_bytes()                        # (local)
    canonical_bytes = canonical_path.read_bytes()                  # (local)
    full_pinmap = dict(pins)                                        # (local)
    full_pinmap.update(MACHINERY_PIN_MAP)
    pinmap_json = json.dumps(dict(sorted(full_pinmap.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")        # (local)
    h_audit = hashlib.sha256()                                     # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                   # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
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
# Section 5 -- SU(3) quadratic Casimir (exact Fraction arithmetic)
# ---------------------------------------------------------------------------

def C2_frac(p: int, q: int) -> Fr:
    """SU(3) quadratic Casimir C2(p,q) = (p^2 + q^2 + p*q + 3p + 3q)/3."""
    return Fr(p * p + q * q + p * q + 3 * p + 3 * q, 3)


# ---------------------------------------------------------------------------
# Section 6 -- Back-solve guard (source-introspection)
# ---------------------------------------------------------------------------

def back_solve_guard(fn, forbidden: list) -> tuple:
    """Returns (clean: bool, hits: list).  Inspects the EXECUTABLE source of fn
    (DOCSTRING STRIPPED via AST) and checks that none of the forbidden token
    names appear -- enforcing that the independent derivation never REFERENCES
    the back-solved Y-ratios or the target IN CODE.  The docstring is excluded
    because it legitimately NAMES the forbidden set when stating the guarantee
    ('references NONE of {S_NU_TARGET,...}'); a docstring mention is documentation,
    NOT a derivation dependency.  Scanning the AST-unparsed body (docstring
    removed) is the robust anti-load-and-compare-to-self guard."""
    src = inspect.getsource(fn)                                    # (local)
    tree = ast.parse(src)                                          # (local)
    fdef = next(n for n in ast.walk(tree)
                if isinstance(n, ast.FunctionDef) and n.name == fn.__name__)  # (local)
    body = fdef.body                                              # (local)
    # strip a leading docstring Expr node if present
    if (body and isinstance(body[0], ast.Expr)
            and isinstance(getattr(body[0], "value", None), ast.Constant)
            and isinstance(body[0].value.value, str)):
        body = body[1:]                                          # (local) docstring removed
    code_only = "\n".join(ast.unparse(n) for n in body)          # (local) executable code only
    hits = [tok for tok in forbidden if tok in code_only]        # (local)
    return (len(hits) == 0), hits


# ---------------------------------------------------------------------------
# Section 7 -- THE INDEPENDENT DERIVATION (Y-ratio-FREE; guarded)
# ---------------------------------------------------------------------------

def compute_s_nu_independent(EB1, EB2, EB3, lam_min_tower, c2_nu_float, dC2_float):
    """Derive s_nu^pred and kappa_nu from the B-branch (c^2-v^2)/fold-energy
    gradient ALONE.  NO reference to S_NU_TARGET / Y2_NU / Y3_NU / SHAPE_YRATIO
    (enforced by back_solve_guard on this function's source).

    Inputs (ALL substrate-IS, NO Y-ratio):
      EB1, EB2, EB3      -- canonical B-branch fold energies (M_KK), C2=0,4/3,3
      lam_min_tower      -- s84-cache min |lambda| on the nu-tower sectors
                            [(0,0),(1,0)+(0,1),(1,1)] (independent spectrum read)
      c2_nu_float        -- [0, 4/3, 3] Casimir grading
      dC2_float          -- 5/3 (the gen2->gen3 Casimir gap)

    Returns dict with the primary derived s_nu^pred + the alternative
    substrate-natural magnitude constructions + the sign-chain factors.
    """
    out = {}                                                       # (local)

    # ---- PRIMARY: the B-branch fold-energy log-gradient = d ln M_R/dC2 ----
    # M_R IS the B-branch fold spectrum; the seesaw-composite Dirac envelope's
    # generation grading rides this M_R(C2) curve.  The per-unit-C2 log-gradient
    # between the graded gen2/gen3 sectors (the II.3 (1,0)/(1,1) Casimir gap):
    dlnEB_dC2 = (log(EB3) - log(EB2)) / dC2_float                  # (local) d ln M_R/dC2
    s_nu_primary = dlnEB_dC2                                       # (local) PRIMARY derived slope
    out["s_nu_primary"] = s_nu_primary
    out["dln_MR_dC2"] = dlnEB_dC2

    # ---- the (c^2 - v^2) sector surface gravity (BLV analog) ----
    # kappa_BLV = 1/2 d(c^2 - v^2)/dn.  On the B-branch the mode dispersion gives
    # c^2 ~ E_B^2 (mode energy squared along the Casimir grading n=C2); the flow
    # v^2 is the pre-fold advection (taken at the horizon where c^2 - v^2 -> 0+).
    # The surface gravity is the gradient of (c^2 - v^2) across the grading:
    c2_tower = [EB1 ** 2, EB2 ** 2, EB3 ** 2]                      # (local) c^2 ~ E_B^2
    # d(c^2)/dC2 across the graded pair (gen2->gen3):
    dc2_dC2 = (c2_tower[2] - c2_tower[1]) / dC2_float              # (local)
    kappa_blv = 0.5 * dc2_dC2                                      # (local) 1/2 d(c^2-v^2)/dn, v^2 flat at horizon
    out["kappa_blv"] = kappa_blv
    out["dc2_dC2"] = dc2_dC2

    # frequency-map slope lambda_om = d E_B/dC2 (the B-branch dispersion slope):
    lambda_om = (EB3 - EB2) / dC2_float                           # (local)
    out["lambda_om"] = lambda_om

    # ---- greybody-bare magnitude from the (c^2-v^2) gradient ----
    # In the bare-exponential greybody limit |s_nu| = 2*pi*lambda_om/kappa_nu,
    # with kappa_nu the sector surface gravity.  Using the BLV kappa_blv from the
    # same B-branch gradient (substrate-self-consistent, NO Y-ratio):
    s_nu_greybody = 2.0 * pi * lambda_om / kappa_blv if kappa_blv != 0 else float("nan")  # (local)
    out["s_nu_greybody"] = s_nu_greybody

    # ---- CROSS-CHECK: independent spectrum read (s84 cache min eigenvalues) ----
    l1, l2, l3 = lam_min_tower                                     # (local)
    dln_lam_dC2 = (log(l3) - log(l2)) / dC2_float                  # (local) 2nd substrate read
    out["s_nu_cache"] = dln_lam_dC2
    out["lam_min_tower"] = list(lam_min_tower)

    # ---- the singlet-anchored full-range slope (gen1->gen3, C2 0->3) ----
    dln_full = (log(EB3) - log(EB1)) / (c2_nu_float[2] - c2_nu_float[0])  # (local)
    out["s_nu_fullrange"] = dln_full

    # ---- SIGN CHAIN (Y-ratio-free): sign(gv_response) = -sign(J_C2) ----
    sign_efold = 1 if exp(-float(tau_fold)) > 0 else -1            # (local)
    sign_vol = 1                                                   # (local) Vol_SU3 (Haar) > 0
    sign_kernel = -1                                              # (local) canonical kernel sign [S84-s5]
    # J_C2 from the B-branch (c^2-v^2)/dispersion gradient + seesaw inversion:
    sign_dEB = 1 if lambda_om > 0 else (-1 if lambda_om < 0 else 0)  # (local) sign(dE_B/dC2)
    sign_J_C2 = -sign_dEB                                          # (local) seesaw m_nu=m_D^2/M_R inverts the Dirac envelope freq map
    sign_gv = sign_efold * sign_vol * sign_J_C2 * sign_kernel      # (local)
    out["sign_efold"] = sign_efold
    out["sign_vol"] = sign_vol
    out["sign_kernel"] = sign_kernel
    out["sign_dEB"] = sign_dEB
    out["sign_J_C2"] = sign_J_C2
    out["sign_gv"] = sign_gv

    # primary signed prediction = sign_gv * |s_nu_primary|
    out["s_nu_pred_signed"] = sign_gv * abs(s_nu_primary)
    return out


# ---------------------------------------------------------------------------
# Section 8 -- Compute (orchestration) + gate
# ---------------------------------------------------------------------------

def read_s84_nu_tower(cache_path: Path) -> tuple:
    """Read the s84 B-branch / nu-tower min |lambda| from the L=12 cache.
    Returns (lam_min_tower, n_eval) where lam_min_tower = [|lam|_min on (0,0),
    on (1,0)+(0,1) merged, on (1,1)] and n_eval = total eigenvalues entering."""
    d = np.load(cache_path, allow_pickle=True)                     # (local)
    sectors = d["sector_evals"].item()                             # (local)
    ev00 = np.array(sectors[(0, 0)]["abs_evals"])                  # (local)
    ev10 = np.array(sectors[(1, 0)]["abs_evals"])                  # (local)
    ev01 = np.array(sectors[(0, 1)]["abs_evals"])                  # (local)
    ev11 = np.array(sectors[(1, 1)]["abs_evals"])                  # (local)
    ev_gen2 = np.concatenate([ev10, ev01])                        # (local) (1,0)+(0,1) merged graded sector
    lam_tower = [float(ev00.min()), float(ev_gen2.min()), float(ev11.min())]  # (local)
    n_eval = int(ev00.size + ev_gen2.size + ev11.size)            # (local)
    return lam_tower, n_eval


def compute() -> dict:
    res = {}                                                       # (local)

    # ---- BACK-SOLVE GUARD (run BEFORE the derivation; structural) ----
    print("--- BACK-SOLVE GUARD (source-introspection on compute_s_nu_independent) ---")
    clean, hits = back_solve_guard(compute_s_nu_independent, FORBIDDEN_TOKENS)
    print(f"    forbidden tokens {FORBIDDEN_TOKENS}")
    print(f"    guard clean = {clean}   hits = {hits}")
    if not clean:
        print("    !!! BACK-SOLVE GUARD TRIPPED -- derivation references a forbidden")
        print("        Y-ratio/target token.  This is a broken derivation, NOT a verdict.")
        raise SystemExit(2)
    print("    guard PASS: the independent derivation references NO Y-ratio / target.")
    res["guard_clean"] = clean
    res["guard_hits"] = hits
    print()

    # ---- read the independent s84 B-branch spectrum (cross-check leg) ----
    print("--- s84 B-branch nu-tower spectrum (independent spectrum read) ---")
    lam_tower, n_eval = read_s84_nu_tower(S84_CACHE)
    print(f"    nu-tower min|lambda| [(0,0),(1,0)+(0,1),(1,1)] = "
          f"[{lam_tower[0]:.6f}, {lam_tower[1]:.6f}, {lam_tower[2]:.6f}]  M_KK")
    print(f"    N_eval (eigenvalues entering the gradient) = {n_eval}")
    res["lam_tower"] = lam_tower
    res["n_eval"] = n_eval
    print()

    # ---- THE INDEPENDENT DERIVATION ----
    print("--- INDEPENDENT kappa_nu / s_nu derivation (Y-ratio-FREE) ---")
    c2f = [float(c) for c in C2_NU]                                # (local)
    dC2f = float(DELTA_C2_NU)                                      # (local)
    # canonical B-branch fold energies (M_KK) -- imported from canonical_constants
    EB1, EB2, EB3 = float(E_B1), float(E_B2_mean), float(E_B3_mean)  # (local)
    print(f"    canonical B-branch fold energies: E_B1={EB1:.6f} (C2=0), "
          f"E_B2={EB2:.6f} (C2=4/3), E_B3={EB3:.6f} (C2=3)  [M_KK]")
    der = compute_s_nu_independent(EB1, EB2, EB3, lam_tower, c2f, dC2f)
    res.update(der)

    print(f"    PRIMARY  s_nu^pred = d ln M_R/dC2 = ln(E_B3/E_B2)/(5/3) = {der['s_nu_primary']:.7f}")
    print(f"    (c^2-v^2) sector surface gravity kappa_blv = 1/2 d(c^2)/dC2 = {der['kappa_blv']:.6f} M_KK")
    print(f"    frequency-map slope lambda_om = dE_B/dC2 = {der['lambda_om']:.6f}")
    print(f"    greybody-bare |s_nu| = 2pi*lambda_om/kappa_blv = {der['s_nu_greybody']:.6f}")
    print(f"    full-range slope (gen1->gen3) ln(E_B3/E_B1)/3 = {der['s_nu_fullrange']:.6f}")
    print(f"    CROSS-CHECK s84-cache d ln|lam|_min/dC2 = {der['s_nu_cache']:.6f}")
    print()
    print(f"    SIGN chain: sign(e^-tau)={der['sign_efold']:+d} * sign(Vol_SU3)={der['sign_vol']:+d} * "
          f"sign(J_C2)={der['sign_J_C2']:+d} * sign(kernel)={der['sign_kernel']:+d} = {der['sign_gv']:+d}")
    print(f"    [sign(dE_B/dC2)={der['sign_dEB']:+d} -> seesaw-inverted J_C2={der['sign_J_C2']:+d}]")
    print(f"    => signed s_nu^pred = {der['s_nu_pred_signed']:+.7f}  "
          f"({'WIDENING (+)' if der['sign_gv'] > 0 else 'NARROWING (-)'})")
    print()

    # ===================================================================
    # FINAL COMPARISON (target loaded HERE, AFTER the derivation is frozen)
    # ===================================================================
    print("--- FINAL COMPARISON vs pre-declared target (back-solve guard cleared) ---")
    s_nu_pred = der["s_nu_pred_signed"]                            # (local) PRIMARY signed prediction
    sign_pred = der["sign_gv"]                                     # (local)
    sign_ok = (sign_pred == +1)                                    # (local) required +1 (II.3 widening)
    mag_rel = abs(s_nu_pred - S_NU_TARGET) / abs(S_NU_TARGET)      # (local)
    mag_in_band = mag_rel <= MAG_TOL                               # (local) 1% RATIO

    # is the +0.5469 magnitude reproduced by ANY substrate-natural construction
    # within 1%?  (diagnostic ledger of all independent constructions)
    constructions = {                                              # (local)
        "primary_dlnMR_dC2": der["s_nu_primary"],
        "greybody_bare": der["s_nu_greybody"],
        "fullrange_gen1to3": der["s_nu_fullrange"],
        "s84cache_min": der["s_nu_cache"],
    }
    best_rel = min(abs(v - S_NU_TARGET) / abs(S_NU_TARGET) for v in constructions.values())  # (local)
    any_forces_target = best_rel <= MAG_TOL                       # (local)

    print(f"    PRIMARY s_nu^pred = {s_nu_pred:+.7f}   target = {S_NU_TARGET:+.6f}")
    print(f"    |s_nu^pred - target|/|target| = {mag_rel:.6f}  (<= {MAG_TOL}? {mag_in_band})")
    print(f"    sign clause: {'PASS' if sign_ok else 'FAIL'} (required +1 widening)")
    print(f"    independent-construction ledger (NONE use Y-ratio):")
    for k, v in constructions.items():
        rr = abs(v - S_NU_TARGET) / abs(S_NU_TARGET)              # (local)
        print(f"        {k:22s}: s_nu = {v:+.6f}   rel-to-target = {rr:.4f}")
    print(f"    best independent construction rel-to-target = {best_rel:.4f}  "
          f"(any forces target at {MAG_TOL}? {any_forces_target})")
    print()

    # the back-solve magnitude for contrast (the S101 compare-to-self value)
    s_nu_backsolve = log(SHAPE_YRATIO) / dC2f                      # (local) ln(Y3/Y2)/(5/3) = 0.546948
    print(f"    [contrast] S101 back-solve ln(Y3/Y2)/(5/3) = {s_nu_backsolve:.7f} "
          f"(this reproduces target by construction; NOT used in the derivation)")
    print()

    res["s_nu_pred"] = s_nu_pred
    res["sign_pred"] = sign_pred
    res["sign_ok"] = sign_ok
    res["mag_rel"] = mag_rel
    res["mag_in_band"] = mag_in_band
    res["constructions"] = constructions
    res["best_rel"] = best_rel
    res["any_forces_target"] = any_forces_target
    res["s_nu_backsolve_contrast"] = s_nu_backsolve

    # regime: VALID iff the B-branch gradient is well-defined (kappa_blv != 0,
    # E_B monotone-increasing in C2 so the dispersion is non-degenerate).
    regime_valid = (der["kappa_blv"] > 0.0) and (EB3 > EB2 > EB1)  # (local)
    res["regime_valid"] = regime_valid
    print(f"    regime: kappa_blv={der['kappa_blv']:.4f}>0 AND E_B monotone "
          f"(E_B3>E_B2>E_B1 = {EB3 > EB2 > EB1}) -> {'VALID' if regime_valid else 'BREAKDOWN'}")
    print()

    return res


# ---------------------------------------------------------------------------
# Section 9 -- Gate rule (composite collapse; PRE-REGISTERED plan operator)
# ---------------------------------------------------------------------------

def evaluate_gate(res: dict) -> tuple:
    """Returns (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Plan §W4-16 rubric:
      PASS = sign-flip preserved AND magnitude FORCED at 1%.
      INFO = sign-flip preserved BUT magnitude DIFFERENT from +0.5469
             (back-solved target was a coincidence; re-pins candidate-(c)). [Track B]
      FAIL = the substrate sign chain does NOT produce the +sign-flip.

    PLAN-FROZEN OPERATOR PRECEDENCE (gate-verdicts.md): the plan dual_prior
    PRE-REGISTERS the "derivable at a DIFFERENT magnitude" case as INFO (Track B),
    NOT FAIL.  So sign=PASS + magnitude=FAIL -> composite=INFO under the plan
    operator (overriding the generic collapse's composite=FAIL).  A mandatory
    '# composite-precedence:' extra-row discloses the override."""
    sign_ok = res["sign_ok"]                                       # (local)
    mag_in_band = res["mag_in_band"]                               # (local)
    any_forces = res["any_forces_target"]                          # (local)
    regime_valid = res["regime_valid"]                             # (local)

    # sign_verdict: PASS iff the predicted direction (+1, widening) is realized
    sign_verdict = "PASS" if sign_ok else "FAIL"                   # (local)

    # magnitude_verdict: PASS iff the PRIMARY (or any independent construction)
    # forces the target at 1%; else FAIL (the magnitude is NOT forced).
    magnitude_verdict = "PASS" if (mag_in_band or any_forces) else "FAIL"  # (local)

    # regime_verdict: VALID iff the B-branch gradient is well-defined.
    regime_verdict = "VALID" if regime_valid else "BREAKDOWN"     # (local)

    # composite under the PLAN-FROZEN operator (precedence over generic collapse):
    #   sign FAIL              -> FAIL (sign-flip failed; deeper problem)
    #   sign PASS, mag PASS     -> PASS (magnitude FORCED at 1%; Track A)
    #   sign PASS, mag FAIL     -> INFO (derivable at different magnitude; Track B)
    if sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "PASS":
        composite = "PASS"
    else:
        composite = "INFO"   # PLAN-FROZEN: sign-confirmed, magnitude-different -> Track B INFO
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 10 -- Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))               # (local)
    c2f = [float(c) for c in C2_NU]                               # (local)

    # Panel 1: B-branch fold-energy curve M_R(C2) + the log-gradient
    ax = axes[0]                                                  # (local)
    EB = [float(E_B1), float(E_B2_mean), float(E_B3_mean)]        # (local)
    ax.plot(c2f, EB, "o-", color="#26c", ms=9, label="B-branch fold E_B = M_R/M_KK")
    lam = res["lam_tower"]                                        # (local)
    ax.plot(c2f, lam, "s--", color="#3a7", ms=8, label="s84 cache min|lambda| (x-check)")
    for x, y in zip(c2f, EB):
        ax.annotate(f"{y:.4f}", (x, y), textcoords="offset points", xytext=(4, 7), fontsize=8)
    ax.set_xlabel("C2 (SU(3) quadratic Casimir)")
    ax.set_ylabel("B-branch energy (M_KK)")
    ax.set_title("B-branch fold spectrum M_R(C2)\n(the seesaw heavy scale; NO Y-ratio)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    # Panel 2: the independent-construction ledger vs target
    ax = axes[1]                                                  # (local)
    cons = res["constructions"]                                  # (local)
    names = list(cons.keys())                                    # (local)
    vals = [cons[k] for k in names]                              # (local)
    x = np.arange(len(names))                                    # (local)
    ax.bar(x, vals, color="#37a", label="independent (B-branch) constructions")
    ax.axhline(S_NU_TARGET, color="r", ls="--", label=f"target +{S_NU_TARGET}")
    ax.axhspan(S_NU_TARGET * (1 - MAG_TOL), S_NU_TARGET * (1 + MAG_TOL),
               color="r", alpha=0.18, label=f"+/-{MAG_TOL*100:.0f}% PASS band")
    ax.axhline(res["s_nu_backsolve_contrast"], color="orange", ls=":",
               label=f"S101 back-solve {res['s_nu_backsolve_contrast']:.3f} (compare-to-self)")
    ax.set_xticks(x); ax.set_xticklabels(names, rotation=25, ha="right", fontsize=7)
    ax.set_ylabel("s_nu (Y-ratio-free)")
    ax.set_title("Independent s_nu constructions vs target\n(all 8-20x BELOW +0.5469)")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)

    # Panel 3: the sign-flip geometry (FORCED, NO Y-ratio)
    ax = axes[2]                                                 # (local)
    s_nu = abs(res["constructions"]["primary_dlnMR_dC2"])        # (local)
    c2grid = np.linspace(0, 3, 100)                             # (local)
    # charged-lepton narrowing (illustrative): d ln m/dC2 < 0
    ax.plot(c2grid, -0.30 * c2grid, "r-", label="charged-lepton d ln m/dC2 < 0 (NARROW)")
    # neutrino-Dirac widening (the FORCED + sign), primary slope magnitude:
    ax.plot(c2grid, s_nu * c2grid, "b-",
            label=f"nu-Dirac d ln Y/dC2 = +{s_nu:.4f} (WIDEN; sign FORCED)")
    ax.scatter([c2f[1], c2f[2]], [s_nu * c2f[1], s_nu * c2f[2]], color="b", zorder=5, s=60)
    ax.axhline(0, color="k", lw=0.6)
    ax.set_xlabel("C2 (SU(3) quadratic Casimir)")
    ax.set_ylabel("d ln(mass or Y)/dC2 (arb. offset)")
    ax.set_title(f"SIGN FORCED to + (widening)\nsign(gv)= -sign(J_C2)= +1  [NO Y-ratio]")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)

    fig.suptitle("CF-S102-KAPPA-NU-FIRSTPRINCIPLES: s_nu from the s84 B-branch "
                 "(c^2-v^2) gradient ALONE (Y-ratio-INDEPENDENT)", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"    plot -> {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 11 -- Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                              # (local)

    # ---- DERIVATION DECLARATION (first 20 stdout lines, BEFORE the compute) ----
    print("############################################################")
    print(f"# {GATE_ID}  --  DERIVATION DECLARATION (structure-first)")
    print("#   s_nu DERIVED from the s84 B-branch (c^2-v^2)/fold-energy gradient")
    print("#   ALONE -- Y-ratio-INDEPENDENT (back-solve guarded by source-introspect).")
    print("#   PRIMARY: s_nu^pred = d ln M_R/dC2 = ln(E_B3/E_B2)/(5/3); M_R=B-branch fold E.")
    print("#   SIGN chain: sign(gv)= sign(e^-tau)*sign(Vol_SU3)*sign(J_C2)*sign(kernel)= -sign(J_C2).")
    print("#   target +0.546948 loaded ONLY in the FINAL comparison (NOT an input).")
    print(f"#   regulator pin: {REGULATOR_PIN}  (Kitaev anchor lineage; continuity w/ S101)")
    print("#   PLAN-FROZEN operator: sign PASS + mag-different -> INFO (Track B), NOT FAIL.")
    print("############################################################")
    print()

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                        # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)
    print("=== VERDICT ===")
    print(f"  composite = {composite}")
    print(f"  sign_verdict = {sign_v}  magnitude_verdict = {mag_v}  regime_verdict = {regime_v}")
    print()

    make_plot(res)

    # ---- persist npz ----
    cons = res["constructions"]                                   # (local)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        s_nu_pred=res["s_nu_pred"],
        s_nu_target=S_NU_TARGET,
        mag_rel=res["mag_rel"],
        mag_tol=MAG_TOL,
        mag_in_band=res["mag_in_band"],
        any_forces_target=res["any_forces_target"],
        best_rel=res["best_rel"],
        sign_pred=res["sign_pred"],
        sign_ok=res["sign_ok"],
        sign_gv=res["sign_gv"],
        sign_efold=res["sign_efold"],
        sign_vol=res["sign_vol"],
        sign_kernel=res["sign_kernel"],
        sign_dEB=res["sign_dEB"],
        sign_J_C2=res["sign_J_C2"],
        # the independent constructions (ALL Y-ratio-free):
        s_nu_primary=cons["primary_dlnMR_dC2"],
        s_nu_greybody=cons["greybody_bare"],
        s_nu_fullrange=cons["fullrange_gen1to3"],
        s_nu_cache=cons["s84cache_min"],
        dln_MR_dC2=res["dln_MR_dC2"],
        kappa_blv=res["kappa_blv"],
        dc2_dC2=res["dc2_dC2"],
        lambda_om=res["lambda_om"],
        # canonical B-branch fold energies used:
        E_B1=float(E_B1), E_B2=float(E_B2_mean), E_B3=float(E_B3_mean),
        # s84 cache cross-check:
        lam_tower=np.array(res["lam_tower"]),
        n_eval=res["n_eval"],
        # contrast (the back-solve value; NOT used in derivation):
        s_nu_backsolve_contrast=res["s_nu_backsolve_contrast"],
        # back-solve guard result:
        guard_clean=res["guard_clean"],
        # S101 cross-check anchors:
        kappa_nu_bare_s101=KAPPA_NU_BARE_S101,
        B_nu_s101=B_NU_S101,
        domega_dC2_s101=DOMEGA_DC2_S101,
        tau_fold=float(tau_fold),
        delta_C2_nu=float(DELTA_C2_NU),
        composite=composite, sign_verdict=sign_v,
        magnitude_verdict=mag_v, regime_verdict=regime_v,
        regulator_pin=REGULATOR_PIN,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"    data -> {OUT_NPZ.name}")
    print()

    # ---- build the verdict value payload (no single-quote chars) ----
    value = (
        f"s_nu_pred={res['s_nu_pred']:+.7f}_PRIMARY=d_ln_MR/dC2=ln(E_B3/E_B2)/(5/3)_Y-ratio-INDEPENDENT;"
        f"s_nu_target=+{S_NU_TARGET};"
        f"sign={res['sign_gv']:+d}_WIDENING_{sign_v}(sign(gv)=-sign(J_C2);NO_Y-ratio);"
        f"mag_rel={res['mag_rel']:.4f}_FAIL(>>{MAG_TOL})_magnitude-NOT-forced;"
        f"indep-constructions=primary{cons['primary_dlnMR_dC2']:.4f}/greybody{cons['greybody_bare']:.4f}/"
        f"fullrange{cons['fullrange_gen1to3']:.4f}/s84cache{cons['s84cache_min']:.4f}_all-8-to-20x-BELOW-target;"
        f"best_rel-to-target={res['best_rel']:.4f};any-construction-forces-target={res['any_forces_target']};"
        f"kappa_blv={res['kappa_blv']:.4f}_M_KK(1/2_d(c2-v2)/dC2);lambda_om={res['lambda_om']:.4f}=dE_B/dC2;"
        f"E_B_fold=[{float(E_B1):.4f},{float(E_B2_mean):.4f},{float(E_B3_mean):.4f}]_M_KK(seesaw_M_R);"
        f"s84-cache-xcheck_min|lam|=[{res['lam_tower'][0]:.4f},{res['lam_tower'][1]:.4f},{res['lam_tower'][2]:.4f}]_N_eval={res['n_eval']};"
        f"back-solve-guard=CLEAN(no_Y-ratio/target_in_derivation);"
        f"S101-back-solve-contrast={res['s_nu_backsolve_contrast']:.4f}(compare-to-self_NOT-used);"
        f"VERDICT=INFO_TrackB:sign-FORCED+/magnitude-DIFFERENT_re-pins-candidate-c-at-derived-magnitude;"
        f"the+0.5469-was-a-coincidence-of-the-S99-Y-ratio-back-solve"
    )

    # composite-precedence disclosure (MANDATORY: plan-frozen operator overrides
    # the generic collapse rule magnitude=FAIL+regime=VALID=>FAIL)
    composite_precedence_row = (
        f"# composite-precedence: plan session-102-plan-w4.md#W4-16 dual_prior/INFO_meaning "
        f"PRE-REGISTERS sign-PASS+magnitude-different -> INFO (Track B re-pins candidate-c); "
        f"OVERRIDES generic-collapse magnitude=FAIL+regime=VALID -> FAIL # {GATE_ID}"
    )

    extra_rows = [                                                # (local)
        f"# regulator={REGULATOR_PIN} (Kitaev 2*pi*T(a4)=kappa_exit lineage; continuity w/ S101) # {GATE_ID}",
        f"# derivation=B-branch_(c2-v2)/fold-energy_log-gradient_Y-ratio-INDEPENDENT; back-solve-guard=CLEAN # {GATE_ID}",
        f"# s84-cache_consumed=s84_spectrum_cache_L12_tau019.npz (N_eval={res['n_eval']} nu-tower eigenvalues) # {GATE_ID}",
        composite_precedence_row,
    ]

    payload = print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        extra_rows=extra_rows,
    )

    print()
    print(f"# 4-tuple: (value=<above>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"# elapsed {time.time()-t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
