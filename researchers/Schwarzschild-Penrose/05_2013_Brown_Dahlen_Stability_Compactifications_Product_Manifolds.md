# Spectrum and Stability of Compactifications on Product Manifolds

**Author(s):** Adam R. Brown, Alex Dahlen
**Year:** 2013 (v1); 2014 (v2)
**Journal:** arXiv preprint (hep-th)
**arXiv:** 1310.6360
**Relevance:** MEDIUM
**Substitutes for:** Fabricated "Brown-Dahlen 2009 Dynamical Compactification from de Sitter Space" entry (the original arXiv ID 0904.3915 in the prior index is actually a biostatistics paper, not a Brown-Dahlen paper). This is the authentic Brown-Dahlen stability paper from their actual flux-compactification research program.

---

## Abstract

We study the spectrum and perturbative stability of Freund-Rubin compactifications on M_p x M_Nq, where M_Nq is itself a product of N q-dimensional Einstein manifolds. The higher-dimensional action has a cosmological term Lambda and a q-form flux, which individually wraps each element of the product; the extended dimensions M_p can be anti-de Sitter, Minkowski, or de Sitter. We find the masses of every excitation around this background, as well as the conditions under which these solutions are stable. This generalizes previous work on Freund-Rubin vacua, which focused on the N = 1 case, in which a q-form flux wraps a single q-dimensional Einstein manifold. The N = 1 case can have a classical instability when the q-dimensional internal manifold is a product — one of the members of the product wants to shrink while the rest of the manifold expands. Here, we will see that individually wrapping each element of the product with a lower-form flux cures this cycle-collapse instability. The N = 1 case can also have an instability when Lambda > 0 and q >= 4 to shape-mode perturbations; we find the same instability in compactifications with general N, and show that it even extends to cases where Lambda <= 0. On the other hand, when q = 2 or 3, the shape modes are always stable and there is a broad class of AdS and de Sitter vacua that are perturbatively stable to all fluctuations.

---

## Key Arguments and Derivations

*This is the authentic Brown-Dahlen flux-compactification paper, replacing a fabricated index entry.*

**Freund-Rubin setup.** The authors study D = p + Nq-dimensional gravity with a higher-dimensional cosmological constant Lambda and a q-form flux F_q, governed by the action S = integral d^p x d^q y_1 ... d^q y_N sqrt(-g) [ R - (1/(2 q!)) F_q^2 - 2 Lambda ]. The ansatz is a Freund-Rubin compactification M_p x M_{q,1} x ... x M_{q,N}, where M_p is maximally symmetric (AdS, Minkowski, or dS) and each M_{q,i} is a q-dimensional Einstein manifold. Critically, instead of letting a single q-form flux wrap the entire internal product (as in the classical N=1 case), the flux is written as F_q = sum_i c_i vol_{M_{q,i}}, so each sub-manifold is individually wrapped by its own flux density c_i. This ansatz automatically solves Maxwell's equation in the absence of warping.

**Review of the N = 1 case.** For comparison, the authors catalog the three instabilities known from [5, 6] in standard Freund-Rubin compactifications where a single q-form flux wraps a single q-dimensional Einstein manifold: (i) a total-volume instability (only for Lambda > 0, when flux density is too small); (ii) a lumpiness instability (only for Lambda > 0 and q-spheres with q >= 4, driven by coupling between metric and flux fluctuations for angular momentum ell >= 2); and (iii) a cycle-collapse instability, present for any sign of Lambda when the internal manifold is itself a product and wrapped by a highest-form flux. The highest-form flux depends only on the total-volume combination (e.g., (R_1^2 R_2^2)^2 for S^2 x S^2 with a 4-form), so sub-curvatures are not stabilized: one sphere expands while the other shrinks, and V_eff -> -infinity. The endpoint is conjectured to be a bubble-of-nothing pinch-off, akin to closed-string tachyon condensation.

