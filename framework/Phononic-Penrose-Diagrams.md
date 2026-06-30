# Penrose Diagrams for the Phonon-Exflation Framework

**Author**: Schwarzschild-Penrose Geometer
**Date**: 2026-03-21 (authored, post-S53); comprehensively expanded 2026-05-25 (S93-era synthesis, Session-X W5)
**Status**: Definitive framework document — current through Session 93
**Sources**: S7–S53 (original catalog A–I); S39 Penrose diagrams; S48/S49 conformal + censorship; S50 CMPP; S52 Weyl crossings; S53 tight-binding + acoustic pivot. **S54→S93 expansion**: S54 scale-factor/q(τ); S55 dynamic-transit conformal diagram (DIAGRAM-55); S63/S66 bi-metric Kasparov decoupling ([T3]); S63/S64 second-order tensor (TENSOR-SCALAR-64); S66 DILUTION-CC; S69 conformal-factor transit (TRANSIT-69/FACTOR-69) + conformal anomaly (ANOM-69); S70/S71 Penrose sequence + causal-moment-map (MAP-71); S74 entry-horizon/open-exit + modulus decay; S76 GGE-transit CMPP (TRANSIT-76); S77 overshoot turnaround + reheating; S84 W8B-95 + S85 W6-2 CMPP type-invariance; S85 W6 conformal-structure suite (J–N); S92 spectral-dimension flow vs CDT; S93 W8-7 emergent 3-slices.
**Grounding**: Every number cited is computed and traced to a canonical constant, permanent theorem (`atlas-07-permanent-results`), closed mechanism, or gate verdict. Every boundary classified. Nothing speculative unless marked. Direction of explanation: **D_K eigenvalues → spectral-action moments → emergent metric → causal structure** — never the reverse.

**Regulator convention (a_n Seeley-DeWitt tagging)**: throughout this document the Seeley-DeWitt / spectral-action coefficients are the **zeta-regularized** moments of the Connes-Chamseddine spectral action `S_b(D_K, Λ) = Tr f(D_K²/Λ²) ~ f_4·Λ⁴·a_0^{ζ} + f_2·Λ²·a_2^{ζ} + f_0·a_4^{ζ} + …`; i.e., every bare `a_n` below denotes `a_n^{ζ}` (zeta-function regularization) per `regulator-pin-discipline.md`. The three load-bearing moments are: **a_0^{ζ}** (cosmological/vacuum-energy term; a_0 = 6440 M_KK^{d−4}, DILUTION-CC), **a_2^{ζ}** (Einstein-Hilbert/gravity term; the emergent 4D metric g_M), **a_4^{ζ}** (Yang-Mills + Higgs quartic term). The conformal-infinity bifurcation (Diagrams L_dS/L_flat) is the one place regulator-class matters for the *causal* conclusion — there the asymptotic ℐ⁺ is S³ (de Sitter) under cutoff/heat/dim and R×S² (flat) under ζ/PV; that regulator-conditionality is stated explicitly at Diagram L.

---

## Overview

Product spacetime M^{3,1} × SU(3), dimension 12. Volume-preserving Jensen deformation τ ∈ [0, ∞). The fabric's internal geometry at each point IS the spectral triple (A_K, H_K, D_K); the 4D effective metric g_M emerges from the a_2 Seeley-DeWitt moment. The physical universe lives at **τ ~ 0.22** (the post-fold epoch), DISTINCT from the **van Hove fold τ_fold = 0.19** (see disambiguation below). N_pair = 1 on a 32-cell lattice. The acoustic metric a_acoustic = a_geom √(ρ_s/c_s) is a SECOND causal structure — and, per the bi-metric Kasparov split (Diagram C), it is what the SCALAR excitation sector sees, while the TENSOR sector sees the a_2-emergent gravitational metric.

Five distinct diagram types are needed: (A) full 12D product spacetime; (B) 1+1D modulus space; (C) acoustic metric with two null cones (bi-metric); (D) 32-cell lattice causal structure; (E–I) cosmological history, Petrov/Weyl, horizons/censorship, complete history, novel/speculative. The post-S53 work added the conformal-factor / Penrose-sequence diagrams (S69–S71), the S85 W6 conformal-structure suite (J–N), and the spectral-dimension / CCC sections. **Their interrelation IS the framework.**

### Disambiguation Callout 1 — The τ landmarks (τ_fold = 0.19 vs the physical epoch τ ~ 0.22)

The two values are NOT the same point and must never be conflated:

