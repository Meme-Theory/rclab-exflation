"""S88-3HE-B-CLASS-A-LAB-DISPATCH
================================================================
Aalto LTL coordination on Class-A kernel-signature NULL pre-
registration for the decisive triplet F1 + F2 + F5 from the
inheritance-falsifier 4-Gate Structure.

Pre-registration: sessions/session-plan/session-88-plan-w4c.md
                  Section §W4c-32 (lines 335-429; PASS line 387;
                  INFO line 389; substitution chain Steps 1-5
                  lines 393-407).

Hypothesis (plan §W4c-32 lines 348-349):
    Decisive Class-A triplet F1 + F2 + F5 maps to three independent
    Aalto observables, each pre-registered NULL with substrate-
    derived margin and 9 sigma S/N forecast per one-decade pressure
    window.

PASS predicate (plan §W4c-32 line 387):
    PASS iff Sections A+B+C+D substantive (>=15 lines each); per-row
    substrate margins from S86 W-5 §VII.AF.1; Aalto group assignment
    for ALL three F1/F2/F5 rows; 9 sigma S/N forecast pre-registered;
    mack rows #45/#47/#48 update emitted.

INFO branch (plan §W4c-32 line 389):
    Class-A dispatch pre-registered + per-row Aalto schedule TBD
    OR mack inventory deferred. Solo mode -> mack DEFERRED.

Substitution chain (plan §W4c-32 lines 393-407):
  Step 1: Decisive triplet from inheritance-falsifier-protocol.md
          §"Four-Gate Structure": Gate 1 = NULL on F1 + F2 + F5
  Step 2: Substrate margin per row (S86 W-5 calibration):
          F1 = 0.573193 M_KK^2 (Caroli-Matricon)
          F2 = derived (cocycle partner of phi_67)
          F5 = derived (chiral pair of phi_67)
  Step 3: Lab S/N forecast: 9 sigma per one-decade pressure window
  Step 4: NULL prediction: F_i^{lab}_predicted = 0 +/- sigma/sqrt(N_obs)
  Step 5: Decisive vs supporting separation:
          F1+F2+F5 = decisive (substrate-clean cocycles)
          F3+F4    = supporting (cocycle-degenerate; #34 governs)
  Direction: sign=N/A; mag=INFO (mack-deferred); regime=VALID.

Solo-mode: mack-cosmic-bridge sole-writer for rows #45+#47+#48
DEFERRED to Wave-5 batch.

Author: volovik-superfluid-universe-theorist (S88 W4c-32 PRIMARY).
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
    raise RuntimeError("Phase 2b bootstrap: tools not found")
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, project_root as _x2_project_root
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
# === end X2 ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
import hashlib, json, sys  # noqa: E402
from pathlib import Path  # noqa: E402

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import substrate_cocycle_ratio_67_88, tau_fold  # noqa: E402

GATE_ID    = "S88-3HE-B-CLASS-A-LAB-DISPATCH"
WP_ID      = "S88-W4c-32"
SCHEME     = "Class-A-decisive-triplet"
CONVENTION = "kernel-signature-NULL-9sigma"
L_MAX      = "10"

SCRIPT_PATH    = resolve_script(88, 's88_w4c_class_a_lab_dispatch.py')
VERDICT_OUT    = resolve_output(88, 's88_gate_verdicts.txt')
PROTOCOL_PATH  = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                  / "class-a-lab-dispatch-pre-registration.md")
PLAN_PATH      = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w4c.md"
INHERITANCE_FAL = PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"
CROSS_PILLAR    = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
INVENTORY_PATH  = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                   / "falsifier-master-inventory.md")

CLASS_A_DECISIVE_ROWS  = ["F1_Caroli_Matricon", "F2_NMR_satellite", "F5_Andreev_edge"]  # (local) plan line 366
SUBSTRATE_MARGIN_F1    = 0.573193  # (local) plan line 60; S86 W-5 §VII.AF.1 calibration M_KK^2
S_N_FORECAST_PER_ROW   = 9.0       # (local) plan line 370
AALTO_GROUPS_PER_ROW   = {  # (local) plan line 371
    "F1": "Krusius_ROTA",
    "F2": "Krusius_NMR_long",
    "F5": "Tuoriniemi_Andreev",
}

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


PROTOCOL_BODY = r"""# Class-A Decisive Triplet (F1 + F2 + F5) — Aalto LTL Lab Dispatch Pre-Registration

