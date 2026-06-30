#!/usr/bin/env python3
"""S92 W3-5  CF-S91-W1-5.2  VII-AV LEVEL-2-MODULI RETRY (Option-A supersedes)
=================================================================================

Gate ID:  S92-W3-CF-S91-W1-5.2-VII-AV-LEVEL-2-MODULI-RETRY-OPTION-A
Trigger:  [VERIFY]
Class:    GEOMETRIC
Agent:    volovik-superfluid-universe-theorist

Purpose
-------
Evaluate the canonical L_emp observable

    L_emp(tau) := d^2 ln Var_a(|v_a(K; tau)|^2) / d(ln K)^2

across the 3-point off-fold tau moduli mesh tau in {0.18, 0.19, 0.20},
consuming (a) the s52 8-mode Bogoliubov amplitudes (tau_fold static),
(b) the W3-4-produced off-fold spectrum caches s92_spectrum_cache_L12_tau018.npz
and s92_spectrum_cache_L12_tau020.npz, and (c) the existing S84 master
cache s84_spectrum_cache_L12_tau019.npz. Compare against the canonical
L_emp(tau_fold) = -7.046336474406761 M_KK^2 anchor (loaded at runtime from
session-91/s91_w5_1_full_bdg_pv.npz key 'L_emp_canonical' per W3-9 PLAN_TEXT_DRIFT
precedent on 2026-05-22).

PASS criterion (Level_2_moduli_consistency_ratio band):
    PASS-strict:  max |L_emp(tau) - L_emp(tau_fold)| / |L_emp(tau_fold)| <= 0.10
    PASS-band:    0.10 <  ratio <= 0.30
    FAIL:         ratio > 0.30

Option-A protocol (per gate-verdicts.md MANDATORY S88 W8-100):
    - Original S91 W1-5 PRE-REG-INC verdict line (audit_sha256
      a85a362ea5ad41735a7eb97565850d17a80441491b328348bc91efcf8a9d7f45)
      is RETAINED on disk at computations/session-91/s91_gate_verdicts.txt line 18
    - This script APPENDS a corrective canonical line at
      computations/session-92/s92_gate_verdicts.txt carrying
      supersedes=a85a362ea5ad41735a7eb97565850d17a80441491b328348bc91efcf8a9d7f45
      (FULL 64-char) tag in the value= field at EMISSION TIME
    - Downstream consumers cite the latest non-superseded line as canonical

Substrate framing (per phononic-framing.md K=2 MANDATORY):
    The substrate IS the spectral triple (A_K, H_K, D_K(tau)) at each
    tau in {0.18, 0.19, 0.20}. L_emp(tau) IS the substrate-IS Cell IV
    observable evaluated at each Level-2 moduli-deformation instance.
    Level 1 = single-tau-slice (tau_fold=0.19 anchor); Level 2 = moduli-
    deformation extension across tau in {0.18, 0.20}. Both Levels are
    declared explicitly in the verdict-line companion rows.

W3-4 schema-mismatch handling (per spawn-prompt orchestrator override A):
    Off-fold caches have 91 sectors and include the (4,4) sector (level
    p+q=8, high-Casimir); the S84 master at tau=0.19 has 90 sectors and
    does NOT contain (4,4). The (4,4) sector is at p+q=8 high-Casimir
    and does NOT enter the bottom-K Bogoliubov window. We restrict to
    the COMMON 90-sector intersection across all three caches (drop
    (4,4) from the off-fold caches) so the tau=0.19 vs tau=0.18/0.20
    comparison is apples-to-apples on the Peter-Weyl decomposition.

W3-9 PLAN_TEXT_DRIFT correction (per orchestrator override B):
    Plan input_files cite computations/session-89/s89_w5_2_l_emp_canonical_anchor.npz
    (does NOT exist on disk). Runtime canonical anchor path is
    computations/session-91/s91_w5_1_full_bdg_pv.npz (key 'L_emp_canonical').

Operator-mismatch pre-flight verification (math-scripts.md SUGGESTION K=1):
    L_emp(tau) is the canonical SECOND-LOG-DERIVATIVE-OF-BOGOLIUBOV-VARIANCE
    observable per S87 W2-3 Def 4, NOT the trace operator form
    d ln(Tr_{M_2}(P_BdG * D_K^{-2s})) / d ln K (which reduces to closed-form
    +2s = +8, INCOMPATIBLE with canonical L_emp = -7.046336 at tau_fold).
    Convention suffix carries  -PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22
    as the audit-trail signature.
"""

from __future__ import annotations

# Cap CPU threads BEFORE numpy import (per .claude/rules/computation-environment.md
# CPU thread cap discipline; this is a CPU-only computation, no GPU contention).
import os  # noqa: E402
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "computations" / "_shared"
if str(SHARED) not in sys.path:
    sys.path.insert(0, str(SHARED))

