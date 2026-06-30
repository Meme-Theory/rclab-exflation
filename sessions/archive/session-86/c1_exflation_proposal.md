# C.1 Proposal — Exflation Class

**Author**: volovik-superfluid-universe-theorist
**Date**: 2026-04-26
**Source**: canonical_constants.py (1603 lines, full read in chunks); canonical_classes.py (650 lines, schema + fold/CC/KK/Higgs/alpha_s exemplars).
**Substrate framing**: per `.claude/rules/phononic-framing.md`. The Exflation class is the WHOLE substrate cosmogenesis process — pre-fold tau cascade, fold transit, post-fold GGE relic, effacement-residual leakage. NOT inflation. NOT a Big Bang singularity. The acoustic white hole.

---

## Class metadata

```python
EXFLATION_CLASS = {
    "id": "Exflation",
    "name": "Exflation — substrate cosmogenesis (acoustic white hole)",
    "level": 0,
    "parent_id": None,
    "description": (
        "The framework's cosmogenesis process end-to-end: the Jensen "
        "deformation parameter tau cascading from an unstable maximum at "
        "tau=0 through the van-Hove fold (tau_fold=0.19) into the post-fold "
        "GGE relic plateau. Replaces inflation with a first-order phase "
        "transition driven by the spectral action gradient dS/dtau=+58,673; "
        "replaces the Big Bang singularity with a supersonic transit "
        "(Mach=13.75) of the modulus through the fold. The eigenvalue "
        "spectrum of D_K reorganizes at the fold; what cosmologists call "
        "'particle creation' IS that reorganization — n_pairs=59.8 "
        "Bogoliubov quasiparticle pairs per Parker mode, P_exc_kz=1 "
        "exactly. Post-fold dynamics are an acoustic white hole: pre-/"
        "post-fold causally disconnected by the supersonic flow, with "
        "impedance Gamma_effacement=0.99970 transmitting structure and "
        "the (1-Gamma)=3e-4 residual constituting dark-energy-like "
        "leakage. Class members span the substrate's pre-condition "
        "constants (sound speeds, vacuum-floor instability), the "
        "transit-event quantities (fold-tagged S_fold, dS_fold, H_fold, "
        "v_terminal, dt_transit), the consequence quantities (n_pairs, "
        "Bog occupation, GGE acoustic temperature, Leggett mode), and "
        "the observational anchors that cosmology DERIVES from this "
        "process (n_s framework, w_0_FW, e-fold count N_pivot)."
    ),
    "seed_session": "S38",
}
```

**Seed-session reasoning**: S38 is when the transit paradigm was crystallized — Kibble-Zurek excitation P_exc_kz=1, the GGE relic's permanence theorem, the 59.8-pair Parker production count, and the H_fold / v_terminal / dt_transit kinematic triple all landed in S38 (s38_kz_defects, s38_attempt_freq). Earlier sessions (S12 phi_paasch, S22 Pomeranchuk) discovered substrate elements; later sessions (S58 I-CC-YOU, S64 BLV) refined the post-fold GGE thermodynamics; but S38 is the moment the *process* — the cascade-fold-relic story end-to-end — was first formulated as a unified narrative. The fold class (seed S38) and Exflation class share this seed but cover different scopes: fold = the geometric event at tau=0.19; Exflation = the WHOLE cascade including pre- and post-fold dynamics.

---

## Member constants — PRIMARY (16)

The PRIMARY membership level comprises constants WITHOUT WHICH THE CLASS CANNOT BE DESCRIBED. The Exflation story has four irreducible chapters: (i) the substrate driver (gradient + curvature of the spectral action at the fold), (ii) the supersonic-transit kinematics (Mach number, terminal velocity, transit duration), (iii) the Parker/Kibble-Zurek production (excitation probability, pair count, Bogoliubov occupation), (iv) the post-fold relic (GGE acoustic temperature, effacement impedance, framework EOS). Removing any of these collapses the narrative.

