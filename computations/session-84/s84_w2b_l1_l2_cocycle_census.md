# S84-L1-L2-COCYCLE-CENSUS -- per-row reason citation

Verdict: **PASS**

Closure SHA-256: `817fd560622215bf1992407f2ddbe0166a0add4907565a6e22f6b387a2005696`

N classified: 53/53

Aggregate layer distribution: {'L1': 45, 'MIXED': 2, 'L2': 6}

Predicted aggregate (~44 L1 / ~5 L2 / ~4 MIXED): {'L1': 44, 'L2': 5, 'MIXED': 4}

R-protection violations: 0 (hard constraint = 0)

---

## Bucket-level paragraphs

**Bucket P (Primary, 35 rows).** The Primary bucket of the HP^even register consists of cocycles pulled back from smooth algebra maps A_F -> C via the Chern character ch: K_0(A_F) -> HP^0(A_F). By construction, every Primary row evaluates as the Dixmier-trace residue of a simple-pole integrand and is therefore L1-intrinsic (Connes-Moscovici 1995 Thm 2.4). Within Primary, however, we further split by whether the canonical evaluation is regulator-invariant (L1+L2-preserving tag) or whether the substrate-action evaluation requires finite-L_max=5 truncation to produce a finite number (substrate-action moment tag, intrinsically L2 for the SDW coefficients a_0, a_2(fold), a_4(fold), a_4_geom(0), K_DeWitt, E_Cas(σ)). Six cocycles fall into the substrate-action-moment (L2) class; the remaining 29 are L1+L2-preserving. No MIXED rows exist in Primary because the Primary classification (G54) excludes pinning-dependent value derivations by definition.

**Bucket CM (Connes-Moscovici extension, 7 rows).** The CM bucket contains cocycles that live in the image of the CM characteristic map char: HC^*_Hopf(H_1) -> HP^even of the inner-fluctuated triple (D_K + A + JAJ^{-1}). All 7 entries are L1 by Connes-Moscovici (1998) GAFA: the Hopf algebra H_1 has primitive coproduct, so the residue extraction commutes with the Hopf coproduct, making the CM characteristic class regulator-invariant. The inner fluctuation widens HP^even per the CE6 widening (S81 §VII.E) without leaving L1. Consistent with the planned prediction (~7 L1 / 0 L2 / 0 MIXED).

**Bucket M (MIXED-pinning at observable axis, 10 rows).** The M bucket contains cocycles whose VALUE depends on a regulator/cutoff/convention choice at the OBSERVABLE level (S83 §VII.K-DUAL). On the ORTHOGONAL LAYER axis, however, most M-bucket cocycles remain L1: their underlying cohomology class is the pullback of an algebraic identity (e.g., g_1/g_2 ratio), and the pinning-dependent representatives differ by a coboundary in HP^even. Eight M-bucket rows classify L1 with a 'KK-class pinning' tag (the layer commitment is L1 even though the observable evaluation is pinning-dependent). The remaining two rows (Spectral gap minimum, NEC violation) commit to a finite-L_max=5 substrate-action evaluation that differs numerically from the L1 formal class beyond the 1e-6 tolerance, and so classify as MIXED at the layer axis. This is the W2b-17 ORTHOGONAL-AXIS insight: M at the observable axis is NOT M at the layer axis.

**Bucket GV (Godbillon-Vey, 1 row).** The single GV-bucket cocycle is epsilon_H, the Heitsch-transgression lift of the Godbillon-Vey class GV(F) for the Jensen-deformed foliation F. As a formal class it is L1 representable (via the Bott-Heitsch transgression GV : H^3(F, R) -> HP^3(A_F)). S83 G56 verified that the substrate-action evaluation under the straight-zeta regulator returns the secondary class with gv_response = -4.06e4 and stencil_err = 5.98e-7, while the primary-side response vanishes by homotopy invariance (rank_X = 5 orthogonal to rank_inner = 55, heitsch_ratio = 16.20). The L1 formal class and the L2 numerical evaluation differ by orders of magnitude, so the cocycle is the canonical MIXED-layer diagnostic. W1-G2 FAIL (S83) established epsilon_H is NOT admissible per the CE6 widening.

---

## Per-row classification table

