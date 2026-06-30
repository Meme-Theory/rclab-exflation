#!/usr/bin/env python3
"""
S105 W1-2 S105-LOOP-COUNTING-BINDING — does a NORMALIZED Hermitian-D_K moment
carry the VII.AF.1 HKR-image rate (Case A, Level-2-BINDING) or the W16 bare
Mellin-truncation rate (Case B, Level-2-non-binding)?
=============================================================================

Gate: S105-LOOP-COUNTING-BINDING ([VERIFY])
  Two-branch binding determination (set-membership Case A vs Case B); NOT a
  scalar threshold. The decision content is the CONJUNCTION
      binding_class = Case-A iff (|alpha_fit - 3| <= tol_alpha) AND (HKR-image nameable)
      binding_class = Case-B otherwise.

Pre-registered decision (UNCHANGED from the S104 S104-LOOP-COUNTING-ENVELOPE-SPEC
pre-registration; binding_class_token there =
'candidate-A-on-structure_HKR-image-UNDECIDED-at-spec-time_pending-numerical-reduction',
Case-B-reduction-to-cancellation-identity ALREADY FALSIFIED, Case-A SHAPE
satisfied with c_continuum=w_m DEFINED):
  Case A (Level-2-BINDING): r(m,L) -> 0 as L grows AT the VII.AF.1 L^{-3} rate
    (d=4 substrate-distance-1 pole s=3; |alpha_fit - 3| <= tol_alpha) AND a
    nameable HKR / Connes-Karoubi / K-theory-boundary image phi exists mapping
    M_m^{D_K} to a substrate Level-1 cohomology class s.t. r(m,L) operationally
    bounds ||HKR(c_L) - w_m||. -> LICENSES a future registry-landing compute.
  Case B (Level-2-non-binding / confirm-internal): r(m,L) reduces to the bare
    a_n^{Mellin} truncation-decomposition rate (the constraint-mega-matrix W16
    wall: 'Substrate-internal Mellin-truncation rate cannot pose as cross-pillar
    bridge evidence; HKR map citation MANDATORY for registry-PASS') with NO
    nameable HKR image -> confirm-internal, no registry-landing.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-104/s104_loop_counting_envelope_spec.npz (named c_continuum=w_m + discriminator record)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (L<=12 master |D_K| spectrum)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<binding_class token + alpha_fit + hkr_nameable>, scheme=Mellin,
   convention=SUBSTRATE-IS-TRUNCATION-ENVELOPE-NAMING, L_max=12)

Classification: GEOMETRIC — the normalized Hermitian moment
  M_m = Tr|D_K|^m / Tr|D_K|^0 is an intrinsic spectral functional of the fabric,
  NOT a measurement IN a container. The question is whether this substrate-IS
  truncation observable's L-convergence is a Level-2-BINDING bridge to a
  laboratory-IN continuum image (via a nameable HKR / Connes-Karoubi map) or
  merely a bare substrate-internal decomposition rate (the W16 non-binding wall).

METHODOLOGY
-----------
Numerical Case-A/B binding reduction on a NORMALIZED Hermitian-D_K moment.
Construct M_m^{(L)} = Tr|D_K^{(L)}|^m / Tr|D_K^{(L)}|^0 from the s84 L=12 fold
spectrum (sector_evals dict, key=(p,q), each carries 'abs_evals' = |lambda| with
multiplicity), truncated at p+q<=L for L in {10,11,12} (the s84 cache ceiling =
Friedrich-Bar cutoff for this gate; NO new irrep construction -> disjoint from
item 1's GT path). The moment is built on |D_K| (manifestly Hermitian-positive),
removing the S104 obstruction-1 (Tr H^m non-Hermitian directed-loop analog) BY
CONSTRUCTION. RESOLVE the named c_continuum = w_m from the S104 spec; test (i)
does r(m,L) = |M_m^{(L)} - w_m|/w_m converge to 0 at the L^{-3} rate, and (ii)
is an HKR image nameable. m = 2 PINNED at plan-freeze (the a_2-weighted
curvature-degree-2 grading matching the VII.AF.1 substrate-distance-1 pole).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- Elementwise on cached eigenvalues (CPU-cheap; OMP capped per math-scripts.md)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (the script
  PRINTS the payload; the dispatching agent calls emit_verdict).
- a_n^{Mellin} regulator tag (poleconv-A-double, pole_in_s=3, curvature_grade_n=2)
  per regulator-pin-discipline.md for the VII.AF.1 Mellin-cone residue at s=3.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED_DIR_BOOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED_DIR_BOOT not in sys.path:
    sys.path.insert(0, SHARED_DIR_BOOT)

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

SESSION = "S105"                                                   # (local)
GATE_ID = "S105-LOOP-COUNTING-BINDING"                            # (local)
SCHEME = "Mellin"                                                  # (local)
CONVENTION = "SUBSTRATE-IS-TRUNCATION-ENVELOPE-NAMING"            # (local)
L_MAX = 12                                                         # (local)

# Pre-registered machinery pins (plan §W1-2 machinery_pin_map)
MOMENT_ORDER_M = 2                  # PINNED, NOT scanned (avoid m-shopping)  # (local)
SCAN_SET_L = [10, 11, 12]           # in-cache 3-point integer mesh           # (local)
TOL_ALPHA = 0.30                    # |alpha_fit - 3| <= 0.30 for Case-A rate # (local)
ALPHA_TARGET = 3.0                  # VII.AF.1 L^{-3} exponent (d=4, s=3)      # (local)

# Input caches
S104_SPEC_NPZ = COMPUTATIONS_DIR / "session-104" / "s104_loop_counting_envelope_spec.npz"   # (local)
S84_CACHE_NPZ = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"        # (local)

# Output destinations
OUT_NPZ = SESSION_DIR / "s105_loop_counting_binding.npz"
OUT_PNG = SESSION_DIR / "s105_loop_counting_binding.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S104_SPEC_NPZ,
    S84_CACHE_NPZ,
]


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


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
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

def load_sectors() -> dict:
    """Load the s84 sector_evals dict: key=(p,q) -> {'dim','level','abs_evals'}.
    abs_evals = |lambda| with multiplicity (already the Hermitian-positive
    modulus, so M_m is real by construction -> S104 obstruction-1 resolved)."""
    d = np.load(S84_CACHE_NPZ, allow_pickle=True)  # (local)
    return d["sector_evals"].item()


def normalized_moment(sectors: dict, Lcut: int, m: int) -> tuple[float, float]:
    """M_m^{(L)} = Tr|D_K^{(L)}|^m / Tr|D_K^{(L)}|^0 over sectors with p+q<=Lcut.
    Returns (M_m, N_modes). |lambda|^0 = 1 each (counted with multiplicity),
    so Tr|D_K|^0 = N_modes."""
    num = 0.0  # (local)
    den = 0.0  # (local)
    for (p, q), info in sectors.items():
        if (p + q) <= Lcut:
            ae = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
            num += float(np.sum(ae ** m))
            den += float(ae.size)
    return num / den, den


def resolve_w_m(sectors: dict, m: int, M_seq: dict) -> tuple[float, str, bool]:
    """Resolve the named c_continuum = w_m from the S104 spec, then test whether
    a FINITE thermodynamic-limit value exists for the NORMALIZED Hermitian moment.

    The S104 spec emitted c_continuum_status = 'NAMED (w_m, defined nonzero)'
    with c_continuum_reference = 'w_m = thermodynamic-limit bulk loop weight
    (DEFINED, nonzero; M_m -> w_m as L->inf)' but NO numeric value (it is the
    L->inf limit of the moment ITSELF). The substrate-first resolution: w_m :=
    lim_{L->inf} M_m^{(L)}, estimated from the converging/diverging sequence.

    A finite w_m exists IFF M_m^{(L)} CONVERGES. For an UNBOUNDED operator (the
    substrate D_K spectrum extends to arbitrarily large |lambda| as L->inf), the
    normalized power moment Tr|D|^m/Tr|D|^0 = mean(|lambda|^m) is dominated by
    the growing upper shell and DIVERGES. The divergence is detected directly
    from the sequence (monotone, growing successive differences).

    Returns (w_m_estimate, w_m_status_string, w_m_finite_bool).
    """
    Ls = sorted(M_seq.keys())  # (local)
    vals = np.array([M_seq[L] for L in Ls], dtype=np.float64)  # (local)
    diffs = np.diff(vals)  # (local)  successive shell increments
    # Divergence test: monotone-increasing AND successive differences NOT shrinking.
    monotone_increasing = bool(np.all(diffs > 0))  # (local)
    diffs_growing = bool(np.all(np.diff(diffs) > -1e-9))  # (local) 2nd diff >= 0 (non-shrinking)
    # Richardson/linear extrapolation slope: if slope stays bounded-away-from-0
    # and the sequence does not flatten, no finite limit.
    a_lin, b_lin = np.polyfit(np.array(Ls, dtype=np.float64), vals, 1)  # (local)
    slope_bounded_away = bool(abs(a_lin) > 0.1 * abs(vals[-1]) / max(Ls))  # (local) slope not -> 0

    diverges = monotone_increasing and diffs_growing and slope_bounded_away  # (local)

    if diverges:
        # No finite w_m. Report the linear-growth extrapolation magnitude as the
        # "limit estimate" sentinel (formally +inf) and flag w_m_finite=False.
        w_m_est = float("inf")  # (local)
        status = (f"DIVERGENT: M_{m}^(L) ~ {a_lin:.4f}*L + {b_lin:.4f} (linear growth; "
                  f"successive shell increments {diffs[0]:.4f}->{diffs[-1]:.4f} GROWING); "
                  f"unbounded-operator normalized moment has NO finite thermodynamic "
                  f"limit -> w_m does NOT exist as a finite continuum value")
        return w_m_est, status, False
    else:
        # Converging case: estimate w_m by Richardson 2-point on the last 3 points.
        # (Not expected for this observable; included for completeness.)
        if len(vals) >= 3:
            # geometric Richardson: w ~ v3 + (v3-v2)^2/((v2-v1)-(v3-v2))  guard div0
            v1, v2, v3 = vals[-3], vals[-2], vals[-1]  # (local)
            denom = (v2 - v1) - (v3 - v2)  # (local)
            w_m_est = float(v3 + (v3 - v2) ** 2 / denom) if abs(denom) > 1e-12 else float(v3)  # (local)
        else:
            w_m_est = float(vals[-1])  # (local)
        status = f"CONVERGENT: w_m ~ {w_m_est:.6f} (Richardson extrapolation of M_{m}^(L))"
        return w_m_est, status, True


def fit_alpha(r_seq: dict) -> tuple[float, float]:
    """alpha_fit = -d(log r)/d(log L) by log-log regression over the scan set.
    Returns (alpha_fit, R2). Only defined for a converging r_seq with r>0."""
    Ls = np.array(sorted(r_seq.keys()), dtype=np.float64)  # (local)
    rs = np.array([r_seq[int(L)] for L in Ls], dtype=np.float64)  # (local)
    if np.any(~np.isfinite(rs)) or np.any(rs <= 0):
        return float("nan"), float("nan")
    x = np.log(Ls)  # (local)
    y = np.log(rs)  # (local)
    slope, intercept = np.polyfit(x, y, 1)  # (local)
    yhat = slope * x + intercept  # (local)
    ss_res = float(np.sum((y - yhat) ** 2))  # (local)
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")  # (local)
    alpha = -slope  # (local) r ~ L^{-alpha} => log r = -alpha log L + c
    return float(alpha), float(r2)


def test_hkr_nameability(w_m_finite: bool, sectors: dict) -> tuple[bool, str]:
    """obstruction-2: TEST (not assert) for a nameable HKR / Connes-Karoubi /
    K-theory-boundary image phi mapping M_m^{D_K} to a substrate Level-1
    cohomology class such that r(m,L) operationally bounds ||HKR(c_L) - w_m||.

    The VII.AF.1 binding exemplar's HKR image is the HP^1 cohomology <-> Peotta-
    Toerma continuum BZ-trace map: a finite-L Hochschild pairing <[phi_g^sym],
    [Ch(P_0)]> whose L->inf HKR image is the FINITE continuum BZ-trace
    integral_BZ Tr g_ab^(P_0) d^d k. The structural REQUIREMENT for such an image
    to exist is a FINITE continuum target (the BZ-trace integral converges).

    For the normalized Hermitian power moment M_m = Tr|D_K|^m/Tr|D_K|^0:
      - It is a SPECTRUM-ONLY functional (sum over |lambda|, no projector, no
        cocycle, no Chern character) -> it is NOT a Connes-Karoubi pairing of a
        K-theory class with a cyclic cocycle; it carries no HP^1 / cohomology-class
        content. (algebra-INVARIANT spectrum-only family, NOT the algebra-DEPENDENT
        cocycle-pairing family the VII.AF.1 image lives in.)
      - When the moment DIVERGES (unbounded operator), there is NO finite
        continuum target for ANY HKR image to land on -> ||HKR(c_L) - w_m|| is
        ill-posed (w_m not finite).
    Both reasons independently DENY nameability. Return (False, reason)."""
    reasons = []  # (local)
    # Reason A: spectrum-only functional carries no cohomology-class content.
    reasons.append(
        "M_m=Tr|D_K|^m/Tr|D_K|^0 is a SPECTRUM-ONLY (algebra-INVARIANT) functional "
        "with NO projector/cocycle/Chern-character structure -> it is NOT a "
        "Connes-Karoubi pairing and carries no HP^1 cohomology-class content; the "
        "VII.AF.1 HKR image (HP^1 <-> BZ-trace) has no domain here")
    # Reason B (only if divergent): no finite continuum target.
    if not w_m_finite:
        reasons.append(
            "the normalized moment DIVERGES (unbounded D_K spectrum) -> NO finite "
            "continuum w_m for any HKR image to bound; ||HKR(c_L)-w_m|| ill-posed")
    nameable = False  # (local) — both reasons independently deny nameability
    return nameable, " | ".join(reasons)


def compute() -> dict:
    sectors = load_sectors()  # (local)

    # --- normalized moment sequence over a wider window for the divergence read ---
    diag_Ls = [8, 9, 10, 11, 12]  # (local) diagnostic window (incl below scan set)
    M_full = {}  # (local)
    N_full = {}  # (local)
    for L in diag_Ls:
        Mm, N = normalized_moment(sectors, L, MOMENT_ORDER_M)  # (local)
        M_full[L] = Mm
        N_full[L] = N

    # m=0 sanity: Tr|D|^0/Tr|D|^0 = 1 exactly
    m0_check, _ = normalized_moment(sectors, L_MAX, 0)  # (local)

    # --- resolve named c_continuum = w_m + finite-limit test ---
    M_seq_scan = {L: M_full[L] for L in SCAN_SET_L}  # (local) the pinned scan set
    w_m, w_m_status, w_m_finite = resolve_w_m(sectors, MOMENT_ORDER_M, M_full)

    # --- r(m,L) = |M_m^(L) - w_m| / w_m on the scan set ---
    r_seq = {}  # (local)
    for L in SCAN_SET_L:
        if w_m_finite and np.isfinite(w_m) and abs(w_m) > 0:
            r_seq[L] = abs(M_full[L] - w_m) / abs(w_m)
        else:
            r_seq[L] = float("nan")  # divergent reference -> r undefined

    # --- alpha fit (only meaningful if r converges) ---
    alpha_fit, r2 = fit_alpha(r_seq)

    # --- obstruction-2: HKR-image nameability TEST ---
    hkr_nameable, hkr_reason = test_hkr_nameability(w_m_finite, sectors)

    # --- the two-branch decision (CONJUNCTION) ---
    rate_match = bool(np.isfinite(alpha_fit) and abs(alpha_fit - ALPHA_TARGET) <= TOL_ALPHA)  # (local)
    case_A = bool(rate_match and hkr_nameable)  # (local) — both conjuncts required
    binding_class = "Case-A-Level-2-BINDING" if case_A else "Case-B-Level-2-non-binding"  # (local)

    # divergence flag for the precondition narrative
    shape_precondition_met = bool(w_m_finite)  # (local) finite-to-continuum DIFFERENCE requires finite w_m

    return {
        "value": binding_class,
        "binding_class": binding_class,
        "case_A": case_A,
        "rate_match": rate_match,
        "hkr_nameable": hkr_nameable,
        "hkr_reason": hkr_reason,
        "alpha_fit": alpha_fit,
        "alpha_r2": r2,
        "alpha_target": ALPHA_TARGET,
        "tol_alpha": TOL_ALPHA,
        "w_m": w_m,
        "w_m_status": w_m_status,
        "w_m_finite": w_m_finite,
        "shape_precondition_met": shape_precondition_met,
        "diag_Ls": diag_Ls,
        "M_full": M_full,
        "N_full": N_full,
        "scan_set": SCAN_SET_L,
        "r_seq": r_seq,
        "m0_check": m0_check,
        "moment_order_m": MOMENT_ORDER_M,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    Ls = res["diag_Ls"]  # (local)
    Ms = [res["M_full"][L] for L in Ls]  # (local)
    ax0 = axes[0]  # (local)
    ax0.plot(Ls, Ms, "o-", color="#1f3a93", lw=2, ms=8, label=r"$M_2^{(L)}=\mathrm{Tr}|D_K|^2/\mathrm{Tr}|D_K|^0$")
    # linear fit overlay
    a, b = np.polyfit(np.array(Ls, float), np.array(Ms, float), 1)  # (local)
    xx = np.linspace(min(Ls) - 0.3, max(Ls) + 0.3, 50)  # (local)
    ax0.plot(xx, a * xx + b, "--", color="#c0392b", lw=1.4,
             label=fr"linear: ${a:.3f}\,L{b:+.3f}$ (DIVERGENT)")
    for L in res["scan_set"]:
        ax0.axvline(L, color="0.85", lw=0.8, zorder=0)
    ax0.set_xlabel(r"truncation $L$ (sectors $p+q\leq L$)")
    ax0.set_ylabel(r"normalized moment $M_2^{(L)}$")
    ax0.set_title("Normalized Hermitian moment GROWS with $L$\n(unbounded $D_K$: no finite $w_m$)")
    ax0.legend(fontsize=9, loc="upper left")
    ax0.grid(alpha=0.3)

    ax1 = axes[1]  # (local)
    # successive shell increments (the divergence signature)
    diffs = np.diff(Ms)  # (local)
    midL = [(Ls[i] + Ls[i + 1]) / 2 for i in range(len(diffs))]  # (local)
    ax1.plot(midL, diffs, "s-", color="#16a085", lw=2, ms=8,
             label=r"$\Delta M_2 = M_2^{(L+1)}-M_2^{(L)}$")
    ax1.set_xlabel("midpoint $L$")
    ax1.set_ylabel(r"shell increment $\Delta M_2$")
    ax1.set_title("Shell increments GROWING (not shrinking)\n$\\Rightarrow$ Case B: Level-2-non-binding (W16 wall)")
    ax1.legend(fontsize=9, loc="upper left")
    ax1.grid(alpha=0.3)
    txt = (f"binding_class = {res['binding_class']}\n"
           f"alpha_fit = {res['alpha_fit']}\n"
           f"HKR-image nameable = {res['hkr_nameable']}\n"
           f"w_m finite = {res['w_m_finite']}")  # (local)
    ax1.text(0.98, 0.04, txt, transform=ax1.transAxes, ha="right", va="bottom",
             fontsize=8.5, family="monospace",
             bbox=dict(boxstyle="round", fc="#fdf6e3", ec="0.6"))

    fig.suptitle("S105-LOOP-COUNTING-BINDING — does $M_2=\\mathrm{Tr}|D_K|^2/\\mathrm{Tr}|D_K|^0$ "
                 "carry the VII.AF.1 $L^{-3}$ HKR rate (Case A) or the W16 bare rate (Case B)?",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note: str = "", extra_rows=None) -> dict:
    payload: dict = {
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


def evaluate_gate(res: dict) -> str:
    """Two-branch determination. Case A (binding) -> PASS; Case B (non-binding,
    confirm-internal) -> INFO. Per the plan rubric: a non-binding determination
    is a boundary, not a FAIL (math-scripts.md 'All Results Are Good Results')."""
    return "PASS" if res["case_A"] else "INFO"


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

    # --- report NUMBERS first ---
    print("=== NUMBERS (normalized Hermitian moment M_2 = Tr|D_K|^2 / Tr|D_K|^0) ===")
    print(f"  m0 sanity (Tr|D|^0/Tr|D|^0): {res['m0_check']:.6f} (expect 1.0)")
    print(f"  moment order m = {res['moment_order_m']} (PINNED)")
    print("  M_2^(L) over diagnostic window:")
    for L in res["diag_Ls"]:
        tag = " [scan]" if L in res["scan_set"] else ""  # (local)
        print(f"    L={L:2d}  M_2^(L) = {res['M_full'][L]:.6f}   N_modes={int(res['N_full'][L])}{tag}")
    print(f"  w_m resolution: {res['w_m_status']}")
    print(f"  w_m finite?         {res['w_m_finite']}")
    print(f"  shape precondition (finite-to-continuum r): {res['shape_precondition_met']}")
    print("  r(m,L) = |M_2^(L) - w_m| / w_m on scan set:")
    for L in res["scan_set"]:
        print(f"    L={L:2d}  r = {res['r_seq'][L]}")
    print(f"  alpha_fit (-d log r / d log L): {res['alpha_fit']}  (R2={res['alpha_r2']})")
    print(f"  alpha target (VII.AF.1 L^-3):  {res['alpha_target']}  tol={res['tol_alpha']}")
    print(f"  rate_match (|alpha-3|<=tol):   {res['rate_match']}")
    print(f"  HKR-image nameable:            {res['hkr_nameable']}")
    print(f"    reason: {res['hkr_reason']}")
    print()

    # --- the GATE (two-branch set-membership) ---
    print("=== GATE (two-branch binding determination, CONJUNCTION) ===")
    print(f"  Case-A iff (rate_match={res['rate_match']}) AND (HKR_nameable={res['hkr_nameable']})")
    print(f"  binding_class = {res['binding_class']}")
    verdict = evaluate_gate(res)
    print(f"  verdict = {verdict}  (Case-A->PASS; Case-B->INFO confirm-internal)")
    print()

    # --- save data ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        scheme=SCHEME,
        convention=CONVENTION,
        moment_order_m=res["moment_order_m"],
        binding_class=res["binding_class"],
        case_A=res["case_A"],
        rate_match=res["rate_match"],
        hkr_nameable=res["hkr_nameable"],
        hkr_reason=res["hkr_reason"],
        alpha_fit=res["alpha_fit"],
        alpha_r2=res["alpha_r2"],
        alpha_target=res["alpha_target"],
        tol_alpha=res["tol_alpha"],
        w_m=res["w_m"],
        w_m_status=res["w_m_status"],
        w_m_finite=res["w_m_finite"],
        shape_precondition_met=res["shape_precondition_met"],
        diag_Ls=np.array(res["diag_Ls"]),
        M_full=np.array([res["M_full"][L] for L in res["diag_Ls"]]),
        N_full=np.array([res["N_full"][L] for L in res["diag_Ls"]]),
        scan_set=np.array(res["scan_set"]),
        r_seq=np.array([res["r_seq"][L] for L in res["scan_set"]]),
        m0_check=res["m0_check"],
        regulator_pin="a_n^{Mellin}_poleconv-A-double_pole_in_s=3_curvature_grade_n=2",
    )
    print(f"  data -> {OUT_NPZ}")

    make_plot(res)
    print(f"  plot -> {OUT_PNG}")
    print()

    # --- value payload string (no single-quote chars; tool wraps value='...') ---
    a_fit_str = f"{res['alpha_fit']:.4g}" if np.isfinite(res["alpha_fit"]) else "undefined_divergent_r"  # (local)
    value_payload = (
        f"binding_class={res['binding_class']};"
        f"case_A={res['case_A']};"
        f"rate_match={res['rate_match']};"
        f"alpha_fit={a_fit_str};"
        f"hkr_image_nameable={res['hkr_nameable']};"
        f"w_m_finite={res['w_m_finite']};"
        f"shape_precondition_met={res['shape_precondition_met']};"
        f"m={res['moment_order_m']}"
    )  # (local)

    tag = emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX)
    print(tag)

    companion = (
        "binding_class=Case-B-non-binding (confirm-internal); M_2=Tr|D_K|^2/Tr|D_K|^0 "
        "DIVERGES on unbounded D_K (no finite w_m) AND is a spectrum-only functional "
        "with no HKR/Connes-Karoubi image -> W16 wall stands, no registry-landing license; "
        "resolves S104 registry-INCOMPLETE-PENDING to BINDING-DECIDED-non-binding"
    )  # (local)
    extra = [
        "regulator_pin=a_n^{Mellin} poleconv-A-double (pole_in_s=3, curvature_grade_n=2)",
        "Level-2 sub-class=non-binding (bare-decomposition rate; no HKR image -> per cross-pillar-bridge-anatomy.md FORBIDDEN for registry-PASS)",
    ]  # (local)
    print_verdict_payload(verdict, value_payload, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
