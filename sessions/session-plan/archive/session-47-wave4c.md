## Wave 4c: Spectral Flow Through the Q-Theory Potential (1 task)

Volovik's n_s reassessment identified three surviving paths. Path C — the texture spectrum across the fabric — is the most novel but requires multi-cell infrastructure that doesn't exist yet. This task investigates a related but more immediately computable mechanism from the same Volovik corpus:

**Spectral flow through the q-theory potential well.** Not pair creation (Bogoliubov quench). Not dissipation (LZ friction). Adiabatic spectral flow of BdG levels as tau traverses the q-theory potential landscape.

In 3He-A (Paper 09, Paper 04), spectral flow through the Fermi point produces the chiral anomaly with a specific spectral index related to the Fermi point topology (winding number N₃ = ±1). The framework has N₃ = 0 (BDI class, 3He-B, Paper 28) — no Fermi point, no chiral anomaly. But the q-theory potential well (Papers 15-16, crossing at τ* = 0.209 from S46) provides a different landscape for spectral flow: as tau evolves through the well, the BdG quasiparticle spectrum changes, levels shift, and the occupation numbers of the GGE relic are set by which levels crossed what thresholds during transit.

The question: does this spectral flow have a k-dependent rate that produces a specific n_s?

---

### W4-3: BDI Spectral Flow and n_s (SPECTRAL-FLOW-NS-47)

**Agent**: `volovik-superfluid-universe-theorist`
**Model**: opus
**Cost**: MEDIUM (spectral flow computation + analytic theory)

**Prompt**:

You are investigating whether adiabatic spectral flow of BdG levels through the q-theory potential well can produce a primordial perturbation spectrum with the correct tilt. This is Path C from your own n_s reassessment, adapted to the BDI classification of the framework.

### The Mechanism

In 3He-A (your Paper 09), the chiral anomaly arises from spectral flow: as a texture (vortex) evolves, quasiparticle levels flow through the Fermi point. The rate of spectral flow is topologically quantized by N₃:

  dN/dt = N₃ × (topological charge of texture) × (rate of texture evolution)

This produces a specific anomalous current with known spectral properties.

The framework is BDI (Paper 28), not the Fermi-point class. N₃ = 0. No chiral anomaly. BUT:

1. The BdG spectrum has a GAP, not a Fermi point. Levels don't flow through zero energy — they flow across the gap edge.
2. The q-theory potential V(τ) has a well with crossing at τ* = 0.209 (S46). As τ evolves from 0 to ~0.4 during transit, the BdG spectrum changes continuously.
3. At each τ, the quasiparticle energies E_k(τ) = sqrt(ξ_k(τ)² + Δ_k(τ)²) shift. Some levels approach the gap edge, some move away.
4. The GGE relic (S38: 8 Richardson-Gaudin conserved quantities, 59.8 quasiparticle pairs) is the FROZEN snapshot of this spectral flow. The occupation numbers {n_k} of the GGE are determined by the history of spectral flow during transit.

The question: if the spectral flow rate is k-dependent (different PW sectors flow at different rates), the GGE relic inherits a k-dependent occupation spectrum. That occupation spectrum IS the primordial perturbation spectrum — not from pair creation events, but from the adiabatic evolution of the BdG spectrum through the q-theory landscape.

### Key distinction from S46 pair creation routes

S46 computed n_s from:
- Bogoliubov pair creation (sudden quench, |β_k|² ~ (Δ/ω)⁴)
- LZ transitions (non-adiabatic, P = exp(-πΔ²/ℏv))
- Hose count (counting modes)

All of these are PRODUCTION mechanisms — they ask "how many pairs are created at each k?"

Spectral flow is different. It asks: "as the BdG spectrum evolves adiabatically, how do the occupation numbers of the GGE redistribute?" This is not production of new pairs — it's the adiabatic redistribution of existing spectral weight across modes. The spectral index comes from the tau-dependence of the BdG spectrum, not from the pair creation amplitude.

### What to Read First

1. `sessions/session-47/session-47-ns-reassessment.md` — your own reassessment (just written)
2. `tier0-computation/s47_rhos_tensor.npz` — ρ_s at 16 tau values (the spectrum DOES change with tau)
3. `tier0-computation/s46_qtheory_selfconsistent.npz` — gaps Δ(τ) and eigenvalues λ²(τ) at 60 tau values
4. `tier0-computation/s44_dos_tau.npz` — full 992-mode spectrum at 5 tau values
5. Your papers:
   - **Paper 09** (`researchers/Volovik/09_1998_Volovik_Axial_Anomaly_3He_A_Baryogenesis.md`): spectral flow + chiral anomaly in 3He-A
   - **Paper 04** (`researchers/Volovik/04_2008_Volovik_Emergent_Physics_Fermi_Point_Scenario.md`): N₃ invariant, Fermi point topology
   - **Paper 28** (`researchers/Volovik/28_2009_Volovik_3He_B_Topological_Order_BDI_Classification.md`): BDI class, N₃=0
   - **Paper 24** (`researchers/Volovik/24_2016_Volovik_Zhang_Type_II_Weyl_Lifshitz_Transition.md`): Lifshitz transitions, Van Hove at transition
   - **Paper 06** (`researchers/Volovik/06_2012_Volovik_Topology_Quantum_Vacuum.md`): AZ classification, bulk-boundary
   - **Paper 27** (`researchers/Volovik/27_2013_Volovik_Superfluids_Non_Equilibrium_Quantum_Vacua.md`): non-equilibrium vacuum, quench
   - **Paper 15** (`researchers/Volovik/15_2008_Klinkhamer_Volovik_Self_Tuning_Vacuum.md`): q-theory

