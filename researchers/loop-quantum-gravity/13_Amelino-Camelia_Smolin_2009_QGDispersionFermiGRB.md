# Prospects for Constraining Quantum Gravity Dispersion with Near Term Observations

## Citation

- **Authors**: Giovanni Amelino-Camelia (Universita "La Sapienza" and Sez. Roma1 INFN), Lee Smolin (Perimeter Institute for Theoretical Physics)
- **Year**: 2009 (v3: 23 Jun 2009; preprint dated October 24, 2018 in the typeset; original submission June 2009)
- **arXiv**: 0906.3731v3 [astro-ph.HE]
- **Pages**: 34
- **Type**: Phenomenology paper -- review + new bounds + forward-looking proposal, tying quantum gravity theory frameworks (NLSB / LSB-EFT / DSR) to the first 10 months of Fermi LAT GRB observations.

## Abstract (verbatim)

"We discuss the prospects for bounding and perhaps even measuring quantum gravity effects on the dispersion of light using the highest energy photons produced in gamma ray bursts measured by the Fermi telescope. These prospects are brigher than might have been expected as in the first 10 months of operation Fermi has reported so far eight events with photons over $100\,MeV$ seen by its Large Area Telescope (LAT). We review features of these events which may bear on Planck scale phenomenology and we discuss the possible implications for the alternative scenarios for in-vacua dispersion coming from breaking or deforming of Poincare invariance. Among these are semi-conservative bounds, which rely on some relatively weak assumptions about the sources, on subluminal and superluminal in-vacuo dispersion. We also propose that it may be possible to look for the arrival of still higher energy photons and neutrinos from GRB's with energies in the range $10^{14} - 10^{17}\,eV$. In some cases the quantum gravity dispersion effect would predict these arrivals to be delayed or advanced by days to months from the GRB, giving a clean separation of astrophysical source and spacetime propagation effects."

## Position in the LQG / quantum-gravity-phenomenology arc

This is **not** a structural LQG paper; it is a **quantum-gravity phenomenology** paper co-authored by Smolin (one of the founders of LQG) and Amelino-Camelia (one of the originators of DSR and quantum-gravity phenomenology). It uses LQG-motivated dispersion ideas as one of three explicit testable frameworks alongside naive Lorentz Symmetry Breaking (NLSB) and Doubly Special Relativity (DSR). Within the LQG corpus this paper marks the **transition from theoretical speculation to observational confrontation** of Planck-scale Lorentz-modification scenarios:

- Before 2008: pre-Fermi GRB bound was only $M_{QG} > 2 \cdot 10^{17}\,GeV$ (Boggs et al. on GRB 021206), about two orders below $M_{Planck}$.
- After GRB 080916C (Fermi LAT 2008): Fermi collaboration achieves $M_{QG} > 1.3 \cdot 10^{18}\,GeV \approx 0.1\,M_{Planck}$ from a SINGLE GRB.

The paper then extends/sharpens these bounds using less-conservative assumptions and proposes a forward observational program at $10^{14}$ to $10^{17}\,eV$ with delays of days to months from GRBs, which would cleanly separate quantum-gravity dispersion from astrophysical source effects.

## The three testable scenarios for one-parameter dispersion

All three scenarios share the leading-order ultrarelativistic parametrization (Eq. 3):

$$E \simeq p + \frac{m^2}{2p} - s_\pm \frac{1}{2}\,\frac{E^{\alpha+1}}{M_{QG}^\alpha}$$

with $\alpha$ the suppression power (paper focuses on $\alpha=1$), $s_\pm \in \{-1,+1\}$ the sign parameter ($+1$ = subluminal, higher-energy photons go slower; $-1$ = superluminal). The frameworks differ on whether Lorentz symmetry is broken, deformed, or preserved and on how this fits inside an effective field theory.

### 2.1 NLSB -- Naive Lorentz Symmetry Breaking (without effective field theory)

