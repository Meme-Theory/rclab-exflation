# CC Path D: Volume Dilution -- A KK Theorist's Investigation

**Author**: Kaluza-Klein Theorist
**Date**: 2026-04-01
**Status**: INVESTIGATION -- detailed dimensional reduction analysis
**Sources**: Papers 02-06, 10, 14, 19 (KK corpus); framework-cc-oom.md; Volovik-VdD workshop (S63)

---

## 0. Executive Summary

Volume dilution claims that the 114-OOM CC gap is the ratio of Hubble to KK volume. Volovik (E1.4) argues the substrate's vacuum energy per KK cell is O(M_KK), distributed across ~10^{114} emergent cells, with the observed CC being the energy per emergent volume.

**Verdict**: Naive volume dilution FAILS for the CC density, for two independent reasons:

1. **The CC is intensive, not extensive.** The explicit KK dimensional reduction shows this unambiguously: the internal volume V_K enters BOTH the vacuum energy and Newton's constant (through M_Pl^2 = V_K * M_D^{D-2}), and these factors cancel in the dimensionless ratio rho_vac / M_Pl^4.

2. **The numerology is wrong.** (R_H/R_K)^3 = 10^{176}, not 10^{117}. The match at d = 2 -- (R_H/R_K)^2 ~ 10^{117} -- is not a coincidence but a tautological restatement of the Friedmann equation H_0^2 = rho_obs/M_Pl^2.

No modified version survives as a CC resolution. Spectral dilution (the mode sum decreasing with tau) reduces to Path C (transit-as-relaxation) and faces the a_0 floor obstruction (Theorem T14).

---

## I. The KK Perspective on Vacuum Energy: Explicit Dimensional Reduction

### I.1. The Higher-Dimensional Action

The framework's total spacetime is M^4 x K where K = SU(3) with dim K = 8, so D = 4 + 8 = 12. The higher-dimensional Einstein-Hilbert action is:

    S_12 = (1 / 2 kappa_12^2) integral d^{12}x sqrt(-g_12) R_12     (D-1)

where kappa_12^2 = 8 pi G_12 = M_12^{-10} (in natural units where hbar = c = 1), with M_12 the fundamental 12-dimensional Planck mass.

The spectral action provides the NCG formulation of this:

    S = Tr f(D_total^2 / Lambda^2)     (D-2)

Both (D-1) and (D-2) must yield the same 4D physics after reduction. I will track the volume factors through both routes to show they are consistent and that the CC is intensive.

### I.2. The Metric Ansatz

The product metric on M^4 x K:

    ds_12^2 = g_{mu nu}(x) dx^mu dx^nu + g_{ab}(y; tau) dy^a dy^b     (D-3)

with mu, nu = 0,...,3 (base) and a, b = 1,...,8 (fiber). The Jensen deformation parameter tau enters only through g_{ab}. The product structure means the O'Neill tensors A = T = 0 (confirmed A-TENSOR-61, S61).

No warping. No off-diagonal base-fiber components at tree level. This is the simplest possible ansatz -- a direct product.

### I.3. Reduction of the Ricci Scalar

For a product metric with A = T = 0, the D-dimensional Ricci scalar decomposes exactly:

    R_12 = R_4 + R_K(tau)     (D-4)

where R_4 is the 4D Ricci scalar (function of x^mu only) and R_K(tau) is the scalar curvature of the fiber (function of the internal coordinates y^a and the deformation parameter tau). This follows from the Gauss-Codazzi relations for a product decomposition. With zero O'Neill tensors, there are no cross terms.

The 12-dimensional volume element factorizes:

    sqrt(-g_12) = sqrt(-g_4) * sqrt(g_K)     (D-5)

### I.4. Reduction of the Einstein-Hilbert Action

Inserting (D-4) and (D-5) into (D-1):

    S_12 = (1 / 2 kappa_12^2) integral d^4x sqrt(-g_4) integral d^8y sqrt(g_K) [R_4 + R_K(tau)]     (D-6)

The integral over K is a number (K is compact). Define the internal volume:

    V_K = integral d^8y sqrt(g_K(tau))     (D-7)

For the Jensen deformation on SU(3), the volume-preserving constraint gives V_K = Vol(SU(3)) = 1349.74 (in units of R_K^8, the KK length scale to the 8th power; source: canonical_constants.py, corrected S44). The volume is tau-INDEPENDENT by the volume-preservation condition of the Jensen deformation.

The scalar curvature R_K depends on y^a in general, but for a homogeneous space (left-invariant metric on SU(3)), R_K is constant on K. Define:

    R_K(tau) = (1/V_K) integral d^8y sqrt(g_K) R_K(tau)     (D-8)

