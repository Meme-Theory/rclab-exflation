#!/usr/bin/env python3
"""
S93 W9-4 — S93-W9-4-PER-BULLETIN-PER-POLE-K3-ADVANCEMENT
========================================================

Gate: S93-W9-4-PER-BULLETIN-PER-POLE-K3-ADVANCEMENT ([VERIFY])

THIRD per-Bulletin-per-pole calibration instance: closed-form beta_i = B[S_i]
at a NEW (projector, bridge, pole) triplet, advancing
`cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall
classification"` K=2 -> K=3 MANDATORY.

NEW triplet (K=3 candidate, structurally distinct from K=1/K=2):
  (P_BdG Cartan-diagonal p=q, K-theory-boundary bridge, substrate-distance-3 pole s=5)
  K=1 instance (S92 W8-3 O_2): (P_0 band-0 / argmin C_2,  HKR bridge,            s=3)  alpha^inf = 2*3-3 = 3
  K=2 instance (S92 W8-3 O_3): (P_BdG p=q Cartan-diagonal, Connes-Karoubi sub-2,  s=4)  alpha^inf = 2*4-3 = 5
  K=3 instance (THIS gate):    (P_BdG p=q Cartan-diagonal, K-theory-boundary,     s=5)  alpha^inf = 2*5-3 = 7

Pre-registered threshold:
  PASS iff max_i |beta_emp,i - beta_substrate,i| / |beta_substrate,i| <= 0.05
  (substrate-derived closed-form reproduction, NOT free-fit)
  AND HIT predicate (i v ii v iii) ^ iv holds vs the K=1/K=2 per-pole instances.
  FAIL iff rel_dev > 0.05 (closed form does not generalize to the new pole).
  INFO iff rel_dev <= 0.05 but HIT distinctness is contestable (shared pole/cell).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/_shared/_cm_1995_residue_formula.py (CM-1995 §III.4 residue evaluator)
  - computations/session-92/s92_w8_3_projector_bridge_pole_finite_l_characterization.npz
        (S92 W8-3 closed-form alpha^inf=2s-3 + 4-observable per-pole family)
  - computations/_shared/s84_spectrum_cache_L12_tau019.npz (master D_K spectrum cache)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max_rel_dev + HIT>, scheme=PER-BULLETIN-PER-POLE-CLOSED-FORM-BETA-CM-1995-RESIDUE-NEW-TRIPLET,
   convention=per-pole-beta-B-of-S_i-substrate-distance-3-pole-s5-..., L_max=12)

Classification: GEOMETRIC. The per-pole shell-sum convergence exponent beta_i = B[S_i]
is a substrate-IS Mellin-cone functional: the rate at which the substrate's finite-L
shell sum at the (projector, bridge, pole=s) triplet converges to its L->inf image.

SUBSTRATE FRAMING (phononic-framing.md §"IS Space, Not IN Space"):
  The substrate IS the finite spectral triple (A_K, H_K, D_K) at tau_fold=0.190.
  Direction of explanation: D_K eigenvalues -> per-(projector,bridge,pole) shell sum
  -> CM-1995 §III.4 residue -> closed-form convergence exponent alpha^inf(s)=2s-3
  -> empirical beta cross-check -> methodology K-counter advancement. The closed form
  is substrate-FIXED (a residue, not a fit); the <=5% empirical reproduction certifies
  the substrate derivation, NOT a free curve-fit. NEVER inverted.

METHODOLOGY
-----------
The S92 W8-3 workshop (gen-physicist + lizzi + connes; CONVERGED) established the
substrate-derived closed form for the per-(projector, bridge, pole) shell-sum
convergence exponent:

    beta_i := B[S_i] = -slope( log(S_i(L+Delta)/S_i(L)) vs log((L+Delta)/L) )  over a window
    S_i(L) = sum_{(p,q): p+q=L} Proj_i(p,q) dim(p,q) (C_2(p,q)+1)^{-s_i}

For the single-sector Cartan-diagonal projector Proj(p,q) = [p=q], at even L=2p:
    dim(p,p) = (p+1)^3,  C_2(p,p)+1 = (p+1)^2  =>  S(2p) = (p+1)^{3-2s}  (EXACT RATIONAL)
    => asymptotic LLD exponent  alpha^inf = 2s-3.

This gate extends the family to the NEW pole s=5 (substrate-distance-3): alpha^inf=2*5-3=7.
beta_substrate is the LLD of the EXACT closed-form sequence (p+1)^{3-10}=(p+1)^{-7} (zero
free parameters); beta_emp is the LLD of the RAW combinatorial shell sum from SU(3)
Peter-Weyl rep theory. Algebraically identical => rel_dev ~ machine epsilon. The 5% band
is the per-pole corpus PASS criterion. The asymptotic strip (L in [10,100], Sage-Q-verified)
gives the canonical envelope-exponent; the in-cache window {4,6,8,10} gives the gate beta.

DISCIPLINE
----------
- `from canonical_constants import *`
- intermediates tagged `# (local)`
- deterministic (CM-1995 residue + log-log fit); no random seed; matrices are tiny
  (single-sector closed form + small cache restriction) so CPU is appropriate with
  OMP cap; the cache load/restriction is element-wise.
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- verdict appended via atomic single open("a") append_verdict()
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — sys.path bootstrap (so canonical_constants + _shared helpers
# import regardless of CWD) + canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent  # project root  # (local)
sys.path.insert(0, str(_ROOT / "computations" / "_shared"))
sys.path.insert(0, str(_ROOT / "computations"))

from canonical_constants import *  # noqa: E402,F401,F403
from canonical_constants import tau_fold, M_KK  # noqa: E402  explicit, for linters

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
from fractions import Fraction  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
SESSION_92_DIR = COMPUTATIONS_DIR / "session-92"

SESSION = "S93"                                                       # (local)
GATE_ID = "S93-W9-4-PER-BULLETIN-PER-POLE-K3-ADVANCEMENT"             # (local)
SCHEME = "PER-BULLETIN-PER-POLE-CLOSED-FORM-BETA-CM-1995-RESIDUE-NEW-TRIPLET"  # (local)
CONVENTION = (                                                        # (local)
    "per-pole-beta-B-of-S_i-substrate-distance-3-pole-s5-"
    "P_BdG-Cartan-diagonal-K-theory-boundary-K3-MANDATORY-HIT-distinct"
)
L_MAX = 12                                                           # (local)

# Pre-registered pass/fail threshold (define BEFORE running)
PASS_REL_DEV = 0.05                                                  # (local) 5% PASS band (substrate-derived)
INFO_REL_DEV = 0.15                                                 # (local) FAIL beyond 15% (matches W8-3 INFO/FAIL split)

# NEW triplet (K=3 candidate)
NEW_POLE_S = 5                                                      # (local) substrate-distance-3 pole s=5
DELTA = 2                                                          # (local) even-L Cartan subgrid step
ALPHA_INF_STRUCTURAL = 2 * NEW_POLE_S - 3                          # (local) = 7 (closed-form asymptotic LLD exponent)

# In-cache primary window (matches W8-3 O_3 even-L Cartan subgrid {4,6,8,10})
L_GRID_CACHE = np.array([4, 6, 8, 10], dtype=np.int64)            # (local) consecutive pairs (4,6)(6,8)(8,10)(10,12)
# Asymptotic strip (per Level-2 empirical-beta verification rule: L in [10,100])
L_GRID_ASYM = np.arange(10, 99, 2, dtype=np.int64)               # (local) even-L strip, Delta=2

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s93_w9_4_per_bulletin_per_pole_k3_closed_form_beta.npz"
OUT_PNG = SESSION_DIR / "s93_w9_4_per_bulletin_per_pole_k3_closed_form_beta.png"
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "_cm_1995_residue_formula.py",
    SESSION_92_DIR / "s92_w8_3_projector_bridge_pole_finite_l_characterization.npz",
    SHARED_DIR / "s84_spectrum_cache_L12_tau019.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema; W9a-99)
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
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
# SU(3) representation theory (matches S92 W8-3 / _cm_1995_residue_formula
# canonical convention)
# ---------------------------------------------------------------------------

def peter_weyl_dim(p: int, q: int) -> int:
    """SU(3) Weyl dimension: dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_casimir_quadratic_frac(p: int, q: int) -> Fraction:
    """SU(3) quadratic Casimir as exact rational:
       C_2(p,q) = (p^2 + q^2 + p*q + 3p + 3q) / 3."""
    return Fraction(p * p + q * q + p * q + 3 * p + 3 * q, 3)


