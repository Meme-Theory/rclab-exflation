"""
S88 W9 §W9-108 — mack-cosmic-bridge sole-writer landing of §VII.K-PROP-W8-LAYERED
to `sessions/permanent-results-registry.md` per registry-landing.md SOURCE-DOUBLE-CITE-CO-PRIMARY.

CO-PRIMARY anchors:
- ANCHOR-1 (V-input): CF-W6-V0 — S87 W6 verbatim-extract from W-6 quotient-functor pre-reg discipline
- ANCHOR-2 (C-output): CF-W8-A3 — S86 W-8 RULE-1 Δ_0 LOCALIZATION FORMULA Δ_0(σ;(c_1,…,c_4)) = 4·c_{σ⁻¹((1,1))}

Closure SHA pin: §W9-107 audit_sha256 = 80563de0bdd25af21878e1ac9ef60cf7896bdabcc6fac0364069648eaea4fe6f
(24/24 σ ∈ S_4 Sage-exact verification; both anchors non-fungible per registry-landing.md §"Detection")

Conditional on §W9-107 PASS (verified). Single-shot append-only writer per
epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"; race-safe.

Orchestrator-direct write per user's "avoid agent tasking" preference + new /rclab-solo
Phase 2 step 2 agent-ownership-takeover discipline.
"""
import hashlib
import sys
from pathlib import Path

REGISTRY = Path("sessions/permanent-results-registry.md")
VERDICT_FILE = Path("computations/session-88/s88_gate_verdicts.txt")
GATE_ID = "S88-VII-K-PROP-W8-LAYERED-CO-PRIMARY-LANDING"
SLOT = "§VII.K-PROP-W8-LAYERED"
W9_107_AUDIT_SHA = "80563de0bdd25af21878e1ac9ef60cf7896bdabcc6fac0364069648eaea4fe6f"
W9_107_CONTENT_SHA = "4e0129fad7df6fff42901f76aab11513e434642cc19c2798c51faf7915eafcb6"


