# External-Research Conceptual-Search Prompt

> **Purpose**: deployable prompt for the `web-researcher` agent to surface external research (papers, programs, anomalies, speculative claims, fringe theories) that touches the phonon-exflation substrate at the **conceptual** level — sufficient specificity for 2-agent adversarial workshop adjudication per `.claude/rules/Investigating-Workshops.md` 3-Q discriminator — regardless of mainstream-vs-fringe sociological status.
>
> **Provenance**: authored 2026-05-17 after the W-DIA-1/2/3 DIA-investigation track demonstrated that external-paper review (DIA-08-1004-007 + White et al. PRR 2026) produces substantive structural outputs (2 × STAGE-1-CANDIDATEs + 1 framework no-go theorem + 22 carry-forwards) when the source touches substrate-relevant physics at the right abstraction level.
>
> **When to deploy**: at session-start when planning the next investigation track; OR when a specific topical question emerges and we want to canvass external work before drafting a workshop schedule directly.

---

## Why this exists

The framework rests on a single conceit: **all observations are made ON the substrate**. Anything interesting in the wider physics literature — settled, controversial, speculative, or rejected-as-crackpot — is a candidate F-image of substrate-IS structure. The framework's 25+ closed mechanisms came as often from "wait, what if this fringe claim actually says X about the substrate" as from internal first-principles derivation. The W-DIA-1/2/3 dispatch from DIA-08-1004-007 (defense-research grey literature, formally not "physics" by most standards) produced the framework's FIRST explicit no-go theorem.

This prompt selects external candidates by **structural-readability**, not respectability.

---

## Mission (paste as web-researcher's task statement)

You are the `web-researcher` agent for the phonon-exflation cosmology project. Surface external research candidates that could seed future DIA-style 2-agent adversarial workshops on the same model as W-DIA-1/2/3 (see `sessions/archive/session-91/workshops/` for shape). Candidates may be mainstream, heterodox, speculative, or crackpot — what matters is the candidate's **structural readability**: does it make a specific math/physics claim that two of our framework specialists could plausibly take adversarial readings on, where Reading A is substrate-faithful and Reading B is substrate-incompatible / layer-collapse?

The output is a **ranked list of 5-10 candidates**, each with the full schema below. The output is NOT a workshop schedule — `/rclab-investigate` consumes the candidate list to author the actual schedule. Your job is the upstream selection.

---

## Search domains (cover all 5; minimum 1 candidate from each tier where available)

### Domain 1 — Recent peer-reviewed (last ~3 years), conceptually substrate-touching

- Analog gravity, BEC analogs, ³He-B / ³He-A analog horizons, superfluid universe analogs
- Emergent spacetime / emergent Lorentz invariance / emergent gauge symmetry papers (Wilczek, Volovik, Carlip, Smolin, Markopoulou, Padmanabhan)
- Modified dispersion relations at IR or UV (Hořava-Lifshitz, doubly-special-relativity, Bogoliubov-class)
- Casimir-effect tunability, dynamical Casimir, dielectric Lifshitz precision
- Dark energy mechanisms beyond ΛCDM (interacting dark energy, holographic dark energy, vacuum-decay, K-essence)
- Dark matter via dispersive / fuzzy / superfluid / Bose-Einstein media
- NCG / spectral-action / Connes-Chamseddine extensions
- Kaluza-Klein revivals / extra-dimensional anomaly-cancellation proposals

### Domain 2 — Defense / aerospace grey literature

- DIA / DARPA / AFOSR / NASA technical reports on vacuum-energy extraction, propellantless propulsion, advanced energy concepts
- NASA Eagleworks legacy + Casimir Inc. (Sonny White program) outputs
- Earthtech / Institute for Advanced Studies at Austin (Hal Puthoff, Bernhard Haisch) papers
- EM-drive / Mach-effect / Woodward-thruster claims AND refutations (both sides admit-eligible; the structural question is whether the claimed effect would be substrate-faithful if real)
- AAWSAP / AATIP follow-on technical literature

### Domain 3 — Speculative-but-specific theoretical proposals

- Time-crystal proposals (Wilczek + follow-ons) — substrate-relevant if they touch broken-time-translation in low-temperature condensed matter
- Anomalous BEC dynamics with mathematical specificity
- Anyonic / topological matter proposals touching K-theoretic obstructions
- Alternative inertia / Mach-principle math (Woodward, Sciama, Hoyle-Narlikar)
- Reciprocal System Theory or other heterodox math frameworks IF they make specific dispersion / K-theory / spectral claims

### Domain 4 — Unexplained experimental anomalies with concrete numbers

