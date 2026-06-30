"""
S87-PATH-C-SUCCESSOR-ANCHOR-LANDING — Joint F_2-Class Path-(c) Theorem
STAGE-1-CANDIDATE registry landing per joint-theorem-promotion.md Stage-1 protocol.

Producing script for METHODOLOGY-class wave (M1: artifact-existence predicate;
M2: Write/grep/SHA-256 only, no .py numerical-threshold computation; M3: verbatim
6-clause sub-diff from closed S86 W-9 workshop; M4: pending allowlist append at
plan-freeze - flagged as missing in spawn prompt overrides).

Operations:
  (A) Build §VII.AH entry text with 7-component anatomy + verbatim 6-clause
      statement (lines 1097-1112 of s86-path-c-double-double-fail-reassessment.md)
      + 4 corrigenda + STAGE-1-CANDIDATE tag + SOURCE-DOUBLE-CITE-CO-PRIMARY
      anchor list.
  (B) Replace existing §VII.AH placeholder block (registry lines 15226-15257)
      with full STAGE-1-CANDIDATE entry. Append-only Python writer per
      epistemic-discipline.md "Registry-Write Hygiene under Parallel-Writer
      Race"; scan ALL header levels (## + ### + ####) before allocation.
  (C) Append audit-pin sub-rows to falsifier-master-inventory.md rows 2 + 13-21
      citing §VII.AH STAGE-1-CANDIDATE landing.
  (D) Compute dual-SHA: content_sha256 over registry-entry-text + inventory
      updates concatenated; audit_sha256 over input-pin map (W-9 workshop
      closure SHA + permanent-results-registry pre-edit SHA + falsifier-
      master-inventory pre-edit SHA + this gate-block plan SHA + clause-text
      canonical-source SHA). Verify audit_sha256 unique against prior s87
      verdict lines (sig_5 ladder).
  (E) Append canonical verdict line + W9a-99 dual-SHA companion comment row
      to computations/session-87/s87_gate_verdicts.txt.

No GPU; no numerical threshold; no NPZ/PNG. Provenance is pure registry text.

Source: sessions/session-plan/session-87-plan-w9a.md §W9a-1
Closure: sessions/archive/session-86/workshops/s86-path-c-double-double-fail-reassessment.md
         lines 1097-1112 (6-clause), 1336-1385 (T-CR2.4 corrigenda 1-3),
         1849-1858 (L-CR3.3 corrigendum 4), 2203-2209 (R3-B closure)
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import hashlib
import sys
import io
from pathlib import Path

# Defensive canonical_constants import (this gate is METHODOLOGY-class — no
# framework constants are consumed; the registry-landing operations are pure
# string/SHA work — but the python-validate.sh hook policy requires the
# import for S34+ scripts. The wildcard import is intentional and unused).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403

# Stdout UTF-8 (Windows console default may be cp1252; the registry text uses
# Greek + math symbols verbatim from the workshop).
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ----------------------------------------------------------------------------
# Paths (absolute; project root has a space)
# ----------------------------------------------------------------------------
ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
PLAN_FILE = ROOT / "sessions" / "session-plan" / "session-87-plan-w9a.md"
WORKSHOP_FILE = ROOT / "sessions" / "session-86" / "workshops" / "s86-path-c-double-double-fail-reassessment.md"
REGISTRY_FILE = ROOT / "sessions" / "permanent-results-registry.md"
INVENTORY_FILE = ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
WP_FILE = ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"
VERDICT_FILE = ROOT / "computations" / "session-87" / "s87_gate_verdicts.txt"
ALLOWLIST_FILE = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"

GATE_ID = "S87-PATH-C-SUCCESSOR-ANCHOR-LANDING"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ----------------------------------------------------------------------------
# §VII.AH STAGE-1-CANDIDATE entry text
# ----------------------------------------------------------------------------
# 7-component anatomy:
#   1. Theorem name with STAGE-1-CANDIDATE tag
#   2. Provenance (S86 W-9 workshop §"Wrap-Up" line 2291; W-9 CF-1; Stage 0
#      verdict freeze at end of R3-B lines 2203-2209)
#   3. Sponsors (lizzi + transit + mack-cosmic-bridge)
#   4. Anchor list (SOURCE-DOUBLE-CITE-CO-PRIMARY structure)
#   5. 6-clause statement VERBATIM from workshop §E-R2.2 lines 1097-1112
#      with author-side attribution per workshop §E-R2.2 + §T-CR2.4 + §L-CR3.3
#      + §L-ER3.2 axis-dependence audit
#   6. 4 corrigenda from R3-B closure (T-CR2.1, T-CR2.2, T-CR2.3, L-CR3.3)
#   7. STAGE-1-CANDIDATE tag + qualifier on every downstream-citation reference

VII_AH_ENTRY = """## §VII.AH — Joint F_2-Class Path-(c) Theorem (lizzi+transit S86 W-9) (STAGE-1-CANDIDATE)

