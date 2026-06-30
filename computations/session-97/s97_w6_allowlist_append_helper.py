"""S97 W6 METHODOLOGY-class allowlist append helper (orchestrator-only).

Appends `S97-W6-1-OMDM-RHOVAC-PINS` + `S97-W6-2-PETROV-ANNOTATION` rows to
methodology-wave-allowlist-ledger.md + paired rationales to
methodology-wave-instances.md, per .claude/rules/methodology-wave-allowlist.md.
Classification CONFIRMED METHODOLOGY-class by the W6 plan §"METHODOLOGY-class
classification (both gates)" M1-M3 conjunction (mirrors the S96 W7-2 pattern).

sha256_of_plan_block = SHA-256 over each gate's §-block (header-delimited).
"""
import hashlib
from pathlib import Path

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
PLAN = ROOT / "sessions" / "session-plan" / "session-97-plan-w6.md"
LEDGER = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-allowlist-ledger.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"
SESSION = "S97"

text = PLAN.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)

def block(start_hdr, end_hdr):
    s = next(i for i, l in enumerate(lines) if l.startswith(start_hdr))
    if end_hdr is None:
        e = len(lines)
    else:
        e = next(i for i, l in enumerate(lines) if i > s and l.startswith(end_hdr))
    return "".join(lines[s:e])

gates = [
    ("S97-W6-1-OMDM-RHOVAC-PINS", "## §W6-1.", "## §W6-2.",
     "S97 W6-1 — METHODOLOGY-class canonical-pin provenance promotion (mirrors S96 W7-2). "
     "update_constant Omega_DM_h2=0.1200 (OBSERVATIONAL-ANCHOR, lab-IN datum, DISTINCT from "
     "Omega_DM_obs=0.264 density parameter) + rho_vac_over_rho_obs=1.032 (FRAMEWORK-PREDICTION, "
     "DILUTION-CC-66). M1 artifact-existence (get_constant resolves with non-empty PROVENANCE + "
     "keying-tag); M2 update_constant + get_constant-verify (no numerical-threshold .py); M3 "
     "verbatim existing values from closed S70/S66 gates (no new derivation); M4 herewith."),
    ("S97-W6-2-PETROV-ANNOTATION", "## §W6-2.", None,
     "S97 W6-2 — METHODOLOGY-class annotation-hygiene: verdict-file companion-comment consistency "
     "for the tau->inf Jensen-product-metric Petrov/CMPP type. M1 artifact-existence (companion-comment "
     "consistent-with/governed-by the value-field); M2 companion-comment touch-up + grep cross-check "
     "(no numerical-threshold .py); M3 verbatim from the existing Petrov-type verdict (no re-derivation); "
     "M4 herewith. orchestrator-direct-eligible per mechanical-closure-discipline.md."),
]

ledger_text = LEDGER.read_text(encoding="utf-8")
inst_text = INSTANCES.read_text(encoding="utf-8")
for gate_id, sh, eh, rationale in gates:
    blk = block(sh, eh)
    sha = hashlib.sha256(blk.encode("utf-8")).hexdigest()
    print(f"{gate_id}: block {len(blk)} bytes, sha256_of_plan_block = {sha}")
    if gate_id in ledger_text:
        print(f"  GUARD: {gate_id} already in ledger — no append.")
    else:
        with open(LEDGER, "a", encoding="utf-8") as f:
            f.write(f"| {gate_id} | {SESSION} | {sha} |\n")
        print(f"  APPENDED ledger row.")
    if gate_id in inst_text:
        print(f"  GUARD: {gate_id} already in instances — no append.")
    else:
        with open(INSTANCES, "a", encoding="utf-8") as f:
            f.write(f"\n### {gate_id} ({SESSION}) — {sha}\n\n{rationale}\n")
        print(f"  APPENDED instances rationale.")
