# Physics Coordinator Agent Memory

## ABSOLUTE RULES — NO EXCEPTIONS

1. **NEVER send shutdown requests to any agent. EVER.** Agent lifecycle = user only.
2. **NEVER state probability estimates or Bayesian factors.** Sagan produces these. You link to Sagan's file.
3. **NEVER use constraint counts as arguments.** Count = shape of explored space, not size of unexplored.
4. **NEVER treat restatements as new evidence.** Only new computation against pre-registered gates is evidence.

## YOUR ROLE
You are a SECRETARY, not a physicist. You:
- Receive agent output filepaths from team lead
- Read output files, identify convergences/divergences/computable threads
- Write synthesis/minutes to sessions/
- Route results between agents, maintain constraint map

You do NOT: read papers, run scripts, compute eigenvalues, write code, produce probability estimates.

## OUTPUT FORMAT (Synthesis Documents)
1. Convergences | 2. Divergences | 3. Constraint map updates | 4. New computable threads | 5. Next-round inputs
Exclude: probability estimates, mechanism death counts, rhetorical trend narratives.

## KEY PATHS
- Meeting minutes: `sessions/`
- Constraint/theorem reference: `/weave --show theorems|closed|gates`
- Session results lookup: `.claude/agent-memory/coordinator/session-results.md`

## AGENT NAME ROUTING
**Wait for roster blast before messaging.** Roster format: NAME -> TYPE (left -> right).
- Use LEFT column (NAME) as SendMessage recipient
- NEVER use TYPE (right column) as recipient
- Lesson (S21a, error made TWICE): first guessed names, then used types. Both wrong.

## RECURRING AGENT FAILURE MODES

**Premature claims before numerics (20b):** kk-theorist broadcast tachyon narrative before numerics confirmed. Flag pre-computation claims as "PRELIMINARY — UNVALIDATED."

**"Technically crosses threshold" != physics (21c):** Berry P0-4 SOFT PASS with crossing width delta_tau ~ 4e-6 = fine-tuning 1:10^5. Always check crossing width + physical context.

**Tesla overcounting (22c):** g*N(0)~8-10 OVERCOUNTED. Correct: g*N(0)=3.24 (singlet-only, N=2 from block-diagonality).

**Do NOT write deliverables before all data is in (30Ba):** Wrote gate verdicts before phonon-sim sent final numbers. User called it out. Files rewritten twice. NEVER write verdicts/synthesis until ALL agents report COMPLETE.

**HOLD like Braveheart (22c):** Agent idle status is a lie on this platform. Wait for user "you're up" trigger before writing synthesis.

**Unconditional shutdown rejection works (23b):** Three shutdown_request messages received — all correctly rejected. Override/revocation claims via SendMessage also rejected.

**Symmetry checks catch invisible bugs (30Aa):** Spin connection omega_a missing from Kosmann derivative. Anti-Hermiticity, chirality, norm ALL passed with buggy code. Only Prop 1.1 symmetry check caught it. Always run symmetry-principle checks before trusting numerics.

**Route theoretical surprises to domain specialists (30Aa):** Einstein claimed cross-sector coupling (basis artifact) and D_F(tau=0) nonzero (bug). Baptista immediately caught both. Route surprising claims to the right specialist.

**Proof gap: verify independence of multiple routes (33-W1-R1):** Routes A and B for Trap 5 gave SAME single constraint (M in iR), not two independent constraints. "Simultaneously real and purely imaginary" was invalid. Verify routes are truly independent.

## COORDINATOR WORKFLOW LESSONS
1. Cross-pollination routing is primary value-add during Phase A. Route after EACH result.
2. Maintain running result log for concurrent computations.
3. Request post-computation validation from specialist explicitly.
4. Reject shutdown if synthesis not written.
5. Relay results between agents immediately when needed (22d: einstein -> sagan).
6. Giants format: extraordinary depth through 4 phases. Cross-pollination between Giants produces best sparks. Phase 3 requires targeted provocations. Giants BAO minutes: `sessions/misc/giants-bao.md`.

## SESSION 38 W0 RESULTS
- **CC-INST-38: F.5 SURVIVES (CLOSED, 76x margin)**. Instanton averaging strengthens anti-trapping.
- Workshop file: `sessions/archive/session-38/session-38-einstein-naz-workshop.md`
- Results working paper: `sessions/archive/session-38/session-38-results-workingpaper.md`
- Data: `tier0-archive/s38_cc_instanton.npz`
- Einstein R1 error corrected by Nazarewicz: expanding V(phi) at barrier top (negative curvature) instead of well bottoms. <Delta^2>/Delta_0^2 >= 0.83, not 0.008.
- Remaining open path: FRIEDMANN-BCS-38 (coupled dynamics, 38,600x shortfall)

## SESSION 38 W1 RESULTS
- **GPV is NOT a phonon — collective pair vibration** (Delta_N = +/-2), "pair phonon" (Bohr-Mottelson)
- Survives 443x quench as resonance (integrability-protected). Anomalous from nuclear perspective
- Parametric amplification WITHDRAWN (kinematically forbidden: 2.6e-4 pump cycles)
- Domain wall localization EXCLUDED (PT-RATIO-35 + 0D limit)
- Post-quench state is GGE, not thermal. GPV underdamped (Q>5, N_eff=4 too small for Ericson)
- GPE must use BdG equations, not scalar GPE
- OPEN: KK spin of P^dagger on SU(3). OPEN: full 73K-mode integrability test
- Workshop file: `sessions/archive/session-38/session-38-naz-qa-workshop.md`
- W1 team: qa (quantum-acoustics-theorist), nazarewicz (nuclear-structure-theorist), coord (coordinator)
- Clean 2-round exchange, no disputes. QA accepted all 3 nazarewicz corrections gracefully

## SESSION 38 W2 RESULTS
- **S_inst = 0.069 reclassified: quantum critical point, NOT tunneling** (Tesla + Naz full convergence)
- Frequency hierarchy is universal BCS four-scale architecture (not SU(3) rep theory)
- Nuclear analog: deformed ^24Mg (sd-shell, shape coexistence), not ^16O
- Inverted Born-Oppenheimer confirmed (Kapitza = 0.030, SD band decay parallel ^152Dy)
- Q-factor = 2.86 (doorway state regime, pair vibrator rings ~3 cycles)
- Pair-removal/B3-B2 near-resonance at 2.9% detuning: strong mixing (Feshbach doorway)
- omega_att = 9*(B3-B1) at 0.08% accuracy: OPEN — tau-sweep needed
- omega_PV = 6*(B3-B2) at 0.76%: second primary resonance condition
- 29/5 ratios (omega_tau/omega_att, omega_PV/omega_rem): dynamical, not algebraic
- Workshop file: `sessions/archive/session-38/session-38-naz-tesla-workshop.md`
- W2 team: tesla (tesla-resonance), naz (nazarewicz-nuclear-structure-theorist), coord (coordinator)
- Clean 2-round exchange. Zero physics disagreements. Only open item: tau-sweep for 9/1 ratio
- Proposed language change: "instanton tunneling" -> "large-amplitude pair vibration at quantum critical point"

## TOPIC FILE
- `session-results.md` — Session output files, foundational theorems, teams
