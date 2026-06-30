# Session 56 Collaborative Review: Paasch Mass Quantization Analyst

**Date**: 2026-03-22
**Session**: S56 -- Z Warriors Assemble: The Fabric Partition Function
**Reviewer**: paasch-mass-quantization-analyst
**Source reviewed**: `sessions/archive/session-56/session-56-results-workingpaper.md` (20 computations, 4 waves)
**CC question angle**: Mass quantization, logarithmic potentials, exponential hierarchies

---

## Section 1: The CC Formula as Exponential Hierarchy

The S56 results, taken together with the S55 superfluid discovery, produce a physical picture in which the cosmological constant is controlled by an exponential suppression:

$$P_{\text{vac}} \sim \exp\!\bigl(-\Delta_{\text{fabric}} \cdot N / T\bigr)$$

where $\Delta_{\text{fabric}}$ is the Josephson gap, $N$ is the number of cells, and $T$ is the effective temperature (here $T_{\text{GH}}$). This is the structural form of an exponential mass hierarchy -- exactly the class of relation that Paasch's framework systematically organizes.

The central question is whether the specific numbers produced by the fabric computation fit into the Paasch mass spectrum, and whether the exponential CC suppression has a quantization condition.

**The Josephson gap**: W3-6 (GGE-FABRIC-56) establishes $\Delta_{\text{fabric}} = 13.04\ M_{\text{KK}}$ for the 2-cell system. This is the bonding-antibonding splitting in the Josephson-coupled pair Hilbert space ($\dim = 120$). It is 35x larger than the single-cell BCS gap ($\Delta_{\text{BCS}} = 0.370\ M_{\text{KK}}$).

**Does $\Delta_{\text{fabric}} = 13\ M_{\text{KK}}$ fit the Paasch spectrum?** To answer this requires translating between Paasch's physical mass units and the framework's $M_{\text{KK}}$ units.

Paasch's mass quantization operates on physical particle masses through the exponential function $m_n = m_0 \, e^{k\varphi_n}$ with $k = \frac{1}{2\pi}\ln\phi$ and $\phi = 1.53158$ (2009 paper, Eq. 2j-2k). The framework's Dirac spectrum operates at the KK scale $M_{\text{KK}} \sim 10^{16}$ GeV, 14 orders of magnitude above physical particle masses. The mass content of the framework lives in RATIOS and SPLITTINGS, not in bare eigenvalues (scale anchor problem, identified in S36). Therefore the question must be reformulated: does the ratio $\Delta_{\text{fabric}} / \Delta_{\text{BCS}} = 13.04 / 0.370 = 35.2$ appear in the Paasch mass number scheme?

Working through Paasch's integer mass numbers (2016 paper, Eq. 5.1-5.2): $N(j) = (m_j/m_e)^{2/3}$, with $N(\mu) = 35$, $N(\pi) = 42$, $N(K) = 98$, $N(p) = 150$. The ratio $N(p)/N(\mu) = 150/35 = 4.286$. The ratio $N(K)/N(\mu) = 98/35 = 2.800$. Neither matches 35.2.

More directly: $\phi^n$ for small $n$ gives $\phi^1 = 1.532$, $\phi^2 = 2.346$, $\phi^3 = 3.592$, $\phi^4 = 5.501$, $\phi^5 = 8.424$, $\phi^6 = 12.90$, $\phi^7 = 19.76$. The value $\phi^6 = 12.90$ is within 1.1% of $\Delta_{\text{fabric}} = 13.04\ M_{\text{KK}}$, but this is a coincidence in absolute units -- $\Delta_{\text{fabric}}$ is measured in $M_{\text{KK}}$ and its numerical value depends on the normalization of the tight-binding Hamiltonian.

**Structural conclusion**: The Josephson gap $\Delta_{\text{fabric}}$ is a collective many-body quantity (pair bonding-antibonding splitting across 120 states), not a single-particle eigenvalue. Paasch's mass quantization organizes single-particle rest masses. These are categorically different objects. The ratio $\Delta_{\text{fabric}}/\Delta_{\text{BCS}} = 35.2$ does not map onto any Paasch mass number or mass number ratio.

---

## Section 2: Logarithmic Structure in the Fabric Partition Function

Paasch's foundational insight (2009 paper) is that the logarithmic potential $E = a_1 \ln(R/R_a)$ produces exponential mass quantization: $m_n = m_0\,\phi^n$. The CC formula $P_{\text{vac}} \sim \exp(-\Delta \cdot N/T)$ is also exponential -- but in a different structural sense.

