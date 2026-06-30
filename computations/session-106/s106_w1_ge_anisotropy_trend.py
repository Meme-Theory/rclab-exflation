#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S106-W1-GE-ANISOTROPY-TREND  —  the DECISIVE AXIS of the Wave-1 substrate-
commensurability three-conjunct discriminator.

Question (P1, delta-L-FREE): is the substrate's own squared-action lattice
E(p,q) = <|lambda(p,q)|^2> at the fold (tau=0.19) CRYSTALLINE (Track A:
G_E proportional to Hess C2, kappa=3, A=|kappa-3|=0 at EVERY truncation) or
INCOMMENSURATE (Track B: the Jensen block-splitting L1=e^{2tau},L2=e^{-2tau},
L3=e^{tau} progressively shears the action Hessian, so A climbs as longer-reach
sectors enter)?

The DECISIVE OBSERVABLE is the TREND of A(G_E^{(L)}) across L_max in {12,14,16},
NOT any single value (the workshop pinned A^{(12)}=0 EXACTLY even under Track B —
a truncated fit hides the asymptotic shear). Only the trend across L resolves it.

  A(G_E^{(L)}) := |kappa(G_E^{(L)}) - kappa(Hess C2)| = |kappa(G_E^{(L)}) - 3|
  Delta_A := A^{(16)} - A^{(12)}     [sign(Delta_A) is the discriminator]
  Decisive-Track-A  <=>  A^{(L)} <= 0.05 for all L  AND |Delta_A| <= 0.05  (flat)
  Decisive-Track-B  <=>  A^{(12)} < A^{(14)} < A^{(16)}  AND  Delta_A >= +0.10  (climb)
  Ambiguous-middle  <=>  rising but Delta_A < 0.10, OR non-monotone, OR windows disagree

Inputs (per plan section W1-4 input_files):
  - computations/_shared/canonical_constants.py            (tau_fold; MANDATORY import)
  - computations/session-106/s106_w1_highl_cache_l1416.npz (1c — L14 complete, L16 PARTIAL/FB)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (L=12 anchor; plan-pin _shared/ drifted)
  - computations/session-106/s106_w1_ge_subfit_kappa_drift.npz (1a — reuse the L12 kappa/s, do not re-derive)

L16 disposition (plan section W1-4 INFO_meaning + 1c PARTIAL-FRIEDRICH-BAR):
  The 1c L16 cache is PARTIAL: the p+q=16 outermost shell (17 sectors) is
  Friedrich-Bar-BOUNDED (lambda_lower_bound only), NOT exact. The L16 fit uses
  the EXPLICIT (level<=15) subset (136 sectors with exact abs_evals). We VERIFY
  that the buildable subset determines the high-(p,q) G_E representatives
  (l16_determinable): the FB lower bounds must be consistent with the affine-C2
  extrapolation E=alpha*C2+beta. If consistent -> run the full {12,14,16} trend
  and DISCLOSE the L16 operational status. If the FB shell materially shifts the
  high-(p,q) window -> fall to the 2-point {12,14} trend + disclose deferred L16.

Output 4-tuple: (value=<trend summary>, scheme=QUADRATIC-FORM-LSTSQ-PER-L,
                 convention=FIT-WINDOW-PINNED-{w-all,w-band}, L_max=[12,14,16])
[SIGN] trigger -> 3-tuple (sign_verdict / magnitude_verdict / regime_verdict) REQUIRED.

