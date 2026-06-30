### 11.2 Cosmological Constant from `a_0`

`Λ_CC ∝ f_0 · a_0 · M_KK⁴`. The key distinction from vacuum-energy-cutoff calculations: `a_0` is a spectral moment integrated against the `x⁰ = 1` weight, which includes ALL modes, including the ones that are spectrally suppressed. The Volovik-vS entropy identification (Paper 41 in the Tesla library) shows that the CC is the zeroth moment of `Tr f(D²/Λ²)`, and it is algebraically distinct from `a_2` (gravity) and `a_4` (Yang-Mills). The framework's CC computation through the chi_2 × HP4 route gives `0.337 · ρ_obs` (S75 W4-C, sole L_max-robust route) — within a factor 3 of observed. The factor 3 residual is pre-registered as the remaining theoretical deficit; every known mechanism for canceling vacuum energy has been tested and all fail for structural reasons (S66 CC reframe, S74 Friedmann wrong-question theorem).

The CC is not small because fine-tuning; it is small because it is a different integration than vacuum energy, and the integration is dominated by the high-k spectral tail suppressed by the sqrt(x) cutoff.


#### 11.2.A Regulator-stratification: The Three-Layer Theorem (§VII.N, S84 W2a-11)

The CC-from-`a_0` computation is a spectral-functional evaluation, and it inherits
the three-layer regulator stratification proven in S84 W2a-11 and landed as
registry §VII.N (Connes + Lizzi + Van den Dungen three-solo convergence):

- **L1 (axiomatic, global)**: the canonical measure on the substrate's operator
  spectrum is the Dixmier trace / zeta-residue form, `Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s})`
  (Connes-Marcolli 2008 Thm 1.31). Unique regulator at L1: **zeta**.
- **L2 (substrate-action, at τ_fold)**: three-criterion intersection (integrability,
  `d²S/dτ² > 0` at fold, chirality χ = +1) selects **Zubarev** at τ = 0.19,
  L_max = 5.
- **L3 (observable, per-Q)**: 5-regulator span partitions into R-protected
  `[1.0, 1.5]` / NOT-R-protected `[2.5, ∞)`. Gap `[1.5, 2.5]` empty. CC-5
  propagation `span(O) = ∏_i span(F_i)^|p_i|` applies ONLY at L3.

**Consequence for CC**: `Λ_CC` is an L3 observable (regulator-dependent span per
§VII.K-DUAL atlas; the `0.337 ρ_obs` value above is at Zubarev/L2, L_max = 5).
The factor-3 residual is the per-observable span bracket, not a fundamental
discrepancy — L1 and L2 are already canonicalized, L3 residue is pre-registered.

#### 11.2.B Corridor separability: Disjoint-Corridor (§VII.P pending, W2-7 FAIL-with-refinement)

S84 S-5 Connes synthesis proposed §VII.P: HP⁰ ∩ HP¹ = {0} for (A_F, H_F, D_F),
with secondary class ε_H explicitly living in HP¹. This separability was
further proposed to imply spectral-functional distinguishability across
HP²-disjoint corridor pairs in the (a_0, a_2, a_4) Seeley-DeWitt coefficients.

**Status (S85 W2-7, 2026-04-23, this session)**: Counter-construction audit
**FAILED** registry landing with num_counter_examples = 1. The pair
(C_H, C_epsH) shares identical factor support {H} but differs only in the
ε_H secondary HP¹ twist, which is invisible to even-parity Seeley-DeWitt
coefficients. §VII.P as originally written is FALSIFIED at the literal level;
refined §VII.P-v2 (restricted to HP⁰-content-distinct corridors) is S86+
carry-forward.

**Consequence for CC**: the `a_0` CC computation uses the HP⁰-content of
(A_F, H_F, D_F), unambiguously distinguished across corridors even without
§VII.P. The CC calculation is NOT affected by the pending refinement; the
structural parity-blindness exposed by W2-7 affects only corridor-pair
Seeley-DeWitt MATCHING (which is NOT a CC evaluation step).

#### 11.2.C Cross-references — S85 W2-6 and W2-7

- **S85 W2-6 (Quantum disjoint corridor, PASS)**: The Disjoint-Corridor
  separability theorem survives q-deformation of A_F at generic q ∈ (0,1) ∪ (1,∞)
  via 4-route confluence (HKR+SBI, H²_dR(S¹_q)=0, q-scan over 10 generic values,
  pullback from A_θ). Extending the substrate to non-commutative fiber
  algebras A_F^q does not break the parity-based corridor separation.

- **S85 W2-7 (Counter-construction, FAIL-with-refinement)**: identified the
  (C_H, C_epsH) twin pair where spectral moments match exactly despite
  HP²-disjointness — documenting the parity-blindness of even Seeley-DeWitt
  to HP¹ secondary twists. Refinement: §VII.P-v2 restricted to
  HP⁰-content-distinct corridors; odd-parity diagnostic (η-invariant,
  Godbillon-Vey integral) required for twin-pair distinguishability.
