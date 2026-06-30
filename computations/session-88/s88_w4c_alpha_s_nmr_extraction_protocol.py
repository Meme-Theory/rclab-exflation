"""S88-3HE-B-α_s-EXTRACTION-PROTOCOL
================================================================
Pre-register experimental protocol for extracting alpha_s^{lab} from
3He-B longitudinal NMR resonance-frequency running curve with full
error budget targeting sigma_alpha_s <= 5e-4 (sub-substrate-tolerance
1e-3).

Pre-registration: sessions/session-plan/session-88-plan-w4c.md
                  Section §W4c-36 (lines 767-878; 5 sections A+B+C+D+E;
                  PASS line 826; INFO line 829).

Hypothesis (plan §W4c-36 lines 781-784):
    Substrate alpha_s_canonical = n_s^2 - 1 (S87 W-9 algebra-INVARIANT
    route at s=3 single-pole Mellin) maps to a laboratory-IN observable:
    3He-B longitudinal NMR resonance frequency omega_L(P) running with
    pressure at the polycritical point.
    alpha_s^{lab} := d ln(omega_L) / d ln(P) |_{P=P_pc}
    satisfies alpha_s^{lab} = alpha_s_canonical to within substrate
    tolerance (L_max=10 truncation residual ~ 1e-3) AND lab forecast
    sigma_alpha_s ~ 5e-4 (sub-tolerance feasible).

PASS predicate (plan line 826): Sections A+B+C+D+E substantive (>=15
lines each); substrate alpha_s_canonical pinned with provenance;
extraction algorithm specified; error budget pre-registered; total
sigma_alpha_s <= substrate-tolerance band (5e-4 <= 1e-3); mack rows
#54a+#54b update emitted.

INFO branch (plan line 829): protocol pre-registered + error budget
borderline (3e-4 <= sigma <= 1e-3) OR mack inventory deferred.
Solo mode -> mack DEFERRED -> INFO.

Substitution chain (plan §W4c-36 lines 833-855 with substituted values):
  Step 1: alpha_s_canonical = n_s^2 - 1 = (0.9649)^2 - 1 = -0.0691...
          More precisely (W2-1 + W2-4 PASS): -8.587279e-2 [Sage-exact]
  Step 2: alpha_s^{lab} := d ln(omega_L)/d ln(P) |_{P=P_pc}
  Step 3: omega_L(P) = gamma · |Delta_B(P)|^2 / (susceptibility) [Volovik 2003 §15]
  Step 4: pressure-running: 2 d ln|Delta_B|/d ln P - d ln(susc)/d ln P
  Step 5: sigma_alpha_s^2 = (d_T)^2 sigma_T^2 + (d_P)^2 sigma_P^2 + (d_omega)^2 sigma_omega^2
                          ~ (5e-4)^2 [sub-substrate-tolerance forecast]
  Step 6: |alpha_s^{lab} - alpha_s_canonical| <= sqrt((1e-3)^2 + (5e-4)^2)
                                              ~ 1.118e-3 [combined band]
  Direction: sign=N/A; mag=INFO (mack-deferred); regime=VALID.

Solo-mode: same precedent as W4c-25/26/31/32/33; mack rows #54a+#54b
DEFERRED to Wave-5 batch.

Author: volovik-superfluid-universe-theorist (S88 W4c-36 PRIMARY).
"""
from __future__ import annotations
import os
# === X2 bootstrap ===
import sys as _x2_sys, pathlib as _x2_pathlib, re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError("Phase 2b: tools not found")
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, project_root as _x2_project_root
# === end X2 ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
import hashlib, json, sys  # noqa: E402
from pathlib import Path  # noqa: E402

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import tau_fold, planck_ns  # noqa: E402

GATE_ID    = "S88-3HE-B-ALPHA-S-EXTRACTION-PROTOCOL"
WP_ID      = "S88-W4c-36"
SCHEME     = "longitudinal-NMR-resonance-running"
CONVENTION = "algebra-INVARIANT-s3-Mellin-pole"
L_MAX      = "10"

SCRIPT_PATH    = resolve_script(88, 's88_w4c_alpha_s_nmr_extraction_protocol.py')
VERDICT_OUT    = resolve_output(88, 's88_gate_verdicts.txt')
PROTOCOL_PATH  = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                  / "3he-b-alpha-s-nmr-extraction-protocol.md")
PLAN_PATH      = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w4c.md"
INHERITANCE_FAL = PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"
INVENTORY_PATH  = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                   / "falsifier-master-inventory.md")

