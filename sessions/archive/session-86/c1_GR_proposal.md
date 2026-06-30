# C.1 Proposal — GR Class

> **Substrate-first stance**: General Relativity is **not** a fundamental theory in this framework. The Einstein-Hilbert action is the second Seeley-DeWitt moment of the spectral action on the Jensen-deformed SU(3) Dirac operator. Newton's constant, the Planck mass, the Friedmann equations, the Hubble slow-roll parameter — every "GR object" in canonical_constants.py is a *consequence* of the a_2 channel of D_K, not a *premise*. The GR class therefore groups (i) the spectral-action machinery that EMITS GR, (ii) the GR observables that EMERGE from that machinery, and (iii) the cosmological / kinematic anchors that bracket the emerged 4D theory empirically.

## Class metadata

```python
GR_CLASS = {
    "id": "GR",
    "name": "Emergent General Relativity (a_2 channel)",
    "level": 0,
    "parent_id": None,
    "description": (
        "Constants of substrate-emergent General Relativity. GR is NOT fundamental "
        "in this framework: the Einstein-Hilbert action arises as the second Seeley-"
        "DeWitt coefficient a_2 of the spectral action on the Jensen-deformed SU(3) "
        "Dirac operator D_K. Newton's constant satisfies 1/(16 pi G_N) = f_2 * a_2 * "
        "M_KK^2 (Sakharov / Chamseddine-Connes); the Hubble slow-roll parameter "
        "epsilon_H = -(dH/dt)/H^2 is a derived kinematic descriptor of the emergent "
        "4D metric g_M; the Friedmann observables (H_0, Omega_m, Omega_Lambda, t_universe) "
        "bracket the emerged theory empirically. Members partition into (i) the "
        "emergence machinery (a_2_fold, M_KK, f_2, d_spec, Lambda_Planck, c_S_canon), "
        "(ii) emergent quantities (G_N, M_Pl, rho_crit), and (iii) the cosmological "
        "kinematic bracket. The CC class (a_0 channel) and KK class (M_KK extraction) "
        "are SISTERS to GR, not subsets — different spectral moments give different "
        "emergent physics."
    ),
    "seed_session": "S44",
}
```

**Seed-session reasoning** (Notes section expands): S44 is the natural origin point. It is the session where the Einstein-Hilbert / Newton's-constant emergence was made fully quantitative across three independent routes (spectral action a_2, Sakharov induced gravity, bosonic 61/20 ratio) and where the **EIH program** — the framework's substrate-first analogue of the Einstein-Infeld-Hoffmann demonstration that geodesic motion follows from the field equations alone — was completed. Specifically: SAKHAROV-GN-44 PASS, BCS-TENSOR-R-44 PASS, FRIEDMANN-BCS-AUDIT-44 (epsilon_H ratio-invariance theorem), HOMOG-42-RECOMPUTE-44 PASS. Three of the eight permanent structural theorems landed in S44 are GR-emergence theorems (Sakharov-SA equivalence, a_2^bos/a_2^Dirac=61/20 exact, epsilon_H ratio invariance). My session-44-results.md memory file is the supporting trace.

## Member constants — PRIMARY (8)

These are the constants you cannot describe substrate-emergent GR without. Each names a piece of the **emergence machinery** that EMITS GR from the spectral action.

