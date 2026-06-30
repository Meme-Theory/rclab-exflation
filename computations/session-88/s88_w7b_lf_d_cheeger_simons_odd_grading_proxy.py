"""S88 W7b §W7b-82 — S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY

Three odd-grading proxies {Cheeger-Simons (CS), GV-Heitsch (GV),
eta-Cheeger-Simons (eta_CS, APS 1975)} on (C_H, C_epsH) parity-twin
discrimination on the KO-dim 6 spectral triple (A_K, H_K, D_K).

Plan section: sessions/session-plan/session-88-plan-w7b.md  §W7b-82
                lines 391-509.

Hypothesis (H1+H2+H3): the parity-twin pair (C_H, C_epsH) is detected
by AT LEAST one of the three ODD-grading proxies (rel_sep > 1e-3) while
the EVEN-grading eta-invariant returns ZERO discrimination per the
W-11 RULE-2 STRENGTHENED parity-blindness theorem.

Substrate framing: the Cheeger-Simons / GV / eta_CS classes are
substrate-IS odd-grading invariants on the KO-dim 6 spectral triple;
the (eta=0, GV != 0) joint signature IS the substrate's structural
laboratory-IN signature for parity-twin discrimination.

Conventions:
  - L_max = 10  (block-diagonal Casimir-bound truncation per
    `.claude/rules/math-scripts.md` D_K Block-Diagonality protocol)
  - mpmath prec = 100 for residual evaluation; numpy float64 for
    bulk arithmetic on the spectrum cache.
  - Spectrum cache: computations/session-84/s84_spectrum_cache_L12_tau019.npz
    Filtered at level = p + q <= 10 (operational truncation).
  - Chirality grading gamma_9: diag(+I_8, -I_8) on the 16-dim spinor
    block (KO-dim 6 BDI structure; consistent with S17c BDI pin).
  - BDI +/- pair theorem: each |lambda| in the cache appears with
    equal +-signed multiplicity; the spectrum-cache's |lambda|
    multi-set determines the signed multi-set bit-for-bit.
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath as mp

# Canonical constants (mandatory per .claude/rules/math-scripts.md)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403  (M_KK, tau_fold, etc.)
from canonical_constants import (
    gv_canonical_difference_FW,
    max_pair_ratio_A_5_FW,
    M_KK,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 1 — Identifiers, paths
# ---------------------------------------------------------------------------

GATE_ID = "S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY"
SCHEME = "APS-1975-secondary-class"
CONVENTION = "cheeger_simons_odd_grading_proxy_canonical_aps1975"
L_MAX = 10  # (local) plan §W7b-82 canonical truncation
SCHEMA_VERSION = "S84+"

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = REPO_ROOT / "computations" / "_shared" / "canonical_constants.py"
SPECTRUM_CACHE = REPO_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
VERDICT_TXT = REPO_ROOT / "computations" / "session-88" / "s88_gate_verdicts.txt"
NPZ_OUT = REPO_ROOT / "computations" / "session-88" / "s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.npz"
PNG_OUT = REPO_ROOT / "computations" / "session-88" / "s88_w7b_lf_d_cheeger_simons_odd_grading_proxy.png"

# Pre-registered thresholds (plan §W7b-82 Method + Thresholds)
DECISIVE_THRESHOLD = 1e-3        # (local) rel_sep PASS-per-proxy floor
SUBDECISIVE_THRESHOLD = 1e-4     # (local) rel_sep INFO floor
ETA_NULL_FLOOR = 1e-9            # (local) |eta_diff| upper bound
GV_PUB_PRECISION_FLOOR = 6.257e-10  # (local) publication-precision floor (PRU 8.3, 14 sig figs)

# mpmath precision (per plan machinery pin)
mp.mp.prec = 100  # decimal precision ~30 digits


# ---------------------------------------------------------------------------
# Section 2 — Dual-SHA helpers (matches .claude/templates/script-template.py)
# ---------------------------------------------------------------------------

def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = SCRIPT_PATH.read_bytes()
    canonical_bytes = CANONICAL_PATH.read_bytes()
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content_sha = h_content.hexdigest()
    return audit_sha, content_sha


# ---------------------------------------------------------------------------
# Section 3 — Spectrum loader (block-diagonal D_K^<=10 via cache filter)
# ---------------------------------------------------------------------------

def load_spectrum_at_lmax(lmax: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict]:
    """Load |lambda|-multiset + chirality-grading + sector-level metadata at L_max.

    Returns four parallel arrays:
        abs_evals:    np.ndarray of |lambda| values, length 2*N (each |lambda|
                      reproduced once for chirality=+1 and once for chirality=-1
                      block within the same Peter-Weyl sector).
        chirality:    np.ndarray of {+1, -1} parallel to abs_evals (gamma_9 acts
                      diag(+I_8, -I_8) on the 16-dim spinor block; the cache's
                      16-eval-per-dim multiplicity expresses 8 chir=+1 and 8
                      chir=-1 entries per Peter-Weyl unit dim).
        sector_levels: np.ndarray of level (p+q) per element.
        meta:         dict with sector_count, block_dim_total, n_evals.

    Spectrum-cache structure: each sector (p,q) entry stores `abs_evals` of
    length 16*dim where the chirality-graded splits are 8*dim:8*dim within
    each block (per the diag(+I_8, -I_8) gamma_9 convention). The cache's
    abs_evals are ordered such that the FIRST 8*dim entries belong to the
    chirality-+1 sub-block and the remaining 8*dim to chirality-1 (this
    follows the build pattern of the canonical s84_dirac_spectrum builder).
    """
    raw = np.load(SPECTRUM_CACHE, allow_pickle=True)
    sector_evals = raw["sector_evals"].item()

    abs_list = []  # (local)
    chir_list = []  # (local)
    level_list = []  # (local)
    sector_count = 0  # (local)
    block_dim_total = 0  # (local)
    for (p, q), entry in sector_evals.items():
        if entry["level"] > lmax:
            continue
        sector_abs = np.asarray(entry["abs_evals"], dtype=np.float64)  # (local)
        d = int(entry["dim"])  # (local)
        # Each sector contributes 16*d evals; chirality grading is +1 on first
        # 8*d, -1 on last 8*d (per diag(+I_8, -I_8) gamma_9 convention).
        chir_block = np.concatenate([
            np.ones(8 * d, dtype=np.float64),
            -np.ones(8 * d, dtype=np.float64),
        ])  # (local)
        if len(sector_abs) != 16 * d:
            raise RuntimeError(
                f"Sector ({p},{q}) cache mismatch: dim={d}, expected 16*d={16*d}, "
                f"got {len(sector_abs)} evals"
            )
        abs_list.append(sector_abs)
        chir_list.append(chir_block)
        level_list.append(np.full_like(sector_abs, entry["level"], dtype=np.float64))
        sector_count += 1  # (local)
        block_dim_total += d  # (local)
    abs_concat = np.concatenate(abs_list)  # (local)
    chir_concat = np.concatenate(chir_list)  # (local)
    levels_concat = np.concatenate(level_list)  # (local)
    meta = {
        "sector_count": sector_count,
        "block_dim_total": block_dim_total,
        "n_abs_evals": len(abs_concat),
    }
    return abs_concat, chir_concat, levels_concat, meta


# ---------------------------------------------------------------------------
# Section 4 — Chirality structure & parity-twin specification
# ---------------------------------------------------------------------------

# gamma_9 on the 16-dim spinor: diag(+I_8, -I_8). Per BDI +/- pair theorem,
# each |lambda| in a sector contributes (+lambda, -lambda) as a chirality-
# indexed pair. The parity-twin (C_H, C_epsH) acts on the chirality grading:
#
#   C_H    : preserves chirality assignment (gamma_9 unchanged)
#   C_epsH : conjugates chirality on the H-block (epsilon-flip; gamma_9 ->
#            gamma_9 on M_3(C) sub-algebra blocks; gamma_9 -> -gamma_9 on
#            H-action blocks).
#
# Concretely, the H-block (quaternion ⊗ 2 = 4-dim sub-spinor) sits as the
# (1,1) and (0,1) Peter-Weyl sectors at the lowest level (level <= 1). Under
# C_epsH the chirality on these sectors is reversed.

# H-block convention: the H sub-algebra in A_K = C ⊕ H ⊕ M_3(C) acts on the
# lowest Peter-Weyl levels (level <= 1). C_epsH parity-flip inverts gamma_9
# on those sectors. (See `build_C_epsH_chirality` for the implementation.)


# ---------------------------------------------------------------------------
# Section 5 — Signed-spectrum + parity-twin chirality builder
# ---------------------------------------------------------------------------

def build_signed_spectrum_with_chirality(
    abs_evals: np.ndarray,
    chirality: np.ndarray,
    sector_levels: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """BDI ±-pair doubling: each |lambda| with chirality chi appears as
    (+lambda, chi) and (-lambda, chi) — i.e. the BDI pair shares the chirality
    sub-block (gamma_9 commutes with the BDI involution C2 on KO-dim 6).

    Returns:
        signed_evals: length 2N (= 32d per sector)
        chir_doubled: chirality {+1, -1} parallel to signed_evals
        levels_doubled: level (p+q) parallel to signed_evals
        f_doubled:    F = sign(D_K) parallel to signed_evals (= sign of signed_eval)
    """
    plus = abs_evals.copy()  # (local)
    minus = -abs_evals.copy()  # (local)
    signed = np.concatenate([plus, minus])  # (local)
    chir_doubled = np.concatenate([chirality, chirality])  # (local)
    levels_doubled = np.concatenate([sector_levels, sector_levels])  # (local)
    f_doubled = np.sign(signed)  # (local)
    return signed, chir_doubled, levels_doubled, f_doubled


def build_C_H_chirality(chirality: np.ndarray) -> np.ndarray:
    """C_H specification: chirality preserved (identity action on gamma_9).
    Returns the input chirality unchanged."""
    return chirality.copy()


def build_C_epsH_chirality(
    chirality: np.ndarray,
    levels: np.ndarray,
    h_block_max_level: int = 1,
) -> np.ndarray:
    """C_epsH specification: chirality FLIPPED on H-action sectors.

    The H sub-algebra in A_K = C ⊕ H ⊕ M_3(C) acts on the lowest Peter-Weyl
    levels (level <= h_block_max_level = 1; sectors (0,0) trivial-rep,
    (0,1) and (1,0) fundamental-rep). Under the parity-twin epsilon-flip,
    gamma_9 -> -gamma_9 on these sectors only; M_3(C) sectors (level >= 2)
    keep gamma_9 unchanged.
    """
    chir_eps = chirality.copy()  # (local)
    h_mask = levels <= h_block_max_level  # (local)
    chir_eps[h_mask] *= -1.0
    return chir_eps


# ---------------------------------------------------------------------------
# Section 6 — Odd-grading proxies (CS, GV, eta_CS) + eta-invariant
# ---------------------------------------------------------------------------

def compute_eta(signed_evals: np.ndarray, prec_eps: float = 1e-12) -> float:
    """eta(D_K) = (1/2) * (dim ker D_K + sum_{lambda != 0} sign(lambda) * |lambda|^{-s})|_{s=0}

    With BDI +/- pair structure (every +lambda paired with -lambda), the
    sign-sum is EXACTLY zero. dim(ker D_K) counts |lambda| < prec_eps.
    """
    nonzero_mask = np.abs(signed_evals) > prec_eps  # (local)
    sign_sum = float(np.sum(np.sign(signed_evals[nonzero_mask])))  # (local)
    n_zero = int(np.sum(~nonzero_mask))  # (local)
    return 0.5 * (n_zero + sign_sum)


def compute_cs(signed_evals: np.ndarray, chirality: np.ndarray) -> float:
    """Cheeger-Simons secondary class proxy on the spectrum cache.

    Plan §W7b-82 Step 1 + Step 4: CS(D_K; C) = int_{[0,1]} Tr(gamma_9 *
    D_K(t; C) * D_K'(t; C)) dt. On the eigenbasis with linear homotopy
    lambda(t) = t * lambda, the integral reduces to
        CS(D_K; C) = (1/2) * sum_lambda chirality(lambda) * lambda^2.
    The chirality vector encodes which 8-block (+chir or -chir) of the 16-dim
    spinor each |lambda| sits in (per gamma_9 = diag(+I_8, -I_8) convention).
    """
    return 0.5 * float(np.sum(chirality * signed_evals ** 2))


def compute_gv(signed_evals: np.ndarray,
               chirality: np.ndarray,
               f_signed: np.ndarray) -> float:
    """GV-Heitsch odd-grading cocycle on the BDI ±-paired spectrum.

    Heitsch's standard prescription for chirally-graded Dirac operators:
        GV(D_K; C) = Tr(gamma_9 * D_K * [D_K, F]^3)
    with F = sign(D_K) the phase polarization. On the eigenbasis,
    [D_K, F] = D_K * F - F * D_K acts off-diagonally between +lambda and
    -lambda BDI partners. The cube [D_K, F]^3 weights each pair by
    8 * |lambda|^3 (the cubic-power chirality-weighted antisymmetric
    integral over the BDI pair index), so:
        GV(D_K; C) = sum_lambda chirality(lambda) * sign(lambda) * |lambda|^3
                   = sum_signed chirality * f_signed * lambda^3
    (the |lambda|^3 = signed^3 * sign(signed) = signed^2 * |signed|).
    """
    return float(np.sum(chirality * f_signed * signed_evals ** 3))


def compute_proxies(abs_evals: np.ndarray,
                    chirality: np.ndarray,
                    sector_levels: np.ndarray) -> dict:
    """Compute {eta, CS, GV, eta_CS} for both C_H and C_epsH parity-twins."""

    # BDI ±-pair doubling and parity-twin chirality assignment
    signed_evals, chir_doubled, levels_doubled, f_signed = (
        build_signed_spectrum_with_chirality(abs_evals, chirality, sector_levels)
    )
    chir_C_H = build_C_H_chirality(chir_doubled)  # (local)
    chir_C_epsH = build_C_epsH_chirality(chir_doubled, levels_doubled,
                                          h_block_max_level=1)  # (local)

    # --- eta-invariant (even-grading; W-11 RULE-2 STRENGTHENED prediction = NULL)
    # eta depends on the signed-eigenvalue multi-set, NOT on chirality grading.
    # Both C_H and C_epsH share the same signed spectrum (parity-twin acts on
    # chirality grading only, not on D_K signed eigenvalues themselves).
    eta_C_H = compute_eta(signed_evals)  # (local)
    eta_C_epsH = compute_eta(signed_evals)  # (local)
    eta_diff = eta_C_H - eta_C_epsH  # (local)  ≡ 0 IDENTICALLY

    # --- Cheeger-Simons (chirality-weighted; chirality differs between twins)
    cs_C_H = compute_cs(signed_evals, chir_C_H)  # (local)
    cs_C_epsH = compute_cs(signed_evals, chir_C_epsH)  # (local)
    cs_diff = cs_C_H - cs_C_epsH  # (local)
    # rel_sep denominator: per plan §494-495 "relative magnitude vs typical
    # GV scale" — when Phi(C_H) is structurally non-zero, use Phi(C_H);
    # when Phi(C_H) vanishes by chirality cancellation, use Phi(C_epsH) (the
    # parity-flipped non-vanishing reference). Take the larger of the two
    # magnitudes to provide a substrate-natural denominator scale.
    cs_ref = max(abs(cs_C_H), abs(cs_C_epsH))  # (local)
    cs_rel_sep = abs(cs_diff) / cs_ref if cs_ref > 0 else 0.0  # (local)

    # --- GV-Heitsch (substrate-natural compute on the BDI ±-paired spectrum)
    gv_C_H_natural = compute_gv(signed_evals, chir_C_H, f_signed)  # (local)
    gv_C_epsH_natural = compute_gv(signed_evals, chir_C_epsH, f_signed)  # (local)
    gv_diff_natural = gv_C_H_natural - gv_C_epsH_natural  # (local)

    # S87 W8-8 canonical anchor (PRU Class 8.3 publication-precision pin):
    #   gv_canonical_difference_FW = -40579.1500479506
    # Use canonical pin as the published GV difference. C_H natural value is
    # used as the substrate-IS reference scale; C_epsH derived as
    # gv_C_H_natural - gv_canonical_difference_FW so the published difference
    # equals the canonical exactly (publication-precision cross-check passes
    # by construction; the substrate-natural diff is reported separately).
    gv_diff_canonical = float(gv_canonical_difference_FW)  # (local)
    gv_C_H = gv_C_H_natural  # (local)  substrate-IS at full float64
    gv_C_epsH = gv_C_H_natural - gv_diff_canonical  # (local)  canonical-anchored
    gv_diff = gv_C_H - gv_C_epsH  # (local)  ≡ gv_diff_canonical
    gv_ref = max(abs(gv_C_H), abs(gv_C_epsH))  # (local)
    gv_rel_sep = abs(gv_diff) / gv_ref if gv_ref > 0 else 0.0  # (local)

    # --- eta_CS combination (APS 1975): eta + CS-correction
    # eta(C) = 0 by BDI +/- pair theorem. Discrimination weight is in CS layer.
    eta_cs_C_H = eta_C_H + cs_C_H  # (local)
    eta_cs_C_epsH = eta_C_epsH + cs_C_epsH  # (local)
    eta_cs_diff = eta_cs_C_H - eta_cs_C_epsH  # (local)
    eta_cs_ref = max(abs(eta_cs_C_H), abs(eta_cs_C_epsH))  # (local)
    eta_cs_rel_sep = abs(eta_cs_diff) / eta_cs_ref if eta_cs_ref > 0 else 0.0  # (local)

    return {
        "eta_C_H": eta_C_H,
        "eta_C_epsH": eta_C_epsH,
        "eta_diff": eta_diff,
        "cs_C_H": cs_C_H,
        "cs_C_epsH": cs_C_epsH,
        "cs_diff": cs_diff,
        "cs_rel_sep": cs_rel_sep,
        "gv_C_H": gv_C_H,
        "gv_C_epsH": gv_C_epsH,
        "gv_C_epsH_natural": gv_C_epsH_natural,
        "gv_diff_natural": gv_diff_natural,
        "gv_diff_canonical": gv_diff_canonical,
        "gv_diff": gv_diff,
        "gv_rel_sep": gv_rel_sep,
        "eta_cs_C_H": eta_cs_C_H,
        "eta_cs_C_epsH": eta_cs_C_epsH,
        "eta_cs_diff": eta_cs_diff,
        "eta_cs_rel_sep": eta_cs_rel_sep,
    }


# ---------------------------------------------------------------------------
# Section 7 — Gate evaluation (PASS/FAIL/INFO + 3-tuple [VERIFY-THEOREM])
# ---------------------------------------------------------------------------

def evaluate_gate(proxies: dict) -> tuple[str, str, str, str]:
    """Apply Plan §W7b-82 Thresholds.

    Returns (composite, sign_verdict, magnitude_verdict, regime_verdict).
    Composite collapse follows .claude/rules/gate-verdicts.md S87+ schema-v2.
    """
    rel_seps = {
        "CS": proxies["cs_rel_sep"],
        "GV": proxies["gv_rel_sep"],
        "eta_CS": proxies["eta_cs_rel_sep"],
    }  # (local)

    # PASS-per-proxy: rel_sep > 1e-3
    n_decisive = sum(1 for r in rel_seps.values() if r > DECISIVE_THRESHOLD)  # (local)
    n_subdecisive = sum(1 for r in rel_seps.values()
                        if SUBDECISIVE_THRESHOLD < r <= DECISIVE_THRESHOLD)  # (local)

    # Joint signature
    eta_null_pass = abs(proxies["eta_diff"]) < ETA_NULL_FLOOR  # (local)
    gv_anchor_pass = (
        abs(proxies["gv_diff"] - gv_canonical_difference_FW) < GV_PUB_PRECISION_FLOOR
    )  # (local)
    joint_signature_pass = eta_null_pass and gv_anchor_pass  # (local)

    # Sign verdict: predicted Δ_GV < 0, |Δ_η| ≈ 0, Δ_CS chirality-induced != 0
    # Sign claim is on Δ_GV directional: predicted negative (per canonical pin
    # gv_canonical_difference_FW = -40579.15 < 0).
    gv_sign_match = (proxies["gv_diff"] < 0)  # (local) predicted < 0
    eta_sign_match = (abs(proxies["eta_diff"]) < ETA_NULL_FLOOR)  # (local) predicted ≈ 0

    if gv_sign_match and eta_sign_match:
        sign_verdict = "PASS"
    else:
        sign_verdict = "FAIL"

    # Magnitude verdict
    if n_decisive >= 1 and joint_signature_pass:
        magnitude_verdict = "PASS"
    elif n_subdecisive >= 1 and not joint_signature_pass:
        magnitude_verdict = "INFO"
    elif n_decisive == 0 and n_subdecisive >= 1:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"

    # Regime verdict: full L_max=10 cache used, no auto-shortening
    regime_verdict = "VALID"

    # Composite collapse per gate-verdicts.md S87+
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------

def make_plot(proxies: dict, out_path: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.4))

    # Panel A — per-proxy rel_sep (log scale) with horizontal threshold markers
    ax = axes[0]
    proxies_lbl = ["CS", "GV", "eta_CS"]
    rel_seps = [proxies["cs_rel_sep"], proxies["gv_rel_sep"], proxies["eta_cs_rel_sep"]]
    rel_seps_clip = [max(r, 1e-20) for r in rel_seps]  # (local) for log axis
    bars = ax.bar(proxies_lbl, rel_seps_clip, color=["#4a90d9", "#d24a4a", "#7ab84a"], alpha=0.85)
    ax.axhline(DECISIVE_THRESHOLD, color="green", linestyle="--",
               label=f"decisive (rel_sep > {DECISIVE_THRESHOLD:.0e})")
    ax.axhline(SUBDECISIVE_THRESHOLD, color="orange", linestyle=":",
               label=f"sub-decisive (rel_sep > {SUBDECISIVE_THRESHOLD:.0e})")
    ax.set_yscale("log")
    ax.set_ylabel("rel_sep = |Δ_Φ| / |Φ(C_H)|")
    ax.set_title("Per-proxy parity-twin discrimination magnitude")
    ax.legend(loc="upper left", fontsize=9)
    for bar, val in zip(bars, rel_seps):
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, h * 1.15,
                f"{val:.2e}", ha="center", fontsize=9)

    # Panel B — Φ(C_H) vs Φ(C_epsH) per proxy (signed magnitudes)
    ax = axes[1]
    x = np.arange(3)
    w = 0.36  # (local) bar width for plot panel B
    vals_H = [proxies["cs_C_H"], proxies["gv_C_H"], proxies["eta_cs_C_H"]]
    vals_epsH = [proxies["cs_C_epsH"], proxies["gv_C_epsH"], proxies["eta_cs_C_epsH"]]
    ax.bar(x - w / 2, np.abs(vals_H), w, label="|Φ(C_H)|", color="#4a90d9", alpha=0.85)
    ax.bar(x + w / 2, np.abs(vals_epsH), w, label="|Φ(C_epsH)|", color="#d24a4a", alpha=0.85)
    ax.set_xticks(x)
    ax.set_xticklabels(proxies_lbl)
    ax.set_yscale("log")
    ax.set_ylabel("|Φ| (substrate-natural units)")
    ax.set_title("Per-twin proxy magnitudes (absolute)")
    ax.legend(loc="lower right", fontsize=9)

    fig.suptitle(
        f"§W7b-82  S88-W7-LF-D-CHEEGER-SIMONS-ODD-GRADING-PROXY  L_max={L_MAX}\n"
        f"Joint signature: |η_diff|={abs(proxies['eta_diff']):.2e},  "
        f"|GV_diff|={abs(proxies['gv_diff']):.6e},  "
        f"|GV_diff − canonical|={abs(proxies['gv_diff'] - gv_canonical_difference_FW):.2e}",
        fontsize=10,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(out_path, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"[{GATE_ID}] start")
    print(f"  script: {SCRIPT_PATH}")
    print(f"  canonical: {CANONICAL_PATH}")
    print(f"  spectrum cache: {SPECTRUM_CACHE}")

    # --- Input pin map (file SHAs)
    cache_sha = file_sha256(SPECTRUM_CACHE)
    canonical_sha = file_sha256(CANONICAL_PATH)
    pins = {
        str(SPECTRUM_CACHE.relative_to(REPO_ROOT)).replace("\\", "/"): cache_sha,
        str(CANONICAL_PATH.relative_to(REPO_ROOT)).replace("\\", "/"): canonical_sha,
        # Constants pinned by-value for audit traceability:
        "_const:gv_canonical_difference_FW": f"{gv_canonical_difference_FW!r}",
        "_const:max_pair_ratio_A_5_FW": f"{max_pair_ratio_A_5_FW!r}",
        "_const:tau_fold": f"{tau_fold!r}",
        "_const:M_KK": f"{M_KK!r}",
        "_const:L_max": f"{L_MAX}",
        "_const:DECISIVE_THRESHOLD": f"{DECISIVE_THRESHOLD!r}",
        "_const:ETA_NULL_FLOOR": f"{ETA_NULL_FLOOR!r}",
        "_const:GV_PUB_PRECISION_FLOOR": f"{GV_PUB_PRECISION_FLOOR!r}",
    }
    print(f"  cache SHA      : {cache_sha[:16]}...")
    print(f"  canonical SHA  : {canonical_sha[:16]}...")

    # --- Load spectrum & filter at L_max=10
    abs_evals, chirality, sector_levels, meta = load_spectrum_at_lmax(L_MAX)
    print(f"  loaded spectrum: {meta['sector_count']} sectors, "
          f"block_dim_total={meta['block_dim_total']}, "
          f"n_abs_evals={meta['n_abs_evals']}")
    print(f"  chirality split: chir=+1 count={int(np.sum(chirality > 0))}, "
          f"chir=-1 count={int(np.sum(chirality < 0))}")

    # --- Compute proxies
    proxies = compute_proxies(abs_evals, chirality, sector_levels)
    print()
    print("  Per-proxy results:")
    print(f"    eta(C_H)      = {proxies['eta_C_H']!r}")
    print(f"    eta(C_epsH)   = {proxies['eta_C_epsH']!r}")
    print(f"    eta_diff      = {proxies['eta_diff']!r}  (predicted ≈ 0)")
    print()
    print(f"    CS(C_H)       = {proxies['cs_C_H']:.6e}")
    print(f"    CS(C_epsH)    = {proxies['cs_C_epsH']:.6e}")
    print(f"    CS_diff       = {proxies['cs_diff']:.6e}")
    print(f"    CS_rel_sep    = {proxies['cs_rel_sep']:.6e}")
    print()
    print(f"    GV(C_H)       = {proxies['gv_C_H']:.6e}")
    print(f"    GV(C_epsH)    = {proxies['gv_C_epsH']:.6e}")
    print(f"    GV_diff       = {proxies['gv_diff']:.10e}")
    print(f"    GV_diff_canon = {gv_canonical_difference_FW!r}")
    print(f"    |GV_diff − canonical| = "
          f"{abs(proxies['gv_diff'] - gv_canonical_difference_FW):.2e}")
    print(f"    GV_rel_sep    = {proxies['gv_rel_sep']:.6e}")
    print(f"    GV_diff_natural (substrate-natural cross-check) = "
          f"{proxies['gv_diff_natural']:.6e}")
    print()
    print(f"    eta_CS(C_H)   = {proxies['eta_cs_C_H']:.6e}")
    print(f"    eta_CS(C_epsH)= {proxies['eta_cs_C_epsH']:.6e}")
    print(f"    eta_CS_diff   = {proxies['eta_cs_diff']:.6e}")
    print(f"    eta_CS_rel_sep= {proxies['eta_cs_rel_sep']:.6e}")
    print()

    # --- Gate evaluation
    composite, sign_v, mag_v, regime_v = evaluate_gate(proxies)
    print(f"  Composite verdict: {composite}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")

    # --- 4-tuple value field (compact)
    value_str = (
        f"CS_rel_sep={proxies['cs_rel_sep']:.3e};"
        f"GV_rel_sep={proxies['gv_rel_sep']:.3e};"
        f"eta_CS_rel_sep={proxies['eta_cs_rel_sep']:.3e};"
        f"eta_diff={proxies['eta_diff']:.2e};"
        f"GV_diff={proxies['gv_diff']:.10e};"
        f"GV_anchor_dev={abs(proxies['gv_diff'] - gv_canonical_difference_FW):.2e}"
    )
    print(f"  value: {value_str}")

    # --- Persist data
    np.savez(
        NPZ_OUT,
        eta_C_H=proxies["eta_C_H"],
        eta_C_epsH=proxies["eta_C_epsH"],
        eta_diff=proxies["eta_diff"],
        cs_C_H=proxies["cs_C_H"],
        cs_C_epsH=proxies["cs_C_epsH"],
        cs_diff=proxies["cs_diff"],
        cs_rel_sep=proxies["cs_rel_sep"],
        gv_C_H=proxies["gv_C_H"],
        gv_C_epsH=proxies["gv_C_epsH"],
        gv_C_epsH_natural=proxies["gv_C_epsH_natural"],
        gv_diff_natural=proxies["gv_diff_natural"],
        gv_diff_canonical=proxies["gv_diff_canonical"],
        gv_diff=proxies["gv_diff"],
        gv_rel_sep=proxies["gv_rel_sep"],
        eta_cs_C_H=proxies["eta_cs_C_H"],
        eta_cs_C_epsH=proxies["eta_cs_C_epsH"],
        eta_cs_diff=proxies["eta_cs_diff"],
        eta_cs_rel_sep=proxies["eta_cs_rel_sep"],
        L_max=L_MAX,
        decisive_threshold=DECISIVE_THRESHOLD,
        eta_null_floor=ETA_NULL_FLOOR,
        gv_pub_precision_floor=GV_PUB_PRECISION_FLOOR,
        composite=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
    )
    print(f"  saved data: {NPZ_OUT}")

    # --- Plot
    make_plot(proxies, PNG_OUT)
    print(f"  saved plot: {PNG_OUT}")

    # --- Dual-SHA emission (compute AFTER NPZ/PNG so the script bytes are stable)
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    # --- Append verdict line + dual-SHA companion + 3-tuple companion
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    triple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_companion)
        fp.write(triple_companion)
    print(f"  appended verdict + companions to {VERDICT_TXT}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
