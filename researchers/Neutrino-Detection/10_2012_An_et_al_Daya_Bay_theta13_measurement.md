# Observation of Electron-Antineutrino Disappearance at Daya Bay

**Authors:** F. P. An et al. (Daya Bay Collaboration)
**Year:** 2012
**Journal:** *Physical Review Letters*, **108**(17), 171803

---

## Abstract

The Daya Bay Reactor Neutrino Experiment measured the neutrino mixing angle $\theta_{13}$ by observing the disappearance of electron antineutrinos from six nuclear reactor cores at baselines of 0.5 km (near detectors) and 1.6 km (far detector). Using six identically designed antineutrino detectors -- two at the Daya Bay near site, one at the Ling Ao near site, and three at the far site -- the collaboration employed a relative measurement strategy that cancels most systematic uncertainties. In 55 days of data, they observed a rate deficit at the far site relative to the near sites, obtaining $\sin^2(2\theta_{13}) = 0.092 \pm 0.016\text{(stat)} \pm 0.005\text{(syst)}$, excluding $\theta_{13} = 0$ at $5.2\sigma$. This measurement established that $\theta_{13}$ is non-zero and surprisingly large, opening the door to CP violation measurements in the lepton sector and providing the last missing angle of the PMNS neutrino mixing matrix. The final Daya Bay result (2022, full dataset) refined this to $\sin^2(2\theta_{13}) = 0.0851 \pm 0.0024$.

---

## Historical Context

### The Missing Angle

By 2010, the three-flavor neutrino oscillation framework was well established with two of three mixing angles measured: $\theta_{12} \approx 34^\circ$ (solar/KamLAND) and $\theta_{23} \approx 45^\circ$ (atmospheric/Super-K). The third angle, $\theta_{13}$, controlled the coupling of $\nu_e$ to the third mass eigenstate $\nu_3$ and was known only to be small:

$$\sin^2(2\theta_{13}) < 0.17\quad(90\%\;\text{CL, CHOOZ, 1999})$$

The CHOOZ experiment in France had set this upper limit using a single detector at 1 km from the Chooz nuclear reactors, limited by the 2.8% systematic uncertainty on the reactor antineutrino flux prediction.

### Why theta_13 Matters

The value of $\theta_{13}$ is the gateway to the entire next generation of neutrino physics:

**CP violation:** The Jarlskog invariant, which controls the magnitude of CP-violating effects in neutrino oscillation, is proportional to $\sin\theta_{13}$:

$$J_{CP} = \frac{1}{8}\sin 2\theta_{12}\;\sin 2\theta_{23}\;\sin 2\theta_{13}\;\cos\theta_{13}\;\sin\delta_{CP}$$

If $\theta_{13} = 0$, then $J_{CP} = 0$ regardless of $\delta_{CP}$, and CP violation in neutrino oscillation would be unobservable. The question "is $\theta_{13}$ zero?" was therefore a binary gate: if yes, a large class of experiments becomes pointless; if no, a rich physics program opens up.

**Mass hierarchy:** The sensitivity of long-baseline experiments (like NOvA and DUNE) to the neutrino mass hierarchy depends on the magnitude of $\theta_{13}$. A large $\theta_{13}$ makes hierarchy determination feasible with current-generation experiments.

**Leptogenesis:** Baryogenesis through leptogenesis (Fukugita-Yanagida, 1986) requires CP violation in the lepton sector. While leptogenesis at high energy depends on different CP phases than low-energy oscillation, a non-zero $\theta_{13}$ is a necessary (though not sufficient) condition for the PMNS phase $\delta_{CP}$ to be physical.

**Tri-bimaximal mixing:** The popular Harrison-Perkins-Scott "tri-bimaximal" (TBM) mixing ansatz predicted exactly $\theta_{13} = 0$, $\sin^2\theta_{12} = 1/3$, and $\sin^2\theta_{23} = 1/2$. A non-zero $\theta_{13}$ would rule out TBM as an exact symmetry and redirect flavor model building.

