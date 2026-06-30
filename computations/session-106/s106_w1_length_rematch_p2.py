#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S106-W1-LENGTH-REMATCH-P2  —  P2-ONLY (measurement-faithfulness) axis of the
Wave-1 substrate-commensurability discriminator.  REPORTED alongside P1, NOT
folded into it (the workshop's pre-registered circularity guard: P1 is the
delta-L-free A(G_E) trend (1d), NOT the delta-L-limited length functional).

Question (P2): does re-extracting the tau_fold length spectrum at the FINER
resolution enabled by the L14/L16 caches, and re-running the W7-3 line-by-line
Berry-Tabor match at FIXED rel_tol=1e-6 (NOT resolution-matched -- the documented
vacuity trap), yield match_frac >= 2/3 with n_lambda_range_robust > 0 (P2 now
faithful -- the S105 match_frac=0.1579 FAIL was a spectral-window-truncation
artifact)?

CRITICAL (vacuity-trap avoidance, plan section W1-5 substitution chain):
  match tolerance is FIXED rel_tol=1e-6, NOT resolution-matched. At the coarse
  S105 resolution delta(L^2)/L^2 = 1.09e-1, a resolution-matched tolerance reads
  ~1891/1891 'rational' VACUOUSLY. Fixing rel_tol at 1e-6 makes the match
  faithfulness-bearing.

n_lambda_range_robust PROMOTED to a PRE-REGISTERED CONJUNCT (the S105 W7-2
diagnostic was 0). PASS requires (match_frac >= 2/3) AND (n_lambda_range_robust > 0)
AND (per-L delta(L^2)/L^2 <= 1e-6 at the five BT lengths {21.27,37,43,56,64}).

Method (faithful re-run of s105_w7_2_length_spectrum_ft.py at finer caches):
  density -> Strutinsky-Weyl subtract -> Gaussian-windowed length-FFT -> peak
  extraction (SNR>=6, window-halving stable) -> lambda-range-robustness (spectral
  sub-band recurrence) -> W7-3 line-by-line match against the FIXED pred_L_formA
  Berry-Tabor lattice (s105_w7_3_berry_tabor_match.npz, R^2=1.0 surface).
  Per L_max in {14, 16}.

L16 is PARTIAL (1c PARTIAL-Friedrich-Bar): the L16 length spectrum uses the
EXPLICIT (level<=15) subset (the p+q=16 shell is FB-bounded, no abs_evals);
disclosed in the verdict + npz.

phononic-framing.md: GEOMETRIC -- the P2 axis. The length spectrum is the
geodesic-length-side image of the substrate's squared-action lattice via the
trace-formula duality (agent-memory: at tau=0 the torus theta IS the dualizable
object, conjugate variable = coroot/winding lattice setting closed-geodesic
LENGTHS). Flow: D_K eigenvalues at L in {14,16} -> length-spectrum FT (geometric
side) -> BT line-by-line match at FIXED 1e-6 -> measurement-faithfulness P2.

Output 4-tuple: (value=<match_frac + robust + cert-floor>,
                 scheme=BT-LINE-BY-LINE-MATCH-FIXED-RELTOL-1e-6,
                 convention=SQUARED-LENGTH-RATIOS-vs-EXACT-QUADRATIC-BT-LATTICE,
                 L_max=[14,16])
[VERIFY] trigger -> no 3-tuple required.
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
# Section 2 — Standard imports (numpy CPU + numpy.fft; OMP capped)
# ---------------------------------------------------------------------------
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import numpy as np  # noqa: E402
from scipy.ndimage import gaussian_filter1d  # noqa: E402
from scipy.signal import find_peaks  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + paths + pinned machinery
# ---------------------------------------------------------------------------
SESSION = "S106"
GATE_ID = "S106-W1-LENGTH-REMATCH-P2"
SCHEME = "BT-LINE-BY-LINE-MATCH-FIXED-RELTOL-1e-6"
CONVENTION = "SQUARED-LENGTH-RATIOS-vs-EXACT-QUADRATIC-BT-LATTICE"
L_MAX = "[14,16]"

