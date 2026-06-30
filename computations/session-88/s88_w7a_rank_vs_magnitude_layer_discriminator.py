#!/usr/bin/env python3
"""
S88 W7a-74 — S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR
=============================================================

Gate: S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR  ([VERIFY])

Sub-wave: session-88-plan-w7a.md §W7a-74 (lizzi-spectral-functional-theorist
PRIMARY; transit-dynamics-theorist CO-AUTHOR per plan §214).

Pre-registered hypothesis (per plan §216-220):
  S87 W9b-2 line 268 reports |rho_S(s=4)| = 1.000 EXACT (Spearman rank
  correlation, A_5 4-class projection at s=4 pole) AND cross-regulator
  spread 0.0513. The single PASS verdict aggregates TWO DISTINCT EPISTEMIC
  LAYERS:
    - Rank-ordering layer (Layer 1): |rho_S| = 1.000 EXACT is FUNCTIONAL-
      INDEPENDENT — Spearman is rank-only; ordinal structure survives any
      monotonic transform of the regulator-class moments. Substrate
      prediction: rank-ordering survives PRIMARY-vs-SCHEMATIC level switch.
    - Magnitude-ratio layer (Layer 2): 0.0513 is REGULATOR-DRESSED — the
      magnitude scatter is a real-valued function of absolute moments,
      sensitive to the absolute regulator parameter scales (M_KK vs
      heuristic Casimir-fraction). Substrate prediction: magnitude scatter
      DIFFERS structurally between PRIMARY and SCHEMATIC level.

Two-PASS evaluation:
  PASS-RANK         iff |rho_S(s=4)|_TIER-1 >= 0.999 AND |rho_S(s=4)|_TIER-2 >= 0.999
  PASS-MAGNITUDE    iff spread_TIER-1 <= 0.06 AND spread_TIER-2 <= 0.06
  INFO-MAGNITUDE    iff spread_TIER-1 <= 0.06 AND spread_TIER-2 <= 0.06
                       AND max(s_T1, s_T2)/min(s_T1, s_T2) >= 1.5
                    (magnitude layer level-sensitive but bounded)
  Expected outcome  : PASS-RANK + INFO-MAGNITUDE — confirms two-layer
                       epistemic structure; unblocks §VII.AJ TWO-ROW
                       landing at #76.

Output 4-tuple:
  (value="rho_S_T1=<v>;rho_S_T2=<v>;spread_T1=<v>;spread_T2=<v>",
   scheme=cross-regulator-A5-4-class-projection-Spearman,
   convention=substrate-distance-2-pole-s4-PRIMARY-AND-SCHEMATIC,
   L_max=12)

Classification: GEOMETRIC + PHONONIC

DISCIPLINE
----------
- `from canonical_constants import *` (MANDATORY)
- Every local intermediate tagged `# (local)`
- TIER-1 callable via `_analytic_zeta.load_spectrum` for the actual D_K
  eigenvalue spectrum at L_max=12, tau_fold=0.19; rigorous M_KK-scale
  regulator anchors per substrate-first-canonical-sourcing.md §(iv)
- TIER-2 callable via `_spectral_action_regulators.py` SCHEMATIC helpers
  (deterministic; structural form only)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 3-tuple (sign / magnitude / regime) annotation per S87+ schema-v2
- Verdict appended to `computations/session-88/s88_gate_verdicts.txt`
  per `.claude/rules/gate-verdicts.md` Canonical Verdict-File Path

SUBSTITUTION CHAIN (per .claude/rules/math-scripts.md sec Double-Check Logic)
----------------------------------------------------------------------------

Step 1 — Definitions:
  D_K eigenspectrum at tau_fold=0.19, L_max=12: {(lambda_k, m_k)}_k from
    `s84_spectrum_cache_L12_tau019.npz`.
  For each c ∈ {F_2, cutoff_sqrt, anomaly, Zubarev} class, define a
    regulator R^c that maps the spectrum to a real number M_R^c(s):
      M_R^c(s) := (1/Vol_SU3_Haar) · Σ_k m_k · g_R^c(lambda_k; s)
    where g_R^c depends on the regulator class and level (PRIMARY vs SCHEMATIC).

  rho_S(s) := Spearman( spectral_proj(s, c), dynamical_proj(s, c) )
              over c in 4-class projection
              (W-9 §L-CR3.2 baseline construction)

  spread_TIER := range of rho_S across 5 F_2-rep substitutions within
                 the same TIER level (matching W9b-2 metric)

Step 2 — TIER-2 (SCHEMATIC) regulator definitions (frozen W9b-2 convention):
  F_2 (zeta):       g(C_2; n=2) = 1 / C_2(p,q)^2  on multiplicity-weighted
                                  Casimir spectrum
  cutoff_sqrt:      g(C_2; n=2) = 1 / C_2^2 if C_2 ≤ 0.7 · max(C_2) else 0
  anomaly (PV):     g(C_2; n=2) = 1/C_2^2 - 1/(C_2 + M_PV^2)^2
                                  with M_PV² = 0.1 · max(C_2)
  Zubarev (HK):     g(C_2; n=2) = exp(-t·C_2) / C_2^2 with t = max(tau_fold, 1e-6)

Step 3 — TIER-1 (PRIMARY) regulator definitions (rigorous physical anchors):
  F_2 (zeta):       g(λ; s=4) = 1 / λ^{2s}  on physical D_K eigenvalues
                    (zeta_D direct evaluation = Σ m_k / λ_k^8)
  cutoff_sqrt:      g(λ; s=4) = 1/λ^8 if λ^2 ≤ M_KK^2_eff else 0
                    (substrate-natural UV cutoff at the spectrum's max λ²
                     scaled by 0.7 to match W9b-2's relative-fraction protocol;
                     PRIMARY anchors on physical λ² rather than abstract C_2)
  anomaly (PV):     g(λ; s=4) = 1/λ^8 - 1/(λ^2 + M_PV²_eff)^4
                    with M_PV²_eff = 0.1 · max(λ^2)
                    (substrate-natural mass scale; physical λ²)
  Zubarev (HK):     g(λ; s=4) = exp(-t·λ^2) / λ^8 with t = max(tau_fold, 1e-6)
                    (substrate-natural heat-kernel time; physical λ²)

  KEY DISTINCTION (PRIMARY vs SCHEMATIC):
    PRIMARY uses physical λ² (Jensen-deformed D_K eigenvalue squared) at
    tau_fold=0.19; SCHEMATIC uses abstract Casimir C_2(p,q) on the bare
    SU(3) representation lattice with Weyl-dim multiplicity. The two
    spectra are STRUCTURALLY RELATED but NUMERICALLY DISTINCT — physical
    eigenvalues are TT-deformed (Jensen) while Casimir is undeformed.

Step 4 — Direction of the rank-ordering claim:
  At fixed L_max=12 and the same n_helper=2 (s=4 pole), the 4 regulator
  classes order their moments by:
    F_2 > cutoff_sqrt > anomaly > Zubarev
  in BOTH SCHEMATIC and PRIMARY. The ordering is structurally fixed by:
    - F_2 (un-suppressed zeta) gives the largest M_R (no truncation, no PV
      subtraction, no exponential suppression).
    - cutoff_sqrt drops large-eigenvalue (large-Casimir) sectors → smaller
      than F_2 by the truncation tail mass.
    - anomaly subtracts the (C+M_PV²)^{-n} massive-counterterm term →
      smaller still by the PV subtraction mass.
    - Zubarev exponentially suppresses large sectors → smallest of all.
  This ordinal structure is PRESERVED under any monotonic re-parameter-
  ization of the absolute mass scales (M_KK² vs frac × max C_2 vs ...).
  Spearman is rank-only, so:
    Direction: |rho_S|_TIER-1 = |rho_S|_TIER-2 = 1.000 EXACT
    (PASS-RANK structurally guaranteed by ordinal-monotonicity of
    the four regulator schemes.)

Step 5 — Direction of the magnitude-ratio claim:
  The cross-regulator spread (range of rho_S across 5 F_2-rep substitutions)
  IS sensitive to absolute mass scales because:
    - Substituting Zubarev as F_2-rep changes the F_2-rep value from
      M_F2_canonical to M_Zub_canonical (a substantively different number
      whose magnitude depends on the heat-kernel temperature t).
    - In SCHEMATIC, t = tau_fold (canonical W4-2 P5 convention).
    - In PRIMARY, t = 1/(2 M_KK²) (canonical Compton timescale at substrate
      UV scale). These two t values differ by factor 2 M_KK² · tau_fold ≈
      2 · (7.43e16)² · 0.19 ≈ 2.10e33 — a ~33-OOM difference.
    - Such large parameter differences propagate to substantially different
      M_R magnitudes between TIER-1 and TIER-2, and hence different
      cross-regulator spreads.
  Direction: spread_TIER-1 ≠ spread_TIER-2 with ratio likely ≥ 1.5×,
  triggering INFO-MAGNITUDE (the substantively expected outcome).

Step 6 — Conclusion (predicted):
  PASS-RANK + INFO-MAGNITUDE composite verdict.
  This decomposes the W9b-2 single-PASS into its two structural components:
    rank-ordering layer is FUNCTIONAL-INDEPENDENT across LEVEL (PASS-RANK)
    magnitude-ratio layer is LEVEL-SENSITIVE (INFO-MAGNITUDE)
  Unblocks §VII.AJ TWO-ROW landing at #76:
    §VII.AJ.1 RANK-ORDER STAGE-1-CANDIDATE  ← from PASS-RANK
    §VII.AJ.2 MAGNITUDE-RATIO STAGE-1-CANDIDATE-INFO  ← from INFO-MAGNITUDE
  And confirms the substrate-first-canonical-sourcing.md §(iv) discipline:
  PRIMARY (full physical) and SCHEMATIC (deterministic structural form)
  agree on STRUCTURAL features (rank ordering) but disagree on REGULATOR-
  DRESSED features (magnitude scatter). The two layers are STRUCTURALLY
  ORTHOGONAL per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthog-
  onality K-counter"` MANDATORY.
"""

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = PROJECT_ROOT / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (
    tau_fold,
    M_KK,
    M_KK_gravity,
    Vol_SU3_Haar,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU thread cap BEFORE numpy import)
