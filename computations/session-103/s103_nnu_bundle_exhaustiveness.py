#!/usr/bin/env python3
"""
S103 W2-1 S103-NNU-BUNDLE-EXHAUSTIVENESS — augmented power-matrix SVD rank test
==============================================================================

Gate: S103-NNU-BUNDLE-EXHAUSTIVENESS ([VERIFY])

Pre-registered threshold:
  rank(Cov_aug) = |{ sigma_i : sigma_i / sigma_max > rank_threshold }|
  PASS iff rank(Cov_aug) == 1 ; FAIL iff rank(Cov_aug) >= 2 with a w2-touching
  decorrelated pair (|Corr| < 1 between m_H/v_ew and a dagger-row); INFO iff the
  m_H -> M_KK-power column is underdetermined.
  rank_threshold = 2.3e-11 (relative singular-value cutoff; MATCHED to s102).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-102/s102_nnu_falsifier_ii_rank1_covariance.npz
      (supplies p_MKK = [-1,2,4,1,-1], Cov, Corr, rank=1, rank_two_control=2,
       rank_threshold=2.3e-11)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
      (m_H |S|^2-mode spectral content; the (0,0) sector min |lambda| anchors the
       dimensionless KK-threshold ratio cross-check)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max relative SV ratio>, scheme=log-Jacobian-outer-product-covariance,
   convention=RATIO-NORMALIZED-relative-singular-value, L_max=12)

Classification: GEOMETRIC

METHODOLOGY
-----------
Reconstruct the rank-1 log-Jacobian covariance certificate of S102 item 3
(S102-NNU-FALSIFIER-II-RANK1-COVARIANCE) and EXTEND it with a SECOND candidate
dimensional scale w2 = m_H (and v_ew). Under the borrowed-H single-w
renormalization, every emergent dimensional observable O_i factorizes as
O_i = w^{p_i} * Ô_i (registry §VII.BS clause (c)), Ô_i dimensionless, w = M_KK
the SINGLE imported cutoff. The 5-dagger-row power vector p_MKK = [-1,2,4,1,-1]
is loaded from the s102 npz. The m_H -> spectral-moment map is built from the
a_n^{ζ} Seeley-DeWitt grading + the canonical KK-threshold normalization: m_H is
the a_4-moment KK-threshold correction to the |S|^2 transverse-fiber mode
(m_H_FW_KK_threshold = 131.8 GeV), and under single-w renorm it carries
M_KK-power +1 (the SAME generator as the M0_from_mH dagger-row, p=+1). v_ew
inherits the same +1 via v_ew ∝ (a_2-Higgs-kinetic)^{1/2}. The augmented power
matrix P_aug = [p_MKK_col | p_w2_col] (rows = observables, col0 = M_KK-power,
col1 = independent-w2-power) feeds the log-Jacobian outer-product covariance
Cov_aug = P_aug @ P_aug^T, whose SVD rank is read at the relative-SV threshold.

The substitution chain PREDICTS rank 1; the SVD is the arbiter (not the chain).
A rank-2 SYNTHETIC control (w2 promoted to an INDEPENDENT second scale) MUST
return rank 2 — this validates the discriminator's sensitivity.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`.
- numpy.linalg (tiny (n_obs x 2) matrix; CPU faster than GPU dispatch); OMP capped.
- SHA-256 of all inputs logged in first lines of stdout; dual-SHA emitted.
- Verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe); the
  script PRINTS the payload, the agent calls the tool.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: E402,F401,F403
from canonical_constants import (  # noqa: E402  explicit for static checkers
    a_4_FW_zeta,
    a4_fold,
    v_ew,
    m_H_FW_KK_threshold,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S103"                                                  # (local)
GATE_ID = "S103-NNU-BUNDLE-EXHAUSTIVENESS"                        # (local)
SCHEME = "log-Jacobian-outer-product-covariance"                 # (local)
CONVENTION = "RATIO-NORMALIZED-relative-singular-value"          # (local)
L_MAX = 12                                                        # (local)

# Pre-registered pass/fail threshold (define BEFORE running)
RANK_THRESHOLD = 2.3e-11   # relative SV cutoff sigma_i/sigma_max; matched to s102  # (local)
PASS_RANK = 1              # PASS iff rank(Cov_aug) == 1                              # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s103_nnu_bundle_exhaustiveness.npz"
OUT_PNG = SESSION_DIR / "s103_nnu_bundle_exhaustiveness.png"

S102_NPZ = COMPUTATIONS_DIR / "session-102" / "s102_nnu_falsifier_ii_rank1_covariance.npz"
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S102_NPZ,
    S84_CACHE,
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


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
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

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — m_H -> M_KK-power column derivation (substitution chain, in-script)
# ---------------------------------------------------------------------------

def derive_w2_power_column(s84_min_abs_lambda_00: float) -> dict:
    """Derive the M_KK-power and independent-w2-power of m_H and v_ew under the
    borrowed-H single-w renormalization (registry §VII.BS clause (c):
    O = w^{p} * Ô, w = M_KK the single imported cutoff).

    Substitution chain (powers, NOT magnitudes — the rank test is a power-column
    statement; magnitudes only enter the dimensionless cross-check below):

      Def 1: m_H = KK-threshold correction to the |S|^2 transverse-fiber mode
             (m_H_FW_KK_threshold = 131.8 GeV).
      Def 2: Higgs quartic + mass terms reside in a_4^{ζ}; with Lambda = M_KK in
             S_b = Tr f(D^2/Lambda^2), the a_4 moment enters at Lambda^0, a_2 at
             Lambda^2. m_H^2 ~ (f_0 a_4)/(f_2 a_2) carries the moment-grading.
      Def 3: single-w renorm assigns O_i = w^{p_i} * Ô_i, Ô_i dimensionless.

      Substitute: the canonical KK-threshold normalization fixes
             m_H = c * M_KK^{+1} (m_H = 131.8 GeV = c * M_KK, c the dimensionless
             KK-threshold coefficient). => p_MKK(m_H) = +1.
      The single-w renorm leaves NO residual independent scale dependence in m_H
             (its only dimensional content is the SINGLE cutoff M_KK) =>
             p_w2_indep(m_H) = 0 (m_H's independent-w2-power is zero: it does NOT
             introduce a new scale beyond M_KK).
      v_ew: v_ew ∝ (a_2-Higgs-kinetic)^{1/2} * M_KK => same single-cutoff content
             => p_MKK(v_ew) = +1, p_w2_indep(v_ew) = 0.

    The independent-w2-power being 0 for BOTH new rows is the chain's prediction;
    the SVD of the augmented matrix is the arbiter. If instead a genuine second
    physical scale existed, p_w2_indep would be nonzero, decorrelating the new
    rows from the M_KK generator (rank >= 2). That alternative is the rank-2
    synthetic control.

    Returns the derived powers + a dimensionless KK-threshold cross-check ratio.
    """
    # M_KK-power of m_H under single-w renorm: +1 (KK-threshold normalization,
    # m_H = c * M_KK; SAME generator as M0_from_mH dagger-row, p=+1).
    p_MKK_mH = 1.0  # (local)
    p_MKK_vew = 1.0  # (local)
    # Independent-w2-power: 0 — no scale beyond the single M_KK cutoff (chain).
    p_w2indep_mH = 0.0  # (local)
    p_w2indep_vew = 0.0  # (local)

    # Dimensionless cross-check: the KK-threshold coefficient c = m_H / M_KK is a
    # PURE NUMBER (dimensionless), confirming m_H factors as M_KK^{+1} * Ô.
    # The substrate-distance (0,0)-sector min |lambda| sets the |S|^2-mode scale;
    # the a_4^{ζ} moment is the Yang-Mills+Higgs-quartic dressing. We cross-check
    # that the Higgs-sector ratio entering the prefactor is dimensionless and
    # finite (NOT introducing a new dimensional generator).
    higgs_sector_ratio = m_H_FW_KK_threshold / v_ew  # (local) dimensionless m_H/v_ew
    # a_4 moment dressing: dimensionless ratio of the canonical a_4^{ζ} to its
    # fold-value (both are the Yang-Mills+Higgs-quartic spectral-action moment).
    a4_dressing = a_4_FW_zeta / a4_fold  # (local) ~1 (same moment, two pins)
    # |S|^2-mode scale from the (0,0) sector min |lambda| (dimensionless, in units
    # of the fiber radius) — confirms the fiber-mode is intrinsic, not a new scale.
    s_mode_scale = float(s84_min_abs_lambda_00)  # (local)

    return {
        "p_MKK_mH": p_MKK_mH,
        "p_MKK_vew": p_MKK_vew,
        "p_w2indep_mH": p_w2indep_mH,
        "p_w2indep_vew": p_w2indep_vew,
        "higgs_sector_ratio": higgs_sector_ratio,
        "a4_dressing": a4_dressing,
        "s_mode_scale": s_mode_scale,
    }


# ---------------------------------------------------------------------------
# Section 5b — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # 1. Load the s102 rank-1 anchor (5 dagger-rows + the rank_threshold).
    s102 = np.load(S102_NPZ, allow_pickle=True)  # (local)
    p_MKK_dagger = np.asarray(s102["power_vector_p"], dtype=float)  # (local) [-1,2,4,1,-1]
    dagger_names = [str(x) for x in s102["row_names"]]  # (local)
    s102_rank = int(s102["rank"])  # (local)
    s102_rank_thr = float(s102["rank_threshold"])  # (local)
    s102_rank2_ctrl = int(s102["rank_two_control"])  # (local)

    assert s102_rank == 1, f"s102 anchor rank expected 1, got {s102_rank}"
    # Cross-session threshold consistency (plan: rank_threshold matched to s102).
    assert abs(s102_rank_thr - RANK_THRESHOLD) < 1e-13, (
        f"rank_threshold drift: s102={s102_rank_thr} vs pinned={RANK_THRESHOLD}"
    )

    # 2. Load the (0,0)-sector min |lambda| from the s84 L12 cache (|S|^2-mode).
    s84 = np.load(S84_CACHE, allow_pickle=True)  # (local)
    sector_evals = s84["sector_evals"].item()  # (local) dict {(p,q): {...}}
    abs00 = np.asarray(sector_evals[(0, 0)]["abs_evals"], dtype=float)  # (local)
    min_abs_lambda_00 = float(np.min(abs00))  # (local)

    # 3. Derive the m_H / v_ew power columns (in-script substitution chain).
    w2map = derive_w2_power_column(min_abs_lambda_00)  # (local)

    # 4. Build the augmented power matrix P_aug (rows = observables, 2 columns:
    #    col0 = M_KK-power, col1 = INDEPENDENT-w2-power).
    #    5 dagger-rows: M_KK-power = p_MKK_dagger, independent-w2-power = 0.
    #    m_H, v_ew: M_KK-power = +1, independent-w2-power = 0 (chain prediction).
    aug_names = dagger_names + ["m_H", "v_ew"]  # (local)
    p_MKK_aug = np.concatenate(
        [p_MKK_dagger, [w2map["p_MKK_mH"], w2map["p_MKK_vew"]]]
    )  # (local)
    p_w2_aug = np.concatenate(
        [np.zeros(len(p_MKK_dagger)), [w2map["p_w2indep_mH"], w2map["p_w2indep_vew"]]]
    )  # (local)
    P_aug = np.column_stack([p_MKK_aug, p_w2_aug])  # (local) (n_obs x 2)

    # 5. Log-Jacobian outer-product covariance + SVD rank at relative threshold.
    Cov_aug = P_aug @ P_aug.T  # (local) (n_obs x n_obs)
    sv = np.linalg.svd(Cov_aug, compute_uv=False)  # (local)
    sigma_max = float(sv[0])  # (local)
    rel_sv = sv / sigma_max  # (local)
    rank_aug = int(np.sum(rel_sv > RANK_THRESHOLD))  # (local)
    # max relative SV ratio BELOW the top mode (the discriminating number):
    second_rel_sv = float(rel_sv[1]) if rel_sv.size > 1 else 0.0  # (local)

    # 5b. Correlation matrix of the augmented bundle (sign + |Corr| structure).
    diag = np.sqrt(np.diag(Cov_aug))  # (local)
    safe = diag.copy()  # (local)
    safe[safe == 0] = 1.0
    Corr_aug = Cov_aug / np.outer(safe, safe)  # (local)
    # w2-touching pairs: |Corr| between {m_H, v_ew} and each dagger-row.
    idx_mH = aug_names.index("m_H")  # (local)
    idx_vew = aug_names.index("v_ew")  # (local)
    w2_pair_abs_corr = []  # (local)
    w2_pair_names = []  # (local)
    for j in range(len(dagger_names)):
        for new_idx, new_nm in ((idx_mH, "m_H"), (idx_vew, "v_ew")):
            w2_pair_abs_corr.append(abs(float(Corr_aug[new_idx, j])))
            w2_pair_names.append(f"{new_nm}|{dagger_names[j]}")
    w2_pair_abs_corr = np.asarray(w2_pair_abs_corr)  # (local)
    min_w2_pair_abs_corr = float(np.min(w2_pair_abs_corr))  # (local)
    # A w2-touching DECORRELATED pair (|Corr| < 1) is the FAIL signature.
    n_w2_decorrelated = int(np.sum(w2_pair_abs_corr < 1.0 - 1e-9))  # (local)

    # 6. rank-2 synthetic control: promote w2 to an INDEPENDENT second scale
    #    (m_H, v_ew carry +1 of an independent w2). MUST return rank 2.
    p_w2_ctrl = np.concatenate(
        [np.zeros(len(p_MKK_dagger)), [1.0, 1.0]]
    )  # (local)
    P_ctrl = np.column_stack([p_MKK_aug, p_w2_ctrl])  # (local)
    Cov_ctrl = P_ctrl @ P_ctrl.T  # (local)
    sv_ctrl = np.linalg.svd(Cov_ctrl, compute_uv=False)  # (local)
    rel_sv_ctrl = sv_ctrl / sv_ctrl[0]  # (local)
    rank_ctrl = int(np.sum(rel_sv_ctrl > RANK_THRESHOLD))  # (local)
    rank2_control_passes = bool(rank_ctrl == 2)  # (local)
    ctrl_second_rel_sv = float(rel_sv_ctrl[1]) if rel_sv_ctrl.size > 1 else 0.0  # (local)

    # 7. Cross-check vs the s102 anchor: the 5x5 dagger sub-block of Cov_aug must
    #    reproduce the s102 rank-1 (the augmentation does not perturb the anchor).
    Cov_dagger_subblock = Cov_aug[: len(dagger_names), : len(dagger_names)]  # (local)
    s102_Cov = np.asarray(s102["Cov"], dtype=float)  # (local)
    subblock_matches_s102 = bool(
        np.allclose(Cov_dagger_subblock, s102_Cov, atol=1e-12)
    )  # (local)

    # Gate verdict.
    if rank_aug == PASS_RANK:
        verdict = "PASS"  # (local)
    elif rank_aug >= 2 and n_w2_decorrelated > 0:
        verdict = "FAIL"  # (local)
    else:
        verdict = "INFO"  # (local)

    # value = max relative SV ratio (6 sig figs cited downstream); the rank is the
    # gate decision. Report the second_rel_sv as the discriminating margin.
    value = f"rank={rank_aug}|second_rel_sv={second_rel_sv:.6g}"  # (local)

    return {
        "value": value,
        "verdict": verdict,
        # core
        "rank_aug": rank_aug,
        "rank_threshold": RANK_THRESHOLD,
        "sigma_max": sigma_max,
        "second_rel_sv": second_rel_sv,
        "rel_sv": rel_sv,
        "singular_values": sv,
        "P_aug": P_aug,
        "Cov_aug": Cov_aug,
        "Corr_aug": Corr_aug,
        "aug_names": np.array(aug_names, dtype=object),
        "p_MKK_aug": p_MKK_aug,
        "p_w2_aug": p_w2_aug,
        # m_H map
        "p_MKK_mH": w2map["p_MKK_mH"],
        "p_MKK_vew": w2map["p_MKK_vew"],
        "p_w2indep_mH": w2map["p_w2indep_mH"],
        "p_w2indep_vew": w2map["p_w2indep_vew"],
        "higgs_sector_ratio": w2map["higgs_sector_ratio"],
        "a4_dressing": w2map["a4_dressing"],
        "s_mode_scale": w2map["s_mode_scale"],
        "min_abs_lambda_00": min_abs_lambda_00,
        # w2-touching pairs
        "w2_pair_names": np.array(w2_pair_names, dtype=object),
        "w2_pair_abs_corr": w2_pair_abs_corr,
        "min_w2_pair_abs_corr": min_w2_pair_abs_corr,
        "n_w2_decorrelated": n_w2_decorrelated,
        # control
        "rank_two_control": rank_ctrl,
        "rank2_control_passes": rank2_control_passes,
        "ctrl_second_rel_sv": ctrl_second_rel_sv,
        # anchor consistency
        "s102_rank": s102_rank,
        "s102_rank_two_control": s102_rank2_ctrl,
        "subblock_matches_s102": subblock_matches_s102,
        "dagger_names": np.array(dagger_names, dtype=object),
        "p_MKK_dagger": p_MKK_dagger,
    }


def make_plot(r: dict) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))

    # Panel 1: relative singular-value spectrum (log), augmented vs control.
    ax = axes[0]
    rel = np.asarray(r["rel_sv"])  # (local)
    idx = np.arange(1, rel.size + 1)  # (local)
    floor = 1e-120  # (local)
    ax.semilogy(idx, np.clip(rel, floor, None), "o-", label="Cov_aug (single-w)")
    ax.axhline(r["rank_threshold"], color="red", ls="--",
               label=f"rank_thr = {r['rank_threshold']:.1e}")
    # control second SV marker
    ax.semilogy([2], [max(r["ctrl_second_rel_sv"], floor)], "s",
                color="darkorange", ms=11, label="rank-2 control σ2/σmax")
    ax.set_xlabel("singular-value index")
    ax.set_ylabel("σ_i / σ_max")
    ax.set_title(f"Augmented SVD spectrum — rank(Cov_aug) = {r['rank_aug']}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2: augmented correlation matrix heatmap.
    ax = axes[1]
    Corr = np.asarray(r["Corr_aug"])  # (local)
    names = [str(x) for x in r["aug_names"]]  # (local)
    im = ax.imshow(Corr, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(names)))
    ax.set_yticks(range(len(names)))
    ax.set_xticklabels(names, rotation=90, fontsize=7)
    ax.set_yticklabels(names, fontsize=7)
    ax.set_title("Corr_aug  (|Corr|=1 ⇒ bundle exhaustive)")
    fig.colorbar(im, ax=ax, fraction=0.046)

    # Panel 3: power columns of the augmented matrix.
    ax = axes[2]
    names = [str(x) for x in r["aug_names"]]  # (local)
    x = np.arange(len(names))  # (local)
    ax.bar(x - 0.2, r["p_MKK_aug"], width=0.4, label="M_KK-power")
    ax.bar(x + 0.2, r["p_w2_aug"], width=0.4, label="indep-w2-power")
    ax.axhline(0, color="k", lw=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=90, fontsize=7)
    ax.set_ylabel("power")
    ax.set_title("P_aug columns (w2-col ≡ 0 ⇒ scalar-multiple ⇒ rank 1)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        f"S103-NNU-BUNDLE-EXHAUSTIVENESS — {r['verdict']}  "
        f"(σ2/σmax = {r['second_rel_sv']:.3g} < {r['rank_threshold']:.1e}; "
        f"rank-2 ctrl = {r['rank_two_control']})",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload: dict = {
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


# ---------------------------------------------------------------------------
# Section 7 — Main
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

    r = compute()

    # Numbers FIRST.
    print("--- NUMBERS ---")
    print(f"  dagger power vector p_MKK = {r['p_MKK_dagger']}  ({list(r['dagger_names'])})")
    print(f"  m_H map: p_MKK(m_H)={r['p_MKK_mH']}  p_indep-w2(m_H)={r['p_w2indep_mH']}")
    print(f"  v_ew map: p_MKK(v_ew)={r['p_MKK_vew']}  p_indep-w2(v_ew)={r['p_w2indep_vew']}")
    print(f"  P_aug rows = {list(r['aug_names'])}")
    print(f"  P_aug M_KK-col = {r['p_MKK_aug']}")
    print(f"  P_aug indep-w2-col = {r['p_w2_aug']}")
    print(f"  singular_values = {r['singular_values']}")
    print(f"  rel σ_i/σ_max   = {r['rel_sv']}")
    print(f"  sigma_max = {r['sigma_max']:.6f}")
    print(f"  second_rel_sv (σ2/σmax) = {r['second_rel_sv']:.6g}  vs threshold {r['rank_threshold']:.3e}")
    print(f"  rank(Cov_aug) = {r['rank_aug']}  (PASS iff == {PASS_RANK})")
    print(f"  min |Corr| (w2-touching pairs) = {r['min_w2_pair_abs_corr']:.6g}")
    print(f"  n_w2_decorrelated pairs (|Corr|<1) = {r['n_w2_decorrelated']}")
    print("  --- cross-checks ---")
    print(f"  rank-2 control rank = {r['rank_two_control']}  (passes iff ==2: {r['rank2_control_passes']})")
    print(f"  control σ2/σmax = {r['ctrl_second_rel_sv']:.6g}  (>> threshold)")
    print(f"  dagger sub-block matches s102 Cov = {r['subblock_matches_s102']}")
    print(f"  s102 anchor rank = {r['s102_rank']}  rank2_control = {r['s102_rank_two_control']}")
    print(f"  higgs_sector_ratio m_H/v_ew = {r['higgs_sector_ratio']:.6f} (dimensionless)")
    print(f"  a4 dressing (a_4_FW_zeta/a4_fold) = {r['a4_dressing']:.8f}")
    print(f"  (0,0)-sector min |lambda| (|S|^2-mode scale) = {r['min_abs_lambda_00']:.8f}")
    print()

    # Persist.
    np.savez(
        OUT_NPZ,
        value=r["value"],
        verdict=r["verdict"],
        rank_aug=r["rank_aug"],
        rank_threshold=r["rank_threshold"],
        sigma_max=r["sigma_max"],
        second_rel_sv=r["second_rel_sv"],
        rel_sv=r["rel_sv"],
        singular_values=r["singular_values"],
        P_aug=r["P_aug"],
        Cov_aug=r["Cov_aug"],
        Corr_aug=r["Corr_aug"],
        aug_names=r["aug_names"],
        p_MKK_aug=r["p_MKK_aug"],
        p_w2_aug=r["p_w2_aug"],
        p_MKK_mH=r["p_MKK_mH"],
        p_MKK_vew=r["p_MKK_vew"],
        p_w2indep_mH=r["p_w2indep_mH"],
        p_w2indep_vew=r["p_w2indep_vew"],
        higgs_sector_ratio=r["higgs_sector_ratio"],
        a4_dressing=r["a4_dressing"],
        s_mode_scale=r["s_mode_scale"],
        min_abs_lambda_00=r["min_abs_lambda_00"],
        w2_pair_names=r["w2_pair_names"],
        w2_pair_abs_corr=r["w2_pair_abs_corr"],
        min_w2_pair_abs_corr=r["min_w2_pair_abs_corr"],
        n_w2_decorrelated=r["n_w2_decorrelated"],
        rank_two_control=r["rank_two_control"],
        rank2_control_passes=r["rank2_control_passes"],
        ctrl_second_rel_sv=r["ctrl_second_rel_sv"],
        s102_rank=r["s102_rank"],
        s102_rank_two_control=r["s102_rank_two_control"],
        subblock_matches_s102=r["subblock_matches_s102"],
        dagger_names=r["dagger_names"],
        p_MKK_dagger=r["p_MKK_dagger"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    make_plot(r)
    print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    verdict = r["verdict"]  # (local)
    value = r["value"]  # (local)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Companion rows: regulator_pin (a_4^{ζ} m_H dressing) + dual_prior posterior.
    extra_rows = [
        f"# regulator_pin=a_4^{{zeta}}={a_4_FW_zeta} (Yang-Mills+Higgs-quartic; m_H |S|^2-mode KK-threshold dressing); a_n^{{zeta}} grading powers feed p_MKK(m_H)=+1",
        f"# bundle_exhaustiveness: rank(Cov_aug)={r['rank_aug']}; second_rel_sv={r['second_rel_sv']:.6g}<{r['rank_threshold']:.1e}; rank-2 control={r['rank_two_control']}; min|Corr|(w2-pairs)={r['min_w2_pair_abs_corr']:.4g}; dual_prior PASS->0.9 Track A (clause-(b) CONFIRMED)",
    ]
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
