"""S88-A0-M2-BICONDITIONAL-SPLIT-REGISTRY-LANDING (W4a-17).

3-row split registry-landing of the W4a-16 A0/M2 backward rescue theorem at
permanent-results-registry.md §VII.W-3.{ALGEBRAIC, SUBSTRATE, LAB} — REROUTED
from plan-pinned §VII.W-2 (occupied by S87 W1a-5 cross-program biconditional)
to §VII.W-3 per plan §5 line 240 explicit fallback + epistemic-discipline.md
§"Registry-Write Hygiene" item 3.

Composite verdict: FAIL-with-remediation per item 3 of §"Registry-Write Hygiene":
"When a planned slot is occupied at runtime, rerouting to next-free-letter is
permitted (S84 W2a-11 §VII.M→§VII.N precedent), but the verdict line MUST emit
FAIL-with-remediation (not PASS) so the rerouting is visible in the audit trail."
The 3 rows themselves land structurally complete; the FAIL flag captures the slot
reroute, not a content defect. .ALGEBRAIC + .SUBSTRATE land STAGE-3-PERMANENT
(W4a-16 PASSed); .LAB lands STAGE-1-CANDIDATE per joint-theorem-promotion.md
4-stage pathway.

K-counter advancement (cross-pillar-bridge-anatomy.md §"Forward template-adoption"):
The W4a-17 .LAB row is calibration corpus instance #3 (FWD-C3 family; substrate
cocycle ratio bridge map). K=2 → K=3 advance triggers SUGGESTION → MANDATORY
promotion per the rule's §"Promotion event": "an orchestrator landing the third
bridge writes the promotion edit in the same dispatch as the registry entry".

Pre-reg per session-88-plan-w4a.md §W4a-17 (lines 208-336).
Gate ID: S88-A0-M2-BICONDITIONAL-SPLIT-REGISTRY-LANDING
Trigger: [VERIFY]
Schema: dual-SHA + 3-tuple annotation (S87 schema-v2).
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Project root + canonical_constants
# ---------------------------------------------------------------------------
ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import *  # noqa: F401, F403  # (local) Tier0 canonical-constants

# ---------------------------------------------------------------------------
# Pins
# ---------------------------------------------------------------------------
GATE_ID = "S88-A0-M2-BICONDITIONAL-SPLIT-REGISTRY-LANDING"
SCHEME = "vii-w-3-three-row-split-landing"
CONVENTION = "algebraic-substrate-lab-with-stage-1-candidate-on-lab-rerouted-from-vii-w-2"
L_MAX_TAG = "N/A"  # (local) registry-write gate; no L_max
SCHEMA_VERSION = "S87+"

JSON_PATH = ROOT / "computations" / "s88_w4a_split_registry_writer.json"
VERDICTS_PATH = ROOT / "computations" / "_shared" / "s88_gate_verdicts.txt"
SCRIPT_PATH = ROOT / "computations" / "s88_w4a_split_registry_writer.py"
PLAN_PATH = ROOT / "sessions" / "session-plan" / "session-88-plan-w4a.md"
W4A_16_VERDICT_PATH = ROOT / "computations" / "_shared" / "s88_gate_verdicts.txt"
W4A_16_NPZ_PATH = ROOT / "computations" / "s88_w4a_a0_m2_backward_rescue_theorem.npz"
W4A_16_JSON_PATH = ROOT / "computations" / "s88_w4a_a0_m2_backward_rescue_theorem.json"
WORKSHOP_PATH = ROOT / "sessions" / "session-87" / "workshops" / "s87-a0-r-protection-m2-biconditional.md"
W5_PAIRING_NPZ = ROOT / "computations" / "session-86" / "s86_w5_r_universal_pairing.npz"  # may not exist; informational
REGISTRY_PATH = ROOT / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
CROSS_PILLAR_PATH = ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"

# Slot reroute pins
SLOT_PLANNED = "§VII.W-2"  # plan-pinned; OCCUPIED at runtime by S87 W1a-5
SLOT_LANDED = "§VII.W-3"   # next-free per plan §5 line 240 fallback
SLOT_REROUTE_FIRED = True  # forces FAIL-with-remediation


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def sha256_hex(data) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256_hex(path.read_bytes())


def closure_hash(pin_map: dict) -> str:
    canonical = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return sha256_hex(canonical)


def extract_w4a_16_verdict_audit_sha(verdict_text: str) -> str:
    """Extract audit_sha256 from the W4a-16 verdict line."""
    for line in verdict_text.splitlines():
        if line.startswith("S88-A0-M2-BACKWARD-RESCUE-CHARACTERIZATION") and "PASS" in line:
            for part in line.split():
                if part.startswith("audit_sha256="):
                    return part.split("=", 1)[1]
    return ""


def extract_w4a_16_verdict_content_sha(verdict_text: str) -> str:
    for line in verdict_text.splitlines():
        if line.startswith("S88-A0-M2-BACKWARD-RESCUE-CHARACTERIZATION") and "PASS" in line:
            for part in line.split():
                if part.startswith("content_sha256="):
                    return part.split("=", 1)[1]
    return ""


def extract_plan_block_sha(plan_text: str, gate_label: str) -> str:
    """Extract SHA-256 of the gate block in the plan file matching '## §<gate_label>.'."""
    lines = plan_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith(f"## §{gate_label}.") or line.startswith(f"## §{gate_label} "):
            start = i
            break
    if start is None:
        return "block-not-found"
    # End at next ## section or EOF
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## ") and not lines[j].startswith(f"## §{gate_label}"):
            end = j
            break
    block_text = "\n".join(lines[start:end])
    return sha256_hex(block_text)


# ---------------------------------------------------------------------------
# Slot-occupancy verification at runtime
# ---------------------------------------------------------------------------
def scan_slot_occupancy(registry_text: str, slot_label: str) -> bool:
    """Scan all header levels (## ### ####) for slot_label occupancy."""
    pat_2 = f"## {slot_label}"
    pat_3 = f"### {slot_label}"
    pat_4 = f"#### {slot_label}"
    for line in registry_text.splitlines():
        if line.startswith(pat_2) or line.startswith(pat_3) or line.startswith(pat_4):
            return True
    return False


# ---------------------------------------------------------------------------
# 3 §VII.W-3 sub-section content blocks
# ---------------------------------------------------------------------------
def build_vii_w3_blocks(w4a_16_audit_sha: str, w4a_16_content_sha: str,
                        workshop_sha: str, today: str) -> dict:
    """Build the 3 sub-section markdown blocks for §VII.W-3.{ALG, SUB, LAB}."""

    alg_block = f"""

---


## §VII.W-3.ALGEBRAIC — Wedderburn-Artin Frobenius Rescue Class Theorem (S88 W4a-17 — gen-physicist + connes-ncg-theorist co-authored, {today}) STAGE-3-PERMANENT

**Status**: STAGE-3-PERMANENT (W4a-16 theorem-verifier PASSed; this row is the algebraic-IS-content registry entry).

**Slot-reroute note**: §VII.W-2 OCCUPIED at landing time (S87 W1a-5 A0-R-Protection-Failure ⟺ M2-Axiom-Failure Cross-Program Unification). Per plan §W4a-17 §5 line 240 explicit fallback to §VII.W-3 + `epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race" item 3, the math content lands at §VII.W-3; only the slot identity diverged from plan. FAIL-with-remediation emitted in verdict line per protocol.

**Authorship**: gen-physicist PRIMARY (theorem-proof verifier in S88 W4a-16 /rclab-solo); connes-ncg-theorist CO-AUTHOR (NCG-axiomatic substitution chain Steps 4-7 + KO-dim=6 sufficiency; workshop precedent S87 W1a-5 §R3 Prompt-3 lines 501-553).

**Theorem statement** (pure algebraic IS-content; no laboratory observable):

> Let A be a finite-dimensional unital associative real *-algebra and χ : A → M_2(ℂ) a unital *-homomorphism (the inheritance morphism). Then A satisfies A0 (KO-dim=6 + chirality-fiber consistency) ∧ M2 (order-one [[D, a], b°] = 0) iff in the Wedderburn-Artin (1907) block decomposition A = ⊕_i M_{{n_i}}(D_i) with D_i ∈ {{ℝ, ℂ, ℍ}} (Frobenius 1877), every block i satisfies EITHER:
>
> - **(i) Frobenius division-algebra block**: n_i = 1 (block is just D_i ∈ {{ℝ, ℂ, ℍ}}), OR
> - **(ii) χ-killed matrix block**: n_i ≥ 2 AND χ vanishes on M_{{n_i}}(D_i).

**Substitution chain** (Steps 1-8 + Conclusion; verbatim from plan §W4a-16 §5 + workshop S87 W1a-5 §R3 Prompt-3 lines 514-541):

```
Step 1 (Wedderburn-Artin 1907): A = ⊕_i M_{{n_i}}(D_i), D_i finite-dim div-alg over ℝ.
Step 2 (Frobenius 1877): D_i ∈ {{ℝ, ℂ, ℍ}}.
Step 3 (compose 1+2): A = ⊕_i M_{{n_i}}(D_i) with D_i ∈ {{ℝ, ℂ, ℍ}}.
Step 4 (A0): γ_F scalar per block (automatic for n=1; forced for n≥2 by matrix-unit commutation).
Step 5 (M2): [[D, a], b°] = 0 reduces to χ-image sub-*-algebra closure constraint.
Step 6 (n=1 blocks): χ embeds D_i into M_2(ℂ); image closed under self-commutators; M2 holds.
Step 7 (n≥2 blocks): non-trivial χ-image generates non-abelian sub-*-algebra of M_2(ℂ);
        commutators with opposite ≠ 0; M2 FAILS unless χ kills the block.
Step 8 (combine): A satisfies A0 ∧ M2 iff every block is (i) n=1 division OR (ii) n≥2 χ-killed.
Conclusion: Wedderburn-Artin Frobenius Rescue Class characterizes A0 ∧ M2 satisfiers up to χ-kernel choice.
```

**4-example verification table** (W4a-16 Sage-compatible QQ-exact arithmetic; bit-deterministic):

| Algebra | Part | Wedderburn-Artin blocks | Rescue clauses | A0 | M2 | Commutator residual (QQ) | Match |
|:--------|:-----|:------------------------|:---------------|:---|:---|:-------------------------|:-----|
| ℝ ⊕ ℂ | A.1 | (ℝ, n=1) + (ℂ, n=1) | i + i | PASS | PASS | 0 | ✓ |
| ℂ ⊕ M_2(ℂ)_χ-killed | A.2 | (ℂ, n=1) + (ℂ, n=2, χ=0) | i + ii | PASS | PASS | 0 | ✓ |
| ℍ ⊕ ℍ | A.3 | (ℍ, n=1) + (ℍ, n=1) | i + i | PASS | PASS | 0 | ✓ |
| ℝ ⊕ M_2(ℝ)_id-χ | B.4 | (ℝ, n=1) + (M_2(ℝ), n=2, χ=id) | i + NEITHER | PASS | **FAIL** | **2** | ✓ |

**Direction of explanation** (substrate IS the algebraic structural class; no IN-content):

Wedderburn-Artin + Frobenius (purely algebraic IS-content) → Rescue class characterization
   (substrate-internal structural theorem) → A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) (substrate IS instance,
   §VII.W-3.SUBSTRATE) → χ : A_F → M_2(ℂ) inheritance morphism → BdG laboratory measurement
   IN M_2(ℂ) image (§VII.W-3.LAB).

**Cross-link**: §VII.W-3.SUBSTRATE (substrate instance) + §VII.W-3.LAB (laboratory image bridge) +
§VII.W-2 (S87 W1a-5 BACKWARD biconditional with synthetic 2-eigenvalue toy; structurally
related FAIL-with-remediation precedent that motivated the rescue characterization).

**Audit SHAs** (this entry):
- Plan SHA: pinned at §W4a-16 + §W4a-17 plan blocks
- W4a-16 audit_sha256: `{w4a_16_audit_sha}`
- W4a-16 content_sha256: `{w4a_16_content_sha}`
- Workshop precedent SHA (S87 W1a-5 R3 Prompt-3): `{workshop_sha}`

**Producing artifacts**:
- W4a-16 script: `computations/s88_w4a_a0_m2_backward_rescue_theorem.py`
- W4a-16 data: `computations/s88_w4a_a0_m2_backward_rescue_theorem.npz` + `.json`
- W4a-16 plot: `computations/s88_w4a_a0_m2_backward_rescue_theorem.png`
- W4a-17 split-writer: `computations/s88_w4a_split_registry_writer.py` + `.json`

"""

    sub_block = f"""

---


## §VII.W-3.SUBSTRATE — A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) Realizes the Wedderburn-Artin Frobenius Rescue Class (S88 W4a-17 — connes-ncg-theorist primary, {today}) STAGE-3-PERMANENT

**Status**: STAGE-3-PERMANENT (W4a-16 substrate match Part C PASS bit-exact; S84 W8-87b SINGLE-INSTANCE substrate uniqueness already permanent; this row LIFTS substrate uniqueness from a single-instance fact to structural class membership).

**Slot-reroute note**: identical to §VII.W-3.ALGEBRAIC (parent §VII.W-2 occupied; rerouted to §VII.W-3).

**Authorship**: connes-ncg-theorist PRIMARY (NCG-axiomatic substrate uniqueness audit; A_F SINGLETON theorem provenance from S84 W8-87b); gen-physicist + connes-ncg-theorist CO-AUTHORS via W4a-16 verifier execution.

**Substrate instance** (substrate IS the spectral triple's algebra; Pillar III observable):

> The framework's finite-dimensional spectral-triple algebra `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (with KO-dim=6, observed SM gauge content, A0 ∧ M2 simultaneously satisfied per S84 W8-87b SINGLETON theorem) realizes the §VII.W-3.ALGEBRAIC rescue class as:
>
> - **ℂ block**: n=1 Frobenius division algebra → clause **(i)**
> - **ℍ block**: n=1 Frobenius division algebra → clause **(i)**
> - **M_3(ℂ) block**: n=3 matrix block; under inheritance morphism χ : A_F → M_2(ℂ) (BdG sector child; S88 W3b plan canonical `χ_inheritance_morphism = "M3C_to_zero_C_and_H_to_canonical_M2C"`), χ vanishes on M_3(ℂ) → clause **(ii)**

All 3 blocks satisfy the rescue clause; A_F is a member of the Wedderburn-Artin Frobenius Rescue Class. The substrate's algebra is one specific instance of the rescue class, NOT a uniquely-positioned structurally-special object.

**KO-dim=6 + observed SM gauge content + A0 + M2 simultaneously satisfied**: consistent with S84 W8-87b SINGLETON theorem; the W4a-17 promotion lifts substrate uniqueness from a SINGLE-INSTANCE empirical fact to STRUCTURAL CLASS MEMBERSHIP within the rescue class characterized at §VII.W-3.ALGEBRAIC.

**Direction of explanation**: substrate IS A_F (Pillar III instance); no IN-content. The substrate's algebra is structurally determined by its OWN axioms (A0 + M2 + KO-dim=6 + SM gauge content); the BdG image M_2(ℂ) at §VII.W-3.LAB is downstream of the substrate's structural uniqueness, NOT upstream. Container-thinking inversion ("the BdG sector M_2(ℂ) constrains A_F to be ℂ ⊕ ℍ ⊕ M_3(ℂ)") is FORBIDDEN per `phononic-framing.md` §"IS Space, Not IN Space".

**Cross-link**: §VII.W-3.ALGEBRAIC (algebraic class theorem) + §VII.W-3.LAB (BdG laboratory image) +
§VII.K (KO-dim=6 substrate uniqueness; S84 W8-87b parent entry).

**Audit SHAs** (inherited from §VII.W-3.ALGEBRAIC + adds S84 W8-87b reference):
- W4a-16 audit_sha256: `{w4a_16_audit_sha}`
- W4a-16 content_sha256: `{w4a_16_content_sha}`
- Workshop precedent SHA: `{workshop_sha}`
- S84 W8-87b SINGLETON (referenced; canonical `permanent-results-registry.md §VII.K`)

"""

    lab_block = f"""

---


## §VII.W-3.LAB — Cross-Pillar Bridge: Substrate Cocycle-Ratio Preservation Under χ Inheritance Morphism into 3He-B + 3He-A BdG Laboratory Observables (S88 W4a-17 — volovik-superfluid-universe-theorist + connes-ncg-theorist + mack-cosmic-bridge co-authored, {today}) STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway

**Status**: STAGE-1-CANDIDATE — Stage-2 two-agent cross-axis independent-verify deferred to multi-year experimental cycle (Lancaster MCT-3 + RHUL/Aalto LTL 2027-2030 horizon).

**Slot-reroute note**: identical to §VII.W-3.ALGEBRAIC (parent §VII.W-2 occupied; rerouted to §VII.W-3).

**Authorship**:
- volovik-superfluid-universe-theorist PRIMARY (substrate cocycle-pair ([φ_67], [φ_88]) + ratio 7.324992; W-5 calibration corpus instance #1)
- connes-ncg-theorist CO-AUTHOR (inheritance morphism χ : A_F → M_2(ℂ); rescue characterization theorem per §VII.W-3.ALGEBRAIC)
- mack-cosmic-bridge CO-AUTHOR (observational discrimination map; falsifier-master-inventory rows #47-#54b cross-link)

**Cross-pillar bridge anatomy** (5-element IS-not-IN per `cross-pillar-bridge-anatomy.md` §"Five anatomy elements"):

1. **Substrate-IS observable**: A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) finite-spectral-triple algebra (per §VII.W-3.SUBSTRATE) + substrate cocycle pair (φ_67, φ_88) with **ratio 7.324992** (Sage-exact; canonical_constants.py:237 `substrate_cocycle_ratio_67_88`; S86 W-5 R2-B Convergence #3 + R2-A EMERGENCE #2). The substrate IS the rank-2 cocycle pair in ker(ι_*) — these are intrinsic structural numbers, NOT BdG band-structure derivatives.

2. **Laboratory-IN observable**: 3He-B vortex-core Caroli-Matricon ladder asymmetry (W11-C5; Lancaster MCT-3 / Helsinki ROTA cells) AND 3He-A µSR chirality discrimination (W11-C6; RHUL/Aalto LTL); plus the supporting F2/F3/F4 channels and decisive triplet F1+F2+F5 + ratio Gate-2 cohomology-asymmetry test, all listed at `falsifier-master-inventory.md` rows #47-#54b (S87 W5-2 + W5-3 LANDED via `s87_w5_falsifier_inventory_consolidation_writer.py`). Lab measures these IN the helium cryostat container under (p, T) sweep.

3. **Bridge map**: inheritance morphism `χ : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)` (M_3(ℂ) → 0; BDI → BdG sector child) ∘ (Δ_B/Δ_A)^p lab-conversion factor. Cancellation theorem (S86 W-5 DONE-5; 0.0e+00 residual at machine precision) preserves substrate-derived ratio ‖φ_67‖/‖φ_88‖ = 7.324992 INTACT under common-exponent (Δ_B/Δ_A)^p rescaling. The bridge map is the same as FWD-C3 candidate per cross-pillar-bridge-anatomy.md §"Three forward bridge candidates".

4. **Algebraic envelope (Level 2)**: cohomology-asymmetry test ratio preservation **7.3250 ± 0.1%** (S86 W-5 Gate-2 pre-registered band; structural-exact form, NOT L^{{-α}} convergence — replaces L_max-dependent envelope for inheritance-morphism class per `cross-pillar-bridge-anatomy.md` §"Three forward bridge candidates" FWD-C3 envelope spec).

5. **Empirical anchor (Level 3)**: S88+ Lancaster MCT-3 vortex-core spectroscopy + RHUL/Aalto LTL µSR run delivering NULL on F1+F2+F5 + ratio 7.3250 ± 0.1% on any non-NULL detection (4-gate falsifier protocol per `inheritance-falsifier-protocol.md` §"Four-Gate Structure"). MULTI-YEAR experimental cycle blocking Stage-3 promotion. Pre-registered falsifier rows at `sessions/framework/registry/falsifier-master-inventory.md` #47-#54b.

**3-level structural-confidence ladder** (per `cross-pillar-bridge-anatomy.md` §"Three-Level Structural-Confidence Ladder"):

- **Level 1** (substrate-IS structural identity): rescue characterization theorem (§VII.W-3.ALGEBRAIC) + cohomology-class identity ‖φ_67‖/‖φ_88‖ = 7.324992 (Sage-exact, Connes-Karoubi pairing on Jensen-deformed band-0 projector at τ_fold=0.190); regulator-invariant; L-independent.
- **Level 2** (algebraic envelope): structural-exact preservation 7.3250 ± 0.1% under (Δ_B/Δ_A)^p cancellation theorem; pre-registered band; replaces L_max-dependent algebraic bound for the inheritance-morphism class.
- **Level 3** (empirical anchor): DEFERRED to multi-year experimental cycle; Lancaster MCT-3 + RHUL/Aalto LTL falsifier campaign 2027-2030; STAGE-1-CANDIDATE pending until Stage-2 cross-axis verify + Stage-3 lab measurement.

**Inheritance kernel rank**: rank(ker ι_*) = 2 (φ_67 chiral pair + φ_88 Cartan hypercharge) — directly invokes `inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)" rank-2 case.

**Direction of explanation** (substrate IS the substrate-IS observable; lab measures the laboratory-IN observable):

Substrate (Pillars III + IV) IS the cocycle pair (φ_67, φ_88) and the rescue-class
membership of A_F → χ inheritance morphism (cancellation theorem preserves ratio INTACT)
→ Laboratory (Pillar V) measures BdG observable IN helium cryostat → Detector signature:
NULL on F1+F2+F5 + ratio 7.3250 ± 0.1% on any non-NULL detection.

Container-thinking violation FORBIDDEN: "the lab measures the substrate AT the helium temperature/pressure point" — the lab measures BdG observables IN the cryostat container; the substrate's prediction is structurally INDEPENDENT of (Δ_B/Δ_A)^p exponents under the cancellation theorem.

**Stage-2 cross-axis independent-verify pre-registration** (per joint-theorem-promotion.md):
- Axis A: connes-ncg-theorist on NCG-axiomatic axis (KO-dim=6, A0 ∧ M2 axiom verification on substrate algebra, χ kernel structure)
- Axis B: lizzi-spectral-functional-theorist on spectral-functional axis (cocycle ratio under regulator class change; HP^1 cohomology stability)
- Both dispatched WITHOUT prior workshop context; joint clauses PASS-AND across both verdicts
- Gate ID (forward): `S88-OR-LATER-VII-W-3-LAB-INDEPENDENT-VERIFY`

**Cross-link**:
- §VII.W-3.ALGEBRAIC (algebraic class theorem)
- §VII.W-3.SUBSTRATE (substrate instance Pillar III)
- §VII.AF.1 (S86 W-5 Pillar III ↔ Pillar IV bridge; instance #1)
- §VII.AJ (S87 W11-5 Pillar IV ↔ Pillar V REGISTRY-FAIL; instance #2)
- `falsifier-master-inventory.md` rows #47-#54b (laboratory-IN falsifier rows)
- `cross-pillar-bridge-anatomy.md` §"Forward template-adoption" calibration corpus instance #3 (this entry)
- `inheritance-falsifier-protocol.md` §"Generalization beyond 3He-B (W-5 Q8)" rank-2 generalization

**K-counter advancement**: this row is calibration corpus instance **#3** (FWD-C3 family extended). Per `cross-pillar-bridge-anatomy.md` §"Promotion event": "an orchestrator landing the third bridge writes the promotion edit in the same dispatch as the registry entry". K=2 → K=3 advance triggered; SUGGESTION → MANDATORY status promotion landed in same dispatch (cross-pillar-bridge-anatomy.md edit per W4a-17 split-writer).

**Audit SHAs**:
- W4a-16 audit_sha256: `{w4a_16_audit_sha}`
- W4a-16 content_sha256: `{w4a_16_content_sha}`
- Workshop precedent SHA (S87 W1a-5 R3 Prompt-3): `{workshop_sha}`
- substrate_cocycle_ratio_67_88 = 7.324992 (canonical_constants.py:237; S86 W-5 R2-B Convergence #3)

"""

    return {
        "alg_block": alg_block,
        "sub_block": sub_block,
        "lab_block": lab_block,
    }


# ---------------------------------------------------------------------------
# §VII slot-allocation table rows
# ---------------------------------------------------------------------------
def build_slot_table_rows(today: str) -> list[str]:
    return [
        f"| §VII.W-3.ALGEBRAIC | THM | Wedderburn-Artin Frobenius Rescue Class Theorem (S88 W4a-17 — gen-physicist + connes-ncg-theorist co-authored, {today}; rerouted from §VII.W-2 plan-pin per epistemic-discipline.md §Registry-Write Hygiene item 3) | gen-physicist | {today} |",
        f"| §VII.W-3.SUBSTRATE | THM | A_F = C ⊕ H ⊕ M_3(C) Realizes the Wedderburn-Artin Frobenius Rescue Class (S88 W4a-17 — connes-ncg-theorist primary, {today}; STAGE-3-PERMANENT lifting S84 W8-87b SINGLE-INSTANCE to structural class membership) | connes-ncg-theorist | {today} |",
        f"| §VII.W-3.LAB | THM | Cross-Pillar Bridge: Substrate Cocycle-Ratio Preservation Under χ Inheritance Morphism into 3He-B + 3He-A BdG Laboratory Observables (S88 W4a-17 — volovik PRIMARY + connes + mack co-authored, {today}; STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway; cross-pillar-bridge-anatomy.md K-counter instance #3 → K=3 MANDATORY) | volovik-superfluid-universe-theorist | {today} |",
    ]


# ---------------------------------------------------------------------------
# Methodology-wave-allowlist row
# ---------------------------------------------------------------------------
def build_allowlist_row(plan_block_sha: str) -> str:
    return (
        "| W4a-17 | S88 | "
        "S88-A0-M2-BICONDITIONAL-SPLIT-REGISTRY-LANDING (3-row split landing of A0/M2 backward "
        "rescue theorem at permanent-results-registry §VII.W-3.{ALGEBRAIC, SUBSTRATE, LAB}; "
        "rerouted from plan-pinned §VII.W-2 occupied by S87 W1a-5 per epistemic-discipline.md "
        "§Registry-Write Hygiene item 3 + plan §5 line 240 fallback to §VII.W-3; "
        ".ALGEBRAIC + .SUBSTRATE STAGE-3-PERMANENT iff W4a-16 PASS [PASSED]; "
        ".LAB STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway; "
        "K-counter K=2→K=3 + SUGGESTION→MANDATORY promotion of cross-pillar-bridge-anatomy.md "
        "§Forward template-adoption; "
        "FAIL-with-remediation verdict-line composite; "
        "orchestrator-direct-write per wave-classification.md §Dispatch consequences) "
        f"| {plan_block_sha} |"
    )


# ---------------------------------------------------------------------------
# Cross-pillar-bridge-anatomy.md K-counter K=2 → K=3 promotion
# ---------------------------------------------------------------------------
def cross_pillar_k_counter_promote(today: str) -> tuple[str, str]:
    """Edit cross-pillar-bridge-anatomy.md to advance K=2 → K=3 + MANDATORY status.
    Returns (old_text, new_text) for the targeted block."""

    old_status_line = "### Status: SUGGESTION (NOT MANDATORY) at K=2"
    new_status_line = f"### Status: MANDATORY at K=3 (promoted from SUGGESTION at S88 W4a-17 close, {today})"

    old_table = (
        "| 1 | S86 W-5 (volovik PRIMARY + connes CO-AUTHOR) | Pillar III ↔ Pillar IV  (HP^1 cohomology ↔ Peotta-Törmä quantum-metric trace) | LANDED §VII.AF.1 (S87 W5-1) |\n"
        "| 2 | S87 W11-5 (volovik PRIMARY) | Pillar IV ↔ Pillar V (substrate spectral-excess ↔ 3He-B BdG-undoubled excess at polycritical pressure) | REGISTRY-FAIL §VII.AJ NOT eligible per §\"Registry-PASS criterion\" (Level-3 1.029 violates Level-2 0.05 by ~21×); calibration corpus K=1→2 |\n"
        "| 3 | — | — | (awaits future high-density workshop) |"
    )
    new_table = (
        "| 1 | S86 W-5 (volovik PRIMARY + connes CO-AUTHOR) | Pillar III ↔ Pillar IV  (HP^1 cohomology ↔ Peotta-Törmä quantum-metric trace) | LANDED §VII.AF.1 (S87 W5-1) |\n"
        "| 2 | S87 W11-5 (volovik PRIMARY) | Pillar IV ↔ Pillar V (substrate spectral-excess ↔ 3He-B BdG-undoubled excess at polycritical pressure) | REGISTRY-FAIL §VII.AJ NOT eligible per §\"Registry-PASS criterion\" (Level-3 1.029 violates Level-2 0.05 by ~21×); calibration corpus K=1→2 |\n"
        f"| 3 | S88 W4a-17 (volovik PRIMARY + connes + mack co-authored) | Pillar IV ↔ Pillar V (substrate cocycle ratio ‖φ_67‖/‖φ_88‖=7.324992 preservation under χ inheritance morphism ↔ 3He-B + 3He-A laboratory falsifier rows #47-#54b) | LANDED §VII.W-3.LAB (S88 W4a-17, {today}) STAGE-1-CANDIDATE per joint-theorem-promotion.md; K-counter K=2→K=3 advance |"
    )

    old_threshold = "K = 2  <  K_promotion = 3  ⇒  status = **SUGGESTION** (NOT MANDATORY).  Promotion event triggers when a 3rd calibration instance lands; until then, future cross-pillar bridge candidates SHOULD adopt the 5-anatomy + 3-level discipline as a design SUGGESTION, not yet a structural REQUIREMENT."
    new_threshold = f"K = 3 = K_promotion ⇒ status = **MANDATORY** (promoted at S88 W4a-17 close, {today}; the 3rd calibration instance landed at §VII.W-3.LAB triggers MANDATORY status per §\"Promotion event\"). Future cross-pillar bridge candidates MUST adopt the 5-anatomy + 3-level discipline; SUGGESTION → MANDATORY promotion is FORWARD-LOOKING from this date onward."

    return (old_status_line, new_status_line, old_table, new_table, old_threshold, new_threshold)


# ---------------------------------------------------------------------------
# Verdict-line emission (per gate-verdicts.md S87+ schema-v2)
# ---------------------------------------------------------------------------
def emit_verdict_line(composite: str, value_str: str, content_str: str,
                      sign_v: str, mag_v: str, regime_v: str,
                      plan_sha: str, workshop_sha: str,
                      w4a_16_audit_sha: str, w4a_16_content_sha: str,
                      plan_block_sha: str) -> tuple[str, str]:
    pin_map = {
        "GATE_ID": GATE_ID,
        "SCHEME": SCHEME,
        "CONVENTION": CONVENTION,
        "L_MAX_TAG": L_MAX_TAG,
        "SCHEMA_VERSION": SCHEMA_VERSION,
        "PLAN_SHA": plan_sha,
        "WORKSHOP_SHA": workshop_sha,
        "W4A_16_AUDIT_SHA": w4a_16_audit_sha,
        "W4A_16_CONTENT_SHA": w4a_16_content_sha,
        "PLAN_BLOCK_SHA": plan_block_sha,
        "SLOT_PLANNED": SLOT_PLANNED,
        "SLOT_LANDED": SLOT_LANDED,
        "SLOT_REROUTE_FIRED": str(SLOT_REROUTE_FIRED),
        "substrate_cocycle_ratio_67_88": "7.324992",
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha256_hex(content_str)

    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"slot_target_planned={SLOT_PLANNED} slot_landed={SLOT_LANDED} "
        f"reroute_fired={'true' if SLOT_REROUTE_FIRED else 'false'} "
        f"reroute_reason='{SLOT_PLANNED}_occupied_by_S87_W1a-5_cross_program_biconditional' "
        f"reroute_protocol='S84-W2a-11-next-free-letter+plan_5_line_240_fallback'"
    )
    annotation = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )
    with VERDICTS_PATH.open("a", encoding="utf-8") as f:
        f.write(canonical + "\n")
        f.write(dual_sha_companion + "\n")
        f.write(annotation + "\n")
    return audit_sha, content_sha


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # 1. Verify prerequisite landings
    plan_text = PLAN_PATH.read_text(encoding="utf-8")
    workshop_text = WORKSHOP_PATH.read_text(encoding="utf-8")
    plan_sha = sha256_hex(plan_text)
    workshop_sha = sha256_hex(workshop_text)

    verdict_text = W4A_16_VERDICT_PATH.read_text(encoding="utf-8")
    w4a_16_audit_sha = extract_w4a_16_verdict_audit_sha(verdict_text)
    w4a_16_content_sha = extract_w4a_16_verdict_content_sha(verdict_text)
    if not w4a_16_audit_sha:
        print("ERROR: W4a-16 PASS verdict not found in s88_gate_verdicts.txt; cannot proceed.")
        return 2

    # 2. Verify slot occupancy (§VII.W-2 should be OCCUPIED; §VII.W-3 should be FREE)
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")
    is_w2_occupied = scan_slot_occupancy(registry_text, "§VII.W-2")
    is_w3_occupied = scan_slot_occupancy(registry_text, "§VII.W-3")
    print(f"§VII.W-2 occupied: {is_w2_occupied}")
    print(f"§VII.W-3 occupied: {is_w3_occupied}")
    if not is_w2_occupied:
        print("WARNING: §VII.W-2 unexpectedly free; reroute may not be needed.")
    if is_w3_occupied:
        print("ERROR: §VII.W-3 occupied; cannot land here without further reroute.")
        return 2

    # 3. Build 3 §VII.W-3 sub-section blocks
    blocks = build_vii_w3_blocks(w4a_16_audit_sha, w4a_16_content_sha,
                                 workshop_sha[:16], today)
    alg_sha = sha256_hex(blocks["alg_block"])
    sub_sha = sha256_hex(blocks["sub_block"])
    lab_sha = sha256_hex(blocks["lab_block"])
    print(f"§VII.W-3.ALGEBRAIC content_sha256: {alg_sha[:16]}…  ({len(blocks['alg_block'])} bytes)")
    print(f"§VII.W-3.SUBSTRATE  content_sha256: {sub_sha[:16]}…  ({len(blocks['sub_block'])} bytes)")
    print(f"§VII.W-3.LAB        content_sha256: {lab_sha[:16]}…  ({len(blocks['lab_block'])} bytes)")

    # 4. Append to permanent-results-registry.md (one-shot append-only)
    full_payload = blocks["alg_block"] + blocks["sub_block"] + blocks["lab_block"]
    with REGISTRY_PATH.open("a", encoding="utf-8") as f:
        f.write(full_payload)
    print(f"Appended to: {REGISTRY_PATH}")

    # 5. Insert §VII slot-allocation table rows
    # Find the slot-allocation table; insert 3 rows just before the next ## section
    slot_rows = build_slot_table_rows(today)
    registry_text_after_append = REGISTRY_PATH.read_text(encoding="utf-8")
    # Find the LAST row in the slot allocation table (before the next major section)
    # Slot table rows look like: "| §VII.<L> | ... |"
    lines = registry_text_after_append.splitlines()
    table_start = None
    table_end = None
    for i, line in enumerate(lines):
        if "## §VII Slot Allocation Table" in line:
            table_start = i
        elif table_start is not None and (line.startswith("## ") or line.startswith("# ")) and i > table_start:
            table_end = i
            break
    if table_start is not None:
        if table_end is None:
            # Find end of contiguous table rows from table_start
            for j in range(table_start, len(lines)):
                if lines[j].startswith("| §VII"):
                    table_end = j + 1
            if table_end is None:
                table_end = len(lines)
        else:
            # Walk back to last contiguous "| §VII" row
            last_row_idx = table_end - 1
            while last_row_idx > table_start and not lines[last_row_idx].startswith("| §VII"):
                last_row_idx -= 1
            table_end = last_row_idx + 1
        # Insert slot_rows after table_end-1 (i.e., before lines[table_end])
        new_lines = lines[:table_end] + slot_rows + lines[table_end:]
        REGISTRY_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print(f"Inserted 3 slot-allocation rows at line {table_end}")
    else:
        print("WARNING: §VII slot-allocation table not found; skipping table-row insert")

    # 6. Append methodology-wave-allowlist row
    plan_block_sha = extract_plan_block_sha(plan_text, "W4a-17")
    print(f"plan-block SHA for W4a-17: {plan_block_sha[:16]}…")
    allowlist_row = build_allowlist_row(plan_block_sha)
    with ALLOWLIST_PATH.open("a", encoding="utf-8") as f:
        f.write(allowlist_row + "\n")
    print(f"Appended allowlist row to: {ALLOWLIST_PATH}")

    # 7. Edit cross-pillar-bridge-anatomy.md K-counter K=2 → K=3 + MANDATORY
    cp_text = CROSS_PILLAR_PATH.read_text(encoding="utf-8")
    promo = cross_pillar_k_counter_promote(today)
    old_status, new_status, old_table, new_table, old_thresh, new_thresh = promo
    if old_status not in cp_text:
        print(f"ERROR: K-counter status line not found verbatim in cross-pillar-bridge-anatomy.md")
        return 2
    cp_text = cp_text.replace(old_status, new_status, 1)
    cp_text = cp_text.replace(old_table, new_table, 1)
    cp_text = cp_text.replace(old_thresh, new_thresh, 1)
    CROSS_PILLAR_PATH.write_text(cp_text, encoding="utf-8")
    print(f"K-counter K=2→K=3 + SUGGESTION→MANDATORY promotion landed in: {CROSS_PILLAR_PATH}")

    # 8. Build .json sidecar
    sidecar = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "schema_version": SCHEMA_VERSION,
        "today": today,
        "slot_planned": SLOT_PLANNED,
        "slot_landed": SLOT_LANDED,
        "slot_reroute_fired": SLOT_REROUTE_FIRED,
        "rows_landed": [
            {"slot": "§VII.W-3.ALGEBRAIC", "stage": "STAGE-3-PERMANENT", "content_sha256": alg_sha, "lines": len(blocks["alg_block"].splitlines())},
            {"slot": "§VII.W-3.SUBSTRATE", "stage": "STAGE-3-PERMANENT", "content_sha256": sub_sha, "lines": len(blocks["sub_block"].splitlines())},
            {"slot": "§VII.W-3.LAB", "stage": "STAGE-1-CANDIDATE", "content_sha256": lab_sha, "lines": len(blocks["lab_block"].splitlines())},
        ],
        "k_counter_advance": {"old": "K=2_SUGGESTION", "new": "K=3_MANDATORY", "instance_3_landing": "§VII.W-3.LAB"},
        "allowlist_row_appended": True,
        "plan_block_sha": plan_block_sha,
        "w4a_16_audit_sha": w4a_16_audit_sha,
        "w4a_16_content_sha": w4a_16_content_sha,
        "workshop_sha_short": workshop_sha[:16],
    }
    JSON_PATH.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    print(f"Saved sidecar: {JSON_PATH}")

    # 9. Compose verdict-line composite
    # Per epistemic-discipline.md §"Registry-Write Hygiene" item 3:
    #   "FAIL-with-remediation (not PASS) so the rerouting is visible in the audit trail"
    # The ROW LANDINGS themselves are structurally complete; FAIL flag is for slot reroute only.
    composite = "FAIL"  # FAIL-with-remediation per item 3
    sign_v = "N/A"      # registry-write gate; no directional pre-reg
    mag_v = "FAIL"      # slot reroute fired (item 3 protocol)
    regime_v = "VALID"  # rows themselves are structurally complete

    value_str = (
        f"3_rows_landed_at_VII-W-3_REROUTED_FROM_VII-W-2;"
        f"alg=STAGE-3-PERMANENT;sub=STAGE-3-PERMANENT;lab=STAGE-1-CANDIDATE;"
        f"K-counter_K2_to_K3_MANDATORY_promoted;"
        f"allowlist_row_appended;"
        f"slot_reroute_fired_per_epistemic-discipline_registry-write-hygiene_item_3"
    )

    content_str = json.dumps(
        {k: sidecar[k] for k in sorted(sidecar.keys())},
        sort_keys=True, separators=(",", ":")
    )

    audit_sha, content_sha = emit_verdict_line(
        composite=composite, value_str=value_str, content_str=content_str,
        sign_v=sign_v, mag_v=mag_v, regime_v=regime_v,
        plan_sha=plan_sha, workshop_sha=workshop_sha,
        w4a_16_audit_sha=w4a_16_audit_sha, w4a_16_content_sha=w4a_16_content_sha,
        plan_block_sha=plan_block_sha,
    )
    print(f"Verdict appended: {VERDICTS_PATH}")
    print(f"  composite: {composite} (FAIL-with-remediation per slot reroute)")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