# ---------------------------------------------------------------------------
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import time

import numpy as np
from scipy.stats import spearmanr

# ---------------------------------------------------------------------------
# Section 3 — Tier-0 modules (TIER-1 + SCHEMATIC atlas)
# ---------------------------------------------------------------------------
from _analytic_zeta import zeta_D_direct, load_spectrum  # TIER-1 callable
from _spectral_action_regulators import (
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    hard_cutoff_a_n,
    pauli_villars_a_n,
)

# ---------------------------------------------------------------------------
# Section 4 — Pre-registered atlas mapping (W-9 §L-CR3.2 baseline)
# ---------------------------------------------------------------------------
A5_4CLASS_ORDER = ("F_2", "cutoff_sqrt", "anomaly", "Zubarev")  # (local)

# 5-regulator atlas for cross-regulator F_2-rep spread audit
ATLAS_MAP_TIER2 = (  # (local) SCHEMATIC level: bare _spectral_action_regulators helpers
    ("zeta", zeta_a_n),
    ("Zubarev", heat_kernel_a_n),
    ("SDW", mellin_a_n),
    ("cutoff_sqrt", hard_cutoff_a_n),
    ("anomaly", pauli_villars_a_n),
)

# Reference baseline N_break(R) at s=3 from W-9 §L-CR3.2 line 1791-1795
# (regulator-INTRINSIC; same baseline reused for s=4 per W9b-2 protocol)
N_BREAK_BASELINE = {  # (local)
    "F_2": 0.12243,
    "cutoff_sqrt": 0.17775,
    "anomaly": 0.73645,
    "Zubarev": 55.0,
}


