# Investigation 8 Plan — Wave 3: Cross-Domain Bridges (transit + condensed-matter + spectral-geometry)

**Date**: 2026-06-14
**Author**: phonon-first-cosmologist (per /rclab-plan --investigation per-wave swarm; reviewer-origin owner of this wave)
**Owner agent**: phonon-first-cosmologist (the cross-domain pattern detector; this wave is built from my own investigation-1 survey §5 "Untraveled Bridges" + the Closing "Highest-Leverage Next Steps")
**Seed**: `sessions/investigation/investigation-1/phonon-first-cosmologist.md` §5 (B-1, B-2, B-3, B-5) + §4 (R-1, R-2) + Closing next-steps 1–5
**Plan source**: `sessions/investigation/investigation-8/investigation-8-seed.md §"Wave 3 items"` + `investigation-8-partition.md §"Wave 3"`
**Working paper**: `sessions/investigation/investigation-8/investigation-8-w3-workingpaper.md`

---

## Wave 3 Summary

This wave runs the five springboards that a decade of condensed-matter / analog-gravity / quantum-geometry literature opened *adjacent to the framework's own pillars* — the place my survey's meta-observation named as "where the framework is least exhaustive is exactly where it is strongest in principle." Each gate translates a known post-2015 result into the substrate's own language and tests whether the cross-domain image survives, using ONLY already-derived substrate inputs (z=2, Mach 13.75, the Z_3 Jensen structure, the fold-band quantum metric, m_H, the broken-charge algebra). The wave straddles three pillars (Pillar I/VI transit + soliton, Pillar IV/V flat-band BCS + Josephson, Pillar VII/VIII spectral dimension + KK geometry):

1. **INV8-W3-1** (Kibble-Zurek Z_3 walls) — does the finite-rate transit through the *actual* Z_3-structured Jensen manifold at the *actual* Mach 13.75 freeze in a wall network? The "no-walls" verdict was decided on a π_0(U(1))=0 homotopy argument that may have used the wrong symmetry group (U(1) instead of U(1)×Z_3). Reaches C-1 (DESI w_a, walls give w=−2/3) AND C-4 (BBN, walls add an a⁻¹ relativistic-energy channel) with one compute.
2. **INV8-W3-2** (quantum-metric stiffness → H(τ)) — is the Peotta-Törmä superfluid-weight stiffness `D_geom = (2Δ/V)∫Tr g d²k` of the fold band, dimensionalized by M_KK, the Hubble backbone H(τ) the rank-1 NNU theorem currently *imports*? This is the constructive attack on the a(t) gap (G-1) from a substrate-IS spectral-triple invariant. Builds on the registered §VII.W / §VII.AF.1 Pillar-III↔IV bridge.
3. **INV8-W3-3** (P(σ) at L_max=14-16) — push the heat-trace return probability past the narrow-band artifact (the GT-builder lifted the Sym^13/14 wall at S104/S105) and finally MAKE the CDT/asymptotic-safety dimensional-reduction comparison the framework currently ASSERTS but never measured, via the energy-axis γ_E (the diffusion-window K=2 specialization). **Multiplicative-normalization-cancellation pre-flight is MANDATORY** (is the L_max-plateau a structural identity or empirical regulator-class evidence?).
4. **INV8-W3-4** (Higgs quartic RG) — run λ(μ) from the framework's predicted m_H=131.8 GeV up to M_KK on the substrate spectrum: does λ stay positive (absolute stability, a prediction distinguishing the substrate from the SM) or λ→0 near a high scale (SM near-criticality reproduced from geometry — strong evidence the spectral-action cutoff f IS physical, bridging A-3)?
5. **INV8-W3-5** (Watanabe-Murayama branch count) — settle the parked 6-vs-7 phonon-branch count as a *theorem* via the exact non-Lorentz-invariant Goldstone-counting formula `n_NG = (dim G − dim H) − ½ rank ρ`, with `ρ_ab = −i⟨[Q_a,Q_b]⟩` computed from the D_K / Kosmann-connection algebra. z=2 (already known) ⇒ Type-B; this needs the broken-charge algebra (already built), NOT the deferred full SU(3) sigma-model.

Gate-type mix: **compute × 5** (all five emit verdict lines to `computations/investigation-8/inv8_gate_verdicts.txt`).

## Wave 3 Gate-Type Manifest

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| INV8-W3-1 | compute | Kibble-Zurek defect density of the transit through the actual Z_3 Jensen manifold at Mach 13.75; does a frozen Z_3 wall network form? (w=−2/3 candidate for DESI w_a; a⁻¹ BBN channel). Reaches C-1 + C-4. |
| INV8-W3-2 | compute | Quantum-metric stiffness `D_geom = (2Δ/V)∫Tr g d²k` of the fold band, dimensionalized by M_KK; is it the imported Hubble backbone H(τ)? (Tr g>0, Ω=0 EXACT — C=0 maximally-NON-ideal). Attacks G-1. |
| INV8-W3-3 | compute | Push P(σ)=Tr e^{−σ D_K²} to L_max=14-16 (GT-builder unlock); d_s(σ→0)→8 (Weyl) AND d_s(σ_*) windowed; CDT/asymptotic-safety comparison via energy-axis γ_E. Multiplicative-normalization pre-flight MANDATORY. |
| INV8-W3-4 | compute | Run Higgs quartic λ(μ) from m_H=131.8 GeV to M_KK on the substrate spectrum; absolute stability (λ>0) or near-criticality (λ→0)? Bridges A-3. |
| INV8-W3-5 | compute | Watanabe-Murayama Goldstone count `n_NG=(dim G−dim H)−½ rank ρ`, ρ_ab from the Kosmann algebra (z=2⇒Type-B); settle 6-vs-7 branch count as a theorem; classify Type-A vs Type-B. |

## Wave 3 Decision Point Prerequisites

All five gates are **independently dispatchable** — none consumes another W3 gate's verdict. Every prerequisite is an already-landed canonical constant, an on-disk data cache, or a PROVEN structural theorem (verified against the knowledge MCP at plan-freeze):

- **INV8-W3-1**: z=2 (DYNAMICAL-EXPONENT-63 / EXPONENT-63, INFO); ν=1/2 (mean-field BCS, S53/S88 KZ); τ_Q = `dt_transit` = 1.1301575e-3 M_KK⁻¹ (canonical); ξ_0 = `xi_BCS` = 0.8083468753837275 (canonical); `Mach_max_framework` = 13.75 (canonical); the Z_3 structure §VII.AG.4 (512-plaquette PASS, `S87-F-PLAQUETTE-TRIANGULAR-WILSON` value=512). No upstream W3 gate.
- **INV8-W3-2**: the §VII.W / §VII.AF.1.OP-PROJ registered bridge (`S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND` value=0.0950 at L_max=10, the R_geom laboratory-IN observable); Berry Ω=0 EXACT (W5, 1.12e-16, atlas-07 ERRATUM); `Delta_BCS` = 0.4642547394830737 (canonical); M_KK = 7.428660036284456e16; `w0_FW` = −0.918 (the imported backbone target). No upstream W3 gate.
- **INV8-W3-3**: the L_max=12 master spectrum cache `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9`, on-disk-verified); the GT-builder `computations/session-104/s104_branch_iv_phase1_builder.py` + the Sym^p chain cache `s104_sym_p_chain_cache_L1314.npz` (the deep-set sectors that lifted the Sym^13/14 wall, `S105-BRANCH-IV-DIRECT-L1314` INFO spread_CAC=0.0443091); `d_s_fold_window_sigma` = 1.4005 (canonical); the γ_E estimator `sessions/archive/session-93/workshops/s93-w7-3-gamma-e-dos-exponent-estimator.md` (eq_6934–eq_6942). No upstream W3 gate.
- **INV8-W3-4**: `m_H_FW_KK_threshold` = 131.8 GeV (canonical, Route-B); `v_ew` = 246.0; `m_H_obs` = 125.1; M_KK = 7.428660036284456e16; the substrate spectrum (the L12 cache) for the geometric β-function inputs. No upstream W3 gate.
- **INV8-W3-5**: the broken-charge algebra (U(1)_7 broken by the BCS condensate, B6 PROVEN, Cooper pairs carry K_7 charge ±1/2; the su(2)+u(1) Jensen stabilizer (3+1 generators) and the C² Higgs coset (4 generators, T_coset), session-73a); z=2 (Type-B); `S82-W0-A-BRANCH-COUNT` INFO value=6 (the number this gate seeks to settle as a theorem). No upstream W3 gate.

If any prerequisite is unmet at dispatch (e.g., the GT-builder times out at p+q≥13 for W3-3), the gate honestly closes per `mechanical-closure-discipline.md` (PRE-REG-INC), NOT a forced PASS.

---

## §W3-1. INV8-W3-1 — Kibble-Zurek Z_3 Wall Network of the Transit

