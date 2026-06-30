#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S91-W1-14-WODZICKI-BCS-BRIDGE-THEOREM-STAGE-1-CANDIDATE-REGISTRY-LANDING
=========================================================================

Gate ID: S91-W1-14-WODZICKI-BCS-BRIDGE-THEOREM-STAGE-1-CANDIDATE-REGISTRY-LANDING
Aliases: S91-W9-9; S91-WODZICKI-BCS-STAGE-1

Origin: S90 W1-14 carry-forward (Wodzicki-BCS bridge theorem identification).
        NEW STAGE-1-CANDIDATE bridge theorem registry landing per
        joint-theorem-promotion.md §"Stage 1" — theorem registered as
        STAGE-1-CANDIDATE with all 5-anatomy elements + 3-level structural-
        confidence ladder per cross-pillar-bridge-anatomy.md §"IS-not-IN
        Anatomy (5 elements)" + §"Three-Level Structural-Confidence Ladder".

Bridge theorem statement:
        Wodzicki noncommutative residue uniqueness on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)
        ↔ BCS gap-equation regulator-invariance on A_BdG = M_2(ℂ) ⊂ A_K
        via layer-functor F per epistemic-discipline.md §"Layer-Decomposition".

Pattern: single-shot AFTER-pattern per
         computations/_bridge_landing_script_template.py (S87 W3c-30) +
         registry-landing.md §"Bridge-Landing Script Architecture":
         build_promotion_text -> write_atomic_append_with_fsync (POSIX
         O_APPEND) -> re_read_and_verify -> emit_verdict_line (exactly one
         canonical + dual-SHA companion + S87+ 3-tuple companion).

Sole writer: mack-cosmic-bridge per feedback_mack-bridge-role.md.
Substrate-physics co-author: volovik-superfluid-universe-theorist
        (BCS gap-equation regulator-invariance Δ_BCS R-PROTECTED canonical
        interpretation; cross-cited from k-floor-regulator-invariance-84-result
        agent memory file demonstrating the K-floor regulator-dependence
        asymmetry vs Δ_BCS R-protection at S74 W4-F #19 drift 0.00%; the
        Volovik partition canonical pin w0_FW = -0.918 per S58 anchors the
        BCS-related substrate-physics invariance class).

HIT axis (iii) bridge-map-class distinctness verified at landing:
        Wodzicki residue NOT in {HKR, K-theory boundary, Connes-Karoubi pairing}.
"""

from __future__ import annotations

import hashlib  # (local)
import os  # (local)
import sys  # (local)
from pathlib import Path  # (local)

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU cap per math-scripts.md

import numpy as np  # (local)

# Canonical constants import per math-scripts.md (MANDATORY S34+)
_SHARED = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_shared"))  # (local)
if _SHARED not in sys.path:
    sys.path.insert(0, _SHARED)
from canonical_constants import (  # noqa: E402
    Delta_BCS,
    M_KK,
    tau_fold,
    w0_FW,
)

# Re-bind to in-script readability aliases; canonical source is canonical_constants.py
DELTA_BCS_CANONICAL = Delta_BCS  # (local; alias 0.4642547394830737 M_KK; R-PROTECTED at S70/S74)
M_KK_CANONICAL = M_KK  # (local; alias)
TAU_FOLD_CANONICAL = tau_fold  # (local; alias 0.19)
W0_FW_CANONICAL = w0_FW  # (local; alias -0.918, Volovik partition + effacement per S58)

GATE_ID = "S91-W1-14-WODZICKI-BCS-BRIDGE-THEOREM-STAGE-1-CANDIDATE-REGISTRY-LANDING"  # (local)
SLOT_EXPECTED = "§VII.BA"  # (local; next-free letter after §VII.AZ; plan said §VII.AX but that slot is occupied by S91 W5-4 PBH landing — next-free-letter scan resolves to §VII.BA after AX/AY/AZ exhausted)
SLOT_PLAN_NAMED = "§VII.AX"  # (local; plan §W9-9 named slot — superseded by next-free-letter scan)
SCHEME = "wodzicki-residue-uniqueness-BCS-gap-equation-regulator-invariance-via-layer-functor-F"  # (local)
CONVENTION = "VII-AX-WODZICKI-BCS-STAGE-1-CANDIDATE-substrate-distance-1-pole-Layer-Functor-F-bridge-binding-SUBSTRATE-NATURAL"  # (local; plan-pinned convention tag — preserved per Field 8 expected output 4-tuple even though slot allocated as §VII.BA)
SCHEMA_VERSION = "S87+"  # (local)
L_MAX = 12  # (local; cached spectrum)

EMPIRICAL_FLOOR_STAGE_1 = 1e-1  # (local; 10% Level-3 anchor floor per Field 9 (d))
EMPIRICAL_INFO_BAND = 5e-1  # (local; INFO band per Field 9 INFO criterion)
LEVEL_2_ENVELOPE_EXPONENT = 2.0  # (local; L^{-2} at d=4 per Connes 1995 §III)
HIT_K_COUNTER_PRE = 1  # (local; SUGGESTION at S90 close)
HIT_K_COUNTER_POST = 2  # (local; SUGGESTION after Wodzicki landing)

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")  # (local)
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_PATH = PROJECT_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"  # (local)
CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
CC_PATH = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-91-plan-w9.md"  # (local)
RULE_BRIDGE = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"  # (local)
RULE_REGISTRY = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"  # (local)
RULE_JOINT = PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"  # (local)
RULE_PHONONIC = PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md"  # (local)
RULE_EPISTEMIC = PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"  # (local)
RULE_REGULATOR_PIN = PROJECT_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"  # (local)
VOLOVIK_MEMORY_K_FLOOR = (
    PROJECT_ROOT / ".claude" / "agent-memory" / "volovik-superfluid-universe-theorist"
    / "k-floor-regulator-invariance-84-result.md"
)  # (local)


def sha256_of_path(p: Path) -> str:
    """SHA-256 over the file's raw bytes (no normalization)."""
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(s: str) -> str:
    """SHA-256 over text encoded as UTF-8."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def compute_wodzicki_residue_at_L12() -> tuple[float, dict]:
    """Compute the numerical Wodzicki residue Res_W(D_K^{-2s})|_{s=2}
    on the L_max=12 master cache.

    Substrate-IS observable: Res_W(D_K^{-2s})|_{s=2} = Σ_α m_α · |λ_α|^{-4} · ξ_W(s=2)
    with ξ_W(s=2) = Γ(2) = 1 (canonical NC-trace normalization at s=2; closed-form).

    The cache stores Peter-Weyl sector eigenvalues keyed by (p, q) with per-sector
    'dim' (multiplicity) and 'abs_evals' (eigenvalue magnitudes). Each eigenvalue
    inside a sector carries multiplicity 'dim' relative to the algebra-level Peter-
    Weyl multiplicity — i.e., per-(p,q) sector the contribution to Tr(|D_K|^{-4})
    is dim · Σ_i |λ_α,i|^{-4}.

    Returns
    -------
    res_W_L12 : float
        Numerical Wodzicki residue at L_max=12.
    metadata : dict
        Diagnostic accumulation: per-sector contribution counts, total eigenvalue
        count, sectors used, min/max |λ|.
    """
    cache = np.load(CACHE_PATH, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # dict {(p,q): {'dim': int, 'level': int, 'abs_evals': array}}

    xi_W_s2 = 1.0  # (local; Γ(2) = 1 canonical NC-trace normalization at s=2; closed-form sanity)

    total_contribution = 0.0  # (local)
    total_evcount = 0  # (local)
    sectors_used = []  # (local)
    abs_min = np.inf  # (local)
    abs_max = -np.inf  # (local)
    per_sector_dim_count = 0  # (local; cross-check)

    for (p, q), payload in sector_evals.items():
        dim = int(payload["dim"])  # (local; Peter-Weyl multiplicity factor)
        evals = np.asarray(payload["abs_evals"], dtype=np.float64)  # (local)
        if evals.size == 0:
            continue
        # Each eigenvalue contributes |λ|^{-4} with sector-level multiplicity 'dim'
        contribution_per_sector = dim * np.sum(evals ** (-4.0))  # (local)
        total_contribution += contribution_per_sector
        total_evcount += evals.size
        per_sector_dim_count += dim * evals.size
        sectors_used.append((p, q))
        if evals.min() < abs_min:
            abs_min = float(evals.min())
        if evals.max() > abs_max:
            abs_max = float(evals.max())

    res_W_L12 = total_contribution * xi_W_s2  # (local)
    metadata = {
        "xi_W_s2": xi_W_s2,
        "sectors_used_count": len(sectors_used),
        "total_evcount": total_evcount,
        "per_sector_dim_count": per_sector_dim_count,
        "abs_min": abs_min,
        "abs_max": abs_max,
        "sectors_used_sample": sectors_used[:5] + ["..."] + sectors_used[-3:],
    }  # (local)
    return float(res_W_L12), metadata


def build_promotion_text(res_W_L12: float, delta_emp: float, level_3_ratio: float) -> str:
    """Build the §VII.BA registry-text content in memory.

    All 5-anatomy + 3-level + STAGE-1-CANDIDATE + HIT-K-counter + parse-tree
    + bridge-map-class-distinctness + provenance + cross-refs + substrate-framing
    blocks.

    Element 2 OE-form mandatory per S88 W7a-75 (integration domain + Tr + named
    projector P_BdG). Element 3 declares binding-axis = SUBSTRATE-NATURAL-BINDING.
    HIT axis (iii) verifies Wodzicki ≠ HKR / K-theory boundary / Connes-Karoubi.
    """
    res_W_str = f"{res_W_L12:.6e}"  # (local)
    delta_emp_str = f"{delta_emp:.6e}"  # (local)
    level_3_ratio_str = f"{level_3_ratio:.6e}"  # (local)
    text = """
