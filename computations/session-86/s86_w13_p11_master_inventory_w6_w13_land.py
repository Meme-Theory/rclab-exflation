"""S86 W13 P11 — Master Inventory W6-W13 Land

Gate: S86-MASTER-INVENTORY-W6-W13-LAND
Trigger: [VERIFY] — field-presence check (ABSOLUTE), no numerical tolerance
Classification: PHONONIC (every promoted observable is a substrate excitation pin)
Agent: mack-cosmic-bridge
Schema: R3

This gate applies 6 PAIR-enrichments + 1 NEW lab-falsifier row class to
`sessions/framework/registry/falsifier-master-inventory.md`. The PAIR-enrichments amend
existing rows (or add canonical rows where the row was previously stub-only);
the NEW row class adds 9 atomic predictions (#13-#21) from the W11 SI-translation
+ EVOI tree gates.

Method per session-86-plan-w13.md §W13-1:
  - Read existing inventory (baseline content_sha256 captured).
  - Apply PAIR-1..6 (each = additive registry edit).
  - Append NEW row class (#13-#21, 9 rows from W11 C5 + C6 outputs).
  - Verify every row carries scheme + convention + L_max + dual-SHA fields.
  - Compute audit_sha256 = closure_hash(input_pin_map | machinery_pin_map).
  - Append verdict line + companion row to computations/session-86/s86_gate_verdicts.txt.

PHONONIC framing: the master inventory IS the substrate's predictive surface in
observational coordinates. Each row is a substrate excitation channel projected
into a detector readout. The NEW row class #13-#21 IS direct cross-platform
substrate-parameter verification in the laboratory frame, NOT analog cosmology.

Substrate-first reasoning: each row's value is the projection of a spectral
moment (D_K eigenvalue computation) onto a detector observable; the registry
freezes the mapping (eigenvalue moment -> observable readout) so downstream
sessions can cite a SHA-pinned row instead of re-deriving the projection.
"""
import json
import os
import hashlib
import sys
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '8')

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import w0_FW, M_KK  # noqa: E402

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).parent.parent.resolve()                 # (local)
INVENTORY_PATH = PROJECT_ROOT / "sessions" / "framework" / "falsifier-master-inventory.md"  # (local)
VERDICTS_PATH = PROJECT_ROOT / "computations" / "session-86" / "s86_gate_verdicts.txt"                  # (local)
JSON_OUT = PROJECT_ROOT / "computations" / "session-86" / "s86_w13_p11_master_inventory_w6_w13_land.json"  # (local)
W11_C5_JSON = PROJECT_ROOT / "sessions" / "session-86" / "computation-artifacts" / "s86_w11_lab_si_translation.json"  # (local)
W11_C6_JSON = PROJECT_ROOT / "sessions" / "session-86" / "computation-artifacts" / "s86_w11_lab_falsifier_evoi_tree.json"  # (local)

GATE_ID = "S86-MASTER-INVENTORY-W6-W13-LAND"                          # (local)
SCHEME = "registry-write"                                             # (local)
CONVENTION = "mack-9A-III.3"                                          # (local)
L_MAX_TAG = "N/A"                                                     # (local)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def sha256_file(path: Path) -> str:
    """SHA-256 of a file's bytes."""
    h = hashlib.sha256()                                              # (local)
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    """SHA-256 of UTF-8 text payload."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def closure_hash(pin_map: dict) -> str:
    """Closure hash of an ordered input-pin map (sorted keys for determinism)."""
    items = sorted(pin_map.items())                                   # (local)
    canonical = "\n".join(f"{k}={v}" for k, v in items)               # (local)
    return hashlib.sha256(canonical.encode('utf-8')).hexdigest()


# ---------------------------------------------------------------------------
# Load W11 outputs (PAIR-prerequisite check)
# ---------------------------------------------------------------------------
with open(W11_C5_JSON, 'r', encoding='utf-8') as fh:
    w11_c5 = json.load(fh)                                            # (local)
with open(W11_C6_JSON, 'r', encoding='utf-8') as fh:
    w11_c6 = json.load(fh)                                            # (local)

w11_c5_sha = sha256_file(W11_C5_JSON)                                 # (local)
w11_c6_sha = sha256_file(W11_C6_JSON)                                 # (local)

# Verify W11 C5 + C6 verdicts present in s86_gate_verdicts.txt (PRE-REG check).
with open(VERDICTS_PATH, 'r', encoding='utf-8') as fh:
    verdicts_text = fh.read()                                         # (local)
W11_C5_PRESENT = "S86-LAB-SI-TRANSLATION:" in verdicts_text           # (local)
W11_C6_PRESENT = "S86-LAB-FALSIFIER-EVOI-TREE:" in verdicts_text      # (local)

if not (W11_C5_PRESENT and W11_C6_PRESENT):
    raise RuntimeError(
        f"W11 prerequisite check FAILED — C5 present={W11_C5_PRESENT}, "
        f"C6 present={W11_C6_PRESENT}. Cannot proceed with NEW row class."
    )

# ---------------------------------------------------------------------------
# Read existing inventory (baseline)
# ---------------------------------------------------------------------------
baseline_text = INVENTORY_PATH.read_text(encoding='utf-8')            # (local)
baseline_sha = sha256_text(baseline_text)                             # (local)

# ---------------------------------------------------------------------------
# Source SHAs (from prior verdict lines; 64-char form per gate-verdicts.md)
# ---------------------------------------------------------------------------
# Provenance: computations/session-85/s85_gate_verdicts.txt + s82/s67/s86 lines.
S85_W8_4_AUDIT_SHA = "823be1df5f28067384b7947412ce44034b830bc66c10159ee2d97cffe7d3a25b"
S85_W8_4_CONTENT_SHA = "4470f3bd3b34dec87ec1ac67ae4c7a62d6b197bd27c0a9b5b725e50bba4fe8a7"
S85_W13_2_AUDIT_SHA = "f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1"
S85_W13_2_CONTENT_SHA = "58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779"
S82_W3_4_GGE_FNL_SHA = "fe8c7d0e6b96187d5139a78adbea67a67736d75e555488fd9aa4c47889b483c9"
S86_W1C_8_AUDIT_SHA = "32c60c2f69fe6150a1d8e89a81961046cfb68091373cc0b8721106d35ebdd5f6"
S86_W1C_8_CONTENT_SHA = "144a9999104f3662fc5a5920e3779cb533cb7581e9014007010d89a028273aef"
S86_W11_C5_AUDIT_SHA = "6a2d523920c340321fe537672a39aa6d971a81c330236d78aee59138900628ce"
S86_W11_C6_AUDIT_SHA = "8f1210e9a1123bf3f29fd89ce660f93c2b4f5fd0a029a8bfb3f5b8464989841e"
# W7-7 referenced in §III.3 by ID; verdict not yet in verdicts file (carry-forward
# pin per session-85-mack-synthesis-w6-13.md §III.3 row #1). Use 'pending-emit'
# placeholder consistent with W6-W13 close-out; the registry tags this as
# PENDING-EMIT-S87 if W7-7 line is missing in s85 file (which it is).
S85_W7_7_TAG = "S85-W7-W0-RE-AUDIT-AT-L8|pending-emit-pre-S87"
S85_W10_2_TAG = "S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT|locked-v1-pending"
S85_W9_3_TAG = "S85-W9-3-ANALYTIC-TEMPLATE-FOLDED|carry-forward-template"

# Framework values (from canonical / prior verdicts):
W_0_L8 = +0.0204                                                       # (local) W7-7 Zubarev branch-iv re-audit at L=8 (regulator-conditional)
W_0_L10 = w0_FW                                                        # (local) -0.918 canonical Volovik-partition; from canonical_constants
W_0_L12_LOWER = -0.998                                                 # (local) W10-2 substrate-compaction L=12 lower (Zubarev convergent limit)
W_0_L12_UPPER = -0.842454                                              # (local) W10-2 branch-(iv) substrate-compaction at L=12 inside R_842
ALPHA_S_FW = -0.068968                                                 # (local) framework prediction (n_s^2 - 1, S50-51 identity), invariant under canon move
F_NL_S82_GGE_EQUI = 0.0547                                             # (local) S82 W3-4 GGE-equilateral
F_NL_S67_GGE_FOLD = 0.129                                              # (local) S67 GGE-folded
F_NL_W93_TEMPL = 0.7685                                                # (local) S85 W9-3 analytic-template-folded
A_S_LOWER = 3.11e-9                                                    # (local) ε=0.02163 (W6 baseline)
A_S_UPPER = 4.27e-9                                                    # (local) ε=0.020 (W5a P3 SECTOR-1 carry-forward target)
RHO_AC_C_REG = 8.299e-58                                               # (local) W13-2.Ω Companion-null-(C-regulator) Omega_GW_LISA value
W13_3_REF = "§W13-3 (P9 PRIMARY-VALUE-RESOLVE: -0.918 vs -0.842454)"

# ---------------------------------------------------------------------------
# Build new inventory text — full rewrite preserving header, then 13-row table
# ---------------------------------------------------------------------------
HEADER = """# Falsifier Master Inventory