```yaml
# ---- Identity ----
gate_id: "INV8-W3-1-KZ-Z3-WALL-NETWORK"
schema_version: "R3"
gate_type: "compute"
trigger: "[SIGN]"
classification: "PHONONIC"
agent_type: "transit-dynamics-theorist"
hypothesis: "The finite-rate transit through the ACTUAL Z_3-structured Jensen order-parameter manifold at the ACTUAL Mach 13.75 (z=2, dt/T_L=1.25e-5) freezes in a Z_3 domain-wall network at a density set by the Kibble-Zurek correlation length xi_hat = xi_0 (tau_Q/tau_0)^{nu/(1+z nu)}; the 'no-walls' verdict used pi_0(U(1))=0 but the broken symmetry is U(1)_7 x Z_3 with pi_0(Z_3)=Z_3 != 0, so a wall network DOES form, contributing a w=-2/3 dark-energy component (DESI w_a candidate) and an a^{-1}-redshifting BBN relativistic-energy channel."

method:
  description: >
    (1) Confirm the homotopy: the order-parameter manifold at the fold is the U(1)_7
    BCS-condensate phase circle TIMES the Z_3 Jensen-deformation structure (pi_0(Z_3)=Z_3,
    from framework-paasch-potential.md 1.2; the per-plaquette n_p^(T)=1/2 frustration of
    s86-two-layer-obstruction). The framework's 'no-walls' (my MEMORY: 'domain walls ABSENT
    on Jensen ridge, pi_0(U(1))=0') used the U(1) factor ONLY. Compute pi_0(U(1)_7 x Z_3) =
    pi_0(Z_3) = Z_3. (2) Compute the Kibble-Zurek frozen correlation length xi_hat at the
    canonical (z=2, nu=1/2, tau_Q=dt_transit, tau_0 from the microscopic relaxation scale)
    using the del Campo-Zurek scaling xi_hat = xi_0 (tau_Q/tau_0)^{nu/(1+z nu)}. Cross-check
    against the historical s53_kz_power_spectrum (xi_KZ=0.1398 at z=2/nu=1/2) and the s88-w2
    universality-class verdict. (3) Compute the wall-network number density n_wall ~ xi_hat^{-2}
    (codimension-1 Z_3 walls in d=3) and the wall-tension energy density rho_wall = sigma_wall *
    n_wall, with sigma_wall the Z_3 wall tension (Q18 anchor via §VII.AG.4; the framework's
    own ANDREEV-Z3 BdG wall solution at delta_phi=2pi/3). (4) The Mach-dependence: tau_Q ∝
    1/Mach (faster transit = shorter fold-crossing). Compute n_wall(Mach) and read off the
    direction. (5) Map to the equation of state: a frozen wall network has w_wall = -2/3
    (standard for codim-1 domain walls); compute the implied w_a contribution and the a^{-1}
    BBN-epoch energy-density scaling.
  producing_script: "computations/investigation-8/inv8_w3_kz_z3_wall_network.py"

# (1) operator
operator:
  type: "set"
  form: "pi_0(U(1)_7 x Z_3) = Z_3 != {e}  (walls admitted)  AND  n_wall(Mach) monotone-increasing in Mach"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "pi_0 = Z_3 (3-element set, |pi_0| = 3 > 1)  =>  WALLS-FORM; the verdict PASS/FAIL/INFO is set by the 3-tuple (homotopy-admits-walls, KZ-freezes-network, w=-2/3-component-nonzero)"
  direction: "!="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "framework-paasch-potential.md §1.2 (pi_0(Z_3)=Z_3); del Campo-Zurek IJMPA 29 1430018 (2014) xi_hat scaling; s88-w2-kz-universality-class.md (z=2/nu=1/2 mean-field BCS class)"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "pi_0 cardinality is an integer (=3); the KZ exponent nu/(1+z nu)=1/4 is rational; w_wall=-2/3 is rational"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "1 (single canonical point Mach=13.75) + 8-point Mach scan [13.75, 27.5] for the direction read-off"
  L_max: "N/A — homotopy + KZ scaling computation, not a spectral truncation"
  scan_range: "Mach in [13.75, 27.5]; tau_Q = dt_transit * (13.75/Mach)"
  step_size: "8 log-spaced Mach points (diagnostic direction scan)"
  tolerance: "1e-9 (cross-check xi_hat against s53 canonical 0.1398 to 3 sig figs); n_wall direction is a SIGN, not a magnitude tolerance"
  scheme: "FW"
  convention: "KZ-mean-field-BCS-z2-nu-half"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8 (scalar KZ arithmetic; no matrices)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain
substitution_chain:
  required: true
  content: |
    Claim: "Mach UP => tau_Q DOWN => xi_hat DOWN => n_wall UP (denser wall network at higher Mach)."
    Step 1: xi_hat = xi_0 (tau_Q/tau_0)^{nu/(1+z nu)}     [del Campo-Zurek 2014; xi_0 = xi_BCS = 0.8083468753837275]
    Step 2: nu = 1/2, z = 2  =>  nu/(1+z nu) = (1/2)/(1 + 2*(1/2)) = (1/2)/2 = 1/4   [mean-field BCS, S53/S88]
    Step 3: tau_Q(Mach) = dt_transit * (13.75/Mach)        [faster transit = shorter fold-crossing time; dt_transit=1.1301575e-3 at Mach=13.75]
    Step 4: Substitute:  xi_hat(Mach) = xi_0 * [dt_transit*(13.75/Mach)/tau_0]^{1/4}
                                       = const * Mach^{-1/4}
    Step 5: n_wall(Mach) ~ xi_hat^{-2}  (codim-1 walls in d=3)  =>  n_wall ∝ (Mach^{-1/4})^{-2} = Mach^{+1/2}
    Direction: d n_wall / d Mach = +(1/2) const Mach^{-1/2} > 0  =>  n_wall INCREASES with Mach.
    Numerical check (verified at plan-freeze): xi_hat(13.75)=0.1389 (cf canonical 0.1398/0.139);
                  Mach 13.75 -> 27.5: xi_hat 0.1389 -> 0.1168, n_wall(d=3 illustrative xi^-3) 373 -> 628 (UP).
    Conclusion: the wall-density-vs-Mach direction is +; a faster (higher-Mach) transit freezes a DENSER Z_3 wall network. The framework's actual Mach=13.75 is in the regime where xi_hat ~ 0.14 M_KK^{-1} < the fold horizon, so a network DOES freeze (the question the gate answers).

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  # No npz input — KZ scaling is computed from canonical constants. The s53 canonical xi_KZ=0.1398
  # is a methodological cross-check value (cited, not loaded).

# ---- Conditional blocks ----
fb_pair:
  forward: "z=2 (DYNAMICAL-EXPONENT-63); dt_transit + Mach_max_framework + xi_BCS (canonical); §VII.AG.4 Z_3 512-plaquette (S87-F-PLAQUETTE-TRIANGULAR-WILSON)"
  backward: "C-1 (DESI w_a; a frozen wall w=-2/3 component is a candidate for w_a != 0); C-4 (BBN; a^{-1} wall-energy channel re-opens the DeltaN_eff ledger); the 'no-walls' GGE-homogeneity claim (T2) is re-scoped if pi_0(Z_3) admits walls"
dual_prior:
  track_A: "0.5 — Reading_A (walls FORM): the homotopy pi_0(U(1)_7 x Z_3)=Z_3 admits walls AND the KZ correlation length is sub-horizon, so a frozen Z_3 network forms with w=-2/3; this re-opens C-1/C-4 as a SINGLE mechanism."
  track_B: "0.5 — Reading_B (no walls survive): even with pi_0(Z_3)!=0, the sudden-quench limit (dt/T_L=1.25e-5, P_exc=1.000) drives the system so fast that the Z_3 sectors are populated UNIFORMLY (no domain selection) OR the wall tension is sub-threshold (the ANDREEV-Z3 BdG core energy is < the GGE thermal scale), so the network anneals; the original no-walls verdict stands on a SHARPER argument than pi_0(U(1))=0."
  discriminator: "PASS (xi_hat sub-horizon AND sigma_wall > thermal scale) -> 0.9 to Track A; INFO (xi_hat sub-horizon but sigma_wall sub-threshold, network forms then anneals) -> mass split per the annealing fraction; FAIL (pi_0 argument was correct, no Z_3 walls at any Mach) -> 0.9 to Track B."

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/investigation-8/inv8_w3_kz_z3_wall_network.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/investigation-8/inv8_w3_kz_z3_wall_network.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/investigation-8/inv8_w3_kz_z3_wall_network.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/investigation-8/inv8_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^INV8-W3-1-KZ-Z3-WALL-NETWORK:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true
  wp_section:
    path: "sessions/investigation/investigation-8/investigation-8-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-1. INV8-W3-1"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

PASS_meaning: >
  The Z_3 wall network FORMS: pi_0(U(1)_7 x Z_3)=Z_3 admits walls, the KZ correlation length
  xi_hat is sub-horizon, AND the wall tension exceeds the post-transit thermal scale. The
  'no-walls' verdict (pi_0(U(1))=0) used the wrong symmetry group. A w=-2/3 dark-energy
  component and an a^{-1} BBN channel exist — ONE mechanism reaching both C-1 (DESI w_a)
  and C-4 (BBN DeltaN_eff). Solution-space: the frozen-modulus w_a=0 lock (C-1) and the
  GGE-homogeneity T2 are BOTH re-scoped; the wall network becomes a live candidate for the
  DESI w_a != 0 signal.
FAIL_meaning: >
  No Z_3 wall network survives the transit: either the homotopy argument was already correct
  (the Z_3 structure does not source codim-1 walls in the broken-symmetry manifold), or the
  sudden-quench limit + sub-threshold wall tension anneals any network. The frozen-modulus
  w_a=0 lock (C-1) stands on a SHARPER footing than before. Solution-space: the Kibble-Zurek
  route to the w_a / BBN tension is CLOSED; the running-vacuum mechanism (INV8-W2-4) is the
  surviving candidate.
INFO_meaning: >
  Walls form but anneal partially (network freezes then relaxes), OR the homotopy admits
  walls but the wall tension / equation-of-state is regime-dependent (Mach-window-sensitive).
  The gate quantifies the surviving wall fraction and its w_a contribution as a band; the
  Kibble-Zurek route is NEITHER cleanly open nor closed — it is a partial channel whose
  magnitude requires the wall-annealing dynamics (a follow-up compute).

effort:
  files_created:
    - "computations/investigation-8/inv8_w3_kz_z3_wall_network.py"
    - "computations/investigation-8/inv8_w3_kz_z3_wall_network.npz"
    - "computations/investigation-8/inv8_w3_kz_z3_wall_network.png"
  estimated_time: "0.5 day"

substrate_framing: |
  PHONONIC. The transit IS a quench of the substrate's internal spectral structure through
  the van Hove fold — not a system passing through a phase transition IN a container. The
  order-parameter manifold IS the structure the D_K spectrum reorganizes onto at tau_fold:
  the U(1)_7 BCS-condensate phase (Cooper pairs carry K_7 charge +/-1/2, B6) TIMES the Z_3
  Jensen-deformation structure (pi_0(Z_3)=Z_3, the 512-plaquette frustration §VII.AG.4). A
  Kibble-Zurek wall is a frozen-in mismatch between Z_3 sectors of the reorganized spectrum
  — a relay-pattern domain boundary, NOT a topological defect embedded in a pre-existing
  spacetime. The direction of explanation: D_K eigenvalues reorganize at the fold -> the
  Z_3 sectors of the reorganization may not be domain-selected at finite quench rate -> a
  frozen wall network is a substrate-IS interference pattern -> its w=-2/3 equation of state
  and a^{-1} energy scaling are the EMERGENT cosmological consequence (the DESI w_a candidate
  and the BBN channel). The 'no-walls' claim inverted this once by reading pi_0 off the U(1)
  factor alone; this gate reads it off the full U(1)_7 x Z_3 substrate symmetry.
```