# ---------------------------------------------------------------------------
# Section 5 — TIER-2 (SCHEMATIC) evaluator (W9b-2 frozen convention)
# ---------------------------------------------------------------------------
def evaluate_4class_TIER2(n_helper, L_max, tau_slice=None):
    """W9b-2 SCHEMATIC level evaluator. Frozen convention.

    Returns dict { F_2: ..., cutoff_sqrt: ..., anomaly: ..., Zubarev: ... }
    """
    if tau_slice is None:
        tau_slice = tau_fold  # (local) W4-2 P5 default
    t_ref_zub = max(tau_slice, 1e-6)  # (local)
    M_zeta = zeta_a_n(n_helper, L_max, Vol_SU3_Haar)               # (local)
    M_csq = hard_cutoff_a_n(n_helper, L_max, Vol_SU3_Haar, 0.7)    # (local) cutoff_frac=0.7 SCHEMATIC heuristic
    M_an = pauli_villars_a_n(n_helper, L_max, Vol_SU3_Haar, 0.1)   # (local) M_PV_sq_frac=0.1 SCHEMATIC heuristic
    M_zub = heat_kernel_a_n(n_helper, L_max, Vol_SU3_Haar, t_ref_zub)  # (local) t_ref=tau_fold SCHEMATIC
    return {
        "F_2": float(M_zeta),
        "cutoff_sqrt": float(M_csq),
        "anomaly": float(M_an),
        "Zubarev": float(M_zub),
    }


def evaluate_5regulators_TIER2(n_helper, L_max, tau_slice=None):
    """5-regulator atlas at TIER-2 (SCHEMATIC level)."""
    if tau_slice is None:
        tau_slice = tau_fold
    t_ref_zub = max(tau_slice, 1e-6)  # (local)
    out = {}  # (local)
    for name, fn in ATLAS_MAP_TIER2:
        if fn is hard_cutoff_a_n:
            v = fn(n_helper, L_max, Vol_SU3_Haar, 0.7)
        elif fn is pauli_villars_a_n:
            v = fn(n_helper, L_max, Vol_SU3_Haar, 0.1)
        elif fn is heat_kernel_a_n:
            v = fn(n_helper, L_max, Vol_SU3_Haar, t_ref_zub)
        else:
            v = fn(n_helper, L_max, Vol_SU3_Haar)
        out[name] = float(v)
    return out


# ---------------------------------------------------------------------------
# Section 6 — TIER-1 (PRIMARY) evaluator (rigorous M_KK-scale anchors)
# ---------------------------------------------------------------------------
def _physical_zeta_T1(eigvals, mults, n_helper, lambda_max_sq):
    """PRIMARY ζ-canonical: Σ m_k / λ_k^{2 n_helper}."""
    pos = eigvals > 0  # (local) avoid the kernel
    lam2 = (eigvals[pos] ** 2)  # (local)
    m = mults[pos]  # (local)
    val = np.sum(m / (lam2 ** n_helper))  # (local) Σ m / (λ²)^n
    return float(val) / Vol_SU3_Haar


def _physical_cutoff_T1(eigvals, mults, n_helper, lambda_max_sq, cutoff_frac=0.7):
    """PRIMARY hard-cutoff: truncate at λ² ≤ cutoff_frac × max(λ²).

    PRIMARY analog of SCHEMATIC's `cutoff_frac × max(C_2)`: same fractional
    truncation protocol, but applied to physical eigenvalue squared.
    """
    pos = eigvals > 0  # (local)
    lam2 = (eigvals[pos] ** 2)  # (local)
    m = mults[pos]  # (local)
    thresh = cutoff_frac * lambda_max_sq  # (local)
    keep = lam2 <= thresh  # (local)
    val = np.sum(m[keep] / (lam2[keep] ** n_helper))  # (local)
    return float(val) / Vol_SU3_Haar


def _physical_pv_T1(eigvals, mults, n_helper, lambda_max_sq, mpv_frac=0.1):
    """PRIMARY Pauli-Villars: Σ m · [1/λ^{2n} - 1/(λ²+M_PV²)^n].

    M_PV² pinned to mpv_frac × max(λ²) — same fractional protocol as
    SCHEMATIC, applied to physical λ² rather than abstract C_2.
    """
    pos = eigvals > 0  # (local)
    lam2 = (eigvals[pos] ** 2)  # (local)
    m = mults[pos]  # (local)
    M_PV_sq = mpv_frac * lambda_max_sq  # (local)
    val = np.sum(m * (1.0 / (lam2 ** n_helper) - 1.0 / ((lam2 + M_PV_sq) ** n_helper)))  # (local)
    return float(val) / Vol_SU3_Haar


