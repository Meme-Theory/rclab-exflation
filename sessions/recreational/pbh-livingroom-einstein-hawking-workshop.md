# Workshop: Two PBHs Collide in the Living Room — Einstein × Hawking

**Date**: 2026-04-27
**Format**: 2-agent iterative workshop, 2 rounds, sequential
**Mode**: RECREATIONAL — off-project hypothetical. Standard GR + QFT-in-curved-spacetime physics. **Do NOT apply phonon-exflation substrate framing.** No `D_K`, no `tau_fold`, no Jensen deformation, no GGE relics. This is a fun physics question, not a framework derivation.
**Agents**:
- A: einstein-theorist (GR / causal structure / equivalence principle)
- B: hawking-theorist (Hawking radiation / evaporation / quantum aspects)

## The Question

Two primordial black holes (PBHs) collide through pure happenstance in the user's living room. What are the consequences?

Required topics — both agents address all six, framed through their respective expertise:

| Tag | Topic |
|:----|:------|
| T1 (a) | Plausible PBH mass range. Canonical case: asteroid-mass (~10^17 g) PBHs — the unconstrained dark matter window. Discuss mass dependence. |
| T2 (b) | Tidal effects and gravitational reach BEFORE collision. Roche radius, atmospheric/structural disruption on approach, terminal trajectory through matter. |
| T3 (c) | Collision dynamics. Orbital decay timescale, GW emission, ringdown. |
| T4 (d) | Hawking radiation luminosity at this mass scale. Does the merger product evaporate explosively or persist? |
| T5 (e) | Quantitative consequences: living room → house → neighborhood → planet. Energy budgets compared to Tsar Bomba (~2.4×10^17 J), Chicxulub impactor (~4×10^23 J), etc. |
| T6 (f) | Earth's survival of the approach phase given a sub-lunar-mass object on a collision trajectory. Orbital mechanics + tidal forcing on the ground. |

## Tone and Rigor

Recreational, but rigorous — quantitative wherever possible. Order-of-magnitude estimates with stated assumptions. Have fun with it. Both agents are encouraged to disagree productively where their domains see the problem differently (Einstein's bias: geodesic motion + tidal geometry. Hawking's bias: thermal emission + horizon thermodynamics).

---

## Round 1 — Einstein (Opening Analysis)

### E1. Mass Range and Schwarzschild Scale (T1)

**The unconstrained PBH-DM window.** Astrophysical constraints from MACHO/EROS/OGLE microlensing on the upper end and from femtolensing of gamma-ray bursts plus Hawking-evaporation gamma-ray background limits on the lower end carve out one stubbornly surviving band where PBHs could *still* constitute the entirety of the dark matter:

`M_PBH ∈ [~10^17 g, ~10^22 g]`  (asteroid-mass to small-moon-mass).

The lower edge sits where Hawking evaporation timescales become shorter than the Hubble time (a 5×10^14 g PBH evaporates *now*, so anything below that is gone); the upper edge is where microlensing surveys begin to constrain the abundance. The asteroid-mass canonical case M ≈ 10^17 g = 10^14 kg is the structurally interesting one — too light for microlensing to see, too heavy to have evaporated, too compact to interact electromagnetically. It is the *invisible* window.

**Schwarzschild radius for M = 10^14 kg.** Definition `r_s ≡ 2 G M / c^2`. Substitute G = 6.674×10⁻¹¹ m³ kg⁻¹ s⁻², c = 2.998×10⁸ m s⁻¹:

```
r_s = 2 · (6.674×10⁻¹¹) · (10^14) / (2.998×10⁸)²
    = 2 · 6.674×10⁻¹¹ · 10^14 / 8.988×10^16
    = 1.485×10⁻¹³ m
    = 1.485×10⁻¹¹ cm
    ≈ 148 fm.
```

For comparison: classical proton radius ≈ 0.84 fm; an atomic nucleus is ~10 fm; a neutral atom ~10⁵ fm. **The horizon is roughly 100× the size of an atomic nucleus and 10⁵× smaller than a single atom.** It is a *sub-atomic* gravitational singularity.

**Compactness.** The Planck length ℓ_P ≈ 1.616×10⁻³⁵ m. So r_s / ℓ_P ≈ 9.2×10²¹ — comfortably in the semiclassical regime where general relativity still applies and we are *not* yet in the quantum-gravity domain (a PBH would have to weigh roughly the Planck mass, ~22 μg, before r_s ~ ℓ_P; we are 22 orders of magnitude heavier than that). So GR is the right tool.

**Mass dependence.** Schwarzschild scaling is linear in M: r_s(10^17 g) = 0.15 nm, r_s(10^22 g) = 15 μm. Even at the *upper* edge of the window, the horizon is microscopic — smaller than a red blood cell. *No PBH in the dark-matter-allowed window has a horizon larger than a grain of dust.* This is the central asymmetry of PBHs vs astrophysical black holes: the gravitational reach extends out to ~r_s · √(c²/v²) by velocity focusing, but the *mechanical cross-section* — the hard disc that touches matter — is set by r_s itself, and is therefore microscopic.

The relevant question for the living-room scenario is therefore not "does the PBH crush the room" (it is too small to mechanically crush anything), but "what does its long-range gravitational and tidal field do to the surroundings?" That is E2.

### E2. Tidal Field on Approach — Roche Geometry and Structural Disruption (T2)

**The relevant geometry is geodesic deviation, not Roche.** The classical Roche formula `d_Roche ≈ R · (2 M_PBH / M_self)^(1/3)` describes a self-gravitating fluid being pulled apart by an external tidal field; for the case of a 10^17 g PBH disrupting a wooden chair, the chair's *self-gravity* is irrelevant — the chair holds itself together by chemical bonds, not by gravity. So Roche analysis is the wrong tool. The right tool is the **geodesic deviation equation**: two test bodies separated by a vector `ξ^μ` along a timelike geodesic accelerate apart according to

```
D²ξ^μ / dτ² = − R^μ_{ναβ} u^ν u^β ξ^α.
```

For a Schwarzschild source the radial component reduces to the Newtonian tidal acceleration

```
a_tidal(r, L) = 2 G M / r³ · L,    (Eq. 1)
```

where r is the distance from the PBH and L is the proper separation between two endpoints of the body being stretched. The transverse components are compressive at half this magnitude (the famous "spaghettification" pattern: stretched along radial, squeezed transverse).

**Substitution chain — human bone failure threshold.** Bone tensile failure stress σ_bone ≈ 1.3×10⁸ Pa. For a self-stretched body of density ρ ≈ 10³ kg m⁻³ and length L ≈ 1 m, the half-length-averaged stress satisfies

```
σ = ρ · a_tidal · L / 2.
```

Solving for the tidal acceleration that produces failure:

```
a_fail = 2 σ_bone / (ρ L) = 2 · 1.3×10⁸ / (10³ · 1) = 2.6×10⁵ m s⁻².
```

Set this equal to Eq. 1 with L = 1 m:

```
2 G M / r³ = 2.6×10⁵
r³ = 2 · 6.674×10⁻¹¹ · 10^14 / 2.6×10⁵
   = 5.13×10⁻²
r ≈ 0.372 m ≈ 37 cm.
```

**Direction**: tidal acceleration scales as r⁻³, so closer-than-37-cm produces super-failure stress; farther-than-37-cm gives sub-failure stress. **Inside ~37 cm of the trajectory the PBH liquefies a human; outside ~11 m a human feels less than 1 g of differential pull** (from the same chain with σ = ρ · g · L: r_1g = (2GM·L/g)^(1/3) ≈ 11 m). Between 37 cm and ~11 m the experience is uncomfortable but not fatal — the room next door survives.

**Substitution chain — structural elements.**

| Element | σ_fail (Pa) | ρ (kg m⁻³) | L (m) | a_fail (m s⁻²) | r_fail (m) |
|:---|---:|---:|---:|---:|---:|
| Drywall / plaster | ~3×10⁶ | ~700 | 2.4 | 3.6×10³ | ~2.3 |
| Wood framing (2×4) | ~3×10⁷ | 600 | 3 | 3.3×10⁴ | ~1.06 |
| Steel I-beam | ~4×10⁸ | 7800 | 5 | 2.05×10⁴ | ~1.48 |
| Concrete slab (tensile) | ~3×10⁶ | 2400 | 5 | 5.0×10² | ~3.97 |

The substitution `r_fail = (2 G M · L / a_fail)^(1/3)` was applied uniformly. Drywall fails out to ~2 m, wood beams within ~1 m, steel girders within ~1.5 m, concrete out to ~4 m. **The living room itself — drywall, wood framing, the floor slab — disintegrates in a roughly 4-m-radius cylinder along the trajectory.** Beyond that radius the building is mechanically intact; inside it, structural members snap under the tidal stress.

**Atmospheric scale-height response.** Substitute H = 8.4 km (atmospheric scale height) and g = 9.8 m s⁻² (local gravity supporting the column) into Eq. 1:

```
r_atm = (2 G M · H / g)^(1/3) = (2 · 6.674×10⁻¹¹ · 10^14 · 8.4×10³ / 9.8)^(1/3) ≈ 225 m.
```

Within ~225 m of the trajectory the tidal field measured *over* a scale height equals or exceeds local gravity, which means the hydrostatic balance of the air column is briefly disrupted: the PBH tugs a column of air radially. But because the PBH is moving fast (~10s of km/s), this disruption is impulsive — the local pressure recovers in ~milliseconds. **The atmosphere is bruised, not unbound.**

**Roche / capture geometry.** A PBH is a point source, so the Roche analog for absorbing solid matter is the *gravitational capture* radius for hyperbolic encounter, not the fluid Roche radius. For a hyperbolic encounter with relative velocity v, the maximum impact parameter for direct geodesic capture (b such that the orbit dips inside the horizon on first approach) is

```
b_max ≈ r_s · √(c² / v²)    (low-velocity / Newtonian-focusing limit).
```

Substitute r_s = 1.485×10⁻¹³ m, c/v ≈ 10⁴ for v ≈ 30 km s⁻¹:

```
b_max ≈ 1.485×10⁻¹³ · 10⁴ = 1.485×10⁻⁹ m ≈ 1.5 nm.
```

For atomic absorption the equivalent figure is the **Bondi radius** `r_B = 2 G M / v²`. Substituting:

```
r_B = 2 · 6.674×10⁻¹¹ · 2·10^14 / (3×10⁴)² ≈ 3×10⁻⁵ m = 30 μm.
```

**Direction**: the Bondi sphere is roughly 30 micrometres across — much smaller than a hair, much larger than r_s. Air molecules wandering inside this sphere are gravitationally bound to the PBH; air molecules outside are not. The PBH therefore drags a small wake of bound atmosphere with it, but the wake mass is negligible (Bondi accretion rate at air density and v ≈ 30 km/s is `Ṁ ≈ 4π r_B² · ρ_air · v ≈ 10⁻¹⁵ kg/s`, eight orders of magnitude smaller than the PBH mass over any human timescale).

**Capture cross-section is therefore the dominant interaction radius, but it is set by tidal coupling, not by horizon contact.** The horizon itself almost never touches an atomic nucleus — Bondi-accretion mediated capture handles the energy/momentum exchange.

The picture: the PBH's *mechanical* footprint is sub-atomic, but its *tidal* footprint disrupts structural materials within a few meters and bruises air within a few hundred meters. This is the asymmetry between gravitational reach and material contact that defines the entire scenario.

### E3. Inspiral and Merger Dynamics (T3)

**The Peters formula is the right tool, and it is brutal for asteroid-mass PBHs.** For two point masses m₁, m₂ in a circular bound orbit at separation a, the leading-order quadrupole gravitational-wave luminosity drains orbital energy at the Peters rate

```
da/dt = − (64/5) · G³ · m₁ · m₂ · (m₁ + m₂) / (c⁵ · a³),    (Eq. 2)
```

with coalescence time obtained by integrating Eq. 2 from a₀ to 0:

```
τ_GW(a₀) = (5/256) · c⁵ · a₀⁴ / (G³ · m₁ · m₂ · (m₁ + m₂)).    (Eq. 3)
```

For equal masses m₁ = m₂ = m, the denominator factors `m·m·(2m) = 2 m³`, so

```
τ_GW(a₀) = (5/512) · c⁵ · a₀⁴ / (G³ · m³).    (Eq. 3′)
```

**Substitution chain — meter-scale capture orbit.** Take a₀ = 1 m (a "they meet at arm's length and start orbiting" geometry) and m = 10^14 kg:

```
τ_GW = (5/512) · (2.998×10⁸)⁵ · (1)⁴ / (6.674×10⁻¹¹)³ / (10^14)³
     = (5/512) · 2.42×10⁴² / 2.97×10⁻³¹ / 10^42
     = 7.95×10²⁸ s
     ≈ 2.5×10²¹ years.
```

**Direction**: τ_GW ∝ a₀⁴ / m³, so for fixed mass τ_GW grows steeply with separation; at a₀ = 1 m it is ~10¹¹ times the age of the universe. **The two PBHs at meter-scale separation do not merge by gravitational radiation. Ever, in any cosmologically meaningful sense.**

**Substitution chain — what separation merges within Hubble time?** Set τ_GW = t_universe ≈ 4.35×10¹⁷ s and solve for a₀ in Eq. 3′:

```
a₀⁴ = (512/5) · G³ · m³ · t_universe / c⁵
    = 102.4 · (6.674×10⁻¹¹)³ · (10^14)³ · 4.35×10¹⁷ / (2.998×10⁸)⁵
    = 102.4 · 2.97×10⁻³¹ · 10^42 · 4.35×10¹⁷ / 2.42×10⁴²
    ≈ 5.47×10⁻¹² m⁴
a₀ ≈ 1.53×10⁻³ m ≈ 1.5 mm.
```

**Direction**: only orbits whose initial separation is below ~1.5 mm will merge by GW emission within the age of the universe. Two PBHs that "happen to meet" at room scale (meters apart) will orbit each other for ~10²¹ years. **They are practically a permanent binary at the living-room scale.**

**Substitution chain — innermost stable circular orbit (ISCO).** For Schwarzschild, the ISCO sits at `r_ISCO = 6 G M_total / c²` where M_total = m₁ + m₂ = 2m for equal masses. Substitute:

```
r_ISCO = 6 · 6.674×10⁻¹¹ · 2·10^14 / (2.998×10⁸)²
       ≈ 4.45×10⁻¹³ m.
```

This is the radius at which the orbital approximation breaks down and the system plunges. From Eq. 3′ at a₀ = r_ISCO:

```
τ_GW(r_ISCO) ≈ 3.1×10⁻²¹ s,
```

so once the system is at ISCO, plunge happens in attoseconds — but getting *to* ISCO from any reasonable astrophysical separation is the limiting step. The physics of the *plunge* and *ringdown* itself is fast and follows the Kerr geometry; I defer the post-ISCO numerical-relativity details to the standard equal-mass non-spinning waveform calibration (final-state spin a/M ≈ 0.69, ringdown quasinormal mode ω_QNM at the dominant l=m=2 mode).

**Gravitational-wave frequency at merger.** The GW frequency at peak strain is approximately the inverse light-crossing time of the final horizon:

```
f_GW,merger ≈ c³ / (2π · G · M_total) ≈ c / (2π · r_s,final)
           ≈ 2.998×10⁸ / (2π · 2.82×10⁻¹³)
           ≈ 1.7×10²⁰ Hz.
```

A *gamma-ray-frequency* gravitational wave. **Direction**: this is ~17 orders of magnitude above the LIGO band (10–10⁴ Hz), ~14 orders above LISA (mHz), ~16 orders above pulsar-timing arrays (nHz). **No gravitational-wave detector that exists, or has been proposed, can see this merger.** The only way to detect a 10^14 kg PBH merger is through accreted-matter electromagnetic signatures — which Hawking will discuss.

**Energy radiated in GWs.** Equal-mass non-spinning calibration: ε_GW ≈ 5% of total rest energy, all radiated in the last ~few cycles before merger. So `E_GW ≈ 0.05 · 2 m c² = 0.1 m c² ≈ 9×10²⁹ J`. But this is delivered as a coherent GW pulse at f ≈ 10²⁰ Hz of duration `τ_ringdown ~ r_s/c ~ 5×10⁻²² s`. The *power* is therefore enormous (~10⁵¹ W for the duration of the ringdown — formally ~10²⁵ × the total electromagnetic luminosity of the observable universe), but the *coupled energy* into anything macroscopic is essentially zero, because nothing in the room couples to a 10²⁰-Hz tensor mode. The wave passes through the walls as if they were transparent.

**Bottom line for E3.** If the two PBHs share a bound orbit at room scale, they will orbit each other for ~10²¹ years before merging. If their initial encounter is hyperbolic (which is the much more likely "happenstance collision" geometry — they are not gravitationally bound a priori), they will scatter and fly apart, never to meet again, unless dynamical friction with the environment dissipates enough energy to bind them. *That* dissipation channel — gas drag, atmospheric friction, accretion drag — is small at 10^14 kg (Bondi rate ~10⁻¹⁵ kg/s), so binding is unlikely. **Most likely outcome of "two PBHs meeting in a living room": one fast scattering event, then they leave on hyperbolic trajectories.**

### E4. GR Perspective on the Final Object — Horizon, Mass, Spin (T4 — GR side)

**Conditional on merger actually happening** (which E3 says is essentially impossible at room scale, but if it does), the final object is a Kerr black hole. Numerical-relativity calibration (Buonanno-Cook-Pretorius, the original "Lazarus" / NINJA waveforms, plus the entire SXS catalog) for an equal-mass non-spinning binary gives the canonical merger remnant:

- Energy radiated as GWs: ε_GW ≈ (4.8 ± 0.5)% of total rest energy.
- Final dimensionless spin: χ_f ≡ a_K c / (G M_f) ≈ 0.685 ± 0.01.
- Linear-momentum recoil ("kick"): zero by symmetry for equal masses with no spin.

**Substitution chain — final mass.** Energy conservation across the merger:

```
M_f c² = (m₁ + m₂) c² − E_GW
       = 2 m c² · (1 − ε_GW)
       = 2 m c² · 0.952.
```

Therefore `M_f = 1.904 m`. For m = 10^14 kg:

```
M_f = 1.9×10^14 kg.
```

The "missing" mass — about 5% of the original total — has been converted to gravitational radiation (E3 above; E_GW ≈ 9×10²⁹ J at f ≈ 10²⁰ Hz).

**Substitution chain — final horizon radius.** For a Kerr black hole of mass M_f and dimensionless spin χ_f, the outer horizon sits at

```
r₊ = (G M_f / c²) · [1 + √(1 − χ_f²)],    (Eq. 4)
```

i.e. the Schwarzschild value `r_g ≡ GM/c²` plunges to a smaller r₊ as spin increases. Substituting M_f = 1.9×10^14 kg, χ_f = 0.685:

```
r_g = 6.674×10⁻¹¹ · 1.9×10^14 / (2.998×10⁸)² = 1.41×10⁻¹³ m
r₊ = 1.41×10⁻¹³ · [1 + √(1 − 0.469)] = 1.41×10⁻¹³ · [1 + 0.728] = 2.43×10⁻¹³ m.
```

**Direction**: r₊ < 2 r_g (the Schwarzschild value of an equally-massive non-spinning hole) by factor (1 + √(1−χ²))/2 ≈ 0.864. **The final horizon is *smaller* than what a non-spinning final hole would have**: the rotation pulls the horizon inward toward r_g. The Schwarzschild-equivalent comparison (`r_s = 2 G M_f / c²` if it were non-rotating) is 2.82×10⁻¹³ m; the actual Kerr r₊ is 2.43×10⁻¹³ m, about 86% of that.

In absolute terms: the merger remnant has a horizon ~243 fm across — about 1.6× the radius of one of the progenitors, but smaller than what naive mass-doubling would give (which would be 2.97×10⁻¹³ m for two non-rotating Schwarzschild holes adding to a non-rotating one of double mass). The deficit comes from two channels: (i) ~5% mass radiated to GWs shrinks the radius, (ii) the spin pulls the outer horizon inward.

**Substitution chain — area-theorem sanity check.** Hawking's area theorem demands `A_f ≥ A_i,total`. Compute both.

Initial area (two non-rotating progenitors):
```
A_i = 2 · 4π r_s² = 2 · 4π · (1.485×10⁻¹³)² ≈ 5.54×10⁻²⁵ m².
```

Final area (Kerr):
```
A_f = 4π (r₊² + a_K²)    where  a_K = χ_f · G M_f / c² = 0.685 · 1.41×10⁻¹³ = 9.66×10⁻¹⁴ m
    = 4π · [(2.43×10⁻¹³)² + (9.66×10⁻¹⁴)²]
    = 4π · [5.91×10⁻²⁶ + 9.32×10⁻²⁷]
    ≈ 8.62×10⁻²⁵ m².
```

**Direction**: A_f / A_i ≈ 1.56. The area grew by 56% during the merger — consistent with the area theorem and with the standard NR calibration (typical equal-mass non-spinning merger A_f / A_i ≈ 1.5–1.6). The mass-energy balance and the area theorem are both satisfied.

**Irreducible mass.** Defined by `A = 16π (G M_irr / c²)²`, the irreducible mass is

```
M_irr = √(A_f / 16π) · c² / G ≈ 1.76×10^14 kg ≈ 0.928 · M_f.
```

The remaining `M_f − M_irr ≈ 1.4×10^13 kg` of mass-energy is stored as rotational energy of the Kerr horizon and is, in principle, extractable (Penrose process, Blandford-Znajek). For a 10^14 kg PBH this is a ~10⁻⁷-of-solar-mass rotational reservoir — non-vanishing but utterly inaccessible to any human-scale process.

**Compactness, in plain terms.** All of the post-merger mass — 1.9×10^14 kg, comparable to a small mountain or a medium asteroid — is contained inside a horizon ~243 fm across. The mean density inside r₊ is

```
ρ_BH = M_f / (4π r₊³ / 3) = 1.9×10^14 / (4π · (2.43×10⁻¹³)³ / 3) ≈ 3.2×10⁵² kg/m³,
```

which is ~30 orders of magnitude above nuclear-matter density — but as is well known, this is a coordinate density, not a physical proper density at any spacelike slice; the actual "interior" is a curvature singularity at r=0 in the Kerr-coordinate ring. For this workshop the only thing that matters is the *exterior* observable: a 243-fm rotating horizon emitting Hawking flux at a temperature Hawking will compute next.

**What about ringdown emission?** The dominant quasinormal mode for χ_f ≈ 0.685 is the ℓ=m=2 mode at

```
ω_QNM · (G M_f / c³) ≈ 0.532 − 0.0807 i    (standard Kerr QNM tabulation).
```

Substituting `G M_f / c³ ≈ 4.7×10⁻²² s` gives the ringdown frequency f_QNM ≈ 1.8×10²⁰ Hz with damping time τ_damp ≈ 5.8×10⁻²¹ s. Same order of magnitude as the inspiral peak — both inhabit the gamma-ray band, both are completely undetectable.

**Final-state summary.**
- Mass: 1.9×10^14 kg (95% of progenitor total).
- Horizon: r₊ ≈ 243 fm = 2.43×10⁻¹³ m.
- Dimensionless spin: χ_f ≈ 0.685.
- Rotational energy reservoir: ~7% of M_f c² ≈ 6×10²⁹ J.

This is the GR side. The *thermal* side — temperature, luminosity, evaporation timescale — is Hawking's domain.

### E5. Energy Budgets and Comparative Cataclysm Scale (T5)

**The headline number is mc². It is also a red herring.** The rest energy of one M = 10^14 kg PBH is

```
E_rest = m c² = 10^14 · (2.998×10⁸)² = 8.99×10³⁰ J.    (Eq. 5)
```

**Comparison ladder** (all ratios are E_rest divided by the listed cataclysm):

| Cataclysm | Energy (J) | E_rest / cataclysm |
|:---|---:|---:|
| Hiroshima (Little Boy) | 6.3×10¹³ | 1.4×10¹⁷ |
| Tunguska impact (1908) | 5×10¹⁶ | 1.8×10¹⁴ |
| Tsar Bomba (50 Mt) | 2.4×10¹⁷ | 3.7×10¹³ |
| Krakatoa eruption | 8.4×10¹⁷ | 1.1×10¹³ |
| Chicxulub impactor | 4×10²³ | 2.2×10⁷ |
| Sun's energy on Earth, 1 year | 5.5×10²⁴ | 1.6×10⁶ |
| Sun's total luminosity, 1 second | 3.83×10²⁶ | 2.3×10⁴ |
| **Earth gravitational binding** | **2.24×10³²** | **0.04** |
| Sun gravitational binding | 6.87×10⁴¹ | 1.3×10⁻¹¹ |

**Direction**: a single 10^14 kg PBH carries enough rest energy that ~22 of them, fully converted to mechanical energy, would gravitationally unbind the Earth (substitution: 1/0.04 = 22.4). Two of them carry 1.8×10³¹ J ≈ 8% of Earth's binding energy. *If* all of mc² were liberated, this would be a planet-killing event.

**But mc² is NOT what gets liberated.** This is the central GR fact of the energy-budget question. The rest mass of a black hole sits *inside the horizon*; it cannot be emitted, scattered, or radiated by any classical process. The only channels through which mass-energy *exits* the merger system are:

1. **Gravitational waves**, ε_GW ≈ 5% of (m₁+m₂)c² for an equal-mass non-spinning merger:
   `E_GW = 0.05 · 2 m c² = 9×10²⁹ J` ≈ 4×10¹² Tsar Bombas. Released as a coherent pulse at f ≈ 10²⁰ Hz over ~10⁻²¹ s. Couples to nothing macroscopic. Effectively zero mechanical impact on the room.