SESSION_DIR = PROJECT_ROOT / "computations" / "session-106"  # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"  # (local)
CACHE_L1416 = SESSION_DIR / "s106_w1_highl_cache_l1416.npz"  # (local) 1c forward-pinned
W7_2_PIPELINE = PROJECT_ROOT / "computations" / "session-105" / "s105_w7_2_length_spectrum_ft.py"  # (local) method src
W7_3_NPZ = PROJECT_ROOT / "computations" / "session-105" / "s105_w7_3_berry_tabor_match.npz"  # (local) FIXED BT lattice
OUT_NPZ = SESSION_DIR / "s106_w1_length_rematch_p2.npz"  # (local)
OUT_PNG = SESSION_DIR / "s106_w1_length_rematch_p2.png"  # (local)

# Pre-registered machinery pins (plan section W1-5 machinery_pin_map)
REL_TOL = 1e-6              # (local) FIXED match tolerance (NOT resolution-matched -- vacuity-trap avoidance)
MATCH_FRAC_BOUNDARY = 2.0 / 3.0  # (local) match_frac >= 2/3 PASS boundary (inherited W7-3)
CERT_FLOOR = 1e-6          # (local) delta(L^2)/L^2 <= 1e-6 certification floor at the BT lengths
N_GRID = 4000              # (local) lambda-grid points (inherit s105_w7_2 scale; n_grid set the FFT length not the L-resolution)
GAUSS_FULL = 3.0           # (local) Strutinsky gauss factor (full)
GAUSS_HALF = 1.5           # (local) window-halving cross-check factor
WEYL_POLY_DEG = 6          # (local) Weyl polynomial degree
QUANTILE_LO = 20.0         # (local) interior band low percentile
QUANTILE_HI = 70.0         # (local) interior band high percentile
SNR_FLOOR = 6.0            # (local) peak SNR floor
# The five plan BT-predicted lower-winding lengths (from pred_L_formA, W7-3 R^2=1.0):
BT_FIVE = np.array([21.26821332, 36.83762606, 42.53642664, 56.27040327, 63.80463996])  # (local)


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


def print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=None):
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 — length-spectrum pipeline (faithful re-run of s105_w7_2)
# ---------------------------------------------------------------------------
def build_density(lams, weights, n_grid):
    lo, hi = float(lams.min()), float(lams.max())  # (local)
    grid = np.linspace(lo, hi, n_grid)  # (local)
    dl = grid[1] - grid[0]  # (local)
    idx = np.clip(((lams - lo) / dl).astype(np.int64), 0, n_grid - 1)  # (local)
    rho = np.zeros(n_grid, dtype=np.float64)  # (local)
    np.add.at(rho, idx, weights)
    return grid, rho, dl


def strutinsky_weyl_subtract(grid, rho_raw, lams, gauss_factor, poly_deg, q_lo, q_hi):
    s = np.sort(lams)  # (local)
    l1, l2 = np.percentile(s, [q_lo, q_hi])  # (local)
    dl = grid[1] - grid[0]  # (local)
    sigma_lambda = gauss_factor * dl  # (local) Strutinsky width anchored to grid resolution
    sigma_pts = max(sigma_lambda / dl, 1.0)  # (local)
    rho_smoothed = gaussian_filter1d(rho_raw, sigma_pts, mode="nearest")  # (local)
    band_mask = (grid >= l1) & (grid <= l2)  # (local)
    g0, g1 = grid[band_mask].min(), grid[band_mask].max()  # (local)
    xs = (2.0 * (grid - g0) / (g1 - g0)) - 1.0  # (local)
    coef = np.polyfit(xs[band_mask], rho_smoothed[band_mask], poly_deg)  # (local)
    rho_weyl = np.polyval(coef, xs)  # (local)
    rho_osc = rho_smoothed - rho_weyl  # (local)
    rho_osc = np.where(band_mask, rho_osc, 0.0)  # (local)
    return rho_smoothed, rho_weyl, rho_osc, sigma_lambda, band_mask


