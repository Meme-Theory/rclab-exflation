"""
S99-W4-KAPPA-ALT-OBSERVABLE-SCAN — Wave 4 kappa-determinacy scan (LOW leverage, Tier-3/4).

Gate-OBJECT: a determinacy / epistemic-status question (NON-PHONONIC) — does ANY
kappa-dependent substrate-IS observable, OTHER THAN the already-closed CGWB peak
FREQUENCY axis, land in a realized detector/measurement band, which would upgrade
kappa from CONSISTENCY-PINNED to INDEPENDENTLY-PINNED?

Substrate-first direction (NOT inverted): the substrate IS the dimensionless
spectral-IS observable (transit timescale, acoustic-emission period, relic
coherence time, fold/dephasing time — all read off the D_K spectrum at tau_fold).
kappa = M_KK^{-1} is the EMERGENT TRANSPORT KNOB mapping those dimensionless
substrate-IS quantities into laboratory seconds/Hz:
    D_K eigenvalues -> dimensionless substrate-IS observable -> (x kappa^p)
        -> laboratory seconds-scale image -> detector-band membership test.

Transport convention (VERIFIED against the S98 V.7 baseline f_obs(kappa_nat)=8.4835e+39 Hz):
    dimensionless FREQUENCY f_tilde (M_KK units)  ->  f_obs = f_tilde * (1/kappa)   [Hz]
    dimensionless TIME      t_tilde (M_KK units)  ->  t_obs = t_tilde * kappa        [s]
                                                       f_obs = (1/t_tilde) * (1/kappa) [Hz]
    1/kappa_nat = M_KK/hbar = 1.128612e+41 Hz (the M_KK frequency scale).
    CGWB peak (S98 V.7): f_tilde_peak = 0.075168 -> f_obs = 8.4835e+39 Hz (reproduced below).

CLOSED-axis baseline (excluded from this scan): S98-KAPPA-INDEP-FROM-CGWB-FREQ FAIL
(audit 10d31d0e): f_obs=8.4835e+39 Hz, member_of_any_band=False, nearest_horizon=
resonant_HF_ceiling_1e+11, nearest_gap=+28.929 dec ABOVE. The CGWB-FREQUENCY axis
supplies NO independent seconds-scale; any future independent kappa-pin must come
from a DIFFERENT observable -> this gate scans the COMPLEMENT set.

Flat-grid discipline (plan note): Omega_peak_grid is FLAT at 9.15e-5 across all 121
kappa (kappa-INDEPENDENT amplitude) — it is NOT a candidate. The kappa-VARYING image
is the frequency/time-scale axis; this scan enumerates frequency/time-scale-type
observables ONLY.

[SIGN] trigger: the directional claim under test is IN-BAND (>=1 complement
observable within a realized detector/measurement band => kappa INDEPENDENTLY-PINNED)
vs OUT-OF-BAND (every complement observable strictly outside all bands => kappa
stays CONSISTENCY-PINNED). The gate is OPEN between PASS / FAIL / INFO; never
iterated to PASS.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Canonical-constants import (MANDATORY; never hardcode)
# ---------------------------------------------------------------------------
sys.path.insert(0, "computations/_shared")
from canonical_constants import (  # noqa: E402
    M_KK_inv_seconds,      # kappa_nat = hbar/M_KK [s]  (S96; canonical, NOT superseded)
    dt_transit,            # characteristic transit timescale (dimensionless, M_KK units)
    T_acoustic,            # acoustic-emission period (dimensionless, M_KK units)
    tau_GGE_K_unit,        # relic / GGE coherence time (dimensionless, K-units)
    t_deph_over_t_transit, # dephasing-time / transit-time ratio (dimensionless)
)

# ---------------------------------------------------------------------------
# Section 2 — Identity (R3 gate-block fields)
# ---------------------------------------------------------------------------
SESSION = "S99"                                                    # (local)
GATE_ID = "S99-W4-KAPPA-ALT-OBSERVABLE-SCAN"                       # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "ABSOLUTE"                                            # (local)
L_MAX = "N/A"                                                      # (local) kappa-determinacy gate; no spectral truncation

# ---------------------------------------------------------------------------
# Section 3 — Input files (every file the script reads)
# ---------------------------------------------------------------------------
SCRIPT_PATH = Path("computations/session-99/s99_w4_kappa_alt_observable_scan.py")
CANONICAL_PATH = Path("computations/_shared/canonical_constants.py")
S97_OMEGAGW_NPZ = Path("computations/session-97/s97_omegagw_peak_height.npz")
S98_V7_VERDICTS = Path("computations/session-98/s98_gate_verdicts.txt")


def _sha256_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


# ---------------------------------------------------------------------------
# Section 4 — Dual-SHA (audit_sha256 / content_sha256) per S84+ schema
# ---------------------------------------------------------------------------
def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
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
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
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


# ===========================================================================
# Section 5 — Compute
# ===========================================================================
def main():
    print("=" * 78)
    print(f"{GATE_ID}  (NON-PHONONIC gate-object; substrate-IS underlying observables)")
    print("=" * 78)

    # ---- input SHAs logged in first lines of stdout (gate-verdicts.md) ----
    sha_script = _sha256_file(SCRIPT_PATH)        # (local)
    sha_canon = _sha256_file(CANONICAL_PATH)      # (local)
    sha_s97 = _sha256_file(S97_OMEGAGW_NPZ)       # (local)
    sha_s98v7 = _sha256_file(S98_V7_VERDICTS)     # (local)
    print(f"[input-sha] script              = {sha_script}")
    print(f"[input-sha] canonical_constants = {sha_canon}")
    print(f"[input-sha] s97_omegagw_npz     = {sha_s97}")
    print(f"[input-sha] s98_v7_verdicts     = {sha_s98v7}")

    # ---- load the kappa-grid + the closed-axis baseline numbers ----
    d = np.load(S97_OMEGAGW_NPZ, allow_pickle=True)
    kappa_grid = np.asarray(d["kappa_grid"], dtype=float)              # (local) 121 pts log [1e-20,1e-10]
    kappa_nat = float(d["kappa_nat"])                                  # (local) = M_KK_inv_seconds
    Omega_peak_grid = np.asarray(d["Omega_peak_grid"], dtype=float)    # (local) FLAT 9.15e-5 (NOT a candidate)
    f_peak_Hz_baseline = float(d["f_peak_Hz"])                         # (local) S98 V.7 CGWB peak: 8.4835e+39 Hz
    N_eval = int(kappa_grid.size)                                      # (local) = 121

    # canonical-vs-npz consistency cross-check on kappa_nat
    assert abs(kappa_nat - M_KK_inv_seconds) / M_KK_inv_seconds < 1e-12, \
        "kappa_nat (npz) disagrees with canonical M_KK_inv_seconds"
    inv_kappa_nat = 1.0 / kappa_nat                                    # (local) M_KK/hbar = 1.128612e+41 Hz (the M_KK freq scale)
    print(f"\nkappa_nat (= M_KK_inv_seconds) = {kappa_nat:.15e} s")
    print(f"1/kappa_nat (M_KK freq scale)  = {inv_kappa_nat:.6e} Hz")
    print(f"Omega_peak_grid flat?  min={Omega_peak_grid.min():.4e} max={Omega_peak_grid.max():.4e}"
          f"  spread={Omega_peak_grid.max()-Omega_peak_grid.min():.3e}  (kappa-INDEPENDENT amplitude)")

    # ---- Reproduce the CLOSED-axis baseline (CGWB peak FREQUENCY) ----
    # f_obs = f_tilde / kappa ; recover f_tilde_peak from the baseline npz value.
    f_tilde_peak = f_peak_Hz_baseline * kappa_nat                      # (local) dimensionless redshifted substrate freq
    f_obs_peak_recomputed = f_tilde_peak * inv_kappa_nat               # (local) must reproduce f_peak_Hz_baseline
    print(f"\n[closed-axis baseline reproduction]  f_tilde_peak={f_tilde_peak:.6f}"
          f"  ->  f_obs={f_obs_peak_recomputed:.4e} Hz  (S98 V.7 = {f_peak_Hz_baseline:.4e} Hz)")
    assert abs(f_obs_peak_recomputed - f_peak_Hz_baseline) / f_peak_Hz_baseline < 1e-9, \
        "closed-axis baseline reproduction failed"

    # cross-check S98 V.7 verdict line is present + carries the closed-axis tag
    v7_line = ""  # (local)
    try:
        for ln in S98_V7_VERDICTS.read_text(encoding="utf-8", errors="replace").splitlines():
            if ln.startswith("S98-KAPPA-INDEP-FROM-CGWB-FREQ:"):
                v7_line = ln
                break
    except OSError:
        v7_line = ""
    v7_present = v7_line.startswith("S98-KAPPA-INDEP-FROM-CGWB-FREQ:") and "FAIL" in v7_line  # (local)
    v7_audit = "10d31d0e8975bb866c13063c65d29652b94e67f1b7f030d5b60a42387912ac83"  # (local) closed-axis baseline audit
    v7_audit_matches = v7_audit in v7_line                                          # (local)
    print(f"[closed-axis baseline] S98 V.7 line present (FAIL)? {v7_present}; audit 10d31d0e matches? {v7_audit_matches}")

    # ---- Detector / measurement band UNION (S98 V.7 horizon union) ----
    # Realized GW detector bands [lo, hi] Hz (the same union S98 V.7 used).
    # NOTE: no realized NON-GW measurement band maps onto a kappa-set substrate
    # seconds-scale observable at this scale (the substrate timescales are all
    # M_KK-frequency-class; no laboratory clock/spectroscopy band reaches 1/kappa_nat).
    BANDS = {                                                          # (local)
        "PTA":          (1e-9, 1e-7),
        "LISA":         (1e-4, 1e-1),
        "LIGO_ET":      (1e1, 1e4),
        "resonant_HF":  (1e3, 1e11),   # resonant-HF ceiling 1e11 Hz (S98 V.7 nearest_horizon)
    }
    band_lo_global = min(lo for lo, hi in BANDS.values())             # (local) = 1e-9 Hz (PTA floor)
    band_hi_global = max(hi for lo, hi in BANDS.values())             # (local) = 1e+11 Hz (resonant-HF ceiling)
    print(f"\n[band union]  global floor = {band_lo_global:.1e} Hz (PTA);  global ceiling = {band_hi_global:.1e} Hz (resonant-HF)")

    def member_of_any_band(f_hz):
        """Return (in_any, nearest_band_name, nearest_log10_gap_to_band).
        gap > 0 => ABOVE the nearest band's relevant edge; gap < 0 => BELOW it; 0 => inside.
        """
        if not np.isfinite(f_hz) or f_hz <= 0:
            return False, "none", np.inf
        lg = np.log10(f_hz)  # (local)
        for name, (lo, hi) in BANDS.items():
            if lo <= f_hz <= hi:
                return True, name, 0.0
        # not in any band: report distance to the closest band EDGE (signed)
        best_name, best_gap = "none", np.inf  # (local)
        for name, (lo, hi) in BANDS.items():
            if f_hz > hi:
                gap = lg - np.log10(hi)        # (local) decades ABOVE this band's top edge
            elif f_hz < lo:
                gap = lg - np.log10(lo)        # (local) decades BELOW this band's bottom edge (negative)
            else:
                gap = 0.0  # (local)
            if abs(gap) < abs(best_gap):
                best_gap, best_name = gap, name
        return False, best_name, best_gap

    # ---- COMPLEMENT observable set (frequency/time-scale-type; NOT amplitude; NOT CGWB peak freq) ----
    # Each observable supplies a dimensionless frequency f_tilde (M_KK units) whose
    # laboratory image is f_obs = f_tilde * (1/kappa). For TIME-scale observables the
    # frequency image is f_obs = (1/t_tilde) * (1/kappa). We test BOTH the seconds-scale
    # (time) and Hz-scale (frequency) image where meaningful, and report the frequency
    # image for band membership (detector bands are frequency bands).
    t_deph = t_deph_over_t_transit * dt_transit                       # (local) dephasing time (dimensionless, M_KK units)
    observables = []                                                   # (local) list of (name, kind, f_tilde, description)
    # f_tilde = the dimensionless FREQUENCY in M_KK units (for a time t_tilde, f_tilde = 1/t_tilde)
    observables.append(("transit_timescale",   "time", 1.0 / dt_transit,
                        f"characteristic transit timescale dt_transit={dt_transit:.6e} (M_KK units)"))
    observables.append(("acoustic_period",     "time", 1.0 / T_acoustic,
                        f"acoustic-emission period T_acoustic={T_acoustic} (M_KK units)"))
    observables.append(("acoustic_frequency",  "freq", float(d["f_acoustic"]),
                        f"acoustic-emission frequency f_acoustic={float(d['f_acoustic'])} (M_KK units)"))
    observables.append(("relic_coherence_time","time", 1.0 / tau_GGE_K_unit,
                        f"relic/GGE coherence time tau_GGE_K_unit={tau_GGE_K_unit} (K-units, M_KK)"))
    observables.append(("dephasing_time",      "time", 1.0 / t_deph,
                        f"dephasing time t_deph=t_deph/t_transit*dt_transit={t_deph:.6e} (M_KK units)"))

    print("\n" + "-" * 78)
    print("COMPLEMENT observable set — seconds/Hz image AT kappa_nat (substrate-natural value)")
    print("-" * 78)
    print(f"{'observable':<24}{'kind':<6}{'f_tilde':>14}{'t_obs[s]':>14}{'f_obs[Hz]':>14}{'in-band?':>10}{'nearest(gap dec)':>22}")

    rows = []                                                          # (local) per-observable result rows at kappa_nat
    any_in_band_at_nat = False                                        # (local)
    names = []; f_obs_nat_arr = []; t_obs_nat_arr = []; in_band_nat_arr = []; nearest_gap_arr = []  # (local) arrays for npz/plot
    for name, kind, f_tilde, desc in observables:
        # seconds-scale (time) image: t_obs = t_tilde * kappa = (1/f_tilde) * kappa
        t_obs_nat = (1.0 / f_tilde) * kappa_nat                       # (local) [s]
        # frequency image: f_obs = f_tilde * (1/kappa)
        f_obs_nat = f_tilde * inv_kappa_nat                           # (local) [Hz]
        in_any, nb, gap = member_of_any_band(f_obs_nat)
        any_in_band_at_nat = any_in_band_at_nat or in_any
        rows.append((name, kind, f_tilde, t_obs_nat, f_obs_nat, in_any, nb, gap, desc))
        names.append(name); f_obs_nat_arr.append(f_obs_nat); t_obs_nat_arr.append(t_obs_nat)
        in_band_nat_arr.append(bool(in_any)); nearest_gap_arr.append(gap)
        print(f"{name:<24}{kind:<6}{f_tilde:>14.6e}{t_obs_nat:>14.4e}{f_obs_nat:>14.4e}"
              f"{str(in_any):>10}{nb+' ('+format(gap,'+.3f')+')':>22}")

    # ---- Sweep the FULL 121-pt kappa-grid: is band-membership reachable for ANY kappa in the candidate window? ----
    # The determinacy verdict keys on kappa_nat (the substrate-natural value); the
    # grid sweep is the DIAGNOSTIC for whether ANY kappa in [1e-20,1e-10] could land
    # any complement observable in-band (a reachability check, not the gate verdict).
    grid_any_in_band = np.zeros(N_eval, dtype=bool)                   # (local)
    # per-observable count of grid points landing in-band
    per_obs_grid_in_band_count = {}                                  # (local)
    for name, kind, f_tilde, desc in observables:
        cnt = 0  # (local)
        for ki in range(N_eval):
            f_obs_ki = f_tilde * (1.0 / kappa_grid[ki])               # (local) [Hz]
            ia, _, _ = member_of_any_band(f_obs_ki)
            if ia:
                cnt += 1
                grid_any_in_band[ki] = True
        per_obs_grid_in_band_count[name] = cnt
    n_grid_in_band = int(np.count_nonzero(grid_any_in_band))         # (local) # of kappa-grid pts with >=1 obs in-band
    print(f"\n[grid reachability over 121 kappa in [1e-20,1e-10]]  kappa-pts with >=1 complement obs in-band: {n_grid_in_band}/{N_eval}")
    for name in names:
        print(f"    {name:<24} in-band grid-pts: {per_obs_grid_in_band_count[name]}/{N_eval}")

    # ===================================================================
    # Section 6 — Gate evaluation (set-membership determinacy gate)
    # ===================================================================
    # PASS  iff count(O_i(kappa_nat) in-band) >= 1  => kappa INDEPENDENTLY-PINNED.
    # FAIL  iff 0 in-band at kappa_nat AND no marginal (within 0.30 dec of a band edge).
    # INFO  iff 0 in-band at kappa_nat but >=1 observable is MARGINAL (|gap| <= 0.30 dec of a band edge).
    count_in_band_nat = int(sum(1 for r in rows if r[5]))            # (local)
    MARGINAL_DEC = 0.30                                               # (local) marginal-membership tolerance (decades to nearest band edge)
    marginal_hits = [(r[0], r[7]) for r in rows if (not r[5]) and abs(r[7]) <= MARGINAL_DEC]  # (local)
    # nearest approach across all complement observables (smallest |gap|)
    nearest_obs = min(rows, key=lambda r: abs(r[7]))                 # (local)
    nearest_obs_name, nearest_obs_gap = nearest_obs[0], nearest_obs[7]  # (local)

    if count_in_band_nat >= 1:
        verdict = "PASS"
    elif marginal_hits:
        verdict = "INFO"
    else:
        verdict = "FAIL"

    # ---- [SIGN] 3-tuple ----
    # sign_verdict: the predicted IN/OUT-of-band DIRECTION vs the computed direction.
    #   Pre-registration (substitution chain Step 4): the OPEN possibilities are PASS
    #   (some complement obs in-band) vs FAIL/INFO (none). The directional CLAIM the
    #   gate registers is the in/out-of-band determination itself. sign matches the
    #   computed direction by construction of the set-membership test => PASS, EXCEPT
    #   we set N/A only if there were no observables (there are 5). Here the computed
    #   direction is well-defined for every observable, so sign_verdict=PASS (the
    #   direction read-off matches the enumeration's computed in/out determination).
    sign_verdict = "PASS"
    # magnitude_verdict: count-in-band vs the >=1 PASS-band; INFO if marginal; FAIL if clean out.
    if count_in_band_nat >= 1:
        magnitude_verdict = "PASS"
    elif marginal_hits:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # regime_verdict: the transport map f_obs=f_tilde/kappa is exact (no expansion);
    # the band-membership test is exact over the full window => VALID.
    regime_verdict = "VALID"

    # Composite-collapse cross-check (gate-verdicts.md): with regime=VALID,
    # sign=PASS: magnitude=FAIL & regime=VALID -> FAIL; magnitude=INFO -> INFO; else PASS.
    if regime_verdict == "BREAKDOWN":
        composite_check = "FAIL"
    elif sign_verdict == "FAIL":
        composite_check = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite_check = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite_check = "INFO"
    elif magnitude_verdict == "INFO":
        composite_check = "INFO"
    else:
        composite_check = "PASS"
    assert composite_check == verdict, f"composite-collapse mismatch: {composite_check} vs {verdict}"

    kappa_status = "INDEPENDENTLY-PINNED" if verdict == "PASS" else "CONSISTENCY-PINNED"  # (local)

    print("\n" + "=" * 78)
    print(f"count(O_i(kappa_nat) in-band) = {count_in_band_nat}")
    print(f"nearest-approach observable: {nearest_obs_name}  (gap {nearest_obs_gap:+.3f} dec to nearest band edge)")
    print(f"marginal hits (|gap|<= {MARGINAL_DEC} dec): {marginal_hits}")
    print(f"VERDICT: {verdict}   (kappa_status -> {kappa_status})")
    print(f"3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print("=" * 78)

    # ---- value payload string (no single-quote chars; the tool wraps value='...') ----
    value = (
        f"complement_in_band_count={count_in_band_nat};"
        f"member_of_any_band={any_in_band_at_nat};"
        f"nearest_obs={nearest_obs_name};nearest_gap={nearest_obs_gap:+.3f}dec;"
        f"grid_in_band_pts={n_grid_in_band}/{N_eval};"
        f"CGWB_freq_axis_excluded=True(S98_V7_FAIL_10d31d0e,+28.929dec);"
        f"kappa_status={kappa_status}"
    )

    # ---- dual-SHA over the input-pin map ----
    pins = {                                                          # (local)
        "script": sha_script,
        "s97_omegagw_npz": sha_s97,
        "s98_v7_verdict_baseline": sha_s98v7,
        "canonical": sha_canon,
        "pinmap": closure_hash({
            "N_eval": str(N_eval),
            "kappa_nat": f"{kappa_nat:.15e}",
            "scan_range": "[1e-20,1e-10]",
            "scheme": SCHEME,
            "convention": CONVENTION,
            "marginal_dec": str(MARGINAL_DEC),
            "gate_id": GATE_ID,
        }),
    }
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)

    # ---- npz output ----
    npz_path = Path("computations/session-99/s99_w4_kappa_alt_observable_scan.npz")
    np.savez(
        npz_path,
        gate_id=GATE_ID,
        verdict=verdict,
        kappa_status=kappa_status,
        kappa_nat=kappa_nat,
        inv_kappa_nat=inv_kappa_nat,
        kappa_grid=kappa_grid,
        N_eval=N_eval,
        Omega_peak_grid=Omega_peak_grid,
        f_peak_Hz_baseline=f_peak_Hz_baseline,
        f_tilde_peak=f_tilde_peak,
        observable_names=np.array(names, dtype=object),
        f_obs_nat=np.array(f_obs_nat_arr, dtype=float),
        t_obs_nat=np.array(t_obs_nat_arr, dtype=float),
        in_band_nat=np.array(in_band_nat_arr, dtype=bool),
        nearest_gap_dec=np.array(nearest_gap_arr, dtype=float),
        count_in_band_nat=count_in_band_nat,
        n_grid_in_band=n_grid_in_band,
        marginal_dec=MARGINAL_DEC,
        nearest_obs_name=nearest_obs_name,
        nearest_obs_gap=nearest_obs_gap,
        band_lo_global=band_lo_global,
        band_hi_global=band_hi_global,
        band_names=np.array(list(BANDS.keys()), dtype=object),
        band_edges=np.array([[lo, hi] for lo, hi in BANDS.values()], dtype=float),
        v7_present=v7_present,
        v7_audit_matches=v7_audit_matches,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite=verdict,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"[npz] wrote {npz_path}")

    # ---- plot: complement observables vs detector bands on the log-frequency axis ----
    fig, ax = plt.subplots(figsize=(11, 6))
    # shade the detector bands
    band_colors = {"PTA": "#5fa8d3", "LISA": "#8ac926", "LIGO_ET": "#ffca3a", "resonant_HF": "#ff595e"}  # (local)
    for bname, (lo, hi) in BANDS.items():
        ax.axvspan(np.log10(lo), np.log10(hi), alpha=0.18, color=band_colors.get(bname, "#999"),
                   label=f"{bname} [{lo:.0e},{hi:.0e}]Hz")
    # closed-axis baseline (CGWB peak freq) — excluded, drawn for reference
    ax.axvline(np.log10(f_peak_Hz_baseline), color="black", ls="--", lw=1.4,
               label=f"CLOSED: CGWB peak {f_peak_Hz_baseline:.2e}Hz (S98 V.7, excluded)")
    # complement observables at kappa_nat
    ys = np.arange(len(rows))  # (local)
    for i, r in enumerate(rows):
        f_obs = r[4]  # (local)
        col = "tab:green" if r[5] else "tab:red"  # (local)
        ax.scatter(np.log10(f_obs), i, s=90, color=col, zorder=5, edgecolor="k")
        ax.annotate(f"{r[0]}  (f_obs={f_obs:.2e}Hz, gap {r[7]:+.2f}dec)",
                    (np.log10(f_obs), i), textcoords="offset points", xytext=(8, 0),
                    va="center", fontsize=8)
    ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in rows], fontsize=8)
    ax.set_xlabel("log10(f_obs / Hz)  —  laboratory frequency image at kappa_nat")
    ax.set_title(f"{GATE_ID}: kappa-dependent COMPLEMENT observables vs realized detector bands\n"
                 f"VERDICT={verdict}  (kappa_status -> {kappa_status}; count in-band={count_in_band_nat}/5)")
    ax.legend(loc="upper left", fontsize=7, framealpha=0.9)
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    png_path = Path("computations/session-99/s99_w4_kappa_alt_observable_scan.png")
    fig.savefig(png_path, dpi=130)
    plt.close(fig)
    print(f"[png] wrote {png_path}")

    # ---- emit verdict payload (agent passes to emit_verdict MCP tool) ----
    extra_rows = [                                                    # (local)
        f"# kappa_nat={kappa_nat:.6e}s 1/kappa_nat={inv_kappa_nat:.6e}Hz band_ceiling={band_hi_global:.0e}Hz nearest_obs={nearest_obs_name}(gap{nearest_obs_gap:+.3f}dec)",
        f"# CGWB-freq axis CLOSED upstream (S98-KAPPA-INDEP-FROM-CGWB-FREQ FAIL audit=10d31d0e {f_peak_Hz_baseline:.4e}Hz +28.929dec); this gate = COMPLEMENT set",
    ]
    print_verdict_payload(
        verdict=verdict,
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        companion_note="kappa-determinacy COMPLEMENT-set scan (NON-PHONONIC gate-object; substrate-IS observables)",
        extra_rows=extra_rows,
    )

    # 4-tuple output (final non-verdict line)
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")


if __name__ == "__main__":
    main()
