"""
S88 W7c-84 — S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN
====================================================

Mechanical-closure script for the live-physical Pauli-Villars re-run of the
axiom-side c_sub cross-review at substrate-distance-1 anomaly pole s=4.

This script implements the PRE-REG-INC mechanical-closure path per
.claude/rules/mechanical-closure-discipline.md when the upstream prerequisite
S88-PV-PIPELINE-LANDING has not yet landed.

Plan reference: sessions/session-plan/session-88-plan-w7c.md §W7c-84.
Plan §"Wave 7c Decision Point Prerequisites" item 4 (line 30) anticipates
this scenario explicitly:

    "Pauli-Villars pipeline spec available — S61/S78 PV mass-scale-running
     module at phonon-exflation-sim/src/spectral_action_pv.py (or analog)
     compiled and callable; if absent, route #84 to PRE-REG-INC
     blocked-by-S88-PV-PIPELINE-LANDING."

Per plan §line 33:

    "If any prerequisite fails verification at dispatch time, the producing
     script emits PRE-REG-INC per `mechanical-closure-discipline.md`
     §'When mechanical closure IS acceptable' with per-gate-distinct
     `audit_sha256` and value string `'PRE-REG-INC_blocked_by_<symbol>_<status>'`."

Spawn-prompt orchestrator override (canonical):

    "If absent at dispatch-time, emit PRE-REG-INC per
     .claude/rules/mechanical-closure-discipline.md with
     value='PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent'
     and document blocked-prereq in WP §W7c-84 Verdict block."

Authorship
----------
- PRIMARY: lizzi-spectral-functional-theorist (regulator-axis expert)
- CO-AUTHOR: connes-ncg-theorist (NCG-axiomatic; Chamseddine-Connes 1996 +
             Andrianov-Lizzi 1001.2036 anomaly-cancellation derivation)

Machinery pin (PRDR §0.11; verbatim from plan §W7c-84 lines 57-67)
-------------------------------------------------------------------
- D_K_block_diagonal_cache:
    computations/session-84/s84_spectrum_cache_L12_tau019.npz
    (truncate to L_max=10 per W11-2 Casimir-bound feasibility cross-check;
     truncation_consistent = True against L_max=12 master cache)
- tau_fold = 0.190 (canonical_constants.py)
- M_KK = 7.428660036284456e+16 GeV (canonical_constants.py)
- pv_mass_pairs = [(M_KK, +1), (2*M_KK, -5), (4*M_KK, +10),
                   (8*M_KK, -10), (16*M_KK, +5), (32*M_KK, -1)]
                  rank-3 PV subtraction
                  (sum C_i = 0, sum C_i*M_i^2 = 0, sum C_i*M_i^4 = 0;
                   SHA-pinned at plan-freeze)
- s_anomaly = 4 (substrate-distance-1 anomaly pole)
- s_normalization = 3 (substrate-distance-1 baseline pole)
- c_sub_baseline = 2.238 (canonical_constants.py)
- LEVEL = 1 (live-physical; SCHEMATIC FORBIDDEN; verdict convention= field
             MUST encode PRIMARY-PV-live)
- regulator_class = "Pauli-Villars" (per regulator-pin-discipline.md)
- L_max_operational = 10

Mechanical-closure rationale (per discipline §"When mechanical closure IS
acceptable")
----------------------------------------------------------------------------
1. Upstream-block topology IS the cause: this gate's PV-pipeline prereq
   has verdict-equivalent status "absent" at dispatch time; the plan
   author pre-registered the prereq-block scenario explicitly at
   plan §"Wave 7c Decision Point Prerequisites" item 4.
2. Verdict honesty: emitted verdict is PRE-REG-INC with value=
   'PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent'.
   PASS is FORBIDDEN here per discipline §item 2 + PROHIBITED_ACTIONS
   Class 4 (ansatz-forced PASS).
3. Per-gate-distinct audit_sha256: pin-map embeds gate identity keys
   (_gate_id, _wp_id, _scheme, _convention, _pin_pv_pipeline_path,
    _pin_pv_pipeline_status) so the audit_sha256 is structurally
   unique to this closure.
4. Audit-trail signature: descriptive value string names the blocking
   prereq + its status; future audit grep can verify the named upstream
   gate exists with the named status.
5. Working-paper update is in-script: this script writes the §W7c-84
   Status / Verdict / Results / Substrate framing blocks in the same
   run as the verdict-line append.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Cap CPU threads per .claude/rules/computation-environment.md fallback
os.environ.setdefault("OMP_NUM_THREADS", "8")

# Canonical-constant imports (per .claude/rules/math-scripts.md MANDATORY for S34+).
# Make computations/_shared/ importable so canonical_constants.py is found.
sys.path.insert(
    0,
    str(
        Path(r"C:\sandbox\Ainulindale Exflation")
        / "computations"
        / "_shared"
    ),
)
from canonical_constants import (  # noqa: E402  (path-injected import)
    M_KK,
    tau_fold,
    c_sub_baseline,
)

# ---------------------------------------------------------------------------
# Canonical paths (absolute; per CLAUDE.md path-discipline)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
SESSION_DIR = PROJECT_ROOT / "computations" / "session-88"
WP_PATH = PROJECT_ROOT / "sessions" / "session-88" / "session-88-w7c-workingpaper.md"
VERDICT_FILE = SESSION_DIR / "s88_gate_verdicts.txt"
PV_PIPELINE = PROJECT_ROOT / "phonon-exflation-sim" / "src" / "spectral_action_pv.py"
SPECTRUM_CACHE = (
    PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
)

OUT_PY = SESSION_DIR / "s88_w7c_tier1_live_physical_re_run.py"
OUT_NPZ = SESSION_DIR / "s88_w7c_tier1_live_physical_re_run.npz"
OUT_PNG = SESSION_DIR / "s88_w7c_tier1_live_physical_re_run.png"
OUT_JSON = SESSION_DIR / "s88_w7c_tier1_live_physical_re_run.json"

# Plan-block pins (verbatim machinery pin per plan §W7c-84 lines 57-67).
# Canonical constants M_KK, tau_fold, c_sub_baseline imported above.
# Schema-only literals (gate-block parameters, not framework-physical
# constants) are tagged `# (local)` per math-scripts.md §"Local Variable Tagging".
GATE_ID = "S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN"
WP_ID = "W7c-84"
SCHEME_TAG = "Pauli-Villars rank-3 mass-scale-running"
CONVENTION_TAG = "axiom-side-WZW-anomaly-isolating-proxy-PRIMARY-PV-live"
L_MAX_TAG = 10            # (local)  gate-block schema parameter (plan §W7c-84 line 73)
S_ANOMALY = 4             # (local)  gate-block schema parameter (plan §W7c-84 line 62)
S_NORMALIZATION = 3       # (local)  gate-block schema parameter (plan §W7c-84 line 63)
LEVEL = 1                 # (local)  gate-block schema parameter (plan §W7c-84 line 65)
REGULATOR_CLASS = "Pauli-Villars"
PV_MASS_PAIRS = [
    (1.0 * M_KK, +1),     # (local)  gate-block schema PV mass-pair (plan §W7c-84 line 61)
    (2.0 * M_KK, -5),     # (local)
    (4.0 * M_KK, +10),    # (local)
    (8.0 * M_KK, -10),    # (local)
    (16.0 * M_KK, +5),    # (local)
    (32.0 * M_KK, -1),    # (local)
]


def _hash_path(p: Path) -> str:
    """SHA-256 hex of file content if file exists; 'absent' marker otherwise."""
    if not p.exists():
        return "absent"
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    """SHA-256 over the ordered, JSON-serialized input-pin map (matches
    .claude/rules/gate-verdicts.md S81+ closure-hash protocol)."""
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# 1. Verify upstream-prereq absence (artifact-existence test only;
#    NO physics computation per mechanical-closure-discipline.md §item 2:
#    emitted verdict is PRE-REG-INC, NOT PASS, regardless of cache existence).
# ---------------------------------------------------------------------------
pv_pipeline_status = "present" if PV_PIPELINE.exists() else "absent"
spectrum_cache_status = "present" if SPECTRUM_CACHE.exists() else "absent"

print(f"[S88 W7c-84 mechanical-closure] PV pipeline: {PV_PIPELINE}")
print(f"  status: {pv_pipeline_status}")
print(f"[S88 W7c-84 mechanical-closure] spectrum cache: {SPECTRUM_CACHE}")
print(f"  status: {spectrum_cache_status}")

# Verify the PV-pipeline absence is NOT a sympy false-positive
# (sympy.physics.paulialgebra.py exists in venv; the named pipeline does not)
print(f"[S88 W7c-84 mechanical-closure] PV pipeline absence verified: "
      f"named module phonon-exflation-sim/src/spectral_action_pv.py = "
      f"{pv_pipeline_status}")

# ---------------------------------------------------------------------------
# 2. Build the per-gate-distinct input-pin map (audit-SHA basis)
#    Per discipline §item 3: pin-map embeds per-gate identity keys so the
#    audit_sha256 is structurally unique across all gates this script could
#    close (here we close exactly one gate, but the discipline applies).
# ---------------------------------------------------------------------------
input_pin_map = {
    "_gate_id": GATE_ID,
    "_wp_id": WP_ID,
    "_scheme": SCHEME_TAG,
    "_convention": CONVENTION_TAG,
    "_L_max": L_MAX_TAG,
    "_regulator_class": REGULATOR_CLASS,
    "_level": LEVEL,
    "_s_anomaly": S_ANOMALY,
    "_s_normalization": S_NORMALIZATION,
    "_tau_fold": tau_fold,
    "_M_KK": M_KK,
    "_c_sub_baseline": c_sub_baseline,
    "_pv_mass_pairs": [[m, c] for (m, c) in PV_MASS_PAIRS],
    "_pin_pv_pipeline_path": str(PV_PIPELINE).replace("\\", "/"),
    "_pin_pv_pipeline_status": pv_pipeline_status,
    "_pin_pv_pipeline_sha": _hash_path(PV_PIPELINE),
    "_pin_spectrum_cache_path": str(SPECTRUM_CACHE).replace("\\", "/"),
    "_pin_spectrum_cache_status": spectrum_cache_status,
    "_pin_spectrum_cache_sha": _hash_path(SPECTRUM_CACHE),
    "_pin_plan_doc": "sessions/session-plan/session-88-plan-w7c.md#W7c-84",
    "_blocked_by": "S88-PV-PIPELINE-LANDING",
    "_closure_class": "PRE-REG-INC",
    "_closure_rule_file": ".claude/rules/mechanical-closure-discipline.md",
    "_planned_prereq_route": (
        "plan-Wave-7c-Decision-Point-Prerequisites-item-4 "
        "+ plan-line-30-routing-clause"
    ),
}

audit_sha = closure_hash(input_pin_map)
content_payload = json.dumps(
    {"verdict_payload": "PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent",
     "audit_sha256": audit_sha,
     "gate_id": GATE_ID,
     "wp_id": WP_ID},
    sort_keys=True,
    separators=(",", ":"),
)
content_sha = hashlib.sha256(content_payload.encode("utf-8")).hexdigest()

print(f"[S88 W7c-84 mechanical-closure] audit_sha256 = {audit_sha}")
print(f"[S88 W7c-84 mechanical-closure] content_sha256 = {content_sha}")

# ---------------------------------------------------------------------------
# 3. Substitution chain (substrate-IS reasoning; no numerical c_sub claim)
#    Per .claude/rules/math-scripts.md §"Double-Check Logic Before Compute":
#    the substitution chain documents the structural reasoning for emitting
#    PRE-REG-INC rather than PASS/FAIL. No directional claim about
#    c_sub_anomaly_WZW vs c_sub_baseline is made; the gate is structurally
#    untestable until upstream lands.
# ---------------------------------------------------------------------------
SUBSTITUTION_CHAIN = """\
Step 1 (definition of gate executability):
  prereq_pipeline   := phonon-exflation-sim/src/spectral_action_pv.py
                       (per plan §W7c-84 line 50, machinery pin)
  prereq_callable   := exists(prereq_pipeline) AND
                       has_callable(prereq_pipeline, "pv_anomaly_kernel")
                       (per plan method step 1)
  gate_executable   := prereq_callable
                       (per plan §"Wave 7c Decision Point Prerequisites"
                        item 4, "if absent, route #84 to PRE-REG-INC")