(This is just R_K itself for a homogeneous space -- the average equals the value at any point.)

Now (D-6) becomes:

    S_12 = (V_K / 2 kappa_12^2) integral d^4x sqrt(-g_4) [R_4 + R_K(tau)]     (D-9)

### I.5. Identification of 4D Newton's Constant and Cosmological Constant

**Step 1: Newton's constant.** Comparing (D-9) with the standard 4D Einstein-Hilbert action:

    S_4 = (1 / 16 pi G_4) integral d^4x sqrt(-g_4) [R_4 - 2 Lambda_4]     (D-10)

the gravitational sector (R_4 term) gives:

    1 / (16 pi G_4) = V_K / (2 kappa_12^2) = V_K * M_12^{10} / (16 pi)     (D-11)

Therefore:

    M_Pl_4^2 = (1 / 8 pi G_4) = V_K * M_12^{10} / (8 pi)     (D-12)

Or equivalently:

    M_Pl_4^2 = V_K * M_12^{10}     (D-13)

(absorbing the 8 pi into the definition of the reduced Planck mass). This is the standard KK volume relation, consistent with the ADD formula (Paper 19, Eq. M_P^2 = M_{4+n}^{2+n} * V_n) specialized to n = 8.

**Key point**: M_Pl_4^2 is PROPORTIONAL to V_K. The larger the internal volume, the larger the 4D Planck mass. This is the volume dependence that will cancel in dimensionless ratios.

**Step 2: Cosmological constant.** The R_K(tau) term in (D-9) acts as a 4D cosmological constant:

    S_CC = (V_K / 2 kappa_12^2) integral d^4x sqrt(-g_4) R_K(tau)     (D-14)

Comparing with the Lambda_4 term in (D-10):

    Lambda_4 = -(1/2) R_K(tau)     (D-15)

(with standard sign convention Lambda_4 > 0 for positive curvature K). The vacuum energy density is:

    rho_vac = Lambda_4 / (8 pi G_4) = -(1/2) R_K(tau) * M_Pl_4^2     (D-16)

Now substitute (D-13) for M_Pl_4^2:

    rho_vac = -(1/2) R_K(tau) * V_K * M_12^{10}     (D-17)

But R_K(tau) has dimensions of (length)^{-2} = M_KK^2 on the fiber, so R_K(tau) ~ c * M_KK^2 where c is a dimensionless curvature coefficient. And V_K ~ V_0 * M_KK^{-8} where V_0 is a dimensionless volume. And M_12^{10} = M_Pl_4^2 / V_K = M_Pl_4^2 * M_KK^8 / V_0.

Putting it all:

    rho_vac ~ (1/2) * |c| * M_KK^2 * V_0 * M_KK^{-8} * M_Pl_4^2 * M_KK^8 / V_0     (D-18)
            = (1/2) * |c| * M_KK^2 * M_Pl_4^2     (D-19)

The internal volume V_K (or equivalently V_0) has CANCELLED EXACTLY. The 4D vacuum energy density depends on M_KK^2 * M_Pl_4^2, not on V_K separately.

This is the central result of this section: **the 4D vacuum energy density from the KK reduction is volume-independent**.

### I.6. Dimensional Analysis Verification

Let me verify (D-19) dimensionally.

- [rho_vac] = energy / volume = M^4 in natural units (GeV^4)
- [M_KK^2 * M_Pl_4^2] = GeV^2 * GeV^2 = GeV^4. CHECK.

The numerical value: with |c| ~ O(1) (from R_K at the fold), M_KK = 7.43 x 10^{16} GeV, M_Pl_4 = 2.44 x 10^{18} GeV:

    rho_vac ~ (1/2) * M_KK^2 * M_Pl_4^2 ~ (1/2) * (7.43e16)^2 * (2.44e18)^2     (D-20)
            ~ (1/2) * 5.52e33 * 5.95e36 ~ 1.64e70 GeV^4

This gives log10(rho_vac / rho_obs) ~ log10(1.64e70 / 2.7e-47) ~ 117. Consistent with the framework's CC gap of 114-118 OOM.

### I.7. The Spectral Action Route

The spectral action provides an independent derivation. The Seeley-DeWitt expansion of the spectral action on M^4 x K gives (Connes-Chamseddine-Marcolli 2007):

    S = Tr f(D_total^2 / Lambda^2) = sum_n f_n Lambda^{12-2n} a_n(D_total^2)     (D-21)

For the Kasparov product factorization (VdD Paper 01, confirmed A-TENSOR-61):

    a_n(D_total^2) = sum_{j+k=n} a_j(D_M^2) * a_k(D_K^2)     (D-22)