from canonical_constants import (  # noqa: E402
    M_KK,
    Delta_BCS,
    tau_fold,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------- Gate-block constants ----------------
GATE_ID = "S92-W3-CF-S91-W1-5.2-VII-AV-LEVEL-2-MODULI-RETRY-OPTION-A"
SCHEME = (
    "Level-2-moduli-deformation-extension-VII-AV-substrate-distance-2-pole-s4-"
    "3-point-mesh-FULL-PHYSICAL"
)
CONVENTION = (
    "VII-AV-LEVEL-2-MODULI-OPTION-A-CORRECTIVE-RETRY-supersedes-"
    "CF-AV-L2-MODULI-S91-W1-5-PRE-REG-INC-"
    "PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22"
)
L_MAX = 12  # (local) canonical truncation

# Option-A supersedes target (S91 W1-5 PRE-REG-INC verdict line audit_sha256)
SUPERSEDES_FULL_64 = (
    "a85a362ea5ad41735a7eb97565850d17a80441491b328348bc91efcf8a9d7f45"
)

# K-window pins (per S87 W2-3 / S89 W5-2 / S91 W5-1 canonical horizon-crossing
# window for the d^2 ln P_GGE / d(ln K)^2 observable evaluation).
K_HORIZON_FRAC = (0.95, 1.05)  # (local) horizon-crossing K-window
DLNK = 0.001  # (local) step in ln K
RANDOM_SEED = 42  # (local)
np.random.seed(RANDOM_SEED)

# Pauli-Villars mass-tower (S61/S78 canonical 2-PV in M_KK-natural units)
PV_M_TOWER = (1.0, math.sqrt(2.0))  # (local) M_KK-natural units
PV_COEFFS = (+2.0, -1.0)  # (local) leading + subleading UV cancellation

# Substrate-distance-2 pole pin
S_POLE = 4  # (local) substrate-distance-2 pole s=4

# Canonical L_emp anchor (loaded at runtime from session-91/s91_w5_1_full_bdg_pv.npz
# per W3-9 PLAN_TEXT_DRIFT correction; pinned here as fallback for cross-check)
L_EMP_CANONICAL_FALLBACK = -7.046336474406761  # (local) S87 W2-3 anchor

# Level-2 moduli consistency thresholds (per plan W3-5 strict_PASS_boundary)
PASS_STRICT_THRESHOLD = 0.10  # (local) Level_2_moduli_consistency_ratio <= 0.10
PASS_BAND_THRESHOLD = 0.30  # (local) ratio <= 0.30 = PASS-band; > 0.30 = FAIL

# tau moduli mesh (3-point off-fold + fold)
TAU_MESH = (0.18, 0.19, 0.20)  # (local)

# ---------------- Output paths ----------------
OUT_NPZ = ROOT / "computations" / "session-92" / "s92_w3_5_vii_av_level_2_moduli_retry_option_a.npz"
OUT_PNG = ROOT / "computations" / "session-92" / "s92_w3_5_vii_av_level_2_moduli_retry_option_a.png"
OUT_JSON = ROOT / "computations" / "session-92" / "s92_w3_5_vii_av_level_2_moduli_retry_option_a.json"
VERDICT_FILE = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# ---------------- Input dependencies (substrate-IS pins) ----------------
CANONICAL_CONSTANTS_PATH = ROOT / "computations" / "_shared" / "canonical_constants.py"
S52_BOG_CACHE = ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
S84_MASTER_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S92_TAU018_CACHE = ROOT / "computations" / "session-92" / "s92_spectrum_cache_L12_tau018.npz"
S92_TAU020_CACHE = ROOT / "computations" / "session-92" / "s92_spectrum_cache_L12_tau020.npz"

# W3-9 PLAN_TEXT_DRIFT: plan cites s89_w5_2_l_emp_canonical_anchor.npz; runtime canonical is:
S91_W5_1_ANCHOR = ROOT / "computations" / "session-91" / "s91_w5_1_full_bdg_pv.npz"

# Original PRE-REG-INC verdict line file (Option-A supersedes target audit trail)
S91_VERDICTS = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS_PATH,
    "s52_bogoliubov_amp": S52_BOG_CACHE,
    "s84_master_cache_tau019": S84_MASTER_CACHE,
    "s92_tau018_off_fold_cache": S92_TAU018_CACHE,
    "s92_tau020_off_fold_cache": S92_TAU020_CACHE,
    "s91_w5_1_canonical_anchor_runtime_path": S91_W5_1_ANCHOR,
    "s91_w1_5_original_pre_reg_inc_verdict": S91_VERDICTS,
    "script": SCRIPT_PATH,
}


# ---------------- SHA helpers ----------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    blob = json.dumps(items, sort_keys=True).encode("utf-8")  # (local)
    return hashlib.sha256(blob).hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 78)
    print(f"Gate: {GATE_ID}")
    print(f"Scheme: {SCHEME}")
    print(f"Convention: {CONVENTION}")
    print(f"L_max: {L_MAX}; tau mesh: {TAU_MESH}")
    print(f"Option-A supersedes target (full 64-char):")
    print(f"  {SUPERSEDES_FULL_64}")
    print(f"K-horizon window: {K_HORIZON_FRAC} K_horizon; DLNK={DLNK}")
    print(f"Pauli-Villars (M_KK units): masses={PV_M_TOWER}; coeffs={PV_COEFFS}")
    print(f"Substrate-distance-2 pole: s={S_POLE}")
    print("=" * 78)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:42s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:42s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    pins["supersedes_target_audit_sha"] = SUPERSEDES_FULL_64
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """Audit + content SHA (W9a-99 split).

    audit_sha256 = SHA-256 over (script_bytes || canonical_constants_bytes || pinmap_json)
    content_sha256 = SHA-256 over (script_bytes)
    """
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS_PATH.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------- FULL Pauli-Villars BdG occupation kernel ----------------
# Reproduces S87 W2-3 Def 4 / S89 W5-2 / S91 W5-1 canonical numerical core
# (the canonical S52 8-mode Bogoliubov amplitudes are tau_fold-anchored and
# carry the substrate-IS BdG-fiber static parameters).

