# Session 83 Synthesis: Falsifier Campaign Inventory and Observational Roadmap Refresh

**Date**: 2026-04-18
**Agent**: mack-cosmic-bridge (Katie Mack, Cosmic Bridge) — part (a) of two-solo synthesis
**Source Documents**:
- `sessions/archive/session-83/session-83-results-workingpaper.md` (Level-6 §W3-G42..G52 and W3-G48..G49 bookkeeping)
- `computations/s83_gate_verdicts.txt` (S81+ canonical verdict lines, 62 gates)
- `sessions/evoi-framework.md` (S83 Stamp, 2026-04-18 refresh, post-S83 top-10)
- `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md` (historical trajectory S57 -> S83)

**Scope note**: This synthesis is the observational-roadmap half of the S83 two-solo pair. It maps the 11 Level-6 gates onto the 2026-2035 detector timeline, orders them by EVOI (reach date x posterior-update magnitude), and computes the DR3 decision tree for the G42 rectangle R = [-1.05, -0.85] x [-0.2, 0.2]. It does NOT re-adjudicate any gate — verdicts are authoritative from the source docs.

---

## I. Session Outcome

Level-6 delivered a structured falsifier inventory with sharply asymmetric observational-reach properties: four channels are decisive on the 2026-2032 roadmap (DR3 rectangle, 21cm alpha_f_NL at SKA-2, LiteBIRD n_T with extended mission, BICEP/Keck r reconfirmation), one channel is observationally sterile on the 2030-2040 roadmap (C_cons at CMB-S4 + LiteBIRD joint), and the rest are structural bookkeeping or scheme audits. The substrate-compaction w_0 = -0.918 prediction is tested live against DESI DR3 via G42 (PENDING-EVENT, framework point +0.032 inside the rectangle midpoint in w_0, exactly on the midpoint in w_a), with a closure protocol that hands the verdict off to a successor script at release. The single new adversity is G51: the canonical substrate-native regulator (Zubarev, selected by W1-G1) drives the Volovik-partition w_0 from -0.916 (zeta) to -0.998 (Zubarev), a 0.08 scheme-split that opens a structural tension in the w_0 mechanism stack independent of DR3 data.

---

## II. Key Results

### R1 — G42 DR3-LIVE-WATCH: Binary falsifier infrastructure with pre-registered containment rule

**Result**: PENDING-EVENT — framework point (w0_FW, wa_FW) = (-0.918, 0.0) strictly inside the pre-registered rectangle R = [-1.05, -0.85] x [-0.2, 0.2]. Offset from midpoint +0.032 in w_0, 0.000 in w_a. Half-widths in projected DR3 sigma: 2.174 in w_0, 1.130 in w_a. **Classification**: PHONONIC (framework prediction) / NON-PHONONIC (DR3 data).

The rectangle is the coarse binary projection of the S73-W4-C 7-scenario decision tree and the S60 three-scenario preregister. It is a pre-registered containment rule with a structural closure: a successor script invoked at the DR3 release pins the S83 artifact `s83_w3_g42_dr3_live_watch.npz` into its own closure hash so the verdict rule applied at release is traceable back to today's pre-registration unchanged. If DR3 publishes (w_0^DR3, w_a^DR3) inside R, PASS; outside, FAIL; if the release surface drifts to a bf-only format without public covariance, the rectangle containment remains the PRIMARY verdict rule (case (ii) in the saved cov_plan_json). The asymmetric half-widths (2.17 sigma in w_0 vs 1.13 sigma in w_a) reflect intentional sensitivity: w_a = 0 is the structurally sharp claim (four-fold locked on substrate-compaction per the S68 discovery) while w_0 has ~3% residual regulator-scheme dependence (see R9 below).

### R2 — G43 LITEBIRD n_T reach: 3-year INFO, crosses PASS at ~6.5 yr

**Result**: INFO — sigma(n_T)_3yr = 0.054005, PASS threshold 0.04, INFO band [0.04, 0.06]. **Classification**: PHONONIC (tensor BB observability on emergent g_M).

The Fisher forecast marginalizes (r, n_T) jointly against LiteBIRD 3-year combined sensitivity sigma_3yr = 2.16 mu-K-arcmin (PTEP 2023, 042F01 Table 3) at f_sky = 0.70, 50% delensing. Empirical scaling sigma(n_T) ~ t_obs^{-0.39} is shallower than the pure-noise 1/sqrt(t_obs) because sample-variance + lensing-residual contributions lift the denominator off the white-noise asymptote. Substitution chain for the crossover: sigma(n_T) = 0.054 at 3 yr; threshold 0.04; t_cross/3 = (0.054/0.04)^(1/0.39); t_cross = 6.48 yr (rounded 6.8 yr in the task prompt). LiteBIRD-alone cannot PASS on the nominal 3-year baseline; PASS requires either an extended mission >= ~7 yr, or a LiteBIRD + CMB-S4 joint analysis whose full-sky + delensing lever-arm tightens sigma(n_T) below 0.04. Note the asymptotic floor sits near sigma(n_T) ~ 0.015-0.020 (dominated by residual-lensing + sample variance at the recombination peak); a 100-year extrapolation gives sigma = 0.021.

### R3 — G44 C_cons at CMB-S4 + LiteBIRD: observationally sterile on 2030-2040 roadmap

**Result**: FAIL-detector — sigma(C_cons) = 0.2556 at CMB-S4 4-yr + LiteBIRD joint; PASS threshold 0.011 (23.2x above), INFO ceiling 0.02 (12.8x above); **0/80 configuration grid cells reach INFO** across t_int in {1,2,3,4,6} yr x N_f in {0.5,1,1.5,2} x f_sky in {0.25,0.40,0.55,0.70}. **Classification**: PHONONIC (framework prediction); detector reach is NON-PHONONIC.