The vacuum energy comes from the n = 0 term:

    S_CC = f_0 Lambda^{12} * a_0(D_M^2) * a_0(D_K^2)     (D-23)

Here a_0(D_M^2) = (4 pi)^{-2} * rank(S_M) * Vol(M^4) is proportional to the 4D spacetime volume. The 4D vacuum energy DENSITY is:

    rho_vac = f_0 Lambda^{12} * a_0(D_K^2) * [a_0(D_M^2) / Vol(M^4)]     (D-24)

The ratio a_0(D_M^2) / Vol(M^4) is a number independent of Vol(M^4) -- it is the mode density per unit 4D volume. Therefore rho_vac is:

    rho_vac = f_0 Lambda^{12} * a_0(D_K^2) * (4 pi)^{-2} * rank(S_M)     (D-25)

This depends on a_0(D_K^2) (a fiber quantity, = 6440 at the fold) and the cutoff Lambda, but NOT on the 4D spacetime volume Vol(M^4). The vacuum energy density is intensive.

The gravitational coupling from the a_2 term:

    1/(16 pi G_4) ~ f_2 Lambda^{10} * [a_0(D_M^2) / Vol(M^4)] * a_2(D_K^2)     (D-26)
                   + f_2 Lambda^{10} * [a_2(D_M^2) / Vol(M^4)] * a_0(D_K^2)

Both terms are proportional to (intensive quantity) * (fiber coefficient). The Planck mass is:

    M_Pl_4^2 ~ f_2 Lambda^{10} * a_0(D_K^2) * (curvature terms)     (D-27)

Again, no 4D volume dependence in M_Pl_4. Both rho_vac and M_Pl_4^2 are 4D-volume-independent. The dimensionless ratio:

    rho_vac / M_Pl_4^4     (D-28)

is doubly volume-independent.

**The spectral action and the KK reduction agree**: the CC is intensive.

---

## II. Intensive vs. Extensive: Resolving the Volovik-VdD Disagreement

### II.1. Volovik's Argument (E1.4)

Volovik argues (Volovik-VdD workshop, S63, E1.4):

1. The vacuum energy per KK cell is O(Delta * N_pair / V_cell) ~ O(M_KK).
2. The observed CC is rho_obs ~ 10^{-122} M_Pl^4.
3. The ratio rho_obs / (Delta / V_cell) ~ 10^{-114}.
4. This ratio equals (R_H / R_K)^3 ~ (10^{39})^3 = 10^{117}, within 3 OOM.
5. Conclusion: the CC is the single-pair binding energy "spread" across the emergent 4D volume.

### II.2. VdD's Correction (Gap 1)

VdD responds (Volovik-VdD workshop, S63, Re:E1 Gap 1): the CC is intensive, not extensive. The Kasparov factorization gives a_0(D_total) = a_0(D_M) * a_0(D_K), and the vacuum energy density does NOT dilute with base-space volume growth.

### II.3. The KK Resolution

Both Volovik and VdD are partially correct. The resolution comes from tracking what is EXTENSIVE and what is INTENSIVE through the dimensional reduction.

**EXTENSIVE quantities** (scale with Vol(M^4)):
- Total vacuum energy: E_vac = rho_vac * Vol(M^4). Grows with volume.
- Total gravitational action: S_grav = (1/16 pi G_4) * integral sqrt(-g_4) R_4. Grows with volume.
- Total spectral action: S = Tr f(D^2/Lambda^2). The trace sums over the full Hilbert space, which grows with Vol(M^4) (more base-space modes).

**INTENSIVE quantities** (independent of Vol(M^4)):
- Vacuum energy DENSITY: rho_vac = f_0 Lambda^{12} * a_0(D_K^2) * (normalization). Set by fiber spectrum.
- Newton's constant: G_4 = 1 / (V_K * M_12^{10}). Set by fiber volume and fundamental scale.
- The Planck mass: M_Pl_4^2 = V_K * M_12^{10}. Set by fiber volume and fundamental scale.
- The dimensionless CC: rho_vac / M_Pl_4^4. Set entirely by fiber spectrum ratios.

**Volovik's error**: He writes the CC gap as "(R_H/R_K)^3 ~ 10^{117}", suggesting the observed CC is the KK-scale energy diluted over the Hubble volume. This contains two errors:

1. **(R_H/R_K)^3 = 10^{176}, not 10^{117}.** The ratio R_H/R_K = M_KK/H_0 = 5.16 x 10^{58}. Cubed: 10^{176}. The d = 3 volume ratio overshoots the CC gap by 59 OOM (Section III.1).