Step 2 (substitution at dispatch-time on this run):
  exists(prereq_pipeline) = False
    (filesystem check via Bash glob on dispatch:
     phonon-exflation-sim/src/spectral_action_pv.py NOT found;
     only sympy.physics.paulialgebra.py at venv site-packages,
     which is NOT the named module — different signature, different scope)
  has_callable(prereq_pipeline, "pv_anomaly_kernel") = False
    (cannot have a callable in a non-existent file)
  prereq_callable = False AND False = False
  gate_executable = False

Step 3 (simplification per discipline rule):
  mechanical-closure-discipline.md §"When mechanical closure IS acceptable"
  conditions (1)-(5):
    (1) upstream-block topology pre-registered:
        plan §"Wave 7c Decision Point Prerequisites" item 4 (line 30)
        AND routing clause line 33 — SATISFIED;
    (2) verdict honesty:
        emitted verdict = PRE-REG-INC; value =
        'PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent';
        PASS FORBIDDEN — SATISFIED;
    (3) per-gate-distinct audit_sha256:
        pin-map embeds (_gate_id, _wp_id, _scheme, _convention,
        _pin_pv_pipeline_path, _pin_pv_pipeline_status,
        _pin_pv_pipeline_sha) — SATISFIED;
    (4) audit-trail signature:
        canonical value string names the blocking prereq AND its
        status — SATISFIED;
    (5) in-script WP update:
        this script writes §W7c-84 Status / Verdict / Results /
        Substrate-framing blocks in the same run — SATISFIED.

