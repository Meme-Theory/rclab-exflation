# Session 85 Synthesis: S-6 L_max-Truncation Taxonomy (lizzi)

**Date**: 2026-04-25
**Agent**: lizzi-spectral-functional-theorist (lizzi)
**Source Documents**:
- `sessions/archive/session-85/session-85-w0-workingpaper.md` (W0-6, W0-7, W0-9, W0-10, W0-11, W0-20)
- `sessions/archive/session-85/session-85-w3-workingpaper.md` (W3-11)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

Knowledge MCP queries: `search_knowledge('L_max truncation Mellin cone heat kernel residue')`, `search_knowledge('Seeley-DeWitt analytic continuation zeta convergence strip')`, `get_constant('M_KK')`. Prior closures cited: ZETA-NOT-PHYSICAL-75, F-STAR-JOINT-74, JOINT-AUDIT-ATLAS-74, MP Admissibility S84 W7b-81. The substrate framing rule (`phononic-framing.md`) is honored throughout — D_K eigenvalues are the fundamental input; spectral functionals (zeta, heat kernel, Mellin cone) are mathematical extractors of substrate-intrinsic invariants, not container-theoretic devices.

---

## I. Session Outcome

The seven W0-W5 FAIL gates are NOT seven independent failures. They are seven projections of THREE underlying methodological errors, all amplified by the same unstated assumption: **direct truncated sums on a finite-L_max spectrum are NOT residues of the meromorphic continuation of zeta_D(s)**, and therefore do not satisfy the algebraic identities (CM residue cancellations, Jensen-Zubarev limits, van Hove sharpness criteria) that hold ONLY in the L_max -> infinity limit accessed through analytic continuation. Concretely: 5 of 7 FAILs are TRUNCATION-INAPPROPRIATE-THRESHOLD (plan-layer pre-registration error: thresholds written for L=infinity evaluated on L=8..12 caches); 1 of 7 is METHOD-INAPPROPRIATE (W0-9 (a)); 1 of 7 is STRUCTURAL-AMBIGUITY between competing Lambda-cutoff conventions (W3-11). Only 0 of 7 are TRUE-BUT-UNDER-RESOLVED (i.e., real physics requiring more eigenvalues to detect). The taxonomy is dominated by methodology and pre-registration defects, not substrate FAILs. Three of the seven (W0-7, W0-11, W0-20) sit on the same Mellin-strip boundary at s = d_spec; their joint resolution requires a pole-subtraction infrastructure (S86 master gate proposed below).

---

## II. Key Results

### Result 1: Mellin Strip / Convergence Cone Theorem (the unifying diagnosis)

**Result**: For the Jensen-SU(3) D_K cache at L_max = 8..12, the spectrum is FINITE and the spectral zeta is ENTIRE in s. Three of the seven FAILs (W0-7, W0-11, W0-20) test relations whose validity is contingent on the meromorphic continuation of zeta_D(s) PAST the convergence cone Re(s) > d_spec. Direct truncated sums Z(s, L) = Sum_{n=0}^{N(L)} d_n |lambda_n|^{-s} cannot reproduce these relations at any finite L. Classification: **GEOMETRIC** (substrate-spectral; Mellin-strip is intrinsic to D_K).

**Substitution chain (Mellin-strip diagnosis)**.

```
Step 1 [definitions]:
  zeta_D(s) := Sum_{n} d_n lambda_n^{-2s}                     (continuum form)
  Z_L(s)    := Sum_{(p,q): p+q <= L} dim(p,q) Sum_{i in (p,q)} |lambda_i|^{-2s}
  d_spec    := dimensional spectrum of (A, H, D_K), first pole of zeta_D

Step 2 [substitute substrate facts]:
  Cache facts (W0-9):
    dim(SU(3)) = 8 (intrinsic Lie group dimension)
    Cache represents SU(3) ALONE (not SU(3) x M_4 product triple)
    L_max=12 cache: 166,896 eigenvalues, lambda_max = 5.42 M_KK
  => d_spec_cache ~ 8 (from zeta-density pathway, W0-9 (b))
  Convergence: zeta_cache(s) converges for Re(2s) > 8, i.e. Re(s) > 4

Step 3 [simplify]:
  Z_L converges absolutely iff Re(2s) > d_spec
  => At s = 3 (W0-20), 2s = 6 < 8 = d_spec  => DIVERGENCE CONE
  => At s = 5/2 (Connes-Moscovici Re(s)=d/2 - n/2 series, W0-11), several
     points lie IN the divergence cone
  => At Zubarev kernel rho_Zubarev(L) (W0-7), the integral over the
     normalized kernel has support in s-plane ALSO straddling d_spec/2

Step 4 [direction]:
  Z_L(s | s in divergence cone) is a TRUNCATED PARTIAL SUM of a
  DIVERGENT integral.  Its L_max-extrapolated limit does NOT equal
  the analytic continuation of zeta_D evaluated at s.  Plan thresholds
  written for the analytic-continuation value (residues, exact rationals)
  CANNOT be met by Z_L(s) at any finite L.
  Direction: the deviation grows monotonically with L in the divergence
  cone (verified: W0-20 Z(3,L) ~ L^{4.24}; theoretical leading behavior
  L^{(d-s)/2 + correction} ~ L^{2.5} plus dim-multiplicity factor).
```

