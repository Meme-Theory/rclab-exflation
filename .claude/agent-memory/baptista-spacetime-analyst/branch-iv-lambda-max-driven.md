---
name: branch-iv-lambda-max-driven
description: METHOD TRAP — branch-iv Zubarev moment rho_B=mean_Z/lambda_max-1 is lambda_max-DRIVEN, NOT bottom-K-driven; FB bottom-K saturation does NOT apply to its high-L tail. Plus the p+q shell-build technique (conj-CPT halving, Casimir-ordered lambda_max, stdout-buffering blind spot).
metadata:
  type: feedback
---

The branch-(iv) late-time w0 proxy `rho_B(L) = mean_Z(L)/lambda_max(L) - 1` (Zubarev occupation weight `w_Z=exp(-|lambda|^2/Lambda_Z^2)`, Lambda_Z=1; S85 W0-7 evaluator `rho_zubarev_from_sectors`) is **lambda_max-DRIVEN**, NOT bottom-K-driven.

**Why:** Adding a new p+q=L shell does TWO things, with OPPOSITE saturation behavior:
- `mean_Z` (numerator) is **FROZEN / FB-saturated** — the new shell's |lambda| >= ~4.5 are Zubarev-killed (`w_Z~exp(-20)~2e-9`); per-shell mean_Z shift collapses to ~1e-6 (e.g. L15->L16 shift 8.86e-07).
- `lambda_max` (denominator) **RUNS Weyl-linearly** — `dlambda_max/dL ~ 0.375`; the shell RAISES it (e.g. lambda_max 6.542827@L15 -> 6.917603@L16). lambda_max at each level is **Casimir-ordered**, set by the GT-pure (N,0)/(0,N) sector (largest C_2 at fixed p+q; C_2(16,0)=304/3 highest), NOT by the central mixed sectors. So `rho_B` moves almost entirely through the denominator.

**The trap (S117 W7-3 vs INV13-W1-3):** INV13 SET `rho_B(16) == rho_B(15)` EXACTLY (`rho16_eq_15=0.0`) by the **bottom-K Friedrich-Bar saturation** argument (the p+q=16 |lambda|_min ~ 4.5 >> the bottom-20 ceiling 0.845, so the shell cannot enter the bottom-K floor). That is VALID for the bottom-K observable but **STRUCTURALLY WRONG for rho_B** — bottom-K saturation is ORTHOGONAL to the lambda_max-driven moment shift (S116-W9's own stated orthogonality). Building the shell gave the genuine `rho_B(16)=-0.712635` (shift 0.016460 INV13 missed). **How to apply:** never assume FB bottom-K saturation freezes a lambda_max-driven (or any sup-norm-normalized) spectral moment at high L — only the bottom-edge / Zubarev-suppressed part saturates; the sup-norm edge keeps running. Build the shell (or bound lambda_max) explicitly. The decrement obeys `|d(L->L+1)| = mu*b/lambda_max^2 ~ 1/L^2` (mu=mean_Z frozen, b=dlambda_max/dL) — verified to residual 1.35e-07.

**p+q shell-build technique (s105/s116-W9/s117 route):**
- Conjugate-CPT symmetry `|lambda(p,q)| == |lambda(q,p)|` (machine-exact, conj_sentinel~3.5e-14) ⇒ build ONLY the upper-triangle (p>=q) sectors and mirror the conjugates — HALVES the cost vs a full-triangle build. Build a live (0,N) GT sentinel to certify the mirror at the new level.
- GT-pure (N,0)/(0,N) via `irrep_symmetric_power_gt` (bosonic-ladder, never forms 3^N) is sub-second; the cost is the mixed-sector `get_irrep` Casimir-projection recursion (central (k,k) ~ minutes; p+q=16 (8,8) ~272s, (9,7) ~286s; full p+q=16 upper-triangle ~1184s GPU). Use a resume cache + background run.
- **stdout blind spot:** plain `print()` redirected to a log BLOCK-BUFFERS (~8KB) and flushes only at process exit — a long background build shows an empty log mid-run (looks hung but isn't). Key the completion waiter on the **npz output file existence**, not a log marker; or run with `python -u` / `PYTHONUNBUFFERED=1` for live progress. Verify the process is alive via RAM (the central-sector build holds ~2GB).

Related: [[s80_w0_15_branch_shortfall]], [[s116-branch-iv-l15-fb-scope]]. Verdict values live in the canonical verdict file (`computations/s{N}_gate_verdicts.txt`), NOT here.
