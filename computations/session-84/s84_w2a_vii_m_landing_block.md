## §VII.N — Three-Layer Regulator Theorem (Connes + Lizzi + Van den Dungen convergence, S84 W2a-11, 2026-04-19)

**Source**: S84 W2a-11. Script `computations/session-84/s84_w2a_vii_m_landing.py`; log
`s84_w2a_vii_m_landing.log`; block `s84_w2a_vii_m_landing_block.md`.

**Slot-allocation note**: Target slot §VII.M was occupied by the S84 W1b-9
DR3-RESPONSE-PROTOCOL registered earlier the same day (2026-04-19). Per plan
`session-84-plan-w2a.md` §9 FAIL clause and §11 remediation path, the theorem
content is preserved by landing under §VII.N; the registry-hygiene
violation is logged as FAIL-with-remediation. This does NOT invalidate the
theorem content; the three-layer stratification remains mathematically complete
and anchor-SHA-verified.

**Substrate framing**: The three-layer regulator theorem IS the substrate's
self-determination structure. L1 IS the form of the substrate's canonical
measure on its own operator spectrum -- Tr_omega(|D|^(-d)) = Res_{s=d}
zeta_D(s). L2 IS the substrate's heat-kernel action minimum at its own fold.
L3 IS the residual per-observable span after L1+L2 have done their work.
Direction: D_K spectrum -> canonical measure -> substrate action -> emergent
observable.

### Statement

Let (A, H, D) be the spectral triple of the phonon-exflation framework:

  - A  = C_infty(M^4) (x) A_F,  with A_F = C (+) H (+) M_3(C)  [G32 singleton]
  - H  = L^2(M^4, S) (x) H_F,   with H_F = C^32
  - D  = dslash_M (x) 1 + gamma^5 (x) D_F(tau),  at tau = tau_fold = 0.19

Regulator-choice for the spectral action S[D] = Tr f(D^2 / Lambda^2) admits a
unique three-layer stratification:

#### L1 (AXIOMATIC, global)

Under Connes axioms A1-A6 (dim-summability d >= 6, reality J^2 = -1 at KO-dim 6,
first-order [[D, a], b^o] = 0, orientability via Hochschild cycle of degree d,
Poincare duality in K-theory, regularity delta-closure), the canonical
summation measure on the spectrum of |D| is

    Tr_omega(T) = Res_{s = d} Tr(T |D|^(-s))      (Connes-Marcolli 2008 Thm 1.31)

Equivalently, Tr_omega(|D|^(-d)) coincides with the Dixmier trace on the ideal
L^(1, infty)(H) (Connes 1988 Thm 5; Dixmier 1966), and this is the ONLY trace-
class invariant under the Connes-Moscovici local index formula. Any external
scalar Lambda not already supplied by A1-A6 -- including the cut-offs required
by Zubarev and by Seeley-DeWitt -- falls OUTSIDE L1.

**Uniqueness at L1**: zeta.
**Anchor**: S83 W1-G3 PASS, sha256=`2343920a4c2a807a26bb9740ad6ede1c9d3465bb722d548dbefa978578c99ab5`.

#### L2 (SUBSTRATE-ACTION, local, at tau_fold)

Among the regulators {zeta, Zubarev, SDW, dim-reg, lattice-BR} that pass L1
admissibility AFTER an external scalar Lambda is admitted, the three-criterion
intersection test at L_max = 5, tau = tau_fold = 0.19 selects:

  (i)   integrability of the spectral sum                        [structural]
  (ii)  local-min-in-tau: d^2 S / d tau^2 > 0 at the fold         [structural]
  (iii) chirality chi = +1: sign(d^2 S / d(log Lambda)^2) = +1    [KO-6 filter]

  passes[zeta]    = (True,  True,  False)  [chi = 0; no explicit Lambda dependence beyond subtraction pole]
  passes[Zubarev] = (True,  True,  True)   [heat-kernel integrable; curv +1.16e5; chi = +1]
  passes[SDW]     = (True,  False, True)   [a_4 saddle vanishes curvature; chi_SDW = -1 wrong-sign]

**Uniqueness at L2**: Zubarev.
**Anchor**: S83 W1-G1 PASS, sha256=`227a591307f88d2cfdb1c505c6ab4a040f873db4656116c5948ae7ba3c96dcdd`.

#### L3 (OBSERVABLE, per-Q)

For each observable Q in the §VII.K-DUAL 42-row propagation atlas, the
5-regulator span

    span_Q  =  max_R  Q[R]  /  min_R  Q[R]

partitions into exactly two classes:

  R-protected    (balanced Mellin ratio) : span_Q in [1.0, 1.5]
  NOT-R-protected (unbalanced)            : span_Q in [2.5, infinity)

