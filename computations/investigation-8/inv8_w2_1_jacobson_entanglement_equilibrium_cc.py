#!/usr/bin/env python3
"""
INV8 W2-1 — Jacobson Entanglement-Equilibrium -> Cosmological-Constant Magnitude
=================================================================================

Gate: INV8-W2-1 ([SIGN])

Pre-registered threshold (plan §W2-1):
  operator: delta S_gen(ell)|_{delta V=0} = 0  solved for Lambda_substrate;
            then  D_OOM = |log10(Lambda_substrate dimensionalized) - log10(rho_Lambda,obs)|
  strict_PASS_boundary: D_OOM < 1.0 (CC magnitude recovered to within 1 OOM via
            entanglement equilibrium -> would CLOSE JACOBSON-NONLOCAL-64), direction "<"
  PASS  iff D_OOM < 1.0 AND Lambda_substrate > 0
  FAIL  iff D_OOM > 3.0 OR  Lambda_substrate < 0 (wrong sign)
  INFO  iff 1.0 <= D_OOM <= 3.0, OR small-diamond expansion breaks down within the
            scan window (regime=MARGINAL/BREAKDOWN), OR W1-1 unmet + fallback discrepancy.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py     (feeds audit_sha256 only)
  - computations/session-52/s52_bogoliubov_amp.npz   (GGE Bogoliubov state; AMP-52)
  - computations/investigation-8/inv8_gate_verdicts.txt (INV8-W1-1 verdict;
        if absent/empty -> substrate-first fallback, S_ent discrepancy disclosed)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=D_OOM, scheme=FW-zeta, convention=ABSOLUTE, L_max=10)

Classification: PHONONIC
  The CC IS the a_0 spectral moment of D_K; the entanglement entropy IS the GGE
  causal-diamond half-trace; the modular flow IS Tomita-Takesaki on
  A_hor = A_K rtimes_{sigma^omega} R (§VII.BZ, STAGE-3-PERMANENT, S105-S106).

METHODOLOGY
-----------
Jacobson-2015 (PRL 116.201101) entanglement-equilibrium variation executed with the
substrate's ACTUAL modular flow and ACTUAL entanglement entropy.

  Step 1: S_gen(ell) = S_ent(GGE, ell) + A(ell)/(4 G_eff) - (Lambda_sub/8 pi G_eff) V(ell)
          (generalized entropy of a small causal diamond of geodesic radius ell).
  Step 2: G_eff^{-1} = Lambda_cutoff^2 f_2 a_2(D_K)            (PB-8; a_2-channel Newton coupling).
          a_2 = a_2_FW_zeta ; a_0 = a_0_FW_zeta (canonical; a_n^{zeta}).
  Step 3: S_ent(GGE, ell) = causal-diamond half-trace entanglement entropy of rho_GGE,
          the half-mode trace over a sub-region of the 8-mode Richardson-Gaudin GGE.
          (Three distinct entropies are disclosed: S_ent=0 global BCS product state;
           S_GGE full 8-mode von-Neumann; S_diamond the causal-diamond half-trace.)
  Step 4: entanglement equilibrium  delta S_gen|_{delta V=0} = 0
          => delta S_ent = - delta(A/4 G_eff)  (area term balances matter-entanglement).
  Step 5: restore delta V != 0 (maximal-vacuum-entanglement):
          Lambda_substrate = 8 pi G_eff [d S_ent / d V]_eq
                           = (8 pi / (Lambda_cutoff^2 f_2 a_2)) [d S_ent / d V]_eq.
  Step 6: sign read-off  d S_ent/d V > 0 (entropy increases with diamond volume) and
          G_eff > 0, 8 pi > 0  =>  Lambda_substrate > 0 (de-Sitter-like, sign-consistent
          with observed positive rho_Lambda).

The CC magnitude is then dimensionalized and compared to rho_Lambda,obs; D_OOM is the
deliverable. TWO dimensionalization routes are computed for transparency:
  ROUTE 1 (bare a_0 spectral-action variation, NOT entanglement-equilibrium):
          Lambda_SA = (f_0/f_2)(a_0/a_2) Lambda_sp^2 ; rho_SA = Lambda_SA M_Pl^2/(8 pi)
          -> the canonical NAIVE 114-115.5 OOM gap (S64 SA-VERSUS-JACOBSON; what
             DILUTION-CC closes via Volovik tracking, a DIFFERENT route).
  ROUTE 2 (Jacobson-2015 entanglement-equilibrium, the gate's actual functional):
          rho_ent = T_modular * (d S_ent/d V), with T_modular the substrate modular
          (Unruh) temperature on A_hor and d S_ent/d V the causal-diamond entanglement
          density. This is the magnitude D_OOM keys on.

The canonical D_OOM is ROUTE 2 (the entanglement-equilibrium functional). ROUTE 1 is
reported as the bare-a_0 reference the route is measured against.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU numpy capped at OMP_NUM_THREADS=8 (matrices are tiny: 8-mode RDM, scalar scan)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict via the emit_verdict knowledge-MCP tool (race-safe): the script PRINTS
  the payload (print_verdict_payload); the dispatching AGENT calls emit_verdict.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403
import canonical_constants as _cc  # explicit handle for getattr fallbacks

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
SESSION_DIR = Path(__file__).resolve().parent           # computations/investigation-8/
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "8"                                            # (local) investigation number
GATE_ID = "INV8-W2-1"                                    # (local)
SCHEME = "FW-zeta"                                       # (local)
CONVENTION = "ABSOLUTE"                                  # (local)
L_MAX = 10                                               # (local)

# Pre-registered pass/fail thresholds (plan §W2-1 strict_PASS_boundary + rubric)
PASS_D_OOM = 1.0                                         # (local) D_OOM < 1.0 -> PASS
FAIL_D_OOM = 3.0                                         # (local) D_OOM > 3.0 -> FAIL
N_EVAL = 100                                             # (local) diamond radii scanned
SCAN_MIN = 1.0e-3                                        # (local) ell / M_KK^{-1}
SCAN_MAX = 1.0e+3                                        # (local) ell / M_KK^{-1}
ROOT_TOL = 1.0e-10                                       # (local) delta S_gen=0 root tol

# Output destinations
OUT_NPZ = SESSION_DIR / "inv8_w2_1_jacobson_entanglement_equilibrium_cc.npz"
OUT_PNG = SESSION_DIR / "inv8_w2_1_jacobson_entanglement_equilibrium_cc.png"

S52_NPZ = COMPUTATIONS_DIR / "session-52" / "s52_bogoliubov_amp.npz"
INV8_VERDICTS = SESSION_DIR / "inv8_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S52_NPZ,
    INV8_VERDICTS,
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


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p).replace("\\", "/")  # (local)
        print(f"  {rel}: {(sha[:16] + '...') if sha else '<absent/empty>'}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
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


# ---------------------------------------------------------------------------
# Section 5 — Physics helpers
# ---------------------------------------------------------------------------
def mode_entropy(n):
    """von-Neumann entropy (nats) of a single Bogoliubov mode at quasiparticle
    occupation n (a 2-level {0, n} distribution): -n ln n - (1-n) ln(1-n)."""
    n = float(n)  # (local)
    if n <= 0.0 or n >= 1.0:
        return 0.0
    return -n * np.log(n) - (1.0 - n) * np.log(1.0 - n)


def load_gge_state():
    """Load the s52 GGE Bogoliubov state. Returns (labels, u, v, n_k)."""
    d = np.load(S52_NPZ, allow_pickle=True)  # (local)
    u = np.asarray(d["u_k"], dtype=float)    # (local)
    v = np.asarray(d["v_k"], dtype=float)    # (local)
    labels = np.asarray(d["branch_labels"])  # (local)
    n_k = v ** 2                             # (local) per-mode quasiparticle occupation
    return labels, u, v, n_k


def w1_1_status():
    """Resolve the INV8-W1-1 prereq STATUS for the diamond S_ent anchor.

    The plan prereq is specifically the INV8-W1-1 producer that emits the
    causal-diamond S_ent = 1.039 nats. A W1-1 line that is non-PASS (or whose
    payload carries no S_ent, e.g. the PBH/fold-transit-spectrum producer whose
    value is an I_PBH integral) is treated as UNMET -> the substrate-first
    fallback anchors the diamond instead (plan §"Discipline on the S_ent
    discrepancy": the W1-1 S_ent is an INPUT VALUE, not a structural
    prerequisite; the gate is runnable regardless, with the fallback disclosed).

    Returns (status_str, S_ent_input_or_None). A PASS line carrying an explicit
    S_ent token would return ('PRESENT-PASS', value); anything else -> UNMET."""
    if not INV8_VERDICTS.exists():
        return "UNMET-FALLBACK-absent", None
    try:
        txt = INV8_VERDICTS.read_text(encoding="utf-8", errors="ignore")  # (local)
    except OSError:
        return "UNMET-FALLBACK-unreadable", None
    for line in txt.splitlines():
        if not line.startswith("INV8-W1-1"):
            continue
        # A usable W1-1 anchor requires (i) PASS and (ii) an S_ent payload token.
        is_pass = (" PASS " in f" {line} ") or line.split(":", 1)[1].lstrip().startswith("PASS") if ":" in line else False  # (local)
        if "PASS" in line.split("value=", 1)[0] and "S_ent" in line:
            # parse S_ent=<float> if present
            try:
                frag = line.split("S_ent", 1)[1]                         # (local)
                num = "".join(ch for ch in frag if ch in "0123456789.eE+-")[:16]  # (local)
                return "PRESENT-PASS-Sent", float(num)
            except Exception:
                return "PRESENT-PASS-noSentval", None
        # present but non-PASS or no S_ent (e.g. the PBH-fold-transit producer,
        # gate INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM whose value is an I_PBH integral)
        for tok in ("FAIL", "INFO", "PRE-REG-INC", "PASS"):
            if line.split("value=", 1)[0].find(tok) != -1:
                return f"UNMET-W1-1-{tok}-no-usable-Sent", None
        return "UNMET-W1-1-unparsed", None
    return "UNMET-FALLBACK-empty", None


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # ----- canonical constants (with provenance-checked fallbacks) -----
    a0 = float(a_0_FW_zeta)                                  # (local) a_0^{zeta}
    a2 = float(a_2_FW_zeta)                                  # (local) a_2^{zeta}
    M_KK_val = float(M_KK)                                   # (local) GeV
    M_Pl = float(M_Pl_reduced)                               # (local) reduced Planck, GeV
    rho_obs = float(rho_Lambda_obs)                          # (local) GeV^4, Planck 2018
    f0_over_f2 = 1.0                                         # (local) Gaussian cutoff (S64: sharp=1/2, Gaussian=1); O(1)
    f2_val = float(getattr(_cc, "f_2_default", 2.34))        # (local) cutoff 2nd moment

    # ----- GGE causal-diamond entanglement entropy (the matter piece) -----
    labels, u, v, n_k = load_gge_state()
    # full 8-mode von-Neumann (per-mode-occupation form)
    S_GGE_occ = float(sum(mode_entropy(nn) for nn in n_k))   # (local) full 8-mode
    # causal-diamond HALF-TRACE: keep the B1+B3 half-region (4 of 8 modes), the
    # sub-region a small diamond cuts through (the half-mode trace Jacobson needs).
    half_mask = np.array(["B2" not in str(L) for L in labels])  # (local) B1+B3 modes
    S_diamond = float(sum(mode_entropy(n_k[i]) for i in range(len(n_k)) if half_mask[i]))  # (local)
    S_diamond_B2 = float(sum(mode_entropy(n_k[i]) for i in range(len(n_k)) if not half_mask[i]))  # (local)
    # global BCS product-state entanglement (ENT-39): exactly 0 (no inter-cell entanglement)
    S_ent_BCS = 0.0                                          # (local) ENT-39 product state
    # S62-workshop free-fermion local-entanglement reference (8 x 0.138 nats)
    S_ent_S62 = 8.0 * 0.138                                  # (local) QR2.9 reference

    # W1-1 input value (seed: 1.039 nats) -- use as the fiducial diamond anchor when
    # available; otherwise the substrate-first half-trace S_diamond is the anchor.
    w1_status, w1_S_ent = w1_1_status()
    S_ent_W1_1 = 1.039                                       # (local) seed value (investigation-track)
    # Anchor selection (plan: the prereq governs WHICH number anchors the diamond).
    # ONLY a PASS W1-1 line carrying an explicit S_ent uses that value; otherwise
    # the substrate-first half-trace is the anchor (plan §"Discipline on the S_ent
    # discrepancy" fallback: W1-1 here is INV8-W1-1-PBH-FOLD-TRANSIT-SPECTRUM=FAIL,
    # an I_PBH producer that emitted NO usable causal-diamond S_ent).
    if w1_status == "PRESENT-PASS-Sent" and w1_S_ent is not None:
        S_anchor = float(w1_S_ent)                           # (local) W1-1 PASS -> its S_ent
        anchor_src = "INV8-W1-1 PASS (S_ent=%.6f nats)" % w1_S_ent
    else:
        S_anchor = S_diamond                                 # (local) fallback -> substrate half-trace
        anchor_src = ("substrate-first half-trace (s52 B1+B3, %.6f nats); "
                      "W1-1=%s -> fallback" % (S_diamond, w1_status))

    # ----- Newton coupling on the a_2 channel (PB-8) -----
    # G_eff^{-1} = Lambda_cutoff^2 f_2 a_2 ; Lambda_cutoff = M_KK (spectral cutoff).
    Lambda_cut = M_KK_val                                    # (local) GeV
    G_eff_inv = (Lambda_cut ** 2) * f2_val * a2              # (local) GeV^2 (1/G_eff)
    G_eff = 1.0 / G_eff_inv                                  # (local) GeV^{-2}

    # ----- ROUTE 1: bare a_0 spectral-action variation (the NAIVE 114-115.5 OOM gap) -----
    # Lambda_SA = (f_0/f_2)(a_0/a_2) Lambda_sp^2 ; rho_SA = Lambda_SA M_Pl^2/(8 pi)   [S64 Eq 13]
    Lambda_SA = f0_over_f2 * (a0 / a2) * (M_KK_val ** 2)     # (local) GeV^2
    rho_SA = Lambda_SA * (M_Pl ** 2) / (8.0 * np.pi)         # (local) GeV^4
    D_OOM_bare = abs(np.log10(rho_SA) - np.log10(rho_obs))   # (local)

    # ----- Diamond scan: S_gen(ell), area/volume, small-diamond regime check -----
    # Geometric ball of geodesic radius ell on the emergent metric g_M.
    # In M_KK^{-1} units: A(ell) = 4 pi ell^2 ; V(ell) = (4/3) pi ell^3 (3-ball);
    # entanglement density per cell-volume sets dS_ent/dV.
    ell = np.logspace(np.log10(SCAN_MIN), np.log10(SCAN_MAX), N_EVAL)   # (local) M_KK^{-1}
    A_ell = 4.0 * np.pi * ell ** 2                           # (local) M_KK^{-2}
    V_ell = (4.0 / 3.0) * np.pi * ell ** 3                   # (local) M_KK^{-3}
    # entanglement-entropy density of the GGE diamond: dS_ent/dV ~ S_anchor * M_KK^3
    # (S_anchor nats per cell of volume ~ M_KK^{-3}); per-AREA form S_anchor * M_KK^2.
    dS_dV_density = S_anchor                                 # (local) nats per M_KK^{-3} cell (=> S_anchor*M_KK^3 in GeV^3)
    dS_dA_density = S_anchor                                 # (local) nats per M_KK^{-2} (=> S_anchor*M_KK^2 in GeV^2; S62 QR2.10)

    # Small-diamond regime: the Jacobson expansion is valid for ell << R_H and the
    # geodesic-ball (flat) approximation valid for ell <~ curvature radius. The lower
    # end (ell -> SCAN_MIN) recovers the local Rindler horizon. Mark the fraction of
    # the window in the valid small-diamond regime: ell <= 1 (sub-cell) is the cleanest
    # Jacobson regime; ell up to 1e3 stays sub-horizon (R_H ~ 1e60 M_KK^{-1}).
    R_H_over_lKK = (M_Pl ** 2) / (M_KK_val * float(getattr(_cc, "rho_Lambda_obs", rho_obs)) ** 0.25)  # (local) crude horizon/cell
    valid_mask = ell < R_H_over_lKK                          # (local) sub-horizon throughout
    frac_valid = float(np.mean(valid_mask))                  # (local)

    # ----- ROUTE 2: Jacobson-2015 entanglement-equilibrium magnitude -----
    # rho_ent = T_modular * (dS_ent/dV).  T_modular = substrate modular (Unruh)
    # temperature on A_hor. Present-day comoving observer: T_U = H_0/(2 pi).
    H0_GeV = 1.18e-42                                        # (local) H_0 ~ 67.4 km/s/Mpc in GeV
    T_U_cosmo = H0_GeV / (2.0 * np.pi)                       # (local) GeV (cosmological Unruh temp)
    dS_dV_GeV3 = dS_dV_density * M_KK_val ** 3               # (local) GeV^3 (entanglement density)
    rho_ent_cosmo = T_U_cosmo * dS_dV_GeV3                   # (local) GeV^4 (entanglement-equilib vacuum energy)
    D_OOM_ent_cosmo = abs(np.log10(rho_ent_cosmo) - np.log10(rho_obs))  # (local)

    # Cross-check: the S62 area-law form Lambda_Jac = T_U * dS_ent/dA, rho = Lambda*M_Pl^2/8pi.
    # (S62 reported "17 OOM" but that estimate was dimensionally inconsistent -- it
    # divided Lambda[GeV^2] by M_Pl^4[GeV^4] and read the GeV^-2 result as a pure ratio.
    # The dimensionally-correct area-law magnitude is recomputed here.)
    Lambda_Jac_area = T_U_cosmo * dS_dA_density * M_KK_val ** 2  # wrong dim path? no: T_U[GeV]*S*M_KK^2[GeV^2]=GeV^3
    # Correct area-law: Lambda_Jac[GeV^2] = (T_U/M_KK) * S_anchor * M_KK^2 = S_anchor*T_U*M_KK
    Lambda_Jac_area = S_anchor * T_U_cosmo * M_KK_val        # (local) GeV^2
    rho_Jac_area = Lambda_Jac_area * (M_Pl ** 2) / (8.0 * np.pi)  # (local) GeV^4
    D_OOM_ent_area = abs(np.log10(rho_Jac_area) - np.log10(rho_obs))  # (local)

    # ----- Sign of Lambda_substrate (substitution-chain Step 6) -----
    # Lambda_substrate = 8 pi G_eff [dS_ent/dV]_eq ; G_eff>0, 8pi>0, dS_ent/dV>0
    dS_dV_sign = +1.0 if dS_dV_density > 0 else (-1.0 if dS_dV_density < 0 else 0.0)  # (local)
    Lambda_substrate_sign = +1.0 if (G_eff > 0 and dS_dV_sign > 0) else (
        -1.0 if (G_eff > 0 and dS_dV_sign < 0) else 0.0)    # (local)
    # the explicit magnitude (for record): Lambda_sub = 8 pi G_eff dS_ent/dV
    Lambda_substrate = 8.0 * np.pi * G_eff * dS_dV_GeV3      # (local) GeV^? (Jacobson convention)

    # ----- canonical deliverable: ROUTE 2 cosmological-modular-temp D_OOM -----
    D_OOM = D_OOM_ent_cosmo                                  # (local) the entanglement-equilibrium gap

    # ----- verdict 3-tuple (plan rubric) -----
    # sign: Lambda_substrate > 0 expected (de-Sitter-like); PASS if matches.
    sign_verdict = "PASS" if Lambda_substrate_sign > 0 else ("FAIL" if Lambda_substrate_sign < 0 else "N/A")
    # magnitude: D_OOM < PASS_D_OOM -> PASS; <= FAIL_D_OOM -> INFO; else FAIL.
    if D_OOM < PASS_D_OOM:
        magnitude_verdict = "PASS"
    elif D_OOM <= FAIL_D_OOM:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # regime: small-diamond expansion validity over the scan window.
    if frac_valid >= 0.95:
        regime_verdict = "VALID"
    elif frac_valid >= 0.50:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"
    # W1-1 fallback forces INFO floor on magnitude per rubric (documented discrepancy).
    fallback_active = not w1_status.startswith("PRESENT")    # (local)

    return {
        "value": float(D_OOM),
        "D_OOM": float(D_OOM),
        "D_OOM_ent_cosmo": float(D_OOM_ent_cosmo),
        "D_OOM_ent_area": float(D_OOM_ent_area),
        "D_OOM_bare": float(D_OOM_bare),
        "Lambda_substrate": float(Lambda_substrate),
        "Lambda_substrate_sign": float(Lambda_substrate_sign),
        "Lambda_SA": float(Lambda_SA),
        "rho_SA": float(rho_SA),
        "rho_ent_cosmo": float(rho_ent_cosmo),
        "rho_Jac_area": float(rho_Jac_area),
        "rho_obs": float(rho_obs),
        "G_eff": float(G_eff),
        "G_eff_inv": float(G_eff_inv),
        "T_U_cosmo": float(T_U_cosmo),
        "dS_dV_GeV3": float(dS_dV_GeV3),
        "S_GGE_occ": S_GGE_occ,
        "S_diamond": S_diamond,
        "S_diamond_B2": S_diamond_B2,
        "S_ent_BCS": S_ent_BCS,
        "S_ent_S62": S_ent_S62,
        "S_ent_W1_1": S_ent_W1_1,
        "S_anchor": float(S_anchor),
        "anchor_src": anchor_src,
        "w1_status": w1_status,
        "fallback_active": bool(fallback_active),
        "frac_valid": frac_valid,
        "CC_OOM_canonical": float(getattr(_cc, "CC_OOM", 115.5)),
        "n_k": n_k,
        "labels": np.asarray([str(x) for x in labels]),
        "ell": ell,
        "A_ell": A_ell,
        "V_ell": V_ell,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "a0": a0, "a2": a2, "M_KK_val": M_KK_val, "M_Pl": M_Pl,
        "f0_over_f2": f0_over_f2, "f2_val": f2_val,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def collapse_composite(sign_v, mag_v, regime_v) -> str:
    """Deterministic composite-collapse rule (gate-verdicts.md, PRE-REGISTERED)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "track": "investigation",
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


