# S115 W1 — Stage-2-verify gate + forced-external-corridor-residue COMPUTE gate (paired plan-authoring)

Cross-domain recipe for PLAN-AUTHORING a wave that pairs (W1-1) a Stage-2 blind cross-axis VERIFY of a
STAGE-1-CANDIDATE §VII obstruction theorem with (W1-2) a COMPUTE gate testing the SAME theorem's named
EXTERNAL corridor's phenomenological RESIDUE. The two are INDEPENDENT (one closes the internal-class
genus; the other tests the external corridor's observable) — do NOT sequence W1-2 after W1-1.

## W1-1 — Stage-2 verify gate shape (joint-theorem-promotion.md §Stage-2)
- `gate_type: compute` BUT the PASS predicate is artifact-existence-of-TWO-PASS-AND-verdicts (set-membership,
  NOT a scalar inequality). PRDR numeric fields (2)(3)(4) = N/A per the r3-template non-compute clause
  (lines 79-87); the validator ACCEPTS N/A there and does NOT coerce a threshold. cutoff_axis=N/A.
- The "operator" is the dual-reviewer PASS-AND; `strict_PASS_boundary` = "BOTH reviewers PASS each clause".
- Pin IN THE PLAN-BLOCK (machinery_pin_map): registered-entry path + EXACT body anchor (prefix-match the
  on-disk `### §VII.X — …` header; verify with grep) + master-index row# + the Stage-1 landing audit_sha256
  + workshop_transcript_WITHHELD (the transcript SHA, recorded ONLY to pin what must be excluded — reviewers
  do NOT receive it) + reviewer_axis_A/B (axis-distinct NON-AUTHOR names) + EXCLUDED_authors + dispatch
  PARALLEL + joint_clause_passand + reviewer_machinery_self_authorship (SATISFIED iff the clauses are
  shared NCG-axiomatic identities, not a reviewer-private decision procedure) + substrate_input_orthogonality
  (route the ONE compute artifact, e.g. the D1 npz, to EXACTLY ONE reviewer ⇒ predicate SATISFIED ⇒ no
  overlap-caveat) + promotion_on_PASS (name the EXACT tag transition + scope qualifier RETAINED/changed).
- substitution_chain is on the LOGICAL-AND direction claim: promotion is MONOTONE in the conjunction
  (a 5-of-6 partial STRICTLY blocks STAGE-3; INFO on any clause ⇒ stays STAGE-1). VERIFY-THEOREM ⇒ NO 3-tuple.
- output_artifacts: add TWO `review_md` entries (the per-reviewer blind synthesis files) alongside the
  closeout script + verdict_line; data/plot optional:true (adjudication closeout has no matrix compute).

## The reviewer-exclusion audit is STILL parser-unreliable (confirms [[stage2_verify_reviewer_exclusion_audit_gap]])
- `_joint_theorem_independent_verify_audit.py --check-reviewers VII.CK --reviewers a,b` returned
  `EXCLUSION-PASS` but with `stage0_authors: []` EMPTY — it did NOT parse the registered entry's
  "Stage-2 verifiers MUST EXCLUDE the YUKSHAPE Stage-0 authors connes / paasch" idiom. The PASS is correct
  on the MERITS (lizzi+volovik are genuinely non-authors) but reached via an empty author-set, not by
  actually enforcing the exclusion. ⇒ ENCODE the guard IN the plan-block (EXCLUDED_authors + per-reviewer
  non-author rationale), never rely on the audit's verdict. Run it for the record; read it critically.
- §VII.CK EXCLUDED set: {connes-ncg-theorist (Reading-A pole), paasch-mass-quantization-analyst (Reading-B
  pole)} = the ws-s113-7-yukshape Stage-0 authors. Axis-A=lizzi (NCG/spectral, audits D1 supertrace + D2
  even-moment), Axis-B=volovik (substrate/superfluid, audits D3 leg-membership/commutant). Axis-distinct.

## W1-2 — forced-external-corridor RESIDUE compute gate
- The §VII.CK D4-disposition annotation ALREADY records the forced-texture prediction the gate computes:
  `|U_ij|²=1/3` (coefficient-INDEPENDENT circulant — diagonalized by DFT₃ regardless of c_a), `arg(w)=2π/3`,
  `J=1/(6√3)=0.09622504` (Sage-exact), quark-CKM FALSIFIED ~3124× (=J_forced/J_CKM, J_CKM=3.08e-5), lepton-
  PMNS RESONANT-CONDITIONAL ~2.9× from observed (=J_forced/J_obs, J_obs≈0.0329). The bare deviation
  dev=|J_f−J_obs|/J_obs=1.9248 — so the SYMMETRIC limit FAILS any PMNS-3σ band; the gate's load-bearing
  physics is the CHARGED-LEPTON correction U_L (coset-diagonal, ℂ⊕ℍ asymmetry) and the PHYSICAL
  U_mix=U_L†U_R (W-2 Q3: one-circulant-one-coset-diagonal ⇒ tri-maximal; two-circulant ⇒ identity).
- `[SIGN]` trigger ⇒ 3-tuple companion REQUIRED (the "forced-and-surviving ⇒ prediction" is a DIRECTION
  claim). substitution_chain plugs J_bare=1/(6√3) and J_obs into dev; the SIGN of (J_corrected−J_obs) and
  in-band-vs-out IS the surviving-vs-washed-out verdict. dual_prior: ~0.15 SURVIVING / ~0.85 WASHED-OUT
  (the registry's "~2.9× RESONANT-CONDITIONAL" IS the bare-limit Track-B prior). Negative control:
  M₃(ℂ)-shared quark chiralities ⇒ TWO circulants ⇒ assert |U_mix−I|<1e-12.
- `J_PMNS` is NOT a canonical constant (get_constant→not-found) — pin J_PMNS_obs + the 3σ Jarlskog interval
  as EXTERNAL `# (local)` observational anchors (NuFIT/PDG) per substrate-first §(i) methodological-anchor
  admissibility. DISTINGUISH from `delta_CP_PMNS_substrate=0` (S100b, the SEPARATE substrate seesaw δ_CP,
  IS canonical) and `J_CP_PDG=3.08e-5` (CKM-quark, the negative-control reference). 3×3 ⇒ numpy.linalg
  cpu-cap-OMP8 (below the 100×100 GPU threshold). publication_precision=6 (J/dev/ratio cited downstream).

## Wave→Wave decision point
- W1-1 lands FIRST (D1-D3 → STAGE-3-PERMANENT, D4-OPEN RETAINED); the SEPARATE W2 gate re-scopes D4 →
  UNCONDITIONAL on TOP of it. W1-1 FAIL ⇒ W2 BLOCKED (cannot re-scope D4 over an unverified D1-D3 class);
  W1-1 INFO on D3 specifically ⇒ W2 blocked (D4 discharge rests on D3 leg-membership). W1-2 gates NEITHER
  (externality-as-a-coupling is structural; the PMNS residue is its phenomenological shadow).

Links: [[s114_w33_shapewall_vii_landing_perblock_identity]] (the §VII.CK Stage-1 landing I authored — the
theorem this wave verifies); [[stage2_verify_reviewer_exclusion_audit_gap]] (the parser-unreliability,
now CONFIRMED via empty stage0_authors); [[joint_theorem_clause_formalization_landing]] (the JOINT-clause
PASS-AND'd-at-Stage-2 pattern); [[stage2_pass_and_aggregation_closeout]] (the PASS-AND closeout shape).