- Modified dispersion of the form (Eq. 2): $m^2 = E^2 - p^2 + \Delta_{qg}(E, p^2; M_{QG})$
- **Unmodified** energy-momentum conservation (Eqs. 4-5): $E_a + E_b = E_c + E_d$, $p_a + p_b = p_c + p_d$
- Lorentz symmetry is BROKEN; framework is to be studied in a privileged frame (the CMB rest frame)
- **NO birefringence** (correction terms independent of polarization)
- Cannot be embedded in an EFT in a classical spacetime
- Status pre-Fermi: ONE strike against, from GZK observations (Auger)

### 2.2 LSB-EFT -- Lorentz Symmetry Breaking within effective field theory

- Initially proposed by Gambini and Pullin (1999) within LQG, but depends on a particular non-physical ground state -- NOT a definite LQG prediction
- Most useful framework: Myers-Pospelov (2003) -- assumes effects are linear in $l_{Planck}$ and characterized by an external four-vector $n^\alpha$, gives a unique correction to the electrodynamics Lagrangian (Eq. 6):

$$\mathcal{L} = -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} + \frac{1}{2 M_{Planck}}\, n^\alpha F_{\alpha\delta}\, n^\sigma \partial_\sigma (n_\beta \varepsilon^{\beta\delta\gamma\lambda} F_{\gamma\lambda})$$

- Spatially isotropic case (time-only $n^\alpha = (n_0, 0, 0, 0)$) with $\xi \equiv (n_0)^3$ reduces to (Eq. 7):

$$\mathcal{L} = -\frac{1}{4} F_{\mu\nu} F^{\mu\nu} + \frac{\xi}{2 M_{Planck}}\, \varepsilon^{jkl} F_{0j}\,\partial_0 F_{kl}$$

- PREDICTS BIREFRINGENCE: the two circular polarizations get OPPOSITE signs of $s_\pm$
- Status pre-Fermi: TWO strikes against, from birefringence bounds on polarized radio galaxies AND GZK

### 2.3 DSR -- Doubly / Deformed Special Relativity

- Adds a SECOND invariant scale (the Planck energy) to the relativity-of-inertial-frames principle without breaking Lorentz symmetry
- Realized via Hopf algebras, kappa-Poincare noncommutativity, "rainbow metric"
- Limit: $\hbar \to 0$ and $G_N \to 0$ with $M_{Planck} = \sqrt{\hbar / G_N}$ held fixed
- Example dispersion relation (Eq. 8):

$$0 = 8 M_{dsr}^2 \left[\cosh\!\left(\frac{E}{2 M_{dsr}}\right) - \cosh\!\left(\frac{m}{2 M_{dsr}}\right)\right] - p^2 e^{s_\pm E/(2 M_{dsr})}$$

  which for $E \ll M_{dsr}$ reduces to (Eq. 9): $E \simeq p + \frac{m^2}{2p} - s_\pm \frac{E^2}{2 M_{dsr}}$

- Alternative form (Eq. 10): $E^2 = p^2 / (1 + s_\pm E/(4 M_{dsr}))^2 + m^2$
- DEFORMED energy-momentum conservation (Eqs. 11-12):

$$E_a + E_b - \frac{s_\pm}{2 M_{dsr}} p_a p_b - E_c - E_d + \frac{s_\pm}{2 M_{dsr}} p_c p_d = 0$$
$$p_a + p_b - \frac{s_\pm}{2 M_{dsr}} (E_a p_b + E_b p_a) - p_c - p_d + \frac{s_\pm}{2 M_{dsr}} (E_c p_d + E_d p_c) = 0$$

- NO birefringence; same sign $s_\pm$ for all photons
- Status pre-Fermi: NO strikes against -- predicts GZK threshold unchanged because interactions evaluated in center-of-mass frame (where deformations are small)
- Heuristic arguments link DSR to LQG (refs [35, 36, 37]); proven in 2+1 dimensional gravity (refs [38, 39, 40]); no rigorous proof in 3+1 dimensions

