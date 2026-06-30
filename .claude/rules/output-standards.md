# Output Standards

<!-- No paths: frontmatter — loads unconditionally for all agents -->

## Action Items Format

Every action item must include all 7 components:

1. **What** — the specific deliverable
2. **Who** — which agent or role
3. **Input** — what they need to start
4. **Output** — what they produce
5. **Format** — file type and location
6. **Deadline** — session or phase
7. **Depends on** — prerequisite action items

## Handoff Documents

Every session produces a handoff document with these 7 sections:

1. Session metadata (date, format, agents, prompt)
2. Key results (numbered, specific)
3. Constraint map updates (new entries, state changes)
4. Open questions (numbered, actionable)
5. Action items (using 7-component format above)
6. Files created or modified (paths)
7. Next session recommendations

## General Output Rules

- **Mark preliminary results** — label any claim not yet validated by computation as "PRELIMINARY"
- **Cite sources precisely** — paper numbers, file paths, line numbers
- **One writer per file** — designated writer only; others contribute via messages
- **Gate verdicts are permanent** — once recorded, a verdict cannot be retroactively changed
- **No filler** — avoid "as we can see," "it's worth noting," "interestingly"

## Workshop Wrap-Up "What Changed" — Numerical vs Structural Distinction

Workshop Wrap-Up "What Changed" sections (and analogous handoff §3 "Constraint map updates" sections) MUST distinguish two epistemic categories:

**(a) Numerical revisions** — quantitative recalibrations of values, σ-bands, ratios, OOM splits. Examples:
- `σ_naive = 4.250 → σ_HypB = 2.222` (σ-discrimination band re-pin)
- `"~45 OOM" → 47.081 OOM` exact (OOM-split numerical sharpening via Sage QQ)

**(b) Structural changes** — reframings that alter the EPISTEMIC TYPE of the result, not just its numerical value. Examples:
- `single-binary falsifier → rank-2 product detector` (type promotion: 1-detector → 2-detector outcome matrix)
- `PRIMARY+CONFIRMATION → SOURCE-DOUBLE-CITE-CO-PRIMARY` (anchor-structure reclassification)
- `1D successor-promotion → 4×4 partition grid` (dimensional reading change)

**Why the distinction matters**: numerical revisions are SUBORDINATE to structural reframings; structural changes are the more durable workshop outputs. A handoff that lists numerical revisions in the same bullet-block as structural changes confuses readers about which results are durable vs which are precision-tightening updates. The two MUST be in separate sub-sections of "What Changed".

**Format**:

```markdown
## What Changed

### (a) Numerical revisions

- `σ_naive = 4.250 → σ_HypB = 2.222` (Sage QQ Path-C inheritance-forced LiteBIRD discrimination)
- `"~45 OOM" → 47.081 OOM` exact (Sage-verified)

### (b) Structural changes

- single-binary falsifier → rank-2 product detector (Row #2 promoted to 2×2 outcome matrix)
- PRIMARY+CONFIRMATION → SOURCE-DOUBLE-CITE-CO-PRIMARY (V1+C1 sequential-chain registry-anchor structure adopted)
```

## Carry-Forward Dependency Enumeration (extends Action Items §7 "Depends on")

Carry-forward 4-field specs in workshop Wrap-Up sections (and §5 "Action items" of the handoff document) SHOULD explicitly enumerate dependencies in the §7 "Depends on" field — rather than leave dependencies discoverable at next-session plan time.

**Required when present**:
- Cite the upstream gate / data file / module / canonical_constants pin by name
- For multi-input dependencies, enumerate ALL inputs (not just the most prominent one)
- For transitive dependencies, cite the PROXIMATE upstream (next-session plan author resolves transitive chain)

**Format**:

```markdown
### Action Item N

1. **What**: Compute δ_speed_substrate via Mellin-Barnes residue at the a_4 pole (s=2)
2. **Who**: gen-physicist
3. **Input**: B1 eigenvalue trajectory data
4. **Output**: δ_speed_substrate ± regime tag
5. **Format**: computations/session-{N}/s{N}_delta_speed_mellin_barnes_residue.py (.npz + .png)
6. **Deadline**: next session, Wave 2
7. **Depends on**:
   - B1 trajectory data from the D_K^2 spectral computation (UPSTREAM GATE)
   - meta-classifier_v2 spec from this workshop (REGISTRY ENTRY: §VII.X classification (a))
   - canonical_constants.py: c_sub_baseline = 2.238, r_PathH = 0.0074705
```

**Why this matters**: explicit enumeration clarifies wave order at next-session plan-freeze. Without it, the planner must walk the carry-forward chain to discover prerequisites — slow, error-prone, and prone to missing inputs that are only implicit. The 7th "Depends on" field is mandatory in the action items format above; this rule extends it to be a structured enumeration when the carry-forward has multiple substantively distinct prerequisites.
