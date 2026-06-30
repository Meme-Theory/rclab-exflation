# Session 116 — Wave Partition Manifest

**Date**: 2026-06-27
**Mode**: SESSION (session-116 namespace), mixed gate types per wave (workshop + compute).
**Scope**: `sessions/session-plan/session-116-context.md` (authoritative per-wave scope + grounding catches).
**Partition rule**: one open question → one wave. Owner = domain specialist matched to the question's substrate. Each wave is MIXED (≥1 workshop + ≥1 compute).
**Dispatch (planner swarm)**: 9 per-wave planners, batched 5 + 4 (≤8 concurrent per `feedback_dispatch-discipline.md`).
**gate_type column** is load-bearing — `/rclab-coordinate` branches dispatch on it (compute → compute-mode; workshop → `/rclab-workshop` 2-agent pattern). Workshop gates close by artifact-existence; only compute gates emit verdict lines to `computations/session-116/s116_gate_verdicts.txt`.

---

## Batch A (planners w1–w5)

### Wave 1 — Q23 Transit power spectrum / A_s  [owner: transit-dynamics-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W1-HTILDE-RECON | workshop | transit-dynamics-theorist × mack-cosmic-bridge: pin the H̃-branch OOM figure (2.38 / 3.15 / 4.56); convention-vs-physics blocker verdict |
| S116-W1-AS-CFB1 | compute | A_s amplitude through τ-fold at canonical L_max; extend S110-CF-B1-TRANSITPS; pre-reg OOM-gap band |
| S116-W1-AS-CF2 | compute | CF-AS-2 second-route A_s amplitude (planner resolves route from atlas-08 Q23 materials) |
| S116-W1-AS-CF3 | compute | CF-AS-3 cross-route reconciliation against the workshop-pinned figure + n_s scheme split (0.959 sqrt-cutoff vs 0.9561 framework) |

*Natural split (if stalled)*: W1a workshop+CFB1; W1b CF-AS-2/CF-AS-3.

### Wave 2 — Q18b Yukawa hierarchy  [owner: connes-ncg-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W2-CK-STAGE2-VERIFY | compute | §VII.CK two-agent cross-axis Stage-2 verify (Axis A connes / Axis B spectral-geometer or transit; no workshop context) |
| S116-W2-PMNS-RESCUE | workshop | connes-ncg-theorist × neutrino-detection-specialist: does external ε_LX rescue the lepton shape leg or is PMNS also walled |
| S116-W2-LEPTON-PMNS-TEXTURE | compute | CF-S115-LEPTON-PMNS-FORCED-TEXTURE; lepton-sector forced texture (math-owner: neutrino-detection-specialist) |

*Natural split*: W2a Stage-2 verify; W2b workshop+texture.

### Wave 3 — Q3 Goldstone mass from disorder  [owner: landau-condensed-matter-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W3-DISORDER-CLOSURE | workshop | landau × phonon-first-cosmologist: given inv5 Imry-Ma FAIL (frac170~4e-5), is the disorder route structurally closed or does a non-Imry-Ma mechanism survive |
| S116-W3-GOLDSTONE-M2 | compute | m²~1/ξ_disorder² under the surviving mechanism OR disorder-route ceiling pin; build on INV5-W2-4 npz; pre-reg frac170 band vs 170× |

### Wave 4 — Q8 4D modulus effective action  [owner: kaluza-klein-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W4-ZNORM-PROVENANCE | workshop | kaluza-klein-theorist × feynman-theorist: is Z(τ)/G_DeWitt=5 first-principles-derived (12D Einstein KK) or fitted; do S74 and S41 routes agree |
| S116-W4-MODULUS-PATHINT | compute | path-integral derivation of kinetic + potential (Gaussian one-loop, fold saddle); pre-reg PASS = agreement with G_DeWitt=5 within tol |

### Wave 5 — Q11 A_F quaternion (H) extraction  [owner: connes-ncg-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W5-H-ROUTE-ADJUD | workshop | connes-ncg-theorist × van-den-dungen-bridge-theorist: o-map vs Wedderburn-singleton vs χ-real-form — same construction or distinct |
| S116-W5-BIMODULE-H | compute | execute S10 o-map bimodule construction yielding ℍ; pre-reg PASS = dim_ℝ(ℍ)=4 correct quaternionic real form (machine-exact) |

---

## Batch B (planners w6–w9)

### Wave 6 — Q12 τ=0 initial conditions  [owner: quantum-foam-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W6-BC-FORK | workshop | hawking-theorist × quantum-foam-theorist: Hartle-Hawking no-boundary vs Vilenkin tunneling for Ψ(τ=0); does either close the inv11 e-fold gap |
| S116-W6-WDW-IC-REFINE | compute | WDW Ψ(τ) refinement under workshop-selected BC; re-evaluate clause_efold; build on INV11-W3-3 npz; pre-reg N_e band vs 3.1 |

### Wave 7 — Q33 §VII.AJ.STATE-PROJ  [owner: volovik-superfluid-universe-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W7-STATEPROJ-BCS | compute | BCS-grounded substrate-IS image of R_3HeB=+0.03536 at P_pc=21.22 bar; (a−b)/(a+b) shape; pre-reg PASS vs published precision |
| S116-W7-ALGEBRA-AXIS | workshop | volovik × landau: is STATE-PROJ (algebra-DEPENDENT) orthogonal to OP-PROJ (algebra-INVARIANT R_∞≈−1.892) or do they collapse |

### Wave 8 — Q30 Forward bridges FWD-C1 / FWD-C2  [owner: connes-ncg-theorist]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W8-FWDC1-LANDING | compute | Pillar I↔II bridge (n_s ↔ Planck CMB); 5-anatomy+3-level; PRE-FLIGHT confirm c_sub canonical exists (was S88 blocker) else mechanical-closure PRE-REG-INC |
| S116-W8-FWDC2-LANDING | compute | Pillar II↔V bridge (Mellin s=3 ↔ BdG spectral triple); 5-anatomy+3-level (math-owner: volovik/connes) |
| S116-W8-BRIDGEMAP-INDEP | workshop | connes-ncg-theorist × van-den-dungen-bridge-theorist: FWD-C2 bridge-map class (HKR/Connes-Karoubi/K-theory) + FWD-C1 Hybrid Independence Test |

*Natural split*: W8a FWD-C1+pre-flight; W8b FWD-C2+workshop.

### Wave 9 — Q36 D_K sectors p+q=15  [owner: baptista-spacetime-analyst]

| Gate ID | gate_type | Scope |
|:--------|:----------|:------|
| S116-W9-SATURATION-ADJUD | workshop | baptista-spacetime-analyst × spectral-geometer: does p+q=15 shift bottom-K/w0_FW or is it Friedrich-Bär-saturated at ≤14 |
| S116-W9-GTBUILDER-L15 | compute | GT-builder extension to p+q=15; construct (15,0)/(0,15)+mixed, diagonalize, report observable shift; FEASIBILITY pin mandatory (math-scripts.md Casimir pre-check); GPU |

---

## Gate-ID collision check

S116-* prefix; no collision with S115 gate-ID space (verified against `computations/session-115/`). Per-wave planners cross-check `computations/session-115/s115_gate_verdicts.txt` before finalizing IDs.

## Dispatch order

1. Batch A: planners w1–w5 (parallel, background, `name=planner-w{i}`).
2. Wait ALL → Batch B: planners w6–w9 (parallel).
3. Phase 3 validation (compute gates) → user checkpoint → WP prompters.