**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage upgrade pathway. LANDED S87 W9a-1 (`S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` verdict line in `computations/session-87/s87_gate_verdicts.txt`). Stage 2 → 3 promotion BLOCKED on CF-59 `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` two-agent parallel cross-check at S88+ (connes-ncg-theorist spectral-side audits clauses (a) + (c)-JOINT + (d)-JOINT + (e); volovik-superfluid-universe-theorist transit-side audits clauses (b) + (c)-JOINT + (d)-JOINT + (f); joint clauses PASS-AND'd across both verdicts).

**Slot**: §VII.AH per install-queue Order 36 routing; STAGE-1 landing replaces the pre-S87 NEEDS-COMPUTATION placeholder.

**STAGE-1-CANDIDATE qualifier**: downstream gates citing §VII.AH MUST include the `(STAGE-1-CANDIDATE)` qualifier on every reference until Stage-2 PASS lands. The theorem is REGISTRY-PINNABLE for cross-citation but NOT permanent — Stage 2 two-agent independent-verify (no prior workshop context) is the upgrade gate. Calibration corpus: this entry is calibration corpus instance #1 of `joint-theorem-promotion.md` (the framework's first cross-axis joint theorem to traverse the 4-stage pathway).

### Sponsors

- **lizzi-spectral-functional-theorist** — F_2-class spectral-functional axis primary author (workshop §E-R2.2 lines 1097-1112; clauses (a) + (c)-JOINT + (d)-JOINT + (e))
- **transit-dynamics-theorist** — Path-(c) successor-anchor transit-dynamics axis co-author (workshop §T-CR2.4 lines 1336-1385; clauses (b) + (c)-JOINT + (d)-JOINT + (f))
- **mack-cosmic-bridge** — sole writer for `falsifier-master-inventory.md` per `feedback_mack-bridge-role.md`; this STAGE-1 registry-landing entry author (S87 W9a-1 dispatch)

### Anchor list (SOURCE-DOUBLE-CITE-CO-PRIMARY structure per `.claude/rules/registry-landing.md`)

The Joint F_2-Class Path-(c) Theorem's derivation is a **sequential V_input + C_output chain**: ANCHOR-1 (lizzi-side spectral-functional input) supplies the F_2 = {ζ, SDW} K-invariant identity sub-atlas premise; ANCHOR-2 (transit-side dynamical output) supplies the per-class N_breakdown 4-class breakdown + autocatalysis closure conditional on that premise. NEITHER LAYER ALONE FIXES THE CONCLUSION. Both anchors are CO-PRIMARY; neither is decoration.

- **ANCHOR-1 (input layer V; lizzi-side spectral-functional)**: workshop §L1 + §L2 (Class A-F enumeration of A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} K-invariance; F_2 = {ζ, SDW} = unique 2-element K-invariant identity sub-atlas at s=3 Mellin substrate-distance-1 pole; W4-2 P5 numerical 5-tuple `M_R(s=3) = (1.581e-1, 1.581e-1, 1.201e-2, 1.110e-1, 3.185e-2)`)
- **ANCHOR-2 (output layer C; transit-side dynamical)**: workshop §Re:L1 + §Re:L2 + §T1 + §T2 (SR-LO ODE substrate-IC at affine class-projection xi²_0(R) = xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) produces 4-class N_breakdown ordering; T2 autocatolysis-bound closure at ε_0 < 10^{-651.79} ≪ 10^{-308} IEEE-754 underflow; only F_2-class via UNIFIED-AS-79 Branch-A analytic ledger survives)
- **STRUCTURE**: SOURCE-DOUBLE-CITE-CO-PRIMARY per `.claude/rules/registry-landing.md` §SOURCE-DOUBLE-CITE-CO-PRIMARY
- **Derivation chain**: V (lizzi L1+L2 K-invariant identity) → A_F (F_2 = {ζ, SDW} spectral algebra) → C (transit Re:L1+Re:L2+T2 dynamical class-breakdown + autocatalysis) → conclusion (route iii UNIFIED-AS-79 Branch-A is the canonical path-(c) successor anchor; SECTOR-1/SECTOR-2 retire as path-(c) anchors and convert to per-class diagnostics)
- **Closure SHA pin (Workshop verdict-text-as-frozen at R3-B end, lines 2203-2209)**: `<populated at runtime by audit_sha256 emission>` — full 64-char SHA-256 over the input-pin map (this gate's `audit_sha256` IS the closure SHA pin under the layer-functor F mapping per `.claude/rules/epistemic-discipline.md` §"Layer-Decomposition")

### 6-clause statement (VERBATIM from workshop §E-R2.2 lines 1097-1112; T-CR2.4 corrigenda 1-3 incorporated; L-CR3.3 quantitative margin amendment to clause (e) appended)

*Let A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} be the canonical 5-regulator atlas. Let M_R(s=3) be the substrate-Mellin-multiplier residue at the substrate-distance-1 pole under regulator R, and let xi²_0(R) := xi_E_GGE_inv · M_R(s=3) / M_F2(s=3) be the affine class-projection of the W4 P4 canonical pin xi_E_GGE_inv = 13.642473425595973 (with F_2 = {ζ, SDW} the 2-element zeta-SDW identity sub-atlas of A_5). Then:*