Substitution chain: C_cons := r + 8 n_T; Jacobian J = (1, 8); sigma^2(C_cons) = sigma_r^2 + 64 sigma_nT^2 + 16 rho sigma_r sigma_nT. At the realized joint sigma_nT = 0.0322 the 8-factor in the Jacobian inflates sigma_nT by 23.4x before combining with sigma_r^2 (negligible at sigma_r = 0.0018). The 0.011 target requires sigma_nT <= 0.00137, which is ~23x below the current joint-Fisher floor and well below the residual-foreground-limited floor of sigma_nT ~ 0.015-0.020. Direction: no reachable (t_int, N_f, f_sky) configuration on the 2030-2040 roadmap crosses PASS. **This does NOT close the framework's C_cons prediction** (C_cons(k_transit) > 0.033 structurally survives per W-3 META-PRINCIPLE Observable 5) — it is a statement about detector reach, not framework correctness. EVOI for this channel drops to ~0 for the near-term window and the channel is effectively removed from the 2030-2040 falsifier catalog until a post-CMB-S4 space mission with foreground-cleaning breakthroughs appears.

### R4 — G45 21cm alpha_f_NL at SKA-2: PASS with 12.5x margin

**Result**: PASS — sigma(alpha_f_NL)_SKA2 = 0.800, PASS threshold 10 (12.5x under), SKA-1 phase-1 sigma = 5.118. **Classification**: PHONONIC (GGE bispectrum running probes fold-time dispersion).

The marginalized sigma(alpha)/sigma(f_NL) = 1/sqrt(<(ln k/k_*)^2>) is an instrument-independent geometric fact about Fisher information on a running parameter. SKA-2's extended k-range (0.02-10 Mpc^-1, 2.7 decades) gives <(ln k/k_*)^2> = 14.08, sigma(f_NL) = 3.0 (literature anchor, Munoz-Dvorkin-Cyr-Racine 2015 + Karagiannis 2018 equilateral vs local scaling), yielding sigma(alpha) = 0.80. SKA-1 gives 5.12. Direction: larger k-range -> larger Fisher variance in ln k -> smaller sigma(alpha). The framework's f_NL^total = 1.03 (S67) is marginally detectable at SKA-2 (SNR ~ 1.3 for f_NL_equil = 0.85); an alpha_f_NL in the O(0.1-1) range becomes 0.1-1.2 sigma, i.e., SKA-2 is the first instrument on the roadmap where alpha-type structure becomes a live discriminator. The SKA-1 sigma = 5.12 gives marginal PASS by the pre-registered 10 threshold but essentially no SNR against the framework's native O(1) alpha.

### R5 — G46 r(k_CMB) tensor transfer: PASS at 3.07x below BICEP/Keck 2021

**Result**: PASS — r(k_CMB) = 0.01173, BICEP/Keck 2021 95% CL r < 0.036, factor 3.077x under. **Classification**: PHONONIC (tensor-mode dispersion on emergent g_M).

The substrate-dispersion transfer relates r(k_transit) to r(k_CMB) through the eps_H(tau) flow across 54 decades of k (transit-to-CMB). Substitution chain (canonical-form slow-roll horizon-exit regime, both modes superhorizon through the transit): r(k) = 16 eps_H(t_k*) (c_S / c_T); c_T = 1, c_S = c_BLV = 0.485 (S67), so T^2 = eps_CMB/eps_transit = 0.0700; r(k_CMB) = 0.0700 x 0.168 = 0.0117. The S66 FAIL was a criterion mismatch (S66 tested blue-tilt preservation; G46 tests the BK18 r-bound) — the blue tilt IS structurally confined to the transit band k > 587 M_KK (see R7 below), and the CMB-scale r is the slow-roll horizon-exit value which is what BICEP/Keck measures. This is the cleanest zero-free-parameter prediction in the G42..G52 cluster: c_BLV and eps_H(0.05) were both substrate-geometry outputs of earlier sessions, not tuned to match r.

### R6 — G47 sin^2 theta_W: 0.064-sigma PASS (2-loop RGE + mu_BC = 188.44 GeV)

**Result**: PASS — sin^2(M_Z)_pred = 0.23121743, PDG = 0.23122, |dev|/sigma_PDG = 0.064, PDG sigma = 4e-5. **Classification**: PARTICLE (electroweak mixing angle under 2-loop RGE).

S82 W3-10 baseline (mu_BC = 2 M_Z = 182.38 GeV, 2-loop gauge only) gave 3.98 sigma INFO. S83 introduces a 3.32% mu_BC lift to the SM RGE brentq root mu_crit = 188.44 GeV (satisfying sin^2_SM(mu_crit) = 0.234803 cubic BC from tau_fold = 0.19 exactly) plus a 2-loop top-Yukawa correction. The improvement is dominated by the mu_BC lift (shift -1.59e-4 in sin^2(M_Z)); the Yukawa contributes an additional -2.68e-6, i.e., two orders smaller and essentially decorative on the PASS margin. Total gain over S82: 62.2x reduction in sigma-tension (1.8 OOM). The open item is whether 188.44 GeV has a geometric derivation. The most plausible candidate per the G47 self-assessment is mu_BC = M_Z + M_H_framework with M_H_framework ~ 97 GeV, giving 188.19 GeV (within 0.13%). This is NOT yet derived; it is a testable geometric hypothesis for S84.

### R7 — G50 n_T magnitude from Bogoliubov: PASS (|n_T| = 0.468 BLUE at transit)

**Result**: PASS — n_T = +0.4676 at tau_fold, sign definite across tau in [0.10, 0.30] (all-blue), magnitude threshold 0.033 satisfied at 14x margin. **Classification**: PHONONIC (dominant channel is Jensen-curvature / eps_H flow).