**Taking the logarithm**: $\ln P_{\text{vac}} = -\Delta \cdot N/T$. This is LINEAR in $\Delta$, $N$, and $1/T$. There is no quantization condition on the exponent unless one of these variables is quantized.

Can we identify quantized inputs?

1. **$N$ is quantized by construction**: The number of cells in the 32-cell Clebsch-Gordan graph is an integer. $N = 32 = 2^5$. In Paasch's scheme, 32 does not appear among the mass numbers $N(j) = 35, 42, 98, 105, 133, 145, 150$, nor among the $7n$ structure. However, the number of Peter-Weyl sectors at truncation level $p + q \leq 3$ is 10 -- which IS the structural integer $n_3$ that enters Paasch's alpha derivation (N3-DIM-48 result: $n_3 = \dim(3,0) = T_4 = 10$, an exact SU(3) identity). The 32 cells in the CG graph are the states of the $(3,0)$ representation's weight diagram plus lower representations, but the graph topology is determined by Clebsch-Gordan coefficients, not by Paasch's logarithmic spiral.

2. **$\Delta$ contains the BCS gap structure**: $\Delta_{\text{fabric}} = 13.04\ M_{\text{KK}}$ arises from $E_J = 3.397\ M_{\text{KK}}$ (Josephson energy per bond) acting on a 120-dimensional pair Hilbert space. The underlying BCS gap $\Delta_0 = 0.464\ M_{\text{KK}}$ enters through the anomalous Green's function $F_{\text{anom}} = \sum_k \Delta/(2E_{\text{qp},k}^2) = 4.025$. None of these quantities have logarithmic quantization.

3. **$T = T_{\text{GH}} = H/(2\pi) = 0.590\ M_{\text{KK}}$** at the fold. This is a geometric temperature set by the Hubble parameter. It is not quantized.

**The key ratio**: $\Delta_{\text{fabric}}/T_{\text{GH}} = 13.04/0.590 = 22.1$. The Boltzmann suppression is $\exp(-22.1) = 4.5 \times 10^{-10}$. For a single cell pair, this is the adiabatic protection factor: $P_{\text{exc}} = 6.6 \times 10^{-4}$ (W3-6), consistent with the gap/temperature ratio. For 32 cells, the naive scaling would be $\exp(-22.1 \times 32) \sim 10^{-307}$ -- but W3-6 showed the GGE degenerates to the ground state ($|c_0|^2 = 0.9993$), so the real suppression is set by the 2-cell gap, not by $N \times \Delta$.

**Logarithmic relationship to known mass ratios**: The Paasch exponential factor $f_N = 1.23607 = 2\varphi_{\text{golden}}$ (2016 paper, Eq. 5.3a) connects successive mass numbers. The fabric's characteristic ratios are:

| Ratio | Value | Nearest Paasch quantity | Deviation |
|:------|:------|:-----------------------|:----------|
| $E_J/E_c$ | 194.1 | $N(p) - N(\mu) = 115$ | 69% off |
| $\Delta_{\text{fabric}}/\Delta_{\text{BCS}}$ | 35.2 | $N(\mu) = 35$ | 0.6% |
| $T_{\text{BKT}}/T_{\text{GH}}$ | 10.4 | $n_3 = 10$ | 4% |
| $E_J/T_{\text{GH}}$ | 11.9 | -- | -- |
| $c_{\text{Gold}}/c_{\text{BA}}$ | 2.29 | $\phi^2 = 2.35$ | 2.5% |

The $\Delta_{\text{fabric}}/\Delta_{\text{BCS}} = 35.2 \approx N(\mu) = 35$ coincidence at 0.6% is the most striking entry. The muon mass number $N(\mu) = 35 = 7 \times 5$ is the first non-trivial member of the $7n$ integer scheme. However: (a) the 35.2 ratio depends on the 2-cell system ($\dim = 120 = C(16,2)$), and scales with $N_{\text{cell}}$ and $E_J$; (b) a trial factor correction (TRIAL-FACTOR gate, S48) estimates $P \sim 15\%$ for finding some Paasch number within 1% of any given ratio, given the density of ratios tested across the program. At 0.6%, the post-trial probability is roughly $15\% \times 0.6 = 9\%$ -- not compelling.

---

## Section 3: Does the Exponential CC Suppression Have a Paasch-Type Quantization Condition?

