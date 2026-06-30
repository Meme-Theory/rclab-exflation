# Session 96 — Wave Partition

Mode: **fanout** (per-wave plan + per-wave WP). 7 waves, ≈46 distinct gates. Owners = reviewer-origin specialists; cross-reviewer waves → `gen-physicist`. Source detail + per-wave §V map: `session-96-context.md`. Dedup basis: `equation-collab/_consolidated-findings.md §II/§III`.

Dispatch the planner swarm at **≤5 concurrent** (this session already tripped a transient server-side rate-limit on an 8-wide launch; hold at 5). Batches: {W1,W2,W3,W4,W5} then {W6,W7}.

---

## Wave 1 — Emergent FRW `a(t)` closure  (cluster C1; FLAGSHIP, multi-session)
**Owner**: `transit-dynamics-theorist`  ·  **Gate prefix**: `S96-W1-` / `S96-AOFT-`

| # | Gate (seed) | Scope (one line) |
|:--|:------------|:-----------------|
| 1 | derived-Friedmann-map | Derive `H²=f(ρ_relic,S_SA)` back-reaction closure from `D_K` (flagship; pre-register first leg only) |
| 2 | oneill-nonflat-additivity | Does `S_SA=a₀−a₂+a₄` survive a non-flat SU(3) bundle (O'Neill A≠0)? (van-den-dungen) |
| 3 | mkk-seconds-normalization | `M_KK⁻¹ → seconds` physical-scale normalization (most tractable sub-piece of the gap) |
| 4 | volovik-twofluid-closure | Volovik two-fluid hydrodynamic back-reaction closure template |
| 5 | gft-friedmann-transfer | LQC/GFT-condensate effective-Friedmann transfer target |
| 6 | tau-dot-sweep-profile | Global `τ̇(τ)` sweep-rate profile (controlling rate; currently known only at the fold) |
| 7 | qflow-2v3-residual | Reconcile q-flow vs τ-flow 2-normalization `{Z_norm,V0}` vs 3-component accounting (kaku) |

**Split candidates (if stall)**: W1a {1,4,5,6 — Friedmann-core} · W1b {2,3,7 — structural prereqs}.

---

## Wave 2 — SDW absolute-convergence & EFT-control  (cluster C2)
**Owner**: `lizzi-spectral-functional-theorist`  ·  **Gate prefix**: `S96-W2-` / `S96-SDW-`

| # | Gate (seed) | Scope |
|:--|:------------|:------|
| 1 | sdw-borel-pade | Borel/Padé resummation of the divergent SDW series toward the zeta value (feynman F-2) |
| 2 | a0-pole-residue-finiteness | Residue-finiteness at the `a₀` pole (quantum-foam V.1) |
| 3 | wronskian-FI-across-schemes | FI-ness of the decoupling Wronskian across regulator schemes (lizzi V.2) |
| 4 | oneloop-saddle-regulator-invariance | One-loop no-interior-saddle regulator-invariance, not zeta-specific (lizzi V.4) |
| 5 | sdw-eft-control-param | SDW-EFT parametric-control parameter / species scale `Λ_sp/M_KK=2.06` (string-theory V.1) |
| 6 | sdw-convergence-cc-gap | SDW convergence under the CC magnitude gap (JACOBSON-NONLOCAL-64; confirmed OPEN/FAIL) |

**Split candidates**: W2a {1,2,6 — resummation} · W2b {3,4,5 — invariance/EFT-control}.

---

## Wave 3 — NNLO Casimir EP discriminator + `Γ_grav/H_0`  (cluster C3 + dissonance D1)
**Owner**: `gen-physicist`  ·  **Gate prefix**: `S96-W3-` / `S96-EP-`, `S96-LEGGETT-`

| # | Gate (seed) | Scope |
|:--|:------------|:------|
| 1 | nnlo-casimir-ep | NNLO Casimir EP discriminator — first value-bearing EP prediction beyond the generic-identity ceiling (κ_EP=1, Noether-½) |
| 2 | leggett-gamma-grav-margin | Explicit `Γ_grav/H_0` margin for LEGGETT-GRAV-DECAY-67 (resolves D1; gate is genuinely uncomputed per knowledge graph; CRITICAL) |
| 3 | oneloop-saddle-full-domain | Full-domain one-loop saddle robustness (hawking V.9 / feynman F-5) |

**Split candidates**: keep whole (focused CRITICAL wave); if stall, W3a {1,3} · W3b {2}.

---

## Wave 4 — `a₄` matter sector + seesaw reconciliation  (cluster C6 + dissonance D5)
**Owner**: `dirac-antimatter-theorist`  ·  **Gate prefix**: `S96-W4-` / `S96-MATTER-`

| # | Gate (seed) | Scope |
|:--|:------------|:------|
| 1 | a4-yukawa-mass-ratio | First fermion-mass ratio extracted from the `a₄` Yukawa block (paasch V.3 — the empty layer) |
| 2 | pmns-3x3-beyond-jensen | Full 3×3 PMNS beyond the Level-5 Jensen wall (neutrino V.7) |
| 3 | 0nubb-majorana-dirac | 0νββ Majorana-vs-Dirac falsifier (KO-dim-6 Pfaffian → Majorana; neutrino V.6) |
| 4 | external-baryogenesis-locate | η_B must be sourced external to `D_K` (too CPT-symmetric internally; dirac) |
| 5 | product-yukawa-chirality | Product-KO ε″ Yukawa-chirality sub-finding (dirac) |
| 6 | mass-hierarchy-R-closure | R=27.2 bare → measured 33.8 mass-hierarchy closure route (neutrino) |
| 7 | seesaw-reconcile-D5 | "No seesaw" (§0) vs S60 seesaw `m_2=0.008678 eV` reconciliation (D5) |

**Split candidates**: W4a {1,5,6 — charged/Yukawa} · W4b {2,3,7 — neutrino} + {4 — baryogenesis}.

---

## Wave 5 — Geometry / causal structure / transition order
**Owner**: `schwarzschild-penrose-geometer`  ·  **Gate prefix**: `S96-W5-` / `S96-GEOM-`

| # | Gate (seed) | Scope |
|:--|:------------|:------|
| 1 | landau-free-energy-order | Landau `F(η;τ)` + E13/E17 transition-order reconciliation (first-order modulus vs continuous pairing) (landau V.1) |
| 2 | asymmetric-penrose-diagram | Asymmetric two-cone Penrose diagram (closes the §6.2 no-diagram gap; cite `Phononic-Penrose-Diagrams.md`) |
| 3 | tau-inf-petrov | τ→∞ Petrov/CMPP classification of the censored Kasner singularity |
| 4 | ccc-weyl-curvature | CCC / Weyl-Curvature-Hypothesis comparison (engages Penrose's own program) |
| 5 | off-jensen-chern | Off-Jensen Berry curvature / Chern number (sole route to nontrivial substrate topology; berry) |
| 6 | gauge-sourcing-reconcile | NCG `SU(A_K)` vs isometry-route gauge-group sourcing (Weinberg theorem; kk V.1) |
| 7 | mkk-bracket-propagation | `M_KK` gravity-vs-Kerner 0.83-decade bracket propagation into absolute `a₀` (kk V.2) |

**Split candidates**: W5a {2,3,4 — causal geometry} · W5b {1,5,6,7 — order/topology/gauge}.

---

## Wave 6 — Observational falsifiers & detector reach + cosmogenesis  (obs cluster + D2, D4)
**Owner**: `mack-cosmic-bridge`  ·  **Gate prefix**: `S96-W6-` / `S96-OBS-`

| # | Gate (seed) | Scope |
|:--|:------------|:------|
| 1 | fsigma8-growth-forecast | `f·σ₈(z)` 4%-suppression forecast — add the missing PROVEN prediction to the §7 scorecard (cosmic-web V.3) |
| 2 | first-sound-ring-fetch | S43 first-sound BAO ring experiment-sensitivity fetch + imprint amplitude (cosmic-web V.1/V.2; tesla V.2) |
| 3 | cgwb-peak-frequency | CGWB peak-frequency derivation — mHz(LISA) vs GHz? [D4; LISA flagship at risk] (little-red-dots V.3) |
| 4 | omega-gw-gge-vs-zn | LISA `Ω_GW` GGE-acoustic vs `Z_N` wall-network discriminator (phonon-first V.7) |
| 5 | lrd-assembly-clock | LRD assembly-clock proxy from SCALE-FACTOR-54 (little-red-dots V.1) |
| 6 | cmb-scenario-reconcile-D2 | GGE-relic-IS-CMB vs hot-big-bang SCENARIO A reconciliation (D2) |
| 7 | obs-anchor-hygiene | σ₈ reconcile (0.811 vs 0.829), DESI-DR3 timeline, `A_s` tension-vs-band (mack CF-1/2/3) |

**Split candidates**: W6a {1,2,5,7 — LSS} · W6b {3,4,6 — GW/CGWB + cosmogenesis}.

---

## Wave 7 — Hygiene / canonical-pins / convention-firewall + joint-evidence + self-inventory  (C4/C5/C8 + D3)
**Owner**: `gen-physicist`  ·  **Gate prefix**: `S96-W7-` / `S96-HYG-`

| # | Gate (seed) | Scope |
|:--|:------------|:------|
| 1 | fnl-bound-vs-point | `f_NL` bound-vs-point fix + provenance (no canonical pin; conflicts S67 1.03 / S84 −0.143 FAIL) |
| 2 | canonical-pin-promotion | Promote cited-but-unpinned: `t*`, `tau_NEC=1.383`, `Mach`, `Z_fold`, `R₁`, `R_therm`, `Mass_LeggettDM` |
| 3 | mellin-poleset-labeling | Pin Mellin pole-set `{0,2,4,6,8}` vs `{0,1,2,3,4}` under `λ⁻²ˢ` (factor-2 downstream risk; lizzi V.1) |
| 4 | rk-normalization-firewall | `R_K` normalization firewall table `{2,4,1.5}` (mirror the §8 `a_n` two-object firewall; baptista V.1) |
| 5 | scorecard-self-inventory | Add omitted PROVEN results to §7/§9: `f·σ₈`, neutrino sector, `c_s²=0`, holonomy `Ω=0` |
| 6 | kind-tag-section53 | KIND-tag pass on §5.3 surface-gravity/temperature ledger (T_H=0 vs T_GH=0.217; 0.112 relabel) |
| 7 | joint-evidence-restrict-D3 | §7.3 joint-evidence restriction to the zero-parameter structural spine (algebraic ≠ statistical independence; D3) |
| 8 | cs2-topological-registry | `c_s²=0` Kasparov-bound topological-prediction registry entry (van-den-dungen V.4) |

**Split candidates**: W7a {2,3,4 — pins/firewall} · W7b {1,5,6,7,8 — f_NL/self-inventory/D3/KIND/registry}.

> Methodology-class items (rule/registry/canonical_constants edits) must satisfy `wave-classification.md` M1–M4 and append to the allowlist at plan-freeze; items that produce a NUMBER are COMPUTE-class with pre-registered thresholds.

---

## Wave 8 — Capstone consolidation & status-synchronization  (external-review driven; RUN-EARLY)
**Owner**: `gen-physicist`  ·  **Gate prefix**: `S96-CONSOL-`  ·  **Driver**: `deep-research-report.md` (external second-opinion) + `_consolidated-findings.md §III` (the panel's D1–D6 dissonances are status-drift instances)

> **Sequencing**: W8-1 (status-sync) and W8-3 (standing hygiene gate) are **Wave-0 class — run BEFORE the ambitious compute waves W1–W7** per the external reviewer's "synchronize before getting more ambitious." The plan-index records the recommended order: W8-1/W8-3 → W1–W7 → remaining W8 publication-discipline gates.

| # | Gate (seed) | Class | Scope |
|:--|:------------|:------|:------|
| 1 | S96-CONSOL-STATUS-SYNC | METHODOLOGY | Reconcile the capstone against the current registry/assumptions/retraction-log: §5.3 GGE permanence (vs T3 BROKEN + retraction-16, thermalization ~6 natural units), §6.2 horizon language (vs retraction-22, no-superflow / amplitude≠phase), §7 status tags, `w_a=0` BROKEN, `w₀` raw-vs-derived inversion. ALSO absorb panel dissonances D1/D2/D5 + f_NL (C4). Emit a status-diff; PASS = every major capstone claim's status tag matches the repo-wide register. |
| 2 | S96-CONSOL-3REGISTER-TABLE | METHODOLOGY | Split §7 "now" table into 3 registers: **robust-structural** / **conditional** / **currently-falsified** rows (per report §"Critique"). No flattening of PROVEN/CONDITIONAL/BROKEN into one rhetorical register. |
| 3 | S96-CONSOL-HYGIENE-GATE | METHODOLOGY | Standing **capstone-hygiene gate** (5-question checklist: does this alter §6.3 a(t)? / a §7 falsifier row? / a PROVEN-CONDITIONAL-BROKEN-INFO status? / a prose claim not just the ledger? / a citation?) as a new methodology rule + audit hook, run every session. (The AI-to-AI recurring-process recommendation.) |
| 4 | S96-CONSOL-DK-DF-EQUIV | COMPUTE/structural | The highest-burden NCG departure: a dedicated `D_K ≅ D_F` equivalence / controlled low-energy recovery theorem (SU(3)-manifold triple vs almost-commutative SM triple). connes-domain. |
| 5 | S96-CONSOL-REPRO-BUNDLE | infra/COMPUTE | Minimal frozen end-to-end reproducer for 5–10 headline numbers (n_s, m_H, w₀, a₄^ζ, …) + locked env manifest. PASS = one-command reproduction from canonical_constants + cache. |
| 6 | S96-CONSOL-CITATION-ANCHOR | METHODOLOGY | Primary-literature citation anchoring per report §"Suggested citations" (CCM 1996/2007, Vassilevich 2003, Jacobson 1995, Volovik 2005/07, Klinkhamer–Volovik q-theory, Planck18 / BICEP-Keck24 / Popovic+25 / DES-Y3) — distinguishing inherited vs novel claims. |
| 7 | S96-CONSOL-MODULARIZE | METHODOLOGY | Declare the 3-stratum layered-program structure explicitly (spectral/algebraic math · substrate transit physics · cosmological phenomenology) — make the existing internal modularity visible in the capstone. |

**Split candidates (if stall)**: W8a {1,2,3 — status-sync + registers + hygiene gate, RUN-EARLY} · W8b {4,5,6,7 — publication-discipline}.

**Per-gate agent_type**: connes-ncg-theorist (#4); mack-cosmic-bridge (#2, falsifier/obs table); gen-physicist (#1,#3,#5,#6,#7).
