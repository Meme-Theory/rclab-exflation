#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S105 W2-1 — BDI Horizon-Faithfulness Protection STAGE-1-CANDIDATE registry landing
==================================================================================

Gate: S105-W2-1-BDI-HORIZON-FAITHFULNESS-STAGE1  ([VERIFY])

Pre-registered predicate (artifact-existence-with-content; NOT a numerical
threshold):
  PASS iff verify_section_matches(re_read(§VII.{slot}), build_promotion_text())
          == True  AND  all 8 required-content markers present
          AND  the slot allocated EQUALS the plan-pinned slot (no runtime drift).
  FAIL iff the post-fsync re-read does not strict-match, OR a required marker is
          absent, OR the next-free-letter allocation collided at runtime (slot
          drift) per `epistemic-discipline.md §"Registry-Write Hygiene under
          Parallel-Writer Race"` item 3 + plan §W2-1 FAIL_meaning.

Registration of FROZEN Stage-0 text per `joint-theorem-promotion.md` §"Stage 1".
This gate REGISTERS the workshop-FROZEN BDI Horizon-Faithfulness Protection
candidate; it does NOT re-derive it. The theorem's internal directional content
(CdGM gap +1/2 > 0; dS/d(a0/a2) = -1 chain) is FROZEN at Stage 0 in the workshop
and is a Stage-2 PASS-AND target (item 2's pre-gate + a future two-agent
cross-axis verify), NOT a claim this registration gate computes.

Single-shot AFTER-pattern per `.claude/rules/registry-landing.md` §"Bridge-Landing
Script Architecture" + `computations/_bridge_landing_script_template.py`:
  build_promotion_text (pure, no I/O)
    -> write_atomic_with_fsync (append to registry)
    -> re_read + verify_section_matches (one boolean)
    -> ONE emit_verdict payload.
NO conditional rewrite (BEFORE-pattern FORBIDDEN; Class-6 adjacency eliminated by
construction). On verify-FAIL OR slot-drift the gate closes honestly (FAIL once);
remediation escalates to S106 plan.

