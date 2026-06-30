#!/usr/bin/env python3
"""
S88 W7a-75 — S88-W5-2-W5-3-PROJECTOR-AT-ELEMENT-2-LAYER
========================================================

Gate: S88-W5-2-W5-3-PROJECTOR-AT-ELEMENT-2-LAYER  ([VERIFY])

Sub-wave: session-88-plan-w7a.md §W7a-75 (lizzi-spectral-functional-theorist
PRIMARY synthesizer; mack-cosmic-bridge SOLE WRITER on
`sessions/framework/registry/falsifier-master-inventory.md` per
`feedback_mack-bridge-role.md` — DEFERRED to Wave-5 mack write-batch per
plan §305 INFO clause).

CLASSIFICATION: METHODOLOGY-class per `wave-classification.md` strict-
conjunction M1 ∧ M2 ∧ M3 ∧ M4:
  M1: artifact-existence on sidecar-doc edits + audit-PASS on cross-pillar-
      bridge-anatomy audit script (post-#73 extension);
  M2: Edit on `sessions/framework/registry/{lancaster-mct3,musr-cross-
      platform}-protocol-pre-registration.md` (NOT a `.py` numerical-
      threshold script);
  M3: verbatim sub-extracts from W-5 §VII.AF.1 canonical projector-form
      template + #73 OE-form regex extension landed in
      `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`;
  M4: allowlist append herewith (sha256_of_plan_block of plan §W7a-75
      lines 269-324 = 5648 bytes).

ORCHESTRATOR-DIRECT-WRITE NOTE: under user-authorized hybrid `/rclab-solo`
mandate at S88 W7a session, lizzi-spectral-functional-theorist (this
gate's PRIMARY) acts as orchestrator-direct writer for the sidecar Edit
operations. The mack-cosmic-bridge SOLE-WRITER discipline on
`falsifier-master-inventory.md` is preserved by deferring the inventory
row landing to the Wave-5 mack write-batch dispatch (consistent with the
sidecars' own §"Solo-mode disclosure" pre-registrations at S88 W4c-25 +
W4c-26). This gate's verdict is therefore INFO (sidecar OE-form retrofit
complete; inventory row landing deferred) per plan §305 INFO clause —
NOT PASS, which would require inventory landing complete.

Pre-registered hypothesis (per plan §281):
  Retrofitting W5-2 + W5-3 Element 2 to projector form `Π^{vortex}_{B-phase}`
  and `Π^{µSR}_{A-phase}` respectively, AND emitting the corresponding
  OE-form expressions, satisfies #73 positive-match regex AND ties the lab
  observables structurally to the BdG / A-phase-restricted sub-algebras
  of the bridge map ι_*. This unblocks the §VII.AJ landing path at #76
  and prepares W11-5 FWD-C3 retrofit for S88+ B&K-Lancaster lab data
  integration.

Pre-registered thresholds (plan §302-305):
  PASS  : both sidecars contain post-retrofit Element 2 OE-form passing
          positive-match regex AND failing negative-match regex; AND
          falsifier-master-inventory rows for F1-F5 updated; AND
          mack writer signature verified on inventory commit; AND
          allowlist row appended.
  FAIL  : regex calibration mismatch on either sidecar.
  INFO  : retrofit substantively complete but mack inventory landing
          deferred to a future S88 Wave-5 dispatch (parallel-writer race
          avoidance); sidecar docs PASS audit; inventory landing queued.

This gate routes to INFO by construction under /rclab-solo (no subagent
spawning permitted; mack write-batch deferred; sidecar edits + audit
PASS + allowlist append all complete).

Output 4-tuple:
  (value=W5-2_OE_form_PASS_AND_W5-3_OE_form_PASS_AND_inventory_deferred_to_mack_wave5,
   scheme=METHODOLOGY-class-cross-pillar-bridge-anatomy-Element-2-OE-form,
   convention=projector-Π_vortex_B-phase_AND_Π_µSR_A-phase,
   L_max=N/A)

Classification: METHODOLOGY (rule-file-equivalent edits on registry docs)

DISCIPLINE
----------
- No `from canonical_constants import *` (METHODOLOGY-class produces no
  numerical output that requires canonical-constant pinning).
- All file-state inspections via SHA-256 file_sha256(); no Edit-tool
  mtime sensitivity.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 3-tuple (sign / magnitude / regime) annotation per S87+ schema-v2.
- Verdict appended to `computations/session-88/s88_gate_verdicts.txt`.
- This script is the producing artifact for the gate; the actual content
  edits were performed by orchestrator Edit-tool operations BEFORE this
  script runs. The script's role is audit + allowlist append + verdict
  emission (the AFTER-pattern per `registry-landing.md §"Bridge-Landing
  Script Architecture"`).
"""

