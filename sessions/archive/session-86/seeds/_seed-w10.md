# Seed file — sessions/archive/session-86/session-86-w10-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w10-workingpaper.md` (339 lines / ~42KB)

## Candidates

### Candidate 1 — Mellin-cone residue infrastructure post-mortem and repair pathway

**What it would do**: Open a 2-agent workshop on the W2 C9 (`S86-MELLIN-HEAT-KERNEL-INFRA` FAIL at value 9.456) and W2 C10 (`S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` INFO with non-physical residue 280743+0j) infrastructure failures, plus the upstream S85 W0-L Mellin-cone S3 residue FAIL (1.814e+06). Determine whether the Mellin-cone residue extraction has a recoverable bug (e.g., off-pole Hankel contour deformation, SD-subtraction sign), or whether the truncated finite-spectrum substrate is fundamentally incompatible with the Connes-Moscovici Mellin-Barnes residue scheme. Output: either (a) a concrete repair-pathway spec for S87 with pre-registered PASS criteria, or (b) a structural-no-go theorem stating the truncation regime in which the Mellin-cone scheme breaks down.

**Why it's worthwhile**: C37 (`S86-MU-BC-V2-ZETA-AT-INTERIOR`) PRE-REG-INC explicitly cites C9 FAIL as the obstruction (WP §W10-1). The S87 carry-forward `S87-MU-BC-V2-ZETA-AT-INTERIOR-RE-ATTEMPT` is "1h once prereq chain is live (4-6h if Mellin-cone repair is included)." The 4-6h Mellin-cone repair is the load-bearing item — it gates the third route to integer-12 AND any future substrate-spectral probe that uses `analytic_zeta(s, L_max)`. The S85 → S86 chain shows persistent failure (S85 FAIL → S86 FAIL/INFO), suggesting this is not a one-off bug. Diagnosing it now is higher-leverage than re-attempting C37 in S87 with the same broken infrastructure.

**Type**: 2-agent workshop

**Suggested agents**: connes-ncg-theorist, lizzi-spectral-functional-theorist

**Rounds**: 3 (R1 lizzi steelman the Mellin-cone scheme + diagnose; R2 connes respond with finite-triple compatibility analysis; R3 converge on repair-or-no-go)

**Context the workshop will need**:
- W2 C9 verdict line (FAIL, value 9.456, MB-Connes-Moscovici, SD-subtracted): `computations/s86_gate_verdicts.txt:95-96`
- W2 C10 verdict line (INFO, value 280743+0j, analytic-continuation, off-pole-Hankel): `computations/s86_gate_verdicts.txt:91`
- S85 W0-L Mellin-cone S3 residue verdict line (FAIL, 1.814e+06)
- W2 C9/C10 producing scripts (`_mellin_cone_residue.py` and prerequisites)
- The connes-ncg expansion as substrate-spectral substitute for BLV (S54 result; cross-pillar already established)
- Pre-registered PASS spec or no-go criterion: workshop must emit one of the two within R3

### Candidate 2 — Charge-conjugation-doubling 12 → 24 cross-route convergence as a permanent identity

**What it would do**: Solo synthesis (1 agent) re-examining the WP §"Cross-route convergence" claim: C38 PASS at integer 12 (`dim(H_F^quark) = 6+6`) and C39's INFO loose match at integer 24 (`2·dim(H_F^quark)`, charge-conjugation-doubled) are methodologically orthogonal but converge on the same quark sub-block of M_F. The synthesis would search for a THIRD independent witness — e.g., the spectral-action a_2 quark-trace coefficient, the doubled-flavor inverse-Higgs structure, the Connes-Chamseddine spectral-action functional's quark-color trace — that produces 12 or 24 from a non-rep-theoretic and non-heat-kernel route. If a third witness lands, the convergence consolidates from "corollary at §VII.R" to "permanent identity" eligible for §IV (or wherever permanent rep-theoretic identities live in the registry).

**Why it's worthwhile**: The WP synthesis explicitly states "the convergence is the harvest, not the individual verdict polarities." But the convergence as recorded is two routes (one PASS, one INFO loose). For a structural identity, the framework's own discipline (epistemic-discipline.md "evidence hierarchy: structural constraints permanent") prefers more witnesses. C38's PASS is exact; C39's INFO is at 0.45% deviation. A third independent route — if it exists — would either confirm the doubling pattern as substrate-fundamental or expose C39's match as numerical coincidence. This is single-agent synthesis work, not a multi-round workshop, because the candidate witness routes are already enumerable from the eight pillars.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (best fit: spectral-action a_2 quark-trace coefficient is in his domain)

**Rounds**: N/A (solo)

**Context the workshop will need**:
- C38 verdict line and its substitution chain (WP §W10-2 lines 134-146)
- C39 candidate catalogue (WP §W10-3 lines 175-189) — the 18-entry table with rel_err for each
- The CCM 2007 finite-triple structure: A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ), KO-dim 6, ε signs (+1, +1, -1)
- The spectral-action functional Tr f(D/Λ) and which moments produce trace numerators 12 or 24 directly
- The §VII.R positive corollary text now landed in `permanent-results-registry.md` §VII.R.1
- Explicit pre-registration: solo synthesis emits either (a) "third witness identified, identity promotes from §VII.R.1 corollary to permanent identity" with 4-field S87 verification gate, or (b) "no third witness within enumerated pillars; identity remains §VII.R.1 corollary"

### Candidate 3 — Distinguishability of V.2's truncated-cache log-slope as a 2N_c-detector

