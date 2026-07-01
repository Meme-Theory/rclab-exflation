---
name: S71 Inter-Site Entanglement Results
description: INTER-SITE-ENTANGLE-71 gate INFO — S_vN=1.999 bits vs predicted 0.876, Josephson-dominated 4-state entanglement
type: project
---

## S71 INTER-SITE-ENTANGLE-71 Results

- Gate: **INFO**. |S_ent - S_pred|/S_pred = 1.282. In INFO band [0.20, 3.0].
- S_vN(BCS GS) = 1.999 bits (2-cell partial trace, dim_A = 37, exact diag dim = 120)
- S_predicted = 2*r_spatial^2/ln(2) = 0.876 bits (Gaussian 2-mode squeeze, r=0.551)
- Entanglement EXCEEDS prediction by factor 2.28

**Why:** The Gaussian two-mode squeeze formula assumes two modes. The actual system has 4 effective Schmidt states (eigenvalues ~0.25 each, K=3.99) because N_pair=2 on 2 cells in the Josephson-dominated regime (E_J/Delta=7.3) distributes pairs nearly uniformly across (n1=0, n1=1a, n1=1b, n1=2) sectors.

**How to apply:** The A_s Route B squeeze budget needs revision -- either use multi-mode squeeze formalism or recognize that the Josephson junction provides MORE entanglement than a simple two-mode squeeze. r_eff = 0.881 (inverted from S_vN) is the correct effective parameter for the squeeze budget.

**Key structural finding:** BCS pairing is IRRELEVANT to the entanglement -- bare (no pairing) gives S_vN = 2.000 bits, BCS gives 1.999. All entanglement is from Josephson tunneling. This is the transmon regime: pair number is not a good quantum number per cell (consistent with S61 Ginzburg FAIL).

- Files: `computations/s71_inter_site_entangle.{py,npz,png}`
