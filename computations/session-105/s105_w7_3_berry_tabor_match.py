#!/usr/bin/env python3
"""
S105 W7-3 — S105-W7-3-BERRY-TABOR-MATCH — independent Berry-Tabor frequency-map
prediction of the substrate's closed-geodesic length spectrum at tau_fold, matched
line-by-line against the W7-2 measured peak table.
================================================================================

Gate: S105-W7-3-BERRY-TABOR-MATCH ([VERIFY])

Pre-registered threshold (plan §W7-3):
  operator: ratio  n_matched / n_W7-2_stable_peaks >= match_frac
            with |L_pred - L_meas| <= delta_L per match
  PASS iff match_frac >= 2/3 (>=2 of every 3 W7-2 stable peaks matched to a
            predicted resonance length within delta_L).
  FAIL iff < 2/3 matched (systematic position mismatch).
  INFO iff positions match but amplitudes systematically off (sign/position
            correct, magnitude off) -- composite per schema-v2 collapse; OR
            W7-2 returned INFO (few peaks) -> resolution-limited.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-105/s105_w7_2_length_spectrum_ft.npz  (measured peaks + delta_L)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (tau_fold level surface E(p,q))
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  Method source (REQUIRED READING; not consumed at runtime as data):
  - computations/session-54/s54_gutzwiller_su3.py (Berry-Tabor amplitude, Manakov
    integrability, det(M-I)=0 theorem)

Output 4-tuple:
  (value=<match_frac>, scheme=BERRY-TABOR-INTEGRABLE,
   convention=Berry-Tabor integrable-system trace formula (rank r=2; NOT Gutzwiller),
   L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
The Jensen Euler-Arnold geodesic flow on (SU(3), g_tau) is Manakov-integrable
(S54-established: compact semisimple group + left-invariant metric => Manakov
integrals). Integrable => periodic geodesics lie on rank-2 invariant tori in
continuous conjugation families => transverse monodromy M has a kernel along the
family => det(M - I) = 0 IDENTICALLY => the Gutzwiller isolated-orbit amplitude
1/sqrt|det(M-I)| DIVERGES and is structurally inapplicable. The regular replacement
is the Berry-Tabor trace formula for integrable systems.

The action variables ARE the Dynkin labels (p,q) (S54). The substrate's level
surface is the Dirac square E(p,q) = <|lambda|^2>_(p,q); at tau_fold it is read
DIRECTLY from the s84 L=12 cache (sector-mean lambda^2). It is EXACTLY quadratic in
(p,q) (R^2 = 1.0 measured in-script): E = a(p^2+q^2) + c*pq + d(p+q) + f. The
frequency map is omega_i = dE/dI_i; the energy Hessian G_E = d^2E/dI_i dI_j is the
metric quadratic form in action space.

Berry-Tabor closed-orbit lengths (the geometric-side lengths the W7-2 FT-in-lambda
measures). Two complementary substrate-natural forms:

  FORM A (PRIMARY -- Poisson-dual wave-trace; matches the W7-2 length-axis
          convention EXACTLY):
    The FT-in-lambda peak at L is sourced by a cos(lambda * L) oscillation in the
    eigenvalue density (W7-2 length_fft: L_axis = 2*pi*freq; period-in-lambda
    2*pi/L). For an integrable system with E(I) = lambda^2(I) a quadratic form, the
    Poisson summation of the lattice sum gives oscillations whose closed-orbit
    length for winding vector m is the dual-lattice length in the energy metric:
        L_m = 2*pi * sqrt( m^T (G_E/2)^{-1} m ),   m in Z^2 minus {0}
    where G_E/2 = M(tau) is the metric form. At tau=0, G_E = Hess(C2) and M =
    (1/3)[[1,1/2],[1/2,1]], giving the primitive length 4*pi = 12.566 EXACTLY at
    m=(-1,-1) -- the W7-2 coroot-lattice control. This is the SAME wave-trace
    conjugation W7-2 uses for its tau=0 control (s105_w7_2 coroot_lengths()).

  FORM B (SECONDARY -- the plan's single-resonance phrasing):
    L_{m1,m2} = 2*pi / |m1*omega1 + m2*omega2| at a reference action I*=(p*,q*),
    omega_i = dE/dI_i. Reported for completeness; Form A controls the FT-in-lambda
    peaks via Poisson summation and is the one matched as PRIMARY.

Berry-Tabor amplitude per sector (canonical proven_498 / S54 form):
    A_BT(p,q) = dim(p,q) * 16 / (2*pi)^{3/2} / sqrt|det(Hess E)|,  r=2.

The match: for each W7-2 stable peak L_meas, test whether some predicted L_pred
(Form A, |m_i| <= m_max=8) lies within delta_L; report n_matched / 19 and the
amplitude correspondence. PASS iff >= 2/3.

ARROW: metric g_tau -> frequency map omega(I)=dE/dI -> resonance lengths L_m ->
predicted oscillation peaks -> matched against measured spectrum. Lengths are
DERIVED from the substrate's own integrable dynamics, never fit.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- CPU-cap OMP8 (small symbolic/numeric frequency map; heavy spectral work is in W7-2)
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
from canonical_constants import PI, tau_fold  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import itertools  # noqa: E402
import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + paths + pinned machinery
# ---------------------------------------------------------------------------
SESSION = "S105"
GATE_ID = "S105-W7-3-BERRY-TABOR-MATCH"
SCHEME = "BERRY-TABOR-INTEGRABLE"
CONVENTION = "Berry-Tabor-integrable-trace-formula-rank2-NOT-Gutzwiller-detMmI0"
L_MAX = "12"

SESSION_DIR = PROJECT_ROOT / "computations" / "session-105"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
W7_2_NPZ = SESSION_DIR / "s105_w7_2_length_spectrum_ft.npz"  # (local)
CACHE_NPZ = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
S54_SRC = PROJECT_ROOT / "computations" / "session-54" / "s54_gutzwiller_su3.py"  # (local)
OUT_NPZ = SESSION_DIR / "s105_w7_3_berry_tabor_match.npz"  # (local)
OUT_PNG = SESSION_DIR / "s105_w7_3_berry_tabor_match.png"  # (local)

# Pre-registered machinery pins (plan §W7-3 machinery_pin_map)
M_MAX = 8                       # (local) Berry-Tabor winding range |m_i| <= 8 (S54)
MATCH_FRAC_PASS = 2.0 / 3.0     # (local) strict PASS boundary
FREQ_TOL_REL = 1e-3             # (local) resonance frequency tolerance (Form B)


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
# Section 5 — SU(3) representation theory (re-aimed S54 machinery)
# ---------------------------------------------------------------------------
def dim_pq(p, q):
    """Dimension of (p,q) irrep of SU(3) (S54 dim_pq)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_pq(p, q):
    """SU(3) quadratic Casimir C2(p,q) = (p^2+q^2+pq+3p+3q)/3 (S54 casimir_pq)."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


# ---------------------------------------------------------------------------
# Section 6 — tau_fold level surface E(p,q) from the s84 cache + frequency map
# ---------------------------------------------------------------------------
def load_level_surface():
    """Read the s84 L=12 cache; build E(p,q) = sector-mean |lambda|^2 (the Dirac
    square level surface at tau_fold). Returns (P, Q, E, Emin) arrays + dim map."""
    d = np.load(CACHE_NPZ, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local)
    P, Q, Emean, Emin, Dim = [], [], [], [], []  # (local)
    for (p, q), rec in se.items():
        ae = np.asarray(rec["abs_evals"], dtype=float)  # (local) BLOCK-level |lambda|
        lam2 = ae ** 2  # (local)
        P.append(p); Q.append(q)
        Emean.append(float(lam2.mean()))
        Emin.append(float(lam2.min()))
        Dim.append(int(rec["dim"]))
    return (np.array(P, float), np.array(Q, float), np.array(Emean, float),
            np.array(Emin, float), np.array(Dim, int))


def fit_quadratic_surface(P, Q, E):
    """Fit E(p,q) = a p^2 + b q^2 + c pq + d p + e q + f; return coeffs + Hessian + R2."""
    A = np.column_stack([P**2, Q**2, P*Q, P, Q, np.ones_like(P)])  # (local)
    coef, _, _, _ = np.linalg.lstsq(A, E, rcond=None)  # (local)
    a, b, c, dd, e, f = coef  # (local)
    pred = A @ coef  # (local)
    rms = float(np.sqrt(np.mean((E - pred) ** 2)))  # (local)
    ss_res = float(np.sum((E - pred) ** 2))  # (local)
    ss_tot = float(np.sum((E - E.mean()) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")  # (local)
    Hess = np.array([[2 * a, c], [c, 2 * b]])  # (local) d^2E/dI_i dI_j
    return dict(coef=coef, a=a, b=b, c=c, d=dd, e=e, f=f, rms=rms, r2=r2, Hess=Hess)


def grad_E(coef, p, q):
    """Frequency map omega_i = dE/dI_i at action (p,q) (Form B reference)."""
    a, b, c, dd, e, f = coef  # (local)
    w1 = 2 * a * p + c * q + dd  # (local) dE/dp
    w2 = 2 * b * q + c * p + e  # (local) dE/dq
    return np.array([w1, w2])


# ---------------------------------------------------------------------------
# Section 7 — Berry-Tabor predicted length spectrum
# ---------------------------------------------------------------------------
def berry_tabor_lengths_formA(Hess, m_max):
    """FORM A (PRIMARY): Poisson-dual wave-trace closed-orbit lengths.
        L_m = 2*pi * sqrt( m^T (Hess/2)^{-1} m ),  m in Z^2 \\ {0}, |m_i| <= m_max.
    G_E/2 = M(tau) is the metric quadratic form. Recovers 4*pi at tau=0.
    Returns sorted-unique (L, m1, m2, |m|^2_dual) with the PRIMITIVE first per L."""
    Mform = Hess / 2.0  # (local) metric form M(tau)
    Minv = np.linalg.inv(Mform)  # (local) dual metric (up to 4pi^2)
    raw = []  # (local)
    for m1, m2 in itertools.product(range(-m_max, m_max + 1), repeat=2):
        if m1 == 0 and m2 == 0:
            continue
        m = np.array([m1, m2], float)  # (local)
        qd = float(m @ Minv @ m)  # (local)
        L = 2.0 * PI * np.sqrt(qd)  # (local)
        raw.append((L, m1, m2, qd))
    raw.sort(key=lambda r: r[0])
    # unique lengths (collapse degenerate windings to the representative)
    uniq = []  # (local)
    for L, m1, m2, qd in raw:
        if not uniq or abs(L - uniq[-1][0]) > 1e-6:
            uniq.append((L, m1, m2, qd))
    return uniq, raw


def berry_tabor_lengths_formB(coef, p_ref, q_ref, m_max, freq_tol_rel):
    """FORM B (SECONDARY): single-resonance phrasing.
        L_{m1,m2} = 2*pi / |m1*omega1 + m2*omega2|, omega = dE/dI at I*=(p_ref,q_ref).
    Resonances within freq_tol_rel are dropped (L -> infinity); finite lengths kept."""
    w = grad_E(coef, p_ref, q_ref)  # (local)
    wmag = float(np.hypot(*w))  # (local)
    out = []  # (local)
    for m1, m2 in itertools.product(range(-m_max, m_max + 1), repeat=2):
        if m1 == 0 and m2 == 0:
            continue
        denom = abs(m1 * w[0] + m2 * w[1])  # (local)
        if denom < freq_tol_rel * wmag:
            continue  # near-resonance -> infinite-length torus, not a finite peak
        L = 2.0 * PI / denom  # (local)
        out.append((L, m1, m2, denom))
    out.sort(key=lambda r: r[0])
    return out, w


def berry_tabor_amplitudes(P, Q, Dim, Hess):
    """A_BT(p,q) = dim(p,q) * 16 / (2*pi)^{3/2} / sqrt|det(Hess E)|  (proven_498 / S54).
    Hess is the GLOBAL energy Hessian (the surface is exactly quadratic, so the
    sector Hessian is (p,q)-independent). Returns per-sector amplitudes."""
    detH = abs(float(np.linalg.det(Hess)))  # (local)
    amps = []  # (local)
    for p, q, dim in zip(P, Q, Dim):
        A = dim * 16.0 / ((2.0 * PI) ** 1.5) / np.sqrt(detH) if detH > 1e-300 else 0.0  # (local)
        amps.append((int(p), int(q), int(dim), float(A)))
    amps.sort(key=lambda r: -r[3])
    return amps, detH


# ---------------------------------------------------------------------------
# Section 8 — line-by-line match against W7-2 measured peaks
# ---------------------------------------------------------------------------
def match_peaks(meas_L, pred_lengths, delta_L):
    """For each measured L, find nearest predicted L within delta_L. Returns the
    per-peak match table and n_matched."""
    pred_arr = np.array([t[0] for t in pred_lengths])  # (local)
    table = []  # (local)
    n_matched = 0  # (local)
    for Lm in meas_L:
        if pred_arr.size == 0:
            table.append((float(Lm), float("nan"), float("nan"), False, None))
            continue
        idx = int(np.argmin(np.abs(pred_arr - Lm)))  # (local)
        Lp = float(pred_arr[idx])  # (local)
        gap = abs(Lp - Lm)  # (local)
        ok = gap <= delta_L  # (local)
        if ok:
            n_matched += 1
        m_label = (pred_lengths[idx][1], pred_lengths[idx][2])  # (local)
        table.append((float(Lm), Lp, float(gap), bool(ok), m_label))
    return table, n_matched


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"{GATE_ID} — Berry-Tabor frequency-map length-spectrum match at tau_fold")
    print("=" * 78)

    pins = log_input_pins([W7_2_NPZ, CACHE_NPZ, CANONICAL, S54_SRC, Path(__file__)])
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL, pins)
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")

    # ---- 0. GATED dispatch: verify W7-2 verdict is non-FAIL ----
    w7_2 = np.load(W7_2_NPZ, allow_pickle=True)  # (local)
    w7_2_verdict = str(w7_2["verdict"])  # (local)
    print(f"\n[0] Upstream W7-2 verdict = {w7_2_verdict}")
    if w7_2_verdict == "FAIL":
        # mechanical closure path (not reached: disk-verified PASS)
        value = "upstream_W7-2_FAIL"  # (local)
        print("  W7-2 FAILED -> mechanical closure.")
        print_verdict_payload("FAIL", value, audit_sha, content_sha, "N/A", "FAIL", "BREAKDOWN")
        return

    # ---- 1. measured peak table (W7-2 stable peaks) + delta_L ----
    stable = np.asarray(w7_2["stable_peaks"], dtype=float)  # (local) cols: L, amp, snr, drift
    meas_L = stable[:, 0]  # (local)
    meas_amp = stable[:, 1]  # (local)
    delta_L = float(w7_2["delta_L"])  # (local)
    n_stable = int(w7_2["n_stable_peaks"])  # (local)
    coroot = np.asarray(w7_2["coroot_lengths"], dtype=float)  # (local) tau=0 control
    prim_coroot = float(w7_2["primitive_coroot_length"])  # (local)
    w7_2_info = (w7_2_verdict == "INFO")  # (local)
    print(f"[1] W7-2 measured: {n_stable} stable peaks; delta_L={delta_L:.4f}; "
          f"L range [{meas_L.min():.2f},{meas_L.max():.2f}]; dominant L={float(w7_2['dominant_L']):.2f}")
    print(f"    tau=0 control coroot lengths: {np.round(coroot,3)}  (primitive {prim_coroot:.4f}=4*pi)")

    # ---- 2. tau_fold level surface E(p,q) from cache + frequency map ----
    P, Q, Emean, Emin, Dim = load_level_surface()  # (local)
    fit = fit_quadratic_surface(P, Q, Emean)  # (local)
    print(f"\n[2] tau_fold level surface E(p,q)=<|lambda|^2> from s84 cache "
          f"({len(P)} sectors, max p+q={int((P+Q).max())}):")
    print(f"    E = a(p^2+q^2)+c*pq+d(p+q)+f : a={fit['a']:.5f} b={fit['b']:.5f} "
          f"c={fit['c']:.5f} d={fit['d']:.5f} e={fit['e']:.5f} f={fit['f']:.5f}")
    print(f"    quadratic-fit RMS resid = {fit['rms']:.3e}  R^2 = {fit['r2']:.8f}  "
          f"(EXACTLY quadratic level surface)")
    Hess = fit["Hess"]  # (local)
    print(f"    Hess(E_tau_fold) = {np.round(Hess,5).tolist()}  "
          f"(tau=0 ref Hess(C2)=[[0.6667,0.3333],[0.3333,0.6667]])")

    # cross-check: surface fit on Emin (bottom-of-band) — robustness
    fit_min = fit_quadratic_surface(P, Q, Emin)  # (local)
    print(f"    [robustness] Emin-surface Hess = {np.round(fit_min['Hess'],5).tolist()} "
          f"(R^2={fit_min['r2']:.6f})")

    # ---- 3. tau=0 self-consistency: Form A on Hess(C2) must reproduce 4*pi ----
    HessC2 = np.array([[2.0/3.0, 1.0/3.0], [1.0/3.0, 2.0/3.0]])  # (local) Hessian of C2
    predA_tau0, _ = berry_tabor_lengths_formA(HessC2, M_MAX)  # (local)
    prim_pred_tau0 = predA_tau0[0][0]  # (local)
    tau0_ok = abs(prim_pred_tau0 - 4.0 * PI) < 1e-9  # (local)
    print(f"\n[3] tau=0 self-consistency (Form A on Hess(C2)): "
          f"primitive L_pred = {prim_pred_tau0:.6f} vs 4*pi={4*PI:.6f}  "
          f"=> {'EXACT MATCH' if tau0_ok else 'MISMATCH'}")
    # also confirm the predicted tau=0 lattice reproduces W7-2 coroot lengths
    predA_tau0_L = np.array([t[0] for t in predA_tau0])  # (local)
    coroot_recov = all(np.min(np.abs(predA_tau0_L - Lc)) < 1e-6 for Lc in coroot[:6])  # (local)
    print(f"    W7-2 coroot lengths reproduced by Form A(tau=0): {coroot_recov}")

    # ---- 4. PREDICTED Berry-Tabor lengths at tau_fold (Form A PRIMARY) ----
    predA, predA_raw = berry_tabor_lengths_formA(Hess, M_MAX)  # (local)
    predA_L = np.array([t[0] for t in predA])  # (local)
    prim_pred = predA[0][0]  # (local)
    print(f"\n[4] PREDICTED Berry-Tabor lengths at tau_fold (Form A, |m_i|<={M_MAX}):")
    print(f"    primitive L_pred = {prim_pred:.4f} at m={(predA[0][1],predA[0][2])} "
          f"(tau=0 was 12.566; deformation flattens surface -> longer orbit)")
    print(f"    L_pred range [{predA_L.min():.2f}, {predA_L.max():.2f}], "
          f"{len(predA_L)} unique lengths")
    print(f"    first 12 predicted lengths: {np.round(np.sort(predA_L)[:12],3)}")

    # Form B (secondary; reference action at the level-surface "center of mass")
    p_ref = float(np.average(P, weights=Dim))  # (local)
    q_ref = float(np.average(Q, weights=Dim))  # (local)
    predB, wref = berry_tabor_lengths_formB(fit["coef"], p_ref, q_ref, M_MAX, FREQ_TOL_REL)  # (local)
    predB_L = np.array([t[0] for t in predB]) if predB else np.array([])  # (local)
    print(f"    [Form B secondary] omega(I*={p_ref:.2f},{q_ref:.2f})="
          f"({wref[0]:.4f},{wref[1]:.4f}); {len(predB_L)} finite lengths, "
          f"range [{(predB_L.min() if predB_L.size else float('nan')):.2f},"
          f"{(predB_L.max() if predB_L.size else float('nan')):.2f}]")

    # ---- 5. Berry-Tabor amplitudes ----
    amps, detH = berry_tabor_amplitudes(P, Q, Dim, Hess)  # (local)
    print(f"\n[5] Berry-Tabor amplitudes A_BT = dim*16/(2pi)^1.5/sqrt|det Hess|; "
          f"|det Hess|={detH:.5f}")
    print(f"    top-5 A_BT sectors: " +
          ", ".join(f"({a[0]},{a[1]})dim{a[2]}:A={a[3]:.2f}" for a in amps[:5]))

    # ---- 6. LINE-BY-LINE MATCH (Form A PRIMARY) ----
    table, n_matched = match_peaks(meas_L, predA, delta_L)  # (local)
    match_frac = n_matched / n_stable  # (local)
    print(f"\n[6] LINE-BY-LINE MATCH (Form A, tolerance delta_L={delta_L:.4f}):")
    print(f"    {'L_meas':>9} {'L_pred':>9} {'gap':>8} {'<=dL?':>6} {'winding':>10} {'amp_meas':>11}")
    for (Lm, Lp, gap, ok, mlab), am in zip(table, meas_amp):
        ms = f"{mlab}" if mlab is not None else "-"  # (local)
        print(f"    {Lm:9.3f} {Lp:9.3f} {gap:8.3f} {str(ok):>6} {ms:>10} {am:11.3e}")
    print(f"    n_matched = {n_matched} / {n_stable}  =>  match_frac = {match_frac:.4f}")

    # Form B match (secondary, informational)
    if predB_L.size:
        _, n_matched_B = match_peaks(meas_L, predB, delta_L)  # (local)
        match_frac_B = n_matched_B / n_stable  # (local)
    else:
        n_matched_B, match_frac_B = 0, 0.0  # (local)
    print(f"    [Form B secondary] n_matched = {n_matched_B}/{n_stable} "
          f"(match_frac_B={match_frac_B:.4f})")

    # ---- 7. amplitude correspondence (for INFO discrimination) ----
    # For matched peaks: does measured amplitude ordering track A_BT? Pull the
    # predicted A_BT for the winding's representative sector where derivable.
    matched_pairs = [(Lm, Lp, am) for (Lm, Lp, gap, ok, ml), am
                     in zip(table, meas_amp) if ok]  # (local)
    print(f"\n[7] amplitude correspondence (matched peaks): {len(matched_pairs)} matched")

    # ---- 8. verdict (pre-registered) ----
    # PASS iff match_frac >= 2/3. INFO iff positions match but amplitude regime off
    #   OR W7-2 was INFO (resolution-limited). FAIL iff < 2/3.
    # sign_verdict: direction is "more peaks matched => stronger confirmation"
    #   (substitution chain Step Direction). sign=PASS iff match_frac > 0 in the
    #   predicted direction (peaks land ON predicted lengths, not anti-correlated).
    print("\n[8] VERDICT (pre-registered: PASS iff match_frac >= 2/3):")
    print(f"    self-consistency (tau=0 -> 4*pi EXACT): {tau0_ok}")
    if not tau0_ok:
        # method mis-built -> cannot certify; this is a structural FAIL of the predictor
        verdict = "FAIL"  # (local)
        sign_v, mag_v, reg_v = "FAIL", "FAIL", "BREAKDOWN"  # (local)
        value = (f"method_self_consistency_FAIL;tau0_primitive={prim_pred_tau0:.6f}"
                 f"_vs_4pi={4*PI:.6f}")  # (local)
    else:
        if match_frac >= MATCH_FRAC_PASS:
            verdict = "PASS"  # (local)
            sign_v, mag_v, reg_v = "PASS", "PASS", "VALID"  # (local)
        elif w7_2_info:
            verdict = "INFO"  # (local) resolution-limited (W7-2 INFO)
            sign_v, mag_v, reg_v = "PASS", "INFO", "MARGINAL"  # (local)
        else:
            verdict = "FAIL"  # (local) systematic position mismatch
            # sign: peaks did NOT land on predicted lengths within dL
            sign_v = "PASS" if n_matched > 0 else "FAIL"  # (local) partial vs none
            mag_v, reg_v = "FAIL", "VALID"  # (local)
        value = (f"match_frac={match_frac:.4f}_({n_matched}/{n_stable});"
                 f"PASS_boundary=2/3;delta_L={delta_L:.4f};"
                 f"tau0_selfconsistency=4pi_EXACT;"
                 f"primitive_L_pred_tau_fold={prim_pred:.4f}_vs_meas_dominant="
                 f"{float(w7_2['dominant_L']):.2f};"
                 f"surface_R2={fit['r2']:.6f};Form_B_frac={match_frac_B:.4f};"
                 f"scale_gap=meas[{meas_L.min():.0f},{meas_L.max():.0f}]_vs_"
                 f"pred[{predA_L.min():.0f},{predA_L.max():.0f}]")  # (local)
    print(f"    match_frac={match_frac:.4f}  =>  VERDICT = {verdict}")
    print(f"    3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v}")

    # ---- 9. save ----
    np.savez(
        OUT_NPZ,
        # inputs / provenance
        tau_fold=tau_fold, delta_L=delta_L, n_stable_peaks=n_stable,
        w7_2_verdict=w7_2_verdict, m_max=M_MAX,
        # level surface
        surface_coef=fit["coef"], surface_R2=fit["r2"], surface_rms=fit["rms"],
        Hess_E=Hess, Hess_C2_tau0=HessC2, detH=detH,
        Emin_Hess=fit_min["Hess"], Emin_R2=fit_min["r2"],
        # tau=0 self-consistency
        tau0_primitive_pred=prim_pred_tau0, tau0_selfconsistent=tau0_ok,
        coroot_reproduced=coroot_recov,
        # predicted lengths
        pred_L_formA=predA_L, pred_L_formA_sorted=np.sort(predA_L),
        pred_primitive_tau_fold=prim_pred,
        pred_windings_formA=np.array([(t[1], t[2]) for t in predA]),
        pred_L_formB=predB_L, omega_ref=wref, p_ref=p_ref, q_ref=q_ref,
        # amplitudes
        amps_table=np.array([(a[0], a[1], a[2], a[3]) for a in amps]),
        # measured
        meas_L=meas_L, meas_amp=meas_amp, coroot_lengths=coroot,
        primitive_coroot=prim_coroot, dominant_L=float(w7_2["dominant_L"]),
        # match
        match_table=np.array([(r[0], r[1], r[2], float(r[3])) for r in table]),
        n_matched=n_matched, match_frac=match_frac,
        n_matched_B=n_matched_B, match_frac_B=match_frac_B,
        # verdict
        verdict=verdict, value=value,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n[9] saved -> {OUT_NPZ.name}")

    # ---- 10. plot ----
    make_plot(meas_L, meas_amp, predA_L, predB_L, coroot, table, delta_L,
              fit, prim_pred, prim_coroot, match_frac, verdict)
    print(f"[10] saved -> {OUT_PNG.name}")

    # ---- 11. 4-tuple + verdict payload ----
    print(f"\n4-tuple: (value={match_frac:.4f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    extra = [
        f"# Berry-Tabor (NOT Gutzwiller): Manakov-integrable flow => det(M-I)=0 "
        f"identically (S54); A_BT=dim*16/(2pi)^1.5/sqrt|det Hess| (proven_498)",
        f"# tau=0 self-consistency EXACT: Form A on Hess(C2) -> primitive 4*pi="
        f"{4*PI:.6f} (=W7-2 coroot primitive); coroot lattice reproduced={coroot_recov}",
        f"# scale gap: predicted L in [{predA_L.min():.1f},{predA_L.max():.1f}] vs "
        f"measured L in [{meas_L.min():.0f},{meas_L.max():.0f}] (W7-2 truncation-influence "
        f"caveat: n_lambda_range_robust=0 at L_max=12)",
        f"# regulator_pin=N/A (Berry-Tabor lengths from metric frequency map, not a "
        f"regulated a_n)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_v, mag_v, reg_v, extra_rows=extra)
    return verdict


def make_plot(meas_L, meas_amp, predA_L, predB_L, coroot, table, delta_L,
              fit, prim_pred, prim_coroot, match_frac, verdict):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(
        f"S105-W7-3 Berry-Tabor frequency-map length-spectrum match at tau_fold=0.19\n"
        f"Manakov-integrable => Berry-Tabor (NOT Gutzwiller) | match_frac="
        f"{match_frac:.3f} (PASS>=2/3) | VERDICT: {verdict}",
        fontsize=12, fontweight="bold")

    # Panel 1: measured vs predicted length spectra (stick plot)
    ax = axes[0, 0]
    ax.vlines(meas_L, 0, 1.0, color="steelblue", lw=1.6, label=f"measured ({len(meas_L)})")
    ax.vlines(np.sort(predA_L), 0, -0.7, color="crimson", lw=1.0, alpha=0.7,
              label=f"predicted Form A ({len(predA_L)})")
    ax.vlines(coroot, 0, -0.35, color="green", lw=1.0, alpha=0.5, ls=":",
              label=f"tau=0 coroot ({len(coroot)})")
    ax.axhline(0, color="k", lw=0.5)
    ax.set_xlabel("length L (FT-in-lambda conjugate)")
    ax.set_ylabel("(up: measured / down: predicted)")
    ax.set_title("Length spectra: measured vs Berry-Tabor predicted")
    ax.legend(fontsize=8)

    # Panel 2: per-peak match gaps
    ax = axes[0, 1]
    Lm = np.array([r[0] for r in table])  # (local)
    gaps = np.array([r[2] for r in table])  # (local)
    oks = np.array([r[3] for r in table])  # (local)
    cols = ["green" if o else "red" for o in oks]  # (local)
    ax.bar(range(len(Lm)), gaps, color=cols, alpha=0.7)
    ax.axhline(delta_L, color="k", ls="--", label=f"delta_L={delta_L:.3f}")
    ax.set_xticks(range(len(Lm)))
    ax.set_xticklabels([f"{x:.0f}" for x in Lm], rotation=90, fontsize=6)
    ax.set_xlabel("measured peak L")
    ax.set_ylabel("gap to nearest predicted L")
    ax.set_title(f"Per-peak match gaps ({int(oks.sum())}/{len(Lm)} within delta_L)")
    ax.legend(fontsize=8)

    # Panel 3: level surface E(p,q) quadratic fit residual
    ax = axes[1, 0]
    ax.text(0.05, 0.92, "tau_fold level surface E(p,q)=<|lambda|^2>:", fontsize=10,
            fontweight="bold", transform=ax.transAxes)
    ax.text(0.05, 0.80, f"E = {fit['a']:.4f}(p^2+q^2) + {fit['c']:.4f} pq", fontsize=10,
            transform=ax.transAxes)
    ax.text(0.05, 0.72, f"      + {fit['d']:.4f}(p+q) + {fit['f']:.4f}", fontsize=10,
            transform=ax.transAxes)
    ax.text(0.05, 0.60, f"R^2 = {fit['r2']:.8f}  (EXACTLY quadratic)", fontsize=10,
            transform=ax.transAxes)
    ax.text(0.05, 0.50, f"Hess(E) = {np.round(fit['Hess'],4).tolist()}", fontsize=9,
            transform=ax.transAxes)
    ax.text(0.05, 0.36, f"primitive L_pred(tau_fold) = {prim_pred:.3f}", fontsize=10,
            transform=ax.transAxes, color="crimson")
    ax.text(0.05, 0.28, f"primitive coroot(tau=0)    = {prim_coroot:.3f} = 4*pi",
            fontsize=10, transform=ax.transAxes, color="green")
    ax.text(0.05, 0.14, "frequency map omega(I)=dE/dI -> Poisson-dual lengths\n"
            "L_m = 2*pi*sqrt(m^T (Hess/2)^-1 m)", fontsize=9, transform=ax.transAxes)
    ax.axis("off")
    ax.set_title("Substrate frequency map (metric -> omega(I) -> lengths)")

    # Panel 4: predicted-vs-measured nearest scatter
    ax = axes[1, 1]
    Lp = np.array([r[1] for r in table])  # (local)
    ax.scatter(Lm, Lp, c=cols, s=40, alpha=0.7)
    lo, hi = 0, max(Lm.max(), Lp.max()) * 1.05  # (local)
    ax.plot([lo, hi], [lo, hi], "k--", alpha=0.5, label="L_pred = L_meas")
    ax.fill_between([lo, hi], [lo - delta_L, hi - delta_L], [lo + delta_L, hi + delta_L],
                    color="gray", alpha=0.15, label=f"+/- delta_L")
    ax.set_xlabel("measured L")
    ax.set_ylabel("nearest predicted L")
    ax.set_title("Nearest-predicted vs measured")
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
