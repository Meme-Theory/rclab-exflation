# 2012 Moduli spaces abelian vortices Kahler manifolds

**Source:** `11_2012_Moduli_spaces_abelian_vortices_Kahler_manifolds.pdf`

---

arXiv:1211.0012v2 [math.DG] 20 Aug 2013       Moduli Spaces of Abelian Vortices on
                                                             K�ahler Manifolds

                                                                               J. M. Baptista
                                                                                August 2013

                                                                                  Abstract

                                         We consider the self-dual vortex equations on a positive line bundle L  M over a compact
                                         Ka�hler manifold of arbitrary dimension. When M is simply connected, the moduli space
                                         M of vortex solutions is a projective space. When M is an abelian variety, M is the
                                         projectivization of the Fourier-Mukai transform L^  M^ over the dual variety. We extend
                                         this description of the moduli space to the abelian GLSM, i.e. to vortex equations with
                                         a torus gauge group acting linearly on a complex vector space. After establishing the
                                         Hitchin-Kobayashi correspondence appropriate for the general abelian GLSM, we give
                                         explicit descriptions of the moduli space M in the case where the manifold M is simply
                                         connected or is an abelian variety. In these examples we compute the Ka�hler class of the
                                         natural L2-metric on the moduli space. In the simplest cases we compute the volume and
                                         total scalar curvature of M. Finally, we note that for abelian GLSM the moduli space M
                                         is a compactification of the space of holomorphic maps from M to toric targets, just as in
                                         the usual case of M being a Riemann surface. This leads to various natural conjectures,
                                         for instance explicit formulae for the volume of the space of maps CPm  CPn.

                                         Keywords : Vortex equations; moduli space; Ka�hler manifold; L2-metric; holomorphic maps;
Contents

1 Introduction                                                        1

2 Vortices on line bundles                                            4

2.1 General description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2 Case of simply connected manifolds . . . . . . . . . . . . . . . . . . . . . . 5

2.3 Case of abelian varieties . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

3 Vortices in abelian GLSM                                            12

3.1 General results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

3.2 Case of simply connected manifolds . . . . . . . . . . . . . . . . . . . . . . 20

3.3 Case of abelian varieties . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24

4 K�ahler class and volume of the L2-metric                           27

4.1 Line bundles over simply connected manifolds . . . . . . . . . . . . . . . . 27

4.2 Line bundles over abelian varieties . . . . . . . . . . . . . . . . . . . . . . . 29

4.3 Abelian GLSM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

4.4 Abelian GLSM with polynomial constraints . . . . . . . . . . . . . . . . . 33

5 Holomorphic maps to toric manifolds                                 34

5.1 Vortices and maps to projective space . . . . . . . . . . . . . . . . . . . . . 34

5.2 Vortices and maps to toric manifolds . . . . . . . . . . . . . . . . . . . . . 36

5.3 Conjectures about the L2-metrics . . . . . . . . . . . . . . . . . . . . . . . 41

A Appendices                                                          43

A.1 Limits of the vortex equations . . . . . . . . . . . . . . . . . . . . . . . . . 43

A.2 Auxiliary lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

1 Introduction

The simplest type of vortex equations on a Ka�hler manifold is defined on a hermitian
line bundle L - M over the manifold. The variables are a unitary connection A and a
smooth section  of L. To each pair (A, ) one associates a positive energy

              E(A, ) =       1    |FA|2  +  |dA|2  +  e2  ||2 -  2 ,  (1.1)
                            2 e2                      2
                        M

where  and e2 are positive constants, dA is the covariant derivative, and FA denotes
the curvature form of the connection A. All the norms are taken with respect to the

                                         1
hermitian metric on L and the Ka�hler metric on M. In two dimensions, this energy
functional coincides with the usual static energy of the abelian Higgs model. Assuming
that M is compact, a standard Bogomolny-type argument [Bra1] shows that the energy
is bounded below by a constant,

                          E(A, )  Evortex ,                                   (1.2)

and that this minimum is attained precisely when the pair (A, ) satisfies the so-called
self-dual vortex equations. The equations read

                     �A = 0                   =0                              (1.3)
                     FA - ie2 ||2 -                                           (1.4)
                     FA0,2 = 0 ,                                              (1.5)

where FA represents the contraction of the curvature with the Ka�hler form M on M.
When M is a Riemann surface, FA = FA is just the Hodge-dual and the last equation
is trivially satisfied, since every 2-form has vanishing (0,2) Dolbeault component. The

energy of a vortex solution on a m-dimensional compact Ka�hler manifold is given by