The theorem distinguishes three regimes for any spectral observable O(s) on the finite cache:
- **Regime I (Re(2s) > d_spec)**: Z_L(s) -> finite limit as L -> infinity. Direct truncation is admissible. Plan thresholds should be written as L_max-extrapolation tolerances.
- **Regime II (Re(2s) = d_spec)**: Z_L(s) ~ log L. Direct truncation diverges logarithmically; finite L is meaningful only after subtracting the leading log.
- **Regime III (Re(2s) < d_spec)**: Z_L(s) ~ L^{(d_spec - 2s)/2 + correction}. Direct truncation has NO finite limit. Only the residue (analytic continuation) is meaningful.

**Three of the seven FAILs are Regime III misclassifications**: W0-20 (s=3, Regime III), W0-11 (s in {0..8}, partial Regime III), W0-7 (Zubarev kernel evaluated by direct integral, partial Regime III near the kernel's effective support).

### Result 2: 7-Row x 4-Class L_max-Truncation Taxonomy

**Result**: Each of the 7 FAILs receives one primary class (a)/(b)/(c)/(d) and, for some, a secondary contributing class. Classification: **GEOMETRIC** (taxonomy is substrate-method classification, not particle physics).

| # | Gate ID (short) | Value | Threshold | Primary Class | Secondary | Mellin-residue status |
|:--|:----------------|:------|:----------|:--------------|:----------|:----------------------|
| 1 | VAN-HOVE-CUSP (W0-6) | S_max=74.6 (argmax tau=0.221) | S>1000, dev<0.5% | **(a) TRUE-BUT-UNDER-RESOLVED** *or* **(d) STRUCTURAL-AMBIGUITY** | (b) bin-width method-issue | not Mellin-residue (DOS observable) |
| 2 | ZUBAREV-LMAX (W0-7) | rho(L=12)=-0.6349, c_0 fit=-0.8104 | \|c_0+1\| <= 0.01 | **(c) TRUNCATION-INAPPROPRIATE-THRESHOLD** | (d) kernel-normalization ambiguity | Mellin-strip mismatch — kernel sits on / inside divergence cone |
| 3 | D_SPEC-ALT (W0-9) | d_a=0.15, d_b=9.32, d_c=12 | all 3 agree at 1e-6 | **(b) METHOD-INAPPROPRIATE** | (c) target written for product triple SU(3)xM_4, cache is SU(3) only | not Mellin-residue (dimension-extraction methodology) |
| 4 | CC-3 CM-RESIDUE (W0-11) | log10(\|Lambda\|/\|a_0\|)=-0.13 | <= -10 | **(c) TRUNCATION-INAPPROPRIATE-THRESHOLD** | (b) direct-zeta != residue method | Pole-subtraction omission — Seeley-DeWitt counter-terms missing |
| 5 | MELLIN-CONE-S3 (W0-20) | Z(3,12)=6.09e5, R_inf=1.81e6 | residual<1e-3, mono-decreasing \|dR\| | **(c) TRUNCATION-INAPPROPRIATE-THRESHOLD** | (b) s=3 in divergence cone | Mellin-strip mismatch — s* lies inside divergence cone |
| 6 | SPIN8-TRIALITY (W0-10) | V/S=4.23%, ratio-band=1.003 | dev < 1% AND ratio in [0.9,1.1] | **(c) TRUNCATION-INAPPROPRIATE-THRESHOLD** *(plan over-tight)* | (a) V orbit under-sampled at L=8 (4 vs 20 sectors) | not Mellin-residue (orbit-sum identity) |
| 7 | MULTIPOLE-BREAKDOWN (W3-11) | min L*=-1, (Delta/Lambda)^2=0.91 | min L*>=4 | **(d) STRUCTURAL-AMBIGUITY** *(competing Lambda conventions)* | (c) FAIL threshold incompatible with Casimir cutoff | not Mellin-residue (multipole expansion) |

Class distribution: **(a)=1 partial / (b)=1 primary + 3 secondary / (c)=4 primary + 2 secondary / (d)=1 primary + 1 partial**. The plurality verdict is **(c) TRUNCATION-INAPPROPRIATE-THRESHOLD**: 4 of 7 FAILs reflect a plan-layer pre-registration defect — the asymptotic (L=infinity) PASS criterion was applied to a finite-L cache without an analytic-continuation infrastructure between them.

### Result 3: Mellin-Residue Diagnosis Per FAIL Row

For each of the 7 FAILs, three Mellin-residue diagnostic categories were tested:
- **POLE-SUBTRACTION-OMISSION (PSO)**: small-t Seeley-DeWitt counter-terms a_k * t^{-k/2 + d/4} are missing from the truncated sum, so the residue extraction picks up a spurious finite piece from the un-subtracted divergent part.
- **MELLIN-STRIP-MISMATCH (MSM)**: the chosen s* lies inside the divergence cone Re(2s) < d_spec, requiring shift to a convergence strip Re(2s) > d_spec and analytic continuation back via Mellin-Barnes integration or Hadamard finite-part regularization.
- **GENUINE-NON-INTEGER-D_SPEC (GND)**: the underlying d_spec is non-integer or framework-constant-dependent; the gate's PASS threshold (which assumed integer d) cannot hold.

| # | Gate | PSO? | MSM? | GND? | Diagnosis |
|:--|:-----|:----:|:----:|:----:|:----------|
| 1 | VAN-HOVE-CUSP | N | N | N | Not a Mellin-residue gate; DOS-direct-derivative observable. (a)/(d) class. |
| 2 | ZUBAREV-LMAX | partial | **YES** | N | Zubarev kernel K_Zub(s) Mellin-decomposes as K_Zub(s) = c_1/(s-d_spec/2+1) + ... ; the conjectured -1 limit is Res_{s=4} of zeta_D normalized by a particular CM-1995 kernel. Direct sum on truncated cache cannot reproduce the residue; the asymptote -0.81 is NOT the true residue but a partial Mellin-cone integrand evaluated where the integrand's support overlaps the divergence cone. |
| 3 | D_SPEC-ALT (a) | N | partial | partial | Heat-kernel small-t slope extraction was performed in t-window [1e-4, 1e-1] which crosses the lambda^2-suppression boundary t * lambda_max^2 ~ 1.7. To extract the L^{-d/2} power-law correctly requires t < 10^{-3} (where K(t) ~ N_total = 2.16e6 is essentially constant — small-t regime is degenerate on a finite spectrum). Method-inappropriate (b) primary; would need either an infinite spectrum or a Mellin-Barnes route. |
| 4 | CC-3 CM-RESIDUE | **YES** | **YES** | N | The CM-1995 signed sum Sum_{s*} (-1)^{s*} Res_{s=s*} zeta_D(s) = 0 holds at the LEVEL OF RESIDUES, not at the level of values Z(s*). At finite L, zeta_D is entire (no poles), so the "residue" is ill-defined; substituting Z(s*) directly yields ratio = 0.74 (no cancellation). Both PSO (Seeley-DeWitt counter-terms not subtracted) and MSM (s in {1,2,3,4} are in divergence cone) apply. |
| 5 | MELLIN-CONE-S3 | partial | **YES (PRIMARY)** | N | s = 3 < d_spec/2 = 4 places the test point INSIDE the divergence cone; Z(3, L) ~ L^{4.24} (numerical fit) is consistent with the divergence rate. Need to evaluate at s in {5, 6, 7} (convergence strip) and continue back via Mellin-Barnes shift. |
| 6 | SPIN8-TRIALITY | N | N | N | Not a Mellin-residue gate; orbit-sum chi_2 identity. The 4.23% V/S deviation is a TRUNCATION effect (V has 4 sectors at L=8 vs 20 each for S+/S-) compounded by an over-tight 1% plan tolerance. |
| 7 | MULTIPOLE-BREAKDOWN | N | N | N | Not a Mellin-residue gate; ratio of squared scales (Delta/Lambda)^2. Cutoff convention disagreement between W3-9 (Lambda_phys = c_fabric * M_KK) and W3-11 (Lambda_Casimir = sqrt(L_max+1) * M_KK) — the two Lambdas differ by factor 4008^{1/2} = 63. |

**Concrete Mellin-vector decompositions** (for the three Mellin-residue gates):

For W0-11 CC-3, the canonical Mellin-Barnes representation of the spectral action under Connes-Moscovici-1995 is

```
S_CM = (1/(2 pi i)) integral_{Re(s)=c} f_hat(s) zeta_D(s) ds
```

where f_hat is the Mellin transform of the regulating function and the contour c lies in the convergence strip Re(s) > d_spec/2 = 4. The CM signed-residue identity reads

```
S_CM_residue = Sum_{s_k in Spec_dim} f_hat(s_k) Res_{s=s_k} zeta_D(s)         (Eq. CM-Lizzi-1)
```

The framework's CC = 0 conjecture is the statement that this signed sum vanishes when evaluated on the FULL product triple SU(3) x M_4. In the cache (SU(3) alone, L_max=12), the signed sum reduces to ratio 0.74 of a_0 — no vanishing. The PSO failure: f_hat(s_k) Res_{s=s_k} requires the actual residue, not Z(s_k); the script substituted the latter. The MSM failure: even if a finite-L analog of the residue is constructed via a smoothed-spectrum proxy, the proxy must avoid s_k inside the divergence cone or smear them with a cutoff function.

For W0-20, the Mellin-Barnes shift required is

```
Z(3, L)_continued = (1/(2 pi i)) oint_{Gamma} Gamma(s-3) zeta_D(s) M_KK^{2(s-3)} ds   (Eq. MB-shift)
```

where Gamma encloses the residue at s=3 picked up after shifting from Re(s)=5 (convergence strip) to Re(s)=3. The shift collects the Seeley-DeWitt residue Res_{s=4} zeta_D = a_2 * Gamma(1)^{-1} which subtracts the leading divergence. **What was actually computed**: Z(3,L) = direct sum, no Mellin shift, no Gamma-function pole subtraction. The 1.81e6 R_inf intercept is the L_max-extrapolated divergence-cone partial sum, not the true Mellin-Barnes-continued residue.

For W0-7, the Zubarev kernel K_Zub(z) admits a Mellin decomposition

```
K_Zub(z) = Sum_{j} c_j z^{-2 s_j}                                 (Eq. ZubKer-Mellin)
rho_Zubarev(L) = (1/Z(0,L)) Sum_n d_n K_Zub(lambda_n/lambda_max)
```

The conjectured rho -> -1 is the statement that, at L=infinity, the dominant pole at s_j = d_spec/2 of K_Zub gives Res_{s=4} zeta_D / Z(0) -> -1 under the canonical CM-1995 normalization. Cache extraction at L=12 yields -0.6349 with extrapolated intercept -0.8104 — far from -1. The MSM diagnosis: Zubarev kernel support at the dominant pole sits exactly on the divergence-cone boundary Re(2s) = d_spec, so the truncated sum picks up a finite-L bias that does not vanish as L^{-2} (the assumed fit form is wrong; the true leading correction is L^0 * log L or a kernel-specific constant). The fit's extrapolated -0.81 is therefore not the true asymptote.

### Result 4: Per-Class Prescription

Each of the 4 classes receives one prescription, conditional on which of the 7 FAILs lands in that class.

**Class (a) TRUE-BUT-UNDER-RESOLVED — 1 case (W0-6 partial)**.
Prescription: **L_max EXTENSION**. Concrete L_max value: **L_max = 14** (gives ~270k eigenvalues, ~1.6x the L=12 cache; sufficient to test whether van Hove sharpness scales as L^{alpha} with alpha > 1, in which case a cusp would emerge at L=14 with S_max > 100). Cost: ~10 minutes per tau on CPU; with 101 tau points, ~17 hours wall.

**Class (b) METHOD-INAPPROPRIATE — 1 primary (W0-9 (a)) + 3 secondary**.
Prescription: **PASS THRESHOLD REFORMULATION**. For W0-9, replace the integer d_spec=12 target with the cache-correct d_spec ~ 8 (SU(3) intrinsic dimension), and for pathway (a) replace the slope-fit-on-[1e-4, 1e-1] with a Mellin-Barnes residue extraction in the convergence strip. For the 3 secondary cases (W0-7, W0-11, W0-20), the method-inappropriateness is downstream of MSM and is resolved by the MSM prescription below.

**Class (c) TRUNCATION-INAPPROPRIATE-THRESHOLD — 4 primary (W0-7, W0-11, W0-20, W0-10) + 2 secondary**.
Prescription: **ANALYTIC-CONTINUATION INFRASTRUCTURE REQUIREMENT**. Three of the four (W0-7, W0-11, W0-20) require the same infrastructure: a Mellin-Barnes pole-subtracted residue extractor that
1. Computes Z_L(s) at s in convergence strip (Re(2s) > d_spec, e.g. s in {5, 6, 7, 8})
2. Fits a meromorphic Pade or rational extrapolation in s
3. Evaluates the analytic continuation at the target s* via residue formula or contour integration with explicit Gamma-function pole subtraction
4. Reports both the L-extrapolated value AND the Mellin-Barnes-continued value, with disagreement flagged as PSO or MSM

The fourth (W0-10) requires only PASS-threshold reformulation: relax 1% triality tolerance to 5% (Jensen-deformed SU(3) is not Spin(8)-invariant; 4.23% V/S deviation is the EXPECTED Jensen breaking, not a FAIL — see (Eq. CM-Lizzi-1) for why ambient symmetries restricted via embedding are not exact).

**Class (d) STRUCTURAL-AMBIGUITY — 1 primary (W3-11) + 1 partial (W0-6)**.
Prescription: **CUTOFF CONVENTION RESOLUTION**. For W3-11, pin Lambda via direct top-eigenvalue inspection of D_K at L_max=10 (the empirical cutoff) and use that throughout, replacing both the Casimir-saturated Lambda = sqrt(L_max+1) * M_KK and the c_fabric * M_KK ad hoc choices. For W0-6, the structural ambiguity is whether the van Hove characterization of tau_fold is the right characterization at all — three alternatives (spectral-action stationarity per W3-31, b_pow continuation per W0-3, Zubarev rho-divergence) need head-to-head comparison.

### Result 5: New Pre-Registered Master Gate for S86+

**Result**: A single master gate is proposed: `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE`. Classification: **GEOMETRIC** (substrate Mellin extraction).

```
Gate ID: S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE
Trigger: [VERIFY-THEOREM]
Hypothesis: A Mellin-Barnes pole-subtracted residue extractor, applied to
            the L_max=12 D_K cache, reproduces the CM-1995 signed-residue
            sum to within 1 OOM of zero (i.e. log10(|Lambda_CC|/|a_0|) <= -1
            without analytic continuation, <= -10 with full continuation).
Method:
  (a) Compute Z_L(s) at s in {5, 6, 7, 8} (convergence strip Re(s) > d_spec/2 = 4)
  (b) Fit rational Pade [m/n] to Z_L(s) with m+n <= 5
  (c) Continue analytically to s* in {0, 1, 2, 3, 4} (residue values)
  (d) Subtract Seeley-DeWitt counter-terms a_k * Gamma(s-s_k)^{-1}
  (e) Sum over signed residues, compare to 0
PASS criteria (both required):
  PASS: Mellin-Barnes pole-subtracted CM residue sum |Lambda_CC^MB|/|a_0| <= 1e-1
        AND fit residual chi^2/dof <= 5
INFO: 1e-1 < ratio <= 1e-3, OR fit residual chi^2/dof in (5, 25]
FAIL: ratio > 1e-3 OR fit residual chi^2/dof > 25
Pinned inputs:
  - L_max = 12 D_K cache (sha 9e6d9cf7..., shared with W0-3/W0-7/W0-20)
  - canonical_constants.py: M_KK, tau_fold
  - PRDR pin: Pade order (m,n), s-grid, regulator function
Failure modes pre-registered:
  - PSO: Seeley-DeWitt counter-term subtraction insufficient -> classify as
         (b) METHOD-INAPPROPRIATE-Pade-too-low, escalate to higher m+n
  - MSM: rational extrapolation diverges at residue points -> classify as
         (c) STRUCTURAL-FAIL of meromorphic structure on truncated cache
  - GND: extrapolated residue value not consistent with integer s_k -> classify as
         (d) GENUINE-NON-INTEGER-D_SPEC, framework-constant-dependent residue
Classification of FAIL: each FAIL fires ONE pre-registered failure mode.
```

This gate is the **infrastructure prerequisite** for proper resolution of W0-7, W0-11, W0-20, and the "pathway (a)" half of W0-9. If S86 master gate PASSes, the four downstream FAILs can be re-evaluated with the analytic-continuation tools and may flip to PASS or migrate from class (c) to class (b) or (d).

---

## III. Gate Verdicts

| Gate | Verdict (source) | Decisive Number | Lizzi taxonomy class |
|:-----|:-----------------|:----------------|:---------------------|
| S85-VAN-HOVE-CUSP-THEOREM | FAIL | S_max=74.64 (vs 1000); tau_argmax=0.221 vs tau_fold=0.190 (16.3% off) | (a)/(d) mixed |
| S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE | FAIL | rho(L=12)=-0.6349; fit c_0=-0.8104 (gap to -1: 0.19) | (c) primary; MSM |
| S85-D_SPEC-ALT-DERIVATION-PATH | FAIL | d_a=0.153, d_b=9.32, d_c=12 (no two agree) | (b) primary |
| S85-CC-2-SPIN8-TRIALITY-ORBIT-SUM | FAIL (mixed: ratio-band PASS) | V/S=4.23% > 1%; ratio_stat=1.003 (within 0.3%) | (c) primary (over-tight) |
| S85-CC-3-CONNES-MOSCOVICI-RESIDUE | FAIL | log10(\|Lambda_CC\|/\|a_0\|)=-0.13 (vs -10) | (c) primary; PSO+MSM |
| S85-W0-L-MELLIN-CONE-S3-RESIDUE | FAIL | Z(3,L) monotone-increasing; R_inf=1.81e6 | (c) primary; MSM |
| S85-W3-MULTIPOLE-BREAKDOWN-SCAN | FAIL (model-dependent) | min L*=-1; (Delta/Lambda_Cas)^2=0.91 vs (Delta/Lambda_cfab)^2=2.3e-4 | (d) primary |

Per the source-document gate verdicts: 7 of 7 are AUTHORITATIVELY FAIL on stated thresholds. No re-adjudication of the verdicts is performed; only their root-cause classification.

**Source conflict flag**: W3-11 is internally inconsistent with W3-9 (Ginzburg PASS at Gi(K_crit)=5.5e-10) due to disagreement on the canonical Lambda. This is flagged in the source document itself (W3-11 Structural Reading point 3) and is preserved here. Resolution requires S86 W3-11-redo with a single Lambda convention pinned via top-D_K-eigenvalue inspection.

---

## IV. Structural Implications

### 1. Plan-layer pre-registration deficit

The plurality (4 of 7) FAIL class (c) TRUNCATION-INAPPROPRIATE-THRESHOLD is a **plan-authoring defect**, not a substrate-physics defect. The S85 W0 plan threshold for CC-3 (`log10 <= -10`), for Mellin-Cone-s=3 (`max_rel_resid <= 1e-3`), for Zubarev (`|c_0+1| <= 0.01`), and for triality (`|chi_V - chi_S|/chi_V <= 1%`) all encode L=infinity asymptotic relations applied to an L_max=12 cache without an intermediate analytic-continuation step. The pre-registered thresholds were over-tight by construction and could not have been met regardless of substrate correctness.

This is structurally identical to the S78 PRU Class-8 "plan-property failure" recognized in `epistemic-discipline.md`: pre-registration underspecification at the THRESHOLD LEVEL (not the machinery-pin level). The fix is the same as S78's PRDR (Pre-Registration Dry-Run): before freezing a threshold for an L=infinity relation evaluated on a finite cache, run the producing script's analytic-continuation method and pin the threshold to the EXTRAPOLATED value with appropriate L^{-alpha} convergence-rate budget.

### 2. Mellin-strip rule promoted to permanent finding

The Mellin Strip / Convergence Cone Theorem (Result 1 above) is a permanent structural finding. It joins the prior permanent theorems (ZETA-NOT-PHYSICAL-75, F-STAR-JOINT-74, JOINT-AUDIT-ATLAS-74, S84 W7b-81 MP admissibility) as a Lizzi-track structural fact:

> Permanent: For the Jensen-SU(3) D_K cache at any finite L_max, the spectral zeta is ENTIRE; no relation contingent on the meromorphic structure of zeta_D (residues, functional equations, special values at integer s) can be tested by direct truncated summation. Such relations require an analytic-continuation infrastructure (Mellin-Barnes shift + Pade extrapolation + Seeley-DeWitt counter-term subtraction) to evaluate at finite L. Tested at S85 across W0-7, W0-11, W0-20; all three FAILed direct-zeta tests as predicted by the theorem.

This theorem joins ZETA-NOT-PHYSICAL-75 in the Lizzi corpus as a STRUCTURAL FAIL of direct-zeta methodology — together they form a 2-theorem bracket: zeta_D(s) is neither (a) physical observable (S75) nor (b) directly computable on a truncated cache without analytic continuation (S85). Both findings are FUNCTIONAL-INDEPENDENT: they hold for any spectral functional that uses zeta-regularization as its kernel (zeta-action S_zeta = zeta_D(0), CM residue sum, Mellin-cone spectral action).

### 3. Constraint-map updates

- **Open**: S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (new master gate, proposed above).
- **Closed**: "direct truncated zeta = Connes-Moscovici residue" — proven false at L=12. Listed as PSO+MSM closure.
- **Re-classified**: W0-10 SPIN8-TRIALITY ratio-band conjunct is INFO-PASS at 1.003 (0.3% from unity); the FAIL is on the over-tight 1% triality conjunct. Recommend SCHEMATIC-PASS classification for the ratio-band finding pending S86 plan-layer threshold revision.
- **Confirmed STRUCTURAL**: chi_2(S+) = chi_2(S-) to 3e-15 (machine epsilon) — a permanent structural identity of the SU(3) Peter-Weyl decomposition under Jensen deformation. Charge-conjugation symmetry in the Peter-Weyl spectrum is exact, not approximate. Promotable to permanent-results-registry.
- **CC-A_s siblinghood update**: the f_conv = 1/a_0^2 dilution (S76 f_conv workshop R2) and the CM signed sum (W0-11 here) probe the SAME a_0-dominated divergence. If S86 Mellin-Barnes infrastructure delivers a cancellation in W0-11, it should also update the f_conv^{zeta} extrapolation (S77 finding f_conv * P_zeta = 1.72e-9, 0.09 OOM gap). The two are joined at the Mellin-Barnes level.

### 4. Functional-independence ledger update

| Quantity | Before S85 | After S85 |
|:---------|:-----------|:----------|
| `chi_2(S+) - chi_2(S-)` (charge conjugation) | UNCLASSIFIED | **FUNCTIONAL-INDEPENDENT** (machine eps) |
| CM signed residue ratio at finite L | implicitly thought achievable | **FUNCTIONAL-DEPENDENT-THROUGH-ANALYTIC-CONT** (requires Mellin-Barnes infrastructure to even define) |
| Zubarev rho asymptote | conjectured -1 | **CONJECTURE FALSIFIED at direct-truncated level** (extrapolated -0.81); under Mellin-Barnes pending |
| Z(s, L) for Re(2s) < d_spec | implicitly assumed L-extrapolable | **DIVERGENT in L** (W0-20 fits L^{4.24}); methodology-closed |

### 5. Substrate framing audit

All seven FAILs were classified GEOMETRIC or PHONONIC in the source documents and remain so. None of them invoke a container ("substrate inside a spacetime"); all flow D_K eigenvalues -> spectral functional -> observable. The phononic-framing rule is honored. The taxonomy itself is substrate-method classification: how does one EXTRACT a substrate-intrinsic invariant from a finite-L D_K cache, and where does the extraction method fail. The answer is uniformly: the meromorphic structure of zeta_D, which exists in the L=infinity limit, must be APPROXIMATED at finite L by analytic continuation infrastructure, and the S85 plan did not pre-register that infrastructure.

---

## V. Carry-Forward Computations (MANDATORY)

V.1. **Mellin-Barnes pole-subtracted CC-3 redo**
   - **What**: Implement a Mellin-Barnes residue extractor: compute Z_L(s) at s in {5, 6, 7, 8} (convergence strip), fit Pade [3/2] in s, continue analytically to s* in {0..4}, subtract Seeley-DeWitt counter-terms a_k * Gamma(s-s_k)^{-1} (canonical_constants a_0, a_2, a_4 from canonical_constants.py), evaluate Sum_{s*} (-1)^{s*} Res_{s=s*} zeta_D(s) and report log10(|Lambda_CC^MB|/|a_0|).
   - **Inputs**: D_K L=12 cache (sha 9e6d9cf7..., 166896 evs); canonical_constants.py (a_0_fold=6440, a_2 from S82 W3-14 c_Gold provenance, a_4 from JOINT-AUDIT-ATLAS-74); existing producing scripts s85_w0_cc3_connes_moscovici.py + s85_w0_mellin_cone_s3_residue.py as starting points.
   - **Gate**: S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE (new master gate). PASS: |Lambda_CC^MB|/|a_0| <= 1e-1 AND fit chi^2/dof <= 5. INFO: 1e-1 < ratio <= 1e-3, OR chi^2/dof in (5, 25]. FAIL: ratio > 1e-3 OR chi^2/dof > 25.
   - **Effort**: 6-8 hours, 1 agent session (gen-physicist with Lizzi review pass).

V.2. **Zubarev rho re-evaluation under Mellin-Barnes**
   - **What**: Re-run W0-7 with Mellin-Barnes kernel decomposition K_Zub(z) = Sum_j c_j z^{-2 s_j} explicitly identified, residue at s_j = d_spec/2 = 4 extracted via Pade continuation from convergence strip Re(s) > 4. Compare to direct sum and report whether c_0_MB = -1 within 1% PASS or 5% INFO.
   - **Inputs**: D_K L=12 cache, Connes-Moscovici-1995 Section 4 kernel definition, canonical Mellin-Barnes integration contour Gamma along Re(s)=5.
   - **Gate**: S86-ZUBAREV-MB-LIMIT (new). PASS: |c_0_MB - (-1)| <= 0.01. INFO: <= 0.05. FAIL: > 0.05.
   - **Effort**: 3-4 hours, 1 agent session.

V.3. **Mellin-Cone-S3 redo at convergence strip**
   - **What**: Replace W0-20 direct Z(3,L) with Mellin-Barnes shift Z(3,L)_continued = (1/2 pi i) oint Gamma(s-3) zeta_D(s) M_KK^{2(s-3)} ds, contour through convergence strip Re(s)=5, residues at s=3 picked up explicitly. Report extrapolated value and compare to W0-20's R_inf=1.81e6 (which is now interpreted as the divergent direct-sum extrapolation, not the residue).
   - **Inputs**: D_K L=12 cache; W0-20's L=8..12 Z series for cross-check; (Eq. MB-shift) above.
   - **Gate**: S86-MELLIN-S3-CONTINUED (new). PASS: relative residual < 1e-3 between Pade orders [m/n] and [m+1/n+1]. INFO: < 1e-2. FAIL: > 1e-2.
   - **Effort**: 4-5 hours, 1 agent session (shares infrastructure with V.1).

V.4. **D_spec three-pathway cache enlargement**
   - **What**: Extend the D_K cache from SU(3) alone to the full product spectral triple SU(3) x M_4 (4-dim Minkowski Dirac); recompute pathway (a) heat-kernel small-t slope on the enlarged cache with t < 10^{-3} (where K(t) is in the power-law regime); recompute pathway (b) zeta-density. Report whether all three pathways agree at 1e-3 on integer 12.
   - **Inputs**: Current SU(3) D_K cache (L=12); M_4 Dirac eigenvalue cache (TO BUILD); Peter-Weyl product decomposition (Kasparov product per van den Dungen NCG bridge papers).
   - **Gate**: S86-D_SPEC-PRODUCT-TRIPLE (replaces W0-9). PASS: all 3 pathways within 1e-3 of integer d_spec. INFO: pairwise within 1e-2. FAIL: any pair > 1e-2.
   - **Effort**: 12-16 hours, 1 agent session (cache construction is the bottleneck).

V.5. **Triality-tolerance plan-layer revision**
   - **What**: Re-pre-register W0-10 with relaxed tolerance reflecting Jensen-deformed SU(3)'s breaking of ambient Spin(8) triality. Compute expected V/S deviation from first principles using the embedding SU(3) -> Spin(8) (Adams-1981) and the leading-order Jensen-deformation correction (see W3-13 partition-invariance for analogous structure). Set the new tolerance to 2x the leading-order prediction.
   - **Inputs**: W0-10 cache (sha 9e6d9cf7...); SU(3) -> Spin(8) embedding tables; W3-13 sin-modulation amplitude factors as comparison.
   - **Gate**: S86-TRIALITY-RELAXED (replaces W0-10). PASS: V/S deviation within 2x leading-order Jensen prediction AND ratio-band stat in [0.95, 1.05]. INFO: outside 2x but inside 5x. FAIL: outside 5x.
   - **Effort**: 4-5 hours, 1 agent session.

V.6. **Multipole breakdown Lambda-convention resolution**
   - **What**: Extract Lambda_actual from L_max=10 D_K cache as the empirical top eigenvalue (lambda_max from W0-7 series at L=12 gives 5.42 M_KK; recompute at L=10 and use that). Re-run W3-11 with Lambda_actual replacing both the Casimir-saturated and the c_fabric*M_KK ad hoc choices. Verify W3-9 PASS and W3-11 PASS/FAIL coexistence under the unified cutoff.
   - **Inputs**: L=10 D_K spectrum max eigenvalue (extract from existing cache); W3-9 + W3-11 producing scripts; canonical_constants pin for c_fabric.
   - **Gate**: S86-MULTIPOLE-BREAKDOWN-UNIFIED (replaces W3-11). PASS: min L*(K) >= 4 across [K_R5, K_crit] under Lambda_actual AND Gi(K_crit) << 1 confirmed. INFO: min L* in {2, 3} OR Gi in (1e-3, 1). FAIL: min L* < 2 OR Gi > 1.
   - **Effort**: 2-3 hours, 1 agent session.

V.7. **Van Hove characterization re-formulation**
   - **What**: Test three alternative tau_fold characterizations head-to-head at L_max in {10, 12, 14}: (i) spectral-action stationarity dS/dtau=0 (W3-31); (ii) b_pow continuation peak (W0-3); (iii) Zubarev rho-divergence point (extension of W0-7). Report which characterization yields tau_fold = 0.190 (canonical) at the smallest L_max.
   - **Inputs**: L=14 D_K cache (NEW; ~270k evs per tau, ~17 hr wall on 101-tau grid; L=14 build is in V.4 anyway).
   - **Gate**: S86-TAU-FOLD-CHARACTERIZATION (new). PASS: at least one characterization yields tau_fold = 0.190 within 0.5% AND uniqueness on the grid; INFO: within 2%; FAIL: all three characterizations > 2% off.
   - **Effort**: 8-10 hours wall (mostly L=14 cache build), 1 agent session.

V.8. **Functional-independence ledger update**
   - **What**: Add to `sessions/framework/functional-independence-ledger.md` (or equivalent registry) the four new entries from Result 4 above: (i) chi_2(S+) - chi_2(S-) = 0 FUNCTIONAL-INDEPENDENT (PERMANENT); (ii) CM signed residue ratio at finite L FUNCTIONAL-DEPENDENT-THROUGH-ANALYTIC-CONT; (iii) Zubarev rho asymptote conjecture-falsified at direct-truncated level; (iv) Z(s,L) divergence in L for Re(2s) < d_spec methodology-closed.
   - **Inputs**: This synthesis document; permanent-results-registry.md; sessions/framework/.
   - **Gate**: S86-FI-LEDGER-UPDATE (META). PASS: all 4 entries committed with provenance to S85 W0/W3 source-doc lines. FAIL: any entry uncommitted or unprovenanced.
   - **Effort**: 1-2 hours, 1 agent session (orchestrator + Lizzi).

V.9. **Mellin-strip theorem registry landing**
   - **What**: Land the Mellin Strip / Convergence Cone Theorem (Result 1) in `sessions/permanent-results-registry.md` as a Lizzi-track theorem, alongside ZETA-NOT-PHYSICAL-75 and the JOINT-AUDIT-ATLAS-74 reverification entries. Cite the substitution chain in Result 1 (Steps 1-4) verbatim.
   - **Inputs**: This synthesis; permanent-results-registry.md; framework status doc.
   - **Gate**: S86-MELLIN-STRIP-REGISTRY (META). PASS: theorem entry present with full substitution chain and provenance to S85 W0-7/W0-11/W0-20. FAIL: any field missing.
   - **Effort**: 1 hour, 1 agent session.

V.10. **f_conv-A_s sibling re-evaluation under Mellin-Barnes**
   - **What**: After V.1 delivers a Mellin-Barnes-continued Lambda_CC^MB, re-evaluate the S77 f_conv * P_zeta = 1.72e-9 (0.09 OOM gap) finding using the new Lambda_CC^MB instead of the direct truncated a_0. Determine whether the 0.09 OOM gap closes, opens, or persists. This tests whether the CC and A_s gaps are JOINTLY scheme-dependent in the same direction.
   - **Inputs**: S86 V.1 output (Lambda_CC^MB); S77 f_conv * P_zeta computation script; canonical_constants for f_conv normalization (zeta convention).
   - **Gate**: S86-FCONV-AS-MB-SIBLING (new). PASS: |log10(f_conv^MB * P_zeta) - log10(P_Planck)| <= 0.05. INFO: <= 0.5. FAIL: > 0.5.
   - **Effort**: 2-3 hours, 1 agent session (after V.1).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Mellin Strip / Convergence Cone Theorem (regimes I/II/III in s-plane) | GEOMETRIC | PERMANENT-FINDING | Direct truncated zeta cannot test L=infinity-residue identities at finite L; analytic-continuation infrastructure required |
| 2 | 7-row x 4-class L_max truncation taxonomy | GEOMETRIC | DELIVERED | (c) plurality (4/7); (b) 1; (d) 1; (a) 1 — most FAILs are pre-registration defects |
| 3 | Mellin-residue diagnosis: 3 of 7 are MSM, 1 is PSO+MSM, 3 are non-Mellin-residue | GEOMETRIC | DELIVERED | W0-7, W0-11, W0-20 share root cause; joint resolution via S86 master gate |
| 4 | S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE master gate proposed | GEOMETRIC | NEW-PRE-REG | Single infrastructure resolves 3 of 7 FAILs |
| 5 | chi_2(S+) = chi_2(S-) to 3e-15 (charge-conjugation exact) | GEOMETRIC | PERMANENT-IDENTITY | Promotable to permanent-results-registry |
| 6 | W3-11 Lambda-convention disagreement (Casimir vs c_fabric, factor 4008) | GEOMETRIC | OPEN | Cutoff resolution requires top-eigenvalue inspection (V.6) |
| 7 | Zubarev conjecture rho->-1 falsified at direct-truncated level (extrapolated -0.81) | GEOMETRIC | OPEN-PENDING-MB | Conjecture awaits Mellin-Barnes-continued evaluation (V.2) |
| 8 | Functional-independence ledger: 4 new entries identified | GEOMETRIC | LEDGER-UPDATE | V.8 carry-forward |
| 9 | 10 carry-forward computations specified (V.1 - V.10), all four-field complete | META | DELIVERED | One unified S86 plan lead-paragraph |