Channel decomposition: d ln eps_H / d tau = +10.286 (99.4%), d ln H^2 / d tau = +0.0595 (0.6%), d ln(1+2|beta|^2)^2 / d tau = 0.000 (squeeze channel is strictly k-independent in the linear-phonon regime). Multiplied by d tau / d ln k = +0.0452 at fold, n_T_full = +0.4676. The narrow reading of the task formula "n_T = 2 d ln|beta|^2 / d ln k" gives exactly zero — a structural null showing the framework's blue tilt does NOT originate from k-dependent squeezing but from eps_H flow across the van Hove fold. The transit-scale blue tilt is separated from CMB scales by ~54 decades of k (see R5); LiteBIRD cannot discriminate the tilt at CMB scales where n_T = -2 eps_H(tau_CMB) ~ -0.003 RED and 10^-4 from slow-roll consistency.

### R8 — G48 P_obs_aligned: 6/9 -> 7/9 (A_s INFO -> PASS via G10 co-PASS)

**Result**: PASS — P_obs_aligned = 7/9 = 0.7778, Delta = +1/9 = +0.1111 under S80-strict convention (PASS = 1, INFO = 0, FAIL = 0). Both conventions converge because n_INFO = 0 post-update. **Classification**: NON-PHONONIC (bookkeeping over verdict records).

The A_s channel re-classifies from INFO to PASS via the stack S82 W1-2 (PASS-F2 TD branch, 1.57-factor agreement with Planck 2.10e-9) plus S83 G1 IC-scheme-derivation PASS (Zubarev selected as substrate-native) plus S83 G10 A_s ledger meta co-PASS plus S83 G16 unified A_s = 5.08e-9 PASS (4/5 regulators). Only n_s, r, m_H, N_eff, w_0, f_NL, A_s are now PASS; sin^2 theta_W and alpha_s remain FAIL. Ceiling is 7/9 absent mechanism work — closing one FAIL brings 8/9, both 9/9.

### R9 — G51 w_0 regulator canonical choice: FAIL at 0.08 scheme-split

**Result**: FAIL — w_0(Zubarev, canonical R) = -0.998116, w_0(zeta, S58 baseline) = -0.916539, |w_0_canonical - (-0.918)| = 0.080116 > 0.05 INFO ceiling. **Classification**: PHONONIC (regulator acts on GGE mode density).

Under W1-G1 Connes-Moscovici + local-min-tau + KK-sign axioms, Zubarev regulator f_R(lambda) = exp(-lambda^2/M_KK^2) is uniquely selected as substrate-native. Applying Zubarev instead of zeta to the Volovik partition suppresses rho_GGE by a factor 51x (xi_E = 0.0196), driving the vacuum toward the R-independent Josephson kernel (w_J = -1). The substitution chain: rho_GGE_Zub = 0.0336, P_GGE_Zub = -0.0137, rho_J = 10.520, P_J = -10.520; w_0 = (-10.520 + (-0.0137))/(10.520 + 0.0336) = -0.9981. This is an OPEN TENSION with the canonical w_0 = -0.918 used in G42's rectangle containment: under the canonical regulator the framework prediction may actually be w_0 ~ -1 (LCDM-compatible, DESI-tension grows), NOT -0.918. The fix condition is whether rho_J is ALSO R-suppressed by Zubarev (in which case both sectors rescale proportionally and the -0.918 result may survive). That cross-check is NOT performed in S83 and is the highest-priority carry-forward. If rho_J is R-invariant as assumed, the framework's canonical w_0 prediction is -1 and the G42 rectangle containment test gets a different interpretation.

### R10 — G52 Channel-5 GW reclassified: falsifier -> CONSTRAINT-MAP WALL

**Result**: PASS — registry updated; Omega_GW(gamma) = 1.8e-59 at 1 mHz, 46.7 OOM below LISA canonical sensitivity, 39 OOM below any UHF GW roadmap proposal (levitated-sensor / CAST magnetic conversion at Omega ~ 1e-20). **Classification**: NON-PHONONIC (registry bookkeeping) with structural substrate physics underneath.

C5 cannot be falsified by any 2026-roadmap instrument in any band. Per the epistemic-discipline Evidence Hierarchy, a PASS verdict that (i) confirms a zero-parameter structural theorem (f^3 x T_rh^{13/3} scaling from Parker 1966 + T_rh scaling) and (ii) is not reachable by any roadmap instrument, functions as a Category 1 structural constraint (WALL), not a Category 2 falsifier. The relabel is the correct classification; the physics is unchanged.

### R11 — G49 EVOI watchlist refresh: DR3 promoted +2.00pp, top-10 reshuffled

**Result**: PASS (procedural) — 39-entry priority table rewritten into `sessions/evoi-framework.md` (S83 Stamp). **Classification**: NON-PHONONIC (priority bookkeeping).

Only material shift relevant to this synthesis: S78-W3-G DESI-DR3-UPDATE promoted from 8.20% to 10.20% EVOI (+2.00pp) to rank 9, because G42's rectangle is now pre-registered and the DR3 release is the EVOI-carrying event, not further internal computation. S78-W3-J SIN2-W-NON-TREE dropped -1.45pp (G47 passed geometrically but the channel still has a 4-sigma gap on the underived mu_BC side; P(pass) on channel-close went down even though P(pass) on geometric-reading went up, because that went banked). S78-W3-C TENSOR-FAMP dropped -1.05pp (G46 directly realized a chunk of the |delta_P(pass)|). See Section VI for the EVOI-ordered observational priority.

---

## III. Gate Verdicts (Level-6 observational cluster)

