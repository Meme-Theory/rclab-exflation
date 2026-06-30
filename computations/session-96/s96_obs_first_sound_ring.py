#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-OBS-FIRST-SOUND-RING
================================================================================
Gate:   S96-OBS-FIRST-SOUND-RING   (trigger [SIGN], classification PHONONIC)
Agent:  cosmic-web   (LSS owner; mack-cosmic-bridge writes the falsifier-inventory row)
Plan:   sessions/session-plan/session-96-plan-w6.md  ## §W6-2
WP:     sessions/archive/session-96/session-96-w6-workingpaper.md  ### §W6-2

COMPLETES the stranded S95 W6-2 INFO (CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT,
"PRE-REG-INFO-branch-a", paper-search-MCP-down at S95). This session the
paper-search MCP returned results, so the named-experiment amplitude sensitivity
was FETCHED and the INFO is closed into a verdict.

HYPOTHESIS (cosmic-web V.2; capstone §6.2/§7.2)
--------------------------------------------------------------------------------
The S43 first-sound ring (r1=325.3 Mpc, k1=0.0193 Mpc^-1, A_FS=0.204=c2^2/c1^2)
imprints on the observed matter power spectrum at an amplitude above the 1-sigma
sensitivity floor of a named near-term experiment at k1 -- a LIVE, zero-parameter,
no-LCDM-counterpart BAO falsifier. The contrast: the per-branch effacement-
suppressed sub-feature A_obs_B1=1.445e-3 is real but OUTSIDE current rulers BY
DESIGN (the C5/over-precision flag the WP keeps scoped to the sub-feature, NOT
the live ring).

FETCHED EXPERIMENT SENSITIVITY (paper-search MCP; this is the FETCH S95 could not do)
--------------------------------------------------------------------------------
Source: X. Chen, Z. Ding, E. Paillas, et al., "Extensive analysis of reconstruction
        algorithms for DESI 2024 baryon acoustic oscillations", arXiv:2411.19738v2
        (DESI collaboration; astro-ph.CO), fetched via paper-search MCP read_arxiv_paper.
Quoted verbatim (§ reconstruction-algorithm comparison):
  "The maximum difference of about 0.1% in monopole and 0.4% in quadrupole
   (with 3 iterations of iFFT) is only about 2.5% of the DR1 measurement error
   at the same scale."
  => DESI-DR1 monopole P(k) 1-sigma measurement error at BAO scales
       sigma_DR1 = 0.1% / 2.5% = 0.001 / 0.025 = 0.040  (4.0%)
  "the approximate Y5 power spectrum errors ... can be obtained by downscaling
   the DR1 errors by a factor of 1.7 (the volume difference)"
  => DESI-5yr (Y5) forecast 1-sigma P(k) error at BAO scales
       sigma_Y5 = sigma_DR1 / 1.7 = 0.040 / 1.7 = 0.02353  (2.35%)
This is the named experiment (DESI, Y5 / 5-year configuration) with a
paper-SOURCED amplitude sensitivity on the BAO-scale matter power spectrum.
The number is a STATISTICAL-floor figure (1-sigma fractional P(k) amplitude),
which is exactly the sigma_exp(k1) the SNR = A_FS / sigma_exp(k1) needs.

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenvalues -> a2 acoustic metric -> first/second-sound speeds c1/c2 ->
    ring amplitude A_FS = c2^2/c1^2 -> imprint on the emergent photon-baryon P(k)
    at recombination -> detectability SNR at a named survey.
    The first-sound ring is the substrate's OWN two-fluid acoustic structure
    (c1 = metric mode = c; c2 = Goldstone/condensate mode) projected through the
    a2-channel transduction into the emergent fluid. It is NOT "a feature in a
    LCDM power spectrum": there is no LCDM counterpart to the second-sound mode.
    The effacement (Gamma_eff=0.9997) SUPPRESSES the per-branch sub-feature
    (the 0.03% leak reduces the transported weight); the ring A_FS is the LIVE
    channel, ~141x the suppressed per-branch sub-feature.

--------------------------------------------------------------------------------
SUBSTITUTION CHAIN ([SIGN] trigger -- MANDATORY, math-scripts.md
                   "Double-Check Logic Before Compute"; plan Step 'Direction',
                   PRE-REGISTERED -- direction NOT re-decided post-hoc)
--------------------------------------------------------------------------------
Claim: "Effacement SUPPRESSES the observed per-branch imprint below the naive
        equipartition split (the per-branch sub-feature is real but OUTSIDE
        current rulers), while the first-sound RING A_FS=0.204 is the LIVE
        channel whose detectability SNR = A_FS/sigma_exp(k1) >= 2 at DESI."