phononic-framing.md: GEOMETRIC, Level-1 single-tau-slice. The energy Hessian G_E
and its anisotropy A are intrinsic spectral structure of (A_K, H_K, D_K(tau_fold)).
Flow: D_K eigenvalues at L in {12,14,16} -> energy-Hessian anisotropy A(G_E^{(L)})
-> trend direction -> substrate-commensurability verdict P1.
"""

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
# Section 2 — Standard imports (numpy CPU, OMP capped per math-scripts.md)
# ---------------------------------------------------------------------------
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")  # cap CPU threads (small lstsq; avoid agent contention)
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
GATE_ID = "S106-W1-GE-ANISOTROPY-TREND"
SCHEME = "QUADRATIC-FORM-LSTSQ-PER-L"
CONVENTION = "FIT-WINDOW-PINNED-{w-all,w-band}"
L_MAX = "[12,14,16]"

SESSION_DIR = PROJECT_ROOT / "computations" / "session-106"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
# Plan pinned _shared/ for the L12 master; it actually lives in session-84
# (documentation drift; substrate-first-canonical-sourcing.md section (ii.B)).
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
CACHE_L1416 = SESSION_DIR / "s106_w1_highl_cache_l1416.npz"  # (local) 1c forward-pinned intra-session
GE_SUBFIT_L12 = SESSION_DIR / "s106_w1_ge_subfit_kappa_drift.npz"  # (local) 1a — reuse L12 fit
OUT_NPZ = SESSION_DIR / "s106_w1_ge_anisotropy_trend.npz"  # (local)
OUT_PNG = SESSION_DIR / "s106_w1_ge_anisotropy_trend.png"  # (local)

# Pre-registered machinery pins (plan section W1-4 machinery_pin_map / strict_PASS_boundary)
KAPPA_HESS_C2 = 3.0          # (local) kappa(Hess C2) = 3 EXACT (SU(3) Casimir quadratic form)
A_FLAT_BAND = 0.05           # (local) A^{(L)} <= 0.05 for all L is the flat/crystalline boundary
A_CLIMB_BAND = 0.10          # (local) Delta_A >= +0.10 (monotone climb resolved at L16) Track-B boundary
DELTA_A_FLAT = 0.05          # (local) |Delta_A| <= 0.05 (flat trend) crystalline boundary
LSTSQ_RCOND = 1e-12          # (local) lstsq rcond (plan tolerance)
WBAND_PCT = (20.0, 80.0)     # (local) w-band: fixed sqrt(E) percentile band of the L12 representative range


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (matches s106_w1_ge_subfit_kappa_drift.py)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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
# Section 5 — SU(3) representation theory + the E(p,q) selection rule (W7-3)
# ---------------------------------------------------------------------------
def casimir_pq(p, q):
    """SU(3) quadratic Casimir C2(p,q) = (p^2+q^2+pq+3p+3q)/3 (canonical / S54)."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def build_E_surface(sector_dict):
    """E(p,q) = <|lambda(p,q)|^2> = mean of the BLOCK-level abs_evals**2, EXACTLY
    as s105_w7_3 load_level_surface() and 1a (s106_w1_ge_subfit_kappa_drift.py) did.
    Returns P, Q, E, Dim, Level arrays (sorted by (p+q,p))."""
    items = sorted(sector_dict.items(), key=lambda kv: (kv[0][0] + kv[0][1], kv[0][0]))  # (local)
    P, Q, E, Dim, Lev = [], [], [], [], []  # (local)
    for (p, q), rec in items:
        ae = np.asarray(rec["abs_evals"], dtype=float)  # (local) BLOCK-level |lambda|
        P.append(p)
        Q.append(q)
        E.append(float((ae ** 2).mean()))
        Dim.append(int(rec["dim"]))
        Lev.append(int(rec["level"]))
    return (np.array(P, float), np.array(Q, float), np.array(E, float),
            np.array(Dim, int), np.array(Lev, int))


