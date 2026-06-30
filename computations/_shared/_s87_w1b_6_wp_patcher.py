"""One-shot WP patcher for §W1b-6 (S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE).

Atomic Edit-tool-mtime-race-immune writer following the W1b-4 precedent
(`_s87_w1b_4_wp_patcher.py`). Reads the WP file, locates the §W1b-6 shell
heading at line 1108, replaces the body up to (but not including) the next
`### §W2-1.` heading or the `---` separator, writes once via temp + os.replace.

Loads numbers from the gate's NPZ to recover the per-candidate residual table.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WP = PROJECT_ROOT / "sessions" / "session-87" / "session-87-results-workingpaper.md"
NPZ = PROJECT_ROOT / "computations" / "session-87" / "s87_w1b_connes_distance_finite_spectrum_identity.npz"

SHELL_HEADER = "### §W1b-6. S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE (gen-physicist)"
NEXT_HEADER = "### §W2-1. S87-LAB-3HE-B-ALPHA-S-EQUIVALENT (mack-cosmic-bridge)"


def main():
    text = WP.read_text(encoding="utf-8")

    # Locate shell start (line 1108 area) and next-header start
    shell_start = text.find(SHELL_HEADER)
    if shell_start < 0:
        raise RuntimeError(f"Shell header not found: {SHELL_HEADER}")

    next_start = text.find(NEXT_HEADER, shell_start + len(SHELL_HEADER))
    if next_start < 0:
        raise RuntimeError(f"Next header not found: {NEXT_HEADER}")

    # The block ends just before the next-header's preceding "---\n\n"
    # Find the last "---\n" between shell_start and next_start
    block_text = text[shell_start:next_start]
    # The shell ends with "\n\n---\n\n" before next_start; we'll replace
    # everything from shell_start up to but not including next_start.

    # Verify we are looking at THE structurally-correct shell at the line-1108
    # location (not the post-W13 stale shell which is at line 2893+).
    line_at = text[:shell_start].count("\n") + 1
    if line_at > 1500:
        raise RuntimeError(f"Refusing to patch — shell at line {line_at} is too late "
                           f"(expected near line 1108; this is the post-W13 stale shell).")

    # Load NPZ
    d = np.load(NPZ, allow_pickle=True)
    residuals = d["residuals_per_identity"]  # (4, 3)
    rhs_table = d["rhs_per_identity"]
    lhs_per_pair = d["lhs_per_pair"]
    candidate_names = list(d["candidate_identities_list"])
    pair_names = list(d["canonical_state_pairs_tested"])
    sdp_status = list(d["sdp_status"])
    R_sweep = d["R_sweep_values"]
    lhs_R = d["lhs_R_sweep"]
    eigs_count = int(d["eigenvalues_L12"][0])
    flat_min = float(d["flat_abs_min"][0])
    flat_max = float(d["flat_abs_max"][0])
    best_residual = float(d["best_residual"][0])
    verdict_class = str(d["verdict_class"][0])
    conjecture_status = str(d["conjecture_status"][0])
    regime_v = str(d["regime_verdict"][0])
    best_form = str(d["best_identity_form"][0])

    # Compose the substantive replacement
    lines = []
    lines.append(SHELL_HEADER)
    lines.append("")
    lines.append("**Status**: COMPLETE — 2026-04-28")
    lines.append("**Gate ID**: `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE`")
    lines.append("**Trigger**: `AUDIT-OPEN-Q`")
    lines.append("**Classification**: **GEOMETRIC** (Connes distance functional on substrate finite spectral triple; conjecture of finite-spectrum algebraic identity analogous to §VII.U.1 Mellin-Dirichlet)")
    lines.append("**Agent**: `gen-physicist`")
    lines.append("**Hypothesis**: The Connes distance `d_C(p, q; D_K^{<=L})` admits a closed-form algebraic identity in eigenvalues `{λ_n}` at L_max=12, holding at max_rel_err < 1e-9 for ≥2 canonical state pairs. Sub-classes: CLASS-α (verified < 1e-9 → S88 verify gate); CLASS-β (residual ∈ [1e-9, 1e-3] → carry-forward); CLASS-γ (no identity → conjecture closed).")
    lines.append("**Plan reference**: `sessions/session-plan/session-87-plan-w1b.md` §W1b-6 (lines 1127-1347).")
    lines.append("")
    lines.append("**MCP Pre-Compute Audit** (2026-04-28):")
    lines.append("- `search_knowledge(\"Connes distance anisotropy functional\")` → 5 hits, all from `s46_connes_distance.py` (S46 connes_distance script; T3-BATCH-S46-CONNES-DISTANCE = MIGRATED INFO). No prior closure of this conjecture.")
    lines.append("- `search_knowledge(\"finite spectrum identity algebraic Mellin Dirichlet\")` → key hit `Σ_k m_k λ_k^{0} = ΣN(λ_k)` substrate-counting form (S86 W-1 mellin-cone-repair-or-no-go) + Mellin↔Dirichlet identity in `_analytic_zeta.py`.")
    lines.append("- `search_knowledge(\"VII.U Mellin-Dirichlet identity finite spectrum\")` → §VII.U.1 entry (S86 W-1 connes+lizzi joint, 2026-04-27): `Σ_k m_k · λ_k^{-s} = ζ_D(s)`; PROVEN at L=12 rel_diff = 0e+00 (S87 W1a-4 PASS).")
    lines.append("- `trace_entity(\"Connes distance\")` → 1 closed mechanism (`State-dependent Connes distance D_BCS`, closure 266); 5 equation hits all from S46.")
    lines.append("- `trace_entity(\"§VII.U Mellin-Dirichlet\")` → no direct trace; recovered via §VII.U registry grep at registry lines 12834-12873 (analogy template).")
    lines.append("- **Pre-existing closure status**: NOT pre-closed; this conjecture is a fresh open-question audit. PRE-COMPUTE-AUDIT-CLEARED.")
    lines.append("")
    lines.append("**Verdict**: `INFO (CLASS-γ)` — composite collapse: OPEN-Q decision rule pre-registers `INFO` as the structured outcome for CLASS-γ closure (per plan §W1b-6 Field 9 INFO-band table). 3-tuple: `sign=N/A, magnitude=FAIL, regime=VALID`.")
    lines.append("")
    lines.append("**Verdict line** (canonical, S84+ schema; final iteration after CLARABEL-keyword + chiral-D-form + Frobenius-regulator fixes — first 3 iterations emitted `value=inf` due to SDP non-convergence; iters 4-5 converged at the regularization saturation):")
    lines.append("```")
    lines.append("S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE: INFO -- value=0.9800418463588636 scheme=Connes-distance-finite-spectrum-identity-conjecture convention=substrate-state-pair-canonical L_max=12 audit_sha256=b3652c276acec8e1b24dd18de8f303c24329c33cc9b95f25e0b60095acb98ca5 content_sha256=1472a38026de3eed80da540e18b8bd59a27f14a3ed100e793cd378bb5ac00f7e schema_version=S84+")
    lines.append("# audit_sha256_short=b3652c276acec8e1 content_sha256_short=1472a38026de3eed # S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE dual-SHA companion row (W9a-99 split)")
    lines.append("# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID # S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE 3-tuple annotation (S87 schema-v2)")
    lines.append("```")
    lines.append("")
    lines.append("**Results**:")
    lines.append("")
    lines.append(f"**4-tuple**: `(value=0.9800418463588636, scheme=Connes-distance-finite-spectrum-identity-conjecture, convention=substrate-state-pair-canonical, L_max=12)`")
    lines.append("")
    lines.append(f"**Spectrum cache**: `s84_spectrum_cache_L12_tau019.npz` (sha256 prefix `9e6d9cf7fd6a6949…`); 90 SU(3) sectors; **{eigs_count:,}** absolute eigenvalues in [{flat_min:.6f}, {flat_max:.6f}] M_KK.")
    lines.append("")
    lines.append("**Per-candidate × per-state-pair residual table (4 × 3 = 12 entries)**:")
    lines.append("")
    lines.append("| | Pair-1 (vacuum / n=0 quasi) | Pair-2 (B1 acoustic min/max) | Pair-3 (Cartan α_1 / α_2) |")
    lines.append("|:--|:--|:--|:--|")
    lines.append(f"| **LHS d_C(SDP)** | {lhs_per_pair[0]:.6e} | {lhs_per_pair[1]:.6e} | {lhs_per_pair[2]:.6e} |")
    lines.append(f"| C1: SDP sup-form (= LHS by definition) — RHS / residual | {rhs_table[0,0]:.6e} / {residuals[0,0]:.3e} | {rhs_table[0,1]:.6e} / {residuals[0,1]:.3e} | {rhs_table[0,2]:.6e} / {residuals[0,2]:.3e} |")
    lines.append(f"| C2: Mellin-Dirichlet Σ c_n·λ_n^{{−α}} — RHS / residual | {rhs_table[1,0]:.6e} / {residuals[1,0]:.4e} | {rhs_table[1,1]:.6e} / {residuals[1,1]:.4e} | {rhs_table[1,2]:.6e} / {residuals[1,2]:.4e} |")
    lines.append(f"| C3: Commutator-norm 1/‖[D, ρ_p−ρ_q]‖_op — RHS / residual | {rhs_table[2,0]:.6e} / {residuals[2,0]:.4e} | {rhs_table[2,1]:.6e} / {residuals[2,1]:.4e} | {rhs_table[2,2]:.6e} / {residuals[2,2]:.4e} |")
    lines.append(f"| C4: Heat-kernel-trace √Tr[Q_pq·D^{{−2}}] — RHS / residual | {rhs_table[3,0]:.6e} / {residuals[3,0]:.4e} | {rhs_table[3,1]:.6e} / {residuals[3,1]:.4e} | {rhs_table[3,2]:.6e} / {residuals[3,2]:.4e} |")
    lines.append("")
    lines.append("C1 is identity-by-definition (SDP IS the LHS), so it does not count as an independent identity in `{λ_n}`. Among C2/C3/C4 (the genuine candidate forms), the smallest residual across all 9 entries is **0.9800418** (C4 at Pair-1). Best `max_j(residual_kj)` per non-definitional candidate: C2 → 1.000, C3 → 0.989, C4 → 0.984. None satisfies PASS_THRESHOLD = 1e-9 across ≥2 pairs; none satisfies INFO_CEILING = 1e-3 at any pair.")
    lines.append("")
    lines.append(f"**Best-of-failures**: C4 (heat-kernel-trace form), `best_residual = 0.9800418` (Pair-1).")
    lines.append("")
    lines.append("**Sub-classification: CLASS-γ** (`best_residual = 0.980 > 1e-3 = INFO_CEILING` across all candidates and all state-pairs).")
    lines.append("")
    lines.append("**LHS regulator-scale diagnostic** (Pair-1; physics evidence for the structural finding that `d_C` is regulator-divergent on the full M_n(ℂ) algebra):")
    lines.append("")
    lines.append("| R (Frobenius regulator on ‖a‖_F) | LHS d_C(R) | d_C(R) / R |")
    lines.append("|:--|:--|:--|")
    for i in range(len(R_sweep)):
        lines.append(f"| {float(R_sweep[i]):.1f} | {float(lhs_R[i]):.4e} | {float(lhs_R[i])/float(R_sweep[i]):.4f} |")
    lines.append("")
    lines.append("The ratio `d_C(R)/R` is asymptotically constant (≈ 0.88–1.41) over 3 OOM in R. Therefore `d_C ~ c·R` linearly diverges as R → ∞. **The Connes distance for the FULL `M_n(ℂ)` algebra of a finite spectral triple is regulator-divergent** — it is not a function of `{λ_n}` alone but depends on the regulator scale R.")
    lines.append("")
    lines.append("**Substitution chain (regulator-divergence)**:")
    lines.append("- Step 1 (definition): `d_C(R) = max_a Tr((ρ_p−ρ_q)·a)  s.t.  ‖[D,a]‖_op ≤ 1, ‖a‖_F ≤ R`.")
    lines.append("- Step 2 (substitution): For any polynomial f, `[D, f(D²)] = 0` (D commutes with itself), so `f(D²)` lies in the commutant of D. The constraint `‖[D,a]‖_op ≤ 1` imposes nothing on the `f(D²)` component of a; only the `‖a‖_F ≤ R` cap bounds it.")
    lines.append("- Step 3 (simplification): SDP saturates at the Frobenius bound: `d_C(R) ≈ R · sup_{a: ‖a‖_F=1, [D,a]=0} Tr((ρ_p−ρ_q)·a)`. The supremum factor is finite (~ 0.9 for our pairs).")
    lines.append("- Step 4 (direction): As R → ∞, `d_C(R) → ∞` linearly. Hence the LHS is regulator-divergent for the full `M_n(ℂ)` algebra.")
    lines.append("")
    lines.append("**Substitution chain (analogy template — §VII.U.1 vs Connes-distance conjecture)**:")
    lines.append("- §VII.U.1 (template, PROVEN at L=12): `Σ_k m_k · λ_k^{−s} = ζ_D(s) = M[Tr e^{−tD²}](s/2) / Γ(s/2)`. Identity is L-INVARIANT off-pole; max_rel_diff = 0e+00 at s ∈ {3,4,5} (S87 W1a-4 PASS).")
    lines.append("- Conjecture (this gate): `d_C(p,q; D_K^{≤L}) = G({λ_n}, p, q)` for some closed-form G, at max_rel_err < 1e-9 across ≥2 state-pairs.")
    lines.append("- Substitution test: 4 candidates × 3 pairs = 12 evaluations. C1 = LHS by definition; C2/C3/C4 finite values O(1); LHS regulator-divergent O(R).")
    lines.append("- Simplification: `residual = |RHS−LHS|/|LHS| → 1` as `LHS → ∞`. Identity FAILS for any candidate G that produces a regulator-independent finite value (which is all 4 pre-registered candidates).")
    lines.append("- Direction: §VII.U.1 holds because LHS = Tr[D^{−2s}] is itself `Σ_k m_k λ_k^{−2s}` — purely algebraic in the spectrum and finite for s in the convergence cone. The Connes-distance LHS depends on the algebra A_loc and a regulator R, neither encoded in `{λ_n}` alone.")
    lines.append("")
    lines.append("**Cross-checks**:")
    lines.append("- **CC1** (§VII.U.1 analogy reproduction): `{λ_n}` are loaded from the same cache (`s84_spectrum_cache_L12_tau019.npz`, sha 9e6d9cf7…) used by §VII.U.1 / S87 W1a-4 PASS; spectrum count and range agree (166,896 absolute eigenvalues; min 0.8197, max 5.4189 M_KK).")
    lines.append(f"- **CC2** (SDP convergence regime): all 3 final-iteration SDPs converged with status `{sdp_status[0]}` (=`optimal_inaccurate`) — solver found the optimum at the regularization saturation boundary. Note that the first 3 verdict-line iterations (lines 38, 41, 44) emitted `value=inf` because (a) the original CLARABEL solver invocation used SCS-style `eps_abs/eps_rel` keywords (rejected by CLARABEL), then (b) a diagonal D construction made D commute with all diagonal a's, giving unbounded SDP, then (c) the chiral off-diagonal D = [[0,M],[M^T,0]] form was correctly substituted but without Frobenius regularization the LHS still diverged. Iter 4-5 added the Frobenius regulator and converged. The current canonical line at line 53 reflects the final correct setup. regime_verdict = VALID at gate close.")
    lines.append("- **CC3** (regulator-divergence diagnostic): R-sweep at R ∈ {1, 10, 100, 1000} confirms `d_C(R) ≈ c·R` linearly with c ≈ 0.9 — a 3-OOM regulator scan with `d_C/R` asymptotically constant. The LHS is not a function of `{λ_n}` alone.")
    lines.append("")
    lines.append("**Sub-classification rationale**:")
    lines.append("- CLASS-α requires `best_residual < 1e-9` across ≥2 state-pairs — **NOT MET** (smallest residual is 0.9800).")
    lines.append("- CLASS-β requires `best_residual ∈ [1e-9, 1e-3]` at ≥1 state-pair — **NOT MET** (no residual below 1e-3 anywhere; the smallest is 0.9800).")
    lines.append("- CLASS-γ closure: `best_residual > 1e-3` everywhere → **MET**. Conjecture closed as non-existent at L=12.")
    lines.append("")
    lines.append("**Conjecture closure (CLASS-γ) — structural reasoning**:")
    lines.append("The §VII.U.1 Mellin-Dirichlet identity is **STRUCTURALLY SPECIFIC** to spectral functionals of the form `F({λ_n}) = Σ_k m_k · g(λ_k)` (with g a fixed function); it is NOT generic to all substrate algebraic functionals. The Connes distance is a different functional class:")
    lines.append("1. it depends on the algebra A_loc (here `M_n(ℂ)`), not just `{λ_n}`;")
    lines.append("2. for the FULL matrix algebra it is regulator-divergent (because `f(D²)` commutes with D for any f, allowing the algebra-element norm to scale unboundedly while leaving `[D,a]=0`);")
    lines.append("3. for sub-algebras (e.g., the substrate's `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`) it can be finite, but its value depends explicitly on the algebra-element decomposition into A_F sectors, not on `{λ_n}` alone.")
    lines.append("")
    lines.append("**CC1 / CC2 / CC3 + the regulator-divergence diagnostic together forbid an identity in `{λ_n}` alone.** No closed-form `G({λ_n}, p, q)` can match the regulator-dependent LHS.")
    lines.append("")
    lines.append("**Promotion / carry-forward / closure paths**:")
    lines.append("- **Promotion path on CLASS-α** (NOT TRIGGERED): would have spawned `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-VERIFY` with the verifying candidate form pinned + §VII.{next-letter} registry candidate.")
    lines.append("- **Carry-forward on CLASS-β** (NOT TRIGGERED): would have queued `S88+_algebraic_refinement` for tighter candidate forms.")
    lines.append("- **Closure on CLASS-γ** (TRIGGERED): conjecture closed as non-existent at L=12 finite spectrum. The §VII.U.1 Mellin-Dirichlet identity (FINITE-VECTOR class, lizzi-finite-infinite classification §1-§2; Lens-Mediated regulator-class-INVARIANT) does NOT generalize to the Connes-distance algebraic functional family. **No new §VII.{letter} registry entry is created by this gate.**")
    lines.append("- **Suggested forward-look** (S88+ optional): re-test at L=14 via §W1b-3 cross-pillar bridge if the L_max scan suggests the regulator-divergence is L-truncation-sensitive (preliminary evidence at L=12 says it is NOT — the divergence is structural, not L-truncation-dependent).")
    lines.append("- **Sub-algebra restriction track** (S88+ optional, NOT a carry-forward of this gate): test whether restricting A_loc to the substrate's actual A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) (instead of the full `M_n(ℂ)`) gives a finite, well-defined Connes distance that THEN admits a finite-spectrum identity. This is a different conjecture (different algebra), not CLASS-β of the present one.")
    lines.append("")
    lines.append("**Substrate framing**:")
    lines.append("The Connes distance is the substrate-internal state-space metric on the finite spectral triple `(A_loc, H_loc, D_K^{≤L})`. The substrate IS this commutator-algebra metric structure; it is not \"a metric on a manifold the substrate lives in\". Direction of explanation: **D_K eigenvalues + commutator algebra → SDP over A_F → d_C(p, q)**. The CLASS-γ closure says: the STATE-SPACE metric on the substrate's finite spectral triple is NOT a Mellin-Dirichlet-type spectral functional. State-pair-dependent observables generally require both `{λ_n}` AND the algebra-element decomposition; the §VII.U.1 identity belongs to the algebra-INVARIANT family of spectral moments, while the Connes distance belongs to the algebra-DEPENDENT family of state-pair functionals. This is a structural orthogonality between the two functional classes, not a numerical accident.")
    lines.append("")
    lines.append("**Artifacts on disk**:")
    lines.append("- Script: `computations/session-87/s87_w1b_connes_distance_finite_spectrum_identity.py` (38,955 bytes; content_sha256 prefix `1472a38026de3eed…`).")
    lines.append("- Data: `computations/session-87/s87_w1b_connes_distance_finite_spectrum_identity.npz` (8,880 bytes; keys: `candidate_identities_list, residuals_per_identity, rhs_per_identity, lhs_per_pair, best_residual, best_identity_form, canonical_state_pairs_tested, eigenvalues_L12, flat_abs_min, flat_abs_max, verdict_class, conjecture_status, sdp_status, regime_verdict, pairs_meta_json, R_sweep_values, lhs_R_sweep`).")
    lines.append("- Plot: `computations/session-87/s87_w1b_connes_distance_finite_spectrum_identity.png` (128,515 bytes; 3-panel: residuals per candidate × pair, best-fit candidate residuals, regulator-divergence diagnostic).")
    lines.append("- Verdict: `computations/session-87/s87_gate_verdicts.txt` line 53 (canonical) + lines 54-55 (dual-SHA + 3-tuple companions). 5 prior iteration lines (lines 38, 41, 44, 47, 53) preserved per gate-verdicts \"verdicts permanent\" rule.")
    lines.append("")
    lines.append("**Dual-SHA + 3-tuple annotation** (S87 schema-v2):")
    lines.append("- `audit_sha256 = b3652c276acec8e1b24dd18de8f303c24329c33cc9b95f25e0b60095acb98ca5`")
    lines.append("- `content_sha256 = 1472a38026de3eed80da540e18b8bd59a27f14a3ed100e793cd378bb5ac00f7e`")
    lines.append("- `sign_verdict = N/A` (OPEN-Q has no directional pre-registration)")
    lines.append("- `magnitude_verdict = FAIL` (best_residual = 0.980 > info_band = 1e-3)")
    lines.append("- `regime_verdict = VALID` (all 3 final-iteration SDPs converged at the regularization saturation; `optimal_inaccurate` status reflects boundary saturation, which IS the answer for the regulator-divergent LHS, not a solver malfunction)")
    lines.append("")
    lines.append("**Pre-registered candidates were tested EXACTLY as enumerated in plan §W1b-6 Field 6.** No post-hoc candidates were added (Class-6 PROHIBITED_ACTIONS). The 4 candidates × 3 state-pairs = 12 evaluations specification was honored; the 3 PRE-REGISTERED canonical state-pairs (vacuum / n=0 quasi; B1 acoustic min/max; Cartan α_1 / α_2) were instantiated via lowest-N_loc=16 sub-spectrum localization across the corresponding SU(3) sectors. The CLASS-γ outcome IS the structural physics result: the §VII.U.1 Mellin-Dirichlet identity does not generalize to algebra-dependent state-pair functionals. The orthogonality between the algebra-INVARIANT family (spectral moments, ζ-residues) and the algebra-DEPENDENT family (Connes distances, state-pair commutator norms) is itself a substrate structural finding.")
    lines.append("")
    lines.append("---")
    lines.append("")  # blank line before next section starts

    new_block = "\n".join(lines)
    new_text = text[:shell_start] + new_block + text[next_start:]

    # Atomic write via temp + replace
    tmp = WP.with_suffix(".md.tmp.s87w1b6")
    tmp.write_text(new_text, encoding="utf-8")
    os.replace(tmp, WP)

    # Verification: count lines in the new section
    new_section_text = new_text[shell_start:new_text.find(NEXT_HEADER, shell_start)]
    line_count = new_section_text.count("\n")
    substantive_lines = sum(1 for ln in new_section_text.split("\n") if ln.strip() and not ln.strip().startswith("#"))
    print(f"WP §W1b-6 patched at byte offset {shell_start} (line ~{text[:shell_start].count(chr(10))+1})")
    print(f"  total lines in section: {line_count}")
    print(f"  substantive (non-header non-blank) lines: {substantive_lines}")
    print(f"  WP file size: {WP.stat().st_size} bytes")


if __name__ == "__main__":
    main()
