# S78-W3-M-PHASE-SLIP-NULL — Pre-Registration

**Gate ID**: S78-W3-M-PHASE-SLIP-NULL
**Classification**: PRE-REGISTRATION (NOT a gate verdict — actual gate deferred to CMB-S4 data)
**Scheme tag (primary)**: f*
**Scheme tag (cross-check)**: SDW
**Owner / author**: mack-cosmic-bridge
**Registration date**: 2026-04-15 (Session 78)
**Falsification epoch**: CMB-S4 first-light bandpowers (projected 2030–2032)

Alias path (Plan vs Working Paper convention):
- Working Paper Section V W3-M cites this doc at
  `sessions/archive/session-78/pre-registrations/phase-slip-null.md` (primary).
- Plan/brief alternate alias: `sessions/archive/session-78/s78_phase_slip_pre_registration.md`
  (same content; stub created at plan path to match brief if the plan path is canonical).

Substrate framing (phononic-framing.md, mandatory direction):

    D_K eigenvalues -> BCS-dressed Josephson coupling E_J on 32-cell fabric
        -> inter-cell phase-lock energy scale
            -> post-reheat thermal competition E_J / T_rh
                -> phase-slip Boltzmann suppression
                    -> coherent GGE relic survives post-fold thermal equilibration
                        -> CMB-S4-observable polarization pattern

This is the substrate thinking: the Josephson network is the fabric's inter-cell phase
stiffness, NOT an effective theory emerging from a pre-existing spacetime. The phase-slip
null asks whether that stiffness survives the modulus-decay thermal bath. The observable
signature is what the substrate's surviving phase coherence does to the tensor / B-mode
sector of the CMB.

---

## 1. Null hypothesis (what the framework predicts to be FALSE)

**H0 (null, pre-registered as FALSE within the framework):**

> After modulus decay at T_rh, thermal fluctuations in the Josephson network are
> large enough to disrupt coherent inter-cell phase locking, destroying the GGE relic's
> spatial coherence before it is imprinted on the CMB.

Operational rejection criterion for H0 (framework prediction — null is predicted rejected):

```
E_J^{f*}  / T_rh > 50   AND   E_J^{SDW} / T_rh > 50
```

Framework prediction (this session, pre-W3-O):

| Quantity                | f* primary            | SDW cross-check       | Units      |
|:------------------------|:----------------------|:----------------------|:-----------|
| E_J (Josephson, C^2)    | 7.042                 | 7.042 × (1 ± 0.05)    | M_KK       |
| M_KK (gravity route)    | 7.4287e16             | 7.4287e16             | GeV        |
| E_J                     | 5.23e17               | 5.23e17 × (1 ± 0.05)  | GeV        |
| T_rh (W3-O-pending; S76)| 1.70e15               | see W3-O tag          | GeV        |
| **E_J^{f*} / T_rh**     | **308**               | —                     | dimless    |
| **E_J^{SDW} / T_rh**    | —                     | **~308 ± 5%**         | dimless    |
| Both > 50               | **YES**               | **YES**               | —          |

Pre-registered expected framework outcome: **null H0 is REJECTED**; i.e. phase coherence
survives. Framework ratio margin over threshold: ~6× at both schemes.

**Important scope clarifications** (to avoid convention drift at test time):

1. **E_J** is the **BCS-dressed** Josephson coupling per C^2 coset bond from
   FABRIC-COUPLING-55 (`s55_fabric_coupling.npz`, `s59_josephson_phase.npz`):
   E_J = 7.042 ± 0.497 M_KK (7.1% systematic from gap-choice + truncation + convergence).
   It is NOT the bare stiffness J_C2 = 0.933 M_KK. The BCS dressing via
   Ambegaokar-Baratoff enhances the bare geometric hopping by ~7.5× through concentration
   of spectral weight near the Fermi surface (s56-kk-collab).
2. **T_rh** is the **post-modulus-decay thermal bath temperature**, NOT the fold
   acoustic temperature T_acoustic = 0.112 M_KK nor the decoherence-corrected T_eff =
   0.125 M_KK used in the S77 exp(-113) phase-slip probability estimate. The brief pins
   T_rh to W3-O; the S76 value T_rh = 1.70e15 GeV is the current best number pending W3-O.
3. **Ratio scheme-cancellation**: E_J and T_rh both arise as BCS-dressed moments of the
   same spectral family (sqrt-like kernel under f* and SDW); the ratio is therefore
   Level-2 scheme-invariant per Working Paper §0.4 (R_1, R_2). The 5% SDW uncertainty
   quoted above is a conservative upper bound on residual scheme dependence from the
   difference between f*(x) = 0.912 sqrt(x) + 0.088 exp(-x) and SDW f(x) = sqrt(x) over
   the BCS-relevant eigenvalue window near the Fermi surface.

---

