#!/usr/bin/env python3
"""
S93 W8-3 — NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT (LQG cluster, Wave 8)
==========================================================================

Gate: S93-W8-3-NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT  ([SIGN])  HIGHEST-EVOI
Classification: GEOMETRIC

Pivotal decision gate. The S92 LQG × phonon-first workshop reduced the §IX.7
narrow path — the only structurally-coherent route by which canonical LQG
kinematical observables (area operator, spin networks) could enter the framework
as DERIVED emergent shadows of the substrate (A_K, H_K, D_K) — to ONE empirical
question about one dimensionless bridge coefficient α_bridge:

  α_bridge ≈ 4.81e-3 (Regime I)  ⇒ narrow path closes, γ_emergent = γ_BH = 0.2375
  α_bridge ∼ O(1)    (Regime II) ⇒ narrow path FAILS structurally (γ_emergent ∼ 50,
                                    ~200× too large), NO recovery (γ does NOT admit
                                    cutoff running; Paper 03 §VII; LQG-theorist Q2)

This gate is the JOINT pre-flight: it tests whether the required α_bridge is
JOINTLY consistent with (PART A) the substrate-side Cauchy-Schwarz moment floor
F_0·F_2 ≥ F_1² AND (PART C) the LQG-side area-volume uncertainty band at canonical
j≤3 spin-networks (Bojowald 2001 / Paper 04). If EITHER is violated, Regime I is
structurally pre-forbidden BEFORE any Step-4 projection operator is built.

PIVOTAL re-keying of W8-7:
  PASS (Regime I survives)  → W8-7 workshop targets canonical LQG matching.
  FAIL (Regime I forbidden) → W8-7 targets the substrate's OWN narrow-path
                              effective theory (algebraic-form-resembles-LQG,
                              numerical-coefficient-disagrees ~200×).
  INFO (band edges ambiguous) → declare deferred-pending sub-class
                              (band-edge-convention-ambiguous).

Pre-registered 3-regime rubric (plan §W8-3 PASS/FAIL/INFO_meaning):
  PASS  iff (PART A sign ≥ 0)  ∧  (required α=4.81e-3 inside substrate-admissible
           α window set by s_CS + N_e)  ∧  (γ_BH=0.2375 ∈ [γ_lo, γ_hi] j≤3 band)
  FAIL  iff required α OUTSIDE the substrate-admissible window  OR  γ_BH OUTSIDE
           the j≤3 area-volume band (single-prescription).
  INFO  iff the j≤3 band edges are convention-ambiguous (SU(2)-state-counting
           prescription split neither cleanly contains nor cleanly excludes 0.2375).

[SIGN] trigger (schema-v2 3-tuple REQUIRED):
  - PART A: F_0·F_2 − F_1² ≥ 0 is the Cauchy-Schwarz floor (theorem A8 / S62 #18:
    F_0·F_{k+l} ≥ F_k F_l). Structurally ALWAYS ≥ 0 for ANY non-negative spectrum
    ⇒ sign_verdict tracks moment-floor satisfaction (PASS expected by theorem).
  - PART C: the LIVE discriminator — band-containment direction of γ_BH=0.2375 in
    the j≤3 area-volume band, JOINED with whether required α=4.81e-3 sits in the
    substrate-admissible α window (set by s_CS and the N_e=2.92 bulk-to-surface
    reduction).

Moment convention (PINNED; substitution-chain Step 1):
  SPECTRAL-SUM moments  F_p ≡ Σ_k m_k |λ_k|^p,  m_k = dim(p,q) PW weight of the
  sector containing mode k. F_0 = total PW-weighted mode count = 31,956,720
  (= Σ_sectors dim(p,q)·len(abs_evals) = Σ 16·dim(p,q)² on the L_max=12 cache).
  DISTINCT from the cutoff-function moments f_n (f_2_default=2.34, f_4_default=0.558
  in canonical_constants — NOT used here).

Substrate framing (phononic-framing.md §"IS Space, Not IN Space"):
  The spectral moments F_0,F_1,F_2 are the substrate's intrinsic dispersion data;
  the Cauchy-Schwarz slack s_CS = F_0·F_2/F_1²−1 caps the substrate-admissible
  α_bridge. The substrate √(C_2(p,q)) area spectrum is PRIMARY; the LQG √(j(j+1))
  is the candidate EMERGENT shadow whose area-volume self-consistency is the second
  leg. Explanation flows substrate → HKR/Cheeger-Simons → laboratory-IN LQG
  kinematical observable. GEOMETRIC: a spectral-moment computation on the fabric's
  eigenvalue spectrum, deciding whether the emergent-LQG matching corridor is open
  or closed BEFORE any projection operator is constructed.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (sector_evals dict)
  - computations/session-93/s93_w8_1_narrow_path_eigenvalue_inventory.npz (W8-1 ground truth)
  - computations/_shared/canonical_constants.py (feeds audit_sha256; LQG pins + N_e)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<composite verdict string>,
   scheme=narrow-path-cauchy-schwarz-joint-preflight-F0F2-F1sq-floor-AND-area-volume-band-j-le-3,
   convention=NARROW-PATH-joint-preflight-spectral-SUM-moments-F0F1F2-PW-weighted-required-alpha-bridge-4p81e-3-reduced-planck-disclosed-area-volume-Bojowald-2001-j-le-3,
   L_max=12)

DEVIATION DISCLOSURE (plan §"DEVIATION HINT"; substrate-first-canonical-sourcing.md §(ii.B)):
  canonical_constants.py runtime SHA differs from the plan-pinned value
  1aa90bb1...790c (benign plan-text drift). This script consumes
  ALPHA_BRIDGE_REQUIRED_FW, SCALE_BRIDGE_PREFACTOR_FW, GAMMA_BH_SU2_CONVENTION_LQG,
  M_KK_gravity, M_Pl_reduced via canonical import (MCP get_constant confirmed
  values 4.81e-3 / 49.34 / 0.2375 / 7.4287e16 / 2.435e18), NOT via plan-pinned SHA.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (path setup precedes canonical import)
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths (must precede canonical_constants import)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402  explicit names this gate consumes
    ALPHA_BRIDGE_REQUIRED_FW,
    SCALE_BRIDGE_PREFACTOR_FW,
    GAMMA_BH_SU2_CONVENTION_LQG,
    M_KK_gravity,
    M_Pl_reduced,
    tau_fold,
)

# ---------------------------------------------------------------------------
# GPU eligibility (plan machinery pin): the 31.96M-mode F_n reductions ship to
# cuda (torch) at 0.26 GB << 17 GB VRAM. numpy cpu-cap-OMP8 fallback if needed.
# The reductions are simple sums (no eigendecomposition); torch GPU is preferred.
# ---------------------------------------------------------------------------
USE_GPU = False                                                       # (local) resolved below
try:
    import torch  # noqa: E402
    if torch.cuda.is_available():
        USE_GPU = True
except Exception:  # noqa: BLE001
    USE_GPU = False

SESSION = "S93"                                                       # (local)
GATE_ID = "S93-W8-3-NARROW-PATH-CAUCHY-SCHWARZ-JOINT-PREFLIGHT"       # (local)
SCHEME = (
    "narrow-path-cauchy-schwarz-joint-preflight-"
    "F0F2-F1sq-floor-AND-area-volume-band-j-le-3"
)                                                                     # (local)
CONVENTION = (
    "NARROW-PATH-joint-preflight-spectral-SUM-moments-F0F1F2-PW-weighted-"
    "required-alpha-bridge-4p81e-3-reduced-planck-disclosed-"
    "area-volume-Bojowald-2001-j-le-3"
)                                                                     # (local)
L_MAX = 12                                                            # (local) cache native ceiling
L_MAX_HISTORICAL = 10                                                 # (local) narrow-path comparison scope

# Substrate-side bulk-to-surface reduction magnitude — the only landed instance.
# S53 N_e^acoustic = 2.9202 post-fold acoustic e-folds; the substrate-side prior
# evidence that bulk-to-surface reductions produce O(1) outputs, NOT 1e-3.
N_E_BULK_TO_SURFACE = 2.9202                                          # (local) S53 N_e^acoustic

# Pre-registered tolerances / thresholds (plan §W8-3 strict_PASS_boundary)
REQUIRED_ALPHA_RELTOL = 1e-3                                          # (local) PART B cross-check
# Canonical spin-network ladder j ∈ {1/2, 1, 3/2, 2, 5/2, 3} (canonical j≤3)
J_LADDER = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]                             # (local) Bojowald 2001 j≤3

# Reduced-vs-unreduced Planck convention (disclosure; ℓ_P² = 8π·ℓ_P_red²)
PLANCK_REDUCTION_8PI = 8.0 * np.pi                                    # (local) ℓ_P²/ℓ_P_red²

# Output destinations (per-session, canonical path)
OUT_NPZ = SESSION_DIR / "s93_w8_3_narrow_path_cauchy_schwarz_joint_preflight.npz"
OUT_PNG = SESSION_DIR / "s93_w8_3_narrow_path_cauchy_schwarz_joint_preflight.png"
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W8_1_INVENTORY = SESSION_DIR / "s93_w8_1_narrow_path_eigenvalue_inventory.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    W8_1_INVENTORY,
    CACHE_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema; W9a-99)
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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
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
# Section 5 — Compute
# ---------------------------------------------------------------------------

def load_sector_evals(path: Path) -> dict:
    c = np.load(path, allow_pickle=True)  # (local)
    return c["sector_evals"].item()


def spectral_moments(se: dict, level_max: int) -> tuple[float, float, float, int]:
    """SPECTRAL-SUM moments F_p = Σ_k m_k |λ_k|^p, m_k = dim(p,q) PW weight.

    Returns (F_0, F_1, F_2, n_modes_weighted). The PW-weighted full-multiplicity
    spectrum repeats each sector's abs_evals by dim(p,q). On GPU we build the
    weighted |λ| array and reduce with torch; numpy fallback otherwise.
    """
    # Collect per-sector (weight, abs_evals) up to level_max.
    abs_chunks: list[np.ndarray] = []  # (local)
    weights: list[float] = []          # (local)
    for (p, q), rec in se.items():
        if int(rec["level"]) > level_max:
            continue
        dimpq = float(rec["dim"])                      # (local) PW weight m_k
        ae = np.asarray(rec["abs_evals"], dtype=np.float64)  # (local)
        abs_chunks.append(ae)
        weights.append(dimpq)

    if USE_GPU:
        # Stream per-sector reductions to GPU (avoids materializing the full
        # 31.96M weighted array; each sector's |λ| array goes to cuda, the three
        # weighted power-sums accumulate on host as Python floats).
        F0 = F1 = F2 = 0.0  # (local)
        for ae, w in zip(abs_chunks, weights):
            t = torch.as_tensor(ae, device="cuda", dtype=torch.float64)  # (local)
            n = t.numel()                                                # (local)
            s1 = torch.sum(t).item()                                     # (local)
            s2 = torch.sum(t * t).item()                                 # (local)
            F0 += w * n
            F1 += w * s1
            F2 += w * s2
        n_modes = int(round(F0))  # (local)
        return F0, F1, F2, n_modes

    # numpy fallback (cpu) — same accumulation
    F0 = F1 = F2 = 0.0  # (local)
    for ae, w in zip(abs_chunks, weights):
        F0 += w * ae.size
        F1 += w * float(ae.sum())
        F2 += w * float((ae * ae).sum())
    n_modes = int(round(F0))  # (local)
    return F0, F1, F2, n_modes


def cauchy_schwarz_slack(F0: float, F1: float, F2: float) -> tuple[float, float]:
    """Return (det = F_0·F_2 − F_1², s_CS = F_0·F_2/F_1² − 1)."""
    det = F0 * F2 - F1 * F1            # (local) Cauchy-Schwarz floor margin
    s_cs = (F0 * F2) / (F1 * F1) - 1.0  # (local) dimensionless slack
    return det, s_cs


def area_volume_band(j_ladder: list[float]) -> dict:
    """LQG area-volume admissible-Immirzi band at canonical j≤3.

    Physics (substrate → emergent shadow direction):
      Area   A_j = 8πγℓ_P² √(j(j+1))                       [Paper 02 Eq.7 / Paper 05 Eq.5.4]
      Volume V_j = (γℓ_P²)^{3/2} √(j(j+1/2)(j+1)/27)        [Bojowald 2001 / Paper 04 Eq.2]
      Area-volume dimensionless ratio R_AV = V_j^{2/3}/(A_j ℓ_P^{-2}) — γ CANCELS
      exactly (net γ power 0; Sage-verified). So R_AV does NOT pin γ; the admissible
      γ band comes from the BH-entropy state-counting normalization across the
      canonical SU(2)-vs-U(1) prescriptions evaluated on the j≤3 ladder.

    Band determination — state-counting prescriptions (entropy normalization
    Σ_j w(j) exp(−2πγ√(j(j+1))) = 1) at the j≤3 truncation:
      - U(1) ABCK analytic:     γ_0 = ln2/(π√3) ≈ 0.12738
      - GM (no degeneracy):     Σ_j exp(−2πγ√(j(j+1))) = 1
      - DL (full SU(2), 2j+1):  Σ_j (2j+1) exp(−2πγ√(j(j+1))) = 1

    The DL prescription is the CANONICAL SU(2) state-counting (Domagala-Lewandowski
    / Meissner); it brackets the single-prescription band. The GM/DL/U(1) spread is
    the full prescription-uncertainty band ("Immirzi γ pinning is single-input" open
    channel: different state-counting prescriptions yield different γ).
    """
    js = np.asarray(j_ladder, dtype=np.float64)              # (local)
    sqrt_casimir = np.sqrt(js * (js + 1.0))                   # (local) √(j(j+1))

    # U(1) ABCK analytic value
    gamma_U1 = float(np.log(2.0) / (np.pi * np.sqrt(3.0)))    # (local)

    # Volume eigenvalues V_j ∝ √(j(j+1/2)(j+1)/27) — Bojowald Eq.2 (γ-stripped factor)
    vol_factor = np.sqrt(js * (js + 0.5) * (js + 1.0) / 27.0)  # (local) V_j/(γℓ_P²)^{3/2}

    # Solve entropy-normalization for γ at j≤3 truncation (bisection; monotone in γ)
    def entropy_sum(g: float, w_deg: np.ndarray) -> float:
        return float(np.sum(w_deg * np.exp(-2.0 * np.pi * g * sqrt_casimir)))

    def solve_gamma(w_deg: np.ndarray, lo: float = 0.02, hi: float = 1.2) -> float:
        # find γ with entropy_sum == 1 (decreasing in γ)
        for _ in range(200):
            mid = 0.5 * (lo + hi)  # (local)
            val = entropy_sum(mid, w_deg)  # (local)
            if val > 1.0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    deg_GM = np.ones_like(js)            # (local) no-degeneracy
    deg_DL = (2.0 * js + 1.0)            # (local) full SU(2) (2j+1)
    gamma_GM = solve_gamma(deg_GM)       # (local)
    gamma_DL = solve_gamma(deg_DL)       # (local)

    # Single-prescription (DL canonical SU(2)) band: a tight band around the DL
    # solution from the j≤3 vs full-ladder truncation spread.
    js_full = np.array([0.5 * k for k in range(1, 61)], dtype=np.float64)  # (local)
    sc_full = np.sqrt(js_full * (js_full + 1.0))                            # (local)

    def entropy_full(g: float, w_deg: np.ndarray) -> float:
        return float(np.sum(w_deg * np.exp(-2.0 * np.pi * g * sc_full)))

    def solve_full(w_deg: np.ndarray, lo: float = 0.02, hi: float = 1.2) -> float:
        for _ in range(200):
            mid = 0.5 * (lo + hi)  # (local)
            if entropy_full(mid, w_deg) > 1.0:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)

    gamma_DL_full = solve_full(2.0 * js_full + 1.0)  # (local)
    gamma_GM_full = solve_full(np.ones_like(js_full))  # (local)

    # Single-prescription DL band (the canonical SU(2) state-counting):
    dl_lo = min(gamma_DL, gamma_DL_full)  # (local)
    dl_hi = max(gamma_DL, gamma_DL_full)  # (local)

    # Full prescription-spread band (U(1) ABCK … DL): exposes the convention
    # ambiguity that the single-input Immirzi pinning carries.
    spread_vals = [gamma_U1, gamma_GM, gamma_GM_full, gamma_DL, gamma_DL_full]  # (local)
    spread_lo = float(min(spread_vals))  # (local)
    spread_hi = float(max(spread_vals))  # (local)

    return {
        "sqrt_casimir": sqrt_casimir,
        "vol_factor": vol_factor,
        "gamma_U1": gamma_U1,
        "gamma_GM_le3": gamma_GM,
        "gamma_DL_le3": gamma_DL,
        "gamma_GM_full": gamma_GM_full,
        "gamma_DL_full": gamma_DL_full,
        "dl_band_lo": dl_lo,
        "dl_band_hi": dl_hi,
        "spread_band_lo": spread_lo,
        "spread_band_hi": spread_hi,
    }


def compute() -> dict:
    se = load_sector_evals(CACHE_PATH)  # (local)

    # --- W8-1 inventory consistency cross-check (consume as ground truth) ---
    inv = np.load(W8_1_INVENTORY, allow_pickle=True)  # (local)
    inv_F0_check = int(np.int64(inv["a0_dim2_L12"]))  # (local) = 16·Σdim² = 31,956,720
    inv_F0_check_L10 = int(np.int64(inv["a0_dim2_L10"]))  # (local)

    # --- PART A: substrate spectral-SUM moments + Cauchy-Schwarz floor ---
    F0_12, F1_12, F2_12, nmodes_12 = spectral_moments(se, L_MAX)        # (local)
    F0_10, F1_10, F2_10, nmodes_10 = spectral_moments(se, L_MAX_HISTORICAL)  # (local)
    det_12, s_cs_12 = cauchy_schwarz_slack(F0_12, F1_12, F2_12)         # (local)
    det_10, s_cs_10 = cauchy_schwarz_slack(F0_10, F1_10, F2_10)         # (local)

    # PART A sign: F_0·F_2 − F_1² ≥ 0 (Cauchy-Schwarz, theorem A8 — always ≥ 0)
    partA_sign_ok = (det_12 >= 0.0)  # (local)

    # --- PART B: required-α inversion (recompute + cross-check canonical) ---
    # prefactor = (M_Pl_red/M_KK)²/(4√3π); γ_emergent = α_bridge · prefactor
    ratio = M_Pl_reduced / M_KK_gravity                                 # (local)
    prefactor_recomp = (ratio * ratio) / (4.0 * np.sqrt(3.0) * np.pi)   # (local)
    alpha_required_recomp = GAMMA_BH_SU2_CONVENTION_LQG / SCALE_BRIDGE_PREFACTOR_FW  # (local)
    alpha_required_canonical = float(ALPHA_BRIDGE_REQUIRED_FW)          # (local) 4.81e-3
    alpha_reldev = abs(alpha_required_recomp - alpha_required_canonical) / alpha_required_canonical  # (local)
    partB_ok = (alpha_reldev <= REQUIRED_ALPHA_RELTOL)                  # (local)

    # --- substrate-admissible α window (the LIVE substrate-side constraint) ---
    # The substrate's bulk-to-surface (3D→2D) reduction compresses an O(1) bulk
    # coefficient by a factor set by the moment-ratio spread s_CS over the N_e
    # acoustic e-folds. The substrate-natural α scale is O(1) (the N_e=2.92 landed
    # evidence: bulk-to-surface reductions produce O(1) outputs, NOT 1e-3-suppressed).
    #   - upper edge: α ~ O(1) (unreduced substrate dispersion coefficient)
    #   - lower edge: the maximal compression a single e-fold-modulated reduction can
    #     achieve from the tight spectrum: α_min ~ s_CS / N_e  (slack divided by the
    #     bulk-to-surface e-fold count — the most a tight spectrum can shrink it).
    alpha_admissible_hi = 1.0                                           # (local) O(1) substrate-natural
    alpha_admissible_lo = s_cs_12 / N_E_BULK_TO_SURFACE                 # (local) maximal compression
    required_in_window = (alpha_admissible_lo <= alpha_required_canonical <= alpha_admissible_hi)  # (local)
    # decades the required α sits BELOW the substrate-admissible lower edge:
    alpha_oom_below = np.log10(alpha_admissible_lo / alpha_required_canonical)  # (local)

    # --- PART C: LQG area-volume band at canonical j≤3 ---
    av = area_volume_band(J_LADDER)                                     # (local)
    gamma_bh = float(GAMMA_BH_SU2_CONVENTION_LQG)                       # (local) 0.2375
    in_dl_band = (av["dl_band_lo"] <= gamma_bh <= av["dl_band_hi"])     # (local) single-prescription
    in_spread_band = (av["spread_band_lo"] <= gamma_bh <= av["spread_band_hi"])  # (local) full spread
    # band-edge ambiguity: single-prescription EXCLUDES but full-spread CONTAINS
    band_edge_ambiguous = (in_spread_band and not in_dl_band)           # (local)

    return {
        # PART A
        "F0_12": F0_12, "F1_12": F1_12, "F2_12": F2_12, "nmodes_12": nmodes_12,
        "F0_10": F0_10, "F1_10": F1_10, "F2_10": F2_10, "nmodes_10": nmodes_10,
        "det_12": det_12, "s_cs_12": s_cs_12,
        "det_10": det_10, "s_cs_10": s_cs_10,
        "partA_sign_ok": partA_sign_ok,
        "inv_F0_check": inv_F0_check, "inv_F0_check_L10": inv_F0_check_L10,
        # PART B
        "prefactor_recomp": prefactor_recomp,
        "alpha_required_recomp": alpha_required_recomp,
        "alpha_required_canonical": alpha_required_canonical,
        "alpha_reldev": alpha_reldev, "partB_ok": partB_ok,
        # substrate-admissible window
        "alpha_admissible_lo": alpha_admissible_lo,
        "alpha_admissible_hi": alpha_admissible_hi,
        "required_in_window": required_in_window,
        "alpha_oom_below": float(alpha_oom_below),
        "N_e": N_E_BULK_TO_SURFACE,
        # PART C
        "av": av, "gamma_bh": gamma_bh,
        "in_dl_band": in_dl_band, "in_spread_band": in_spread_band,
        "band_edge_ambiguous": band_edge_ambiguous,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict (3-regime rubric) + schema-v2 3-tuple
# ---------------------------------------------------------------------------

def evaluate_3tuple(r: dict) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    sign_verdict   : PART A Cauchy-Schwarz floor sign (predicted ≥0 by theorem A8).
    magnitude_verdict: substrate-admissible-α window containment of required α=4.81e-3
                       (the substrate-side magnitude discriminator).
    regime_verdict : PART C band-edge convention status (VALID = clean band;
                       MARGINAL = single-prescription excludes but spread contains
                       ⇒ convention-ambiguous; BREAKDOWN reserved/unused here).
    Composite collapse per gate-verdicts.md §"Composite-collapse rule".
    """
    # sign_verdict: predicted direction F_0·F_2−F_1² ≥ 0 matches computed sign
    sign_verdict = "PASS" if r["partA_sign_ok"] else "FAIL"  # (local)

    # magnitude_verdict: required α=4.81e-3 inside substrate-admissible window?
    #   PASS  if inside; FAIL if outside (the substrate-side magnitude test)
    magnitude_verdict = "PASS" if r["required_in_window"] else "FAIL"  # (local)

    # regime_verdict: PART C band-edge convention status
    if r["band_edge_ambiguous"]:
        regime_verdict = "MARGINAL"  # (local) convention-ambiguous band edge
    elif r["in_dl_band"]:
        regime_verdict = "VALID"     # (local) clean single-prescription containment
    else:
        # neither in single-prescription DL band NOR in full spread band ⇒ clean exclusion
        regime_verdict = "VALID"     # (local) clean exclusion (band determinate)

    # Composite collapse (pre-registered; gate-verdicts.md):
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # SIGN-correct, MAGNITUDE-wrong-but-band-ambiguous
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_verdict, magnitude_verdict, regime_verdict


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str, value, audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
) -> None:
    """Atomic append: canonical line + dual-SHA companion row (W9a-99) +
    schema-v2 3-tuple companion row (S87; REQUIRED for [SIGN] trigger).
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple_row)


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict, composite: str) -> None:
    av = r["av"]  # (local)
    fig, axes = plt.subplots(1, 3, figsize=(17, 5.4))  # (local)

    # Panel A: Cauchy-Schwarz floor — F_0·F_2 vs F_1² (the floor margin)
    ax = axes[0]  # (local)
    labels = ["L≤10", "L≤12"]  # (local)
    f0f2 = [r["F0_10"] * r["F2_10"], r["F0_12"] * r["F2_12"]]  # (local)
    f1sq = [r["F1_10"] ** 2, r["F1_12"] ** 2]                  # (local)
    x = np.arange(2)  # (local)
    ax.bar(x - 0.18, f0f2, 0.34, label=r"$F_0\!\cdot\!F_2$", color="C0")
    ax.bar(x + 0.18, f1sq, 0.34, label=r"$F_1^2$", color="C3")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("moment product")
    ax.set_yscale("log")
    ax.set_title(
        f"PART A: Cauchy-Schwarz floor  $F_0 F_2 \\geq F_1^2$\n"
        f"$F_0F_2-F_1^2={r['det_12']:.3e} \\geq 0$ (sign PASS); "
        f"$s_{{CS}}={r['s_cs_12']:.4f}$"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")

    # Panel B: substrate-admissible α window vs required α=4.81e-3
    ax = axes[1]  # (local)
    ax.axhspan(r["alpha_admissible_lo"], r["alpha_admissible_hi"],
               color="C2", alpha=0.25,
               label=f"substrate-admissible α\n[{r['alpha_admissible_lo']:.3e}, "
                     f"{r['alpha_admissible_hi']:.2f}]")
    ax.axhline(r["alpha_required_canonical"], color="C3", lw=2.0,
               label=f"required α = {r['alpha_required_canonical']:.3e}\n"
                     f"(Regime I closure)")
    ax.axhline(r["alpha_admissible_lo"], color="C2", ls="--", lw=1.0)
    ax.set_yscale("log")
    ax.set_ylim(1e-4, 3.0)
    ax.set_xticks([])
    ax.set_ylabel(r"$\alpha_{bridge}$")
    ax.set_title(
        f"PART B+window: required α vs substrate-admissible\n"
        f"required sits {r['alpha_oom_below']:.2f} OOM BELOW window floor "
        f"(N_e={r['N_e']:.2f})"
    )
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.3, axis="y")

    # Panel C: area-volume admissible-Immirzi band at j≤3 + γ_BH=0.2375
    ax = axes[2]  # (local)
    ax.axhspan(av["spread_band_lo"], av["spread_band_hi"], color="C1", alpha=0.18,
               label=f"full prescription-spread\n[{av['spread_band_lo']:.4f}, "
                     f"{av['spread_band_hi']:.4f}]")
    ax.axhspan(av["dl_band_lo"], av["dl_band_hi"], color="C0", alpha=0.35,
               label=f"DL canonical SU(2) j≤3\n[{av['dl_band_lo']:.4f}, "
                     f"{av['dl_band_hi']:.4f}]")
    ax.axhline(r["gamma_bh"], color="C3", lw=2.2,
               label=f"γ_BH = {r['gamma_bh']:.4f} (SU(2))")
    ax.axhline(av["gamma_U1"], color="k", ls=":", lw=1.0,
               label=f"γ_0 U(1) = {av['gamma_U1']:.4f}")
    ax.set_ylim(0.10, 0.32)
    ax.set_xticks([])
    ax.set_ylabel("Immirzi γ")
    ax.set_title(
        f"PART C: area-volume band j≤3 (Bojowald 2001)\n"
        f"γ_BH in DL band? {r['in_dl_band']} | in spread? {r['in_spread_band']} "
        f"⇒ ambiguous={r['band_edge_ambiguous']}"
    )
    ax.legend(fontsize=7.5, loc="upper right")
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        f"S93-W8-3 NARROW-PATH joint pre-flight (τ_fold={tau_fold}) — {composite} | "
        f"Regime I {'SURVIVES' if composite == 'PASS' else ('PRE-FORBIDDEN' if composite == 'FAIL' else 'INCONCLUSIVE')}",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  GPU path: {'cuda (torch)' if USE_GPU else 'numpy cpu fallback'}")
    print()

    r = compute()  # (local)
    composite, sign_v, mag_v, reg_v = evaluate_3tuple(r)  # (local)
    av = r["av"]  # (local)

    # ===================== NUMBERS FIRST =====================
    print("=== PART A: substrate spectral-SUM moments (PW-weighted) ===")
    print(f"  convention: F_p = Σ_k m_k|λ_k|^p, m_k=dim(p,q) PW weight "
          f"(NOT cutoff moments f_n)")
    print(f"  L_max=12: F_0={r['F0_12']:.10e}  F_1={r['F1_12']:.10e}  "
          f"F_2={r['F2_12']:.10e}  ({r['nmodes_12']:,} weighted modes)")
    print(f"  L_max=10: F_0={r['F0_10']:.10e}  F_1={r['F1_10']:.10e}  "
          f"F_2={r['F2_10']:.10e}  ({r['nmodes_10']:,} weighted modes)")
    print(f"  W8-1 inventory cross-check: a0_dim2_L12={r['inv_F0_check']:,} "
          f"(== F_0? {r['inv_F0_check'] == r['nmodes_12']})")
    print(f"  F_0·F_2 − F_1² (L12) = {r['det_12']:.10e}  "
          f"(sign {'+' if r['det_12'] >= 0 else '-'}; floor {'PASS' if r['partA_sign_ok'] else 'FAIL'})")
    print(f"  s_CS = F_0·F_2/F_1² − 1 (L12) = {r['s_cs_12']:.10e}")
    print(f"  s_CS (L10) = {r['s_cs_10']:.10e}")
    print()
    print("=== PART B: required-α inversion (γ_BH / SCALE_BRIDGE_PREFACTOR_FW) ===")
    print(f"  M_Pl_red/M_KK = {M_Pl_reduced / M_KK_gravity:.6f}")
    print(f"  prefactor recompute (M_Pl/M_KK)²/(4√3π) = {r['prefactor_recomp']:.6f} "
          f"(canonical 49.34)")
    print(f"  α_required recompute = γ_BH/prefactor_canon = {r['alpha_required_recomp']:.6e}")
    print(f"  α_required canonical (ALPHA_BRIDGE_REQUIRED_FW) = {r['alpha_required_canonical']:.6e}")
    print(f"  rel-dev = {r['alpha_reldev']:.3e} (reltol {REQUIRED_ALPHA_RELTOL:.0e}; "
          f"PASS={r['partB_ok']})")
    print(f"  reduced-Planck disclosure: ℓ_P² = 8π·ℓ_P_red² (8π = {PLANCK_REDUCTION_8PI:.6f})")
    print()
    print("=== substrate-admissible α window (LIVE substrate discriminator) ===")
    print(f"  N_e (S53 acoustic, bulk-to-surface) = {r['N_e']:.4f}")
    print(f"  window [α_lo, α_hi] = [{r['alpha_admissible_lo']:.6e}, "
          f"{r['alpha_admissible_hi']:.4f}]  (α_lo = s_CS/N_e; α_hi = O(1))")
    print(f"  required α = {r['alpha_required_canonical']:.6e} inside window? "
          f"{r['required_in_window']}")
    print(f"  required α sits {r['alpha_oom_below']:.3f} OOM BELOW the window floor")
    print()
    print("=== PART C: LQG area-volume admissible-Immirzi band at j≤3 ===")
    print(f"  j ladder: {J_LADDER}")
    print(f"  √(j(j+1)): {np.round(av['sqrt_casimir'], 5).tolist()}")
    print(f"  γ_U1 (ABCK analytic ln2/π√3)   = {av['gamma_U1']:.6f}")
    print(f"  γ_GM  (no-deg)  j≤3 / full     = {av['gamma_GM_le3']:.6f} / {av['gamma_GM_full']:.6f}")
    print(f"  γ_DL  (SU(2) 2j+1) j≤3 / full  = {av['gamma_DL_le3']:.6f} / {av['gamma_DL_full']:.6f}")
    print(f"  DL canonical SU(2) band [γ_lo,γ_hi] = [{av['dl_band_lo']:.6f}, {av['dl_band_hi']:.6f}]")
    print(f"  full prescription-spread band       = [{av['spread_band_lo']:.6f}, {av['spread_band_hi']:.6f}]")
    print(f"  γ_BH = {r['gamma_bh']:.4f}: in DL band? {r['in_dl_band']} | "
          f"in spread band? {r['in_spread_band']}")
    print(f"  band-edge convention-ambiguous? {r['band_edge_ambiguous']}")
    print()
    print("=== JOINT 3-tuple ===")
    print(f"  sign_verdict      = {sign_v}  (PART A Cauchy-Schwarz floor; theorem A8 ⇒ ≥0)")
    print(f"  magnitude_verdict = {mag_v}  (required α inside substrate-admissible window?)")
    print(f"  regime_verdict    = {reg_v}  (PART C band-edge convention status)")
    print(f"  COMPOSITE         = {composite}")
    print()

    # Composite value string (descriptive)
    regime_label = (
        "REGIME-I-SURVIVES" if composite == "PASS"
        else ("REGIME-I-PRE-FORBIDDEN" if composite == "FAIL"
              else "band-edge-convention-ambiguous-DEFERRED-PENDING")
    )  # (local)
    value = (
        f"{regime_label}_sCS={r['s_cs_12']:.4f}_alphaReq={r['alpha_required_canonical']:.3e}_"
        f"alphaWinLo={r['alpha_admissible_lo']:.3e}_oomBelow={r['alpha_oom_below']:.2f}_"
        f"gammaBH={r['gamma_bh']:.4f}_DLband=[{av['dl_band_lo']:.4f},{av['dl_band_hi']:.4f}]_"
        f"inDL={r['in_dl_band']}_inSpread={r['in_spread_band']}"
    )  # (local)

    # --- Persist npz (full float64) ---
    np.savez(
        OUT_NPZ,
        # PART A
        F0_12=np.float64(r["F0_12"]), F1_12=np.float64(r["F1_12"]),
        F2_12=np.float64(r["F2_12"]), nmodes_12=np.int64(r["nmodes_12"]),
        F0_10=np.float64(r["F0_10"]), F1_10=np.float64(r["F1_10"]),
        F2_10=np.float64(r["F2_10"]), nmodes_10=np.int64(r["nmodes_10"]),
        det_12=np.float64(r["det_12"]), s_cs_12=np.float64(r["s_cs_12"]),
        det_10=np.float64(r["det_10"]), s_cs_10=np.float64(r["s_cs_10"]),
        partA_sign_ok=np.bool_(r["partA_sign_ok"]),
        inv_F0_check=np.int64(r["inv_F0_check"]),
        inv_F0_check_L10=np.int64(r["inv_F0_check_L10"]),
        # PART B
        prefactor_recomp=np.float64(r["prefactor_recomp"]),
        alpha_required_recomp=np.float64(r["alpha_required_recomp"]),
        alpha_required_canonical=np.float64(r["alpha_required_canonical"]),
        alpha_reldev=np.float64(r["alpha_reldev"]),
        partB_ok=np.bool_(r["partB_ok"]),
        planck_reduction_8pi=np.float64(PLANCK_REDUCTION_8PI),
        # substrate-admissible window
        alpha_admissible_lo=np.float64(r["alpha_admissible_lo"]),
        alpha_admissible_hi=np.float64(r["alpha_admissible_hi"]),
        required_in_window=np.bool_(r["required_in_window"]),
        alpha_oom_below=np.float64(r["alpha_oom_below"]),
        N_e=np.float64(r["N_e"]),
        # PART C
        j_ladder=np.asarray(J_LADDER, dtype=np.float64),
        sqrt_casimir=np.asarray(av["sqrt_casimir"], dtype=np.float64),
        vol_factor=np.asarray(av["vol_factor"], dtype=np.float64),
        gamma_U1=np.float64(av["gamma_U1"]),
        gamma_GM_le3=np.float64(av["gamma_GM_le3"]),
        gamma_DL_le3=np.float64(av["gamma_DL_le3"]),
        gamma_GM_full=np.float64(av["gamma_GM_full"]),
        gamma_DL_full=np.float64(av["gamma_DL_full"]),
        dl_band_lo=np.float64(av["dl_band_lo"]),
        dl_band_hi=np.float64(av["dl_band_hi"]),
        spread_band_lo=np.float64(av["spread_band_lo"]),
        spread_band_hi=np.float64(av["spread_band_hi"]),
        gamma_bh=np.float64(r["gamma_bh"]),
        in_dl_band=np.bool_(r["in_dl_band"]),
        in_spread_band=np.bool_(r["in_spread_band"]),
        band_edge_ambiguous=np.bool_(r["band_edge_ambiguous"]),
        # verdict
        sign_verdict=np.str_(sign_v),
        magnitude_verdict=np.str_(mag_v),
        regime_verdict=np.str_(reg_v),
        composite=np.str_(composite),
        tau_fold=np.float64(tau_fold),
    )
    make_plot(r, composite)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(composite, value, audit_sha, content_sha, sign_v, mag_v, reg_v)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v} mag={mag_v} regime={reg_v}; wall {wall:.1f}s) ===")
    # Verdict is DATA, not exit code (math-scripts.md §Exit Codes): exit 0 on a
    # valid scientific verdict regardless of PASS/FAIL/INFO.
    return 0


if __name__ == "__main__":
    sys.exit(main())
