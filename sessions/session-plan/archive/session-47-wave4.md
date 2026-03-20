## Wave 4: n_s Crisis Reassessment (2 tasks)

S46 closed every single-particle pair creation route to n_s = 0.965. The sole survivor is non-singlet dissipation at 3.8x shortfall. But S47 produced structural results that change the landscape:

- The superfluid density tensor is 24x anisotropic (ρ_s: C²=7.96, su(2)=0.50, u(1)=0.33)
- The condensate grips the soft curvature directions hardest (r=-0.906 anti-correlation)
- The crystal has protected geometric invariants (K=1/16, Ric(u(1))=1/4)
- The B2 funnel concentrates 91% of dynamics in the U(2) fundamental sector
- The character coherence function is kinematic (ARTIFACT), but the superfluid stiffness is dynamical (PASS)

The question: does any of this change the n_s picture? Volovik reassesses from scratch.

---

### W4-1: Volovik n_s Reassessment (NS-REASSESS-47)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: LOW-MEDIUM (analysis + possibly one computation)

**Prompt**:

You are reassessing the n_s crisis in light of ALL Session 47 results. This is not a review of S46 — it's a fresh look at the structural landscape after the crystal geometry, superfluid stiffness tensor, and coherence response results.

### The n_s Crisis (Status entering S47)

S46 closed 7 n_s routes (total ~10 closed). Every single-particle pair creation channel produces the wrong tilt. The structural wall:

- All hose-count/spectral-flow/LZ methods give wrong alpha or wrong sign
- Transfer function suppression: 56 orders of magnitude between ξ_KZ and λ_CMB
- d_eff floor = 3 (topological, K₇)
- Only 0.667 e-folds available
- Sole survivor: non-singlet dissipation at 3.8x shortfall (NONSINGLET-SELFCONSIST-47)

Your own S46 assessment: "The n_s crisis is real and deep... may require physics outside the pair creation paradigm entirely."

### What S47 Changed

**Read these files FIRST** (all of them):

1. `sessions/session-47/session-47-wave1-workingpaper.md` — ALL sections W1-1 through W3-4
2. `sessions/session-47/session-47-crystal-geometry.md` — Tesla's synthesis
3. `sessions/session-47/session-47-volovik-coherence-response.md` — your own coherence response
4. `tier0-computation/s47_rhos_tensor.npz` — the superfluid density tensor data
5. `tier0-computation/s47_curvature_anatomy.npz` — curvature data

**Key S47 results relevant to n_s**:

1. **ρ_s anisotropy 24x**: The condensate is not isotropically stiff. Dissipation in C² directions costs 24x more energy than in su(2) directions. If non-singlet Landau-Zener transitions are direction-dependent, the effective friction is direction-weighted — NOT the isotropic average used in S46.

2. **Soft-stiff anti-correlation**: The condensate grips hardest where the geometry is softest (C², K=0.010). This means the modes that dissipate energy most efficiently live in the geometrically compliant directions — the ones with the most phase space for excitations.

3. **Protected directions don't participate**: K(u(1), C²) = 1/16 exactly, ρ_s(u(1)) = 0.33 (weakest). The u(1) direction is geometrically protected but dynamically inert for dissipation. This removes 1/8 of the su(3) directions from the dissipation budget.

4. **B2 funnel**: 91% of pairing dynamics in B2. The 976 non-singlet modes are not equally weighted — B2 modes dominate. The effective mode count for dissipation may be much less than 976.

5. **Block-resolved structure**: QA-theorist's S46 suggestion — compute n_s as a crossover between B2-dominated (low k) and B3-dominated (high k) regimes, not a single power law.

### Your Task

Write a reassessment document at: `sessions/session-47/session-47-ns-reassessment.md`

Address:

