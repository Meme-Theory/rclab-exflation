## III-b. Wave 2: CC Routes + n_s (4 tasks, depends on W1-1 and W1-4)

### W2-1: Holographic Spectral Action from KZ Domain Boundaries (HOLOGRAPHIC-SPEC-44)

**Agent**: `hawking-theorist`
**Additional Researcher Context** researchers/Schwarzschild-Penrose/index.md
**Model**: opus
**Cost**: HIGH

**Prompt**:

You are computing the holographic-bounded spectral action: replace the volume-weighted Tr f(D^2/Lambda^2) with a spectral action counting only boundary modes of the 32 KZ domains. The holographic principle demands entropy scale as area, not volume. This is the Hawking route to CC suppression.

**Context.** S43 CC workshop (Hawking R1 A.1): "The spectral action Tr f(D^2) is the correct entropy functional for the internal geometry (Paper 20 proves this), but it is the WRONG gravitating energy. The gravitating vacuum energy must satisfy a holographic bound. The spectral action violates this bound by ~115 orders, which IS the CC problem."

S43 CC workshop divergent D1: Hawking proposes area-law, Volovik proposes Gibbs-Duhem. Both run in S44. HOLOGRAPHIC-SPEC-44 tests the area-law route. Pre-registered: PASS if Lambda within 10 OOM of observed.

S43 GSL-43 PASS: dS_gen/dt >= 0 at all 300 timesteps; Bekenstein saturation 1.5%. S43 FIRSTLAW-43 PASS: verified to 1.26e-7 fractional deviation.

Hawking R1 A.3: Gibbons-Hawking de Sitter entropy S_dS = 3 pi / (Lambda l_P^2). The framework has 32 KZ domains. Each domain has a boundary. The boundary modes are a subset of the full 992-mode spectrum. The holographic spectral action counts only these boundary modes.

**Computation Steps**:

1. Load all 992 eigenvalues from `tier0-computation/s42_hauser_feshbach.npz`. Load KZ domain parameters: N_domains = 32, xi_KZ = 0.152 M_KK^{-1} (S42), domain volume V_domain = V_SU(3) / 32.

2. **Boundary mode count.** For a KZ domain of linear size L_domain ~ xi_KZ, the boundary area is A_domain ~ L_domain^7 (7-dimensional boundary of 8-dimensional SU(3)). The boundary mode count:

   $$N_{\text{boundary}} = \frac{A_{\text{domain}}}{l_{\text{KK}}^7} \cdot \text{(multiplicity per site)}$$

   where l_KK = 1/M_KK. Compute N_boundary for N_domains = 32.

3. **Holographic spectral action.** Replace the bulk trace with boundary trace:

   $$S_{\text{holo}} = \sum_{k \in \text{boundary}} d_k \cdot f\left(\frac{\lambda_k^2}{\Lambda^2}\right)$$

   The boundary modes are the lowest-lying modes (longest wavelength, extending across domain walls). Identify which of the 992 modes are boundary modes by their representation content: modes with p+q <= 1 (fundamental + trivial) live on the boundary; higher representations live in the bulk.

4. **Vacuum energy from holographic spectral action.** Compute:

   $$\rho_{\text{holo}} = S_{\text{holo}} \cdot M_{\text{KK}}^4 / (16\pi^2)$$

5. **Area/volume ratio suppression.** The holographic suppression factor:

   $$R_{\text{holo}} = \frac{S_{\text{holo}}}{S_{\text{bulk}}} \sim \frac{A}{V \cdot M_{\text{KK}}} \sim \frac{N_{\text{boundary}}}{992}$$

   Report log10(R_holo) as the number of orders of CC suppression from the holographic bound.

6. **Effacement hierarchy.** From S43 FIRSTLAW-43: 4-order effacement hierarchy. The holographic spectral action includes effacement automatically through the domain boundary structure.

7. **Compare to Lambda_obs.** Report rho_holo and log10(rho_holo / rho_obs).