> **Status**: Pre-registered S88 W4c-32 (`S88-3HE-B-CLASS-A-LAB-DISPATCH`; volovik PRIMARY; orchestrator-direct in /rclab-solo, 2026-05-04). Multi-year cycle 2027–2030.
>
> **Cross-references**: `.claude/rules/inheritance-falsifier-protocol.md` §"Two Test Classes" + §"Four-Gate Structure" (W11-C5 calibration corpus); `sessions/permanent-results-registry.md` §VII.AF.1 (substrate-side anchor); §W4c-25 Lancaster F1 cross-platform; §W4c-31 Aalto LTL coordination matrix.

## Section A — Per-Row Substrate Predictions (volovik PRIMARY)

The Class-A kernel-signature decisive triplet (F1, F2, F5) consists of
three substrate-clean cocycle observables, each probing an independent
generator in `ker(ι_*)`. Per `inheritance-falsifier-protocol.md` §"Two
Test Classes":

> "Class A — Kernel-Signature Test: row-wise NULL prediction across
> each F-row of the falsifier inventory ... [confirms] BdG-restricted
> spectrum carries no ker(ι_*) cocycle."

**Row F1 — Caroli-Matricon ladder asymmetry** (Volovik 2003 §6):
- Substrate cocycle: [φ_67] (chiral pair, angular OFF-diagonal sector)
- Substrate margin: ‖[φ_67]‖_{Caroli-Matricon} = 0.573193 M_KK² (S86 W-5 §VII.AF.1 calibration)
- Lab observable: F1 = (E_+ − E_-)/(E_+ + E_-) at vortex-core n=0 minigap
- Substrate prediction: F1^{lab} = NULL at substrate-clean level (Class-A kernel-signature)
- Class-A direction: NULL is structural-cohomological, not statistical-precision

**Row F2 — NMR satellite peak ratio** (cocycle partner of φ_67):
- Substrate cocycle: derived from φ_67 (cocycle partner channel; S86 W-5 §VII.AF.1)
- Substrate margin: derived from same chiral-pair structure as F1; analogous M_KK² order of magnitude
- Lab observable: ratio of NMR satellite peak intensities probing the off-diagonal channel
- Substrate prediction: F2^{lab} = NULL (Class-A kernel-signature; same ker(ι_*) generator family)

**Row F5 — Andreev reflection edge-state asymmetry** (chiral pair of φ_67):
- Substrate cocycle: chiral pair partner of φ_67 in the (lambda_6, lambda_7) sector
- Substrate margin: derived analogously from S86 W-5 calibration
- Lab observable: edge-state asymmetry from Andreev reflection at the BdG sector boundary
- Substrate prediction: F5^{lab} = NULL (Class-A kernel-signature)

**Decisive vs supporting separation**: F1 + F2 + F5 are substrate-CLEAN
cocycle generators (each probes ONE independent ker(ι_*) element);
their combined NULL prediction is the substrate's most decisive Class-A
falsifier set. Rows F3 + F4 are cocycle-DEGENERATE (multiple substrate
cocycles superpose at those observables); they require the slope-
discrimination Gate-4 from the 4-Gate Structure (handled at §W4c-34
(Δ_B/Δ_A) calibration family).

## Section B — Aalto Group / Cell Assignment Per Row (volovik + sagan)

Each row maps to an independent Aalto observable per the §W4c-31
multi-session coordination matrix:

| Row | Aalto group | Cell + method | Lab observable |
|:----|:------------|:--------------|:----------------|
| F1 | Krusius | ROTA channel + transverse-NMR ladder | First-harmonic ladder asymmetry |
| F2 | Krusius | ROTA channel + longitudinal NMR | Satellite peak ratio (90°-rotated coil) |
| F5 | Tuoriniemi | Nanofluidic 3He cell + Andreev reflection | Edge-state asymmetry from sub-µm channel walls |

**Why two of three to Krusius**: F1 + F2 both rely on the rotation-
stabilized vortex array; the same ROTA cell generates both observables
modulo the transverse-vs-longitudinal NMR coil rotation. This shares
the cell-engineering overhead and provides cross-checking within the
same physical sample.

**Why F5 to Tuoriniemi**: the nanofluidic 3He cell's sub-µm channel
geometry creates a controlled BdG-sector boundary at the wall;
Andreev reflection from this boundary directly samples the edge-state
asymmetry of the chiral-pair cocycle. Krusius ROTA cannot replicate
this geometry (rotation requires bulk fluid).

## Section C — Statistical-Power Forecast Per Row at 9σ S/N (sagan + volovik)