| Gate | Verdict | Decisive Number | Source Script |
|:-----|:--------|:----------------|:--------------|
| S83-DR3-LIVE-WATCH (G42) | PENDING-EVENT | Framework (w_0, w_a) = (-0.918, 0.0) inside R; |offset_w0| = 0.032 from midpoint | s83_w3_g42_dr3_live_watch.py |
| S83-LITEBIRD-SIGMA-N_T-REACH (G43) | INFO | sigma(n_T)_3yr = 0.054005 (in [0.04, 0.06]) | s83_w3_g43_litebird_sigma_nT_reach.py |
| S83-CMB-S4-SIGMA-C-CONS-SENSITIVITY (G44) | FAIL-detector | sigma(C_cons)_joint = 0.2556 (23.2x above 0.011 PASS) | s83_w3_g44_cmb_s4_ccons.py |
| S83-21-CM-SIGMA-ALPHA-F-NL-REACH (G45) | PASS | sigma(alpha_f_NL)_SKA2 = 0.800 (12.5x under 10) | s83_w3_g45_ska_alpha_fnl.py |
| S83-TENSOR-TRANSFER-K-TRANSIT-TO-K-CMB (G46) | PASS | r(k_CMB) = 0.01173 (3.077x under 0.036) | s83_w3_g46_tensor_transfer_k_transit_cmb.py |
| S83-SIN2-THETA-W-2-LOOP-PLUS-MU-BC (G47) | PASS | |dev|/sigma_PDG = 0.064 (62.2x improvement over S82) | s83_w3_g47_sin2_thetaW_2loop_mu_BC.py |
| S83-P-OBS-ALIGNED-UPDATE-LOGIC (G48) | PASS | 7/9 = 0.7778 (+0.1111 from S80 baseline) | s83_w3_g48_p_obs_aligned.py |
| S83-EVOI-WATCHLIST-REFRESH (G49) | PASS | DR3 promoted +2.00pp to rank 9 | s83_w3_g49_evoi_refresh.py |
| S83-N_T-MAGNITUDE-FROM-BOGOLIUBOV (G50) | PASS | n_T = +0.4676 BLUE, sign stable tau in [0.10, 0.30] | s83_w3_g50_nT_bogoliubov.py |
| S83-W_0-REGULATOR-CANONICAL-CHOICE (G51) | FAIL | Zubarev w_0 = -0.998116, split 0.080 vs -0.918 | s83_w3_g51_w0_regulator.py |
| S83-CHANNEL-5-RELABEL (G52) | PASS | OOM ratio = 29.63, gamma 46.7 OOM below LISA | s83_w3_g52_channel5_relabel.py |

---

## IV. Structural Implications

### IV.1 — Observational-reach asymmetry is sharp

The Level-6 cluster exhibits an asymmetric three-way structure that was not obvious before the gates landed:
- **Decisive 2026-2032**: G42 (DR3 rectangle, event-driven), G46 (BICEP/Keck Array 2026 reconfirmation). Both are binary/pre-registered.
- **Decisive 2030-2035**: G43 (LiteBIRD at extended mission ~7 yr), G45 (21cm alpha_f_NL at SKA-2 phase-2 full survey).
- **Sterile 2030-2040**: G44 (C_cons channel; sigma(n_T) requires ~23x reduction beyond CMB-S4 + LiteBIRD joint Fisher floor).

This partitions the 11 Level-6 gates into "observational" (5 decisive channels + 1 sterile + 1 retired-to-WALL) and "bookkeeping" (G47, G48, G49, G50, G51). Observational priority for the 2026-2035 window is now sharp: DR3 first, r-reconfirmation second, SKA-2 alpha third, LiteBIRD extended fourth, everything else structural.

### IV.2 — Dual vulnerability on w_0

The G42 rectangle is pre-registered against w_0 = -0.918 (zeta, S58/S59 baseline). But G51 shows that under the canonical substrate-native regulator (Zubarev, W1-G1 PASS), the Volovik-partition w_0 is -0.998 — 0.08 further from the DESI DR2 central -0.752 than the baseline. There are three possible resolutions:
(i) rho_J IS also R-suppressed by Zubarev; both sectors rescale proportionally; -0.918 survives the regulator canonicalization. **Cross-check required — not yet performed.**
(ii) rho_J is truly R-invariant (topological CPT, per S58 claim verified at explicit-dressing level); canonical prediction is w_0 ~ -1 (LCDM-compatible); DESI-tension grows; G42 rectangle contains the Zubarev reading w_0 = -0.998 but ASYMMETRICALLY. Substitution chain for the asymmetric margins (Python-verified):
- Def: dist_lower := |w_0 - (-1.05)|; dist_upper := |w_0 - (-0.85)|; binding-margin := min(dist_lower, dist_upper)
- Sub (zeta): w_0 = -0.916539 -> dist_lower = 0.1335, dist_upper = 0.0665; binding-margin = 0.0665 (UPPER edge)
- Sub (Zubarev): w_0 = -0.998116 -> dist_lower = 0.0519, dist_upper = 0.1481; binding-margin = 0.0519 (LOWER edge)
- Simp: ratio = 0.0665 / 0.0519 = 1.28x
- Direction: Zubarev binds tighter than zeta by 1.28x, AND the binding edge FLIPS from upper (zeta, so sensitive to DR3 centrals near -0.85) to lower (Zubarev, so sensitive to DR3 centrals near -1.05).

**Rectangle-containment PASS is robust under (ii), but the binding edge shifts from upper (zeta) to lower (Zubarev).** A DR3 central near -1.0 (e.g., Planck-compatible w ~ -1.03) is compatible with EITHER zeta (distance 0.114 from -0.92, safely inside R; Zubarev distance 0.002, at edge). A DR3 central near -0.92 is compatible with zeta (distance 0.004) but Zubarev is distance 0.08 from -0.92, safely inside but asymmetric. The cleanest discriminating DR3 centrals are at the two edges of R: w_0 near -0.85 favors zeta reading; w_0 near -1.05 favors Zubarev reading. **G42 becomes a partial scheme-discriminator under (ii), not purely a framework-tester.**
(iii) The -0.918 was an artifact of the bare scheme; the framework's canonical prediction is -1.

Until the rho_J R-dependence cross-check is done (carry-forward V.1), G42's post-release interpretation is scheme-dependent. The rectangle containment binary still fires correctly; the mechanistic reading shifts.

### IV.3 — The transit-scale blue tilt is observationally inaccessible (closed structural result)

