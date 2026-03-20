# On the Movement of Small Particles Suspended in Stationary Liquids Required by the Molecular-Kinetic Theory of Heat

**Author:** Albert Einstein
**Year:** 1905
**Journal:** *Annalen der Physik*, **17**, 549--560

---

## Abstract

Einstein demonstrates that the molecular-kinetic theory of heat predicts that microscopic particles suspended in a liquid will undergo a persistent, observable random motion driven by thermal molecular bombardment. He derives a quantitative diffusion equation for the distribution of such particles and shows that the mean-squared displacement grows linearly with time: $\langle x^2 \rangle = 2Dt$, where the diffusion coefficient $D = k_B T/(6\pi\eta a)$ depends on temperature, fluid viscosity, and particle radius. This relation provides a direct experimental method for determining Avogadro's number $N_A$ and, through it, the sizes and existence of atoms. The paper thus transformed the atomic hypothesis from a useful but debated theoretical postulate into an experimentally testable and ultimately confirmed physical fact.

---

## Historical Context

### The Atomic Debate at the Turn of the Century

It is difficult from a modern vantage to appreciate how contested the reality of atoms was in 1905. The atomic hypothesis -- that matter consists of discrete, indivisible units -- was enormously useful in chemistry (Dalton's law of definite proportions, Avogadro's hypothesis, the periodic table) and in the kinetic theory of gases (Maxwell, Boltzmann). However, a significant fraction of the physics community, led by Ernst Mach and Wilhelm Ostwald, regarded atoms as convenient fictions -- mathematical devices for organizing empirical regularities, not descriptions of physical reality.

Mach's positivist philosophy demanded that scientific theories refer only to observable quantities. Since no one had "seen" an atom, Mach argued that atomic theory was metaphysics, not physics. Ostwald championed "energetics" -- the idea that energy, not matter, was the fundamental substance, and that thermodynamics could be formulated without reference to atoms.

Ludwig Boltzmann, the principal defender of atomism, suffered enormously from these philosophical attacks. His statistical mechanics -- the derivation of thermodynamic behavior from molecular dynamics -- was dismissed by some as mathematically interesting but physically meaningless.

### Brownian Motion

The phenomenon that Einstein analyzed had been known since 1827, when botanist Robert Brown observed the perpetual jittering of pollen grains suspended in water. The motion was persistent (it did not die out), irregular, and affected particles of all compositions -- it was clearly not biological in origin. Various explanations had been proposed (convection, electrical effects, capillary forces), but none was quantitatively satisfactory.

By the early 1900s, some physicists (Gouy in particular) had argued qualitatively that Brownian motion was caused by molecular impacts. But no quantitative theory existed. Einstein, remarkably, was not certain that the phenomenon he was analyzing was identical to Brown's observation -- he notes in the paper's introduction that the motion he predicts "is possibly identical" with Brownian motion.

### Einstein's Motivation

Einstein's primary goal was not to explain Brownian motion per se but to demonstrate that the molecular-kinetic theory made definite, testable predictions about macroscopic phenomena. If atoms exist and obey statistical mechanics, then suspended particles MUST exhibit diffusive random motion with specific, calculable properties. An experimental test would therefore be a test of the atomic hypothesis itself.

---

## Key Arguments and Derivations

### I. Osmotic Pressure of Suspended Particles

Einstein begins with a bold conceptual move: he treats the suspended particles as a "solute" in thermodynamic equilibrium with the surrounding fluid. If the particles obey the equipartition theorem (each translational degree of freedom carries average energy $\frac{1}{2}k_BT$), then a collection of $n$ particles per unit volume exerts an osmotic pressure:

$$p = nk_BT = \frac{n}{N_A}RT$$

where $R = N_A k_B$ is the gas constant. This equation is the van't Hoff law applied to suspended particles -- an audacious extension, since the "solute molecules" here are colloidal particles $10^3$--$10^4$ times larger than atoms.

The justification is purely thermodynamic: if the equipartition theorem applies (which it must, if the molecular-kinetic theory is correct), then the osmotic pressure formula holds regardless of the "molecule" size.

### II. The Balance Between Osmotic Pressure and Friction

Consider a vertical column of fluid containing suspended particles in a gravitational field (or any external potential). In equilibrium, the osmotic pressure gradient balances the external force. More generally, in any configuration with a gradient of particle concentration $n(x,t)$, the osmotic pressure gradient creates a drift:

$$f_{osmotic} = -\frac{\partial p}{\partial x} = -k_BT\frac{\partial n}{\partial x}$$

per unit volume. This drives a flux of particles:

$$J_{osmotic} = -D\frac{\partial n}{\partial x}$$

where $D$ is the diffusion coefficient.

Simultaneously, an external force $F$ on each particle causes a drift velocity $v_d = F/(6\pi\eta a)$ by Stokes' law, where $\eta$ is the fluid viscosity and $a$ is the particle radius. This gives a flux:

$$J_{drift} = n \cdot v_d = \frac{nF}{6\pi\eta a}$$

In equilibrium ($J_{total} = 0$), the two fluxes balance.

### III. The Einstein Relation

For the specific case of particles in a gravitational field, $F = -mg_{eff}$ (the effective weight accounting for buoyancy), and in equilibrium the concentration follows a barometric distribution:

$$n(z) = n_0 \exp\left(-\frac{m_{eff}gz}{k_BT}\right)$$

The osmotic flux is:

$$J_{osmotic} = -D\frac{\partial n}{\partial z} = D\frac{m_{eff}g}{k_BT}n$$

The gravitational drift flux is:

$$J_{grav} = -\frac{nm_{eff}g}{6\pi\eta a}$$

Setting $J_{osmotic} + J_{grav} = 0$:

$$D\frac{m_{eff}g}{k_BT}n = \frac{nm_{eff}g}{6\pi\eta a}$$

$$\boxed{D = \frac{k_BT}{6\pi\eta a}}$$

This is the **Stokes-Einstein relation** (or Einstein relation). It connects a macroscopic transport coefficient (the diffusion constant) to microscopic thermal physics ($k_BT$) and hydrodynamics ($\eta$, $a$).

Note that the gravitational field has canceled out -- the relation is universal. It applies to any suspended particle in any fluid, regardless of the force that established the equilibrium.

### IV. The Diffusion Equation

Einstein now derives the time-dependent behavior. Consider particles distributed along the $x$-axis with concentration $n(x,t)$. In a small time interval $\tau$, each particle undergoes a random displacement $\Delta$ whose probability distribution is symmetric: $\phi(\Delta) = \phi(-\Delta)$, with:

$$\int_{-\infty}^{\infty} \phi(\Delta)\,d\Delta = 1$$

The concentration at time $t + \tau$ is:

$$n(x, t+\tau) = \int_{-\infty}^{\infty} n(x - \Delta, t)\,\phi(\Delta)\,d\Delta$$

Expanding both sides in Taylor series (assuming $\tau$ and typical $\Delta$ are small):

**Left side:**
$$n(x, t+\tau) \approx n(x,t) + \tau\frac{\partial n}{\partial t}$$

**Right side:** Expanding $n(x - \Delta, t)$ around $\Delta = 0$:
$$n(x-\Delta,t) \approx n - \Delta\frac{\partial n}{\partial x} + \frac{\Delta^2}{2}\frac{\partial^2 n}{\partial x^2}$$

Integrating against $\phi(\Delta)$: the first term gives $n$, the second vanishes by symmetry, and the third gives:

$$\frac{1}{2}\frac{\partial^2 n}{\partial x^2}\int_{-\infty}^{\infty}\Delta^2\phi(\Delta)\,d\Delta = \frac{\langle\Delta^2\rangle}{2}\frac{\partial^2 n}{\partial x^2}$$

Equating:

$$\tau\frac{\partial n}{\partial t} = \frac{\langle\Delta^2\rangle}{2}\frac{\partial^2 n}{\partial x^2}$$

Defining $D = \langle\Delta^2\rangle/(2\tau)$:

$$\frac{\partial n}{\partial t} = D\frac{\partial^2 n}{\partial x^2}$$