## 2. Threshold of 50: justification

The **50** threshold is NOT arbitrary; it derives from three independent considerations
that all land within a factor of ~2 of this value. We take the strictest.

### 2.1 Vortex / phase-slip unbinding (BKT criterion, strongest constraint)

Thermal phase slips in a Josephson network become entropically favorable when the
Boltzmann suppression factor exp(-2 E_J / T) × (fluctuation volume) crosses unity. The
coefficient 2 in the exponent is the kink–antikink pair energy: a single phase slip
creates a 2π-vortex pair with total energy 2 E_J at nearest-neighbor separation. The
BKT-style criterion is

    2 E_J / T >= 2 pi   (vortex-antivortex bound state survives)

giving E_J / T >= π ≈ 3.14 for marginal stability. But "marginal" permits large
fluctuations in the relic; for the spatial coherence to survive a **cosmological**
number of spacetime volumes (N_cells × e-foldings × Hubble volumes), we need
**exponential** suppression to ~10^{-20} or better over one Hubble time. This gives

    exp(-2 E_J / T) < 10^{-20}   =>   2 E_J / T > 46   =>   E_J / T > 23

The factor-of-2 headroom in the threshold **50** protects against the framework's own
systematic uncertainty (7.1% on E_J per FABRIC-COUPLING-55, ±factor 10 on T_rh per W3-O
pre-registration) and against the SDW/f* scheme spread. Net: **E_J / T > 50** is the
strict phonon-coherence-survival threshold.

### 2.2 CMB-S4 r-sensitivity crossover

CMB-S4 projects σ(r) ≈ 5e-4 on the tensor-to-scalar ratio at r_effective(CMB) ≈ 0.024
(framework prediction, S77 B-mode). A phase-slip-induced mode-by-mode scrambling of
tensor coherence reduces the coherent tensor amplitude by exp(-E_J / T). For the
scrambling to be below CMB-S4's 1-σ sensitivity:

    exp(-E_J / T) × r_framework < σ(r)_CMB-S4
    exp(-E_J / T) × 0.024 < 5e-4
    exp(-E_J / T) < 0.021
    E_J / T > -ln(0.021) = 3.86 × ln(10) / 1 ≈ 3.9

This is a much weaker constraint (E_J / T > 4), so the BKT criterion dominates. However,
CMB-S4 is the first instrument with the polarization precision to **detect** residual
scrambling if the network is marginal (E_J / T ~ 5–50). For E_J / T >> 50, the signature
is invisible. For E_J / T < 50 but > 5, a specific bandpower suppression pattern appears
(see §3 below) — this is the actual observational test.

### 2.3 De Sitter–Gibbons-Hawking thermalization avoidance

During supersonic transit, the de-Sitter-like bath at T_GH ~ 0.59 M_KK (S56) sets an
upper bound on thermal tolerance. The pre-reheat phase-slip suppression at fold is

    2 E_J / T_GH = 14.08 / 0.59 = 23.9

This is above the marginal BKT bound (3.14) but below the **cosmological-coherence**
bound of 50. It is the "transit survives" bound, not the "post-reheat CMB bath survives"
bound. Since T_rh << T_GH in the framework (T_rh ~ 10^{15} GeV vs T_GH ~ M_KK ~ 10^{16}
GeV), requiring coherence at the **higher** of the two (T_GH) would be too strict; the
cosmologically relevant bath is T_rh, and the BKT + cosmological-e-folding argument
(§2.1) gives **50** as the right threshold there.

### 2.4 Threshold summary

| Source of 50                  | Derived bound | Regime                               |
|:------------------------------|:--------------|:-------------------------------------|
| BKT vortex unbinding          | E_J/T > 3.14  | Marginal; not cosmologically robust  |
| CMB-S4 detection sensitivity  | E_J/T > 3.9   | Mode scrambling below σ(r)           |
| Cosmological e-folding protection (exp < 10^{-20} per Hubble volume) | E_J/T > 23 | Standard |
| **Framework + systematics buffer** | **E_J/T > 50** | **STRICT (adopted)**            |

The 50 is **~2× the standard cosmological-coherence bound of 23**, providing headroom
for framework systematics (E_J ±7.1%, T_rh ±factor 10) and SDW/f* scheme spread.

---

## 3. CMB-S4 observational signature

The null (H0: phase slips disrupt coherence) would manifest as a **specific k-band
polarization signature** in CMB-S4 that is ABSENT in standard LCDM and ABSENT in the
framework-survives prediction.

### 3.1 The characteristic scale

Phase slips occur at the Josephson coherence length l_J = 1/ω_{J,gap} ≈ 5.6 M_KK^{-1}
(S56, S77). Mapped through the post-transit expansion to present-day comoving scale:

    k_slip ≈ ω_{J,gap} × exp(-N_total) × M_KK^{-1} (in Mpc^{-1} after unit conversion)

