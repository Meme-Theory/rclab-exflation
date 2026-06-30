# Higgs response and pair condensation energy in superfluid nuclei

**Author(s):** Kengo Takahashi, Yusuke Matsuda, Masayuki Matsuo
**Year:** 2023
**Journal:** Prog. Theor. Exp. Phys. 083D01 (2023)
**arXiv:** 2302.14214
**Relevance:** HIGH

---

## Abstract

The pairing correlation in nuclei causes a characteristic excitation, known as the pair vibration, which is populated by the pair transfer reactions. Here we introduce a new method of characterizing the pair vibration by employing an analogy to the Higgs mode, which emerges in infinite superconducting/superfluid systems as a collective vibrational mode associated with the amplitude oscillation of the Cooper pair condensate. The idea is formulated by defining a pair-transfer probe, the Higgs operator, and then describing the linear response and the strength function to this probe. We will show that the pair condensation energy in nuclei can be extracted with use of the strength sum and the static polarizability of the Higgs response. In order to demonstrate and validate the method, we perform for Sn isotopes numerical analysis based the quasi-particle random phase approximation to the Skyrme-Hartree-Fock-Bogoliubov model. We discuss a possibility to apply this new scheme to pair transfer experiment.

---

## Key Arguments and Derivations

### Higgs operator construction

The authors define pair-addition and pair-removal operators:

P_ad = (1/sqrt(4pi)) integral dr f(r) psi^dag(r,down) psi^dag(r,up)
P_rm = (1/sqrt(4pi)) integral dr f(r) psi(r,up) psi(r,down)

where f(r) is a Woods-Saxon form factor (R = 1.27 A^{1/3} fm, a = 0.67 fm). The Higgs operator is defined as their sum:

P_H = P_ad + P_rm

This probes the amplitude fluctuation of the pair condensate, since delta|rho_tilde(r)| ~ (delta_rho_tilde + delta_rho_tilde*)/2 for real rho_tilde.

### Key distinction: Higgs vs phase mode

The pair rotation (Nambu-Goldstone mode) has pair-addition and pair-removal amplitudes with opposite sign, so the Higgs matrix element vanishes: <nu|P_H|0> = <nu|P_ad|0> + <nu|P_rm|0> = 0. The low-lying pair vibration has same-sign amplitudes, giving coherent enhancement in the Higgs strength. This cleanly separates amplitude (Higgs) from phase (Goldstone) responses.

### Effective potential and condensation energy

The effective potential U(p) = E(p) - E(0) is computed via constrained HFB (CHFB) as a function of the order parameter p = <P_H>. The key finding is that U(p) is well approximated by a quartic polynomial (Ginzburg-Landau form):

U_4th(p) = a p^4 + b p^2 + c

This yields the condensation energy via:

U_cond^Higgs = -(1/8) p_0^2 / alpha_H

where p_0 = <Psi_0|P_H|Psi_0> is the ground state order parameter and alpha_H is the Higgs polarizability (inversely energy-weighted sum of the Higgs strength function).

### Higgs polarizability

The static polarizability relates to the inverse energy-weighted sum:

I_{-1} = 2 integral S_H(E)/E dE = alpha_H

And the curvature of the effective potential at the minimum:

C = d^2 U / dp^2 |_{p=p_0} = -4b = 1/alpha_H

### Numerical validation on Sn isotopes

Using SLy4 Skyrme functional with density-dependent delta interaction (DDDI) pairing (v_0 = -458.4 MeV fm^3), the method reproduces CHFB condensation energies within ~10%. For 120Sn: U_cond^Higgs = -1.51 MeV vs U_cond^CHFB = -1.58 MeV.

The low-lying pair vibration contributes ~35% of the inversely energy-weighted sum, while high-lying pair vibrations (up to ~20 MeV) contribute ~45% more. Both are essential for the total Higgs response.

---

## Key Results

1. The Higgs operator P_H = P_ad + P_rm cleanly separates amplitude (Higgs) from phase (Goldstone) pair excitation modes
2. The nuclear effective potential is well approximated by a quartic Ginzburg-Landau form U(p) = ap^4 + bp^2 + c
3. Pair condensation energy can be extracted from the Higgs polarizability: U_cond = -(1/8) p_0^2 / alpha_H
4. The method works to ~10% accuracy across Sn isotopes (A = 100 to 150)
5. Both low-lying and high-lying pair vibrations contribute comparably to the Higgs response
6. 140Sn has anomalously small condensation energy (~0.1 MeV) despite finite pairing gap, due to very large Higgs polarizability
7. The condensation energy carries information beyond what is contained in the pairing gap alone

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Pair condensate | $\tilde{\rho}(r) = \langle \Psi | \psi(r\uparrow)\psi(r\downarrow) | \Psi \rangle$ | Eq. (1) |
| HFB equation | $\begin{pmatrix} \hat{t}+\Gamma-\mu & \Delta \\ \Delta^* & -(\hat{t}+\Gamma-\mu) \end{pmatrix} \begin{pmatrix} \varphi_{1,i} \\ \varphi_{2,i} \end{pmatrix} = E_i \begin{pmatrix} \varphi_{1,i} \\ \varphi_{2,i} \end{pmatrix}$ | Eq. (4) |
| Higgs operator | $\hat{P}_H = \hat{P}_{\text{ad}} + \hat{P}_{\text{rm}} = \frac{1}{\sqrt{4\pi}} \int dr\, f(r)[\psi\psi + \psi^\dagger\psi^\dagger]$ | Eq. (23) |
| Higgs strength | $S_H(E) = \sum_\nu |\langle \nu | \hat{P}_H | 0 \rangle|^2 \delta(E - E_\nu)$ | Eq. (24) |
| Higgs polarizability | $\alpha_H = 2 \int \frac{S_H(E)}{E} dE$ | Eq. (26) |
| Order parameter | $p_0 = \langle \Psi_0 | \hat{P}_H | \Psi_0 \rangle$ | Eq. (33) |
| Curvature | $C = 1/\alpha_H$ | Eq. (34) |
| Condensation energy | $U_{\text{cond}}^{\text{Higgs}} = -\frac{1}{8} \frac{p_0^2}{\alpha_H}$ | Eq. (35) |
| Quartic potential | $U_{4\text{th}}(p) = a p^4 + b p^2 + c$ | Eq. (29) |
| Potential depth | $D = -b^2/(4a) = \frac{1}{8} C p_0^2$ | Eq. (32) |
| DDDI pairing | $V_q(r) = v_0[1 - \eta(\rho(r)/\rho_0)^\gamma]$ | Eq. (15) |
| Average gap | $\bar{\Delta} = \int dr\, \Delta(r) \rho(r) / \int dr\, \rho(r)$ | Text |

## Relevance to Phonon-Exflation

This paper provides the exact methodology needed to extract the pair condensation energy E_cond from the Higgs (amplitude) response of the K_7 BCS condensate on SU(3). The framework's E_cond = -0.115 (Session 35) was computed directly; the Higgs operator approach offers an independent route via the inversely-energy-weighted sum of the pair-transfer strength. The quartic Ginzburg-Landau structure of the effective potential validates the framework's use of a similar U(tau) potential, and the finding that both low-lying and high-lying pair vibrations contribute to alpha_H is directly relevant to the GPV fragmentation physics identified in Session 37-38.