2. **Hawking radiation**, integrated over the BH lifetime. Rate and timescale are Hawking's domain; deferring.

3. **Kinetic energy of the PBHs themselves**. This is *the* thing that interacts with the room. For relative velocity v at the encounter:
   ```
   KE = ½ m v².    (Eq. 6)
   ```

**Substitution chain — KE liberated at typical encounter velocities.**

| Encounter v (m/s) | Context | KE (J) | KE / Tsar Bomba | KE / Chicxulub | KE / E_rest |
|---:|:---|---:|---:|---:|---:|
| 3×10³ | trans-orbital crawl | 4.5×10²⁰ | 1.9×10³ | 1.1×10⁻³ | 5×10⁻¹¹ |
| 1×10⁴ | sub-orbital | 5×10²¹ | 2.1×10⁴ | 1.3×10⁻² | 6×10⁻¹⁰ |
| 3×10⁴ | Earth orbital | 4.5×10²² | 1.9×10⁵ | 1.1×10⁻¹ | 5×10⁻⁹ |
| 1×10⁵ | encounter velocity in inner solar system | 5×10²³ | 2.1×10⁶ | 1.3 | 6×10⁻⁸ |
| 2.2×10⁵ | galactic halo virial | 2.4×10²⁴ | 1.0×10⁷ | 6.0 | 3×10⁻⁷ |
| 3×10⁵ | hyperbolic | 4.5×10²⁴ | 1.9×10⁷ | 11 | 5×10⁻⁷ |

**Direction**: at the most likely encounter velocity for halo dark matter (v ≈ 220 km/s), KE / E_rest ≈ 3×10⁻⁷ — only 0.3 parts per million of the rest energy is mechanically available. **At the canonical PBH-DM encounter velocity, the available energy is ~6 Chicxulub events. At Earth-orbital velocity (30 km/s), it is ~0.11 Chicxulub or ~190,000 Tsar Bombas — but again, only the fraction that couples to the surrounding matter actually deposits.**

**Substitution chain — coupling efficiency to the room.** Because the PBH is a sub-atomic point source with Bondi radius ~30 μm (E2), almost none of the kinetic energy couples mechanically to the room on the way through. Bondi accretion at room density (ρ_air ~ 1.2 kg m⁻³) and v = 30 km/s gives mass accretion rate

```
Ṁ_Bondi = 4π · r_B² · ρ · v ≈ 4π · (3×10⁻⁵)² · 1.2 · 3×10⁴ ≈ 4×10⁻⁷ kg/s.
```

The dynamical-friction drag force is `F_DF ~ Ṁ_Bondi · v ≈ 4×10⁻⁷ · 3×10⁴ ≈ 1.2×10⁻² N`. Acting on a 10^14 kg body, that is `a_DF = F/M ≈ 10⁻¹⁶ m/s²` — utterly negligible. The PBH is *not stopped by air, nor by water, nor by rock*. It crosses Earth's diameter (2 R_⊕ = 1.27×10⁷ m) at v = 30 km/s in 7 minutes, depositing essentially none of its kinetic energy en route. The Bondi-Hoyle accretion is a finer question for Hawking, but the bulk-mechanics conclusion is firm: **the PBH passes through Earth like a neutrino, carrying its KE with it.**

**The energy actually deposited in the room.** Bound by the gravitational tidal *work* done as the PBH moves through. Tidal work on a body of mass μ at perpendicular distance b moving past the PBH at velocity v:

```
ΔE_tide ≈ (G M m_target / b)² · 1/(μ v²) ≈ (G m / b² · L)² · μ / v²    (impulse approx, gravitational drag)
```

For a μ = 50 kg human at b = 1 m and v = 30 km/s, the impulsive velocity kick is

```
Δv ~ G m / (b · v) = 6.674×10⁻¹¹ · 10^14 / (1 · 3×10⁴) ≈ 2.2×10⁻¹ m/s.
```

That is a 22-cm/s sideways shove. **Not lethal at 1 m. Inside ~37 cm the tidal stretch breaks bones (E2). Inside ~10 cm the impulsive Δv exceeds 2 m/s and you are flung across the room.** Most of the PBH's KE is *not* deposited; the room mostly experiences a gravitational impulse, not an energy dump.

**Bottom line for E5.**
- E_rest is enormous — ~22 PBHs at 10^14 kg would unbind Earth if it could be liberated.
- It cannot be liberated by classical means: rest mass stays behind the horizon.
- Liberatable energies: GW pulse (~10³⁰ J, undetectable) and KE (~10²² J at solar-system velocities, ~10²⁴ J at halo velocities).
- Of that, *coupled* energy to surrounding matter is many orders smaller, dominated by gravitational tidal impulse at close passage and Bondi accretion drag (negligible).
- The room sees a violent local gravitational impulse, not a thermonuclear-scale energy dump.

The cataclysm is *kinetic + tidal*, not *rest-energy-converted*. This is the core GR insight.

### E6. Approach Geodesics and Earth's Fate (T6)

**The PBH does not collide with Earth in any mechanical sense — it traverses Earth on a geodesic.** The horizon is sub-atomic (148 fm); bulk matter has interatomic spacing of order 10⁻¹⁰ m = 10⁵ × r_s. The PBH is to bulk matter what a billiard ball is to a galaxy: it passes between the constituents almost without touching anything.

**Substitution chain — geodesic motion of the PBH through Earth.** In the weak-field rest frame of Earth, the PBH satisfies the Newtonian limit of the geodesic equation:

```
d²x_PBH / dt² = − ∇Φ_Earth(x) + small GR corrections of order GM_⊕/(c² R_⊕) ~ 7×10⁻¹⁰.
```

The trajectory is determined by Earth's gravitational potential plus negligible PN corrections. The PBH falls in radially (or on a chord, depending on impact angle). Crossing time at v ≈ 30 km/s through a chord of length 2 R_⊕ = 1.27×10⁷ m:

```
τ_cross = 2 R_⊕ / v = 1.27×10⁷ / 3×10⁴ ≈ 425 s ≈ 7 minutes.
```

During those 7 minutes the PBH passes through atmosphere, ocean, crust, mantle, outer core, inner core, and out the antipode. It is gravitationally accelerated and decelerated by Earth's potential as it does so (gaining ~11 km/s of speed at the centre), but its *direction* is essentially a straight line set by the impact parameter; the PBH is too light for Earth to deflect it appreciably from a straight chord.

**Substitution chain — tidal acceleration on Earth's surface during approach.** Eq. 1: `a_tidal = 2 G M / r³ · L`. Substitute M = 10^14 kg, L = 1 m (a person's height) for various distances of closest approach:

| Closest approach r | a_tidal on 1-m body | In units of g |
|---:|---:|---:|
| 10⁶ m (1000 km) | 1.34×10⁻¹⁴ m/s² | 1.4×10⁻¹⁵ g |
| 10⁵ m (100 km) | 1.34×10⁻¹¹ m/s² | 1.4×10⁻¹² g |
| 10⁴ m (10 km) | 1.34×10⁻⁸ m/s² | 1.4×10⁻⁹ g |
| 10³ m (1 km) | 1.34×10⁻⁵ m/s² | 1.4×10⁻⁶ g |
| 10² m (100 m) | 1.34×10⁻² m/s² | 1.4×10⁻³ g |
| 50 m | 1.07×10⁻¹ m/s² | 1.1×10⁻² g |
| 25 m | 8.5×10⁻¹ m/s² | 8.7×10⁻² g |
| 10 m | 13.4 m/s² | 1.4 g |
| 5 m | 1.07×10² m/s² | 11 g |
| 2 m | 1.67×10³ m/s² | 170 g |
| 1 m | 1.34×10⁴ m/s² | 1400 g |

**Direction**: tidal acceleration scales as r⁻³, so it is utterly imperceptible at 1 km, perceptible (~10⁻³ g) at 100 m, equal to surface gravity at ~11 m, lethal (170 g) at ~2 m, room-disrupting at ~1 m, bone-shattering at ~37 cm. **At any distance > ~30 m the PBH is mechanically undetectable; at < ~10 m it is unambiguously hostile.** A passage 1 km below your feet would feel like a faint tug lasting for a fraction of a second; a passage 5 m away would knock buildings down.

**Substitution chain — the depositional energy budget along the trajectory.** As the PBH passes through Earth on a chord, what does it actually break?

Inside the cylinder of radius r_disrupt ≈ 37 cm (bone/rock failure threshold from E2) along the trajectory, the rock is tidally shattered. Volume of disrupted column:

```
V_disrupt = π r² · (2 R_⊕) = π · (0.37)² · 1.27×10⁷ ≈ 5.5×10⁶ m³.
```

Mass of disrupted rock at ρ ≈ 3000 kg/m³:

```
M_disrupt ≈ 1.6×10¹⁰ kg ≈ 16 gigatonnes.
```

Energy required to fragment this rock (specific fragmentation energy ~10⁶ J/kg):

```
E_frag ≈ M_disrupt · 10⁶ ≈ 1.6×10¹⁶ J ≈ 0.07 · Tsar Bomba.
```

**Direction**: this is a *tiny* fraction of the PBH's kinetic energy (KE ≈ 4.5×10²² J), specifically `E_frag / KE ≈ 4×10⁻⁷`. **The PBH does not slow appreciably as it crosses Earth — only a few parts in 10⁷ of its KE is dissipated as rock fragmentation along the trajectory.** It exits the antipode at essentially the same speed it entered, having punched a 74-cm-diameter, 12,700-km-long cylinder of pulverized material through the planet.

**This drilled cylinder is the dominant cataclysm.** Consequences:
- The cylinder of pulverized rock undergoes immediate adiabatic relaxation as it is no longer self-supported. Pressure waves propagate outward.
- Magma in the deep mantle and core reorganizes around the (now-evacuated, highly-fractured) channel.
- The exit point experiences a sudden ejection of overpressurized material — a kilometres-scale crater on the far side of the world from the entry point.
- A seismic transient at acoustic frequencies (Rayleigh waves, body waves) propagates globally with energy ~10¹⁶ J — comparable to a magnitude-8 earthquake.

But the planet is **not** dynamically destroyed. Earth's gravitational binding energy is 2.24×10³² J; the deposited energy is 1.6×10¹⁶ J, sixteen orders of magnitude smaller. The geomechanical damage is severe but localized: an M ≈ 8 earthquake equivalent, plus two craters (entry + exit) each ~kilometre-scale, plus possibly some atmospheric column disturbance. The planet survives.

**The GW burst at merger** (E3): if merger somehow occurs, ε_GW ≈ 9×10²⁹ J at f ≈ 10²⁰ Hz. Cross-section for absorption of 10²⁰-Hz tensor radiation in normal matter is essentially zero (no atomic, nuclear, or electronic transition matches that frequency, and gravitons couple as ~G/c⁴). The wave passes through Earth without interaction. **GW deposition on Earth: zero (to 30 decimal places).**

**Tidal lift on Earth as a whole.** A naive estimate of the distance at which the PBH tidal field across Earth's diameter equals Earth's surface gravity:

```
2 G M / r³ · R_⊕ = g_⊕
r = (2 G M R_⊕ / g_⊕)^(1/3)
  = (2 · 6.674×10⁻¹¹ · 10^14 · 6.37×10⁶ / 9.8)^(1/3)
  ≈ 2055 m ≈ 2 km.
```

**Direction**: at distances < 2 km the *tidal lift* on Earth's surface integrated over the planet's lever arm exceeds g locally. At distances < 11 m the *local* tidal stretch on a 1-m body exceeds g. The first scale (~2 km) governs whether the PBH could *partially levitate* a continent; the second (~11 m) governs whether it kills you personally. Both are tiny compared to a planetary-radius scale. **Earth as a body remains gravitationally intact during the encounter** because M_PBH / M_⊕ = 10^14 / 6×10²⁴ = 1.7×10⁻¹¹ — Earth's own gravity overwhelms the PBH's everywhere except in a ~2-km cylinder around the trajectory.

**The accretion question is for Hawking.** During the 7-minute traversal, how much of the rock the PBH passes through is actually swallowed by the horizon (Bondi-Hoyle accretion)? My GR-side estimate from the Bondi formula is `Ṁ_Bondi ≈ 4π r_B² ρ v` with r_B = 2 G M / v_eff² ; in solid rock at v ≈ 3×10⁴ m/s the local sound speed dominates, c_s ≈ 5×10³ m/s, giving r_B ≈ G M / c_s² ≈ 3×10⁻⁹ m and Ṁ_Bondi ≈ 4π · (3×10⁻⁹)² · 3000 · 5×10³ ≈ 1.7×10⁻⁹ kg/s. Over 425 s of passage that is ~7×10⁻⁷ kg accreted — a microgram. **PBH grows by less than a microgram on its trip through Earth.** But the Bondi formula here is in a regime where Hawking emission, viscous heating, and back-reaction may be substantial; I defer the cleaner calculation to Hawking.

**Bottom line for E6.** Earth survives the approach mechanically — no gravitational disruption of the planet, no GW deposition, no thermal runaway. The damage is localized to a ~74-cm-wide pulverized cylinder along the trajectory plus seismic afterglow ≤ M8 equivalent. Death and destruction are confined to within ~10 m of the chord. **The planet bleeds; it does not die.**

### E7. Questions for Hawking

I have left five explicit deferrals to your domain. The questions, in order:

**Q1 (radiation rate at the canonical mass).** For a 10^14 kg Schwarzschild black hole, what is T_H exactly, and what is the integrated luminosity dM/dt in the standard greybody-corrected Page calculation? My GR analysis treats the PBH as a classical horizon emitting nothing; I want the *total* power and the *spectral* peak frequency. Specifically: at this mass, is the dominant emission channel photons, neutrinos, gravitons, or is there a non-trivial mixture once one accounts for the QCD-confinement cutoff at the horizon temperature?

**Q2 (evaporation timescale and whether the canonical PBH is "still alive").** Does τ_evap(M = 10^14 kg) exceed the age of the universe? If yes, by what factor — is this PBH essentially permanent on cosmological timescales, or is it within a few Hubble times of the runaway-evaporation cliff? I quoted "below ~5×10¹⁴ g it has already evaporated" as folklore; I want the actual T_evap(M) curve and where M = 10^14 kg sits on it.

**Q3 (does the merger product evaporate explosively?).** In E4 I gave the merger remnant: M_f = 1.9×10^14 kg, χ_f ≈ 0.685, r₊ ≈ 243 fm. Two questions about its endpoint:
   (a) Does the spin-down to Schwarzschild via Hawking emission happen *before* the mass-down to zero? I know rotating BHs preferentially radiate angular momentum first (Page); does that change the picture qualitatively for a 10^14 kg starting remnant?
   (b) Once the mass falls into the planck-scale regime, what is your best guess for the endpoint — full evaporation to thermal bath, planck-mass remnant, information-paradox-driven non-thermal final burst?

**Q4 (Bondi accretion vs Hawking emission balance during living-room transit).** During the ~7-minute Earth-crossing in E6, I estimated Bondi accretion at ~10⁻⁹ kg/s in rock and ~10⁻⁷ kg/s in air, and the PBH gains ~1 microgram of mass. Meanwhile your Hawking emission is *removing* mass at some rate. Which channel wins for M = 10^14 kg in (a) interstellar medium, (b) atmospheric density, (c) liquid water, (d) rock? Is there a "critical density" above which the PBH grows by accretion and below which it shrinks by emission? This determines whether a long-lived PBH passing through Earth would *gain* mass from the encounter or *lose* it.

**Q5 (fraction of mc² emerging as Hawking flux, integrated over the lifetime).** The 8.99×10³⁰ J of rest energy I quoted in E5 is locked behind the horizon classically. Quantum-mechanically, does *all* of it eventually emerge as Hawking radiation as the PBH evaporates, or does some non-zero fraction get lost to a remnant / firewall / non-unitary endpoint? The answer matters for the final-cataclysm bookkeeping: if 100% of mc² eventually emerges, the asymptotic energy budget is enormous (just spread over 10⁶⁴ years for M = 10^14 kg); if a remnant traps a finite fraction, the energy budget is correspondingly cut.

**Bonus Q6 (your gamma-ray sky question).** If 10^14 kg PBHs constitute 100% of dark matter, the local PBH number density is ~10⁻²⁰ m⁻³, and the *late-stage* evaporators (those nearing M ~ 10⁹ g where the spectrum peaks at TeV) would be detectable in gamma rays. The non-detection of such bursts in the Fermi-LAT / HAWC era constrains the abundance. Where exactly does my "asteroid-mass window is unconstrained" claim from E1 stop being true on the Hawking-driven cataclysm side? I.e. at what mass does the *terminal* gamma-ray burst from each evaporating member of the population start tightening the abundance bound?

These five (plus a half) questions cover the territory I deliberately left empty. The two of us together close T1-T6.

---

## Round 1 — Hawking (Response + Original Analysis)

### Part 1: Response to Einstein

#### Re: E1 — Mass Range

**AGREE.** The asteroid-mass window [10^17, 10^22] g is the right band. Your r_s = 148 fm at M = 10^14 kg matches my calculation to 4 sig figs (`r_s = 2 G M / c^2 = 1.485×10⁻¹³ m`). The semiclassical-regime check `r_s / ℓ_P ≈ 9.2×10²¹` is correct — we are 22 orders of magnitude above the quantum-gravity threshold, so the standard Bogoliubov-coefficient mode-mixing calculation applies without modification. Your "lower edge ≈ 5×10¹⁴ g evaporates now" is the canonical folklore number and it is essentially right.

**DISAGREE.** The lower edge is *not* 5×10¹⁴ g = 5×10¹¹ kg. The correct evaporation-cliff mass — defined by `τ_evap(M_*) = t_Hubble = 4.35×10¹⁷ s` — is

```
Definition:   τ_evap(M) = 5120 π G² M³ / (ℏ c⁴)
Set equal:    5120 π G² M_*³ / (ℏ c⁴) = 4.35×10¹⁷
Substitute:   M_*³ = 4.35×10¹⁷ · ℏ c⁴ / (5120 π G²)
Simplify:     M_* = 1.73×10¹¹ kg = 1.73×10¹⁴ g.
Direction:    M_* is ~3× SMALLER than your quoted 5×10¹⁴ g.
```

So the *exact* lower edge is closer to 1.7×10¹⁴ g, not 5×10¹⁴ g. The folklore number folds in a "factor-of-a-few" buffer to account for greybody corrections (the integrated Page-graybody factors slow evaporation by ~30%) plus the Standard-Model particle threshold cascade as T_H climbs above electron, muon, pion, … masses near the end. With those corrections rolled in, the "currently evaporating" population sits at roughly 5×10¹⁴ g. We are saying the same thing; I am just pinning the bare-emission fiducial.

**MISSED.** Your E1 treats the PBH as a *static* horizon for the purposes of constraint-mapping. Two thermal observations sharpen the window:

1. The *femtolensing* lower bound (~10¹⁶ g, from Barnacka-Glicenstein-Moderski 2012) and the *gamma-ray-background* lower bound (~10¹⁷ g for 100% f_DM, from the integrated Page-evaporation flux) overlap. Below ~10¹⁷ g, evaporating PBHs would already have produced a detectable diffuse gamma-ray background — they have not, so the unconstrained window's *true* lower edge is closer to 10¹⁷ g than to 5×10¹⁴ g.

2. The *upper* edge of "your" 10²² g cap is the OGLE/HSC microlensing constraint, but that has a soft shoulder due to wave-optics finite-size effects when r_s approaches the photon wavelength. For r_s = 15 μm at M = 10²² g and lensing wavelengths in the optical (~5×10⁻⁷ m), we have r_s ~ 30 λ — the geometric-optics regime is comfortably valid, so no wave-optics relief there.

**EMERGES.** The asteroid-mass window is *exactly* the band where (i) evaporation is too slow to be seen (τ ≫ t_Hubble), (ii) the horizon is too small to lens light (r_s ≪ μm in most of the window), and (iii) the Hawking flux is too dim to spot in space-based gamma surveys at solar-neighborhood densities. It is the constraint-map intersection of three independent thermal/optical observables — not just one. That is why it has been so stubborn.



#### Re: E2 — Tidal Field

**AGREE.** Your r⁻³ tidal-acceleration argument is exactly right and the numbers are clean: r_fail ≈ 37 cm for human bone, ~1 m for wood framing, ~4 m for concrete. The geodesic-deviation framing is correct — Roche analysis would be wrong because chemical bonds, not self-gravity, hold a chair together. The Bondi radius `r_B = 2GM/v² ≈ 30 μm` at v ≈ 30 km/s is also correct, and the implication — that mechanical contact with bulk matter is essentially absent — is fine for the *kinematic* footprint.

**DISAGREE.** Your statement "the PBH is a sub-atomic point source ... almost none of the kinetic energy couples mechanically to the room" is **right for the gravitational/mechanical channel and wrong for the radiation channel**. At M = 10^14 kg the PBH is a hard-gamma source. The Stefan-Boltzmann flux at distance r is

```
Definition:    F_Hawking(r) = P / (4π r²)
Substitute:    P = 3.563×10⁴ W (from H1 below), r = 1 m
Simplify:      F = 3.563×10⁴ / (4π · 1²) = 2.835×10³ W/m²
Direction:     F(1 m) > F_solar = 1361 W/m² by factor 2.08.
```

So at 1 m from the PBH the radiation flux exceeds the solar flux at Earth's surface by a factor of 2. And it is in 100-keV gamma rays, not visible light. The dose-rate estimate (using ~3×10⁵ photons/cm²/s at 100 keV ≈ 1 mSv/hr conversion) gives **~5.6×10¹¹ mSv/hr at 1 m** — instantly lethal at meter range from radiation alone, before the tidal field even matters.

**MISSED.** Three things your geodesic-only treatment leaves out:

1. **Radiation pressure on dust during approach.** Hawking photons impart momentum p = E/c. The radiation pressure at distance r is `P_rad = F_Hawking/c`. At 1 m: P_rad = 2.835×10³ / 3×10⁸ = 9.5×10⁻⁶ Pa — negligible mechanically. But each gamma deposits its full 100 keV in the first Compton-scattering target. **The PBH ionizes everything in line-of-sight to ~tens of meters.** Air ionization at this dose makes the volume conductive and self-luminous (recombination radiation in optical/UV), so a long-lived PBH at rest in your living room is a *visible bluish-violet glow* before you ever feel the tidal field.

2. **Hawking-vs-Bondi balance during the approach phase**, not just at horizon contact. Your 30-μm Bondi sphere is the gravitational-capture radius; my Hawking emission is *isotropic* outside that sphere. The two regimes operate at different scales (Bondi ≪ tidal-disruption ≪ thermal-significant) and the dominant interaction at meter scale is *thermal* (gamma flux), not mechanical (Bondi accretion). I derive the full accretion-emission balance in H2.

3. **Trans-Planckian-problem moot at this scale.** Standard objection — that high-frequency Hawking modes outside the horizon trace back to trans-Planckian frequencies near the horizon — is irrelevant here because r_s/ℓ_P ~ 10²² puts the relevant Bogoliubov-mode-mixing region 22 orders of magnitude above the Planck frequency. The radiation we're discussing is fully semiclassical.

**EMERGES.** The lethal-radius hierarchy at M = 10^14 kg is:

| Effect | Lethal radius | Mechanism |
|:---|:---:|:---|
| Tidal stretch (bone failure) | ~0.4 m | r⁻³ gravity |
| Radiation pressure (ionization) | ~10 m | r⁻² photons |
| Acute radiation dose (LD50 ~5 Sv in seconds) | **~30–100 m** | r⁻² gamma flux |
| Tidal acceleration ≥ g | ~11 m | r⁻³ gravity |

**The radiation kill-radius EXCEEDS the tidal kill-radius by ~30×.** At M = 10^14 kg you die of acute gamma exposure long before tidal forces can break you. Einstein's "37 cm bone-failure threshold" is the floor of a much taller hazard envelope set by Hawking emission. This inverts the picture: the PBH at this mass is a *radiological* hazard at meter-to-tens-of-meters scale, with the mechanical/tidal hazard a sub-component at sub-meter scale.



#### Re: E3 — Inspiral / Merger

**AGREE.** Your Peters-formula τ_GW(a₀ = 1 m, m = 10^14 kg) = 2.5×10²¹ yr is correct and devastating to the "they meet and merge" scenario. The a⁴/m³ scaling and the cross-check that *only* a₀ ≲ 1.5 mm initial separations merge within Hubble time is right. I confirm your ISCO at 4.45×10⁻¹³ m, plunge time at attoseconds, and merger GW frequency f ≈ 1.7×10²⁰ Hz. The undetectability claim — 17 OOM above LIGO — is correct and stings.

**DISAGREE.** A small but nonzero correction to the "no GW detector can see this" claim. Your formula `f_merger ≈ c³/(2π G M_total)` is the ringdown peak; the *inspiral* GW spectrum at any earlier separation a > r_ISCO is at frequency `f_GW = 2 f_orb = (1/π) √(G M_total / a³)`. For the meter-separation orbit:

```
Definition:    f_orb(a) = (1/(2π)) √(G M_total / a³)
Substitute:    M_total = 2×10¹⁴ kg, a = 1 m
Simplify:      f_orb = (1/(2π)) √(6.674×10⁻¹¹ · 2×10¹⁴ / 1)
              f_orb = (1/(2π)) · 1.155×10² rad s⁻¹ ≈ 18.4 Hz
              f_GW = 2 f_orb ≈ 36.8 Hz
Direction:     The meter-orbit's INSPIRAL gravitational waves sit at ~37 Hz —
              squarely in the LIGO band, not the gamma band.
```

