---
name: repro-bundle-honest-manifest
description: One-command reproducer-bundle gate (S96 W8-5) — _shared/-resident script path handling, honest provenance partition, plan-SHA-drift runtime resolution
metadata:
  type: feedback
---

Building a "one-command reproducer + locked env manifest" COMPUTE-class gate that recomputes the capstone's headline numbers from canonical_constants.py + the L_max cache.

**Why:** S96-CONSOL-REPRO-BUNDLE (W8-5) — the report asked for a "minimal frozen end-to-end reproducer" + "standard locked environment manifest". The gate IS the reproducer AND emits the verdict.

**How to apply:**

1. **`_shared/`-resident producing-script path handling.** When `producing_script` lives in `computations/_shared/` (not `computations/session-N/`), the sibling template's `SESSION_DIR=parent; COMPUTATIONS_DIR=parent.parent` resolves DIFFERENTLY: `SHARED_DIR=parent`, `COMPUTATIONS_DIR=parent.parent`. Outputs (npz/png/verdict) still go to `computations/session-N/` — anchor `OUT_DIR = COMPUTATIONS_DIR / "session-96"` explicitly. The verdict file is `OUT_DIR / "s96_gate_verdicts.txt"` (canonical per gate-verdicts.md), NOT `_shared/`.

2. **Honest provenance partition (the load-bearing discipline).** Not every "headline" is a direct importable float pin. Classify each: RESOLVED-CANONICAL (direct `canonical_constants` float) / RESOLVED-GATE-REGISTER (the value is a gate output or Atlas-D04 register row, e.g. Ω_DM h²=0.1200 from LEGGETT-MOMENT-70, ρ_vac/ρ_obs=1.032 from DILUTION-CC-66 — importable COMPANION exists: Mass_LeggettDM_over_Delta_BCS=11.97, CC_OOM=115.5) / STRUCTURAL (identity, e.g. σ/m=0 N_Fock=1, no pin) / BAND-VALUED (e.g. m_H 127.5-131.8 GeV Aitken-Gaussian — the band IS the reproducible object) / UNRESOLVED. **Refuse to fabricate a clean RESOLVED row over a non-importable value** (task directive + substrate-first-canonical-sourcing.md). The partition counts go in the companion row.

3. **Verdict = INFO (not PASS) when band-valued/register-sourced rows exist** even at 12/12-within-precision: that is the plan's INFO_meaning, not a failure. FAIL is reserved for `n_unresolved>0` OR a within-precision miss. PASS only if ALL rows are clean direct-canonical.

4. **Plan-SHA-drift → resolve at runtime (substrate-first-canonical-sourcing.md §(ii.B)).** canonical_constants.py is frequently in the session modified-files set, so its plan-pinned input SHA goes stale. Compute the SHA at runtime (live SHA feeds audit_sha256), flag the drift in BOTH the verdict convention tag (`...-CANON-SHA-DRIFT-RUNTIME-RESOLVED`) AND the env manifest (`[DRIFT-FROM-PLAN-PIN]`). NEVER hardcode the stale plan pin. The headline VALUES are unchanged by the drift (only other file lines changed) ⇒ no SOURCE-RECON value-drift.

5. **Cache re-touch is a reduction, not a re-diagonalization.** s84_spectrum_cache_L12_tau019.npz has ONE key `sector_evals` = {(p,q): {dim, level, abs_evals}} (90 sectors, 166896 eigenvalues w/ mult; (0,0) constant-mode floor dim=16, ⟨|λ|²⟩=0.795051). The block-diagonal G10 theorem makes re-diagonalization unnecessary — torch reduction with a numpy first-use cross-check (matched 0.0e+00) satisfies the GPU_path pin without any matrix ≥100×100.

6. **The ROCm-SDK stderr probe ("Ainulindale: Unknown command line argument …offload-arch.exe") is benign** — triggered by the SPACE in the project path during torch import. torch GPU still initializes True; ignore it. Script exits 0; verdict is data not exit-code (math-scripts.md).

Related: [[capstone-status-sync-gate]] (the sibling W8-1 status-sync gate), [[cross-layer-shared-input-covariance]] (the W3/hygiene covariance audit that sourced the LEGGETT/DILUTION layer tags).