2. **The dimensionless CC is volume-independent.** The ratio rho_vac/M_Pl_4^4 does not contain the Hubble volume. The 4D volume cancels between the vacuum energy and the gravitational action (Section I.5).

The match at d = 2 -- (R_H/R_K)^2 = 2.66 x 10^{117} versus CC gap ~ 10^{117} -- is an algebraic identity. From the Friedmann equation H_0^2 = rho_obs / M_Pl^2 and the KK reduction rho_vac ~ M_KK^2 * M_Pl^2:

    (R_H/R_K)^2 = (M_KK/H_0)^2 = M_KK^2 * M_Pl^2 / rho_obs ~ 2 * rho_vac / rho_obs     (D-29)

This is the Friedmann equation restated, not a volume dilution mechanism (Section III.2).

### II.4. The Physical Content of "Intensive"

What does it MEAN for the CC to be intensive? The explicit reduction in Section I shows:

1. When you compactify from D dimensions to 4, both rho_vac AND G_4 absorb the internal volume V_K (Eqs. D-13, D-17).

2. In the dimensionless CC ratio rho_vac/(M_Pl_4^4), the V_K factors cancel (Eq. D-19).

3. The CC problem is the statement that the FIBER'S intrinsic curvature scale (set by R_K(tau) ~ M_KK^2) is too large compared to what observation requires.

4. Making the 4D universe bigger (increasing Vol(M^4)) does not help, because it simultaneously makes the 4D gravitational action bigger, and the ratio is unchanged.

In substrate language: the vacuum energy density is a LOCAL property of the fabric -- it is the spectral weight per fiber point, not the total spectral weight divided by the number of fiber points. Growing the fabric (creating more fiber points) creates proportionally more vacuum energy AND proportionally more gravitational action. The density is a fixed number set by the internal geometry.

### II.5. Verdict on the Disagreement

**VdD is correct on all points**: the CC density is intensive, volume dilution does not reduce it, and the Kasparov factorization makes this structurally clear.

**Volovik's physical intuition identifies a real hierarchy** (M_KK/H_0 ~ 10^{58}), but the mechanism he proposes (volume dilution of binding energy) does not work for the density. The numerical match at (R_H/R_K)^2 ~ 10^{117} is the Friedmann equation restated, not evidence for dilution. The natural volume ratio (R_H/R_K)^3 ~ 10^{176} does NOT match the CC gap.

The dimensional reduction is unambiguous. No version of volume dilution applied to the vacuum energy DENSITY works within the standard KK framework.

---

## III. The 117 OOM Hierarchy: Origin and Role

### III.1. Where Does 10^{117} Come From?

The ratio (R_H/R_K)^3 involves two length scales:

**The Hubble radius:**

    R_H = c / H_0 = 1.38 x 10^{26} m = 4.27 Gpc     (D-34)

In natural units: R_H = 1 / H_0 = 1 / (1.44 x 10^{-42} GeV) = 6.97 x 10^{41} GeV^{-1}.

**The KK radius:**

    R_K = 1 / M_KK = 1 / (7.43 x 10^{16} GeV) = 1.35 x 10^{-17} GeV^{-1}     (D-35)

The ratio:

    R_H / R_K = M_KK / H_0 = 7.43 x 10^{16} / 1.44 x 10^{-42} = 5.16 x 10^{58}     (D-36)

Cubed:

    (R_H / R_K)^3 = (5.16 x 10^{58})^3 = 1.38 x 10^{176}     (D-37)

This is 10^{176}, NOT 10^{117}. The difference is 59 orders of magnitude. Volovik's claim that (R_H/R_K)^3 ~ 10^{117} (matching the CC gap) is numerically INCORRECT for the natural definition of R_K = 1/M_KK.

**Tracing Volovik's estimate.** Volovik writes (E1.4): "The ratio rho_obs / (Delta / V_cell) ~ 10^{-114} is the 114-OOM gap. This ratio would be explained if the effective volume at the current epoch is 10^{114} times the single-cell volume -- a number that is the ratio of the Hubble volume to the Kaluza-Klein volume, (R_H / R_K)^d for some effective dimension d."

For this to work with (R_H/R_K) = 5.16 x 10^{58}:
- d = 3 gives 10^{176} (59 OOM too large)
- d = 2 gives 10^{117} (matches the CC gap to 0.2 OOM)

So Volovik's estimate implicitly uses d = 2, not d = 3. This is because the relevant "volume" is not a spatial 3-volume but a 2-dimensional cross-section or an effective area ratio. There is no geometric justification within the M^4 x SU(3) framework for choosing d = 2. The numerological match at d = 2 is coincidental.

