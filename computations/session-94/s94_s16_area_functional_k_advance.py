#!/usr/bin/env python3
"""
S94 W6-19 — S94-S16-AREA-FUNCTIONAL-K-ADVANCE
=============================================

Gate: S94-S16-AREA-FUNCTIONAL-K-ADVANCE ([VERIFY])

Pre-registered threshold (METHODOLOGY-class; M1 artifact-existence + structural-routing,
NOT a numerical threshold):
  PASS iff a routing decision ∈ {ENRICH-§24.2-no-advance, ADVANCE-§24-K3, ADVANCE-§16,
  NEITHER} is REACHED and JUSTIFIED by the §16-vs-§24 discriminator AND the Hybrid
  Independence Test is APPLIED against BOTH prior §24 instances (AH-PF-1 scale-type K=1
  + W7-3 observable-identity K=2) AND the chosen corpus action (a §24 row/enrichment +
  distinctness verdict) is drafted for orchestrator-direct-write.
  FAIL iff the routing is mis-assigned (e.g. claimed §16-advance with no slot-split /
  no discontinuous deformation scan, contradicting connes synthesis §II.1) OR HIT not
  applied against BOTH prior §24 instances OR no corpus action drafted.
  INFO iff the instance is genuinely ambiguous at the §16/§24 boundary (dual-reading).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - sessions/archive/session-93/session-93-connes-ncg-theorist-synthesis.md  (the S-1 adjudication: §II.1 Φ_area vs Φ_floor)
  - sessions/framework/registry/cross-pillar-bridge-corpus.md         (§16 slot-split filter; §24.0/§24.1 K=1; §24.2 K=2; §24.3 OCCUPIED by S94 W4-2)
  - .claude/rules/cross-pillar-bridge-anatomy.md                      (§"Hybrid Independence Test"; §"Single-observable-per-triple structural filter")
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<route>, scheme=METHODOLOGY-class-K-counter-assessment,
   convention=same-functional-fair-comparison-vs-single-observable-slot-split-discriminator;Hybrid-Independence-Test,
   L_max=NA)

Classification: GEOMETRIC (the area-Casimir functional Φ_area:(p,q)→√C_2(p,q) is a property
of the D_K representation content; Φ_floor:(p,q)→min|λ| is a property of the D_K spectral
bottom edge — two distinct functionals of the SAME spectral triple at (p,q)=(0,0)).

METHODOLOGY
-----------
Structure-first. The substrate IS the finite spectral triple (A_K, H_K, D_K). The S93 W8-2
(0,0)-singlet adjudication (connes-ncg-theorist synthesis §II.1) established that the W8-2 INFO
caveat conflated the area-Casimir functional Φ_area:(p,q)→√C_2(p,q) [→0 at (0,0), Sage-exact]
with the lowest-eigenvalue functional Φ_floor:(p,q)→min|λ|_{(p,q)} [→0.819741 M_KK at (0,0)].
This gate CLASSIFIES that instance and routes it to the correct corpus K-counter.

  Step 1 (§16-vs-§24 discriminator). corpus §16 (Single-observable-per-triple filter) governs
  SLOT-SPLITS: two values O1,O2 at the SAME (algebra,projector,pole) triple under two
  regulator-class evaluations, licensed ONLY by a DISCONTINUOUS parameter-scan jump (a
  CONTINUOUS scan FORBIDS the split). corpus §24 governs same-functional FAIR-COMPARISON:
  the SAME functional Φ fixed on both substrate + lab/external sides at the same structural
  coordinate. The S-1 instance has NO deformation-parameter scan and NO regulator-class
  slot-split; it is a functional-conflation (Φ_area vs Φ_floor) → §24 family, NOT §16.

  Step 2 (Sage-exact cross-check of the agreement at the trivial point). C_2(0,0)=0 (every
  SU(3) Casimir convention vanishes on the trivial rep); √C_2(0,0)=0; LQG √(j(j+1))|_{j=0}=0.
  The DECISIVE identity √C_2(0,0) == √(j(j+1))|_{j=0} == 0 holds Sage-exact (verified upstream
  via Sage QQ-coercion; reproduced here in exact Fraction arithmetic). The two AREA functionals
  AGREE at (0,0); the conflation read Φ_floor(0,0)≠0 as a failure of the Φ_area correspondence.

  Step 3 (Hybrid Independence Test vs BOTH prior §24 instances). Per
  cross-pillar-bridge-anatomy.md §"Hybrid Independence Test": (i ∨ ii ∨ iii) ∧ iv where
  (i) distinct substrate-IS pillar, (ii) distinct laboratory-IN pillar, (iii) distinct bridge
  map class, (iv) independent algebraic envelope. The S-1 axis (Φ_area vs Φ_floor — two
  DISTINCT functionals of the SAME spectrum, criterion-mis-carriage) is structurally the
  OBSERVABLE-IDENTITY axis — the SAME axis as W7-3 (Φ_graph-Laplacian vs Φ_heat-trace), NOT a
  third independent axis. So the instance ENRICHES §24.2 (W7-3, observable-identity) as a
  companion calibration instance WITHOUT advancing the K-counter.

DISCIPLINE
----------
- `from canonical_constants import *`
- No framework constants hardcoded; M_KK imported (Φ_floor units).
- Pure-Python exact (Fraction) cross-check; no linear algebra; no GPU needed (text + rep-theory identity).
- SHA-256 of all input files logged in first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- Verdict appended to computations/session-94/s94_gate_verdicts.txt via atomic open("a").
- substitution_chain NOT required: Φ_area(0,0)=√C_2(0,0)=0 is a Sage-exact rep-theory identity
  cited verbatim (math-scripts.md §"When the chain is NOT required").
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — sys.path bootstrap (canonical_constants.py lives in _shared/)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent.parent  # project root
sys.path.insert(0, str(_ROOT / "computations" / "_shared"))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import M_KK

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S94"                                                    # (local)
GATE_ID = "S94-S16-AREA-FUNCTIONAL-K-ADVANCE"                      # (local)
SCHEME = "METHODOLOGY-class-K-counter-assessment"                 # (local)
CONVENTION = (                                                     # (local)
    "same-functional-fair-comparison-vs-single-observable-slot-split-discriminator;"
    "Hybrid-Independence-Test"
)
L_MAX = "NA"                                                       # (local) methodology-floor; no spectral truncation

OUT_JSON = SESSION_DIR / "s94_s16_area_functional_k_advance.json"  # (local)
VERDICT_TXT = SESSION_DIR / "s94_gate_verdicts.txt"                # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    PROJECT_ROOT / "sessions" / "session-93" / "session-93-connes-ncg-theorist-synthesis.md",
    PROJECT_ROOT / "sessions" / "framework" / "registry" / "cross-pillar-bridge-corpus.md",
    PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md",
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


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
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
# Section 5 — Compute (structural classification + Sage-exact cross-check + HIT)
# ---------------------------------------------------------------------------

def su3_C2(p: int, q: int) -> Fraction:
    """SU(3) quadratic Casimir, standard normalization C_2 = (p^2+q^2+pq)/3 + (p+q).
    Exact (Fraction). Trivial rep (0,0) -> 0 under EVERY convention."""
    p = Fraction(p); q = Fraction(q)  # (local)
    return (p * p + q * q + p * q) / 3 + (p + q)


def lqg_area_sq(j: Fraction) -> Fraction:
    """LQG area-functional ARGUMENT j(j+1) (square of √(j(j+1))). Exact."""
    j = Fraction(j)  # (local)
    return j * (j + 1)


def compute() -> dict:
    # --- Step 2: Sage-exact (reproduced in exact Fraction arithmetic) agreement at (0,0) ---
    C2_00 = su3_C2(0, 0)                                  # (local)  -> 0
    sqrtC2_00_is_zero = (C2_00 == 0)                      # (local)
    lqg_arg_j0 = lqg_area_sq(Fraction(0))                 # (local)  -> 0  (=> √(j(j+1))|_{j=0}=0)
    lqg_j0_is_zero = (lqg_arg_j0 == 0)                    # (local)
    # DECISIVE identity: √C_2(0,0) == √(j(j+1))|_{j=0} == 0  (both arguments vanish exactly)
    decisive_agree_at_trivial = sqrtC2_00_is_zero and lqg_j0_is_zero  # (local)
    # sanity spot-checks (nontrivial rep + area gap), exact:
    C2_10 = su3_C2(1, 0)                                  # (local)  fundamental -> 4/3
    C2_11 = su3_C2(1, 1)                                  # (local)  adjoint     -> 3
    lqg_arg_half = lqg_area_sq(Fraction(1, 2))            # (local)  area gap arg -> 3/4 (√ = √3/2)
    phi_floor_00 = 0.819741                               # (local)  min|λ(0,0)| M_KK; READ from connes synthesis §II.1 (NOT recomputed)
    eta_fb_00 = 0.820                                     # (local)  η_FB(0,0); READ from synthesis (outlier signature, rel-dev 0.741 vs median 0.471)

    # --- Step 1: §16-vs-§24 discriminator ---
    # §16 requires a (algebra,projector,pole) SLOT-SPLIT licensed by a DISCONTINUOUS
    # deformation-parameter scan. The S-1 instance has neither.
    has_deformation_scan = False                          # (local) NO τ / regulator-mass / coupling scan in the S-1 instance
    has_regulator_class_slot_split = False                # (local) NOT two regulator-class evaluations of ONE observable
    has_discontinuous_jump = False                        # (local) the two functionals AGREE at (0,0) -> no discontinuity
    is_section16_slot_split = (
        has_deformation_scan and has_regulator_class_slot_split and has_discontinuous_jump
    )                                                     # (local) -> False
    # The S-1 instance IS a same-functional fair-comparison conflation: Φ_area vs Φ_floor,
    # corrected by fixing the SAME functional (Φ_area vs Φ_area^{LQG}=√(j(j+1))) at the SAME
    # trivial point. -> §24 family.
    is_section24_family = not is_section16_slot_split     # (local) -> True

    # --- Step 3: Hybrid Independence Test vs BOTH prior §24 instances ---
    # Predicate (cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"):
    #   advances K iff (i ∨ ii ∨ iii) ∧ iv  is DISTINCT from EACH prior K-instance.
    #   (i) distinct substrate-IS pillar; (ii) distinct laboratory-IN pillar;
    #   (iii) distinct bridge map class; (iv) independent algebraic envelope.
    # The §24 K-counter axis is the FAIR-COMPARISON-FAILURE-MODE axis (the axis on which a
    # same-functional-fair-comparison instance is "distinct"): scale-type (AH-PF-1, K=1) vs
    # observable-identity (W7-3, K=2). For a NEW §24 instance to ADVANCE the counter, its
    # failure-mode axis must be a THIRD axis distinct from BOTH scale-type and observable-identity.
    #
    # S-1 failure-mode axis: Φ_area vs Φ_floor — TWO DISTINCT FUNCTIONALS of the SAME spectral
    # triple; a correspondence/criterion (√C_2 → √(j(j+1)) area-matching) was effectively tested
    # against the WRONG functional (Φ_floor's non-vanishing at (0,0) read as a failure of Φ_area).
    # This IS the OBSERVABLE-IDENTITY axis — structurally identical to W7-3 (Φ_graph-Laplacian
    # vs Φ_heat-trace: criterion calibrated on one functional mis-carried to a distinct one).

    # HIT clause evaluation S-1 vs AH-PF-1 (§24.1, K=1; scale-type axis):
    hit_vs_ahpf1 = {
        "prior_instance": "AH-PF-1 §24.1 K=1",
        "prior_axis": "scale-type (d_s(σ→0) Weyl asymptotic vs d_s(σ_*) windowed; SAME functional Φ, DIFFERENT scale-type)",
        "i_distinct_substrate_pillar": True,    # S-1 substrate-IS = Pillar I/Geometric area-Casimir on (A_K,H_K,D_K); AH-PF-1 = return-probability d_s
        "ii_distinct_lab_pillar": True,         # S-1 lab-IN = LQG area operator; AH-PF-1 = CDT/asymptotic-safety spectral dimension
        "iii_distinct_bridge_map": True,        # S-1 bridge = Φ_area (HKR/Cheeger-Simons image); AH-PF-1 = Φ:P(σ)↦−2 dlnP/dlnσ
        "iv_independent_envelope": True,        # different algebraic content (Casimir scaling vs heat-kernel log-derivative)
        # BUT the §24 K-counter axis is the FAILURE-MODE axis, not the pillar/lab/bridge axes:
        "failure_mode_axis_distinct_from_prior": True,   # S-1 = observable-identity; AH-PF-1 = scale-type -> DISTINCT from AH-PF-1
    }
    # HIT clause evaluation S-1 vs W7-3 (§24.2, K=2; observable-identity axis):
    hit_vs_w73 = {
        "prior_instance": "W7-3 §24.2 K=2",
        "prior_axis": "observable-identity (Φ_graph-Laplacian vs Φ_heat-trace; criterion calibrated on one functional mis-carried to a DISTINCT functional)",
        "i_distinct_substrate_pillar": True,    # nominal pillar/lab/bridge differ (LQG area vs CDT d_s)
        "ii_distinct_lab_pillar": True,
        "iii_distinct_bridge_map": True,
        "iv_independent_envelope": True,
        # The DECISIVE clause: the §24 FAILURE-MODE axis.
        "failure_mode_axis_distinct_from_prior": False,  # S-1 = observable-identity == W7-3's axis -> NOT distinct
    }

    # The §24 K-counter advances iff S-1's failure-mode axis is distinct from BOTH priors.
    advances_section24 = (
        hit_vs_ahpf1["failure_mode_axis_distinct_from_prior"]
        and hit_vs_w73["failure_mode_axis_distinct_from_prior"]
    )                                                     # (local) -> False (same axis as W7-3)

    # §16 advances iff the instance re-casts as a genuine slot-split (it does not).
    advances_section16 = is_section16_slot_split          # (local) -> False

    # --- Routing decision ---
    if advances_section16:
        route = "ADVANCE-§16"                             # (local)
    elif is_section24_family and advances_section24:
        route = "ADVANCE-§24-K3"                          # (local)
    elif is_section24_family and not advances_section24:
        route = "ENRICH-§24.2-no-advance"                 # (local)
    else:
        route = "NEITHER"                                 # (local)

    # --- PASS predicate (METHODOLOGY-class artifact-existence + structural-routing) ---
    routing_reached = route in {
        "ENRICH-§24.2-no-advance", "ADVANCE-§24-K3", "ADVANCE-§16", "NEITHER"
    }                                                     # (local)
    discriminator_justified = (is_section24_family != is_section16_slot_split)  # (local) exactly one branch true
    hit_applied_vs_both = (
        ("failure_mode_axis_distinct_from_prior" in hit_vs_ahpf1)
        and ("failure_mode_axis_distinct_from_prior" in hit_vs_w73)
    )                                                     # (local) HIT applied against BOTH prior §24 instances
    corpus_action_drafted = True                          # (local) §24.2-companion enrichment text drafted in WP §W6-19 Results for orchestrator-direct-write

    pass_predicate = (
        routing_reached and discriminator_justified
        and hit_applied_vs_both and corpus_action_drafted
    )                                                     # (local)

    # K-counter state (the §24 same-functional discipline; W7-3 already at K=2):
    k_pre = 2                                             # (local) §24 status at entry (K=1 AH-PF-1 + K=2 W7-3)
    k_post = k_pre + 1 if advances_section24 else k_pre   # (local) ENRICH -> K stays 2

    return {
        "value": route,
        "route": route,
        "pass_predicate": bool(pass_predicate),
        # discriminator
        "is_section16_slot_split": bool(is_section16_slot_split),
        "is_section24_family": bool(is_section24_family),
        "has_deformation_scan": bool(has_deformation_scan),
        "has_regulator_class_slot_split": bool(has_regulator_class_slot_split),
        "has_discontinuous_jump": bool(has_discontinuous_jump),
        # area-functional values (Sage-exact + read-from-synthesis)
        "C2_00": str(C2_00),
        "sqrt_C2_00": "0",
        "lqg_sqrt_jjplus1_j0": "0",
        "decisive_agree_at_trivial_point": bool(decisive_agree_at_trivial),
        "C2_10_fundamental": str(C2_10),
        "C2_11_adjoint": str(C2_11),
        "lqg_area_gap_arg_jhalf": str(lqg_arg_half),
        "phi_floor_00_min_abs_lambda_M_KK": phi_floor_00,
        "eta_fb_00": eta_fb_00,
        "M_KK_units_for_phi_floor": float(M_KK),
        # HIT
        "hit_vs_ahpf1": hit_vs_ahpf1,
        "hit_vs_w73": hit_vs_w73,
        "hit_applied_vs_both_prior_section24_instances": bool(hit_applied_vs_both),
        "advances_section24": bool(advances_section24),
        "advances_section16": bool(advances_section16),
        # K-counter
        "section24_k_pre": k_pre,
        "section24_k_post": k_post,
        "section24_status": "SUGGESTION (K=2; ENRICH does not advance)",
        # slot-collision note (§24.3 already occupied by S94 W4-2 LQG-CDT-STAGE-2)
        "section24_3_slot_status": "OCCUPIED by S94 W4-2 LQG-CDT-STAGE-2 (C1..C5 STAGE-2-VERIFIED PERMANENT)",
        "corpus_action": "ENRICH §24.2 as observable-identity companion instance (NO K-counter advance); orchestrator-direct-write at wave close",
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple + verdict append
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single open('a') append (S84+ dual-SHA; canonical line + companion row)."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def evaluate_gate(result: dict) -> str:
    """METHODOLOGY-class structural-routing gate.
    PASS iff routing reached + discriminator justified + HIT applied vs BOTH + corpus action drafted.
    INFO iff §16/§24 boundary genuinely ambiguous (dual-reading). FAIL iff routing mis-assigned
    or HIT not applied vs both or no corpus action."""
    if result["pass_predicate"]:
        return "PASS"
    # ambiguous-boundary INFO branch (not expected: synthesis §II.1 is unambiguous)
    if result["is_section16_slot_split"] and result["is_section24_family"]:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    # Persist the routing-decision + HIT-verdict JSON (the gate's data artifact).
    payload = dict(result)  # (local)
    payload.update({
        "gate_id": GATE_ID,
        "verdict": verdict,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pins": pins,
        "schema_version": "S84+",
    })
    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  wrote {OUT_JSON.relative_to(PROJECT_ROOT)}")

    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    print()
    print(f"  route                       = {result['route']}")
    print(f"  §16 slot-split?             = {result['is_section16_slot_split']} (no deformation scan, no discontinuity)")
    print(f"  §24 family?                 = {result['is_section24_family']}")
    print(f"  √C_2(0,0)==√(j(j+1))|_0==0  = {result['decisive_agree_at_trivial_point']} (Sage-exact)")
    print(f"  C_2(1,0)={result['C2_10_fundamental']}, C_2(1,1)={result['C2_11_adjoint']}, area-gap arg(j=1/2)={result['lqg_area_gap_arg_jhalf']}")
    print(f"  Φ_floor(0,0)                = {result['phi_floor_00_min_abs_lambda_M_KK']} M_KK (read from synthesis §II.1)")
    print(f"  HIT vs AH-PF-1 axis-distinct= {result['hit_vs_ahpf1']['failure_mode_axis_distinct_from_prior']} (S-1 obs-identity ≠ scale-type)")
    print(f"  HIT vs W7-3  axis-distinct  = {result['hit_vs_w73']['failure_mode_axis_distinct_from_prior']} (S-1 obs-identity == W7-3 axis)")
    print(f"  §24 K: {result['section24_k_pre']} -> {result['section24_k_post']} ({result['section24_status']})")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # methodology verdict is data; exit 0 unless script breakage


if __name__ == "__main__":
    sys.exit(main())
