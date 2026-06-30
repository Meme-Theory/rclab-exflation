#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W6-2-VII-AZ-OP-PROJ-ELEMENT-4-SUB-CLASS-TAG-REPLACEMENT
==========================================================

Gate: S93-W6-2-VII-AZ-OP-PROJ-ELEMENT-4-SUB-CLASS-TAG-REPLACEMENT  [AUDIT]
Classification: NON-PHONONIC (registry-anatomy / METHODOLOGY-class deferred-pending
                tag-flip adjudication; PASS predicate is artifact-existence-with-
                substantive-content per wave-classification.md M1-M4).
Owner: mack-cosmic-bridge (sole registry writer for §VII entries per
       `feedback_mack-bridge-role.md`).
Plan: sessions/session-plan/session-93-plan-w6.md §W6-2.

═══════════════════════════════════════════════════════════════════════════
WHAT THIS GATE WAS ASKED TO DO vs WHAT THE GROUND TRUTH FORCES
═══════════════════════════════════════════════════════════════════════════

The plan §W6-2 (and the spawn prompt) assert that §W7-5 first-extracted
α_HH^1_emp(s=4) INSIDE the [1.5, 4.0] Wodzicki/Connes d=4 band, and ask for a
tag-flip REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION → STAGE-1-CANDIDATE-FIRST-EXTRACTED,
adjudicating that an INFO-class (band-resident) first-extraction SUFFICES.

GROUND TRUTH (read from the §W7-5 npz on disk + the §W7-5 verdict line; NOT recomputed):
  - s92_w7_5_hh_1_first_extraction_s4.npz:
        alpha_HH1_emp_s4         -> 0.19431228     (the empirically first-extracted exponent)
        ALPHA_PASS_BAND_LOW      -> 1.5            (band lower edge)
        ALPHA_PASS_BAND_HIGH     -> 4.0            (band upper edge)
        sub_a_in_band            -> False          (band-membership FAILED)
        abs_diff_from_target     = 3.80568772      (from Wodzicki anchor α=4)
        composite=INFO  sign_verdict=PASS  magnitude_verdict=INFO  regime_verdict=VALID
  - §W7-5 verdict line (computations/session-92/s92_gate_verdicts.txt:191):
        value='...alpha_HH1_emp_s4=0.194312; ... in_pass_band_1p5_to_4p0=False; ...' | INFO

  => The §W7-5 extraction is 0.194312, which lies in (0, 1.5) — BELOW the band's
     lower edge 1.5. It is NOT band-resident. The §W7-5 INFO is the producing-script's
     pre-registered "out-of-band but direction-correct" INFO
     (s92 script Section 11 line 589: magnitude_verdict='INFO'  # envelope too coarse),
     NOT a "band-resident INFO". The spawn-prompt / plan premise
     "first-extracted ... inside the [1.5,4.0] band" is FACTUALLY FALSE — a plan-authoring
     premise defect (SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE per
     epistemic-discipline.md §"Source Reconciliation": the plan tested against a stale /
     incorrect view of the §W7-5 result).

═══════════════════════════════════════════════════════════════════════════
INFO-vs-PASS SUFFICIENCY ADJUDICATION (pre-registered reading; explicit)
═══════════════════════════════════════════════════════════════════════════

Two structurally distinct predicates the plan conflates:

  Predicate 1 — FIRST-EXTRACTION sub-class discharge:
    Per cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class",
    REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION = "Level-2 envelope SYMBOLIC-only
    (no numerical anchor); PENDING first extraction via L_max scan / Friedrich-Bär
    saturation / closed-form residue." The LITERAL discharge predicate is "a numerical
    anchor now exists (no longer symbolic-only)". §W7-5 DID produce a numerical α=0.194312
    via L_max scan, so the BARE symbolic-only condition is now FALSE.

  Predicate 2 — the extracted α must REALIZE an ADMISSIBLE envelope:
    The W6-2 gate's own pre-registered strict_PASS_boundary (plan §W6-2 line 302) requires
    band-residence as the FIRST conjunct of PASS: "α_HH^1_emp(s=4) band-resident in [1.5,4.0]
    (verified from §W7-5 npz) AND the §VII.AZ.OP-PROJ Element-4 tag flipped...". The plan's own
    substitution chain Step 4 makes band-membership the admissibility gate: "The band-membership
    confirms the realized α is physically admissible (in the Wodzicki/Connes d=4 range)".
    The actual α=0.194312 is NOT in [1.5,4.0] => NOT admissible.

  ADJUDICATED READING (the answer to the pre-registered INFO-vs-PASS question):
    INFO-class band-RESIDENCE WOULD suffice to flip to STAGE-1-CANDIDATE-FIRST-EXTRACTED
    (envelope-REALIZATION, distinct from Level-3 anchor-singleness). BUT band-residence is
    a NECESSARY conjunct of the discharge, and it is FALSE here. An out-of-band extraction is
    a numerical anchor that the substrate's OWN admissibility criterion (the Wodzicki/Connes d=4
    band) REJECTS; it does NOT realize an ADMISSIBLE envelope. The §W7-5 INFO is the out-of-band
    "envelope-too-coarse" INFO, NOT the "band-resident INFO" the plan assumed.
    => The discharge predicate is NOT satisfied. The tag does NOT flip.

  This is exactly the gate's pre-registered FAIL_meaning (plan §W6-2 lines 420-425):
    "α_HH^1_emp(s=4) is NOT band-resident in [1.5,4.0] ... the tag must STAY at
     REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION — the bridge entry is registry-incomplete
     on Sub-claim B until a band-admissible α is extracted."

═══════════════════════════════════════════════════════════════════════════
SUBSTITUTION CHAIN (math-scripts.md §"Double-Check Logic Before Compute")
═══════════════════════════════════════════════════════════════════════════

