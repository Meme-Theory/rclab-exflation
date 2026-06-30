"""
S89 W3-8 — S89-SU-N-CROSS-VALIDATION-5PI-CHAIN  (A.32)

Tests whether the cross-gate chain `5π = (dim+rank)/2 · π_Plancherel(SU(3)/T)`
claimed at S88 W6a workingpaper line 761 as "load-bearing structural finding"
extends structurally to SU(N) for N ∈ {2, 3, 4} — the LOAD-BEARING reading —
or is SU(3)-specific Cartan-arithmetic — the COINCIDENCE reading.

Substrate-IS framing per `phononic-framing.md §"IS Space, Not IN Space"`:
- The substrate IS the SU(3) Cartan-rational-sum structure on positive roots.
- The 5π factor IS the substrate's intrinsic heat-kernel volume normalization
  at SU(3); the chain `(dim+rank)/2 · π_Plancherel` IS the substrate-IS
  Cartan-rational-sum identity at general N.
- SU(N) extension IS the substrate algebra analog at different rank.

Method (W-19 §V.1 step 5 protocol — substrate-first canonical):
For Y_N = (1, ..., 1, 0) (N-1 ones + 1 zero, the canonical W-19 hypercharge):
  Cartan-rational-sum(N) := Σ_{α ∈ Δ⁺(SU(N))} ⟨α, Y_N⟩² / |α|²
PASS-LOAD-BEARING iff Cartan-rational-sum ≡ 1 across N ∈ {2, 3, 4}.

Discriminator at the empirical α_N level:
  α_N^{empirical}  := (dim+rank)/2 · Cartan-rational-sum(N)
                     [W-19 §V.1 line 32 algebraic identification:
                      τ-kernel denom coefficient = (dim+rank)/2 · π · Cartan-rational-sum]
  α_N^{predicted} := (dim+rank)/2  =  (N-1)(N+2)/2  =  2 (N=2), 5 (N=3), 9 (N=4)
                     [chain prediction: Cartan-rational-sum drops out as ≡ 1]
  r_N             := |α_N^{empirical} − α_N^{predicted}| / α_N^{predicted}

Decision (per plan §11):
  PASS-LOAD-BEARING iff r_2 ≤ 0.05 AND r_4 ≤ 0.05
  PASS-COINCIDENCE iff (r_2 > 0.20 OR r_4 > 0.20) AND SU(3) substrate canonical robust
  INFO              iff 0.05 < max(r_2, r_4) ≤ 0.20
  FAIL              iff regime BREAKDOWN (Sage-Q exact ⇒ never fires here)

Trigger: [SIGN] + [VERIFY] — Schema-v2 3-tuple companion row required.

Conditional follow-up (mutually exclusive, post-verdict mechanical dispatch):
  decision=LOAD-BEARING → B.46 (mack-cosmic-bridge: register §VII.{next-free} STAGE-1-CANDIDATE)
  decision=COINCIDENCE  → B.47 (orchestrator: edit s88-w6a-workingpaper.md:761 verbiage)
  decision=INFO         → NEITHER (defer to S90)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import sys
import json
import time
import hashlib
from fractions import Fraction
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path resolution + canonical_constants import (MANDATORY S34+)
# -----------------------------------------------------------------------------
THIS_FILE = Path(__file__).resolve()
ROOT = THIS_FILE.parents[2]
SHARED = ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

from canonical_constants import tau_fold, M_KK  # noqa: E402

GATE_ID = "S89-SU-N-CROSS-VALIDATION-5PI-CHAIN"
SCHEME = "SU-N-cross-validation-Cartan-rational-sum-5pi-chain"
CONVENTION = "Cartan-rational-sum-pi-Plancherel-substrate-algebra-SU-N-extension"
L_MAX = 8  # (local) plan-pinned; structural identity is L_max-independent (Sage-Q exact)
N_SCAN = [2, 3, 4]  # (local) plan-pinned

PASS_BAND_LOAD_BEARING = 0.05  # (local) plan-pinned 5%
INFO_BAND = 0.20  # (local) plan-pinned 20%

OUT_DIR = ROOT / "computations" / "session-89"
SCRIPT_STEM = "s89_w3_su_n_cross_validation_5pi_chain"
NPZ_PATH = OUT_DIR / f"{SCRIPT_STEM}.npz"
PNG_PATH = OUT_DIR / f"{SCRIPT_STEM}.png"
JSON_PATH = OUT_DIR / f"{SCRIPT_STEM}.json"
VERDICT_FILE = OUT_DIR / "s89_gate_verdicts.txt"


# -----------------------------------------------------------------------------
# SHA helpers
# -----------------------------------------------------------------------------
def sha256_bytes(b: bytes) -> str:
    """Return full 64-char hex SHA-256 of bytes."""
    return hashlib.sha256(b).hexdigest()


def sha256_file(path: Path) -> str:
    """Return full 64-char hex SHA-256 of a file's contents."""
    if not path.exists():
        return "FILE-MISSING"
    return sha256_bytes(path.read_bytes())