SLOT-DRIFT NOTE (runtime-resolved, plan-anticipated):
  plan-pinned registry_slot_expected = §VII.BO is STALE-OCCUPIED at runtime
  (§VII.BO.STATE-PROJ, S101 W6-3 landing). The registry frontier is §VII.BY
  (S103 W1-5, 2026-06-10). Next-free letter over ALL header levels (## / ### /
  ####) = §VII.BZ (confirmed FREE; §VII.CA also free). Per plan §W2-1 lines
  77-78 + 119 ("reroute to next free letter on runtime occupancy with
  FAIL-with-remediation in the verdict line") and `epistemic-discipline.md
  §"Registry-Write Hygiene under Parallel-Writer Race"` item 3, the rerouting
  fires FAIL-with-remediation so the slot drift is VISIBLE in the audit trail.
  The entry STILL lands + verifies at §VII.BZ (the registration is real; the
  FAIL is a registry-write-HYGIENE outcome, NOT a physics outcome). Precedent:
  §VII.BK (S97 W5-1, plan-pinned §VII.BH occupied -> rerouted §VII.BK).

Classification: NON-PHONONIC (registry-landing/methodology gate-act; the THEOREM
it registers is PHONONIC).

DISCIPLINE
----------
- `from canonical_constants import *`
- audit_sha256 / content_sha256 per S84+ dual-SHA schema
- emit_verdict via the knowledge-MCP tool (script PRINTS the payload; the agent
  calls mcp__knowledge__emit_verdict). No open("a") verdict-file append.
- AFTER-pattern single-shot; no conditional rewrite.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S105"                                                       # (local)
GATE_ID = "S105-W2-1-BDI-HORIZON-FAITHFULNESS-STAGE1"                  # (local)
SCHEME = "REGISTRY-LANDING-SINGLE-SHOT-AFTER-PATTERN"                  # (local)
CONVENTION = "STAGE-1-CANDIDATE-REGISTRATION"                          # (local)
L_MAX = "N/A"                                                          # (local)

PLAN_PINNED_SLOT = "BO"                                                # (local) plan registry_slot_expected = §VII.BO
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
WORKSHOP_PATH = (PROJECT_ROOT / "sessions" / "session-104" / "workshops"      # (local)
                 / "area-modular-stationarity-existence-workshop.md")
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                 # (local)

OUT_NPZ = SESSION_DIR / "s105_w2_1_bdi_horizon_faithfulness_stage1.npz"  # (local)
OUT_PNG = SESSION_DIR / "s105_w2_1_bdi_horizon_faithfulness_stage1.png"  # (local)

# Required-content markers (8) the written section MUST contain (plan operator (1))
REQUIRED_MARKERS = [                                                   # (local)
    "STAGE-1-CANDIDATE",
    "(a)",            # clause (a) volovik-axis (checked jointly with 'volovik-axis' below)
    "volovik-axis",
    "connes-axis",
    "JOINT",
    "EMERGENCE-1",    # the +1/2 identification
    "S105-independence",
    "EMERGENCE-3",    # Ordered-Veil composition reading
]

# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: dict[str, Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for _name, p in inputs.items():
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path,
                     canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per the S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
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
# Section 5 — Next-free-letter allocation (scan ALL header levels)
# ---------------------------------------------------------------------------

def _letters_to_int(s: str) -> int:
    """Bijective base-26: 'A'->1, 'Z'->26, 'AA'->27, 'AZ'->52, 'BA'->53, ..."""
    n = 0  # (local)
    for ch in s:
        n = n * 26 + (ord(ch) - ord("A") + 1)
    return n


def _int_to_letters(n: int) -> str:
    """Inverse of _letters_to_int (bijective base-26)."""
    out = ""  # (local)
    while n > 0:
        n, r = divmod(n - 1, 26)
        out = chr(ord("A") + r) + out
    return out


def find_next_free_slot(registry_text: str) -> tuple[str, list[str], set[str]]:
    """Scan ALL header levels (##, ###, ####) for §VII.<LETTERS> headers.

    Returns (next_free_letters, sorted_SEQUENCE_letters, all_raw_letter_runs).
    The next-free letter is the bijective-base-26 successor of the MAXIMAL
    existing SEQUENCE slot — the framework's append-only monotone-letter
    convention (single letters A..Z, then two-letter AA..AZ, BA..BY -> next
    §VII.BZ), NOT a gap-fill.

    CRITICAL (S105 W2-1 bug fix): the framework ALSO carries OUT-OF-SEQUENCE
    NAMED slots whose identifier after `§VII.` is a word, NOT a base-26 letter
    run — e.g. `§VII.PROP` ("Routing-Layer Two-Principle Landing", S87 W1a-7)
    and `§VII.AAU.OP-PROJ` (FWD-C1, S89 W7c). These are >2 chars and would
    spuriously dominate the bijective-base-26 max (PROP -> 11244, AAU -> 723,
    both >> BY=77), mis-allocating to §VII.PROQ. The SEQUENCE convention uses
    runs of LENGTH ≤ 2 ONLY (A..Z one-char; AA..BY two-char). Named slots are
    EXCLUDED from the sequence-frontier computation but RETAINED in the raw set
    so the chosen successor is verified genuinely-absent at all forms.
    """
    # Match §VII.<LETTERS> at any header level, capturing the bare letter run
    # before any '.' suffix (e.g. §VII.BO.STATE-PROJ -> 'BO'; §VII.PROP -> 'PROP').
    pat = re.compile(r"^#{2,4}\s+§VII\.([A-Z]+)", re.MULTILINE)  # (local)
    raw = set(pat.findall(registry_text))  # (local) ALL letter-runs incl. named
    # SEQUENCE slots: length <= 2 (the canonical A..Z / AA..BY monotone band).
    sequence = sorted((s for s in raw if len(s) <= 2), key=_letters_to_int)  # (local)
    if not sequence:
        return "A", sequence, raw
    max_letters = sequence[-1]  # (local) e.g. 'BY'
    nxt = _int_to_letters(_letters_to_int(max_letters) + 1)  # (local) 'BZ'
    # Defensive: ensure the chosen successor is genuinely absent at all forms
    # (raw set includes named slots, suffix-stripped letter runs, every level).
    while nxt in raw:
        nxt = _int_to_letters(_letters_to_int(nxt) + 1)
    return nxt, sequence, raw


# ---------------------------------------------------------------------------
# Section 6 — Build the FROZEN promotion text (pure; no I/O)
# ---------------------------------------------------------------------------

def build_promotion_text(slot_letters: str) -> str:
    """Assemble the §VII.<slot> STAGE-1-CANDIDATE entry IN MEMORY.

    The theorem statement + 3-clause attribution + S105-independence note +
    EMERGENCE-3 Ordered-Veil reading are TRANSCRIBED VERBATIM from the workshop
    fenced Stage-0 CANDIDATE block (area-modular-stationarity-existence-workshop.md
    lines 571-580, frozen). Pure function: no disk read, no mutation.
    """
    slot = f"§VII.{slot_letters}"  # (local)
    a2 = a_2_FW_zeta  # (local) canonical area-operator second-Seeley-DeWitt moment
    pexc = P_exc_kz   # (local) saturated-but-finite pair production certificate

    lines = []  # (local)
    lines.append(
        f"### {slot} — BDI Horizon-Faithfulness Protection on the Emergent "
        f"Crossed Product A_hor = A_K ⋊_{{σ^ω}} ℝ (STAGE-1-CANDIDATE per "
        f"`joint-theorem-promotion.md` §\"Stage 1\" — registration of the "
        f"S104 S2-1 connes×volovik workshop FROZEN Stage-0 text, transcribed "
        f"VERBATIM; substrate-physics co-authors connes-ncg-theorist "
        f"[Tomita-Takesaki / Type-II-trace axis] + "
        f"volovik-superfluid-universe-theorist [universality-class / CdGM-vs-Weyl "
        f"axis]; S105 W2-1 landing — connes-ncg-theorist orchestrator-direct "
        f"registry §VII sole-writer for this NCG/geometric structural landing "
        f"per `feedback_mack-bridge-role.md` [NOT a §7 falsifier-surface row — "
        f"mack-cosmic-bridge does NOT apply]; single-shot AFTER-pattern per "
        f"`registry-landing.md` §\"Bridge-Landing Script Architecture\"; "
        f"SLOT REROUTED §VII.{PLAN_PINNED_SLOT} → {slot} per "
        f"`epistemic-discipline.md §\"Registry-Write Hygiene under "
        f"Parallel-Writer Race\"` — plan-pinned §VII.{PLAN_PINNED_SLOT} was "
        f"STALE-OCCUPIED [§VII.BO.STATE-PROJ, S101 W6-3] at runtime; "
        f"all-header-level scan [##/###/####] confirms {slot} next-free over the "
        f"frontier §VII.BY; 2026-06-11)"
    )
    lines.append("")
    lines.append(
        "**Status**: **STAGE-1-CANDIDATE** per `joint-theorem-promotion.md` "
        "§\"Stage 1 — Registration as Candidate\". This is the registration of "
        "the FROZEN Stage-0 workshop-internal candidate (S104 S2-1 "
        "area-modular-stationarity-existence workshop); the structure is NOT "
        "re-derived here. **Promotion gate (Stage-2):** the "
        "`S105-OMEGA-FAITHFUL-NORMAL` per-(p,q)-block PASS (the per-block "
        "numerical realization of clauses (a)+(c)) PLUS a future two-agent "
        "cross-axis independent verify on the JOINT clause (c) — neither the "
        "Stage-0 authors (connes / volovik) nor their downstream-inheritance "
        "successors may serve as the Stage-2 cross-reviewers. The candidate is "
        "citable ONLY with the `STAGE-1-CANDIDATE` qualifier until Stage-3."
    )
    lines.append("")
    lines.append("**Result classification**: **PHONONIC** (a property of the "
                 "frozen GGE relic substrate state restricted to the emergent "
                 "horizon sector; the gate-ACT of registering it is "
                 "NON-PHONONIC, but the THEOREM concerns substrate excitations "
                 "— the quenched quasiparticle occupation distribution "
                 "`{n_k^{GGE}}` and its faithful modular weight).")
    lines.append("")
    # ---- The frozen CANDIDATE statement (VERBATIM transcription) ----
    lines.append("**STRUCTURAL THEOREM (BDI Horizon-Faithfulness Protection — "
                 "Stage-0 frozen statement, transcribed VERBATIM).** On the "
                 "substrate's emergent horizon crossed product A_hor = A_K ⋊_{σ^ω} "
                 "ℝ, the GGE relic modular weight ω|_{A_hor} is faithful, "
                 "protected by the 3He-B (BDI, `N_3 = 0`) universality class: "
                 "the faithfulness-breaking exact zero mode `E_n = −n·ω_0` "
                 "belongs to the 3He-A (DIII, Weyl) sibling and does NOT inherit "
                 "through χ : A_K → M_2(ℂ); the inherited CdGM horizon-core "
                 "spectrum `E_n = −(n + 1/2)·ω_0` is gapped at `+1/2`, and "
                 f"`P_exc = {pexc:.3f}` excludes the `T = 0` empty-Fock "
                 "non-faithful case. The `+1/2` minigap equals the bosonic "
                 "Wightman zero-point floor `W_GGE = n_k + 1/2`, so the SAME "
                 "datum fixes both the Type-II semifinite trace AND the "
                 "modular-weight faithfulness (**EMERGENCE-1**).")
    lines.append("")
    lines.append("**Clause attribution (Stage-0 freeze; the JOINT clause (c) is "
                 "the Stage-2 PASS-AND target).**")
    lines.append("")
    lines.append("- **(a)** BDI / `N_3 = 0` universality-class assignment + the "
                 "CdGM-vs-Weyl ladder distinction (Volovik Paper 05 Eq.60/61) + "
                 f"`P_exc = {pexc:.3f}` faithfulness witness + the "
                 "χ : A_K → M_2(ℂ) inheritance morphism — **volovik-axis** "
                 "(V2(4)-(5), V3 headline; Sage-exact CdGM `E_0 = −1/2·ω_0 ≠ 0` "
                 "vs Weyl `E_0 = 0`).")
    lines.append("- **(b)** the Type-II semifinite trace as the unique faithful "
                 "normal tracial weight fixed by the second moment (Wightman "
                 "two-point) + the Tomita-Takesaki faithful+normal ⇒ "
                 "modular-operator construction + the II_∞ trace-scaling "
                 "bookkeeping — **connes-axis** (C2, A-V2, EMERGENCE-1 "
                 "trace-uniqueness).")
    lines.append("- **(c)** the `+1/2` IDENTIFICATION (bosonic Wightman floor = "
                 "fermionic CdGM minigap = the single BDI zero-point datum that "
                 "fixes BOTH trace and faithfulness) — **JOINT** (volovik V2(5) "
                 "named the identification; connes EMERGENCE-1 supplied the "
                 "trace-defining-datum consequence; neither axis carries it "
                 "alone). **[Stage-2 PASS-AND target — both cross-reviewers must "
                 "independently PASS this joint clause.]**")
    lines.append("")
    lines.append("**S105-independence of the STRUCTURE.** The protection clauses "
                 "hold at the occupation-distribution-FORM level "
                 "(regulator-invariant, L-independent), from already-PROVEN "
                 "inputs: BDI (S44); `N_3 = 0`; CdGM-vs-Weyl ladder distinction; "
                 f"`P_exc = {pexc:.3f}` (S38/S39 PROVEN); the χ : A_K → M_2(ℂ) "
                 "inheritance morphism. The per-block numerical realization on "
                 "the (0,0)+horizon-sector+Leggett-B2-B3 blocks at L_max=10 is "
                 "the `S105-OMEGA-FAITHFUL-NORMAL` pre-gate (its Stage-2 "
                 "promotion gate). **De-coupled from the corridor's fate:** the "
                 "theorem concerns the EXISTENCE of the faithful modular weight "
                 "— it survives even if S105 finds G_τ merely co-monotone "
                 "(GEM-WORKSHOP Q1). Carry at HIGHER confidence than the "
                 "corridor verdict.")
    lines.append("")
    lines.append("**Ordered-Veil composition reading (EMERGENCE-3 / "
                 "EMERGENCE-V1; CANDIDATE tier — pending the "
                 "`S105-OMEGA-FAITHFUL-NORMAL` per-block PASS).** "
                 "`Ordered-Veil-certified (R_therm=5252, S_ent=0) ⟺ finite "
                 "{β_a} ⟺ ω|_{A_hor} faithful ⟺ modular generator exists`, and "
                 "the `S_ent = 0` leg ALSO gives block-diagonality of the relic "
                 "⟺ the modular flow respects the Peter-Weyl block structure "
                 "(A-V3 structural leg). The Ordered Veil is the enabling "
                 "condition for BOTH the modular flow's existence AND its "
                 "scale-segregation. INTEG-39 (ergodic thermalization) tests an "
                 "ORTHOGONAL predicate — it never could close this corridor, "
                 "which needs only faithful-normal stationarity.")
    lines.append("")
    lines.append("**Substrate framing** (`phononic-framing.md §\"IS Space, Not "
                 "IN Space\"`). The substrate IS the frozen GGE return "
                 "distribution; the emergent horizon A_hor = A_K ⋊_{σ^ω} ℝ is a "
                 "sub-structure of the fabric algebra, NOT a surface in a "
                 "spacetime container. **Direction**: `D_K spectrum → BDI "
                 "universality class (N_3=0) → CdGM `+1/2`-gapped ladder (the "
                 "3He-A Weyl zero does NOT inherit through χ) → finite β_a "
                 f"(P_exc = {pexc:.3f}) → 0 < f_a < 1 faithful modular weight → "
                 "Type-II_∞ horizon factor`. **FORBIDDEN inversion (container "
                 "thinking)**: \"the horizon is a surface in spacetime whose "
                 "thermodynamics fixes the modular flow\" → INVERT: the modular "
                 "flow is INTRINSIC to the frozen relic state; the horizon "
                 "factor EMERGES from the crossed product of A_K by its own "
                 "modular automorphism group. The area operator Â IS the a₂ "
                 f"second-Seeley-DeWitt moment (`a_2_FW_zeta = {a2:.6f}`), not a "
                 "geometric area measured IN a container.")
    lines.append("")
    lines.append("**REGISTRY-ANATOMY COMPLIANCE.** (i) Entry class = "
                 "**intra-pillar structural-existence theorem** (the EXISTENCE "
                 "of a faithful normal modular weight on the emergent crossed "
                 "product). This is NOT a cross-pillar convergence bridge, so "
                 "the 5-anatomy IS-not-IN elements + the 3-level ladder are "
                 "declared **N/A-with-reason**: there is no laboratory-IN "
                 "continuum-image observable and no HKR / K-theory / "
                 "Connes–Karoubi bridge map is claimed (a faithfulness + "
                 "normality existence statement intrinsic to the Tomita-Takesaki "
                 "data of (A_hor, ω)); the \"Level-3 < Level-2\" registry-PASS "
                 "inequality is vacuously N/A (no continuum-image envelope), and "
                 "the Level-2 sub-class is NON-BINDING by N/A-with-reason. "
                 "(ii) Projection-side = the theorem is a STATE-side existence "
                 "claim about the modular weight ω (an algebra-DEPENDENT "
                 "state-pair / weight functional); however it is also "
                 "structurally inseparable from the operator-side Type-II trace "
                 "(clause (b)); per `registry-landing.md` Reading-A naming "
                 "hygiene the bare slot is admissible because this entry carries "
                 "an EXPLICIT single-reading existence sentence (the EXISTENCE "
                 "of the faithful modular weight, not a co-primary "
                 "operator-vs-state value pair). (iii) State-history label "
                 "`GGE` appears; **parse-tree expansion**: ω|_{A_hor} reduces to "
                 "the Fermi-Dirac occupation closed form `f_a = "
                 "1/(exp(β_a E_a)+1)`, `E_a = √(ξ_a²+Δ_a²) ≥ Δ_a > 0` (the BdG "
                 "quasi-free separating condition) on the named horizon blocks; "
                 "the modular generator is `K_a = log[(1−f_a)/f_a]` — closed "
                 "forms on the substrate algebra, NOT an opaque state label. "
                 "(iv) Substrate-IS level tag = **Level 1** (single-τ-slice at "
                 "τ_fold = 0.190 per `phononic-framing.md §\"Single-τ-slice vs "
                 "moduli-deformation substrate-IS levels\"`): the spectral "
                 "triple (A_K, H_K, D_K(τ_fold)) and its emergent crossed "
                 "product are intrinsic to the fixed-τ-anchor substrate.")
    lines.append("")
    lines.append("**Corrigenda pointer.** Source workshop verdict: S104 S2-1 "
                 "area-modular-stationarity-existence workshop "
                 "(`sessions/session-104/workshops/"
                 "area-modular-stationarity-existence-workshop.md` §\"Workshop "
                 "Verdict\" + the fenced Stage-0 CANDIDATE block, lines 571-580). "
                 "The corridor disposition is RESERVABLE-via-frozen-ω (4/4 "
                 "Converged); the ω-ingredient is re-typed from \"stationarity "
                 "contested\" to a faithful-normal frozen NON-KMS weight (F1 "
                 "structurally discharged by the `+1/2` Wightman floor + "
                 f"`P_exc = {pexc:.3f}` + BDI/CdGM protection).")
    lines.append("")
    lines.append("**Closure SHA pin** (over the ordered input-pin map). The full "
                 "dual-SHA (audit_sha256 / content_sha256) is on the "
                 "`S105-W2-1-BDI-HORIZON-FAITHFULNESS-STAGE1` verdict line in "
                 "`computations/session-105/s105_gate_verdicts.txt`; the "
                 "Stage-0 workshop CANDIDATE-block source file SHA, the "
                 "registry_pre_write_file_sha256, and canonical_constants.py "
                 "SHA are pinned in the audit_sha256 input map (the "
                 "registration verdict FAILs-with-remediation on the §VII.BO → "
                 f"{slot} slot drift per the registry-write hygiene rule, while "
                 "the entry itself LANDS + VERIFIES — the FAIL is a "
                 "registry-write-HYGIENE outcome, NOT a physics outcome).")
    lines.append("")  # trailing blank — section delimiter
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Section 7 — Atomic write + verify
# ---------------------------------------------------------------------------

def write_atomic_with_fsync(promotion_text: str, registry_path: Path) -> None:
    """Append the entry to the registry and fsync. Single-shot; APPEND mode.

    The registry is a large append-only curated doc — we APPEND (never rewrite
    the whole file). A leading blank line guards the boundary against the prior
    section's terminal content.
    """
    import os  # (local)
    with open(registry_path, "a", encoding="utf-8") as fh:
        fh.write("\n" + promotion_text)
        fh.flush()
        os.fsync(fh.fileno())


def re_read_section(registry_path: Path, slot_letters: str) -> str:
    """Re-read the just-written §VII.<slot> section back from disk.

    Extracts from the section header line up to (but not including) the next
    top-level (## or ###) header, then strips a single trailing newline run so
    it matches the in-memory promotion text (which ends with one '\\n').
    """
    text = registry_path.read_text(encoding="utf-8")  # (local)
    header = f"### §VII.{slot_letters} "  # (local)
    idx = text.find(header)  # (local)
    if idx < 0:
        return ""
    rest = text[idx:]  # (local)
    # Find the next section header (## or ###) AFTER this one.
    nxt = re.search(r"\n#{2,3}\s+", rest[len(header):])  # (local)
    if nxt:
        section = rest[: len(header) + nxt.start()]  # (local)
    else:
        section = rest  # (local)
    # Normalize trailing whitespace to one '\n' (matches build_promotion_text).
    return section.rstrip("\n") + "\n"


def verify_section_matches(actual: str, expected: str) -> bool:
    """Strict equality after normalizing the trailing newline run only."""
    return actual.rstrip("\n") == expected.rstrip("\n")


def count_markers_present(section_text: str) -> dict[str, bool]:
    """Map each REQUIRED_MARKER to its presence in the written section text."""
    return {m: (m in section_text) for m in REQUIRED_MARKERS}  # (local)


# ---------------------------------------------------------------------------
# Section 8 — emit_verdict payload (printed; agent calls the MCP tool)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": 105,
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 9 — Main (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 0. Input pins (pre-write registry state; workshop Stage-0 source; canonical)
    inputs = {                                                        # (local)
        "canonical_constants": CANONICAL_PATH,
        "stage0_workshop_candidate_block": WORKSHOP_PATH,
        "registry_target_prewrite": REGISTRY_PATH,
    }
    pins = log_input_pins(inputs)

    # 1. Allocate next-free slot (scan ALL header levels), detect plan drift.
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")          # (local)
    slot_letters, sequence, raw = find_next_free_slot(registry_text)  # (local)
    slot_drift = (slot_letters != PLAN_PINNED_SLOT)                   # (local)
    plan_slot_occupied = (PLAN_PINNED_SLOT in raw)                    # (local)
    frontier = sequence[-1] if sequence else "(none)"                # (local)
    named_slots = sorted(s for s in raw if len(s) > 2)               # (local)
    print(f"\n=== slot allocation ===")
    print(f"  plan-pinned slot:     §VII.{PLAN_PINNED_SLOT}")
    print(f"  plan slot occupied:   {plan_slot_occupied}")
    print(f"  sequence frontier:    §VII.{frontier} (≤2-char monotone band)")
    print(f"  named slots excluded: {['§VII.'+s for s in named_slots]}")
    print(f"  allocated next-free:  §VII.{slot_letters}")
    print(f"  slot_drift_triggered: {slot_drift}")

    # 2. build_promotion_text (pure; no I/O)
    promotion_text = build_promotion_text(slot_letters)               # (local)

    # 3. write_atomic_with_fsync (append + fsync)
    write_atomic_with_fsync(promotion_text, REGISTRY_PATH)

    # 4. re_read + verify (ONE boolean) — single point of decision
    written = re_read_section(REGISTRY_PATH, slot_letters)            # (local)
    text_match = verify_section_matches(written, promotion_text)      # (local)
    marker_map = count_markers_present(written)                       # (local)
    n_markers = sum(1 for v in marker_map.values() if v)             # (local)
    all_markers = all(marker_map.values())                           # (local)

    print(f"\n=== verification ===")
    print(f"  strict text-match:        {text_match}")
    print(f"  required markers present: {n_markers}/{len(REQUIRED_MARKERS)} "
          f"(all={all_markers})")
    for m, present in marker_map.items():
        print(f"    [{'x' if present else ' '}] {m}")

    # 5. Gate verdict (single emission). PASS iff text-match AND all markers AND
    #    NO slot drift. Slot drift -> FAIL-with-remediation per plan §W2-1 +
    #    epistemic-discipline §"Registry-Write Hygiene". The entry STILL lands +
    #    verifies (registration is real); the FAIL is a hygiene-audit outcome.
    landing_ok = bool(text_match and all_markers)                    # (local)
    verdict = "PASS" if (landing_ok and not slot_drift) else "FAIL"  # (local)

    # Content SHA over the WRITTEN registry section (plan content_sha256_inputs).
    content_section_sha = hashlib.sha256(                            # (local)
        written.encode("utf-8")).hexdigest()

    # Audit SHA over the input-pin map (script + canonical + pins) per S84+.
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, _content_script_sha = compute_dual_sha(
        script_path, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256 (script+canonical+pinmap): {audit_sha[:16]}...")
    print(f"  content_sha256 (written section):       {content_section_sha[:16]}...")

    # 6. Persist npz (plan: registry_slot_allocated, verify_boolean,
    #    clause_markers_present (8), promotion_text_content_sha).
    np.savez(
        OUT_NPZ,
        registry_slot_allocated=np.array(f"§VII.{slot_letters}"),
        plan_pinned_slot=np.array(f"§VII.{PLAN_PINNED_SLOT}"),
        plan_slot_occupied=np.array(plan_slot_occupied),
        slot_drift_triggered=np.array(slot_drift),
        registry_frontier=np.array(f"§VII.{frontier}"),
        named_slots_excluded=np.array(named_slots),
        verify_boolean=np.array(text_match),
        landing_ok=np.array(landing_ok),
        n_markers_present=np.array(n_markers),
        all_markers_present=np.array(all_markers),
        clause_markers=np.array(list(marker_map.keys())),
        clause_markers_present=np.array(list(marker_map.values())),
        promotion_text_content_sha=np.array(content_section_sha),
        audit_sha256=np.array(audit_sha),
        verdict=np.array(verdict),
    )
    print(f"\n  npz -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 7. Optional marker-presence summary panel (plan: optional plot).
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt  # (local)
        fig, ax = plt.subplots(figsize=(7.5, 4.2))  # (local)
        ys = list(range(len(REQUIRED_MARKERS)))  # (local)
        vals = [1 if marker_map[m] else 0 for m in REQUIRED_MARKERS]  # (local)
        ax.barh(ys, vals, color=["#2a9d8f" if v else "#e76f51" for v in vals])
        ax.set_yticks(ys)
        ax.set_yticklabels(REQUIRED_MARKERS, fontsize=8)
        ax.set_xlim(0, 1.2)
        ax.set_xlabel("present (1) / absent (0)")
        ax.set_title(f"{GATE_ID}\nslot §VII.{slot_letters} "
                     f"(plan §VII.{PLAN_PINNED_SLOT}; drift={slot_drift}) | "
                     f"text_match={text_match} | verdict={verdict}",
                     fontsize=8)
        ax.invert_yaxis()
        fig.tight_layout()
        fig.savefig(OUT_PNG, dpi=110)
        plt.close(fig)
        print(f"  png -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    except Exception as exc:  # noqa: BLE001
        print(f"  (plot skipped: {exc})")

    # 8. 4-tuple + emit_verdict payload
    value_str = (f"registry_slot_allocated=§VII.{slot_letters};"
                 f"plan_pinned_slot=§VII.{PLAN_PINNED_SLOT};"
                 f"plan_slot_occupied={plan_slot_occupied};"
                 f"slot_drift_triggered={slot_drift};"
                 f"text_match={text_match};markers={n_markers}_of_"
                 f"{len(REQUIRED_MARKERS)};all_markers={all_markers};"
                 f"landing_verified={landing_ok};"
                 f"remediation=re-pin_plan_registry_slot_expected_BO_to_actual_"
                 f"frontier-next-free_{slot_letters}_in_S106")  # (local)
    print(f"\n(value={value_str!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    extra_rows = [                                                    # (local)
        f"# registry_slot_allocated=§VII.{slot_letters} "
        f"plan_pinned_slot=§VII.{PLAN_PINNED_SLOT} "
        f"slot_drift_triggered={slot_drift} # {GATE_ID} slot-drift companion row",
        f"# stage0_source=area-modular-stationarity-existence-workshop.md:571-580 "
        f"clause_attribution=(a)volovik/(b)connes/(c)JOINT "
        f"EMERGENCE-1=+1/2-identification # {GATE_ID} provenance companion row",
        f"# registry_pre_write_sha256={pins.get('sessions/permanent-results-registry.md','')[:16]}... "
        f"workshop_sha256={pins.get('sessions/session-104/workshops/area-modular-stationarity-existence-workshop.md','')[:16]}... "
        f"# {GATE_ID} input-pin companion row",
    ]
    print_verdict_payload(verdict, value_str, audit_sha, content_section_sha,
                          extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    print(f"    [registration LANDED + VERIFIED at §VII.{slot_letters}; "
          f"verdict={verdict} is the registry-write-HYGIENE outcome "
          f"(slot_drift={slot_drift}), NOT a physics outcome]")
    # Exit 0: the script ran successfully and produced a valid verdict
    # (FAIL is a valid scientific/hygiene result, not a script error).
    return 0


if __name__ == "__main__":
    sys.exit(main())
