# Paasch -- Addendum: The Logarithmic Functional (Corrected)

**Author**: Paasch (Mass Quantization, Logarithmic Potentials)
**Date**: 2026-03-11
**Re**: Correction to Section 6C of S40 collab -- existing computations of ln(lambda^2)

---

## Section 1: What Was Already Computed

Two independent scripts computed the logarithmic functional on Jensen-deformed SU(3):

**Script 1: `tier0-computation/spectral_veff.py`** (Session 13-14 era, Feynman-Theorist agent)

Computes V_zeta(s) = (1/2) sum_n d_n ln(lambda_n^2(s) / mu^2), where d_n is the Peter-Weyl multiplicity and lambda_n are Dirac eigenvalues. The sum runs over all non-zero eigenvalues at max_pq_sum = 3 (10 sectors, (0,0) through (1,2)). The script sweeps s in [0, 2.0] at 21 points with mu = 1.0.

Result: V_zeta has its minimum at s = 0.000 (bi-invariant metric). The functional increases monotonically with s. The combined potential V_total = -kappa * R(s) + V_zeta(s) was computed for kappa in {0.1, 0.5, 1.0, 2.0, 5.0, 10.0}. The plot (`veff_spectral.png`) confirms that V_quantum dominates V_classical at all kappa values tested, and the minimum remains at or near s = 0.

**Script 2: `tier0-computation/tier1_spectral_free_energy.py`** (Session 17c, Hawking-Theorist agent)

Computes F(s, mu) = -sum_{(p,q)} dim(p,q) * sum_j ln(|lambda_j^{(p,q)}(s)|^2 / mu^2), which is -2 * V_zeta. This is the same logarithmic functional with opposite sign convention. The computation runs at max_pq_sum = 6 (significantly more modes), over 51 s-values in [0, 2.5], 31 mu-values in [0.1, 10], and 5 Lambda values for Boltzmann-regulated variants. Additionally computes dF/ds, specific heat, and phase transition classification.

Result: "No sharp phase transitions detected." The unregulated F is monotonically decreasing with s (equivalently, V_zeta monotonically increasing). Critical points found in the Boltzmann-regulated variant F_reg at some Lambda values are smoothed-out artifacts of the regulator, not intrinsic features of the logarithmic sum. Session 16 round-1c summarized: "The zeta-regularized potential (Lambda-independent) has its minimum at s = 0 (bi-invariant = max symmetry)."

Both computations agree: sum_n d_n ln(lambda_n^2) increases monotonically along the Jensen deformation. No minimum at nonzero s exists.

---

## Section 2: What My Original Claim Got Wrong

Section 6C of my S40 collab stated:

> "The 27 closures of equilibrium stabilization all used the LINEAR spectral action. None tested the LOGARITHMIC functional. This is not a mechanism that has been closed -- it is an entirely unexplored functional."

This is wrong. The logarithmic functional was computed in Session 13-14 (`spectral_veff.py`) and again in Session 17c (`tier1_spectral_free_energy.py`), both finding monotonic behavior with no minimum at nonzero s. The claim that it was "entirely unexplored" is a factual error that I should have caught by reading the tier0-computation directory before writing Section 6C.

The downstream claim -- that "every closure that assumed the linear spectral action needs re-examination against the log-determinant functional" -- is also wrong in its implication. The existing computations already show that the logarithmic functional is WORSE than the linear one for stabilization, not better. V_zeta is monotonically increasing for the same structural reason that makes the linear spectral action monotonically increasing: eigenvalues grow along the Jensen deformation, and ln(x) is a monotonically increasing function of x.

I retract the proposed gate "Compute zeta'_{D_K^2}(0) at 10 tau values" as already performed.

---

## Section 3: What Remains Genuinely Open

Despite the retraction above, there is a specific mathematical question that the existing computations did NOT settle and that CUTOFF-SA-37 does NOT cover.

**What CUTOFF-SA-37 proves**: For S_f(tau) = sum_n mult_n * f(lambda_n^2(tau)/Lambda^2), if f is monotonically increasing or monotonically decreasing, S_f is monotone in tau. Since ln(x) is monotonically increasing, V_zeta = sum d_n ln(lambda_n^2) falls directly under this theorem. The logarithmic functional is COVERED by CUTOFF-SA-37. It is monotone by the same structural mechanism: <lambda^2>(tau) increases from 2.495 to 3.471 across [0, 0.5], all 10 sectors contribute with the same sign, and any monotone function of the eigenvalues inherits the monotonicity.