### Distinguishability

NLSB and DSR predict the SAME leading-order dispersion (Eq. 3 with $\alpha=1$). They are distinguishable only via experiments where the modified transformation / conservation laws matter -- threshold experiments such as GZK and TeV-photon pair-production cutoffs. LSB-EFT predicts birefringence, distinguishing it from both NLSB and DSR via time-of-arrival vs polarization correlations.

## The basic dispersion arrival-time relation

For two photons emitted simultaneously at small redshift with energy difference $\Delta E$, the arrival-time difference is (Eq. 1 + Eq. 13):

$$\Delta t \simeq s_\pm \frac{\Delta E}{M_{QG}}\, L$$

For cosmological sources at large redshift $z$, the exact $\Lambda$CDM-corrected formula is (Eq. 14):

$$\Delta t = \frac{\Delta E}{M_{QG}}\, \frac{1}{H}\, \int_0^z dz\, \frac{1 + z}{\sqrt{\Omega_\Lambda + (1 + z^3)\, \Omega_{\rm Matter}}}$$

For photons in the GeV-TeV range and cosmological $L$, $\Delta t$ ranges from seconds to hours.

## Fermi LAT GRB catalogue (Table 1 -- 8 GRBs with > 1 GeV photons)

The paper compiles publicly-known information on 8 Fermi-LAT GRBs (extensive narrative in Appendix A):

| GRB | redshift | duration | counts|LAT | E_max | t_i^LAT | t_f^LAT |
|:----|:--------:|:--------:|:--------:|:-----:|:-------:|:-------:|
| 080916C | 4.35 | long | strong | 13 GeV | 4.5s | > 10^3 s |
| 081024B | -- | short | -- | 3 GeV | 0.2s | -- |
| 090510 | 0.9 | short | strong | > 1 GeV | < 1s | ~ 60s |
| 090328 | 0.7 | long | -- | > 1 GeV | -- | ~ 900s |
| 090323 | 4 | long | strong | > 1 GeV | -- | > 10^3 s |
| 090217 | -- | long | -- | -- | ~ 1s | ~ 20s |
| 080825C | -- | long | weak | 0.6 GeV | 3s | > 40s |
| 081215A | -- | -- | weak | 0.2 GeV | -- | -- |

The flagship event is **GRB 080916C**: ~200 photons > 100 MeV detected; redshift 4.35; the 13.2 GeV photon arrived 16.5s after the GBM trigger; Band-function fit holds from 8 keV to ~10 GeV (single emission mechanism conjectured). Most significant feature for QG: the onset of > 100 MeV emission (at $\simeq 4.5\,s$) coincides with the SECOND low-energy peak.

Common features across the 8 GRBs (Sec. 3.1.3): (1) LAT-event onset typically coincides with a SECOND GBM peak occurring seconds to fractions of a second after the first peak; (2) high-energy emission lasts much longer than low-energy emission; (3) the number of LAT detections is often relatively large.

## Bounds on subluminal dispersion ($s_\pm = +1$)

### Conservative Fermi bound (Eq. 15)

Using the 13.6 GeV photon of GRB 080916C arriving 16s after the trigger (Fermi collaboration, [15]):

$$M_{QG} > 1.3 \cdot 10^{18}\,GeV \approx 0.1\,M_P$$

### Less-conservative reasonably-robust bound (Eq. 16)

Counting time from the SECOND GBM peak (~4.5s after the first), under the assumption that the multi-GeV photons cannot have departed before the second peak:

$$M_{QG} > 1.8 \cdot 10^{18}\,GeV$$

### GRB 081024B sub-event analysis

