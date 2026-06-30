# First law of de Sitter thermodynamics

**Author(s):** G.E. Volovik
**Year:** 2025
**Journal:** [INCOMPLETE - preprint as of April 2025]
**arXiv:** 2504.05763
**Relevance:** HIGH

---

## Abstract

The de Sitter state has a special symmetry: it is homogeneous, and its curvature is constant in space. Since all the points in the de Sitter space are equivalent, this state is described by local thermodynamics. This state has the local temperature T = H/pi (which is twice the Gibbons-Hawking temperature), the local entropy density, the local energy density, and also the local gravitational degrees of freedom -- the scalar curvature R and the effective gravitational coupling K. On the other hand, there is the cosmological horizon, which can be also characterized by the thermodynamic relations. We consider the connections between the local thermodynamics and the thermodynamics of the cosmological horizon. In particular, there is the holographic connection between the entropy density integrated over the Hubble volume and the Gibbons-Hawking entropy of the horizon, S_volume = S_horizon = A/4G. We also consider the first law of thermodynamics in these two approaches. In the local thermodynamics, on the one hand, the first law is valid for an arbitrary volume V of de Sitter space. On the other hand, the first law is also applicable to the thermodynamics of the horizon. In both cases, the temperature is the same. This consideration is extended to the contracting de Sitter with its negative entropy, S_volume = S_horizon = -A/4G.

---

## Key Arguments and Derivations

### II. de Sitter Local Temperature and Local Entropy

Using Painleve-Gullstrand coordinates: ds^2 = -dt^2 + (dr - Hr dt)^2 + r^2 d Omega^2

The local temperature of de Sitter is T = H/pi (TWICE the Gibbons-Hawking temperature T_GH = H/2pi). This local temperature determines the entropy density:

s_dS = (3H^2)/(4piG) * 1/(H/pi) = 3H/(4G)

The entropy of the Hubble volume V_H = (4pi/3) r_H^3 with r_H = 1/H:

S_Hubble = V_H s_dS = A/(4G)

This exactly equals the Gibbons-Hawking horizon entropy, demonstrating holographic bulk-surface correspondence.

### III. Thermodynamics Modified by Gravity

The conventional Gibbs-Duhem law is modified by gravitational degrees of freedom:

T s = epsilon + p + KR

where K = 1/(16pi G) and R is the scalar curvature. Defining the modified pressure P = p + KR:

T s = epsilon + P (conventional form)

The first law: T dS = dE + P dV

For de Sitter in Einstein gravity: P = p_vac + KR = -p_vac = epsilon_vac = 3H^2/(8pi G). The equation of state in modified pressure is P = w epsilon_vac with w = 1 (Zeldovich stiff matter, c_s = c).

### IV. f(R) Gravity Extension

In f(R) gravity with action W = integral d^4x sqrt(-g) f(R), the conjugate variable K = df/dR. The equilibrium curvature satisfies 2f(R) = R df/dR, and the effective Newton constant G = 1/(16pi K). The cosmological "constant" emerges from the equilibrium value of f(R): epsilon_vac(H) = f(R = 12H^2).

### V. First Law for Cosmological Horizon

The first law T dS_H = dE_H + P dV_H is verified:

T dS_H = (H/pi) d(pi/(H^2 G)) = -2 dH/(GH^2)
dE_H = d(1/(2GH)) = -(1/2) dH/(GH^2)
P dV_H = (3H^2/(8pi G)) d(4pi/(3H^3)) = -(3/2) dH/(GH^2)

Sum: -(1/2) - (3/2) = -2, confirming the first law. The Hubble volume energy is E_H = 1/(2GH).

### VI. Negative Entropy of Contracting de Sitter

For H < 0 (contraction), the temperature is negative T = H/pi < 0, and the entropy is negative: S_H = -A/(4G). The cosmological horizon of contracting de Sitter has white-hole properties. Negative entropy is consistent with the white-hole-to-black-hole tunneling rate.

For gravastars (black holes with de Sitter interior, H < 0): the positive Bekenstein-Hawking entropy of the horizon cancels the negative interior entropy: S_gravastar = -A/(4G) + A/(4G) = 0. Zero entropy correlates with absence of Hawking radiation.

---

## Key Results

1. The de Sitter local temperature is T = H/pi = 2 T_GH (twice Gibbons-Hawking)
2. Holographic correspondence: S_volume = S_horizon = A/(4G) from local entropy density
3. The first law works for both arbitrary volume and the cosmological horizon
4. Gravitational degrees of freedom enter as (K, R) conjugate pair in modified thermodynamics
5. The equation of state in modified pressure is Zeldovich stiff matter (w = 1)
6. Contracting de Sitter has negative entropy S = -A/(4G) and negative temperature
7. Gravastar entropy is exactly zero (negative interior + positive horizon)
8. The first law extends to f(R) gravity via K = df/dR

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| PG metric | $ds^2 = -dt^2 + (dr - Hr\,dt)^2 + r^2 d\Omega^2$ | Eq.(2) |
| Local temperature | $T = H/\pi = 2T_{\text{GH}}$ | Sec.II |
| Entropy density | $s_{\text{dS}} = \frac{3H}{4G}$ | Eq.(5) |
| Holographic relation | $S_{\text{Hubble}} = V_H s_{\text{dS}} = \frac{A}{4G}$ | Eq.(6) |
| Modified Gibbs-Duhem | $Ts = \varepsilon + p + KR$ | Eq.(8) |
| Modified pressure | $P = p_{\text{vac}} + KR = \varepsilon_{\text{vac}} = \frac{3H^2}{8\pi G}$ | Eq.(11) |
| EOS (modified) | $P = w\varepsilon_{\text{vac}},\quad w = 1$ | Eq.(12) |
| f(R) equilibrium | $2f(R) = R\frac{df}{dR}$ | Eq.(15) |
| First law (horizon) | $T\,dS_H = dE_H + P\,dV_H$ | Eq.(17) |
| Hubble energy | $E_H = \frac{1}{2GH}$ | Eq.(22) |
| Negative entropy | $S_{\text{contracting}} = -\frac{A}{4G}$ | Sec.VI |
| Gravastar | $S_{\text{gravastar}} = -\frac{A}{4G} + \frac{A}{4G} = 0$ | Eq.(28) |

---

## Relevance to Phonon-Exflation

1. **Modified thermodynamics with (K, R) pair**: The gravitational degrees of freedom (K, R) as conjugate thermodynamic variables extend the vacuum thermodynamics of earlier papers. In the framework, the SU(3) fiber curvature plays the role of R, and the effective gravitational coupling K is determined by the spectral action. The modified pressure P = p + KR is the gravitational version of the framework's vacuum pressure.

2. **T = 2 T_GH**: The local temperature being twice the horizon temperature has implications for the framework's de Sitter phase. If the framework produces a de Sitter vacuum, the local thermal effects (particle production, spontaneous processes) are governed by T = H/pi, not H/(2pi).

3. **Negative entropy for contraction**: The contracting de Sitter with negative entropy connects to the framework's time-reversal considerations. The framework's BDI class (T^2 = +1) involves time reversal, and the entropy sign flip under H -> -H reflects the same symmetry.

4. **f(R) extension**: The result that the first law extends to any f(R) gravity validates the framework's use of general spectral action functionals (not just the Einstein-Hilbert action). The framework's spectral action f(D_K) is a specific instance of f(R) gravity.

5. **Zeldovich stiff matter EOS**: The w = 1 equation of state for the modified pressure in de Sitter is precisely the Zeldovich stiff matter that Volovik identifies with dark matter in later work (2410.04392). The framework's dark matter channel may connect to this.
