---
name: S84 W7a-79 EQUIV-CLASS-FALSIF verdict (first-pass, PROVISIONAL)
description: Literature-walk falsifier for framework structural uniqueness — PASS at S84 close with 65 papers reviewed; 26 KO-dim=6 near-misses all from shared Connes-program ancestor
type: project
---

# S84 W7a-79: S84-EQUIV-CLASS-FALSIF

Date: 2026-04-19
Gate: S84-EQUIV-CLASS-FALSIF (long-horizon monotone falsifier)
Verdict: **PASS** — value=0, scheme=joint_signature, convention=band_4.18_to_5.18, L_max=N/A
sha256: e01d6fa3c66499dff30767ab03e33d858b3f83965b639a0a1feb7dae797f4268 (closure/audit)

**Why:** Falsifier gate testing the framework's structural-equivalence-class uniqueness claim. Predicate: any construction with BOTH KO-dim=6 AND |E_cond|~L^p with p in [4.18, 5.18] (±0.5 band around 4.68).

**How to apply:** Verdict is PROVISIONAL — monotone falsifier extends across S85-S90. Once a matching construction is found, verdict becomes FAIL permanently. Absence of match is provisional until catalog is exhaustive (>=200 papers).

## First-pass catalog stats (65 papers)

- n_total: 65 (exceeds 50-paper S84 target)
- n_ko_eq_6 (strict): 26
- n_in_band: 0
- n_matrix_models: 16
- **falsification_count: 0**
- near_miss_ko_only: 26 (all from Connes NCG-SM program)
- near_miss_ecd_only: 0

## Key structural finding

The 26 KO-dim=6 near-misses are ALL descendants of Chamseddine-Connes-Marcolli 2006 (hep-th/0610241) — the framework's own algebraic ancestor via A_F = C + H + M_3(C). These are ALMOST-COMMUTATIVE geometries M×F with continuum Lambda-cutoff spectral action, NOT matrix-model L-truncation. Different computational object entirely.

The 0 band-criterion hits confirm the matrix-model/continuum-NCG split: IKKT/BFSS (no KO-dim in Connes sense), fuzzy spheres (KO-dim=2), Barrett-Glaser random NCG (restricted to p+q<=3, KO-dim 0-3). Barrett-Glaser 2015 is the most structurally likely candidate for a future KO-dim=6 matrix-model extension.

## Critical caveat

Framework's OWN G36 gate (S83-MATRIX-MODEL-CLASSIFICATION) was FAIL: R2_power=nan, R2_linear=0.428571, b_power=nan. The 4.68 exponent comes from the plan background, not from a settled computation. If W7b-75 or W7b-76 downgrade G36, the [4.18, 5.18] band re-centres and §W7-79 must be re-run.

## Correspondence-table implication

PASS supports §VII.N landing (admissibility singleton + IKKT anti-correspondence + 11-dim exclusion). With HET-DECOMP PASS and this PASS, Scenario A is in play for W7+W8 consolidation — §VII.N lands at S84 close if remaining positive-correspondence gates return as expected.

## Carry-forward (S85 priorities)

1. Catalog extension +20 papers (2020-2026 NCG program continuations)
2. Band re-centering if G36 downgrades in W7b-75/76
3. Barrett-Glaser KO-dim=6 Monte Carlo extension follow-up (most likely external band hit)
4. Twisted-triple linkage (W7b-77)
5. Van den Dungen KK-bridge investigation

## Artifacts

- `computations/s84_w7a_equiv_class_falsif.py` (script)
- `computations/lit_search_manifest.jsonl` (65-entry catalog)
- `computations/s84_w7a_79_data.npz` (numpy dump)
- `sessions/archive/session-84/session-84-w7-workingpaper.md` §W7-79 (filled)
- `computations/s84_gate_verdicts.txt` (verdict line appended)