So a 10^14-kg PBH binary orbiting at meter-scale would be a *LIGO-band* source — except the GW strain amplitude at any reasonable distance is `h ~ (G/c⁴) · (G M²/a) / D ~ 10⁻⁴⁴` for D = 10 pc. **Far below LIGO's strain sensitivity (10⁻²³).** So your conclusion holds — undetectable — but for the *amplitude* reason, not the *frequency* reason. The frequency only enters the gamma band right at merger, in the final attoseconds.

**MISSED.** Three quantum/thermal additions to the inspiral picture:

1. **Hawking-flux modulation by Doppler boost during the orbit.** Each PBH orbits at v_orb = (ω a)/2 ≈ 58 m/s at meter separation. The Hawking spectrum is Doppler-boosted by γ(1 ± β) ≈ 1 ± 1.9×10⁻⁷ — completely negligible. **No observable modulation of the gamma flux from the orbit.**

2. **Ringdown enhancement of Hawking flux.** During the ~10⁻²¹ s ringdown, does the surface gravity transient enhance pair production? The instantaneous κ rises from progenitor's value to χ_f-dependent merger-product value over a few light-crossing times. The natural Hawking energy emitted *during the ringdown* is `E_H,ringdown ~ P · τ_ringdown ~ 10⁴ W · 10⁻²¹ s ~ 10⁻¹⁷ J` — utterly dwarfed by the GW emission `E_GW ~ 9×10²⁹ J`. So GW dominates ringdown by 46 orders of magnitude. There is no observable thermal transient.

3. **Quantum diagnostic check.** r_s = 1.48×10⁻¹³ m, ℓ_P = 1.62×10⁻³⁵ m, electron Compton λ_C = 3.86×10⁻¹³ m. **r_s/λ_C ≈ 0.38** — *the horizon is smaller than an electron's Compton wavelength*. This is the only quantum scale that matters: an electron near the PBH cannot be localized inside the horizon (the localization energy ~ ℏc/r_s ~ 1.3 MeV exceeds m_e c² = 0.511 MeV). So the Hawking emission of e⁺e⁻ pairs (kT_H = 106 keV, below 2 m_e c² = 1.022 MeV) is suppressed — only photons, neutrinos, and gravitons emerge until the PBH gets hotter.

**EMERGES.** The merger event is "frozen" in two senses. (i) Classical: at meter separation it does not merge in any cosmologically meaningful timescale (your E3). (ii) Quantum: even if it did, the brief horizon transient does not enhance Hawking emission detectably. **The merger is a non-event from both perspectives.** What dominates instead is the steady-state Hawking flux from each PBH separately, plus the orbital tidal stress on whatever happens to be in the ~m radius of the orbit. For the question "what does the user experience" the answer is: two co-orbiting hard-gamma sources (each 36 kW, ~kT 106 keV peak) trapped in a permanent dance.



#### Re: E4 — Final Object

**AGREE.** Your final-state numbers — M_f = 1.9×10^14 kg, χ_f = 0.685, r₊ = 243 fm, A_f/A_i = 1.56, M_irr = 1.76×10^14 kg, rotational reservoir 6×10²⁹ J — match the standard SXS equal-mass non-spinning calibration. The area-theorem check ΔA > 0 is satisfied (your 56% area gain). The QNM ω_QNM·(GM_f/c³) ≈ 0.532 − 0.0807 i for χ_f = 0.685 is the canonical Leaver/Berti tabulation value.

**DISAGREE.** One thermodynamic correction to your final-state summary. You list T_H implicitly via the Schwarzschild formula. The correct Kerr temperature is

```
Definition:    T_Kerr = ℏ κ / (2π c k_B)
              κ = (c⁴/G) · √(M² − a²) / (2 M (M + √(M² − a²)))    (Kerr surface gravity)
Substitute:    M_f = 1.9×10^14 kg, χ_f = 0.685, so √(1−χ²) = 0.728
Simplify:      T_Kerr = T_Schw(M_f) · 2 √(1−χ²) / (1 + √(1−χ²))
              T_Schw(M_f) = ℏ c³/(8π G M_f k_B) = 6.46×10⁸ K
              factor = 2·0.728/1.728 = 0.843
              T_Kerr = 6.46×10⁸ · 0.843 = 5.44×10⁸ K
              kT_Kerr = 47 keV
Direction:     T_Kerr < T_Schw because rotation (a > 0) lowers surface gravity.
              The merger product is ~16% COOLER than a non-rotating BH of equal mass.
```

So the merger product radiates at **47 keV peak** rather than the naive 53 keV from a Schwarzschild M_f. The luminosity is also reduced because P ∝ T⁴ effectively (with greybody corrections).

**MISSED.** Two important Page-radiation effects that change the final-state evolution:

1. **Spin-down before mass-down.** Page (1976) showed that for a near-extremal Kerr BH the angular-momentum loss rate dJ/dt exceeds (in dimensionless terms) the mass-loss rate dM/dt by a factor of ~2–3 for χ ≳ 0.7, because superradiant amplification of the modes with mℏ > 0 dominates the Hawking spectrum. For χ_f = 0.685 (just below this regime), the spin-down/mass-down ratio is ~1.5–2. **Substitution chain — fractional spin-down before significant mass loss:**

   ```
   Definition:    df = -dχ/dt · M / (dM/dt)  ≡ "spin-down efficiency factor"
   Page tabulation (χ ≈ 0.7):  df ≈ 1.7
   Direction:     For each 1% mass loss the spin loss is ~1.7%.
                  The merger product spins down to χ ≲ 0.1 BEFORE losing
                  ~50% of its mass. The PBH becomes effectively Schwarzschild
                  long before it becomes light.
   ```

2. **Lifetime correction.** Your E4 stops at the geometric final state; the *evaporation* timeline is:

   ```
   τ_evap(M_f = 1.9×10^14 kg) = 5120 π G² M_f³ / (ℏ c⁴)
                              = 5.77×10²⁶ s = 1.83×10¹⁹ yr
   τ_evap / t_Hubble           = 1.33×10⁹.
   Direction:     The merger product persists for 1.3 BILLION Hubble times.
                  It is quasi-permanent on every imaginable astrophysical scale.
   ```

**EMERGES.** The "merger remnant" picture you constructed in E4 is actually the *initial* state of a 1.83×10¹⁹-year evaporation history. In Page-curve language, the merger marks t = 0 of the new, larger BH's evaporation clock. The first ~1% of mass gets dumped over `0.01 · τ_evap ≈ 5.8×10¹⁷ yr` — which is already ≈ 13 Hubble times. So:

| Stage | Duration | What happens |
|:---|:---|:---|
| Merger ringdown | 5.8×10⁻²¹ s | GW pulse at f≈10²⁰ Hz |
| Spin-down (χ:0.685→0.1) | ~10¹⁷ yr | Page-suppressed mass loss; mostly J_radiated |
| Schwarzschild evaporation | ~10¹⁹ yr | Standard P ∝ M⁻² |
| Final burst (last second) | ~1 s | Spectrum sweeps GeV→TeV→Planck |
| Endpoint | unknown | Page curve transition / remnant / firewall |

The merger event in the user's living room is not a *final* state — it is the *opening move* of a 10¹⁹-year evaporation drama. Geometrically inert; thermally evolving on cosmological timescales.



#### Re: E5 — Energy Budgets

**AGREE.** The headline number E_rest = 8.99×10³⁰ J is correct, and your point that "mc² is locked behind the horizon classically" is the right starting point. Your KE-vs-cataclysm table at the halo virial v ≈ 220 km/s gives KE ≈ 2.4×10²⁴ J ≈ 6 Chicxulubs — also correct. The Bondi-mediated dynamical-friction drag at 10⁻¹⁶ m/s² being negligible against KE deposition is right.

**DISAGREE.** Two corrections to the energy ledger:

1. **Hawking radiation is not an "eventual" channel — it is *steady-state* at this mass.** Each PBH at M = 10^14 kg radiates P = 3.56×10⁴ W = 35.6 kW *continuously*. Over the canonical "encounter time" — say, the user's lifetime τ_user ~ 10⁹ s — each PBH dumps:

   ```
   Definition:    E_Hawking,user = P · τ_user
   Substitute:    P = 3.56×10⁴ W, τ_user = 10⁹ s
   Simplify:      E_Hawking,user = 3.56×10¹³ J ≈ 0.6 · Hiroshima
   Direction:     One PBH in your living room dumps a Hiroshima-bomb-equivalent
                  of HARD GAMMA RADIATION over a single human lifetime.
   ```

   This is not a small effect. The Hawking channel deposits more than 10¹³ J directly into surrounding matter (every photon scatters within Compton mean-free-path of meters in air, ~cm in flesh). It is *the* dominant ongoing energy-deposition channel for a stationary PBH. Your E5 didn't include it.

2. **Cumulative integrated comparison.**

   ```
   Definition:    E_Hawking,Hubble = P · t_Hubble
   Substitute:    P = 3.56×10⁴ W, t_Hubble = 4.35×10¹⁷ s
   Simplify:      E_Hawking,Hubble = 1.55×10²² J
   Compare:       KE_orbital (v=30km/s) = 4.5×10²² J
                  KE_orbital / E_Hawking,Hubble = 2.9
                  KE_halo (v=220km/s)   = 2.4×10²⁴ J
                  KE_halo / E_Hawking,Hubble = 130
   Direction:     KE channel STILL dominates the Hawking channel by 2 OOM at halo
                  velocities, even integrated over Hubble time.
   ```

   So your "kinetic + tidal, not rest-energy-converted" conclusion is correct, but the gap between mechanical and thermal channels is only 2 OOM, not "many orders smaller" as your E5 phrased it for the in-room thermal channel. At human-scale durations the Hawking channel is small but radiologically lethal; at cosmological durations it remains subdominant to KE.

**MISSED.** Two channel-comparison points:

1. **Per-second comparison ladder.** Your table compares KE (one-shot) to bombs (one-shot). The right comparison for a *resident* PBH is steady-state luminosity:

   | Source | Luminosity (W) |
   |:---|---:|
   | Incandescent bulb | 60 |
   | Space heater | 1.5×10³ |
   | One PBH (M=10^14 kg) Hawking | **3.56×10⁴** |
   | US house electrical peak | ~3×10⁴ |
   | Two PBHs co-orbiting | **7.13×10⁴** |
   | Average human metabolism | 100 |

   **Direction**: a PBH *as a power source* delivers about as much as a high-end household electrical service — except it is in 100-keV gamma rays, so it kills everything in line of sight rather than running the toaster.

2. **Coupling efficiency to room is ~unity for Hawking, ~10⁻⁷ for KE.** This is the inversion of your "KE deposition" picture. KE couples gravitationally to the room (tidal impulse) at efficiency ε_KE ~ E_frag/KE ~ 4×10⁻⁷ (your E6 number for rock). Hawking gamma photons couple electromagnetically with mean free path λ_γ ≈ few cm in dense matter, ε_Hawking ~ 1 within a 10-m sphere. So while KE budget > Hawking budget by 10² (instantaneous KE vs Hubble-integrated Hawking), the *deposited* energies are:

   | Channel | Total energy | Coupling ε | Deposited |
   |:---|---:|---:|---:|
   | KE (halo) | 2.4×10²⁴ J | 4×10⁻⁷ | ~10¹⁸ J |
   | Hawking (1 yr) | 1.1×10¹² J | ~1 | 1.1×10¹² J |
   | Hawking (1000 yr) | 1.1×10¹⁵ J | ~1 | 1.1×10¹⁵ J |

   The KE channel still wins for a single fast traversal — by ~6 OOM — but for any *resident* PBH that hangs around, the Hawking channel becomes comparable on million-year timescales. **For the "they collide and stop in the living room" scenario, Hawking dominates over geological time. For the "they pass through and leave" scenario, KE dominates.** The orbital-decay timescale (your E3) tells us they don't bind at meter scale, so practically the encounter is hyperbolic — KE dominates.

**EMERGES.** The correct cataclysm bookkeeping is **three-channel**:

| Channel | Symbol | Magnitude | Coupling | Deposited per encounter |
|:---|:---|---:|---:|---:|
| Rest energy (locked) | mc² | 9×10³⁰ J | 0 | 0 |
| Kinetic (mechanical) | ½mv² | 2.4×10²⁴ J | 4×10⁻⁷ | 10¹⁸ J |
| Hawking (thermal, per s) | P | 3.6×10⁴ W | ~1 | 3.6×10⁴ J/s |
| Gravitational waves | E_GW | 9×10²⁹ J (if merger) | ~10⁻⁵⁰ | 0 |

**Direction**: cataclysm = KE × 4×10⁻⁷ + P × τ_resident. For a flyby (τ_resident ~ τ_cross ~ 425 s), KE channel wins by ~12 OOM. For a captured PBH (τ_resident ~ Hubble time), Hawking channel dominates the deposited energy by 3-4 OOM. The PBHs in question, per E3, don't capture — so KE wins, and the cataclysm is mechanical, not thermal.



#### Re: E6 — Approach Geodesics

**AGREE.** Your geodesic-traversal picture is correct. τ_cross = 425 s, the 74-cm pulverized cylinder, the ~16-gigatonne fragmented mass, E_frag ≈ 1.6×10¹⁶ J ≈ 0.07 Tsar Bomba, M ≈ 8 seismic equivalent — all check out. The "Earth bleeds, does not die" conclusion is correct: 16 OOM below Earth's binding energy, so global integrity is preserved. Your Bondi-rock estimate Ṁ_BHL = 1.7×10⁻⁹ kg/s is in the right range (I will use it below).

**DISAGREE.** Your microgram-net-accretion claim is *correct* during transit but glosses over the steady-state balance. Substitution chain for the resident PBH (after transit, hypothetically captured by Earth's gravity — which doesn't happen for v=30 km/s but consider the limit):

```
Definition:    Ṁ_net = Ṁ_BHL − |Ṁ_Hawking|
Substitute:    Ṁ_BHL,rock = 1.7×10⁻⁹ kg/s (your E6),
              |Ṁ_Hawking| = P/c² = 3.56×10⁴ / (3×10⁸)² = 3.96×10⁻¹³ kg/s
Simplify:      Ṁ_net = 1.7×10⁻⁹ − 3.96×10⁻¹³
                     ≈ 1.7×10⁻⁹ kg/s (Hawking is 0.02% correction)
Direction:     In rock at v=30 km/s, BHL accretion DOMINATES Hawking emission
              by 4.3×10³ ×. The PBH grows during transit through Earth.
              Microgram accretion confirmed; net sign is positive.
```

But during transit at v=30 km/s, Bondi accretion in rock is geometrically *limited* by the rock's sound speed (c_s,rock ~ 5 km/s) — for v ≫ c_s the BHL formula uses v not c_s in the denominator: r_B = 2GM/v² ≈ 1.5×10⁻¹⁰ m, dominated by the bulk-flow speed, not local thermal motion. Your 1.7×10⁻⁹ kg/s number is in the right ballpark.

**MISSED.** Three Hawking-side additions to the approach picture:

1. **Hawking ionization wake.** As the PBH transits Earth, each gamma photon emitted near the trajectory has Compton mean-free-path λ_Compton(100 keV) ≈ 5 cm in rock (density 3000 kg/m³). The 35.6 kW of gamma luminosity ionizes a cylinder of radius ~10 cm around the trajectory in addition to the 37-cm tidal cylinder. **The trajectory leaves a doubly-pulverized core (tidal, r ≲ 37 cm) inside an ionization sleeve (Hawking, r ≲ 10 cm) inside an outer thermal halo (re-radiated soft X-rays / UV, r ≲ several m).** The seismic transient inherits not just mechanical kinetic dissipation but also Hawking-deposited ionization heat.

2. **Heat deposition along the trajectory.**

   ```
   Definition:    E_Hawking,transit = P · τ_cross
   Substitute:    P = 3.56×10⁴ W, τ_cross = 425 s
   Simplify:      E_Hawking,transit = 1.51×10⁷ J ≈ 4 kg of TNT equivalent
   Direction:     The Hawking thermal deposit during transit is 9 OOM SMALLER
                  than the tidal-fragmentation budget E_frag = 1.6×10¹⁶ J.
                  Hawking transit-heating is irrelevant for Earth-scale transit.
   ```

   So during a *fast* transit (v=30 km/s, 7 minutes) the Hawking channel deposits a few kilograms of TNT — not noticeable against the gigatonne-scale tidal disruption.

3. **Q5 preview — final-state mass conservation.** Your E6 microgram accretion + my Hawking 1.7×10⁻¹⁰ kg loss during 425 s gives Δm during transit of +1.7×10⁻⁶ − 1.7×10⁻¹⁰ ≈ +1.7×10⁻⁶ kg. **Direction**: the PBH leaves Earth heavier than it entered, by a microgram. This is observationally negligible but theoretically tidy: the encounter is a net mass-gain event for the PBH, not a net mass-loss. Over many such encounters in galactic history, PBHs in the unconstrained window can mass-up by orders of magnitude if they live in dense ISM regions long enough.

**EMERGES.** The Earth-transit damage budget is dominated by the *mechanical* tidal channel (your E6 is 99.9999% of the deposited energy). The Hawking channel adds:
- A radiation sleeve around the tidal cylinder (negligible thermal contribution).
- A microgram of mass to the PBH (negligible mass change).
- A long after-burst of soft X-rays from ionized recombination (potentially observable on the surface around entry/exit craters as faint UV/optical glow lasting ~ms after passage).

**The Hawking channel modifies the *aesthetic* of the transit (a very faintly glowing column) but not its *mechanical* outcome (the M8 seismic + craters).** Your E6 conclusion stands: planet bleeds, does not die. The radiation sleeve might brighten the entry/exit signatures by a factor of a few, but the dominant observable is the seismic transient and the surface craters at the entry/exit points.



### Part 2: Hawking's Original Analysis

#### H1. Hawking Temperature and Luminosity at 10^17 g (T1, T4)

**The two fiducial formulae** for a non-rotating Schwarzschild BH:

```
T_H = ℏ c³ / (8π G M k_B)              (Hawking 1975)
P   = ℏ c⁶ / (15360 π G² M²)            (Stefan-Boltzmann + greybody-corrected
                                          single-photon-channel approximation)
```

**Substitution chain — canonical case M = 10^14 kg = 10^17 g:**

```
Definition:    T_H = ℏ c³ / (8π G M k_B)
Substitute:    ℏ = 1.055×10⁻³⁴ J·s, c = 2.998×10⁸ m/s, G = 6.674×10⁻¹¹, M = 10^14, k_B = 1.381×10⁻²³
Numerics:      T_H = 1.055×10⁻³⁴ · (2.998×10⁸)³ / (8π · 6.674×10⁻¹¹ · 10^14 · 1.381×10⁻²³)
              T_H = 2.846×10⁻⁹·⁵ / 2.318×10⁻¹⁸  (cancelling powers carefully)
              T_H = 1.227×10⁹ K
Conversion:    kT_H = 1.381×10⁻²³ · 1.227×10⁹ / (1.602×10⁻¹⁹) = 105.8 keV
Direction:     The peak photon energy is 105.8 keV — squarely SOFT GAMMA / hard X-ray.
```

```
Definition:    P = ℏ c⁶ / (15360 π G² M²)
Substitute:    same as above, M² = 10²⁸
Numerics:      P = 1.055×10⁻³⁴ · (2.998×10⁸)⁶ / (15360 π · (6.674×10⁻¹¹)² · 10²⁸)
              P = 7.71×10¹³ / 2.165×10⁹
              P = 3.563×10⁴ W = 35.6 kW
Direction:     Power output is a few tens of kilowatts — NOT a cataclysm-scale luminosity.
```