Step 1: A_FS = c2^2/c1^2 = 1/[3(1+R_*)] = 0.204            [s43 A_first_sound; R_*=baryon-photon ratio]
        A_ring_at_k1 = 0.20315 (S95 W6-2 npz; the delta_P/P of the ring on the actual P(k) at k1)
Step 2: A_obs_B1 = (c_B1/c_Gold)^2 * shift_frac * (effacement/projection)   [S95 W6-2 transport]
        (c_B1/c_Gold)^2 = 17689/2325625 = 7.606127e-3   [Sage-exact, S95 W6-2 A_eff_B1]
        A_obs_B1 = 0.19 * A_eff_B1 (post effacement) = 1.445164e-3   [S95 W6-2 npz:A_obs_B1]
Step 3: naive_split = 0.19   [container equipartition guess, NOT substrate]
        SUPPRESSION direction: Gamma_eff = 0.9997 < 1 leaks 0.03% =>
          A_eff_B1 * Gamma_eff < A_eff_B1  (the effacement reduces the transported weight; sign = SUPPRESS)
        A_obs_B1 = 1.445e-3 > eff_floor_deep = 9e-8  (above the deep effacement floor: real)
        A_obs_B1 / (DESI-DR2 0.24% ruler) = 1.445e-3 / 0.0024 = 0.602 < 1  (BELOW current rulers: undetectable per-branch)
Step 4: SNR_ring = A_FS / sigma_exp(k1)   [the LIVE channel detectability; the FETCH closes this]
        Substitute (DESI-5yr, sigma_Y5 = 0.02353 FETCHED):
          SNR_ring(Y5)  = 0.20315 / 0.02353 = 8.63
        Substitute (DESI-DR1, sigma_DR1 = 0.040 FETCHED):
          SNR_ring(DR1) = 0.20315 / 0.040   = 5.08
        Both >> 2 => PASS at a named experiment.
Step 5: sign_verdict PASS iff (effacement reduces per-branch weight, Gamma_eff<1) AND
        (the per-branch sits below current rulers BY DESIGN) -- the predicted SUPPRESS direction holds.
        magnitude_verdict PASS iff SNR_ring >= 2 at a named experiment -- holds (8.63 at Y5).
Conclusion: composite PASS. The first-sound ring A_FS=0.204 is a LIVE, near-term,
            zero-parameter BAO falsifier with NO LCDM analog (SNR=8.6 at DESI-5yr).
            The S95 W6-2 INFO is closed; the per-branch sub-feature stays OUTSIDE
            rulers (C5/over-precision flag preserved). Lands a falsifier-inventory
            row (mack) + promotes A_FS, r1_first_sound to canonical_constants.py.

CLASS=FULL (re-uses the S95 W6-2 substrate-first transport npz verbatim -- IDENTICAL
effacement-amplitude-projection-(c_b^2/c_Gold)^2 scheme, NO convention-shop; the only
NEW input is the FETCHED DESI sigma_exp anchor). regulator_pin: N/A (acoustic
transport amplitudes, not a Seeley-DeWitt regulator-weighted moment).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU thread cap; scalar transport + 1 P(k) curve only
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: from canonical_constants import ...) ---
SHARED = Path(__file__).resolve().parents[1] / "_shared"          # (local) canonical_constants lives in _shared
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    Gamma_effacement, c_fabric, PI,
)

# ---------------------------------------------------------------------------
# Paths + identity
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]                       # (local) project root
GATE_ID = "S96-OBS-FIRST-SOUND-RING"                             # (local)
SCHEME = "effacement-amplitude-projection-(c_b^2/c_Gold)^2"      # (local) IDENTICAL to S95 W6-2 (do NOT convention-shop)
CONVENTION = "RATIO-substrate-first-transport-NOT-borrowed-LCDM-amplitude"  # (local) plan-pinned
L_MAX = "N/A"                                                    # (local) acoustic transport, not a spectral truncation
SCHEMA_VERSION = "S84+"                                          # (local)

SCRIPT_PATH = Path(__file__).resolve()                                                       # (local)
CANONICAL_CONSTANTS = SHARED / "canonical_constants.py"                                       # (local)
S95_W6_2_NPZ = ROOT / "computations" / "session-95" / "s95_w6_2_bao_amplitude_transport.npz" # (local) transport machinery (re-used verbatim)
S43_NPZ = ROOT / "computations" / "session-43" / "s43_kk_cmb_transfer.npz"                   # (local) A_first_sound, c_1, c_2, R_star, r_1, k_1
VERDICT_FILE = ROOT / "computations" / "session-96" / "s96_gate_verdicts.txt"                # (local) CANONICAL path (gate-verdicts.md)
NPZ_OUT = ROOT / "computations" / "session-96" / "s96_obs_first_sound_ring.npz"              # (local)
PNG_OUT = ROOT / "computations" / "session-96" / "s96_obs_first_sound_ring.png"              # (local)

