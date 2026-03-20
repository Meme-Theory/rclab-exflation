# Resilience of the Spectral Standard Model

**Authors:** Ali Chamseddine, Alain Connes
**Year:** 2012
**Journal:** Journal of High Energy Physics, 2012(9), 104
**arXiv:** 1208.1030
**Pages:** 23

---

## 1. The Higgs Mass Crisis

### 1.1 The Original NCG Prediction

The spectral action principle, applied to the noncommutative geometry of the
Standard Model, produced a specific prediction for the Higgs boson mass. The
calculation, first performed by Chamseddine and Connes in 1996 and refined in
2006-2007, gave:

```
m_H^2 = (8 * lambda) / (pi^2 * g^2) * m_W^2
```

where lambda is the quartic Higgs coupling at the unification scale Lambda,
determined by the spectral action. The boundary condition from NCG at the
unification scale Lambda ~ 10^{17} GeV was:

```
lambda(Lambda) = (g_2^4 * b) / (pi^2 * a^2)
```

where a and b are traces of Yukawa coupling matrices:

```
a = Tr(Y_nu^* Y_nu + Y_e^* Y_e + 3 Y_u^* Y_u + 3 Y_d^* Y_d)
b = Tr((Y_nu^* Y_nu)^2 + (Y_e^* Y_e)^2 + 3(Y_u^* Y_u)^2 + 3(Y_d^* Y_d)^2)
```

Running these down to the electroweak scale using the renormalization group
equations gave m_H approximately 170 GeV.

### 1.2 The LHC Discovery

On July 4, 2012, the ATLAS and CMS experiments at the LHC announced the
discovery of a scalar boson with mass:

```
m_H = 125.09 +/- 0.24 GeV
```

This was 45 GeV below the NCG prediction. The discrepancy was devastating:
it appeared to falsify the spectral Standard Model.

### 1.3 The Response

Chamseddine and Connes responded within weeks (arXiv submission: August 6,
2012). Their paper showed that the NCG framework contains a previously
neglected scalar field -- the sigma field -- whose inclusion corrects the
Higgs mass to be consistent with 125 GeV. The framework was not falsified;
it was INCOMPLETE.


---

## 2. The Sigma Field

### 2.1 Origin in the Dirac Operator

The finite Dirac operator D_F of the NCG Standard Model has the block
structure:

```
D_F = (  S         T^*  )
      (  T         S^*  )
```

where S and T are matrices acting on the particle Hilbert space. The matrix S
contains the Yukawa couplings, and T contains the Majorana mass terms for
right-handed neutrinos.

In the original treatment, the Majorana sector was simplified by setting the
Majorana mass M_R to a fixed value (the unification scale). This amounts to
treating the sigma field as a CONSTANT rather than a dynamical field.

### 2.2 The Dynamical Sigma Field

The key insight of the Resilience paper: the Majorana coupling in D_F
corresponds to a SCALAR FIELD sigma that should be treated dynamically, just
as the Higgs field H corresponds to the Yukawa coupling sector.

In the inner fluctuations of D, the Higgs field arises from:

```
A_H = sum_i a_i [D, b_i]  (acting on particle space)
```

The sigma field arises from the same mechanism but in the Majorana sector:

```
A_sigma = sum_i a_i [D, b_i]  (acting on the nu_R-nu_R^c sector)
```

Both H and sigma are GEOMETRIC -- they are inner fluctuations of the Dirac
operator. Setting sigma = constant was an unjustified truncation.

### 2.3 Quantum Numbers of Sigma

The sigma field is:
- A complex scalar (spin 0)
- Neutral under all SM gauge groups: SU(3) singlet, SU(2) singlet, Y = 0
- Carries lepton number L = 2 (from its coupling to nu_R nu_R)
- Has a large VEV: <sigma> ~ Lambda (the unification scale)

Its gauge quantum numbers are trivial, making it invisible to colliders
unless its mass is below the TeV scale.


---

## 3. The Modified Higgs Potential

### 3.1 The Two-Field Potential

With both H and sigma as dynamical fields, the spectral action produces a
two-field potential:

```
V(H, sigma) = lambda_H * |H|^4
            + lambda_sigma * |sigma|^4
            + lambda_{H sigma} * |H|^2 * |sigma|^2
            - mu_H^2 * |H|^2
            - mu_sigma^2 * |sigma|^2
```

The quartic couplings at the unification scale Lambda are determined by the
spectral action:

```
lambda_H(Lambda) = (pi^2 * b) / (2 * f_0 * a^2)

lambda_sigma(Lambda) = (pi^2 * d) / (2 * f_0 * c^2)

lambda_{H sigma}(Lambda) = (pi^2 * e) / (2 * f_0 * a * c)
```

where a, b, c, d, e are traces of various combinations of Yukawa and
Majorana coupling matrices, and f_0 is the zeroth moment of the cutoff
function f.

### 3.2 The Boundary Conditions

The spectral action determines ALL quartic couplings at the unification
scale in terms of the Yukawa and Majorana matrices. The key boundary
conditions are:

```
At Lambda ~ 10^{17} GeV:

lambda_H(Lambda) ~ g^2 * sum(y_i^4) / sum(y_i^2)^2
lambda_sigma(Lambda) ~ g^2 * sum(y_{M,i}^4) / sum(y_{M,i}^2)^2
lambda_{H sigma}(Lambda) ~ g^2 * sum(y_i^2 * y_{M,i}^2) / (sum(y_i^2) * sum(y_{M,i}^2))
```

where y_i are the SM Yukawa couplings and y_{M,i} are the Majorana Yukawa
couplings.

### 3.3 Running to Low Energies

The renormalization group equations for the two-field system couple lambda_H,
lambda_sigma, and lambda_{H sigma}. The key effect: the sigma-Higgs portal
coupling lambda_{H sigma} REDUCES the effective Higgs quartic at the
electroweak scale:

```
lambda_H^{eff}(m_Z) = lambda_H(m_Z) - lambda_{H sigma}^2(m_Z) / (4 * lambda_sigma(m_Z))
```

This tree-level shift from integrating out the heavy sigma field LOWERS the
Higgs mass prediction from ~170 GeV to a range consistent with 125 GeV.


---

## 4. The Corrected Higgs Mass

### 4.1 The Mass Formula

The physical Higgs mass in the two-field model is:

```
m_H^2 = 2 * lambda_H^{eff}(v) * v^2
```

where v = 246 GeV is the electroweak VEV. The effective quartic coupling
lambda_H^{eff} includes:

1. The tree-level NCG boundary condition at Lambda
2. RG running from Lambda to m_Z
3. The sigma portal correction (negative, lowering m_H)
4. Threshold corrections at the sigma mass scale

### 4.2 The Viable Parameter Space

Chamseddine and Connes show that for Majorana Yukawa couplings of order 1
and sigma VEV of order Lambda, the Higgs mass comes out in the range:

```
m_H in [120, 130] GeV
```

depending on the precise Majorana coupling values. The observed 125.09 GeV
sits comfortably in this range.

### 4.3 What is Predicted, What is Free

The model has the following structure:
- PREDICTED: the existence of sigma and the form of V(H, sigma)
- CONSTRAINED: the quartic couplings at Lambda (determined by spectral action)
- FREE: the Majorana Yukawa matrix entries (these are not determined by geometry)

The Higgs mass is not a sharp prediction but lies in a BAND determined by the
Majorana sector parameters.


---

## 5. The Seesaw Mechanism

### 5.1 Majorana Masses from Sigma

When sigma acquires its VEV <sigma> = v_sigma ~ Lambda, the Majorana mass
matrix for right-handed neutrinos becomes:

```
M_R = Y_M * v_sigma
```

where Y_M is the Majorana Yukawa matrix. For Y_M entries of order 1 and
v_sigma ~ 10^{13} GeV, the Majorana masses are:

```
M_R ~ 10^{13} GeV
```

### 5.2 Light Neutrino Masses

The type-I seesaw formula gives light neutrino masses:

```
m_nu = - Y_nu * v * (M_R)^{-1} * Y_nu^T * v
     = - Y_nu * v^2 * Y_M^{-1} / v_sigma * Y_nu^T
```

For Y_nu ~ Y_u (top-quark Yukawa ~ 1) and v_sigma ~ 10^{13} GeV:

```
m_nu ~ v^2 / v_sigma ~ (246)^2 / 10^{13} ~ 0.006 eV
```

This is in the correct range for atmospheric neutrino oscillations
(m_nu ~ 0.05 eV), with the precise values depending on the Yukawa textures.

### 5.3 The NCG Seesaw is Natural

In the NCG framework, the seesaw mechanism is not an optional addition -- it
is BUILT INTO the spectral triple. The finite Dirac operator D_F contains the
Majorana mass term as part of its structure. The sigma field is the dynamical
manifestation of this term. The seesaw is as natural in NCG as the Higgs
mechanism itself.


---