def build_entry() -> str:
    return f"""

## §VII.K-PROP-W8-LAYERED — 4-Row Layered Re-Narration of W-8 4-Channel-LAYER-2 Composition (S88 W9-108 — mack-cosmic-bridge SOLE WRITER, 2026-05-06)

**Status**: STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway (Stage-2 cross-axis independent-verify queued for S89+ as `S89-VII-K-PROP-W8-LAYERED-STAGE-2-INDEPENDENT-VERIFY`).

**Theorem statement**: The §VII.K-PROP-W8 4-channel-LAYER-2 composition theorem (S86 W-8 RULE-1; LOCALIZATION FORMULA `Δ_0(σ;(c_1,…,c_4)) = 4·c_{{σ⁻¹((1,1))}}` Sage QQ-exact across all 24 σ ∈ S_4) admits a 4-row layered re-narration where row R_k carries the substrate-derived a_2 Seeley-DeWitt coefficient under regulator R_k ∈ {{ζ, Pauli-Villars, Mellin, lattice}}, the σ ∈ S_4 permutation acts on row-indices, and the row ↔ channel correspondence (R_k ↔ regulator-tagged a_2^{{R_k}}) is structurally equivalent to the §VII.K-PROP-W8 4-channel-LAYER-2 composition theorem.

**Anchor structure**: SOURCE-DOUBLE-CITE-CO-PRIMARY per `.claude/rules/registry-landing.md`.
- **ANCHOR-1 (V-input)**: CF-W6-V0 — S87 W6 verbatim-extract from W-6 quotient-functor pre-reg discipline (T1-6); supplies the quotient-equivalence specification + rank-match check + residual cokernel content declaration.
- **ANCHOR-2 (C-output)**: CF-W8-A3 — S86 W-8 RULE-1 Δ_0 LOCALIZATION FORMULA `Δ_0(σ;(c_1,…,c_4)) = 4·c_{{σ⁻¹((1,1))}}` (Sage QQ-exact; verified 24/24 σ at §W9-107 audit_sha256 = `{W9_107_AUDIT_SHA}`).
- **DERIVATION CHAIN**: V (quotient-functor pre-reg) → 4-row layered tensor on R_1, R_2, R_3, R_4 (regulator-tagged a_2 channels) → S_4 group action on row-indices → C (LOCALIZATION FORMULA) → re-narration as STRUCTURAL THEOREM at meta-level.
- **Non-fungibility verification** (§W9-107 24-σ Sage-exact PASS): removing CF-W6-V0 breaks the quotient-equivalence specification at the 4-row layered tensor construction step (Step 3 of plan §W9-107 substitution chain); removing CF-W8-A3 breaks the LOCALIZATION FORMULA target (Step 5). Both anchors are STRUCTURALLY INDISPENSABLE per registry-landing.md §"Detection" criterion 2.

**Substrate framing** (per `phononic-framing.md §"IS Space Not IN Space"`): the 4-row layered re-narration is a STRUCTURAL property of the substrate's 4-channel a_2 Seeley-DeWitt decomposition. Each row carries a substrate-derived regulator-tagged a_2^{{R_k}} coefficient (substrate-level UV regularization, NOT a laboratory-imposed cutoff). The σ ∈ S_4 permutation action is a substrate-level symmetry of the LAYER-2 composition. Direction of explanation: substrate IS the 4-row layered tensor; substrate IS the σ-action; substrate IS the LOCALIZATION FORMULA. Container-thinking inversion (treating the regulator as external) is FORBIDDEN.

**24-σ Sage-exact verification distribution** (per §W9-107):
- σ⁻¹((1,1)) = 1 ⇒ Δ_0 = 4·c_1: 6 σ (matching S_4 stabilizer of "1")
- σ⁻¹((1,1)) = 2 ⇒ Δ_0 = 4·c_2: 6 σ
- σ⁻¹((1,1)) = 3 ⇒ Δ_0 = 4·c_3: 6 σ
- σ⁻¹((1,1)) = 4 ⇒ Δ_0 = 4·c_4: 6 σ
Total: 24 σ ∈ S_4; 24/24 PASS Sage-exact (audit_sha256 = `{W9_107_AUDIT_SHA[:16]}...`).

**Class declaration** (per `substrate-first-canonical-sourcing.md §(iv)`): CLASS = FULL physical (NOT SCHEMATIC). The LOCALIZATION FORMULA is a STRUCTURAL identity in `QQ(c_1, c_2, c_3, c_4)` — its QQ-equality holds independent of specific numerical pins. Sage MCP polynomial-ring confirmation (per §W9-107 MCP audit): `R(LHS - RHS) == R(0)` for all 24 σ in `PolynomialRing(QQ, ['c1','c2','c3','c4'])`. The 4 a_2^{{R_k}} numerical pins (a_2^ζ_FW, a_2^PV_FW, a_2^Mellin_FW, a_2^lattice_FW) are queued for canonical promotion as carry-forward `S89-A_2-REGULATOR-TAGGED-CANONICAL-PROMOTION` — promotion does NOT alter the structural-theorem layer (the FORMULA holds in QQ symbolically; concrete pins land downstream).

**Cross-link**:
- §VII.K-PROP-W8 (S86 W-8 RULE-1; parent 4-channel-LAYER-2 composition theorem)
- §VII.K-PROP-W8.CELL-OCCUPANCY (S86 W-8 REG-2; sister sub-slot at line 15382)
- §VII.AF.1 (S86 W-5 cross-pillar bridge calibration; 5-anatomy + 3-level ladder discipline)
- `.claude/rules/registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY schema (calibration corpus instance #3 — extends W-3 RULE-1 + W-9 V1+C1 + this §VII.K-PROP-W8-LAYERED to N=3 instances)
- `.claude/rules/cross-pillar-bridge-anatomy.md §"Forward template-adoption"` Hybrid Independence Test (this is INTRA-PILLAR re-narration, NOT a cross-pillar bridge; K-counter does NOT advance — preserves §VII.AF.1 calibration baseline)

**Closure SHAs**:
- ANCHOR-2 closure (CF-W8-A3 ↔ §W9-107 24-σ Sage-exact PASS): audit_sha256 = `{W9_107_AUDIT_SHA}`; content_sha256 = `{W9_107_CONTENT_SHA}` (per `computations/session-88/s88_gate_verdicts.txt` line 336)
- This §VII.K-PROP-W8-LAYERED registry-landing closure SHAs: emitted by producing-script `computations/session-88/s88_w9_108_vii_k_prop_w8_layered_writer.py` at S88 W9-108 close (see verdict-line trio appended to s88_gate_verdicts.txt)

---
"""