Claim: an INFO-class first-extraction does NOT discharge FIRST-EXTRACTION when it is
       OUT-OF-BAND; the §VII.AZ Sub-claim-B Element-4 tag STAYS at
       REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION.

  Step 1: discharge predicate = (numerical α exists)  AND  (α realizes an ADMISSIBLE envelope).
          The admissibility criterion is the Wodzicki/Connes d=4 band [1.5, 4.0]
          (the substrate's own per-pole admissibility; analytic anchor α=2(s−2)=4 at s=4,
          canonical alpha_HH1_per_pole_FW_s4=4.0).
  Step 2: §W7-5 RESULT: α=0.194312 (numerical exists ⇒ first conjunct TRUE);
          sub_a_in_band=False, 0.194312 ∉ [1.5,4.0] ⇒ second conjunct FALSE.
  Step 3: Substitute: discharge_predicate = TRUE ∧ FALSE = FALSE.
  Step 4: direction read-off: a numerical-but-out-of-band α does NOT realize an admissible
          envelope; the bridge stays registry-INCOMPLETE on Sub-claim B. The §W7-5 INFO
          (sign=PASS direction-correct, magnitude=INFO out-of-band) confirms the extraction
          is direction-correct but the magnitude is 3.806 away from the d=4 anchor —
          "envelope too coarse", not admissible.
  Conclusion: tag STAYS REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION. The flip to
              STAGE-1-CANDIDATE-FIRST-EXTRACTED is NOT licensed on the actual §W7-5 data.
              Flipping it on the (false) plan premise would be PROHIBITED_ACTIONS Class-4
              (ansatz-forced PASS) / Class-1 (convention-shopping). Direction: substrate
              first-extraction admissibility → tag standing; NEVER infer a tag-flip from a
              plan premise contradicted by the ground-truth npz.

═══════════════════════════════════════════════════════════════════════════
CONSEQUENCE FOR THE REGISTRY WRITE
═══════════════════════════════════════════════════════════════════════════

The registry write is a VERIFIED NO-OP: the §VII.AZ.OP-PROJ Sub-claim-B Element-4 tag is
CONFIRMED UNCHANGED at REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (both the Level-2 ladder
row AND the Element-4 envelope text retain the tag; the STAGE-1-CANDIDATE-FIRST-EXTRACTED
target string is CONFIRMED ABSENT). The gate verdict is FAIL (the tag-flip is not warranted).
FAIL is a valid scientific result per `math-scripts.md §"All Results Are Good Results"` —
it closes the "INFO-out-of-band discharges FIRST-EXTRACTION" corridor and records that a
BAND-ADMISSIBLE re-extraction is the discharge prerequisite (carry-forward).

The Stage-1/2/3 promotion pathway is untouched regardless: §VII.AZ.OP-PROJ remains
STAGE-3-PERMANENT-eligible on Sub-claim A (S91 W8-4 Stage-2 PASS-AND), and the Sub-claim-B
sub-class tag lives at the Element-4 envelope-extraction layer per the registry
SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM structure.

═══════════════════════════════════════════════════════════════════════════
SINGLE-SHOT AFTER PATTERN (registry-landing.md §"Bridge-Landing Script Architecture")
═══════════════════════════════════════════════════════════════════════════

read registry -> (no replacement: the flip is not warranted) -> NO write -> re-read +
verify the tag is STILL REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION and the FIRST-EXTRACTED
target is ABSENT -> emit exactly one FAIL verdict line. The §VII.AZ slot is resolved by
CONTENT (heading-anchor + unique Element-4 tag substrings), NOT the plan-pinned line ~19400 /
~19438 (STALE-drifted to ~19735 / ~19762/19773 per substrate-first-canonical-sourcing.md §(ii.B)).

Verdict file: computations/session-93/s93_gate_verdicts.txt
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU-only (npz read + registry text scan + SHA; no linalg)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent  # (local) project root
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

# Per computations/_shared/CLAUDE.md ALL scripts MUST import canonical_constants.
from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import M_KK, tau_fold, alpha_HH1_per_pole_FW_s4  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity + canonical paths
# ---------------------------------------------------------------------------
GATE_ID = "S93-W6-2-VII-AZ-OP-PROJ-ELEMENT-4-SUB-CLASS-TAG-REPLACEMENT"  # (local)
SCHEME = "FW"  # (local)
CONVENTION = "registry-tag-flip-FIRST-EXTRACTION-to-FIRST-EXTRACTED-INFO-sufficiency-adjudicated"  # (local) plan-pinned convention
L_MAX = "N/A"  # (local) registry/METHODOLOGY tag-flip adjudication; no L_max
SCHEMA_VERSION = "S84+"  # (local)

SESSION_DIR = ROOT / "computations" / "session-93"  # (local)
OUT_NPZ = SESSION_DIR / "s93_w6_2_vii_az_op_proj_element_4_sub_class_tag_replacement.npz"  # (local)
OUT_PNG = SESSION_DIR / "s93_w6_2_vii_az_op_proj_element_4_sub_class_tag_replacement.png"  # (local)
OUT_JSON = SESSION_DIR / "s93_w6_2_vii_az_op_proj_element_4_sub_class_tag_replacement.json"  # (local)
VERDICT_FILE = SESSION_DIR / "s93_gate_verdicts.txt"  # (local)

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"  # (local)
W7_5_NPZ = ROOT / "computations" / "session-92" / "s92_w7_5_hh_1_first_extraction_s4.npz"  # (local)
SCRIPT_PATH = Path(__file__).resolve()  # (local)

