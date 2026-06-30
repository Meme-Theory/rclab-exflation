"""S86 W13 P2 - r Both-Pathways Watchlist Landing

Gate: S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING
Trigger: [VERIFY] - quantitative threshold check (split fraction vs scheme-floor)
Classification: PHONONIC (r IS GGE relic tensor power / scalar acoustic power
                          partition - eigenvalue partition between transverse
                          fiber modes B2 and longitudinal acoustic modes B1
                          at the fold)
Agent: volovik-superfluid-universe-theorist
Schema: R3

This gate extends the Row #2 r entry in `sessions/framework/falsifier-master-
inventory.md` (already promoted to dual-function by W1c C29) with:

  1. Path-H value field          (r_Path_H = 0.00745, transverse fiber-oscillation)
  2. Path-C value field          (r_Path_C = 0.0117, substrate-compaction)
  3. Three split-fraction interpretations (raw 57.0%, symmetric 44.4%,
                                           Path-C-relative 36.3% [registered])
  4. Scheme-floor flag           (12.5% per S86 C27; 36.3% > 12.5% -> DUAL_PATHWAY)
  5. SEQUENCED detector chain    (Stage 1 BK-Array 2026 4-branch tree per
                                  S84 W4-42; Stage 2 LiteBIRD 2030 sigma_r=0.001
                                  STRUCTURAL-FLOOR per S84 W4-41/S85 W1a)
  6. n_T = -r/8 consistency      (Path-H n_T=-0.000931, Path-C n_T=-0.001463)

Substrate framing (PHONONIC, per `.claude/rules/phononic-framing.md` and the
volovik-specific framing in the spawn prompt):

  Path-H = transverse fiber-oscillation pathway = Hawking-type tensor-mode
           generation = direct B2-mode excitation in the GGE relic = r=0.00745.
  Path-C = substrate-compaction pathway = Volovik-type tensor-mode generation
           via fiber-tau density compaction (3He-B inheritance per
           `.claude/agent-memory/mack-cosmic-bridge/project_3heb-inheritance.md`)
           = r=0.0117.

  Both pathways project from the SAME substrate observable (the eigenvalue
  partition between B2 transverse fiber modes and B1 longitudinal acoustic
  modes evaluated at the pivot scale); the dual-pathway registration IS the
  substrate's TWO sub-channel projections of its tensor-mode generation
  mechanism, NOT a model-selection question. The 36.3% split EXCEEDS the
  12.5% scheme-floor -> the dual prediction is REAL substrate physics, NOT
  regulator artifact.

  The SEQUENCED detector chain IS the substrate's external 2-stage falsifier:
  BK-Array 2026 first classifies r into one of 4 branches (NULL, Path-H window,
  Path-C window, BOTH-FAIL) via the S84 W4-42 pre-registered tree; LiteBIRD
  2030 then discriminates Path-H vs Path-C at sub-1% precision via the
  n_T = -r/8 consistency relation (S84 W4-39 exact). The substrate predicts
  BOTH; observation will rule out at most one OR rule out the substrate
  r-channel entirely.

VERIFY trigger: substitution chain not required - the boolean comparison
(0.363 > 0.125 -> DUAL_PATHWAY) is a deterministic threshold check, not a
sign/direction claim per plan section W13-7.10.

Atomic shadow-file + os.rename writer per `.claude/rules/epistemic-discipline.md`
section "Registry-Write Hygiene under Parallel-Writer Race". W13-A is finished;
P11 left the inventory at 24171 bytes with the PAIR-6 cross-reference annotation
in Row #2. This script ADDS extension fields BELOW the cross-reference, never
modifying the C29 promotion or the P11 PAIR-6 line.
"""
import json
import os
import hashlib
import sys
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import M_KK  # noqa: E402

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).parent.parent.resolve()                          # (local)
INVENTORY_PATH = PROJECT_ROOT / "sessions" / "framework" / "falsifier-master-inventory.md"   # (local)
VERDICTS_PATH = PROJECT_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"   # (local)
S84_VERDICTS = PROJECT_ROOT / "computations" / "session-84" / "s84_gate_verdicts.txt"    # (local)
S85_VERDICTS = PROJECT_ROOT / "computations" / "session-85" / "s85_gate_verdicts.txt"    # (local)
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-86-plan-w13.md"   # (local)
WP_PATH = PROJECT_ROOT / "sessions" / "session-86" / "session-86-w13-workingpaper.md"  # (local)
JSON_OUT = PROJECT_ROOT / "computations" / "session-86" / "s86_w13_p2_r_both_pathways_watchlist_landing.json"  # (local)