### The Race to Measure theta_13

By 2010, three reactor experiments were under construction specifically to measure $\theta_{13}$:

1. **Double Chooz** (France): One near, one far detector at the Chooz reactors. Started far-detector-only data taking in 2011.
2. **Daya Bay** (China): Six detectors at three sites near the Daya Bay and Ling Ao nuclear power plants. Most sensitive design.
3. **RENO** (South Korea): Two identical detectors at the Yonggwang reactor complex.

All three employed the same basic strategy: compare the $\bar{\nu}_e$ rate at a near site (before oscillation develops) with a far site (at the oscillation maximum for $\Delta m^2_{32}$).

---

## Key Arguments and Derivations

### I. Oscillation Physics at Short Baseline

At baselines of 1-2 km and antineutrino energies of 2-8 MeV, the dominant oscillation channel is driven by $\Delta m^2_{32}$:

$$P(\bar{\nu}_e \to \bar{\nu}_e) \approx 1 - \sin^2(2\theta_{13})\;\sin^2\left(\frac{\Delta m^2_{32} L}{4E}\right) - \cos^4\theta_{13}\;\sin^2(2\theta_{12})\;\sin^2\left(\frac{\Delta m^2_{21} L}{4E}\right)$$

The second term (driven by $\Delta m^2_{21}$) is negligible at 1-2 km baselines because $\Delta m^2_{21} L / 4E \ll 1$:

$$\frac{\Delta m^2_{21} L}{4E} = 1.267 \times \frac{7.9 \times 10^{-5} \times 1600}{3.5} \approx 0.046\;\text{rad}$$

So $\sin^2(0.046) \approx 0.002$, contributing less than 0.2% and entirely negligible compared to the $\theta_{13}$ term.

The first oscillation maximum occurs at:

$$\frac{\Delta m^2_{32} L}{4E} = \frac{\pi}{2} \implies L = \frac{2\pi E}{\Delta m^2_{32}} \approx \frac{2\pi \times 3.5}{2.5 \times 10^{-3}} \times \frac{1}{1.267} \approx 1750\;\text{m}$$

So the far detector at 1.6 km is near the first oscillation maximum, where the sensitivity to $\theta_{13}$ is largest.

### II. The Daya Bay Reactor Complex

The Daya Bay Nuclear Power Station and the adjacent Ling Ao Nuclear Power Station together house six reactor cores:

- **Daya Bay**: 2 cores, each 2.9 GW$_{th}$
- **Ling Ao I**: 2 cores, each 2.9 GW$_{th}$
- **Ling Ao II**: 2 cores, each 2.9 GW$_{th}$

Total thermal power: $\sim$17.4 GW$_{th}$, making this one of the most powerful neutrino sources in the world. The total $\bar{\nu}_e$ emission rate was approximately $3.5 \times 10^{21}$ per second.

### III. Detector Design

Each of the six antineutrino detectors (ADs) was a nested-cylinder design:

**Inner Acrylic Vessel (IAV):** 3.1 m diameter, 3.1 m height, containing 20 tonnes of 0.1% gadolinium-doped liquid scintillator (Gd-LS) as the $\bar{\nu}_e$ target.

**Outer Acrylic Vessel (OAV):** 4.0 m diameter, containing 22 tonnes of undoped liquid scintillator as a gamma catcher -- capturing gamma rays that escape the target volume.

**Stainless Steel Vessel (SSV):** 5.0 m diameter, containing 40 tonnes of mineral oil as a buffer. 192 8-inch Hamamatsu photomultiplier tubes (PMTs) were mounted on the SSV wall, viewing the scintillator volumes.

**Automated calibration system:** LED pulsers, $^{60}$Co, $^{68}$Ge, and $^{241}$Am-$^{13}$C sources deployed along three axes.

The gadolinium doping was the key innovation compared to KamLAND. When a neutron from IBD is captured on gadolinium:

$$n + \text{Gd} \to \text{Gd}^* \to \text{Gd} + \gamma\text{'s}\;(\text{total}\;\sim 8\;\text{MeV})$$

The 8 MeV gamma cascade is much more energetic than the 2.2 MeV gamma from neutron capture on hydrogen (used by KamLAND), providing:

1. A much higher energy threshold for the delayed signal, reducing accidental backgrounds.
2. A shorter capture time ($\sim$28 $\mu$s vs $\sim$200 $\mu$s), reducing the coincidence time window and further suppressing accidentals.
3. Higher capture efficiency within the Gd-LS volume ($\sim$84%).

### IV. Near/Far Relative Measurement

The crucial insight of the Daya Bay design was the relative measurement. The absolute prediction of the reactor $\bar{\nu}_e$ flux has a $\sim$2-3% uncertainty (from reactor power, fission fractions, and $\bar{\nu}_e$ spectra per fission). CHOOZ was limited by this uncertainty. Daya Bay circumvented it entirely.

The near detectors at $\sim$0.5 km measure the unoscillated $\bar{\nu}_e$ rate:

$$R_{near} = \phi_0 \cdot \sigma_{IBD} \cdot \epsilon \cdot N_p / L_{near}^2$$

The far detectors at $\sim$1.6 km measure the oscillated rate:

$$R_{far} = \phi_0 \cdot \sigma_{IBD} \cdot \epsilon \cdot N_p \cdot \langle P_{surv} \rangle / L_{far}^2$$

The ratio:

$$\frac{R_{far}}{R_{near}} \cdot \frac{L_{far}^2}{L_{near}^2} = \langle P_{surv} \rangle \approx 1 - \sin^2(2\theta_{13})\left\langle\sin^2\left(\frac{\Delta m^2_{32} L_{far}}{4E}\right)\right\rangle$$

In this ratio, the reactor flux $\phi_0$, cross section $\sigma_{IBD}$, and (to first order) the detection efficiency $\epsilon$ all cancel. The residual systematic uncertainty on the far/near ratio was reduced to $\sim$0.2% -- more than an order of magnitude better than CHOOZ.

In practice, the analysis accounted for the different baselines to each reactor core for each detector:

$$N_d^{predicted} = \epsilon_d \sum_r \frac{N_r}{4\pi L_{dr}^2}\;\langle\sigma P_{surv}(L_{dr}, E; \theta_{13})\rangle$$

where $d$ labels detectors and $r$ labels reactors, and $\epsilon_d$ is the relative efficiency of detector $d$ (calibrated to $<$0.2% using the identical detector design and shared calibration sources).

### V. The First Result (2012)

In 55 days of data (December 2011 -- February 2012), the far site observed:

- **Observed events (far):** 9901
- **Expected events (far, no oscillation):** $10587 \pm 161$

The deficit at the far site relative to near-site extrapolation yielded:

$$R = 0.940 \pm 0.011\text{(stat)} \pm 0.004\text{(syst)}$$

Fitting for $\theta_{13}$:

$$\sin^2(2\theta_{13}) = 0.092 \pm 0.016\text{(stat)} \pm 0.005\text{(syst)}$$

The null hypothesis ($\theta_{13} = 0$) was excluded at $5.2\sigma$. This was the first definitive measurement of $\theta_{13}$.

### VI. Simultaneous Measurements

Within weeks, the two competing experiments reported consistent results:

- **RENO** (South Korea): $\sin^2(2\theta_{13}) = 0.113 \pm 0.013\text{(stat)} \pm 0.019\text{(syst)}$ at $4.9\sigma$ (April 2012)
- **Double Chooz** (France): $\sin^2(2\theta_{13}) = 0.109 \pm 0.030\text{(stat)} \pm 0.025\text{(syst)}$ at $2.9\sigma$ (far-only, 2011-2012)

All three were consistent, with Daya Bay achieving the highest significance due to its larger detector mass, higher reactor power, and better systematic control.

### VII. Final Daya Bay Result (2022)

After collecting data from 2011 to 2020 with the full eight-detector configuration:

$$\sin^2(2\theta_{13}) = 0.0851 \pm 0.0024$$

$$|\Delta m^2_{32}| = (2.466 \pm 0.060) \times 10^{-3}\;\text{eV}^2\;\text{(normal ordering)}$$

The relative precision on $\sin^2(2\theta_{13})$ was 2.8%, making this the most precisely known neutrino mixing parameter.

---

## Physical Interpretation

### The PMNS Matrix Completed

With $\theta_{13}$ measured, all three mixing angles of the PMNS matrix are known:

$$U_{PMNS} = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta} \\ -s_{12}c_{23} - c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23} - s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13} \\ s_{12}s_{23} - c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23} - s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13} \end{pmatrix}$$

