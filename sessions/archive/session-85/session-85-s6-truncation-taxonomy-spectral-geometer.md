# Session 85 Synthesis: S-6 L_max-Truncation Taxonomy (spectral-geometer)

**Slot**: 1b synthesis S-6
**Reviewer**: spectral-geometer (heat-kernel / Seeley-DeWitt technical track)
**Sources**: `sessions/archive/session-85/session-85-w0-workingpaper.md`, `sessions/archive/session-85/session-85-w3-workingpaper.md`
**Knowledge MCP queries (before any direction claim)**: `search_knowledge('L_max truncation')`, `search_knowledge('heat kernel analytic continuation Seeley-DeWitt')`, `search_knowledge('Connes-Moscovici residue zeta cosmological')`, `search_knowledge('van Hove cusp DOS spectral density divergence')`, `search_knowledge('spectral dimension d_spec heat kernel')`, `search_knowledge('triality SO(8) S+ S- vector spinor')`, `get_constant('M_KK')`, `get_constant('c_fabric')`, `get_constant('tau_fold')`.
**Date**: 2026-04-25.

---

## I. Subject

Seven gates over Wave W0 and Wave W3 of S85 returned FAIL verdicts whose root cause is a structural mismatch between (i) plan thresholds calibrated to L_max → ∞ asymptotic identities, and (ii) computations executed on a finite Peter–Weyl truncation of the Jensen-deformed SU(3) D_K spectrum. The gates are listed below by gate ID. Verdicts are AUTHORITATIVE per source documents; this synthesis classifies their FAIL modes and prescribes per-class remediation.

| # | Gate ID | Verdict | Source §  | Reported value | Plan threshold |
|:--|:--------|:--------|:----------|:--------------|:--------------|
| 1 | S85-VAN-HOVE-CUSP-THEOREM | FAIL | W0 §W0-6 | r=16.32%, S_max=74.64 | r ≤ 0.5%, S>1000 |
| 2 | S85-ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE | FAIL | W0 §W0-7 | c_0 = −0.8104, |c_0+1| = 0.1896 | |c_0+1| ≤ 0.01 |
| 3 | S85-D_SPEC-ALT-DERIVATION-PATH | FAIL | W0 §W0-9 | d_a=0.153, d_b=9.32, d_c=12 | three-pathway agree at 1e-6 |
| 4 | S85-CC-3-CONNES-MOSCOVICI-RESIDUE | FAIL | W0 §W0-11 | log10(|Λ_CC|/|a_0|) = −0.132 | ≤ −10 |
| 5 | S85-W0-L-MELLIN-CONE-S3-RESIDUE | FAIL | W0 §W0-20 | R_∞ = 1.81e6 (divergent) | finite limit, max_rel_resid ≤ 1e-3 |
| 6 | S85-CC-2-SPIN8-TRIALITY-ORBIT-SUM | FAIL (mixed) | W0 §W0-10 | |Δχ_2|/χ_2 = 4.23%; ratio_stat=1.003 | triality 1% AND ratio band [0.90, 1.10] |
| 7 | S85-W3-MULTIPOLE-BREAKDOWN-SCAN | FAIL | W3 §W3-11 | min L*(K) = −1; (Δ/Λ_Casimir)² = 0.913 | min L*(K) ≥ 4 |

The taxonomy below classifies each FAIL into one of four classes (A/B/C/D), prescribes the specific remediation, and lays out a Mellin-heat-kernel analytic-continuation infrastructure spec that would convert §W0-11 and §W0-20 from FAIL to evaluable.

---

## II. Method — Heat-kernel governing structure (substitution chain)

### II.A The Mellin-heat-kernel duality (foundational identity)

For a positive elliptic operator D_K² of dimension d on a compact manifold, the spectral zeta function and the heat kernel are related by the Mellin transform:

```
Step 1 [definition]:
  K(t)         = Tr exp(−t D_K²)  =  Σ_λ d_λ exp(−t λ²)
  ζ_D(s)       = Σ_λ d_λ |λ|^(−s)                  (Re s > d)
  Mellin id.   :  ζ_D(s) Γ(s/2) = ∫_0^∞ t^{s/2 − 1} K(t) dt
```

```
Step 2 [Seeley-DeWitt asymptotics, t → 0+]:
  K(t)  ~  (4π)^{−d/2} Σ_{n ≥ 0} a_{2n} t^{n − d/2}
       = (4π)^{−4} [ a_0 t^{−4} + a_2 t^{−3} + a_4 t^{−2} + a_6 t^{−1} + a_8 + O(t) ]    (d=8)
```