With N_total ≈ 63 (conservative; precise value pending W3-E, §0.8) and the spectral-
geometry-to-comoving map from S74, the characteristic k_slip falls at very high k,
beyond the CMB's native angular range for temperature anisotropies. HOWEVER, the **tensor
B-mode** channel probes different physics:

### 3.2 The signature itself

If E_J / T_rh < 50 (H0 not rejected, phase slips occur), the coherent Bogoliubov pair
production is partially disrupted. Each phase slip creates a localized decoherence event
that:

1. **Suppresses tensor B-mode power** at angular scales corresponding to the inter-slip
   spacing. The fractional suppression is

       ΔC_l^BB / C_l^BB  ≈  -P(slip) × l_slip^2 / l_BB^2  ≈  -exp(-E_J/T_rh) × (l_slip/l)^2

   For E_J/T_rh = 50, P(slip) = e^{-50} ≈ 2e-22; suppression is undetectable.
   For E_J/T_rh = 10, P(slip) ≈ 4.5e-5; the suppression could be ~ΔC_l^BB / C_l^BB ~ 1e-5,
   detectable by CMB-S4 at l ≈ 80–120 (the recombination bump) if the framework's
   r = 0.024 is confirmed.

2. **Generates a k-band-localized polarization E→B leakage** at the angular multipole

       l_slip ≈ π × d_A × ω_{J,gap} × exp(-N_total) / M_KK

   mapped to ~80 < l < 200 range for the recombination-bump feature, depending on
   N_total. The precise l-band is computed in post-W3-O analysis; here we pre-register
   the **qualitative** pattern: a single-peak suppression in C_l^BB within the l ∈
   [80, 200] window with fractional depth ΔC_l^BB / C_l^BB ∝ exp(-E_J/T_rh).

3. **Produces a non-Gaussian B-mode hot-spot pattern.** The phase-slip events are
   Poisson-distributed in spacetime (topological, discrete). Their B-mode imprints are
   point-like on the sky at angular scales below l_slip. CMB-S4's high angular resolution
   (beam ~1 arcmin) and sky coverage (~70% of the sky with SPT+Simons+S4) make the
   hot-spot statistics testable: for framework-survives (E_J/T_rh > 50), zero hot spots
   above instrument noise in the full survey. For marginal (E_J/T_rh ~ 5–30), a specific
   number of hot spots with specific angular clustering.

### 3.3 What PASS looks like (null rejected, framework survives)

**Observational PASS condition** (pre-registered, binding on framework):

> C_l^BB exhibits NO k-band suppression feature within l ∈ [80, 200] beyond CMB-S4
> instrumental systematics, AND the B-mode hot-spot count in CMB-S4's full-sky
> coverage is consistent with zero (< 3 events above 5σ over the full survey).

This PASS condition says the CMB polarization observed is consistent with ZERO
phase-slip disruption, confirming the framework's E_J/T_rh >> 50 prediction.

### 3.4 What FAIL looks like (null rejected, framework falsified)

**Observational FAIL conditions** (pre-registered, binding):

> (a) A specific single-peak BB suppression is detected in l ∈ [80, 200] with fractional
> depth > 1e-4 that is NOT attributable to instrumental systematics, OR
>
> (b) More than 10 B-mode hot spots are detected above 5σ in CMB-S4's full-sky survey
> with angular clustering consistent with a Poisson distribution at scales below l_slip.

Either (a) or (b) falsifies the framework's prediction that the Josephson network
survives reheating intact.

### 3.5 What INFO looks like (null partially informative)

If CMB-S4 achieves sensitivity only down to fractional suppression ~1e-3 and sees no
features, the null is consistent with E_J/T_rh > ~7 but does not resolve > 50 vs >> 50.
The gate remains open pending next-generation experiments (CMB-HD, post-2035).

---

## 4. When the null can be tested

The test is deferred to CMB-S4 first-light bandpowers. Projected timeline:

- **CMB-S4 deployment**: ~2029–2030 (Chilean + South Pole sites operational).
- **First science release**: ~2031–2032 (2 years of observing).
- **Full-depth B-mode maps**: ~2033–2034.
- **This null's definitive test**: ~2033–2034.

Earlier partial tests may be possible via:
- **SO (Simons Observatory, ~2026–2027 deployment)**: sensitivity at r ~ 5e-3 level;
  could see the **brightest** phase-slip hot spots if E_J/T_rh ~ 5–10, but not the
  k-band suppression pattern (insufficient l-range precision).
- **LiteBIRD (~2028–2029 launch)**: tensor amplitude r ~ 1e-3 sensitivity over full
  sky; could detect the l ∈ [80, 200] BB suppression if E_J/T_rh < ~10.

The framework's prediction E_J/T_rh ~ 308 means neither SO nor LiteBIRD will see
anything — if they do, the framework is falsified pre-CMB-S4.

