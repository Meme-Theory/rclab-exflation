# Session 74 Synthesis: Horizon Physics, Moduli Stabilization, and the Substrate-Native Page Curve

**Date**: 2026-04-11
**Agent**: hawking-theorist (Hawking)
**Source Documents**:
- `sessions/archive/session-74/session-74-results-workingpaper.md` (S74 W1-W4, 84 computations)
- `.claude/agent-memory/hawking-theorist/MEMORY.md` (S73 carry-forward and permanent theorems)

---

## I. Session Outcome

S74 decisively resolved the S73B alpha_s = +0.833 (125-sigma) tension via multifield transfer (W1-A `|alpha_s|` = 8.4e-15, machine epsilon) but left n_s = 1 scale-invariant on this route; closed the single-instanton, Coulomb-gas, and 't Hooft-vertex routes to substrate-internal modulus stabilization (W1-B FAIL, W1-Q FAIL, W1-R FAIL, all with 158-309x shortfalls or 12-OOM suppressions); established the self-consistent Hawking temperature of the kinematic entry horizon at `T_H = 72.838 M_KK` (W3-B PASS, exact `|2 pi T_H - kappa_v| = 0` at machine precision); and confirmed that the Euclidean path integral `Z = Tr f(D_K^2/Lambda^2)` is non-perturbatively J-invariant to 5.8e-11 (W4-H PASS), lifting the S21 infinitesimal `[J, D_K] = 0` theorem to the full spectral action sum over 1.08M weighted modes.

The session established a **three-scale kappa hierarchy** on a single spectral triple (W3-E): structural `kappa_spec = 0.104 M_KK`, kinematic `kappa_v = 457.66 M_KK`, and curvature-spline `kappa_fold = 79,386 M_KK`. These are three independent spectral-moment projections of the same D_K; the 173x and 4420x ratios are bookkeeping artifacts, not physical discrepancies. The W3-E structural route finds **no horizon at all** in the c_spec projection -- the modulus is supersonic by factor ~12.6 throughout the entry window -- confirming that the entry horizon is purely a feature of the W3-B group-velocity projection. This is the substrate-native version of Hawking's 1975 horizon-subspace selection: the horizon exists only in one kinematic channel, carrying no spectral reorganization in the geometric channel.

---

## II. Key Results

### W1-A: Multifield Transfer Eliminates the 125-sigma alpha_s Tension

**Result**: `|alpha_s(k_pivot)|` = 8.39e-15 (machine epsilon) on the emergent 4D pivot k = 0.05 Mpc^{-1}, down from `|alpha_s^{S73B}|` = +0.833 at the fiber level. `n_s(k_pivot)` = 1.000000 (exact scale-invariance). **Classification**: PHONONIC.

The S73B TRANSIT-PS tension -- a 125-sigma failure driven by the `r_BCS(B1) = 3.57` near-Fermi-surface accident in the (0,0) Peter-Weyl sector -- dissolves when the fiber-level fold Bogoliubov coefficients are projected onto the emergent 4D Hubble horizon via per-branch Jacobians `J_b = sqrt(psi_b) / H_{cross,b}`. The three branches cross the emergent horizon at different substrate times (`tau_cross(B1) = 18.0`, `tau_cross(B2) = 112.5`, `tau_cross(B3) = 13.2`), and their per-branch Planck factors `H_cross^2 ~ (c_b k)^2` cancel exactly against the Jacobian-squared `J_b^2 ~ 1/H_cross^2 ~ 1/(c_b k)^2`. This is the Sasaki-Stewart multifield theorem realized at the spectral-triple level: scale-invariance is **structurally forced** when H(tau) decays radiation-like, independent of the fiber-level squeezing hierarchy.

The transfer function does **not** produce a red tilt. n_s = 1 is exact at every k because the k-dependence cancels between Planck factor and Jacobian. The fiber-level `r_B1 = 2 r_B2` non-monotonicity cannot propagate to CMB scales -- this is the substrate-native resolution of the S73B alpha_s = +0.833 puzzle: the 125-sigma diagnosis was correct, but it was diagnosing an extrapolation error of a 3-point fiber fit over `Delta_lnk = 0.07`, not a failure of the underlying transit physics. The A_s gap reduces from +6.66 OOM (raw single-branch) to +5.83 OOM (multifield-projected); the remaining 5.83 OOM must close through BCS dressing (S66 Coleman-Weinberg route, already at `n_s = 0.9595`) or the W3-E ENTRY-TH-DERIV/dissipative channels.

### W1-B: Moduli Stabilization Runs Away on All Four Sub-Gates

**Result**: 0 minima in `[0.45, 0.70]` across all four sub-gates at `L_max in {3,5,7}`. Ratio `|dV_restoring|/|dV_runaway|` at `tau = 0.48`: **0.28%** (instanton-only) or 0.27% (compound, since BCS dressing and GGE relic **reinforce** the runaway). **Classification**: GEOMETRIC.

The substrate-internal effective potential `V_eff(tau)` on the Jensen-deformed SU(3) spectral triple has no minimum in the Planck-preferred band. The bare spectral action gradient `dV_bare/dtau = +445 M_KK^4` at `tau = 0.48` overwhelms the single-instanton restoring force of 1.44 M_KK^4 by a factor of 309. More damaging: **sub-gates (b) and (c) push in the wrong direction**. BCS dressing yields `Delta V_BCS = -(1/2) N_BCS |Delta(tau)|^2`, a negative condensation energy; because `Delta(tau)` is monotonically decreasing from 0.4654 M_KK at the fold to 0.1178 M_KK at tau = 1.614, `V_BCS(tau)` is monotonically RISING (from -90.87 to -5.59 M_KK^4), adding +77.6 M_KK^4 to `dV/dtau` at the kappa=1 crossing. The GGE relic adds another +1.10 M_KK^4 through spectral-rescaling monotonicity `d<H_GGE>/dtau > 0`. And sub-gate (d) confirms that raising `L_max` from 3 to 7 (450x more weighted eigenvalues) yields zero sign changes in `dS/dtau` -- the monotonicity is not a truncation artifact.