### Computation Steps

1. **Compute the BdG spectral flow.** At each of the available tau values, compute the full BdG quasiparticle spectrum E_k(τ) = sqrt(λ_k(τ)² + Δ_sector(k)(τ)²) for all 992 modes. Use eigenvalues from s44_dos_tau (5 tau) interpolated to the 60-point grid from s46_qtheory_selfconsistent. Plot E_k(τ) vs τ for representative modes from each sector.

2. **Identify spectral flow rates.** For each mode k, compute dE_k/dτ. This is the spectral velocity — how fast the quasiparticle energy changes during transit. Decompose:
   - dE_k/dτ = (ξ_k/E_k)(dλ_k/dτ) + (Δ_k/E_k)(dΔ_k/dτ)
   - The first term is the GEOMETRIC contribution (eigenvalue drift)
   - The second term is the BCS contribution (gap evolution)
   Which dominates? Is it k-dependent?

3. **Compute the spectral flow index.** If dE_k/dτ ~ E_k^α for some power α, then the spectral flow has a scale dependence. For adiabatic evolution, the occupation numbers of the GGE evolve as n_k(τ) ∝ (dE_k/dτ)^{-1} (slower flow = higher occupation, by the adiabatic theorem). The spectral index of the occupation spectrum would be:

   n_s - 1 = d ln(n_k) / d ln(k) ≈ -α × d ln(E_k) / d ln(k)

   Compute α from the data. Does it give n_s ≈ 0.965?

4. **The BDI spectral flow theorem.** In the Fermi-point case (Paper 09), spectral flow is quantized by N₃. In BDI (N₃=0), there's no topological quantization of spectral flow — but that doesn't mean there's NO spectral flow. It means the flow isn't topologically protected. Compute the TOTAL spectral flow:

   N_flow = Σ_k sign(dE_k/dτ) across the transit from τ=0 to τ=0.19

   In BDI, this should integrate to zero (no net level crossing). But the DISTRIBUTION of flow rates across k-values can still carry spectral information.

5. **Connect to Paper 24 (Lifshitz transitions).** The fold at τ=0.19 was identified as having Lifshitz-like features (S22-24: Pomeranchuk instability). At a Lifshitz transition, the Van Hove singularity produces a divergent density of states. If the spectral flow RATE diverges at the fold's Van Hove point, this could imprint a specific feature on the perturbation spectrum. Check: does dE_k/dτ have a singularity or near-singularity at the Van Hove eigenvalues?

6. **The occupation spectrum.** Using the spectral flow rates from step 2, compute the predicted GGE occupation numbers n_k(τ_fold). Compare to the S38 sudden quench result (59.8 pairs, P_exc=1.000). The sudden quench is the OPPOSITE limit from adiabatic spectral flow — which gives a better match to the known GGE?

7. **Assess.** Does adiabatic spectral flow produce a k-dependent occupation with n_s ≈ 0.965? Or is the spectral flow too flat (giving n_s ≈ 1) or too steep (giving n_s << 0.9)?

### Pre-registered gate SPECTRAL-FLOW-NS-47
- **PASS**: Spectral flow index gives n_s in [0.93, 0.99] at the fold
- **INFO**: Spectral flow is k-dependent (α ≠ 0) but gives n_s outside [0.93, 0.99]
- **FAIL**: Spectral flow is k-independent (α ≈ 0, flat spectrum) or the mechanism is structurally inapplicable

### Output files
- Script: `tier0-computation/s47_spectral_flow_ns.py`
- Data: `tier0-computation/s47_spectral_flow_ns.npz`
- Plot: `tier0-computation/s47_spectral_flow_ns.png`

### Working paper section: W4-3

### Critical notes
- The S38 result P_exc = 1.000 (complete condensate destruction) argues for sudden quench, not adiabatic flow. But the REAL transit is neither perfectly sudden nor perfectly adiabatic — it's intermediate (the Kibble-Zurek regime). The spectral flow computation gives the adiabatic limit; the S38 computation gives the sudden limit. The actual n_s may be between these extremes.
- Paper 09's spectral flow formula involves the momentum-space topology of the texture. In BDI, the relevant topology is the Pfaffian invariant (sgn(Pf) = -1 at all tau, from S35). How does the Pfaffian enter the spectral flow? This is a theoretical question — if you can connect them, that's a structural result.
- The q-theory crossing at τ* = 0.209 is where the vacuum energy changes sign. The spectral flow should have distinctive behavior near this crossing — levels may pile up or separate. Check specifically what happens at τ ∈ [0.19, 0.22].
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
- Working directory: C:\sandbox\Ainulindale Exflation (space in path — quote in shell)
