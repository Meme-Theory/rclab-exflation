# Feynman-Theorist Agent Memory

Path integral, QED/QFT, renormalization, Feynman diagrams, "shut up and calculate." 14 papers in `/researchers/Feynman/`.

## Memory Index
- [feynman_test_and_constraints.md](feynman_test_and_constraints.md) -- Scorecard (7 steps), constraint walls, structural results, forward program, Ricci gauge, library gaps
- [session_results.md](session_results.md) -- Per-session gate verdicts (S40-S84), amplitudes, alpha_s paper record, data file inventory
- [critical_lessons.md](critical_lessons.md) -- User directives, computation error patterns, compressed session timeline S16-S84
- [instanton_1loop_W3O.md](instanton_1loop_W3O.md) -- S79 P3-B: Einstein W3-O tree+exp gives 13 OOM cushion; proper 1-loop (C_N*S^8) gives 7 OOM. Rule for instanton Gamma formulas
- [modulus_kinetic_a4_order_separation.md](modulus_kinetic_a4_order_separation.md) -- S116-W4: G_DeWitt=5 leading modulus kinetic coeff DERIVED + path-integral measure-confirmed rel=0; a4 order-split (Layer A/B/C); K_total=7.07 retired (order-mixing); operator-coeff vs numerical-dominance distinction

## Current State Summary

**Feynman Test**: Steps 1-6 substantively DONE. Step 7 (data) mixed: FIRAS PASS, w=-1 PASS, sin^2 FAIL, n_s FAIL, S83 CC7-UV PASS, S84 DYNAMICS-DRESSING FAIL (confirmation-of-wall).

**Paradigm**: Transit physics (compound nucleus dissolution), not equilibrium. Ordered Veil = integrable GGE relic, never thermalizes.

**Walls**: W4 (spectral action monotone, 28D), W_Josephson (fabric F monotone), W_integ_Josephson (R-G preserved), W_J_Majorana (CP shield from [J,D_K]=0). **27 equilibrium closures COMPLETE.**

**Open**: Zeta-regularized one-loop Gamma[tau] from existing eigenvalue data. Heat kernel at finite density (Comp A). KK graviton mass (Comp B).

**Post-Transit EFT (S55)**: 8-mode Lagrangian with V_kl, full Feynman rules. UV-complete in d=0+1 (256 states). All operators marginal. Optical theorem PASS (1.1e-15).

**Recent (S83-S84)**: CC7-UV-DECAY n=2 exact via 3PI-NLO matching ansatz (rule: check log-contamination from Feynman-parameter endpoint singularities). DYNAMICS-DRESSING 6 channels exhaust dynamics-sub-surface as A_s rescue (F_supp_max=1.0438 < 1.10).

**Key Numbers**: |M|_QP=0.02273 M_KK (S52), |M|_EFT=0.0799 M_KK (S55), Z=74731 (S42), w_0=-1+O(10^{-29}), eta=3.4e-9 (0.7 OOM off), d/Delta=42 (lattice pairing collapse), n_s=0.501 FAIL (14x overshoot). alpha_s = n_s^2 - 1 paper drafted (5 robustness proofs, 6.1 sigma tension with Planck).

Notes:
- Agent threads always have their cwd reset between bash calls, as a result please only use absolute file paths.
- In your final response, share file paths (always absolute, never relative) that are relevant to the task. Include code snippets only when the exact text is load-bearing (e.g., a bug you found, a function signature the caller asked for) -- do not recap code you merely read.
- For clear communication with the user the assistant MUST avoid using emojis.
- Do not use a colon before tool calls. Text like "Let me read the file:" followed by a read tool call should just be "Let me read the file." with a period.
- Do NOT Write report/summary/findings/analysis .md files. Return findings directly as your final assistant message -- the parent agent reads your text output, not files you create.
