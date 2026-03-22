# Session 26 Priority 3: Higher-Order Seeley-DeWitt (a_6) -- DESIGN DOCUMENT

## Author: Gen-Physicist
## Date: 2026-02-25

---

## 1. Goal

Compute the Seeley-DeWitt coefficient a_6(tau) for the Dirac Laplacian D_K^2 on
Jensen-deformed (SU(3), g_tau) at 21 tau values in [0, 0.30], then assemble the
three-term spectral action potential

    V_spec^(6)(tau) = c_2 * R_K(tau) + c_4 * A_4(tau) + c_6 * A_6(tau)

and determine whether including a_6 creates a stabilization minimum in V_spec
that was absent in the two-term (a_2 + a_4) analysis (V-1 closure, Session 24a).

---

## 2. Mathematical Framework

### 2.1 Spectral Action Expansion

The spectral action Tr f(D_K^2 / Lambda^2) on a compact Riemannian 8-manifold
has the asymptotic expansion (Chamseddine-Connes):

    S ~ f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4 + f_{-2} Lambda^{-2} a_6 + ...

where f_k = integral_0^infty f(u) u^{(k/2)-1} du are the moments of the test
function f, and a_{2n} are the Seeley-DeWitt (heat kernel) coefficients.

The effective potential for the modulus tau (after factoring out tau-independent
constants) is:

    V_spec(tau) = c_2 * a_2^{red}(tau) + c_4 * a_4^{red}(tau) + c_6 * a_6^{red}(tau) + ...

where:
- c_2 = f_2 Lambda^2 (4pi)^{-4} Vol_K       [tau-independent]
- c_4 = f_0 (4pi)^{-4} Vol_K                 [tau-independent]
- c_6 = f_{-2} Lambda^{-2} (4pi)^{-4} Vol_K  [tau-independent]

and the "reduced" coefficients carry all tau-dependence:

    a_2^{red}(tau)  = (20/3) R_K(tau)
    a_4^{red}(tau)  = (1/360) [500 R^2 - 32|Ric|^2 - 28 K](tau)
    a_6^{red}(tau)  = [formula derived below]

**Key ratio:** rho = c_4/c_2 = f_0 / (f_2 Lambda^2), and
rho_6 = c_6/c_2 = f_{-2} / (f_2 Lambda^4).

The V-1 closure (Session 24a) showed that V_spec(tau; rho) = -R_K + rho * a4_geom
is monotonically increasing for ALL rho > 0. The question is whether the a_6
term, which involves CUBIC curvature invariants, breaks this monotonicity.

### 2.2 Convention Reconciliation

**IMPORTANT:** Two different a_4 formulas exist in the codebase.

The **CORRECT** formula for the Dirac Laplacian D_K^2 on 8-dim SU(3) is
(derived in `s23c_fiber_integrals.py`, lines 380-429):

    a_4 propto 500 R^2 - 32|Ric|^2 - 28 K

where K = R_{abcd} R^{abcd} is the Kretschner scalar. This accounts for:
- Universal Gilkey terms: 16*(5R^2 - 2|Ric|^2 + 2K)  [dim_S * scalar Laplacian piece]
- Lichnerowicz E = R/4: 240 R^2 + 180 R^2  [from 60RE + 180E^2 traced over dim_S=16]
- Spin connection curvature: 30 * tr_S(Omega_S^2) = 30 * (-2K) = -60K

The `sd20a_seeley_dewitt_gate.py` script uses a DIFFERENT formula
(125 R^2 - 8|Ric|^2 + 2K, up to an overall factor) that has an error in the
spin connection curvature trace. For the a_6 design, we use the s23c convention
exclusively.

### 2.3 Gilkey-Seeley-DeWitt a_6 Formula

For a general Laplacian-type operator P = -(g^{ij} nabla_i nabla_j + ...) =
nabla^* nabla + E with connection curvature Omega_{ij}, the a_6 coefficient
on a closed (boundaryless) Riemannian manifold of dimension d is
(Gilkey 1995, Theorem 4.3.1; Avramidi 2000, eq 6.58; Vassilevich 2003, eq 4.3):

    (4pi)^{d/2} a_6(x) = tr_V [
        (1/7!) * {
            -18 R_{;kk;ll}                                       ... (T1)
          + 17 R_{;k} R_{;k}                                     ... (T2)
          - 2  R_{ab;k} R_{ab;k}                                 ... (T3)
          - 4  R_{ab;c} R_{ac;b}                                 ... (T4)
          + 9  R_{abcd;e} R_{abcd;e}                              ... (T5)
          + 28 R R_{;kk}                                          ... (T6)  [**]
          - 8  R_{ab} R_{ab;kk}                                  ... (T7)  [**]
          + 24 R_{ab} R_{ac;bc}                                  ... (T8)  [**]
          + 12 R_{abcd} R_{abcd;ee}                              ... (T9)  [**]
          + (35/9) R^3                                            ... (T10)
          - (14/3) R R_{ab} R_{ab}                                ... (T11)
          + (14/3) R R_{abcd} R_{abcd}                            ... (T12)
          - (208/9) R_{ab} R_{bc} R_{ca}                         ... (T13)
          - (64/3) R_{ab} R_{cdea} R_{cdeb}                      ... (T14)
          + (16/3) R_{ab} R_{acde} R_{bcde}                      ... (T15)
          + (44/9) R_{abcd} R_{abef} R_{cdef}                    ... (T16)
          + (80/9) R_{abcd} R_{aecf} R_{bedf}                    ... (T17)
        } * Id_V
                                                                  ... [UNIVERSAL PART]
      + (1/360) * {
            8 R_{;kk} E                                           ... (T18)
          + 2 R_{;k} E_{;k}                                      ... (T19)  [**]
          + 12 R_{;kk} Omega_{ab} Omega_{ab}                     ... (T20)  [**]
          ... [many E and Omega cross-terms]
        }
                                                                  ... [E AND OMEGA PART]
    ]

**CRITICAL SIMPLIFICATION on (SU(3), g_tau):**

On a **homogeneous space** with a **left-invariant metric**, ALL covariant
derivatives of curvature tensors VANISH:

    R_{;k} = 0,   R_{ab;k} = 0,   R_{abcd;e} = 0

This is because the curvature is constant (parallel with respect to the
left-invariant frame). More precisely: on a Lie group with left-invariant metric,
the Riemann tensor, Ricci tensor, and scalar curvature are constant functions
on the manifold (computed purely from the structure constants and metric).

**Consequence:** Terms T1-T9 and T18-T20 (all terms with covariant derivatives
of curvature) are IDENTICALLY ZERO.

Similarly, for the Lichnerowicz endomorphism E = (R/4)*Id_S:
    E_{;k} = (R_{;k}/4)*Id_S = 0
    E_{;kk} = 0

