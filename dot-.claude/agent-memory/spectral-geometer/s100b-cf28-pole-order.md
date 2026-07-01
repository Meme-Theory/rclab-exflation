---
name: s100b-cf28-pole-order
description: S100b W3-1 CF28 pole-order pre-flight — cubic-point exact-theta theorem, single-pole dimension spectrum, mpmath complex-Hurwitz pitfall, W3-2 LC-point finding
metadata:
  type: project
---

# S100b CF28 simple-pole pre-flight (W3-1) — durable results

**Why:** these are permanent spectral identities + a reusable numerical-methods lesson; future s=7 Pillar-VII work and any τ=0 reasoning cites them.
**How to apply:** cite before re-deriving anything about SU(3) cubic-point heat traces, pole orders, or τ=0 operator identity.

## Cubic-point exact-theta theorem (route-1 EXACT, Fraction arithmetic)

For ζ_A(s) = 4 Σ_{u,v≥1} u²v²(u+v)² (u²+uv+v²)^{−s} (full-PW cubic Dirac zeta, λ̂² = 3C₂+3 = |λ+ρ|² form, 16·dim² = 4u²v²(u+v)²):

- **Single pole in all of ℂ**: s_A = 4 only. Res = 3690677704889354953477419992365613/20602119781744137104576709959443800 = 0.1791406779. a₀^{Mellin} = Γ(4)·Res = 1.074844067694351 = Weyl angular integral 12∫₀^{π/2}cos²sin²(cos+sin)²/(1+cos·sin)⁴ to ALL float64 digits.
- Res(s_A=2) = 2·[c_{0,1}+2c_{1,3}] = 2·[−1/30+2/60] = 0 EXACT; Res(s_A=1) = 0 EXACT (3-term); s_A=3 has ZERO candidate terms (degree 2j+3 in the structural gap of S_j).
- **S_j(N) = Σ_u u^{j+2}(N−u)^{j+2} has ODD powers of N only** (verified j ≤ 50; S_0 = (N⁵−N)/30, S_1 = N⁷/140+N³/60−N/42). Degree set = {leading 2j+5} ∪ low cluster; gap kills the a_2-grade diagonal.
- **Exotic locus s_A ∈ {0,−1,−2,−3}** (Γ-collisions, n ∈ {8,10,12,14}): all candidate terms Pochhammer-annihilated ((s_A)_j = 0) ⇒ ζ_A REGULAR, trivial zeros ζ_A(−k) = 0 ⇒ Γζ_A simple ⇒ NO Fucci-Stanfill log on the closed substrate.
- Heat trace: **K(t)·t⁴ = a₀ to 2.6e-16 for t ≤ 1e-2**; theta corrections (Poisson dual lattice) only at t ≳ 0.3 (−0.6% at t=1). Unshifted grading: K_unshift = e^{3t}K ⇒ a_n^{unshift} = a₀·3^k/k! (a_2 = 3a₀ = 3.2245). Pole ORDERS invariant under e^{3t} and κ-rescale.
- Verdict: S100b-CF28-SIMPLE-POLE-PREFLIGHT canonical PASS (audit c0a0b9f3…143213, supersedes 031b6267…ce6156 INFO per pre-registered W3-2-FAIL SOFT note). Max key-set |c₋₂| ratio 3.71e-46 vs 1e-8. s=7 ELIGIBLE with the LC-identity rider.
- Canonical S_d = {0,2,4,6,8} (E58) is the generic pole-LOCATION statement; the cubic point is its degenerate-residue corner (refinement, not contradiction).

## W3-2 STRUCTURED-LC finding (cross-gate, load-bearing for ALL τ=0 reasoning)

S100b-TAU0-LAITEH-REDUCTION FAIL, SUBCASE=STRUCTURED_LC: **the framework's τ=0 operator sits at the Levi-Civita torsion point t=1/2, NOT the Kostant cubic point t=1/3** (lcdev = 8.95e-15, machine epsilon; blocks do NOT collapse to single |λ| — spread 0.439). λ² = n/36 integrality STILL holds at LC (σ=1, resid 1.85e-12). My CF28 certificate covers the PRE-REGISTERED cubic object; LC-extension certification is carry-forward item 2 (route-1 machinery applies per shifted-Casimir sub-lattice).

## Numerical-methods lessons (reusable)

1. **mpmath two-arg zeta(w, a) at COMPLEX w with large Re(w) returns ABSOLUTE noise ~1e-57·O(1) at dps=50** (true value ~a^{−Re w} ~ 1e-154 at w≈85, a=64); real axis is accurate. Fix: in-house Euler–Maclaurin ζ_H(w,a) = a^{−w}[1/2 + a/(w−1) + Σ_r B_{2r}/(2r)!·(w)_{2r−1}·a^{1−2r}] — multiplicative prefactor ⇒ relative error only (~1e-40 at R=45, a=64, |w| ≤ 92).
2. **Faulhaber monomial basis is numerically catastrophic near N=2** (S_j(2)=1 via ~1e58 Bernoulli monomials at j=40). Fix: Hurwitz split at N₀=64 (finite exact-integer part + leading-dominated ζ_H tails); residues split-independent.
3. **Shell-exponent fits on L ∈ [6,12] are pre-asymptotic**: exact τ=0 lattice gives window slopes −2.425/−4.041/−5.658 vs asymptotic −3/−5/−7 (devs +0.575/+0.959/+1.342); τ_fold matches the exact-window devs to ≤ 0.06. Never gate an asymptotic-exponent band on this window; gate |exp_τ − exp_exact-τ0-window| instead.
4. (4,4) sector reconstruction at τ_fold: get_irrep(4,4) builds in 0.1 s (hom err 2.8e-15); 2000×2000 GPU eigvalsh; cache lineage cross-checks (2,2)/(4,3) reproduce s84 cache to 2e-14/4e-14; |λ|_{(4,4)} ∈ [2.4120, 3.7640].