with $c_{ij} = \cos\theta_{ij}$, $s_{ij} = \sin\theta_{ij}$, and:

| Parameter | Value |
|:----------|:------|
| $\theta_{12}$ | $33.4^\circ \pm 0.8^\circ$ |
| $\theta_{23}$ | $49.0^\circ \pm 1.3^\circ$ |
| $\theta_{13}$ | $8.6^\circ \pm 0.1^\circ$ |
| $\delta_{CP}$ | Unknown ($\sim 200^\circ$ hints) |

The element $U_{e3} = \sin\theta_{13}\;e^{-i\delta_{CP}} \approx 0.15\;e^{-i\delta_{CP}}$ is small but non-zero.

### Tri-Bimaximal Mixing Ruled Out

The TBM ansatz predicts $\theta_{13} = 0$ exactly. With $\sin^2(2\theta_{13}) = 0.085$, corresponding to $\theta_{13} = 8.6^\circ$, TBM is ruled out as an exact symmetry. This redirected the theoretical landscape from discrete symmetries ($A_4$, $S_4$) that predict TBM toward models with small perturbations that generate a non-zero $\theta_{13}$.

### CP Violation Becomes Accessible

The Jarlskog invariant evaluates to:

$$J_{CP} = \frac{1}{8}\sin(2 \times 33.4^\circ)\;\sin(2 \times 49.0^\circ)\;\sin(2 \times 8.6^\circ)\;\cos(8.6^\circ)\;\sin\delta_{CP}$$

$$J_{CP} \approx 0.033\;\sin\delta_{CP}$$

The maximum possible CP violation ($\delta_{CP} = \pm 90^\circ$) gives $J_{CP} \approx \pm 0.033$, which is about 1000 times larger than the CKM Jarlskog invariant ($J_{CKM} \approx 3 \times 10^{-5}$). This large potential CP violation in the lepton sector makes experimental detection feasible and is a primary physics goal of DUNE and T2HK.

### Implications for Leptogenesis

While the connection between low-energy PMNS CP violation and high-energy leptogenesis is model-dependent, a non-zero $\theta_{13}$ means the PMNS phase $\delta_{CP}$ is physical and can in principle be measured. In specific seesaw models, the high-energy CP phases are related to the low-energy observables, and a measurement of $\delta_{CP}$ constrains the leptogenesis parameter space.

---

## Impact and Legacy

### The Breakthrough Prize

The Daya Bay Collaboration (jointly with KamLAND, SNO, Super-K, T2K, K2K, Sudbury, and others) shared the 2016 Breakthrough Prize in Fundamental Physics "for the fundamental discovery of neutrino oscillation, revealing a new frontier beyond, and possibly above, the standard model of particle physics."

### Foundation for Next-Generation Experiments

Daya Bay's precise $\theta_{13}$ measurement directly enabled the design of:

- **DUNE** (Deep Underground Neutrino Experiment): long-baseline $\nu_\mu \to \nu_e$ appearance experiment sensitive to $\delta_{CP}$ and mass hierarchy.
- **Hyper-Kamiokande (T2HK)**: upgraded T2K with 260 kt water Cherenkov detector.
- **JUNO** (Jiangmen Underground Neutrino Observatory): 20 kt liquid scintillator at $\sim$53 km from reactors, optimized for mass hierarchy determination.