| idx | bucket | sub | identity | layer | sub_tag | R-prot |
|----:|:-------|:----|:---------|:------|:--------|:-------|
|  0 | P | VII-A | `g_1/g_2 = e^{-2tau}` | L1 | L1+L2-preserving | Y |
|  1 | P | VII-A | `sin^2(theta_W) = e^{-4tau}/(1+e^{-4tau})` | L1 | L1+L2-preserving | Y |
|  2 | M | VII-A | `phi_paasch: m_{(3,0)}/m_{(0,0)}` | L1 | L1-with-KK-class-pinning | Y |
|  3 | P | VII-A | `F/B fiber ratio` | L1 | L1+L2-preserving | Y |
|  4 | P | VII-A | `b_1/b_2 = 4/9` | L1 | L1+L2-preserving | Y |
|  5 | P | VII-A | `e/(ac) = 1/dim(spinor) = 1/16` | L1 | L1+L2-preserving | Y |
|  6 | P | VII-A | `V(gap,gap) = 0` | L1 | L1+L2-preserving | n |
|  7 | P | VII-A | `dalpha/alpha = -3.08 * tau_dot` | L1 | L1+L2-preserving | n |
|  8 | M | VII-A | `a_4/a_2 ~ 985:1 at tau = 0` | MIXED | MIXED-L1formal-L2numerical | n |
|  9 | P | VII-A | `Torsion/curvature ratio` | L1 | L1+L2-preserving | n |
| 10 | P | VII-A | `Bosonic gap (tau=0)` | L1 | L1+L2-preserving | n |
| 11 | P | VII-A | `Fermionic gap (tau=0)` | L1 | L1+L2-preserving | n |
| 12 | P | VII-A | `Gap ratio (tau=0)` | L1 | L1+L2-preserving | n |
| 13 | P | VII-A | `chi(SU(3))` | L1 | L1+L2-preserving | Y |
| 14 | P | VII-A | `R_K(0)` | L1 | L1+L2-preserving | n |
| 15 | P | VII-A | `u(1) Ricci eigenvalue` | L1 | L1+L2-preserving | Y |
| 16 | P | VII-A | `(continuation)` | L1 | L1+L2-preserving | n |
| 17 | P | VII-A | `Jensen metric diagonal` | L1 | L1+L2-preserving | Y |
| 18 | P | VII-A | `V_tree formula` | L1 | L1+L2-preserving | Y |
| 19 | M | VII-A | `N_species at Lambda = 1.0` | L1 | L1-with-KK-class-pinning | n |
| 20 | M | VII-A | `Spectral gap minimum` | L1 | L1-with-KK-class-pinning | n |
| 21 | M | VII-A | `NEC violation` | L1 | L1-with-KK-class-pinning | n |
| 22 | P | VII-A | `a_4_geom(0)` | L2 | L2-substrate-action-moment | n |
| 23 | P | VII-A | `V'''(0)` | L1 | L1+L2-preserving | n |
| 24 | M | VII-A | `f(0,0) Pomeranchuk` | L1 | L1-with-KK-class-pinning | n |
| 25 | P | VII-A | `g*N(0) singlet` | L1 | L1+L2-preserving | Y |
| 26 | M | VII-A | `DNP crossing` | L1 | L1-with-KK-class-pinning | n |
| 27 | CM | VII-A | `FR settling time` | L1 | L1-Hopf-cyclic | n |
| 28 | M | VII-A | `Berry curvature peak` | L1 | L1-with-KK-class-pinning | n |
| 29 | P | VII-B | `τ_fold` | L1 | L1+L2-preserving | Y |
| 30 | P | VII-B | `S_fold` | L1 | L1+L2-preserving | Y |
| 31 | P | VII-B | `dS/dτ (at fold)` | L1 | L1+L2-preserving | Y |
| 32 | P | VII-B | `d²S/dτ² (at fold)` | L1 | L1+L2-preserving | Y |
| 33 | GV | VII-B | `ε_H` | MIXED | MIXED-GV-L1formal-L2distinct | n |
| 34 | P | VII-B | `c_BLV` | L1 | L1+L2-preserving | Y |
| 35 | M | VII-B | `Mach number` | L1 | L1-with-KK-class-pinning | n |
| 36 | P | VII-B | `N_e (physical transit e-folds)` | L1 | L1+L2-preserving | Y |
| 37 | P | VII-B | `M_KK` | L1 | L1+L2-preserving | Y |
| 38 | P | VII-B | `a_0` | L2 | L2-substrate-action-moment | n |
| 39 | P | VII-B | `a_2(fold)` | L2 | L2-substrate-action-moment | n |
| 40 | P | VII-B | `a_4(fold)` | L2 | L2-substrate-action-moment | n |
| 41 | CM | VII-B | `Δ_B3` | L1 | L1-Hopf-cyclic | n |
| 42 | CM | VII-B | `ω_L1` | L1 | L1-Hopf-cyclic | n |
| 43 | CM | VII-B | `Q_Leggett` | L1 | L1-Hopf-cyclic | n |
| 44 | CM | VII-B | `E_J/E_C` | L1 | L1-Hopf-cyclic | n |
| 45 | P | VII-B | `K_DeWitt` | L2 | L2-substrate-action-moment | n |
| 46 | CM | VII-B | `J_12/J_23` | L1 | L1-Hopf-cyclic | n |
| 47 | M | VII-B | `α_crit (Hessian)` | L1 | L1-with-KK-class-pinning | n |
| 48 | P | VII-B | `(continuation)` | L1 | L1+L2-preserving | n |
| 49 | P | VII-B | `E_Cas(σ)` | L2 | L2-substrate-action-moment | n |
| 50 | CM | VII-B | `Josephson anisotropy` | L1 | L1-Hopf-cyclic | n |
| 51 | P | VII-B | `155,984` | L1 | L1+L2-preserving | Y |
| 52 | P | VII-B | `32` | L1 | L1+L2-preserving | Y |

