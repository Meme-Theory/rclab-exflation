#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S118 W0-3 CF-S118-HK-ROW79-DISCHARGE — Row #79 170× KINEMATIC-survival discharge-confirmation
=============================================================================================

Gate: CF-S118-HK-ROW79-DISCHARGE ([VERIFY])
Classification: NON-PHONONIC (registry-hygiene / discharge-confirmation sub-row landing;
  the Row #79 DM physics is PHONONIC, the GATE is the sub-row landing).

GREP-VERIFIER CANONICAL-IMPORT EXEMPTION (pre-registered): PURE grep-verifier; consumes NO
canonical constant. MUST NOT import canonical_constants.py; canonical_constants.py is
DELIBERATELY ABSENT from input_files + the audit_sha256 pinmap. (Reading
`s117_gate_verdicts.txt` is a verdict file, NOT a canonical import.) The python-validate.sh
Check-1 WARN is a pre-registered WARN-only exemption per
`feedback_grep-verifier-canonical-import-exemption.md` (S117 W0-2); do NOT add a dead import.

Pre-registered threshold (verify-then-land artifact-existence; NOT a numerical threshold):
  PART A (verify): the three S117 W4 verdict lines exist in computations/session-117/
    s117_gate_verdicts.txt with verdict==PASS and the pinned audit SHAs present —
      CF-S117-FREESTREAM-AT-ANCHOR        audit 409637d4… (λ_fs^4D=0, cold, 170x-DISCHARGED)
      CF-S117-LEGGETT-COLLECTIVE-CEILING  audit 2714a45a… (frac170=0.070412)
      CF-S117-LEGGETT-EDGE-AND-STIFFNESS  audit ba745a65… (x^⊥=2.530217>1)
  PART B (PASS predicate, artifact-existence): a Row #79.audit-S117-W4 discharge-confirmation
    sub-row is present in falsifier-master-inventory.md, flipping
    "discharge owed / NOT asserted-closed" -> "discharged on three orthogonal axes" and
    citing the three S117 W4 audit SHAs.
  PASS iff (PART A all-three verified PASS) AND (PART B sub-row landed + must_contain match).
  A required line absent/not-PASS -> honest FAIL-with-remediation per
  `.claude/rules/mechanical-closure-discipline.md` (NOT a forced PASS).

LOAD-BEARING SCOPE: the discharge is KINEMATIC survival of the 170×-re-typed object ONLY
(the cross-pillar n_s/Leggett ratio, x_target=30.12 unprotectable). It does NOT touch the
σ_SI NULL (1.299e-63 cm², ≥26.5 OOM below LZ-2024), Ω_DM h²=0.120 (LEGGETT-MOMENT-70,
C11-conditional), or the Reading-A survival argument — all UNCHANGED.

Single-shot AFTER-pattern (build text -> write_atomic_with_fsync -> re-read+verify -> emit
exactly one verdict line) per `.claude/rules/registry-landing.md` §"Bridge-Landing Script
Architecture". Surgical insertion designated-writer patch (NOT a bulk append).

Provenance: S118 W0-3 plan `sessions/session-plan/session-118-plan-w0.md` §W0-3.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S118"                                                # (local)
GATE_ID = "CF-S118-HK-ROW79-DISCHARGE"                          # (local)
SCHEME = "FALSIFIER-INVENTORY-SUBROW-LANDING"                   # (local)
CONVENTION = "DISCHARGE-CONFIRMATION-three-orthogonal-axes-KINEMATIC-survival-Reading-A-UNCHANGED"  # (local)
L_MAX = "N/A"                                                   # (local)

INVENTORY = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
S117_VERDICTS = PROJECT_ROOT / "computations" / "session-117" / "s117_gate_verdicts.txt"

# PART A — the three S117 W4 PASS lines to verify (gate_id -> full audit_sha256).
S117_W4 = {
    "CF-S117-FREESTREAM-AT-ANCHOR":
        "409637d4373418082bf855ab8e6146b0006ba8d16334fc5497f5698255ca43b8",
    "CF-S117-LEGGETT-COLLECTIVE-CEILING":
        "2714a45ab512271158f599303931b2c2dab115c5059447d633727078934d0e5e",
    "CF-S117-LEGGETT-EDGE-AND-STIFFNESS":
        "ba745a655acbec1a499e5a0bffd613940667a30ccdc65058eac8f056db90f678",
}

# Insertion anchor (unique via the Row #93 header): land the sub-row AFTER the corrigendum
# sub-row (its tail "(AMRI-PROMOTED 2026-04-28).") and BEFORE the '---' that precedes Row #93.
ANCHOR = ("(AMRI-PROMOTED 2026-04-28).\n\n---\n\n## NEW Row #93 — exflation horizon "
          "/ flatness / scale-range obligation cluster:")

SUBROW_MARKER = "### Row #79.audit-S117-W4 —"

SUBROW = """### Row #79.audit-S117-W4 — the three pre-registered Row #79-family "discharge owed / NOT asserted-closed" obligations on the 170× DM-mass KINEMATIC-survival axis are DISCHARGED on three orthogonal axes (S117 W4 all PASS: cold free-streaming λ_fs⁴ᴰ=0 / collective-mode ceiling frac170=0.070412 / Leggett edge x^⊥=2.530217>1); KINEMATIC scope ONLY — the σ_SI NULL, Ω_DM h²=0.120, and the Reading-A survival argument are UNCHANGED (S118 W0-3 verify-then-land discharge-confirmation; mack-cosmic-bridge sole-writer landing)

> **THIS IS A DISCHARGE-CONFIRMATION sub-row on the Row #79 σ_SI DM-nucleon NULL — NOT a new prediction value, NOT a status flip on the σ_SI NULL, and NOT a substrate-physics status change.** It records that the THREE forward "discharge owed / NOT asserted-closed" obligations the S116 Row #79 family pre-registered on the 170× DM-mass KINEMATIC-survival axis have ALL PASSED at S117 W4. The discharge is KINEMATIC survival of the 170×-re-typed object ONLY (the cross-pillar n_s/Leggett ratio, x_target=30.12 unprotectable, per Row #79.compute-S116-W3-DISORDER-CLOSURE); it does NOT touch the σ_SI = 1.299e-63 cm² NULL (anchor-robust, ≥26.5 OOM below LZ-2024), the Ω_DM h²=0.120 abundance (LEGGETT-MOMENT-70, C11-conditional), or the DM survival reading (Reading A — CPT non-annihilation [J,D_K]=0 + GGE integrability S_ent=0/R_therm=5252 + Γ_grav<H₀, C11-conditional). NO `canonical_constants` pin (the three values are already pinned in the S117 W4 verdict lines; this is an artifact-existence verify-then-land — canonical write-order Step 2 N/A).

**The three orthogonal discharge axes (S117 W4, all PASS — verified present in `computations/session-117/s117_gate_verdicts.txt`):**

| Axis (S116 Row #79 owed obligation) | S117 W4 gate | Result (pinned in the verdict line) | audit_sha256 |
|:------------------------------------|:-------------|:------------------------------------|:-------------|
| (1) free-streaming / cold | `CF-S117-FREESTREAM-AT-ANCHOR` **PASS** | λ_fs⁴ᴰ = 0 EXACT (v_fs⁴ᴰ = 3.04e-17); z_tr = 6.754e29 ≫ z_thr (22.0 OOM); cold; "170x-DISCHARGED" | `409637d4373418082bf855ab8e6146b0006ba8d16334fc5497f5698255ca43b8` |
| (2) collective-mode ceiling | `CF-S117-LEGGETT-COLLECTIVE-CEILING` **PASS** | frac170 = 0.070412 ∈ [0.06, 0.08]; 170× needs p+q ~ 212 (√N-saturated, structurally unreachable) | `2714a45ab512271158f599303931b2c2dab115c5059447d633727078934d0e5e` |
| (3) Leggett edge / stiffness | `CF-S117-LEGGETT-EDGE-AND-STIFFNESS` **PASS** | ω_Leg = 5.5571 M_KK sits x^⊥ = 2.530217 > 1 ABOVE the inter-band sharp-mode edge E_edge^⊥ = 4.731·Δ_BCS; eq(15c) WITHDRAWN; NOT-survival (Reading A) | `ba745a655acbec1a499e5a0bffd613940667a30ccdc65058eac8f056db90f678` |

**Status flip (the owed discharge).** The S116 Row #79 family (Row #79.compute-S116-W3-DISORDER-CLOSURE + the S116-W2 corrigendum) pre-registered these three as "discharge owed / NOT asserted-closed" — the 170×-re-typing carried ZERO evidential weight until the discharge computes ran. They have now ALL run and PASSED ⇒ the owed discharge flips "discharge owed / NOT asserted-closed" → **discharged on three orthogonal axes**. The three axes map 1:1 to the S116 family's owed obligations (free-streaming/cold ← the structure-formation discharge ROUTED to CF-S117-FREESTREAM-AT-ANCHOR; collective-mode ceiling ← the clean inter-band Leggett J_⊥ frac170 channel; Leggett edge ← the S116-W2 corrigendum's CF-S117-LEGGETT-EDGE-AND-STIFFNESS forward gate).

**LOAD-BEARING SCOPE (what is UNCHANGED).** The discharge is KINEMATIC survival of the 170×-re-typed object ONLY. UNCHANGED: (a) the σ_SI = 1.299e-63 cm² INVERTED falsifier (Row #79 primary; any confirmed DM-nucleon scattering above the gravitational floor still kills the Leggett-DM identity; ≥26.5 OOM below LZ-2024, anchor-robust); (b) Ω_DM h² = 0.120 (LEGGETT-MOMENT-70, C11-conditional on Γ_grav < H₀); (c) the Reading-A survival argument (CPT + GGE integrability + Γ_grav < H₀, C11-conditional). This sub-row records the KINEMATIC discharge; it does NOT adjudicate Reading A vs Reading B (priors UNCHANGED on that axis) and does NOT weaken the INVERTED σ_SI falsifier.

**Substrate framing (PHONONIC).** The Leggett-channel GGE quasiparticle DM IS an inter-band relative-phase coherence mode of the post-transit B2⊕B3 substrate (read FORWARD from the D_K spectrum at τ_fold, CPT-neutral, non-annihilating). The KINEMATIC discharge is read FORWARD from the D_K spectrum: the DM is cold (free-streaming λ_fs⁴ᴰ = 0, algebraic per CDM-CONSTRUCT-44), the disorder→Goldstone-mass route is magnitude-excluded at every projection (collective-mode ceiling frac170 = 0.0704, √N-saturated), and the heavy Leggett anchor sits above its inter-band sharp-mode edge (x^⊥ = 2.530217 > 1). Direction preserved (substrate → D_K spectrum → Leggett mode → emergent DM observable); no container inversion.

**Provenance**: S118 W0-3 gate `CF-S118-HK-ROW79-DISCHARGE` [VERIFY] (verify-then-land artifact-existence; `scheme=FALSIFIER-INVENTORY-SUBROW-LANDING`, `convention=DISCHARGE-CONFIRMATION-three-orthogonal-axes-KINEMATIC-survival-Reading-A-UNCHANGED`; verdict line in `computations/session-118/s118_gate_verdicts.txt`, emitted via the `emit_verdict` knowledge-MCP tool; producing/verifier script `computations/session-118/s118_w0_row79_discharge.py`, a grep-verifier consuming NO canonical constant — reading the S117 verdict file is NOT a canonical import). The three discharged S117 W4 gates (verdict lines + audit SHAs VERIFIED PRESENT in `computations/session-117/s117_gate_verdicts.txt`): **`CF-S117-FREESTREAM-AT-ANCHOR`** PASS `audit_sha256=409637d4373418082bf855ab8e6146b0006ba8d16334fc5497f5698255ca43b8` (λ_fs⁴ᴰ=0, cold, 170x-DISCHARGED); **`CF-S117-LEGGETT-COLLECTIVE-CEILING`** PASS `audit_sha256=2714a45ab512271158f599303931b2c2dab115c5059447d633727078934d0e5e` (frac170=0.070412); **`CF-S117-LEGGETT-EDGE-AND-STIFFNESS`** PASS `audit_sha256=ba745a655acbec1a499e5a0bffd613940667a30ccdc65058eac8f056db90f678` (x^⊥=2.530217>1). NO new canonical value (the three values are already pinned in the S117 W4 verdict lines; this is an artifact-existence verify-then-land — canonical write-order Step 2 N/A). Cross-link Row #79 (the σ_SI DM-nucleon NULL primary — UNCHANGED), Row #79.compute-S116-W3-DISORDER-CLOSURE (the 170× re-typing + the structure-formation discharge ROUTED to CF-S117-FREESTREAM-AT-ANCHOR — now DISCHARGED), Row #79.compute-corrigendum-S116-W2-PROTECTION-MAGNITUDE-RESCOPE (the E_edge^⊥ ceiling + the CF-S117-LEGGETT-EDGE-AND-STIFFNESS forward gate — now DISCHARGED, x^⊥=2.530217>1), Row #79.compute-S114-W3-2-HK-170X-DM-MISATTRIB (the mis-attribution record), LEGGETT-MOMENT-70 (Ω_DM h²=0.120, C11-conditional, UNCHANGED), atlas-04 P2 (the 170× standing gap — KINEMATIC survival now discharged; the EVOI §1 170× DM-mass gap "RESOLVED-on-kinematics" mark is the orchestrator's MAINTAIN action at the S118 re-stamp, NOT this gate). NO forward gate on the σ_SI NULL (anchor-robust, unchanged); the KINEMATIC discharge is closed on three orthogonal axes. Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole writer for `falsifier-master-inventory.md` (AMRI-PROMOTED 2026-04-28)."""


# ---------------------------------------------------------------------------
# SHA helpers
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_atomic_with_fsync(text: str, path: Path) -> None:
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


# ---------------------------------------------------------------------------
# PART A — verify the three S117 W4 PASS lines
# ---------------------------------------------------------------------------
def verify_s117_w4(verdict_text: str) -> dict:
    results = {}  # (local)
    for line in verdict_text.splitlines():
        for gid, sha in S117_W4.items():
            if line.startswith(gid + ":"):
                is_pass = (" PASS " in line) or line.startswith(gid + ": PASS")  # (local)
                sha_ok = sha in line                                            # (local)
                results[gid] = {"pass": is_pass, "sha_ok": sha_ok, "audit_sha256": sha}
    all_ok = (len(results) == 3) and all(r["pass"] and r["sha_ok"] for r in results.values())  # (local)
    return {"per_gate": results, "all_three_pass": all_ok}


# ---------------------------------------------------------------------------
# Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          companion_note: str = "") -> dict:
    payload: dict = {
        "session": 118,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} — input SHA-256 pins (grep-verifier; NO canonical_constants) ===")
    print(f"  s117_gate_verdicts.txt:               {sha256_of(S117_VERDICTS)[:16]}...")
    print(f"  falsifier-master-inventory.md (pre):  {sha256_of(INVENTORY)[:16]}...")
    print()

    # PART A — verify the three S117 W4 PASS lines.
    s117_text = S117_VERDICTS.read_text(encoding="utf-8")
    va = verify_s117_w4(s117_text)
    print("--- PART A: verify three S117 W4 PASS lines ---")
    for gid in S117_W4:
        r = va["per_gate"].get(gid)
        print(f"  {gid}: {r}")
    print(f"  all_three_pass: {va['all_three_pass']}")
    print()

    if not va["all_three_pass"]:
        # Honest mechanical closure: a required upstream line is absent/not-PASS.
        audit_sha = sha256_text(sha256_of(Path(__file__).resolve())
                                + json.dumps(va, sort_keys=True, default=str))
        content_sha = sha256_text("FAIL:s117-w4-prereq-not-met:" + json.dumps(va, sort_keys=True, default=str))
        val = "PRE-REG-INC_blocked_by_S117-W4_prereq_not_all_PASS_NO_LANDING"
        print_verdict_payload("FAIL", val, audit_sha, content_sha,
                              companion_note="S118 W0-3 FAIL-with-remediation per mechanical-closure-discipline.md: a required S117 W4 PASS line was absent/not-PASS; sub-row NOT landed")
        print(f"\n=== {GATE_ID}: FAIL (wall {time.time()-t0:.2f}s) ===")
        return 1

    # PART B — single-shot landing (build -> write+fsync -> re-read+verify).
    original = INVENTORY.read_text(encoding="utf-8")
    if SUBROW_MARKER in original:
        new_text = original
        inserted_now = False  # (local)
    else:
        if original.count(ANCHOR) != 1:
            raise RuntimeError(f"insertion anchor not unique (count={original.count(ANCHOR)}); refusing to patch")
        head, sep, tail = ANCHOR.partition("\n\n---\n\n## NEW Row #93")
        # head == "(AMRI-PROMOTED 2026-04-28)."
        replacement = head + "\n\n" + SUBROW + sep + tail
        new_text = original.replace(ANCHOR, replacement, 1)
        inserted_now = True  # (local)

    if new_text != original:
        write_atomic_with_fsync(new_text, INVENTORY)
        print("--- PART B: discharge sub-row INSERTED (surgical, single-shot) ---")
    else:
        print("--- PART B: discharge sub-row ALREADY PRESENT (idempotent no-op) ---")

    landed = INVENTORY.read_text(encoding="utf-8")  # final re-read (post-fsync)

    # Verify: sub-row present + must_contain patterns + anchor consumed once + Row #93 intact.
    marker_ok = SUBROW_MARKER in landed                       # (local)
    block_ok = SUBROW in landed                               # (local)
    mc1 = re.search(r"(discharged on three orthogonal axes|discharge owed.{0,40}(discharged|no-row)"
                    r"|latest-synthesis-wins)", landed) is not None  # (local)
    mc2 = re.search(r"(2\.530217|x\^⊥|0\.070412|frac170|λ_fs|lambda_fs)", landed) is not None  # (local)
    mc3 = re.search(r"(409637d4|2714a45a|ba745a65)", landed) is not None  # (local)
    subrow_once = landed.count(SUBROW_MARKER) == 1            # (local)
    row93_intact = "## NEW Row #93 — exflation horizon" in landed  # (local)
    all_ok = bool(marker_ok and block_ok and mc1 and mc2 and mc3 and subrow_once and row93_intact)

    print("--- PART B verify ---")
    print(f"  marker_ok={marker_ok} block_ok={block_ok} mc1={mc1} mc2={mc2} mc3={mc3} "
          f"subrow_once={subrow_once} row93_intact={row93_intact}")
    print(f"  => all_ok: {all_ok}")
    print()

    verdict = "PASS" if all_ok else "FAIL"

    # Dual-SHA: audit over (script || pinmap) — NO canonical (grep-verifier).
    # content over the landed discharge sub-row text.
    script_path = Path(__file__).resolve()
    pins = {
        str(INVENTORY.relative_to(PROJECT_ROOT)).replace("\\", "/"): sha256_of(INVENTORY),
        str(S117_VERDICTS.relative_to(PROJECT_ROOT)).replace("\\", "/"): sha256_of(S117_VERDICTS),
    }
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_path.read_bytes())
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()           # (local)
    content_sha = sha256_text(SUBROW)         # (local) landed sub-row text

    value = ("verify(3xS117-W4 PASS)=True [FREESTREAM 409637d4/COLLECTIVE-CEILING 2714a45a/"
             "EDGE-STIFFNESS ba745a65]; Row#79.audit-S117-W4 sub-row LANDED -> "
             "discharged on three orthogonal axes (λ_fs⁴ᴰ=0 / frac170=0.070412 / x^⊥=2.530217>1); "
             "KINEMATIC scope only — σ_SI NULL / Ω_DM h²=0.120 / Reading-A survival UNCHANGED")
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(verdict, value, audit_sha, content_sha)
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time()-t0:.2f}s) ===")
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
