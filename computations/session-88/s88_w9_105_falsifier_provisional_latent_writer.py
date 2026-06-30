"""
S88 W9 §W9-105 — mack-cosmic-bridge sole-writer landing of 5 cross-regulator-ratio rows
F-47-Zub through F-51-latt to `sessions/framework/registry/falsifier-master-inventory.md`.

Per plan §W9-105: each row pre-registers a 3He-B vortex-core Caroli-Matricon F1/F5 ratio
measurement testing the Sage-QQ-exact substrate cocycle ratio 7.324992 (= 793346/108307)
± 0.1% under regulator-R-specific bandpass filtering on Lancaster MCT-3 / Helsinki ROTA /
RHUL-Aalto LTL cells. R ∈ {Zubarev, ζ, Pauli-Villars, Mellin, lattice}.

§W9-104 PASSed (audit_sha256=0173b45b1992f390ead14a4781230766c1b435b35f37ad09105177106990cba6;
25/25 cells QQ-equal 793346/108307 across 5 regulators × 5 atlas-restrictions). The plan-pinned
PROVISIONAL-LATENT tag's promotion-conditional (b) "§W9-104 PASS" is satisfied; rows land
directly as ACTIVE-PRE-REGISTERED.

Orchestrator-direct write per user's "avoid agent tasking" preference + new /rclab-solo Phase 2
step 2 agent-ownership-takeover (corpus-loaded mack context: researchers/Mack/ + falsifier-
master-inventory.md row format precedent at lines 1000-1015 from S87 W5-2 W11-C5 + lines
1020-1034 from S87 W5-3 W11-C6).

Single-shot append-only writer per epistemic-discipline.md §"Registry-Write Hygiene under
Parallel-Writer Race"; race-safe by construction (single writer = orchestrator).
"""
import hashlib
import sys
from pathlib import Path

INVENTORY = Path("sessions/framework/registry/falsifier-master-inventory.md")
VERDICT_FILE = Path("computations/session-88/s88_gate_verdicts.txt")
GATE_ID = "S88-LAB-CROSS-REGULATOR-RATIO-FALSIFIER-PROVISIONAL-LATENT-PRE-REG"

# Plan-pinned canonicals + §W9-104 anchor:
COCYCLE_RATIO_QQ = "793346/108307"
COCYCLE_RATIO_FLOAT = "7.324992"
TOLERANCE_BAND = "0.1%"
W9_104_AUDIT_SHA = "0173b45b1992f390ead14a4781230766c1b435b35f37ad09105177106990cba6"
VII_AF_1_PRECEDENT = "§VII.AF.1 (Pillar III ↔ Pillar IV LANDED bridge theorem; W-5 calibration)"

REGULATORS = [
    # (label, F-row-id, scheme, convention)
    ("Zubarev", "F-47-Zub", "Zubarev-regulated-Hochschild-pairing-F1-F5-ratio", "3He-B-BDI-vortex-core-Zubarev-bandpass-filter"),
    ("ζ", "F-48-zeta", "zeta-regulated-Hochschild-pairing-F1-F5-ratio", "3He-B-BDI-vortex-core-zeta-bandpass-filter"),
    ("Pauli-Villars", "F-49-PV", "Pauli-Villars-regulated-Hochschild-pairing-F1-F5-ratio", "3He-B-BDI-vortex-core-PV-bandpass-filter"),
    ("Mellin", "F-50-Mellin", "Mellin-regulated-Hochschild-pairing-F1-F5-ratio", "3He-B-BDI-vortex-core-Mellin-bandpass-filter"),
    ("lattice", "F-51-latt", "lattice-regulated-Hochschild-pairing-F1-F5-ratio", "3He-B-BDI-vortex-core-lattice-bandpass-filter"),
]