| Constant | Comment / why PRIMARY |
|:---------|:----------------------|
| `tau_fold` | Jensen-deformation locus of the van-Hove fold (= 0.19). The class is *named after* this transit; without tau_fold there is no event to describe. |
| `dS_fold` | Spectral action gradient at the fold (= +58,672.80). THIS is the substrate driver — what cosmologists call the "inflaton field" in container language. The cascade is irreversible because dS/dtau is enormous and one-signed at fold. |
| `S_fold` | Spectral action at the fold (= 250,360.7). The action evaluation point at which the cascade is registered; sets the absolute energy scale of the substrate cosmogenesis event. |
| `Mach_max_framework` | Mach number at the fold (= 13.75). The transit is supersonic — this is the *defining* property that distinguishes Exflation from slow-roll inflation and produces the acoustic white hole. NOT a slow-roll regime. |
| `v_terminal` | Terminal velocity of the modulus (= 26.545 in M_KK units). The kinematic state that the substrate reaches at the fold; sets the Mach number against c_fabric. |
| `dt_transit` | Transit duration (= 1.130e-3 M_KK^{-1}, S38). The fold event is impulsive on this timescale — sets the Kibble-Zurek freezing window. Without dt_transit the "speed" of the fold is ill-defined. |
| `H_fold` | Hubble parameter at the fold (= 586.5 in M_KK units). The expansion rate the substrate's eigenvalue spectrum experiences during the transit; sets the horizon scale at which Bogoliubov modes get squeezed. |
| `P_exc_kz` | Kibble-Zurek excitation probability at the fold (= 1.0 exactly). EVERY mode is excited — the impulsive transit is so fast that no Landau-Zener adiabaticity protects any mode. This is the substrate analog of Parker pair production saturation. |
| `n_pairs` | Bogoliubov quasiparticle pairs from transit (= 59.8). The post-fold GGE relic IS this many pairs of excitations, frozen into the eigenvalue spectrum reorganization. The "reheating" output of substrate cosmogenesis. |
| `n_Bog` | Bogoliubov fraction per mode (= 0.9986). Fine-grained per-mode occupation of the post-fold relic; complements n_pairs (total) with the per-mode density. PRIMARY because it pins the GGE distribution shape, not just its norm. |
| `T_acoustic` | GGE acoustic temperature (= 0.112 M_KK). The relic's effective acoustic temperature on the substrate — the post-fold thermal-like signature from a system that NEVER thermalized (algebraic GGE permanence per S38). |
| `Gamma_effacement` | Acoustic-white-hole impedance-transmission coefficient (= 0.99970). Quantifies the asymmetric causal disconnection across the fold; (1-Gamma)=3e-4 is the IR leakage that constitutes the framework's dark-energy-like residual. |
| `c_fabric` | Substrate sound speed (= 209.97). PRECONDITION-ROLE candidate (see role-taxonomy flag below). The transit being supersonic is *defined relative to* c_fabric; the Mach number is v/c_fabric. PRIMARY because the Exflation event is supersonic-by-definition, and c_fabric is the supersonic referent. |
| `c_BLV` | Brillouin-Landau-Vortex post-fold scalar sound speed (= 0.485). The GGE-relic phonon sector's effective sound speed; distinct from c_fabric (substrate-level) and c_Gold (Goldstone). PRIMARY for the post-fold chapter of the cascade. |
| `w0_FW` | Framework dark-energy equation-of-state w_0 (= -0.918, Volovik vacuum + effacement). The post-fold cosmological state's CC observable — the substrate's residual EOS as measured by external cosmology. The OUTPUT observable of Exflation. |
| `n_s_framework` | Framework scalar spectral index at CMB pivot (= 0.9561). The first-derivative observable of the post-fold relic's correlation structure; how the substrate's frozen-in interference pattern is registered by CMB. |

---

## Member constants — DERIVED (8)

The DERIVED level comprises algebraic/definitional consequences of the PRIMARY members. Each entry below is a quantity whose value is determined ONCE the PRIMARY members are pinned.

