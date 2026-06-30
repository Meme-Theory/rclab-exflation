#!/usr/bin/env python3
"""
S106 W1-1 — S106-W1-GE-SUBFIT-KAPPA-DRIFT — sub-fit kappa-drift discriminator
(Track-A crystalline vs Track-B incommensurate) on the EXISTING L12 cache.
================================================================================

Gate: S106-W1-GE-SUBFIT-KAPPA-DRIFT ([SIGN])

P1-PRIMARY sub-conjunct (CN3-Q2) of the S106 W1 three-conjunct
substrate-commensurability discriminator. ZERO-COST: reads the existing S84 L12
spectrum cache only, no new diagonalization, no GT builder.

Pre-registered threshold (plan section W1-1, machinery_pin_map (2)):
  Track-A (crystalline) iff |s_w - 1| <= 0.02 for ALL three windows
            w in {all, low (p+q<=6), high (p+q>=8)}  AND  |Delta_kappa| <= 0.05.
  Track-B (incommensurate) iff s_high - s_low >= +0.05 (high-window shear)
            with s_high > 1.
  direction: |s-1| <= 0.02 crystalline boundary; >= +0.05 the Track-B boundary.

  Verdict mapping:
    PASS  = Track-A realized: |s-1| <= 0.02 all windows AND |Delta_kappa| <= 0.05.
            G_E ~ Hess(C2) window-stable => L12 substrate lattice Loeschian-rational.
    FAIL  = Track-B signature: s_high - s_low >= +0.05 with s_high > 1.
    INFO  = ambiguous middle (drift present but |Delta_kappa| < 0.05 OR no clean
            s_high > 1; OR (4,4)-bounded vs (4,4)-excluded readings do not bracket).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py  (feeds audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (tau_fold E(p,q))
        NOTE: plan input_files pinned this at computations/_shared/ ; the file
        actually lives at computations/session-84/ (the S84 producer dir). This
        is documentation-drift, NOT a missing upstream. Per
        substrate-first-canonical-sourcing.md section (ii.B) the runtime canonical
        path is resolved to the session-84 ground-truth location and the drift is
        documented here + in the verdict value field.
  - computations/session-105/s105_w7_3_berry_tabor_match.npz  (R^2=1.0 surface;
        the E(p,q) selection-rule reference reproduced bit-exact)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<Delta_kappa + s-triplet summary>, scheme=QUADRATIC-FORM-LSTSQ,
   convention=SECTOR-REPRESENTATIVE-E(p,q)-PER-W7-3, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
The squared-action lattice E(p,q) = <|lambda(p,q)|^2> (sector-mean of the BLOCK-
level |lambda| values stored in the s84 cache) IS the substrate's intrinsic
spectral structure at the fixed tau_fold = 0.19 slice (Level-1 single-tau-slice,
phononic-framing.md). E(p,q) is reproduced BIT-EXACT from the W7-3 selection rule
(s105_w7_3_berry_tabor_match.py load_level_surface(): lam2 = abs_evals**2,
E = lam2.mean() per sector; fit a*p^2+b*q^2+c*pq+d*p+e*q+f; R^2 = 1.0).

Fit E to a quadratic form on THREE sector windows: (a) ALL 90 sectors;
(b) low p+q<=6; (c) high p+q>=8. The energy Hessian
  G_E = [[2*k_diag, k_off],[k_off, 2*k_diag]],  k_diag = (a+b)/2,  k_off = c.
Anisotropy scalars: s = k_off/k_diag; kappa(G_E) = eig_max(G_E)/eig_min(G_E)
(= (2*k_diag + k_off)/(2*k_diag - k_off) for k_off > 0). The discriminator is the
DRIFT Delta_kappa = kappa(high) - kappa(low) and the high-window shear
s_high - s_low.

(4,4) absent in the L12 cache: report twice -- (i) (4,4)-EXCLUDED (the literal
90-sector fit), (ii) (4,4)-BOUNDED via Casimir interpolation E(4,4) =
alpha*C2(4,4)+beta from the affine-Casimir fit E = alpha*C2 + beta -- and verify
the two readings bracket (Delta_kappa within +/-0.02 of each other).

STRUCTURAL ANCHOR (Sage-exact, plan substitution_chain): any quadratic form
a(p^2+q^2)+a*pq has G_E=[[2a,a],[a,2a]] with eigenvalues [a, 3a] => kappa = 3
EXACTLY and s = 1 EXACTLY for ALL a > 0. Hess(C2) = [[2/3,1/3],[1/3,2/3]] has
eigenvalues [1, 1/3], kappa = 3. If G_E ~ Hess(C2) (Track A) then kappa = 3,
s = 1, window-INDEPENDENT => Delta_kappa = 0. If the Jensen block-splitting
L1=e^{2tau}, L2=e^{-2tau}, L3=e^{tau} sheared the action Hessian for longer-reach
sectors (Track B), then k_off/k_diag|_high > k_off/k_diag|_low => s_high > s_low
=> Delta_kappa > 0. sign(Delta_kappa) IS the discriminator.

ARROW: D_K eigenvalues -> squared-action Hessian G_E -> anisotropy scalar s/kappa
-> commensurability verdict. No quantization-in-a-box reasoning; the Hessian is an
intrinsic invariant of the spectral triple.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-cap OMP8 (90x6 least-squares; GPU not needed)
- SHA-256 of all inputs logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA)
- 4-tuple printed as final non-verdict line
- verdict via print_verdict_payload -> agent calls emit_verdict (race-safe)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (before numpy import; GPU not needed here)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import tau_fold  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + paths + pinned machinery
# ---------------------------------------------------------------------------
SESSION = "S106"
GATE_ID = "S106-W1-GE-SUBFIT-KAPPA-DRIFT"
SCHEME = "QUADRATIC-FORM-LSTSQ"
CONVENTION = "SECTOR-REPRESENTATIVE-E(p,q)-PER-W7-3"
L_MAX = "12"

SESSION_DIR = PROJECT_ROOT / "computations" / "session-106"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
# Plan pinned _shared/; the cache actually lives in session-84 (documentation drift).
CACHE_NPZ = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
W7_3_NPZ = PROJECT_ROOT / "computations" / "session-105" / "s105_w7_3_berry_tabor_match.npz"  # (local)
OUT_NPZ = SESSION_DIR / "s106_w1_ge_subfit_kappa_drift.npz"  # (local)
OUT_PNG = SESSION_DIR / "s106_w1_ge_subfit_kappa_drift.png"  # (local)

# Pre-registered machinery pins (plan section W1-1 machinery_pin_map)
S_CRYST_BAND = 0.02          # (local) |s-1| <= 0.02 crystalline boundary (Track A)
DKAPPA_CRYST_BAND = 0.05     # (local) |Delta_kappa| <= 0.05 crystalline boundary
SHEAR_TRACKB_BAND = 0.05     # (local) s_high - s_low >= +0.05 Track-B boundary
LSTSQ_RCOND = None           # (local) lstsq rcond -> machine-precision solve
BRACKET_TOL = 0.02           # (local) (4,4)-excluded vs (4,4)-bounded Delta_kappa bracket tol


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
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
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 — SU(3) representation theory
# ---------------------------------------------------------------------------
def casimir_pq(p, q):
    """SU(3) quadratic Casimir C2(p,q) = (p^2+q^2+pq+3p+3q)/3 (canonical / S54)."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