And for the spin connection curvature Omega_{ij} = (1/4) R_{ijkl} gamma^{kl}:
    (Omega_{ij})_{;k} = (1/4) R_{ijkl;m} gamma^{kl} = 0

**All derivative terms vanish.** Only the purely algebraic (zero-derivative)
terms survive.

### 2.4 Surviving Terms for a_6 on Homogeneous Spaces

After eliminating all derivative terms, the a_6 coefficient for a general
Laplacian P = nabla^*nabla + E with connection Omega reduces to
(Vassilevich 2003, eq 4.3, derivative-free terms only):

    (4pi)^{d/2} a_6(x) = tr_V [
      (1/7!) * A_universal * Id_V
      + (1/360) * B_mixed
      + C_pure_E_Omega
    ]

where the **universal** part (purely geometric, traced with Id_V) involves
ONLY the cubic curvature invariants:

    A_universal = (35/9) R^3
                - (14/3) R |Ric|^2
                + (14/3) R K
                - (208/9) Ric^3
                - (64/3) I_5
                + (16/3) I_6
                + (44/9) I_7
                + (80/9) I_8

with the cubic Riemann invariants defined as:

    |Ric|^2 = R_{ab} R_{ab}
    K = R_{abcd} R_{abcd}
    Ric^3 = R_{ab} R_{bc} R_{ca}
    I_5 = R_{ab} R_{cdea} R_{cdeb}
    I_6 = R_{ab} R_{acde} R_{bcde}
    I_7 = R_{abcd} R_{abef} R_{cdef}
    I_8 = R_{abcd} R_{aecf} R_{bedf}

The **E-dependent** terms (from E = R/4 on spinors):

    B_E = (1/360) * tr_S [
        60 R E^2 + 30 E R_{;kk} + 30 E_{;k} E_{;k} + ...
    ]

On a homogeneous space, the non-vanishing E-terms are those involving only E
and curvature (no derivatives of E or curvature). From Gilkey (1995), the
relevant E-terms in a_6 (zero derivatives only) are:

    a_6^E = tr_S [
        (1/7!) * (
            -  (44/9) R E^2
            + (20/3) R_{ab} R_{ab} E
            ... [additional E, E^2, E^3 terms]
        )
      + (1/7!) * (
            (1/45) {E^3}
          + (1/36) R E^2
          + (1/90) R^2 E
          ...
        )
    ]

**Let me state the exact formula more carefully.**

For the general operator P = nabla^*nabla + E on a closed manifold WITHOUT
boundary, the full a_6 with ZERO covariant derivatives of R, E, Omega is
(Avramidi 2000, Heat Kernel Method, Chapter 6; also Branson-Gilkey 1990):

    (4pi)^{d/2} * 7! * a_6(x) = tr_V [
        (35/9) R^3 Id
      - (14/3) R |Ric|^2 Id
      + (14/3) R K Id
      - (208/9) Ric^3 Id
      - (64/3) I_5 Id
      + (16/3) I_6 Id
      + (44/9) I_7 Id
      + (80/9) I_8 Id
                                          ... [7 purely geometric terms]
      + 42 R^2 E
      - 28 |Ric|^2 E
      + 28 K E
      - 140 R E^2
      + 280 E^3
                                          ... [E terms, up to E^3]
      + 42 R Omega^2
      - 168 R_{ab} Omega_{ai} Omega_{bi}
      + 168 R_{abcd} Omega_{ab} Omega_{cd}
      + 280 E Omega^2
                                          ... [Omega and E*Omega cross-terms]
    ]

where:
- Omega^2 = Omega_{ij} Omega_{ij} (summed over spacetime indices i,j)
- Traces are over the fiber (spinor) bundle

**NOTE ON COEFFICIENT SOURCE:** The exact numerical coefficients vary across
references due to different conventions for the overall normalization (some use
(4pi)^{-d/2}, some use (4pi t)^{-d/2}, some include factors of 7! or 360).
The coefficients above are from Avramidi (2000) using the 7! convention.

**BEFORE IMPLEMENTATION:** The coefficients must be cross-checked against at
least two independent sources. The recommended primary references are:

1. Gilkey, P.B. (1995). "Invariance Theory, the Heat Equation, and the
   Atiyah-Singer Index Theorem," 2nd edition. CRC Press. Theorem 4.3.1.

2. Vassilevich, D.V. (2003). "Heat kernel expansion: user's manual."
   Physics Reports 388, 279-360. Equation (4.3).

3. Avramidi, I.G. (2000). "Heat Kernel and Quantum Gravity." Springer.
   Section 6.3.

4. Branson, T.P., Gilkey, P.B. (1990). "The asymptotics of the Laplacian
   on a manifold with boundary." Comm. PDE 15, 245-272.

**The implementation MUST verify these coefficients by checking the bi-invariant
(tau=0) limit against known results for compact Lie groups before computing
the tau-dependence.**

---

## 3. Required Cubic Curvature Invariants

### 3.1 Definitions

On (SU(3), g_tau) with R_{abcd} in the orthonormal (ON) frame (where g_{ab} = delta_{ab}),
we need eight cubic curvature invariants:

1. **R^3**: Cube of scalar curvature.
   - Available: R_scalar from `r20a_riemann_tensor.npz`.
   - Computation: trivial.

2. **R * |Ric|^2**: R * R_{ab} R_{ab}.
   - Available: R_scalar and Ric_sq from `s23c_fiber_integrals.npz`.
   - Computation: trivial (product of known quantities).

3. **R * K**: R * R_{abcd} R_{abcd}.
   - Available: R_scalar and K_kretschner.
   - Computation: trivial.

4. **Ric^3 = R_{ab} R_{bc} R_{ca}**: Trace of the cube of the Ricci tensor.
   - Available: Ric tensor from `r20a_riemann_tensor.npz` (shape (21,8,8)).
   - Computation: `np.einsum('ab,bc,ca->', Ric, Ric, Ric)` at each tau.

5. **I_5 = R_{ab} R_{cdea} R_{cdeb}**: Mixed Ricci-Riemann cubic.
   - Requires: Ric (8x8) and R_abcd (8x8x8x8).
   - Computation: `np.einsum('ab,cdea,cdeb->', Ric, R, R)` at each tau.
   - Note: R_abcd has antisymmetry R_{cdea} = R_{abcd}[c,d,e,a]. This
     contraction is between one Ricci index (b) and two Riemann tensors
     sharing three indices (c,d,e).

6. **I_6 = R_{ab} R_{acde} R_{bcde}**: Ricci contracted with Riemann-squared.
   - Computation: `np.einsum('ab,acde,bcde->', Ric, R, R)`.
   - Note: This is equivalent to R_{ab} * (sum_{c,d,e} R_{acde} R_{bcde}),
     which is R_{ab} times the "Lichnerowicz Riemann operator" applied to Ric.