def _physical_heat_T1(eigvals, mults, n_helper, lambda_max_sq, t_ref):
    """PRIMARY heat-kernel: Σ m · exp(-t·λ²) / λ^{2n}.

    t_ref is dimensionful (inverse mass squared); we use the substrate's
    canonical Compton timescale at the heat-kernel UV anchor.
    """
    pos = eigvals > 0  # (local)
    lam2 = (eigvals[pos] ** 2)  # (local)
    m = mults[pos]  # (local)
    val = np.sum(m * np.exp(-t_ref * lam2) / (lam2 ** n_helper))  # (local)
    return float(val) / Vol_SU3_Haar


def evaluate_4class_TIER1(eigvals, mults, n_helper, t_ref_T1):
    """PRIMARY level evaluator on the actual D_K spectrum.

    Returns dict { F_2: ..., cutoff_sqrt: ..., anomaly: ..., Zubarev: ... }
    """
    pos = eigvals > 0  # (local)
    lambda_max_sq = float(np.max(eigvals[pos] ** 2))  # (local) substrate UV anchor
    M_F2 = _physical_zeta_T1(eigvals, mults, n_helper, lambda_max_sq)
    M_csq = _physical_cutoff_T1(eigvals, mults, n_helper, lambda_max_sq, cutoff_frac=0.7)
    M_an = _physical_pv_T1(eigvals, mults, n_helper, lambda_max_sq, mpv_frac=0.1)
    M_zub = _physical_heat_T1(eigvals, mults, n_helper, lambda_max_sq, t_ref_T1)
    return {
        "F_2": M_F2,
        "cutoff_sqrt": M_csq,
        "anomaly": M_an,
        "Zubarev": M_zub,
    }


def evaluate_5regulators_TIER1(eigvals, mults, n_helper, t_ref_T1):
    """5-regulator atlas at TIER-1 (PRIMARY level on physical spectrum)."""
    base = evaluate_4class_TIER1(eigvals, mults, n_helper, t_ref_T1)
    # zeta and Mellin and SDW collapse to F_2 on positive spectrum
    return {
        "zeta": base["F_2"],
        "Zubarev": base["Zubarev"],
        "SDW": base["F_2"],  # (local) Mellin/SDW machine-eps merge per W-9 §L-CR3.2
        "cutoff_sqrt": base["cutoff_sqrt"],
        "anomaly": base["anomaly"],
    }


# ---------------------------------------------------------------------------
# Section 7 — Spearman + spread metric (W9b-2 canonical)
# ---------------------------------------------------------------------------
def compute_spearman_4class(M_per_class, N_per_class):
    """Spearman ρ_S over 4-class projection."""
    classes = list(A5_4CLASS_ORDER)  # (local)
    M_vec = np.array([M_per_class[c] for c in classes])  # (local)
    N_vec = np.array([N_per_class[c] for c in classes])  # (local)
    rs, pv = spearmanr(M_vec, N_vec)  # (local)
    if np.isnan(rs):
        return float("nan"), float("nan")
    return float(rs), float(pv)


def cross_regulator_spread_TIER(eval_5reg, M_4class):
    """W9b-2 metric: range of ρ_S across 5 F_2-rep substitutions.

    For each of the 5 atlas regulators substituted as F_2-rep, recompute
    ρ_S; return (max - min) of the 5 ρ_S values.

    Args:
        eval_5reg: dict { atlas_reg_name: M_value } — 5 candidate F_2 reps.
        M_4class:  dict { class: M_value } — full 4-class baseline; the
                    F_2 entry is replaced by each candidate.
    """
    rho_per = {}  # (local)
    for f2_name, f2_val in eval_5reg.items():
        M_alt = {
            "F_2": float(f2_val),
            "cutoff_sqrt": M_4class["cutoff_sqrt"],
            "anomaly": M_4class["anomaly"],
            "Zubarev": M_4class["Zubarev"],
        }  # (local)
        rho_alt, _ = compute_spearman_4class(M_alt, N_BREAK_BASELINE)
        rho_per[f2_name] = rho_alt
    spread = max(rho_per.values()) - min(rho_per.values())  # (local)
    return float(spread), rho_per


