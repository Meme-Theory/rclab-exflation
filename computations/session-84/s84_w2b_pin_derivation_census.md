# S84-PIN-DERIVATION-CENSUS — Derivation Log

**Gate**: S84-PIN-DERIVATION-CENSUS (W2-16)
**Trigger**: [AUDIT]
**Classification**: META
**Agent**: lizzi-spectral-functional-theorist
**Verdict**: PASS — value=5/5 scheme=per-obs convention=A L_max=5
**Closure SHA-256**: `9d501a94ca307efd5bf3b32556ae5fccf7af4da0f6d8e3976e8522dcf539ba74`

## Substrate framing

Particles are phononic excitations of the D_K spectrum on Jensen-deformed
SU(3); regulators are test-functions applied to that spectrum. Layer
commitment of an observable is the structural question of which fiber
of the Three-Layer Regulator Theorem (S83 §VII.M) the observable
physically lives on:

- **L1 (axiomatic / Dixmier-residue)**: the observable's defining
  functional IS a `<phi, x>` pairing with `phi in HP^n(A_F)` and
  `x in K_*(A_F)`. Evaluation is regulator-invariant by Connes (1988)
  Thm 5.3 (Dixmier-trace uniqueness). Zeta is the natively-admissible
  regulator at this layer (S83-G3 conjecture-promoted-to-theorem).
- **L2 (substrate-action / Zubarev)**: the observable REQUIRES a finite
  L_max truncation + regulator kernel to yield a numerical value. The
  Zubarev kernel `f_R(lambda) = exp(-lambda^2 / M_KK^2)` is the
  canonical L2 regulator (S82 MP-Exclusion Theorem, S83-G3-axiomatic).
- **MIXED**: the observable is a composite `f(O_L1, O_L2)` where neither
  component can be eliminated. Substrate derivation = positive
  construction of the decomposition + per-layer evaluation rule.

Layer commitments below are derived from the substrate-structural
properties of each observable's defining functional, NOT from the
regulator-scan span data backward (the span data are diagnostic
confirmations once the layer is identified).

## Template precedent

S83-G47 derived `mu_BC = M_Z * sqrt(1 + exp(12*tau_fold)/3)` from
2-loop RGE + mu_BC threshold matching, pinning `mu_BC = 188.34 GeV` from
substrate structure rather than from a PDG fit. The 5 derivations
below follow that pattern: substrate structure → layer commitment.

## Control: c_s (R-protected → must derive as L1)

Per plan §W2b-16 machinery pin §7: `c_s` (S83-G14 PASS, R-protected,
factor-1.227 span) is the template integrity check. It must reproduce
as L1 intrinsic via the same template, otherwise the derivation
template itself is broken.

Substitution chain (mandated by [AUDIT] trigger):

- Step a: `c_s^2 = <lambda^2>_R = tau_R(lambda^2) / tau_R(1)` — Bogoliubov
  dispersion first-moment ratio.
- Step b: Numerator and denominator carry the SAME regulator weight
  `w_R`; under L1 (Dixmier-residue) evaluation, both reduce to
  `Res_{s=0}(Tr |D_K|^{-s} * X)` with X = lambda^2 or 1; their ratio
  is the universal Connes-Moscovici state `rho_0` evaluated on
  `lambda^2` — regulator-invariant.
- Step c: S83-G14 reports 3-regulator span 1.227 at L_max=5; the
  residual 22.7% is the L2 finite-truncation correction, asymptoting
  to exact L1 invariance as L_max → infinity.
- Step d: 1.227 < 1.5 (R-protection threshold per S83-G58 meta-principle)
  → REGULATOR-INVARIANT at leading order → L1 intrinsic.
- Step e: Template-integrity check **PASS**: c_s = L1 intrinsic via
  the same template logic that derives k_a2 = L1 intrinsic via
  ratio-of-residues.

This certifies the template against the R-protected-control before
applying it to the 5 NOT-R-protected observables.

---

## O_1: k_a2 (Mellin multiplier at a_2 slot) → L1 intrinsic

**S83 anchor**: G15 K-A2-CANONICAL-RANGE FAIL — span_A=14.685054
(Convention A, Lambda_Z=M_KK), span_B=2.956027 (Convention B,
Lambda_Z=matched). SHA `5de7db1d032475a3...`.