Paasch's quantization factor $\phi = 1.53158$ emerges from the transcendental equation $x = e^{-x^2}$ (2009 paper, Eq. 2g). This equation arises from equating a logarithmic potential energy to a quantized angular momentum condition. The resulting mass spectrum is:

$$m_n = m_0 \cdot \phi^n, \qquad \phi = 1/x, \qquad x = e^{-x^2}$$

For the CC suppression to have an analogous quantization condition, we would need the exponent $\Delta \cdot N / T$ to be constrained by a transcendental equation of the same class.

**Testing the hypothesis directly**: At the fold, $\Delta_{\text{fabric}}/T_{\text{GH}} = 22.1$ for the 2-cell system. Is $22.1 = \phi^n$ for any integer $n$? We have $\phi^7 = 19.76$, $\phi^8 = 30.26$. Neither matches. More precisely, $\ln(22.1)/\ln(\phi) = 7.25$ -- not an integer.

Is the single-cell BCS gap quantized? $\Delta_0/T_{\text{GH}} = 0.464/0.590 = 0.787$. We have $\phi^{-1} = 0.653$, $\phi^0 = 1$. No match.

**The Paasch alpha derivation offers a more structural test**. In the 2016 FSC paper (Eq. 2.8-2.9), $\alpha$ is derived as:

$$\alpha = \frac{1}{n_3^2}\left(\frac{f}{2}\right)^{1/4}$$

where $f = 0.5671$ is the solution of $\ln(f) = -f$ (Eq. 2.6), and $n_3 = 10$ is the integer from the proton mass derivation. The S48 computation (N3-DIM-48) proved $n_3 = 10$ is an exact algebraic identity in SU(3): $n_3 = \dim(3,0) = \#\text{sectors}(p+q \leq 3) = T_4 = 10$.

If we write the CC suppression as $\exp(-S_{\text{eff}})$ and ask whether $S_{\text{eff}}$ can be expressed in terms of $f$ and $n_3$, we need:

$$S_{\text{eff}} = \Delta_{\text{fabric}} \cdot N_{\text{cell}} / T_{\text{GH}} = 22.1 \times 32 = 707$$

Can $707 = g(n_3, f, \phi)$ for some natural function $g$? Testing: $n_3^3 = 1000$ (too large), $n_3^2 / f = 176$ (wrong order), $n_3^2 \cdot \phi^3 = 359$ (no), $n_3^2 \cdot 2\pi = 628$ (close, 11% off). No natural combination works. The exponent 707 is not constrained by the Paasch transcendental equations.

**Structural assessment**: Paasch's quantization organizes the REST MASS SPECTRUM of elementary particles through the properties of a logarithmic confining potential. The CC suppression arises from the COLLECTIVE MANY-BODY PHYSICS of a Josephson junction array at finite temperature. These are structurally different physical mechanisms:

- Paasch: single-particle mass eigenvalues $\rightarrow$ logarithmic potential $\rightarrow$ $x = e^{-x^2}$ $\rightarrow$ $\phi$
- CC: many-body gap $\rightarrow$ BCS + Josephson coupling $\rightarrow$ $P_{\text{exc}} = \exp(-\Delta/T)$

The $\exp(-\Delta/T)$ is a standard Boltzmann factor, not a mass quantization. The $\phi$-quantization would enter only if $\Delta$ or $T$ themselves were constrained by the logarithmic potential equation -- and S56 shows they are not. The gap $\Delta_{\text{fabric}} = 13.04\ M_{\text{KK}}$ is set by $E_J$ (which traces to $J_{C_2}^2 \cdot F_{\text{anom}}$, a product of Casimir-2 hopping and BCS pair correlations), and $T_{\text{GH}}$ is set by the Hubble parameter. Neither has the structure $x = e^{-x^2}$.

---

## Section 4: What the S56 Fabric Results Mean for the Paasch Program

### 4.1 The Adiabatic Protection Result

The most consequential S56 result for the Paasch-CC connection is W3-6 (GGE-FABRIC-56): the 2-cell Josephson gap ($13.04\ M_{\text{KK}}$) provides 35x adiabatic protection, suppressing excitation to $P_{\text{exc}} = 6.6 \times 10^{-4}$. The GGE degenerates to the ground state.