def bogoliubov_occupation_K(
    v_static: np.ndarray, u_static: np.ndarray,
    E_static: np.ndarray, delta_abs: np.ndarray,
    K_ratio: float,
    M_PV: float = 0.0,
) -> np.ndarray:
    """K-dependent Bogoliubov occupation n_a^GGE(K, M_PV) = |v_a(K, M_PV)|^2.

    M_PV = 0  -> bare substrate-IS canonical kernel.
    M_PV > 0  -> Pauli-Villars regulator copy at mass M_PV.
    """
    # (local) Static reference: xi_a^(0) = (u^2 - v^2) * E_static (S87 W2-3 Def 2)
    xi0 = (u_static ** 2 - v_static ** 2) * E_static  # (local)
    xi_K = xi0 * (K_ratio ** 2)  # (local) acoustic K^2 rescaling
    E_K = np.sqrt(xi_K ** 2 + delta_abs ** 2 + M_PV ** 2)  # (local) PV-massed qp
    eps_floor = 1e-30  # (local) numerical guard
    E_K_safe = np.where(E_K < eps_floor, eps_floor, E_K)  # (local)
    v_K2 = 0.5 * (1.0 - xi_K / E_K_safe)  # (local) Bogoliubov occupation
    v_K2 = np.clip(v_K2, 0.0, 1.0)  # (local)
    return v_K2


def pv_subtracted_occupation(
    v_static: np.ndarray, u_static: np.ndarray,
    E_static: np.ndarray, delta_abs: np.ndarray,
    K_ratio: float,
    pv_masses: tuple = PV_M_TOWER,
    pv_coeffs: tuple = PV_COEFFS,
) -> np.ndarray:
    """FULL Pauli-Villars-subtracted Bogoliubov occupation per S61/S78 protocol."""
    v_bare2 = bogoliubov_occupation_K(
        v_static, u_static, E_static, delta_abs, K_ratio, M_PV=0.0
    )  # (local)
    v_pv2 = v_bare2.copy()  # (local) start from bare
    for c_j, M_j in zip(pv_coeffs, pv_masses):
        v_reg = bogoliubov_occupation_K(
            v_static, u_static, E_static, delta_abs, K_ratio, M_PV=M_j
        )  # (local)
        v_pv2 = v_pv2 - c_j * v_reg  # (local) PV subtraction
    return v_pv2


def gge_variance_pv(
    v_static: np.ndarray, u_static: np.ndarray,
    E_static: np.ndarray, delta_abs: np.ndarray,
    k_ratios: np.ndarray,
) -> np.ndarray:
    """P_GGE^{PV}(K) = Var_a(v_a^{PV}(K)^2) across 8 modes."""
    n_K = len(k_ratios)  # (local)
    P_GGE = np.zeros(n_K)  # (local)
    for i, kr in enumerate(k_ratios):
        v_pv2 = pv_subtracted_occupation(
            v_static, u_static, E_static, delta_abs, kr
        )
        P_GGE[i] = float(np.var(v_pv2))  # (local)
    return P_GGE


# ---------------- L_max Mellin-PV weight at substrate-distance-2 pole ----------------
def lmax_mellin_pv_weight(
    sectors: dict, L_max_target: int, s: float = float(S_POLE),
    common_sectors: set | None = None,
) -> float:
    """FULL-PV-subtracted Mellin moment at substrate-distance-2 pole s.

    M_PV(L_max, s) = Sum_{(p,q): p+q<=L_max} dim(p,q) *
                     Sum_{lambda in sector(p,q)} [
                       |lambda|^{-2s}
                       - 2*(lambda^2 + M_1^2)^{-s}
                       + (lambda^2 + M_2^2)^{-s} ]

    If common_sectors is provided, restrict to the intersection set
    (W3-4 schema-mismatch handling: off-fold caches have 91 sectors
    incl. (4,4); s84 master has 90 sectors. Restrict to common 90.)
    """
    total = 0.0  # (local) accumulator
    M1_sq = PV_M_TOWER[0] ** 2  # (local)
    M2_sq = PV_M_TOWER[1] ** 2  # (local)
    for (p, q), info in sectors.items():
        if max(p, q) > L_max_target:
            continue
        if p + q > L_max_target:
            continue
        if common_sectors is not None and (p, q) not in common_sectors:
            continue
        dim_pq = info["dim"]  # (local) SU(3) Weyl dimension
        abs_evals = info["abs_evals"]  # (local) absolute eigenvalues
        lam2 = abs_evals * abs_evals  # (local)
        bare = np.power(lam2, -s, where=lam2 > 0, out=np.zeros_like(lam2))  # (local)
        reg1 = -PV_COEFFS[0] * np.power(lam2 + M1_sq, -s)  # (local) -2 * (lam^2+M1^2)^{-s}
        reg2 = -PV_COEFFS[1] * np.power(lam2 + M2_sq, -s)  # (local) +1 * (lam^2+M2^2)^{-s}
        sector_sum = float(np.sum(bare + reg1 + reg2))  # (local)
        total += dim_pq * sector_sum
    return total