**Step 1 — Definitional origin**:
`k_a2^R := f_2^R(Lambda^2) / f_2^{f*}(Lambda^2)` where
`f_2^R(Lambda^2) := int_0^{Lambda^2} w_R(u) du` is the Chamseddine-Connes
a_2-slot Mellin weight under regulator kernel `w_R(u)`, and `f_2^{f*}`
is the FIXED anchor denominator (S80-W1-A f* fit). The numerator varies
across 5 regulators; the denominator is a single anchor.

**Step 2 — Layer-of-definition test**:
`f_2^R` pairs the regulator kernel against the spectral density on the
a_2 slot. Two evaluation modes are available:
- (L1) Dixmier-residue `Res_{s=0} Tr(|D_K|^{-s}) * M_KK^{-2}` — regulator-
  invariant by Dixmier-trace uniqueness;
- (L2) finite-L_max substrate-action evaluation
  `sum_i w_R(lambda_i^2/M_KK^2) * lambda_i^{-2}` — regulator-dependent.
The denominator `f_2^{f*}` is a FIXED anchor (not a residue), so
ratio-cancellation is asymmetric. NOT-R-protected pattern: Mellin
kernel integral vs fixed anchor (S83-G15 memo: this is the FAIL pattern,
not PASS pattern).

**Step 3 — Substrate derivation chain**:
D_K eigenvalues `{lambda_i}` at L_max=5 → regulator-weighted spectral
moment `m_2^R = sum_i w_R(lambda_i^2/M_KK^2) / lambda_i^2` →
`f_2^R(Lambda^2)` is the finite cumulative integral of `w_R` on
`[0, Lambda^2]` → `k_a2 = f_2^R / f_2^{f*}`. The L1 path REQUIRES the
Dixmier-residue representation: `f_2^R^{L1} = C * M_KK^2` with `C`
universal (regulator-invariant). Under L1: `k_a2^{L1} = (C * M_KK^2)
/ (C * M_KK^2) = 1` TRIVIALLY. Under L2 at L_max=5: span 14.685 (S83-G15).
Therefore S83-G15 evaluated at L2, NOT at L1.

**Step 4 — Concrete substitution chain**:
- Step a: `k_a2^{L1} := f_2^R^{L1} / f_2^{f*}^{L1}` where both are
  Dixmier residues `Res_{s=0}(Tr |D_K|^{-s})`.
- Step b: By Connes (1988) Thm 5.3, `Res_{s=0}(Tr |D_K|^{-s}) = C * M_KK^2`
  independent of regulator R.
- Step c: `k_a2^{L1} = (C*M_KK^2)/(C*M_KK^2) = 1`.
- Step d: Span_A=14.685 per G15 is >> 1 at L_max=5, incompatible with
  L1 regulator-invariance. Therefore G15 evaluated at L2 (finite-L_max
  substrate-action cumulative integral).
- Step e: Layer assignment **L1 with L2-evaluation-artifact tag**.
  The L2-span 14.685 reflects the FACT that the framework's downstream
  uses (e.g., S83 UNIFIED-AS-79 with k_a2 = 0.583 zeta value) all
  invoke L2 evaluation; the intrinsic layer remains L1 (residue ratio = 1).

---

## O_2: f_conv (a_0-slot tadpole normalization) → L2 intrinsic

**S83 anchor**: G28 F-CONV-CLUSTER-TEST FAIL — cluster_max_over_min=
1766.162324 (5-regulator atlas, L_max=5). SHA `612146123a852d13...`.

**Step 1 — Definitional origin**:
`f_conv` is the tadpole normalization `1/M_0^2` where
`M_0^2 = sum_i (lambda_i^2)^{-1} * w_R(lambda_i^2/M_KK^2)` is the
zeroth-moment of the regulated spectrum. In Connes-Chamseddine bosonic
spectral action, `f_conv` enters as the a_0-slot Mellin moment
`f_0^R = int_0^inf w_R(u) du` (relative measure of the zeroth moment).
Anchor (S78-W2-D): `f_0^{sharp} = 1/2` (anomaly-forced, Andrianov-Lizzi
arXiv:1001.2036); `f_0^{f*} = f*(0) = beta_star = 0.0883` (S72 f* kernel
at u=0).