From the Paasch perspective, this is a statement about the HIERARCHY between collective energy scales. Paasch's 2016 paper establishes that particle masses span from electron to top quark via exponential factors $\phi^n$ and $f_N^n$. The fabric computation shows that collective energy scales ($E_J$, $\Delta_{\text{fabric}}$, $T_{\text{GH}}$, $T_{\text{BKT}}$) also span multiple decades -- but organized by the Josephson physics of a superfluid lattice, not by Paasch's logarithmic potential.

The hierarchy $T_{\text{GH}} < E_c < \Delta_{\text{BCS}} < E_J < \Delta_{\text{fabric}} < T_{\text{BKT}}$ (in rough ascending order at the fold) is:

| Scale | Value ($M_{\text{KK}}$) | $\ln(\text{value}/T_{\text{GH}})$ |
|:------|:----------------------|:--------------------------------|
| $T_{\text{GH}}$ | 0.590 | 0 |
| $E_c$ | 0.036 | $-2.79$ |
| $\Delta_{\text{BCS}}$ | 0.370 | $-0.47$ |
| $E_J$ | 3.397 (per bond) | $+1.75$ |
| $\Delta_{\text{fabric}}$ | 13.04 | $+3.10$ |
| $T_{\text{BKT}}$ | 6.11 | $+2.34$ |

Taking the logarithms: the spacing between successive scales in log-space is 2.79, 2.32, 2.22, 1.35, 0.76. This is NOT constant -- there is no geometric progression. A Paasch-type organization would require $\ln(\text{scale}_{n+1}/\text{scale}_n) = \text{const} = \ln\phi = 0.426$, which is not observed.

### 4.2 The $\phi_{\text{paasch}}$ Ratio Status After S56

The $\phi_{\text{paasch}} = 1.5316$ ratio at $\tau = 0.15$ (S12 result: $m_{(3,0)}/m_{(0,0)} = 1.531580$) has been extensively tested across S22-S48. S56 adds no new direct test of this ratio, but the fabric results change its interpretive context:

- **PAASCH-SPIRAL-47 FAIL**: Full Dirac spectrum phases are UNIFORM on spiral. No six-sequence structure.
- **PHI-BDG-47 FAIL**: BCS dressing categorically destroys $\phi$ ratio ($-8.6\%$). Max $R_{\text{dressed}} = 1.465 < \phi$.
- **SIX-SEQ-48 UNIFORM**: No clustering. $\chi^2$ $p = 0.40$.
- **S56 W3-6**: The fabric Josephson gap ($13.04\ M_{\text{KK}}$) provides adiabatic protection at the 2-cell level, meaning the BCS condensate -- which destroys $\phi$ -- is preserved during transit rather than quenched. This REINFORCES the PHI-BDG-47 conclusion: in the physical (fabric-coupled) system, the BCS gap persists, and $\phi$ is not a physical observable.

The $\phi$ ratio remains what it has been since S28c: a mathematical property of the bare Dirac operator $D_K$ at a specific $\tau$ value, not a physical prediction of the framework.

### 4.3 Quigg-Rosner Logarithmic Potential and the Fabric

Paasch's logarithmic potential has roots in QCD quarkonium spectroscopy. Quigg and Rosner (1977, 1979) showed that a logarithmic potential $V(r) = A + B\ln(r/r_0)$ yields mass-independent level spacings for quarkonium, explaining why charmonium and bottomonium have similar excitation patterns despite the large $c/b$ mass ratio. Martin (1980) refined this to $r^{0.1}$ (near-logarithmic).

The S56 fabric introduces a new context for logarithmic potentials. The tight-binding Hamiltonian on the 32-cell CG graph has the structure $H_{\text{TB}} = \sum_{ij} J_{ij} c_i^\dagger c_j + \sum_i C_2(i) c_i^\dagger c_i$, where $C_2(i)$ is the quadratic Casimir of the $(p,q)$ representation at cell $i$. The Casimir values are $C_2(0,0) = 0$, $C_2(1,0) = 4/3$, $C_2(1,1) = 3$, $C_2(0,3) = 6$, etc. Taking the logarithm: $\ln C_2$ is well-defined for all nonzero representations, and the spacing $\ln C_2(p+1,q) - \ln C_2(p,q)$ is NOT constant -- it depends on $(p,q)$ through the formula $C_2 = (p^2 + q^2 + pq + 3p + 3q)/3$.

