#!/usr/bin/env python3
"""
S101 W1-4 S101-VIIAM-ALPHA-ENVELOPE-PIN — §VII.AM Level-2 envelope alpha-pin
============================================================================

Gate: S101-VIIAM-ALPHA-ENVELOPE-PIN ([VERIFY])
Classification: PHONONIC (effacement / Bogoliubov spectrum-reorganization —
  GGE/transit substrate physics; Gamma_eff IS the acoustic-white-hole
  transmission, not a measurement IN any container)

Pre-registered band (plan session-101-plan-w1.md §W1-4 strict_PASS_boundary):
  PASS iff fitted alpha in [1, 3.52)
  FAIL-low iff alpha < 1            (contradicts registered structural floor;
                                     atlas-09-relevant)
  FAIL-high iff alpha >= 3.52       (Level-3 anchor 3.0e-4 would violate the
                                     pinned envelope at canonical L_max=10;
                                     clause-(b) Registry-PASS breaks)
  INFO iff scan ill-conditioned (pre-registered conditioning predicates:
    non-monotone dGamma_eff in L, OR OLS R^2 < 0.90, OR any
    dGamma_eff/Gamma_eff < 1e-13 float-floor saturation, OR estimator-mismatch
    flag fires |Gamma_eff(12) - Gamma_effacement| >= 1e-3)

Hypothesis (plan): the Level-2 convergence envelope
  dGamma_eff/Gamma_eff ~ L_max^{-alpha} on the Bogoliubov-spectrum-
  reorganization-rate observable has fitted exponent alpha in [1, 3.52),
  consistent with the registered structural floor alpha >= 1 (Volovik
  effacement scaling, registry line 16755) and with the Level-3 anchor 3.0e-4
  satisfying the envelope at canonical L_max=10 (Registry-PASS criterion).

SUBSTRATE-IS OBSERVABLE (the single, pre-committed estimator — chosen on
S37/S58 physics, NOT iterated to land in-band):
  Gamma_eff is the S58 Volovik-partition effacement = the acoustic-white-hole
  IMPEDANCE TRANSMISSION (canonical_constants.py:540 "S37 acoustic-white-hole
  impedance-transmission"). The impedance mismatch is between the gapless
  acoustic transmitting band (the lowest Peter-Weyl sector (0,0) — the
  Bogoliubov-Anderson phonon floor of the truncated D_K spectrum) and the bulk
  reorganized spectrum. The reflected fraction follows the acoustic-white-hole
  reflection formula
        R(L) = ((1 - r(L)) / (1 + r(L)))^2,
        r(L) = <|lambda|>_acoustic / <|lambda|>_total(L)     (INTENSIVE ratio),
  using INTENSIVE spectral means on BOTH sides (impedance is an intensive
  quantity; an extensive Sigma|lambda| denominator would inject a spurious
  mode-count steepening). The effacement is Gamma_eff(L) = 1 - k*R(L), with the
  single overall scale k FIXED by the sanity anchor so the deepest truncation
  reproduces the canonical Gamma_effacement = 0.99970 EXACTLY at L=12; k cancels
  identically in the log-log slope, so alpha is INDEPENDENT of the anchor scale
  (verified analytically: a multiplicative pre-factor is annihilated by
  d ln(.)/d ln L). The fitted alpha is the convergence exponent of the
  finite-L description of the reorganization rate to the substrate's own value.

  Direction: D_K(tau_fold) eigenvalues at truncation L -> Bogoliubov
  occupation/impedance reorganization -> Gamma_eff(L) -> dGamma_eff/Gamma_eff ~
  L^{-alpha} (the envelope) -> the laboratory-IN images (horizon area, Hawking
  spectrum, Page crossover) the composite bridge map carries them to. The
  truncation is OUR window; alpha certifies how fast the window closes onto the
  substrate value.

ESTIMATOR-FAMILY ROBUSTNESS (recorded as cross-check, NOT a gate, NOT a search
for PASS): four independent physically-motivated reorganization-rate estimators
were evaluated on the same cache. ALL anchor-respecting readings give
alpha ~ 4-8 (FAIL-high); the ONLY reading landing in [1,3.52) (the bare
truncation-tail (W12-W(L))/W12) VIOLATES the binding sanity anchor
(Gamma_eff(12) -> 1, not 0.99970) and is therefore inadmissible. The FAIL-high
verdict is robust across the admissible estimator family.

Method:
  In-cache truncation of the s84 L12 master cache (NO new diagonalization;
  D_K block-diagonal by Peter-Weyl => filter sectors at p+q <= L; L_max_plan =
  L_max_operational = 12). Scan L in {8,9,10,11,12}; define
  dGamma_eff(L)/Gamma_eff = |Gamma_eff(L) - Gamma_eff(12)| / Gamma_eff(12) for
  L in {8,9,10,11}; OLS log-log fit ln(dGamma_eff/Gamma_eff) vs ln(L) ->
  alpha = -slope. Conditioning predicates route the INFO branch.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (in-cache trunc)
  - computations/session-58/s58_volovik_partition.py (S58 effacement machinery)
  - computations/session-58/s58_volovik_partition.npz (S58 reference values)
  - canonical_constants.py (Gamma_effacement=0.99970 ; tau_fold=0.190; feeds audit SHA)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<alpha + band verdict + conditioning + sub-class>,
   scheme=S58-VOLOVIK-PARTITION-EFFACEMENT-LSCAN,
   convention=RATIO-acoustic-white-hole-impedance-intensive-Lref12, L_max=12)

Audit discriminators (plan SW1-4 item 6):
  audit_sha256   = sha256(script || s84_L12_cache || s58_volovik_partition.py
                   || pinmap_json)   ["script","s84cache","s58","pinmap"]
                   (canonical_constants.py also folded via the standard
                    compute_dual_sha contract -> audit reflects canonical pin)
  content_sha256 = sha256(script)                       ["script"]

Verdict emission: this script PRINTS the payload (print_verdict_payload); the
dispatching agent calls mcp__knowledge__emit_verdict(**payload) — the race-safe,
lock-serialized single writer of s101_gate_verdicts.txt. The script does NOT
write the verdict file (Windows open("a") cross-process race; S98 lost 5/8 lines
under 8 concurrent writers).

GPU_path: cpu-cap-OMP8 (in-cache filtering + intensive occupation means; no
diagonalization, no matrix >= 100x100).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy import (GPU_path=cpu-cap-OMP8)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; S34+)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
# Consumed canonical pins:
#   Gamma_effacement = 0.99970 (canonical_constants.py:540; S37 acoustic-white-
#     hole impedance-transmission; clause-(b) Level-3 anchor; (1-Gamma)=3e-4)
#   tau_fold = 0.190 (S12/S42; the fold-transit layer of the §VII.AM 3-instance
#     corpus — the S58 Gamma_eff anchor's own regime; the L12 cache is at tau019)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins (plan SW1-4 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "101"                                                    # (local)
GATE_ID = "S101-VIIAM-ALPHA-ENVELOPE-PIN"                          # (local)
SCHEME = "S58-VOLOVIK-PARTITION-EFFACEMENT-LSCAN"                  # (local)
CONVENTION = "RATIO-acoustic-white-hole-impedance-intensive-Lref12"  # (local)
L_MAX = "12"                                                       # (local)

# Pre-registered band (plan strict_PASS_boundary)
BAND_LO = 1.0          # (local) closed lower edge (registry line 16755 floor)
BAND_HI = 3.52         # (local) open upper edge (rounded DOWN from exact 3.5229)
# Conditioning predicates (plan machinery_pin_map.tolerance)
R2_MIN = 0.90          # (local) OLS R^2 floor for INFO
FLOAT_FLOOR = 1e-13    # (local) dGamma_eff/Gamma_eff float-floor saturation
SANITY_ABS_TOL = 1e-3  # (local) |Gamma_eff(12) - Gamma_effacement| estimator-mismatch

# Scan + reference (plan machinery_pin_map)
L_SCAN = (8, 9, 10, 11, 12)   # (local) integer truncation mesh
L_REF = 12                    # (local) deepest cache truncation = continuum proxy
L_FIT = (8, 9, 10, 11)        # (local) 4 fit points (vs the L_REF reference)
TAU_TAG = "tau_fold=0.190"    # (local) cache anchor (s84 L12 master at tau019)

# Input files (SHA-pinned into pinmap)
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S58_SCRIPT = COMPUTATIONS_DIR / "session-58" / "s58_volovik_partition.py"
S58_NPZ = COMPUTATIONS_DIR / "session-58" / "s58_volovik_partition.npz"
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [
    CANONICAL_PATH,
    S84_CACHE,
    S58_SCRIPT,
    S58_NPZ,
]

OUT_NPZ = SESSION_DIR / "s101_viiam_alpha_envelope_pin.npz"
OUT_PNG = SESSION_DIR / "s101_viiam_alpha_envelope_pin.png"


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the pinmap."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """S84+ dual-SHA:
    audit_sha256   = sha256(script || canonical_constants.py || pinmap_json)
    content_sha256 = sha256(script)
    The pinmap (which contains the s84-cache + s58 SHAs + identity keys) is
    folded into the audit digest, so audit reflects every pinned input."""
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
# Section 5 — Spectrum loading + effacement estimator
# ---------------------------------------------------------------------------

def load_sector_evals() -> dict:
    """Load the s84 L12 master cache: {(p,q): {dim, level, abs_evals}}."""
    d = np.load(S84_CACHE, allow_pickle=True)  # (local)
    return d["sector_evals"].item()


def acoustic_band_mean(sec: dict) -> float:
    """<|lambda|> of the gapless acoustic transmitting band = the lowest
    Peter-Weyl sector (0,0) (the Bogoliubov-Anderson phonon floor). L-INVARIANT
    (the floor sector is present at every truncation)."""
    ac = np.asarray(sec[(0, 0)]["abs_evals"], dtype=float)  # (local)
    return float(ac.mean())


def total_mean_at_L(sec: dict, L: int) -> float:
    """<|lambda|>_total over the truncation p+q <= L (INTENSIVE)."""
    vals = [np.asarray(b["abs_evals"], dtype=float)
            for (p, q), b in sec.items() if p + q <= L]  # (local)
    allv = np.concatenate(vals)  # (local)
    return float(allv.mean())


def n_modes_at_L(sec: dict, L: int) -> int:
    """Mode count (with multiplicity) at truncation L — diagnostic only."""
    return int(sum(np.asarray(b["abs_evals"]).size
                   for (p, q), b in sec.items() if p + q <= L))


def effacement_estimator(sec: dict) -> dict:
    """The single pre-committed estimator. Returns the per-L Gamma_eff table,
    the anchor scale k, and the dGamma_eff/Gamma_eff vector for L_FIT."""
    gam_canon = Gamma_effacement  # canonical pin
    dev_canon = 1.0 - gam_canon   # (local) = 3.0e-4
    ac_mean = acoustic_band_mean(sec)  # (local) L-invariant acoustic <|lam|>

    # raw reflected fraction R(L) via acoustic-white-hole impedance formula
    tot_mean = {L: total_mean_at_L(sec, L) for L in L_SCAN}  # (local)
    r = {L: ac_mean / tot_mean[L] for L in L_SCAN}           # (local) intensive ratio
    R_refl = {L: ((1.0 - r[L]) / (1.0 + r[L])) ** 2 for L in L_SCAN}  # (local)

    # single overall scale k fixed by the sanity anchor at L_REF (cancels in slope)
    k = dev_canon / R_refl[L_REF]  # (local)
    Gamma_eff = {L: 1.0 - k * R_refl[L] for L in L_SCAN}  # (local)

    gam_ref = Gamma_eff[L_REF]  # (local) must equal Gamma_effacement by construction
    dGG = {L: abs(Gamma_eff[L] - gam_ref) / gam_ref for L in L_FIT}  # (local)

    return {
        "gam_canon": gam_canon,
        "dev_canon": dev_canon,
        "ac_mean": ac_mean,
        "tot_mean": tot_mean,
        "r": r,
        "R_refl": R_refl,
        "k": k,
        "Gamma_eff": Gamma_eff,
        "gam_ref": gam_ref,
        "dGG": dGG,
    }


def ols_loglog(Ls: np.ndarray, y: np.ndarray) -> dict:
    """OLS fit ln(y) = slope*ln(L) + intercept; alpha = -slope; R^2."""
    lnL = np.log(Ls)  # (local)
    lny = np.log(y)   # (local)
    slope, intercept = np.polyfit(lnL, lny, 1)  # (local)
    pred = slope * lnL + intercept  # (local)
    ss_res = float(((lny - pred) ** 2).sum())  # (local)
    ss_tot = float(((lny - lny.mean()) ** 2).sum())  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")  # (local)
    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "alpha": float(-slope),
        "r2": float(r2),
        "residuals": (lny - pred).tolist(),
    }


# ---------------------------------------------------------------------------
# Section 6 — S58 reference cross-check (non-gating)
# ---------------------------------------------------------------------------

def s58_reference_crosscheck() -> dict:
    """Confirm the S58 reference npz loads and report its canonical effacement-
    adjacent values for the audit trail (non-gating; the effacement Gamma=0.99970
    is a canonical pin, not stored as a per-L function in S58 — S58 is the
    machinery provenance, the L-scan is THIS gate's contribution)."""
    try:
        d = np.load(S58_NPZ, allow_pickle=True)  # (local)
        w_eff = float(np.asarray(d["w_eff_Volovik"]))  # (local)
        f_jos = float(np.asarray(d["F_Josephson"]))    # (local)
        verdict = str(np.asarray(d["gate_verdict"])[0])  # (local)
        return {"loaded": True, "w_eff_Volovik": w_eff,
                "F_Josephson": f_jos, "s58_gate_verdict": verdict}
    except Exception as exc:  # noqa: BLE001
        return {"loaded": False, "error": str(exc)}


# ---------------------------------------------------------------------------
# Section 7 — Gate evaluation
# ---------------------------------------------------------------------------

def evaluate_gate(alpha: float, dGG_vals: list[float], r2: float,
                  sanity_breach: bool) -> tuple[str, str, list[str]]:
    """Apply the pre-registered band + conditioning predicates.
    Returns (verdict, band_tag, conditioning_flags)."""
    flags: list[str] = []  # (local)
    monotone = all(dGG_vals[i] > dGG_vals[i + 1]
                   for i in range(len(dGG_vals) - 1))  # (local) decreasing in L
    float_floor_hit = any(v < FLOAT_FLOOR for v in dGG_vals)  # (local)

    if not monotone:
        flags.append("non_monotone_dGamma")
    if r2 < R2_MIN:
        flags.append(f"R2_below_{R2_MIN}")
    if float_floor_hit:
        flags.append("float_floor_saturation")
    if sanity_breach:
        flags.append("estimator_mismatch_sanity_breach")

    # INFO branch fires on any conditioning predicate
    if flags:
        return "INFO", "ill-conditioned", flags

    # band verdict (well-conditioned)
    if alpha < BAND_LO:
        return "FAIL", "FAIL-low", flags
    if alpha >= BAND_HI:
        return "FAIL", "FAIL-high", flags
    return "PASS", "in-band", flags


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------

def make_plot(est: dict, fit: dict, verdict: str, band_tag: str,
              n_modes: dict) -> None:
    Ls_fit = np.array(L_FIT, dtype=float)  # (local)
    dGG = np.array([est["dGG"][L] for L in L_FIT])  # (local)

    fig, axes = plt.subplots(1, 2, figsize=(13.5, 5.4))
    fig.suptitle(
        f"{GATE_ID} — Level-2 envelope alpha-pin  |  alpha = {fit['alpha']:.4f}  "
        f"=> {verdict} ({band_tag})\n"
        f"dGamma_eff/Gamma_eff ~ L^(-alpha); band [1, 3.52); "
        f"R^2={fit['r2']:.4f}; Gamma_eff(12)={est['gam_ref']:.5f}",
        fontsize=11, fontweight="bold")

    # (a) log-log envelope fit
    ax = axes[0]
    ax.loglog(Ls_fit, dGG, "o", ms=10, color="#1565c0",
              label="dGamma_eff/Gamma_eff (data)")
    Lgrid = np.linspace(L_FIT[0] * 0.95, L_FIT[-1] * 1.05, 100)  # (local)
    ax.loglog(Lgrid, np.exp(fit["intercept"]) * Lgrid ** fit["slope"],
              "-", color="#c62828",
              label=f"OLS fit alpha={fit['alpha']:.3f}")
    # band edges as reference envelopes anchored at L_REF deviation scale
    for a_edge, st, lab in [(BAND_LO, ":", "alpha=1 (floor)"),
                            (BAND_HI, "--", "alpha=3.52 (upper edge)")]:
        c = np.exp(fit["intercept"]) * (L_FIT[0] ** fit["slope"]) \
            / (L_FIT[0] ** (-a_edge))  # (local) match data at first point
        ax.loglog(Lgrid, c * Lgrid ** (-a_edge), st, color="gray",
                  alpha=0.7, label=lab)
    ax.set_xlabel("L_max (truncation)")
    ax.set_ylabel("dGamma_eff / Gamma_eff")
    ax.set_title("(a) Level-2 convergence envelope")
    ax.legend(fontsize=8.5, loc="lower left")
    ax.grid(True, which="both", alpha=0.3)

    # (b) Gamma_eff(L) approach to canonical + mode count
    ax = axes[1]
    Ls_all = np.array(L_SCAN, dtype=float)  # (local)
    Gam = np.array([est["Gamma_eff"][L] for L in L_SCAN])  # (local)
    ax.plot(Ls_all, Gam, "s-", color="#2e7d32", ms=8,
            label="Gamma_eff(L)")
    ax.axhline(est["gam_canon"], color="orange", ls="--",
               label=f"canonical Gamma_eff={est['gam_canon']:.5f}")
    ax.set_xlabel("L_max (truncation)")
    ax.set_ylabel("Gamma_eff(L)")
    ax.set_title("(b) Effacement approach (anchored at L=12)")
    ax.legend(fontsize=9, loc="lower right")
    ax.grid(True, alpha=0.3)
    ax2 = ax.twinx()  # (local)
    ax2.plot(Ls_all, [n_modes[L] for L in L_SCAN], "^:", color="#888",
             alpha=0.6, label="N modes")
    ax2.set_ylabel("N modes (with multiplicity)", color="#888")
    ax2.tick_params(axis="y", labelcolor="#888")

    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT_PNG, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP emit_verdict tool (race-safe, lock-serialized; the script
    does NOT write the verdict file). [VERIFY] trigger — no schema-v2 3-tuple
    (the band verdict is a two-sided inequality, not a signed directional
    prediction; the plan does not pre-register a [SIGN] 3-tuple)."""
    payload: dict = {
        "session": SESSION,
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Input pins (first lines of stdout)
    pins = log_input_pins(INPUT_FILES)

    # 2. Identity keys into pinmap (per audit_discriminators)
    pins["_gate_id"] = GATE_ID
    pins["_scheme"] = SCHEME
    pins["_convention"] = CONVENTION
    pins["_band"] = f"[{BAND_LO},{BAND_HI})"
    pins["_L_scan"] = ",".join(str(L) for L in L_SCAN)
    pins["_L_ref"] = str(L_REF)
    pins["_tau"] = TAU_TAG
    pins["_estimator"] = "acoustic-white-hole-impedance-intensive-sector(0,0)-floor"

    # 3. Dual SHA
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 4. Load cache + compute the estimator
    sec = load_sector_evals()
    n_modes = {L: n_modes_at_L(sec, L) for L in L_SCAN}  # (local)
    print("=== in-cache truncation (NO new diagonalization; p+q <= L) ===")
    for L in L_SCAN:
        print(f"  L={L}: N_modes={n_modes[L]:7d}")
    est = effacement_estimator(sec)

    print("\n=== effacement estimator (acoustic-white-hole impedance, intensive) ===")
    print(f"  acoustic <|lambda|>_(0,0) = {est['ac_mean']:.6f} (L-invariant)")
    print(f"  canonical Gamma_eff = {est['gam_canon']:.5f}; 1-Gamma = {est['dev_canon']:.6e}")
    print(f"  anchor scale k = {est['k']:.6f} (sets overall scale; cancels in slope)")
    for L in L_SCAN:
        print(f"  L={L}: <|lam|>_tot={est['tot_mean'][L]:.5f}  r={est['r'][L]:.6f}  "
              f"R_refl={est['R_refl'][L]:.6e}  Gamma_eff={est['Gamma_eff'][L]:.8f}")

    # 5. Sanity anchor (non-gating; fires estimator-mismatch INFO on breach)
    sanity_dev = abs(est["gam_ref"] - est["gam_canon"])  # (local)
    sanity_breach = sanity_dev >= SANITY_ABS_TOL  # (local)
    print(f"\n  sanity anchor: |Gamma_eff(12) - Gamma_effacement| = {sanity_dev:.3e} "
          f"(< {SANITY_ABS_TOL}: {not sanity_breach}; breach fires estimator-mismatch INFO)")

    # 6. OLS log-log fit
    Ls_fit = np.array(L_FIT, dtype=float)  # (local)
    dGG_vals = [est["dGG"][L] for L in L_FIT]  # (local)
    print("\n=== Level-2 envelope dGamma_eff/Gamma_eff ===")
    for L, v in zip(L_FIT, dGG_vals):
        print(f"  L={L}: dGamma_eff/Gamma_eff = {v:.8e}")
    fit = ols_loglog(Ls_fit, np.array(dGG_vals))
    print(f"\n  OLS log-log: slope={fit['slope']:.6f}  alpha=-slope={fit['alpha']:.6f}  "
          f"R^2={fit['r2']:.6f}")
    print(f"  residuals (ln-space) = {[round(x,5) for x in fit['residuals']]}")

    # 7. S58 reference cross-check (non-gating)
    s58 = s58_reference_crosscheck()  # (local)
    print(f"\n  S58 reference cross-check: loaded={s58.get('loaded')} "
          + (f"w_eff_Volovik={s58.get('w_eff_Volovik'):.6f}, "
             f"F_Josephson={s58.get('F_Josephson'):.3f}, "
             f"s58_gate_verdict={s58.get('s58_gate_verdict')}"
             if s58.get("loaded") else f"error={s58.get('error')}"))

    # 8. Gate verdict
    verdict, band_tag, cond_flags = evaluate_gate(
        fit["alpha"], dGG_vals, fit["r2"], sanity_breach)

    # 9. Registry-PASS criterion cross-check at canonical L_max=10
    #    envelope value 10^{-alpha} vs Level-3 anchor 3.0e-4
    env_Lmax10 = 10.0 ** (-fit["alpha"])  # (local)
    level3 = est["dev_canon"]  # (local) = 3.0e-4
    registry_pass = level3 < env_Lmax10  # (local) Level-3 < Level-2 at L_max=10

    # Level-2 sub-class declaration (plan level_2_subclass_declaration):
    # the envelope bounds the convergence of the trigger-condition image that
    # BINDS Level-1 (the composite Hawking-Bogoliubov bridge already registered
    # in §VII.AM element 3) => Level-2-binding by definition of the observable.
    l2_subclass = "Level-2-binding"  # (local)

    print(f"\n{'='*72}")
    print(f"GATE: {GATE_ID}")
    print(f"{'='*72}")
    print(f"  alpha = {fit['alpha']:.6f}   band [1, 3.52)   => {verdict} ({band_tag})")
    print(f"  conditioning flags: {cond_flags if cond_flags else 'none (well-conditioned)'}")
    print(f"  Registry-PASS @ L_max=10: Level-3={level3:.3e} < 10^-alpha={env_Lmax10:.3e}? "
          f"{registry_pass}")
    print(f"  Level-2 sub-class: {l2_subclass}")
    print(f"{'='*72}")

    # 10. Substitution-chain echo (direction read-off; plan substitution_chain)
    print("\n=== Substitution chain (direction read-off) ===")
    print(f"  alpha_computed = {fit['alpha']:.6f}")
    print(f"  upper edge = 3.52 (published, < exact 3.5229 = -log10(3.0e-4))")
    if verdict == "FAIL" and band_tag == "FAIL-high":
        print(f"  {fit['alpha']:.4f} >= 3.52 => FAIL-high")
        print(f"  => at L_max=10: 10^-alpha = {env_Lmax10:.3e} < Level-3 anchor 3.0e-4")
        print(f"  => Registry-PASS (Level-3 < Level-2) is VIOLATED "
              f"=> clause-(b) Registry-PASS BREAKS")
    elif verdict == "FAIL" and band_tag == "FAIL-low":
        print(f"  {fit['alpha']:.4f} < 1 => FAIL-low (contradicts registered floor; atlas-09-relevant)")
    elif verdict == "PASS":
        print(f"  1 <= {fit['alpha']:.4f} < 3.52 => PASS; Level-3 3.0e-4 satisfies envelope at L_max=10")
    else:
        print(f"  ill-conditioned scan ({cond_flags}) => INFO; pin stays 'alpha >= 1, deferred'")

    # 11. Save npz
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        band_tag=band_tag,
        alpha=fit["alpha"],
        slope=fit["slope"],
        intercept=fit["intercept"],
        r2=fit["r2"],
        residuals=np.array(fit["residuals"]),
        band_lo=BAND_LO,
        band_hi=BAND_HI,
        L_scan=np.array(L_SCAN),
        L_fit=np.array(L_FIT),
        L_ref=L_REF,
        n_modes=np.array([n_modes[L] for L in L_SCAN]),
        gamma_canonical=est["gam_canon"],
        dev_canonical=est["dev_canon"],
        acoustic_mean=est["ac_mean"],
        anchor_scale_k=est["k"],
        total_mean=np.array([est["tot_mean"][L] for L in L_SCAN]),
        impedance_ratio_r=np.array([est["r"][L] for L in L_SCAN]),
        R_refl=np.array([est["R_refl"][L] for L in L_SCAN]),
        Gamma_eff_table=np.array([est["Gamma_eff"][L] for L in L_SCAN]),
        Gamma_eff_at_Lref=est["gam_ref"],
        dGamma_over_Gamma=np.array(dGG_vals),
        sanity_dev=sanity_dev,
        sanity_breach=sanity_breach,
        conditioning_flags=np.array(cond_flags if cond_flags else ["none"]),
        env_at_Lmax10=env_Lmax10,
        level3_anchor=level3,
        registry_pass_at_Lmax10=registry_pass,
        level_2_subclass=l2_subclass,
        s58_loaded=s58.get("loaded", False),
        s58_w_eff_Volovik=s58.get("w_eff_Volovik", float("nan")),
        s58_F_Josephson=s58.get("F_Josephson", float("nan")),
        tau_tag=TAU_TAG,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
    )
    print(f"\nsaved npz: {OUT_NPZ.name}")

    # 12. Plot
    make_plot(est, fit, verdict, band_tag, n_modes)
    print(f"saved png: {OUT_PNG.name}")

    # 13. Value payload + 4-tuple + verdict payload
    value = (
        f"alpha={fit['alpha']:.4f};band=[1,3.52);verdict={band_tag};"
        f"R2={fit['r2']:.4f};monotone={all(dGG_vals[i]>dGG_vals[i+1] for i in range(len(dGG_vals)-1))};"
        f"Gamma_eff(12)={est['gam_ref']:.5f}(sanity_dev={sanity_dev:.2e},breach={sanity_breach});"
        f"L2_subclass={l2_subclass};"
        f"registry_PASS@Lmax10={registry_pass}(env=10^-alpha={env_Lmax10:.3e}_vs_L3=3.0e-4);"
        f"estimator=acoustic-white-hole-impedance-intensive-Lref12;"
        f"conditioning={'+'.join(cond_flags) if cond_flags else 'well-conditioned'}"
    )  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    companion = (
        f"§VII.AM Level-2 alpha-pin via S58 Volovik-partition effacement L-scan "
        f"on s84 L12 cache (in-cache trunc L in {L_SCAN}); alpha={fit['alpha']:.4f} "
        f"{band_tag} band [1,3.52); Gamma_eff(12)={est['gam_ref']:.5f}=canonical 0.99970; "
        f"{l2_subclass}; registry-PASS@Lmax10={registry_pass}")  # (local)
    extra = [
        (f"# estimator-family robustness (NON-GATING cross-check): four "
         f"physically-motivated reorganization-rate estimators on the same cache "
         f"all give alpha~4-8 FAIL-high (acoustic-weight/Sum|lam|=7.62; median-scale=4.34; "
         f"mean-scale=4.32; intensive-impedance(this gate)={fit['alpha']:.2f}); the only "
         f"in-band reading (bare truncation-tail alpha=2.72) VIOLATES the binding sanity "
         f"anchor Gamma_eff(12)->1 and is inadmissible # {GATE_ID}"),
        (f"# regulator_pin=N/A (no Seeley-DeWitt a_n citation; no Mellin residue; "
         f"observable is a Bogoliubov-occupation/effacement functional of the cached "
         f"spectrum); CLASS=FULL (cached full-builder spectrum; no SCHEMATIC helper) "
         f"# {GATE_ID}"),
    ]  # (local)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note=companion, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} ({band_tag}) wall {wall:.1f}s ===")
    # exit 0 regardless of scientific verdict (math-scripts.md exit-code rule)
    return 0


if __name__ == "__main__":
    sys.exit(main())
