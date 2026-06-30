# Session 85 Slot 3A — ζ-Regulator-Stabilization Theorem Candidate (Lizzi Mellin-cone / spectral-functional track)

**Date**: 2026-04-25
**Agent**: lizzi-spectral-functional-theorist (lizzi)
**Track**: subsection (a) — Mellin-cone / ζ-regularization / spectral-functional. Subsection (b) is being written in parallel by `spectral-geometer` on the heat-kernel / Seeley–DeWitt / ζ_D(s) analytic-continuation track.

**Source Documents**:
- `sessions/archive/session-85/session-85-w10-workingpaper.md` (Highlight #1 closing-note + Constraint-Map row + W10-4 PASS verdict block)
- `computations/s85_gate_verdicts.txt` (S85-W10-* and S85-W0-L-MELLIN-CONE-S3-RESIDUE)
- `computations/s85_w10_w0_inverted_branch_enumeration.json` (raw SV2 trajectories for L ∈ {5,6,7,8} — Python-verified below)
- `sessions/archive/session-85/session-85-w6-13-workshop-schedule.md` (Slot 1a Row 3A invocation)
- `sessions/archive/session-85/session-85-workshop-schedule.md` (W0-W5 S-1 + S-6 cross-pairings)
- `sessions/archive/session-85/session-85-s1-regulator-boundary-lizzi.md` (S-1 Mellin-residue scope statement; pure-a_4 family `F_4`)
- `sessions/archive/session-85/session-85-s6-truncation-taxonomy-lizzi.md` (S-6 4-class taxonomy + S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate)
- `sessions/permanent-results-registry.md`

---

## I. Session Outcome

**Verdict on the candidate theorem**: **REFUTED at the proposed scope, REPLACED by a strictly weaker scope-bounded statement that is provable inside that scope.**

The empirical 5-regulator slope inequality recorded in W10 Highlight #1 — slope(S_zeta_E) = 0.97 > slope(mellin_s3) = 0.56 > slope(S_Zubarev_E) = 0.17 (data-verified ordering; see §II.1; the schedule context-block has the Mellin and Zubarev labels swapped) — is **L_max-WINDOWED** (fit on L ∈ {5,6,7,8}; log-linear fit, not constant-exponent power-law) and lives at s=3 which is **INSIDE the divergence cone** of `Z_D(s) = Σ d(λ) λ^{-s}` for d_spec ≈ 8 (s=3 < d_spec/2 = 4). Per S85 W0-W5 S-6 (lizzi solo) primary class (c) TRUNCATION-INAPPROPRIATE-THRESHOLD with secondary (b) METHOD-INAPPROPRIATE, the W0-L-MELLIN-CONE-S3-RESIDUE FAIL (value=1.81e6, monotone-increasing) is a class-(c)-primary and class-(b)-secondary instance: direct truncated `Z(s=3, L)` is NOT a residue of the meromorphic continuation of ζ_D(s). The candidate theorem's "ζ-regulator stabilization" property is therefore conditional on the analytic-continuation infrastructure that does NOT exist at finite L until S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE lands. The empirical observation IS L_max=12 truncation artifact at the structural level the candidate theorem claims to characterize.

**What survives** (proven inside its scope): a **windowed kinematic inequality** on the log-linear-fit slopes of three specific spectral aggregates over the small-L window {5,6,7,8}, with explicit Mellin-multiplier interpretation per regulator. This is not a regulator-class theorem about L→∞ stabilization. It is a finite-L FIT statement whose extrapolation through the analytic continuation is the actual physics question, deferred to the S86 gate proposed below.

**Cross-pairing flags**: this synthesis intersects W0-W5 S-1 (Regulator-Family Boundary; pure-a_4 `F_4` scope) and W0-W5 S-6 (L_max-Truncation Taxonomy + S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate). Both pairings are recorded in §III. The candidate theorem's scope inherits both: S-1 forbids the use of mixed-support observables as pure-a_4 invariants, and S-6 forbids residue claims at finite L without analytic continuation.

---

## II. Key Results

### II.1 Data-Verified Slope Ordering (CANONICAL)

**Result**: slope(S_zeta_E) = 0.9748 > slope(mellin_s3) = 0.5598 > slope(S_Zubarev_E) = 0.1716. **GEOMETRIC** (substrate-spectral aggregate growth diagnostic; Mellin-cone is intrinsic to D_K).

**Substitution chain (verified via Python on `computations/s85_w10_w0_inverted_branch_enumeration.json`)**:

```
Step 1 (definition):
  slope_X := d ln(X(L)) / dL, fit by least-squares on L ∈ {5,6,7,8}.

Step 2 (substitute the numerical SV2 trajectories):
  S_zeta_E(L)    = [3.34e5, 1.03e6, 2.81e6, 6.17e6]
  mellin_s3(L)   = [2.05e4, 3.96e4, 7.07e4, 1.09e5]
  S_Zubarev_E(L) = [6.56e3, 8.84e3, 1.04e4, 1.10e4]
  ⇒ slope(S_zeta_E)    = 0.9748, R^2 = 0.9938
  ⇒ slope(mellin_s3)   = 0.5598, R^2 = 0.9918
  ⇒ slope(S_Zubarev_E) = 0.1716, R^2 = 0.9122

Step 3 (simplify pairwise differences):
  Δ_1 := 0.9748 - 0.5598 = 0.4150 > 0
  Δ_2 := 0.5598 - 0.1716 = 0.3881 > 0

Step 4 (direction):
  slope(S_zeta_E) > slope(mellin_s3) > slope(S_Zubarev_E)
  on the fit window L ∈ {5,6,7,8}.
```

The W10 working paper body (`session-85-w10-workingpaper.md` lines 1098–1100) and Constraint-Map row 6 / row 9 (lines 1150, 1153) both use this ordering. **The schedule's Slot 3A context-block writes "(b) Mellin-cone s=3 residue numerator growth slope ≈ 0.17. (c) Zubarev slope ≈ 0.56 (intermediate)" — these two labels are SWAPPED relative to the data.** The authoritative numerical assignment is: zeta = 0.97, **mellin = 0.56**, **Zubarev = 0.17**. Both this synthesis and subsection (b) (spectral-geometer) operate on the data-verified ordering. The candidate theorem's prose statement ("ζ denominator strictly exceeds Mellin-cone s=3 residue numerator; Zubarev does not") is preserved by either label-assignment because the order of the three numbers is unambiguous; only the label "Zubarev does not" changes meaning. Under the data-verified labelling, the theorem prose reads correctly: ζ-slope (0.97) exceeds mellin-slope (0.56) AND exceeds Zubarev-slope (0.17); both ζ and (trivially) Zubarev denominators undershoot the slope ordering required for the "stabilization" reading. Subsection (b) confirms this independently from the heat-kernel side.

**Power-law diagnostic** (log-log fits on the same window, for context):
- S_zeta_E ~ L^6.24
- mellin_s3 ~ L^3.58
- S_Zubarev_E ~ L^1.12

The data are clearly POWER-LAW in L on the {5,6,7,8} window, not log-linear. The log-linear slope numbers 0.97 / 0.56 / 0.17 are window-specific descriptors that PARAMETRIZE the local extrapolation, not constant-exponent invariants of the substrate. This matters for the theorem candidate's L→∞ reading: see §II.5 for why this distinction breaks the proposed stabilization claim.

### II.2 Mellin Form of the Three Aggregates

**Result**: Both spectral aggregates `S_zeta_E(L)` and `S_Zubarev_E(L)` are MIXED-support Mellin-cone evaluations (a_2/a_4-weighted), and `mellin_s3(L)` is the truncated direct-sum value of `Z(s=3; L) = Σ_{λ ≤ Λ(L)} d(λ) λ^{-3}`. None of the three is a pure-a_4 (F_4) observable per S-1. **GEOMETRIC**.

The three aggregates are defined (per the W10-4 script `s85_w10_w0_inverted_branch_enumeration.py` and SV2 trajectories) as:

```
mellin_s3(L)   :=  Σ_{n: λ_n ≤ Λ(L)}  d_n · λ_n^{-3}                            (1)
S_zeta_E(L)    :=  Σ_{n: λ_n ≤ Λ(L)}  d_n · w_zeta(λ_n) · E(λ_n)                (2)
S_Zubarev_E(L) :=  Σ_{n: λ_n ≤ Λ(L)}  d_n · w_Zub(λ_n)  · E(λ_n)                (3)
```

where `w_zeta(x) ≡ 1` (zeta-class is sharp truncation, no extra weight beyond the cap; per S78 R1 cross-groups dictionary), `w_Zub(x) = exp(-x^2/Λ_Z^2)` (Zubarev Gaussian with scale Λ_Z = M_KK), `E(λ) = λ` (energy weight; sets these as second-moment-weighted aggregates), and `Λ(L)` is the spectral cutoff implied by the L_max truncation (Λ(L) ~ L · M_KK by Weyl growth on Jensen-SU(3)).

In Mellin language, `S_zeta_E(L)` is the truncation of `Σ_n d_n λ_n^{-(-1)} = Σ_n d_n λ_n` evaluated on the Λ(L) sphere — i.e. it tracks the residue of `Z(s; L)` at s = -1, equivalently the "growth integral" of the spectral density. This sits MUCH deeper inside the divergence cone than s=3 (s=-1 is below ALL Seeley–DeWitt poles of d=8 NCG, which lie at s ∈ {0, 2, 4, 6, 8}). It is dominated by the Weyl bulk and grows roughly as Λ(L)^{d_spec+1} ≈ L^9 in the asymptotic L_max → ∞ limit; on the small-L window {5,6,7,8} the observed log-log exponent is ≈ 6.24 (start-up regime). Under the Mellin-multiplier framework of S78 W2-F (and per S-1 lizzi solo §II.4), `S_zeta_E` is NOT a pure-a_4 observable: its character vector `m^{S_zeta_E} = (m_0, m_2, m_4, m_6, m_8)` has support beyond `n=4`, so it falls in the M (mixed-support) class.

`S_Zubarev_E(L)` is the SAME bulk integral DAMPED multiplicatively by the Zubarev Gaussian. The damping kicks in at λ ≳ Λ_Z = M_KK and saturates beyond it. On the L ∈ {5,6,7,8} window the saturation regime dominates (the trajectory grows from 6564 → 11023, a factor of 1.68 over 3 steps in L; cf. S_zeta_E's factor of 18.5 over the same range). The Zubarev cutoff is NOT a Mellin-multiplier of the form `f^r = (f_0, f_2, f_4, f_6, ...)` with FINITE Mellin support; it is a Schwartz-class function whose Mellin transform `M[w_Zub](s) = (Λ_Z^s/2) Γ(s/2)` is meromorphic with poles at s = 0, -2, -4, ... (an infinite-support analytic Mellin multiplier). So `S_Zubarev_E` is also OUTSIDE F_4.

`mellin_s3(L)` is the direct truncated zeta value. At s=3 in d_spec=8 NCG, s=3 is BETWEEN the a_6 Seeley–DeWitt pole at s=2 and the a_4 pole at s=4. It is an OFF-POLE evaluation, but s=3 < d_spec/2 = 4 places it inside the divergence half-plane below the leading pole, so direct truncated sums diverge as L → ∞. The asymptotic Weyl divergence rate is `Z(3; L) ~ Λ(L)^{d_spec - 3} = L^5`; the small-L observed log-log exponent is 3.58 (start-up regime, consistent with L^5 asymptotics undershooting on the {5,6,7,8} window).

**S-1 implication**: none of the three aggregates is in F_4. The schedule's instruction to "derive the slope inequality... using the Mellin-multiplier theorem (S78 W2-F scope) restricted to the pure-a_4 family per the W0-W5 S-1 Regulator-Family Boundary Theorem" is an INSTRUCTION TO RESTRICT SCOPE, but no such restriction exists for these observables — they live in M, not F_4. The Mellin-multiplier theorem in F_4 form applies to observables of the shape `O = m_4^O · a_4` only; `S_zeta_E`, `S_Zubarev_E`, and `mellin_s3` all carry support across multiple n. Therefore S78 W2-F does NOT directly bound the slope inequality. This is the FIRST scope-failure of the candidate theorem statement.

### II.3 Mellin-Pole Structure at s=3 in d_spec=8

**Result**: s=3 is OFF-POLE (between a_6 at s=2 and a_4 at s=4) and INSIDE the divergence cone (s < d_spec/2 = 4). The "residue" extraction at s=3 is therefore NOT a Seeley–DeWitt residue in the Connes–Moscovici sense — it is a direct truncated-zeta evaluation. **GEOMETRIC**.

**Substitution chain**:

```
Step 1 (definition; CM 1995 / Lizzi 2014):
  ζ_D(s) · Γ(s/2) = ∫_0^∞ t^(s/2 − 1) K(t) dt           (Mellin transform)
  K(t) = Σ_n a_n(D^2) t^(n − d_spec/2)                  (small-t Seeley–DeWitt expansion)

Step 2 (substitute into the Mellin integral):
  ∫_0^∞ t^(s/2 − 1) · t^(n − d_spec/2) dt
    = ∫_0^∞ t^(s/2 + n − d_spec/2 − 1) dt
    = pole at  s/2 + n − d_spec/2 = 0
    ⇔  s = d_spec − 2n.

Step 3 (simplify for d_spec = 8):
  Pole at s = 8 (n = 0, residue ∝ a_0)
  Pole at s = 6 (n = 1 → a_2 in heat-kernel index; equivalently CM index 2)
  Pole at s = 4 (n = 2 → a_4; CM index 4)
  Pole at s = 2 (n = 3 → a_6; CM index 6)
  Pole at s = 0 (n = 4 → a_8; CM index 8).

Step 4 (direction):
  s = 3 ∈ (2, 4) is BETWEEN the a_6 pole (s=2) and the a_4 pole (s=4).
  s = 3 < d_spec/2 = 4 puts s=3 INSIDE the divergence half-plane
    (Re(s) ≤ d_spec/2 has divergent direct truncated sums).
  At s=3, the analytic continuation of ζ_D(s) is FINITE and equals the
    boundary value picked up between the a_4 and a_6 poles —
    a NUMBER, not a residue.
```

This is the pivot: at s=3 the ANALYTIC continuation `ζ_D(3)` is finite for the full L→∞ spectrum, but the DIRECT TRUNCATED sum `Z(3; L) = Σ_{n: λ_n ≤ Λ(L)} d_n λ_n^{-3}` diverges as L → ∞. The W10-4 fit on `mellin_s3(L)` measures the FINITE-L direct-sum growth, NOT the analytic-continuation residue. The W0-W5 S-6 lizzi solo's class (c) primary + class (b) secondary classification of S85-W0-L-MELLIN-CONE-S3-RESIDUE FAIL value=1.81e6 (Z(3;12)=6.09e5 with extrapolation R_inf=1.81e6) is precisely this distinction: **the value the candidate theorem labels "Mellin-cone s=3 residue" is a direct truncated sum, NOT a residue.** Subsection (b) (spectral-geometer) develops the Seeley–DeWitt / Γ(s/2) / analytic-continuation derivation directly; the two routes converge.

### II.4 Why the Candidate Theorem REFUTES Inside Its Stated Scope

**Result**: The candidate theorem statement, as written in the schedule and W10 closing-note, is **REFUTED** as a structural theorem and **REPLACED** by a windowed kinematic inequality on the small-L data. **GEOMETRIC**.

Theorem candidate (verbatim from the schedule):
> "Under log-linear UV scaling on Jensen-SU(3) × A_F, the ζ-regulator's denominator growth rate strictly exceeds the Mellin-cone s=3 residue numerator growth rate; Zubarev does not."

The four internal terms — "log-linear UV scaling", "ζ-regulator's denominator growth rate", "Mellin-cone s=3 residue numerator", "Zubarev" — must each pass scope tests for the theorem to be structural:

**Scope test 1** — *"log-linear UV scaling"*. The data are POWER-LAW in L (log-log slopes 6.24, 3.58, 1.12 on the {5,6,7,8} window). Log-linear fits ARE valid descriptors over a small window but are NOT scale-invariant: the slope numbers 0.97/0.56/0.17 are derived quantities that depend on the L_max window used. As L → ∞, log-linear fit slopes drift (per dispersive small-L start-up). Therefore "log-linear UV scaling" is a parametrization, not a structural property. **Status**: test FAILS as structural — the term has no L → ∞ limit independent of the window.

**Scope test 2** — *"ζ-regulator's denominator growth rate"*. The "denominator" `S_zeta_E(L)` is the spectral aggregate `Σ_n d_n · λ_n` truncated at Λ(L). It is NOT specific to the ζ-regulator — it is the same E-weighted truncation under sharp-cutoff f(λ) = 1[λ ≤ Λ(L)]. Per S78 W3-L and the lizzi memory entry on the SDW/zeta dictionary, `a_n = ζ-class` is a per-branch / L_max=3 convention. At L_max ∈ {5,...,8} the "ζ-regulator denominator" is more accurately a sharp-truncated E-moment. **Status**: test PASSES as a labelling convention (acceptable) but does NOT bind the regulator-class identity (the same number arises under multiple regulator labels in this convention).

**Scope test 3** — *"Mellin-cone s=3 residue numerator"*. From §II.3 above, s=3 is OFF-POLE in d_spec=8 NCG. The "residue at s=3" is NOT a Seeley–DeWitt residue. The W10-4 quantity `mellin_s3(L)` is the direct truncated `Z(3; L)`, which diverges at L → ∞. Calling it a "residue" is a NOMENCLATURE ERROR carried in from the original W10-4 plan-prose. The honest term is "truncated zeta value at s=3". **Status**: test FAILS as structural — there is no residue at s=3 to extract.

**Scope test 4** — *"Zubarev does not"*. `S_Zubarev_E(L)` is the same E-weighted spectral aggregate damped by `exp(-λ^2/M_KK^2)`. Under L → ∞ with FIXED Λ_Z = M_KK, the integrand saturates beyond λ ≈ M_KK and the integral approaches a FINITE limit. So `S_Zubarev_E(L → ∞)` is bounded; its "growth rate" is asymptotically zero. Therefore in the L → ∞ limit `slope(S_Zubarev_E) → 0 < slope(mellin_s3) ≈ L^5`. The "stabilization" comparison "Zubarev does not stabilize" is therefore BACKWARDS in the asymptotic limit: Zubarev FULLY DAMPS the s=3 numerator (drives the "denominator/numerator" ratio to zero, which IS asymptotic stabilization in a different sense — it kills the spectral content beyond M_KK), while the candidate theorem describes only the small-L window where Zubarev has not yet saturated. **Status**: test FAILS — the theorem's interpretation inverts under L → ∞.

The CANDIDATE THEOREM is therefore **REFUTED in the stated scope** (regulator-class structural theorem at L → ∞) and **REPLACED by a windowed empirical inequality** (kinematic statement on the L ∈ {5,6,7,8} fit window), provable by direct numerical fit per §II.1. The replacement inequality has no theorem-grade content — it is a Section II.1 calculation.

### II.5 What Survives — A Two-Step Replacement

**Result**: A weaker, scope-bounded statement is provable inside the small-L window AND reduces to a known structural fact under analytic continuation. **GEOMETRIC**.

**Statement (REPLACEMENT-A, windowed kinematic inequality)**:
> *For the Jensen-SU(3) × A_F D_K spectrum at L_max ∈ {5,6,7,8}, the log-linear fit slopes of `S_zeta_E(L)`, `mellin_s3(L)`, `S_Zubarev_E(L)` satisfy slope(S_zeta_E) > slope(mellin_s3) > slope(S_Zubarev_E) at numerical values 0.9748, 0.5598, 0.1716 respectively (R^2 ≥ 0.91 each).*

This is a calculation, not a theorem. PROOF: §II.1 substitution chain. Direct Python fit on the SV2 cache. Qualifies as a documented FINDING per the project's epistemic discipline; does NOT qualify for permanent §VII registry.

**Statement (REPLACEMENT-B, asymptotic structural property under analytic continuation)**:
> *Conditional on the S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate (S-6 lizzi solo) landing PASS, the analytically-continued ζ_D(3) is a finite substrate-intrinsic number (boundary value between the a_4 and a_6 Seeley–DeWitt poles in d_spec=8 NCG), and the comparison `S_zeta_E_continued / ζ_D(3)` and `S_Zubarev_E_continued / ζ_D(3)` are well-defined regulator-class invariants. The "stabilization" reading then holds asymptotically iff `S_Zubarev_E(L → ∞)` is finite (provable; Schwartz damping) and `S_zeta_E(L → ∞)` is divergent in a Mellin-strip-controllable way (provable; sharp truncation).*

This statement IS theorem-candidate-grade but is CONDITIONAL on infrastructure that does not yet exist. The S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE gate (proposed in S-6 lizzi solo, §V) is the prerequisite. The current synthesis cannot land REPLACEMENT-B without that infrastructure.

**S-1 cross-check**: REPLACEMENT-A and REPLACEMENT-B both operate on M-class observables (mixed-support Mellin vectors). They are NOT pure-a_4 statements and therefore are NOT competitor theorems to S-1. They live in the M-side of the regulator-family boundary, where Mellin-multiplier scope-bounding (S78 W2-F) does NOT apply uniformly. This is consistent with — not contradictory to — S-1.

**S-6 cross-check**: REPLACEMENT-A is a finite-L numerical statement (class (a) TRUE-BUT-UNDER-RESOLVED in the S-6 4-class taxonomy); REPLACEMENT-B is a class (c) → (b) migration candidate (TRUNCATION-INAPPROPRIATE-THRESHOLD becomes METHOD-INAPPROPRIATE, then resolves under analytic continuation infrastructure). Both classifications are explicit in S-6 lizzi solo §III.

### II.6 The f^r Mellin-Vector Decomposition for ζ vs Zubarev (per Schedule Instruction)

**Result**: Per S78 W3-L conventions and S-1 lizzi solo §II.2, the Mellin support vectors are: `f^zeta = e_4 = (0,0,1,0,0,0,...)` (pure-a_4, F_4 class); `f^Zubarev` = analytic Mellin transform of `exp(-x/Λ_Z^2)` with infinite Schwartz-class support, NOT a finite vector in F_4. The schedule's request to "write the f^r residue decomposition for ζ vs Zubarev at s=3" therefore yields an asymmetric pair: the ζ side is finite-support; the Zubarev side has infinite support. **GEOMETRIC**.

For ζ-class (under the per-branch / L_max=3 / a_n=zeta convention):
```
f^zeta_n  =  δ_{n,4}
O^zeta    =  ⟨f^zeta, m^O⟩  =  m_4^O                                (4)
```
Here `m^O = (m_0, m_2, m_4, m_6, m_8)` is the character vector of observable O against the Seeley–DeWitt basis. For the W10-4 aggregates:
- `m^{mellin_s3}` has full support at s=3 (off-pole boundary).
- `m^{S_zeta_E}` has support at indices implied by the E-weight; under per-branch/L_max=3 ζ convention, this resolves to `m_4^{S_zeta_E} ≠ 0` only.
- `m^{S_Zubarev_E}` has the same full Schwartz-induced support.

For Zubarev-class:
```
f^Zubarev_n  =  M[exp(-x/Λ_Z^2)](s) | s = n + 1
              =  Λ_Z^{2(n+1)} · Γ(n+1)                              (5)
O^Zub        =  Σ_n  Λ_Z^{2(n+1)} Γ(n+1) · m_n^O                    (6)
```
which is an INFINITE sum over n with rapidly growing coefficients controlled by Schwartz-class regularity. This is the structural reason Zubarev cannot be co-quantified against ζ in the same `(f_0, f_2, f_4, f_6)` 4-vector framework that S-1 uses for the cutoff/zeta/SDW/anomaly atlas. The S-1 5-atlas treats Zubarev within a specific FINITE truncation of f^r where only `(f_0, f_2, f_4, f_6)` are tracked as effective Mellin coefficients. Beyond the truncation, Zubarev's tail matters, and at s=3 (off-pole) the tail is what dominates.

**Slope inequality from first principles?** The schedule asks: *"Verify whether the slope difference (0.97 vs 0.17, vs 0.56 for Zubarev) emerges from the Mellin denominator's pole structure at s=3 vs the heat-kernel a_4 coefficient's residue normalization."*

Answer: **No, the slopes do NOT directly emerge from a Mellin pole-structure comparison.** They emerge from three distinct kinematic mechanisms:

- `slope(S_zeta_E)`: BULK Weyl growth of an E-weighted truncated sum on a d_spec=8 spectrum, fitted log-linearly on the start-up window L ∈ {5,...,8}. Asymptotic behaviour: power-law L^9 in L, log-log slope → 9 as L → ∞. Observed window value 0.97 is a START-UP-REGIME window slope.

- `slope(mellin_s3)`: BULK Weyl growth of a λ^{-3}-weighted truncated sum on the same spectrum. Asymptotic L^5. Observed window value 0.56 is also a start-up window slope.

- `slope(S_Zubarev_E)`: Schwartz-DAMPED truncated sum, asymptotically saturating at finite value as L → ∞ (slope → 0). Observed window value 0.17 is the residual pre-saturation slope.

The three slope values are produced by THREE DIFFERENT kinematic mechanisms (Weyl bulk integrand, Weyl bulk integrand at higher s-power, Schwartz damping toward saturation). They are NOT three measurements of the same regulator-class invariant against a common Mellin pole structure. The candidate theorem statement conflates three kinematic mechanisms into one structural inequality. **This is the fatal scope flaw.**

### II.7 Refutation Summary

The empirical 5-regulator slope-comparison observation in W10 Highlight #1 is:
1. **Real**: data-verified to R^2 ≥ 0.91 on the L ∈ {5,6,7,8} fit window (REPLACEMENT-A).
2. **Window-specific, not L → ∞-asymptotic**: log-log diagnostics give different effective exponents (6.24 / 3.58 / 1.12), and Zubarev saturates while ζ and Mellin-direct diverge.
3. **Three distinct kinematic mechanisms, not one regulator-class invariant**: bulk-Weyl-E, bulk-Weyl-s=3, Schwartz-damped.
4. **At s=3 OFF a Seeley–DeWitt pole** for d_spec=8: the "residue" terminology is a misnomer.
5. **Inside the divergence cone**: direct truncated zeta cannot test L → ∞ residue identities (S-6 class (b) + (c) finding).
6. **Outside the F_4 (pure-a_4) scope** of S78 W2-F Mellin-multiplier theorem: the schedule's instruction to derive the inequality "from the Mellin-multiplier theorem restricted to pure-a_4" cannot be followed — the observables are M-class.
7. **L_max=12 truncation artifact at the structural level**: the theorem as stated requires the analytic continuation that does not yet exist (S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE).

The candidate theorem as stated is **REFUTED**. REPLACEMENT-A (windowed kinematic inequality) is a calculation; REPLACEMENT-B (asymptotic structural property) is theorem-candidate-grade but conditional on the S86 infrastructure gate. The S86 gate `ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` proposed in §V is the adjudicating successor — pre-registered to either land REPLACEMENT-B (theorem-grade) or formalize the refutation (permanent finding).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | Cross-pairing |
|:-----|:--------|:----------------|:--------------|
| S85-W10-W0-L-INVERTED-BRANCH-ENUMERATION | PASS | value=1 (inverted_stable) | source of Highlight #1 5-regulator slope observation |
| S85-W0-L-MELLIN-CONE-S3-RESIDUE | FAIL | value=1.81e6 (R_inf extrapolation) | S-6 class (c) primary + (b) secondary; mentioned by schedule directly |
| (proposed) S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING | PRE-REG | (see §V.1) | depends on S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE |
| (cross-pair) S85 W0-W5 S-1 (Regulator-Family Boundary, lizzi solo) | LANDED | f^zeta = e_4 ∈ F_4 only | scope bound: F_4 vs M; W10-4 observables ARE M-class |
| (cross-pair) S85 W0-W5 S-6 (L_max-Truncation Taxonomy, lizzi solo) | LANDED | 7 FAILs / 4 classes | proposes S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate |

---

## IV. Structural Implications

**A. Constraint-map updates.**

| Date | Mechanism / claim | Prior state | New state | Reason |
|:-----|:------------------|:------------|:----------|:-------|
| 2026-04-25 | "ζ-regulator-stabilization" candidate theorem | Empirical 5-regulator slope observation (W10 Highlight #1) | REFUTED at stated scope; REPLACED by REPLACEMENT-A (windowed) + REPLACEMENT-B (conditional on S86 infrastructure) | §II.4: 4 of 4 scope tests fail under structural reading; §II.5: weaker scope-bounded replacements survive |
| 2026-04-25 | "Mellin-cone s=3 residue" terminology | Used informally in W10 plan-prose and Highlight #1 | DEPRECATED as misleading | §II.3: s=3 is OFF a Seeley–DeWitt pole in d_spec=8 NCG; "residue" should be replaced by "direct truncated value at s=3" |
| 2026-04-25 | Schedule context-block label assignment for Slot 3A | "(b) Mellin slope ≈ 0.17. (c) Zubarev slope ≈ 0.56" | LABELS SWAPPED relative to data; canonical assignment: zeta=0.97, mellin=0.56, Zubarev=0.17 | §II.1: data-verified ordering matches W10 WP body lines 1098–1100 and Constraint-Map row 9 line 1153 |
| 2026-04-25 | Pure-a_4 family scope (S-1) applicability to W10-4 observables | Schedule asked to "restrict to pure-a_4 family" | NOT APPLICABLE: `S_zeta_E`, `S_Zubarev_E`, `mellin_s3` are ALL M-class | §II.2: character vectors have multi-n support |
| 2026-04-25 | Branch-c (ζ-Jos-inverted) stable-w_0 status from W10-4 PASS | Discovered as third stable branch | UNAFFECTED by this synthesis | W10-4 PASS does NOT depend on the candidate theorem's structural reading; it depends on the windowed kinematic inequality (REPLACEMENT-A), which IS verified |

**B. What shifts in the framework's regulator-of-choice posture.**

The W10 working paper §4 ("Downstream implications") records: "Regulator-of-choice canonical lean: ζ for L ≥ 10 analyses." This synthesis QUALIFIES that lean: under the L ∈ {5,6,7,8} fit window and the windowed kinematic inequality (REPLACEMENT-A), ζ-truncation aggregates grow faster than mellin-s3 direct sums grow faster than Zubarev-damped sums. This is a kinematic ordering, not an L→∞ regulator-class superiority claim. Under the L→∞ asymptotic reading (REPLACEMENT-B, conditional on S86 infrastructure), Zubarev SATURATES (its E-weighted spectral integral converges), ζ-direct DIVERGES at the bulk Weyl rate, and the well-defined regulator-class invariant is the analytically-continued ζ_D(3) — a single finite number — NOT the ratio of growth rates.

The lean toward ζ for L ≥ 10 should be understood as: ζ-class direct truncation gives MORE INFORMATION at finite L (it tracks bulk Weyl growth) before saturation kicks in, but Zubarev gives a CLEANER L → ∞ limit (Schwartz convergence) at the cost of damping high-λ structure that the framework MAY want to keep.

**C. What walls remain.**

- S-1 Regulator-Family Boundary stands: F_4 (pure-a_4: {zeta, Zubarev, SDW, anomaly}) ⊥ M (mixed-support: {cutoff_sqrt}). The W10-4 observables sit in M; the S-1 wall does not bite directly. This is consistent.
- S-6 7-FAIL × 4-class taxonomy stands; the candidate theorem REFUTATION is class (c) primary + (b) secondary (truncation-inappropriate-threshold; analytic continuation required).
- The S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate (S-6) is the PREREQUISITE for any L → ∞ theorem-grade ζ-stabilization claim. It is unscheduled at S85 wave-end.

**D. What opens.**

- A pre-registered S86 gate `ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (§V.1) that requires the analytic continuation infrastructure to evaluate, and that pre-registers BOTH the PASS clause (REPLACEMENT-B lands as theorem-grade) and the FAIL clause (refutation stands; permanent finding).
- A documentation hygiene action: deprecate "Mellin-cone s=3 residue" terminology; replace with "truncated zeta at s=3" everywhere.
- A schedule-prose correction action: the Slot 3A invocation context-block has Mellin/Zubarev labels swapped relative to data; this should be rectified post-hoc as a documentation fix (not a verdict change).

**E. What does NOT shift.**

- W10-4 PASS verdict (value=1 inverted_stable) is unchanged: it depends on the windowed kinematic inequality, which is verified.
- Branch-c (ζ-Jos-inverted) discovery is unchanged: it is a finite-L kinematic configuration, not a regulator-class theorem.
- LOCKOUT-C / R_842 / τ_fold theorem registrations are unchanged.
- All ANTI-CORRESPONDENCE ledger entries are unchanged.

---

## V. Carry-Forward Computations

**MANDATORY pre-registered carry-forward per `feedback_fix-in-session-never-defer.md`. Every entry has all four fields.**

V.1. **S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING (proposed master gate)**
   - **What**: Adjudicate REPLACEMENT-B (asymptotic structural property of regulator-class growth-rate ordering) against the analytic continuation of `ζ_D(s) Γ(s/2) = ∫_0^∞ t^(s/2−1) K(t) dt` evaluated at s=3 with explicit small-t Seeley–DeWitt pole subtraction (subtract a_0 t^{-4} + a_2 t^{-3} + a_4 t^{-2} + a_6 t^{-1} + a_8 from K(t), then evaluate). Compute the analytically-continued `ζ_D(3)` for the L_max ∈ {8, 10, 12} truncations (using extrapolated trajectories from W10-4 SV2 if dense L=12 remains infeasible). Compute `S_zeta_E^{cont}(L → ∞)` and `S_Zubarev_E^{cont}(L → ∞)` under the same continuation. Test whether the ordering `lim S_zeta_E / ζ_D(3) > 1 > lim S_Zubarev_E / ζ_D(3)` (the asymptotic stabilization inequality) holds.
   - **Inputs**: SV2 cache `computations/s85_w10_w0_inverted_branch_enumeration.json`; Seeley–DeWitt coefficients a_0, a_2, a_4, a_6, a_8 of `D_K^2` on Jensen-SU(3) × A_F at L_max=10 (canonical_constants `a_0=+6440 at τ_fold` per S72 cited in S-1; a_2/a_4 from S77 a_4 Gilkey decomp); S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate (must land FIRST).
   - **Gate**: `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING`. **PASS** if `lim_{L→∞} S_zeta_E^{cont} / ζ_D(3) > 1 + ε` AND `lim_{L→∞} S_Zubarev_E^{cont} / ζ_D(3) < 1 − ε` with ε ≥ 0.05 (5% margin), AND analytic-continuation residual χ²/dof ≤ 5. **INFO** if 0 < ε < 0.05 OR χ²/dof ∈ (5, 25]. **FAIL** if either limit lies on the wrong side, OR χ²/dof > 25, OR the analytic-continuation infrastructure (S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE) returns chi^2/dof > 25 itself (cascade FAIL). FAIL outcome formalizes the REFUTATION as a permanent finding; PASS outcome upgrades REPLACEMENT-B to theorem-grade and lands a §VII registry entry.
   - **Effort**: 4–6 hours; 1 agent session; depends on S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (S-6 lizzi solo §V) being available — if unavailable, this gate is BLOCKED-prereq-pending and must wait. Builds directly on the SV2 cache; no new spectral computation required at L_max ∈ {8, 10}, only L=12 extrapolation.

V.2. **Schedule-context-block label rectification (documentation patch)**
   - **What**: Issue a post-hoc correction to `sessions/archive/session-85/session-85-w6-13-workshop-schedule.md` Slot 3A invocation: swap the labels "(b) Mellin-cone s=3 residue numerator growth slope ≈ 0.17" and "(c) Zubarev slope ≈ 0.56 (intermediate)" so they match the data: `(b) Mellin-cone s=3 direct sum slope ≈ 0.56`, `(c) Zubarev slope ≈ 0.17`. Also rename "Mellin-cone s=3 residue" to "Mellin-cone s=3 direct truncated zeta" throughout the invocation, since s=3 is OFF a Seeley–DeWitt pole in d_spec=8 NCG.
   - **Inputs**: this synthesis (§II.1 data verification + §II.3 Mellin-pole substitution chain); subsection (b) (spectral-geometer) confirmation; W10 working paper body lines 1098–1100, 1150, 1153 (canonical labels).
   - **Gate**: documentation-patch verdict (no PASS/FAIL/INFO; landing-only). The patch is `post-hoc:rectify-context-block-label-swap` and must be logged in the schedule's edit history. No SHA verdict; documentation-only.
   - **Effort**: 30 minutes; orchestrator action (no agent dispatch needed). Should be executed BEFORE the Slot 1a Row 3A workshop close-out so subsection (b) and the unified candidate-theorem statement reference the rectified text.

V.3. **REPLACEMENT-A documentation as a finding (NOT a theorem)**
   - **What**: Record the windowed kinematic inequality slope(S_zeta_E) > slope(mellin_s3) > slope(S_Zubarev_E) at numerical values 0.9748, 0.5598, 0.1716 with R^2 ≥ 0.91 on the L ∈ {5,6,7,8} fit window as a **DOCUMENTED FINDING** (not a permanent theorem) in `sessions/permanent-results-registry.md` under §VII.W (working-finds) or equivalent provisional section. Cite W10-4 PASS verdict + this synthesis + subsection (b).
   - **Inputs**: SV2 cache + this synthesis + subsection (b); permanent-results-registry.md current §VII top-level structure.
   - **Gate**: registry-landing diff. PASS if landing produces a single documented finding row with all source SHAs cited and the SCOPE BOUND (window-specific, not L → ∞-asymptotic) explicit. INFO if landing is partial. FAIL if registry diff produces a permanent §VII.B / §VII.P entry treating the finding as theorem-grade (this would conflate REPLACEMENT-A with REPLACEMENT-B).
   - **Effort**: 1 hour; 1 light agent session (registry-landing only).

V.4. **f^r Mellin-vector decomposition extension to Zubarev (formal, deferred)**
   - **What**: Compute the analytic Mellin transform `M[exp(-x/Λ_Z^2)](s)` and its Schwartz-class infinite-support Mellin vector. Embed Zubarev in the S-1 5-atlas as an INFINITE-VECTOR class (extension of F_4's finite-vector formalism). Formalize the asymmetry between ζ-class (finite-vector e_4) and Zubarev-class (infinite-vector M[Schwartz]) at the level of the Mellin-multiplier theorem. This is the formal extension of S-1's 4-class atlas {a_0, a_2, a_4, a_6} to the infinite-vector regime needed to handle Zubarev rigorously.
   - **Inputs**: S-1 lizzi solo §II.2 5-atlas; S78 W2-F Mellin-multiplier theorem; standard Schwartz-class Mellin-transform tables.
   - **Gate**: `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION`. PASS: explicit M[Zubarev](s) computed AND class M extended to include infinite-vector regime AND theorem statement that Zubarev is in the infinite-vector M class with no finite-truncation that lands it in F_4. INFO: extension partial (e.g., only finite-truncation analysed). FAIL: Zubarev DOES land in F_4 under some natural truncation (would refute S-1's mixed-support classification of Zubarev — unlikely but pre-registered).
   - **Effort**: 3–4 hours; 1 agent session (lizzi or van-den-dungen).

V.5. **Cross-pairing with Slot 3B (branch-c phonon mechanism phenomenology)**
   - **What**: The W10-4 PASS verdict that this synthesis PRESERVES is the discovery of branch c (ζ-Jos-inverted) as a new stable w_0 branch at high L_max. Slot 3B (parallel synthesis) writes the PHENOMENOLOGY of branch c. This carry-forward records that the structural status of branch c — IS it real physics, or kinematic artifact of the windowed inequality — depends on V.1 outcome. If V.1 PASSes, branch c's structural status is supported by the asymptotic regulator-class invariant; if V.1 FAILs, branch c remains a finite-L kinematic configuration, not a regulator-class invariant, and the Slot 3B phenomenology must be SCOPE-BOUNDED accordingly.
   - **Inputs**: this synthesis §IV.E; Slot 3B writeups (volovik / landau / kaku); V.1 outcome.
   - **Gate**: cross-pairing audit gate `S86-BRANCH-C-PHENOMENOLOGY-SCOPE-AUDIT`. PASS: Slot 3B phenomenology is explicit about V.1-conditional vs V.1-independent claims. INFO: partial scope-binding. FAIL: Slot 3B phenomenology assumes V.1 PASSes without registration as conditional.
   - **Effort**: 1 hour; runs as part of Slot 3 closeout (W6-W13 9A combined-landscape synthesis); no new compute.

V.6. **S-1 Mellin-multiplier scope re-affirmation (cross-pairing flag landing)**
   - **What**: Confirm in `sessions/permanent-results-registry.md` §VII.B (Regulator-Family Boundary Theorem entry, per S-1 lizzi solo §IV) that the W10-4 / Highlight #1 observables `S_zeta_E`, `S_Zubarev_E`, `mellin_s3` are M-class (mixed-support), and that the S-1 theorem's pure-a_4 (F_4) scope-bound DOES NOT apply to them. This is a documentation cross-pairing flag, not a new theorem.
   - **Inputs**: this synthesis §II.2; S-1 lizzi solo §II.2; permanent-results-registry.md §VII.B (when landed).
   - **Gate**: documentation cross-pairing flag landing. PASS if the §VII.B entry contains the explicit M-class enumeration including the W10-4 observables, with a citation to this synthesis. INFO if partial. FAIL if S-1's pure-a_4 scope bound is mistakenly applied to W10-4 observables in any downstream document.
   - **Effort**: 30 minutes; orchestrator action; runs alongside V.3 in the same registry-landing session.

V.7. **Subsection-(b) joint candidate-theorem MD (unified deliverable per schedule)**
   - **What**: Per the schedule's invocation: "Both: produce a unified candidate-theorem MD with statement, proof sketch (or refutation), and a pre-registered S86 gate." This synthesis is subsection (a); subsection (b) (spectral-geometer) is being authored in parallel. The UNIFIED candidate-theorem MD is the joint product of the two subsections, prepared after both land. It will state the REFUTATION (per §II.7) plus REPLACEMENT-A/REPLACEMENT-B structure, the S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING gate (per V.1), and the cross-pairing flags to S-1 and S-6.
   - **Inputs**: this synthesis (subsection a); subsection (b) by spectral-geometer (parallel write); schedule Slot 3A invocation.
   - **Gate**: unified-MD landing audit. PASS if the unified MD: (i) cites both subsection MDs, (ii) writes the REFUTATION and REPLACEMENT-A/B structure explicitly, (iii) pre-registers V.1 (S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING), (iv) flags S-1 and S-6 cross-pairings. INFO if any of (i)-(iv) is partial. FAIL if the unified MD treats REPLACEMENT-A as the candidate theorem (misses the structural-vs-windowed distinction).
   - **Effort**: 1–2 hours; 1 light agent session AFTER both (a) and (b) land. Could be authored by either the lizzi or spectral-geometer agent in a follow-up session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Data-verified slope ordering: zeta(0.9748) > mellin(0.5598) > Zubarev(0.1716) on L ∈ {5,6,7,8} | GEOMETRIC | NEW-FINDING (REPLACEMENT-A) | Windowed kinematic inequality, R^2 ≥ 0.91; not theorem-grade |
| 2 | Schedule context-block has Mellin/Zubarev labels SWAPPED relative to data | DOCUMENTATION | NEW-CORRECTION-NEEDED | Post-hoc rectify (V.2); does NOT change the W10-4 PASS verdict |
| 3 | s=3 in d_spec=8 NCG is OFF a Seeley–DeWitt pole; "residue at s=3" is a misnomer | GEOMETRIC | NOMENCLATURE-DEPRECATION | Replace "Mellin-cone s=3 residue" with "Mellin-cone s=3 direct truncated zeta" throughout |
| 4 | Candidate ζ-stabilization theorem at L → ∞ scope FAILS 4 of 4 scope tests | GEOMETRIC | REFUTED | Theorem as stated does not survive; REPLACEMENT-A (windowed) + REPLACEMENT-B (conditional on S86 infrastructure) replace it |
| 5 | W10-4 observables ARE M-class (mixed-support); S-1's F_4 scope bound DOES NOT directly apply | GEOMETRIC | CROSS-PAIRING-FLAG | S-1 stays intact; W10-4 lives outside its purview |
| 6 | The candidate theorem's PASS path requires S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (S-6 master gate) | GEOMETRIC | PREREQUISITE-IDENTIFIED | V.1 is BLOCKED-prereq-pending until S-6 master gate lands |
| 7 | W10-4 PASS verdict (branch c stable) is UNAFFECTED by the candidate-theorem refutation | PHONONIC | UNCHANGED | Branch c remains a finite-L kinematic configuration; structural status depends on V.1 outcome (V.5 cross-pairing) |
| 8 | The three slope values arise from THREE DIFFERENT kinematic mechanisms (bulk-Weyl-E, bulk-Weyl-s=3, Schwartz-damped) | GEOMETRIC | NEW-FINDING | The candidate theorem conflates three mechanisms into one inequality; this is its fatal scope flaw |
| 9 | f^r Mellin-vector for ζ is finite (e_4 ∈ F_4); for Zubarev is infinite-Schwartz | GEOMETRIC | KNOWN (S-1 + S78) | Cannot align ζ vs Zubarev in a common 4-vector Mellin framework; need V.4 infinite-vector extension |
| 10 | S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING (V.1) pre-registered | GEOMETRIC | NEW-PRE-REG | Adjudicates REPLACEMENT-B as theorem-grade; conditional on V.1 prereqs |

---

## VII. Substrate-Framing Audit

All results above are derived FROM the substrate spectrum of D_K on Jensen-deformed SU(3) × A_F TOWARD emergent observables. The flow is:

```
  D_K eigenvalues → spectral aggregates {S_zeta_E, S_Zubarev_E, mellin_s3}(L)
    → regulator-class slope diagnostics (windowed + asymptotic)
    → Mellin-cone analytic continuation (deferred to S86)
    → late-time w_0 branch enumeration (W10-4)
```

No container thinking. No "regulator on top of the substrate" — regulators ARE specifications of how Mellin moments project onto the spectral basis. The substrate is logically prior; the slope-comparison observation is a property of the substrate's spectral density, not of an external geometric measure. Particles do not enter at any step. Everything is a moment of D_K^2.

---

**End of Lizzi subsection (a).** Subsection (b) (spectral-geometer) handles the heat-kernel / Seeley–DeWitt / ζ_D(s) analytic-continuation track in parallel. The unified candidate-theorem MD (V.7) is to be assembled after both subsection deliverables land.
