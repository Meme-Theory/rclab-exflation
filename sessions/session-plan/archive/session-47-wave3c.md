## Wave 3c: Deformation Response of Character Coherence Function (1 task)

Naz's substrate reframe produced xi_C = 0.55 rad — the character coherence length at the fold. This is one number at one tau. The decisive test: does this coherence length TRACK the BCS physics across tau, or is it a truncation artifact? If it anti-correlates with Delta_B2(tau) at |r| > 0.9, the coherence function is dynamically determined — real substrate self-coherence. If |r| < 0.3, it's Fourier analysis on a compact group.

---

### W3-3: Deformation Response of Character Coherence (COHERENCE-RESPONSE-47)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Cost**: MEDIUM (condensate torus computation at 26 tau values)

**Prompt**:

You proposed this test in your substrate reframe document. Now you execute it.

**THE TEST**: Compute C(θ, 0; τ) — the character coherence function on T² — at 26 tau values in [0, 0.50]. Extract the 1/e² radius r_C(τ) at each tau. Correlate with Delta_B2(τ).

**Two predictions**:

**Null hypothesis (Fourier artifact)**: r_C is determined by truncation (max_pq_sum), not physics. It will be approximately constant across tau, because the identity peak is kinematic — all characters satisfy χ(e) = dim(p,q) regardless of tau. BCS weights modulate weakly (factor 2-3) but don't produce qualitatively different behavior at different tau. The contrast ratio ≈ dim(max_rep)²/dim(min_rep)² at every tau.

**Alternative hypothesis (substrate self-coherence)**: r_C tracks Delta_B2(τ), not truncation. Specifically r_C(τ) ~ 1/Delta_B2(τ) — wider coherence when pairing is weaker (less spectral weight in higher reps = slower character decay), narrower when stronger. Contrast varies by orders of magnitude across tau. At τ_c where BCS vanishes, the coherence flattens to truncation-dominated.

**Decisive criterion**: Plot r_C(τ) versus Delta_B2(τ). If anti-correlation |r| > 0.9 across 26 tau values → dynamically determined (substrate). If |r| < 0.3 → kinematically determined (artifact).

**The nuclear analog**: In a deformed nucleus, Δ(r) changes shape when deformation changes. At spherical (β₂ = 0), Δ follows spherical density. At large deformation, Δ becomes prolate/oblate. The RESPONSE of the pairing field to deformation tests self-consistency — a truly self-consistent solution has the pairing field track the density, not the external potential. Here, the RESPONSE of C(θ; τ) to the Jensen parameter τ tests whether the coherence function tracks BCS physics or truncation.

### Verified data locations

**s44_dos_tau.npz** — eigenvalues at 5 tau values:
- `tau0.00_all_omega: shape=(992,)`, `tau0.00_all_dim2: shape=(992,)`
- `tau0.05_all_omega: shape=(992,)`, `tau0.05_all_dim2: shape=(992,)`
- `tau0.10_all_omega: shape=(992,)`, `tau0.10_all_dim2: shape=(992,)`
- `tau0.15_all_omega: shape=(992,)`, `tau0.15_all_dim2: shape=(992,)`
- `tau0.19_all_omega: shape=(992,)`, `tau0.19_all_dim2: shape=(992,)`
- NOTE: Only 5 tau values have full 992-mode spectra, not 26.

**s46_qtheory_selfconsistent.npz** — BCS gaps at 60 tau values:
- `Delta_B1_sc: shape=(60,)`, `Delta_B2_sc: shape=(60,)`, `Delta_B3_sc: shape=(60,)`
- `tau_scan: shape=(60,)` — the 60 tau values
- `lam_sq_B1: shape=(20,)`, `lam_sq_B2: shape=(20,)`, `lam_sq_B3: shape=(20,)` — eigenvalues² at subset of tau
- `lam2_B1_interp: shape=(60,)`, `lam2_B2_interp: shape=(60,)`, `lam2_B3_interp: shape=(60,)` — interpolated eigenvalues² at all 60 tau

**s47_condensate_torus.py** — the W2-1 script that computes condensate on T². This has the character evaluation infrastructure. Adapt it to loop over tau values.

**s47_condensate_torus.npz** — W2-1 output at the fold:
- Contains the character computation setup, BCS weights, grid

**tier0-computation/canonical_constants.py**

### Computation Steps