| Constant | Comment / derivation chain |
|:---------|:----------------------|
| `d2S_fold` | Curvature of the spectral action at the fold (= 317,862.85). Definitional second derivative whose role is to characterize the *width* of the fold transit; algebraically downstream of S_fold and tau_fold parametrization. |
| `Z_fold` | Gradient stiffness at fold (= 74,730.76). The G_DeWitt-weighted gradient term; combines dS_fold + d2S_fold + G_DeWitt into a single moduli-space stiffness. Definitionally derivable. |
| `omega_tau` | Transit frequency d(tau)/dt (= 8.27 in M_KK units). Algebraically tied to v_terminal and the modulus mass; the "rate of fold approach" inferred from the transit kinematics. |
| `omega_att` | Attractor frequency of the post-fold modulus (= 1.430). Geometrically determined by the curvature of the spectral action manifold at the post-fold attractor — definitionally downstream of the fold geometry. |
| `E_exc_ratio` | Excitation-to-condensation ratio (= 443.0). E_exc / |E_cond|, the Schwinger-instanton-duality ratio that measures the post-fold reorganization energy scale relative to the pre-fold pairing scale. Definitionally a ratio. |
| `E_exc` | Total excitation energy from BCS transit quench (= 60.625 M_KK = E_exc_ratio * |E_cond|). DERIVED: the product of the ratio and the pre-existing condensation energy; the substrate's "reheating" energy budget. |
| `T_compound` | Microcanonical post-fold compound temperature (= E_exc / 8 in M_KK units). Definitionally the per-mode excitation energy across the 8 BCS Fock-space modes; the temperature that the GGE relic *would* have if it could thermalize. |
| `N_pivot` | CMB pivot e-fold count on substrate (= 64.08 = 55 + ln(c/c_s)). Algebraic correction to the LCDM 55-e-fold figure: substrate horizon-crossing is bounded by c_s, NOT c, lifting the count by ln(c/c_s)=9.08. The MAPPING from substrate cosmogenesis to CMB pivot. |

---

## Member constants — RELATED (10)

The RELATED level comprises constants that participate in the Exflation story but are NOT defining of it — they are upstream / downstream / cross-cutting quantities whose primary identity sits in another class.

| Constant | Comment / why RELATED but not native |
|:---------|:----------------------|
| `phi_paasch` | Paasch spectral ratio at s=0.15 (= 1.531580, PROVEN to machine epsilon, S12). Substrate-geometric anchor pre-dating Exflation; the substrate's residue identity. RELATED because the fold geometry inherits from this, but phi_paasch is a static substrate property, not an Exflation-process quantity. |
| `m_tau` | Modulus mass at fold (= 2.062 in M_KK units). Sets the inertial response of the substrate to the dS_fold gradient; appears in the cascade equations but is a static mass scale, not a cascade quantity. |
| `Q_Leggett` | Leggett mode quality factor (= 6.7e5, S50). The substrate has a Leggett mode that becomes a long-lived dark-matter candidate post-fold; the QF tells us the relic is exceptionally undamped. RELATED to Exflation as a downstream-survivor quantity. |
| `T_BCS` | BCS canonical temperature (= 0.640). Substrate-pairing temperature scale; the BCS condensate exists pre-fold and partially survives the transit. RELATED because it pre-conditions the cascade but isn't a cascade quantity per se. |
| `T_c_BCS` | BCS critical temperature (= 0.083). Post-fold transition scale; below this, residual pairing reconstitutes. RELATED as a thermal landmark for the post-fold relic. |
| `kappa_BCS` | BCS surface-gravity analog (= 4.019, S69). The substrate's analog of the BH horizon surface gravity, applied at the fold's acoustic-white-hole horizon. RELATED to Exflation because it characterizes the white-hole side. |
| `tau_phase_trans` | Geometric phase transition at C^2 sectional K=0 (= 0.53723065, S48). A SECOND tau-landmark beyond tau_fold — the substrate has further geometric structure post-fold. RELATED as a downstream geometric event. |
| `tau_overshoot` | Overshoot turnaround at K=53.35 (= 1.614, S77). Post-fold modulus dynamics' first turnaround. RELATED as a kinematic landmark of the post-fold cascade. |
| `v_crit` | Censorship critical velocity (= 219.3). Above v_crit, the substrate dynamics enter an analog cosmic-censorship regime. RELATED because the transit *just barely* satisfies v_terminal < v_crit. |
| `eps_H_W6` | Slow-roll bound from S80 dS/dtau at fold (= 0.02163). Phenomenological Hubble-slow-roll proxy applied as an NLO-margin cap; an *interface* parameter between substrate dynamics and slow-roll-equivalent observables. RELATED, not native — it lives between Exflation and the LCDM-mapping layer. |

---

## Role-taxonomy flags (3)

Three constants surface friction with the PRIMARY/DERIVED/RELATED schema:

- **`c_fabric`** — proposed role: `PRECONDITION` (currently classed as PRIMARY in this proposal, RELATED in the existing fold class).
  Reason: c_fabric is the substrate sound speed; it exists IN THE SUBSTRATE before any cascade dynamics begin. PRIMARY (this class) overstates: the cascade does not *define* c_fabric. RELATED understates: without c_fabric, the Mach=13.75 supersonic-transit defining property is meaningless. The constant is a substrate-geometric input the cascade *consumes* to define its supersonic character.
  Suggested addition to schema: `PRECONDITION` role — a substrate property the class's PRIMARY members compute against but do not produce. Distinct from PRIMARY (defining quantity), DERIVED (algebraic consequence), and RELATED (cross-cutting). Could fold into PRIMARY if the schema explicitly notes "PRIMARY includes preconditions whose value is irreducibly required by the class's defining equations."

- **`n_pairs`** — currently proposed PRIMARY (this class), DERIVED (fold class).
  Reason: n_pairs=59.8 is a CONSEQUENCE of the transit (Parker production from P_exc_kz=1 over 60 modes weighted by Bogoliubov amplitudes) but is itself the headline Exflation observable for the post-fold relic — the count of excitations the cascade *produces*. DERIVED (relative to fold mechanics) and PRIMARY (relative to the post-fold relic) are both correct depending on viewpoint. The CONSEQUENCE role would mean: a quantity produced BY the class's process but that DEFINES the post-event state.
  Suggested addition to schema: `CONSEQUENCE` role — a quantity the class produces and that becomes a downstream-class PRIMARY but is not itself a defining input. Distinguishes process-output from process-driver. Could be left as PRIMARY in Exflation (post-fold relic chapter is part of Exflation) and DERIVED in fold (where it is downstream of fold geometry alone).

- **`w0_FW` / `n_s_framework`** — proposed PRIMARY (this class).
  Reason: These are observational outputs MEASURED post-cascade by external cosmology — they are not internal substrate quantities the cascade dynamics consume. PRIMARY-by-being-the-headline-observable is plausible (the whole point of the class is what it predicts), but PRIMARY-as-defining-the-class is overstated (the class is defined by its dynamics; w0_FW is what the dynamics PRODUCE).
  Suggested addition to schema: `OBSERVABLE_OUTPUT` role — a quantity external cosmology measures that is the class's PRIMARY testable consequence. Distinguishes cosmological-prediction from substrate-internal quantity. In the absence of this role, leave as PRIMARY since the Exflation class's defining purpose IS to predict these.

If the schema is to remain three-level (PRIMARY/DERIVED/RELATED), the proposal above stands. If the orchestrator wants finer granularity, the three flagged constants would migrate to PRECONDITION (c_fabric), CONSEQUENCE (n_pairs), and OBSERVABLE_OUTPUT (w0_FW, n_s_framework). My recommendation is to KEEP the three-level schema for now — adding more roles complicates the visualizer and MCP query semantics without (yet) demonstrated need across multiple classes. Re-evaluate if a SECOND class (e.g., a future "Effacement" or "GGE-relic" class) hits the same friction.

---

## Overlap with existing classes

Exflation is a process-class that transits THROUGH the KK scale, INTO the post-fold CC vacuum, while also producing GGE relics whose spectral signature dominates the CMB observables. Substantial overlap is expected and structural.

