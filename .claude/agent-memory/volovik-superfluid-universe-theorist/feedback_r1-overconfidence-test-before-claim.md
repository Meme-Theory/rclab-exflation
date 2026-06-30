---
name: R1 overconfidence — verify partition-symmetry tests before opening-position commitments
description: When defending a structural-confidence position in cold-open R1, run the empirical partition-symmetry / projection tests Sage-QQ exact in dispatch BEFORE writing the substitution chain that asserts the symmetry holds; do not rely on "manifestly symmetric d(p,q)" as an implicit chain link
type: feedback
---

In S87 W-4 R1 cold-open I committed to K=2-with-OBSERVABLE-CONSTRUCTION reading on the cross-pillar-bridge-anatomy K-counter discipline + W11-5 cause attribution. My R1 chain claimed "(p,q)↔(q,p) symmetry of d(p,q) implies chi_67/chi_88 partition-ratio symmetry, justifying rank-1 effective reduction at p=0".

R2 dispatch ran the empirical test in Sage-QQ exact rationals: r_paired = 13.434, r_unpaired = 7.550, asymmetry 43.8% — well above the 25% rank-1-INVALID FAIL band. The d(p,q) symmetry preserves the **partition** (verified swap_invariant=True) but does NOT preserve the **chi_67/chi_88 ratio within each part**. My R1 implication was a non-sequitur.

R2 also tested the M_3(C) projection corollary I implied in R1 ("post-projection R_substrate matches R_3HeB_lit at relative ≤ 5%"): post-projection observable is UNDEFINED (N_paired^post = 0, all (p+q≥2) sectors are killed by ι_*; only fundamental sectors (1,0), (0,1) survive in H, both unpaired). The "fix" I proposed was structurally false.

**Why:** Cold-open R1 is the moment with maximum incentive to cite "manifest" or "trivial" symmetry as a chain-link without testing it. The agent-memory rule "topology-class first" + "microscopic Hamiltonian first" requires more than a structural assertion — it requires the test to actually run in the substitution chain step that makes the load-bearing direction-claim. Running the test in R2 invalidated 2 of my R1 claims (rank-1 reduction justified; M_3(C) post-projection ratio matches lit).

**How to apply:** for any future R1-cold-open response in adversarial workshop format where I am defending a structural-confidence position, run the explicit empirical test (Sage-QQ exact via mcp__sage__ or fractions.Fraction) for the partition-symmetry / projection / cancellation claim DURING R1 dispatch, not deferred to R2 verification. Specifically, when the substitution chain reads "Step N (read direction): X is symmetric under involution σ; therefore Y is symmetric under σ", verify Y is symmetric under σ — do not infer Y from X by "manifest" composition. Volovik corpus calibration: 3He-B parent→child morphism is structural, but the morphism's INTERACTION with truncated finite-L observables is exactly the layer where structural intuition fails most often (cf. S86 W1b-T8 + W11-5 finite-L FAIL pattern).

**Calibration corpus instance #1**: S87 W-4 R1→R2 retraction (this dispatch). Cold-open R1 K=2 + OBSERVABLE-CONSTRUCTION; R2 partial-retraction to K=1 + acknowledged kernel-rank-INVALID + bridge-map-mis-specification readings as structurally defensible alternatives. My R1 was overconfident on two specific predictions (rank-1 reduction symmetry-justified; M_3(C) post-projection in PASS band) — both empirically falsified within R2 dispatch. The calibration is not "do not defend K=2 cold-open"; it is "run the empirical sub-tests of the substitution chain WITHIN R1 dispatch, do not defer them to R2".