**Using spatial volumes directly.** The Hubble 3-volume V_H ~ (4 pi/3) R_H^3 ~ 10^{79} m^3 and the KK "volume" V_K = Vol(SU(3)) * R_K^8 are dimensionally incomparable (3-volume vs 8-volume). The tessellation cell count is:

    N_cells ~ V_H / l_cell^3     (D-38)

where l_cell is the tessellation cell spacing. If l_cell ~ R_K = 1/M_KK, then N_cells ~ (R_H * M_KK)^3 ~ 10^{176} -- the same number as (R_H/R_K)^3 and not 10^{114}.

**The actual 114 OOM.** The CC gap is:

    rho_vac / rho_obs = 10^{114}     (D-43)

From the formula chain in framework-cc-oom.md:

    rho_vac = (2/pi^2) * a_0 * M_KK^4 ~ 8.44 x 10^{71} GeV^4 (Kerner) or 3.97 x 10^{68} (gravity)     (D-44)
    rho_obs = 2.7 x 10^{-47} GeV^4     (D-45)

The gap is 115-119 OOM depending on M_KK route. The 114 OOM number comes from the q-theory formulation (CC-QTHEORY-GGE-62): Lambda_CC = 0.838 M_KK^4 ~ 2.56 x 10^{67} GeV^4, giving Lambda_CC / Lambda_obs = 9.46 x 10^{113} ~ 10^{114}.

### III.2. The Numerological Non-Coincidence

The approximate numerical agreement between (R_H/R_K)^d and the CC gap requires d = 2, not d = 3, and is NOT a coincidence in the geometric sense.

The Hubble parameter satisfies:

    H_0^2 ~ G_4 * rho_obs ~ rho_obs / M_Pl^2     (D-46)

Therefore:

    R_H / R_K = M_KK / H_0 ~ M_KK * M_Pl / rho_obs^{1/2}     (D-47)

The CC gap is:

    rho_vac / rho_obs ~ a_0 * M_KK^4 / rho_obs     (D-48)

The ratio:

    (R_H/R_K)^3 / (rho_vac/rho_obs) = (M_KK/H_0)^3 / (a_0 * M_KK^4/rho_obs)     (D-49)
                                      = rho_obs^{1/2} / (a_0 * M_KK * H_0^3)
                                      = M_Pl^3 / (a_0 * M_KK * H_0^2)     (D-50)

Numerically: M_Pl^3 / (a_0 * M_KK * H_0^2) = (2.44e18)^3 / (6440 * 7.43e16 * (1.44e-42)^2) = 1.45e55 / (9.91e-67) ~ 10^{59}. Verified computationally: the ratio is 9.37 x 10^{58}.

For the match at d = 2:

    (R_H/R_K)^2 = (5.16 x 10^{58})^2 = 2.66 x 10^{117}     (D-51)
    rho_vac/rho_obs = 1.47 x 10^{117}     (D-52)

These agree to within a factor of 1.8 -- seemingly remarkable. But the match at d = 2 is an algebraic identity in disguise:

    (R_H/R_K)^2 = (M_KK/H_0)^2 = M_KK^2 * M_Pl^2 / rho_obs     (D-53)

and from (D-19):

    rho_vac ~ (1/2) * M_KK^2 * M_Pl^2     (D-54)

so (R_H/R_K)^2 = 2 * rho_vac / rho_obs. The "coincidence" at d = 2 is just the Friedmann equation restated. It has zero explanatory content.

The factor of 2 discrepancy between (D-53) and (D-54) arises from the O(1) coefficient in the KK reduction (the factor (1/2) in Eq. D-19 versus the exact spectral action value involving a_0 and 2/pi^2). The coincidence is exact to the extent that rho_vac ~ M_KK^2 * M_Pl^2, which is just dimensional analysis for a CC set by the compactification curvature.

### III.3. Role in the Framework

The ratio (R_H/R_K)^d plays no CAUSAL role in the framework's CC dynamics. The match at d = 2 is the Friedmann equation restated (Eq. D-53). The match at d = 3 does not hold (off by 59 OOM).

The volume ratio is a derived number -- a consequence of:
1. M_KK ~ 10^{16-17} GeV (set by spectral action / gauge coupling extraction)
2. H_0 ~ 10^{-42} GeV (set by observation, linked to rho_obs through Friedmann)

Both numbers encode the M_KK/M_Pl hierarchy and the Hubble/Planck hierarchy. The volume ratio restates the CC gap in geometric language without explaining it. It is a diagnostic, not a mechanism.

---

## IV. Modified Versions: What Survives

