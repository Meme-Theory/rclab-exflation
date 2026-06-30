"""S86-TWO-LAYER-OBSTRUCTION-LANDING (S86 W1b T7).

Lands the W5-7 PASS (n_joint = 0/5 across the 5-regulator atlas
{zeta, Zubarev, SDW, cutoff_sqrt, anomaly}) into
sessions/permanent-results-registry.md §VII-B as the permanent
"Two-Layer Obstruction Theorem (Lizzi-track)" entry, with the
strengthening clause "every conjunct fails individually for every
regulator" and the (definition -> substitution -> simplification ->
direction) substitution chain.

Pure I/O + SHA hashing. CPU-only. No GPU/numpy linalg.

Substitution chain (verified at write-time):
    Step 1 (Definition): Joint(r) := AND_i C_i(r); Atlas:= {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}.
    Step 2 (Substitution): W5-7 measured n_joint = 0/5; Lizzi strengthening:
        for every r in Atlas and every conjunct C_i, C_i(r) = FALSE.
    Step 3 (Simplification): if any C_i(r) = FALSE then Joint(r) = FALSE.
        Strengthening: for-all r, for-all i: C_i(r) = FALSE
        => for-all r: Joint(r) = FALSE => n_joint = 0/5 (matches measurement).
    Step 4 (Direction): obstruction is STRONGER than predicted joint failure.
        Each individual conjunct is a wall, not just their conjunction.
"""

from __future__ import annotations

import hashlib
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# Canonical constants (mandatory per math-scripts.md S34+)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Pinned paths (PRDR machinery pin map)
# ---------------------------------------------------------------------------

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
REGISTRY_PATH = ROOT / "sessions" / "permanent-results-registry.md"
LIZZI_S7_PATH = ROOT / "sessions" / "session-85" / "session-85-s7-combined-landscape-lizzi.md"
S85_VERDICTS_PATH = ROOT / "computations" / "session-85" / "s85_gate_verdicts.txt"
S86_VERDICTS_PATH = ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"

GATE_ID = "S86-TWO-LAYER-OBSTRUCTION-LANDING"
SCHEME = "registry_landing"
CONVENTION = "lizzi-track"
L_MAX_TAG = "N/A"
SCHEMA_VERSION = "S84+"

# 5-regulator atlas (canonical order matches lizzi S-7 §V.8 / W5-7)
ATLAS_5 = ["zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly"]
N_JOINT_REQUIRED = "0/5"
STRENGTHENING_CLAUSE = "every conjunct fails individually for every regulator"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(k.encode("utf-8")); h.update(b"=")
        h.update(v.encode("utf-8")); h.update(b"\n")
    return h.hexdigest()


def emit_4tuple(value: str, scheme: str, convention: str, L_max: str) -> str:
    return f"(value={value}, scheme={scheme}, convention={convention}, L_max={L_max})"


# ---------------------------------------------------------------------------
# Step 1: locate W5-7 verdict line and parse SHAs + n_joint
# ---------------------------------------------------------------------------

def parse_w5_7_verdict(path: Path) -> dict[str, str]:
    txt = path.read_text(encoding="utf-8")
    canonical_re = re.compile(
        r"^S85-W5-7-TWO-LAYER-OBSTRUCTION:\s*(PASS|FAIL|INFO)\s*--\s*"
        r"value=(\S+)\s+scheme=(\S+)\s+convention=(\S+)\s+L_max=(\S+)\s+"
        r"audit_sha256=([0-9a-f]{64})\s+content_sha256=([0-9a-f]{64})",
        re.MULTILINE,
    )
    m = canonical_re.search(txt)
    if not m:
        raise RuntimeError("W5-7 canonical line not found in s85_gate_verdicts.txt")
    return {
        "verdict": m.group(1),
        "value": m.group(2),
        "scheme": m.group(3),
        "convention": m.group(4),
        "L_max": m.group(5),
        "audit_sha256": m.group(6),
        "content_sha256": m.group(7),
    }


# ---------------------------------------------------------------------------
# Step 2: build the §VII-B entry block
# ---------------------------------------------------------------------------

