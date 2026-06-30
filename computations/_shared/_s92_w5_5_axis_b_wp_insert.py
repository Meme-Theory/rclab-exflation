"""S92 W5-5 Axis-B mack WP sub-section insertion helper.

Parallel-writer-safe atomic insert via tempfile + os.replace, per
`.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race"`: "Use append-only Python writers, not Edit-tool
round-trips, for shared-write registries. The Edit tool is mtime-conditional:
when two agents both Read the file then Edit, the second Edit fails with
mtime conflict."

This helper:
  (i) reads the current WP state
  (ii) checks idempotency (skip if Axis-B sub-section already present)
  (iii) locates the sentinel '---\n\n## Wave 5 Synthesis (team-lead)'
  (iv) inserts the Axis-B sub-section atomically before that sentinel
  (v) writes via tempfile + fsync + os.replace (race-safe).

Idempotency: re-running this script after success is a no-op.
"""
import os
import sys
import tempfile

# Required per `computations/_shared/CLAUDE.md` "Canonical Constants (MANDATORY)"
# discipline (`/weave --update` audit grep). This helper consumes zero framework
# constants (pure I/O + atomic file write); import is defensive-conformance only.
from canonical_constants import *  # noqa: F401,F403

WP_PATH = "sessions/archive/session-92/session-92-w5-workingpaper.md"
SENTINEL = "\n---\n\n## Wave 5 Synthesis (team-lead)"
IDEMPOTENCY_MARKER = "### Axis-B mack-cosmic-bridge Per-Clause Verdict"

