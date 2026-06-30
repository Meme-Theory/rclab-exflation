---
name: S84 DR3-RESPONSE-PROTOCOL
description: S84 W1b-9 PASS at registration -- R_842 locked, 6 lockouts A-F enforced, DR3 window opens 2026-04-23
type: project
---

S84 W1b-9 S84-DR3-RESPONSE-PROTOCOL -- PASS at registration (2026-04-19). Pre-commit framework response to DESI DR3 release.

**Why**: DR3 is first hard-decide observational event. Pre-commitment 4 days ahead of window open (2026-04-23) under binary rectangle-containment rule. R_918 discovered to be self-falsifier of its own prediction under branch (iv) W0-workshop promotion; migration to R_842 restores self-consistency without rectangle-resizing.

**How to apply**: On DR3 release 2026-04-23+, apply decision rule unchanged:
- DR3 central in R_842 = [-0.942, -0.742] x [-0.2, 0.2] -> PASS (branch (iv) corroborated)
- DR3 central outside R_842 -> FAIL (branch (iv) refuted; scorecard entry REQUIRED at §VII.M.scorecard.refutations linking content_sha256)
- DR3 central in margin or one component in/one out -> INFO, escalate to S84-DR3-CONTINGENCY-FINE-GRAINED (CF #44, 7-scenario sub-tree)

**Key numbers**:
- R_842 center: (w_0, w_a) = (-0.842, 0); half-widths (0.100, 0.200)
- Framework branch (iv): w_0_pred = -0.842454, w_a_pred = 0 (W0-workshop promotion)
- Offset from R_842 center: 0.000454 (0.454% of half-width) -- CC1 self-consistency PASS
- R_918 retrospective: w_0_pred + 0.85 = +0.007546 -> was OUTSIDE R_918 upper edge, self-falsifier
- DR3 projected cov: sigma_w0=0.046, sigma_wa=0.177, rho=-0.85
- cov matrix exact: [[0.002116, -0.0069207], [-0.0069207, 0.031329]]
- ~2.17-sigma central shift in w_0 needed to exit nearest R_842 edge

**Hard lockouts (A-F, NO exceptions)**:
- A: NO retreat to dual-pin
- B: NO scheme-shopping post-data
- C: NO rectangle-resizing
- D: NO w_a axis migration
- E: NO post-2026-04-23 redefinition of branch (iv) canonical w_0_pred
- F: NO post-2026-04-23 tau_fold relocation shifting w_0_pred

**SHA pins** (S84+ dual-SHA schema):
- content_sha256: 9cc7f47e3dedc978de50947914ebca073663c172fb9d5e45268bca4e74b79d9f
- audit_sha256:   e325e13e9dfe3b297a230fb510ef980c8fd184e5c99394708e75af0c04838e1f
- audit_flow_sha_payload (schedule): 2471488993b0dbca1c0e03d503608028138a53f1742891c6a10939be0789b876
- R_918 historical (retained verbatim): 7f23a7c603522a105dffe271584cc22d7a25c6c22a0cccf09fe180954af5c140

**Convention note**: canonical_constants.py currently pins w0_FW = -0.918 (S58 four-fold lock). branch-(iv) override w_0_pred = -0.842454 is W0-workshop promotion under test by SV1-SV4. Promotion of -0.842454 into canonical_constants.py is S85 carry-forward CONDITIONAL on PASS-at-DR3.

**Substrate framing** (mandatory): w_0 is NOT dark energy EOS parameter. It is substrate-effacement residual (0.03% leakage through substrate-to-observable coupling) projected onto CPL plane. Framework predicts (w_0, w_a) from substrate internal dynamics; DR3 rectangle is phenomenological projection of observational data for binary comparison.

**Artifacts**:
- computations/s84_w1b_dr3_response_protocol.py (driver)
- computations/s84_w1b_dr3_response_protocol.json (locked payload, 6.8 KB)
- computations/s84_w1b_dr3_response_protocol.npz (cov + corners + point)
- computations/s84_w1b_dr3_response_protocol.png (w_0, w_a plane with R_842 + R_918 + 1-sigma ellipse)
- sessions/permanent-results-registry.md §VII.M.1 (registry entry)
- computations/s84_gate_verdicts.txt (verdict line, dual-SHA)

**Downstream contingencies**:
- PASS-at-DR3: S85 promotes w0_FW=-0.842454 in canonical_constants.py; §VII.M.scorecard.corroborations entry
- FAIL-at-DR3: §VII.M.scorecard.refutations entry REQUIRED; branch reorganization per FAIL clause (alternative branch canonical OR tau_fold recalibration S85+ OR substrate-impedance recalibration) -- all require FRESH pre-registration
- INFO-at-DR3: CF #44 7-scenario sub-tree

**Race condition note**: concurrent W1-5 agent write overwrote the verdicts file during initial dispatch; verdict line was re-appended via Python append with exclusive write. Three S84 verdicts now present in s84_gate_verdicts.txt (MU-BC-GEOMETRIC, W0-REGULATOR-RESOLUTION-SV1, DR3-RESPONSE-PROTOCOL).