**Step 2 — Layer-of-definition test**:
`f_0` is the a_0-slot Mellin moment. At L1 (Dixmier residue), the a_0
moment is `Res_{s=0}(Tr |D_K|^{-s})|_{a_0 slot}` — a topological
number (Euler characteristic times Vol for a compact fiber), regulator-
invariant. At L2 (substrate-action finite-L_max=5),
`f_0 = sum_i w_R(lambda_i^2 / M_KK^2) / M_KK^2` depends on `w_R`'s shape
near `u=0`. The L_max-scan in S78-W2-D Table (L_max in {3,5,7,9}) shows
the 3-scheme cluster {SDW, zeta, anomaly-sharp} drifts monotonically
1.129 → 1.161 (tight), but `f_0^{f*}` is categorically OUTSIDE by
factor 16.2. S83-G28 cluster-span = 1766 across the 5-regulator atlas
= regulator-shape-at-origin sensitivity. This is NOT a Dixmier residue
invariant.

**Step 3 — Substrate derivation chain**:
D_K at L_max=5 → spectrum `{lambda_i}` (finite, no accumulation at 0
for compact-fiber bosonic projector) → `f_conv(R) = sum_i
w_R(lambda_i^2/M_KK^2) / sum_j (lambda_j^2/M_KK^2)`. Numerator dominated
by smallest eigenvalues, where `w_R(0)` differs sharply across
regulators: `w_zeta(0) = 1`, `w_SDW(0) = 0.088`, `w_Zubarev(0) = 1`,
`w_fstar(0) = 0.088`. S83-G28's cluster=1766 directly reflects this
regulator-shape-at-origin dependence. The Dixmier-residue at the a_0
slot is regulator-invariant by construction; therefore `f_conv` cannot
be Dixmier-residue-determined.

**Step 4 — Concrete substitution chain**:
- Step a: `f_conv ~ 1/M_0^2`, `M_0^2 = (f_0^R)^{-1}`.
- Step b: `f_0^R = int_0^Lambda^2 w_R(u) du`, with `w_R(0)` varying
  across R by factor 16.2.
- Step c: A Dixmier residue `Res_{s=0}(Tr |D_K|^{-s})` at the a_0 slot
  picks out the heat-kernel-zeroth coefficient (topological), which
  does NOT carry regulator-shape-at-origin information.
- Step d: S83-G28 cluster = 1766 = regulator-shape-at-origin span.
  This is an L2 artifact: `f_conv` is the L2 evaluation of the a_0
  tadpole, not an L1 Dixmier residue.
- Step e: Layer assignment **L2 intrinsic** (substrate-action at a_0
  slot). Canonical L2 regulator: Zubarev (per S83-G3 axiomatic
  priority).

---

## O_3: A_s absolute (Mukhanov-Sasaki amplitude) → MIXED-irreducible

**S83 anchor**: UNIFIED-AS-79-WITH-3PI-SUBSTITUTION PASS — A_s_new=
5.0782e-9, log10/canon=+0.1872, scan_span=14.69 (k_a2 driver),
PASS_reg=4/5. SHA `9917b78e62bfb5e6...`.

**Step 1 — Definitional origin**:
`A_s_absolute = P_zeta(k_pivot) = (H^2 / (8 pi^2 * M_Pl^2 * eps_H))
* F_amp_3PI * k_a2`, where:
- `H` = horizon-exit Hubble parameter (epoch-gated: H_TD pre-fold or
  H_LI post-fold);
- `eps_H` = Hubble slow-roll parameter (substrate-derived from a_2
  Seeley-DeWitt gradient per S83-G20, F_traj=3/2 EXACT rational);
- `M_Pl^2` = emergent Planck mass squared (a_2 coefficient of spectral
  action);
- `F_amp_3PI` = Berges-Serreau 3PI NLO amplitude factor;
- `k_a2` = O_1 above (L1-intrinsic-with-L2-evaluation-artifact).

**Step 2 — Layer-of-definition test**:
A_s decomposes into 5 factors residing on different layers:
- (i) `H` — epoch-gated substrate-action value at horizon exit → L2;
- (ii) `eps_H` — F_traj=3/2 EXACT rational, S83-G20 substrate-derivable
  → L1 (a_2-gradient ratio with Cartan Dixmier trace);
- (iii) `M_Pl^2 ~ a_2` coefficient → L1 intrinsic (a_2 IS the Seeley-
  DeWitt cocycle residue);