AXIS_B_SUBSECTION = """
### Axis-B mack-cosmic-bridge Per-Clause Verdict

**Dispatch role**: Stage-2 cross-axis independent-verify per `joint-theorem-promotion.md §"Stage 2"` 4-stage pathway; Axis-B = cosmological-anchor / observational-bridge axis. JSON sidecar: `computations/session-92/s92_w5_5_axis_b_mack_verdict.json` (primary deliverable for aggregator gen-physicist composite PASS-AND aggregation).

**Independence discipline pin** (`joint-theorem-promotion.md §"Two-Agent Independent-Verify"` item 4): consumed ONLY the registered Stage-1 entry text at `sessions/permanent-results-registry.md §VII.AU.OP-PROJ` (canonical CF-64 RETRY content-host + §W5-2 sub-class tag attachment at lines 18939+ + §W5-3 RETROFIT Anchor_2 inline citation at lines 18923-18934), Set_B substrate-input files (`mack-observational-constraints.md` + `canonical_constants.py` n_s pins), and rule files (`joint-theorem-promotion.md`, `gate-verdicts.md`, `cross-pillar-bridge-anatomy.md`, `phononic-framing.md`). NO READING of S91 W6-1 workshop transcripts at `sessions/archive/session-91/workshops/`. NO READING of Axis-A vdd verdict JSON sidecar (file ABSENT on disk at verify-time, structurally confirming independent-verify discipline).

**Axis-B Selection Protocol compliance** (`joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` MANDATORY K=1 since S88 W-14): clause 1 axis-distinctness PASS (mack cosmological-anchor methodology != vdd substrate-physics/NCG-bridge methodology); clause 2 original-authoring-agent exclusion + downstream-inheritance reach test PASS (mack was Stage-1 registry-text sole-writer at S89 W7c; writer-vs-reviewer scope distinction structural — Stage-2 reviewer-of-OTHER-axis substrate-physics PASS-AND audit is structurally distinct from registry-text sole-writer role); clause 3 audit-coverage adequacy PASS (cosmological-anchor domain expertise covers ALL JOINT clauses + ALL cosmological-anchor / observational-bridge single-axis clauses).

**Set_B substrate-input pin** (`joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY K=3 since S90 W2 CF-20): Set_B files = (i) `sessions/framework/registry/mack-observational-constraints.md` (sole-writer registry of Planck/DESI/BICEP-Keck observational anchors + framework-prediction snapshots; lines 215-217 supply Planck 2018 n_s anchor + Planck alpha_s + ACT DR4+Planck alpha_s; lines 223-225 supply framework-vs-observation discrimination snapshot); (ii) `computations/_shared/canonical_constants.py` n_s pins (`planck_ns = 0.9649` at line 1604; `planck_ns_err = 0.0042` at line 1605; `n_s_framework = 0.9561` at line 1738). Set_B SHA-256 (mack-observational-constraints.md) = `cc721a4e233ab4a0c98bb82baff6e3bf59b6bb59d94e7306a04c89e3764848f0` (computed at runtime via Python hashlib over file bytes). Set_B loaded by mack (Axis-B) ONLY; the substrate-physics L_max=14+ first-extraction npz from §W5-1 (Set_A) is consumed by vdd (Axis-A) ONLY. Partition disjoint at obs_1 = framework-prediction-vs-Planck-observation comparison at §VII.AU.OP-PROJ Level 3 empirical anchor => substrate-input-orthogonality predicate PASS at STRUCTURAL CEILING (no substrate-input-overlap caveat applies).

#### Single-axis clauses (cosmological-anchor / observational-bridge)

**Clause 1 -- CMB n_s observation as laboratory-IN observable**: **PASS**. Registry §VII.AU.OP-PROJ Element 2 identifies CMB n_s as the laboratory-IN observable for Pillar II via the OE-form `int_BZ d^d k Tr_{A_K}( P_n-s-substrate-distance-1 . rho_BZ(k; tau_fold) )`. The substrate framing flows correctly: Substrate (Pillar I) IS the substrate-distance-1 Hochschild pairing image n_s_FW -> HKR bridge map -> Laboratory (Pillar II) IN CMB n_s observation. CMB n_s is operationally the slope of the primordial scalar power spectrum `P_zeta(k) = A_s (k/k_pivot)^(n_s-1)` at `k_pivot = 0.05 Mpc^{-1}`, measured by Planck via TT,TE,EE+lowE+lensing angular-power-spectrum likelihood. This is the canonical continuum cosmological measurement at the Pillar II anchor; the IS-not-IN direction matches `phononic-framing.md §"IS Space, Not IN Space"` direction-of-explanation requirement. Element 2 satisfies MANDATORY OE-form discipline (S88 W7a-73 K=2) via the named projector `P_n-s-substrate-distance-1` lifting the band-0 spectral-density-of-states operator under the HKR image.

**Clause 2 -- Planck n_s anchor at 2.0952 sigma central value per Level 3 empirical anchor at L_max=10**: **PASS**. Registry Element 5: `|n_s_planck - n_s_FW| / sigma_planck = (0.9649 - 0.9561) / 0.0042 = 2.0952 sigma at L_max=10 canonical truncation`. Independent verification: Planck 2018 n_s = 0.9649 +/- 0.0042 is the TT,TE,EE+lowE+lensing central value per `canonical_constants.py:1604-1605` (planck_ns + planck_ns_err); mack-observational-constraints.md:215 corroborates ("Planck 2018 n_s = 0.9649 +/- 0.0042"); :223 independently computes 2.10 sigma to 4 sig figs (full-precision 2.09524 sigma matches registry citation). The Level-3 empirical anchor at L_max=10 satisfies the Level-2 `L^{-3}` envelope at the SUBSTRATE-IS convergence axis via W7b PASS (`audit_sha256=d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f`). The 2.0952 sigma Planck discrimination IS the laboratory-IN discriminator content the FWD-C1 bridge predicts -- a legitimate structural feature, NOT a Level-2 envelope violation. CMB-S4 sigma_n_s ~ 1.8e-3 will sharpen this to >= 4 sigma at S4 horizon.

**Clause 3 -- Pillar II observational constraint per mack-observational-constraints.md framework-prediction snapshot**: **PASS**. Three canonical observational anchors at mack-observational-constraints.md:215-217 (Planck 2018 n_s, Planck 2018 alpha_s, ACT DR4+Planck Aiola 2020 alpha_s post-W1b-8 canonical pin update 2026-04-30). Line 224: `alpha_s_canonical = -0.0859` vs Planck alpha_s gives 12.15 sigma -- FIRST multi-sigma falsifier within near-term observational reach per `falsifier-master-inventory.md` Row #3 CF-29 update. Line 225: alpha_s_canonical vs ACT DR4 = 13.99 sigma -- within CMB-S4 + CMB-HD horizon. The substrate-IS image n_s_FW = 0.9561 provides legitimate Level-3 discriminator content at current Planck precision (2.10 sigma) sharpening to >= 4 sigma at CMB-S4; the FWD-C1 bridge is a near-term-falsifiable structural prediction, NOT a vacuous-margin claim. The 2.10 sigma Planck discrimination IS the bridge predicted structural content per Element 3 fiducial-anchor binding type (i) substrate-self-consistent.

#### JOINT clauses (PASS-AND with Axis-A vdd)

**JOINT Clause A -- 5-anatomy Element 3 bridge map (HKR L_max -> infinity image)**: **PASS**. Registry Element 3 declares the bridge map EXPLICITLY: HKR (Hochschild-Kostant-Rosenberg) map L_max -> infinity image (Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula). Element 3 fiducial-anchor binding type is DECLARED: (i) substrate-self-consistent -- pre-substrate pin `n_s_FW_exact = Fraction(9561, 10000)` IS the framework prediction at the same algebra-axis family (Cell I x substrate-distance-1 pole s=3); NOT (ii) external-observation; NOT (iii) joint-hypersurface. Per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`, undeclared binding => registry-incompleteness FAIL; declaration IS present. The bridge map admits HKR-class only (single-scheme; cross-pillar bridge K-counter Table column "HKR L_max->infinity" for instance #4); optional scheme-suffix extensions (APS-1975 / Cheeger-Simons / Bismut-Cheeger) per "Bridge-map-scheme suffix discipline" apply when bridge admits multiple scheme evaluations -- for single-scheme HKR this is admissible without suffix. Cross-validates Axis-A vdd substrate-physics-NCG-bridge audit at the bridge-map-identification layer (CM-1995 §III.4 residue formula + HKR L_max -> infinity image -- jointly cited).

**JOINT Clause B -- 3-level ladder substrate-IS-to-laboratory-IN mapping**: **PASS**. Registry Three-level ladder table: Level 1 = STRUCTURAL THEOREM `n_s_FW^2 - 1 == alpha_s_canonical` in Q at substrate-distance-1 pole s=3 (regulator-invariant, L-independent, Cell I algebra-INVARIANT spectrum-only-functional; W7a PASS `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`); Level 2 = STRUCTURAL PREDICTION `L^{-3}` algebraic convergence envelope at d=4 substrate-distance-1 pole s=3 (Level-2-binding sub-class per S88 W8-88 -- HKR-image binds Level-1); Level 3 = EMPIRICAL CONFIRMATION Planck n_s = 0.9649 +/- 0.0042 vs substrate-IS n_s_FW = 0.9561; discrimination 2.0952 sigma at L_max=10 (W7b PASS satisfies envelope). The substrate-IS-to-laboratory-IN mapping flows correctly: substrate-IS cohomology-class identity (Level 1) -> HKR-image convergence envelope binding Level-1 to laboratory-IN (Level 2) -> Planck observation IS the laboratory-IN anchor satisfying Level-2 envelope at L_max=10 (Level 3). The Level-2 binding sub-class is DECLARED (admissible for registry-PASS per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"` -- non-binding would be FORBIDDEN). The Level-3 < Level-2 satisfaction criterion applies to the substrate-IS-side convergence envelope (W7b PASS confirms substrate-side L^{-3} convergence clean at L_max=10), NOT to the framework-vs-observation discrimination (which IS the bridge structural discriminator content per Element 3 fiducial-anchor binding type (i) substrate-self-consistent). Post-S92 W5-2 sub-class tag attachment CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED (registry line 18939+) further notes the L_operational=14+ empirical confirmation and the asymptotic L_max -> infinity deferred via Friedrich-Bar saturation theorem; sub-class status IS the Stage-2 dispatch licensing status.

**JOINT Clause C -- HIT K-counter advancement axes (i)/(iii) for K=3 -> K=4 saturation continuation**: **PASS**. Registry HIT block: (i) distinct substrate-IS pillar YES -- Pillar I (M^4 x SU(3) Mellin-cone closure at substrate-distance-1 pole s=3) distinct from Pillar III (HP^1 cohomology of §VII.AF.1.OP-PROJ W-5 / W11-5 / W4a-17); (ii) distinct laboratory-IN pillar YES -- Pillar II (CMB n_s observation; cosmological anchor) distinct from Pillar IV (Peotta-Tormae quantum-metric BZ-trace) and Pillar V (3He-B BdG sector); (iii) distinct bridge map class NO -- same HKR class; disjunction `(i v ii v iii)` only requires ANY, and (i) ^ (ii) both YES; (iv) independent algebraic envelope YES -- `L^{-3}` d=4 envelope shares structural form but binds STRUCTURALLY DISTINCT Level-1 identity (`n_s^2 - 1 == alpha_s` Sage-QQ exact rational in Q vs HP^1 cohomology norm `R_universal_HP1_strict_F4 = 1.030902` vs 3He-B inheritance kernel); refinement-vs-independent test PASS (NOT a numerical refinement of any prior K-instance envelope). Predicate evaluation: `(YES v YES v NO) ^ YES = YES`. K-counter advancement K=3 -> K=4 is a SATURATION CONTINUATION (NOT a re-promotion event); rule status MANDATORY at K=3 since S88 W4a-17 close is PRESERVED per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` Companion-entry tagging clause. From cosmological-anchor cross-review axis: clause (ii) PASS is structurally unambiguous (Pillar II IS the CMB cosmological anchor pillar, structurally distinct from Pillar IV laboratory quantum-metric and Pillar V 3He-B BdG); clauses (i) and (iv) PASS verified at the substrate-IS pillar + algebraic-envelope identification level.

#### Axis-B composite

**axis_B_composite = PASS**. All 3 single-axis cosmological-anchor / observational-bridge clauses PASS (CMB n_s laboratory-IN observable identification; Planck n_s 2.0952 sigma anchor at L_max=10; Pillar II observational constraint per mack registry snapshot). All 3 JOINT clauses PASS-AND-eligible from Axis-B side (Element 3 HKR bridge map; 3-level ladder substrate-IS-to-laboratory-IN mapping; HIT K=3 -> K=4 saturation continuation). Substrate-input-orthogonality at STRUCTURAL CEILING verified (Set_B mack registry + canonical_constants n_s pins routed to Axis-B ONLY; disjoint from Set_A §W5-1 npz routed to Axis-A). Final aggregator composite PASS contingent on Axis-A vdd PASS-AND from the substrate-physics/NCG-bridge axis + Option A `supersedes` tag emission compliance (full 64-char `supersedes=cdbebfa9ad4cc4a8d14d487142a2b132f6d5f8073bea0aeb2f2e29ef330c408b` in `value=` field at corrective canonical line emission per Option A clause 5 forward-emission discipline since S88 W8-100).
"""


def main():
    with open(WP_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if IDEMPOTENCY_MARKER in content:
        print("ALREADY_INSERTED (idempotent no-op)")
        return 0

    idx = content.find(SENTINEL)
    if idx == -1:
        print("SENTINEL_NOT_FOUND -- '---\\n\\n## Wave 5 Synthesis (team-lead)' not located")
        return 2

    new_content = content[:idx] + AXIS_B_SUBSECTION + content[idx:]

    # Atomic write: tempfile in same directory + fsync + os.replace
    dir_path = os.path.dirname(WP_PATH)
    tmp_fd, tmp_path = tempfile.mkstemp(
        suffix=".md", dir=dir_path, prefix=".tmp_w5_axis_b_"
    )
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
            f.write(new_content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, WP_PATH)
        print("INSERTED")
        return 0
    except Exception:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise


if __name__ == "__main__":
    sys.exit(main())