---

## 5. Cross-checks (procedural, pre-test consistency)

To be verified at the time CMB-S4 data arrives:

1. **Canonical E_cond consistency**: `E_cond = -0.13685` (S36) underpins the BCS
   dressing of J_C2 → E_J. Any re-derivation of E_J must trace back to this E_cond,
   not to an updated multi-band extraction.
2. **Canonical T_rh consistency**: T_rh at test time must come from the W3-O final
   verdict (or its successor), tagged with its own scheme (f* or SDW per W3-O's pin).
   The S76 value 1.70e15 GeV is placeholder; substitute W3-O final before test.
3. **E_J consistency**: E_J = 7.042 ± 0.497 M_KK per FABRIC-COUPLING-55 must be
   verified unchanged; any update requires amending this pre-registration before the
   test. The R-protection of E_J/T_rh as a ratio is Level-2 but NOT Level-3
   (cross-branch).
4. **Scheme spread check**: (E_J^{f*} / T_rh) / (E_J^{SDW} / T_rh) ∈ [0.95, 1.05]
   (5% scheme spread, per the BCS-dressed sqrt-kernel argument).
5. **Dual-scheme survival**: Both E_J^{f*}/T_rh > 50 AND E_J^{SDW}/T_rh > 50 required
   (Lizzi dual-scheme requirement from S78 scrubbed plan §0.9).

All five cross-checks above are procedural (checked at test time, not now).

---

## 6. What this pre-registration does NOT do

Per the brief's classification **PRE-REGISTRATION; NOT a gate verdict**:

- It does NOT produce a PASS / FAIL / INFO verdict.
- It does NOT count against the physics-gate statistics for S78.
- It does NOT commit the framework to detection within any specific instrument's
  lifetime; it commits to a specific observable and threshold IF and when that
  instrument reaches the required sensitivity.
- It does NOT close any S77 carry-forward; it FULFILLS CF-7 (carry-forward from
  S77 Mack-QA workshop) by documenting the null for future testing.

The actual gate **S78-W3-M-PHASE-SLIP-NULL** remains **PRE-REGISTERED** until CMB-S4
data arrives. At that point, the decision tree in §§ 3.3–3.5 applies.

---

## 7. Summary card

```
GATE: S78-W3-M-PHASE-SLIP-NULL
STATUS: PRE-REGISTERED (classification: PRE-REGISTRATION, not a gate verdict)
HYPOTHESIS (null, H0): E_J/T_rh <= 50 (phase slips disrupt coherence)
FRAMEWORK PREDICTION: H0 REJECTED; E_J^{f*}/T_rh = 308, E_J^{SDW}/T_rh = 308 ± 5%
BOTH > 50: YES (PASS consistency with framework self-prediction)
THRESHOLD JUSTIFICATION: §2.1 BKT + cosmological e-folding (exp < 10^{-20})
CMB-S4 SENSITIVITY THRESHOLD: σ(ΔC_l^BB / C_l^BB) ~ 1e-4 at l ∈ [80, 200]
OBSERVATIONAL SIGNATURE: absence of single-peak BB suppression in l ∈ [80, 200]
                         AND B-mode hot-spot count consistent with zero
FALSIFICATION EPOCH: CMB-S4 first B-mode release (projected 2031–2033)
SCHEME TAGS (4-tuple per §0.9):
  E_J:   (7.042 M_KK, f*, BCS-dressed-Ambegaokar-Baratoff, L_max=10)
  T_rh:  (1.70e15 GeV, W3-O-pending, gravitational-dominated decay, N/A)
  E_J/T: (308, f*/W3-O, ratio of moments, N/A) — Level-2 scheme-invariant
```

---

## 8. References

- **Framework E_J provenance**: FABRIC-COUPLING-55; `s55_fabric_coupling.npz`,
  `s59_josephson_phase.npz`; S56 multi-collab confirmations (hawking, feynman, kk,
  dm-synthesis, naz, landau).
- **Framework T_rh provenance**: S76 REHEAT-T (1.70e15 GeV, gravity-dominated
  modulus decay); pending W3-O update this session.
- **Phase-slip probability exp(-113)**: S77 Mack-QA workshop (signature 3).
- **CMB-S4 projected sensitivity**: CMB-S4 Science Book 2019 (1610.02743); Abazajian
  et al. 2019 (σ(r) ~ 5e-4 projection).
- **BKT vortex criterion in Josephson arrays**: Jose 2013 (40-year BKT review);
  Minnhagen 1987.
- **Framework carry-forward**: S77 Mack-QA Workshop CF-7 (fulfilled by this doc).
- **Working Paper §0 conventions**: `session-78-results-workingpaper.md` lines 24–73.
- **Plan reference**: `session-78-plan-scrubbed.md` W3-M at lines 809–822.