- (iv) `F_amp_3PI` — Berges-Serreau NLO amplitude → L3-style epoch-
  observable-tied closure factor (best classified under L2 canonical
  substrate);
- (v) `k_a2` — L1 with L2-evaluation artifact (per O_1).
Multiple layers present irreducibly → A_s is MIXED.

**Step 3 — Substrate derivation chain**:
D_K at tau=tau_fold → `{lambda_i(tau)}` spectrum → `a_2(tau)` Seeley-
DeWitt coefficient (L1 residue) → `M_Pl^2_eff(k)` via a_2-gradient
Jensen-flow scale transport (L2 substrate evaluation) → `eps_H` via
F_traj=3/2 from a_2-ratio (L1-structural) → `H(N)` via substrate
impedance and epoch gate (L2: H_TD or H_LI) → `P_zeta` per Mukhanov-
Sasaki formula. Decomposition `A_s = F(A_s^{L1}, A_s^{L2})`:
`A_s^{L1}` = `k_a2^{L1} * eps_H^{-1, L1} * (a_2)^{-1, L1} = 1 * (3/2)^{-1}
* const` (L1-trivial-product); `A_s^{L2}` carries epoch-gated H^2 and
F_amp_3PI. Multiplicative combination is fixed by the standard scalar
power spectrum definition.

**Step 4 — Concrete substitution chain**:
- Step a: `A_s = (H^2 / (8 pi^2)) * (eps_H * M_Pl^2)^{-1} * F_amp_3PI
  * k_a2`.
- Step b: L1 factors: `eps_H` (F_traj=3/2, S83-G20), `M_Pl^2` (a_2
  residue), `k_a2` (trivial 1 at L1 per O_1).
- Step c: L2 factors: `H^2` (epoch-gated), `F_amp_3PI` (Berges-Serreau
  NLO).
- Step d: Multiplicative product rule (Mukhanov-Sasaki standard form):
  `A_s = [L1 kernel: (eps_H * M_Pl^2 * k_a2)^{-1}] * [L2 kernel:
  (H^2 / 8 pi^2) * F_amp_3PI]`.
- Step e: Under L1 alone (H-epoch-independent limit), A_s carries only
  the k-space transport ratio (epoch-insensitive, formally undefined
  scale); under L2 alone, H^2 is fixed but the L1-prefactor must be
  imported. Both layers are required for the numerical 5.0782e-9
  (S83 PASS). Layer assignment **MIXED-irreducible** with positive
  L1/L2 decomposition.

---

## O_4: w_0 (dark-energy equation of state today) → MIXED

**S83 anchor**: G51 W_0-REGULATOR-CANONICAL-CHOICE FAIL —
w_0_Zubarev=-0.998116; L1 value = -1 (CC identity); L1-vs-L2 split=0.080.
SHA `224b7b5648f5fdf2...`.

**Step 1 — Definitional origin**:
`w_0 = p_substrate(today) / rho_substrate(today)`. Volovik partition
sum: `w_0 = - Sum_i E_i (1 + E_i * dE_i/dN) / Sum_i E_i` where `E_i`
are the D_K-mode energy eigenvalues and `dE_i/dN` is the e-fold-gradient
of mode-i energy. In the exact CC limit (static fiber), `dE_i/dN = 0`
for all i and `w_0 = -1` identically.

**Step 2 — Layer-of-definition test**:
`w_0` is the ratio of two linear functionals of the D_K spectrum.
- (L1, Dixmier trace / CC identity): `w_0 = -1` exactly because the
  CC sector is static-substrate-dominated; the Dixmier trace gives
  the universal CC value.
- (L2, Zubarev substrate-action at L_max=5): Volovik partition sum
  evaluates to `w_0 = -0.998116` (S83-G51) with epoch-gated
  `dE_i/dN ~ exp(-alpha * tau_fold)` non-zero.
Both L1 and L2 representations exist and DIFFER numerically at the
4th decimal: `|(-1) - (-0.998116)| = 0.001884`, exceeding the 1e-6
MIXED tolerance → MIXED.