7. **I_7 = R_{abcd} R_{abef} R_{cdef}**: Pure Riemann cubic (type I).
   - Computation: `np.einsum('abcd,abef,cdef->', R, R, R)`.
   - This contracts two pairs of indices between each pair of Riemann tensors.

8. **I_8 = R_{abcd} R_{aecf} R_{bedf}**: Pure Riemann cubic (type II).
   - Computation: `np.einsum('abcd,aecf,bedf->', R, R, R)`.
   - This contracts indices in a "cyclic" pattern. This is the most intricate
     contraction.

### 3.2 Computational Cost

Each einsum over an (8,8,8,8) tensor:
- I_7 and I_8 involve triple contraction of 8^4-tensors.
- Naive cost: O(8^8) ~ 16.7M operations per invariant per tau.
- With numpy einsum optimization: effectively O(8^6) ~ 260K per contraction.
- For 21 tau values: 21 * 8 invariants * ~260K ~ 44M operations total.
- **Estimated time: < 1 second on CPU.** No GPU needed.

### 3.3 Spinor Traces

Beyond the universal geometric terms, a_6 involves traces over the spinor bundle
of expressions involving E = (R/4)*Id_S, Omega_{ij} = (1/4) R_{ijkl} gamma^{kl},
and their products.

**E terms:** Since E = (R/4)*Id_{16} is proportional to the identity:
- tr_S(E) = 4R
- tr_S(E^2) = R^2
- tr_S(E^3) = R^3/4
- tr_S(R^2 E) = R^3/4 * 16 = 4 R^3
- tr_S(|Ric|^2 E) = |Ric|^2 * (R/4) * 16 = 4R|Ric|^2
- etc.

All E-terms reduce to products of scalar curvature with known quadratic
invariants. No new tensor contractions needed.

**Omega terms:**

tr_S(Omega_{ij} Omega_{ij}) was already computed in s23c:
    tr_S(Omega^2) = -2K

For a_6, we need HIGHER traces involving Omega:

**tr_S(Omega_{ij} Omega_{jk} Omega_{ki}):**

    Omega_{ij} = (1/4) R_{ijkl} gamma^{kl}

    Omega_{ij} Omega_{jk} = (1/16) R_{ijab} R_{jkcd} gamma^{ab} gamma^{cd}

    tr_S(Omega_{ij} Omega_{jk} Omega_{ki})
      = (1/64) R_{ijab} R_{jkcd} R_{kief} * tr_S(gamma^{ab} gamma^{cd} gamma^{ef})

The trace of 6 gamma matrices (in 8 dimensions) is:

    tr(gamma^{a1} ... gamma^{a6}) = 16 * [delta^{a1a2} delta^{a3a4} delta^{a5a6}
                                          - delta^{a1a2} delta^{a3a5} delta^{a4a6}
                                          + delta^{a1a2} delta^{a3a6} delta^{a4a5}
                                          + 14 more terms (all 15 pairings)]

This is the sum over all 15 perfect matchings of {a1,...,a6} with signs
determined by the permutation parity. In d=8 Euclidean:

    tr(gamma^{a1} ... gamma^{a6}) = 16 * sum_{sigma in S_6/((S_2)^3*S_3)} sgn(sigma) * prod delta^{sigma}

This generates new cubic Riemann contractions beyond I_7 and I_8. However,
because we are on a low-dimensional space (d=8 with only 3 independent scale
factors in the Jensen deformation), the number of independent cubic invariants
is limited.

**tr_S(R * Omega^2) and tr_S(E * Omega^2):**

    tr_S(R * Omega^2) = R * tr_S(Omega^2) = R * (-2K) = -2RK

    tr_S(E * Omega^2) = (R/4) * tr_S(Omega^2) = (R/4)*(-2K) = -RK/2

**tr_S(R_{ab} Omega_{ai} Omega_{bi}):**

    R_{ab} * (1/16) R_{aicd} R_{bief} tr_S(gamma^{cd} gamma^{ef})
    = R_{ab} * (1/16) R_{aicd} R_{bief} * 16 * 2 (delta^{ce} delta^{df} - delta^{cf} delta^{de})
    = R_{ab} * [2 R_{aicd} R_{bicd} - 2 R_{aicd} R_{bidc}]
    = R_{ab} * [2 R_{aicd} R_{bicd} + 2 R_{aicd} R_{bicd}]     (using R_{bidc} = -R_{bicd})
    = 4 R_{ab} R_{aicd} R_{bicd}
    = 4 I_6

where in the last step we used R_{aicd} R_{bicd} summed over i,c,d is precisely
the contraction pattern defining I_6 (with the Ricci tensor R_{ab} contracting the
remaining free indices).

Wait -- let me recheck. The trace:

    tr_S(gamma^{cd} gamma^{ef}) = 16(delta^{ce} delta^{df} - delta^{cf} delta^{de})

But gamma^{cd} = (1/2)[gamma^c, gamma^d], so:

    tr_S(gamma^{cd} gamma^{ef}) = (1/4) tr([gamma^c,gamma^d][gamma^e,gamma^f])
                                = 16 (delta^{ce} delta^{df} - delta^{cf} delta^{de})

(same result as computed in sd20a lines 258-282).

Then:

    R_{ab} * tr_S(Omega_{ai} Omega_{bi})
    = R_{ab} * (1/16) * sum_{i} R_{aicd} R_{bief} * 16 * (delta^{ce}delta^{df} - delta^{cf}delta^{de})
    = R_{ab} * sum_i [R_{aicd} R_{bicd} - R_{aicd} R_{bidc}]
    = R_{ab} * sum_i [R_{aicd} R_{bicd} + R_{aicd} R_{bicd}]
    = 2 * R_{ab} * sum_{icd} R_{aicd} R_{bicd}

Now sum_{icd} R_{aicd} R_{bicd} = sum_{icd} R_{aicd}^2 with a shared first index.
This is NOT the same as I_6.

I_6 = R_{ab} R_{acde} R_{bcde} = R_{ab} * (sum_{cde} R_{acde} R_{bcde})

The contraction here is R_{ab} * M_{ab} where M_{ab} = sum_{cde} R_{acde} R_{bcde}.

The quantity sum_i R_{aicd} R_{bicd} = sum_{icd} R_{aicd} R_{bicd} = M_{ab}^{(2)}
where the contraction pattern is over i (2nd index) and c,d (3rd,4th indices).

By the pair-exchange symmetry R_{abcd} = R_{cdab}, and antisymmetries:
    sum_{icd} R_{aicd} R_{bicd}

To relate this to standard invariants, note:
    R_{aicd} = -R_{iacd} (antisymmetry in first pair)

So: sum_{icd} R_{aicd} R_{bicd} = sum_{icd} R_{iacd} R_{ibcd}
                                  = sum_{icd} R_{cdai}^2 ... [using pair exchange]

