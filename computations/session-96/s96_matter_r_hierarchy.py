#!/usr/bin/env python3
"""
S96 W4-6 S96-MATTER-R-HIERARCHY — direct-from-D_K neutrino mass-squared ratio
============================================================================

Gate: S96-MATTER-R-HIERARCHY ([SIGN])

Pre-registered threshold (plan §W4-6):
  operator: R_direct = Delta_m2_32 / Delta_m2_21  (dimensionless, M_KK units)
  PASS iff  R_direct in [30, 38]
  FAIL iff  R_direct outside [17, 66]
  INFO otherwise (R_direct in [17,30) U (38,66])

[SIGN] directional pre-registration (plan §W4-6 Step 4 substitution chain):
  The weak-mixing correction factor
      F = [1 - V23^2/(E3-E2)^2] / [1 + V12^2/(E2-E1)^2]
  satisfies F <= 1 (numerator <= 1, denominator >= 1). Therefore the mixing
  correction MULTIPLIES the bare R DOWNWARD: R = R_0 * F <= R_0. The mixing
  correction moves R the WRONG way (away from the measured 33.8). The SIGN
  verdict tests this F <= 1 directional prediction.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-52/s52_msw_transit.npz   (B1/B2/B3 trajectories + couplings)
  - computations/_shared/canonical_constants.py    (feeds audit_sha256 only)
  - computations/session-96/s96_matter_a4_yukawa_ratio.npz  (OPTIONAL CC2 cross-check; W4-1)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=R_direct, scheme=direct-DK-eigenvalue-spacing-no-seesaw,
   convention=RATIO, L_max=10)

Classification: PARTICLE

METHODOLOGY
-----------
The neutrino mass-squared ratio R = Delta_m2_32/Delta_m2_21 is read DIRECTLY off
the D_K bottom-content lepton triplet (B1,B2,B3) eigenvalues at tau_fold = 0.190
— NO seesaw, NO external right-handed Majorana M_R. The eigenvalues E_B1, E_B2,
E_B3 and the inter-generation couplings V12, V23, V13 are taken from the S52 MSW
transit trajectory cache (TRANSIT-52). Under m_1 = 0 normal ordering, the
neutrino masses are the spacings of the D_K eigenvalues; we form Delta_m2_21,
Delta_m2_32 and the truncation-robust dimensionless ratio R_direct.

The bare zero-mixing ratio R_0 = (E3^2-E2^2)/(E2^2-E1^2) is the S35 analytic
formula's first factor (CC1 verifies this identity). The weak-mixing correction
F (CC1 second factor) is computed and its sign tested (the [SIGN] verdict). The
registry-PROVEN bare R=27.2 (framework-bbn-hypothesis.md) is a DIFFERENT
construction (B2/G1 near-degeneracy at a tuned tau_0, S35) than the B1/B2/B3
spacings at tau_fold computed here; the gate reconciles the two and adjudicates
the bare-PROVEN-tag retirement.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- Matrices are 3x3 (lepton triplet) — CPU is correct; OMP capped at 8 per
  the gate (GPU_path pinned torch.linalg but the operative matrices are 3x3,
  far below the 100x100 GPU threshold; we cross-check the 3x3 eig against a
  closed-form for the bare ratio).
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- [SIGN] trigger => schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row REQUIRED
- R_direct written to the .npz for the downstream W4-7 SEESAW-D5 R-route check
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED_PATH not in sys.path:
    sys.path.insert(0, SHARED_PATH)

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
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

SESSION = "S96"                                                    # (local)
GATE_ID = "S96-MATTER-R-HIERARCHY"                                 # (local)
SCHEME = "direct-DK-eigenvalue-spacing-no-seesaw"                  # (local)
CONVENTION = "RATIO"                                               # (local)
L_MAX = 10                                                         # (local)

# Pre-registered bands (plan §W4-6 operator + strict_PASS_boundary)
PASS_LO = 30.0                                                     # (local)
PASS_HI = 38.0                                                     # (local)
FAIL_LO = 17.0                                                     # (local)
FAIL_HI = 66.0                                                     # (local)

# External comparison anchors (NuFit-6.0 / S35 record — comparison-only, NOT canonical pins)
R_NUFIT = 33.8                                                     # (local) NuFit-6.0 R = Delta_m2_32/Delta_m2_21
R_S35_RECORD = 32.6                                                # (local) S35 record 32.6 +/- 1.4
R_S35_SIGMA = 1.4                                                  # (local)
R_BARE_PROVEN = 27.2                                               # (local) registry-PROVEN bare value (framework-bbn-hypothesis.md)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s96_matter_r_hierarchy.npz"
OUT_PNG = SESSION_DIR / "s96_matter_r_hierarchy.png"
VERDICT_TXT = SESSION_DIR / "s96_gate_verdicts.txt"

MSW_NPZ = COMPUTATIONS_DIR / "session-52" / "s52_msw_transit.npz"
YUK_NPZ = SESSION_DIR / "s96_matter_a4_yukawa_ratio.npz"   # optional CC2

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    MSW_NPZ,
]
if YUK_NPZ.exists():
    INPUT_FILES.append(YUK_NPZ)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


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
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Direct-from-D_K R = Delta_m2_32/Delta_m2_21 (no seesaw), m_1=0 normal ordering."""
    d = np.load(MSW_NPZ)  # (local)

    # Direct D_K bottom-content lepton-triplet eigenvalues at tau_fold (M_KK units)
    E1 = float(d["E1_fold"])   # (local) E_B1 = lambda_{G1}-content lightest
    E2 = float(d["E2_fold"])   # (local) E_B2
    E3 = float(d["E3_fold"])   # (local) E_B3 heaviest
    # Inter-generation couplings (S34 spinor V, M_KK units); V13 = 0 EXACT (NNI)
    V12 = float(d["V_12"])     # (local)
    V23 = float(d["V_23"])     # (local)
    V13 = float(d["V_13"])     # (local)

    # ---- m_1 = 0 normal ordering, direct |lambda_i| spacings (gate-pinned) ----
    # Convention A (gate-natural "direct spacings, m_1=0"): masses are the
    # spacings of the D_K eigenvalues measured from the lightest:
    #   m_1 = 0, m_2 = E2 - E1, m_3 = E3 - E1.
    m1 = 0.0              # (local)
    m2 = E2 - E1          # (local)
    m3 = E3 - E1          # (local)
    dm2_21 = m2**2 - m1**2   # (local)
    dm2_32 = m3**2 - m2**2   # (local)
    R_direct = dm2_32 / dm2_21   # (local) THE gate observable (feeds W4-7)

    # ---- Companion convention readings (reported, not the verdict driver) ----
    # Convention C (eigenvalues taken directly as masses, m_i = E_i): the S52
    # native squared-spacing ratio R = (E3^2-E2^2)/(E2^2-E1^2).
    R_convC = (E3**2 - E2**2) / (E2**2 - E1**2)   # (local)
    # Convention B (m_1=0 but m_2=E2, m_3=E3 directly): unphysical-large dm2_21.
    R_convB = (E3**2 - E2**2) / (E2**2 - 0.0)     # (local)

    # ---- Bare zero-mixing ratio R_0 via the S35 analytic formula FIRST factor ----
    # R_0 = (E3-E2)(E3+E2) / [(E2-E1)(E2+E1)] == R_convC (algebraic identity, CC1).
    R0_formula = ((E3 - E2) * (E3 + E2)) / ((E2 - E1) * (E2 + E1))   # (local)

    # ---- Weak-mixing correction factor F (S35 analytic formula SECOND factor) ----
    F_num = 1.0 - V23**2 / (E3 - E2)**2   # (local)
    F_den = 1.0 + V12**2 / (E2 - E1)**2   # (local)
    F = F_num / F_den                     # (local)
    R_full_mixing = R0_formula * F        # (local) R = R_0 * F

    # ---- [SIGN] directional test: F <= 1 ? (mixing moves R the WRONG way) ----
    F_le_1 = bool(F <= 1.0)   # (local) pre-registered prediction: True

    # ---- 3x3 effective-matrix eig cross-check (CC of the convention-C ratio) ----
    # Build the lepton 3x3 real-symmetric effective Dirac sub-matrix with the
    # direct eigenvalues on the diagonal and V_ij off-diagonal; diagonalize and
    # form the squared-eigenvalue ratio to cross-check R_convC under mixing.
    M = np.array([[E1,  V12, V13],
                  [V12, E2,  V23],
                  [V13, V23, E3 ]], dtype=np.float64)   # (local)
    w = np.linalg.eigvalsh(M)   # (local) ascending
    w = np.sort(np.abs(w))      # (local) ascending |eig| -> mass ordering
    R_eig_mixed = (w[2]**2 - w[1]**2) / (w[1]**2 - w[0]**2)   # (local) full-mixing squared-ratio (m_i=eig)
    # small-matrix numpy cross-check is fine (3x3); torch not needed below 100x100

    # ---- CC1: S35 analytic-formula bare identity residual (RATIO 0.5% rubric) ----
    cc1_ratio = abs(R0_formula - R_convC) / R_convC if R_convC != 0 else float("inf")  # (local)
    cc1_pass = bool(cc1_ratio < 0.005)   # (local) 0.5% RATIO tolerance

    # ---- CC2 (optional): W4-1 R_Yuk cross-check if landed ----
    cc2_present = False   # (local)
    R_yuk = float("nan")  # (local)
    if YUK_NPZ.exists():
        try:
            dy = np.load(YUK_NPZ)   # (local)
            for key in ("R_Yuk", "R_yuk", "value", "R_direct"):
                if key in dy.files:
                    R_yuk = float(dy[key]); cc2_present = True; break
        except Exception:
            cc2_present = False

    return {
        "value": R_direct,
        "E1": E1, "E2": E2, "E3": E3,
        "V12": V12, "V23": V23, "V13": V13,
        "m1": m1, "m2": m2, "m3": m3,
        "dm2_21": dm2_21, "dm2_32": dm2_32,
        "R_direct": R_direct,
        "R_convC": R_convC, "R_convB": R_convB,
        "R0_formula": R0_formula,
        "F_num": F_num, "F_den": F_den, "F": F,
        "R_full_mixing": R_full_mixing,
        "F_le_1": F_le_1,
        "R_eig_mixed": R_eig_mixed,
        "cc1_ratio": cc1_ratio, "cc1_pass": cc1_pass,
        "cc2_present": cc2_present, "R_yuk": R_yuk,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(R_direct: float) -> str:
    """PASS iff R in [30,38]; FAIL iff outside [17,66]; INFO otherwise."""
    if PASS_LO <= R_direct <= PASS_HI:
        return "PASS"
    if R_direct < FAIL_LO or R_direct > FAIL_HI:
        return "FAIL"
    return "INFO"


def three_tuple_verdicts(res: dict, composite: str) -> tuple[str, str, str]:
    """SIGN/MAGNITUDE/REGIME 3-tuple per gate-verdicts.md schema-v2.

    sign_verdict   : direction of the mixing correction. Pre-registered Step-4
                     prediction is F <= 1 (mixing DECREASES R). PASS iff F<=1.
    magnitude_verdict: |R_direct - 33.8| vs PASS-band / INFO-band. PASS-band is
                     the [30,38] membership (=> |R-34|<=4 roughly); we key the
                     magnitude verdict on band membership against R_NUFIT.
    regime_verdict : the weak-mixing perturbative formula validity. VALID iff
                     V_ij << dE_ij throughout (the formula's regime). Here we
                     report MARGINAL/BREAKDOWN if the perturbative expansion
                     parameter exceeds the pre-registered thresholds.
    """
    # SIGN: F <= 1 prediction
    sign = "PASS" if res["F_le_1"] else "FAIL"   # (local)

    # MAGNITUDE: band membership of R_direct against the NuFit target
    if PASS_LO <= res["R_direct"] <= PASS_HI:
        mag = "PASS"   # (local)
    elif FAIL_LO <= res["R_direct"] <= FAIL_HI:
        mag = "INFO"   # (local)
    else:
        mag = "FAIL"   # (local)

    # REGIME: weak-mixing perturbative-expansion validity.
    # expansion parameters x12 = V12^2/(E2-E1)^2, x23 = V23^2/(E3-E2)^2.
    x12 = res["V12"]**2 / (res["E2"] - res["E1"])**2   # (local)
    x23 = res["V23"]**2 / (res["E3"] - res["E2"])**2   # (local)
    x_max = max(x12, x23)   # (local)
    # The S35 formula is a weak-mixing (V_ij << dE_ij) expansion; x_max << 1 is
    # the regime of validity. x12 = 0.077^2/0.0161^2 ~ 22.7 >> 1 => the B1-B2
    # gap is NARROW relative to its coupling => the perturbative formula is OUT
    # of its regime for the 12 sector. Report BREAKDOWN when x_max > 1 over the
    # whole single-point window (breach fraction = 100% > 50%).
    if x_max <= 0.25:
        regime = "VALID"      # (local)
    elif x_max <= 1.0:
        regime = "MARGINAL"   # (local)
    else:
        regime = "BREAKDOWN"  # (local)
    return sign, mag, regime


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Append the canonical verdict line (atomic single open('a') write)."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def append_companion_rows(audit_sha: str, content_sha: str,
                          sign: str, mag: str, regime: str) -> None:
    """Append dual-SHA companion row + schema-v2 3-tuple row (atomic appends)."""
    dual = (f"# audit_sha256_short={audit_sha[:16]} "
            f"content_sha256_short={content_sha[:16]} "
            f"# {GATE_ID} dual-SHA companion row\n")
    tuple_row = (f"# sign_verdict={sign} magnitude_verdict={mag} "
                 f"regime_verdict={regime} "
                 f"# {GATE_ID} 3-tuple annotation (schema-v2)\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(dual)
        fp.write(tuple_row)


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Panel 1: R across conventions vs PASS/FAIL bands and anchors
    convs = ["A: m1=0\nspacing\n(gate)", "C: m_i=E_i\n(S52 native)",
             "R_0*F\n(mixing)", "eig\n(3x3 mixed)"]   # (local)
    vals = [res["R_direct"], res["R_convC"], res["R_full_mixing"], res["R_eig_mixed"]]  # (local)
    xpos = np.arange(len(convs))   # (local)
    bars = ax1.bar(xpos, vals, color=["#c0392b", "#e67e22", "#7f8c8d", "#95a5a6"])
    ax1.axhspan(PASS_LO, PASS_HI, color="green", alpha=0.18, label="PASS [30,38]")
    ax1.axhspan(FAIL_LO, PASS_LO, color="gold", alpha=0.12)
    ax1.axhspan(PASS_HI, FAIL_HI, color="gold", alpha=0.12, label="INFO band")
    ax1.axhline(R_NUFIT, color="blue", ls="--", lw=1.5, label=f"NuFit R={R_NUFIT}")
    ax1.axhline(R_BARE_PROVEN, color="purple", ls=":", lw=1.5, label=f"bare PROVEN R={R_BARE_PROVEN}")
    ax1.set_xticks(xpos); ax1.set_xticklabels(convs, fontsize=8)
    ax1.set_ylabel("R = Delta_m2_32 / Delta_m2_21")
    ax1.set_title(f"S96 W4-6: direct-from-D_K R  (R_direct = {res['R_direct']:.4g})")
    ax1.legend(fontsize=7, loc="upper left")
    ax1.set_yscale("log")
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width()/2, v*1.05, f"{v:.3g}",
                 ha="center", va="bottom", fontsize=8)

    # Panel 2: the F<=1 [SIGN] decomposition
    comp = ["R_0\n(bare)", "F_num\n(<=1)", "1/F_den\n(<=1)", "R_0*F\n(result)"]  # (local)
    cv = [res["R0_formula"], res["F_num"], 1.0/res["F_den"], res["R_full_mixing"]]  # (local)
    ax2.bar(np.arange(len(comp)), cv, color=["#e67e22", "#2980b9", "#2980b9", "#7f8c8d"])
    ax2.axhline(1.0, color="k", ls="--", lw=1, alpha=0.6)
    ax2.set_xticks(np.arange(len(comp))); ax2.set_xticklabels(comp, fontsize=8)
    ax2.set_ylabel("factor value")
    ax2.set_title(f"[SIGN] F = {res['F']:.4g} <= 1  (mixing DECREASES R)")
    ax2.set_yscale("log")

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)   # (local)
    script_path = Path(__file__).resolve()   # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"   # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()   # (local)
    value = res["value"]   # (local)
    verdict = evaluate_gate(value)   # (local)

    # 3-tuple (schema-v2) — recompute composite via the pre-registered collapse rule
    sign, mag, regime = three_tuple_verdicts(res, verdict)   # (local)
    # Composite-collapse rule (gate-verdicts.md schema-v2):
    if regime == "BREAKDOWN":
        composite = "FAIL"        # (local)
    elif sign == "FAIL":
        composite = "FAIL"        # (local)
    elif mag == "FAIL" and regime == "VALID":
        composite = "FAIL"        # (local)
    elif mag == "FAIL" and regime == "MARGINAL":
        composite = "INFO"        # (local)
    elif mag == "INFO":
        composite = "INFO"        # (local)
    else:
        composite = "PASS"        # (local)

    # The band-verdict (evaluate_gate) and the composite-collapse must agree on
    # the top-line. The band rule is the primary pre-registered operator; the
    # 3-tuple regime BREAKDOWN can only make a band-PASS more conservative, not
    # less. Reconcile: top-line is the MORE CONSERVATIVE of the two.
    rank = {"PASS": 0, "INFO": 1, "FAIL": 2}   # (local)
    top = verdict if rank[verdict] >= rank[composite] else composite   # (local)

    print("=== RESULTS ===")
    print(f"  E_B1 = {res['E1']:.8f}  E_B2 = {res['E2']:.8f}  E_B3 = {res['E3']:.8f}  (M_KK units)")
    print(f"  V12 = {res['V12']:.4f}  V23 = {res['V23']:.4f}  V13 = {res['V13']:.4f}  (V13=0 EXACT, NNI)")
    print(f"  m_1=0 normal ordering: m2 = {res['m2']:.6f}  m3 = {res['m3']:.6f}")
    print(f"  Delta_m2_21 = {res['dm2_21']:.8e}  Delta_m2_32 = {res['dm2_32']:.8e}")
    print(f"  R_direct (gate, conv A) = {res['R_direct']:.4f}")
    print(f"  R_convC (m_i=E_i)       = {res['R_convC']:.4f}")
    print(f"  R_0 (S35 bare formula)  = {res['R0_formula']:.4f}")
    print(f"  F = [1-V23^2/dE23^2]/[1+V12^2/dE12^2] = {res['F']:.6f}  (F<=1 ? {res['F_le_1']})")
    print(f"  R_0 * F (weak-mixing)   = {res['R_full_mixing']:.6f}")
    print(f"  R_eig_mixed (3x3)       = {res['R_eig_mixed']:.4f}")
    print(f"  CC1 |R0_formula-R_convC|/R_convC = {res['cc1_ratio']:.2e}  (0.5% RATIO PASS={res['cc1_pass']})")
    print(f"  CC2 W4-1 R_Yuk present? {res['cc2_present']}  R_Yuk={res['R_yuk']}")
    print(f"  PASS-band [30,38]: {PASS_LO}<=R<={PASS_HI};  FAIL outside [17,66]")
    print(f"  band-verdict={verdict}  3-tuple=(sign={sign},mag={mag},regime={regime})  composite={composite}")
    print(f"  TOP-LINE (more conservative) = {top}")
    print()

    # Save .npz (R_direct consumed by downstream W4-7 SEESAW-D5)
    np.savez(
        OUT_NPZ,
        R_direct=res["R_direct"],
        R_convC=res["R_convC"], R_convB=res["R_convB"],
        R0_formula=res["R0_formula"],
        F=res["F"], F_num=res["F_num"], F_den=res["F_den"],
        F_le_1=res["F_le_1"],
        R_full_mixing=res["R_full_mixing"],
        R_eig_mixed=res["R_eig_mixed"],
        E1=res["E1"], E2=res["E2"], E3=res["E3"],
        V12=res["V12"], V23=res["V23"], V13=res["V13"],
        m1=res["m1"], m2=res["m2"], m3=res["m3"],
        dm2_21=res["dm2_21"], dm2_32=res["dm2_32"],
        cc1_ratio=res["cc1_ratio"], cc1_pass=res["cc1_pass"],
        R_NUFIT=R_NUFIT, R_BARE_PROVEN=R_BARE_PROVEN,
        PASS_LO=PASS_LO, PASS_HI=PASS_HI, FAIL_LO=FAIL_LO, FAIL_HI=FAIL_HI,
        verdict=top, sign=sign, magnitude=mag, regime=regime,
    )
    make_plot(res)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)   # (local)
    print(tag)
    append_verdict(top, value, audit_sha, content_sha)
    append_companion_rows(audit_sha, content_sha, sign, mag, regime)

    wall = time.time() - t0   # (local)
    print(f"\n=== {GATE_ID}: {top} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