G50 establishes |n_T| = +0.4676 BLUE at the transit scale with sign definite across the full [0.10, 0.30] tau window. G46 establishes that at CMB scales 54 decades of k away, n_T = -2 eps_H(tau_CMB) ~ -0.003 RED with a framework-vs-slow-roll split of 10^-4. G43 establishes that the realistic LiteBIRD sigma(n_T) is two OOM larger than this split. **Cumulative conclusion: any LiteBIRD tensor detection at the expected r ~ 0.024 will confirm the r-amplitude but provide no tilt-based discrimination between the framework and standard slow-roll.** The blue transit-scale tilt is a structural fact about the framework; it is not a near-term observational handle. I recommend formally closing this as a permanent structural result in the registry (V.3 below).

### IV.4 — Level-6 does not close any framework mechanism; it re-classifies the observational surface

None of G42-G52 close a mechanism. G42 sets up a live falsifier. G43-G45 map detector reach. G46 closes an S66 interpretation ambiguity in the framework's favor. G47 brings sin^2 theta_W into P_obs_aligned (PASS, but mu_BC still underived). G48-G49 bookkeeping. G50 verifies + restates an S65 result. G51 opens a new tension. G52 retires a channel from the falsifier list to the WALL registry. **The Level-6 contribution is MAP-making, not closure**: the 2026-2035 roadmap is now concretely specified with pre-registered verdict rules at each instrument milestone.

### IV.5 — EVOI ordering per channel (post-S83)

Priority for next-session observational work, by EVOI (P(pass) x |delta_P(pass)| + P(fail) x |delta_P(fail)|), restricted to Level-6-related items:

| Rank (relevant) | Item | EVOI | Trigger Event / Date |
|:--|:--|:--|:--|
| 9 | S78-W3-G DESI-DR3-UPDATE (G42) | 10.20% | DR3 release (projected 2026-2028) |
| 22 | S78-W3-J SIN2-W-NON-TREE (G47 follow-up) | 5.75% | mu_BC geometric derivation (S84+) |
| 27 | S78-W3-C TENSOR-FAMP (G46 follow-up) | 4.50% | r(k_CMB) reconfirm at LiteBIRD |

The DR3 event is the dominant near-term observational EVOI node.

---

## V. Carry-Forward Computations

V.1. **RHO-J-R-INVARIANCE-84**
   - **What**: Recompute rho_J = F_Josephson / N_cells under Zubarev regulator dressing (vs the S58 claim of R-independence by topological CPT). If rho_J_Zub / rho_J_zeta differs from rho_GGE_Zub / rho_GGE_zeta, the Volovik-partition w_0 is scheme-variant; if they differ by the same 51x suppression factor, -0.918 survives regulator canonicalization. Equation: w_0(R) = (P_J(R) + P_GGE(R)) / (rho_J(R) + rho_GGE(R)); test whether numerator and denominator rescale proportionally.
   - **Inputs**: `canonical_constants.py` (F_Josephson, N_cells, M_KK, Vol_SU3, tau_fold); `s83_w3_g51_w0_regulator.npz` (zeta and Zubarev S sums + GGE contributions at L_max=5); L_max in {5, 7, 9} cross-scheme scan.
   - **Gate**: NEW S84 gate RHO-J-R-INVARIANCE-84. PASS: |w_0(Zubarev) - (-0.918)| < 0.02 after R-consistent treatment of rho_J. INFO: in (0.02, 0.05). FAIL: >= 0.05 (canonical prediction is genuinely w_0 ~ -1). Feeds G42's post-DR3-release interpretation.
   - **Effort**: 4-6 hours, 1 agent session (compute-mode). Re-uses s83_w3_g51 machinery; adds explicit Zubarev dressing of the Josephson sector.

V.2. **G42-DR3-RELEASE-VERDICT**
   - **What**: Event-driven. When DESI DR3 central (w_0^DR3, w_a^DR3) publishes, invoke the successor script pinned to `s83_w3_g42_dr3_live_watch.npz`. Compute verdict_rule(w_0^DR3, w_a^DR3) and append the verdict line. If public covariance released, also compute chi^2 = delta @ cov_inv @ delta.T as ancillary OOM vs LCDM/Quintom candidates.
   - **Inputs**: `desi_dr3_w0wa_bf.json` (central values), optional `desi_dr3_w0wa_cov.json` (2x2 CPL covariance); polling directory `computations/desi_dr3_release/`.
   - **Gate**: S83-DR3-LIVE-WATCH successor verdict (PENDING-EVENT -> PASS|FAIL). The rectangle [-1.05, -0.85] x [-0.2, 0.2] is frozen; no re-registration at release.
   - **Effort**: <1 hour once data lands; infrastructure already in place.

V.3. **BLUE-TRANSIT-TILT-INACCESSIBILITY-84**
   - **What**: Formally close "LiteBIRD cannot discriminate framework from slow-roll on n_T" as a permanent structural result in the registry. Derivation: transit-scale blue tilt (G50: n_T = +0.468) lives at k > k_transit ~ 587 M_KK; CMB scales are 54 decades of k away (G46); framework-vs-slow-roll Delta(n_T) at CMB scales ~ 10^-4 (S68 LITEB-R-FORECAST-68); realistic LiteBIRD sigma(n_T) ~ 0.05-0.15 (G43) >> Delta(n_T)_CMB.
   - **Inputs**: `s65_blue_tensor_tilt.npz`, `s66_tensor_transfer.npz`, `s68_liteb_r_forecast.npz`, `s83_w3_g43_litebird_sigma_nT_reach.npz`, `s83_w3_g46_tensor_transfer.npz`, `s83_w3_g50_nT_bogoliubov.npz`.
   - **Gate**: NEW S84 gate BLUE-TRANSIT-TILT-INACCESSIBILITY-84. PASS: registry updated with permanent-structural-result tag; EVOI for "LiteBIRD n_T-tilt discrimination" set to 0 for the 2030-2040 window. Bookkeeping gate.
   - **Effort**: 1-2 hours (bookkeeping + constraint-map entry).