# ---------------------------------------------------------------------------
# Pre-registered band + analytic anchor (plan §W6-2 + canonical_constants)
# ---------------------------------------------------------------------------
BAND_LO = 1.5  # (local) plan §W6-2 ALPHA_PASS_BAND_LOW (= §W7-5 npz ALPHA_PASS_BAND_LOW)
BAND_HI = 4.0  # (local) plan §W6-2 ALPHA_PASS_BAND_HIGH (= §W7-5 npz ALPHA_PASS_BAND_HIGH)
ANALYTIC_ANCHOR_ALPHA = float(alpha_HH1_per_pole_FW_s4)  # (local) canonical: Wodzicki/Connes d=4 α=2(s−2)=4 at s=4

# ---------------------------------------------------------------------------
# Tag strings (the deferred-pending sub-class tags)
# ---------------------------------------------------------------------------
TAG_PENDING = "REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION"  # (local) the CURRENT Sub-claim-B Element-4 tag
TAG_EXTRACTED = "STAGE-1-CANDIDATE-FIRST-EXTRACTED"  # (local) the (NOT-warranted) flip target

# ---------------------------------------------------------------------------
# Registry CONTENT anchors for §VII.AZ.OP-PROJ Sub-claim-B Element-4
# (resolve by CONTENT, NOT plan-pinned ~19400/~19438 STALE-drifted lines).
# ---------------------------------------------------------------------------
AZ_HDR_MARKER = "### §VII.AZ.OP-PROJ — Cross-Morphism M_3(ℂ)-Kernel Universality"  # (local) §VII.AZ heading (content-anchored)

# Element-4 tag context: the Level-2-A operational-finite-α envelope at the Sub-claim-B HH^1
# observable. Two on-disk occurrences carry the tag inside the §VII.AZ block; both are unique
# substrings (the Level-2 ladder row + the Element-4 envelope paragraph).
ELEM4_ENVELOPE_TAG_CONTEXT = (  # (local) Element-4 envelope paragraph occurrence (line ~19773)
    "**REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION** sub-class tag applies per "
    "`cross-pillar-bridge-anatomy.md §\"Deferred-pending intermediate verdict-class"
)
LEVEL2_ROW_TAG_CONTEXT = (  # (local) Level-2 ladder row occurrence (line ~19762)
    "Level-2-A **REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION** sub-class tag at "
    "Sub-claim B HH^1 observable"
)


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 76)
    print(f"Gate: {GATE_ID}")
    print("=" * 76)
    print("Input SHA-256 pins (first lines of stdout):")
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        rel = str(p.relative_to(ROOT)).replace("\\", "/") if p.exists() else str(p)
        print(f"  {name:30s} = {sha[:16]}...  ({rel})")
    return pins


def extract_az_block(registry_text: str) -> str:
    """Extract the §VII.AZ.OP-PROJ entry block (from its `### §VII.AZ.OP-PROJ` heading to the
    next `### §VII.` heading) for the content_sha256 leg. Content-anchored, NOT line-pinned
    (drift-robust per substrate-first-canonical-sourcing.md §(ii.B)). Returns '' if absent.
    """
    start = registry_text.find(AZ_HDR_MARKER)  # (local)
    if start < 0:
        return ""
    rest = registry_text[start + len(AZ_HDR_MARKER):]  # (local)
    nxt = rest.find("\n### §VII.")  # (local) next §VII entry heading
    block = AZ_HDR_MARKER + (rest if nxt < 0 else rest[:nxt])  # (local)
    return block


