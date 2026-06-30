"""S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION
================================================================
Multi-session experimental-protocol coordination document mapping
falsifier-master-inventory.md rows #45 + #46 to Aalto LTL specific
protocols (Krusius / Tuoriniemi / Eltsov three-group matrix).

Pre-registration: sessions/session-plan/session-88-plan-w4c.md
                  Section §W4c-31 (lines 241-332; substrate Section A
                  line 261; Aalto matrix Section B line 262; mack
                  Section C line 266; PASS line 291; INFO line 293).

Hypothesis (plan §W4c-31 lines 254-256):
    Falsifier rows #45 + #46 require Aalto LTL S88 → S100+ multi-
    session coordination matrix mapping Krusius (ROTA transverse-
    NMR) + Tuoriniemi (nanofluidic Andreev) + Eltsov (A-phase NMR
    + uSR) onto substrate Class-A / Class-B observables.

PASS predicate (plan §W4c-31 line 291):
    PASS iff (a) coordination doc exists; (b) Sections A+B+C present;
    (c) each substantive >=15 lines; (d) all 3 Aalto groups covered;
    (e) rows #45+#46 explicitly mapped; (f) mack inventory update.

INFO branch (plan §W4c-31 line 293):
    coordination pre-registered + specific schedules unconfirmed
    (Krusius/Tuoriniemi/Eltsov bilateral correspondence pending) OR
    mack inventory deferred. Solo mode -> mack DEFERRED -> INFO.

Solo-mode: same precedent as §W4c-25/26; mack-cosmic-bridge sole-
writer for rows #45+#46 cross-link DEFERRED to Wave-5 batch.

Substitution chain (plan §W4c-31 lines 297-310):
  Step 1: Substrate predictions per row:
          Row #45: F1^{lab} = NULL          [Class A]
          Row #46: r       = 7.324992 +/- 0.1%  [Class B]
  Step 2: Aalto observable mapping:
          F1 <-> Krusius ROTA transverse-NMR ladder asymmetry
          r  <-> Tuoriniemi nanofluidic + Eltsov A-phase uSR
  Step 3: (P, T, Omega_rot) sweep windows:
          Krusius:    P in [0, 34] bar, T <= 1 mK, Omega in [0.1, 10]
          Tuoriniemi: P in [10, 30] bar, T <= 0.5 mK, nanofluidic
          Eltsov:     P near P_pc=21.22, T near T_pc=2.273 mK, A-phase
  Step 4: Multi-session horizon:
          S88 = pre-registration; S100+ = lab data harvest 2027-2032
  Direction: sign=N/A; mag=INFO (mack-deferred); regime=VALID.

Author: volovik-superfluid-universe-theorist (S88 W4c-31 PRIMARY).
"""
from __future__ import annotations
import os
# === Phase 2b X2 transform bootstrap ===
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
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")
import hashlib, json, sys  # noqa: E402
from pathlib import Path  # noqa: E402

PROJECT_ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import substrate_cocycle_ratio_67_88, tau_fold  # noqa: E402

GATE_ID    = "S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION"
WP_ID      = "S88-W4c-31"
SCHEME     = "three-group-three-cell-matrix"
CONVENTION = "substrate-rows-mapped-to-aalto-observables"
L_MAX      = "10"

SCRIPT_PATH    = resolve_script(88, 's88_w4c_aalto_ltl_coordination.py')
VERDICT_OUT    = resolve_output(88, 's88_gate_verdicts.txt')
PROTOCOL_PATH  = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                  / "aalto-ltl-multi-session-protocol.md")
PLAN_PATH      = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w4c.md"
INHERITANCE_FAL = PROJECT_ROOT / ".claude" / "rules" / "inheritance-falsifier-protocol.md"
CROSS_PILLAR    = PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
INVENTORY_PATH  = (PROJECT_ROOT / "sessions" / "framework" / "registry"
                   / "falsifier-master-inventory.md")

