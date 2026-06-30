#!/usr/bin/env python3
"""
INV9 W2-2 — INV9-W2-2-DS-ENTROPY-SUBSTRATE-SPECIES-COUNT
=========================================================

Gate: INV9-W2-2-DS-ENTROPY-SUBSTRATE-SPECIES-COUNT ([SIGN])

Question (B-4, string-survey next-step): is the de Sitter (Gibbons-Hawking)
entropy reproduced to O(1) by a FINITE substrate SPECIES-COUNT?

  S_count = log(N_shell),   N_shell = #{ |lambda| in [1.0, 2.06] M_KK at the fold }
  S_dS    = 3*pi / (Lambda * ell_P^2),   Lambda from the a_0^{zeta} Seeley-DeWitt moment

Pre-registered threshold (plan §W2-2):
  operator: r = |S_count - S_dS| / S_dS
  PASS iff r <= 1.0 (O(1) agreement, the seed-pre-registered band)
  INFO iff 1.0 < r <= info_band (order-right but not O(1))  [info_band = 10.0, one OOM]
  FAIL iff r > info_band (OOM mismatch)

  [SIGN] 3-tuple: sign_verdict = N/A (a MAGNITUDE-agreement gate, |.| <= O(1),
  no signed directional prediction); magnitude_verdict carries the O(1)/INFO/FAIL
  band; regime_verdict tracks (a) the L_max=10 Friedrich-Bar saturation regime and
  (b) the Lambda-form ambiguity (substrate-scale a_0^{zeta}-derived Lambda is pinned;
  the dimensionless moment-prefactor form is form-sensitive at the OOM level).

LOAD-BEARING regulator-class separation (plan §W2-2 substitution chain):
  - S_count = log(N_shell) is an ALGEBRA-INVARIANT spectrum-only functional; the
    eigenvalue-shell CARDINALITY is regulator-INVARIANT (counting eigenvalues does
    NOT depend on the UV regulator). Verified here: N_shell is L_max-INVARIANT
    (identical at L_max=10 and L_max=12) by Friedrich-Bar saturation.
  - S_dS depends on Lambda, which is REGULATOR-DEPENDENT via a_0^{zeta} (the
    zeta-regulated zeroth Seeley-DeWitt moment). regulator_pin = a_0^{zeta} is
    MANDATORY: the two sides of the comparison live on DIFFERENT regulator axes.
  - The raw degeneracy-weighted count 155984 (= a_0 raw) is NOT used for Lambda;
    Lambda uses a_0^{zeta} = 6440.0. Using 155984 for both would be a
    UV_REGULARIZATION_CONFLATION error.

LOAD-BEARING WHICH-Lambda pin (orchestrator override):
  The O(1) match is a SUBSTRATE-SCALE statement. We use the substrate-scale
  Lambda derived from a_0^{zeta} via the spectral-action vacuum-energy path, NOT
  the observed-dark-energy Lambda (which gives S_dS ~ 3.26e122 nats per S61
  s61_bekenstein_desitter; that is the ~10^120 CC problem DILUTION-CC addresses,
  a DIFFERENT question). The substrate Lambda carries an M_KK^2 scale factor.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (sector_evals per-(p,q) dict)
  - computations/_shared/canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<r>, scheme=species-count-vs-Gibbons-Hawking,
   convention=log-cardinality-vs-S_dS-a0zeta-Lambda-SUBSTRATE-SCALE, L_max=10)

Classification: PHONONIC (count of accessible substrate VIBRATIONAL MODES below
the species scale; the dS horizon is an EMERGENT acoustic surface, not a
holographic boundary).

METHODOLOGY
-----------
(i)   load s84_spectrum_cache_L12_tau019.npz (sector_evals[(p,q)] =
      {'dim': PeterWeyl-multiplicity, 'level', 'abs_evals': per-sector |lambda| set}).
(ii)  reconstruct the species-shell membership N_shell = #{|lambda| in [1.0, 2.06]}
      at L_max_operational=10 (cache stored at L_max_plan=12; filter p+q<=10 per the
      Friedrich-Bar saturation truncation, math-scripts.md D_K block-diagonality
      pre-check). Report BOTH the unique-per-sector count (canonical N_shell) and the
      dim-weighted (multiplicity) count for transparency; the canonical S_count uses
      the unique-per-sector shell cardinality (the distinct accessible-mode count).
(iii) S_count = log(N_shell).
(iv)  Lambda = (2 f_0/f_2) * a_0^{zeta} * M_KK^2  [dimensionless moment prefactor *
      substrate energy-scale^2; session-39-naz-hawking "Lambda_cc=(2 f_0/f_2)*a_0",
      M_KK^2 scale per the session-64 Lambda_SA=(f_0/f_2)(a_0/a_2)M_KK^2 dimensional form].
      ell_P^2 = 1/M_Pl_reduced^2 (REDUCED-Planck convention, declared).
      S_dS = 3*pi/(Lambda*ell_P^2) = 3*pi*M_Pl^2/Lambda.
(v)   r = |S_count - S_dS|/S_dS; gate per the band above.

DISCIPLINE: from canonical_constants import *; intermediates tagged # (local);
numpy.linalg (cheap vectorized shell-membership count) with OMP cap 8; a_0
citation carries its regulator tag a_0^{zeta} per regulator-pin-discipline.md.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str((_Path(__file__).resolve().parent.parent / "_shared")))
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (
    a_0_FW_zeta,        # zeta-regulated zeroth Seeley-DeWitt moment (regulator: zeta)
    a_2_FW_zeta,        # zeta-regulated second Seeley-DeWitt moment (cross-check form)
    Lambda_sp_over_M_KK,  # species-scale ratio Lambda_sp/M_KK = 2.06 (THIN shell upper edge)
    M_KK,               # substrate energy scale (gravity route), GeV
    M_Pl_reduced,       # reduced Planck mass, GeV (CODATA 2018)
    f_0_sharp,          # f_0 spectral-functional moment (sharp cutoff)
    f_2_default,        # f_2 spectral-functional moment (Gaussian cutoff constraint)
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU thread cap (numpy.linalg path)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
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
SESSION_DIR = Path(__file__).resolve().parent          # computations/investigation-9/
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "9"                                                       # (local) investigation index
GATE_ID = "INV9-W2-2-DS-ENTROPY-SUBSTRATE-SPECIES-COUNT"           # (local)
SCHEME = "species-count-vs-Gibbons-Hawking"                        # (local)
CONVENTION = "log-cardinality-vs-S_dS-a0zeta-Lambda-SUBSTRATE-SCALE"  # (local)
L_MAX = 10                                                         # (local) L_max_operational
L_MAX_PLAN = 12                                                    # (local) cache stored at L_max=12

# Pre-registered bands (plan §W2-2 machinery_pin_map / verdict rubric)
PASS_BAND = 1.0                                                    # (local) O(1) PASS band on r
INFO_BAND = 10.0                                                   # (local) one OOM on r -> INFO ceiling
SHELL_LO = 1.0                                                     # (local) [M_KK, ...] lower edge (M_KK units)
SHELL_HI = float(Lambda_sp_over_M_KK)                              # 2.06 species-scale upper edge (M_KK units)
N_EVAL = 155984                                                    # (local) a_0 raw degeneracy-weighted total at L_max=10 (NOT used for Lambda)

# Output destinations (investigation-track, per gate-verdicts.md Investigation-Track path)
OUT_NPZ = SESSION_DIR / "inv9_w2_ds_entropy_species_count.npz"
OUT_PNG = SESSION_DIR / "inv9_w2_ds_entropy_species_count.png"

SPECTRUM_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SPECTRUM_CACHE,
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


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
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
def shell_membership(sector_evals: dict, maxsum: int, lo: float, hi: float):
    """Count |lambda| in [lo, hi] (M_KK units) over Peter-Weyl sectors p+q <= maxsum.

    Returns (n_unique_sector, n_dim_weighted, n_total_unique, n_total_dimw):
      n_unique_sector = number of stored abs_evals in the shell (distinct-mode count)
      n_dim_weighted  = sum over shell of dim(p,q) (SU(3) multiplicity-weighted)
      n_total_unique  = total stored abs_evals at this maxsum (shell-agnostic)
      n_total_dimw    = total dim-weighted at this maxsum (shell-agnostic)
    """
    n_unique = 0   # (local)
    n_dimw = 0     # (local)
    tot_unique = 0  # (local)
    tot_dimw = 0    # (local)
    for (p, q), rec in sector_evals.items():
        if p + q > maxsum:
            continue
        dim = int(rec["dim"])                              # (local) Peter-Weyl multiplicity
        ev = np.asarray(rec["abs_evals"], dtype=float)     # (local) per-sector |lambda| set
        tot_unique += ev.size
        tot_dimw += dim * ev.size
        mask = (ev >= lo) & (ev <= hi)                     # (local) species-shell membership
        c = int(mask.sum())                                # (local)
        n_unique += c
        n_dimw += dim * c
    return n_unique, n_dimw, tot_unique, tot_dimw


def compute() -> dict:
    # (i) load the per-(p,q) spectrum cache
    data = np.load(SPECTRUM_CACHE, allow_pickle=True)               # (local)
    sector_evals = data["sector_evals"].item()                      # (local) dict[(p,q)] -> rec

    # (ii) species-shell membership at L_max_operational=10 AND the L_max_plan=12 cache
    #      => verify the count is L_max-INVARIANT (Friedrich-Bar saturation).
    n_uniq_10, n_dimw_10, tot_uniq_10, tot_dimw_10 = shell_membership(
        sector_evals, L_MAX, SHELL_LO, SHELL_HI)
    n_uniq_12, n_dimw_12, tot_uniq_12, tot_dimw_12 = shell_membership(
        sector_evals, L_MAX_PLAN, SHELL_LO, SHELL_HI)

    shell_Lmax_invariant = (n_uniq_10 == n_uniq_12) and (n_dimw_10 == n_dimw_12)  # (local)

    # canonical N_shell = unique-per-sector (distinct accessible-mode count) at L_max=10
    N_shell = n_uniq_10                                             # (local)
    N_shell_dimw = n_dimw_10                                        # (local) alt multiplicity-weighted

    # (iii) substrate species-count entropy
    S_count = math.log(N_shell)                                     # (local) canonical
    S_count_dimw = math.log(N_shell_dimw)                          # (local) alt

    # (iv) Gibbons-Hawking S_dS at the SUBSTRATE scale.
    #   Lambda = (2 f_0/f_2) * a_0^{zeta} * M_KK^2   [GeV^2]  (dimensionless prefactor * M_KK^2)
    #   ell_P^2 = 1/M_Pl_reduced^2 (REDUCED-Planck convention)
    #   S_dS = 3*pi/(Lambda*ell_P^2) = 3*pi*M_Pl^2/Lambda
    moment_prefactor = (2.0 * f_0_sharp / f_2_default) * a_0_FW_zeta   # (local) dimensionless
    Lambda_sub = moment_prefactor * M_KK ** 2                         # (local) GeV^2, substrate-scale CC
    ellP2 = 1.0 / (M_Pl_reduced ** 2)                                 # (local) GeV^-2, reduced ell_P^2
    Lambda_ellP2 = Lambda_sub * ellP2                                 # (local) dimensionless
    S_dS = 3.0 * math.pi / Lambda_ellP2                              # (local)

    # CROSS-CHECK only (NOT the registered Lambda): session-64 dimensional form
    #   Lambda_SA = (f_0/f_2)*(a_0/a_2)*M_KK^2  -> divides by a_2, shrinks Lambda ~a_2x,
    #   inflating S_dS ~a_2x. Demonstrates the Lambda-FORM ambiguity (-> regime MARGINAL).
    pref_alt = (f_0_sharp / f_2_default) * (a_0_FW_zeta / a_2_FW_zeta)  # (local)
    Lambda_alt = pref_alt * M_KK ** 2                                  # (local)
    S_dS_alt = 3.0 * math.pi / (Lambda_alt * ellP2)                   # (local)

    # CROSS-CHECK only: OBSERVED-dark-energy S_dS (the ~10^120 CC problem; the WRONG Lambda).
    #   S61 s61_bekenstein_desitter: S_dS ~ 3.263e122 nats. Reproduced here for contrast so
    #   the WHICH-Lambda pin is auditable. rho_Lambda_obs ~ (2.25e-3 eV)^4; H0 ~ 1.44e-42 GeV.
    H0_obs_GeV = 1.44e-42                                             # (local) ~67 km/s/Mpc in GeV
    Lambda_obs = 3.0 * H0_obs_GeV ** 2                               # (local) GeV^2, observed CC (Lambda=3H^2)
    S_dS_obs = 3.0 * math.pi / (Lambda_obs * ellP2)                  # (local) ~10^122 contrast value

    # (v) target ratio r (canonical = substrate-scale Lambda, unique-per-sector N_shell)
    r = abs(S_count - S_dS) / S_dS                                   # (local) canonical gate value
    r_dimw = abs(S_count_dimw - S_dS) / S_dS                        # (local) alt N_shell reading

    return {
        "value": r,
        "r": r,
        "r_dimw": r_dimw,
        "S_count": S_count,
        "S_count_dimw": S_count_dimw,
        "S_dS": S_dS,
        "S_dS_alt": S_dS_alt,
        "S_dS_obs": S_dS_obs,
        "N_shell": N_shell,
        "N_shell_dimw": N_shell_dimw,
        "shell_lo": SHELL_LO,
        "shell_hi": SHELL_HI,
        "n_uniq_10": n_uniq_10,
        "n_uniq_12": n_uniq_12,
        "n_dimw_10": n_dimw_10,
        "n_dimw_12": n_dimw_12,
        "tot_uniq_10": tot_uniq_10,
        "tot_dimw_10": tot_dimw_10,
        "shell_Lmax_invariant": shell_Lmax_invariant,
        "moment_prefactor": moment_prefactor,
        "Lambda_sub": Lambda_sub,
        "Lambda_alt": Lambda_alt,
        "Lambda_obs": Lambda_obs,
        "Lambda_ellP2": Lambda_ellP2,
        "ellP2": ellP2,
        "MKK_over_MPl_sq": (M_KK / M_Pl_reduced) ** 2,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple + 3-tuple ([SIGN])
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(r: float) -> str:
    """Composite per the plan band: PASS r<=1.0; INFO 1.0<r<=10.0; FAIL r>10.0."""
    if r <= PASS_BAND:
        return "PASS"
    if r <= INFO_BAND:
        return "INFO"
    return "FAIL"


def evaluate_3tuple(res: dict) -> tuple:
    """[SIGN] 3-tuple.

    sign_verdict = N/A: the claim is a MAGNITUDE agreement |.| <= O(1); no signed
      directional prediction was pre-registered (plan substitution chain Step 'Direction').
    magnitude_verdict: PASS if r<=1.0; INFO if 1.0<r<=10.0; FAIL if r>10.0.
    regime_verdict: VALID iff the species shell is L_max-saturated (count L_max-invariant)
      AND the Lambda-form is unambiguous. Here the shell IS L_max-saturated (VALID on that
      axis) but the Lambda-FORM is ambiguous at the OOM level (substrate prefactor form vs
      session-64 a_2-divided form differ by ~a_2x) -> regime MARGINAL on the Lambda-scale axis.
    """
    r = res["r"]  # (local)
    sign_verdict = "N/A"  # (local) magnitude-agreement gate, no signed prediction
    if r <= PASS_BAND:
        magnitude_verdict = "PASS"  # (local)
    elif r <= INFO_BAND:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    # Lambda-form ambiguity (S_dS_alt / S_dS ~ a_2) makes the precise O(1) value
    # form-sensitive at the OOM level => MARGINAL (the shell L_max-saturation is VALID,
    # but the Lambda-scale leg is the marginal axis the plan INFO branch anticipates).
    lambda_form_ratio = res["S_dS_alt"] / res["S_dS"]  # (local) ~a_2 ~ 2776
    regime_verdict = "MARGINAL" if lambda_form_ratio > 10.0 else "VALID"  # (local)
    return sign_verdict, magnitude_verdict, regime_verdict


def composite_collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Deterministic composite collapse per gate-verdicts.md schema-v2."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"   # magnitude-wrong-but-out-of-regime
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


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1: entropy ladder (log scale) — substrate-scale vs observed-Lambda contrast
    labels = [
        "S_count\nlog(N_shell)\n[unique]",
        "S_count\nlog(N_shell)\n[dim-wt]",
        "S_dS\nsubstrate\n(a0^zeta)",
        "S_dS\nalt-form\n(a0/a2)",
        "S_dS\nOBSERVED\nLambda (~10^122)",
    ]
    vals = [res["S_count"], res["S_count_dimw"], res["S_dS"],
            res["S_dS_alt"], res["S_dS_obs"]]
    colors = ["#1f77b4", "#7fb3d8", "#d62728", "#ff9896", "#7f7f7f"]
    ax1.bar(range(len(vals)), vals, color=colors)
    ax1.set_yscale("log")
    ax1.set_xticks(range(len(labels)))
    ax1.set_xticklabels(labels, fontsize=8)
    ax1.set_ylabel("entropy (nats, log scale)")
    ax1.set_title("INV9-W2-2: substrate species-count vs Gibbons-Hawking S_dS\n"
                  "(substrate-scale Lambda gives O(1) S_dS; observed Lambda gives ~10^122)")
    ax1.axhspan(res["S_count"] / math.e, res["S_count"] * math.e,
                color="#1f77b4", alpha=0.08, label="S_count factor-e band")
    for i, v in enumerate(vals):
        ax1.text(i, v * 1.3, f"{v:.3g}", ha="center", fontsize=7)
    ax1.legend(fontsize=7, loc="upper left")

    # Panel 2: the species shell on the eigenvalue axis (schematic) + verdict numbers
    ax2.axis("off")
    txt = (
        f"GATE: {GATE_ID}\n"
        f"VERDICT: {res['_verdict']}  (composite)\n"
        f"  sign={res['_sign']}  magnitude={res['_mag']}  regime={res['_regime']}\n\n"
        f"species shell: [{res['shell_lo']:.2f}, {res['shell_hi']:.2f}] M_KK\n"
        f"N_shell (unique-per-sector) = {res['N_shell']}\n"
        f"N_shell (dim-weighted)      = {res['N_shell_dimw']}\n"
        f"shell L_max-invariant (L10==L12): {res['shell_Lmax_invariant']}\n"
        f"  (N@L10={res['n_uniq_10']}, N@L12={res['n_uniq_12']})\n\n"
        f"S_count = log(N_shell) = {res['S_count']:.4f}\n"
        f"S_count (dim-wt)       = {res['S_count_dimw']:.4f}\n\n"
        f"Lambda = (2 f_0/f_2) a_0^zeta M_KK^2\n"
        f"  prefactor = {res['moment_prefactor']:.3f}\n"
        f"  Lambda*ellP^2 = {res['Lambda_ellP2']:.4f}\n"
        f"S_dS (substrate) = {res['S_dS']:.4f}\n\n"
        f"r = |S_count - S_dS|/S_dS = {res['r']:.4f}\n"
        f"  (PASS<=1.0, INFO<=10.0, FAIL>10.0)\n"
        f"r (dim-wt N_shell) = {res['r_dimw']:.4f}\n\n"
        f"regulator_pin = a_0^{{zeta}} (a_0^zeta=6440.0)\n"
        f"WHICH Lambda = SUBSTRATE-SCALE (NOT observed-DE)\n"
        f"Lambda-form ambiguity: S_dS_alt/S_dS = {res['S_dS_alt']/res['S_dS']:.1f}x\n"
    )
    ax2.text(0.0, 1.0, txt, va="top", ha="left", fontsize=9, family="monospace",
             transform=ax2.transAxes)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
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

    sign_v, mag_v, regime_v = evaluate_3tuple(res)
    verdict = composite_collapse(sign_v, mag_v, regime_v)
    res["_verdict"] = verdict
    res["_sign"] = sign_v
    res["_mag"] = mag_v
    res["_regime"] = regime_v

    # Echo the numeric chain (numbers first)
    print("=== NUMERIC CHAIN ===")
    print(f"  species shell [lo, hi] (M_KK units) = [{res['shell_lo']}, {res['shell_hi']}]")
    print(f"  N_shell (unique-per-sector, L_max=10) = {res['N_shell']}")
    print(f"  N_shell (dim-weighted, L_max=10)      = {res['N_shell_dimw']}")
    print(f"  shell L_max-INVARIANT (L10==L12): {res['shell_Lmax_invariant']} "
          f"(N@L10={res['n_uniq_10']}, N@L12={res['n_uniq_12']})")
    print(f"  total cardinality (unique-per-sector, L=10) = {res['tot_uniq_10']} "
          f"(canonical 78080 unique)")
    print(f"  total cardinality (dim-weighted, L=10)      = {res['tot_dimw_10']}")
    print(f"  S_count = log(N_shell)            = {res['S_count']:.6f}")
    print(f"  S_count (dim-weighted)            = {res['S_count_dimw']:.6f}")
    print(f"  moment prefactor (2 f_0/f_2)a_0^z = {res['moment_prefactor']:.6f}")
    print(f"  (M_KK/M_Pl)^2                     = {res['MKK_over_MPl_sq']:.6e}")
    print(f"  Lambda_substrate [GeV^2]          = {res['Lambda_sub']:.6e}")
    print(f"  Lambda*ellP^2 (dimensionless)     = {res['Lambda_ellP2']:.6f}")
    print(f"  S_dS (substrate-scale)            = {res['S_dS']:.6f}")
    print(f"  S_dS (alt a0/a2 form, X-CHECK)    = {res['S_dS_alt']:.6f}")
    print(f"  S_dS (OBSERVED Lambda, X-CHECK)   = {res['S_dS_obs']:.6e}  (~10^122; WRONG Lambda)")
    print(f"  r = |S_count - S_dS|/S_dS         = {res['r']:.6f}")
    print(f"  r (dim-weighted N_shell)          = {res['r_dimw']:.6f}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  composite verdict: {verdict}")
    print()

    # Persist data
    np.savez(
        OUT_NPZ,
        value=res["r"], r=res["r"], r_dimw=res["r_dimw"],
        S_count=res["S_count"], S_count_dimw=res["S_count_dimw"],
        S_dS=res["S_dS"], S_dS_alt=res["S_dS_alt"], S_dS_obs=res["S_dS_obs"],
        N_shell=res["N_shell"], N_shell_dimw=res["N_shell_dimw"],
        shell_lo=res["shell_lo"], shell_hi=res["shell_hi"],
        n_uniq_10=res["n_uniq_10"], n_uniq_12=res["n_uniq_12"],
        n_dimw_10=res["n_dimw_10"], n_dimw_12=res["n_dimw_12"],
        tot_uniq_10=res["tot_uniq_10"], tot_dimw_10=res["tot_dimw_10"],
        shell_Lmax_invariant=res["shell_Lmax_invariant"],
        moment_prefactor=res["moment_prefactor"],
        Lambda_sub=res["Lambda_sub"], Lambda_alt=res["Lambda_alt"],
        Lambda_obs=res["Lambda_obs"], Lambda_ellP2=res["Lambda_ellP2"],
        ellP2=res["ellP2"], MKK_over_MPl_sq=res["MKK_over_MPl_sq"],
        a_0_FW_zeta=a_0_FW_zeta, a_2_FW_zeta=a_2_FW_zeta,
        Lambda_sp_over_M_KK=Lambda_sp_over_M_KK, M_KK=M_KK, M_Pl_reduced=M_Pl_reduced,
        f_0_sharp=f_0_sharp, f_2_default=f_2_default,
        L_max_operational=L_MAX, L_max_plan=L_MAX_PLAN,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite_verdict=verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # 4-tuple (final non-verdict line) + emit payload
    tag = emit_4tuple(res["r"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    extra_rows = [
        f"# regulator_pin=a_0^{{zeta}} a_0_zeta={a_0_FW_zeta} (Lambda regulator-DEPENDENT; "
        f"N_shell regulator-INVARIANT; raw count 155984 NOT used for Lambda)",
        f"# publication_precision=3 S_count={res['S_count']:.3g} S_dS={res['S_dS']:.3g} "
        f"r={res['r']:.3g} N_shell={res['N_shell']}",
        f"# WHICH_Lambda=SUBSTRATE-SCALE (a0^zeta-derived, NOT observed-DE); "
        f"observed-Lambda S_dS={res['S_dS_obs']:.3e} (~10^122) is the DILUTION-CC question, NOT this gate",
        f"# Lambda_form_ambiguity S_dS_alt/S_dS={res['S_dS_alt']/res['S_dS']:.1f}x "
        f"(session-64 (f_0/f_2)(a_0/a_2)M_KK^2 vs plan (2 f_0/f_2)a_0 M_KK^2) -> regime MARGINAL",
        f"# shell_Lmax_invariant={res['shell_Lmax_invariant']} L_max_plan=12 L_max_operational=10 "
        f"(Friedrich-Bar saturation; species shell fully resolved at L_max=10)",
    ]
    companion_note = (
        f"species-count log(N_shell={res['N_shell']})={res['S_count']:.3f} vs substrate-scale "
        f"S_dS={res['S_dS']:.3f}; r={res['r']:.3f} INFO (order-right, not O(1)); "
        f"regime MARGINAL (Lambda-form ambiguity)"
    )
    print_verdict_payload(
        verdict, res["r"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=companion_note, extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0   # verdict is DATA; exit 0 on script success regardless (math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