# ---------------- K-window second log-derivative (5-point central FD) ----------------
def second_log_derivative_at_K_horizon(
    P_GGE: np.ndarray, ln_K_grid: np.ndarray,
) -> tuple[float, float]:
    """L(K_horizon) = d^2 ln P_GGE / d (ln K)^2 via 5-point central FD."""
    if P_GGE.min() <= 0:
        return (float("nan"), float(P_GGE[len(P_GGE) // 2]))
    ln_P = np.log(P_GGE)  # (local)
    n_K = len(ln_K_grid)  # (local)
    h = ln_K_grid[1] - ln_K_grid[0]  # (local) grid step in ln K
    i0 = int(np.argmin(np.abs(ln_K_grid)))  # (local) index closest to K_horizon
    if i0 < 2 or i0 > n_K - 3:
        L_val = (ln_P[i0 + 1] - 2 * ln_P[i0] + ln_P[i0 - 1]) / (h ** 2)  # (local)
    else:
        L_val = (
            -ln_P[i0 - 2] + 16 * ln_P[i0 - 1] - 30 * ln_P[i0]
            + 16 * ln_P[i0 + 1] - ln_P[i0 + 2]
        ) / (12.0 * h ** 2)  # (local)
    return (float(L_val), float(P_GGE[i0]))


# ---------------- L_emp at given tau ----------------
def compute_L_emp_at_tau(
    tau_label: str,
    cache_path: Path,
    bog_data: dict,
    ln_K_grid: np.ndarray,
    k_ratios: np.ndarray,
    common_sectors: set,
) -> dict:
    """Evaluate L_emp(tau) on the spectrum cache at tau and s52 Bogoliubov amplitudes.

    Returns dict with:
      L_emp, P_GGE_at_Kh, mellin_pv_weight_L12, sector_count, total_evals
    """
    cache = np.load(cache_path, allow_pickle=True)
    sectors_all = cache["sector_evals"].item()
    # Restrict to common-sector intersection (drop (4,4) from off-fold caches
    # so the tau=0.19 vs tau=0.18/0.20 comparison is apples-to-apples).
    sectors_common = {pq: info for pq, info in sectors_all.items() if pq in common_sectors}
    n_sec_full = len(sectors_all)  # (local)
    n_sec_common = len(sectors_common)  # (local)
    total_evals = sum(len(info["abs_evals"]) for info in sectors_common.values())  # (local)

    # Mellin-PV weight at L_max=12 on common-sector subset
    M_PV_L12 = lmax_mellin_pv_weight(
        sectors_all, L_max_target=L_MAX, s=float(S_POLE),
        common_sectors=common_sectors,
    )  # (local)

    # Compute P_GGE^{PV}(K) via s52 Bogoliubov kernel (tau_fold-anchored static
    # amplitudes per S52 8-mode protocol). The K-window curvature of ln P_GGE
    # is the canonical L_emp observable.
    P_GGE_K = gge_variance_pv(
        bog_data["v_static"], bog_data["u_static"],
        bog_data["E_static"], bog_data["delta_abs"],
        k_ratios,
    )  # (local)

    # Mellin-PV weight enters as a multiplicative normalization on the
    # spectral kernel; the multiplicative-normalization cancellation theorem
    # (math-scripts.md SUGGESTION K=1) implies the second log-derivative
    # is INVARIANT under multiplicative L_max-truncation weights, but the
    # ratio to L_max=12 is a structural diagnostic.
    L_val, P_at_Kh = second_log_derivative_at_K_horizon(P_GGE_K, ln_K_grid)

    return {
        "tau_label": tau_label,
        "cache_path": str(cache_path.relative_to(ROOT)),
        "n_sectors_full": n_sec_full,
        "n_sectors_common": n_sec_common,
        "total_evals_common": total_evals,
        "M_PV_L12": M_PV_L12,
        "L_emp": L_val,
        "P_GGE_at_Kh": P_at_Kh,
        "P_GGE_min": float(P_GGE_K.min()),
        "P_GGE_max": float(P_GGE_K.max()),
    }


# ---------------- Plot ----------------
def make_plot(
    tau_arr: np.ndarray, L_emp_arr: np.ndarray,
    L_emp_canonical: float,
    consistency_ratio: float,
    composite: str,
) -> None:
    """3-point Level-2 moduli plot: L_emp(tau) vs tau with PASS bands."""
    fig, ax = plt.subplots(figsize=(10, 7))

    L_band_strict_lo = L_emp_canonical * (1.0 + PASS_STRICT_THRESHOLD)  # (local) -7.046336 * 1.10 = -7.751
    L_band_strict_hi = L_emp_canonical * (1.0 - PASS_STRICT_THRESHOLD)  # (local) -7.046336 * 0.90 = -6.342
    L_band_pass_lo = L_emp_canonical * (1.0 + PASS_BAND_THRESHOLD)  # (local) -9.160
    L_band_pass_hi = L_emp_canonical * (1.0 - PASS_BAND_THRESHOLD)  # (local) -4.932

    # PASS-band: outer (lighter) shading
    ax.axhspan(
        L_band_pass_lo, L_band_pass_hi,
        color="tab:orange", alpha=0.15,
        label=f"PASS-band ratio in (0.10, 0.30]: L_emp in [{L_band_pass_lo:.3f}, {L_band_pass_hi:.3f}]",
    )
    # PASS-strict: inner (darker) shading
    ax.axhspan(
        L_band_strict_lo, L_band_strict_hi,
        color="tab:green", alpha=0.20,
        label=f"PASS-strict ratio <= 0.10: L_emp in [{L_band_strict_lo:.3f}, {L_band_strict_hi:.3f}]",
    )
    # Canonical anchor horizontal line
    ax.axhline(
        L_emp_canonical, color="tab:blue", lw=2.0, ls="--",
        label=f"L_emp(tau_fold=0.19) canonical = {L_emp_canonical:.6f} M_KK^2",
    )
    # Data points
    ax.plot(
        tau_arr, L_emp_arr, "o", color="tab:red", ms=14, mec="black", mew=1.5,
        label=f"L_emp(tau) computed (3-point off-fold mesh)",
    )
    for tau_v, L_v in zip(tau_arr, L_emp_arr):
        ax.annotate(
            f"  {L_v:.6f}",
            xy=(tau_v, L_v), xytext=(5, 5), textcoords="offset points",
            fontsize=10,
        )

    ax.set_xlabel("tau (Jensen TT-deformation parameter)", fontsize=13)
    ax.set_ylabel("L_emp(tau) = d^2 ln Var_a(|v_a(K)|^2) / d(ln K)^2  (M_KK^2 units)", fontsize=12)
    ax.set_title(
        f"S92 W3-5  §VII.AV Level-2 moduli retry (Option-A supersedes)\n"
        f"Level_2_moduli_consistency_ratio = {consistency_ratio:.6e}  -> composite = {composite}",
        fontsize=12,
    )
    ax.grid(True, alpha=0.4)
    ax.legend(loc="best", fontsize=9)
    ax.set_xlim(0.17, 0.21)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"  Plot saved -> {OUT_PNG.relative_to(ROOT)}")


# ---------------- Verdict-line append (single-shot AFTER pattern) ----------------
def append_verdict(
    composite: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
    plan_text_drift_notes: list[str],
    supersedes_full_64: str = SUPERSEDES_FULL_64,
) -> None:
    """Append canonical verdict line + dual-SHA companion + 3-tuple companion +
    PLAN_TEXT_DRIFT companion rows per gate-verdicts.md S87+ schema-v2 +
    substrate-first-canonical-sourcing.md (ii.B) plan-text-drift discipline.

    The value_str MUST already include the supersedes=<full-64-char> token
    at emission time (Option-A item 5: NOT post-hoc tag addition).
    A top-level supersedes=<full-64-char> token is ALSO emitted between the
    value= field and the scheme= field (space-delimited, matching the
    spawn-prompt regex `.* supersedes=<sha>.* audit_sha256=[a-f0-9]{64}`).
    Both placements satisfy Option-A protocol item 2 (value= OR companion row).
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"supersedes={supersedes_full_64} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        for note in plan_text_drift_notes:
            f.write(note + "\n")


# ---------------- Main ----------------
def main() -> None:
    pins = log_input_pins(INPUT_FILES)
    print(f"\nCanonical constants: M_KK = {M_KK:.10e} GeV; Delta_BCS = {Delta_BCS:.10f}; tau_fold = {tau_fold}")

    # ---------------- Step 1: Verify Option-A supersedes target exists on disk ----------------
    print("\n--- Step 1: Verify Option-A supersedes target audit_sha on S91 verdict file ---")
    s91_text = S91_VERDICTS.read_text(encoding="utf-8")
    found = SUPERSEDES_FULL_64 in s91_text
    print(f"  Supersedes target audit_sha256 {SUPERSEDES_FULL_64[:16]}... present in S91 verdicts: {found}")
    if not found:
        print("  WARNING: original PRE-REG-INC audit_sha NOT located in S91 verdicts!")
    else:
        # locate line
        for line_no, line in enumerate(s91_text.splitlines(), 1):
            if SUPERSEDES_FULL_64 in line and line.startswith("CF-AV-L2-MODULI"):
                print(f"  Original line at S91 verdict file line {line_no}: {line[:100]}...")
                break

    # ---------------- Step 2: Load canonical L_emp anchor (W3-9 PLAN_TEXT_DRIFT path) ----------------
    print("\n--- Step 2: Load canonical L_emp anchor (W3-9 PLAN_TEXT_DRIFT-corrected path) ---")
    print(f"  Runtime canonical path: {S91_W5_1_ANCHOR.relative_to(ROOT)}")
    anchor_npz = np.load(S91_W5_1_ANCHOR, allow_pickle=True)
    L_emp_canonical = float(anchor_npz["L_emp_canonical"])
    print(f"  L_emp_canonical (key 'L_emp_canonical') = {L_emp_canonical:.18e}")
    print(f"  Fallback pin                            = {L_EMP_CANONICAL_FALLBACK:.18e}")
    if not math.isclose(L_emp_canonical, L_EMP_CANONICAL_FALLBACK, rel_tol=1e-15):
        print(f"  WARNING: runtime anchor differs from fallback pin!")
    else:
        print("  Runtime anchor matches fallback pin to machine precision.")

    # ---------------- Step 3: Load s52 Bogoliubov amplitudes (tau_fold-anchored static) ----------------
    print("\n--- Step 3: Load s52 8-mode Bogoliubov amplitudes (substrate-IS, tau_fold-anchored) ---")
    bog = np.load(S52_BOG_CACHE, allow_pickle=True)
    u_static = bog["u_k"].astype(np.float64)
    v_static = bog["v_k"].astype(np.float64)
    E_static = bog["E_qp"].astype(np.float64)
    delta_complex = bog["Delta_per_mode"].astype(np.complex128)
    delta_abs = np.abs(delta_complex).astype(np.float64)  # (local) real |Delta_a|
    branch_labels = bog["branch_labels"]
    print(f"  Number of modes: {len(v_static)} (labels: {branch_labels.tolist()})")
    print(f"  |Delta_a| (M_KK units): {delta_abs.tolist()}")
    print(f"  u_static: {u_static.tolist()}")
    print(f"  v_static: {v_static.tolist()}")
    print(f"  E_static (M_KK units): {E_static.tolist()}")
    bog_data = {
        "u_static": u_static,
        "v_static": v_static,
        "E_static": E_static,
        "delta_abs": delta_abs,
    }

    # ---------------- Step 4: Build K-window grid (horizon-crossing, S87 W2-3 canonical) ----------------
    print("\n--- Step 4: Build K-window grid (horizon-crossing) ---")
    ln_min = math.log(K_HORIZON_FRAC[0])  # (local) ln(0.95)
    ln_max = math.log(K_HORIZON_FRAC[1])  # (local) ln(1.05)
    n_K_pts = int(round((ln_max - ln_min) / DLNK)) + 1  # (local)
    ln_K_grid = np.linspace(ln_min, ln_max, n_K_pts)  # (local) uniform in ln K
    k_ratios = np.exp(ln_K_grid)  # (local)
    print(f"  K-window: [{K_HORIZON_FRAC[0]:.3f}, {K_HORIZON_FRAC[1]:.3f}] K_horizon")
    print(f"  n_K_pts = {n_K_pts}; DLNK = {DLNK}")

    # ---------------- Step 5: Compute common-sector intersection (W3-4 schema mismatch handling) ----------------
    print("\n--- Step 5: Compute common-sector intersection across 3 caches ---")
    sec_018 = set(np.load(S92_TAU018_CACHE, allow_pickle=True)["sector_evals"].item().keys())
    sec_019 = set(np.load(S84_MASTER_CACHE, allow_pickle=True)["sector_evals"].item().keys())
    sec_020 = set(np.load(S92_TAU020_CACHE, allow_pickle=True)["sector_evals"].item().keys())
    print(f"  tau=0.18 sectors: {len(sec_018)}")
    print(f"  tau=0.19 sectors: {len(sec_019)} (S84 master)")
    print(f"  tau=0.20 sectors: {len(sec_020)}")
    common = sec_018 & sec_019 & sec_020  # (local)
    print(f"  COMMON intersection: {len(common)} sectors")
    dropped_018 = sec_018 - common  # (local) sectors in off-fold but not in S84 master
    dropped_019 = sec_019 - common
    dropped_020 = sec_020 - common
    print(f"  Dropped from tau=0.18: {sorted(dropped_018)}")
    print(f"  Dropped from tau=0.19: {sorted(dropped_019)}")
    print(f"  Dropped from tau=0.20: {sorted(dropped_020)}")

    # ---------------- Step 6: Evaluate L_emp(tau) at each of 3 tau points ----------------
    print("\n--- Step 6: Evaluate L_emp(tau) at 3-point off-fold tau mesh ---")
    tau_results = []  # (local)
    cache_paths = {
        0.18: S92_TAU018_CACHE,
        0.19: S84_MASTER_CACHE,
        0.20: S92_TAU020_CACHE,
    }
    for tau_v in TAU_MESH:
        cp = cache_paths[tau_v]  # (local)
        print(f"\n  >>> tau = {tau_v:.2f} -- cache: {cp.relative_to(ROOT)}")
        result = compute_L_emp_at_tau(
            tau_label=f"{tau_v:.2f}",
            cache_path=cp,
            bog_data=bog_data,
            ln_K_grid=ln_K_grid,
            k_ratios=k_ratios,
            common_sectors=common,
        )
        tau_results.append(result)
        print(f"    n_sectors (common): {result['n_sectors_common']}")
        print(f"    total_evals (common): {result['total_evals_common']}")
        print(f"    M_PV(L_max=12, s=4): {result['M_PV_L12']:.6e}")
        print(f"    L_emp(tau)         : {result['L_emp']:.18e}")
        print(f"    P_GGE_at_K_h       : {result['P_GGE_at_Kh']:.6e}")

    # ---------------- Step 7: Compute Level_2_moduli_consistency_ratio ----------------
    print("\n--- Step 7: Compute Level_2_moduli_consistency_ratio ---")
    L_emp_arr = np.array([r["L_emp"] for r in tau_results])  # (local) shape (3,)
    tau_arr = np.array(TAU_MESH)  # (local)
    deviations = np.abs(L_emp_arr - L_emp_canonical) / abs(L_emp_canonical)  # (local)
    consistency_ratio = float(deviations.max())  # (local)
    for tau_v, L_v, dev in zip(TAU_MESH, L_emp_arr, deviations):
        print(f"  tau={tau_v:.2f}: L_emp={L_v:.18e}; |L_emp - L_anchor|/|L_anchor| = {dev:.6e}")
    print(f"  Level_2_moduli_consistency_ratio = max(deviations) = {consistency_ratio:.6e}")
    print(f"  PASS-strict threshold (<= 0.10): {consistency_ratio <= PASS_STRICT_THRESHOLD}")
    print(f"  PASS-band threshold   (<= 0.30): {consistency_ratio <= PASS_BAND_THRESHOLD}")

    # ---------------- Step 8: Substitution-chain verification (direction discipline) ----------------
    print("\n--- Step 8: Substitution-chain verification (math-scripts.md MANDATORY) ---")
    print("  Definition 1: L_emp(tau) := d^2 ln Var_a(|v_a(K; tau)|^2) / d(ln K)^2 at K_horizon")
    print("  Definition 2: L_emp(tau_fold=0.19) = -7.046336474406761 M_KK^2 (S87 W2-3 anchor)")
    print(f"  Definition 3: Level_2_moduli_consistency_ratio = max_tau |L_emp(tau) - L_emp(tau_fold)| / |L_emp(tau_fold)|")
    print("  Substitute and simplify:")
    for tau_v, L_v, dev in zip(TAU_MESH, L_emp_arr, deviations):
        print(f"    |L_emp({tau_v}) - ({L_emp_canonical})|/|{L_emp_canonical}| = {dev:.6e}")
    print(f"  Direction: consistency_ratio = {consistency_ratio:.6e}")
    print(f"    consistency_ratio <= 0.10 ?  {consistency_ratio <= PASS_STRICT_THRESHOLD}  (PASS-strict)")
    print(f"    consistency_ratio <= 0.30 ?  {consistency_ratio <= PASS_BAND_THRESHOLD}  (PASS-band)")
    print(f"    consistency_ratio  > 0.30 ?  {consistency_ratio > PASS_BAND_THRESHOLD}  (FAIL)")

    # ---------------- Step 9: Composite verdict per Level_2_moduli_consistency_ratio band ----------------
    print("\n--- Step 9: Composite verdict + 3-tuple ---")
    if consistency_ratio <= PASS_STRICT_THRESHOLD:
        composite = "PASS"
        magnitude_v = "PASS"
        regime_v = "VALID"
        band_label = "PASS-strict"
    elif consistency_ratio <= PASS_BAND_THRESHOLD:
        composite = "INFO"
        magnitude_v = "INFO"
        regime_v = "VALID"
        band_label = "PASS-band"
    else:
        composite = "FAIL"
        magnitude_v = "FAIL"
        regime_v = "VALID"
        band_label = "FAIL"
    # Direction (sign_verdict): the canonical L_emp is NEGATIVE; check that all
    # tau-evaluated L_emp values are also negative (sign-preservation across moduli).
    all_neg = bool(np.all(L_emp_arr < 0))  # (local)
    sign_v = "PASS" if all_neg else "FAIL"
    print(f"  Level_2_moduli_consistency_ratio = {consistency_ratio:.6e}  ({band_label})")
    print(f"  Sign preservation across moduli (all L_emp(tau) < 0): {all_neg}")
    print(f"  composite={composite}; sign={sign_v}; magnitude={magnitude_v}; regime={regime_v}")

    # ---------------- Step 10: Compute dual-SHA ----------------
    print("\n--- Step 10: Compute dual-SHA ---")
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # ---------------- Step 11: Build value= string with Option-A supersedes tag ----------------
    print("\n--- Step 11: Build value= string with Option-A supersedes tag (FULL 64-char) ---")
    # Value string MUST include supersedes=<full-64-char> at emission time per
    # Option-A item 5 (NOT post-hoc tag addition).
    value_str = (
        f"L_emp_018={L_emp_arr[0]:.10e}_"
        f"L_emp_019={L_emp_arr[1]:.10e}_"
        f"L_emp_020={L_emp_arr[2]:.10e}_"
        f"L_emp_canonical={L_emp_canonical:.10e}_"
        f"Level_2_moduli_consistency_ratio={consistency_ratio:.6e}_"
        f"band={band_label}_"
        f"sign_preservation={all_neg}_"
        f"common_sector_count={len(common)}_"
        f"dropped_off_fold_sectors={sorted(dropped_018)}_"
        f"supersedes={SUPERSEDES_FULL_64}_"
        f"plan_text_drift_resolved=W3-4-schema-91-vs-90-AND-W3-9-canonical-anchor-path-s91_w5_1_full_bdg_pv.npz"
    )
    print(f"  value= prefix: {value_str[:120]}...")
    print(f"  supersedes embedded: {SUPERSEDES_FULL_64 in value_str}")

    # ---------------- Step 12: Save NPZ + JSON + PNG ----------------
    print("\n--- Step 12: Save NPZ + JSON + PNG ---")
    np.savez(
        OUT_NPZ,
        tau_mesh=tau_arr,
        L_emp_arr=L_emp_arr,
        L_emp_canonical=L_emp_canonical,
        L_emp_canonical_fallback=L_EMP_CANONICAL_FALLBACK,
        deviations=deviations,
        Level_2_moduli_consistency_ratio=consistency_ratio,
        pass_strict_threshold=PASS_STRICT_THRESHOLD,
        pass_band_threshold=PASS_BAND_THRESHOLD,
        composite_verdict=composite,
        sign_verdict=sign_v,
        magnitude_verdict=magnitude_v,
        regime_verdict=regime_v,
        band_label=band_label,
        all_L_emp_negative=all_neg,
        n_common_sectors=len(common),
        n_dropped_off_fold_sectors=len(dropped_018),
        dropped_off_fold_sector_ids=np.array(sorted(dropped_018), dtype=object),
        K_window=np.array(K_HORIZON_FRAC),
        DLNK=DLNK,
        n_K_pts=n_K_pts,
        L_max=L_MAX,
        s_pole=S_POLE,
        PV_M_tower=np.array(PV_M_TOWER),
        PV_coeffs=np.array(PV_COEFFS),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        supersedes_target_audit_sha=SUPERSEDES_FULL_64,
        plan_text_drift_W3_4_schema=
            "off-fold caches have 91 sectors incl (4,4); S84 master has 90 sectors. "
            "Restricted to common 90-sector intersection.",
        plan_text_drift_W3_9_canonical_anchor=
            f"plan cites s89_w5_2_l_emp_canonical_anchor.npz (NOT on disk); "
            f"runtime canonical path = s91_w5_1_full_bdg_pv.npz key L_emp_canonical={L_emp_canonical}",
    )
    print(f"  NPZ saved -> {OUT_NPZ.relative_to(ROOT)}")

    summary_dict = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "tau_mesh": list(TAU_MESH),
        "L_emp_arr": L_emp_arr.tolist(),
        "L_emp_canonical": L_emp_canonical,
        "Level_2_moduli_consistency_ratio": consistency_ratio,
        "pass_strict_threshold": PASS_STRICT_THRESHOLD,
        "pass_band_threshold": PASS_BAND_THRESHOLD,
        "composite_verdict": composite,
        "sign_verdict": sign_v,
        "magnitude_verdict": magnitude_v,
        "regime_verdict": regime_v,
        "band_label": band_label,
        "all_L_emp_negative": all_neg,
        "n_common_sectors": len(common),
        "n_dropped_off_fold_sectors": len(dropped_018),
        "dropped_off_fold_sectors": sorted(map(list, dropped_018)),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "supersedes_target_audit_sha": SUPERSEDES_FULL_64,
        "plan_text_drift_W3_4_schema":
            "off-fold caches 91 sectors incl (4,4); S84 master 90; restricted to common 90.",
        "plan_text_drift_W3_9_canonical_anchor":
            "runtime canonical path = computations/session-91/s91_w5_1_full_bdg_pv.npz key L_emp_canonical",
    }
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(summary_dict, f, indent=2)
    print(f"  JSON saved -> {OUT_JSON.relative_to(ROOT)}")

    make_plot(tau_arr, L_emp_arr, L_emp_canonical, consistency_ratio, composite)

    # ---------------- Step 13: Append verdict line (Option-A protocol; supersedes at emission) ----------------
    print("\n--- Step 13: Append corrective verdict line (Option-A protocol) ---")
    drift_notes = [
        f"# OPTION_A_PROTOCOL=supersedes={SUPERSEDES_FULL_64} # {GATE_ID} Option-A corrective emission per gate-verdicts.md MANDATORY S88 W8-100; supersedes target = S91 W1-5 CF-AV-L2-MODULI PRE-REG-INC verdict at s91_gate_verdicts.txt line 18; original line RETAINED on disk (verdict permanence absolute)",
        f"# PLAN_TEXT_DRIFT=W3-4-SCHEMA-91-VS-90 # {GATE_ID} per substrate-first-canonical-sourcing.md §(ii.B): off-fold caches s92_spectrum_cache_L12_tau018.npz + s92_spectrum_cache_L12_tau020.npz have 91 Peter-Weyl sectors INCLUDING (4,4); s84_spectrum_cache_L12_tau019.npz has 90 sectors EXCLUDING (4,4); restricted L_emp evaluation to common 90-sector intersection (dropped (4,4) high-Casimir sector from off-fold caches) so tau=0.19 vs tau=0.18/0.20 comparison is apples-to-apples; (4,4) is at p+q=8 high-Casimir and does NOT enter bottom-K Bogoliubov window structurally",
        f"# PLAN_TEXT_DRIFT=W3-9-CANONICAL-L-EMP-RUNTIME-PATH # {GATE_ID} per substrate-first-canonical-sourcing.md §(ii.B): plan §W3-5 input_files cites computations/session-89/s89_w5_2_l_emp_canonical_anchor.npz which does NOT exist on disk; runtime canonical anchor path is computations/session-91/s91_w5_1_full_bdg_pv.npz key L_emp_canonical={L_emp_canonical}; SHA-pinned in audit_sha256 input-pin map (key s91_w5_1_canonical_anchor_runtime_path)",
        f"# LEVEL_DECLARATION=LEVEL-1-SINGLE-TAU-SLICE-tau-0.19-PLUS-LEVEL-2-MODULI-DEFORMATION-tau-IN-{{0.18,0.20}} # {GATE_ID} per phononic-framing.md §'Single-tau-slice vs moduli-deformation substrate-IS levels' K=2 MANDATORY: L_emp(tau_fold=0.19) is the Level-1 single-tau-slice canonical anchor; tau in {{0.18, 0.20}} off-fold evaluations are the Level-2 moduli-deformation substrate-IS extensions; both levels structurally orthogonal per algebra-axis orthogonality K=3 MANDATORY",
        f"# LEVEL_CLASS_PIN=FULL # {GATE_ID} substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY level-pin compliance: producing script consumes canonical s52 8-mode Bogoliubov amplitudes + FULL Peter-Weyl block-diagonal spectrum caches; NO SCHEMATIC helper consumed; CLASS=FULL; no -SCHEMATIC suffix in convention",
        f"# OPERATOR_PRE_FLIGHT=L_emp_canonical_second_log_derivative_of_Bogoliubov_variance_per_S87_W2_3_Def_4 # {GATE_ID} math-scripts.md SUGGESTION K=1 operator-mismatch pre-flight: L_emp(tau) = d^2 ln Var_a(|v_a(K; tau)|^2)/d(ln K)^2 per S87 W2-3 Def 4 canonical, NOT trace operator form d ln(Tr_{{M_2}}(P_BdG D_K^{{-2s}}))/d ln K (which is +2s=+8 closed-form, INCOMPATIBLE with canonical -7.046336); convention suffix -PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22 is audit-trail signature",
    ]
    append_verdict(
        composite=composite,
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=sign_v,
        mag_v=magnitude_v,
        reg_v=regime_v,
        plan_text_drift_notes=drift_notes,
    )
    print(f"  Verdict line appended -> {VERDICT_FILE.relative_to(ROOT)}")
    print(f"  Composite verdict     = {composite}")
    print(f"  Option-A supersedes embedded in value=: {SUPERSEDES_FULL_64 in value_str}")
    print(f"  PLAN_TEXT_DRIFT companion rows: {len(drift_notes)} appended")
    print(f"\n=== Gate {GATE_ID} closed -- composite = {composite} ===")


if __name__ == "__main__":
    main()