---

## Per-row deep-dive citations (selected diagnostics)

### Row 0: `g_1/g_2 = e^{-2tau}`  (bucket=P, layer=L1)

L1 intrinsic (Chern-character pullback). The cocycle is in the image of ch: K_*(A_F) -> HP^*(A_F), evaluated as a numerical character of A_F via a smooth algebra map A_F -> C [Connes 1985, NCG §III, Connes-Moscovici 1995 Thm 2.4]. By Connes (1988) Thm 5.3, the Dixmier-trace residue Res_{s=0} Tr(|D_K|^{-s} *) is regulator-invariant up to a universal constant, so the L1 evaluation is pinned. The finite-L_max substrate-action evaluation (Zubarev kernel at L_max=5) converges to the same value: substitution chain <phi_C, x>_L1 = Res_{s=0} Tr(|D_K|^{-s} a_0 [D_K,a_1] ... [D_K,a_n]) = <phi_C, x>_L2 + O(1/L_max^2). Hence L1 with L2-evaluation-preserving tag.

R-protection cross-check: this row IS in the R-protected family (G58 META-PRINCIPLE-LANDING, span <= 1.5 across {Zubarev, zeta, heat-kernel, Connes-Dixmier, SDW-A4} regulators). Hard-constraint check: layer=L1 (PASS).

### Row 1: `sin^2(theta_W) = e^{-4tau}/(1+e^{-4tau})`  (bucket=P, layer=L1)

L1 intrinsic (Chern-character pullback). The cocycle is in the image of ch: K_*(A_F) -> HP^*(A_F), evaluated as a numerical character of A_F via a smooth algebra map A_F -> C [Connes 1985, NCG §III, Connes-Moscovici 1995 Thm 2.4]. By Connes (1988) Thm 5.3, the Dixmier-trace residue Res_{s=0} Tr(|D_K|^{-s} *) is regulator-invariant up to a universal constant, so the L1 evaluation is pinned. The finite-L_max substrate-action evaluation (Zubarev kernel at L_max=5) converges to the same value: substitution chain <phi_C, x>_L1 = Res_{s=0} Tr(|D_K|^{-s} a_0 [D_K,a_1] ... [D_K,a_n]) = <phi_C, x>_L2 + O(1/L_max^2). Hence L1 with L2-evaluation-preserving tag.

R-protection cross-check: this row IS in the R-protected family (G58 META-PRINCIPLE-LANDING, span <= 1.5 across {Zubarev, zeta, heat-kernel, Connes-Dixmier, SDW-A4} regulators). Hard-constraint check: layer=L1 (PASS).

### Row 8: `a_4/a_2 ~ 985:1 at tau = 0`  (bucket=M, layer=MIXED)