Actually, let me define it precisely:
    M_{ab} = sum_{icd} R_{aicd} R_{bicd}

Using pair exchange: R_{aicd} = R_{cdai}, so:
    M_{ab} = sum_{icd} R_{cdai} R_{bicd}

And R_{bicd} = R_{cdbi} by pair exchange, so:
    M_{ab} = sum_{icd} R_{cdai} R_{cdbi} = sum_{cdi} R_{cdai} R_{cdbi}

This is: for each (c,d), contract the last two indices of R_{cd..} against each other
with one index being a and the other being b.

In any case, M_{ab} is a well-defined symmetric tensor that can be computed from
R_{abcd} by `np.einsum('aicd,bicd->ab', R, R)`.

Then: sum_{ab,i} R_{ab} Omega_{ai} Omega_{bi} (traced) = 2 * R_{ab} M_{ab}
    = 2 * np.einsum('ab,ab->', Ric, M) = 2 * new_invariant.

**This is a new contraction that must be computed explicitly.**

**tr_S(R_{abcd} Omega_{ab} Omega_{cd}):**

    = (1/16) R_{abcd} R_{abef} R_{cdgh} tr_S(gamma^{ef} gamma^{gh})
    = (1/16) R_{abcd} R_{abef} R_{cdgh} * 16 (delta^{eg} delta^{fh} - delta^{eh} delta^{fg})
    = R_{abcd} [R_{abef} R_{cdef} - R_{abef} R_{cdfe}]
    = R_{abcd} [R_{abef} R_{cdef} + R_{abef} R_{cdef}]     (R_{cdfe} = -R_{cdef})
    = 2 R_{abcd} R_{abef} R_{cdef}
    = 2 I_7

So: tr_S(R_{abcd} Omega_{ab} Omega_{cd}) = 2 I_7.

### 3.4 Summary of Required New Contractions

Beyond the already-available quantities (R, |Ric|^2, K), we need:

| Invariant | Formula | Einsum | New? |
|-----------|---------|--------|------|
| R^3 | R_scalar^3 | trivial | No |
| R * |Ric|^2 | R * Ric_sq | trivial | No |
| R * K | R * K_kretschner | trivial | No |
| Ric^3 | R_{ab} R_{bc} R_{ca} | `'ab,bc,ca->'` on Ric | **Yes** |
| I_5 | R_{ab} R_{cdea} R_{cdeb} | `'ab,cdea,cdeb->'` on Ric, R, R | **Yes** |
| I_6 | R_{ab} R_{acde} R_{bcde} | `'ab,acde,bcde->'` on Ric, R, R | **Yes** |
| I_7 | R_{abcd} R_{abef} R_{cdef} | `'abcd,abef,cdef->'` on R, R, R | **Yes** |
| I_8 | R_{abcd} R_{aecf} R_{bedf} | `'abcd,aecf,bedf->'` on R, R, R | **Yes** |
| M_{ab} | sum_{icd} R_{aicd} R_{bicd} | `'aicd,bicd->ab'` on R, R | **Yes** (for Omega trace) |
| Omega^3 trace | (see Section 3.3) | triple gamma trace | **Yes** (complex) |

### 3.5 The Omega^3 Trace Problem

The term tr_S(Omega_{ij} Omega_{jk} Omega_{ki}) requires evaluating:

    (1/64) sum_{ijk} R_{ijab} R_{jkcd} R_{kief} tr_S(gamma^{ab} gamma^{cd} gamma^{ef})

The trace of 6 gamma matrices in d=8 dimensions is a sum over 15 terms (Wick
contractions). Defining gamma^{ab} = (1/2)[gamma^a, gamma^b], the product
gamma^{ab} gamma^{cd} gamma^{ef} is a sum of products of 6 individual gammas
(with factors of 1/8 from the three commutators). The trace of 6 gammas is:

    tr(gamma^{a1} gamma^{a2} gamma^{a3} gamma^{a4} gamma^{a5} gamma^{a6})
    = 2^{d/2} * sum_{pairings} sgn(pairing) * prod delta^{paired}

For d=8, 2^{d/2} = 16. There are 15 perfect matchings of 6 objects:

    {12,34,56}, {12,35,46}, {12,36,45},
    {13,24,56}, {13,25,46}, {13,26,45},
    {14,23,56}, {14,25,36}, {14,26,35},
    {15,23,46}, {15,24,36}, {15,26,34},
    {16,23,45}, {16,24,35}, {16,25,34}

Each pairing gives a product of 3 Kronecker deltas with a sign.

**Implementation approach:** Rather than expanding the 15-term sum analytically,
compute tr_S(Omega_{ij} Omega_{jk} Omega_{ki}) NUMERICALLY by:

1. Build Omega_{ij} = (1/4) R_{ijkl} gamma^{kl} as an (8,8,16,16) array.
2. For each (i,j,k), multiply the three 16x16 matrices Omega_{ij}, Omega_{jk}, Omega_{ki}.
3. Take the trace.
4. Sum over (i,j,k).

This is O(8^3 * 16^3) ~ 2.1M operations per tau value. Negligible.

**Alternatively:** Use the explicit Clifford algebra representation from
`tier1_dirac_spectrum.py` (`build_cliff8()` function) which provides the
8 gamma matrices as 16x16 matrices.

---

## 4. Complete a_6 Formula on Homogeneous SU(3)

Collecting all terms (universal, E, Omega, E*Omega) with ZERO derivatives,
for the Dirac Laplacian D_K^2 on an 8-dimensional homogeneous space:

    (4pi)^4 * 7! * a_6^{red}(tau) = [UNIVERSAL] + [E-ONLY] + [OMEGA-ONLY] + [E*OMEGA]

### 4.1 Universal Part (traced with dim_S = 16)

    U = 16 * [
        (35/9) R^3
      - (14/3) R |Ric|^2
      + (14/3) R K
      - (208/9) Ric^3
      - (64/3) I_5
      + (16/3) I_6
      + (44/9) I_7
      + (80/9) I_8
    ]

### 4.2 E-Only Part (E = R/4 * Id_16)

From the Gilkey/Vassilevich formulas with derivative terms dropped:

    E_part = tr_S [
        42 R^2 * E - 28 |Ric|^2 * E + 28 K * E - 140 R * E^2 + 280 E^3
    ]
    = 16 * [42 R^2 * (R/4) - 28 |Ric|^2 * (R/4) + 28 K * (R/4) - 140 R * (R/4)^2 + 280 * (R/4)^3]
    = 16 * [(42/4) R^3 - 7 R |Ric|^2 + 7 R K - (140/16) R^3 + (280/64) R^3]
    = 16 * [(10.5 - 8.75 + 4.375) R^3 - 7 R |Ric|^2 + 7 R K]
    = 16 * [6.125 R^3 - 7 R |Ric|^2 + 7 R K]
    = 98 R^3 - 112 R |Ric|^2 + 112 R K