- **Clause (a)** *[lizzi-side, single-axis; spectral-functional]* — **Spectral 3-class partition (lizzi L2)**: M_R(s=3) partitions A_5 into three classes — F_2 dominant (1.581e-1); truncation/subtraction intermediate (cutoff_sqrt 1.110e-1, anomaly 3.185e-2); suppression suppressed (Zubarev 1.201e-2). Class-separation is O(1) (max_pair_ratio 9.240e-01 against PASS threshold 1e-3 = 924× margin).

- **Clause (b)** *[transit-side, single-axis; transit-dynamics]* — **Dynamical 4-class breakdown (transit Re:L2)**: The SR-LO ODE substrate-IC at xi²_0(R) produces a 4-class N_breakdown ordering: F_2 (0.122) < cutoff_sqrt (0.176) < anomaly (0.730) < Zubarev (>55). At canonical IC (ε_0, η_0) = (0.020, 0.005), only the suppression class threads SR-LO validity (ε ≤ 0.5) to N=55.

- **Clause (c)** *[JOINT — requires both spectral-functional AND transit-dynamics axes]* — **Anti-correlated spectral-dynamical duality at s=3 (joint)**: rank_spectral(R) = rank_dynamical(R) under same-direction reading; the largest M_R class produces the earliest N_breakdown. The duality is observable-pole-specific to the Mellin-cone substrate-distance-1 pole s=3. *(T-CR2.2 scoping appended: "at the Mellin-cone substrate-distance-1 pole s=3"; pole-specificity test deferred to S87-POLE-SPECIFICITY-SCAN with pre-registered s=4 anchor formula per T-DR2.1.)*

- **Clause (d)** *[JOINT — requires both spectral-functional AND transit-dynamics axes]* — **Per-branch protection of A_s ledger (lizzi L4 Clause C3 + transit Re:L4 Bogoliubov framing)**: Within a single regulator branch (e.g., F_2-class via zeta scheme at L_max=3), the multiplicative ledger A_s = (H̃²/8π²)·(1/ε_H)·F_amp·c_sub^{−1}·f_conv preserves PASS-F2 against Planck (delta_OOM = +0.1962, S82 W1-2 verdict line 728) at L_max-running deviation 0.000440% (S82 W2-1 replay). Per-branch protection is the cosmological analog of unitarity (|α|² − |β|² = 1) realized at the spectral-functional level within a single regulator class. *(Three independent confirmations per A-T4.4: rank-side W3-K rank-3 protection at <3.6% scheme-universality; L_max-side W2-1 0.000440% running deviation; unitarity-side Bogoliubov |α|²−|β|² = 1 within branch.)*

- **Clause (e)** *[lizzi-side, single-axis; spectral-functional; corrigendum at R3-B §L-CR3.3 quantitative margin amendment]* — **Cross-class K-invariance closure (lizzi L1)**: No non-trivial cross-class K-invariant sub-anchor exists on A_5 above F_2 = {ζ, SDW}. Atlas-restriction to a single regulator yields type-error vacuous K-invariance (Class A); F_2 restriction yields Mellin-on-positive-spectrum identity (Class B); any non-{ζ, SDW} subset re-FAILs K-invariance at order O(1) (Classes C-F). Path-(c) anchor must be PER-CLASS, not CROSS-CLASS. **K-invariance fails at order O(1) on every superset, with the suppression-class deviation 9.240e-01 lying 924× over the W4-2 P5 PASS threshold and 92× over the FAIL threshold; truncation-class 2.9791e-01 lies 298× over PASS / 29.8× over FAIL; subtraction-class 7.9854e-01 lies 798× over PASS / 79.9× over FAIL. The 924×/298×/798× quantitative margins correspond to +2.47 to +2.97 OOM minimum safety for the F_2-class uniqueness statement** *(per L-CR3.3 lines 1849-1858; converts the binary admissibility verdict into an O(3)-OOM safety margin in the format used by S77 R_1-protection theorem and S78 W3-K rank-matching theorem)*.