**What it would do**: Solo synthesis examining whether the V.2 producing script `s85_w0_d_spec_alt_derivations.py` (small-t log-slope of truncated heat trace at L_max=8) systematically returns numerator `2·N_color·N_subblock` regardless of which sub-block dominates the finite triple, OR whether 24 = 2·dim(H_F^quark) is a substrate-content-dependent identification. Test: drive the same V.2 machinery against a controlled artificial sub-block insertion (e.g., a 2·dim(H_F^lepton) = 8 stress test, a 2·dim(H_F^1-gen) = 32 test). If V.2 produces the doubled integer regardless of input, the C39 loose match is a machinery artifact, not substrate-spectral evidence. If V.2 produces the correct doubled integer for each test, the 24 = 2·12 reading is structurally sound.

**Why it's worthwhile**: WP §W10-3 says (line 231): "0.45% residual deviation from `24/(4π)²` exceeds the strict 0.1% threshold required to confidently declare 'V.2 sampled the wrong SD weight.'" The S87 carry-forward `S87-MU-BC-V3-HEAT-KERNEL-CONE-APEX` re-runs at d_spec=8 cone-apex, which addresses normalization but not distinguishability. Whether the V.2 machinery actually CAN sense quark-sub-block content (vs. uniformly producing doubled-integer outputs) is an orthogonal diagnostic. This determines whether C39's "corroborative evidence" claim is structural or accidental — directly affects §VII.R.1 corollary's strength.

**Type**: solo (1 agent)

**Suggested agents**: spectral-geometer (already authored C39; has machinery context)

**Rounds**: N/A (solo)

**Context the workshop will need**:
- V.2 source script `computations/s85_w0_d_spec_alt_derivations.py` (508 lines, SHA `22ab12e3...`) — re-run against artificial sub-block insertions
- C39 candidate catalogue (WP §W10-3): all 18 candidates, integer prefactors {6, 8, 12, 16, 24, 32}
- L_max=8 cache (`s84_spectrum_cache_L8_tau019.npz`) — required as the V.2 machinery's input
- L_max=10 cache for cross-check that the doubling depends on L_max truncation level
- Pre-registered gate: solo emits either (a) "V.2 machinery distinguishes sub-blocks" with rel_err per controlled-stress test, or (b) "V.2 machinery produces doubled-integer artifact regardless of input; C39 loose match is non-structural"

### Candidate 4 — §VII.R meta-theorem re-statement: from exclusion-only to inclusion-with-bounds

**What it would do**: 2-agent workshop on the §VII.R Meta-Theorem extension. Pre-S86 W10, §VII.R was an exclusion-only catalogue (FI-axis FORBIDDEN, rank-axis FORBIDDEN, Mellin-support-axis FORBIDDEN). C38 PASS introduces a positive corollary (§VII.R.1: dim(H_F^quark)=12 admitted under all 3 axes). The workshop would produce a re-stated meta-theorem with explicit predicate logic: "exclusion axes ∩ admitted positive identities = ∅" formalized so that future positive corollaries (e.g., from Candidate 2) can be tested for compatibility with the exclusion catalogue *before* they're registered. Output: a re-stated §VII.R with its predicate structure pinned and an entry-test procedure for future positive corollaries.

**Why it's worthwhile**: WP §"Permanent-results-registry landing" notes the corollary "is methodologically distinct from FI/RD exclusion." This is correct but informal. As more positive corollaries accumulate (Candidate 2 may produce one; future substrate-spectral integers will), §VII.R needs a clean entry-test or it accumulates inconsistencies. Doing this when only one positive corollary exists is cheaper than retrofitting after several land. This is a structural cleanup that pays forward — it's not new substrate physics, it's making the meta-theorem usable as a filter.

**Type**: 2-agent workshop

**Suggested agents**: connes-ncg-theorist, mack-cosmic-bridge

**Rounds**: 2 (R1 connes draft re-statement; R2 mack stress-test against future positive corollaries / observational anchors)

**Context the workshop will need**:
- §VII.R original statement in `sessions/permanent-results-registry.md` (the 3-axis exclusion meta-theorem)
- §VII.R.1 positive corollary text just landed in S86 W10
- The 3 forbidden axes' precise definitions (FI, rank, Mellin-support)
- C38's substitution chain (WP §W10-2 lines 134-146) as the canonical example of an admitted positive identity
- Explicit pre-registration: workshop emits a re-stated §VII.R with (a) predicate logic, (b) entry-test procedure for new positive corollaries, (c) cross-check that the existing 3 exclusion axes remain valid under the re-stated form

## Notes on candidates not raised

- **The W9-5 V.2 EW-sector OPEN status update (DISCHARGED-WITH-CAVEAT)** is already correctly reflected in WP §"Constraint-Map Updates" — no follow-up needed.
- **The verdict-format drift (S86+ vs legacy)** is correctly classified as "minor self-report" hygiene per `feedback_fix-in-session-never-defer.md` — docs-only patch, not a workshop topic.
- **The S87 carry-forwards (`S87-MU-BC-V2-ZETA-AT-INTERIOR-RE-ATTEMPT` and `S87-MU-BC-V3-HEAT-KERNEL-CONE-APEX`)** are correctly 4-field-spec'd in the WP — they belong in `/rclab-plan` for S87, not in a workshop. Candidate 1 and Candidate 3 above are deeper-leverage variants of the same investigation that go beyond what the S87 carry-forwards as written would discover.
- **Sub-block uniqueness at integer 12** in the {4, 12, 16, 48, 96} ladder is already established at machine ε in C38 — no further workshop adds value.
- **The substrate-framing interpretation** (substrate's EW-sector revealing rep-theoretic skeleton through `mu_BC`) is correctly stated in WP §"Substrate-framing" — no follow-up needed.