### 4.3 Omega-Only Part

    Omega_part = tr_S [
        42 R * Omega^2 - 168 R_{ab} Omega_{ai} Omega_{bi} + 168 R_{abcd} Omega_{ab} Omega_{cd}
    ]

Using the traces computed in Section 3.3:
- tr_S(Omega^2) = -2K
- tr_S(R_{ab} Omega_{ai} Omega_{bi}) = 2 * R_{ab} M_{ab}  (new contraction)
- tr_S(R_{abcd} Omega_{ab} Omega_{cd}) = 2 * I_7

    Omega_part = 42 R * (-2K) - 168 * (2 R_{ab} M_{ab}) + 168 * (2 I_7)
               = -84 R K - 336 R_{ab} M_{ab} + 336 I_7

### 4.4 E*Omega Cross Part

    EO_part = tr_S [280 E * Omega^2]
            = 280 * (R/4) * (-2K) * ...

Wait -- the 280 E Omega^2 term requires:
    tr_S(E * Omega_{ij} Omega_{ij}) = (R/4) * tr_S(Omega_{ij}^2) = (R/4)*(-2K) = -RK/2

Summed over all i,j (already included in Omega^2 notation):

    EO_part = 280 * (-R K / 2) = -140 R K

### 4.5 Cubic Omega Part

There may also be a pure Omega^3 term:

    Omega3_part = c_Omega3 * tr_S(Omega_{ij} Omega_{jk} Omega_{ki})

The coefficient c_Omega3 needs to be extracted from the full a_6 formula.
From Vassilevich (2003, eq 4.3), the Omega^3 term in a_6 is:

    (1/7!) * ... [no pure Omega^3 in universal part]

Actually, examining the Vassilevich formula more carefully, the Omega^3 term
appears with coefficient:

    In (4pi)^{d/2} * a_6: ... + (1/45) tr(Omega_{ij} Omega_{jk} Omega_{ki}) + ...

Wait -- this needs to be verified. The exact coefficient depends on the reference.
Let me note this as a **critical verification item**.

### 4.6 Assembled Formula (Provisional)

    (4pi)^4 * 7! * a_6^{red}(tau) =
        [16 * (35/9) + 98] R^3
      + [16 * (-14/3) - 112] R |Ric|^2
      + [16 * (14/3) + 112 - 84 - 140] R K
      + 16 * (-208/9) Ric^3
      + 16 * (-64/3) I_5
      + 16 * (16/3) I_6
      + [16 * (44/9) + 336] I_7
      + 16 * (80/9) I_8
      - 336 R_{ab} M_{ab}
      + Omega3_part

Computing the R^3 coefficient: 16*(35/9) + 98 = 560/9 + 98 = 62.22 + 98 = 160.22
  = 560/9 + 882/9 = 1442/9

R|Ric|^2 coefficient: 16*(-14/3) - 112 = -224/3 - 112 = -224/3 - 336/3 = -560/3

RK coefficient: 16*(14/3) + 112 - 84 - 140 = 224/3 + 112 - 84 - 140 = 224/3 - 112
  = 224/3 - 336/3 = -112/3

Ric^3 coefficient: 16*(-208/9) = -3328/9

I_5 coefficient: 16*(-64/3) = -1024/3

I_6 coefficient: 16*(16/3) = 256/3

I_7 coefficient: 16*(44/9) + 336 = 704/9 + 3024/9 = 3728/9

I_8 coefficient: 16*(80/9) = 1280/9

New Omega trace: -336 * R_{ab} M_{ab}

**CRITICAL WARNING:** These assembled coefficients are PROVISIONAL. The exact
values of the a_6 coefficients from Vassilevich/Gilkey/Avramidi differ between
references due to:
1. Different conventions for the overall (4pi)^{d/2} and n! prefactors.
2. Different sign conventions for E (some use P = Delta + E, others P = -Delta + E).
3. Whether the "trace" includes dim_S or not.

**The implementation MUST include an independent verification (see Section 6).**

---

## 5. Pseudocode

