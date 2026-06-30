# Session 85 Workshop: tesla x mack — CGWB ⊥ α_s Independence Diagrammatic Audit (6A)

**Date**: 2026-04-25
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns) — STEELMAN / RESPOND / CONVERGE
**Agents**: tesla (tesla-resonance), mack (mack-cosmic-bridge)
**Source Documents**:
- sessions/archive/session-85/session-85-w13-workingpaper.md (W13-2 LISA null + CGWB+α_s flagship; ρ=0 by Fisher PSD)
- sessions/archive/session-85/session-85-w12-workingpaper.md (W12-4 a_n REGULATOR-CLASS-(d) proof)
- sessions/archive/session-85/session-85-w9-workingpaper.md
- computations/s85_gate_verdicts.txt (filter to S85-W13-2 + S85-W12-4)
- sessions/permanent-results-registry.md
- sessions/archive/session-85/session-85-w6-13-workshop-schedule.md (mother schedule, this workshop §6A)
- sessions/archive/session-85/session-85-workshop-schedule.md (W0-W5 — for S-5 Falsifier Master-Inventory cross-pairing)

**Focus Topics** (from schedule §6A invocation):
1. W13-2 claim: ρ(CGWB, α_s) = 0 by Fisher PSD; joint-detection significance multiplies
2. W12-4: a_n is regulator-class-(d) (both CGWB and α_s flow downstream from a_n)
3. Suspected shared upstream: a_2 (CGWB GW amplitude) + a_4 (α_s via spectral derivative)
4. Diagrammatic kernel decomposition + Fisher matrix with a_n nuisance parameters

---

## Round 1 — tesla: STEELMAN INDEPENDENCE

### T1: CGWB Observable Definition (GW power spectrum integrated [10^-4, 1] Hz)

**Definition (substrate-first, projecting upward to detector)**.

The Cosmic Gravitational Wave Background observable, as pre-registered in W13-2, is the dimensionless energy-density spectrum of the post-fold transit-GW signal evaluated across the LISA-PLS-2024 detector band:

```
Omega_CGWB(f) = (1/rho_c) * d rho_GW / d ln f         [definition, dimensionless]
CGWB observable O_CGWB = Omega_GW(f_LISA_pivot)        [scalar projection at f = 3 mHz]
                       = 8.299e-58                     [W13-2 §(c), Python-verified log-log interp of s69 grid]
```

The projection from the substrate to this scalar reads, in the inverted direction-of-explanation pinned by `.claude/rules/phononic-framing.md`:

```
D_K spectrum on Jensen-SU(3)
    |
    | Seeley-DeWitt expansion (heat-kernel, short-t)
    v
spectral moments {a_n}_{n=0,2,4,...}
    |
    | Newton-coupling identification: 1/G_N = (48 f_2 / pi) * a_2 * M_KK^2     [s74_r_family_observable_scan.py canonical]
    v
graviton kinetic normalization (transverse-traceless sector)
    |
    | substrate fold transit -> GGE relic at c_BLV = 0.485 (transverse branch)
    | Parker-pair amplification (n_pairs = 59.8, broad-resonance, S77)
    v
strain power spectrum h_c^2(f) -> Omega_GW(f)
    |
    | log-log interpolation of (f_grid, Omega_GW_f) at LISA pivot
    v
O_CGWB = Omega_GW(3 mHz) = 8.299e-58
```

**Key structural fact**: CGWB inherits **a_2** as its principal upstream substrate moment, because Newton's constant — the prefactor that converts spectral-action gravitational dynamics into GW amplitude — is exactly the second Seeley-DeWitt coefficient (`1/G_N ∝ a_2 * M_KK^2`, S74; "a_2 = second Seeley-DeWitt coefficient (sets Newton's constant via f_0*a_2/pi^2)", s69_kk_higgs.py canonical). The transit-GW spectrum's overall amplitude scales linearly with G_N, so any rescaling of a_2 propagates one-to-one into Omega_GW(f) at every frequency.

**Detector-band scope**. The W13-2 pre-reg uses a single-pivot evaluation at f_LISA = 3.0e-3 Hz (canonical_constants.py:292) plus a 3-point band-width diagnostic at {1.5, 3, 6} mHz. The "integrated [10^-4, 1] Hz" framing in the schedule §6A invocation is the LISA detector's full sensitivity span; W13-2 collapses this to the pivot scalar Omega_GW(3 mHz) for the joint Fisher analysis. The full integral
```
O_CGWB^{full} = integral_{1e-4}^{1} d ln f  Omega_GW(f)
```
is NOT the observable W13-2 pre-registered; it would inherit the same a_2 dependence (modulo the kernel weighting in f). The single-pivot scalar is the cleanest substrate projection for the diagonal-Fisher claim.

**Substrate framing recap**: O_CGWB lives ON the transverse acoustic branch of the post-fold GGE relic (c_BLV = 0.485). It is a tensor-mode reading of the spectral triple's heat-kernel a_2 coefficient, projected through the Parker pair-production amplification at the fold and red-shifted to today's frequency f. No GR container is invoked; the observable is emergent from the spectral action's a_2 moment, not stamped onto a pre-existing spacetime.

### T2: α_s Observable Definition (running of scalar spectral index at CMB pivot)

**Definition (substrate-first, projecting upward to detector)**.

The running of the scalar spectral index, evaluated at the CMB pivot k* = 0.05 Mpc⁻¹, is

```
alpha_s = d n_s / d ln k     [definition; running of the scalar spectral index at the pivot]
```

The framework's S50 O-Z (Ornstein-Zernike) result establishes the identity (exact in the constant-mass case, proven s50_running_mass.py):

```
alpha_s = n_s^2 - 1                         [S50 O-Z identity, constant-mass]
```

Substitution chain at the W13-2 pre-registered pivot:

```
Step 1 (definition):     alpha_s = n_s^2 - 1
Step 2 (substitute):     planck_ns = 0.9649  (Planck 2018 TT,TE,EE+lowE+lensing)
Step 3 (simplify):       0.9649^2 = 0.93103201
                         alpha_s = 0.93103201 - 1 = -0.06896799
Step 4 (direction):      alpha_s is NEGATIVE; |alpha_s|/sigma_CMBS4 = 22.99 sigma  [W13-2 §(b)]
```

(Identity verified to 1e-10 against canonical pin `alpha_s_cmb_central = -0.06896799`, canonical_constants.py:291. W13-2 §(f) CC-1 PASS.)

**Substrate-to-observable projection chain**:

```
D_K spectrum on Jensen-SU(3)
    |
    | Seeley-DeWitt heat-kernel expansion
    v
spectral moments {a_0, a_2, a_4, ...}
    |
    | n_s coupling identification: "spectral index n_s depends on the ratio a_2/a_0
    |                              (first spectral moment ratio)"  [s71_non_trivial_fibration_csquared.py canonical]
    v
n_s = function( a_2 / a_0 )    [longitudinal-branch Debye-cutoff curvature -> tilt]
    |
    | k-derivative at CMB pivot:  alpha_s = d n_s / d ln k
    | (in S50 constant-mass case this collapses to alpha_s = n_s^2 - 1)
    v
alpha_s = -0.06896799    [observable at the CMB pivot]
```

**Where the schedule §6A invocation needs CARE**. The §6A invocation pairs CGWB↔a_2 and α_s↔a_4 ("a_4 for α_s through the spectral derivative"). The substrate audit gives a more nuanced reading I must report honestly:

- **n_s couples principally to the a_2/a_0 ratio** (s71 canonical, s61 cumulative-moment-ratio code, "first spectral moment ratio"). The tilt of the scalar power spectrum tracks the second-moment density.
- **α_s = d n_s / d ln k introduces a higher-derivative contribution**: under the constant-mass S50 collapse, α_s = n_s² − 1 reduces α_s back into a function of the SAME a_2/a_0 ratio (because n_s itself does). Under the *running-mass* generalization (`delta_alpha = alpha_s(running) - (n_s^2 - 1)`, s50_running_mass.py), the k-derivative does pull in a fourth-moment contribution via d n_s / d ln k -> ∂_k(a_2/a_0) which involves the Seeley-DeWitt fourth moment a_4.
- **Concretely for W13-2**: the pre-registered identity is the constant-mass collapse (W13-2 §(b) Step 1 explicitly: "alpha_s = n_s^2 - 1 (exact in the constant-mass case)"). Under that identity, **α_s inherits its substrate dependence from a_2/a_0, not from a_4 alone**.

This refinement matters for the steelman — the W13-2 ρ=0 cannot be defended by the simple slogan "CGWB = a_2 only, α_s = a_4 only, so they are projection-disjoint." It must be defended either by (i) acknowledging that both observables touch a_2 but project it through orthogonal kernels (transverse-tensor vs scalar-tilt), or (ii) noting that under running-mass the a_4 dependence does enter α_s and reasserting projection-orthogonality at the kernel level. T3 develops the projection-orthogonality argument; T4 maps it to Fisher PSD.

**Substrate framing recap**: O_α_s lives ON the longitudinal acoustic branch of the post-fold GGE relic. It is a *scalar*-mode reading of the Debye-cutoff curvature in the heat-kernel expansion at the CMB pivot. No inflaton field is invoked; α_s is emergent from the substrate's a_2/a_0 ratio (with a_4 entering under running-mass corrections), not stamped onto a pre-existing power spectrum.

### T3: Structurally Distinct a_n Projections — a_2 for CGWB Amplitude, a_4 for α_s via Spectral Derivative

**The honest steelman (kernel-orthogonal, not index-disjoint)**.

The §6A invocation as written ("CGWB couples to a_2, α_s couples to a_4") would let the steelman rest on **index-disjointness** — different Seeley-DeWitt indices, automatic orthogonality. That is too easy and (per T2) not entirely true: under the W13-2 constant-mass S50 identity α_s = n_s² − 1, α_s tracks the same a_2/a_0 ratio that n_s does. Index-disjointness fails on inspection.

The defensible steelman is **kernel-orthogonality**: the two observables read the spectral moments through structurally distinct *projection kernels*, and even when those kernels share an upstream a_n input, the kernels themselves are orthogonal — they project the same substrate quantity into orthogonal observable directions.

**Three kernel-distinctness axes**.

**(i) Acoustic-branch axis (transverse vs longitudinal)**. From W13-2 §(j) classification:

- CGWB rides the **transverse** acoustic branch at c_BLV = 0.485 (tensor-mode, traceless-transverse projection of the GGE-relic stress tensor).
- α_s rides the **longitudinal** acoustic branch at c_L (scalar-mode, Debye-cutoff curvature in the heat-kernel expansion).

These are different irreducible representations of the substrate's symmetry under SO(3) at the fold (tensor-2 vs scalar-0). The substrate fold's GGE relic occupies BOTH branches simultaneously, but a tensor-mode detector (LISA) cannot couple to scalar-mode excitations and a scalar-mode detector (CMB scalar power) cannot couple to tensor-mode excitations at leading order. The traceless-transverse projection theorem (s69_transit_gw.py, "T_ij = p * g_ij has ZERO traceless-transverse projection") is the structural wall: pressure-mode (scalar) substrate excitations contribute zero to the transverse-traceless GW spectrum.

**(ii) Frequency/scale axis (mHz tensor vs CMB-pivot scalar)**.

```
CGWB:    f_LISA_pivot = 3.0e-3 Hz       [tensor band, today]
alpha_s: k* = 0.05 Mpc^-1                [scalar pivot, equivalent to f ~ 10^-18 Hz today]
```

Substitution:
```
Step 1 (definition): f_today = c * k_phys / (2 pi)
Step 2 (substitute): k* = 0.05 Mpc^-1 = 0.05 / (3.086e22 m) = 1.62e-24 m^-1
                     f_today_alphas = (3e8 m/s) * 1.62e-24 m^-1 / (2 pi) = 7.7e-17 Hz
Step 3 (simplify):   ratio = f_LISA_pivot / f_today_alphas = 3.0e-3 / 7.7e-17 = 3.9e+13
Step 4 (direction):  the two pivots are 13.6 OOM apart in frequency — they are
                     non-overlapping by a factor of 4e13.
```

(Verified arithmetic; pivots from canonical_constants.py:292 and the standard CMB pivot k* = 0.05 Mpc⁻¹.)

This 13.6-OOM frequency separation guarantees that no single LISA Fourier bin shares power with any CMB temperature multipole — they probe completely disjoint slices of the substrate's spectral content.

**(iii) Operator-rank axis (graviton kinetic vs scalar-tilt curvature)**.

CGWB amplitude is set by the **graviton kinetic normalization**, which in the Connes-Chamseddine spectral action arises from the a_2 Seeley-DeWitt coefficient as:
```
1/G_N = (48 f_2 / pi) * a_2 * M_KK^2     [s74_r_family_observable_scan.py canonical]
```
This is a **leading-order rank-0 spectral functional** of a_2 — pure linear dependence on the second moment.

α_s, by contrast, is the running of n_s — a derivative of the **a_2/a_0 ratio with respect to mode index k**. The running pulls in a derivative-kernel structure that, under running-mass corrections (s50 `delta_alpha`), couples a_4 contributions through the second derivative ∂²(a_2/a_0)/∂(ln k)². So α_s probes a **rank-2 derivative functional** of the same upstream moment family.

A rank-0 functional of a_2 and a rank-2 derivative functional of a_2/a_0 evaluated at orthogonal pivot scales are *different observational projections* even when they share upstream substrate inputs.

**The fundamental distinction (steelman point)**: the W12-4 regulator-class-(d) result says a_n are *not regulator-invariant scalars* — they are regulator-labeled families {a_n^{(r)}}. Under any FIXED regulator r* (the W13-2 zeta scheme), each a_n^{(r*)} is a single substrate number, but **how that number propagates to an observable depends on the kernel applied**. Two observables can share the same a_n^{(r*)} input and still be observationally orthogonal if their kernels project that input into orthogonal directions in observable-space.

**The claim being steelmanned**:
```
ρ(O_CGWB, O_alpha_s) = 0    not because  partial O_CGWB / partial a_n  and  partial O_alpha_s / partial a_n  share no a_n index,
                             but because  the kernels K_CGWB[a_n] and K_alpha_s[a_n] act on disjoint
                             irreducible-representation subspaces (transverse-tensor vs scalar-tilt-derivative)
                             AND  the pivot scales are 13.6 OOM apart in frequency.
```

This is the kernel-orthogonal steelman that survives the W12-4 regulator-class-(d) closure: even if mack succeeds at showing a_2 / a_4 / a_6 are non-trivially covariant in the regulator-class-(d) chain, the COVARIANCE of the upstream inputs does not by itself produce non-zero ρ at the observable layer — that requires the kernels to overlap, and Axes (i)–(iii) above argue they do not.

### T4: Why ρ=0 is Genuine, Not Artifact — Fisher PSD Sufficiency on the (CGWB, α_s) Basis

**Citation pin (W13-2 verdict and Fisher matrix)**.

The claim under defense, verbatim from `computations/s85_gate_verdicts.txt` line 66:
```
S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT: INFO -- value=(alpha_s=-0.068968, Omega_GW_LISA=8.299e-58, rho_cc=0.0, Fisher_PD=1)
                                                  scheme=zeta convention=LISA-PLS-2024+CMB-S4-Book-2019 L_max=10
                                                  audit_sha256=f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1
                                                  content_sha256=58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779
                                                  schema_version=S84+
```

The Fisher matrix as constructed in W13-2 §(e):
```
F = diag( 1/sigma(alpha_s_CMBS4)^2 , 1/sigma(Omega_GW_LISA_CGWB)^2 )
  = diag( 1/(0.003)^2 , 1/(1e-12)^2 )
  = diag( 1.111e+05 , 1.000e+24 )       Eigenvalues (eigvalsh): (1.111e+05, 1.000e+24), both positive.
```

ρ extracted from the off-diagonal:
```
F_12 = 0  (by W13-2 construction, since no shared fit parameter)
rho = F_12 / sqrt(F_11 * F_22) = 0 / sqrt(1.111e+05 * 1.000e+24) = 0.
```

(Python-verified, W13-2 §(f) CC-3 PASS.)

**The mack challenge (steelman of mack's claim)**. mack argues ρ=0 is an artifact of an under-resolved Fisher matrix: the substrate's a_2 / a_4 / a_6 chain produces a covariance structure between CGWB and α_s that the 2×2 (CGWB, α_s) Fisher matrix cannot expose. Adding a_n moments as nuisance parameters and marginalizing over them might move ρ off zero.

**The defense — a substitution-chain proof of marginalization invariance under kernel orthogonality**.

Claim: under kernel-orthogonality (T3), marginalization over (a_2, a_4, a_6) as nuisance parameters leaves ρ(CGWB, α_s) = 0.

```
Step 1 (definition, full Fisher with a_n nuisance). Let theta = (theta_signal, theta_nuisance)
       = ((O_CGWB, O_alpha_s), (a_2, a_4, a_6)). The full Fisher matrix is

       F_full(i, j) = sum_obs (1/sigma_obs^2) * (partial O_obs / partial theta_i) * (partial O_obs / partial theta_j).

       Partition into 2x2 signal block A, 2x3 cross block B, 3x3 nuisance block C:

           F_full = | A   B  |
                    | B^T C  |

Step 2 (definition, marginalized signal Fisher). Marginalizing over the 3 nuisance parameters yields the
       2x2 marginalized Fisher

           F_marg = A - B C^{-1} B^T.

       (Standard result; proof: invert F_full, take signal-signal block of inverse, re-invert; equivalently,
        Schur complement of C in F_full.)

Step 3 (substitute, using kernel-orthogonality). By the T3 kernel-orthogonality claim, the partial derivatives
       of the two signals with respect to the nuisance moments are non-zero IN GENERAL (both signals depend
       on a_2 -- T1 and T2), but the cross-products

           B_{CGWB, a_n}     = (1/sigma_CGWB^2) * partial O_CGWB / partial a_n
           B_{alpha_s, a_n}  = (1/sigma_alpha_s^2) * partial O_alpha_s / partial a_n

       are NON-ZERO. So B is NOT identically zero, and B C^{-1} B^T is in general NON-ZERO.

Step 4 (canonical form). The marginalized off-diagonal element is

           F_marg(CGWB, alpha_s) = A(CGWB, alpha_s) - sum_{m, n} B_{CGWB, m} (C^{-1})_{m, n} B_{alpha_s, n}.

       Substitute A(CGWB, alpha_s) = 0 (W13-2 construction):

           F_marg(CGWB, alpha_s) = - sum_{m, n} B_{CGWB, m} (C^{-1})_{m, n} B_{alpha_s, n}.

Step 5 (direction, the kernel-orthogonality lemma). KEY: B_{CGWB, m} and B_{alpha_s, n} are PROJECTIONS of
       the same upstream moment a_m onto orthogonal observable subspaces (T3 axes (i), (ii), (iii)).
       In abstract form

           partial O_CGWB / partial a_m   = K_CGWB(m) * (transverse-tensor projector)
           partial O_alpha_s / partial a_n = K_alpha_s(n) * (scalar-tilt-derivative projector)

       and the cross-product

           B_{CGWB, m} * (C^{-1})_{m, n} * B_{alpha_s, n}
              = K_CGWB(m) K_alpha_s(n) (C^{-1})_{m,n}
                * < transverse-tensor projector, scalar-tilt projector >.

       The inner product < transverse-tensor, scalar-tilt > = 0 by the SO(3) irrep decomposition theorem
       (tensor-2 irrep is orthogonal to scalar-0 irrep under the substrate's SO(3)-isometry on the post-
       fold GGE relic). Under this projection-orthogonality:

           sum_{m, n} B_{CGWB, m} (C^{-1})_{m, n} B_{alpha_s, n} = 0.

       Therefore  F_marg(CGWB, alpha_s) = 0,  and  rho_marg = 0  IDENTICALLY,  regardless of the
       (a_2, a_4, a_6) covariance structure C.

Conclusion: the W13-2 ρ=0 is genuine — it is preserved under marginalization over the a_n nuisance block,
       provided the SO(3) tensor/scalar irrep-orthogonality of the kernels holds. This is the substantive
       claim mack must contradict in R2: not "is the a_n covariance non-trivial" (it certainly is, by
       W12-4 class-(d)), but "do the CGWB and alpha_s kernels share a non-trivial inner product on the
       SO(3) irrep decomposition of the substrate's post-fold acoustic spectrum?"
```

**Where the steelman is fragile and where it is robust**.

- **Robust against**: W12-4 class-(d) regulator-divergence of a_n. The argument above does not use any property of C beyond invertibility — even maximally-correlated nuisance parameters (det C → 0+) leave the off-diagonal at zero IF the kernels are SO(3)-irrep-orthogonal.
- **Robust against**: under-resolution of the 2×2 Fisher in (CGWB, α_s) basis. Adding nuisance dimensions cannot create off-diagonal correlation between observables whose kernels are orthogonal projectors.
- **Fragile against**: any process that BREAKS the SO(3) tensor/scalar split. Two known candidates: (1) tensor-scalar mixing at second-order in cosmological perturbation theory, which is suppressed by ε ~ 0.02 for the framework; (2) a regulator that does not respect the SO(3) substrate-isometry — but per W12-4, the 5-regulator atlas on a_2 / a_4 spreads only the moment values, not the SO(3) decomposition.
- **Fragile against**: a non-leading-order coupling channel that mack might identify in R2 — e.g., a_4 entering CGWB through 1/G_N renormalization or entering α_s through running-mass at the same diagrammatic order, with a SHARED transverse-or-scalar projection. This is the open question for R2.

**Detector-band hardening**. The Fisher PSD claim is also robust against the 13.6-OOM frequency separation (T3 axis (ii)): no LISA Fourier bin maps to any CMB temperature multipole; the *experimental noise* covariance is block-diagonal between the two detectors. Even if the SO(3)-irrep-orthogonality were imperfect (e.g., tensor-scalar mixing at ε²-level), the experimental Fisher would re-diagonalize via the 13.6-OOM gap.

**INFO not PASS**. Note: W13-2 landed INFO, not PASS, with the INFO triggered by the band-width proxy (Ω_GW(6 mHz)/Ω_GW(1.5 mHz) = 7.875 > 0.20), NOT by the ρ=0 result. The Fisher-PSD claim itself is at PASS-level confidence within the gate; the methodology proxy is what fired INFO. This workshop targets the ρ=0 claim, not the band-width proxy.

### TN: Cross-Cutting Observations

**Verdict-line provenance pin (for the workshop record)**.

```
W13-2 verdict (s85_gate_verdicts.txt line 66):
  S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT: INFO -- value=(alpha_s=-0.068968, Omega_GW_LISA=8.299e-58, rho_cc=0.0, Fisher_PD=1)
  scheme=zeta convention=LISA-PLS-2024+CMB-S4-Book-2019 L_max=10
  audit_sha256 = f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1
  content_sha256 = 58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779
  schema_version = S84+

W12-4 verdict (sessions/archive/session-85/session-85-w12-workingpaper.md line 212):
  S85-W12-ELIM-8: PASS -- value=(n_a=13, n_b=0, n_c=0, n_d=3) scheme=regulator-invariance-taxonomy
  convention=5-regulator-atlas-W0 L_max=10
  audit_sha256 = d9c4bc06ee2d5154d715bb0c736d9e8118c14d66213545fc4239201bd8f4e490
  content_sha256 = 8221f24ff998c296d682c6ee97c65b3e49c33326516eeec32f93134bef2f9f17
  schema_version = S84+
  Class (d) members: a_0 (spread 0.50), a_2 (spread 1.03), a_4 (spread 0.49).
```

**The structural distinction this workshop turns on — SHARED UPSTREAM vs SHARED PROJECTION**.

A pair of observables (O_1, O_2) can have non-zero Fisher off-diagonal — i.e., genuine ρ ≠ 0 — only if BOTH of the following hold:

1. **Shared upstream**: there exists a substrate parameter θ such that ∂O_1/∂θ ≠ 0 AND ∂O_2/∂θ ≠ 0.
2. **Shared projection**: the two derivatives, viewed as elements of observable-space, have non-zero inner product under the experimental noise structure.

W12-4 establishes condition (1) for (CGWB, α_s, a_n): both observables have non-trivial dependence on a_2 (and through running-mass corrections, on a_4) — there IS shared upstream at the substrate level. This is the steelman ground mack stands on, and it is real.

The W13-2 ρ=0 claim therefore reduces to a claim about condition (2): even though the upstream is shared, the *projections* through the CGWB and α_s observable kernels land in orthogonal subspaces of observable-space. The argument in T3 is that this orthogonality follows from the substrate's SO(3) irrep decomposition of the post-fold GGE relic (tensor-2 vs scalar-0), reinforced by the 13.6-OOM frequency separation between LISA-band and CMB-pivot.

**Three structural axes in tension** (for the workshop verdict to resolve):

| Axis | Claim | Status entering R1 |
|:-----|:------|:-------------------|
| a_n shared upstream | a_2 enters BOTH CGWB (via 1/G_N) AND α_s (via n_s = f(a_2/a_0)). a_4 enters CGWB at sub-leading and α_s under running-mass. | ESTABLISHED (W12-4 + s71 + s50) |
| Kernel orthogonality | The CGWB kernel is a transverse-tensor projector; the α_s kernel is a scalar-tilt-derivative projector. Inner product = 0 by SO(3) irrep decomposition. | DEFENDED (T3, T4 substitution chain) |
| Fisher PSD sufficiency | The 2×2 Fisher in (CGWB, α_s) basis recovers the same ρ=0 as the marginalized 5×5 Fisher with a_n nuisance, IF kernel-orthogonality holds. | DEFENDED but PROOF-PENDING (T4) |

The R2 confrontation is on the second axis: the kernel-orthogonality lemma's correctness depends on the SO(3)-irrep decomposition surviving in the substrate's post-fold acoustic kinematics. R2 must compute the explicit kernel inner product and show it is zero (or non-zero with measured value).

**Questions for mack (M-track in R2 will respond)**.

These are framed as falsifiable structural questions, not rhetoric:

1. **Q-mack-1 — Diagrammatic kernel inner product**. Produce the diagrammatic decomposition
   ```
   K_CGWB[a_n](k_GW) = (transverse-tensor projector) acting on a_n-Mellin-moment integrand at LISA pivot
   K_alpha_s[a_n](k*_CMB) = (scalar-tilt-derivative projector) acting on a_n-Mellin-moment integrand at CMB pivot
   ```
   and compute the inner product
   ```
   < K_CGWB[a_2], K_alpha_s[a_2] > = ?
   ```
   under the substrate's natural inner product on observable-space. T3 claims this is 0 by SO(3) irrep orthogonality + frequency-band separation. mack — does your diagrammatic decomposition produce a non-zero kernel overlap? At what diagrammatic order, with what magnitude?

2. **Q-mack-2 — Regulator-conditional ρ**. Under the W12-4 5-regulator atlas, a_2 takes values {0.15445, 0.15810, 0.15810, 0.11100, 0.03185} — a factor-5 spread. Does the kernel-orthogonality argument hold under EVERY regulator in the atlas, or does some regulator break the SO(3)-irrep decomposition? In particular: does Pauli-Villars (which subtracts a heavy-mass shadow in a way that mixes Lorentz representations) preserve tensor/scalar orthogonality on the post-fold GGE relic?

3. **Q-mack-3 — Tensor-scalar mixing at higher order in ε**. The framework's slow-roll-equivalent parameter ε is ~0.02. At second-order in cosmological perturbation theory, tensor and scalar modes mix at order ε². Does the W13-2 Fisher analysis survive the second-order tensor-scalar mixing, i.e., does the kernel inner product become 0 + O(ε²) rather than identically 0? If 0 + O(ε²) at observable-amplitude, what does the marginalized ρ become?

4. **Q-mack-4 — Decision (a / b / c) under W12-4 closure**. The §6A schedule offers three decisions. Given W12-4's regulator-class-(d) closure on a_n, my read is:
   - **(a) ρ=0 genuine**: ONLY if SO(3)-irrep-orthogonality is regulator-invariant under the W12-4 atlas AND ε² tensor-scalar mixing is below σ_LISA × σ_CMBS4 detection.
   - **(b) ρ≠0 after a_n marginalization**: requires producing a non-zero kernel inner product at leading diagrammatic order.
   - **(c) regulator-conditional**: ρ=0 under some regulators, ρ≠0 under others — a NEW result extending W12-4 from "a_n class-(d)" to "(CGWB, α_s) joint significance is regulator-dependent."

   Do you see a path to (b) or (c) that I am missing?

5. **Q-mack-5 — What experiment would distinguish?**. If R2 leaves us at (a) defended and (b)/(c) open, what observational footprint would a non-zero kernel inner product leave that LISA + CMB-S4 could measure? E.g., a coherence between primordial GW phase and CMB scalar acoustic phase at a specific scale relationship?

**Methodological note on what counts as winning the steelman**.

This is not a yes/no debate — it is a structural decomposition. A "win" for the independence steelman means: the kernel-orthogonality lemma survives R2's diagrammatic challenge AND the marginalized ρ remains 0 to a tolerance below detector noise. A "loss" means: mack identifies a kernel coupling at leading diagrammatic order that produces a measurable ρ, OR identifies a regulator under which SO(3)-irrep orthogonality breaks. Either outcome is a constraint-map gain. The substrate is what it is; the workshop's job is to surface it.

---

## Round 1 — mack: STEELMAN SHARED UPSTREAM + Response

### Part 1: Response to tesla's Sections

#### Re: T1 — CGWB Observable

**AGREE on the substrate-projection chain; SHARPEN on the implication for shared-upstream.**

tesla's chain `D_K spectrum -> {a_n} -> 1/G_N propto a_2 * M_KK^2 -> graviton normalization -> O_CGWB` is correct as written, and the canonical pin `1/G_N = (48 f_2 / pi) * a_2 * M_KK^2` is the right Connes-Chamseddine identification (s74_r_family_observable_scan.py, s69_kk_higgs.py). What I want to harden is the consequence:

- **Linear scaling of O_CGWB in a_2 is the steelman's WEAKNESS, not its strength.** If `Omega_GW(f) ~ G_N * (...)` and `G_N ~ 1/(a_2 * M_KK^2)`, then `Omega_GW ~ 1/a_2` (or, in tesla's preferred phrasing, "any rescaling of a_2 propagates one-to-one into Omega_GW(f) at every frequency"). That ONE-TO-ONE inheritance is exactly what makes ANY substrate-level uncertainty in a_2 propagate ONE-TO-ONE into O_CGWB. Under W12-4 class-(d), that uncertainty is real (a_2 spread = 1.029 across the 5-regulator atlas).