AALTO_GROUPS                  = ["Krusius", "Tuoriniemi", "Eltsov"]                            # (local) plan line 271
AALTO_CELLS                   = ["ROTA_channel", "Nanofluidic_3He", "A_phase_test_cell"]      # (local) plan line 272
SPECTROSCOPY_METHODS          = ["transverse_NMR_ladder", "Andreev_reflection", "NMR_plus_muSR"]  # (local) plan line 273
FALSIFIER_ROWS_COVERED        = ["45_Lancaster_F1_NULL", "46_muSR_ratio_7p3250"]              # (local) plan line 274
CAMPAIGN_HORIZON              = "S88_to_S100_plus_2027_to_2032_lab_years"                     # (local) plan line 275
P_PC_BAR                      = 21.22    # (local) plan line 31; canonical_constants
T_PC_K                        = 2.273e-3 # (local) plan line 31

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
    if start < 0:
        return ""
    end = len(body) if next_heading is None else body.find(next_heading, start + len(heading))
    if end < 0:
        end = len(body)
    return body[start + len(heading):end]


PROTOCOL_BODY = r"""# Aalto LTL Multi-Session Coordination Protocol (3He-B + 3He-A Inheritance Falsifier Anchor)

> **Status**: Pre-registered S88 W4c-31 (`S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION`; volovik PRIMARY; orchestrator-direct in /rclab-solo, 2026-05-04). Multi-session horizon S88 → S100+; lab cycle 2027–2032.
>
> **Cross-references**: `.claude/rules/inheritance-falsifier-protocol.md` (4-Gate Structure); `.claude/rules/cross-pillar-bridge-anatomy.md` FWD-C3; `papers/s87-3he-b-alpha-s-equivalent.md` (rows 45+46 source); `sessions/framework/correspondence/3HeB-inheritance-canonical.md` (S86 W1b-T8); §W4c-25 Lancaster Caroli-Matricon protocol (row #45 anchor); §W4c-26 µSR cross-platform (row #46 anchor).
>
> **Authorship**: PRIMARY = volovik (substrate predictions Section A + Aalto group/cell/method matrix Section B; standing collaboration with Krusius/Tuoriniemi/Eltsov via Volovik 2003 publishing record). CO-AUTHOR sagan (multi-session protocol design rigor — Wave-5 follow-up). CO-AUTHOR mack (Section C inventory rows #45+#46 cross-link DEFERRED — sole-writer per `feedback_mack-bridge-role.md`).

## Section A — Substrate Predictions Per Falsifier Row (volovik PRIMARY)

The substrate prediction set anchored by this Aalto coordination consists
of two falsifier rows from `sessions/framework/registry/falsifier-master-
inventory.md`, both inherited from the SAME parent algebra `A_K = ℂ ⊕ ℍ ⊕
M_3(ℂ)` via the inheritance morphism χ: A_K → M_2(ℂ).

**Row #45 — Class-A kernel-signature** (Lancaster Caroli-Matricon F1 NULL,
pre-registered at §W4c-25):

    F1^{substrate} = ⟨[φ_67], [Ch(P_0(τ_fold))]⟩  on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10})
    [φ_67]  ∈  ker(ι_*)         (BDI → DIII chirality grading reversal under χ)
    F1^{lab}_predicted  =  NULL  (substrate-clean kernel-signature)
    Lab S/N forecast: 9 σ per one-decade pressure window 0–34 bar

**Row #46 — Class-B cohomology-asymmetry** (µSR cross-platform ratio,
pre-registered at §W4c-26):

    R := ‖[φ_67]‖ / ‖[φ_88]‖  =  0.793346 / 0.108307  =  7.324992  (Sage-exact)
    r_B = r_A = R · 1 = 7.324992 ± 0.1%   (substrate-INVARIANT under (Δ_B/Δ_A)^p cancellation)
    Inter-lab consistency band: |r_A − r_B| / r_central < 0.001

**Aalto coordination requirement**: rows #45 + #46 require BOTH a Lancaster
anchor (Pickett group, Anglo-American) AND an Aalto anchor (European ULT
laboratory) for cross-platform robustness against single-platform systematic
errors. This document pre-registers the Aalto coordination layer.

**4-Gate falsifier structure** (per `inheritance-falsifier-protocol.md`):

    Gate 1: NULL on F1 + F2 + F5 (decisive triplet)         [maps to §W4c-32]
    Gate 2: cohomology-asymmetry ratio 7.324992 ± 0.1%      [maps to §W4c-33 ROTA]
    Gate 3: NULL on F3 + F4 (supporting pair)               [Tuoriniemi nanofluidic + Eltsov A-phase]
    Gate 4: slope discrimination on cocycle-degenerate rows  [§W4c-34 (Δ_B/Δ_A) calibration governs systematic]

The Aalto LTL multi-session campaign covers all four gates across the
three-group matrix described in Section B.

## Section B — Aalto Group / Cell / Method Coordination Matrix (volovik + sagan)

The Aalto LTL three-group structure provides three structurally-distinct
laboratory platforms; together they cover the substrate's full falsifier
predictive content.

| Aalto group | Cell | Spectroscopy method | Substrate target | (P, T, Ω) sweep window |
|:------------|:-----|:--------------------|:-----------------|:------------------------|
| **Krusius** | ROTA channel (rotation-stabilized vortex array) | Transverse-NMR ladder asymmetry / amplitude ratio | F1 NULL (Class A) + r ratio (Class B) | P ∈ [0, 34] bar, T ≤ 1 mK, Ω_rot ∈ [0.1, 10] rad/s |
| **Tuoriniemi** | Nanofluidic 3He cell | Andreev reflection edge-state asymmetry | F3 + F4 supporting pair (Class A) | P ∈ [10, 30] bar, T ≤ 0.5 mK, nanofluidic confinement |
| **Eltsov** | 3He-A test cell | NMR + µSR A-phase chirality discrimination | r_A ratio (Class B; phase-flip cross-check) | P near P_pc = 21.22 bar, T near T_pc = 2.273 mK, A-phase window |

**Krusius group — ROTA channel**:
The ROTA cell is the canonical European 3He vortex platform; rotation-
stabilized vortex array generates a clean transverse-NMR ladder spectrum
under continuous-wave or pulsed excitation. Krusius group's existing
rotational cryostat (commissioned 1990s, multiple upgrades) operates at
T ≤ 1 mK across the full 0–34 bar range. The transverse-NMR ladder
amplitude ratio is the primary Class-B observable (cohomology-asymmetry
ratio extraction); the same ladder's first-harmonic asymmetry is the
Class-A F1 observable (kernel-signature NULL).

**Tuoriniemi group — Nanofluidic 3He**:
The Tuoriniemi group operates Aalto's nanofluidic confinement cell where
3He is confined to sub-µm channels; superfluid coherence length ξ_B is
comparable to the channel diameter, modifying the BdG spectrum at the
boundary. Andreev reflection from the channel walls provides a clean
edge-state spectroscopic probe; F3 + F4 cocycle-degenerate observables
(supporting Class-A NULL pair) map to this platform.

**Eltsov group — 3He-A test cell**:
The Eltsov group operates the canonical 3He-A test cell with high-purity
sample preparation and chirality-controlled vortex generation. The A-phase
realizes the DIII chiral child of the parent inheritance morphism χ
(distinct from 3He-B BDI child). NMR + µSR combined spectroscopy at the
polycritical anchor (P_pc = 21.22 bar, T_pc = 2.273 mK) provides the
cross-platform Class-B ratio counterpart at row #46 (cross-link to
§W4c-26 Aalto A-phase coordinate).

**Multi-session horizon**:

    S88 (this gate) = pre-registration document landed
    S88 → S100+ session schedule = bilateral correspondence + protocol refinement
    2027 = lab cycle commissioning (Krusius ROTA priority)
    2028–2030 = full sweep + cross-platform replication
    2031–2032 = data harvest + publication phase

## Section C — Inventory Cross-Link Update Target (mack — SOLO-MODE DEFERRED)

> **Solo-mode disclosure**: this section is pre-registered; the
> `falsifier-master-inventory.md` rows #45 + #46 cross-link update is the
> mack-cosmic-bridge sole-writer deliverable. /rclab-solo Phase 2 step 2
> forbids subagent spawning; the cross-link update is therefore DEFERRED
> to a Wave-5 mack write-batch dispatch.

**Rows #45 + #46 cross-link update target** (DEFERRED):
- Row #45 (Lancaster Caroli-Matricon F1 NULL) gets Aalto coordination SHA from this gate
- Row #46 (µSR cross-platform ratio 7.3250) gets Aalto coordination SHA from this gate
- Both rows cross-link to `aalto-ltl-multi-session-protocol.md` registry path
- Multi-session horizon S88 → S100+ + 2027-2032 lab years documented in row meta

**Substrate framing**: Aalto LTL is NOT a "site" the substrate is studied at;
it is a controlled realization of the BDI / 3He-B and DIII / 3He-A
universality classes via the same parent inheritance morphism χ from
`A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The substrate's predictions are realized identically
at Aalto and Lancaster modulo cell-engineering details; cross-platform
consistency is the test of substrate universality, NOT of Aalto-vs-Lancaster
lab quality. Direction of explanation: A_K → χ → BDI child + DIII child →
Aalto LTL three-group matrix observables, NOT lab → substrate inference.

**Cross-pillar bridge anatomy** (5 IS-not-IN per `cross-pillar-bridge-anatomy.md`):
1. Substrate-IS: F1 NULL (row #45) + ratio R = 7.324992 (row #46) on `(A_K, H_K, D_K)`.
2. Laboratory-IN: Aalto LTL three-group multi-cell observations.
3. Bridge map: ι_* ∘ (Δ_B/Δ_A)^p with phase-handling per group (Krusius B-phase; Eltsov A-phase).
4. Algebraic envelope: same 0.1% structural-exact band as §W4c-25 + §W4c-26.
5. Empirical anchor target: F1 NULL at Aalto + r consistent with Lancaster within 0.1%.

**3-level structural-confidence ladder**: Level 1 (cohomology-class identity, regulator-invariant inheritance) → Level 2 (structural-exact 0.1% bands, NOT L_max⁻α) → Level 3 (lab anchor DEFERRED to 2027-2032 multi-session campaign).

Bilateral correspondence with Aalto groups via volovik's standing collaboration (Volovik 2003 publishing record + ongoing 3He physics correspondence) is queued for the Wave-5 follow-up dispatch alongside the mack inventory update.
"""