8. **Cross-check with Bekenstein bound.** S43 GSL-43: S_Bek = 320 nats per KK site, S_GGE = 2.21 nats (0.7% of bound). Verify that S_holo respects the Bekenstein bound.

**Pre-registered gate HOLOGRAPHIC-SPEC-44**:
- PASS: rho_holo within 10 OOM of Lambda_obs (log10(rho_holo/rho_obs) < 10)
- FAIL: rho_holo > 10^{10} * Lambda_obs (no significant suppression)
- INFO: suppression computed but depends on boundary mode identification

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/s43_gsl_transit.npz`
- `tier0-computation/s43_first_law.npz`
- `researchers/Hawking/05_1998_Hawking_Penrose_Nature_Space_Time.md`

**Output files**:
- Script: `tier0-computation/s44_holographic_spec.py`
- Data: `tier0-computation/s44_holographic_spec.npz`
- Plot: `tier0-computation/s44_holographic_spec.png`

**Working paper section**: W2-1

---

### W2-2: Spectral Dimension Flow for n_s (DIMFLOW-44)

**Agent**: `connes-ncg-theorist`
**Additional Researcher Context** researchers/Spectral-Geometry/index.md
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the spectral dimension d_s(tau) from the heat kernel return probability at 10 tau values across the transit, and extracting the n_s prediction from the spectral dimension flow.

**Context.** S43 CC workshop divergent D2: Hawking proposes d_s(tau) flows during transit, giving n_s - 1 ~ -d(d_s)/d(tau). This is the second surviving n_s route (the first is Lifshitz eta, W1-3).

The spectral dimension is defined from the heat kernel:

$$P(\sigma) = \text{Tr}\, e^{-\sigma D_K^2} = \sum_k d_k \, e^{-\sigma \lambda_k^2}$$

$$d_s(\sigma) = -2 \frac{d \ln P(\sigma)}{d \ln \sigma}$$

At small sigma (UV): d_s -> dim(SU(3)) = 8. At large sigma (IR): d_s -> 0 (compact space, discrete spectrum). The spectral dimension FLOW as tau evolves through the transit determines the effective dimensionality of the space during the phase transition.

S43 CC workshop unification gate: |n_s(DIMFLOW) - n_s(LIFSHITZ)| < 0.005. If both give the same n_s, the mechanisms are the same seen from different angles.

Paper 57 (`researchers/Baptista/57_2024_van_Suijlekom_NCG_Particle_Physics_2ed.md`) Section on spectral dimension of almost-commutative geometries.

**Computation Steps**:

1. Load eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz` (992 eigenvalues at fold) and from `tier0-computation/s41_spectral_refinement.npz` (eigenvalues at multiple tau).

2. **Compute d_s(sigma, tau) at 10 tau values.** For tau = 0.00, 0.02, 0.05, 0.08, 0.10, 0.12, 0.15, 0.17, 0.19, 0.25:
   - Recompute eigenvalues using `tier0-computation/tier1_dirac_spectrum.py` if not available at that tau.
   - Compute P(sigma) = sum_k d_k exp(-sigma lambda_k^2) for sigma in [10^{-4}, 10^{4}] (100 log-spaced points).
   - Extract d_s(sigma) = -2 d ln P / d ln sigma by numerical differentiation.

3. **Spectral dimension at the transition.** Plot d_s(sigma_pivot, tau) where sigma_pivot is chosen to be the "CMB-relevant" scale: sigma_pivot such that lambda_min / sqrt(sigma_pivot) ~ k_CMB * M_KK^{-1}.

4. **n_s from spectral dimension flow.** Following Hawking's proposal:

   $$n_s - 1 \sim -\left.\frac{d \, d_s}{d\tau}\right|_{\tau=\tau_{\text{transit}}}$$

   Compute the derivative d(d_s)/d(tau) at the transit point and at tau=0. Report n_s from this formula.

5. **Alternative: n_s from d_s directly.** In several quantum gravity approaches (CDT, causal sets), n_s - 1 is related to d_s at the relevant scale:

   $$n_s - 1 = \frac{d_s - 4}{2}$$

   Report d_s at sigma_pivot for each tau value. If d_s ~ 3.93 at the transit, this gives n_s ~ 0.965.