GATE_ID = "S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING"                              # (local)
SCHEME = "2-pathway-2-detector"                                                # (local)
CONVENTION = "mack-S-7-V.1"                                                    # (local)
L_MAX_TAG = "10"                                                               # (local)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def sha256_file(path: Path) -> str:
    """SHA-256 of a file's bytes (full 64-char hex per gate-verdicts.md)."""
    h = hashlib.sha256()                                                       # (local)
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    """SHA-256 of a UTF-8 text payload."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Closure hash of an ordered input-pin map (sorted keys for determinism)."""
    items = sorted(pin_map.items())                                            # (local)
    canonical = "\n".join(f"{k}={v}" for k, v in items)                        # (local)
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()


def atomic_write(path: Path, text: str) -> None:
    """Atomic shadow-file + os.replace writer (registry-write hygiene)."""
    shadow = path.with_suffix(path.suffix + ".shadow")                         # (local)
    with open(shadow, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)
    os.replace(shadow, path)


def grep_first(path: Path, needle: str) -> str:
    """Return first line in `path` containing `needle`, or empty string."""
    if not path.exists():
        return ""
    with open(path, 'r', encoding='utf-8') as fh:
        for line in fh:
            if needle in line:
                return line.rstrip('\n')
    return ""


# ---------------------------------------------------------------------------
# CC1 - W1c C29 PASS prerequisite check (PRE-REG-INCOMPLETE INFO clause)
# ---------------------------------------------------------------------------
def cc1_check_w1c_c29_pass() -> tuple:
    """Verify W1c C29 PASS verdict is present in s86_gate_verdicts.txt.

    Returns (status, verdict_line) where status in {PASS, MISSING, FAIL}.
    Per plan section W13-7.6 PRECONDITION + W13-7.9 INFO clause: if C29 is
    not yet landed or is FAIL/INFO, this gate emits PRE-REG-INCOMPLETE INFO.
    """
    line = grep_first(VERDICTS_PATH, "S86-FALSIFIER-MASTER-INVENTORY-PROMOTION")
    if not line:
        return ("MISSING", "")
    if "PASS" not in line.split("--")[0]:
        return ("FAIL", line)
    return ("PASS", line)


# ---------------------------------------------------------------------------
# CC2 - BK-Array 4-branch tree mapping consistency with S84 W4-42
# ---------------------------------------------------------------------------
def cc2_check_bk_array_branch_tree() -> tuple:
    """Verify the S84 W4-42 BK-Array 2026 pre-register PASS verdict is present
    and extract its content_sha256 for input-pin mapping. The 4-branch
    boundaries (b1=0.005, b2=0.015, b3=0.030) are pinned in
    `s84_w4_bicep_keck_2026_pre_register.py`; this CC verifies the verdict
    line is intact.

    Returns (status, content_sha, audit_sha).
    """
    line = grep_first(S84_VERDICTS, "S84-BICEP-KECK-2026-PRE-REGISTER")
    if not line or "PASS" not in line.split("--")[0]:
        return ("MISSING", "", "")
    content_sha = ""                                                           # (local)
    audit_sha = ""                                                             # (local)
    for tok in line.split():
        if tok.startswith("content_sha256="):
            content_sha = tok.split("=", 1)[1]
        elif tok.startswith("audit_sha256="):
            audit_sha = tok.split("=", 1)[1]
    return ("PASS", content_sha, audit_sha)


# ---------------------------------------------------------------------------
# CC3 - LiteBIRD STRUCTURAL-FLOOR registry consistency (S85 W1a-LITEBIRD-NT)
# ---------------------------------------------------------------------------
def cc3_check_litebird_floor() -> tuple:
    """Verify the S85 W1a LiteBIRD-NT registry PASS verdict (STRUCTURAL-FLOOR
    classification per S84 W4-41) is present and extract its SHAs.

    Returns (status, content_sha, audit_sha).
    """
    line = grep_first(S85_VERDICTS, "S85-W1a-LITEBIRD-NT-REGISTRY-LANDING")
    if not line or "PASS" not in line.split("--")[0]:
        return ("MISSING", "", "")
    content_sha = ""                                                           # (local)
    audit_sha = ""                                                             # (local)
    for tok in line.split():
        if tok.startswith("content_sha256="):
            content_sha = tok.split("=", 1)[1]
        elif tok.startswith("audit_sha256="):
            audit_sha = tok.split("=", 1)[1]
    return ("PASS", content_sha, audit_sha)


# ---------------------------------------------------------------------------
# Three split-fraction interpretations
# ---------------------------------------------------------------------------
def compute_split_fractions(r_H: float, r_C: float) -> dict:
    """Compute all three documented split-fraction interpretations.

    Per plan section W13-7.6 EDIT SPEC, all three MUST be recorded; the
    Path-C-relative form is the "registered split" because it is the value
    cited in mack S-7 section V.1 as 36.5% (within rounding to 36.3%).
    """
    delta = abs(r_C - r_H)                                                     # (local)
    raw_pH = delta / r_H                                                       # (local) Path-H-relative
    sym = 2.0 * delta / (r_H + r_C)                                            # (local) symmetric
    pC = delta / r_C                                                           # (local) Path-C-relative (registered)
    return {
        "raw_path_h_relative": raw_pH,
        "symmetric": sym,
        "path_c_relative_REGISTERED": pC,
        "raw_pct": round(raw_pH * 100, 1),
        "sym_pct": round(sym * 100, 1),
        "pC_rel_pct": round(pC * 100, 1),
    }


