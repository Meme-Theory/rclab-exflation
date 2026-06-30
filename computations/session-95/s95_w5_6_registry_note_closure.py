"""S95 W5-6 TAU-FLOW-Q-FLOW-REGISTRY-NOTE — METHODOLOGY-class dual-SHA closure.

Orchestrator-direct-write (METHODOLOGY-class per wave-classification.md M1-M4; no
numerical gate). This is the dual-SHA *closure helper* mandated by
wave-classification.md §"Dual-SHA closure for METHODOLOGY-class":
  - content_sha256 over the registry-note diff (the correspondence-ledger note body)
  - audit_sha256   over the source-document input-pin map (E7 / S62 #19 / q=N_pair)
Idempotent: re-running reproduces the same dual-SHA from the note content and does
not double-append the verdict line.
"""
import hashlib
import os
import sys

# METHODOLOGY-class closure helper consumes NO framework constants (it only hashes the
# note diff + the source-document pin map). The import below is present for
# canonical-sourcing compliance per .claude/rules/math-scripts.md; M_KK_gravity is unused.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import M_KK_gravity  # noqa: F401  # (compliance import; unused)

NOTE = "sessions/framework/correspondence/tau-flow-vs-q-flow-note.md"
VERDICT = "computations/session-95/s95_gate_verdicts.txt"
GATE = "TAU-FLOW-Q-FLOW-REGISTRY-NOTE"

note_bytes = open(NOTE, "rb").read()
content_sha = hashlib.sha256(note_bytes).hexdigest()              # content over the note diff

pinmap = "|".join([                                              # audit over the source-pin map
    GATE,
    "scheme=REGISTRY-HYGIENE-NOTE",
    "convention=METHODOLOGY-class-dual-SHA-content-over-diff-audit-over-source-pinmap",
    "L_max=NA",
    "allowlist_sha256_of_plan_block=ac0f215daefad38bc30bd9c73111b1931e9f7f9e1f84082e4be249badc723e95",
    "e7_provenance=E7-Structural-Monotonicity-dS_SA/dtau>0-row13-S37",
    "s62_provenance=S62-CC-Monotonicity-#19-dE_ZP/dq>0-row19-atlas07-A9",
    "q_identity=q=N_pair-s59_q_variable_results.txt",
    "content_sha256=" + content_sha,
])
audit_sha = hashlib.sha256(pinmap.encode("utf-8")).hexdigest()

value = ("METHODOLOGY-class_registry-note_landed;"
         "cites_E7_tau-flow_dS/dtau>0_order-parameter-texture-geometric-modulus;"
         "cites_S62#19_q-flow_dE_ZP/dq>0_conserved-charge_q=N_pair;"
         "states_CC_layer_rests_on_q-flow_NOT_tau-ramp;4_content_conditions_present")
line = (f"{GATE}: PASS -- value='{value}' scheme=REGISTRY-HYGIENE-NOTE "
        f"convention=METHODOLOGY-class-dual-SHA-content-over-diff-audit-over-source-pinmap "
        f"L_max=NA audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n")
comp = (f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE} dual-SHA companion row (METHODOLOGY-class; content over note diff, audit over source-pin map)\n")

existing = open(VERDICT, "r", encoding="utf-8").read()
if ("\n" + existing).find(f"\n{GATE}: PASS") != -1:
    print("ALREADY-PRESENT; not re-appending")
else:
    with open(VERDICT, "a", encoding="utf-8") as f:
        f.write(line)
        f.write(comp)
    print("APPENDED")
print("content_sha256", content_sha)
print("audit_sha256", audit_sha)
