"""S88 Phase 5b: Option-A `supersedes`-tagged corrective verdict-line emission.

Implements Ledger entries B.32 + B.33 per `.claude/rules/gate-verdicts.md`
§"Option A — sig_5 remediation pathway under absolute verdict permanence"
(S88 W8-100 user adjudication).

B.32 source: `sessions/archive/session-88/workshops/s88-w9-w3a-18-surrogate-fail-info-value.md` §V.1
B.33 source: `sessions/archive/session-88/workshops/s88-w15-alpha-s-canonical-merged.md` §V.1

Pattern (per Option A protocol §1-§5):
  1. Original verdict lines RETAINED on disk (verdict permanence absolute; never edited)
  2. Corrective verdict lines APPENDED with new audit_sha256 + content_sha256
  3. Dual-SHA companion comment row carries `supersedes=<full-64-char-old-audit-sha>`
  4. Audit_sha256 uniqueness preserved (sig_5 check before write)
  5. 3-tuple annotation row preserves S87+ schema-v2 sign/magnitude/regime semantics

Three corrective trios emitted in single script run (one per gate-ID):
  - B.32 §W3a-18 (FAIL → corrective FAIL with -SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN suffix)
  - B.33 §VII.AN W5a-37 (PASS → corrective PASS with -CORRIGENDUM-PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL suffix)
  - B.33 §VII.AO W5a-42 (PASS → corrective PASS with -CORRIGENDUM-INHERITS-VII-AN-CORRIGENDUM suffix)
"""
# Route: Route-B (n_s² − 1 identity)
# Derivation: alpha_s_canonical = n_s_FW_exact ** 2 - 1
#                              = Fraction(9561, 10000) ** 2 - 1
#                              = Fraction(-8587279, 100000000)
#
# Route-A vs Route-B route-declaration block (per `_registry_landing_audit.py`
# Class-(g) audit; S90 W1-1 K=1 calibration corpus closure):
#
#   ROUTE-A (cited at §VII.AN ORIGINAL V-anchor; pre-corrigendum):
#       "S82 W3-9 single-pole Mellin closure" — substrate-distance-1 pole
#       residue formula on the primary single-pole Mellin closure. This was
#       the V-anchor declaration at the original §VII.AN block PRE-CORRIGENDUM.
#       The cited upstream script is `computations/session-82/s82_w3_9_as_adjacent_obs.py`
#       which lacks an explicit `# Route:` header and was therefore the
#       calibration target that surfaced the Class-(g) detector at S90 W1-1.
#
#   ROUTE-B (ACTUAL implementation; CANONICAL per §VII.AN-CORRIGENDUM at
#   registry line 16882 — Option-A successor landed by this script's
#   B.33 part 1 emission):
#       The n_s² − 1 algebraic identity image of the substrate's n_s_FW_exact
#       canonical (Fraction(9561, 10000)) into the alpha_s_canonical
#       observable on Cell I (algebra-INVARIANT × Mellin pole s=3) per
#       the 4-corner classification. The identity is verified by the assert
#       at lines 39-43 of this script (closes the Class-(g) commutativity
#       check between registry-anchor declaration and producing-script body
#       at the docstring layer).
#
#   W5a-44 NEGATIVE-CALIBRATION corrigendum-evidence
#   (audit_sha256=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b)
#       empirically determined via AST-parse audit at S88 W5a-44 that the
#       prior SOURCE-DOUBLE-CITE-CO-PRIMARY anchor-structure at §VII.AN was
#       cross-corner-FORBIDDEN per algebra-axis orthogonality K=3 MANDATORY
#       (V-anchor on Cell I `n_s² − 1` image × C-anchor on Cell IV variance
#       theorem cannot be co-primary under the orthogonality K-counter).
#       The PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL anchor-structure migration
#       implemented by this script's B.33 part 1 emission canonicalizes
#       Route-B as the §VII.AN-CORRIGENDUM (Option-A successor) anchor route.
#
# Audit commutativity verification (Class-(g) PASS condition under this block):
#   registry V-anchor declares Route-B (via §VII.AN-CORRIGENDUM canonical form)
#   ↔ this script's first `# Route:` header declares Route-B
#   ⇒ `route_claimed == actual_normalized` ⇒ `anchor_diagnostic = 'PASS'`.
#
# Cross-references:
#   - `.claude/rules/registry-landing.md §"SOURCE-DOUBLE-CITE-CO-PRIMARY"` —
#     anchor-structure rule + cross-corner co-primary FORBIDDEN clause
#     (S88 W-15 V.6; B.14)
#   - `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality
#     K-counter"` — MANDATORY at K=3 (S87 W-2 R3 close)
#   - `.claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway
#     under absolute verdict permanence"` — supersedes-tag protocol this
#     script implements (S88 W8-100 user adjudication, 2026-05-05)
#   - `computations/_shared/_registry_landing_audit.py` — Class-(g) audit;
#     `read_script_route_header()` matches `^\s*#\s*(?:Route|Derivation)\s*:`
#     regex on the first 60 lines of the script (this comment block is
#     positioned within that audit window).
import hashlib
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path("C:/sandbox/Ainulindale Exflation")
VERDICT_FILE = ROOT / "computations" / "session-88" / "s88_gate_verdicts.txt"

