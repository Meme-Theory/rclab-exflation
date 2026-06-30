# Stage-2 Axis-A BLIND cross-reviewer prompt — S103-S7-LC-TIER1-REANCHOR

**Dispatch target**: `lizzi-spectral-functional-theorist` (Axis-A = spectral-functional / NCG-axiomatic).
**Reviewer-exclusion**: PASS — lizzi is NOT gen-physicist (the §VII.BT Stage-0/Stage-1 author); lizzi did not author the §VII.BT landing and her memory does not cite its transcript as canonical (`joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`).
**Run mode**: `run_in_background: false` (await), IN PARALLEL with the Axis-B (volovik) dispatch.

---

You are `lizzi-spectral-functional-theorist`. You have ONE task: a BLIND Stage-2 cross-axis independent verify (Axis-A, spectral-functional / NCG-axiomatic) of the registered §VII.BT STAGE-1-CANDIDATE theorem.

**BLIND CONSTRAINT (mandatory, audited).** You read ONLY these two artifacts and NOTHING else:
1. The registered §VII.BT entry text in `sessions/permanent-results-registry.md`. Locate it by `grep -n '### §VII.BT'` (the entry begins there; read the entry block through the next `### §VII.` heading). DO NOT read any other registry entry.
2. The LC certificate `computations/session-101/s101_w3_lc_pole_cert.npz` (load with numpy, `allow_pickle=True`; inspect the fields).

You MUST NOT read: any session-101 / session-102 / session-103 workshop transcript, any plan file (`session-*-plan-*.md`), any working paper, any other agent's verdicts, or any S101/S102 session document. You verify the registered theorem FROM FIRST PRINCIPLES using only the two artifacts above. Do not seek the "expected" outcome — there is none provided.

**What you audit (Axis-A clauses).** Return a per-clause PASS / FAIL / INFO verdict on each:

- **Clause J1 (JOINT — Mellin simple-pole-tower identity, Level-1 cohomology-class).** Verify the §VII.BT Level-1 structural claim: on the τ=0 LC genesis spectral triple, the s=7 Mellin-cone residue tower of ζ_{D_K}(s) is a tower of SIMPLE poles, and the load-bearing n=2 (a_2) row is a GENUINE SIMPLE pole with a_2^{Mellin}(LC) ≠ 0 (the gravity moment at genesis). The certificate's non-degeneracy witness (`mu_shift_hessian_dets` all = 48 ≠ 0 ⇒ each μ-shift sub-family is a non-degenerate binary quadratic ⇒ θ_δ log-free ⇒ only simple poles ⇒ c_{−2}(ζ_LC) = 0 structural) and the Hecke factorization (`hecke_s2_rel`; Epstein_{A2}(s) = 6 ζ(s) L(s,χ_{−3}), single simple pole at s=1) are the evidence. Is the simple-pole-tower identity correctly established at the cohomology-class layer (regulator-invariant, L-independent at the class level)?

- **Clause J2 (JOINT — Tier-1 dimensionless re-anchor validity).** The §VII.BT entry documents a Tier-1 re-anchor pathway: re-anchor the Level-3 from the DIMENSIONFUL residue magnitude |a_2^{Mellin}(LC)| (M_KK² units; Tier-2-dimensionful, registry-PASS-INELIGIBLE) to the DIMENSIONLESS truncation match-error `peel_heldout` (certificate field `peel_heldout_nolog`). Verify from first principles: is `peel_heldout` the CORRECT dimensionless truncation invariant of the a_2^{Mellin}(LC) residue? Specifically — (a) is it dimensionless (a relative deviation, M_KK² cancels in the ratio)? (b) does it correctly measure the L_max=10 truncation's deviation from the converged continuum residue (the quantity that should be compared against the dimensionless Level-2 = L^{−α} convergence-rate envelope)? (c) is re-anchoring to it the substrate-natural Tier-1 pathway (a log-derivative / ratio / cohomology-class anchor that annihilates the dimensionful W(L) factor), NOT a methodology-floor sideways re-pin? Note: the certificate holds TWO peel fields — `peel_heldout_nolog` and `peel_heldout_withlog`; judge whether the log-free field is the appropriate truncation invariant.

- **Clause A1 (Axis-A single-axis — spectral-functional consistency).** Are the certificate's Laurent data (`laurent_c_m1`, `laurent_c_0`, `laurent_s_A`, `laurent_grade_n`, `laurent_conv`) internally consistent with the registered poleconv-DUAL grading (load-bearing a_2 at s_A=3 ≡ s_B=6, grade n=2)? Is the abscissa `abscissa_pw ≈ 4.000` (= d/2, d=8) consistent with the full-L²(SU(3)) Peter-Weyl multiplicity claim?

**Output.** Write a JSON verdict file to:
`computations/session-103/s103_s7_lc_tier1_reanchor_axisA_verdicts.json`

with this structure (the orchestrating script ingests `overall_verdict` and the per-clause `joint`+`verdict` fields):

```json
{
  "gate_id": "S103-S7-LC-TIER1-REANCHOR",
  "axis": "A",
  "axis_label": "spectral-functional / NCG-axiomatic",
  "reviewer_agent": "lizzi-spectral-functional-theorist",
  "blind_attestation": {
    "read_only": [
      "sessions/permanent-results-registry.md §VII.BT entry block (located by grep '### §VII.BT')",
      "computations/session-101/s101_w3_lc_pole_cert.npz"
    ],
    "did_not_read": "no workshop transcripts, no plan files, no working papers, no S101/S102/S103 session documents, no other registry entries",
    "first_principles": true
  },
  "clauses": {
    "J1_mellin_simple_pole_tower_identity": {"joint": true,  "verdict": "PASS|FAIL|INFO", "reasoning": "..."},
    "J2_tier1_reanchor_validity":          {"joint": true,  "verdict": "PASS|FAIL|INFO", "reasoning": "..."},
    "A1_spectral_functional_consistency":  {"joint": false, "verdict": "PASS|FAIL|INFO", "reasoning": "..."}
  },
  "overall_verdict": "PASS|FAIL|INFO",
  "notes": "..."
}
```

`overall_verdict` = FAIL if any clause is FAIL; else INFO if any clause is INFO; else PASS. Use the venv Python (`phonon-exflation-sim/.venv312/Scripts/python.exe`) to load the npz. Working dir: `C:\sandbox\Ainulindale Exflation`.