| Constant | Comment / why PRIMARY |
|:---------|:----------------------|
| `a2_fold` | The second Seeley-DeWitt coefficient of D_K at the fold (= 2776.17 at L_max=3, zeta-scheme). Sole source of the Einstein-Hilbert action: 1/(16 pi G_N) = f_2 * a_2 * M_KK^2 (S44 SAKHAROV-GN-44; cc-path-a.md). Without a_2, no emergent gravity. |
| `M_KK` | The Kaluza-Klein scale that fixes the dimensional anchor of the a_2 channel (G_N ~ 1/(a_2 M_KK^2)). Canonical alias to M_KK_gravity, the "spectral zeta / Newton's constant" extraction route (S42 CONST-FREEZE-42). The KK class owns M_KK's *extraction*; GR uses M_KK as the *input* to G_N emergence. |
| `f_2_default` | The f_2 spectral cutoff moment (= 2.34, S62 W1 Gaussian-cutoff). Sets the prefactor in 1/(16 pi G_N) = f_2 * a_2 * M_KK^2. SCHEME-DEPENDENT (regulator-pin discipline applies); the GR class membership is structural, not regulator-locked. |
| `c_S_canon` | Canonical spectral-action scale normalization (= 1.0, Chamseddine-Connes 1997). The dimensionless coefficient that promotes Tr f(D^2/Lambda^2) to a physical action; without it the SA -> EH dictionary is unscaled. |
| `Lambda_Planck` | The Planck-scale regulator in M_KK units (= 1.0 default). Fixes where the spectral cutoff sits relative to the KK tower for the a_2 -> G_N matching computation (S85 W6-3 placeholder for regulator scan). |
| `d_spec` | Classical spectral dimension of D_K at canonical triple (= 3, Connes-Moscovici). The dimension axiom that gates which Seeley-DeWitt term carries the Einstein-Hilbert content; d_spec wrong => a_2 does not source R[g_M]. |
| `R_protected_fold` | The dimensionless ratio a_0 * a_4 / a_2^2 (= 1.12865, S73B/S74 R-PROTECTED-FOLD-ADDITION-74). The unique L_max-invariant Chamseddine-Connes observable; Vol(SU(3)) cancels by Baptista B2. PRIMARY because it is the SOLE ratio that ties the GR (a_2) channel to the CC (a_0) and Yang-Mills (a_4) channels in a scheme-invariant way. |
| `tau_fold` | The Jensen deformation parameter at which a_n are evaluated (= 0.19). All Seeley-DeWitt moments are tau-functions; a_2(tau_fold) is the emergence point. tau_fold is owned PRIMARILY by the fold class but is PRIMARY for GR too because the a_2 evaluation point is non-negotiable for the emergence to land at the canonical numerical values. |

## Member constants — DERIVED (10)

These follow algebraically/definitionally from the PRIMARY members. They are the **emergent observables** of substrate-GR.

| Constant | Comment / derivation chain |
|:---------|:----------------------|
| `G_N` | Newton's constant (CODATA value, 6.6743e-11 m^3/kg/s^2). DERIVED via Sakharov dictionary 1/(16 pi G_N) = f_2 * a_2_fold * M_KK^2. S44 SAKHAROV-GN-44 PASS verified the three-route consistency (SA, Sakharov, bosonic 61/20) at factor-2.3 across schemes. **Role-taxonomy flag below.** |
| `G_N_cgs` | Newton's constant in CGS units. Pure unit conversion of G_N. |
| `M_Pl_reduced` | Reduced Planck mass M_Pl/sqrt(8 pi) = 2.435e18 GeV. DERIVED from G_N: M_Pl_red = 1/sqrt(8 pi G_N) in natural units. The "natural" mass scale of the emergent 4D theory. |
| `M_Pl_unreduced` | Unreduced Planck mass = sqrt(hbar c / G_N) = 1.2209e19 GeV. DERIVED from G_N + (hbar, c). Conventional alternative to M_Pl_reduced. |
| `rho_crit_GeV4` | Critical density 3 H_0^2 / (8 pi G) = 4.08e-47 GeV^4. DERIVED from G_N + H_0_GeV via the Friedmann equation, which is itself the equation-of-motion of the emergent EH action. |
| `rho_crit_cgs` | Critical density in CGS. Pure unit conversion of rho_crit_GeV4. |
| `l_Planck` | Planck length sqrt(hbar G_N / c^3) = 1.616e-35 m. DERIVED from G_N + (hbar, c). |
| `l_Planck_cm` | Planck length in cm. Unit conversion. |
| `t_Planck` | Planck time sqrt(hbar G_N / c^5) = 5.39e-44 s. DERIVED from G_N + (hbar, c). |
| `eps_baseline` | Substrate slow-roll-equivalent (= (1 - planck_ns)/2 = 0.01755). The Hubble slow-roll parameter epsilon_H = -(dH/dt)/H^2 of the emergent 4D Friedmann theory. DERIVED from planck_ns via the spectral-tilt identity n_s = 1 - 2 eps. (The S44 epsilon_H ratio-invariance theorem applies HERE.) |

