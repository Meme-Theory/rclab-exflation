# Analog Sommerfeld law in quantum vacuum

**Author(s):** G.E. Volovik
**Year:** 2023
**Journal:** JETP Letters
**arXiv:** 2307.00860
**Relevance:** MEDIUM

---

## Abstract

The activation temperature $T$ in the de Sitter environment is twice larger than the Gibbons-Hawking temperature, related to the cosmological horizon. We consider the activation temperature as the local temperature of the de Sitter vacuum, and construct the local thermodynamics of the de Sitter state. This thermodynamics includes also the gravitational coupling $K$ and the scalar Riemann curvature $\mathcal{R}$ as the thermodynamically conjugate variables. These variables modify the thermodynamics of the Gibbs-Duhem relation in the de Sitter state. The free energy density is proportional to $-T^2$, which is similar to that in the non-relativistic Fermi liquids and in relativistic matter with equation of state $w = 1$. The local entropy is proportional to the local temperature, while the total entropy inside the cosmological horizon is $A/4G$, where $A$ is the area of the horizon. This entropy is usually interpreted as the entropy of the cosmological horizon. We also consider the possible application of the de Sitter thermodynamics to the Schwarzschild-de Sitter black hole and to black and white holes with the de Sitter cores.

---

## Key Arguments and Derivations

### II. Thermodynamics of the de Sitter state

#### A. Local temperature and local entropy
The de Sitter vacuum has a local temperature $T = H/\pi$, which is twice the Gibbons-Hawking temperature $T_{\text{GH}} = H/2\pi$. The vacuum energy density expressed in terms of this temperature is $\epsilon_{\text{vac}} = \Lambda = (3\pi/8G)T^2$. The entropy density follows as $s_{\text{vac}} = (3\pi/4G)T = (3/4G)H$.

#### B. Modified Gibbs-Duhem relation
The conventional vacuum pressure $P_{\text{vac}} = -\epsilon_{\text{vac}}$ does not satisfy $Ts = \epsilon + P$ because the gravitational degrees of freedom are missing. Gravity contributes through the conjugate pair $(K, \mathcal{R})$ where $K = 1/(16\pi G)$ and $\mathcal{R} = -12H^2$. The modified Gibbs-Duhem relation is: $Ts_{\text{vac}} = \epsilon_{\text{vac}} + P_{\text{vac}} - K\mathcal{R}$.

Defining effective pressure $P = P_{\text{vac}} - K\mathcal{R}$, the de Sitter state satisfies $P = \epsilon_{\text{vac}} > 0$ with equation of state $w = 1$ (Zel'dovich stiff matter).

#### C-E. Entropy of horizons
The total entropy inside the cosmological horizon reproduces the Gibbons-Hawking result: $s_{\text{vac}}V_H = A/(4G)$. The same modified Gibbs-Duhem relation applied to Schwarzschild black holes gives $T_{\text{BH}}S_{\text{BH}} = M/2$. For Schwarzschild-de Sitter in the Nariai limit, the cosmological horizon entropy is recovered as $S_c = A/(4G)$.

#### F. Sommerfeld law
The vacuum entropy density $s_{\text{vac}} \sim T/l_P^2 \sim (T/E_P)/l_P^3$ suggests the density of "atoms of the vacuum" is $n_P \sim 1/l_P^3$, with entropy per atom $S \sim T/E_P$. This is the Sommerfeld law for Fermi liquids. The density of states $N_P \sim E_P^2$ leads to enormous entropy even at very small vacuum temperature.

#### G. Expansion vs Planckian dissipation
The energy relaxation time of matter in de Sitter environment is $1/\tau_E = H = \pi T$. This resembles Planckian dissipation but relates matter relaxation to vacuum temperature, not matter temperature.

### III. Gravastars and white holes
The de Sitter thermodynamics with negative temperature (contracting interior) cancels black hole entropy: $S_{\text{gravastar}} = sV_h + S_{\text{BH}} = -A/(4G) + A/(4G) = 0$. Similarly for antigravastars (white holes with expanding interior).

---

## Key Results

1. The local activation temperature of de Sitter vacuum is $T = H/\pi = 2T_{\text{GH}}$, twice the Gibbons-Hawking temperature
2. The modified Gibbs-Duhem relation requires gravitational conjugate variables $(K, \mathcal{R})$
3. The de Sitter vacuum thermodynamically behaves as Zel'dovich stiff matter ($w = 1$) and Fermi liquid ($\epsilon \propto T^2$)
4. Total entropy inside the cosmological horizon equals $A/(4G)$ from local entropy (bulk-boundary correspondence)
5. The analog Sommerfeld law gives entropy per vacuum "atom" as $S \sim T/E_P$
6. Gravastars with de Sitter cores have zero total entropy (interior cancels horizon)

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Local temperature | $T = H/\pi = 2T_{\text{GH}}$ | Sec. I |
| Vacuum energy | $\epsilon_{\text{vac}} = \Lambda = \frac{3\pi}{8G}T^2$ | Eq. (2) |
| Entropy density | $s_{\text{vac}} = \frac{3\pi}{4G}T = \frac{3}{4G}H$ | Eq. (3) |
| Modified Gibbs-Duhem | $Ts_{\text{vac}} = \epsilon_{\text{vac}} + P_{\text{vac}} - K\mathcal{R}$ | Eq. (5) |
| Effective pressure | $P = P_{\text{vac}} - K\mathcal{R}$ | Eq. (6) |
| Horizon entropy | $s_{\text{vac}}V_H = A/(4G)$ | Eq. (8) |
| BH Gibbs-Duhem | $T_{\text{BH}}S_{\text{BH}} = M/2$ | Eq. (10) |
| Sommerfeld law | $S = s_{\text{vac}}l_P^3 \sim T/E_P$ | Eq. (16) |
| Relaxation time | $1/\tau_E = H = \pi T$ | Eq. (19) |
| Gravastar entropy | $S_{\text{gravastar}} = -A/(4G) + A/(4G) = 0$ | Eq. (23) |

---

## Relevance to Phonon-Exflation

1. **Two-temperature framework**: The distinction between vacuum temperature $T = H/\pi$ and matter temperature $T_M$ is directly relevant to the framework's post-transit GGE state, which has its own effective temperature distinct from the CMB.

2. **Sommerfeld law as Fermi liquid analogy**: The $\epsilon \propto T^2$ behavior of the de Sitter vacuum mirrors the Fermi liquid thermodynamics that the framework exploits on the internal $SU(3)$ fiber.

3. **Gravitational conjugate variables $(K, \mathcal{R})$**: These modify the Gibbs-Duhem relation in exactly the way the framework's spectral action treatment handles the interplay between geometric and matter degrees of freedom.

4. **Planckian dissipation connection**: The relaxation time $\tau_E = 1/(\pi T)$ bridges condensed matter transport (strange metals) and cosmological expansion, relevant to the framework's transit dynamics.