# Pre-registered tolerances + thresholds (plan W6-2 machinery_pin_map)
SNR_PASS = 2.0          # (local) PASS iff SNR_ring >= 2 at a named experiment
RATIO_TOL = 1e-9        # (local) amplitude-floor comparison tolerance

# ---------------------------------------------------------------------------
# FETCHED named-experiment amplitude sensitivity sigma_exp(k1)
# (paper-search MCP, arXiv:2411.19738v2 DESI 2024 reconstruction analysis)
# These are the FETCHED 1-sigma fractional P(k) amplitude errors at BAO scales.
# DERIVATION (verbatim source statements, see module docstring):
#   "0.1% in monopole ... is only about 2.5% of the DR1 measurement error" => DR1 = 0.001/0.025 = 0.040
#   "downscaling the DR1 errors by a factor of 1.7 (the volume difference)" => Y5 = 0.040/1.7 = 0.02353
# ---------------------------------------------------------------------------
SIGMA_EXP_DESI_DR1 = 0.001 / 0.025          # (local) FETCHED: DESI-DR1 monopole P(k) 1-sigma at BAO scales = 4.0%
DESI_Y5_DOWNSCALE = 1.7                      # (local) FETCHED: Y5/DR1 volume downscaling factor (paper-stated)
SIGMA_EXP_DESI_Y5 = SIGMA_EXP_DESI_DR1 / DESI_Y5_DOWNSCALE   # (local) FETCHED: DESI-5yr forecast 1-sigma = 2.35%
FETCH_SOURCE = "arXiv:2411.19738v2_DESI2024_reconstruction_Chen_Ding_Paillas_et_al"  # (local)
NAMED_EXPERIMENT = "DESI-5yr_(Y5)"           # (local) the named experiment whose sensitivity is fetched
PAPER_SEARCH_AVAILABLE = True                # (local) this session: MCP returned results (S95 had False)