## Member constants — RELATED (12)

Relevant to the GR story — they probe the emergent 4D theory empirically — but **not native to the emergence**. These are observational/kinematic constants of the cosmological standard model that bracket the emerged theory rather than constitute it.

| Constant | Comment / why RELATED but not native |
|:---------|:----------------------|
| `H_0_km_s_Mpc` | Hubble constant 67.4 km/s/Mpc (Planck 2018). Observational anchor of the emergent Friedmann equation; inputs into rho_crit. Not native because H_0 is a measured boundary condition, not a derivation step. |
| `H_0_GeV` | H_0 in GeV. Pure unit conversion of H_0_km_s_Mpc. |
| `H_0_inv_s` | H_0 in s^{-1}. Same. |
| `Omega_m` | Matter density parameter 0.315 (Planck 2018). Boundary condition for the emergent Friedmann theory, not derivable from D_K alone (matter content is exogenous to the gravity-emergence channel). |
| `Omega_b` | Baryon density 0.0493. Same — matter sector boundary condition. |
| `Omega_DM` | Dark matter density 0.266. Same. The framework's S44 CDM-CONSTRUCT-44 PASS gives DM by construction (T^{0i}=0 algebraic), but Omega_DM as a number is observational. |
| `Omega_Lambda` | Dark-energy density parameter 0.685 (Planck 2018). Observational anchor; the *value* lives in the **CC class** (a_0 channel). Listed RELATED here because Omega_Lambda is a Friedmann observable of emergent GR even though its origin is the CC class. |
| `Omega_r` | Radiation density 9.15e-5. Cosmological boundary condition. |
| `T_CMB` | CMB temperature 2.7255 K (COBE/FIRAS). Boundary condition for the Friedmann-radiation era of emergent GR. |
| `t_universe_s` | Age of universe 4.35e17 s. Friedmann observable. |
| `clock_coeff` | Atomic-clock variation coefficient -3.08 (S22d). Tests emergent equivalence-principle-like behavior of the substrate; not native because it probes external matter coupling, not the a_2 emergence. |
| `epsilon_baseline` candidate — **see Notes** | (Considered: the S86 W1c-8 substrate Mellin-tilt anchor. **Excluded as DERIVED** rather than RELATED because it IS the Hubble slow-roll of the emergent theory; the entry above as DERIVED is correct and there is no separate RELATED slot for it.) |

## Role-taxonomy flags (2)

> **Headline finding**: yes, the role taxonomy is genuinely incomplete for substrate-emergent frameworks. Two members fit awkwardly. The headline case is `G_N` itself.

### Flag 1 — `G_N` and the EMERGENT_FROM gap