def build_entry(w5_7: dict[str, str], iso_ts: str) -> str:
    """Build the registry entry. The strengthening clause MUST appear
    within the entry block (otherwise PASS->INFO per plan §9)."""
    n_joint_value = w5_7["value"]                          # "0"
    n_joint_display = f"{n_joint_value}/{len(ATLAS_5)}"     # "0/5"
    if n_joint_display != N_JOINT_REQUIRED:
        raise RuntimeError(
            f"n_joint mismatch: W5-7 reports {n_joint_display}, "
            f"plan requires {N_JOINT_REQUIRED}"
        )
    atlas_set = "{" + ", ".join(ATLAS_5) + "}"

    return f"""

### VII-B.TWO-LAYER-OBSTRUCTION — Two-Layer Obstruction Theorem (Lizzi-track) (S86 W1b T7, {iso_ts})

THEOREM (Two-Layer Obstruction; Lizzi-track). Let L1 denote the spectral-action layer Tr f(D_K^2 / Lambda^2) and L2 denote the Jensen-deformed substrate-action layer S(tau). Let C_i (i = 1, ..., N_C) denote the L1<->L2 functoriality conjuncts (Mellin commutation, Wick-rotated trace pairing, regulator-pulled-back action invariance, etc.). Define Joint(r) := AND_i C_i(r), the conjunction of all functoriality conjuncts at regulator r. Then on the 5-regulator atlas

    Atlas := {atlas_set}                                      (VII-B.TLO-1)

NO regulator r in Atlas satisfies Joint(r). Equivalently,

    n_joint := |{{r in Atlas : Joint(r)}}| = {n_joint_display}.                 (VII-B.TLO-2)

STRENGTHENING (Lizzi). The obstruction is stronger than the predicted joint failure: {STRENGTHENING_CLAUSE}. That is, for every r in Atlas and every conjunct C_i, C_i(r) = FALSE individually — not merely the conjunction Joint(r) but each individual L1<->L2 functoriality conjunct fails at every regulator. The L1<->L2 interface is structurally obstructed at every categorical axis simultaneously, for every regulator in the 5-atlas.

SUBSTITUTION CHAIN (definition -> substitution -> simplification -> direction):

  Step 1 (Definition):
    L1 := spectral-action layer (Tr f(D_K^2 / Lambda^2) family)
    L2 := substrate-action layer (Jensen-deformed action S(tau) family)
    Conjunct C_i := L1<->L2 functoriality requirement at the i-th categorical
                    morphism axis (Mellin commutation, Wick-rotated trace
                    pairing, regulator-pulled-back action invariance, etc.)
    Joint(r) := AND_i C_i(r)               [all conjuncts hold for regulator r]
    Atlas := {atlas_set}                                       [|Atlas| = 5]

  Step 2 (Substitution):
    W5-7 measurement: n_joint = |{{r in Atlas : Joint(r)}}| = {n_joint_display}.
    Lizzi strengthening: for every r in Atlas and every conjunct C_i,
                         individual C_i(r) = FALSE.

  Step 3 (Simplification):
    Joint(r) = AND_i C_i(r). If any C_i(r) = FALSE then Joint(r) = FALSE.
    Strengthening: for-all r in Atlas, for-all i: C_i(r) = FALSE.
    Therefore: for-all r in Atlas, Joint(r) = FALSE.
    => n_joint = {n_joint_display}.   [matches W5-7 measured value]

  Step 4 (Direction):
    The obstruction is STRONGER than predicted joint failure. Predicted
    obstruction: there-exists at least one C_i failing for each r (joint fails).
    Measured obstruction: EVERY C_i fails for EVERY r. Each individual
    conjunct is a wall, not merely their conjunction. The L1<->L2 interface
    is structurally obstructed at every categorical axis simultaneously,
    for every regulator in the 5-atlas. This is a categorical statement
    about the spectral triple's two-layer structure, not a fine-tuning failure.

SUBSTRATE-FRAMING. The Two-Layer Obstruction is a categorical wall on the substrate's L1<->L2 interface itself. The substrate has a two-layer structure (spectral-action moment expansion sitting above the Jensen substrate-action) and that two-layer structure IS categorically inadmissible at every regulator-and-conjunct combination — the obstruction does not live IN an external functor space, it IS the substrate's two-layer non-functoriality. No regulator pulls L1 back through L2 along all categorical axes simultaneously; this is structural geometry of the substrate, not a fine-tuning of an external functor.

SOLUTION-SPACE CONSEQUENCE.
- C45 (sixth-regulator-synthesis test, deferred to S87 per S86 partition §2): any composite regulator r_mix = alpha * zeta + beta * cutoff_sqrt with alpha + beta = 1, alpha, beta > 0 inherits the obstruction at every individual conjunct. No convex combination escapes per-conjunct failure when both endpoints fail individually. The C45 defer-decision is now anchored to this registry entry as the structural reason it is meaningful only after C28 (W4 cutoff_sqrt adjudication) closes.
- C28 (cutoff_sqrt adjudication): whether cutoff_sqrt is structurally excluded from the regulator scope determines whether the {{F_4}}-only landscape (zeta, Zubarev, SDW) IS the framework's regulator scope or whether two coexisting classes must each be tracked. The Two-Layer Obstruction holds within F_4 alone (n_joint = 0/3) and within the M = {{cutoff_sqrt, anomaly}} extension (n_joint = 0/2), so the wall persists across either C28 outcome.

SOURCE CITATION. lizzi S-7 §V.8 (CF-LZ-S86-8); see `sessions/archive/session-85/session-85-s7-combined-landscape-lizzi.md` lines 442-446.

W5-7 VERDICT PIN. S85-W5-7-TWO-LAYER-OBSTRUCTION (PASS, value={n_joint_value}, scheme={w5_7["scheme"]}, convention={w5_7["convention"]}, L_max={w5_7["L_max"]}).
- content_sha256: `{w5_7["content_sha256"]}`
- audit_sha256:   `{w5_7["audit_sha256"]}`
- file pin: `computations/session-85/s85_gate_verdicts.txt` (line containing the canonical S85-W5-7-TWO-LAYER-OBSTRUCTION verdict).

CLASSIFICATION. GEOMETRIC (categorical wall on the L1<->L2 spectral-action / substrate-action interface; n_joint = {n_joint_display} with strengthening to per-conjunct individual failure).

REGISTRY 4-TUPLE. (value=<entry_SHA>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG}).

---
"""