| Symbol | Value | Meaning | Causal role | Source |
|:-------|:------|:--------|:------------|:-------|
| **τ_fold** | **0.19** | van Hove fold = dump = `B2` eigenvalue minimum | **Extremal horizon** (double-root V=V'=0 ⟹ κ=0, T_H=0) | `tau_fold` canonical, S12/S42 CONST-FREEZE-42 (NOT superseded); S85 W6-4 extremal horizon |
| **τ ~ 0.22** | ~0.22 | post-fold physical-universe epoch | where the GGE relic / observable cosmology sits, just past the extremal horizon | atlas-07 "4-zone Penrose, Zone I τ∈[0.19, 0.22]"; S53 |

The fold is the *boundary* (extremal Killing horizon); 0.22 is *just inside* the surviving region. Treating 0.22 as "the fold" or 0.19 as "the physical epoch" is a category error. (This is the conformal-geometry analog of the broader τ-quartet disambiguation tracked framework-wide.)

### Disambiguation Callout 2 — The Equation-of-State quartet (do NOT collapse to one w)

The framework carries FOUR distinct equation-of-state values, at DIFFERENT epochs and from DIFFERENT physics. The 2026-03 version of this document wrote "w = 0.202" on the cosmological diagrams as if it were the dark-energy EoS; it is not — it is the kinetic/transit-era *stiff* value. The current quartet:

| Symbol | Value | Epoch / physics | Source |
|:-------|:------|:----------------|:-------|
| w (kinetic, transit-era) | **0.202** | post-transit GGE relic kinetic domination (the decelerating-FRW epoch on Diagrams A/E/H) | S53 phonon EoS |
| w (initial stiff) | **+1** | τ→0 round-SU(3) modulus kinetic domination (Zel'dovich stiff matter) | atlas-einstein-collab |
| **w0_FW** (late-time DE, **canonical**) | **−0.918** | the framework's dark-energy EoS today (Volovik vacuum partition + effacement Γ_eff=0.99970) | `w0_FW` canonical, S58/S66 |
| w_0_B (substrate-compaction branch) | **−0.842454** | DE EoS under the substrate-compaction timescape branch-(iv) | S85 W10-2 (workshop value; not a separate canonical pin) |
| GGE multi-T band | **[−0.43, −0.59]** | GGE relic effective EoS over its 8-temperature band | S49 multi-T |

LCDM reference: w_0_LCDM = −1.0 (cosmological constant, by definition). The cosmological-history diagrams (E, H) annotate the kinetic w=0.202 at the GGE epoch AND the late-time DE w0_FW=−0.918 — they are different rows of the same history, not a contradiction.

### Disambiguation Callout 3 — The velocity glossary (THREE distinct transit/sound speeds)

The diagrams carry three velocity-type quantities that look alike but are physically distinct. The 2026-03 version labeled Diagram A's extrinsic velocity "v_transit = 26.5" — colliding the symbol `v_transit` (whose canonical Mach partner is 13.75) with the 12D extrinsic-curvature velocity. Disambiguated:

| Quantity | Value | What it is | Mach partner |
|:---------|:------|:-----------|:-------------|
| **v_transit** (modulus-space) | **6.67 M_KK** | dτ/dt, the rate of the Jensen modulus through the fold (1+1D modulus metric) | **Mach_max = 13.75** = v_transit / c_s (c_s = 0.485 M_KK, BLV acoustic speed; S63 W1-04) |
| 12D extrinsic velocity | **26.5 M_KK** | the extrinsic-curvature transit speed that makes K²_ext dominate internal Weyl by ~10⁷× (Type G driver, Diagram A) | (distinct from the modulus Mach; an extrinsic-curvature magnitude, not a sound-relative ratio) |
| acoustic-analog Mach | **54.3** | the peak Mach of the GPE/BEC acoustic-analog white-hole simulation (a laboratory projection, not a substrate quantity) | (analog-platform value; MEMORY analog) |

The substrate-relevant supersonic ratio is **Mach_max = 13.75** (modulus dτ/dt vs BLV sound speed). The acoustic-analog Mach 54.3 belongs to the BEC model OF the transit, not the substrate itself (substrate-first: the BEC models a simplified projection of the substrate).

---

## Diagram A: The Full 12D Product Spacetime

The exact metric on M^{3,1} x K^8 is:

    ds^2_{12} = -dt^2 + a(t)^2 d x_3^2 + g_{ab}(tau(t)) dy^a dy^b

where g_{ab}(tau) = 3 * diag(e^{-2tau} x 3, e^{tau} x 4, e^{2tau} x 1) is the Jensen metric on SU(3). The CMPP algebraic classification (S50 W1-G; now PERMANENT, S84 W8B-95 / S85 W6-2) gives:

- **Static (tau_dot = 0)**: Exact Type D at ALL tau. The WAND is the time + SU(2) pair direction. This is a structural theorem: any product M^{3,1}_flat x K^n is Type D with WAND in the flat factor.
- **Dynamic (tau_dot > 0)**: Type G (algebraically general). Extrinsic curvature K^2 dominates internal Weyl by 10^7x during transit (the 12D extrinsic velocity v = 26.5 M_KK is the driver — NOT the modulus v_transit = 6.67; see velocity glossary). Post-freeze (tau_dot -> 0): Type D restored.

### The Type-Invariance Theorem (S84 W8B-95, PERMANENT) — and the Riemannian artifact it corrected

The static-D / dynamic-G classification is no longer a single-τ result; it is a **type-invariance theorem**. `S84-W8B-95-CMPP-PETROV-TYPE-INVARIANCE` (PASS) returned the signature `D/D/D/D/D/D/D/D/G/G/G/G/G/G/G/G` across 8 static + 8 dynamic τ-points, with the 4D a_2-reduced effective metric (`convention=a2-reduction-4D`); S85 W6-2 confirmed it on a **dense 171-point grid** τ∈[0, 1.7]. The type does not flow within either branch — it is a structural invariant of the product geometry, exactly as the WAND-in-the-flat-factor theorem predicts.

This corrected a **substrate-first self-correction worth flagging explicitly**: the earlier S49 computation, `CMPP-TRANSITION-49`, FAILED — it returned **Type II at all 16 τ-values** because it classified the *Riemannian* SU(3) bivector spectrum ("Riemannian signature locks CMPP type"). The CMPP scheme is a *Lorentzian* algebraic classification; applying it to the Euclidean internal Weyl tensor is a category error that artificially produces Type II. The S50 Lorentzian a_2-reduction (atlas-07 A3/A4) — which projects the 12D Weyl content onto the emergent 4D Lorentzian effective metric BEFORE classifying — gives the correct **Type D**. The lesson is canonical to the framework's method: the causal/algebraic type is a property of the *emergent Lorentzian* geometry (substrate → a_2 moment → 4D metric → Petrov type), not of the raw Riemannian fiber. The 8D Riemannian Petrov classification of the bare fiber (atlas-07 A3: Type D at τ=0 Einstein manifold, algebraically general with 8 distinct eigenvalues at τ>0, stable multiplicity {3,4,1,2,4,3,...}) is a SEPARATE statement about the internal geometry and is not the causal type of the spacetime.

> ![Diagram A — Full 12D Product Spacetime](../../figures/penrose/framework-A-12d-product.png)
>
> **TikZ source**: [`figures/penrose/framework-A-12d-product.tex`](../../figures/penrose/framework-A-12d-product.tex) — compile with `xelatex` (or `./figures/penrose/build.sh framework-A-12d-product.tex`).

```
                        i+
                       /  \
                      /    \                    CONFORMAL INFINITY
                     / I+   \                   of the 4D factor.
                    /  (null) \                 SU(3) is compact:
                   /    inf    \                it does NOT appear
                  /             \               at conformal infinity.
                 /  STANDARD     \              I+/- are 4D constructs.
                /   FRW with      \
               /    w=0.202        \            Post-transit: 78 decelerating
              /     (GGE relic      \           e-folds with w=0.202.
             /       epoch)          \          T: 8.32e15 -> 0.016 GeV.
            /                         \
           /===========================\  <---- TRANSIT COMPLETION (tau ~ 0.22)
          /   EXFLATIONARY TRANSIT      \       a_acoustic gains 2.92 e-folds
         /    tau: 0 -> 0.22            \       a_geometric gains 0.17 e-folds
        /     dt = 0.00113 M_KK^{-1}    \      Petrov: D -> G -> D
       /     (instantaneous on 4D        \
      /       cosmological timescales)    \
     /                                     \
    / - - - - - - - - - - - - - - - - - - - \ <-- 4D INITIAL SURFACE
   /    INITIAL STATE (tau = 0)              \     Hartle-Hawking or
  /     Round SU(3) metric                    \    equivalent prescription
 /      K = 0.500, |C|^2 = 5/14               \
/       WCH MINIMUM. DNP-unstable.              \
\       ALL directions repulsive.                /
 \                                              /
  \                                            /
   \                                          /
    \                                        /
     \                                      /
      \                                    /
       \                                  /
        \                                /
         \                              /
          \                            /
           \                          /
            \                        /
             \                      /
              \                    /
               \                  /
                \                /
                 \              /
                  \            /
                   \          /
                    \        /
                     \      /
                      \    /
                       \  /
                        \/
                        i-
```

### Key Feature: SU(3) Invisible at Conformal Infinity

The product structure means the compact internal space does not contribute to the conformal boundary. The 12D Penrose diagram is conformally identical to the 4D diagram with modified matter content. The internal dimensions appear only through the 4D effective stress-energy with w = p/rho >= 1 (stiff matter, G_mod = 5.0, V_KK = -(M_p^2/2)R_K < 0). This is why the diagram resembles decelerating FRW, not de Sitter.

### Petrov Type Evolution on the Diagram

```
    i+  ─── TYPE D (static product restored, tau_dot -> 0)
     |
     |       TYPE G  (generic, K_{ext}^2 >> C_{int}, v_ext = 26.5 M_KK)
     |       bw+2 = 0.83%
     |       |C|^2 = 2.27e7 (K^2 dominates by 10^7x)
     |
    ═══ ─── TYPE D -> G TRANSITION (transit begins, tau_dot jumps)
     |
    i-  ─── TYPE D (round SU(3), static, exact)
```

The vertical axis is conformal time on the 4D factor; the type is INVARIANT within each branch (S84 W8B-95). The transition D→G→D is driven by τ̇ switching on at the fold and off at freeze — not by any change in the WAND structure, which remains the time + SU(2)-pair direction throughout.

### GGE-Transit Petrov Type (S76 TRANSIT-76, sp-authored)

A finer question than "static vs dynamic" is the Petrov type of the **GGE state during the transit itself** — the algebraic type of the effective Weyl content carried by the post-pair-production GGE relic as it forms across the fold. `CMPP-TYPE-GGE-TRANSIT-76` (W3-H) classifies this intermediate régime: it is consistent with the dynamic Type-G branch (the GGE forms inside the τ̇>0 window where K²_ext dominates), confirming that the GGE relic does NOT introduce an independent algebraic structure — it inherits the transit's Type G and relaxes to the static Type D as τ̇→0 at freeze. This closes a potential loophole: one might have worried that the 8-temperature GGE (with its 8 distinct Lagrange multipliers) could carry a more special algebraic type (e.g., Type II or D split per branch); S76 shows it does not. The causal type of the spacetime is governed by the product geometry, not by the relic's internal thermodynamic structure.

---

## Diagram B: The Modulus Space Conformal Diagram

This is the core diagram of the framework. The modulus tau parametrizes the internal geometry. The effective 1+1D metric on the (t, tau) plane is ds^2 = -dt^2 + G_mod dtau^2 with G_mod = 5.0. This is a FLAT 1+1D Minkowski space with coordinate speed of light c_tau = 1/sqrt(G_mod) = 0.447. All physically significant features are labeled at their computed tau values.

> ![Diagram B — Modulus Space Conformal Diagram](../../figures/penrose/framework-B-modulus-space.png)
>
> **TikZ source**: [`figures/penrose/framework-B-modulus-space.tex`](../../figures/penrose/framework-B-modulus-space.tex) — compile with `xelatex`. Every labeled tau landmark (0.000, 0.190, 0.220, 0.285, 0.350, 0.537, 0.895, 1.340, 1.382) appears as a horizontal level-set inside the FRW square; BCS window and NEC-violation strip are shaded.

```
                             i+  (future timelike infinity)
                            /  \
                           /    \
                          /      \
                         / GIBBS  \
                        / THERMAL  \         S_Gibbs = 6.70 bits
                       / S=6.70 b   \        T = 0.113 M_KK
                      / T=0.113      \
                     /                \
                    / · · · · · · · · ·\ ← THERMALIZATION BOUNDARY
                   / t_therm ~ 6 nat   \    Delta_S = +3.159 bits
                  /    units [INTEG-39]  \   (irreversible entropy production)
                 /                        \
                /    POST-TRANSIT GGE      \
               /     S_GGE = 3.542 bits     \     w = 0.202
              /      S_entanglement = 0      \    N_e(FRW) = 78
             /       3 distinct lambdas       \   T: 8.32e15 -> 0.016 GeV
            /        Product state             \
           /          [ENT-39]                  \
          / ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ \ ← BCS EXIT (tau = 0.235)
         /          BCS WINDOW                    \
        /     tau in [0.143, 0.235], width 0.092   \
       /      59.8 qp pairs (Parker-type)           \    dwell = 3e-4
      /       Speed bump at tau = 0.2015              \   (max of V_eff)
     /        ▓▓▓▓▓▓▓▓ N_pair = 1 ▓▓▓▓▓▓▓▓            \
    /    ═════╪═══════════════════════╪══════             \
   /    fold │ tau=0.190  K=0.5346  │                     \
  /    ──────┤ |C|^2=0.3859        │                      \
 /           │ v_transit=26.5      │                       \
│   DUMP ────┤ tau=0.19            │                        │
│            │ B2 eigenvalue min   │                        │
│            │ T_H=0, kappa=0     │                        │
│   DNP ─────┤ tau=0.285           │                        │
│            │ TT-stability ends   │                        │
│            │                     │                        │
│   BCS ─────┤ tau=0.35            │                        │
│   WELL     │ (Jensen saddle)     │                        │
│            │                     │                        │
│   GEO. ────┤ tau=0.537           │                        │
│   PHASE    │ C2 sect. K < 0     │                        │
│   TRANS.   │ SPACELIKE boundary  │                        │
│            │                     │                        │
│   WEYL ────┤ tau=0.895           │                        │
│   ZERO     │ Branch 27 crosses 0 │                        │
│   (1st)    │ |C|^2 = 15.6       │                        │
│            │                     │                        │
│   WEYL ────┤ tau=1.340           │                        │
│   ZERO     │ Branch 27 re-crosses│                        │
│   (2nd)    │ Curvature island    │                        │
│            │                     │                        │
│   NEC  ────┤ tau=1.382           │                        │
│   VIOLA-   │ C2 Ricci eig = 0   │                        │
│   TION     │ Penrose thm blocked │                        │
│            │                     │                        │
│    ┌───────┴─────────────────────┘                        │
│    │                                                      │
│    │    ▒▒▒▒▒ KASNER SINGULARITY ▒▒▒▒▒                   │
│    │    ▒ K ~ (1/12) exp(4 tau) ▒▒▒▒▒                    │
│    │    ▒ DIRECTION-DEPENDENT:  ▒▒▒▒▒                    │
│    │    ▒   SU(2): TIMELIKE     ▒▒▒▒▒   tau* -> inf      │
│    │    ▒   C2/U1: SPACELIKE    ▒▒▒▒▒   tau* = 2.582     │
│    │    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    │
│    │                                                      │
 \   │  CENSORED: BCS freezes transit at tau=0.22.         /
  \  │  Triple-layered censorship:                        /
   \ │    (1) Energy: V(0.537)/T_0 = 65x                /
    \│    (2) Friction: Gamma_BCS = 4424               /
     │    (3) No trapped surfaces (K_ab traceless)    /
      \                                              /
       \    ROUND METRIC  tau = 0                   /
        \   K = 0.500  |C|^2 = 5/14               /
         \  WCH MINIMUM  R = 2.000               /
          \ DNP-UNSTABLE (all dirs repulsive)    /
           \                                    /
            \                                  /
             \                                /
              \                              /
               \                            /
                \                          /
                 \                        /
                  \                      /
                   \                    /
                    \                  /
                     \                /
                      \              /
                       \            /
                        \          /
                         \        /
                          \      /
                           \    /
                            \  /
                             \/
                             i-
```

### Four Conformal Zones (S49, corrected; overshoot integrated S77)

| Zone | tau Range | Properties | Physical Status |
|:-----|:----------|:-----------|:----------------|
| I | [0, 0.537) | All K >= 0, NEC holds | **Physical universe lives here (tau ~ 0.22, just past the tau_fold=0.19 extremal horizon)** |
| II | (0.537, 1.382) | Mixed-sign K, NEC holds | Never physically reached (triple censorship). **Contains the S77 classical turnaround at tau=1.614** (see below) |
| III | (1.382, inf) | NEC violated in C2 | Never reached; Penrose theorem inapplicable |
| IV | tau -> inf | K -> inf (singularity) | Genuinely singular but dynamically inaccessible |

The physical epoch tau ~ 0.22 sits in Zone I, immediately past the extremal horizon at the van Hove fold tau_fold = 0.19 (the dump / B2-minimum / kappa=0 surface). Zone I is the surviving causal region after the triple censorship is imposed.

### The S77 Overshoot Turnaround (tau = 1.614) — where a runaway modulus would turn back

The censorship picture has a dynamical corollary the 2026-03 version omitted. If the modulus were to overshoot the fold and run up-potential (a counterfactual the censorship layers forbid), it would reach a **classical turning point at tau = 1.614** — the surface Sigma_overshoot where tau_dot = 0 and the energy E_turnaround = V(1.614) (S76 sp-transit T1.4). At this point the curvature is large (K = 53.35, |C|^2 = 35.07, condition number 636) and the fiber anisotropy is maximal (L_1/L_2 = e^{4*1.614} = 643). Crucially, `S77-C5-HESSIAN-OVERSHOOT` (PASS) found **35/35 negative Hessian eigenvalues** at tau=1.614: the Jensen ridge persists through the full overshoot, so the modulus remains confined to the Jensen family — no off-Jensen escape opens up even at the turnaround. The CMPP type there is the static Type D (per the S84/S85 type-invariance theorem; the turnaround is a tau_dot=0 surface, hence static). On the conformal diagram, Sigma_overshoot is a classical turning point deep in Zone II — reachable only by a trajectory that the energy barrier (V(0.537)/T_0 ≈ 65) and BCS friction (Gamma_fric = 4424) already exclude. It is the "far wall" of the censored region: even if a trajectory breached the censorship, it would turn around at 1.614 rather than reach the Kasner singularity at tau→∞. (Diagram N renders the τ-neighborhood of this turnaround.)

### Direction-Dependent Singularity (S49, novel)

The tortoise coordinate tau* converges or diverges depending on internal direction:

| Direction | Behavior | tau* | Singularity Type | Conformal Location |
|:----------|:---------|:-----|:-----------------|:-------------------|
| SU(2) | Contracts (R -> 0) | Diverges | TIMELIKE (i+ analog) | Infinitely far conformally |
| C2 | Expands | 2.582 (finite) | SPACELIKE (r=0 analog) | Finite conformal distance |
| U(1) | Expands | 1.291 (finite) | SPACELIKE | Finite conformal distance |

An anisotropic singularity whose conformal type depends on internal direction -- novel, with no standard GR analog. The volume-preserving constraint (SU(2) contracts as C2/U(1) expand) forces spacelike behavior in expanding directions and timelike in contracting.

### Modulus-Space Conformal-Structure Refinements (S55, S69, S70, S71)

Four post-S53 results sharpen the modulus-space diagram. All are intra-Zone-I refinements of the (t, τ) conformal structure; none alter the zone topology above.

**(a) S55 — viable cosmology WITHOUT a static fixed point (DIAGRAM-55).** The original framework search expected a stabilized modulus minimum (a static fixed point in τ) to anchor late-time cosmology. `CONFORMAL-DIAGRAM-55` (S55, consumes the SCALE-FACTOR-54 a(τ) and Connes-distance data) shows the conformal diagram supports a viable cosmology *without* any such fixed point: the modulus need not settle into a potential minimum for the post-transit FRW history to close — the GGE relic plateau (τ ~ 0.22) plays the role a fixed point would, dynamically rather than as an attractor. The falsifier is "GGE relic failing to reproduce observed physics," not "modulus fails to stabilize." This removes a hidden assumption from Diagram B: the physical epoch is a *dynamical plateau*, not a stationary point.

**(b) S69 — the Penrose-diagram SHAPE from the conformal factor (TRANSIT-69 / FACTOR-69, sp-authored W4-F).** The conformal factor Ω(τ) that compactifies the (t, τ) plane is itself computed from the substrate: `CONFORMAL-FACTOR-TRANSIT-69` derives the shape of the Penrose diagram (the boundary geometry, the location of conformal infinity relative to the transit) directly from Ω(τ) rather than imposing it. The companion `CONFORMAL-ANOMALY-69` (ANOM-69 / EPSH-69, einstein-theorist W4-C) checks the conformal anomaly against the ε_H slow-roll-analog protection — confirming that the conformal-factor transit does not generate an anomaly large enough to destabilize the diagram's boundary structure. Substrate-first reading: the conformal compactification is not a coordinate choice imposed on the modulus space; it is read off from the substrate's own Ω(τ).

**(c) S70/S71 — the time-ordered Penrose sequence and the causal moment map (MAP-71).** Two complementary objects: `s70_penrose_sequence` is a time-ordered sequence of conformal slices through the transit (the diagram "in motion" as τ advances); `CAUSAL-MOMENT-MAP-71` (MAP-71, consumes `s70_penrose_sequence.npz` + `s66_zeta_sa.npz`, depends on c_fabric / τ_fold / v_terminal / a0,a2,a4_fold) builds a moment map of the causal structure — a τ-resolved record of how the causal diamonds (geometric and acoustic) open and close across the fold. Together they make precise the statement that the pre- and post-transit regions are causally disconnected by the supersonic transit (Mach_max = 13.75): the moment map shows the acoustic causal diamond pinching off at the fold while the geometric one stays open. This is the quantitative backbone of the "acoustic white hole" causal disconnect (Diagram C / Diagram J).

These four results live inside Zone I and refine the FRW-square interior of Diagram B; they do not change the zone boundaries (0.537, 1.382), the singularity classification, or the censorship structure.

---

## Diagram C: The Acoustic Metric -- Two Causal Structures

The BLV acoustic metric (S53 W0-1, exact) for phononic excitations in the condensate is:

    ds^2_acoustic = -rho c_s dt^2 + (rho/c_s) a_geom^2 dx^2

This has lapse N = sqrt(rho c_s) and scale factor a_acoustic = a_geom sqrt(rho/c_s). The acoustic null cone has opening angle arctan(c_s / c_geom). With c_Gold = 0.915 M_KK and c_fabric = 209.97 M_KK (c_geom ~ c_fabric for the substrate), the acoustic cone is ~229x NARROWER than the geometric cone.

**Substitution chain — CLAIM A (acoustic cone is narrower than the geometric cone):**

```
Claim: "the acoustic null cone is ~229x narrower (in horizon distance) than the geometric cone"
  Step 1: c_Gold   = 0.915 M_KK         [canonical_constants.py:636; Goldstone sound speed]
  Step 2: c_fabric = 209.97368021 M_KK  [canonical_constants.py:485; substrate fabric speed; c_geom ~ c_fabric]
  Step 3: cone-opening ratio = arctan(c_Gold/c_fabric) / arctan(1)        [opening-angle defn; geom cone at 45deg]
  Step 4: = arctan(0.915/209.97368021) / (pi/4)
        = arctan(0.0043577) / 0.7853982
        ~ 0.0043577 / 0.7853982          [small-angle arctan(x) ~ x]
        ~ 0.005549                       [dimensionless opening-angle ratio]
        => reciprocal horizon-distance scale c_fabric/c_Gold = 209.97368021/0.915 = 229.4794
  Step 5: c_Gold/c_fabric << 1  =>  acoustic opening angle << geometric  =>  acoustic cone NARROWER  [direction]
  Conclusion: the acoustic null cone is 229.48x narrower in horizon distance than the geometric cone.
              [verified in sx_w5_domain_survey.py: c_fabric/c_Gold = 229.4794]
```

### The Bi-Metric Kasparov Decoupling — Two Metrics for Two Field Sectors ([T3], S63/S66 VdD-Hawking, PERMANENT)

The two cones above are NOT merely "two observers looking at the same metric." They are **two distinct effective metrics seen by two distinct field sectors** — a structural result, not a viewpoint. This is the **Scalar-Tensor Kasparov Decoupling** [T3] (atlas-07-permanent-results; baseline-findings-s66), proven exact at linear order in the S63 VdD-Hawking workshop:

```
    U_total  =  1_M  ⊗  U_K        =>        beta_T = 0   exactly at linear order      [T3]
```

The total Bogoliubov transformation factorizes as the identity on the 4D Minkowski factor (1_M) tensored with the internal-space mixing (U_K). Because the 4D factor carries the identity, the TENSOR sector (gravitons, which live on the 4D factor) sees NO Bogoliubov mixing — beta_T = 0 — and therefore experiences NO white hole and NO particle production at linear order. The SCALAR sector (which couples to the internal U_K mixing) sees the full acoustic metric, with its white hole. Concretely:

| Field sector | Effective metric it propagates in | White hole? | Bogoliubov beta |
|:-------------|:----------------------------------|:------------|:----------------|
| **Scalar** (phonon / pair excitations) | **acoustic** metric ds^2_acoustic (with c_Gold sound cone) | YES (one-directional disconnect, S70/S85 W6-1) | beta_S ≠ 0 (Parker pair production, 59.8 pairs) |
| **Tensor** (graviton) | **gravitational** metric g_M (a_2-emergent, c_fabric-scale) | NO | **beta_T = 0 exactly** (linear order) |

The two metrics are related by the horizon-distance identity (H3.2):

```
    r_s = c_s * r_H                                                       (H3.2)
```

— the acoustic (scalar) horizon radius r_s is the geometric (tensor) horizon radius r_H scaled by the sound speed c_s. With c_s = c_Gold << c_fabric, r_s << r_H: the scalar horizon is deep inside the tensor horizon. This is the structural origin of the two-cone picture and the physical reason the scalar and tensor sectors have radically different causal structure.

**Substrate-first framing**: neither metric is fundamental. Both are EMERGENT — the gravitational metric g_M from the a_2 Seeley-DeWitt moment of D_K, the acoustic metric from the BLV construction on the scalar condensate. The bi-metric split is a statement about which emergent metric each excitation sector couples to, derived from the Kasparov-product structure U_total = 1_M ⊗ U_K of the substrate's own Bogoliubov transformation. (This [T3] is also the reason the framework predicts an UNobservable primary tensor signal — see Diagram E/H: r = 3.86e-10, with second-order scalar→tensor conversion r^{(2)} ~ 0.033 as the SOLE tensor mechanism.)

> ![Diagram C — Acoustic vs Geometric Causal Structure](../../figures/penrose/framework-C-acoustic-causality.png)
>
> **TikZ source**: [`figures/penrose/framework-C-acoustic-causality.tex`](../../figures/penrose/framework-C-acoustic-causality.tex) — compile with `xelatex`. Two-panel bi-metric diagram: geometric 45° lightcone on the left, acoustic cone drawn at arctan(1/12) with the true 229× ratio labeled numerically.

```
     GEOMETRIC CAUSAL STRUCTURE          ACOUSTIC CAUSAL STRUCTURE
     (substrate observer)                (phononic observer)

              /\                                 │
             /  \                                │
            /    \  45°                          /\
           /      \                             / |\  0.25°
          /        \                           /  | \
         /  LIGHT   \                         /   |  \
        /   CONE     \                       / ACOUSTIC\
       /              \                     / NULL CONE  \
      /                \                   /    (229x     \
     /                  \                 /    narrower)    \
    ────────────────────────           ─────────────────────────
     \                  /                 \                /
      \                /                   \    229x     /
       \              /                     \ narrower /
        \            /                       \       /
         \          /                         \    /
          \        /                           \ /
           \      /                             │
            \    /                               │
             \  /
              \/

    Geometric causal horizon                Acoustic causal horizon
    d_geom = 2.373e-1 M_KK^{-1}           d_acoustic = 1.034e-3 M_KK^{-1}
    (c_fabric * dt_transit)                 (c_Gold * dt_transit)
```

### Two-Horizon Diagram

Events causally connected in the geometric metric may be causally DISCONNECTED in the acoustic metric. During transit (dt = 0.00113 M_KK^{-1}): d_geom = 0.237 M_KK^{-1} (covers ~10% of SU(3)), d_acoustic = 0.001 M_KK^{-1} (covers 0.04%).

### Second Sound CMB Multipole Ladder (S53 W3-16; CMB-53)

Each of the 6 GL branches defines a different acoustic horizon. The ratio of geometric to branch-specific horizon maps to a CMB multipole. The primary (Goldstone) feature sits at the **pair acoustic horizon multipole**

```
    l_second_sound = pi * (c_fabric / c_Gold) = pi * 229.48 = 720.9      (S53 CMB-53)
```

(this is the `l_pair = 720.9` quoted in the bi-metric workshop; cf. the geometric horizon l_geom = pi * 1 = 3.1 = full sky). The current sound-speed pins are c_Gold = 0.915 M_KK (Goldstone), with the lower acoustic branches c_BA = 0.399 (Anderson-Bogoliubov second sound, S56) and c_L = 0.019–0.032 (Leggett group velocity, S56); the BLV spectral-action acoustic speed is c_s = 0.485 M_KK (the speed entering Mach_max = v_transit/c_s = 6.67/0.485 = 13.75). The ladder below uses the branch group velocities v_g; the primary Goldstone feature is delta C_l ~ 24 muK^2 (below current Planck noise):

```
    l (CMB multipole)
    │
    │
    2223 ─── ──── Higgs-3 (v_g = 0.297, flat band)
    │
    │
    987  ─── ──── Higgs-2 (v_g = 0.669)
    │
    775  ─── ──── Higgs-1 (v_g = 0.851)
    740  ─── ──── Leggett-2 (v_g = 0.891)
    732  ─── ──── Leggett-1 (v_g = 0.901)
    721  ─── ──── Goldstone (v_g = 0.915 = c_Gold)       ← PRIMARY FEATURE
    │                                                        delta C_l ~ 24 muK^2
    │                                                        (below Planck noise)
    0
```

---

## Diagram D: The Mott Regime and Lattice Causal Structure

S53 established N_pair = 1 (exactly), Gi = 0.506, E_J/E_C = 0.818. The system is on the Mott insulator side of the superfluid-insulator transition. The single Cooper pair hops on a 32-cell Voronoi tessellation of SU(3). This is not a continuum spacetime. The "causal structure" is the lattice connectivity.

> ![Diagram D — Mott Lattice & Brillouin Zone Dispersion](../../figures/penrose/framework-D-mott-lattice.png)
>
> **TikZ source**: [`figures/penrose/framework-D-mott-lattice.tex`](../../figures/penrose/framework-D-mott-lattice.tex) — compile with `xelatex`. Panel A shows the anisotropic Josephson hierarchy (J_C2 > J_SU(2) > J_U(1)) as three line weights; Panel B shows the six-branch Brillouin-zone dispersion as the lattice analog of conformal compactification.

```
    THE 32-CELL LATTICE CAUSAL STRUCTURE

    Each cell is a Voronoi domain in 8D SU(3).
    a_cell = 1.596 M_KK^{-1}.   xi_BCS = 0.808 M_KK^{-1}.
    The pair is LOCALIZED within a single cell (xi < a_cell).

    ┌─────┐     ┌─────┐     ┌─────┐     ┌─────┐
    │  1  │─J──│  2  │─J──│  3  │─J──│  4  │─ ─ ...
    │     │ C2 │     │ C2 │     │ C2 │     │
    └──┬──┘     └──┬──┘     └──┬──┘     └──┬──┘
       │J_su2      │J_su2      │J_su2      │J_su2
    ┌──┴──┐     ┌──┴──┐     ┌──┴──┐     ┌──┴──┐
    │  5  │─J──│  6  │─J──│  7  │─J──│  8  │─ ─ ...
    │     │ C2 │     │ C2 │     │ C2 │     │
    └──┬──┘     └──┬──┘     └──┬──┘     └──┬──┘
       │           │           │           │
       :           :           :           :         ... 32 cells total
                                                     in 8D topology

    Hopping parameters:
    ├── J_C2  = 0.933 M_KK  (dominant, C2 directions)
    ├── J_su2 = 0.149 M_KK  (SU(2) directions)
    └── J_u1  = 0.038 M_KK  (U(1) direction)

    Tight-binding "null cone":
    The pair propagates at v_g(K) = dE/dK.
    At K = K_BZ/2:

    Branch      │  v_g (M_KK)  │  Effective c
    ────────────┼──────────────┼─────────────
    Goldstone   │  0.74        │  c_Gold = 0.915
    Leggett-1   │  0.28        │  0.35
    Leggett-2   │  1.40        │  1.73
    Branch-3    │  0.08        │  0.10
    Branch-4    │  4.06        │  5.02
    Higgs-1     │  0.004       │  0.005

    Gamma/omega = 0 EXACT (all branches, all K).
    Bloch states are exact energy eigenstates.
    Coherence length = INFINITE on the lattice.
```

### The Discrete "Penrose Diagram"

On a periodic lattice, the Brillouin zone replaces conformal compactification. Zone boundary K = K_BZ = pi/a is the analog of null infinity; zone center K = 0 is the analog of the singularity (group velocity vanishes for gapped modes).

```
    omega (M_KK)
     ↑
     │
  11.47 ┤──────────────────────── Higgs-1 (nearly flat, BW = 0.002)
     │
     │
   1.41 ┤    ╱──────────────╲     Branch-4 (BW = 1.383)
     │   ╱                    ╲
     │  ╱                      ╲
   0.38 ┤╱────────────────────────╲  Branch-3 (BW = 1.077)
     │
   0.19 ┤    ╱──────────╲          Leggett-2 (BW = 0.794)
   0.14 ┤   ╱────────╲             Leggett-1 (BW = 0.392)
     │  ╱          ╲
   0.00 ┤╱────────────╲            Goldstone (BW = 0.507)
     │                              omega(0) = 0 (Goldstone theorem)
     └───────────────────────→ K
     0        K_BZ/2      K_BZ
              (pi/2a)     (pi/a = 0.716 M_KK)
```

The x-axis (crystal momentum) replaces the spatial coordinate; the y-axis (frequency) replaces time. "Null geodesics" are dispersion curves; the "speed of light" is v_g = domega/dK. No singularity, no horizon -- the lattice is periodic. This is the causal structure of a MOTT INSULATOR: globally connected, locally localized (xi < a_cell), topologically trivial (W = 0, Berry = 0).

---

## Diagram E: The GGE Relic Epoch and Cosmological History

Post-transit GGE with kinetic w = 0.202 produces 78 decelerating FRW e-folds. The deceleration is NOT monotone from the start: per `SCALE-FACTOR-54`, the deceleration parameter q(τ) runs from **q ≈ −0.97 (quasi-de Sitter)** in the early transit to **q ≈ +0.81 (decelerating)** in the GGE epoch — the diagram resembles decelerating FRW *after* a brief quasi-de Sitter phase at the fold, not pure deceleration throughout. Full history:

> ![Diagram E — GGE Relic Epoch & Cosmological History](../../figures/penrose/framework-E-gge-history.png)
>
> **TikZ source**: [`figures/penrose/framework-E-gge-history.tex`](../../figures/penrose/framework-E-gge-history.tex) — compile with `xelatex`. FRW Penrose square with labeled epoch rules: today, radiation era, exflation end (T=0.016 GeV), GGE formation (T=8.32e15 GeV), initial state (tau=0).

```
                 T (GeV)        N_e (acoustic)    Epoch
    ──────────────────────────────────────────────────────
     i+
     ↑
     │
     │  2.35e-13      │  ~106     │  Today (T_CMB = 2.725 K)
     │                │           │
     │  ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
     │                │           │  +25 radiation e-folds
     │                │           │  (standard BBN, recombination)
     │  ─ ─ ─ ─ ─ ─ ─│─ ─ ─ ─ ─ │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
     │                │           │
     │  0.016         │  80.89    │  END OF EXFLATION
     │                │           │  Exflation -> radiation transition
     │                │           │
     │                │           │  GGE RELIC EPOCH
     │                │           │  w = 0.202  (decelerating)
     │                │           │  T proportional to a^{-0.504}
     │                │           │
     │                │           │  Goldstone dispersion omega ~ c_Gold |K|
     │                │           │  dominates thermodynamics
     │                │           │
     │  100           │  63.6     │  Electroweak scale
     │                │           │
     │  75.9          │  61.1     │  QCD scale (Lambda_QCD)
     │                │           │
     │  8.32e15       │  2.92     │  GGE FORMATION
     │                │           │  (= T_acoustic = 0.112 M_KK)
     │                │           │  (GUT scale, zero free parameters)
     │                │           │
     │  ══════════════╪═══════════╪══════════════════════════
     │                │  2.92     │  ACOUSTIC E-FOLD GAIN
     │                │           │  (229x sound speed hierarchy)
     │                │           │
     │                │           │  ┌─────────────────────────┐
     │                │           │  │ Sound speed transition  │
     │                │           │  │ c_fabric -> c_Gold      │
     │                │           │  │ 209.97 -> 0.915 M_KK   │
     │                │           │  │ N_e = +2.72 (dominant)  │
     │                │           │  └─────────────────────────┘
     │                │           │
     │                │  0.17     │  GEOMETRIC CEILING
     │                │           │  (EFOLD-MAPPING-52 theorem)
     │                │           │  Jensen volume-preserving
     │                │           │
     │  ??            │  0        │  INITIAL STATE (tau = 0)
     │                │           │  Hartle-Hawking or equivalent
     │                │           │
     ↓
     i-
```

Standard decelerating FRW with kinetic w = 0.202 (after the early quasi-de Sitter phase, q: −0.97 → +0.81). Particle horizon present, no event horizon. Omega_k grows by 2.00x (opposite of inflation — the framework EXPANDS the curvature scale rather than flattening it). Flatness/horizon problems NOT resolved by this epoch (S53 W2-8); the horizon problem is instead addressed by the acoustic white-hole pre/post causal disconnect (Diagram C / J), not by an inflationary near-de-Sitter phase.

**Substitution chain — CLAIM B (the acoustic observer gains more e-folds than the geometric observer):**

```
Claim: "the acoustic observer gains +2.92 e-folds across the transit; the geometric observer gains +0.17"
  Step 1: a_acoustic = a_geom * sqrt(rho/c_s)        [BLV acoustic scale factor; Diagram C]
  Step 2: N_e = ln(a_final / a_initial)              [e-fold definition]
  Step 3: N_e^acou - N_e^geom = ln( sqrt(rho_f/c_s,f) / sqrt(rho_i/c_s,i) )   [a_geom cancels in the ratio]
  Step 4: dominant term is the sound-speed transition c_fabric -> c_Gold during BCS condensation
        => Delta N_e(sound-speed) = +0.5 * ln(c_fabric/c_Gold)
                                  = +0.5 * ln(229.4794)
                                  = +0.5 * 5.4358
                                  = +2.7179                    [the ~+2.72 acoustic e-folds]
        geometric gain (volume-preserving Jensen, det g_tau = const) ~ +0.17 e-folds   [EFOLD-MAPPING-52 ceiling]
  Step 5: 2.92 (= 2.72 acoustic + ~0.17 baseline) >> 0.17 (geometric)
        => acoustic observer sees a UNIVERSE; geometric observer barely moves           [direction]
  Conclusion: the +2.72 dominant acoustic e-fold gain is +0.5*ln(c_fabric/c_Gold), grounded in the
              c_s transition AND the bi-metric split (only the SCALAR sector, on the acoustic metric,
              experiences this expansion; the TENSOR sector on g_M sees the +0.17 geometric gain).
              [verified in sx_w5_domain_survey.py: c_fabric/c_Gold = 229.4794; 0.5*ln = 2.7179]
```

### The Cosmological Constant — RESOLVED by DILUTION-CC (S66, CC_OOM = 115.5)

The cosmological-history diagram now carries the framework's headline late-time result. The vacuum energy is the **a_0 Seeley-DeWitt moment** (a_0 = 6440 M_KK^{d-4}, the zeroth spectral-action moment) — a DIFFERENT moment than gravity (a_2, Einstein-Hilbert) and Yang-Mills (a_4). The naive vacuum energy overshoots the observed dark-energy density by ~114 orders of magnitude (the cosmological-constant problem). `S66-W1-A-DILUTION-CC` (PASS) closes this gap to **0.01 OOM** via the Volovik tracking-vacuum partition: the substrate's vacuum energy tracks the gravitational background as rho_vac ~ M_Pl^2 H^2 (Volovik Paper 25 §V, Paper 35), giving rho_vac/rho_obs = 1.032. The canonical dilution depth is `CC_OOM = 115.5`. On the conformal diagram this is the reason the late-time epoch has a small positive dark-energy term (w0_FW = −0.918, NOT −1) rather than the catastrophic a_0 overshoot — the a_0 moment is diluted by the tracking partition, not fine-tuned away.

### Reheating — the modulus-decay epoch (two pathways disambiguated)

Between the transit and the radiation era sits the **modulus-decay reheating epoch**, which the 2026-03 version omitted. Two computed pathways:

| Pathway | T_RH | e-folds | Source |
|:--------|:-----|:--------|:-------|
| **Combined modulus-decay channels** (canonical) | **1.70e15 GeV** | N_decay = 63.4 | S77/S76 REHEAT-TEMPERATURE-76 (mack); N_pivot = 3.12 (Hubble exit, ζ freezes) |
| Standard radiation-era matching (alternative) | 1.374e10 GeV | — | S74 DECAY-74 (T_rh = (90/(π²g_*))^{1/4}·√(Γ_mod·M_Pl)) |

The two differ by ~5 OOM because they make different assumptions about the modulus-decay channel structure; the S77 combined-channel value (1.70e15 GeV, near the GUT scale) is the current canonical, with the S74 value retained as the conservative single-channel alternative. The reheating epoch slots into Diagram E between "GGE FORMATION (T = 8.32e15 GeV)" and "END OF EXFLATION (T = 0.016 GeV)."

### Tensor-to-scalar ratio — primary unobservable, second-order the sole signal

The primary tensor-to-scalar ratio is **r = 3.86e-10** (atlas-07 permanent, S44) — unobservable (9.3e7× below BICEP), a direct consequence of the bi-metric [T3] decoupling (beta_T = 0 at linear order, so no primary tensor production). The SOLE tensor mechanism is the **second-order scalar→tensor conversion** r^{(2)} ~ 0.033 (S63/S64): `TENSOR-SCALAR-64` (PASS) gives r = 0.0333 < 0.036 (W3-A agreement 0.25%), arising from the scalar sector sourcing tensors at second order in perturbation theory. These two values annotate Diagram E/H: the primary r is invisible; any detectable tensor signal would be the second-order conversion, with its own duty-cycle suppression.

---

## Diagram F: Petrov Classification and Weyl Eigenvalue Crossings

The Weyl operator on Lambda^2(R^8) has 28 eigenvalues. Branch 27 (C2-C2 bivectors) crosses zero at tau = 0.895 and 1.340, creating a bounded curvature island.

> ![Diagram F — Petrov Classification & Weyl Eigenvalue Crossings](../../figures/penrose/framework-F-petrov-weyl.png)
>
> **TikZ source**: [`figures/penrose/framework-F-petrov-weyl.tex`](../../figures/penrose/framework-F-petrov-weyl.tex) — compile with `xelatex`. Shows branch 27 dipping through zero at tau_1=0.895 and re-crossing at tau_2=1.340; the shaded curvature island is bounded by the two zero-crossings; Petrov type box documents the static Type D theorem.

```
    Weyl eigenvalue (branch 27)
     ↑
     │
  +4 ┤                                              ╱ (grows toward
     │                                             ╱    singularity)
     │                                            ╱
  +2 ┤                           ╱───────────╲   ╱
     │                          ╱  CURVATURE   ╲╱
     │                         ╱    ISLAND
   0 ┤────────────────────────X─────────────────X──────────
     │                     tau_1=0.895      tau_2=1.340
     │  (27 eigs negative)     (1 zero +        (branch 27
     │                          27 negative)     re-crosses)
  -2 ┤
     │                                          Near NEC boundary
     │                                          at tau = 1.382
  -4 ┤
     └──────────────────────────────────────────────────→ tau
     0    0.2   0.4   0.537  0.8   1.0   1.2   1.4

                      ↑                          ↑
                      │                          │
              Geometric phase            NEC violation
              transition                 boundary
              (C2 sect. K = 0)           (C2 Ricci = 0)

    CURVATURE SIGN HIERARCHY:
    K_sect(0.537) < lambda_Weyl(0.895) < Ric(1.382) < singularity(inf)

    Each zero-crossing is BUFFERED from the next by > 0.3 in tau.
    The Weyl tensor buffers the sectional curvature sign change
    from the Ricci sign change. Physics "peels off" in layers.
```

CMPP type is Type D at ALL tau (static) — now PERMANENT across a dense 171-point grid τ∈[0, 1.7] (S85 W6-2) and the `D×8` static signature (S84 W8B-95). The branch-27 zero-crossing is a **SIGNATURE CHANGE on Lambda^2(R^8), NOT a Petrov transition**. This corrects a legacy framing: an early collab note (atlas-sp-collab) labeled τ=0.895 "Weyl = 0, conformal flatness," which would imply a momentary Type O. That reading is SUPERSEDED — it confused a single Λ²-bivector-eigenvalue zero-crossing (one of 28 eigenvalues of the Weyl operator on Λ²) with the vanishing of the full Weyl tensor. The full Weyl scalar **|C|^2 NEVER vanishes** (minimum 3.468 at τ=0, monotone increasing; Type O is impossible because the SU(3) structure constants force |C|^2 > 0). What happens at τ=0.895 and 1.340 is that the C2–C2 bivector eigenvalue (branch 27) passes through zero and back, creating a bounded **curvature island** (branch 27 positive in [0.895, 1.340]) — a transient positive-curvature mode created by C2 expansion, destroyed at NEC violation (τ = 1.382). The CMPP type is D on both sides of, and at, each crossing. The curvature sign hierarchy K_sect(0.537) < λ_Weyl(0.895) < Ric(1.382) < singularity(∞) means the physics "peels off in layers," each buffered from the next by > 0.3 in τ — the Weyl-eigenvalue signature change is buffered from the sectional-curvature sign change, which is buffered from the Ricci sign change.

---

## Diagram G: Horizons, Trapped Surfaces, and Censorship

Volume-preserving Jensen: det(g_tau) = const, so tr(K) = 0. No closed 2-surface has both expansions negative. No trapped surfaces. This is now a **permanent structural result**: the S63 explicit 12D computation `s63_trapped_surface_12d` (SURFACE-12 / D-63) evaluated the expansion scalars of closed 2-surfaces in the full 12D product spacetime and found **theta_int = 0 identically** — the [T5]-class Volume-Preserving No-Trapping result. Because SU(2) contracts (theta_SU2 < 0) exactly as C2/U(1) expand (theta_C2, theta_U1 > 0) under the volume-preserving constraint, the opposite-sign expansions cancel and NO closed 2-surface in the internal space can have both outgoing null expansions negative. Trapped surfaces are STRUCTURALLY impossible on the Jensen family, not merely absent at sampled τ.

> ![Diagram G — Horizons, Trapped Surfaces & Censorship](../../figures/penrose/framework-G-censorship.png)
>
> **TikZ source**: [`figures/penrose/framework-G-censorship.tex`](../../figures/penrose/framework-G-censorship.tex) — compile with `xelatex`. Modulus-space view with three censorship "barriers" (energy, BCS friction, no trapped surfaces) standing between the physical universe at tau~0.22 and the Kasner singularity at tau->inf. Uses the skill's canonical `barrier` style (hatched green-blue).

```
    PENROSE 1965 SINGULARITY THEOREM
    (Paper 04, conditions for geodesic incompleteness)

    CONDITION (1): NEC (R_uv k^u k^v >= 0 for null k)
    ├── HOLDS for tau in [0, 1.382)
    └── FAILS for tau > 1.382 (C2 Ricci eigenvalue < 0)

    CONDITION (2): Non-compact Cauchy surface
    ├── SU(3) IS COMPACT
    └── FAILS STRUCTURALLY (this was noted in meta-analysis S42)
         The compact internal space voids this condition entirely.

    CONDITION (3): Trapped surface exists
    ├── Volume-preserving Jensen: tr(K) = 0
    ├── SU(2) contracts: theta_SU2 < 0
    ├── C2/U(1) expand: theta_C2, theta_U1 > 0
    └── FAILS: opposite-sign expansions prevent trapping.

    VERDICT: 0/3 conditions met. Theorem does NOT apply.
    The singularity at tau -> inf is GENUINE (K -> inf)
    but NOT predicted by the Penrose theorem. It exists
    because the Kasner-type behavior e^{4tau} diverges,
    not because of gravitational focusing.
```

### Triple-Layered Censorship (S49)

The Kasner singularity at tau -> inf is dynamically inaccessible:

```
    LAYER 1: ENERGY BARRIER
    V(0.537)/T_0 = 65.2. tau_turn = 0.088 (from 0), 0.218 (from fold).

    LAYER 2: BCS FRICTION
    Gamma_fric = 4424. v_crit/v_terminal = 8.3x.

    LAYER 3: NO TRAPPED SURFACES
    K_ab traceless (tr K = 0, volume-preserving Jensen).
    theta_int = 0 IDENTICALLY (S63 SURFACE-12, 12D explicit).
    No closed surface has both expansions negative. [T5] permanent.

    Result: tau ~ 0.22 is MAXIMALLY SEPARATED from singularity.
    POTENTIAL BARRIERS + BCS FRICTION play the role of horizons.
```

### The overshoot as the "far wall" of the censored region (S77)

The three censorship layers are *entry* barriers — they prevent a trajectory from leaving the physical epoch (τ ~ 0.22) toward the singularity. The S77 overshoot turnaround (τ = 1.614, Diagram B / N) is the complementary *exit* bound: even a counterfactual trajectory that breached all three layers would not reach the Kasner singularity at τ→∞ — it would hit the classical turning point Sigma_overshoot at τ = 1.614 (E_turnaround = V(1.614); tau_dot → 0) and turn back. `S77-C5-HESSIAN-OVERSHOOT` (PASS, 35/35 negative Hessian eigenvalues) confirms the Jensen ridge persists through the full overshoot — no off-Jensen escape direction opens even at the turnaround, so the volume-preserving (hence no-trapping) condition holds all the way to 1.614. The censored region is thus doubly bounded: triple-layer entry barriers below, the overshoot turnaround above, with the genuine Kasner singularity at τ→∞ dynamically unreachable from either side.

### Asymmetric fold — entry horizon, open exit (S74)

The transit fold is causally asymmetric (S74 open-channel "Asymmetric Fold: Entry Horizon, Open Exit"; `s74_s70_s72_exit_horizon_audit`, AUDIT-74). The supersonic transit (Mach_max = 13.75) creates a one-directional acoustic causal disconnect: ingoing null rays toward the fold stall (the entry horizon, the white-hole surface), while the exit toward the post-transit GGE epoch is open. This is the causal-structure statement of the acoustic white hole — pre-transit and post-transit regions are causally disconnected for the SCALAR sector (which sees the acoustic metric), exactly as the S70/S71 causal-moment-map quantifies (Diagram B refinements). The TENSOR sector (beta_T = 0, no white hole) crosses freely — the asymmetry is sector-dependent, a direct corollary of the bi-metric [T3] split.

---

## Diagram H: The Complete Framework History

The masterpiece diagram. The ENTIRE history from tau = 0 through transit, condensation, destruction, GGE relic, to standard cosmology. Both geometric and acoustic structures are shown.

> ![Diagram H — Complete Framework History (Two-Observer)](../../figures/penrose/framework-H-complete-history.png)
>
> **TikZ source**: [`figures/penrose/framework-H-complete-history.tex`](../../figures/penrose/framework-H-complete-history.tex) — compile with `xelatex`. Two-column diagram: GEOMETRIC observer (left, 0.17 e-folds) vs ACOUSTIC observer (right, 2.92 e-folds). Epoch rules cross both columns; the factor-17x arrow at the transit makes the two-observer asymmetry explicit.

```
    ┌─────────────────────────────────────────────────────────────┐
    │                    COMPLETE FRAMEWORK                       │
    │              CAUSAL-CONFORMAL HISTORY                       │
    │                                                             │
    │   GEOMETRIC OBSERVER               ACOUSTIC OBSERVER       │
    │   (substrate)                       (phonon/pair)           │
    │                                                             │
    │         │                                  │                │
    │   ══════╪══════════════════════════════════╪═══════         │
    │         │  TODAY (T = 2.725 K)             │                │
    │         │  Standard cosmology              │                │
    │         │  13.8 Gyr                        │                │
    │   ══════╪══════════════════════════════════╪═══════         │
    │         │                                  │                │
    │         │  RADIATION ERA                   │                │
    │         │  +25 e-folds                     │                │
    │         │  BBN, recombination              │                │
    │         │                                  │                │
    │   ══════╪══════════════════════════════════╪═══════         │
    │         │                                  │                │
    │   EPOCH 3: GGE RELIC (w = 0.202)          │                │
    │         │                                  │                │
    │         │  N_e^geom = 78                   │  N_e^acou = 78 │
    │         │  (identical in this epoch:        │  (same a(t),   │
    │         │   rho, c_s constant)              │   same H)      │
    │         │                                  │                │
    │         │  T: 8.32e15 GeV -> 0.016 GeV    │                │
    │         │  Particle horizon grows          │                │
    │         │  No event horizon               │                │
    │         │  Flatness: UNRESOLVED           │                │
    │         │                                  │                │
    │   ══════╪══════════════════════════════════╪═══════         │
    │         │                                  │                │
    │   EPOCH 2: CONDENSATE EXISTENCE            │                │
    │         │                                  │                │
    │   2a: PAIR CREATION                        │                │
    │         │  59.8 qp pairs (Parker-type)     │                │
    │         │  Anti-thermal spectrum            │                │
    │         │  r = +0.74 (correlation)          │                │
    │         │                                  │                │
    │   2b: CONDENSATE + TRANSIT                 │                │
    │         │                                  │                │
    │         │  N_e^geom = 0.17   │────────────│N_e^acou = 2.92 │
    │         │  (volume-preserving │            │(229x hierarchy)│
    │         │   Jensen)           │   FACTOR   │                │
    │         │                     │    17x     │                │
    │         │  a_geom barely      │  ACOUSTIC  │ a_acou gains   │
    │         │  changes            │  > GEOM    │ 2.72 e-folds   │
    │         │                     │            │ from c_s change│
    │         │                                  │                │
    │         │  ACOUSTIC NULL CONES 229x NARROWER                │
    │         │  Phonon sees EXPANSION that substrate does not.   │
    │         │                                  │                │
    │   2c: BCS CONDENSATION                     │                │
    │         │  S_inst = 0.069 (from vacuum)    │                │
    │         │  N_pair = 1 (Mott regime)        │                │
    │         │  Speed bump at tau = 0.2015      │                │
    │         │  Stalling: 8.85x (LK overshoot) │                │
    │         │                                  │                │
    │   ══════╪══════════════════════════════════╪═══════         │
    │         │                                  │                │
    │   EPOCH 1: PRE-CONDENSATE FOAM             │                │
    │         │                                  │                │
    │         │  Round SU(3) at tau = 0          │  No acoustic   │
    │         │  K = 0.500, |C|^2 = 5/14        │  metric exists │
    │         │  WCH minimum                    │  (no condensate│
    │         │  DNP-unstable                   │   = no phonon) │
    │         │  c_fabric = 209.97 M_KK         │                │
    │         │  (substrate speed only)          │                │
    │         │                                  │                │
    │         │  12D Planck scale ~ M_KK         │                │
    │         │  M_P_12D = 0.977 M_KK           │                │
    │         │                                  │                │
    │   ══════╪══════════════════════════════════╪═══════         │
    │         │  INITIAL STATE                   │                │
    │         │  (tau = 0, HH or equivalent)     │                │
    │         │                                  │                │
    └─────────────────────────────────────────────────────────────┘
```

### The Central Insight

The geometric observer sees almost nothing (0.17 e-folds, volume-preserving Jensen). The acoustic observer sees a UNIVERSE (2.92 acoustic e-folds + 78 GGE e-folds). **The universe is what a phonon sees when the substrate barely moves.**

---

## Diagram I: Novel and Speculative Diagrams

### I-1: The White Hole Analogy (revised post-S53)

The S39 white hole comparison remains structurally sound but requires revision for N_pair = 1:

> ![Diagram I-1 — Schwarzschild White Hole ↔ Exflation Analogy](../../figures/penrose/framework-I1-white-hole-analogy.png)
>
> **TikZ source**: [`figures/penrose/framework-I1-white-hole-analogy.tex`](../../figures/penrose/framework-I1-white-hole-analogy.tex) — compile with `xelatex`. Side-by-side Schwarzschild Region IV vs exflation transit; uses the skill's canonical `thermal boundary` dashed-teal style to distinguish thermalization from a genuine horizon.

```
    SCHWARZSCHILD WHITE HOLE         EXFLATION TRANSIT (post-S53)
    (Kruskal Region IV)              (N_pair = 1, Mott regime)

              i+                                i+
             / \                               / \
            /   \                             /   \
           / I+  \                           /GIBBS\
          /  null \                         / T=0.113\
         /  infty  \                       /   M_KK   \
        /...........\ ← horizon          /·············\ ← thermalization
       / EVENT       \                   / THERM BNDRY   \
      / HORIZON       \                 / t/t_tr = 5253   \
     / (null, r=2M)    \               /                   \
    |                    |             | GGE (PRODUCT)       |
    |  THERMAL EMISSION  |             | S_ent = 0 EXACT     |
    |  T_H = kappa/2pi   |             | ANTI-THERMAL         |
    |  Planckian spectrum |             | (Parker, r = +0.74) |
    |  S_BH = A/4        |             |                      |
    |                    |             | ONE PAIR (not 59.8   |
    |                    |             |  -- those are         |
    |  INFORMATION LOST  |             |  quasiparticle        |
    |  behind horizon    |             |  excitations)         |
    |                    |             |                      |
     \  PAST HORIZON    /               \ BCS WINDOW         /
      \ (null surface) /                 \ (NO horizon)     /
       \              /                   \                 /
    ////\////////////\////              ════\═══════════/═══
    // PAST SING.    //                 ROUND METRIC (tau=0)
    // r=0, K->inf   //                 K=0.500, REGULAR
    // GENUINE       //                 DNP-UNSTABLE
    ////////////////////                (repulsive, not singular)
```

N_pair = 1 revision: "pair creation zone" produces one quantum of excitation, not a macroscopic state. White hole emits thermally; transit produces an anti-thermal product state (S_ent = 0).

### I-2: The Internal SU(3) Curvature Landscape

SU(3) is Riemannian (no causal structure), but the curvature landscape admits conformal analysis.

> ![Diagram I-2 — Curvature Landscape K(τ)](../../figures/penrose/framework-I2-curvature-landscape.png)
>
> **TikZ source**: [`figures/penrose/framework-I2-curvature-landscape.tex`](../../figures/penrose/framework-I2-curvature-landscape.tex) — compile with `xelatex`. K(tau) Kretschmann scalar plot; three τ landmarks (Schur min, fold, geom. phase trans.) collapsed into one compact "Key τ landmarks" callout; asymptotic K~(1/12)exp(4tau) annotated at the right edge.

```
    K (Kretschner scalar)
     ↑
     │                                                 ╱
     │                                                ╱
     │                                               ╱  K ~ exp(4tau)
     │                                              ╱
     │                                             ╱
     │                                            ╱
  2.0┤                                           ╱
     │                                          ╱
     │                                         ╱
  1.0┤                                        ╱
     │                                       ╱
     │                             ╱────────╱
     │                            ╱
  0.5┤──── ──── ──── ──── ─╱─── ╱
     │   K'(0) = 0        ╱
     │   (Schur)         ╱      K(fold) = 0.535
     │   K(0) = 0.500   ╱       (sub-Planckian by 9 orders)
     │                 ╱
     └────────┬────────┬──────────────────────────→ tau
              0      0.19                1.0
           (round)  (fold/dump)

    Weyl Curvature Hypothesis (WCH):
    |C|^2(0) = 5/14 = MINIMUM (conformally flattest point)
    |C|^2 monotonically increasing (confirmed through tau = 2.0)
    Opposite to 4D gravitational collapse (where Weyl dominates Ricci)
    Here: |C|^2/K ratio DECREASES (Ricci dominance grows)
```

### I-3: The Fock Space Spectral Horizon (revised for N_pair = 1)

The S39 Fock space diagram showed a 256-state Hilbert space with chaotic central sectors and integrable edges. With N_pair = 1, the physical state lives entirely in the 8-dimensional N = 1 sector:

> ![Diagram I-3 — Fock Space Sector Ladder](../../figures/penrose/framework-I3-fock-space.png)
>
> **TikZ source**: [`figures/penrose/framework-I3-fock-space.tex`](../../figures/penrose/framework-I3-fock-space.tex) — compile with `xelatex`. Fock-space sector ladder with integrable/chaotic/dead styles; the N>=2 sectors are grayed-out (pair-repulsive, S_2=-0.131); the N=1 physical sector is highlighted with a bold horizon-color border.

```
    FOCK SPACE CAUSAL STRUCTURE (N_pair = 1, S53)

    N = 0    N = 1       N = 2       N = 3    ...    N = 8
    dim=1    dim=8       dim=28      dim=56          dim=1
             │
             │ ← PHYSICAL
             │   STATE
             │
    ┌───┐   ┌┴──────┐   ┌──────┐   ┌──────┐       ┌───┐
    │ 1 │   │ 8     │   │ 28   │   │ 56   │  ...  │ 1 │
    │   │   │ modes │   │      │   │      │       │   │
    │ P │   │       │   │ G    │   │ I    │       │ P │
    │ o │   │ Brody │   │ O    │   │ n    │       │ o │
    │ i │   │ beta  │   │ E    │   │ t    │       │ i │
    │ s │   │ =0.001│   │      │   │ e    │       │ s │
    │ s │   │ (S53) │   │      │   │ r    │       │ s │
    │ o │   │       │   │      │   │ m    │       │ o │
    │ n │   │ INTEG-│   │CHAO- │   │ e    │       │ n │
    │   │   │ RABLE │   │ TIC  │   │ d    │       │   │
    └───┘   └───────┘   └──────┘   └──────┘       └───┘

    At N_pair = 1: all 8 modes are exact Bloch eigenstates,
    Gamma/omega = 0, six integrability diagnostics PASS.
    N >= 2 sectors are NOT POPULATED (S_2 = -0.131, pair-repulsive).
    The Fock space "horizon" is an ENERGY BARRIER, not causal.
```

### I-4: The Weyl Curvature Hypothesis in 12D

Penrose's WCH states that the Weyl tensor was zero (or near-zero) at the Big Bang and grows through gravitational clumping. In the framework:

> ![Diagram I-4 — Weyl Curvature Hypothesis in 12D](../../figures/penrose/framework-I4-wch-12d.png)
>
> **TikZ source**: [`figures/penrose/framework-I4-wch-12d.tex`](../../figures/penrose/framework-I4-wch-12d.tex) — compile with `xelatex`. |C|^2/K ratio plot starting at 5/7 at tau=0, decreasing through 0.477 at fold, approaching ~0.13 at tau=2; WCH assessment box documents weak-WCH HOLDS / strong-WCH VIOLATED verdict with mirrored left/right callout rhythm.

```
    |C|^2 / K ratio (Weyl fraction of total curvature)

    1.0 ┤
        │
    0.8 ┤
        │
  5/7 ──┤─── ← tau = 0 (round). Weyl is 71.4% of total.
    0.6 ┤      ALREADY LARGE. Not conformally flat.
        │      But this IS the MINIMUM |C|^2.
    0.5 ┤─ ─ ─ ← ratio at tau = 0.19 (fold): 0.477
        │         Ricci GAINS relative to Weyl.
    0.4 ┤
        │      DIRECTION OF INCREASE ────→
        │      (as tau increases, |C|^2 grows
    0.3 ┤       but K grows FASTER because
        │       Ricci terms dominate at large tau)
    0.2 ┤
        │
    0.1 ┤
        │
    0.0 ┤
        └──────────────────────────────────────→ tau
        0     0.19    0.5      1.0     1.5    2.0

    WCH ASSESSMENT:
    ├── |C|^2 at tau=0 is MINIMUM: CONSISTENT with WCH
    ├── |C|^2 monotone increasing: CONSISTENT with WCH
    ├── NOT conformally flat at tau=0: strong WCH violated
    │   (SU(3) structure constants force |C|^2 > 0; topology forbids C=0)
    └── |C|^2/K DECREASING: OPPOSITE to 4D collapse
        (Ricci dominates, not Weyl -- compactification, not focusing)
```

---

## Spectral Dimension and Conformal Structure (S92 — resolves Open Question #7)

The original Open Question #7 asked how the running spectral dimension affects the conformal structure, noting that "a spacetime with running spectral dimension does not have a standard Penrose diagram." The S92 ad-hoc workshop (`s92-adhoc-spectral-dimension-ds-flow-vs-cdt`) resolves this — and the resolution is a lesson in **same-functional-same-scale fair comparison**, not a new horizon.

The spectral dimension is the substrate observable

```
    d_s(sigma) = -2 d ln P(sigma) / d ln sigma,        P(sigma) = Tr exp(-sigma D_K^2)
```

This is ONE function of σ (the diffusion time), but it has TWO physically distinct *windows* that the early framing conflated:

- **σ → 0 (UV) Weyl asymptotic**: `lim_{σ→0} d_s(σ) = 8` on the 8-dimensional SU(3) fiber — the standard Weyl/manifold dimension. (S52 decomposition: d_s^total = d_s^M4 + d_s^SU(3); the SU(3) limit is 8.) This is the dimension of the *internal manifold*, recovered at short diffusion times.
- **windowed `d_s(σ_*)` at the fold**: evaluated at `σ_* = 1.4005 M_KK^{−2}` (the fold's feature scale), `d_s(σ_*) ≡ Φ[P_{D_K}](σ_*)` gives the *windowed* spectral dimension — a DIFFERENT functional value of the SAME P(σ), probing the band structure at the fold rather than the UV manifold.

**The conformal-structure resolution**: there is no obstruction to the Penrose diagram, because the σ→0 Weyl asymptotic (=8) and the windowed `d_s(σ_*)` are distinct functionals of P(σ) and may differ arbitrarily without implying a "running dimension" pathology in the causal structure. The causal/conformal structure is governed by the emergent 4D Lorentzian metric g_M (from a_2), whose dimension is fixed at 4 — the spectral-dimension flow is a property of the *internal* diffusion operator D_K², not of the emergent spacetime's causal cones. A comparison to CDT's dimensional reduction must apply the SAME functional Φ at the SAME scale-type (intermediate-window ↔ intermediate-window): comparing the substrate's σ→0 Weyl asymptotic to CDT's intermediate-window value would be a category error (substituting the lab framework's scale-type for the substrate's). The discriminating sub-quantity is the directly-fitted energy-axis DOS exponent γ_E; the impedance product `Z = ρ_E · v_g` is a CONSISTENCY CHECK (Z = const across the branch family), not a lock.

**Why the standard Penrose diagram survives**: the running of d_s(σ) lives entirely on the internal heat-kernel/diffusion axis. The conformal compactification of the emergent 4D spacetime (Diagrams A, B, E, H) uses g_M, which is 4-dimensional Lorentzian at every τ. The spectral-dimension flow modifies the *matter content* (the effective stress-energy from the internal modes) but not the dimensionality of the conformal boundary — i⁺/i⁻/i⁰/ℐ⁺/ℐ⁻ remain 4D constructs. **Open Question #7 is therefore RESOLVED**: the running spectral dimension is an internal-diffusion property, not a causal-structure obstruction; the diagrams are well-defined.

---

## Synthesis: The Causal Structure of Exflation (current through S93)

### What the Diagrams Collectively Reveal

1. **No event horizons in geometric spacetime — but the fold is an extremal Killing horizon.** Modulus space is flat 1+1D Minkowski with c_τ = 0.447. The singularity is censored by energy barriers + BCS friction (not event horizons); the Penrose 1965 theorem is inapplicable (compact Cauchy surface, no trapped surfaces). REFINEMENT (S85 W6-4, Diagram K): the van Hove fold τ_fold = 0.19 IS a horizon — an *extremal* one (double-root V=V'=0 ⟹ κ=0, T_H=0), thermodynamically null. The physical epoch τ ~ 0.22 sits just past it.

2. **The acoustic spacetime has a one-directional white hole (bi-metric).** The S48 superflow analog horizon was RETRACTED (S49: φ=0, static). But the acoustic metric is NOT horizon-free: S85 W6-1 (Diagram J) re-derived a one-directional acoustic white-hole causal disconnect at the fold, and the bi-metric [T3] Kasparov decoupling (S63/S66) makes it sector-dependent — the SCALAR sector (acoustic metric) sees the white hole and is causally disconnected pre/post transit; the TENSOR sector (gravitational metric, β_T = 0) crosses freely. r_s = c_s·r_H.

3. **Two causal structures are nested, and they are two DISTINCT metrics for two field sectors.** Acoustic null cones are ~229× narrower than geometric (c_fabric/c_Gold = 229.48; CLAIM A chain). This is the bi-metric Kasparov split [T3], PERMANENT: scalars propagate in the acoustic metric, tensors in the a_2-emergent gravitational metric. Events in the geometric causal diamond may be outside the acoustic causal diamond (the basis of the horizon-problem resolution via causal disconnect rather than inflation).

4. **The lattice breaks continuum causal structure.** 32-cell Voronoi tessellation replaces spacetime with a discrete lattice. BZ replaces conformal infinity. The pair is a quantum walker, not a geodesic follower. (Open Question #3 / CF19: whether the lattice→continuum and Akama-Diakonov emergent-metric limits admit a Regge-type conformal completion remains open; S93 W8-7 studies the emergent 3-slices.)

5. **Information flows monotonically.** S: 0 → 3.54 → 6.70 bits. No information LOST (no event horizon). Redistributed within the 256-state Hilbert space. Unitarity preserved. The GGE relic is a product state (S_ent = 0) — the Ordered Veil.

6. **Petrov classification is a PERMANENT type-invariance theorem.** Static: exact Type D. Transit: Type G. Post-freeze: Type D restored. This is now PERMANENT across the `D×8/G×8` signature (S84 W8B-95) and a dense 171-point grid (S85 W6-2, Diagram M). The GGE-during-transit type is Type G (S76 TRANSIT-76), inheriting the dynamic branch. The Weyl-eigenvalue crossings at τ=0.895, 1.340 are signature changes on Λ²(R⁸), NOT type transitions (|C|² never vanishes; Type O impossible). The earlier S49 "Type II" was a Riemannian-signature artifact, corrected by the S50 Lorentzian a_2-reduction.

7. **Censorship without event horizons — doubly bounded.** Triple-layered (energy + friction + no trapped surfaces); BCS dynamics, not gravity, is the censor. The no-trapping is PERMANENT ([T5], S63 SURFACE-12: θ_int = 0 identically). The censored region is doubly bounded: triple-layer entry barriers below (toward the physical epoch), the S77 overshoot turnaround at τ=1.614 above (the far wall). Conformal infinity is regulator-conditional (S85 W6-3, Diagrams L_dS/L_flat: S³ dS vs R×S² flat) but ALWAYS 4D — SU(3) is compact and absent from ℐ. Novel censorship mechanism with no standard GR analog.

8. **The cosmological-constant problem is RESOLVED at the substrate level.** DILUTION-CC (S66): the a_0 vacuum-energy moment is diluted by the Volovik tracking-vacuum partition to within 0.01 OOM of the observed dark-energy density (CC_OOM = 115.5; w0_FW = −0.918). Vacuum energy = a_0, a DIFFERENT spectral moment than gravity (a_2). This is the headline late-time result the causal-history diagrams (E, H) now carry.

9. **The spectral-dimension flow does not obstruct the Penrose diagram.** (S92) The σ→0 Weyl asymptotic (d_s = 8) and the windowed d_s(σ_*) at the fold are distinct functionals of the internal diffusion operator, not a running causal dimension. The emergent 4D Lorentzian g_M is 4D at every τ; the conformal boundary is well-defined.

---

## Open Questions in Causal Structure

1. **The 8D BLV formula.** The acoustic metric was derived in 3+1D. What changes in the full 12D product spacetime? This is the leading source of uncertainty in the e-fold count.

2. **Post-transit acoustic metric existence.** After condensate destruction (P_exc = 1.000), does the acoustic metric continue to exist? The GGE relic has no condensate, so the BLV derivation (which requires a background condensate) may not apply. The GGE quasiparticles may propagate in a different effective metric.

3. **The lattice Penrose diagram.** The discrete "Penrose diagram" (Diagram D) is heuristic. A rigorous conformal compactification of a lattice requires the theory of discrete geometry (Regge calculus or causal set theory). Does the 32-cell tessellation of SU(3) admit a Regge-type conformal completion?

4. **Direction-dependent singularity stability.** The anisotropic singularity (SU(2) timelike, C2/U(1) spacelike) is a novel feature. Is it stable under perturbations away from the Jensen family? The 27 transverse directions in the 28D moduli space could modify the singularity structure.

5. **Trapped surfaces off-Jensen.** [PARTIALLY ADDRESSED — S63, S77] The no-trapped-surface theorem relies on the volume-preserving property (tr K = 0) of the Jensen deformation; off-Jensen deformations that change the volume could in principle create trapped surfaces. The S63 12D computation (SURFACE-12) confirmed θ_int = 0 identically ON the Jensen family ([T5] permanent). The S77 overshoot analysis (`S77-C5-HESSIAN-OVERSHOOT`, 35/35 negative Hessian eigenvalues at τ=1.614) shows the Jensen ridge persists through the full overshoot — no off-Jensen escape direction opens up even at the censored far wall, so the volume-preserving (hence no-trapping) condition is dynamically maintained along the whole physical trajectory. The RESIDUAL open question: a fully general off-Jensen perturbation analysis (the 27 transverse directions in the 28D moduli space) at arbitrary τ has not been exhausted — only the Jensen ridge and the overshoot point are proven confined.

6. **Acoustic horizon during the c_s transition.** [PARTIALLY ADDRESSED — S85 W6-1] The sound speed changes from c_fabric to c_Gold during BCS condensation. S85 W6-1 (Diagram J) formalized the resulting acoustic white hole as a one-directional causal disconnect; the transient-horizon question (whether a moving acoustic horizon sweeps through as c_s passes through intermediate values) is consistent with this one-directional disconnect. The 0D limit (L/ξ = 0.031) suggests no spatial structure supports an extended horizon; the S85 W6-1 result treats the disconnect at the fold rather than a continuum of transient horizons. RESIDUAL: a fully time-resolved c_s(t) sweep with the moving-horizon structure remains a refinement target.

7. **Spectral dimension and conformal structure.** [RESOLVED — S92] See the dedicated "Spectral Dimension and Conformal Structure" section above. The running d_s(σ) is a property of the internal diffusion operator D_K² (σ→0 Weyl asymptotic = 8 on SU(3); windowed d_s(σ_*) at σ_*=1.4005 is a distinct functional), NOT of the emergent 4D Lorentzian causal structure. The Penrose diagram is well-defined because g_M is 4D Lorentzian at every τ; the spectral-dimension flow modifies matter content, not the dimensionality of the conformal boundary. Fair comparison to CDT applies the same functional Φ at the same scale-type.

8. **Emergent metric and the lattice→continuum completion.** [OPEN — CF19, S47/S93] The Akama-Diakonov emergent-metric channel (CF19, S47 Volovik 3.1: analog horizon from condensate) and the lattice→continuum Regge-completion question (Open Q#3) remain open. S93 W8-7 (substrate-mode-localization-emergent-3-slices) studies how localized substrate modes give rise to emergent 3-slices — a step toward the emergent-metric completion, but the full Akama-Diakonov derivation of g_M from condensate dynamics (rather than from the a_2 spectral moment) is not closed.

---

*Supersedes S39 Penrose diagrams. Catalog A–I authored post-S53; comprehensively expanded through Session 93 (Session-X W5): bi-metric Kasparov decoupling ([T3]), CMPP type-invariance theorem (S84/S85), DILUTION-CC, reheating, second-order tensor, S69–S71 conformal diagrams, J–N integration, spectral-dimension/CDT resolution. All numbers computed and traced to canonical constants / permanent theorems / gate verdicts; all boundaries classified. Classification: GEOMETRIC.*


---

## Diagrams J–N: The S85 W6 Conformal-Structure Suite + S77 Overshoot (integrated 2026-05-25)

Following Session 85 W6-1..W6-5 (and the S77 overshoot), five additional diagram families J–N were computed. They were originally bolted on as an append; **they are now integrated into the catalog and the synthesis** — each J–N diagram is a τ-localized or regulator-conditional refinement of one of the core diagrams A–I, and the table below states the interrelation explicitly. Each is labeled per output-standards (full boundary set {i⁺, i⁻, i⁰, ℐ⁺, ℐ⁻, horizons, singularities, shading}), cross-references its producing gate, and carries a skill-compliant TikZ stub (full canonical TikZ via `.claude/skills/penrose-diagram/SKILL.md`; these five are ASCII/TikZ-stub only — no rendered .png/.pdf yet, flagged for a future render pass).

### J–N ↔ A–I interrelation map (the integration)

| Diagram | What it refines | Parent diagram(s) | Synthesis point it sharpens |
|:--------|:----------------|:------------------|:----------------------------|
| **J** — Acoustic White Hole Causal Disconnect (S85 W6-1) | the one-directional acoustic disconnect at the fold (Mach > 1 ergoregion) | **C** (acoustic bi-metric), **G** (asymmetric fold) | #2 "no horizons in acoustic spacetime" → REFINED: there IS a one-directional white-hole disconnect for the scalar sector |
| **K** — Extremal Horizon at τ_dump (S85 W6-4) | the κ=0, T_H=0 Killing horizon at the fold (double-root V=V'=0) | **B** (modulus space), **G** (censorship) | #7 "censorship without horizons" → REFINED: the fold IS an extremal (thermodynamically null) horizon |
| **L_dS / L_flat** — Regulator-Conditional ℐ⁺ (S85 W6-3) | the asymptotic conformal boundary under 5 regulators (S³ dS vs R×S² flat) | **A** (12D product), synthesis #7 | the "SU(3) absent from ℐ" invariant → SHARPENED: ℐ⁺ is regulator-conditional but ALWAYS 4D |
| **M** — CMPP Dense-Grid Transit (S85 W6-2) | the 171-point dense-grid confirmation of static-D/dynamic-G | **A** (12D product), **F** (Petrov/Weyl) | #6 "Petrov classification trivial" → ELEVATED to a PERMANENT type-invariance theorem |
| **N** — Overshoot Turnaround at τ=1.614 (S77) | the classical turning point / far wall of the censored region | **B** (modulus zones), **G** (censorship) | #7 censorship → REFINED: doubly-bounded (entry barriers + overshoot exit bound) |

The five diagrams below retain their per-diagram boundary-label blocks and TikZ stubs. **The "append-only, does not modify A–I" caveat is RETIRED**: J–N are now first-class members of the catalog, woven into the synthesis (points #2, #6, #7) and the open-questions update.

## Diagram J: Acoustic White Hole Causal Disconnect (S85 W6-1)

**tau-slice**: tau in [tau_fold - 0.05, tau_fold + 0.05]
**Sources**: W6-1 PASS, s85_w6_acoustic_white_hole_formal.npz
**Causal structure**: one-directional WH disconnect (post-fold ingoing null stalls at tau_H+)

**Boundary labels**:
- i+: True
- i-: True
- i0: True
- I+: True
- I-: True
- Horizons: ['tau_H+', 'tau_H-']
- Singularities: none (censored)
- Shaded region(s): supersonic ergoregion (Mach > 1)

**TikZ source** (skill-compliant stub; full TikZ via `/penrose-diagram` skill):

```latex
\begin{tikzpicture}[scale=1.5]
  % Diagram J: Acoustic White Hole Causal Disconnect (S85 W6-1)
  \draw[thick] (-1,0) -- (0,1) -- (1,0) -- (0,-1) -- cycle;     % diamond
  \node at (0,1.1) {$i^+$}; \node at (0,-1.1) {$i^-$};
  \node at (1.1,0) {$i^0$}; \node at (-1.1,0) {$i^0$};
  \node at (0.6,0.6) {$\mathcal{I}^+$}; \node at (-0.6,0.6) {$\mathcal{I}^+$};
  \node at (0.6,-0.6) {$\mathcal{I}^-$}; \node at (-0.6,-0.6) {$\mathcal{I}^-$};
\end{tikzpicture}
```

---

## Diagram K: Extremal Horizon at tau_dump (S85 W6-4)

**tau-slice**: modulus-space 2D at tau = tau_dump = 0.19
**Sources**: W6-4 PASS, s85_w6_extremal_horizon_formal.npz
**Causal structure**: Killing horizon with double-root V(tau_dump) = V'(tau_dump) = 0; T_H = 0

**Boundary labels**:
- i+: True
- i-: True
- i0: True
- I+: True
- I-: True
- Horizons: ['Sigma_dump (kappa = 0, extremal)']
- Singularities: none (censored)
- Shaded region(s): none (extremal horizon is thermodynamically null)

**TikZ source** (skill-compliant stub; full TikZ via `/penrose-diagram` skill):

```latex
\begin{tikzpicture}[scale=1.5]
  % Diagram K: Extremal Horizon at tau_dump (S85 W6-4)
  \draw[thick] (-1,0) -- (0,1) -- (1,0) -- (0,-1) -- cycle;     % diamond
  \node at (0,1.1) {$i^+$}; \node at (0,-1.1) {$i^-$};
  \node at (1.1,0) {$i^0$}; \node at (-1.1,0) {$i^0$};
  \node at (0.6,0.6) {$\mathcal{I}^+$}; \node at (-0.6,0.6) {$\mathcal{I}^+$};
  \node at (0.6,-0.6) {$\mathcal{I}^-$}; \node at (-0.6,-0.6) {$\mathcal{I}^-$};
\end{tikzpicture}
```

---

## Diagram L_dS: Regulator-Conditional I+ (dS S^3, S85 W6-3): cutoff/heat/dim

**tau-slice**: asymptotic r -> inf under 3 regulators giving Lambda_eff > 0
**Sources**: W6-3 PASS, s85_w6_conformal_infinity_bifurcation.npz
**Causal structure**: asymptotically de Sitter; I+/I- spacelike S^3

**Boundary labels**:
- i+: True
- i-: True
- i0: True
- I+: S^3 spacelike (de Sitter)
- I-: S^3 spacelike (de Sitter)
- Horizons: ['cosmological horizon (de Sitter)']
- Singularities: none (censored)
- Shaded region(s): none

**TikZ source** (skill-compliant stub; full TikZ via `/penrose-diagram` skill):

```latex
\begin{tikzpicture}[scale=1.5]
  % Diagram L_dS: Regulator-Conditional I+ (dS S^3, S85 W6-3): cutoff/heat/dim
  \draw[thick] (-1,0) -- (0,1) -- (1,0) -- (0,-1) -- cycle;     % diamond
  \node at (0,1.1) {$i^+$}; \node at (0,-1.1) {$i^-$};
  \node at (1.1,0) {$i^0$}; \node at (-1.1,0) {$i^0$};
  \node at (0.6,0.6) {$\mathcal{I}^+$}; \node at (-0.6,0.6) {$\mathcal{I}^+$};
  \node at (0.6,-0.6) {$\mathcal{I}^-$}; \node at (-0.6,-0.6) {$\mathcal{I}^-$};
\end{tikzpicture}
```

---

## Diagram L_flat: Regulator-Conditional I+ (flat R x S^2, S85 W6-3): zeta/PV

**tau-slice**: asymptotic r -> inf under 2 regulators giving Lambda_eff = 0
**Sources**: W6-3 PASS, s85_w6_conformal_infinity_bifurcation.npz
**Causal structure**: asymptotically Minkowski; I+/I- null R x S^2

**Boundary labels**:
- i+: True
- i-: True
- i0: True
- I+: R x S^2 null (Minkowski)
- I-: R x S^2 null (Minkowski)
- Horizons: none
- Singularities: none (censored)
- Shaded region(s): none

**TikZ source** (skill-compliant stub; full TikZ via `/penrose-diagram` skill):

```latex
\begin{tikzpicture}[scale=1.5]
  % Diagram L_flat: Regulator-Conditional I+ (flat R x S^2, S85 W6-3): zeta/PV
  \draw[thick] (-1,0) -- (0,1) -- (1,0) -- (0,-1) -- cycle;     % diamond
  \node at (0,1.1) {$i^+$}; \node at (0,-1.1) {$i^-$};
  \node at (1.1,0) {$i^0$}; \node at (-1.1,0) {$i^0$};
  \node at (0.6,0.6) {$\mathcal{I}^+$}; \node at (-0.6,0.6) {$\mathcal{I}^+$};
  \node at (0.6,-0.6) {$\mathcal{I}^-$}; \node at (-0.6,-0.6) {$\mathcal{I}^-$};
\end{tikzpicture}
```

---

## Diagram M: CMPP-Dense-Grid Transit Consolidated Diagram (S85 W6-2)

**tau-slice**: dense 171-point grid tau in [0, 1.7]
**Sources**: W6-2 PASS, s85_w6_cmpp_dense_grid.npz
**Causal structure**: Type D static / Type G dynamic invariant on 171-point dense grid

**Boundary labels**:
- i+: True
- i-: True
- i0: True
- I+: True
- I-: True
- Horizons: ['tau_fold acoustic WH (from W6-1)', 'tau_dump extremal (from W6-4)']
- Singularities: none (censored)
- Shaded region(s): Type D static throughout; Type G dynamic throughout

**TikZ source** (skill-compliant stub; full TikZ via `/penrose-diagram` skill):

```latex
\begin{tikzpicture}[scale=1.5]
  % Diagram M: CMPP-Dense-Grid Transit Consolidated Diagram (S85 W6-2)
  \draw[thick] (-1,0) -- (0,1) -- (1,0) -- (0,-1) -- cycle;     % diamond
  \node at (0,1.1) {$i^+$}; \node at (0,-1.1) {$i^-$};
  \node at (1.1,0) {$i^0$}; \node at (-1.1,0) {$i^0$};
  \node at (0.6,0.6) {$\mathcal{I}^+$}; \node at (-0.6,0.6) {$\mathcal{I}^+$};
  \node at (0.6,-0.6) {$\mathcal{I}^-$}; \node at (-0.6,-0.6) {$\mathcal{I}^-$};
\end{tikzpicture}
```

---

## Diagram N: Post-S77 Overshoot Turnaround at tau = 1.614 (S77 overshoot)

**tau-slice**: tau neighborhood of turnaround point tau = 1.614
**Sources**: S77 overshoot turnaround; MEMORY.md tau_overshoot = 1.614
**Causal structure**: Petrov Type D static (per W6-2 dense-grid confirmation); classical turning point

**Boundary labels**:
- i+: True
- i-: True
- i0: True
- I+: True
- I-: True
- Horizons: ['Sigma_overshoot (classical turning point of modulus evolution)']
- Singularities: none (censored)
- Shaded region(s): high-K, |C|^2 = 35.07, condition number 636

**TikZ source** (skill-compliant stub; full TikZ via `/penrose-diagram` skill):

```latex
\begin{tikzpicture}[scale=1.5]
  % Diagram N: Post-S77 Overshoot Turnaround at tau = 1.614 (S77 overshoot)
  \draw[thick] (-1,0) -- (0,1) -- (1,0) -- (0,-1) -- cycle;     % diamond
  \node at (0,1.1) {$i^+$}; \node at (0,-1.1) {$i^-$};
  \node at (1.1,0) {$i^0$}; \node at (-1.1,0) {$i^0$};
  \node at (0.6,0.6) {$\mathcal{I}^+$}; \node at (-0.6,0.6) {$\mathcal{I}^+$};
  \node at (0.6,-0.6) {$\mathcal{I}^-$}; \node at (-0.6,-0.6) {$\mathcal{I}^-$};
\end{tikzpicture}
```

---