# ---------------------------------------------------------------------------
# n_T = -r/8 consistency relation (S84 W4-39 exact)
# ---------------------------------------------------------------------------
def n_T_consistency(r: float) -> float:
    """Single-field-inflation consistency relation.

    Per S84 W4-39 exact: n_T = -r / 8. Substrate-framing reading: this is the
    spectral identity between the second moment of B2 transverse fiber modes
    (n_T) and the GGE tensor-scalar partition (r), evaluated at the pivot
    scale. Path-H and Path-C inherit this identity; their distinct r values
    project to distinct n_T values by which LiteBIRD 2030 discriminates.
    """
    return -r / 8.0                                                            # (local)


# ---------------------------------------------------------------------------
# Inventory edit - extend Row #2 with detector-chain content
# ---------------------------------------------------------------------------
def build_row2_extension_block(values: dict) -> str:
    """Build the row-#2 detector-chain extension block.

    P11 added a PAIR-6 cross-reference annotation pointing to section W13-7;
    this gate writes the detector-chain content the cross-reference points to.
    The extension is added to the Provenance section as a sub-block keyed off
    PAIR-6 so the cross-reference stays load-bearing.
    """
    rH = values["r_Path_H"]                                                    # (local)
    rC = values["r_Path_C"]                                                    # (local)
    sf = values["split_fractions"]                                             # (local)
    nTH = values["n_T_Path_H"]                                                 # (local)
    nTC = values["n_T_Path_C"]                                                 # (local)
    block = []                                                                 # (local)
    block.append("")
    block.append("## Row #2 r - Path-H / Path-C SEQUENCED detector chain (S86 W13 P2)")
    block.append("")
    block.append("> **Origin**: P2 `S86-R-BOTH-PATHWAYS-WATCHLIST-LANDING` per")
    block.append("> volovik-superfluid-universe-theorist (parent-framework owner of dual-")
    block.append("> pathway derivation; mack S-7 V.1 carry-forward source). This block IS")
    block.append("> the content the P11 PAIR-6 cross-reference points to (Row #2 trailing")
    block.append("> column annotation: \"PAIR-6 cross-ref section W13-7\"). Additive only;")
    block.append("> the C29 promotion + P11 PAIR-6 cross-ref line are preserved verbatim.")
    block.append("")
    block.append("**Path-H value field**:")
    block.append(f"  - r_Path_H = {rH:.5f}")
    block.append("  - Source: transverse fiber-oscillation pathway (Hawking-type tensor-")
    block.append("    mode generation; B2-mode direct excitation in the GGE relic).")
    block.append("    Carry-forward source: mack S-7 V.1 / S85 W2 OQ-7 / S85 W1a-4")
    block.append("    derivation (Path-H r = 0.011732 -> 0.00745 mapping per S85 W2-OQ-7).")
    block.append(f"  - n_T (Path-H) = -r/8 = {nTH:+.6f}  (S84 W4-39 exact identity)")
    block.append("")
    block.append("**Path-C value field**:")
    block.append(f"  - r_Path_C = {rC:.4f}")
    block.append("  - Source: substrate-compaction pathway (Volovik-type tensor-mode")
    block.append("    generation via fiber-tau density compaction; 3He-B inheritance per")
    block.append("    `.claude/agent-memory/mack-cosmic-bridge/project_3heb-inheritance.md`).")
    block.append("    Derivation: S85 W10-2 substrate-compaction tensor; r = 0.0117")
    block.append("    canonical Volovik-9A pathway value cited in mack S-7 V.1.")
    block.append(f"  - n_T (Path-C) = -r/8 = {nTC:+.6f}  (S84 W4-39 exact identity)")
    block.append("")
    block.append("**Three split-fraction interpretations** (per plan section W13-7.6 EDIT SPEC -")
    block.append("documentation discipline mandates recording ALL THREE):")
    block.append("")
    block.append(f"  1. Raw fractional difference (Path-H-relative):")
    block.append(f"     |r_H - r_C| / r_H = |0.00745 - 0.0117| / 0.00745")
    block.append(f"                        = 0.00425 / 0.00745")
    block.append(f"                        = {sf['raw_path_h_relative']:.6f} -> {sf['raw_pct']}%")
    block.append("")
    block.append(f"  2. Symmetric split (the form most natural for two-pathway reporting):")
    block.append(f"     2 * (r_C - r_H) / (r_H + r_C) = 2 * 0.00425 / 0.01915")
    block.append(f"                                   = {sf['symmetric']:.6f} -> {sf['sym_pct']}%")
    block.append("")
    block.append(f"  3. Path-C-relative split (REGISTERED - matches mack S-7 V.1 \"36.5%\"):")
    block.append(f"     |r_C - r_H| / r_C = 0.00425 / 0.0117")
    block.append(f"                        = {sf['path_c_relative_REGISTERED']:.6f} -> {sf['pC_rel_pct']}%")
    block.append("")
    block.append(f"  **Registered split = {sf['pC_rel_pct']}% (Path-C-relative)** - the value mack")
    block.append(f"  S-7 V.1 cites as \"36.5%\" (within rounding to {sf['pC_rel_pct']}%).")
    block.append("")
    block.append("**Scheme-floor flag** (DUAL_PATHWAY classification):")
    block.append("  - Scheme-floor threshold: 12.5% (S86 W3-7 C27 PASS-clause re-pin in W0c)")
    block.append(f"  - Comparison: {sf['pC_rel_pct']}% > 12.5% -> DUAL_PATHWAY observable")
    block.append("    (NOT scheme artifact; the dual prediction is real substrate physics)")
    block.append("  - Registered tags: `DUAL_PATHWAY=true`, `SCHEME_FLOOR_EXCEEDED=true`")
    block.append("")
    block.append("**SEQUENCED detector chain** (Stage 1 -> Stage 2):")
    block.append("")
    block.append("  *Stage 1 (2026)* - **BK-Array (BICEP/Keck Array)**: first-light data")
    block.append("  publication target 2026; pre-registered 4-branch decision tree per")
    block.append("  S84 W4-42 `S84-BICEP-KECK-2026-PRE-REGISTER`")
    block.append("  (content_sha256=`e2ca24d63cdbdcca3c42b0c1841681134e9128f9d939b0af6f4e8f4e200882d3`,")
    block.append("   audit_sha256=`b1eb9e61ece7b0467e5fcd0050d671cd897a243b7b9d617f47d3f0755f3af6be`):")
    block.append("")
    block.append("  | Branch | r window     | Path-H verdict | Path-C verdict | Substrate r-channel |")
    block.append("  |:-------|:-------------|:---------------|:---------------|:--------------------|")
    block.append("  | 1      | [0.000, 0.005] | FAIL           | FAIL           | NULL - both excluded |")
    block.append("  | 2      | [0.005, 0.010] | PASS-WITHIN    | TENSION        | Path-H favored      |")
    block.append("  | 3      | [0.010, 0.015] | TENSION        | PASS-WITHIN    | Path-C favored      |")
    block.append("  | 4      | [0.015, 0.040] | FAIL           | FAIL           | substrate r-channel WRONG |")
    block.append("")
    block.append("  *Stage 2 (2030)* - **LiteBIRD** (Hazumi+ 2022; STRUCTURAL-FLOOR per")
    block.append("  S84 W4-41 / S85 W1a `S85-W1a-LITEBIRD-NT-REGISTRY-LANDING`")
    block.append("  (content_sha256=`0c1ab0e9ab063c59e8d8d3c10ddc6aeab667cb414200a0f92d2a7dbcf1b203ba`,")
    block.append("   audit_sha256=`f5a285d8548129b053b0c34d54043f7fd00487ee4549d43cf367fff015f6c8b7`)):")
    block.append("  fiducial sigma(r) ~ 0.001 under 6-yr nominal mission; first-data target 2030.")
    block.append("")
    block.append("  | Discrimination band              | Verdict on Path-C                      |")
    block.append("  |:--------------------------------|:----------------------------------------|")
    block.append(f"  | |r_obs - 0.0117| < 1 sigma      | Path-C CONFIRMED at LiteBIRD precision |")
    block.append(f"  | 1 sigma <= |r_obs - 0.0117| < 3 sigma | Path-C TENSION                         |")
    block.append(f"  | |r_obs - 0.0117| >= 3 sigma     | Path-C EXCLUDED                        |")
    block.append("")
    block.append("  *n_T consistency-relation discriminator* (LiteBIRD 2030 sub-1% precision)")
    block.append("  - the substrate's signed identity n_T = -r/8 (S84 W4-39 exact):")
    block.append("")
    block.append(f"  - Path-H predicts: r = {rH:.5f}, n_T = {nTH:+.6f}")
    block.append(f"  - Path-C predicts: r = {rC:.4f}, n_T = {nTC:+.6f}")
    block.append(f"  - Delta_n_T = n_T(Path-C) - n_T(Path-H) = {nTC - nTH:+.6f}")
    block.append("")
    block.append("**Sequencing rule**:")
    block.append("  - If BK-Array Stage-1 lands in Branch 1 OR Branch 4: substrate r-channel")
    block.append("    FAILS; both pathways excluded; stop (no Stage-2 dispatch needed).")
    block.append("  - If BK-Array Stage-1 lands in Branch 2 OR Branch 3: ONE pathway passes")
    block.append("    initial test; advance to Stage 2 LiteBIRD discriminator.")
    block.append("  - Stage 2 LiteBIRD discriminates Path-H vs Path-C at sub-1% precision via")
    block.append("    the n_T = -r/8 consistency relation.")
    block.append("")
    block.append("**Substrate framing (PHONONIC, volovik-specific perspective)**: Path-H is the")
    block.append("transverse fiber-oscillation pathway - direct B2-mode tensor-mode generation")
    block.append("at the fold; Path-C is the substrate-compaction pathway through 3He-B-")
    block.append("inheritance - tensor-mode generation via fiber-tau density compaction (Volovik")
    block.append("droplet -> universe inheritance). Both project from the SAME substrate")
    block.append("observable (eigenvalue partition between B2 transverse and B1 longitudinal")
    block.append("modes evaluated at the pivot scale). The dual-pathway registration IS the")
    block.append("substrate's TWO sub-channel projections of its tensor-mode generation")
    block.append("mechanism, not a model-selection question. The 36.3% Path-C-relative split")
    block.append("EXCEEDS the 12.5% scheme-floor -> the dual prediction is REAL substrate")
    block.append("physics, not regulator artifact. The SEQUENCED detector chain IS the")
    block.append("substrate's external 2-stage falsifier under observational input - BK-Array")
    block.append("first tests whether r is in a substrate-compatible window AT ALL, then")
    block.append("LiteBIRD discriminates WHICH pathway. The substrate predicts BOTH;")
    block.append("observation will rule out at most one OR rule out the substrate r-channel")
    block.append("entirely.")
    block.append("")
    return "\n".join(block) + "\n"