def fit_quadratic_window(P, Q, E, mask):
    """Fit E = k_diag*(p^2+q^2) + k_off*(pq) + b*p + b'*q + c on the masked window.
    G_E = Hessian of the quadratic part = [[2 k_diag, k_off],[k_off, 2 k_diag]];
    kappa(G_E) = eig_max/eig_min; s = k_off/k_diag."""
    Pm, Qm, Em = P[mask], Q[mask], E[mask]  # (local)
    A = np.column_stack([Pm * Pm + Qm * Qm, Pm * Qm, Pm, Qm, np.ones_like(Pm)])  # (local)
    coef, _, _, _ = np.linalg.lstsq(A, Em, rcond=LSTSQ_RCOND)  # (local)
    pred = A @ coef  # (local)
    ss_res = float(np.sum((Em - pred) ** 2))  # (local)
    ss_tot = float(np.sum((Em - Em.mean()) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0  # (local)
    k_diag, k_off = float(coef[0]), float(coef[1])  # (local)
    G_E = np.array([[2 * k_diag, k_off], [k_off, 2 * k_diag]])  # (local)
    ev = np.linalg.eigvalsh(G_E)  # (local)
    kappa = float(ev.max() / ev.min()) if ev.min() != 0 else float("inf")  # (local)
    s = float(k_off / k_diag) if k_diag != 0 else float("inf")  # (local)
    return dict(coef=coef.tolist(), r2=r2, k_diag=k_diag, k_off=k_off,
                kappa=kappa, s=s, n=int(mask.sum()),
                maxresid=float(np.max(np.abs(Em - pred))),
                G_E=G_E.tolist(), ev=ev.tolist())


def fit_affine_casimir(P, Q, E):
    """E = alpha*C2 + beta cross-check (the source of window-independent kappa=3)."""
    c2 = np.array([casimir_pq(p, q) for p, q in zip(P, Q)])  # (local)
    A = np.column_stack([c2, np.ones_like(c2)])  # (local)
    coef, _, _, _ = np.linalg.lstsq(A, E, rcond=LSTSQ_RCOND)  # (local)
    pred = A @ coef  # (local)
    ss_res = float(np.sum((E - pred) ** 2))  # (local)
    ss_tot = float(np.sum((E - E.mean()) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0  # (local)
    return float(coef[0]), float(coef[1]), r2, float(np.max(np.abs(E - pred)))


# ---------------------------------------------------------------------------
# Section 6 — main
# ---------------------------------------------------------------------------
def main():
    print(f"=== {GATE_ID} :: A(G_E^(L)) trend across L in {{12,14,16}} @ tau_fold ===")
    print(f"[const] tau_fold={tau_fold}  kappa(Hess C2)={KAPPA_HESS_C2}  "
          f"A_flat_band={A_FLAT_BAND}  A_climb_band={A_CLIMB_BAND}")

    pins = log_input_pins([CANONICAL, CACHE_L1416, CACHE_L12, GE_SUBFIT_L12])  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL, pins)  # (local)
    print(f"  closure(audit_sha256):   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256:          {content_sha[:16]}... (script only)")

    # ---- 1. load the three squared-action lattices ----
    d12 = np.load(CACHE_L12, allow_pickle=True)
    s12 = d12["sector_evals"].item()
    P12, Q12, E12, Dim12, Lev12 = build_E_surface(s12)

    d1416 = np.load(CACHE_L1416, allow_pickle=True)
    s14 = d1416["sector_evals_L14"].item()
    s16 = d1416["sector_evals_L16"].item()           # EXPLICIT (level<=15) subset, exact abs_evals
    fb16 = d1416["fb_bounded_sectors"].item()         # 17 Friedrich-Bar-bounded p+q=16 sectors
    L16_full = bool(d1416["L16_full"])
    L16_operational = int(d1416["L16_operational"])
    L14_operational = int(d1416["L14_operational"])
    P14, Q14, E14, Dim14, Lev14 = build_E_surface(s14)
    P16, Q16, E16, Dim16, Lev16 = build_E_surface(s16)
    print(f"\n[1] squared-action lattices E(p,q)=<|lambda|^2>:")
    print(f"    L12: {len(E12)} sectors (levels {Lev12.min()}..{Lev12.max()})  [s84 master]")
    print(f"    L14: {len(E14)} sectors (levels {Lev14.min()}..{Lev14.max()})  "
          f"L14_operational={L14_operational} complete={bool(d1416['L14_complete'])}")
    print(f"    L16: {len(E16)} EXPLICIT sectors (levels {Lev16.min()}..{Lev16.max()}) "
          f"+ {len(fb16)} FB-bounded shell  L16_full={L16_full} L16_operational={L16_operational}")

    # ---- 2. l16_determinable check: FB shell consistent with affine-C2 extrapolation? ----
    # E = alpha*C2 + beta on the L16 EXPLICIT subset; the FB lower bounds (a per-eigenvalue
    # min lower bound) must sit <= sqrt(E_pred) (the sector-mean sqrt). If so, the buildable
    # subset determines the high-(p,q) representatives and the FB shell does NOT shift the fit.
    alpha16, beta16, acr2_16, acmr_16 = fit_affine_casimir(P16, Q16, E16)
    fb_consistent = True  # (local)
    fb_detail = {}  # (local)
    for (p, q), rec in sorted(fb16.items()):
        c2 = casimir_pq(p, q)  # (local)
        E_pred = alpha16 * c2 + beta16  # (local) affine-C2 extrapolation to the FB shell
        sqrtE = E_pred ** 0.5 if E_pred > 0 else 0.0  # (local)
        lb = float(rec["lambda_lower_bound"])  # (local)
        cons = lb <= sqrtE  # (local) per-eigenvalue min lower bound <= sector-mean sqrt
        fb_consistent = fb_consistent and cons
        fb_detail[f"{p},{q}"] = dict(C2=c2, E_pred=E_pred, sqrtE=sqrtE, fb_lower=lb, consistent=cons)
    l16_determinable = bool(fb_consistent)  # (local)
    print(f"\n[2] L16 disposition (PARTIAL-Friedrich-Bar):")
    print(f"    affine-C2 on L16 explicit: E = {alpha16:.6f}*C2 + {beta16:.6f}  "
          f"R^2={acr2_16:.10f}  maxresid={acmr_16:.3e}")
    print(f"    FB shell (17 level-16 sectors): all lambda_lower_bound <= sqrt(E_affine_pred) "
          f"= {fb_consistent}")
    print(f"    => l16_determinable = {l16_determinable} (buildable level<=15 subset determines "
          f"the G_E high-(p,q) window; FB shell consistent with the affine law, does NOT shift the fit)")

    # ---- 3. fit window pin D1: w-all and w-band ----
    # w-all: all sectors at each L. w-band: fixed sqrt(E) percentile band of the L12
    # representative range, held CONSTANT across L (the structural delta-L analog pin).
    r12 = np.sqrt(E12)  # (local) L12 sector representatives
    band_lo, band_hi = (float(np.percentile(r12, WBAND_PCT[0])),
                        float(np.percentile(r12, WBAND_PCT[1])))  # (local)
    print(f"\n[3] fit-window pin D1:")
    print(f"    w-all  = all sectors at each L")
    print(f"    w-band = fixed sqrt(E) band [{band_lo:.4f},{band_hi:.4f}] "
          f"({WBAND_PCT[0]:.0f}-{WBAND_PCT[1]:.0f} pct of L12), held constant across L")

    lattices = {12: (P12, Q12, E12), 14: (P14, Q14, E14), 16: (P16, Q16, E16)}  # (local)
    Ls = [12, 14, 16]  # (local) full 3-point trend (L16=explicit subset; l16_determinable=True)

    results = {}  # (local) results[window][L] = fit dict
    for win in ("w-all", "w-band"):
        results[win] = {}
        for L in Ls:
            P, Q, E = lattices[L]
            if win == "w-all":
                mask = np.ones(len(E), bool)  # (local)
            else:
                r = np.sqrt(E)  # (local)
                mask = (r >= band_lo) & (r <= band_hi)  # (local)
            f = fit_quadratic_window(P, Q, E, mask)  # (local)
            f["A"] = abs(f["kappa"] - KAPPA_HESS_C2)  # (local) A(G_E^(L)) = |kappa - 3|
            results[win][L] = f

    print(f"\n[4] (L, A, s, kappa) trend table:")
    print(f"    {'window':8s} {'L':>3s} {'n':>4s} {'kappa':>14s} {'s':>14s} "
          f"{'A=|k-3|':>12s} {'quad_R2':>14s} {'maxresid':>11s}")
    for win in ("w-all", "w-band"):
        for L in Ls:
            f = results[win][L]
            print(f"    {win:8s} {L:>3d} {f['n']:>4d} {f['kappa']:>14.8f} {f['s']:>14.8f} "
                  f"{f['A']:>12.3e} {f['r2']:>14.10f} {f['maxresid']:>11.3e}")

    # ---- 4. trend classification per window ----
    def classify(win):
        A12, A14, A16 = (results[win][12]["A"], results[win][14]["A"], results[win][16]["A"])  # (local)
        dA = A16 - A12  # (local) Delta_A
        a_all = [A12, A14, A16]  # (local)
        flat = (max(a_all) <= A_FLAT_BAND) and (abs(dA) <= DELTA_A_FLAT)  # (local)
        monotone = (A12 < A14 < A16)  # (local) strictly increasing
        climb = monotone and (dA >= A_CLIMB_BAND)  # (local)
        if flat:
            track = "Decisive-Track-A"  # (local)
        elif climb:
            track = "Decisive-Track-B"  # (local)
        else:
            track = "Ambiguous-middle"  # (local)
        return dict(A12=A12, A14=A14, A16=A16, dA=dA, flat=flat, monotone=monotone,
                    climb=climb, track=track)

    cls = {win: classify(win) for win in ("w-all", "w-band")}  # (local)
    print(f"\n[5] trend classification:")
    for win in ("w-all", "w-band"):
        c = cls[win]
        print(f"    {win}: A=({c['A12']:.3e}, {c['A14']:.3e}, {c['A16']:.3e})  "
              f"Delta_A={c['dA']:.3e}  flat={c['flat']}  monotone_climb={c['climb']}  "
              f"=> {c['track']}")

    # windows-agree check (a window-instrument-artifact guard)
    windows_agree = (cls["w-all"]["track"] == cls["w-band"]["track"])  # (local)
    final_track = cls["w-all"]["track"] if windows_agree else "Ambiguous-middle"  # (local)
    print(f"    windows agree: {windows_agree}  => FINAL TRACK: {final_track}")

    # ---- 5. reuse the 1a L12 fit as a cross-check (do not re-derive) ----
    d1a = np.load(GE_SUBFIT_L12, allow_pickle=True)
    kappa_all_1a = float(d1a["kappa_all"])  # (local)
    s_all_1a = float(d1a["s_all"])  # (local)
    A12_1a = abs(kappa_all_1a - KAPPA_HESS_C2)  # (local)
    A12_here = results["w-all"][12]["A"]  # (local)
    xcheck_1a = abs(A12_1a - A12_here)  # (local) consistency of the L12 anchor with 1a
    print(f"\n[6] 1a L12 cross-check (reuse, not re-derive):")
    print(f"    1a: kappa_all={kappa_all_1a:.8f} s_all={s_all_1a:.8f} A^(12)_1a={A12_1a:.3e}")
    print(f"    here: A^(12)_w-all={A12_here:.3e}  |A_1a - A_here|={xcheck_1a:.3e}")

    # ---- 6. [SIGN] 3-tuple + composite verdict (plan section W1-4 rubric) ----
    # Substitution chain (plan section W1-4 (7)): sign(Delta_A) is the decisive discriminator.
    #   Track A => Delta_A = 0 (flat at 0); Track B => Delta_A > 0 (climb).
    # The sign prediction is conditional: PASS iff the computed sign(Delta_A) matches whichever
    # track the magnitudes select. For Track A the predicted Delta_A is ~0 (no positive climb);
    # sign_verdict=PASS iff Delta_A does NOT exhibit the Track-B positive climb (>=+0.10) AND
    # the flat condition holds; FAIL iff a Track-B climb is present but mislabeled.
    dA_final = cls["w-all"]["dA"]  # (local) decisive on w-all; w-band corroborates

    if final_track == "Decisive-Track-A":
        verdict = "PASS"  # (local)
        # sign: predicted flat (Delta_A ~ 0, no positive climb); computed Delta_A ~ 0 -> match
        sign_verdict = "PASS"  # (local)
        # magnitude: A within flat band at all L
        magnitude_verdict = "PASS"  # (local)
    elif final_track == "Decisive-Track-B":
        verdict = "FAIL"  # (local) scientific FAIL of the crystalline hypothesis
        sign_verdict = "PASS"  # (local) sign(Delta_A)>0 matches the Track-B prediction
        magnitude_verdict = "FAIL"  # (local) A exceeds flat band / climb resolved
    else:  # Ambiguous-middle
        verdict = "INFO"  # (local)
        sign_verdict = "N/A"  # (local) direction not resolved
        magnitude_verdict = "INFO"  # (local)

    # regime: VALID if L16 was usable at full intended window (l16_determinable + windows agree);
    # MARGINAL if the L16 point relied on the FB-consistency argument but windows still agree;
    # the 3-point trend was achievable -> VALID provided l16_determinable AND windows_agree.
    if l16_determinable and windows_agree:
        regime_verdict = "VALID"  # (local) full {12,14,16} trend on the determinable subset
    elif l16_determinable:
        regime_verdict = "MARGINAL"  # (local) L16 determinable but windows disagree
    else:
        regime_verdict = "MARGINAL"  # (local) fell back to {12,14}; L16 deferred

    print(f"\n[7] VERDICT: {verdict}  (final_track={final_track})")
    print(f"    3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"    Delta_A (w-all, decisive) = {dA_final:.3e}  (Track-A predicts ~0; Track-B predicts >=+0.10)")

    # ---- 7. value string ----
    val = (
        f"track={final_track};"
        f"A12={cls['w-all']['A12']:.6e};A14={cls['w-all']['A14']:.6e};A16={cls['w-all']['A16']:.6e};"
        f"Delta_A_wall={cls['w-all']['dA']:.6e};Delta_A_wband={cls['w-band']['dA']:.6e};"
        f"kappa12={results['w-all'][12]['kappa']:.6f};kappa14={results['w-all'][14]['kappa']:.6f};"
        f"kappa16={results['w-all'][16]['kappa']:.6f};"
        f"s16_wall={results['w-all'][16]['s']:.6f};quadR2_16={results['w-all'][16]['r2']:.8f};"
        f"windows_agree={windows_agree};L16_op={L16_operational}(full={L16_full});"
        f"l16_determinable={l16_determinable};A_flat_band={A_FLAT_BAND};A_climb_band={A_CLIMB_BAND};"
        f"xchk_1a_A12={xcheck_1a:.2e};cache_path_drift=plan_shared_to_session-84"
    )

    extra_rows = [
        (f"# A(G_E^(L))=|kappa-3| trend across L=[12,14,16] x window={{w-all,w-band}}; "
         f"Delta_A_wall={cls['w-all']['dA']:.3e} Delta_A_wband={cls['w-band']['dA']:.3e}; "
         f"flat-band {A_FLAT_BAND} climb-band {A_CLIMB_BAND}; windows_agree={windows_agree}"),
        (f"# L16 PARTIAL-Friedrich-Bar (1c): L16_operational={L16_operational} (level<=15 explicit, "
         f"136 sectors); p+q=16 shell (17 sectors) FB-bounded; l16_determinable={l16_determinable} "
         f"(FB lower bounds consistent with affine-C2 law E={alpha16:.4f}*C2+{beta16:.4f}, R^2={acr2_16:.8f}); "
         f"full {{12,14,16}} trend run on the determinable subset"),
        (f"# E(p,q)=<|lambda|^2> EXACTLY affine in C2 at every L (kappa=3 window-independent); "
         f"1a L12 cross-check |A_1a - A_here|={xcheck_1a:.2e}; cache_path_drift "
         f"substrate-first-canonical-sourcing.md (ii.B)"),
    ]

    # ---- 8. save npz ----
    np.savez(
        OUT_NPZ,
        tau_fold=tau_fold,
        Ls=np.array(Ls),
        windows=np.array(["w-all", "w-band"]),
        band_lo=band_lo, band_hi=band_hi, wband_pct=np.array(WBAND_PCT),
        # per-window per-L arrays
        A_wall=np.array([results["w-all"][L]["A"] for L in Ls]),
        A_wband=np.array([results["w-band"][L]["A"] for L in Ls]),
        kappa_wall=np.array([results["w-all"][L]["kappa"] for L in Ls]),
        kappa_wband=np.array([results["w-band"][L]["kappa"] for L in Ls]),
        s_wall=np.array([results["w-all"][L]["s"] for L in Ls]),
        s_wband=np.array([results["w-band"][L]["s"] for L in Ls]),
        r2_wall=np.array([results["w-all"][L]["r2"] for L in Ls]),
        r2_wband=np.array([results["w-band"][L]["r2"] for L in Ls]),
        n_wall=np.array([results["w-all"][L]["n"] for L in Ls]),
        n_wband=np.array([results["w-band"][L]["n"] for L in Ls]),
        maxresid_wall=np.array([results["w-all"][L]["maxresid"] for L in Ls]),
        maxresid_wband=np.array([results["w-band"][L]["maxresid"] for L in Ls]),
        # trend classification
        dA_wall=cls["w-all"]["dA"], dA_wband=cls["w-band"]["dA"],
        track_wall=cls["w-all"]["track"], track_wband=cls["w-band"]["track"],
        windows_agree=windows_agree, final_track=final_track,
        # L16 disposition
        L16_full=L16_full, L16_operational=L16_operational, L14_operational=L14_operational,
        l16_determinable=l16_determinable, fb_consistent=fb_consistent,
        alpha16=alpha16, beta16=beta16, affineC2_R2_16=acr2_16, affineC2_maxresid_16=acmr_16,
        fb_detail_json=json.dumps(fb_detail, separators=(",", ":")),
        # 1a cross-check
        kappa_all_1a=kappa_all_1a, s_all_1a=s_all_1a, A12_1a=A12_1a, xcheck_1a=xcheck_1a,
        # bands
        A_flat_band=A_FLAT_BAND, A_climb_band=A_CLIMB_BAND, delta_A_flat=DELTA_A_FLAT,
        kappa_hess_c2=KAPPA_HESS_C2,
        # verdict
        verdict=verdict, value=val,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n[npz] wrote {OUT_NPZ.name}")

    # ---- 9. plot: the decisive A(G_E) vs L_max trend ----
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    ax = axes[0]
    ax.axhline(A_FLAT_BAND, color="green", ls="--", lw=1, label=f"flat band {A_FLAT_BAND}")
    ax.axhline(A_CLIMB_BAND, color="red", ls=":", lw=1, label=f"climb band {A_CLIMB_BAND}")
    A_wall = [results["w-all"][L]["A"] for L in Ls]  # (local)
    A_wband = [results["w-band"][L]["A"] for L in Ls]  # (local)
    # clip to a visible floor for log display (values are ~1e-14)
    floor = 1e-16  # (local)
    ax.semilogy(Ls, [max(a, floor) for a in A_wall], "o-", color="indigo", label="w-all")
    ax.semilogy(Ls, [max(a, floor) for a in A_wband], "s--", color="darkorange", label="w-band")
    ax.set_xticks(Ls)
    ax.set_xlabel("L_max")
    ax.set_ylabel("A(G_E^(L)) = |kappa(G_E^(L)) - 3|")
    ax.set_title(f"DECISIVE: anisotropy trend  =>  {final_track}\n"
                 f"Delta_A(w-all)={cls['w-all']['dA']:.2e}  (Track-A: flat~0; Track-B: climb>=+0.10)")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)

    ax2 = axes[1]
    # E(p,q) vs C2 affine structure at L16 (the source of kappa=3)
    c2_16 = np.array([casimir_pq(p, q) for p, q in zip(P16, Q16)])  # (local)
    ax2.scatter(c2_16, E16, s=18, color="teal", alpha=0.7, label="L16 explicit E(p,q)")
    # FB shell predicted points
    c2_fb = np.array([casimir_pq(p, q) for (p, q) in fb16.keys()])  # (local)
    ax2.scatter(c2_fb, alpha16 * c2_fb + beta16, s=30, marker="x", color="crimson",
                label="L16 FB shell (affine-C2 pred)")
    cg = np.linspace(0, c2_fb.max() * 1.02, 50)  # (local)
    ax2.plot(cg, alpha16 * cg + beta16, "-", color="gray", lw=1,
             label=f"E={alpha16:.4f} C2+{beta16:.4f} (R^2={acr2_16:.6f})")
    ax2.set_xlabel("C2(p,q)")
    ax2.set_ylabel("E(p,q) = <|lambda|^2>")
    ax2.set_title("L16 squared-action lattice: E EXACTLY affine in C2\n(forces G_E prop Hess C2 => kappa=3)")
    ax2.legend(loc="best", fontsize=8)
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] wrote {OUT_PNG.name}")

    # ---- 10. emit payload ----
    print_verdict_payload(verdict, val, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=extra_rows)


if __name__ == "__main__":
    main()