## 6. Sigma as a Dark Matter Candidate

### 6.1 Properties

After sigma acquires its VEV, the physical sigma particle (the excitation
around the VEV) has:

- Mass: m_sigma ~ v_sigma (or lower, depending on the potential)
- Couplings to SM: ONLY through the Higgs portal lambda_{H sigma} |H|^2 |sigma|^2
- Gauge interactions: NONE (it is a complete singlet)
- Stability: protected by a Z_2 symmetry sigma -> -sigma if the VEV is
  at a Z_2-symmetric point

### 6.2 Cosmological Viability

If m_sigma ~ TeV and the portal coupling is small, sigma could be:
- A WIMP dark matter candidate (thermal relic)
- A source of dark radiation (if light)
- A mediator for neutrino mass generation at loop level

Chamseddine and Connes note the possibility but do not pursue the
phenomenology in detail. Subsequent work (van den Broek, van Suijlekom 2012;
Devastato, Lizzi, Martinetti 2014) explores these scenarios.

### 6.3 Constraints

The Higgs invisible width measurement at the LHC constrains:

```
BR(H -> sigma sigma) < 0.19  (at 95% CL, current bound)
```

This requires either m_sigma > m_H/2 ~ 62.5 GeV or lambda_{H sigma} < 0.01.
Both are consistent with the NCG parameter space.


---

## 7. Vacuum Stability

### 7.1 The SM Stability Problem

In the pure Standard Model, the Higgs quartic coupling lambda_H runs to
negative values at high energies:

```
lambda_H(mu) < 0  for mu > 10^{10} GeV  (approximately)
```

This means the electroweak vacuum is metastable -- it could tunnel to a
lower-energy state. The metastability is a fine-tuning problem: we live in a
universe whose vacuum is not absolutely stable.

### 7.2 Sigma Stabilization

The sigma portal coupling lambda_{H sigma} contributes positively to the
beta function of lambda_H:

```
beta_{lambda_H} = beta_{lambda_H}^{SM} + (1/16*pi^2) * lambda_{H sigma}^2 + ...
```

This additional positive contribution can PREVENT lambda_H from going
negative, making the electroweak vacuum absolutely stable.

### 7.3 The Stability Window

Chamseddine and Connes show that for:

```
lambda_{H sigma}(Lambda) > 0.1 (approximately)
```

the electroweak vacuum is stable all the way to the unification scale. The
sigma field solves the vacuum stability problem as a BONUS of the NCG
construction.


---

## 8. Gravitational Sector

### 8.1 The Full Spectral Action

The spectral action Tr(f(D^2/Lambda^2)) for the product geometry
M^4 x F expands as:

```
S = integral d^4x sqrt(g) * [
    (48 * f_4 * Lambda^4) / pi^2
  - (c / pi^2) * f_2 * Lambda^2 * R
  + (11 * f_0) / (6 * pi^2) * R * R^*
  + (3 * f_0) / (10 * pi^2) * C_{mu nu rho sigma} * C^{mu nu rho sigma}
  + ... (gauge + Higgs + sigma terms)
]
```

where f_0, f_2, f_4 are moments of the cutoff function, R is the scalar
curvature, R* R* is the Gauss-Bonnet term, and C is the Weyl tensor.

### 8.2 Conformal Gravity at the Cutoff

At the unification scale, the gravitational action is dominated by the Weyl
tensor squared term -- this is CONFORMAL gravity, not Einstein gravity. The
transition to Einstein gravity at low energies occurs through the VEV of
the Higgs and sigma fields, which generate the Einstein-Hilbert term:

```
S_EH = integral d^4x sqrt(g) * (1/16*pi*G) * R
```

with Newton's constant determined by:

```
1 / (16*pi*G) = (f_2 * Lambda^2) / (pi^2) * (a + c)
```

where a involves Yukawa couplings and c involves Majorana couplings. The
sigma field contributes to Newton's constant through c.

### 8.3 The Cosmological Constant

The cosmological constant in the spectral action is:

```
Lambda_cosmo = (48 * f_4 * Lambda^4) / (pi^2)
```

This is of order Lambda^4 ~ (10^{17} GeV)^4, which is 120 orders of magnitude
too large. This is the standard cosmological constant problem. The NCG
framework does not resolve it but makes it EXPLICIT: the cosmological constant
is the leading term in the spectral action expansion.


---

## 9. Connection to Phonon-Exflation

### 9.1 The Sigma Field in the Jensen Framework