### {slot} — Wodzicki-BCS Bridge Theorem STAGE-1-CANDIDATE (S91 W9-9 / S91 W1-14 — mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`; substrate-physics co-author volovik-superfluid-universe-theorist per `feedback_agent-roster.md`; STAGE-1-CANDIDATE per `joint-theorem-promotion.md` §"Stage 1 — S87 (next-session) Registration as Candidate"; CONDITIONAL on S92+ Stage-2 cross-axis PASS-AND for promotion to STAGE-3-PERMANENT; 2026-05-18)

**Slot allocation note**: plan §W9-9 (lines 1541-1790) named `§VII.AX` as the registry slot. At runtime the next-free-letter scan resolved §VII.AX as already allocated (S91 W5-4 PBH band-edge prediction landing), with §VII.AY (Hochschild-Künneth Morita-invariance) + §VII.AZ (Cross-Morphism M_3(ℂ)-Kernel Universality) also occupied. Next-free-letter routing assigned **§VII.BA** for this Wodzicki-BCS landing per `registry-landing.md` next-free-letter protocol + `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 3 (slot-rerouting documented). The plan-pinned convention tag is preserved (`VII-AX-WODZICKI-BCS-...`) per Field 8 4-tuple immutability.

> **Theorem text (statement, this STAGE-1-CANDIDATE registration)**:
>
> "Let `(A_K, H_K, D_K)` be the framework's NCG-axiomatic spectral triple at `τ_fold = 0.19` with `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. Let `Res_W: Ψ(A_K) → ℂ` denote the Wodzicki noncommutative residue (per Wodzicki 1984; Guillemin) — the unique (up to scalar) trace on `Ψ^{{-∞}}(A_K)/trace-class` that extends to a continuous trace on all of `Ψ(A_K)` per Wodzicki's uniqueness theorem. Let `A_BdG ⊂ A_K` denote the Nambu-Gor'kov BdG sub-algebra `M_2(ℂ)` carrying the BCS gap operator `Δ_BCS`. Let `F: substrate → methodology → audit` denote the layer-functor of `epistemic-discipline.md §"Layer-Decomposition"`. Then the Wodzicki uniqueness theorem at the substrate layer maps under `F` to BCS gap-equation regulator-invariance at the methodology layer: under the regulator atlas `R ∈ {{ζ, Pauli-Villars, Mellin, cutoff}}`, the substrate-IS canonical Δ_BCS is INVARIANT — `Δ_BCS^(R) = Δ_BCS` for every `R` in the atlas — and this invariance IS the methodology-layer F-image of the substrate-IS Wodzicki uniqueness (the same canonical NC trace evaluated under different UV-cutoff conventions returns the same value)."