A small peak of 300-500 MeV photons in coincidence with the second low-energy peak (0.2s after the first), then a 3 GeV photon 0.2s later. The 3 GeV-photon bound forces any QG delay for 300-500 MeV photons to be at most 0.04s. Therefore the observed 0.2s delay between first low-energy peak and 300-500 MeV photons is NOT a QG effect; it is astrophysical. **A hypothetical redshift measurement of $z_{081024B} > 0.35$ would yield $M_{QG} > 2.2 \cdot 10^{18}\,GeV$**.

### Comparison with AGN flares

MAGIC/HESS observations of Mk501 and PKS2155-304 (refs [47, 48]) reported an ESTIMATE (not bound) of $M_{QG} = (0.98^{+0.77}_{-0.30}) \cdot 10^{18}\,GeV$, favoring subluminal $s_\pm = +1$. The Fermi conservative bound $> 1.3 \cdot 10^{18}\,GeV$ is compatible at 1$\sigma$. The reasonably-conservative bound $> 1.8 \cdot 10^{18}\,GeV$ is in tension with this estimate.

## Bounds on superluminal dispersion ($s_\pm = -1$)

### Bound from photons that ARE seen (Eq. 17)

Reasoning: first two > 1 GeV photons from GRB 080916C arrived at 6.0 +/- 0.5 s and 7.0 +/- 0.5 s, within a first burster-activity interval estimated to last < 12s. So the 1 GeV photon could not have gained more than 5.5 s after a $z = 4.3$ trajectory. Yields:

$$M_{QG}^{[s_\pm = -1]} > 3.2 \cdot 10^{17}\,GeV$$

A near-identical bound ($M_{QG}^{[s_\pm = -1]} > 3.5 \cdot 10^{17}\,GeV$) follows from the > 100 MeV first peak. **This is the best superluminal bound in the literature at paper's date.**

### Bound from photons NOT seen (Sec. 3.3.2)

For LSB-EFT specifically: parity-violation predicts equal numbers of subluminal and superluminal photons (opposite circular polarizations). For a candidate value $\bar{M}_{QG}$, count the N high-energy photons within $[E_0, t_0]$ post-trigger such that $\delta t = (E_0/\bar{M}_{QG}) L \geq t_0$. If no photons in the same window appear pre-trigger and the source emits both helicities equally, the absence of N "missing" superluminal photons sets a confidence-level bound:

$$p_{\rm total} = \bar{p}_{\rm missed}^N$$

with $1 - p_{\rm total}$ the confidence that $M_{QG} > \bar{M}_{QG}$.

### "Conspiracy" caveat for superluminal bounds

The $\sim 3 \cdot 10^{17}\,GeV$ ceiling on superluminal bounds is set by the inability to exclude a source-side conspiracy: if $M_{QG}^{[s_\pm = -1]} \approx 4 \cdot 10^{17}\,GeV$, a 13.2 GeV photon at $z = 4.3$ would gain ~65 seconds in transit, requiring fine-tuned source-side emission to arrive 16 s AFTER (rather than well before) the trigger. The authors argue this disfavors $M_{QG}^{[s_\pm = -1]}$ values much below $M_{Planck}$ and suggest future work focus on $M_{QG}^{[s_\pm = -1]} \sim M_{Planck}$.

## Forward observational program (Sec. 4)

### 4.1 TeV photons

For $M_{QG} \sim M_{Planck}$, a 10 TeV photon should acquire $\sim 10^3$ s delay from $z = 4$. Manageable for telescopes that can re-point (e.g., MAGIC). The IR-background pair-production absorption argument is NOT a reason to skip these searches, because the NLSB framework itself predicts reduced absorption (refs [6, 69-72]).

### 4.2 Photons at $10^{14}$ to $10^{17}$ eV

For $M_{QG} \sim M_{Planck}$, a $10^{16}\,eV$ photon would acquire $\sim 10^6\,s$ delay ($\sim$ a month) from $z = 4$. Target: Auger cosmic-ray observatory. **A single such detection in a window consistent with QG-predicted lower-energy delays could decisively break the astrophysical-vs-QG degeneracy.**

### 4.3 VHE neutrinos