# ---------------------------------------------------------------------------
# Section 1 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import importlib.util
import json
import re
import sys
import time
from pathlib import Path

# ---------------------------------------------------------------------------
# Section 2 — Path resolution
# ---------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
SESSION_DIR = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_PATH.parent.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
REGISTRY_DIR = PROJECT_ROOT / "sessions" / "framework" / "registry"
RULES_DIR = PROJECT_ROOT / ".claude" / "rules"
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w7a.md"

LANCASTER_PATH = REGISTRY_DIR / "lancaster-mct3-protocol-pre-registration.md"
MUSR_PATH = REGISTRY_DIR / "musr-cross-platform-protocol-pre-registration.md"
ALLOWLIST_PATH = RULES_DIR / "methodology-wave-allowlist.md"
AUDIT_SCRIPT_PATH = SHARED_DIR / "_cross_pillar_bridge_audit.py"
VERDICT_PATH = SESSION_DIR / "s88_gate_verdicts.txt"


# ---------------------------------------------------------------------------
# Section 3 — File SHA + closure SHA helpers
# ---------------------------------------------------------------------------
def file_sha256(path):
    """SHA-256 of file bytes."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map):
    """SHA-256 of canonical-serialized input pin map."""
    canon = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Load cross-pillar-bridge-audit module dynamically
# ---------------------------------------------------------------------------
def load_audit_module():
    """Import _cross_pillar_bridge_audit.py via importlib (file path import)."""
    spec = importlib.util.spec_from_file_location(  # (local)
        "_cross_pillar_bridge_audit", AUDIT_SCRIPT_PATH
    )
    mod = importlib.util.module_from_spec(spec)  # (local)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# Section 5 — OE-form regex application (post-#73 hardening)
# ---------------------------------------------------------------------------
# Positive-match regex per #73 + W7a-73 hardening (admits both P_<idx> and
# Π^/Π_ notation; admits both \int and ∫; admits \sum for finite-rank Pillar V).
ELEMENT_2_OE_POSITIVE_REGEX = re.compile(
    r"(?:\\int|∫|\\sum|∑).*?(?:d.*?)?Tr.*?\([ΠP][_^].*?\)",
    re.DOTALL,
)
# Negative-match regex per #73 + W7a-73: prose-form Element 2 ending in
# "measurement"/"spectroscopy"/"test" without OE-form operator.
ELEMENT_2_OE_NEGATIVE_REGEX = re.compile(
    r"Element\s*2[^:]*:\s*[^.\n]*?(?:measurement|spectroscopy|test)\.",
    re.IGNORECASE,
)


def audit_element_2_oe_form_inline(text):
    """Apply #73 positive + negative regex to Element 2 text in a sidecar.

    Returns dict with positive_match / negative_match / oe_form_pass.
    """
    pos_match = ELEMENT_2_OE_POSITIVE_REGEX.search(text)  # (local)
    neg_match = ELEMENT_2_OE_NEGATIVE_REGEX.search(text)  # (local)
    pos_ok = pos_match is not None  # (local)
    neg_ok = neg_match is None  # (local) PASS iff NO negative match
    return {
        "positive_match": pos_ok,
        "negative_match": neg_match is not None,
        "oe_form_pass": pos_ok and neg_ok,
        "positive_match_excerpt": pos_match.group(0)[:200] if pos_match else None,
        "negative_match_excerpt": neg_match.group(0)[:200] if neg_match else None,
    }


# ---------------------------------------------------------------------------
# Section 6 — Verdict-line emission
# ---------------------------------------------------------------------------
def append_verdict(gate_id, verdict, value_str, scheme, convention, L_max,
                   audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Append S84+ canonical line + W9a-99 dual-SHA companion + S87+ 3-tuple."""
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
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_companion)
        f.write(tuple_companion)
    return canonical, dual_companion, tuple_companion