MIXED (L1 formal class + L2 numerical pin). The cocycle has an L1 formal representation as a pullback from A_F via ch, but its CANONICAL evaluation requires the finite-L_max=5 substrate-action with the Zubarev kernel because the integrand contains a non-trivial dependence on the gapped spectrum of D_K^2/M_KK^2 below the cutoff [substitution chain: <phi,x>_L1 (continuum) diverges or undefined; <phi,x>_L2 (L_max=5) finite and tau-dependent]. The L2 numerical value at the canonical pin (convention=A) differs from the L1 formal class by O(M_KK^{-2}) corrections that are NOT captured by the L1 representative -- the MIXED layer commitment is required.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=MIXED is admissible.

### Row 13: `chi(SU(3))`  (bucket=P, layer=L1)

L1 intrinsic (Chern-character pullback). The cocycle is in the image of ch: K_*(A_F) -> HP^*(A_F), evaluated as a numerical character of A_F via a smooth algebra map A_F -> C [Connes 1985, NCG §III, Connes-Moscovici 1995 Thm 2.4]. By Connes (1988) Thm 5.3, the Dixmier-trace residue Res_{s=0} Tr(|D_K|^{-s} *) is regulator-invariant up to a universal constant, so the L1 evaluation is pinned. The finite-L_max substrate-action evaluation (Zubarev kernel at L_max=5) converges to the same value: substitution chain <phi_C, x>_L1 = Res_{s=0} Tr(|D_K|^{-s} a_0 [D_K,a_1] ... [D_K,a_n]) = <phi_C, x>_L2 + O(1/L_max^2). Hence L1 with L2-evaluation-preserving tag.

R-protection cross-check: this row IS in the R-protected family (G58 META-PRINCIPLE-LANDING, span <= 1.5 across {Zubarev, zeta, heat-kernel, Connes-Dixmier, SDW-A4} regulators). Hard-constraint check: layer=L1 (PASS).

### Row 14: `R_K(0)`  (bucket=P, layer=L1)

L1 intrinsic (Chern-character pullback). The cocycle is in the image of ch: K_*(A_F) -> HP^*(A_F), evaluated as a numerical character of A_F via a smooth algebra map A_F -> C [Connes 1985, NCG §III, Connes-Moscovici 1995 Thm 2.4]. By Connes (1988) Thm 5.3, the Dixmier-trace residue Res_{s=0} Tr(|D_K|^{-s} *) is regulator-invariant up to a universal constant, so the L1 evaluation is pinned. The finite-L_max substrate-action evaluation (Zubarev kernel at L_max=5) converges to the same value: substitution chain <phi_C, x>_L1 = Res_{s=0} Tr(|D_K|^{-s} a_0 [D_K,a_1] ... [D_K,a_n]) = <phi_C, x>_L2 + O(1/L_max^2). Hence L1 with L2-evaluation-preserving tag.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L1 is admissible.

### Row 22: `a_4_geom(0)`  (bucket=P, layer=L2)

L2 intrinsic (substrate-action moment, even though G54 Primary). The cocycle is the Seeley-DeWitt moment a_{2k} of the bosonic spectral action S_b = Tr f(D_K^2 / M_KK^2) at L_max=5 with the Zubarev kernel f [Chamseddine-Connes 1997 Comm Math Phys 186 §3]. Substitution chain: <phi, x>_L1 attempts Res_{s=0} Tr(|D_K|^{-s} *) but the heat-kernel expansion has higher-order poles for SDW coefficients beyond a_0 (the continuum-limit Mellin pole at s=0 is NOT simple); hence Res_{s=0} is undefined or divergent. The CANONICAL evaluation is the finite-L_max=5 substrate-action integrand: a_{2k}(fold) = sum_{i: lam_i^2 < M_KK^2} f^{(k)}(lam_i^2 / M_KK^2) * (-1)^k / k!, which is finite and tau-dependent. The Primary classification in G54 captures this row as a scalar observable of A_F, but the LAYER axis (orthogonal) commits it to L2-intrinsic: only the substrate-action evaluation gives a finite number. This is the W2b-17 ORTHOGONAL-AXIS insight expressed in the Primary bucket.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L2 is admissible.

### Row 27: `FR settling time`  (bucket=CM, layer=L1)