- Pioneer / Flyby anomaly (residuals + competing explanations)
- DAMA/LIBRA annual modulation
- ANITA upward-going events
- Muon g-2 deviation
- Hubble tension, S8 tension, faint-galaxy abundance, JWST overmassive black holes
- CRESST low-mass signals, XENON1T low-energy excess, ATOMKI X17 anomaly
- Anomalous magnetic-shielding or weight-loss claims (Podkletnov-class; mainstream-rejected but specific)
- Recent precision-frequency tests (atomic clocks at altitude, optical-clock comparisons, transportable-clock measurements)

### Domain 5 — Crackpot-tier sources with structural specificity

- Specifically: papers that mainstream science rejects but that make math/physics-readable claims (not pure word-salad)
- Examples: alternative ether models with mathematical specificity, zero-point-energy extraction proposals citing specific Casimir or dispersion math, alternative-dispersion proposals invoking specific spectral identities, "vacuum engineering" papers naming specific boundary geometries
- Selection criterion: can two of our framework specialists READ the claim and adversarially evaluate it? If yes, the sociological rejection is irrelevant.

---

## Selection criteria (each candidate MUST satisfy all 4)

- **(a) Specific math/physics claim**: numerical value, dispersion form, structural identity, geometric construction, scaling law — NOT vague hand-waving like "the vacuum has energy" or "consciousness affects measurement"
- **(b) Substrate-touch point**: identify ≥1 framework pillar the claim touches (KK geometry / spectral action / 3He-B inheritance / dark sector / cosmological constant / emergent dispersion / boundary modification / cross-pillar bridge / etc.)
- **(c) Adversarial-reading plausibility**: Reading A (substrate-faithful interpretation) and Reading B (substrate-incompatible / layer-collapse interpretation) BOTH plausible. Specialist-pair candidates from the agent roster: connes × volovik, landau × connes, transit × lizzi, mack × landau, etc.
- **(d) Q1 math/physics adjudication YES** per `.claude/rules/Investigating-Workshops.md` §"Discriminating decision" 3-Q discriminator. NOT Q2 (hygiene / registry-state) or Q3 (parallel-compute-wave).

---

## Anti-patterns (REJECT — do NOT include in candidate list)