### IV.1. Mode-Counting Version

The spectral action at the fold sums over 992 eigenvalues (at L_max = 6):

    S_fold = sum_n d_n |lambda_n(tau_fold)| = 250,360.68 M_KK     (D-55)

The a_0 coefficient counts modes:

    a_0 = sum_n d_n = 6440     (D-56)

One could ask: what if only a FRACTION of the 992 modes contribute to the gravitating vacuum energy? If N_eff modes contribute instead of 992:

    rho_vac^{eff} = (N_eff / 992) * rho_vac     (D-57)

To reduce the CC gap by 114 OOM requires N_eff / 992 ~ 10^{-114}, i.e., N_eff ~ 10^{-111}. This is less than one mode. There is no regime in which mode counting alone resolves the CC.

**However**, the mode-counting version DOES have structural content. The a_0 coefficient is:

    a_0(D_K^2) = (4 pi)^{-dim(K)/2} * rank(S_K) * Vol(K)     (D-58)

For SU(3) with dim(K) = 8, spinor rank = 2^{[8/2]} = 16 (spinor bundle on 8-manifold), Vol(K) = 1349.74:

    a_0 = (4 pi)^{-dim(K)/2} * 2^{[dim(K)/2]} * Vol(K)     (D-59)
        = (4 pi)^{-4} * 16 * 1349.74

This gives 0.875, not 6440. The discrepancy is because a_0 in the framework is the DIRECT spectral sum a_0 = sum_n d_n = 6440 (the total multiplicity-weighted mode count at L_max = 6), which includes the full Peter-Weyl tower up to the truncation level. The Gilkey formula gives the leading asymptotic coefficient, which equals the spectral sum only in the continuum limit. At finite L_max = 6, the mode count 6440 is the actual number entering the spectral action, and the Gilkey formula is a smooth approximation to it.

The correct interpretation: a_0 = 6440 is the weighted count of Dirac eigenvalues at the fold, and it is an intrinsic fiber quantity. No volume dilution can change it.

### IV.2. Spectral Dilution Version

Consider the spectral action at general tau, not just the fold:

    S(tau) = sum_n d_n f(lambda_n(tau)^2 / Lambda^2)     (D-57)

As tau increases past the fold:
- The eigenvalue spectrum {lambda_n(tau)} spreads (some eigenvalues increase, others decrease)
- The cutoff function f suppresses large eigenvalues
- The mode density near zero eigenvalue is controlled by the van Hove singularity structure

If S(tau) decreases with tau, the effective a_0 contribution per 4D volume decreases. This is NOT volume dilution -- it is SPECTRAL dilution: the eigenvalue landscape changes, reducing the vacuum energy density.

This IS Path C (transit-as-relaxation), not a separate mechanism. The a_0 floor obstruction (VdD Gap 2, Theorem T14) blocks this: a_0 = const for volume-preserving Jensen, so the zeroth spectral moment is tau-independent. Only the curvature-dependent contributions (a_2, a_4, ...) can relax.

**What a modified volume dilution could mean**: if one reinterprets "volume dilution" as "the transit increases the effective tau, which reduces the curvature contributions a_2(tau) and a_4(tau), which dilutes the curvature-dependent vacuum energy across the emergent 4D spacetime," then this is just Path C restated. The mechanism is spectral, not volumetric.

### IV.3. Tessellation Version

The 32-cell tessellation introduces a finite number of fabric cells. The total vacuum energy is:

    E_total = N_cells * E_cell     (D-60)