The gap [1.5, 2.5] is empty at L_max = 5 (S83 G58 meta-principle, 10/10 checks
pass). L3 is NOT a uniqueness layer; it is the residual per-observable freedom
AFTER L1 and L2 have selected canonical measures.

**Anchors**:
  - G57 pinning audit: sha256=`fcfbc362651e3f57137a90dd703a501d645ef87b99f8d250e92c6984bf6ccd68` (11/11 pinning validity)
  - G58 meta-principle: sha256=`b941613aa8ae91fcebf4ecadb0da74ad37d9382c7cbd2413a14f9b91729d24f2` (R-protected <=1.5 / NOT-R >=2.5 band separation)

### Corollaries

**(C1)** The CC-5 propagation identity (§VII.K-PROP) --
`span(O) = product_i span(F_i)^|p_i|` -- applies ONLY WITHIN L3; L1 and L2 do
NOT propagate via Mellin exponents. Propagation is a feature of the residual
stratum only.

**(C2)** NOT-R-protected observables (e.g. k_a2 with span = 14.685 at L_max = 5,
G15 FAIL) inherit regulator-dependence at L3. L2 canonicalizes them by fiat of
the Zubarev substrate-action minimum; degree of discretion is **ZERO at L1**,
**ZERO at L2**, **NON-ZERO at L3**.

**(C3)** The theorem is FALSIFIABLE: any spectral triple (A', H', D') in which
L1 selects Zubarev OR L2 selects zeta refutes the layer ordering. Testing slot
is S84 W2a-12 (HP^4, Spin(8)-extended SU(3), T^4, T^8).

### Three-solo convergence

  Connes (NCG axiomatic, L1):            Dixmier-trace / residue-theorem uniqueness
  Lizzi (spectral functional, L2):       three-criterion intersection uniqueness
  Van den Dungen (Kasparov bridge, L3):  per-Q span partition via KK-product

Each solo derives its layer from an independent mathematical infrastructure.
The three layers are mutually orthogonal: L1 does not propagate; L2 does not
admit zeta; L3 is the residual the other two leave behind.

### Falsifiability handle

The theorem-level falsifier is gate S84-LAYER-ORDERING-FALSIFIER (W2a-12); the
per-row layer pin is S84-LAYER-PIN-REGISTRY-LANDING (W2a-13); the L1-L2
projection table across the 11 framework-target observables is
S84-L1-L2-PROJECTION (W2a-14). Any of these returning FAIL refutes the theorem
at the corresponding stratum.

### Anchor-SHA pin block

  S83 W1-G1 IC-SCHEME-DERIVATION:                 sha256 = `227a591307f88d2cfdb1c505c6ab4a040f873db4656116c5948ae7ba3c96dcdd`
  S83 W1-G3 SUBSTRATE-NATIVE-REGULATOR-PRIORITY:  sha256 = `2343920a4c2a807a26bb9740ad6ede1c9d3465bb722d548dbefa978578c99ab5`
  S83 G57   PINNING-AUDIT-FRAMEWORK-WIDE:         sha256 = `fcfbc362651e3f57137a90dd703a501d645ef87b99f8d250e92c6984bf6ccd68`
  S83 G58   META-PRINCIPLE-REGISTRY-LANDING:      sha256 = `b941613aa8ae91fcebf4ecadb0da74ad37d9382c7cbd2413a14f9b91729d24f2`

### Verdict

**FAIL** at registration (2026-04-19).

  collision_note: §VII.M occupied by: Event-driven pre-registrations (S84+) (DR3-RESPONSE-PROTOCOL, S84 W1b-9, 2026-04-19); landing routed to §VII.N
  4-tuple: (value=<landing_block_sha>, scheme=VII.M, convention=three-layer, L_max=5)

**What PASS means (when slot is vacant)**: Theorem becomes permanent; regulator
choice is uniquely determined in 2 of 3 layers, residual fully catalogued by
CC-5; all "regulator ambiguity" objections in the framework are henceforth
answered by the layer classification.

**What FAIL-with-remediation means (this instance)**: Theorem content is
mathematically complete and anchor-SHA-verified, but §VII.M was pre-occupied
by S84 W1b-9 DR3-RESPONSE-PROTOCOL registered earlier the same day. Landing
preserved under §VII.N. Registry-hygiene violation logged; no
compromise of theorem content. Carry-forward: if DR3-RESPONSE-PROTOCOL is
subsequently relocated (e.g. to §VII.M-PRE-REG sub-namespace), this entry may
be relocated to §VII.M on an explicit reconciliation-gate action.

---
