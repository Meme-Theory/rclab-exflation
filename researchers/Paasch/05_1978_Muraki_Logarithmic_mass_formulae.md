# Logarithmic Mass Formulae for Elementary Particles and a New Quantum Number

**Authors**: Muraki Y., Mori K., Nakagawa M.
**Year**: 1978
**Journal**: Lettere al Nuovo Cimento, vol. 23, no. 1, pp. 27-31
**DOI**: 10.1007/BF02762459
**Source**: https://link.springer.com/article/10.1007/BF02762459

---

## Abstract

The authors propose a logarithmic mass formula for elementary particles, introducing a new
quantum number that governs the mass spectrum. By plotting the logarithm of particle masses
against an integer-valued quantum number, they demonstrate that known hadrons and leptons fall
on approximately linear trajectories in log-mass space. The formula takes the form
$\ln(m/m_0) = a \cdot n + b$, where $n$ is an integer quantum number, and $a$, $b$ are
trajectory-dependent constants. The observed regularity suggests an underlying algebraic
structure governing the particle mass spectrum.

---

## Historical Context

By the late 1970s, the Standard Model of particle physics was rapidly consolidating. QCD had
been established, the electroweak theory unified, and the quark model was well-confirmed. Yet
the mass spectrum of elementary particles remained unexplained -- the SM contains Yukawa
couplings as free parameters, offering no prediction of WHY particles have the masses they do.

Against this backdrop, several groups attempted to find empirical regularities in the particle
mass spectrum. The earliest notable attempt was Nambu (1952), who proposed empirical mass
formulas. Muraki, Mori, and Nakagawa took a different approach: rather than fitting polynomial
mass relations, they examined logarithmic (i.e., multiplicative/geometric) patterns.

This paper is the DIRECT ANCESTOR of Paasch's framework. Paasch's 2009 Paper 02 explicitly
cites Muraki et al. and extends their logarithmic mass approach by:
1. Identifying the integer quantum number with a "mass number" on a spiral
2. Connecting the logarithmic spacing to a potential of the form $V(r) \propto \ln(r)$
3. Embedding the scheme in a cosmological context via the Large Numbers Hypothesis

The Muraki paper demonstrated that the idea of integer-labeled mass trajectories in log-space
is NOT original to Paasch -- it has a legitimate 1970s pedigree in mainstream particle physics.

---

## Key Arguments and Derivations

### The Logarithmic Mass Formula

The central observation is that when one plots $\ln(m)$ for known particles against a suitably
chosen integer quantum number $n$, the points cluster along approximately linear trajectories.
The mass formula is:

$$\ln(m_i / m_0) = a \cdot n_i + b$$

or equivalently:

$$m_i = m_0 \cdot e^{a \cdot n_i + b}$$

where:
- $m_i$ is the mass of particle $i$
- $m_0$ is a reference mass (typically the electron mass $m_e$ or pion mass $m_\pi$)
- $n_i$ is an integer quantum number assigned to particle $i$
- $a$ and $b$ are constants characterizing the mass trajectory

This is a GEOMETRIC (exponential) mass spectrum rather than an arithmetic one. The ratio of
successive masses on the same trajectory is constant: $m_{n+1}/m_n = e^a$.

### Assignment of Quantum Numbers

The key step is the assignment of integer quantum numbers to known particles. Muraki et al.
do this by:

1. Ordering known particle masses
2. Computing $\ln(m_i/m_e)$ for each particle
3. Looking for approximate integer spacings in these logarithmic values
4. Assigning integer $n$ values that minimize deviations from linearity

The remarkable finding is that the deviations from exact integer spacing are small --
typically a few percent or less for the best-fitting trajectories.

### Multiple Trajectories

Not all particles lie on a single trajectory. The authors identify MULTIPLE parallel
trajectories, distinguished by other quantum numbers (spin, isospin, strangeness). Each
trajectory has the same slope $a$ but different intercepts $b$. This means:

- The mass-generating mechanism has a UNIVERSAL exponential structure
- Different particle families share the same fundamental scale $e^a$
- The intercept $b$ encodes additional quantum numbers

### The New Quantum Number

The "new quantum number" of the title is essentially the integer $n$ itself -- a mass number
that counts the particle's position along its mass trajectory. This is not a standard SM
quantum number (charge, isospin, color, etc.) but an ADDITIONAL label that correlates with
mass.

The physical interpretation proposed is that $n$ labels excitation levels of some underlying
system -- analogous to principal quantum number labeling energy levels in atomic physics.
But unlike atomic physics, no dynamical equation (Schrodinger, Dirac) is provided to derive
these levels. The formula is purely empirical.

---

## Key Results

1. Known hadron and lepton masses cluster along approximately linear trajectories when
   plotted as $\ln(m)$ vs. integer $n$
2. Multiple parallel trajectories exist, sharing a common slope $a$
3. The universal slope suggests a common exponential scale for mass generation
4. Deviations from exact linearity are small (few percent) for the best-fitting assignments
5. The scheme works across both hadrons and leptons, suggesting a universal mass-generation
   mechanism
6. The integer quantum number $n$ has no standard model counterpart -- it is genuinely new
7. The exponential mass formula $m \propto e^{an}$ implies multiplicative (geometric) rather
   than additive mass quantization

---

## Impact and Legacy

The Muraki-Mori-Nakagawa paper established the logarithmic mass formula approach within the
particle physics community. While it did not achieve mainstream acceptance (the SM treats
masses as free parameters), it influenced several subsequent works:

- **Paasch (2009)**: Directly builds on Muraki's framework, extending it with a spiral
  structure and cosmological embedding via the Large Numbers Hypothesis
- **Mac Gregor (2007)**: Independently developed alpha-quantized mass formulas with related
  exponential structure
- **Zenczykowski (2015)**: Argued that mass-integer correlations "strongly suggest an
  algebraic origin of mass"

The paper's significance lies not in providing a dynamical explanation but in establishing
an EMPIRICAL PATTERN that demands explanation. If the pattern is real (not a statistical
artifact), then the Standard Model's treatment of masses as arbitrary Yukawa couplings
is incomplete.

---

## Relevance to Paasch Framework

This is the FOUNDATIONAL paper for Paasch's mass quantization scheme. Paasch's Paper 02
(2009) explicitly cites Muraki et al. and extends their work in three ways:

1. **Spiral structure**: Paasch arranges the integer mass numbers on a spiral (not just
   linear trajectories), connecting the angular structure to the golden ratio $\phi$
2. **Logarithmic potential**: Paasch interprets the logarithmic mass formula as arising from
   a potential $V(r) \propto \ln(r)$, giving a dynamical origin to the empirical pattern
3. **Cosmological connection**: Paasch links the mass scale to the Large Numbers Hypothesis
   via $G(t) \sim 1/t$, embedding particle masses in cosmological evolution

The key question is whether Paasch's extensions are justified generalizations of a real
pattern or over-interpretation of statistical coincidences.

---

## Relevance to Phonon-Exflation Project

The logarithmic/exponential mass structure found by Muraki is suggestive in the context of
the phonon-exflation framework because:

1. The Jensen TT-deformation of SU(3) has EXPONENTIAL scale factors ($e^{2s}$, $e^{-2s}$,
   $e^s$) -- precisely the kind of structure that could generate geometric mass ratios
2. The Tier 1 Dirac spectrum computation found phi_paasch ($\phi_P = 1.53158$) appearing at specific
   deformation parameters, suggesting that "special" algebraic numbers CAN emerge from the
   geometry
3. If $V_{\text{eff}}(s)$ selects a specific deformation parameter $s_0$, the eigenvalue
   ratios at that $s_0$ would predict specific mass ratios -- potentially explaining
   Muraki's empirical pattern from geometry
