# BA-31-5: Khoury-Berezhiani vs. Phonon-Exflation -- Structured Theoretical Comparison

**Author**: Baptista Spacetime Analyst
**Session**: 31Aa
**Date**: 2026-03-02
**Gate**: BA-31-kb (no binary gate; structured theoretical assessment)
**Sources**: Cosmic-Web-07 (Berezhiani-Khoury 2015, PRD 92 103510), Cosmic-Web-18 (Berezhiani-Khoury 2015, PRD detailed theory), Baptista Papers 13-14 (KK bosons/fermions on M4 x SU(3)), Session 29 fusion synthesis (frozen-state program), Session 30 master synthesis (BCS/Kapitza status), permanent results registry, observational avenues document

---

## 1. Executive Summary

Two frameworks claim phononic physics as fundamental to cosmology. They share vocabulary but almost nothing else. Berezhiani-Khoury (BK) operates at meV-to-galactic scales with a concrete DBI-type phonon Lagrangian and makes contact with galaxy rotation curves. Phonon-exflation (PE) operates at GUT-to-Planck scales with a spectral action on a compact internal manifold and has zero testable predictions after 30 computational sessions. The two frameworks make no overlapping predictions at any scale. Their phonons are structurally different objects: BK phonons are Bogoliubov quasiparticles of a non-relativistic condensate in flat 4D spacetime; PE phonons are hypothetical Goldstone modes of an unconfirmed BCS condensate on the 8-dimensional internal space SU(3).

The central question posed by the adversarial review -- can the BCS condensate on SU(3) produce a massless Goldstone mode in 4D? -- receives a negative answer on structural grounds. The BCS condensate (if it forms) breaks a discrete symmetry (Z_2 Pfaffian parity), not a continuous one. Discrete symmetry breaking does not produce Goldstone modes.

---

## 2. The Khoury-Berezhiani Framework

### 2.1 Fundamental Setup

BK proposes that dark matter consists of axion-like particles with mass $m_\phi \sim$ eV and a self-interaction Lagrangian (Cosmic-Web-18, eq 1-2):

$$\mathcal{L} = \partial_\mu \phi^* \partial^\mu \phi - m_\phi^2 |\phi|^2 - \lambda(|\phi|^2)^2$$

At sufficiently low temperature and high density (galactic interiors), the field condenses:

$$\phi(\mathbf{r}, t) = \sqrt{\rho_s / m_\phi} \, e^{i\Theta(\mathbf{r}, t)}$$

The condensate obeys a polytropic equation of state $P = \lambda \rho^3$ with sound speed $c_s^2 = 3\lambda \rho^2$ (Cosmic-Web-18, eqs 3-4).

### 2.2 Phonon Lagrangian

The phonons are Bogoliubov quasiparticles of the condensate. Their dispersion relation is (Cosmic-Web-18, eq 6):

$$\omega(k) = c_s k \sqrt{1 + k^2 \ell_q^2 / 4}$$

where $\ell_q$ is the quantum healing length. At low $k$, this is linear (acoustic phonons with sound speed $c_s \sim 10$ km/s in galactic cores). At high $k$, it transitions to the free-particle regime $\omega \sim k^2 / (2m_\phi)$.

The phonon-mediated force on baryonic matter produces (Cosmic-Web-07, eq 5-6):

$$a_{\text{eff}} = \sqrt{a_0 \, g_N}, \qquad a_0 \sim c_s^2 / r_0$$

This is the MOND acceleration law, now *derived* rather than postulated.

### 2.3 Scale-Dependent Phase Structure

The critical temperature scales as $T_c \propto \rho^{2/3}$ (Cosmic-Web-18, eq 4). This gives:

| Regime | Density | Temperature | Phase | Dynamics |
|:-------|:--------|:------------|:------|:---------|
| Galactic core | $\rho \sim 0.1$ GeV/cm$^3$ | $T \ll T_c$ | Superfluid ($n_s/n \gtrsim 0.9$) | MOND-like |
| Cluster outskirts | $\rho \sim 10^{-4}$ GeV/cm$^3$ | $T \gtrsim T_c$ | Normal | $\Lambda$CDM-like |
| Cosmological | low $\rho$ | $T \gg T_c$ | Normal | Standard CDM |

