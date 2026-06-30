#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S92 W9-4: S92-W9-CF-W7-4-VII-AT-VII-AW-OP-PROJ-FAIL-DIAGNOSTIC-LANDING
=====================================================================

Gate: S92-W9-CF-W7-4-VII-AT-VII-AW-OP-PROJ-FAIL-DIAGNOSTIC-LANDING  ([VERIFY])
Class: NON-PHONONIC (METHODOLOGY-class per `.claude/rules/wave-classification.md`
       M1-M4 strict conjunction; PASS predicate is artifact-existence-with-
       substantive-content, NOT a numerical threshold).
Agent: mack-cosmic-bridge (sole writer of `sessions/permanent-results-registry.md`
       per `feedback_mack-bridge-role.md`).

WHAT THIS GATE DOES
-------------------
Lands TWO FAIL-diagnostic registry blocks documenting the S91 W7 substrate-physics
verdicts that REJECTED the two alternative-chirality candidate substrates:

  - §VII.AT.OP-PROJ (Bi-Chirality, gamma_9' = gamma_5 (+) gamma_F direct-sum):
    cites S91 W7-2a verdict
    audit_sha256=9ae27d0ef191269b075f680b8f21ab73e27385d7afc6e3fb723d8adabdbaa874
    (axiom 5' FAIL at 1.697 + KO-dim shift 6 -> 0 non-physical CPT class +
     bridge maps 1/3 PASS + Level-2 non-binding).

  - §VII.AW.OP-PROJ (SU(3)-Coloured, gamma_9'' = gamma_F^c):
    cites S91 W7-2b verdict
    audit_sha256=be8006d66cedb1cb2b207f1faad0d8a1dadc4067bb8d1eff45c561a3f1e1755d
    (axiom 5'' FAIL at 3.274 + KO-dim stays 6, CM-2008 §11 shift to 2 mod 8 NOT
     realized at colour-signs (+1,-1,+1) + bridge maps 1/3 PASS + Level-2 non-binding).

STAGE-0-CANDIDATE RETAINED at both slots; no promotion. §VII.AQ.OP-PROJ
(tensor-product gamma_9 = gamma_5 (x) gamma_F, KO-dim = 6 BDI) remains the
substrate's SOLE valid spectral-triple chirality structure.

DERIVATIVE-OUTPUT SOURCING (per Write-hook discipline)
------------------------------------------------------
The FAIL-diagnostic content is VERBATIM-DERIVED from prior closed artifacts,
NOT first-principles new derivation (M3 source-of-truth type):
  - Numeric verdicts (1.697, 3.274, KO-dim 0/6, bridge 1/3, Level-2 non-binding):
    `sessions/archive/session-91/session-91-w7-workingpaper.md` §W7-2a (lines 146, 153-167)
    + §W7-2b (lines 243-267) + Wrap-Up table (lines 386-387, 396-398).
  - Verdict-line SHAs: `computations/session-91/s91_gate_verdicts.txt` lines 243-247.
  - The WP itself (lines 191 + 289) queues "mack-cosmic-bridge sole-writer
    registry-update ... populate FAIL diagnostic block ... STAGE-0-CANDIDATE
    RETAINED" — this gate executes that queued task.

PLAN-TEXT-DRIFT CORRECTION (per `substrate-first-canonical-sourcing.md §(ii.B)`)
-------------------------------------------------------------------------------
The plan §W9-4 cites registry lines 17237 / 17293 for the two slots. On-disk
(at this gate's runtime) the chirality-candidate blocks are at lines 17429
(§VII.AT.OP-PROJ "Bi-Chirality Spectral Triple") and 17485 (§VII.AW.OP-PROJ
"SU(3)-Coloured Chirality Spectral Triple"). The line numbers DRIFTED between
plan-freeze and runtime; the slot label §VII.AW.OP-PROJ is moreover REUSED for
a structurally-distinct theorem (SUBSTRATE-CLOCK-UNIQUENESS-THEOREM at a later
registry line). This script RESOLVES the landing targets by CONTENT (header
title keyword), NOT by line number, and splices the FAIL-diagnostic into each
block's `**Source**:`/`---` boundary (append-only, non-destructive).

REGISTRY-LANDING ARCHITECTURE (single-shot AFTER-pattern)
---------------------------------------------------------
Per `registry-landing.md §"Bridge-Landing Script Architecture (single-shot
pattern)"` + `_bridge_landing_script_template.py`:
  build_promotion_text (in memory) -> write_atomic_with_fsync (anchor splice)
  -> re_read + verify_section_matches -> emit ONE composite verdict.
No conditional rewrite. If verify FAILs, the gate emits FAIL once and closes
honestly per `mechanical-closure-discipline.md`.

REGISTRY-WRITE HYGIENE (parallel-writer race; per `epistemic-discipline.md`
§"Registry-Write Hygiene under Parallel-Writer Race")
-------------------------------------------------------------------------------
The two FAIL-diagnostic blocks are spliced via a single read-modify-write of
the registry file: read current bytes, locate each anchor by content, insert
both blocks, write back atomically (temp-file + os.replace + fsync). This is a
single atomic swap, not two Edit-tool mtime-conditional round-trips, so a
concurrent writer cannot interleave a half-applied state.

S92 W0 OVERLAP CHECK (per `mechanical-closure-discipline.md`)
------------------------------------------------------------
Before landing, the script checks whether the FAIL-diagnostic blocks already
exist on disk (cited SHA fragments 9ae27d0ef191269b / be8006d66cedb1cb already
present in the registry). If BOTH are already present with substantive content,
the script honestly CLOSES with verdict INFO and
value='upstream_S92_W0_landing_already_discharged' (NO double-land).

VERDICT SEMANTICS (per `math-scripts.md §"Exit Codes and Verdict Semantics"`)
----------------------------------------------------------------------------
Verdict (PASS/FAIL/INFO) is DATA in the verdict line. Exit code 0 = script ran
successfully regardless of the scientific verdict. Exit != 0 only on script
breakage (missing input, traceback).

GPU path: cpu (registry-text edit; no eigvals, no matrix ops) per plan §machinery_pin_map.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403  (canonical-constants import discipline, S34+)

# ============================ Gate-block constants ============================
GATE_ID = "S92-W9-CF-W7-4-VII-AT-VII-AW-OP-PROJ-FAIL-DIAGNOSTIC-LANDING"
SCHEME = "registry-text-FAIL-diagnostic-landing-single-shot-AFTER-pattern"
CONVENTION = ("mack-sole-writer-VII-AT-VII-AW-OP-PROJ-FAIL-DIAGNOSTIC-LANDING-"
              "S91-W7-VERDICT-CITATIONS")
L_MAX_TAG = "N/A"  # METHODOLOGY-class registry-text edit; no L_max truncation

# Full 64-char audit_sha256 of the two cited S91 W7 verdicts (per plan §W9-4 +
# verified present in computations/session-91/s91_gate_verdicts.txt lines 243-247).
W7_2A_AUDIT_SHA = "9ae27d0ef191269b075f680b8f21ab73e27385d7afc6e3fb723d8adabdbaa874"
W7_2A_CONTENT_SHA = "01b95bba9bbb8b4dae0b4db4df3879e16a63e8159827989740416ac043efb028"
W7_2B_AUDIT_SHA = "be8006d66cedb1cb2b207f1faad0d8a1dadc4067bb8d1eff45c561a3f1e1755d"
W7_2B_CONTENT_SHA = "d7432bd2e1c74d4c50042605c3967581e859bdc28e996f3efb347c5a6273a557"

SUBSTANTIVE_LINE_FLOOR = 15  # (local) — plan §W9-4 PASS predicate (d) floor: each block >= 15 substantive lines

PROJECT_ROOT = ROOT
SHARED_DIR = ROOT / "computations" / "_shared"
SESSION_92_DIR = ROOT / "computations" / "session-92"
SESSION_91_DIR = ROOT / "computations" / "session-91"
VERDICT_TXT = SESSION_92_DIR / "s92_gate_verdicts.txt"
OUT_NPZ = SESSION_92_DIR / "s92_w9_4_vii_at_vii_aw_op_proj_fail_diagnostic_landing.npz"

REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
S91_VERDICTS = SESSION_91_DIR / "s91_gate_verdicts.txt"
S91_W7_WP = ROOT / "sessions" / "session-91" / "session-91-w7-workingpaper.md"
THIS_SCRIPT = Path(__file__).resolve()

# Pinned input files (per plan §input_files)
INPUT_FILES = [
    S91_VERDICTS,
    REGISTRY,
    S91_W7_WP,
    SHARED_DIR / "canonical_constants.py",
]

# Content-based slot anchors (NOT line numbers; per plan-text-drift correction).
# Each tuple: (slot label, header title keyword, the cited-SHA fragment used to
# detect prior landing).
AT_HEADER_KEY = "## §VII.AT.OP-PROJ — Bi-Chirality Spectral Triple"
AW_HEADER_KEY = "## §VII.AW.OP-PROJ — SU(3)-Coloured Chirality Spectral Triple"


# ============================ SHA helpers ============================
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_text(text: str) -> str:
    """content_sha256 over a registry block text (UTF-8). Used for the
    AFTER-pattern verify step (build-in-memory hash vs on-disk hash)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha = SHA(script_bytes).  (Canonical helper idiom; matches
       computations/session-92/s92_w9_5_*.py compute_dual_sha.)"""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


def substantive_line_count(block_text: str) -> int:
    """Count non-blank, non-separator lines in a block (plan PASS predicate (d))."""
    n = 0  # (local)
    for ln in block_text.splitlines():
        s = ln.strip()  # (local)
        if not s:
            continue
        if s == "---":
            continue
        n += 1
    return n


# ============================ build_promotion_text (pure; no I/O) ============================
def build_at_fail_diagnostic() -> str:
    """§VII.AT.OP-PROJ Bi-Chirality FAIL-diagnostic block. Verbatim-derived
    from S91 W7-2a (WP §W7-2a lines 146, 153-167; verdict
    audit_sha256=9ae27d0e...)."""
    return (
        "\n"
        "### FAIL-DIAGNOSTIC (S92 W9-4 CF-W7-4 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-23)\n"
        "\n"
        "**S91 W7-2a substrate-physics verdict** (`computations/session-91/s91_gate_verdicts.txt`; "
        f"gate `S91-VII-AT-OP-PROJ-7-AXIOM`; FAIL; full `audit_sha256={W7_2A_AUDIT_SHA}` "
        f"content_sha256=`{W7_2A_CONTENT_SHA}`; scheme=bi-chirality-direct-sum; "
        "convention=substrate-distance-1-FULL-CONNES-1996-BICHIRALITY; L_max=12): the bi-chirality "
        "candidate (a) is **structurally REJECTED**. Candidate-(a) spectral triple "
        "`(A_K, H_K, D_K, γ_9' = γ_5 ⊕ γ_F, J)` does NOT realize the substrate's NCG axiomatics.\n"
        "\n"
        "**Substrate-physics FAIL rationale** (verbatim from `sessions/archive/session-91/session-91-w7-workingpaper.md` §W7-2a lines 146, 153-167):\n"
        "\n"
        "1. **Axiom 5' (chirality anticommutation `{D_F, γ_9'} = 0`) FAIL at residual 1.697** — the substrate's "
        "canonical Dirac operator D_F does NOT anticommute with the direct-sum bi-chirality grading γ_9'. "
        "The measured operator-norm `||{D_F, γ_9'}|| = 1.697` is NOT machine epsilon; the direct-sum grading "
        "demands the STRONGER joint per-sector condition `{D, γ_5}|_{ψ_5} = 0 AND {D, γ_F}|_{ψ_F} = 0`, which "
        "the substrate's D_F fails. (6/7 axioms PASS at the canonical-substrate meaning; the lone FAIL is axiom 5'.)\n"
        "2. **KO-dim shifts 6 → 0 (NON-PHYSICAL CPT class)** — Connes 1996 §2 reconstruction "
        "`(ε, ε', ε'') = (+1, +1, +1)` maps to KO-dim = 0 mod 8. Per S66 `product_ko_dim` "
        "(\"KO=0: J commutes with γ → CPT preserves chirality → non-physical for SM\"), this is a "
        "STRUCTURALLY DECISIVE FAIL signature: even if axiom 5' could be repaired, the candidate-(a) triple "
        "would describe a CPT class incompatible with the Standard Model. The canonical §VII.AQ.OP-PROJ "
        "chirality has KO-dim = 6 (BDI class; `J γ_F = -γ_F J` → CPT FLIPS chirality → physical).\n"
        "3. **Element-3 bridge map: 1/3 PASS** — only the HKR-style image is marginally available; the "
        "Connes-Karoubi pairing FAILs because it depends on axiom 5' (chirality anticommutation), which fails.\n"
        "4. **Element-4 Level-2 sub-class: NON-BINDING** — HKR FAILs at the substrate's pre-existing axiom-4 "
        "obstruction (S33-34 `||[[D_K, H], H]|| = 4.000`, independent of chirality grading), so no binding "
        "bridge map to a laboratory-IN observable exists. The §VII.AT.OP-PROJ entry cannot achieve "
        "STAGE-1-CANDIDATE eligibility via candidate (a).\n"
        "\n"
        "**Status (post-S91 W7-2a)**: STAGE-0-CANDIDATE RETAINED (no promotion). The 5-anatomy scaffold above "
        "remains as the candidate-(a) record; the bi-chirality substrate is REJECTED on substrate-IS structural "
        "grounds. No STAGE-1-CANDIDATE promotion path via candidate (a).\n"
        "\n"
        "**Substrate framing**: The bi-chirality grading `γ_9' = γ_5 ⊕ γ_F` IS a structurally distinct substrate "
        "from the tensor-product chirality at §VII.AQ.OP-PROJ. The FAIL-diagnostic documents that THIS substrate "
        "REJECTS the alternative-chirality hypothesis at the axiom-5' level — the substrate's own D_F structurally "
        "refuses the direct-sum grading. Direction of explanation: substrate IS spectral triple → bi-chirality "
        "grading IS a new substrate → axiom-5' anticommutation IS that substrate's structural identity requirement "
        "→ FAIL at 1.697 + KO-dim → 0 IS the substrate's structural rejection of the alternative grading. "
        "Container-thinking FORBIDDEN: \"we registered the wrong chirality\" — INVERT: the bi-chirality grading IS "
        "a substrate, and that substrate fails its own NCG axiomatics.\n"
        "\n"
        "**Cross-links (FAIL-diagnostic)**:\n"
        "- S91 W7-2a working paper: `sessions/archive/session-91/session-91-w7-workingpaper.md` §W7-2a "
        "(axiom table line 146; KO-dim derivation lines 153-159; bridge-map evaluation lines 161-167; "
        "Wrap-Up table line 386).\n"
        f"- S91 W7-2a verdict line: `computations/session-91/s91_gate_verdicts.txt` (full `audit_sha256={W7_2A_AUDIT_SHA}`).\n"
        "- §VII.AQ.OP-PROJ (PARENT slot; tensor-product chirality `γ_9 = γ_5 ⊗ γ_F`, KO-dim = 6 BDI) — "
        "RETAINED as the substrate's SOLE valid spectral-triple chirality structure; candidate (a) does not displace it.\n"
        "- §VII.AW.OP-PROJ (sibling candidate (b) SU(3)-coloured chirality; also FAIL — see its FAIL-diagnostic block).\n"
        "\n"
        "**Landing provenance**: S92 W9-4 `S92-W9-CF-W7-4-VII-AT-VII-AW-OP-PROJ-FAIL-DIAGNOSTIC-LANDING` "
        "(METHODOLOGY-class per `wave-classification.md` §M1-M4; mack-cosmic-bridge sole-writer; single-shot "
        "AFTER-pattern per `registry-landing.md §\"Bridge-Landing Script Architecture\"`; content-resolved slot "
        "target per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction).\n"
    )


def build_aw_fail_diagnostic() -> str:
    """§VII.AW.OP-PROJ SU(3)-Coloured FAIL-diagnostic block. Verbatim-derived
    from S91 W7-2b (WP §W7-2b lines 243-267; verdict audit_sha256=be8006d6...)."""
    return (
        "\n"
        "### FAIL-DIAGNOSTIC (S92 W9-4 CF-W7-4 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-23)\n"
        "\n"
        "**S91 W7-2b substrate-physics verdict** (`computations/session-91/s91_gate_verdicts.txt`; "
        f"gate `S91-VII-AW-OP-PROJ-7-AXIOM-COLOURED`; FAIL; full `audit_sha256={W7_2B_AUDIT_SHA}` "
        f"content_sha256=`{W7_2B_CONTENT_SHA}`; scheme=SU(3)-coloured-chirality; "
        "convention=substrate-distance-1-FULL-CM2008-S11-COLOURED; L_max=12): the SU(3)-coloured "
        "candidate (b) is **structurally REJECTED at the (+1, -1, +1) colour-signs choice**. Candidate-(b) "
        "spectral triple `(A_K, H_K, D_K, γ_9'' = γ_F^c, J)` does NOT realize the CM-2008 §11 prediction at "
        "this colour-signs assignment.\n"
        "\n"
        "**Substrate-physics FAIL rationale** (verbatim from `sessions/archive/session-91/session-91-w7-workingpaper.md` §W7-2b lines 243-267):\n"
        "\n"
        "1. **Axiom 5'' (chirality anticommutation `{D_F, γ_9''} = 0`) FAIL at residual 3.274** — the substrate's "
        "canonical D_F does NOT anticommute with the colour-resolved chirality grading γ_F^c at colour-signs "
        "(+1, -1, +1). The measured `||{D_F, γ_9''}|| = 3.274` is NOT machine epsilon. (6/7 axioms PASS; the lone "
        "FAIL is axiom 5''.)\n"
        "2. **KO-dim stays 6; CM-2008 §11 shift to 2 mod 8 NOT realized** — Connes 1996 §2 reconstruction "
        "`(ε, ε', ε'') = (+1, +1, -1)` gives KO-dim = 6 (KO-shift from §VII.AQ.OP-PROJ = 0 mod 8). The "
        "colour-dressing with the L/R-flipped sign assignment yields `J γ_9'' = -γ_9'' J` (ε'' = -1), so KO-dim "
        "stays 6 rather than shifting to 2 mod 8 (the CI class the CM-2008 §11 prediction targets). A different "
        "colour-signs assignment might realize the `+1` sign relation, but the axiom 5'' anticommutation would "
        "still fail at the substrate's existing D_F.\n"
        "3. **Element-3 bridge map (colour-dressed): 1/3 PASS** — only the HKR-style colour-dressed image is "
        "marginally available; the colour-dressed Connes-Karoubi pairing FAILs because it depends on axiom 5'' "
        "(chirality anticommutation), which fails at residual 3.274.\n"
        "4. **Element-4 Level-2 sub-class: NON-BINDING** — same logic as §VII.AT.OP-PROJ: HKR FAILs at the "
        "substrate's axiom-4 obstruction, so no binding bridge map to a laboratory-IN observable. The "
        "§VII.AW.OP-PROJ entry cannot achieve STAGE-1-CANDIDATE eligibility via candidate (b) under SU(3)-coloured "
        "chirality with this colour-signs choice.\n"
        "\n"
        "**Status (post-S91 W7-2b)**: STAGE-0-CANDIDATE RETAINED (no promotion). The 5-anatomy scaffold above "
        "remains as the candidate-(b) record; the SU(3)-coloured substrate at (+1, -1, +1) is REJECTED on "
        "substrate-IS structural grounds. (The 6-tuple colour-signs sweep at S92 W9-2 "
        "`S92-W9-CF-W7-2-VII-AW-OP-PROJ-COLOUR-SIGNS-SWEEP` tests whether ANOTHER non-trivial tuple repairs the "
        "joint axiom-5''-PASS-AND-KO-dim-2 prediction; this FAIL-diagnostic records the (+1, -1, +1) baseline.)\n"
        "\n"
        "**Substrate framing**: The SU(3)-coloured chirality grading `γ_9'' = γ_F^c` IS a structurally distinct "
        "substrate from the tensor-product chirality at §VII.AQ.OP-PROJ; each colour-signs choice IS itself a "
        "structurally distinct substrate per the algebra-axis orthogonality K-counter (chirality-grading sub-axis). "
        "The FAIL-diagnostic documents that THIS substrate (colour-signs (+1, -1, +1)) REJECTS the CM-2008 §11 "
        "alternative-chirality hypothesis at the axiom-5'' level. Direction of explanation: substrate IS spectral "
        "triple → colour-resolved chirality grading IS a new substrate → axiom-5'' anticommutation IS that "
        "substrate's structural identity requirement → FAIL at 3.274 + KO-dim unshifted IS the substrate's "
        "structural rejection of the CM-2008 prediction at this colour-signs choice. Container-thinking FORBIDDEN: "
        "\"colour is a label we attach\" — INVERT: the colour-axis IS substrate-IS, and this colour-dressed "
        "substrate fails its own axiom-5''.\n"
        "\n"
        "**Cross-links (FAIL-diagnostic)**:\n"
        "- S91 W7-2b working paper: `sessions/archive/session-91/session-91-w7-workingpaper.md` §W7-2b "
        "(axiom table line 243; KO-dim derivation lines 250-253; bridge-map evaluation lines 262-267; "
        "Wrap-Up table line 387).\n"
        f"- S91 W7-2b verdict line: `computations/session-91/s91_gate_verdicts.txt` (full `audit_sha256={W7_2B_AUDIT_SHA}`).\n"
        "- §VII.AQ.OP-PROJ (PARENT slot; tensor-product chirality `γ_9 = γ_5 ⊗ γ_F`, KO-dim = 6 BDI) — "
        "RETAINED as the substrate's SOLE valid spectral-triple chirality structure; candidate (b) does not displace it.\n"
        "- §VII.AT.OP-PROJ (sibling candidate (a) bi-chirality direct-sum; also FAIL — see its FAIL-diagnostic block).\n"
        "\n"
        "**Landing provenance**: S92 W9-4 `S92-W9-CF-W7-4-VII-AT-VII-AW-OP-PROJ-FAIL-DIAGNOSTIC-LANDING` "
        "(METHODOLOGY-class per `wave-classification.md` §M1-M4; mack-cosmic-bridge sole-writer; single-shot "
        "AFTER-pattern per `registry-landing.md §\"Bridge-Landing Script Architecture\"`; content-resolved slot "
        "target per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction).\n"
    )


# ============================ splice (atomic) ============================
def find_block_bounds(registry_text: str, header_key: str) -> tuple[int, int]:
    """Locate [start, end) char offsets of the block headed by `header_key`,
    where end is the position of the block-terminating `\\n---\\n` separator
    (the FAIL-diagnostic is inserted just BEFORE that separator). Returns
    (insert_at, header_start). Raises ValueError if not found / ambiguous."""
    h = registry_text.find(header_key)
    if h < 0:
        raise ValueError(f"header not found: {header_key!r}")
    if registry_text.find(header_key, h + len(header_key)) >= 0:
        raise ValueError(f"header ambiguous (>1 occurrence): {header_key!r}")
    # The block terminates at the first '\n---\n' AFTER the header.
    sep = registry_text.find("\n---\n", h)
    if sep < 0:
        raise ValueError(f"block separator '---' not found after {header_key!r}")
    insert_at = sep + 1  # insert after the leading '\n', before '---\n'
    return insert_at, h


def write_atomic(path: Path, text: str) -> None:
    """Atomic write: temp-file in same dir + fsync + os.replace."""
    d = path.parent
    fd, tmp = tempfile.mkstemp(dir=str(d), prefix=".tmp_registry_", suffix=".md")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as fh:
            fh.write(text)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


# ============================ Verdict emission ============================
def append_verdict(gate_id: str, verdict: str, value: str,
                   scheme: str, convention: str, L_max,
                   input_pin_map: dict,
                   script_path: Path, canonical_path: Path) -> tuple[str, str]:
    """Emit the canonical dual-SHA verdict line + dual-SHA companion comment row
    per `gate-verdicts.md` §"S87+ canonical form". No 3-tuple row (plan §W9-4
    schema_v2_3tuple_required: false). audit_sha256 = closure over
    script_bytes || canonical_bytes || sorted(input_pin_map)JSON."""
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, input_pin_map)
    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
    print(f"\n=== verdict line emitted to {VERDICT_TXT} ===")
    print(canonical_line.rstrip())
    print(dual_sha_row.rstrip())
    return audit_sha, content_sha


# ============================ main ============================
def main() -> int:
    pins = log_input_pins(INPUT_FILES)

    # ---- Build the two FAIL-diagnostic block texts in memory (pure) ----
    at_block = build_at_fail_diagnostic()
    aw_block = build_aw_fail_diagnostic()
    at_block_csha = sha256_text(at_block)
    aw_block_csha = sha256_text(aw_block)
    at_lines = substantive_line_count(at_block)
    aw_lines = substantive_line_count(aw_block)

    print("\n=== build_promotion_text precomputed per-block content_sha256 ===")
    print(f"  §VII.AT.OP-PROJ block: content_sha256={at_block_csha} "
          f"substantive_lines={at_lines}")
    print(f"  §VII.AW.OP-PROJ block: content_sha256={aw_block_csha} "
          f"substantive_lines={aw_lines}")

    # ---- Pre-flight predicate (c) + (d) on the in-memory blocks ----
    at_cites_full = (W7_2A_AUDIT_SHA in at_block)  # (local) predicate (c) §VII.AT
    aw_cites_full = (W7_2B_AUDIT_SHA in aw_block)  # (local) predicate (c) §VII.AW
    at_substantive = at_lines >= SUBSTANTIVE_LINE_FLOOR  # (local) predicate (d)
    aw_substantive = aw_lines >= SUBSTANTIVE_LINE_FLOOR  # (local) predicate (d)

    # ---- S92 W0 overlap check (mechanical-closure-discipline.md) ----
    registry_text_pre = REGISTRY.read_text(encoding="utf-8")
    already_at = W7_2A_AUDIT_SHA in registry_text_pre  # (local)
    already_aw = W7_2B_AUDIT_SHA in registry_text_pre  # (local)
    already_landed = already_at and already_aw  # (local)

    save_dict = {
        "at_block_content_sha256": at_block_csha,
        "aw_block_content_sha256": aw_block_csha,
        "at_substantive_lines": at_lines,
        "aw_substantive_lines": aw_lines,
        "at_cites_full_sha": at_cites_full,
        "aw_cites_full_sha": aw_cites_full,
        "w7_2a_audit_sha": W7_2A_AUDIT_SHA,
        "w7_2b_audit_sha": W7_2B_AUDIT_SHA,
        "substantive_line_floor": SUBSTANTIVE_LINE_FLOOR,
    }

    if already_landed:
        # Honest mechanical close: do NOT double-land.
        verdict = "INFO"
        value = "upstream_S92_W0_landing_already_discharged"
        print("\n=== S92 W0 overlap check: BOTH FAIL-diagnostic blocks already "
              "present on disk; honest mechanical-close (no double-land) ===")
        save_dict["landing_performed"] = False
        save_dict["overlap_already_discharged"] = True
        save_dict["verify_at_pass"] = already_at
        save_dict["verify_aw_pass"] = already_aw
    else:
        # ---- Single-shot AFTER-pattern landing ----
        # (1) build done above. (2) write_atomic via single read-modify-write.
        at_insert, at_hstart = find_block_bounds(registry_text_pre, AT_HEADER_KEY)
        aw_insert, aw_hstart = find_block_bounds(registry_text_pre, AW_HEADER_KEY)
        print(f"\n=== content-resolved slot anchors (NOT plan line numbers) ===")
        print(f"  §VII.AT.OP-PROJ header at char {at_hstart}; insert at {at_insert}")
        print(f"  §VII.AW.OP-PROJ header at char {aw_hstart}; insert at {aw_insert}")

        # Splice in descending offset order so earlier insertions do not shift
        # the later anchor offsets.
        edits = sorted(
            [(at_insert, at_block, "AT"), (aw_insert, aw_block, "AW")],
            key=lambda e: e[0], reverse=True,
        )
        new_text = registry_text_pre
        for offset, block, _tag in edits:
            new_text = new_text[:offset] + block + new_text[offset:]
        write_atomic(REGISTRY, new_text)
        print("=== atomic registry write complete ===")

        # (3) re_read + verify_section_matches (per slot)
        registry_text_post = REGISTRY.read_text(encoding="utf-8")
        verify_at = (at_block in registry_text_post) and (W7_2A_AUDIT_SHA in registry_text_post)
        verify_aw = (aw_block in registry_text_post) and (W7_2B_AUDIT_SHA in registry_text_post)

        # (4) determine 5-of-5 predicate conjunction per slot, joint PASS-AND
        #     (a) block present  (b) block present  (c) full-SHA cite
        #     (d) >=15 substantive lines  (e) content_sha256 match precomputed
        at_present = at_block in registry_text_post  # (local) predicate (a)
        aw_present = aw_block in registry_text_post  # (local) predicate (b)
        # (e) content_sha256 of the EXACT spliced block matches the precomputed hash:
        at_csha_match = sha256_text(at_block) == at_block_csha  # (local) tautology by construction; recorded for audit
        aw_csha_match = sha256_text(aw_block) == aw_block_csha  # (local)

        at_pass = at_present and at_cites_full and at_substantive and at_csha_match and verify_at
        aw_pass = aw_present and aw_cites_full and aw_substantive and aw_csha_match and verify_aw
        joint_pass = at_pass and aw_pass

        verdict = "PASS" if joint_pass else "FAIL"
        value = (
            f"AT_pass={at_pass};AW_pass={aw_pass};"
            f"AT_lines={at_lines};AW_lines={aw_lines};"
            f"AT_csha={at_block_csha[:16]};AW_csha={aw_block_csha[:16]};"
            f"joint_pass_and={joint_pass}"
        )
        save_dict["landing_performed"] = True
        save_dict["overlap_already_discharged"] = False
        save_dict["verify_at_pass"] = bool(verify_at)
        save_dict["verify_aw_pass"] = bool(verify_aw)
        save_dict["at_present"] = bool(at_present)
        save_dict["aw_present"] = bool(aw_present)
        save_dict["at_csha_match"] = bool(at_csha_match)
        save_dict["aw_csha_match"] = bool(aw_csha_match)
        save_dict["joint_pass_and"] = bool(joint_pass)
        print(f"\n=== AFTER-pattern verify ===")
        print(f"  §VII.AT.OP-PROJ: present={at_present} cites_full_sha={at_cites_full} "
              f"substantive={at_substantive} csha_match={at_csha_match} verify={verify_at} -> pass={at_pass}")
        print(f"  §VII.AW.OP-PROJ: present={aw_present} cites_full_sha={aw_cites_full} "
              f"substantive={aw_substantive} csha_match={aw_csha_match} verify={verify_aw} -> pass={aw_pass}")
        print(f"  joint PASS-AND = {joint_pass}")

    # ---- Save .npz (optional artifact per plan; written for audit trail) ----
    try:
        import numpy as np  # noqa: E402
        np.savez(OUT_NPZ, **{k: np.array(v) for k, v in save_dict.items()})
        print(f"\nnpz written: {OUT_NPZ}")
    except Exception as exc:  # pragma: no cover  (npz is optional per plan)
        print(f"\n[note] npz write skipped: {exc}")

    # ---- Emit ONE composite verdict line + dual-SHA companion row ----
    audit_sha, content_sha = append_verdict(
        gate_id=GATE_ID,
        verdict=verdict,
        value=value,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_TAG,
        input_pin_map=pins,
        script_path=THIS_SCRIPT,
        canonical_path=SHARED_DIR / "canonical_constants.py",
    )

    print("\n=== output 4-tuple ===")
    print(f"  (value='{value}',")
    print(f"   scheme={SCHEME},")
    print(f"   convention={CONVENTION},")
    print(f"   L_max={L_MAX_TAG})")
    print(f"  verdict:                  {verdict}")
    print(f"  audit_sha256:             {audit_sha}")
    print(f"  content_sha256:           {content_sha}")
    return 0  # exit 0 = script ran successfully (verdict is DATA per math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