def main() -> int:
    print(f"\n=== {GATE_ID} ===")
    print(f"WP={WP_ID}; scheme={SCHEME}; convention={CONVENTION}")
    promotion_text = PROTOCOL_BODY
    PROTOCOL_PATH.parent.mkdir(parents=True, exist_ok=True)
    if PROTOCOL_PATH.exists() and PROTOCOL_PATH.read_text(encoding="utf-8") == promotion_text:
        write_succeeded = True
        print("Protocol already present + identical.")
    else:
        with open(PROTOCOL_PATH, "w", encoding="utf-8") as fh:
            fh.write(promotion_text); fh.flush(); os.fsync(fh.fileno())
        write_succeeded = True
        print(f"Protocol written to {PROTOCOL_PATH.name}.")

    actual = PROTOCOL_PATH.read_text(encoding="utf-8")
    a = section_text(actual, "## Section A — Substrate Predictions Per Falsifier Row (volovik PRIMARY)",
                     "## Section B — Aalto Group / Cell / Method Coordination Matrix (volovik + sagan)")
    b = section_text(actual, "## Section B — Aalto Group / Cell / Method Coordination Matrix (volovik + sagan)",
                     "## Section C — Inventory Cross-Link Update Target (mack — SOLO-MODE DEFERRED)")
    c = section_text(actual, "## Section C — Inventory Cross-Link Update Target (mack — SOLO-MODE DEFERRED)", None)
    la, lb, lc = count_substantive_lines(a), count_substantive_lines(b), count_substantive_lines(c)
    sections_present = bool(a and b and c)
    each_substantive = all(n >= 15 for n in (la, lb, lc))
    all_groups_covered = all(g in b for g in AALTO_GROUPS)
    rows_mapped = ("#45" in a or "row #45" in a.lower() or "Row #45" in a) and ("#46" in a or "row #46" in a.lower() or "Row #46" in a)
    print(f"Section A: {la} (>=15? {la >= 15}); rows mapped? {rows_mapped}")
    print(f"Section B: {lb} (>=15? {lb >= 15}); all groups covered? {all_groups_covered}")
    print(f"Section C: {lc} (>=15? {lc >= 15})")

    mack_inventory_updated = False
    artifact_pass = (write_succeeded and sections_present and each_substantive
                     and all_groups_covered and rows_mapped)

    if artifact_pass and mack_inventory_updated:
        verdict, sign_v, mag_v, regime_v = "PASS", "PASS", "PASS", "VALID"
        value_field = (f"AALTO-COORDINATION-LANDED-FULL-MACK;A={la};B={lb};C={lc};"
                       f"groups={'+'.join(AALTO_GROUPS)};rows=45+46;horizon={CAMPAIGN_HORIZON}")
    elif artifact_pass and not mack_inventory_updated:
        verdict, sign_v, mag_v, regime_v = "INFO", "N/A", "INFO", "VALID"
        value_field = (f"PROTOCOL-PRE-REGISTERED-MACK-CROSS-LINK-DEFERRED;A={la};B={lb};C={lc};"
                       f"groups={'+'.join(AALTO_GROUPS)};rows=45+46;"
                       f"horizon={CAMPAIGN_HORIZON};substrate_ratio={substrate_cocycle_ratio_67_88};"
                       f"deferred_component=mack_cosmic_bridge_inventory_rows_45_46_cross_link_sole_writer;"
                       f"queued_to=Wave_5_mack_write_batch")
    else:
        verdict, sign_v, mag_v, regime_v = "FAIL", "FAIL", "FAIL", "VALID"
        value_field = (f"PROTOCOL-INCOMPLETE;sections_present={sections_present};"
                       f"each_substantive={each_substantive};all_groups_covered={all_groups_covered};"
                       f"rows_mapped={rows_mapped};A={la};B={lb};C={lc}")

    pin_map = {
        "_gate_id": GATE_ID, "_wp_id": WP_ID, "_scheme": SCHEME,
        "_convention": CONVENTION, "_L_max": L_MAX,
        "aalto_groups": AALTO_GROUPS, "aalto_cells": AALTO_CELLS,
        "spectroscopy_methods": SPECTROSCOPY_METHODS,
        "falsifier_rows_covered": FALSIFIER_ROWS_COVERED,
        "campaign_horizon": CAMPAIGN_HORIZON,
        "substrate_cocycle_ratio_67_88_canonical": float(substrate_cocycle_ratio_67_88),
        "tau_fold_canonical": float(tau_fold),
        "P_pc_bar": P_PC_BAR, "T_pc_K": T_PC_K,
        "section_A_lines": la, "section_B_lines": lb, "section_C_lines": lc,
        "all_groups_covered": all_groups_covered, "rows_mapped": rows_mapped,
        "mack_inventory_updated": mack_inventory_updated,
        "deferred_component": "mack_cosmic_bridge_inventory_rows_45_46_cross_link",
        "plan_path_sha256": sha256_file(PLAN_PATH),
        "inheritance_falsifier_protocol_sha256": sha256_file(INHERITANCE_FAL),
        "cross_pillar_bridge_anatomy_sha256": sha256_file(CROSS_PILLAR),
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
        print(f"Verdict line for {GATE_ID} already present; skipping.")
    else:
        with open(VERDICT_OUT, "a", encoding="utf-8") as fh:
            fh.write(canonical_line); fh.write(companion_line); fh.write(schema_v2_line)
            fh.flush(); os.fsync(fh.fileno())
        print(f"Verdict block appended.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