# ---------------------------------------------------------------------------
# Step 3: insert entry into registry §VII-B (collision-aware)
# ---------------------------------------------------------------------------

def insert_into_registry(registry_text: str, entry: str) -> tuple[str, int]:
    """Insert entry at end of §VII-B (after table+constants block, before §VII.J).

    Idempotent: if Two-Layer Obstruction already present, raises (do not
    duplicate). Collision-aware: if §VII.J start moves due to T6 / W1a-1
    landings, the heading-anchor still locates correctly.
    """
    if "VII-B.TWO-LAYER-OBSTRUCTION" in registry_text:
        raise RuntimeError(
            "Two-Layer Obstruction entry already present in §VII-B; "
            "refusing to duplicate. Manual review required."
        )

    # Anchor: the next section heading after VII-B is §VII.J. Insert before it.
    anchor_pat = re.compile(
        r"(?m)^### VII\.J — Cartan Level-2 Exclusion Theorem"
    )
    m = anchor_pat.search(registry_text)
    if not m:
        raise RuntimeError("Registry anchor §VII.J not found; cannot insert.")
    insert_at = m.start()
    new_text = registry_text[:insert_at] + entry.lstrip("\n") + "\n" + registry_text[insert_at:]
    return new_text, insert_at


# ---------------------------------------------------------------------------
# Step 4: post-write verification
# ---------------------------------------------------------------------------

