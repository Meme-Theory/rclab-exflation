# S95 Phonon-Exflation-Equation Doc-Incorporation Log

**Date**: 2026-05-29
**Target**: `sessions/framework/phonic-exflation-equation.md` (curated master)
**Scope**: Folded the S95 compute results + Slot-1 review syntheses INTO the master doc in place (incorporation, not addition; no bolted-on "S95 results" section). The 10-domain integration plan (`Collabs/phonic-exflation-equation-integration-plan.md`) was authored BEFORE S95 compute landed; this round folds the COMPUTE RESULTS back in.
**Sole writer this round**: phonon-first-cosmologist (per S95 doc-incorporation dispatch).
**Held**: §6.2 white-hole SYMMETRY (symmetric vs asymmetric) left with an inline `[PENDING S95 W-1 c_s-softening verdict]` marker pending the concurrent W-1 workshop.

Revision types: **SUPERSEDE** (replaces a now-wrong claim), **SHARPEN** (ties an already-correct claim to a theorem / adds derived content), **QUALIFY** (adds a regime / scope / conditionality), **CONFIRM** (records that a claim is now compute-backed, unchanged in substance).

| Doc section | S95 source (gate / synthesis) | Revision type | Provenance audit_sha256 short |
|:--|:--|:--|:--|
| §1.3a (no-well one-loop robust) | W2-3 `S95-W2-3-NO-WELL-ONE-LOOP` PASS (N_interior_sign_changes=0; A10) | SHARPEN (tree-level → one-loop-robust; + GHY boundary-domination reading) | `14dbd362` |
| §1.3a (exhaustion of interactions) | W2-2 `S95-W2-2-EXHAUSTION-FALSIFIER` PASS (HH¹=HH²=0; A9) | SHARPEN ("no third term" → verified algebraic rigidity; matrix-model/IKKT genre) | `2bc553db` |
| §1.3a (τ-flow vs q-flow) | W5-6 `TAU-FLOW-Q-FLOW-REGISTRY-NOTE` (A16); volovik R3 | SHARPEN (distinguish the two monotonicity theorems) | `eb5cc45f` |
| §1.4 (t* stays empirical) | W2-1 `S95-W2-1-T-STAR-ONELOOP-ORIGIN` FAIL R=1.977 (A11) | CONFIRM (corridor "t* is one-loop" CLOSED; ledger {τ,Λ,f₀,f₂,f₄}+t* unchanged) + SHARPEN (principle-theory framing) | `1c9102f3` |
| §5.1 (why r=16ε fails) | transit-collab V.7 | SHARPEN (inline the 3-premises-absent reason) | (review; no gate SHA) |
| §5.2(i) (genesis singularity) | W4-5 `S95-W4-5-SP-12D-SINGULARITY-CENSOR` PASS (A15, SP-V1) | SUPERSEDE ("no t=0 singularity" → censored anisotropic τ→∞ singularity, 12D weak cosmic censorship) | `9ffb4aea` |
| §5.3 (mode equations) | transit-collab V.1 | SHARPEN (print BOTH BdG `u_k` + Mukhanov–Sasaki `v_k`; A_s NOT from BdG) | (review; no gate SHA) |
| §5.3 (Ordered Veil rewrite) | W5 C2 RESOLVED (R_therm=5251.82, S_ent=0; A17) + volovik R1/S-4 | SUPERSEDE (integrability permanence + t_Hubble → diabatic transit-freeze; t_scr/t_transit=814; S39 retraction acknowledged) | `5ad898fa`/`b7d769be` |
| §5.3 (extremal-horizon leg) | sp-collab V.2 (S85 W6-4 κ=0 extremal horizon) | SHARPEN (independent geometric leg: T_H=0 ⇒ never thermalizes) | (review; S85 W6-4) |
| §5.3 (info-paradox resolution) | hawking-collab II.2 | SHARPEN (unitary Bogoliubov + S_ent=0 ⇒ no Page curve) | (review; no gate SHA) |
| §5.3 (N_pair firewall) | transit V.2 + nazarewicz R1 | QUALIFY (`N_Fock=1` vs `⟨Q⟩_GGE=59.8`; BCS-projection caveats S46/S63) | (review; no gate SHA) |
| §6.2 (analog-T ledger) | W4-2 `S95-W4-2-HAWKING-ANALOG-T-LEDGER` PASS (A15) + S-3 synthesis | SHARPEN (3-surface ledger; entry single-valued 72.8; 2.948 is distinct surface, not contradiction) | `e5030430` |
| §6.2 (A_s = produced × greybody) | W4-3 `S95-W4-3-HAWKING-GREYBODY-AS` INFO (A15, HAW-V3) | SHARPEN (model-independent exit greybody Γ(ω); not retracted S73B) | `98cb1ed4` |
| §6.2 (bi-metric, two null cones) | sp-collab V.4 ([T3] Scalar-Tensor Kasparov decoupling, PERMANENT) | SHARPEN (scalar sees white hole; tensor crosses freely; root of r/n_s split) | (review; [T3] PERMANENT) |
| §6.2 (BAO effacement) | W6-2 `CF-S95-BAO-TWO-SPEED-AMPLITUDE-TRANSPORT` INFO (A21) | SHARPEN (effacement SUPPRESSES per-branch; S43 first-sound ring is the live no-ΛCDM channel; INFO-by-unavailability) | `e0ae2393` |
| §6.2 (white-hole SYMMETRY) | W4-1 `S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY` PASS → ASYMMETRIC (A14) | **HELD — PENDING S95 W-1** (inline marker; not finalized) | `5d1ac75a` (held) |
| §6.3 (proxy distinction) | W4-4 `S95-W4-4-SP-CONFORMAL-EMBED` INFO (A15) | SUPERSEDE (conformal factor = Connes-distance proxy, NOT a_eff; a_eff near-flat, q_Ω diverges) | `7b2093b9` |
| §6.3 (back-reaction-closure gap) | transit-collab V.5 | SHARPEN (gap is back-reaction closure `H²=f(ρ_relic,S_SA)`, not kinematics) | (review; no gate SHA) |
| §6.3 (Jacobson EoS) | hawking-collab II.4 | SHARPEN (Friedmann = equation of state; substrate expected NOT to contain it) | (review; no gate SHA) |
| §6.3 (#1 = #8 one gap / EIH lift) | einstein-collab III.2 (A13 mirror) | SHARPEN (generally-covariant emergent g_M action = Friedmann + EP + EIH; reduces frontier dimensionality) | (review; A13) |
| §6.3 (τ derived parameter, not "derived cosmic time") | einstein-collab III.4 | QUALIFY (τ is a derived monotone *parameter*; "is cosmic time" + global rate postulated/C1) | (review; no gate SHA) |
| §7.1 table (DE joint posterior) | W6-3 `DE-JOINT-POSTERIOR-RESOURCE` (A21) + mack §2 | SUPERSEDE (two-compilation anchors → one joint (w₀,wₐ) posterior, Popovic arXiv:2511.07517v3, ρ≈−0.85) | (W6-3 §7.1; A21) |
| §7.1 table (daggers + pivot caption) | mack-collab §5 | QUALIFY (`†` on w₀/wₐ/CC/σ₈ = borrowed FRW H(t), C10; n_s/r/α_s at CMB pivot) | (review; no gate SHA) |
| §7.1 table (f_NL row) | W6-6 `F-NL-ROW` PASS (f_NL=−1.505, 0.47σ; A19) + transit V.3 | SHARPEN (new zero-parameter row, squeezed-vacuum Gaussian by Wick) | `077fde64` |
| §7.1 table (n_s per-value σ) | mack §7.2 | QUALIFY (1.4–2.1σ → 1.29σ/1.40σ/2.10σ per value) | (review; no gate SHA) |
| §7.1 table (σ₈ wording) | mack §3.1 | QUALIFY ("in tension gap" → ~2σ between, not a resolution) | (review; no gate SHA) |
| §7.1 table (m_H ~2% budget) | mack §7.3 | QUALIFY (compare at framework ~2% budget, not PDG 0.17 GeV) | (review; no gate SHA) |
| §7.1 table (N_pair firewall in σ/m row) | transit V.2 | QUALIFY (`N_pair=1` → `N_Fock=1; ⟨Q⟩_GGE=59.8`) | (review; no gate SHA) |
| §7.1 (CC box clause-R4 two-clause split) | W5-3 `EQUILIBRIUM-CC-WARRANT` PASS (A17) + S-4 synthesis + volovik R4 | SHARPEN+QUALIFY (Clause A non-inheritance EXACT; Clause B observed-magnitude re-scoped to C10; thermodynamic not topological) | `397cf449` |
| §7.1 (Leggett DM mechanism) | volovik R5 | SUPERSEDE ("integrability-protected" → superselection + T^{0i}=0; S39 caveat) | (review; no gate SHA) |
| §7.1 (260σ over-closure + σ/m=0) | mack §3.2 | SHARPEN (promote from parenthetical: geometry can't tune DM abundance) | (review; no gate SHA) |
| §7.1 (de Sitter horizon tracking law) | hawking-collab II.4 | SHARPEN (ρ_vac ∼ M_Pl²H² = dS horizon energy density, H/2π=T_dS) | (review; no gate SHA) |
| §7.1 (α_s status word + frozen-FI pin + derived-not-chosen) | mack §3.3 + kaku R5 + nazarewicz R5 | QUALIFY (RESOLVED → RESOLVED-AS-CHANNEL-ARTIFACT; −0.08587279 frozen FI; deg=+2 derived) | (review; S93 W7-1) |
| §7.1 (α_s glossary) | mack §7.1 | QUALIFY (`α_s` = dn_s/dln k, NOT QCD coupling, NOT n_s²−1) | (review; no gate SHA) |
| §7.1 (α_s Bogoliubov-saturation footnote) | transit V.4 | SHARPEN (primordial α_s=0 from P_exc=1 frozen spectrum) | (review; no gate SHA) |
| §7.1 (n_s BMA band) | nazarewicz R3 | SHARPEN (BMA n_s=0.969±0.022 is the correct UQ object) | (review; no gate SHA) |
| §7.1 (LEGGETT-GRAV-DECAY-67 conditional) | nazarewicz R2 | QUALIFY (Ω_DM h²=0.120 PASS conditional on Γ_grav < H_0) | (review; no gate SHA) |
| §7.2 (Falsifier #2 n_T caveat) | mack §7.4 | QUALIFY (n_T=−r/8 is CMB-transferred S66, not slow-roll) | (review; no gate SHA) |
| §7.3 (joint-probability cross-layer) | mack §6 | SHARPEN (product across a₀×a₂×a₄ by Decoupling Theorem; within-a₂ pair not independent) | (review; no gate SHA) |
| §8.3 (f₂ not a free knob) | mack §7.5 | SHARPEN (f₂≈92 fixed by M_Pl/M_KK once a₂^ζ pinned; no fitting DOF) | (review; no gate SHA) |
| §9 "At τ" face row | volovik R2 (mirror of §5.3) | SUPERSEDE (Ordered Veil → transit-timescale freeze-out; ⟨Q⟩_GGE=59.8) | `5ad898fa` |
| §9 "At time t" face row | W4-1/W4-5 + sp V.4 | QUALIFY (sector-dependent two cones; symmetry under W-1; censored anisotropic τ→∞ singularity) | `5d1ac75a`/`9ffb4aea` |
| §9 "At now" face row | W6-6 f_NL | SHARPEN (add f_NL to the observable list) | `077fde64` |
| §9 frontier #1 (one gap with #8) | einstein III.2 | SHARPEN (a(t) = EP = EIH; closing one closes both) | (review; no gate SHA) |
| §9 frontier #5 (CC two-clause) | S-4 synthesis (mirror) | QUALIFY (non-inheritance exact; observed magnitude C10-conditional) | `397cf449` |
| §9 frontier #6 (location vs magnitude) | einstein II.4 | QUALIFY (CC term located permanently; magnitude open; not "solved the CC problem") | (review; no gate SHA) |
| §9 frontier #8 (EP genericity) | S-2 genericity synthesis (A13; effected in-session at compute) | QUALIFY (structurally-inevitable-on-single-operator, value-generic; NOT substrate-uniquely-predicted) | `1662b455`/`bb8b14e5` |
| Verification ledger (line 506 flag) | W6-4 `W0-MKK-PROVENANCE` PASS (A20) | CONFIRM (M_KK + w0_FW PROVENANCE now present; flag CLOSED) | `8298cea9` |

## Not requiring a master-doc edit (recorded for completeness)

- **§VII.BE reverted to STAGE-1-CANDIDATE** (S-1 synthesis, A24): the master doc does NOT cite §VII.BE / Pati-Salam / FWD-C4 anywhere (verified by grep). The revert is a registry-state correction (`permanent-results-registry.md`), already effected at A24; no master-doc edit needed.
- **PBH Tier-2-DIMENSIONFUL** (W6-1 `CF-S95-N-PBH-MAGNITUDE-RECOMPUTE` INFO): the master doc does NOT cite n_PBH (verified by grep). The Tier-2-DIMENSIONFUL / registry-PASS-INELIGIBLE result is a registry / falsifier-inventory item; no master-doc edit needed.
- **W7 spectral-dimension γ_E / van-Hove noun / LQG Regime-II** (A22/A23): these route to `Classification-of-phonon-exflation.md` and `lqg-narrow-path-bridge-class.md`, NOT the master capstone (the capstone does not carry the van-Hove-noun proven_1086 line or the LQG narrow-path entry). No master-doc edit needed in this round.

## Incorporation summary

- **SUPERSEDE**: 7 (§5.2 singularity, §5.3 Ordered Veil, §6.3 proxy distinction, §7.1 DE joint posterior, §7.1 Leggett mechanism, §9 "At τ" row; counting the §5.3+§9 Ordered Veil pair as the same supersession applied in two places = effectively one structural correction in two locations)
- **SHARPEN**: 19
- **QUALIFY**: 13
- **CONFIRM**: 3
- **HELD (PENDING W-1)**: 1 (§6.2 white-hole symmetry)

§-sections touched: §1.3a, §1.4, §5.1, §5.2, §5.3, §6.2, §6.3, §7.1, §7.2, §7.3, §8.3, §9 (faces table + frontiers #1/#5/#6/#8), verification ledger.

## Coverage-completion pass (collab additive drop-ins, 2026-05-29)

**Sole writer this round**: phonon-first-cosmologist (S95 doc-incorporation COVERAGE dispatch).
**Scope**: the purely-ADDITIVE collab-review STRENGTHEN/OPTIONAL drop-ins with NO S95 gate behind them — the gap left by the prior compute-results-folding pass. Source of truth: the integration plan §C/§D + the cited collab files (verbatim drop-in text adapted to the doc's voice). Each item below was verified ABSENT (or absent-in-substance) from the master doc before incorporation; the change-log rows above were respected (no duplication).
**Held / untouched**: §6.2 white-hole SYMMETRY `[PENDING S95 W-1 c_s-softening verdict]` marker (concurrent workshop owns it; grep-confirmed present and unedited).

| Doc section | Collab source §X | Revision type | Provenance |
|:--|:--|:--|:--|
| §2.1 (G_N τ-flatness) | volovik R6 / II.1 | SHARPEN (1/G = vacuum gradient stiffness / compressibility; TT = pure shear ⇒ G invariant) | (review; no gate SHA) |
| §1.3 (KO-mismatch caveat 4) | kaku II.4 | SHARPEN (KO=6 plays "why D=10" role; mismatch = constructive level-matching analog) | (review; no gate SHA) |
| §2.2 (spectrum / block structure) | nazarewicz R6 | SHARPEN (E6 = SU(3) analog of j-channel decoupling ⇒ §5.3 factorizes mode-by-mode EXACTLY) | (review; no gate SHA) |
| §3.2 (FI/RD partition) | nazarewicz §3 discipline note | SHARPEN (anomaly family excluded STRUCTURALLY/pre-registered, NOT for wrong tilt; over-fitting protection) | (review; no gate SHA) |
| §3.2 (FI/RD partition) | nazarewicz R3 (§3.2 half) | SHARPEN (FI/RD = marginalization over nuisance functional f; BMA reading; cross-ref §7.1 BMA band) | (review; no gate SHA) |
| §3.2 (f* direct-sum) | tesla V.3 | SHARPEN (√x = acoustic linear-in-ω envelope; up-weights B1; Mellin divergence = acoustic signature) | (review; no gate SHA) |
| §3.3 (convergence cone) | quantum-foam II.1 | SHARPEN (finite closed pole ladder, NOT Wheeler-superspace sum; CC freedom = one functional's worth) | (review; no gate SHA) |
| §3.3 (defensive note) | kaku R3 | SHARPEN (S_d τ-independent; no CDT-like UV reduction, d_s∼8 S31Aa; low-d_s = windowed artifact S92; no 12→5.65→4 flow) | (review; no gate SHA) |
| §4.2 (Wronskian) | tesla V.2 | SHARPEN (dispersion-rigidity: W[{1,R_K,R_K²}]∝R_K′³; collapse iff dispersion stops moving; = §2.4 band-lifting at moment level) | (review; no gate SHA) |
| §4.2 (Wronskian) | nazarewicz §4 (optional) | SHARPEN (degree-distinctness = Strutinsky smooth/shell independence S44/S55/S56; concurrence, NOT evidence) | (review; no gate SHA) |
| §9 frontier #6 (SDW convergence) | quantum-foam II.3/V.2 | QUALIFY (SDW is the open gate UNDERNEATH CC closure #5; ratio closed / absolute held = one entangled conditional, not two) | (review; no gate SHA) |
| §9 (organizing spine, pre-frontiers) | quantum-foam V.1/IV.1 | SHARPEN (geometry/topology dichotomy: topological outputs survive T3-S43 continuum dissolution ε_c∼N^−0.457; absolute geometric magnitudes conditional) | (review; no gate SHA) |
| §9 frontier #8 (emergent Lorentz/EP) | quantum-foam II.2 | SHARPEN (LIV/foam-dispersion immunity: internal discreteness + continuous emergent g_M ⇒ α_LIV=0 exactly; Hossenfelder no-go does not bite; open item = higher-order isotropy INFO) | (review; no gate SHA) |

### Coverage-completion: already-present (skipped, recorded for completeness — NOT duplicated)

- **einstein II.1** (§0/§1.4 principle-theory) — already present at §1.4 ("`S[D_K(τ), f, Λ]` is a **principle theory** in Einstein's 1919 sense…").
- **volovik II.4** (§0 N₃=0 ⇒ q-relaxation-not-topological-protection) — already present at §0 as an explicit strength-bearing clause ("Because `N₃ = 0`, the Fermi-point protection … is *absent* — which is precisely why the cosmological-constant layer (§7) is a q-theory relaxation problem, not a topological-protection statement").
- **kaku R1** (§1.1 matrix-model/IKKT genre virtue) — already present at §1.3a ("This is the matrix-model/IKKT genre's virtue … no Hagedorn tower or `10⁵⁰⁰` landscape").
- **kaku R2** (§1.3a landscape contrast) — already present at §1.3a ("a monotone weight `e^{−S(τ)}` has no competing interior minima, so the CC problem is vacuum-*subtraction*+adiabaticity, not vacuum-*selection*").
- **quantum-foam II.4** (§1.3a conformal-factor instability is container artifact) — already present at §1.3a (last sentence: "…conformal-factor instability … is a container artifact, absent here because the deformation is volume-preserving TT, G6").
- **hawking II.1** (§1.3a whose-temperature / inverse-Euclidean-period) — already present at §1.3a ("uses the substrate's *own* inverse-Euclidean-period temperature, not a thermal-bath `T`; there is no Gibbsian `T` until something thermalizes").
- **einstein II.2** (§1.3a tree-level saddle vs one-loop separation) — already present at §1.3a (the W2-3 one-loop-robust row: "ONE-LOOP-ROBUST, not merely tree-level … the loop introduces no interior feature absent at tree level").

### Coverage-completion: routed elsewhere / skipped per dispatch

- **quantum-foam V.3** (α_LIV=0 "NULL-by-construction" row) → `falsifier-master-inventory.md` (mack-cosmic-bridge sole writer), NOT the capstone. Skipped.
- **sp III.C** (a₂-reduced Petrov type) — OPTIONAL/contingent on a causal-structure box that does not exist in the doc; skipped per dispatch (not trivially additive).
- All §E computational carry-forwards — NOT incorporated (next-session gates; route to /rclab-plan).

### Coverage-completion summary

- **Incorporated (newly additive)**: 13 drop-ins across 7 §-sections.
- **Already-present (skipped, no duplication)**: 7.
- **Routed-elsewhere / skipped per dispatch**: 3 (quantum-foam V.3 → inventory; sp III.C optional; §E gates → plan).
- **§-sections touched this pass**: §1.3 (caveat 4), §2.1, §2.2, §3.2, §3.3, §4.2, §9 (frontier #6, frontier #8, + new organizing-spine block before the frontiers list).
- **Held untouched**: §6.2 white-hole SYMMETRY `[PENDING S95 W-1]` marker.

## §6.2 follow-up (W-1 verdict applied, 2026-05-29)

**Sole writer this round**: phonon-first-cosmologist (S95 §6.2 doc-follow-up dispatch).
**Scope**: Resolved the held `[PENDING S95 W-1 c_s-softening verdict]` marker in `phonic-exflation-equation.md §6.2` once the W-1 workshop (`sessions/archive/session-95/workshops/c1-cs-softening-completeness.md`) CONVERGED. Applied the verbatim §6.2 disposition (Effects 1–3) from the workshop's §"Doc-routing (PENDING)" section. The prior rows above (incl. the line-28 `§6.2 (white-hole SYMMETRY) … HELD — PENDING S95 W-1`) are preserved; this subsection records the resolution.

| Doc section | S95 source (gate / synthesis) | Revision type | Provenance audit_sha256 short |
|:--|:--|:--|:--|
| §6.2 (white-hole SYMMETRY) | W-1 workshop `c1-cs-softening-completeness.md` (CONVERGED; C1→ASYMMETRIC STANDS, over-determined at six walls) → Effect 1 | **SUPERSEDE / RESOLVE** (PENDING marker REMOVED → ASYMMETRIC: one entry sonic surface + open supersonic exit, N_zeros=1; dropped V.6 "two distinct horizons" stays dropped — thermodynamic≠sonic conflation; substrate-IS framing: diagram asymmetric *because* the Kibble–Zurek quench is irreversible) | `5d1ac75a` (W4-1 anchor; W-1 workshop verdict basis) |
| §6.2 (analog-T KIND-column) | W-1 workshop → Effect 2 + Effect 3 | **SHARPEN** (analog-T ledger gains a KIND column: `a₂`=THERMODYNAMIC-kinematic T=72.8 / `a₄`=THERMODYNAMIC-spectral T=7.578 OBSERVED relic spectral / S63-BLV=SONIC T=0.112; the two-stage composite-emission narrative — a₂ stage-1 kinematic-carrier × a₄ stage-2 observed-spectral, parent→child from ³He-A #27; a₂-observability HELD pending falsifier F1, COMPOSITE form locked) | `e5030430` (W4-2 ledger anchor; W-1 KIND-column) |

**§9 consistency follow-on** (in-scope; the PENDING resolution propagated): §9 "At time t" face row — the stale `symmetry under W-1 adjudication` clause was updated to `ASYMMETRIC — one entry sonic surface, open supersonic exit, over-determined at six walls, S95 W-1` (QUALIFY → RESOLVE; was QUALIFIED W-1-pending in the line-54 row above).

- **PENDING-marker count**: `1 → 0` (grep-verified before/after on `phonic-exflation-equation.md`).
- **§-sections touched this follow-up**: §6.2 (PENDING blockquote → ASYMMETRIC resolution + KIND-tagged analog-T ledger + two-stage composite-emission narrative), §9 ("At time t" face row consistency).