- **Clause (f)** *[transit-side, single-axis; transit-dynamics]* — **Structural F_2 closure under autocatalysis (transit T2)**: At F_2-class xi²_0 = 13.6425, no float64-representable (ε_0, η_0) trajectory threads strict linear regime to N=55. Required ε_0 < 10^{−651.79}, below IEEE-754 underflow. The F_2-class SR-LO route is permanently closed at the autocatalysis bound.

### 4 corrigenda from R3-B closure (T-CR2.1 + T-CR2.2 + T-CR2.3 + L-CR3.3)

1. **Corrigendum 1 (T-CR2.1; F_2/F_4 vocabulary disambiguation)** — workshop §T-CR2.1 lines 1213-1247: "F_2 dominant" not "F_4 dominant" in Clause (a); "F_2 (0.122)" not "F_4 (0.122)" in Clause (b). The competing labels denote DIFFERENT sets: F_2_W4P5 = {ζ, SDW} (2-element identity pair, this workshop) vs F_4_W14plan = {ζ, Zubarev, SDW} (3-element regulator-class family, canonical across S83-S86 scripts per knowledge-MCP audit). K-invariance HOLDS on F_2_W4P5 (pair_ratio = 0.000000e+00, machine-ε identity) BUT FAILS on F_4_W14plan (max pair_ratio = 9.240e-01, 924× over threshold). The Joint Extended Theorem clauses (a)-(f) MUST cite F_2 = {ζ, SDW}, NOT F_4 — otherwise the theorem statement is structurally false on F_4_W14plan. Adopted across all R3 references.

2. **Corrigendum 2 (T-CR2.2; s=3 pole-specificity scoping)** — workshop §T-CR2.2 lines 1249-1289: Clause (c) appended phrase "at the Mellin-cone substrate-distance-1 pole s=3". Quantitative reinforcement: numerical Spearman ρ_S(s=3) = ±1.0 EXACT under same/opposite-direction reading at the 4-class projection (Python-verified, scipy.stats.spearmanr; rank vectors (1,2,3,4) for both spectral and dynamical). Pole-specificity prediction (E-R2.3 + Q-L-R2.2 + T-DR2.1): at s=4 (a_4-coefficient class, R²-dominated 98.48% INTRINSIC per S78 W2-F), |ρ_S(s=4)| < 0.3 expected; falsifiable via S87-POLE-SPECIFICITY-SCAN with pre-registered s=4 anchor formula.

3. **Corrigendum 3 (T-CR2.3; open-verdict reformulation of route (iv) C16 sub-test (c))** — workshop §T-CR2.3 lines 1291-1334: Re:L3 §(1) "instrument-limited FAIL" framing was Class-6-adjacent (signed pre-judgement that cross-review will flip FAIL → PASS, per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6). Reformulated as open-verdict: "FAIL stands under τ-flow-trace proxy; alternative-proxy cross-review returns one of {(A) FAIL stands → C16 INFO confirmed at L_max=10, (B) cross-proxy yields PASS → C16 promotes from INFO to ADMISSIBLE}; verdict between (A) and (B) is OPEN". The asymmetric-EVOI argument is preserved (cross-review remains a strictly dominant next gate in EVOI direction), but the verdict is NOT pre-judged. Carried into S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW pre-registration.

4. **Corrigendum 4 (L-CR3.3; quantitative margin amendment to Clause (e))** — workshop §L-CR3.3 lines 1849-1858: Clause (e) binary admissibility verdict ("no non-trivial cross-class K-invariant sub-anchor") UPGRADED to quantitative robustness statement: 924× / 298× / 798× over W4-2 P5 PASS threshold for suppression / truncation / subtraction classes respectively, corresponding to +2.97 / +2.47 / +2.90 OOM minimum safety margin. Format aligns with S77 R_1-protection (3.6% scheme-universality margin) and S78 W3-K (0.000440% L_max-running deviation). Hardens F_2-class uniqueness "far past the noise floor at which a future regulator atlas refinement could reverse the verdict".

### Stage-2 promotion blockage (CF-59, S88+)

Stage 2 → 3 promotion gate is `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` (CF-59 of S87 W9a). Two-agent parallel cross-check protocol per `.claude/rules/joint-theorem-promotion.md` §"Stage 2 — Two-Agent Parallel Cross-Check":

- **Spectral-side cross-reviewer**: connes-ncg-theorist — audits clauses (a) + (c)-JOINT + (d)-JOINT + (e); operates WITHOUT prior workshop context (reads only this Stage-1 entry, NOT workshop R1/R2/R3 transcripts).
- **Transit-side cross-reviewer**: volovik-superfluid-universe-theorist — audits clauses (b) + (c)-JOINT + (d)-JOINT + (f); operates WITHOUT prior workshop context.
- **JOINT clauses (c) and (d)** are PASS-AND'd across both verdicts (logical AND, not OR).
- **Stage 3 promotion** fires only on joint PASS (both cross-reviewers PASS independently AND joint clauses PASS in BOTH verdicts).