def compute_dual_sha(pins: dict, az_block_text: str, w7_5_facts: dict) -> tuple[str, str]:
    """Dual-SHA per S84+ schema.
    content_sha256 = SHA over the (re-read) §VII.AZ.OP-PROJ entry block (the artifact whose
      state-with-content IS the METHODOLOGY-class predicate; here CONFIRMED UNCHANGED).
    audit_sha256   = SHA over the input-pin map + the §W7-5 ground-truth facts + per-gate
      identity keys (gate-distinct per mechanical-closure-discipline.md item 3).
    """
    h_content = hashlib.sha256()  # (local)
    h_content.update(az_block_text.encode("utf-8"))
    content = h_content.hexdigest()  # (local)

    pinmap_json = json.dumps(dict(sorted(pins.items())), sort_keys=True).encode("utf-8")  # (local)
    facts_json = json.dumps(dict(sorted(w7_5_facts.items())), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(pinmap_json)
    h_audit.update(facts_json)
    h_audit.update(f"{GATE_ID}|{SCHEME}|{CONVENTION}|L_max={L_MAX}".encode("utf-8"))
    audit = h_audit.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Option-A supersedes source (latest non-superseded prior line for this gate-ID)
# ---------------------------------------------------------------------------
def find_latest_prior_audit_sha() -> str | None:
    if not VERDICT_FILE.exists():
        return None
    superseded: set[str] = set()  # (local)
    candidates: list[str] = []  # (local)
    for ln in VERDICT_FILE.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:") and "audit_sha256=" in ln:
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                candidates.append(m.group(1))
            sm = re.search(r"supersedes=([a-f0-9]{64})", ln)  # (local)
            if sm:
                superseded.add(sm.group(1))
    live = [c for c in candidates if c not in superseded]  # (local)
    return live[-1] if live else None


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   supersedes: str | None = None) -> None:
    """Single canonical dual-SHA verdict line + companion row. METHODOLOGY/registry tag-flip
    adjudication; [AUDIT] — no [SIGN] 3-tuple (band-membership + tag standing, not a
    sign/direction prediction; plan §W6-2 schema_v2_3tuple_required: false). Append-only
    single open("a") write.
    """
    value_field = value_str if supersedes is None else f"{value_str};supersedes={supersedes}"  # (local)
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); METHODOLOGY-class mack-cosmic-bridge "
        f"sole-writer §VII.AZ.OP-PROJ Sub-claim-B Element-4 tag-flip ADJUDICATION; verdict FAIL — "
        f"§W7-5 alpha_HH1_emp_s4=0.194312 OUT-of-band [1.5,4.0] (in_pass_band=False); tag STAYS "
        f"REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (registry NO-OP, tag confirmed unchanged); "
        f"plan/spawn premise 'inside band' is FALSE (SOURCE-RECON Class-(c) stale-source); INFO "
        f"band-residence WOULD suffice but α NOT band-resident; [AUDIT] no [SIGN] 3-tuple{supersedes_note}\n"
    )
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    input_files = {
        "w7_5_npz": W7_5_NPZ,
        "canonical_constants": CANONICAL_CONSTANTS,
        "permanent_results_registry": REGISTRY,
        "script": SCRIPT_PATH,
    }
    pins = log_input_pins(input_files)

    # ------------------------------------------------------------------
    # 1. Load §W7-5 ground-truth first-extraction result (NOT recomputed)
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("§W7-5 ground-truth first-extraction (read from npz; NOT recomputed)")
    print("=" * 76)
    if not W7_5_NPZ.exists():
        print(f"ERROR: §W7-5 npz not found at {W7_5_NPZ}")
        return 1
    d = np.load(W7_5_NPZ, allow_pickle=True)  # (local)
    alpha_emp_s4 = float(d["alpha_HH1_emp_s4"])  # (local)
    npz_band_lo = float(d["ALPHA_PASS_BAND_LOW"])  # (local)
    npz_band_hi = float(d["ALPHA_PASS_BAND_HIGH"])  # (local)
    npz_sub_a_in_band = bool(d["sub_a_in_band"])  # (local)
    npz_abs_diff = float(d["abs_diff_from_target"])  # (local)
    npz_composite = str(d["composite"])  # (local)
    npz_sign = str(d["sign_verdict"])  # (local)
    npz_magnitude = str(d["magnitude_verdict"])  # (local)
    npz_regime = str(d["regime_verdict"])  # (local)

    print(f"  alpha_HH1_emp_s4       = {alpha_emp_s4:.6f}")
    print(f"  npz band               = [{npz_band_lo}, {npz_band_hi}]")
    print(f"  npz sub_a_in_band      = {npz_sub_a_in_band}")
    print(f"  abs_diff_from_target   = {npz_abs_diff:.6f}  (analytic anchor α={ANALYTIC_ANCHOR_ALPHA})")
    print(f"  §W7-5 composite/sign/magnitude/regime = "
          f"{npz_composite}/{npz_sign}/{npz_magnitude}/{npz_regime}")

    # Independent band-membership recompute (sanity cross-check against the npz flag)
    band_resident_recompute = (BAND_LO <= alpha_emp_s4 <= BAND_HI)  # (local)
    band_consistent = (band_resident_recompute == npz_sub_a_in_band)  # (local) npz flag matches recompute
    print(f"  band-membership recompute ({BAND_LO} <= {alpha_emp_s4:.6f} <= {BAND_HI}) = "
          f"{band_resident_recompute}  (npz flag consistent: {band_consistent})")

    # ------------------------------------------------------------------
    # 2. INFO-vs-PASS sufficiency adjudication (pre-registered reading)
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("INFO-vs-PASS sufficiency adjudication (pre-registered reading)")
    print("=" * 76)
    numerical_anchor_exists = np.isfinite(alpha_emp_s4)  # (local) FIRST-EXTRACTION literal predicate 1: no longer symbolic-only
    direction_correct = (alpha_emp_s4 > 0) and (npz_sign == "PASS")  # (local) substrate-physics direction
    band_admissible = band_resident_recompute  # (local) discharge predicate 2: α realizes an ADMISSIBLE envelope
    # The deferred-pending FIRST-EXTRACTION discharge requires BOTH a numerical anchor AND that
    # the anchor realize an ADMISSIBLE envelope (band-resident in the Wodzicki/Connes d=4 range).
    discharge_predicate = numerical_anchor_exists and band_admissible  # (local)
    # INFO band-residence WOULD suffice for the flip; but band-residence is a NECESSARY conjunct.
    info_suffices_IF_band_resident = True  # (local) the adjudicated reading (counterfactual; admissible-INFO discharges)
    info_suffices_for_discharge = discharge_predicate  # (local) ACTUAL: requires band-residence, which is False here
    print(f"  numerical_anchor_exists (no longer symbolic-only) = {numerical_anchor_exists}")
    print(f"  direction_correct (α>0 ∧ sign=PASS)               = {direction_correct}")
    print(f"  band_admissible (α ∈ [1.5,4.0])                    = {band_admissible}")
    print(f"  --> adjudicated reading: INFO-band-residence SUFFICES IF band-resident = {info_suffices_IF_band_resident}")
    print(f"  --> ACTUAL discharge_predicate (numerical ∧ admissible) = {discharge_predicate}")
    print("  --> §W7-5 INFO is the OUT-OF-BAND 'envelope-too-coarse' INFO (sign=PASS, magnitude=INFO),")
    print("      NOT a band-resident INFO; it does NOT realize an admissible envelope.")

    tag_flip_warranted = discharge_predicate  # (local) flip iff the discharge predicate holds
    tag_after = TAG_EXTRACTED if tag_flip_warranted else TAG_PENDING  # (local)
    print(f"  tag_flip_warranted = {tag_flip_warranted}")
    print(f"  tag_before = {TAG_PENDING}")
    print(f"  tag_after  = {tag_after}  ({'FLIP' if tag_flip_warranted else 'STAYS — NO-OP'})")

    # ------------------------------------------------------------------
    # 3. Plan/spawn premise defect disclosure (SOURCE-RECON Class-(c))
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("Plan/spawn premise defect (SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE)")
    print("=" * 76)
    plan_premise_band_resident = True  # (local) what plan §W6-2 + spawn prompt ASSERTED
    premise_defect_detected = (plan_premise_band_resident != band_resident_recompute)  # (local)
    print(f"  plan/spawn premise 'first-extracted INSIDE [1.5,4.0]' = {plan_premise_band_resident}")
    print(f"  ground-truth band-residence (npz)                    = {band_resident_recompute}")
    print(f"  premise_defect_detected                              = {premise_defect_detected}")
    print("  => the plan §W6-2 PASS rubric was built on a FALSE premise; the gate's own pre-registered")
    print("     FAIL_meaning (plan lines 420-425) governs: tag STAYS REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION.")

    # ------------------------------------------------------------------
    # 4. Read registry; resolve §VII.AZ by CONTENT (drift-corrected)
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("Registry read + §VII.AZ content-anchor resolution (drift-corrected)")
    print("=" * 76)
    print("  plan-pinned §VII.AZ heading line ~19400 / Element-4 tag ~19438 = STALE plan-frozen refs.")
    registry_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    az_present = AZ_HDR_MARKER in registry_text  # (local)
    # Resolve the runtime line of the §VII.AZ heading (for the drift note in value=)
    az_line_runtime = -1  # (local)
    for i, ln in enumerate(registry_text.splitlines(), start=1):
        if ln.startswith(AZ_HDR_MARKER):
            az_line_runtime = i
            break
    print(f"  §VII.AZ.OP-PROJ heading present = {az_present}; runtime line = {az_line_runtime} "
          f"(plan-pinned ~19400; drift +{az_line_runtime - 19400 if az_line_runtime > 0 else 'N/A'})")
    elem4_envelope_tag_found = ELEM4_ENVELOPE_TAG_CONTEXT in registry_text  # (local)
    level2_row_tag_found = LEVEL2_ROW_TAG_CONTEXT in registry_text  # (local)
    print(f"  Element-4 envelope tag context found = {elem4_envelope_tag_found}")
    print(f"  Level-2 ladder row tag context found = {level2_row_tag_found}")

    # ------------------------------------------------------------------
    # 5. Registry write = VERIFIED NO-OP (the flip is NOT warranted)
    #    Single-shot AFTER pattern: no replacement -> no write -> re-read + verify
    #    the tag is STILL the PENDING tag and the FIRST-EXTRACTED target is ABSENT.
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("Registry write decision (single-shot AFTER pattern)")
    print("=" * 76)
    if tag_flip_warranted:
        # NOT reached on the actual §W7-5 data; guarded for structural completeness only.
        print("  tag_flip_warranted=True would flip here — NOT the case on §W7-5 ground truth.")
        new_text = registry_text  # (local) (no actual flip implemented; would be a separate gate)
    else:
        print("  tag_flip NOT warranted (α out-of-band) => registry write is a NO-OP.")
        print("  Confirming the §VII.AZ Sub-claim-B Element-4 tag STAYS REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION.")
        new_text = registry_text  # (local)

    changed = new_text != registry_text  # (local) expected False (NO-OP)
    print(f"  registry text changed this run = {changed} (expected False for the NO-OP)")
    # NO write (changed is False); single-shot AFTER pattern re-reads disk to verify.

    # ------------------------------------------------------------------
    # 6. FINAL verification step (determines the verdict)
    #    Verdict FAIL iff the tag-flip is not warranted AND the registry correctly
    #    still carries the PENDING tag (NO-OP integrity) AND the FIRST-EXTRACTED target absent.
    # ------------------------------------------------------------------
    print("\n" + "=" * 76)
    print("Re-read + verify §VII.AZ Element-4 tag standing on-disk (single point of decision)")
    print("=" * 76)
    disk_text = REGISTRY.read_text(encoding="utf-8")  # (local)
    az_block = extract_az_block(disk_text)  # (local)
    pending_tag_in_block = TAG_PENDING in az_block  # (local) PENDING tag still present in §VII.AZ block
    elem4_envelope_tag_in_block = ELEM4_ENVELOPE_TAG_CONTEXT in az_block  # (local)
    level2_row_tag_in_block = LEVEL2_ROW_TAG_CONTEXT in az_block  # (local)
    # The FIRST-EXTRACTED flip target must NOT have been introduced at the §VII.AZ Element-4
    # Sub-claim-B HH^1 context (it would be present only if the flip had been (wrongly) applied).
    extracted_target_absent_at_elem4 = TAG_EXTRACTED not in az_block  # (local)
    az_block_word_count = len(az_block.split())  # (local)
    print(f"  PENDING tag present in §VII.AZ block          = {pending_tag_in_block}")
    print(f"  Element-4 envelope tag present in block       = {elem4_envelope_tag_in_block}")
    print(f"  Level-2 ladder row tag present in block       = {level2_row_tag_in_block}")
    print(f"  FIRST-EXTRACTED target ABSENT in §VII.AZ block = {extracted_target_absent_at_elem4}")
    print(f"  §VII.AZ block word count                      = {az_block_word_count}")

    # NO-OP integrity: the registry is unchanged AND the tag standing is exactly the PENDING tag.
    no_op_integrity = (
        (not changed)
        and az_present
        and pending_tag_in_block
        and elem4_envelope_tag_in_block
        and level2_row_tag_in_block
        and extracted_target_absent_at_elem4
        and (az_block_word_count >= 15)
    )  # (local)

    # Verdict: the gate's pre-registered PASS requires band-residence (FALSE here), so the
    # gate FAILs (per its own FAIL_meaning). The FAIL is the CORRECT, honest mapping; the
    # registry NO-OP integrity confirms the tag was NOT (wrongly) flipped.
    verdict = "PASS" if tag_flip_warranted and changed else "FAIL"  # (local)
    print(f"\n  tag_flip_warranted = {tag_flip_warranted}  =>  verdict = {verdict}")
    print(f"  NO-OP integrity (registry unchanged ∧ PENDING tag intact ∧ FIRST-EXTRACTED absent) = {no_op_integrity}")

    if verdict != "FAIL":
        # Structural guard: on the §W7-5 data the verdict MUST be FAIL.
        print("  WARNING: unexpected non-FAIL verdict on out-of-band data — re-check ground truth.")

    # ------------------------------------------------------------------
    # 7. value string
    # ------------------------------------------------------------------
    value_str = (  # (local)
        f"TAG-FLIP-NOT-WARRANTED_tag_STAYS_{TAG_PENDING}_"
        f"alpha_HH1_emp_s4={alpha_emp_s4:.6f}_band=[{BAND_LO},{BAND_HI}]_"
        f"band_resident={band_resident_recompute}_in_pass_band_npz={npz_sub_a_in_band}_"
        f"abs_diff_from_anchor_alpha4={npz_abs_diff:.6f}_"
        f"w7_5_composite={npz_composite}_sign={npz_sign}_magnitude={npz_magnitude}_regime={npz_regime}_"
        f"INFO_vs_PASS_adjudication=INFO-band-residence-WOULD-suffice-BUT-alpha-NOT-band-resident_"
        f"discharge_predicate=numerical_AND_admissible=FALSE_"
        f"numerical_anchor_exists={numerical_anchor_exists}_band_admissible={band_admissible}_"
        f"plan_spawn_premise_inside_band=FALSE_SOURCE-RECON-class-c-stale-source_premise_defect={premise_defect_detected}_"
        f"stage_pathway_untouched=True_sub_claim_A_STAGE-3-eligible_independent_"
        f"registry_NO-OP_tag_unchanged_pending_tag_in_block={pending_tag_in_block}_"
        f"first_extracted_target_absent={extracted_target_absent_at_elem4}_no_op_integrity={no_op_integrity};"
        f"az_heading_runtime_line={az_line_runtime}_plan_pinned_19400_stale_drifted_resolved_by_content;"
        f"band_resident_recompute_consistent_with_npz_flag={band_consistent};"
        f"carry_forward=band_admissible_re-extraction_required_to_discharge_FIRST-EXTRACTION;"
        f"M4_allowlist_append=ORCHESTRATOR-ONLY"
    )

    # ------------------------------------------------------------------
    # 8. dual-SHA over the verified (unchanged) §VII.AZ block + ground-truth facts
    # ------------------------------------------------------------------
    w7_5_facts = {  # (local) the §W7-5 ground-truth facts pinned into audit_sha256
        "alpha_HH1_emp_s4": f"{alpha_emp_s4:.12f}",
        "band_lo": str(BAND_LO),
        "band_hi": str(BAND_HI),
        "sub_a_in_band": str(npz_sub_a_in_band),
        "abs_diff_from_target": f"{npz_abs_diff:.12f}",
        "w7_5_composite": npz_composite,
        "w7_5_sign": npz_sign,
        "w7_5_magnitude": npz_magnitude,
        "w7_5_regime": npz_regime,
        "tag_flip_warranted": str(tag_flip_warranted),
        "tag_after": tag_after,
    }
    audit_sha, content_sha = compute_dual_sha(pins, az_block, w7_5_facts)  # (local)
    supersedes = find_latest_prior_audit_sha()  # (local) None on first emission
    if supersedes:
        print(f"  prior verdict line detected; emitting corrective line with supersedes={supersedes[:16]}...")

    # ------------------------------------------------------------------
    # 9. artifacts (npz + json + png) BEFORE verdict emission
    # ------------------------------------------------------------------
    _emit_npz_and_json(
        alpha_emp_s4, band_resident_recompute, npz_sub_a_in_band, npz_abs_diff,
        npz_composite, npz_sign, npz_magnitude, npz_regime,
        numerical_anchor_exists, band_admissible, discharge_predicate,
        info_suffices_IF_band_resident, info_suffices_for_discharge,
        tag_flip_warranted, tag_after, premise_defect_detected,
        no_op_integrity, pending_tag_in_block, extracted_target_absent_at_elem4,
        az_line_runtime, verdict, value_str, audit_sha, content_sha, supersedes,
    )
    _emit_plot(alpha_emp_s4, verdict)

    # ------------------------------------------------------------------
    # 10. emit verdict line (exactly one canonical + companion)
    # ------------------------------------------------------------------
    append_verdict(verdict, value_str, audit_sha, content_sha, supersedes=supersedes)
    print(f"\n  4-tuple: (value=<...>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  audit_sha256={audit_sha}")
    print(f"  content_sha256={content_sha}")
    print(f"\n  >>> VERDICT: {verdict}")
    print(f"  §W7-5 alpha_HH1_emp_s4={alpha_emp_s4:.6f} is OUT of band [{BAND_LO},{BAND_HI}] (in_pass_band=False).")
    print(f"  §VII.AZ.OP-PROJ Sub-claim-B Element-4 tag STAYS {TAG_PENDING} (registry NO-OP).")
    print("  INFO-vs-PASS adjudication: INFO-band-residence WOULD suffice, but α is NOT band-resident,")
    print("    so the FIRST-EXTRACTION sub-class is NOT discharged (the §W7-5 INFO is out-of-band).")
    print("  Plan/spawn premise 'inside band' is FALSE (SOURCE-RECON Class-(c) stale-source premise defect).")
    print("  Stage-1/2/3 promotion pathway UNTOUCHED (§VII.AZ STAGE-3-eligible on Sub-claim A independently).")
    print("  Carry-forward: a BAND-ADMISSIBLE re-extraction of α_HH^1_emp(s=4) is required to discharge.")
    print("  M4 allowlist append = ORCHESTRATOR-ONLY (flagged in WP §W6-2).")
    return 0  # verdict is DATA; exit 0 regardless of PASS/FAIL (math-scripts.md §"Exit Codes")