1. **Does anisotropic ρ_s change the non-singlet dissipation estimate?** The S46 computation assumed isotropic friction. If the 976 non-singlet modes are weighted by their directional ρ_s, does the effective friction increase or decrease? Which direction dominates the LZ transitions?

   In your superfluid program: the mutual friction force in He-3 is anisotropic — it depends on the orientation of the vortex relative to the flow. The anisotropy ratio in He-3B is ~5-10x. Here it's 24x. Does the analogy transfer?

2. **Does the superfluid stiffness provide a new n_s mechanism?** The stiffness tensor ρ_s^{ab}(τ) varies by 40% across tau (CV=0.40). During transit, τ changes. The CHANGING stiffness during transit means the condensate's grip on the geometry evolves — tightening in some directions, loosening in others. Could this anisotropic evolution imprint a spectral tilt on the perturbations?

   Specifically: if the C² stiffness drops from 21 (early tau) to 8 (late tau), the condensate releases energy into C² directions during transit. This is a direction-dependent particle creation mechanism. Does it have the right k-dependence for n_s?

3. **Does the q-theory crossing at τ*=0.209 interact with the stiffness?** Your coherence response document noted that q-theory F(τ) survives as a dynamical probe, with a crossing at 0.209 (near the fold at 0.19). If the vacuum energy equilibrium selects τ*=0.209, and the stiffness tensor at 0.209 differs from 0.19, what are the implications for the perturbation spectrum?

4. **Is the 56-order gap bridgeable through the fabric?** The tessellation (S42, 32-cell) provides a spatial structure at scales >> ξ_KZ. Each cell has its own τ value, its own condensate, its own ρ_s tensor. The inter-cell coupling through shared boundaries could propagate perturbations from ξ_KZ to much larger scales. Does the anisotropic stiffness affect how perturbations propagate between cells?

5. **Your revised assessment.** After considering all of the above: is the n_s crisis still terminal for pair creation mechanisms? Does S47 open any new path? Or does it confirm Volovik's S46 verdict that external physics (curvaton, defects, pre-transit slow-roll) is required?

6. **If a new path exists, pre-register a gate.** Specify: what to compute, what data to use, what PASS/FAIL means.

### Rules
- Read ALL specified files before writing.
- Ground in YOUR papers and the superfluid program.
- Be honest. If S47 doesn't change the n_s picture, say so.
- If it does change the picture, be specific about HOW and WHAT COMPUTATION would test it.
- 200-400 lines.
- Working directory: C:\sandbox\Ainulindale Exflation (space in path — quote in shell)

---

### W4-2: Anisotropic Non-Singlet Dissipation (ANISO-DISSIP-47)

**Agent**: `landau-condensed-matter-theorist`
**Model**: opus
**Cost**: MEDIUM (direction-resolved LZ computation)
**Depends**: Can run in parallel with W4-1, but W4-1's conclusions may reframe the interpretation

**Prompt**:

You computed the superfluid density tensor in W3-4 (RHOS-TENSOR-47: PASS, anisotropy 24x). Now apply it to the n_s problem: recompute the non-singlet Landau-Zener dissipation with direction-dependent weighting from the ρ_s tensor.

### Background

S46 W4-5 computed non-singlet dissipation isotropically: 976 non-singlet modes, each contributing LZ transition probability P_k = exp(-π Δ_k² / (ℏ v_k)), summed uniformly. Result: 3.8x shortfall from the target friction.

Your ρ_s tensor shows the condensate stiffness is 24x anisotropic: C²=7.96, su(2)=0.50, u(1)=0.33. If the LZ transitions are mediated by current operators in specific su(3) directions, the effective friction should be weighted by the directional stiffness.

### The question

Does direction-weighting the 976 non-singlet modes by their ρ_s projections close the 3.8x gap?

### Verified data locations