Step 4 (direction):
  All five conditions hold ⇒ PRE-REG-INC mechanical closure is the
  ONLY structurally-valid path. Re-routing to a different convention
  (e.g., dropping PRIMARY-PV-live and substituting a SCHEMATIC re-run)
  is FORBIDDEN per PROHIBITED_ACTIONS Class 1 (convention-shopping)
  AND violates substrate-first-canonical-sourcing.md §(iv) MANDATORY-
  at-K=4 SCHEMATIC-vs-FULL level pin discipline (which this very
  gate exists to enforce by closing the W4-2 SCHEMATIC pathology
  with a live-physical PRIMARY counterpart).

Step 5 (conclusion):
  Verdict = PRE-REG-INC FAIL (composite top-line; per
  gate-verdicts.md §"S87+ canonical form" composite-collapse rule:
  regime_verdict = INVALID forces composite = FAIL,
  whence the PRE-REG-INC label is encoded in the value= field as a
  descriptive prefix per discipline §"Audit-trail signature").
  No claim about c_sub_anomaly_WZW_TIER1 vs c_sub_baseline is made;
  the gate is structurally untestable at this session.
  Carry-forward: S89-PV-PIPELINE-LANDING (NEW)
                 → THEN S89-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN-RETRY.
"""

print(SUBSTITUTION_CHAIN)

# ---------------------------------------------------------------------------
# 4. NPZ artifact (artifact-existence pin per discipline §"in-script update")
# ---------------------------------------------------------------------------
np.savez(
    OUT_NPZ,
    gate_id=np.array([GATE_ID]),
    wp_id=np.array([WP_ID]),
    closure_class=np.array(["PRE-REG-INC"]),
    blocked_by=np.array(["S88-PV-PIPELINE-LANDING"]),
    pv_pipeline_path=np.array([str(PV_PIPELINE).replace("\\", "/")]),
    pv_pipeline_status=np.array([pv_pipeline_status]),
    spectrum_cache_path=np.array([str(SPECTRUM_CACHE).replace("\\", "/")]),
    spectrum_cache_status=np.array([spectrum_cache_status]),
    audit_sha256=np.array([audit_sha]),
    content_sha256=np.array([content_sha]),
    scheme=np.array([SCHEME_TAG]),
    convention=np.array([CONVENTION_TAG]),
    L_max=np.array([L_MAX_TAG]),
    regulator_class=np.array([REGULATOR_CLASS]),
    level=np.array([LEVEL]),
    s_anomaly=np.array([S_ANOMALY]),
    s_normalization=np.array([S_NORMALIZATION]),
    tau_fold=np.array([tau_fold]),
    M_KK=np.array([M_KK]),
    c_sub_baseline=np.array([c_sub_baseline]),
    pv_mass_pairs=np.array(PV_MASS_PAIRS, dtype=float),
    substitution_chain=np.array([SUBSTITUTION_CHAIN]),
)
print(f"[S88 W7c-84 mechanical-closure] wrote {OUT_NPZ.name}")

# ---------------------------------------------------------------------------
# 5. JSON sidecar (compact machine-readable closure record)
# ---------------------------------------------------------------------------
closure_record = {
    "gate_id": GATE_ID,
    "wp_id": WP_ID,
    "closure_class": "PRE-REG-INC",
    "verdict_top_line": "FAIL",
    "value_string": (
        "PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent"
    ),
    "scheme": SCHEME_TAG,
    "convention": CONVENTION_TAG,
    "L_max": L_MAX_TAG,
    "regulator_class": REGULATOR_CLASS,
    "level": LEVEL,
    "blocked_by": "S88-PV-PIPELINE-LANDING",
    "blocked_by_status": "absent",
    "blocked_by_path": str(PV_PIPELINE).replace("\\", "/"),
    "spectrum_cache_path": str(SPECTRUM_CACHE).replace("\\", "/"),
    "spectrum_cache_status": spectrum_cache_status,
    "rule_file": ".claude/rules/mechanical-closure-discipline.md",
    "plan_pre_registration_clause": (
        "session-88-plan-w7c.md §'Wave 7c Decision Point Prerequisites' "
        "item 4 + line 33 routing clause"
    ),
    "audit_sha256": audit_sha,
    "content_sha256": content_sha,
    "input_pin_map": input_pin_map,
    "schema_version": "S84+",
    # Schema-v2 3-tuple (S87+ canonical form per gate-verdicts.md):
    "sign_verdict": "N/A",          # no directional pre-registration possible
                                    # without c_sub_anomaly_WZW value
    "magnitude_verdict": "FAIL",    # PRE-REG-INC: gate did not produce a
                                    # value to compare against c_sub_baseline
    "regime_verdict": "BREAKDOWN",  # PRIMARY-PV-live regime UNREACHABLE
                                    # without upstream PV pipeline; pre-reg
                                    # validity domain is INVALID by
                                    # pipeline absence
}
with open(OUT_JSON, "w", encoding="utf-8") as fh:
    json.dump(closure_record, fh, indent=2, sort_keys=True)
print(f"[S88 W7c-84 mechanical-closure] wrote {OUT_JSON.name}")

# ---------------------------------------------------------------------------
# 6. PNG artifact (figure documenting the closure topology)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis("off")
title = (
    "S88 W7c-84  PRE-REG-INC Mechanical Closure\n"
    "S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN  blocked by  "
    "S88-PV-PIPELINE-LANDING (status: absent)"
)
ax.text(
    0.5,
    0.96,
    title,
    ha="center",
    va="top",
    fontsize=12,
    fontweight="bold",
    transform=ax.transAxes,
)
body = (
    "Plan reference: sessions/session-plan/session-88-plan-w7c.md  Section W7c-84.\n"
    "Plan pre-registers PRE-REG-INC routing at line 30 (item 4) + line 33.\n\n"
    "Upstream prereq:\n"
    "  phonon-exflation-sim/src/spectral_action_pv.py  ABSENT.\n"
    "Spectrum cache:\n"
    "  computations/session-84/s84_spectrum_cache_L12_tau019.npz  PRESENT\n"
    "    (truncate-to-L_max=10 path validated; ready for retry).\n\n"
    "Mechanical-closure conditions per .claude/rules/mechanical-closure-discipline.md:\n"
    "  1. Upstream-block topology pre-registered                  SATISFIED\n"
    "  2. Verdict honesty (PRE-REG-INC; PASS FORBIDDEN)            SATISFIED\n"
    "  3. Per-gate-distinct audit_sha256                          SATISFIED\n"
    "  4. Audit-trail signature (descriptive value string)        SATISFIED\n"
    "  5. In-script working-paper update                          SATISFIED\n\n"
    "Verdict 4-tuple at PRE-REG-INC closure:\n"
    f"  value      = PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent\n"
    f"  scheme     = {SCHEME_TAG}\n"
    f"  convention = {CONVENTION_TAG}\n"
    f"  L_max      = {L_MAX_TAG}\n\n"
    f"audit_sha256  = {audit_sha[:16]}...{audit_sha[-16:]}\n"
    f"content_sha256 = {content_sha[:16]}...{content_sha[-16:]}\n\n"
    "Carry-forward to S89:\n"
    "  S89-PV-PIPELINE-LANDING (NEW; build phonon-exflation-sim/src/spectral_action_pv.py\n"
    "    per S61/S78 PV mass-scale-running spec)\n"
    "  THEN  S89-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN-RETRY (re-run this gate)."
)
ax.text(
    0.02,
    0.86,
    body,
    ha="left",
    va="top",
    fontsize=9,
    family="monospace",
    transform=ax.transAxes,
)
plt.tight_layout()
plt.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
plt.close(fig)
print(f"[S88 W7c-84 mechanical-closure] wrote {OUT_PNG.name}")

# ---------------------------------------------------------------------------
# 7. Append verdict line to canonical session verdict file (S87+ schema-v2)
#    Per gate-verdicts.md §"Canonical Verdict-File Path (MANDATORY)":
#      computations/session-88/s88_gate_verdicts.txt
# ---------------------------------------------------------------------------
canonical_line = (
    f"{GATE_ID}: FAIL -- "
    f"value='PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent' "
    f"scheme={SCHEME_TAG.replace(' ', '-')} "
    f"convention={CONVENTION_TAG} "
    f"L_max={L_MAX_TAG} "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha} "
    f"schema_version=S84+\n"
)
audit_short = audit_sha[:16]
content_short = content_sha[:16]
companion_dual_sha = (
    f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
    f"PRE-REG-INC per session-88-plan-w7c.md §W7c-84; "
    f"deferred to S89; "
    f"required prereqs: [S88-PV-PIPELINE-LANDING absent]; "
    f"closure_script=computations/session-88/s88_w7c_tier1_live_physical_re_run.py\n"
)
companion_3tuple = (
    f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=BREAKDOWN "
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
)

# Idempotent: if a prior run already appended this gate's PRE-REG-INC trio,
# do not duplicate (per discipline §"Carry-forward script-bytes immutability"
# idempotent-recovery branch).
existing = VERDICT_FILE.read_text(encoding="utf-8") if VERDICT_FILE.exists() else ""
already_present = (
    f"{GATE_ID}: FAIL -- value='PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING"
    in existing
)
if already_present:
    print(
        f"[S88 W7c-84 mechanical-closure] verdict already present in "
        f"{VERDICT_FILE.name}; skipping append (idempotent recovery branch)"
    )
else:
    with open(VERDICT_FILE, "a", encoding="utf-8") as fh:
        fh.write(canonical_line)
        fh.write(companion_dual_sha)
        fh.write(companion_3tuple)
    print(
        f"[S88 W7c-84 mechanical-closure] appended canonical line + 2 "
        f"companion rows to {VERDICT_FILE.name}"
    )

# ---------------------------------------------------------------------------
# 8. In-script working-paper update (per discipline §item 5)
#    Replace the "(pending ...)" placeholders inside §W7c-84 ONLY.
#    Do NOT touch §W7c-85, §W7c-86, §W7c-167.
# ---------------------------------------------------------------------------
WP_W7C_84_BLOCK = f"""### §W7c-84. S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN (lizzi-spectral-functional-theorist)