## LC-branch pole-order certificate (S101 W1-2, S101-W3-LC-POLE-CERT PASS, audit `ebfd1d439462e4ce…`)

The LC (Levi-Civita t=1/2) τ=0 operator is a DIFFERENT operator from the cubic point (t=1/3). Its certificate is SEPARATE; the cubic-REFERENCE certificate (W3-1, `c0a0b9f3010adfad…`) is PERMANENT and unaffected.

- **LC integer n-mesh (BINDING form):** for sector (p,q), spinor bundle S⊗V_(p,q) decomposes (Lai-Teh Lemma 2.6, `mu_list_lemma26`, 8 μ-sub-reps) and on each V_μ the D² eigenvalue is **n(p,q,μ) = 2·poly(V) + 2·poly(μ) + 9** (= 4·eig_LT; eig_LT = ½[poly(V)+poly(μ)]+9/4; poly(a,b)=a²+b²+ab+3a+3b=3C₂; λ²=n/36, **n ODD**), block multiplicity 2·dim(μ). Bit-faithful to the W1-1 npz `lc_pred_vals_concat` (0/28 sector mismatch). LC n(0,0)=27 vs cubic λ̂²(0,0)=3 — distinct operators.
- **PETER-WEYL FACTOR IS MANDATORY (key lesson):** the full-spectrum heat-trace multiplicity is m_n = Σ_{(p,q),μ} **dim(p,q)**·2dim(μ) — the dim(p,q) PW factor (each rep appears dim(p,q)× in L²(SU(3))). WITHOUT it the cumulative-weight abscissa is 1.366 (WRONG); WITH it abscissa = **4.000** = d/2 (d=8, correct). Omitting it gives a₀<0 (unphysical). Always include the PW factor when zeta-summing the FULL D² spectrum from per-sector blocks.
- **c₋₂ = 0 STRUCTURAL (route-1, proven, COMPUTED not presumed):** each μ-shift family is a weighted 2D lattice zeta of binary quadratic Q_δ=4(p²+pq+q²)+linear+const; **Hessian [[8,4],[4,8]], det=48≠0 for all 8 families** ⇒ non-degenerate ⇒ θ_δ log-free (Gaussian/Poisson) ⇒ simple poles only. A₂ principal part has exact **Hecke factorization Epstein_{A₂}(s)=6ζ(s)L(s,χ₋₃)** (single simple pole s=1). Finite sum of simple poles ⇒ c₋₂(ζ_LC)=0 at every order.
- **a₂^{Mellin}(LC, τ=0) = −0.0125958 ≠ 0** (gravity moment at genesis populated; the workshop two-way-split confirmed; column-2/Kostant pure-volume a₂(0)=0 foreclosed by W1-1 PASS). a₀^{Mellin}(LC) = +0.00419861 > 0 (Weyl positive). Heat coeffs (θ ~ Σ a_j t^{j−4}): a₀=4.19861e-3, a₁=−2.51917e-2 ⇒ a₂^{Mellin}=a₁/Γ(3)=a₁/2; Res_{s_A=k}ζ = a_{4−k}/Γ(k). The n=2 row REVERTS from removable (cubic θ degeneracy) to a genuine simple pole under LC.
- **NUMERICAL METHOD (fast + exact, the working recipe):** (i) vectorize the LC mesh via `np.bincount` on integer n (PMAX=800 in 0.4s; pure-Python dict loop is multi-minute — DON'T). (ii) extract heat coeffs by an **exact-power (no-log basis) θ-peel** on a RESOLVED window (big box PMAX≥700 so exp(−t·n_max)≈0 at t≥0.03): float64 θ (all-positive, no cancellation, ~1e-15 accurate) + mpmath linear solve; held-out rel err 4.95e-12 IS the numeric log-freedom witness. (iii) contour-Laurent cross-check on the closed-form meromorphic `ζ_mero(s) = E(s)/Γ(s) + (1/Γ(s))Σ_j a_j/(s+powers_j)` with E(s)=Σ m_n n^{−s}Γ(s,n) TRUNCATED at n≤400 (Γ(s,n)/Γ(s)·n^{−s} ~ e^{−n}/(nΓ(s)) decays like e^{−n}, so small-n dominates — the full 74k-point mesh is intractable for contour). c₋₂ ratio 1.77e-34, xroute (c₋₁ vs a₁/Γ(3)) = 0.0 EXACT (entire part analytic ⇒ contour residue = pole-part residue). DON'T fit θ in a narrow window or with a with-log Vandermonde column — ill-conditioned (a₀<0, spurious b_log~1e-8 noise floor).
- **PITFALL:** the s=5 "value self-check" (mero vs convergent direct sum) FAILS by construction (rel~4) — ζ_mero captures pole structure only, drops the entire t∈[0,1] regular remainder; it is NOT the full ζ value. Validate via (a) entire-part E(s) analyticity (contour c₋₁≈0 at the pole, got 2e-64) and (b) xroute residue match, NOT via value reconstruction above abscissa.