V.4. **LB-CMBS4-JOINT-SIGMA-NT-84**
   - **What**: Extend the G43 Fisher matrix to a 3-parameter joint (r, n_T, Alens) likelihood combining LiteBIRD B-modes + CMB-S4 delensing to quantify how much sigma(n_T) tightens beyond the LiteBIRD-alone 0.054 at 3 yr. Target: does the combined lever-arm cross the 0.04 PASS threshold at 3-yr LiteBIRD + full-survey S4?
   - **Inputs**: LiteBIRD noise spec (sigma_3yr = 2.16 mu-K-arcmin, f_sky = 0.70, 50% delensing), CMB-S4 noise spec (1.0 mu-K-arcmin, 30-arcmin beam, f_sky = 0.40, 90% delensing), framework fid (r, n_T) = (0.0242, -0.003024); independent-experiment Fisher sum.
   - **Gate**: NEW S84 gate LB-CMBS4-JOINT-SIGMA-NT-84. PASS: sigma(n_T)_joint_3yr <= 0.04. INFO: <= 0.06. FAIL: > 0.06.
   - **Effort**: 3-4 hours, 1 agent session. Adapts G43 script.

V.5. **MU-BC-GEOMETRIC-DERIVATION-84**
   - **What**: Test whether mu_BC = 188.44 GeV derives geometrically from the framework. Candidate H1: mu_BC = M_Z + M_H_framework with M_H_framework ~ 97 GeV (tree-level prior to KK threshold corrections; see S63/S66 m_H channel decomposition). Compute M_H_framework from a_6/a_4 at L_max=5,7 without the RGE running and check the sum against 188.44 GeV.
   - **Inputs**: `canonical_constants.py` (M_Z, a_6/a_4 at tau_fold), `s66_mack_qa_workshop` / `s73b_mack_vdd_workshop` m_H history, L_max in {5, 7, 9} ladder.
   - **Gate**: NEW S84 gate MU-BC-GEOMETRIC-DERIVATION-84. PASS: |mu_BC_geometric - 188.44 GeV| < 0.25 GeV (0.13% match anchor). INFO: < 2 GeV. FAIL: >= 2 GeV.
   - **Effort**: 4-5 hours, 1 agent session.

V.6. **ALPHA-F-NL-FRAMEWORK-PRED-84**
   - **What**: First-principles framework prediction for alpha_f_NL (running of the equilateral f_NL). The G45 PASS sets sigma(alpha) = 0.80 at SKA-2; the framework's native alpha comes from the acoustic-optical branch crossing at M_KK and the BCS gap broadening across the transit (S63, S65, S78). Compute d f_NL / d ln k at k_pivot from GGE bispectrum machinery + fold-time dispersion.
   - **Inputs**: `s67_gge_bispectrum.npz`, S63 RUNNING-NS machinery, S78 FNL-COHERENCE template, transit Bogoliubov amplitude k-dependence.
   - **Gate**: NEW S84 gate ALPHA-F-NL-FRAMEWORK-PRED-84. PASS: alpha_f_NL_framework derived with < 20% uncertainty and |alpha| > sigma(alpha)_SKA2 = 0.8 (detectable at SKA-2). INFO: |alpha| in (0.3, 0.8) (marginal). FAIL: |alpha| < 0.3 (invisible at SKA-2 even with tightest Fisher).
   - **Effort**: 8-10 hours, 1-2 agent sessions. Foundational computation.

V.7. **BICEP-KECK-ARRAY-2026-RECONFIRM-PRE-REGISTER**
   - **What**: Pre-register G46's r(k_CMB) = 0.0117 as a testable prediction against the 2026 BICEP/Keck Array data release (expected to tighten r < 0.036 -> r < 0.02-0.025). Document the decision tree: if r < 0.020 at BK-Array 2026 tight bound, framework consistent; if r > 0.025 upper bound, framework disfavored at 2-3 sigma; if r ~ 0.012 +/- 0.003 positive detection, +3-sigma framework confirmation.
   - **Inputs**: G46 prediction r = 0.01173 (pinned), canonical BK-Array 2026 forecast (Ade et al. 2025 preprint literature sigma_r ~ 0.005).
   - **Gate**: Pre-registration document. Procedural. PASS: decision tree written with scheme tags. FAIL: not written.
   - **Effort**: 1-2 hours.

V.8. **DR3-CONTINGENCY-FINE-GRAINED**
   - **What**: At DR3 release, if w_0^DR3 or w_a^DR3 falls OUTSIDE the G42 rectangle, invoke the S73 W4-C fine-grained 7-scenario decision tree to distinguish sub-scenarios B1, B2, B3 (differ on which CPL-template parameter drives the exclusion). Compute per-sub-scenario framework interpretation.
   - **Inputs**: `s73_w4_c_dr3_prep.npz` (7-scenario decision tree, frozen 2026-04-10), `s83_w3_g42_dr3_live_watch.npz`.
   - **Gate**: Conditional on V.2 FAIL. If G42 fires FAIL, this gate classifies the sub-scenario. No PASS/FAIL at S83; activated by V.2 outcome.
   - **Effort**: 2-3 hours post-release.

V.9. **G47-YUKAWA-REGIME-TIGHTENING**
   - **What**: The CHK3 pre-registration in G47 predicted Yukawa shift O(10^-4); actual shift is O(10^-6) — two OOM overestimate due to log-arm length 0.73 (not 1 decade) and (C_1 - C_2) partial cancellation. Refine the OOM estimator for future 2-loop + Yukawa-threshold gates so pre-registered thresholds are not over-generous.
   - **Inputs**: `s83_w3_g47` script; analytic 2-loop SM RGE Yukawa contribution formula.
   - **Gate**: Meta-methodological. NEW S84 gate YUKAWA-OOM-ESTIMATOR-84. PASS: documented formula reproduces actual shift within 30% across at least 3 test cases. INFO: reproduces within 3x. FAIL: off by factor 10.
   - **Effort**: 2-3 hours.