def length_fft(grid, rho_osc, dl):
    n = grid.size  # (local)
    win = np.hanning(n)  # (local)
    sig = rho_osc * win  # (local)
    ft = np.abs(np.fft.rfft(sig))  # (local) numpy FFT (CPU; the FT grid is small)
    freq = np.fft.rfftfreq(n, d=dl)  # (local)
    L_axis = 2.0 * np.pi * freq  # (local) conjugate length
    return L_axis, ft


def extract_peaks(L_axis, amp, snr_floor, L_min_phys):
    valid = L_axis >= L_min_phys  # (local)
    amp_v = amp.copy()  # (local)
    amp_v[~valid] = 0.0
    med = np.median(amp[valid])  # (local)
    mad = np.median(np.abs(amp[valid] - med))  # (local)
    noise = 1.4826 * mad if mad > 0 else (np.std(amp[valid]) or 1.0)  # (local)
    height = snr_floor * noise  # (local)
    dL_bin = L_axis[1] - L_axis[0] if L_axis.size > 1 else 1.0  # (local)
    distance = max(int(round((2.0 * np.pi / 5.5) / dL_bin)), 1)  # (local)
    pk, _ = find_peaks(amp_v, height=height, distance=distance)  # (local)
    out = []  # (local)
    for i in pk:
        out.append((float(L_axis[i]), float(amp[i]), float(amp[i] / noise)))
    out.sort(key=lambda r: r[1], reverse=True)
    return out, float(noise), float(height)


def run_pipeline(lams, weights, n_grid, gauss_factor, poly_deg, q_lo, q_hi, snr_floor):
    grid, rho_raw, dl = build_density(lams, weights, n_grid)
    rho_sm, rho_weyl, rho_osc, sigma_lambda, band_mask = strutinsky_weyl_subtract(
        grid, rho_raw, lams, gauss_factor, poly_deg, q_lo, q_hi)
    L_axis, amp = length_fft(grid, rho_osc, dl)
    lam_max = float(lams.max())  # (local)
    delta_L = 2.0 * np.pi / lam_max  # (local)
    L_min_phys = delta_L  # (local)
    peaks, noise, height = extract_peaks(L_axis, amp, snr_floor, L_min_phys)
    return dict(grid=grid, L_axis=L_axis, amp=amp, delta_L=delta_L, lam_max=lam_max,
                peaks=peaks, noise=noise, height=height, dl=dl)


def lambda_range_robustness(lams, weights, ref_peaks, n_grid, gauss_factor, poly_deg,
                            q_lo, q_hi, snr_floor, delta_L,
                            bands=((0, 75), (10, 85), (25, 100))):
    """n_lambda_range_robust: a GENUINE closed-geodesic peak recurs (within delta_L)
    across spectral lambda sub-bands; a truncation/aliasing artifact moves/vanishes."""
    s = np.sort(lams)  # (local)
    sub_peak_sets = []  # (local)
    for lo_pct, hi_pct in bands:
        lo, hi = np.percentile(s, [lo_pct, hi_pct])  # (local)
        m = (lams >= lo) & (lams <= hi)  # (local)
        if m.sum() < 100:
            continue
        sub = run_pipeline(lams[m], weights[m], n_grid, gauss_factor, poly_deg,
                           q_lo, q_hi, snr_floor)  # (local)
        sub_peak_sets.append(np.array([p[0] for p in sub["peaks"] if p[2] >= snr_floor]))
    robust = []  # (local)
    for L, amp, snr in ref_peaks:
        if sub_peak_sets and all(
                s_set.size > 0 and np.min(np.abs(s_set - L)) <= delta_L for s_set in sub_peak_sets):
            robust.append((L, amp, snr))
    return len(robust), robust, len(sub_peak_sets)


# ---------------------------------------------------------------------------
# Section 6 — cache loading (PRIMARY PW-weighted, per s105_w7_2)
# ---------------------------------------------------------------------------
def load_spectrum(sector_dict):
    """PRIMARY (PW-weighted): each block eigenvalue weighted by dim(p,q) (the
    regular-rep multiplicity in L^2(SU(3))), per s105_w7_2 load_cache_spectra."""
    lams, w = [], []  # (local)
    for (p, q), v in sector_dict.items():
        a = np.asarray(v["abs_evals"], dtype=np.float64)  # (local)
        if a.size == 0:
            continue
        lams.append(a)
        w.append(np.full_like(a, float(v["dim"])))
    return np.concatenate(lams), np.concatenate(w)