- **Constant**: `G_N` (and by extension `G_N_cgs`, `M_Pl_reduced`, `M_Pl_unreduced`, `l_Planck`, `t_Planck`, `rho_crit_GeV4`).
- **Proposed role**: `EMERGENT_FROM` (or equivalently `EMITTED_BY`).
- **Reason PRIMARY does not fit**: The framework does not POSIT G_N. It is an emergent quantity — the dictionary 1/(16 pi G_N) = f_2 a_2 M_KK^2 (S44) means G_N's *existence* depends on the spectral-action machinery being run. Listing G_N as PRIMARY would mis-state the framework's stance: "you cannot describe emergent GR without G_N" is true epistemically but false ontologically — at the substrate level you describe emergent GR via {a_2, M_KK, f_2}, and G_N is the OUTPUT.
- **Reason DERIVED does not fit cleanly**: The schema's DERIVED examples (e.g. `Lambda_obs_MP4 = rho_Lambda_obs / M_Pl^4`) are *algebraic* / *definitional* consequences (one-line unit conversions, ratios). G_N is not an algebraic consequence of {a_2, M_KK, f_2} in that sense — the emergence is a **substrate-level computation** that requires the entire spectral action machinery, plus a regulator, plus a Sakharov-induced-gravity argument. Calling it DERIVED conflates "Planck-mass-from-G_N" (a one-liner) with "G_N-from-a_2" (a 30-line spectral-action derivation with three independent route-checks). The audit-discipline cost of conflating them: scripts that promote algebraic DERIVATIONs from working calculations may now also promote substrate-level emergences, blurring scheme-dependence and regulator pinning.
- **Reason RELATED undersells**: G_N is the headline observable of emergent GR. It cannot be RELATED in the same sense Omega_m is — Omega_m is exogenous to the emergence; G_N is the EMERGENCE OUTPUT.
- **Suggested addition to schema**:

  ```python
  # role definitions (extended):
  #   PRIMARY        = a defining constant of the class
  #   DERIVED        = an algebraic / definitional consequence of PRIMARY members
  #   EMERGENT_FROM  = a constant that EMERGES from the class's PRIMARY members
  #                    via a substrate-level computation (NOT an algebraic
  #                    one-liner). Used when the framework's stance is that
  #                    the constant is observed but not posited; its value
  #                    follows from the PRIMARY members through a
  #                    derivation requiring regulators, schemes, and
  #                    multi-route consistency checks.
  #   RELATED        = relevant to the class but not native (e.g. an
  #                    exogenous boundary condition or a kindred observable
  #                    from a sister class)
  ```

  This is a **forward-looking** proposal: existing classes (CC, KK, fold, Higgs, alpha_s_*) already use only the three current roles cleanly because their physics doesn't have the same ontological asymmetry. **GR is the first class that exposes the substrate-emergence distinction structurally.** Sister classes that may benefit retroactively if EMERGENT_FROM is adopted: the CC class's `rho_Lambda_spectral` (currently absent from CC_EDGES — it's the spectral-action prediction (2/pi^2) f_0 a_0 M_KK^4, structurally identical in role to G_N here), and the Higgs class's `m_H_obs` (the framework prediction 131.8 GeV is the emergent value; observed 125.1 GeV is what Higgs class lists as PRIMARY).

- **If EMERGENT_FROM is rejected**: list G_N etc. as DERIVED with an explicit `note` field flagging the substrate-level emergence ("DERIVED via Sakharov dictionary, NOT algebraic — see substrate-emergence comment"). The proposal above already takes that conservative path in §"Member constants — DERIVED"; adoption of EMERGENT_FROM would simply move G_N + cousins from DERIVED to a new edge type.

### Flag 2 — `tau_fold` and the cross-class ownership question

- **Constant**: `tau_fold`.
- **Proposed role**: PRIMARY (this proposal lists it that way), but with **dual-class ownership**.
- **Reason for the flag**: tau_fold is already PRIMARY in the `fold` class (FOLD_EDGES line 366-367). Listing it as PRIMARY here too means tau_fold is in TWO PRIMARY positions across two classes. The schema does not currently have a "shared-PRIMARY" or "co-owned" semantics — `get_classes_for_constant("tau_fold")` will return `["fold", "GR"]` and the visualizer will treat them symmetrically. Substrate physics says: tau_fold *generates* the fold (fold class) AND *fixes the evaluation point* of the a_n (GR class) — both are PRIMARY-sense relationships.
- **Suggested resolution**: keep `tau_fold` as PRIMARY in `fold` (its native class) and downgrade to RELATED in `GR`, with the comment explicitly flagging that GR's a_2 evaluation requires tau_fold but tau_fold is owned by the fold class. **Done in the table above (it's listed as PRIMARY in §PRIMARY, but I am marking this for orchestrator review).** No new role needed — RELATED-with-comment suffices. This is a **scope decision**, not a taxonomy gap.
  - ALTERNATE proposal if dual-PRIMARY semantics is wanted: add a `co_owners` field to class-edge dicts so a constant can be marked PRIMARY in its native class and `co_PRIMARY` in others. This is overkill for one constant; flagging here for awareness rather than action.