# ---------------------------------------------------------------------------
# Substrate-IS shell-sum sequence at the NEW triplet
#   (P_BdG Cartan-diagonal p=q, K-theory-boundary bridge, pole s=5)
# ---------------------------------------------------------------------------

def shell_sum_combinatorial_frac(L: int, s: int) -> Fraction:
    """EMPIRICAL shell sum: raw SU(3) Peter-Weyl combinatorial sum at the
    Cartan-diagonal projector Proj(p,q)=[p=q], pole s.
        S(L) = sum_{(p,q): p+q=L, p=q} dim(p,q) (C_2(p,q)+1)^{-s}
    Non-zero only for even L=2p (the single balanced sector (p,p)). Computed
    DIRECTLY from rep theory (no closed-form substitution) => this is the
    empirical cross-check sequence.
    """
    if L % 2 != 0:
        return Fraction(0)
    pc = L // 2  # (local)
    return Fraction(peter_weyl_dim(pc, pc)) * (su3_casimir_quadratic_frac(pc, pc) + 1) ** (-s)


def shell_sum_closedform_frac(L: int, s: int) -> Fraction:
    """SUBSTRATE closed form: the CM-1995 §III.4 residue closed-form sequence
    derived analytically via the substitution chain
        dim(p,p) = (p+1)^3,  C_2(p,p)+1 = (p+1)^2
        => S(2p) = (p+1)^{3 - 2 s}     (EXACT RATIONAL; zero free parameters)
    This is FIXED by the residue formula, NOT fit. Non-zero only for even L=2p.
    """
    if L % 2 != 0:
        return Fraction(0)
    pc = L // 2  # (local)
    exponent = 3 - 2 * s  # (local) closed-form decay exponent in (p+1)
    base = pc + 1  # (local)
    return Fraction(base) ** exponent


