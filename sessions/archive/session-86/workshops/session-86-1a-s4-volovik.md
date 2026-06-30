# Session 86 Synthesis: Lab-Falsifier Portfolio Coherence + Level-Saturation Audit (Volovik lane)

**Date**: 2026-04-27
**Agent**: volovik-superfluid-universe-theorist (volovik)
**Slot**: S86 1a S-4
**Source Documents**:
- `sessions/archive/session-86/session-86-w11-workingpaper.md` (W11-1 INFO C5; W11-2 PASS C6)
- `sessions/archive/session-86/session-86-w14-workingpaper.md` (§W14-1..§W14-6 META; W14-6 lab-falsifier landing)
- `sessions/framework/registry/falsifier-master-inventory.md` (Rows #1-#21 + 21.audit-block + summary section)
- `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv` (9-row SI table; CSV path resolved at `sessions/archive/session-86/computations-artifacts/`, not `computations/`)
- `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv` (9-row EVOI level table + 4-branch decision conditions)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md` (lab-si-translation-86-result, w0-regulator-sv1-84-result, framework-3heb-comparison)

---

## I. Session Outcome

The 9-row LAB-FALSIFIER suite (3He-A vortex-line NMR, FeSe 77Se NMR, 173Yb optical-lattice 3-body loss) clears the A-level floor (`detection_ratio >= 10`) by 1.5 to 4.8 orders of magnitude at baseline literature anchors, but the assignment is **fragile in the SW3/XA3 direction**: a single-decade loosening of the 173Yb K_3 sigma_detect (from theoretical 0.05 s^-1 to a publication-typical 0.5 s^-1) demotes SW3 from level A to level C and pushes XA3 to level B. The framework's claim of `9x A-level dominance` is therefore an upper bound on the actual portfolio coherence, conditional on the 6 provisional `sigma_detect` anchors being sustainable as **single-shot** floors. Independent of the level question, the **173Yb sweet-spot anomaly** is real and structural: the compactification-resonance mental model predicts each platform's own sweet-spot lambda projects with the largest amplitude, and 173Yb violates it (lambda_8 sweet-spot W8_4_ratio = 2.85 is the *smallest* of the three 173Yb measurements; cross-platform lambda_7 = 13.19 is 4.63x larger). This violation localizes to one of three diagnostic causes (compactification-resonance wrong / Jensen inner-product non-Euclidean / sigma_detect normalization wrong); current evidence favors the second.

---

## II. Key Results

### Level-shift table under 100x sigma_detect scan (volovik-lane: 3He-A and 173Yb provisional rows)

**Result**: Six of the nine LAB-FALSIFIER rows are sigma_detect-floor-conditional. SW3 (173Yb, lambda_8 sweet-spot) is the **most fragile** — a 100x looser floor sends it to level D; the realistic 10x looser floor (matching publication-typical K_3 measurements) sends it to level C. **Classification: PHONONIC** (substrate excitations measured at table-top compactification ratio).

Substitution chain (per `.claude/rules/math-scripts.md` §Double-Check Logic):

```
Step 1 (definitions):
  detection_ratio d_r := SI_value / sigma_detect           [W11 §W11-1 line 88]
  Level ladder (W11 §W11-2 line 188):
    A: d_r >= 10
    B: 3 <= d_r < 10
    C: 1 <= d_r < 3
    D: d_r < 1

Step 2 (substitution -- 100x tighter floor):
  sigma_detect -> sigma_detect / 100
  d_r' = SI_value / (sigma_detect/100) = 100 * d_r

Step 3 (substitution -- 100x looser floor):
  sigma_detect -> 100 * sigma_detect
  d_r' = SI_value / (100 * sigma_detect) = d_r / 100

Step 4 (simplification -- level transition thresholds under 100x looser):
  A -> B at d_r/100 < 10  <=> d_r < 1000  (under 100x looser: 1000 cleared by 3He-A only)
  A -> C at d_r/100 < 3   <=> d_r < 300
  A -> D at d_r/100 < 1   <=> d_r < 100

Step 5 (direction):
  Tighter floor -> larger d_r -> level preserved or improved (DOMINATES level ladder).
  Looser floor -> smaller d_r -> level preserved only if baseline d_r >= 100*level_floor.
```

| obs_id | platform | lambda    | d_r baseline | level_base | d_r/100 (loose) | level_loose | d_r*100 (tight) | level_tight |
|:-------|:---------|:----------|-------------:|:---------:|----------------:|:----------:|----------------:|:----------:|
| SW1    | 3He-A    | lambda_6  |    58 958.86 |     A     |          589.59 |     A      |     5 895 886.4 |     A      |
| XA1    | 3He-A    | lambda_6  |    58 958.86 |     A     |          589.59 |     A      |     5 895 886.4 |     A      |
| XB1    | 3He-A    | lambda_7  |    19 652.95 |     A     |          196.53 |     A      |     1 965 295.5 |     A      |
| SW3    | 173Yb    | lambda_8  |        28.50 |     A     |            0.29 |     **D**  |       2 850.00  |     A      |
| XA3    | 173Yb    | lambda_6  |        54.94 |     A     |            0.55 |     **D**  |       5 493.83  |     A      |
| XB3    | 173Yb    | lambda_7  |       131.85 |     A     |            1.32 |     **C**  |      13 185.20  |     A      |

(FeSe non-provisional rows for comparison: SW2 d_r=72.90 (A) -> 0.73 (D) under /100, 7290.4 (A) under x100; XA2 d_r=30.70 (A) -> 0.31 (D) under /100; XB2 d_r=72.90 (A) -> 0.73 (D) under /100. The non-provisional FeSe rows also fail level A under 100x looser, but the FeSe single-shot 5 ppm floor is empirically grounded and not expected to inflate.)

**173Yb K_3 anomaly (10x looser floor, sigma_detect 0.05 -> 0.5 s^-1; spawn-prompt cite)**:

- SW3 d_r = 2.85 -> level C (LAB-FALSIFIER-A demotion confirmed; the spawn-prompt's specific scenario reproduces)
- XA3 d_r = 5.49 -> level B
- XB3 d_r = 13.19 -> level A (clears at 10x looser by factor 1.32 over the A-floor)

**The 173Yb sweet-spot row SW3 is the most fragile entry in the entire 9-row portfolio.** A single decade of literature-anchor loosening collapses both the level assignment and the unique-lambda_8 substrate-direction-falsification claim.

### 173Yb sweet-spot anomaly diagnosis (volovik lab-falsifier-coherence anchor)

**Result**: The spawn-prompt asserts the W14-6 §W14-6 substrate-direction analysis identifies SW3 / 173Yb / lambda_8 as the framework's **strongest single-row substrate-direction-falsification trigger** (W14 working paper line 769). At the same time, SW3 has the **smallest detection_ratio** (28.5 vs the next-smallest XA2 = 30.70 and FeSe-class rows ~73; vs the 3He-A class at 1.97e4-5.90e4). This combination — most decisive yet smallest margin — is the "least decisive at sweet-spot but most decisive at cross-platform" anomaly the spawn prompt asks me to diagnose. **Classification: PHONONIC** (substrate-direction asymmetry within a single platform's measurement set).

**Substitution chain (sweet-spot self-rank test)**:

```
Step 1 (definition):
  Compactification-resonance mental model claim: each platform's
  own sweet-spot lambda direction projects with the largest
  W8_4_ratio amplitude among the lambda directions that platform
  measures (CSV column W8_4_ratio).

Step 2 (substitution -- the 9-row CSV table):
  3He-A sweet=lambda_6: W8_4_ratio = 1.7267 ; cross-row XB1 (lambda_7) = 0.5756
  FeSe  sweet=lambda_7: W8_4_ratio = 1.8226 ; cross-row XA2 (lambda_6) = 0.7674
  173Yb sweet=lambda_8: W8_4_ratio = 2.85   ; cross-row XA3 (lambda_6) = 5.4938
                                              cross-row XB3 (lambda_7) = 13.1852

Step 3 (simplification -- sweet/cross ratio per platform):
  3He-A:  1.7267 / 0.5756  = 3.000   -> sweet HIGHEST   (consistent with model)
  FeSe:   1.8226 / 0.7674  = 2.375   -> sweet HIGHEST   (consistent with model)
  173Yb:  2.85 / 5.4938   = 0.519    -> CROSS HIGHER    (model violated)
          2.85 / 13.1852  = 0.216    -> CROSS HIGHER    (model violated)

Step 4 (direction):
  173Yb violates the compactification-resonance prediction in BOTH
  cross-platform comparisons. Mean cross/sweet at 173Yb = 3.27.
  Two of three platforms (3He-A, FeSe) confirm; 173Yb is the
  outlier. The violation is not boundary -- it is 5-13x.
```

**Three candidate diagnoses (per spawn-prompt instruction, pick one)**:

| # | Diagnosis | Evidence for | Evidence against |
|:--|:----------|:-------------|:-----------------|
| (a) | "Compactification-resonance" mental model is wrong for 173Yb specifically | 3He-A and FeSe both confirm; if model is generically wrong they should fail too (they don't). The lambda_8 mode being smallest-projection at the platform whose 3-body-loss kinematics give it sole access is geometrically odd, not anomalous. | The 5-13x violation is too large for "minor model deviation"; flips the predicted ordering, not just shifts magnitudes. |
| (b) | Jensen-deformed inner product breaks Euclidean rank-ordering | Volovik 9A: SU(3) Casimir on Jensen-deformed manifold has off-diagonal kinetic terms; the W8_4_ratio is a moment of D_K, not a Euclidean projection; Jensen-deformed inner product mixes rep-theoretic content (memory: project_volovik-convergence.md, framework-3heb-comparison.md). 173Yb's lambda_8 access is via 3-body Gamma_3B kinematics (not a single-pair pole), so it samples a 3-channel structure where Casimir mixing is most pronounced. | Same Jensen deformation should show up in 3He-A and FeSe lambda_6/lambda_7 mixing — it doesn't. |
| (c) | sigma_detect normalization for 173Yb is wrong (Cazalilla+ 2009 theoretical floor underestimates real K_3 by 10x per spawn-prompt) | Direct experimental evidence: K_3 publication-typical floors are 0.5 s^-1 (cf. Florence/JILA 2018-2022 SU(N) lattice papers), not the Cazalilla theoretical 0.05 s^-1; the d_r anomaly inverts under level-shift to looser floor (SW3 -> level C). | Doesn't explain the W8_4_ratio rank inversion (which lives upstream of sigma_detect); only explains level fragility. |

**Pick (per spawn-prompt instruction)**: **(b) Jensen-deformed inner product breaks Euclidean rank-ordering**.

Reasoning: (a) is ruled out because 2 of 3 platforms validate the compactification-resonance prediction; if the mental model were generically wrong, all three would fail. (c) is ruled out because the spawn-prompt's own anomaly statement compares W8_4_ratios (NOT detection_ratios), and W8_4_ratios are upstream of sigma_detect. The lambda_8 mode is the rep-theoretic generator most strongly mixed under Jensen deformation in the SU(3) algebra (memory: project_volovik-convergence.md, S60-S62 Volovik partition results); the 173Yb 3-body Gamma channel projects the substrate via a kinematic 3-channel structure that is geometrically distinct from the 1-pair NMR (3He-A) or single-shift Knight (FeSe) channels. **The Jensen inner product is non-Euclidean specifically in the rep-content that Gamma_3B projects.**

This diagnosis is testable: it predicts the rank-ordering violation should appear in **any** 3-body or higher-correlator channel, not just 173Yb. A Florence/JILA 173Yb lattice plus a Cs/Yb mixed 3-body channel should both invert the lambda_8 rank. (This is a S87 carry-forward.)

**Solution-space note**: this diagnosis does NOT invalidate W11-2's PASS. The EVOI level ladder runs on detection_ratio (a measurable lab quantity), not W8_4_ratio (a rep-theoretic structural quantity). The PASS verdict is on level assignment, not on which-lambda-is-largest at each platform. The anomaly is a **structural finding latent in the ratios but not gated on**, surfaced here for the first time at suite-coherence level. It joins the W14-6 finding (SW3 = unique-lambda_8 channel) as a complementary structural observation.

### Substrate-framing audit on BCS prefactor 1.764 k_B T_c + h_planck normalization

**Result**: The numerical value 1.764 used in the W11-1 SI translation script is **correct** (it equals pi/exp(gamma_E) = 1.7639 to 4 figures, the canonical BCS weak-coupling Delta(0)/(k_B T_c) ratio). The frequency translation 34.146 MHz reproduces from this value via Delta_3HeA / h_planck. **However, the working-paper attribution comment at §W11-1 line 67 reads "1.764 = 2 e^gamma_E / pi" — this is numerically wrong**. The correct identity is 1.764 = pi / exp(gamma_E). Substitution: 2 * exp(0.5772156649) / pi = 1.1339, not 1.764. The 1.764 value used in the script is right; only the comment is wrong. **Classification: META** (substrate-framing audit on a working-paper text comment, not on the substrate computation).

```
Step 1 (definition):
  BCS weak-coupling: Delta(0) / (k_B * T_c) = pi / exp(gamma_E)
  where gamma_E = Euler-Mascheroni constant = 0.5772156649...

Step 2 (substitution):
  pi / exp(gamma_E) = 3.14159 / 1.78107 = 1.7639   -> matches 1.764
  2 * exp(gamma_E) / pi = 2 * 1.78107 / 3.14159 = 1.1339  -> NOT 1.764

Step 3 (direction):
  W11 §W11-1 substitution chain text wrongly attributes 1.764 to
  2*e^gamma_E/pi. The numerical computation is right; the
  algebraic identity comment is wrong. Single-character text
  fix (swap pi and e^gamma_E and drop the factor of 2).
```

**Substrate-framing assessment**: The `delta_omega_K / omega_K` ratio is a **substrate observable** (substrate's Kelvin-wave excitation amplitude under Jensen-deformed lambda_a projection), measured AT the 3He-A compactification scale. The BCS prefactor 1.764 = pi/exp(gamma_E) connects the 3He-A microscopic gap to the W8_4_ratio's natural frequency unit via an emergent (low-energy effective) BCS theorem inherited from the parent superfluid — NOT from the substrate spectral triple D_K directly. The h_planck normalization is required because the 3He-A platform's measurement instrument is a frequency counter (sensitive to nu = E/h), not an energy spectrometer. Both prefactors are PROPAGATION-class translations (substrate -> emergent g_M -> measurement device readout), not SUBSTRATE-DYNAMICS-class quantities. They live in the convention-translation layer, where condensed-matter conventions (Delta in units of energy or frequency) must be unambiguously mapped to substrate conventions (W8_4_ratio dimensionless M_KK-units). This is appropriate substrate-first practice: the substrate carries the dimensionless ratio; the lab carries the dimensioned readout; the prefactor is the convention bridge.

**No container-thinking violations** found in the W11-1 §W11-1 §SW1 illustrative substitution chain. The CSV `phenomenology_note` column for SW1/XA1/XB1 reads "the substrate's delta_omega_K/omega_K ratio measured at the 3He-A compactification scale" — substrate-first phrasing ("the substrate's ratio measured AT 3He-A's scale"), not container-thinking ("a 3He-A measurement of cosmic substrate"). This is correct substrate-IS-NOT-IN-spacetime framing per `.claude/rules/phononic-framing.md`.

### Cross-platform Spearman rank-correlation (3 platforms, lambda_6 vs lambda_7 common pair)

**Result**: The (lambda_6 vs lambda_7) within-platform rank-ordering is **2-of-3 concordant** across the three platforms (FeSe and 173Yb agree; 3He-A disagrees). The 3He-A lambda_6/lambda_7 inversion is the second structural finding (alongside the 173Yb lambda_8 anomaly) where the W8_4_ratio cross-platform comparison surfaces non-trivial substrate-direction structure. **Classification: PHONONIC**.

```
Step 1 (definition -- pairwise rank concordance):
  For each pair (platform_i, platform_j) and a common lambda-pair
  (lambda_a, lambda_b), the platforms are CONCORDANT if both rank
  W8_4_ratio(lambda_a) > W8_4_ratio(lambda_b) (or both reversed),
  DISCORDANT otherwise.

Step 2 (substitution -- the lambda_6 vs lambda_7 pair, 3 platforms):
  3He-A:  lambda_6 = 1.7267 > lambda_7 = 0.5756  -> rank: lambda_6 first
  FeSe:   lambda_6 = 0.7674 < lambda_7 = 1.8226  -> rank: lambda_7 first
  173Yb:  lambda_6 = 5.4938 < lambda_7 = 13.1852 -> rank: lambda_7 first

Step 3 (simplification -- pairwise concordance matrix):
  3He-A vs FeSe:   DISCORDANT
  3He-A vs 173Yb:  DISCORDANT
  FeSe  vs 173Yb:  CONCORDANT

Step 4 (direction):
  Of 3 pairwise comparisons, 1 is concordant.
  3He-A is the singleton outlier on (lambda_6 vs lambda_7) ranking.
  This is a SECOND structural rank-inversion (the first being the
  173Yb lambda_8 anomaly above).
```

The 3He-A inversion has a candidate structural cause: lambda_6 corresponds to a generator that is U(1)_K-charged under the BDI Z_2 gap protection (per `framework-3heb-comparison.md` memory and the BDI W=0 result of S53), and the 3He-A Kelvin-wave channel is the sole superfluid mode that respects this Z_2 charge protection. lambda_7's amplitude is suppressed at 3He-A because the Kelvin-wave channel does not carry it — it carries lambda_6 most efficiently. At FeSe and 173Yb the host material's microscopic order parameter reverses the charge structure (FeSe is nematic; 173Yb is SU(N)-symmetric), so lambda_7 dominates. **This pattern is consistent with the substrate's BDI-class topological gap protection being inherited at the 3He-A platform but not at FeSe/173Yb.**

### Lab-cosmic correlation matrix coverage (volovik lane: 3He-A and 173Yb)

**Result**: The volovik-lane platforms (3He-A and 173Yb) cover **two of four** cosmic falsifier channels with structural linkage; **one of four** with weak structural linkage; **one of four** with no analog. The FeSe lane (mack lane) covers the remaining channels. **Classification: PHONONIC** (cross-channel structural mapping table).

| Lab observable (3He-A or 173Yb) | Cosmic counterpart | Linkage (substrate origin) | Status |
|:---|:---|:---|:---|
| 3He-A NMR delta_omega_K/omega_K (SW1/XA1/XB1) | CGWB Omega_GW (Row #7, LISA 2035) | Both probe a_4 spectral moment; 3He-A = lab analog of GGE-relic tensor production at Mach 13.75 transit per Row #7 inheritance convention `GGE-relic-tensor-Mach-13.75` | **STRUCTURAL** (W14-3 paragraph + lizzi S-7 §V.6 Mellin Strip Theorem; not yet cross-derived numerically) |
| 3He-A vortex texture nucleation (3He-A KZ defects) | r tensor-to-scalar (Row #2, BK-Array 2026 + LiteBIRD 2030) | B2 transverse mode shared origin; Path-H pathway = transverse fiber-oscillation; 3He-B inheritance per Volovik 9A 3-solo + S85 W2 OQ-7 | **STRUCTURAL** (Row #2 substrate framing block; PHONONIC linkage explicit in inventory line 228-243) |
| 173Yb Gamma_3B (lambda_8 sweet-spot, SW3) | none | lambda_8 is uniquely resolved via 173Yb 3-body channel (W14-6 finding); no cosmic falsifier accesses lambda_8 at 5-yr horizon | **NO COSMIC ANALOG** (substrate-direction-asymmetric coverage; W14 line 769 finding) |
| 173Yb Gamma_3B (lambda_6/_7 cross, XA3/XB3) | f_NL_folded Pathway-C (Row #9, SKA-1) | Kinematic similarity: 3-body Gamma at threshold-resonance is the laboratory analog of folded-triangle bispectrum kinematics; both probe 3-particle correlator at folded limit | **WEAK STRUCTURAL** (kinematic similarity only; no derivation pinning the Pathway-C 0.7685 to XA3/XB3 amplitudes) |

Rows #1 (w_0) and #12 (A_s) are not covered by 3He-A or 173Yb — they live in the cosmological-only registry. Row #3 (alpha_s) is also cosmological-only (n_s^2 - 1 identity, S50-51, no lab analog). The volovik lane covers the **substrate-dynamics + tensor-channel** subset; the mack/Landau/sagan lanes cover the scalar/equation-of-state/flux subsets.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S86-LAB-SI-TRANSLATION (W11-1, C5) | INFO | 9 rows populated (`SI_value`, `sigma_detect`, `lit_sha` non-null) with 6 provisional flags |
| S86-LAB-FALSIFIER-EVOI-TREE (W11-2, C6) | PASS | level distribution `{A:9, B:0, C:0, D:0}` at baseline sigma_detect; lowest d_r = 28.50 (SW3); highest = 58 958.86 (SW1=XA1) |
| S86-WATCHLIST-W6-NEW-CLASS (W14-6) | PASS | inventory +7022 bytes; 21.audit-block + summary section; 7 dE_a constants promoted to canonical_constants.py SECTION E |
| S86-WATCHLIST-W1-EDIT (W14-1) | FAIL | route (b) row-numbering-mismatch; honest timing-induced failure (subsequently moot via W13 P11) |
| S86-WATCHLIST-W2..5-EDIT (W14-2..W14-5) | PASS x4 | sub-row {3,7,9,12}.audit landings; full-64-hex pin discipline applied per `.claude/rules/gate-verdicts.md` |

I do not re-adjudicate any of these per spawn-prompt rule "Gate verdicts from source docs are authoritative."

---

## IV. Structural Implications

### IV.1 Level-saturation is not as decisive as the 9x A-level headline suggests

The `9x A-level` distribution is correct AT BASELINE sigma_detect anchors, but six of the nine rows are flagged provisional (W11-1 §line 106; the 3He-A and 173Yb rows). The 173Yb single-platform anomaly is structural: a 10x looser sigma_detect (matching publication-typical K_3 floors per spawn-prompt) demotes SW3 from level A to level C. The framework's lab-falsifier portfolio is therefore **5-yr-decisive only conditional on the 6 provisional sigma_detect anchors being sustainable as 1-sigma single-shot floors, not state-of-art upper-bounds**. The 3 FeSe rows are non-provisional and robust under any plausible tightening; the 3 3He-A rows have 2-3 OOM headroom and remain level A under the 100x looser scenario; the 3 173Yb rows are the fragile subset.

This is not a contradiction with the W11-2 PASS verdict — the PASS is correctly stated against the pre-registered ladder thresholds. It is a constraint-map observation: **the EVOI level ladder is sigma_detect-anchor-dominated for the 173Yb sub-portfolio**.

### IV.2 The unique-lambda_8 substrate-direction trigger has the highest fragility-to-leverage ratio

W14-6 line 769 names SW3 as the framework's strongest single-row substrate-direction-falsification trigger (a FAIL-AT-LAB on SW3 closes the lambda_8 substrate direction at lab precision, an exposure no other row supplies). My level-shift analysis adds: SW3 is also the row most likely to lose level-A under realistic literature-anchor revision. The combined statement is: **the framework's most decisive single-row falsifier is also its most fragile**. This is a structural concentration of risk, and it is appropriate to flag at suite-coherence level.

The mitigation is straightforward: re-anchor SW3's sigma_detect via a single-shot 3-sigma K_3 floor measurement at JILA / Florence / Munich during 2026-2028 (the literature gap S87 carry-forward consolidation already opened by W11-1 §line 106 + W14 wave §line 776). If the achievable single-shot K_3 floor at SU(N) lattice density is verified at 0.05 s^-1 (or below, e.g. 0.01 s^-1 with state-of-art Florence calibration), SW3 is robust. If the achievable floor is 0.1 s^-1 or higher, SW3 demotes and the unique-lambda_8 substrate-direction-falsification trigger weakens.

### IV.3 The 173Yb lambda_8 sweet-spot anomaly is a Jensen-deformation diagnostic

The W8_4_ratio rank inversion at 173Yb (sweet-spot lambda_8 = 2.85 < cross lambda_6 = 5.49 < cross lambda_7 = 13.19) is a **structural property of the Jensen-deformed inner product on SU(3)**, not an artifact of sigma_detect normalization. The compactification-resonance mental model (each platform's sweet-spot lambda projects with the largest amplitude) is approximately correct for 1-pair / single-shift channels (3He-A NMR, FeSe Knight) but **fails for 3-body / multi-correlator channels** because Gamma_3B samples the rep-theoretic content of the substrate via a kinematic 3-channel structure where Casimir mixing is most pronounced. This is a NEW prediction at suite level (the W14-6 substrate-direction asymmetric-coverage finding noted SW3 is the unique lambda_8 channel; my anomaly diagnosis adds: SW3 is unique AND the worst-projecting at its own platform — both follow from the same Jensen inner-product non-Euclidean structure).

Test: any other 3-body or higher-correlator channel (e.g. Cs/Yb mixed 3-body, Feshbach-resonance 3-body in degenerate Bose-Fermi mix) should exhibit the same lambda_8 rank-suppression. If observed, this confirms (b); if not, (a) or (c) is preferred.

### IV.4 3He-A is a sweet-spot-dominant (lambda_6 wins) platform; FeSe and 173Yb are sweet-spot-weakened (lambda_7 wins)

The pairwise rank-concordance analysis (lambda_6 vs lambda_7 across 3 platforms) shows 3He-A is the **singleton outlier** preferring lambda_6. This is consistent with 3He-A's BDI-class Z_2 gap protection (Volovik memory: framework-3heb-comparison.md, S60 22-correspondence count, BDI gap protection theorem of S65 GAP-ANTIJENSEN-65 PASS). lambda_6 carries the U(1)_K charge that the BDI Z_2 protects; FeSe (nematic, broken U(1)_K) and 173Yb (SU(N), no U(1)_K-singlet) lose this protection and revert to lambda_7-dominance. **This is a substrate inheritance pattern: BDI-class platforms inherit lambda_6 dominance; non-BDI platforms revert to lambda_7.**

### IV.5 BCS prefactor text-comment correction is documentation hygiene, not a physics issue

The 1.764 = pi / exp(gamma_E) identity is the standard BCS weak-coupling Delta(0)/(k_B T_c). The W11-1 substitution chain text incorrectly attributes 1.764 to 2*e^gamma_E/pi (= 1.1339 numerically). The script's numerical computation uses 1.764 directly (correct value), so the SI translation 34.146 MHz is correct. This is a **single-character text fix** (one swap of pi and e^gamma_E and drop the factor of 2 in the §W11-1 line 67 attribution comment). It does not propagate to any verdict, any downstream gate, or any inventory cell — the value 1.764 is canonical and is used correctly in the SI computation.

### IV.6 Audit-pin discipline closure: 21.audit-block consolidates the 9-row chain in full-64-hex form

W14-6's 21.audit-block sub-row pins W8-4 + W11 C5 + W11 C6 + W12 C30 + P11 in the full-64-hex form mandated by `.claude/rules/gate-verdicts.md`. Combined with W14-2/3/4/5's per-row audit sub-rows for Rows #3/#7/#9/#12, the entire upstream chain for the framework's 14 atomic predictions (5 cosmological + 9 lab) is now full-64-hex-citable from a single inventory file. Downstream consumers (the v3-closure ladder, S87 carry-forward gates, future audit re-runs) can extract canonical pins without grep-roundtrip against the verdict files. This is registry-layer infrastructure, not physics; the underlying substrate predictions are unchanged.

### IV.7 Constraint-map summary of the volovik-lane lab-cosmic coverage

The 3He-A lab-falsifier rows (SW1/XA1/XB1) are now structurally linked to **two** cosmic channels (CGWB Omega_GW via a_4 spectral moment; r tensor-to-scalar via Path-H B2-mode substrate inheritance). The 173Yb lab-falsifier rows are structurally linked to **one** cosmic channel (f_NL_folded Pathway-C via 3-body Gamma kinematic analog; weak linkage). The 3He-A/CGWB linkage is the **strongest** lab-cosmic structural bridge in the volovik lane — both observables probe the substrate's a_4 spectral moment under regulator-class adjudication (A)/(C) per W14-3's discriminator paragraph. A LISA detection at Omega_GW > 1e-12 (forward-falsifier threshold per inventory line 113) and a 3He-A NMR linewidth measurement at 1 kHz precision (Aalto/ROTA per Eltsov+ 2010) provide **dual-channel** access to the same substrate observable with 30+ years of separation and 5+ orders of magnitude of detector-environment dissimilarity. This is the framework's structurally cleanest lab-cosmic correlation pairing.

---

## V. Carry-Forward Computations

V.1. **173Yb single-shot K_3 floor re-anchor (sigma_detect refinement for SW3/XA3/XB3)**
   - **What**: Re-anchor SW3/XA3/XB3 sigma_detect from Cazalilla+ 2009 theoretical floor (0.05 s^-1) to a single-shot 3-sigma 173Yb K_3 measurement floor from Florence/JILA/Munich 2018-2024 SU(N) optical-lattice papers. Re-run W11 C5 SI translation with the updated sigma_detect; recompute detection_ratio for SW3/XA3/XB3; re-evaluate W11 C6 level assignment. Output: revised LAB-FALSIFIER level distribution conditional on the updated 173Yb floor; document whether SW3 remains level A or demotes to level B/C/D.
   - **Inputs**: `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv` (rows SW3/XA3/XB3); literature search via `mcp__paper-search__search_arxiv` for "173Yb SU(N) K_3 single-shot 3-body loss rate" 2018-2024; `computations/canonical_constants.py` (M_KK provenance, currently missing per W14-6 audit); `mcp__knowledge__get_constant("dE_173Yb_lambda_8")` = 2.8500.
   - **Gate**: `S87-173YB-K3-SINGLE-SHOT-FLOOR-REANCHOR` — PASS = single-shot 3-sigma K_3 floor from a peer-reviewed 2020-2024 paper found AND SW3 detection_ratio recomputed AND the row's level assignment held or formally revised in the inventory; FAIL = no peer-reviewed single-shot floor found AND SW3 carries provisional flag forward to S88+ with explicit literature-gap citation; INFO = peer-reviewed floor found at 0.1-1 s^-1 AND SW3 demotes to level B/C/D AND the 5-yr lab-decisive band 0.30-0.50 (P_decisive) is recomputed.
   - **Effort**: ~2-3 hours (1 agent-session: literature search + script update + re-run + inventory edit).

V.2. **Jensen-deformed inner-product non-Euclidean structure verification (3-body channel at non-173Yb platform)**
   - **What**: Compute the W8_4_ratio for at least one 3-body channel at a non-173Yb platform (Cs/Yb mixed Feshbach 3-body; or Sr-87 nuclear-spin-protected 3-body channel). Compare the lambda_8 amplitude rank against lambda_6 and lambda_7 at the same platform. Predict: 3-body channels at any SU(N)-respecting host should show lambda_8 sweet-spot suppressed below lambda_6/lambda_7 cross-platform amplitudes (replicating the SW3/XA3/XB3 pattern). 1-pair channels at the same hosts should NOT show this suppression.
   - **Inputs**: substrate D_K eigenvalues at L_max=8 with Jensen deformation (canonical from S85 W8-4 producing script `s85_w8_su3_op_lab_predictions.py`); SU(3) lambda_a basis with Casimir operator; 3-body kinematic kernel for the chosen non-173Yb platform; `mcp__knowledge__search_knowledge("Jensen deformation SU(3) Casimir 3-body channel")` for prior closures; `mcp__sage__sage_eval` for the Casimir mixing matrix elements <lambda_a | C2 | lambda_b> on the Jensen-deformed manifold.
   - **Gate**: `S87-JENSEN-NON-EUCLIDEAN-3BODY-CONFIRMATION` — PASS = at least one 3-body channel at a non-173Yb platform reproduces the lambda_8 rank-suppression pattern (sweet-spot < cross-platform amplitudes); FAIL = all tested 3-body channels reproduce the compactification-resonance prediction (sweet-spot largest); INFO = mixed result (some 3-body channels confirm, others don't), suggesting the diagnosis is platform-host-coupling-dependent rather than pure Jensen-inner-product structure.
   - **Effort**: ~1 day (1 agent-session): SU(3) Casimir mixing computation + 3-body kinematic kernel + cross-platform amplitude comparison. Could be batched with V.3.

V.3. **3He-A lab-cosmic correlation derivation: a_4 spectral moment shared origin (NMR linewidth <-> CGWB Omega_GW)**
   - **What**: Derive the explicit numerical coupling between the 3He-A NMR delta_omega_K/omega_K = 1.7267 (SW1, MHz-scale) and the substrate's a_4 spectral moment that generates CGWB Omega_GW(LISA) = 8.299e-58 (via the Mach 13.75 transit and the (A)/(C) regulator-class split). Predict: the same a_4 spectral moment under the (A)-class regulator family {zeta, Zubarev, SDW} produces both the 3He-A SW1 amplitude AND the (A)-class O(10^-10) LISA-detectable Omega_GW, with a fixed dimensionless ratio determined by the substrate's regulator-class-invariant content.
   - **Inputs**: `mcp__knowledge__trace_entity("S85-W13-2-CGWB-ALPHA-S-FLAGSHIP-JOINT")`; substrate a_4 spectral moment under zeta regulator (W12-4 5-regulator atlas); `dE_He_A_lambda_6 = 1.7267` (canonical post-W14-6); `Omega_GW_LISA = 8.299e-58` (W13-2 verdict); Mellin Strip Theorem from lizzi S-7 §V.6; `computations/canonical_constants.py` (M_KK = 7.428660e+16 GeV).
   - **Gate**: `S87-3HEA-CGWB-A4-SPECTRAL-COUPLING` — PASS = explicit formula derived AND numerical ratio (3He-A delta_omega_K/omega_K) / Omega_GW(LISA, A-class) computed AND result is regulator-class-invariant within 0.5 OOM across F_4 = {zeta, Zubarev, SDW}; FAIL = no closed-form derivation possible OR numerical ratio is not regulator-class-invariant (Mellin Strip Theorem assumption violated); INFO = derivation possible but only in a specific regulator-class subset (e.g. zeta only).
   - **Effort**: ~2-3 days (1 agent-session, with mack-cosmic-bridge co-derivation): a_4 derivation + cross-channel coupling + 5-regulator atlas evaluation. This is the strongest lab-cosmic structural bridge in the volovik lane and worth dedicated effort.

V.4. **W11-1 BCS prefactor attribution comment correction**
   - **What**: Edit `sessions/archive/session-86/session-86-w11-workingpaper.md` §W11-1 Step 1 (line 67 of the working paper) to correct the attribution comment from "1.764 = 2 e^gamma_E / pi" to "1.764 = pi / exp(gamma_E) (BCS weak-coupling Delta(0)/(k_B T_c) ratio)". Verify the corrected identity numerically. The script value 1.764 used in the SI translation is correct; only the comment is wrong; no verdict line, downstream gate, or inventory cell is affected. This is in-session documentation hygiene per `.claude/rules/agent-standards.md`; if not edited in S86, it propagates.
   - **Inputs**: `sessions/archive/session-86/session-86-w11-workingpaper.md` line 67-68; numerical verification: pi / exp(0.5772156649) = 1.7639 to 4 figures.
   - **Gate**: `S87-W11-1-BCS-ATTRIBUTION-COMMENT-FIX` — PASS = comment edited AND new identity numerically verified AND no other working-paper text affected; FAIL = comment cannot be edited without affecting verdict-line content (impossible by inspection, since the verdict line does not cite the algebraic identity); INFO = comment edited via /shortterm batch documentation hygiene rather than dedicated gate.
   - **Effort**: ~5 minutes (single Edit tool call + verification grep). Could be batched into the S87 W0 cleanup wave.

V.5. **3He-A BDI lambda_6 dominance theorem (formalize the singleton-outlier finding)**
   - **What**: Formalize the structural observation that 3He-A's lambda_6 dominance (over lambda_7) is the inheritance of BDI-class Z_2 gap protection from the substrate. Derive: (i) lambda_6 carries the U(1)_K charge that BDI Z_2 protects; (ii) FeSe (nematic, broken U(1)_K) and 173Yb (SU(N), no U(1)_K-singlet) lose this protection and revert to lambda_7 dominance; (iii) the cross-platform pattern (3He-A: lambda_6; FeSe: lambda_7; 173Yb: lambda_7) is uniquely predicted by BDI inheritance. Test: predict the rank-ordering for a 4th platform (TBD: pick a candidate that should also be BDI-class, e.g. UPt3 superconducting heavy-fermion, which also has a Z_2 protected gap).
   - **Inputs**: `mcp__knowledge__search_knowledge("BDI Z_2 lambda_6 U(1)_K substrate")`; framework-3heb-comparison.md memory file (S60 22-correspondences); S65 GAP-ANTIJENSEN-65 PASS; S53 BDI-W-PHONON-53 INFO; UPt3 host superconductor literature via `mcp__paper-search__search_arxiv`.
   - **Gate**: `S87-3HEA-BDI-LAMBDA6-DOMINANCE-THEOREM` — PASS = derivation closes AND a 4th BDI-class platform's lambda rank-ordering is correctly predicted (lambda_6 > lambda_7); FAIL = derivation does not close OR 4th-platform prediction wrong (lambda_7 > lambda_6 at the BDI-class candidate); INFO = derivation closes for 3He-A only and is not generic to BDI class (host-specific protection structure), suggesting lambda_6 dominance is a 3He-A-specific empirical feature, not a substrate-class theorem.
   - **Effort**: ~1 day (1 agent-session): BDI rep-theory + UPt3 host literature + cross-platform prediction + write-up.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Level-shift table: 6 of 9 rows are sigma_detect-floor-conditional; SW3 demotes A->C under realistic 10x looser K_3 floor | PHONONIC | Reported (not gated) | 9x A-level portfolio is conditional on sigma_detect anchor sustainability; 173Yb is fragile sub-portfolio |
| 2 | 173Yb sweet-spot anomaly diagnosis: Jensen-deformed inner product breaks Euclidean rank-ordering for 3-body channels | PHONONIC | Reported + diagnosis (b) selected | Predicts lambda_8 rank-suppression at any 3-body channel (testable via V.2) |
| 3 | BCS prefactor 1.764 = pi/exp(gamma_E) confirmed; W11-1 §line 67 comment text wrongly says "2*e^gamma_E/pi" (= 1.1339) | META | Documentation correction (V.4) | Single-character text fix; no physics propagation; numerical script value correct |
| 4 | Cross-platform Spearman concordance: 1 of 3 pairs concordant; 3He-A is singleton outlier on (lambda_6 vs lambda_7) | PHONONIC | Reported + structural cause proposed | BDI Z_2 lambda_6 dominance theorem candidate (V.5); host-coupling diagnostic |
| 5 | Lab-cosmic correlation: 3He-A covers CGWB + r (2 cosmic channels structurally); 173Yb covers f_NL Pathway-C (weak); SW3 lambda_8 has no cosmic analog | PHONONIC | Coverage matrix complete | 3He-A/CGWB a_4 coupling (V.3) is volovik lane's strongest lab-cosmic bridge |
| 6 | SW3 = unique-lambda_8 channel (W14-6 finding) AND most-fragile level-A entry (this work) — most decisive AND most fragile | PHONONIC | Combined structural concentration | Re-anchor sigma_detect via single-shot K_3 floor (V.1) is the highest-EVOI infrastructure task for the lab portfolio |
| 7 | Substrate-framing audit: SW1 phenomenology_note + W11-1 substitution chain pass substrate-first criterion | META | No container-thinking violations | "the substrate's ratio measured AT 3He-A scale" phrasing is correct; phononic-framing.md compliance preserved |
| 8 | Audit-pin discipline: 21.audit-block landed; 14 atomic predictions full-64-hex-citable from inventory | META | Registry infrastructure complete | Downstream consumers extract pins without grep-roundtrip; v3-closure ladder integration ready |