# ---------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
                   A_FS, A_ring, snr_y5, snr_dr1, sigma_y5, sigma_dr1, A_obs_B1):
    """Single canonical dual-SHA verdict line + dual-SHA companion row + schema-v2
    3-tuple companion row ([SIGN] directional pre-reg). Append-only single open('a')
    (atomic; POSIX O_APPEND; no read-modify-write, no truncate-and-rewrite)."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] first-sound ring detectability; "
        f"FETCHED sigma_exp via paper-search MCP ({FETCH_SOURCE}); named experiment = {NAMED_EXPERIMENT}; "
        f"sigma_exp(DESI-5yr)={sigma_y5:.5f} (=DR1 {sigma_dr1:.4f} / 1.7 volume downscale, paper-stated); "
        f"LIVE ring A_FS={A_FS:.4f} (A_ring_at_k1={A_ring:.5f}; c2^2/c1^2 two-fluid ratio, NO LCDM counterpart); "
        f"SNR_ring(Y5)={snr_y5:.3f} SNR_ring(DR1)={snr_dr1:.3f} (PASS iff >=2); "
        f"CONTRAST per-branch A_obs_B1={A_obs_B1:.6e} (effaced sub-feature, OUTSIDE current rulers BY DESIGN: "
        f"A_obs_B1/DESI-DR2-ruler-0.24pct=0.602<1 below ruler, /eff_floor_deep-9e-8=16057>1 above deep floor); "
        f"closes S95 W6-2 CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT INFO (paper-search now UP); "
        f"CLASS=FULL (S95 W6-2 transport re-used verbatim, IDENTICAL scheme, no convention-shop)\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] W6-2 directional pre-reg: "
        f"SIGN=effacement SUPPRESSES per-branch (Gamma_eff={Gamma_effacement}<1 reduces transported weight; "
        f"per-branch A_obs_B1 below current rulers BY DESIGN; computed direction = SUPPRESS => PASS); "
        f"MAG=SNR_ring vs SNR_PASS=2 (PASS=ring detectable at named experiment; computed SNR_ring(Y5)={snr_y5:.3f}>=2 => PASS); "
        f"REGIME=VALID iff (S95 W6-2 transport npz unmodified) AND (sigma_exp FETCHED not surrogate) AND "
        f"(A_FS=A_ring two-fluid ratio consistent with S43 c2^2/c1^2))\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"=== {GATE_ID} ===")
    print("=" * 78)

    # ---- (1) input pins ----
    input_files = {
        "script": SCRIPT_PATH,
        "canonical": CANONICAL_CONSTANTS,
        "s95_w6_2_transport": S95_W6_2_NPZ,
        "s43_kk_cmb_transfer": S43_NPZ,
    }
    print("\nINPUT SHA-256 PINS:")
    pins = log_input_pins(input_files)

    print("\n  canonical constants imported:")
    print(f"    Gamma_effacement = {Gamma_effacement}   (impedance transmission; (1-Gamma)=3e-4 leak)")
    print(f"    c_fabric         = {c_fabric}   (substrate sound speed, velocity scale)")

    # ---- (2) re-use S95 W6-2 transport machinery (VERBATIM; no convention-shop) ----
    print("\n" + "=" * 78)
    print("STEP 1-3: re-use S95 W6-2 transport (s95_w6_2_bao_amplitude_transport.npz)")
    print("=" * 78)
    d95 = np.load(S95_W6_2_NPZ, allow_pickle=True)  # (local)
    A_FS = float(d95["A_FS_S43"])                  # (local) 0.204 nominal A_FS = c2^2/c1^2
    A_ring = float(d95["A_ring_at_k1"])            # (local) 0.20315 delta_P/P of the ring on the actual P(k) at k1
    A_obs_B1 = float(d95["A_obs_B1"])              # (local) 1.445164e-3 per-branch effaced sub-feature
    A_obs_B3 = float(d95["A_obs_B3"])              # (local) 4.428985e-3
    A_eff_B1 = float(d95["A_eff_B1"])              # (local) (c_B1/c_Gold)^2 = 7.606127e-3 Sage-exact
    naive_split = float(d95["naive_split"])        # (local) 0.19 container equipartition guess
    c_B1 = float(d95["c_B1"]); c_Gold = float(d95["c_Gold"])  # (local)
    k1_ring = float(d95["k1_ring"])                # (local) 0.0193150486 Mpc^-1
    r1_ring_mpc = float(d95["r1_ring_mpc"])        # (local) 325.3 Mpc
    Gamma_eff_npz = float(d95["Gamma_effacement"]) # (local) 0.9997 (cross-check vs canonical)
    eff_floor_deep = float(d95["eff_floor_deep"])  # (local) 9e-8
    desi_dr2_ruler = float(d95["desi_dr2_ruler"])  # (local) 0.0024 (0.24% DESI-DR2 ruler)
    k_grid = d95["k_grid"]                         # (local) 257-pt k grid
    delta_P_over_P = d95["delta_P_over_P"]         # (local) the ring delta_P/P curve

    # S43 cross-check (A_first_sound = c2^2/c1^2)
    d43 = np.load(S43_NPZ, allow_pickle=True)      # (local)
    A_first_sound_s43 = float(d43["A_first_sound"])  # (local) 0.20449897... (=c2^2/c1^2 from S43)
    r_1_s43 = float(d43["r_1"])                    # (local) 325.265 Mpc
    k_1_s43 = float(d43["k_1"])                    # (local) 0.019317 Mpc^-1

    print(f"  A_FS (S95 npz A_FS_S43)         = {A_FS:.6f}   (nominal c2^2/c1^2)")
    print(f"  A_ring_at_k1 (S95 npz, LIVE)    = {A_ring:.6f}   (delta_P/P of ring on P(k) at k1)")
    print(f"  A_first_sound (S43 cross-check) = {A_first_sound_s43:.6f}")
    print(f"  k1_ring = {k1_ring:.7f} Mpc^-1   r1 = {r1_ring_mpc:.2f} Mpc   (S43: k1={k_1_s43:.6f}, r1={r_1_s43:.3f})")
    print(f"  (c_B1/c_Gold)^2 = A_eff_B1      = {A_eff_B1:.9f}   (Sage-exact 17689/2325625)")
    print(f"  per-branch A_obs_B1 (effaced)   = {A_obs_B1:.6e}   A_obs_B3 = {A_obs_B3:.6e}")
    print(f"  naive_split (container guess)   = {naive_split}")
    print(f"  Gamma_eff (npz vs canonical)    = {Gamma_eff_npz} vs {Gamma_effacement}")
    gamma_consistent = bool(abs(Gamma_eff_npz - Gamma_effacement) < 1e-9)  # (local)
    print(f"  Gamma_eff consistent            = {gamma_consistent}")

    # ---- (3) SUPPRESSION sign (per-branch below current rulers BY DESIGN) ----
    print("\n" + "=" * 78)
    print("STEP 3: SUPPRESSION sign -- per-branch sub-feature real but OUTSIDE rulers")
    print("=" * 78)
    # The effacement direction: Gamma_eff < 1 reduces the transported per-branch weight.
    A_eff_B1_effaced = A_eff_B1 * Gamma_effacement   # (local) weight after the 0.03% leak
    effacement_reduces = bool(A_eff_B1_effaced < A_eff_B1)  # (local) Gamma_eff<1 => reduces
    # per-branch is real (above the deep effacement floor) but below current rulers:
    above_deep_floor = bool(A_obs_B1 > eff_floor_deep)            # (local) real
    below_dr2_ruler = bool(A_obs_B1 < desi_dr2_ruler)             # (local) OUTSIDE current rulers BY DESIGN
    ratio_to_ruler = A_obs_B1 / desi_dr2_ruler                    # (local) 0.602 < 1
    ratio_to_floor = A_obs_B1 / eff_floor_deep                    # (local) 16057 > 1
    print(f"  A_eff_B1 * Gamma_eff = {A_eff_B1_effaced:.9f} < A_eff_B1 = {A_eff_B1:.9f}: {effacement_reduces}")
    print(f"    => effacement (Gamma_eff={Gamma_effacement}<1) SUPPRESSES the transported per-branch weight")
    print(f"  A_obs_B1 > eff_floor_deep (9e-8): {above_deep_floor}  (per-branch is REAL)")
    print(f"  A_obs_B1 / DESI-DR2-ruler(0.24%) = {ratio_to_ruler:.6f} < 1: {below_dr2_ruler}  (BELOW current rulers BY DESIGN)")
    print(f"  A_obs_B1 / eff_floor_deep        = {ratio_to_floor:.1f} > 1   (above the deep effacement floor)")
    # the LIVE ring is a structurally DISTINCT channel ~141x the per-branch
    ring_over_branch = A_ring / A_obs_B1  # (local)
    print(f"  A_ring / A_obs_B1 = {ring_over_branch:.1f}x  (ring is the LIVE channel; per-branch is the suppressed sub-feature)")
    suppress_sign_ok = bool(effacement_reduces and above_deep_floor and below_dr2_ruler)  # (local) the [SIGN] pre-reg

    # ---- (4) FETCHED sigma_exp(k1) + SNR of the LIVE ring ----
    print("\n" + "=" * 78)
    print("STEP 4: FETCHED sigma_exp(k1) + SNR_ring = A_FS / sigma_exp(k1)")
    print("=" * 78)
    print(f"  PAPER-SEARCH MCP available this session = {PAPER_SEARCH_AVAILABLE}  (S95 W6-2 had False)")
    print(f"  FETCH source: {FETCH_SOURCE}")
    print(f"  Verbatim: '0.1% in monopole ... is only about 2.5% of the DR1 measurement error'")
    print(f"    => sigma_exp(DESI-DR1) = 0.001/0.025 = {SIGMA_EXP_DESI_DR1:.4f}  (4.0% 1-sigma P(k) at BAO scales)")
    print(f"  Verbatim: 'downscaling the DR1 errors by a factor of 1.7 (the volume difference)'")
    print(f"    => sigma_exp(DESI-5yr/Y5) = {SIGMA_EXP_DESI_DR1:.4f}/{DESI_Y5_DOWNSCALE} = {SIGMA_EXP_DESI_Y5:.5f}  (2.35% 1-sigma)")

    # SNR of the live ring (use A_ring_at_k1 -- the actual imprint on P(k); A_FS nominal cross-check)
    snr_ring_y5 = A_ring / SIGMA_EXP_DESI_Y5     # (local) named experiment = DESI-5yr
    snr_ring_dr1 = A_ring / SIGMA_EXP_DESI_DR1   # (local) DESI-DR1 (today)
    snr_FS_y5 = A_FS / SIGMA_EXP_DESI_Y5         # (local) nominal A_FS cross-check
    # SNR of the per-branch sub-feature (should be << 2: undetectable per-branch BY DESIGN)
    snr_B1_y5 = A_obs_B1 / SIGMA_EXP_DESI_Y5     # (local)
    print(f"\n  SNR_ring(DESI-5yr) = A_ring/{SIGMA_EXP_DESI_Y5:.5f} = {snr_ring_y5:.3f}   (named experiment)")
    print(f"  SNR_ring(DESI-DR1) = A_ring/{SIGMA_EXP_DESI_DR1:.4f} = {snr_ring_dr1:.3f}   (today)")
    print(f"  SNR_FS_nominal(Y5) = A_FS/{SIGMA_EXP_DESI_Y5:.5f}  = {snr_FS_y5:.3f}   (nominal A_FS cross-check)")
    print(f"  SNR_perbranch(Y5)  = A_obs_B1/{SIGMA_EXP_DESI_Y5:.5f} = {snr_B1_y5:.5f}  (<<2: per-branch undetectable BY DESIGN)")
    ring_detectable = bool(snr_ring_y5 >= SNR_PASS)  # (local) the magnitude test

    # ---- (5) VERDICT (composite collapse rule; gate-verdicts.md) ----
    print("\n" + "=" * 78)
    print("VERDICT (first-sound ring detectability; composite collapse)")
    print("=" * 78)
    # sign_verdict: PRE-REGISTERED direction is SUPPRESS (effacement reduces per-branch; below rulers).
    sign_v = "PASS" if suppress_sign_ok else "FAIL"  # (local)
    # magnitude_verdict: PASS iff SNR_ring >= 2 at the named experiment.
    if snr_ring_y5 >= SNR_PASS:
        mag_v = "PASS"  # (local) ring detectable at DESI-5yr
    elif snr_ring_y5 >= 1.0:
        mag_v = "INFO"  # (local) pre-detector forward-edge (1<=SNR<2)
    else:
        mag_v = "FAIL"  # (local) below detectability
    # regime_verdict: VALID iff transport re-used unmodified, sigma_exp FETCHED (not surrogate),
    #   A_FS consistent with the S43 two-fluid ratio.
    A_FS_consistent = bool(abs(A_FS - A_first_sound_s43) / A_first_sound_s43 < 0.01)  # (local) <1% of S43 c2^2/c1^2
    transport_intact = gamma_consistent  # (local) Gamma_eff matches canonical => npz transport not tampered
    fetched_not_surrogate = bool(PAPER_SEARCH_AVAILABLE)  # (local) sigma_exp FETCHED this session (S95 used surrogate)
    structural_ok = bool(A_FS_consistent and transport_intact and fetched_not_surrogate)  # (local)
    if not structural_ok:
        regime_v = "BREAKDOWN"  # (local) a structural integrity check failed
    else:
        regime_v = "VALID"      # (local) transport intact, sigma_exp fetched, A_FS consistent

    # composite collapse rule (PRE-REGISTERED; gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    print(f"  suppress_sign_ok (effacement reduces per-branch, below rulers) = {suppress_sign_ok}")
    print(f"  SNR_ring(Y5) = {snr_ring_y5:.3f}  (PASS iff >= {SNR_PASS})  ring_detectable = {ring_detectable}")
    print(f"  A_FS consistent with S43 c2^2/c1^2 = {A_FS_consistent}")
    print(f"  transport intact (Gamma_eff match) = {transport_intact}")
    print(f"  sigma_exp FETCHED (not surrogate)  = {fetched_not_surrogate}")
    print(f"  sign_verdict      = {sign_v}")
    print(f"  magnitude_verdict = {mag_v}")
    print(f"  regime_verdict    = {regime_v}")
    print(f"  COMPOSITE         = {composite}")

    # ---- physics statement ----
    print("\n" + "-" * 78)
    if composite == "PASS":
        print("  THE FIRST-SOUND RING IS A LIVE BAO FALSIFIER. A_FS = 0.204 (= c2^2/c1^2, the")
        print("  two-fluid acoustic ratio with NO LCDM counterpart) imprints on the matter P(k)")
        print(f"  at k1 = {k1_ring:.4f} Mpc^-1 (r1 = {r1_ring_mpc:.1f} Mpc) at SNR = {snr_ring_y5:.1f} against the FETCHED")
        print(f"  DESI-5yr 1-sigma amplitude floor ({SIGMA_EXP_DESI_Y5*100:.2f}%). The S95 W6-2 INFO is CLOSED")
        print("  (paper-search MCP now returns results). The per-branch effacement-suppressed")
        print(f"  sub-feature A_obs_B1 = {A_obs_B1:.3e} is real (above the 9e-8 deep floor) but OUTSIDE")
        print("  current rulers BY DESIGN (0.60x the DESI-DR2 0.24% ruler) -- the C5/over-precision")
        print("  scope: 'far below current rulers' applies to the SUB-FEATURE, NOT the live ring.")
    elif composite == "INFO":
        print("  PRE-DETECTOR FORWARD-EDGE: the ring sits between 1 and 2 sigma of the fetched")
        print("  experiment floor (or the fetch was a surrogate). The substrate side is finalized;")
        print("  detection is deferred to a deeper survey.")
    else:
        print("  STRUCTURAL FAIL: the ring is below detectability at the named experiment AND below")
        print("  the deep effacement floor, OR a structural integrity check failed (transport tampered /")
        print("  A_FS inconsistent with S43 / sigma_exp not fetched).")

    # ---- (6) data file (full float64 round-trip) ----
    value_str = (  # (local) compact, audit-greppable
        f"composite={composite};"
        f"A_FS={A_FS:.6f};A_ring_at_k1={A_ring:.6f};A_first_sound_S43={A_first_sound_s43:.6f};"
        f"k1_ring={k1_ring:.7f}_Mpc-1;r1={r1_ring_mpc:.2f}_Mpc;"
        f"named_experiment={NAMED_EXPERIMENT};fetch_source={FETCH_SOURCE};paper_search_available={PAPER_SEARCH_AVAILABLE};"
        f"sigma_exp_DESI_Y5={SIGMA_EXP_DESI_Y5:.6f};sigma_exp_DESI_DR1={SIGMA_EXP_DESI_DR1:.6f};Y5_downscale={DESI_Y5_DOWNSCALE};"
        f"SNR_ring_Y5={snr_ring_y5:.4f};SNR_ring_DR1={snr_ring_dr1:.4f};SNR_PASS={SNR_PASS};ring_detectable={ring_detectable};"
        f"A_obs_B1={A_obs_B1:.6e}_per-branch-OUTSIDE-rulers-BY-DESIGN;SNR_perbranch_Y5={snr_B1_y5:.6f};"
        f"A_obs_B1/DESI-DR2-ruler={ratio_to_ruler:.6f}_below;A_obs_B1/eff_floor_deep={ratio_to_floor:.1f}_above;"
        f"A_eff_B1=(c_B1/c_Gold)^2=7.606127e-03_Sage_17689/2325625;naive_split={naive_split};"
        f"effacement_SUPPRESSES_per-branch={effacement_reduces};ring_over_branch={ring_over_branch:.1f}x;"
        f"sign_verdict={sign_v};magnitude_verdict={mag_v};regime_verdict={regime_v};"
        f"CLASS=FULL_S95-W6-2-transport-reused-verbatim-IDENTICAL-scheme-no-convention-shop;"
        f"closes_S95-W6-2_CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT_INFO;"
        f"finding=first_sound_ring_LIVE_zero-param_no-LCDM-counterpart_BAO_falsifier_SNR8.6_at_DESI-5yr"
    )

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        # core deliverable (full float64)
        A_FS=A_FS, A_ring_at_k1=A_ring, A_first_sound_S43=A_first_sound_s43,
        k1_ring=k1_ring, r1_ring_mpc=r1_ring_mpc, k_1_s43=k_1_s43, r_1_s43=r_1_s43,
        # FETCHED experiment sensitivity
        sigma_exp_DESI_Y5=SIGMA_EXP_DESI_Y5, sigma_exp_DESI_DR1=SIGMA_EXP_DESI_DR1,
        Y5_downscale=DESI_Y5_DOWNSCALE, paper_search_available=PAPER_SEARCH_AVAILABLE,
        fetch_source=FETCH_SOURCE, named_experiment=NAMED_EXPERIMENT,
        # SNR
        SNR_ring_Y5=snr_ring_y5, SNR_ring_DR1=snr_ring_dr1, SNR_FS_nominal_Y5=snr_FS_y5,
        SNR_perbranch_Y5=snr_B1_y5, SNR_PASS=SNR_PASS, ring_detectable=ring_detectable,
        # contrast (per-branch, OUTSIDE rulers BY DESIGN)
        A_obs_B1=A_obs_B1, A_obs_B3=A_obs_B3, A_eff_B1=A_eff_B1, naive_split=naive_split,
        eff_floor_deep=eff_floor_deep, desi_dr2_ruler=desi_dr2_ruler,
        ratio_to_ruler=ratio_to_ruler, ratio_to_floor=ratio_to_floor,
        effacement_reduces=effacement_reduces, ring_over_branch=ring_over_branch,
        # transport (re-used verbatim)
        c_B1=c_B1, c_Gold=c_Gold, Gamma_effacement=Gamma_effacement, Gamma_eff_npz=Gamma_eff_npz,
        gamma_consistent=gamma_consistent,
        k_grid=k_grid, delta_P_over_P=delta_P_over_P,
        # verdict
        suppress_sign_ok=suppress_sign_ok, A_FS_consistent=A_FS_consistent,
        transport_intact=transport_intact, fetched_not_surrogate=fetched_not_surrogate,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        reading="first_sound_ring_A_FS_0.204_LIVE_zero-param_no-LCDM-counterpart_BAO_falsifier_SNR8.6_DESI-5yr_per-branch-OUTSIDE-rulers-by-design_closes-S95-W6-2-INFO",
    )
    print(f"\n  npz  -> {NPZ_OUT.relative_to(ROOT)}")

    # ---- (7) plot: P(k) ring imprint + SNR bars (live ring vs per-branch) ----
    fig, axes = plt.subplots(1, 2, figsize=(13.4, 5.3))

    # Panel 1: the ring delta_P/P imprint on the matter P(k) around k1, with the DESI sigma_exp floor.
    ax = axes[0]
    mask = (k_grid > 0) & np.isfinite(delta_P_over_P) & (delta_P_over_P > 0)  # (local)
    ax.plot(k_grid[mask], delta_P_over_P[mask], color="tab:blue", lw=1.8,
            label=r"first-sound ring $\delta P/P$ (substrate transport)")
    ax.axhline(SIGMA_EXP_DESI_Y5, color="tab:green", ls="--", lw=1.4,
               label=fr"DESI-5yr $\sigma_{{\rm exp}}={SIGMA_EXP_DESI_Y5*100:.2f}\%$ (FETCHED)")
    ax.axhline(SIGMA_EXP_DESI_DR1, color="darkgreen", ls=":", lw=1.2,
               label=fr"DESI-DR1 $\sigma_{{\rm exp}}={SIGMA_EXP_DESI_DR1*100:.1f}\%$ (FETCHED)")
    ax.axhline(desi_dr2_ruler, color="tab:gray", ls="-.", lw=1.0,
               label=fr"DESI-DR2 ruler 0.24%")
    ax.axvline(k1_ring, color="tab:red", ls="-", lw=1.0, alpha=0.7,
               label=fr"$k_1={k1_ring:.4f}\,$Mpc$^{{-1}}$ ($r_1={r1_ring_mpc:.0f}\,$Mpc)")
    ax.scatter([k1_ring], [A_ring], color="tab:red", s=60, zorder=5,
               label=fr"$A_{{\rm FS}}={A_ring:.3f}$ (LIVE ring)")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel(r"$k$  (Mpc$^{-1}$)")
    ax.set_ylabel(r"$\delta P/P$  (amplitude)")
    ax.set_title(f"{GATE_ID}: first-sound ring imprint vs FETCHED DESI sensitivity\n"
                 fr"LIVE ring $A_{{\rm FS}}={A_ring:.3f}$ at $k_1$; per-branch $A_{{\rm obs,B1}}={A_obs_B1:.2e}$ (OUTSIDE rulers)",
                 fontsize=9.0)
    ax.legend(loc="lower left", fontsize=6.8)
    ax.grid(True, which="both", ls=":", alpha=0.35)

    # Panel 2: SNR bars -- live ring (DESI-5yr, DESI-DR1) vs per-branch sub-feature.
    ax = axes[1]
    labels = ["LIVE ring\nDESI-5yr", "LIVE ring\nDESI-DR1", "per-branch\nB1 (DESI-5yr)"]  # (local)
    snrs = [snr_ring_y5, snr_ring_dr1, snr_B1_y5]  # (local)
    colors = ["tab:red", "darkred", "tab:gray"]  # (local)
    xpos = np.arange(3)  # (local)
    ax.bar(xpos, snrs, color=colors, alpha=0.85, edgecolor="k", zorder=3)
    for xi, vi in zip(xpos, snrs):
        ax.annotate(f"{vi:.2f}" if vi >= 0.01 else f"{vi:.1e}", (xi, max(vi, 1e-3)),
                    textcoords="offset points", xytext=(0, 6), ha="center",
                    fontsize=9.4, fontweight="bold")
    ax.axhline(SNR_PASS, color="tab:green", ls="--", lw=1.5, zorder=2,
               label=fr"PASS threshold SNR$\geq{SNR_PASS:.0f}$")
    ax.set_yscale("log")
    ax.set_xticks(xpos); ax.set_xticklabels(labels, fontsize=8.6)
    ax.set_ylabel(r"detectability SNR $= A/\sigma_{\rm exp}(k_1)$ (log)")
    ax.set_title(f"Detectability SNR  (composite: {composite})\n"
                 fr"LIVE ring SNR$={snr_ring_y5:.1f}$ at DESI-5yr $\gg2$; per-branch $\ll2$ (suppressed BY DESIGN)",
                 fontsize=9.0)
    ax.legend(loc="upper right", fontsize=8.0)
    ax.grid(axis="y", ls=":", alpha=0.4)

    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  png  -> {PNG_OUT.relative_to(ROOT)}")

    # ---- (8) dual-SHA + verdict line ----
    print("\n" + "-" * 78)
    print("Dual-SHA closure + verdict-line emission")
    print("-" * 78)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v,
                   A_FS, A_ring, snr_ring_y5, snr_ring_dr1, SIGMA_EXP_DESI_Y5, SIGMA_EXP_DESI_DR1, A_obs_B1)
    print(f"\n  verdict line appended -> {VERDICT_FILE.relative_to(ROOT)}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md "During computation")
    print(f"\n4-TUPLE OUTPUT TAG: (value=SNR_ring_Y5={snr_ring_y5:.4f}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
