# Session 100a — Carry-Forward Context (mechanical gather, `/rclab-plan` Phase 1b + 1c-REGISTERS.CONSUME)

**Generated**: 2026-06-03 | **Prior session**: 99 | **Mode**: fanout

## Source manifest

| Source | Type | CF section | Items contributed |
|:-------|:-----|:-----------|:------------------|
| `sessions/archive/session-99/session-99-w1-workingpaper.md` | per-wave WP | `## Carry-Forward Computations` (L87–98) | CF-S100-W1-SF54-MAPPING |
| `sessions/archive/session-99/session-99-w2-workingpaper.md` | per-wave WP | `## Carry-Forward Computations` (L166–177) | CF-S100-W2-1-QEQ-DRIVE |
| `sessions/archive/session-99/session-99-w3-workingpaper.md` | per-wave WP | `## Carry-Forward Computations` (L180–193) | CF-S100-MD-NORMALIZATION |
| `sessions/archive/session-99/session-99-w4-workingpaper.md` | per-wave WP | `## Carry-Forward Computations` (L153–155) | NONE (explicit: both W4 FAILs map corridors) |
| `session-99-lizzi-synthesis.md` | review synthesis | `## V. Carry-Forward Computations` (V.1–V.6) | 5 panel mirrors + 1 lizzi-specific (V.5) |
| `session-99-mack-synthesis.md` | review synthesis | `## V.` (V.1–V.5) | 4 panel mirrors + 1 mack-specific (V.5) |
| `session-99-phonon-first-synthesis.md` | review synthesis | `## V.` (V.1–V.7) | 5 panel mirrors + 1 pf-specific (V.6) |
| `session-99-quantum-foam-synthesis.md` | review synthesis | `## V.` (V.1–V.5) | 4 panel mirrors + 1 foam-specific (V.5) |
| `session-99-volovik-synthesis.md` | review synthesis | `## V.` (V.1–V.6) | 5 panel mirrors (V.3 widening standalone) |
| `session-99-housekeeping.md` | Q2 ledger | §A/§B–§E + consumption pointers | 0 CF items (§B/§C/§D all empty); 2 plan-freeze process obligations (below) |
| `session-99-fermion-mass-{panel,baptista,hawking,connes,transit}.md` | panel files | **NO formal CF section** (skip per skill error-handling; content fully mirrored by the 5 syntheses' §V) | — |
| Forward registers (1c-REGISTERS.CONSUME) | EVOI §6 / atlas-08 / open-channel-ledger / capstone §7.3 | — | 6 register-sourced items (#3, #4, #15, #17, #18, #19) |

**Dropped as stale (register-state wins):** the E1 Stage-2 verify (lizzi V.6 / phonon-first V.7 / volovik V.6) — EXECUTED S99 W3-1, PASS, §VII.BL E1 now STAGE-3-PERMANENT (audit `0f0c4f65…`, supersedes `13998949…`). The §VII.AH Stage-2 (atlas-08 Q26) — ALREADY STAGE-3-PERMANENT since S90 W2 CF-20 (backfill corrected this pass; see `registry/atlas-08-freshness-S99.md`).

**Workshop-class items NOT here** (route via `/rclab-investigate`, not this plan): W1-1 acoustic-frame deceleration covariance Q1 seed (housekeeping §A); Q44 Sagan re-anchoring; CF21 TD/LI H̃-divergence adjudication.

---

## Deduplicated carry-forward table (19 items)

### Item 1 — S100a-SF54-MAPPING (= CF-S100-W1-SF54-MAPPING) [Wave 1]
**Sources**: W1 WP (convergence 1). **Reviewer origin**: transit-dynamics-theorist (W1-1 executor).
| Field | Spec (verbatim-derived, W1 WP L93–98) |
|:--|:--|
| What | Re-derive the a_eff(a₂-channel) → SF54 deceleration-band map: is SF54 [−0.97, +0.81] the correct comparison object for the bare-frame q_bare history, or does the Connes-distance proxy require a frame/normalization correction? Test band-membership under the corrected map. Resolves whether the SF54 miss is a genuine substrate prediction (post-fold mostly-accelerating, SF54 wrong band) or an a_eff→SF54 mapping defect. |
| Inputs | `s99_w1_q_nonratio_observable.npz` (arr_q_bare_t, arr_H_bare_t, arr_tau, band_frac_primary/qbare); `little-red-dots-synthesis.md` (SF54 derivation / Connes-distance proxy); `canonical_constants.py` (Omega_BA_fold, a_2_FW_zeta). |
| Gate | `[SIGN]`: PASS iff corrected-map in-band fraction ≥ 0.90; INFO iff substrate is structurally mostly-accelerating post-fold and SF54 is the wrong band (informative re-scope); FAIL iff the mapping is ill-defined. |
| Effort | ~1 wave (1D post-processing + SF54-map re-derivation; no diagonalization). |

### Item 2 — S100a-QEQ-DRIVE (= CF-S100-W2-1-QEQ-DRIVE) [Wave 1]
**Sources**: W2 WP (convergence 1). **Reviewer origin**: transit (executor); content = Volovik q-theory.
| Field | Spec (verbatim-derived, W2 WP L172–177) |
|:--|:--|
| What | Derive a substrate-internal `q_eq(H)` drive (an H-dependent equilibrium/source from the substrate's own back-reaction — e.g. back-reaction closure `H² = f(ρ_relic, S_SA)` per capstone §6.3, or a Hubble-sourced chemical-potential shift in the Volovik Gibbs-Duhem relation — NOT an imposed CPL fluid law) and re-integrate the friction-ODE WITHOUT the imposed linear closure; test whether `d ln q/d ln H = 1` (n=2) emerges unforced. |
| Inputs | `s99_w2_relaxation_closure.npz` (bare-ODE oscillator, k_curv=+3586.5, q_boundary); `s99_w1_q_nonratio_observable.npz` (`arr_H_bare_t`); Volovik Gibbs-Duhem ρ_vac(eq)=0 (S95); S62 #19 (q=0 interior equilibrium); `canonical_constants.py` (a_0_FW_zeta). |
| Gate | `[SIGN]`: PASS iff substrate-derived q_eq(H) yields \|slope − 1\| ≤ 0.05 UNFORCED (C10 Object-C → substrate-forced, §8.5 OPEN→CLOSED); INFO iff slope narrows toward 1 with a residual closure parameter; FAIL iff no substrate q_eq(H) drive exists (n=2 structurally a fluid-closure input — Object-C closes STRUCTURALLY-CONDITIONAL, §8.5 stays OPEN by design). |
| Effort | ~1–2 waves (the q_eq(H) derivation is the hard part; ODE re-run + regression cheap). |

### Item 3 — S100a-NS-NLO [Wave 1] — REGISTER-SOURCED (EVOI Tier-2 rank 6; no WP CF existed)
| Field | Spec (EVOI §2 row 6) |
|:--|:--|
| What | Compute n_s second-order slow-variation correction (NLO beyond the PROVEN leading-order n_s = 0.9561), testing precision-stability of the headline tilt. |
| Inputs | B1 trajectory; a_2/a_4 spectral moments (`a_2_FW_zeta`, `a_4` per regulator-pin discipline); `canonical_constants.py` n_s pins. |
| Gate | PASS iff \|Δn_s(NLO)\| < 0.003 vs the Planck-band leading-order anchor; INFO band and FAIL per planner pre-registration. |
| Effort | ~1–2 waves per EVOI; plan as 1 gate. |

### Item 4 — S100a-SIGMA-DM-NUCLEON [Wave 1] — REGISTER-SOURCED (EVOI Tier-2 rank 7 / atlas #10)
| Field | Spec (EVOI §2 row 7) |
|:--|:--|
| What | Compute σ_DM-nucleon from the substrate coupling of the Leggett-channel GGE quasiparticle (CPT-neutral, non-annihilating inter-band coherence mode) — turning the DM identity into a direct-detection prediction. |
| Inputs | Leggett-channel machinery (LEGGETT-MOMENT-70, Mass_LeggettDM/Δ_BCS = 11.97); S42/S44 σ/m = 5.7e-51 cm²/g collisionless anchor; `canonical_constants.py` (M_KK, Δ_BCS). |
| Gate | Pre-register vs current direct-detection exclusion curves (LZ/XENONnT band at the predicted mass); PASS/INFO/FAIL bands set by planner from the substrate-predicted cross-section's position vs the neutrino fog. On any landing, the observational row routes to mack (sole writer). |
| Effort | ~1 wave. |

### Item 5 — S100a-DUAL-Z3-PHI-POINTS [Wave 2 — RUN FIRST]
**Sources**: phonon-first V.2 + volovik V.2 (standalone) + lizzi/mack/quantum-foam V.1 (folded sub-test). Convergence 5.
| Field | Spec (PF V.2 / VV V.2) |
|:--|:--|
| What | Diagonalize the closed-form 3×3 lepton matrix `Ω^b_g` at the three Z₃ φ-points {0, 2π/3, 4π/3}; verify `c(φ) = 1/(1+8cos²φ)` gives {1/9, 1/3, 1/3} (2-fold collapse) — tests whether the s_φ-phase is genuinely the second Z₃ of the dual-Z₃ generation structure; check quark matrices Ω^D, Ω^c show NO φ-dependence (lepton-only lever). |
| Inputs | baptista's closed-form 3×3 `Ω^b_g(φ)` (in hand, Baptista Paper 14 §3 lineage); `c(φ)` factor. |
| Gate | PASS iff {1/9, 1/3, 1/3} collapse confirmed at the Z₃ points AND quark matrices φ-independent; FAIL otherwise. |
| Effort | 1–2 h, closed-form, no eigensolve. **Precondition feed to Item 6.** |

### Item 6 — S100a-YUKAWA-OVERLAP-OFFDIAG [Wave 2 — PANEL CONSENSUS LEAD]
**Sources**: lizzi V.1, mack V.1, phonon-first V.1, quantum-foam V.1, volovik V.1. Convergence 5.
| Field | Spec (merged; mack V.1 fullest) |
|:--|:--|
| What | Compute `O_g = ∫_K Tr[ψ_g† |s(h)|² ψ_g] vol_{g_τ}` at L_max=12, τ_fold, PLUS the inter-sector t1↔t2 matrix element — yielding the diagonal envelope {d_i} AND the off-diagonal `w = |w|·e^{i·arg(w)}` in one object (the literal missing calc from Baptista Paper 14 §3). |
| Inputs | `s84_spectrum_cache_L12_tau019.npz`; Jensen fiber `|s(h)|²` Higgs-mode overlap kernel; `canonical_constants.py`: tau_fold, Vol_SU3_Haar=1349.74, M_KK; PDG anchors m_e/m_mu/m_tau; triality-distinct tower assignment (1,0)/(1,1)/(3,0), C₂=(4/3,3,6). |
| Gate | PASS iff |s|²-weighted diagonal reproduces the e-vs-heavy envelope sign + OOM + gap-asymmetry direction AND widening lands in the [1.800 (Casimir), 1.8894 (PDG)] band; INFO if envelope direction right but widening needs the Jensen tilt / sector-assignment closure; FAIL if diagonal is generation-blind (1:1:1 recurs — would contradict the ε_LX-on-multiplicity reframe). |
| Effort | 4–6 h, 1 agent session (needed (p,q) sectors are low, p+q ≤ 4). |
| Note | lizzi functional-sensitivity pin: extracted RATIOS are FUNCTIONAL-INDEPENDENT — one scheme suffices; only an a₄-pulled |s(h)|² scale would be functional-dependent (tag scheme if so). |

### Item 7 — S100a-CASIMIR-WIDENING [Wave 2 — after Item 6 machinery]
**Sources**: volovik V.3 (standalone); folded into V.1 PASS criteria by lizzi/mack/phonon-first/quantum-foam. Convergence 5.
| Field | Spec (VV V.3) |
|:--|:--|
| What | Confirm or refute the 9/5 = 1.800 widening from the ACTUAL |s(h)|²-weighted overlap integral on the triality-distinct tower (1,0)/(1,1)/(3,0), vs the generic-overlap 3.0 discriminator. Resolves the panel's layer-2 OPEN item (the 1.889 shape). |
| Inputs | C₂ = (4/3, 3, 6) Sage-exact; L_max=12 spectrum cache; sector-assignment hypothesis; Item-6 overlap machinery. |
| Gate | PASS iff integral-derived widening ∈ [1.80, 1.89]; INFO iff 1.333 (fundamental (k,0) tower selected — sector-assignment wrong); FAIL iff ≈ 3.0 (generic overlap, Casimir ladder refuted). |
| Effort | 3–4 h (depends on Item 6 overlap machinery). |

### Item 8 — S100a-CONNES-DISTANCE-LADDER [Wave 2]
**Sources**: lizzi V.2, mack V.2, phonon-first V.3, quantum-foam V.2. Convergence 4.
| Field | Spec (merged) |
|:--|:--|
| What | Compute Connes geodesic distances d_i between generation-states on the multiplicity bundle; test `mass = e^{−d_i/ℓ}` + the widening signature ≈ 1.89. Independent regulator-invariant route to the SAME envelope as Item 6. |
| Inputs | `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY` machinery (exists); finite D_F / multiplicity-bundle metric (greybody-reweighted per quantum-foam V.2); J involution; PDG lepton masses (ℓ calibration). |
| Gate | PASS iff d_i ladder reproduces the ~8-e-fold e-vs-heavy envelope AND widening ∈ [1.80, 1.89]; INFO iff envelope-only; FAIL iff distances generation-degenerate (would re-confirm multiplicity-blindness against the ε_LX premise). |
| Effort | 2–4 h, 1 agent session (machinery exists; new content = multiplicity-bundle metric). |

### Item 9 — S100a-FREEZEIN-OVERCONSTRAINED [Wave 3]
**Sources**: lizzi V.3, mack V.3, phonon-first V.4, quantum-foam V.3, volovik V.4. Convergence 5. Merged IDs: S99-CF-FREEZEIN-BLOCK-OVERDETERMINED / S100a-FREEZE-IN-PREDICT / S100a-FREEZEIN-OVERCONSTRAINED / S100a-FREEZEIN-PREDICT / S100a-FREEZEIN-MASS-MIXING.
| Field | Spec (merged) |
|:--|:--|
| What | Fit {S₀, \|w\|} to the charged-lepton masses and arg(w) to ONE mixing datum, then PREDICT the six quark ratios + CKM angles + J_CP with no further freedom (3 inputs → ~12 predictions; over-constrained by construction). A clean FAIL closes the dynamical-freeze-in corridor; a PASS derives the mass+mixing SHAPE (not scale) from substrate squeezed-vacuum dynamics. |
| Inputs | `[[d,w],[w*,d]]` block; diabatic freeze-in amplitude `exp(−S₀·C₂)` (S₀ ≈ 3.2 seed — a RATIO (ε_LX-split scale)/(horizon κ)); P_exc=1.000, δt/T_L=1.25e-5; Casimir grading C₂(p,q); PDG charged-lepton masses + one CKM anchor; held-out test set = quark masses + CKM angles + J_CP; Item-6 \|w\| as cross-check seed (SOFT dependency — the fit is PDG-self-contained). |
| Gate | PASS iff predicted quark ratios (OOMs correct) + CKM angles (within PDG 1σ) + J_CP within pre-registered bands from {S₀,\|w\|,arg w} alone; FAIL iff over-constraint breaks (closes corridor cleanly); INFO iff mass shape PASS but mixing FAIL (or vice versa). |
| Effort | 3–7 h, 1 agent session. |

### Item 10 — S100a-ENVELOPE-OVERDETERMINE [Wave 3 — after Item 9 S₀]
**Sources**: lizzi V.4, mack V.4, phonon-first V.5, quantum-foam V.4, volovik V.5. Convergence 5.
| Field | Spec (merged; QF V.4 numeric band) |
|:--|:--|
| What | Compute the diagonal exponent TWO ways — greybody filter at the SONIC surface κ_SONIC = 0.7048 M_KK (= 2π·0.112, the v=c_BLV Mach-1 crossing; NOT κ_GH=1.365, NOT a₂/a₄ thermodynamic surfaces) vs transit's S₀ — and test coincidence (envelope derived twice = genuine independent confirmation). |
| Inputs | κ_SONIC = 0.7048 M_KK (volovik cites 2π·0.112 = 0.7037 — planner reconciles the 4th digit vs `T_acoustic = 0.112 M_KK` canonical, S63); ε_LX frequency offsets (Δω ~ 0.9 M_KK one-fiber-gap); S₀ from Item 9; greybody transmission Γ(ω)·e^{−2πω/κ}. |
| Gate | PASS iff \|2πω/κ_SONIC − S₀·C₂\|/(S₀·C₂) < 0.1 across the heavy pair; INFO iff same OOM / O(1)-factor traceable to κ-surface choice; FAIL iff > 1 OOM divergence (breaks the "one operator, several faces" identification on the production/filter axis). |
| Effort | 2–4 h (hawking + transit machinery). |
| Note | lizzi pin: κ_SONIC is FIBER-ACOUSTIC (functional-INDEPENDENT); the panel's exclusion of a_n-gradient κ surfaces is endorsed — an a_n-gradient κ would contaminate a regulator-invariant ratio. |

### Item 11 — S100a-S0-THRESHOLD-JOINT [Wave 3 — after Items 9/10]
**Sources**: phonon-first V.6 (standalone; the joint-closure consequence also flagged in QF V.4). Convergence 2.
| Field | Spec (PF V.6) |
|:--|:--|
| What | Test whether S₀ = (ε_LX-split scale)/(horizon κ) is FIXED by the KK-threshold machinery. If yes, envelope magnitude AND slope close JOINTLY — the single highest-leverage open question the panel flagged. |
| Inputs | KK-THRESHOLD-64 machinery; ε_LX-split scale Δω ~ 0.9 M_KK (post shape-preserving-squaring halving); κ_SONIC; S₀ from Item 9. |
| Gate | PASS iff S₀ derives from threshold quantities with no free normalization; INFO iff threshold-constrained to O(1) with a 1-parameter residual; FAIL iff S₀ independent of the threshold (scale stays an empirical anchor, as in the S99 W3-2 neutrino pattern). |
| Effort | 3–4 h, 1 agent session. |

### Item 12 — S100a-M0-FUNCTIONAL-SENSITIVITY [Wave 4]
**Sources**: lizzi V.5 (lizzi-specific functional-axis gate). Convergence 1.
| Field | Spec (LZ V.5) |
|:--|:--|
| What | Recompute the per-sector overall scale M₀^{sector} (and m_H) the KK threshold sets, under BOTH the cutoff action Tr f(D_K²/Λ²) AND the zeta action S_ζ = ζ_{D_K}(0) = a₄; report the scheme-dependence of the SCALE explicitly, confirming the RATIOS (Items 5–11) are untouched — makes the §IV bosonic/fermionic layer-separation EMPIRICAL rather than asserted. |
| Inputs | KK-THRESHOLD-64 machinery (m_H=131.8 GeV, \|S\|² fiber-embedding mode); a₄ zeta moment; cutoff f₄ moment (f4=6446.63942272 at X_MAX=50, f*-scheme); M_KK=7.4287e16 GeV (canonical). Regulator-pin discipline: every a_n cited as a_n^{ζ} / a_n^{cutoff}. |
| Gate | INFO-by-design (functional-dependence characterization): report Δ(M₀^{sector}) and Δ(m_H) between schemes; PASS-side assertion = fermion mass RATIOS bit-identical across schemes; FAIL = ratios move (falsifies the decoupling claim). |
| Effort | 2–3 h, 1 agent session. |

### Item 13 — S100a-M0-MH-INHERITANCE [Wave 4]
**Sources**: mack V.5 (bridge-role specific). Convergence 1.
| Field | Spec (MK V.5) |
|:--|:--|
| What | Trace whether the per-sector scale M₀^{sector} inherits the framework's m_H residual; quantify how the 5–7% m_H over-prediction (framework 131.8 KK-threshold / 134 tree vs PDG 125.1) propagates into the absolute mass normalization. |
| Inputs | KK-THRESHOLD-64 machinery; `canonical_constants.py` m_H_obs=125.1; framework m_H = 131.8 (KK-threshold) + 134 (tree-level filter-independent, theorem A10). |
| Gate | INFO-class report-only (provenance trace feeding the honest-scope ledger): documents whether M₀ is anchored independently or carries the m_H residual. No PASS/FAIL. |
| Effort | ~2 h, 1 agent session. |

### Item 14 — S100a-EPSLX-FOAM-SURVIVAL [Wave 4 — soft-after Wave 2]
**Sources**: quantum-foam V.5 (foam-domain specific). Convergence 1.
| Field | Spec (QF V.5) |
|:--|:--|
| What | Verify ε_LX — a left-invariance-breaking finite-part deformation resolving the topological generation index — survives the foam-continuum limit: compute `[H_foam, ε_LX]` on the multiplicity bundle + the N-scaling of any residual. Tests whether generation labels are topological (foam-robust, QF-71 δn_foam=0 class) or geometric (foam-dissolving, QF-79 ε_c ~ N^{−0.457} class). |
| Inputs | H_foam model (S43–S44 machinery); ε_LX operator from Items 6/9; multiplicity-bundle occupation operators; QF-71/QF-79 scaling laws. |
| Gate | PASS iff [H_foam, ε_LX] = 0 exact (topological; masses foam-robust); INFO iff residual scales N^{−α}, α>0 (foam-fragile hierarchy); FAIL iff residual O(1) N-independent. |
| Effort | 3–4 h, 1 agent session. |

### Item 15 — S100a-H0-SPINOR-FACTOR [Wave 4] — REGISTER-SOURCED (atlas-08 Q27 decisive; LIVE-PENDING since S58)
| Field | Spec (atlas-08 Q27 + falsifier-watchlist:160–169) |
|:--|:--|
| What | First-principles KK-derivation of the spinor normalization factor M_Pl,eff/M_Pl,unred = 3.92 ≈ √16 from the substrate's d_spec=8 spectral triple (16-component spinor structure). H₀ = 65.4 km/s/Mpc is CONTINGENT on this factor; promotes to FLAGSHIP on resolution. |
| Inputs | d_spec=8 spectral-triple spinor bundle (Ψ₊ = ℂ^16); Sakharov induced-gravity machinery (S44, C8); `canonical_constants.py` (M_Pl pins, M_KK). |
| Gate | `[SIGN]`/`[VERIFY]`: PASS iff the factor derives structurally as √16 = 4 within a pre-registered tolerance of the empirical 3.92 (≈2%); INFO iff a derivation exists but with a residual scheme parameter; FAIL iff no spinor-normalization derivation reproduces the factor. |
| Effort | ~1 gate; derivation-heavy, compute-light. |

### Item 16 — S100a-MD-NORMALIZATION (= CF-S100-MD-NORMALIZATION) [Wave 5]
**Sources**: W3 WP (convergence 1). **Reviewer origin**: neutrino-detection-specialist (+ connes cross-axis).
| Field | Spec (verbatim-derived, W3 WP L188–193) |
|:--|:--|
| What | Derive the Dirac neutrino Yukawa couplings Y_i (i=2,3) directly from the substrate D_K bottom light-triple eigenvalue structure (the ~0.82–0.87 M_KK E1/E2/E3 set that S96-MATTER-R-HIERARCHY read as R_direct=9.86), uniquely pinning the bottom-triple → Y_i map; RE-COMPUTE Σm_ν as a genuine zero-free-parameter substrate prediction and re-gate vs DESI. Tests whether the substrate predicts Σm_ν independent of oscillation input, or whether a 1-parameter Dirac-scale normalization is structurally irreducible. |
| Inputs | `s84_spectrum_cache_L12_tau019.npz` (bottom light-triple); `s55_bogoliubov_992.npz` (alternate triple); `s99_w3_seesaw_summnu.npz` (M_R, oscillation-anchored Y_i baseline, Σm_ν=0.058205 reference); `canonical_constants.py` (M_KK, v_ew, Sigma_mnu_FW, Sigma_mnu_bound_DESI_2024). Cross-axis: connes-ncg-theorist for the Dirac-side D_F texture. |
| Gate | `[SIGN]`/`[VERIFY]`: PASS iff substrate-pinned-Y_i Σm_ν is (a) < DESI bound AND (b) within pre-registered tol of 0.058205 eV (zero-free-parameter reproduction); INFO iff the substrate Y_i map is non-unique (residual Dirac-scale normalization — confirms track_B); FAIL iff substrate-pinned Σm_ν > 0.12 eV. |
| Effort | ~1 wave (bottom-triple cached; work = Y_i derivation + 3×3 seesaw re-eval + uniqueness argument). |

### Item 17 — S100a-D5-0NUBB-MAJORANA [Wave 5] — REGISTER-SOURCED (capstone §7.3 item-(4) forward route)
| Field | Spec (capstone §7.3 scorecard item (4) + S96-MATTER-0NUBB INFO machinery) |
|:--|:--|
| What | The compute leg of the unreconciled D5 "no-seesaw" tension (SHARPENED by the S99 W3-2 seesaw PASS that uses a right-handed Majorana M_R): compute the 0νββ effective mass m_ββ = \|Σ U_ei² m_i\| from the substrate KO-dim-6 Pfaffian Majorana texture (M_3(ℂ) summand; delta_CP ∈ {0,π} forced by [J,D_K]=0; normal ordering m₁=0) and place it against current + next-gen 0νββ bounds (KamLAND-Zen, LEGEND-1000) — the laboratory Majorana-vs-Dirac discriminator for whether the substrate's neutrino IS Majorana (seesaw stands, §0 "no-seesaw" framing falls) or Dirac (seesaw route needs reconciliation). |
| Inputs | `s99_w3_seesaw_summnu.npz` (m_ν,i, M_R, ordering); S96-MATTER-0NUBB (`KO-dim-6-Pfaffian-Majorana-on-H_K+` INFO) machinery; PMNS U_ei (PDG); KamLAND-Zen 2024 + LEGEND-1000 forecast bounds; `canonical_constants.py` (Sigma_mnu_FW). |
| Gate | Pre-register m_ββ bands: with m₁=0 NO, m_ββ ∈ [1.5, 4.5] meV expected (substrate-pinned value computed exactly); PASS iff substrate m_ββ is below current bounds AND inside the NO funnel (consistent Majorana, falsifiable at LEGEND); FAIL iff above KamLAND-Zen bound; INFO per planner. The MATH adjudication of D5 (capstone §0 prose vs Majorana M_R) stays a workshop question — this gate supplies its observable leg only; capstone §7.3 STATUS stays unreconciled pending the workshop. Observational row → mack on landing. |
| Effort | ~0.5–1 gate (3×3 PMNS contraction + bound comparison; texture machinery exists). |

### Item 18 — S100a-VIIW3LAB-STAGE2-VERIFY [Wave 6] — REGISTER-SOURCED (open-channel-ledger §C K5 / atlas-08 Q24)
| Field | Spec (registry §VII.W-3.LAB line ~130 + joint-theorem-promotion.md Stage 2) |
|:--|:--|
| What | Stage-2 two-agent parallel cross-axis independent-verify of §VII.W-3.LAB (Cross-Pillar Bridge: Substrate Cocycle-Ratio Preservation Under χ Inheritance Morphism into 3He-B + 3He-A BdG Laboratory Observables; STAGE-1-CANDIDATE since S88 W4a-17; FWD-C3 / cross-pillar-bridge K-counter instance #3). PASS-AND promotes to STAGE-3-PERMANENT with Stage-3-CLASS tag `JOINT-CROSS-AXIS-STAGE-2-PASS-AND`. |
| Inputs | Registered §VII.W-3.LAB entry text ONLY (no workshop transcripts); relevant npz pins per the entry's anchor list; `joint-theorem-promotion.md` Stage-2 protocol + Axis-B Selection Protocol; `inheritance-falsifier-protocol.md` (rank-2 ker(ι_*) 4-gate structure). |
| Gate | `[VERIFY]`: Stage-2 PASS-AND (both reviewers PASS all own-axis clauses AND the JOINT clauses independently; OR is FORBIDDEN); any clause FAIL holds STAGE-1; INFO clause → Stage-2-INFO-deferred. **Reviewer constraint (S99 E1 lesson, MANDATORY at plan-freeze)**: Stage-0 authors per registry line 130 = {volovik-superfluid-universe-theorist PRIMARY, connes-ncg-theorist, mack-cosmic-bridge} — ALL EXCLUDED (+ downstream-inheritance reach test on the substitutes). Eligible: Axis-A spectral/NCG = van-den-dungen-bridge-theorist (or lizzi); Axis-B substrate/BdG-laboratory = landau-condensed-matter-theorist. Substrate-input-orthogonality predicate MUST be satisfied (≥1 npz loaded by exactly one reviewer). |
| Effort | 2–3 h, 2 parallel reviewer dispatches + 1 closeout. |

### Item 19 — S100a-VIIAM-STAGE2-VERIFY [Wave 6] — REGISTER-SOURCED (open-channel-ledger §C K6 / atlas-08 Q25)
| Field | Spec (registry §VII.AM block lines ~16700–16712 + joint-theorem-promotion.md) |
|:--|:--|
| What | Stage-2 THREE-agent parallel cross-axis independent-verify of §VII.AM (Universal Lock Condition: pixelation lock + effacement lock + Page-time lock; STAGE-1-CANDIDATE since S88 W1b2-65; atlas-09 flags it Suspected-but-Not-Yet-Retracted — a clause-level FAIL routes to retraction, making this gate informative in BOTH directions). Per the registry block: spectral-functional-axis reviewer audits clauses (a)+(b)+(c)-JOINT; transit-dynamics-axis reviewer audits (a)+(b)+(c)-JOINT; semiclassical-gravity-axis reviewer audits (a)+(c)-JOINT; joint clauses PASS-AND'd across ALL THREE verdicts. |
| Inputs | Registered §VII.AM entry text ONLY; the 3-instance calibration-corpus anchors named in the entry; `joint-theorem-promotion.md`; atlas-09 §"Suspected-but-Not-Yet-Retracted" routing. |
| Gate | `[VERIFY]`: PASS-AND across all three reviewers → STAGE-3-PERMANENT (+ Stage-3-CLASS tag); any clause FAIL → hold STAGE-1 + atlas-09 retraction-route evaluation. **Reviewer constraint (S99 E1 lesson)**: Stage-0 authors per registry Sponsors = {hawking-theorist PRIMARY, transit-dynamics-theorist, connes-ncg-theorist} — ALL EXCLUDED (+ downstream-inheritance reach). Eligible axis assignments: spectral-functional = lizzi-spectral-functional-theorist; dynamics = volovik-superfluid-universe-theorist (or quantum-acoustics-theorist); semiclassical-gravity = schwarzschild-penrose-geometer. |
| Effort | 3 parallel reviewer dispatches + 1 closeout. |

---

## Plan-freeze process obligations (from S99 housekeeping §A — NOT gates)

1. **Stage-2 reviewer Stage-0-authorship cross-reference** (E1 axis-A lesson): effected ABOVE for Items 18/19 (authorship extracted from registry lines 130 / 16700–16712 and pinned into the gate specs). Any planner adding a Stage-2 gate MUST repeat the check against the registered §VII entry's authorship lines, NOT merely the prior column-computing gates.
2. **`_joint_theorem_independent_verify_audit.py` hardening**: the script currently has NO registered-Stage-0-authorship cross-reference (grep verified 2026-06-03). Orchestrator adds the check during Phase 3 validation (audit-script extension; in-session, not deferred).

## Gate-ID collision space

S99 gate IDs (do not collide): S99-W1-Q-NONRATIO-OBSERVABLE, S99-W2-RELAXATION-CLOSURE, S99-W2-BBN-RELIEF, S99-E1-STAGE2-VERIFY, S99-W3-SEESAW-SUMMNU, S99-W4-A0A2-LMAX13, S99-W4-KAPPA-ALT-OBSERVABLE-SCAN. Verdict file: `computations/session-99/s99_gate_verdicts.txt`. All S100a gate IDs above are new.