In the phonon-exflation framework, the internal space is SU(3) with a
Jensen TT-deformation parameterized by s. The Chamseddine-Connes sigma field
may correspond to a specific mode of this deformation.

The Dirac operator on the deformed SU(3) is D_K(s), where s controls the
shape of the internal space (at fixed volume, since the Jensen deformation is
volume-preserving). A scalar fluctuation of s around the equilibrium value s_0
would produce a massive neutral scalar -- the NCG sigma field.

### 9.2 V_eff and the Higgs-Sigma Potential

The project's computation of V_eff(s) = Tr f(D_s^2/Lambda^2) is DIRECTLY
related to the Higgs-sigma potential. In the phonon-exflation picture:

```
V_eff(s) = V(H = 0, sigma(s))
```

The Higgs VEV is an inner fluctuation (gauge direction), while s is the
modulus (geometric direction). The full two-field potential V(H, sigma)
emerges from computing the spectral action with both fluctuations active.

### 9.3 Resilience as Methodological Lesson

The Resilience paper demonstrates a crucial property of the NCG framework:
it is ROBUST under experimental challenges. The 125 GeV Higgs did not
falsify NCG -- it revealed a previously overlooked degree of freedom. This
"resilience" is characteristic of frameworks with deep structural constraints:
they bend rather than break.

For phonon-exflation, this suggests that if specific predictions (e.g., mass
ratios from the Dirac spectrum at s_0) disagree with experiment by factors of
O(1), the framework should be examined for overlooked modes or corrections
before being abandoned.

### 9.4 The Coleman-Weinberg Connection

The project's Session 17a computed the Coleman-Weinberg effective potential
for the spectral action (deliverable H-1). The 1-loop correction stabilizes
the potential at s_0 ~ 0.3-0.6. This is the phonon-exflation analog of the
Chamseddine-Connes sigma stabilization: quantum corrections select the
equilibrium shape of the internal space.

### 9.5 Testable Consequences

If the sigma field IS a Jensen deformation mode, then:

1. Its mass is determined by V_eff''(s_0) -- computable from the Dirac spectrum
2. Its coupling to the Higgs is lambda_{H sigma} = d^2 V / (dH^2 ds^2) at
   the equilibrium point -- also computable
3. The seesaw scale v_sigma ~ s_0 * Lambda_KK -- determined by the geometry
4. Light neutrino masses follow from the seesaw formula

All of these are in principle CALCULABLE from the Dirac spectrum on
Jensen-deformed SU(3), making the Resilience paper's sigma field a concrete
prediction target.


---

## 10. Impact and Reception

### 10.1 Resolution of the Crisis

The Resilience paper saved the NCG approach to the Standard Model from what
appeared to be a fatal blow. The sigma field was not an ad hoc fix -- it was
already present in the mathematical structure but had been overlooked.

### 10.2 New Predictions

The paper opened new directions:
- Sigma phenomenology at the LHC (Higgs portal searches)
- Vacuum stability from sigma coupling
- Connection between neutrino masses and Higgs physics through the seesaw
- Dark matter from the NCG spectral triple

### 10.3 Criticism

Critics note that the Majorana Yukawa matrix Y_M introduces new free
parameters, weakening the predictivity of the framework. The Higgs mass is
no longer a sharp prediction but lies in a band. However, the EXISTENCE of
sigma and the FORM of the potential are predicted -- only the parameters
are free.


---

## References

1. Chamseddine, A.H. and Connes, A. (2012). "Resilience of the Spectral
   Standard Model." JHEP 1209:104. arXiv: 1208.1030.
2. Chamseddine, A.H. and Connes, A. (1997). "The Spectral Action Principle."
   Commun. Math. Phys. 186, 731-750. arXiv: hep-th/9606001.
3. Chamseddine, A.H., Connes, A., and Marcolli, M. (2007). "Gravity and the
   Standard Model with Neutrino Mixing." Adv. Theor. Math. Phys. 11, 991-1089.
   arXiv: hep-th/0610241.
4. ATLAS Collaboration (2012). "Observation of a new particle in the search
   for the Standard Model Higgs boson." Phys. Lett. B 716, 1-29.
5. CMS Collaboration (2012). "Observation of a new boson at a mass of 125 GeV."
   Phys. Lett. B 716, 30-61.
6. van den Broek, T. and van Suijlekom, W.D. (2012). ""; Devastato, A.,
   Lizzi, F., and Martinetti, P. (2014). "Higgs mass in NCG."
7. Degner, A. (2006). "The Standard Model of Particle Physics in
   Non-Commutative Geometry." Diploma thesis.