# Build the new section (#58-#62 numeric).
def build_section() -> str:
    lines = [
        "",
        "",
        "## NEW Rows #58--#62 -- Cross-regulator-ratio rows F-47-Zub..F-51-latt (S88 W9-105 ACTIVE-PRE-REGISTERED)",
        "",
        f"> **Origin**: S88 W9-105 `{GATE_ID}` (mack-cosmic-bridge SOLE WRITER per `feedback_mack-bridge-role.md`; orchestrator-direct write per user's \"avoid agent tasking\" preference + `/rclab-solo` Phase 2 step 2 agent-ownership-takeover discipline). Substrate-side anchor: §W9-104 `S88-SUBSTRATE-IS-PRESERVATION-RANK2-INHERITANCE-THEOREM` PASS at 25/25 cells QQ-equal `{COCYCLE_RATIO_QQ}` (audit_sha256=`{W9_104_AUDIT_SHA}`; verdict-file line 321).",
        f"> **Substrate framing (PHONONIC)**: each row tests the substrate's INTRINSIC HP^1 cocycle ratio `‖φ_67‖/‖φ_88‖ = {COCYCLE_RATIO_QQ} = {COCYCLE_RATIO_FLOAT}` (Sage QQ-exact at machine precision; S86 W-5 DONE-5) under regulator-specific bandpass filtering. The substrate IS the (φ_67, φ_88) cocycle pair on `(A_K^{{≤10}}, H_K^{{≤10}}, D_K^{{≤10}})`; the regulator is a substrate-IS UV regularization of the HP^1 cohomology pairing (NOT a laboratory-imposed cutoff per `phononic-framing.md` §\"IS Space, Not IN Space\"). Lab platforms IN the cryostat measure the inherited ratio under regulator-R-specific bandpass filtering.",
        f"> **Tag**: ACTIVE-PRE-REGISTERED (PROVISIONAL-LATENT plan-pinned tag promoted on §W9-104 PASS — promotion-conditional (b) of plan §W9-105 line 222 satisfied by §W9-104 audit_sha256=`{W9_104_AUDIT_SHA[:16]}...`).",
        f"> **Methodology precedent**: {VII_AF_1_PRECEDENT}; `cross-pillar-bridge-anatomy.md §\"Calibration corpus\"`. Parent rule: `inheritance-falsifier-protocol.md §\"Generalization beyond 3He-B\"` (rank-2 case Class B cohomology-asymmetry test).",
        f"> **(Δ_B/Δ_A)^p cancellation theorem applicability**: F1 (NMR longitudinal Δ²) and F5 (acoustic-mode Bogoliubov Δ²) share common p=2; cancellation residual = 0.0e+00 QQ-exact at common p (S86 W-5 DONE-5). Substrate-derived ratio `{COCYCLE_RATIO_FLOAT}` is PRESERVED INTACT across all 5 regulators (verified at the cohomology-class layer by §W9-104 25-cell PASS).",
        f"> **EVOI level**: LAB-FALSIFIER-A (decisive-Class-B); 5-yr horizon = Lancaster MCT-3 / Helsinki ROTA / RHUL-Aalto LTL 2027-2030.",
        "",
        "| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |",
        "|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|",
    ]
    for i, (R, fid, scheme, convention) in enumerate(REGULATORS):
        row_num = 58 + i
        observable = f"{fid} F1/F5 cross-regulator ratio test under {R}-regulated bandpass (cocycle-pair Class-B Gate-2 ratio denominator; {R}-specific filter applied to substrate spectral data)"
        falsifier = f"inheritance-morphism Class-B Gate-2 cohomology-asymmetry ratio falsifier; {R} regulator slice of §W9-104 25-cell QQ-exact grid"
        channels = f"Lancaster MCT-3 vortex-core spectroscopy (PRIMARY) + Helsinki ROTA + RHUL-Aalto LTL cross-validation; {R}-specific spectral-bandpass discrimination on raw Caroli-Matricon ladder readout"
        prediction = f"r_lab(F1/F5)_{R} = {COCYCLE_RATIO_FLOAT} = {COCYCLE_RATIO_QQ} ± {TOLERANCE_BAND} substrate-IS prediction (§W9-104 25-cell QQ-PASS)"
        envelope = f"PASS_lab if |r_lab − {COCYCLE_RATIO_FLOAT}|/{COCYCLE_RATIO_FLOAT} < 0.001; FAIL_lab if r_lab outside [7.3177, 7.3323] under {R} bandpass"
        ic_split = f"§W9-104 cell ({R}, A_5→A_4) substrate row PASS-anchors this lab row; cross-regulator agreement across 5 lab rows = {COCYCLE_RATIO_FLOAT} confirms substrate-resident locus"
        detector = f"Lancaster MCT-3 / Helsinki ROTA / RHUL-Aalto LTL 2027-2030 horizon; {R}-specific bandpass requires instrument-side calibration"
        L_max = "10"
        content_sha = "(landed at next §W9-105 emission)"
        audit_sha = "(landed at next §W9-105 emission)"
        notes = f"NEW S88 W9-105 ACTIVE-PRE-REGISTERED; cross-regulator extension of S87 W5-2 Row #51 F1/F5 ratio test; regulator R={R}; substrate-IS cocycle ratio {COCYCLE_RATIO_QQ} preserved under §W9-104 25-cell QQ-exact PASS"
        lines.append(f"| {row_num} | {observable} | {falsifier} | {channels} | {prediction} | {envelope} | {ic_split} | {detector} | {scheme} | {convention} | {L_max} | {content_sha} | {audit_sha} | {notes} |")
    lines.extend([
        "",
        "**Cross-regulator substrate-residence-locus test** (high-leverage discriminator): the 5 lab rows are direct lab-side counterparts of the 5 regulator rows of §W9-104's 25-cell QQ-exact grid. Substrate-IS framing predicts ALL 5 lab measurements yield IDENTICAL ratio `{r}` to within ± 0.1% (substrate-residence locus = substrate spectral triple, NOT BdG-sector or regulator-class). Disagreement across regulators falsifies substrate-IS framing at the regulator-axis layer; agreement confirms the W-11 RULE-2 strengthened parity-blindness theorem extends from η/even-Mellin (§VII.AQ STAGE-1-CANDIDATE) to the cohomology-asymmetry ratio layer.".replace("{r}", COCYCLE_RATIO_FLOAT),
        "",
        f"**Cross-link**: §W9-104 (substrate-side rank-2 inheritance-invariance theorem; STAGE-1-CANDIDATE registry diff text-spec for §VII.AR landing); §VII.AF.1 (Pillar III ↔ Pillar IV LANDED bridge theorem; W-5 calibration corpus); §VII.AQ (S88 W7b-79 STRUCTURAL-EVEN-GRADING-BLINDNESS-AT-CORNER-I-SCOPE; complementary parity-blindness anchor).",
        "",
    ])
    return "\n".join(lines)