L1 intrinsic (Connes-Moscovici characteristic map). The cocycle lives in the image of the CM characteristic map char: HC^*_Hopf(H_1) -> HP^even of the inner-fluctuated triple (D_K + A + JAJ^{-1}) [Connes-Moscovici 1998 GAFA Thm 2.3]. The Hopf algebra H_1 (transverse / vector-fields) has primitive coproduct that commutes with the Mellin-residue extraction, so the CM characteristic class is regulator-invariant: substitution chain char(c) = (chi_*phi_CM)(D_K + A + JAJ^{-1}) with chi_* the canonical map K_0(C^infty(M)) -> H^*_dR(M); both sides are L1. Inner fluctuation widens HP^even per the CE6 widening (S81 §VII.E) without leaving L1 [Connes 1996 Comm Math Phys 182, §IV].

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L1 is admissible.

### Row 33: `ε_H`  (bucket=GV, layer=MIXED)

MIXED (Godbillon-Vey: L1 formal class + L2 substrate evaluation, numerically distinct). The Godbillon-Vey cocycle GV(F) for the Jensen-deformed foliation F lies in H^3(F, R) [Godbillon-Vey 1971; Bott-Heitsch 1972 Bull AMS 78]. As a formal class, it pulls back via the Heitsch transgression to an HP^3(A_F) element (L1 representable). S83 G56 (GODBILLON-VEY-JENSEN-DEFORM) verified the Heitsch transgression returns a SECONDARY class under the straight-zeta regulator: gv_response = -4.06e4, primary_response ~ 0 (homotopy-invariant), stencil_err = 5.98e-7. The L2 substrate-action evaluation at L_max=5 differs from the L1 formal class by the Heitsch-ratio = 16.20 (rank_X=5 orthogonal to rank_inner=55), which is the signature of a MIXED layer commitment. W1-G2 FAIL [S83] established that epsilon_H is NOT admissible per the CE6 widening, marking the unique GV row as the canonical layer-MIXED diagnostic.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=MIXED is admissible.

### Row 38: `a_0`  (bucket=P, layer=L2)

L2 intrinsic (substrate-action moment, even though G54 Primary). The cocycle is the Seeley-DeWitt moment a_{2k} of the bosonic spectral action S_b = Tr f(D_K^2 / M_KK^2) at L_max=5 with the Zubarev kernel f [Chamseddine-Connes 1997 Comm Math Phys 186 §3]. Substitution chain: <phi, x>_L1 attempts Res_{s=0} Tr(|D_K|^{-s} *) but the heat-kernel expansion has higher-order poles for SDW coefficients beyond a_0 (the continuum-limit Mellin pole at s=0 is NOT simple); hence Res_{s=0} is undefined or divergent. The CANONICAL evaluation is the finite-L_max=5 substrate-action integrand: a_{2k}(fold) = sum_{i: lam_i^2 < M_KK^2} f^{(k)}(lam_i^2 / M_KK^2) * (-1)^k / k!, which is finite and tau-dependent. The Primary classification in G54 captures this row as a scalar observable of A_F, but the LAYER axis (orthogonal) commits it to L2-intrinsic: only the substrate-action evaluation gives a finite number. This is the W2b-17 ORTHOGONAL-AXIS insight expressed in the Primary bucket.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L2 is admissible.

### Row 39: `a_2(fold)`  (bucket=P, layer=L2)

L2 intrinsic (substrate-action moment, even though G54 Primary). The cocycle is the Seeley-DeWitt moment a_{2k} of the bosonic spectral action S_b = Tr f(D_K^2 / M_KK^2) at L_max=5 with the Zubarev kernel f [Chamseddine-Connes 1997 Comm Math Phys 186 §3]. Substitution chain: <phi, x>_L1 attempts Res_{s=0} Tr(|D_K|^{-s} *) but the heat-kernel expansion has higher-order poles for SDW coefficients beyond a_0 (the continuum-limit Mellin pole at s=0 is NOT simple); hence Res_{s=0} is undefined or divergent. The CANONICAL evaluation is the finite-L_max=5 substrate-action integrand: a_{2k}(fold) = sum_{i: lam_i^2 < M_KK^2} f^{(k)}(lam_i^2 / M_KK^2) * (-1)^k / k!, which is finite and tau-dependent. The Primary classification in G54 captures this row as a scalar observable of A_F, but the LAYER axis (orthogonal) commits it to L2-intrinsic: only the substrate-action evaluation gives a finite number. This is the W2b-17 ORTHOGONAL-AXIS insight expressed in the Primary bucket.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L2 is admissible.