where E_cell is the vacuum energy per cell and N_cells = 32 (fixed by the framework's tessellation). The vacuum energy per emergent Hubble volume is:

    rho_H = E_total / V_H = N_cells * E_cell / V_H     (D-61)

But E_cell = rho_vac * V_cell (where V_cell is the 4D volume of one tessellation cell), so:

    rho_H = N_cells * rho_vac * V_cell / V_H = rho_vac * (N_cells * V_cell / V_H)     (D-62)

If the tessellation covers the entire Hubble volume (N_cells * V_cell = V_H), then rho_H = rho_vac. The density is unchanged.

If the tessellation does NOT cover the entire Hubble volume (the 32 cells are the ONLY fabric, and the rest of "space" is empty), then the fabric is a finite object embedded in... what? In the substrate picture, there is no "rest of space" -- the fabric IS space. The tessellation IS the universe. This removes the dilution argument entirely.

**Assessment**: The tessellation version adds nothing to volume dilution. The 32-cell fabric either covers the Hubble volume (density unchanged) or IS the entire universe (no dilution).

### IV.4. Dynamic Volume Version (Time-Dependent Compactification)

Consider the possibility that V_K changes with cosmological time (moduli dynamics, Einstein-Bergmann dilaton evolution). The 4D CC would then be:

    rho_vac(t) ~ R_K(t)^{-2} * [V_K(t) * M_12^{10}]     (D-63a)

Both R_K(t) and V_K(t) change, and the CC can evolve. This IS the modulus equation:

    G_tt Box(tau) + dV_eff/dtau = 0     (D-63b)

with G_tt = 5 (the moduli kinetic metric; source: session 33 modulus equation).

In this version, the CC is NOT diluted by volume growth -- it EVOLVES because the fiber geometry changes. The vacuum energy density changes because the eigenvalue spectrum of D_K changes with tau, not because the same energy is spread over more 4D volume.

This is again Path C, not Path D. The dynamic modulus version is a physically distinct mechanism from naive volume dilution.

---

## V. Required Computations and Assessment

### V.1. Assessment

| Claim | Status | Structural Reason |
|:------|:-------|:------------------|
| Naive volume dilution resolves CC | **CLOSED** | CC is intensive. V_K cancels in rho_vac/M_Pl^4. Eqs. (D-13), (D-19) |
| (R_H/R_K)^3 = 10^{117} matches CC gap | **REFUTED** | (R_H/R_K)^3 = 10^{176}, not 10^{117}. Off by 59 OOM. Match at d=2 is Friedmann restatement. |
| Mode-counting reduces CC | **CLOSED** | N_eff/992 ~ 10^{-114} required. Less than one mode |
| Spectral dilution reduces CC | **REDIRECTED to Path C** | a_0 floor blocks full reduction (Theorem T14). Curvature terms can relax. |
| Tessellation dilution | **CLOSED** | 32 cells either cover V_H (density unchanged) or ARE the universe (no dilution) |
| Dynamic volume evolution | **REDIRECTED to Path C** | Modulus equation changes fiber geometry, not 4D volume. Same as transit relaxation. |

### V.2. What Path D Teaches

Path D is closed as a CC resolution, but it clarifies the structure of the CC problem:

1. **The CC is intensive.** This is a theorem of the KK reduction, not an assumption. Any mechanism that claims to reduce the CC must modify the fiber spectrum or the fiber-to-gravity coupling, not the 4D volume. This eliminates a large class of proposed solutions.

2. **The claimed numerological coincidence fails at d=3 and is tautological at d=2.** (R_H/R_K)^3 = 10^{176}, overshooting the CC gap by 59 OOM. The match at d=2 is the Friedmann equation H_0^2 = rho_obs/M_Pl^2 restated. No volume ratio explains the CC gap.

3. **The only volume that matters is V_K.** The internal volume V_K enters the CC problem through M_Pl^2 = V_K * M_12^{10}. If V_K were different (different compactification manifold, different radius), M_KK and M_Pl would change, and so would the CC gap. But V_K is fixed by the Jensen volume-preservation constraint (tau-independent). The CC gap is structurally frozen.

4. **All surviving CC paths must modify the fiber, not the base.** Paths B (gravitational integrability breaking), C (transit-as-relaxation), E (self-consistent BdG triple), and G (sector-selective breaking) all operate on the fiber Dirac operator D_K or its BCS modification D_BdG. Path D's failure confirms that the CC problem lives entirely in the fiber sector.

### V.3. Pre-Registerable Computations

No new computations are needed for Path D itself (it is closed). However, the analysis motivates:

**S-ASYMPTOTIC-64** (from Path C, already proposed in framework-cc-oom.md). Compute S(tau) for tau = 0.5, 1, 2, 5, 10. Determine whether the curvature-dependent terms a_2(tau), a_4(tau) approach zero at large tau. This is the spectral dilution mechanism that survives from Path D's debris. The a_0 floor (Theorem T14) means only the curvature terms can relax, but their large-tau behavior is unknown.

Pass criterion: a_2(tau = 10) / a_2(tau_fold) < 0.01 (99% reduction). This would indicate the curvature-dependent CC can relax through transit dynamics. Fail criterion: a_2(tau = 10) / a_2(tau_fold) > 0.5 (less than 50% reduction). This would close the transit-as-relaxation path for the curvature-dependent CC.

---

## VI. Structural Theorem: Intensivity of the KK Vacuum Energy

**Theorem (KK CC Intensivity).** For any product compactification M^d x K^n with product metric g = g_M + g_K (O'Neill tensors A = T = 0), the dimensionless cosmological constant Lambda / M_Pl^{d/(d-2)} is independent of the d-dimensional spacetime volume Vol(M^d).

**Proof.** The D-dimensional Einstein-Hilbert action on M^d x K^n is:

    S_D = (1 / 2 kappa_D^2) integral d^D x sqrt(-g_D) R_D     (D-63)

where kappa_D^2 = 8 pi G_D = M_D^{-(D-2)}. With the product metric ansatz, R_D = R_d + R_K and sqrt(-g_D) = sqrt(-g_d) * sqrt(g_K). Integrating over K:

    S_D = (V_K / 2 kappa_D^2) integral d^d x sqrt(-g_d) [R_d + R_K]     (D-64)

The d-dimensional Newton's constant is identified from the R_d term:

    1 / (16 pi G_d) = V_K / (2 kappa_D^2)     (D-65)

The d-dimensional Planck mass satisfies M_{Pl,d}^{d-2} = V_K * M_D^{D-2}.

The CC term is the R_K piece:

    S_CC = (V_K / 2 kappa_D^2) integral d^d x sqrt(-g_d) R_K     (D-66)

Comparing with the standard CC action -(Lambda_d / 8 pi G_d) integral d^d x sqrt(-g_d):

    Lambda_d = -(1/2) R_K     (D-67)

The vacuum energy density is:

    rho_d = Lambda_d / (8 pi G_d) = -(1/2) R_K / (8 pi G_d)
          = -(1/2) R_K * M_{Pl,d}^{d-2} / (8 pi)     (D-68)

The dimensionless CC is:

    rho_d / M_{Pl,d}^d = -(R_K / 16 pi) * M_{Pl,d}^{-2}     (D-69)

Now M_{Pl,d}^{d-2} = V_K * M_D^{D-2}, so M_{Pl,d}^{-2} = (V_K * M_D^{D-2})^{-2/(d-2)}. Therefore:

    rho_d / M_{Pl,d}^d = -(R_K / 16 pi) * (V_K * M_D^{D-2})^{-2/(d-2)}     (D-70)

Every quantity on the right-hand side is determined by the fiber geometry (R_K, V_K) and the fundamental scale (M_D). None depends on Vol(M^d). QED.

**Consequence**: No cosmological evolution (expansion of M^d) changes rho_d / M_{Pl,d}^d. The CC problem is a fiber problem. This is the structural reason Path D fails.

---

## Appendix: Notation and Sources

| Symbol | Definition | Source |
|:-------|:-----------|:-------|
| M_12 | Fundamental 12D Planck mass | Eq. (D-1) |
| kappa_12 | 12D gravitational coupling: kappa_12^2 = 8 pi G_12 = M_12^{-10} | Eq. (D-1) |
| V_K | Internal volume Vol(SU(3)) = 1349.74 (tau-independent) | canonical_constants.py |
| M_KK | KK mass scale = 7.43 x 10^{16} GeV (gravity route) | canonical_constants.py |
| M_Pl_4 | Reduced 4D Planck mass = 2.435 x 10^{18} GeV | canonical_constants.py |
| a_0 | Zeroth SDW coefficient = 6440 at fold | S42, framework-cc-oom.md |
| R_K(tau) | Fiber scalar curvature | Baptista Eq. 3.70 |
| H_0 | Hubble constant = 1.44 x 10^{-42} GeV | canonical_constants.py |
| rho_obs | Observed vacuum energy = 2.7 x 10^{-47} GeV^4 | Planck 2018 |

**KK Paper Citations**:
- Paper 02 (Kaluza 1921): Original 5D metric ansatz and cylinder condition
- Paper 03 (Klein 1926): S^1 compactification, charge quantization, KK mass tower
- Paper 04 (Einstein-Bergmann 1938): Periodicity, dilaton, variational principle
- Paper 05 (DeWitt 1964): Fiber bundle interpretation of non-Abelian KK
- Paper 10 (Freund-Rubin 1980): Flux-driven spontaneous compactification
- Paper 14 (DNP 1986): Complete KK spectrum on S^7, consistent truncation
- Paper 19 (ADD 1998): M_Pl^2 = M_{4+n}^{2+n} * V_n (hierarchy from large extra dims)

**Framework Citations**:
- S42: Constants snapshot (a_0, a_2, a_4, M_KK)
- S44: Vol(SU(3)) correction (Weyl integration formula)
- S56: FABRIC-PVAC-56 (Josephson self-tuning, CC unchanged)
- S61: A-TENSOR-61 (A = T = 0 exact for product metric)
- S62: CC-QTHEORY-GGE-62 (Lambda_CC = 0.838 M_KK^4, 114 OOM)
- S63: Volovik-VdD workshop (E1.4 volume dilution, Gap 1 intensive correction)