```python
"""
s26_p3_a6_computation.py
Session 26 Priority 3: Seeley-DeWitt a_6 on Jensen-deformed SU(3)
"""

import numpy as np

# =====================================================================
# STEP 0: Load infrastructure
# =====================================================================
# Load: r20a_riemann_tensor.npz (R_abcd, Ric, R_scalar, K at 21 tau values)
# Load: s23c_fiber_integrals.npz (Ric_sq, K_kretschner, a4_geom at 21 tau)
# Load: tier1_dirac_spectrum.py (build_cliff8 for gamma matrices)

R_data = np.load('tier0-computation/r20a_riemann_tensor.npz')
tau_all = R_data['tau']          # (21,)  [0.0, 0.1, ..., 2.0]
R_abcd_all = R_data['R_abcd']   # (21, 8, 8, 8, 8)
Ric_all = R_data['Ric']         # (21, 8, 8)
R_scalar_all = R_data['R_scalar']  # (21,)
K_all = R_data['K']              # (21,)

# We only need tau in [0, 0.30], so indices 0-3 (tau = 0.0, 0.1, 0.2, 0.3)
# But compute at all 21 for completeness.

# =====================================================================
# STEP 1: Build Clifford algebra and gamma^{ab} matrices
# =====================================================================

from tier1_dirac_spectrum import build_cliff8
gammas = build_cliff8()  # list of 8 matrices, each 16x16

# Precompute gamma^{ab} = (1/2)[gamma^a, gamma^b]
gamma_ab = np.zeros((8, 8, 16, 16), dtype=complex)
for a in range(8):
    for b in range(8):
        gamma_ab[a, b] = 0.5 * (gammas[a] @ gammas[b] - gammas[b] @ gammas[a])

# =====================================================================
# STEP 2: Compute cubic curvature invariants at each tau
# =====================================================================

def compute_cubic_invariants(R_abcd, Ric, R_scalar, K):
    """Compute all 8 cubic curvature invariants from Riemann and Ricci."""

    # Products of known scalars
    R3 = R_scalar**3
    R_Ric2 = R_scalar * np.sum(Ric**2)
    R_K = R_scalar * K

    # Ric^3 = tr(Ric @ Ric @ Ric) = R_{ab} R_{bc} R_{ca}
    Ric3 = np.einsum('ab,bc,ca->', Ric, Ric, Ric)

    # I_5 = R_{ab} R_{cdea} R_{cdeb}
    I5 = np.einsum('ab,cdea,cdeb->', Ric, R_abcd, R_abcd)

    # I_6 = R_{ab} R_{acde} R_{bcde}
    I6 = np.einsum('ab,acde,bcde->', Ric, R_abcd, R_abcd)

    # I_7 = R_{abcd} R_{abef} R_{cdef}
    I7 = np.einsum('abcd,abef,cdef->', R_abcd, R_abcd, R_abcd)

    # I_8 = R_{abcd} R_{aecf} R_{bedf}
    I8 = np.einsum('abcd,aecf,bedf->', R_abcd, R_abcd, R_abcd)

    return {
        'R3': R3, 'R_Ric2': R_Ric2, 'R_K': R_K,
        'Ric3': Ric3, 'I5': I5, 'I6': I6, 'I7': I7, 'I8': I8
    }

# =====================================================================
# STEP 3: Compute spin connection traces
# =====================================================================

def compute_omega_traces(R_abcd, Ric, gamma_ab):
    """Compute fiber traces involving spin connection Omega."""
    n = 8
    dim_S = 16

    # Omega[i,j] = (1/4) R_{ijkl} gamma^{kl}  (16x16 matrix for each i,j)
    # Build Omega as (8,8,16,16) array
    Omega = np.zeros((n, n, dim_S, dim_S), dtype=complex)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    Omega[i, j] += 0.25 * R_abcd[i, j, k, l] * gamma_ab[k, l]

    # tr_S(Omega^2) = sum_{ij} tr(Omega[i,j] @ Omega[i,j])
    # Expected: -2K (verified in s23c)
    Omega2_trace = 0.0
    for i in range(n):
        for j in range(n):
            Omega2_trace += np.trace(Omega[i, j] @ Omega[i, j]).real

    # M_{ab} = sum_{icd} R_{aicd} R_{bicd} (for the R_{ab} Omega_{ai} Omega_{bi} trace)
    M_ab = np.einsum('aicd,bicd->ab', R_abcd, R_abcd)
    Ric_M = np.einsum('ab,ab->', Ric, M_ab)

    # tr_S(R_{ab} Omega_{ai} Omega_{bi}) -- compute directly to cross-check
    Ric_OmOm = 0.0
    for a in range(n):
        for b in range(n):
            for i in range(n):
                Ric_OmOm += Ric[a, b] * np.trace(Omega[a, i] @ Omega[b, i]).real

    # tr_S(R_{abcd} Omega_{ab} Omega_{cd}) -- compute directly
    Riem_OmOm = 0.0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    Riem_OmOm += R_abcd[a,b,c,d] * np.trace(Omega[a,b] @ Omega[c,d]).real

    # tr_S(Omega_{ij} Omega_{jk} Omega_{ki}) -- cubic trace
    Omega3_trace = 0.0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Omega3_trace += np.trace(Omega[i,j] @ Omega[j,k] @ Omega[k,i]).real

    # tr_S(E * Omega^2) = (R/4) * tr_S(Omega^2) [scalar, already computed]

    return {
        'Omega2_trace': Omega2_trace,      # expected: -2K
        'Ric_OmOm': Ric_OmOm,             # tr_S(R_{ab} Omega_{ai} Omega_{bi})
        'Riem_OmOm': Riem_OmOm,           # tr_S(R_{abcd} Omega_{ab} Omega_{cd})
        'Omega3_trace': Omega3_trace,       # tr_S(Omega_{ij} Omega_{jk} Omega_{ki})
        'M_ab': M_ab,
        'Ric_M': Ric_M,
    }

# =====================================================================
# STEP 4: Assemble a_6^{red}(tau)
# =====================================================================

def assemble_a6(cubic_inv, omega_traces, R_scalar, K,
                coefficients):
    """
    Assemble a_6^{red} from cubic invariants and omega traces.

    coefficients: dict of verified numerical coefficients from Gilkey/Vassilevich.
    """
    # Universal part (x dim_S = 16)
    U = 16 * (
        coefficients['c_R3'] * cubic_inv['R3']
      + coefficients['c_RRic2'] * cubic_inv['R_Ric2']
      + coefficients['c_RK'] * cubic_inv['R_K']
      + coefficients['c_Ric3'] * cubic_inv['Ric3']
      + coefficients['c_I5'] * cubic_inv['I5']
      + coefficients['c_I6'] * cubic_inv['I6']
      + coefficients['c_I7'] * cubic_inv['I7']
      + coefficients['c_I8'] * cubic_inv['I8']
    )

    # E part (traced, using E = R/4 * Id_16)
    E = (
        coefficients['c_R2E'] * R_scalar**3 / 4 * 16        # 42 R^2 E
      + coefficients['c_Ric2E'] * cubic_inv['R_Ric2'] / 4 * 16  # -28 |Ric|^2 E
      + coefficients['c_KE'] * cubic_inv['R_K'] / 4 * 16    # 28 K E
      + coefficients['c_RE2'] * R_scalar * (R_scalar/4)**2 * 16  # -140 R E^2
      + coefficients['c_E3'] * (R_scalar/4)**3 * 16          # 280 E^3
    )

    # Omega part (direct numerical traces)
    Om = (
        coefficients['c_ROm2'] * R_scalar * omega_traces['Omega2_trace']
      + coefficients['c_RicOm2'] * omega_traces['Ric_OmOm']
      + coefficients['c_RiemOm2'] * omega_traces['Riem_OmOm']
      + coefficients['c_EOm2'] * (R_scalar/4) * omega_traces['Omega2_trace']
      + coefficients['c_Om3'] * omega_traces['Omega3_trace']
    )

    # Total (divide by (4pi)^4 * 7! for the final reduced coefficient)
    a6_red = (U + E + Om) / ((4*np.pi)**4 * 5040)

    return a6_red

# =====================================================================
# STEP 5: V_spec^(6) potential and minimum search
# =====================================================================

def V_spec_6(tau_arr, a2_arr, a4_arr, a6_arr, c2, c4, c6):
    """Compute 3-term spectral action potential."""
    return c2 * a2_arr + c4 * a4_arr + c6 * a6_arr

# Scan over (c4/c2, c6/c2) parameter space
# rho = c4/c2 in [0.001, 0.5]    (same as Session 24a)
# rho6 = c6/c2 in [0.0001, 0.1]  (new parameter)
# Search for minima using finite-difference dV/dtau

# =====================================================================
# STEP 6: B-1 minimum test
# =====================================================================

# The B-1 analysis found structure (a minimum) in V_spec under certain
# conditions. Check whether this minimum PERSISTS when a_6 is included.
#
# Specifically:
# 1. At the B-1 minimum location tau_B1 (from s26_baptista_bridge.py):
#    is V_spec^(6)'(tau_B1) = 0 and V_spec^(6)''(tau_B1) > 0?
# 2. For what range of (rho, rho6) does a minimum exist?
# 3. Is the minimum location tau_min stable against rho6 variation?

# =====================================================================
# STEP 7: Verification at tau=0 (bi-invariant SU(3))
# =====================================================================

# At tau=0, SU(3) with the bi-invariant metric is a symmetric space.
# The curvature simplifies: R_{abcd} = -(1/4) f_{abe} f_{cde}
# All cubic invariants can be computed analytically.
#
# Known result for bi-invariant SU(n):
#   R = n(n^2-1)/(4*vol_factor)  [depends on normalization]
#   Ric_{ab} = (1/4) g_{ab}      [Einstein manifold]
#   |Ric|^2 = n^2-1 / 16 * d    [d = dim SU(n)]
#
# Cross-check: Ric^3 = tr(Ric^3) = n * (Ric eigenvalue)^3
# For SU(3) with our normalization: Ric = (1/4)*Id_8 (at tau=0)
# So Ric^3 = 8 * (1/4)^3 = 8/64 = 1/8 = 0.125
#
# Verify I_7, I_8 against the bi-invariant formula:
#   R_{abcd} = -(1/4) sum_e f_{abe} f_{cde}
#
# I_7 = sum_{abcdef} R_{abcd} R_{abef} R_{cdef}
#     = -(1/64) sum f_{abg} f_{cdg} * f_{abh} f_{efh} * f_{cdi} f_{efi}
#     = -(1/64) * [algebraic expression in structure constants of su(3)]
#
# This MUST be verified numerically as a self-consistency check.

# =====================================================================
# STEP 8: Output
# =====================================================================

# Save: s26_p3_a6.npz with keys:
#   tau, a6_red, cubic_invariants (all 8), omega_traces,
#   V_spec_6 at grid of (rho, rho6) values,
#   minimum_locations, minimum_depths
#
# Plot: s26_p3_a6.png with panels:
#   (a) a_6^{red}(tau) vs tau
#   (b) V_spec^(6)(tau) at selected (rho, rho6)
#   (c) Minimum location tau_min vs rho6 (at fixed rho)
#   (d) Phase diagram: (rho, rho6) regions with/without minimum
```