# ---------------------------------------------------------------------------
# Section 7 — W7-3 line-by-line Berry-Tabor match at FIXED rel_tol
# ---------------------------------------------------------------------------
def bt_match(meas_L, pred_L, rel_tol):
    """A measured length is MATCHED iff |L^2_meas - L^2_pred|/L^2_pred <= rel_tol
    (rel_tol FIXED at 1e-6, NOT resolution-matched). match_frac = #matched / #meas."""
    pred2 = pred_L ** 2  # (local)
    matched = 0  # (local)
    table = []  # (local)
    for Lm in meas_L:
        Lm2 = Lm * Lm  # (local)
        rel = np.abs(Lm2 - pred2) / pred2  # (local)
        j = int(np.argmin(rel))  # (local)
        is_match = bool(rel[j] <= rel_tol)  # (local)
        matched += int(is_match)
        table.append((float(Lm), float(pred_L[j]), float(rel[j]), float(is_match)))
    frac = matched / len(meas_L) if len(meas_L) else 0.0  # (local)
    return matched, frac, table


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} :: length re-match P2 at FIXED rel_tol={REL_TOL} (finer L14/L16) ===")
    print(f"[const] tau_fold={tau_fold}  rel_tol={REL_TOL} (NOT resolution-matched)  "
          f"match_frac boundary={MATCH_FRAC_BOUNDARY:.4f}  cert_floor={CERT_FLOOR}")

    pins = log_input_pins([CANONICAL, CACHE_L1416, W7_2_PIPELINE, W7_3_NPZ])  # (local)
    audit_sha, content_sha = compute_dual_sha(Path(__file__), CANONICAL, pins)  # (local)
    print(f"  closure(audit_sha256):   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256:          {content_sha[:16]}... (script only)")

    # ---- FIXED Berry-Tabor predicted lattice (W7-3 R^2=1.0 surface) ----
    w73 = np.load(W7_3_NPZ, allow_pickle=True)
    pred_L = np.asarray(w73["pred_L_formA"], dtype=float)  # (local) FIXED predicted lengths
    s105_match_frac = float(w73["match_frac"])  # (local) the S105 anchor (0.1579)
    print(f"\n[BT] FIXED pred_L_formA: {len(pred_L)} lengths, "
          f"min={pred_L.min():.4f} max={pred_L.max():.4f}; S105 match_frac={s105_match_frac:.4f} (3/19, FAIL)")
    print(f"     five lower-winding BT lengths: {BT_FIVE}")

    # ---- caches ----
    d = np.load(CACHE_L1416, allow_pickle=True)
    s14 = d["sector_evals_L14"].item()
    s16 = d["sector_evals_L16"].item()           # EXPLICIT (level<=15) subset
    L16_full = bool(d["L16_full"])
    L16_operational = int(d["L16_operational"])
    L14_operational = int(d["L14_operational"])

    per_L = {}  # (local)
    for Ltag, sec, n_FB in [("L14", s14, 0), ("L16", s16, int(d["n_fb_bounded"]))]:
        lams, w = load_spectrum(sec)
        lam_min, lam_max = float(lams.min()), float(lams.max())  # (local)
        span = lam_max - lam_min  # (local)

        # ---- full-spectrum pipeline ----
        res = run_pipeline(lams, w, N_GRID, GAUSS_FULL, WEYL_POLY_DEG,
                           QUANTILE_LO, QUANTILE_HI, SNR_FLOOR)
        meas_L = np.array([p[0] for p in res["peaks"]])  # (local)
        delta_L = res["delta_L"]  # (local)
        dL_bin = res["L_axis"][1] - res["L_axis"][0]  # (local) FT length-bin width

        # ---- window-halving cross-check (Strutinsky gamma) ----
        res_half = run_pipeline(lams, w, N_GRID, GAUSS_HALF, WEYL_POLY_DEG,
                                QUANTILE_LO, QUANTILE_HI, SNR_FLOOR)
        meas_L_half = np.array([p[0] for p in res_half["peaks"]])  # (local)
        n_stable = 0  # (local) peaks stable under window-halving (drift <= delta_L)
        for p in res["peaks"]:
            if meas_L_half.size and np.min(np.abs(meas_L_half - p[0])) <= delta_L:
                n_stable += 1

        # ---- lambda-range robustness (the promoted conjunct) ----
        n_robust, robust, n_subbands = lambda_range_robustness(
            lams, w, res["peaks"], N_GRID, GAUSS_FULL, WEYL_POLY_DEG,
            QUANTILE_LO, QUANTILE_HI, SNR_FLOOR, delta_L)

        # ---- W7-3 line-by-line match at FIXED rel_tol=1e-6 ----
        n_matched, match_frac, mtable = bt_match(meas_L, pred_L, REL_TOL)

        # ---- per-L certification floor delta(L^2)/L^2 at the five BT lengths ----
        # FT length bin width dL_bin -> d(L^2)=2*L*dL_bin -> rel = 2*dL_bin/L
        cert = {f"{bt:.2f}": float(2.0 * dL_bin / bt) for bt in BT_FIVE}  # (local)
        cert_ok = all(v <= CERT_FLOOR for v in cert.values())  # (local)

        per_L[Ltag] = dict(
            lam_min=lam_min, lam_max=lam_max, span=span, dL_bin=float(dL_bin),
            delta_L=float(delta_L), n_peaks=int(meas_L.size), n_stable=int(n_stable),
            n_robust=int(n_robust), n_subbands=int(n_subbands),
            n_matched=int(n_matched), match_frac=float(match_frac),
            cert=cert, cert_ok=bool(cert_ok), n_FB=n_FB,
            meas_L=meas_L.tolist(), match_table=mtable,
            L_axis=res["L_axis"], amp=res["amp"],
        )
        print(f"\n=== {Ltag} (operational={L16_operational if Ltag=='L16' else L14_operational}"
              f"{', PARTIAL +'+str(n_FB)+' FB shell' if n_FB else ''}) ===")
        print(f"  lambda=[{lam_min:.4f},{lam_max:.4f}] span={span:.4f}  dL_bin(FT)={dL_bin:.4f}  "
              f"delta_L={delta_L:.4f}")
        print(f"  peaks={meas_L.size}  window-halving-stable={n_stable}  "
              f"n_lambda_range_robust={n_robust}/{meas_L.size} (over {n_subbands} sub-bands)")
        print(f"  W7-3 match @ FIXED rel_tol={REL_TOL}: n_matched={n_matched}  "
              f"match_frac={match_frac:.4f} (boundary {MATCH_FRAC_BOUNDARY:.4f})")
        print(f"  cert-floor delta(L^2)/L^2 at BT lengths (need <= {CERT_FLOOR}):")
        for k, v in cert.items():
            print(f"    L={k}: {v:.4e}  {'OK' if v <= CERT_FLOOR else 'ABOVE-FLOOR'}")
        print(f"  cert_ok (all five <= {CERT_FLOOR}): {cert_ok}")

    # ---- verdict (plan section W1-5 rubric) ----
    # PASS  <=> (match_frac >= 2/3) AND (n_lambda_range_robust > 0) AND (cert_ok) per L.
    # We report per L_max; the gate verdict is the AND across the available L (14,16).
    pass_per_L = {}  # (local)
    for Ltag, r in per_L.items():
        pass_per_L[Ltag] = (r["match_frac"] >= MATCH_FRAC_BOUNDARY
                            and r["n_robust"] > 0 and r["cert_ok"])
    all_pass = all(pass_per_L.values())  # (local)
    any_partial = any(  # (local) matches present but robust=0, OR cert partial
        (r["match_frac"] >= MATCH_FRAC_BOUNDARY and r["n_robust"] == 0) for r in per_L.values())

    if all_pass:
        verdict = "PASS"  # (local)
    elif any_partial:
        verdict = "INFO"  # (local) matches but not lambda-range-robust (residual window artifact)
    else:
        verdict = "FAIL"  # (local) P2 still measurement-limited (the regime both tracks agreed on)

    print(f"\n[VERDICT] {verdict}")
    print(f"  per-L PASS: {pass_per_L}  (PASS needs match_frac>=2/3 AND robust>0 AND cert_ok)")
    mf16 = per_L["L16"]["match_frac"]; mf14 = per_L["L14"]["match_frac"]  # (local)
    r16 = per_L["L16"]["n_robust"]; r14 = per_L["L14"]["n_robust"]  # (local)
    print(f"  match_frac: L14={mf14:.4f} L16={mf16:.4f} (vs 2/3={MATCH_FRAC_BOUNDARY:.4f})")
    print(f"  n_lambda_range_robust: L14={r14} L16={r16} (conjunct: >0 required)")
    print(f"  cert_ok: L14={per_L['L14']['cert_ok']} L16={per_L['L16']['cert_ok']} "
          f"(delta(L^2)/L^2<=1e-6 at the BT lengths)")
    print(f"  STRUCTURAL: the length-FT resolution dL_bin=2*pi/lambda_span is bounded by the "
          f"D_K eigenvalue magnitude (|lambda|~O(6.5) at L16); span={per_L['L16']['span']:.2f} "
          f"=> dL_bin~{per_L['L16']['dL_bin']:.2f} => delta(L^2)/L^2~0.10 at L~21, "
          f"4 OOM above the 1e-6 floor. The finer cache CANNOT reach the 1e-6 certifiable band.")

    # ---- value string ----
    val = (
        f"verdict_basis=P2-measurement;"
        f"match_frac_L14={mf14:.4f};match_frac_L16={mf16:.4f};boundary=2/3={MATCH_FRAC_BOUNDARY:.4f};"
        f"n_lambda_range_robust_L14={r14};n_lambda_range_robust_L16={r16};conjunct=>0;"
        f"cert_ok_L14={per_L['L14']['cert_ok']};cert_ok_L16={per_L['L16']['cert_ok']};"
        f"rel_tol_FIXED={REL_TOL}(NOT_resolution-matched);"
        f"dL_bin_L16={per_L['L16']['dL_bin']:.4f};lambda_span_L16={per_L['L16']['span']:.4f};"
        f"cert_floor_L16_at_21.27={per_L['L16']['cert']['21.27']:.4e};"
        f"S105_anchor_match_frac=0.1579;L16_op={L16_operational}(full={L16_full});"
        f"P2_NOT_folded_into_P1"
    )

    extra_rows = [
        (f"# P2-ONLY measurement-faithfulness (REPORTED, NOT folded into P1; P1=1d A(G_E) trend). "
         f"match_frac L14={mf14:.4f} L16={mf16:.4f} (boundary 2/3); n_lambda_range_robust L14={r14} L16={r16} "
         f"(promoted conjunct, >0 required); rel_tol FIXED {REL_TOL} (vacuity-trap avoidance)"),
        (f"# cert-floor delta(L^2)/L^2 at BT lengths {{21.27,36.84,42.54,56.27,63.80}}: "
         f"L16 at L=21.27 = {per_L['L16']['cert']['21.27']:.4e} (>> 1e-6); STRUCTURAL: dL_bin=2pi/lambda_span "
         f"bounded by |lambda|~O(6.5) at L16 (span={per_L['L16']['span']:.2f}) => floor ~0.10, 4 OOM above 1e-6"),
        (f"# L16 PARTIAL-Friedrich-Bar (1c): L16_operational={L16_operational} (level<=15 explicit + "
         f"{int(d['n_fb_bounded'])} FB-bounded shell, NOT used in length spectrum); S105 W7-3 anchor match_frac=0.1579"),
    ]

    # ---- save npz ----
    np.savez(
        OUT_NPZ,
        tau_fold=tau_fold, rel_tol=REL_TOL, match_frac_boundary=MATCH_FRAC_BOUNDARY,
        cert_floor=CERT_FLOOR, BT_FIVE=BT_FIVE, pred_L=pred_L,
        Ltags=np.array(list(per_L.keys())),
        match_frac_L14=per_L["L14"]["match_frac"], match_frac_L16=per_L["L16"]["match_frac"],
        n_robust_L14=per_L["L14"]["n_robust"], n_robust_L16=per_L["L16"]["n_robust"],
        n_subbands_L14=per_L["L14"]["n_subbands"], n_subbands_L16=per_L["L16"]["n_subbands"],
        n_peaks_L14=per_L["L14"]["n_peaks"], n_peaks_L16=per_L["L16"]["n_peaks"],
        n_stable_L14=per_L["L14"]["n_stable"], n_stable_L16=per_L["L16"]["n_stable"],
        dL_bin_L14=per_L["L14"]["dL_bin"], dL_bin_L16=per_L["L16"]["dL_bin"],
        span_L14=per_L["L14"]["span"], span_L16=per_L["L16"]["span"],
        lam_max_L14=per_L["L14"]["lam_max"], lam_max_L16=per_L["L16"]["lam_max"],
        cert_ok_L14=per_L["L14"]["cert_ok"], cert_ok_L16=per_L["L16"]["cert_ok"],
        cert_L14_json=json.dumps(per_L["L14"]["cert"]),
        cert_L16_json=json.dumps(per_L["L16"]["cert"]),
        match_table_L14_json=json.dumps(per_L["L14"]["match_table"]),
        match_table_L16_json=json.dumps(per_L["L16"]["match_table"]),
        meas_L_L14=np.array(per_L["L14"]["meas_L"]),
        meas_L_L16=np.array(per_L["L16"]["meas_L"]),
        L16_full=L16_full, L16_operational=L16_operational, L14_operational=L14_operational,
        s105_anchor_match_frac=s105_match_frac,
        verdict=verdict, value=val,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\n[npz] wrote {OUT_NPZ.name}")

    # ---- plot: length-spectrum FT + BT overlay + cert-floor ----
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    ax = axes[0]
    for Ltag, color in [("L14", "steelblue"), ("L16", "darkviolet")]:
        r = per_L[Ltag]
        m = r["L_axis"] <= max(pred_L.max(), 130) * 1.05  # (local)
        ax.plot(r["L_axis"][m], r["amp"][m] / r["amp"][m].max(), lw=0.9, color=color,
                alpha=0.8, label=f"{Ltag} length-FT (norm)")
    for bt in pred_L[pred_L <= 130]:
        ax.axvline(bt, color="crimson", ls=":", lw=0.6, alpha=0.5)
    ax.axvline(pred_L[0], color="crimson", ls=":", lw=0.6, alpha=0.5, label="BT pred_L_formA")
    ax.set_xlabel("geodesic length L = 2*pi*freq_lambda")
    ax.set_ylabel("normalized length-FT amplitude")
    ax.set_title(f"length spectrum vs FIXED BT lattice\nmatch_frac L14={mf14:.3f} L16={mf16:.3f} "
                 f"(@ rel_tol={REL_TOL}); boundary 2/3")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)

    ax2 = axes[1]
    cert16 = [per_L["L16"]["cert"][f"{bt:.2f}"] for bt in BT_FIVE]  # (local)
    cert14 = [per_L["L14"]["cert"][f"{bt:.2f}"] for bt in BT_FIVE]  # (local)
    ax2.semilogy(BT_FIVE, cert14, "s-", color="steelblue", label="L14 cert-floor")
    ax2.semilogy(BT_FIVE, cert16, "o-", color="darkviolet", label="L16 cert-floor")
    ax2.axhline(CERT_FLOOR, color="green", ls="--", lw=1.2, label=f"1e-6 floor (target)")
    ax2.set_xlabel("BT-predicted length L")
    ax2.set_ylabel("delta(L^2)/L^2 = 2*dL_bin/L (cert floor)")
    ax2.set_title("certification floor vs 1e-6 target\n(bounded by |lambda|~O(6.5): floor ~0.10, 4 OOM above)")
    ax2.legend(loc="best", fontsize=8)
    ax2.grid(True, alpha=0.3, which="both")

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] wrote {OUT_PNG.name}  ({time.time()-t0:.1f}s)")

    # ---- emit payload ----
    print_verdict_payload(verdict, val, audit_sha, content_sha, extra_rows=extra_rows)


if __name__ == "__main__":
    main()