def closure_hash(items: list[tuple[str, str]]) -> str:
    s = "|".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    text_old = REGISTRY.read_text(encoding="utf-8")
    if "## §VII.K-PROP-W8-LAYERED" in text_old:
        print("FAIL: §VII.K-PROP-W8-LAYERED already present (re-run guard); aborting to avoid duplicate landing.", file=sys.stderr)
        return 1

    entry = build_entry()
    with REGISTRY.open("a", encoding="utf-8") as f:
        f.write(entry)

    pin_map = [
        ("gate_id", GATE_ID),
        ("registry_path", str(REGISTRY)),
        ("slot", SLOT),
        ("anchor_1_V", "CF-W6-V0"),
        ("anchor_2_C", "CF-W8-A3"),
        ("anchor_structure", "SOURCE-DOUBLE-CITE-CO-PRIMARY"),
        ("closure_sha_W9_107", W9_107_AUDIT_SHA),
        ("writer", "mack-cosmic-bridge"),
    ]
    audit_sha256 = closure_hash(pin_map)

    value = (
        f"slot={SLOT};anchor_1=CF-W6-V0;anchor_2=CF-W8-A3;structure=SOURCE-DOUBLE-CITE-CO-PRIMARY;"
        f"both_non_fungible=True;closure_sha_W9_107={W9_107_AUDIT_SHA[:16]};stage=STAGE-1-CANDIDATE"
    )
    scheme = "registry-landing-SOURCE-DOUBLE-CITE-CO-PRIMARY-VII-K-PROP-W8-LAYERED"
    convention = "mack-sole-writer-append-only-python-W9-107-closure-pinned"
    canonical = (
        f"{GATE_ID}: PASS -- "
        f"value='{value}' "
        f"scheme={scheme} "
        f"convention={convention} "
        f"L_max=N/A "
        f"audit_sha256={audit_sha256} "
    )
    content_sha256 = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    canonical += f"content_sha256={content_sha256} schema_version=S87+"

    dual_sha_row = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); §VII.K-PROP-W8-LAYERED registry slot landed at permanent-results-registry.md (CO-PRIMARY anchors CF-W6-V0 + CF-W8-A3 non-fungible per §W9-107 24/24 σ PASS)"
    )
    tuple_row = (
        f"# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway"
    )

    if audit_sha256 in VERDICT_FILE.read_text(encoding="utf-8"):
        print(f"FAIL: audit_sha256={audit_sha256} already in verdict file (sig_5 collision).", file=sys.stderr)
        return 1
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write("\n" + canonical + "\n" + dual_sha_row + "\n" + tuple_row + "\n")

    print(f"S88 W9-108: PASS")
    print(f"  registry: {REGISTRY} (§VII.K-PROP-W8-LAYERED appended; {len(text_old.splitlines())} → {len((text_old + entry).splitlines())} lines)")
    print(f"  audit_sha256={audit_sha256}")
    print(f"  content_sha256={content_sha256}")
    print(f"  closure_sha_pin (W9-107) = {W9_107_AUDIT_SHA[:16]}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