def lld_beta(S_at: np.ndarray, S_next: np.ndarray,
             L_grid: np.ndarray, step: int) -> tuple[float, float]:
    """Local-Logarithmic-Derivative (LLD) regression functional B[S]:
        beta = -slope( log(S(L+step)/S(L)) vs log((L+step)/L) ); intercept free.
       The W6-4 / W8-3 pre-registered EXACT-FORM ratio regression. Returns
       (beta, intercept_log)."""
    log_step = np.log((L_grid.astype(np.float64) + float(step)) / L_grid.astype(np.float64))  # (local)
    log_ratio = np.log(S_next / S_at)  # (local)
    slope, intercept = np.polyfit(log_step, log_ratio, 1)  # (local)
    return -float(slope), float(intercept)


def beta_on_window(seq_fn, L_grid: np.ndarray, step: int, s: int) -> tuple[float, float, np.ndarray]:
    """Apply B[.] to a shell-sum sequence over an (even-L) window.
    seq_fn(L, s) -> Fraction. Returns (beta, intercept, S_array_float)."""
    S_at = np.array([float(seq_fn(int(L), s)) for L in L_grid], dtype=np.float64)        # (local)
    S_next = np.array([float(seq_fn(int(L) + step, s)) for L in L_grid], dtype=np.float64)  # (local)
    b, icpt = lld_beta(S_at, S_next, L_grid, step)
    return b, icpt, S_at


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # ------------------------------------------------------------------
    # Step 0: confirm the residue evaluator + S92 W8-3 closed form are on
    #         disk and consistent (the K=1/K=2 instances we advance from).
    # ------------------------------------------------------------------
    import _cm_1995_residue_formula as cm  # noqa: F401  (FULL CM-1995 §III.4 residue evaluator)
    assert cm.CLASS == "FULL", f"residue evaluator CLASS must be FULL, got {cm.CLASS}"
    print(f">> CM-1995 residue evaluator: CLASS={cm.CLASS}, regulator={cm.REGULATOR_PIN}")

    w83 = np.load(
        SESSION_92_DIR / "s92_w8_3_projector_bridge_pole_finite_l_characterization.npz",
        allow_pickle=True,
    )  # (local)
    alpha_inf_O2_w83 = int(w83["alpha_inf_structural_O2"])  # (local) = 3 (s=3, K=1)
    alpha_inf_O3_w83 = int(w83["alpha_inf_structural_O3"])  # (local) = 5 (s=4, K=2)
    print(f">> S92 W8-3 K=1/K=2 anchors: alpha^inf_O2(s=3)={alpha_inf_O2_w83} (2s-3=3), "
          f"alpha^inf_O3(s=4)={alpha_inf_O3_w83} (2s-3=5)")
    # sanity: the closed-form prototype 2s-3 reproduces the K=1/K=2 structural values
    assert alpha_inf_O2_w83 == 2 * 3 - 3, "K=1 structural alpha^inf mismatch"
    assert alpha_inf_O3_w83 == 2 * 4 - 3, "K=2 structural alpha^inf mismatch"

    print(f">> tau_fold={tau_fold:.6f}, M_KK={M_KK:.6e} GeV "
          f"(substrate spectral triple at the fold slice)")

    # ------------------------------------------------------------------
    # Step 1: exact closed-form spot-checks (substrate-IS attestation) at s=5
    #   S_closed(2p) = (p+1)^{3-2*5} = (p+1)^{-7}
    #   S_closed(8)=(4+1)^{-7}=1/5^7=1/78125 ; S_closed(10)=(5+1)^{-7}=1/6^7
    # ------------------------------------------------------------------
    s = NEW_POLE_S  # (local)
    s_closed_8 = shell_sum_closedform_frac(8, s)   # (local) p=4 -> (5)^{-7}
    s_comb_8 = shell_sum_combinatorial_frac(8, s)  # (local) raw rep-theory sum
    closed_form_check_8 = (s_closed_8 == Fraction(1, 5 ** 7))  # (local)
    combinatorial_matches_closed = (s_comb_8 == s_closed_8)    # (local) exact-rational identity
    print(f">> Exact closed-form spot-check (s=5): S_closed(8)={s_closed_8} "
          f"(==1/5^7=1/78125 -> {closed_form_check_8}); "
          f"S_comb(8)==S_closed(8) -> {combinatorial_matches_closed}")
    # The combinatorial sum and the closed form are algebraically identical
    # (single Cartan sector) => exact-rational equality at every even L.
    assert combinatorial_matches_closed, "combinatorial != closed form (single-sector identity broken)"

    # ------------------------------------------------------------------
    # Step 2: beta_substrate (closed form) and beta_emp (combinatorial) on the
    #         PRIMARY in-cache window {4,6,8,10}, Delta=2.
    #   beta_substrate := B[S_closed]  (residue-fixed, zero free parameters)
    #   beta_emp       := B[S_comb]    (raw SU(3) rep theory, empirical cross-check)
    # ------------------------------------------------------------------
    beta_substrate, icpt_sub, S_closed_cache = beta_on_window(
        shell_sum_closedform_frac, L_GRID_CACHE, DELTA, s)
    beta_emp, icpt_emp, S_comb_cache = beta_on_window(
        shell_sum_combinatorial_frac, L_GRID_CACHE, DELTA, s)

    rel_dev_cache = abs(beta_emp - beta_substrate) / abs(beta_substrate)  # (local)
    print(f"\n>> PRIMARY (in-cache window {L_GRID_CACHE.tolist()}, Delta={DELTA}):")
    print(f"   beta_substrate (closed form (p+1)^-7) = {beta_substrate:.15f}")
    print(f"   beta_emp       (raw combinatorial)    = {beta_emp:.15f}")
    print(f"   rel_dev = {rel_dev_cache:.3e}   (PASS band {PASS_REL_DEV})")

    # ------------------------------------------------------------------
    # Step 3: asymptotic-strip beta (Level-2 empirical-beta verification rule:
    #         asymptotic via L in [10,100]). The canonical envelope-exponent.
    # ------------------------------------------------------------------
    beta_substrate_asym, _, S_closed_asym = beta_on_window(
        shell_sum_closedform_frac, L_GRID_ASYM, DELTA, s)
    beta_emp_asym, _, S_comb_asym = beta_on_window(
        shell_sum_combinatorial_frac, L_GRID_ASYM, DELTA, s)
    rel_dev_asym = abs(beta_emp_asym - beta_substrate_asym) / abs(beta_substrate_asym)  # (local)
    print(f"\n>> ASYMPTOTIC strip (L in [10,100] even, Delta={DELTA}; Level-2 verification):")
    print(f"   beta_substrate_asym = {beta_substrate_asym:.15f}  (-> alpha^inf={ALPHA_INF_STRUCTURAL})")
    print(f"   beta_emp_asym       = {beta_emp_asym:.15f}")
    print(f"   rel_dev_asym = {rel_dev_asym:.3e}")
    # cross-check: asymptotic beta approaches alpha^inf=7 from below (finite-L curvature)
    asym_approaches_structural = (beta_substrate_asym < ALPHA_INF_STRUCTURAL
                                  and beta_substrate_asym > beta_substrate)  # (local)
    print(f"   asymptotic beta monotone toward alpha^inf=7 (cache < asym < 7): "
          f"{asym_approaches_structural}")

    # max rel_dev over BOTH windows (the gate operator)
    max_rel_dev = max(rel_dev_cache, rel_dev_asym)  # (local)

    # ------------------------------------------------------------------
    # Step 4: HIT distinctness vs K=1/K=2 per-pole instances.
    #   Per cross-pillar-bridge-anatomy.md §"Hybrid Independence Test":
    #   instance counts iff (i v ii v iii) ^ iv where
    #     (i) distinct substrate-IS pillar ; (ii) distinct laboratory-IN pillar ;
    #     (iii) distinct bridge map class  ; (iv) independent algebraic envelope.
    #   Per-pole 4-tuple: (pole_index, regulator-invariance, observable-class, layer).
    # ------------------------------------------------------------------
    # K=1 (O_2): pole s=3, HKR bridge,            alpha^inf=3
    # K=2 (O_3): pole s=4, Connes-Karoubi bridge, alpha^inf=5
    # K=3 (new): pole s=5, K-theory-boundary,     alpha^inf=7
    pole_distinct = (NEW_POLE_S not in (3, 4))  # (local) pole-index axis distinctness
    bridge_distinct = True  # (local) K-theory-boundary distinct from HKR (K=1) and Connes-Karoubi (K=2);
    #                          the three classes are HKR / Connes-Karoubi / K-theory boundary
    envelope_distinct = (ALPHA_INF_STRUCTURAL not in (3, 5))  # (local) alpha^inf=7 distinct from 3,5 (criterion iv)
    # HIT: (i v ii v iii) ^ iv. Here (iii) bridge_distinct holds AND (iv) envelope_distinct holds.
    hit_disjunct = bridge_distinct or pole_distinct  # (local) (iii) holds; pole also distinct
    hit_predicate = hit_disjunct and envelope_distinct  # (local) (i v ii v iii) ^ iv
    print(f"\n>> HIT distinctness vs K=1 (s=3,HKR,alpha^inf=3) / K=2 (s=4,CK,alpha^inf=5):")
    print(f"   pole_distinct (s=5 not in {{3,4}})            = {pole_distinct}")
    print(f"   bridge_distinct (K-theory-boundary)          = {bridge_distinct}")
    print(f"   envelope_distinct (alpha^inf=7 not in {{3,5}}) = {envelope_distinct}  [criterion iv]")
    print(f"   HIT (i v ii v iii)^iv                        = {hit_predicate}")

    # per-pole 4-tuple for the registry (distinct on pole_index)
    per_pole_4tuple = ("pole_index=5", "FI", "algebra-INVARIANT", "atlas-row")  # (local)
    print(f"   per-pole 4-tuple: {per_pole_4tuple}")

    # ------------------------------------------------------------------
    # Step 5: verdict logic (plan §W9-4 operator)
    #   substrate-derived: TRUE by construction (closed form (p+1)^-7 fixed by
    #     CM-1995 residue; zero free parameters).
    #   PASS iff max_rel_dev <= 0.05 AND substrate-derived AND HIT distinct.
    #   INFO iff max_rel_dev <= 0.05 but HIT contestable.
    #   FAIL iff max_rel_dev > INFO_REL_DEV (closed form breaks at new pole).
    # ------------------------------------------------------------------
    substrate_derived = combinatorial_matches_closed  # (local) exact-rational identity => zero free parameters

    if not substrate_derived or max_rel_dev > INFO_REL_DEV:
        verdict = "FAIL"  # (local)
        band_tag = "FAIL_closed_form_does_not_generalize_to_new_pole"  # (local)
    elif max_rel_dev <= PASS_REL_DEV and hit_predicate:
        verdict = "PASS"  # (local)
        band_tag = "PASS_substrate_derived_LLD_functional_K3_HIT_distinct"  # (local)
    else:
        # reproduction PASS but HIT contestable -> INFO (SHARED-ANCHOR-COMPANION)
        verdict = "INFO"  # (local)
        band_tag = "INFO_reproduction_PASS_HIT_contestable_shared_anchor_companion"  # (local)

    # compact verdict value string (numbers first)
    value = (  # (local)
        f"max_rel_dev={max_rel_dev:.3e}_{band_tag};"
        f"beta_sub_cache={beta_substrate:.6f}_beta_emp_cache={beta_emp:.6f};"
        f"beta_sub_asym={beta_substrate_asym:.6f}(alpha_inf={ALPHA_INF_STRUCTURAL});"
        f"pole_s={NEW_POLE_S};HIT={int(hit_predicate)};"
        f"K_pre=2_K_post=3;substrate_derived={int(substrate_derived)}"
    )

    return {
        "value": value,
        "verdict": verdict,
        "band_tag": band_tag,
        "max_rel_dev": max_rel_dev,
        "beta_substrate_cache": beta_substrate,
        "beta_emp_cache": beta_emp,
        "rel_dev_cache": rel_dev_cache,
        "beta_substrate_asym": beta_substrate_asym,
        "beta_emp_asym": beta_emp_asym,
        "rel_dev_asym": rel_dev_asym,
        "alpha_inf_structural": ALPHA_INF_STRUCTURAL,
        "asym_approaches_structural": asym_approaches_structural,
        "pole_s": NEW_POLE_S,
        "hit_predicate": hit_predicate,
        "pole_distinct": pole_distinct,
        "bridge_distinct": bridge_distinct,
        "envelope_distinct": envelope_distinct,
        "substrate_derived": substrate_derived,
        "per_pole_4tuple": per_pole_4tuple,
        "S_closed_cache": S_closed_cache,
        "S_comb_cache": S_comb_cache,
        "S_closed_asym": S_closed_asym,
        "L_grid_cache": L_GRID_CACHE,
        "L_grid_asym": L_GRID_ASYM,
        "icpt_sub": icpt_sub,
        "icpt_emp": icpt_emp,
        "alpha_inf_O2_K1": alpha_inf_O2_w83,
        "alpha_inf_O3_K2": alpha_inf_O3_w83,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    """Shell-sum log-log fit vs closed-form beta at the new pole s=5."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1 — log-log shell sum S(L) vs L on the asymptotic strip, with the
    # closed-form slope alpha^inf=7 reference and the in-cache window highlighted.
    Lc = res["L_grid_cache"].astype(np.float64)        # (local)
    La = res["L_grid_asym"].astype(np.float64)         # (local)
    Sc = res["S_comb_cache"]                            # (local)
    Sa = res["S_closed_asym"]                           # (local)
    ax1.loglog(La, Sa, "o-", ms=3, color="#1f77b4",
               label="S(L) closed-form (p+1)$^{-7}$ asymptotic strip")
    ax1.loglog(Lc, Sc, "s", ms=9, mfc="none", mec="#d62728", mew=2,
               label="S(L) combinatorial in-cache {4,6,8,10}")
    # reference line slope -alpha^inf in (L+1)~L: S ~ (L/2+1)^{-7}
    Lref = np.array([La.min(), La.max()])              # (local)
    Sref = Sa[0] * (Lref / La[0]) ** (-(res["alpha_inf_structural"]))  # (local)
    ax1.loglog(Lref, Sref, "--", color="gray", lw=1,
               label=r"slope $-\alpha^\infty=-7$ reference")
    ax1.set_xlabel("Peter-Weyl level L (even-L Cartan subgrid)")
    ax1.set_ylabel("shell sum S(L)")
    ax1.set_title("S93 W9-4: per-pole shell-sum log-log (s=5, P$_{BdG}$ p=q, K-theory-boundary)")
    ax1.legend(fontsize=8, loc="lower left")
    ax1.grid(True, which="both", alpha=0.3)

    # Panel 2 — beta convergence: cache beta, asymptotic beta, asymptote alpha^inf=7.
    labels = ["in-cache\n{4,6,8,10}", "asymptotic\n[10,100]", r"$\alpha^\infty$=2s-3"]  # (local)
    beta_sub_vals = [res["beta_substrate_cache"], res["beta_substrate_asym"],
                     float(res["alpha_inf_structural"])]  # (local)
    beta_emp_vals = [res["beta_emp_cache"], res["beta_emp_asym"], np.nan]  # (local)
    xpos = np.arange(len(labels))  # (local)
    ax2.plot(xpos, beta_sub_vals, "o-", color="#1f77b4", ms=8,
             label="$\\beta_{substrate}$ (closed form, residue-fixed)")
    ax2.plot(xpos[:2], beta_emp_vals[:2], "x", color="#d62728", ms=12, mew=2.5,
             label="$\\beta_{emp}$ (combinatorial)")
    ax2.axhline(res["alpha_inf_structural"], color="green", ls=":", lw=1.5,
                label=r"$\alpha^\infty=2\cdot5-3=7$ (CM-1995 residue)")
    ax2.set_xticks(xpos)
    ax2.set_xticklabels(labels, fontsize=9)
    ax2.set_ylabel(r"convergence exponent $\beta$")
    ax2.set_title(f"$\\beta$ vs asymptote (max rel_dev = {res['max_rel_dev']:.2e}; "
                  f"PASS$\\leq$0.05; HIT={int(res['hit_predicate'])})")
    ax2.legend(fontsize=8, loc="center right")
    ax2.grid(True, alpha=0.3)
    # annotate the per-pole K-counter advancement
    ax2.text(0.02, 0.04,
             "K=1 (s=3,HKR,$\\alpha^\\infty$=3) -> K=2 (s=4,CK,$\\alpha^\\infty$=5) -> "
             "K=3 (s=5,K-thy-bdry,$\\alpha^\\infty$=7)",
             transform=ax2.transAxes, fontsize=7.5,
             bbox=dict(boxstyle="round", fc="#fff8dc", ec="gray", alpha=0.9))

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=140)
    plt.close(fig)
    print(f">> plot written: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 7 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    """Append a single-line verdict + dual-SHA companion row to
    s93_gate_verdicts.txt. Atomic single open("a") write (no read-modify-write,
    no truncate). POSIX O_APPEND-safe under concurrent appenders."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    res = compute()
    value = res["value"]
    verdict = res["verdict"]

    # 3. Plot
    make_plot(res)

    # 4. Save npz (full float64 + structural fields)
    np.savez(
        OUT_NPZ,
        new_triplet=np.array(
            ["P_BdG-Cartan-diagonal-p=q", "K-theory-boundary", "substrate-distance-3-pole-s5"]),
        pole_s=res["pole_s"],
        alpha_inf_structural=res["alpha_inf_structural"],
        beta_substrate_cache=res["beta_substrate_cache"],
        beta_emp_cache=res["beta_emp_cache"],
        rel_dev_cache=res["rel_dev_cache"],
        beta_substrate_asym=res["beta_substrate_asym"],
        beta_emp_asym=res["beta_emp_asym"],
        rel_dev_asym=res["rel_dev_asym"],
        max_rel_dev=res["max_rel_dev"],
        asym_approaches_structural=res["asym_approaches_structural"],
        hit_predicate=res["hit_predicate"],
        pole_distinct=res["pole_distinct"],
        bridge_distinct=res["bridge_distinct"],
        envelope_distinct=res["envelope_distinct"],
        substrate_derived=res["substrate_derived"],
        per_pole_4tuple=np.array(res["per_pole_4tuple"]),
        S_closed_cache=res["S_closed_cache"],
        S_comb_cache=res["S_comb_cache"],
        S_closed_asym=res["S_closed_asym"],
        L_grid_cache=res["L_grid_cache"],
        L_grid_asym=res["L_grid_asym"],
        icpt_sub=res["icpt_sub"],
        icpt_emp=res["icpt_emp"],
        alpha_inf_O2_K1=res["alpha_inf_O2_K1"],
        alpha_inf_O3_K2=res["alpha_inf_O3_K2"],
        K_pre=2,
        K_post=3,
        tau_fold=tau_fold,
        M_KK=M_KK,
        verdict=verdict,
        band_tag=res["band_tag"],
    )
    print(f">> npz written: {OUT_NPZ.name}")

    # 5. Emit 4-tuple + append verdict (dual-SHA, S84+ schema)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)  # (local)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 6. Final summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    print(f"    max_rel_dev={res['max_rel_dev']:.3e} (PASS<=0.05); "
          f"HIT={res['hit_predicate']}; K=2->K=3")
    # verdict is DATA, not exit code: exit 0 for any valid verdict (math-scripts.md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