ICECUBE could play a decisive role. Neutrinos have the advantage of zero EM absorption. Production process: $p + \gamma \to X + \pi^+ \to X + e^+ + \nu_e + \nu_\mu + \bar{\nu}_\mu$. Realistic rate estimates suggest few neutrinos at best. Even a SINGLE such detection at correct delay would be decisive.

### 4.4 Forward and backward in time -- superluminal photons / neutrinos

If $M_{QG}^{[s_\pm = -1]} \sim M_{Planck}$: a multi-TeV photon emitted at the second peak of GRB 080916C would have arrived several seconds BEFORE the GRB trigger; a $10^{16}\,eV$ photon or neutrino would have arrived $10^5$ s before the trigger. The only existing weak evidence in this direction is Plunkett et al. (1995) [80]: ~100 TeV photons from GRB 910511 some 40 minutes BEFORE the GBM trigger, at 2.9$\sigma$.

## Two-parameter models (Sec. 5)

### 5.1 Fuzzy dispersion

If a source emits a sharp burst of duration $\Delta t^*$, quantum-mechanical uncertainty $\Delta E \gtrsim \hbar/\Delta t^*$ propagating through dispersion $v(E) = 1 - \eta E/M_{Planck}$ produces a measured spread (Eq. 19-20):

$$\Delta t_{\rm meas} \approx \eta T \hbar / (M_{Planck} \Delta t^*)$$

The full phenomenological "fuzzy" model adds an independent fluctuation contribution (Eq. 21):

$$v(E) \simeq 1 - \eta E/M_{Planck} \pm \eta/(M_{Planck} \Delta t^*) \pm \eta_f E/M_{Planck}$$

with $\eta_f$ a free phenomenological parameter expected within 1-2 orders of magnitude of unity. **Advantage**: GZK threshold is essentially unaffected (ref [84]). Averaged arrival times remain one-parameter; individual arrival times become stochastic.

### 5.2 Mixed-parity dispersion

Motivated by the chiral asymmetry inherent in LQG via the **Immirzi parameter** (refs [85, 86]). LSB-EFT predicts $\delta v = -\beta \langle s \rangle E/M_{QG}$ (parity-odd via chirality $\langle s \rangle \in [-1, +1]$); NLSB/DSR predict $\delta v = -\alpha E/M_{QG}$ (parity-even). The hybrid (Eq. 22):

$$\delta v = -(\alpha + \beta \langle s \rangle)\, \frac{E}{M_{QG}}$$

with $\alpha + \beta = 1$. For random helicity, this induces stochastic arrival times (Eq. 23):

$$\delta t = (\alpha + \beta \langle s \rangle)\,\frac{E}{M_{QG}}\,L$$

## Conclusions and open questions

### Conclusions

- The single-GRB conservative bound $M_{QG} > 0.1\,M_P$ from GRB 080916C is a striking near-Planck-scale result.
- Plausible future bounds could push to $M_{QG} \sim 4 \cdot 10^{20}\,GeV$ (10$^2 M_P$) -- e.g., a 20 GeV photon within 0.1s of the LAT peak at z = 4.5 in a short burst.
- Detection of nonzero $M_{QG}$ is harder than bounding due to astrophysical-source / QG degeneracy.
- $10^{14}$ to $10^{17}\,eV$ photon/neutrino observations would CLEANLY separate the two effects via the day-to-month delay scale -- "even a single detection could provide crucial input."
- Pre-trigger photon/neutrino detection at TeV-EeV from a known GRB would be robust evidence for superluminal QG dispersion.

### Open questions named by the paper

- No rigorous LQG -> DSR derivation in 3+1 dimensions; only partial results in 2+1d (refs [35, 38-40]).
- DSR has not been fully incorporated into realistic interacting quantum field theories.
- Whether the LSB-EFT Myers-Pospelov framework's natural anisotropy in the CMB frame is consistent with current bounds.
- The role of the Immirzi parameter in generating mixed-parity photon dispersion has NOT been shown -- "it has definitely not been shown that this leads to a mixed parity dispersion of photon velocities but let us suppose it does."
- Distinguishing source-side astrophysics from in-vacuo dispersion requires methodology that "models or averages out" astrophysical effects; this is "much harder than putting a bound."