| Constant | Existing class membership | Role in existing class | Role in Exflation |
|:---------|:--------------------------|:----------------------|:------------------|
| `tau_fold` | fold | PRIMARY (defining: the fold IS this tau locus) | PRIMARY (defining: the cascade IS through this tau) |
| `S_fold` | fold | PRIMARY (action at the fold) | PRIMARY (action at the cascade event) |
| `dS_fold` | fold | PRIMARY (drives the geometric event) | PRIMARY (drives the cascade) |
| `d2S_fold` | fold | PRIMARY (curvature of action at fold) | DERIVED (consequence of pinning S_fold + tau parametrization) |
| `Z_fold` | fold | DERIVED (gradient stiffness) | DERIVED (same derivation) |
| `H_fold` | fold | DERIVED | PRIMARY (the substrate's expansion rate during cascade — defining for the impulsive Hubble dynamics) |
| `v_terminal` | fold | DERIVED (terminal modulus velocity) | PRIMARY (the kinematic state at fold — defining for Mach=13.75) |
| `dt_transit` | fold | DERIVED (transit duration) | PRIMARY (the impulsiveness IS dt_transit; without it the cascade is not impulsive) |
| `P_exc_kz` | fold | DERIVED (KZ excitation probability) | PRIMARY (the saturation P=1 is what makes Parker production headline) |
| `n_Bog` | fold | DERIVED (Bog fraction per mode) | PRIMARY (per-mode relic occupation, defining for the GGE) |
| `n_pairs` | fold | DERIVED (Bog pairs from transit) | PRIMARY (the relic's pair count, headline post-fold observable) |
| `c_fabric` | fold | RELATED (substrate sound speed sets Mach) | PRIMARY (same reason; both classes treat it as the supersonic referent — flagged as PRECONDITION-candidate) |
| `phi_paasch` | fold | RELATED (related to fold geometry) | RELATED (same reason; substrate-static identity) |
| `m_tau` | fold | RELATED (modulus mass at fold) | RELATED (same reason; substrate inertial scale) |
| `omega_tau` | fold | RELATED (transit frequency) | DERIVED (algebraic from v_terminal + modulus mass) |
| `Gamma_effacement` | CC | RELATED (acoustic-white-hole impedance; (1-Gamma) = effacement residual = dark-energy-like leakage) | PRIMARY (the white-hole impedance IS the Exflation post-fold causal-disconnection mechanism) |
| `Mach_max_framework` | (none yet) | n/a | PRIMARY (newly canonical S85 W6-1; first proposed class home) |
| `c_BLV` | (none yet) | n/a | PRIMARY (newly canonical S64; first proposed class home) |
| `w0_FW` | (none yet) | n/a | PRIMARY (CC-class candidate too; w_0 is the dark-energy EOS) |
| `n_s_framework` | (none yet, but cousin of `alpha_s_inflation_framework` in alpha_s_inflation) | n/a directly | PRIMARY (Exflation's CMB-tilt prediction) |
| `N_pivot` | (none yet) | n/a | DERIVED (e-fold count from the substrate-c_s correction) |

The overlap with `fold` is structural: fold is the GEOMETRIC EVENT at tau=0.19 in isolation; Exflation is the WHOLE cascade through that event including pre-fold cascade ignition (cold-big-bang vacuum-floor instability per `project_cold-big-bang-vacuum-floor.md` — tau=0 is an unstable maximum, dS/dtau=+58,673 forces the cascade) and post-fold relic dynamics. Many fold-class members appear with DIFFERENT roles in Exflation because the viewpoint shifts: a quantity that is `DERIVED` from the fold's local geometry (e.g., H_fold) becomes `PRIMARY` for the cascade dynamics it drives.

The overlap with CC is one constant: `Gamma_effacement` is RELATED in CC (the (1-Gamma)=3e-4 IR leakage that constitutes the framework's CC observable) and PRIMARY in Exflation (the impedance IS the white-hole causal-disconnection mechanism). Both classes legitimately claim it, with different roles.

The overlap with KK is implicit, not direct: every Exflation quantity is in M_KK units, but no KK-defining constant (M_KK, M_KK_gravity, M_KK_kerner, OOM_diff_MKK) is itself an Exflation member. The cascade transits THROUGH the KK scale; KK is the unit-frame, not a participant in the dynamics.

The overlap with Higgs is zero: Higgs-sector constants (m_H_obs, v_ew, m_t_pole, m_b_pole) are properties of the post-fold spectral content's representation theory, evaluated long after the cascade has settled. The Higgs class is downstream of Exflation in time but disjoint in defining-constant set.

The overlap with alpha_s is via the Exflation member `n_s_framework` (= 0.9561) cousining the alpha_s_inflation member `alpha_s_inflation_framework` (= n_s^2 - 1, S50 identity). Different constants, same logical neighborhood — alpha_s_inflation is the *first derivative* of the post-fold relic's spectral correlation, and Exflation contains the *value* (n_s_framework) but not the *derivative* (alpha_s_inflation_framework). The class boundary is clean: alpha_s_inflation is the running of n_s; Exflation is the substrate event that produced n_s in the first place.

---

## Notes for the orchestrator

1. **Member count**: 16 PRIMARY + 8 DERIVED + 10 RELATED = 34 total. Within the 15-40 target band; appropriately larger than fold (15) given Exflation's broader scope, but smaller than would result from listing every constant nominally tagged with a fold/transit session.

2. **Constants considered but excluded**: `J_C2`, `J_su2`, `J_u1` (Josephson couplings on the 32-cell tessellation, S47): these are POST-FOLD substrate properties, not cascade quantities. If a "post-fold-fabric" class is later created, they would PRIMARY there. `N_cells` (= 32, Voronoi cells): same reason — fabric tessellation, not cascade. `omega_L1`, `omega_L2`, `omega_H1`, `omega_H2`, `omega_H3` (S52 GL-Josephson phonon spectrum): post-fold phonon spectrum, would PRIMARY a "post-fold-phonon" class. `Q_Leggett` is the borderline case: included as RELATED because the Leggett mode IS a cascade-survivor quasiparticle and its quality factor is the headline DM-survival observable, but excluded from PRIMARY since its existence is a fabric property, not a cascade output. `alpha_QM` (= -0.579, quantum-metric K^4 correction): a substrate-geometric correction term, not an Exflation participant. `gamma_RP`, `t_deph_over_t_transit`: Liouvillian decoherence ratios — these characterize the cascade's information-theoretic structure but are second-level observables, excluded for member-count discipline. `kappa_BCS` (= 4.019): BCS surface gravity at the analog horizon — included as RELATED (white-hole side); not PRIMARY because it's a *characterization* of the white-hole, not a *driver* of the cascade.

3. **Excluded explicitly**: `H_tilde_lo`, `H_tilde_hi`, `H_tilde_center`, `H_tilde_canonical_TD`, `H_tilde_canonical_LI` — these are S82-S84 PASS-window endpoints / Branch-A/B microscopic anchors for an Hubble-tilde constraint; they are NOT cascade-defining quantities, just bookkeeping bounds. They would belong in a possible future "H_tilde-anchor" class if one is created.

4. **Substrate framing audit** (per `.claude/rules/phononic-framing.md`): every comment in this proposal uses substrate language. The class description uses "eigenvalue spectrum reorganizes" not "particle creation in spacetime"; "acoustic white hole" not "horizon problem"; "supersonic transit" not "slow-roll inflation"; "first-order phase transition" not "Big Bang"; "Parker quasiparticle pair production" not "reheating"; "GGE relic" not "thermal afterglow"; "effacement-residual leakage" not "vacuum energy". The class IS the substrate cosmogenesis story; container thinking is actively avoided.

5. **Inheritance audit (3He-B parent->child)**: Per `framework-3heb-comparison.md` (S60 Surprise Catalog), the framework is universality-class-3He-B (BDI, idealized, 0D). The Exflation class inherits the supersonic-transit phenomenology from the 3He-B Kibble-Zurek defect-formation literature (Volovik 2003 §27), with the key delta being P_exc_kz=1 (saturation, not a Landau-Zener probability) reflecting the framework's 0D limit and impulsive transit. The post-fold GGE relic inherits from the 3He-B integrability theorem (algebraic GGE permanence per S38), again with the delta being N_pair=1 discreteness. xi_E_GGE_inv (canonical_constants.py line 676) is the explicit s=-1 Mellin diagnostic on the GGE-projected D_K and is currently consumed by the 3He-B inheritance correspondence; it is a *post-fold relic spectral observable* that in a future revision could be added to Exflation as RELATED (linking the substrate cosmogenesis class to the 3He-B inheritance line). I have NOT included xi_E_GGE_inv in the current proposal because it is a methodologically-distinct spectral diagnostic (Branch-IV S86 W4-1 P4 commit), not a cascade-defining quantity.

6. **Schema compliance check**: every constant ID listed above was verified by Grep against canonical_constants.py to confirm it resolves as a real attribute (line numbers cited in the upstream Grep). Self-validation in canonical_classes.py §E (`if e["tgt"] not in _module_globals`) will pass on the proposed edges.

7. **Role-taxonomy recommendation**: keep the three-level PRIMARY/DERIVED/RELATED schema for C.2 merge. The three flagged constants (c_fabric, n_pairs, w0_FW/n_s_framework) currently sit on PRIMARY without forcing an ambiguity that breaks downstream consumers. Reassess if a second process-class proposal hits the same friction in C.3+.

8. **Headline takeaway for the visualizer**: Exflation's PRIMARY count (16) is high because it is an end-to-end PROCESS class spanning four chapters (driver, kinematics, production, relic). Compare to fold (15 members, single-chapter geometric event), CC (6 members, single-observable family), KK (4 members, single-scale family). Exflation's scope is intermediate — narrower than "the whole framework" (which would be every constant) but broader than any single-event class. The 34-member total reflects this scope honestly.

---

**End of C.1 Proposal — Exflation Class.**
