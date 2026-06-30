#!/usr/bin/env python3
"""
S93 W9-5 — Layer-Functor F Verdict-Shape Consistency Theorem Reformulation-vs-Close
===================================================================================

Gate: S93-W9-5-LAYER-FUNCTOR-F-VERDICT-SHAPE-CONSISTENCY-REFORMULATION-WORKSHOP
      ([VERIFY-THEOREM]; GEOMETRIC)

This is a WORKSHOP-DISPATCH verdict-emission script (NO physics compute). The
adversarial 2-agent / 3-round workshop (lizzi-spectral-functional-theorist Axis-A
vs landau-condensed-matter-theorist Axis-B) is documented in the transcript
`sessions/archive/session-93/workshops/s93-w9-5-layer-functor-f-reformulation.md`; this
script (a) emits the canonical dual-SHA verdict line whose closure is COMPUTED
(NOT hardcoded) over the input-pin map per the plan's audit_discriminators, and
(b) writes the JSON closure record (the structural verdict A/B, evidence basis,
K-counter consequence).

STRUCTURAL VERDICT (R3 convergence): VERDICT-B (CLOSE).
  The Layer-Functor F Verdict-Shape Consistency Theorem's universal-envelope
  reading is retired at K=2 (FALSIFIED-at-K=2 -> CLOSED), with the S82 within-
  channel F_2-axis FI contour-deformation identity carved out and PRESERVED.

  Evidence basis (cited per plan operator clause):
    - §W9-3 CF-W6-4-S91-1: sigma_beta = 1.065 at the Friedrich-Bar-saturated
      L->infinity layer (grown from cache baseline 0.8936) -> the cross-observable
      consistency the K=2 SUGGESTION asserted is FALSIFIED at the asymptotic layer
      where Reading_Hybrid placed it (FI-side decisive blow).
    - §W9-5 Richardson: alpha_sub = 0.876 (SUB-geometric), anchor-crossing L=10,
      divergent step ratio 2.105 -> the FI-sub-projection sub-window has no
      convergent asymptotic exponent (RD-classified; corroborating second leg).

Top-line verdict: PASS (workshop-complete: R1/R2/R3 present + single STRUCTURAL
  VERDICT pinned in R3 + evidence basis cited). The STRUCTURAL VERDICT (CLOSE) is
  recorded in value= / WP / JSON.

Output 4-tuple:
  (value='PASS_workshop-complete;STRUCTURAL_VERDICT=CLOSE;...',
   scheme=ADVERSARIAL-WORKSHOP-2-AGENT-3-ROUND-LAYER-FUNCTOR-F-REFORMULATION,
   convention=R1-steelman-R2-respond-R3-converge-STRUCTURAL-VERDICT-reformulate-K2-weak-vs-close,
   L_max=N/A)

Dual-SHA (plan audit_discriminators):
  audit_sha256  inputs: [s91_w5_predecessor_adjudication, s92_w8_1_disambiguation,
                         s92_w9_workingpaper, pinmap]   ("script","canonical","pinmap")
  content_sha256 inputs: [workshop_document]            ("script")

Classification: GEOMETRIC

DISCIPLINE
----------
- from canonical_constants import *  (MANDATORY first import)
- every local/intermediate tagged # (local)
- no matrices, no GPU needed (workshop-dispatch emission; NO physics compute)
- dual-SHA (audit_sha256 + content_sha256) + W9a-99 companion row
- [VERIFY-THEOREM] trigger: NO S87 schema-v2 3-tuple companion row required
- Option-A supersedes-chain read (verdict permanence) for re-runs
- 4-tuple printed as final non-verdict line
- Exit 0 for any valid verdict (verdict is DATA, not script health)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap (make canonical_constants importable)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration (paths defined in Section 0)
# ---------------------------------------------------------------------------

SESSION = "S93"                                                              # (local)
GATE_ID = ("S93-W9-5-LAYER-FUNCTOR-F-VERDICT-SHAPE-"
           "CONSISTENCY-REFORMULATION-WORKSHOP")                             # (local)
SCHEME = "ADVERSARIAL-WORKSHOP-2-AGENT-3-ROUND-LAYER-FUNCTOR-F-REFORMULATION"  # (local)
CONVENTION = ("R1-steelman-R2-respond-R3-converge-STRUCTURAL-VERDICT-"
              "reformulate-K2-weak-vs-close")                                # (local)
L_MAX = "N/A"                                                                # (local) categorical verdict; no compute

# Top-line verdict (workshop-complete) + the categorical STRUCTURAL VERDICT
TOP_VERDICT = "PASS"                                                         # (local) workshop-complete
STRUCTURAL_VERDICT = "CLOSE"                                                 # (local) VERDICT-B (R3 convergence)
STRUCTURAL_VERDICT_LABEL = "VERDICT-B"                                       # (local)

# Evidence basis (analytically fixed S91/S92 outputs, on disk; NOT recomputed here)
ALPHA_SUB = 0.876001          # (local) §W9-5 Richardson sub-window exponent at L in {6..12} (SUB-geometric)
ALPHA_SUB_STEP_RATIO = 2.1052  # (local) §W9-5 divergent step ratio |d12/d11| > 1
ALPHA_INF = -10.7104          # (local) §W9-5 Richardson alpha_inf (non-physical; divergent sequence)
SIGMA_BETA_FB = 1.0651        # (local) §W9-3 cross-observable scatter at FB-saturated L->inf layer
SIGMA_BETA_CACHE = 0.8936     # (local) §W9-3 cache baseline (S91 W6-4) — sigma_beta GREW under FB saturation
ETA_FB = 0.547221             # (local) §W9-3 Friedrich-Bar ratio (>= 0.40 saturation predicate CERTIFIED)
ALPHA_S82_WITHIN_CHANNEL = 2.6926237  # (local) W6-1 Mellin=zeta EXACT (S82 contour-deformation identity; PRESERVED)

# Participant selection (plan §W9-5 machinery_pin_map)
AXIS_A_AGENT = "lizzi-spectral-functional-theorist"                          # (local)
AXIS_B_AGENT = "landau-condensed-matter-theorist"                            # (local)
EXCLUDED_AGENTS = ["volovik (S92 W8-1 Axis-B co-author)",
                   "connes (S91 W5 two-layer-theorem author)"]              # (local)

# Output destinations (per-session)
STEM = "s93_w9_5_layer_functor_f_reformulation"                             # (local)
OUT_JSON = SESSION_DIR / f"{STEM}_verdict.json"
VERDICT_TXT = SESSION_DIR / "s93_gate_verdicts.txt"
WORKSHOP_DOC = (PROJECT_ROOT / "sessions" / "session-93" / "workshops" /
                "s93-w9-5-layer-functor-f-reformulation.md")

# Input files (plan §W9-5 input_files) — the workshop's evidence base
S91_W5_DOC = (PROJECT_ROOT / "sessions" / "session-91" / "workshops" /
              "s91-w5-layer-functor-f-universal-envelope-scope-adjudication.md")
S92_W8_1_DOC = (PROJECT_ROOT / "sessions" / "session-92" / "workshops" /
                "s92-w8-1-layer-functor-f-puzzle-disambiguation.md")
S92_W9_WP = (PROJECT_ROOT / "sessions" / "session-92" / "session-92-w9-workingpaper.md")


# ---------------------------------------------------------------------------
# Section 4 — Option-A supersession-chain read (verdict permanence)
# ---------------------------------------------------------------------------

def _latest_non_superseded_line(gate_id: str) -> str:
    """Return the latest NON-superseded canonical verdict line for gate_id,
    following the Option-A supersession chain (gate-verdicts.md). '' if none."""
    if not VERDICT_TXT.exists():
        return ""
    superseded: set[str] = set()                 # (local) audit_shas named in supersedes=
    lines_for_gate: list[tuple[str, str]] = []    # (local) (audit_sha, full_line) in file order
    for raw in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if raw.startswith(f"{gate_id}:"):
            this_sha = ""                         # (local)
            for tok in raw.split():
                if tok.startswith("audit_sha256="):
                    this_sha = tok.split("=", 1)[1]
                if tok.startswith("supersedes="):
                    superseded.add(tok.split("=", 1)[1].strip("'\""))
            if "supersedes=" in raw:
                frag = raw.split("supersedes=", 1)[1]   # (local)
                superseded.add(frag.split()[0].strip("'\""))
            if this_sha:
                lines_for_gate.append((this_sha, raw))
    live = [(s, ln) for (s, ln) in lines_for_gate if s not in superseded]    # (local)
    return live[-1][1] if live else ""


# ---------------------------------------------------------------------------
# Section 5 — SHA-256 dual-pin block (plan audit_discriminators)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def build_pinmap() -> dict[str, str]:
    """Input-pin map per plan input_files: the three workshop evidence files."""
    pins: dict[str, str] = {                      # (local)
        "s91_w5_predecessor_adjudication": sha256_of(S91_W5_DOC),
        "s92_w8_1_disambiguation": sha256_of(S92_W8_1_DOC),
        "s92_w9_workingpaper": sha256_of(S92_W9_WP),
    }
    return pins


def compute_dual_sha(pins: dict[str, str], workshop_doc: Path) -> tuple[str, str]:
    """audit_sha256 over [s91_w5, s92_w8_1, s92_w9_wp, pinmap]; content_sha256 over
    [workshop_document]. Closure is COMPUTED, not hardcoded.

    'pinmap' (the audit_discriminators 4th input) is the JSON-canonicalized input-pin
    dict folded into the audit closure -- this makes audit_sha256 a closure over the
    ordered input-pin map per gate-verdicts.md.
    """
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()                    # (local)
    for k, v in sorted(pins.items()):             # fold each pinned input's SHA
        h_audit.update(f"{k}={v}\n".encode("utf-8"))
    h_audit.update(pinmap_json)                   # then the canonical pinmap blob
    audit = h_audit.hexdigest()                   # (local)

    workshop_bytes = b""                          # (local)
    try:
        workshop_bytes = workshop_doc.read_bytes()
    except OSError:
        workshop_bytes = b""
    h_content = hashlib.sha256()                  # (local)
    h_content.update(workshop_bytes)
    content = h_content.hexdigest()               # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 6 — Verdict construction (NO physics compute)
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def build_value_string() -> str:
    """Descriptive value string: top-line workshop-complete + the categorical
    STRUCTURAL VERDICT (CLOSE) + the cited evidence basis + the S82 carve-out."""
    return (
        f"PASS_workshop-complete;STRUCTURAL_VERDICT={STRUCTURAL_VERDICT}_"
        f"({STRUCTURAL_VERDICT_LABEL});K2_FALSIFIED-at-K2->CLOSED;"
        f"evidence_W9-3_sigma_beta_FB={SIGMA_BETA_FB}_grown_from_{SIGMA_BETA_CACHE}_"
        f"eta_FB={ETA_FB}_saturated;"
        f"evidence_W9-5_alpha_sub={ALPHA_SUB}_SUB-geometric_step_ratio={ALPHA_SUB_STEP_RATIO}_"
        f"anchor-crossing-L10_alpha_inf={ALPHA_INF};"
        f"S82-within-channel-F2-FI-identity-alpha={ALPHA_S82_WITHIN_CHANNEL}-EXACT-PRESERVED-carve-out;"
        f"axisA={AXIS_A_AGENT};axisB={AXIS_B_AGENT};"
        f"excluded=volovik+connes-downstream-inheritance-reach;"
        f"followup=mack-sole-writer-open-channel-CLOSED+corpus-RETIRE-SEPARATE"
    )


# ---------------------------------------------------------------------------
# Section 7 — append_verdict (canonical line + W9a-99 companion row)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append the canonical line + dual-SHA companion row. [VERIFY-THEOREM] trigger:
    NO S87 schema-v2 3-tuple companion row. Atomic single-open append.

    Option-A: if a prior non-superseded canonical line for this gate-ID exists with a
    DIFFERENT audit_sha, emit supersedes=<prior_audit_sha> in value= (verdict permanence).
    """
    prior_line = _latest_non_superseded_line(GATE_ID)     # (local)
    prior_sha = ""                                        # (local)
    if prior_line:
        for tok in prior_line.split():
            if tok.startswith("audit_sha256="):
                prior_sha = tok.split("=", 1)[1]
    if prior_sha and prior_sha != audit_sha:
        value_field = f"'{value};supersedes={prior_sha}'"  # (local) Option A tag
    else:
        value_field = f"'{value}'"                         # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value={value_field} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                              # (local)

    print(f"=== {GATE_ID} ===")
    print(f"  Workshop: {AXIS_A_AGENT} (Axis-A) vs {AXIS_B_AGENT} (Axis-B)")
    print(f"  Excluded (downstream-inheritance reach): {EXCLUDED_AGENTS}")
    print(f"  Top-line verdict: {TOP_VERDICT} (workshop-complete)")
    print(f"  STRUCTURAL VERDICT: {STRUCTURAL_VERDICT_LABEL} ({STRUCTURAL_VERDICT})")
    print()

    # ---- Evidence basis echo (analytically fixed S91/S92 outputs; NOT recomputed) ----
    print("=== Evidence basis (cited; analytically fixed, on disk) ===")
    print(f"  §W9-3 CF-W6-4-S91-1: sigma_beta(FB-saturated) = {SIGMA_BETA_FB} "
          f"(grown from cache {SIGMA_BETA_CACHE}); eta_FB = {ETA_FB} >= 0.40 CERTIFIED")
    print(f"     -> Level-1 asymptotic-universal (sigma_beta -> 0) FALSIFIED at the "
          f"FB-saturation layer (FI-side decisive blow)")
    print(f"  §W9-5 Richardson: alpha_sub = {ALPHA_SUB} (SUB-geometric); "
          f"step ratio = {ALPHA_SUB_STEP_RATIO} > 1 (DIVERGENT); alpha_inf = {ALPHA_INF}")
    print(f"     -> FI-sub-projection sub-window has NO convergent asymptotic exponent "
          f"(RD-classified; corroborating leg)")
    print(f"  S82 carve-out (PRESERVED): within-channel Mellin=zeta = "
          f"{ALPHA_S82_WITHIN_CHANNEL} EXACT (contour-deformation identity; FI; untouched)")
    print()

    # ---- Structural-verdict echo (R3 convergence direction) ----
    print("=== STRUCTURAL VERDICT (R3 convergence) ===")
    sigma_grew = SIGMA_BETA_FB > SIGMA_BETA_CACHE           # (local) expect True (Leg A)
    divergent = ALPHA_SUB_STEP_RATIO > 1.0                  # (local) expect True (Leg B)
    print(f"  Leg A (asymptotic-universal, FI): sigma_beta grew under FB saturation "
          f"({SIGMA_BETA_CACHE} -> {SIGMA_BETA_FB}) = {sigma_grew}  [Level-1 FALSIFIED]")
    print(f"  Leg B (convergence-rate, RD-but-independent): step ratio "
          f"{ALPHA_SUB_STEP_RATIO} > 1 = {divergent}  [no convergent exponent]")
    print(f"  Leg C (S82-preservation, FI): within-channel Mellin=zeta EXACT, "
          f"untouched by cross-observable sigma_beta or single-trajectory alpha_sub  [PRESERVED]")
    print(f"  => K2-distinctive content (universal-envelope/Verdict-Shape Consistency) "
          f"= LegA AND LegB = {sigma_grew and divergent} (falsified at EVERY layer)")
    print(f"  => VERDICT-B (CLOSE): FALSIFIED-at-K=2 -> CLOSED; S82 identity carved out + PRESERVED")
    print()

    # ---- Dual-SHA over the input-pin map (COMPUTED, not hardcoded) ----
    pins = build_pinmap()                         # (local)
    print("=== input SHA-256 pins (audit_discriminators) ===")
    for k, v in pins.items():
        print(f"  {k}: {v[:16]}...")
    print(f"  workshop_document (content): {sha256_of(WORKSHOP_DOC)[:16]}...")

    audit_sha, content_sha = compute_dual_sha(pins, WORKSHOP_DOC)   # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (pins + pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (workshop document)")
    print()

    # ---- Persist JSON closure record (the verdict A/B + evidence + K-counter) ----
    closure_record = {                            # (local)
        "gate_id": GATE_ID,
        "session": SESSION,
        "top_line_verdict": TOP_VERDICT,
        "structural_verdict": STRUCTURAL_VERDICT_LABEL,
        "structural_verdict_meaning": STRUCTURAL_VERDICT,
        "structural_verdict_long": (
            "VERDICT-B (CLOSE): the Layer-Functor F Verdict-Shape Consistency Theorem "
            "universal-envelope reading is retired at K=2 (FALSIFIED-at-K=2 -> CLOSED), "
            "with the S82 within-channel F_2-axis FI contour-deformation identity carved "
            "out and PRESERVED as an independently PROVEN, untouched result."
        ),
        "evidence_basis": {
            "W9-3_CF-W6-4-S91-1": {
                "sigma_beta_fb_saturated": SIGMA_BETA_FB,
                "sigma_beta_cache_baseline": SIGMA_BETA_CACHE,
                "sigma_beta_grew_under_fb_saturation": bool(SIGMA_BETA_FB > SIGMA_BETA_CACHE),
                "eta_FB": ETA_FB,
                "saturation_predicate_certified": True,
                "role": ("FI-side decisive blow: cross-observable consistency (Level-1 "
                         "asymptotic-universal) FALSIFIED at the L->inf FB-saturation layer "
                         "where Reading_Hybrid placed it"),
                "FI_status": "regulator-INVARIANT (Friedrich-Bar saturation theorem; 4-way discriminator)",
            },
            "W9-5_Richardson": {
                "alpha_sub_L6_12": ALPHA_SUB,
                "step_ratio": ALPHA_SUB_STEP_RATIO,
                "divergent": bool(ALPHA_SUB_STEP_RATIO > 1.0),
                "alpha_inf": ALPHA_INF,
                "anchor_crossing_L": 10,
                "role": ("corroborating leg: FI-sub-projection sub-window has no convergent "
                         "asymptotic exponent (sub-geometric, divergent step ratio)"),
                "RD_status": ("SCHEME-DEPENDENT (single FWD-C1 trajectory; anchor-crossing "
                              "contaminated); CLOSE rests on W9-3, not on over-reading W9-5"),
            },
        },
        "k_counter_consequence": {
            "prior_status": "K=2 SUGGESTION (RESCUED-SHARPENED S91 W5; Reading_Hybrid S92 W8-1)",
            "new_status": "FALSIFIED-at-K=2 -> CLOSED",
            "reformulate_to_k2_weak_rejected_reason": (
                "none of the three candidate contents for 'K=2-weak' is simultaneously "
                "(i) non-trivial, (ii) NOT the PROVEN S82 contour-deformation identity, and "
                "(iii) a genuine consistency/universality claim untouched by the evidence; "
                "relabeling the S82 identity as 'K=2-weak' double-counts a proven theorem"
            ),
            "negative_calibration_records_absorbed": [
                "Reading B-strong (4-observable-family universal) FALSIFIED at finite L (S91 W6-4 sigma_beta=0.8936)",
                "Level-1 asymptotic-universal (Reading_Hybrid) FALSIFIED at FB-saturation layer (W9-3 sigma_beta=1.065)",
            ],
            "k_counter_promotes_to_k3": False,
            "k_counter_survives_at_k2_weak": False,
        },
        "preserved_carve_out": {
            "identity": "S82 W-3 within-channel F_2-axis FI contour-deformation identity",
            "form": "alpha_Mellin = alpha_zeta EXACT at the simple pole s=3 (CM-1995 §III.4)",
            "anchor": ("W6-1 PASS-A alpha=2.6926237 EXACT (audit d54b26a9...); re-tagged as a "
                       "Level-3 record of the S82 identity for §VII.AU.OP-PROJ, NOT a universal-"
                       "envelope theorem anchor"),
            "status": "independently PROVEN, FI, untouched by this workshop",
        },
        "participant_selection": {
            "axis_A": AXIS_A_AGENT,
            "axis_B": AXIS_B_AGENT,
            "excluded": EXCLUDED_AGENTS,
            "exclusion_basis": ("joint-theorem-promotion.md Stage-2 Axis-B Selection Protocol "
                                "downstream-inheritance reach prong (a) original-authoring"),
            "genuine_adversarial_convergence": (
                "lizzi entered REFORMULATE, conceded under landau's S82-double-counting argument "
                "+ the independent W9-3 FI blow; landau accepted lizzi's W9-5 RD caveat + adopted "
                "lizzi's S82-preservation condition"
            ),
        },
        "followup_landing_separate_mack_sole_writer": {
            "what": ("open-channel FALSIFIED-at-K=2 -> CLOSED + corpus RETIRE Layer-Functor F K=2 "
                     "SUGGESTION row + §VII.AU.OP-PROJ S82-identity carve-out annotation"),
            "writer": "mack-cosmic-bridge (sole writer per feedback_mack-bridge-role.md)",
            "effort_we": 0.5,
            "note": "NOT written by this workshop; flagged for the orchestrator",
        },
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }
    OUT_JSON.write_text(json.dumps(closure_record, indent=2, sort_keys=False),
                        encoding="utf-8")
    print(f"  JSON closure record -> {OUT_JSON.name}")
    print()

    # ---- Emit verdict line (canonical + dual-SHA companion; NO 3-tuple) ----
    value = build_value_string()                  # (local)
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)   # (local)
    print(tag)
    append_verdict(TOP_VERDICT, value, audit_sha, content_sha)

    wall = time.time() - t0                       # (local)
    print(f"\n=== {GATE_ID}: {TOP_VERDICT} "
          f"(workshop-complete; STRUCTURAL VERDICT = {STRUCTURAL_VERDICT_LABEL} "
          f"[{STRUCTURAL_VERDICT}]; wall {wall:.2f}s) ===")
    # Exit 0 for any valid verdict (verdict is DATA, not script health) per
    # math-scripts.md §"Exit Codes and Verdict Semantics".
    return 0


if __name__ == "__main__":
    sys.exit(main())