## Central terms / definitions

| Term | Definition (per paper text) |
|:-----|:----------------------------|
| **$M_{QG}$** | Quantum-gravity scale governing leading-order dispersion; expected within "a few orders of magnitude" of $M_{Planck} = 1/\sqrt{G_N}$ |
| **$s_\pm$** | Sign parameter $\in \{-1, +1\}$; $+1$ = subluminal (higher-E slower), $-1$ = superluminal (higher-E faster) |
| **$\alpha$** | Suppression power; $\alpha = 1$ linear, $\alpha = 2$ quadratic; paper focuses on $\alpha = 1$ |
| **NLSB** | Naive Lorentz Symmetry Breaking -- modified dispersion (Eq. 2), unmodified energy-momentum conservation, broken Lorentz, no birefringence, no EFT embedding |
| **LSB-EFT** | Lorentz-Symmetry Breaking in Effective Field Theory -- the Myers-Pospelov framework; predicts birefringence for $\alpha = 1$ |
| **DSR** | Doubly / Deformed Special Relativity -- second invariant scale (Planck energy), Lorentz preserved as deformed Hopf-algebra symmetry; modified energy-momentum conservation (Eqs. 11-12) |
| **Band function** | Empirical broken-power-law function (Band et al. [62]) that fits GRB time-resolved spectra |
| **GBM** | Gamma-ray Burst Monitor onboard Fermi (low-energy, < 5 MeV typically) |
| **LAT** | Large Area Telescope onboard Fermi (high-energy, > 100 MeV) |
| **Fuzzy dispersion** | Two-parameter scenario adding stochastic fluctuation to the dispersion (Eq. 21); GZK-preserving |
| **Mixed-parity dispersion** | Two-parameter scenario with both parity-even and parity-odd dispersion contributions (Eq. 22); motivated by Immirzi-parameter chirality in LQG |

## Connection to LQG -- broader-program function

This paper sits at the intersection of:

1. **Phenomenological-LQG output**: Smolin's broader program of "falsifiable predictions from semiclassical quantum gravity" (refs [36, 37]) heuristically argues DSR-like dispersion arises in the LQG semiclassical limit. The Immirzi-parameter chirality (refs [85, 86]) is invoked as an LQG-specific motivation for mixed-parity dispersion (Sec. 5.2).
2. **LQG-rooted but non-canonical**: the Gambini-Pullin LSB-EFT scenario (ref [7]) is explicitly noted as LQG-rooted but "dependent on the assumption of a particular and non-physical ground state for that theory. Thus, their scenario should not be viewed as a definite prediction of loop quantum gravity."
3. **Theorist accountability message**: paper closes with explicit warning to QG theorists: "we suggest urgent attention be given to any possibility of deriving predictions for these observations from theories of quantum gravity, otherwise it may be only a matter of months to a year or two before we theorists are demoted to the role of postdictors of great experimental discoveries."

## Connection to phonon-exflation framework

Substrate-first framing: the LQG-motivated dispersion features identified here are themselves LABORATORY-IN observables on photons that propagate through the substrate; the relevant phonon-exflation IS-side comparison is at the level of what substrate features could give rise to modified low-energy effective dispersion, and how phonon-exflation's discrete spectral content (D_K eigenvalues at L_max = 10/12) compares to LQG's discrete area/volume operators as the kinematical source of the modification.

### Structural parallels