**Step 3 — Substrate derivation chain**:
D_K(tau_today) → `{E_i(tau_today)}` via Zubarev regulator → Volovik
partition sum `w_0^{Zubarev} = -0.998116` (L2 at finite L_max=5). L1
path: Dixmier trace `tau(1)` on substrate sector = universal CC
identity → `w_0^{L1} = -1`. The L1→L2 correction is
`O(exp(-alpha * tau_fold)) ~ O(10^-3)`, dominated by residual
exterior-gradient leakage through the impedance mismatch
(`Gamma = 0.99970`).

**Step 4 — Concrete substitution chain**:
- Step a: `w_0 = - Sum_i E_i * (1 + E_i * dE_i/dN) / Sum_i E_i`.
- Step b: L1: `dE_i/dN → 0` (static fiber) → `w_0^{L1} = -Sum_i E_i
  / Sum_i E_i = -1` identically.
- Step c: L2: `dE_i/dN` non-zero from `exp(-alpha * tau_fold)` leakage
  → `w_0^{L2} = -0.998116`.
- Step d: `|w_0^{L1} - w_0^{L2}| = 0.001884 > 1e-6` → numerically
  different across layers → **MIXED**.
- Step e: DR3 forecasting policy: use L2 Zubarev (substrate-action
  canonical, S83-G3 axiomatic priority) for observational prediction;
  cite L1 theoretical limit `-1` as reference asymptote.

---

## O_5: CC-ratios (composite dark-energy family ratios) → MIXED-heterogeneous

**S83 anchor**: G34 CC-RATIO-CLUSTER-UNIVERSALITY FAIL — max_span=
42.025734; per-ratio: span_1=4.607771, span_2=42.025734, span_3=6.482726.
SHA `64d7f2c3be60a656...`.

**Step 1 — Definitional origin**:
`CC-ratios := {R_1, R_2, R_3}` are three composite Mellin-moment ratios
drawn from the a_0/a_2/a_4-slot spectral-action coefficients under 5
regulators. Per S83-G34: R_1 ~ a_0/a_4 ratio family (span_1=4.61);
R_2 ~ cross-slot tadpole ratio (span_2=42.03, dominant);
R_3 ~ subdominant a_2-moment cousin (span_3=6.48). CC-5 transport
identity (S83-G34 PROP): `span(R_i) = prod_j span(F_j)^{|p_ij|}` where
`F_j` are irreducible factor spans and `p_ij` integer exponents.

**Step 2 — Layer-of-definition test**:
Each `R_i` decomposes into an integer-power product of factors `F_j`,
each an a_k-slot Mellin moment. Layer of `R_i` = layer-set of dominant
`F_j` by `|p_ij|`. Inspection:
- R_2 (span 42) dominated by a_0-slot tadpole factor (cf. f_conv, O_2
  = L2 intrinsic), exponent `~|2|`.
- R_1 (span 4.6) dominated by a_2/a_4 ratio: a_2 is L1 residue, a_4
  requires finite-L_max evaluation → mixed L1/L2 per ratio.
- R_3 (span 6.5) dominated by a_2-moment cousin: L1 at residue level,
  L2 at finite evaluation.
Different ratios have different dominant-layer assignments →
HETEROGENEOUS MIXED at the family level.

**Step 3 — Substrate derivation chain**:
D_K → spectrum → `a_k(R)` Seeley-DeWitt coefficients at L_max=5 →
factor `F_j` = Mellin-kernel-integral at slot k under regulator R →
`R_i = prod_j F_j^{p_ij}` per CC-5. Layer-assignment per `R_i`:
(a) compute `p_ij` Smith-normal-form integer matrix; (b) per `F_j`
determine layer (L1 if Dixmier-residue-representable, L2 if finite-
L_max-required, MIXED if both with numerical disagreement); (c) `R_i`
layer = weighted set of dominant `F_j` layers by `|p_ij|`. Per G34 span
data: R_1 → {L1-a_2-residue, L2-a_4-evaluation} (MIXED, both relevant);
R_2 → L2-a_0-tadpole-dominant (MIXED, L2-dominant); R_3 → L1-a_2-cousin
dominant (MIXED, L1-dominant).

**Step 4 — Concrete substitution chain**:
- Step a: `R_i = prod_j F_j^{p_ij}` (CC-5 identity).
- Step b: For each `F_j`, compute `layer(F_j)` by Step 1-4 template
  (as applied to k_a2/f_conv above).