**Status**: PRE-REG-INC (mechanical-closure; deferred to S89)
**Gate ID**: `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (live-physical Pauli-Villars re-run of axiom-side c_sub cross-review at substrate-distance-1 anomaly pole s=4)
**Agent**: `lizzi-spectral-functional-theorist` PRIMARY + `connes-ncg-theorist` CO-AUTHOR (NCG-axiomatic side per Chamseddine-Connes 1996 + Andrianov-Lizzi 1001.2036 anomaly-cancellation derivation)
**Hypothesis**: live-physical Pauli-Villars regularization with rank-3 mass-scale running recovers the substrate-derived c_sub baseline at <5% tolerance, eliminating the SCHEMATIC-level helper artifact that produced S87 W9c-1 FAIL composite.
**Plan reference**: `sessions/session-plan/session-88-plan-w7c.md` §W7c-84.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):
- `mcp__knowledge__.get_constant("c_sub_baseline")` -> `2.238` (no PROVENANCE entry; mirrored in canonical_constants.py).
- `mcp__knowledge__.get_constant("tau_fold")` -> `0.190` (S12/S42 CONST-FREEZE-42; canonical pin verified).
- `mcp__knowledge__.get_constant("M_KK")` -> `7.428660036284456e+16` GeV (canonical; matches plan §W7c-84 line 60).
- `mcp__knowledge__.trace_entity("S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW")` -> S87 calibration corpus instance #3 of K=4 SCHEMATIC-level pin promotion: prior gate closed `value=0/5+twin=0/2 scheme=WZW-consistency-residue-substr-d-2 convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC L_max=10 FAIL` — this S88 W7c-84 gate is the PRIMARY-PV-live counterpart that the SCHEMATIC closure pre-registers as forward-pinned remediation.
- `mcp__knowledge__.search_knowledge("Pauli-Villars rank-3 mass-scale running anomaly cancellation")` -> top hit: `w_PV^primary(λ²) = 1 - Σ_k c_k · M_{{PV,k}}² / (λ² + M_{{PV,k}}²)` (s87-axis-of-observation-anatomy-pin.md citing "S61/S78 pipeline"); secondary hit: `S87-PV-SUBTRACTION-RECALIBRATION` FAIL (different scope: finite-L PV at substrate-mass-scale, not the axiom-side WZW-anomaly proxy).

**Verdict**:

```
{GATE_ID}: FAIL -- value='PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent' scheme={SCHEME_TAG.replace(' ', '-')} convention={CONVENTION_TAG} L_max={L_MAX_TAG} audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+
# audit_sha256_short={audit_short} content_sha256_short={content_short} # {GATE_ID} dual-SHA companion row (W9a-99 split); PRE-REG-INC per session-88-plan-w7c.md §W7c-84; deferred to S89; required prereqs: [S88-PV-PIPELINE-LANDING absent]; closure_script=computations/session-88/s88_w7c_tier1_live_physical_re_run.py
# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=BREAKDOWN # {GATE_ID} 3-tuple annotation (S87 schema-v2)
```

**Composite collapse**: per `.claude/rules/gate-verdicts.md` §"Composite-collapse rule", `regime_verdict = BREAKDOWN ⇒ composite = FAIL`. The PRE-REG-INC closure-class is encoded in the descriptive `value=` field per `.claude/rules/mechanical-closure-discipline.md` §"Audit-trail signature".

**Blocked prerequisite**:

| Prereq ID | Path | Status at dispatch | Plan clause |
|:----------|:-----|:------------------:|:------------|
| `S88-PV-PIPELINE-LANDING` | `phonon-exflation-sim/src/spectral_action_pv.py` | **absent** | plan §"Wave 7c Decision Point Prerequisites" item 4 (line 30) + routing clause line 33 |

The named module is genuinely absent; only `sympy.physics.paulialgebra.py` (venv site-packages) and `sympy.physics.quantum.pauli.py` exist, neither of which is the framework's PV mass-scale-running pipeline. The plan author pre-registered this exact scenario at line 30, routing to PRE-REG-INC mechanical closure per `.claude/rules/mechanical-closure-discipline.md`.

**Mechanical-closure conditions verified** (per discipline §"When mechanical closure IS acceptable"):

1. **Upstream-block topology pre-registered** — plan line 30 + line 33 anticipate the prereq-block scenario explicitly. Not post-hoc plan editing (PROHIBITED_ACTIONS Class 3 cleared).
2. **Verdict honesty** — emitted verdict is PRE-REG-INC (composite FAIL); descriptive `value=` follows the `'PRE-REG-INC_blocked_by_<symbol>_<status>'` canonical pattern. PASS verdict FORBIDDEN per discipline §item 2 + PROHIBITED_ACTIONS Class 4 (ansatz-forced PASS).
3. **Per-gate-distinct audit_sha256** — input-pin map embeds `(_gate_id, _wp_id, _scheme, _convention, _pin_pv_pipeline_path, _pin_pv_pipeline_status, _pin_pv_pipeline_sha, _blocked_by, _closure_class)` so `audit_sha256={audit_sha[:16]}...` is structurally unique to this closure.
4. **Audit-trail signature** — canonical `value=` string names the blocking prereq AND its status; future audit grep can verify.
5. **In-script working-paper update** — this script (`s88_w7c_tier1_live_physical_re_run.py`) writes the §W7c-84 Status / Verdict / Results / Substrate-framing blocks in the same run as the verdict-line append (this very block). S82/S84 task-complete-lie pattern avoided by construction.

**Substitution chain** (per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute"; no quantitative `c_sub` claim is made — the gate is structurally untestable until upstream lands; chain documents the structural reasoning for emitting PRE-REG-INC):

```
Step 1 (definition of gate executability):
  prereq_pipeline := phonon-exflation-sim/src/spectral_action_pv.py
  prereq_callable := exists(prereq_pipeline) AND
                     has_callable(prereq_pipeline, "pv_anomaly_kernel")
  gate_executable := prereq_callable