V.10. **SKA-1-PHASE-1-ALPHA-FRAMEWORK-SNR**
   - **What**: Before SKA-2 is operational (2030-2035), estimate the SKA-1 Phase-1 SNR (sigma(alpha) = 5.12, G45) against the framework-native alpha (V.6 output). If framework alpha > 2-3 sigma at SKA-1, there's a mid-2020s-2030s discriminator; if not, SKA-2 is the sole channel.
   - **Inputs**: V.6 framework alpha prediction; G45 sigma(alpha)_SKA1 = 5.118; SKA-1 commissioning timeline (2027-2029).
   - **Gate**: DEPENDS ON V.6. Pre-register: SKA-1 SNR = |alpha_framework| / 5.118. PASS: SNR >= 2. INFO: 1-2. FAIL: < 1.
   - **Effort**: 1 hour (depends on V.6).

V.11. **G51-RHO-J-CROSS-CHECK-AT-L-MAX-7**
   - **What**: Independent of V.1, also test G51 at L_max = 7 and 9 to verify the scheme-split is not an L_max = 5 truncation artifact. If scheme-split grows with L_max, the canonicalization tension is real; if it shrinks, the -0.918 baseline may converge.
   - **Inputs**: zeta and Zubarev S sums at L_max in {5, 7, 9}; canonical eigenvalue spectrum of D_K.
   - **Gate**: NEW S84 gate G51-LMAX-CONVERGENCE-84. PASS: |w_0(Zubarev, L=9) - w_0(Zubarev, L=5)| < 0.005 AND converged value reaches -0.918 +/- 0.02. INFO: converged but outside band. FAIL: does not converge.
   - **Effort**: 6-8 hours (L=9 eigenvalue count ~ 1e6).

V.12. **P-OBS-ALIGNED-CEILING-CLOSURE**
   - **What**: Elevate sin^2 theta_W from FAIL to PASS requires mu_BC geometric derivation (V.5); elevate alpha_s requires multifield-transfer-function resolution (N1 TRANSFER-FUNCTION-74, EVOI rank 1). Document the explicit ceiling-lifting chain so the P_obs_aligned 7/9 -> 8/9 -> 9/9 transitions are pre-registered.
   - **Inputs**: G48 output, N1 and V.5 gate specs.
   - **Gate**: NEW S84 gate P-OBS-ALIGNED-CEILING-84. PASS: ceiling-lifting chain documented with dependency graph. Procedural.
   - **Effort**: 1 hour.

---

## VI. Summary Table — Observational Roadmap by EVOI

**EVOI ordering = reach-date x posterior-update magnitude.** Row order below is the decision-relevance ranking for the 2026-2035 observational window.

| # | Channel | Gate (S83) | Verdict | Reach Date | Detector | Statistical Power | Framework Prediction | EVOI Magnitude | Classification |
|:--|:--------|:-----------|:--------|:-----------|:---------|:------------------|:---------------------|:---------------|:---------------|
| 1 | DR3 rectangle | G42 | PENDING-EVENT | 2026-2028 | DESI (Stage IV) | 2.17 sigma (w_0) + 1.13 sigma (w_a) half-widths | (-0.918, 0.0) inside R; PASS iff DR3 central in R | EVOI_rank=9 post-refresh, event-driven +2.00pp | PHONONIC/NON-PHONONIC |
| 2 | r reconfirm | G46 | PASS | 2026 | BICEP/Keck Array 2026 | sigma_r ~ 0.005 | r(k_CMB) = 0.0117 (3.07x under BK18 0.036) | High (posterior update if r > 0.025 disfavors) | PHONONIC |
| 3 | 21cm alpha_f_NL | G45 | PASS (reach) | 2032-2035 | SKA phase-2 full survey | sigma(alpha) = 0.80 (12.5x under 10) | f_NL^total = 1.03; alpha_framework TBD (V.6) | High (sole near-term test of fold-time dispersion) | PHONONIC |
| 4 | LiteBIRD n_T extended | G43 | INFO | ~2030-2032 + extended | LiteBIRD 3yr + extended mission ~7 yr | sigma(n_T)_3yr = 0.054 -> 0.04 at 6.5 yr | CMB-scale n_T ~ -0.003 RED (not discriminable from slow-roll) | Medium (V.3 bookkeeping) | PHONONIC |
| 5 | LiteBIRD + S4 joint | V.4 | NEW S84 | 2030 | LB + CMB-S4 joint Fisher | 3x3 Fisher, sigma(n_T)_joint TBD | Testable at joint reach | Medium | PHONONIC |
| 6 | DR3 fine-grained | V.8 | Conditional | 2026-2028 | DESI sub-scenario decision tree | 7-scenario tree (S73 W4-C) | Branch identification post-G42 FAIL | Conditional on V.2 outcome | PHONONIC |
| 7 | sin^2 theta_W mu_BC geometric | G47 + V.5 | PASS (S83) / TBD (S84) | 2025 (PDG) | PDG precision 4e-5 | 62.2x improvement S82 -> S83 | sin^2 = 0.23122 at mu_BC = 188.44 GeV (underived) | EVOI_rank=22, -1.45pp post-refresh | PARTICLE |
| 8 | C_cons at CMB-S4 | G44 | FAIL-detector | 2030-2040 | CMB-S4 + LiteBIRD joint | sigma(C_cons) = 0.2556 (23x above PASS) | C_cons > 0.033 (structurally survives but undetectable) | 0 near-term (retired to long-term structural) | PHONONIC (framework) / NON-PHONONIC (reach) |
| 9 | n_T magnitude at transit | G50 | PASS | N/A (transit-scale; observationally inaccessible) | None within 34 decades | n_T = +0.4676 BLUE, sign stable [0.10, 0.30] | 0 near-term (V.3 permanent structural) | PHONONIC |
| 10 | P_obs_aligned | G48 + V.12 | PASS | N/A (bookkeeping) | N/A | 7/9 = 0.7778; ceiling 7/9 absent mechanism work | Bookkeeping | NON-PHONONIC |
| 11 | Channel-5 GW (gamma route) | G52 | PASS-WALL | 2040+ (no roadmap reach) | LISA + UHF roadmap | 46.7 OOM below LISA; 39 OOM below UHF best | WALL (structural, retired from falsifier list) | 0 | NON-PHONONIC registry |