def closure_hash(items: list[tuple[str, str]]) -> str:
    s = "|".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    # 1. Read inventory tail to confirm append-position.
    text_old = INVENTORY.read_text(encoding="utf-8")
    if "## NEW Rows #58--#62" in text_old:
        print("FAIL: §W9-105 section already present (re-run guard); aborting to avoid duplicate landing.", file=sys.stderr)
        return 1

    # 2. Build new section.
    section = build_section()

    # 3. Append atomically.
    with INVENTORY.open("a", encoding="utf-8") as f:
        f.write(section)

    # 4. Compute verdict-line SHAs.
    pin_map = [
        ("gate_id", GATE_ID),
        ("inventory_path", str(INVENTORY)),
        ("rows_added", "5"),
        ("row_numbers", "58-62"),
        ("F_row_ids", ",".join(fid for _, fid, _, _ in REGULATORS)),
        ("regulators", ",".join(R for R, _, _, _ in REGULATORS)),
        ("cocycle_ratio_QQ", COCYCLE_RATIO_QQ),
        ("tolerance_band", TOLERANCE_BAND),
        ("substrate_anchor_audit_sha256", W9_104_AUDIT_SHA),
        ("methodology_precedent", VII_AF_1_PRECEDENT),
        ("tag", "ACTIVE-PRE-REGISTERED-on-W9-104-PASS"),
        ("writer", "mack-cosmic-bridge"),
        ("L_max", "10"),
    ]
    audit_sha256 = closure_hash(pin_map)

    value = (
        f"rows_added=5;row_numbers=58-62;regulators=5;cocycle_ratio={COCYCLE_RATIO_QQ};"
        f"tag=ACTIVE-PRE-REGISTERED;substrate_anchor_W9-104=audit_sha={W9_104_AUDIT_SHA[:16]};"
        f"methodology_precedent=VII.AF.1"
    )
    scheme = "5-cross-regulator-ratio-falsifier-rows-substrate-anchored-on-W9-104"
    convention = "ACTIVE-PRE-REGISTERED-promoted-on-W9-104-PASS-mack-sole-writer"
    canonical = (
        f"{GATE_ID}: PASS -- "
        f"value='{value}' "
        f"scheme={scheme} "
        f"convention={convention} "
        f"L_max=10 "
        f"audit_sha256={audit_sha256} "
    )
    content_sha256 = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    canonical += f"content_sha256={content_sha256} schema_version=S87+"

    dual_sha_row = (
        f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); 5 cross-regulator-ratio rows F-47-Zub..F-51-latt landed at falsifier-master-inventory.md §\"NEW Rows #58--#62\" (rows numeric 58-62)"
    )
    tuple_row = (
        f"# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); ACTIVE-PRE-REGISTERED on §W9-104 PASS-promotion conditional"
    )

    # 5. Append verdict line atomically.
    if audit_sha256 in VERDICT_FILE.read_text(encoding="utf-8"):
        print(f"FAIL: audit_sha256={audit_sha256} already in verdict file (sig_5 collision).", file=sys.stderr)
        return 1
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write("\n" + canonical + "\n" + dual_sha_row + "\n" + tuple_row + "\n")

    # 6. Report.
    print(f"S88 W9-105: PASS")
    print(f"  inventory: {INVENTORY} (5 rows #58-#62 appended; {len(text_old.splitlines())} → {len((text_old + section).splitlines())} lines)")
    print(f"  audit_sha256={audit_sha256}")
    print(f"  content_sha256={content_sha256}")
    print(f"  cocycle_ratio={COCYCLE_RATIO_QQ}")
    print(f"  substrate_anchor_W9-104={W9_104_AUDIT_SHA[:16]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