**Cure for cycle-collapse via lower-form flux.** The effective potential for individually-wrapped cycles (e.g., n_1 units of 2-form flux around the first S^2 and n_2 around the second) contains the combination n_1^2 / R_1^4 + n_2^2 / R_2^4 rather than n^2 / (R_1^2 R_2^2)^2. Because this term now depends on R_1 and R_2 separately, the flux is sensitive to sub-curvature perturbations and can restore the manifold to equilibrium. This is the central physical argument motivating the generalization to N > 1.

**Spectrum and stability for general N.** The authors then solve the coupled first-order equations of motion for all fluctuations (metric h_MN and flux potential B_{q-1}) around the background. The technical machinery proceeds in two stages: (1) a simultaneous Hodge decomposition and Lichnerowicz-Laplacian eigenmode decomposition of every tensor field, carried out sub-manifold by sub-manifold because the background is not uniform across the whole internal manifold (different c_i give different sub-curvatures R_i); (2) field-redefinitions that diagonalize the coupled system into decoupled ordinary differential equations from which masses can be read off. New subtleties arise from the fact that a component longitudinal on one sub-manifold can combine with components on the other sub-manifolds to produce a mode transverse on the whole internal manifold; 2N-1 of the 2N such vector pieces are globally transverse while 1 is longitudinal.

**Main stability verdict for N >= 2.** Individually wrapping each sub-manifold with its own lower-form flux cures the cycle-collapse instability. The total-volume instability persists (for Lambda > 0 with too-small flux density), as does a generalized lumpiness instability: for q = 2 shape modes always have positive mass, for q = 3 all shape-mode mass-squareds are stable (though possibly negative and above the BF bound), while for q >= 4 lumpiness instabilities can appear for any sign of Lambda — including Lambda <= 0, which is novel relative to the N = 1 case. A residual cycle-collapse instability survives when a sub-manifold M_{q,i} is itself a product (e.g., S^2 x S^2 x S^2 x S^2 wrapped by an 8-form or two 4-forms is unstable; only the fully factored N=4 case with four 2-forms is stable). Extra mode classes that exist only for N > 1 — inter-sub-manifold angles, off-diagonal form fluctuations — all have positive mass. The standard Kaluza-Klein tower structure is recovered: a massless graviton, massless vectors per Killing vector, and massless higher-form fields per harmonic form of the internal manifold, each with a massive KK tower above it.

## Key Results

1. **Cycle-collapse cured by lower-form flux.** Replacing a single q-form flux on a product M_{q,1} x ... x M_{q,N} with N individual q/N-form fluxes (where each sub-manifold is now q-dimensional) eliminates the classical cycle-collapse instability present in the N = 1 case, because the flux term in V_eff then depends on each sub-volume separately rather than only on the total volume.

2. **Three instability classes only.** Beyond cycle-collapse (cured), only the total-volume instability and the lumpiness (shape-mode) instability survive for general N; no new instability classes arise.

3. **Stability for q = 2 and q = 3.** Shape modes for internal products of 2-spheres or 3-spheres individually wrapped by 2-forms or 3-forms are always stable (for q = 3, negative mass squareds may appear but they lie above the BF bound). A broad class of AdS and dS vacua of this form are perturbatively stable to all fluctuations.

4. **Extended shape-mode instability for q >= 4.** For N >= 2 and q >= 4, shape-mode instabilities can appear for any sign of Lambda, including Lambda <= 0. This is qualitatively different from the N = 1 case, in which all Lambda <= 0 solutions were shape-stable.

5. **Residual cycle-collapse for partial factorings.** If any sub-manifold M_{q,i} is itself a product, a residual cycle-collapse instability persists. Full stability requires factoring the internal manifold all the way down so that every irreducible factor is individually wrapped.

6. **Refutation of prior literature.** Earlier claims in [25-27] that Minkowski compactifications M_4 x S^2 x S^2 and M_4 x S^2 x S^2 x S^2 are unstable to ell = 1 perturbations are shown to be incorrect: correct handling of residual gauge invariance proves all modes of these compactifications are stable.