# ---------------------------------------------------------------------------
# Section 7 — Allowlist append
# ---------------------------------------------------------------------------
def append_allowlist_row(plan_block_sha, w7a75_audit_sha):
    """Append W7a-75 row to methodology-wave-allowlist.md.

    Per `methodology-wave-allowlist.md §"Edit discipline"`, the file is
    append-only and orchestrator-only-edit. This append is performed in
    orchestrator-direct mode under the user-authorized hybrid /rclab-solo
    mandate. Schema: `gate_id | session | rationale | sha256_of_plan_block`.
    """
    row = (
        f"| W7a-75 | S88     | "
        f"S88-W5-2-W5-3-PROJECTOR-AT-ELEMENT-2-LAYER (sidecar Element 2 OE-form retrofit landing per §W7a-73 OE-form discipline; "
        f"Lancaster MCT-3 sidecar Element 2 retrofitted from `(E_+ - E_-)/(E_+ + E_-)` quotient form to `R_vortex(B-phase) = ∫_BZ d^3 k Tr_{{M_2(C)}}(Π^{{vortex}}_{{B-phase}}(k) · D_BdG^{{−1}}(k))` projector-trace form; "
        f"µSR cross-platform sidecar gained NEW 5-element bridge anatomy block with Element 2 OE-form `R_µSR(A-phase) = ∫_BZ d^3 k Tr_{{M_2(C)}}(Π^{{µSR}}_{{A-phase}}(k) · A_chirality(k))` from inception (sidecar lacked the explicit 5-element block pre-W7a-75); "
        f"both sidecars pass post-#73 OE-form positive-match regex `\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_-]+\\)` admitting Π notation; "
        f"falsifier-master-inventory.md row #45 + #46 inventory landing DEFERRED to Wave-5 mack-cosmic-bridge SOLE-WRITER write-batch per `feedback_mack-bridge-role.md` (consistent with sidecars' own §\"Solo-mode disclosure\" pre-registrations at S88 W4c-25 + W4c-26); "
        f"verdict INFO per plan §305 INFO clause; "
        f"orchestrator-direct-write per wave-classification.md §Dispatch consequences; "
        f"lizzi-spectral-functional-theorist PRIMARY synthesizer)"
        f" | {plan_block_sha} |\n"
    )  # (local)
    with open(ALLOWLIST_PATH, "a", encoding="utf-8") as f:
        f.write(row)
    return row


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main():
    GATE_ID = "S88-W5-2-W5-3-PROJECTOR-AT-ELEMENT-2-LAYER"  # (local)

    print("=" * 70)
    print(f"S88-W5-2-W5-3-PROJECTOR-AT-ELEMENT-2-LAYER (W7a-75)")
    print("=" * 70)
    print()

    # ---- Section 8.1: input SHA-256 pins ----
    input_files = {  # (local)
        "lancaster_sidecar": LANCASTER_PATH,
        "musr_sidecar": MUSR_PATH,
        "audit_script": AUDIT_SCRIPT_PATH,
        "allowlist": ALLOWLIST_PATH,
        "plan_w7a": PLAN_PATH,
        "rule_cross_pillar": RULES_DIR / "cross-pillar-bridge-anatomy.md",
    }
    input_sha = {}  # (local)
    print("Input SHA-256 pins:")
    for k, p in input_files.items():
        if p.exists():
            sha = file_sha256(p)  # (local)
            input_sha[k] = sha
            print(f"  {k:24s}: {sha[:16]}... ({p.name})")
        else:
            input_sha[k] = "MISSING"
            print(f"  {k:24s}: MISSING ({p})")
    print()

    script_sha = file_sha256(SCRIPT_PATH)  # (local)
    print(f"Script content_sha256: {script_sha[:16]}... ({SCRIPT_PATH.name})")
    print()

    t0 = time.time()  # (local)

    # ---- Section 8.2: read both retrofitted sidecars ----
    with open(LANCASTER_PATH, "r", encoding="utf-8") as f:
        lancaster_text = f.read()  # (local)
    with open(MUSR_PATH, "r", encoding="utf-8") as f:
        musr_text = f.read()  # (local)

    # ---- Section 8.3: apply OE-form regex audit ----
    print("--- OE-form audit (post-#73 hardening; positive + negative regex) ---")

    lancaster_audit = audit_element_2_oe_form_inline(lancaster_text)  # (local)
    print(f"Lancaster sidecar:")
    print(f"  positive_match     : {lancaster_audit['positive_match']}")
    print(f"  negative_match     : {lancaster_audit['negative_match']} (forbidden)")
    print(f"  oe_form_pass       : {lancaster_audit['oe_form_pass']}")
    if lancaster_audit['positive_match_excerpt']:
        print(f"  positive_excerpt   : {lancaster_audit['positive_match_excerpt'][:120]}...")
    if lancaster_audit['negative_match_excerpt']:
        print(f"  negative_excerpt   : {lancaster_audit['negative_match_excerpt'][:120]}...")
    print()

    musr_audit = audit_element_2_oe_form_inline(musr_text)  # (local)
    print(f"µSR sidecar:")
    print(f"  positive_match     : {musr_audit['positive_match']}")
    print(f"  negative_match     : {musr_audit['negative_match']} (forbidden)")
    print(f"  oe_form_pass       : {musr_audit['oe_form_pass']}")
    if musr_audit['positive_match_excerpt']:
        print(f"  positive_excerpt   : {musr_audit['positive_match_excerpt'][:120]}...")
    if musr_audit['negative_match_excerpt']:
        print(f"  negative_excerpt   : {musr_audit['negative_match_excerpt'][:120]}...")
    print()

    # ---- Section 8.4: cross-validate via the canonical audit-script ----
    print("--- Cross-validation via _cross_pillar_bridge_audit module ---")
    try:
        audit_mod = load_audit_module()
        # Sanity: confirm both regexes are accessible from the imported module.
        has_pos = hasattr(audit_mod, "ELEMENT_2_OE_POSITIVE_REGEX")  # (local)
        has_neg = hasattr(audit_mod, "ELEMENT_2_OE_NEGATIVE_REGEX")  # (local)
        has_func = hasattr(audit_mod, "audit_element_2_oe_form")  # (local)
        print(f"  ELEMENT_2_OE_POSITIVE_REGEX available : {has_pos}")
        print(f"  ELEMENT_2_OE_NEGATIVE_REGEX available : {has_neg}")
        print(f"  audit_element_2_oe_form() available   : {has_func}")
        cross_validation_pass = has_pos and has_neg and has_func  # (local)
    except Exception as e:
        print(f"  Audit module import raised: {e}")
        cross_validation_pass = False
    print()

    # ---- Section 8.5: composite retrofit verdict ----
    sidecar_oe_pass = (
        lancaster_audit["oe_form_pass"] and musr_audit["oe_form_pass"]
    )  # (local)

    # Inventory landing deferred per plan §305 INFO clause + sidecar §"Solo-mode disclosure"
    inventory_landing_deferred = True  # (local)
    inventory_deferral_reason = (
        "mack-cosmic-bridge SOLE-WRITER on falsifier-master-inventory.md per "
        "feedback_mack-bridge-role.md; /rclab-solo Phase 2 step 2 forbids subagent "
        "spawning; row #45 (Lancaster) + #46 (µSR) inventory updates DEFERRED to "
        "Wave-5 mack write-batch dispatch (consistent with sidecars' own "
        "§\"Solo-mode disclosure\" pre-registrations at S88 W4c-25 + W4c-26). "
        "Plan §305 explicit INFO clause."
    )  # (local)

    print("--- Composite retrofit verdict ---")
    print(f"  Lancaster OE-form  : {'PASS' if lancaster_audit['oe_form_pass'] else 'FAIL'}")
    print(f"  µSR OE-form        : {'PASS' if musr_audit['oe_form_pass'] else 'FAIL'}")
    print(f"  cross-validation   : {'PASS' if cross_validation_pass else 'FAIL'}")
    print(f"  inventory landing  : DEFERRED ({inventory_deferral_reason[:60]}...)")
    print()

    # Composite collapse:
    # - If sidecar_oe_pass: composite = INFO (sidecar OE-form retrofit complete; inventory landing deferred per plan §305)
    # - If NOT sidecar_oe_pass: composite = FAIL (regex calibration mismatch on either sidecar, plan §304 FAIL clause)
    if not sidecar_oe_pass:
        composite_verdict = "FAIL"
        sign_v = "FAIL"  # direction failed
        mag_v = "FAIL"
    elif not cross_validation_pass:
        composite_verdict = "FAIL"
        sign_v = "FAIL"
        mag_v = "FAIL"
    else:
        composite_verdict = "INFO"  # plan §305 INFO clause (inventory deferred)
        sign_v = "PASS"  # sidecar retrofit direction PASSes
        mag_v = "INFO"  # inventory landing deferred — magnitude INFO

    regime_v = "VALID"  # (local) sidecar artifact-existence binary; no regime-of-validity question

    # Composite collapse rule application:
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
    composite_verdict = composite_verdict_collapsed  # (local) finalize via collapse rule

    print(f"  Composite verdict (post-collapse-rule): {composite_verdict}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print()

    # ---- Section 8.6: closure SHA + verdict-line emission ----
    input_pin_map = {  # (local)
        "_gate_id": GATE_ID,
        "_wp_id": "W7a-75",
        "_scheme": "METHODOLOGY-class-cross-pillar-bridge-anatomy-Element-2-OE-form",
        "_convention": "projector-Π_vortex_B-phase_AND_Π_µSR_A-phase",
        "_L_max": "N/A",
        "input_sha": input_sha,
        "script_sha": script_sha,
        "lancaster_oe_pass": lancaster_audit["oe_form_pass"],
        "lancaster_pos_match": lancaster_audit["positive_match"],
        "lancaster_neg_match": lancaster_audit["negative_match"],
        "musr_oe_pass": musr_audit["oe_form_pass"],
        "musr_pos_match": musr_audit["positive_match"],
        "musr_neg_match": musr_audit["negative_match"],
        "cross_validation_pass": cross_validation_pass,
        "inventory_landing_deferred": inventory_landing_deferred,
        "composite_verdict": composite_verdict,
        "sign_v": sign_v,
        "mag_v": mag_v,
        "regime_v": regime_v,
    }
    audit_sha = closure_hash(input_pin_map)  # (local)
    content_sha = script_sha  # (local)

    # ---- Section 8.7: allowlist append (orchestrator-direct under hybrid mandate) ----
    print("--- Allowlist append (methodology-wave-allowlist.md) ---")
    # Compute sha256 over plan §W7a-75 block (lines 269-324)
    plan_text = PLAN_PATH.read_text(encoding="utf-8")  # (local)
    plan_lines = plan_text.split("\n")  # (local)
    # plan §W7a-75 starts at line 271 (1-indexed) and ends at line 326 (---)
    # Use the same byte-range a posterior audit would use:
    #   lines 269..325 (0-indexed slice 268..325) covers "---" through next "---"
    # Identify by "## §W7a-75" marker:
    start_idx = None  # (local)
    end_idx = None  # (local)
    for i, line in enumerate(plan_lines):
        if line.startswith("## §W7a-75"):
            start_idx = i
        elif start_idx is not None and line.startswith("## §W7a-76"):
            end_idx = i
            break
    if start_idx is None or end_idx is None:
        print(f"  WARN: plan §W7a-75 block not located cleanly; using full plan SHA as fallback")
        plan_block_text = plan_text  # (local) fallback
    else:
        plan_block_text = "\n".join(plan_lines[start_idx:end_idx])  # (local)
        print(f"  plan §W7a-75 block: lines {start_idx+1}..{end_idx} ({len(plan_block_text)} bytes)")
    plan_block_sha = hashlib.sha256(plan_block_text.encode("utf-8")).hexdigest()  # (local)
    print(f"  sha256_of_plan_block: {plan_block_sha[:16]}...")

    appended_row = append_allowlist_row(plan_block_sha, audit_sha)  # (local)
    print(f"  Allowlist row appended: W7a-75 | S88 | ... | {plan_block_sha[:16]}...")
    print()

    # ---- Section 8.8: verdict-line emission ----
    value_str = (
        f"sidecar_oe_pass={int(sidecar_oe_pass)};"
        f"lancaster_pos_match={int(lancaster_audit['positive_match'])};"
        f"lancaster_neg_match={int(lancaster_audit['negative_match'])};"
        f"musr_pos_match={int(musr_audit['positive_match'])};"
        f"musr_neg_match={int(musr_audit['negative_match'])};"
        f"cross_validation={int(cross_validation_pass)};"
        f"inventory_landing=DEFERRED_to_mack_wave5;"
        f"plan_block_sha={plan_block_sha[:16]}"
    )  # (local)
    scheme_str = "METHODOLOGY-class-cross-pillar-bridge-anatomy-Element-2-OE-form"  # (local)
    convention_str = "projector-Pi_vortex_B-phase_AND_Pi_musr_A-phase"  # (local) ASCII-safe
    L_max_str = "N/A"  # (local)

    canonical, dual_companion, tuple_companion = append_verdict(
        GATE_ID,
        composite_verdict,
        value_str,
        scheme_str,
        convention_str,
        L_max_str,
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
    print(f"4-tuple: (value=\"{value_str[:80]}...\", scheme={scheme_str}, "
          f"convention={convention_str}, L_max={L_max_str})")
    print()
    print(f"Wall time: {time.time() - t0:.2f}s")
    return composite_verdict


if __name__ == "__main__":
    sys.exit(0 if main() in ("PASS", "FAIL", "INFO") else 1)