---

## 6. Verification Strategy

### 6.1 Bi-Invariant Check (tau=0)

At tau=0, the Jensen metric reduces to the bi-invariant metric on SU(3).
All curvature quantities are computable from the structure constants alone.
For the bi-invariant metric with our normalization (R(0) = 2, |Ric|^2(0) = 0.5,
K(0) = 0.5):

**Cubic invariants at tau=0:**
- R^3 = 8
- R*|Ric|^2 = 1.0
- R*K = 1.0
- Ric^3 = tr((1/4 * Id)^3) * 8 = 8*(1/64) = 0.125
- I_5, I_6, I_7, I_8: compute numerically from R_{abcd}(0) and verify against
  the bi-invariant formula R_{abcd} = -(1/4) f_{abe} f_{cde}.

**Omega trace check:**
- tr_S(Omega^2)(0) should equal -2*K(0) = -1.0.

**a_6 at tau=0:** Compare against known results for compact Lie groups
(e.g., Bernstein-Gelfand 1969, or direct computation from heat kernel of
Casimir operator on SU(3)).

### 6.2 Dimensional Consistency

All terms in a_6 must have dimensions of [curvature]^3 = [length]^{-6}.
In our units where the metric is O(1), this means all cubic invariants are
dimensionless numbers of order O(1) at tau=0 and grow exponentially with tau.

### 6.3 Symmetry Checks

- I_7 and I_8 must be real (Riemann tensor is real).
- All Omega traces must be real (D_K is self-adjoint).
- a_6(tau) must be smooth (analytic in tau since it's an algebraic function
  of exponentials e^{k*tau}).

### 6.4 Cross-Check: Heat Kernel Fit

From `c1_seeley_dewitt_convergence.py`, the heat kernel Tr(e^{-t D_K^2}) is
available at max_pq_sum = 6. The coefficient of t^{-1} (i.e., t^{(6-d)/2}
= t^{-1} for d=8) in the small-t expansion gives a_6 (up to (4pi)^{-4}).

Fit the numerically computed heat kernel to:

    t^4 * K(t) = a_0 + a_2 t + a_4 t^2 + a_6 t^3 + ...

and extract the t^3 coefficient. Compare with the analytic a_6 from our
formula. Agreement to within the truncation error of max_pq_sum=6 validates
the computation.

---

## 7. Expected Computational Cost

| Step | Operations per tau | Time estimate |
|------|-------------------|---------------|
| Load .npz files | I/O | < 0.1s |
| Build Clifford algebra | 8 matrices 16x16 | < 0.01s |
| Build gamma^{ab} | 64 matrix products | < 0.01s |
| Cubic invariants (einsum) | 5 * O(8^6) | < 0.1s per tau |
| Build Omega (8x8x16x16) | O(8^4 * 16^2) | < 0.1s per tau |
| Omega^2 trace | O(8^2 * 16^2) | < 0.01s per tau |
| R_{ab}Omega Omega trace | O(8^3 * 16^2) | < 0.01s per tau |
| R_{abcd}Omega Omega trace | O(8^4 * 16^2) | < 0.1s per tau |
| Omega^3 trace | O(8^3 * 16^3) | < 0.1s per tau |
| Assembly + V_spec | O(1) per (tau, rho, rho6) | < 0.001s |
| Minimum search | O(21 * n_rho * n_rho6) | < 1s |
| Verification | same as above at tau=0 | < 0.5s |
| Plotting | matplotlib | < 2s |
| **Total for 21 tau values** | | **< 15 seconds** |

GPU is not needed. This is a purely algebraic computation on 8x8x8x8 tensors.

---

## 8. What "B-1 Minimum Persists" Means Quantitatively

### 8.1 Background

The B-1 analysis (`s26_baptista_bridge.py`) investigates whether the 12D
spectral action (on M^4 x SU(3)) produces a kappa_12D parameter large enough
to bridge V_Baptista to the spectral action framework. The key question for
Priority 3 is: does the a_6 term create or destroy structure in V_spec?

### 8.2 Test Criteria

**A. Minimum existence test:**
For a given (rho, rho6), does V_spec^(6)(tau) have a local minimum at some
tau_min in [0, 0.30]?

Quantitative criterion:
- dV_spec^(6)/dtau = 0 at tau = tau_min
- d^2 V_spec^(6)/dtau^2 > 0 at tau = tau_min (stable minimum)

**B. Minimum depth test:**
If a minimum exists, is it deep enough to matter? Define:

    delta_V = V_spec^(6)(tau_boundary) - V_spec^(6)(tau_min)

where tau_boundary = max(tau_min - 0.1, 0) or tau_boundary = min(tau_min + 0.1, 0.3).

Criterion: delta_V > 0 (minimum is below the boundary values). If delta_V < 0,
the "minimum" is a shallow saddle and physically irrelevant.