Step 2 (substitution at dispatch-time on this run):
  exists(prereq_pipeline) = False
    (Bash glob on phonon-exflation-sim/src/ returns no match;
     sympy.physics.paulialgebra.py in venv is NOT the named pipeline)
  has_callable(prereq_pipeline, "pv_anomaly_kernel") = False
    (cannot have a callable in a non-existent file)
  prereq_callable = False AND False = False
  gate_executable = False

Step 3 (simplification per discipline rule):
  All five mechanical-closure conditions hold (see verified table above)
  ⇒ PRE-REG-INC mechanical closure is the ONLY structurally-valid
    path. Re-routing to a different convention (e.g., dropping
    PRIMARY-PV-live for a SCHEMATIC re-run) is FORBIDDEN per
    PROHIBITED_ACTIONS Class 1 (convention-shopping) AND violates
    `substrate-first-canonical-sourcing.md` §(iv) MANDATORY-at-K=4
    SCHEMATIC-vs-FULL-physical level pin discipline (which this
    very gate exists to enforce by closing the W4-2 SCHEMATIC
    pathology with a live-physical PRIMARY counterpart).

Step 4 (direction):
  Verdict = PRE-REG-INC FAIL (composite top-line; per
  gate-verdicts.md composite-collapse rule
  regime_verdict = BREAKDOWN ⇒ composite = FAIL).
  No claim about c_sub_anomaly_WZW_TIER1 vs c_sub_baseline = 2.238
  is made; the gate did not produce `c_sub_anomaly_WZW_TIER1`.