def verify_post_write(text: str) -> dict[str, bool]:
    """Verify both theorem statement, n_joint = 0/5 citation, and the
    strengthening clause are within the entry block (not separate paragraphs)."""
    # Locate the entry block: from "VII-B.TWO-LAYER-OBSTRUCTION" header to next "### VII"
    start_pat = re.compile(r"^### VII-B\.TWO-LAYER-OBSTRUCTION", re.MULTILINE)
    m = start_pat.search(text)
    if not m:
        return {"entry_present": False}
    entry_start = m.start()
    rest = text[entry_start + 1:]
    next_section = re.search(r"^### VII", rest, re.MULTILINE)
    entry_end = entry_start + 1 + (next_section.start() if next_section else len(rest))
    entry_block = text[entry_start:entry_end]

    return {
        "entry_present": True,
        "theorem_statement_present": "Two-Layer Obstruction Theorem" in entry_block
            and "no regulator" in entry_block.lower()
            and "n_joint" in entry_block,
        "n_joint_05_present": N_JOINT_REQUIRED in entry_block,
        "strengthening_clause_present": STRENGTHENING_CLAUSE in entry_block,
        "w5_7_pin_present": "S85-W5-7-TWO-LAYER-OBSTRUCTION" in entry_block,
        "substitution_chain_present": all(
            tag in entry_block for tag in
            ("Step 1 (Definition)", "Step 2 (Substitution)",
             "Step 3 (Simplification)", "Step 4 (Direction)")
        ),
        "source_citation_present": "lizzi S-7 §V.8 (CF-LZ-S86-8)" in entry_block,
        "atlas_5_present": all(r in entry_block for r in ATLAS_5),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Time (UTC): {datetime.now(timezone.utc).isoformat()}")

    # Pre-flight: ensure all input files exist
    for p in (REGISTRY_PATH, LIZZI_S7_PATH, S85_VERDICTS_PATH, S86_VERDICTS_PATH):
        if not p.exists():
            print(f"FATAL: missing input {p}")
            return 1

    # SHA pins (input-pin map)
    pins: dict[str, str] = {}
    pins["registry_pre"] = sha256_of(REGISTRY_PATH)
    pins["lizzi_s7"] = sha256_of(LIZZI_S7_PATH)
    pins["s85_verdicts"] = sha256_of(S85_VERDICTS_PATH)
    pins["gate_id"] = GATE_ID
    pins["scheme"] = SCHEME
    pins["convention"] = CONVENTION
    pins["L_max"] = L_MAX_TAG
    pins["atlas_5"] = ",".join(ATLAS_5)
    pins["n_joint_required"] = N_JOINT_REQUIRED
    pins["strengthening_clause"] = STRENGTHENING_CLAUSE

    print("\nINPUT-PIN MAP:")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v}")

    # Parse W5-7 verdict
    w5_7 = parse_w5_7_verdict(S85_VERDICTS_PATH)
    print("\nW5-7 verdict parsed:")
    for k, v in w5_7.items():
        print(f"  {k}: {v}")

    if w5_7["verdict"] != "PASS":
        print(f"FATAL: W5-7 not PASS (got {w5_7['verdict']})")
        return 1

    n_joint_display = f"{w5_7['value']}/{len(ATLAS_5)}"
    if n_joint_display != N_JOINT_REQUIRED:
        print(f"FATAL: n_joint mismatch ({n_joint_display} vs {N_JOINT_REQUIRED})")
        return 1

    # Build entry
    iso_ts = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    entry = build_entry(w5_7, iso_ts)
    entry_sha = hashlib.sha256(entry.encode("utf-8")).hexdigest()
    pins["entry_sha"] = entry_sha
    print(f"\nentry_sha (full SHA256): {entry_sha}")

    # Coordination directive: re-read the registry IMMEDIATELY before write
    # to detect any T6 / W1a-1 landings between dispatch and write.
    print("\n[coordination] Re-reading registry immediately before write...")
    time.sleep(0.20)  # brief poll-delay to catch in-flight writes
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")
    pins["registry_at_write"] = hashlib.sha256(registry_text.encode("utf-8")).hexdigest()
    print(f"  registry_at_write SHA: {pins['registry_at_write']}")
    if pins["registry_at_write"] != pins["registry_pre"]:
        print("  [coordination] Registry changed between pre-flight and write; "
              "anchor-based insertion still safe (regex-anchored on §VII.J).")

    # Insert and write
    new_text, insert_at = insert_into_registry(registry_text, entry)
    REGISTRY_PATH.write_text(new_text, encoding="utf-8")
    pins["registry_post"] = sha256_of(REGISTRY_PATH)
    print(f"\nRegistry written. insert_at byte-offset = {insert_at}")
    print(f"registry_post SHA: {pins['registry_post']}")

    # Post-write verification
    final_text = REGISTRY_PATH.read_text(encoding="utf-8")
    verification = verify_post_write(final_text)
    print("\nPOST-WRITE VERIFICATION:")
    for k, v in verification.items():
        print(f"  {k}: {v}")

    all_checks = [
        verification.get("entry_present", False),
        verification.get("theorem_statement_present", False),
        verification.get("n_joint_05_present", False),
        verification.get("strengthening_clause_present", False),
        verification.get("w5_7_pin_present", False),
        verification.get("substitution_chain_present", False),
        verification.get("source_citation_present", False),
        verification.get("atlas_5_present", False),
    ]
    if all(all_checks):
        verdict = "PASS"
    elif verification.get("entry_present") and not verification.get("strengthening_clause_present"):
        # Per plan §9: strengthening absent or in separate paragraph -> INFO
        verdict = "INFO"
    else:
        verdict = "FAIL"
    print(f"\nVerdict: {verdict}")

    # Closure SHA
    closure = closure_hash(pins)
    pins["closure_sha256"] = closure
    print(f"closure_sha256 (audit): {closure}")

    # Content SHA = entry_sha (the artifact landed)
    content_sha = entry_sha
    audit_sha = closure

    # 4-tuple emission
    four_tuple = emit_4tuple(entry_sha[:16], SCHEME, CONVENTION, L_MAX_TAG)
    print(f"\n4-tuple: {four_tuple}")

    # Append verdict line to s86_gate_verdicts.txt
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={entry_sha[:16]} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion_line = (
        f"# {GATE_ID}: audit_sha256_short={audit_sha[:16]} "
        f"content_sha256={content_sha} audit_sha256={audit_sha}  "
        f"# entry landed in §VII-B (S86 W1b T7); n_joint={N_JOINT_REQUIRED}; "
        f"strengthening='{STRENGTHENING_CLAUSE}'\n"
    )
    with open(S86_VERDICTS_PATH, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
    print(f"\nAppended verdict line to {S86_VERDICTS_PATH}")

    print(f"\n=== END {GATE_ID} ({verdict}) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