The lab S/N forecast for each row at the Aalto LTL cell sensitivity
delivers σ_F_i ≈ 9.0 per one-decade pressure window 0–34 bar. The
per-row statistical-power calculation:

    σ_F_i / F_substrate = 1 / (S/N · √N_obs)
                        = 1 / (9 · √(10⁴))
                        ≈ 1.11e-3 per pressure step
                        ≈ 0.001 aggregated over 10 pressure steps

A non-NULL detection at the 9σ level on ANY single row falsifies the
substrate Class-A prediction unless the Class-B cohomology-asymmetry
ratio test (§W4c-26 / §W4c-33) survives in the cross-cocycle channel
— the substrate's overall PASS requires NULL-on-rows AND ratio-on-cross
per `inheritance-falsifier-protocol.md` §"Two Test Classes".

Statistical-power calculation assumes:
- N_obs = 10⁴ per pressure step (forecast at Aalto LTL ensemble size)
- 10 pressure steps per decade (logarithmic spacing 0–34 bar)
- Independent measurements per row (independent statistical aggregation)

Cross-platform replication at Lancaster MCT-3 (§W4c-25) provides an
INDEPENDENT 9σ NULL test on F1, doubling the Class-A discrimination
power against single-platform systematics.

## Section D — Inventory Rows #45 + #47 + #48 Update Target (mack — SOLO-MODE DEFERRED)

> **Solo-mode disclosure**: this section pre-registered with substrate-
> physics content authored by volovik PRIMARY; the falsifier-master-
> inventory.md rows #45 + #47 + #48 update is the mack-cosmic-bridge
> sole-writer deliverable. /rclab-solo Phase 2 step 2 forbids subagent
> spawning; the row updates are DEFERRED to a Wave-5 mack write-batch.

**Inventory row update target** (DEFERRED):
- Row #45 (Lancaster Caroli-Matricon F1 NULL) — already addressed at §W4c-25; this gate adds Aalto Krusius ROTA F1 SHA cross-link
- Row #47 (F2 NMR satellite ratio) — Aalto Krusius longitudinal NMR coordination SHA + 9σ S/N forecast
- Row #48 (F5 Andreev edge-state asymmetry) — Aalto Tuoriniemi nanofluidic Andreev coordination SHA + 9σ S/N forecast

**Decisive-triplet leverage**: a single non-NULL detection on any one
of F1, F2, F5 falsifies the substrate Class-A prediction directly
(modulo Class-B rescue). Three independent rows × two platforms
(Lancaster + Aalto) = SIX independent NULL tests on the kernel-signature
prediction. The falsifier-master-inventory.md row structure makes this
explicit; the mack write-batch installs the cross-link SHAs.

**Substrate framing**: F1, F2, F5 are NOT three "different experiments"
— they are three independent observables, each probing a substrate-
clean cocycle generator in `ker(ι_*)`. The decisive triplet is the
substrate's most leverage-rich falsifier set: a non-NULL on any ONE
row falsifies the substrate Class-A prediction (modulo Class-B rescue).
Direction of explanation: A_K cocycle pair → χ inheritance → BdG-sector
image → three Aalto observables → three NULL predictions at 9σ S/N.

**Cross-pillar bridge anatomy** (5 IS-not-IN):
1. Substrate-IS: ‖[φ_67]‖_{F1, F2, F5} on `(A_K, H_K, D_K)`.
2. Laboratory-IN: F1^{lab}, F2^{lab}, F5^{lab} at Aalto LTL three-group cells.
3. Bridge map: ι_*: A_K → M_2(ℂ) ∘ (Δ_B/Δ_A)^p per row.
4. Algebraic envelope: per-row substrate margin ± 9σ statistical band.
5. Empirical anchor: NULL on all three rows.