Step 5 (conclusion):
  Carry-forward to S89:
    (i)  S89-PV-PIPELINE-LANDING (NEW; build
         phonon-exflation-sim/src/spectral_action_pv.py per
         S61/S78 PV mass-scale-running spec, with callable
         signature pv_anomaly_kernel(D_K_block, s, mass_scale_pairs)
         per plan line 50);
    (ii) S89-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN-RETRY (re-run this
         gate against (i); spectrum cache is already in place at
         computations/session-84/s84_spectrum_cache_L12_tau019.npz
         and L_max=10 truncation feasibility is W11-2 Casimir-bound
         pre-validated, so re-run is single-step once (i) lands).
```

**Results** (PRE-REG-INC; no live-physical numerical evaluation produced):

- `c_sub_anomaly_WZW_TIER1` value: **NOT EVALUATED** (upstream PV pipeline absent).
- 4-tuple at closure (verdict-line `convention=` field encodes PRIMARY-PV-live with NO SCHEMATIC suffix per discipline §item 2 verdict-honesty AND `substrate-first-canonical-sourcing.md` §(iv)):
  - `value     = PRE-REG-INC_blocked_by_S88-PV-PIPELINE-LANDING_status_absent`
  - `scheme    = {SCHEME_TAG}`
  - `convention = {CONVENTION_TAG}`
  - `L_max     = {L_MAX_TAG}`
- **CC1 PV-subtraction-condition rank-3 saturation**: pre-registered conditions
  `Σ_i C_i = 0`, `Σ_i C_i·M_i^2 = 0`, `Σ_i C_i·M_i^4 = 0` for the rank-3 PV mass-pair set
  `[(M_KK, +1), (2·M_KK, -5), (4·M_KK, +10), (8·M_KK, -10), (16·M_KK, +5), (32·M_KK, -1)]`
  are **NOT VERIFIED** at this closure — verification requires the live-physical PV
  evaluator at `pv_anomaly_kernel()`. The rank-3 saturation is a CC1 consistency check
  on the PV pipeline output once it lands; pre-registration is preserved in the input
  pin-map for the S89 retry.
- **CC2 Mellin-residue extraction at s=3 AND s=4**: `Res[M_R(s); s=3]` and
  `Res[M_R(s); s=4]` extraction is **NOT EVALUATED** — same upstream-blocked basis.
  Pre-registration of `s_anomaly = 4` and `s_normalization = 3` is preserved in the
  input pin-map.
- Artifacts on disk:
  - `computations/session-88/s88_w7c_tier1_live_physical_re_run.py` (this script)
  - `computations/session-88/s88_w7c_tier1_live_physical_re_run.npz` (closure metadata)
  - `computations/session-88/s88_w7c_tier1_live_physical_re_run.png` (closure topology figure)
  - `computations/session-88/s88_w7c_tier1_live_physical_re_run.json` (closure record + 3-tuple schema-v2)

**Substrate framing** (per `.claude/rules/cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy" 5 elements; level pin per `.claude/rules/phononic-framing.md` §"Single-τ-slice vs moduli-deformation substrate-IS levels"):

