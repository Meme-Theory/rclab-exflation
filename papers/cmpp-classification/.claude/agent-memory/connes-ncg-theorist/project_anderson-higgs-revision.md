---
name: Anderson-Higgs paper revision
description: Peer review fixes applied to papers/anderson-higgs/main.tex — spectral triple specified, proofs restructured, claims toned down
type: project
---

Paper at `papers/anderson-higgs/main.tex` revised 2026-03-20 per 7 peer review fixes:

1. **Spectral triple specified**: Added Definition 2 (almost-commutative spectral triple on SU(3)) with A = C^inf(SU(3)) x A_F, H_F = C^32, D = D_K x 1 + gamma_9 x D_F. Gauge group Inn(A_F). K_7 outer for commutative factor.
2. **Proofs restructured**: Three proofs -> two. Old Proof II (all-orders propagation) became Corollary 4 under Proof I. Old Proof III (categorical) became new Proof II, rewritten to NOT use [K_7, D_K]=0.
3. **Categorical proof genuinely independent**: Four-step argument using only (i) K_7 generates diffeo, (ii) diffeos are Aut(C^inf), (iii) commutative => Inn={id}, (iv) gauge from Inn(A_F).
4. **Novelty claims toned**: Removed "all-orders impossibility" as separate novelty. Stated novelty as "explicit worked example with computational verification."
5. **Clifford order language fixed**: "second-order Clifford" -> "first-order differential operator" vs "zeroth-order multiplication operators."
6. **Title changed**: "Anderson-Higgs Impossibility" -> "Ungaugeability of Kosmann Symmetries"
7. **D_phys remark added**: Remark 9 addresses 11.7% breaking, explains it doesn't enable gauging because K_7 is categorically outer regardless of commutant status.

**Why:** Paper overclaimed by not specifying the algebra (making result vacuous for commutative case) and presenting three proofs that were not truly independent.

**How to apply:** If paper is revisited, the two-proof structure and Definition 2 are the load-bearing changes. The almost-commutative spectral triple must always be stated explicitly.