**tier0-computation/s47_rhos_tensor.npz**:
- `rho_s_all: shape=(16, 8, 8)` — full tensor at 16 tau values
- `rho_s_eigs_all: shape=(16, 8)` — eigenvalues at each tau
- `rho_s_fold: shape=(8, 8)` — tensor at fold
- `rho_s_eigs_fold: shape=(8,)` — [0.327, 0.505, 0.505, 0.505, 7.962, 7.962, 7.962, 7.962]
- `K_per_dir: shape=(8,)` — curvature per direction for cross-reference
- `tau_sweep: shape=(16,)` — tau values

**S46 non-singlet dissipation data** — check for:
- `tier0-computation/s46_nonsinglet_dissipation.npz` — may contain the S46 isotropic LZ result
- `tier0-computation/s46_landau_zener_ns.npz` — LZ transition data

**s44_dos_tau.npz** — full 992-mode spectrum at 5 tau values

**s46_qtheory_selfconsistent.npz** — gaps at 60 tau values

**canonical_constants.py**

### Computation Steps

1. **Load the S46 non-singlet dissipation data.** Find the LZ transition probabilities, mode energies, and friction sum from the S46 computation. Identify the 976 non-singlet modes.

2. **Classify non-singlet modes by su(3) direction.** Each non-singlet mode (p,q) ≠ (0,0) transforms under a specific representation of SU(3). The current operator coupling that mode to the condensate projects onto su(3) directions. Classify each mode's primary coupling direction: u(1), su(2), or C².

   Practical approach: the representation matrices ρ(X_a) for each (p,q) sector determine which directions couple. For the fundamental (1,0) and anti-fundamental (0,1), all 8 generators have nonzero matrix elements but with different weights. The C² generators (X_4...X_7) connect B1↔B2 and B2↔B3 (from the W3-4 current operator analysis), while su(2) generators (X_1,X_2,X_3) connect B1↔B3.

3. **Weight each mode's LZ contribution by ρ_s.** For mode k with primary direction a:

   F_k^{aniso} = P_k × ρ_s^{aa}(τ)

   vs the isotropic version:

   F_k^{iso} = P_k × (1/8) Tr(ρ_s)

4. **Sum over all 976 modes.** Compare:
   - F_total^{iso} = Σ_k F_k^{iso} (the S46 result, 3.8x short)
   - F_total^{aniso} = Σ_k F_k^{aniso} (the direction-weighted result)
   - Ratio: F_aniso / F_iso — this tells you whether anisotropy helps or hurts

5. **Report the updated shortfall.** If F_aniso > F_iso, the shortfall decreases (anisotropy helps). If F_aniso < F_iso, it increases (anisotropy hurts). The C² modes (ρ_s=7.96) should dominate if they also have the largest LZ probabilities.

6. **Sensitivity to tau.** Repeat at multiple tau values. The ρ_s tensor changes by 40% across tau — does the anisotropic friction peak at the fold or elsewhere?

### Pre-registered gate ANISO-DISSIP-47
- **PASS**: Anisotropic shortfall < 2.0x (direction-weighting closes more than half the 3.8x gap)
- **INFO**: 2.0x < shortfall < 3.8x (anisotropy helps but doesn't resolve)
- **FAIL**: Shortfall ≥ 3.8x (anisotropy doesn't help or makes it worse)

### Output files
- Script: `tier0-computation/s47_aniso_dissip.py`
- Data: `tier0-computation/s47_aniso_dissip.npz`
- Plot: `tier0-computation/s47_aniso_dissip.png`

### Working paper section: W4-2

### Critical notes
- The direction classification of non-singlet modes is approximate — each mode couples to multiple directions. Use the DOMINANT direction (largest |ρ(X_a)| matrix element) as the primary.
- If you can't cleanly decompose all 976 modes by direction, use the sector-level approximation: B2 modes → C² coupling, B3 modes → su(2) coupling, B1 modes → mixed. This is coarser but captures the main effect.
- The S46 3.8x shortfall may be stored in s46_nonsinglet_dissipation.npz or s46_landau_zener_ns.npz. Check both. If neither has the raw friction sum, reconstruct from the S46 computation description.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