def _emit_npz_and_json(alpha_emp_s4, band_resident, npz_sub_a_in_band, npz_abs_diff,
                       npz_composite, npz_sign, npz_magnitude, npz_regime,
                       numerical_anchor_exists, band_admissible, discharge_predicate,
                       info_suffices_IF_band_resident, info_suffices_for_discharge,
                       tag_flip_warranted, tag_after, premise_defect_detected,
                       no_op_integrity, pending_tag_in_block, extracted_target_absent,
                       az_line_runtime, verdict, value_str, audit_sha, content_sha, supersedes):
    np.savez(
        OUT_NPZ,
        # §W7-5 ground-truth (read, not recomputed)
        alpha_HH1_emp_s4=np.float64(alpha_emp_s4),
        band_lo=np.float64(BAND_LO),
        band_hi=np.float64(BAND_HI),
        band_resident=np.bool_(band_resident),
        npz_sub_a_in_band=np.bool_(npz_sub_a_in_band),
        analytic_anchor_alpha=np.float64(ANALYTIC_ANCHOR_ALPHA),
        abs_diff_from_target=np.float64(npz_abs_diff),
        w7_5_composite=str(npz_composite),
        w7_5_sign_verdict=str(npz_sign),
        w7_5_magnitude_verdict=str(npz_magnitude),
        w7_5_regime_verdict=str(npz_regime),
        # adjudication
        numerical_anchor_exists=np.bool_(numerical_anchor_exists),
        band_admissible=np.bool_(band_admissible),
        discharge_predicate=np.bool_(discharge_predicate),
        info_suffices_IF_band_resident=np.bool_(info_suffices_IF_band_resident),
        info_suffices_for_discharge=np.bool_(info_suffices_for_discharge),
        tag_flip_warranted=np.bool_(tag_flip_warranted),
        tag_before=str(TAG_PENDING),
        tag_after=str(tag_after),
        # premise defect
        plan_spawn_premise_band_resident=np.bool_(True),
        premise_defect_detected=np.bool_(premise_defect_detected),
        premise_defect_class="SOURCE-RECON-class-c-PIN-DRIFT-FROM-STALE-SOURCE",
        # NO-OP integrity
        registry_no_op=np.bool_(True),
        no_op_integrity=np.bool_(no_op_integrity),
        pending_tag_in_block=np.bool_(pending_tag_in_block),
        first_extracted_target_absent=np.bool_(extracted_target_absent),
        stage_pathway_untouched=np.bool_(True),
        registry_line_resolved_at_runtime=np.int64(az_line_runtime),
        slot_resolution="content-anchored-NOT-plan-pinned-line-19400-stale-drifted",
        # metadata
        L_max=str(L_MAX),
        tau_fold=np.float64(tau_fold),
        M_KK=np.float64(M_KK),
        verdict=str(verdict),
        scheme=SCHEME,
        convention=CONVENTION,
        gate_id=GATE_ID,
        audit_sha256=str(audit_sha),
        content_sha256=str(content_sha),
        supersedes=str(supersedes) if supersedes else "NONE-first-emission",
        m1_artifact_existence_with_content=np.bool_(True),
        m4_allowlist="ORCHESTRATOR-ONLY",
    )
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")
    _chk = np.load(OUT_NPZ, allow_pickle=True)  # (local)
    rt_ok = (bool(_chk["band_resident"]) == band_resident)  # (local) round-trip integrity
    print(f"  round-trip: npz band_resident preserved: {rt_ok}")

    record = {  # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "supersedes": supersedes if supersedes else "NONE (first emission)",
        "task": ("mack-cosmic-bridge §VII.AZ.OP-PROJ Sub-claim-B Element-4 deferred-pending "
                 "tag-flip ADJUDICATION (REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION -> "
                 "STAGE-1-CANDIDATE-FIRST-EXTRACTED requested; NOT warranted on ground truth)"),
        "w7_5_ground_truth": {
            "alpha_HH1_emp_s4": alpha_emp_s4,
            "band": [BAND_LO, BAND_HI],
            "band_resident": band_resident,
            "in_pass_band_npz_flag": npz_sub_a_in_band,
            "abs_diff_from_anchor_alpha_4": npz_abs_diff,
            "composite": npz_composite,
            "sign_verdict": npz_sign,
            "magnitude_verdict": npz_magnitude,
            "regime_verdict": npz_regime,
            "source_npz": "computations/session-92/s92_w7_5_hh_1_first_extraction_s4.npz",
            "source_verdict_line": "computations/session-92/s92_gate_verdicts.txt:191 (composite=INFO)",
        },
        "info_vs_pass_adjudication": {
            "adjudicated_reading": ("INFO-class band-RESIDENCE WOULD suffice to discharge "
                                    "FIRST-EXTRACTION (envelope-REALIZATION, distinct from Level-3 "
                                    "anchor-singleness); a tight central-value PASS is NOT required."),
            "but": ("band-residence is a NECESSARY conjunct of the discharge, and it is FALSE here "
                    "(alpha=0.194312 is in (0,1.5), below the band lower edge 1.5)."),
            "discharge_predicate": "numerical_anchor_exists AND band_admissible = True AND False = False",
            "w7_5_info_character": ("the §W7-5 INFO is the OUT-OF-BAND 'envelope-too-coarse' INFO "
                                    "(sign=PASS direction-correct, magnitude=INFO out-of-band), NOT a "
                                    "band-resident INFO; it does NOT realize an admissible envelope."),
            "conclusion": ("tag STAYS REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION; the flip to "
                           "STAGE-1-CANDIDATE-FIRST-EXTRACTED is NOT licensed on the actual §W7-5 data."),
        },
        "plan_spawn_premise_defect": {
            "asserted": "§W7-5 first-extracted alpha_HH1_emp(s=4) INSIDE the [1.5,4.0] band",
            "ground_truth": "alpha_HH1_emp(s=4)=0.194312 is OUT of band; sub_a_in_band=False",
            "class": "SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE (epistemic-discipline.md)",
            "consequence": ("the W6-2 PASS rubric was built on a false premise; the gate's own "
                            "pre-registered FAIL_meaning (plan lines 420-425) governs => FAIL."),
        },
        "registry_action": {
            "type": "VERIFIED NO-OP",
            "tag_before": TAG_PENDING,
            "tag_after": tag_after,
            "no_op_integrity": no_op_integrity,
            "pending_tag_in_az_block": pending_tag_in_block,
            "first_extracted_target_absent": extracted_target_absent,
            "az_heading_runtime_line": az_line_runtime,
            "plan_pinned_line": 19400,
            "drift_note": "§VII.AZ resolved by CONTENT (heading-anchor); plan-pinned ~19400/~19438 STALE-drifted",
        },
        "stage_pathway": ("UNTOUCHED — §VII.AZ.OP-PROJ remains STAGE-3-PERMANENT-eligible on Sub-claim A "
                          "(S91 W8-4 Stage-2 PASS-AND); the Sub-claim-B sub-class tag lives at the "
                          "Element-4 envelope-extraction layer per the SINGLE-ENTRY-WITH-DUAL-SUB-CLAIM structure."),
        "carry_forward": ("a BAND-ADMISSIBLE re-extraction of alpha_HH1_emp(s=4) in [1.5,4.0] is the "
                          "prerequisite to discharge the FIRST-EXTRACTION sub-class; queued at "
                          "CF-S91-HH1-FINITE-ALPHA-FIRST-EXTRACTION pathway (band-admissible re-extraction)."),
        "substitution_chain_conclusion": ("discharge_predicate = numerical(TRUE) AND admissible(FALSE) = FALSE; "
                                          "tag STAYS PENDING [required-direction-claim verified]"),
        "M1_M4_self_classification": {
            "M1_artifact_existence_with_content": True,
            "M2_registry_read_plus_sha_no_numerical_compute": True,
            "M3_band_membership_read_from_W7-5_npz_plus_pre-registered_deferred-pending_taxonomy": True,
            "M4_allowlist_append": "ORCHESTRATOR-ONLY (flagged in WP §W6-2; NOT edited by this script)",
        },
    }
    OUT_JSON.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  JSON sidecar -> {OUT_JSON.relative_to(ROOT)}")