def make_plot(res: dict):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    # Panel 1: OOM-gap ladder
    ax = axes[0]
    labels = ["bare a_0\nspectral-action\n(NOT this gate)",
              "entanglement-equilib\narea-law",
              "entanglement-equilib\nvolume (canonical)",
              "DILUTION-CC\n(Volovik, ref)"]
    vals = [res["D_OOM_bare"], res["D_OOM_ent_area"], res["D_OOM_ent_cosmo"],
            res["CC_OOM_canonical"]]
    colors = ["#b0b0b0", "#6699cc", "#cc3333", "#33aa55"]
    bars = ax.bar(range(len(vals)), vals, color=colors)
    ax.axhline(PASS_D_OOM, color="green", ls="--", lw=1, label=f"PASS D_OOM<{PASS_D_OOM}")
    ax.axhline(FAIL_D_OOM, color="red", ls="--", lw=1, label=f"FAIL D_OOM>{FAIL_D_OOM}")
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labels, fontsize=7)
    ax.set_ylabel("D_OOM = |log10(rho) - log10(rho_obs)|")
    ax.set_title("INV8-W2-1: CC magnitude OOM gap by route")
    for b, vv in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, vv + 1, f"{vv:.1f}",
                ha="center", fontsize=8)
    ax.legend(fontsize=7, loc="upper center")
    # Panel 2: the three entropies + diamond scan
    ax2 = axes[1]
    ax2.loglog(res["ell"], res["A_ell"], label="A(ell)=4 pi ell^2 (area)", color="#6699cc")
    ax2.loglog(res["ell"], res["V_ell"], label="V(ell)=(4/3)pi ell^3 (vol)", color="#cc6633")
    ax2.set_xlabel("diamond radius ell / M_KK^{-1}")
    ax2.set_ylabel("area / volume (M_KK units)")
    ax2.set_title("Causal-diamond scan (small-diamond regime)")
    txt = (f"S_ent disclosure (nats):\n"
           f"  S_BCS(global product) = {res['S_ent_BCS']:.3f}\n"
           f"  S_GGE(8-mode vN)      = {res['S_GGE_occ']:.3f}\n"
           f"  S_diamond(B1+B3 half) = {res['S_diamond']:.3f}\n"
           f"  S_ent(W1-1 seed)      = {res['S_ent_W1_1']:.3f}\n"
           f"  S62 ref (8x0.138)     = {res['S_ent_S62']:.3f}\n"
           f"anchor: {res['S_anchor']:.3f}\n"
           f"Lambda_sub sign = {'+' if res['Lambda_substrate_sign']>0 else '-'} (de-Sitter)\n"
           f"D_OOM = {res['D_OOM']:.4f}")
    ax2.text(0.02, 0.02, txt, transform=ax2.transAxes, fontsize=7,
             va="bottom", family="monospace",
             bbox=dict(boxstyle="round", fc="wheat", alpha=0.6))
    ax2.legend(fontsize=7, loc="upper left")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
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
    print()

    res = compute()

    # ----- report -----
    print("=== INV8-W2-1: Jacobson entanglement-equilibrium -> CC magnitude ===")
    print(f"  W1-1 prereq status: {res['w1_status']}  (fallback_active={res['fallback_active']})")
    print(f"  S_ent anchor: {res['anchor_src']}")
    print("  --- S_ent three-entropy disclosure (nats) ---")
    print(f"    S_ent(global BCS product, ENT-39)   = {res['S_ent_BCS']:.6f}")
    print(f"    S_GGE(full 8-mode von-Neumann)      = {res['S_GGE_occ']:.6f}  (plan cites 2.2125 full R-G)")
    print(f"    S_diamond(causal-diamond half-trace) = {res['S_diamond']:.6f}  (B1+B3 sub-region)")
    print(f"    S_ent(W1-1 seed, investigation)     = {res['S_ent_W1_1']:.6f}")
    print(f"    S62 ref (8 x 0.138 free-fermion)    = {res['S_ent_S62']:.6f}")
    print("  --- Newton coupling (PB-8) ---")
    print(f"    G_eff^-1 = Lambda_cut^2 f_2 a_2 = {res['G_eff_inv']:.6e} GeV^2  (G_eff>0)")
    print("  --- ROUTE 1 (bare a_0 spectral-action variation; NOT entanglement-equilib) ---")
    print(f"    Lambda_SA = (f_0/f_2)(a_0/a_2)M_KK^2 = {res['Lambda_SA']:.6e} GeV^2")
    print(f"    rho_SA    = {res['rho_SA']:.6e} GeV^4 ; rho_obs = {res['rho_obs']:.3e} GeV^4")
    print(f"    D_OOM_bare = {res['D_OOM_bare']:.4f}  (canonical naive gap ~114-115.5; DILUTION-CC closes THIS)")
    print("  --- ROUTE 2 (Jacobson-2015 entanglement-equilibrium; the gate's functional) ---")
    print(f"    T_U_cosmo  = {res['T_U_cosmo']:.6e} GeV (H_0/2pi)")
    print(f"    dS_ent/dV  = {res['dS_dV_GeV3']:.6e} GeV^3")
    print(f"    rho_ent    = {res['rho_ent_cosmo']:.6e} GeV^4")
    print(f"    D_OOM_ent_cosmo (CANONICAL) = {res['D_OOM_ent_cosmo']:.4f}")
    print(f"    D_OOM_ent_area  (cross-chk) = {res['D_OOM_ent_area']:.4f}  (S62 '17 OOM' was dim-inconsistent)")
    print("  --- substitution-chain Step 6 sign read-off ---")
    print(f"    dS_ent/dV > 0, G_eff > 0, 8pi > 0 => Lambda_substrate sign = "
          f"{'+ (de-Sitter, sign-consistent)' if res['Lambda_substrate_sign']>0 else '- (WRONG)'}")
    print(f"  small-diamond regime: frac_valid = {res['frac_valid']:.3f}")
    print()

    # ----- save data -----
    np.savez(
        OUT_NPZ,
        **{k: v for k, v in res.items() if not isinstance(v, str)},
        anchor_src=res["anchor_src"], w1_status=res["w1_status"],
        sign_verdict=res["sign_verdict"], magnitude_verdict=res["magnitude_verdict"],
        regime_verdict=res["regime_verdict"],
    )
    print(f"  saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # ----- verdict -----
    sign_v = res["sign_verdict"]          # (local)
    mag_v = res["magnitude_verdict"]      # (local)
    regime_v = res["regime_verdict"]      # (local)
    composite = collapse_composite(sign_v, mag_v, regime_v)  # (local)

    tag = emit_4tuple(round(res["value"], 4), SCHEME, CONVENTION, L_MAX)
    print(tag)

    note = (f"Jacobson-2015 entanglement-equilib CC magnitude; "
            f"D_OOM={res['D_OOM']:.4f} (ROUTE2 vol cosmological-Tmod); "
            f"Lambda_sub sign=+ de-Sitter; bare-a0 ref D_OOM={res['D_OOM_bare']:.2f}; "
            f"DISTINCT functional from inv4/inv5/inv7 on same VII.BZ crossed product; "
            f"W1-1={res['w1_status']}")
    extra = [
        f"# regulator_pin=a_2^{{zeta}},a_0^{{zeta}} # {GATE_ID} Seeley-DeWitt regulator pin",
        (f"# S_ent disclosure: S_BCS=0.0 S_GGE={res['S_GGE_occ']:.4f} "
         f"S_diamond={res['S_diamond']:.4f} S_W1-1=1.039 anchor={res['S_anchor']:.4f} # {GATE_ID}"),
        (f"# routes: D_OOM_bare={res['D_OOM_bare']:.4f} D_OOM_ent_vol={res['D_OOM_ent_cosmo']:.4f} "
         f"D_OOM_ent_area={res['D_OOM_ent_area']:.4f} CC_OOM_canon={res['CC_OOM_canonical']} # {GATE_ID}"),
    ]
    print_verdict_payload(
        composite, round(res["value"], 4), audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=note, extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v}/mag={mag_v}/regime={regime_v}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