7. **Kuenneth formula recovered.** The product structure of harmonic eigenmodes on the product manifold directly reproduces the Kuenneth formula for Betti numbers b_k(Z) = sum_{k_1 + ... + k_N = k} b_{k_1}(Z_1) ... b_{k_N}(Z_N).

8. **Minkowski condition on flux densities.** The M_p = Minkowski solution (L^{-2} = 0) requires sum_i c_i^2 = (4 / (q-1)) Lambda; vanishing all flux gives the Nariai solution, while sending one c_i -> infinity (R_i -> 0) corresponds to the "nothing state."

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Action | S = integral d^p x d^q y_1 ... d^q y_N sqrt(-g) [ R - (1/(2 q!)) F_q^2 - 2 Lambda ] | Eq. (5) |
| Einstein eq. | R_MN = (1/2)(1/(q-1)!) F_{M P_2...P_q} F_N^{P_2...P_q} - (1/2)((q-1)/(D-2))(1/q!) F_q^2 g_MN + (2/(D-2)) Lambda g_MN | Eq. (6) |
| Maxwell eq. | nabla^M F_{M P_2 ... P_q} = 0 | Eq. (7) |
| Flux ansatz | F_q = sum_{i=1}^N c_i vol_{M_{q,i}} | Eq. (8) |
| Einstein background (p) | (p-1)/L^2 = -(1/2)((q-1)/(D-2)) sum_i c_i^2 + (2/(D-2)) Lambda | Eq. (10) |
| Einstein background (q_i) | (q-1)/R_i^2 = (1/2) c_i^2 + (p-1)/L^2 | Eq. (11) |
| Minkowski condition | sum_{i=1}^N c_i^2 = 4 Lambda / (q-1) | Eq. (12) |
| V_eff, highest-form (unstable) | V_eff,4-form ~ (1/(R_1^2 R_2^2)^{2/(p-2)}) [ n^2 / (R_1^2 R_2^2)^2 - 1/R_1^2 - 1/R_2^2 + Lambda ] | Eq. (3) |
| V_eff, individually-wrapped (stable) | V_eff,2-form ~ (1/(R_1^2 R_2^2)^{2/(p-2)}) [ n_1^2 / R_1^4 + n_2^2 / R_2^4 - 1/R_1^2 - 1/R_2^2 + Lambda ] | Eq. (4) |
| Lichnerowicz operator | Delta_L T_{a_1...a_m} = Box T_{a_1...a_m} - sum_i R^c_{a_i} T_{...c...} + sum_{i != j} R^{cd}_{a_i a_j} T_{...c...d...} | Eq. (20) |
| Product eigenvalues | Y^I(y) = Y^{I_1}_1(y_1) ... Y^{I_N}_N(y_N), lambda^I = sum_{k=1}^N lambda^{I_k}_k | Eq. (24) |
| Kuenneth formula | b_k(Z) = sum_{k_1 + ... + k_N = k} b_{k_1}(Z_1) ... b_{k_N}(Z_N) | Eq. (55) |

## Relevance to Phonon-Exflation

This paper is the closest classical analog to the framework's Jensen-deformed SU(3) internal manifold: it is the general theory of when flux-supported product compactifications are stable, including the precise cycle-collapse failure mode and its cure. The phonon-exflation framework requires the internal SU(3) fiber to remain a stable single geometry under tau-evolution through the dump point tau ~ 0.19 — any instability that fragmented SU(3) into disjoint sub-pieces would destroy the spectral triple and with it the entire construction. Brown-Dahlen establish that the fragmentation mode exists generically when highest-form flux wraps a product, and is cured by individually wrapping each sub-factor with a lower-form flux; this is exactly the topological datum needed to check whether the framework's U(1)_7 gauge field from KK reduction plays the stabilizing role of the per-cycle flux, or whether the fiber is vulnerable to the residual cycle-collapse instability that survives when sub-manifolds are themselves products. The q = 2 and q = 3 stability windows are particularly relevant given SU(3)'s 3-cycle structure.