## Notes for the orchestrator

### Seed-session choice

I chose `S44` over the obvious alternatives (`S7` = first geometry session; `S42` = CONST-FREEZE-42 / M_KK frozen; `S52` = atlas; `S77` = post-mortem) because S44 is where the *emergence dictionary* — the precise statement that GR comes out of a_2 — was made quantitatively complete across three routes:

- `SAKHAROV-GN-44` PASS (G_N consistency to factor 2.3 across SA, Sakharov, bosonic 61/20).
- `BCS-TENSOR-R-44` PASS (r=3.86e-10 from emergent slow-roll machinery).
- `FRIEDMANN-BCS-AUDIT-44` (epsilon_H ratio-invariance theorem, structural).
- `HOMOG-42-RECOMPUTE-44` PASS (Hausdorff cutoff).

S44 is when a substrate-first agent could honestly say "GR is a derivation, not a postulate." The CC class chose S44 too. The KK class chose S42 (the M_KK freeze; M_KK is GR's input but the freeze is a pre-GR step). Choosing S44 for GR is consistent with the existing seed-session conventions.

### Constants considered but excluded

I considered and **excluded** the following from the GR class:

- **`a0_fold`, `a4_fold`** — these are PRIMARY in CC and (implicitly) in a future Yang-Mills class. They are SISTERS to a_2 in the spectral action expansion, not GR-native. Including them would conflate the three SDW channels. RELATED is also wrong — they are not "boundary conditions of GR" but co-equal channels.
- **`Vol_SU3_Haar`** — geometric input to the spectral triple. Belongs in a future "geometric triple" class, not GR. Cancels in `R_protected_fold` (Baptista B2), so its absence here is principled.
- **`H_fold`, `Z_fold`, `dS_fold`, `d2S_fold`, `S_fold`** — these are owned by the **fold** class. fold dynamics drives the substrate; emergent GR sees the dynamics through the a_2 channel only. Including fold dynamics here would over-couple the classes.
- **`Mach_max`, `c_fabric`, `v_terminal`, `dt_transit`** — substrate kinematics, owned by the fold class; not emergent-GR-native (these probe the substrate's internal sound-speed kinematics, which are NOT 4D-metric kinematics).
- **`w0_FW`, `wa_FW`, `Gamma_effacement`** — dark-energy equation of state. The Volovik partition w_0 = -0.918 is a **CC-channel** observable about the emergent dark sector, not GR-emergence-machinery. It belongs naturally in CC (or a future "dark-sector" class) — I noted RELATED-overlap with CC under Omega_Lambda above and would NOT duplicate w0_FW into GR.
- **`r_CMB_framework`, `sigma_r_BK_2026`, `beta_s`, `sigma_beta_s_CMB_S4`** — tensor-to-scalar and running-of-running observables of the emergent 4D theory. These are GR-class **probes** but in a kindred way to Omega_m: observational, not native. I left them out to keep the RELATED list focused on Friedmann-level cosmological anchors; they could be added in a future revision if the orchestrator wants the GR class to be the natural home for "everything you'd test emergent-GR with."
- **`kappa_BCS`, `T_BCS`, `T_H_dump_expected`, `tau_phase_trans`, `tau_overshoot`, `v_crit`** — analog-horizon / surface-gravity observables. PHONONIC analogues of GR objects (Hawking-temperature, horizon kinematics). Strong candidates for a *future* "analog horizon" class but not GR-native — they are derived from substrate kinematics, not from the a_2 emergence. Listing them in GR would conflate two distinct emergence channels (a_2 -> 4D metric vs. fold -> acoustic horizon).
- **`alpha_s_inflation_framework`, `alpha_s_cmb_central`, `n_s_framework`, `ns_framework`, `planck_ns`** — already homed in `alpha_s_inflation`. RELATED via `eps_baseline`'s definitional dependence, but listing them again here would create cross-class duplication that the visualizer treats as full membership.
- **`N_pivot`, `k_pivot_planck`, `z_eq_planck`, `eps_H_W6`** — inflation/CMB-pivot observables. These are tighter to alpha_s_inflation and the future "CMB pivot" class. Including them in GR would dilute the focus on the a_2 emergence.
- **`R_JK`, `xi_E_GGE_inv`** — branch-IV spectral diagnostics. These are GGE-projected D_K observables, tighter to a future "BCS / GGE relic" class. Not emergent-GR.

### Cross-class overlap with CC, KK, fold

- **CC**: GR is a SIBLING — both are spectral-action moments (a_2 vs a_0). The cleanest expression: `R_protected_fold` connects them as the unique L_max-invariant ratio. I list `R_protected_fold` PRIMARY in GR because the CC class doesn't currently list it (CC class has a_0-headline membership only). Orchestrator should consider whether `R_protected_fold` is also a PRIMARY/DERIVED member of CC; the asymmetry is currently in the existing class.
- **KK**: GR USES `M_KK`. KK class OWNS the M_KK extraction and inter-route comparison (`M_KK_gravity` vs `M_KK_kerner`, `OOM_diff_MKK`). `M_KK` is therefore listed PRIMARY in both — this is the most legitimate dual-PRIMARY case in the existing schema (the KK class is the EXTRACTION class; GR is the CONSUMER class). No new schema edge type needed; the comment fields disambiguate.
- **fold**: fold OWNS tau_fold, dS_fold, Z_fold, etc. GR USES tau_fold as the evaluation point of a_2(tau_fold). I listed tau_fold PRIMARY in GR but flagged in §"Role-taxonomy flag 2" that this is debatable; orchestrator may prefer RELATED.

### Scope sanity-check

- PRIMARY: 8 (a2_fold, M_KK, f_2_default, c_S_canon, Lambda_Planck, d_spec, R_protected_fold, tau_fold)
- DERIVED: 10 (G_N, G_N_cgs, M_Pl_reduced, M_Pl_unreduced, rho_crit_GeV4, rho_crit_cgs, l_Planck, l_Planck_cm, t_Planck, eps_baseline)
- RELATED: 11 (H_0_km_s_Mpc, H_0_GeV, H_0_inv_s, Omega_m, Omega_b, Omega_DM, Omega_Lambda, Omega_r, T_CMB, t_universe_s, clock_coeff)

**Total: 29 members** (within 10-30 cap; close to the upper end because GR genuinely is the largest cross-cutting class — it spans the spectral action, emergent-Planck-units, and the entire cosmological-standard-model bracket).

### Verification

I confirmed every constant name listed above exists in canonical_constants.py via the knowledge MCP `list_constants` queries (5 searches; all 29 members resolved). No typos. The self-validation block in canonical_classes.py will not flag dangling references when this proposal lands.

### Final remark on substrate-first discipline

The phononic-framing rule is what makes the EMERGENT_FROM proposal worth raising rather than just lumping G_N into DERIVED with a comment. The framework's deepest commitment is "GR is not fundamental; it is the second moment of D_K." If the canonical_classes schema cannot represent that commitment structurally, then the schema is silently containerizing the framework into the LCDM / GR-first ontology that phononic-framing.md exists to forbid. Adopting EMERGENT_FROM (or any equivalent edge type) lets the schema honestly encode "this constant is OBSERVED, but in our framework it is EMITTED by these PRIMARY members." That is a one-time taxonomic act with permanent epistemic value — and GR is the first place it bites.