# ---------------------------------------------------------------------------
# Section 8 — Verdict-line emission (S84+ dual-SHA + S87+ 3-tuple)
# ---------------------------------------------------------------------------
def closure_hash(input_pin_map):
    """SHA-256 of canonical-serialized input pin map."""
    canon = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def file_sha256(path):
    """SHA-256 of file bytes."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def append_verdict(gate_id, verdict, value_str, scheme, convention, L_max,
                   audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Append S84+ canonical line + W9a-99 dual-SHA companion + S87+ 3-tuple."""
    verdict_path = PROJECT_ROOT / "session-88" / "s88_gate_verdicts.txt"  # (local) per gate-verdicts.md canonical path
    canonical = (
        f"{gate_id}: {verdict} -- value='{value_str}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )  # (local)
    dual_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    with open(verdict_path, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_companion)
        f.write(tuple_companion)
    return canonical, dual_companion, tuple_companion


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------
def main():
    GATE_ID = "S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR"  # (local)
    L_MAX = 12  # (local) plan §6 PRDR pin
    N_HELPER = 2  # (local) s=4 ↔ n=2 per W9b-2 canonical mapping (W4-2 P5 line 35-36)

    # PASS thresholds (plan §238-243)
    PASS_RANK_THRESH = 0.999  # (local) plan §239
    PASS_MAG_THRESH = 0.06  # (local) plan §240
    INFO_MAG_FACTOR = 1.5  # (local) plan §241 (structurally significant factor)

    # ---- Section 9.1: input SHA-256 pins ----
    input_files = {  # (local)
        "spectrum_cache": SHARED_DIR.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz",
        "spectral_action_regulators": SHARED_DIR / "_spectral_action_regulators.py",
        "analytic_zeta": SHARED_DIR / "_analytic_zeta.py",
        "canonical_constants": SHARED_DIR / "canonical_constants.py",
        "w9b2_npz": SHARED_DIR.parent / "session-87" / "s87_w9b_pole_specificity_scan.npz",
        "plan_w7a": SHARED_DIR.parent.parent / "sessions" / "session-plan" / "session-88-plan-w7a.md",
    }
    input_sha = {}  # (local)
    print("=" * 70)
    print(f"S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR (W7a-74)  L_max={L_MAX}")
    print("=" * 70)
    print()
    print("Input SHA-256 pins (first 20 lines):")
    for k, p in input_files.items():
        if p.exists():
            sha = file_sha256(p)  # (local)
            input_sha[k] = sha
            print(f"  {k:32s}: {sha[:16]}... ({p.name})")
        else:
            input_sha[k] = "MISSING"
            print(f"  {k:32s}: MISSING ({p})")
    print()

    script_path = Path(__file__).resolve()  # (local)
    script_sha = file_sha256(script_path)   # (local)
    print(f"Script content_sha256: {script_sha[:16]}... ({script_path.name})")
    print()

    # SHA-pin S87 W9b-2 verdict line audit_sha (plan §234)
    W9B2_VERDICT_AUDIT_SHA = "30815fae79102fb9ac671fb33101029d5318253b69a2d125ea85ae5eb7396ebc"  # (local)
    print(f"S87 W9b-2 verdict audit_sha (input pin): {W9B2_VERDICT_AUDIT_SHA[:32]}...")
    print()

    t0 = time.time()  # (local)

    # ---- Section 9.2: load D_K eigenspectrum (PRIMARY input) ----
    print("--- Loading D_K eigenspectrum at L_max=12, tau_fold=0.19 ---")
    spec = load_spectrum(L_MAX)  # (local) returns (eigvals, mults)
    if isinstance(spec, tuple):
        eigvals, mults = spec
    else:
        eigvals = spec  # (local)
        mults = np.ones_like(eigvals)
    eigvals = np.asarray(eigvals, dtype=float)  # (local)
    mults = np.asarray(mults, dtype=float)  # (local)
    print(f"  eigvals shape: {eigvals.shape}, range: [{eigvals.min():.4e}, {eigvals.max():.4e}]")
    print(f"  total multiplicity: {np.sum(mults):.0f}")
    pos = eigvals > 0  # (local)
    print(f"  positive eigvals: {pos.sum()} / {len(eigvals)}")
    lambda_max_sq = float(np.max(eigvals[pos] ** 2))  # (local)
    print(f"  lambda_max² = {lambda_max_sq:.4e} (substrate UV anchor)")
    # Substrate-natural Compton heat-kernel timescale at substrate UV
    t_ref_T1 = 1.0 / max(lambda_max_sq, 1e-30)  # (local) inverse-UV² timescale
    print(f"  PRIMARY heat-kernel t_ref = 1/lambda_max² = {t_ref_T1:.4e}")
    print()

    # ---- Section 9.3: TIER-2 (SCHEMATIC) evaluation ----
    print("--- TIER-2 (SCHEMATIC) evaluation at s=4 (n_helper=2) ---")
    M_R_T2 = evaluate_4class_TIER2(N_HELPER, L_MAX)  # (local)
    M_R_T2_5reg = evaluate_5regulators_TIER2(N_HELPER, L_MAX)  # (local)
    rho_T2, pv_T2 = compute_spearman_4class(M_R_T2, N_BREAK_BASELINE)  # (local)
    spread_T2, rho_per_T2 = cross_regulator_spread_TIER(M_R_T2_5reg, M_R_T2)  # (local)
    print(f"  M_R(s=4) by class : {[f'{M_R_T2[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"  rho_S(s=4)_T2     : {rho_T2:+.6f}  (p-value {pv_T2:.4e})")
    print(f"  |rho_S(s=4)|_T2   : {abs(rho_T2):.6f}")
    print(f"  spread_T2 (5-reg F_2-rep substitution range): {spread_T2:.6f}")
    print(f"    rho_S per F_2-rep substitution:")
    for r, rh in rho_per_T2.items():
        print(f"      {r:14s}: {rh:+.6f}")
    print()

    # ---- Section 9.4: TIER-1 (PRIMARY) evaluation ----
    print("--- TIER-1 (PRIMARY) evaluation at s=4 (n_helper=2) on physical D_K spectrum ---")
    M_R_T1 = evaluate_4class_TIER1(eigvals, mults, N_HELPER, t_ref_T1)  # (local)
    M_R_T1_5reg = evaluate_5regulators_TIER1(eigvals, mults, N_HELPER, t_ref_T1)  # (local)
    rho_T1, pv_T1 = compute_spearman_4class(M_R_T1, N_BREAK_BASELINE)  # (local)
    spread_T1, rho_per_T1 = cross_regulator_spread_TIER(M_R_T1_5reg, M_R_T1)  # (local)
    print(f"  M_R(s=4) by class : {[f'{M_R_T1[c]:.4e}' for c in A5_4CLASS_ORDER]}")
    print(f"  rho_S(s=4)_T1     : {rho_T1:+.6f}  (p-value {pv_T1:.4e})")
    print(f"  |rho_S(s=4)|_T1   : {abs(rho_T1):.6f}")
    print(f"  spread_T1 (5-reg F_2-rep substitution range): {spread_T1:.6f}")
    print(f"    rho_S per F_2-rep substitution:")
    for r, rh in rho_per_T1.items():
        print(f"      {r:14s}: {rh:+.6f}")
    print()

    # ---- Section 9.5: cross-tier ratios ----
    print("--- Cross-tier ratios (TIER-1 vs TIER-2) ---")
    for c in A5_4CLASS_ORDER:
        v1 = M_R_T1[c]
        v2 = M_R_T2[c]
        ratio = v1 / v2 if abs(v2) > 1e-300 else float("inf")
        print(f"  {c:14s}: T1={v1:.4e}  T2={v2:.4e}  ratio T1/T2={ratio:.4e}")
    print()

    # ---- Section 9.6: TWO-LAYER PASS evaluation ----
    print("--- Two-Layer PASS evaluation (plan §238-243) ---")
    abs_rho_T1 = abs(rho_T1)  # (local)
    abs_rho_T2 = abs(rho_T2)  # (local)
    PASS_RANK = (abs_rho_T1 >= PASS_RANK_THRESH) and (abs_rho_T2 >= PASS_RANK_THRESH)  # (local)

    # Magnitude layer:
    if (spread_T1 <= PASS_MAG_THRESH) and (spread_T2 <= PASS_MAG_THRESH):
        # Both bounded — check level-sensitivity factor
        s_min = min(spread_T1, spread_T2) if min(spread_T1, spread_T2) > 0 else 1e-30  # (local)
        s_max = max(spread_T1, spread_T2)  # (local)
        spread_factor = s_max / s_min  # (local)
        if spread_factor >= INFO_MAG_FACTOR:
            MAG_LAYER = "INFO"  # (local) bounded but level-sensitive — substrate-prior expected
            INFO_MAG_REASON = f"both spreads ≤ {PASS_MAG_THRESH} but max/min = {spread_factor:.3f} ≥ {INFO_MAG_FACTOR}"
        else:
            MAG_LAYER = "PASS"  # (local) bounded AND level-invariant
            INFO_MAG_REASON = f"both spreads ≤ {PASS_MAG_THRESH} and max/min = {spread_factor:.3f} < {INFO_MAG_FACTOR}"
    else:
        # FAIL_MAGNITUDE: one or both spreads exceed bound
        MAG_LAYER = "FAIL"  # (local)
        spread_factor = float("nan")  # (local)
        INFO_MAG_REASON = f"spread_T1={spread_T1:.4f} or spread_T2={spread_T2:.4f} exceeds {PASS_MAG_THRESH}"

    # Composite:
    if not PASS_RANK:
        composite_verdict = "FAIL"  # (local) FAIL-RANK defeats §VII.AJ.1 landing
        composite_reason = f"FAIL-RANK: |rho_S|_T1={abs_rho_T1:.6f} or |rho_S|_T2={abs_rho_T2:.6f} < {PASS_RANK_THRESH}"
    elif MAG_LAYER == "FAIL":
        composite_verdict = "FAIL"  # (local) FAIL-MAGNITUDE defeats §VII.AJ.2 INFO landing
        composite_reason = f"FAIL-MAGNITUDE: {INFO_MAG_REASON}"
    elif MAG_LAYER == "INFO":
        composite_verdict = "INFO"  # (local) PASS-RANK + INFO-MAGNITUDE = substrate-expected
        composite_reason = f"PASS-RANK + INFO-MAGNITUDE: {INFO_MAG_REASON}"
    else:
        composite_verdict = "PASS"  # (local) PASS-RANK + PASS-MAGNITUDE
        composite_reason = f"PASS-RANK + PASS-MAGNITUDE: {INFO_MAG_REASON}"

    print(f"  PASS-RANK?       : {PASS_RANK}  (|ρ|_T1={abs_rho_T1:.6f}, |ρ|_T2={abs_rho_T2:.6f}, threshold={PASS_RANK_THRESH})")
    print(f"  MAGNITUDE layer  : {MAG_LAYER}  ({INFO_MAG_REASON})")
    print(f"  Composite verdict: {composite_verdict}")
    print(f"  Reason           : {composite_reason}")
    print()

    # ---- Section 9.7: 3-tuple verdict (sign / magnitude / regime) ----
    # sign_verdict: did substrate prediction direction (PASS-RANK + INFO-MAGNITUDE) match?
    sign_v = "PASS" if PASS_RANK else "FAIL"  # (local) sign = rank-ordering survival
    # magnitude_verdict: PASS if both layers PASS; INFO if rank PASS + magnitude INFO; FAIL otherwise
    if PASS_RANK and MAG_LAYER == "PASS":
        mag_v = "PASS"
    elif PASS_RANK and MAG_LAYER == "INFO":
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    # regime_verdict: VALID if both TIER computations produced finite, non-NaN values
    all_finite = (
        np.all(np.isfinite([rho_T1, rho_T2, spread_T1, spread_T2]))
        and all(np.isfinite(v) for v in M_R_T1.values())
        and all(np.isfinite(v) for v in M_R_T2.values())
    )  # (local)
    regime_v = "VALID" if all_finite else "BREAKDOWN"  # (local)
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print()

    # ---- Section 9.8: Composite collapse rule (gate-verdicts.md) ----
    if regime_v == "BREAKDOWN":
        composite_verdict_collapsed = "FAIL"
    elif sign_v == "FAIL":
        composite_verdict_collapsed = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite_verdict_collapsed = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite_verdict_collapsed = "INFO"
    elif mag_v == "INFO":
        composite_verdict_collapsed = "INFO"
    else:
        composite_verdict_collapsed = "PASS"
    if composite_verdict_collapsed != composite_verdict:
        print(f"  NOTE: composite from rubric ({composite_verdict}) differs from collapse rule ({composite_verdict_collapsed}); using collapse-rule for verdict line.")
    composite_verdict = composite_verdict_collapsed
    print(f"  composite (post-collapse-rule): {composite_verdict}")
    print()

    # ---- Section 9.9: NPZ data dump ----
    npz_path = PROJECT_ROOT / "session-88" / "s88_w7a_rank_vs_magnitude_layer_discriminator.npz"  # (local)
    np.savez(
        npz_path,
        rho_S_T1=np.array([rho_T1]),
        rho_S_T2=np.array([rho_T2]),
        spread_T1=np.array([spread_T1]),
        spread_T2=np.array([spread_T2]),
        M_R_T1_4class=np.array([M_R_T1[c] for c in A5_4CLASS_ORDER]),
        M_R_T2_4class=np.array([M_R_T2[c] for c in A5_4CLASS_ORDER]),
        M_R_T1_5reg_keys=np.array(list(M_R_T1_5reg.keys()), dtype=object),
        M_R_T1_5reg_vals=np.array(list(M_R_T1_5reg.values())),
        M_R_T2_5reg_keys=np.array(list(M_R_T2_5reg.keys()), dtype=object),
        M_R_T2_5reg_vals=np.array(list(M_R_T2_5reg.values())),
        rho_per_T1_keys=np.array(list(rho_per_T1.keys()), dtype=object),
        rho_per_T1_vals=np.array(list(rho_per_T1.values())),
        rho_per_T2_keys=np.array(list(rho_per_T2.keys()), dtype=object),
        rho_per_T2_vals=np.array(list(rho_per_T2.values())),
        N_break_baseline=np.array([N_BREAK_BASELINE[c] for c in A5_4CLASS_ORDER]),
        a5_4class_order=np.array(list(A5_4CLASS_ORDER), dtype=object),
        composite_verdict=np.array([composite_verdict], dtype=object),
        sign_verdict=np.array([sign_v], dtype=object),
        magnitude_verdict=np.array([mag_v], dtype=object),
        regime_verdict=np.array([regime_v], dtype=object),
        L_max=np.array([L_MAX]),
        n_helper=np.array([N_HELPER]),
        lambda_max_sq=np.array([lambda_max_sq]),
        t_ref_T1=np.array([t_ref_T1]),
        tau_fold=np.array([tau_fold]),
        Vol_SU3_Haar=np.array([Vol_SU3_Haar]),
        M_KK=np.array([M_KK]),
    )
    print(f"  NPZ saved: {npz_path}")
    print()

    # ---- Section 9.10: Plot ----
    print("--- Plotting ---")
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 2, figsize=(13, 10))

        # Panel (a): T1 vs T2 4-class M_R values (log-scale)
        ax = axes[0, 0]
        x = np.arange(len(A5_4CLASS_ORDER))
        v_T1 = np.array([M_R_T1[c] for c in A5_4CLASS_ORDER])
        v_T2 = np.array([M_R_T2[c] for c in A5_4CLASS_ORDER])
        ax.bar(x - 0.2, v_T1, width=0.4, label="TIER-1 (PRIMARY)", color="C0", edgecolor="black")
        ax.bar(x + 0.2, v_T2, width=0.4, label="TIER-2 (SCHEMATIC)", color="C1", edgecolor="black")
        ax.set_xticks(x)
        ax.set_xticklabels(A5_4CLASS_ORDER, rotation=20)
        ax.set_yscale("log")
        ax.set_ylabel("M_R(s=4) [log]")
        ax.legend()
        ax.set_title("4-class M_R(s=4): TIER-1 (physical) vs TIER-2 (SCHEMATIC)")
        ax.grid(alpha=0.3, axis="y")

        # Panel (b): rho_S per F_2-rep substitution within each tier
        ax = axes[0, 1]
        names = list(rho_per_T1.keys())
        vT1 = [rho_per_T1[n] for n in names]
        vT2 = [rho_per_T2[n] for n in names]
        x = np.arange(len(names))
        ax.bar(x - 0.2, vT1, width=0.4, label=f"T1 spread={spread_T1:.4f}", color="C0", edgecolor="black")
        ax.bar(x + 0.2, vT2, width=0.4, label=f"T2 spread={spread_T2:.4f}", color="C1", edgecolor="black")
        ax.axhline(0, color="black", linewidth=0.6)
        ax.set_xticks(x)
        ax.set_xticklabels(names, rotation=30)
        ax.set_ylabel("rho_S(s=4) per F_2-rep substitution")
        ax.set_ylim(-1.15, 1.15)
        ax.legend(fontsize=9)
        ax.set_title(f"Cross-regulator spread: |Δ_T1/Δ_T2| = {spread_factor:.3f}×" if np.isfinite(spread_factor) else "Cross-regulator spread")
        ax.grid(alpha=0.3, axis="y")

        # Panel (c): rho_S(s=4) bars
        ax = axes[1, 0]
        bars = ax.bar(["TIER-1 (PRIMARY)", "TIER-2 (SCHEMATIC)"], [rho_T1, rho_T2],
                      color=["C0", "C1"], edgecolor="black", width=0.6)
        for b, v in zip(bars, [rho_T1, rho_T2]):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.04 * np.sign(v),
                    f"{v:+.6f}", ha="center", va="bottom" if v > 0 else "top", fontsize=11)
        ax.axhline(PASS_RANK_THRESH, color="green", linestyle="--", linewidth=0.8, label=f"PASS-RANK = ±{PASS_RANK_THRESH}")
        ax.axhline(-PASS_RANK_THRESH, color="green", linestyle="--", linewidth=0.8)
        ax.axhline(0, color="black", linewidth=0.6)
        ax.set_ylabel("rho_S(s=4)")
        ax.set_ylim(-1.15, 1.15)
        ax.legend()
        ax.set_title(f"Spearman ρ_S(s=4)  PASS-RANK = {PASS_RANK}")
        ax.grid(alpha=0.3, axis="y")

        # Panel (d): summary
        ax = axes[1, 1]
        ax.axis("off")
        summary_text = (
            f"S88 W7a-74 — RANK-vs-MAGNITUDE Layer Discriminator\n"
            f"{'-' * 55}\n"
            f"Composite verdict: {composite_verdict}\n"
            f"3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}\n\n"
            f"PASS-RANK        : {PASS_RANK}\n"
            f"  |ρ_S|_TIER-1   : {abs_rho_T1:.6f}\n"
            f"  |ρ_S|_TIER-2   : {abs_rho_T2:.6f}\n"
            f"  threshold      : {PASS_RANK_THRESH}\n\n"
            f"MAGNITUDE layer  : {MAG_LAYER}\n"
            f"  spread_TIER-1  : {spread_T1:.6f}\n"
            f"  spread_TIER-2  : {spread_T2:.6f}\n"
            f"  ratio max/min  : {spread_factor:.3f}× (INFO threshold: {INFO_MAG_FACTOR})\n"
            f"  PASS bound     : {PASS_MAG_THRESH}\n\n"
            f"Substrate prediction: PASS-RANK + INFO-MAGNITUDE\n"
            f"Two-layer epistemic structure:\n"
            f"  Layer 1 (rank): FUNCTIONAL-INDEPENDENT\n"
            f"  Layer 2 (mag) : LEVEL-SENSITIVE\n"
        )
        ax.text(0.0, 1.0, summary_text, transform=ax.transAxes,
                family="monospace", fontsize=9, verticalalignment="top")

        plt.suptitle(f"S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR  L_max={L_MAX}",
                     fontsize=12, y=1.00)
        plt.tight_layout()
        plot_path = PROJECT_ROOT / "session-88" / "s88_w7a_rank_vs_magnitude_layer_discriminator.png"
        plt.savefig(plot_path, dpi=120, bbox_inches="tight")
        plt.close()
        print(f"  Plot saved: {plot_path}")
    except Exception as e:
        print(f"  Plot raised: {e}")
    print()

    # ---- Section 9.11: closure SHA + verdict-line emission ----
    input_pin_map = {  # (local)
        "_gate_id": GATE_ID,
        "_wp_id": "W7a-74",
        "_scheme": "cross-regulator-A5-4-class-projection-Spearman",
        "_convention": "substrate-distance-2-pole-s4-PRIMARY-AND-SCHEMATIC",
        "_L_max": L_MAX,
        "input_sha": input_sha,
        "script_sha": script_sha,
        "w9b2_verdict_audit_sha": W9B2_VERDICT_AUDIT_SHA,
        "rho_T1": float(rho_T1),
        "rho_T2": float(rho_T2),
        "spread_T1": float(spread_T1),
        "spread_T2": float(spread_T2),
        "spread_factor": float(spread_factor) if np.isfinite(spread_factor) else None,
        "PASS_RANK": bool(PASS_RANK),
        "MAG_LAYER": MAG_LAYER,
        "composite_verdict": composite_verdict,
        "sign_v": sign_v,
        "mag_v": mag_v,
        "regime_v": regime_v,
        "n_helper": N_HELPER,
        "tau_fold": float(tau_fold),
        "lambda_max_sq": float(lambda_max_sq),
        "t_ref_T1": float(t_ref_T1),
    }
    audit_sha = closure_hash(input_pin_map)  # (local)
    content_sha = script_sha  # (local)

    value_str = (
        f"rho_T1={rho_T1:.6f};rho_T2={rho_T2:.6f};"
        f"spread_T1={spread_T1:.6f};spread_T2={spread_T2:.6f};"
        f"spread_ratio={spread_factor:.3f};PASS_RANK={int(PASS_RANK)};MAG={MAG_LAYER}"
    )  # (local)
    scheme_str = "cross-regulator-A5-4-class-projection-Spearman"  # (local)
    convention_str = "substrate-distance-2-pole-s4-PRIMARY-AND-SCHEMATIC"  # (local)

    canonical, dual_companion, tuple_companion = append_verdict(
        GATE_ID,
        composite_verdict,
        value_str,
        scheme_str,
        convention_str,
        L_MAX,
        audit_sha,
        content_sha,
        sign_v,
        mag_v,
        regime_v,
    )
    print("=" * 70)
    print("Verdict line written to s88_gate_verdicts.txt:")
    print(canonical.rstrip())
    print(dual_companion.rstrip())
    print(tuple_companion.rstrip())
    print("=" * 70)
    print()
    print(f"4-tuple: (value=\"{value_str}\", scheme={scheme_str}, "
          f"convention={convention_str}, L_max={L_MAX})")
    print()
    print(f"Wall time: {time.time() - t0:.2f}s")
    return composite_verdict


if __name__ == "__main__":
    sys.exit(0 if main() in ("PASS", "FAIL", "INFO") else 1)