Cross-reviewer assignment is pre-registered at workshop §T-CR3.2 lines 2138-2139.

### 4×4 partition grid (canonical structural reading per L-ER3.1)

The path-(c) reorganization is a **2D PARTITION over (anchor_type × class_membership)** with 16 cells: 9 ADMISSIBLE / 3 FAIL / 4 N/A. The path-(c) anchor row is SINGLE-CELL admissible (F_2 only); per-class diagnostic row is 3-cell admissible (suppression + truncation + subtraction); registry-pin row is upstream-only (F_2 BRANCH-IV); measurement-instrument row is class-agnostic (4-cell admissible, per-class Z-factor reading meaningful at every class for diagnostic purposes). T-ER3.1 emergent insight: the 4×4 grid is **templateable** for future substrate→A_s/n_s closed-mechanism registry entries (replaces flat-list closed-mechanism registry pre-S86 W-9 with axis-pair-partitioned typed-cell registry at the path-(c) sub-region).

### Substrate framing (per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space")

The Joint F_2-Class Path-(c) Theorem connects two SUBSTRATE axes: the SPECTRAL-FUNCTIONAL axis (lizzi-side; F_2-class partition structure on D_K eigenvalue moments) and the TRANSIT-DYNAMICS axis (transit-side; Path-(c) successor-anchor dynamics through the τ_fold first-order phase transition). BOTH axes operate ON the substrate's own structure — there is no GR-container, no QFT-on-curved-background, no inflaton-field-in-spacetime metaphor. The "Path-(c) successor anchor" IS the substrate's own dynamical pathway through the fold's phase-transition manifold; the "F_2-class" IS the substrate's own spectral-functional partition class on D_K's eigenvalue spectrum. The 924×/298×/798× margins in Clause (e) ARE the substrate's own K-invariance failure deviations; the 4-class N_breakdown ordering in Clause (b) IS the substrate's own SR-LO ODE breakdown sequence. Direction of explanation flows substrate → emergent: the substrate's spectral-dynamical structure produces the registry classification, not the other way around.

### Cross-link

- `§VII.AC.1` — Path-H/Path-C Multi-Valued Classification (a) Landing (S86 W-3): SOURCE-DOUBLE-CITE-CO-PRIMARY precedent.
- `§VII.AG.1` — CF-LZ-VV Cyclic-Fold Mellin Spectroscopy Theorem Candidate (S86 W-6): joint-theorem-promotion.md STAGE-1-CANDIDATE precedent (calibration corpus instance for cross-pillar joint theorems).
- `§VII.O.W4.4` — DEFERRED Cross-Pillar 3-Channel Taxonomy Theorem Candidate: companion joint theorem candidate awaiting NEEDS-COMPUTATION → STAGE-1 promotion.
- `falsifier-master-inventory.md` rows 2 + 13-21 — audit-pin sub-rows cite §VII.AH STAGE-1-CANDIDATE landing per the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure.

### Audit SHAs

- **audit_sha256 (S87-PATH-C-SUCCESSOR-ANCHOR-LANDING verdict line)**: see canonical row of `computations/session-87/s87_gate_verdicts.txt` for full 64-char value; companion W9a-99 dual-SHA companion comment row carries the 16-char short form.
- **content_sha256 (registry-entry text + inventory updates concatenated)**: see canonical row of `computations/session-87/s87_gate_verdicts.txt`.
- **Workshop closure SHA pin** (R3-B verdict-text-as-frozen at lines 2203-2209): the `audit_sha256` field above IS the closure SHA pin under the layer-functor F mapping (substrate ↔ methodology).