This is the **diffusion equation** (Fick's second law).

### V. Mean-Squared Displacement

For $N$ particles all starting at $x = 0$ at $t = 0$, the solution of the diffusion equation is:

$$n(x,t) = \frac{N}{\sqrt{4\pi D t}}\exp\left(-\frac{x^2}{4Dt}\right)$$

The mean-squared displacement is:

$$\langle x^2 \rangle = \int_{-\infty}^{\infty} x^2 \frac{n(x,t)}{N}\,dx = 2Dt$$

In three dimensions:

$$\langle r^2 \rangle = 6Dt$$

Substituting the Einstein relation:

$$\langle x^2 \rangle = 2\left(\frac{k_BT}{6\pi\eta a}\right)t = \frac{k_BT}{3\pi\eta a}t$$

### VI. Determination of Avogadro's Number

The measurable quantities are: the mean-squared displacement $\langle x^2\rangle$ (observable under a microscope), the time $t$, the temperature $T$, the viscosity $\eta$ (known), and the particle radius $a$ (measurable). The only unknown is $k_B = R/N_A$. Therefore:

$$N_A = \frac{RT \cdot t}{3\pi\eta a \langle x^2\rangle}$$

Einstein provided a numerical estimate: for particles of radius $a = 0.001$ mm in water at $T = 17°$C ($\eta \approx 0.0135$ poise), the expected root-mean-square displacement in one second is:

$$\sqrt{\langle x^2\rangle} \approx 0.8\;\mu\text{m}$$

This was well within the range of microscopic observation.

---

## Physical Interpretation

### The Random Walk

Einstein's derivation amounts to the first rigorous theory of the random walk (though the term was coined by Karl Pearson in the same year, independently). The key insight is that the $\sqrt{t}$ scaling of displacement -- rather than the linear scaling one would expect for directed motion -- is a signature of stochastic dynamics.

A particle undergoing $N$ random steps of average length $\ell$ in random directions accumulates a net displacement that scales as $\ell\sqrt{N}$, not $\ell N$. This is because the cross-terms in $\langle(\sum \Delta_i)^2\rangle$ average to zero for independent steps.

### Fluctuation-Dissipation

The Einstein relation $D = k_BT/(6\pi\eta a)$ is a prototype of what would later be called the **fluctuation-dissipation theorem**: the diffusion constant (a measure of fluctuations) is proportional to $k_BT$ (thermal energy) divided by the friction coefficient $\zeta = 6\pi\eta a$ (a measure of dissipation). In general form:

$$D = \frac{k_BT}{\zeta}$$

This deep connection -- that the same molecular collisions cause both random motion (fluctuations) and viscous resistance (dissipation) -- was formalized by Nyquist (1928) for electrical noise, by Onsager (1931) for irreversible thermodynamics, and by Kubo (1966) in full generality.

### Proving Atoms Exist

The paper's most profound implication was existential: if Brownian motion has the quantitative properties Einstein predicted, then atoms must be real physical objects with definite sizes and masses. The prediction was fully confirmed by Jean Perrin's meticulous experiments (1908-1909), in which he measured $\langle x^2\rangle$ for colloidal gamboge particles and obtained $N_A \approx 6.8 \times 10^{23}$, consistent with independent determinations. Perrin received the 1926 Nobel Prize "for his work on the discontinuous structure of matter."

After Perrin's work, even Ostwald conceded the reality of atoms.

---

## Impact and Legacy

### Smoluchowski's Independent Derivation

Marian Smoluchowski independently developed a theory of Brownian motion (published 1906), arriving at the same $\sqrt{t}$ scaling but with a slightly different prefactor (off by a factor of $64/(27\pi)$ from Einstein's result). Smoluchowski used a more molecular approach, explicitly modeling individual collisions, while Einstein's thermodynamic method was more elegant and general.

### Langevin's Approach (1908)

Paul Langevin introduced a simpler and more intuitive derivation by writing the equation of motion for a single Brownian particle:

$$m\ddot{x} = -\zeta\dot{x} + F(t)$$

where $\zeta\dot{x}$ is the Stokes friction and $F(t)$ is a random force with $\langle F(t)\rangle = 0$ and $\langle F(t)F(t')\rangle = 2\zeta k_BT\,\delta(t - t')$. Multiplying by $x$ and averaging gives the same $\langle x^2\rangle = 2Dt$ result.

### Wiener Process and Mathematical Foundations

Norbert Wiener (1923) provided rigorous mathematical foundations for the Brownian motion process, showing that the paths are continuous but nowhere differentiable. The Wiener process became a cornerstone of probability theory and stochastic analysis. Ito calculus, stochastic differential equations, and the Black-Scholes model for financial derivatives all trace their mathematical lineage to Einstein's physical theory.

### Confirmation of Statistical Mechanics

The quantitative success of Einstein's theory decisively vindicated Boltzmann's statistical mechanics. The Second Law of thermodynamics was revealed to be statistical, not absolute -- Brownian motion involves visible fluctuations away from thermodynamic equilibrium. A particle's displacement occasionally violates the "expected" direction, exactly as Boltzmann had argued.

---

## Connections to Modern Physics

### Stochastic Thermodynamics

The modern field of stochastic thermodynamics extends Einstein's framework to systems far from equilibrium. The Jarzynski equality (1997):

$$\langle e^{-\beta W}\rangle = e^{-\beta \Delta F}$$

and the Crooks fluctuation theorem relate nonequilibrium work to equilibrium free-energy differences, generalizing the fluctuation-dissipation theorem to arbitrary driving protocols. These are direct descendants of Einstein's insight that thermal fluctuations have quantitative, testable consequences.

### Active Matter and Biophysics

In biological systems, molecular motors (kinesin, myosin) undergo biased Brownian motion, using chemical energy to produce directed transport. The Einstein relation provides the baseline: any directed motion beyond the $\sqrt{t}$ diffusive scaling requires energy input. The ratio of directed velocity to diffusion constant gives a measure of the motor's efficiency.

### Single-Molecule Experiments

Modern optical tweezers, atomic force microscopy, and fluorescence tracking allow observation of individual molecules undergoing Brownian motion. These experiments measure forces on the piconewton scale and displacements on the nanometer scale, in quantitative agreement with Einstein's theory.

### Analog Gravity and Phononic Systems

In condensed matter analogs of cosmological systems, the diffusion of defects (vortices, domain walls) in superfluids and Bose-Einstein condensates follows Einstein-type random walk dynamics at finite temperature. The mean-squared displacement of vortex positions provides a probe of the effective temperature and dissipation mechanisms in these systems, directly paralleling Einstein's original program of using macroscopic fluctuations to extract microscopic parameters.