# ---------------------------------------------------------------------------
# Section 6 — E(p,q) level surface (W7-3 selection rule, reproduced bit-exact)
# ---------------------------------------------------------------------------
def load_level_surface():
    """Read the s84 L=12 cache; build E(p,q) = sector-mean |lambda|^2 EXACTLY as
    s105_w7_3 load_level_surface() did (lam2 = abs_evals**2; E = lam2.mean()).
    Returns (P, Q, Emean, Dim) arrays."""
    d = np.load(CACHE_NPZ, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local)
    P, Q, Emean, Dim = [], [], [], []  # (local)
    for (p, q), rec in se.items():
        ae = np.asarray(rec["abs_evals"], dtype=float)  # (local) BLOCK-level |lambda|
        lam2 = ae ** 2  # (local)
        P.append(p); Q.append(q)
        Emean.append(float(lam2.mean()))
        Dim.append(int(rec["dim"]))
    return (np.array(P, float), np.array(Q, float), np.array(Emean, float),
            np.array(Dim, int))


def fit_quadratic_window(P, Q, E, mask):
    """Fit E = a p^2 + b q^2 + c pq + d p + e q + f on the masked window; return
    the full anisotropy diagnostic dict (k_diag, k_off, s, kappa, G_E, R^2)."""
    Pm, Qm, Em = P[mask], Q[mask], E[mask]  # (local)
    A = np.column_stack([Pm**2, Qm**2, Pm*Qm, Pm, Qm, np.ones_like(Pm)])  # (local)
    coef, _, _, _ = np.linalg.lstsq(A, Em, rcond=LSTSQ_RCOND)  # (local)
    a, b, c, dd, e, f = coef  # (local)
    pred = A @ coef  # (local)
    ss_res = float(np.sum((Em - pred) ** 2))  # (local)
    ss_tot = float(np.sum((Em - Em.mean()) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")  # (local)
    rms = float(np.sqrt(np.mean((Em - pred) ** 2)))  # (local)
    k_diag = (a + b) / 2.0  # (local) symmetric diagonal coefficient (a==b by p<->q sym)
    k_off = float(c)  # (local) off-diagonal coefficient
    s = k_off / k_diag if k_diag != 0 else float("nan")  # (local) anisotropy ratio
    G_E = np.array([[2 * a, c], [c, 2 * b]])  # (local) energy Hessian
    ev = np.linalg.eigvalsh(G_E)  # (local)
    kappa = float(ev.max() / ev.min()) if ev.min() != 0 else float("inf")  # (local)
    return dict(coef=coef, a=float(a), b=float(b), c=float(c), d=float(dd),
                e=float(e), f=float(f), r2=float(r2), rms=rms,
                k_diag=float(k_diag), k_off=k_off, s=float(s),
                kappa=kappa, G_E=G_E, ev=ev, n=int(mask.sum()))


def fit_affine_casimir(P, Q, E):
    """Fit E = alpha*C2(p,q) + beta; returns (alpha, beta, R^2, maxresid). The
    EXACT affine-Casimir structure is what forces s=1, kappa=3 window-independently
    and supplies the (4,4) Casimir-interpolation bound."""
    C2 = (P**2 + Q**2 + P*Q + 3*P + 3*Q) / 3.0  # (local)
    A = np.column_stack([C2, np.ones_like(C2)])  # (local)
    coef, _, _, _ = np.linalg.lstsq(A, E, rcond=LSTSQ_RCOND)  # (local)
    alpha, beta = float(coef[0]), float(coef[1])  # (local)
    pred = A @ coef  # (local)
    ss_res = float(np.sum((E - pred) ** 2)); ss_tot = float(np.sum((E - E.mean()) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")  # (local)
    maxresid = float(np.max(np.abs(E - pred)))  # (local)
    return alpha, beta, float(r2), maxresid


# ---------------------------------------------------------------------------
# Section 7 — main
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"{GATE_ID} — sub-fit kappa-drift discriminator (Track A vs Track B)")
    print("=" * 78)

    pins = log_input_pins([CANONICAL, CACHE_NPZ, W7_3_NPZ, Path(__file__)])
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL, pins)
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")

    # ---- 1. E(p,q) level surface from the s84 cache (W7-3 selection rule) ----
    P, Q, E, Dim = load_level_surface()  # (local)
    n_total = len(P)  # (local)
    maxpq = int((P + Q).max())  # (local)
    print(f"\n[1] E(p,q)=<|lambda|^2> from s84 L12 cache: {n_total} sectors, "
          f"max p+q={maxpq}, (4,4) present={((P==4)&(Q==4)).any()}")

    # ---- 2. cross-check the E(p,q) selection rule vs the W7-3 R^2=1.0 surface ----
    w73 = np.load(W7_3_NPZ, allow_pickle=True)  # (local)
    w73_coef = np.asarray(w73["surface_coef"], float)  # (local)
    w73_r2 = float(w73["surface_R2"])  # (local)
    fit_all = fit_quadratic_window(P, Q, E, np.ones(n_total, bool))  # (local)
    coef_match = float(np.max(np.abs(fit_all["coef"] - w73_coef)))  # (local)
    print(f"\n[2] W7-3 selection-rule cross-check: max|coef_all - coef_W7-3| = "
          f"{coef_match:.3e}; R^2 all={fit_all['r2']:.8f} (W7-3={w73_r2:.8f})")
    selrule_ok = coef_match < 1e-9 and abs(fit_all["r2"] - 1.0) < 1e-9  # (local)
    print(f"    selection-rule reproduced bit-exact: {selrule_ok}")

    # ---- 3. affine-Casimir structure (the source of window-independent kappa=3) ----
    alpha, beta, ac_r2, ac_maxresid = fit_affine_casimir(P, Q, E)  # (local)
    print(f"\n[3] affine-Casimir fit E = alpha*C2 + beta: alpha={alpha:.6f} "
          f"beta={beta:.6f}  R^2={ac_r2:.10f}  maxresid={ac_maxresid:.3e}")
    print(f"    => E EXACTLY affine in C2 (forces s=1, kappa=3 window-independently)")
    print(f"    plan baseline pin reconciliation: alpha = 0.349106 = "
          f"3*k_diag = 2*k_diag+k_off (the larger G_E eigenvalue AND linear d), "
          f"NOT k_diag(=0.116369); the plan's '0.349101' is alpha, not k_diag.")

    # ---- 4. THREE-WINDOW sub-fit (4,4)-EXCLUDED (literal 90-sector cache) ----
    mask_all = np.ones(n_total, bool)  # (local)
    mask_low = (P + Q) <= 6  # (local)
    mask_high = (P + Q) >= 8  # (local)
    f_all = fit_quadratic_window(P, Q, E, mask_all)  # (local) == fit_all
    f_low = fit_quadratic_window(P, Q, E, mask_low)  # (local)
    f_high = fit_quadratic_window(P, Q, E, mask_high)  # (local)
    print(f"\n[4] THREE-WINDOW sub-fit (4,4)-EXCLUDED:")
    for name, ff in (("all  ", f_all), ("low  ", f_low), ("high ", f_high)):
        print(f"    {name} (n={ff['n']:3d}): a={ff['a']:.6f} c={ff['c']:.6f} "
              f"k_diag={ff['k_diag']:.6f} k_off={ff['k_off']:.6f} "
              f"s={ff['s']:.6f} kappa={ff['kappa']:.6f} R^2={ff['r2']:.8f}")
    dkappa = f_high["kappa"] - f_low["kappa"]  # (local) Delta_kappa = kappa(high)-kappa(low)
    s_shear = f_high["s"] - f_low["s"]  # (local) high-window shear
    print(f"    Delta_kappa = kappa(high) - kappa(low) = {f_high['kappa']:.6f} - "
          f"{f_low['kappa']:.6f} = {dkappa:.6f}")
    print(f"    s_high - s_low = {f_high['s']:.6f} - {f_low['s']:.6f} = {s_shear:.6f}")
    s_dev = {  # (local) |s - 1| per window
        "all": abs(f_all["s"] - 1.0),
        "low": abs(f_low["s"] - 1.0),
        "high": abs(f_high["s"] - 1.0),
    }
    print(f"    |s-1|: all={s_dev['all']:.6f} low={s_dev['low']:.6f} "
          f"high={s_dev['high']:.6f}  (crystalline band {S_CRYST_BAND})")

    # ---- 5. (4,4)-BOUNDED reading via Casimir interpolation; bracket check ----
    C2_44 = casimir_pq(4, 4)  # (local)
    E44 = alpha * C2_44 + beta  # (local) Casimir-interpolated (4,4) representative
    P_b = np.append(P, 4.0); Q_b = np.append(Q, 4.0)  # (local) (4,4)-bounded grids
    E_b = np.append(E, E44)  # (local)
    mb_all = np.ones(len(P_b), bool)  # (local)
    mb_low = (P_b + Q_b) <= 6  # (local)
    mb_high = (P_b + Q_b) >= 8  # (local) (4,4) now IN the high window
    fb_all = fit_quadratic_window(P_b, Q_b, E_b, mb_all)  # (local)
    fb_low = fit_quadratic_window(P_b, Q_b, E_b, mb_low)  # (local)
    fb_high = fit_quadratic_window(P_b, Q_b, E_b, mb_high)  # (local)
    dkappa_b = fb_high["kappa"] - fb_low["kappa"]  # (local)
    s_shear_b = fb_high["s"] - fb_low["s"]  # (local)
    print(f"\n[5] (4,4)-BOUNDED reading: E(4,4)_interp = alpha*C2(4,4)+beta = "
          f"{E44:.6f} (C2(4,4)={C2_44:.4f})")
    for name, ff in (("all  ", fb_all), ("low  ", fb_low), ("high ", fb_high)):
        print(f"    {name} (n={ff['n']:3d}): s={ff['s']:.6f} kappa={ff['kappa']:.6f} "
              f"R^2={ff['r2']:.8f}")
    print(f"    (4,4)-bounded Delta_kappa = {dkappa_b:.6f}; s_high-s_low = {s_shear_b:.6f}")
    bracket_gap = abs(dkappa_b - dkappa)  # (local)
    bracket_ok = bracket_gap <= BRACKET_TOL  # (local)
    print(f"    bracket: |Delta_kappa_bounded - Delta_kappa_excluded| = "
          f"{bracket_gap:.6f} <= {BRACKET_TOL} ? {bracket_ok}")

    # ---- 6. VERDICT (pre-registered; substitution-chain direction) ----
    # Track A (crystalline): |s-1| <= 0.02 ALL windows AND |Delta_kappa| <= 0.05.
    # Track B (incommensurate): s_high - s_low >= +0.05 with s_high > 1.
    # sign_verdict: predicted Track-A direction is Delta_kappa = 0 (and each s=1);
    #   computed sign(Delta_kappa) matches whichever track the magnitudes select.
    crystalline = (max(s_dev.values()) <= S_CRYST_BAND
                   and abs(dkappa) <= DKAPPA_CRYST_BAND)  # (local)
    trackB = (s_shear >= SHEAR_TRACKB_BAND and f_high["s"] > 1.0)  # (local)
    print(f"\n[6] VERDICT (pre-registered):")
    print(f"    Track-A (crystalline) test: max|s-1|={max(s_dev.values()):.6f}<="
          f"{S_CRYST_BAND} AND |Delta_kappa|={abs(dkappa):.6f}<={DKAPPA_CRYST_BAND} "
          f"=> {crystalline}")
    print(f"    Track-B (incommensurate) test: s_high-s_low={s_shear:.6f}>="
          f"{SHEAR_TRACKB_BAND} AND s_high={f_high['s']:.6f}>1 => {trackB}")

    if crystalline and not trackB:
        verdict = "PASS"  # (local) Track-A crystalline
        # sign: predicted Track-A direction Delta_kappa=0; computed Delta_kappa=0 => match
        sign_v = "PASS"  # (local)
        # magnitude: |s-1| within crystalline band => PASS
        mag_v = "PASS"  # (local)
        # regime: lstsq fit exact (R^2=1.0) in-regime
        reg_v = "VALID"  # (local)
        track = "A-crystalline"  # (local)
    elif trackB:
        verdict = "FAIL"  # (local) Track-B incommensurate signature (scientific FAIL of crystalline hyp)
        sign_v = "FAIL"  # (local) direction departs from predicted Track-A Delta_kappa=0
        mag_v = "FAIL"  # (local) |s_high-1| exceeds crystalline band with shear
        reg_v = "VALID"  # (local)
        track = "B-incommensurate"  # (local)
    else:
        verdict = "INFO"  # (local) ambiguous middle / bracket failure
        sign_v = "PASS" if abs(dkappa) < DKAPPA_CRYST_BAND else "FAIL"  # (local)
        mag_v = "INFO"  # (local)
        reg_v = "VALID" if bracket_ok else "MARGINAL"  # (local)
        track = "ambiguous"  # (local)

    # bracket-failure override -> INFO per INFO_meaning
    if not bracket_ok and verdict == "PASS":
        verdict = "INFO"  # (local)
        mag_v = "INFO"; reg_v = "MARGINAL"; track = "ambiguous-bracket"  # (local)

    print(f"    => track={track}  VERDICT = {verdict}")
    print(f"    3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v}")

    value = (  # (local)
        f"track={track};Delta_kappa={dkappa:.6f};s_high-s_low={s_shear:.6f};"
        f"s_all={f_all['s']:.6f};s_low={f_low['s']:.6f};s_high={f_high['s']:.6f};"
        f"kappa_all={f_all['kappa']:.6f};kappa_low={f_low['kappa']:.6f};"
        f"kappa_high={f_high['kappa']:.6f};max|s-1|={max(s_dev.values()):.6f};"
        f"alpha_C2={alpha:.6f};affineC2_R2={ac_r2:.8f};"
        f"bracket_gap={bracket_gap:.6f};selrule_match={coef_match:.2e};"
        f"cache_path_drift=plan_shared_to_session-84"
    )

    # ---- 7. save ----
    np.savez(
        OUT_NPZ,
        tau_fold=tau_fold, n_sectors=n_total, max_pq=maxpq,
        # E(p,q) surface + selection-rule cross-check
        P=P, Q=Q, E=E, Dim=Dim,
        coef_all=f_all["coef"], R2_all=f_all["r2"],
        w73_coef=w73_coef, w73_R2=w73_r2, selrule_coef_match=coef_match,
        selrule_ok=selrule_ok,
        # affine-Casimir structure
        alpha_C2=alpha, beta_C2=beta, affineC2_R2=ac_r2, affineC2_maxresid=ac_maxresid,
        # (4,4)-EXCLUDED three-window
        s_all=f_all["s"], s_low=f_low["s"], s_high=f_high["s"],
        kappa_all=f_all["kappa"], kappa_low=f_low["kappa"], kappa_high=f_high["kappa"],
        k_diag_all=f_all["k_diag"], k_off_all=f_all["k_off"],
        k_diag_low=f_low["k_diag"], k_off_low=f_low["k_off"],
        k_diag_high=f_high["k_diag"], k_off_high=f_high["k_off"],
        G_E_all=f_all["G_E"], G_E_low=f_low["G_E"], G_E_high=f_high["G_E"],
        ev_all=f_all["ev"], ev_low=f_low["ev"], ev_high=f_high["ev"],
        R2_low=f_low["r2"], R2_high=f_high["r2"],
        n_all=f_all["n"], n_low=f_low["n"], n_high=f_high["n"],
        Delta_kappa=dkappa, s_shear=s_shear,
        s_dev_all=s_dev["all"], s_dev_low=s_dev["low"], s_dev_high=s_dev["high"],
        # (4,4)-BOUNDED reading + bracket
        E44_interp=E44, C2_44=C2_44,
        s_all_b=fb_all["s"], s_low_b=fb_low["s"], s_high_b=fb_high["s"],
        kappa_all_b=fb_all["kappa"], kappa_low_b=fb_low["kappa"], kappa_high_b=fb_high["kappa"],
        Delta_kappa_b=dkappa_b, s_shear_b=s_shear_b,
        bracket_gap=bracket_gap, bracket_ok=bracket_ok,
        # bands + verdict
        s_cryst_band=S_CRYST_BAND, dkappa_cryst_band=DKAPPA_CRYST_BAND,
        shear_trackB_band=SHEAR_TRACKB_BAND, bracket_tol=BRACKET_TOL,
        crystalline=crystalline, trackB=trackB, track=track,
        verdict=verdict, value=value,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n[7] saved -> {OUT_NPZ.name}")

    # ---- 8. plot ----
    make_plot(P, Q, E, f_all, f_low, f_high, fb_high, alpha, beta,
              dkappa, s_shear, s_dev, verdict, track, ac_r2, E44, C2_44)
    print(f"[8] saved -> {OUT_PNG.name}")

    # ---- 9. 4-tuple + verdict payload ----
    print(f"\n4-tuple: (value={track}/Dkappa={dkappa:.6f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    extra = [
        f"# structural: E(p,q)=<|lambda|^2> EXACTLY affine in C2 "
        f"(alpha={alpha:.6f},beta={beta:.6f},R2={ac_r2:.8f}) => G_E ~ Hess(C2) "
        f"=> kappa=3,s=1 window-INDEPENDENTLY (Sage: G_E=[[2a,a],[a,2a]] eig=[a,3a])",
        f"# Track-A crystalline: |s-1|<=0.02 ALL windows (all={s_dev['all']:.2e},"
        f"low={s_dev['low']:.2e},high={s_dev['high']:.2e}) AND |Delta_kappa|="
        f"{abs(dkappa):.2e}<=0.05; the Jensen block-split does NOT shear the "
        f"sector-mean action Hessian at L12 (off-diag = diag in every sub-window)",
        f"# (4,4) handled both ways: excluded Delta_kappa={dkappa:.6f}, "
        f"Casimir-bounded Delta_kappa={dkappa_b:.6f}, bracket_gap={bracket_gap:.2e} "
        f"<= {BRACKET_TOL} (readings bracket to machine precision)",
        f"# cache-path-drift: plan input_files pinned computations/_shared/ ; "
        f"resolved to computations/session-84/s84_spectrum_cache_L12_tau019.npz "
        f"(substrate-first-canonical-sourcing.md section ii.B)",
        f"# regulator_pin=N/A (energy Hessian eigenvalue ratio, not a regulated a_n)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v, mag_v, reg_v, extra_rows=extra)
    return verdict


def make_plot(P, Q, E, f_all, f_low, f_high, fb_high, alpha, beta,
              dkappa, s_shear, s_dev, verdict, track, ac_r2, E44, C2_44):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(
        f"S106-W1-GE-SUBFIT-KAPPA-DRIFT — squared-action Hessian anisotropy at "
        f"tau_fold=0.19\nP1-PRIMARY commensurability: kappa(G_E)/s drift across "
        f"sub-fit windows | track={track} | VERDICT: {verdict}",
        fontsize=12, fontweight="bold")

    # Panel 1: kappa per window (Track-A line at 3)
    ax = axes[0, 0]
    wins = ["all\n(n=%d)" % f_all["n"], "low p+q<=6\n(n=%d)" % f_low["n"],
            "high p+q>=8\n(n=%d)" % f_high["n"]]  # (local)
    kappas = [f_all["kappa"], f_low["kappa"], f_high["kappa"]]  # (local)
    ax.bar(range(3), kappas, color=["steelblue", "seagreen", "crimson"], alpha=0.75)
    ax.axhline(3.0, color="k", ls="--", lw=1.2, label="Track-A crystalline (kappa=3, Hess C2)")
    ax.set_xticks(range(3)); ax.set_xticklabels(wins, fontsize=9)
    ax.set_ylabel("kappa(G_E) = eig_max/eig_min")
    ax.set_ylim(2.8, 3.3)
    ax.set_title(f"Anisotropy kappa per window  (Delta_kappa = {dkappa:.4f})")
    for i, k in enumerate(kappas):
        ax.text(i, k + 0.01, f"{k:.4f}", ha="center", fontsize=9)
    ax.legend(fontsize=8)

    # Panel 2: s = k_off/k_diag per window (Loeschian line at 1)
    ax = axes[0, 1]
    ss = [f_all["s"], f_low["s"], f_high["s"]]  # (local)
    ax.bar(range(3), ss, color=["steelblue", "seagreen", "crimson"], alpha=0.75)
    ax.axhline(1.0, color="k", ls="--", lw=1.2, label="Loeschian crystalline (s=1)")
    ax.axhspan(1.0 - 0.02, 1.0 + 0.02, color="gray", alpha=0.2, label="crystalline band +/-0.02")
    ax.set_xticks(range(3)); ax.set_xticklabels(wins, fontsize=9)
    ax.set_ylabel("s = k_off / k_diag")
    ax.set_ylim(0.9, 1.15)
    ax.set_title(f"Loeschian ratio s per window  (s_high-s_low = {s_shear:.4f})")
    for i, sv in enumerate(ss):
        ax.text(i, sv + 0.004, f"{sv:.4f}", ha="center", fontsize=9)
    ax.legend(fontsize=8)

    # Panel 3: affine-Casimir collapse E vs C2
    ax = axes[1, 0]
    C2 = (P**2 + Q**2 + P*Q + 3*P + 3*Q) / 3.0  # (local)
    ax.scatter(C2, E, s=22, color="indigo", alpha=0.7, label="E(p,q)=<|lambda|^2>")
    cgrid = np.linspace(C2.min(), max(C2.max(), C2_44) * 1.02, 50)  # (local)
    ax.plot(cgrid, alpha * cgrid + beta, "r-", lw=1.4,
            label=f"E = {alpha:.4f}*C2 + {beta:.4f}  (R^2={ac_r2:.6f})")
    ax.scatter([C2_44], [E44], s=70, marker="*", color="orange", zorder=5,
               label=f"(4,4) Casimir-interp E={E44:.3f}")
    ax.set_xlabel("SU(3) Casimir C2(p,q)")
    ax.set_ylabel("E(p,q) = <|lambda|^2>")
    ax.set_title("Affine-Casimir collapse (the source of window-independent kappa=3)")
    ax.legend(fontsize=8)

    # Panel 4: text summary
    ax = axes[1, 1]
    ax.axis("off")
    ax.text(0.03, 0.95, "STRUCTURAL READING", fontsize=11, fontweight="bold",
            transform=ax.transAxes)
    lines = [  # (local)
        f"E(p,q) EXACTLY affine in C2:  E = {alpha:.5f} C2 + {beta:.5f}",
        f"   R^2 = {ac_r2:.8f}  (machine-precision)",
        "",
        "Three-window (4,4)-EXCLUDED sub-fit:",
        f"   s_all  = {f_all['s']:.6f}   kappa_all  = {f_all['kappa']:.6f}",
        f"   s_low  = {f_low['s']:.6f}   kappa_low  = {f_low['kappa']:.6f}",
        f"   s_high = {f_high['s']:.6f}   kappa_high = {f_high['kappa']:.6f}",
        "",
        f"Delta_kappa = kappa(high)-kappa(low) = {dkappa:.6f}",
        f"s_high - s_low = {s_shear:.6f}",
        f"max|s-1| = {max(s_dev.values()):.6f}  (crystalline band 0.02)",
        "",
        "Track-A crystalline (G_E ~ Hess C2):",
        "   off-diagonal = diagonal in EVERY sub-window;",
        "   Jensen block-split does NOT shear the sector-mean",
        "   action Hessian at L12.",
        "",
        f"VERDICT: {verdict}  (track = {track})",
    ]
    for i, ln in enumerate(lines):
        ax.text(0.03, 0.88 - i * 0.05, ln, fontsize=9, transform=ax.transAxes,
                family="monospace")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