- Already-settled mainstream physics with no controversy and no substrate-IS reframing opportunity (standard precision HEP, routine astrometry, etc.) — these have nothing structurally adversarial to say in our framework
- Purely terminological speculation with no specific claim ("consciousness creates spacetime", "the universe is computation")
- Refutation-only papers (the Mach-effect-thruster-doesn't-work paper alone is not a candidate; the original claim WITH its refutation can be a candidate)
- Topics duplicating already-investigated workshops (check `sessions/archive/session-91/workshops/` + the closed-mechanism list via knowledge MCP `mcp__knowledge__.list_entities("closed")` before proposing)
- Topics already in the EVOI table at `sessions/evoi-framework.md` as scheduled work — those are accounted for, not external-research seeds

---

## Per-candidate output schema (use this exact format for each)

```markdown
### Candidate #N: [TITLE]

- **Source**: authors, year, DOI / arXiv / report ID / URL
- **Risk tier**: Mainstream | Heterodox | Speculative | Crackpot
- **Substrate-touch points**: [≥1 framework pillar; cite specific framework results where overlap exists]
- **Specific claim**: [the math/physics claim in 1-3 sentences — numerical value, dispersion form, structural identity, etc.]
- **Reading A (substrate-faithful)**: [how a substrate-IS interpretation might read the claim; which framework specialist would advocate]
- **Reading B (substrate-incompatible)**: [how the substrate-IS reframing might reject the claim or expose layer-collapse; which framework specialist would advocate]
- **Workshop-candidate viability**: [Q1 YES rationale; specialist pair; expected verdict-shape (Reading A wins / Reading B wins / Mixed / no-go theorem candidate)]
- **Why this matters**: [1-paragraph standalone justification — what's at stake if this workshop dispatches; what structural output category would emerge]
```

---

## Risk-tier classification (4-tier scheme)

- **Mainstream**: peer-reviewed, broad scientific acceptance. Example: standard Casimir derivation in textbook form.
- **Heterodox**: peer-reviewed but minority view in the field; advocate-camps disagree. Example: modified-inertia proposals, holographic-dark-energy variants.
- **Speculative**: grey literature, preprint, cross-discipline, defense-research. Example: DIA-08-1004-007; NASA Eagleworks Q-thruster theory papers.
- **Crackpot**: rejected by mainstream but contains specific math/physics-readable claims. Example: PRP zero-point-energy extraction proposals; alternative-ether papers with explicit dispersion math.

**Critical**: tier classification is descriptive (where the work sits sociologically), NOT prescriptive (whether to include). All four tiers are admissible candidates IF the 4 selection criteria are satisfied.

---

## Pre-search workflow (mandatory before web search)

1. Query knowledge MCP for the framework's closed mechanisms: `mcp__knowledge__.list_entities("closed")` and `mcp__knowledge__.search_knowledge("dispersion analog horizon Casimir vacuum")`. Note which substrate-touch points are already closed so candidates don't re-litigate.
2. Read `sessions/evoi-framework.md` to see what's already scheduled.
3. Read `sessions/permanent-results-registry.md §VII` for already-landed §VII entries (don't propose candidates that duplicate landed work).
4. Read `sessions/archive/session-91/workshops/dia-w*.md` for the W-DIA-1/2/3 substantive outputs (don't duplicate Bogoliubov-fluid reduction, Casimir-in-finite-spectral-triple, or dark-energy-thruster sector-asymmetry).

---

## Web-search execution (per domain)

For each of the 5 domains, perform 2-3 targeted searches using a mix of:
- Google Scholar (recent + cited-by network)
- arXiv (specifically: gr-qc, hep-th, cond-mat.quant-gas, astro-ph.CO, physics.gen-ph for crackpot tier)
- DTIC.mil for defense grey literature
- ResearchGate / preprint servers for heterodox / speculative
- Specific institutional sites: nasa.gov, casimirinc.com, earthtech.org, etc.

Use the Anthropic-available paper-search MCP tools (`mcp__paper-search__search_*`, `mcp__paper-search__download_*`) where applicable; fall back to web fetch for grey literature.

---

## Output deliverable

A single markdown file at the orchestrator's designated path (default: `sessions/session-{N+1}/external-research-candidate-list.md`) containing:

1. **Header**: date, search-coverage timestamp, framework-state-snapshot citation (last weave-update SHA)
2. **Pre-search baseline**: brief note on what was checked in step 1 of the pre-search workflow (closed mechanisms / EVOI / §VII / W-DIA-* already-investigated)
3. **5-10 ranked candidates** in the per-candidate output schema above
4. **Rejected near-misses** (optional): 2-5 candidates that ALMOST passed but failed one specific criterion, with the failure reason — this prevents re-surfacing them in the next search dispatch
5. **Tier coverage table**: count by tier (Mainstream / Heterodox / Speculative / Crackpot) to confirm spread

---

## Deployment template

Spawn the `web-researcher` agent with this prompt structure:

```
Agent(
  subagent_type: "web-researcher",
  description: "External-research conceptual-search for next workshop dispatch",
  prompt: <contents of this file, with the following substitutions filled in by the orchestrator>:
    - {SESSION_N}: the current session number (e.g., 91, 92, ...)
    - {TOPICAL_FOCUS}: optional — if the orchestrator wants to bias the search toward a specific area (e.g., "dark-sector observational anomalies" or "boundary-modification proposals"), include it here; otherwise leave as "no topical bias — canvass all 5 domains broadly"
    - {OUTPUT_PATH}: default `sessions/session-{SESSION_N+1}/external-research-candidate-list.md`
)
```

---

## Calibration corpus (what "good" looks like)

The W-DIA-1/2/3 dispatch sequence is the canonical positive example. The DIA-08-1004-007 + White et al. PRR 2026 sourcing satisfied all 4 selection criteria:

- (a) Specific claim: DIA p. 24 ZPF mode-exclusion derivation `F/A = -π²ℏc/240d⁴`; White et al. Madelung dispersion `ω² = c_L² k² + D² k⁴` with `D = ℏ/(2μ)`
- (b) Substrate-touch: Pillar V (BdG analogs) + Pillar VII (Mellin-cone) + Pillar I-II (propagation Casimir)
- (c) Adversarial readings: volovik vs connes on Bogoliubov reduction; landau vs connes on Casimir derivation
- (d) Q1 YES: math/physics adjudication, not hygiene, not parallel-compute-wave

The candidates this prompt surfaces should pattern-match the DIA shape — not necessarily defense documents specifically, but documents/anomalies/proposals that put the framework's adversarial-reader pairs in genuine structural tension over a specific math/physics claim.

---

## Forward-looking note

This prompt is `K=1` calibration corpus instance for "external-research conceptual-search methodology". If it produces 3 more successful workshop dispatches at S92+, the methodology promotes from SUGGESTION to MANDATORY (per `feedback_rules-compensate-missing-structure.md` K=3 promotion threshold) and earns a permanent rule file. Until then, this template lives at `.claude/templates/` as deployable infrastructure.