**What remains open**: The concavity of ln(x) matters for a different question -- not whether the full sum is monotone, but whether PARTIAL sums or DIFFERENCES of logarithmic terms can produce non-monotone behavior. Specifically:

1. **Signed logarithmic sum**: The physically relevant one-loop effective potential for a theory with bosons and fermions is V = +(1/2) sum_bosons d_n ln(lambda_n^2) - (1/2) sum_fermions d_n ln(lambda_n^2). The relative minus sign between bosonic and fermionic contributions means CUTOFF-SA-37's monotonicity theorem does NOT apply to the signed sum. The constant-ratio trap (F/B = 0.55 full spectrum, from Weyl's law) makes the signed sum proportional to the unsigned sum at leading order, but the SUBLEADING corrections from the gap-edge modes (where F/B varies 10-37%, Session 22c) could produce non-monotone behavior in the signed logarithmic difference.

    This is distinct from the linear signed sum (sum d_n |lambda_n| with signs), which was already tested as the "signed sums b1-b2" escape route. The logarithmic version has not been computed. The concavity of ln amplifies the contribution of LOW eigenvalues relative to HIGH eigenvalues, which means the gap-edge modes (where F/B is most asymmetric) are weighted MORE heavily in the logarithmic sum than in the linear sum.

2. **Sub-sector logarithmic sums**: The B2 branch has 288 eigenvalues that DECREASE through the fold (CUTOFF-SA-37, Check 6: 288/1232 decrease). In the full sum, the increasing eigenvalues (944/1232) overwhelm the decreasing ones. But in a logarithmic sum restricted to the B2 sector alone, the weight of the decreasing eigenvalues is amplified by ln's concavity. Whether the B2-restricted logarithmic sum has a minimum near the fold is an uncomputed question.

3. **Resolution and range**: The `spectral_veff.py` computation used max_pq_sum = 3 (coarse truncation). The `tier1_spectral_free_energy.py` used max_pq_sum = 6 with 51 s-points spanning [0, 2.5]. Both have sufficient resolution to detect a minimum if one exists in the UNSIGNED sum. But neither computed the SIGNED (boson - fermion) logarithmic sum. That specific functional has not been evaluated.

---

## Section 4: The Specific Computation That Would Settle It

**Gate**: LOG-SIGNED-40

**What to compute**: V_log^{signed}(tau) = +(1/2) sum_{bosonic modes} d_n ln(lambda_n^2(tau)) - (1/2) sum_{fermionic modes} d_n ln(lambda_n^2(tau)) at 20 tau values in [0.10, 0.30].

**Criterion**: If V_log^{signed} has a local minimum at any tau in [0.10, 0.25], the gate PASSES. If monotone across the entire range, the gate FAILS and the logarithmic stabilization pathway is closed completely.

**Why this could differ from the unsigned case**: The F/B ratio at the gap edge varies from 0.56 to 0.83 across tau (Session 22c). The logarithmic weighting amplifies gap-edge modes relative to high modes. If the fermionic gap-edge modes decrease faster than the bosonic gap-edge modes through the fold, the signed logarithmic sum could reverse sign.

**Cost**: Zero new eigenvalue computation. The existing eigenvalue data from `s37_cutoff_sa.npz` (16 tau values, 155,984 weighted modes with boson/fermion labels from BdG classification) suffices. The computation is: re-sum the existing eigenvalues with ln(lambda^2) weighting and boson/fermion sign assignment. Estimated runtime: seconds.

**If PASS**: The logarithmic signed sum provides a stabilization mechanism that the linear signed sum does not. The concavity of ln concentrates weight on gap-edge modes where F/B asymmetry is largest. This would be a genuinely new result -- not a retread of CUTOFF-SA-37.

**If FAIL**: The logarithmic functional is closed as a stabilization pathway, for both unsigned (already closed by CUTOFF-SA-37 + existing computations) and signed variants. The closure is structural and permanent.

---

## Closing

My S40 collab Section 6C made a factual error: the logarithmic functional was computed twice in Sessions 13-17, both times finding monotonic behavior. The claim that it was "entirely unexplored" is retracted. The CUTOFF-SA-37 structural monotonicity theorem covers the unsigned logarithmic sum (ln is monotone increasing), so the unsigned case is closed by theorem, not merely by numerical evidence.

What survives is a narrower and more precise question: the SIGNED (boson - fermion) logarithmic sum, where CUTOFF-SA-37 does not apply because the relative sign breaks the monotonicity argument. The concavity of ln amplifies the gap-edge contribution where F/B asymmetry is maximal. This is a zero-cost computation on existing data. Gate LOG-SIGNED-40 is specified above.