**C. B-1 bridge test:**
At the B-1 minimum location, does the a_6 correction:
1. STRENGTHEN the minimum (deepen delta_V)?
2. WEAKEN the minimum (reduce delta_V toward zero)?
3. DESTROY the minimum (V becomes monotone)?

Report the fractional change: delta_V_with_a6 / delta_V_without_a6 for each
(rho, rho6) pair.

**D. Physical window test:**
Does the minimum fall in the tau range [0.10, 0.20] where phi_paasch lives
(tau = 0.15)?

### 8.3 Parameter Space to Scan

| Parameter | Range | Grid | Points |
|-----------|-------|------|--------|
| rho = c4/c2 | [0.001, 0.5] | log-spaced | 20 |
| rho6 = c6/c2 | [-0.1, 0.1] | linear | 41 |
| tau | [0, 0.30] | step 0.01 | 31 (interpolated from 21-point grid) |

Note: rho6 can be NEGATIVE (since f_{-2} can have either sign depending on the
test function f). The sign of rho6 determines whether a_6 contributes a
positive or negative correction to V_spec.

Total parameter evaluations: 20 * 41 * 31 = 25,420. At O(1) microsecond each
(just algebraic evaluation of the assembled formula), this takes < 0.1 seconds.

---

## 9. Potential Numerical Pitfalls

### 9.1 Cancellations in Cubic Invariants

The eight cubic invariants can have opposite signs and comparable magnitudes,
leading to catastrophic cancellation in the assembled a_6. At tau=0 (bi-invariant),
the invariants are all O(1). At large tau, they grow as e^{12*tau} (from K^{3/2}
scaling). The cancellation risk is highest at tau=0 where the invariants are
comparable.

**Mitigation:** Compute all invariants in double precision (float64). The Riemann
tensor from `r20a_riemann_tensor.npz` is verified at machine epsilon (~1e-15),
so cubic products should be accurate to ~1e-14.

### 9.2 Complex Phases in Omega Traces

The spin connection Omega_{ij} involves gamma matrices, which may be stored as
complex matrices (from `build_cliff8()`). The traces of Omega products must be
real for self-adjoint D_K. Verify:

    |Im(tr(Omega @ Omega @ ...))| < 1e-13

If the imaginary part exceeds this, there is a sign or convention error.

### 9.3 Einsum Memory

The triple einsum `np.einsum('abcd,aecf,bedf->', R, R, R)` for I_8 requires
numpy to contract over 8 indices on three rank-4 tensors. On an 8-dimensional
space, the intermediate array is at most 8^4 = 4096 elements. No memory issues.

However, if `np.einsum` creates a temporary array of shape (8,8,8,8,8,8,8,8)
= 16.7M elements, this is still only ~134 MB in float64. Acceptable on a
128 GB machine. Use `optimize='optimal'` flag in einsum to minimize temporaries.

### 9.4 Convention Ambiguity in a_6 Coefficients

**THE BIGGEST RISK.** The literature on a_6 coefficients has multiple conventions
and known errata. The coefficients from Gilkey (1995), Vassilevich (2003),
Avramidi (2000), and Branson-Gilkey (1990) must be cross-compared term by term.

**Mitigation strategy:**
1. Code the formula with symbolic coefficient names (not hardcoded numbers).
2. Implement the bi-invariant SU(3) check as the FIRST validation.
3. Cross-check the total a_6(tau=0) against the heat kernel fit from
   `c1_seeley_dewitt_convergence.py` (which extracts a_6 numerically).
4. If the two disagree, iterate on the coefficient values until agreement.

### 9.5 V-1 Dominance

The V-1 closure established that a_4 dominates a_2 by a factor of 1000:1 at tau=0.
The a_6 term enters with an additional power of Lambda^{-2}, so its physical
weight is:

    a_6 contribution / a_4 contribution ~ (1/Lambda^2) * a_6 / a_4

For Lambda >> 1 (Planck scale cutoff), this ratio is SMALL. The a_6 correction
is perturbatively suppressed. A minimum from a_6 alone requires |rho6 * a_6| to
compete with |rho * a_4|, which may require unnaturally large rho6.

**This is the most likely outcome: a_6 does NOT create a minimum, and the V-1
closure remains in force.** The computation is still worth performing to close
this possibility quantitatively.

---

## 10. Files and Dependencies

### 10.1 Input Files

| File | Arrays Used |
|------|-------------|
| `tier0-computation/r20a_riemann_tensor.npz` | `tau`, `R_abcd` (21,8,8,8,8), `Ric` (21,8,8), `R_scalar` (21,), `K` (21,) |
| `tier0-computation/s23c_fiber_integrals.npz` | `Ric_sq` (21,), `K_kretschner` (21,), `a4_geom` (21,) |
| `tier0-computation/s24a_vspec.npz` | `V_spec_rho_*` (21,) for comparison |
| `tier0-computation/tier1_dirac_spectrum.py` | `build_cliff8()`, `su3_generators()`, etc. |
| `tier0-computation/sd20a_seeley_dewitt_gate.py` | Analytic R(tau), Ric^2(tau), K(tau) formulas |

### 10.2 Output Files

| File | Contents |
|------|----------|
| `tier0-computation/s26_p3_a6.npz` | All computed invariants + V_spec^(6) + minima data |
| `tier0-computation/s26_p3_a6.png` | 4-panel diagnostic plot |

### 10.3 Script

| File | Purpose |
|------|---------|
| `tier0-computation/s26_p3_a6_computation.py` | Main computation script |

Python invocation: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s26_p3_a6_computation.py`

---

## 11. Open Questions for Implementation

1. **Exact a_6 coefficients:** The provisional coefficients in Section 4.6 MUST
   be verified against Vassilevich (2003) Table 2 and Avramidi (2000) eq 6.58.
   The implementer should read these references and extract the derivative-free
   terms explicitly.

2. **Omega^3 coefficient:** The coefficient of tr_S(Omega^3) in a_6 needs to
   be extracted from the references. This term was not fully pinned down in
   the present design. It involves a 6-gamma trace that is computable numerically.

3. **Sign of rho6:** The moment f_{-2} = integral f(u) u^{-2} du depends on
   the choice of test function f. For the standard Chamseddine-Connes f(u) =
   chi_{[0,1]}(u), all moments f_k are positive for k >= 0, but f_{-2} is
   negative (since f(u) = 0 for u > 1 and the integral over u^{-2} converges
   only because of the UV cutoff). This means c_6 < 0 and rho6 < 0 in the
   physical regime. The scan should include both signs.

4. **Comparison with Session 24a V-1 result:** The V-1 closure was established
   for the two-term potential (a_2 + a_4). If a_6 does not create a minimum
   for any physical (rho, rho6), this strengthens V-1 to a three-term closure.
   If a minimum appears for some rho6, this REOPENS the spectral action path
   (with a BF penalty for the additional free parameter).