### Reactor Antineutrino Anomaly

Daya Bay's precise near-detector measurements also contributed to the "reactor antineutrino anomaly" -- a $\sim$5% deficit of observed $\bar{\nu}_e$ relative to updated flux predictions (Huber-Mueller model). While initially interpreted as evidence for sterile neutrinos, Daya Bay's measurement of the $^{235}$U and $^{239}$Pu flux components suggested the anomaly is likely due to an overestimate of the $^{235}$U flux prediction rather than new physics.

---

## Connection to Phonon-Exflation Framework

### theta_13 from Internal Geometry

In the phonon-exflation framework, all three neutrino mixing angles are determined by the eigenvector structure of the internal Dirac operator $D_K(s)$. The mixing angle $\theta_{13}$ controls the overlap between the electron neutrino flavor state and the third mass eigenstate:

$$\sin\theta_{13} = |\langle \nu_e | \nu_3 \rangle_K|$$

The fact that $\theta_{13}$ is small but non-zero ($\sin\theta_{13} \approx 0.15$) has a geometric interpretation: the electron neutrino wavefunction on $K = \text{SU}(3)$ has a small but non-vanishing projection onto the heaviest neutrino mass eigenmode. In the bi-invariant limit ($s = 0$), symmetry may force $\theta_{13} = 0$ exactly (analogous to TBM). The Jensen deformation $s \neq 0$ breaks this symmetry and generates a non-zero $\theta_{13}$ proportional to the deformation:

$$\theta_{13}(s) \sim c \cdot s + O(s^2)$$

This is a testable prediction: the framework should produce $\theta_{13} \approx 8.6^\circ$ at the same deformation parameter $s_0$ that gives the correct gauge coupling ratios and mass ratios.

### CP Phase as Geometric Phase

The CP-violating phase $\delta_{CP}$ in the PMNS matrix has a natural interpretation in the framework as a geometric (Berry) phase associated with the internal Dirac operator. When the eigenvectors of $D_K(s)$ are transported along a path in parameter space, they acquire geometric phases that depend on the curvature of the eigenstate bundle. The CP phase $\delta_{CP}$ is one such geometric phase, determined entirely by the geometry of $K$ and the deformation $s$.

Session 17a result D-1 showed that $[J, D_K(s)] = 0$ identically, confirming CPT invariance. However, this does not forbid CP violation -- the real structure $J$ commutes with $D_K$, but the CP phase arises from the relationship between mass and flavor eigenstates, which depends on the full structure of the spectral triple $(A, H, D; J, \gamma)$.

### Three Generations from Geometry

The number of neutrino generations (three) is an output of the framework, not an input. Session 17a result B-4 established the $Z_3 = (p-q)\;\text{mod}\;3$ partition of the 28 irreducible representations of $\text{SU}(3)$. If this $Z_3$ grading corresponds to generation number (as suggested by Baptista Paper 18, Appendix E), then exactly three generations of neutrinos emerge from the geometry of the compactification manifold. This is one of the deepest structural predictions of the framework.

### Constraints on D_K(s) from Daya Bay

The final Daya Bay value $\sin^2(2\theta_{13}) = 0.0851 \pm 0.0024$ is now the most precisely known neutrino oscillation parameter. Combined with $\Delta m^2_{32}$, it constrains the third row and column of the PMNS matrix, which in the framework is determined by the highest-lying neutrino mass eigenmode of $D_K(s_0)$. The precision of the Daya Bay measurement ($\sim$3%) provides a stringent test: the framework must reproduce this value to within this precision or be falsified.

The fact that $\theta_{13}$ is neither zero (as TBM predicts) nor maximal (as some models predict) but is a specific intermediate value ($8.6^\circ$) is naturally accommodated in the framework, where mixing angles take whatever values the geometry dictates. There is no reason for the overlap integrals on $\text{SU}(3)$ to produce any special "magic" values -- the observed angles are simply what the Jensen-deformed geometry gives.