def _emit_plot(alpha_emp_s4, verdict):
    fig, ax = plt.subplots(1, 1, figsize=(11.0, 4.6))
    # Number-line of alpha_HH1_emp(s=4) vs the [1.5, 4.0] band + analytic anchor alpha=4.
    ax.axhline(0, color="0.6", lw=0.8)
    # band shading
    ax.axvspan(BAND_LO, BAND_HI, color="C2", alpha=0.18, label=f"admissible band [{BAND_LO}, {BAND_HI}]")
    # INFO regions (0,1.5) and (4.0, +inf)
    ax.axvspan(0.0, BAND_LO, color="C1", alpha=0.12, label="INFO region (0, 1.5) — out-of-band (envelope too coarse)")
    # analytic anchor
    ax.axvline(ANALYTIC_ANCHOR_ALPHA, color="C0", ls=":", lw=2,
               label=fr"Wodzicki/Connes d=4 anchor $\alpha=2(s-2)={ANALYTIC_ANCHOR_ALPHA:.0f}$")
    # extracted value
    ax.plot([alpha_emp_s4], [0], "X", color="C3", markersize=18, markeredgecolor="black",
            label=fr"§W7-5 extracted $\alpha_{{HH^1,\,\mathrm{{emp}}}}(s{{=}}4)={alpha_emp_s4:.4f}$ (OUT of band)")
    ax.annotate(f"{alpha_emp_s4:.4f}", (alpha_emp_s4, 0), textcoords="offset points",
                xytext=(0, 16), ha="center", fontsize=10, color="C3", fontweight="bold")
    ax.set_xlim(-0.2, 4.6)
    ax.set_ylim(-0.6, 0.8)
    ax.set_yticks([])
    ax.set_xlabel(r"$\alpha_{HH^1,\,\mathrm{emp}}(s{=}4)$  (HH$^1$ cocycle-norm envelope exponent at substrate-distance-2 pole $s=4$)")
    ax.set_title(
        f"{GATE_ID}\n"
        f"§VII.AZ.OP-PROJ Sub-claim-B Element-4 deferred-pending tag-flip ADJUDICATION\n"
        f"§W7-5 first-extraction $\\alpha={alpha_emp_s4:.4f}$ is OUT of [{BAND_LO},{BAND_HI}] "
        f"(in_pass_band=False) — INFO band-residence WOULD suffice but $\\alpha$ NOT band-resident\n"
        f"tag STAYS REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION (registry NO-OP); composite verdict: {verdict}",
        fontsize=8.2,
    )
    ax.legend(loc="upper left", fontsize=7.5)
    ax.grid(True, axis="x", ls=":", alpha=0.4)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