# Canonical-constants import per .claude/rules/math-scripts.md (S34+ compliance)
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import n_s_FW_exact  # noqa: E402

# Bit-exact identity sanity check (B.1 promotion verification): the corrective
# verdict-line value strings cite alpha_s_qq=-8587279/100000000 as the Route-B
# image of n_s_FW_exact = Fraction(9561, 10000). Verify the identity holds in Q
# before emission so the supersedes successors are pinned to a verified canonical.
_alpha_s_canonical_expected = Fraction(-8587279, 100000000)
_alpha_s_canonical_computed = n_s_FW_exact ** 2 - 1
assert _alpha_s_canonical_computed == _alpha_s_canonical_expected, (
    f"n_s_FW_exact**2 - 1 sanity check FAIL: "
    f"computed {_alpha_s_canonical_computed} != expected {_alpha_s_canonical_expected}"
)

# Source workshop files for input-pin map SHA-pinning
W9_SYNTHESIS = ROOT / "sessions" / "session-88" / "workshops" / "s88-w9-w3a-18-surrogate-fail-info-value.md"
W15_SYNTHESIS = ROOT / "sessions" / "session-88" / "workshops" / "s88-w15-alpha-s-canonical-merged.md"
SUBSTRATE_FIRST_RULE = ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
REGISTRY_LANDING_RULE = ROOT / ".claude" / "rules" / "registry-landing.md"
GATE_VERDICTS_RULE = ROOT / ".claude" / "rules" / "gate-verdicts.md"


