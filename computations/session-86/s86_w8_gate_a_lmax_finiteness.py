"""
S86 W-8 / GATE A: S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS
========================================================

Master gate of the cutoff_AL2010 atlas-cardinality determinant trio (W-8).
Tests whether `f_0 * Lambda(L_max)^4 * a_0(L_max)` admits a positive-alpha
scaling Lambda(L_max) = Lambda_0 * L_max^alpha (alpha in [-2, +2]) such that
the coupling is bounded as L_max -> infty on Jensen-deformed SU(3).

Per `sessions/framework/registry/cutoff-sqrt-adjudication.md` §3.1 + workshop
R3-C-E3-C, GATE A FAIL is structurally pre-determined by the substrate's
Peter-Weyl L^8 mode-count growth at d=8 spectral dimension. This S86
dispatch is canonical-record (logging the FAIL with input-pin closure-hash
for the permanent registry), NOT adjudication.

Substitution chain (per .claude/rules/math-scripts.md §Double-Check Logic
Before Compute):

  Step 1 (definitions):
    coupling g(L) := f_0 * Lambda(L)^4 * a_0(L)
    Lambda(L)    := Lambda_0 * L^alpha
    a_0(L)       := 16 * sum_{p+q<=L} [(p+1)(q+1)(p+q+2)/2]^2
                    [Peter-Weyl L^2(SU(3)) sum-of-dim^2 multiplicity;
                     leading term L^8/960 per workshop §1.5 Sage closed form]

  Step 2 (substitute):
    g(L) = f_0 * Lambda_0^4 * L^{4*alpha} * a_0(L)
    For boundedness as L -> infty:
      log g(L) = const + 4*alpha*log(L) + log a_0(L)
               = const + 4*alpha*log(L) + k_eff(L)*log(L) + O(1)
    where k_eff(L) := log(a_0(L)/a_0(L-1)) / log(L/(L-1)).

  Step 3 (simplify):
    Bounded limit requires 4*alpha + k_eff(L) -> 0 as L -> infty,
    i.e., alpha_star = -k_eff(L)/4.
    Asymptotic regime: a_0(L) ~ L^8/960 implies k_eff -> 8, alpha_star -> -2.

  Step 4 (direction):
    For L in {3, 5, 7, 10}, compute alpha_star(L) numerically.
    PASS test: exists alpha in [0, 2] with bounded limit.
    FAIL test: alpha_star < 0 for ALL L in scan -> no positive-alpha admissible.

PRDR machinery pin (per cutoff-sqrt-adjudication.md §3.1):
  - scheme           = peter-weyl-sum-of-dim2
  - convention       = cutoff_AL2010-canonical
  - L_max range      = {3, 5, 7, 10}  (PRDR-pinned discrete probe set)
  - alpha range      = [-2.0, +2.0] with step 0.05 (81 grid points)
  - cutoff_axis      = coherence
  - schema_version   = R3
  - GPU              = NONE (Sage symbolic + finite enumeration)
  - random seed      = N/A (deterministic)
  - OMP_NUM_THREADS  = 8

Trigger: [VERIFY]   Classification: GEOMETRIC (substrate Peter-Weyl spectrum)
Expected outcome: FAIL (pre-registered per R3-C-E3-C structural pre-determination)
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import hashlib
import json
import datetime
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# Project root resolution -----------------------------------------------------
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

ADJUDICATION_PATH = ROOT / "sessions" / "framework" / "cutoff-sqrt-adjudication.md"
W4_WP_PATH        = ROOT / "sessions" / "session-86" / "session-86-w4-workingpaper.md"
CONSTANTS_PATH    = ROOT / "computations" / "_shared" / "canonical_constants.py"
VERDICT_PATH      = ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID            = "S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS"
SCHEME             = "peter-weyl-sum-of-dim2"
CONVENTION         = "cutoff_AL2010-canonical"
L_MAX_TAG          = "{3,5,7,10}"
SCHEMA_VERSION     = "R3"
CUTOFF_AXIS        = "coherence"
TRIGGER            = "[VERIFY]"
CLASSIFICATION     = "GEOMETRIC"

# PRDR-pinned probe range
L_MAX_PROBE         = (3, 5, 7, 10)            # (local) PRDR pin from §3.1
ALPHA_MIN, ALPHA_MAX = -2.0, +2.0              # (local) gate scan window
ALPHA_STEP          = 0.05                     # (local) 81 grid points
PASS_BAND_ALPHA     = 0.0                      # (local) PASS requires alpha_star >= 0
PASS_RATIO_MAX      = 10.0                     # (local) bounded ratio g(L_max)/g(L_min) <= 10
FAIL_RATIO_MIN      = 100.0                    # (local) FAIL if ratio >= 100 (2 OOM divergence)
RTOL_BOUND          = 1e-12                    # (local) numerical tolerance for boundedness


# Discrete a_0(L_max) anchors from cutoff-sqrt-adjudication.md §3.1
A0_ANCHORS_EXPECTED = {                        # (local) PRDR-pinned anchors
    3:  12880,
    4:  50176,
    5:  159936,
    6:  439488,
    7:  1077120,
    8:  2410320,
    9:  5008432,
    10: 9785776,
}


def sha256_of_path(p: Path) -> str:
    """Return SHA-256 hex digest of file at p (full content, byte-exact)."""
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map) -> str:
    """SHA-256 of the canonicalized JSON-serialized ordered input-pin map.
    Per .claude/rules/v3-closure-recovery.md sig_5: audit_sha256 MUST be
    COMPUTED, not hardcoded."""
    canon = json.dumps(pin_map, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def a_0_peter_weyl(L_max: int) -> int:
    """Peter-Weyl L^2(SU(3)) sum-of-dim^2 multiplicity through Casimir level
    L_max. Each (p,q) irrep has dim d(p,q) = (p+1)(q+1)(p+q+2)/2; mode count
    is sum d^2 (each irrep contributes d copies in d-dimensional rep).
    Factor of 16 = 2 (two real components) x 8 (Clifford-8 spinor). Returns
    integer (anchors are integer per §3.1 enumeration)."""
    s = 0  # (local) Peter-Weyl accumulator over (p,q) with p+q <= L_max
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p + q <= L_max:
                d = (p + 1) * (q + 1) * (p + q + 2) // 2
                s += d * d
    return 16 * s


def k_eff_local(L: int, a0_L: int, a0_Lminus1: int) -> float:
    """Local effective polynomial growth k_eff(L) := log(a_0(L)/a_0(L-1))
    / log(L/(L-1)). Approaches 8 in the asymptotic regime (Peter-Weyl L^8
    leading)."""
    return float(np.log(a0_L / a0_Lminus1) / np.log(L / (L - 1.0)))


def alpha_star_root(k_eff: float) -> float:
    """Boundedness root: alpha_star = -k_eff/4. Bounded coupling exists at
    alpha = alpha_star; PASS test requires alpha_star >= 0."""
    return -k_eff / 4.0


def main() -> None:
    print(f"[start] {GATE_ID}")
    print(f"[start] timestamp = {datetime.datetime.now(datetime.timezone.utc).isoformat()}Z")
    print()

    # ---------------- SHA pinning of inputs (first 20 lines of stdout) -----
    adjudication_sha = sha256_of_path(ADJUDICATION_PATH)
    w4_wp_sha        = sha256_of_path(W4_WP_PATH)
    constants_sha    = sha256_of_path(CONSTANTS_PATH)

    print(f"[input-sha] cutoff-sqrt-adjudication.md   = {adjudication_sha}")
    print(f"[input-sha] session-86-w4-workingpaper.md = {w4_wp_sha}")
    print(f"[input-sha] canonical_constants.py        = {constants_sha}")
    print()

    # ---------------- Verify a_0(L_max) anchors -----------------------------
    print("[anchor] Verifying Peter-Weyl a_0(L_max) anchors against §3.1:")
    a0_actual: dict[int, int] = {}
    for L, expected in A0_ANCHORS_EXPECTED.items():
        a0 = a_0_peter_weyl(L)
        a0_actual[L] = a0
        match = (a0 == expected)
        print(f"          L_max={L}: a_0={a0} vs expected={expected} -> {'MATCH' if match else 'MISMATCH'}")
        if not match:
            print(f"[FATAL] a_0 anchor mismatch at L_max={L}; aborting.")
            sys.exit(2)
    print()

    # ---------------- Compute k_eff(L) and alpha_star(L) at probe points ---
    print("[scan] alpha_star(L) at PRDR-pinned probe points L in {3,5,7,10}:")
    print(f"       Substitution chain: a_0(L)=PW; k_eff(L)=d log a_0/d log L; alpha_star=-k_eff/4.")
    print(f"       Boundedness: 4*alpha + k_eff -> 0 as L -> infty.")
    print()
    print(f"       {'L_max':>6s}  {'a_0(L)':>12s}  {'a_0(L-1)':>12s}  {'k_eff(L)':>10s}  "
          f"{'alpha_star':>10s}  {'sign':>10s}")
    print(f"       {'-'*70}")
    k_eff_arr: dict[int, float] = {}
    alpha_star_arr: dict[int, float] = {}
    for L in L_MAX_PROBE:
        a0_L = a0_actual[L]
        a0_Lm1 = a_0_peter_weyl(L - 1)
        ke = k_eff_local(L, a0_L, a0_Lm1)
        a_star = alpha_star_root(ke)
        k_eff_arr[L] = ke
        alpha_star_arr[L] = a_star
        sign = "POSITIVE" if a_star >= 0 else "NEGATIVE"
        print(f"       {L:6d}  {a0_L:12d}  {a0_Lm1:12d}  {ke:10.6f}  {a_star:10.6f}  {sign:>10s}")
    print()

    # ---------------- Asymptotic check (Peter-Weyl L^8 leading) ------------
    L_top = max(L_MAX_PROBE)                     # (local) probe top end
    L_pre = max(L for L in L_MAX_PROBE if L < L_top)  # (local) probe one below top
    a0_top = a0_actual[L_top]
    a0_pre = a0_actual[L_pre]
    k_eff_asymptotic = float(np.log(a0_top / a0_pre) / np.log(L_top / L_pre))  # (local)
    alpha_star_asymptotic = -k_eff_asymptotic / 4.0                            # (local)
    print(f"[asymptotic] k_eff({L_pre}->{L_top}) = {k_eff_asymptotic:.6f}  (target: 8 as L->infty)")
    print(f"[asymptotic] alpha_star_asymptotic    = {alpha_star_asymptotic:.6f}  (target: -2)")
    print()

    # ---------------- alpha grid scan: find bounded alphas --------------------
    print("[grid] Scanning alpha in [{:.2f}, {:.2f}] step {:.3f}:".format(
        ALPHA_MIN, ALPHA_MAX, ALPHA_STEP))
    alphas = np.arange(ALPHA_MIN, ALPHA_MAX + ALPHA_STEP/2, ALPHA_STEP)  # (local) scan
    bounded_alphas: list[float] = []                                     # (local) accumulator
    for alpha in alphas:
        # g(L) = const * L^{4*alpha} * a_0(L)
        gvals = np.array([(L ** (4*alpha)) * a0_actual[L] for L in L_MAX_PROBE])
        ratio = float(gvals[-1] / gvals[0])                              # (local)
        log10_ratio = float(np.log10(abs(ratio)))                        # (local)
        if abs(log10_ratio) <= np.log10(PASS_RATIO_MAX):
            bounded_alphas.append(float(alpha))

    print(f"[grid] bounded_alphas (|log10 g(L_max)/g(L_min)| <= {np.log10(PASS_RATIO_MAX):.2f}): "
          f"{len(bounded_alphas)} of {len(alphas)} grid points")
    if bounded_alphas:
        print(f"[grid] bounded alpha range: [{min(bounded_alphas):.3f}, {max(bounded_alphas):.3f}]")
    print()

    # ---------------- PASS / FAIL / INFO decision ---------------------------
    # PASS: there exists alpha >= 0 in bounded_alphas (positive-alpha admits boundedness)
    # FAIL: ALL bounded alphas have alpha < 0 (no positive-alpha admissible)
    # INFO: ambiguous (subleading polynomial corrections non-canonical)
    has_nonnegative_bounded = any(a >= -1e-12 for a in bounded_alphas)
    all_alphastar_negative = all(alpha_star_arr[L] < -1e-12 for L in L_MAX_PROBE)

    print(f"[decision] has_nonnegative_bounded_alpha = {has_nonnegative_bounded}")
    print(f"[decision] all_alpha_star_negative       = {all_alphastar_negative}")
    print(f"[decision] alpha_star at L=3,5,7,10      = "
          f"[{alpha_star_arr[3]:.4f}, {alpha_star_arr[5]:.4f}, "
          f"{alpha_star_arr[7]:.4f}, {alpha_star_arr[10]:.4f}]")
    print()

    if has_nonnegative_bounded:
        verdict_word = "PASS"
        verdict_value = f"alpha_star_max={max(alpha_star_arr.values()):.4f}|bounded_pos_alpha=True"
    elif all_alphastar_negative:
        verdict_word = "FAIL"
        # Canonical FAIL value: report alpha_star range and asymptotic alpha
        verdict_value = (
            f"alpha_star_range=[{min(alpha_star_arr.values()):.4f},"
            f"{max(alpha_star_arr.values()):.4f}];"
            f"alpha_star_asymptotic={alpha_star_asymptotic:.4f};"
            f"k_eff_range=[{min(k_eff_arr.values()):.4f},{max(k_eff_arr.values()):.4f}];"
            f"k_eff_asymptotic={k_eff_asymptotic:.4f}"
        )
    else:
        verdict_word = "INFO"
        verdict_value = (
            f"alpha_star_range=[{min(alpha_star_arr.values()):.4f},"
            f"{max(alpha_star_arr.values()):.4f}];ambiguous_subleading"
        )

    print(f"[verdict] {verdict_word}")
    print(f"[verdict] value = {verdict_value}")
    print()

    # ---------------- Compute dual-SHA closure ------------------------------
    pin_map = {
        "gate_id":              GATE_ID,
        "trigger":              TRIGGER,
        "classification":       CLASSIFICATION,
        "scheme":               SCHEME,
        "convention":           CONVENTION,
        "L_max":                L_MAX_TAG,
        "schema_version":       SCHEMA_VERSION,
        "cutoff_axis":          CUTOFF_AXIS,
        "adjudication_path":    str(ADJUDICATION_PATH.relative_to(ROOT)).replace("\\", "/"),
        "adjudication_sha256":  adjudication_sha,
        "w4_wp_path":           str(W4_WP_PATH.relative_to(ROOT)).replace("\\", "/"),
        "w4_wp_sha256":         w4_wp_sha,
        "constants_path":       str(CONSTANTS_PATH.relative_to(ROOT)).replace("\\", "/"),
        "constants_sha256":     constants_sha,
        "L_max_probe":          list(L_MAX_PROBE),
        "alpha_min":            ALPHA_MIN,
        "alpha_max":            ALPHA_MAX,
        "alpha_step":           ALPHA_STEP,
        "pass_ratio_max":       PASS_RATIO_MAX,
        "fail_ratio_min":       FAIL_RATIO_MIN,
        "a0_anchors":           {str(k): int(v) for k, v in A0_ANCHORS_EXPECTED.items()},
        "a0_actual":            {str(k): int(v) for k, v in a0_actual.items()},
        "k_eff":                {str(k): float(v) for k, v in k_eff_arr.items()},
        "alpha_star":           {str(k): float(v) for k, v in alpha_star_arr.items()},
        "alpha_star_asymptotic": alpha_star_asymptotic,
        "verdict":              verdict_word,
        "verdict_value":        verdict_value,
        "bounded_alpha_count":  len(bounded_alphas),
    }
    audit_sha = closure_hash(pin_map)

    # content_sha256 = SHA-256 of script bytes (per W9a-99 dual-SHA template)
    content_sha = sha256_of_path(Path(__file__))

    print(f"[closure] content_sha256 = {content_sha}")
    print(f"[closure] audit_sha256   = {audit_sha}")
    print()

    # ---------------- Append verdict line + companion row -------------------
    canonical_line = (
        f"{GATE_ID}: {verdict_word} -- value='{verdict_value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S86+"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split) "
        f"alpha_star_L3={alpha_star_arr[3]:.4f} alpha_star_L5={alpha_star_arr[5]:.4f} "
        f"alpha_star_L7={alpha_star_arr[7]:.4f} alpha_star_L10={alpha_star_arr[10]:.4f} "
        f"alpha_star_asymptotic={alpha_star_asymptotic:.4f} "
        f"k_eff_asymptotic={k_eff_asymptotic:.4f} "
        f"target_k_eff_inf=8.0 target_alpha_star_inf=-2.0 "
        f"atlas_cardinality_after=A_4 "
        f"structural_pre_determination=R3-C-E3-C"
    )

    with open(VERDICT_PATH, "a", encoding="utf-8", newline="\n") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")

    print("[append] canonical line:")
    print(f"  {canonical_line}")
    print("[append] companion row:")
    print(f"  {companion_line}")
    print()
    print(f"[done] {GATE_ID}: {verdict_word}")
    sys.exit(0)


if __name__ == "__main__":
    main()