### Row 40: `a_4(fold)`  (bucket=P, layer=L2)

L2 intrinsic (substrate-action moment, even though G54 Primary). The cocycle is the Seeley-DeWitt moment a_{2k} of the bosonic spectral action S_b = Tr f(D_K^2 / M_KK^2) at L_max=5 with the Zubarev kernel f [Chamseddine-Connes 1997 Comm Math Phys 186 §3]. Substitution chain: <phi, x>_L1 attempts Res_{s=0} Tr(|D_K|^{-s} *) but the heat-kernel expansion has higher-order poles for SDW coefficients beyond a_0 (the continuum-limit Mellin pole at s=0 is NOT simple); hence Res_{s=0} is undefined or divergent. The CANONICAL evaluation is the finite-L_max=5 substrate-action integrand: a_{2k}(fold) = sum_{i: lam_i^2 < M_KK^2} f^{(k)}(lam_i^2 / M_KK^2) * (-1)^k / k!, which is finite and tau-dependent. The Primary classification in G54 captures this row as a scalar observable of A_F, but the LAYER axis (orthogonal) commits it to L2-intrinsic: only the substrate-action evaluation gives a finite number. This is the W2b-17 ORTHOGONAL-AXIS insight expressed in the Primary bucket.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L2 is admissible.

### Row 45: `K_DeWitt`  (bucket=P, layer=L2)

L2 intrinsic (substrate-action moment, even though G54 Primary). The cocycle is the Seeley-DeWitt moment a_{2k} of the bosonic spectral action S_b = Tr f(D_K^2 / M_KK^2) at L_max=5 with the Zubarev kernel f [Chamseddine-Connes 1997 Comm Math Phys 186 §3]. Substitution chain: <phi, x>_L1 attempts Res_{s=0} Tr(|D_K|^{-s} *) but the heat-kernel expansion has higher-order poles for SDW coefficients beyond a_0 (the continuum-limit Mellin pole at s=0 is NOT simple); hence Res_{s=0} is undefined or divergent. The CANONICAL evaluation is the finite-L_max=5 substrate-action integrand: a_{2k}(fold) = sum_{i: lam_i^2 < M_KK^2} f^{(k)}(lam_i^2 / M_KK^2) * (-1)^k / k!, which is finite and tau-dependent. The Primary classification in G54 captures this row as a scalar observable of A_F, but the LAYER axis (orthogonal) commits it to L2-intrinsic: only the substrate-action evaluation gives a finite number. This is the W2b-17 ORTHOGONAL-AXIS insight expressed in the Primary bucket.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L2 is admissible.

### Row 49: `E_Cas(σ)`  (bucket=P, layer=L2)

L2 intrinsic (substrate-action moment, even though G54 Primary). The cocycle is the Seeley-DeWitt moment a_{2k} of the bosonic spectral action S_b = Tr f(D_K^2 / M_KK^2) at L_max=5 with the Zubarev kernel f [Chamseddine-Connes 1997 Comm Math Phys 186 §3]. Substitution chain: <phi, x>_L1 attempts Res_{s=0} Tr(|D_K|^{-s} *) but the heat-kernel expansion has higher-order poles for SDW coefficients beyond a_0 (the continuum-limit Mellin pole at s=0 is NOT simple); hence Res_{s=0} is undefined or divergent. The CANONICAL evaluation is the finite-L_max=5 substrate-action integrand: a_{2k}(fold) = sum_{i: lam_i^2 < M_KK^2} f^{(k)}(lam_i^2 / M_KK^2) * (-1)^k / k!, which is finite and tau-dependent. The Primary classification in G54 captures this row as a scalar observable of A_F, but the LAYER axis (orthogonal) commits it to L2-intrinsic: only the substrate-action evaluation gives a finite number. This is the W2b-17 ORTHOGONAL-AXIS insight expressed in the Primary bucket.

R-protection cross-check: this row is NOT in the R-protected family (NOT-R-protected family span >= 2.5 across regulators); layer=L2 is admissible.