The MOND-to-$\Lambda$CDM transition occurs naturally at the cluster scale, consistent with where MOND observationally breaks down.

### 2.4 Observable Predictions

BK makes the following concrete predictions:

1. **Axion mass**: $m_\phi \sim$ eV, testable by ADMX/CAST
2. **Sound speed**: $c_s \sim 10$ km/s, measurable from galactic kinematics
3. **MOND acceleration scale**: $a_0 \approx 1.2 \times 10^{-10}$ m/s$^2$, derived (not fitted)
4. **Transition scale**: MOND fails at $r \sim 100$ kpc -- Mpc, testable via cluster dynamics
5. **Vortex density**: $n_v = 2m_\phi \Omega / \hbar$ in rotating systems, potentially traceable in mergers
6. **Jeans length**: $\lambda_J = c_s \sqrt{\pi / (G\rho)} \sim 100$ kpc, matching halo size

---

## 3. The Phonon-Exflation Framework

### 3.1 Fundamental Setup

PE proposes that all particles are phononic excitations of a higher-dimensional spacetime $P = M^4 \times K$ with $K = \text{SU}(3)$ equipped with a Jensen-deformed left-invariant metric (Baptista Paper 13, Section 2; Paper 14, Section 2). The particle content arises from the Dirac operator $D_K$ on the internal space.

The effective potential for the internal geometry is the spectral action (cf. Connes Paper 07):

$$V_{\text{eff}}(\tau) = \text{Tr}\, f(D_K(\tau)^2 / \Lambda^2)$$

where $\tau$ parametrizes the Jensen deformation.

### 3.2 The Phonon Identification