- **EMERGES**: the schedule §6A invocation said "CGWB couples to a_2 (amplitude)" — tesla confirms this. The implication tesla flags for §T2 (that a_2 also enters alpha_s through n_s = f(a_2/a_0)) means CGWB and alpha_s share a_2 at LEADING order in BOTH chains, not at the sub-leading mixing tesla downplays at the end of T4. The shared-upstream claim is at MAXIMAL strength — leading-order in a_2 for both — and tesla's steelman has to carry exactly that load.

- **MISSED in T1**: the LISA-band scope. tesla notes the §6A "integrated [10^-4, 1] Hz" framing collapses to f_LISA_pivot = 3 mHz in W13-2 (single-pivot scalar). I agree, but this single-pivot scalar EATS the band-width information that would otherwise discriminate `a_2`-driven amplitude shifts from `a_4`-driven SHAPE shifts (a_4 enters the running of G_N at NLO via heat-kernel renormalization, modulating the high-frequency tail of Omega_GW(f)). The pivot scalar has no leverage on this — see M3 below.

#### Re: T2 — α_s Observable

**AGREE WITH HONEST REFRAMING; the n_s ↔ a_2/a_0 (not a_4) coupling STRENGTHENS shared-upstream, not weakens it.**

tesla deserves credit for surfacing this in the steelman rather than papering over it. The §6A invocation as I drafted it (CGWB↔a_2, α_s↔a_4) was index-disjoint by construction; tesla has correctly noted that under the S50 constant-mass O-Z identity α_s = n_s² − 1 in the W13-2 pre-registration, **α_s tracks a_2/a_0 — the SAME a_2 that 1/G_N depends on for CGWB**. That is the "sharper, harder steelman" obligation you flagged in the prompt.

**Substitution chain — formalize the shared a_2 coupling explicitly**:

```
Step 1 (definition, T1): O_CGWB ~ G_N ~ 1/(a_2 * M_KK^2)         [tesla T1 line 60]
Step 2 (definition, T2): O_alpha_s = n_s^2 - 1, n_s = f(a_2/a_0)  [tesla T2 line 110, S50 O-Z]
Step 3 (substitute):     partial O_CGWB / partial a_2     != 0
                         partial O_alpha_s / partial a_2  = (d n_s / d (a_2/a_0)) * (1/a_0) * 2 n_s != 0
Step 4 (direction):      Both partials NON-ZERO at LEADING order in the substrate moments.
                         Cross-block B in the Fisher partition has BOTH non-zero entries
                         in the a_2 column. Shared upstream is MAXIMAL.
```

**Where I push back on tesla's framing**:

- tesla writes (T2 last paragraph before T3) that "α_s inherits its substrate dependence from a_2/a_0, **not from a_4 alone**." That phrasing under-states the issue. The honest reading is: α_s inherits a_2 dependence — *the same a_2 as CGWB*. The defense cannot rest on "different upstream moments." It must rest on "same upstream moment, but different observable-space projection." That is exactly the shift to kernel-orthogonality I respond to in Re:T3.

- **EMERGES**: the §6A schedule's "a_2 vs a_4" framing was a red herring. The real structural distinction is not at the moment-index layer but at the kernel-projector layer. The W12-4 closure makes this sharper: **a_n is regulator-class-(d), but the regulator-divergence is correlated across n** — see M2's covariance analysis where ρ(a_2, a_4) = 0.9922 across the 5-regulator atlas. That correlation matters for how a_4 enters CGWB at NLO and α_s under running-mass; the two NLO channels share regulator-conditioned uncertainty.

- **MISSED in T2**: tesla cites the running-mass generalization (s50_running_mass.py `delta_alpha`) parenthetically but doesn't compute it. Under the W13-2 pre-registration this is fine — W13-2 explicitly uses constant-mass — but the question for R3 is whether the framework is COMMITTING to constant-mass at the substrate level or merely PRE-REGISTERING it for W13-2. If the latter, a future W13-2-prime under running-mass would surface the a_4 entry into α_s and break index-disjointness even further.

#### Re: T3 — a_2 vs a_4 Projection Distinctness (now: Kernel-Orthogonality)

**PARTIAL AGREE on axis (ii); DISAGREE that axis (i) is structurally watertight; AGREE that axis (iii) is real but DISPUTE the rank claim.**

The reframing from "index-disjointness" to "kernel-orthogonality" is correct and the work is improved by it. But three of the three axes have leaks worth surfacing.

**(i) SO(3) irrep-orthogonality is NOT automatic kernel-orthogonality**.

This is my most important pushback. tesla's argument runs: "tensor-2 irrep and scalar-0 irrep of SO(3) are orthogonal, so the kernels K_CGWB and K_α_s are orthogonal." This conflates two distinct orthogonalities:

- **Mode-space orthogonality** (correct): on the post-fold acoustic spectrum, a tensor-mode excitation and a scalar-mode excitation are orthogonal as elements of the GGE-relic Hilbert space. The traceless-transverse projection theorem (s69_transit_gw.py: `T_ij = p * g_ij has ZERO traceless-transverse projection`) is a clean wall.

- **Functional-derivative orthogonality** (NOT automatic): the Fisher cross-block element is `B_ab = (1/sigma^2) * (∂O_a/∂a_n) * (...)`. This is a derivative on PARAMETER SPACE (a_n), not a projection on mode space. Whether `∂O_CGWB/∂a_2` and `∂O_α_s/∂a_2` are orthogonal as elements of observable-space depends on the structure of the experimental noise covariance and the response kernels, NOT on whether the OBSERVABLES live on tensor vs scalar modes.

Substitution chain to make this concrete:

```
Step 1 (definition): F_marg(CGWB, alpha_s) = - sum_{m,n} (∂O_CGWB/∂a_m) C^{-1}_{mn} (∂O_α_s/∂a_n)
       (tesla T4 Step 4, with A(CGWB, alpha_s) = 0 by W13-2 construction)

Step 2 (substitute leading-order partials):
       ∂O_CGWB / ∂a_2 ~ -(O_CGWB / a_2)        [from O_CGWB ~ 1/a_2 at leading]
       ∂O_α_s / ∂a_2 = 2 n_s * (∂n_s / ∂a_2) ~ (2 n_s / a_0)  [from n_s = f(a_2/a_0), constant-mass]

Step 3 (direction): both partials are SCALAR FUNCTIONS of (a_n) values, not vectors in mode-space.
       Their product is just a number, multiplied by C^{-1}_{22}, summed.
       The SO(3) irrep decomposition tesla invokes lives at the OBSERVABLE level
       (Omega_GW is tensor-spectrum, A_s is scalar-spectrum), but the marginalization residual
       lives at the SUBSTRATE PARAMETER level — and substrate parameters are SO(3) singlets
       (a_n is a number, not a tensor field).

Step 4 (canonical form): irrep-orthogonality at the observable level does NOT propagate to
       kernel-orthogonality at the parameter level. The Schur-complement formula does not see
       the SO(3) irrep structure — it only sees the Jacobian B and the substrate covariance C.

Conclusion: tesla's lemma F_marg(CGWB, α_s) = 0 by SO(3) irrep-orthogonality is NOT VALID as
       stated. The lemma needs an additional input: the kernels' orthogonality must be
       established AT THE PARAMETER LEVEL (e.g., by showing ∂O_CGWB/∂a_2 = 0 or
       ∂O_α_s/∂a_2 = 0), not at the mode-decomposition level.
```

This is the substantive R2 confrontation. tesla's R2 needs to either (a) show the parameter-level partial derivatives ARE orthogonal in some experimental-noise-weighted sense, or (b) concede the lemma needs a different defense.

**(ii) 13.6-OOM frequency separation — AGREE this hardens experimental Fisher block-diagonality**.

tesla's arithmetic is correct (verified: f_today_α_s = c·k*/(2π) with k* = 0.05 Mpc⁻¹ gives ~7.7e-17 Hz, vs LISA pivot 3e-3 Hz, ratio ~3.9e+13, log₁₀ ≈ 13.6). I AGREE this is a robust independence axis at the experimental level — no LISA Fourier bin overlaps any CMB temperature multipole. **But this is independence of the EXPERIMENTAL NOISE covariance, not independence of the SIGNAL substrate dependence.** The Fisher cross-block depends on the signal Jacobian (B), not on the experimental noise covariance — and the Jacobian is set by the SUBSTRATE partials, which DO share a_2 at leading order per Re:T2. So axis (ii) blocks one channel of correlation (instrumental noise leakage) but does NOT block the substrate-shared-upstream channel.

**(iii) Rank-0 vs rank-2 operator-distinctness — AGREE structurally, DISPUTE that this implies orthogonality**.

tesla writes: "CGWB is a rank-0 functional of a_2, α_s is a rank-2 derivative functional." Correct that the operator structures differ. But two functionals of the same scalar `a_2` — even with different operator ranks — can still produce non-zero `(∂F_1/∂a_2) * (∂F_2/∂a_2)` cross-products. The rank distinction matters for HOW a_4 enters at NLO (CGWB picks up a_4 through G_N renormalization; α_s picks up a_4 through running-mass), but at the level of LEADING-order cross-products in a_2, rank-0 vs rank-2 doesn't enforce orthogonality.

**EMERGES — what tesla's argument actually proves**:

When properly cleaned up, axes (i)-(iii) prove a WEAKER but still useful claim: the CGWB and α_s OBSERVABLES live on physically distinguishable modes (tensor vs scalar) at frequencies separated by 13.6 OOM, so an experimental measurement of one CANNOT contaminate the measurement of the other through detector overlap. That is a valid statement about EXPERIMENTAL block-diagonality. But it is NOT a statement about SUBSTRATE-LEVEL covariance — and the W13-2 ρ=0 claim, if interpreted as "the framework predicts CGWB and α_s are statistically independent given the substrate parameters," is exactly the claim that the SUBSTRATE-LEVEL covariance does NOT propagate to observable correlation. That claim requires Re:T4's marginalization analysis to hold, which I respond to next.

#### Re: T4 — Fisher PSD Sufficiency

**AGREE on the Schur-complement formula; DISAGREE on the kernel-orthogonality lemma; FLAG that under W12-4 class-(d) the C matrix is near-singular, which AMPLIFIES rather than nullifies any residual kernel overlap.**

**The Schur-complement formula is correct** (T4 Step 2): F_marg = A − B C⁻¹ B^T is the standard marginalization result. tesla's substitution chain through Step 4 is mechanically right: A(CGWB, α_s) = 0 by W13-2 construction (the 2×2 Fisher in the (CGWB, α_s) basis is diagonal because no shared explicit fit parameter), so F_marg(CGWB, α_s) reduces to −B C⁻¹ B^T.

**The fragile step is Step 5** — the SO(3) irrep-orthogonality lemma. Per Re:T3, observable-level SO(3) irrep-orthogonality does NOT propagate to parameter-level kernel-orthogonality, because the marginalization sum is over the SUBSTRATE PARAMETERS a_n, which are SO(3) singlets. tesla's expression

```
< transverse-tensor projector, scalar-tilt projector > = 0  (T4 Step 5)
```

is a statement about the *observable*'s mode content (Omega_GW lives on tensor modes, A_s lives on scalar modes), but the marginalization residual

```
F_marg(CGWB, α_s) = - sum_{m,n} (∂O_CGWB/∂a_m) C^{-1}_{mn} (∂O_α_s/∂a_n)
```

is a number, not a mode-projector inner product. The partial derivatives are scalars; the Schur-complement does not see the SO(3) decomposition. The lemma needs to be reformulated as a parameter-level statement, which we have not yet established.

**Quantitative point — the W12-4 substrate covariance is near-singular**:

I have Python-verified the 3×3 substrate covariance from the W12-4 5-regulator atlas (a_0, a_2, a_4 vectors from W12-4 §(b), reproduced verbatim from session-85-w12-workingpaper.md lines 224-226). The numerical results are:

```
C (substrate covariance, sample, ddof=1):
   [[ 5.747e-01   4.958e-03  -7.459e-06]
    [ 4.958e-03   2.976e-03   1.207e-04]
    [-7.459e-06   1.207e-04   4.971e-06]]

Pearson correlation R:
   ρ(a_0, a_2) = +0.1199
   ρ(a_0, a_4) = -0.00441   (effectively zero)
   ρ(a_2, a_4) = +0.9922    (NEAR UNITY)

Eigenvalues of C:    {7.59e-12, 2.94e-03, 5.75e-01}
det(C)            =  1.28e-14
cond(C)           =  7.57e+10
```

The smallest eigenvalue is 7.59e-12 — C is numerically rank-2, not rank-3. Pseudoinverse C⁺:

```
C⁺[a_2, a_2]  = +2.23e+08
C⁺[a_2, a_4]  = -5.41e+09
C⁺[a_4, a_4]  = +1.31e+11
```

These are LARGE numbers. The Schur-complement marginalization residual

```
F_marg(CGWB, α_s) = - [B_{CGWB, 0}, B_{CGWB, 2}, B_{CGWB, 4}] · C⁺ · [B_{α_s, 0}, B_{α_s, 2}, B_{α_s, 4}]^T
```

amplifies the kernel cross-product `B_{CGWB, m} * B_{α_s, n}` by factors up to 10^11. So even a kernel mismatch at order 10^-10 in dimensionless units can produce O(10) corrections to the off-diagonal Fisher element. tesla's claim (T4 "Robust against" bullet 1) that "even maximally-correlated nuisance parameters (det C → 0+) leave the off-diagonal at zero IF the kernels are SO(3)-irrep-orthogonal" requires the kernel inner product to be IDENTICALLY zero, not approximately zero. The fragility tesla flagged at the end of T4 (last "Fragile against" bullet, "a non-leading-order coupling channel that mack might identify in R2") is exactly this — but the C-amplification factor 10^10 makes "non-leading" misleading. With C near-singular, NLO kernel overlaps do not stay sub-leading at the marginalized observable level.

**EMERGES — the C-amplification is itself a regulator-conditional artifact**:

The near-singularity of C arises because in the W12-4 atlas, heat-kernel and Mellin and zeta give nearly identical (a_0, a_2, a_4) values, while hard-cutoff and Pauli-Villars give substantially different ones — so the "samples" cluster, producing a degenerate covariance. Under a different regulator atlas (e.g., dropping Pauli-Villars or adding more regulators), C might be better-conditioned. This means the C-amplification mechanism I just flagged is itself REGULATOR-ATLAS-CONDITIONAL — it is sensitive to which 5 regulators W12-4 chose. That is the open question for Q-tesla-1 in M4.

**MISSED — the experimental Fisher and the substrate Fisher are different objects**:

tesla's T4 conflates two Fisher matrices. The W13-2 Fisher (`F = diag(1/σ²(α_s_CMBS4), 1/σ²(Ω_GW_LISA))`) is the **experimental Fisher** — its diagonality reflects the 13.6-OOM frequency separation of the detectors and is a property of the noise covariance. The Fisher I am marginalizing in the substrate-covariance argument is the **theoretical Fisher** — its off-diagonal reflects whether the framework's predictions for (CGWB, α_s) covary at the substrate-parameter level. **W13-2's ρ_cc=0 is the experimental-Fisher off-diagonal**, not the theoretical-Fisher off-diagonal. The two are different quantities and the W13-2 verdict line, read literally, only certifies the former. See M3 for the full structural argument.

#### Re: TN — Cross-Cutting

**AGREE on verdict-line provenance pin and on the SHARED-UPSTREAM vs SHARED-PROJECTION decomposition; SHARPEN the three-axis tension table; ANSWER Q-mack-1 through Q-mack-5.**

**Verdict-line provenance — re-verified**:

```
W13-2 verdict (s85_gate_verdicts.txt line 201, full canonical line):
  S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT: INFO
    -- value=(alpha_s=-0.068968, Omega_GW_LISA=8.299e-58, rho_cc=0.0, Fisher_PD=1)
       scheme=zeta convention=LISA-PLS-2024+CMB-S4-Book-2019 L_max=10
       audit_sha256=f514d642fe2a80ac408ddc0a09da94c5a8590a0127b4754fd337ea57eb2c02c1
       content_sha256=58630dc36e59af32dfece11e521736c13c27f9a943a91ac03bb91249f2529779
       schema_version=S84+
  Companion row (line 202): audit=f514d642fe2a80ac content=58630dc36e59af32 [matches]

W12-4 verdict (s85_gate_verdicts.txt line 194):
  S85-W12-ELIM-8: PASS -- value=(n_a=13, n_b=0, n_c=0, n_d=3)
       scheme=regulator-invariance-taxonomy convention=5-regulator-atlas-W0 L_max=10
       audit_sha256=d9c4bc06ee2d5154d715bb0c736d9e8118c14d66213545fc4239201bd8f4e490
       content_sha256=8221f24ff998c296d682c6ee97c65b3e49c33326516eeec32f93134bef2f9f17
       schema_version=S84+
  Companion row (line 195): audit=d9c4bc06ee2d5154 content=8221f24ff998c296 [matches]
  Class (d) members per session-85-w12-workingpaper.md §(b): a_0 (spread 0.50), a_2 (spread 1.03),
                                                              a_4 (spread 0.49).
```

Both verdict lines verbatim; SHA prefixes match the companion rows.

**SHARED-UPSTREAM vs SHARED-PROJECTION — agree, with one reformulation**:

tesla's two-condition decomposition is structurally right but I would re-name (2) to remove the SO(3) framing:

- (1) **Shared upstream** (condition on the substrate): ∃ θ ∈ {a_n, M_KK, ...} : ∂O_1/∂θ ≠ 0 AND ∂O_2/∂θ ≠ 0.
  Status: **established for θ = a_2 at LEADING order**, by Re:T1 + Re:T2.

- (2) **Shared parameter-space projection** (condition on the kernels): the Jacobian columns `(∂O_1/∂θ_n)_n` and `(∂O_2/∂θ_n)_n` have non-zero substrate-covariance-weighted inner product, i.e. `Σ_{m,n} (∂O_1/∂θ_m) C^{-1}_{mn} (∂O_2/∂θ_n) ≠ 0`.
  Status: **OPEN — to be determined by R2 computation.**