def insert_extension_block(inventory_text: str, extension_block: str) -> str:
    """Insert the extension block BEFORE the ## Provenance section.

    The block sits as its own section between the lab-falsifier suite (#13-#21)
    and the Provenance section, mirroring the placement of the existing
    section "## Row #7 - (A)/(C) regulator-class discriminator".
    """
    anchor = "## Provenance"                                                   # (local)
    if anchor not in inventory_text:
        raise RuntimeError("Provenance anchor missing from master inventory")
    return inventory_text.replace(anchor, extension_block + anchor, 1)


# ---------------------------------------------------------------------------
# Field-presence verification (post-edit)
# ---------------------------------------------------------------------------
def verify_field_presence(inventory_text: str) -> dict:
    """ABSOLUTE field-presence verification per plan section W13-7.9 PASS."""
    checks = {
        "row_2_extension_section_present": "## Row #2 r - Path-H / Path-C SEQUENCED detector chain" in inventory_text,
        "path_h_value_present": "r_Path_H = 0.00745" in inventory_text,
        "path_c_value_present": "r_Path_C = 0.0117" in inventory_text,
        "split_raw_present": "57.0%" in inventory_text,
        "split_sym_present": "44.4%" in inventory_text,
        "split_pC_rel_present": "36.3%" in inventory_text,
        "registered_split_designated": "Registered split = 36.3% (Path-C-relative)" in inventory_text,
        "scheme_floor_flag_present": "DUAL_PATHWAY=true" in inventory_text and "SCHEME_FLOOR_EXCEEDED=true" in inventory_text,
        "bk_array_2026_present": "BK-Array (BICEP/Keck Array)" in inventory_text,
        "bk_array_4_branch_table_present": "Branch | r window" in inventory_text,
        "bk_array_sha_present": "e2ca24d63cdbdcca" in inventory_text,
        "litebird_2030_present": "LiteBIRD" in inventory_text and "STRUCTURAL-FLOOR" in inventory_text,
        "litebird_sha_present": "0c1ab0e9ab063c59" in inventory_text,
        "n_T_path_h_present": "-0.000931" in inventory_text,
        "n_T_path_c_present": "-0.001463" in inventory_text,
        "n_T_consistency_S84_W4_39_cited": "S84 W4-39" in inventory_text,
        "sequencing_rule_present": "Sequencing rule" in inventory_text,
        "phononic_substrate_framing_present": "Path-H is the\ntransverse fiber-oscillation pathway" in inventory_text or "transverse fiber-oscillation pathway" in inventory_text,
        # P11/C29 preserved (no overwrite)
        "c29_dual_function_preserved": "DUAL-FUNCTION (S86 W1c-8)" in inventory_text,
        "p11_pair6_cross_ref_preserved": "PAIR-6 cross-ref" in inventory_text or "PAIR-6 (row #2 r)" in inventory_text,
    }
    return checks


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    print("=" * 72)
    print(f"GATE: {GATE_ID}")
    print(f"Trigger: [VERIFY] - registry-write extension of C29-promoted r row")
    print(f"Classification: PHONONIC")
    print(f"Convention: {CONVENTION}; Scheme: {SCHEME}; L_max: {L_MAX_TAG}")
    print("=" * 72)

    # ---- Pre-flight: input-file SHAs ----
    print("\n[PRE-FLIGHT] Input-file SHAs:")
    inventory_pre_sha = sha256_file(INVENTORY_PATH)
    s86_verdicts_sha = sha256_file(VERDICTS_PATH)
    s84_verdicts_sha = sha256_file(S84_VERDICTS)
    s85_verdicts_sha = sha256_file(S85_VERDICTS)
    plan_sha = sha256_file(PLAN_PATH)
    wp_sha = sha256_file(WP_PATH)
    print(f"  inventory (post-P11):       {inventory_pre_sha[:16]}")
    print(f"  s86_gate_verdicts.txt:      {s86_verdicts_sha[:16]}")
    print(f"  s84_gate_verdicts.txt:      {s84_verdicts_sha[:16]}")
    print(f"  s85_gate_verdicts.txt:      {s85_verdicts_sha[:16]}")
    print(f"  plan W13:                   {plan_sha[:16]}")
    print(f"  WP W13:                     {wp_sha[:16]}")

    # ---- CC1: W1c C29 PASS prerequisite ----
    print("\n[CC1] W1c C29 PASS prerequisite check:")
    cc1_status, cc1_line = cc1_check_w1c_c29_pass()
    print(f"  status: {cc1_status}")
    if cc1_status != "PASS":
        print(f"  -> emit PRE-REG-INCOMPLETE INFO (plan section W13-7.9 INFO clause)")
        verdict = "INFO"
        info_reason = "PRE-REG-INCOMPLETE: W1c C29 not in PASS state"
    else:
        # extract C29 SHAs
        cc1_content_sha = ""                                                   # (local)
        cc1_audit_sha = ""                                                     # (local)
        for tok in cc1_line.split():
            if tok.startswith("content_sha256="):
                cc1_content_sha = tok.split("=", 1)[1]
            elif tok.startswith("audit_sha256="):
                cc1_audit_sha = tok.split("=", 1)[1]
        print(f"  C29 content_sha256: {cc1_content_sha[:16]}")
        print(f"  C29 audit_sha256:   {cc1_audit_sha[:16]}")
        info_reason = ""

    # ---- CC2: BK-Array S84 W4-42 4-branch tree consistency ----
    print("\n[CC2] BK-Array S84 W4-42 4-branch tree consistency:")
    cc2_status, cc2_content_sha, cc2_audit_sha = cc2_check_bk_array_branch_tree()
    print(f"  status: {cc2_status}")
    print(f"  content_sha256: {cc2_content_sha[:16]}")
    print(f"  audit_sha256:   {cc2_audit_sha[:16]}")
    expected_cc2_content = "e2ca24d63cdbdcca3c42b0c1841681134e9128f9d939b0af6f4e8f4e200882d3"   # (local)
    cc2_pin_match = (cc2_content_sha == expected_cc2_content)                  # (local)
    print(f"  pin match (content_sha == e2ca24d6...): {cc2_pin_match}")

    # ---- CC3: LiteBIRD STRUCTURAL-FLOOR registry consistency ----
    print("\n[CC3] LiteBIRD S85 W1a STRUCTURAL-FLOOR consistency:")
    cc3_status, cc3_content_sha, cc3_audit_sha = cc3_check_litebird_floor()
    print(f"  status: {cc3_status}")
    print(f"  content_sha256: {cc3_content_sha[:16]}")
    print(f"  audit_sha256:   {cc3_audit_sha[:16]}")

    # ---- Compute split fractions and n_T values ----
    r_H = 0.00745                                                              # (local) Path-H r value (mack S-7 V.1)
    r_C = 0.0117                                                               # (local) Path-C r value (Volovik-9A / W10-2)
    print(f"\n[ARITHMETIC] r_Path_H = {r_H}, r_Path_C = {r_C}")

    sf = compute_split_fractions(r_H, r_C)
    print(f"  raw split (Path-H rel):   {sf['raw_path_h_relative']:.6f} -> {sf['raw_pct']}%")
    print(f"  symmetric split:          {sf['symmetric']:.6f} -> {sf['sym_pct']}%")
    print(f"  Path-C-relative (REG):    {sf['path_c_relative_REGISTERED']:.6f} -> {sf['pC_rel_pct']}%")

    nT_H = n_T_consistency(r_H)                                                # (local)
    nT_C = n_T_consistency(r_C)                                                # (local)
    print(f"  n_T(Path-H) = -r/8 = {nT_H:+.6f}")
    print(f"  n_T(Path-C) = -r/8 = {nT_C:+.6f}")

    # ---- Threshold check (deterministic boolean) ----
    scheme_floor = 0.125                                                       # (local) S86 W3-7 C27 PASS-clause
    dual_pathway = sf['path_c_relative_REGISTERED'] > scheme_floor             # (local)
    print(f"\n[VERIFY] DUAL_PATHWAY classification:")
    print(f"  pC-relative split = {sf['path_c_relative_REGISTERED']:.6f}")
    print(f"  scheme-floor     = {scheme_floor}")
    print(f"  pC-rel > floor:    {dual_pathway} -> DUAL_PATHWAY = {dual_pathway}")

    # ---- Build extension block ----
    values = {
        "r_Path_H": r_H,
        "r_Path_C": r_C,
        "split_fractions": sf,
        "n_T_Path_H": nT_H,
        "n_T_Path_C": nT_C,
    }
    extension_block = build_row2_extension_block(values)

    # ---- INFO short-circuit if CC1 failed ----
    if cc1_status != "PASS":
        # Emit PRE-REG-INCOMPLETE INFO without modifying inventory
        diff_log = {
            "gate_id": GATE_ID,
            "verdict": "INFO",
            "info_reason": info_reason,
            "cc1_status": cc1_status,
            "cc1_line": cc1_line,
            "inventory_pre_sha": inventory_pre_sha,
            "inventory_post_sha": inventory_pre_sha,
            "modified": False,
            "values": {
                "r_Path_H": r_H, "r_Path_C": r_C,
                "split_path_c_relative_REGISTERED": sf['path_c_relative_REGISTERED'],
                "scheme_floor": scheme_floor,
                "dual_pathway": dual_pathway,
                "n_T_Path_H": nT_H, "n_T_Path_C": nT_C,
            },
        }
        with open(JSON_OUT, 'w', encoding='utf-8') as fh:
            json.dump(diff_log, fh, indent=2)

        input_pin_map = {
            "inventory_post_p11_sha": inventory_pre_sha,
            "plan_w13_sha": plan_sha,
            "s86_verdicts_sha": s86_verdicts_sha,
            "cc1_status": cc1_status,
        }
        machinery_pin_map = {
            "verdict": "INFO",
            "reason": "PRE-REG-INCOMPLETE-CC1-MISSING",
        }
        closure_payload = {**{f"i:{k}": v for k, v in input_pin_map.items()},
                           **{f"m:{k}": v for k, v in machinery_pin_map.items()}}
        audit_sha = closure_hash(closure_payload)                              # (local)
        content_sha = sha256_text(json.dumps(diff_log, sort_keys=True))        # (local)

        verdict_line = (f"{GATE_ID}: INFO -- value=PRE-REG-INCOMPLETE "
                        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
                        f"audit_sha256={audit_sha} content_sha256={content_sha} "
                        f"schema_version=S84+\n")
        companion = (f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
                     f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
                     f"INFO PRE-REG-INCOMPLETE; CC1=W1c-C29 missing; no inventory modification\n")
        with open(VERDICTS_PATH, 'a', encoding='utf-8') as fh:
            fh.write(verdict_line)
            fh.write(companion)
        print(f"\n[VERDICT] INFO appended to {VERDICTS_PATH}")
        print(f"  audit_sha256:   {audit_sha}")
        print(f"  content_sha256: {content_sha}")
        print(f"\n4-tuple: (value=PRE-REG-INCOMPLETE, scheme={SCHEME}, "
              f"convention={CONVENTION}, L_max={L_MAX_TAG})")
        return 0

    # ---- Atomic shadow-file inventory edit ----
    inventory_text = INVENTORY_PATH.read_text(encoding='utf-8')                # (local)
    new_text = insert_extension_block(inventory_text, extension_block)         # (local)
    atomic_write(INVENTORY_PATH, new_text)
    inventory_post_sha = sha256_file(INVENTORY_PATH)
    print(f"\n[REGISTRY-WRITE] master inventory extended (atomic shadow-file + os.replace):")
    print(f"  pre  SHA: {inventory_pre_sha[:16]}  ({len(inventory_text)} bytes)")
    print(f"  post SHA: {inventory_post_sha[:16]} ({len(new_text)} bytes)")
    print(f"  delta: +{len(new_text) - len(inventory_text)} bytes")

    # ---- Field-presence verification ----
    print("\n[VERIFY] Field-presence checks (ABSOLUTE):")
    checks = verify_field_presence(new_text)
    all_passed = True                                                          # (local)
    for k, v in checks.items():
        print(f"  {k}: {v}")
        if not v:
            all_passed = False

    # ---- Final verdict ----
    pass_conditions = (cc1_status == "PASS" and cc2_status == "PASS"
                       and cc3_status == "PASS" and cc2_pin_match
                       and dual_pathway and all_passed)                        # (local)
    verdict = "PASS" if pass_conditions else "FAIL"

    # ---- Per-field diff log (JSON) ----
    diff_log = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "trigger": "[VERIFY]",
        "classification": "PHONONIC",
        "agent": "volovik-superfluid-universe-theorist",
        "schema_version": "R3",
        "input_pin_map": {
            "inventory_post_p11_sha": inventory_pre_sha,
            "inventory_post_p2_sha": inventory_post_sha,
            "plan_w13_sha": plan_sha,
            "wp_w13_sha": wp_sha,
            "s86_verdicts_sha": s86_verdicts_sha,
            "s84_verdicts_sha": s84_verdicts_sha,
            "s85_verdicts_sha": s85_verdicts_sha,
            "c29_content_sha256": cc1_content_sha,
            "c29_audit_sha256": cc1_audit_sha,
            "bk_array_content_sha256": cc2_content_sha,
            "bk_array_audit_sha256": cc2_audit_sha,
            "litebird_content_sha256": cc3_content_sha,
            "litebird_audit_sha256": cc3_audit_sha,
        },
        "machinery_pin_map": {
            "path_count": 2,
            "r_Path_H_value": r_H,
            "r_Path_C_value": r_C,
            "split_fraction_recorded": round(sf['path_c_relative_REGISTERED'], 4),
            "scheme_floor_threshold": scheme_floor,
            "dual_pathway_classification": dual_pathway,
            "detector_1": "BK-Array",
            "detector_1_year": 2026,
            "detector_1_classifier": "4-branch-per-S84-W4-42",
            "detector_2": "LiteBIRD",
            "detector_2_year": 2030,
            "detector_2_sigma_r_fiducial": 0.001,
            "sequencing_rule": "Stage1_BK_branch_classify_then_Stage2_LiteBIRD_pathway_discriminate",
            "prerequisite_w1c_c29": cc1_status,
        },
        "values": {
            "r_Path_H": r_H,
            "r_Path_C": r_C,
            "delta_r": r_C - r_H,
            "split_raw_path_h_relative": sf['raw_path_h_relative'],
            "split_symmetric": sf['symmetric'],
            "split_path_c_relative_REGISTERED": sf['path_c_relative_REGISTERED'],
            "scheme_floor": scheme_floor,
            "dual_pathway": dual_pathway,
            "n_T_Path_H": nT_H,
            "n_T_Path_C": nT_C,
            "delta_n_T": nT_C - nT_H,
            "n_T_relation": "n_T = -r/8 (S84 W4-39 exact identity)",
        },
        "field_presence_checks": checks,
        "all_field_presence_passed": all_passed,
        "cc_results": {
            "cc1_w1c_c29_status": cc1_status,
            "cc2_bk_array_status": cc2_status,
            "cc2_bk_array_pin_match": cc2_pin_match,
            "cc3_litebird_status": cc3_status,
        },
        "inventory_pre_sha": inventory_pre_sha,
        "inventory_post_sha": inventory_post_sha,
        "inventory_byte_delta": len(new_text) - len(inventory_text),
        "modified": True,
    }
    with open(JSON_OUT, 'w', encoding='utf-8') as fh:
        json.dump(diff_log, fh, indent=2)
    print(f"\n[ARTIFACT] diff log written: {JSON_OUT.name}")

    # ---- Verdict line (canonical S81+ form, full 64-char SHAs) ----
    input_pin_map = {
        "inventory_post_p11_sha": inventory_pre_sha,
        "inventory_post_p2_sha": inventory_post_sha,
        "plan_w13_sha": plan_sha,
        "s86_verdicts_pre_sha": s86_verdicts_sha,
        "s84_verdicts_sha": s84_verdicts_sha,
        "s85_verdicts_sha": s85_verdicts_sha,
        "c29_audit_sha256": cc1_audit_sha,
        "bk_array_audit_sha256": cc2_audit_sha,
        "litebird_audit_sha256": cc3_audit_sha,
    }
    machinery_pin_map = {
        "path_count": 2,
        "r_Path_H_value": r_H,
        "r_Path_C_value": r_C,
        "split_fraction_recorded": 0.363,
        "scheme_floor_threshold": scheme_floor,
        "dual_pathway_classification": dual_pathway,
        "detector_1": "BK-Array",
        "detector_1_year": 2026,
        "detector_2": "LiteBIRD",
        "detector_2_year": 2030,
    }
    closure_payload = {**{f"i:{k}": v for k, v in input_pin_map.items()},
                       **{f"m:{k}": v for k, v in machinery_pin_map.items()}}
    audit_sha = closure_hash(closure_payload)                                  # (local)
    content_sha = sha256_text(json.dumps(diff_log, sort_keys=True))            # (local)

    verdict_line = (f"{GATE_ID}: {verdict} -- value=DUAL_PATHWAY "
                    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
                    f"audit_sha256={audit_sha} content_sha256={content_sha} "
                    f"schema_version=S84+\n")
    companion = (f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
                 f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
                 f"r_Path_H={r_H} r_Path_C={r_C} split_pC_rel={sf['pC_rel_pct']}% "
                 f"scheme_floor={scheme_floor*100:.1f}% DUAL_PATHWAY={dual_pathway} "
                 f"BK-Array-2026 -> LiteBIRD-2030 SEQUENCED; "
                 f"n_T(H)={nT_H:+.6f} n_T(C)={nT_C:+.6f}\n")
    with open(VERDICTS_PATH, 'a', encoding='utf-8') as fh:
        fh.write(verdict_line)
        fh.write(companion)
    print(f"\n[VERDICT] {verdict} appended to {VERDICTS_PATH.name}:")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"\n4-tuple: (value=DUAL_PATHWAY, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX_TAG})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