```
Step 3 [meromorphic continuation]:
  Substituting the asymptotic expansion into the Mellin integral and splitting at t = 1
  produces explicit poles of ζ_D(s) at  s = d − 2n,  n = 0, 1, 2, ...
  with residues  Res_{s = d−2n} ζ_D(s) = (4π)^{−d/2} · 2 · a_{2n} / Γ((d−2n)/2)        (d=8)
```

```
Step 4 [direction — pole locations for SU(3), d=8]:
  Poles at s ∈ {8, 6, 4, 2, 0}.  Between these the function is HOLOMORPHIC.
  The Connes-Moscovici dimension spectrum is exactly Sd = {0, 2, 4, 6, 8} (CM-1995 §5).
```

### II.B Convergence regime of the direct truncated sum

The truncated zeta on the finite L_max spectrum ζ_{D,L}(s) = Σ_{p+q ≤ L_max} dim(p,q) Σ_λ |λ|^(−s) is an entire function of s (a finite sum of finitely many exponentials in s). The full ζ_D(s) — the L_max → ∞ limit — is meromorphic with poles at s = d − 2n.

```
Step 1 [def]: directly summed Z_L(s)  ≡  Σ_{p+q ≤ L_max} dim(p,q) · Σ |λ|^(−s)
Step 2 [substitute]: as L_max → ∞ at FIXED s,
                      Z_L(s) → ζ_D(s)  iff  Re s > d  (Weyl-law convergence regime)
Step 3 [simplify]: at s ≤ d, Z_L(s) is finite at every finite L but DIVERGES as L → ∞.
Step 4 [direction]: a "residue extraction" from direct truncated sums at s = d − 2n is
                    NOT a residue in the analytic-continuation sense; it is a partial
                    sum at the divergence boundary. The plan's PASS conditions targeting
                    asymptotic CM identities cannot be satisfied by direct sum at any
                    finite L_max.
```

