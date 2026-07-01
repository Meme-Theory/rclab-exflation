---
name: project_s92_w9_4_chirality_fail_diagnostic
description: S91 W7 closed the two alternative-chirality candidate substrates as FAIL; §VII.AQ.OP-PROJ (tensor-product γ_5⊗γ_F) is the sole surviving valid chirality structure
metadata:
  type: project
---

S92 W9-4 (mack sole-writer) landed FAIL-diagnostic blocks at the two alternative-chirality candidate slots, documenting the S91 W7 substrate-physics verdicts.

**Substrate-physics result (S91 W7, confirmed from `sessions/archive/session-91/session-91-w7-workingpaper.md`):**
- **§VII.AT.OP-PROJ** (Bi-Chirality, γ_9' = γ_5 ⊕ γ_F direct-sum): S91 W7-2a FAIL `audit_sha256=9ae27d0ef191269b075f680b8f21ab73e27385d7afc6e3fb723d8adabdbaa874`. Axiom 5' chirality anticommutation `||{D_F, γ_9'}|| = 1.697` (NOT 0); KO-dim shifts 6 → **0** under (ε,ε',ε'')=(+1,+1,+1) — non-physical CPT class (S66 KO=0: J commutes with γ → CPT preserves chirality → non-physical for SM); bridge maps 1/3 PASS (only HKR-style; Connes-Karoubi FAIL because it depends on axiom 5'); Level-2 non-binding. 6/7 axioms PASS. Candidate (a) REJECTED.
- **§VII.AW.OP-PROJ** (SU(3)-Coloured, γ_9'' = γ_F^c): S91 W7-2b FAIL `audit_sha256=be8006d66cedb1cb2b207f1faad0d8a1dadc4067bb8d1eff45c561a3f1e1755d`. Axiom 5'' anticommutation `||{D_F, γ_9''}|| = 3.274` (NOT 0); KO-dim stays **6** (CM-2008 §11 shift to 2 mod 8 NOT realized at colour-signs (+1,-1,+1); ε''=-1); bridge maps 1/3 PASS; Level-2 non-binding. 6/7 axioms PASS. Candidate (b) REJECTED at this colour-signs choice.

**Why durable:** these two slots are STAGE-0-CANDIDATE RETAINED with FAIL diagnostic — NO promotion path via candidate (a)/(b). The parent §VII.AQ.OP-PROJ (tensor-product γ_9 = γ_5 ⊗ γ_F, KO-dim=6 BDI, J γ_9 = -γ_9 J) is the substrate's SOLE valid chirality structure.

**How to apply:** if a future gate proposes promoting §VII.AT.OP-PROJ or §VII.AW.OP-PROJ, the axiom-5'/5'' anticommutation FAIL is the structural wall — it is a property of the substrate's canonical D_F, not a convention choice. S92 W9-2 (colour-signs sweep over the 6 non-trivial tuples) tests whether ANOTHER (s_r,s_g,s_b) tuple repairs §VII.AW; W9-1 (CCvS 2013 quadratic extension) tests whether the inner-fluctuation closes axiom-4 at §VII.AQ. Neither touches the axiom-5'/5'' chirality wall closed here.

Related: [[op-proj-slot-label-collision]].