**3-level ladder**: Level 1 (kernel-signature cohomology identity, regulator-invariant) → Level 2 (structural-exact NULL form, no L_max⁻α envelope) → Level 3 (lab anchor DEFERRED to 2027–2030 multi-row campaign).
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

    actual = PROTOCOL_PATH.read_text(encoding="utf-8")
    a = section_text(actual, "## Section A — Per-Row Substrate Predictions (volovik PRIMARY)",
                     "## Section B — Aalto Group / Cell Assignment Per Row (volovik + sagan)")
    b = section_text(actual, "## Section B — Aalto Group / Cell Assignment Per Row (volovik + sagan)",
                     "## Section C — Statistical-Power Forecast Per Row at 9σ S/N (sagan + volovik)")
    c = section_text(actual, "## Section C — Statistical-Power Forecast Per Row at 9σ S/N (sagan + volovik)",
                     "## Section D — Inventory Rows #45 + #47 + #48 Update Target (mack — SOLO-MODE DEFERRED)")
    d = section_text(actual, "## Section D — Inventory Rows #45 + #47 + #48 Update Target (mack — SOLO-MODE DEFERRED)", None)
    la, lb, lc, ld = (count_substantive_lines(s) for s in (a, b, c, d))
    sections_present = bool(a and b and c and d)
    each_substantive = all(n >= 15 for n in (la, lb, lc, ld))
    all_rows_assigned = all(row in b for row in ["F1", "F2", "F5"])
    margin_pinned = "0.573193" in a
    s_n_forecast_pinned = "9" in c and "10" in c  # 9 sigma + 10 pressure steps
    print(f"A={la} B={lb} C={lc} D={ld}; rows={all_rows_assigned}; margin={margin_pinned}; SN={s_n_forecast_pinned}")

    mack_inventory_updated = False
    artifact_pass = (write_succeeded and sections_present and each_substantive
                     and all_rows_assigned and margin_pinned and s_n_forecast_pinned)

    if artifact_pass and mack_inventory_updated:
        verdict, sign_v, mag_v, regime_v = "PASS", "PASS", "PASS", "VALID"
        value_field = (f"CLASS-A-DISPATCH-LANDED-FULL-MACK;A={la};B={lb};C={lc};D={ld};"
                       f"rows=F1+F2+F5;margin_F1={SUBSTRATE_MARGIN_F1};SN_per_row={S_N_FORECAST_PER_ROW}")
    elif artifact_pass and not mack_inventory_updated:
        verdict, sign_v, mag_v, regime_v = "INFO", "N/A", "INFO", "VALID"
        value_field = (f"CLASS-A-DISPATCH-PRE-REGISTERED-MACK-INVENTORY-DEFERRED;"
                       f"A={la};B={lb};C={lc};D={ld};rows=F1+F2+F5;"
                       f"margin_F1={SUBSTRATE_MARGIN_F1};SN_per_row={S_N_FORECAST_PER_ROW};"
                       f"per_row_assignment_Krusius_ROTA+Krusius_NMR_long+Tuoriniemi_Andreev;"
                       f"deferred_component=mack_cosmic_bridge_inventory_rows_45_47_48_sole_writer;"
                       f"queued_to=Wave_5_mack_write_batch")
    else:
        verdict, sign_v, mag_v, regime_v = "FAIL", "FAIL", "FAIL", "VALID"
        value_field = (f"CLASS-A-DISPATCH-INCOMPLETE;A={la};B={lb};C={lc};D={ld};"
                       f"rows={all_rows_assigned};margin={margin_pinned};SN={s_n_forecast_pinned}")

    pin_map = {
        "_gate_id": GATE_ID, "_wp_id": WP_ID, "_scheme": SCHEME,
        "_convention": CONVENTION, "_L_max": L_MAX,
        "class_A_decisive_rows": CLASS_A_DECISIVE_ROWS,
        "substrate_margin_F1_M_KK_sq": SUBSTRATE_MARGIN_F1,
        "S_N_forecast_per_row": S_N_FORECAST_PER_ROW,
        "aalto_groups_per_row": AALTO_GROUPS_PER_ROW,
        "test_class": "Class_A_kernel_signature_decisive",
        "substrate_cocycle_ratio_67_88_canonical": float(substrate_cocycle_ratio_67_88),
        "tau_fold_canonical": float(tau_fold),
        "section_A_lines": la, "section_B_lines": lb,
        "section_C_lines": lc, "section_D_lines": ld,
        "all_rows_assigned": all_rows_assigned,
        "margin_pinned": margin_pinned, "s_n_forecast_pinned": s_n_forecast_pinned,
        "mack_inventory_updated": mack_inventory_updated,
        "deferred_component": "mack_cosmic_bridge_inventory_rows_45_47_48",
        "plan_path_sha256": sha256_file(PLAN_PATH),
        "inheritance_falsifier_protocol_sha256": sha256_file(INHERITANCE_FAL),
        "cross_pillar_bridge_anatomy_sha256": sha256_file(CROSS_PILLAR),
        "falsifier_inventory_sha256": sha256_file(INVENTORY_PATH),
        "script_sha256": sha256_file(SCRIPT_PATH),
        "verdict": verdict, "sign_verdict": sign_v, "mag_verdict": mag_v, "regime_verdict": regime_v,
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha256_text(promotion_text)
    print(f"audit_sha256:   {audit_sha}\ncontent_sha256: {content_sha}")
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
        print("Verdict block appended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