**Cross-references (MANDATORY, so /rclab-coordinate does not see redundancy)**:
- **INV8-W3-1 (Kibble-Zurek walls) ↔ INV8-W2-4 (running-vacuum RG, einstein's wave)** — the TWO competing mechanisms for the w_a/BBN tension. NOT a shared gate, NOT duplicate: this gate computes a *frozen Z_3 wall network* (w=−2/3, codim-1); INV8-W2-4 computes an *RG-running c₁H²* of the Volovik tracking vacuum. Both FRESH (no prior investigation computed either). Convergence/competition is the `/rclab-investigate --investigation 8` close synthesis.
- **Surveyed-but-not-elevated B-4 (analog-gravity QNM ringdown)** is adjacent context: the same sonic-horizon transit that this gate quenches has a QNM spectrum (my survey B-4); cross-ref in the INV8-W1-1 / INV8-W3-1 transit context, NOT a gate here.
- Cross-investigation dedup: no prior inv-2…inv-7 gate computed a wall network; inv-4 W3-1 (de Sitter a₀ ≡ Volovik tracking) and inv-5 W1-2/W1-5 (a₄-anomaly + entropy-functional CC) touch the SAME CC but neither a wall network nor an RG c₁H².

---

## §W3-2. INV8-W3-2 — Quantum-Metric Stiffness as the Imported Hubble Backbone H(τ)

```yaml
# ---- Identity ----
gate_id: "INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU"
schema_version: "R3"
gate_type: "compute"
trigger: "[SIGN]"
classification: "PHONONIC"
agent_type: "phonon-first-cosmologist"
hypothesis: "The integrated quantum metric of the fold band, dimensionalized by M_KK as the Peotta-Torma superfluid-weight stiffness D_geom = (2 Delta_BCS / V) integral_BZ Tr g_ab^{(P_0)}(k; tau_fold) d^d k, is a substrate-IS spectral-triple invariant (g_ab = Re<d_a u|(1-P)|d_b u>, no imported scale but M_KK) that sets an emergent oscillation frequency identifiable with the Hubble backbone H(tau) the rank-1 NNU theorem (§VII.BS) currently imports; the substrate flat band has Tr g > 0 and Berry Omega = 0 EXACTLY (C=0, maximally-NON-ideal)."

method:
  description: >
    (1) Load / reconstruct the fold-band quantum metric g_ab^{(P_0)}(k; tau_fold) — this is
    the §VII.W / §VII.AF.1.OP-PROJ laboratory-IN observable R_geom = integral_BZ Tr g_ab^{(P_0)}
    d^d k (the Peotta-Torma continuum BZ-trace; the registered Pillar-III<->IV bridge, S87
    value=0.0950 at L_max=10). The quantum metric is the real part of the quantum geometric
    tensor on the lowest-band projector P_0 of the Jensen-deformed D_K at tau_fold. (2) Confirm
    the band is maximally-NON-ideal: Tr g > 0 (metrically rich) while Berry Omega = 0 EXACTLY
    (W5: K_a anti-Hermitian => Omega = 0 identically, 1.12e-16; atlas-07 ERRATUM 'g~982.5 was
    quantum metric, NOT Berry; Berry = 0'). So the ideal-band trace condition Tr g = |Omega|
    is MAXIMALLY violated (Tr g > 0 = |0|=0 is false), and the integrated bound integral Tr g
    >= 2pi|C| is saturated at C=0 from above (Tr g > 0 = 2pi*0). (3) Build the superfluid-weight
    stiffness D_geom = (2 Delta_BCS / V) integral_BZ Tr g d^d k. This is the GEOMETRIC part of
    the superfluid weight — the part that survives in a flat band where the conventional Drude
    weight vanishes (D_conv ~ d^2 E/dk^2 = 0 for a flat band). (4) Dimensionalize: D_geom has
    units of (energy)(length)^{d-2} = a stiffness; M_KK sets the overall lambda-units. A
    stiffness sets an oscillation frequency omega_stiff = sqrt(D_geom / chi) (chi = the relevant
    susceptibility / inertia). Compute omega_stiff in M_KK units. (5) Compare omega_stiff to the
    Hubble backbone H(tau): the H-parity theorem (S100a-W1-2-QEQ-DRIVE FAIL) established the
    backbone is an INPUT on a fixed background; the rank-1 NNU theorem (§VII.BS) imports exactly
    ONE dimensional scale w=M_KK. Test whether omega_stiff(fold), as a multiple of M_KK,
    reproduces the magnitude of the imported H* (triangulated <=0.04% across 3 routes, S96-S102).
  producing_script: "computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.py"

# (1) operator
operator:
  type: "ratio"
  form: "R_stiff = omega_stiff(fold) / H*_imported ; PASS if |log10(R_stiff)| < info_band AND Tr g > 0 AND Omega = 0 (the maximally-NON-ideal flat-band signature)"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "|log10(omega_stiff / H*_imported)| <= 0.5 (within half a decade => the quantum-metric stiffness IS the backbone scale); INFO band 0.5 < |log10| <= 2.0; FAIL |log10| > 2.0"
  direction: "<="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: false
  proof_ref: "null — the integral_BZ Tr g d^d k is a numerical spectral-triple integral on the L_max-truncated D_K; the stiffness-to-frequency map omega = sqrt(D/chi) is dimensional, the magnitude is numerical"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous — Tr g(k) is integrated over the BZ / substrate-distance pole; D_geom and omega_stiff are continuum reals"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "L_max-truncated D_K spectrum at tau_fold (single fold point); BZ integral over the lowest-band projector"
  L_max: "10 (canonical for the §VII.W bridge; cross-check at L_max=12 via the master cache s84_spectrum_cache_L12_tau019.npz)"
  scan_range: "N/A — single tau_fold point; the comparison is omega_stiff vs H*_imported"
  step_size: "N/A"
  tolerance: "1e-9 (reproduce the §VII.W R_geom anchor to its published precision as a self-consistency check) ; the R_stiff comparison is an OOM-band test (0.5 / 2.0 decade bands)"
  scheme: "FW"
  convention: "Peotta-Torma-D-geom-substrate-IS-OP-PROJ"
  random_seed: "N/A — deterministic"
  GPU_path: "torch.linalg (D_K block-diagonal Peter-Weyl blocks; largest block at L_max=10 is dim ~ few-thousand, fits VRAM) ; numpy.linalg fallback for the BZ-integral assembly"
  publication_precision: "6 (omega_stiff and R_stiff cited downstream in the a(t)-gap convergence synthesis with INV8-W2-1)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain
substitution_chain:
  required: true
  content: |
    Claim: "A positive integrated quantum metric (Tr g > 0) of the flat fold band sets a NONZERO
            geometric stiffness D_geom > 0, hence a real oscillation frequency omega_stiff > 0,
            EVEN THOUGH the conventional Drude weight vanishes (flat band) and Berry Omega = 0."
    Step 1: D_s = D_conv + D_geom            [Peotta-Torma 2015 decomposition]
    Step 2: D_conv ∝ <d^2 E_n / dk^2>        [single-particle Drude / band curvature]
    Step 3: fold band is FLAT (B1 PROVEN, A_2 catastrophe, van Hove) => d^2 E/dk^2 = 0 => D_conv = 0
    Step 4: D_geom = (2 Delta_BCS / V) integral_BZ Tr g_ab^{(P_0)} d^d k   [the geometric / interband term]
    Step 5: Tr g_ab^{(P_0)} = Re <d_a u|(1-P)|d_b u> traced over a,b >= 0 (positive-semidefinite quantum metric),
            and the fold band is METRICALLY RICH (the §VII.W R_geom > 0; the atlas-07 g~982.5 magnitude WAS the
            quantum metric) => integral_BZ Tr g d^d k > 0 STRICTLY.
    Step 6: Substitute: D_s = 0 + D_geom = (2 Delta_BCS / V) integral Tr g > 0   [Delta_BCS = 0.4642547... > 0]
    Direction: D_geom > 0 STRICTLY despite D_conv = 0; the superfluid weight of the flat fold band is ENTIRELY
               geometric. The stiffness is POSITIVE, so omega_stiff = sqrt(D_geom/chi) is REAL and POSITIVE.
    Berry sub-claim: Omega = 0 EXACTLY (W5, K_a anti-Hermitian) => the ideal-band bound integral Tr g >= 2pi|C|
               is SATURATED FROM ABOVE at C=0 (Tr g > 0 = 2pi*0); the band is C=0 maximally-NON-ideal.
    Conclusion: the fold band carries a strictly-positive geometric stiffness with NO Berry curvature; whether
               that stiffness IS the imported H(tau) backbone is the magnitude test (R_stiff OOM band).

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  spectrum_cache_L12:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
  dirac_spectrum_module:
    path: "computations/_shared/dirac_spectrum.py"
    sha256: "<computed-at-runtime>"

# ---- Conditional blocks ----
fb_pair:
  forward: "§VII.W / §VII.AF.1.OP-PROJ R_geom (S87-PILLAR-III-IV-BRIDGE-PERMANENT-LAND); W5 Berry=0 EXACT; Delta_BCS; M_KK (canonical); the rank-1 NNU theorem §VII.BS"
  backward: "G-1 (the a(t) gap; if omega_stiff IS H(tau) the gap closes from a substrate-IS invariant); convergence with INV8-W2-1 (Jacobson -> CC magnitude) — the TWO constructive attacks on the dimensionful-scale knot"
dual_prior:
  track_A: "0.4 — Reading_A (stiffness IS the backbone): omega_stiff(fold) reproduces H*_imported within ~half a decade => the a(t) gap's imported function H(tau) is derived from the fold-band quantum metric, a substrate-IS invariant with no new scale; G-1 closes."
  track_B: "0.6 — Reading_B (stiffness is a DIFFERENT scale): D_geom is real and positive but its dimensionful magnitude is set by Delta_BCS and the BZ volume in a way that does NOT match H*; the quantum-metric stiffness is a BCS-superfluid scale (the GGE superfluid weight, QUANTUM-METRIC-63) distinct from the cosmological Hubble backbone — the a(t) gap survives, but the gate has CHARACTERIZED the flat band as maximally-NON-ideal (a permanent structural result independent of the H(tau) question)."
  discriminator: "PASS (R_stiff within 0.5 decade) -> 0.9 to Track A; INFO (within 2 decades) -> mass split per the OOM distance; FAIL (R_stiff > 2 decades off) -> 0.9 to Track B (the maximally-NON-ideal characterization still lands as a separate structural result)."

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/investigation-8/inv8_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^INV8-W3-2-QUANTUM-METRIC-STIFFNESS-HTAU:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true
  wp_section:
    path: "sessions/investigation/investigation-8/investigation-8-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-2. INV8-W3-2"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

PASS_meaning: >
  The quantum-metric stiffness omega_stiff(fold) reproduces the imported Hubble backbone H*
  within half a decade. The a(t) gap (G-1) — the framework's #1 gap — closes from a substrate-IS
  spectral-triple invariant (the integrated quantum metric, computable from D_K eigenvectors with
  no scale beyond M_KK). The rank-1 NNU theorem's 'imported function H(tau)' is DERIVED. Solution-
  space: the conformal-class-is-not-a-cosmology objection (my G-1) is answered; the substrate now
  supplies the dimensionless tracking shape AND its dimensionful backbone.
FAIL_meaning: >
  D_geom is real and positive (the flat band IS metrically rich, maximally-NON-ideal: Tr g > 0,
  Omega = 0) but its dimensionful magnitude does NOT match H* (> 2 decades off). The quantum-metric
  stiffness is a BCS-superfluid scale, NOT the cosmological Hubble backbone. The a(t) gap survives.
  Solution-space: the constructive attack on G-1 via the quantum metric is CLOSED; the maximally-
  NON-ideal flat-band characterization (Tr g > 0, C=0) lands as a SEPARATE permanent structural
  result (the substrate's flat band is quantum-geometrically trivial in the Chern sense, consistent
  with p_1[SU(3)]=0 on g_M).
INFO_meaning: >
  omega_stiff is within 2 decades of H* but not within half a decade — the quantum-metric stiffness
  is the RIGHT order of physics but the precise identification requires the susceptibility/inertia
  chi to be pinned (the stiffness-to-frequency map has a free O(1) factor). The gate reports the
  OOM distance and the maximally-NON-ideal flat-band signature as the durable outputs; the H(tau)
  identification is a partial (order-of-magnitude) success pending the chi pin.

effort:
  files_created:
    - "computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.py"
    - "computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.npz"
    - "computations/investigation-8/inv8_w3_quantum_metric_stiffness_htau.png"
  estimated_time: "1 day"

substrate_framing: |
  PHONONIC. The quantum metric g_ab^{(P_0)} IS a substrate-IS spectral-triple invariant — it is
  the real part of the quantum geometric tensor on the lowest-band projector of D_K at tau_fold,
  computed from D_K eigenvectors with NO imported scale except M_KK setting the lambda-units. It
  is NOT a property of a band IN a Brillouin-zone container; it IS the metric structure of the
  substrate's reorganized spectral weight at the fold. The fold IS a flat band (the van Hove A_2
  catastrophe), so the conventional band-curvature Drude weight vanishes and the entire superfluid
  stiffness is GEOMETRIC: D_geom = (2 Delta_BCS / V) integral Tr g. The direction of explanation:
  D_K eigenvectors at the fold -> the quantum metric of the lowest-band projector -> the geometric
  superfluid stiffness D_geom -> an emergent oscillation frequency -> (the test) is that frequency
  the Hubble backbone H(tau) the cosmology rides on? The Berry curvature is ZERO EXACTLY (K_a is
  anti-Hermitian, a theorem on any compact Lie group), so the substrate flat band is the C=0,
  maximally-NON-ideal case: metrically rich (Tr g > 0) but topologically trivial (Omega = 0,
  p_1[SU(3)]=0). This is the cross-domain bridge B-1: the post-2015 ideal-flat-band literature
  (Roy 2014; Ledwith-Vishwanath 2020) made the Tr g <-> Omega relation precise, and the substrate
  sits at its maximally-non-ideal corner.
```

**Cross-pillar bridge anatomy (this gate REFINES the registered §VII.W / §VII.AF.1.OP-PROJ bridge)** — per `cross-pillar-bridge-anatomy.md`, the 5 anatomy elements + 3 levels + substrate-IS level:
- **Substrate-IS observable** (Element 1): the finite-L integrated quantum metric `integral_BZ Tr g_ab^{(P_0)}(k; tau_fold) d^d k` on `(A_K^{<=10}, H_K^{<=10}, D_K^{<=10})` — and its dimensionalized stiffness `D_geom`. The substrate IS this stiffness.
- **Laboratory-IN observable** (Element 2, OE-form): `R_geom = integral_BZ Tr_{lowest-band} P_{0}(k) [Provost-Vallee QGT real part] d^d k` (the Peotta-Torma continuum BZ-trace; the registered §VII.W laboratory-IN observable). The named projector is `P_0` (lowest-band).
- **Bridge map** (Element 3): HKR `L_max -> infinity` image (the same map as §VII.W / §VII.AF.1; substrate-distance-1 Connes-Karoubi pairing). Scheme suffix per the §VII.W convention.
- **Algebraic envelope** (Element 4): `L^{-3}` at d=4 (= 0.10% at L_max=10), inherited from the §VII.W Level-2-binding HKR envelope.
- **Empirical anchor** (Element 5): the §VII.W Level-3 anchor (0.0095% F_4 strict at L_max=10; Level-3/Level-2 = 0.0950, 10x inside envelope). This gate ADDS the dimensionalized-stiffness magnitude.
- **Three levels**: Level-1 (cohomology-class identity: Tr g > 0 / Omega = 0 is regulator-invariant, the maximally-NON-ideal structural identity); Level-2 (L^{-3} HKR envelope, Level-2-binding); Level-3 (numerical D_geom / omega_stiff at canonical L_max). **Substrate-IS level**: Level-1 single-tau-slice (the quantum metric at fixed tau_fold = 0.190 is intrinsic to the spectral triple at that tau-anchor). If this gate registers a NEW §VII slot for the H(tau)-identification, it is OP-PROJ (operator-projection, algebra-INVARIANT spectrum-side: a projector trace, NOT a state-pair functional) and declares the single-tau-slice level. **NOTE**: this is an investigation gate — any permanent §VII registration is session-track promotion at `/rclab-investigate` close, NOT an investigation edit.

**Cross-references (MANDATORY)**:
- **INV8-W3-2 (quantum-metric → H(τ)) ↔ INV8-W2-1 (Jacobson → CC magnitude, einstein's wave)** — the TWO constructive attacks on the dimensionful-scale knot. NOT a shared gate, NOT duplicate: this gate attacks the *Hubble backbone H(τ)* (the imported FUNCTION) from the fold-band quantum-metric stiffness; INV8-W2-1 attacks the *CC magnitude* (an imported NUMBER) from the §VII.BZ modular entanglement-equilibrium. Their convergence (do both land on the same dimensionful scale?) is the `/rclab-investigate --investigation 8` close synthesis, NOT a plan-time gate.

---

## §W3-3. INV8-W3-3 — Spectral Dimension P(σ) at L_max=14-16: the CDT / Asymptotic-Safety Comparison

```yaml
# ---- Identity ----
gate_id: "INV8-W3-3-SPECTRAL-DIMENSION-LMAX14-CDT"
schema_version: "R3"
gate_type: "compute"
trigger: "[CHAIN]"
classification: "GEOMETRIC"
agent_type: "spectral-geometer"
hypothesis: "Pushing the heat-trace return probability P(sigma) = Tr e^{-sigma D_K^2} to L_max=14-16 (the GT-builder lifted the Sym^13/14 wall at S104/S105) escapes the narrow-band artifact and yields BOTH d_s(sigma->0) -> 8 (the Weyl / SU(3)-manifold dimension) AND a windowed d_s(sigma_*) at the fold; the CDT / asymptotic-safety dimensional-reduction comparison is made fairly via the energy-axis DOS exponent gamma_E (the diffusion-window K=2 specialization), with the (observable, diffusion-window) pair fixed on BOTH sides and the same functional Phi applied at the same scale-type."

method:
  description: >
    (1) MANDATORY multiplicative-normalization-cancellation pre-flight (math-scripts.md §K=3):
    determine whether L_max enters P(sigma) as a multiplicative spectral-support pre-factor
    w(L_max) * g(sigma) where g(sigma) is L_max-independent. The heat trace P(sigma) =
    Sum_{(p,q)} dim(p,q) Sum_i exp(-sigma lambda_i^2) ADDS new (p,q) sectors as L_max grows
    (it is NOT a pure multiplicative rescale of a fixed kernel — each new sector adds modes at
    new lambda values), so d_s = -2 dlnP/dlnsigma is NOT expected to be multiplicatively-
    cancelled. CONFIRM via Sage symbolic factorization (sage_simplify) that P(sigma) does not
    factor as w(L_max)*g(sigma); record the verdict. If multiplicative factorization HELD, the
    L_max-plateau of d_s would be a STRUCTURAL identity (not empirical L_max-stability) and the
    PASS criterion would target the asymptote value, not the L_max-stability per se. (2) Build
    the NORMAL-STATE (Delta=0, bare D_K) heat trace on the converged-L_max spectrum: load the
    L_max=12 master cache (s84_spectrum_cache_L12_tau019.npz), extend to L_max=14,15,16 via the
    GT-builder (s104_branch_iv_phase1_builder.py + the Sym^p chain cache s104_sym_p_chain_cache_
    L1314.npz that lifted the Sym^13/14 wall). (3) FEASIBILITY GATE (math-scripts.md §D_K Block-
    Diagonality + Recursive-Casimir-Projection): D_K is block-diagonal by Peter-Weyl; irrep
    CONSTRUCTION at p+q >= 13 may time out. Pin the Casimir-bound feasibility argument: bound
    the worst-case new sector via |lambda|_min^(p,q) ~ sqrt(C_2(p,q))/r(tau), and the Friedrich-
    Bar saturation eta_FB(p,q) = |lambda|_min/sqrt(C_2+1); if the new-sector eigenvalue floor at
    p+q=L_max exceeds the UV window's lambda ceiling for d_s(sigma->0), the small-sigma asymptote
    is structurally saturated. Declare L_max_plan = 16 and L_max_operational = the largest p+q the
    GT-builder completes within the agent timeslot; cross-check the L_max=12 anchor reproduces
    bit-for-bit on the operational truncation. (4) Compute d_s(sigma->0): the small-sigma slope
    of -2 dlnP/dlnsigma should approach the Weyl/MP manifold dimension = 8 (dim SU(3)). (5)
    Compute d_s(sigma_*) at the fold window sigma_* = d_s_fold_window_sigma = 1.4005 M_KK^{-2}
    (canonical). (6) The CDT comparison via the energy-axis gamma_E (the diffusion-window K=2
    specialization, cross-pillar-bridge-anatomy.md §"Single-observable-per-triple structural
    filter" / §24): fix the (observable, diffusion-window) pair on BOTH sides — compare the
    substrate d_s^{substrate}(sigma_*) = Phi[P_{D_K}](sigma_*) to CDT's d_s^{CDT}(intermediate-
    window plateau) = Phi[P_CDT](sigma_CDT-window) using the SAME functional Phi at the SAME
    scale-type, with the directly-fitted energy-axis DOS exponent gamma_E as the discriminator
    (rho_E(lambda) ~ lambda^{gamma_E}; the impedance Z = rho_E v_g is a consistency check, not a
    lock). Use the gamma_E estimator (s93-w7-3-gamma-e-dos-exponent-estimator, eq_6934-6942).
  producing_script: "computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.py"

# (1) operator
operator:
  type: "inequality"
  form: "|d_s(sigma->0) - 8| < tol_UV  (Weyl-dimension recovery)  AND  gamma_E fitted at L_max>=14 stable to within tol_gamma across L in {12,14,15,16}  (escape of the narrow-band artifact)"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "|d_s(sigma->0) - 8| <= 0.5 (UV Weyl recovery) AND |gamma_E(L_max=16) - gamma_E(L_max=14)| <= 0.10 (L_max-convergence of the energy-axis DOS exponent)"
  direction: "<="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "Weyl asymptotic: d_s(sigma->0) = dim(manifold) = dim SU(3) = 8 (canonical_constants.py d_s_fold_window_sigma note 'UV d_s->8'); the gamma_E convergence is an empirical L_max-stability test"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "the UV target d_s->8 is an integer; gamma_E is a continuum-fitted real (L_max scan {12,14,15,16})"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "heat-trace evaluated over a log-sigma grid (>= 200 points spanning the UV asymptote to the fold window); per-L_max in {12,14,15,16}"
  L_max: "L_max_plan = 16; L_max_operational = largest p+q the GT-builder completes within timeslot (>= 14 per S105-BRANCH-IV-DIRECT-L1314 deep-set landing); both recorded in npz"
  scan_range: "log10(sigma) in [-4, +1] M_KK^{-2} (UV small-sigma to the fold window sigma_*=1.4005); L_max scan {12,14,15,16}"
  step_size: "200 log-sigma points; L_max integer steps"
  tolerance: "tol_UV = 0.5 (Weyl recovery); tol_gamma = 0.10 (gamma_E L_max-convergence); the L_max=12 anchor bit-match floor 1e-12"
  scheme: "zeta"
  convention: "NORMAL-STATE-Delta0-heat-trace-energy-axis-gamma_E ; diffusion-window-K2-specialization"
  random_seed: "N/A — deterministic"
  GPU_path: "torch.linalg for any per-block diagonalization the GT-builder needs at p+q in {13,14,15,16}; numpy for the heat-trace sum over the cached spectrum (vectorized exp)"
  regulator_pin: "a_n^{ζ}  (the heat-trace small-sigma expansion is the zeta-regulated Seeley-DeWitt asymptotics; the leading a_0^{ζ} term sets d_s(sigma->0)=8)"
  publication_precision: "4 (d_s and gamma_E cited downstream in the CDT-comparison synthesis)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain
substitution_chain:
  required: true
  content: |
    Claim: "P(sigma) = Tr e^{-sigma D_K^2} does NOT factor as w(L_max)*g(sigma) with g L_max-independent;
            therefore d_s = -2 dlnP/dlnsigma is a GENUINE L_max-dependent observable and its convergence at
            L_max=14-16 is empirical evidence of escape from the narrow-band artifact, NOT a structural-identity
            plateau."
    Step 1: P(sigma) = Sum_{(p,q): p+q <= L_max} dim(p,q) Sum_{i in sector (p,q)} exp(-sigma lambda_i^2)   [heat trace; NORMAL state]
    Step 2: Increasing L_max -> L_max+1 ADDS new sectors {(p,q): p+q = L_max+1} with NEW eigenvalues lambda_i at NEW magnitudes
            (the new sectors have higher Casimir C_2(p,q), hence larger |lambda|_min ~ sqrt(C_2)/r(tau)).
    Step 3: P_{L_max+1}(sigma) = P_{L_max}(sigma) + [new-sector contribution](sigma)   [ADDITIVE in sigma-dependent terms, not multiplicative]
    Step 4: Therefore P_{L_max+1}(sigma) / P_{L_max}(sigma) is sigma-DEPENDENT (the new sectors weight large-lambda => they reshape the small-sigma UV tail),
            so there is NO L_max-independent kernel g(sigma) with P(sigma) = w(L_max) g(sigma).
    Step 5: d ln P / d ln sigma picks up the new-sector reshaping => d_s(sigma) genuinely flows with L_max in the UV window until the
            sector sum is converged (the Weyl tail is saturated). This is the OPPOSITE of the multiplicative-normalization case
            (math-scripts.md §K=3, where a w(L_max) pre-factor is annihilated by the log-derivative).
    Direction: the multiplicative-normalization-cancellation pre-flight returns FALSE (no factorization);
               hence the gate's PASS criterion correctly targets the L_max-STABILITY of d_s/gamma_E (empirical convergence),
               NOT an asymptote-value-only test. The Sage sage_simplify factorization check at plan-freeze CONFIRMS this
               (the additive-new-sector structure is not a product form).
    Conclusion: d_s(sigma->0)->8 (Weyl) and the L_max-convergent gamma_E are genuine spectral observables; the CDT comparison
               is fair iff Phi and the diffusion-window are matched on both sides (the K=2 specialization).

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  spectrum_cache_L12:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
  gt_builder:
    path: "computations/session-104/s104_branch_iv_phase1_builder.py"
    sha256: "<computed-at-runtime>"
  sym_p_chain_cache:
    path: "computations/session-104/s104_sym_p_chain_cache_L1314.npz"
    sha256: "<computed-at-runtime>"
  dirac_spectrum_module:
    path: "computations/_shared/dirac_spectrum.py"
    sha256: "<computed-at-runtime>"

# ---- Conditional blocks ----
fb_pair:
  forward: "s84_spectrum_cache_L12_tau019.npz (the L_max=12 master spectrum); the GT-builder + Sym^p chain cache (S104/S105 Sym^13/14 unlock); d_s_fold_window_sigma=1.4005 (canonical); the gamma_E estimator (s93-w7-3)"
  backward: "R-1 (the spectral-dimension / CDT comparison — currently asserted as a resonance, never measured); the dimensional-reduction analogy to CDT/asymptotic-safety is CONFIRMED or KILLED; complementary to inv-3 W2-1 (d_s-flow as K->K* map) + inv-3 W2-2 (isospectral rigidity at L_max=3)"
dual_prior:
  track_A: "0.5 — Reading_A (dimensional reduction CONFIRMED): d_s(sigma->0)->8 (UV Weyl) and a LOWER windowed d_s(sigma_*) at the fold, with gamma_E reproducing the CDT/asymptotic-safety intermediate-window reduction (the substrate flows from d_s=8 toward a lower windowed dimension, matching the CDT pattern when Phi and the window are matched). The asserted resonance becomes a measured result."
  track_B: "0.5 — Reading_B (no fair reduction / artifact-dominated): either the GT-builder cannot reach L_max high enough to escape the narrow-band artifact (gamma_E still L_max-unstable at the operational truncation), OR when the (observable, window) pair is matched the substrate d_s does NOT reproduce the CDT reduction — the resonance was a scale-type mismatch (comparing the substrate UV asymptote to CDT's intermediate window). The honest verdict is 'comparison not yet decidable' or 'no reduction on the matched functional'."
  discriminator: "PASS (d_s->8 recovered AND gamma_E L_max-convergent) -> 0.9 to Track A; INFO (UV recovered but gamma_E marginal / window-sensitive) -> mass split per the convergence quality; FAIL (artifact-dominated at operational L_max, or matched-functional reduction absent) -> 0.9 to Track B."

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/investigation-8/inv8_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^INV8-W3-3-SPECTRAL-DIMENSION-LMAX14-CDT:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/investigation/investigation-8/investigation-8-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-3. INV8-W3-3"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

PASS_meaning: >
  d_s(sigma->0) recovers the Weyl manifold dimension 8 (escape of the narrow-band artifact
  confirmed) AND the energy-axis gamma_E is L_max-convergent across {12,14,15,16}, so the
  CDT/asymptotic-safety dimensional-reduction comparison is MADE (not asserted) on the matched
  functional. Solution-space: R-1 closes — the substrate's spectral dimension is measured at
  high enough L_max to compare to CDT, and the dimensional-reduction analogy is either confirmed
  (Track A) at the matched scale-type. A standing fence (my MEMORY: 'DO NOT compare d_s to CDT
  until L_max >> 6') is lifted.
FAIL_meaning: >
  Either the GT-builder cannot reach L_max high enough to escape the narrow-band artifact within
  the agent timeslot (gamma_E still L_max-unstable at the operational truncation) OR, on the
  matched (observable, window) functional, the substrate d_s does NOT reproduce the CDT reduction.
  Solution-space: the asserted CDT resonance is NOT a measured result; the dimensional-reduction
  analogy is downgraded from 'asserted' to 'not-yet-decidable' or 'absent on the matched
  functional'. The narrow-band-artifact fence remains until a higher L_max is reachable.
INFO_meaning: >
  UV Weyl recovery (d_s->8) succeeds but gamma_E is marginal (L_max-convergence between tol and
  2*tol) or window-sensitive. The gate reports d_s(sigma->0), d_s(sigma_*), and gamma_E with the
  L_max-convergence quality as a band; the CDT comparison is partially made (the UV is clean, the
  intermediate window needs more L_max). Multiplicative-normalization pre-flight verdict (FALSE,
  no factorization) is recorded regardless.

effort:
  files_created:
    - "computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.py"
    - "computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.npz"
    - "computations/investigation-8/inv8_w3_spectral_dimension_lmax14_cdt.png"
  estimated_time: "1.5 days (GT-builder irrep construction at p+q in {13..16} is the wall-clock bottleneck)"

substrate_framing: |
  GEOMETRIC. The return probability P(sigma) = Tr e^{-sigma D_K^2} IS the substrate's own heat
  trace — the spectral fingerprint of the D_K eigenvalue spectrum, the set of all vibrational
  modes of the fabric. The spectral dimension d_s(sigma) = -2 dlnP/dlnsigma is a substrate-IS
  functional of that fingerprint; it is NOT a property of a diffusion process IN a background
  geometry. d_s(sigma->0) -> 8 because the small-sigma limit probes the full SU(3) manifold
  dimension (the Weyl asymptotic of the bare D_K). The CRITICAL framing discipline (phononic-
  framing.md §"Same-functional-different-scale fair-comparison", K=2): do NOT let the CDT /
  asymptotic-safety framework's scale-type be authoritative over the substrate's own. The
  substrate IS the return probability; d_s(sigma->0) (Weyl asymptotic) and d_s(sigma_*) (windowed
  at the fold) are TWO intrinsic functionals of it. Comparing the substrate's sigma->0 asymptote
  to an external framework's intermediate-window value is a container-thinking violation at the
  observable layer. The fix: fix the (observable, diffusion-window) pair on BOTH sides; compare
  the same functional Phi at the same scale-type; the discriminator is the directly-fitted
  energy-axis DOS exponent gamma_E (the impedance Z = rho_E v_g is a consistency check, not a
  lock). The direction of explanation: D_K eigenvalue spectrum -> heat trace P(sigma) -> spectral
  dimension functional d_s -> (the comparison) does the substrate's matched-window d_s reproduce
  the CDT dimensional-reduction pattern? This is the high-L_max measurement the framework asserts
  but never made.
```

**Cross-references (MANDATORY)**:
- **INV8-W3-3 ↔ inv-3 W2-1 (d_s-flow as K→K* map) + inv-3 W2-2 (isospectral rigidity at L_max=3)** — same heat-trace d_s observable, but this gate is the HIGH-L_max (14-16) CDT/asymptotic-safety dimensional-reduction comparison (the GT-builder unlock), distinct from the K→K* scale-transport map (inv-3 W2-1) and the low-L_max isospectral rigidity test (inv-3 W2-2). Complementary, NOT duplicate.
- **INV8-W3-3 ↔ INV8-W1-4 (mack's wave, finite-L no-go theorem)** — they share the "what a finite truncation can / cannot reach in a spectral sum" theme; W1-4 proves which analytic-continuation poles a truncation misses, W3-3 measures the heat-trace spectral dimension at the highest reachable L_max. Co-dispatchable (both spectral-geometer-executed, no observational input). Cross-reference, not a shared gate.

---

## §W3-4. INV8-W3-4 — Higgs Quartic λ(μ) Running: Substrate Stability vs SM Near-Criticality

```yaml
# ---- Identity ----
gate_id: "INV8-W3-4-HIGGS-QUARTIC-RG-STABILITY"
schema_version: "R3"
gate_type: "compute"
trigger: "[SIGN]"
classification: "PARTICLE"
agent_type: "phonon-first-cosmologist"
hypothesis: "Running the Higgs quartic lambda(mu) from the framework's predicted m_H = 131.8 GeV (Route-B KK-threshold) up to M_KK = 7.43e16 GeV on the substrate spectrum determines whether the substrate vacuum is absolutely stable (lambda stays positive all the way to M_KK — a prediction distinguishing the substrate from the SM) or reproduces SM near-criticality (lambda -> 0 near a high scale ~10^10-10^11 GeV — strong evidence the spectral-action cutoff f IS physical, since the RG running of lambda is a genuine dynamical statement, not a regulator artifact)."

method:
  description: >
    (1) Tree-level matching: the Higgs is the transverse |S|^2 oscillation of the fiber embedding;
    its tree quartic is lambda_tree = m_H^2 / (2 v_ew^2) with m_H = m_H_FW_KK_threshold = 131.8 GeV,
    v_ew = 246.0 GeV. Cross-check against the SM-observed lambda_tree(125.1). (2) Run lambda(mu) via
    the RG: the SM beta-function beta_lambda = (1/16pi^2)[24 lambda^2 - 6 y_t^4 + (3/8)(2 g^4 + (g^2+g'^2)^2) + lambda(...)]
    + the SUBSTRATE corrections from the KK-threshold spectrum (the new states at M_KK enter the
    beta-functions above the threshold scale; below M_KK the running is SM-like with the substrate-
    fixed boundary value lambda(m_H)). Use the substrate spectrum (the L12 cache) to set the
    threshold structure. Run from m_H = 131.8 GeV up to M_KK. (3) Detect the sign of lambda(mu):
    does lambda(mu) cross zero at some mu_* < M_KK (near-criticality / metastability) or stay
    positive all the way (absolute stability)? (4) Compare to the SM benchmark: Degrassi 2012 /
    Buttazzo 2013 place the SM (m_H=125 GeV, m_t=173 GeV) in a metastable regime with lambda(mu)
    < 0 at ~10^10-10^11 GeV (methodological cross-check anchor, NOT a canonical value source). The
    substrate's m_H=131.8 GeV is HIGHER than the observed 125.1, so lambda_tree is LARGER (verified
    at plan-freeze: 0.1435 vs 0.1293) => the substrate starts FURTHER from the instability boundary.
    The question is whether the substrate beta-function (with its KK-threshold corrections and its
    own top-Yukawa, if the substrate fixes y_t) drives lambda to zero before M_KK or keeps it
    positive.
  producing_script: "computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.py"

# (1) operator
operator:
  type: "set"
  form: "sign(lambda(mu)) for mu in [m_H, M_KK]: ABSOLUTE-STABILITY iff lambda(mu) > 0 for all mu in [m_H, M_KK]; NEAR-CRITICALITY iff exists mu_* < M_KK with lambda(mu_*) = 0 (and lambda < 0 above)"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "min_{mu in [m_H, M_KK]} lambda(mu) : if min > 0 => ABSOLUTE-STABILITY (one structural outcome); if exists mu_* with lambda(mu_*)=0 at mu_* in [10^9, 10^13] GeV => NEAR-CRITICALITY (the other structural outcome). Both are RESULTS; the verdict maps to the solution-space reading, not a single threshold direction."
  direction: ">="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "lambda_tree = m_H^2/(2 v_ew^2) is closed-form (verified at plan-freeze: 0.14352600965 at m_H=131.8); the running is a 1-loop (optionally 2-loop) RG ODE integration — the crossing scale mu_* is an ODE root, analytically characterizable"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "continuous — lambda(mu) is a continuum RG trajectory; the crossing scale mu_* is a continuum real"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "RG ODE integrated over log(mu) in [log(m_H), log(M_KK)] with >= 500 steps; tree match at m_H"
  L_max: "10 (the substrate KK-threshold spectrum sets the boundary value; cross-check the threshold structure via the L12 cache)"
  scan_range: "mu in [131.8, 7.428660036284456e16] GeV (m_H to M_KK)"
  step_size: "500 log-mu RG steps (adaptive for the ODE)"
  tolerance: "1e-6 (lambda(mu) relative ODE tolerance); the sign-crossing detection is a SIGN, not a magnitude tolerance"
  scheme: "MS"
  convention: "MSbar-1loop-SM-plus-KK-threshold ; substrate-boundary-lambda(m_H)=m_H^2/(2 v_ew^2)"
  random_seed: "N/A — deterministic"
  GPU_path: "cpu-cap-OMP8 (RG ODE is scalar; the threshold-spectrum read is a small cache load)"
  publication_precision: "4 (lambda(M_KK) and mu_* cited downstream in the metastability / A-3 synthesis)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain
substitution_chain:
  required: true
  content: |
    Claim: "The substrate's boundary quartic lambda(m_H=131.8) is LARGER than the SM-observed
            lambda(m_H=125.1); the substrate therefore starts FURTHER from the SM instability
            boundary, so absolute stability is the a-priori-favored outcome and any lambda->0
            crossing requires the substrate beta-function to drive HARDER negative than the SM."
    Step 1: lambda_tree = m_H^2 / (2 v_ew^2)        [tree matching; m_H the |S|^2 transverse mode mass, v_ew=246.0]
    Step 2: lambda_tree(m_H=131.8) = 131.8^2 / (2*246.0^2) = 17371.24 / 121032 = 0.143526   [verified at plan-freeze]
    Step 3: lambda_tree(m_H=125.1) = 125.1^2 / (2*246.0^2) = 15650.01 / 121032 = 0.129305   [SM-observed benchmark]
    Step 4: m_H_FW = 131.8 > m_H_obs = 125.1  =>  lambda_tree(FW) - lambda_tree(obs) = 0.014221 > 0
    Direction: the substrate boundary quartic is LARGER (more positive) than the SM-observed value.
               A larger initial lambda means the RG must run DOWN by a larger amount to reach lambda=0,
               so at fixed beta-function the substrate crosses zero (if at all) at a HIGHER scale than the SM,
               or NOT at all (absolute stability). The substrate sits FURTHER from instability at tree level.
    Conclusion: the well-posed sign question is whether the substrate beta-function (SM running + KK-threshold
               corrections above M_KK; the substrate's own y_t if fixed) drives lambda to zero below M_KK
               (near-criticality, reproducing the SM coincidence from geometry) or keeps it positive
               (absolute stability, a substrate prediction distinct from the SM). The tree-level direction
               FAVORS stability; the gate computes which wins after running.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  spectrum_cache_L12:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"

# ---- Conditional blocks ----
fb_pair:
  forward: "m_H_FW_KK_threshold=131.8 (canonical, Route-B); v_ew=246.0; m_H_obs=125.1 (canonical); M_KK=7.428660036284456e16; the substrate KK-threshold spectrum (L12 cache)"
  backward: "A-3 (is the spectral-action cutoff f physical? — if the substrate reproduces SM near-criticality from geometry, the RG running of lambda is a genuine dynamical statement => strong evidence f IS physical, the deepest assumption behind the n_s prediction); B-5 metastability; the EW-vacuum-stability sector (currently un-engaged)"
dual_prior:
  track_A: "0.45 — Reading_A (absolute stability): lambda(mu) > 0 all the way to M_KK; the substrate vacuum is absolutely stable, a CLEAN prediction distinguishing the substrate from the metastable SM. Solution-space: the substrate makes a falsifiable stability statement; A-3 is NOT directly bridged (stability is a different claim from near-criticality)."
  track_B: "0.55 — Reading_B (near-criticality reproduced): lambda(mu) -> 0 near ~10^10-10^11 GeV, reproducing the SM near-criticality coincidence FROM GEOMETRY (the KK-threshold-fixed boundary value + the substrate spectrum). Solution-space: a stunning result — the substrate reproduces one of particle physics' deepest coincidences, which is strong evidence the spectral-action f IS physical (bridges A-3), since the lambda running is dynamical, not a regulator artifact."
  discriminator: "min lambda > 0 (no crossing below M_KK) -> 0.9 to Track A (absolute stability); lambda crossing at mu_* in [10^9, 10^13] GeV -> 0.9 to Track B (near-criticality, bridges A-3); lambda crossing well outside that window (e.g. mu_* < 10^6 GeV, immediate instability) -> the substrate m_H/spectrum is in tension with vacuum stability (a FAIL-direction structural finding)."

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/investigation-8/inv8_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^INV8-W3-4-HIGGS-QUARTIC-RG-STABILITY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: true
  wp_section:
    path: "sessions/investigation/investigation-8/investigation-8-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-4. INV8-W3-4"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

PASS_meaning: >
  EITHER outcome is a result. ABSOLUTE-STABILITY (lambda > 0 to M_KK): the substrate predicts an
  absolutely stable vacuum, a clean falsifiable statement distinguishing it from the metastable SM.
  NEAR-CRITICALITY (lambda -> 0 at ~10^10-10^11 GeV): the substrate reproduces the SM near-criticality
  coincidence from geometry, strong evidence the spectral-action cutoff f IS physical (bridges A-3, the
  deepest unsupported assumption behind the n_s prediction). The verdict-line value records which outcome
  and the crossing scale mu_* (or 'no-crossing'). Solution-space: the EW-vacuum-stability sector is
  engaged for the first time; either branch constrains the f-physicality question (A-3).
FAIL_meaning: >
  lambda(mu) crosses zero at an anomalously LOW scale (mu_* < ~10^6 GeV) — the substrate m_H=131.8 GeV
  together with its spectrum and top-Yukawa would imply near-immediate vacuum instability, in tension with
  the observed long-lived vacuum. Solution-space: this would flag a problem with the Route-B m_H prediction
  or the substrate's matching to the SM Yukawa sector — a structural tension, NOT a benign result.
INFO_meaning: >
  lambda(mu) approaches zero (within ~0.01 of crossing) near a high scale but does not cleanly cross within
  the 1-loop integration uncertainty, OR the crossing scale depends sensitively on the (uncertain) substrate
  top-Yukawa matching. The gate reports lambda(M_KK), the minimum of lambda(mu), and the would-be crossing
  scale as a band; the stability-vs-near-criticality verdict is regime-sensitive (needs the y_t pin or 2-loop).

effort:
  files_created:
    - "computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.py"
    - "computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.npz"
    - "computations/investigation-8/inv8_w3_higgs_quartic_rg_stability.png"
  estimated_time: "1 day"

substrate_framing: |
  PARTICLE. The Higgs is the transverse |S|^2 oscillation of the fiber embedding — a specific
  excitation mode of the substrate's reorganized spectral structure, NOT a scalar field living
  IN spacetime. Its mass m_H = 131.8 GeV is fixed by the KK-threshold corrections to that fiber
  mode (Route-B, 0-free-param up to M_KK). The quartic self-coupling lambda is the quartic
  spectral-action vertex of that mode. Running lambda(mu) from m_H to M_KK is asking how that
  vertex evolves as the substrate is probed at higher energy — a genuine dynamical statement about
  the substrate's spectral-action structure, NOT a regulator artifact. This is precisely why the
  result bridges A-3 (the f-physicality question): if the substrate reproduces SM near-criticality
  (lambda -> 0 at a high scale) from the KK-threshold-fixed boundary value, that is the spectral
  action behaving as a physical dynamics with a physical cutoff f, not as a mathematical regulator.
  The direction of explanation: D_K KK-threshold spectrum -> the |S|^2 fiber-mode mass m_H and its
  quartic vertex lambda -> the RG running of lambda -> (the test) does the substrate predict absolute
  stability (a distinct prediction) or reproduce the SM near-criticality coincidence (evidence f is
  physical)?
```

**Cross-references (MANDATORY)**:
- **INV8-W3-4 ↔ inv-5 W1-1 (Pati-Salam m_H VALUE) + inv-5 W2-3 (Pekker-Varma Higgs self-energy) + inv-5 W3-3 (Higgs-residual synthesis)** — all touch the Higgs sector, but this gate is the RG-RUNNING / metastability question (does λ→0 near a high scale, or stay positive to M_KK?), distinct from the m_H-VALUE +5.36% residual computes. Complementary, NOT duplicate.
- **Surveyed-but-not-elevated mack B4 (vacuum-decay rate Γ(τ_fold→τ′) as the τ_fold metastability selector)** is adjacent context: the same metastability physics; cross-ref in this gate's context, NOT a gate here.

---

## §W3-5. INV8-W3-5 — Watanabe-Murayama Goldstone Branch Count (6-vs-7 Theorem)

```yaml
# ---- Identity ----
gate_id: "INV8-W3-5-WATANABE-MURAYAMA-BRANCH-COUNT"
schema_version: "R3"
gate_type: "compute"
trigger: "[VERIFY-THEOREM]"
classification: "PHONONIC"
agent_type: "phonon-first-cosmologist"
hypothesis: "The phonon branch count is settled as a representation-theoretic THEOREM by the exact non-Lorentz-invariant Goldstone-counting formula n_NG = (dim G - dim H) - (1/2) rank(rho), where rho_ab = -i<[Q_a, Q_b]> is the Watanabe-Murayama matrix of broken-charge commutators computed from the D_K / Kosmann-connection algebra; z=2 (known, EXACT) implies the principal mode is Type-B (quadratic), so rank(rho) >= 2 and the count is fixed by rank(rho) WITHOUT the deferred full SU(3) sigma-model — settling the parked 6-vs-7 and classifying which branches are Type-A (acoustic, feed the GGE pair count -> A_s) vs Type-B."

method:
  description: >
    (1) Enumerate the broken-symmetry pattern at the fold: the BCS condensate breaks U(1)_7
    (Cooper pairs carry K_7 charge +/-1/2, B6 PROVEN), and the relevant generator set is the
    Jensen-stabilizer-vs-coset split — su(2)+u(1) stabilizer (3+1 generators) and the C^2 Higgs
    coset (4 generators, T_coset, session-73a) plus the U(1)_7 phase. Identify dim G and dim H
    (the unbroken stabilizer) at tau_fold, hence dim(G/H) = the number of broken generators.
    (2) Build the broken charges Q_a as the Kosmann-connection operators K_a (the natural
    anti-Hermitian connection on the spinor bundle; the BCS interaction generators). Compute the
    Watanabe-Murayama matrix rho_ab = -i <[Q_a, Q_b]> as the ground-state (post-condensate)
    expectation of the commutators of the broken charges. rho_ab is antisymmetric; compute its
    RANK (an even integer, since antisymmetric). (3) Apply the exact counting theorem (Watanabe-
    Murayama PRL 108.251602 2012; Hidaka PRL 110.091601 2013): n_NG = (dim G - dim H) - (1/2)
    rank(rho). The Type-B modes count once per PAIR of broken generators with nonzero rho (they
    pair up); the Type-A modes count once each. (4) Cross-check the z=2 consistency: the framework
    knows z=2 EXACT for the principal B-sector mode (omega_B = 0.0019 + 7.0415 lambda_n, residual
    7e-15; DYNAMICAL-EXPONENT-63). z=2 (quadratic dispersion) is the Type-B signature => at least
    one pair of broken charges has nonzero rho => rank(rho) >= 2. Verify the computed rho rank is
    consistent with z=2. (5) Settle 6-vs-7: the S82-W0-A-BRANCH-COUNT INFO value=6 (3 amplitude +
    3 phase) is the number under test; n_NG from the theorem either confirms 6 or yields 7. Classify
    each branch Type-A (acoustic, omega ~ k) vs Type-B (omega ~ k^2): the Type-A count feeds the GGE
    pair-production (59.8 pairs) and hence A_s; the Type-B modes have a different finite-T fate.
  producing_script: "computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.py"

# (1) operator
operator:
  type: "equality"
  form: "n_NG = (dim G - dim H) - (1/2) rank(rho_ab)  [representation-theoretic identity; the PASS is the THEOREM holding, not a scalar-threshold comparison]"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "N/A — theorem-form gate (no scalar threshold). The PASS criterion is: (i) rho_ab = -i<[Q_a,Q_b]> computed exactly from the Kosmann algebra with rank determined to integer precision (antisymmetric => even rank), (ii) n_NG = (dim G - dim H) - (1/2) rank(rho) evaluated, (iii) the result is consistent with z=2 (rank(rho) >= 2, at least one Type-B pair), (iv) the 6-vs-7 question is RESOLVED to a definite integer with the Type-A/Type-B classification stated."
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "Watanabe-Murayama PRL 108.251602 (2012); Hidaka PRL 110.091601 (2013) — exact counting theorem. rho_ab from the Kosmann commutators is a finite-dimensional antisymmetric matrix; its rank is an exact integer (Sage-exact). N/A-with-reason for the scalar PRDR items (2)(3)(4): this is a representation-theoretic identity, NOT a numerical-threshold gate."

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "the whole computation is integer/rational: dim G, dim H, rank(rho) are integers; n_NG is an integer; Sage-exact"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "the broken-charge set (dim(G/H) generators) and the antisymmetric rho_ab matrix (dim(G/H) x dim(G/H)); rank via exact linear algebra"
  L_max: "10 (the Kosmann generators K_a and the ground-state expectation <[Q_a,Q_b]> are evaluated on the L_max=10 / L_max=12 D_K spectral data; the commutator structure is L_max-robust by the algebra)"
  scan_range: "N/A — single fold point; representation-theoretic"
  step_size: "N/A"
  tolerance: "1e-12 (the <[Q_a,Q_b]> expectations computed to machine precision; the rank is determined by an exact/near-exact singular-value gap — Sage-exact where the algebra permits)"
  scheme: "FW"
  convention: "Watanabe-Murayama-rho-ab-Kosmann-broken-charge ; Type-A-Type-B-classification"
  random_seed: "N/A — deterministic"
  GPU_path: "numpy.linalg / Sage for the small antisymmetric rho_ab rank (dim(G/H) is small, <= ~8); torch.linalg only if the K_a matrices on the L12 cache are large"
  publication_precision: "exact (n_NG and rank(rho) are integers; cited downstream in the branch-count theorem registration and the A_s pair-count synthesis)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["script", "canonical", "pinmap"]
  content_sha256_inputs: ["script"]

# (7) substitution_chain
substitution_chain:
  required: true
  content: |
    Claim: "z=2 (EXACT, principal B-sector mode) implies the principal branch is Type-B, hence at least
            one pair of broken charges has nonzero rho_ab, hence rank(rho) >= 2; the branch count
            n_NG = (dim G - dim H) - (1/2) rank(rho) is therefore SHIFTED BELOW the naive coset dimension
            by exactly (1/2) rank(rho)."
    Step 1: n_NG = (dim G - dim H) - (1/2) rank(rho_ab)        [Watanabe-Murayama 2012; rho_ab = -i<[Q_a,Q_b]>]
    Step 2: Type-A mode: omega ~ k (linear, z=1); Type-B mode: omega ~ k^2 (quadratic, z=2).   [WM classification]
    Step 3: framework principal mode has z=2 EXACT (omega_B = 0.0019 + 7.0415 lambda_n, residual 7e-15; EXPONENT-63)
            => the principal branch is Type-B.
    Step 4: a Type-B mode arises iff a PAIR of broken generators (Q_a, Q_b) has <[Q_a,Q_b]> != 0
            => rho_ab has a nonzero 2x2 antisymmetric block => rank(rho) >= 2.
    Step 5: Substitute: n_NG = (dim G - dim H) - (1/2) rank(rho) <= (dim G - dim H) - 1   [since rank(rho) >= 2]
    Direction: the Type-B pairing REDUCES the count below the naive broken-generator count by (1/2)rank(rho).
               If (dim G - dim H) = k broken generators and rank(rho) = 2r, then n_NG = k - r.
               The 6-vs-7 question is exactly: what is k (the broken-generator count) and what is r (the
               number of Type-B pairs)? Plan-freeze enumeration (illustrative): k=6,r=0 -> n_NG=6 (all Type-A);
               k=7,r=1 -> n_NG=6; k=6,r=1 -> n_NG=5; etc. The theorem makes the count DEPEND ON rank(rho),
               which z=2 forces to be >= 2.
    Conclusion: settling 6-vs-7 requires computing BOTH (dim G - dim H) (the broken-generator count) AND
               rank(rho_ab) (the number of Type-B pairs) from the Kosmann algebra; z=2 guarantees rank(rho) >= 2,
               so the count is NOT the naive coset dimension. This is a theorem, not a dynamical solve, and needs
               NO full SU(3) sigma-model.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  spectrum_cache_L12:
    path: "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
    sha256: "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
  dirac_spectrum_module:
    path: "computations/_shared/dirac_spectrum.py"
    sha256: "<computed-at-runtime>"

# ---- Conditional blocks ----
fb_pair:
  forward: "the broken-charge algebra (U(1)_7 broken by BCS, B6 PROVEN; the su(2)+u(1) Jensen stabilizer + C^2 coset, session-73a); z=2 (DYNAMICAL-EXPONENT-63); the Kosmann connection K_a (anti-Hermitian, W5); S82-W0-A-BRANCH-COUNT INFO value=6"
  backward: "R-2 (the branch count parked at dim(V)=6 with the 7-count deferred to the non-existent full SU(3) sigma-model); C-2 (which modes survive vs thermalize — Type-A vs Type-B have different finite-T fate); the GGE pair-production count -> A_s (the Type-A acoustic branches feed the 59.8-pair count)"
dual_prior:
  track_A: "0.5 — Reading_A (count = 6, theorem-confirmed): n_NG = (dim G - dim H) - (1/2)rank(rho) = 6 with a definite Type-A/Type-B split; the S82 INFO=6 is upgraded from INFO to a THEOREM via WM counting, WITHOUT the sigma-model. The 7th branch does NOT exist (the naive coset dimension over-counted by the Type-B pairing)."
  track_B: "0.5 — Reading_B (count = 7, or count = 6-but-different-mechanism): the WM theorem yields n_NG = 7 (the framework's principal-mode picture undercounted), OR yields 6 by a DIFFERENT (dim G - dim H, rank(rho)) decomposition than the naive '3 amplitude + 3 phase' reading — in which case the Type-A/Type-B classification reorganizes which branches feed the GGE pair count and A_s."
  discriminator: "n_NG = 6 with the (dim G - dim H, rank(rho)) decomposition matching the 3-amplitude+3-phase reading -> 0.9 to Track A (S82 INFO upgraded to theorem); n_NG = 7 -> 0.9 to Track B (the 7th branch is real, settled by rank(rho)); n_NG = 6 but a different decomposition -> the count is 6 but the Type-A/Type-B reorganization is the new structural content (a refinement, not a 6-vs-7 flip)."

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "print_verdict_payload"
  data:
    path: "computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.npz"
    artifact_kind: "data"
    optional: false
  plot:
    path: "computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.png"
    artifact_kind: "plot"
    optional: false
  verdict_line:
    path: "computations/investigation-8/inv8_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^INV8-W3-5-WATANABE-MURAYAMA-BRANCH-COUNT:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/investigation/investigation-8/investigation-8-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-5. INV8-W3-5"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

PASS_meaning: >
  The branch count is settled as a THEOREM: n_NG = (dim G - dim H) - (1/2)rank(rho) evaluated exactly
  from the Kosmann broken-charge algebra, consistent with z=2 (rank(rho) >= 2), with the 6-vs-7 question
  resolved to a definite integer AND the Type-A/Type-B classification stated. Solution-space: R-2 closes —
  the parked branch count is settled without the deferred full SU(3) sigma-model, via a representation-
  theoretic identity. The Type-A (acoustic) count is pinned, which feeds the GGE pair-production -> A_s;
  the Type-B modes are identified, which bears on the C-2 thermalization-vs-survival split. NOTE: any
  permanent §VII / canonical registration of the settled count is session-track promotion at /rclab-investigate
  close, NOT an investigation edit.
FAIL_meaning: >
  The Watanabe-Murayama formula CANNOT be cleanly applied: either the broken charges Q_a do not close into
  a well-defined finite algebra under the Kosmann commutators (the rho_ab matrix is ill-defined or
  L_max-unstable), or the ground-state expectation <[Q_a,Q_b]> is not computable from the available spectral
  data without the sigma-model after all. Solution-space: the 6-vs-7 count remains parked; the WM route does
  NOT settle it without the deferred machinery, contrary to the survey's R-2 claim — the deferral was
  justified.
INFO_meaning: >
  rho_ab and n_NG are computed but the result is decomposition-sensitive: the count is a definite integer
  but which (dim G - dim H, rank(rho)) decomposition is the physical one depends on a choice (e.g. whether
  U(1)_7 is counted among the broken generators, or whether the C^2 coset phases pair with the amplitude
  modes). The gate reports the count under each admissible decomposition; the 6-vs-7 is settled MODULO the
  decomposition choice, which is the residual structural question.

effort:
  files_created:
    - "computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.py"
    - "computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.npz"
    - "computations/investigation-8/inv8_w3_watanabe_murayama_branch_count.png"
  estimated_time: "1 day"

substrate_framing: |
  PHONONIC. The phonon branches ARE the Goldstone modes of the substrate's spontaneously-broken
  symmetry at the fold — the acoustic and amplitude excitations of the reorganized D_K spectral
  structure when the BCS condensate breaks U(1)_7 (Cooper pairs carry K_7 charge +/-1/2). They are
  NOT modes propagating IN a medium; they ARE the medium's own low-energy degrees of freedom. The
  Watanabe-Murayama counting is the exact statement of how many such modes there are when Lorentz
  invariance is absent (z != 1) — which is precisely the substrate's situation (z=2 for the principal
  B-sector mode). The broken charges Q_a ARE the Kosmann-connection generators K_a (the natural
  anti-Hermitian connection on the spinor bundle, which also provides the BCS interaction). The
  Watanabe-Murayama matrix rho_ab = -i<[Q_a,Q_b]> is a substrate-IS object: the ground-state
  expectation of the commutators of the substrate's own broken charges. The direction of explanation:
  D_K / Kosmann broken-charge algebra at the fold -> the antisymmetric rho_ab and its rank -> the
  Goldstone count n_NG = (dim G - dim H) - (1/2)rank(rho) and the Type-A/Type-B classification -> the
  number of acoustic branches (which feed the GGE pair-production -> A_s) and the soft Type-B modes
  (which bear on the thermalization split). z=2 is the smoking gun: it FORCES Type-B, hence rank(rho)>=2,
  hence a count below the naive coset dimension — settling 6-vs-7 as a theorem, not a dynamical solve.
```

**Cross-references (MANDATORY)**:
- **INV8-W3-5 (Watanabe-Murayama branch count) ↔ S82-W0-A-BRANCH-COUNT (INFO value=6)** — this gate seeks to upgrade the S82 INFO to a THEOREM via the ρ_ab rank, settling whether the count is genuinely 6 or 7 WITHOUT the deferred full SU(3) sigma-model. The S82 INFO is the prior the gate tests, NOT a duplicate.
- **INV8-W3-5 ↔ C-2 (which modes survive vs thermalize)** — the Type-A/Type-B classification this gate produces bears directly on the C-2 vocabulary hazard (the Leggett channel in the integrable/bounded-Krylov sector vs the bulk GGE in the chaotic/linear-Krylov sector, my survey B-6). Cross-reference for context.
- **Surveyed-but-not-elevated B-6 (SYK/Krylov integrability split)** is adjacent context: the Type-A/Type-B split connects to the integrable-vs-chaotic mode classification (B-6); cross-ref in the INV8-W4-1 context (per the seed), and noted here for the C-2 link.

---

## Wave 3 → (close synthesis) Decision Point

Wave 3's five gates feed the `/rclab-investigate --investigation 8` close synthesis (NOT a plan-time gate), per the seed's spine:

- **INV8-W3-2 (quantum-metric → H(τ))** converges with **INV8-W2-1 (Jacobson → CC magnitude)** — the TWO constructive attacks on the dimensionful-scale knot (the investigation's spine). The close synthesis asks: do both routes land on the same dimensionful scale (one fixing the Hubble backbone function, the other the CC magnitude)? Convergence would close G-1 + G-2 (the a(t)/CC magnitude knot) from two independent substrate-IS computations. This is `/rclab-investigate` work, NOT a plan-time gate (you cannot adjudicate readings whose values do not yet exist).
- **INV8-W3-1 (Kibble-Zurek walls)** competes with **INV8-W2-4 (running-vacuum RG)** — the TWO candidate mechanisms for the w_a/BBN tension (C-1 + C-4). The close synthesis asks: which mechanism (frozen Z_3 walls w=−2/3, or running-vacuum c₁H²) better fits the DESI w_a and the BBN ΔN_eff ledger? If INV8-W3-1 PASSes (walls form), the frozen-modulus w_a=0 lock is re-scoped; if it FAILs, the running-vacuum is the surviving candidate.
- **INV8-W3-3 (CDT comparison)** and **INV8-W3-4 (Higgs near-criticality)** and **INV8-W3-5 (branch count)** are each self-contained structural results feeding their respective survey refinements (R-1, A-3/B-5, R-2). Any that PASS as permanent structural content (the maximally-NON-ideal flat-band characterization from W3-2; the branch-count theorem from W3-5; the d_s/CDT measurement from W3-3) are **promoted into a session** at close — lifted as a carry-forward into a session-mode `/rclab-plan` plan and re-computed under a `session-{N}` gate, NOT held in the investigation track (the track-local boundary, `gate-verdicts.md §"Investigation-Track Canonical Path"`).
- **Routed OUT (session-track, NOT a gate here)**: HY5 — the Strutinsky = O'Neill A-tensor = spectral-action saddle-point cross-pillar identity §VII registration (my survey R-4) — is session-track promotion at `/rclab-investigate --investigation 8` close, NOT an investigation gate.

## Wave 3 Machinery-Enumeration Pin

Aggregate of all five COMPUTE gate `machinery_pin_map` entries (what `_yaml_gate_validator.py` reads). All five gates are COMPUTE-class; each pins N_eval, L_max, scan_range, step_size, tolerance, scheme, convention, random_seed, GPU_path. Conditional pins declared where they apply:

- **INV8-W3-1**: scheme=FW, convention=KZ-mean-field-BCS-z2-nu-half, GPU=cpu-cap-OMP8, deterministic. No regulator_pin (no Seeley-DeWitt a_n). publication_precision N/A (no downstream-cited value beyond the wall-density direction).
- **INV8-W3-2**: scheme=FW, convention=Peotta-Torma-D-geom-substrate-IS-OP-PROJ, GPU=torch.linalg (block-diagonal D_K), deterministic, publication_precision=6. No regulator_pin (quantum-metric integral, not a Seeley-DeWitt a_n citation). CLASS=FULL (no SCHEMATIC helper — the quantum metric is computed from the real D_K eigenvectors, not a schematic regulator module).
- **INV8-W3-3**: scheme=zeta, convention=NORMAL-STATE-Delta0-heat-trace-energy-axis-gamma_E + diffusion-window-K2-specialization, GPU=torch.linalg (GT-builder per-block diagonalization) + numpy (heat-trace sum), deterministic, **regulator_pin=a_n^{ζ}** (the heat-trace small-σ Seeley-DeWitt expansion; a_0^{ζ} sets d_s(σ→0)=8), publication_precision=4. L_max_plan=16 / L_max_operational declared per the Casimir-bound feasibility pre-check. **Multiplicative-normalization-cancellation pre-flight MANDATORY** (math-scripts.md §K=3): Sage `sage_simplify` factorization check at plan-freeze CONFIRMS P(σ) is additive-in-new-sectors, NOT a w(L_max)·g(σ) product ⇒ d_s is a genuine L_max-dependent observable, the PASS targets L_max-stability (not an asymptote-only test).
- **INV8-W3-4**: scheme=MS, convention=MSbar-1loop-SM-plus-KK-threshold + substrate-boundary-λ(m_H), GPU=cpu-cap-OMP8 (scalar RG ODE), deterministic, publication_precision=4. No regulator_pin in the Seeley-DeWitt sense (the RG β-function is the SM MSbar scheme; if the substrate β touches a₄ via the KK-threshold spectral-action vertex, tag a_4^{ζ} — declared CONDITIONAL, to be confirmed at the producing-script dry-run).
- **INV8-W3-5**: scheme=FW, convention=Watanabe-Murayama-rho-ab-Kosmann-broken-charge + Type-A-Type-B-classification, GPU=numpy.linalg/Sage (small antisymmetric ρ_ab), deterministic, publication_precision=exact (integers). No regulator_pin. theorem-form gate: PRDR (2)(3)(4) set N/A-with-reason (representation-theoretic identity, not a numerical threshold); the real criterion is in operator + the verdict rubric.

## Wave 3 Input-SHA Ledger

Every input file the five COMPUTE gates consume, with expected SHA-256 (static files precomputed at plan-freeze; dynamic marked `<computed-at-runtime>`):

| Input file | Consumed by | SHA-256 |
|:-----------|:------------|:--------|
| `computations/_shared/canonical_constants.py` | W3-1, W3-2, W3-3, W3-4, W3-5 | `<computed-at-runtime>` (dynamic — edited frequently) |
| `computations/session-84/s84_spectrum_cache_L12_tau019.npz` | W3-2, W3-3, W3-4, W3-5 | `9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9` (on-disk-verified at plan-freeze) |
| `computations/session-104/s104_branch_iv_phase1_builder.py` (GT-builder) | W3-3 | `<computed-at-runtime>` |
| `computations/session-104/s104_sym_p_chain_cache_L1314.npz` (Sym^p chain, Sym^13/14 unlock) | W3-3 | `<computed-at-runtime>` |
| `computations/_shared/dirac_spectrum.py` (irrep construction module) | W3-2, W3-3, W3-5 | `<computed-at-runtime>` |

**Methodological cross-check anchors (cited, NOT loaded as canonical value sources — per `substrate-first-canonical-sourcing.md §(i)`)**: del Campo-Zurek IJMPA 29 1430018 (2014) [W3-1 KZ scaling]; Roy PRB 90 165139 (2014) + Ledwith-Tarnopolsky-Khalaf-Vishwanath PRR 2 023237 (2020) [W3-2 ideal-band trace condition]; Degrassi et al. JHEP 08 (2012) 098 + Buttazzo et al. JHEP 12 (2013) 089 [W3-4 SM near-criticality λ→0 at ~10^10-10^11 GeV]; Watanabe-Murayama PRL 108 251602 (2012) + Hidaka PRL 110 091601 (2013) [W3-5 Goldstone counting]. These provide conceptual framing / cross-check anchors; every NUMERICAL pin sources from substrate-first computation or a canonical constant.