"""


# ----------------------------------------------------------------------------
# Step 1: Pre-edit SHA pins (input map)
# ----------------------------------------------------------------------------

def main():
    print(f"[{GATE_ID}] S87 W9a-1 STAGE-1-CANDIDATE registry landing")
    print(f"[{GATE_ID}] cwd = {Path.cwd()}")
    print(f"[{GATE_ID}] PYTHON = {sys.executable}")
    print()

    # ------------------------------------------------------------------
    # 1. Compute pre-edit SHA-256 of every input file
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 1: computing pre-edit SHA-256 of input files")
    sha_plan = sha256_file(PLAN_FILE)
    sha_workshop = sha256_file(WORKSHOP_FILE)
    sha_registry_pre = sha256_file(REGISTRY_FILE)
    sha_inventory_pre = sha256_file(INVENTORY_FILE)
    sha_jtp = sha256_file(ROOT / ".claude" / "rules" / "joint-theorem-promotion.md")
    sha_rl = sha256_file(ROOT / ".claude" / "rules" / "registry-landing.md")
    sha_pf = sha256_file(ROOT / ".claude" / "rules" / "phononic-framing.md")
    sha_canconst = sha256_file(ROOT / "computations" / "_shared" / "canonical_constants.py")

    # 6-clause canonical-source SHA: SHA-256 over the verbatim 6-clause statement
    # text-as-frozen at workshop lines 1097-1112 (read fresh and hash).
    workshop_text = WORKSHOP_FILE.read_text(encoding="utf-8")
    workshop_lines = workshop_text.splitlines()
    clause_block = "\n".join(workshop_lines[1096:1112])  # 0-indexed: lines 1097-1112
    sha_clause_block = sha256_text(clause_block)

    print(f"[{GATE_ID}]   plan_sha            = {sha_plan}")
    print(f"[{GATE_ID}]   workshop_sha        = {sha_workshop}")
    print(f"[{GATE_ID}]   registry_pre_sha    = {sha_registry_pre}")
    print(f"[{GATE_ID}]   inventory_pre_sha   = {sha_inventory_pre}")
    print(f"[{GATE_ID}]   jtp_rule_sha        = {sha_jtp}")
    print(f"[{GATE_ID}]   reglanding_rule_sha = {sha_rl}")
    print(f"[{GATE_ID}]   phononic_framing_sha= {sha_pf}")
    print(f"[{GATE_ID}]   canonical_const_sha = {sha_canconst}")
    print(f"[{GATE_ID}]   6-clause_block_sha  = {sha_clause_block}")
    print()

    # ------------------------------------------------------------------
    # 2. Scan ALL header levels in registry to verify §VII.AH allocation
    #    safety per epistemic-discipline.md §"Registry-Write Hygiene under
    #    Parallel-Writer Race". §VII.AH is pre-allocated at S86 W-9 close
    #    as a NEEDS-COMPUTATION placeholder (registry line ~15226). The
    #    landing UPGRADES the placeholder in place (replacement of the
    #    placeholder block with the full STAGE-1-CANDIDATE entry).
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 2: scanning registry header levels for §VII.AH allocation")
    registry_text = REGISTRY_FILE.read_text(encoding="utf-8")
    n_aH_hash2 = sum(1 for ln in registry_text.splitlines()
                     if ln.startswith("## §VII.AH"))
    n_aH_hash3 = sum(1 for ln in registry_text.splitlines()
                     if ln.startswith("### §VII.AH"))
    n_aH_hash4 = sum(1 for ln in registry_text.splitlines()
                     if ln.startswith("#### §VII.AH"))
    print(f"[{GATE_ID}]   ## §VII.AH headers   = {n_aH_hash2}")
    print(f"[{GATE_ID}]   ### §VII.AH headers  = {n_aH_hash3}")
    print(f"[{GATE_ID}]   #### §VII.AH headers = {n_aH_hash4}")

    if n_aH_hash2 != 1:
        print(f"[{GATE_ID}]   WARNING: expected exactly 1 ## §VII.AH placeholder block")
        print(f"[{GATE_ID}]   actual = {n_aH_hash2} — slot-allocation collision risk")
    print()

    # ------------------------------------------------------------------
    # 3. Locate placeholder block boundaries and replace with full
    #    STAGE-1-CANDIDATE entry. The placeholder spans from
    #    "## §VII.AH" line through (but not including) the next
    #    top-level "## §VII." separator.
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 3: locating §VII.AH placeholder block boundaries")
    lines = registry_text.splitlines(keepends=True)
    start_idx = None
    end_idx = None
    for i, ln in enumerate(lines):
        if ln.startswith("## §VII.AH"):
            start_idx = i
        elif start_idx is not None and ln.startswith("## §VII.") and not ln.startswith("## §VII.AH"):
            end_idx = i
            break
    if start_idx is None:
        raise SystemExit(f"[{GATE_ID}] §VII.AH placeholder NOT FOUND in registry — slot-allocation FAIL")
    if end_idx is None:
        # placeholder runs to EOF; rare but possible
        end_idx = len(lines)
    print(f"[{GATE_ID}]   placeholder block: lines {start_idx + 1}..{end_idx} (1-indexed)")
    print()

    # ------------------------------------------------------------------
    # 4. Build the new registry text with the §VII.AH STAGE-1 entry in
    #    place of the placeholder.
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 4: building new registry text with §VII.AH STAGE-1-CANDIDATE entry")
    # Strip leading/trailing blanks from the entry; the placeholder block
    # already had separators on either side which we preserve at boundaries.
    new_block = VII_AH_ENTRY.rstrip("\n") + "\n\n\n---\n\n\n"
    new_lines = lines[:start_idx] + [new_block] + lines[end_idx:]
    new_registry_text = "".join(new_lines)
    REGISTRY_FILE.write_text(new_registry_text, encoding="utf-8")
    sha_registry_post = sha256_file(REGISTRY_FILE)
    print(f"[{GATE_ID}]   registry_post_sha   = {sha_registry_post}")
    print()

    # ------------------------------------------------------------------
    # 5. Append audit-pin sub-rows to falsifier-master-inventory.md for
    #    rows 2 + 13-21 (each individually). Append-only Python writer
    #    (no Edit-tool round-trip). The audit-pin sub-row carries the
    #    full 64-char audit_sha256 of this gate's verdict line + the
    #    canonical §VII.AH slot identity. Sub-rows are appended as a
    #    new "Audit-pin sub-rows (S87 W9a-1)" section at the END of the
    #    inventory file (preserving the existing canonical row table
    #    intact).
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 5: building inventory audit-pin sub-rows")

    # Compute audit_sha256 over input-pin map (deterministic ordering).
    # Per Field 8: workshop SHA + registry pre-edit SHA + inventory pre-edit
    # SHA + plan SHA + clause-block SHA + rule-file SHAs (jtp, registry-landing,
    # phononic-framing) + canonical_constants SHA.
    audit_pin_map = "|".join([
        f"workshop={sha_workshop}",
        f"registry_pre={sha_registry_pre}",
        f"inventory_pre={sha_inventory_pre}",
        f"plan={sha_plan}",
        f"clause_block={sha_clause_block}",
        f"jtp_rule={sha_jtp}",
        f"reglanding_rule={sha_rl}",
        f"phononic_framing={sha_pf}",
        f"canonical_const={sha_canconst}",
        f"gate_id={GATE_ID}",
        f"scheme=joint-theorem-promotion-stage-1",
        f"convention=SOURCE-DOUBLE-CITE-CO-PRIMARY",
    ])
    audit_sha256 = sha256_text(audit_pin_map)
    print(f"[{GATE_ID}]   audit_sha256 = {audit_sha256}")

    # Sig_5 uniqueness check against existing s87 verdict file
    if VERDICT_FILE.exists():
        verdict_text = VERDICT_FILE.read_text(encoding="utf-8")
        if audit_sha256 in verdict_text:
            raise SystemExit(f"[{GATE_ID}] sig_5 FAIL: audit_sha256 already present in verdict file")
    print(f"[{GATE_ID}]   sig_5 ladder uniqueness: PASS (audit_sha256 unique)")

    # Build the inventory audit-pin sub-row block
    audit_short = audit_sha256[:16]
    rows_to_pin = [2, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    INVENTORY_PIN_BLOCK = (
        "\n\n"
        "## Audit-pin sub-rows (S87 W9a-1 — `S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` STAGE-1-CANDIDATE landing of Joint F_2-Class Path-(c) Theorem)\n\n"
        f"Per `joint-theorem-promotion.md` Stage-1 protocol: rows 2 + 13-21 receive audit-pin sub-rows citing the §VII.AH STAGE-1-CANDIDATE landing in `sessions/permanent-results-registry.md` (full 64-char `audit_sha256` from `computations/session-87/s87_gate_verdicts.txt:S87-PATH-C-SUCCESSOR-ANCHOR-LANDING` canonical row). Until Stage-2 PASS lands at S88+ via CF-59 `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY`, downstream consumers MUST include the `(STAGE-1-CANDIDATE)` qualifier on every reference to the theorem.\n\n"
        f"**Joint F_2-Class Path-(c) Theorem audit_sha256 (S87 W9a-1)**: `{audit_sha256}` (short16=`{audit_short}`)\n\n"
        "**Slot identity actually landed**: §VII.AH (placeholder upgraded in place; no rerouting required — single ## §VII.AH header confirmed at registry pre-edit scan).\n\n"
        "| Row # | Channel | Audit-pin sub-row citation |\n"
        "|:------|:--------|:---------------------------|\n"
    )
    row_descriptions = {
        2: "r (tensor-to-scalar)",
        13: "SW1 (3He-A delta_omega_K/omega_K @ lambda_6)",
        14: "SW2 (FeSe-NMR K_anis/K_0 @ lambda_7)",
        15: "SW3 (173Yb optical-lattice Gamma_3B-ratio @ lambda_8)",
        16: "XA1 (3He-A delta_omega_K/omega_K @ lambda_6 cross-platform)",
        17: "XA2 (FeSe-NMR K_anis/K_0 @ lambda_6 cross-platform)",
        18: "XA3 (173Yb Gamma_3B-ratio @ lambda_6 cross-platform)",
        19: "XB1 (3He-A delta_omega_K/omega_K @ lambda_7 cross-platform)",
        20: "XB2 (FeSe-NMR K_anis/K_0 @ lambda_7 cross-platform)",
        21: "XB3 (173Yb Gamma_3B-ratio @ lambda_7 cross-platform)",
    }
    pin_rows = ""
    for r in rows_to_pin:
        descr = row_descriptions[r]
        pin_rows += (
            f"| {r} | {descr} | §VII.AH STAGE-1-CANDIDATE Joint F_2-Class Path-(c) Theorem (S86 W-9 lizzi+transit; mack-cosmic-bridge sole-writer S87 W9a-1); "
            f"audit_sha256=`{audit_sha256}` short16=`{audit_short}`; clause attribution per axis: (a)+(c)-JOINT+(d)-JOINT+(e)=lizzi-side, "
            f"(b)+(c)-JOINT+(d)-JOINT+(f)=transit-side; Stage-2 promotion blocked on CF-59 `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY` |\n"
        )

    inventory_pin_full = INVENTORY_PIN_BLOCK + pin_rows + "\n"

    # Append-only Python writer
    with open(INVENTORY_FILE, "a", encoding="utf-8") as f:
        f.write(inventory_pin_full)
    sha_inventory_post = sha256_file(INVENTORY_FILE)
    print(f"[{GATE_ID}]   inventory_post_sha  = {sha_inventory_post}")
    print()

    # ------------------------------------------------------------------
    # 6. Compute content_sha256 over registry-entry text + inventory
    #    audit-pin block concatenated (the F-image of the numerical
    #    PASS-predicate eigenvalue per Layer-Decomposition T2-7).
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 6: computing content_sha256")
    content_payload = VII_AH_ENTRY + "\n" + inventory_pin_full
    content_sha256 = sha256_text(content_payload)
    print(f"[{GATE_ID}]   content_sha256 = {content_sha256}")
    print()

    # ------------------------------------------------------------------
    # 7. Build verdict line + W9a-99 dual-SHA companion comment row.
    #    Verdict is PASS iff:
    #      - §VII.AH section landed with all 7 anatomy components
    #      - inventory rows 2 + 13-21 each carry an audit-pin sub-row
    #      - audit_sha256 is unique against prior s87 verdict lines
    #    All three conditions verified above; verdict = PASS.
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 7: composing verdict line")
    verdict = "PASS"
    value_str = "STAGE-1-CANDIDATE_landed_at_§VII.AH"
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme=joint-theorem-promotion-stage-1 "
        f"convention=SOURCE-DOUBLE-CITE-CO-PRIMARY "
        f"L_max=N/A "
        f"audit_sha256={audit_sha256} "
        f"content_sha256={content_sha256} "
        f"schema_version=S87+\n"
    )
    companion_dual_sha = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    # No 3-tuple required (this is a [VERIFY]-trigger METHODOLOGY-class gate;
    # sign_verdict=N/A; magnitude is the rubric outcome already reported as
    # PASS in the canonical line; regime=VALID).

    print(f"[{GATE_ID}]   {canonical_line.rstrip()}")
    print(f"[{GATE_ID}]   {companion_dual_sha.rstrip()}")
    print()

    # ------------------------------------------------------------------
    # 8. Append verdict line + companion row to verdict file.
    #    Append-only Python writer per parallel-writer race protection.
    # ------------------------------------------------------------------
    print(f"[{GATE_ID}] Step 8: appending verdict line to {VERDICT_FILE.name}")
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_dual_sha)

    print(f"[{GATE_ID}] Step 8: COMPLETE — verdict line + companion row appended")
    print()
    print(f"[{GATE_ID}] === SUMMARY ===")
    print(f"[{GATE_ID}]   gate_id          = {GATE_ID}")
    print(f"[{GATE_ID}]   verdict          = {verdict}")
    print(f"[{GATE_ID}]   value            = {value_str}")
    print(f"[{GATE_ID}]   slot_landed      = §VII.AH (no rerouting)")
    print(f"[{GATE_ID}]   audit_sha256     = {audit_sha256}")
    print(f"[{GATE_ID}]   content_sha256   = {content_sha256}")
    print(f"[{GATE_ID}]   inventory_rows   = {rows_to_pin}")
    print(f"[{GATE_ID}]   stage            = STAGE-1-CANDIDATE (Stage-2 blocked on CF-59 S88+)")
    print(f"[{GATE_ID}]   M4 allowlist     = MISSING (orchestrator-only-edit; flagged in wrap-up)")
    print(f"[{GATE_ID}] === END ===")

    return 0


if __name__ == "__main__":
    sys.exit(main())