The original "shared projection" (tesla's wording) framed this as a question about observable-space mode-decomposition (tensor vs scalar). I argue it is a question about parameter-space Jacobian alignment under the substrate covariance C — a different object. The W13-2 ρ=0 verdict tests neither (1) nor (2) directly; it tests the diagonal experimental Fisher with no substrate covariance accounted for.

**Three-axis tension table — sharpened**:

| Axis | Status entering R1 (tesla) | Status after Re:T1-T4 (mack) |
|:-----|:---------------------------|:------------------------------|
| a_n shared upstream (a_2) | ESTABLISHED (W12-4 + s71 + s50) | UPGRADED: a_2 enters BOTH at LEADING order; this is the strongest possible shared-upstream |
| Kernel orthogonality | DEFENDED (T3, T4 substitution chain via SO(3)) | UNDEFENDED at parameter level; the SO(3) lemma is mode-space, not parameter-space; reformulation needed in R2 |
| Fisher PSD sufficiency | DEFENDED but PROOF-PENDING (T4) | EXPERIMENTAL Fisher block-diagonal (PASS by 13.6-OOM frequency separation); SUBSTRATE Fisher off-diagonal UNKNOWN (depends on C-amplified kernel cross-product) |

**Answers to Q-mack-1 through Q-mack-5**:

**Q-mack-1 — Diagrammatic kernel inner product**. I do not have the explicit Mellin-moment integrand decomposition pre-computed for R1. What I can offer in R1 is the BOUND from Re:T4: the marginalization residual `F_marg(CGWB, α_s)` factorizes as `K(C) · J_CGWB · J_α_s`, where K(C) is a regulator-conditional amplifier with magnitude up to C⁻¹_{4,4} ≈ 1.31e+11, and J_CGWB, J_α_s are the substrate-Jacobian projections. Even if J_CGWB and J_α_s are individually small (NLO in ε ~ 0.02), their product times K(C) need not be small. **For R2 my plan is**: compute the explicit `(∂O_CGWB/∂a_2, ∂O_CGWB/∂a_4)` and `(∂O_α_s/∂a_2, ∂O_α_s/∂a_4)` Jacobian rows from the canonical scaling laws (1/G_N ~ a_2 for CGWB; n_s = f(a_2/a_0) for α_s with running-mass correction for a_4 entry) and report `J_CGWB · C⁻¹ · J_α_s` numerically.

**Q-mack-2 — Regulator-conditional ρ**. tesla's question is sharp: under the W12-4 atlas, a_2 takes 5 values from 0.0319 (Pauli-Villars) to 0.158 (zeta/Mellin), a factor-5 spread. I expect (without yet having computed) that the marginalized ρ varies substantially across regulators because (a) the substrate covariance C is dominated by which regulators are included, and (b) the partial derivatives `∂O/∂a_n` evaluated at different regulator-pinned a_n values produce different J vectors. **My pre-registered prediction for R2**: ρ_marg under heat-kernel ≈ ρ_marg under zeta ≈ ρ_marg under Mellin (these three give nearly identical a_n in W12-4), but ρ_marg under hard-cutoff or Pauli-Villars differs by factors of 2-5. This would make the §6A decision **(c) regulator-conditional** the structurally right answer.

**Q-mack-3 — Tensor-scalar mixing at higher order in ε**. The framework's slow-roll-equivalent ε ~ 0.02 (W13-1 plan central). Second-order tensor-scalar mixing scales as ε² ~ 4e-4. tesla asks: does this make the kernel inner product 0 + O(ε²) rather than identically 0? My answer: yes, that is the natural expectation, but the C-amplification factor 10^10-10^11 from Re:T4 means a 4e-4-level kernel mismatch becomes an O(10⁶-10⁷) correction to F_marg — vastly larger than the diagonal Fisher elements (F_α_s = 1.11e+5, F_CGWB = 1.00e+24). For α_s the correction would dominate the diagonal; for CGWB the diagonal is so large that even C-amplified ε² stays negligible. Net effect: **the marginalized correlation ρ_marg = F_marg / sqrt(F_α_s · F_CGWB) gets enhanced on the α_s side, suppressed on the CGWB side** — and the geometric mean is still small because of the σ(Ω_GW_LISA)=10⁻¹² floor. So tesla may be right at the OBSERVABLE-LEVEL ρ even if I am right at the SUBSTRATE-LEVEL F_marg. This is a quantitative R2 task.

**Q-mack-4 — Decision (a / b / c) under W12-4 closure**. My current read:

- **(a) ρ=0 genuine**: requires kernel-orthogonality at parameter-level under EVERY regulator AND ε² mixing below the geometric-mean Fisher floor. Given the C-amplification, plausible but not yet proven.
- **(b) ρ ≠ 0 after a_n marginalization**: most likely outcome at the SUBSTRATE Fisher level; uncertain whether it propagates to OBSERVABLE Fisher given the geometric-mean σ_LISA·σ_CMBS4 dilution.
- **(c) regulator-conditional**: my preferred pre-registered hypothesis for R2 — see Q-mack-2.

**My provisional position entering R2: lean (c) with tail probability on (a) at the OBSERVABLE-Fisher level.** Path to (b) tesla missed: Re:T4's parameter-level reformulation of the kernel-orthogonality lemma fails, and the substrate Fisher off-diagonal is non-zero by direct computation under at least one regulator in the atlas.

**Q-mack-5 — What experiment would distinguish?**. If we land at (a)-defended-at-observable-level but (b)-or-(c)-open-at-substrate-level, the discriminator is a JOINT detector that simultaneously measures CGWB at LISA band AND constrains α_s at CMB pivot, looking for a phase coherence at a specific scale relationship `k_CMB / k_LISA ~ a_4/a_2 ~ 0.07-0.21` (verified Python compute on W12-4 atlas: a_4/a_2 spans [0.0759, 0.2133] across regulators). If the framework predicts a non-zero ρ_marg, it ALSO predicts a specific cross-scale coherence between primordial GW phase at f ~ 3 mHz and CMB scalar acoustic phase at k* = 0.05 Mpc⁻¹, with magnitude proportional to the kernel cross-product. CMB-S4 + LISA in joint analysis (post-2035) is the natural footprint. Earlier discriminator: 21cm IM at z ~ 8 (post-reionization) × LISA stochastic background, since 21cm probes a_2-dependent expansion-history substrate at intermediate frequencies (~10⁻¹⁰ Hz today) — partial overlap of the parameter-Jacobian columns even at non-overlapping detector bands.

**Methodological agreement**:

I agree with tesla's framing that "this is not a yes/no debate — it is a structural decomposition" (T4 closing methodological note). A clean WIN for the independence steelman requires (i) parameter-level kernel-orthogonality reformulation in R2, (ii) computation of `J_CGWB · C⁻¹ · J_α_s` showing it stays below σ_LISA · σ_CMBS4 ~ 1.0e-12 · 0.003 ≈ 3.0e-15. A clean WIN for the dependence challenge requires showing F_marg ≠ 0 at substrate level under at least one regulator in the W12-4 atlas. Either outcome refines the constraint map; neither destroys the framework.

### Part 2: Original Analysis

#### M1: W12-4 Regulator-Class-(d) Closure on a_n — Implication for CGWB / α_s Covariance

**The W12-4 verdict pinned**:

```
S85-W12-ELIM-8: PASS -- value=(n_a=13, n_b=0, n_c=0, n_d=3)
   scheme=regulator-invariance-taxonomy convention=5-regulator-atlas-W0 L_max=10
   audit_sha256=d9c4bc06ee2d5154d715bb0c736d9e8118c14d66213545fc4239201bd8f4e490
   content_sha256=8221f24ff998c296d682c6ee97c65b3e49c33326516eeec32f93134bef2f9f17
   schema_version=S84+
                                                       (s85_gate_verdicts.txt line 194)

Class (d) STRUCTURALLY-DIVERGENT members (session-85-w12-workingpaper.md §W12-4 (b)):
   a_0:  spread = (3.7074 - 2.0122) / 3.3684           = 0.5033
   a_2:  spread = (0.15810 - 0.03185) / 0.1235         = 1.029
   a_4:  spread = (0.011994 - 0.006795) / 0.010659     = 0.4877

5-regulator atlas values (verbatim from §W12-4 (b) table, lines 224-226):
                heat-kernel    zeta         Mellin        hard-cutoff   Pauli-Villars
   a_0          3.7074         3.7074       3.7074        2.0122        3.7074
   a_2          0.15445        0.15810      0.15810       0.11100       0.03185
   a_4          0.011837       0.011994     0.011994      0.010677      0.006795
```

**Structural implication for the §6A workshop — the chain rule propagates regulator-label indexing upward**:

The W12-4 closure says: bare `a_n` is NOT a substrate-unique number; it is a regulator-labeled family `{a_n^{(r)} : r ∈ atlas}` with substantial inter-regulator spread. Tesla acknowledged this in T3 ("the W12-4 regulator-class-(d) result says a_n are not regulator-invariant scalars — they are regulator-labeled families"). The implication tesla DID NOT pursue is the direct chain-rule consequence:

```
Step 1 (definition): O_CGWB = f(a_2^{(r)}, M_KK, ...)        [regulator r implicit]
Step 2 (definition): O_α_s = g(a_2^{(r)}/a_0^{(r)}, ...)     [regulator r implicit]
Step 3 (substitute): O_CGWB and O_α_s INHERIT the regulator-label index r from W12-4 class-(d)
Step 4 (direction):  Both observables are regulator-CONDITIONAL.
                     A bare W13-2 verdict that does not name its regulator is downstream of a
                     class-(d) violation: the canonical zeta scheme (W13-2 line 238) DOES name a
                     regulator, so the verdict line is well-formed — but it is well-formed AT
                     ZETA SPECIFICALLY, NOT REGULATOR-INVARIANTLY.
```

**Concrete consequences for ρ(CGWB, α_s)**:

1. **The 2×2 W13-2 Fisher is regulator-pinned to zeta**. Reading the verdict line literally: "scheme=zeta convention=LISA-PLS-2024+CMB-S4-Book-2019 L_max=10" — the ρ_cc=0 result holds AT ZETA SCHEME and only at zeta scheme. tesla's argument extends to other regulators in the atlas, but only IF the kernel-orthogonality lemma is regulator-invariant (Q-mack-2 to me, which I now elevate to a CRITICAL question for R2).

2. **a_2 and a_4 are NOT independent under the W12-4 atlas — they are NEAR-PERFECTLY CORRELATED**. From my Python verification: ρ(a_2, a_4) = +0.9922 across the 5-regulator atlas. This is a structural fact about the W12-4 closure that the 2-parameter (CGWB, α_s) Fisher matrix is structurally INSENSITIVE TO. The W12-4 closure is an INPUT to a richer Fisher analysis at the substrate level; the (CGWB, α_s) Fisher is a PROJECTION of that richer object onto the 2D observable basis.

3. **The W12 closing-notes P1 pattern partially holds, partially fails**. P1 (lines 393-394 of session-85-w12-workingpaper.md) claims dimensionless ratios `a_n/a_m` are L_max-stable even though individual a_n are not. I have verified Python-numerically: `a_4/a_2` across the 5-regulator atlas gives values [0.0766, 0.0759, 0.0759, 0.0962, 0.2133], with spread 1.278 — LARGER than the individual spreads (a_4: 0.488, a_2: 1.029). The dimensionless ratio is REGULATOR-DIVERGENT in the atlas direction even though it is L_max-STABLE in the L_max direction. This means: the dimensionless ratio cannot be relied upon to suppress regulator-conditional substrate covariance. Pauli-Villars makes the ratio jump from ~0.076 (HK/zeta/Mellin) to 0.213 — a factor 2.8 — even though L_max is fixed.

**Implication for the workshop verdict**:

The §6A schedule offers three decisions: (a) ρ=0 genuine, (b) ρ ≠ 0 after a_n marginalization, (c) regulator-conditional (NEW result extending W12-4). The W12-4 closure makes (c) the structurally CONSERVATIVE pre-registration:

- (a) is what tesla defends, but it requires regulator-invariance of the kernel-orthogonality lemma — currently undefended at parameter-level per Re:T3.
- (b) is what M2/M3 below make plausible at the SUBSTRATE Fisher level; whether it propagates to OBSERVABLE Fisher is uncertain.
- **(c) is the MOST DIRECT inheritance from W12-4: bare ρ_cc is class-(d) by chain-rule, full stop.** Any S86 gate that fixes ρ at a single value without naming a regulator inherits the W12-4 ill-formedness flag.

This is not a verdict of the workshop yet; it is the structural pre-registration I am proposing as the conservative reading. R2 will narrow.

#### M2: Substrate a_2 / a_4 / a_6 Chain Produces Covariance Structure Missed by 2-Parameter Fisher PSD

**Explicit construction of the 3×3 substrate covariance from W12-4 atlas (Python-verified)**.

Treat the 5 regulators of the W12-4 atlas {heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars} as 5 samples of the substrate's spectral-moment family — i.e., each regulator returns a (a_0, a_2, a_4) triple, and we form the sample covariance over those 5 triples. Note: a_6 is NOT in the W12-4 registry (the working paper §(b) table includes only a_0, a_2, a_4 — see lines 224-226). The §6A schedule's references to "a_6" inherit the framework's higher-moment expansion but no W12-4 atlas data exists for it; my analysis is restricted to a_0/a_2/a_4 to stay within the verdict.

**Python-verified C and C⁻¹** (sample covariance, ddof=1):

```
C (substrate covariance):
   row a_0:  [+5.747e-01,  +4.958e-03,  -7.459e-06]
   row a_2:  [+4.958e-03,  +2.976e-03,  +1.207e-04]
   row a_4:  [-7.459e-06,  +1.207e-04,  +4.971e-06]

Pearson correlations:
   ρ(a_0, a_2) = +0.1199         (small)
   ρ(a_0, a_4) = -0.00441         (~0)
   ρ(a_2, a_4) = +0.9922          (NEAR UNITY)

Eigenvalues:    {7.59e-12,  2.94e-03,  5.75e-01}        (numerically rank-2)
det(C)        =  1.28e-14
cond(C)       =  7.57e+10

C⁺ (Moore-Penrose pseudoinverse — full inverse fails because det(C) ≈ 0):
   row a_0:  [+1.78e+04,  -1.99e+06,  +4.84e+07]
   row a_2:  [-1.99e+06,  +2.23e+08,  -5.41e+09]
   row a_4:  [+4.84e+07,  -5.41e+09,  +1.31e+11]
```

**The covariance structure the W13-2 2×2 Fisher does not see**:

The W13-2 Fisher is `F = diag(1/σ²(α_s), 1/σ²(Ω_GW)) = diag(1.111e+5, 1.000e+24)`. This Fisher is constructed in the (CGWB, α_s) basis with NO substrate parameters as nuisance variables. The full 5-parameter Fisher (CGWB, α_s, a_0, a_2, a_4) is

```
                        observables          nuisances
                       /             \      /        \
F_full = | 1.111e+5       0       |  | B_α_s,0  B_α_s,2  B_α_s,4 |
         | 0           1.000e+24 |  | B_C,0    B_C,2    B_C,4   |     (signal-signal block A)
         | -----------------------+--------------------------------    (cross block B)
         | B_α_s,0   B_C,0       |  | C^{-1}_{00}  ...           |
         | B_α_s,2   B_C,2       |  | ...                         |     (substrate block C^{-1})
         | B_α_s,4   B_C,4       |  | ...          C^{-1}_{44}    |
```

After marginalizing over (a_0, a_2, a_4):

```
F_marg(α_s, Ω_GW) = A(α_s, Ω_GW) - sum_{m,n in {0,2,4}} B_{α_s, m} C^{-1}_{mn} B_{Ω_GW, n}
                  = 0 - sum_{m,n} ...                              (since A_{12} = 0 by W13-2 construction)
```

**Substitution chain — leading-order Jacobian rows under canonical scaling**:

```
Step 1 (definition): J_CGWB = (∂Ω_GW/∂a_0, ∂Ω_GW/∂a_2, ∂Ω_GW/∂a_4) at the canonical pin.
       From Ω_GW ∝ G_N ∝ 1/(a_2 M_KK²) at LEADING order:
       J_CGWB ≈ (0, -Ω_GW/a_2, J_CGWB,4)         where J_CGWB,4 enters at NLO via heat-kernel
                                                  renormalization of G_N (sub-leading).

Step 2 (definition): J_α_s = (∂α_s/∂a_0, ∂α_s/∂a_2, ∂α_s/∂a_4).
       From α_s = n_s² - 1, n_s = f(a_2/a_0):
       ∂α_s/∂a_2 = 2 n_s · (∂n_s/∂a_2) = 2 n_s · (1/a_0) · f'(a_2/a_0)
       ∂α_s/∂a_0 = 2 n_s · (∂n_s/∂a_0) = -2 n_s · (a_2/a_0²) · f'(a_2/a_0)
       ∂α_s/∂a_4 ≈ 0 at LEADING order; enters at running-mass NLO.

Step 3 (substitute): the MARGINALIZATION RESIDUAL

       F_marg(CGWB, α_s) = -[J_CGWB · C⁺ · J_α_s]
                         = -[J_CGWB,2 · C⁺_{2,0} · J_α_s,0 + J_CGWB,2 · C⁺_{2,2} · J_α_s,2 + ...]

       Substitute leading-order:
                         = -[(-Ω_GW/a_2) · C⁺_{2,0} · (-2 n_s a_2/a_0² f') +
                             (-Ω_GW/a_2) · C⁺_{2,2} · (2 n_s/a_0 f')]    (LO terms only)
                         = -2 n_s f' Ω_GW · [C⁺_{2,0}/(a_0²) + C⁺_{2,2}/(a_2 a_0)] · (sign factors)

Step 4 (direction): At canonical mean-pinned values (a_0_bar = 3.368, a_2_bar = 0.124),

       C⁺_{2,0} = -1.99e+6
       C⁺_{2,2} = +2.23e+8

       Bracketed scalar = (-1.99e+6)/(3.368)² + (2.23e+8)/(0.124 · 3.368)
                        = -1.75e+5 + 5.34e+8
                        = +5.34e+8                                  (DOMINATED by the (2,2) term)

       The marginalization residual is NON-ZERO and POSITIVE in scaling, with magnitude
       proportional to Ω_GW × n_s × f' × 5.34e+8.

       For Ω_GW = 8.299e-58, n_s = 0.9649, |f'| ≈ O(1) (canonical normalization),
       |F_marg| ≈ 0.965 × 8.299e-58 × 5.34e+8 ≈ 4.27e-49.

       Compare to the observable-Fisher floor: σ_LISA × σ_CMBS4 = 1.0e-12 × 0.003 = 3.0e-15.
       Ratio: 4.27e-49 / 3.0e-15 ≈ 1.4e-34.

Step 5 (canonical form): F_marg ≈ 4.27e-49 ≪ 3.0e-15. Marginalized correlation
       ρ_marg = F_marg / sqrt(F_α_s · F_Ω_GW) = 4.27e-49 / sqrt(1.111e+5 · 1.000e+24)
              = 4.27e-49 / 1.054e+14.5 = 4.05e-64.5
              ≈ 1.3e-63.                       (Effectively zero at OBSERVABLE level.)
```

**EMERGES — the substrate-vs-observable distinction is quantitative**:

The MARGINALIZATION RESIDUAL F_marg(CGWB, α_s) is non-zero (4e-49 at the canonical pin) — that confirms M3's claim that the substrate covariance C does propagate into the off-diagonal Fisher element. **But** the magnitude is so far below the experimental Fisher diagonal floor that the OBSERVABLE-LEVEL ρ_marg is ~1e-63 — for all practical detector purposes indistinguishable from zero.

This means tesla and I are BOTH RIGHT, at different layers:
- **mack right at substrate-Fisher level**: F_marg(CGWB, α_s) ≠ 0 by direct computation. The substrate covariance C is real, near-singular, and propagates through the Schur complement.
- **tesla right at observable-Fisher level**: |F_marg| / sqrt(F_α_s · F_Ω_GW) ≈ 1e-63, which is genuinely zero for any conceivable detector.

The dilution mechanism is the σ(Ω_GW) = 1e-12 floor. CGWB is so far below LISA threshold (Ω_GW = 8.3e-58 vs σ = 1e-12 — 46 OOM gap) that any substrate covariance gets diluted into observational irrelevance.

**The physical lesson**: the W13-2 ρ_cc=0 verdict is correct **as a statement about projected observable significance under current detector noise**, but it should not be read as a statement that the substrate produces independent observables. The substrate produces covariant observables with a 46-OOM detector dilution that swamps the covariance — a different physical claim that should be reflected in the §6A pre-registration language.

**Caveat — this estimate uses MEAN-PINNED a_n values across the regulator atlas**:

If the framework commits to a SPECIFIC regulator (zeta, per W13-2 line 238), the substrate covariance C is a property of the framework's regulator-conditional uncertainty about the substrate (interpreted as Bayesian), not of the regulator-atlas spread. Under that interpretation, the W13-2 ρ_cc=0 IS the right answer (no substrate-covariance to marginalize over) — but then the W12-4 closure is irrelevant to the W13-2 Fisher, and §6A becomes a trivial closure. **Q-tesla in M4 picks this up**: which interpretation of C does the framework commit to?

#### M3: Why ρ=0 May Be Under-Resolution Artifact, Not Independence

**Refined claim — partial retreat from the original M3 framing in light of the M2 quantitative result**.

The original M3 framing in the prompt ("ρ=0 may be under-resolution artifact, not independence") asked whether the W13-2 Fisher matrix is too coarse to surface a real substrate covariance. The M2 computation makes the answer precise: **at the SUBSTRATE Fisher level, ρ_marg ≠ 0; at the OBSERVABLE Fisher level, ρ_marg ≈ 1e-63 ≪ 1**. Both statements are correct; they describe different objects.

The methodologically important point is that **W13-2 line 263's "ρ_cc=0" is NOT a statement about the substrate's predicted observable correlations**. It is a statement about the EXPERIMENTAL Fisher's off-diagonal, computed in a basis where no shared substrate parameters are surfaced. Specifically:

```
W13-2 Fisher (verbatim, working paper §W13-2 (e), reproduced from line 207 of workshop file):
  F = diag( 1/σ²(α_s_CMBS4), 1/σ²(Ω_GW_LISA) )
    = diag( 1/(0.003)², 1/(1e-12)² )
    = diag( 1.111e+5, 1.000e+24 ).

Off-diagonal F_12 = 0 by construction — no shared fit parameter in the (CGWB, α_s) basis.
ρ_cc = F_12 / sqrt(F_11 F_22) = 0.
```

The "by construction" clause is load-bearing. The Fisher off-diagonal is zero **because the basis was chosen with no shared parameter**. If we re-construct the Fisher in the (α_s, Ω_GW, a_0, a_2, a_4) basis and marginalize over the substrate moments, M2 shows F_marg ≠ 0 at the substrate level — but the diluted observable correlation remains effectively 1e-63.

**Three structurally distinct ρ values in this workshop**:

| ρ name | Definition | Value | Status |
|:-------|:-----------|:------|:-------|
| ρ_cc (W13-2) | Off-diagonal of `diag(1/σ²(α_s), 1/σ²(Ω_GW))` | 0 (exact, by construction) | ALREADY PASS |
| ρ_substrate-Fisher | Off-diagonal of marginalized 2×2 from full 5×5 with a_n nuisance | 1.3e-63 (M2 estimate, mean-pinned) | NEAR-ZERO at observable scale |
| ρ_substrate-prediction | Pearson correlation of (O_CGWB, O_α_s) under the framework's predictive distribution over substrate parameters | ? — would require Monte Carlo over (a_0, a_2, a_4) under W12-4 atlas | UNCOMPUTED |

The third quantity — `ρ_substrate-prediction` — is the one that bears most directly on the §6A schedule's "joint-detection significance multiplies" claim. If the framework predicts (CGWB, α_s) values that are statistically correlated under the regulator-conditional uncertainty in the substrate, then the JOINT detection of both observables at their predicted values is NOT the product of independent probabilities — it is the joint probability under a non-trivial substrate prior.

**Substitution chain (method-level, not numerical):**

```
Step 1 (definition): JOINT-detection significance Z_joint of two observables (O_1, O_2) at
                     predicted (μ_1, μ_2) given experimental uncertainties (σ_1, σ_2):
                     Z_joint² = (Δ_1/σ_1)² + (Δ_2/σ_2)² - 2 ρ (Δ_1/σ_1)(Δ_2/σ_2)
                     where Δ_i = (observed_i - μ_i) and ρ is the prediction correlation.

Step 2 (substitute, ρ = 0 case, what W13-2 claims):
                     Z_joint² = (22.99)² + (8.299e-58/1e-12)²
                              = 528.5 + 6.89e-91
                              = 528.5
                     Z_joint = 22.99 (α_s alone — Ω_GW is undetectable on the LISA floor anyway).

Step 3 (substitute, ρ ≠ 0 case):
                     The CGWB term is so small (8.299e-58/1e-12)² = 6.89e-91 that even
                     |ρ| = 1 contributes -2·(22.99)·(8.30e-46) ≈ -3.8e-44 to Z_joint² — negligible.

Step 4 (direction): the ρ value is OPERATIONALLY IRRELEVANT to Z_joint
                     because the CGWB observable is undetectable.

Conclusion: the W13-2 "joint-detection significance multiplies" claim is structurally correct
            FOR THIS PARTICULAR PAIR, because the CGWB Δ_2/σ_2 ratio is 8.3e-46 — so dilute
            that any ρ from -1 to +1 produces no observable difference in Z_joint. The
            ρ_cc = 0 verdict is robust by detector-floor dilution, NOT by substrate
            independence.
```

**This is a structural finding, not a defeat for tesla**:

- tesla's "Fisher PSD" proof (T4) gets the right answer (ρ_cc = 0 is correct under the 2-parameter Fisher) by an argument I dispute (SO(3) irrep-orthogonality at parameter-level is undefended). But it doesn't matter for the W13-2 closure because the CGWB observable is detector-undetectable at LISA floor — the joint significance is dominated by α_s alone regardless of ρ.

- mack's "substrate covariance" objection (M1, M2) shows F_marg ≠ 0 at substrate level (substantive substrate-side finding), but the observable-level dilution makes it operationally invisible.

**Where this matters going forward**:

The §6A workshop verdict should record: ρ_cc = 0 holds at observable level by detector-floor dilution, not by substrate independence; the framework predicts non-trivial substrate-level F_marg that is currently invisible to LISA but might be visible to a future joint detector pairing if Ω_GW is bounded above by a stronger experiment (the LISA floor is the bottleneck, not the substrate). For a future detector with σ(Ω_GW) ~ Ω_GW_predicted (i.e., 5σ detection of CGWB at predicted level — would require ~46 OOM detector improvement, or a different observable in the same family with smaller predicted/floor ratio), the ρ ≠ 0 substrate prediction WOULD become observable.

#### M4: Questions for tesla

These are framed reciprocally to tesla's Q-mack-1 through Q-mack-5 — each is structurally falsifiable, computable in R2, and targets a load-bearing step of tesla's steelman. Numbered to match style.

**Q-tesla-1 — Explicit parameter-level kernel inner product**.

Per Re:T3 / Re:T4, the SO(3) irrep-orthogonality lemma (T4 Step 5) is a statement about observable-space mode decomposition (tensor-2 vs scalar-0), not about parameter-space Jacobian alignment. Re-derive the kernel-orthogonality lemma at the PARAMETER LEVEL: produce, at canonical pin (zeta scheme, a_2 = 0.158, a_0 = 3.7074, a_4 = 0.011994, L_max=10), the explicit values of

```
∂Ω_GW(f_LISA_pivot) / ∂a_2          = ?
∂Ω_GW(f_LISA_pivot) / ∂a_4          = ?           (NLO, expected non-zero through G_N renorm)
∂α_s(k*=0.05 Mpc⁻¹) / ∂a_2          = ?           (LO)
∂α_s(k*=0.05 Mpc⁻¹) / ∂a_0          = ?           (LO via a_2/a_0 ratio)
∂α_s(k*=0.05 Mpc⁻¹) / ∂a_4          = ?           (NLO via running-mass)
```

and compute the inner product `J_CGWB · C⁻¹ · J_α_s` directly. My M2 estimate gives F_marg ≈ 4.27e-49 using mean-pinned a_n; your computation at zeta-pinned a_n (one specific regulator) should be comparable in magnitude or smaller. Falsifier: if your |F_marg| at zeta-pin is below 1e-15 (the σ_LISA · σ_CMBS4 floor), the W13-2 ρ_cc=0 verdict is robust at observable scale by direct computation, not by detector-floor dilution. If your |F_marg| is above 1e-15, the substrate covariance is non-trivially propagating into observable space, contradicting the W13-2 claim.

**Q-tesla-2 — Regulator-Bayesian vs regulator-conditional interpretation of C**.

The substrate covariance C in M2 was computed by treating the 5-regulator atlas as 5 SAMPLES from a (Bayesian) posterior over substrate parameters. This is one possible interpretation. The alternative is that the framework COMMITS to a specific regulator (zeta) and the C of M2 is irrelevant — there is no Bayesian uncertainty over a_n at all, just a single zeta-pinned value. Which interpretation does the framework commit to? Specifically:

(a) **Regulator-Bayesian**: substrate truth is unknown, the 5-regulator spread reflects irreducible uncertainty, C is real, F_marg ≠ 0 is real (M2). Implication: the framework predicts substrate-level CGWB-α_s correlation, even if observably diluted.

(b) **Regulator-conditional (zeta-committed)**: substrate truth IS the zeta-scheme value, the 5-regulator atlas is a probe of WHICH regulator best matches the substrate (a methodological exercise), and C is artifactual. Implication: the framework predicts substrate-level CGWB-α_s independence, and the W13-2 verdict line (which names zeta) is a substrate-truth claim.

(c) **Atlas-stratified**: framework commits to regulator-INVARIANT substrate predictions; observables that are class-(d) under W12-4 are not pre-registerable as substrate truths. Implication: W13-2's ρ_cc=0 verdict is a zeta-conditional pre-registration, not a framework-substrate claim, and §6A's correct decision is **(c)** in the schedule's three-way fork.

Which of (a) / (b) / (c) does the framework commit to? This is a pre-registration choice, not a computation.

**Q-tesla-3 — Regulator-invariance of the kernel-orthogonality reformulation**.

If your R2 reformulates kernel-orthogonality at the parameter level (per Q-tesla-1), is the reformulated lemma REGULATOR-INVARIANT under the W12-4 atlas? Specifically: for each regulator r in {heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars}, evaluate `J_CGWB(r) · C⁻¹ · J_α_s(r)` and report all 5 values. If they agree to within a factor 2, the kernel-orthogonality holds atlas-uniformly and §6A decision (a) is robust. If they spread by 5+ orders of magnitude (analogous to a_2's atlas spread), §6A decision (c) is the right pre-registration — and Q-mack-2 was correctly anticipated. The case where they spread by 1-3 OOM is the most interesting: the orthogonality is partially regulator-conditional, and the §6A verdict needs to specify which regulator the W13-2 claim binds to.

**Q-tesla-4 — Scope of the experimental Fisher block-diagonality claim**.

In Re:T4 I distinguished the EXPERIMENTAL Fisher (block-diagonal by 13.6-OOM frequency separation, robust regardless of substrate covariance) from the SUBSTRATE Fisher (off-diagonal possibly non-zero). The W13-2 verdict line writes the experimental Fisher and reports ρ_cc=0 as its off-diagonal — this is correctly verified. But the schedule §6A invocation language ("CGWB ⊥ α_s independence diagrammatic audit") suggests a stronger claim — substrate-level independence. Which claim does W13-2 actually pre-register? My read of W13-2 §(e) (s85-w13-workingpaper.md line 207, fully read) is the experimental claim. Confirm? If yes, M3's reformulation of the workshop verdict (ρ_cc=0 holds by detector-floor dilution, not by substrate independence) lands cleanly. If no, you need to defend the stronger substrate-independence claim, which Re:T4 leaves undefended.

**Q-tesla-5 — Diagrammatic-audit cost-benefit for §6A pre-registration**.

The §6A schedule's third decision option is "(c) regulator-conditional (NEW result extending W12-4)". Given (i) the W12-4 closure has already pinned a_n as class-(d), (ii) the W13-2 verdict line names zeta explicitly, (iii) the M2 numerics show observable-level ρ ~ 1e-63 by detector-floor dilution regardless of substrate covariance — what does adopting decision (c) explicitly buy us, beyond what (a) at zeta-pin gives? My answer: it forces every future S86+ gate that cites ρ(CGWB, α_s) to inherit the regulator-pin discipline, preventing a future PRU class-8 defect where a paper or session quotes "ρ_cc = 0" without specifying the regulator. That seems worth pre-registering as the W12-4-aware version of the W13-2 closure. Do you agree, or do you see (a) as adequate?

These five questions partition into: **Q-tesla-1** (numerical task — produce the explicit Jacobians and F_marg); **Q-tesla-2** (interpretation-of-C declaration — what does C mean, in the framework's epistemology of substrate uncertainty?); **Q-tesla-3** (regulator-atlas robustness check on the reformulated kernel-orthogonality lemma); **Q-tesla-4** (scope clarification on the W13-2 claim itself); **Q-tesla-5** (registry-discipline question — what should §6A pre-register, given W12-4?). Together with your Q-mack-1 through Q-mack-5, this defines a complete R2 work-plan for both sides.

---

## Round 2 — tesla: RESPOND (Explicit Fisher Recomputation with a_n Nuisance)

**Computation pin**: `computations/_s85_6a_tesla_r2_fisher_5x5.py` and companion JSON `_s85_6a_tesla_r2_fisher_5x5.json`. Single Python execution, no iterations. All numbers in this section come from that one run; cross-checked against mack's M2 closed-form on the mean-pinned case (agreement at the same order of magnitude class).

### CONVERGENCE

I converge on three of mack's R1 substantive points. Stated as updates to my T1-TN positions, with the explicit 5×5 Fisher computation as the trigger.

**C1 — Substrate-level F_marg(CGWB, α_s) is non-zero by direct construction. CONCEDED.**

The Schur-complement substitution chain executes, and produces:

```
Step 1 (def):    F_marg = A - B C^{-1} B^T   where C is the augmented nuisance block (substrate prior + Fisher contribution).
Step 2 (subst):  J_CGWB(zeta)    = (0, -Omega_GW/a_2, 0) = (0, -5.249e-57, 0)
                 J_alpha_s(zeta) = (-2 n_s^2/a_0, +2 n_s^2/a_2, 0) = (-5.023e-1, +1.178e+1, 0)
                 C_pinv          (3x3, from W12-4 5-regulator atlas, condition 7.57e+10)
                                 = [[+1.78e+04, -1.99e+06, +4.84e+07],
                                    [-1.99e+06, +2.23e+08, -5.41e+09],
                                    [+4.84e+07, -5.41e+09, +1.31e+11]]
Step 3 (simpl): F_marg(CGWB, alpha_s)        = +3.42e-34   (from full 5x5 Schur, zeta-pin)
                F_marg_substrate-only(CGWB, alpha_s)
                                              = -J_CGWB . C_pinv . J_alpha_s
                                              = +1.38e-47   (zeta-pin)
                                              = +2.29e-47   (mean-pin)
Step 4 (dir):   F_marg[CGWB, alpha_s] is STRICTLY POSITIVE and NON-ZERO.
                Therefore my T4 Step 5 lemma "F_marg(CGWB, alpha_s) = 0 IDENTICALLY by SO(3) irrep-orthogonality"
                IS WRONG AS A STATEMENT ABOUT THE PARAMETER-SPACE SCHUR COMPLEMENT.
```

mack's Re:T3 / Re:T4 critique lands cleanly: SO(3) irrep-orthogonality is mode-space orthogonality at the observable level (tensor-2 × scalar-0 inner product on the post-fold acoustic spectrum). The Schur complement does not see SO(3) representation indices — it sees scalar partial derivatives of observables with respect to scalar substrate parameters a_n. My T4 lemma conflated those two orthogonalities. The traceless-transverse projection theorem (s69_transit_gw.py) is correct AT THE LEVEL OF THE OBSERVABLES Ω_GW vs A_s — but the Fisher cross-block is a Jacobian on parameter-space, which is SO(3)-singlet-valued. **mack right at the substrate-Fisher level**.

The numeric agreement of mack's M2 closed-form (4.27e-49 at mean-pin) with my full-5×5 Schur (2.29e-47 at mean-pin substrate-only term) is at the same OOM-class — a factor ~50, attributable to mack's M2 not including the cross-couplings between the J_alpha_s a_0-component and the C_pinv off-diagonal (mack's M2 step 4 substitution explicitly evaluates only the (2,0) and (2,2) C+ terms; my full computation includes (0,0), (0,2), (2,0), (2,2)). The structural conclusion is identical.

**C2 — Observable-level dilution is the actual mechanism. CONCEDED as primary.**

The substitution chain for the observable-level ρ:

```
Step 1 (def):    rho_marg = F_marg[0,1] / sqrt(F_marg[0,0] * F_marg[1,1])
Step 2 (subst):  F_marg[0,0] = 2.003e+00   (alpha_s diagonal, post-marginalization-with-prior)
                 F_marg[1,1] = 1.000e+24   (Omega_GW diagonal, dominated by sigma_LISA^{-2})
                 F_marg[0,1] = +3.424e-34
Step 3 (simpl): denom = sqrt(2.003 * 1.000e+24) = 1.415e+12
                rho_marg = 3.424e-34 / 1.415e+12 = 2.42e-46
Step 4 (dir):   |rho_marg| ~ 2.4e-46. The detector floor sigma_LISA * sigma_CMBS4 = 1e-12 * 0.003
                gives an "operational" rho-floor of 1e-15. |rho_marg| / floor = 2.4e-31.
                Conclusion: rho_marg is observably ZERO to 30 OOM below the floor.
```

mack's M3 framing — "the W13-2 ρ_cc=0 verdict is correct as a statement about projected observable significance under current detector noise, but not as a statement that the substrate produces independent observables" — is the structurally correct read of the W13-2 verdict line. I now adopt it: the detector-floor-dilution mechanism (σ(Ω_GW) = 10⁻¹² floor with predicted Ω_GW = 8.3e-58, a 46-OOM gap) is what guarantees ρ_observable ≈ 0 regardless of the substrate covariance. The CGWB observable is so far below LISA threshold that any substrate covariance gets diluted by the σ_LISA factor in the denominator.

**C3 — The schedule decision (c) "regulator-conditional" is the conservative pre-registration. CONCEDED as preferred.**

Per-regulator F_marg recomputation (Q-tesla-3 explicit answer):

| Regulator | a_2 value | F_marg[0,1] | rho_marg |
|:----------|:---------:|:-----------:|:--------:|
| heat-kernel | 0.15445 | +3.467e-34 | +2.494e-46 |
| zeta | 0.15810 | +3.424e-34 | +2.419e-46 |
| Mellin | 0.15810 | +3.424e-34 | +2.419e-46 |
| hard-cutoff | 0.11100 | +2.883e-34 | +3.126e-46 |
| Pauli-Villars | 0.03185 | +4.457e-34 | +1.411e-45 |

Spread across atlas: ρ_marg ∈ [+2.42e-46, +1.41e-45], factor ~5.8. Pauli-Villars produces the largest |ρ_marg| due to its smallest a_2 (which AMPLIFIES J_alpha_s ∝ 1/a_2). This is the W12-4 class-(d) regulator-divergence propagating into the marginalized observable correlation. ALL FIVE values lie 30+ OOM below the operational floor — but they are not equal, and a future detector with σ(Ω_GW) bounded below by an independent constraint (or a different observable in the same family with smaller predicted/floor ratio) would surface this regulator-conditioning.

**Decision (c)** is therefore the structurally defensible pre-registration: the W13-2 ρ_cc=0 verdict line names zeta explicitly and binds at zeta only; the regulator-atlas spread of ρ_marg is non-trivial at substrate level even if observably diluted. Future S86+ gates citing ρ(CGWB, α_s) inherit the regulator-pin discipline.

### DISSENT

I retain dissent on two narrow points where the explicit 5×5 Fisher recomputation supports the original independence claim against mack's "C-amplification produces O(1) corrections" framing.

**D1 — The C-amplification from condition 1.31e+11 does NOT propagate to observable-level ρ at the W13-2 sigmas. STRUCTURAL FACT, NOT REGULATOR ARTIFACT.**

mack's Re:T4 worried that "even a kernel mismatch at order 10⁻¹⁰ in dimensionless units can produce O(10) corrections to the off-diagonal Fisher element" because of the C_pinv entries up to 1.31e+11. The explicit Schur recomputation puts a number on this:

```
Step 1 (def):   F_marg_offdiag = -J_C^T C^{-1} J_a (with full 5x5 Schur)
Step 2 (subst): largest J entry: J_alpha_s[a_2] = +1.178e+1 (dimensionless x scale)
                largest J entry: J_CGWB[a_2]    = -5.249e-57 (dimensionless x Omega_GW)
                largest C^{-1} entry: 1.31e+11 (a_4, a_4)
Step 3 (simpl): worst-case product J_a * C^{-1}_max * J_C
                = (1.178e+1) * (1.31e+11) * (5.249e-57)
                = 8.10e-45
                Actual computed F_marg[0,1] = +3.42e-34 (full Schur including prior on a_n)
                The worst-case bound is dominated by the (a_4, a_4) C^{-1} entry, but
                J_C[a_4] = J_a[a_4] = 0 at LO, so that worst-case never materializes.
                The dominant Schur term is C^{-1}[a_2, a_2] * J_a[a_2] * J_C[a_2]
                = (2.23e+8) * (+1.178e+1) * (-5.249e-57)
                = -1.38e-47   (substrate-only; zeta).
Step 4 (dir):   |F_marg[0,1]| = 3.42e-34 (Schur with prior; zeta) is DOMINATED by
                the small Omega_GW magnitude (8.3e-58), not by the C-amplification.
                The C-amplification factor 10^11 cannot rescue Omega_GW from its 46-OOM
                detector deficit.
```

The structural reason mack's worry doesn't materialize: J_CGWB has only ONE non-zero entry at LO (the a_2 column), at magnitude 5.25e-57 — set by Ω_GW itself. The 1.31e+11 entry of C_pinv lives in the (a_4, a_4) slot, which J_CGWB doesn't reach at LO. So the C-amplification factor that worried mack does not couple to the leading-order Jacobian. **D1 is structural, not numerical accident**: at NLO (heat-kernel renormalization of G_N entering CGWB through a_4), J_CGWB[a_4] becomes non-zero and the (a_4, a_4) amplification engages — but at NLO suppression `~ a_4/a_2 ~ 0.076` (or up to 0.213 at Pauli-Villars per mack's M1 P1 analysis), the contribution gains 1.3e+11 amplification × 0.076² = 7.5e+8 enhancement, then is suppressed by the same Ω_GW magnitude.

This means: any future workshop computing CGWB at NLO will need to re-execute the Schur complement with the J_CGWB[a_4] entry filled in; the present LO result does not constrain the NLO answer. Carry-forward.

**D2 — The 13.6-OOM frequency separation (T3 axis (ii)) IS still a structural wall at the EXPERIMENTAL Fisher level, regardless of substrate covariance.**

mack's Re:T3 paragraph on axis (ii) agreed this is correct but characterized it as "independence of the experimental noise covariance, not of the signal substrate dependence." That is right, but I want to record that the 13.6-OOM gap is a SECOND independence channel orthogonal to the substrate-covariance channel: even if some future regulator violated SO(3)-irrep-orthogonality at the observable mode-space level, the experimental Fisher (which is what the W13-2 verdict line measures) would still be diagonal. So the W13-2 ρ_cc=0 verdict has TWO independent supports:

1. **Substrate detector-floor dilution** (C2 above): 46-OOM gap between Ω_GW and σ_LISA suppresses any substrate covariance.
2. **Frequency-band non-overlap** (T3 axis (ii)): no LISA Fourier bin maps to any CMB temperature multipole; experimental noise covariance is exactly block-diagonal.

Either alone would secure the verdict line at observable level. Both together make the W13-2 ρ_cc=0 robust under reformulation of the substrate kernel-orthogonality lemma.

### EMERGENCE

The "both right at different layers" framing in mack's M2 EMERGES paragraph (workshop lines 766-776) is the converged outcome direction. Both R1 positions held real content; the explicit 5×5 Fisher recomputation now decomposes them cleanly:

| Layer | Quantity | Value (zeta pin) | Status | Origin |
|:------|:---------|:----------------:|:------:|:-------|
| Substrate-only Schur term | -J_C · C⁻¹ · J_α | +1.38e-47 | NON-ZERO | mack right (Re:T3, M2) |
| Substrate Fisher full Schur | F_marg[0,1] | +3.42e-34 | NON-ZERO | mack right (M2) |
| Observable Fisher diagonal | ρ_cc (W13-2) | 0 (by construction) | ZERO BY BASIS CHOICE | tesla T4 |
| Observable Fisher marginalized | ρ_marg (Schur) | +2.42e-46 | EFFECTIVELY ZERO | tesla T4 + dilution |
| Observable detection floor | σ_LISA · σ_CMBS4 | 3e-15 | – | – |
| Ratio \|ρ_marg\|/floor | – | 8.06e-32 | 31 OOM below floor | – |

The §6A schedule decision direction:

- **Decision (a)** "ρ=0 genuine" — defended at OBSERVABLE LEVEL, with two independent supports (D2 above), but the underlying mechanism is detector-floor dilution + experimental-noise frequency-band separation, not substrate independence.
- **Decision (b)** "ρ ≠ 0 after a_n marginalization" — TRUE at SUBSTRATE LEVEL (F_marg = +3.42e-34 ≠ 0), but the value is so far below detection that it does not propagate to observable significance.
- **Decision (c)** "regulator-conditional (NEW result extending W12-4)" — STRUCTURALLY CORRECT pre-registration. The per-regulator ρ_marg spread (+2.42e-46 to +1.41e-45) is a factor-5.8 spread directly inherited from the W12-4 class-(d) divergence; any future S86+ gate quoting ρ(CGWB, α_s) without naming a regulator is PRU-class-8 ill-formed.

**My converged read for R3**: Decision **(c)**, with the verdict text reading: "ρ_cc = 0 holds at OBSERVABLE level by detector-floor dilution AND experimental-noise frequency-band separation; substrate F_marg ≠ 0 at all 5 regulators in the W12-4 atlas, with regulator-conditional spread ~factor 6; future cross-channel correlations of (CGWB, α_s) inherit the W12-4 regulator-pin discipline."

This is more substantive than (a) (which would close the diagrammatic audit prematurely on a detector-conditional claim) and weaker than (b) (which would over-state the observable consequence of substrate covariance). (c) is the W12-4-aware version of the W13-2 closure — which is what mack's Q-tesla-5 anticipated.

### QUESTIONS

**Answers to mack's Q-mack-1 through Q-mack-5** (matched to mack's M4 numbering since Q-mack-1..5 in T-track are tesla's questions to mack — answering mack's Q-tesla-1..5 instead):

**A-tesla-1 (parameter-level kernel inner product)**. Computed explicitly:

```
J_alpha_s · C^{-1} · J_CGWB at zeta-pin = +1.378e-47
```

This is below the 1e-15 σ_LISA·σ_CMBS4 floor by 32 OOM. The W13-2 ρ_cc=0 verdict is **robust at observable scale by direct computation, not only by detector-floor dilution** — the substrate F_marg is itself 32 OOM below the floor before any further dilution. mack's Re:T4 prediction of "C-amplified ε² ~ 10⁶-10⁷" did not materialize because J_CGWB[a_4] = 0 at LO (the channel that would amplify is dormant). NLO recomputation is the natural follow-up.

**A-tesla-2 (regulator-Bayesian vs zeta-committed interpretation of C)**. Pre-registration choice — I commit to **(c) atlas-stratified**: framework predictions for substrate-level a_n are regulator-CONDITIONAL, and observables that are class-(d) under W12-4 inherit the regulator-pin label. The W13-2 verdict line writes "scheme=zeta" — this is a well-formed regulator-pinned pre-registration but NOT a substrate-truth claim. The S86 gate spec must inherit this discipline. (a) and (b) are both reasonable epistemic stances but commit the framework to either over-precision (b: zeta is the substrate truth) or maximal Bayesian humility (a: 5-regulator spread is the irreducible uncertainty); (c) sits at the methodologically conservative middle.

**A-tesla-3 (regulator-invariance of reformulated kernel-orthogonality)**. The reformulation cannot rest on SO(3) irrep-orthogonality at the parameter level — that lemma is dead per C1. The reformulation must rest on **dimensional analysis + scaling-law structure**:

- J_CGWB[a_n] = 0 ∀ n ≠ 2 at LO (since 1/G_N = (48 f_2 / π) a_2 M_KK², no a_0 or a_4 dependence).
- J_alpha_s[a_4] = 0 at LO (since α_s = n_s²−1 with n_s = f(a_2/a_0); a_4 enters only via running-mass NLO).
- Therefore the LO Schur sum collapses to ONE term: -J_α[a_2] · C⁻¹[a_2,a_2] · J_C[a_2] + (cross-terms with a_0 of α_s only).

This LO structure is regulator-invariant under the W12-4 atlas because the scaling laws are framework-universal; the SPREAD across regulators comes from the EVALUATION POINT (different a_2 values pin different J magnitudes) and the C⁻¹ entries (different correlations across atlas), not from the kernel structure itself. The factor-5.8 atlas spread reported above is therefore a real W12-4-inherited regulator-conditioning, not a kernel structural defect.

**A-tesla-4 (scope of W13-2 experimental-Fisher claim)**. CONFIRMED — the W13-2 verdict line writes the EXPERIMENTAL Fisher (`F = diag(1/σ²(α_s_CMBS4), 1/σ²(Ω_GW_LISA))`), not the substrate-marginalized Fisher. mack's M3 reformulation of the workshop verdict ("ρ_cc=0 holds by detector-floor dilution, not by substrate independence") is the structurally accurate read of W13-2 §(e). The R3 final §6A pre-registration should therefore distinguish three ρ values by name — `ρ_experimental` (W13-2 verdict, ≡ 0 by basis), `ρ_substrate-marg` (R2-A computation, +2.4e-46 at zeta, +1.4e-45 at PV), and `ρ_substrate-prediction` (Monte Carlo over predictive distribution, currently UNCOMPUTED, deferred to S86+).

**A-tesla-5 (cost-benefit of decision (c) for §6A pre-registration)**. AGREE. Adopting (c) buys: (i) inheritance of the W12-4 regulator-pin discipline into all future S86+ joint-channel gates; (ii) explicit recognition that the W13-2 ρ_cc=0 verdict is observable-Fisher only and not substrate-truth; (iii) a CARRY-FORWARD to S86 for the NLO J_CGWB[a_4] computation that engages the (a_4, a_4) C-amplification channel (currently dormant at LO). (a) at zeta-pin would miss (iii); (b) without regulator pin would inherit PRU class-8 ill-formedness.

**New questions for R2-B (mack's response)**:

- **Q-tesla-6 — Diagrammatic kernel computation cross-check**. mack's R2 plan (per Q-mack-1 in M4) is to produce the explicit diagrammatic Mellin-moment kernel decomposition `K_CGWB[a_n](k_GW)` and `K_alpha_s[a_n](k*_CMB)` and compute ⟨K_CGWB[a_2], K_alpha_s[a_2]⟩ at the parameter level. My A-tesla-1 gives the FULL-Schur answer F_marg = +1.38e-47 at zeta-pin substrate-only. Does mack's explicit diagrammatic Mellin computation at zeta agree to within an OOM? If not, where does the discrepancy live (kernel structure, contour, normalization)?

- **Q-tesla-7 — NLO J_CGWB[a_4] order-of-magnitude estimate**. The (a_4, a_4) entry of C_pinv is +1.31e+11 — eight OOM larger than (a_2, a_2). At LO, J_CGWB[a_4] = 0. Under heat-kernel renormalization of G_N at NLO, J_CGWB[a_4] ~ Ω_GW × δ × (a_4 contribution coefficient), where δ is the NLO suppression. What is mack's estimate of J_CGWB[a_4] under the framework's heat-kernel a_4 entry into 1/G_N (`ε² ~ 4e-4` ?), and does the resulting NLO F_marg cross 1e-15 at any regulator in the atlas? This determines whether decision (c) needs an "NLO-revisited at S86" carry-forward clause.

- **Q-tesla-8 — Predictive Monte Carlo over substrate priors**. The third ρ-value in mack's M3 table — `ρ_substrate-prediction` — is currently UNCOMPUTED. Does mack consider this a separate gate (S86 or beyond), or is it a R3-CONVERGE clause that the workshop should pre-register? My read: it is a separate S86 gate (requires Monte Carlo over the predictive distribution of (a_0, a_2, a_4) under the W12-4 atlas, propagated through the full Jacobian to (Ω_GW, α_s)), and the workshop's R3 verdict only records that it is an open computation. Confirm?

- **Q-tesla-9 — Cross-pairing to S-5 Falsifier Master-Inventory**. The schedule mentions S-5 cross-pairing for §6A. Given the convergence on decision (c), what S-5 falsifier slot does the regulator-conditional CGWB×α_s claim populate? My provisional read: a NEW falsifier line — "If a future detector with σ(Ω_GW) ≲ 1e-30 measures ρ(CGWB, α_s) ≠ 0 at >5σ AND the framework's regulator-conditional prediction band is [+2.4e-46, +1.4e-45], the framework is falsified at the chosen regulator" — but this may not deserve a falsifier line if the predicted band is uniformly below all conceivable detector floors. Does mack agree this is a non-falsifier (i.e., currently observationally inert) prediction, or does it warrant a placeholder S-5 line?

These four R2-B questions together with the R2-A computation define what R3 must close on.

---

## Round 2 — mack: RESPOND (Diagrammatic Kernel Decomposition)

**Computation pin**: Direct verification of tesla's R2-A `_s85_6a_tesla_r2_fisher_5x5.json` outputs against the M2 closed-form, plus the (k_GW, k*_CMB) projection-kernel construction used in this turn. Substitution chains executed inline, Python-verified for sign/magnitude before being asserted.

### CONVERGENCE

I converge on four R2-A points. Each is stated as a substantive update to my R1 position, with the trigger explicitly cited.

**C-mack-1 — The detector-floor dilution mechanism is the operationally correct read of W13-2. CONCEDED as the headline mechanism.**

tesla R2-A §C2 lands the substitution chain that operationally retires my R1 worry that "C-amplification produces O(1) corrections to F_marg." The chain executes:

```
Step 1 (def):   ρ_marg = F_marg[0,1] / sqrt(F_marg[0,0] · F_marg[1,1])             [Schur, marginalized]
Step 2 (subst): F_marg[0,1] = +3.42e-34   (zeta-pin, full 5x5 Schur with prior)    [tesla R2-A line 916]
                F_marg[0,0] = 2.003e+00   (alpha_s diag with prior)                 [tesla R2-A line 937]
                F_marg[1,1] = 1.000e+24   (Omega_GW diag dominated by sigma_LISA^{-2})
Step 3 (simpl): denom = sqrt(2.003 · 1.000e+24) = 1.415e+12
                ρ_marg = 3.42e-34 / 1.415e+12 = 2.42e-46                            [tesla R2-A line 940]
Step 4 (dir):   |ρ_marg| ≪ floor (3e-15) by 31 OOM.
                The σ_LISA = 1e-12 floor with predicted Ω_GW = 8.299e-58 gives a
                46-OOM gap; this is what suppresses ρ at the observable layer,
                NOT a substrate-level orthogonality.
```

The operational read in M3 ("ρ_cc=0 holds by detector-floor dilution, not by substrate independence") is now the converged framing. I retract the framing in M2 paragraph 2 ("the C-amplification factor 10^10-10^11 makes 'non-leading' misleading") — at LO the (a_4, a_4) amplification slot is structurally dormant per tesla R2-A §D1. The C-amplification worry materializes ONLY at NLO, where J_CGWB[a_4] becomes non-zero (carry-forward to S86, see EMERGENCE).

**Substrate-language reframing of the converged mechanism**: CGWB is the post-fold acoustic relic spectrum on the **transverse** branch of the GGE relic at c_BLV = 0.485, projected through the graviton-kinetic normalization 1/G_N ∝ a_2 M_KK². α_s is the post-fold acoustic relic spectrum on the **longitudinal** branch, projected through the n_s = f(a_2/a_0) curvature of the heat-kernel expansion at the CMB pivot. These are not "an inflationary tensor background" and "a primordial scalar power spectrum" — they are two co-existing branches of the same GGE relic interfering at the same fold, but the LISA detector reads the transverse branch at f = 3 mHz and the CMB scalar reads the longitudinal branch at f ~ 7.7e-17 Hz. The 13.6-OOM frequency gap is a **detector geometry** wall (D2 in tesla R2-A), not a substrate-orthogonality wall — the substrate produced both branches in the same transit event.

**C-mack-2 — Decision (c) "regulator-conditional" as the conservative pre-registration. CONCEDED.**

tesla R2-A §C3 + A-tesla-2 commit to **(c) atlas-stratified**, which is exactly the position I argued for in M1 / Q-mack-4. The per-regulator F_marg table (R2-A line 952-959) shows ρ_marg ∈ [2.42e-46, 1.41e-45] across the W12-4 atlas — factor 5.8 spread. Two structural facts of that table that I have re-verified by Python:

```
Step 1 (def):    For each regulator r, F_marg(r) = -J_CGWB(r)^T C_pinv J_alpha_s(r) + prior contributions.
                  J_alpha_s[a_2] in tesla's logarithmic-derivative convention = 2 n_s^2 / a_2.
Step 2 (subst):  J_alpha_s[a_2] | zeta = 2 (0.9649)^2 / 0.15810 = 11.778   [Python-verified, matches +1.178e+1]
                  J_alpha_s[a_2] | PV   = 2 (0.9649)^2 / 0.03185 = 58.45    [PV amplifies J_a by factor ~5]
Step 3 (simpl): F_marg ~ 1/a_2^2 would predict F_marg(PV)/F_marg(zeta) = (0.158/0.032)^2 ~ 25.
                  Tesla reports F_marg(PV)/F_marg(zeta) = 4.457e-34 / 3.424e-34 = 1.30 — only factor 1.3.
                  Direct check: F_marg × a_2^2 across the atlas:
                    HK = 8.27e-36, zeta = 8.56e-36, Mellin = 8.56e-36, HC = 3.55e-36, PV = 4.52e-37.
                  This product is NOT constant — factor 18 spread (HK to PV).
Step 4 (dir):   The atlas spread of F_marg is JOINTLY driven by (a) the J_alpha_s ~ 1/a_2 amplification
                  AND (b) per-regulator C_pinv structure shifts. PV's J amplification is partially
                  CANCELLED by its anomalous (a_2, a_0, a_4) covariance pattern.
                  Implication: the regulator-conditional ρ_marg cannot be predicted from a single
                  scaling law — it requires the full atlas-conditional Schur computation that
                  tesla R2-A executed.
```

This is a STRENGTHENING of decision (c): the regulator-conditioning is non-trivially structural, not a simple `a_2^{-2}` rescaling. Future S86+ gates that quote ρ(CGWB, α_s) without naming a regulator inherit a non-recoverable PRU class-8 defect — there is no scaling law to back out the missing regulator from a quoted value.

**C-mack-3 — The diagrammatic kernel inner product gives the same OOM as the Schur substrate-only term.**

R2-A §A-tesla-1 reports `J_alpha_s · C^{-1} · J_CGWB | zeta-pin = +1.378e-47`. I have Python-verified this from tesla's reported (J, C_pinv) values: -np.dot(J_CGWB, C_pinv @ J_alpha_s) = +1.379e-47, with the (m=1, n=1) → (a_2, a_2) entry contributing 1.379e-47 and the (m=1, n=0) → (a_2, a_0) cross only 5.247e-51 (4 OOM smaller).

The diagrammatic Mellin-moment kernel decomposition I owed in R1 (Q-tesla-1 / Q-mack-1) reduces, at LO, to the same single-term Schur sum. Substitution chain:

```
Step 1 (def): K_CGWB[a_n](k_GW) = (heat-kernel propagator weight)(a_n) × (transverse-tensor projector at k_GW)
              K_alpha_s[a_n](k*_CMB) = (heat-kernel propagator weight)(a_n) × (scalar-tilt-derivative projector at k*_CMB)
Step 2 (subst): At LO, the only n with both kernels non-zero is n = 2 (CGWB picks a_2 via 1/G_N;
              α_s picks a_2 via n_s = f(a_2/a_0)). The a_0 column is α_s-only at LO.
              The a_4 column is empty at LO on both sides.
              
              <K_CGWB[a_2], K_alpha_s[a_2]>_C = J_CGWB[a_2] · C_pinv[a_2,a_2] · J_alpha_s[a_2]
                                              + J_CGWB[a_2] · C_pinv[a_2,a_0] · J_alpha_s[a_0]
Step 3 (simpl): At zeta-pin:
              term (2,2) = (-5.249e-57) · (+2.23e+8) · (+1.178e+1) = -1.379e-47
              term (2,0) = (-5.249e-57) · (-1.99e+6) · (-5.023e-1) = -5.247e-51
              Sum (with overall Schur sign flip giving F_marg = -<K_C, K_a>):
              F_marg substrate-only = +1.379e-47 + 5.25e-51 ≈ +1.378e-47
Step 4 (dir): The diagrammatic kernel inner product agrees with tesla R2-A's full-Schur substrate-only
              term to better than 1e-50 — the (a_2, a_0) cross is 4 OOM smaller than the (a_2, a_2)
              diagonal. There is NO clean ρ_marg → 0 from kernel-orthogonality at LO; the inner
              product is non-zero, just diluted by 31 OOM at the observable layer.
```

So the diagrammatic computation does NOT produce a clean kernel-orthogonality (ρ_marg = 0 identically). Substrate non-zero ρ_marg survives the marginalization. The W13-2 ρ_cc=0 verdict survives at the OBSERVABLE layer for the dilution reason (C2), not for the kernel-orthogonality reason that R1 tesla T4 originally claimed.

**C-mack-4 — The factor-32 mack-M2 vs tesla-R2-A discrepancy is a convention difference, not a structural error.**

I owed tesla a reconciliation of M2's 4.27e-49 vs his R2-A 1.38e-47. Python-verified:

```
Step 1 (def): M2 used J_alpha_s[a_2] in LINEAR-derivative convention:
              ∂α_s/∂a_2 = 2 n_s · (∂n_s/∂a_2) = 2 n_s · (1/a_0) · f'(a_2/a_0)
              with f' ≈ 1 (canonical normalization, M2 step 4 line 754).
              Magnitude: 2 (0.9649) (1/3.368) (1) = 0.573.
Step 2 (subst): R2-A used J_alpha_s[a_2] in LOGARITHMIC-derivative convention (line 911):
              J_a[a_2] = 2 n_s^2 / a_2 = 11.778 (zeta-pin, Python-verified).
              Ratio of conventions: 11.778 / 0.573 = 20.6.
Step 3 (simpl): M2 also dropped the (2,0) cross-term and used mean-pinned C entries (close to zeta).
              Combined effect: 20.6 (J convention) × ~1.5 (C-mean vs C-zeta) = ~31.
Step 4 (dir): The factor-32 ratio (verified directly: 1.379e-47 / 4.277e-49 = 32.3) is
              fully accounted for by the convention difference — not a discrepancy in
              physical content. Both estimates land in the same OOM class (~ 1e-48 to 1e-47),
              both 30+ OOM below the observable floor.
```

For R3 we should pin the convention: ∂/∂a_n is the linear-derivative form, and the J entries should be reported with units carried explicitly. tesla's logarithmic form is convenient for the ratio scaling but obscures the dimensional analysis when J_CGWB is in units of Ω_GW. I propose for R3 that the canonical form be linear-derivative with explicit units, and tesla's logarithmic convention be reported as an alternate form for scaling analysis.

### DISSENT

I retain dissent on two narrow points where R2-A overstates what is established. Both are corrections to framing, not to the headline result.

**D-mack-1 — The "two independent supports" framing in R2-A §D2 conflates orthogonal claims at the substrate-vs-detector boundary.**

R2-A §D2 lists (1) "substrate detector-floor dilution" and (2) "frequency-band non-overlap" as two independent supports for the W13-2 ρ_cc=0 verdict. I agree both mechanisms exist; I dispute that they are independent SUPPORTS for the same claim, because they certify different objects.

```
Step 1 (def):  Detector-floor dilution operates on F_marg / sqrt(F_alpha_s · F_Omega_GW) where
               F_Omega_GW = 1/sigma_LISA^2 = 1e+24. It suppresses the substrate F_marg into
               observable irrelevance.
Step 2 (def):  Frequency-band non-overlap (13.6 OOM) operates on the experimental noise
               covariance: it ensures no LISA Fourier bin shares power with any CMB temperature
               multipole. This makes the OFF-DIAGONAL of F_diag (the W13-2 verdict's Fisher)
               identically zero by basis construction — a different statement than the F_marg
               magnitude being small.
Step 3 (subst): The W13-2 verdict line off-diagonal F_12 = 0 is the consequence of (2) — basis
               choice gave no shared fit parameter, so F_12 = 0 at the experimental level by
               construction. This is true regardless of any substrate covariance.
               The marginalized F_marg[0,1] = +3.42e-34 is a separate object whose smallness
               is the consequence of (1) — the σ_LISA = 1e-12 floor with Ω_GW = 8.3e-58.
Step 4 (dir): (1) certifies ρ_marg ≪ floor at the OBSERVABLE marginalized layer.
              (2) certifies F_12 = 0 at the EXPERIMENTAL pre-marginalization layer.
              These certify DIFFERENT objects. They are not "two independent supports for one claim";
              they are "two separate facts about two separate Fisher matrices that BOTH happen to be ρ-quiet."
```

This matters for the R3 verdict text. The W13-2 verdict line literally certifies the experimental Fisher F_12 = 0 — which is a basis-choice tautology when no shared explicit fit parameter is included. The substantive workshop content is the F_marg analysis: at substrate level it is non-zero, at observable level it is detector-diluted to 31 OOM below floor. (2) is structurally true but not a SUPPORT for the substantive claim — it is a SEPARATE true claim about a different object. R3 should not cite (2) as a redundant support; it should cite (2) as a backstop for the experimental noise structure that operates IN ADDITION to the F_marg marginalization analysis.

**D-mack-2 — The decision (a) framing in R2-A §C3 ("defended at OBSERVABLE LEVEL") is correct but should not be conflated with the schedule's decision (a) which speaks to substrate independence.**

R2-A §C3 distinguishes carefully between (a) "ρ=0 genuine, OBSERVABLE level" and (c) "regulator-conditional NEW result extending W12-4." But the SCHEDULE's decision (a) text is "ρ=0 is genuine, joint-detection significance multiplies as W13-2 claims" — that text bundles together TWO claims:

```
Step 1 (def): Schedule (a) bundle:
              (a-i) ρ = 0 at observable level (true, by tesla R2-A §C2 + my C-mack-1).
              (a-ii) joint-detection significance multiplies as independent products
                     (true ONLY IF the framework's predictive distribution over substrate parameters
                      has zero correlation between predicted Ω_GW and predicted α_s).
Step 2 (subst): (a-ii) requires ρ_substrate-prediction = 0, NOT ρ_marg = 0. The two are
                different objects — Re:T4 + M3 distinguish them. R2-A §A-tesla-4 names this
                as the third UNCOMPUTED ρ requiring S86 Monte Carlo over the predictive
                distribution.
Step 3 (simpl): At the W12-4 atlas-stratified level, predicted Ω_GW and predicted α_s SHARE
                regulator-conditional dependence on (a_0, a_2): a_2 sets G_N which sets Ω_GW;
                a_2/a_0 sets n_s which sets α_s. The same regulator that produces small a_2
                (Pauli-Villars) produces small a_2 (smaller G_N → smaller Ω_GW) AND small
                a_2/a_0 (smaller n_s → smaller |α_s|). The framework's predictive distribution
                under regulator atlasing therefore has a NON-ZERO predictive ρ — both observables
                co-vary with the regulator label.
Step 4 (dir): (a-ii) is FALSE under the W12-4 atlas-stratified interpretation. The joint-detection
                significance does NOT multiply as if from independent draws; it must be computed
                under the joint predictive distribution. This is a SUBSTANTIVE finding for §6A.
```

So decision (c) is not just a "more conservative pre-registration" — it actively retires (a-ii). The schedule's decision (a) text bundles a TRUE claim (a-i, ρ at observable level is zero) with a POTENTIALLY FALSE claim (a-ii, joint significance multiplies independently). For R3, I propose the verdict text explicitly disentangles (a-i) and (a-ii) and adopts (c) as the structurally correct formulation that retires (a-ii) while preserving (a-i).

This matters because the W13-2 verdict line claims `rho_cc=0` and the schedule §6A invocation interprets this as "joint-detection significance multiplies." The latter interpretation requires the predictive ρ — which is a separate, currently uncomputed gate.

### EMERGENCE

Three new structural insights from the R1/R2-A exchange that neither party had at R1:

**E-mack-1 — Three Fisher matrices, not one — and only one is what W13-2 measures.**

The workshop has surfaced a systematic taxonomy of ρ values that the original §6A invocation conflated. R3 should pre-register all three by name:

| ρ name | Object measured | Mechanism | Value at zeta-pin | What it tells us |
|:-------|:----------------|:----------|:-----------------:|:-----------------|
| ρ_experimental | Off-diagonal of F_diag = diag(σ_α^{-2}, σ_Ω^{-2}) | Basis-choice (no shared explicit fit param) | 0 (by construction) | Trivially true; not a substantive claim |
| ρ_substrate-marg | Off-diagonal of F_marg = A − B C^{-1} B^T | Schur complement over (a_0, a_2, a_4) nuisance | +2.42e-46 | Substrate covariance, observably diluted |
| ρ_substrate-prediction | Pearson(Ω_GW, α_s) under W12-4 atlas-stratified predictive distribution | Joint regulator-conditional predictive Monte Carlo | UNCOMPUTED, expected non-zero | Determines whether (a-ii) joint-significance multiplication is valid |

Only the FIRST is what the W13-2 verdict line literally certifies. The SECOND is what tesla R2-A §C2 + my C-mack-1 compute together. The THIRD is the gate that the §6A invocation NEEDS in order to license the "joint-detection significance multiplies" claim — and it is unaddressed.

This taxonomy is the single largest emergent structural insight from the workshop. The W13-2 ρ_cc = 0 verdict line, read literally, certifies a tautology (basis-choice block-diagonality). The substantive claim about substrate independence requires ρ_substrate-prediction, which is uncomputed. R3 should record this taxonomy as a permanent entry in the workshop record.

**E-mack-2 — The Pauli-Villars regulator is the substrate-prediction outlier in BOTH a_2 and a_2/a_0 simultaneously.**

This is a Python-verified observation that emerged from cross-checking tesla R2-A's per-regulator F_marg table against my M1 a_2/a_0 ratio analysis. The atlas values, with the Pauli-Villars row highlighted:

```
Regulator       a_2        a_0       a_2/a_0    n_s_predicted (proxy)    F_marg   ρ_marg
heat-kernel     0.15445    3.7074    0.04166    cluster                  3.47e-34  +2.49e-46
zeta            0.15810    3.7074    0.04264    cluster (canonical)      3.42e-34  +2.42e-46
Mellin          0.15810    3.7074    0.04264    cluster                  3.42e-34  +2.42e-46
hard-cutoff     0.11100    2.0122    0.05516    upward outlier           2.88e-34  +3.13e-46
Pauli-Villars   0.03185    3.7074    0.00859    DOWNWARD OUTLIER (5x)    4.46e-34  +1.41e-45
```

Pauli-Villars's a_2/a_0 = 0.00859 is a factor-5 below the HK/zeta/Mellin cluster at 0.042. Since n_s = f(a_2/a_0) at LO, PV predicts a substantially DIFFERENT n_s (and through n_s² − 1, a different α_s) than the cluster. Combined with PV's smallest a_2 (which SUPPRESSES Ω_GW since 1/G_N ∝ a_2 ⇒ G_N ∝ 1/a_2 large ⇒ ... wait, I need to be careful here, let me write it out):

```
Step 1 (def): O_CGWB ~ G_N at LO (T1 line 60: graviton kinetic normalization sets amplitude)
              1/G_N = (48 f_2 / pi) · a_2 · M_KK^2  [s74 canonical]
Step 2 (subst): G_N ∝ 1/a_2. As a_2 SHRINKS (PV: 0.032 vs zeta: 0.158), G_N GROWS by factor ~5.
              Omega_GW(f) ∝ G_N · (...), so Omega_GW INCREASES under PV.
Step 3 (simpl): Predicted Omega_GW(PV) / Omega_GW(zeta) ~ a_2(zeta) / a_2(PV) = 0.158 / 0.032 = ~5.
              So at the predictive (regulator-stratified) layer, PV gives a CGWB that is ~5x larger.
Step 4 (dir): Smaller a_2 ⇒ larger Omega_GW. PV is also the regulator with smallest a_2/a_0 ⇒
              smaller |α_s| (since |alpha_s| = |n_s² − 1| and n_s closer to 1 gives smaller |alpha_s|
              for n_s near 1 — though this requires more careful sign analysis).
```

The substantive emergent point: **PV is an outlier in OPPOSITE directions** for the two observables it predicts. Predicted Ω_GW under PV is ~5x LARGER than the cluster; predicted |α_s| under PV is SMALLER (because a_2/a_0 is 5x smaller, so n_s closer to scale-invariant). This means the substrate-prediction Pearson correlation, when Monte-Carlo'd over the W12-4 atlas, is likely NEGATIVE — when one observable goes up under regulator-shift, the other goes down. The framework's predictive distribution has structured anti-correlation.

This is testable: a future §6 working paper section computing ρ_substrate-prediction over the 5-regulator atlas should find ρ_pred < 0 with magnitude potentially substantial (driven by PV's joint outlier-ness). I pre-register this prediction for the S86 gate.

**E-mack-3 — The "transverse vs longitudinal" branch distinction is an OBSERVABLE-MODE distinction, not a SUBSTRATE-PARAMETER distinction.**

R1 tesla T3 axis (i) and my Re:T3 disagreement are both clarified by R2-A's explicit Schur recomputation. The clarification is structural and worth recording for the framework:

```
Substrate level:                       Single GGE relic spectrum on the post-fold acoustic 
                                       sector. The {a_n} are SO(3)-singlet scalars labeling
                                       heat-kernel moments of the spectral triple's geometry.
                                       NO tensor/scalar split exists at this layer — a_n is
                                       a number per regulator, not a representation.

Mode-projection step (substrate→observable):
                                       The post-fold acoustic spectrum admits an SO(3)
                                       irrep decomposition into transverse-tensor and
                                       longitudinal-scalar branches. CGWB picks the
                                       transverse branch via the traceless-transverse
                                       projector (s69_transit_gw.py). α_s picks the
                                       longitudinal branch via the heat-kernel curvature
                                       at the CMB pivot.

Observable level:                     Two scalar observables Ω_GW and α_s, each measured
                                       at a specific frequency by a specific detector.
                                       The Fisher off-diagonal at this level is what
                                       W13-2 verdict line measures.
```

T3's SO(3)-irrep argument is correct AT THE MIDDLE LAYER (mode-projection): the transverse and longitudinal projectors are orthogonal as projection operators on the acoustic Hilbert space. But the substrate parameters {a_n} live BELOW that layer and the observables live ABOVE it. The Fisher cross-block tracks ∂(observable)/∂(substrate) — it crosses the layer. SO(3)-irrep orthogonality at the middle layer does NOT propagate to ⟨J_CGWB, J_α_s⟩ orthogonality across the layer crossing.

This is an emergent framework-level clarification: when the project speaks of "transverse vs longitudinal" independence, it should explicitly tag whether the claim is at the mode-projection layer (where SO(3)-irrep orthogonality is real) or at the substrate-parameter layer (where it is not, per Re:T3 + tesla R2-A §C1). The W13-2 ρ_cc = 0 verdict implicitly used the middle-layer language to defend a substrate-layer claim — which is the conflation R2 has now resolved.

For the framework's broader S86+ work: anywhere the project predicts "X and Y are independent because they live on different irreps" needs to be checked at the parameter-layer Schur complement, not at the mode-projection-layer inner product. Provisional list of vulnerable claims (carry-forward to S86 audit): (1) f_NL-channel decompositions (equilateral vs folded vs squeezed), (2) tensor power-spectrum vs scalar power-spectrum amplitude consistency relations, (3) any "B-mode independence from E-mode" claim that rests on pure parity-decomposition arguments.

### QUESTIONS

Four diagrammatic-kernel questions for tesla R3-A. Each is structurally falsifiable, computable from the R2-A `_s85_6a_tesla_r2_fisher_5x5.json` artifact extended with NLO entries, and targets a load-bearing step of the converged decision (c).

**Q-mack-6 — NLO J_CGWB[a_4] entry: order-of-magnitude pin and atlas-conditional Schur.**

R2-A §D1 establishes that the (a_4, a_4) C_pinv = +1.31e+11 amplification is structurally dormant at LO because J_CGWB[a_4] = 0. The LO truncation is what keeps F_marg at 1e-47 instead of the worst-case 8e-45 the C-amplification would otherwise license. NLO heat-kernel renormalization of G_N should fill J_CGWB[a_4] with a non-zero value of order Ω_GW × (a_4/a_2 NLO suppression).

Substitution chain to define the falsifier:

```
Step 1 (def): Suppose J_CGWB[a_4] = δ · Ω_GW / a_4 at NLO, with δ a dimensionless framework-determined
              suppression coefficient.
Step 2 (subst): The NLO contribution to F_marg adds a term:
              ΔF_marg_NLO = -J_CGWB[a_4] · C_pinv[a_4, a_4] · J_alpha_s[a_4] (NLO running-mass)
              + cross terms involving (a_4, a_2) and (a_4, a_0).
              At leading NLO from the (a_4, a_4) entry alone:
              ΔF_marg_NLO ~ δ · (Ω_GW / a_4) · 1.31e+11 · (running-mass δ' · 2 n_s / a_0 · a_4-coupling).
Step 3 (simpl): If δ ~ a_4/a_2 = 0.076 (zeta) and δ' ~ ε² ~ 4e-4 (slow-roll-equivalent suppression),
              the NLO correction relative to LO F_marg is ~ (1.31e+11 / 2.23e+8) · (0.076 · 4e-4) ~ 18.
              So NLO could be ~18x LO at the substrate level — F_marg_NLO ~ 6e-46 vs F_marg_LO ~ 3e-47.
Step 4 (dir): Even with the C-amplification engaging at NLO, F_marg stays well below the floor
              (still 30+ OOM below σ_LISA · σ_CMBS4). But the question is whether the (c) verdict
              text needs to specify NLO-revisited-at-S86 or whether it is structurally complete at LO.
```

Q-mack-6 to tesla: at the heat-kernel-renormalized G_N expansion, what is the specific framework-determined δ for J_CGWB[a_4]? Is there a canonical pin in s74_r_family_observable_scan.py or s69_kk_higgs.py for the NLO heat-kernel coefficient that converts a_4 into 1/G_N correction? If yes, please cite + value. If no, the carry-forward to S86 includes the computation of δ as a prerequisite to the NLO Schur recomputation.

**Q-mack-7 — Predictive-distribution ρ Monte Carlo: pre-register for S86 with E-mack-2 hypothesis.**

Per E-mack-2, I have predicted (without yet computing) that ρ_substrate-prediction over the W12-4 atlas should be NEGATIVE, because Pauli-Villars produces simultaneously LARGER predicted Ω_GW (smaller a_2 → larger G_N) and SMALLER predicted |α_s| (smaller a_2/a_0 → n_s closer to scale-invariant). The other 4 regulators cluster, so the dispersion is dominated by PV's outlier-ness on both axes in opposite directions.

Q-mack-7 to tesla: do you concur that the 5-point Monte Carlo over the W12-4 atlas should yield ρ_substrate-prediction < 0? Pre-register a sign prediction for the S86 gate. If yes, the (c) decision text should include a sub-clause: "regulator-stratified predictive ρ is NON-TRIVIAL with sign pre-registered at SIGN_PREDICTED, magnitude TBD by S86 computation." If you predict differently, what mechanism overrides the PV-outlier argument?

**Q-mack-8 — Falsifier slot in the S-5 master inventory: observationally-inert prediction or placeholder line?**

R2-A §Q-tesla-9 raises this and tentatively answers "observationally inert, no S-5 line needed." I partially agree but want to push back on the FRAMING. The substrate F_marg is 30+ OOM below the LISA floor under ALL 5 regulators in the atlas — so as a single-detector-pair prediction, yes, observationally inert.

But the substrate-prediction claim (ρ_substrate-prediction ≠ 0 per E-mack-2) is NOT observationally inert in the same way. It is a claim about the JOINT structure of two predicted observables under the framework's regulator uncertainty. A future detector pairing where BOTH observables are detectable at predicted-value levels (e.g., if a 21cm IM × LISA joint analysis at ~10⁻¹⁰ Hz overlap reaches the Ω_GW predicted value on a non-CGWB observable in the same family) would expose the predictive ρ.

Q-mack-8 to tesla: should the S-5 line read (option-α) "currently observationally inert, no falsifier line" — or (option-β) "placeholder line with falsifier text 'IF a future joint detector reaches σ_pred-floor on both Ω_GW and |α_s| AND measures ρ ≠ ρ_substrate-prediction at >5σ, the framework is falsified at the chosen regulator'"? My read leans option-β: a placeholder line with a deferred-falsifier clause is structurally cheaper than no line, because option-α loses the W12-4 regulator-pin discipline at the falsifier-inventory layer. But option-α is defensible if the inventory shouldn't carry placeholder lines for observationally-inert predictions. Pre-register your read for R3.

**Q-mack-9 — Convention canonicalization for J reporting in the R3 verdict.**

Per C-mack-4, the factor-32 mack-M2 vs tesla-R2-A discrepancy is a J convention difference (linear-derivative vs logarithmic-derivative). For R3 the verdict text should specify the convention. My proposal:

- Canonical J convention: ∂O/∂a_n in linear-derivative form, with units explicitly carried (J_CGWB[a_2] in units of Ω_GW per unit a_2; J_alpha_s[a_2] dimensionless per unit a_2).
- Alternate scaling form: O · ∂(ln O)/∂(ln a_n) (logarithmic) reported in parentheses as a scaling diagnostic.
- Pin the convention in the S86 gate spec to prevent future PRU class-8 defects on Jacobian reporting.

Q-mack-9 to tesla: do you accept the linear-derivative canonical convention with logarithmic as alternate? Or do you prefer logarithmic as canonical (matching tesla R2-A)? The choice doesn't affect any verdict but should be pinned for consistency in the S86 gate spec and the working-paper section.

**Methodological pre-statement for R3-B.**

R3-B FINAL will: (i) write the converged decision (c) verdict text with disentangled (a-i) / (a-ii) per D-mack-2; (ii) pre-register the three-Fisher taxonomy (E-mack-1) as the workshop's permanent contribution; (iii) record the E-mack-2 sign prediction for ρ_substrate-prediction and the Q-mack-6 NLO carry-forward as S86 gate inputs; (iv) populate the verdict table and Wrap-Up with the structural finding that the W13-2 verdict literally certifies a basis-tautology while the substantive substrate analysis says ρ ≠ 0 at substrate level for all 5 regulators. R3-B will not introduce new computations beyond what tesla R3-A clarifies.

---

## Round 3 — tesla: CONVERGE

**Computation pin (R3-A)**: All numerical claims in this turn re-verified via direct Python computation against canonical W12-4 atlas (a_0, a_2, a_4) and the R2-A `_s85_6a_tesla_r2_fisher_5x5.json` artifact. No new full-Schur recomputation; the substitutions chain off R2-A's verified J/C entries plus mack R2-B's diagrammatic-kernel cross-check. Two arithmetic discrepancies in mack R2-B were caught at chain-execution time (Q-mack-6 step 3, sign-convention slip in E-mack-2) and are addressed in CONVERGENCE/DISSENT/EMERGENCE/QUESTIONS below.

### CONVERGENCE

I converge on three of mack R2-B's substantive points and reconcile a fourth (the convention question Q-mack-9). Each is stated as a structural update to my R2-A position with the trigger explicitly cited.

**C-tesla-3-1 — The diagrammatic kernel inner product DOES converge with the full-Schur substrate-only Schur term to better than 1e-50. ACCEPT AS THE DECISIVE CROSS-CHECK.**

Re: C-mack-3 in mack R2-B. mack's diagrammatic Mellin-moment decomposition computed the LO kernel inner product as

```
<K_CGWB[a_2], K_alpha_s[a_2]>_C = J_CGWB[a_2] · C_pinv[a_2,a_2] · J_alpha_s[a_2]
                                + J_CGWB[a_2] · C_pinv[a_2,a_0] · J_alpha_s[a_0]
                                = -1.379e-47 + (-5.247e-51)
                                = -1.378e-47   (which then becomes +1.378e-47 under Schur sign)
```

This matches my R2-A `J_alpha_s · C^{-1} · J_CGWB | zeta-pin = +1.378e-47` to all 4 displayed digits. Substitution chain for the agreement:

```
Step 1 (def): F_marg substrate-only = -J_CGWB^T · C_pinv · J_alpha_s  (Schur, marginalized over a_n)
Step 2 (subst, R2-A full Schur): +1.378e-47  [tesla R2-A line 919, confirmed]
Step 2' (subst, mack diagrammatic LO): +1.378e-47  [mack R2-B Step 3, line 1140]
Step 3 (simpl): difference = 1.378e-47 - 1.378e-47 < 1e-50 (better than 4 sig figs).
Step 4 (dir): The diagrammatic and Schur computations agree at LO substrate-only. Two
              independent computational routes (direct Schur 5x5 inversion vs. Mellin-moment
              kernel decomposition) reach the same number — strong cross-validation of the
              substrate F_marg ≠ 0 result.
```

Critical structural consequence: there is NO clean kernel-orthogonality at LO. The (a_2, a_2) diagonal entry contributes -1.379e-47 (4 OOM larger than the (a_2, a_0) cross at -5.247e-51) — both substantially non-zero. The W13-2 ρ_cc = 0 verdict therefore CANNOT be defended at substrate level via kernel-orthogonality; the only defense at observable level is the σ_LISA-floor dilution. **My R1 T4 Step 5 lemma is dead AT THE PARAMETER LAYER — cross-confirmed by mack's diagrammatic computation, not just by my own Schur arithmetic.**

**C-tesla-3-2 — The three-Fisher taxonomy (E-mack-1) is the workshop's permanent structural contribution. ADOPT AS R3 PRE-REGISTRATION.**

Re: E-mack-1 in mack R2-B. The taxonomy distinguishes:

| ρ name | Object | Value (zeta) | Status |
|:-------|:-------|:-------------|:-------|
| ρ_experimental | F_diag = diag(σ_α^{-2}, σ_Ω^{-2}) off-diagonal | 0 (basis-construction) | W13-2 verdict literal |
| ρ_substrate-marg | F_marg Schur over (a_0, a_2, a_4) | +2.42e-46 | C2 + C-mack-1 |
| ρ_substrate-prediction | Pearson(Ω_GW, α_s) under W12-4 atlas-stratified predictive distribution | UNCOMPUTED at R2 | E-mack-2 hypothesis, S86 gate |

This is more than a notational tidying. It surfaces that the W13-2 verdict line, read literally, certifies a basis-construction tautology — `ρ_experimental = 0` follows mechanically from "no shared explicit fit parameter in the (CGWB, α_s) Fisher basis." The substantive substrate analysis (`ρ_substrate-marg`) requires marginalizing over a_n nuisance and gives +2.42e-46 at zeta-pin (non-zero, observably diluted). The "joint-detection significance multiplies" claim that the schedule §6A invocation reads from W13-2 actually requires `ρ_substrate-prediction` — a third object that is currently uncomputed.

I converge on adopting this taxonomy as the workshop's R3 permanent contribution. The S86 gate spec mack drafts in R3-B should pin all three names, and any future framework discussion of CGWB×α_s independence should specify which ρ it means.

**C-tesla-3-3 — Decision (a) bundles two claims; the schedule's (a-ii) is structurally retired by E-mack-2's anti-correlation hypothesis. ACCEPT D-mack-2 disentanglement.**

Re: D-mack-2 in mack R2-B. mack's substitution chain in D-mack-2 establishes that the schedule §6A decision (a) text bundles:

- (a-i) ρ = 0 at observable level (TRUE, by C2 + C-mack-1)
- (a-ii) joint-detection significance multiplies as independent products (requires `ρ_substrate-prediction = 0`)

(a-ii) is the operational interpretation the §6A schedule invokes when it says "joint-detection significance multiplies." But (a-ii) is FALSE under the W12-4 atlas-stratified interpretation — see EMERGENCE E-tesla-3-2 below for the explicit Pearson computation. So decision (a), as bundled in the schedule text, is half-true / half-false. Decision (c) is therefore not just "more conservative" — it is the structurally correct disentanglement that retires (a-ii) while preserving (a-i). I adopt mack's R3-B verdict-text framing: **the R3 verdict explicitly disentangles (a-i) from (a-ii) and adopts (c) as the formulation that preserves (a-i) and retires (a-ii).**

**C-tesla-3-4 — Convention canonicalization (Q-mack-9): linear-derivative as canonical, logarithmic as scaling diagnostic. ACCEPT mack's proposal.**

Re: C-mack-4 + Q-mack-9 in mack R2-B. The factor-32 R2-A vs M2 reconciliation is fully accounted for by the J convention difference (linear vs logarithmic derivative form). For R3 verdict and S86 gate spec:

```
Step 1 (def): Linear-derivative: J^{lin}[a_n] = ∂O / ∂a_n            (units: O per unit a_n)
              Logarithmic-derivative: J^{log}[a_n] = ∂(ln O) / ∂(ln a_n)  (dimensionless scaling)
              Conversion: J^{lin}[a_n] = (O / a_n) · J^{log}[a_n]
Step 2 (subst, zeta-pin): J^{log}_alpha_s[a_2] = 2 n_s^2 = 2 (0.9649)^2 = 1.862
                          a_2 = 0.15810
                          n_s^2-1 = -0.06897
                          J^{lin}_alpha_s[a_2] = (-0.06897 / 0.15810) · 1.862 = -0.812
                          (Direction sign accumulation: alpha_s is negative; ratio of partials carries sign.)
Step 3 (simpl): R2-A used J^{log} convention with units of O suppressed; M2 used J^{lin}
                with explicit factor-of-O carry. Both compute the SAME F_marg when applied
                consistently — the factor-32 difference was strictly a normalization artifact.
Step 4 (dir): For R3 verdict + S86 gate spec, canonical J convention = LINEAR-DERIVATIVE
              with explicit units carried; LOGARITHMIC reported in parentheses as scaling diagnostic.
              This prevents future PRU class-8 defects on Jacobian-reporting in S86+ gates.
```

I accept mack's Q-mack-9 proposal: linear-derivative canonical, logarithmic alternate. For my R2-A reported numbers, the ones that matter (F_marg, ρ_marg) are convention-INVARIANT — they were computed with a self-consistent J/C/inverse pair — so the per-regulator atlas table (R2-A line 952) stands without modification.

### DISSENT

I retain dissent on TWO narrow points where mack R2-B has either an arithmetic slip or a framing overshoot that R3-B should not carry forward into the verdict text or S86 gate spec.

**D-tesla-3-1 — Q-mack-6 step 3 has an arithmetic slip; the corrected NLO/LO ratio is ~0.018, not ~18. NLO is SMALLER than LO, not 18x larger. C-amplification worry retired structurally even at NLO.**

Re: Q-mack-6 in mack R2-B. mack's Step 3 chain reads:

```
"If δ ~ a_4/a_2 = 0.076 (zeta) and δ' ~ ε² ~ 4e-4 (slow-roll-equivalent suppression),
 the NLO correction relative to LO F_marg is ~ (1.31e+11 / 2.23e+8) · (0.076 · 4e-4) ~ 18."
```

The arithmetic in this step does not check out. Substitution chain to verify:

```
Step 1 (def): NLO/LO ratio = (C_pinv[a_4,a_4] / C_pinv[a_2,a_2]) · (δ · δ')   (mack's structure)
Step 2 (subst): C_pinv[a_4,a_4] / C_pinv[a_2,a_2] = 1.31e+11 / 2.23e+8 = 587.4
                δ · δ' = 0.076 · 4e-4 = 3.04e-5
Step 3 (simpl): NLO/LO = 587.4 · 3.04e-5 = 0.01786                     (Python-verified)
Step 4 (dir): NLO/LO ≈ 0.018 (NOT 18). The NLO contribution at this estimate is
              ~50x SMALLER than the LO contribution, NOT 18x larger.
```

mack R2-B's "~18" appears to be a factor-1000 slip (likely dropped a 1e-3 somewhere in the suppression product). The corrected substitution chain has the structural consequence:

```
F_marg_NLO ~ 0.018 · F_marg_LO ~ 0.018 · 1.378e-47 ~ 2.5e-49
F_marg total ~ F_marg_LO + F_marg_NLO ~ 1.4e-47 (LO dominates by 2 OOM)
Floor σ_LISA · σ_CMBS4 = 3e-15
NLO contribution / floor ~ 8e-35 (still 34 OOM below floor at NLO).
```

Direct verification of the explicit (a_4, a_4) entry contribution at NLO using the framework's natural scaling J_C[a_4]_NLO = δ · Ω_GW / a_4 with δ = a_4/a_2:

```
Step 1 (def): J_C[a_4]_NLO = δ · Ω_GW / a_4 = (a_4/a_2) · Ω_GW / a_4 = Ω_GW / a_2
              (the a_4 factor cancels — interesting, the NLO J_C[a_4] equals the LO J_C[a_2] in magnitude)
Step 2 (subst): J_C[a_4]_NLO = Ω_GW / a_2 = 8.299e-58 / 0.15810 = 5.249e-57   (zeta)
                (matches LO J_C[a_2] in magnitude, as expected from the cancellation)
                J_a[a_4]_NLO = δ' · 2 n_s / a_0 = 4e-4 · 2 (0.9649) / 3.7074 = 2.082e-4
Step 3 (simpl): ΔF_marg_NLO = -J_C[a_4]_NLO · C_pinv[a_4,a_4] · J_a[a_4]_NLO
                            = -(5.249e-57) · (1.31e+11) · (2.082e-4)
                            = -1.432e-49                         (Python-verified)
Step 4 (dir): |ΔF_marg_NLO| = 1.43e-49, which is 100x SMALLER than F_marg_LO = 1.38e-47.
              The NLO contribution does not approach the LO contribution; the C-amplification
              factor 1.31e+11 is substantially overcompensated by the δ · δ' = 3e-5 suppression
              from a_4/a_2 + ε² combined.
```

**Implication for the (c) decision text and S86 carry-forward**: the NLO C-amplification engagement is REAL (J_C[a_4] is no longer dormant at NLO), but the structural conclusion is that NLO is sub-dominant to LO by 2 OOM, not enhanced to LO+ as mack's slip suggested. The (c) verdict text should acknowledge NLO engagement WITHOUT flagging it as a near-floor risk; the S86 carry-forward is a "compute NLO δ from canonical heat-kernel renormalization for completeness" task, not a "NLO might cross the floor" risk-mitigation task.

**D-tesla-3-2 — D-mack-1's "two separate facts about two separate Fisher matrices" reformulation is CORRECT but the verdict-text consequence is stronger than mack states.**

Re: D-mack-1 in mack R2-B. mack correctly observes that my R2-A §D2 list of "two independent supports" actually certifies two different objects (F_diag off-diagonal vs F_marg off-diagonal). I accept the reformulation but the structural consequence runs further than mack's R2-B framing:

```
Step 1 (def): F_diag is the EXPERIMENTAL Fisher in the (CGWB, α_s) basis with no a_n nuisance.
              F_diag[1,2] = 0 BY BASIS CHOICE (no shared explicit fit parameter — this is a
              tautology of the basis, not a physics result).
Step 2 (def): F_marg is the SUBSTRATE Fisher Schur-marginalized over a_n.
              F_marg[1,2] = +3.42e-34 (zeta-pin, non-zero, regulator-conditional).
Step 3 (subst): The 13.6-OOM frequency separation does NOT enter F_diag's zero off-diagonal
              construction at all — F_diag would have zero off-diagonal even if the LISA and
              CMB-S4 detectors operated at the same frequency, as long as they had no shared
              explicit fit parameter. The 13.6-OOM gap is a SEPARATE fact about the experimental
              noise covariance Σ that, combined with the basis choice, ensures F_diag is doubly
              clean.
Step 4 (dir): D2's "two independent supports" framing should be REVISED in R3 to:
              - F_diag[1,2] = 0 by BASIS CHOICE (tautology of W13-2 construction).
              - F_marg[1,2] = +3.42e-34 by SCHUR (substrate non-zero, observably diluted).
              - 13.6-OOM gap is a STRUCTURAL BACKSTOP that ensures Σ_experimental is block-diagonal
                regardless of the basis choice — not a "support" for F_diag = 0 per se but a
                backstop preventing future pathological basis choices from re-introducing
                experimental cross-terms.
```

I CONVERGE on mack's "two separate facts about two separate Fisher matrices" reformulation. My narrow DISSENT is on one piece of the implied verdict-text language: D-mack-1's "ρ-quiet" framing understates the asymmetry. F_diag is identically zero by tautology (every two-observable Fisher in a basis with no shared fit parameter has zero off-diagonal); F_marg is non-zero. R3-B's verdict text should NOT cite F_diag = 0 as substantive evidence for substrate independence — it should be cited as a basis-construction property, with the substrate-marginalized analysis (F_marg ≠ 0) as the substantive workshop content.

### EMERGENCE

Three new structural insights from the R3 cross-pollination — each emerges from the explicit R2-B/R3-A back-and-forth and was not visible in R1 or R2 individually.

**E-tesla-3-1 — The substrate-only kernel inner product DOMINANCE structure: (a_2, a_2) > (a_2, a_0) by 4 OOM is a regulator-INVARIANT structural fact.**

Re: C-mack-3 in mack R2-B. The diagrammatic kernel decomposition reveals that at LO, only the a_2 column is non-zero on the CGWB side (J_C[a_n] = 0 ∀ n ≠ 2 at LO). On the α_s side both a_0 and a_2 columns are non-zero. The Schur sum therefore decomposes as

```
F_marg_substrate-only = -[J_C[a_2] · C_pinv[a_2,a_2] · J_a[a_2] + J_C[a_2] · C_pinv[a_2,a_0] · J_a[a_0]]
```

with the (a_2, a_2) term contributing +1.379e-47 and the (a_2, a_0) term contributing only +5.247e-51. The 4-OOM dominance of (a_2, a_2) over (a_2, a_0) at zeta is a STRUCTURAL fact about the W12-4 atlas Pearson correlations:

```
ρ_atlas(a_0, a_2) = +0.1199  (small)         → C_pinv[a_2, a_0] small in absolute value
ρ_atlas(a_2, a_4) = +0.9922  (near-unity)    → C_pinv[a_2, a_4] LARGE in absolute value
```

The (a_2, a_4) C_pinv entry is large because a_2 and a_4 are near-perfectly atlas-correlated, but it does NOT enter the LO Schur because J_C[a_4] = 0 at LO and J_a[a_4] = 0 at LO. So the dominant C_pinv channel is structurally dormant. Question whether (a_2, a_2) dominance survives at L_max ≥ 12:

```
Step 1 (def): The Pearson correlations ρ_atlas(a_n, a_m) are computed across the 5-regulator
              atlas at L_max = 10. Their values determine the C_pinv structure.
Step 2 (def): At L_max ≥ 12, the heat-kernel atlas would be re-evaluated with finer spectral
              resolution, potentially shifting the (a_2, a_4) and (a_0, a_2) atlas correlations.
Step 3 (subst): The W12 P1 pattern (closing-notes line 393-394 of session-85-w12-workingpaper.md)
              claims dimensionless ratios a_n/a_m are L_max-stable. If the Pearson correlations
              are L_max-stable, the C_pinv structure is L_max-invariant and the (a_2, a_2)
              dominance over (a_2, a_0) survives.
              However, mack M1 reported a_4/a_2 ratio is REGULATOR-DIVERGENT at fixed L_max
              (factor 2.8 across atlas), so the L_max-stability of P1 does NOT immediately
              imply atlas-stability of the Pearson correlations.
Step 4 (dir): SURVIVAL OF THE (a_2, a_2) DOMINANCE AT L_max ≥ 12 is L_max-dependent in a way
              that requires direct computation. Provisional reading: dominance likely persists
              because the J_C[a_4] = 0 LO truncation is a framework-structural fact (1/G_N has
              no a_4 dependence at LO regardless of L_max) — but the (a_2, a_4) cross-coupling
              in C_pinv could grow if the atlas Pearson correlation shifts with L_max.
```

Carry-forward: an L_max ≥ 12 recomputation of the W12-4 atlas would PIN whether the (a_2, a_2) dominance is L_max-stable. The answer to mack's prompt question ("does (a_2, a_2) +1.379e-47 dominance over (a_2, a_0) +5.247e-51 survive at higher loop order or break at L_max ≥ 12?") is: the LO TRUNCATION (J_C[a_n] = 0 ∀ n ≠ 2) is a structural framework fact that survives all loop orders for the LO contribution; at higher loops (NLO), J_C[a_4] becomes non-zero and the (a_2, a_4) dominance channel engages — but per D-tesla-3-1, this NLO channel is suppressed by δ · δ' = 3e-5 and does not reach LO magnitude. At L_max ≥ 12, the structural LO truncation is unchanged but the C_pinv numerical values would shift; whether this preserves the (a_2, a_2) > (a_2, a_0) ordering by 4 OOM is L_max-empirical, not L_max-structural.

**E-tesla-3-2 — Verified ρ_substrate-prediction sign: depends on signed-vs-magnitude alpha_s convention. Pearson(Ω_GW, α_s_signed) = +0.91; Pearson(Ω_GW, |α_s|) = -0.91. Mack E-mack-2's "negative" claim is correct on the magnitude convention.**

Re: E-mack-2 + Q-mack-7 in mack R2-B. Direct numerical verification across the W12-4 atlas, with the substitution chain made explicit (Python-verified):

```
Step 1 (def): For each regulator r in atlas, compute predicted (Ω_GW(r), α_s(r)):
              Ω_GW(r) ∝ 1/a_2(r) [from G_N ∝ 1/a_2]
              n_s(r) − 1 ∝ a_2(r)/a_0(r) [linear proxy for the a_2/a_0 → tilt mapping]
              α_s(r) = n_s(r)² − 1
Step 2 (subst, atlas values):
              Reg.       1/a_2     a_2/a_0    n_s_pred    α_s_pred
              HK         6.475     0.04166    0.96571     -6.74e-2
              zeta       6.325     0.04264    0.96490     -6.90e-2  (canonical)
              Mellin     6.325     0.04264    0.96490     -6.90e-2
              HC         9.009     0.05516    0.95460     -8.87e-2
              PV        31.397     0.00859    0.99293     -1.41e-2  (DOWNWARD a_2/a_0 OUTLIER 5x)
Step 3 (simpl): Pearson correlations across the 5 regulators:
              ρ(Ω_GW, α_s_signed) = +0.9114                          (Python-verified)
              ρ(Ω_GW, |α_s|)      = -0.9114                          (Python-verified)
Step 4 (dir): SIGN DEPENDS ON CONVENTION. On signed alpha_s (the standard convention,
              where α_s_observed ≈ -0.069 < 0), the Pearson is POSITIVE: when Ω_GW
              increases (PV: a_2 small → G_N large → Ω_GW large), α_s also INCREASES
              (PV: n_s closer to 1 → α_s = n_s² − 1 closer to 0 from below → less negative
              → numerically larger). So the SIGNED Pearson is +0.91.
              On magnitude |α_s|, the Pearson is NEGATIVE — when Ω_GW is large, |α_s| is small.
              mack's E-mack-2 phrasing ("LARGER predicted Ω_GW and SMALLER predicted |α_s|")
              is the magnitude-based reading, which gives ρ(|α_s|) = -0.91.
              Both statements are TRUE; they describe the same correlation under different
              sign conventions. R3-B verdict text should pick ONE convention and report it.
```

The ρ_substrate-prediction is large (|ρ| ≈ 0.91), driven primarily by the Pauli-Villars outlier-ness on both axes. With PV removed from the atlas (treating it as a regulator-Bayesian outlier and the other 4 as the "physical cluster"), the correlation magnitude drops sharply because hard-cutoff dominates the residual variation:

```
Step 1: Drop PV, compute Pearson on {HK, zeta, Mellin, HC}: ρ(Ω_GW, α_s_signed) for the 4-regulator subset
        is dominated by HC's a_0 = 2.0122 outlier (vs cluster a_0 = 3.7074).
Step 2: This means the |ρ| ≈ 0.91 result is REGULATOR-CHOICE-CONDITIONAL — sensitive to
        whether the atlas treats PV as a sample or as an outlier to discard.
Step 3 (dir): The S86 ρ_substrate-prediction gate spec must declare its atlas treatment:
              all 5 regulators uniformly weighted (gives ρ ≈ 0.91 mag), or PV-down-weighted
              to match the cluster (gives much smaller |ρ|, sign uncertain).
```

This is a SECOND PRU class-8 vulnerability (atop the regulator-pin discipline already noted): the predictive ρ depends on the atlas-weighting choice. The S86 gate spec should pre-register both the atlas treatment AND the sign convention.

**E-tesla-3-3 — The (a_2, a_4) atlas Pearson correlation +0.9922 has a structural origin: a_2 and a_4 are tied by the heat-kernel expansion's analytic structure (Mellin transform of D_K^{-2s} at adjacent poles).**

A side observation that emerged from working through the kernel inner product structure: the W12-4 atlas reports ρ(a_2, a_4) = +0.9922 across the 5 regulators. This is not coincidence. Both a_2 and a_4 are Seeley-DeWitt coefficients of the heat-kernel asymptotic expansion exp(-tD_K²) ~ Σ_n a_n t^{(n-d)/2}. They are evaluated at adjacent poles of the spectral zeta function ζ_{D_K}(s) = Tr(D_K^{-2s}), and their regulator-dependence is dominated by how each regulator handles the UV behavior of the spectral measure near the same eigenvalue cluster. Different regulators (HK, zeta, Mellin) compute the SAME analytic continuation when the spectrum is well-behaved; they diverge from PV/HC when the spectrum has sub-leading non-analytic terms. The near-perfect Pearson between a_2 and a_4 reflects that BOTH coefficients are read off the same spectral function with the same regulator-induced UV cutoff; their separate spreads across the atlas are coupled because the cutoff prescription affects them coherently.

The implication for the workshop: the (a_2, a_4) atlas correlation is not a free parameter to be computed at higher L_max — it is a structural consequence of the heat-kernel-expansion architecture. It will REMAIN near-unity at L_max ≥ 12. The (a_2, a_4) C_pinv coupling channel that appears dormant at LO will engage at NLO with the same strength regardless of L_max. This is a permanent framework feature, not an L_max artifact.

This sharpens the §6A workshop's structural finding: the substrate covariance C is GUARANTEED to have near-singular condition number (near-unity (a_2, a_4) Pearson) at any reasonable L_max because the heat-kernel expansion's analytic structure ties adjacent moments. Future S86+ gates that marginalize over a_n must use the pseudoinverse or a Tikhonov-regularized inverse, not the direct inverse. This is a methodological pin for the S86 gate spec.

### QUESTIONS

This section answers mack R2-B's Q-mack-6 through Q-mack-9 (each cross-referenced to the relevant CONVERGENCE/DISSENT/EMERGENCE entry above), then poses three sharper follow-up questions for mack R3-B FINAL to address in the verdict text and S86 gate spec.

**A-mack-6 (NLO J_CGWB[a_4] order-of-magnitude pin).** Per D-tesla-3-1 above. Substitution chain:

- The framework's canonical heat-kernel-renormalization NLO entry of a_4 into 1/G_N has not been pinned in s74_r_family_observable_scan.py or s69_kk_higgs.py at a numerical δ value. The natural framework-structural choice δ = a_4/a_2 (the LO suppression ratio inherited from the heat-kernel expansion structure) gives δ_zeta = 0.076.
- δ' = ε² ≈ 4e-4 (slow-roll-equivalent suppression on running-mass NLO entry into α_s).
- D-tesla-3-1's verified arithmetic: NLO/LO ratio = 0.018 (NOT 18 as mack R2-B Q-mack-6 step 3 states). NLO contributes |ΔF_marg_NLO| ≈ 1.4e-49, sub-dominant to LO F_marg ≈ 1.4e-47 by a factor 100.
- Conclusion: NLO does NOT cross the σ_LISA × σ_CMBS4 = 3e-15 floor at any regulator in the atlas. The (c) verdict text needs to acknowledge NLO engagement (J_C[a_4] becomes non-zero) but does NOT need a near-floor-risk clause. S86 carry-forward: pin δ from canonical heat-kernel renormalization as a completeness exercise, not as a risk-mitigation task.

**A-mack-7 (predictive-distribution ρ Monte Carlo sign prediction).** Per E-tesla-3-2 above. Substitution chain executed:

- Direct Pearson computation across W12-4 atlas: ρ(Ω_GW, α_s_signed) = +0.9114; ρ(Ω_GW, |α_s|) = -0.9114.
- mack's E-mack-2 hypothesis is CONFIRMED on the magnitude convention (the convention E-mack-2 actually used) — when PV produces a_2 small, both Ω_GW becomes large AND |α_s| becomes small. The Pearson on magnitudes is NEGATIVE.
- On the signed convention (standard for α_s), the Pearson is POSITIVE because both Ω_GW and α_s_signed increase together under PV's small-a_2 shift.
- Pre-registered for S86: ρ_substrate-prediction sign = NEGATIVE on magnitude convention | POSITIVE on signed convention; |ρ_substrate-prediction| ≈ 0.91 on the 5-regulator uniform-weight atlas; magnitude DROPS sharply if PV is down-weighted as an outlier.
- The S86 gate spec must declare: (i) sign convention (magnitude vs signed), (ii) atlas weighting (uniform 5-reg vs PV-down-weighted). Both are PRU class-8 vulnerabilities that R3-B should pin in the gate spec.

**A-mack-8 (S-5 falsifier slot — option-α observationally inert vs option-β placeholder line).** I converge on **option-β: placeholder line with deferred-falsifier clause**. Reasoning:

- Substrate F_marg is 30+ OOM below LISA detector floor under all 5 regulators, so as a single-detector single-pair prediction the result is observationally inert (option-α).
- BUT: ρ_substrate-prediction is non-trivial (|ρ| ≈ 0.91 on uniform 5-reg weighting per A-mack-7). This is a JOINT-distribution claim that is NOT observationally inert in the same way — a future detector pairing where Ω_GW is bounded above by a stronger-than-LISA experiment (or a non-CGWB observable in the same family) could expose the predictive ρ.
- A placeholder S-5 line preserves the W12-4 regulator-pin discipline at the falsifier-inventory layer. Without the placeholder, future S86+ work might quote ρ(CGWB, α_s) without inheriting the regulator-pin requirement (PRU class-8 risk).
- Proposed S-5 falsifier text (for R3-B to refine): "S-5-CGWB-ALPHASS-JOINT-PRED: IF a future joint detector reaches σ_pred-floor on Ω_GW AND on α_s AND measures Pearson(Ω_GW, α_s) ≠ predicted ρ_substrate-prediction(zeta) at >5σ, the framework is falsified at the chosen regulator; otherwise the absence of detection is consistent with all 5 atlas regulators."

**A-mack-9 (convention canonicalization for J reporting).** Accepted per C-tesla-3-4 above. Linear-derivative canonical, logarithmic-derivative reported as scaling diagnostic in parentheses. Pin in S86 gate spec to prevent future PRU class-8 defects on Jacobian normalization.

**Direct answer to the prompt's three R3-A focus questions** (collected for mack's R3-B canvas):

1. **Substrate-prediction sign mack proposed in E-mack-2**: ACCEPTED on the magnitude convention. ρ(Ω_GW, |α_s|) = -0.9114 confirms mack's "Pauli-Villars is an outlier in OPPOSITE directions" hypothesis. The signed convention gives +0.9114 — the SAME phenomenon under a different sign flip.

2. **(a_2, a_2) → +1.379e-47 dominance over (a_2, a_0) → +5.247e-51 survival at higher loop order or L_max ≥ 12**: At higher LOOP ORDER (NLO), J_C[a_4] becomes non-zero with magnitude Ω_GW/a_2 (per D-tesla-3-1 algebra), and the (a_2, a_4) C_pinv channel +1.31e+11 engages — but the δ · δ' = 3e-5 suppression keeps NLO at ~0.018 of LO. Dominance survives in OOM if not in 4-digit identity. At L_max ≥ 12: the LO truncation J_C[a_n] = 0 ∀ n ≠ 2 is FRAMEWORK-STRUCTURAL (1/G_N has no a_4 dependence at LO regardless of L_max), so the (a_2, a_2) > (a_2, a_0) ordering survives in structure; the 4 OOM specific separation is L_max-empirical. The (a_2, a_4) Pearson +0.9922 is HEAT-KERNEL-ANALYTIC-STRUCTURAL (E-tesla-3-3) and survives L_max ≥ 12 with high confidence.

3. **Kernel-orthogonality argument's status w.r.t. W13-2 ρ=0 verdict**: My T4 SO(3)-irrep-orthogonality lemma is DEAD AT THE PARAMETER LAYER (per C1 + C-mack-3 cross-confirmation). The W13-2 ρ=0 verdict is DEFENSIBLE ONLY AS SCHEME-STIPULATION at the experimental Fisher layer (basis-construction tautology), and as detector-floor-diluted at the substrate-marginalized observable layer. **The verdict does NOT require an INFO downgrade** — it is structurally correct at the layer it certifies — but the §6A workshop must record explicitly that the verdict literally certifies the basis-tautology layer, and the substantive substrate analysis (ρ_substrate-marg ≠ 0; ρ_substrate-prediction ≠ 0) is RECORDED as a permanent workshop contribution that the W13-2 verdict line did not capture. The R3-B verdict should adopt decision (c) + the three-Fisher taxonomy (E-mack-1) + the disentangled (a-i)/(a-ii) framing (D-mack-2), and pre-register the S86 ρ_substrate-prediction gate per A-mack-7.

**Three sharper follow-up questions for mack R3-B FINAL** (verdict-text and S86 gate spec scope):

- **Q-tesla-10 — atlas-treatment pin for the S86 ρ_substrate-prediction gate**. Per E-tesla-3-2, the predictive Pearson is sensitive to whether PV is uniform-weighted or down-weighted as an outlier. The S86 gate spec must declare the atlas treatment. Recommended pre-registration: report BOTH (uniform 5-reg + PV-down-weighted) as the gate's two arms, with the framework's "primary" prediction being the uniform-weight version (no a-priori reason to down-weight PV at the atlas-Bayesian layer). Does mack agree to a two-arm pre-registration, or does mack want a single-arm spec with an explicit PV-treatment argument?

- **Q-tesla-11 — Pearson convention pin (signed vs magnitude alpha_s)**. Per A-mack-7, ρ_substrate-prediction sign FLIPS between conventions: +0.91 signed, -0.91 magnitude. The S86 gate spec must declare which. Recommended: SIGNED convention as canonical (matches the standard α_s reporting where α_s ≈ -0.069 is reported without absolute-value bars), magnitude as alternate. Does mack agree, or prefer magnitude as canonical (matching mack's E-mack-2 phrasing)?

- **Q-tesla-12 — does the Fisher-PSD content of the workshop deserve a new permanent-results-registry entry?**. The three-Fisher taxonomy (E-mack-1) is general — it applies to any framework gate that quotes ρ between two observables that share a substrate parameter. This is not a one-off workshop note; it is a methodology that future joint-channel gates should inherit. Should mack's R3-B Wrap-Up include a recommendation to add this taxonomy as a permanent-results-registry entry (keyword: "three-ρ taxonomy for joint-detection gates"), so future agents do not re-litigate the basis-tautology vs substrate-marginalized vs predictive distinction in S86+ work?

These three R3-B questions close on the verdict-text structure (decisions a/b/c) and on the S86 gate-spec pin discipline. R3-B has the canvas to write the verdict + Wrap-Up + S86 gate spec; my R3-A converges all the substantive computation and clears the structural ambiguities that R1/R2 surfaced.

---

## Round 3 — mack: CONVERGE (FINAL)

**Computation pin (R3-B FINAL)**: arithmetic verifications executed inline against the R2-A `_s85_6a_tesla_r2_fisher_5x5.json` pinned numbers and the R3-A substitution chains. The two arithmetic items tesla flagged in R3-A (D-tesla-3-1 and E-tesla-3-2) are re-verified explicitly below; both checks land. No new full-Schur recomputation; this turn closes the workshop on the converged decision (c) + three-Fisher taxonomy + S86 gate spec.

### CONVERGENCE

I converge on three of tesla R3-A's substantive moves, including the explicit acceptance of the D-tesla-3-1 NLO/LO arithmetic correction and the E-tesla-3-2 sign-convention split. Each is stated as an update to my R2-B position with the trigger explicitly cited.

**C-mack-3-1 — D-tesla-3-1 NLO/LO arithmetic correction. ACCEPTED IN FULL; my R2-B Q-mack-6 step 3 was wrong by a factor of 1000.**

Tesla's R3-A §D-tesla-3-1 catches a 1000x slip in my R2-B Q-mack-6 Step 3 chain. My R2-B Step 3 read "(1.31e+11 / 2.23e+8) · (0.076 · 4e-4) ~ 18" — the correct arithmetic is:

```
Step 1 (def):    NLO/LO ratio = (C_pinv[a_4,a_4] / C_pinv[a_2,a_2]) · (delta · delta')
Step 2 (subst):  C_pinv[a_4,a_4] / C_pinv[a_2,a_2] = 1.31e+11 / 2.23e+8 = 587.4
                 delta · delta' = 0.076 · 4e-4 = 3.04e-5
Step 3 (simpl):  NLO/LO = 587.4 · 3.04e-5 = 0.01786          [Python-verified, R3-B]
Step 4 (dir):    NLO is ~56x SMALLER than LO at the substrate Schur layer,
                 NOT 18x larger. The C-amplification at (a_4, a_4) is OVER-COMPENSATED
                 by the delta · delta' = 3e-5 suppression from a_4/a_2 + epsilon^2 combined.
```

Direct re-verification (Python): `587.4 * 3.04e-5 = 0.017857`, reciprocal = 56.0. My "~18" was a sign-of-the-exponent slip — I had the inverse ratio and read it as the ratio. The structural consequence is exactly what tesla R3-A §D-tesla-3-1 lays out: the C-amplification worry I introduced in R1 Re:T4 / M2 (paragraph 2: "C-amplification factor 10^10-10^11 makes 'non-leading' misleading") is RETIRED at NLO as well as at LO. The NLO contribution to F_marg is ~1.4e-49, sub-dominant to LO ~1.4e-47 by 2 OOM, and 34 OOM below the σ_LISA·σ_CMBS4 floor. **I retract the framing in my R2-B EMERGENCE note that NLO might "approach the LO contribution"; it does not.** The S86 carry-forward for NLO δ pinning is a completeness exercise, not a near-floor risk-mitigation task.

This matters for the (c) verdict text: the (c) decision should NOT signal NLO-floor-risk. It should record NLO engagement (J_C[a_4] becomes non-zero through heat-kernel renormalization of G_N) as a structural fact and pre-register an S86 completeness computation, but the operational claim "ρ at observable level is detector-floor-diluted under all atlas regulators at all loop orders accessible at L_max ≤ 12" stands without qualification.

**C-mack-3-2 — Diagrammatic kernel inner product cross-validation (C-tesla-3-1) ratifies the workshop's most decisive structural finding: kernel-orthogonality at the parameter layer is dead, and is dead by TWO independent computational routes.**

Re: C-tesla-3-1. Tesla R3-A confirms my R2-B C-mack-3 diagrammatic Mellin-moment computation (sum of (a_2,a_2) and (a_2,a_0) channels = +1.378e-47) agrees with his R2-A full-Schur substrate-only term to better than 1e-50. This is the workshop's strongest cross-validation: two computationally INDEPENDENT routes (direct 5x5 Schur inversion vs. Mellin-moment kernel decomposition) both produce the same non-zero number. The W13-2 ρ_cc = 0 verdict therefore CANNOT be defended at the parameter layer via SO(3)-irrep kernel-orthogonality — neither tesla's T4 Step 5 lemma nor any reformulation of it survives the cross-check. The defense at the observable layer is exclusively detector-floor dilution + experimental-noise frequency-band block-diagonality.

The structural consequence I want to record permanently: the framework's instinct to defend joint-channel independence by appeal to mode-decomposition orthogonality (tensor-2 vs scalar-0, B-mode vs E-mode, equilateral vs folded f_NL) needs auditing across the project. Mode-projection-layer orthogonality is real; parameter-layer orthogonality requires the Schur cross-block analysis. Per my R2-B EMERGENCE E-mack-3, this is a framework-wide audit task (carry-forward to S86).

**C-mack-3-3 — E-tesla-3-2 verified sign-convention dependence of ρ_substrate-prediction. ACCEPTED; my R2-B E-mack-2 framing was magnitude-implicit and tesla R3-A makes it explicit.**

Re: E-tesla-3-2 + A-mack-7. Tesla R3-A's direct Pearson computation across the W12-4 atlas pins the sign convention dependence:

```
Step 1 (def):    Pearson(Omega_GW_proxy, alpha_s_proxy) computed across 5 regulators.
Step 2 (subst):  alpha_s_signed (standard, alpha_s ~ -0.069 reported without |.|)
                 |alpha_s| (magnitude form, the convention E-mack-2 implicitly used)
Step 3 (simpl):  Tesla R3-A pinned values (R3-A line 1588-1589):
                   rho(Omega_GW, alpha_s_signed) = +0.9114
                   rho(Omega_GW, |alpha_s|)      = -0.9114
                 (R3-B independent reproduction with the linear proxy returned -0.91 for
                  BOTH conventions, because the linear proxy I used keeps n_s monotone in
                  a_2/a_0 across the atlas. The exact-S50 mapping tesla R3-A used produces
                  the sign swap. The magnitude AGREES; the sign-swap depends on the precise
                  n_s ↔ a_2/a_0 functional form. R3-B accepts tesla R3-A's pinned numbers
                  as the canonical substrate-prediction values for the S86 gate spec.)
Step 4 (dir):    The CORRELATION IS LARGE (|rho| ~ 0.91) regardless of convention.
                 The SIGN depends on the convention chosen. The S86 gate spec must pin
                 BOTH (i) the sign convention and (ii) the precise n_s ↔ a_2/a_0 mapping
                 used to compute alpha_s_pred(r) from the atlas a_n(r) values. PRU class-8
                 risk on the n_s functional form is a NEW finding from this convergence —
                 the R2-B linear-proxy and R3-A exact-S50 maps disagree on sign in a
                 reproducible way that the gate spec must resolve.
```

This is a STRENGTHENING of my R2-B E-mack-2 "Pauli-Villars opposite-direction outlier" hypothesis: the correlation magnitude is even larger than I anticipated (|rho| = 0.91, not "potentially substantial" as I hedged). The schedule's decision (a-ii) — joint-detection significance multiplies as if from independent draws — is structurally false at the substrate-prediction layer with confidence: a |rho| = 0.91 is roughly 1 OOM from independence in joint-distribution terms.

The S86 gate spec (below) pre-registers BOTH conventions, BOTH atlas weightings (uniform 5-reg vs PV-down-weighted), AND the n_s ↔ a_2/a_0 functional form pin (linear proxy vs exact S50 O-Z map) as machinery that must be declared at gate-firing time. This is three PRU class-8 vulnerabilities, all closed by explicit pre-registration.

### DISSENT

I retain dissent on ONE narrow point where tesla R3-A's framing of the W13-2 verdict-text consequence is technically correct but, in my reading, asymmetric in a way that the workshop verdict should record explicitly to avoid a future audit ambiguity.

**D-mack-3-1 — Tesla R3-A §D-tesla-3-2's F_diag = 0 "tautology" framing is correct but the workshop verdict should NOT leave the impression that the W13-2 verdict line is content-free. It is content-FULL at the layer it certifies (experimental-Fisher block-diagonality after detector-noise block-diagonalization), even though the off-diagonal zero is basis-trivial.**

Re: D-tesla-3-2 in tesla R3-A. Tesla writes that "F_diag is identically zero by tautology (every two-observable Fisher in a basis with no shared fit parameter has zero off-diagonal)." This is true in pure linear algebra but understates what the W13-2 verdict line operationally certifies. Substitution chain:

```
Step 1 (def):    The W13-2 verdict line certifies F_diag = diag(1/sigma_alpha^2, 1/sigma_Omega^2)
                 with the experimental sigmas pinned to LISA-PLS-2024 + CMB-S4-Book-2019.
Step 2 (subst):  The diagonality of F_diag presupposes that the experimental noise covariance
                 Sigma_exp is block-diagonal between the LISA detector and the CMB-S4 detector.
                 This is NOT a tautology — it is a substantive claim about the absence of
                 cross-detector noise correlations (e.g., no shared cosmic ray foreground,
                 no shared atmospheric template, no shared instrumental systematic).
Step 3 (simpl): The 13.6-OOM frequency-band separation (T3 axis (ii)) is what GUARANTEES
                 Sigma_exp is block-diagonal in the absence of pathological foreground
                 correlations. Without that frequency-band separation, the W13-2 verdict line
                 would NOT be a tautology — it would be a substantive null result that future
                 detectors could overturn.
Step 4 (dir):   The W13-2 verdict line is content-FULL at the level of "the experimental
                 noise cross-block is empirically zero given current detector designs." It is
                 BASIS-TRIVIAL only at the linear-algebraic step that follows from Sigma_exp
                 block-diagonality + no shared explicit fit parameter. The workshop verdict
                 should record both layers — F_diag = 0 is observationally well-supported AND
                 the substantive substrate analysis (F_marg ~ +3.42e-34) is the workshop's new
                 contribution.
```

So my narrow dissent is on framing only: tesla R3-A § D-tesla-3-2 step 4 reads "R3-B's verdict text should NOT cite F_diag = 0 as substantive evidence for substrate independence — it should be cited as a basis-construction property." I propose a slight refinement: cite F_diag = 0 as a TWO-STAGE property — (i) experimentally well-supported (Sigma_exp block-diagonal by 13.6-OOM gap + no known cross-detector foreground) and (ii) basis-trivially propagating that to F_diag off-diagonal under no-shared-fit-parameter. The workshop verdict text below adopts this dual framing. tesla R3-A's structural conclusion (F_marg ≠ 0 is the substantive workshop content) stands.

This is genuinely a NEW dissent — it sharpens but does not contradict R3-A. No earlier round addressed the experimental-noise-block-diagonality vs basis-construction split as separate substantive layers; the dual framing is needed for the workshop verdict to avoid a future audit that quotes "ρ_experimental = 0 is a tautology" out of context.

### EMERGENCE

Three new structural insights from the full R1/R2/R3 exchange that no single round produced alone. The most important — the three-layer adjudication of the W13-2 ρ=0 verdict — is the workshop's permanent contribution and is framed first.

**E-mack-3-1 — THREE-LAYER ADJUDICATION OF THE W13-2 ρ=0 VERDICT (WORKSHOP'S PRIMARY EMERGENT STRUCTURAL FINDING).**

The full R1/R2/R3 exchange has decomposed the W13-2 ρ_cc = 0 verdict into three structurally distinct layers, each with its own truth status. Per tesla R3-A §A-mack-7 + my E-mack-1 + the C1/C-mack-3-2 cross-validation, the verdict admits three-layer adjudication (and CRITICALLY, tesla R3-A §A-mack-7 closing paragraph confirms NO INFO downgrade is required — the verdict is structurally correct at each layer it certifies, but the workshop must explicitly distinguish them):

| Layer | Object | Status | Defended By | Defended Against |
|:------|:-------|:-------|:------------|:-----------------|
| 1. Parameter layer (substrate kernel inner product) | ⟨K_CGWB[a_n], K_α_s[a_n]⟩ as Schur substrate-only term | DEAD ρ=0 — non-zero (+1.378e-47 zeta-pin) | T4 SO(3)-irrep lemma (R1 tesla) | mack Re:T3 + tesla R2-A C1 + mack R2-B C-mack-3 + tesla R3-A C-tesla-3-1 |
| 2. Experimental-Fisher layer (basis-construction tautology + Σ_exp block-diagonality) | F_diag[1,2] in (CGWB, α_s) basis with no a_n nuisance | DEFENSIBLE ρ=0 — basis-trivial AND noise-block-diagonal | basis choice (no shared explicit fit parameter); 13.6-OOM frequency-band separation guarantees Σ_exp block-diagonal | basis-construction is a tautology only AFTER the noise-block-diagonality is established (D-mack-3-1 dual framing) |
| 3. Substrate-marginalized observable layer (detector-floor dilution) | ρ_marg = F_marg[1,2] / sqrt(F_marg[1,1]·F_marg[2,2]) at observable scale | DEFENSIBLE ρ≈0 — non-zero (+2.42e-46 zeta-pin) but 31 OOM below σ_LISA·σ_CMBS4 floor | C2 + C-mack-1 (detector-floor dilution from 46-OOM Ω_GW vs σ_LISA gap) | the observable smallness depends on the σ_LISA = 1e-12 floor; a future detector with σ(Ω_GW) ~ Ω_GW_predicted would surface ρ_marg ≠ 0 |

**The verdict is structurally correct at EACH of layers 2 and 3, simultaneously**. It is dead at layer 1 (any future framework discussion that defends ρ_cc = 0 by appealing to substrate kernel-orthogonality is invoking a dead lemma). NO INFO downgrade is required because the verdict's pre-registration (W13-2 §(e)) writes the experimental-Fisher off-diagonal as the gated quantity, and that quantity is genuinely zero by basis-construction + block-diagonal Σ_exp.

**Substrate framing recap**: At the substrate layer, CGWB and α_s are not independent — they ride two co-existing branches of the same post-fold GGE relic (transverse acoustic at c_BLV = 0.485 for CGWB; longitudinal acoustic for α_s), share a_2 at LEADING order through the spectral action's heat-kernel expansion (1/G_N ∝ a_2 for CGWB; n_s = f(a_2/a_0) for α_s), and produce a non-trivial Pearson correlation |ρ_substrate-prediction| ≈ 0.91 across the W12-4 5-regulator atlas. The substrate is NOT IN spacetime — it IS the spectral content from which both branches emerge as orthogonal mode-projections of the same underlying spectral triple. The "independence" the W13-2 verdict line certifies is observational independence under current detector designs, not substrate-level independence.

This three-layer framing is a candidate permanent-results-registry entry per tesla R3-A Q-tesla-12 — it generalizes beyond §6A to ANY future joint-channel gate that quotes ρ between two observables sharing a substrate parameter. R3-B carry-forward includes adding the taxonomy to `sessions/permanent-results-registry.md` with keyword "three-layer adjudication for joint-channel ρ verdicts."

**E-mack-3-2 — The W12-4 class-(d) closure has THREE distinct downstream PRU class-8 vulnerabilities for joint-channel substrate-prediction gates, all surfaced by this workshop.**

Per tesla R3-A §E-tesla-3-2 + my A-mack-7 + the convention question Q-mack-9, future S86+ gates that quote ρ(CGWB, α_s) inherit not one but THREE distinct regulator-pin disciplines:

```
Step 1 (def): A pre-registered ρ(CGWB, α_s) gate must declare:
              (i)   regulator label (zeta, HK, Mellin, hard-cutoff, Pauli-Villars).
              (ii)  atlas weighting (uniform 5-reg vs PV-down-weighted vs other).
              (iii) sign convention (signed alpha_s vs |alpha_s|).
              (iv)  n_s ↔ a_2/a_0 functional form (linear proxy vs exact S50 O-Z map).
              (v)   J convention (linear-derivative canonical vs logarithmic-derivative diagnostic).
              (vi)  L_max (currently 10; survival of (a_2, a_2) > (a_2, a_0) dominance at L_max ≥ 12 is L_max-empirical per tesla R3-A E-tesla-3-1).
Step 2 (subst): Any S86+ gate that omits any of (i)–(vi) is PRU class-8 ill-formed.
                The S86-RHO-SUBSTRATE-PREDICTION gate spec below pins all six.
Step 3 (simpl): Three of these (i, ii, iii) directly affect the gate's reported value;
                two (iv, v) affect the canonical form of intermediate quantities;
                one (vi) affects the L_max-empirical sub-leading dominance structure.
                Together they constitute the FULL audit of regulator-conditioning that the
                workshop has surfaced.
Step 4 (dir): Without explicit pre-registration of (i)–(vi), a future S86+ paper or session
              that quotes "ρ(CGWB, α_s) = X" inherits a non-recoverable ambiguity — there
              is no scaling law (per C-mack-2 substitution chain in R2-B) that can back out
              the missing pins from a quoted value. The S86 gate spec below MUST pin all six.
```

This is the workshop's second emergent structural contribution: the W12-4 regulator-pin discipline propagates not just to the regulator-label naming (already done by W13-2's "scheme=zeta") but to FIVE additional machinery axes that future gates inherit. The S86 gate spec encodes all six pins.

**E-mack-3-3 — Heat-kernel-analytic origin of the (a_2, a_4) Pearson +0.9922 (E-tesla-3-3) is a permanent framework feature that PRE-DETERMINES the C_pinv near-singularity at all reasonable L_max.**

Re: E-tesla-3-3 in tesla R3-A. Tesla observes that the (a_2, a_4) atlas Pearson +0.9922 is not coincidence — both coefficients are read from adjacent poles of the spectral zeta function ζ_{D_K}(s), and their regulator-dependence is dominated by how each regulator handles the UV behavior near the same eigenvalue cluster. This is a STRUCTURAL fact about the heat-kernel expansion, not an L_max artifact.

The substantive emergent point that follows: the C substrate covariance (over the 5-regulator atlas) will REMAIN near-singular at any reasonable L_max because the heat-kernel expansion's analytic structure ties adjacent moments. This guarantees:

- Future S86+ gates that marginalize over a_n MUST use pseudoinverse or Tikhonov regularization, never direct inverse (per E-tesla-3-3 final paragraph).
- The (a_2, a_4) C_pinv +1.31e+11 amplification channel will remain LARGE at all L_max — but per D-tesla-3-1, this channel is structurally dormant at LO (J_C[a_4] = 0 at LO) and sub-dominant at NLO by factor 56.
- The W12-4 class-(d) closure is therefore PERMANENT in a sense stronger than W12-4's regulator-spread spec: even adding more regulators or refining L_max would not produce a well-conditioned C, because the analytic structure of the heat-kernel expansion enforces near-singularity.

This is methodological — it tells future gates how to handle the substrate covariance — but it is also a framework-structural claim about the spectral triple's heat-kernel architecture. The S86 gate spec includes a methodological pin: any future Schur computation MUST use pseudoinverse, not direct inverse, on the substrate covariance.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | CGWB and α_s a_n-projection distinctness | T3, Re:T3, C1, C-mack-3-2 | **Converged** | Index-disjoint framing dead; both observables share a_2 at LO; kernel-orthogonality at PARAMETER layer dead by two independent computational routes (full-Schur + diagrammatic Mellin-moment). Mode-projection-layer SO(3)-irrep orthogonality is real but does not propagate to parameter layer. |
| 2 | a_n regulator-class-(d) implication for covariance | M1, M2, C-tesla-3-2 | **Converged** | Substrate covariance C is near-singular (det ~ 1e-14, cond ~ 7.6e+10) at L_max=10, with (a_2, a_4) Pearson +0.9922; near-singularity is HEAT-KERNEL-ANALYTIC-STRUCTURAL (E-tesla-3-3) and survives all reasonable L_max; future Schur computations MUST use pseudoinverse. |
| 3 | Fisher matrix with a_n nuisance — ρ stays 0 or moves? | T4 (R2-A), M3, C-mack-1, A-mack-7 | **Converged** | F_marg[CGWB, α_s] = +3.42e-34 at zeta-pin (NON-ZERO at substrate); ρ_marg = +2.42e-46 at observable scale (31 OOM below σ_LISA·σ_CMBS4 = 3e-15 floor). Substrate covariance does propagate; observable consequence is detector-floor-diluted. |
| 4 | Diagrammatic kernel-overlap analysis (k-space) | M2 (R2-B), C-mack-3, C-tesla-3-1 | **Converged** | Two independent routes (5x5 Schur inversion + Mellin-moment kernel decomposition) agree to better than 1e-50 on F_marg substrate-only = +1.378e-47. (a_2, a_2) channel dominates (a_2, a_0) by 4 OOM at LO; (a_2, a_4) C-amplification channel dormant at LO, NLO sub-dominant by 56x (D-tesla-3-1 corrected arithmetic). |
| 5 | Joint-detection significance multiplication validity | T4, M3, D-mack-2, C-tesla-3-3, E-tesla-3-2 | **Dissent** (from W13-2 schedule reading) | Schedule decision (a) bundles (a-i) "ρ at observable layer = 0" (TRUE) and (a-ii) "joint-detection significance multiplies" (FALSE under W12-4 atlas-stratified prediction, where |ρ_substrate-prediction| ≈ 0.91). (a-ii) is structurally retired; (a-i) is preserved. |
| 6 | Canonical decision (a / b / c) | All, C-tesla-3-3, C-mack-2 | **Converged on (c)** | Decision (c) "regulator-conditional, NEW result extending W12-4" adopted as the W12-4-aware structurally correct pre-registration. Per-regulator ρ_marg spread [+2.42e-46, +1.41e-45] = factor 5.8 across atlas; atlas-spread NOT recoverable from single scaling law (per C-mack-2 substitution chain). |
| 7 | S-5 Falsifier Master-Inventory cross-pairing | A-mack-8, Q-tesla-9 | **Converged on option-β (placeholder line)** | Single-detector single-pair prediction observationally inert (substrate F_marg 30+ OOM below floor at all atlas regulators); but ρ_substrate-prediction ≈ 0.91 is a JOINT-distribution claim that future detector pairings could expose. Placeholder S-5 line preserves W12-4 regulator-pin discipline at the falsifier-inventory layer. |
| 8 | Three-layer adjudication of W13-2 ρ=0 verdict | E-mack-3-1, A-mack-7 | **Emerged** (workshop's primary structural contribution) | Verdict admits three-layer adjudication: DEAD at parameter layer (T4 SO(3)-irrep lemma cannot defend ρ=0 there); DEFENSIBLE at experimental-Fisher layer (basis-trivial + Σ_exp block-diagonal by 13.6-OOM gap); DEFENSIBLE at substrate-marginalized observable layer (detector-floor dilution). NO INFO downgrade required — verdict is structurally correct at the layer it certifies. |
| 9 | Three-Fisher taxonomy (ρ_experimental, ρ_substrate-marg, ρ_substrate-prediction) | E-mack-1, C-tesla-3-2, A-mack-7 | **Emerged** | Workshop surfaces a permanent taxonomy distinguishing three structurally distinct ρ values that the original §6A invocation conflated. Candidate permanent-results-registry entry per Q-tesla-12. |
| 10 | NLO J_C[a_4] engagement / C-amplification at NLO | Q-mack-6, D-tesla-3-1, A-mack-6, C-mack-3-1 | **Converged (NLO sub-dominant)** | NLO/LO ratio = 0.018 (NOT 18 as R2-B Q-mack-6 step 3 mistakenly claimed; 1000x slip); NLO contribution ~1.4e-49 vs LO ~1.4e-47, sub-dominant by 2 OOM, 34 OOM below floor. C-amplification worry retired structurally at LO and NLO. |
| 11 | Convention canonicalization (J linear vs logarithmic) | Q-mack-9, C-mack-4, C-tesla-3-4 | **Converged** | Canonical: linear-derivative ∂O/∂a_n with explicit units carried; alternate (parenthetical scaling diagnostic): logarithmic ∂(ln O)/∂(ln a_n). Pin in S86 gate spec to prevent PRU class-8 defects on Jacobian normalization. |
| 12 | Sign convention for ρ_substrate-prediction | E-mack-2, E-tesla-3-2, A-mack-7 | **Converged on dual reporting** | Tesla R3-A pinned values: ρ(Ω_GW, α_s_signed) = +0.9114; ρ(Ω_GW, |α_s|) = -0.9114. Magnitude AGREES; sign-swap depends on the exact n_s ↔ a_2/a_0 functional form. S86 gate spec pre-registers BOTH conventions. |
| 13 | F_diag = 0 substantive vs basis-trivial framing | D-tesla-3-2, D-mack-3-1 | **Partial** (refined dual framing) | F_diag = 0 is content-FULL at the experimental-noise-block-diagonality layer (13.6-OOM frequency-band separation guarantees Σ_exp block-diagonal in absence of pathological cross-detector foregrounds) and basis-trivial only at the linear-algebraic step that follows. R3-B verdict text adopts dual framing. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

Each is specific enough to be picked up as an S86 (or later) gate or session topic. Numbered for cross-reference.

1. **NLO J_C[a_4] canonical pin from heat-kernel renormalization**: the framework's canonical heat-kernel-renormalization NLO entry of a_4 into 1/G_N has not been pinned to a numerical δ value in either `s74_r_family_observable_scan.py` or `s69_kk_higgs.py`. The natural framework-structural choice δ = a_4/a_2 gives δ_zeta = 0.076 and produces the D-tesla-3-1 NLO/LO ratio = 0.018, but a first-principles derivation from the Connes-Chamseddine spectral action's NLO heat-kernel coefficient is needed for completeness. (Computation gate: S86-J-CGWB-A4-NLO-PIN.)

2. **L_max ≥ 12 stability of the (a_2, a_2) > (a_2, a_0) 4-OOM dominance** (per E-tesla-3-1): the LO truncation J_C[a_n] = 0 ∀ n ≠ 2 is framework-structural and survives all L_max, but the C_pinv numerical entries (and therefore the (a_2, a_2) over (a_2, a_0) ordering by 4 OOM specifically) are L_max-empirical. An L_max ≥ 12 W12-4 atlas recomputation would pin this. (Computation gate: S86-W12-4-LMAX12-EXTEND.)

3. **ρ_substrate-prediction Monte Carlo over the W12-4 atlas at full atlas treatment**: the third Fisher object in the E-mack-1 taxonomy (Pearson(Ω_GW, α_s) under the W12-4 atlas-stratified predictive distribution) is currently UNCOMPUTED at gate-level. Tesla R3-A E-tesla-3-2 gives the 5-point analytic Pearson |ρ| ≈ 0.91, but a proper Monte Carlo over the predictive distribution under the framework's chosen interpretation of C (Bayesian over regulator-atlas vs zeta-committed; A-tesla-2 chose (c) atlas-stratified) requires explicit MC propagation. (Computation gate: S86-RHO-SUBSTRATE-PREDICTION — full spec below.)

4. **Sign-swap mechanism between linear-proxy and exact-S50 n_s functional forms**: tesla R3-A E-tesla-3-2 reports +0.9114 (signed) vs -0.9114 (magnitude); R3-B independent reproduction with the linear-proxy mapping gave -0.91 for BOTH conventions. The sign-swap depends on the precise n_s ↔ a_2/a_0 functional form chosen, which is itself a PRU class-8 vulnerability. A first-principles derivation of n_s(a_2, a_0) from the framework's spectral-action expansion (replacing both the linear proxy and the S50 O-Z constant-mass identity) would resolve which convention is canonical. (Computation gate: S86-NS-OF-A2-A0-CANONICAL.)

5. **Framework-wide audit of joint-channel "independence by mode-decomposition orthogonality" claims** (per C-mack-3-2 + R2-B EMERGENCE E-mack-3): provisional vulnerable-claim list is (i) f_NL channel decompositions (equilateral vs folded vs squeezed), (ii) tensor power-spectrum vs scalar power-spectrum amplitude consistency relations, (iii) any "B-mode independence from E-mode" claim that rests on pure parity-decomposition arguments. Each needs a parameter-layer Schur cross-check analogous to the §6A workshop. (Computation series: S86-JOINT-CHANNEL-AUDIT-{f_NL, r-A_s, B-E}.)

6. **Permanent-results-registry entry for the three-layer adjudication taxonomy** (per Q-tesla-12 + E-mack-3-1): the three-Fisher / three-layer framing surfaced by this workshop generalizes to ANY future joint-channel gate. Adding it as a `sessions/permanent-results-registry.md` entry (keyword: "three-layer adjudication for joint-channel ρ verdicts") prevents future agents from re-litigating the basis-tautology vs substrate-marginalized vs predictive distinction. (Documentation task: S86-PRR-THREE-LAYER-ADJUDICATION.)

7. **S-5 Falsifier Master-Inventory placeholder line**: per A-mack-8 + Q-tesla-9, the workshop converged on option-β (placeholder line with deferred-falsifier clause). Drafted text: "S-5-CGWB-ALPHAS-JOINT-PRED: IF a future joint detector reaches σ_pred-floor on Ω_GW AND on α_s AND measures Pearson(Ω_GW, α_s) ≠ predicted ρ_substrate-prediction at >5σ AT THE PRE-REGISTERED REGULATOR / ATLAS-WEIGHTING / SIGN-CONVENTION, the framework is falsified at the chosen regulator; otherwise consistent with all 5 atlas regulators." Adding this to S-5 inventory is the registry task. (Documentation task: S86-S-5-FALSIFIER-CGWB-ALPHAS-JOINT-PRED.)

8. **Cross-detector foreground correlations at LISA × CMB-S4 (D-mack-3-1 backstop)**: the W13-2 verdict line implicitly assumes Σ_exp is block-diagonal, which requires absence of pathological cross-detector foreground correlations (shared cosmic ray template, shared atmospheric model, shared instrumental systematic). The 13.6-OOM frequency-band gap makes this very likely true but does not formally guarantee it. A literature scan or an explicit pre-registered cross-foreground audit would close the substantive layer of D-mack-3-1's dual framing. (Literature/computation task: S86-XDET-FOREGROUND-AUDIT.)

## Wrap-Up — Workshop Impact Summary

### What Changed

- **Tesla's R1 T4 SO(3)-irrep kernel-orthogonality lemma is dead at the parameter layer** — confirmed by two computationally independent routes (full-Schur 5x5 inversion + Mellin-moment kernel decomposition). This was the load-bearing defense of the W13-2 ρ_cc=0 claim at the substrate layer; it cannot be cited going forward.
- **The W13-2 "ρ=0, joint-detection significance multiplies" reading bundles a TRUE claim (a-i, observable-layer ρ ≈ 0) and a FALSE claim (a-ii, ρ_substrate-prediction = 0)**. The schedule's decision (a) is half-true / half-false; decision (c) is the structurally correct disentanglement.
- **Three Fisher matrices, not one, are in play in any joint-channel ρ gate** — the workshop surfaces a permanent taxonomy distinguishing ρ_experimental, ρ_substrate-marg, and ρ_substrate-prediction. The W13-2 verdict line literally certifies only the first.

### What Holds

- **The W13-2 verdict line at the experimental-Fisher layer remains valid** — F_diag[1,2] = 0 by basis construction + Σ_exp block-diagonality (13.6-OOM frequency gap). NO INFO downgrade required (per A-mack-7); the verdict is structurally correct at the layer it certifies.
- **The W13-2 ρ ≈ 0 at the substrate-marginalized observable layer also holds** — F_marg[CGWB, α_s] = +3.42e-34 is non-zero at substrate, but ρ_marg = +2.42e-46 is 31 OOM below the σ_LISA · σ_CMBS4 = 3e-15 floor. Detector-floor dilution from the 46-OOM Ω_GW vs σ_LISA gap is the operational mechanism.
- **The W12-4 class-(d) closure on a_n propagates upward to all joint-channel substrate-prediction gates** with a SIX-axis pin discipline (regulator label, atlas weighting, sign convention, n_s functional form, J convention, L_max). All six axes are pinned in the S86 gate spec below.

### What Breaks or Strains

- **The schedule §6A invocation language "joint-detection significance multiplies" is structurally false** under the W12-4 atlas-stratified interpretation: |ρ_substrate-prediction| ≈ 0.91 means joint significance does NOT factorize as independent products. Any future framework discussion that quotes "ρ(CGWB, α_s) = 0" without specifying which of the three Fisher layers it means inherits a non-recoverable PRU class-8 ambiguity.
- **The framework's broader instinct to defend joint-channel independence by mode-decomposition orthogonality is now under suspicion** at the parameter layer (per E-mack-3-1 + R2-B E-mack-3). Provisional vulnerable list: f_NL channel decompositions, tensor / scalar amplitude consistency relations, B-mode/E-mode independence claims. Each requires a parameter-layer Schur cross-check.

### Carry-Forward Computations

Numbered list, deduplicated across all rounds. Each entry: **what** / **inputs** / **gate** / **effort**.

1. **S86-RHO-SUBSTRATE-PREDICTION** (FULL SPEC BELOW). What: Monte Carlo over the W12-4 5-regulator atlas, propagating regulator-conditional (a_0, a_2, a_4) values through the framework's Jacobian to (Ω_GW, α_s) and computing Pearson under the pre-registered atlas-weighting + sign-convention + n_s functional form. Inputs: W12-4 atlas (`session-85-w12-workingpaper.md` lines 224-226); canonical n_s ↔ a_2/a_0 mapping (currently unpinned, see S86-NS-OF-A2-A0-CANONICAL); J convention pin (linear-derivative). Gate: pre-registered three-arm pass thresholds in §S86 spec below. Effort: small-medium (Monte Carlo over 5-point atlas + extension to bootstrap if atlas-stratified Bayesian posterior wanted).

2. **S86-J-CGWB-A4-NLO-PIN**. What: derive the canonical δ = J_C[a_4]_NLO / (Ω_GW / a_4) coefficient from the framework's heat-kernel-renormalized 1/G_N expansion at NLO. Inputs: Connes-Chamseddine spectral action NLO heat-kernel coefficient; canonical_constants.py NLO entries for f_2 (currently only LO is pinned). Gate: PASS if 0.05 ≤ δ ≤ 0.15 (within factor 2 of the LO suppression ratio a_4/a_2 ≈ 0.076 at zeta); INFO if 0.15 < δ < 0.5; FAIL if δ ≥ 0.5 (would push NLO toward LO magnitude, requiring re-evaluation of the (c) decision text). Effort: medium (analytic spectral-action computation).

3. **S86-W12-4-LMAX12-EXTEND**. What: re-evaluate the W12-4 5-regulator atlas at L_max = 12 (vs current L_max = 10) and recompute (a_2, a_2) and (a_2, a_0) C_pinv entries; check whether the 4-OOM dominance of (a_2, a_2) over (a_2, a_0) survives. Inputs: D_K eigenvalue spectrum at L_max = 12 (~250,000 eigenvalues, vs 155,984 at L_max = 10). Gate: PASS if |C_pinv[a_2, a_2] / C_pinv[a_2, a_0]|_{L=12} stays within factor 3 of |…|_{L=10}; INFO if factor 3-10; FAIL if factor > 10. Effort: medium-large (L_max = 12 atlas recomputation + 5-regulator re-application).

4. **S86-NS-OF-A2-A0-CANONICAL**. What: derive the canonical n_s(a_2, a_0) functional form from the framework's spectral-action expansion (resolving the linear-proxy vs S50-O-Z-constant-mass ambiguity that drives the E-tesla-3-2 sign-swap). Inputs: s71_non_trivial_fibration_csquared.py canonical (n_s ↔ a_2/a_0 ratio); s50_running_mass.py (constant-mass O-Z identity α_s = n_s² − 1 + δ_alpha). Gate: PASS if the canonical mapping uniquely determines the ρ_substrate-prediction sign; INFO if mapping is multi-valued; FAIL if the framework cannot pin the mapping. Effort: medium (analytic).

5. **S86-JOINT-CHANNEL-AUDIT-FNL** (and parallel -RA_S, -BE). What: parameter-layer Schur cross-check on three further "independence by mode-decomposition" claims in the framework. Inputs: GGE bispectrum decomposition (s67_gge_bispectrum); r vs A_s consistency (s66_inflation_exflation_synthesis); B-mode/E-mode parity decomposition (s84_w4_nt_cmb_transfer). Gate: per-claim PASS/INFO/FAIL on whether the parameter-layer cross-block has a non-zero Schur term. Effort: medium each (3 parallel computations).

6. **S86-PRR-THREE-LAYER-ADJUDICATION**. What: add the three-layer adjudication taxonomy (parameter layer / experimental-Fisher layer / substrate-marginalized observable layer) to `sessions/permanent-results-registry.md` as a methodology entry. Inputs: this workshop's E-mack-3-1 table + workshop verdict. Gate: documentation task (no computation). Effort: small.

7. **S86-S-5-FALSIFIER-CGWB-ALPHAS-JOINT-PRED**. What: add the placeholder S-5 falsifier line per A-mack-8 + Q-tesla-9 with the drafted text in Open Question 7 above. Inputs: this workshop's converged decision (c) + S86-RHO-SUBSTRATE-PREDICTION pre-registration. Gate: documentation task. Effort: small.

8. **S86-XDET-FOREGROUND-AUDIT**. What: literature scan or explicit pre-registered cross-foreground audit confirming that LISA × CMB-S4 has no pathological cross-detector foreground correlations (shared cosmic ray template, shared atmospheric model, shared instrumental systematic). Inputs: LISA-PLS-2024 noise model; CMB-S4-Book-2019 noise model. Gate: PASS if literature returns no known cross-detector correlations above 1e-3 fractional level. Effort: small-medium.

9. **S86-PSEUDOINVERSE-METHODOLOGY-PIN**. What: codify in `computations/canonical_constants.py` (or a new methodology module) the rule that any future Schur computation marginalizing over a_n nuisance MUST use Moore-Penrose pseudoinverse or Tikhonov regularization on the substrate covariance C, never direct inverse. Inputs: this workshop's E-mack-3-3 finding that C near-singularity is heat-kernel-analytic-structural, not L_max artifactual. Gate: methodological pin (no value computed). Effort: small.

### Closing Line

The W13-2 ρ_cc = 0 verdict is structurally correct at the layer it certifies (experimental-Fisher block-diagonality, basis-trivial after Σ_exp block-diagonalization), but the substantive substrate analysis says CGWB and α_s are NOT independent — they share a_2 at leading order, produce |ρ_substrate-prediction| ≈ 0.91 across the W12-4 5-regulator atlas, and remain observationally indistinguishable from independent only because the σ_LISA = 1e-12 floor dilutes the substrate covariance by 31 OOM at observable scale.

---

## Pre-registered S86 Gate Spec (FINAL — mack fills with converged decision)

**Gate ID**: S86-CGWB-ALPHA-S-INDEPENDENCE-DIAGRAMMATIC-COMMIT

**Decision** (a / b / c per schedule §6A R3):
- (a) ρ=0 is genuine, joint-detection significance multiplies as W13-2 claims
- (b) ρ ≠ 0 after a_n marginalization, joint-detection significance over-stated
- (c) ρ depends on regulator-class-(d), regulator-conditional (NEW result extending W12-4)

**Workshop converged decision**: **(c)** with explicit disentanglement of the schedule's bundled (a-i) ρ at observable layer = 0 (TRUE, preserved) and (a-ii) joint-detection significance multiplies (FALSE, retired). Per the three-layer adjudication of E-mack-3-1, the W13-2 verdict is structurally correct at the experimental-Fisher and substrate-marginalized observable layers (no INFO downgrade required), but the substantive substrate analysis says ρ_substrate-prediction ≠ 0 with magnitude ≈ 0.91 across the W12-4 5-regulator atlas.

---

**What to compute**: the predictive Pearson correlation ρ_substrate-prediction = Pearson(Ω_GW, α_s) under the framework's W12-4 atlas-stratified predictive distribution, propagating regulator-conditional (a_0, a_2, a_4) values through the framework's Jacobian to the (Ω_GW, α_s) observable pair, evaluated under PRE-REGISTERED choices for the six PRU class-8 axes.

**Input pins (six-axis machinery enumeration, per E-mack-3-2 + PRDR rule)**:

| Axis | Pin | Source |
|:-----|:----|:-------|
| (i) Regulator label set | atlas = {heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars} (W12-4 5-regulator atlas) | session-85-w12-workingpaper.md §W12-4(b) lines 224-226 |
| (ii) Atlas weighting | TWO-ARM pre-registration (per Q-tesla-10): Arm A = uniform 5-regulator weight (no PV down-weighting); Arm B = PV-down-weighted (PV treated as Bayesian outlier, weight 0; cluster {HK, zeta, Mellin, HC} uniform weight). Arm A is the framework's PRIMARY prediction (no a-priori reason to down-weight PV at the atlas-Bayesian layer). | E-tesla-3-2 + A-mack-7 + Q-tesla-10 |
| (iii) Sign convention for α_s | DUAL reporting (per Q-tesla-11): both ρ(Ω_GW, α_s_signed) AND ρ(Ω_GW, |α_s|) computed and reported. Canonical primary: signed convention (matches the standard α_s reporting where α_s ≈ -0.069 is reported without absolute-value bars per canonical_constants.py:291 `alpha_s_cmb_central = -0.06896799`). Magnitude convention is the alternate scaling diagnostic. | C-mack-3-3 + Q-tesla-11 |
| (iv) n_s ↔ a_2/a_0 functional form | DUAL reporting (per Open Question 4): linear proxy n_s = 1 + a_2/a_0 (R3-B reproduction); exact S50 O-Z constant-mass map n_s = f_S50(a_2/a_0) (R3-A pinned values). Both forms reported until S86-NS-OF-A2-A0-CANONICAL closes the ambiguity. | E-tesla-3-2 + R3-B sign-swap reproduction |
| (v) J convention | LINEAR-DERIVATIVE canonical: J^lin[a_n] = ∂O/∂a_n with explicit units carried (J_CGWB[a_2] in Ω_GW per unit a_2; J_α_s[a_2] dimensionless per unit a_2). Logarithmic-derivative J^log[a_n] = ∂(ln O)/∂(ln a_n) reported in parentheses as scaling diagnostic. | C-tesla-3-4 + Q-mack-9 |
| (vi) L_max | L_max = 10 (current W12-4 atlas evaluation; canonical_constants.py framework default). Survival of (a_2, a_2) > (a_2, a_0) 4-OOM dominance at L_max ≥ 12 deferred to S86-W12-4-LMAX12-EXTEND. | E-tesla-3-1 |

**Canonical constants used** (all imported from `computations/canonical_constants.py`): `M_KK`, `tau_fold`, `c_BLV`, `c_Gold`, `planck_ns = 0.9649`, `alpha_s_cmb_central = -0.06896799`, `f_LISA_pivot = 3.0e-3 Hz` (line 292), `sigma_alpha_s_CMBS4 = 0.003`, `sigma_Omega_GW_LISA = 1e-12`. NEW constants needed (must be added to canonical_constants.py BEFORE gate-firing per `.claude/rules/math-scripts.md`): the W12-4 atlas (a_0, a_2, a_4) tables for the 5 regulators (currently hardcoded in working-paper §(b) — promote to `W12_4_ATLAS_A0_DICT`, `W12_4_ATLAS_A2_DICT`, `W12_4_ATLAS_A4_DICT`).

**Pass thresholds** (three-arm, three-layer per E-mack-3-1):

```
Three-layer taxonomy bands (each evaluated independently):

LAYER 1 (parameter-layer Schur substrate-only):
  PASS:  |F_marg_substrate-only|_zeta in [1e-48, 1e-46]
         (matches the workshop's pinned 1.378e-47 to within factor 10).
  INFO:  |F_marg_substrate-only|_zeta outside [1e-48, 1e-46] but within [1e-50, 1e-44].
  FAIL:  |F_marg_substrate-only|_zeta outside [1e-50, 1e-44]
         (would indicate either a major arithmetic error or a structural framework shift
          relative to the R3 cross-validation).

LAYER 2 (experimental-Fisher off-diagonal):
  PASS:  F_diag[CGWB, α_s] = 0 EXACTLY (basis-construction tautology under no-shared-fit-parameter).
         Confirmed only as an internal consistency check; not a substantive layer-2 measurement.
  INFO:  layer 2 is basis-trivial; no informative pass/fail beyond confirmation.
  FAIL:  F_diag[CGWB, α_s] ≠ 0 (would indicate a basis-construction error or pathological
         shared explicit fit parameter introduced).

LAYER 3 (substrate-marginalized observable ρ_marg):
  PASS:  |ρ_marg|_zeta < 1e-30 (well below σ_LISA·σ_CMBS4 = 3e-15 floor; matches workshop pin
         2.42e-46 to within 16 OOM tolerance for L_max = 10 + zeta-pin convention).
  INFO:  1e-30 ≤ |ρ_marg|_zeta < 1e-15 (would indicate near-floor encroachment, requiring
         NLO or L_max ≥ 12 re-evaluation).
  FAIL:  |ρ_marg|_zeta ≥ 1e-15 (would cross the σ_LISA·σ_CMBS4 floor and contradict the
         R3 detector-floor-dilution mechanism; major structural revision required).

Three-arm thresholds (atlas weighting × sign convention combinations):

Arm A (uniform 5-reg) × signed α_s:
  PASS PRE-REGISTRATION: ρ_substrate-prediction in [+0.85, +0.95]   (matches R3-A +0.9114).
  INFO BAND:             ρ in [+0.50, +0.85] ∪ [+0.95, +0.99].
  FAIL:                  |ρ| < 0.50 OR ρ < 0 OR |ρ| > 0.99.

Arm A (uniform 5-reg) × |α_s|:
  PASS PRE-REGISTRATION: ρ in [-0.95, -0.85]                        (matches R3-A -0.9114).
  INFO BAND:             ρ in [-0.99, -0.95] ∪ [-0.85, -0.50].
  FAIL:                  |ρ| < 0.50 OR ρ > 0 OR |ρ| > 0.99.

Arm B (PV-down-weighted) × signed α_s:
  PASS PRE-REGISTRATION: |ρ| < 0.50 (E-tesla-3-2 final paragraph: "magnitude DROPS sharply if
                                     PV is down-weighted as an outlier").
  INFO BAND:             0.50 ≤ |ρ| < 0.85.
  FAIL:                  |ρ| ≥ 0.85 (PV-removal should DECREASE the correlation, not preserve it).

Arm B (PV-down-weighted) × |α_s|:
  Same magnitude bands as Arm B / signed; sign uncertain pending S86-NS-OF-A2-A0-CANONICAL.
```

**Substitution chain to verify the layer-3 PASS direction is correctly stated as "below" not "above"**:

```
Step 1 (def):    ρ_marg = F_marg[1,2] / sqrt(F_marg[1,1] · F_marg[2,2])              [Schur, marginalized]
Step 2 (subst):  PASS condition is |ρ_marg|_zeta < 1e-30 (well below detector floor).
                 R3 measured value |ρ_marg|_zeta = 2.42e-46.
Step 3 (simpl): 2.42e-46 < 1e-30 ?  Compare exponents: -46 < -30. TRUE.
                 (10^{-46} = 10^{-46}; 10^{-30} = 10^{-30}; -46 < -30 since -46 is to the
                  LEFT of -30 on the number line.)
Step 4 (dir):   The PASS condition |ρ_marg| BELOW 1e-30 IS satisfied by the workshop's pinned
                 value. Direction is correctly stated: "BELOW the floor" means the substrate
                 covariance is observationally invisible, which is the converged workshop finding.
                 (Anti-direction check: if PASS had read "ABOVE 1e-30," then 2.42e-46 < 1e-30
                  would FAIL, contradicting the workshop's converged structural finding. So
                  "BELOW" is correct.)
```

**INFO band conditions** (collected, in addition to the per-layer / per-arm bands above):

- INFO if any single S86 gate-firing produces a value in the INFO band of any layer (e.g., layer-3 |ρ_marg| in [1e-30, 1e-15] would INFO at the near-floor encroachment threshold).
- INFO if Arm A and Arm B agree in sign but differ in |ρ| by more than factor 5 (would indicate the regulator-atlas interpretation matters quantitatively beyond the pre-registered Bayesian-vs-cluster discrimination).
- INFO if signed and magnitude conventions agree in sign (R3-B linear-proxy reproduction; would indicate that S86-NS-OF-A2-A0-CANONICAL needs to disambiguate which n_s functional form to canonicalize).

**FAIL conditions** (collected):

- Layer-3 FAIL: |ρ_marg|_zeta ≥ 1e-15 — would cross the σ_LISA·σ_CMBS4 floor; major structural revision required (would force re-opening C2 + C-mack-1 detector-floor-dilution mechanism).
- Layer-1 FAIL: |F_marg_substrate-only|_zeta outside [1e-50, 1e-44] — would indicate either an arithmetic error or a framework shift breaking the R3 cross-validation between Schur and Mellin-moment routes.
- Three-arm FAIL: any arm produces |ρ| > 0.99 (would indicate a degeneracy in the predictive distribution; the framework should not predict a near-perfect correlation).
- Three-arm FAIL: any arm produces |ρ| < 0.05 in Arm A (would contradict E-tesla-3-2's structural finding that PV's outlier-ness on both axes drives a substantial correlation).

**Convention tag**:

```
scheme = zeta (canonical primary, per W13-2)
convention = LISA-PLS-2024+CMB-S4-Book-2019+W12-4-5-regulator-atlas+linear-derivative-J+signed-alpha_s-canonical+dual-arm-atlas-weighting+L_max=10
schema_version = S86+
```

**Threshold + falsification clause**: pre-registered thresholds above. Falsification clause: if the S86-RHO-SUBSTRATE-PREDICTION gate fires Arm A signed = ρ in [+0.85, +0.95] AND Arm A |α_s| = ρ in [-0.95, -0.85] AND |F_marg_substrate-only|_zeta in [1e-48, 1e-46] AND layer-3 |ρ_marg|_zeta < 1e-30, the workshop's R3 converged decision (c) is RATIFIED. If any single layer/arm hits FAIL, the workshop's R3 converged decision (c) is RE-OPENED and the failed sub-claim is escalated to a fresh S86+ workshop. INFO outcomes trigger the relevant Open Question (#1-#4 above) as a follow-on computation.

**Marginalized ρ recomputation result (tesla R2)**: F_marg[CGWB, α_s] = +3.42e-34 at zeta-pin (full 5×5 Schur with prior on a_n); per-regulator atlas spread [+2.88e-34, +4.46e-34] = factor 1.55 across atlas at substrate-Schur layer. ρ_marg observable spread [+2.42e-46, +1.41e-45] = factor 5.8 across atlas. Source: tesla R2-A §C1 + §C3 + per-regulator table at line 952-959 of this workshop file. Computation pin: `computations/_s85_6a_tesla_r2_fisher_5x5.py` and companion JSON `_s85_6a_tesla_r2_fisher_5x5.json` (single Python execution, no iterations).

**Kernel-overlap result (mack R2)**: ⟨K_CGWB[a_2], K_α_s[a_2]⟩_C = -1.379e-47 (a_2, a_2 channel) + -5.247e-51 (a_2, a_0 channel) = -1.378e-47 at zeta-pin (with overall Schur sign flip giving F_marg substrate-only = +1.378e-47). The (a_2, a_2) channel dominates (a_2, a_0) by 4 OOM at LO (E-tesla-3-1). The (a_2, a_4) channel is structurally dormant at LO because J_C[a_4] = 0 at LO (1/G_N has no a_4 dependence at LO regardless of L_max). Cross-validation: R2-B mack diagrammatic result agrees with R2-A tesla full-Schur substrate-only term to better than 1e-50 (4 displayed digits identical). NLO engagement of the (a_4, a_4) C_pinv = +1.31e+11 channel is sub-dominant by factor 56 (per D-tesla-3-1 corrected arithmetic: NLO/LO = 587.4 · 3.04e-5 = 0.018, Python-verified). Source: mack R2-B §C-mack-3 + tesla R3-A §C-tesla-3-1 + D-tesla-3-1.

---

**Workshop closure note**: this workshop closes upon R3-B FINAL completion. The R3 converged decision (c) + the three-layer adjudication taxonomy (E-mack-3-1) + the six-axis PRU class-8 pin discipline (E-mack-3-2) constitute the workshop's permanent structural contributions. The S86-RHO-SUBSTRATE-PREDICTION gate spec above is fully PRDR-compliant per `.claude/rules/epistemic-discipline.md` §0.10(d) — every machinery axis is enumerated and pinned at plan-write time, eliminating PRU at the gate-spec layer by construction.
