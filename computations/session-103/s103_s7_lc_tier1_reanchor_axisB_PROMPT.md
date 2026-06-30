# Stage-2 Axis-B BLIND cross-reviewer prompt — S103-S7-LC-TIER1-REANCHOR

**Dispatch target**: `volovik-superfluid-universe-theorist` (Axis-B = substrate / superfluid-universe).
**Reviewer-exclusion**: PASS — volovik is NOT gen-physicist (the §VII.BT Stage-0/Stage-1 author); volovik did not author the §VII.BT landing and his memory does not cite its transcript as canonical (`joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`, all three conditions: axis-distinctness from Axis-A spectral/NCG PASS; original-authoring-exclusion PASS; audit-coverage-adequacy PASS).
**Run mode**: `run_in_background: false` (await), IN PARALLEL with the Axis-A (lizzi) dispatch.

---

You are `volovik-superfluid-universe-theorist`. You have ONE task: a BLIND Stage-2 cross-axis independent verify (Axis-B, substrate / superfluid-universe) of the registered §VII.BT STAGE-1-CANDIDATE theorem.

**BLIND CONSTRAINT (mandatory, audited).** You read ONLY these two artifacts and NOTHING else:
1. The registered §VII.BT entry text in `sessions/permanent-results-registry.md`. Locate it by `grep -n '### §VII.BT'` (the entry begins there; read the entry block through the next `### §VII.` heading). DO NOT read any other registry entry.
2. The LC certificate `computations/session-101/s101_w3_lc_pole_cert.npz` (load with numpy, `allow_pickle=True`; inspect the fields).

You MUST NOT read: any session-101 / session-102 / session-103 workshop transcript, any plan file (`session-*-plan-*.md`), any working paper, any other agent's verdicts, or any S101/S102 session document. You verify the registered theorem FROM FIRST PRINCIPLES using only the two artifacts above. Do not seek the "expected" outcome — there is none provided.

**What you audit (Axis-B clauses).** Return a per-clause PASS / FAIL / INFO verdict on each:

- **Clause J1 (JOINT — Mellin simple-pole-tower identity, substrate-structure reading).** Verify the §VII.BT Level-1 claim from the substrate side: the genesis simple-pole structure IS the substrate's structural identity at τ=0. The n=2 (a_2) row REVERTS from removable (cubic-θ degeneracy at the generic operator) to a GENUINE SIMPLE pole under the LC (Levi-Civita, t=1/2) genesis operator; a_2^{Mellin}(LC) ≠ 0 is the gravity moment at genesis. The certificate's genesis-structure witnesses — `mu_shift_hessian_dets` (all 48, non-degenerate ⇒ θ_δ log-free), the per-pole residue grades, `n2_row_status`, and the Hessian-nondegeneracy block — are the evidence. Is the genesis simple-pole structure correctly established as a substrate-IS structural identity at the τ=0 LC slice (single-τ-slice Level-1)?

- **Clause J2 (JOINT — Tier-1 re-anchor as substrate-natural-binding pin).** The §VII.BT entry re-anchors Level-3 to the DIMENSIONLESS truncation match-error `peel_heldout` (field `peel_heldout_nolog`). Verify from the substrate side: is this re-anchor a SUBSTRATE-NATURAL-BINDING pin (the substrate-IS truncation invariant — how well the L_max=10 truncation of the substrate's own spectral triple captures the continuum genesis residue), NOT a canonical-import-binding or a methodology-floor F-image sideways re-pin? Is the HELD dimensionful magnitude (the M_KK² gravity moment) correctly held against substrate-natural extraction rather than sideways-re-pinned (the "Non-Promotion-by-Held-Number" differentia = dimensionful-slot-collision)?

- **Clause B1 (Axis-B single-axis — substrate-IS-vs-laboratory-IN bridge anatomy).** Verify the 5-element IS-not-IN bridge anatomy: (1) substrate-IS observable = the s=7 Mellin-cone residue tower at the τ=0 LC genesis slice; (2) laboratory-IN observable = the continuum Mellin-cone image; (3) bridge map = HKR / Connes-Karoubi (explicit, not "analogous"); (4) algebraic envelope = L^{−α}, α=6.584, Level-2-binding; (5) empirical anchor. Is the DIRECTION OF EXPLANATION correct (substrate IS the residue tower → bridge → laboratory-IN continuum image), with NO container-thinking inversion? Is the genesis-structure non-degeneracy witness (Hessian dets, an Axis-B-loaded observable) substantively confirming the τ=0 structural identity?

**Output.** Write a JSON verdict file to:
`computations/session-103/s103_s7_lc_tier1_reanchor_axisB_verdicts.json`

with this structure (the orchestrating script ingests `overall_verdict` and the per-clause `joint`+`verdict` fields):

```json
{
  "gate_id": "S103-S7-LC-TIER1-REANCHOR",
  "axis": "B",
  "axis_label": "substrate / superfluid-universe",
  "reviewer_agent": "volovik-superfluid-universe-theorist",
  "blind_attestation": {
    "read_only": [
      "sessions/permanent-results-registry.md §VII.BT entry block (located by grep '### §VII.BT')",
      "computations/session-101/s101_w3_lc_pole_cert.npz"
    ],
    "did_not_read": "no workshop transcripts, no plan files, no working papers, no S101/S102/S103 session documents, no other registry entries",
    "first_principles": true
  },
  "clauses": {
    "J1_genesis_simple_pole_structural_identity": {"joint": true,  "verdict": "PASS|FAIL|INFO", "reasoning": "..."},
    "J2_tier1_reanchor_substrate_natural_binding": {"joint": true,  "verdict": "PASS|FAIL|INFO", "reasoning": "..."},
    "B1_substrate_is_vs_lab_in_bridge_anatomy":    {"joint": false, "verdict": "PASS|FAIL|INFO", "reasoning": "..."}
  },
  "overall_verdict": "PASS|FAIL|INFO",
  "notes": "..."
}
```

`overall_verdict` = FAIL if any clause is FAIL; else INFO if any clause is INFO; else PASS. Use the venv Python (`phonon-exflation-sim/.venv312/Scripts/python.exe`) to load the npz. Working dir: `C:\sandbox\Ainulindale Exflation`.