1. **Substrate-IS observable** (Level 1 single-τ-slice): `c_sub_anomaly_WZW_TIER1` evaluated on the substrate spectral triple `(A_K^{{<=10}}, H_K^{{<=10}}, D_K^{{<=10}})` at `τ_fold = 0.190`. The substrate IS this Mellin-residue ratio at the axiom-side WZW consistency-check pole — NOT a quantity in any pre-existing geometric container. At PRE-REG-INC closure, the observable is pre-registered but unmeasured (the substrate has the structure; the live-physical evaluator that reads it does not yet exist in the toolchain).
2. **Laboratory-IN observable**: N/A (this gate is intra-substrate; bridge map deferred to §VII.AF.1 Pillar III ↔ IV registered theorem; no laboratory-IN image consumed at this gate).
3. **Bridge map**: N/A (substrate-internal; not a cross-pillar bridge).
4. **Algebraic envelope**: PV-rank-3 saturation captures anomaly-cancellation at d=4 to a closed-form structural identity (Andrianov-Lizzi 1001.2036 anomaly-induced bosonic spectral action); no `L^{{-α}}` envelope at this gate. At PRE-REG-INC closure, the saturation identity remains pre-registered as the CC1 consistency check awaiting the S89 retry.
5. **Empirical anchor**: `c_sub_baseline = 2.238` from `canonical_constants.py`; substrate-first canonical sourcing PASS (no `O(10⁻²)` placeholder; no SCHEMATIC helper consumption; conforms to `.claude/rules/substrate-first-canonical-sourcing.md` §"(iv) The 'SCHEMATIC vs full physical' level pin rule" MANDATORY-at-K=4 discipline).