**Decision timeline (compressed)**:
- **2026**: BICEP/Keck Array r-reconfirmation (G46 test; V.7 pre-register).
- **2026-2028**: DESI DR3 release (G42 rectangle fires binary PASS/FAIL; V.2 succession activates).
- **2030-2032**: CMB-S4 full survey + LiteBIRD 3-yr nominal (G43 INFO at nominal, G44 FAIL-detector on C_cons; V.4 joint Fisher test).
- **~2032-2035**: LiteBIRD extended mission reaches sigma(n_T) = 0.04 at ~6.5 yr (G43 PASS condition).
- **2032-2035**: SKA Phase-2 full survey (G45 PASS framework-vs-LCDM alpha_f_NL discrimination; V.6 framework alpha prediction required).

**DR3 decision tree (G42 rectangle at release)**:

| DR3 central (w_0, w_a) location | G42 verdict | Sub-scenario interpretation (S73 W4-C fine-grained) | V.2 successor action |
|:--------------------------------|:------------|:----------------------------------------------------|:---------------------|
| Inside R: (w_0, w_a) in ([-1.05, -0.85], [-0.2, 0.2]) | PASS | Sc.A-like (null or hardening) | Append PASS line + update P_obs_aligned delta |
| w_0 outside [-1.05, -0.85], w_a inside | FAIL | Sub-B2 (w_0 quench-dominated) | Invoke V.8 + re-examine Volovik partition R-consistency (V.1) |
| w_0 inside, w_a outside [-0.2, 0.2] | FAIL | Sub-B1 or B3 (w_a phantom-like, Scenario B) | Invoke V.8; four-fold w_a lock challenged |
| Both outside | FAIL (strong) | Beyond S73 decision tree; new mechanism required | Re-examine Volovik partition from scratch |
| bf-only release (no covariance) | Rectangle rule only | Ancillary chi^2 unavailable | Verdict via verdict_rule() only |
| Public covariance | Rectangle rule + chi^2 vs LCDM/Quintom | OOM comparison as ancillary context | Verdict + chi^2 diagnostic |

**Dual vulnerability note (IV.2)**: Under G51 (canonical regulator = Zubarev), the Volovik-partition w_0 is -0.998, inside R with binding-margin 0.0519 to the LOWER edge (vs zeta's binding-margin 0.0665 to the UPPER edge; ratio 1.28x). V.1 (rho_J R-invariance cross-check) is the prerequisite for interpreting a post-DR3 G42 PASS: with V.1 resolved, the rectangle is a framework test; without V.1, it is partially a scheme-discriminator whose sharpness depends on which rectangle edge DR3 lands near.

---

**Substitution chains used in this synthesis** (math-is-hard compliance):

1. *DR3 rectangle half-widths in projected sigma.* Def: sigma-reach := half-width / sigma_proj. Sub: 0.10 / 0.046 (w_0); 0.20 / 0.177 (w_a). Simp: 2.174 ; 1.130. Direction: larger ratio = broader tolerance, higher PASS probability at fixed central-value scatter. (Source: G42 self-assessment Step 4; Python-verified.)

2. *LiteBIRD t_cross from empirical scaling.* Def: sigma(n_T)_t = sigma_3yr x (t/3)^{-0.39}. Sub: 0.04 = 0.054 x (t_cross/3)^{-0.39}. Simp: t_cross = 3 x (0.054/0.04)^{1/0.39} = 3 x 1.35^{2.564} = 6.48 yr. Direction: monotonic decrease of sigma with t, exponent 0.39 < 0.5 (sample-variance inflated). (Python-verified.)

3. *C_cons detector sterility.* Def: sigma^2(C_cons) = sigma_r^2 + 64 sigma_nT^2 + 16 rho sigma_r sigma_nT. Sub: sigma_nT required for sigma(C_cons) = 0.011 at sigma_r ~ 0.0018 is sigma_nT_req ~ 0.011/8 = 0.001375. Simp: reduction = 0.0322 / 0.001375 = 23.4x. Direction: joint-Fisher floor of sigma_nT ~ 0.032 is 23x above the floor needed for PASS; no (t_int, f_sky, N_f) configuration reaches PASS -> sterile. (Python-verified.)

4. *w_0 scheme-split (G51 FAIL).* Def: |w_0(canonical R) - w0_FW| compared to PASS threshold 0.02, INFO threshold 0.05. Sub: |-0.998116 - (-0.918)| = 0.080116. Simp: 0.08 > 0.05 > 0.02 -> FAIL. Direction: Zubarev UV-suppresses GGE (xi_E = 0.0196) -> vacuum dominated by R-invariant Josephson -> w_0 -> w_J = -1 monotonically as UV suppression tightens. (Source: G51 Step 4; Python-verified.)

5. *sin^2 theta_W improvement factor.* Def: n_sigma = |sin^2_pred - PDG| / sigma_PDG, sigma_PDG = 4e-5. Sub: n_sigma_S82 = 3.98; n_sigma_S83 = 0.064. Simp: improvement = 3.98 / 0.064 = 62.2x. Direction: mu_BC lift 2M_Z -> 188.44 GeV drops |sin^2_pred - PDG| from 1.59e-4 to 2.57e-6. (Python-verified.)