Only sub-gate (a) places the (qualitative) minimum at the right location: `n_inst(tau)` peaks at `tau ~ 0.595` exactly in the target band, a consequence of the instanton action `S_inst(tau) = 2 pi^2 exp(-2 tau)` decreasing with tau. This is a structurally interesting finding -- the topological-sector density has the right geometry -- but the magnitude of the one-instanton back-reaction is governed by `E_inst = gap^2 ~ 0.75 M_KK^4`, 1740x smaller than the bare potential depth. Adding the W2-R analytic refinement (`dV_inst/dtau = -1.438 M_KK^4`, 0.36% different from W1-B's CubicSpline) confirms the W1-B conclusion is **not a precision artifact**: the 213x shortfall is structural. The W1-B retraction of "single-instanton saddle closes modulus" is permanent.

### W1-Q, W1-R: Coulomb-Gas and 't Hooft Channels Cannot Salvage W1-B

**Result (W1-Q)**: Coulomb-gas enhancement over dilute = 1.97x, insufficient to close shortfall. `|dV_CG/dtau|(tau=0.48) = 2.80 M_KK^4` vs `|dV_bare/dtau| = 445 M_KK^4`; remaining shortfall 158.8x. **Classification**: GEOMETRIC.

**Result (W1-R)**: `|dV_tHooft/dtau|(tau=0.48) = 1.498e-07 M_KK^4`, 2.55e-12 of the bare driving gradient. The 6-fermion vertex is the **most strongly suppressed** contribution yet tested, 7 OOM below the one-instanton back-reaction and 12 OOM below the bare gradient. **Classification**: GEOMETRIC.

The W1-Q Coulomb-gas treatment over `(n_I, n_{Ibar})` sectors with log-Coulomb interactions on the instanton moduli space `[rho_min, rho_max] = [1, 2.462]` yields a uniform ~2.0x enhancement over the dilute Boltzmann sum. This is almost entirely the structural doubling `1 + 2y` from symmetric counting of instantons and anti-instantons, plus a small `cosh(0.579) ~ 1.175` attractive-pair enhancement from the `(1,1)` sector partially canceling the repulsive `(2,0) + (0,2)` sector. Extending to 3-body sectors adds only ~1-2%. **The 309x shortfall is structural to the fugacity scale `y(tau) ~ n_inst(tau) = O(1)`**, not a dilute-gas truncation artifact. Scale-bracket invariance: shifting `rho_max` by +/-20% changes `|dV|` by <4%.

The W1-R 't Hooft vertex `V_tHooft(tau) = K Lambda^4 exp(-8 pi^2 exp(-2 tau))` is a double-exponential in tau. At `tau = 0.48` the instanton action is `S_inst = 30.23`, so the Boltzmann suppression `exp(-30.23) ~ 7e-14` dominates the vertex magnitude. The permanent structural addendum: the vertex only reaches 1% of the bare driving gradient for `tau >= 1.53`, which is essentially coincident with the S73B runaway position `tau = 1.614`. **The vertex becomes relevant only when it is no longer needed** -- a PERMANENT constraint on the 't Hooft channel's viability for modulus stabilization. Together with W1-B (single instanton), W1-P (connected correlator), and W1-Q (Coulomb gas), this triangulates: no one-instanton, multi-instanton, or local fermion-number-violating vertex in the Jensen-deformed SU(3) gauge sector closes the W1-B shortfall. Something qualitatively different -- multi-instanton condensate at `p+q >= 8`, cross-spectral-moment back-reaction (a_2/a_4 sectors), or fold-stiffness renormalization -- is required.

### W2-C: Fold-Squeeze Backreaction Too Small to Close kappa Inconsistency

**Result**: `delta_kappa = +0.00487` (0.49% reduction), below the 2% INFO floor. **Classification**: PHONONIC.

The S70/S71 kappa_entry = 79,386 vs kappa_v = 457.66 factor-173 inconsistency was flagged as potentially resolvable by fold-squeeze Bogoliubov backreaction on the horizon surface gravity. At `tau_entry = 0.2195`, the three B3 modes carry 81.8% of the squeeze weight with `cos(phi_comp) ~ -0.52`, producing per-mode `factor_k ~ 0.953` (4.7% sound-speed reduction). B1 at 15% weight has `cos(phi) = +0.12`, slightly amplifying its contribution. The weighted-average effective sound speed is 0.9638, a 3.62% reduction -- but because `v_g = v_tau - c_s` and `|v_tau| << |c_s|` at `tau_entry`, the propagation to surface gravity dilutes this to **0.49%**. The small-r validity window (`r_exit ~ 0.05-0.12`) was confirmed: at `r ~ 2.92` (n_bar = 85.2 stress test) the `cosh(2r)` variance term dominates and the formula flips sign unphysically.

This is a boundary result: the S70/S71 kappa inconsistency cannot be a backreaction effect. The W3-B finding supersedes this entirely -- the 173x ratio is **not a physics discrepancy** but a definitional mismatch between two diagnostics of the D_K spectral triple. The fold-squeeze channel is closed as a potential resolver; the resolution is W3-B's exact identity `2 pi T_H = kappa_v` at machine precision.

### W2-L: Self-Consistency Fixed-Point FAIL by Prerequisite

**Result**: All three initial conditions converge to `tau* = -0.887`, outside the physical transit regime. Gate FAIL by W1-B prerequisite. **Classification**: GEOMETRIC.

The joint `(T_b, tau_min)` fixed-point loop has **no tau_min input** to iterate against because W1-B returned no V_eff minimum in any sub-gate. Proceeding with the tilted-parabola local model at the fold (`V_local = V_bcs_fold + dV_bcs_fold * dtau + 0.5 * k_local * dtau^2` with `k_local = +84.89 M_KK^2` from W2-D's BCS-dressed 36D Hessian and `dV_bcs_fold = +91.43 M_KK^4` from the global runaway), the formal critical point is `tau_local_crit = 0.19 - 91.43/84.89 = -0.887`, LEFT of the fold. This is a mathematical artifact of the quadratic model evaluated outside its regime of validity.

The permanent structural result: `tau_local_crit = tau_fold - dV_bcs_fold / curv_jensen_bcs = -0.887` is an algebraic identity that closes the "local convexity rescues global runaway" channel at the fold. Even the `(35+, 0-, 0)` Morse-nondegenerate signature from W2-D (local minimum in the 36D `Sym^2(su(3))` moduli fluctuations) is insufficient: the local Hessian is positive in the transverse moduli, but the Jensen-direction runaway `dV_bcs_fold = +91.43 M_KK^4` wins over the local curvature `k_local = +84.89 M_KK^2` over any tau width `|Delta_tau| > delta_tau_balance/2 ~ 0.54`. Over a typical 0.1 tau width, slope dominates curvature by ~10.8x. **Modulus stabilization cannot come from local Jensen curvature alone.**

### W2-R: Analytic Instanton Stabilization Confirms W1-B is Not a Precision Artifact

**Result**: `dV_inst_A/dtau(0.480) = -1.438 M_KK^4` (analytic), versus W1-B CubicSpline-on-21-points result -1.436 (0.17% relative error). Shortfall 213x against canonical threshold. Gate INFO (sign correct, magnitude FAIL). **Classification**: GEOMETRIC.

The W2-R analytic computation uses the closed-form chain rule on `n_inst(tau) = C S^6 exp(-S)` with `S_inst(tau) = 2 pi^2 exp(-2 tau)`. The n_inst peak location `tau_peak = -0.5 ln(6/(2 pi^2)) = 0.595424` is exact, coincident with the target band center. Precision cross-check: the 21-point CubicSpline W1-B result is 0.17% accurate in `|dV/dtau|`; the analytic refinement shifts the shortfall ratio from 3.22e-3 to 3.23e-3, a 0.36% bookkeeping change. The multi-charge tower (`Q = 1, 2, ..., 5`) contributes at most factor 1.034 to the force; combined with W1-P's 2.21x Coulomb-gas factor, the total correction is ~96x below the canonical threshold of 305.83 M_KK^4.

The physical conclusion is identical to FAIL: single-field instanton stabilization at `alpha = 1` (flat-space dilute gas) is ruled out by more than precision-level margins. The `alpha > 1` valley-deformed regime (W2-S IBAR-VALLEY-JACOBIAN) is a distinct channel and should not be conflated with this result. The "maybe W1-B's precision was inadequate" escape hatch is closed.

### W3-B: T_entry Self-Consistency at Machine Precision

**Result**: `kappa_entry_v2 = 457.655933 M_KK`, `T_H = 72.838204 M_KK`, identity residual `|2 pi T_H - kappa_v2|/kappa_v2 = 0.000e+00` (exact floating-point round-trip). **Classification**: PHONONIC.

Three independent estimators for `|dv_tau/dtau|` at `tau_entry = 0.21950`: Method A (cubic spline) = 457.656, Method B (np.gradient + linear interp) = 457.677, Method C (nearest-grid) = 459.942. Method A adopted as canonical. The Hawking temperature `T_H = 72.838 M_KK` is reproduced from the S71 stored value `kappa_v_s71 = 457.656` to `6.45e-07` relative deviation (cubic vs grid-derivative estimator).

The S71 Phase-1 `kappa_entry = 79,386` is reframed as a **separate diagnostic** -- specifically, a 4-point logarithmic spline on the Mach-number curve, multiplied by the sound speed `c_s ~ 432 M_KK`. It is the "Mach-gradient curvature scale" of the S70 transit profile, not a rival Hawking surface gravity. The 173x ratio between 79,386 and 457.656 is a dimensional/interpolation bookkeeping artifact, not a physical discrepancy. Any S74+ computation using `T_entry` must use 72.838 M_KK unambiguously. The W2-C carry-forward gate `KAPPA-DEFINITION-75` is now cleanly closed by this decomposition.

### W3-E: Structural Route Finds No Entry Horizon At All

**Result**: `c_spec(tau)` = sqrt(a_2/a_0) range `[0.6494, 0.6576] M_KK` on the entry window. Modulus velocity `v_modulus = 8.27 M_KK`. Mach number `v_mod/c_spec = [12.58, 12.73]` -- **supersonic throughout**, no crossing. Projected `kappa_spec = 0.104 M_KK`, `T_spec = 0.0165 M_KK`, **4420x below W3-B**. **Classification**: GEOMETRIC.

This is the deepest structural finding of the Hawking gates. The Seeley-DeWitt ratio `c_spec = sqrt(a_2/a_0)` probes the intrinsic scalar-curvature content of the emergent 4D geometry -- `a_2 = R * Vol` in M_KK^{-2} units, `a_0 = Vol` dimensionless -- and sets a "geometric sound speed" of 0.66 M_KK. The modulus velocity `omega_tau = 8.27 M_KK` is set by a **different** spectral moment chain: `dS/dtau` against the ATDHFB collective mass. These are independent projections:

- `c_spec` probes the GEOMETRIC content of D_K (volume vs curvature).
- `v_modulus` probes the DYNAMICAL content (Jensen-parameter force vs inertia).

On this structural route, **there is no `c_spec = v_modulus` crossing in the entry window** -- the modulus is supersonic by factor ~12.6 throughout `[0.18, 0.25]`. This is not a numerical failure; it is a diagnostic that the entry horizon is a feature of the W3-B kinematic projection only. The framework now has a **three-kappa hierarchy** on the same D_K:

| Route | kappa [M_KK] | Definition | Projection |
|:------|-------------:|:-----------|:-----------|
| W3-E structural c_spec | 0.104 | `|d sqrt(a_2/a_0)/dtau|_fold` | Seeley-DeWitt ratio -- GEOMETRIC |
| W3-B / S71 kappa_v | 457.66 | `|dv_g/dtau|_{tau_entry}` | Branch-averaged group velocity -- KINEMATIC |
| S71 kappa_entry | 79,386 | Mach-spline curvature | Curvature scale from Ma spline |

These are three independent spectral-moment projections. The Hawking-thermal interpretation `T_H = kappa/(2 pi)` belongs to the W3-B kinematic route alone. The structural route has no horizon -- because `sqrt(a_2/a_0)` is not a kinematic velocity and its gradient is not a surface gravity.

**This is the substrate-native version of Hawking's 1975 horizon-subspace selection**: Hawking showed that only a specific causal-structure feature (the future horizon) produces thermal radiation via Bogoliubov mixing of positive and negative frequency modes. Here, only the specific spectral-moment projection (the kinematic `v_g` channel on the `F_{+2}` moment chain) produces a horizon. The `F_{-1}` (cosmological constant), `F_{+1}` (NEC), and geometric `F_{0}` (a_2/a_0) chains see no horizon. Information paradox dissolution: in the GEOMETRIC projection there is nothing behind the horizon because there is no horizon -- the "paradox" is an artifact of projecting a pure substrate state onto one kinematic channel while asking about information encoded in another channel (the a_2 projection, as S71/S73B Block-Diagonal Sector Protection Theorem #22 already established).

The c_spec = sqrt(a_2/a_0) formula is **forced by the spectral action structure**. There is no free parameter to adjust. The 12.6x supersonic ratio is a structural constant of the framework, permanent until a different projection is chosen.

### W3-G: Island-Lefschetz Page Curve Agrees at Peak, Differs at Small k

**Result**: max relative deviation = 0.2084 at k = 3 (t = 1/8), mean relative deviation = 0.1459. Peak match exact by one-parameter normalization (`c_norm = 5.4612`). Gate INFO (in `[0.10, 0.30]`). **Classification**: PHONONIC.

The S72 ensemble-averaged bipartition entropy on `CG(24)` with `s_0 = 1.4259 nats/edge` is compared against the one-time Lefschetz thimble Gaussian squeezed-thermal state from W2-E on the 35-dim volume-preserving Hessian (W2-D signature `(35+, 0-, 0)` confirms Morse-nondegenerate saddle). For a two-mode squeezed vacuum, the reduced-subsystem symplectic eigenvalue is `nu_k = cosh(2 r_k)/2`; at finite temperature `nu_k = (1/2 + n_k^th) cosh(2 r_k)`. Cross-check: `g(sinh^2 r) = h(cosh(2r)/2)` verified to machine precision for `r in {0.01, 0.03, 0.1}`.

The 35 bosonic moduli paired into 17 squeezed pairs plus 1 unpaired. Per-pair bosonic entropies in `[5.97e-3, 8.99e-3]` nats. Fermion sector adds a monogamous contribution with per-pair ceiling `log 2 = 0.6931` nats reduced by gap fraction `Delta_0/(Delta_0 + T_state) = 0.8056`, yielding `s_ferm_per_pair = 0.5584` nats and `S_ferm_max = 9.4933` nats. The ratio `S_boson_max/S_ferm_max = 0.01362` -- **bosons are a 1% correction, fermion pairs carry essentially all Page entropy**.

The two curves match exactly at the peak (49.7887 nats, by construction) and at `k = 11` (2% deviation), systematically diverging toward small k where they differ by 20%. The INFO verdict does NOT mean ensemble averaging matters for the Page curve; it means the shape has a second-order dependence on how the subsystem is defined (graph bipartition vs phase-space mode partition). The `(24 vs 35)` Hilbert-space dimensionality ratio produces a ~20% shape asymmetry at small k. The saddle-point approximation reproduces the ensemble-averaged entropy at >= 80% fidelity over the full half-bipartition range; at `k >= 10` agreement is near-exact (Page's random-state formula is tightest where it matters).

Critically, W3-G **routes the Page curve through the kinematic (v_g) channel**, not the spectral one. This matches W3-E's finding: the Page curve exists only in the sector that sees a horizon. The spectral sound-speed sector carries NO Page curve at all because it carries no horizon. This is consistent with the Baptista framework: fibre entanglement flows through the kinematic channel, not the spectral one, and is captured by the one-time Lefschetz thimble as a Gaussian-saddle reconstruction of the S72 ensemble average.

### W3-H: 3-Cell GSL Cross-Check PASSES to 3.81%

**Result**: `sigma_phi^2(K_3)/sigma_phi^2(CG(24)) = 0.9619`, `delta_phi` agreement to 1.92%, variance agreement to 3.81%. Gate PASS. **Classification**: PHONONIC.

The S71 three-cell GSL frustrated ring (`K_3` topology, phi_ring = `[0, 2pi/3, 4pi/3]`) is the strict 3-cell limit of the W1-E Route 2 cell-phase variance formula `sigma_phi^2 = sigma_sj^2 * R_spectral`, where `sigma_sj^2 = sqrt(2 E_C / E_J) = 0.99759` is the single-junction reference and `R_spectral = (1/N) sum_{alpha>0} lambda_alpha^{-1/2}` is a pure graph Laplacian invariant. For `K_3`, `R_spectral = 2/(3 sqrt(3)) = 0.38490` (analytic, exact to 1e-15). For `CG(24)` Cayley graph of `S_4`, `R_spectral = 0.40015`. The ratio `0.9619` drives the 4% variance agreement.

Both computations use identical inputs: `J_C2 = 0.933` (Josephson coupling), `Delta_BCS = 0.46425` (Route 2 OES E_C), 3-bond Josephson topology. This is the quantitatively-direct cross-check; the S71 per-cell entanglement entropies `[0.693, 0, 0.693]` use a truncated 4-state charge basis that cannot directly measure `sigma_phi^2` (only via `n_eq ~ 0.158`, `r_eq ~ 0.388` which agree in order of magnitude). The harmonic-limit graph-Laplacian variance comparison is the rigorous cross-check, and it passes with 4x margin against the 15% threshold. W3-H confirms that `R_spectral` is the correct GRAPH INVARIANT that extrapolates the S71 minimal-topology result to the full CG(24) substrate.

### W4-E: Modulus Decay Reheats 12 OOM Above BBN Floor

**Result**: `T_rh = 1.374e+10 GeV = 1.374e+13 MeV`. Gate PASS by 13 orders of magnitude above the 1 MeV BBN threshold. **Classification**: PHONONIC (with a GEOMETRIC coupling derivation).

Post-fold at `tau_post = 0.20` (first grid point past `tau_fold = 0.19`), the substrate modulus decays through the instanton-mediated channel. The canonical modulus is `phi_mod = M_KK * tau` with substrate vertex `g_mod = |dS_inst/dtau|_{post} = 26.5073` (dimensionless, loaded from `s73a_instanton_landscape.npz`). Decay constant `f_mod = M_KK / g_mod = 2.802e+15 GeV`, sub-Planckian at `f_mod/M_Pl_red = 1.15e-3`. Modulus mass from the curvature of the instanton-generated potential: `m_mod^2 = M_KK^2 * [(dS/dtau)^2 - d^2 S/dtau^2] * exp(-S_inst)`, yielding `m_mod = 2.535e+15 GeV` and `m_mod/M_KK = 0.034` (sub-M_KK, enforced automatically by the `exp(-S_inst) = 1.80e-6` factor).

Modulus-to-two-gluon rate: `Gamma(phi_mod -> gg) = N_G * m_mod^3 / (64 pi f_mod^2) = 8.255e+13 GeV` (bare). Instanton mediation suppresses by `exp(-2 S_inst) = 3.22e-12`, yielding `Gamma_mod = 2.654e+02 GeV`. Reheat temperature from standard radiation-era matching: `T_rh = (90/(pi^2 g_*))^{1/4} sqrt(Gamma_mod M_Pl_red) = 1.374e+10 GeV`.

The physical story is substrate-native: after the fold, the Jensen deformation reorganizes the D_K eigenvalue spectrum; `S_inst(tau)` measures how much spectral density must tunnel through the fold to settle; when tau relaxes post-fold, spectral weight cascades into the SU(3) gauge connection between fibers, populating the 8-fold gluon sector. **This cascade IS reheating** -- not a separate physical process. The `exp(-2 S_inst)` suppression is self-regulating: without it `T_rh_bare = 7.66e15 GeV` sits above M_KK (illegal regime); the very tunneling amplitude that lets the modulus decay is what keeps the decay rate below M_KK. This is Ordered-Veil self-consistency, not tuning. The result leaves plenty of thermal room for the standard sequence (EW transition, QCD confinement, BBN, CMB decoupling) to unfold on the emergent 4D a_2 metric.

### W4-H: Non-Perturbative J-Invariance of the Euclidean Path Integral

**Result**: `|Z_J/Z - 1| = 5.821e-11 < 1e-10`. Gate PASS. Lifts the S21 infinitesimal `[J, D_K] = 0` theorem to the full spectral action sum over 1,077,120 weighted modes at `L_max = 7`. **Classification**: GEOMETRIC.

The Euclidean partition function `Z = Tr f(D_K^2/Lambda_UV^2)` is computed directly as a sum over 20,064 unique D_K eigenvalues at `tau_fold = 0.19`, weighted by Peter-Weyl multiplicities across 36 sectors `(p,q)` with `p+q <= 7`. The Chamseddine-Connes cutoff polynomial `f(u) = 1 - u + u^2/2 - u^3/6 + u^4/24` is a quartic in `D_K^2`, i.e., 8th-order in D_K. The J transformation is the antilinear `(p,q) -> (q,p)` permutation (KO-dim 6, `J^2 = +1`).

The result `|ln Z - ln Z_J| = 5.82e-11` is the non-perturbative extension of the permanent S21 theorem. **This is strictly stronger than the infinitesimal `[J, D_K] = 0`**: the infinitesimal statement is a first-derivative test at the operator level, while `Z` is an 8th-order polynomial in D_K summed over 1.08M modes. The anomaly decomposes entirely as eigenvalue-conjugation noise: max per-pair `|dlam|` = 1.23e-13 at the `(3,4) <-> (4,3)` pair (d = 90), mean per-eigenvalue error ~5e-15, consistent with IEEE 754 double-precision rounding. Conjugate-pair balance `(S_pq + S_qp) - (S_J_pq + S_J_qp) = 0` exactly for all 16 pairs; self-conjugate invariance for `(0,0), (1,1), (2,2), (3,3)` exact. Linear response cross-check: injected asymmetric perturbation `delta lam = +1e-8` on `lam[0]` of sector (1,2) only; direct response `delta_ln_Z = 4.884e-08` matches analytic prediction `4.880e-08` to 0.07%, and matches J-transformed response `4.878e-08` within the 5.82e-11 anomaly floor.

Structural consequence for the Block-Diagonal Sector Protection Theorem (S73B #22): BDSPT is now rigorous at the non-perturbative level. The 240-dimensional BCS subspace `(0,0) + (0,1) + (1,0) + (1,1)` is `J`-invariant (contains both self-conjugate and conjugate-pair elements), and since the spectral action contains no `J`-breaking (odd-in-D_K) terms, the BCS subspace is causally closed under ALL `J`-invariant dynamical evolutions at the non-perturbative level. **The CPT-protected dark matter sector is above numerical suspicion within this test**. The only way to leak out is via an explicit `J`-breaking term requiring a `gamma_9` insertion -- the spectral action has no such term.

### W4-P: Mott Gap Redshift Places it at Ultralight Cosmological Frequency

**Result**: `E_C_today = 1.0373e-41 GeV = 1.0373e-32 eV` under canonical `a^{-1}` frequency scaling. Gate PASS (rescaling well-defined, invertibility to machine epsilon). `E_C_today / H_0 = 7.21`. **Classification**: GEOMETRIC (spectral first-order-operator eigenvalue redshifted through emergent FRW).

Under `a_today/a_fold = exp(+N_total) = exp(132.4488) = 3.3e+57`, the Mott charging gap `E_C_fold = 0.46425 M_KK = 3.45e+16 GeV` redshifts as a frequency-like eigenvalue `omega_phys(t) = omega_fold * (a_fold/a_today)` to `E_C_today = 1.04e-41 GeV`. The fold ratio `E_C_fold/H_fold = 1.17` is preserved by common `a^{-1}` redshift, yielding today `E_C_today/H_0 = 7.21`: the Mott mode is still underdamped by Hubble friction, completing roughly one full oscillation per Hubble time (period ~12.6 Gyr, frequency `1.58e-17 Hz`).

Wavelength picture: `lambda_mode_today = 1.90e+25 m` vs Hubble radius `c/H_0 = 1.37e+26 m`, ratio `0.139`. The redshifted mode wavelength is about one-seventh of the Hubble radius -- a permanent structural identity from `E_C_fold/H_fold = 1.17` carried forward by common `a^{-1}` redshift.

The DM implication: Mott DM is **ultralight** at `10^{-32} eV`, 11 OOM below the fuzzy-DM Lyman-alpha bound `m > 10^{-21} eV`. This closes the Mott sector as a DM candidate under the physical `a^{-1}` scaling. DM remains the Leggett-1 mode (S66 LEGGETT-SPECTRAL PASS, `omega_L1 = 0.138 M_KK`), which also redshifts to an ultralight scale `3.08e-33 eV` under `a^{-1}`. The Mott gap enters the framework only through the W2-F decoherence channel (`delta_OOM_Mott = 0.141`), not as DM. The "horizon-scale alignment" `lambda_mode_today/(c/H_0) ~ 0.14` is a **non-trivial prediction** emerging from fold-scale Landau-universality: when the microscopic gap and the Hubble scale are built from the same spectral operator, they redshift in lock-step and their ratio is fixed by fold dynamics alone.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W1-A TRANSFER-FUNCTION-74 | INFO | `alpha_s = 8.4e-15` (PASS) but `n_s = 1.000` (out of Planck band) |
| W1-B MODULI-STABILIZATION-74 | FAIL | 0 minima in `[0.45, 0.70]` across all 4 sub-gates; restoring/driving ratio 0.28% |
| W1-Q COULOMB-GAS-INSTANTON-VEFF-74 | FAIL | CG enhancement 1.97x; ratio vs bare 6.30e-3; remaining shortfall 158.8x |
| W1-R TH-OOFT-VERTEX-MODULUS-74 | FAIL | `|dV_tHooft/dtau|/|dS_bare/dtau| = 2.55e-12` (12 OOM below PASS) |
| W2-C HFB-HORIZON-BACKREACTION-74 | FAIL | `delta_kappa = +0.00487` (below 2% INFO floor) |
| W2-L SELF-CONSISTENCY-74 | FAIL | Prerequisite (W1-B FAIL); `tau_local_crit = -0.887` unphysical |
| W2-R INSTANTON-STABILIZATION-74 | INFO | `dV_inst/dtau = -1.438 M_KK^4`; sign correct, magnitude 213x short |
| W3-B T-ENTRY-D-K-74 | PASS | `T_H = 72.838204 M_KK`, identity residual 0.000e+00 (machine zero) |
| W3-E ENTRY-TH-DERIV-74 | FAIL | `T_spec = 0.0165 M_KK` vs `T_H = 72.838 M_KK`, 4420x split (route-split discriminant) |
| W3-G ISLAND-LEFSCHETZ-CONSISTENCY-74 | INFO | max rel dev = 0.2084 at k=3; mean 0.1459; peak match exact |
| W3-H S71-THREE-CELL-GSL-CROSS-CHECK-74 | PASS | `sigma_phi^2(K_3)/sigma_phi^2(CG(24)) = 0.9619`, 3.81% variance agreement |
| W4-E N15-MODULUS-DECAY-74 | PASS | `T_rh = 1.374e+10 GeV`, 13 OOM above BBN floor |
| W4-H BDSPT-ANOMALY-74 | PASS | `|Z_J/Z - 1| = 5.821e-11 < 1e-10` |
| W4-P MOTT-GAP-RENORMALIZATION-74 | PASS | `E_C_today = 1.04e-32 eV` under canonical `a^{-1}` scaling |

---

## IV. Structural Implications

**Permanent theorems established or strengthened by S74 Hawking-program results**:

1. **Non-perturbative J-invariance of Euclidean spectral action** (W4-H, PERMANENT). The partition function `Z = Tr f(D_K^2/Lambda^2)` is J-invariant to 5.8e-11 (machine precision floor) at `L_max = 7` over 1.08M weighted modes. This lifts the S21 infinitesimal `[J, D_K] = 0` theorem to the full non-perturbative path integral. The BDSPT (S73B theorem #22) inherits non-perturbative rigor: the 240-dimensional BCS subspace `(0,0) + (0,1) + (1,0) + (1,1)` is causally closed under all J-invariant dynamics, not merely at the operator-derivative level.

2. **Three-kappa hierarchy on a single D_K** (W3-B + W3-E, PERMANENT). The Hawking-thermal interpretation `T_H = kappa/(2 pi)` exists only in one spectral-moment projection. The structural `c_spec = sqrt(a_2/a_0)` projection sees NO horizon (modulus supersonic by factor 12.6 throughout the entry window); the branch-averaged group-velocity projection sees `kappa_v = 457.66 M_KK`; the Mach-spline curvature projection sees `kappa_fold = 79,386 M_KK`. The 173x and 4420x ratios are definitional, not physical. This is the substrate-native version of Hawking 1975's horizon-subspace selection.

3. **T_H = 72.838 M_KK self-consistency identity** (W3-B, PERMANENT). `|2 pi T_H - kappa_v| = 0` at floating-point machine precision. Any S74+ computation using `T_entry` must use 72.838 M_KK unambiguously; the S71 reference to `kappa_entry = 79,386` as a Hawking surface gravity is retracted and reframed as `kappa_fold_curvature`.

4. **tau_local_crit = -0.887 algebraic identity** (W2-L, PERMANENT). Any future modulus stabilization proposal must introduce a NEW effect that reverses the slope at some `tau > tau_fold`, not appeal to the fold's own local Hessian. The BCS-dressed local convexity `k_local = +84.89 M_KK^2` cannot rescue the global runaway `dV_bcs/dtau = +91.43 M_KK^4`; the local quadratic minimum sits at `tau = -0.887`, outside the physical transit regime.

5. **'t Hooft vertex irrelevance in target band** (W1-R, PERMANENT). The analytic formula `V_tHooft(tau) = K Lambda^4 exp(-8 pi^2 exp(-2 tau))` guarantees that the 6-fermion vertex reaches 1% of the bare driving gradient only at `tau >= 1.53`, coincident with the S73B runaway position. The vertex becomes relevant only when it is no longer needed -- a permanent structural constraint on fermion-number-violating routes to modulus stabilization.

6. **Horizon-scale alignment of ultralight modes** (W4-P, PERMANENT). Under `a^{-1}` frequency scaling, `lambda_mode_today/(c/H_0) = 0.139` is a structural identity carried forward from `E_C_fold/H_fold = 1.17` via common redshift. In any emergent spacetime picture where the microscopic gap and the Hubble scale are built from the same spectral operator, they redshift in lock-step -- a Landau-universal observation not a tuning.

**Constraint-map updates (what closed, what survives)**:

- **CLOSED**: Single-instanton `alpha = 1` modulus stabilization (W1-B/W2-R, 213x structural shortfall, not precision).
- **CLOSED**: Coulomb-gas multi-instanton at `n_I + n_{Ibar} <= 3` (W1-Q, 1.97x enhancement insufficient, 158x remaining shortfall).
- **CLOSED**: 't Hooft 6-fermion vertex modulus stabilization (W1-R, 12 OOM below threshold in target band; double-exponential structure guarantees irrelevance until too late).
- **CLOSED**: BCS-dressing-only modulus stabilization (W1-B sub-gate b, sign correct but monotonic; reinforces runaway since `Delta(tau)` decreases).
- **CLOSED**: GGE-relic-only modulus stabilization (W1-B sub-gate c, sign WRONG; spectral rescaling `g(tau)` monotonic reinforces runaway).
- **CLOSED**: `L_max <= 7` truncation-artifact hypothesis (W1-B sub-gate d; monotonicity persists from `L_max = 3` to `L_max = 7` with zero sign changes in `dS/dtau`).
- **CLOSED**: Local Jensen curvature rescue of global runaway (W2-L, `tau_local_crit = -0.887` outside physical regime).
- **CLOSED**: Fold-squeeze Bogoliubov backreaction as resolver of S70/S71 kappa inconsistency (W2-C, 0.49% effect; inconsistency reframed as W3-B definitional).
- **CLOSED**: Mott gap as DM candidate under any redshift scaling (W4-P, 11 OOM below Lyman-alpha bound in physical `a^{-1}` scaling, above Planck in `a^0`).
- **CLOSED** (reframed): S73B alpha_s = +0.833 tension (W1-A, machine-epsilon eliminated by multifield transfer; fiber-level non-monotonicity is projection-out at CMB scales).

**SURVIVING channels for substrate-internal modulus stabilization**:

1. **Multi-instanton condensate at `p + q >= 8` sectors** (UNCOMPUTED). `L_max <= 7` scan excluded higher spectral sectors; this is the one remaining lane in the dilute-gas expansion.
2. **Cross-spectral-moment back-reaction (a_2/a_4 sectors)** (UNCOMPUTED). `V_eff(tau)` here is built from `a_0` (pure cutoff) and the sqrt moment; `a_2` (Einstein-Hilbert) and `a_4` (Yang-Mills) may carry tau-dependence that modifies the total effective potential. Most promising channel, structurally decoupled from W1-B sub-gates.
3. **Fold-stiffness renormalization / exogenous fold-redshift** (UNCOMPUTED). If the S73B runaway position `tau = 1.614` is an artifact of fold dynamical stiffness (KE >> PE), a slower transit could relocate the post-fold state without needing a literal minimum. This is what W1-A already did for alpha_s: fiber-level extrapolation errors at CMB scales dissolved under proper projection.

**Remaining A_s gap**: After W1-A reduces the gap from +6.66 OOM to +5.83 OOM, the remaining 5.83 OOM must close through the BCS-dressing Coleman-Weinberg route (S66 `n_s = 0.9595`), dissipative effects (W3-E family), or cross-spectral-moment corrections. This is a known-direction problem; the `n_s = 1` exact-scale-invariance of the W1-A transfer function must be broken to produce the Planck red tilt.

**Open n_s puzzle**: The multifield delta-N transfer function is structurally scale-invariant because `H_cross^2 ~ (c_b k)^2` and `J_b^2 ~ 1/H_cross^2` cancel exactly -- the Sasaki-Stewart theorem for radiation-like H decay. To produce `n_s = 0.9649`, **at least one of**: (a) BCS dressing of the Coleman-Weinberg one-loop potential (S66 route), (b) intra-transit dispersive `r_b(k)` running beyond the flat-band approximation, or (c) non-power-law `H(tau)` decay (quasi-de Sitter phase before effacement). The S66 route is the sole surviving mechanism confirmed independently.

---

## V. Carry-Forward Computations

**Pre-registered gates for S75 (Hawking-program)**:

1. **H-75-1: CROSS-SPECTRAL-MOMENT-STABILIZATION-75** -- MEDIUM priority. Compute `d V_eff(a_2) / dtau` and `d V_eff(a_4) / dtau` at `tau = 0.48` from the `a_2 = R * Vol` (Einstein-Hilbert) and `a_4 = R^2/2 - |C|^2 + Yang-Mills` sectors, using the Chamseddine-Connes heat-kernel expansion beyond `a_0`. **PASS** if the combined cross-moment contribution at `tau = 0.48` is `>= 58,673 M_KK^4` and has sign that generates a minimum in `[0.45, 0.70]`. **INFO** if magnitude is 1-10% of bare but sign is correct. **FAIL** if magnitude `< 1%` of bare or wrong sign. This is the structurally most promising surviving channel.

2. **H-75-2: MULTI-INSTANTON-LMAX10-75** -- MEDIUM priority. Extend the W1-B sub-gate (d) scan to `L_max = 10` specifically to probe `(p + q) = 8, 9, 10` sectors. Cost estimate: 4-8 hours CPU on 50-point tau scan. **PASS** if `dS/dtau` sign changes appear at any `tau in [0.45, 0.70]` at `L_max in {8, 9, 10}`. **INFO** if sign changes appear outside the target band. **FAIL** if monotonicity persists at all tested L_max.

3. **H-75-3: FOLD-STIFFNESS-RENORMALIZATION-75** -- HIGH priority (structural). Derive whether the S73B `tau = 1.614` overshoot position is a kinematic artifact of the fold dynamical stiffness (KE/PE ratio) by computing the ATDHFB collective mass `M_ATDHFB(tau)` at `tau > 0.48` under GGE-relic back-reaction. **PASS** if the back-reacted `tau_overshoot` falls in `[0.45, 0.70]` without requiring a V_eff minimum. **INFO** if `tau_overshoot in [0.70, 1.2]`. **FAIL** if `tau_overshoot > 1.2` (runaway persists). This is W1-A's approach applied to the modulus trajectory itself.

4. **H-75-4: N_S-FROM-NON-POWER-LAW-H-75** -- HIGH priority. Compute `n_s` under a modified `H(tau)` profile with quasi-de Sitter phase before effacement. Non-power-law `H(tau)` would break the Sasaki-Stewart scale-invariance theorem and allow the transfer function to carry a red tilt. **PASS** if `n_s(k_pivot) in [0.9607, 0.9691]` (Planck 1-sigma). **INFO** if in `[0.94, 0.99]`. **FAIL** otherwise.

5. **H-75-5: ISLAND-SMALL-K-REFINEMENT-75** -- LOW priority. Investigate the 20% shape deviation at small k in W3-G by refining the subsystem-definition matching between the `CG(24)` graph bipartition and the 35-dim phase-space mode partition. Specifically, construct a consistent bijection between 24 graph vertices and the 35 bosonic moduli (respecting the `(35+, 0-, 0)` signature). This is bookkeeping; the physics at `k = N/2` is already exact.

6. **H-75-6: BDSPT-LMAX10-NON-PERTURBATIVE-75** -- LOW priority. Repeat W4-H at `L_max = 10` to verify the anomaly scales linearly with `n_modes` as predicted (projected `|Z_J/Z - 1| ~ 3e-10` at `L_max = 10`). This is a direct cross-check of the W4-H conclusion that the 5.8e-11 residual is eigenvalue-conjugation noise, not a genuine J-breaking term.

7. **H-75-7: ALPHA-A2-FROM-TRANSFER-75** -- MEDIUM priority. Combine the W1-A multifield transfer function with the S66 BCS-dressed Coleman-Weinberg route to compute a joint `(n_s, A_s)` prediction including both the substrate-internal red tilt mechanism and the multifield scale-transfer mechanism. **PASS** if `n_s in [0.9607, 0.9691]` AND `|log10(A_s/A_s^obs)| < 1.0`. This is the combined amplitude-normalization gate that the S66 H-66-1 pre-registered.

**What the S74 Hawking results enable for S75**:

- **Three-kappa decomposition** as a reference for all future horizon-physics computations. Any reference to "entry horizon surface gravity" must specify which projection is meant; the three distinct projections are now documented and cannot be conflated.
- **T_H = 72.838 M_KK** as the canonical entry-horizon Hawking temperature for all S75+ island, replica, Page-curve, and greybody computations.
- **Non-perturbative J-invariance** as the foundational protection layer for all S75+ BCS-subspace claims (DM stability, CPT protection, information containment).
- **Multifield transfer pipeline** (W1-A code) as the standard projection tool for any future fiber-to-CMB scale transfer computation; the S73B lesson is generalized.

**What remains blocked**:

- Substrate-internal modulus stabilization via perturbative or single-instanton channels: DEFINITIVELY CLOSED, no further tests needed in this lane.
- Fold-squeeze backreaction as resolver of kappa inconsistencies: CLOSED, reframed as definitional.
- The n_s red tilt via multifield transfer alone: BLOCKED by Sasaki-Stewart scale-invariance theorem. Must come from an additional mechanism.
- The 5.83 OOM A_s gap: partially addressed by W1-A's 0.83 OOM reduction; 5.0 OOM remain and require the S66 BCS-dressing + dissipative (S67 multifield-delta-N) route.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | W1-A TRANSFER-FUNCTION: `alpha_s = 8.4e-15`, `n_s = 1.000` | PHONONIC | INFO | S73B 125-sigma tension dissolved; fiber non-monotonicity projects out; red tilt requires separate mechanism |
| 2 | W1-B MODULI-STABILIZATION: 0/4 sub-gates produce V_eff minimum | GEOMETRIC | FAIL | Perturbative/single-instanton route closed; surviving channels are cross-moment and `L_max >= 10` |
| 3 | W1-Q COULOMB-GAS: 1.97x dilute enhancement, 159x remaining shortfall | GEOMETRIC | FAIL | Multi-instanton at `n <= 3` cannot rescue W1-B; shortfall is structural to `y(tau) = O(1)` |
| 4 | W1-R TH-OOFT-VERTEX: 2.55e-12 of bare gradient at `tau = 0.48` | GEOMETRIC | FAIL | 6-fermion vertex relevant only at `tau >= 1.53`, after runaway position -- permanent structural result |
| 5 | W2-C HFB-BACKREACTION: `delta_kappa = +0.49%` | PHONONIC | FAIL | S70/S71 kappa factor-173 is definitional, not physical -- resolved by W3-B |
| 6 | W2-L SELF-CONSISTENCY: `tau_local_crit = -0.887` | GEOMETRIC | FAIL | Local Jensen convexity cannot rescue global runaway; `k_local < |dV_bcs/dtau|/(tau width)` |
| 7 | W2-R INSTANTON-STAB: `dV_inst/dtau = -1.438 M_KK^4`, 213x short | GEOMETRIC | INFO | Analytic refinement confirms W1-B not a precision artifact; structural shortfall permanent |
| 8 | W3-B T-ENTRY-D_K: `T_H = 72.838 M_KK`, identity exact | PHONONIC | PASS | Self-consistent Hawking temperature of kinematic entry horizon; S71 `79,386` reframed as separate diagnostic |
| 9 | W3-E ENTRY-TH-DERIV: `T_spec = 0.0165 M_KK`, Mach 12.6 supersonic | GEOMETRIC | FAIL | Route-split discriminant: no horizon in structural c_spec projection; entry horizon is kinematic-only |
| 10 | W3-G ISLAND-LEFSCHETZ: max rel dev 20.8%, mean 14.6% | PHONONIC | INFO | Page curve shape recovered by one-time Gaussian saddle; 20% small-k deviation is bipartition geometry |
| 11 | W3-H S71-THREE-CELL-GSL: 3.81% variance, 1.92% delta_phi | PHONONIC | PASS | `R_spectral` graph invariant extrapolates S71 K_3 to full CG(24); W1-E Route 2 formula validated |
| 12 | W4-E MODULUS-DECAY: `T_rh = 1.37e+10 GeV` | PHONONIC | PASS | Reheating is spectral-weight cascade through instanton tunneling; 13 OOM above BBN floor |
| 13 | W4-H BDSPT-ANOMALY: `|Z_J/Z - 1| = 5.82e-11` | GEOMETRIC | PASS | Non-perturbative J-invariance lifts `[J, D_K] = 0` to full path integral; BCS subspace rigorously closed |
| 14 | W4-P MOTT-GAP-RENORM: `E_C_today = 1.04e-32 eV` | GEOMETRIC | PASS | Mott DM closed (11 OOM below Lyman-alpha); horizon-scale alignment `lambda/R_H = 0.14` is permanent prediction |