def closure_hash(input_pin_map: dict) -> str:
    """SHA-256 over the JSON-serialized ordered input-pin map (audit_sha256)."""
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return sha256_bytes(canonical.encode("utf-8"))


def log_input_pins(input_pin_map: dict) -> None:
    """Print SHA-256 of every input file in the first 20 lines of stdout (per
    `gate-verdicts.md §"During computation"`)."""
    print(f"=== {GATE_ID} INPUT PIN MAP ===")
    for k, v in input_pin_map.items():
        print(f"  {k}: {v}")
    print(f"=== closure_hash(audit_sha256) = {closure_hash(input_pin_map)} ===")
    print()


# -----------------------------------------------------------------------------
# SU(N) Cartan-rational-sum (substrate-first symbolic computation)
# -----------------------------------------------------------------------------
def su_n_positive_roots(N: int) -> list[tuple[int, ...]]:
    """Positive roots of SU(N) in the standard basis (e_1, ..., e_N).

    Δ⁺(SU(N)) = {α_ij = e_i − e_j : 1 ≤ i < j ≤ N}; |Δ⁺| = N(N−1)/2.
    """
    roots = []  # (local)
    for i in range(N):
        for j in range(i + 1, N):
            root = [0] * N  # (local)
            root[i] = 1
            root[j] = -1
            roots.append(tuple(root))
    return roots


def hypercharge_y_n(N: int) -> tuple[int, ...]:
    """Canonical W-19 hypercharge Y_N = (1, ..., 1, 0).

    N-1 ones followed by 1 zero. Reduces to SU(3) Y = (1, 1, 0) per W-19 line 15
    (verbatim) and SU(2) Y = (1, 0). For SU(4): Y = (1, 1, 1, 0).

    This is the "highest-weight U(1)-direction in the Cartan torus normalized so
    that on SU(3) it reduces to the §W6a-51 Y = (1,1,0)" per W-19 §V.1 step 1.
    """
    return tuple([1] * (N - 1) + [0])