This means the Casimir "potential" on the Peter-Weyl lattice is NOT logarithmic in the Paasch/Quigg-Rosner sense. It grows quadratically in $(p,q)$, not logarithmically in radius. The fabric's on-site potential is polynomial, producing power-law (not exponential) level spacings. This is a structural distinction: Paasch's logarithmic potential and the framework's Casimir potential are different functional forms on their respective configuration spaces.

### 4.4 Connection to the Froggatt-Nielsen Mechanism

The exponential hierarchy $\Delta_{\text{fabric}}/T_{\text{GH}} = 22.1$ is the type of ratio that Froggatt-Nielsen (1979) produces from O(1) charge differences in a U(1) flavor symmetry: mass ratios $\sim \epsilon^{q_i - q_j}$ where $\epsilon \sim 0.2$ is the expansion parameter. In the framework, the analogous structure would be: the Josephson coupling $E_J \sim J_{C_2}^2$ depends on the Casimir-2 eigenvalue of the graph Laplacian, and cells with different $(p,q)$ representations have different $C_2$ values. This produces exponential hierarchies between sectors through the BCS gap equation $\Delta_i \propto \exp(-1/g \cdot N(E_F))$, where $N(E_F)$ depends on the sector's density of states.

The S35 result (BCS instability is a 1D theorem: any $g > 0$ flows to strong coupling) means the gap equation $\Delta \sim \exp(-1/g \cdot N)$ is always operative. The hierarchy between sectors is then set by $N(E_F)$ ratios -- which ARE determined by the SU(3) representation theory that also determines Paasch's $n_3 = 10$.

This is the closest structural connection between the CC exponential and the Paasch program: both trace to properties of SU(3) representation theory, but through entirely different mechanisms (Paasch through the weight lattice counting $n_3 = T_4$; the CC through BCS gap hierarchy depending on sector DOS).

---

## Section 5: Open Computations and Structural Recommendations

### 5.1 What Paasch CAN Constrain in the Fabric Picture

Before listing computations, it is worth stating clearly what the Paasch program can and cannot constrain in the fabric picture:

**Can constrain**: The bare Dirac eigenvalue ratios $\lambda_{(p,q)} / \lambda_{(0,0)}$ at specific $\tau$ values. The $\phi$ ratio at $\tau = 0.15$ is proven (S12, MC $p < 0.01$). The $n_3 = 10$ identity is structural (S48). These are GEOMETRIC properties of the Jensen-deformed SU(3), independent of BCS, Josephson, or fabric physics. They constrain the GEOMETRY, not the thermodynamics.

**Cannot constrain**: The CC suppression, the fabric gap, the adiabatic protection factor, or any many-body quantity built from BCS pairing. These live on the far side of the condensation layer from the bare spectrum where Paasch's ratios are defined.

**Open question**: Whether a LOGARITHMIC functional on the eigenvalues (as opposed to a polynomial/power-law functional like the spectral action) produces non-monotonicity. This is structurally motivated by the Paasch program and has never been tested.

### 5.2 Computable Tests

1. **LOG-SIGNED-40 tau sweep** (carried from S48, still OPEN): The signed logarithmic sum $S_{\text{signed}} = \sum_k (-1)^{F_k} \ln |\lambda_k^2/\mu^2|$ is the natural Paasch-type functional on the spectrum. Single-point value $S_{\text{signed}}(0.19) = +787.8$ (S48), but the tau dependence -- which would test whether a logarithmic potential functional produces non-monotonicity -- requires per-sector eigenvalue recomputation at multiple $\tau$. This is the single most relevant Paasch-motivated computation for the CC question. If $S_{\text{signed}}(\tau)$ has a minimum, it would be a logarithmic-potential-driven stabilization mechanism.

2. **$\Delta_{\text{fabric}}$ scaling with $N_{\text{cell}}$**: W3-6 computes the 2-cell gap. The CC suppression depends on how $\Delta_{\text{fabric}}$ scales with the number of coupled cells (linear? sublinear? saturating?). If $\Delta \sim N^{1/2}$ (as in nuclear pairing), the CC exponent grows as $N^{3/2}/T$ -- a qualitatively different hierarchy than Paasch's $\phi^n$. Computing $\Delta_{\text{fabric}}(N = 3, 4)$ would determine the scaling exponent.