6. **UNIFICATION GATE.** Compare n_s from spectral dimension flow to n_s from LIFSHITZ-ETA-44 (W1-3). Report the difference. Gate: PASS if |n_s(DIM) - n_s(LIFSHITZ)| < 0.005.

7. **Report: d_s(sigma, tau) landscape, n_s prediction, comparison to Planck.**

**Pre-registered gate DIMFLOW-44**:
- PASS: n_s in [0.94, 0.97] from spectral dimension flow
- FAIL: n_s outside [0.80, 1.10]
- UNIFICATION: |n_s(DIM) - n_s(LIFSHITZ)| < 0.005

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s41_spectral_refinement.npz`
- `tier0-computation/tier1_dirac_spectrum.py`
- `researchers/Baptista/57_2024_van_Suijlekom_NCG_Particle_Physics_2ed.md`

**Output files**:
- Script: `tier0-computation/s44_dimflow.py`
- Data: `tier0-computation/s44_dimflow.npz`
- Plot: `tier0-computation/s44_dimflow.png`

**Working paper section**: W2-2

---

### W2-3: ADM Mass of the Fold via EIH (EIH-GRAV-44)

**Agent**: `einstein-theorist`
**Additional Researcher Context** researchers/Baptista/index.md
**Model**: opus
**Cost**: MEDIUM

**Prompt**:

You are computing the ADM mass (gravitating energy) of the fold geometry using the Einstein-Infeld-Hoffmann approach in spectral geometry. This provides a third independent estimate of the gravitating energy, alongside the spectral action (polynomial) and the Sakharov formula (logarithmic).

**Context.** S43 CC workshop converged C1: the spectral action is the wrong gravitating functional. The EIH approach computes the gravitating mass from the metric perturbation at spatial infinity, which is independent of the internal energy functional. In spectral geometry, the metric is encoded in the Dirac operator; the ADM mass can be extracted from the large-distance behavior of the spectral zeta function.

S43 E-vs-F audit: all computations using S(tau) as rho_grav are affected. The ADM mass is the GRAVITATIONAL mass, which is what enters the Friedmann equation. This is the quantity we need.

The spectral zeta function approach: for a compact Riemannian manifold with Dirac operator D_K, the ADM mass in the product geometry M_4 x K is related to the spectral invariants through:

$$M_{\text{ADM}} = \frac{a_2(D_K^2)}{(4\pi)^{d/2}} \cdot V_K \cdot R_4$$

where a_2 is the second Seeley-DeWitt coefficient (encoding the Ricci scalar of K), V_K is the volume of K, and R_4 is the 4D curvature.

**Computation Steps**:

1. Load a_2 from `tier0-computation/s42_constants_snapshot.npz` and eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz`.

2. **a_2 route.** The gravitational coupling from the a_2 coefficient:

   $$\frac{1}{16\pi G_N} = \frac{f_2 \Lambda^2}{(4\pi)^4} \cdot a_2$$

   This is the spectral action route. Extract M_ADM = rho * V from H^2 = (8 pi G_N / 3) rho.

3. **Spectral zeta function route.** The spectral zeta function:

   $$\zeta_{D_K}(s) = \sum_k d_k \, |\lambda_k|^{-2s}$$

   The ADM mass density is related to zeta_D(s) at s = d/2 - 1 = 3 (for d=8):

   $$\rho_{\text{ADM}} \propto \text{Res}_{s=3} \zeta_{D_K}(s) \cdot M_{\text{KK}}^8$$

   Compute the spectral zeta function from the 992 eigenvalues and extract the residue.

4. **Ratio to S_fold.** Compute M_ADM / (S_fold * M_KK^4). If this ratio << 1, the gravitating mass is much less than the spectral action value.

5. **Compare all three estimates.** Report rho_grav from: (a) spectral action S_fold, (b) Sakharov (from W1-1 if available, otherwise estimate), (c) ADM/spectral zeta. Which two agree best?