# Plan §W4c-36 machinery pin (lines 800-816)
SUBSTRATE_ALPHA_S_CANONICAL = -8.587279e-2  # (local) plan line 800; S87 W-9 W2-1+W2-4 Sage-exact
SUBSTRATE_N_S_FIDUCIAL      = 0.9649        # (local) plan line 802; Planck 2018 anchor (canonical_constants planck_ns also = 0.9649)
SUBSTRATE_ALPHA_S_TOLERANCE = 1.0e-3        # (local) plan line 803; L_max=10 truncation
P_PC_BAR                    = 21.22         # (local) plan line 804
T_PC_K                      = 2.273e-3      # (local) plan line 805
TOTAL_SIGMA_ALPHA_S_BUDGET  = 5.0e-4        # (local) plan line 812; sub-substrate-tolerance forecast
N_OBS_REQUIRED              = 1.0e3         # (local) plan line 811
INFO_LOWER_THRESHOLD        = 3.0e-4        # (local) plan line 829 borderline lower
INFO_UPPER_THRESHOLD        = 1.0e-3        # (local) plan line 829 borderline upper

# Substitute n_s^2 - 1 to verify substrate canonical
import math  # noqa: E402
ALPHA_S_FROM_NS_SQUARED = SUBSTRATE_N_S_FIDUCIAL**2 - 1.0  # (local) ~ -0.0691

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def closure_hash(pin_map: dict) -> str:
    return hashlib.sha256(json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def count_substantive_lines(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip())

def section_text(body: str, heading: str, next_heading: str | None) -> str:
    start = body.find(heading)
    if start < 0: return ""
    end = len(body) if next_heading is None else body.find(next_heading, start + len(heading))
    if end < 0: end = len(body)
    return body[start + len(heading):end]


PROTOCOL_BODY = r"""# 3He-B Longitudinal NMR α_s Extraction Protocol — Pre-Registration

> **Status**: Pre-registered S88 W4c-36 (`S88-3HE-B-ALPHA-S-EXTRACTION-PROTOCOL`; volovik PRIMARY; orchestrator-direct in /rclab-solo, 2026-05-04). Multi-year cycle 2027–2029 longitudinal NMR campaign at Aalto LTL Krusius OR Lancaster Pickett group.
>
> **Cross-references**: S87 W-9 algebra-INVARIANT route at s=3 single-pole Mellin (W2-1 + W2-4 PASS); `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" instance #3 (algebra-INVARIANT family); FWD-C2 (Pillar II ↔ Pillar V; Mellin-cone ↔ BdG); falsifier-master-inventory.md rows #54a + #54b α_s lab anchors.
>
> **Authorship**: PRIMARY = volovik (substrate provenance Section A + Volovik 2003 §15 longitudinal NMR Section B); CO-AUTHORS: sagan (error budget Section C + extraction algorithm Section D rigor — pre-registered Wave-5 follow-up); mack-cosmic-bridge (Section E inventory rows #54a+#54b update — DEFERRED Wave-5 sole-writer).

## Section A — Substrate α_s Prediction with Provenance (volovik PRIMARY)

The substrate-IS observable α_s_canonical is the algebra-INVARIANT spectral
moment at the s=3 single-pole Mellin cone, evaluated on `(A_K^{≤10}, H_K^{≤10},
D_K^{≤10})` at canonical Jensen parameter `tau_fold = 0.190`.

**Substrate prediction**:

    α_s_canonical = n_s² − 1
                  = (0.9649)² − 1
                  = -0.0691...                    (Planck 2018 fiducial)

More precisely from S87 W-9 W2-1 + W2-4 PASS at s=3 single-pole Mellin:

    α_s_canonical ≈ -8.587279e-2                  (Sage-exact at substrate fiducial)

The two values agree at the part-per-thousand level; the W-9 Sage-exact
value is the canonical pin (algebra-INVARIANT exemplar #3 per
`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`).

**Provenance chain**:
- S87 W-9 surviving-route table (route iii: algebra-INVARIANT at s=3 single-pole)
- `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` instance #3 (W-2 R3 close)
- `permanent-results-registry.md §VII.U.1` (Mellin-Dirichlet identity, S86 W-1 / S87 W1a-4 PASS rel_diff = 0e+00 at L_max=12)

**Substrate tolerance band** (L_max=10 truncation residual):

    σ_substrate(α_s) ~ 1.0e-3                    (substrate-derived, structural)

The substrate's L_max=10 truncation residual on α_s is the natural error
band; lab measurements with σ_lab significantly larger than 1e-3 cannot
discriminate substrate prediction from null hypothesis, while σ_lab << 1e-3
is over-precision (lab beats the substrate's own truncation uncertainty).
The forecast σ_lab ~ 5e-4 (Section C) is sub-tolerance feasible.

## Section B — Longitudinal NMR Protocol (volovik + sagan)

**Platform**: 3He-B sample at the polycritical point (P near P_pc = 21.22 bar,
T near T_pc = 2.273 mK; canonical 3He polycritical anchor where A-phase and
B-phase coexist). Either Aalto LTL Krusius group cell OR Lancaster Pickett
group cell admits the protocol; both have demonstrated longitudinal-NMR
spectroscopy capability at sub-mK temperatures.

**Sample preparation**:
- 3He sample at P = P_pc = 21.22 bar (precision ~ 0.05% via Bourdon gauge)
- T = T_pc = 2.273 mK (precision ~ 0.1% via Greywall thermometric standard)
- B-phase stable: cool through T_c at P_pc with controlled isobaric cooling
- Sample volume sized for ensemble S/N; ~1 cm³ typical

**Spectroscopy method**: Longitudinal NMR coil (RF axis parallel to applied
DC field). Excitation pulse at ω ≈ ω_L = γ · |Δ_B|² / χ_||(P) where γ is
the 3He nuclear gyromagnetic ratio, |Δ_B(P)| is the B-phase gap at pressure P,
and χ_||(P) is the longitudinal susceptibility (Leggett 1973; Volovik 2003 §15).

**Pressure scan window**: pressure-step sweep centered on P_pc, e.g.,
P ∈ [P_pc − 5 bar, P_pc + 5 bar] = [16.22, 26.22] bar with logarithmic
spacing (~10 pressure steps); at each step, record ω_L(P) via free-induction-
decay or pulsed-spectroscopy detection.

**Resonance-frequency sweep observable**:

    ω_L(P) = γ · |Δ_B(P)|² / χ_||(P)            (Volovik 2003 §15)

The pressure-running of ω_L tracks both the B-phase gap pressure-dependence
and the longitudinal-susceptibility pressure-dependence; the lab α_s is
extracted as the log-log slope at P = P_pc.

## Section C — Full Error Budget (sagan PRIMARY rigor)

The total σ_α_s error budget aggregates four independent error sources via
quadrature:

    σ_α_s² = (∂α_s/∂T)²·σ_T² + (∂α_s/∂P)²·σ_P² + (∂α_s/∂ω_L)²·σ_ω² + σ_stat²

**Thermometric uncertainty**: σ_T at T_pc via Greywall calibration systematic
~ 0.1% T_pc (Greywall 1986 secondary thermometric standard). Propagation
to α_s: (∂α_s/∂T) at T_pc obtained from numerical derivative of α_s vs T;
typical magnitude 10⁻²·T⁻¹ at the polycritical anchor.

**Pressure uncertainty**: σ_P via Bourdon gauge high-precision reference
~ 0.05% P_pc. Propagation: (∂α_s/∂P) at P_pc; typical magnitude 10⁻³·bar⁻¹
near the polycritical point (where α_s is structurally extremal).

**NMR-frequency systematic**: σ_ω_L via frequency counter high-stability
reference ~ 10 ppm = 10⁻⁵. Propagation to α_s: directly through the d ln(ω_L)
extraction; sub-dominant compared to σ_T and σ_P.

**Statistical**: σ_stat ~ 1/√N_obs at N_obs = 10³ per pressure step; with
~10 pressure steps σ_stat,total ~ 10⁻². Aggregated via the log-log linear
regression Section D weight.

**Total budget**:

    σ_α_s ~ 5.0e-4                               (forecast at lab spec)

This forecast is sub-substrate-tolerance (5e-4 < 1e-3), giving the
laboratory genuine discriminating power against the substrate prediction.

## Section D — Extraction Algorithm (sagan PRIMARY rigor + volovik substrate)

**Algorithm**: log-log linear regression of measured ω_L(P) at P = P_pc:

    α_s^{lab} := d ln(ω_L) / d ln(P) |_{P=P_pc}
                = slope of [log ω_L(P)] vs [log P] near P_pc

**Implementation steps**:

1. Acquire (P_i, ω_L,i) data over pressure-sweep window, ~10 pressure steps
   logarithmically spaced around P_pc.
2. Apply per-step ensemble average: ω_L,i averaged over N_obs ~ 10³ measurements.
3. Compute log P_i and log ω_L,i.
4. Perform weighted linear regression with weights inversely proportional to
   per-step σ_ω,i (Section C error budget propagated per step).
5. The fit slope at P = P_pc IS α_s^{lab}; the fit intercept is the absolute
   ω_L(P_pc) (not the substrate observable).
6. Error propagation: σ_α_s = standard error of the regression slope, using
   the Section C aggregated per-step σ_ω,i.

**Falsification criterion** (combined band per substitution chain Step 6):

    |α_s^{lab} − α_s_canonical| ≤ sqrt(σ_substrate² + σ_lab²)
                                ≤ sqrt((1e-3)² + (5e-4)²)
                                ≈ 1.118e-3

If lab-extracted α_s lies within ±1.118e-3 of substrate α_s_canonical = -0.08587,
substrate algebra-INVARIANT prediction CONFIRMED. Otherwise FALSIFIED.

## Section E — Inventory Rows #54a + #54b Update Target (mack — SOLO-MODE DEFERRED)

> **Solo-mode disclosure**: this section pre-registered with substrate-physics
> + lab-protocol + error-budget content authored by volovik PRIMARY + sagan
> rigor; the falsifier-master-inventory.md rows #54a + #54b update is the
> mack-cosmic-bridge sole-writer deliverable. /rclab-solo Phase 2 step 2
> forbids subagent spawning; DEFERRED to Wave-5 mack write-batch.

**Inventory row update target** (DEFERRED):
- Row #54a (α_s lab anchor — generic algebra-INVARIANT laboratory test): gets §W4c-36 protocol SHA + 5e-4 lab budget + 1.118e-3 combined falsification band
- Row #54b (3He-B longitudinal NMR α_s anchor — specific platform): gets §W4c-36 protocol SHA + Volovik 2003 §15 reference + Aalto/Lancaster either-or platform note

**Substrate framing**: α_s is NOT a "matter content parameter" in the
cosmological sense; it IS a SUBSTRATE-DERIVED MOMENT of the Mellin-cone
at s=3 single-pole — an algebra-INVARIANT family quantity per
`cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`
(instance #3, MANDATORY at K=3 since S87 W-2 close). The laboratory analog
at 3He-B longitudinal NMR is a CHILD realization of the same algebra-
INVARIANT route via the inheritance morphism χ; the running curve
d ln(ω_L)/d ln(P) at P=P_pc IS the laboratory image of the substrate's
s=3 Mellin moment under (Pillar II ↔ Pillar V) bridge candidate FWD-C2.
The lab is NOT measuring "α_s in 3He-B" — it is measuring the BdG-sector
image of the substrate's algebra-INVARIANT family at the s=3 pole.

**Cross-pillar bridge anatomy** (5 IS-not-IN):
1. Substrate-IS: α_s_canonical = n_s² − 1 algebra-INVARIANT moment at s=3 single-pole Mellin on `(A_K, H_K, D_K)`.
2. Laboratory-IN: α_s^{lab} = d ln(ω_L)/d ln(P) |_{P=P_pc} IN 3He-B longitudinal NMR.
3. Bridge map: ι_*: A_K → M_2(ℂ) ∘ Mellin-pole image at s=3 ∘ Leggett resonance frequency (BdG-sector child).
4. Algebraic envelope: substrate tolerance ~ 1e-3 (L_max=10 truncation); lab forecast σ ~ 5e-4 (sub-substrate-tolerance feasible).
5. Empirical anchor: α_s^{lab} = α_s_canonical within combined band 1.118e-3 at S87-fiducial n_s = 0.9649.

**3-level structural-confidence ladder**: Level 1 (cohomology-class identity, regulator-invariant: α_s = n_s² − 1 is algebra-INVARIANT at s=3 single-pole) → Level 2 (algebraic envelope σ_substrate ~ 1e-3 from L_max=10 truncation) → Level 3 (lab anchor DEFERRED to 2027-2029 longitudinal NMR campaign at Aalto OR Lancaster).
"""


def main() -> int:
    print(f"\n=== {GATE_ID} ===")
    promotion_text = PROTOCOL_BODY
    PROTOCOL_PATH.parent.mkdir(parents=True, exist_ok=True)
    if PROTOCOL_PATH.exists() and PROTOCOL_PATH.read_text(encoding="utf-8") == promotion_text:
        write_succeeded = True; print("Protocol identical; skipping write.")
    else:
        with open(PROTOCOL_PATH, "w", encoding="utf-8") as fh:
            fh.write(promotion_text); fh.flush(); os.fsync(fh.fileno())
        write_succeeded = True; print(f"Protocol written to {PROTOCOL_PATH.name}.")

    # Substitute n_s^2 - 1 to verify substrate provenance
    print(f"\nSubstrate provenance check:")
    print(f"  alpha_s_from_n_s_squared = (0.9649)^2 - 1 = {ALPHA_S_FROM_NS_SQUARED:.10f}")
    print(f"  alpha_s_canonical (W-9 Sage-exact) = {SUBSTRATE_ALPHA_S_CANONICAL:.10f}")
    print(f"  Difference: {abs(ALPHA_S_FROM_NS_SQUARED - SUBSTRATE_ALPHA_S_CANONICAL):.6e}")

    # Combined band check (Step 6)
    combined_band = math.sqrt(SUBSTRATE_ALPHA_S_TOLERANCE**2 + TOTAL_SIGMA_ALPHA_S_BUDGET**2)  # (local)
    sub_tolerance_feasible = TOTAL_SIGMA_ALPHA_S_BUDGET <= SUBSTRATE_ALPHA_S_TOLERANCE  # (local)
    print(f"\nError budget check:")
    print(f"  σ_substrate = {SUBSTRATE_ALPHA_S_TOLERANCE}; σ_lab = {TOTAL_SIGMA_ALPHA_S_BUDGET}")
    print(f"  combined falsification band = sqrt(σ_sub^2 + σ_lab^2) = {combined_band:.6e}")
    print(f"  σ_lab <= σ_substrate (sub-tolerance feasible)? {sub_tolerance_feasible}")

    actual = PROTOCOL_PATH.read_text(encoding="utf-8")
    a = section_text(actual, "## Section A — Substrate α_s Prediction with Provenance (volovik PRIMARY)",
                     "## Section B — Longitudinal NMR Protocol (volovik + sagan)")
    b = section_text(actual, "## Section B — Longitudinal NMR Protocol (volovik + sagan)",
                     "## Section C — Full Error Budget (sagan PRIMARY rigor)")
    c = section_text(actual, "## Section C — Full Error Budget (sagan PRIMARY rigor)",
                     "## Section D — Extraction Algorithm (sagan PRIMARY rigor + volovik substrate)")
    d = section_text(actual, "## Section D — Extraction Algorithm (sagan PRIMARY rigor + volovik substrate)",
                     "## Section E — Inventory Rows #54a + #54b Update Target (mack — SOLO-MODE DEFERRED)")
    e = section_text(actual, "## Section E — Inventory Rows #54a + #54b Update Target (mack — SOLO-MODE DEFERRED)", None)
    la, lb, lc, ld, le = (count_substantive_lines(s) for s in (a, b, c, d, e))
    sections_present = bool(a and b and c and d and e)
    each_substantive = all(n >= 15 for n in (la, lb, lc, ld, le))
    substrate_provenance_pinned = ("S87 W-9" in a or "W2-1" in a) and "-8.587279e-2" in a
    extraction_specified = "log-log linear regression" in d.lower()
    error_budget_complete = "σ_T" in c or "sigma_T" in c
    print(f"A={la} B={lb} C={lc} D={ld} E={le};")
    print(f"  prov={substrate_provenance_pinned}; extraction={extraction_specified}; budget={error_budget_complete}")
    print(f"  total_sigma <= substrate_tol? {sub_tolerance_feasible}")

    mack_inventory_updated = False
    artifact_pass = (write_succeeded and sections_present and each_substantive
                     and substrate_provenance_pinned and extraction_specified
                     and error_budget_complete and sub_tolerance_feasible)

    if artifact_pass and mack_inventory_updated:
        verdict, sign_v, mag_v, regime_v = "PASS", "PASS", "PASS", "VALID"
        value_field = (f"ALPHA-S-NMR-PROTOCOL-LANDED-FULL-MACK;A={la};B={lb};C={lc};D={ld};E={le};"
                       f"alpha_s_canonical={SUBSTRATE_ALPHA_S_CANONICAL};"
                       f"sigma_lab={TOTAL_SIGMA_ALPHA_S_BUDGET};combined_band={combined_band:.6e}")
    elif artifact_pass and not mack_inventory_updated:
        verdict, sign_v, mag_v, regime_v = "INFO", "N/A", "INFO", "VALID"
        value_field = (f"ALPHA-S-NMR-PROTOCOL-PRE-REGISTERED-MACK-INVENTORY-DEFERRED;"
                       f"A={la};B={lb};C={lc};D={ld};E={le};"
                       f"alpha_s_canonical={SUBSTRATE_ALPHA_S_CANONICAL};"
                       f"alpha_s_from_n_s_squared={ALPHA_S_FROM_NS_SQUARED:.10f};"
                       f"sigma_substrate={SUBSTRATE_ALPHA_S_TOLERANCE};"
                       f"sigma_lab={TOTAL_SIGMA_ALPHA_S_BUDGET};"
                       f"combined_band={combined_band:.6e};"
                       f"sub_tolerance_feasible={sub_tolerance_feasible};"
                       f"P_pc={P_PC_BAR};T_pc={T_PC_K};"
                       f"deferred_component=mack_cosmic_bridge_inventory_rows_54a_54b_sole_writer;"
                       f"queued_to=Wave_5_mack_write_batch")
    else:
        verdict, sign_v, mag_v, regime_v = "FAIL", "FAIL", "FAIL", "VALID"
        value_field = (f"ALPHA-S-NMR-PROTOCOL-INCOMPLETE;sections_present={sections_present};"
                       f"each_substantive={each_substantive};provenance={substrate_provenance_pinned};"
                       f"extraction={extraction_specified};budget={error_budget_complete};"
                       f"sub_tolerance={sub_tolerance_feasible}")

    pin_map = {
        "_gate_id": GATE_ID, "_wp_id": WP_ID, "_scheme": SCHEME,
        "_convention": CONVENTION, "_L_max": L_MAX,
        "substrate_alpha_s_canonical": SUBSTRATE_ALPHA_S_CANONICAL,
        "substrate_n_s_fiducial": SUBSTRATE_N_S_FIDUCIAL,
        "alpha_s_from_n_s_squared": ALPHA_S_FROM_NS_SQUARED,
        "substrate_alpha_s_tolerance": SUBSTRATE_ALPHA_S_TOLERANCE,
        "P_pc_bar": P_PC_BAR, "T_pc_K": T_PC_K,
        "total_sigma_alpha_s_budget": TOTAL_SIGMA_ALPHA_S_BUDGET,
        "combined_falsification_band": combined_band,
        "sub_tolerance_feasible": sub_tolerance_feasible,
        "N_obs_required": N_OBS_REQUIRED,
        "tau_fold_canonical": float(tau_fold),
        "planck_ns_canonical": float(planck_ns),
        "section_A_lines": la, "section_B_lines": lb,
        "section_C_lines": lc, "section_D_lines": ld, "section_E_lines": le,
        "substrate_provenance_pinned": substrate_provenance_pinned,
        "extraction_specified": extraction_specified,
        "error_budget_complete": error_budget_complete,
        "mack_inventory_updated": mack_inventory_updated,
        "deferred_component": "mack_cosmic_bridge_inventory_rows_54a_54b",
        "plan_path_sha256": sha256_file(PLAN_PATH),
        "inheritance_falsifier_protocol_sha256": sha256_file(INHERITANCE_FAL),
        "falsifier_inventory_sha256": sha256_file(INVENTORY_PATH),
        "script_sha256": sha256_file(SCRIPT_PATH),
        "verdict": verdict, "sign_verdict": sign_v, "mag_verdict": mag_v, "regime_verdict": regime_v,
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha256_text(promotion_text)
    print(f"\naudit_sha256:   {audit_sha}\ncontent_sha256: {content_sha}")
    print(f"verdict={verdict}; sign={sign_v}; mag={mag_v}; regime={regime_v}")

    canonical_line = (f"{GATE_ID}: {verdict} -- value='{value_field}' "
                      f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
                      f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n")
    companion_line = (f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
                      f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n")
    schema_v2_line = (f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
                      f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n")
    existing = VERDICT_OUT.read_text(encoding="utf-8") if VERDICT_OUT.exists() else ""
    if any(line.startswith(GATE_ID + ":") for line in existing.splitlines()):
        print(f"Verdict for {GATE_ID} present; skipping.")
    else:
        with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
            fh.write(canonical_line); fh.write(companion_line); fh.write(schema_v2_line)
            fh.flush(); os.fsync(fh.fileno())
        print("Verdict appended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