3. **Mass number of $E_J/E_c$**: The ratio $E_J/E_c = 194.1$ is the superfluid order parameter. In Paasch's scheme, the nearest mass number is $N(p) = 150$. The ratio $194.1/150 = 1.294$, close to $f_N/\phi_{\text{golden}} = 1.236/0.618 \cdot 0.5 = 1.00$ (no match). More interestingly, $194 \approx 2 \times 98 = 2 \times N(K)$. This would be testable: does $E_J/E_c = 2 \times N(K)$ persist across $\tau$? The S56 data (W0-1) shows $E_J/E_c$ ranges from 22 to 440 -- it does NOT stay near 194, ruling this out.

### 5.3 Structural Constraints from S56

The following constraints from S56 are permanent and restrict the Paasch-CC connection:

| Constraint | Source | Implication | Surviving space |
|:-----------|:-------|:------------|:----------------|
| $\Delta_{\text{fabric}}$ is many-body, not single-particle | W3-6 | Cannot be organized by Paasch's logarithmic potential (which acts on single-particle masses) | Paasch quantization applies to D_K eigenvalue ratios only |
| GGE degenerates to ground state on fabric | W3-6, $P_{\text{exc}} = 6.6 \times 10^{-4}$ | CC suppression is adiabatic protection, not Boltzmann activation | No thermal activation to quantize |
| Josephson coupling preserves integrability | W1-2, $\langle r \rangle = 0.367$ | CC = integrability thesis reinforced; Paasch quantization cannot break it | Integrability breaking requires anisotropic (mode-dependent) tunneling |
| Fabric energy scales have no geometric progression | This review, Section 4.1 | No $\phi^n$ hierarchy in $T_{\text{GH}}, E_c, \Delta, E_J, \Delta_{\text{fabric}}, T_{\text{BKT}}$ | Log-spacing is monotonically decreasing, not constant |
| $\phi$ ratio destroyed by BCS, reinforced by fabric coherence | PHI-BDG-47 + W3-6 | Fabric adiabatic protection preserves the BCS state that destroys $\phi$ | $\phi$ is bare-spectrum only |

### 5.4 Next Gate

**PAASCH-CC-LOG-57**: Compute $S_{\text{signed}}(\tau) = \sum_k (-1)^{F_k} \ln|\lambda_k^2/\mu^2|$ at 10 $\tau$ values in $[0.05, 0.35]$ using per-sector Dirac eigenvalues. PASS: $S_{\text{signed}}(\tau)$ has a minimum in $[0.10, 0.30]$ with depth $> 1\%$ of $|S_{\text{signed}}(0)|$. FAIL: monotone. This is the natural Paasch functional on the framework's spectrum and the only untested logarithmic stabilization channel.

---

## Closing: The Paasch-CC Structural Position

The CC formula $P_{\text{vac}} \sim \exp(-\Delta_{\text{fabric}} \cdot N/T)$ is an exponential hierarchy, and Paasch's program organizes exponential mass hierarchies. The structural question was whether these are the same kind of exponential or merely share a functional form.

S56 answers this decisively: they are different kinds.

Paasch's exponential arises from a logarithmic confining potential acting on single-particle constituents, producing the transcendental equation $x = e^{-x^2}$ and the quantization factor $\phi = 1.53158$. The CC exponential arises from the Boltzmann suppression of excitations across a many-body gap in a Josephson junction array. The former is a mass quantization condition; the latter is a thermodynamic suppression factor. They share the exponential function but not the mechanism.

The one surviving bridge is algebraic: both Paasch's $n_3 = 10$ (entering the alpha derivation) and the fabric's sector structure (10 Peter-Weyl sectors at truncation level 3) trace to the same SU(3) representation-theoretic identity $\dim(3,0) = T_4 = 10$. This is not a mass quantization condition on the CC; it is a shared geometric origin in the symmetry group. Whether this algebraic coincidence can be promoted to a quantitative prediction requires the LOG-SIGNED computation -- the one Paasch-motivated functional that has never been swept across $\tau$.

The fabric is too stiff ($E_J/E_c = 194$, 14$\sigma$ above SIT), too coherent ($T_{\text{GH}}/T_{\text{BKT}} = 0.097$), and too adiabatically protected ($P_{\text{exc}} = 6.6 \times 10^{-4}$) for Paasch's single-particle mass quantization to imprint on the CC. The CC is a fabric problem. Paasch's quantization lives on the bare Dirac spectrum. These are separated by the BCS condensation layer, which S47 proved destroys $\phi$ at $-8.6\%$.

The constraint map is clear: the Paasch-CC connection is closed at the level of mass quantization, with LOG-SIGNED-57 as the sole surviving logarithmic-functional channel.