1. **Resolve the tau grid issue.** Full 992-mode spectra exist at only 5 tau values (0.00, 0.05, 0.10, 0.15, 0.19). But the BCS gaps exist at 60 tau values. Two approaches:
   - **Approach A (5-point)**: Compute C(θ; τ) at the 5 available tau values. Extract r_C at each. Correlate with Delta_B2. Five points is minimal but may suffice if the trend is strong.
   - **Approach B (interpolated)**: Use lam2_Bx_interp (eigenvalues² interpolated to 60 tau) to reconstruct approximate spectra at all 60 tau values. The BCS weights (v_k² and Delta_k) at each tau determine the condensate, and if the eigenvalue evolution is smooth, interpolation is valid.

   **Use Approach B.** The eigenvalue ratios evolve smoothly with tau (confirmed by the 5 data points). Interpolate the (0,0) sector eigenvalues and the sector-averaged BCS gaps to a common tau grid. Then compute C(θ; τ) on that grid.

2. **Adapt the condensate computation.** From s47_condensate_torus.py, the condensate density uses:

   |Δ(θ₁,θ₂)|² ∝ Σ_{(p,q)} w_{(p,q)} × |χ_{(p,q)}(θ₁,θ₂)|²

   where w_{(p,q)} is the BCS weight (sector-averaged gap × occupation). The characters χ_{(p,q)} are tau-INDEPENDENT (they're representation characters, not spectrum). Only the WEIGHTS w_{(p,q)} change with tau through:
   - v²_sector(τ) — BCS occupation per sector (computable from Delta and eigenvalues)
   - Delta_sector(τ) — from s46_qtheory_selfconsistent

   So the computation is: at each tau, recompute the BCS weights, apply them to the SAME characters, evaluate on T², extract the coherence function.

3. **Compute C(θ; τ) at each tau.** The character coherence function is the condensate density restricted to the radial direction on T². Use the geodesic distance from the identity: θ parameterizes the "radial" direction. Evaluate |Δ(θ, 0)|² / |Δ(0, 0)|² = C(θ; τ). Extract:
   - r_C(τ) = 1/e² radius (where C drops to e⁻² ≈ 0.135)
   - Contrast ratio max/min at each tau
   - The full C(θ; τ) profile

4. **Compute Delta_B2(τ).** From s46_qtheory_selfconsistent: Delta_B2_sc at each tau on the 60-point grid.

5. **Correlate.** Plot r_C(τ) vs Delta_B2(τ). Compute Pearson correlation coefficient r. Report |r| and p-value.

6. **Also test against truncation.** The null hypothesis predicts r_C ≈ constant. Compute the coefficient of variation CV = std(r_C) / mean(r_C). If CV < 0.1, the radius is effectively constant (artifact). If CV > 0.3, it varies substantially (could be physical).

7. **Visualize.**
   - **Plot A**: r_C(τ) and Delta_B2(τ) on dual y-axes vs tau. If they anti-correlate, the curves should mirror each other.
   - **Plot B**: r_C vs Delta_B2 scatter plot with regression line. Report r and p.
   - **Plot C**: C(θ; τ) heatmap — theta on x-axis, tau on y-axis, color = coherence. Shows whether the coherence profile narrows/widens with tau.

### Pre-registered gate COHERENCE-RESPONSE-47
- **SUBSTRATE**: |r| > 0.9 between r_C and Delta_B2 (or 1/Delta_B2) — coherence is dynamically determined
- **AMBIGUOUS**: 0.3 < |r| < 0.9 — partial correlation, more data needed
- **ARTIFACT**: |r| < 0.3 — coherence is truncation-determined

This is a decisive, pre-registered test with quantitative thresholds. No post-hoc interpretation.

### Output files
- Script: `tier0-computation/s47_coherence_response.py`
- Data: `tier0-computation/s47_coherence_response.npz`
- Plot: `tier0-computation/s47_coherence_response.png`

### Working paper section: W3-3

### Critical notes
- Characters are tau-INDEPENDENT. Only the BCS weights change. This is what makes the test clean: the "Fourier basis" is fixed, only the "Fourier coefficients" (BCS weights) vary with tau. If r_C doesn't change, the weights don't matter and it's a basis artifact. If r_C does change, the weights are driving the coherence structure.
- At tau=0 (bi-invariant), the spectrum is maximally degenerate. BCS may not be well-defined (the gap equation may not converge). Handle this edge case — use the Delta_B2_sc value from the s46 data, which may be zero at tau=0.
- The 60-point tau grid from s46 extends beyond the fold (tau=0.19). The BCS gaps likely vanish at some tau_c > 0.19. What happens to r_C at and beyond tau_c is the most interesting part of the test.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