Evortex =         i  1)!  FA    Mm-1  +  2e2    1   2)!  FA    FA    Mm-2  .  (1.6)
              (m -                            (m -
           M

It does not depend on the particular solution (A, ) because the cohomology class [FA] is
just the Chern class -2i c1(L), a topological invariant of the line bundle L.

    In this article we will study the moduli space of solutions these vortex equations and
of another, more general, flavour of vortex equations: those of the abelian gauged lin-
ear sigma-model (GLSM). These are written down in (3.1). All these equations and
moduli spaces have been widely studied in the case where M is a Riemann surface
[JT, Bra1, Gar, MP, MS, We]. In fact, in two dimensions, the subject has advanced
much further than the abelian case, with an impressive body of work about non-abelian
vortex equations, i.e. equations defined on vector bundles over M (see for instance
[Bra2, Tha, BDGW, EINOS, To, Ba3] and the references therein), and vortex equations
on bundles with non-linear fibres ([CGMS, Wo, Zi] and the references therein). When M
is a higher-dimensional Ka�hler manifold, however, our understanding of vortex moduli
spaces is much less thorough. Important results have already been obtained, such as a
version of the Hitchin-Kobayashi correspondence [Bra1, Ban, Mu]. In the abelian case,
the simplest vortex equations were related to invariant Hermitian-Einstein connections
and their moduli spaces of solutions were described as spaces of divisors on M [Gar, Ba2].
Nonetheless, for higher-dimensional M there seems to be a general lack of explicit descrip-
tions of the moduli spaces as global manifolds, even in the case of the simplest abelian
vortices. Here we try to partially fill in this gap.

    In Section 2 of this article we go through the basic analysis for the simplest abelian
vortices, i.e. for equations (1.3)-(1.5) defined on a line bundle L. In this case, the main
result of [Bra1] implies that the vortex moduli space M is a projective space when M
is simply connected. When M is an abelian variety, the moduli space is a projective

                                2
bundle over dual variety M^ ; more precisely, M is the projectivization of the Fourier-
Mukai transform L^  M^ of the original line bundle L. All the results here are either well
known, or are relatively simple calculations using standard technology. Nevertheless, we
feel that this Section gives a useful overview of the techniques developed ahead, besides
being important to introduce the necessary notation about vortex moduli spaces, abelian
varieties and the universal bundle.

    In Section 3 we consider vortex solutions of the general abelian GLSM. The main
results are Theorems 3.2 and 3.3, which describe the Hitchin-Kobayashi correspondence
for the GLSM and interpret the general  -stability of [Ban, Mu] in this setting. These
results are applied in Sections 3.2 and 3.4, where we show that the vortex moduli space
of the GLSM is a toric orbifold for simply connected M, and that, for abelian varieties,
it is a toric fibration over a cartesian product of copies of the dual variety. We also work
out the topology of the natural "universal" bundle over the product M � M, a result
necessary for the cohomology calculations in Section 4.

    General arguments say that vortex moduli spaces have a natural Ka�hler structure
[Mu]. The complex structure on M is canonically induced by the complex structures on
M and on L. The compatible Ka�hler metric M can be described roughly as follows.
If (At, t) is a one-parameter family of vortex solutions, a tangent vector to this path is
represented by the derivative  � a section of L � and the derivative A � a 1-form on
M. These derivatives satisfy the linearized vortex equations. The standard metric on the
moduli space M is then determined by the L2-norm

A +   2  =      1   |A |2  +  | |2  Mm  (1.7)
      M        4e2                  m!
            M

applied to the horizontal part of the tangent vector, i.e., to the component of (A, )
perpendicular to all vectors tangent to gauge transformations. This metric on M has a
well known interpretation as the reduced metric on a (infinite-dimensional) symplectic
quotient. In physics, it gives relevant information about the low-energy dynamics of
vortices [MS]. It is very hard in general to obtain explicit knowledge about M. Our
work in Section 4 is to compute the cohomology class [M] of the Ka�hler form on the
moduli space. We are able to do so both for the simpler model of vortices on line bundles
and for the more general abelian GLSM. The base M, as always, can either be simply
connected or be an abelian variety. In the simplest examples, our knowledge of the Ka�hler
class [M] and of the cohomology ring of M allows us to write down explicit formulae
for the volume and total scalar curvature of (M, M). The results of this Section extend
formulae obtained by Manton and Nasir [MN] and the author [Ba4] in the case where M
is a Riemann surface. We rely heavily on a description of M originally due to Perutz
[Pe] and generalized in [BS, Ba4].

    In the final part of the paper, Section 5, we look at the relation between vortex moduli
spaces in abelian GLSM and spaces of holomorphic maps M  X to toric targets. This is
a very familiar and well studied story in the case where M is a Riemann surface. In fact, in
two dimensions, one of the main motivations to consider abelian GLSM is that its vortex
moduli space is a natural compactification of the space of holomorphic curves in toric
varieties, and hence can be used to compute Gromov-Witten invariants of these varieties

               3
[Wi, MP, H-al]. Much less attention has been devoted to this line of ideas when M is a
higher-dimensional Ka�hler manifold. Since many of the techniques extend readily from the
two dimensional case, in Section 5 we go through this natural generalization, describing the
natural embedding H  M of the (generally non-compact) space of holomorphic maps
into the corresponding (compact) vortex moduli space (Proposition 5.1). One notable
difference from the two dimensional case is that H does not generally embed as an open
and dense subset of M. Roughly speaking, this will happen only if the dimension of M
is small enough compared to the dimension of the target X (Proposition 5.5) and the line
bundles of the GLSM have enough holomorphic sections.

    One of our original motivations to study the embedding H  M is to compare the

natural Ka�hler metrics on both these spaces. Recall that H is a space of maps between
Riemannian manifolds, and hence has a natural L2-metric H. It is natural to ask if there
is any relation between H and the pullback of the vortex metric M by the embedding
H  M. Following [Ba4], in Section 5.3 we conjecture that the metric H is the pointwise
limit of M when the gauge coupling constant e2 goes to infinity.1 In particular, when H
embeds as an open dense subset of M, we should have that

  Vol (H, H)             =   lim  Vol (M, M)   .

                            e2+

Taking the limit of the explicit formulae for Vol (M, M) obtained in Section 4, we can
thus propose a few conjectural formulae for Vol (H, H), as well as for the total scalar
curvature of (H, H). See for instance the Example in Section 5.3. It seems non-trivial
to check these formulae by direct computations on H, since this space is not compact

and the metric H cannot in general be compactified as a smooth metric (it can have
unbounded scalar curvature). In the very special instances where direct computations

have been performed [Spe], they agreed with analogous conjectures made in [Ba4].

2 Vortices on line bundles

2.1 General description

The simplest vortex equations on a m-dimensional Ka�hler manifold are defined on a
hermitian line bundle L  M. They were written down in (1.3)-(1.5). From equation
(1.5) we see that a necessary condition for the existence of vortex solutions is that

      c1(L)  H1,1(M, C) ,                                                         (2.1)

i.e. that L admits a holomorphic structure. Assuming that M is compact, the integral of
the second equation over (M, M ) shows that another necessary condition for the existence
of solutions with non-trivial section  is that

  :=   Vol M             -  2 m  c1(L)  Vol M  >  0,                              (2.2)
                             e2   [M ]

1This conjecture has now been proved in the case of maps from Riemann surfaces to projective space.
 The proof is presented in [Liu], and appeared on the arXiv after the first version of the present article.

                            4
where denotes the component parallel to the vector [M ] in the euclidean space H2(M, R).
See Section 3.1 for more details. The real number  will be called the stability parameter.
When these two conditions are satisfied, we can have plenty of vortex solutions, as follows
from the basic result of Bradlow:

Proposition 2.1. [Bra1] Assume that condition (2.2) is satisfied. Then for any pair
(A, ) with non-zero  satisfying �A = 0 and FA0,2 = 0, there exists a gauge transforma-
tion g : M  C, unique up to multiplication by U(1)-gauge transformations, such that
(g(A), g()) is a solution of the full vortex equations. All vortex solutions can be obtained
in this way.

So the set of full vortex solutions up to U(1)-gauge transformations coincides with the set

of solutions of (1.3) and (1.5) up to C-gauge transformations. This is an example of a

Hitchin-Kobayashi correspondence. As is well-known, there is also a bijective correspon-
                                 if AMissasuticshfyaincgoFnnA0,e2c=tio0n,anthdenho�loAmor=phi0c
dence between connections on L                                                                   structures on
the line bundle [Ko]. Moreover,                                                                  if and only if

the section  is holomorphic with respect to the holomorphic structure on L induced by

A. It follows that the moduli space M of vortex solutions coincides the space of pairs

"holomorphic structure plus a non-zero holomorphic section" on L, up to isomorphism.

It is also a standard fact that such pairs are in one-to-one correspondence with effective

divisors on M representing the cohomology class c1(L). So we have:

Proposition 2.2. [Bra1] Let M be a compact Ka�hler manifold and assume that condition
(2.2) is satisfied. Pick any effective divisor D on M representing the homology class
Poincar�e-dual to c1(L). Then there is a solution (A, ) of the vortex equations such that
D coincides with the divisor of the zero set of  regarded as a holomorphic section of
L. This solution is unique up to U(1)-gauge transformations. All vortex solutions are
obtained in this way.

Thus choosing a vortex solution is equivalent to picking an effective divisor of hypersur-
faces on M. When M is a Riemann surface, solutions are determined by a choice of d
points on M, where d is the degree of L. In other words, they are determined by a point
in the symmetric product SymdM. This description of the moduli space as a space of
divisors is possible for vortices on line bundles, also called local vortices, but does not in
general extend to other types of vortices.

2.2 Case of simply connected manifolds

Moduli space

When the Ka�hler base M is simply connected, besides describing the vortex moduli space
as a space of divisors, it is easy to describe M as a complex manifold. The arguments
are all very standard.

Proposition 2.3. Let M be a m-dimensional, simply connected, compact Ka�hler man-
ifold, and let L  M be a hermitian line bundle satisfying conditions (2.1) and (2.2).

                                                        5
Denote by H0(M; L) the vector space of holomorphic sections of L equipped with its unique
holomorphic structure. Then the moduli space of vortex solutions is the projective space

                                          M  P H0(M; L) .

In particular, M is empty if L does not have any non-zero holomorphic sections.

Proof. The usual short exact sequence of sheaves implies, after standard identifications
([GH]), the exact sequence in the cohomology

                    H0,1(M, C) - Pic(M ) --c1 H2(M, Z) -p-roj. H0,2(M, C) .

Since M is simply connected, the space on the left is zero. Since c1(L)  H1,1(M, C) 
H2(M, Z), the exactness of the sequence implies that there is precisely one holomorphic
structure on L. Scalar multiplication of a section  by a constant   C corresponds to
a (constant) complex gauge transformation, since these leave the holomorphic structure
(or the Chern connection) invariant. So the moduli space of Bradlow pairs "holomorphic
structure plus a non-zero holomorphic section" on L is, up to isomorphism, H0(M; L)\{0}
divided by the scalar action of C.

Remark. The argument above does not really need the assumption that M is simply
connected, only that b1(M) = 0. Throughout the paper we could have used this weaker
assumption on M.

Examples

(1) When M is a Riemann surface, vortex solutions on a degree d line bundle L  M
are determined by a choice of d points on M, as described above. So the vortex moduli
space M is the symmetric product SymdM -- a classic result.

(2) Suppose that M is a compact and simply connected Ka�hler manifold with H2(M; Z) 

Z. Then Pic(M) is also isomorphic to Z. If the Picard group has a positive generator

E  M, the Chern class c1(E) generates the additive group H2(M; Z) (this follows
from the Lefschetz theorem on (1,1)-classes) and any holomorphic line bundle L  M

is isomorphic to a tensor product dE. The integer d is called the degree of L and is

determined topologically by

                             c1(L) = d � c1(E) .     (2.3)

Since H2(M, R) = R is one dimensional, there is no need to take the parallel component
in inequality (2.2). That stability condition can be rewritten simply as

                             c1(L)  <   e2  [M ]  .
                                       2 m

According to Proposition 2.3, the moduli space of vortex solutions on L = Ed is a projec-
tive space. Its complex dimension is determined by the dimension of H0(M; Ed), which

                                       6
depends only on the manifold M and on the degree d. For instance, when M is the
standard projective space M = CPm, we have E = O(1) and

        dimC H0(CPm; Ed)           =     (m + d)!  .
                                           m! d!

When M is the Grassmannian Gr(n, k) of k-planes in Cn, a generator of Pic(M) is the
pullback by a Plu�cker embedding of the hyperplane bundle O(1) over projective space.
Equivalently, E is dual to the k-th wedge product of the rank-k tautological bundle over
Gr(n, k). A classic result then says that the space of holomorphic sections of Ed has
complex dimension (see [Sa, p.93] and the references therein):

                                    n-k     n   d+j -  i
                                                  j-i
        dimC H0 Gr(n, k), Ed  =                           .

                                   i=1 j=n-k+1

(3) Let M be the Hirzebruch surface Fk = P(O(-k)  C). This is a bundle over CP1 with
fibre CP1. Both the Picard group and the cohomology H2(M, Z) are isomorphic to Z  Z.

The standard generators [F ] and [C] of the 2-cohomology are Poincar�e-dual, respectively,
to a fibre of the bundle and to the canonical section of the bundle. Let La,b  Fk be the
line bundle with Chern class a[C] + b[F ], where a and b are positive integers. Then well

known identifications of holomorphic sections (see ch.V.2 of [Har]) say that

        H0(Fk, La,b)  H0 Sa O(-k)  C  O(b)             a

                                                H0 O(-kl + b) ,

                                                      l=0

and so                        a

        dimC H0(Fk, La,b) =        max{0, b - kl + 1} .

                              l=0

Universal bundle

One of the main objects of study in this paper are the vortex universal bundles over
the cartesian product M � M. In the case of the simplest abelian vortex equations, the
universal bundle is just a line bundle

                                             L - M � M .

It can be constructed in at least two different ways. Regarding M as the space of effective
divisors on M with class c1(L), the universal bundle corresponds to the divisor D on the
cartesian product M � M consisting of the points (x, D) such that x belongs to the
support of D. It is clear that, for every D  M, the restriction L|M�{D} is isomorphic
to [D] as a line bundle over M. In the second construction of L, described for example
in [Pe, Ba1], we regard M as being the quotient V/G of the space of vortex solutions by
the group of unitary gauge transformations on L. Then L is obtained as the quotient
bundle (L � V)/G, where the unitary gauge transformations act both on L and on V.

                              7
If [A, ] denotes the gauge equivalence class of a vortex solution, there exists a global
section  of L that takes a point (x, [A, ]) in M � M to the point [(x), A, ] in the
quotient (L � V)/G. Since the section  vanishes exactly along the tautological divisor
D, we recognize that c1(L) = c1([D]) and that both constructions are equivalent up to
smooth isomorphism. The first construction induces a natural holomorphic structure on
L; the second induces a hermitian metric, inherited from the one on L, and a unitary
connection A (see [Pe, Ba1]).

    When the manifold M is simply connected, and so M is a projective space, the
universal bundle L is particularly easy to describe.

Lemma 2.4. Denote by p1 and p2 the projection from the product M � M onto the first
and second factor, respectively. Then L is isomorphic to p1L  p2 H and has Chern class

                                    c1(L) = p1 c1(L) + p2 c1(H) ,

where H denotes the hyperplane bundle over projective space.

Proof. The cartesian product M � M is simply connected, so the holomorphic structure

on L is determined by its first Chern class. Since each factor has trivial 1-cohomology,

necessarily

              c1(L) = p1 + p2 

with   H2(M, Z) and   H2(M, Z). The class  is the first Chern class of the

restriction of L to M � {point}. By construction of L this restriction coincides with L,

so we get that  = c1(L). The class  is the first Chern class of the restriction of L to
{point} � M, and in [Ba4] it was shown that it coincides with c1(H).

2.3 Case of abelian varieties

Moduli space

Let L  M be a complex line bundle over an abelian variety of complex dimension m.

Since M is a complex torus, it can be represented as a quotient V / of a m-dimensional

complex vector space by a discrete lattice of maximal rank 2m. Any integral basis

{1, . . . , 2m} for this lattice also spans the full vector space over the reals, so it de-
fines dual real coordinates {x1, . . . , x2m} on V . The differential 1-forms {dx1, . . . , dx2m}

then descend to the quotient M and generate the integral cohomology ring H(M, Z). It

is a standard result that the basis of  can be chosen such that the first Chern class of L

is simply
                                                                               m

              c1(L) =                                                             j dxj  dxm+j  (2.4)

                       j=1

for some integer coefficients j  Z [GH]. Now, we want to determine the moduli space
of vortex solutions on L. The easiest way to describe this space is to use the Hitchin-
Kobayashi correspondence of [Bra1] and think of vortices as pairs "holomorphic structure
plus a non-zero holomorphic section on L". On the one hand, since M is an abelian

                                                                                  8
variety, the set of holomorphic structures on L is a complex torus of the same dimension
as M, which will be denoted by Picc1(L)M. On the other hand, by assumption L is

positive, so we know [GH] that for any holomorphic structure on L the dimension of the

space of sections is                                                            m

                      r(L) := dimC H0(M ; L) = j .                                 (2.5)

                                                 j=1

An argument similar to the one used in Section 2.2 then shows that the space of Bradlow
pairs on L should be a projective bundle over Picc1(L)M . The fibre above each point L

in this Picard variety will be the projectivization of H0(M; L). But which bundle is this

precisely? The answer can be stated as follows.

The torus Picc1(L)M is (non-canonically) isomorphic to the Picard group Pic0M of holo-
morphic line bundles over M with trivial Chern class, usually called the dual variety M^ .
Consider the Poincar�e line bundle P - M � Pic0M with the usual normalization. De-
noting by p1 and p2 the projections from this cartesian product onto the first and second
factors, respectively, we can define the push-forward bundle

                                   L^ := p2(P  p1L) - Pic0M .

This is a complex vector bundle of rank r(L) and is called the Fourier-Mukai transform of
L (see [BBR, Huy], for instance, for a description of these transforms in a much broader
setting). Then the space of Bradlow pairs on L -- or, equivalently, the space of effective
divisors on M with class c1(L) -- coincides with the projectivization of L^.

Proposition 2.5. Let L  M be a positive line bundle over an abelian variety and
suppose that condition (2.2) is satisfied. Then the moduli space of vortex solutions on L
is a smooth bundle over the torus Pic 0M with typical fibre CP r(L)-1. In fact, the moduli
space coincides with the projectivization

                                                M  P(L^)

of the Fourier-Mukai transform of L.

Proof. It is a consequence of Proposition 3.4 and the fact that H1(M; L) vanishes for an
ample line bundle on an abelian variety. See, for instance, the description in [Bri, Sect.
5] of the space of effective divisors on M that are Poincar�e-dual to the class c1(L).

Cohomology of the moduli space

Since M is a projective bundle, there exists a natural "hyperplane" line bundle H - M

and a natural class

                       := c1(H)  H2(M; Z)                                          (2.6)

that generates the cohomology of the projective fibres of M. By the Leray-Hirsch theorem,
any cohomology class in H(M; Z) can be written in the form

                      r(L)-1

                             k projk

                        k=0

                                9
for some classes k  H(Pic 0M; Z), where proj : M - Pic 0M denotes the natural
projection. Multiplicatively, these cohomology classes are subject to the standard relation

[BT]:

                                    r(L)

                         r(L) +             ck(L^) r(L)-k = 0 .

                                    k=1

So to obtain the ring structure on H(M; Z) we need to know the Chern classes of the
Fourier-Mukai transform L^. These are determined by the following result.

Lemma 2.6. The Chern character of the Fourier-Mukai transform L^ is

                                       m

                         ch (L^) =          (k - dxk  dxm +k) ,                  (2.7)

                                       k=1

where {dxk} is the basis of H1(M^ , Z) dual to the basis {dxk} of H1(M, Z). The total
Chern class can then be written as

                    m                  r    c1 k     exp arctan c1/r        r
                                       k    r              1 + (c1/r)2
       c(L^) = exp       (-1)k(k-1)/2             =                           ,  (2.8)

                    k=1

where the integer r is given by (2.5) and c1 = c1(L^) = ch1(L^) is the first Chern class.

Proof. Using the definition of L^, the Chern character can be expressed as

       ch(L^) = ch[p2(P  p1L)] = p2 ch(P  p1L)
                = p2 ch(P) � p1ch(L) = p2 exp c1(P) � p1 exp c1(L) .

Notice that in the second equality above we have used the Grothendieck-Riemann-Roch
formula applied to the projection morphism p2. The Todd classes of M and Pic 0M do
not appear in this formula because both manifolds are Lie groups, and hence have trivial

tangent bundle. On abelian varieties the first Chern class of the Poincar�e line bundle is

given by the standard formula [Huy, p.198]

                                            2m

                             c1(P) =              dx  dx .

                                            =1

The Chern class c1(L) is given by (2.4). The push forward map p2, on its turn, is just
the standard integration over the fibre M of the projection M � Pic 0M - Pic 0M. In
particular

                                    p2   dx1  � � �  dx2m = 

for any class  in H(Pic 0M; Q). Using all these elements, an exercise in bookkeeping
yields

       chj(L^) = p2      c1 (P )2j  �  p1 c1(L)m-j
                          (2j)!         (m - j)!

                    = (-1)j                          i          dxl  dxm +l ,

                             {J| #J=j} i{1,...,m}\J         lJ

                                            10
where we have denoted by  the set of subsets of {1, . . . , m}. It is then easy to recognize
that the formula above is equivalent to (2.7), as desired.

    To obtain the total Chern class of L^, recall that it is related to the Chern character
by the standard formulae

                                       m                            m

                     c(L^) = (1 + k)                      ch(L^) =           ek

                                      k=1                           k=1

for some k  H2(M, Z). In particular we can write

                              m                            m     +               (k )j
                                                                                   j
            c(L^) = exp           log(1 + k)        = exp           (-1)j-1
                   = exp
                             k=1                           k=1 j=1

                             +                                                            (2.9)

                                 (-1)j-1(j - 1)! chj(L^) ,

                             j=1

where of course all these sums have only a finite number of nonzero terms. Using (2.7) it
is straightforward to check the recursion property

    chj (L^ )  =  j  (-1)j      ch1(L^)  chj-1(L^)  =     (-1)(j+2)(j-1)/2   ch1(L^)j  .  (2.10)
                     1 � � � m                            j! (1 � � � m)j-1

Then the first equality in formula (2.8) of the lemma can be obtained by substituting

(2.10) into the relation (2.9). To deduce the second equality in formula (2.8) just divide

the series                        +

                                         (-1)k(k-1)/2  r   c1 k                           (2.11)
                                                       k   r
                                  k=1

into a sum of the even and odd sub-series and, using the standard Maclaurin expansion

of the functions log(1 + x) and arctan(x), check that (2.11) coincides with the expansion

of                        r
                          2
                     -       log  1 + (c1/r)2       + r arctan(c1/r) .

This ends the proof of the lemma.

Universal bundle

We consider now the universal line bundle

                                              L - M � M

defined in Section 2.2. When M is an abelian variety we have the following result.
Lemma 2.7. Denote by p1 and p2 the projections from the product M � M onto the first
and second factors, respectively. Call proj the projection M - Picc1(L)  Pic0M. Then
L is isomorphic as a complex line bundle to the tensor product (id�proj)P  p1 L  p2 H.
In particular

                         c1(L) = p1 c1(L) + p2  + (id � proj) c1(P) .

                                                       11
Proof. Regard M as the space of effective divisors on M with class c1(L). The definition
of L in Section 2.2 says that L|M�{D}  [D] as a holomorphic bundle, hence

                        c1(L)|M�{D} = c1(L|M�{D}) = c1([D]) = c1(L)

for any divisor D  M. In particular the restrictions of the complex line bundle L  p1L-1
to submanifolds of the form M � {D} always have trivial first Chern class. Then the
universal property of the Poincar�e line bundle (see [BBR, p. 84]) guarantees the existence
of a unique holomorphic map f : M - Pic0M such that L  p1L-1 is isomorphic to
(id � f )P  p2 N , where N is a line bundle over M. Moreover, the map f is determined
by the formula

                            f (D) := L  p1L-1 |M�{D} = [D]  L-1

for any D  M, so it coincides with the natural projection proj. So we have that

                      c1(L) - p1 c1(L) = (id � proj) c1(P) + p2 c1(N ) .

The normalization of P is such that its restriction to the subset {0} � Pic0M is trivial,
so the line bundle N coincides with the restriction of L to the submanifold {0} � M. As
shown in [Ba4], this last restriction is isomorphic to the hyperplane line bundle H -
M associated with the projectivization, and this proves the formula for c1(L). The
expression for L as a tensor product follows automatically because complex line bundles
are determined up to smooth isomorphism by their first Chern class.

3 Vortices in abelian GLSM

3.1 General results

Let M be a m-dimensional compact Ka�hler manifold and let  be a linear representation
of the k-torus on Cn. We denote by Qaj the integral weights of the representation, where
the indices run as 1  j  n and 1  a  k. Assuming that  is effective, the span of
the weights {Qj  Zk : j = 1, . . . , n} over the real numbers is the full space Rk. Now
take a principal bundle P  M with group T k and define the hermitian line bundles

Lj = P �j C over the manifold M associated with the restriction of  to the j-th copy
of C inside Cn. With these conventions the vortex equations are written for pairs (A, ),
where A is a connection on P and  is a section of the direct sum bundle nj=1Lj. They
read

�A = 0                                  (3.1)
iFA + e2
                        Qj |j|2 -  = 0
FA0,2 = 0 ,
                     j

where the curvature FA has values in the Lie algebra tk = iRk and  is a fixed constant
in Rk. As usual, solutions of the vortex equations will be minima of the Yang-Mills-

Higgs energy of the GLSM. The moduli space of solutions to these equations depends

                     12
on the principal bundle P and on the values of the constants Qj and e2 . For instance,
decomposing the torus bundle as a product of circle bundles

                                          P = �ak=1 P a - M ,
it is clear that the third vortex equation has solutions only if

      c1(P a)  H1,1(M, C) for all 0  a  k .                                      (3.2)

Moreover, using that the volume form on M is just Mm /m! and using the identity
                                       FA Mm = m FA  Mm-1 ,

an integration of the second vortex equation over (M, M ) shows that another necessary
condition for the existence of vortex solutions is that the vector

             :=   (Vol M)   -  i      FA         Mm-1                            (3.3)
                               e2              (m - 1)!
                                    M

in Rk can be written as a linear combination of weights Qj with non-negative scalar
coefficients. In other words, the vector  must be in the closed cone

       :=                                n                         Rk

             v  Rk : v = j Qj with j  0

                                        j=1

generated by the weights of the torus action. To write  in a more "cohomological" way,

denote by c1(P ) the vector in the cohomology kH2(M, Z) with components c1(P a) -- a
slight abuse of notation. Then, using the standard L2 inner product of forms to decompose

H2(M, R) into the real line generated by [M ] and its orthogonal complement, we have

that                                           c1(P )
                                                [M ]
      c1(P )  [M ]m-1  = c1(P )  [M ]m-1    =                     [M ]m ,

where denotes the component parallel to [M ] and the first equality is justified by the
Lefschetz decomposition [GH, Ch 0.7]. So the vector (3.3) can be written more simply as

               =   Vol M    -  2 m  c1(P )  Vol M .                              (3.4)
                                e2   [M ]

This is a vector in Rk and, for each component, we are taking the part of c1(P a) parallel
to [M ] in the cohomology H2(M, R). So the first observation is the following.

Lemma 3.1. The GLSM has vortex solutions only if condition (3.2) is satisfied and the
vector  lies in the closed cone   Rk generated by the weights of the torus action.

Assuming that this necessary condition holds, we now turn to the question of existence
and construction of vortex solutions. Our main result here follows from a type of Hitchin-
Kobayashi correspondence established in [Ban, Mu]. It allows us to construct full vortex
solutions from pairs (A, ) that satisfy only the first and third vortex equations. Before

                               13
being more precise, let us introduce some notation. Given a section  of the direct sum
bundle nj=1Lj, we define the index subset

                                  I := { j  {1, . . . , n} : j  0 } .

Then we call S  Rk the subspace spanned by the weights {Qj  Zk : j  I}, and S
the orthogonal complement with respect to the standard euclidean metric on Rk. Finally,
we define the cone in S generated by linear combinations with non-negative coefficients

 := v  Rk : v = j Qj with j  0                     S .                          (3.5)

                                             j I

We will often talk about the interior of this cone. By this expression, we mean the interior

of  regarded as a subset of S. Equivalently, the interior of  coincides with the subset
of vectors that can be written as a linear combination of the weights {Qj  Zk : j  I}
with strictly positive scalar coefficients (see Lemma A.2 in the Appendix). With these

conventions in mind we can now state the main result of Section 3.1.

Theorem 3.2. Let (A, ) be a pair satisfying the first and third vortex equations. There
exists a gauge transformation g : M  (C)k such that (g(A), g()) solves the full vortex

equations if and only if the vector  defined in (3.4) lies in the interior of the cone
. When this happens, the transformation g is unique up to multiplication by T k-
gauge transformations, and by constant gauge transformations with values on the subgroup
exp(S)  R+k of the group (C)k. All vortex solutions can be obtained in this way.

As mentioned above, the proof of this result relies heavily on a type of Hitchin-Kobayashi
correspondence established in [Ban, Mu]. This correspondence equates the existence of
the gauge transformation g required in Theorem 3.2 to a stability condition on the initial
pair (A, ). This stability condition is defined in [Ban, Mu] in abstract terms that apply
to vortices in very general settings. It is not an easy condition to evaluate in practice,
though. In the case of the abelian GLSM, however, the stability condition simplifies
dramatically and has a very concrete and natural appearance. This is the content of the
next result, which underlies the main part of the proof of Theorem 3.2.

Theorem 3.3. Let (A, ) be a pair that satisfies the first and third vortex equations. It is
a simple pair in the sense of [Mu] if and only if the weights {Qj : j  0} span the whole
Rk. Such a simple pair is  -stable in the sense of [Mu] if and only if the vector  defined
in (3.4) is in the interior of the cone .

An important feature of the moduli space of vortices on line bundles is that it can be

described as a space of effective divisors on M, as we saw in Section 2.1. Unfortunately,

for the general GLSM no such identifications exist. A nice exception is the case of GLSM's

with the special equality n = k, where again choosing a vortex solution corresponds to

picking a set of effective divisors on M that satisfy a natural topological condition. This

is the content of the next result. To introduce the statement, observe that for an effective

T k-action on Ck the integral weights Q1, . . . , Qk form a basis of Rk. In particular, the
                                                                  k
vector  of (3.4) can be uniquely written as a linear combination  j=1  j  Qj .  From

14
Lemma 3.1 we know that if any of the coefficients j is negative, i.e. if  lies outside the
cone , there are no vortex solutions. If  lies in , we denote by I+ (respectively, I0) the
subset of {1, . . . , k} defined by the j's such that j is positive (respectively, is zero). Then
we can decompose Rk = S0  S+, where the subspace S+ (respectively, S0) is spanned
by the weights Qj such that j  I+ (respectively, j  I0). The vortex solutions are then
described by the following result.

Proposition 3.4. Assume that n = k, that the weights Q1, . . . , Qk span Rk, and that the
vector  of (3.4) lies in the cone   Rk. For each index j  I0 pick a holomorphic
structure Hj on the line bundle Lj. For each index j  I+ pick an effective divisor
of analytic hypersurfaces Dj on the manifold M such that the fundamental homology
class [Dj] is Poincar�e-dual to the Chern class c1(Lj) = a Qja c1(P a) in the cohomology
H2(M; Z). Then there exists a solution (A, ) of the vortex equations (3.1) such that:

  (i) For all j  I0, we have j  0 and the holomorphic structure on Lj induced by A
       coincides with Hj.

 (ii) For all j  I+, the divisor Dj coincides with the divisor of the zero set of j regarded
       as a section of Lj.

This solution is unique up to T k-gauge transformations, and up to constant gauge trans-
formations with values on the subgroup exp(S+)  R+k of the group (C)k. Different
choices of divisors or holomorphic structures provide gauge inequivalent solutions. All
vortex solutions are obtained in this way.

Remark. The principal torus bundle P  M may have classes c1(P a) such that it is
impossible to choose a set of divisors Dj satisfying the required condition. The Proposition
then asserts that such a GLSM has no smooth vortex solutions. The same thing happens
if, for any j  I0, the line bundle Lj does not admit a holomorphic structure, i.e. if Lj
does not admit a connection with curvature of type (1, 1).

Proofs

Lemma 3.5. Let (A, ) be a pair that satisfies the first and third vortex equations. The

infinitesimal gauge transformations that preserve (A, ) are represented by the constant
maps M  S  Rk. In particular, the stabilizer of (A, ) under T k-gauge transforma-
tions is discrete iff the weights {Qj : j  0} span the whole Rk. If those weights generate
the lattice Zk over the integers, the stabilizer of (A, ) is trivial.

Proof. An infinitesimal gauge transformation v : M  iRk acts on sections of jLj as

        (1, . . . , n) - dv() =      va Qa1 1, . . . , va Qan n .

                                 a   a

So dv() vanishes if and only if the sum a vaQja is identically zero for every index
j such that j  0. This is equivalent to saying that v has values on the orthogonal

                                 15
complement S. Moreover, since infinitesimal gauge transformations act on connections
by A  A + dv, a map v preserves the connection if and only if it is constant.

    Suppose now that the weights {Qj : j  0} generate the full lattice Zk  Rk over the
integers. Then the vector (1, 0, . . . , 0), for instance, can be written as a linear combination

   jI bj Qj for some integers bj. If a gauge transformation g : M  (C)k preserves the
section , then we must have

                                                                         k

                                                   (ga)Qja = 1

                                                                       a=1

for all j  I. This implies that

             1=                             k

                                              (ga)bj Qja = g1 .

                         jI a=1

Using a similar argument for all the other components of g, we see that g is the constant
map to the identity in (C)k.

Proof of Theorem 3.3. In the language of [Mu], the pair (A, ) is simple precisely if it

has discrete stabilizer under gauge transformations. So the first statement of the theorem
follows from Lemma 3.5. Now identify the Lie algebra tk with Rk so that the usual
exponential map tk  T k is given by v  eiv for any v  Rk. Then the moment map
� : Cn  tk associated to the representation  is

             �(z)     =  -               1     Qj |zj|2 -  .
                                         2
                                            j

Since the representation is effective, the image �(Cn) is a k-dimensional cone inside the
Lie algebra. In our setting, the definition of stability in [Mu] can be stated as follows:

A pair (A, ) is  -stable if and only if

    v, -iFA  + 2 e2((x), v)                 Mm    >  0     f or all v  Rk \ {0} .  (3.6)
                                            m!
xM

 In this expression �, � denotes the canonical euclidean product in Rk and, calling tv :
Cn  Cn the gradient flow of the function v, � : Cn  R, we define for any z  Cn:

             (z, v)       :=                 lim  v, � (tv(z)) .

                                            t+

Since the moment map � is invariant by the representation , so is , and the composition
((x), v) is well defined. The integral of the first term in (3.6) is

             v, -iFA  Mm                 =  - 2 m (Vol M)        c1(P ) , v  .
                      m!                                           [M ]
    M

As for the second term, start by noticing that for abelian hamiltonian actions the gradient
flow of v, � is related to the exponential map of the complexified group action:

                      tv(z) = exp(-tv) (z) .

                                            16
Using the explicit expressions for  and the moment map, it is easy to check that

    (z, v) = +            if for some j we have Qj, v < 0 and zj = 0 ,

                   , v /2 otherwise .

Consider the index subset I = {j  {1, . . . , n} : j  0}. Since the section  is
holomorphic, for every j  I the components j are nonzero almost everywhere on M.
It follows that

    2 e2 ((x), v)  Mm  =  +               if Qj, v < 0 for some j  I ,
                   m!     e2 (Vol M) , v  otherwise .
xM

In the first case the inequality in condition (3.6) is clearly satisfied. So we only need
to worry about the second case, i.e. when v is such that the inner product Qj, v is
non-negative for all j  I. In this case the inequality in condition (3.6) reduces to

                          e2 , v > 0 .                                            (3.7)

Now suppose that  can be written as a linear combination  = jI j Qj with strictly
positive coefficients for some non-empty subset I  I. Then the inner product , v is
non-negative. It vanishes precisely when v is orthogonal to the weights {Qj : j  I}, or,
equivalently, when v is orthogonal to the real span SI  Rk of those weights. But by
assumption Qj, v is non-negative for all j  I, i.e. the cone  lies entirely in one of
the closed half-spaces of Rk determined by the plane v. So if , v vanishes, the vector
  SI  v necessarily lies on the boundary of the cone . This shows that whenever
 is in the interior of , the inequality (3.7) is always satisfied, and hence the pair (A, )
is  -stable.

    To prove the converse, suppose that  is outside the k-dimensional closed cone .
Since the cone is convex, it has a k - 1-dimensional facet such that  and the interior of

the cone lie in opposite sides of the facet, or, more properly, lie in opposite sides of the
subspace of Rk spanned by the facet. Call this facet F. On the other hand, if  lies on
the boundary of the cone , choose F to be any k -1-dimensional facet that contains .
Now let v  Rk be a non-zero vector orthogonal to F and pointing towards the half-space
where the cone lies. Then clearly u, v  0 for all u  , and in particular Qj, v is
non-negative for all j  I. But at the same time , v is negative or zero, so condition
(3.7) is not satisfied. This shows that if  is not in the interior of , the pair (A, ) is
not  -stable.

Proof of Theorem 3.2. The necessity part of the Theorem is clear: if the pair (g(A), g())
solves the full vortex equations, integration over (M, M ) of the second vortex equation
shows that the vector  can be written as a combination of the weights {Qj : j  0}
with strictly positive coefficients.

    The sufficiency and uniqueness follow from Theorem 3.3 and the Hitchin-Kobayashi
correspondence of [Ban, Mu] (see in particular Sections 6.2, 6.4 and 6.5 of [Mu]). Suppose
first that the pair (A, ) is simple in the sense of Theorem 3.3. Then the assumption on 

                          17
implies that (A, ) is  -stable, and so the existence of g and its uniqueness up to T k-gauge

transformations follows directly from Sections 6.2 and 6.4 of [Mu]. Now suppose that the
subspace S  Rk spanned by the weights {Qj  Zk : j  0} has dimension l < k. Then
the orthogonal decomposition Rk = S  S allows us to decompose the second vortex
equation as a pair of equations

iFA + e2     Qj |j|2 -   =0  (3.8)
                             (3.9)
          j

iFA - e2   = 0 ,

where the symbols and  denote the components parallel and orthogonal, respectively,
to the subspace S  Rk. The natural strategy here is to solve these two equations one
at a time. By Lemma 3.5, there are no infinitesimal gauge transformations of the form

M  S that preserve the pair (A, ). Using this fact and the assumption on   S, the
proof in Section 6 of [Mu] guarantees the existence of a complex gauge transformation

g : M - exp(S  iS)  (C)k ,   (3.10)

unique up to T k-gauge transformations, such that the pair (g (A), g ()) solves equation
(3.8) (see the comments in Section 6.5 of [Mu]). Moreover, observe that any complex
gauge transformation of the form (3.10) preserves equation (3.9), and that any gauge
transformation of the form

g : M - exp(S  iS)  (C)k

preserves equation (3.8). So to find a solution of the full vortex equations, we only need
to find a map s : M  S such that the imaginary gauge transformation g = exp s with
values on (R+)k satisfies

                    iF(exp s)(A) - e2   = M (s) + iFA - e2   = 0 ,

where M denotes the Laplacian on the Ka�hler manifold (M, ). But the assumptions
of the Theorem say that the orthogonal component  vanishes, and by formula (3.3)
this is the same as saying that the integral of iFA - e2   over the manifold (M, )
vanishes. Hodge theory then guarantees the existence of the desired s, which is unique up
to an additive constant in S. This completes the proof of the sufficiency and uniqueness
statements.

    Finally, and very obviously, given any vortex solution (A, ), the integral of the second

vortex equation over (M, ) shows that  must lie in the interior of the cone . So the
solution (A, ) can be obtained by the method prescribed in the Theorem if we choose g

to be the trivial gauge transformation. In particular all vortex solutions can be obtained

by the method prescribed in the Theorem.

Proof of Proposition 3.4. We start by showing that each valid choice of divisors Dj
and holomorphic structures Hj leads to a vortex solution. Firstly, the topological condi-
tion on the divisors and standard results on line bundles [GH] guarantee that, for each

             18
j  I+, the nonzero divisor Dj defines a holomorphic structure on Lj  M and a holo-
morphic section j  (Lj) such that Dj is the divisor of the zero set of j. In particular

we have holomorphic structures on all the hermitian bundles Lj, and so for each index
j  {1, . . . , k} we can consider the Chern connection Bj on Lj. This is a hermitian

connection with curvature of type (1, 1). Then the system of k equations and k variables

          Bj =        Qaj Aa      for all 1  j  k

                   a

has a unique solution A, since by assumption the vectors Qj form a basis of Rk. Therefore
the local 1-forms A1, . . . , Ak define a connection on the principal bundle P  M. By
construction we have that

          �A = (. . . , �Bj j, . . . )1jk = 0 ,

and that           Qaj FA0,a2 = FB0,j2 = 0 .

                a

Since the Qj's form a basis of Rk, the last expression implies that FA0,2 = 0. Thus the
pair (A, ) satisfies the first and third vortex equations. By construction, the index set

I coincides with I+ and the vector  lies in the interior of . So we can apply Theorem
3.2 to obtain a complex gauge transformation g : M  (C)k such that (g(A), g()) is a

solution of the full vortex equations. Since complex gauge transformation do not change

(the equivalence class of) the holomorphic structure on the line bundle, nor the divisor of

the zero set of sections, we have obtained a full vortex solution satisfying (i) and (ii).

    The uniqueness part of the Proposition follows from the uniqueness in Theorem 3.2.

Let (A, ) and (A, ) be two vortex solutions satisfying conditions (i) and (ii). Then

for each j  I+ the quotient fj = ()j/j is a nowhere vanishing section of the trivial
bundle over M. Moreover, for each j  I0, if we denote by Bj and Bj the connections
on Lj induced by A and A, respectively, then assumption (i) implies that Bj and Bj are
related by a complex gauge transformation fj : M  C on Lj. So we can define another
complex gauge transformation g : M  (C)k by the system of k equations

          fj =        Qja ga      for all 1  j  k .

                a

By construction we then have that (A, ) = g(A, ) -- a fact that can be checked
directly using the assumption that the vectors Qj form a basis of Rk. The uniqueness
part in Theorem 3.2 then guarantees that g actually has values on the real torus T k, or
has at most a constant factor with values on the subgroup exp S  Rk+ of the group
(C)k. The uniqueness statement follows from the observation that S = S+.

    To see that all vortex solutions are obtained in this way, just observe that if (A, ) is a

vortex solution, for j  I+ we can take the divisors Dj to be those defined by the zero set
of j. Then the homology class of Dj is Poincar�e-dual to c1(Lj). For j  I0, we take the
holomorphic structure Hj on Lj to be the one determined by the connection on this bundle
induced by A (this connection is integrable because A satisfies the third vortex equation).

                              19
By the uniqueness proved above, the solution associated to these Dj's and Hj's by the
existence part of the Proposition will be gauge equivalent to the original (A, ). Finally,
different choices of Dj's and Hj's provide gauge inequivalent solutions because (C)k-
gauge transformations do not change (the equivalence class of) holomorphic structures on

line bundles, nor the divisor of the zero set of sections.

3.2 Case of simply connected manifolds

Assume that the compact Ka�hler manifold M is also simply connected. Then line bundles
over M have unique holomorphic structures, as in Section 2.1. The vector space V of all
holomorphic sections of jLj splits as a direct sum

              n

     V=            H0(M, Lj) .                                                     (3.11)

              j=1

If we let the torus T k act on each subspace H0(M, Lj) by scalar multiplication with
weights Qj  Zk, we get a global torus action on V . If we choose and fix an euclidean

metric on each subspace H0(M, Lj), we get a global metric on V that is preserved by the
torus action. A moment map  : V  iRk for this action is given by

(w)  =  -  i     n                                                                 (3.12)
           2
                    Qj |wj|2 -  ,

              j=1

where each wj is a vector in H0(M, Lj). With these definitions we can state the main
result of this section.

Proposition 3.6. Let M be a compact and simply connected K�ahler manifold. Assume
that condition (3.2) is satisfied. Then the moduli space of vortex solutions of the GLSM
is isomorphic to the symplectic quotient

        M  -1(0) / T k.                                                            (3.13)

In particular, the vector  defined in (3.4) determines the level of the quotient.

Proof. Fix a holomorphic structure on P and let A be the respective Chern connection.
Since M is simply connected, this holomorphic structure is unique up to isomorphism, so
every integrable connection A1 on P is (C)k-gauge equivalent to A. The gauge trans-
formation that takes A1 to A is unique up to multiplication by constant (C)k-gauge
transformations. It follows that every solution (A1, 1) of the first and third vortex equa-
tions is (C)k-gauge equivalent to some pair (A, ), where  is a holomorphic section of
jLj (equipped with the holomorphic structure induced by P ) that is uniquely deter-
mined up to the (C)k-action on V . So we have a natural map from the moduli space B
of solutions of the first and third vortex equations to the topological quotient

                                            : B - V /(C)k .

                   20
This map is injective because two solutions (A1, 1) and (A2, 2) that are (C)k-gauge
equivalent to the same pair (A, ), are necessarily (C)k-gauge equivalent to each other.

There is also an obvious map M  B. This map is injective because the uniqueness part
of Theorem 3.2 guarantees that two vortex solutions that are (C)k-gauge equivalent, are
in fact related by a T k-gauge transformation. (Notice that the constant gauge transfor-
mations with values on the subgroups exp(S)  R+k mentioned in Theorem 3.2 preserve
the respective vortex solutions, by Lemma 3.5). Moreover, it also follows from Theorem

3.2 that the image of the injective map M  B is the set of equivalence classes of pairs

(A1, 1) such that the vector  is in the interior of the cone 1. Using the injective
correspondence , the moduli space M can thus be identified with the quotient of the
(C)k-invariant subset of holomorphic sections

V := {  V :  is in the interior of the cone }  V                   (3.14)

by the (C)k-action.

    Now, given any point w  V , define the index subset Iw as the set {j  {1, . . . , n} :
wj = 0}. The orbit of w under the (C)k-action intersects the inverse image -1(0) if and

only if the vector   Rk can be written as a linear combination jIw jQj with strictly
positive coefficients, i.e. if and only if  lies in the interior of the cone

                        w := v  Rk : v = j Qj with j  0 .

                                                                                   j Iw

When this happens, the intersection of the (C)k-orbit of w with the inverse image -1(0)
is a single T k-orbit (see for instance Lemma 7.2 in [Ki]). This implies that

-1(0) / T k  (C)k � -1(0) / (C)k  V / (C)k ,                       (3.15)

where V is the set of vectors w  V such that  is in the interior of the cone w. But in
the discussion above we had concluded that the last quotient can be identified with the
vortex moduli space M, so this finishes the proof.

Dimension and smoothness of the moduli space

The dimension of the vortex moduli space depends on the value of the parameter   Rk;

it can be described as follows. Let {I1, . . . , IN } be the collection of all non-empty index
subsets I  {1, . . . , n} such that  is in the interior of the cone I. For each subset Is in
the collection, define the non-negative integers

                     Ds :=        dimC H0(M, Lj)

                            j Is

and
                                ds := dimR span{Qj  Zk : j  Is} .

Then the dimension of M is given by

                     dimC M = max {Ds - ds : 1  s  N }.            (3.16)

                                  21
Observe that a generic vector  inside the cone  does not lie in any of the proper
subspaces of Rk spanned by proper subsets of weights Qj. This implies that for generic
 the integer ds is equal to k for all 1  s  N. In particular, the maximum in (3.16)
is attained for the full index set I = {1, . . . , n}, so the complex dimension of the moduli
space in the generic case is just dimC V - k.

    For such generic values of  all vortex solutions have a discrete stabilizer under gauge
transformations, as follows from Lemma 3.5. The points in the subset V  V also have
discrete stabilizers under the (C)k-action. This means that for generic    the moduli
space M is a toric orbifold. To guarantee smoothness of the moduli space we need a
stronger assumption on the weights Qj of the torus action. Suppose that:

(C1) The vector  defined in (3.4) lies in the cone , but does not lie in any of the proper
subspaces of Rk spanned by proper subsets of weights Qj.

(C2) Every subset of weights in {Q1, . . . , Qn} that spans Rk also generates the integer
lattice Zk in Rk.

Then it follows from Lemma 3.5 that all vortex solutions have trivial stabilizer under

gauge transformations. The points in V  V also have trivial stabilizers under the
(C)k-action, and so with these assumptions M is a smooth toric manifold.

In the smooth case, the representation of the vortex moduli space as a symplectic

quotient allows us to define a natural set of cohomology classes in H2(M; Z). In fact, ob-

serving that -1(0)  M is a smooth principal T k-bundle, we can consider the associated

line bundle

             Ha = -1(0) �U(1)a C - M ,                      (3.17)

where the notation means that T k acts on C by simple multiplication of the a-th U(1)-

factor inside T k. This is the same as the line bundle V �(C)a C - M associated with
the principal (C)k-bundle V  M. We then define

             a := c1(Ha) in H2(M; Z) for a = 1, . . . , k.  (3.18)

These cohomology classes are standard in toric geometry and are known to generate the
cohomology ring of the toric quotient M.

Universal bundle

Abelian GLSM deal with connections on a principal bundle P - M with gauge group
T k. If we regard the moduli space M as the quotient V/G of the space of vortex solutions
by the group of gauge transformations G = Map(M  T k), then the quotient

                                     U := (P � V)/G - M � M

is also a T k-bundle. It is called the universal bundle. The decomposition P = �ka=1 P a as
a product of circle bundles induces a similar decomposition U = �ak=1 U a.

    In this paragraph we will describe the topology of the universal bundle U, which is
determined by the Chern classes c1(Ua). We assume that conditions (C1) and (C2) of the
preceeding paragraph are true, so that the moduli space M is a smooth toric manifold
described by Proposition 3.6.

                                                       22
Lemma 3.7. Denote by p1 and p2 the projections from the product M � M onto the
first and second factor, respectively. Then the first Chern classes of the universal circle

bundles are

             c1(U a) = p1 c1(P a) + p2 a

in the cohomology H2(M � M, Z), where the classes a were defined in (3.18).

Proof. Both M and the moduli space M are simply connected, so the first Chern class
of Ua is necessarily of the form

                                        c1(U a) = p1 M + p2 M

for some classes M in H2(M, Z) and M in H2(M, Z). The class M coincides with the
first Chern class of the restriction of the bundle Ua to M � {point}. Choosing a particular
vortex solution (A, ), we have that

             U a |M�{[A,]} = P a � [(A, ) � G] /G  P a ,

where the last isomorphism follows from the fact that the G-action on the space of vortex
solutions is free (cf. Lemma 3.5). Thus M = c1(P a). Similarly, the class M coincides
with the first Chern class of the restriction of the bundle Ua to {p} � M, where p is any

point in M. To prove that this is just a, we will use an argument similar to the one in
[Ba4]. Start by considering the subgroup of gauge transformations

             Gp := g :   T k such that g(p) = (1, . . . , 1) .

It is clear that G splits as Gp � T k. Denoting by Pp the fibre of the principal bundle above
the point p, we then have that

             U a |M�{p} = (V � Pp) / G = [(V � Pp)/Gp] / T k                 (3.19)
                           = [(V/Gp) � Pp] / T k  V / Gp ,

where in the last step we have used that the T k-action on the fibre Pp is free and transitive.
So we conclude that the restriction of Ua to M � {p} is isomorphic to the T k-bundle

V/Gp - M. Consider now the space of pairs that satisfy the first and third vortex
equations:

                              B = {(A, ) : �A = 0 and FA0,2 = 0} .

Define a gauge invariant subset B  B by only taking the pairs (A, ) such that the
vector  is in the positive cone generated by {Qj : j  I}, i.e. the pairs such that   V,
using the notation in (3.14). Observe firstly that, by Lemma 3.5 and assumptions (C1)
and (C2), the group GC of complex gauge transformations acts freely on B. Secondly,
Lemma 3.1 says that all vortex solutions are in this subset, which implies that GC �V  B.
Finally, Theorem 3.2 guarantees that B  GC � V, and hence that

             B = GC � V .                                                    (3.20)

It follows that the vortex moduli space M = V/G = B/GC can be identified with a
complex quotient. Moreover

             B /GpC = (GC/GpC) � V / Gp = [(C)k � V] / Gp

             23
as a principal (C)k-bundle over the moduli space. But the complex quotient B/GpC is just
the space of holomorphic sections of jLj up to isomorphism, or, in other words, it is
the vector space V of (3.11). Clearly, the subset B/GpC is then the corresponding subset
V  V defined in (3.14). This means that the associated line bundles Ha  M defined
in (3.17) are just

           Ha = V �(C)a C = [(C)k � V] / Gp �(C)a C  V/Gp �(U(1))a C .

Finally, using the isomorphism established in the first part of the proof, we conclude that

                                        Ha  U |{p}�M �U(1)a C ,

and hence that c1(Ha) = c1(U a |{p}�M) = M.

3.3 Case of abelian varieties

As in the case of simply connected manifolds, the easiest way to describe the vortex
moduli space when M is an abelian variety is to make use of Theorem 3.2. This result
says that the moduli space M is isomorphic to the complex moduli space of pairs (A, )
satisfying the first and third vortex equations and the additional condition:

(1) The vector  of (3.4) is in the interior of the positive cone   Rk generated by the
weights Qj  Zk such that j  0 .

Here A is a connection on the k-torus bundle P  M and  is a section of the associated
bundle jn=1Lj described in Section 3.1. Now, a pair (A, ) satisfies the first and third vor-
tex equations iff A defines a holomorphic structure on P and the section  is holomorphic
with respect to the induced holomorphic structure on jn=1Lj. The set of holomorphic
structures on P is (non-canonically) isomorphic to the k-fold cartesian product �k Pic0M
of the Picard group. Identifying the set of holomorphic structures on each associated line
bundle Lj = P �j C with Pic0M , the group multiplication

                                                       k

mj : �k Pic0M - Pic0M              (g1, . . . , gk) -       (ga)Qja

                                                       a=1

corresponds to the operation of inducing a holomorphic structure from P to Lj. This

is true because the tensor product of line bundles corresponds to multiplication on the

Picard group. Thus for a given choice g = (g1, . . . , gk) of holomorphic structure on P , we

are looking for sections of Lj with holomorphic structure mj (g), and from the discussion
of Section 2.3 these define a vector space isomorphic to (L^j)mj (g), the fibre of the Fourier-
Mukai transform L^j  Pic0M above the point mj (g). Letting the point g  �k Pic0M
vary, we conclude that the space of pairs "holomorphic structure on P plus holomorphic
section of jn=1Lj" is isomorphic to the total space of the vector bundle

      n

V :=       mj L^j - �k Pic0M .                                       (3.21)

      j=1

                               24
As in the case of simply connected manifolds, some of the points of V still represent
holomorphic sections related to each other by constant (C)k-gauge transformations. In
fact, the action j of (C)k on the components j of a section translates into scalar
multiplication with weight Qj  Zk on the fibres of each summand mj L^j of the bundle.
This defines a global action of (C)k on the total space of the vector bundle V . The

orbits of this action consist of pairs related by constant gauge transformations, and hence

must be identified with a single point in the moduli space. So we must quotient V by
the (C)k-action. Finally, Theorem 3.2 says that we should not quotient the whole V ,

but only the invariant subset V  V defined by the holomorphic sections  that satisfy
condition (1) above. We are thus lead to the following result.

Proposition 3.8. Let M be an abelian variety and suppose that condition (3.2) is satis-

fied. Then the moduli space of vortex solutions of the GLSM is isomorphic to the complex

quotient

          M  V (C)k .                                    (3.22)

In particular there is a natural bundle M - �k Pic0M whose typical fibre is a toric
orbifold.

Remark. As mentioned above, the fibres of the the Fourier-Mukai transform L^j are

isomorphic to a space of sections of Lj = P �j C. So a choice of hermitian metric on Lj
will induce a L2 hermitian metric on L^j. Doing this for every j we get a hermitian metric
on the vector bundle V . Using this metric we can consider the moment map  : V  Rk

defined by a formula analogous to (3.12). The moduli space M can then be represented
as a symplectic quotient -1(0)/T k, just as in the case of a simply connected M.

Note in passing that it is perfectly possible that the bundles Lj do not have non-zero
holomorphic sections. If this happens for all j, then the fibre of the vector bundle V is
zero-dimensional, i.e. the fibre is just a point. In this case the subset V will be empty
whenever  = 0, since condition (1) above cannot be satisfied, and hence also M will be
empty. If  = 0 the subset V will be equal to V, and hence the moduli space M will be
isomorphic to �k Pic0M .

    If the vector  has the generic values described in condition (C1) of Section 3.2, the
(C)k-quotient of Proposition 3.8 will have complex dimension equal to dimC(fibre V ) +
k(dimC M - 1). If condition (C2) is also satisfied, the moduli space M will be a smooth
manifold. In this case the representation of the vortex moduli space as a toric quotient
allows us to define a natural set of cohomology classes in H2(M; Z). Just as in the case of
simply connected M, described at the end of Section 3.2, we can consider the associated
line bundles Ha = V �(C)a C - M and define

          a := c1(Ha) in H2(M; Z) for a = 1, . . . , k.  (3.23)

These cohomology classes generate the cohomology ring of the fibres of M - �k Pic0M.
By the Leray-Hirsch theorem, the cohomology ring of M is generated by the a's and the
pullbacks of classes from the base �k Pic0M of the bundle.

          25
Universal bundle

In this paragraph we compute the Chern classes of the universal bundle U  M � M
in the case where M is an abelian variety. The notation and assumptions are the same
as in the case of simply connected M. In particular, we assume that conditions (C1) and
(C2) of Section 3.2 are valid, so that the moduli space M given by Proposition 3.8 is a
smooth manifold.

Lemma 3.9. Denote by p1 and p2 the projection from the product M � M onto the first
and second factor, respectively. Then the first Chern classes of the universal circle bundles
are

                       c1(U a) = p1 c1(P a) + p2 a + (id � proja) c1(P)
in the cohomology H2(M � M, Z), where the classes a were defined in (3.23).

Proof. In this proof we will denote by the same symbol both the circle bundle Ua 
M � M and the associated complex line bundle over the same base; the same applies to
the circle bundle P a  M. As was seen above, there are k projections

                              proja : M - �k Pic0M - Pic0M ,

where the last arrow is the a-th projection from the cartesian product. In terms of
vortex solutions, proja takes an equivalence class [A, ] to the holomorphic structure on
P a determined by the a-th component of the integrable T k-connection A, which we will
denote by (P a)A. Taking the tensor product (P a)A  (P~a)-1, where P~a denotes a fixed
holomorphic structure P a, we get and element of Pic0M, as desired.

    In terms of vortex solutions, the natural holomorphic structure on the line bundle
Ua can be described in the following way. The proof of Lemma 3.7 says that Ua can be
regarded as a complex quotient

                                U a := (P a � V)/G = (P a � B)/GC .

The space P a � B has a natural complex structure determined by the one on B and by
the rule that, on the tangent space TpP a T[A,]B at a given point, the complex structure
on the first summand is the one of the holomorphic bundle (P a)A. This complex structure
is preserved by complex gauge transformations, and hence induces the complex structure
on the quotient Ua. Now, an argument just like in the proof of Lemma 3.7 says that the
restriction of Ua to a submanifold of the form M � {[A, ]} is

                     U a |M�{[A,] = (P a)A � [(A, ) � GC] /GC  (P a)A .

In particular the restriction of U a  p1(P~a)-1 to the same submanifold has trivial first
Chern class. The universality property of the Poincar�e bundle P  M � Pic0M then
guarantees that the existence of a unique holomorphic map fa : M  Pic0M such that
the bundle U a p1(P~a)-1 is isomorphic to (id �fa)P  p2 Na, where Na is a circle bundle
over M. Moreover, the map fa is determined by

      fa [A, ] := U a  p1(P~a)-1 |M�{[A,]} = (P a)A  (P~a)-1 = proja [A, ] .

                                                       26
So we have that

                    c1(U a) - p1 c1(P~a) = (id � proja) c1(P) + p2 c1(Na) .

The normalization of P is such that its restriction to the subset {0} � Pic0M is trivial, so
the line bundle Na coincides with the restriction of Ua to the submanifold {0} � M. An
argument similar to one in the proof of Lemma 3.7 then says that this last restriction is
isomorphic to the complex line bundle Ha  M. This justifies the formula for c1(Ua).

4 K�ahler class and volume of the L2-metric

4.1 Line bundles over simply connected manifolds

In Section 2 we have seen that the moduli space M of abelian vortices on a positive line
bundle L  M is a projective space whenever the base manifold is simply connected.

Since the cohomology ring of projective spaces is very simple, in this instance it is easy
to calculate the volume of M once we know the Ka�hler class of the L2-metric (1.7). This

class can be computed using a formula of Perutz [Pe], as generalized in [BS, Ba4], that
expresses the Ka�hler form on M in terms of the curvature FA of the universal connection
on the universal line bundle L  M � M. The formula says that the Ka�hler form M of
the L2-metric is given by the fibre integral

      M =        i    FA    Mm    +        1   1)!        FA    FA    Mm-1  .       (4.1)
                2 m!                 4e2(m -
             M

(In passing, we note the remarkable similarity between the integral above and the integral
in (1.6), a similarity for which the author cannot offer a good explanation.) Taking the
cohomology class on both sides of the equation, we get that

M  =         c1(L)    M     m  -       2       c1(L)          c1(L)     M      m-1  (4.2)
         m!                       e2(m -
      M                                   1)!

in H2(M, Z). But we know what the Chern class c1(L) is in the case of simply connected
manifolds: it is given by Lemma 3.7. Using that formula, the fact that Mm /m! is the
volume form on M, and the fact that, by Lefschetz's decomposition,

             c1(L)  [M ]m-1 = c1(L)  [M ]m-1 ,

the fibre integration in (4.2) can be performed to yield

                          M =   c1(H) ,                                             (4.3)

where  is the stability parameter (2.2) and H  M is the hyperplane bundle over
projective space. Observe how  effectively parametrizes the Ka�hler class of the L2-metric

on the moduli space. So we get:

                                     27
Proposition 4.1. Let L  M be a positive line bundle over a m-dimensional, simply
connected, compact Ka�hler manifold. If condition (2.2) is satisfied, the volume of the
L2-metric on the vortex moduli space is

       Vol (M, M)         =   ( ) r-1 ,
                               r-1 !

where  is the positive number in (2.2) and r is the complex dimension of H0(M, L). The
total scalar curvature of the moduli space is

   s(M) volM =   2 r (r - 1)      Vol M (r-2)/(r-1) .                            (4.4)
                (r - 1)! 1/(r-1)
M

Proof. Since we already know the Ka�hler class on the moduli space M  CP r(L)-1, the
total volume of (M, M) follows directly from the standard formula

Vol M =              1          [M]dim M .
                (dim M)!
                              M

Similarly, the total scalar curvature follows from the equally standard formula

   s(M) volM =         2         c1(M)  [M]dim M-1 ,
                (dim M - 1)!
M                             M

and the observation that for projective space c1(M) = (dim M + 1) � c1(H).

Observations

(1) When M is Riemann surface the volume and total scalar curvature of the vortex
moduli space were computed in [MN, Ba4].

(2) When M is a compact and simply connected Ka�hler manifold with H2(M; Z)  Z,
it is possible to express the parameter , and hence Vol M, solely in terms of Vol M,
with no explicit reference to the Ka�hler class [M ]. Using the notation of Example (2) in
Section 2.2, we can write

c1(L)  =        c1(L)  =            d      1/m  ,
 [M ]           [M ]       tM -1 m! Vol M

where d is the degree of L, m is the complex dimension of M, and tM is the positive
topological number defined by

                                            tM := c1(E)m .

                                                                                    M

Observe that when M is a projective space, the number tM is equal to 1. When M is the
complex Grassmannian, the generator E of the Picard group is the pullback by a Plu�cker

                       28
embedding Gr(n, k)  CPr of the hyperplane bundle over projective space. It is then

easy to check that the topological number tM coincides the degree of the Grassmannian
as a projective variety in CPr, which is known to be [HP, XIV.7]

                                                k          (j - 1)!
                                                      (n - k + j - 1)!
                       tGr(n,k) =  k(n - k) !                            .

                                                j=1

(3) Let M be the Hirzebruch surface Fk = P(O(-k)  C). We will use the notation of
Example (3) of Section 2.2. Consider the line bundle La,b - Fk whose first Chern class
is a[C] + b[F ] and write the Ka�hler class of the surface as [M ] = [F ] + [C]. Then, using
the standard intersection numbers of the divisors [C] and [F ] (see ch.V.2 of [Har]), we get
that Vol M =  (2 - k)/2 and that

                       c1(La,b) Vol M = 1 a + b(1 - k) .
                       [M ]                 2

4.2 Line bundles over abelian varieties

When M is an abelian variety, the moduli space M is a projective bundle over the dual
variety M^ = Pic0M, as was seen in Section 2.2. The Ka�hler class [M] of the L2-metric
on the moduli space is given by formula (4.2), just as in the case of simply connected
manifolds. The only difference is that the first Chern class c1(L) of the universal bundle
is now given by Lemma 2.7. Using this lemma, it is relatively straightforward to perform

the fibre integral in (4.2) and hence obtain a formula for [M].

Proposition 4.2. Let L  M be a positive line bundle over an m-dimensional abelian

variety. If condition (2.2) is satisfied, the K�ahler class of the L2-metric on the vortex

moduli space is                                                 [Mm-1]
                                                               (m - 1)!
                 M     =         c1(H) -    22        proj  F               ,            (4.5)
                                            e2

where  is the stability parameter defined in (2.2), H  M is the hyperplane bundle in
(2.6), proj is the natural projection M  M^ , and F : H2m-2(M; R)  H2(M^ ; R) denotes
the cohomological Fourier-Mukai transform.

Proof. We use expression (4.2) for the Ka�hler class [M] and the formula

                 c1(L) = p1 c1(L) + p2  + (id � proj) c1(P)

given in Lemma 2.7. Start by observing that the first two terms in this formula coincide
with the expression for c1(L) in the case of simply connected manifolds. In particular
when we substitute these two terms into (4.2) and perform the fibre integration we will

obtain the result   c1(H), just as in the case of simply connected manifolds (cf. formula
(4.3)). When we substitute the last term of c1(L) into the right hand side of (4.2) we get
the additional term

-  2      (id � proj)  c1(P )    c1 (P )     [Mm-1]   =     -  22  proj        ch(P )     [Mm-1]   .
   e2                                       (m - 1)!           e2                        (m - 1)!
       M                                                                    M

                                            29
This term coincides with the last term in (4.5), by definition of F .

Remark. When [M ] is an integral class we can write M = c1(B) for some line bundle

B - M. Then                          [Mm-1]
                                    (m - 1)!
                                 F                = c1(B^),

where the vector bundle B^ - M^ is the Fourier-Mukai transform of B.

Remark. The dual variety M^ = Pic0M coincides with the moduli space of integrable

U(1)-connections on M with zero mean curvature, i.e. connections that satisfy FA =
0 = FA0,2. This moduli space has a natural L2-metric defined by the first term in (1.7),

i.e. by                                       1
                                             4e2
                      A 2 =                       kab  A 1a    M  A 2b

                                        M

Then the last term in (4.5), before pulling back by proj, is exactly the Ka�hler class of
this L2-metric on the moduli space M^ of connections.

Now that we know the Ka�hler class on the moduli space, the next task is to compute the
total volume of (M, M). Recall in the case of abelian varieties the moduli space is a
projective bundle proj : M = P(L^) - M^ . Therefore the integral of the volume form
can be performed in two steps: first integrate over the projective fibres and then integrate
over the base M^ . That is

             Vol M =      [M]m+r-1                =           proj [M]m+r-1                  .
                      M (m + r - 1)!                            (m + r - 1)!
                                                          M^

Since M is the projectivization  P(L^), the  ofifbrteh-einSteeggrraetciolansps roofjL^:.  H(M, R)         H-r+1(M^ ,  R)
can be conveniently expressed    in terms                                                  This class is  defined as

the inverse of the total Chern class by the formal expansion of

              s(L^)   =            1    =    1+   c1(L^)   1            ���               .
                                 c(L^)                    + c2(L^) +

As explained for instance in [BDW], it has the useful property that

                      proj c1(H)l = sl-r+1(L^) ,

where H - M is the hyperplane bundle and we are using the convention that sj(L^) is
zero for negative j. It is then straightforward to compute that

              m    ( ) l+r-1 (-22/e2)m-l                                                      [Mm-1]   m-l
                     (l + r - 1)! (m - l)!                                                   (m - 1)!
Vol (M, M) =                                                sl(L^)  F                                       ,  (4.6)

              l=0                                         M^

To carry out the integration over the dual variety M^ one needs an explicit expression
for the Segre class and for the Fourier-Mukai transform. The former can in principle be
obtained by expanding the expression for c(L^) given in Lemma 2.6, although computa-
tionally this is non-trivial. The latter depends of course on the particular Ka�hler form
M that we take on M. Here we will not perform the integration over M^ in the general
case. We will do it only for abelian varieties of complex dimension one and two.

                                             30
Examples

(1) When M has complex dimension one, i.e when it is an elliptic curve, the natural
identification H2(M; R) = R leads to the formulae c1(L) = c1(L) = deg L and [M ] =
Vol M. Moreover, the Fourier-Mukai transform of 1 is just -, where  stands for the
positive generator of H2(M^ , Z). Hence our formula for the Ka�hler class coincides with
the one given in [MN, Pe].

(2) Let M have complex dimension m = 2. Using the notation of Section 2.3, we can
choose a set {dxk} of generators of H1(M, Z) such that

               c1(L) = 1 dx1  dxm+1 + 2 dx2  dxm+2 ,

for some positive integers k. If we choose a Ka�hler form on M of the form

               M = 1 dx1  dxm+1 + 2 dx2  dxm+2 ,

where the k's are positive real numbers, then

Vol M = 1 2 ,                         c1(L)    Vol M  =  1  (1  2  +    2 1) .
                                       [M ]              2

The formulae of Lemma 2.6 can be applied to obtain

               s(L^)  =    1    =  1  -  c1(L^)  +    r+1   c1(L^)2  ,
                         c(L^)                         2r

where the first Chern class of the Fourier-Mukai transform L^ - M^ is

                          c1(L^) = - 2 dx1  dxm +1 - 1 dx2  dxm +2 .

In this expression the dxk's are the generators of H1(M^ , Z) dual to the dxk's. Similarly,
the cohomological Fourier-Mukai transform of the Ka�hler class of M is

               F ([M ]) = - 2 dx1  dxm+1 - 1 dx2  dxm +2 .

The volume of the vortex moduli space can then be explicitly computed through (4.6).

The result is                                         42 r  ( )r ,
                                                      e4      r!
               Vol (M, M) =  (Vol M)             +

where r = r(L) = 12 and  is the parameter (2.2).

4.3 Abelian GLSM

The K�ahler class
In this section we will compute the Ka�hler class of the metric on the moduli space for
general abelian gauged linear sigma-models. This will be done both when M is simply

                                                       31
connected and when it is an abelian variety. The essential ingredient is the abstract

formula of Perutz for the Ka�hler form M, or, more precisely, its generalization to gauged
sigma-models and higher dimensional manifolds [Ba4]. This formula presents M as the
fibre integral

M =                 k  i  a   FAa    Mm  +          1  1)!  FAa    FAa     Mm-1  ,     (4.7)
                  a=1  2  m!                  4e2(m -
               M

where FA is the curvature on the universal bundle U  M � M. Since this is a prin-
cipal T k-bundle, the curvature is a 2-form on the base with values in iRk. Taking the

cohomology class we then have

[M] =       k   a  c1(U a)  Mm       -        2      c1(U a)  c1(U a)  Mm-1         .  (4.8)
          a=1  m!                        e2(m - 1)!
       M

When M is simply connected the vortex moduli space is the toric orbifold given by

Proposition 3.6. We will assume that conditions (C1) and (C2) of Section 3.2 are satisfied,
so that M is smooth. Then the Chern classes c1(Ua) are given explicitly by Lemma 3.7.
It is now straightforward to perform the fibre integration and obtain:

Proposition 4.3. Let M a compact and simply connected Ka�hler manifold. The K�ahler
class of the L2-metric on the vortex moduli space (3.13) is

                                         k

                              M =              a a ,                                   (4.9)

                                         a=1

where  is the stability vector (3.4) and the classes a  H2(M, Z) were defined in (3.18).

When the manifold M is an abelian variety, the moduli space M is the toric fibration
over Pic0(M) described in Proposition 3.8. The Chern classes c1(Ua) are in this case
given by Lemma 3.9. The fibre integration over M can be performed in a way completely
analogous to the case of vortices on line bundles (cf. proof of (4.5)) to yield:

Proposition 4.4. Let M be an abelian variety. The K�ahler class of the L2-metric on the
vortex moduli space (3.22) is

                       k                 22              [Mm-1]
                                         e2             (m - 1)!
          M       =          a a     -        proja  F                  ,

                       a=1

where  is the stability vector (3.4), the classes a  H2(M, Z) were defined in (3.23) and
F is the cohomological Fourier-Mukai transform F : H2m-2(M; R)  H2(M^ ; R).

Volumes of moduli spaces

The volume of (M, M) can in principle be computed using our knowledge of the Ka�hler
class [M] and of the cohomology ring H(M, Z). For a general abelian GLSM, however,

                                                       32
the intersection calculations in the cohomology ring are algebraically evolved, since the
moduli space M may be a complicated toric manifold or, in the case of abelian varieties,
may be an even more complicated toric fibration over the Picard group Pic0(M). So it is
difficult to present a clean and general formula for the volume or total scalar curvature
of the moduli space. In this paragraph we will carry out the computations only for the
simplest examples. These will be GLSM with group U(1) and n sections 1, . . . , n, where
U(1) acts with weight 1. As we will recall in Section 5, these models are closely related
to holomorphic maps M  CPn-1. We will perform the calculations in the case where
M is simply connected or when it is an abelian variety of complex dimension 2.

(1) Suppose that P  M is a U(1)-principal bundle over a simply connected manifold.
Using the notation of Section 3, we will consider the associated GLSM with integral
weights Q1 = � � � = Qn = 1. In this case the line bundles L1, . . . , Ln are all isomorphic,
so the j's can be regarded as sections the same line bundle, which we call simply L.
Proposition 3.6 says that for this model the vortex moduli space is the projective space

M  CP n r(L) - 1 ,

where r(L) denotes the complex dimension of the space of holomorphic sections H0(M; L).
Proposition 4.3 says that the Ka�hler class is [M] =   , where  is the standard positive
generator of the cohomology ring of projective space. Thus we have

Vol (M, M)  =          ( )n r-1 .                (4.10)
                        nr - 1 !

The total scalar curvature of (M, M) is still given by formula (4.4). A few explict values
of r(L) for explict manifolds M are given in the examples of Section 2.2.

(2) Consider the same GLSM as above, but now over an abelian variety M of complex
dimension 2, as is Example (2) of Section 4.2. The moduli space M is in this case a
projective bundle over the dual variety M^ with fibre CP n r(L) - 1. Computations similar
to those of Section 4.2 then lead to

Vol (M, M) =  (Vol M)    +  42 n r  ( )nr     .
                             e4      (nr)!

4.4 Abelian GLSM with polynomial constraints

In this paragraph we make a short digression to consider GLSM with polynomial con-

straints. These models are relevant to the study of holomorphic maps from M to projective

varieties [MP]. Take the simple case of the gauged linear sigma-model with group U(1)
and weights Q11 = � � � = Q1n = 1. Then all the complex line bundles Lj are isomorphic to
a given L  M. The variables in the vortex equation are a connection A and n sections
1, . . . , n of this bundle. Now let S(z1, . . . , zn) be a complex homogeneous polynomial

of degree l. It makes sense to write the equation

S(1, . . . , n) = 0                              (4.11)

            33
in the space of sections of the bundle lL. We can thus look for vortex solutions of the
model that satisfy the additional constraint (4.11). This will define a subspace MS of the
moduli space M.

    When L is positive and Pic(M)  Z and the stability condition (2.2) is satisfied,

Proposition 3.6 states that the vortex moduli space for this GLSM is the projective space
M  CP n r(L)-1. As usual, r(L) stands for the complex dimension of the space of holo-

morphic sections of the bundle L equipped with its unique holomorphic structure. In this
case, it is clear that the subset MS cut out by condition (4.11) will then be a projective
variety inside M. In fact, choosing a basis of the r(L)-dimensional space H0(M, L) and
a basis of the r(lL)-dimensional space H0(M, lL), the vector-valued polynomial equa-
tion (4.11) can be rewritten as a set of r(lL) complex-valued homogeneous polynomial

equations of degree l. The variables of these equations are the components of the sections
j with respect to the chosen basis of H0(M, L), which are precisely the homogeneous co-
ordinates on the projective space M. In general the projective variety MS  CP n r(L)-1

may not be smooth. All depends on the polynomial S and on the values r(L). For a
generic choice of S, however, the constrained moduli space MS  M is indeed a smooth
projective variety of complex dimension n r(L) - 1 - r(lL). The Poincar�e-dual of the
homology class [MS] is

                  PD([MS]) = (l )r(lL)   H2 r(lL)(M, Z) ,

where  is the standard positive generator of the cohomology of projective space. It
follows that the volume of the submanifold MS equipped with the metric induced by the
L2-metric on the moduli space M is

Vol (MS, M |MS )  =        1       (M)dim MS  PD([MS])  =  ( )dim MS l r(lL)  .
                     (dim MS)!                                 (dim MS)!
                                M

5 Holomorphic maps to toric manifolds

5.1 Vortices and maps to projective space

Let M be a compact Ka�hler manifold and let H denote the (generally non-compact) space
of holomorphic maps f : M  CPn-1. Here we will describe a natural embedding of H
into a compact vortex moduli space. The necessary ingredients are the Hitchin-Kobayashi
correspondence of Section 3.1 and a standard construction in complex algebraic geometry.
Everything here is well known, at least when M is a Riemann surface [BDW]. This
exposition is a preamble to Section 5.2, where we study the space of maps M  X to
more general toric targets. Nevertheless, the basic ideas already appear and are easier
to grasp when the target is CPn-1. In the final Section 5.3 we make natural conjectures
about the relation between the L2-metrics on H and on M.

    There is a well known construction [GH] that identifies the space of maps H with a
subset of the space M of possible choices of "a holomorphic line bundle L  M plus n
holomorphic sections, up to common rescaling of the sections". In fact, it is easy to see

                                34
that such data (L, 1, . . . , n) determine a holomorphic map f(L,) by the simple definition

f(L,) : M - CPn-1                    (5.1)
           x - 1(x), . . . , n(x) ,

where we are using homogeneous coordinates on the projective space. The map f(L,) is

globally well defined if and only if the sections 1, . . . , n do not vanish simultaneously

at any point x  M. In this case f(L,) is clearly holomorphic, for the sections j are all
holomorphic. If we denote by H  CPn-1 the hyperplane bundle, one can also show that

f(L,) c1(H) = c1(L)                  (5.2)

in H2(M, Z). So the correspondence between holomorphic maps and systems of sections
of line bundles preserves topological sectors. Now denote by I  M the (generally
non-compact) subset defined be the condition that the sections 1, . . . , n do not vanish
simultaneously anywhere on M. So far we have described a map I  H. We will now
describe the inverse H  I. This implies that the correspondence H  M is an injection
with image I. The inverse acts as follows: given a map f  H, just define L := f H
and take the n holomorphic sections to be j := f sj, where s1, . . . , sn are the elements
of the standard basis of H0(CPn-1; H) provided by the n homogeneous coordinates on
projective space. This correspondence has values in I  M and clearly is the inverse of
the correspondence (5.1).

    Having described the map H  M, it is natural to ask whether H embeds as an
open and dense subset of M. The answer is that this need not be the case. In fact,
it is clear that (L, 1, . . . , n) belongs to the subset I  M precisely if the intersection
D1  � � �  Dn of the associated zero-set divisors is empty. When M is Riemann surface,
this is generically true, since different divisors of points do not in general intersect. For
higher-dimensional M, however, the divisors have support along hypersurfaces, and the
generic intersection may not be empty. For instance, when M is a projective space, we
know that the codimension of the intersection of generic projective varieties is the sum
of the codimensions of the varieties. This implies that for a generic choice of divisors the
intersection D1 � � �Dn is empty if and only if n > dimC M. So the space of holomorphic
maps CPm  CPn-1 of positive degree embeds as an open dense subset of M iff n > m.

    Note that so far in this Section we have defined M to be the space of possible choices of
"a holomorphic line bundle L  M plus n holomorphic sections, up to common rescaling
of the sections". However, as was seen in Section 3.1, this space can be identified with
a vortex moduli space. It coincides with the moduli space for the GLSM with goup
U(1) and integer weights Q11 = � � � = Q1n = 1, assuming that the stability parameter
(3.4) is positive. Regarding M as vortex moduli space has the advantage that it now
comes equipped with a natural Ka�hler metric -- the metric defined in (1.7) and studied
in Section 4. Since the space H of maps also has a natural L2-metric, one may wonder
if there is any relation between these two metrics under the embedding H  M. This
question was posed in [Ba4] in the case where M is a Riemann surface. In Section 5.3 we
extend the arguments and conjectures of that reference to higher-dimensional M.

35
5.2 Vortices and maps to toric manifolds

Toric manifolds

Let X be a smooth and not necessarily compact toric manifold of complex dimension n-k.
We will think of it as a symplectic quotient of Cn by a linear, effective and hamiltonian
T k-action with integer weights Qaj , where the indices run as a = 1, . . . , k and j = 1, . . . , n.
This means that X is the quotient space

                        X := �-1(0) / T k ,

with moment map � : Cn  iRk given by

                 � (z)  =  -   i      n                                            (5.3)
                               2
                                         Qj |zj|2 -  .

                                      j=1

As in Section 3.1, denote by  the closed cone in Rk defined by linear combinations of the
weights Qj  Zk with non-negative scalar coefficients. We will assume that the weights
and the constant   Rk satisfy conditions similar to those of Section 3.2, namely:

(H1) The vector   Rk lies in the cone , but does not lie in any of the proper subspaces
of Rk spanned by proper subsets of weights Qj.

(H2) Every subset of weights in {Q1, . . . , Qn} that spans Rk also generates the integer
lattice Zk in Rk.

These two conditions guarantee that the quotient is indeed smooth of dimension n-k. One

can also think of X as a complex quotient of Cn. In this case one uses the complexified

(C)k-action on Cn with the same integer weights, and considers the so-called stable

subset B := (C)k � �-1(0) of the vector space Cn. This is clearly a (C)k-invariant

subset. It follows from condition (H1) and Lemma A.3 that B is open and dense inside
Cn. Moreover

                           X = B /(C)k .                                           (5.4)

All these observations are standard facts in toric geometry and can be recognized by
arguments similar to those used in Lemma 3.5 and Proposition 3.6.

    It is well known that the cohomology ring H(X; Z) of such a toric manifold is gen-

erated by a set of natural (1, 1)-classes. These are the first Chern classes of the k line

bundles Ha  X. Recall that Ha is defined as the quotient of the cartesian product
�-1(0) � C by the free T k-action

                               k                            k

g � (z1, . . . , zn; w) := z1         (gb)Q1b , . . . , zn       (gb)Qnb ; ga w ,  (5.5)

                               b=1                          b=1

where z1, . . . , zn are complex coordinates on Cn, the ambient space of �-1(0).

Holomorphic maps as vortices
Let H denote the space of holomorphic maps f : M  X with its usual topology. It
can be broken into distinct topological components according to the values of the pulback

                                                       36
classes f  c1(Ha) in the integer cohomology of M. For each vector

  k

     H2(M, Z)  H(1,1)(M, C) ,

we denote by H the subspace of holomorphic maps f such that f  c1(Ha) = a for all
indices a. Now let P  M be a principal T k-bundle with c1(P ) = . As in Section 3,
we can consider the GLSM on the manifold M associated to P and the weights Qja. The
vortex equations for this theory are as in (3.1). It is clear from the definition (3.4) of 
that, for a sufficiently big value of the constant e2, the assumptions (H1) and (H2) above
imply the analogous conditions (C1) and (C2) of Section 3.2. So in this case the vortex
equations will have the nice set of solutions described in that Section. Making explicit
the Chern class of the principal bundle, we will denote by M this vortex moduli space.

Proposition 5.1. Assume that condition (H1) is satisfied. If the constant e2 is sufficiently
large there exists a natural holomorphic embedding H  M. The image I  M of
this map consists of the vortex solutions [A, 1, . . . , n] such that, for every point x  M,
the vector  is in the interior of the cone  , I(x) where we have defined the index subset
I(x) = {j  {1, . . . , n} : j(x) = 0}.

Remark. It can happen that the subset I  M is empty, so in this case H will also
be empty.

To describe the embedding H  M, take any map f  H and consider again the k
holomorphic line bundles Ha - X. (Each Ha has a natural hermitian metric, so can be
thought of as being a line bundle, a principal C-bundle, or a principal circle bundle; we
will switch between these three viewpoints.) Defining Pa := f Ha, the cartesian product
P = �kPa is a T k-bundle over the manifold M with first Chern class c1(P ) = . Moreover,
it is apparent from definition (5.5) that the tensor product ak=1 (Ha)Qja - X is a line
bundle with a natural section determined by the simple rule

sj : [z1, . . . , zn] - [z1, . . . , zn; zj] .                     (5.6)

This means that each associated bundle

                             Lj := ka=1 (Pa)Qaj = f  ka=1 (Ha)Qja

has a natural holomorphic section j := f sj. So each map f  H determines a holo-
morphic (C)k-bundle P - M and n holomorphic sections j of the associated bundles
Lj. These correspond to a unique equivalence class of vortex solutions, i.e. to a point in
M, provided that the Hitchin-Kobayashi correspondence of Theorem 3.2 is applicable,
and this follows from the lemma below.

Lemma 5.2. Let If be the index subset {j  {1, . . . , n} : f sj  0}. Then for big enough
e2, the parameter (3.4) can be written as a linear combination jIf j Qj with positive
scalar coefficients, i.e.  is in the interior of the cone If .

     37
Proof. For each index j = 1, . . . , n denote by Bj the subspace of Cn determined by the
equation zj = 0. Since our toric manifold is the quotient X = �-1(0)/T k, the intersection
�-1(0)  Bj projects down to a (possibly empty) submanifold Xj  X. From definition

(5.6) it is clear that the section sj vanishes precisely along this submanifold Xj. In
particular the pulback section f sj is identically zero if and only if the image f (M) is

contained in Xj. This means that

                                             f (M )  Xj .

                                                                                        j If

A fairly uncontroversial consequence of this relation is that the set on the right-hand-side
is not empty. Upstairs on Cn, this means that the set jIf Bj intersects �-1(0). Having
a look at the definition (5.3) of the moment map, this clearly implies that there exists
a subset I  If such that it is possible to write  = jI j Qj with positive scalar
coefficients. The subset I is not empty because of assumption (H1). By Lemma A.3 in
the Appendix, it is also possible to write  = jIf j Qj with positive scalar coefficients,
so summing through the whole If . Finally, it is apparent from definition (3.4) that for
sufficiently large e2 the stability parameter  is arbitrarily close to the value  Vol M in
Rk. Thus for big enough e2 it is possible to write this parameter as a linear combination
 = jIf j Qj with positive scalar coefficients, as desired.

We have described above how to obtain a vortex solution in M from a holomorphic map
f : M - X. That solution is defined by putting j = f sj. Now we have to show that
it belongs to the image I as defined in the statement of Proposition 5.1.

Lemma 5.3. Assume condition (H1). Then the vector  is in the interior of the cone
If(x) for every point x  M , where If(x) is the index subset {j  {1, . . . , n} : f sj(x) =
0}.

Proof. The proof is similar to the one of Lemma 5.2. Using the notation and the arguments
of that proof, we have that

f (x)            Xj .

        jIf (x)

Upstairs on Cn this means that the set  B jIf(x) j intersects �-1(0). Condition (H1) and
the definition (5.3) of the moment map then imply that there exists a non-empty subset

I  If(x) such that it is possible to write  = jI j Qj with positive scalar coefficients.
By Lemma A.3 in the Appendix, the same is true for the whole If(x).

    So far we have constructed a map H  I. Now we will describe its inverse, therefore
showing that it is injective.

Lemma 5.4. The map of Proposition 5.1 has a holomorphic inverse I  H defined on
its image.

Proof. As before, denote by B  Cn the open, dense and (C)k-invariant subset of points
(z1, . . . , zn) such that the parameter  is in the positive cone generated by {Qj : j  Iz},

        38
with Iz := {j  {1, . . . , n} : zj = 0}. The representation (5.4) of the toric manifold X
shows that there is a standard holomorphic projection  : B - X. A vortex solution
[A, 1, . . . , n] belongs to the subspace I precisely if the the images (1(x), . . . , n(x))
are in B for all x  M. So for any such vortex solution the composition f :=    is a
map M - X. It is a holomorphic map because of the first vortex equation, i.e. because
it is possible to find local trivializations of the line bundles such that the sections j are
all holomorphic. It is straightforward to check that the line bundles (f)Ha have Chern
class a and that, for all x  M, we have

                                           (f)sj(x) = j(x) .

Thus the image of f by the map H  I is gauge equivalent to the original vortex
solution, and we have constructed the desired inverse holomorphic map I  H.

Generic vortex solutions and holomorphic maps

In this paragraph we ask whether the space H of holomorphic maps to toric targets
embedds as an open and dense subset the vortex moduli space M. A general criterion

for this to happen is presented. When the base M is a projective space this criterion is

much simpler.

    Consider the stable subset B  Cn. It can be described both as the set of orbits
(C)k � �-1(0), or as the set of points (z1, . . . , zn) in Cn such that the parameter  is in
the positive cone generated by {Qj  Rk : zj = 0}. If assumption (H1) is satisfied, it is a
consequence of Lemma A.3 that B is open and dense in Cn. The complement Cn \ B
is a union of certain coordinate planes E in Cn of different codimensions. Each of these
planes is defined by a set of equations

           zj1() = � � � = zjn-l() = 0 ,                   (5.7)

where l = l()  0 is the complex dimension of the plane. Now, a vortex solution
(A, 1, . . . , n) is in the image I  M of the embedding if and only if for every point
x  M the value (x) is in the subset B ; more precisely, if and only if, for every plane
E, the section j1()  � � �  jn-l() never vanishes. So we have:

Represent the complement Cn\B as a union E of maximal planes defined by equations
of the form (5.7). Then the space of holomorphic maps H embeds as an open dense subset
of the vortex moduli space M if and only if, for all , the generic holomorphic section
of Lj1()  � � �  Ljn-l() never vanishes.

    A more concrete result can be stated when the base M is a projective space. To
make this statement, consider again the maximal coordinate planes E in Cn \ B and
the corresponding sub-bundles Lj1()  � � �  Ljn-l(). To each such plane associate the
integer s defined by the following two conditions:

(i) s = -  if Ljr() is trivial for some 1  r  n - dim E ;

(ii) s = dim E + # 1  r  n - dim E : H0(M ; Ljr()) = 0     otherwise .

           39
This integer is well defined, for when M is simply connected the dimension of the space of
holomorphic sections H0(M; Ljr ) is an unambiguous characteristic of the only holomorphic
structure on Ljr . Now consider the maximum value

s := max         s                               (5.8)


among all planes E. This maximal integer s depends only on the constants Qja and 
that determine the quotient X, and on the cohomology class  that determines the Lj's.

Then we have the following result.

Proposition 5.5. Assume that M is a projective space and that (H1) is satisfied. Then
the space of holomorphic maps H embeds as an open dense subset of the vortex moduli
space M if and only if n - s > dimC M.

Proof. As stated before, a vortex solution (A, 1, . . . , n) is in the image I  M of the
embedding if and only if for every point x  M the value (x) is in the stable set B .
Now consider a maximal coordinate plane E in the complement Cn \ B . Without loss of
generality, we may assume that E is defined by the set of equations z1 = � � � = zn-l() = 0,
where l() denotes the dimension of E. The solution (A, ) belongs to I only if the

sections 1, . . . , n-l() do not have a common zero; otherwise, at that common zero, (x)

would be in the plane E, so outside B . Among these sections, a certain number will
always be identically zero, because H0(M ; Lr()) may be zero, i.e the bundle Lr() may

have negative degree. This will happen for

m := # 1  r  n - l() : H0(M ; Lr) = 0 = s - l()

sections. After relabeling if necessary, we can assume that the sections that are always
zero are n-s+1, . . . , n-l(). The remaining sections 1, . . . , n-s will generically be
non-zero, and will vanish along a divisor in M or will not vanish at all. So the condition
that (x) lies outside the plane E for all x  M is reduced to the condition that the
intersection of the corresponding zero-sets Z(1)  . . .  Z(n-s) is empty in M. If any
of the bundles L1, . . . , Ln-s is trivial, then its generic section will not vanish at all in
M, and hence the intersection of the zero-sets will always be empty. If all the bundles
L1, . . . , Ln-s have positive degree � the remaining case � then the intersection of zero-sets
will be an intersection of n - s divisors in M. When M is a projective space, this last
intersection is generically empty iff n - s > dimC M. Thus a generic  has values outside
the plane E iff n - s > dimC M. Doing the same for all other planes E, we conclude
that a generic  has values outside the union E if and only if n - s > dimC M, where
s is the maximum of the s's.

Example. When the target X is also a projective space CPn-1 = (Cn - {0})/C, there
is only one plane E: the origin {0}. Thus lE = dim E = 0. As described in Section 5.1,
the space H of holomorphic maps then embeds in the vortex moduli space of the GLSM
with group U(1) and integer weights Q11 = � � � = Qn1 = 1. In this case the line bundles
L1, . . . , Ln are all isomorphic, so if they are positive we have that mE = 0 and s = 0. In
this case H is open and dense in M if and only if n > dimC M.

40
5.3 Conjectures about the L2-metrics

Consider again the spaces H of holomorphic maps M  X to toric targets. These spaces
have a natural complex structure induced by the complex structures of the domain M

and of the target X. They also have a compatible Ka�hler metric H determined by the
norm

df              2  :=           |df |2 =              (gM ) (f j) (f l) (gX)lj .  (5.9)
                H
                       (M,gM )               (M,gM )

This is usually called the L2-metric on H. It is defined also for more general spaces of

maps between Riemannian manifolds, not necessarily holomorphic maps. Since one can

regard H as embedded in the vortex moduli space M, and the latter space has the natural

L2-metric M, it is natural to ask whether this is an isometric embedding or not. In [Ba4]

it was argued that this should be the case if: (1) one takes the metric gX on the toric
target to be the symplectic quotient of the standard euclidean metric on Cn determined

by the moment map (5.3), and, (2) one takes the strong coupling limit e2  . (Recall

that both the vortex equations and the metric M on the moduli space are e2-dependent.
The moduli space itself, i.e. the complex manifold M, is not, at least for e2 large enough.)

The heuristic arguments of that reference should hold also in the case of higher-dimension

M, so we have:

Conjecture 5.6. Take the metric on H induced by the metric (1.7) on the vortex moduli
space through the embedding H  M of Proposition 5.1. Then in the limit e2  
this metric converges to the natural L2-metric (5.9) on H.2

When H embeds as an open dense subset of the vortex moduli space, the conjecture
above says that as e2   the pointwise limit of the vortex metric M over the domain
H  M coincides with the natural L2-metric H. On the complement M \ H the

vortex metric M may very well diverge in this limit. In fact, it is clear from the vortex

equation

                       FA - ie2              Qj |j|2 -  = 0

                                          j

that when e2 goes to infinity the curvature FA must explode at the points x  M where
the argument of the square bracket cannot vanish, i.e. at the points such that  is not

in the interior of the cone I(x) (see Proposition 5.1). So FA explodes if the vortex
solution is not in the image H  M. It is then plausible that, in the limit e2  ,
the metric M also diverges outside H. Moreover, there are known examples where the
scalar curvature of H diverges as one approaches the boundary H. So if the conjecture
is to hold, at least in these examples the limit of M must also diverge at H.

    Assuming the validity of the conjecture above, one can go one step further by exchang-
ing the limit with the volume integral and propose:

2This conjecture has now been proved in the case of maps from Riemann surfaces to projective space.
 The proof is presented in [Liu], and appeared on the arXiv after the first version of the present article.

                                             41
Conjecture 5.7. When H embeds as an open dense subset of M, the volume of (H, H)
coincides with the limit

         Vol (H, H)      =   lim  Vol (M, M)   .

                            e2+

The total scalar curvature of (H, H) can also be obtained as the e2   limit of the
total scalar curvature of (M, M).

This conjecture was used in [Ba4] to propose explicit formulae for Vol (H, H) and the
total scalar curvature of H in the case where M is a Riemann surface and X is a projective

space. The volume formula was checked by Speight through a direct computation in the
special case of maps CP1 - CPn-1 of degree 1 [Spe]. By the same token, here we can

use the results of Section 4 to propose formulae for the volume of the space of maps
M  CPn-1 when M is higher-dimensional.

Example

Take M to be simply connected with H2(M, Z)  Pic(M)  Z and the target X to be
the projective space CPn-1. We take the metric on CPn-1 to be  F S, where  > 0 and
F S stands for the Fubini-Study form normalized so that its cohomology class generates
H(CPn-1, Z). Any holomorphic map f : M  CPn-1 has a well defined integer degree
d. If there exists a positive generator E  M of the Picard group and H  CPn-1 is the

hyperplane bundle, the degree is determined by the equation

                         f  c1(H) = d � c1(E)

in H2(M, Z). Proposition 5.1 says that for large e2 we have an embedding Hd  Md.
Observe that the degree on the vortex moduli space coincides with the degree defined in

Example (2) of Section 2.2, as follows from (5.2). If the degree d is negative, the moduli
space Md is always empty, and hence so is the space of maps Hd. If d is zero, Proposition
3.6 says that M0  CPn-1, hence H0 is just the space of constant maps M  CPn-1. If
the degree d is positive and e2 is large, Proposition 3.6 says that Md  CP nr-1, where
the integer r is the complex dimension of H0(M; Ed).

    Now specialize to the case where the base M = CPm is also a projective space. Then
according to Proposition 5.5 and the remark following it, Hd will embed as an open dense
subset of CP nr-1 if and only if n > dim M. If this last condition is satisfied we can use the

volume computations of Section 4.3, together with Conjecture 5.7, to propose the formula

         Vol (Hd, H)  =   lim ( )n r-1  =      (  Vol M )n r-1 .
                         e2+ nr - 1 !               nr - 1 !

Here r is the integer (m + d)!/(m! d!), and we are assuming that m and d are positive.
The total scalar curvature of (Hd, H) should be given by

            s(H) volH =   2 nr (nr - 1)      Vol Hd (nr-2)/(nr-1) .
                         (nr - 1)! 1/(nr-1)
         Hd

                            42
Acknowledgements. I would like to thank CAMGSD and Project PTDC/MAT/119689/2010
of FCT - POPH/FSE for a generous fellowship.

A Appendices

A.1 Limits of the vortex equations

In this appendix we make very informal observations about the strong and weak coupling
limits of the vortex equations, i.e. the limits where the constant e2 is large or small. We
will do so for the simplest abelian equations, namely equations (1.3)-(1.5) for vortices on
a positive line bundle L - M.

Limit e2  

In physics this is called the strong coupling limit. Start by noting that for positive  the
stability condition (2.2) is satisfied for arbitrarily large values of e2. This means that, as a

complex manifold, the vortex moduli space M does not change for big and growing values
of e2. It always coincides with the space of effective divisors on M carrying a homology
class Poincar�e-dual to c1(L). Observe from expression (1.6) that, when e2  , the
energy of each vortex solution tends to the finite positive constant

              Evortex        2       c1(L)  .
                           (m - 1)!
                        M

On the other hand, looking at definition (1.1) of the functional E(A, ), we recognize that
for the energy to remain finite in this limit we must have

              (||2 -  )  0

almost everywhere on M. This is also suggested by the formal limit e2   of the second
vortex equation (1.4). Note, however, that over the effective divisor D  M corresponding
a vortex solution (A, ), the section  is always zero, independently of the value of e2.
So for each vortex solution the picture is that the norm ||2 tends to  everywhere on M
except along the corresponding divisor D, where ||2 remains zero. The second vortex
equation

                                       i FA + e2 ||2 -  = 0

then implies that the curvature FA must explode over D in the strong coupling limit.
The ideal picture would be that the curvature gradually concentrates around the divisor
as e2  . Lets now look at the volume of the moduli space in the example where
M is an abelian variety. As is explained in Section 2, in this case the moduli space is
a projective bundle M - Pic0M over the Picard group. The "size" of the fibres and
base of this bundle is determined by expression (4.5) for the Ka�hler class. As e2  ,
we see that the contribution of the fibres remains finite, while the contribution the base
becomes smaller and smaller. So, metrically, the moduli space M becomes a projective
bundle over an infinitesimally small torus.

                        43
Limit e2  0 with constant e2 

Start by observing that if the stability condition (2.2) is satisfied for some finite values of
 and e2, then it is also satisfied for arbitrarily small values of e2 as long as  e2 remains
constant. Once again, this means that the moduli space M does not change as a complex
manifold when we approach this limit. Now observe that the formal limit of the second
vortex equation is in this case

                                            FA - i e2  = 0 .

This suggests that, for each vortex solution, when e2  0 with constant e2  , the con-
nection A approaches a Hermitian-Einstein connection on L - M. If M is simply
connected, there is a unique such connection, up to gauge transformations. When M is
an abelian variety, the Hermitian-Einstein connections on L are parametrized by Pic0M.
In this case M is a projective bundle over Pic0M, and we expect that the connections
of the vortex solutions corresponding to the same projective fibre in M will all converge
to the same Hermitian-Einstein connection on L. Regarding the Ka�hler class of M, it
follows from (2.2) and (4.5) that both the "size" of the projective fibres and the "size" of
the base Pic0M diverge in the limit e2  0 with constant e2  .

A.2 Auxiliary lemmas

In this appendix we collect two algebraic lemmas about torus actions on vector spaces.
These are relevant to understand the stability condition for toric quotients and the related
gauged linear sigma-models (GLSM).

Lemma A.1. Take a constant     Rk and assume that condition (H1) of Section
5.2 is satisfied. Then there exists an index subset I0  {1, . . . , n} of cardinality k such
that we can write  = jI0 j Qj with positive scalar coefficients. There is no index
subset of smaller cardinality with the same property.

Proof. For each non-empty index subset I  {1, . . . , n} consider the closed cone

               I := v  Rk : v = j Qj with j  0 .

                                                            jI

Condition (H1) says that   I for any subset I of cardinality less than k. Define I to

be an index subset of cardinality k -1 such that the euclidean distance between  and I

is minimal among the (positive) distances between  and the closed cones corresponding
to all index subsets of cardinality k - 1. Call v  I the vector inside this cone that
minimizes the euclidean distance to  . Then  - v is a non-zero vector orthogonal to v.

Observe that there exists an element j0  {0, . . . , n} such that the vector Qj0 has positive

inner product

                      Qj0 � ( - v) > 0 .                                           (A.1)

If this were not true, the assumption that    would imply that

               0   � ( - v) = ( - v) � ( - v) ,

                      44
which is impossible. Taking this index j0, consider the 1-parameter family of vectors

                                      vt := v + t Qj0 for t  0 .

The euclidean norm of each of these vectors is

                      - vt 2 =  - v 2 - 2 t Qj0 � ( - v) + t2 Qj0 2 ,

so from (A.1) it is clear that for small  > 0 the distance  - v 2 is strictly smaller than
the distance  - v 2. In particular j0 must not belong to I, otherwise v would be inside
I and this would contradict the definition of v. So the index subset

                                               I0 := I  {j0}

has cardinality k. We will now show that  belongs to the closed cone I0. Suppose that
this was not true and that  was outside I0. Then the closest point to  inside I0,
which we call v, would necessarily be on the boundary I0. This boundary is the union
of the closed cones determined by the subsets of I0 of cardinality k - 1. In particular
there would be a subset I  I0 of cardinality k - 1 such that v  I. Therefore the
distance from the cone I to  would be equal to or smaller than the distance from the
cone I  I0 to  . By the minimizing assumptions in the definition of I, this distance
cannot be smaller, so it must be equal. Thus

                                            - v 2 =  - v 2

is the shortest distance between the cone I0 and  . This is impossible because above we
have found a vector v  I0 whose squared distance to  is strictly smaller than  -v 2.
The conclusion is that  must belong to I0, and so be of the form  = jI0 j Qj with
j  0. Finally, assumption (H1) guarantees that none of the coefficients j is zero.

Lemma A.2. Let I  {1, . . . , n} be a non-empty index subset, let SI denote the subspace
of Rk spanned by the weights {Qj  Zk : j  I}, and let I  SI be the closed cone
generated by linear combinations of those weights with non-negative coefficients. Then a
vector   Rk is in the interior of the cone I (regarded as a subset of SI) if and only if
it can be written as  = jI j Qj with strictly positive scalar coefficients.

Proof. The condition that  can be written as jI j Qj with strictly positive scalar
coefficients is clearly an open condition in SI, i.e. if  satisfies it, so will all the vectors
in SI sufficiently close to . This shows that such a  is not on the boundary of the
cone I (regarded as a subset of SI), and so justifies the "if" part of the lemma. On the
other direction, suppose that the vector  is in the interior of I. Then for small enough
coefficients j > 0, the vector  =  - jI j Qj is still in the cone I. In particular we
can write  = jI j Qj for some choice of non-negative coefficients j . Thus

                                           = (j + j) Qj ,

                                                                            jI

where the coefficients j + j are all strictly positive, as desired.

                                                       45
Lemma A.3. Take a constant  = 0 in Rk and assume that condition (H1) of Section

5.2 holds. Let I  I be two non-empty index subsets of {1, . . . , n}. Then, if we can

write  = jI j Qj with positive scalar coefficients, we can also write  = jI j Qj
                                                                          n    j
with positive scalar coefficients. In particular, we can always write  =  j=1     Qj  with

positive scalar coefficients.

Proof. By assumption, the vector  is in the interior of the cone I generated by the
weights {Qj  Rk : j  I}. Condition (H1) implies that this cone is k-dimensional.
So for small enough positive coefficients j, the vector   =  - jI\I j Qj is still in
the interior of I, and hence we can write   = jI j Qj for some choice of positive
coefficients j. Thus

                               =      j Qj +           j Qj ,

                                  jI          j I  \I

as desired. To prove the last assertion, just note that condition (H1) implies that   I
for some non-empty index subset of I  {1, . . . , n}, and hence the assertion follows from

the first part of the lemma.

References

[Aud] M. Audin: Torus actions on symplectic manifolds, Progress in Mathematics 93,
          2ed, Birkhauser, 2003.

[Ban] D. Banfield: Stable pairs and principal bundles, Q. J. Math. 51 (2000), 417�436.

[Ba1] J. Baptista: A topological gauged sigma-model, Adv. Theor. Math. Phys. 9 (2005),
          1007�1047.

[Ba2] J. Baptista: Vortex equations in abelian gauged sigma-models, Commun. Math.
          Phys. 261 (2006), 161�194.

[Ba3] J. Baptista: Non-abelian vortices on compact Riemann surfaces, Commun. Math.
          Phys. 291 (2009), 799�812.

[Ba4] J. Baptista: On the L2-metric of vortex moduli spaces, Nucl. Phys. B 844 (2011),
          308�333.

[BBR] C. Bartocci, U. Bruzzo and D. Ruip�erez: Fourier-Moukai and Nahm transforms
          in geometry and mathematical physics, Progress in Mathematics 276, Birkhauser,
          2009.

[BDW] A. Bertram, G. Daskalopoulos and R. Wentworth: Gromov invariants for holo-
          morphic maps from Riemann surfaces to grassmannians, Jour. Amer. Math. Soc.
          9 (1996), 529�571.

[BS] I. Biswas and G. Schumacher: Coupled vortex equations and moduli: deformation
          theoretic approach and Ka�hler geometry, Math. Ann. 343 (2009), 825�851.

                                                       46
[BT] R. Bott and L. Tu: Differential forms in algebraic topology, Graduate Texts in
          Mathematics 82, Springer-Verlag, 1982.

[Bra1] S. Bradlow: Vortices in holomorphic line bundles over closed Ka�hler manifolds,
          Commun. Math. Phys. 135 (1990), 1�17.

[Bra2] S. Bradlow: Special metrics and stability for holomorphic bundles with global
          sections, J. Diff. Geom. 33 (1991), 169�213.

[BDGW] S. Bradlow, G. Daskalopoulos, O. Garc�ia-Prada and R. Wentworth: Stable
          augmented bundles over Riemann surfaces, Vector bundles in algebraic geometry,
          London Math. Soc. Lecture Note Ser. 208, Cambridge Univ. Press, 1995.

[Bri] M. Brion: Homogeneous projective bundles over abelian varieties, arXiv:
          1104.0818v3.

[CGMS] K. Cieliebak, R. Gaio, I. Mundet i Riera and D. Salamon: The symplectic vortex
          equations and invariants of Hamiltonian group actions, J. Symplectic Geom. 1
          (2002), 543�645.

[EINOS] M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai: Solitons in the Higgs
          phase � the moduli matrix approach �, J. Phys. A39 (2006), R315�R392.

[Gar] O. Garc�ia-Prada: Invariant connections and vortices, Commun. Math. Phys, 156
          (1993), 527�546.

[GH] P. Griffiths and J. Harris: Principles of algebraic geometry, Wiley, 1978.

[Har] R. Hartshorne: Algebraic geometry, Graduate Texts in Mathematics 52, Springer-
          Verlag, 1977.

[HP] W. Hodge and D. Pedoe: Methods of algebraic geometry Vol. II, Cambridge Univ.
          Press, 1952.

[Huy] D. Huybrechts: Fourier-Mukai transforms in algebraic geometry, Oxford Mathe-
          matical Monographs, Clarendon Press, 2006.

[JT] A. Jaffe and C. Taubes: Vortices and monopoles, Birkhauser, 1980.

[KW] J. Kazdan and F. Warner: Curvature Functions for Compact 2-Manifolds, Annals
          of Math. 99 (1974), 14�47.

[Ki] F. Kirwan: Cohomology of quotients in symplectic and algebraic geometry, Prince-
          ton Univ. Press, 1984.

[Ko] S. Kobayashi: Differential geometry of complex vector bundles, Iwanami Shoten
          Publishers and Princeton Univ. Press, 1987.

[H-al] K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil
          and E. Zaslow: Mirror symmetry, Amer. Math. Soc. and Clay Math. Institute,
          2003.

                                                       47
[Liu] C. Liu: Dynamics of Abelian Vortices Without Common Zeros in the Adiabatic
          Limit, arXiv: 1301.1407.

[MN] N. Manton and S. Nasir: Volume of vortex moduli spaces, Commun. Math. Phys.
          199 (1999), 591�604.

[MS] N. Manton and P. Sutcliffe: Topological Solitons, Cambridge Univ. Press, 2004.
[MP] D. Morrison and M. Plesser: Summing the instantons: quantum cohomology and

          mirror symmetry in toric varieties; Nucl. Phys. B440 (1995), 279�354.
[Mu] I. Mundet i Riera: A Hitchin-Kobayashi correspondence for Ka�hler fibrations,

          Jour. Reine Angew. Math. 528 (2000), 41�80.
[Pe] T. Perutz: Symplectic fibrations and the abelian vortex equations, Commun.

          Math. Phys. 278 (2008), 289�306.
[Sa] Y. Sakane: On hypersurfaces of a complex Grassmann manifold Gm+n,n(C), Osaka

          J. Math. 16 (1979), 71�95.
[Spe] J.M. Speight: The volume of the space of holomorphic maps from S2 to CP k, J.

          Geom. Phys. 61 (2011), 77�84.
[Tha] M. Thaddeus: Stable pairs, linear systems and the Verlinde formula, Invent.

          Math. 117 (1994), 317�353.
[To] D. Tong: Quantum vortex strings: a review, Annals Phys. 324 (2009) 30�52.
[We] J. Wehrheim: Vortex invariants and toric manifolds, arXiv: 0812.0299.
[Wi] E. Witten: Phases of N=2 theories in two dimensions, Nucl. Phys. B403 (1993),

          159�222.
[Wo] C. Woodward: Quantum Kirwan morphism and Gromov-Witten invariants of

          quotients, arXiv: 1204.1765.
[Zi] F. Ziltener: A quantum Kirwan map: bubbling and Fredholm theory of symplectic

          vortices over the plane, arXiv: 1209.5866.

Centre for Mathematical Analysis, Geometry, and Dynamical Systems (CAMGSD),
Instituto Superior T�ecnico, Av. Rovisco Pais, 1049-001 Lisbon, Portugal

Email address: [email redacted]

                                                       48