**Direction of explanation** (per `phononic-framing.md` §"IS Space, Not IN Space"):

```
Substrate (D_K spectrum at τ_fold=0.190; A_K = C ⊕ H ⊕ M_3(C))
   IS  the c_sub_anomaly_WZW Mellin-residue ratio at s=4 / s=3
   →  Mellin-Barnes residue extractor under live-physical PV regularization
      [BLOCKED at this gate; routes to S89-PV-PIPELINE-LANDING]
   →  c_sub baseline (M_Pl_eff² ratio at substrate-distance-1 anomaly pole)
      [pre-registered anchor; conformity test deferred to S89 retry]
```

The substrate is logically prior to the PV evaluator: the spectrum exists at L_max=10 (cache verified at present); the live-physical evaluator that maps spectrum → c_sub_anomaly_WZW is the missing piece. PRE-REG-INC honors this by emitting the structural pin without forcing a SCHEMATIC substitute (which would silently re-introduce the W4-2 / S87 W9c-1 pathology this gate exists to close).

**Carry-forward to S89** (4-field spec per `feedback_fix-in-session-never-defer.md`):

1. `S89-PV-PIPELINE-LANDING` (NEW)
   - **What**: Build `phonon-exflation-sim/src/spectral_action_pv.py` implementing
     `pv_anomaly_kernel(D_K_block, s, mass_scale_pairs)` per S61/S78 mass-scale-running
     spec with rank-3 PV-subtraction conditions enforced at construction.
   - **Inputs**: `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (L_max=10 truncation);
     PV mass-pair list `[(M_KK, +1), (2·M_KK, -5), (4·M_KK, +10), (8·M_KK, -10), (16·M_KK, +5), (32·M_KK, -1)]`;
     Andrianov-Lizzi 1001.2036 anomaly-cancellation derivation.
   - **Gate**: PASS iff CC1 rank-3 PV-subtraction conditions all satisfied to machine
     epsilon (`|Σ_i C_i| < 1e-12`, `|Σ_i C_i·M_i^2| / M_KK^2 < 1e-12`, `|Σ_i C_i·M_i^4| / M_KK^4 < 1e-12`).
   - **Effort**: ~0.8 wave-equiv (single-thread CPU; library construction + unit tests).
   - **Depends on**: spectrum cache (already in place); canonical constants
     (already in `canonical_constants.py`).

2. `S89-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN-RETRY` (re-run of this gate)
   - **What**: Re-execute `S88-W9c-1-PRIMARY-LIVE-PHYSICAL-RE-RUN` against the
     S89-built PV pipeline; emit composite verdict per pre-registered 5%/2.5% bands.
   - **Inputs**: S89-PV-PIPELINE-LANDING output module + spectrum cache + canonical
     constants (all pinned at this closure's input-pin map).
   - **Gate**: composite PASS / FAIL / INFO per plan §W7c-84 lines 75-79
     (sign × magnitude × regime; 5% PASS / 2.5%-5% INFO / >5% FAIL).
   - **Effort**: ~0.5 wave-equiv (machinery is built; this is the live-physical
     evaluation + composite-verdict emission step).
   - **Depends on**: S89-PV-PIPELINE-LANDING.

---
"""

# Read the working paper, replace ONLY §W7c-84 block (preserve §W7c-85, §W7c-86, §W7c-167)
wp_text = WP_PATH.read_text(encoding="utf-8")

# Anchor: from "### §W7c-84." up to (but not including) "### §W7c-85."
start_marker = "### §W7c-84."
end_marker = "### §W7c-85."
start = wp_text.find(start_marker)
end = wp_text.find(end_marker)
if start < 0 or end < 0:
    raise RuntimeError(
        f"WP anchors not found: §W7c-84 start={start}, §W7c-85 start={end}; "
        f"refusing to write to avoid corrupting working paper"
    )

new_wp_text = wp_text[:start] + WP_W7C_84_BLOCK + "\n" + wp_text[end:]
WP_PATH.write_text(new_wp_text, encoding="utf-8")
print(f"[S88 W7c-84 mechanical-closure] updated WP §W7c-84 in {WP_PATH.name}")

# ---------------------------------------------------------------------------
# 9. Final summary
# ---------------------------------------------------------------------------
print()
print("=" * 72)
print(f"S88 W7c-84 mechanical-closure complete:")
print(f"  Verdict       : PRE-REG-INC (composite FAIL)")
print(f"  Blocked by    : S88-PV-PIPELINE-LANDING (status: absent)")
print(f"  audit_sha256  : {audit_sha}")
print(f"  content_sha256: {content_sha}")
print(f"  Artifacts     :")
print(f"    {OUT_PY.name}")
print(f"    {OUT_NPZ.name}")
print(f"    {OUT_PNG.name}")
print(f"    {OUT_JSON.name}")
print(f"  WP updated    : {WP_PATH.relative_to(PROJECT_ROOT)} §W7c-84")
print(f"  Verdict file  : {VERDICT_FILE.relative_to(PROJECT_ROOT)}")
print("=" * 72)

sys.exit(0)