def sha256_of_file(path: Path) -> str:
    """SHA-256 of file bytes (hexdigest)."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """SHA-256 over ordered (key, value) pairs of input-pin map.

    Canonical pattern matches `_script_template.py append_verdict()` audit-SHA
    derivation: sorted-keys join with `|` separator, value coerced to str,
    UTF-8 bytes hashed.
    """
    items = sorted(pin_map.items())
    s = "|".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def content_hash(canonical_line: str) -> str:
    """SHA-256 of canonical line bytes (no trailing newline)."""
    return hashlib.sha256(canonical_line.rstrip("\n").encode("utf-8")).hexdigest()


def existing_audit_shas(verdict_file: Path) -> set:
    """Extract all audit_sha256 values from existing verdict file (sig_5 check)."""
    shas = set()
    for line in verdict_file.read_text(encoding="utf-8").splitlines():
        # Canonical lines: `<gate>: <verdict> -- ... audit_sha256=<64-hex> ...`
        if "audit_sha256=" in line and not line.startswith("#"):
            try:
                idx = line.index("audit_sha256=") + len("audit_sha256=")
                sha = line[idx:idx + 64]
                if len(sha) == 64 and all(c in "0123456789abcdef" for c in sha):
                    shas.add(sha)
            except (ValueError, IndexError):
                pass
    return shas


def main():
    print(f"S88 B.32+B.33 SUPERSEDES EMISSION")
    print(f"Verdict file: {VERDICT_FILE}")
    print(f"=" * 80)

    # Compute source-file SHAs for input-pin substrate
    w9_sha = sha256_of_file(W9_SYNTHESIS)
    w15_sha = sha256_of_file(W15_SYNTHESIS)
    sf_rule_sha = sha256_of_file(SUBSTRATE_FIRST_RULE)
    rl_rule_sha = sha256_of_file(REGISTRY_LANDING_RULE)
    gv_rule_sha = sha256_of_file(GATE_VERDICTS_RULE)

    print(f"Source pins:")
    print(f"  W-9 synthesis SHA      = {w9_sha}")
    print(f"  W-15 synthesis SHA     = {w15_sha}")
    print(f"  substrate-first.md SHA = {sf_rule_sha}")
    print(f"  registry-landing.md    = {rl_rule_sha}")
    print(f"  gate-verdicts.md SHA   = {gv_rule_sha}")
    print()

    # Pre-check existing audit_sha256s
    existing = existing_audit_shas(VERDICT_FILE)
    print(f"Existing audit_sha256 count: {len(existing)}")
    print()

    # ============================================================
    # B.32 — §W3a-18 corrective with -SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN suffix
    # Original verdict at line 80 of verdict file:
    #   audit_sha256=80405c227a1d04e9e910bf0f67c86e29bc7a83b6ab435fdf6254fe3cc12bf2d8
    # ============================================================
    b32_gate_id = "S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY"
    b32_old_audit_sha = "80405c227a1d04e9e910bf0f67c86e29bc7a83b6ab435fdf6254fe3cc12bf2d8"
    b32_value = "1.138493e+01"
    b32_scheme = "NCG-cohomology-class-Hochschild-pairing-pole-1"
    b32_corrective_convention = "iota-star-composable-preimage-construction-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN"
    b32_L_max = "10"

    b32_pin_map = {
        "gate_id": b32_gate_id,
        "supersedes_audit_sha256": b32_old_audit_sha,
        "value": b32_value,
        "scheme": b32_scheme,
        "convention": b32_corrective_convention,
        "L_max": b32_L_max,
        "verdict": "FAIL",
        "corrective_provenance": "S88-W9-W3A-18-VERDICT-LINE-SUPERSEDES-AMENDMENT",
        "corrective_session": "S88",
        "corrective_wave": "W9",
        "source_workshop_sha": w9_sha,
        "rule_pin_substrate_first_sha": sf_rule_sha,
        "rule_pin_gate_verdicts_sha": gv_rule_sha,
        "schema_version": "S87+",
    }
    b32_audit_sha = closure_hash(b32_pin_map)
    b32_canonical_line = (
        f"{b32_gate_id}: FAIL -- "
        f"value={b32_value} scheme={b32_scheme} convention={b32_corrective_convention} "
        f"L_max={b32_L_max} audit_sha256={b32_audit_sha}"
    )
    b32_content_sha = content_hash(b32_canonical_line)
    b32_canonical_line_full = (
        f"{b32_gate_id}: FAIL -- "
        f"value={b32_value} scheme={b32_scheme} convention={b32_corrective_convention} "
        f"L_max={b32_L_max} audit_sha256={b32_audit_sha} content_sha256={b32_content_sha} schema_version=S87+"
    )

    # ============================================================
    # B.33 part 1 — §VII.AN W5a-37 corrective
    # Original at line 122: audit_sha256=cf5ec646662ccf8be68a206dc96ca38a222ebc6c596131d1d923e237f217f509
    # ============================================================
    w5a37_gate_id = "S88-CF-20-SOURCE-DOUBLE-CITE-CO-PRIMARY-LANDING-FOR-ALPHA-S"
    w5a37_old_audit_sha = "cf5ec646662ccf8be68a206dc96ca38a222ebc6c596131d1d923e237f217f509"
    # Per W-15 §V.1: ANCHOR migrates from `SOURCE-DOUBLE-CITE-CO-PRIMARY` to
    #   `PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM`. ANCHOR-1 (V) becomes
    #   n_s_FW = Fraction(9561, 10000); ANCHOR-2 (C) REMOVED.
    # Substantive ratio retained per W-15 V.1: alpha_s_qq=-8587279/100000000.
    w5a37_corrective_value = (
        "slot=§VII.AN-CORRIGENDUM;anchor_structure=PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM;"
        "anchor_1_v=n_s_FW_exact=Fraction(9561,10000);anchor_2_c=REMOVED-CROSS-CORNER-FORBIDDEN-K3-MANDATORY;"
        "alpha_s_qq=-8587279/100000000;corrigendum_evidence_sha=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b;"
        "corrigendum_evidence_gate=S88-A_2-MELLIN-SPECTRUM-CACHE-DISCRIMINATOR-W5a-44;"
        "verdict_kind=PASS-vii-AN-CORRIGENDUM-route-b-canonical-anchor-restructured-cell-IV-removed-per-algebra-axis-K3-MANDATORY"
    )
    w5a37_scheme = "registry-landing-corrigendum"
    w5a37_corrective_convention = "source-double-cite-co-primary-CORRIGENDUM-PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL"
    w5a37_L_max = "N/A"

    w5a37_pin_map = {
        "gate_id": w5a37_gate_id,
        "supersedes_audit_sha256": w5a37_old_audit_sha,
        "value": w5a37_corrective_value,
        "scheme": w5a37_scheme,
        "convention": w5a37_corrective_convention,
        "L_max": w5a37_L_max,
        "verdict": "PASS",
        "corrective_provenance": "S88-VII-AN-AO-OPTION-A-CORRECTIVE-SUCCESSOR-LANDING-PHASE-5B",
        "corrective_session": "S88",
        "corrective_wave": "W15",
        "source_workshop_sha": w15_sha,
        "rule_pin_registry_landing_sha": rl_rule_sha,
        "rule_pin_gate_verdicts_sha": gv_rule_sha,
        "schema_version": "S87+",
        "anchor_structure_pre": "SOURCE-DOUBLE-CITE-CO-PRIMARY",
        "anchor_structure_post": "PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM",
        "n_s_FW_exact_pin": "Fraction(9561,10000)",
        "alpha_s_canonical_pin": "Fraction(-8587279,100000000)",
    }
    w5a37_audit_sha = closure_hash(w5a37_pin_map)
    w5a37_canonical_line = (
        f"{w5a37_gate_id}: PASS -- "
        f"value='{w5a37_corrective_value}' scheme={w5a37_scheme} convention={w5a37_corrective_convention} "
        f"L_max={w5a37_L_max} audit_sha256={w5a37_audit_sha}"
    )
    w5a37_content_sha = content_hash(w5a37_canonical_line)
    w5a37_canonical_line_full = (
        f"{w5a37_gate_id}: PASS -- "
        f"value='{w5a37_corrective_value}' scheme={w5a37_scheme} convention={w5a37_corrective_convention} "
        f"L_max={w5a37_L_max} audit_sha256={w5a37_audit_sha} content_sha256={w5a37_content_sha} schema_version=S87+"
    )

    # ============================================================
    # B.33 part 2 — §VII.AO W5a-42 corrective
    # Original at line 137: audit_sha256=d536b67445b6468d6ff9778b980aa85683216c1775926559396795139c23e110
    # ============================================================
    w5a42_gate_id = "S88-ALPHA-S-CORNER-I-WITHIN-POLE-CO-PRIMARY-REGISTRY-LANDING"
    w5a42_old_audit_sha = "d536b67445b6468d6ff9778b980aa85683216c1775926559396795139c23e110"
    # Per W-15 §V.1: ANCHOR migrates from `SOURCE-DOUBLE-CITE-CO-PRIMARY (inherits from §VII.AN)` to
    #   `PRIMARY-N_S-IMAGE (inherits §VII.AN successor)`. Pole-scope s=3 + resolution-scope A_5
    #   5-element + sigma values 13.9957σ vs Planck/ACT and 38.3360σ vs CMB-S4 forecast retained
    #   UNCHANGED (independent of anchor-structure tag).
    w5a42_corrective_value = (
        "slot=§VII.AO-CORRIGENDUM;anchor_structure=PRIMARY-N_S-IMAGE-INHERITS-VII-AN-CORRIGENDUM-SUCCESSOR;"
        "upstream_slot=§VII.AN-CORRIGENDUM;pole_scope=s3-RETAINED;resolution_scope=A_5-5-element-RETAINED;"
        "sigma_FW_vs_Planck_ACT=13.9957-RETAINED;sigma_FW_vs_CMB_S4=38.3360-RETAINED;"
        "verdict_kind=PASS-vii-AO-CORRIGENDUM-anchor-restructured-substantive-discrimination-values-RETAINED-UNCHANGED"
    )
    w5a42_scheme = "registry-landing-corner-I-corrigendum"
    w5a42_corrective_convention = "biaxial-FI-s3-pole-CORRIGENDUM-INHERITS-VII-AN-CORRIGENDUM"
    w5a42_L_max = "12"

    w5a42_pin_map = {
        "gate_id": w5a42_gate_id,
        "supersedes_audit_sha256": w5a42_old_audit_sha,
        "value": w5a42_corrective_value,
        "scheme": w5a42_scheme,
        "convention": w5a42_corrective_convention,
        "L_max": w5a42_L_max,
        "verdict": "PASS",
        "corrective_provenance": "S88-VII-AN-AO-OPTION-A-CORRECTIVE-SUCCESSOR-LANDING-PHASE-5B",
        "corrective_session": "S88",
        "corrective_wave": "W15",
        "source_workshop_sha": w15_sha,
        "rule_pin_registry_landing_sha": rl_rule_sha,
        "rule_pin_gate_verdicts_sha": gv_rule_sha,
        "schema_version": "S87+",
        "anchor_structure_pre": "SOURCE-DOUBLE-CITE-CO-PRIMARY-inherits-VII-AN",
        "anchor_structure_post": "PRIMARY-N_S-IMAGE-inherits-VII-AN-CORRIGENDUM",
        "upstream_supersedes_chain": w5a37_old_audit_sha,
    }
    w5a42_audit_sha = closure_hash(w5a42_pin_map)
    w5a42_canonical_line = (
        f"{w5a42_gate_id}: PASS -- "
        f"value='{w5a42_corrective_value}' scheme={w5a42_scheme} convention={w5a42_corrective_convention} "
        f"L_max={w5a42_L_max} audit_sha256={w5a42_audit_sha}"
    )
    w5a42_content_sha = content_hash(w5a42_canonical_line)
    w5a42_canonical_line_full = (
        f"{w5a42_gate_id}: PASS -- "
        f"value='{w5a42_corrective_value}' scheme={w5a42_scheme} convention={w5a42_corrective_convention} "
        f"L_max={w5a42_L_max} audit_sha256={w5a42_audit_sha} content_sha256={w5a42_content_sha} schema_version=S87+"
    )

    # ============================================================
    # sig_5 SHA-uniqueness check (per v3-closure-recovery.md sig_5)
    # ============================================================
    new_shas = {b32_audit_sha, w5a37_audit_sha, w5a42_audit_sha}
    print(f"Computed audit_sha256 values:")
    print(f"  B.32   §W3a-18           = {b32_audit_sha}")
    print(f"  B.33-1 §VII.AN W5a-37    = {w5a37_audit_sha}")
    print(f"  B.33-2 §VII.AO W5a-42    = {w5a42_audit_sha}")
    print()

    # Check for collisions with existing
    collisions = new_shas & existing
    if collisions:
        print(f"ERROR: SHA collision with existing verdict file:")
        for sha in collisions:
            print(f"  {sha}")
        sys.exit(1)
    # Check for collisions among the 3 new SHAs
    if len(new_shas) != 3:
        print(f"ERROR: Internal SHA collision among 3 new corrective lines")
        sys.exit(1)
    print(f"sig_5 check: PASS (all 3 new audit_sha256 values are unique vs existing {len(existing)} + each other)")
    print()

    # ============================================================
    # Compose append block (3 corrective trios + dual-SHA companion + 3-tuple annotation)
    # ============================================================
    append_block = "\n"  # leading blank for visual separation in verdict file
    append_block += "# === S88 Phase 5b Option-A `supersedes`-tagged corrective successors (B.32 + B.33) ===\n"
    append_block += "# Per `gate-verdicts.md §\"Option A — sig_5 remediation pathway under absolute verdict permanence\"`\n"
    append_block += "# (S88 W8-100 user adjudication, 2026-05-05). Original verdict lines RETAINED at original positions;\n"
    append_block += "# corrective canonical lines APPENDED below with `supersedes=<full-64-char>` tag in dual-SHA companion row.\n"
    append_block += "# Downstream consumers cite latest non-superseded line per Option A reading discipline.\n"

    # B.32 trio
    append_block += "\n"
    append_block += b32_canonical_line_full + "\n"
    append_block += (
        f"# audit_sha256_short={b32_audit_sha[:16]} content_sha256_short={b32_content_sha[:16]} "
        f"# {b32_gate_id} dual-SHA companion row (W9a-99 split); "
        f"supersedes={b32_old_audit_sha} (per `gate-verdicts.md §\"Option A\"`; "
        f"corrective adds `-SURROGATE-COHOMOLOGY-CLASS-LEVEL-PIN` suffix per S88 W-9 §V.1; "
        f"rule-pin: `substrate-first-canonical-sourcing.md §iv-bis`)\n"
    )
    append_block += (
        f"# sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {b32_gate_id} 3-tuple annotation (S87 schema-v2; preserved from original; surrogate sign-rigidity "
        f"`R_surrogate = 2*f - 1` per W-9 §V.1 algebraic-distance theorem)\n"
    )

    # B.33 part 1 (W5a-37 / §VII.AN-CORRIGENDUM)
    append_block += "\n"
    append_block += w5a37_canonical_line_full + "\n"
    append_block += (
        f"# audit_sha256_short={w5a37_audit_sha[:16]} content_sha256_short={w5a37_content_sha[:16]} "
        f"# {w5a37_gate_id} dual-SHA companion row (W9a-99 split); "
        f"supersedes={w5a37_old_audit_sha} (per `gate-verdicts.md §\"Option A\"`; "
        f"corrective ANCHOR-STRUCTURE migration SOURCE-DOUBLE-CITE-CO-PRIMARY → "
        f"PRIMARY-N_S-IMAGE-ROUTE-B-CANONICAL-WITH-CORRIGENDUM per S88 W-15 §V.1; "
        f"corrigendum evidence: W5a-44 FAIL audit_sha256=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b; "
        f"registry-side §VII.AN-CORRIGENDUM slot landing deferred to mack-cosmic-bridge writer per Ledger B.31)\n"
    )
    append_block += (
        f"# sign_verdict=N/A magnitude_verdict=PASS regime_verdict=VALID "
        f"# {w5a37_gate_id} 3-tuple annotation (S87 schema-v2; preserved from original PASS; "
        f"substantive ratio alpha_s_qq=-8587279/100000000 RETAINED unchanged per W-15 §V.1)\n"
    )

    # B.33 part 2 (W5a-42 / §VII.AO-CORRIGENDUM)
    append_block += "\n"
    append_block += w5a42_canonical_line_full + "\n"
    append_block += (
        f"# audit_sha256_short={w5a42_audit_sha[:16]} content_sha256_short={w5a42_content_sha[:16]} "
        f"# {w5a42_gate_id} dual-SHA companion row (W9a-99 split); "
        f"supersedes={w5a42_old_audit_sha} (per `gate-verdicts.md §\"Option A\"`; "
        f"corrective ANCHOR-STRUCTURE migration `SOURCE-DOUBLE-CITE-CO-PRIMARY (inherits §VII.AN)` → "
        f"`PRIMARY-N_S-IMAGE (inherits §VII.AN-CORRIGENDUM successor)` per S88 W-15 §V.1; "
        f"upstream supersedes-chain pointer: §VII.AN W5a-37 supersedes={w5a37_old_audit_sha}; "
        f"registry-side §VII.AO-CORRIGENDUM slot landing deferred to mack-cosmic-bridge writer per Ledger B.31)\n"
    )
    append_block += (
        f"# sign_verdict=N/A magnitude_verdict=PASS regime_verdict=VALID "
        f"# {w5a42_gate_id} 3-tuple annotation (S87 schema-v2; preserved from original PASS; "
        f"substantive sigma values 13.9957/38.3360 + pole-scope s3 + resolution-scope A_5 5-element RETAINED unchanged per W-15 §V.1)\n"
    )

    print(f"Append block size: {len(append_block)} bytes / {append_block.count(chr(10))} lines")
    print()
    print(f"Append block preview (first 800 chars):")
    print(append_block[:800])
    print(f"... [truncated]")
    print()

    # ============================================================
    # Append to verdict file (single open("a") atomic POSIX append)
    # ============================================================
    with open(VERDICT_FILE, "a", encoding="utf-8", newline="\n") as f:
        f.write(append_block)
        f.flush()

    print(f"APPEND SUCCESS to {VERDICT_FILE}")
    print()

    # Re-read and verify
    final_shas = existing_audit_shas(VERDICT_FILE)
    new_in_file = final_shas - existing
    print(f"Post-write audit_sha256 count: {len(final_shas)} (was {len(existing)}; delta = {len(new_in_file)})")
    print(f"New SHAs found in file:")
    for sha in sorted(new_in_file):
        print(f"  {sha}")
    if new_in_file == new_shas:
        print(f"VERIFICATION PASS: all 3 new corrective audit_sha256 values present in file")
    else:
        missing = new_shas - new_in_file
        unexpected = new_in_file - new_shas
        print(f"VERIFICATION FAIL: missing={missing}, unexpected={unexpected}")
        sys.exit(1)

    print()
    print(f"=" * 80)
    print(f"S88 Phase 5b complete (B.32 + B.33). 3 corrective trios appended.")
    print(f"  B.32   §W3a-18 audit_sha256        = {b32_audit_sha}  supersedes {b32_old_audit_sha[:16]}...")
    print(f"  B.33-1 §VII.AN W5a-37 audit_sha256 = {w5a37_audit_sha}  supersedes {w5a37_old_audit_sha[:16]}...")
    print(f"  B.33-2 §VII.AO W5a-42 audit_sha256 = {w5a42_audit_sha}  supersedes {w5a42_old_audit_sha[:16]}...")
    print()
    print(f"NOTE: B.31 (registry-side §VII.AN-CORRIGENDUM + §VII.AO-CORRIGENDUM slot landing in")
    print(f"      `permanent-results-registry.md`) remains DEFERRED to mack-cosmic-bridge writer per")
    print(f"      `feedback_mack-bridge-role.md` (sole writer for cross-pillar registry entries).")


if __name__ == "__main__":
    main()