- **Discrete substrate -> emergent dispersion**: in LQG (paper context, refs [18-21, 35-37]), discrete spin-network area/volume operators carry a non-trivial Planck-scale structure that motivates modified dispersion. The phonon-exflation analog is the finite spectral triple $(A_K, H_K, D_K)$ with $A_K = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$ and 155,984 eigenvalues at $L_{\max} = 10$; emergent EM-field propagation arises from the spectral action's $a_4$ Yang-Mills coefficient.

- **Single Planck-scale parameter**: paper's $M_{QG}$ (a single scale near $M_{Planck}$) is the LQG-side analog of phonon-exflation's $\tau_{fold} = 0.190$ Jensen-deformation parameter. The two parameterize different physics (LQG: dispersion modification; phonon-exflation: spectral-action gradient driving cosmogenesis transit) but share the role of single-scalar parameter governing departures from a fiducial relativistic geometry.

- **Immirzi parameter / chirality analog**: paper Sec. 5.2 attributes mixed-parity dispersion to the LQG Immirzi parameter as fundamental chiral asymmetry. The phonon-exflation chiral structure lives in the Jensen-deformation TT-mode + BDI parity-twin (CH, CepsH) cohomology classes (per S86 W-11 instance). Both frameworks identify a parity-axis as a fundamental QG-side prediction with potentially observable polarization-dependent signatures.

### Non-parallels (where the frameworks diverge)

- **Observable focus**: this paper restricts attention to photon dispersion as the canonical low-energy QG-observable. Phonon-exflation's primary observables are CMB-side ($n_s = 0.9561$, low-r tensor-to-scalar, GGE relic from Parker pair production at $\tau_{fold}$) plus BAO/dark-energy ($w \neq -1$ via Volovik vacuum tracking). Time-of-arrival dispersion is NOT a primary phonon-exflation observable.

- **Lorentz status**: phonon-exflation does NOT predict broken or deformed Lorentz invariance at observable scales -- the substrate is c-bounded for propagation (per project memory `project_substrate-not-c-limited.md`); c bounds propagation ACROSS the substrate, not the substrate's own dynamics. The frameworks therefore disagree on whether photons of cosmological-GeV energies should show in-vacuo dispersion.

- **Singularity-resolution mechanism**: paper does NOT directly discuss singularity resolution (that is the LQC sister-program covered by Ashtekar-Pawlowski-Singh 2006, paper #08 in this corpus). Phonon-exflation's $\tau_{fold} = 0.190$ supersonic transit is an IMPULSIVE non-equilibrium acoustic-white-hole transit, distinct from LQC's quasi-equilibrium polymer-Friedmann bounce. The QG-dispersion observation discussed here is a low-energy diagnostic that operates AFTER any cosmogenesis transit; the cosmogenesis mechanisms themselves are not the paper's subject.

### Cross-framework structural-parallel summary

The Amelino-Camelia-Smolin paper is the phonon-exflation analog of "Pillar III (substrate cocycle observables) IS the dispersive medium; Pillar II (electromagnetic dispersion in cosmological propagation) IS the laboratory-IN observable; bridge map = an unspecified phenomenological transfer of substrate-Planck-scale discreteness into a low-energy effective photon dispersion." In phonon-exflation language, the bridge is presented at PHENOMENOLOGICAL level only -- ref [7]'s Gambini-Pullin computation in LQG is paper's own acknowledged example, but explicitly not a definite LQG prediction. **Open question for the corpus**: which (if any) of phonon-exflation's substrate-IS observables produces a phenomenologically equivalent in-vacuo dispersion signal at GeV-TeV scales? If none, then the Fermi LAT non-detection of strict $M_{QG} \ll M_{Planck}$ dispersion is compatible with phonon-exflation but not directly diagnostic of it.

## Provenance

PDF source: `downloads/loop-quantum-gravity/0906.3731v3.pdf` (372 KB, 34 pages). Read via /pdf skill chunking (4 chunks of 10/10/10/4 pages). All quoted equations and numerical bounds verified against the chunked-PDF text. No supplementary information used beyond the paper itself. arXiv ID 0906.3731v3 confirmed from page-1 header.
