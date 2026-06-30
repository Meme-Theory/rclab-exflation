# The discovery of three-dimensional Van Hove singularity

**Author(s):** Wenbin Wu, Zeping Shi, Mykhaylo Ozerov, Yuhan Du, Yuxiang Wang, Xiao-Sheng Ni, Xianghao Meng, Xiangyu Jiang, Guangyi Wang, Congming Hao, Xinyi Wang, Pengcheng Zhang, Chunhui Pan, Haifeng Pan, Zhenrong Sun, Run Yang, Yang Xu, Yusheng Hou, Zhongbo Yan, Cheng Zhang, Hai-Zhou Lu, Junhao Chu, Xiang Yuan
**Year:** 2024
**Journal:** [Not stated in PDF -- preprint]
**arXiv:** 2304.07043
**Relevance:** HIGH

---

## Abstract

Arising from the extreme/saddle point in electronic bands, Van Hove singularity (VHS) manifests divergent density of states (DOS) and induces various new states of matter such as unconventional superconductivity. VHS is believed to exist in one and two dimensions, but rarely found in three dimension (3D). Here, we report the discovery of 3D VHS in a topological magnet EuCd$_2$As$_2$ by magneto-infrared spectroscopy. External magnetic fields effectively control the exchange interaction in EuCd$_2$As$_2$, and shift 3D Weyl bands continuously, leading to the modification of Fermi velocity and energy dispersion. Above the critical field, the 3D VHS forms and is evidenced by the abrupt emergence of inter-band transitions, which can be quantitatively described by the minimal model of Weyl semimetals. Three additional optical transitions are further predicted theoretically and verified in magneto-near-infrared spectra. Our results pave the way to exploring VHS in 3D systems and uncovering the coordination between electronic correlation and the topological phase.

---

## Key Arguments and Derivations

### 1. VHS Classification by Dimension
Van Hove singularities arise from critical points (extrema/saddle points) in electronic bands:
- **1D**: Band extrema $\to$ DOS divergence $\propto 1/\sqrt{\varepsilon}$ (e.g., Landau bands)
- **2D**: Saddle points $\to$ logarithmic DOS divergence; band extrema become non-divergent
- **3D**: Generally believed absent. The key insight of this work is that 3D VHS can exist under specific conditions in Weyl semimetals.

### 2. Minimal Model for 3D VHS via Weyl Semimetal
The two-band minimal model of a Weyl semimetal:
$$H_0 = (\Delta - m\mathbf{k}^2)\sigma_z + v_{xy}(k_x \sigma_x + k_y \sigma_y)$$
where $\sigma_{x,y,z}$ are Pauli matrices; $\Delta$, $m$, $v_{xy}$ are material-dependent band parameters. The energy bands:
$$E = \pm\sqrt{(\Delta - m\mathbf{k}^2)^2 + v_{xy}^2(k_x^2 + k_y^2)}$$
generate a pair of Weyl nodes at momenta $(0,0,\pm k_c)$ with $k_c \equiv \sqrt{\Delta/m}$ when $\Delta \cdot m > 0$.

The in-plane and out-of-plane Fermi velocities are $v_{xy}$ and $v_z = 2mk_c = 2\sqrt{\Delta \cdot m}$.

### 3. Critical Condition for 3D VHS
When $v_z \geq \sqrt{2} v_{xy}$, a 3D VHS appears at finite in-plane momentum with a Mexican-hat in-plane dispersion. The flat dispersion along the tangential direction effectively reduces the dimension, producing **logarithmically divergent DOS** -- a rare 3D phenomenon. Below this threshold, the saddle point at zero momentum is the only critical point (non-divergent).

### 4. Magnetic Field Tuning via Exchange Interaction
In magnetic Weyl semimetals, the parameter $\Delta$ is sensitive to external magnetic fields through exchange interaction $H_{exc}(B)$ between itinerant electrons and local magnetic moments. The overall Hamiltonian $H = H_0 + H_{exc}(B)$ predicts the appearance of 3D VHS at a critical magnetic field $B_c$ when the condition $v_z = \sqrt{2} v_{xy}$ is met.

### 5. Material Realization: EuCd$_2$As$_2$
EuCd$_2$As$_2$ (trigonal, space group $P\bar{3}m1$) was chosen because:
- A-type antiferromagnetic ground state with Eu moments in-plane
- Strong exchange interaction ($\sim$100 meV energy shift at saturation)
- Single pair of Weyl nodes in the Brillouin zone
- Magnetic saturation field $B_s \approx 2$ T at 2 K
- Critical field for 3D VHS: $B_c \approx 0.6$ T

### 6. Experimental Evidence: Magneto-Infrared Spectroscopy
Two prominent optical features $T_\alpha$ and $T_\beta$ shift systematically with magnetic field and saturate at high fields. An **abrupt enhancement** of optical features occurs at $B_c \approx 0.6$ T -- evidencing formation of 3D VHS. Results reproduced independently at two facilities (NHMFL Tallahassee and ECNU Shanghai) with entirely different detector and magnet setups.

### 7. Model Predictions Verified
Based on band parameters from mid-infrared spectra, the model predicts three additional optical transitions and a crossing feature at higher energy. All are quantitatively verified in near-infrared magneto-spectra.

## Key Results

1. First experimental discovery of a 3D Van Hove singularity
2. 3D VHS realized in topological magnet EuCd$_2$As$_2$ via magnetic field tuning
3. Critical condition: $v_z \geq \sqrt{2} v_{xy}$ produces logarithmically divergent DOS in 3D
4. Critical field $B_c \approx 0.6$ T marks abrupt onset of inter-band transitions
5. Controllable 3D VHS: energy, DOS, and even presence/absence tunable by magnetic field
6. Three predicted additional optical transitions quantitatively confirmed
7. Field dependence of optical transition energies scales with magnetization

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Weyl Hamiltonian | $H_0 = (\Delta - m\mathbf{k}^2)\sigma_z + v_{xy}(k_x \sigma_x + k_y \sigma_y)$ | Eq. (1) |
| Energy bands | $E = \pm\sqrt{(\Delta - m\mathbf{k}^2)^2 + v_{xy}^2(k_x^2 + k_y^2)}$ | Sec. Introduction |
| Weyl node position | $k_c = \sqrt{\Delta/m}$ | Sec. Introduction |
| Out-of-plane Fermi velocity | $v_z = 2mk_c = 2\sqrt{\Delta \cdot m}$ | Sec. Introduction |
| 3D VHS condition | $v_z \geq \sqrt{2}\, v_{xy}$ | Sec. Introduction |
| Full Hamiltonian | $H = H_0 + H_{exc}(B)$ | Sec. Introduction |
| Saturation field | $B_s \approx 2$ T (at 2 K) | Fig. 2a |
| Critical field for VHS | $B_c \approx 0.6$ T | Fig. 2c,d |

## Relevance to Phonon-Exflation

The framework's mechanism chain requires van Hove singularities in the Dirac spectrum on SU(3) to drive BCS instability. A central question has been whether vHs can exist in 3D manifolds (SU(3) is 8-dimensional). This paper demonstrates that 3D VHS with logarithmically divergent DOS **can** exist when anisotropy conditions are met ($v_z \geq \sqrt{2} v_{xy}$). The framework's SU(3) fiber has precisely the kind of anisotropy (different curvature along different generators) that could satisfy an analogous condition for the Dirac operator. The magnetic-field tuning mechanism parallels the framework's tau-parameter tuning of the internal geometry: as tau evolves, the effective Fermi velocities along different SU(3) directions change, potentially crossing a critical threshold where 3D VHS appears and triggers BCS pairing.
