# Session 82 Synthesis: Level-2 Cartan Exclusion Theorem (K-theory / cyclic cohomology track)

**Date**: 2026-04-18
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Track**: K-theory + cyclic cohomology (Connes' thesis machinery)
**Source documents**:
- `sessions/archive/session-82/session-82-results-workingpaper.md` §V.C (W2-3 KASPAROV-ABELIAN-PROOF, L1436-1638), §VI.C (W3-3 DIM-H-PI-UNIVERSAL-EXCLUSION, L3636-3887)
- `sessions/archive/session-82/session-82-OOM.md` §IV.A walls #2-#3 (Cartan exclusion + R-family reflection)
- Agent memory: `.claude/agent-memory/connes-ncg-theorist/MEMORY.md`

**Authoritative gate verdicts** (not re-adjudicated):
- `S82-KASPAROV-ABELIAN-PROOF: PASS` — SHA `61d732378be18b95...`
- `S82-DIM-H-PI-UNIVERSAL-EXCLUSION: PASS` (12/12) — SHA `7a4e4f9f5ccff5f9...`

---

## I. Theorem statement

**Theorem (Level-2 Cartan Exclusion — K-theoretic form)**. *Let $G$ be any compact connected simple Lie group of rank $r \geq 1$, $T \cong U(1)^r$ a maximal torus, and let $(\mathcal{A}, \mathcal{H}, D)$ be the almost-commutative spectral triple $\mathcal{A} = C^\infty(M) \otimes \mathcal{A}_F$, $\mathcal{A}_F = C^*(G)$, produced by the Connes-Chamseddine-Marcolli ACM construction (CCM 2007 §1.17-1.20), with Kasparov-submersion factorization (Van den Dungen 2018, Main Theorem). Let $\mathcal{A}_B := C^*(T) \subset \mathcal{A}_F$ denote the Cartan subfactor. Then the Level-2 R-protection K-homology class*
$$
c_2(\mathcal{A}_B) \;\in\; K_0\!\left(C_0(M) \otimes \mathcal{A}_B\right) \qquad (1)
$$
*VANISHES. Equivalently: the within-sector averaging criterion $\dim \mathcal{H}_\pi \geq 2$ fails on every irreducible $*$-representation of $\mathcal{A}_B$.*

**Corollary (Universality)**. *The conclusion holds for the 12 tested representatives $\{SU(3), SU(4), SU(5), Sp(2), Sp(3), \mathrm{Spin}(5), \mathrm{Spin}(7), G_2, F_4, E_6, E_7, E_8\}$ across the Cartan-Killing classification, and by uniform structural reduction extends to the entire class of compact connected simple Lie groups (including all $D_n$, which were not in the sanity table but are covered by the G-agnostic proof of §II below).*

**Dimensional consistency**: $c_2$ is an element of a K-group (additive abelian group, integer-valued rank on generators). Vanishing is a statement about the zero element. No physical units attach to this equation — it is a statement in noncommutative topology.

**Status**: PROVEN (permanent wall) at the K-theoretic level under the named hypotheses. The base case (SU(3)) is W2-3 PASS; the universal extension (12/12) is W3-3 PASS.

---

## II. Proof (K-theory / cyclic cohomology track)

The proof has four steps: (a) reduction to abelian C$^*$-algebra; (b) Kasparov-product representation of $c_2$; (c) cyclic-cohomology vanishing on abelian factors; (d) Gelfand-universal extension. Each step is G-agnostic after (a).

### II.(a) Reduction to abelian C$^*$-algebra

**Step 1 (definition, Maximal torus theorem)**. Every compact connected Lie group $G$ contains a maximal torus $T$, and all maximal tori are conjugate. $T \cong U(1)^r$ where $r = \mathrm{rank}(G)$. (Adams 1969, Thm 4.21; Bröcker-tom Dieck 1985, Thm IV.1.6.)

**Step 2 (substitution)**. $T$ is a compact connected *abelian* Lie group. By the group C$^*$-algebra construction,
$$
\mathcal{A}_B \;=\; C^*(T) \;\cong\; C_0(\widehat{T}), \qquad \widehat{T} \cong \mathbb{Z}^r, \qquad (2)
$$
via Pontryagin duality, hence $\mathcal{A}_B$ is commutative.

**Step 3 (simplification — Gelfand-Naimark)**. Every commutative C$^*$-algebra is isomorphic to $C_0(X)$ for compact Hausdorff $X$. Setting $X := \widehat{T}$, every irreducible $*$-representation $\pi: C_0(X) \to \mathcal{B}(\mathcal{H}_\pi)$ factors through point evaluation:
$$
\pi(f) \;=\; f(x) \cdot \mathbf{1}_{\mathcal{H}_\pi}, \qquad x \in X. \qquad (3)
$$

**Step 4 (direction)**. Schur's lemma applied to (3): a scalar-action irreducible representation admits only the trivial invariant subspace, hence $\dim \mathcal{H}_\pi = 1$ for every irrep of $\mathcal{A}_B$. This is the REQUIRED input for steps (b)-(d) — the `dim H_π = 1` fact is UNIVERSAL over compact connected Lie groups via the chain $T \subset G \Rightarrow C^*(T)$ commutative $\Rightarrow$ all irreps 1D.

**Substitution-chain summary** for the direction claim:
- Def: $\mathcal{A}_B = C^*(T) \cong C_0(\widehat{T})$ commutative (eq. 2).
- Def: Gelfand irreps are point evaluations (eq. 3).
- Simplification: scalar action $\Rightarrow$ Schur $\Rightarrow$ $\dim \mathcal{H}_\pi = 1$.
- Direction: $\dim \mathcal{H}_\pi \geq 2$ FAILS on $\mathcal{A}_B$. This is the *unfavorable* direction — a non-trivial averaging channel would have produced an irrep of dimension $\geq 2$, but Gelfand forbids it.

### II.(b) Kasparov-product representation of $c_2$

Per Van den Dungen 2018 (Paper 01 Main Theorem, `researchers/Van-den-Dungen/01_2018_van_den_Dungen_Kasparov_Submersions.md` L82), for the submersion $\pi: M \times G \to M$ with compact fiber $G$, the Dirac operator $D$ on the total space factors as an unbounded Kasparov product:
$$
[D] \;=\; [D_F] \;\widehat{\otimes}_{C(M)}\; [D_M] \quad\in\quad KK\!\big(\,C(M) \otimes C^*(G),\; \mathbb{C}\,\big). \qquad (4)
$$

S61 extended this with the block-decomposition theorem (`A-TENSOR-61` PASS, block-diag cross-term 0.47% one-loop, exact at tree) over a branch decomposition $\mathfrak{g} = \bigoplus_B \mathfrak{b}_B$:
$$
[D_F] \;=\; \bigoplus_B\, [D_F|_B] \qquad \text{(KK-orthogonal decomposition).} \qquad (5)
$$

The Level-2 R-protection class is constructed as the per-branch Hochschild boundary of the regulator-asymmetry 2-cocycle:
$$
c_2(\mathcal{A}_B) \;:=\; \partial_{HH}\!\left(\frac{J^{SDW} \cdot J^{\zeta_4}}{(J^{\zeta_2})^2}\right) \;\in\; K_0\!\left(C_0(M) \otimes \mathcal{A}_B\right). \qquad (6)
$$

Here $J^{SDW}$, $J^{\zeta_k}$ are the Seeley-DeWitt-regulated and zeta-regulated Wodzicki-residue moment traces (regime of validity: both regulators defined on the same compactly-supported symbol class; cutoff $\Lambda$ common). The 2-cocycle $c_2$ lives in the bivariant KK-group of (4), restricted to the fiber factor $\mathcal{A}_B$. The cancellation mechanism is *within-sector averaging*: for $\pi$ with $\dim \mathcal{H}_\pi \geq 2$, the trace over the basis of $\mathcal{H}_\pi$ supplies a non-trivial averaging operator.

**KK-cycle factorization diagram**:

```
                            fiber-restriction
C(M) ⊗ C*(G) ────────────────────────────────────► C(M) ⊗ A_B
      │                                                  │
      │ [D] = [D_F] ⊗̂_{C(M)} [D_M]                       │ c_2 = ∂_HH(J^SDW·J^ζ_4/(J^ζ_2)²)
      ▼                                                  ▼
                                                   K_0(C(M) ⊗ A_B)
                                                         │
                                  ∃ rank-≥2 projection?  │ Gelfand (§II.c)
                                                         ▼
                                                      c_2 = 0
                                                   (VANISHES for A_B abelian)
```

**Step 5 (substitution)**. Under (5), $c_2$ decomposes as $c_2 = \bigoplus_B c_2(\mathcal{A}_B)$. For the Cartan branch $\mathcal{A}_B = C^*(T)$, the restricted class lives in
$$
c_2(C^*(T)) \;\in\; K_0(C_0(M) \otimes C_0(\widehat{T})) \;\cong\; K_0(C_0(M \times \widehat{T})). \qquad (7)
$$

**Regime of validity**: equation (7) holds under Kasparov-submersion regularity (Van den Dungen 2018 §3, spectral-gap condition on $D_F$). This is satisfied for the Jensen-deformed $D_F$ on SU(3) at all tested $\tau$ (S61 K-HOMOLOGY-STABILITY, Kato-Rellich bound $\alpha = 0.081 < 1$, deformation-invariant).

### II.(c) Cyclic-cohomology vanishing on abelian factors (Connes' thesis theorem)

**Step 6 (definition — Connes' HC for commutative C$^*$-algebras)**. For $A = C^\infty(X)$ smooth, Connes 1985 (IHES Pub. Math. 62, *Non-commutative differential geometry*, Theorem II.3.3) established:
$$
HC^n\!\left(C^\infty(X)\right) \;\cong\; \Omega^n(X)_{\mathrm{closed}} \;\oplus\; H^{n-2}_{dR}(X) \;\oplus\; H^{n-4}_{dR}(X) \;\oplus\; \cdots \qquad (8)
$$
with the cyclic-cohomology / de Rham-cohomology decomposition. For $X = \widehat{T} \cong \mathbb{Z}^r$ discrete, $\Omega^n(X) = 0$ for $n \geq 1$ (no smooth differential forms on a discrete set) and $H^k_{dR}(\mathbb{Z}^r) = 0$ for $k \geq 1$. Hence for all $n \geq 1$:
$$
HC^n\!\left(C_0(\mathbb{Z}^r)\right) \;=\; 0. \qquad (9)
$$

**Step 7 (substitution — K-theory via Chern character)**. Connes' Chern character pairs $K_0$ with $HC^{\mathrm{even}}$:
$$
\langle \cdot, \cdot \rangle: K_0(A) \times HC^{2k}(A) \;\longrightarrow\; \mathbb{C}, \qquad k \geq 0. \qquad (10)
$$
Level-2 protection requires a non-vanishing $k = 1$ cyclic 2-cocycle $\varphi \in HC^2(\mathcal{A}_B)$ such that $\langle c_2, \varphi \rangle \neq 0$. By (9), $HC^2(\mathcal{A}_B) = HC^2(C_0(\mathbb{Z}^r)) = 0$.

**Step 8 (simplification — K_0 structure is free-abelian on rank-1 classes)**. The K-theory of $C_0(\mathbb{Z}^r)$ is
$$
K_0(C_0(\mathbb{Z}^r)) \;=\; \bigoplus_{\chi \in \mathbb{Z}^r} \mathbb{Z}, \qquad K_1(C_0(\mathbb{Z}^r)) \;=\; 0, \qquad (11)
$$
generated by rank-1 character projections $e_\chi: f \mapsto f(\chi)$. Every $K_0$-generator is the class of a rank-1 virtual vector bundle; no rank-$\geq 2$ projection classes are generated purely by abelian data. This is the K-theoretic counterpart of the Gelfand observation (eq. 3).

**Step 9 (direction — Level-2 vanishing)**. The Level-2 class, if non-trivial, would have to pair non-trivially with some element of $HC^2(\mathcal{A}_B)$ through (10). Since $HC^2(\mathcal{A}_B) = 0$ by (9), no such pairing exists. Equivalently, every $c_2$ candidate is realized in a rank-1 projection subgroup of $K_0$ by (11), which cannot carry within-sector averaging ($\mathcal{H}_\pi = \mathbb{C}$, the trace over it is the identity). The class $c_2(\mathcal{A}_B)$ is therefore forced to the zero element:
$$
c_2(\mathcal{A}_B) \;=\; 0 \quad\in\quad K_0(C_0(M) \otimes \mathcal{A}_B). \qquad (12)
$$

**Substitution-chain summary** for the vanishing:
- Def: Level-2 cancellation requires pairing $\langle c_2, \varphi \rangle \neq 0$ with $\varphi \in HC^2(\mathcal{A}_B)$.
- Def: Connes 1985 Thm II.3.3 $\Rightarrow$ $HC^n(C_0(\widehat{T})) = 0$ for $n \geq 1$ (eq. 9).
- Simplification: no non-zero 2-cocycle exists on abelian $\mathcal{A}_B$ (pairing domain empty).
- Direction: no cancellation, $c_2 = 0$. "Vanishes" is the *unfavorable* direction for protection — a non-zero class would have rescued the cancellation; zero class means the scheme-regulator asymmetry is unaveraged.

### II.(d) Gelfand-universal extension (W3-3)

The argument of §II.(a)-(c) uses ONLY:
  (i) $\mathcal{A}_B$ commutative,
  (ii) Gelfand-Naimark (commutative C$^*$-algebra $\cong C_0(X)$),
  (iii) Connes' $HC^*$ computation on $C_0(X)$ abelian (eq. 9),
  (iv) Chern-character pairing (eq. 10).

None of (i)-(iv) invokes the rank $r = 2$ of SU(3), the structure constants of $\mathfrak{su}(3)$, or any specific feature of SU(3). The proof is **G-agnostic after the reduction to the maximal torus**.

**Step 10 (universal reduction)**. For any compact connected simple Lie group $G$, the maximal torus theorem guarantees a canonical abelian subfactor $C^*(T) \subset C^*(G)$. Hence §II.(a)-(c) applies verbatim, and $c_2(C^*(T)) = 0$ in every case.

**Empirical coverage**. The W3-3 sanity table (`s82_w3_3_dim_h_pi_universal.py`) enumerates 12 groups:

| Family | Groups in table | Rank range |
|:-------|:----------------|:-----------|
| $A_n$ | SU(3), SU(4), SU(5) | 2, 3, 4 |
| $B_n$ | Spin(5), Spin(7) | 2, 3 |
| $C_n$ | Sp(2), Sp(3) | 2, 3 |
| Exceptional | $G_2$, $F_4$, $E_6$, $E_7$, $E_8$ | 2, 4, 6, 7, 8 |
| **Total** | **12** | **$r \in \{2, 3, 4, 6, 7, 8\}$** |

All 12: `max_irrep_dim(C^*(T)) = 1`, `dim_obs_L2 = 0`, `L2 class = VANISHES`. Zero counterexamples.

**Scope note on $D_n$**: The sanity table does NOT include any $D_n$ (Spin(2n)) representative. The theorem's claim of Cartan-Killing-universality nevertheless applies: $D_n$'s maximal torus is abelian, Step 10 applies verbatim, $c_2(C^*(T_{D_n})) = 0$ by the same Gelfand reduction. The $D_n$ coverage is inferred from the G-agnostic proof, not from sanity-table enumeration. I recommend adding Spin(8) to an S83 verification pass for completeness — see §V below.

### II.(e) Connection to cyclic cohomology of $C^*(T)$ via Connes' thesis

The free-abelian K_0 structure in (11) is the K-theoretic image of a stronger cyclic-cohomological fact: for a torus $T^r = U(1)^r$, the Pontryagin dual $\widehat{T^r} = \mathbb{Z}^r$ is a discrete abelian group, and Connes' 1985 machinery gives
$$
HC^\bullet(C^*(T^r)) \;\cong\; H^\bullet_{\mathrm{dR}}(T^r) \;\oplus\; H^{\bullet - 2}_{\mathrm{dR}}(T^r) \;\oplus\; \cdots \qquad (13)
$$
where on the RHS $T^r$ appears because $\widehat{T^r}$ is Pontryagin-dual to the continuous torus and ordinary de Rham cohomology of the discrete group vanishes in positive degree. The SBI (Connes' periodicity) sequence degenerates on abelian $C^*$-algebras. All higher cyclic cohomology groups reduce to ordinary cohomology of the *dual*, which for $\mathbb{Z}^r$ gives only $HC^0 = \mathbb{Z}$ (the trace class). Level-2 is structurally outside this range.

---

## III. Consequences for the framework

### III.1 Closes the W0-2 CLT-INAPPLICABLE path universally

S80-W2C-L8-DRIFT returned `drift_u1(L=8) = 88.5390%` vs CLT band $[0.56, 0.76]$ — a FAIL-Sc2 outcome where the abelian branch drifts MORE than CLT predicts. Under the Level-2 Cartan Exclusion Theorem, this empirical finding is no longer a SU(3)-specific anomaly to be explained; it is the UNIVERSAL PREDICTION of K-theoretic Level-2 vanishing applied to the $\mathfrak{u}(1)$ Cartan branch of $\mathfrak{su}(3)$.

**Substitution-chain for the direction of the drift**:
- Def: CLT protection predicts $\mathrm{drift}(L) \to 0$ as $L \to \infty$ with $1/\sqrt{N}$ decay, conditional on a non-vanishing averaging channel (Level-2 protection).
- Def: Level-2 Cartan Exclusion $\Rightarrow$ $c_2(\mathcal{A}_B) = 0$ $\Rightarrow$ no averaging channel.
- Simplification: in the absence of averaging, regulator-scheme asymmetry *accumulates* with mode count, not cancels.
- Direction: $\mathrm{drift}(L)$ monotonically INCREASES with $L$ (observed: 73.67% at $L=4$, 83.75% at $L=6$, 88.54% at $L=8$). Confirmed direction.

The theorem is $L_{\max}$-invariant; the empirical drift is consistent with but not required by the K-track argument. The path closed by this theorem is "CLT-INAPPLICABLE-ON-CARTAN-ONLY" — it now closes for *every* compact connected simple $G$'s Cartan, not just SU(3)'s.

### III.2 Promotes the `dim H_π ≥ 2` criterion to a permanent universal NCG criterion

Before S82: `dim H_π ≥ 2` was a Lizzi workshop pre-theorem (S79 P4-B `CV-L2`), verified on SU(3) Cartan only. After S82: it is a structural theorem across the Cartan-Killing classification. Any framework extension to a new ambient group (SU(4), Spin(10), $E_6$ unification targets) inherits the exclusion automatically.

### III.3 Deformation-invariance under Jensen sweep

S61 K-HOMOLOGY-STABILITY (Kato-Rellich bound $\alpha = 0.081 < 1$): the Kasparov class is continuous in $\tau$ on the Jensen-deformation family. The vanishing of $c_2(C^*(T))$ is therefore invariant under $\tau \in [0, \tau_{\mathrm{fold}}]$. No rescue of Level-2 protection on Cartan branches is available via Jensen tuning.

### III.4 Reconciliation with Level-1 aggregate protection

S77-D3-R1-UNIVERSAL (Lizzi S77 §VI.2): Level-1 R-protection via simplicial cancellation is *universally protected* across SU(3), Sp(2), SU(4). The Level-2 Cartan Exclusion established here is the dual statement: Level-1 protected universally, Level-2 excluded universally on Cartan. Together, the pair carves out the surviving region precisely: **Level-2 protection survives only on non-abelian sub-branches**.

---

## IV. Scope of the exclusion

The theorem closes one region precisely; several NCG protection mechanisms remain viable. Listed by structural category.

### IV.(a) Non-abelian sector protection — OPEN

For a non-abelian $\mathcal{A}_{B'} \subset C^*(G)$ (e.g., the $\mathfrak{su}(2)$ branch of $\mathfrak{su}(3)$ in Baptista's decomposition $\mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2$, Baptista eq 3.58), irreducible representations with $\dim \mathcal{H}_\pi \geq 2$ exist. The matrix subalgebras $M_n(\mathbb{C}) \subset \mathcal{A}_{B'}$ generate rank-$n$ projection classes in $K_0(\mathcal{A}_{B'})$, distinct from $n \cdot [1]$. The 2-cocycle $c_2(\mathcal{A}_{B'})$ is NOT forced to zero by the Cartan argument. Whether it is non-zero and realizes Level-2 protection requires per-case computation. SU(3) $\mathfrak{su}(2)$ branch: W2-3 §V.C Section 4 argues non-vanishing; SU(4), SU(5) $\mathfrak{su}(k)$ sub-branches: OPEN CHANNELS (carry forward to S83).

### IV.(b) Higher-class (Level-3+) protection via $HC^{2k}$ cocycles for $k \geq 2$ — OPEN

The proof in §II uses only the $n = 2$ cyclic cohomology vanishing (eq. 9). The same Connes' thesis computation gives $HC^n = 0$ for all $n \geq 1$ on $C_0(\mathbb{Z}^r)$, so higher-class Cartan protection is ALSO excluded. However, on *non-abelian* branches, higher cyclic cohomology is generally non-trivial (e.g., $HC^\bullet(M_n(\mathbb{C}))$ is a polynomial ring on the Chern character). Level-3+ protection on non-abelian branches is structurally possible but uncomputed. OPEN.

### IV.(c) Non-simple Lie groups (products + abelian factors) — CLOSED UNIVERSALLY

Per §VI.C Section 6.1-6.2 of the source: reductive $G = (G_{ss} \times T') / \Gamma$ have $T_G = T_{G_{ss}} \times T'$ abelian, so the argument applies verbatim. Products $G_1 \times G_2$: maximal torus $T_1 \times T_2$ abelian. Pure abelian $G = A$: $C^*(A)$ already commutative, Level-2 vanishes trivially. All compact connected reductive Lie groups are covered by the same exclusion.

### IV.(d) Quantum-group deformations — NOT CLOSED

For a compact quantum group $G_q$ with Drinfeld-Jimbo deformation parameter $q \neq 1$, $C^*(G_q)$ is generally non-commutative *even when the classical limit $G$ is a torus*. Gelfand's theorem does not apply. The Cartan sub-object of $C^*(G_q)$ is no longer $C_0(\widehat{T})$ but a non-commutative quantum torus $C^*(\mathbb{Z}^r)_\theta$ with Rieffel deformation. Cyclic cohomology of the quantum torus is non-trivial ($HC^2 \neq 0$ at irrational $\theta$), so the argument BREAKS at Step 6. Level-2 protection in quantum-group NCG is an OPEN structural possibility; deserves an S83+ investigation if the framework contemplates a quantum-group ambient.

### IV.(e) Non-compact fibers — NOT CLOSED

The Kasparov-submersion factorization (eq. 4) requires compact-fiber spectral-gap conditions (Van den Dungen 2018 §3). For non-compact $G$, the factorization does not apply directly, and the theorem is silent. Non-compact Cartan subalgebras $\mathbb{R}^r$ still have rank-1 $K_0$ generators (Bott classes), but the framework's submersion structure is absent.

### IV.(f) Infinite-dimensional / loop groups — OUT OF SCOPE

Loop groups, gauge groups, and other infinite-dimensional examples fall outside Van den Dungen 2018 hypotheses. No claim made.

---

## V. Carry-Forward Computations

Every entry is a first-principles computation in the K-theory / cyclic-cohomology track. All are directly produced by open channels identified in §§II-IV or by structural gaps in the verification record. Substitution-chain references: all sign/direction claims in the expected-outcome rows trace to §II.(b)-(c) (the r-invariance of $HC^n(C_0(\mathbb{Z}^r)) = 0$ for $n \geq 1$, Connes 1985 Thm II.3.3) and to the mode-count substitution $N_{\mathrm{modes}}(L, r) = (2L+1)^r$ (verified Python: SU(3) T² at L=8 = 289 modes; Spin(8) T⁴ at L=8 = 83,521 modes).

### V.1 `S83-CARTAN-EXCL-D4-SPIN8-SANITY` — Spin(8) Cartan T⁴ verification

- **What**: Compute `drift_u1(L=4..8)` on the Cartan T⁴ subfactor of Spin(8) via the W3-3 sanity-table pipeline, adapted from SU(3) T² to the rank-4 abelian case. Output variable: `drift_cartan_spin8(L)` for L ∈ {4, 5, 6, 7, 8}; derived quantities: `max_irrep_dim(C*(T_Spin(8)))` (expected 1), `dim_obs_L2` (expected 0), Level-2 class verdict (expected VANISHES). Dimensional check: mode count $(2L+1)^4$ at L=8 is 83,521 (289× the SU(3) count) — GPU-mandatory per agent-memory rule "agents never use GPU by default."
- **Inputs**: (a) `computations/canonical_constants.py` for `tau_fold = 0.19`, `M_KK`, and GPU-path fixture (torch 2.9.1+rocm per `.claude/rules/math-scripts.md`). (b) `s82_w3_3_dim_h_pi_universal.py` as pipeline template — adapt the 12-group loop to include Spin(8) root data: simple roots $\alpha_1 = e_1 - e_2$, $\alpha_2 = e_2 - e_3$, $\alpha_3 = e_3 - e_4$, $\alpha_4 = e_3 + e_4$ (D₄ Cartan matrix). (c) S80-W2C L-scan protocol for `drift_u1(L)` observable.
- **Gate**: NEW gate `S83-CARTAN-EXCL-D4-SPIN8-SANITY` feeding the universality corollary of §I.
  - PASS (expected under theorem): `max_irrep_dim(C*(T_Spin(8))) = 1` AND `drift_cartan_spin8(L=8) ≥ 0.80` AND monotone in L. Closes the D_n gap in the 12-group table.
  - FAIL: `drift_cartan_spin8(L=8) ∈ [0.56, 0.76]` (CLT band) OR monotone-decreasing in L. Would falsify the Gelfand-universal extension and force re-examination of §II.(d).
  - INFO: `drift_cartan_spin8(L=8) ∈ (0.76, 0.80)` — boundary zone; not decisive but constrains universality bound.
- **Effort**: 4-6 hours, 1 agent session. GPU-accelerated torch.linalg eigvals on 83,521-mode sparse Laplacian block; fits 17.1 GB VRAM (AMD RX 9070 XT) with room.

### V.2 `S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER` — G₂ Cartan CLT falsifier

- **What**: Pre-registered falsifier for the universality claim. Compute `drift_cartan_G2(L)` for L ∈ {4, 5, 6, 7, 8} on the G₂ Cartan T² subfactor and test whether any rank-≥2 exceptional group escapes the Cartan exclusion. Output variable: `drift_cartan_G2(L)` with monotonicity table. Rationale: G₂ is the smallest exceptional (rank 2, dim 14); a PASS would force re-examination of whether exceptional root systems produce non-abelian projection classes even on their abelian Cartan (structurally impossible by Gelfand, but the empirical check closes the loop).
- **Inputs**: G₂ simple roots $\alpha_1$ (short), $\alpha_2$ (long) with Cartan matrix $\begin{pmatrix}2 & -1 \\ -3 & 2\end{pmatrix}$; canonical_constants `tau_fold` and `M_KK`; template script `s82_w3_3_dim_h_pi_universal.py`. CLT band reference $[0.56, 0.76]$ from W0-2 / S80-W2C documentation.
- **Gate**: NEW gate `S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER`.
  - PASS (would falsify universality): `drift_cartan_G2(L=8) ∈ [0.56, 0.76]` AND monotone-decreasing in L AND $\propto L^{-1/2}$ to within 15%.
  - FAIL (expected under theorem): `drift_cartan_G2(L=8) ≥ 0.85` AND monotone-increasing in L. Confirms exceptional-family Cartan exclusion.
  - INFO: any mixed signal (e.g., drift in band but non-monotone, or monotone but out of band).
- **Effort**: 1 agent session, ~1 day. Mode count $(2L+1)^2 = 289$ at L=8 — CPU-tractable via numpy.linalg with OMP_NUM_THREADS=8, or GPU for speed.

### V.3 `S83-CARTAN-EXCL-NONSIMPLE-COUNTERTEST` — non-simple G = SU(3) × U(1) counter-test

- **What**: User-specified concern per carry-forward patch: does the theorem EXTEND to non-simple G, specifically $G = SU(3) \times U(1)$ where the second factor is already abelian? Compute $c_2(C^*(T_G))$ via the two-factor Kasparov-product decomposition and verify whether the simple-connected assumption is doing any real work in §II, or whether the proof is purely a statement about abelian subfactors. Output: explicit decomposition $c_2(C^*(T_{SU(3) \times U(1)})) = c_2(C^*(T_{SU(3)})) \oplus c_2(C^*(U(1)))$ in $K_0$.
  - Substitution chain for the vanishing direction: (i) $T_G = T_{SU(3)} \times U(1)$ is still abelian (product of abelian ⇒ abelian). (ii) $C^*(T_G) \cong C_0(\widehat{T_{SU(3)}} \times \widehat{U(1)}) \cong C_0(\mathbb{Z}^2 \times \mathbb{Z}) = C_0(\mathbb{Z}^3)$. (iii) Connes' HC vanishing (eq. 9) applies at rank r=3. (iv) Direction: $c_2 = 0$ — theorem EXTENDS.
- **Inputs**: The K-theoretic decomposition formula $K_0(C_0(X \times Y)) \cong K_0(C_0(X)) \otimes K_0(C_0(Y))$ (Künneth for K-theory of commutative C*-algebras, Blackadar 1998 Thm 23.1.3). Maximal torus structure of $SU(3) \times U(1)$: $T^3 = U(1)^2 \times U(1) = U(1)^3$.
- **Gate**: NEW gate `S83-CARTAN-EXCL-NONSIMPLE-EXT`.
  - PASS: formal proof that $c_2(C^*(T_{SU(3) \times U(1)})) = 0$ follows from the abelian-subfactor argument without invoking simple-connectedness. Confirms the theorem is a statement about *abelian-ness* of $T_G$, not *simpleness* of G.
  - FAIL: counterexample or gap showing the simple hypothesis is load-bearing. Would narrow §IV.(c) scope.
  - INFO: proof works but reveals a hidden dependence (e.g., on torsion in $\pi_1(G)$).
- **Effort**: 4-6 hours, 1 agent session. Purely structural; no GPU. Paper-and-pencil K-theory with confirmatory Python for $K_0(C_0(\mathbb{Z}^3)) = \mathbb{Z}^{\oplus \mathbb{Z}^3}$ rank computation.

### V.4 `S83-QUANTUM-CARTAN-PROTECTION` — U_q(su(2)) Level-2 class under cyclic cohomology

- **What**: Per §IV.(d): compute the Level-2 class on the Drinfeld-Jimbo deformation $C^*(U_q(\mathfrak{su}(2)))$ at $q \neq 1$ (parameter $\theta := \log q / 2\pi i$ on the quantum-torus side). Output variable: $c_2^q := \langle c_2, \varphi_q \rangle$ where $\varphi_q \in HC^2(C^*(U_q(\mathfrak{su}(2))))$ is the Connes-Moscovici canonical 2-cocycle on the quantum torus. The test is whether the argument of §II BREAKS (as hypothesized in §IV.(d)) at Step 6 because $HC^2(C^*_\theta(\mathbb{Z}^r)) \neq 0$ for $\theta$ irrational.
- **Inputs**: (a) Connes-Moscovici 1998 "Hopf algebras, cyclic cohomology and the transverse index theorem" (Commun. Math. Phys. 198, 199-246) — quantum torus cyclic cocycle formula. (b) Rieffel 1981 "C*-algebras associated with irrational rotations" for the noncommutative torus $A_\theta$ structure. (c) Canonical input: $HC^2(A_\theta) = \mathbb{C}$ for $\theta$ irrational (Connes 1985 IHES 62 Appendix). (d) `tau_fold` and `M_KK` if coupling to Jensen deformation is probed.
  - Substitution chain: (i) Def: $A_\theta := C^*(\mathbb{Z}^2)_\theta$ generated by $U, V$ with $UV = e^{2\pi i \theta} VU$. (ii) Def: canonical 2-cocycle $\varphi_\theta(a_0, a_1, a_2) := \tau(a_0 (\delta_1 a_1)(\delta_2 a_2) - a_0 (\delta_2 a_1)(\delta_1 a_2))$ with $\delta_1, \delta_2$ the $U(1) \times U(1)$ action derivations. (iii) $\varphi_\theta \neq 0$ iff $\theta \notin \mathbb{Q}$. (iv) Direction: for $\theta$ irrational, the pairing $\langle c_2^q, \varphi_\theta \rangle$ is structurally allowed to be non-zero; whether it IS non-zero requires explicit computation of the Chern character of the regulator-asymmetry class.
- **Gate**: NEW gate `S83-QUANTUM-CARTAN-PROTECTION`.
  - PASS: $c_2^q \neq 0$ for some $\theta \notin \mathbb{Q}$. Opens Cartan-direction Level-2 protection in the quantum-group extended framework. Would motivate an S84+ investigation of whether the phonon-exflation framework has a natural quantum-deformation parameter.
  - FAIL: $c_2^q = 0$ even for $\theta$ irrational. Strengthens §IV.(d) to a closure.
  - INFO: $c_2^q$ computable only up to a ($q$-dependent) normalization; needs further gauge fixing.
- **Effort**: 2 agent sessions, ~12-16 hours. Mostly symbolic (sympy / paper-and-pencil); confirmatory numerical evaluation of the Connes-Moscovici formula at $\theta = \sqrt{2}$ (irrational test value) on a toy $A_\theta$ state space.

### V.5 `S83-CARTAN-LEVEL3-HIGHER-PROTECTION` — Level-3+ vanishing on abelian Cartan

- **What**: Per §IV.(b): extend the K-track argument from Level-2 to Level-3+ by computing the cyclic 4-cocycle on $C^*(T_{SU(3)}) = C_0(\mathbb{Z}^2)$ and verifying directly that $HC^4(C_0(\mathbb{Z}^2)) = 0$. Output: explicit chain-map computation of $HC^4$ via Connes' SBI sequence, confirming the $n \geq 1$ vanishing extends to $n = 4$.
  - Substitution chain: (i) Def: $HC^{2k}(C_0(X))$ for $X$ discrete abelian is zero for all $k \geq 1$ (Connes 1985 Thm II.3.3 applied at $n = 2k \geq 2$). (ii) Direction: $HC^4(C_0(\mathbb{Z}^2)) = 0$. (iii) Consequence: no Level-3 (= cyclic-4-cocycle pairing) protection on any Cartan subfactor, analogous to §II.(c).
- **Inputs**: (a) Connes 1985 IHES 62 §II.3 (explicit HC chain complex). (b) Loday 1998 "Cyclic Homology" Ch. 3 for the spectral sequence computation. (c) Pairing formula $\langle \cdot, \cdot \rangle: K_0(A) \times HC^{2k}(A) \to \mathbb{C}$ (eq. 10 of this synthesis, generalized to $k = 2$). (d) Canonical input: `tau_fold` invariance (Kato-Rellich bound $\alpha = 0.081$ from S61) implies the vanishing is Jensen-invariant at higher cyclic order as well.
- **Gate**: NEW gate `S83-CARTAN-LEVEL3-UNIVERSAL-EXCLUSION`.
  - PASS (expected): $HC^4(C^*(T)) = 0$ computed explicitly and Level-3 class forced to zero by Chern-character pairing. Extends the Level-2 wall to higher cyclic classes.
  - FAIL: a non-trivial $HC^4$ class discovered. Would force a re-examination of Connes 1985 Thm II.3.3 for group C*-algebras.
  - INFO: the argument requires an additional regularity hypothesis (smoothness of $M$, say) not needed at Level-2.
- **Effort**: 6-8 hours, 1 agent session. Symbolic (sympy); optional GPU-backed Chern-character pairing numerical confirmation.

### V.6 `S83-NONABELIAN-SU2-PROTECTION-COMPUTE` — Level-2 class on su(2) sub-branch of su(3)

- **What**: Per §IV.(a): the theorem forces $c_2 = 0$ on the Cartan $\mathfrak{u}(1)$ branch but leaves the $\mathfrak{su}(2)$ sub-branch of $\mathfrak{su}(3)$ (Baptista eq 3.58) OPEN. Compute $c_2(\mathfrak{su}(2))$ explicitly in $K_0(C_0(M) \otimes C^*(SU(2)))$ using the Kasparov-product representation (eq. 4 of this synthesis). Output: explicit 2-cocycle class; verdict on whether it is non-zero.
  - Substitution chain for the expected direction: (i) $C^*(SU(2))$ is NOT commutative; irreps include $\dim \mathcal{H}_\pi = 2, 3, \ldots$ (spin-$j$ reps). (ii) $HC^2(C^*(SU(2))) \neq 0$ (contains the $SU(2)$ fundamental class per Connes 1985 App). (iii) $K_0(C^*(SU(2))) \cong R(SU(2)) \cong \mathbb{Z}[t]$ (representation ring) has rank-$\geq 2$ projections (e.g., adjoint rep is rank 3). (iv) Direction: pairing $\langle c_2, \varphi \rangle$ structurally allowed to be non-zero; the Gelfand-Schur obstruction does NOT apply.
- **Inputs**: (a) $\mathfrak{su}(3) = \mathfrak{u}(1) \oplus \mathfrak{su}(2) \oplus \mathbb{C}^2$ branch decomposition (Baptista 2010 eq 3.58; Kaluza-Klein-09). (b) S61 A-TENSOR-61 block-decomposition theorem (KK-orthogonal decomposition, 0.47% one-loop, exact at tree). (c) Connes-Moscovici SU(2) cyclic 2-cocycle formula. (d) Canonical constant `tau_fold`, `M_KK` for regulator-asymmetry computation in the CCM spectral triple.
- **Gate**: NEW gate `S83-SU2-NONABELIAN-L2`.
  - PASS: $c_2(\mathfrak{su}(2)) \neq 0$ and realizes Level-2 R-protection on the $\mathfrak{su}(2)$ sub-branch. Identifies a concrete surviving averaging channel for the framework's regulator-asymmetry.
  - FAIL: $c_2(\mathfrak{su}(2)) = 0$ despite non-abelian structure. Would close the sole OPEN non-abelian protection channel at Level-2 and is structurally surprising.
  - INFO: pairing yields a zero-divisor in $\mathbb{Z}[t]$ rather than a clean number. Diagnostic, not decisive.
- **Effort**: 2 agent sessions, ~12-16 hours. Mixed symbolic + GPU numerical evaluation of Hochschild boundary (eq. 6) on the $\mathfrak{su}(2)$ branch basis.

### V.7 `S83-D4-KASPAROV-VDD-ROBUSTNESS` — Kasparov-submersion regularity on D₄

- **What**: Per §II.(b) and S61 K-HOMOLOGY-STABILITY: verify the Kato-Rellich bound $\alpha < 1$ on the Jensen-deformed $D_F$ for Spin(8), ensuring that eq. (4) (unbounded Kasparov-product factorization) applies in the rank-4 case. Output: bound $\alpha_{\mathrm{D4}}(\tau)$ for $\tau \in [0, \tau_{\mathrm{fold}}]$, spectral-gap check at fiber $(\mathrm{Spin}(8), \tau)$.
  - Substitution chain for the direction: (i) Def: Kato-Rellich bound $\alpha := \|[D_F^{(\mathrm{def})} - D_F^{(\tau=0)}] R(D_F^{(\tau=0)})\|$. (ii) For SU(3): S61 measured $\alpha = 0.081 < 1$. (iii) Deformation operator scales with adjoint-representation norm: $\|\mathrm{ad}_{\mathfrak{g}}\| \sim \dim(\mathfrak{g})^{1/2}$. (iv) $\dim(\mathfrak{so}(8)) = 28$ vs $\dim(\mathfrak{su}(3)) = 8$ — ratio 3.5 in dim, 1.87 in norm-bound. (v) Direction: predicted $\alpha_{\mathrm{D4}} \approx 0.081 \times 1.87 \approx 0.15 < 1$ — Kasparov factorization REMAINS valid, but the margin is smaller. Verification required.
- **Inputs**: S61 K-HOMOLOGY-STABILITY protocol and numerical tolerance. `tau_fold = 0.19` and `M_KK` from canonical_constants. Spin(8) adjoint representation matrices (28 × 28).
- **Gate**: NEW gate `S83-D4-KATO-RELLICH-BOUND`.
  - PASS (expected): $\alpha_{\mathrm{D4}}(\tau_{\mathrm{fold}}) < 0.5$. Confirms the base hypothesis of the Level-2 exclusion applies on D₄. Feeds V.1 (V.1 depends on this regularity).
  - FAIL: $\alpha_{\mathrm{D4}}(\tau) \geq 1$ at any $\tau \in [0, \tau_{\mathrm{fold}}]$. Kasparov factorization breaks; V.1 becomes inapplicable until regularity restored. Would open a genuine gap in universality.
  - INFO: $\alpha_{\mathrm{D4}} \in [0.5, 1.0)$ — valid but marginal; may warrant adaptive step-size in Jensen sweep.
- **Effort**: 3-4 hours, 1 agent session. GPU-accelerated 28-dim linear algebra; trivial VRAM footprint.

### V.8 `S83-VII-J-REGISTRY-SUBMIT` — canonical registry entry

- **What**: Submit the §VI-drafted paragraph (§VII.J of `summary/permanent-results-registry.md`) for registry inclusion following three-track (Connes + Van-den-Dungen + Spectral-geometer) cross-verification. Output: 15-line canonical paragraph with SHA-pinned gate verdicts and Connes 1985 citation.
- **Inputs**: (a) §VI of this synthesis (already drafted). (b) Van-den-Dungen synthesis §VIII.J (Gelfand-duality track). (c) Spectral-geometer synthesis §X / §VII.J (functional track). (d) `summary/permanent-results-registry.md` current structure. (e) Gate SHAs `61d732378be18b95` and `7a4e4f9f5ccff5f9`.
- **Gate**: META-gate (registry hygiene, not a new computation).
  - PASS: three-track paragraph integrated, cross-references all three synthesis documents, no sign-convention discrepancies.
  - FAIL: track inconsistency surfaced at integration (e.g., one track claims vanishing, another claims non-vanishing).
  - INFO: tracks agree on verdict but use incompatible conventions; note and defer normalization to S84.
- **Effort**: 1-2 hours, 1 agent session. No computation; synthesis + registry edit only.

---

## VI. Draft §VII.J entry (proposed canonical paragraph for `summary/permanent-results-registry.md`)

```markdown
## §VII.J. Level-2 Cartan Exclusion Theorem (S82)

**Statement**. For every compact connected simple Lie group G of rank r ≥ 1, with
maximal torus T ≅ U(1)^r, the Level-2 R-protection K-homology class c_2(C*(T)) ∈
K_0(C_0(M) ⊗ C*(T)) VANISHES in the CCM spectral triple under Kasparov-submersion
factorization (Van den Dungen 2018). Consequently, the dim H_π ≥ 2 criterion is a
UNIVERSAL NECESSARY condition for Level-2 R-protection across the Cartan-Killing
classification. Verified on 12/12 test groups {SU(3), SU(4), SU(5), Sp(2), Sp(3),
Spin(5), Spin(7), G_2, F_4, E_6, E_7, E_8}; Gelfand-universal extension covers the
entire classification including D_n.

**K-theory / cyclic-cohomology proof sketch** (Connes track). (i) T abelian ⇒
C*(T) ≅ C_0(Ẑ_T) ≅ C_0(ℤ^r) commutative. (ii) Gelfand-Naimark ⇒ every irrep of
C*(T) is 1D scalar point-evaluation. (iii) Connes 1985 (IHES 62) ⇒ HC^n(C_0(ℤ^r))
= 0 for all n ≥ 1, so no 2-cocycle pairs non-trivially with Chern character on K_0.
(iv) K_0(C_0(ℤ^r)) = ⊕_{χ ∈ ℤ^r} ℤ generated by rank-1 characters; no rank-≥2
projection classes. (v) c_2(C*(T)) = 0 follows by absence of averaging channel.
Gelfand's theorem is G-agnostic, so step (i) extends to every compact connected
simple G via the Maximal Torus Theorem.

**Sources**: W2-3 S82-KASPAROV-ABELIAN-PROOF PASS (SHA 61d732378be18b95…) — base
case (SU(3)); W3-3 S82-DIM-H-PI-UNIVERSAL-EXCLUSION PASS 12/12 (SHA 7a4e4f9f5cc…)
— universal extension. Falsifier: S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER (drift_u1
CLT-compliant on G_2 Cartan at L ≥ 8); expected FAIL under theorem. Classification:
GEOMETRIC (structural feature of spectral triple, not phononic excitation).
```

---

## VII. Structural implications (framework)

1. **Permanent wall added** to §IV.A of the S82 OOM doc: Level-2 Cartan exclusion is a universal K-theoretic theorem, $L_{\max}$-invariant, Jensen-invariant, and representation-theoretically uniform across Cartan-Killing.

2. **Substrate framing**: in the fabric picture, the Cartan subfactor of $C^*(G)$ is the set of "scalar directions" on each fiber — directions without internal multiplicity. The K-theoretic obstruction is the statement that these scalar directions cannot *average* regulator-scheme asymmetry within themselves; the within-sector averaging requires multi-dimensional $\mathcal{H}_\pi$, which scalar directions structurally lack. This is NOT a phononic excitation statement — it is a STRUCTURAL statement about the spectrum of $D_K$'s organization under the Baptista branch decomposition.

3. **Relation to the 7 NCG axioms**: the exclusion does not violate any axiom. It operates INSIDE the axiomatic framework, using: dimension (via $HC^n$ degree), regularity (smoothness of $\pi: M \times G \to M$), reality (implicit in $C^*(G)$ being a $*$-algebra), first-order (compatible with branch-orthogonal decomposition), orientability (not invoked), Poincaré duality (not invoked at Level-2; shows up at Level-3 where protection analysis continues). Finiteness, however, is implicit: the per-branch K_0 is countable-free-abelian, compatible with the axioms.

4. **Carry-forward for S83**: see §V for the eight structured carry-forward computations (V.1 through V.8), each with pre-registered gates and effort estimates. High-level summary: V.1 closes the D_n gap (Spin(8) sanity, user's explicit concern); V.2 pre-registers the exceptional-family falsifier (G₂ Cartan); V.3 extends the theorem to non-simple G = SU(3) × U(1); V.4 probes quantum-group deformation at $q \neq 1$; V.5 extends to Level-3 via $HC^4$ on $C_0(\mathbb{Z}^2)$; V.6 computes the OPEN non-abelian $c_2(\mathfrak{su}(2))$ class; V.7 verifies Kato-Rellich regularity on D₄ to support V.1; V.8 submits the §VII.J canonical registry entry.

5. **Updated closures count**: the Level-2 Cartan exclusion is ONE structural wall covering (abelian-subfactor × Cartan-Killing-classification) = (∞ × 12 infinite-families + 5 exceptionals) of the protection lattice. Adds one permanent-theorem row to §IV.A of the OOM doc; adds one row to §VII.J of the permanent-results-registry.

---

## VIII. Summary table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Level-2 Cartan Exclusion Theorem (K-theory track) | GEOMETRIC | PROVEN (W2-3 + W3-3 PASS) | Permanent wall; `dim H_π ≥ 2` is universal Level-2 criterion |
| 2 | Base case SU(3), abelian subfactor $c_2 = 0$ | GEOMETRIC | W2-3 PASS SHA `61d732378be18b95…` | Explains W0-2 drift_u1(L=8) = 88.54% empirically |
| 3 | Universal extension 12/12 compact simple $G$ | GEOMETRIC | W3-3 PASS SHA `7a4e4f9f5ccff5f9…` | All Cartan subfactors unprotected at Level-2 |
| 4 | Cyclic cohomology $HC^n(C^*(T)) = 0$ for $n \geq 1$ | GEOMETRIC | Connes 1985 Thm II.3.3 | Structural reason: no 2-cocycle pairing domain |
| 5 | $K_0(C^*(T)) = \bigoplus_{\chi} \mathbb{Z}$ free-abelian on rank-1 | GEOMETRIC | Standard | No rank-$\geq$2 classes from abelian data |
| 6 | Gelfand-universal reduction (G-agnostic proof) | GEOMETRIC | Structural | Extends to all compact connected reductive $G$ |
| 7 | Jensen-deformation invariance (S61 Kato-Rellich) | GEOMETRIC | $\alpha = 0.081 < 1$ | No rescue via $\tau$ tuning |
| 8 | Scope NOT claimed: non-abelian, Level-3+, quantum-group | GEOMETRIC | OPEN CHANNELS | §IV catalogues what survives |
| 9 | Falsifier gate S83-CARTAN-EXCL-EXCEPTIONAL-FALSIFIER | GEOMETRIC | PRE-REGISTERED | $G_2$ Cartan CLT test at $L \geq 8$; expected FAIL |
| 10 | $D_n$ verification gap in sanity table (Spin(8) missing) | GEOMETRIC | STRUCTURAL (covered by G-agnostic proof) | Recommend S83 verification row |
| 11 | Draft §VII.J entry for permanent-results-registry | META | PROPOSED | ≤15-line canonical paragraph |

---

*End of Connes K-theory / cyclic-cohomology synthesis of the Level-2 Cartan Exclusion Theorem. Verdicts W2-3 PASS and W3-3 PASS authoritative; proof track independent from (but consistent with) the Gelfand-duality and spectral-functional tracks produced by van-den-dungen and spectral-geometer peers. All equations dimensionally consistent; all direction claims traced through substitution chains; all approximations stated with their regime of validity. Canonical §VII.J entry drafted for three-track synthesis.*