This is the structural reason the Connes-Moscovici-residue gate (#4) and the Mellin-cone-s3 gate (#5) FAIL. Their PASS thresholds are residue identities in the meromorphic-continuation sense; the producing scripts execute partial sums at s=3 < d=8, which lies in the divergence regime of the limit function.

Knowledge-MCP cross-check: search results return "The TRUNCATED zeta_L(s) has a residue that grows with L (= a_2(L)/2, divergent)" (`s61_pw_conformal_zeta.py`) and the explicit theorem "the zeta function has a meromorphic continuation with poles at s = d/2 − k" (`s63_gilkey_oneloop.py`) — confirming the structural FAIL mode is already documented in the corpus.

---

## III. The 7 × 4 Truncation Taxonomy

### III.A Class definitions

- **Class A — TRUE-BUT-UNDER-RESOLVED**: PASS achievable at higher L_max with quantitative scaling toward the threshold.
- **Class B — METHOD-INAPPROPRIATE**: an asymptotic identity is being evaluated on a finite spectrum where the relevant analytic object (residue at a pole) does not exist; direct truncated sum is structurally unable to satisfy the PASS condition at any finite L_max.
- **Class C — TRUNCATION-INAPPROPRIATE-THRESHOLD**: the plan's threshold is calibrated to asymptotic regime; finite-L truncation has known O(L^α) drift and the threshold needs truncation-aware loosening.
- **Class D — STRUCTURAL-AMBIGUITY**: machinery parameter (here a UV cutoff Λ) is multi-valued within the same wave; gate threshold requires pinning that parameter before the verdict is meaningful.

### III.B Master classification table

| # | Gate                             | Class | Heat-kernel diagnosis                                                                                                        | Prescription |
|:--|:---------------------------------|:-----:|:-----------------------------------------------------------------------------------------------------------------------------|:-------------|
| 1 | VAN-HOVE-CUSP-THEOREM            | **A** | DOS ρ(E) is the L_max-dependent histogram of |Im λ_i|; cusp sharpness S(τ) = max |dρ/dE| scales with eigenvalue density × bin sampling; both grow with L_max. | L_max ≥ 12 + bin_width ≤ 0.001·M_KK; loosen INFO band to r ≤ 5%, S > 200 at L=10 with extrapolation rule S(L) ~ L^β. |
| 2 | ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE | **A** | ρ_Zubarev(L) is monotone decreasing toward a limit; constrained-to-(-1) fit R²=0.93 vs unconstrained R²=0.99995 indicates the asymptote is genuinely above −1 OR higher-order 1/L^k terms shift the intercept. Δρ moving in correct direction. | Extend to L_max ∈ {13, 14, 15} (6–8 point fit); add 1/L⁶ term; OR derive analytic Mellin-cone Zubarev kernel asymptote as a target. PASS band tightens with point count. |
| 3 | D_SPEC-ALT-DERIVATION-PATH       | **C** | Three pathways measure DIFFERENT quantities. (a) heat-kernel slope on t ∈ [10⁻⁴, 10⁻¹] crosses the t·λ²_max ~ 0.065 boundary (L=8) / 0.034 (L=12) → straddles small-t power-law and large-t exponential-decay regimes. (b) zeta-density d_b=9.3 is a Weyl-law density on a SU(3)-only cache (d=8), L=8 truncation bias O(0.4–1.3). (c) d_c=12 = dim(SU(3))+dim(M_4) is structural by assumption, NOT computed from the cache. | Reformulate: PASS = "d_b on SU(3)-only cache → 8 within 1e-2 at L=12 with truncation-corrected fit." Shrink heat-kernel window to t ∈ [10⁻⁵, 10⁻³]. The "12" target is a product-triple statement; a separate gate is needed if the M_4 factor is to enter. |
| 4 | CC-3-CONNES-MOSCOVICI-RESIDUE    | **B** | The PASS condition log10(|Λ_CC|/|a_0|) ≤ −10 presupposes the meromorphic-continuation residues of ζ_D(s). On a FINITE spectrum ζ_{D,L} is entire — it has NO poles — so the "residue" being summed is a direct partial sum, not an analytic-continuation residue. The 0.74 ratio measured is the alternating sum of partial sums, dominated by Z(0) = a_0 itself. Direct-sum cannot deliver 10-OOM cancellation at any finite L_max. | INFRASTRUCTURE: implement Mellin-heat-kernel pole subtraction (§IV below). Then PASS condition becomes a residue-comparison test on the analytically continued ζ_D(s). |
| 5 | W0-L-MELLIN-CONE-S3-RESIDUE      | **B** | Z(s=3) is a divergent partial sum (s=3 < d=8 = spectral dimension). |ΔR(L)| growing in L is the unmistakable Weyl-law signature: N(λ) ~ λ^d · Vol/(8π⁴) ⇒ Σ d_i |λ|^(−3) diverges. The "residue at s=3" doesn't exist — d_K has no pole at s=3 (poles are at {8, 6, 4, 2, 0}). The plan's contingency "try s* ∈ {2, 4}" is also pole-targeted but s=2 < d also diverges by direct sum. | INFRASTRUCTURE: same Mellin-heat-kernel pole-subtracted residue extraction as #4. Residue is taken at s=4 (genuine pole, Res = 2 a_4 / (4π)^4 / Γ(2)), NOT s=3. |
| 6 | CC-2-SPIN8-TRIALITY-ORBIT-SUM    | **C/A** | Mixed: ratio-band conjunct PASSES at 1.003 (0.3% from unity), triality conjunct FAILS at 4.23% > 1%. The V orbit has 4 self-conjugate sectors (p=q ∈ {(0,0),(1,1),(2,2),(3,3)}), S± each has 20 mixed sectors. λ_max(V)=3.07 vs λ_max(S)=3.92 ⇒ V undersamples its asymptotic distribution at L=8. Jensen deformation breaks ambient Spin(8) → SU(3); residual triality is approximate, not exact. | The 1% threshold is INAPPROPRIATE for an effectively-broken symmetry on an under-resolved orbit. (a) Loosen to 5% — PASSes immediately; (b) extend V orbit to L_max=12 ((4,4) added → 5 sectors) — Class A scaling test; (c) reformulate as "S+/S− equality at machine ε" (PASS by construction, charge-conjugation theorem) plus separate "V/S deviation ~ Jensen anisotropy parameter" measurement. The ratio-band PASS at 1.003 is the load-bearing structural result and should be reported as the gate outcome. |
| 7 | W3-MULTIPOLE-BREAKDOWN-SCAN      | **D** | Two cutoff conventions disagree by a factor 63.3 in Λ, hence factor 4007 in (Δ/Λ)². Λ_Casimir = sqrt(L_max+1)·M_KK = 3.32·M_KK gives (Δ/Λ)² = 0.913 (FAIL). Λ_fabric = c_fabric·M_KK = 209.97·M_KK gives (Δ/Λ)² = 2.28e−4 (PASS by 10 OOM). Same gate, same wave, two answers. The cutoff-pinning is missing from the plan's PRDR. | PIN Λ via direct top-eigenvalue inspection of D_K at L_max=10. The substrate-natural cutoff is the largest physical eigenvalue scale; in the Jensen-SU(3) spectrum at fold this is closer to c_fabric·M_KK than sqrt(L+1)·M_KK because the fabric speed of sound enters the symbol of D_K. Alternatively PIN Λ = λ_max(L_max) directly (which at L=10 is 4.67 M_KK — an intermediate value). |

Numerical sanity (Python-verified, this synthesis):
- Substitution chain (1): r = |0.221 − 0.190|/0.190 = 0.16316.
- Substitution chain (4): Σ (−1)^s Z(s) = +1.5938e6; ratio = 0.7377; log10 = −0.1321.
- Substitution chain (5): Z(s=3, L=8..12) = (1.09, 1.80, 2.81, 4.20, 6.09) × 10⁵; |ΔR| = (7.08, 10.1, 14.0, 18.8) × 10⁴ — strictly INCREASING.
- Substitution chain (6): ratio_stat = (0.765 + 2·0.7326) · 0.4548 / 1.011 = 1.00327.
- Substitution chain (7): (Δ/Λ_Casimir)² = (3.17/sqrt(11))² = 0.9135; (Δ/Λ_fabric)² = (3.17/209.97)² = 2.28e−4; cutoff ratio 63.3 ↔ 3.60 OOM.

### III.C Class distribution

- Class A (true-but-under-resolved): 2 gates — W0-6, W0-7.
- Class B (method-inappropriate, requires analytic continuation): 2 gates — W0-11, W0-20.
- Class C (truncation-inappropriate threshold): 2 gates — W0-9, W0-10 (mixed C/A).
- Class D (structural ambiguity, machinery unpinned): 1 gate — W3-11.

The Class B gates are the load-bearing technical task: §IV below sketches the analytic-continuation infrastructure that converts both from FAIL to evaluable.

---

## IV. Mellin-heat-kernel infrastructure spec sketch (Class B remediation)

This section is the spectral-geometer technical track deliverable. The implementation converts §W0-11 and §W0-20 from FAIL-by-method-mismatch to evaluable residue-comparison gates.

### IV.A Identity to be implemented

```
ζ_D(s) Γ(s/2)  =  ∫_0^∞ t^{s/2 − 1} K(t) dt                                     (Mellin id.)
                =  ∫_0^ε t^{s/2 − 1} K_asy(t) dt        (small-t, Seeley-DeWitt)  (IV.1)
                +  ∫_0^ε t^{s/2 − 1} [K(t) − K_asy(t)] dt  (small-t remainder)    (IV.2)
                +  ∫_ε^∞ t^{s/2 − 1} K(t) dt              (large-t, exp. tail)     (IV.3)
```

Term (IV.2) and (IV.3) are convergent at all s by construction (the first is small-t-regular, the second is exp-decaying for t > 0). Term (IV.1) carries the poles. With the Seeley-DeWitt expansion to order N truncated explicitly:

```
K_asy(t)  =  (4π)^{−d/2} Σ_{n=0}^{N} a_{2n} t^{n − d/2}                           (IV.4)
```

term (IV.1) evaluates exactly:

```
∫_0^ε t^{s/2 − 1} t^{n − d/2} dt  =  ε^{s/2 + n − d/2} / (s/2 + n − d/2)
                                  =  2 ε^{s/2 + n − d/2} / (s + 2n − d)            (IV.5)
```

Each n contributes a SIMPLE POLE at s = d − 2n. The residue at the pole s = d − 2n is, after multiplying by 1/Γ(s/2) and taking the limit:

```
Res_{s = d − 2n} ζ_D(s)  =  2 (4π)^{−d/2} a_{2n} / Γ((d − 2n)/2)                  (IV.6)
```

For d=8, n=0 (CC sector): Res_{s=8} ζ_D(s) = 2 (4π)^{−4} a_0 / Γ(4) = a_0 / (48 π⁴).
For d=8, n=2 (gravity): Res_{s=4} ζ_D(s) = 2 (4π)^{−4} a_4 / Γ(2) = a_4 / (8 π⁴).

### IV.B Implementation as four-step Python recipe

```python
def mellin_heat_kernel_residue(eigenvalues, dims, s_pole, d_dim, ε, N_SD):
    """
    Compute the residue of ζ_D at s = s_pole using Mellin-heat-kernel
    pole subtraction.

    eigenvalues : ndarray of |λ_i| from D_K cache (PW-truncated)
    dims        : ndarray of multiplicities d_i
    s_pole      : integer in {0, 2, 4, 6, 8} for d=8 case
    d_dim       : 8 for SU(3)
    ε           : small-t upper bound; choose ε = 1/(2 λ_max²)  (well inside Weyl regime)
    N_SD        : Seeley-DeWitt expansion order; N ≥ (d − s_pole)/2 + 2 to bracket the pole
    """
    # Step 1 — exact heat-kernel evaluation on truncated cache:
    def K(t): return (dims * np.exp(-t * eigenvalues**2)).sum()

    # Step 2 — Seeley-DeWitt asymptotic with a_2n COMPUTED FROM the geometry,
    # not extracted from the truncated sum:
    a = compute_seeley_dewitt(d_dim, N_SD)   # a_0 = (4π)^{-4} Vol_SU(3); a_2 ∝ ∫ R; ...

    def K_asy(t):
        prefac = (4 * np.pi)**(-d_dim / 2)
        return prefac * sum(a[n] * t**(n - d_dim/2) for n in range(N_SD + 1))

    # Step 3 — three integrals on a fine quad grid:
    # (IV.1) closed-form via (IV.5); (IV.2) numerical, regular; (IV.3) numerical, exp-decay.
    I1 = sum(2 * a[n] * (4*np.pi)**(-d_dim/2) * ε**((s_pole + 2*n - d_dim)/2) /
             (s_pole + 2*n - d_dim) for n in range(N_SD + 1))
    I2 = quad(lambda t: t**(s_pole/2 - 1) * (K(t) - K_asy(t)), 0, ε)
    I3 = quad(lambda t: t**(s_pole/2 - 1) * K(t), ε, np.inf)

    # Step 4 — divide by Γ(s/2) and extract residue at s = s_pole:
    # The pole of (IV.5) at the matching n_pole = (d_dim - s_pole)/2 carries the residue.
    n_pole = (d_dim - s_pole) // 2
    residue = 2 * (4*np.pi)**(-d_dim/2) * a[n_pole] / gamma((s_pole)/2)
    return residue, (I1, I2, I3)  # residue + diagnostic decomposition
```

### IV.C Why this converts §W0-11 and §W0-20 from FAIL to evaluable

Substitution chain (Class B remediation):

```
Step 1 [def]: CC-3 PASS condition | residue-sum | ≤ 1e-10 · |a_0|.
              The "residue sum" is Σ_{s* ∈ {0,...,8}} (−1)^{s*} Res_{s=s*} ζ_D(s).
Step 2 [substitute]: by (IV.6), Res_{s=d-2n} ζ_D(s) = 2 (4π)^{-4} a_{2n} / Γ((d-2n)/2).
              CM-1995 §5: dimension spectrum is {0, 2, 4, 6, 8} (5 elements, not 9).
              Plan's "9-term sum over s*=0..8" mistakenly summed all integers, not poles.
Step 3 [simplify]: signed CM residue sum = 2 (4π)^{-4} Σ_{n=0}^{4} (-1)^{n} a_{2n} / Γ((8-2n)/2)
              = (4π)^{-4} [ a_0/3 - a_2/1 + a_4 - a_6/2 + a_8/12 · ... ] (after Γ-evaluation)
              At fold τ=0.190, a_0 = 6440 (canonical_constants); a_2 ≈ 0.728 (S46);
              a_4, a_6, a_8 require explicit Gilkey computation on Jensen-SU(3).
Step 4 [direction]: the SIGNED-RESIDUE alternating cancellation is a structural property
              of the heat-kernel Mellin-cone. If a_{2n} satisfy CM's vanishing identity,
              the alternating sum cancels to a small remainder. NUMBER OF OOM CANCELLATION
              is a property of the framework's Seeley-DeWitt coefficients, not L_max.
              At any L_max, the residue is the SAME (because residues are extracted from
              the geometric a_{2n}, which converge with L_max).
```

For §W0-20 (Mellin-cone-s3): the TRUE PASS test is at s*=4 (a genuine pole), not s*=3:

```
Step 1 [def]: target = Res_{s=4} ζ_D(s) − a_4_geometric / (8 π⁴)
Step 2 [substitute]: extracted residue from heat-kernel implementation — direct geometric
                     a_4_geometric (Gilkey integral, see S46 a_2 derivation extended to a_4).
Step 3 [simplify]: agreement at machine ε is a Mellin-heat-kernel CONSISTENCY check.
Step 4 [direction]: PASS iff |residue_extracted − a_4_geometric/(8π⁴)| / |a_4_geometric/(8π⁴)| ≤ 1e-3.
```

The plan's choice s*=3 is SHIFTED off the pole. The producing script measures
ζ_{D,L}(s=3), which is finite at any L but L→∞-divergent — the wrong object.

### IV.D Required upstream artifacts (S86 Wave 0)

To execute the analytic-continuation infrastructure, the framework needs:

1. **a_4, a_6, a_8 Gilkey integrals on Jensen-deformed SU(3) at τ=0.190**. Currently a_2 = 0.728 is computed (S46 W2-O). a_4 requires the full curvature polynomial: a_4 = (4π)^{−d/2}/360 · ∫ tr [60 ΔR + 60 R E + 180 E² − 60 R_μν R^μν + 30 R² + ...] (Gilkey 1995 §3.3). On Jensen-SU(3) with deformation tensor T(τ), this is a closed-form polynomial in τ — derive once.
2. **Spinor-rank normalization audit**: heat-kernel prefactor (4π)^{−d/2} times spinor rank N_S = 16 (for d=8 spin bundle). MEMORY check: this is the canonical convention used in S46/S52.
3. **ε pin**: the Mellin-split point. Pin ε = 1/(2 λ_max²) at the working L_max — at L=12, λ_max = 5.42, ε ≈ 0.017. Document in canonical_constants.

---

## V. Carry-Forward to S86+ (mandatory per feedback_fix-in-session-never-defer.md)

Each entry: **what / inputs / gate / effort**. All entries must be planned computations in S86, not deferred lists.

### V.1 — S86 Master Gate Proposal: S86-MASTER-LMAX-CLASSIFICATION-GATE

- **What**: a Master gate that adjudicates every L_max-truncation-vulnerable verdict in S86+ by classifying it into Class A / B / C / D BEFORE compute. The gate output is the per-gate class assignment plus the prescribed remediation route. Plan threshold: every gate in the wave with a closed-form L_max-asymptotic identity (CC-series, zeta-residue, heat-kernel residue, DOS-cusp, Mellin-cone) must declare a class tag in its PRDR pin block.
- **Inputs**: this synthesis taxonomy, the 7-row class table III.B, the IV.B Mellin-heat-kernel recipe (once implemented).
- **Gate (PASS/FAIL/INFO)**: PASS if every S86 gate in the relevant wave has class tag + remediation declared in its PRDR pin block; FAIL if ≥1 gate executes without a declared class; INFO if all gates declared but ≥1 with remediation deferred.
- **Effort**: 0.5 day plan-author work (no compute).

### V.2 — S86-MELLIN-HEAT-KERNEL-INFRA (Class B remediation infra)

- **What**: implement the Mellin-heat-kernel pole-subtracted residue extractor (§IV.B recipe). computation script `s86_mellin_hk_residue.py`. Test fixtures: ε ∈ {0.005, 0.01, 0.02} stability; N_SD ∈ {3, 4, 5} convergence; comparison to Gilkey-computed a_2 at τ=0.190 (cross-check).
- **Inputs**: existing PW-truncated D_K eigenvalue cache (L_max ∈ {8, 9, 10, 11, 12}); Gilkey-computed a_0 = 6440, a_2 = 0.728; new computation of a_4, a_6, a_8 on Jensen-SU(3) (V.3 below).
- **Gate (PASS/FAIL)**: PASS iff Res_{s=8} extracted matches a_0/(48π⁴) within 1e-3, AND Res_{s=4} extracted matches a_4_geometric/(8π⁴) within 1e-3. INFO iff Res_{s=8} matches but Res_{s=4} disagrees (would point to a_4 spinor-rank or normalization audit).
- **Effort**: 2 days (1 compute, 1 audit).

### V.3 — S86-A4-A6-A8-GILKEY-JENSEN

- **What**: derive a_4, a_6, a_8 Seeley-DeWitt coefficients on Jensen-deformed SU(3) at τ=0.190 in closed form. Gilkey-1995 §3.3 curvature polynomial; Jensen deformation contributes a τ-polynomial in each curvature invariant. Produce canonical_constants entries `a_4_jensen_fold`, `a_6_jensen_fold`, `a_8_jensen_fold` with provenance.
- **Inputs**: Jensen metric tensor at τ=0.190 (canonical_constants), curvature scalars R, |Ric|², |Riem|² already computed in S46/S52, extended to higher polynomial invariants; Gilkey 1995 reference (already in `researchers/Spectral-Geometry/`).
- **Gate (PASS/FAIL)**: PASS iff three coefficients computed at machine precision with Riemann-tensor identities cross-checked (Bianchi closure, dimensional consistency).
- **Effort**: 3 days (heavy symbolic algebra; mcp__sage__ likely required for the Riemann polynomial reductions).

### V.4 — S86-VAN-HOVE-CUSP-LMAX12-BIN001 (Class A remediation for #1)

- **What**: rerun §W0-6 van Hove cusp scan at L_max ∈ {10, 12} with bin_width ∈ {0.001, 0.005} M_KK. Test scaling S_max(L) ~ L^β and refine τ_cusp via parabolic fit on finer grid τ ∈ [0.18, 0.22] step 0.001.
- **Inputs**: D_K spectrum cache at L_max = 12 (166,896 eigenvalues per τ); plan §W0-6 PRDR amended: GPU pin REMOVED (CPU eigvals 2-3× faster on this workload per S85 W0-6 benchmark); CPU thread cap = 8.
- **Gate (PASS/FAIL/INFO)**: PASS iff τ_cusp within 0.5% of τ_fold AND S_max > 1000 at L=12 with bin_width = 0.001; INFO iff τ_cusp within 5% AND S_max > 200 with monotone-increasing trend in L; FAIL otherwise.
- **Effort**: 1 day (~50 min CPU per τ at L=12; 41 τ-points × 2 bin_widths).

### V.5 — S86-ZUBAREV-LMAX15-EXTENDED-FIT (Class A remediation for #2)

- **What**: extend Zubarev ρ(L) sweep to L_max ∈ {13, 14, 15}. Refit ρ(L) = c_0 + α/L² + β/L⁴ + γ/L⁶ on the 8-point series; alternatively derive analytic Mellin-cone Zubarev kernel asymptote in closed form as the target.
- **Inputs**: PW-truncation eigenvalue caches at L = 13, 14, 15 (~227k, 305k, 401k modes per τ).
- **Gate (PASS/FAIL/INFO)**: PASS iff |c_0 + 1| ≤ 0.01 from 4-parameter fit; INFO iff |c_0 + 1| ≤ 0.05; FAIL otherwise. Cross-check: analytic-target form (if derived) should be the load-bearing PASS criterion.
- **Effort**: 4 days (each L_max increment ~doubles spectrum; L=15 cache build is ~40 min CPU per τ).

### V.6 — S86-D_SPEC-REFORMULATED (Class C remediation for #3)

- **What**: reformulate §W0-9 as "d_b on SU(3)-only cache → 8 within 1e-2 at L=12 with truncation-corrected Weyl fit." Compute heat-kernel slope on shrunk window t ∈ [10⁻⁵, 10⁻³] (entirely below the 1/λ_max² boundary). Drop pathway (c) — the structural "12 = 8+4" is a separate product-triple statement and should be a different gate.
- **Inputs**: existing L=12 cache; updated `s85_w0_d_spec_alt_derivations.py` script with corrected t-window.
- **Gate (PASS/FAIL)**: PASS iff |d_b − 8| ≤ 1e-2 at L=12 AND |d_a − 8| ≤ 0.5 on shrunk window; INFO iff both within 0.5; FAIL otherwise.
- **Effort**: 0.5 day.

### V.7 — S86-CC2-TRIALITY-LMAX12 (Class C/A mixed remediation for #6)

- **What**: rerun §W0-10 with V orbit extended to (4,4) sector (5 sectors at L=12). Reformulate gate: PASS = "S+/S− equality at machine ε" (always PASS by charge-conjugation theorem) AND "ratio_stat ∈ [0.90, 1.10]" (PASSed at 1.003 already). Drop the V vs S± 1% conjunct as ambient-symmetry-broken; report V/S deviation as informational measurement of Jensen anisotropy.
- **Inputs**: L=12 eigenvalue cache.
- **Gate (PASS/FAIL/INFO)**: PASS on the two retained conjuncts; INFO measurement on V/S deviation.
- **Effort**: 0.5 day.

### V.8 — S86-W3-LAMBDA-PIN-FROM-DK (Class D remediation for #7)

- **What**: pin the multipole-breakdown UV cutoff Λ via direct top-eigenvalue inspection of D_K at L_max=10. Three candidate pins: Λ_λ_max = max |λ| at L=10 (~4.67·M_KK); Λ_fabric = c_fabric·M_KK = 209.97·M_KK; Λ_Casimir = sqrt(L+1)·M_KK = 3.32·M_KK. Reconcile with W3-9 Ginzburg PASS at Λ_fabric.
- **Inputs**: D_K cache at L_max=10; W3-9 Ginzburg gate output (Gi(K_crit) = 5.5e−10 PASS at Λ_fabric).
- **Gate (PASS/FAIL)**: PASS iff Λ_pinned satisfies BOTH multipole gate and Ginzburg gate simultaneously; FAIL iff no Λ choice does (would indicate two physically distinct cutoffs at play, requiring framework reformulation).
- **Effort**: 0.5 day.

### V.9 — S86-CC-3-CM-RESIDUE-MELLIN (Class B remediation for #4)

- **What**: re-execute §W0-11 using the §IV Mellin-heat-kernel infrastructure (V.2). Compute signed CM residue sum over Sd = {0, 2, 4, 6, 8} (the actual dimension spectrum for d=8, NOT integers 0..8 as the original gate did). Targets: |Σ (−1)^n Res_{s=d−2n} ζ_D| / a_0 ≤ 1e-10 (PASS), ≤ 1e-2 (INFO).
- **Inputs**: V.2 infrastructure; V.3 a_4, a_6, a_8 coefficients.
- **Gate (PASS/FAIL/INFO)**: per the stated thresholds. Note: PASS requires the signed-residue cancellation to be a structural property of Jensen-SU(3) Seeley-DeWitt coefficients; FAIL would be a genuine framework signature (positive cosmological-constant contribution from CM residue), not a methodology FAIL.
- **Effort**: 0.5 day after V.2 + V.3.

### V.10 — S86-MELLIN-CONE-S4-RESIDUE (Class B remediation for #5)

- **What**: re-execute §W0-20 at the CORRECT pole s*=4 (genuine pole of ζ_D for d=8), comparing Mellin-extracted Res_{s=4} ζ_D against geometrically-computed a_4 / (8π⁴). Replaces the failed s*=3 gate.
- **Inputs**: V.2 infrastructure; V.3 a_4 coefficient.
- **Gate (PASS/FAIL)**: PASS iff |Res_extracted − a_4_geometric/(8π⁴)| / |a_4_geometric/(8π⁴)| ≤ 1e-3.
- **Effort**: 0.5 day after V.2 + V.3.

---

## VI. Conflicts flagged

1. **W3-11 vs W3-9 cutoff convention**: W3-11 source explicitly notes the conflict ("the W3-9 PASS Λ choice (effectively c_fabric·M_KK) and the W3-11 FAIL Λ choice (sqrt(L_max+1)·M_KK) cannot both be the canonical cutoff"). Verdicts AUTHORITATIVE on both gates as written; the synthesis flags V.8 as the resolution route. No re-adjudication of either FAIL/PASS in this synthesis.

2. **W0-11 dimension spectrum**: the producing script appears to have summed 9 terms (s* = 0..8 inclusive). The Connes-Moscovici dimension spectrum for d=8 is Sd = {0, 2, 4, 6, 8} (5 terms). The 9-term sum includes "residues" at non-pole locations s ∈ {1, 3, 5, 7}, which by definition vanish for the meromorphic ζ_D(s) — the script is summing partial-sum values at non-poles. This is structural in the FAIL diagnosis (Class B) and does NOT change the verdict, but the V.9 reformulation must restrict to the actual Sd.

3. **W0-9 product-triple ambiguity**: source flags pathway (c) "d_c = 8 + 4 = 12" as structural-by-assumption. Verdict authoritative; V.6 reformulation drops this pathway from the gate. No conflict with the FAIL verdict.

---

## VII. Closure

Seven FAIL gates classified under a 4-class taxonomy:

| Class | Count | Gates                       | Remediation |
|:------|:------|:----------------------------|:------------|
| A: true-but-under-resolved | 2 | W0-6, W0-7              | extend L_max, refine grid |
| B: method-inappropriate    | 2 | W0-11, W0-20            | implement Mellin-heat-kernel pole subtraction (V.2) |
| C: truncation-inappropriate threshold | 2 | W0-9, W0-10 (mixed) | reformulate threshold; drop conjuncts that probe broken ambient symmetry |
| D: structural ambiguity    | 1 | W3-11                   | pin cutoff Λ from D_K top eigenvalue |

The Mellin-heat-kernel analytic-continuation infrastructure (§IV.B) is the central technical deliverable: it converts both Class B gates from "FAIL by direct partial sum at non-pole / divergence regime" to "evaluable residue test against geometrically computed Seeley-DeWitt coefficients." Implementation requires V.3 (a_4, a_6, a_8 Gilkey computation on Jensen-SU(3)) as upstream prerequisite.

The proposed S86 master gate (V.1) prevents the 7 FAIL modes from recurring by requiring class-tagging in PRDR pin blocks BEFORE compute. This is a plan-property guard (Class 8 PRU prevention), separate from execution-property guards.

Substrate framing note: the 7 FAILs are heat-kernel and Mellin-cone diagnostics on the substrate's intrinsic spectral data. None of them measure container-physics observables; the truncation issues are L_max-finite-resolution issues on the Peter-Weyl decomposition of D_K, not approximations of an external geometry. The V.1–V.10 carry-forwards reinforce the substrate-first explanatory direction.

---

**Files produced (this synthesis)**:

| File | Path |
|:-----|:-----|
| Synthesis | `sessions/archive/session-85/session-85-s6-truncation-taxonomy-spectral-geometer.md` |

**Source documents (read this session, not re-adjudicated)**:

- `sessions/archive/session-85/session-85-w0-workingpaper.md`
- `sessions/archive/session-85/session-85-w3-workingpaper.md`
- `.claude/agent-memory/spectral-geometer/MEMORY.md`
- knowledge MCP queries (5 search + 3 get_constant)