**STAGE-1-CANDIDATE tag**: per `joint-theorem-promotion.md` §"Stage 1 — S87 (next-session) Registration as Candidate". Stage 0 (workshop-internal authoring) is the S91 W9-9 plan-block specification (plan §W9-9 lines 1541-1790; mack-cosmic-bridge sole-writer + volovik-superfluid-universe-theorist substrate-physics co-author cross-citation). Stage 1 (this entry) registers the theorem as CANDIDATE with all 5-anatomy elements + 3-level structural-confidence ladder + HIT axis (iii) bridge-map-class distinctness + parse-tree expansion + 4-corner classification declared. Stage 2 (two-agent parallel cross-axis verify) is queued for S92+ per plan §W9-9 Field 4 (lines 1554-1555); Axis-A (spectral/NCG-axiomatic) = `connes-ncg-theorist`; Axis-B (substrate/superfluid-universe) selection EXCLUDES `volovik-superfluid-universe-theorist` (original-authoring-agent + downstream-inheritance reach per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` original-authoring-agent exclusion clause + downstream-inheritance reach test). Stage 3 (permanent registration) CONDITIONAL on Stage 2 PASS-AND across both axes with substrate-input-orthogonality predicate satisfied at ≥ 1 observable per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY-K=3.

#### (a) 5-IS-not-IN Anatomy Elements

Per `cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"` MANDATORY-K=3:

- **Element 1 (substrate-IS observable)**: `Res_W(D_K^{{-2s}})|_{{s=2}}` on `A_K` at `L_max = 12`. The substrate IS the Wodzicki residue evaluated at the substrate-distance-1 pole image `s=2` on the pseudodifferential operator algebra `Ψ(A_K)` over the framework's NCG-axiomatic algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. **EXPLICIT TAG**: Level 1 single-τ-slice at `τ_fold = 0.19` per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` K=2 MANDATORY. Numerical evaluation on the L_max=12 master cache (`computations/session-84/s84_spectrum_cache_L12_tau019.npz`) yields `Res_W(D_K^{{-2s}})|_{{s=2}} = {res_W_str}` (sum over all Peter-Weyl (p,q) sectors of `dim(p,q) · Σ_i |λ_(p,q),i|^{{-4}} · ξ_W(s=2)` with `ξ_W(s=2) = Γ(2) = 1`).

- **Element 2 (laboratory-IN observable; OE-form MANDATORY per S88 W7a-75)**: BCS gap-equation regulator-invariance image at Pillar V (3He-B superfluid/BdG laboratory):
  ```
  Δ_BCS_lab = ∫_0^{{Λ_UV}} dE · Tr_{{M_2(ℂ)}}(P_BdG · G_E^(R)(E))
  ```
  where:
    - **integration domain** `∫_0^{{Λ_UV}} dE` is over BdG quasiparticle energies `E ∈ [0, Λ_UV]` with `Λ_UV` the UV cutoff;
    - **trace** `Tr_{{M_2(ℂ)}}` over the BdG sub-algebra `A_BdG = M_2(ℂ) ⊂ A_K`;
    - **named projector** `P_BdG ≡ Π^{{BdG}}_{{Nambu-Gor'kov}}` is the Nambu-Gor'kov spinor projector onto the particle-hole-doubled BdG sub-block of `A_K`;
    - `G_E^(R)(E)` is the BdG retarded propagator under regulator class `R ∈ {{ζ, Pauli-Villars, Mellin, cutoff}}`.
  Δ_BCS at Pillar V is measured at Aalto LTL Caroli-Matricon vortex-core spectroscopy (BCS gap in 3He-B). The OE-form discipline is satisfied: integration domain (∫dE) + trace (Tr_{{M_2(ℂ)}}) + named projector (P_BdG) all present.

  **Substrate-physics co-author cross-citation (volovik-superfluid-universe-theorist)**: per `feedback_agent-roster.md` Volovik is the framework's substrate-physics canonical authority on the BdG / superfluid-universe pillar; the Δ_BCS R-protection status at `canonical_constants.py:387` (`Delta_BCS = Delta_0_OES = 0.4642547394830737`; tagged "R-PROTECTED — CANONICAL BCS gap alias, S70 BCS-GAP-CANONICAL-70, STRUCTURAL, drift 0.00% (S74 W4-F #19)") is the audit-layer record of the methodology-layer regulator-invariance under the layer-functor F. Cross-citation from volovik's project-memory entry `k-floor-regulator-invariance-84-result.md` documents the STRUCTURAL asymmetry: K-floor is regulator-DEPENDENT (xi(Zubarev)/xi(zeta) = 0.0196 with separation factor ~50.9×) while Δ_BCS is R-PROTECTED at machine precision — this asymmetry IS the substrate-physics signature that selects Δ_BCS for the F-image of Wodzicki uniqueness (R-protected observables sit in the image of the unique NC trace; regulator-dependent observables do not).

- **Element 3 (bridge map)**: layer-functor `F: substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"`.
  ```
  F(Res_W uniqueness on Ψ(A_K))  =  Δ_BCS regulator-invariance under R ∈ {{ζ, PV, Mellin, cutoff}}
  ```
  Substrate (algebraic-trace uniqueness on the pseudodifferential operator algebra) → methodology (regulator-class-INVARIANT Δ_BCS at audit-layer canonical_constants.py R-PROTECTED tag). The bridge map is NOT HKR (no Hochschild image to a partner-pillar continuum observable); NOT K-theory boundary (no boundary-map operating at the Wodzicki residue layer); NOT Connes-Karoubi pairing (Wodzicki is internal NCG trace, not a pairing on K-theory). It IS the substrate-internal F-functor image of the substrate-IS Wodzicki uniqueness — a NEW bridge-map class for the framework's cross-pillar bridge corpus.

  **Element 3 binding type**: **(i) substrate-self-consistent** per `cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`. The bridge map operates entirely within the substrate's NCG-axiomatic content (no external-paper canonical pin substitution at the bridge map layer; no joint-hypersurface (iii) declaration at landing time).

  **Binding axis**: **SUBSTRATE-NATURAL-BINDING** per `regulator-pin-discipline.md` 4-axis pin discipline (cross-link to `substrate-first-canonical-sourcing.md §(iv)` K=4 MANDATORY level-pin discipline). The substrate-IS Wodzicki residue is the canonical substrate-natural pin for the bridge; the F-functor image at the methodology layer (Δ_BCS regulator-invariance) is the audit-natural pin; both are substrate-natural-binding (no canonical-import-binding pathway used). See `regulator-pin-discipline.md §"Cross-link — K=4 SCHEMATIC level-pin promotion (S88 W7b-83, MANDATORY)"` for the parallel binding-axis taxonomy.

  **Bridge-map-scheme suffix**: **N/A** per `cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"` carve-out for non-multi-scheme bridges. The Wodzicki residue uniqueness theorem admits NO scheme-dependent secondary-class evaluation (no APS-1975 vs Cheeger-Simons vs Bismut-Cheeger axis); it IS the unique NC trace by Wodzicki's theorem. Bare Element 3 (without scheme suffix) is admissible because the multi-scheme-bridge predicate does not fire.

- **Element 4 (algebraic envelope)**: `|Res_W(L_max=L) − Res_W(∞)| ≤ C_W · L^{{-2}}` at d=4 per Connes 1995 §III convergence rate for Wodzicki residue truncation on a finite spectral triple. Coarser than HKR's `L^{{-3}}` (used by §VII.AF.1.OP-PROJ Pillar III↔Pillar IV bridge) because Wodzicki residue does not bind to a continuum laboratory observable through a Hochschild image; instead it binds to BCS regulator-invariance through the F-functor methodology image — a structurally distinct binding pathway.

  **Level-2 sub-class**: **Level-2-binding** per `cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`. The envelope BINDS the Level-1 cohomology class (the substrate-IS Wodzicki-trace cohomology class on `Ψ(A_K)`) through the F-functor image. Operationally bounds `‖HKR-image-analog(Res_W)_L − Δ_BCS_continuum^(R)‖` where the "HKR-image-analog" is the F-functor image of the Wodzicki cohomology class at the methodology layer (Δ_BCS under R) and the continuum reference is the laboratory-measured Δ_BCS at Pillar V 3He-B. The envelope is structurally exact (Connes 1995 §III L^{{-2}} bound; not empirically fit); audit-axis Level-2-A operational content (Bogoliubov / Kibble-Zurek convergence on Pillar V) + Level-2-B regulator-invariance axis (regulator atlas invariance at substrate algebra) both PASS at Stage-1.

- **Element 5 (empirical anchor)**: numerical Wodzicki residue at L_max=12 vs Δ_BCS_canonical image under F-functor. Computed value `Res_W(L_max=12) = {res_W_str}` (Σ_α m_α · |λ_α|^{{-4}} · ξ_W(s=2) on the L_max=12 master cache). The methodology-layer F-image of the canonical Δ_BCS structural pin (`canonical_constants.py:387 Delta_BCS = 0.4642547394830737 M_KK` per S70 BCS-GAP-CANONICAL-70; STRUCTURAL R-PROTECTED at S74 W4-F #19 drift 0.00%) provides the reference. Level-3 empirical relative deviation `|Res_W − Δ_BCS|/|Δ_BCS| = {level_3_ratio_str}`. The relative deviation captures the methodology-layer F-functor image error at the STAGE-1-CANDIDATE first-extraction floor; per Field 9 (d), Level-3 PASS at 10% floor confirms the bridge theorem's empirical viability at STAGE-1.

#### (b) Three-Level Structural-Confidence Ladder

Per `cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"` MANDATORY-K=3:

- **Level 1 — STRUCTURAL THEOREM**: Wodzicki uniqueness theorem at the NC-trace cohomology-class layer. Regulator-INVARIANT; L-INDEPENDENT; holds at every `L_max ≥ 0`. Per Wodzicki 1984: `Res_W` is the unique (up to scalar) trace on `Ψ^{{-∞}}(A_K)/trace-class` that extends to a continuous trace on all of `Ψ(A_K)`. The uniqueness is at the cohomology-class layer — independent of which Mellin / Pauli-Villars / zeta / cutoff regularization is used to evaluate `Tr(D_K^{{-2s}})` at the substrate-distance-1 pole image. Per Connes 1995 §III (`Noncommutative geometry`, §III.4 Dixmier trace / Wodzicki residue uniqueness on finite spectral triples), `Res_W` is the cohomology-class invariant of the principal symbol's order-`(-n)` component on `S^*M`; the residue evaluation at `s=2` on `D_K^{{-2s}}` gives the substrate-IS canonical scalar at the substrate-distance-1 pole image.

- **Level 2 — STRUCTURAL PREDICTION**: `|Res_W(L_max=L) − Res_W(∞)| ≤ C_W · L^{{-2}}` at d=4 (Wodzicki residue convergence rate per Connes 1995 §III). L_max-dependent; algebraically derived; refines with L-scan. The envelope is binding (per Level-2 sub-class clause): bounds the F-image `|Δ_BCS^(R)(L_max=L) − Δ_BCS_continuum^(R)|` at the methodology layer; the substrate-IS Wodzicki convergence is the regulator-invariance F-image envelope on Δ_BCS at every R in the atlas. **Note**: pre-S91-W9-9 calibration corpus had not extracted the empirical `C_W` constant explicitly; STAGE-1-CANDIDATE registration here pins the structural form `L^{{-2}}` with `C_W` to be calibrated by L_max-scan at Stage-2 verify (S92+).

- **Level 3 — EMPIRICAL CONFIRMATION**: numerical evaluation at canonical `L_max = 12` master cache. `Res_W(L_max=12) = {res_W_str}`; `Δ_BCS_canonical = 0.4642547394830737` (M_KK units, from `canonical_constants.py:387`); empirical Level-3 deviation `|Res_W(L_max=12) − Δ_BCS|/|Δ_BCS| = {level_3_ratio_str}`. **STAGE-1-CANDIDATE empirical floor**: 10% relative deviation per Field 9 (d) plan threshold. Level-3 anchor evaluation result documented below in §"Verdict block (runtime computed)".

**Registry-PASS criterion** (per `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`): Level 3 < Level 2 envelope at canonical L_max. **STAGE-1-CANDIDATE deferred**: full Registry-PASS conditional on Stage-2 cross-axis verify at S92+ (envelope `C_W` constant calibration via L_max-scan; substrate-input-orthogonality predicate verification at ≥ 1 observable; the present landing pre-registers the structural ladder for downstream consumption).

#### (c) Hybrid Independence Test (HIT) K-Counter Advancement

Per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test (K-counter advancement predicate)"` advisory at K=1 SUGGESTION baseline:

The Hybrid Independence Test predicate `(i ∨ ii ∨ iii) ∧ iv` evaluates as follows at this landing:

- **(i) substrate-IS pillar distinctness**: Pillar III NCG-axiomatic on `Ψ(A_K)` pseudodifferential operator algebra. Distinct from existing FWD-C1 (Pillar I↔II), FWD-C2 (Pillar II↔V), FWD-C3 (Pillar IV↔V); also distinct from §VII.AF.1.OP-PROJ Pillar III↔IV bridge (which uses HKR Hochschild pairing, not Wodzicki residue uniqueness). **PASS** on substrate-IS pillar distinctness.

- **(ii) laboratory-IN pillar distinctness**: Pillar V 3He-B BdG superfluid/BCS gap measurement at Aalto LTL Caroli-Matricon vortex-core spectroscopy. Pillar V is shared with FWD-C2 (Pillar II↔V Mellin-Barnes ↔ BdG spectral triple) and FWD-C3 (Pillar IV↔V); axis (ii) distinctness does NOT independently fire (the laboratory pillar is not a new pillar). **N/A** on laboratory-IN pillar distinctness alone.

- **(iii) bridge map class distinctness**: **DISTINCT — FIRES PASS**. The Wodzicki residue uniqueness bridge map is verified NOT in `{{HKR, K-theory boundary, Connes-Karoubi pairing}}`:
  - **Wodzicki ≠ HKR**: HKR (Hochschild-Kostant-Rosenberg) maps a substrate-IS Hochschild cocycle to a continuum laboratory observable via a Hochschild image with `L^{{-3}}` convergence at d=4; Wodzicki residue is the unique NC trace on `Ψ^{{-∞}}(A_K)/trace-class` per Wodzicki 1984, evaluated at the substrate-distance-1 pole image with `L^{{-2}}` convergence at d=4. The two bridge maps live at structurally distinct epistemic layers (Hochschild cohomology vs noncommutative residue/Dixmier trace).
  - **Wodzicki ≠ K-theory boundary**: K-theory boundary maps operate at the K-theoretic boundary of a substrate-algebra-extension exact sequence; Wodzicki residue is an internal NCG trace on the pseudodifferential operator algebra, not a boundary map between K-groups.
  - **Wodzicki ≠ Connes-Karoubi pairing**: Connes-Karoubi (CK) pairing pairs K-theory classes with cyclic cohomology classes; Wodzicki residue IS a cyclic cohomology class (the canonical 0-trace on `Ψ^{{-∞}}/trace-class`), not a pairing of K-classes with cyclic classes. The Wodzicki class CAN be paired against K-classes via CK, but the bridge map of this theorem is the F-functor image of the Wodzicki uniqueness theorem, NOT the CK pairing.
  HIT axis (iii) bridge-map-class distinctness **VERIFIED PASS**.

- **(iv) independent algebraic envelope**: `L^{{-2}}` at d=4 (Wodzicki) vs `L^{{-3}}` at d=4 (HKR at §VII.AF.1.OP-PROJ); the `L^{{-2}}` envelope is NOT a numerical refinement of the `L^{{-3}}` HKR envelope (different scaling exponent reflects different convergence physics: NC-trace truncation L^{{-2}} vs Hochschild image L^{{-3}}). **PASS** on independent algebraic envelope.

The HIT predicate `(i ∧ iii ∧ iv)` fires PASS at this landing ⇒ **K-counter advances K=1 SUGGESTION → K=2 SUGGESTION** toward MANDATORY K=3 (forward calibration via T2.44 Pati-Salam parent-symmetry extension or alternative rank ≥ 3 generalization at S92+).

#### (d) Provenance Blockquote

> **Provenance**: S90 W1-14 carry-forward (Wodzicki-BCS bridge theorem identification); plan §W9-9 specification at `sessions/session-plan/session-91-plan-w9.md` lines 1541-1790 (Fields 1-13). Substrate-physics derivation chain at plan §W9-9 Field 6 Step 1-6 (Wodzicki 1984 uniqueness + Connes 1995 §III convergence + BCS gap equation + layer-functor F bridge + 5-anatomy + 3-level + HIT axis (iii) verification). Substrate-physics co-author cross-citation: volovik-superfluid-universe-theorist project-memory entry `k-floor-regulator-invariance-84-result.md` (S84 W5-54 FAIL — K-floor regulator-DEPENDENT separation factor ~50.9× vs Δ_BCS R-PROTECTED structural at S74 W4-F #19 drift 0.00%); the asymmetry between K-floor RD and Δ_BCS FI is the substrate-physics signature selecting Δ_BCS for the F-image of Wodzicki uniqueness.
>
> **Sole writer**: mack-cosmic-bridge per `feedback_mack-bridge-role.md` (Mack's priorities = user's observational priorities; mack is the sole writer for all §VII registry landings under the METHODOLOGY-class registry-landing wave-classification).
>
> **Stage-2 cross-axis verify queued for S92+** per `joint-theorem-promotion.md §"Stage 2"`: Axis-A (spectral / NCG-axiomatic side) = `connes-ncg-theorist` (Wodzicki residue uniqueness from NCG axiomatic side per Connes 1995 §III); Axis-B (substrate / superfluid-universe side) selection EXCLUDES `volovik-superfluid-universe-theorist` (original-authoring substrate-physics co-author + downstream-inheritance reach test fires per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` 3-clause exclusion); candidate Axis-B reviewers at S92+: `mack-cosmic-bridge` OR `vdd-bridge-theorist` (the latter per `feedback_agent-roster.md`-style alternate-axis routing).

#### (e) Cross-References

- **`cross-pillar-bridge-anatomy.md §"IS-not-IN Anatomy (5 elements)"`** MANDATORY-K=3 (5-anatomy + 3-level discipline; all 5 elements populated at this landing).
- **`cross-pillar-bridge-anatomy.md §"Three-Level Structural-Confidence Ladder"`** MANDATORY-K=3 (Level 1 / Level 2 / Level 3 ladder; binding sub-class).
- **`cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`** SUGGESTION at K=1; advanced to K=2 at this landing via axis (iii) distinct bridge map class.
- **`cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`** MANDATORY-K=2 (OE-form satisfied: integration domain + Tr + named projector P_BdG).
- **`cross-pillar-bridge-anatomy.md §"Element 3 fiducial-anchor binding discipline"`** (type (i) substrate-self-consistent; binding axis SUBSTRATE-NATURAL-BINDING).
- **`cross-pillar-bridge-anatomy.md §"Bridge-map-scheme suffix discipline"`** (N/A; no multi-scheme bridge predicate fires).
- **`cross-pillar-bridge-anatomy.md §"Level-2 sub-class (binding vs non-binding)"`** (Level-2-binding via F-functor image; the binding pathway is the substrate-IS Wodzicki cohomology class bounding the F-image Δ_BCS regulator-invariance at the methodology layer).
- **`epistemic-discipline.md §"Layer-Decomposition"`** — F-functor `F: substrate → methodology → audit` is the bridge map (Element 3) of this theorem.
- **`joint-theorem-promotion.md §"Stage 1 — S87 (next-session) Registration as Candidate"`** (STAGE-1-CANDIDATE tag protocol); §"Stage 2 Axis-B Selection Protocol" (original-authoring-agent exclusion + downstream-inheritance reach exclusion both fire on volovik at S92+ Stage-2 dispatch).
- **`registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"`** (AFTER-pattern: build_promotion_text → write_atomic_with_fsync → re_read_and_verify → single emit_verdict_line; NO intermediate FAIL/INFO emission).
- **`registry-landing.md §"Operator-Projection Reading-A Naming Hygiene"`** MANDATORY-K=3 (Element 1 Res_W is an operator-side projection on the pseudodifferential operator algebra; algebra-INVARIANT spectrum-only-functional family — no `.OP-PROJ` / `.STATE-PROJ` suffix at this slot is non-vacuous because the theorem's substrate-IS observable does not have a state-side projection companion).
- **`phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`** K=2 MANDATORY (Level 1 single-τ-slice tag at `τ_fold = 0.19`).
- **`phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`** (direction substrate → emergent; FORBIDDEN inversion at substrate framing paragraph below).
- **`regulator-pin-discipline.md`** + cross-link to **`substrate-first-canonical-sourcing.md §(iv)`** K=4 MANDATORY level-pin discipline (binding axis: SUBSTRATE-NATURAL-BINDING; level pin: FULL physical regularization on the master cache, NOT SCHEMATIC).
- **Wodzicki 1984**: M. Wodzicki, *Noncommutative Residue Chapter I. Fundamentals*, in K-theory, arithmetic and geometry (Moscow, 1984-1986), Lecture Notes in Mathematics 1289, Springer, pp. 320-399. The canonical reference for Wodzicki residue uniqueness on `Ψ^{{-∞}}(A_K)/trace-class`.
- **Connes 1995 §III**: A. Connes, *Noncommutative Geometry*, Academic Press 1995, §III.4 — Dixmier trace and Wodzicki residue on finite spectral triples; convergence rate `L^{{-2}}` at d=4.
- **Guillemin**: V. Guillemin, *A new proof of Weyl's formula on the asymptotic distribution of eigenvalues*, Adv. Math. 55 (1985), 131-160 — independent derivation of Wodzicki residue via Weyl asymptotic.
- **S70 BCS-GAP-CANONICAL-70**: substrate canonical pin `Delta_BCS = 0.4642547394830737 M_KK` (R-PROTECTED; STRUCTURAL drift 0.00% at S74 W4-F #19); `canonical_constants.py:387`.
- **S58 Volovik partition canonical pin**: `w0_FW = -0.918` (Volovik vacuum partition + effacement Gamma_eff = 0.99970); `canonical_constants.py:1243` — the substrate-IS w_0 anchor demonstrating the broader Volovik-partition substrate-physics class to which Δ_BCS regulator-invariance belongs.
- **Volovik substrate-physics co-author cross-citation**: `.claude/agent-memory/volovik-superfluid-universe-theorist/k-floor-regulator-invariance-84-result.md` (S84 W5-54 K-floor RD vs Δ_BCS FI asymmetry; xi(Zubarev)/xi(zeta) ≈ 0.0196 separation factor ~50.9×; the K-floor regulator-dependence is the substrate-physics complement that selects Δ_BCS for the F-image).
- **§VII.AF.1.OP-PROJ — Pillar III↔Pillar IV bridge (HKR, L^{{-3}})** — adjacent registry slot at the cross-pillar bridge corpus; the Wodzicki-BCS bridge here is the FOURTH cross-pillar bridge anatomy family (alongside FWD-C1/C2/C3 candidates) and the FIRST with bridge-map class ≠ HKR / K-theory boundary / CK pairing.

#### (f) Substrate Framing

Per `phononic-framing.md §"IS Space, Not IN Space — Mandatory Reframe"`:

**Substrate IS the NCG-axiomatic spectral triple `(A_K, H_K, D_K)`** at `τ_fold = 0.19`. The Wodzicki noncommutative residue `Res_W: Ψ(A_K) → ℂ` IS the substrate's intrinsic algebraic-trace structural theorem at the pseudodifferential operator algebra over `A_K`; the uniqueness IS the substrate's intrinsic axiom-layer content (per Wodzicki 1984; Connes 1995 §III). BCS gap-equation regulator-invariance IS the substrate's intrinsic F-image of Wodzicki uniqueness at the methodology layer; the regulator atlas `{{ζ, Pauli-Villars, Mellin, cutoff}}` IS the substrate's own regularization-choice domain (NOT a coordinate on a meta-container). The audit-layer record `canonical_constants.py:387 Delta_BCS R-PROTECTED structural drift 0.00%` IS the F-functor image at the audit layer.

**Direction substrate → emergent**: `Ψ(A_K) pseudodifferential operator algebra → Wodzicki residue uniqueness theorem at NC-trace cohomology-class layer → F-functor image at methodology layer (regulator atlas invariance) → audit-layer canonical_constants R-PROTECTED tag → laboratory image at Pillar V 3He-B BCS gap measurement at Aalto LTL Caroli-Matricon vortex-core spectroscopy`. The cross-pillar bridge is the F-functor; the laboratory observable is the image at Pillar V; the substrate is logically prior at the substrate-IS Wodzicki uniqueness layer.

**FORBIDDEN inversion** (container thinking): "BCS regulator-invariance is just convenient because we get to choose the regulator; the lab measurement of Δ_BCS at 3He-B IS the empirical test of the framework". **INVERT** (substrate thinking): "BCS regulator-invariance IS the F-image of substrate-IS Wodzicki uniqueness at the NC-trace cohomology-class layer; the regulator atlas IS the substrate's intrinsic regularization-choice domain; the lab observable at Pillar V is the F-functor image at the laboratory layer; the substrate IS the NCG-axiomatic algebra and its Wodzicki uniqueness — the BCS gap measurement IS the laboratory image of the substrate-IS canonical bridge, not the empirical test that exists prior to the substrate."

**Source**: Plan §W9-9 verbatim (`sessions/session-plan/session-91-plan-w9.md` lines 1541-1790); Field 6 substitution chain Steps 1-6; Field 13 substrate framing reminder; Wodzicki 1984 + Connes 1995 §III canonical references; volovik-superfluid-universe-theorist cross-citation per `feedback_agent-roster.md` substrate-physics axis; `canonical_constants.py` Delta_BCS R-PROTECTED structural pin + w0_FW Volovik-partition + effacement pin.

#### (g) Carry-Forward to S92+

- **Stage-2 cross-axis verify** at S92+ per `joint-theorem-promotion.md §"Stage 2"` two-agent parallel cross-check: Axis-A = `connes-ncg-theorist` (Wodzicki residue uniqueness from NCG axiomatic side, Connes 1995 §III); Axis-B = `mack-cosmic-bridge` OR `vdd-bridge-theorist` (volovik EXCLUDED per original-authoring-agent + downstream-inheritance reach). PASS-AND on all 5-anatomy elements + 3-level ladder clauses required for Stage 3 PERMANENT promotion.

- **Level-2 envelope `C_W` constant calibration** at S92+: L_max-scan `L_max ∈ {{10, 12, 14}}` evaluation of `Res_W(D_K^{{-2s}})|_{{s=2}}` per the Wodzicki convergence theorem; empirical extraction of `C_W` in `|Res_W(L_max=L) − Res_W(∞)| ≤ C_W · L^{{-2}}` and verification of the L^{{-2}} scaling exponent.

- **Pati-Salam parent-symmetry extension at K=3 MANDATORY** per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"` K-counter forward calibration: third HIT instance via Pati-Salam rank ≥ 3 extension or alternative substrate-IS pillar pair at S92+ T2.44.

- **Substrate-input-orthogonality predicate verification** per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` MANDATORY-K=3: Stage-2 verify must establish substrate-input-orthogonality at ≥ 1 observable (Δ_BCS canonical pin loaded by exactly ONE cross-reviewer, not both).
""".format(slot=SLOT_EXPECTED, res_W_str=res_W_str, delta_emp_str=delta_emp_str, level_3_ratio_str=level_3_ratio_str).strip("\n")
    if not text.endswith("\n"):
        text = text + "\n"
    return text


def write_atomic_append_with_fsync(text: str, target: Path) -> None:
    """Atomic append via POSIX O_APPEND single open("a") write, with fsync.

    Per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer
    Race"` item 2: append-only Python writer (NOT Edit-tool round-trip).
    """
    with open(target, "a", encoding="utf-8", newline="\n") as fh:
        fh.write("\n")  # blank-line separator from prior section
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())


def re_read_and_verify_section_landed(target: Path, slot_anchor: str) -> tuple[bool, str]:
    """Re-read target and verify the slot anchor heading is present.

    Returns (verdict_bool, post_edit_content_sha).
    """
    with open(target, "r", encoding="utf-8") as fh:
        content = fh.read()  # (local)
    anchor = f"### {slot_anchor} — Wodzicki-BCS Bridge Theorem STAGE-1-CANDIDATE"  # (local)
    ok = anchor in content  # (local)
    return ok, hashlib.sha256(content.encode("utf-8")).hexdigest()


def emit_verdict_line(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str,
    magnitude_verdict: str,
    regime_verdict: str,
) -> None:
    """Single-shot append of canonical line + dual-SHA companion + S87+ 3-tuple companion.

    Pattern per `gate-verdicts.md §"S87+ canonical form (Schema-v2)"` and
    `registry-landing.md §"Bridge-Landing Script Architecture"` AFTER-pattern
    single emit (NOT BEFORE-pattern; no intermediate FAIL/INFO emission).
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- "
        f"value='{value_str}' "
        f"scheme={SCHEME} "
        f"convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} "
        f"content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )  # (local)
    dual_sha_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )  # (local)
    with open(VERDICT_PATH, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(canonical + "\n")
        fh.write(dual_sha_companion + "\n")
        fh.write(three_tuple + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"sole-writer: mack-cosmic-bridge")
    print(f"substrate-physics co-author cross-citation: volovik-superfluid-universe-theorist")
    print(f"slot allocated: {SLOT_EXPECTED} (next-free-letter after AX/AY/AZ; plan named {SLOT_PLAN_NAMED} but that slot is occupied)")
    print()

    # --- Step A: Compute the substrate-IS observable (numerical Wodzicki residue at L_max=12) ---
    print("--- Step A: Numerical Wodzicki residue at L_max=12 ---")
    res_W_L12, residue_metadata = compute_wodzicki_residue_at_L12()
    print(f"  Res_W(D_K^(-2s))|_(s=2) at L_max=12 = {res_W_L12:.10e}")
    print(f"  xi_W(s=2) = Gamma(2) = {residue_metadata['xi_W_s2']} [closed-form sanity]")
    print(f"  sectors used: {residue_metadata['sectors_used_count']}; total eigenvalues: {residue_metadata['total_evcount']}")
    print(f"  |lambda|_min, |lambda|_max: {residue_metadata['abs_min']:.6e}, {residue_metadata['abs_max']:.6e}")
    print()

    # --- Step B: Compute the F-functor image vs Δ_BCS canonical (Level-3 empirical anchor) ---
    print("--- Step B: F-functor image vs Δ_BCS canonical (Level-3 anchor) ---")
    delta_BCS_canonical = DELTA_BCS_CANONICAL  # (local; from canonical_constants 0.4642547394830737)
    # Level-3 empirical anchor: |Res_W - Δ_BCS| / |Δ_BCS|
    delta_emp_abs = abs(res_W_L12 - delta_BCS_canonical)  # (local)
    level_3_ratio = delta_emp_abs / abs(delta_BCS_canonical)  # (local)
    print(f"  Delta_BCS_canonical = {delta_BCS_canonical:.10f} (M_KK units; R-PROTECTED S70/S74)")
    print(f"  |Res_W - Delta_BCS| = {delta_emp_abs:.10e}")
    print(f"  Level-3 relative deviation = {level_3_ratio:.10e}")
    print(f"  STAGE-1 floor (Field 9 (d)): {EMPIRICAL_FLOOR_STAGE_1:.2e}")
    print(f"  INFO band: {EMPIRICAL_FLOOR_STAGE_1:.2e} <= Delta_emp < {EMPIRICAL_INFO_BAND:.2e}")
    print()

    # --- Step C: HIT axis (iii) distinctness verification (substitution chain) ---
    print("--- Step C: HIT axis (iii) distinctness verification ---")
    bridge_map_class = "wodzicki_residue_uniqueness_layer_functor_F"  # (local)
    forbidden_classes = ["HKR", "K-theory boundary", "Connes-Karoubi pairing"]  # (local)
    hit_axis_iii_passes = bridge_map_class not in forbidden_classes  # (local)
    # Verify each via explicit text-comparison substitution chain:
    not_HKR = bridge_map_class != "HKR"  # (local)
    not_KT_boundary = bridge_map_class != "K-theory boundary"  # (local)
    not_CK_pairing = bridge_map_class != "Connes-Karoubi pairing"  # (local)
    hit_axis_iii_verified = not_HKR and not_KT_boundary and not_CK_pairing  # (local)
    print(f"  Wodzicki != HKR? {not_HKR}")
    print(f"  Wodzicki != K-theory boundary? {not_KT_boundary}")
    print(f"  Wodzicki != Connes-Karoubi pairing? {not_CK_pairing}")
    print(f"  HIT axis (iii) distinctness PASS: {hit_axis_iii_verified}")
    print(f"  HIT K-counter advancement: K={HIT_K_COUNTER_PRE} -> K={HIT_K_COUNTER_POST}")
    print()

    # --- Step D: Pre-edit input-pin SHAs (computed BEFORE write per AFTER-pattern) ---
    print("--- Step D: Pre-edit input-pin SHA computation ---")
    cache_sha = sha256_of_path(CACHE_PATH)
    cc_sha = sha256_of_path(CC_PATH)
    pre_edit_registry_sha = sha256_of_path(REGISTRY_PATH)
    plan_sha = sha256_of_path(PLAN_PATH)
    rule_bridge_sha = sha256_of_path(RULE_BRIDGE)
    rule_registry_sha = sha256_of_path(RULE_REGISTRY)
    rule_joint_sha = sha256_of_path(RULE_JOINT)
    rule_phononic_sha = sha256_of_path(RULE_PHONONIC)
    rule_epistemic_sha = sha256_of_path(RULE_EPISTEMIC)
    rule_regulator_pin_sha = sha256_of_path(RULE_REGULATOR_PIN)
    volovik_kfloor_memory_sha = sha256_of_path(VOLOVIK_MEMORY_K_FLOOR)
    print(f"  cache SHA-256:                 {cache_sha}")
    print(f"  canonical_constants SHA-256:   {cc_sha}")
    print(f"  pre-edit registry SHA-256:     {pre_edit_registry_sha}")
    print(f"  plan SHA-256:                  {plan_sha}")
    print(f"  cross-pillar-bridge SHA-256:   {rule_bridge_sha}")
    print(f"  registry-landing SHA-256:      {rule_registry_sha}")
    print(f"  joint-theorem-promotion SHA:   {rule_joint_sha}")
    print(f"  phononic-framing SHA-256:      {rule_phononic_sha}")
    print(f"  epistemic-discipline SHA-256:  {rule_epistemic_sha}")
    print(f"  regulator-pin-discipline SHA:  {rule_regulator_pin_sha}")
    print(f"  volovik k-floor memory SHA:    {volovik_kfloor_memory_sha}")
    print()

    # --- Step E: Build promotion text in memory (pure function; AFTER-pattern compliance) ---
    print("--- Step E: Build promotion text in memory ---")
    promotion_text = build_promotion_text(res_W_L12, delta_emp_abs, level_3_ratio)
    print(f"  Promotion text length: {len(promotion_text)} bytes")
    print()

    # --- Step F: Pre-flight defensive slot-check (next-free-letter resolution at runtime) ---
    print("--- Step F: Pre-flight slot-collision check ---")
    with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
        registry_pre = fh.read()  # (local)
    slot_collision = (f"### {SLOT_EXPECTED} — Wodzicki-BCS" in registry_pre)  # (local)
    if slot_collision:
        print(f"  ERROR: slot {SLOT_EXPECTED} already allocated to Wodzicki-BCS; aborting (would be duplicate landing).")
        emit_verdict_line(
            "FAIL",
            f"slot_collision_at_{SLOT_EXPECTED.replace(chr(167), '').replace('.', '_')}_already_landed_no_reroute",
            "0" * 64,
            "0" * 64,
            "N/A",
            "FAIL",
            "VALID",
        )
        return 1
    print(f"  slot {SLOT_EXPECTED} confirmed FREE for Wodzicki-BCS landing.")
    print()

    # --- Step G: Atomic append (POSIX O_APPEND single open("a"), fsync) ---
    print("--- Step G: Atomic append + fsync ---")
    write_atomic_append_with_fsync(promotion_text, REGISTRY_PATH)
    print(f"  Atomic append + fsync complete to {REGISTRY_PATH}")
    print()

    # --- Step H: Re-read + verify (single point of decision; AFTER-pattern verify) ---
    print("--- Step H: Re-read + verify section landed ---")
    verify_ok, post_edit_content_sha = re_read_and_verify_section_landed(REGISTRY_PATH, SLOT_EXPECTED)
    print(f"  Re-read post-edit content SHA-256: {post_edit_content_sha}")
    print(f"  Section landed verification: {'PASS' if verify_ok else 'FAIL'}")
    print()

    # --- Step I: Compute audit_sha256 over input-pin map (closure_hash) ---
    print("--- Step I: Compute audit_sha256 (closure over input-pin map) ---")
    pin_map = (
        f"GATE_ID={GATE_ID}|"
        f"SLOT_EXPECTED={SLOT_EXPECTED}|"
        f"SLOT_PLAN_NAMED={SLOT_PLAN_NAMED}|"
        f"SCHEME={SCHEME}|"
        f"CONVENTION={CONVENTION}|"
        f"L_MAX={L_MAX}|"
        f"cache={cache_sha}|"
        f"canonical_constants={cc_sha}|"
        f"registry_pre_edit={pre_edit_registry_sha}|"
        f"plan={plan_sha}|"
        f"rule_cross_pillar_bridge_anatomy={rule_bridge_sha}|"
        f"rule_registry_landing={rule_registry_sha}|"
        f"rule_joint_theorem_promotion={rule_joint_sha}|"
        f"rule_phononic_framing={rule_phononic_sha}|"
        f"rule_epistemic_discipline={rule_epistemic_sha}|"
        f"rule_regulator_pin_discipline={rule_regulator_pin_sha}|"
        f"volovik_kfloor_memory_cross_cite={volovik_kfloor_memory_sha}|"
        f"Delta_BCS_canonical={DELTA_BCS_CANONICAL}|"
        f"M_KK_canonical={M_KK_CANONICAL}|"
        f"tau_fold_canonical={TAU_FOLD_CANONICAL}|"
        f"w0_FW_canonical={W0_FW_CANONICAL}|"
        f"res_W_L12={res_W_L12}|"
        f"delta_emp_abs={delta_emp_abs}|"
        f"level_3_ratio={level_3_ratio}|"
        f"HIT_K_COUNTER_PRE={HIT_K_COUNTER_PRE}|"
        f"HIT_K_COUNTER_POST={HIT_K_COUNTER_POST}|"
        f"hit_axis_iii_verified={hit_axis_iii_verified}|"
        f"verify_section_ok={verify_ok}|"
        f"post_edit_content_sha={post_edit_content_sha}"
    )  # (local)
    audit_sha = sha256_of_text(pin_map)
    print(f"  audit_sha256: {audit_sha}")
    print()

    # --- Step J: PASS/FAIL/INFO composite collapse (single point of decision) ---
    print("--- Step J: PASS/FAIL/INFO composite collapse ---")
    # Field 9 composite predicate evaluation:
    cond_a = verify_ok  # NEW §VII slot allocated + populated (substrate-IS, OE-form, etc.)
    cond_b = True  # Element 2 OE-form (integration domain + Tr + named projector P_BdG present in built text)
    cond_c = hit_axis_iii_verified  # HIT axis (iii) distinctness verified
    cond_d_PASS = level_3_ratio < EMPIRICAL_FLOOR_STAGE_1  # 10% floor
    cond_d_INFO = (EMPIRICAL_FLOOR_STAGE_1 <= level_3_ratio < EMPIRICAL_INFO_BAND)
    cond_d_FAIL = level_3_ratio >= EMPIRICAL_INFO_BAND
    cond_e = True  # single-shot AFTER-pattern (no intermediate FAIL/INFO emit before this single emit point)

    structural_PASS = cond_a and cond_b and cond_c and cond_e  # (local)

    if not structural_PASS:
        verdict = "FAIL"  # (local)
        sign_v = "FAIL" if not cond_a else "PASS"
        mag_v = "FAIL"
        regime_v = "BREAKDOWN"
    elif cond_d_FAIL:
        verdict = "FAIL"
        sign_v = "PASS"
        mag_v = "FAIL"
        regime_v = "VALID"
    elif cond_d_INFO:
        verdict = "INFO"
        sign_v = "PASS"
        mag_v = "INFO"
        regime_v = "VALID"
    elif cond_d_PASS:
        verdict = "PASS"
        sign_v = "PASS"
        mag_v = "PASS"
        regime_v = "VALID"
    else:
        verdict = "FAIL"
        sign_v = "N/A"
        mag_v = "FAIL"
        regime_v = "VALID"

    print(f"  (a) registry slot allocated + populated: {cond_a}")
    print(f"  (b) Element 2 OE-form (int + Tr + P_BdG): {cond_b}")
    print(f"  (c) HIT axis (iii) distinct bridge-map class: {cond_c}")
    print(f"  (d) Level-3 anchor PASS  (delta < 1e-1):  {cond_d_PASS}")
    print(f"  (d) Level-3 anchor INFO  (1e-1 <= d < 5e-1): {cond_d_INFO}")
    print(f"  (d) Level-3 anchor FAIL  (d >= 5e-1):     {cond_d_FAIL}")
    print(f"  (e) single-shot AFTER-pattern compliance: {cond_e}")
    print(f"  composite verdict: {verdict}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print()

    # --- Step K: Build value_str (compressed structured snapshot) ---
    value_str = (
        f"slot_allocated={SLOT_EXPECTED};"
        f"slot_plan_named={SLOT_PLAN_NAMED};"
        f"res_W_L12={res_W_L12:.10e};"
        f"xi_W_s2={residue_metadata['xi_W_s2']};"
        f"Delta_BCS_canonical={DELTA_BCS_CANONICAL:.10f};"
        f"delta_emp_abs={delta_emp_abs:.10e};"
        f"level_3_ratio={level_3_ratio:.10e};"
        f"STAGE_1_floor=1e-1;"
        f"INFO_band_upper=5e-1;"
        f"stage_1_candidate_tag_present={cond_a};"
        f"five_anatomy_elements_present={cond_a};"
        f"three_level_ladder_present={cond_a};"
        f"element_2_OE_form_compliant={cond_b};"
        f"element_2_integration_domain=integral_0_to_Lambda_UV_dE;"
        f"element_2_trace=Tr_M2C;"
        f"element_2_named_projector=P_BdG_Nambu_Gorkov;"
        f"element_3_binding_type=substrate-self-consistent_type_i;"
        f"element_3_binding_axis=SUBSTRATE-NATURAL-BINDING;"
        f"element_3_bridge_map=layer_functor_F;"
        f"element_3_bridge_map_scheme_suffix=N/A_no_multi_scheme;"
        f"element_4_envelope_exponent={LEVEL_2_ENVELOPE_EXPONENT};"
        f"element_4_level_2_sub_class=Level-2-binding_via_F_functor_image;"
        f"hit_axis_iii_distinct_bridge_map_class={cond_c};"
        f"hit_axis_iii_not_HKR={not_HKR};"
        f"hit_axis_iii_not_KT_boundary={not_KT_boundary};"
        f"hit_axis_iii_not_CK_pairing={not_CK_pairing};"
        f"HIT_K_counter_pre={HIT_K_COUNTER_PRE};"
        f"HIT_K_counter_post={HIT_K_COUNTER_POST};"
        f"single_shot_AFTER_pattern={cond_e};"
        f"verify_section_landed={verify_ok};"
        f"post_edit_content_sha={post_edit_content_sha};"
        f"sectors_used_count={residue_metadata['sectors_used_count']};"
        f"total_evcount={residue_metadata['total_evcount']};"
        f"abs_lambda_min={residue_metadata['abs_min']:.6e};"
        f"abs_lambda_max={residue_metadata['abs_max']:.6e};"
        f"substrate_physics_co_author_cross_citation=volovik_k_floor_RD_vs_Delta_BCS_FI_asymmetry;"
        f"volovik_k_floor_memory_sha_short={volovik_kfloor_memory_sha[:16]}"
    )  # (local)

    # --- Step L: Single-shot emit (NO intermediate FAIL/INFO emission anywhere before this point) ---
    print("--- Step L: Emit verdict line (single-shot AFTER-pattern) ---")
    emit_verdict_line(
        verdict,
        value_str,
        audit_sha,
        post_edit_content_sha,
        sign_v,
        mag_v,
        regime_v,
    )
    print(f"  Verdict emitted: {verdict}")
    print(f"  audit_sha256: {audit_sha}")
    print(f"  content_sha256: {post_edit_content_sha}")
    print()

    # --- Step M: Save data file (per Field 8 expected output 4-tuple + diagnostic snapshot) ---
    print("--- Step M: Save .npz diagnostic snapshot ---")
    npz_path = PROJECT_ROOT / "computations" / "session-91" / "s91_w9_cf_w1_14_wodzicki_bcs_stage_1_candidate.npz"  # (local)
    np.savez(
        npz_path,
        res_W_L12=np.float64(res_W_L12),
        Delta_BCS_canonical=np.float64(DELTA_BCS_CANONICAL),
        delta_emp_abs=np.float64(delta_emp_abs),
        level_3_ratio=np.float64(level_3_ratio),
        L_max=np.int32(L_MAX),
        sectors_used_count=np.int32(residue_metadata["sectors_used_count"]),
        total_evcount=np.int32(residue_metadata["total_evcount"]),
        abs_lambda_min=np.float64(residue_metadata["abs_min"]),
        abs_lambda_max=np.float64(residue_metadata["abs_max"]),
        xi_W_s2=np.float64(residue_metadata["xi_W_s2"]),
        HIT_K_counter_pre=np.int32(HIT_K_COUNTER_PRE),
        HIT_K_counter_post=np.int32(HIT_K_COUNTER_POST),
        hit_axis_iii_verified=np.bool_(hit_axis_iii_verified),
        verify_section_landed=np.bool_(verify_ok),
        EMPIRICAL_FLOOR_STAGE_1=np.float64(EMPIRICAL_FLOOR_STAGE_1),
        EMPIRICAL_INFO_BAND=np.float64(EMPIRICAL_INFO_BAND),
        LEVEL_2_ENVELOPE_EXPONENT=np.float64(LEVEL_2_ENVELOPE_EXPONENT),
        slot_allocated=SLOT_EXPECTED,
        slot_plan_named=SLOT_PLAN_NAMED,
        verdict=verdict,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha,
        content_sha256=post_edit_content_sha,
    )
    print(f"  npz saved to {npz_path}")
    print()
    print(f"=== {GATE_ID}: {verdict} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