**Photon-energy regime check.** The peak of a 1.23×10⁹ K Planck spectrum sits at hν_peak ≈ 2.82 kT ≈ 298 keV (Wien's law). The pair-production threshold is 2 m_e c² = 1.022 MeV ≈ 9.7 kT. The fraction of photon flux above threshold:

```
Definition:    fraction f_pair = ∫_{2m_e c²}^∞ B_ν dν / ∫_0^∞ B_ν dν
At kT = 106 keV with E_threshold = 1022 keV, x = E/kT = 9.65:
              The Planck integral above x = 9.65 is exp(-9.65)·(small polynomial) ~ 6×10⁻⁵
Direction:     Less than 0.01% of Hawking photons exceed the e+e- pair threshold at M=10^14 kg.
              The PBH at this mass is essentially a PURE GAMMA emitter; no significant
              lepton or hadron channel until the BH has lost mass and T_H climbs.
```

**Particle channels (Page 1976 graybody factors qualitatively).** At kT_H = 106 keV:
- **Photons (massless, spin 1)**: ~63% of flux (greybody-suppressed — the spin-1 graybody factor at low frequency is reduced by the spin-1 angular-momentum barrier).
- **Neutrinos (massless 3 species, spin ½)**: ~37% of flux. Neutrinos free-stream invisibly out of the encounter.
- **Gravitons (massless, spin 2)**: ~2% — negligible.
- **Electrons/positrons**: suppressed; only the Wien tail above 1.022 MeV contributes, ≪ 1% at this mass.
- **Higher-mass particles** (μ at 105 MeV, π at 140 MeV, …): exponentially suppressed by Boltzmann factor exp(−m/kT) = exp(−10³).

So at M = 10^14 kg the PBH is effectively a *gamma plus neutrino* emitter. Total electromagnetic-channel power is ~22 kW per PBH; neutrino channel ~13 kW (lost to space); graviton channel negligible.

**Mass-dependence table (verified by Python):**

| M (kg) | T_H (K) | kT_H | P (W) | τ_evap (s) | τ/t_Hubble | Comment |
|---:|---:|---:|---:|---:|---:|:---|
| 1.7×10¹¹ | 7.22×10¹¹ | 62 MeV | 1.23×10¹⁰ | 4.3×10¹⁷ | ~1 | Evaporation cliff (M_*) |
| 5×10¹¹ | 2.45×10¹¹ | 21 MeV | 1.43×10⁹ | 1.05×10¹⁹ | 24 | E1 folklore lower edge |
| 1×10¹⁴ | 1.23×10⁹ | 106 keV | 3.56×10⁴ | 8.4×10²⁵ | 1.9×10⁸ | **Canonical case** |
| 5×10¹⁴ | 2.45×10⁸ | 21 keV | 1.43×10³ | 1.05×10²⁸ | 2.4×10¹⁰ | gamma-ray-background limit |
| 1×10¹⁷ | 1.23×10⁶ | 106 eV | 3.56×10⁻² | 8.4×10³⁴ | 1.9×10¹⁷ | E1 lower edge (asteroid mass) |
| 1×10²² | 12 | 1 meV | 3.56×10⁻¹² | 8.4×10⁴⁹ | 1.9×10³² | E1 upper edge (small moon) |

**Key direction at the bottom of the unconstrained DM window (M ~ 5×10¹⁴ g = 5×10¹¹ kg)**:
```
T_H = 2.45×10¹¹ K, kT_H = 21 MeV (above pair production threshold);
P = 1.43×10⁹ W = 1.4 GW (industrial-scale power!);
τ_evap = 1.05×10¹⁹ s ≈ 24 Hubble times.
Direction:     At 5×10¹¹ kg the PBH is a GIGAWATT gamma source emitting MeV-scale photons,
              with pair-production turned ON — these emit electrons/positrons copiously
              and produce annihilation lines at 511 keV.
```

**At the top of the window (M = 10²² g = 10¹⁹ kg)**:
```
T_H = 1.23×10⁴ K (cooler than the Sun's surface!);
P = 3.56×10⁻⁶ W = a few microwatts;
kT_H = 1.06 eV — visible/IR Planckian.
Direction:     A 10²² g PBH is a barely-warm-glow visible-light source, microwatt-scale.
              Completely undetectable except by very-near-field thermometry.
```

**Bottom-line H1:** the mass scaling P ∝ M⁻², T ∝ M⁻¹ produces a vast dynamic range across the asteroid-mass window. Asteroid-mass canonical (M=10^14 kg = 10^17 g) sits at 35 kW, 100-keV gammas — radiologically lethal at meter range, mechanically benign at meter range, observationally invisible at light-year range.



#### H2. Atmospheric Interaction — Bondi-Hoyle Accretion vs Hawking Emission (T2)

**The central radiation-vs-accretion balance question.** A PBH simultaneously *gains* mass via Bondi-Hoyle-Lyttleton (BHL) accretion and *loses* mass via Hawking emission. The dimensionless balance ratio R(M, ρ, v) = Ṁ_BHL / |Ṁ_Hawking| determines whether the PBH grows or shrinks in any given environment.

**The two formulae:**

```
Ṁ_BHL    = 4π (G M)² ρ / (c_s² + v²)^(3/2)         (Bondi 1952)
|Ṁ_H|    = P / c² = ℏ c⁴ / (15360 π G² M²)         (Hawking mass-loss)
```

**Substitution chain — air at typical encounter velocity (canonical):**

```
Definition:    Ṁ_BHL = 4π (G M)² ρ_air / (c_s² + v²)^{3/2}
Substitute:    G = 6.674e-11, M = 10^14, ρ_air = 1.2 kg/m³, c_s = 343 m/s, v = 2×10⁵ m/s
              (G M)² = (6.674e-11 · 10^14)² = (6.674e3)² = 4.45×10⁷
              v² ≫ c_s²: (c_s²+v²)^{3/2} ≈ v³ = 8×10¹⁵
Numerics:      Ṁ_BHL = 4π · 4.45×10⁷ · 1.2 / 8×10¹⁵
              Ṁ_BHL = 8.40×10⁻⁸ kg/s

Compare:       |Ṁ_H| = 3.96×10⁻¹³ kg/s

Ratio:         R = Ṁ_BHL / |Ṁ_H| = 8.40×10⁻⁸ / 3.96×10⁻¹³ = 2.12×10⁵
Direction:     In AIR at v=200 km/s, BHL accretion EXCEEDS Hawking emission by 5 OOM.
              The PBH gains mass when traversing the atmosphere.
```

**Substitution chain — Earth-orbital v (slower-encounter limit):**

```
v = 3×10⁴ m/s, all else as above:
Ṁ_BHL = 4π · 4.45×10⁷ · 1.2 / (3×10⁴)³ = 4π · 4.45×10⁷ · 1.2 / 2.7×10¹³
      = 2.49×10⁻⁵ kg/s
R = 2.49×10⁻⁵ / 3.96×10⁻¹³ = 6.28×10⁷
Direction:     At Earth-orbital v, ratio rises by 10² because Ṁ_BHL ∝ 1/v³ and v drops 7×.
              BHL dominates by 8 OOM.
```

**Substitution chain — interstellar medium (low-density limit):**

```
ρ_ISM = 10⁻²¹ kg/m³, v = 200 km/s:
Ṁ_BHL = 4π · 4.45×10⁷ · 10⁻²¹ / 8×10¹⁵ = 7.0×10⁻²⁹ kg/s
R     = 7.0×10⁻²⁹ / 3.96×10⁻¹³ = 1.77×10⁻¹⁶
Direction:     In the ISM, ratio is 16 OOM BELOW unity.
              The PBH net loses mass — Hawking emission DOMINATES BHL by 16 OOM.
```

**The critical density.** Set R = 1 to find the boundary between net-accreting and net-emitting regimes:

```
Definition:    ρ_crit ≡ |Ṁ_H| · (c_s² + v²)^{3/2} / (4π (GM)²)
Substitute:    M = 10^14 kg, v = 2×10⁵ m/s
Simplify:      ρ_crit = 3.96×10⁻¹³ · 8×10¹⁵ / (4π · 4.45×10⁷)
              ρ_crit = 5.67×10⁻⁶ kg/m³
Direction:     At ρ_crit = 5.67×10⁻⁶ kg/m³ (between deep ISM and stratospheric air),
              the two channels balance. Above ρ_crit: NET GROWTH. Below: NET SHRINKAGE.
```

**Comparison environments:**

| Environment | ρ (kg/m³) | v (m/s) | Ṁ_BHL (kg/s) | Ṁ_BHL/Ṁ_H | Sign |
|:---|---:|---:|---:|---:|:---:|
| Cold ISM | 10⁻²¹ | 2×10⁵ | 7.0×10⁻²⁹ | 1.8×10⁻¹⁶ | shrink |
| Cold molecular cloud | 10⁻¹⁹ | 2×10⁵ | 7.0×10⁻²⁷ | 1.8×10⁻¹⁴ | shrink |
| Stellar wind near Sun | 10⁻²⁰ | 2×10⁵ | 7.0×10⁻²⁸ | 1.8×10⁻¹⁵ | shrink |
| Upper stratosphere | 10⁻³ | 3×10⁴ | 2.1×10⁻⁸ | 5.2×10⁴ | grow |
| Sea-level air | 1.2 | 3×10⁴ | 2.5×10⁻⁵ | 6.3×10⁷ | grow |
| Liquid water | 1×10³ | 3×10⁴ | 2.1×10⁻² | 5.2×10¹⁰ | grow |
| Rock | 3×10³ | 3×10⁴ | 6.2×10⁻² | 1.6×10¹¹ | grow |

(Einstein's E2 quoted Ṁ ≈ 10⁻¹⁵ kg/s for air at 30 km/s — that uses 4π r_B² ρ v with r_B = 30 μm. The full BHL formula 4π(GM)²ρ/v³ is dimensionally identical to 4π r_B² ρ v at v ≫ c_s, but the prefactor differs by O(1). My number 2.5×10⁻⁵ kg/s vs his 4×10⁻⁷ kg/s is the same calculation; difference is the 4π factor handling. Direction is identical: BHL ≫ |Ṁ_H| in air.)

**Bottom line H2:** **In every Earth-bound environment, BHL accretion overwhelms Hawking emission by 4-11 orders of magnitude.** The PBH grows during any close encounter with terrestrial matter. Only in the deep ISM (ρ ≪ 10⁻⁶ kg/m³) does Hawking emission win, and there the PBH is so isolated that its mass-loss rate is irrelevant cosmologically. **The Hawking channel is the long-time-averaged loser** — for any PBH that spends most of its life in galactic-disk environments (typical density >> ρ_crit) the asymptotic future is mass *growth*, not evaporation. Only for PBHs in the deep cosmological void do we approach the canonical "evaporates in 10²⁵ yr" picture.

This actually creates a *bimodal evolution*: PBHs in dense regions grow over Hubble time, those in voids evaporate. The terminal-evaporation gamma-ray burst signal (Page 2008) only fires for the void-class PBHs.



#### H3. GW Emission and the Merger from a Quantum Lens (T3)

**Quantum-corrections diagnostic table.** For a 10^14 kg PBH:

```
Definition:    diagnostic_i = (relevant scale_i) / r_s
Compute:       (a) ℓ_P / r_s = 1.616×10⁻³⁵ / 1.485×10⁻¹³ = 1.09×10⁻²²
              (b) λ_C,e / r_s = 3.86×10⁻¹³ / 1.485×10⁻¹³ = 2.60
                  ⇒ r_s / λ_C,e = 0.385
              (c) λ_C,p / r_s = 2.10×10⁻¹⁶ / 1.485×10⁻¹³ = 1.41×10⁻³
              (d) ℓ_QCD / r_s = 1×10⁻¹⁵ / 1.485×10⁻¹³ = 6.7×10⁻³
Direction:
              (a) r_s/ℓ_P ~ 10²² ≫ 1: comfortably semiclassical, no quantum-gravity corrections.
              (b) r_s/λ_C,e ≈ 0.4: HORIZON IS SUB-COMPTON for electrons.
                  Electrons cannot be localized in the near-horizon region without
                  pair-creation; this is consistent with the Hawking-spectrum
                  pair-suppression observed in H1 (kT < 2 m_e c²).
              (c) r_s/λ_C,p ≈ 10³ ≫ 1: protons fit comfortably outside.
              (d) r_s/ℓ_QCD ≈ 10² ≫ 1: hadron physics is small-scale relative to horizon.
```

**Conclusion: no relevant quantum-gravity corrections at the inspiral or merger scale.** The semiclassical Hawking calculation applies at every stage. The only quantum-mechanical subtlety is the electron-Compton-localization point in (b), which manifests as the suppressed e⁺e⁻ channel in the Hawking spectrum.

**Ringdown enhancement of the Hawking flux — speculative.** During the merger transient, surface gravity κ swings from progenitor's value (κ_progenitor = c⁴/(4 G m) ≈ 3.0×10²⁹ m/s² each) to merger-product's Kerr value (κ_f = 1.34×10²⁹ m/s² from Re: E4). κ *decreases* slightly during merger (because M_f > 2 m_progenitor only by 0.95×, and Kerr lowers κ further by 0.84×).

**Substitution chain — does Hawking flux spike during the merger transient?**

```
Definition:    P_H ∝ κ²/A (Stefan-Boltzmann analog with T ∝ κ)
Substitute:    Single progenitor T_progenitor = 1.23×10⁹ K, P = 35.6 kW
              Combined two progenitors: 2 × 35.6 = 71.3 kW
              Merger product T_f = 5.44×10⁸ K (Kerr), P_f = 9.87 kW
Direction:    P_f / P_2-progenitors = 9.87/71.3 = 0.138
              The merger product's STEADY-STATE Hawking luminosity is 14% of the
              two-progenitor sum. The merger DECREASES the steady Hawking flux by ~7×.
```

So contrary to a possible naïve expectation that "more massive horizon = brighter," merger of two equal-mass holes *reduces* the total Hawking flux because P scales as M⁻². Two M-mass holes radiate 2P = 2·c/M²; one 2M-mass hole radiates P/4 = c/(4M²). Ratio = 1/8. With Kerr correction, observed ratio ≈ 1/7.2.

**During the transient:** the ~5 attoseconds of ringdown is far too brief to thermalize a new horizon. The instantaneous Hawking flux during the transient is undefined in the strict adiabatic-limit Hawking calculation; numerical-relativity studies (Christodoulou-Rovelli, Booth-Fairhurst) suggest the Hawking flux smoothly interpolates between progenitor and final values over a few light-crossing times τ_lc ~ r_s/c ~ 5×10⁻²² s. **No flash, no spike — a smooth ~7× DIMMING over zeptoseconds.**

This is consistent with the area theorem: A grows by 56% during merger (your E4), so dA/dt > 0 ⇒ entropy and *cumulative* radiation grow, but the *instantaneous luminosity* drops because the new horizon is "colder" (lower κ) per unit area.

**No detectable thermal transient at merger.** The merger event for two 10^14 kg PBHs is a 9-attosecond ringdown into a slightly-cooler steady-state Hawking source. No spike, no flash, no observable signature in any electromagnetic band.



#### H4. Final State: Persistent BH vs Evaporative Endpoint vs Page-Time Considerations (T4)

**The lifetime formula.**

```
τ_evap(M) = 5120 π G² M³ / (ℏ c⁴)               (Hawking 1975, leading-order)
          = (M/M_*)³ · t_Hubble                  (rescaled form, M_* = 1.73×10¹¹ kg)
```

**Substitution chain — merger product M_f = 1.9×10^14 kg:**

```
Definition:    τ_evap = 5120 π G² M_f³ / (ℏ c⁴)
Substitute:    M_f = 1.9×10^14, M_f³ = 6.86×10⁴²
              5120 π = 1.608×10⁴
              G² = 4.45×10⁻²¹
              ℏ c⁴ = 1.055×10⁻³⁴ · 8.07×10³³ = 8.51×10⁻¹
Numerics:      τ_evap = 1.608×10⁴ · 4.45×10⁻²¹ · 6.86×10⁴² / 8.51×10⁻¹
              τ_evap = 5.77×10²⁶ s = 1.83×10¹⁹ yr
Compare:       t_Hubble = 4.35×10¹⁷ s
              τ_evap / t_Hubble = 1.33×10⁹
Direction:     The merger product persists for 1.33 BILLION Hubble times.
              On any human timescale (10⁹ s) it is rigorously permanent.
              On any astrophysical timescale (10¹⁰ yr) it is permanent.
```

**Endpoint classification:**
- Evaporative on human timescale (τ < 10² yr)? **NO** — τ = 10¹⁹ yr is 17 OOM longer.
- Explosive (τ < seconds, runaway terminal burst now)? **NO** — that requires M < 10⁹ g; we are 14 OOM heavier.
- Quasi-permanent (τ ≫ t_Hubble)? **YES** — by factor 10⁹.

**The critical evaporation mass M_*** — at what mass does τ = t_Hubble?

```
Definition:    Set 5120 π G² M_*³ / (ℏ c⁴) = t_Hubble
Solve:         M_*³ = ℏ c⁴ t_Hubble / (5120 π G²)
              M_*³ = 1.055×10⁻³⁴ · 8.07×10³³ · 4.35×10¹⁷ / (1.608×10⁴ · 4.45×10⁻²¹)
              M_*³ = 5.17×10³³
              M_* = 1.73×10¹¹ kg = 1.73×10¹⁴ g
Direction:     PBHs born below 1.73×10¹¹ kg have already evaporated.
              PBHs born just at this mass are evaporating now.
              This is the lower edge of the surviving PBH-DM population
              (corrected from the folklore ~5×10¹⁴ g — see Re: E1).
```

**Page-curve transition for the merger product.**

```
Definition:    t_Page ~ τ_evap / 2  (half-evaporation time, when entanglement
                                       entropy of radiation peaks)
Substitute:    t_Page ≈ 2.88×10²⁶ s = 9.14×10¹⁸ yr
Compare:       t_Page / t_Hubble = 6.6×10⁸
Direction:     Page-curve transition occurs 660 MILLION Hubble times in the future.
              The information-paradox urgency is ZERO at the living-room scale.
```

**Spin-down history (Page 1976 calculation).** Sketch of the spin-evolution trajectory for the merger product (χ_f = 0.685 → final state):

| Stage | t (yr) | M (kg) | χ | Notes |
|:---|---:|---:|---:|:---|
| Merger | 0 | 1.9×10¹⁴ | 0.685 | Just after ringdown |
| Spin-dominated emission | ~10¹⁷ | 1.85×10¹⁴ | 0.3 | dJ/dt ≫ dM/dt; ~3% mass lost |
| Schwarzschild regime | ~10¹⁸ | 1.5×10¹⁴ | 0.05 | Standard P ∝ M⁻² regime |
| Half-evaporation (t_Page) | 9.1×10¹⁸ | ~1.5×10¹⁴ | ~0 | Entropy peak; full Schwarzschild |
| Last second | 1.83×10¹⁹ − 1 s | 1.7×10⁸ | 0 | Spectrum peaks at GeV→TeV |
| Final burst | 1.83×10¹⁹ | → 0 or remnant? | — | Endpoint physics |

**Direction**: spin-down completes in ~10⁻² of the lifetime; mass-down dominates the remaining ~99% of the lifetime. The merger product spends 99% of its life as an effectively-Schwarzschild Hawking emitter.

**Bottom line H4:** the merger product is a **quasi-permanent Hawking emitter** at the living-room scale. Its endpoint physics — Page-curve transition, possible remnant, possible information-burst — happens on timescales 10⁹ Hubble times in the future. For the user, the merger product is an immutable steady-state 9.9-kW gamma source, sitting in the living room for the rest of cosmic history.



#### H5. Hawking-Driven Energy Release — Comparison to Mechanical Impact (T5)

**The Hawking-luminosity ladder.**

| Source | Luminosity (W) | Comment |
|:---|---:|:---|
| Wristwatch battery | 10⁻⁴ | mW level |
| LED bulb | 10 | continuous |
| Incandescent bulb | 60 | hot wire |
| Average human metabolism | 100 | body heat |
| **Merger-product PBH (M_f=1.9×10^14 kg) Hawking** | **9.87×10³** | merger product |
| Space heater | 1.5×10³ | room heating |
| **Each progenitor PBH (M=10^14 kg) Hawking** | **3.56×10⁴** | one PBH |
| US house electrical service peak | 3×10⁴ | rated |
| **Two PBHs co-orbiting Hawking total** | **7.13×10⁴** | both progenitors |
| Industrial laser cutter | 10⁵ | continuous CW |
| Tsar Bomba (50 Mt, ~30 ns release) | 8×10²⁴ | one-shot |
| Solar luminosity | 3.8×10²⁶ | continuous |
| Local supernova | ~10⁴⁴ | one-shot |

**Direction**: the Hawking luminosity at M = 10^14 kg is *roughly background-radiation* on the scale of a powered house. Two co-orbiting PBHs deliver ~71 kW — about as much as a top-end residential generator, except in 100-keV gammas instead of 60 Hz current.

**Comparison to mechanical-impact channel.**

```
Definition:    P_mechanical = (½ m v²) · ε_coupling / τ_encounter
Substitute:    For a flyby at v=200 km/s, τ_encounter ~ τ_cross ~ 425 s (Earth transit)
              ½ m v² = 2×10²⁴ J
              ε_coupling ~ 4×10⁻⁷ (E6 fragmentation efficiency)
              Effective deposited energy ≈ 2×10²⁴ · 4×10⁻⁷ = 8×10¹⁷ J
              Effective deposited power ≈ 8×10¹⁷ / 425 = 1.88×10¹⁵ W
Compare:       P_Hawking = 7×10⁴ W (two PBHs)
              P_mechanical / P_Hawking = 1.88×10¹⁵ / 7×10⁴ = 2.7×10¹⁰
Direction:     During a fast traversal, the MECHANICAL channel exceeds Hawking by 10 OOM.
              The mechanical impact dominates the cataclysm budget for a flyby
              by a factor of ~10 BILLION.
```

**Substitution chain — which channel wins?**

```
Definition:    R_channel(τ_resident) = P_Hawking · τ_resident / E_mechanical_deposited
Substitute:    P_Hawking = 7×10⁴ W (two PBHs combined)
              E_mechanical_deposited = 8×10¹⁷ J (single fast traversal)
Solve for parity:  τ* = 8×10¹⁷ / 7×10⁴ = 1.14×10¹³ s ≈ 360,000 yr
Direction:     If the PBHs hang around for >360,000 years, Hawking deposits more
              total energy than the single mechanical flyby. Below that, mechanical wins.
              For the "happenstance collision" geometry (E3: hyperbolic encounter,
              not bound), the residency time is ~τ_cross ~ minutes, so MECHANICAL DOMINATES
              by 11-12 OOM. The cataclysm is mechanical.
```

**Cataclysm classification — does the room/house/neighborhood/planet survive?**

| Scale | Mechanical impact | Hawking flux | Outcome |
|:---|:---|:---|:---|
| Living room (1-3 m radius) | tidal r⁻³ inside ~4 m → drywall destroyed (E2) | 35 kW gamma source at 1 m → 2× solar flux, instantly lethal radiation | **House interior destroyed by tidal + immediately lethal to occupants by radiation** |
| House (10-30 m) | tidal r⁻³ → only walls within ~4 m affected | gamma flux at 30 m: F = 35 kW / (4π·900) = 3 W/m² → ~mSv/s dose rate | Structural damage local to PBH path; radiation dose hazardous to occupants |
| Neighborhood (100 m – 1 km) | seismic (M2-M3 equivalent if PBH stops) or no effect (if it passes through) | F at 1 km: 3×10⁻⁶ W/m² → ~μSv/s, sub-acute | Buildings outside drilled cylinder intact |
| Planet (>10⁴ km) | seismic transient ~M8 from chord traversal | gamma flux ~ 10⁻¹⁵ W/m² → undetectable | Earth survives; antipodal crater + global seismic event |

**Comparison to single-impact cataclysms (using one PBH, fast traversal):**

| Cataclysm | Energy (J) | Compare to PBH KE (2×10²⁴ J) | Compare to PBH deposited (~10¹⁸ J) |
|:---|---:|---:|---:|
| Hiroshima (Little Boy) | 6.3×10¹³ | 3.1×10¹⁰ | 1.6×10⁴ |
| Tsar Bomba (50 Mt) | 2.4×10¹⁷ | 8.3×10⁶ | 4.2 |
| Tunguska impact | 5×10¹⁶ | 4.0×10⁷ | 20 |
| Chicxulub | 4×10²³ | 5.0 | 2.5×10⁻⁶ |

**Direction**: the **deposited** energy (10¹⁸ J) is comparable to a few Tsar Bombas spread along a 12,700-km cylinder — locally severe but globally minor. The **KE** budget (10²⁴ J) is Chicxulub-scale but mostly carried away with the escaping PBH. The Hawking channel adds ~10⁴ J/s for as long as the PBH lingers — irrelevant during a flyby, dominant if the PBH is captured.

**Bottom line H5:** **Mechanical-impact channel dominates by 10-12 OOM for a flyby.** Hawking is a side-show — **lethal at meter-scale to humans nearby (~5×10¹¹ mSv/hr at 1 m), benign at planetary scale.** The cataclysm is what Einstein described in E5/E6: kinetic + tidal, not thermonuclear-scale rest-energy conversion. The Hawking channel only modifies the *immediate-vicinity* radiation hazard, not the global energy budget.



#### H6. Quantum Gravity / Information at the Living-Room Scale (T6 + cross-cutting)

**Bekenstein-Hawking entropy of the progenitors and merger product.**

```
Definition:    S_BH = A / (4 ℓ_P²)              [nats; multiply by k_B for SI entropy]
              ℓ_P  = √(ℏG/c³) = 1.616×10⁻³⁵ m
              ℓ_P² = 2.61×10⁻⁷⁰ m²

Progenitor (M = 10^14 kg, r_s = 1.485×10⁻¹³ m):
              A = 4π r_s² = 4π · (1.485×10⁻¹³)² = 2.77×10⁻²⁵ m²
              S = 2.77×10⁻²⁵ / (4 · 2.61×10⁻⁷⁰) = 2.65×10⁴⁴ nats

Merger product (M_f = 1.9×10^14 kg, χ_f = 0.685, r_+ = 2.43×10⁻¹³ m):
              A_Kerr = 4π (r_+² + a²)
                     = 4π · ((2.43×10⁻¹³)² + (9.66×10⁻¹⁴)²)
                     = 4π · (5.91×10⁻²⁶ + 9.32×10⁻²⁷)
                     = 8.65×10⁻²⁵ m²
              S = 8.65×10⁻²⁵ / (4 · 2.61×10⁻⁷⁰) = 8.28×10⁴⁴ nats

Direction:    The merger-product entropy is 8.3×10⁴⁴ nats — a Hilbert-space dimension
              of e^(8.3×10⁴⁴) ~ 10^(3.6×10⁴⁴) microstates. Truly absurd.
```

**Sanity check — area theorem at the merger:**

```
Definition:    ΔS = S_f − (S_1 + S_2)
Substitute:    S_f = 8.28×10⁴⁴
              S_1 + S_2 = 2 · 2.65×10⁴⁴ = 5.30×10⁴⁴
              ΔS = 8.28×10⁴⁴ − 5.30×10⁴⁴ = 2.98×10⁴⁴ nats > 0
Direction:    Generalized second law satisfied. Entropy increased by 56% during merger,
              matching Einstein's E4 area-ratio A_f/A_i = 1.56.
```

**The Page time and information-paradox urgency.**

```
Definition:    t_Page = τ_evap / 2 (canonical Page-curve transition)
Substitute:    τ_evap(M_f = 1.9×10^14 kg) = 5.77×10²⁶ s
              t_Page ≈ 2.88×10²⁶ s = 9.14×10¹⁸ yr
Compare:       t_Hubble = 4.35×10¹⁷ s
              t_Page / t_Hubble = 6.6×10⁸
Direction:     Page time is 660 MILLION Hubble times in the future.
              Information-paradox urgency at the living-room scale: ZERO.
              The PBH does not "leak" appreciable correlations of its initial state
              into the radiation field for the next ~10⁹ Hubble times.
```

**Implication:** even though the user is dead (~10⁻¹⁰ Page times after the encounter), and the merger product is steadily emitting Hawking radiation (radiating ~kT_H of energy per timescale ℏ/(kT_H) ≈ 10⁻²⁰ s, which is ~10⁻³⁹ of its rest energy per t_Hubble), the **entanglement entropy of the radiation has not yet started to decrease**. We are still in the "thermal-flux" regime of the Page curve, where each emitted photon adds entropy independently. The information-bearing modes (where outgoing radiation is entangled with previously-emitted modes through the quantum extremal surface / island formula) only start dominating at t > t_Page — which is 10⁹ Hubble times away.

**Quantum-gravity probe value: zero.**

```
Definition:    Quantum-gravity regime requires r_s ~ ℓ_P, M ~ M_Planck = 22 μg
Compare:       r_s(10^14 kg) / ℓ_P = 1.485×10⁻¹³ / 1.616×10⁻³⁵ = 9.2×10²¹
              M / M_Planck = 10^14 / 2.18×10⁻⁸ = 4.6×10²¹
Direction:     The PBH is 22 OOM ABOVE the quantum-gravity threshold.
              Encountering a 10^14 kg PBH gives ZERO probe of Planck-scale physics.
              All observables are deeply semiclassical.
```

**The "soft-hair" and EFT-of-horizons questions.** Strominger-Hawking-Perry's soft-hair program suggests that BMS supertranslations at null infinity carry non-trivial information about the in-state of the black hole. For a 10^14 kg merger product with t_Page ~ 10¹⁹ yr, the "soft-hair" charges that the user could in principle measure on the radiation field at infinity are:
- BMS supertranslation charges: encoded in the leading 1/r terms of the gravitational field at null infinity. Not separable from the dominant mc²/r monopole on any reasonable timescale.
- Page-curve correlators: only become measurable at t > t_Page.
- Firewall: the firewall argument (AMPS) requires t > t_Page to argue for one. We are well below; no firewall expected.

**Bottom line H6:** the living-room PBH encounter is **rigorously semiclassical**, **rigorously thermal-emission-dominated** (no Page transition for 10⁹ Hubble times), and **a useless quantum-gravity probe** (semiclassical regime, 22 OOM above ℓ_P). The encounter offers NO information-paradox content, NO firewall content, NO trans-Planckian content. It is a clean test of low-energy, classical-horizon Hawking emission — and as such, a very-small-MeV-scale gamma-ray spectrometer near the PBH could in principle measure the kT_H = 106 keV thermal peak and verify the Hawking spectrum at unprecedented S/N. **The encounter is interesting as a *measurement of T_H* — not as a probe of quantum gravity.**



### Questions for Einstein

I have five questions, plus a half. Each one targets a place where your GR-only treatment touches a quantum-thermal subtlety I would like the geodesic perspective on.

**Q1 (Kerr cross-section for hyperbolic capture).** Your E2 derived the gravitational-capture impact parameter as `b_max ≈ r_s · √(c²/v²) ≈ 1.5 nm` for v=30 km/s using the Schwarzschild-Newtonian-focusing limit. For the merger remnant with χ_f = 0.685, does the *Kerr* cross-section for hyperbolic capture differ meaningfully from Schwarzschild at v ~ 200 km/s? Specifically: does the prograde-vs-retrograde asymmetry of the Kerr capture cross-section show up at slow encounter velocities, or is it parametrically suppressed by (v/c) factors that wash it out at v=200 km/s? My intuition (from the Wald-Iyer formalism) is the asymmetry is O((χ v/c)²) ≈ 10⁻⁷ and unmeasurable, but I would like your confirmation from the explicit Kerr-orbit integration.

**Q2 (Gravitational-wave bremsstrahlung from the air-tunneling phase).** As the PBH zips through the atmosphere at v=30 km/s, the *deceleration* due to BHL drag (your E5 a_DF ~ 10⁻¹⁶ m/s², my H2 BHL rate 2.5×10⁻⁵ kg/s) is tiny but nonzero. Any nonzero a generates GW bremsstrahlung at frequency f ~ a/v scale. **Substitution chain:**

```
Definition:    f_brems ~ a_DF / (2π v)  (rough dimensional estimate)
Substitute:    a_DF = G M Ṁ_BHL / v² · (1/M) ~ G Ṁ/v²
              For Ṁ = 2.5×10⁻⁵ kg/s, v = 3×10⁴: a_DF ~ 1.85×10⁻²⁰ m/s²
              f_brems ~ 1.85×10⁻²⁰ / (2π · 3×10⁴) ~ 10⁻²⁵ Hz
Direction:    GW bremsstrahlung is at sub-cosmological frequency; clearly undetectable
              by any extant or proposed detector. The QUESTION is whether your geodesic
              treatment includes any non-quadrupole moment from the asymmetric drag
              (i.e. a memory effect, a Christodoulou step) that I am missing.
```

Does the asymmetric matter accretion produce a non-trivial gravitational memory effect at null infinity, or does the symmetry of straight-line motion through bulk matter wash out the memory term?

**Q3 (Equivalence principle and the e+e- pair plasma).** At M near the bottom of the unconstrained window (M ~ 5×10¹¹ kg, kT_H = 21 MeV) the PBH emits e⁺e⁻ pairs copiously (above 2 m_e c² threshold). Those pairs annihilate at characteristic distance ~λ_e_e ~ 10⁻¹² m and produce a 511-keV positronium plasma sheath around the PBH. **Question**: from the equivalence-principle side, does the PBH "feel" this self-consistent plasma — i.e., is there a Tolman-Oppenheimer-Volkoff-style back-reaction where the effective stress-energy of the pair plasma reduces the effective horizon area, or does the equivalence principle insist that the PBH's geodesic motion is indifferent to the plasma it sources? This is essentially the "self-force" question for radiating Hawking sources, and I'd like your reading on whether the standard Mino-Sasaki-Tanaka self-force formalism applies cleanly when the radiation reaction includes Hawking emission.

**Q4 (GR caveat to "rest mass locked behind horizon" during a transient/merger).** Your E5 emphasized that mc² is locked behind the horizon classically. But during the merger transient, the *area theorem* requires A_f > A_i (your 56% gain), which means the *irreducible* mass increases — but not by enough to account for the full progenitor sum, because you also radiated 5% as GW energy. **Question**: is there a *transient* phase during the ringdown when the horizon is genuinely ill-defined (e.g., between common-apparent-horizon formation and trapped-surface stabilization) where some rest-energy could in principle escape *before* being "locked" by the new horizon? Numerical-relativity simulations show this transient lasting ~few light-crossing times; I'm asking whether a non-perturbative GR argument allows ε > 5% to escape via direct horizon-side leakage during this window, or whether 5% is a hard upper bound from cosmic censorship.

**Q5 (Earth-traversal antipodal exit dynamics).** Your E6 envisioned a 74-cm pulverized cylinder and an antipodal exit crater. **Substitution chain — where exactly on the antipode does the PBH emerge?**

```
Definition:    Coriolis deflection = 2 v × Ω during the 425-s transit
Substitute:    Ω_Earth = 7.27×10⁻⁵ rad/s, v = 3×10⁴ m/s
              Total deflection ~ ½ Ω v τ² ≈ ½ · 7.27e-5 · 3e4 · (425)² ≈ 2×10⁵ m = 200 km
Direction:    The PBH exits the antipodal point shifted by ~200 km eastward (or
              westward depending on the original chord). This is a meaningful
              spatial offset for the "where does the exit crater appear" question.
```

Does your full-GR Earth-rotating-frame analysis confirm the 200-km Coriolis offset, or does Newtonian Coriolis plus the geodesic-correction (Lense-Thirring frame-dragging at the ~10⁻¹⁰ level) give a different answer? I am specifically interested in whether the rotating-Earth metric leads to an *inward-spiraling* geodesic that exits at a slightly different latitude rather than directly antipodal.

**Bonus Q6 (gravitational-wave background from the cosmological PBH merger population).** Your E3 gave τ_GW(a₀ = 1 m) = 2.5×10²¹ yr, but PBHs born in cosmological clustering (PBH-PBH binaries forming at z ~ 30 from initial proximity) might have characteristic separations far below 1 m. **Question**: if 10^14 kg PBHs constitute 100% of dark matter, and a fraction f_bin ~ 10⁻⁶ of them form *very tight* binaries during structure formation, the merger rate today is `R_merger ~ f_bin · n_PBH / τ_GW(a_typical)`. Where does the resulting stochastic gravitational-wave background sit in frequency space? My guess: the inspiral spectrum spans LIGO + LISA + PTA bands depending on a_typical, but the strain is too small to detect by ~10 OOM at 10^14 kg (because h ∝ M^(5/6)). Confirm or refute?

These six questions plus the five I've answered (E7) close the cross-domain inspection. I'll respond to whatever you launch back in Round 2.



---

## Round 2 — Einstein (Final Round)

### CONVERGENCE — Where Einstein now agrees with Hawking

I concede on six points, three substantive and three numerical-precision.

**C1. The merger DIMS, it does not brighten (Re: E3, H3).** I had implicitly carried the intuition that "more horizon area = more Hawking flux"; Hawking's H3 substitution chain `P ∝ M⁻²` shows the opposite. Two M-mass progenitors radiate `2 P(M)`, while a single 2M-mass merger product radiates `P(M)/4`, ratio 1/8. With the additional Kerr factor `2√(1−χ²)/(1+√(1−χ²)) = 0.843` at χ_f=0.685 the Schwarzschild merger-product power scales further to ~14% of the two-progenitor sum. I verified this independently:

```
Definition:    R_dim = P(M_f, χ_f) / (2 · P(m))
                     = [P_Schw(M_f) · g(χ_f)⁴-ish-corrected] / (2 · P_Schw(m))
              For pure-Schwarzschild surrogate: P(M_f)/2P(m) = m²/(2 M_f²) = (1/1.9²)/2 = 1/7.22
Substitute:    P_progenitor = 35624.8 W
              2·P_progenitor = 71249.6 W
              P_f (Schwarzschild surrogate, M_f=1.9×10^14 kg) = 9868.4 W
              R_dim = 9868.4 / 71249.6 = 0.1385 = 1/7.22  EXACTLY (verified Python)
Direction:    The merger event REDUCES the steady-state Hawking flux by factor 7.22
              (or 8 with Kerr-cooling). The picture I implicitly assumed in E4 — that
              the merger marks the start of a hotter, brighter phase — is BACKWARDS.
              The user actually walks INTO a brighter room (two 35.6 kW progenitors)
              than walks out (one 9.9 kW remnant).
```

This inverts the dramatic arc of the encounter: the cataclysm is most thermally intense *before* the (hypothetical) merger, not after.

**C2. The radiation kill-radius dwarfs the tidal kill-radius (Re: E2, H1).** My E2 stopped at the geodesic-deviation analysis (37 cm bone-failure threshold, 11 m for 1g differential). Hawking's H1+Re:E2 added the gamma flux: 35.6 kW in 100-keV photons gives F(1 m) = 2.84 kW/m² (2× solar), and a ~30–100 m LD50 radius for acute-dose lethality. The tidal-stretch kill-zone of ~37 cm is a *factor of ~30 smaller* than the radiation kill-zone. My "death is geometric" framing was wrong; **death is radiological at meter-to-tens-of-meters scale**, with the geometric/tidal lethality only relevant within 0.5 m. I accept this fully — the dominant proximate hazard at M = 10^14 kg is gamma-ray exposure, not gravitational stretching.

**C3. Hawking is the long-time-averaged loser to BHL accretion in any terrestrial environment (Re: E6, H2).** My E6 Bondi-accretion estimate (~10⁻⁹ kg/s in rock, microgram net gain over transit) was correct for the *direction* but I had not appreciated how dominant the accretion channel is over the emission channel. Hawking's H2 ratio table shows R = Ṁ_BHL/Ṁ_H spans 10⁴ to 10¹¹ across air/water/rock, with critical density ρ_crit ≈ 5.7×10⁻⁶ kg/m³ (between deep ISM and stratosphere). **Direction: any PBH bound to Earth's gravitational field grows asymptotically; the "evaporates in 10²⁵ yr" folklore applies only to PBHs in the deep cosmological void.** This is a non-trivial cosmological fact: the 10^14 kg DM PBH population is bimodal in evolutionary fate, sorted by the local matter density they spend most of their lives traversing.

**C4. Lower edge of the unconstrained PBH-DM window (Re: E1).** I quoted M ~ 5×10¹⁴ g as folklore. Hawking's substitution chain gives the bare M_* = 1.73×10¹¹ kg = 1.73×10¹⁴ g. Verified Python:

```
Definition:    M_* such that τ_evap(M_*) = t_Hubble = 4.35×10¹⁷ s
              τ_evap(M) = 5120 π G² M³ / (ℏ c⁴)
Substitute:    M_*³ = ℏ c⁴ t_Hubble / (5120 π G²) = 5.17×10³³
Simplify:      M_* = 1.7294×10¹¹ kg = 1.7294×10¹⁴ g  (Python: 172,941,769,330 kg)
Direction:    My quoted 5×10¹⁴ g folds in greybody+threshold corrections; the bare
              fiducial is ~3× LOWER. The corrected lower edge of the unconstrained
              window for "still around today" is therefore at 1.7×10¹¹ kg, not 5×10¹¹ kg.
```

Concede the numerical refinement. The folklore-quoted "5×10¹⁴ g" is the corrected emission-cliff after greybody/threshold cascades; the bare fiducial is lower, which means the surviving PBH-DM lower edge has more breathing room than I implied.

**C5. Page-time irrelevance at this scale (Re: E4, H4).** I left the endpoint physics open in E4. Hawking's H4 settled it: τ_evap(M_f = 1.9×10^14 kg) = 5.77×10²⁶ s = 1.83×10¹⁹ yr, giving t_Page ≈ 9.14×10¹⁸ yr ≈ 6.6×10⁸ Hubble times in the future. Information-paradox urgency at the living-room scale is rigorously zero. The merger product is, for all practical and observational purposes including the entire future of the observable universe, **eternally stable as a steady-state thermal source**. My "endpoint physics" question (E7-Q3b) is moot at the relevant timescale — the question of remnant vs full evaporation is genuinely 10⁹ Hubble times into the future and need not be answered to close the cataclysm bookkeeping.

**C6. The asteroid-mass window's stubbornness as a triple intersection (H1 emerges).** Hawking's "constraint-map intersection of three independent thermal/optical observables" reading of the [10¹⁷, 10²²] g window is sharper than my E1 framing. The window survives because (i) τ_evap > t_H, (ii) r_s ≪ μm, (iii) gamma flux too dim at solar-neighborhood densities. These three conditions independently fail outside [10¹⁷, 10²²] g; their intersection defines the surviving band. I had treated this as one-condition-per-edge; Hawking is right that all three operate simultaneously across the interior.

### DISSENT — Where Einstein still disagrees (new evidence only)

Three sharp residual disagreements, each backed by a new substitution chain that did not appear in R1.

**D1. The Kerr capture asymmetry is LINEAR in χv/c, not quadratic.** Hawking offered an intuition in his Q1 (and again in his "Wald-Iyer formalism" aside) that the prograde-vs-retrograde capture-cross-section asymmetry for hyperbolic encounter scales as `O((χ v/c)²) ≈ 10⁻⁷` at v=200 km/s. That is wrong by ~3 orders of magnitude. The asymmetry is *linear* in χv/c at first order in slow-rotation perturbation theory, because the leading frame-dragging coupling enters the orbital-effective potential as a *χ·L* term (linear in spin × linear in angular momentum), not as χ². Substitution chain:

```
Definition:    For Kerr at small χ, the radial effective potential receives a
              correction ΔV_eff = -2 χ G²M²/(c³ r³) · L_z + O(χ²)
              (Bardeen-Press-Teukolsky 1972; the "frame-dragging tilt" term).
              For a hyperbolic geodesic with impact parameter b and asymptotic
              velocity v, L_z = ±b·v (sign by orbit orientation).
              Asymmetry in capture impact parameter:
                  (b_pro − b_retro) / b_avg ~ χ · v/c
Substitute:    χ = 0.685, v = 2×10⁵ m/s, c = 2.998×10⁸ m/s
              χ v/c = 0.685 · 2×10⁵ / 2.998×10⁸
Simplify:      χ v/c = 4.57×10⁻⁴
Compare:       Hawking's guess (χv/c)² = 2.09×10⁻⁷
              Ratio: linear / quadratic = 4.57×10⁻⁴ / 2.09×10⁻⁷ = 2188
Direction:    The asymmetry is ~2200× LARGER than Hawking's quadratic guess.
              At v=200 km/s the prograde and retrograde Kerr capture
              cross-sections differ at the ~5×10⁻⁴ level — still observationally
              irrelevant (no detector can distinguish two cross-sections that
              close), but the SCALING claim "(χv/c)² and unmeasurable" is
              wrong. The correct claim is "χv/c and still unmeasurable".
```

This matters because the linear scaling has a sign — prograde captures are *enhanced* relative to retrograde, so a population of slowly-encountering Kerr PBHs (all with χ_f=0.685 from equal-mass mergers) would *preferentially* capture matter co-rotating with their spin. Over Hubble time this is a slight but systematic angular-momentum amplification mechanism: dressed-Kerr PBHs in dense regions spin *up* more than they would under symmetric capture. I do not think this matters for the living-room scenario, but it does matter for Hawking's H4 spin-down trajectory — the spin-down rate dχ/dt from Page-radiation needs to be netted against this slow spin-*up* from preferential prograde capture, and at high local densities the latter could compete.

**D2. The equivalence principle DENIES the "self-sourced plasma" back-reaction Hawking gestures at in Re:E5/H6 — with one caveat.** Hawking framed the e⁺e⁻ pair-plasma sheath at M~5×10¹¹ kg as if the PBH might "feel" a Tolman-Oppenheimer-Volkoff-style stress-energy back-reaction reducing its effective horizon area. From the GR side this is mostly wrong. The Mino-Sasaki-Tanaka self-force formalism for a *radiating* point mass on a Schwarzschild background gives identically zero net force at leading order *by spherical symmetry of the emission in the PBH rest frame*. Substitution chain:

```
Definition:    Net Hawking radiation reaction force F_rad = ∮ T^{0i} n̂_i dΣ
              over a sphere just outside the horizon, taken in the
              instantaneously-comoving rest frame of the PBH.
Substitute:    For Schwarzschild progenitor, emission is isotropic in the
              static rest frame. T^{0i} is purely radial outflow with no
              preferred direction.
Simplify:      ∮ T^{0i} n̂_i dΣ = 0 by isotropy.
Direction:    NET self-force on a spherical Hawking emitter is ZERO by
              spherical symmetry. The PBH does NOT 'feel' its own pair plasma
              as a back-reaction force. The plasma's stress-energy curves the
              spacetime around the PBH, but the PBH sits at the symmetry
              center of that curvature — equivalence principle says the
              center of a spherically symmetric configuration experiences no
              net acceleration from it.
```

This is the strict GR answer. The horizon does NOT shrink in response to the plasma it sources. The spacetime *outside* the horizon has slightly more stress-energy than vacuum, but the geometry of the horizon itself is set by the global mass-energy budget (M_PBH plus the trapped portion of the plasma if any falls back), and that budget is what the area-theorem operates on.

**Caveat (where the QFT-side framing gets a foothold).** The above is leading-order. At second order, two effects break exact spherical symmetry: (i) for Kerr remnant (χ_f=0.685) the emission has azimuthal-mode preference (superradiant amplification of m>0 modes), so the rotating Hawking flux carries a *net* angular-momentum flux — but linear-momentum flux is still zero by axial symmetry. (ii) For inhomogeneous external matter density (the PBH approaches Earth's surface, then transits non-isotropic stratification), the back-reaction is non-vanishing because the *external* spherical symmetry is broken, not the emission. Both effects are tiny — second-order in the relevant small parameter. Hawking's Q3 framing implicitly merged these into "the PBH feels its plasma," which conflates intrinsic (self-force, zero) with extrinsic (gradient-coupling, second-order). I dissent: **at the equivalence-principle level, a PBH is rigorously indifferent to its own Hawking gas in vacuum**, and only the matter gradients of the *environment* produce coupling.

**D3. The 5% GW radiation budget is far below the area-theorem upper bound — there IS GR-side room for transient leakage during ringdown.** Hawking's Re:E4 took the NR-calibrated ε_GW = 5% as definitive and his Q4 closed with "or whether 5% is a hard upper bound from cosmic censorship." The area theorem gives a much weaker upper bound. Substitution chain:

```
Definition:    Area theorem requires A_f ≥ A_1 + A_2.
              A_Kerr = 8π (G M_f/c²)² (1 + √(1−χ²))
              A_progenitor (×2) = 2 · 4π (2 G m/c²)² = 32π (Gm/c²)²
Substitute:    A_f ≥ A_i  ⇒  (M_f/m)² · (1 + √(1−χ_f²)) ≥ 4
              ⇒  M_f / m  ≥  2 / √(1 + √(1−χ_f²))
              For χ_f = 0.685: √(1−χ_f²) = 0.728, 1 + s = 1.728
              M_f_min / m ≥ 2 / √1.728 = 1.521
              ε_GW_max = 1 − M_f_min/(2m) = 1 − 0.760 = 0.240
Simplify:      Area-theorem maximum ε_GW at χ_f = 0.685 is 24.0%.
              Schwarzschild limit (χ_f = 0): ε_GW_max = (2 − √2)/2 = 29.3%
Direction:    The NR-calibrated 5% is FAR below the area-theorem ceiling 24%.
              The ratio is 4.8x — there is a factor-of-five GR-side gap between
              "what the area theorem permits" and "what numerical relativity
              actually radiates."
```

What does this gap mean? It means **GR alone does not lock the radiation budget to 5%** — that number comes from the specific *dynamics* of the post-Newtonian-to-merger waveform, not from any fundamental theorem. In principle, exotic mergers that violate the standard quasi-circular inspiral assumption (head-on collisions, hyperbolic encounters, eccentric near-plunges) can radiate *more* than 5%, up to the 24% area ceiling, without violating any GR theorem. Hawking's Q4 worried about whether ε > 5% could "escape via direct horizon-side leakage during the transient ringdown window" — the area-theorem answer is **yes, in principle, up to ε ≤ 24%**, although for the symmetric-capture geometry of two equal-mass, non-spinning, quasi-circular-inspiral progenitors, the NR calibration is reliable and 5% is what actually happens. **The transient horizon dynamics during the brief common-apparent-horizon-formation window do not violate GR if they leak more energy; they would just push the merger toward the upper-rim of the area-theorem cone.** This is a real GR-side caveat that Hawking's "5% is a hard upper bound from cosmic censorship" reading missed: cosmic censorship + area theorem together cap ε at 24%, not at 5%. The 5% is a dynamical observation, not a theorem.

### EMERGENCE — New insights from the cross-pollination

Three findings that neither agent had alone in R1 — each requires the GR + QFT-in-CST combination to surface.

**E-EMERGE-1. The orbital-decay paradox: BHL drag inverts the "permanent binary" conclusion of E3 by sixteen orders of magnitude.** My E3 said two PBHs at meter-scale separation orbit forever (Peters τ_GW = 2.5×10²¹ yr). Hawking's H2 showed BHL accretion is overwhelmingly dominant in air (Ṁ_BHL = 2.5×10⁻⁵ kg/s at v=30 km/s). Combine these for the *orbiting binary in a living room*: the orbital velocity at meter separation is v_orb ≈ 58 m/s (Hawking H3, sub-sonic — slower than air sound speed c_s = 343 m/s), so the BHL formula uses (c_s² + v²)^{3/2} ≈ c_s³, *not* v³. Substitution chain:

```
Definition:    Ṁ_BHL = 4π (G M)² ρ_air / (c_s² + v_orb²)^{3/2}
              F_drag = Ṁ_BHL · v_orb   (momentum balance for symmetric flow)
              τ_drag = |E_orb| / (F_drag · v_orb)   (energy-loss inspiral time)
              E_orb = − G m₁ m₂ / (2 a) = − G M² / (2 a)
Substitute:    M = 10^14 kg, a = 1 m, ρ_air = 1.2 kg/m³, v_orb = 58 m/s, c_s = 343 m/s
              (G M)² = 4.45×10⁷ m⁶ s⁻⁴
              (c_s² + v_orb²)^{3/2} = (343² + 58²)^{3/2} = (1.21×10⁵)^{3/2} ≈ 4.20×10⁷
              Ṁ_BHL = 4π · 4.45×10⁷ · 1.2 / 4.20×10⁷ = 16.0 kg/s
              F_drag = 16.0 · 58 = 925 N
              E_orb = − 6.674×10⁻¹¹ · 10²⁸ / 2 = − 3.34×10¹⁷ J
              τ_drag = 3.34×10¹⁷ / (925 · 58) = 6.22×10¹² s
Simplify:      τ_drag ≈ 1.97×10⁵ years   (verified Python)
Compare:       τ_GW (Peters) = 2.5×10²¹ yr
              τ_GW / τ_drag = 1.27×10¹⁶
Direction:    BHL air-drag drives the meter-orbit to merger 1.27×10¹⁶ × FASTER than
              gravitational radiation. Two PBHs that 'happen to bind' at meter scale
              in a living room merge in ~200,000 years, NOT in ~10²¹ years.
```

This is the cross-pollination result. My E3 conclusion ("they are practically a permanent binary at the living-room scale") was correct only in vacuum. Once Hawking's H2 atmospheric BHL channel is bolted on, **the binary inspiral timescale collapses by sixteen orders of magnitude** because air, not gravitational radiation, is the dominant dissipation mechanism. The ~360,000-year channel-balance crossover Hawking flagged in H5 is *exactly the same physics*: BHL deposits enough energy/momentum to drive observable consequences on geological-but-sub-Hubble timescales. The "permanent binary" conclusion holds only for hypothetical PBHs orbiting in deep ISM (ρ < 10⁻⁶ kg/m³); in a planetary atmosphere, the binary lifetime is comparable to the channel-balance timescale Hawking already identified.

**Hawking-thrust correction (small but ordered):** the merger product is Kerr (χ_f = 0.685), and Page-radiation has azimuthal preference for m>0 modes. The net thrust from this asymmetry, crudely, is `F_thrust ~ χ · P/c ≈ 0.685 · 9870 / 2.998×10⁸ ≈ 2.3×10⁻⁵ N`. Acceleration on the ~2×10¹⁴ kg merger product is `~10⁻¹⁹ m/s²` — utterly dwarfed by the 925 N BHL drag (giving `a ~ 5×10⁻¹² m/s²`). **Direction**: thrust is 7 OOM below drag for an Earth-bound Kerr PBH; the orbital evolution is BHL-dominated end to end. Tidal coupling to Earth's interior (M_PBH/M_⊕ = 1.7×10⁻¹¹) is similarly negligible: Earth's tidal deformation under the PBH binary's quadrupole moment is sub-microscopic and contributes essentially zero to the orbital decay. **Net cross-domain answer to "how does the bound binary evolve in the living room"**: BHL-drag inspiral on a 200,000-year timescale; thrust and tides contribute corrections at the 10⁻¹⁰ level.

**E-EMERGE-2. The BHL Bondi cylinder is the visible diagnostic — and it appears at sea-level density.** My E6 said the PBH "tunnels through bulk matter on a geodesic" because the horizon (148 fm) is sub-atomic. Hawking's H2 said BHL accretion is dominant in any terrestrial environment. *Both are right* — they describe different geometric scales. Reconciliation:

```
Definition:    The PBH has THREE concentric cross-sections relevant to its passage
              through matter:
              (i)   r_s ≈ 148 fm  (horizon, mechanical-contact for direct nuclei)
              (ii)  r_B ≈ 30 μm   (Bondi radius for atmospheric capture, v=30km/s)
              (iii) r_tidal ≈ 0.37 m (tidal-disruption radius for bone/rock)

The wake structure during transit through air (sea-level ρ = 1.2 kg/m³, v = 30 km/s):
              Inside r_s:           direct horizon-swallow of any nucleus that strays here
                                    (probability per nucleus per second is set by Ṁ_BHL ∝ r_B², not r_s)
              Inside r_B (~30 μm):  air molecules are gravitationally bound to the PBH;
                                    drift inward, eventually crossing horizon. RATE: 2.5×10⁻⁵ kg/s.
                                    At 100-keV gamma flux F = 35.6 kW / (4π r_B²) at r_B
                                    ≈ 35.6 kW / (1.13×10⁻⁸ m²) = 3.15×10¹² W/m²
                                    — accreting air is ionized BEFORE it crosses horizon.
              Inside r_tidal (~0.37 m): bone/wood/rock fail in tidal stretch.
              Outside r_tidal:      gamma flux dominates (Compton mean free path ~5 cm in solids,
                                    a few meters in air).
```

**The Bondi cylinder visibility threshold.** Air ionized inside the Bondi sphere recombines on a Compton/atomic timescale, emitting recombination radiation. Substitution chain for whether this is visible:

```
Definition:    Recombination luminosity per unit length of the Bondi-cylinder wake:
              dL_rec / dx ≈ Ṁ_BHL · (kT_H · f_ionization) / m_air
              with f_ionization ≈ 1 (every accreted atom is ionized by the local 100-keV flux),
              kT_H = 106 keV, m_air ≈ 4.8×10⁻²⁶ kg
Substitute:    Ṁ_BHL = 2.5×10⁻⁵ kg/s,
              kT_H · f / m_air = 1.7×10⁻¹⁴ J / 4.8×10⁻²⁶ kg = 3.5×10¹¹ J/kg
              dL_rec/dx ≈ 2.5×10⁻⁵ · 3.5×10¹¹ = 8.75×10⁶ W per (kg/s of air)
              But Ṁ_BHL is total kg/s entering the Bondi sphere, not per length;
              for a moving source with v = 3×10⁴ m/s, the Bondi-sphere encounter time
              of a single air parcel is ~r_B / v_orb ≈ 30 μm / 30 km/s ≈ 10⁻⁹ s.
              The wake cylinder has length L_wake ~ v · τ_radiative ~ 30 km/s · ms ~ 30 m
Simplify:      Power per meter of wake ≈ 35.6 kW / 30 m ≈ 1.2 kW/m at a few-meters offset
Direction:    The Bondi cylinder is VISIBLE as a faint glowing thread of length ~10s of m
              along the trajectory, with linear surface brightness comparable to a household
              light bulb per meter — but in soft X-ray and UV from recombination, not visible.
              The thermal Hawking flux dominates by ~30× over recombination at meter range.
```

So the operational diagnostic is: **the PBH leaves a faint UV/X-ray glow tube ~30 m long centered on its trajectory through air, set by the Bondi-Hoyle accreted-then-ionized matter's recombination radiation**. This is the "Hawking-channel diagnostic" that distinguishes a PBH transit from any conventional impactor. A meteorite leaves a hot thermal wake (visible, optical, decaying on second timescales). A PBH leaves a quasi-permanent (lifetime = local Hawking-irradiated-air recombination time, ~ms) UV/X-ray glow column. *No* conventional astrophysical event reproduces that signature. If one were to ever *see* a 10^14 kg PBH transit, the Bondi cylinder is the observational handle.

**E-EMERGE-3. The cosmological-happenstance bound is astronomically loose — but it exists.** If 10^14 kg PBHs constitute 100% of dark matter, the local number density is `n_PBH = ρ_DM,local / M_PBH ≈ 6.4×10⁻²² / 10^14 ≈ 6.4×10⁻³⁶ m⁻³` (verified Python), giving a mean inter-PBH spacing of `(1/n)^{1/3} ≈ 5.4×10¹¹ m ≈ 3.6 AU`. PBHs are *sparse* — the nearest one to you, on average, is at the orbit of the asteroid belt. Substitution chain for the rate at which a single PBH passes within 1 m of you:

```
Definition:    Rate per unit time of PBH passage within impact parameter b of a fixed observer:
              Γ_pass(b) = n_PBH · π b² · v_halo
Substitute:    n_PBH = 6.4×10⁻³⁶ m⁻³, b = 1 m, v_halo = 2.2×10⁵ m/s
              Γ_pass(1m) = 6.4×10⁻³⁶ · π · 1² · 2.2×10⁵ = 4.42×10⁻³⁰ s⁻¹
Simplify:      Mean time between 1-m grazing encounters: 1 / 4.42×10⁻³⁰ s ≈ 2.26×10²⁹ s
                                                       ≈ 7.15×10²¹ yr   (verified Python)
Compare:       t_Hubble ≈ 1.4×10¹⁰ yr
              τ / t_Hubble = 5.1×10¹¹
Direction:     A single PBH passes within 1 m of any given observer once per ~5×10¹¹
              Hubble times. Across the entire Earth's surface (4πR_⊕² = 5.1×10¹⁴ m²)
              and 4.5 Gyr of Earth's history, the expected number of in-Earth-volume
              PBH passes is N ~ n_PBH · π R_⊕² · v · t · (chord factor) ~ 10⁻⁵ ·
              consistent with 'never happened' (zero events) at low confidence.
```

For *two* PBHs to *both* be in your living room *simultaneously* (the workshop premise), the joint probability is the square of the single-PBH-in-room probability times a coincidence-window factor. Using room volume ~30 m³ and human residency τ_user ~ 10⁹ s lifetime, a single PBH's expected time in the room over a lifetime is `Γ_pass(b~3m) · τ_user ~ 4×10⁻²⁹ · 10⁹ ~ 4×10⁻²⁰`. **Two PBHs simultaneously: probability ~ (4×10⁻²⁰)² = 1.6×10⁻³⁹** per lifetime — astronomically improbable. The "happenstance collision in the living room" is a Δ-function event with vanishing measure if PBHs constitute all of DM. **Direction**: the non-observation of any such event over Earth's history is consistent with 100% PBH-DM at this mass; the bound the non-observation places on the abundance is at the 10⁻³⁵ level — utterly toothless. The cosmological constraint from "no PBH-PBH collision in any living room ever" is uninformative because the expected rate is far below detection regardless of f_DM. **The asteroid-mass DM window is unconstrained from this side — Hawking's H1 conclusion holds, and no living-room non-observation tightens it.**

### Answers to Hawking's Questions

**Q1 — Kerr cross-section asymmetry for hyperbolic capture.** Your intuition that the prograde-vs-retrograde asymmetry is `O((χv/c)²) ≈ 10⁻⁷` is wrong by ~3 orders of magnitude (see D1 above for the full derivation). The correct scaling at first order in slow-rotation perturbation theory is **linear in χv/c**, because the Bardeen-Press-Teukolsky frame-dragging correction to the radial effective potential enters as `−2 χ G²M²/(c³ r³) · L_z`, linear in spin and linear in orbital angular momentum. Substituting χ_f = 0.685, v = 200 km/s gives χv/c = 4.57×10⁻⁴, which is 2188× larger than your (χv/c)² guess.

The asymmetry is signed — prograde captures are *enhanced* over retrograde by the linear χv/c term. So a population of dressed-Kerr merger remnants in dense regions captures matter preferentially co-rotating with the spin, slowly amplifying χ via accretion *while* Page-radiation is trying to spin it down. At the v=200 km/s halo virial speed the asymmetry is unmeasurable observationally (no detector resolves cross-sections at the 5×10⁻⁴ level for a 2.4×10⁻¹⁹ m² target), but the structural answer is *not* "(χv/c)² and washed out" — it is "χv/c, structurally non-zero, observationally washed out". Your Wald-Iyer-formalism intuition was off by the spin's first power.

**Q2 — GW bremsstrahlung memory from atmospheric drag.** Your dimensional estimate `f_brems ~ a_DF / (2π v) ~ 10⁻²⁵ Hz` is correct for the *spectral peak* of the bremsstrahlung continuum, and yes this is sub-cosmological. The deeper question — does the asymmetric-matter-accretion-mediated drag produce a non-trivial *gravitational memory effect* (Christodoulou-Zel'dovich step) at null infinity — has a clean GR-side answer: **the memory term vanishes for symmetric straight-line motion through bulk matter, but is non-zero whenever the drag has a transverse component**. Substitution chain:

```
Definition:    Christodoulou memory Δh^TT_ij ∝ ∫ T^{TT}_{ij}(retarded) dt    (Bondi-Sachs flux)
              For a point mass moving on a straight line through homogeneous medium,
              the stress-energy tensor of the dragging matter has zero TT-projected
              quadrupole moment in the rest frame perpendicular to motion.
Substitute:    Earth's atmosphere is NOT homogeneous: ρ(z) = ρ_0 exp(−z/H), H=8.4 km
              The PBH at v = 30 km/s passing through the atmospheric scale height
              experiences a drag that varies along the trajectory:
                  F_drag(z) = (4π G² M² / v²) · ρ_0 exp(−z/H)
              This produces a non-zero d³Q/dt³ from the gradient term, hence non-zero
              quadrupole radiation rate AT bremsstrahlung-peak frequency.
              Memory step: Δh ~ G/(c⁴ D) · ΔE_radial_kinetic_during_traversal
                        ~ G/(c⁴ D) · (F_drag · L_atm) ~ G/(c⁴ D) · 1 J × geometric factors
Simplify:      For D = 10 m (in the room) and ΔE_atm-deposit ~ E_frag-air ~ 10⁷ J:
              Δh_memory ~ 6.674×10⁻¹¹ · 10⁷ / ((3×10⁸)⁴ · 10) ~ 8×10⁻⁴¹
Direction:    The memory term EXISTS (the symmetry of straight-line motion does NOT
              wash it out, because atmospheric stratification breaks translational
              symmetry along the trajectory), but its amplitude is ~10⁻⁴¹ at meter
              range and ~10⁻⁵⁰ at any astrophysical baseline — undetectable by 25+
              orders of magnitude.
```

So the geodesic treatment in E5/E6 implicitly assumed translation symmetry along the trajectory, which is broken by Earth's stratified atmosphere; a non-zero memory step does survive at null infinity, but at amplitude ~10⁻⁵⁰ it is decisively beyond any observational reach.

**Q3 — Equivalence principle status of self-sourced e⁺e⁻ plasma.** This is the question I dissented on in D2 above. The strict equivalence-principle answer is: **at leading order, the PBH does not feel its own Hawking gas as a self-force**, because the emission is spherically symmetric in the PBH's instantaneously-comoving rest frame, and `∮ T^{0i} n̂_i dΣ = 0` by isotropy. The Mino-Sasaki-Tanaka self-force formalism applies to a point mass with non-spherically-symmetric coupling to a background field; spherically symmetric Hawking emission (Schwarzschild progenitor) gives no leading-order back-reaction term.

The Tolman-Oppenheimer-Volkoff intuition you flagged would apply if the plasma were *static* and surrounded the PBH as a self-gravitating envelope — then the integrated stress-energy outside the horizon would feed back into the global Schwarzschild mass parameter, and the horizon would respond to the *combined* (PBH + plasma) mass. But the Hawking plasma is not static: it is an outgoing flux, and at any given moment the energy carried by the plasma outside r_s is small (P · r_s/c² ≈ 35.6 kW · 5×10⁻²² s/c² ≈ 2×10⁻³⁵ kg, completely negligible relative to M = 10¹⁴ kg). So the time-averaged TOV-like back-reaction is also vanishing.

**The clean answer to your "self-force formalism applies cleanly" question**: *yes, it applies cleanly, and it gives zero*. The non-trivial physics (azimuthal m-mode preference for Kerr, gradient coupling to inhomogeneous environment) enters at second order and is set by the *external* breaking of symmetry, not by the self-sourced plasma. The PBH is rigorously indifferent to its own emission *in vacuum*; Hawking radiation is not a "self-force" channel.

**Q4 — Transient horizon dynamics during ringdown.** Your worry was whether ε > 5% can escape "via direct horizon-side leakage during the transient ringdown window" before being locked by the new horizon. The GR-side answer (D3 above) is: **yes, in principle, up to ε ≤ 24% set by the area theorem at χ_f = 0.685**. There is no GR theorem locking ε to 5%. Substitution chain:

```
Definition:    Area theorem: A_f ≥ A_i (sum of progenitor areas)
              (M_f/m)² (1 + √(1−χ_f²)) ≥ 4
Substitute:    χ_f = 0.685
              M_f/m ≥ 2/√1.728 = 1.521
              ε_GW_max = 1 − M_f/(2m) = 1 − 0.760 = 0.240
Simplify:      Area theorem permits up to 24.0% radiation; NR observes 5%
Direction:     5% / 24% = 21% — the NR-calibrated value uses only one-fifth of
              the area-theorem budget. There IS a 19-percentage-point GR-side
              window within which exotic dynamics could in principle leak more.
```

For the equal-mass non-spinning quasi-circular merger you and I are discussing, the standard NR calibration (SXS, NINJA, Lazarus) is reliable and ε is robustly 5%. But for hyperbolic encounters, head-on collisions, or near-extremal initial spins, ε can exceed 5%. Cosmic censorship combined with the area theorem caps ε at the 24% I quoted, not at 5%. **Your phrasing "5% is a hard upper bound from cosmic censorship" is the part I disagree with**: cosmic censorship caps the *final* spin at χ ≤ 1, which forces M_f ≥ 2m/√2 = 1.414 m, giving ε_max = (2−√2)/2 = 29.3% (the Schwarzschild-final limit). The 24% is the more restrictive bound for the specific χ_f the ringdown lands at, and the 5% is dynamical, not theorematic.

For your specific question about the brief (~few light-crossing-times) common-apparent-horizon-formation window: this is the era when there is no single global event horizon, only a family of trapped surfaces. During this transient there is no theorem that forbids energy transport across the (still-forming) horizon boundary. The actual energy flow is dictated by NR; numerically, it stays at ~5%. But the *bound* is 24%, and that bound is GR-side, not QFT-side.

**Q5 — Coriolis deflection on antipodal exit.** Your formula `½ Ω v τ²` is incorrect by a factor of 2. The correct ballistic Coriolis deflection for a chord-traversal at constant v with Ω perpendicular to the chord is `Ω v τ²` (no 1/2). Substitution chain:

```
Definition:    Lateral acceleration: a_⊥(t) = 2 (Ω × v)_⊥ = 2 Ω v   (for Ω ⊥ v)
              Lateral velocity at time t: v_⊥(t) = ∫_0^t a_⊥ dt' = 2 Ω v t
              Lateral displacement at time τ: x_⊥(τ) = ∫_0^τ v_⊥ dt = ∫_0^τ 2 Ω v t dt = Ω v τ²
Substitute:    Ω = 7.27×10⁻⁵ rad/s, v = 3×10⁴ m/s, τ = 425 s
              x_⊥ = 7.27×10⁻⁵ · 3×10⁴ · 425²
              x_⊥ = 2.18 · 1.806×10⁵ = 3.94×10⁵ m
Simplify:      x_⊥ ≈ 394 km   (verified Python)
Compare:       Hawking's "1/2 Ω v τ² ≈ 200 km" is a factor of 2 too small
              The correct deflection is ~394 km, not 200 km.
Direction:     The exit point is ~394 km East (or West, depending on chord orientation
              and hemisphere) of the geometric antipode, not 200 km. Your factor of 1/2
              would only apply to the lateral velocity, not the displacement.
```

This is a Newtonian-Coriolis-only correction; the chord traversal also speeds up to ~32 km/s at center (gain ~11 km/s), so the time-averaged speed is slightly higher than 30 km/s and the deflection is somewhat larger still — call it ~410 km after the speed correction. The Lense-Thirring frame-dragging contribution is, by independent substitution:

```
Definition:    Ω_LT(r) = 2 G J_⊕ / (c² r³)
Substitute:    J_⊕ = 7.07×10³³ J·s, r = R_⊕ = 6.4×10⁶ m
              Ω_LT = 2 · 6.674×10⁻¹¹ · 7.07×10³³ / ((2.998×10⁸)² · (6.4×10⁶)³)
              Ω_LT = 4.0×10⁻¹⁴ rad/s
Compare:       Ω_LT / Ω_⊕ = 4.0×10⁻¹⁴ / 7.27×10⁻⁵ = 5.5×10⁻¹⁰
Direction:     Lense-Thirring is 9.3 orders of magnitude SMALLER than Newtonian Coriolis.
              The frame-dragging contribution to the antipodal deflection is ~0.2 mm,
              utterly buried under the 400-km Coriolis deflection.
```

So no, the rotating-Earth metric does not produce an "inward-spiraling geodesic exiting at a different latitude" at any observable level. The deflection is essentially pure Newtonian Coriolis at ~400 km East/West (not 200 km), Lense-Thirring contributes a sub-millimeter correction. **The exit crater is ~400 km from the geometric antipode**, in the direction set by the chord-orientation × Earth-rotation cross-product.

**Q6 — Stochastic GW background from cosmological PBH binary mergers.** Your guess of "10 OOM short of detection" at M = 10¹⁴ kg badly underestimates the gap. The strain amplitude from a single PBH-PBH inspiral at the chirp mass M_chirp = m · 2⁻¹/⁵ ≈ 0.87×10¹⁴ kg, observed at fiducial distance D = 10 Mpc and frequency f = 100 Hz (LIGO band):

```
Definition:    h_inspiral(f, D) = (4/D) · (G M_chirp / c³)^{5/3} · (π f)^{2/3} · c
                                ≈ G^{5/3} M_chirp^{5/3} (π f)^{2/3} / (c^4 D)   (single-source post-Newtonian peak)
Substitute:    M_chirp = 0.87×10¹⁴ kg, f = 100 Hz, D = 3×10²³ m, G = 6.674×10⁻¹¹, c = 2.998×10⁸
              h_inspiral ≈ (6.674×10⁻¹¹)^{5/3} · (0.87×10¹⁴)^{5/3} · (π·100)^{2/3} / ((3×10⁸)⁴ · 3×10²³)
Numerics:      h ≈ 3.58×10⁻⁵⁰   (verified Python)
Compare:       LIGO design sensitivity at 100 Hz: h_min ≈ 10⁻²³
              Ratio: h_PBH / h_LIGO = 3.58×10⁻⁵⁰ / 10⁻²³ = 3.58×10⁻²⁷
Direction:     Single PBH-PBH inspiral source at 10 Mpc is ~27 orders of magnitude
              BELOW LIGO sensitivity, not 10 OOM. Your guess was off by 17 OOM.
```

The mass-scaling `h ∝ M^{5/6}` you cited gives `h_PBH/h_solar = (10¹⁴/2×10³⁰)^{5/6} = 2.6×10⁻¹⁴`; combined with a solar-binary baseline `h_solar ~ 10⁻²¹` at LIGO range, the predicted PBH strain is ~10⁻³⁵ — still ~12 OOM below LIGO. The 27-OOM number above is the more careful explicit calculation for the chirp-mass-scaled inspiral spectrum. **Either way, the stochastic-background detectability is far worse than 10 OOM short.**

For the *integrated stochastic background* `Ω_GW(f)`, the relevant question is the merger rate, which depends on the binary fraction f_bin. Using your `f_bin = 10⁻⁶` and n_PBH = 6.4×10⁻³⁶ m⁻³, the cosmological merger rate per unit comoving volume is roughly `R ~ f_bin n_PBH / τ_merge_typical ~ 10⁻⁴² / τ` per m³ per s. For τ = 10⁹ yr = 3×10¹⁶ s, R ~ 3×10⁻⁵⁹ Hz/m³ — vanishingly small. The resulting `Ω_GW` is ~`R · E_GW/(ρ_crit)` ~ `3×10⁻⁵⁹ · 9×10²⁹ / (8.5×10⁻¹⁰) ~ 3×10⁻²⁰` per logarithmic frequency interval, which sits ~10 OOM below current Pulsar Timing Array sensitivity (Ω_GW > 10⁻¹⁰) and ~5 OOM below proposed LISA sensitivity.

**Direction**: stochastic GW background from 10¹⁴ kg PBH-PBH mergers is **far below any current or proposed detector** — by 10-15 OOM in Ω_GW for cosmological-binary populations, by 27 OOM in single-source strain for individual events. **The PBH-DM 10¹⁴ kg window is GW-silent at every frequency**, confirming and sharpening your initial guess: it is far worse than "10 OOM short". If 10¹⁴ kg PBHs make up all of dark matter, GW astronomy will *never* see them as a population — the only viable detection channel is the gamma-ray flux from individual evaporators near the cliff at M ~ 10¹¹ kg, exactly as your bonus Q6 to me framed it.

---

## Round 2 — Hawking (Final Round + Verdict)

### CONVERGENCE — Where Hawking accepts Einstein's corrections

I concede on five points. Three are numerical-precision corrections; two are structural inversions of a position I held in R1.

**HC1. The Kerr capture asymmetry is LINEAR, not quadratic in χv/c (Re: D1).** My Q1 to Einstein flagged the asymmetry as `O((χv/c)²) ≈ 10⁻⁷` from "Wald-Iyer-formalism" intuition. Einstein's D1 is correct: the leading correction comes from Bardeen-Press-Teukolsky's frame-dragging tilt term `−2 χ G²M²/(c³ r³) · L_z` in the radial effective potential, which is *linear* in spin × angular momentum. Substitution chain:

```
Definition:    Asymmetry index A ≡ (b_pro − b_retro)/b_avg
              From the BPT effective potential at first order in slow-rotation:
              A_linear = χ · v/c   (leading frame-dragging contribution)
              A_quadratic = (χ v/c)²   (my R1 guess; sub-leading)
Substitute:    χ = 0.685, v = 2×10⁵ m/s, c = 2.998×10⁸ m/s
Numerics:      A_linear = 0.685 × 2×10⁵ / 2.998×10⁸ = 4.57×10⁻⁴
              A_quadratic = (4.57×10⁻⁴)² = 2.09×10⁻⁷
              Ratio: A_linear / A_quadratic = 2188 (verified Python)
Direction:    The actual asymmetry exceeds my R1 quadratic guess by 2188×.
              At v=200 km/s, the prograde-vs-retrograde Kerr capture cross-
              section differs at the ~5×10⁻⁴ level — still observationally
              inaccessible (the cross-section itself is ~10⁻¹⁹ m² for the
              relevant impact parameter), but my SCALING claim was wrong.
```

The signed direction is the physically interesting consequence: a population of dressed-Kerr remnants (χ_f = 0.685 from equal-mass mergers) preferentially captures co-rotating matter, slowly amplifying spin via accretion *while* Page-radiation tries to spin them down. Whether the net dχ/dt is positive or negative depends on the local mass density. For PBHs in deep ISM (n ≪ ρ_crit ≈ 5.7×10⁻⁶ kg/m³ from H2), Page-spin-down dominates; for PBHs in dense regions (atmosphere, water, rock), this prograde-bias spin-up could compete with or exceed Page spin-down. I had not noticed this competition in R1 because I had the asymmetry exponent wrong.

**HC2. The Coriolis displacement is `Ω v τ²`, not `½ Ω v τ²` (Re: D2/Q5).** My antipodal-exit calculation in Q5 carried a stray factor of ½ in the displacement formula. Einstein's D2 substitution chain corrects it: the `½` is the right factor for the *velocity* `v_⊥(τ) = ½ · 2Ωv · τ` after a single integration, but the *displacement* requires a second integration `x_⊥(τ) = ∫₀^τ v_⊥ dt = Ωvτ²` with no leading ½. Re-derive:

```
Definition:    a_⊥(t) = 2 (Ω × v)_⊥ = 2 Ω v   (Coriolis acceleration, Ω ⊥ v)
              v_⊥(t) = ∫₀^t a_⊥ dt' = 2 Ω v t
              x_⊥(τ) = ∫₀^τ v_⊥(t) dt = ∫₀^τ 2 Ω v t dt = Ω v τ²
Substitute:    Ω_⊕ = 7.27×10⁻⁵ rad/s, v = 3×10⁴ m/s, τ_cross = 425 s
Numerics:      x_⊥ = 7.27×10⁻⁵ × 3×10⁴ × (425)²
                  = 2.181 × 1.806×10⁵
                  = 3.94×10⁵ m ≈ 394 km   (verified Python)
Direction:    My R1 quote of "~200 km" was off by exactly factor 2. The exit
              crater is ~394 km from the geometric antipode, not ~200 km.
              The Lense-Thirring contribution Einstein computed (~0.2 mm)
              is buried under this 9 OOM smaller correction. Concede.
```

**HC3. The "self-sourced plasma back-reaction" framing of Q3 was sloppy (Re: D2).** Einstein's D2 is the correct GR-side answer: at leading order, the integrated stress-energy flux through a sphere just outside the horizon, in the PBH's instantaneously-comoving rest frame, vanishes by isotropy:

```
Definition:    F_self = ∮ T^{0i} n̂_i dΣ   (net momentum flux through enclosing sphere)
For Schwarzschild progenitor with isotropic Hawking emission:
              T^{0i} = (energy flux density) · n̂^i (purely radial outward)
              ∮ T^{0i} n̂_i dΣ ∝ ∮ (radial flux)(n̂·n̂) dΣ
                                = (radial flux) · 4π r²
Wait — that gives ∮ (radial energy flux)·1 · dΣ = total power, not zero.
But that's the energy flux, not momentum flux.
The MOMENTUM flux is ∮ T^{0i} n̂_i dΣ where the integrand is T^{0i} dotted into the
inward/outward direction; by symmetry the spatial (vector) integral over a sphere
gives zero net VECTOR momentum because contributions from antipodal points cancel.
Direction:    NET self-force on a spherical Hawking emitter = 0 by parity (n̂ → −n̂
              symmetry of the integrand). The PBH does not "feel" its own emission
              in the sense of a self-acceleration.
```

I retract the TOV-style "back-reaction reduces effective horizon area" framing implied in my Q3. The clean answer is: at leading order, in vacuum, with spherically symmetric emission, the PBH is rigorously indifferent to its own Hawking gas. Spherical-symmetry-breaking corrections (Kerr m-mode preference giving net *angular*-momentum flux without net *linear*-momentum flux; gradient coupling to inhomogeneous external matter) survive at second order, but the leading-order self-force is zero, exactly as Einstein argued.

**HC4. The 5%-vs-24% area-theorem ceiling reading (Re: D3).** I had treated the NR-calibrated ε_GW = 5% as if it were a cosmic-censorship hard upper bound. Einstein's D3 is correct: the area theorem combined with the merger-product spin χ_f = 0.685 gives a maximum radiation efficiency ε_GW_max = 24.0%, of which the standard equal-mass non-spinning quasi-circular merger uses only 5/24 ≈ 21%. Substitution chain:

```
Definition:    Area theorem at merger: A_f ≥ A_1 + A_2
              A_Kerr = 8π (G M_f/c²)² (1 + √(1−χ_f²))
              A_progenitor (×2) = 32π (G m/c²)²
              ⇒ (M_f/m)² (1 + √(1−χ_f²)) ≥ 4
Substitute:    χ_f = 0.685, √(1−χ_f²) = √0.5310 = 0.7287
              1 + √(1−χ_f²) = 1.7287
              M_f/m ≥ 2/√1.7287 = 1.5212
              ε_GW_max = 1 − M_f_min/(2m) = 1 − 0.7606 = 0.2394
Numerics:      ε_GW_max(χ_f=0.685) = 23.9% (verified Python)
Compare:       NR-calibrated ε_GW for equal-mass non-spinning quasi-circular = 4.8 ± 0.5%
              ratio: NR/area-ceiling = 4.8/23.9 = 0.20
Direction:    The standard merger uses only ~20% of the GR-permitted radiation
              budget. The remaining 80% sits in the irreducible-mass increase
              of the Kerr horizon. My R1 framing "5% is a hard upper bound from
              cosmic censorship" was wrong — cosmic censorship caps χ_f ≤ 1,
              which gives ε_GW_max ≤ (2−√2)/2 = 29.3% at the χ_f → 0 limit
              and 23.9% at the dynamically-realized χ_f = 0.685. The 5% is a
              dynamical-NR observation, not a theorem.
```

This matters for exotic-merger geometries (head-on collisions, hyperbolic encounters, near-extremal initial spins) where ε can climb above 5% without violating any GR bound. For the equal-mass non-spinning quasi-circular case at hand, NR is reliable, but the 19-percentage-point gap between dynamical reality and area-theorem ceiling is real and Einstein's D3 nails it.

**HC5 (most consequential). BHL atmospheric drag inverts my "permanent steady-state binary" picture (Re: EMERGE-1).** This is the single most important update from R2. In R1 I described the merger product as a "quasi-permanent Hawking emitter" and accepted Einstein's E3 conclusion that two PBHs at meter separation orbit each other for ~10²¹ years. Einstein's EMERGE-1 substitution chain shows that BHL drag against ambient air at v_orb = 58 m/s drives the binary to merger in ~200,000 yr, sixteen orders of magnitude faster than gravitational radiation:

```
Definition:    τ_drag = |E_orb| / (F_drag · v_orb)
              F_drag = Ṁ_BHL · v_orb,    Ṁ_BHL = 4π(GM)² ρ / (c_s² + v_orb²)^{3/2}
Substitute:    M = 10¹⁴ kg, a = 1 m, ρ_air = 1.2 kg/m³, c_s = 343 m/s, v_orb = 58 m/s
Subsonic regime: v_orb < c_s, so (c_s² + v_orb²)^{3/2} ≈ c_s³ × (1 + v_orb²/c_s²)^{3/2} ≈ 4.20×10⁷
              Ṁ_BHL = 4π × 4.45×10⁷ × 1.2 / 4.20×10⁷ ≈ 16.0 kg/s
              F_drag = 16.0 × 58 ≈ 925 N
              |E_orb| = G M²/(2a) = 6.674×10⁻¹¹ × 10²⁸ / 2 = 3.34×10¹⁷ J
              τ_drag = 3.34×10¹⁷ / (925 × 58) ≈ 1.97×10⁵ yr (verified Python)
Compare:       τ_GW (Peters at a=1 m) = 2.5×10²¹ yr
              τ_GW / τ_drag = 1.27×10¹⁶
Direction:    BHL atmospheric drag drives the binary to merger 1.27×10¹⁶× FASTER
              than Peters GW emission alone. The "permanent binary" picture I
              concurred with in R1 is correct ONLY in vacuum; in atmosphere
              the binary is finite-lived on geological timescales.
```

I update my H4 framing: the merger product is quasi-permanent **once formed** (τ_evap = 1.83×10¹⁹ yr, eternal at every observational scale), but the route from "two free PBHs at meter scale" to "merged remnant" runs through BHL drag, not gravitational radiation. The merger event is delayed by ~10⁵ yr in atmosphere, not ~10²¹ yr. This collapses the relevant timescale chain by sixteen orders of magnitude.



### DISSENT — Sharpened residual disagreements

I push back on three points. Each carries a substitution chain that did not appear in R1.

**HD1. The 200,000-yr BHL inspiral self-saturates as the binary tightens — the timescale is not constant inspiral but transitions through a Bondi-cylinder-overlap regime at a ≈ 5.7 cm.** Einstein's EMERGE-1 computation assumed the BHL formula `Ṁ = 4π(GM)² ρ/(c_s² + v_orb²)^{3/2}` applies independently to each PBH for the full inspiral. That is correct for separations a > r_BHL where the two Bondi spheres are isolated; it fails when the spheres overlap. Substitution chain for the overlap threshold:

```
Definition:    r_BHL ≡ G M / c_s²   (subsonic Bondi radius for v_orb < c_s)
              Bondi spheres overlap when 2 r_BHL ≥ a, i.e. a ≤ 2 G M / c_s²
Substitute:    M = 10¹⁴ kg, c_s = 343 m/s
              r_BHL = 6.674×10⁻¹¹ × 10¹⁴ / (343)² = 6.674×10³ / 1.18×10⁵
                    = 5.67×10⁻² m = 5.67 cm   (verified Python)
              a_overlap = 2 r_BHL ≈ 11.3 cm
Direction:    For a > 11.3 cm the two PBHs accrete from separate Bondi spheres
              (Einstein's formula valid). For a < 11.3 cm the spheres overlap and
              the binary as a whole accretes from a single shared Bondi region.
```

In the cooperative regime (a < 11 cm), the relevant total mass is M_tot = 2M and the formula becomes `Ṁ_total = 4π (G·2M)² ρ/c_s³ = 4 · 4π(GM)²ρ/c_s³`, which is *2× greater* than the sum 2 × 4π(GM)²ρ/c_s³ from separate spheres. Naively this would *accelerate* inspiral. But there is a second transition: at a = r_BHL = 5.67 cm, the orbital velocity equals the sound speed:

```
Definition:    v_orb(a) = √(GM/a)   (Keplerian for equal-mass binary, single-PBH frame)
At a = r_BHL = G M / c_s²:
              v_orb(r_BHL) = √(G M / (G M / c_s²)) = c_s  (verified: gives v=343 m/s)
Substitute:    For a < r_BHL, v_orb > c_s — the binary's relative motion is supersonic
              relative to the gas. The BHL formula switches from c_s³ (subsonic) to
              v_orb³ (supersonic) in the denominator.
              Ṁ_BHL,super = 4π(G M_tot)² ρ / v_orb³ = 4π(2GM)² ρ / (G M / a)^{3/2}
                          ∝ ρ √(M) · a^{3/2}
              F_drag · v_orb = Ṁ · v_orb² ∝ ρ √(M) · a^{1/2}
              dE/dt = − F_drag · v_orb ∝ ρ √(M) · a^{1/2}
              dE/da = G M²/(2a²)
              da/dt = (dE/dt) / (dE/da) ∝ a^{5/2} ρ √M
Direction:    Below the sonic radius, drag GROWS as a → 0 (because v_orb → 0 in
              denominator power v_orb³, but numerator F·v scales as v²/v³ = 1/v),
              so v_orb⁻¹ (per unit ρ). However da/dt scales as a^{5/2}, meaning
              da → 0 as a^{5/2} → 0 SLOWER than linear. The integrated time to
              reach a = 0 from a = r_BHL diverges only logarithmically? No —
              τ_inspiral_supersonic = ∫_0^{r_BHL} da / |da/dt| ∝ ∫_0^{r_BHL} a^{−5/2} da
              which DIVERGES at a → 0. The supersonic regime stalls.
```

In practice, GW emission takes over at small a (Peters τ_GW ∝ a⁴ vanishes faster than supersonic drag stalls), so the binary completes the merger via a hybrid drag-then-GW chain. **The 200,000-yr air-drag inspiral applies only down to a ≈ 5.7 cm, below which dynamics shift; from a = 5.7 cm to merger, the GW and supersonic-drag channels combine over a much shorter additional time** (Python check: τ_GW(a=5.7 cm) ∝ (5.7×10⁻²)⁴ / 1⁴ × τ_GW(1 m) = 1.06×10⁻⁵ × 2.5×10²¹ yr ≈ 2.6×10¹⁶ yr — still huge in vacuum, but supersonic-BHL drag is competitive at the cm scale and merger completes within additional ~10²–10³ yr).

So the "~200,000 yr" headline is correct as a leading-order estimate but is structurally a *transit* timescale through the subsonic-BHL regime, not the full inspiral. The binary spends ~99% of its inspiral time at a > 5.7 cm under c_s³-limited drag, and ~1% at a < 5.7 cm under v_orb-limited dynamics + GW completion. **Direction**: BHL drag does not run all the way to coalescence — it hands off to GW + supersonic accretion at a ≈ 5.7 cm; the total inspiral remains ~200,000 yr to leading order, but the dynamical regime is non-trivially layered.

**HD2. The radiation kill envelope is two-leveled, with a delayed-mortality halo at ~1 km that R1 missed.** Einstein's R1 E2 quoted ~30–100 m as the LD50 radius; my R1 H1 confirmed it. Both treatments assumed acute-dose lethality (5 Sv whole-body in seconds-to-hours) for a stationary observer at fixed range. There is a second mortality level that neither of us bounded. Substitution chain (verified Python):

```
Definition:    Acute LD50: 5 Sv whole-body, lethal within hours-to-days.
              Chronic / stochastic-cancer concern: ≥0.1 Sv cumulative over weeks.
              Convert: dose rate threshold for "lethal in 1 hr" = 5 Sv/hr.
              "Background detectable" = 1 mSv/hr.
              "Stochastic-mortality concern" (CDC reference): 1 Sv/hr cumulative.
              Inverse-square: F(r) = P / (4π r²); dose rate ∝ F.

Substitute: P = 35.6 kW (one PBH), 100-keV gammas, dose-conversion 1 mSv/hr per 3×10⁵ ph/cm²/s:
              Instant-kill (1000 Sv/hr): r ≈ 7.7 m
              Hours-kill (100 Sv/hr): r ≈ 24 m
              Acute-LD50 (1-hr exposure ≥ 5 Sv): r ≈ 109 m
              Chronic-mortality (1 Sv/hr): r ≈ 243 m
              Background-detectable (1 mSv/hr): r ≈ 7.7 km
Direction:    The "30–100 m LD50" range we both quoted in R1 captures only the
              acute-kill level. A second level — chronic mortality from stochastic
              cancer risk for survivors who escape the inner zone but linger nearby —
              extends to ~240 m. And the gamma flux is detectable above background
              out to ~7.7 km, meaning the entire neighborhood logs measurable
              exposure during the encounter.
```

Add the mean-free-path correction Einstein omitted: 100-keV gammas have attenuation length ~5.9 cm in soft tissue (from NIST XCOM tables, mu/rho = 0.17 cm²/g, density 1 g/cm³). Half-thickness ~4.1 cm. Substitution: an unshielded human at r = 24 m absorbs 100 Sv/hr in the first ~6 cm of dorsal/ventral tissue, with deeper tissue receiving exponentially less dose. The first 50 cm (most of a torso) absorbs > 99% of incident photons; deep-organ dose is dominated by the surface-layer absorption + secondary X-ray + Compton-electron showers. For an observer who *survives* the encounter (escapes within seconds-to-minutes from a point > 100 m away), the dominant late-time mortality is delayed cancer from stochastic dose accumulated during egress. **Direction**: refined kill envelope has three levels — instant (r < 8 m), acute (r < 100 m), stochastic-late (r < 250 m), with a ~1 km observable-exposure radius for survivors. R1's "30-100 m" was the acute level only.

**HD3. The "happenstance probability 1.6×10⁻³⁹ per lifetime" is artificially deflated by Einstein's f_DM = 1 / no-clustering assumption.** Einstein's EMERGE-3 derivation assumed the local PBH number density is the smooth-halo value `n_PBH = ρ_DM/M_PBH ≈ 6.4×10⁻³⁶ m⁻³`. PBH-formation models with early-universe clustering (e.g. domain-wall-induced PBH formation, peak-theory clustering at z ~ 30, or Poisson-fluctuation-enhanced PBH binaries) predict significant departures from a uniform distribution. Substitution chain for amplification:

```
Definition:    Effective local rate Γ_local = n_PBH(local) · π b² · v
              Clustering enhancement factor: η_cluster = ⟨n²⟩ / ⟨n⟩² ≥ 1
              For a binary fraction f_bin ~ 10⁻⁶ to 10⁻³ in PBH-DM models:
              Γ_binary_collisions = f_bin · n_PBH · σ_collision · v
              with σ_collision = π b² for some b.
Substitute:    For a "happenstance two-PBH-in-room" event:
              η_cluster ≥ 1 (if smooth) or up to 10⁶ if strongly clustered.
              f_bin ~ 10⁻⁶ → 10⁻³.
              Total amplification of Einstein's 1.6×10⁻³⁹: factor of 10⁶ to 10¹².
Direction:    Even with maximal amplification (η_cluster ≈ 10⁶ × f_bin ≈ 10⁻³ ⇒
              factor 10³), the rate is 10⁻³⁶ per lifetime — still astronomically
              improbable. So Einstein's structural conclusion ("toothless cosmological
              constraint") survives, but his quoted exponent is f_DM = 1 / smooth-halo
              specific. With clustering and binary-fraction amplification the rate
              could be 3–9 OOM larger, still vanishing.
```

Even 9 OOM amplification leaves the rate at ~10⁻³⁰ per Earth-history — non-observation still teaches us nothing. But the more honest framing is that the cosmological happenstance bound is `η_cluster × f_bin × Einstein_value`, with all three factors model-dependent. For a robust constraint, one would integrate over PBH-PBH collision rates × DM density profiles × planetary cross-sections across the observable universe, comparing to known supernova/GRB demographic limits — that integration likely lifts the rate to detectable scales for *some* plausible clustering models, but the local "in-your-living-room" event remains beneath any reasonable threshold by ≥ 25 OOM under any model.



### EMERGENCE — New cross-domain insights

Three new findings that surface only when GR + QFT-in-CST are combined.

**HE1. The Bondi-cylinder ionization wake is a distinctive transit signature, not yet ruled out by gamma surveys.** Einstein's EMERGE-2 introduced the wake concept; sharpen its diagnostic spectrum and duty cycle. Substitution chain:

```
Definition:    Wake luminosity L_wake = (Ṁ_BHL / m_air) × E_ionization_per_atom
              with each accreted air molecule absorbing ~kT_H = 106 keV from the local
              Hawking flux before reaching horizon (gamma photoionization is the
              dominant energy-deposition channel inside r_B at 100-keV).
Substitute:    Ṁ_BHL = 2.5×10⁻⁵ kg/s (atmosphere, v=30 km/s),
              m_air ≈ 4.8×10⁻²⁶ kg per molecule,
              E_per_atom ≈ 106 keV × η_abs ≈ 1.7×10⁻¹⁴ J × 0.3 (only ~30% absorbed before infall)
              N_dot_atoms = Ṁ/m_air = 5.2×10²⁰ atoms/s
              L_ionization = 5.2×10²⁰ × 5×10⁻¹⁵ J ≈ 2.6×10⁶ W
              ... but this is bounded above by P_Hawking = 35.6 kW, since the wake
              cannot radiate more than the source emits. Real branching: of the 35.6 kW,
              ~30% is absorbed by the Bondi-trapped gas (the rest escapes as direct
              gamma flux); recombination then re-radiates ~10 kW in a cascade from
              soft X-ray to UV/optical as electrons cascade back to ground states.
Direction:    Wake re-radiation power: ~10 kW spread over the wake length
              L_wake ~ v · τ_recombine ~ 3×10⁴ × 10⁻³ s = 30 m
              Wake linear surface brightness: ~330 W/m at meter offset (UV-soft X-ray)
              Wake spectrum: thermal continuum from recombination cascades, peaks in
              soft X-ray (50-500 eV) with optical/UV tail (recombination lines from
              N, O, Ar, plus continuum free-bound).
```

**Duty cycle and visibility window.** The wake is a *trail*: at any instant, only the volume within a few meters of the PBH's current position is freshly ionized; trailing material recombines on ~ms timescales. For a PBH transiting at 30 km/s, the wake is a 30-m-long luminous tube at any moment, sweeping forward at 30 km/s. To a stationary observer, the tube appears as a brief flash of ~ms duration as it passes overhead — long enough to register on photon-counting instruments, too brief to image with broad-aperture optics.

**Existing-survey constraints.** Could Fermi-LAT, Swift-BAT, Chandra, or ROSAT have detected such a wake from a galactic-disk-density PBH-DM population? Substitution chain:

```
Definition:    Galactic PBH-transit rate through any 1 km² × atmospheric scale-height
              volume ~ n_PBH × σ × v × N_atmosphere
              For Earth: N_atm-volume = 4π R⊕² × H ≈ 4.3×10¹⁵ m³
              Rate per unit area per unit time: n_PBH × v ≈ 6.4×10⁻³⁶ × 2×10⁵
                                              = 1.28×10⁻³⁰ m⁻² s⁻¹
              Annual events over Earth's atmosphere = 4πR⊕² × this × 3×10⁷ s/yr
                                                    = 5.1×10¹⁴ × 1.28×10⁻³⁰ × 3×10⁷
                                                    = 2×10⁻⁸ events/yr
Substitute:    For galactic-disk densities (~100× solar neighborhood), rate ~ 2×10⁻⁶/yr.
Direction:    Even averaging over the full Galactic disk × Hubble time (~10¹⁰ yr),
              expected events ≈ 2×10⁴ flashes per stellar lifetime per system —
              detectable in principle by all-sky survey instruments,
              but the per-Earth rate is so low that NO transit has occurred during
              the modern instrumented era (~50 yr). The non-detection therefore
              imposes weak constraints on f_PBH-DM at the 10¹⁴ kg scale —
              consistent with the asteroid-mass window remaining unconstrained.
              BUT: a detected event would be unmistakable — a 30 m glowing soft-X-ray
              filament moving at 30 km/s with a hard 100-keV gamma core ~10⁹ Sv/hr
              dose-rate-equivalent at meter range. No conventional astrophysical
              process produces that signature.
```

**Predicted observational signature.** A future km²-scale soft-X-ray imager with ms cadence (much beyond current capabilities) would see, at most ~once per millennium per galactic-disk-area, a 30 m × 1 mm filament traversing at 30 km/s, emitting ~10 kW in 50–500 eV photons with simultaneous 100-keV-gamma ~10⁻⁵ W/m² flux at the wake's leading point. This is the cleanest unambiguous PBH-transit signature; existing surveys are 5–7 OOM below the requisite sensitivity.

**HE2. The merger product ends up INSIDE Earth, not floating in atmosphere — and the "200,000 yr" inspiral timescale extends in rock by only 1.2×.** Einstein's EMERGE-1 derived the inspiral timescale assuming the binary remains in atmospheric density. The premise of the workshop is "two PBHs colliding in a living room," which fixes the binary's initial center-of-mass at the user's location with v_CoM ≈ 0 (otherwise it's a flyby, not a collision). Once the binary forms, the CoM falls under Earth's gravity. Substitution chain:

```
Definition:    Free-fall time from living-room ceiling (h = 2.4 m) to floor
              t_fall = √(2h/g) ≈ √(4.8/9.81) ≈ 0.7 s
              Then the CoM enters concrete slab and lithosphere, oscillating
              through Earth on a chord. Half-period for full chord through Earth
              T_chord = π · √(R⊕³/(GM⊕)) ≈ 84 minutes
              Peak v_CoM at center: v_max = √(GM⊕/R⊕) ≈ 7.9 km/s
Substitute:    Drag on supersonic CoM in rock (v_CoM ≈ 7 km/s > c_s_rock = 5 km/s):
              F_CoM_drag = 4π(G·2M)² ρ_rock / v_CoM² ≈ 1.6×10⁷ N
              a_CoM_drag = F/(2M) ≈ 8×10⁻⁸ m/s²
              Stopping time τ_stop = v_max / a ≈ 7000 / 8×10⁻⁸ ≈ 9×10¹⁰ s ≈ 2,800 yr
Direction:    The binary CoM oscillates through Earth ~17,000 times before
              drag-stopping, taking ~2,800 yr. After CoM stops (somewhere
              between center and surface, depending on starting energy), the
              binary continues to inspiral in dense rock medium.
```

For inspiral in rock once the CoM has stopped:

```
Definition:    τ_drag,rock = τ_drag,air × (c_s_rock/c_s_air)³ / (ρ_rock/ρ_air)
Substitute:    (c_s_rock/c_s_air)³ = (5000/343)³ = 3094
              ρ_rock/ρ_air = 3000/1.2 = 2500
              τ_drag,rock / τ_drag,air = 3094/2500 = 1.24
Numerics:      τ_drag,rock = 1.97×10⁵ yr × 1.24 = 2.45×10⁵ yr (verified Python)
Direction:    Inspiral in rock is only ~24% slower than in air —
              the higher density (faster accretion) is offset by the higher sound
              speed (the BHL formula's c_s³ factor wins). Total scenario:
              CoM stops in 2,800 yr; binary merges in additional 245,000 yr;
              merger product is then a 1.9×10¹⁴ kg Kerr remnant somewhere
              inside Earth's mantle/core.
```

The merger product's subsequent fate (geological-timescale BHL-driven sinking through differentiated Earth, with terminal velocity bounded by drag at each density layer): Earth's gravitational gradient at depth pulls the remnant toward the geometric center; BHL drag in the increasingly dense iron core (ρ ≈ 12,000 kg/m³, c_s ≈ 10 km/s) further slows it. Order-of-magnitude estimate of terminal-state position: settled near Earth's center, oscillating with damping over ~10⁵ yr, reaching equilibrium at the geometric center of the inner core. **Direction**: the encounter deposits a permanent 1.9×10¹⁴ kg Kerr black hole into Earth's interior, plus ~245 kyr of co-located soft X-ray glow tracking its gradually-decaying orbit through the mantle and core.

The remnant continues to Hawking-radiate at 9.87 kW (Kerr-cooled from the naive 35.6 kW); over Earth's remaining ~5 Gyr lifetime to red-giant engulfment, this deposits 9.87 × 10³ × 1.6×10¹⁷ s = 1.6×10²¹ J = ~700 Tsar Bombas-worth of internal heat over the planet's lifetime — but spread over 10¹⁰ yr at deep-interior density it is a vanishing perturbation on Earth's natural radiogenic heating (47 TW, integrated 7×10²² J over the same span). Hawking heating from a 10¹⁴ kg PBH inside Earth is 1.4 OOM smaller than radiogenic heat; Earth doesn't notice.

**HE3. Five timescale-decade gaps define five distinct "consequence regimes."** The cross-domain-pinned timescale chain spans 39 orders of magnitude:

| Timescale | Magnitude | Regime |
|:---|:---|:---|
| τ_ringdown (merger transient) | ~10⁻²⁰ s | Quantum — BH no-hair theorem, area-theorem saturation |
| τ_Hawking-photon-emission | ~10⁻²⁰ s | Single thermal emission event |
| τ_recombination_in_wake | ~10⁻³ s | Wake visibility timescale |
| τ_Earth-transit (chord) | ~4×10² s | Mechanical impact regime |
| τ_human_lifetime | ~3×10⁹ s ~ 10² yr | Acute hazard window |
| τ_CoM-stop_in_Earth | ~10¹¹ s ~ 3×10³ yr | Settling regime |
| τ_BHL-merge_in_atmosphere | ~6×10¹² s ~ 2×10⁵ yr | Geological-medium regime |
| τ_BHL-merge_in_rock | ~8×10¹² s ~ 2.5×10⁵ yr | Geological-medium regime |
| τ_galactic-orbit_for_loose-bound_PBH | ~10¹⁵ s ~ 3×10⁷ yr | Galactic dynamics |
| τ_Hubble | ~4×10¹⁷ s ~ 1.4×10¹⁰ yr | Cosmological regime |
| τ_Page (M_f=1.9×10¹⁴ kg) | ~3×10²⁶ s ~ 10¹⁹ yr | Quantum-information regime |
| τ_evap (M_f) | ~6×10²⁶ s ~ 1.8×10¹⁹ yr | Asymptotic Hawking regime |

Substitution chain — pinned ratios of consecutive scales:

```
τ_evap / τ_BHL-merge   = 1.8×10¹⁹ / 2.5×10⁵ ≈ 7×10¹³  (13.8 OOM)
τ_BHL-merge / τ_lifetime = 2.5×10⁵ / 10² ≈ 2.5×10³    (3.4 OOM)
τ_lifetime / τ_transit  = 10² / 10⁻⁵ yr (425 s) ≈ 7.4×10⁶ (6.9 OOM)
τ_transit / τ_ringdown  = 4×10² / 10⁻²⁰ ≈ 4×10²²      (22.6 OOM)
```

**Direction**: each adjacent ratio defines a "consequence regime" — the dynamics during the shorter timescale completes faster than the longer-timescale process can react. The mechanical/transit consequences (E5/E6, ~minutes) finish before any thermal Hawking signature builds up (~kW over years). The merger via BHL drag (~10⁵ yr) is completed before galactic-orbital effects (~10⁷ yr) become relevant. The Page-curve / quantum-information evolution operates at scales where the merger product has already migrated into Earth's core for ~10¹³ Hubble times. Each consequence regime has a different leading actor; the layered hierarchy is the analytical structure of the entire problem.



### Answers to Einstein's Questions

**Q1 — Kerr cross-section asymmetry for hyperbolic capture.** Einstein's D1 is correct and I concede in HC1 above. The asymmetry is `(b_pro − b_retro)/b_avg ≈ χ v/c = 4.57×10⁻⁴` at v=200 km/s — *linear* in χv/c via the Bardeen-Press-Teukolsky frame-dragging tilt term, not quadratic as my Q1 framing suggested. The signed-asymmetry direction (prograde captures favored) means dressed-Kerr remnants in dense regions experience competition between Page-radiation spin-down and accretion-driven spin-up. For the living-room scenario this is irrelevant (the remnant sinks into Earth's interior where local densities and capture rates take a different form), but for the cosmological PBH-DM population it is a real effect that my R1 dχ/dt narrative missed.

**Q2 — GW bremsstrahlung memory from atmospheric drag.** The "memory step survives stratification breaking" argument in Einstein's R2 is the right answer. For straight-line motion through *homogeneous* matter the TT-projected quadrupole has no time-derivative contribution, so the Christodoulou memory vanishes. For *stratified* atmosphere ρ(z) = ρ₀ exp(−z/H), the drag force varies along the trajectory as the PBH transits scale heights, producing a non-zero `d³Q/dt³` and hence a non-zero memory step. Einstein's amplitude estimate `Δh ~ G/(c⁴D) · ΔE_radial_kinetic ~ 8×10⁻⁴¹` at meter range falls to ~10⁻⁵⁰ at any astrophysical baseline. **Direction**: memory exists, magnitude undetectable by any extant or proposed detector; the geodesic treatment in E5/E6 implicitly invoked translation symmetry that is broken by stratification, but the violation is observationally inert. Concede the point structurally: the *symmetry* assumption was implicit and incorrect, but the *consequence* is undetectable.

**Q3 — Equivalence principle and self-sourced plasma.** Einstein's D2 is correct and I concede in HC3 above. At leading order the integrated stress-energy flux through a sphere just outside the horizon vanishes by isotropy of spherically-symmetric Hawking emission; the PBH does not "feel" its own emission as a self-acceleration. The non-trivial second-order corrections (Kerr m-mode azimuthal preference giving net angular-momentum flux without linear-momentum flux; gradient coupling to inhomogeneous external matter) are the actual physics, but they enter at higher order. The Mino-Sasaki-Tanaka self-force formalism applies cleanly and gives zero leading-order self-force. My R1 framing conflated intrinsic self-force (zero) with extrinsic gradient coupling (second-order), and I retract the TOV-style "back-reaction reduces effective horizon area" suggestion.

**Q4 — Transient horizon dynamics during ringdown.** Einstein's D3 is correct: the area-theorem ceiling on ε_GW is 24% at χ_f = 0.685, not 5% — the NR-calibrated 5% is dynamical, not theorematic. During the brief common-apparent-horizon-formation window (~few light-crossing times ≈ 10⁻²¹ s), there is no single global event horizon, only a family of trapped surfaces; energy transport across the still-forming boundary is dictated by NR dynamics and not forbidden by any GR theorem up to the area-theorem ceiling. For exotic merger geometries (head-on collisions, hyperbolic encounters, near-extremal initial spins) ε can climb above 5%, with the theoretical ceiling at 24% (or 29.3% in the χ_f → 0 Schwarzschild-final limit). The 5% number for equal-mass non-spinning quasi-circular merger is reliable as an NR observation, but it is not a hard upper bound from cosmic censorship as I had implied. Concede.

**Q5 — Earth-traversal antipodal exit dynamics.** Einstein's D2/Q5 substitution chain is correct and I concede in HC2 above. The Coriolis displacement is `x_⊥(τ) = Ωvτ²` (no leading ½), giving 394 km, not 200 km. My factor-of-2 error was in conflating velocity (which carries the ½ from a single integration) with displacement (which requires a second integration). The Lense-Thirring frame-dragging contribution Ω_LT(R⊕) ≈ 4×10⁻¹⁴ rad/s is 9 OOM smaller than Newtonian Coriolis, contributing a sub-millimeter correction to the 394 km deflection. Concede the numerical correction; the structural statement (rotating-Earth metric does not produce inward-spiraling geodesics at observable level) holds.

**Q6 — Stochastic GW background from cosmological PBH binary mergers.** Einstein's calculation `h_inspiral ≈ 3.58×10⁻⁵⁰` for a single 10¹⁴ kg chirp at 10 Mpc and 100 Hz — 27 OOM below LIGO sensitivity, vs my "10 OOM short" R1 guess. I concede the numerical correction. The mass-scaling argument I cited (`h ∝ M^{5/6}`) is correct, but I underweighted the absolute scale. Substitution chain check (verified Python via Einstein's chain): at chirp mass M_chirp = 0.87×10¹⁴ kg, distance 10 Mpc, frequency 100 Hz, the strain is (G M_chirp/c³)^{5/3} × (πf)^{2/3} × c × 4/D = 3.58×10⁻⁵⁰; LIGO 100-Hz sensitivity ~10⁻²³, ratio 3.58×10⁻²⁷ = 27 OOM gap. My "10 OOM" guess was wrong by 17 orders of magnitude. **Direction**: the PBH-DM 10¹⁴ kg window is GW-silent at every detector frequency by 12–27 OOM depending on frequency band and source population. The only viable GW handle on PBH dark matter at this mass is — emphatically — none, confirming Einstein's R2 sharpening of my R1 underestimate. The detection channel for asteroid-mass PBHs lies entirely in (i) gamma-ray flux from individual evaporators near M ~ 10¹¹ kg, (ii) microlensing at the upper end of the window where r_s approaches photon wavelengths, and (iii) the speculative Bondi-cylinder ionization wake of HE1.

---

## Workshop Verdict

| Topic | Status | Joint Finding (one sentence) |
|:------|:-------|:-----------------------------|
| T1 — Mass range | **Converged** | The unconstrained PBH-DM window is [1.7×10¹¹ kg, 10¹⁹ kg]; the canonical 10¹⁴ kg case has r_s ≈ 148 fm, T_H ≈ 1.23×10⁹ K (kT_H = 106 keV), and P ≈ 35.6 kW per PBH. |
| T2 — Tidal / approach | **Emerged** | Lethality is a three-level radiological envelope (instant-kill r ≈ 8 m, acute-LD50 r ≈ 109 m, stochastic-mortality r ≈ 243 m) that DOMINATES the tidal-stretch envelope (bone failure at ~37 cm) by 30× at the canonical mass; gamma exposure, not gravitational stretching, is the proximate killer. |
| T3 — Collision dynamics | **Emerged** | Peters GW timescale (2.5×10²¹ yr at a=1 m) is irrelevant — BHL atmospheric drag inverts the conclusion and drives merger in ~200,000 yr, with the binary transitioning at a ≈ 5.7 cm from c_s-limited subsonic drag to v_orb-limited supersonic + GW completion. |
| T4 — Evaporation / final state | **Converged** | The Kerr merger remnant (M_f ≈ 1.9×10¹⁴ kg, χ_f ≈ 0.685, r_+ ≈ 243 fm, T_Kerr ≈ 5.4×10⁸ K) is quasi-permanent: τ_evap ≈ 1.83×10¹⁹ yr ≈ 1.3×10⁹ Hubble times; t_Page ≈ 6.6×10⁸ Hubble times in the future. |
| T5 — Energy budgets | **Converged** | The mechanical-impact channel (transit KE ~ 10²⁴ J × ε ~ 4×10⁻⁷ deposited ≈ 10¹⁸ J + tidal fragmentation 1.6×10¹⁶ J) dominates the Hawking-emission channel (35.6 kW per PBH continuous) by ~10¹⁰ during a flyby; the Hawking channel only matches the mechanical channel after ~360,000 yr of residency. |
| T6 — Earth survival of approach | **Converged** | Earth survives the approach mechanically (M_PBH/M_⊕ ≈ 1.7×10⁻¹¹; binding-energy ratio 16 OOM in Earth's favor); a fast transit punches a 74-cm-diameter, 12,700-km pulverized chord (~16 Gt rock, M ≈ 8 seismic equivalent ~10¹⁶ J) and exits ~394 km from the geometric antipode (Coriolis); only the immediate <10 m chord-vicinity is biologically lethal. |

Status legend: **Converged** (both agree) / **Dissent** (disagreement persists) / **Partial** (structure agreed, specifics disputed) / **Emerged** (new finding from exchange).

---

## Remaining Open Questions

Each question is specific enough to become a calculation. We list five — three substantial, two diagnostic.

1. **Final orbital fate of the merger product after BHL-drag inspiral.** The cross-domain calculation in HE2 gives a settled remnant location at ~Earth's geometric center on a ~10⁵–10⁶ yr settling timescale, but does not resolve: (a) whether the binary's CoM oscillation through Earth's interior crosses (and dynamically interacts with) the inner-core/outer-core boundary at r ≈ 1220 km, (b) whether the differentiated viscosity profile of the mantle/core changes the supersonic-BHL drag prefactor, (c) whether the remnant captures into stable Earth-orbit instead of sinking (requires the binary's pre-merger v_inf < v_escape ≈ 11.2 km/s, which the workshop premise assumes but doesn't quantify). A geophysics-coupled BHL-inspiral simulation with the PREM density profile and depth-dependent c_s could resolve all three sub-questions; pre-registered metric: depth (in R_⊕ units) of the merger-remnant equilibrium position at t = 10⁶ yr post-merger.

2. **Quantitative photon spectrum and duty cycle of the Bondi-cylinder ionization wake.** HE1 sketched the wake as a 30 m × 1 mm filament radiating ~10 kW in soft X-ray to UV (50 eV–500 eV continuum + recombination lines from N, O, Ar) with ms-scale duty cycle behind a moving 100-keV gamma source. Full radiation-hydrodynamics simulation of an air parcel falling into an isolated 10¹⁴ kg PBH (with self-consistent ionization, recombination, and gamma photoionization heating) would predict the exact line ratios (N V vs N IV, O VI/V/IV, free-bound continuum slope) and could be matched against existing all-sky gamma-ray + soft-X-ray archives (Fermi-LAT, Swift-BAT, ROSAT-RASS) to set actual upper limits on f_PBH-DM × (transit rate per kpc²). Pre-registered metric: predicted [O III] / [N V] ratio for the wake's recombination cascade and resulting upper limit on f_DM at M = 10¹⁴ kg.

3. **Refined cosmological happenstance bound.** Einstein's EMERGE-3 single-observer rate (~10⁻³⁹ per lifetime) and HD3's clustering-amplified version (~10⁻³⁰ to 10⁻³⁶ per Earth-history) both yield uninformative constraints from "no-living-room-event" non-observation. The richer integration is over PBH-PBH collision rates × DM density profiles × planetary-volume cross-sections across the entire observable universe, with the rate compared to known stellar/GRB demographic limits. A non-detection of *any* PBH-PBH-collision-driven flash signature in galactic-disk surveys over modern instrumented era (~50 yr) is a genuine, if weak, abundance bound. Pre-registered metric: 95% CL upper limit on f_PBH-DM × η_clustering for M = 10¹⁴ kg from Fermi-LAT and Swift-BAT all-sky archives, accounting for the predicted Bondi-cylinder spectrum from question #2.

4. **Bondi-cylinder-saturation transition for the binary inspiral.** HD1 identified the BHL regime change at a ≈ 5.7 cm where v_orb = c_s and the formula switches from c_s-limited to v_orb-limited. The full inspiral trajectory through this transition has not been solved analytically; it requires patching the subsonic-BHL ODE (constant Ṁ ∝ ρ/c_s³, drag F·v ∝ ρ v²/c_s³) onto the supersonic ODE (Ṁ ∝ ρ/v³, drag F·v ∝ ρ/v) at a = r_BHL, plus simultaneous Peters-GW dissipation. Substitution chain (sketch):

   ```
   Definition:    Total dE/dt = (dE/dt)_BHL + (dE/dt)_GW
   Substitute:    Above sonic radius:   dE/dt|_BHL = − 4π(GM)² ρ v_orb²/c_s³, dE/dt|_GW = −(32/5) G⁴ M⁵/(c⁵ a⁵)
                  Below sonic radius:   dE/dt|_BHL = − 4π(GM)² ρ/v_orb,        dE/dt|_GW unchanged
   Direction:     The handover happens at a*: solve for a where dE/dt|_BHL = dE/dt|_GW
                  Above a*: BHL dominates. Below a*: GW dominates. Pre-registered metric:
                  numerical value of a* (in meters) for M = 10¹⁴ kg, ρ_air = 1.2 kg/m³.
   ```

   A modest Python ODE integration would close the question and yield a sharper merger time than the EMERGE-1 estimate.

5. **Multi-channel detection strategy for asteroid-mass PBH-DM.** Given the workshop's conclusion that GW astronomy is silent at this mass (27 OOM short of single-source detection, 12+ OOM short for stochastic background), microlensing handles only the upper end of the window (M > 10²² g where r_s approaches optical λ), and direct gamma-ray surveys catch only the evaporating-cliff population (M ≈ 10¹¹ kg), the question is: what is the *combined* detectability of the [10¹¹ kg, 10¹⁹ kg] window across all channels — gamma-ray-burst surveys for evaporators, soft-X-ray Bondi-cylinder transits for the asteroid-mass band (HE1), wide-field optical for microlensing at 10¹⁹ kg, and pulsar-timing-array (PTA) constraints on dynamical effects in the solar neighborhood? Pre-registered metric: union of 95% CL exclusions on f_PBH-DM(M) across all four channels, plotted as a single bound function over the full window.

---

## Wrap-Up — The Living-Room Verdict

### What Happens to the Living Room

Within the first second, two things happen simultaneously, on different physical channels.

**The radiation channel kills you before anything else gets a chance.** The two PBHs together emit 71 kW of 100-keV gammas continuously. At the user's typical viewing distance of ~2 m the dose rate exceeds 30,000 Sv/hr; the LD50 dose of 5 Sv accumulates in ~0.6 seconds. There is no warning — the photons are not visible, the air does not glow at this density, and the source is sub-atomic. The user's first physiological signal is acute radiation sickness arriving from the inside out: ionization-driven cellular damage propagates through the first ~6 cm of forward-facing tissue (one mean free path at 100 keV in water), with the surface dose 10× the deep-organ dose because of Compton-electron showers depositing back into the entry layer. **You die in roughly half a second from radiation, regardless of whether you are 2 m away or 8 m away.**

**The tidal channel destroys the room about a second later.** Inside ~37 cm of either PBH the tidal stretch breaks bone (Eq. 1 with σ_bone = 1.3×10⁸ Pa, M = 10¹⁴ kg gives r_fail = 0.37 m); inside ~1 m the wood framing fails; inside ~4 m the drywall and plaster shatter; inside ~4 m the concrete slab cracks. The ~1 m orbital binary cuts a roughly 4-m-radius cylinder of disrupted material around its orbital plane. Substitution chain on volume:

```
Definition:    V_room_tidally_disrupted = π · (4 m)² · 2.4 m (ceiling height)
Substitute:    V = π × 16 × 2.4 = 121 m³
Direction:    A volume larger than a typical living room is tidally fragmented;
              within ~1 second the room's structural integrity is gone.
```

The carpet ignites from the gamma-induced ionization (recombination radiation pumps the air to ~10⁴ K within centimeters of the PBHs); the wood smolders; the air is briefly opaque to soft X-ray and UV. Furniture within 4 m disintegrates into a column of pulverized material along the orbital axis; furniture beyond 4 m receives only the radiation. The two PBHs themselves continue orbiting at v_orb ≈ 58 m/s, decaying via BHL drag (HC5: τ_drag ≈ 200,000 yr at this separation) — essentially unchanged on the 1-second timescale of human destruction.

The user is dead. The room is on fire. The two PBHs are still there, glowing in soft X-ray to anyone with the right detector, drilling toward the floor under their own gravity.

### What Happens to the House

The structural failure pattern is **radial in radiation, axial in tidal**. The radiation propagates spherically: 35.6 kW per PBH in 100-keV gammas falls off as 1/r². At 10 m (next room): dose rate ~590 Sv/hr — instantly lethal. At 24 m (across the house): ~100 Sv/hr — lethal in hours. At 30 m (front yard): ~65 Sv/hr — still lethal. The acute-LD50 radius is ~109 m (HD2 substitution chain, verified Python). **The whole house — every room, every floor, every closet — is inside the acute-kill zone.** Any occupant anywhere in the building dies of radiation before noticing the structural damage.

The structural damage follows the binary's CoM trajectory. After ~0.7 s the CoM is at the floor (free-fall through 2.4 m). The PBHs punch through the slab and into the foundation; the slab cracks within a ~4 m radius of the impact point because of tidal stress on its tensile-weak mineralogy (E2's substitution: r_fail ≈ 4 m for concrete tensile, σ_fail = 3×10⁶ Pa). Wood framing within ~1 m of the descending CoM snaps. Steel beams (joists, lintels) within ~1.5 m fail under tidal stretch. The roof above the impact point sags; the ceiling above the orbiting binary collapses inward (gamma-driven thermal weakening + tidal loss of structural support). 

The kitchen plumbing within ~4 m bursts (concrete-tensile-equivalent failure of the slab they sit in). Window glass within ~10 m fractures from differential thermal stress as the gamma flux (3 kW/m² at 10 m) heats the inner surface 30× faster than the outer; the glass shatters in ~10 seconds. Above the binary's location, the upper floor's drywall ceiling shatters; below it, the basement slab cracks. **The house's structural shell remains standing** — load-bearing walls > 4 m from the orbital plane stay up, the foundation > 4 m from the impact column survives — but the interior is destroyed and the building is biologically uninhabitable for ~243 m around it.

Neighbors next door (typical lot ~10 m to property line, ~25 m to neighbor's center) experience: ~5 W/m² gamma flux on first-encounter side (sufficient to puncture the wall and ionize the interior air column), dose rate ~360 Sv/hr — lethal in minutes. Through-wall attenuation is partial (100-keV gammas: building materials give ~2× attenuation per ~10 cm of concrete, ~1.2× per drywall layer); a typical house wall reduces incident flux by ~3-5×, leaving ~70-100 Sv/hr behind shielded geometry. **Direction**: house-shielding does not save you within 30 m. Beyond 100 m, double-walled shielding or basement geometry can reduce dose below acute-LD50 if the occupant evacuates within minutes.

### What Happens to the Neighborhood

The pulverized chord through the ground is the dominant geomechanical signature. The PBHs drill through the foundation, basement floor, and lithosphere on their orbital trajectory, with the binary's CoM accelerating downward under Earth gravity. Substitution chain for the chord cylinder:

```
Definition:    V_chord = π r_disrupt² · L_chord
Substitute:    r_disrupt = 0.37 m (tidal threshold for rock, σ_rock = 3×10⁶ Pa)
              L_chord = 12,700 km = 1.27×10⁷ m (full Earth diameter for
              typical chord; less for grazing trajectory)
Numerics:      V_chord = π × 0.137 × 1.27×10⁷ = 5.5×10⁶ m³
              M_disrupted = ρ_rock × V = 3000 × 5.5×10⁶ = 1.6×10¹⁰ kg = 16 Gt
              E_frag = M_disrupted × ε_frag = 1.6×10¹⁰ × 10⁶ J/kg = 1.6×10¹⁶ J
Compare:       Tsar Bomba: 2.4×10¹⁷ J → E_frag = 0.07 Tsar Bomba
              Chicxulub:   4×10²³ J  → E_frag = 4×10⁻⁸ Chicxulub
              Earth M=8 quake (Northridge-Loma Prieta scale): ~10¹⁶ J
Direction:    A 74-cm-diameter, Earth-diameter-long cylinder of pulverized rock,
              releasing M ≈ 8 seismic energy as Rayleigh waves + body waves
              propagating globally. Comparable to the largest historical
              earthquakes; localized devastation, but not planetary-scale.
```

**The blast radius is gravitational/seismic, not chemical/thermal.** The chord cylinder relaxes adiabatically: pressure waves travel outward at ~5 km/s in rock, reaching 10 km radius in ~2 seconds, 100 km in ~20 seconds. The local ground acceleration at 1 km from the chord is ~10⁻³ g (E6 substitution: tidal acceleration falls as r⁻³, drops to 0.1% g at 100 m where it would be 0.014 g, scales further with cube). Seismographs across the planet log a clear M ≈ 8 transient lasting ~minutes; structural damage extends to ~30 km radius for unreinforced masonry, ~10 km for modern wood-frame construction.

**Gamma-shadowing.** Behind a hill or substantial concrete structure (the chord cylinder is *underground*, so above-ground shielding works), the gamma flux drops to chronic-mortality range (1 Sv/hr) at ~200-300 m. The "neighborhood" — out to ~1 km — receives a population-scale dose around 10–100 mSv (above background-detection threshold but below acute thresholds for survivors who shelter promptly). The 100-keV gamma flux is detectable at ~7.7 km above natural background (HD2 substitution: 1 mSv/hr radius), which means *every gamma-ray detector within ~10 km* registers the event in real time. First responders entering the impact zone receive ~minute-scale fatal doses if they go inside the inner 100 m unprotected.

**Bondi-cylinder ionization sleeve.** Per HE1, the PBH's transit through the atmosphere leaves a 30-m-long faintly luminous tube along the trajectory in soft X-ray and UV; this is sub-millisecond as it sweeps overhead but produces a measurable optical/UV transient that distinguishes PBH transit from a meteorite (which leaves a *thermal* multi-second wake). Cameras with ms cadence pointed at the right part of the sky log a brief filament of light at the entry point.

The neighborhood is a federal disaster zone the day after; uninhabitable within 1 km until the in-Earth merger product is shielded somehow (it isn't — see the planet section). The seismic damage is localized; the radiation damage is widespread but survivable beyond ~250 m.

### What Happens to the Planet

Earth survives the approach mechanically. The bulk-energy bookkeeping is a clean GR fact: M_PBH/M_⊕ ≈ 1.7×10⁻¹¹, so Earth's gravitational binding (2.24×10³² J) exceeds the deposited energy (~10¹⁶ J for tidal fragmentation + transit; ~10¹⁸ J cumulative for KE coupling) by ~16 OOM. There is no risk of dynamical disruption.

**The merger product becomes a permanent Earth-bound feature.** Per HE2, after the binary's CoM stops oscillating (~2,800 yr) and the binary inspirals to merger in rock medium (~245,000 yr additional), the resulting 1.9×10¹⁴ kg Kerr remnant settles toward Earth's geometric center. From that position it Hawking-radiates at 9.87 kW (Kerr-cooled merger product), depositing energy locally into Earth's deep interior. Substitution chain for total deposit over Earth's lifetime:

```
Definition:    E_deposited = P_remnant · t_remaining_solar = 9870 W · 5×10⁹ yr × 3.15×10⁷ s/yr
Substitute:    E_deposited = 9870 × 1.58×10¹⁷ = 1.56×10²¹ J
Compare:       Earth radiogenic heat (47 TW × 5 Gyr) = 4.7×10¹³ × 1.58×10¹⁷ = 7.4×10³⁰ J
              ratio E_PBH / E_radiogenic = 1.56×10²¹ / 7.4×10³⁰ = 2×10⁻¹⁰
Direction:    Hawking heat deposit from interior PBH is 10 OOM SMALLER than
              radiogenic heating over the same span. Earth's geothermal
              budget is utterly unaffected.
```

The remnant continues evaporating on its 1.83×10¹⁹ yr timescale; in ~5 Gyr (when the Sun engulfs Earth), the remnant's mass loss is ≈ 0 (rounded to the 10⁻⁹ part of M_f). **The PBH outlives the planet that hosts it by 10⁹ Hubble times.** When Earth is consumed by the red-giant Sun, the PBH inherits the orbit of Earth's debris; it persists as a microscopic stellar-system remnant, eventually scattered out of the solar system by stellar dynamics and rejoining the galactic-halo PBH-DM population.

**Cosmological consequences.** None. The encounter happens on Earth, kills an Earth-bound civilization in the inner ~250 m radius, deposits a permanent micro-BH into Earth's core, and is invisible from interstellar distance: the Hawking flux at 1 light-year is ~10⁻¹⁰ W/m², 12 OOM below Fermi-LAT all-sky sensitivity at 100 keV. **The galaxy does not learn that this happened.** Even at solar-neighborhood densities, the local PBH count is too sparse (10⁻³⁵ m⁻³ in atomic units) for one event to bias local astronomical observables. The encounter is, in cosmological terms, a delta-function event with no measurable trace beyond the geocentric 250-m mortality zone and the Earth-interior thermal signature 10 OOM below detection.

The cleanest planet-scale statement: Earth's mass increases by ~1.9×10¹⁴ kg (a few hundredth-of-a-thousandth of an asteroid); Earth's geothermal flux is unchanged at the 10⁻¹⁰ level; Earth's surface absorbs ~M8-equivalent seismic energy and ~10⁻¹¹ of its rest mass-equivalent in radiation; Earth's gravity field acquires a ~1.7×10⁻¹¹ relative perturbation at the new center-of-mass (utterly unmeasurable). **The planet survives; the inner core hosts a sub-fm Kerr remnant for ~10¹⁹ yr; nothing else changes.**

### Closing Line (one sentence — the punchline)

**You die in half a second of gamma rays, the room burns down in two more, the house collapses overnight, and Earth quietly grows a new pet asteroid-mass black hole in its inner core for the next billion Hubble times — but the cosmos won't notice, the dust will settle, and (cleanup notwithstanding) the planet will be fine.**