In PE, "phonons" are identified with the Goldstone modes of a proposed BCS condensate on SU(3). The BCS mechanism pairs Dirac eigenvalues of $D_K$ via the Kosmann-Lichnerowicz interaction $V(m, m')$ (Session 23a). The condensate, if it forms, would break a symmetry of the Dirac spectrum and produce collective excitations interpretable as 4D particles.

**Current status of the BCS condensate** (permanent results registry):

- K-1e CLOSED (Session 23a): At $\mu = 0$ (the self-consistent choice from the spectral action), the BdG gap equation gives $M_{\max} = 0.077 - 0.149$, a factor 7-13x below the threshold of 1.0. No spontaneous BCS condensate forms.
- V(gap, gap) = 0 EXACTLY (Session 23a): Selection rule forbids pairing of degenerate gap-edge states.
- W3 (spectral gap wall): $\lambda_{\min} > 0$ at all $\tau$. No Fermi surface exists.

The KC chain (Session 28) shows that an externally driven BCS condensate (with Bogoliubov injection and chemical potential) could form -- but the drive source is unspecified within the framework. KC-3 (the decisive gate) is CONDITIONAL.

### 3.3 What BCS Breaking Produces

This is the critical structural question. IF a BCS condensate forms on SU(3) (through whatever mechanism), what symmetry does it break?

The BCS order parameter $\Delta = \langle \psi \psi \rangle$ pairs states with opposite momenta. On a compact manifold, this pairs Dirac eigenmodes $|n\rangle$ and $|m\rangle$ with coupling $V(n, m)$. The condensate order parameter lives in the space of bilinear pairings on $H_K$ (the Hilbert space of $D_K$).

**Key structural fact**: The Pfaffian $\text{Pf}(\Xi \cdot D_{\text{total}}) = +1$ throughout the Jensen curve (permanent result, Session 17c). This is a $\mathbb{Z}_2$ topological invariant. The BCS condensate, if it forms, modifies the sign structure of $D_{\text{total}}$ but the Pfaffian remains $+1$ (no topological transition, Session 30Ab).

The symmetry that BCS breaks in the PE context is:

- **NOT a continuous gauge symmetry** (the gauge group $U(1) \times SU(3)$ comes from isometries, which are unbroken by BCS)
- **NOT a continuous global symmetry** of the spectral action (the spectral action is a trace, invariant under unitary conjugation, and the BCS order parameter is a specific bilinear, not protected by a continuous symmetry)
- **At best a discrete $\mathbb{Z}_2$ symmetry** (the fermion parity, related to the Pfaffian sign)

**Goldstone's theorem requires the breaking of a continuous symmetry.** Discrete symmetry breaking produces domain walls, not massless Goldstone bosons. Therefore:

> **The BCS condensate on SU(3), if it forms, does NOT produce a massless Goldstone mode in 4D.**

This is a structural result, independent of the details of the condensate.

### 3.4 Observable Predictions

PE's current observational status (observational avenues document, Session 29 fusion):

- **k_transition** $= 9.4 \times 10^{23}$ h/Mpc (Session 29Ac) -- 24 orders of magnitude above DESI
- **w = -1** exactly (frozen modulus, rolling excluded by clock constraint E-3)
- **All dynamic signatures inaccessible** to current or foreseeable experiments
- **Frozen-state predictions** (Weinberg angle, neutrino masses, phi_paasch ratio) require $\tau_0$, which has not been found (Wall 4, no minimum on any tested surface)
- **Zero quantitative predictions stated before measurement** (Sagan Level < 1)

---

## 4. Structural Comparison

### 4.1 Phonon Lagrangians

| Feature | BK | PE |
|:--------|:---|:---|
| **Phonon type** | Bogoliubov quasiparticles of scalar condensate | Hypothetical collective modes of unconfirmed BCS condensate |
| **Lagrangian** | DBI-type: $\mathcal{L} \sim (\mu - m\Phi - (\nabla\theta)^2/(2m))^{3/2}$ | Not derived (condensate does not exist at $\mu = 0$) |
| **Dispersion** | $\omega = c_s k$ at low $k$ (acoustic), $\omega \sim k^2/(2m)$ at high $k$ | Unknown (would be set by BCS gap and Hessian of $V_{\text{eff}}$) |
| **Sound speed** | $c_s \sim 10$ km/s (galactic), from $c_s^2 = 3\lambda\rho^2$ | Unknown (if condensate formed, $v_s^2 \sim d^2 V_{\text{eff}} / d\tau^2$) |
| **Number of species** | 1 (DM phonon) | Unknown (BCS on $C^{16}$ spinor space could produce multiple modes) |
| **Derivation status** | Complete from Lagrangian | No Lagrangian derived; BCS does not form at $\mu = 0$ |

### 4.2 Energy Scales

| Scale | BK | PE |
|:------|:---|:---|
| **Particle mass** | $m_\phi \sim$ eV (axion-like) | $M_{\text{KK}} \sim 10^{16}$ GeV (compactification scale) |
| **Condensation $T_c$** | $\sim$ mK (galactic cores) | $\sim 10^{16}$ GeV (GUT scale, if condensate forms) |
| **Sound speed** | $\sim 10$ km/s | $\sim c$ (relativistic internal modes) |
| **Observable scale** | $\sim$ kpc -- Mpc (galaxy to cluster) | $k_{\text{transition}} = 9.4 \times 10^{23}$ h/Mpc (inaccessible) |
| **Gap** | 0 (gapless acoustic phonons) | $2\lambda_{\min} \sim 1.644$ (gapped Dirac spectrum, W3) |

The energy scales are separated by **at least 25 orders of magnitude** in every comparable quantity. There is no regime where the two frameworks overlap.

### 4.3 Observational Contact

| Prediction | BK Status | PE Status |
|:-----------|:----------|:----------|
| Galaxy rotation curves | YES (MOND from phonon drag) | NO (no mechanism at galactic scales) |
| Tully-Fisher relation | YES (derived, $a_0$ from $c_s$) | NO |
| Cluster-scale transition | YES (phase diagram) | NO |
| Axion detection | YES ($m_\phi \sim$ eV) | NO (no stable low-energy particle predicted) |
| Dark energy $w(z)$ | Not addressed directly | $w = -1$ (frozen; 1.9$\sigma$ from DESI) |
| SM gauge couplings | Not addressed | Structural ($g_1/g_2 = e^{-2\tau}$, Baptista Paper 14 eq 2.93) but requires $\tau_0$ |
| KO-dimension | Not relevant | $= 6 \mod 8$ (parameter-free, Sessions 7-8) |
| Spectral dimension flow | Not addressed | BA-31-1 computation in progress |
| CMB features | BAO consistent | $k_{\text{transition}}$ far above CMB scales |
| Neutrino masses | Not addressed | Conditional on $\tau_0$ |
| Proton lifetime | Not addressed | Conditional on $\tau_0$ |
| Cosmological constant | Not addressed directly | $\Lambda_{\text{cc}} \sim 10^{122} \Lambda_{\text{obs}}$ (unresolved, BA-31-2) |

### 4.4 Mathematical Rigor

| Aspect | BK | PE |
|:-------|:---|:---|
| **Proven theorems** | 0 (phenomenological model) | 12 publishable results (block-diagonality, monotonicity, etc.) |
| **Internal consistency** | Self-consistent as effective theory | 6/7 NCG axioms (first-order condition fails, C-6) |
| **Parameter count** | 2 free ($m_\phi$, $\lambda$) | 0 continuous (geometry determines all), but no minimum found |
| **Closed mechanisms** | N/A (single mechanism) | 21 closed |
| **Active gates** | N/A | KC-3 (decisive), K-1 (Kapitza), plus 7 new from Session 31Aa |

---

## 5. Can PE Reproduce BK at Low Energies?

### 5.1 The Dimensional Reduction Question

For PE to make contact with BK-type phenomenology, the following chain would need to hold:

1. The BCS condensate forms on SU(3) (currently CLOSED at $\mu = 0$; CONDITIONAL on KC-3 at $\mu \neq 0$).
2. The condensate produces a massless or very light mode in 4D (structurally impossible -- see Section 3.3).
3. This mode has a DBI-type effective Lagrangian at low energies (no mechanism for this).
4. The mode couples to ordinary matter (baryons) with the correct strength to reproduce $a_0$ (no mechanism).
5. The condensate has a phase structure with $T_c \sim$ mK on galactic scales (the PE condensate, if it exists, forms at $T \sim 10^{16}$ GeV -- 22 orders too high).

**Every link in this chain is either structurally forbidden or has no known mechanism.**

### 5.2 Why No Goldstone Mode Emerges

The argument deserves explicit elaboration because it is the central structural result of this comparison.

In BK, the condensate $\phi = \sqrt{\rho_s/m} \, e^{i\Theta}$ breaks the global $U(1)$ symmetry of particle number conservation. The phase $\Theta$ is the Goldstone mode. Its fluctuations $\delta\Theta$ are the phonons, with the characteristic acoustic dispersion $\omega = c_s k$.

In PE, the situation is fundamentally different:

- The spectral action $\text{Tr}\, f(D^2/\Lambda^2)$ is invariant under the FULL unitary group $U(H)$ conjugating $D$, not just $U(1)$. But this is a gauge redundancy (unitary equivalence of operators), not a spontaneously breakable symmetry.
- The BCS order parameter $\Delta_{nm} = \langle \psi_n \psi_m \rangle$ breaks the $\mathbb{Z}_2$ fermion parity $\psi \to -\psi$. This is discrete.
- The isometry group of SU(3) (which gives the gauge group $U(1) \times SU(3)_R$) is a GEOMETRIC symmetry of the background, not a symmetry of the condensate order parameter. BCS does not break isometries.
- The continuous parameter $\tau$ (Jensen deformation) is NOT a dynamical field in the BCS sector -- it is the background geometry on which the BCS gap equation is solved. Fluctuations of $\tau$ are metric perturbations (TT modes, scalar modes), not Goldstone modes.

Therefore, no continuous symmetry is spontaneously broken by the BCS condensate. No massless Goldstone mode appears in 4D. The PE phonons, to the extent they exist at all, are massive excitations (with mass $\sim \Delta_{\text{BCS}}$) confined to the internal space.

### 5.3 Could Warping or Form Fields Change This?

The adversarial review (Section 2.1) notes that the framework omits form fields and warping. Could including these change the Goldstone analysis?

- **Form fields**: A 3-form flux on SU(3) (structure constants $f_{abc}$) provides the Freund-Rubin stabilization mechanism (KK-08, KK-10). If the 3-form has a continuous family of degenerate minima parametrized by a phase, this phase would be a Goldstone-like mode. However, the 3-form on SU(3) is UNIQUE (up to normalization) -- there is no continuous family. Gate BA-31-fr tests whether $|omega_3|^2(\tau)$ is non-monotonic.

- **Warping**: Warped compactifications (Randall-Sundrum type) can produce light modes from the warp factor. But the PE framework uses an UNWARPED product $M^4 \times K$. Including warping would be a fundamental revision, not an extension.

Neither modification produces a Goldstone mode at galactic energy scales.

---

## 6. What Each Framework Cannot Do

### 6.1 BK Cannot...

- **Derive the Standard Model**: BK addresses dark matter only. It does not explain the gauge group, fermion generations, or particle masses. These are taken as given.
- **Address the cosmological constant**: The condensation energy of the DM superfluid is $\sim$ meV$^4$, far below $\Lambda_{\text{obs}} \sim$ meV$^4$ coincidentally -- but this is not a derivation.
- **Operate at high energies**: BK is an effective theory valid below the condensation scale. It says nothing about GUT-scale physics or the early universe before the DM phase transition.
- **Explain KO-dimension or spectral geometry**: The DBI phonon Lagrangian has no connection to NCG axioms or spectral triples.

### 6.2 PE Cannot...

- **Make contact with galactic dynamics**: All dynamical signatures are at $k \sim 10^{23}$ h/Mpc (Session 29Ac). No mechanism bridges 24 orders of magnitude.
- **Produce a massless Goldstone mode**: Discrete symmetry breaking only. See Section 5.2.
- **State a quantitative prediction before measurement**: No $\tau_0$ found. Frozen-state observables uncalculable. Sagan Level < 1.
- **Stabilize the internal geometry**: 21 mechanisms closed. K-1 (Kapitza) and KC-3 (driven BCS) remain untested.
- **Address the cosmological constant**: $\Lambda_{\text{cc}} \sim 10^{122} \Lambda_{\text{obs}}$ from the spectral action $a_0$ term (adversarial review Section 3.5, BA-31-2 computation pending).

---

## 7. Do the Frameworks Make Overlapping Predictions?

**No.** The analysis is exhaustive across all identified observable channels:

| Channel | BK Prediction | PE Prediction | Overlap |
|:--------|:-------------|:-------------|:--------|
| Galaxy rotation curves | MOND-like from phonons | None | NO |
| Cluster dynamics | Phase transition scale | None | NO |
| Dark energy $w(z)$ | Not addressed | $w = -1$ | NO |
| Axion detection | $m_\phi \sim$ eV | No light scalar | NO |
| Neutrino masses | Not addressed | Conditional on $\tau_0$ | NO |
| Gauge coupling ratios | Not addressed | $g_1/g_2 = e^{-2\tau}$ at $\tau_0$ | NO |
| CMB spectral distortions | BAO from DM sound waves | None at accessible $k$ | NO |
| GW spectrum | Not addressed | $f_{\text{peak}} \sim 10^{7-9}$ Hz (speculative) | NO |
| Spectral dimension flow | Not addressed | BA-31-1 (pending) | NO |
| Proton lifetime | Not addressed | Conditional on $\tau_0$ | NO |

The two frameworks are **theoretically orthogonal**: they operate at different scales, address different phenomena, and make no common predictions. They cannot be distinguished by any experiment because they never compete for the same observable.

---

## 8. Implications for the Framework

### 8.1 The Observational Vacuum

The comparison with BK sharpens the most uncomfortable feature of the PE framework identified in the adversarial review (Section 5, Attack 2): **zero testable predictions after 30 sessions**. BK demonstrates that a phonon-based cosmological framework CAN make contact with observations at accessible scales. PE does not, and the structural analysis in this document shows that it CANNOT -- not merely that it has not yet done so.

The reason is architectural: BK operates in flat 4D spacetime with a single new field (the DM axion). Its predictions are low-energy consequences of a low-energy condensate. PE operates on a 12-dimensional product manifold where the phonon physics is confined to the 8-dimensional internal space. The dimensional reduction from 12D to 4D kills all phonon signatures except those encoded in the frozen ground state (particle masses, coupling constants). And the frozen ground state has not been determined because $\tau_0$ does not exist on any tested surface.

### 8.2 What BK's Success Tells Us

BK's observational contact comes from three features that PE lacks:

1. **A gapless spectrum**: BK phonons are acoustic ($\omega \to 0$ as $k \to 0$). PE's internal Dirac spectrum is gapped ($\lambda_{\min} > 0.818$ at all $\tau$, W3). Gapless modes mediate long-range forces; gapped modes produce only exponentially decaying interactions with range $\sim 1/\Delta$.

2. **A continuous broken symmetry**: BK breaks $U(1)$ number conservation. PE breaks (at best) $\mathbb{Z}_2$ fermion parity. Continuous breaking $\Rightarrow$ massless Goldstone modes with $1/r$ potential. Discrete breaking $\Rightarrow$ domain walls, not long-range forces.

3. **Accessible energy scales**: BK's condensate forms at $T_c \sim$ mK, well within the observational window. PE's condensate (if it forms) does so at $T \sim 10^{16}$ GeV, 22 orders above any laboratory.

All three are structural features of the frameworks' architectures, not fine-tuning failures. They cannot be remedied by finding a minimum or passing a gate.

### 8.3 Constraint Map Consequences

The comparison does not CLOSE any PE mechanism. It constrains the PE framework's **interpretation**:

- The word "phonon" in phonon-exflation is a **metaphor**, not a physical identification with BK-type phonons. The PE collective modes (if they exist) are massive, short-range, and confined to the internal space. They do not mediate forces in 4D.

- The framework's observational program reduces entirely to **frozen-state observables** -- the SM parameters computed at $\tau_0$. There is no route to dynamical observational signatures at any accessible scale.

- The comparison with BK does not lower the probability (the framework was already at 5%/3% panel/Sagan). It sharpens the diagnosis: **the framework's phonon interpretation adds no empirical content beyond what standard KK compactification provides**.

---

## 9. Summary Table

| Dimension | BK | PE | Advantage |
|:----------|:---|:---|:----------|
| Observational contact | 6+ predictions at accessible scales | 0 predictions (no $\tau_0$) | BK |
| Mathematical rigor | Effective theory, no deep theorems | 12 publishable theorems, exact results | PE |
| Phonon Lagrangian | Derived, explicit | Not derived, condensate unconfirmed | BK |
| Energy scale | meV -- keV (accessible) | $10^{16}$ GeV (inaccessible) | BK |
| Gauge group derivation | None (empirical input) | KO-dim = 6, SM quantum numbers | PE |
| Internal consistency | Self-consistent EFT | 6/7 NCG axioms, 21 closed mechanisms | BK |
| Cosmological constant | Not addressed ($\sim$ meV$^4$ coincidence) | $10^{122}\times$ too large | Neither |
| Falsifiability | YES (axion mass, $c_s$, transition scale) | NO (no $\tau_0$, no predictions) | BK |

---

## 10. Conclusion

The Berezhiani-Khoury superfluid dark matter framework and the phonon-exflation framework share the word "phonon" but differ in every substantive aspect: energy scale (25 orders of magnitude), symmetry breaking pattern (continuous vs. discrete), spectral structure (gapless vs. gapped), and observational accessibility (testable vs. untestable). They make no overlapping predictions at any scale.

The BCS condensate on SU(3), even if it forms, cannot produce a massless Goldstone mode in 4D because it breaks a discrete symmetry ($\mathbb{Z}_2$ fermion parity), not a continuous one. The PE framework's phonons are therefore massive and confined to the internal space, with no route to galactic-scale phenomenology.

The comparison highlights an uncomfortable asymmetry: BK achieves observational contact with 2 free parameters and a well-understood condensed matter mechanism. PE achieves mathematical elegance with 0 free parameters but has no observational contact after 30 sessions and 21 closed mechanisms. This is the price of operating at the GUT scale on a compact internal manifold: the dimensional reduction kills all dynamical signatures except those frozen into the ground state, which has not been found.

The constraint map is unaffected. No PE mechanism is closed by this comparison. The PE framework's probability remains at 5%/3% (panel/Sagan). What is closed is the **interpretation** that PE's phonons have any functional similarity to BK's phonons beyond shared vocabulary.

---

*Comparison grounded in: Baptista Papers 13-14 (KK geometry, gauge couplings), Connes Papers 04/07/12 (NCG axioms, spectral action, classification), Cosmic-Web Papers 07/18 (Berezhiani-Khoury), Session 23a (K-1e closure, selection rules), Session 28 (KC chain), Session 29 (frozen-state program, $k_{\text{transition}}$), Session 30 (master synthesis, adversarial review), permanent results registry.*