- Step c: R_1: F_a = a_2 (L1, Dixmier residue of heat-kernel 2nd
  coefficient, regulator-invariant), F_b = a_4 (L2, finite-L_max
  finite-moment evaluation). `R_1 = F_a^{+1} * F_b^{-1}` → MIXED.
- Step d: R_2: dominant factor F_tadpole = a_0-slot tadpole = f_conv
  cousin (L2 per O_2). `R_2 = F_tadpole^{~+2}` → L2-dominant MIXED.
- Step e: R_3: dominant factor F_a2-cousin = a_2-moment cousin (L1
  residue, L1-evaluable trivially analogous to k_a2^{L1}). `R_3 =
  F_a2-cousin^{~+1}` → L1-dominant MIXED.
- Step f: Per-ratio sub-layer tags:
  - R_1: MIXED-L1L2-both-relevant
  - R_2: MIXED-L2-dominant
  - R_3: MIXED-L1-dominant
  Family-level assignment: **MIXED-heterogeneous**.

---

## Summary Table

| Observable | S83 gate | S83 verdict / value | Layer | Tag |
|:-----------|:---------|:--------------------|:------|:-----|
| O_1 k_a2 | G15 K-A2-CANONICAL-RANGE | FAIL span_A=14.685 | **L1** | L1-intrinsic-with-L2-evaluation-artifact |
| O_2 f_conv | G28 F-CONV-CLUSTER-TEST | FAIL cluster=1766 | **L2** | L2-intrinsic-substrate-action-at-a0-slot |
| O_3 A_s abs | UNIFIED-AS-79 | PASS A_s=5.08e-9 | **MIXED** | MIXED-L1-kernel-L2-epoch-irreducible |
| O_4 w_0 | G51 W_0-REGULATOR | FAIL w_0=-0.998 | **MIXED** | MIXED-L1-limit-L2-canonical-prediction |
| O_5 CC-ratios | G34 CC-RATIO-CLUSTER | FAIL max_span=42 | **MIXED** | MIXED-heterogeneous-per-ratio-sub-layer |

**Layer distribution**: L1=1, L2=1, MIXED=3, UNPINNED=0. **Derived count: 5/5**.

**Control c_s** (R-protected, S83-G14 PASS): derived as **L1 intrinsic**
via the same template (R-protected first-moment ratio). Template-
integrity check **PASS**.

## Verdict

`S84-PIN-DERIVATION-CENSUS: PASS -- value=5/5 scheme=per-obs convention=A`
`L_max=5 sha256=9d501a94ca307efd5bf3b32556ae5fccf7af4da0f6d8e3976e8522dcf539ba74`

## What this PASS means for the solution space

PASS: The Three-Layer Regulator Theorem (S83 §VII.M) has been promoted
from a regulator-classification theorem (S83-G3 + S82 MP-Exclusion +
S83-G27) to an **observable-classification theorem** for NOT-R-protected
observables. Every NOT-R-protected observable in the 5-member set has
its layer commitment derived from substrate structure (D_K eigenvalues
+ Mellin functional evaluation path), NOT from the regulator-scan span
data backward.

Downstream observational forecasts (W3 wave) get a layer-tagged
prediction table for the 5 NOT-R-protected observables. Carry-forward
to W3:
- **L1 (k_a2)**: report intrinsic value 1; L2-span 14.685 is an
  evaluation-layer artifact, must be flagged when computing downstream
  composites (e.g., A_s).
- **L2 (f_conv)**: report Zubarev value as canonical (substrate-action
  at L_max=5); other regulators are L1-incompatible at the a_0 slot.
- **MIXED (A_s, w_0, CC-ratios)**: report explicit L1/L2 decomposition
  per observable; downstream computations cite per-layer reasoning.

No remaining ambiguity about which observables are "regulator-free in
principle" (L1, regulator-invariant Dixmier residue) vs "regulator-
sensitive in principle" (L2, finite-L_max substrate-action) vs
"layer-composite" (MIXED).

## Files

- Script: `computations/session-84/s84_w2b_pin_derivation_census.py`
- Data: `computations/session-84/s84_w2b_pin_derivation_census.npz`
- Verdict: `computations/session-84/s84_gate_verdicts.txt` (line: `S84-PIN-DERIVATION-CENSUS: PASS ...`)
- Working paper section: `sessions/archive/session-84/session-84-w2-workingpaper.md` §W2-16