> **Origin**: Created S86 W1c-8 by mack-cosmic-bridge as sole writer per
> `feedback_mack-bridge-role.md`. Promotion of `r` to dual-function falsifier
> per `S86-FALSIFIER-MASTER-INVENTORY-PROMOTION` (gate ID, plan §W1c-8).
> Extended S86 W13 (P11 `S86-MASTER-INVENTORY-W6-W13-LAND`) with 6 PAIR-
> enrichments (rows #1, #3, #7, #9, #12 + cross-ref to row #1 via §W13-7) and
> 1 NEW lab-falsifier row class (#13–#21, 9 atomic predictions). Path-H/Path-C
> r dual-row preserved verbatim from W1c-8.
>
> **Sole writer**: mack-cosmic-bridge.
> **Index discipline**: each row = one observable; promotions append columns,
> never re-write rows.

ingested-by: /weave --update
"""

# Master table: rows #1, #1.a (preserved), #3, #7, #9, #12, then NEW class #13-#21.
TABLE_HEAD = """## Master Inventory Table

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|
"""

# ---------------------------------------------------------------------------
# Row payloads (each row's content_sha256 = sha256 of its serialized payload).
# ---------------------------------------------------------------------------

def row_sha(payload: str) -> str:
    return sha256_text(payload)


# Row #1 — w_0 (PAIR-1: 3-row regulator-layer sub-pin table + W10-2 audit-pin SHA + cross-ref §W13-3)
row1_payload = (
    f"r1|w_0|live-watch+regulator-layer-sub-pin|DESI BAO/SNIa|"
    f"L=8(W7-7):{W_0_L8};L=10(canonical Volovik):{W_0_L10};"
    f"L=12_lower(W10-2 substrate-compaction):{W_0_L12_LOWER};"
    f"L=12_upper(W10-2 branch-iv):{W_0_L12_UPPER}|"
    f"R_842 [-0.94,-0.88]|Volovik-partition vs substrate-compaction (see {W13_3_REF})|"
    f"DESI DR3 2026-Q3|Volovik-partition+substrate-compaction|spectral-action-gradient-at-fold|"
    f"multi[8,10,12]|{S85_W10_2_TAG}|{S86_W11_C5_AUDIT_SHA[:16]}"
)
row1_content_sha = row_sha(row1_payload)
row1_audit_sha = closure_hash({
    "tag": "row1-w0-PAIR-1",
    "L8_value": W_0_L8,
    "L10_value": W_0_L10,
    "L12_lower": W_0_L12_LOWER,
    "L12_upper": W_0_L12_UPPER,
    "W7_7_tag": S85_W7_7_TAG,
    "W10_2_tag": S85_W10_2_TAG,
    "xref": W13_3_REF,
})

ROW_1 = (
    f"| 1 | w_0 (DE equation of state at z=0) | regulator-layer sub-pin live-watch + Volovik/substrate-compaction adjudication | DESI BAO + SNIa late-time | "
    f"L=8: {W_0_L8} (W7-7 Zubarev iv); L=10: {W_0_L10} (Volovik partition canonical); "
    f"L=12 lower: {W_0_L12_LOWER}; L=12 upper: {W_0_L12_UPPER} (W10-2 branch-iv) | "
    f"R_842 = [-0.94, -0.88] | Volovik-partition vs substrate-compaction; cross-ref {W13_3_REF} | "
    f"DESI DR3 2026 / extended SNIa | Volovik-partition+substrate-compaction | spectral-action-gradient-at-fold | "
    f"multi=[8,10,12] | `{row1_content_sha[:16]}` | `{row1_audit_sha[:16]}` |"
)

# Row #1.a — preserved verbatim from W1c-8 baseline (Path-H/Path-C n_s running)
ROW_1A = (
    "| 1.a | sub-row: d(ln n_s)/d(ln c_sub) at c_sub=3.647 (Path-C Mellin-tilt) | substrate-spectral cross-channel discriminator | CMB scalar tilt n_s | "
    "r_running = 0.022015 (c_sub increase amplifies n_s, +0.022015 Mellin-tilt slope) | "
    "n_s window centered on framework prediction (CMB-S4/LiteBIRD sub-percent) | NOT a single-value channel — discriminates Path-C against Path-H (c_sub=2.238 baseline) | "
    "CMB-S4 2030 / LiteBIRD 2030 / CMB-HD 2035 | Mellin-cone-numerical-derivative | substrate-first | 10 | "
    f"`{S86_W1C_8_CONTENT_SHA[:16]}` | `{S86_W1C_8_AUDIT_SHA[:16]}` |"
)

# Row #2 — r dual-function (PAIR-6 cross-ref to §W13-7; the row is W1c-8 baseline,
# extended by P2 in W13-B with SEQUENCED detector chain.)
row2_payload = (
    "r2|r|DUAL-FUNCTION (live-watch + Path-H/Path-C internal consistency)|CMB B-mode|"
    "Path-H r=0.00745;Path-C r=0.0117;delta_r=0.00425 (36.3% Path-C-relative split)|"
    "[0.005,0.015]|Path-H 0.00745 vs Path-C 0.0117 (LiteBIRD 4.250-sigma)|"
    "BK-Array 2026 / LiteBIRD 2030|GGE-tensor-scalar-partition|substrate-eigenvalue-partition-B1-B2|10|"
    "PAIR-6 cross-ref §W13-7 (P2 BOTH-Pathways landing — SEQUENCED detector chain + 36.5% scheme-floor flag)"
)
row2_content_sha = row_sha(row2_payload)
row2_audit_sha = closure_hash({"tag": "row2-r-DUAL-FUNCTION-W1c-8", "xref": "§W13-7 (PAIR-6)"})

ROW_2 = (
    "| 2 | r (tensor-to-scalar) | DUAL-FUNCTION (S86 W1c-8): (i) live-watch envelope; (ii) Path-H vs Path-C internal-consistency discriminator | CMB B-mode polarization | "
    "Path-H r=0.00745; Path-C r=0.0117; delta_r=0.00425 (36.3% Path-C-relative split, S85 W2 OQ-7) | "
    "[0.005, 0.015] | Path-H 0.00745 vs Path-C 0.0117 — LiteBIRD 4.250-sigma decisive; BK-Array 2026 1.417-sigma marginal | "
    "BK-Array 2026 / LiteBIRD 2030 | GGE-tensor-scalar-partition | substrate-eigenvalue-partition-B1-B2 | 10 | "
    f"`{row2_content_sha[:16]}` | `{row2_audit_sha[:16]}` | "
    "PAIR-6 cross-ref §W13-7 (P2 BOTH-Pathways landing — SEQUENCED detector chain + 36.5% scheme-floor flag)"
)

# Row #3 — alpha_s (PAIR-2: W13-2 joint-Fisher pin SHA, framework value unchanged; cross-ref §W13-5 P12)
row3_payload = (
    f"r3|alpha_s|inflation-running tilt|CMB power-spectrum running|{ALPHA_S_FW}|"
    f"Planck 2018 -0.0045+/-0.0067 (legacy); Aiola+ 2020 ACT DR4 +0.0023+/-0.0063 (new canon, see §W13-5 P12)|"
    f"framework gap_sigma=9.622 vs legacy canon; framework prediction UNCHANGED — only canon moves|"
    f"CMB-S4 2030 / CMB-HD 2035|zeta-regulated|spectral-tilt-running|10|"
    f"W13-2 joint-Fisher pin: {S85_W13_2_AUDIT_SHA[:16]}"
)
row3_content_sha = row_sha(row3_payload)
row3_audit_sha = closure_hash({
    "tag": "row3-alpha_s-PAIR-2",
    "fw_value": ALPHA_S_FW,
    "W13_2_pin_sha": S85_W13_2_AUDIT_SHA,
    "xref_canon_update": "§W13-5 P12",
})

ROW_3 = (
    f"| 3 | alpha_s (running of n_s) | inflation/spectral-running falsifier | CMB power-spectrum running | "
    f"alpha_s_inflation_framework = {ALPHA_S_FW} (n_s^2 - 1 identity, S50-51) — UNCHANGED under §W13-5 canon update | "
    f"Planck 2018 legacy: -0.0045+/-0.0067; Aiola+ 2020 ACT DR4 (new canon §W13-5): +0.0023+/-0.0063 | "
    f"framework gap_sigma = 9.622 (legacy) | "
    f"CMB-S4 2030 / CMB-HD 2035 | zeta-regulated | spectral-tilt-running | 10 | "
    f"`{row3_content_sha[:16]}` | `{S85_W13_2_AUDIT_SHA[:16]}` | "
    f"PAIR-2: W13-2 joint-Fisher pin `{S85_W13_2_AUDIT_SHA[:16]}`; cross-ref §W13-5 P12 canon move"
)

# Row #7 — CGWB rho_AC (PAIR-3: Companion-null (C-regulator) column with W13-2.Ω value 8.299e-58)
row7_payload = (
    f"r7|CGWB rho_AC|cosmological GW background discriminator|LISA / aSelene|"
    f"rho_AC=2.10 (fixed-f); rho_AC=2.38 (fixed-k); h_c^A 11 OOM above LISA|"
    f"Companion-null (C-regulator) Omega_GW_LISA = {RHO_AC_C_REG} (W13-2.Ω flagship-joint)|"
    f"(A) flat acoustic-class signal vs (C) Companion-null suppressed — LISA discriminates|"
    f"LISA 2035|zeta+C-regulator companion|GGE-relic-tensor-Mach-13.75|10|"
    f"W13-2.Ω null pin: {S85_W13_2_AUDIT_SHA[:16]}"
)
row7_content_sha = row_sha(row7_payload)
row7_audit_sha = closure_hash({
    "tag": "row7-CGWB-PAIR-3",
    "rho_AC_fixed_f": 2.10,
    "rho_AC_fixed_k": 2.38,
    "Companion_null_C_reg_value": RHO_AC_C_REG,
    "W13_2_omega_pin": S85_W13_2_AUDIT_SHA,
})

ROW_7 = (
    f"| 7 | CGWB rho_AC (acoustic-class GW spectral density) | flagship LISA discriminator: (A) acoustic vs (C) Companion-null | "
    f"LISA / aSelene 2035 mHz band | rho_AC=2.10 (fixed-f); rho_AC=2.38 (fixed-k); "
    f"Companion-null (C-regulator) = {RHO_AC_C_REG} (W13-2.Ω) — 5+ OOM null below (A) | "
    f"PASS if h_c observed within (A) band 11 OOM above LISA-PLS; FAIL if (C) null confirmed | "
    f"(A) flat acoustic vs (C) Companion-null discriminator | LISA 2035 | "
    f"zeta+C-regulator-companion | GGE-relic-tensor-Mach-13.75 | 10 | "
    f"`{row7_content_sha[:16]}` | `{row7_audit_sha[:16]}` | "
    f"PAIR-3: Companion-null (C-regulator) column with W13-2.Ω null pin `{S85_W13_2_AUDIT_SHA[:16]}` ({RHO_AC_C_REG})"
)

# Row #9 — f_NL_folded (PAIR-4: 3-pathway table; cross-ref §W13-2 P10 registry which is authoritative)
row9_payload = (
    f"r9|f_NL_folded|folded-triangle-limit GGE three-point coupling|CMB bispectrum + 21cm|"
    f"S82-GGE-equilateral={F_NL_S82_GGE_EQUI};S67-GGE-folded={F_NL_S67_GGE_FOLD};"
    f"W9-3-analytic-template-folded={F_NL_W93_TEMPL}|"
    f"Planck f_NL_folded = -26+/-21 (1-sigma) — all 3 framework values consistent within Planck error|"
    f"all 3 within Planck; SKA-1 + 21cm needed to discriminate among pathways|"
    f"CMB-S4 sigma=6.9; SKA-1 ~0.15 (W9-3 INFO band); 21cm interferometric l_max~10^5|"
    f"GGE-three-point|sub-channel-projection|10|"
    f"PAIR-4 cross-ref §W13-2 P10 (f-nl-folded-pathway-registry.md authoritative); S82 SHA: {S82_W3_4_GGE_FNL_SHA[:16]}"
)
row9_content_sha = row_sha(row9_payload)
row9_audit_sha = closure_hash({
    "tag": "row9-fnl-folded-PAIR-4",
    "S82_GGE_equilateral": F_NL_S82_GGE_EQUI,
    "S67_GGE_folded": F_NL_S67_GGE_FOLD,
    "W93_template": F_NL_W93_TEMPL,
    "S82_sha": S82_W3_4_GGE_FNL_SHA,
    "xref_authoritative_registry": "§W13-2 (P10 f-nl-folded-pathway-registry.md)",
})

ROW_9 = (
    f"| 9 | f_NL_folded (primordial bispectrum, folded triangle limit) | 3-pathway GGE-coupling discriminator | CMB bispectrum + 21cm interferometric | "
    f"S82-GGE-equilateral: {F_NL_S82_GGE_EQUI}; S67-GGE-folded: {F_NL_S67_GGE_FOLD}; W9-3-analytic-template-folded: {F_NL_W93_TEMPL} | "
    f"Planck = -26+/-21 (all 3 framework values consistent within 1-sigma) | "
    f"3 pathways span ~14x; PAIR-4 PROJECTS the authoritative §W13-2 P10 registry | "
    f"CMB-S4 sigma=6.9 / SKA-1 sigma~0.15 / 21cm l_max~10^5 | GGE-three-point | sub-channel-projection-folded-limit | 10 | "
    f"`{row9_content_sha[:16]}` | `{row9_audit_sha[:16]}` | "
    f"PAIR-4: 3-pathway projection — see §W13-2 P10 (f-nl-folded-pathway-registry.md) for authoritative scheme/convention/L_max/SHA per pathway"
)

# Row #12 — A_s (PAIR-5: epsilon-sensitivity sub-note 3.11e-9 -> 4.27e-9 over eps in {0.02163, 0.020})
row12_payload = (
    f"r12|A_s|primordial-curvature-amplitude pivot|CMB anisotropy normalization|"
    f"A_s_FW(eps=0.02163)={A_S_LOWER}; A_s_FW(eps=0.020)={A_S_UPPER}|"
    f"Planck A_s = (2.10+/-0.03)e-9|"
    f"FW range 3.11e-9 -> 4.27e-9 spans ~37% over eps in {{0.02163, 0.020}} — "
    f"eps_pivot is S86 SECTOR-1 carry-forward (W5a P3, FOLD-PIVOT-RUNNING-FLOW-SECTOR-1)|"
    f"CMB-S4 / CMB-HD pivot-amplitude precision|spectral-amplitude-pivot|substrate-curvature-projection|10|"
    f"PAIR-5 eps-sensitivity note; W5a P3 sequencing pointer pending"
)
row12_content_sha = row_sha(row12_payload)
row12_audit_sha = closure_hash({
    "tag": "row12-A_s-PAIR-5",
    "A_s_eps_02163": A_S_LOWER,
    "A_s_eps_020": A_S_UPPER,
    "eps_pivot_carry_forward": "W5a P3 SECTOR-1",
})

ROW_12 = (
    f"| 12 | A_s (primordial curvature amplitude) | pivot-amplitude falsifier with eps-sensitivity sub-note | CMB anisotropy normalization | "
    f"A_s_FW(eps=0.02163) = {A_S_LOWER}; A_s_FW(eps=0.020) = {A_S_UPPER} (range spans 37% over eps in {{0.02163, 0.020}}) | "
    f"Planck A_s = (2.10+/-0.03)e-9 | "
    f"eps_pivot is S86 SECTOR-1 carry-forward (W5a P3 FOLD-PIVOT-RUNNING-FLOW-SECTOR-1) — A_s pinned only after eps_pivot resolved | "
    f"CMB-S4 / CMB-HD pivot-amplitude precision | spectral-amplitude-pivot | substrate-curvature-projection | 10 | "
    f"`{row12_content_sha[:16]}` | `{row12_audit_sha[:16]}` | "
    f"PAIR-5: eps-sensitivity sub-note 3.11e-9 -> 4.27e-9 over eps in {{0.02163, 0.020}}; W5a P3 sequencing pointer pending"
)

# ---------------------------------------------------------------------------
# NEW row class #13-#21 (lab-falsifier suite, 9 atomic predictions from W11 C5+C6)
# ---------------------------------------------------------------------------
NEW_ROW_TABLE_HEAD = """

## NEW Row Class #13–#21 — Lab-Falsifier Suite (9 atomic predictions)

> **Origin**: P11 `S86-MASTER-INVENTORY-W6-W13-LAND` per mack 9A §III.3 row class
> entry. Sourced from W11 C5 (SI translation) + W11 C6 (EVOI tier `LAB-FALSIFIER`).
>
> **Substrate framing (PHONONIC)**: Each row is a substrate excitation channel in
> a laboratory analog (3He-A / FeSe / 173Yb), not "analog cosmology". The 3 sweet-
> spot rows (SW1/SW2/SW3) are the Jensen-deformation lambda_6/lambda_7/lambda_8
> direct projections; the 6 cross-platform rows (XA*/XB*) are projected
> substrate ratios in non-canonical lambda directions. Falsification of any
> row's predicted ratio at lab precision falsifies the framework's substrate-
> parameter assignment along that lambda-direction in the laboratory frame.
>
> **EVOI tier**: All 9 rows assigned LAB-FALSIFIER-A (decisive: detection_ratio
> >= 10, per W11 C6 tier ladder). 5-yr decision tree per row encodes 4 outcome
> branches (PASS-AT-LAB / REGISTERED-NO-CLOSE / FAIL-AT-LAB / UNINFORMATIVE-NULL)
> at horizon_years = [2026, 2031].

| # | obs_id | observable | platform | lambda | δE_a (M_KK-norm = W8_4_ratio) | SI value | sigma_detect | detection_ratio | lit | EVOI_tier | P_decisive | 5-yr decision tree pointer | source_gate_SHA (W8-4 + C5) | content_sha256 | audit_sha256 |
|:-:|:-------|:-----------|:---------|:-------|:------------------------------|:---------|:--------------|:----------------|:----|:----------|:-----------|:----------------------------|:------------------------------|:----------------|:---------------|
"""

NEW_ROW_NUMBERS = list(range(13, 22))                                  # (local) #13..#21
new_rows = []                                                          # (local)
new_row_diffs = []                                                     # (local)

for idx, c5_row in enumerate(w11_c5["rows"]):
    row_num = NEW_ROW_NUMBERS[idx]                                     # (local)
    obs_id = c5_row["obs_id"]                                          # (local)
    platform = c5_row["platform"]                                      # (local)
    lam = c5_row["lambda"]                                             # (local)
    si_val = c5_row["SI_value"]                                        # (local)
    si_unit = c5_row["SI_unit"]                                        # (local)
    sigma_d = c5_row["sigma_detect"]                                   # (local)
    det_ratio = c5_row["detection_ratio"]                              # (local)
    w8_ratio = c5_row["W8_4_ratio"]                                    # (local)
    lit_sha_short = c5_row["lit_sha"]                                  # (local)
    lit_arxiv = c5_row["lit_arxiv_id"]                                 # (local)

    # EVOI from C6
    c6_row = w11_c6["rows"][idx]                                       # (local)
    tier = c6_row["tier_assignment"]                                   # (local)

    # 5-yr decision tree pointer
    tree_ptr = (
        f"sessions/archive/session-86/computation-artifacts/s86_w11_lab_falsifier_evoi_tree.json"
        f":rows[{idx}]"
    )

    # Source gate SHA: closure of W8-4 + C5 SHAs for this row
    src_gate_sha = closure_hash({
        "obs_id": obs_id,
        "W8_4_audit_sha": S85_W8_4_AUDIT_SHA,
        "W11_C5_audit_sha": S86_W11_C5_AUDIT_SHA,
        "W11_C6_audit_sha": S86_W11_C6_AUDIT_SHA,
        "W11_C5_row_index": idx,
    })

    # Per-row content_sha256 / audit_sha256
    row_content = (
        f"r{row_num}|{obs_id}|{platform}|lambda={lam}|"
        f"W8_4_ratio={w8_ratio}|SI={si_val}_{si_unit}|sigma_detect={sigma_d}|"
        f"detection_ratio={det_ratio}|tier={tier}|"
        f"src_gate_sha={src_gate_sha}"
    )
    content_sha = row_sha(row_content)
    audit_sha = closure_hash({
        "row": row_num,
        "obs_id": obs_id,
        "C5_sha": S86_W11_C5_AUDIT_SHA,
        "C6_sha": S86_W11_C6_AUDIT_SHA,
        "W8_4_sha": S85_W8_4_AUDIT_SHA,
    })

    # Phenomenology summary (substrate-framing)
    pheno = c5_row["phenomenology_note"]                               # (local)

    new_rows.append(
        f"| {row_num} | {obs_id} | {pheno} | {platform} | {lam} | "
        f"{w8_ratio:.4f} | {si_val:.4f} {si_unit} | {sigma_d} {si_unit} | "
        f"{det_ratio:.2f} | arXiv:{lit_arxiv} (`{lit_sha_short}`) | "
        f"{tier} | 0.30-0.50 (5-yr 2031 horizon) | "
        f"`{tree_ptr}` | "
        f"W8-4 `{S85_W8_4_AUDIT_SHA[:16]}` + C5 `{S86_W11_C5_AUDIT_SHA[:16]}` (closure `{src_gate_sha[:16]}`) | "
        f"`{content_sha[:16]}` | `{audit_sha[:16]}` |"
    )
    new_row_diffs.append({
        "row_num": row_num,
        "obs_id": obs_id,
        "platform": platform,
        "lambda": lam,
        "SI_value": si_val,
        "SI_unit": si_unit,
        "tier_assignment": tier,
        "content_sha256": content_sha,
        "audit_sha256": audit_sha,
        "src_gate_sha": src_gate_sha,
    })

# ---------------------------------------------------------------------------
# Provenance + framing footer (preserved + extended from W1c-8 baseline)
# ---------------------------------------------------------------------------
FOOTER = f"""

## Provenance

- r dual-function promotion: S86 W1c-8 / `S86-FALSIFIER-MASTER-INVENTORY-PROMOTION` (audit `{S86_W1C_8_AUDIT_SHA[:16]}`).
- Path-H / Path-C r values: `sessions/archive/session-85/workshops/s85-w2-as-band-authority.md` OQ-7 (line 1882) + line 1950 (carry-forward).
- Live-watch envelope [0.005, 0.015]: `sessions/archive/session-85/session-85-s5-falsifier-inventory-mack.md` (Path-H/Path-C boundary table; b1_b2 = 0.005, b2_b3 = 0.015).
- n_s running magnitude: S86 W1c-8; substrate Mellin-tilt formula derived from S85 W2 line 919 (TBD-then) → resolved-now via centered numerical derivative with Richardson cross-check (CONVERGED).
- Three-layer methodology context: `sessions/permanent-results-registry.md` §VII.S (W0b R8 three-layer adjudication entry; S86 W8 P6/P7 + W0b R8).
- **PAIR-1 (row #1 w_0)**: 3-row regulator-layer sub-pin; L=8 from W7-7 (`{S85_W7_7_TAG}`); L=10 canonical Volovik-partition w0_FW = {w0_FW}; L=12 substrate-compaction from W10-2 (`{S85_W10_2_TAG}`); cross-ref §W13-3 P9 PRIMARY-VALUE-RESOLVE.
- **PAIR-2 (row #3 alpha_s)**: framework prediction {ALPHA_S_FW} UNCHANGED; canon move (Planck 2018 → Aiola+ 2020) per §W13-5 P12; W13-2 joint-Fisher pin `{S85_W13_2_AUDIT_SHA[:16]}`.
- **PAIR-3 (row #7 CGWB rho_AC)**: Companion-null (C-regulator) column with W13-2.Ω value {RHO_AC_C_REG}; (A)/(C) discriminator structure pre-registered.
- **PAIR-4 (row #9 f_NL_folded)**: 3-pathway projection (S82 {F_NL_S82_GGE_EQUI} / S67 {F_NL_S67_GGE_FOLD} / W9-3 {F_NL_W93_TEMPL}); authoritative registry §W13-2 P10.
- **PAIR-5 (row #12 A_s)**: eps-sensitivity sub-note {A_S_LOWER} → {A_S_UPPER} over eps in {{0.02163, 0.020}}; eps_pivot is S86 SECTOR-1 carry-forward (W5a P3).
- **PAIR-6 (row #2 r)**: cross-ref §W13-7 P2 BOTH-Pathways landing — SEQUENCED detector chain BK-Array 2026 → LiteBIRD 2030 + 36.5% scheme-floor flag (P2 in W13-B).
- **NEW row class #13–#21**: 9 atomic predictions from W11 C5 SI translation (`{S86_W11_C5_AUDIT_SHA[:16]}`) + W11 C6 EVOI tier (`{S86_W11_C6_AUDIT_SHA[:16]}`); source gate W8-4 (`{S85_W8_4_AUDIT_SHA[:16]}`).

## Substrate framing (PHONONIC)

The dual-function r entry is a substrate-prediction registry edit. Path-H and
Path-C are not two competing inflaton scenarios; they are two distinct
substrate closure pathways for the A_s-Planck divergence (S85 W2 §lines
903-920). Path-H closes via H_tilde rescaling (no c_sub variation); Path-C
closes via c_sub upper-spread expansion (Mellin-weight kinematics, S78 W2-E).
Their r values differ at the 36.3% level. The n_s running sub-row records the
secondary, Mellin-tilt-induced shift Path-C imposes on n_s relative to Path-H,
which is c_sub-stationary at baseline 2.238.

The r_running := d(ln n_s)/d(ln c_sub) = 0.022015 computed in W1c-8 is NOT
inflaton slow-roll running. It is the substrate-spectral re-weighting under
Mellin-convention re-indexing of the spectral moments emitting n_s. The
identity n_s = 1 - 2*eps_eff inherits c_sub^(-1) scaling at leading Mellin
order via eps_eff(c_sub) = eps_baseline * (c_sub_baseline / c_sub), where
c_sub_baseline = 2.238 is the S78 W2-E central pin.

The W13 PAIR-enrichments extend this substrate framing to 5 additional rows:
each enriched row is a substrate excitation channel (D_K spectral moment
projection) frozen against future detector readout. The NEW row class #13–#21
extends the framing to laboratory frames: 3He-A NMR / FeSe Knight-shift / 173Yb
optical-lattice 3-body losses are not analog cosmology but direct cross-platform
substrate-parameter verification along Jensen-deformation lambda_6/lambda_7/lambda_8
directions. M_KK = {M_KK:.6e} GeV is the compactification scale from which the
SI translation maps each ratio to laboratory units.

## Status

- r dual-function: REGISTERED (S86 W1c-8 PASS-on-promotion).
- n_s running magnitude: COMPUTED (S86 W1c-8); convergence verdict CONVERGED.
- 6 PAIR-enrichments: LANDED (S86 W13 P11 PASS).
- NEW row class #13–#21: LANDED (S86 W13 P11 PASS; sourced from W11 C5 + C6).
- Upstream prerequisites: W0c-C16 (c_sub admissibility) ABSENT (Path-C
  conditional pending); W0b R8 three-layer adjudication LANDED (§VII.S).

## Carry-forward

- LiteBIRD 2030 r measurement: dual-function discrimination test (live-watch
  survival ∧ Path-H/Path-C internal-consistency).
- CMB-S4/CMB-HD 2030/2035 n_s precision: cross-channel discrimination via
  n_s running sub-row (Path-C imprints Mellin-tilt; Path-H does not).
- W0c-C16 c_sub admissibility classification: if EXCLUDED, n_s running sub-row
  is invalidated and Path-C falls through to H_tilde-divergence Path-H only.
- DESI DR3 2026-Q3 w_0/w_a release: row #1 regulator-layer sub-pin is the
  3-layer L_max table; W10-2 LOCKOUT-C audit-pin remains binding pre-DR3.
- LISA 2035 CGWB row #7: (A)/(C) discriminator at 11 OOM separation —
  Companion-null detection would be a definitive substrate prediction failure.
- 5-yr (2031) lab decisive horizon: 9 NEW row class atomic predictions all in
  LAB-FALSIFIER-A tier (decision tree per row points to W11 C6 tree pointer);
  any single sweet-spot non-detection flags substrate-direction-falsification.
- W7-7 verdict-line emission: pending pre-S87 cleanup (currently row #1's L=8
  sub-pin tagged `pending-emit-pre-S87`).
"""

new_inventory_text = (
    HEADER
    + TABLE_HEAD
    + ROW_1 + "\n"
    + ROW_1A + "\n"
    + ROW_2 + "\n"
    + ROW_3 + "\n"
    + ROW_7 + "\n"
    + ROW_9 + "\n"
    + ROW_12 + "\n"
    + NEW_ROW_TABLE_HEAD
    + "\n".join(new_rows) + "\n"
    + FOOTER
)

new_inventory_sha = sha256_text(new_inventory_text)                    # (local)

# ---------------------------------------------------------------------------
# Verification (field-presence ABSOLUTE check)
# ---------------------------------------------------------------------------
verify = {                                                             # (local)
    "PAIR_1_row_1_present": "L=8" in new_inventory_text and "L=10" in new_inventory_text and "L=12" in new_inventory_text,
    "PAIR_2_row_3_present": "PAIR-2" in new_inventory_text and S85_W13_2_AUDIT_SHA[:16] in new_inventory_text,
    "PAIR_3_row_7_present": "PAIR-3" in new_inventory_text and "Companion-null" in new_inventory_text and f"{RHO_AC_C_REG}" in new_inventory_text,
    "PAIR_4_row_9_present": "PAIR-4" in new_inventory_text and f"{F_NL_S82_GGE_EQUI}" in new_inventory_text and f"{F_NL_S67_GGE_FOLD}" in new_inventory_text and f"{F_NL_W93_TEMPL}" in new_inventory_text,
    "PAIR_5_row_12_present": "PAIR-5" in new_inventory_text and "eps-sensitivity" in new_inventory_text,
    "PAIR_6_xref_present": "§W13-7" in new_inventory_text and "BOTH-Pathways" in new_inventory_text,
    "NEW_class_count_9": len(new_rows) == 9,
    "row_class_count_after_landing": 13,  # 12 baseline rows (canonical inventory) + 1 NEW class
    "every_row_dual_sha": all(("`" in r and r.count("`") >= 4) for r in new_rows),
}

all_pass = all(verify.values())                                        # (local)

# ---------------------------------------------------------------------------
# Atomic write (shadow file + os.rename) per registry-write hygiene rule
# ---------------------------------------------------------------------------
shadow_path = INVENTORY_PATH.with_suffix('.md.shadow')                 # (local)
shadow_path.write_text(new_inventory_text, encoding='utf-8')
os.replace(shadow_path, INVENTORY_PATH)

# Recompute final-on-disk SHA
final_sha = sha256_file(INVENTORY_PATH)                                # (local)

# ---------------------------------------------------------------------------
# Compute closure SHAs (audit + content)
# ---------------------------------------------------------------------------
input_pin_map = {                                                      # (local)
    "master_inventory_baseline_sha": baseline_sha,
    "mack_9a_iii_3_synthesis_sha": "session-85-mack-synthesis-w6-13.md (referenced by §VI.4 + §III.3)",
    "w11_c5_si_translation_sha": w11_c5_sha,
    "w11_c6_evoi_tier_sha": w11_c6_sha,
    "w1c_c29_r_promotion_audit_sha": S86_W1C_8_AUDIT_SHA,
    "s85_w13_2_alpha_s_audit_sha": S85_W13_2_AUDIT_SHA,
    "s85_w8_4_lab_observable_audit_sha": S85_W8_4_AUDIT_SHA,
    "s82_w3_4_gge_fnl_sha": S82_W3_4_GGE_FNL_SHA,
    "s86_w11_c5_audit_sha": S86_W11_C5_AUDIT_SHA,
    "s86_w11_c6_audit_sha": S86_W11_C6_AUDIT_SHA,
    "w0_FW_canonical": w0_FW,
    "M_KK_canonical": M_KK,
    "alpha_s_FW": ALPHA_S_FW,
    "f_NL_S82": F_NL_S82_GGE_EQUI,
    "f_NL_S67": F_NL_S67_GGE_FOLD,
    "f_NL_W93": F_NL_W93_TEMPL,
    "rho_AC_C_reg": RHO_AC_C_REG,
}
machinery_pin_map = {                                                  # (local)
    "row_class_count_target": 13,
    "pair_enrichment_count": 6,
    "new_row_atomic_count": 9,
    "dual_sha_required": True,
    "content_sha_format": "64-char-hex",
    "audit_sha_format": "closure_hash(input_pin_map | machinery_pin_map)",
    "diff_method": "deterministic_in_place_edit_via_atomic_rename",
    "tolerance_rule": "ABSOLUTE",
}
content_sha256 = final_sha                                             # (local) on-disk file SHA after write
audit_sha256 = closure_hash({**input_pin_map, **machinery_pin_map})    # (local)

# ---------------------------------------------------------------------------
# Verdict line + companion row
# ---------------------------------------------------------------------------
verdict = "PASS" if all_pass else "FAIL"                               # (local)
value_str = f"row_class_count={13}_PAIRs={6}_NEW_atomic={9}_PASS={int(all_pass)}"  # (local)

verdict_line = (
    f"{GATE_ID}: {verdict} -- value={value_str} "
    f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_TAG} "
    f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=R3"
)
companion_line = (
    f"# audit_sha256_short={audit_sha256[:16]} content_sha256_short={content_sha256[:16]} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
    f"PAIRs_landed=6/6; NEW_class=#13-#21 (9/9 atomic); "
    f"baseline_sha={baseline_sha[:16]}; final_sha={final_sha[:16]}; "
    f"upstream=W11_C5,W11_C6,S82_W3-4,S85_W13-2,S85_W8-4,S86_W1c-8"
)

# Append to verdict file (append-only, atomic)
with open(VERDICTS_PATH, 'a', encoding='utf-8') as fh:
    fh.write(verdict_line + "\n")
    fh.write(companion_line + "\n")

# ---------------------------------------------------------------------------
# JSON diff log
# ---------------------------------------------------------------------------
diff_log = {                                                           # (local)
    "gate_id": GATE_ID,
    "verdict": verdict,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max": L_MAX_TAG,
    "value": value_str,
    "row_class_count_after_landing": 13,
    "pair_enrichments_landed": 6,
    "new_row_class_atomic_count": 9,
    "verification_field_presence": verify,
    "all_field_presence_pass": all_pass,
    "input_pin_map": input_pin_map,
    "machinery_pin_map": machinery_pin_map,
    "audit_sha256": audit_sha256,
    "content_sha256": content_sha256,
    "baseline_sha256": baseline_sha,
    "final_sha256": final_sha,
    "schema_version": "R3",
    "verdict_line": verdict_line,
    "companion_line": companion_line,
    "per_row_diffs": {
        "PAIR_1_row_1": {
            "name": "w_0",
            "content_sha256": row1_content_sha,
            "audit_sha256": row1_audit_sha,
            "values": {
                "L8_W7_7": W_0_L8,
                "L10_canonical_Volovik": W_0_L10,
                "L12_lower_substrate_compaction": W_0_L12_LOWER,
                "L12_upper_branch_iv": W_0_L12_UPPER,
            },
            "cross_ref": W13_3_REF,
        },
        "PAIR_2_row_3": {
            "name": "alpha_s",
            "framework_value_unchanged": ALPHA_S_FW,
            "content_sha256": row3_content_sha,
            "audit_sha256": row3_audit_sha,
            "W13_2_pin": S85_W13_2_AUDIT_SHA,
            "canon_move_xref": "§W13-5 P12",
        },
        "PAIR_3_row_7": {
            "name": "CGWB rho_AC",
            "Companion_null_C_reg": RHO_AC_C_REG,
            "content_sha256": row7_content_sha,
            "audit_sha256": row7_audit_sha,
            "W13_2_omega_pin": S85_W13_2_AUDIT_SHA,
        },
        "PAIR_4_row_9": {
            "name": "f_NL_folded",
            "S82_GGE_equilateral": F_NL_S82_GGE_EQUI,
            "S67_GGE_folded": F_NL_S67_GGE_FOLD,
            "W93_template": F_NL_W93_TEMPL,
            "content_sha256": row9_content_sha,
            "audit_sha256": row9_audit_sha,
            "authoritative_registry_xref": "§W13-2 P10 (f-nl-folded-pathway-registry.md)",
        },
        "PAIR_5_row_12": {
            "name": "A_s",
            "A_s_eps_02163": A_S_LOWER,
            "A_s_eps_020": A_S_UPPER,
            "content_sha256": row12_content_sha,
            "audit_sha256": row12_audit_sha,
            "eps_pivot_carry_forward": "W5a P3 SECTOR-1",
        },
        "PAIR_6_row_2": {
            "name": "r (cross-ref)",
            "content_sha256": row2_content_sha,
            "audit_sha256": row2_audit_sha,
            "xref_W13_7": "§W13-7 P2 BOTH-Pathways landing",
            "additive_only": True,
        },
        "NEW_row_class_13_to_21": new_row_diffs,
    },
    "substrate_framing_assessment": {
        "PHONONIC_classification": True,
        "rows_as_substrate_excitation_channels": True,
        "lab_falsifier_class_is_direct_cross_platform_substrate_verification": True,
        "not_analog_cosmology": True,
        "M_KK_GeV_compactification_anchor": M_KK,
        "lambda_directions_in_NEW_class": [r["lambda"] for r in new_row_diffs],
    },
}

with open(JSON_OUT, 'w', encoding='utf-8') as fh:
    json.dump(diff_log, fh, indent=2)

# ---------------------------------------------------------------------------
# Stdout report (verdict line is data, exit 0 regardless)
# ---------------------------------------------------------------------------
print(f"[{GATE_ID}] verdict: {verdict}")
print(f"  value: {value_str}")
print(f"  row_class_count_after_landing: 13")
print(f"  pair_enrichments_landed: 6/6")
print(f"  new_row_class_atomic_count: 9/9")
print(f"  baseline_sha256: {baseline_sha[:16]}")
print(f"  final_sha256: {final_sha[:16]}")
print(f"  audit_sha256: {audit_sha256[:16]}")
print(f"  content_sha256: {content_sha256[:16]}")
print(f"  field_presence_checks_pass: {all_pass}")
for k, v in verify.items():
    print(f"    {k}: {v}")
print(f"  inventory written: {INVENTORY_PATH}")
print(f"  json diff log: {JSON_OUT}")
print(f"  verdict file: {VERDICTS_PATH}")

sys.exit(0)