def cartan_rational_sum(N: int) -> Fraction:
    """Compute Σ_{α ∈ Δ⁺(SU(N))} ⟨α, Y_N⟩² / |α|² as an exact rational.

    For α = e_i − e_j, ⟨α, Y⟩ = Y[i] − Y[j], and |α|² = 2 (always).
    Returns Fraction (Sage-Q-exact)."""
    Y = hypercharge_y_n(N)  # (local)
    roots = su_n_positive_roots(N)  # (local)
    total = Fraction(0)  # (local)
    for alpha in roots:
        alpha_dot_Y = sum(a * y for a, y in zip(alpha, Y))  # (local) integer
        alpha_norm_sq = sum(a * a for a in alpha)  # (local) integer (= 2 always)
        total += Fraction(alpha_dot_Y * alpha_dot_Y, alpha_norm_sq)
    return total


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"[{GATE_ID}] start  tau_fold={tau_fold}  M_KK={M_KK:.6e}")
    print(f"[{GATE_ID}] N_scan={N_SCAN}  L_max={L_MAX}  scheme={SCHEME}")
    print(f"[{GATE_ID}] convention={CONVENTION}")
    print()

    # -------------------------------------------------------------------------
    # Per-N computation table
    # -------------------------------------------------------------------------
    results = {}  # (local)
    for N in N_SCAN:
        dim = N * N - 1  # (local)
        rank = N - 1  # (local)
        predicted = Fraction(dim + rank, 2)  # (local) chain prediction (dim+rank)/2
        crs = cartan_rational_sum(N)  # (local) Cartan-rational-sum (Sage-Q exact)
        # Empirical α_N from the W-19 algebraic identification:
        #     τ-kernel denom = (dim+rank)/2 · π · Cartan-rational-sum
        #     so α_N^{empirical} = (dim+rank)/2 · Cartan-rational-sum
        empirical = predicted * crs  # (local) Fraction-exact
        # Relative deviation r_N
        if predicted == 0:
            r_n = Fraction(0)  # (local) (cannot occur for N ≥ 2)
        else:
            r_n = abs(empirical - predicted) / predicted  # (local) Fraction-exact
        # Signed deviation s_N (for SIGN trigger semantics)
        s_n = empirical - predicted  # (local) Fraction; sign(s_N) is the structural sign
        Y = hypercharge_y_n(N)  # (local)
        roots = su_n_positive_roots(N)  # (local)
        results[N] = {
            "N": N,
            "dim": dim,
            "rank": rank,
            "Y_N": Y,
            "n_pos_roots": len(roots),
            "cartan_rational_sum_frac": crs,
            "cartan_rational_sum_float": float(crs),
            "predicted_alpha_N_frac": predicted,
            "predicted_alpha_N_float": float(predicted),
            "empirical_alpha_N_frac": empirical,
            "empirical_alpha_N_float": float(empirical),
            "r_N_frac": r_n,
            "r_N_float": float(r_n),
            "s_N_frac": s_n,
            "s_N_float": float(s_n),
            "sign_s_N": (1 if s_n > 0 else (-1 if s_n < 0 else 0)),
        }
        print(f"  SU({N}): dim={dim}, rank={rank}, |Δ⁺|={len(roots)}, Y_N={Y}")
        print(f"          Cartan-rational-sum = {crs}  ({float(crs):.6f})")
        print(f"          predicted α_N = {predicted}  ({float(predicted):.6f})")
        print(f"          empirical α_N = {empirical}  ({float(empirical):.6f})")
        print(f"          r_N = {r_n}  ({float(r_n) * 100:.4f}%)  sign(s_N) = {results[N]['sign_s_N']:+d}")
        print()

    # SU(3) sanity: Cartan-rational-sum MUST equal 1 (W-19 line 15 verbatim arithmetic).
    crs_su3 = results[3]["cartan_rational_sum_frac"]  # (local)
    assert crs_su3 == Fraction(1, 1), (
        f"SU(3) Cartan-rational-sum sanity FAIL: got {crs_su3}, "
        f"expected 1 per W-19 §V.1 line 15 verbatim '0/2 + 1/2 + 1/2 = 1'"
    )
    print(f"  SU(3) sanity: Cartan-rational-sum = 1 ✓ (matches W-19 line 15 verbatim)")
    # SU(N) prefactor sanity per W6a-52: (dim+rank)/2 = (N-1)(N+2)/2.
    for N in N_SCAN:
        pred = results[N]["predicted_alpha_N_frac"]  # (local)
        formula = Fraction((N - 1) * (N + 2), 2)  # (local)
        assert pred == formula, (
            f"SU({N}) prefactor sanity FAIL: (dim+rank)/2 = {pred}, "
            f"(N-1)(N+2)/2 = {formula}"
        )
    print(f"  W6a-52 prefactor identity (N-1)(N+2)/2 = (dim+rank)/2 verified for N ∈ {N_SCAN} ✓")
    print()

    # -------------------------------------------------------------------------
    # Decision logic per plan §11
    # -------------------------------------------------------------------------
    r_2 = results[2]["r_N_float"]  # (local)
    r_4 = results[4]["r_N_float"]  # (local)
    max_r = max(r_2, r_4)  # (local)
    sign_2 = results[2]["sign_s_N"]  # (local)
    sign_4 = results[4]["sign_s_N"]  # (local)
    signs_consistent_in_one_direction = (sign_2 == sign_4) and (sign_2 != 0)  # (local)

    # Three-way classifier per plan §11
    if r_2 <= PASS_BAND_LOAD_BEARING and r_4 <= PASS_BAND_LOAD_BEARING:
        decision = "LOAD-BEARING"  # (local)
        composite = "PASS"  # (local)
    elif r_2 > INFO_BAND or r_4 > INFO_BAND:
        decision = "COINCIDENCE"  # (local)
        composite = "PASS"  # (local) PASS-COINCIDENCE per §11
    else:
        decision = "INFO"  # (local)
        composite = "INFO"  # (local)

    # Schema-v2 3-tuple (per plan §10 substitution chain Step 5):
    #   sign_verdict: PASS iff signs are near-zero at both N (LOAD-BEARING evidence);
    #                 FAIL iff signs CONSISTENT in same direction at both N AND
    #                       both magnitudes > info_band (structural inconsistency
    #                       per §11 FAIL clause: "sign mismatches at both N=2 AND
    #                       N=4 — substrate algebra extension structurally
    #                       inconsistent").
    #                 N/A otherwise (mixed signs or LOAD-BEARING outcome — the
    #                       gate is a 3-way classifier; the COINCIDENCE branch
    #                       does NOT pre-register a single signed direction).
    # The §11 FAIL "sign mismatches at both" reading: deviations consistently
    # WRONG in the SAME direction across N=2 AND N=4 (both negative or both
    # positive AND both > info_band) — indicating systematic substrate
    # construction failure. Mixed signs (one +, one −) is COINCIDENCE, not FAIL.
    if decision == "LOAD-BEARING":
        sign_verdict = "PASS"  # (local) signs near zero at both N
    elif (
        decision == "COINCIDENCE"
        and signs_consistent_in_one_direction
        and r_2 > INFO_BAND
        and r_4 > INFO_BAND
    ):
        # Would only fire if signs are CONSISTENTLY off in the same wrong
        # direction at both N AND both exceed info_band (structural inconsistency
        # per §11 FAIL clause). Our data has mixed signs, so this branch is
        # unreachable; included for completeness per pre-registration.
        sign_verdict = "FAIL"  # (local)
    else:
        sign_verdict = "N/A"  # (local) gate is a 3-way classifier without a single signed pre-registration

    # magnitude_verdict measures the gate-classification PASS condition, NOT
    # the LOAD-BEARING null hypothesis directly. For PASS-COINCIDENCE the
    # gate-classification PASS condition is `r > 20%` (the COINCIDENCE
    # threshold); when that condition is met, magnitude_verdict = PASS for the
    # gate's classification. The Schema-v2 default reading (target =
    # LOAD-BEARING null, magnitude_verdict = FAIL when r > info_band) IS the
    # diagnostic reading; the gate's §11 3-way classifier OVERRIDES the
    # default for the composite top-line. See verdict-line value field for
    # documentation of the override (decision=COINCIDENCE).
    if decision == "LOAD-BEARING":
        magnitude_verdict = "PASS"  # (local)
    elif decision == "INFO":
        magnitude_verdict = "INFO"  # (local)
    elif decision == "COINCIDENCE":
        # PASS-COINCIDENCE: the gate's COINCIDENCE classification PASS condition
        # (r > 20% at either N) is met. magnitude_verdict = PASS reflects
        # gate-classification success per §11 PASS-COINCIDENCE clause.
        magnitude_verdict = "PASS"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    # regime_verdict: VALID — Sage-Q exact, no regime breakdown possible by construction.
    regime_verdict = "VALID"  # (local)

    # Composite-collapse cross-check: the gate's §11 3-way classifier supersedes
    # the Schema-v2 default collapse for the composite top-line. With our
    # 3-tuple emission (sign=N/A, magnitude=PASS, regime=VALID), the default
    # collapse yields PASS — consistent with our composite=PASS-COINCIDENCE.
    print(f"  Decision: {decision}")
    print(f"  Composite top-line: {composite}")
    print(f"  3-tuple: sign_verdict={sign_verdict}  magnitude_verdict={magnitude_verdict}  regime_verdict={regime_verdict}")
    print()

    # -------------------------------------------------------------------------
    # Substitution chain documentation (MANDATORY per math-scripts.md)
    # -------------------------------------------------------------------------
    sub_chain = [  # (local)
        f"Step 1: For N ∈ {N_SCAN}, dim(SU(N)) = N²−1, rank(SU(N)) = N−1.",
        f"        SU(2): dim={results[2]['dim']}, rank={results[2]['rank']}, predicted α_2 = {results[2]['predicted_alpha_N_frac']} = {results[2]['predicted_alpha_N_float']}",
        f"        SU(3): dim={results[3]['dim']}, rank={results[3]['rank']}, predicted α_3 = {results[3]['predicted_alpha_N_frac']} = {results[3]['predicted_alpha_N_float']} [substrate canonical, per §W6a-51 / §W6a-52]",
        f"        SU(4): dim={results[4]['dim']}, rank={results[4]['rank']}, predicted α_4 = {results[4]['predicted_alpha_N_frac']} = {results[4]['predicted_alpha_N_float']}",
        "Step 2: HK closed form at SU(N): d_eff(τ) = α_N / (1 − τ/(α_N · π_Plancherel))",
        "        SU(2): 2/(1 − τ/(2π))  [chain prediction]",
        "        SU(3): 5/(1 − τ/(5π))  [substrate canonical, S87 d_eff workshop, S88 W6a-51 PROVEN]",
        "        SU(4): 9/(1 − τ/(9π))  [chain prediction]",
        "Step 3: Substrate-first canonical (W-19 §V.1 step 5) — Cartan-rational-sum on SU(N) hypercharge:",
        "        Y_N = (1, ..., 1, 0) (N-1 ones + 1 zero); Σ_α ⟨α,Y_N⟩²/|α|² over Δ⁺(SU(N)).",
        f"        SU(2): Y=(1,0); Δ⁺={{α₁₂=(1,-1)}}; ⟨α,Y⟩=1; |α|²=2; sum = 1/2 = {results[2]['cartan_rational_sum_frac']}",
        f"        SU(3): Y=(1,1,0); Δ⁺={{α₁₂,α₁₃,α₂₃}}; sum = 0/2 + 1/2 + 1/2 = 1 = {results[3]['cartan_rational_sum_frac']} [W-19 line 15 verbatim]",
        f"        SU(4): Y=(1,1,1,0); Δ⁺={{6 roots}}; sum = (0+0+1+0+1+1)/2 = 3/2 = {results[4]['cartan_rational_sum_frac']}",
        "Step 4: Empirical α_N := (dim+rank)/2 · Cartan-rational-sum (W-19 §V.1 line 32 algebraic identification).",
        f"        SU(2) empirical α_2 = {results[2]['empirical_alpha_N_frac']} ({results[2]['empirical_alpha_N_float']})",
        f"        SU(3) empirical α_3 = {results[3]['empirical_alpha_N_frac']} ({results[3]['empirical_alpha_N_float']})  [tautological: Cartan-rational-sum=1]",
        f"        SU(4) empirical α_4 = {results[4]['empirical_alpha_N_frac']} ({results[4]['empirical_alpha_N_float']})",
        f"Step 5: Discriminator: r_N = |α_N^{{empirical}} − α_N^{{predicted}}| / α_N^{{predicted}}.",
        f"        r_2 = {r_2:.6f} ({r_2 * 100:.4f}%); r_4 = {r_4:.6f} ({r_4 * 100:.4f}%)",
        f"        max(r_2, r_4) = {max_r:.6f} ({max_r * 100:.4f}%)",
        f"        Pre-registered bands: PASS-LOAD-BEARING ≤ 5%, INFO 5-20%, PASS-COINCIDENCE > 20%.",
        f"Direction: max(r_2, r_4) = {max_r * 100:.2f}% {'≤ 5%' if max_r <= 0.05 else ('≤ 20%' if max_r <= 0.20 else '> 20%')} ⇒ decision = {decision}.",
        f"Conclusion: Cartan-rational-sum varies with N (1/2, 1, 3/2 for N=2,3,4) ⇒ chain `(dim+rank)/2 · π_Plancherel` is NOT structurally LOAD-BEARING.",
    ]
    print("=== Substitution chain ===")
    for line in sub_chain:
        print(f"  {line}")
    print()

    # -------------------------------------------------------------------------
    # Input-pin map
    # -------------------------------------------------------------------------
    canonical_constants_path = SHARED / "canonical_constants.py"
    s88_w19_path = ROOT / "sessions" / "session-88" / "workshops" / "s88-w19-w6a-cross-gate-chain.md"
    s88_w6a_wp_path = ROOT / "sessions" / "session-88" / "session-88-w6a-workingpaper.md"
    permanent_registry_path = ROOT / "sessions" / "permanent-results-registry.md"

    input_pin_map = {  # (local) ordered by name (sort_keys=True at hash time)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "tau_fold": str(tau_fold),
        "M_KK": str(M_KK),
        "N_scan": N_SCAN,
        "Y_N_canonical_form": "(1, ..., 1, 0) — N-1 ones + 1 zero per W-19 §V.1 step 1",
        "pass_band_LOAD_BEARING": PASS_BAND_LOAD_BEARING,
        "info_band": INFO_BAND,
        "input_files_sha256": {
            "canonical_constants_py": sha256_file(canonical_constants_path),
            "s88_w19_w6a_cross_gate_chain_md": sha256_file(s88_w19_path),
            "s88_w6a_workingpaper_md": sha256_file(s88_w6a_wp_path),
            "permanent_results_registry_md": sha256_file(permanent_registry_path),
        },
        "decision": decision,
        "results_by_N": {
            str(N): {
                "cartan_rational_sum_frac_str": str(results[N]["cartan_rational_sum_frac"]),
                "predicted_alpha_N_frac_str": str(results[N]["predicted_alpha_N_frac"]),
                "empirical_alpha_N_frac_str": str(results[N]["empirical_alpha_N_frac"]),
                "r_N_frac_str": str(results[N]["r_N_frac"]),
                "sign_s_N": results[N]["sign_s_N"],
            }
            for N in N_SCAN
        },
    }
    log_input_pins(input_pin_map)

    audit_sha256 = closure_hash(input_pin_map)  # (local)

    # -------------------------------------------------------------------------
    # NPZ + JSON sidecars
    # -------------------------------------------------------------------------
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        NPZ_PATH,
        N_scan=np.array(N_SCAN, dtype=np.int64),
        cartan_rational_sum=np.array([float(results[N]["cartan_rational_sum_frac"]) for N in N_SCAN], dtype=np.float64),
        predicted_alpha_N=np.array([float(results[N]["predicted_alpha_N_frac"]) for N in N_SCAN], dtype=np.float64),
        empirical_alpha_N=np.array([float(results[N]["empirical_alpha_N_frac"]) for N in N_SCAN], dtype=np.float64),
        r_N=np.array([float(results[N]["r_N_frac"]) for N in N_SCAN], dtype=np.float64),
        sign_s_N=np.array([results[N]["sign_s_N"] for N in N_SCAN], dtype=np.int64),
        decision=decision,
        composite=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        audit_sha256=audit_sha256,
    )
    print(f"[npz]  {NPZ_PATH}")
    content_sha256 = sha256_file(NPZ_PATH)  # (local) full 64-char content SHA on the npz output

    metadata = {  # (local)
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "decision": decision,
        "composite": composite,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "results_by_N": {
            str(N): {
                "cartan_rational_sum": str(results[N]["cartan_rational_sum_frac"]),
                "cartan_rational_sum_float": results[N]["cartan_rational_sum_float"],
                "predicted_alpha_N": str(results[N]["predicted_alpha_N_frac"]),
                "predicted_alpha_N_float": results[N]["predicted_alpha_N_float"],
                "empirical_alpha_N": str(results[N]["empirical_alpha_N_frac"]),
                "empirical_alpha_N_float": results[N]["empirical_alpha_N_float"],
                "r_N": str(results[N]["r_N_frac"]),
                "r_N_float": results[N]["r_N_float"],
                "sign_s_N": results[N]["sign_s_N"],
            }
            for N in N_SCAN
        },
        "substitution_chain": sub_chain,
        "input_pin_map": input_pin_map,
    }
    JSON_PATH.write_text(json.dumps(metadata, indent=2, default=str))
    print(f"[json] {JSON_PATH}")

    # -------------------------------------------------------------------------
    # PNG plot — α_N^{empirical} vs α_N^{predicted} across N ∈ {2, 3, 4}
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 6))
    Ns = np.array(N_SCAN, dtype=np.float64)  # (local)
    pred = np.array([results[N]["predicted_alpha_N_float"] for N in N_SCAN])  # (local)
    emp = np.array([results[N]["empirical_alpha_N_float"] for N in N_SCAN])  # (local)
    crs = np.array([results[N]["cartan_rational_sum_float"] for N in N_SCAN])  # (local)
    # Connect predicted by solid blue (chain prediction line), empirical by red squares
    ax.plot(Ns, pred, "b-o", label=r"$\alpha_N^{\rm predicted} = (\dim+\rm rank)/2$ (chain LOAD-BEARING)", markersize=10, linewidth=2)
    ax.plot(Ns, emp, "rs", label=r"$\alpha_N^{\rm empirical} = (\dim+\rm rank)/2 \cdot \rm Cartan\text{-}rational\text{-}sum$", markersize=12)
    for N, p, e, c in zip(N_SCAN, pred, emp, crs):
        ax.annotate(f"  Cartan-rational-sum={Fraction(c).limit_denominator(100)}",
                    xy=(N, e), fontsize=9, color="darkred")
    ax.axhline(y=0, color="gray", linewidth=0.5)
    ax.set_xlabel("N (SU(N) substrate algebra rank)", fontsize=12)
    ax.set_ylabel(r"$\alpha_N$ (HK closed-form prefactor)", fontsize=12)
    ax.set_title(
        f"S89 W3-8: SU(N) cross-validation of chain $5\\pi = (\\dim+\\rm rank)/2 \\cdot \\pi_{{\\rm Plancherel}}$\n"
        f"decision = {decision} (composite={composite})  |  r_2={r_2 * 100:.2f}%  r_4={r_4 * 100:.2f}%",
        fontsize=11,
    )
    ax.set_xticks(N_SCAN)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=120)
    plt.close(fig)
    print(f"[png]  {PNG_PATH}")
    print()

    # -------------------------------------------------------------------------
    # Verdict-line append per S87+ Schema-v2 (canonical line + dual-SHA companion + 3-tuple companion)
    # -------------------------------------------------------------------------
    audit_short = audit_sha256[:16]  # (local)
    content_short = content_sha256[:16]  # (local)

    value_str = (
        "{"
        f"alpha_2_emp={results[2]['empirical_alpha_N_float']:.6f},"
        f"alpha_4_emp={results[4]['empirical_alpha_N_float']:.6f},"
        f"r_2={r_2:.6f},"
        f"r_4={r_4:.6f},"
        f"decision={decision},"
        f"crs_SU2=1/2,"
        f"crs_SU3=1,"
        f"crs_SU4=3/2"
        "}"
    )

    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )
    three_tuple_companion = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as fh:
        fh.write(canonical_line + "\n")
        fh.write(dual_sha_companion + "\n")
        fh.write(three_tuple_companion + "\n")

    print(f"[verdict] appended to {VERDICT_FILE}")
    print(f"[verdict] {canonical_line}")
    print(f"[verdict] {dual_sha_companion}")
    print(f"[verdict] {three_tuple_companion}")
    print()

    # -------------------------------------------------------------------------
    # Conditional follow-up tag (B.46 vs B.47 mechanical edit; informational)
    # -------------------------------------------------------------------------
    if decision == "LOAD-BEARING":
        followup_tag = "B.46 (LOAD-BEARING → §VII.{next-free} STAGE-1-CANDIDATE registration via mack-cosmic-bridge)"
    elif decision == "COINCIDENCE":
        followup_tag = "B.47 (COINCIDENCE → s88-w6a-workingpaper.md:761 verbiage edit via orchestrator)"
    else:
        followup_tag = "NEITHER (INFO outcome — defer B.46/B.47 to S90)"
    print(f"[followup] {followup_tag}")

    elapsed = time.time() - t0  # (local)
    print(f"[{GATE_ID}] done  elapsed={elapsed:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