**Pre-registered gate EIH-GRAV-44**:
- PASS: M_ADM / S_fold < 10^{-50} (massive suppression)
- FAIL: M_ADM / S_fold > 0.1 (no suppression)
- INFO: intermediate result

**Input files**:
- `tier0-computation/s42_constants_snapshot.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s36_sfull_tau_stabilization.npz`

**Output files**:
- Script: `tier0-computation/s44_eih_grav.py`
- Data: `tier0-computation/s44_eih_grav.npz`
- Plot: `tier0-computation/s44_eih_grav.png`

**Working paper section**: W2-3

---

### W2-4: Singlet Projection of GGE Energy (SINGLET-CC-44)

**Agent**: `einstein-theorist`
**Additional Researcher Context** researchers/Volovik/index.md
**Model**: opus
**Cost**: LOW

**Prompt**:

You are computing the singlet projection of the GGE excitation energy: what fraction of E_exc = 50.9 M_KK transforms as a singlet under SU(3)? Only the singlet component couples to 4D gravity (the rest is "dark" to the gravitational sector).

**Context.** S34 block-diagonal theorem: D_K is exactly block-diagonal in Peter-Weyl decomposition. S34 Schur's lemma on B2: V(B2,B2) is basis-independent. S34 Trap 1: V(B1,B1) = 0 exact (U(2) singlet selection rule). The GGE has 59.8 quasiparticle pairs distributed across B1, B2, B3 sectors.

The question: when the GGE energy couples to 4D gravity through the spectral action, does the FULL energy E_exc = 50.9 M_KK gravitate, or only the singlet component? The Schur selection rule may suppress the coupling of non-singlet modes to the 4D gravitational field.

In KK reduction, only the (0,0) singlet sector of the internal stress-energy tensor sources 4D gravity:

$$T^{\mu\nu}_{4D} = \int_K T^{\mu\nu}[\phi] \, dV_K$$

The integral over K projects onto the (0,0) singlet. Non-singlet components integrate to zero by orthogonality of spherical harmonics on K.

**Computation Steps**:

1. Load GGE occupation numbers from `tier0-computation/s42_gge_energy.npz` and eigenvalue data from `tier0-computation/s42_hauser_feshbach.npz`.

2. **Decompose E_exc by sector.** The GGE energy per sector:
   - E_B2 = sum over B2 modes of n_k * E_k
   - E_B1 = sum over B1 modes of n_k * E_k
   - E_B3 = sum over B3 modes of n_k * E_k

3. **Singlet projection.** Compute the overlap of each sector's energy distribution with the (0,0) singlet representation. For the (1,1) adjoint representation (B2 sector), the tensor product (1,1) x (1,1)* contains the singlet (0,0) ONCE. For the (1,0) fundamental (B1 sector), the product (1,0) x (0,1) contains the singlet ONCE.

4. **E_singlet.** The singlet-projected energy:

   $$E_{\text{singlet}} = \sum_k n_k E_k \cdot |\langle (0,0) | k \rangle|^2$$

   where the projection coefficient |<(0,0)|k>|^2 weights each mode by its singlet content.

5. **Report.** E_singlet / E_total. If E_singlet << E_total, the gravitating energy is suppressed by the Schur selection rule.

6. **Impact on CC.** If E_singlet / E_total ~ 1/dim(rep)^2, this gives a suppression factor. Report the implied CC reduction.

**Pre-registered gate SINGLET-CC-44**:
- PASS: E_singlet / E_total < 0.01 (>2 orders of suppression)
- FAIL: E_singlet / E_total > 0.5 (no significant suppression)
- INFO: intermediate

**Input files**:
- `tier0-computation/s42_gge_energy.npz`
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s35_ed_corrected_dos.npz`

**Output files**:
- Script: `tier0-computation/s44_singlet_cc.py`
- Data: `tier0-computation/s44_singlet_cc.npz`
- Plot: `tier0-computation/s44_singlet_cc.png`

**Working paper section**: W2-4

---
