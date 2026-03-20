# Baptista HD Routes Bosons 2021

**Source:** `04_Baptista_HD_Routes_Bosons_2021.pdf`

---

arXiv:2105.02899v3 [hep-th] 30 May 2023               Higher-dimensional routes
                                                   to the Standard Model bosons

                                                                               Joa~o Baptista

                                                                                  May 2021

                                                                                  Abstract

                                         In the old spirit of Kaluza-Klein, we consider a spacetime of the form P = M4 � K, where
                                         K is the Lie group SU(3) equipped with a left-invariant metric that is not fully right-
                                         invariant. This metric has a U(1) � SU(3) isometry group, corresponding to the massless
                                         gauge bosons, and depends on a parameter  with values in a subspace of su(3) isomorphic
                                         to C2. It is shown that the classical Einstein-Hilbert Lagrangian density RP - 2 on the
                                         higher-dimensional manifold P , after integration over K, encodes not only the Yang-Mills
                                         terms of the Standard Model over M4, as in the usual Kaluza-Klein calculation, but also
                                         a kinetic term |dA|2 identical to the covariant derivative of the Higgs field. For  in
                                         an appropriate range, it also encodes a potential V (||2) having absolute minima with
                                         |0|2 = 0, thereby inducing mass terms for the remaining gauge bosons. The classical
                                         masses of the resulting Higgs-like and gauge bosons are explicitly calculated as functions
                                         of the vacuum value |0|2 in the simplest version of the model. In more general versions,
                                         the classical values of the strong and electroweak gauge coupling constants are given as
                                         functions of the parameters of the left-invariant metric on K.
Contents

1 Introduction                                   3

2 A left-invariant metric on SU(3)               7

Decomposition of su(3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

General properties of left-invariant metrics . . . . . . . . . . . . . . . . . . . . . 8

A family of metrics on SU(3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

Killing vector fields of g . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Orthonormal basis and volume form of g . . . . . . . . . . . . . . . . . . . . . 13
Scalar curvature of g . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

3 Lagrangians and fibre-integrals on M4 � SU(3)  19

Submersive metrics on M4 � SU(3) and their scalar curvature . . . . . . . . . . 19

Yang-Mills terms on M4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

Fibres' second fundamental form and Higgs covariant derivatives . . . . . . . . . 24

Norm of the second fundamental form . . . . . . . . . . . . . . . . . . . . . . . 26

Mean curvature of the fibres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

Lagrangian densities on M4 � SU(3) . . . . . . . . . . . . . . . . . . . . . . . . 31
Vacuum configurations and Higgs-like potentials . . . . . . . . . . . . . . . . . . 35

4 Masses of the classical fields                 40

Higgs-like particle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

Gauge bosons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

Some numerical estimates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

5 Further investigations                         48

Higher-dimensional equations of motion . . . . . . . . . . . . . . . . . . . . . . 48

A more precise version of the model . . . . . . . . . . . . . . . . . . . . . . . . . 49

Full SU(3) � SU(3) gauge fields . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

A Appendices                                     61

A.1 A -rotated basis of su(3) . . . . . . . . . . . . . . . . . . . . . . . . . . . 61

                                    1
A.2 A proof about the Killing fields of g . . . . . . . . . . . . . . . . . . . . . 63
A.3 Weyl rescaling of gP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64

                                                    2
1 Introduction

Traditional Kaluza-Klein theories propose to replace four-dimensional Minkowski space-
time M4 with a higher-dimensional product manifold P = M4 � K, where the internal
space K is a Lie group or a homogeneous space with very small volume. The proposed
Lorentzian metric on P is not the simple product of the metrics on M4 and K, but has non-
diagonal terms that can be interpreted as the observed gauge fields on M4. Geometrically,
the projection P  M4 should be a Riemannian submersion with fibre K.

    The original Kaluza-Klein choice K = U(1) has the remarkable feature that geodesics
on P project down to paths on M4 satisfying the Lorentz law for moving electric charges.
For general choices of K, it can be shown that a natural quantity on P , namely its scalar
curvature RP , can be written as a sum of components that include the individual scalar
curvatures of M4 and K and, more remarkably, the norm |FA|2 of the gauge field strength.
Since the scalar curvature is also the Lagrangian density for general relativity, it follows
that the Einstein-Hilbert action on the higher-dimensional P produces, after projection
down to M4, two of the essential ingredients of physical field theories in four dimensions:
the Einstein-Hilbert and the Yang-Mills Lagrangians on M4.

    Kaluza-Klein theories, however, do present challenging difficulties when interpreted
simply as higher-dimensional versions of general relativity, i.e. as dynamical field theories
for a metric tensor on P that satisfies the full Einstein equations on the higher-dimensional
space. Although unifying and appealing, the direct extension of general relativity to
higher dimensions seems to imply the existence of many unobserved scalar fields satisfying
complicated equations of motion with few physically reasonable solutions. The new fields
generally do not bear much resemblance to the well-known field content of the Standard
Model. Moreover, following the interpretation of fermions in Kaluza-Klein theory as zero
modes of the Dirac operator on the internal space K, there does not seem to be a good
choice of Riemannian manifold K able to deliver the necessary zero modes in the chiral
representations appearing in the Standard Model. For reviews and discussions of Kaluza-
Klein theory from different viewpoints, see for instance [BL, DNP, Wi1, Wi2, OW, CJ,
Ho, Ble]. Some of the early original references are [K], with much more complete lists
given in the mentioned reviews.

    The plan of the present investigation is to dig deeper into some of the geometrical
aspects of the Kaluza-Klein framework and suggest that, besides the curvature |FA|2 of
the gauge fields, there are other natural objets in a Riemannian submersion that resemble
the field content of the Standard Model. For example, when the fibre K is a Lie group
equipped with a left-invariant metric, the second fundamental form of the fibres, denoted
by S, generates terms in the four-dimensional Lagrangian sharing notable similarities with

                                                        3
the covariant derivative of a Higgs field. See for instance the general formula (5.27) for the
norm |S|2, whose quadratic terms in the gauge fields are what is needed to generate the
gauge bosons' mass. When K is chosen to be the group SU(3) equipped with a specific
family of left-invariant metrics, denoted by g, then the terms generated by S contain the
precise covariant derivative dA that appears in the Standard Model, namely a C2-valued
Higgs field coupled to the electroweak gauge fields through the correct representation.

    In the companion study [Ba], we suggest possible ways to integrate fermions in this
picture. For an internal space K = SU(3), we regard fermions as spinorial functions on
the 12-dimensional spacetime M4 � K with a prescribed behaviour along K. A complete
generation of fermionic fields can then be encoded in the 64 complex components of a single
higher-dimensional spinor. Moreover, the vertical behaviour of this spinor can be chosen
so that, after fibre-integration over K, the resulting Dirac kinetic terms in four dimensions
couple to the u(1)  su(2)  su(3) gauge fields in the exact chiral representations present
in the Standard Model. Perhaps one could think of the prescribed vertical behaviour as
a sort of elementary, spinorial oscillation along the compact direction K.

Decomposing the higher-dimensional scalar curvature

This second part of the Introduction gives a brief description of the calculations that

motivate the present study. Let  be an AdSU(3)-invariant inner-product on the Lie algebra
su(3). Using the left-translations on the group, this product can be extended to a left-

invariant metric on the whole manifold K = SU(3). The Ad-invariance of  guarantees

that the resulting metric is bi-invariant on K, i.e. it has isometry group SU(3) � SU(3).

In this study we will consider a deformation g of the product  that extends to K as
a left-invariant metric that is no longer bi-invariant, but has the smaller isometry group

U(1)�SU(3). To do that, observe that any matrix in the Lie algebra su(3) can be uniquely

written as

            v=  - Tr(v) -(v)  ,                      (1.1)

                v     v

where v is an anti-hermitian matrix in u(2) and v is a vector in C2. This determines
a vector space decomposition su(3)  u(2)  C2 that is orthogonal with respect to .
Identifying v and v with their images in su(3), the deformed inner-product on this space

is defined by the three equations

             g(u, v) = (u, v)                        (1.2)
            g(u, v) = ( [u, v], )
            g(u, v) = (u, v) .

                   4
The deformation parameter is a vector   C2 after identification with the matrix

    -      su(3) .                                                               (1.3)


As in the usual Kaluza-Klein framework, the left-invariant metric gK = g on the internal
space K can be combined with a metric gM and one-forms A on Minkowski space to define
a submersive metric gP on the higher-dimensional space P = M4 � K. In our case, there
are two one-forms AL and AR on M4 with values in the Lie algebra su(3). Using a basis
{ej} of su(3), they can be decomposed as AjL ej and AjR ej. Now denote by ejL and eRj
the extensions of ej as left and right-invariant vector fields on K, respectively. We can
construct a one-form A on M4 with values in the space of invariant vector fields on K by
the formula

                                A(X) := j AjL(X) eLj - AjR(X) ejR

for all tangent vectors X  T M . Then the higher-dimensional metric on P is defined by

gP (V, V ) := gK(V, V )                                                          (1.4)
gP (X, V ) := - gK(A(X), V )
gP (X, X) := gM (X, X) + gK(A(X) , A(X)) ,

for all X  T M and all vertical vectors V  T K. This fully determines the higher-
dimensional metric. In this study we will investigate the scalar curvature of the metric
gP . A standard result in Riemannian submersions [Bes] says that it can be decomposed
as

                     RP = RM + RK - |F |2 - |S|2 - |N |2 - 2 N .

Here RM and RK are the scalar curvatures of the metrics gM and gK, respectively; |F |2
is the component that originates the Yang-Mills terms |FA|2 in the usual Kaluza-Klein
calculation; the tensor S is the second fundamental form of the fibres K, also called shape
operator; the vector N is the trace of S, which is a horizontal vector in T P usually called
the mean curvature vector of the fibres. On a Riemannian submersion, the tensor S
vanishes precisely if the all the fibres K are geodesic submanifolds of P . In this case all
the fibres will be isometric to each other. The vector N can be thought of as the gradient
in P of the volume of the fibres, which may vary as one moves along the base M4. Thus,
vanishing N means that all internal spaces have the same volume.

    Since the metric gP can be written as a function of gK, gM and the one-forms AL and
AR, the same must be true for all the terms of the scalar curvature RP . Now fix the choice
of internal metric gK = g. If we assume that the one-form AR has values in the full su(3)

       5
but AL has values in the smaller electroweak subalgebra u(2)  su(3), then the integral
has the following schematic result:

    RP - 2 P ) volg = -  1    |FAL |2 + |FAR |2  + C dAL  2
                         4 B
K

                         + D d ||2 2 + U (||2) + 2 M f       Vol(K, ) .

The coefficients B, C, D and f are functions of the norm ||2 in C2 that will be
explicitly computed later. Thus, the integral's result is a Lagrangian density on M4 that
contains: 1) strong and electroweak Yang-Mills terms; 2) the norm dAL 2 of a covariant
derivative coupling the field   C2 to the electroweak gauge fields AL, but not to the
strong force gauge fields AR; 3) a total derivative term M f that does not affect the
four-dimensional equations of motion; 4) a potential term

                                 U (||2) := (2 P - Rg - RM ) f ,

involving the scalar curvature RK = Rg and the volume density f of the internal space;
5) finally, a term proportional to the norm of the derivative d ||2 that only affects the
equations of motion of  and the mass of the Higgs-like boson. In the simplest versions
of the model, it can be shown that when the constant 2P - RM is larger than a certain
critical value, the potential U (||2) has absolute minima for ||2 = 0 and explodes to
positive infinity when ||2 approaches the boundary value 1/4. Overall, the result of the
fibre-integral over K is a density in M4 remarkably similar to the bosonic part of the
Standard Model Lagrangian.

    Sections 2 and 3 of this study are dedicated to the calculations necessary to arrive
at the four-dimensional Lagrangian density described above, after fibre-integration of the
higher-dimensional scalar RP - 2P . Section 4 starts from this Lagrangian on M4 and
calculates the classical masses of the associated Higgs-like and gauge-bosons as a functions
of the "vacuum value" of |0|2. Section 5 describes a more precise version of the model,
where the deformation g of the internal metric depends on additional parameters that
essentially correspond to the three gauge coupling constants of the Standard Model. In
addition, it discusses some of the important questions that are not sufficiently clarified or
even addressed here, such as the mass in this model of the four additional gauge bosons
present in the full SU(3) � SU(3) gauge theory, and the stability of vacuum configurations
of the form gP = gM � g under the full higher-dimensional Einstein equations of motion.
The discussion in this study also does not encompass the fundamental quantum aspects
of the Standard Model.

                              6
2 A left-invariant metric on SU(3)

Decomposition of su(3)

Consider the eight-dimensional Lie group K = SU(3) and the group homomorphism  :

U(2)  K defined by

                        (a) =  (det a)-1          .              (2.1)

                                               a

This map induces an inclusion of Lie algebras  : u(2)  su(3) that is denoted by the

same symbol:

                    (v) = - Tr(v)              v  .              (2.2)

Any matrix v in su(3) can be uniquely written as in (1.1), where v is a matrix in u(2)
and v is a vertical vector with two complex components. This defines a decomposition
of su(3) and an isomorphism of real vector spaces

                         : u(2)  C2 - su(3) ,                    (2.3)

which extends (2.2) and is still denoted by the same symbol. This decomposition of su(3)
is clearly orthogonal with respect to the usual Ad-invariant inner product on the space:

0(u, v) := Tr(u v) = Tr(u) Tr(v) + Tr[ (u) v ] + 2 Re (u)v .     (2.4)

When acting on vectors in the summand subspaces, the Lie bracket of su(3) satisfies the
simple relations

                    [ u(2), u(2) ] = su(2)  u(2)                 (2.5)
                       [ C2, C2 ] = u(2)

                     [ u(2), C2 ] = C2 ,

where we have denoted (u(2)) and (C2) simply by u(2) and C2, as will be often done
ahead. The adjoint action of any group element a  U(2) on the algebra su(3) can then

be written as                                        

                          - Tr(v) -[ (det a) a v ]

               Ad(a)(v) =                                     .  (2.6)
                                  (det a) a v  Ada(v)

Observe that the action of U(2) on the vector v in C2 coincides with the action of the same
group on the Higgs field  in the Standard Model, having the hypercharge necessary to

absorb the fermionic hypercharges in the Yukawa coupling terms (see [Ham], for instance).

                               7
    The decomposition u(2)  C2 of the matrix space su(3) can also be thought of as an
eigenspace decomposition with respect to the involution

                           v - Ad v =  v                         (2.7)

defined by the diagonal matrix  := diag(1, -1, -1) in SU(3). The involution Ad has
eigenvalue +1 on the subspace (u(2)) and eigenvalue -1 on the subspace (C2) of su(3).

General properties of left-invariant metrics

In the next few paragraphs we introduce notation and mostly describe standard properties
of left-invariant metrics on a Lie group. See for instance [Mil, BD]. As a vector space, the
Lie algebra of a group is the tangent space to the group at the identity element. A vector
v in the Lie algebra k can be extended to a vector field on the group K in two canonical
ways, as a left-invariant vector field vL or as a right-invariant field vR. They satisfy

      (Lh)(vL) = vL              (Rh)(vR) = vR                   (2.8)

for all group elements h  K, where Lh(h) = h h and Rh(h) = h h denote the left

and right-multiplication automorphisms on the group. The one-parameter flows on K

associated to these vector fields can be written in terms of the exponential map exp : k 

K as

      tvL(h) = h exp(t v)        tvR(h) = exp(t v) h .           (2.9)

The explicit expressions for the flows can be used to show that the Lie brackets of invariant
vector fields are also invariant on K and satisfy

      [uL, vL] = [u, v]Lk  [uR, vR] = -[u, v]Rk  [uL, vR] = 0 ,  (2.10)

where the bracket [ . , . ]k in the Lie algebra is just the commutator of matrices in the
case of matrix Lie groups. Just as with vectors, any tensor in the Lie algebra k can be
extended to a left or right-invariant tensor field on k. For example, given an inner product
g on k, it can be extended to a left-invariant metric on K by decreeing that the product
of left-invariant vector fields should have the same value everywhere on K and coincide
with g at the identity element of the group, thus g(uL, vL) = g(u, v). In the opposite
direction, every left-invariant metric on K is fully determined by its restriction to the Lie
algebra. When a left-invariant metric is applied to right-invariant vector fields the result
is a function on K that is not constant in general, but still simple enough:

g(uL, vR) |h = g(u, Adh-1 v)  g(uR, vR) |h = g(Adh-1 u, Adh-1 v) (2.11)

                              8
for all elements h  K and all vectors u, v in the Lie algebra. The preceding observations
are enough to recognize that right-invariant fields are always Killing vector fields for left-
invariant metrics on K, since

     (LwRg)(uL, vL) = LwR g(uL, vL) - g([wR, uL], vL) - g(uL, [wR, vL]) = 0 .     (2.12)
The same is not true for general left-invariant vector fields, since

    (LwLg)(uL, vL) = LwL g(uL, vL) - g([wL, uL], vL) - g(uL, [wL, vL])            (2.13)
                        = -g([w, u], v) - g(u, [w, v])

entails that the Lie derivative LwLg may be a non-zero left-invariant tensor on K. In the
special case when g is an Ad-invariant inner-product on k, then g(uR, vR) is also a constant
function on K and the metric g is both left and right-invariant. In this case left-invariant
vector fields are Killing as well. These are called bi-invariant metrics on the group and,
when K = SU(3), they coincide with minus the Killing form, up to a constant factor.

    If a left-invariant vector field vL is indeed Killing, then the usual Killing condition in
terms of the Levi-Civita connection implies that, for any other invariant field uL,

            g(vLvL, uL)  =  - g(uLvL, vL)      =     1     g(vL, vL)  = 0.        (2.14)
                                                  - 2 LuL

Thus, we must have that vLvL vanishes as a vector field on K. In particular, the flow
lines t  h exp(tv) generated by the field vL are affinely parameterized geodesics on K.

    The Riemannian volume form volg of a left-invariant metric g is always a left-invariant
differential form on the group. In the case of connected, unimodular Lie groups, such as
our K = SU(3), it is also a right-invariant form, even though the metric itself may not be
right-invariant. Thus, we always have here

                         (Lh) volg = (Rh) volg = volg ,                           (2.15)

and the bi-invariant volume form of g coincides, up to normalization, with the Haar
measure on K. Standard results on invariant integration on Lie groups [BD] then say
that, for any smooth function f (h) on K and any fixed element h in the group,

    f (h) volg =         f (h h) volg =         f (h h) volg =        f (h-1) volg . (2.16)

hK                hK                        hK                  hK

So the variable of integration can be changed by left-multiplication, right-multiplication

or inversion without changing the result. This invariance extends to other automorphism

of the Lie group, such as matrix transposition or matrix conjugation in the case of our

K = SU(3):

    f (h) volg =            f (hT ) volg =        f (h) volg =      f (h) volg .  (2.17)

hK                hK                        hK                  hK

                                            9
These invariance properties of integrals can be used to show, for instance, that for any
vector v in the Lie algebra of a simple Lie group we have

                                   Adh(v) volg = 0 .                               (2.18)

                              hK

This is true because the result of the integral is an Ad-invariant vector in the Lie algebra,

        Adh(v) volg =             Adhh(v) volg = Adh             Adh(v) volg ,

    hK                        hK                       hK

and hence belongs to the centre of the algebra, which only contains the zero element in the
case of simple groups. In particular, it follows that left and right-invariant vector fields
look orthogonal to each other after integration over K, since (2.11) and (2.18) imply that

                                   g(uL, vR) volg = 0                              (2.19)

                              hK

for all vectors u and v in k and for all left-invariant metrics. The integral over K of inner-
products of the form g(uL, vL) is also easy to compute, since these are constant functions
on K, by definition of left-invariant metric. So

                           g(uL, vL) volg = g(u, v) Vol(K, g) .                    (2.20)

                      hK

The integral over K of the product g(uR, vR) is not immediate in general, although it does
follow from the second equality in (2.11) that it is Ad-invariant and hence proportional
to the Cartan-Killing product on the simple algebra k. This happens because the second
integral in

    g(uR, vR) volg =       g(Adh-1 u, Adh-1 v) volg  Tr(adu adv) Vol(K, g) (2.21)

hK                    hK

is explicitly averaging the pull-back metric Adh-1 g over K, and hence is invariant under
a change of variable h  hh for any fixed group element h  K.

    Finally, the Ricci curvature of a left-invariant metric is also a left-invariant tensor on
K. This implies that the scalar curvature is constant on the group. Its value can be
expressed in terms of a g-orthonormal basis {uj} of the Lie algebra k through the formula

        Rg = -             1          1                                            (2.22)
                           4 g ([ui, uj], [ui, uj]) + 2 g([ ui, [ui, uj] ], uj) .
                      i,j

This expression is valid for unimodular Lie groups and is a special case of a well-known
formula for the scalar curvature of homogeneous spaces (e.g. see chapter 7 of [Bes]).

                                  10
A family of metrics on SU(3)

Start by considering the general bi-invariant metric on K = SU(3), determined by its
restriction to su(3) and unique up to a positive real constant :

(u, v) :=  0(u, v) =  Tr(u v) .                                  (2.23)

We want to deform this metric and break its bi-invariance using a parameter   C2. It
was noted in (2.3) that there exists an isomorphism of vector spaces  : u(2)  C2  su(3)
that takes any element   C2 to the matrix

                 -                 su(3) .                       (2.24)
() =


We use the parameter (), together with decomposition (1.1), to define a new inner-
product g on su(3) through the general formula

g(u, v) := (u, v) +  ( [u, v] + [v, u],  )                       (2.25)

= (u, v) +  ( [Ad u, v],  ) .

Here we have simplified the notation by omitting the isomorphism  to write , v and v
instead of the respective su(3) matrices (), (v) and (v). We will do this often below,
writing formulae such as v = v + v and regarding the components as elements of su(3).

    A first observation is that the deformed product g coincides with  when restricted to
the subspace u(2) of su(3), since both u and v vanish in this case. For similar reasons,
the two products coincide when restricted to the subspace C2. It is only in products
mixing both subspaces that g differs from . It is clear that the inner-product g can
be equally characterized by the three identities (1.2), which show, in passing, that the
two subspaces of su(3) are no longer orthogonal. Using the Ad-invariance of , it can be
readily verified that the orthogonal complement to u(2) in (su(3), g) is the subspace

u(2) = v + [, v] : v  C2 ,                                       (2.26)

while the orthogonal complement to C2 is the subspace            (2.27)
                                 (C2) = {v + [v, ] : v  u(2)} .

The Ad-invariant product  is positive-definite, so the new product g will maintain that
property if the parameter   C2 is sufficiently small. For larger  it may become an

indefinite product. It can be shown that g is positive-definite if and only if the vector
 = [1 2]T in C2 satisfies

|  |C2 2  =  |1|2 + |2|2          <  1
                                       .

                                     4

                              11
We will always assume that the parameter is in this range.

    By construction, the new product g is not Ad-invariant in su(3). However, its trans-
formation is simple enough when the adjoint action is restricted to elements in the sub-
group (U(2)) of SU(3), which always preserve the decomposition u(2)  C2 of su(3). If
we take any element a  U(2), it follows from (1.2) and the Ad-invariance of  that

(Ad(a)-1) g (u, v) = ( [Ad(a)-1 u, Ad(a)-1 v], ) = ( [u, v], Ad(a) ) .

Combining with expression (2.6) for Ad(a), we conclude that g transforms as  (2.28)
                                        (Ad(a)-1 ) g = g(det a)a 

for any a  U(2). In other words, when the subgroup U(2) of SU(3) acts on the product
g through the co-adjoint action, the parameter  simply rotates in C2 in a representation
analogous to the Higgs field one.

In the section on general left-invariant metrics, we saw that inner-products of the form

g(uR, vR) have an integral over the group K that is proportional to the Ad-invariant prod-

uct of the vectors u and v in su(3). We will now calculate the constant of proportionality

for the case g = g. It follows from (2.11), the definition of g and the Ad-invariance of
 that

       g(uR, vR) |h = (u, v) +  [Adh-1 u, Adh-1 v],  ,                       (2.29)

for any h  SU(3). Since the volume form volg is bi-invariant, the integral of the second
term must be invariant under the change of variable h  h, where  = diag(1, -1, -1).
Thus,

     [Adh-1 u, Adh-1 v],  volg =           [Ad(h)-1 u, Ad(h)-1 v],  volg

hK                                    hK

          =                                [Adh-1 u, Adh-1 v], Ad  volg

                                      hK

          =-                               [Adh-1 u, Adh-1 v],  volg .

                                      hK

This shows that the integral of the second term is zero, and so

       g(uR, vR) volg = (u, v) volg = (u, v) Vol(K, g) .                     (2.30)

    K  K

This means that the inner-product of right-invariant vector fields, after integration over
K, is completely blind to the deformation of the metric caused by the parameter . The
integrals over K of inner-products of the form g(uL, vR) and g(uL, vL) have already been
calculated in (2.19) and (2.20), respectively.

                                  12
Killing vector fields of g

The inner-product g on the Lie algebra su(3) can be extended to a left-invariant metric
on the group SU(3), as described before. The right-invariant vector fields uR will then be
Killing fields of g for every vector u  su(3). The same is not true for the left-invariant
fields uL when  = 0, since expression (2.13) says that the Lie derivative of the metric is
given by

(LuL g)(vL, vL) = 2 g( [v, u], v )                              (2.31)

                  = 2  [v, v], [u, ] + 2  [[v, u], v] + [[u, v], v],  .

The second equality is obtained after inserting the definition of g and using both the
Ad-invariance of  and the Jacobi identity for the Lie bracket on su(3). The left-invariant
vector field uL will be Killing precisely if the right-hand side of (2.31) vanishes for all
vectors v in su(3). A closer investigation of this condition (see appendix A.2) shows that
it can be fulfilled only if u = 0. This means that only vectors in the subspace (u(2))
of su(3) can originate left-invariant Killing fields. But for such a vector u the Killing
condition reduces to

                         [v, v], [u, ] = 0 for all vectors v  su(3) ,

and this can be satisfied only if the bracket [u, ] vanishes in su(3). Finally, the results of

appendix A.1 show that any such u must in fact be proportional to the 3�3 block-diagonal

matrix

                  i -1
                   :=                                        ,  (2.32)
                              3     2I2 - 3 ||-2  

where I2 denotes the 2 � 2 identity matrix and ||2 denotes the canonical norm in C2.

The conclusion is that there is precisely one left-invariant Killing vector field for the

Riemannian metric g, up to normalization, whenever  = 0. This field is the left-invariant
extension of the vector  that sits inside the subalgebra (u(2)) of su(3). Adding to it
the space of all right-invariant fields uR on SU(3), which are always Killing and satisfy
[L, uR] = 0, we conclude that the algebra of Killing vector fields of g can be identified
with a subalgebra u(1)su(3) of the full space su(3)su(3) of translation-invariant vector

fields on SU(3).

Orthonormal basis and volume form of g

The aim of this section is to write down an explicit g-orthonormal basis of su(3) in terms
of a -orthonormal basis of the same space. This will allow us to express the volume form

                                                       13
volg in terms of the volume form vol and, at the end, calculate the Riemannian volume
of the internal space (SU(3), g).

Let {u0, . . . , u3, w1, . . . , w4} be a -orthonormal basis of su(3) = (u(1)  su(2)  C2)

such that the vectors {wj} span the subspace (C2) of su(3); the vectors {u1, u2, u3} span

the subspace (su(2)); and u0 is the vector

                            1                     1
                  u0 =  diag(-2i, i, i) =  (iI2)                                         (2.33)
                            6                     6

spanning (u(1)). The positive factor  comes from definition (2.23) of  and ensures

that u0 has -norm equal to 1. Since the restriction of g to the subspace (C2) coincides
with the restriction of , the four vectors {wj} are g-orthonormal and can be included
in the desired basis. The remaining vectors {uj}, however, are not g-orthogonal to the
{wj}, so have to be modified in order to complete the g-orthonormal basis. With this
purpose, start by recalling from (2.27) that the vectors in su(3) that are g-orthogonal to
the subspace (C2) are of the form u + [u, ], with u in (u(2)). Moreover, one can check

that the metric g satisfies a nice identity when acting on vectors of this form, provided
u is in the smaller subspace (su(2)), namely

                  g u + [u, ], v + [v, ] = (1 - ||2) (u, v)                              (2.34)

for all vectors u, v  (su(2)), where ||2 denotes the canonical C2-norm of . Thus, if
u is -orthogonal to v, the shifted vectors u + [u, ] and v + [v, ] will automatically

be g-orthogonal to each other, besides being g-orthogonal to the {wj}. It follows that

the vectors                1
                         1 - ||2 (uj + [uj, ])
                  vj :=                           for j = 1, 2, 3,                       (2.35)

can be added to the wj to form a g-orthonormal set of vectors {v1, v2, v3, w1, . . . , w4} in
su(3). At this point we only need one more vector to complete the desired basis, and

it should have a non-zero component along the subspace (u(1)) of su(3). Defining the

vector in (u(2))                                   
                                      (iI2) - 2 3 ||2 
                                   1                               ,
                         u := 3

we will choose for v0 the normalized version of the combination

                            u + [u, ] = u + (i) ,

as this automatically ensures orthogonality to the subspace (C2), and hence to the {wj}.

An explicit calculation shows that

v0 :=                         3                                                          (2.36)
                  6(1 - ||2)(1 - 4||2) u + [u, ]

             1 - ||2                        
             1 - 4||2 u0 +                       3
=                                                                  2i   -  i||2I2  +  i

                                    2(1 - ||2)(1 - 4||2)

                                            14
does the job of completing the g-orthonormal basis {v0, . . . , v3, w1, . . . , w4} of su(3). The
explicit form of this basis will be used in many calculations ahead.

    To compute the volume form volg, consider the exterior product of vectors in su(3)
and start by observing that

v1  v2  v3  w1  � � �  w4 = (1 - ||2)-3/2 u1  u2  u3  w1  � � �  w4 .

This follows from definition (2.35) of vj after noticing that the vectors [uj, ] are in the
four-dimensional subspace (C2) of su(3), and therefore have zero exterior product with
the top product w1  � � �  w4 of that subspace. For the same reason, the second term
in the bottom line of (2.36) is in the subspace (su(2)  C2) and therefore has vanishing
exterior product with u1  u2  u3  w1  � � �  w4. Taking only the first term of v0 into
account then yields

v0  � � �  v3  w1  � � �  w4 = (1 - ||2)-1(1 - 4||2)-1/2 u0  � � �  u3  w1  � � �  w4 .

Since {v0, . . . , v3, w1, . . . , w4} is a g-orthonormal basis of su(3), the top exterior product
of its vectors is dual to the volume form volg. For the same reason, the product u0 
� � �  u3  w1  � � �  w4 is dual to the volume form vol. This implies that the two volume
forms on su(3) are related simply by

volg = (1 - ||2) 1 - 4||2 vol = 4 (1 - ||2) 1 - 4||2 vol0 ,            (2.37)

where in the last equality we opted to flesh out the scale factor  appearing in definition
(2.23) of the Ad-invariant product .

    The relations between the volume forms written above allow us to express the Rie-
mannian volume of the left-invariant metric g on K = SU(3) in terms of the volume of
the bi-invariant metrics ,

                 Vol K, g := volg = (1 - ||2) 1 - 4||2 Vol K,  .       (2.38)

                                                            K

But the volume of SU(3) equipped with the Cartan-Killing metric

- Tr(adu adv) = 6 Tr(uv) = 6 -1 (u, v)


is known to be equal to 3 (12)45 (see [AY], for instance). Therefore, after performing

the necessary rescaling to , we finally get that

                                                                       (2.39)
Vol K, g = 3 (2 )4 5 (1 - ||2) 1 - 4||2 .

Thus, the volume of the internal manifold K is controlled both by the overall scaling factor
 and by the norm ||2 of the C2-parameter in the metric g. The volume is maximal

15
for  = 0, i.e. for the bi-invariant metric on K, and then tends to zero as the parameter
||2 approaches the critical value 1/4 at which the metric g stops being positive-definite.
In a model with dynamical , one would certainly wish to have a potential V (||2) that
explodes when ||2 approaches 1/4, and therefore prevents the internal metric from ever
becoming non-definite. The presence of such a potential is a nice feature of the Lagrangian
densities studied ahead.

Scalar curvature of g

The aim of this section is to present a formula for the scalar curvature Rg of the metric
g on the group K = SU(3). The scalar curvature of K is one of the components of the
scalar curvature of the higher-dimensional spacetime P = M4 � K, so will appear in the
higher-dimensional Lagrangian density. Our calculation of Rg uses the standard formula
(2.22), from [Bes], applied to the particular g-orthonormal basis {v0, . . . , v3, w1, . . . , w4}
of su(3) that was constructed in the previous section. It is a rather long calculation, so in
this section we will write down only the final result and its main intermediate components,
which would deserve to be checked independently.

    We start by stating the final result of the calculation. It says that the scalar curvature
of the left-invariant metric g on SU(3) is given by

Rg =                   3 ( 4 - 25 ||2 + 33 ||4 - 8 ||6 )  ,  (2.40)

                        (1 - ||2)2 (1 - 4||2)

where ||2 is the canonical norm in C2 of the parameter  and  is the positive scaling

factor appearing in definitions (2.23) and (2.25) of the metrics  and g. Observe that

Rg only depends on the norm of the vector , not on its orientation, and when  = 0 we
recover the positive scalar curvature R = 12/ of the bi-invariant metric  on SU(3). In
the limit where ||2 approaches the critical value 1/4, at which g stops being positive-

definite and the volume of SU(3) collapses to zero, the scalar curvature Rg explodes
to infinity. The numerator in (2.40) takes a negative value when ||2 = 1/4, so Rg
tends to minus infinity in this limit. The change of sign of Rg occurs at ||2 = 0.221,
approximately. A visual profile of the scalar curvature as || ranges from 0 to 1/2, with

the choice  = 1, is given in figure 1.

                                        16
     Figure 1: Scalar curvature Rg as a function of || at  = 1. 1

    We will now detail some of intermediate results that lead to (2.40). The general
formula (2.22) for the scalar curvature of left-invariant metrics uses an orthonormal basis
of su(3), which we denote here by {ei}, and presents it as a sum of two terms. In the case
of the metric g, the separate value of these two components is calculated to be

  1  8                                   1   8                    8
-
            g([ ei, [ei, ej] ], ej)  =  -       Tr(adei adei) = 3 Tr(ei ei)
  2                                       2
     i,j=1                                   i                    j=1

                                         12 (2 - 9||2 + 9||4 - 2||6)         (2.41)
                                     =  (1 - ||2)2 (1 - 4||2) ,

for the term proportional to the contraction of the Cartan-Killling form on su(3), while
the term that sums the norms of all the commutators is given by

        18                                      3 ( 4 - 11||2 + 3||4 )
     -             g [ei, ej], [ei, ej]  =-                             .    (2.42)
       4                                         (1 - ||2)2 (1 - 4||2)
            i,j=1

The calculation of this second sum is more laborious than that of the first term, so we will
also write down five partial results that originate it. Choosing as g-orthonormal basis
the set of vectors {v0, . . . , v3, w1, . . . , w4} described in the previous section, the sum of the

1Figure generated with the free online version of Wolfram Alpha.

                                                         17
norms of all commutators is obtained from the following partial sums:

 4                                    6
                                  =;
         g [wi, wj], [wi, wj]

i=1 j>i
                                  =   3 (2 + ||4)   ;
     3
                                       (1 - ||2)2
            g [vk, vl], [vk, vl]
                                  =   3 ||4 (9 - 8||2)                 ;
   k=1 l>k
           3                           (1 - ||2)2 (1 - 4||2)

           g [v0, vk], [v0, vk]             3 (2 + 5||2)
                                  =  (1 - ||2)(1 - 4||2) ;
         k=1
          4                       =   3 (2 + 5||2)  .

          g [v0, wj], [v0, wj]         (1 - ||2)

        j=1

  34

          g [vk, wj], [vk, wj]

k=1 j=1

These are the intermediate components that give rise to the formula for the scalar curva-
ture Rg.

                                  18
3 Lagrangians and fibre-integrals on M4 � SU(3)

Submersive metrics on M4 � SU(3) and their scalar curvature

The first objective of this section is to define the metric gP on the higher-dimensional
P = M4 � K that will be used to write Lagrangian densities on that spacetime. As usual
in Kaluza-Klein theories, in order to account for the gauge fields on Minkowski space, one
should go beyond the product "vacuum" metric (gM , gK) and consider metrics on P with
non-diagonal terms. We will also spend a few paragraphs recalling the formula for the
scalar curvature of a Riemannian submersions and establishing the associated notation.

Let  denote the natural projection  : P  M . The tangent space to P at any given

point p = (x, h) has a distinguished subspace Vp defined by the kernel of the derivative
map  : TpP  TxM . This is called the vertical subspace of the projection . When P is
a simple product of manifolds, it can be identified with the tangent space to the internal

manifold ThK. If we are also given a metric gP on P , the gP -orthogonal complement

to Vp is called the horizontal subspace Hp of the tangent space TpP . Then we have a

decomposition

               TpP = Hp  Vp      X = XH + XV ,                         (3.1)

and every tangent vector E  TpP can be written as a sum of the respective components.
By definition of submersion, the derivative  must induce an isomorphism of vector
spaces Hp  TxM . If this isomorphism is an isometry at every point p  P , that is, if the
product (gP )p(XH, XH) is equal to (gM )x(X, X) for every p  P and every vector
X  TpP , then the projection  is called a Riemannian submersion. For this kind of
submersions, the metric gP on the higher-dimensional space is completely determined by
the metrics gK and gM , together with the rule (3.1) to decompose tangents vectors into
their horizontal and vertical components. In fact, we can write

               gP (X, X) |(x,h) = gM ( X,  X) |x + gK (XV , XV ) |h .  (3.2)

The rule (3.1) to decompose tangent vectors at every point, i.e. the definition of the
horizontal distribution H  T P , is called a Ehresmann connection on the submersion. It
is equivalent to the more pervasive notion of K-connections on a K-principal bundle in
the special case where the distribution H is invariant under right-multiplication on K.

    In this study we will consider metrics on P determined by Ehresmann connections
that can be written down using two one-forms AL and AR on M4 with values in the Lie
algebra su(3). These one-forms can be coupled to the invariant vector fields eL and eR on

                             19
the group in order define the horizontal and vertical components of any vector X  TpP :

XV :=     ARj ( X) eRj -     ALj ( X) eLj       (3.3)

       j                  j

XH := X +     AjL( X) eLj -     ARj ( X) eRj ,

           j                 j

where {ej} denotes any basis of su(3). Since X is a vector tangent to M4, it can
be contracted with the one-forms AjL and AjR to define the coefficients of the vertical
vector fields ejL and ejR evaluated at p. The minus signs are inserted to later obtain the
usual formulae for the curvature. The one-forms AL and AR do not define a traditional
SU(3)-connection on P , although they could be used to define a principal connection on
a SU(3)�SU(3)-bundle over M4. In practice, we will think of them as determining the
horizontal distribution and metric gP on P , and never work with that second bundle.

    A second point of order seems appropriate now. The main aim of this investiga-
tion is trying to reproduce the bosonic terms of the Standard Model Lagrangian using a
higher-dimensional, Kaluza-Klein-like route. Since the Lie algebra associated to the clas-
sic Standard Model gauge fields is u(2)  su(3), not the more symmetrical su(3)  su(3),
in most of this study we will assume that the one-form AL in the definition of gP has
values in the subalgebra u(2) of su(3), and then calculate to see if this produces densities
in M4 similar to the terms present in the classical electroweak Lagrangian. Nonetheless,
this constraint on AL, and hence on the metric gP , is not natural from a geometrical point
of view and calls for further justification . In section 5.3 we discuss the natural possibility
of having a form AL with values in the full su(3)  u(2)  C2, but with very massive and
still unobserved bosons associated to the components in the subspace C2.

    Returning to the description of submersive metrics, it follows from groundwork in
[O'Ne] that the scalar curvature of the higher-dimensional metric gP , defined by (3.2),
can be written as a sum of components

RP = RM + RK - |F |2 - |S|2 - |N |2 - 2 N       (3.4)

 where RM and RK denote the scalar curvatures of gM and gK, respectively, and F , S and
 N are tensors on P that we now describe (see chapter 9 of [Bes]2).

     Let  denote the Levi-Civita connection of the metric gP ; let U and V denote vertical
 vector fields on P ; let X and Y denote horizontal vector fields on P . Then S is the linear
 map V � V  H that extracts the horizontal component of the covariant derivative of

2The notation here differs from that in [O'Ne, Bes] in the following points: the tensor called A in [O'Ne, Bes]
 is called here F, to avoid confusion with the gauge fields; the tensor called T in [O'Ne, Bes] is called here
 S, to avoid confusion with the energy-momentum tensor.

              20
vertical fields,

                            SU V := (U V )H .                    (3.5)

Since U and V are tangent vectors to the fibre K, the map S can be identified with the
second fundamental form of the fibres immersed in P . When S vanishes, all the fibres

are geodesic submanifolds of P and are isometric to each other [Her, Bes]. On its turn,
F is the linear map H � H  V that extracts the vertical component of the covariant
derivative of horizontal fields,

                  FX Y      := (X Y )V  =  1 [X, Y ]V .          (3.6)
                                           2

where the second equality is a standard result for torsionless connections [O'Ne, Bes].

When F vanishes, all the Lie brackets of horizontal fields vanish, and hence H is an

integrable distribution. It is clear from the respective definitions that both S and F are
C-linear when their arguments are multiplied by smooth functions on P . The vector

field N is perpendicular to the fibres and is defined simply by

                            N :=        SVj Vj ,                 (3.7)

                                  j

where {Vj} is a gK-orthonormal basis for the vertical space. So N can be identified with
the mean curvature vector of the fibres of P . The norms of all these objects are defined
by

                  |F |2 :=       gK FX� X , FX� X                (3.8)

                            �,

                  |S|2 :=        gM  SVi Vj ,  SVi Vj

                            i,j

                  |N |2 := gP (N, N ) = gM (N, N ) .

where {X�} stands for a gM -orthonormal basis of the horizontal space, isomorphic to the
tangent space T M . Finally, the scalar N is just the negative trace

                  N = - gP X�N, X� .                             (3.9)

                                       �

The purpose of the next few sections will be to calculate explicitly all the terms of RP ,
integrate them over the fibre K and analyze the resulting terms in the four-dimensional

Lagrangian.

Yang-Mills terms on M4

The content of the standard Kaluza-Klein calculation is that the Yang-Mills terms for the
gauge field strength on Minkowski space can be obtained from the term |F|2 contained in

                                                       21
the scalar curvature of the higher-dimensional metric. In this section we will verify how
this works in the case of the metric gP on P = M � K, as determined by the metrics gM
and gK = g on the factors and by the horizontal distribution defined in (3.3). Everything
develops as expected, with a bonus at the end saying that, after fibre-integration over K,
the Yang-Mills terms for the subalgebra u(2)  su(3) of gauge fields are independent of
the orientation of the parameter  in the metric g, and thus are broadly similar to the
Yang-Mills terms that would be obtained from the bi-invariant metric  on SU(3). This
is a nice feature to have, since the Yang-Mills terms of the Standard Model Lagrangian
do not involve the orientation of the Higgs field.

    Let X and Y be tangent vectors to M4, which can also be regarded as tangent vectors
to P satisfying X = X. We will simplify the notation of (3.3) and write the horizontal
component of X as

XH := X + AjL(X) ejL - ARj (X) eRj = X + A(X) ,           (3.10)

where A can be regarded as a one-form on M4 with values in the invariant vertical fields
of P . Then the tensor F of (3.6) satisfies

2 FXHY H = [XH, Y H]V
              = [X, Y ]H - A([X, Y ]) + [A(X), Y ] + [X, A(Y )] + [A(X), A(Y )] V

= (dM A)(X, Y ) + [A(X), A(Y )] V

= FAj L(X, Y ) eLj - FAkR(X, Y ) eRk ,                    (3.11)

where in the last equality we have used the Einstein summation convention and defined
the coefficients

FAj R(X, Y ) := dAjR(X, Y ) + ARi (X) AkR(Y ) [ei, ek]j   (3.12)
FAkL(X, Y ) := dAkL(X, Y ) + AiL(X) ALj (Y ) [ei, ej]k .

The derivation of the third equality in (3.11) uses the standard formula for the exterior
derivative of a one-form :

d(u, v) = Lu[ (v) ] - Lv[ (u) ] - ([u, v]) ,              (3.13)

while the derivation of the fourth equality uses the properties (2.10) of the brackets of

invariant vector fields on K. For example, the decomposition of F into separate com-
ponents FAj L and FAkR is due to the commutation [eLj , eRk ] = 0 of left and right-invariant
vector fields.

22
    To explicitly write down the norm |F|2, let {X�} denote a basis for the tangent space
T M . It follows from (3.11) combined with (3.8) that

|F |2  =  1  gM�  gM  g  (FAj L )� ejL - (FAkR )� eRk , (FAj L ) eLj - (FAkR ) eRk  .  (3.14)
          4

Even though the metric gM and the curvature coefficients FAj only depend on the coordi-
nate x  M , the norm of F is not a constant function along K, since the inner-products
g(ejL, eRk ) and g(ejR, eRk ) do depend on the coordinate h  K.

    The expression for |F |2 is significantly simplified if we integrate over (K, volg), as we
have already seen that the integrals of g(eLj , ekR) are equal to zero, while the integrals
of g(eLj , ekL) and g(eRj , ekR) are proportional to the volume of K. In fact, combining
expression (3.14) with the integrals of products of invariant vector fields calculated in

(2.19), (2.20) and (2.30), one obtains

   |F |2 volg     =   1  gM�  gM  g(ej, ek) (FAj L )� (FAkL )
                      4                   + (ej, ek) (FAj R )� (FAkR )
K

                                                                        Vol(K, g) . (3.15)

Observe how the coefficients in front of the curvature components FAR depend solely on
the bi-invariant metric , and not on the whole metric g as one could presume from
(3.14). In the case where the one-forms AL have values in the electroweak subalgebra u(2)
of su(3), the coefficient g(ej, ek) in front of the curvature components FAL will also be
equal to (ej, ek), since the metric g coincides with  when restricted to u(2). So for the
restricted gauge field algebra u(2)  su(3), the expression for the norm of F is

   |F |2 volg     =   1  gM�  gM     4
                      4
K                                      (ej, ek) (FAj L )� (FAkL )

                                  j,k=1

                                     8

                                  +         (ej, ek) (FAj R )� (FAkR )  Vol(K, g) . (3.16)

                                     j,k=1

This scalar density on M4 broadly coincides with the Yang-Mills terms of the Standard
Model Lagrangian. The fact that the coefficients in front of the curvature terms appear
with the Ad-invariant product , and not with its deformation g, seems to be a relevant
and positive point, since the coupling constants of the strong and weak gauge fields
in the Standard Model do not depend on the orientation of the Higgs field inside C2.
However, integral (3.16) does depend on the norm ||2, for instance through the overall
factor Vol(K, g), which will also appear in the integrals of the remaining terms of the
higher-dimensional scalar curvature RP .

                                            23
Fibres' second fundamental form and Higgs covariant derivatives

Let U and V be vertical vector fields on the submersion  : P  M and let  be a metric
connection on the tangent bundle T P . In a submersion, the Lie bracket of vertical fields
is always vertical [Bes], so for torsionless connections  it is clear that SU V is symmetric,

SU V = (U V )H = V U + [U, V ] + Tor(U, V ) H = SV U .                           (3.17)

Observe that it is not strictly necessary to start with a torsionless connection in order to
obtain a symmetric S. It is enough to demand that Tor(U, V ) be a vertical vector field
whenever U and V are vertical. This will be the case whenever Tor(U, V ) is proportional
to the bracket [U, V ], for instance. Be that as it may, we will still assume in the calculations
ahead that  is the Levi-Civita connection. Thus, using the definition of SU V and the fact
that  is a torsionless metric connection, one can write for every vector X  T M  T P :

gP SU V, X    = gP U V, XH = LU gP (V, XH) - gP V, U XH )
              = - gP V, XHU + [U, XH] .

But SU V is symmetric in U and V , so using again that  is a metric connection,

2 gP SU V, X  = gP SU V, X + gP SV U, X
              = - LXH gP (U, V ) - gP V, [U, XH] - gP U, [V, XH]
              = - (LXH gP ) U, V ,                                               (3.18)

where the last equality is a general identity of Lie derivatives. This expression provides
a concise relation between the tensor SU V and the horizontal Lie derivatives of the sub-
mersion metric gP . Now suppose that the vertical vector fields U and V are left-invariant
on K, and hence can be written as uL and vL, respectively. Since the metric on the fibres
is also left-invariant, the product gP (uL, vL) is constant along K, so

                               LXH gP (uL, vL) = LX gP (uL, vL) .

Combining the definition (3.3) of XH with the usual results (2.10) for the brackets of
invariant vector fields, we also obtain that

gP uL, [XH, vL] =     ALj (X) gP uL, [ej, v]L = gP uL, [AL(X), v]L .             (3.19)

                   j

The one-form AR does not appear in this expression because the brackets [eRj , vL] always
vanish on K. Thus, in the case of left-invariant vertical fields, expression (3.18) can be
rewritten as

2 gP ( SuLvL, X) = - LX gP (uL, vL) - gP vL, [ AL(X), u ]L - gP uL, [ AL(X), v ]L .

                      24
To progress any further we have to be more specific about the restriction to the fibres
of the submersion metric gP , which so far we have called gK and only assumed to be
left-invariant, and say how this restriction can vary when we move across different fibres
over M4.

    We will choose, of course, gK to be the metric g defined in (2.25) and studied in section
2. We will assume that the parameter   C2 of the metric can change when one moves
across the fibres of P , and so  becomes a dynamical variable in four-dimensions that we
will try to identify with the Higgs field. Furthermore, at this point we will also admit the
possibility that the parameter  affects the metric g not only through the second term
of (2.25), but also through the positive scale factor  of (2.23). More precisely, we admit
that  = (||2) may be a non-trivial function of the norm ||2. Such a dependence does
not change any of the calculations done so far in this study. Using the definition (2.25)
of the metric g it is then clear that, for any vector X tangent to M ,

LX g(uL, vL) =  [u, v] + [v, u], d(X) + (LX log ) g(u, v) .  (3.20)

Moreover, an algebraic calculation using the Ad-invariance of  and the Jacobi identity
for the Lie brackets says that, for any vector z in the subspace (u(2)) of su(3), we have

g v, [ z, u ]  + g u, [ z, v ]  =  [v, [z, u]] + [[z, u], v]
                                                      + [u, [z, v]] + [[z, v], u], 

                                =  [z, [v, u]] + [[v, u], z], 
                                =  [v, u] + [u, v], [z, ] .

In particular, when the one-form AL has values in the same subspace (u(2)), we can
substitute z = AL(X) to obtain

       g v, [ AL(X), u ] + g u, [ AL(X), v ] =  [v, u] + [u, v], [AL(X), ] .

Combining this expression with (3.20), we finally conclude that the choice of metric gK =
g in the internal space leads to the result

     2 gP ( SuLvL, X) = -  [u, v] + [v, u], dA(X) - (LX log ) g(u, v) , (3.21)

with the implicit definition of covariant derivative

               dA(X) := d(X) + [ AL(X),  ]  su(3) .          (3.22)

Here we should be more careful, perhaps, and explicitly insert back the vector space
isomorphism  : u(2)  C2  su(3) that identifies the parameter   C2 with a matrix in

                                25
su(3). If we do this, the covariant derivative dA(X) can be written more completely in
two different ways:

dA(X) := [d ()](X) + [ AL(X), () ]                      (3.23)
                                                        (3.24)
                                                     4

           =  d(X) + ALj (X) ej () ,

                                                   j=1

where  : u(2) � C2  C2 is the Lie algebra representation associated to the U(2)-
representation   (det a) a  on the space C2 coming from (2.6). The first line represents
the covariant derivative of the vector () in su(3), hence the bracket is the commutator
of matrices in su(3). The second line represents the -image of the covariant derivative of
the vector   C2 associated to the indicated U(2)-representation.

    It should be mentioned again that the last two expressions for the covariant derivative
dA are valid only for gauge fields (AL, AR) with values in the subalgebra u(2)su(3) of the
more symmetric su(3)  su(3). Moreover, as remarked after (2.6), the U(2)-representation
and the covariant derivative of  are consistent with those attributed to the Higgs field in
the Standard Model Lagrangian, having the hypercharge necessary to absorb the fermionic
hypercharges in the Yukawa coupling terms. The previous calculation, more specifically
the comment after (3.19), also provides a geometrical model to understand why the Higgs
field couples to the electroweak gauge fields AL but not to the strong force fields AR.

Norm of the second fundamental form

In this section we will calculate the norm |S|2 of the second fundamental form of the
fibres in the higher-dimensional spacetime P = M � K. The metric gP on P is the one
described in the last section. We will use (3.8) as definition of norm and result (3.21) as
a working formula for the tensor S. In particular, since the latter formula is valid only
for gauge fields with values in the Standard Model subalgebra u(2)  su(3) of the larger
su(3)  su(3), the same applies to the results obtained in this section. Our calculation of
|S|2 uses the g-orthonormal basis {v0, . . . , v3, w1, . . . , w4} of su(3) that was constructed in
section 2. Since it is a rather long calculation, here we will write down only the final result
and its main intermediate components, which would deserve to be checked independently.

    We start by stating the final result of the calculation. It says that the squared-norm
|S|2 is a constant function along the fibres of P that descends to the following function

26
on the base M4:

|S|2 =  3 (1 - 2||2)          |dA|2 + 3 ( 3 - 8||2 + 8||4 ) |d ||2 |2

        (1 - ||2) (1 - 4||2)  2 (1 - ||2)2 (1 - 4||2)2

                 +      gM� ( log ) � log 2 (1 - ||2) 1 - 4||2         , (3.25)

                    �,

where ||2 is the canonical C2-norm of the parameter of the metric g; the covariant
derivative dA is that of (3.24) and also has values in C2; the function (||2) is the scale

factor of g that, in the last section, we admitted as possibly non-constant and dependent
on ||2 only. Since it is constant on the fibres, the fibre-integral of |S|2 is just

                           |S|2 volg = |S|2 Vol(K, g) ,                (3.26)

                        K

and hence the terms induced in the four-dimensional Lagrangian can be read directly

from (3.25) and the volume formula (2.39).

    The first salient point coming from (3.25) is that this part of the Lagrangian density has
a rather elaborate dependence on ||2, even if we take (||2) to be a constant function.
Thus, the four-dimensional equation of motion of the parameter   C2 will be more
involved than that of the traditional Higgs field in the Standard Model.

    The second salient point is the emergence in the Lagrangian of a term proportional to
|dA|2, with a coefficient function that is always positive in the usual range of ||2 < 1/4.
In particular, if the "vacuum" value of the parameter  is non-zero, i.e. if the "vacuum"
metric of the internal space SU(3) is not bi-invariant, then we will get non-zero mass terms
for the gauge fields, just as in the usual Brout-Englert-Higgs mechanism of the Standard
Model ([Ham, Wei2] or original references [EBH]). Since the parameter  couples to the
one-form AL but not to the one-form AR, as mentioned in the last section, only the former
fields have mass terms. Here we are taking the one-form AL with values in the subalgebra
(u(2)) of su(3). However, we have already seen in (2.32) that there exists a matrix 
in this subalgebra that commutes with (), so the corresponding component of AL will
not couple to  in the covariant derivative (3.22) and will not acquire a mass term. It is
the candidate for the photon field. In short, if the "vacuum" metric of the internal space
is not bi-invariant, the component |S|2 of the higher-dimensional scalar curvature RP
will naturally produce all the terms in the four-dimensional Lagrangian necessary to the
emergence of the Brout-Englert-Higgs mechanism, at least from a qualitative perspective.
In sections 3.7 and 5 we will address the question of finding the "vacuum" metric of this
model.

    In the remainder of this section we will give more details about the calculation leading
to formula (3.25). Let {x�} be a coordinate system on M4. Since the projection  : H 

                                            27
T M is an isometry, it follows from (3.21) that

                   2 gP  SuL vL,         =  2 gM      SuL vL,   
                                  x�                           x�

                                         = - Hz�(u, v) - (� log ) g(u, v) ,              (3.27)

where we have simplified the notation and defined the auxiliary quantities

                            Hz(u, v) :=  [u, v] + [v, u], z

                                  z� := dA                                               (3.28)
                                                      x�

Combined with the definition of norm in (3.8), expression (3.27) leads to

           1   3            8
           4
|S|2 =             gM�         Hz�(ej, ek) Hz (ej, ek)

              �=0        j,k=1

                                      8

                   + 2 ( log ) Hz�(ek, ek) + (dim K)(� log ) ( log )                  , (3.29)

                                               k=1

where {ek} denotes a g-orthonormal basis of the Lie algebra su(3) and the dimension of
K is equal to 8, of course. Now let z  C2 represent any vector in the subspace (C2)
of su(3). A rather long algebraic calculation using definition (3.28) yields the following

general properties of the tensor Hz(u, v):

     8                                |z|2 (1 - 2||2)             z, 2 (3 - 8||2 + 8||4)
                               12                              24
           Hz(ej, ek)    2  =                             +
                                  (1 - ||2) (1 - 4||2)              (1 - ||2)2 (1 - 4||2)2
   j, k=1

     8                            z, 2 (1 - 2||2 + 4||4)
                               48
           Hz(ek, ek)    2  =
                                    (1 - ||2)2 (1 - 4||2)2
     k=1

           8                          z,  (2||2 - 1)

               Hz(ek, ek)   =  12                         .                              (3.30)
                                  (1 - ||2) (1 - 4||2)
          k=1

Here  � , �  denotes the canonical real product on C2 and | � | the corresponding norm.
Observe that when z  C2 is the derivative vector z� defined in (3.28), then the standard
properties of the covariant derivative (3.24), which comes from a unitary representation
in C2, imply that

                   z�,  =                           4              =  1  �||2  .         (3.31)
                                                                      2
                                  d� + (ALj )� ej (), 

                                                  j=1

It can then be easily checked that the last identity in (3.30) becomes simply

8                        6 ( �||2 ) (2||2 - 1)
                           (1 - ||2) (1 - 4||2)
     Hz�(ek, ek)   =                              =   � log    (1 - ||2)2 (1 - 4||2)  .  (3.32)

k=1

                                                  28
Substituting (3.32) and the sums (3.30) into (3.29), we get the final formula (3.25). Due
to length of the calculations involved in obtaining identities (3.30), we will also write
down the partial sums that originated them. Choosing as g-orthonormal basis the set of
vectors {v0, . . . , v3, w1, . . . , w4} described previously, the partial sums are

         3                             12 z, 2
                                       (1 - ||2)2
                  Hz(vk, vl)  2  =

         k, l=1

               3  Hz(v0, vk)  2  =        (1 - ||2)2  |z|2||2 - z, i2 + ||2z, 2 (2 - ||2)
                                       24                  (1 - ||2)2 (1 - 4||2)
         2

             k=1

                  Hz(v0, v0)  2  =             36 z, 2
                                       (1 - ||2)2 (1 - 4||2)2

      3  4                              6 |z|2
                                       1 - ||2
2                 Hz(vk, wj)  2  =

k=1 j=1

      4           Hz(v0, wj)  2  =       (1 - 2||2)2 |z|2 + 4 (1 - ||2) z, 2 + z, i2
                                       6
2
                                                            (1 - ||2) (1 - 4||2)
         j=1

            4                                                                         (3.33)

                Hz(wi, wj) 2 = 0 .

         i, j=1

Mean curvature of the fibres

Among the six components of the higher-dimensional scalar curvature RP , as decomposed
in formula (3.4), only the two terms involving the mean curvature vector of the fibres --
the vector field denoted by N in that formula -- have not yet been calculated here. That
is the purpose of the present section.

    Having in mind definition (3.7) of the horizontal field N , we start by taking the trace
of (3.19) and the formula below it. Let {ek} denote a gK-orthonormal basis of the Lie
algebra su(3), where gK is the left-invariant metric on the fibre that includes the point
p  P . Then the trace of (3.19) evaluated at p is identically zero,

   gP eLk , [XH, eLk ]        =        ALj (X) gP eLk , [ej, ek]L =       AjL(X) gK ek, [ej, ek]

k                                k,j                                 k,j

                              =        ALj (X) Tr(adej ) = 0 ,

                                    j

where the second equality used the left-invariance of gK, while the third equality used
that SU(3) is an unimodular group, which implies that the adv transformations in the Lie
algebra are all traceless. Therefore, combining the definition of N with the trace of the

                                                      29
formula below (3.19), we get that, for any vector X  T M  T P ,

2 gP ( N, X) =      2 gP ( SekL eLk , X) = -        LX gP (eLk , eLk )

                 k                            k

           = - LX             gK(ek, ek) .                              (3.34)

                          k

When reading this expression, it is important to keep in mind that the vertical metric gK
may vary across different fibres, while the basis {ek} was defined to be gK-orthonormal
only at the fibre that includes the point p  P . In particular, the functions gK(ek, ek)
have value 1 at p but need not be constant when moving across the fibres. The mean
curvature vector N is essentially the gradient on P of the sum of these functions.

    In the particular case of the vertical metric gK = g, one can write an explicit expres-
sion for N in terms of the derivatives of ||2. Taking {x�} to be a coordinate system on
M4, it follows from (3.27) and (3.32) that

                 =        gP  SekL ekL ,   
gM ( N,       )                           x�
         x�
                    k

                       1                         1
                 = - 2 (dim K) (� log ) - 2            Hz�(ek, ek)

                                                    k

                 = - � log 4 (1 - ||2) 1 - 4||2 .                       (3.35)

This means that  N is minus the gradient vector in M4 of the logarithmic function
appearing in (3.35). Observe that the argument of the logarithm is precisely the function
that appears in formula (2.37) for the volume form volg in the group K:

         f := 4 (1 - ||2)     1 - 4||2 = volg .                         (3.36)
                                               vol0

It can be regarded either as a function on the base M4 or as a function on P that is
constant along the fibres. Since the projection  : H  T M is an isometry, for any
vector E tangent to P we have

  gP (N, E) = gP (N, EH) = gM ( N,  E) = - LE ( log f ) = - LE (  log f ) ,
so we can write, equivalently,

                    N = - gradP ( log f)                                (3.37)
                  N = - gradM ( log f ) ,

in agreement with well-known properties of the mean curvature vector in Riemannian
fibrations. The norm of N is then equal to the norm on the base M4 of the exterior

                              30
derivative of the same logarithmic function,

                                |N |2 =     d(log f)   2     .                           (3.38)
                                                       gM

Now let {x�} stand for a coordinate system in M4 and let {X�} stand for the unique

gP -orthonormal  basis of  the  horizontal  subspace of T P     such  that X�  =      .  Starting
                                                                                  x�

from definition (3.9) of N , we have

N = -                         gP X�N, X� = -                                  
                                                       gM  (X�N ), x�
                           �                        �

                 = - gM         M N                    = - divM (N )
                                     x�       , x�
                             �

                 = M log f ,                                                             (3.39)

where divM and M stand for the divergence of a vector field and for the Laplacian of
a function on M4, respectively. The third equality uses a standard relation between the
Levi-Civita connection  on P and the Levi-Civita connection M on M , valid for all
Riemannian submersions (see page 240 of [Bes], for instance).

    It is clear from expressions (3.38) and (3.39) that the mean curvature components
|N |2 and N of the scalar curvature RP , unlike its other components |S|2 and |F |2, are
completely independent of the one-forms AL and AR that participate in the definition of
the higher-dimensional metric gP . They are only sensitive to the variation of the volume
(2.39) of the internal space K as one moves around the four-dimensional base M4.

Lagrangian densities on M4 � SU(3)

The purpose of this section is to bring together the work of the last few sections. We
want to write down the Lagrangian density in four dimensions that emerges from the
fibre-integral of the scalar curvature of the higher-dimensional metric gP . This scalar
curvature RP was decomposed in (3.4) into a sum of natural terms, including the scalar
curvatures of K and M ; the Yang-Mills term |F|2; the norm |S|2 of the fibres' second
fundamental form; and the norm and divergence of the fibres' mean curvature vector field
N . Defining the higher-dimensional Lagrangian density

                                             1                                           (3.40)
                                LP := 2 P (RP - 2 P ) ,

where P and P are real constants, we can integrate it over K using the explicit formulae
(2.40), (3.15), (3.25), (3.38) and (3.39) to obtain the four-dimensional density LM . The
result is that, after fibre-integration, the conceptually simple density on P cascades down

                                            31
to a more complicated but familiar group of terms in four dimensions, once the components
of the metric gP are separated from each other and are identified with four-dimensional
bosonic fields:

             1      RP - 2 P ) volg                                         (3.41)
LM = 2 P
                K
             1
      =           ( RM + RK - |F |2 - |S|2 - |N |2 - 2 N - 2 P volg

           2 P  K
             1
                             1  |FAL |20 + |FAR |20  - C dAL 2 - D d ||2 2
      =         RM f - 4 B
           2 P

                                                     - V (||2) - 2 M f Vol(K, 0) .

Here 0 is the Ad-invariant product on the Lie algebra su(3) defined in (2.23). It does
not depend on ||2. The term proportional to the Laplacian M f is a total derivative on
M4, so does not contribute to the classical equations of motion in four dimensions. The
coefficient functions f , B, C and D do depend on ||2 and are collected below:

                f := 4 (1 - ||2) 1 - 4||2                                   (3.42)

                B :=  f

                C :=   3 4 (1 - 2||2)

                         1 - 4||2

                D  :=  4 12 + 15 (1 - 2||2)2         -  7  f-1  df    2
                          8 (1 - ||2) (1 - 4||2)3/2     8       d||2
                                                                        .

Recall that we admit the possibility of  = (||2) being a constant or being an arbitrary
positive function of ||2. Finally, the potential term that does not depend on the gauge
fields or on the derivatives of  is given by

                         V (||2) := (2 P - Rg ) f ,                         (3.43)

where the scalar curvature Rg of K is explicitly given in (2.40) and is depicted in figure
1 of section 2. Inspecting this figure and the dependence of Rg on ||2, it is clear that
the potential V will explode to positive infinity when ||2 approaches the value 1/4 from
below. This is good news, since at ||2 = 1/4 the deformed metric g stops being positive-
definite, and we now see that it takes infinite energy to deform the bi-invariant metric
on K to such an extent. The detailed behaviour of V (||2) for smaller values of ||2,

however, will depend on the value of the constant P and on the specific dependence
(||2) that is chosen. For instance, in the next section we will see that if  is constant,
then the potential V (||2) will have absolute minima with ||2 = 0 whenever the real

constant  P is larger than 13/2. This suggests that the bi-invariant metric on K need

                                       32
not be the lowest-energy configuration of the system whenever P is positive, and that
deformed metrics such as g may be a better model for the classical "vacuum" geometry
of the internal space K.

    The explicit form of the function B given above, in (3.42), is a direct consequence of
the Yang-Mills term (3.15), definition (2.23) and the relation between volume forms on K
that says that volg is equal to f vol0. Likewise, the coefficient function C can be directly
read from formula (3.25) for the norm |S|2 and the relation between the two volume forms.
The calculation of D is slightly less immediate, as it combines contributions from |S|2,
|N |2 and N . The details will not be reproduced here, but the main intermediate steps
can be summarized as follows. The general identity for the scalar Laplacian

                               (log f ) = f -1 f - | grad (log f )|2 ,

combined with (3.38) and (3.39), implies that

    |N |2 + 2 N volg = 2 M f - f-1 df 2 vol0 .                                      (3.44)

At the same time, the third term in expression (3.25) for |S|2 can be rewritten as

    gM� ( log ) � log 2 (1 - ||2) 1 - 4||2       volg =
                                               d log(-4 f) 2 f
�,

    1  f-1 df 2 -                                               vol0 . (3.45)
    8

Then it is clear that the last term of D and the last term of LM result from the simple
sum of (3.44) with (3.45). On the other hand, the last term on the right-hand side of
(3.45) can be combined with the second term in formula (3.25) for |S|2 to obtain the first
term in the expression for D.

    Before ending this section, we will briefly discuss other possible choices to define the
density LP on the higher-dimensional manifold P . The choice (3.40) comes about as
the higher-dimensional analogue of the Einstein-Hilbert Lagrangian for general relativity,
of course. As in the four-dimensional case, the cosmological constant term P is not
particularly natural here, although it helps to obtain potentials V (||2) having minima
with  = 0. Unlike the four-dimensional case, however, the structure of the higher-
dimensional submersion  : P  M4 provides additional natural functions on P , besides
the scalar curvature of the metric gP , which a priori could be combined with RP to define
other variants of the density LP . We are talking about the fibres' second fundamental
form and mean curvature, of course. For instance, if we add to LP any linear combination
of the scalar functions |N |2 and N , it is clear from the previous discussion that the
Einstein-Hilbert and Yang-Mills terms in four dimensions will not be affected, and neither

       33
will the potential V (||2) and the coefficient C of the Higgs covariant derivative. Only
the function D will change, and this will in general be reflected in a different value for
the classical mass of the Higgs particle, as will be discussed in section 4.

    For example, a particularly nice combination of the scalar curvature RP with the two
functions |N |2 and N is

               WP   :=  RP    +  33 |N |2  +  11 N                               (3.46)
                                 32           4

                    =   RM    + RK  - |F |2   - |S|2   +  1 |N |2  +  3 N .
                                                          32          4

Indeed, if  : P  R+ is any positive function with constant values on the fibres and
g~P := 2 gP is the corresponding Weyl transformation, it is shown in appendix A.3 that
the function W~ P calculated for the rescaled metric satisfies the simple relation

                                    W~ P = -2 WP .

This contrasts with the complicated behaviour of RP under the same Weyl transforma-
tions. Here we focus on rescalings that are constant on the fibres, i.e. on scaling functions
 that are pull-backs to P of arbitrary functions on the base M4. A more general rescaling
on P would spoil its structure as a Riemannian submersion. If we use WP instead of the
scalar curvature RP to define the density LP , then fibre-integration over K yields the
following Lagrangian in four dimensions:

L^ M  =   1        WP - 2 P ) volg                                               (3.47)
         2 P
               K

            1               1    |FAL |20 + |FAR |20   - C dAL 2 - D^  d ||2 2
      =        RM f - 4 B

          2 P

                                                       -  V (||2)  +  3          Vol(K, 0) ,
                                                                      4 M f

where the potential V and the coefficient functions f, B and C remain the same as in
(3.43) and (3.42), respectively, while the function D^ is slightly changed to

               D^   :=  4  8  12 + 15 (1 - 2||2)2      +  27  f-1     df    2    (3.48)
                              (1 - ||2) (1 - 4||2)3/2     32          d||2
                                                                              .

Compared to the function D of (3.42), the new D^ has the advantage of being manifestly
positive for ||2 < 1/4. As will be seen in section 4, this property guarantees that the
radial component of the field (x)  C2 will have non-negative mass independently of the
choice of function (||2). This is not always true in the case of the first density LM .

                                              34
Vacuum configurations and Higgs-like potentials

In this section we will consider "vacuum" configurations where the metric gP is taken
to be a product metric (gM , g) on M4 � SU(3) with vanishing gauge fields AL and AR,
constant  and constant scalar curvature RM . We want to analyze the profile of the
potential that subsists in the Lagrangian densities LM and L^M in these configurations,
and want to check whether it can have absolute minima for non-zero values , as this
would lead to spontaneous symmetry breaking and mass generation for the gauge fields
of the model. For a broader discussion about vacuum configurations see also section 5.

    The terms that subsist in the four-dimensional Lagrangians with vanishing gauge fields
and constant  define a potential:

U (||2)  :=  V (||2) - RM f  =  3 3  -4 + 25 ||2 - 33 ||4 + 8 ||6
                                          (1 - ||2) 1 - 4||2

                                + 2 4 ( P - RM /2 ) (1 - ||2) 1 - 4||2 , (3.49)

where we have used formula (2.40) for the scalar curvature Rg and the definition of the
volume density f. For Minkowski space we have of course RM = 0. We allow the scale
factor  of the metric g to be any positive function (||2).

    Consider the simpler case where (||2) = 0 is a positive constant. Then the profile
of the potential, up to rescaling, depends on the single parameter

                                                  1                             (3.50)
                             a := 0 (P - 2 RM ) ,

which is assumed to be constant on the vacuum M4. At the point || = 0, corresponding
to the bi-invariant metric on K, the potential has the value 2 30 (a - 6), whereas it clearly
diverges in the limit ||2  1/4. Observe that if the constant a is positive and large, the

second term of the potential will decrease as || grows, and somewhere inside the interval

[0, 1/2[ this might just balance the increase of the first term in order to define a minimum

with || = 0. Due to the presence of high-degree polynomials, it does not seem possible

to give an analytic expression for these minima as a function of the parameter a, but we

may try to illustrate the situation with numerical plots. Start by defining

         V^a(x)         -4 + 25 x2 - 33 x4 + 8 x6                   
                 :=  3                             +  2a (1 - x2) 1 - 4x2 ,     (3.51)
                        (1 - x2) 1 - 4x2

for a real variable x, and taking the derivative

V^a(x)       :=  6 x (13 - 92 x2 + 205 x4 - 162 x6 + 48 x8)  +    12x(2x2 - 1)
                             (1 - x2)2 (1 - 4x2)3/2             a

                                                                       1 - 4x2

             =: x v1(x) + a v2(x) .

                                     35
Then any stationary point of V^a, apart from the obvious x = 0, will satisfy the equation
a = -v1(x)/v2(x). So we can plot the right-hand side to find out how many stationary
points exist for each value of the parameter a.

Figure 2: Auxiliary function -v1(x) / v2(x).

    It follows from this graphic that when a  6.5 the function V^a(x) has no stationary
point in the interval [0, 1/2[ besides x = 0. When a is larger than 6.5, the potential is
stationary at exactly one other positive point x0(a) that increases monotonously with a
and approaches the boundary x = || = 1/2 as the parameter a tends to infinity. The
stationary points � x0(a) are actually absolute minima of the potential V^a(x) in the open
interval ]-1/2, 1/2[, as follows from the graphics below.

Figure 3: Potential V^a(x) for a  6.5: single minimum at x = 0.

a=4      a = 6.5

     36
Figure 4: Potential V^a(x) for a > 6.5: minima with x = 0. 3

               a=7                                                 a = 10

    Thus, the potential V^a(x) coming from the fibre-integral of the higher-dimensional
density RP - 2P can have a double-well profile, similar to the usual Higgs potential,
whenever its parameter is in the half-line a > 6.5. In this case the potential's absolute
minima occur for x = 0. Since the variable x is just ||, we conclude that there are
relatively natural Kaluza-Klein-like models where the bi-invariant metric on the group K
is not the lowest-energy configuration of the system. Perhaps a deformed metric such as
g, exhibiting manifest left-right asymmetry, could also be considered as a model of the
classical "vacuum" geometry of the internal space K. See also the discussion in section 5.

    The potential depicted in the previous graphics was written in (3.51) under the as-

sumption that the scale factor  of the metric g -- the factor appearing in definitions
(2.23) and (2.25) -- is just a constant 0. This is certainly the simplest choice. However,
as mentioned before, one can also consider definitions of g that include a generalized
scale factor depending on ||2, and the explicit calculations of the previous sections were
open to this possibility. A non-trivial dependence (||2) would affect the formulae for
the scalar curvature Rg and volume coefficient f as functions of ||2, and hence would
certainly affect the shape of the potential V (||2) coming from (3.43). One could, for

example, consider scale factors of the form

                                                                                            q          (3.52)

                   ||2 = 0 (1 - ||2) 1 - 4||2

for some power q. Then the potential function V^a(x) defined in (3.51) would change to
the more versatile variant

V^a,q (x)  :=  3  -4 + 25 x2 - 33 x4 + 8 x6  +  2a                                             1+4q .
                                                                   (1 - x2) 1 - 4x2
                  (1 - x2) 1 - 4x2  1-3q

3Figures generated with the free online version of Wolfram Alpha.

                                                         37
Observe that the special choice q = -1/4 would yield a volume form volg and a coefficient
function f completely independent of ||2, as follows from (2.37) and (3.36). While this
choice could simplify parts of the four-dimensional Lagrangian LM , the constancy of
f would also prevent the appearance of potentials with minima for || = 0, since the
potential V would essentially just be minus the scalar curvature Rg, up to constants.
A second interesting choice is q = -1/5, since in this case the coefficient function B is
constant and independent of ||, as follows from (3.42). In other words, for q = -1/5 the
coefficients of the Yang-Mills terms in LM do not depend on the Higgs field , as happens
in the traditional Standard Model Lagrangian. The same procedure that was described
in the case of constant  leads to the conclusion that, in the case q = -1/5, the absolute
minima of V^a,q(x) have x = 0 whenever the parameter a is larger than the value 14.5.

    More generally, for an arbitrary positive function (||2), observe that the potential
U (||2) written in (3.49) has finite value at || = 0 and diverges to positive infinity as
||  1/2. So a sufficient condition for U to have absolute minima with || = 0 is that it
is a decreasing function for small ||2. But expanding  around the origin:

(||2) = 0 1 + b ||2 + d ||4 + O ||6 ,                                         (3.53)

the corresponding expansion of U is

U (||2) = 30 2 (a - 6) + (39 - 6 a + 8 ab - 36 b) ||2                         . (3.54)
           + (18 + 12 ab2 - 24 ab + 8 ad - 36 b2 + 117 b - 36 d) ||4 + O ||6

So the potential U (||2) is a decreasing function near the origin whenever

    39 - 36 b 9 6
a>                                   =+      .
    6-8b                             2 3-4b

Thus, for any fixed positive function (||2) with b = 3/4, there is a wide range of values
of the constant a for which the potential U will have absolute minima with || = 0.

Kaluza-Klein normalizations

Four-dimensional Lagrangians determined by the higher-dimensional scalar curvature RP
through Kaluza-Klein-type calculations are similar to, but never exactly equal to, the
traditional Lagrangians of Einstein-Maxwell or Einstein-Yang-Mills field theories. Hence
the four-dimensional equations of motion of the classical fields will also not be exactly
the same. If we want that at least the linearized equations of motion around the vacuum
configuration coincide with the traditional ones, then a series of standard normalizations
must be established [BL, DNP].

                                                       38
    If we assume that in the dynamical theory the parameter  is always close to its
vacuum value 0, then the coefficient f in front of the curvature RM in Lagrangians
(3.41) and (3.47) will also be approximately constant and equal to its vacuum value f0.
In this case, the scalar curvature term will resemble the usual Einstein-Hilbert term in
four-dimensions, provided that the constant P satisfies the normalization condition

     1                               1           P = M Vol(K, g0) ,                          (3.55)
     2 P f0 Vol(K, 0) = 2 M

where M = 8 G c-4 is the Einstein gravitational constant. Again, if  is close to its
vacuum value 0, also the potential term in (3.41) and (3.47) will be approximately
constant at its minimum value V (|0|2). In this case, the potential term resembles a
four-dimensional cosmological constant term M determined by

 1   V (|0|2) Vol(K, 0)     =         1                         2 M = 2 P - R(g0) . (3.56)
2 P                                 2 M 2 M

To normalize the Maxwell term of the photon gauge field, recall from section 2 that, among

the left-invariant vector fields on SU(3), there is a special one that is a Killing field of the

metric g. It is generated by a vector  in the subalgebra (u(2)) of su(3) that satisfies
[, ()] = 0 and, up to normalization, is explicitly given by (2.32). Decomposing su(3)
into the sum of the span of  and its orthogonal complement, the photon field AL is
defined as the component of AL with values in . The normalization of the field AL is
determined by the normalization of . Again, if  is close to its vacuum value 0, the
Maxwell term in Lagrangians (3.41) and (3.47) will resemble the canonical Maxwell term
only if we pick the normalization  of  satisfying the condition

                             1   B0  0 ( 0   ,       )  Vol(K,  0)  =     1.
                            2 P                   0

Using the definition of B0, the definition of  and the previous normalization condition
(3.55), this equation is equivalent to

      1     ( 0  ,       )  Vol(K,  g0 )  =  1                    ( 0  ,       )  =  2 M  .  (3.57)
     2 P              0                                                     0

At this stage, we will not try to normalize the electroweak and strong-force fields, since

the metrics  and g are not flexible enough to allow for separate normalizations of these
fields. This will be addressed in section 5.2 using the metrics ~ and g~, which allow for
adjustable values of the classical gauge coupling constants.

                                                39
4 Masses of the classical fields

Higgs-like particle

The purpose of this section is to calculate the classical masses associated to the fields AL,
AR and  that appear in the four-dimensional Lagrangian density LM written in (3.41).
As customary [Wei, Wei2, Ham], the calculation is made in the approximation of weak
fields that are small perturbations of the vacuum configuration defined by vanishing AL
and AR and by constant  = 0. We also work on Minkowski space with RM = 0. Since
the Lagrangian LM is derived from the higher-dimensional scalar curvature, its terms do
not come with the normalized coefficients that are conventional in the literature, so we
will resort to the associated equations of motion to read the mass values.

    Let us start with the mass of the "Higgs particle", that is, the mass of the radial
component r(x) of the field (x)  C2. For 0 = 0, we can write in the unitary gauge

                                  (x) = r(x) 0                                             (4.1)
                                                   |0|

and take the derivative

                         d ||2 2 = d r2 2 = 4 r2 gM� (�r) (r) .                            (4.2)

Using expression (3.24) for the covariant derivative of fields with values in C2, the norm
that appears in LM can be expanded as

dAL  2 = gM� Re             dAL   dAL                                                  (4.3)
                                  �                                                ,

= gM�                       (�r)(r) +   r2          (AL)j� (AL)k  Re  (ej 0) ek 0
                                       |0|2

where we have also used that 0 ek0 is purely imaginary, since ek comes from a unitary
action on C2 and hence is an anti-hermitian matrix. The coefficient functions f , B, C and
D that appear in the Lagrangian LM depend on r2 only, so can be written as B = B(r2),
for instance. Doing this rebranding, taking the first variation of LM with respect to r
and ignoring the total derivative originated by M f , yields the following equation of
motion for r(x):

2 E(r2) gM� (�r)         +  2r E(r2) gM� (�r)(r)    -   r B(r2)       |FAL |20 + |FAR |20
                                                        2             - 2r V (r2) = 0 ,

- C(r2)                      2r   (AL)�j (AL)k  Re  (ej 0) ek 0                            (4.4)
                            |0|2

where E(r2) stands for the combined function C(r2) + 4r2 D(r2). A vacuum configuration
for gP is defined as a product metric on M � K that minimizes the potential V (||2), so

                                                40
it is a configuration with vanishing one-forms AL and AR and a constant  = 0 such
that V (|0|2) = 0. Around the vacuum configuration we can decompose r(x) = r0 + (x),
with r0 = |0| added to a small field (x), and expand

   r V (r2) = (r0 + ) V (r02) + 2 r02 V (r02)  + � � � = 2 r02 V (r02)  + � � � .

Also AL and FA will be small near the vacuum configuration, so only keeping the first
order terms out of the full equation of motion yields the Klein-Gordon equation

                    gM� �      -             2 r02 V (r02)        =  0.
                                        C(r02) + 4 r02 D(r02)

Since we are working in (- + ++) signature, the squared-mass of the radial field r(x) can

be defined as the coefficient

                    MH2  :=    (Mass r)2   =            2 r02 V (r02)     .        (4.5)
                                                   C(r02) + 4 r02 D(r02)

If 0 is an absolute minimum of the potential V (||2), then the numerator of the squared-

mass is non-negative. However, a priori nothing can be guaranteed about the denomina-

tor, since the function D(||2)) defined in (3.42) has one negative term that depends on

f, and hence on the chosen form of the scale factor (||2). This puts a constraint on
the choice of function (||2). This does not happen for the Lagrangian L^M , as in this
case D^ (||2)) is always positive in the domain ||2 < 1/4, as already pointed out.

Gauge bosons

The calculations leading to a mass formula for the fields AL and AR mimic, in every
essential way, the calculations usually performed in the case of the electroweak gauge

fields of the Standard Model [Wei, Wei2, Ham]. One works in the approximation where

the one-forms AL and AR are small, close to their vanishing "vacuum" value, and the
parameter   C2 is approximately constant and equal to 0. The terms of the four-
dimensional Lagrangian LM that depend on AL and AR are

         -  1            |FAL |20 + |FAR |20       + C dAL  2     Vol(K, 0) ,
            4 B                                                      2 P

where one should keep in mind that the whole formula (3.41) for LM is valid only for
one-forms (AL AR) with values in the subalgebra (u(2))su(3) of the bigger su(3)su(3).
This expression does not contain any quadratic terms on the fields AR, so they have zero
mass in the model. Using formula (4.3) for the norm of the covariant derivative dAL at

constant  = 0, the terms involving AL can be rewritten as

-  1     0(ek, ej)  (FAkL )� (FAj L )�  +  C0  (AjL)� (AkL)�  Re  (ej 0) ek 0  Vol(K, 0) ,
   4 B0                                                                           2 P

                                               41
where we have chosen a basis {ek} for the subspace (u(2)) of su(3), while 0 is just the
usual Ad-invariant product 0(u, v) = Tr(u v) on su(3). Working with the Levi-Civita

connection  on M and ignoring total derivatives, the first variation of the expression
above with respect to (ALj )� leads to the equations of motion

B0 0(ek, ej) gM� gM  (FAkL )� - 2 C0 gM� (ALk )� Re (ej 0) ek 0 = 0 . (4.6)

In the particular case where the basis {ek} is 0-orthogonal (u(2)) and, simultaneously,
diagonalizes the quadratic form (u, v)  Re (u0) v0 on the same space, the equa-
tions of motion can be simplified to

gM�  (FAkL )�  -       2 C0     (AkL)  Re  (ek 0) ek 0   = 0,  (4.7)
                  B0 0(ek, ek)

where no sum over the index k is intended. The usual arguments using the Lorentz
condition �Ak� = 0 (e.g. see [MS, section 2.7]) then say that, to first order in the fields,
these equations can be simplified to the Klein-Gordon equation for gauge fields of mass

Mass (ALk )� 2    :=  2 C0 (ek 0) ek 0                         (4.8)
                         B0 0(ek, ek)

                  =   6 (1 - 2|0|2) (ek 0) ek 0          ,

                       (1 - |0|2) (1 - 4|0|2) 0(ek, ek)

where we have used the explicit expressions (3.42) for the coefficient functions B and C
evaluated at the vacuum value 0. Recall that in this formula the vacuum vector 0 should
be regarded as an element of C2; the squared-norm |0|2 stands for the canonical norm
on C2; and ek is the representation of u(2) on C2 induced by the U (2)-representation
  (det a) a on the same space. Unwinding the path that originally lead us to the
representation ek, one can also express the quadratic form (ek0) ek0 in C2 as an
equivalent form in su(3). In fact, it follows from the initial expressions (2.4) and (2.6)

that this relation is simply

2 Re (ej 0) ek 0 = Tr [ej, 0 ] [ek, 0 ] ,                      (4.9)

where all the vectors on the right-hand side should be regarded as elements of su(3), and
0 should have properly been written as (0)  (C2)  su(3). Thus, an alternative
formula for the mass of the fields ALk is

Mass (AkL)� 2     =   3 (1 - 2|0|2) Tr [ek, 0] [ek, 0]   .     (4.10)
                       (1 - |0|2) (1 - 4|0|2) Tr(ek ek)

Again, this formula assumes that the basis {ek} is 0-orthogonal in (u(2)) and, simulta-
neously, that it diagonalizes the quadratic form (u, v)  Tr [u, 0] [v, 0] on the same

                      42
subspace of su(3). One such basis is explicitly constructed in appendix A.1, comprising
four 0-orthogonal vectors (, z, w1, w2). If the components of the one-form AL on that
basis are denoted by

     AL = A  + Z z + W 1 w1 + W 2 w2 ,

then the classical mass associated to each of these component fields follows directly from
(4.10) and the algebraic identities (A.6) and (A.9) of the appendix. We obtain:

M2 := [Mass (A)�]2 = 0                             (4.11)

MW2  :=  [Mass (W a)�]2  =     3 1 - 2|0|2 |0|2
                               1 - |0|2 1 - 4|0|2

MZ2 := [Mass Z�]2 = 4 MW2 .

The simple relation MZ = 2 MW , obtained above, seems to be a feature of the classical
model described so far. However, it is significantly different from the experimental ratio
MZ  1.13 MW observed for the masses of real Z and W -bosons. One can point out
that these are calculations for the bare masses, and all the relations are at the classical,
unification energy scale, not at the experimental energy scale. But unless the running
coupling constants and quantum radiative corrections come to the rescue in significant
amounts -- something that will not be studied here -- this discrepancy shows that the
fields W�a and Z� described above cannot be regarded as quantitatively precise models for
the real electroweak gauge fields. This situation will be improved upon in section 5.2.

    That being said, the numbers and expressions obtained above do not seem to be
entirely off the mark either, especially for a Lagrangian derived from a remote object such
as the higher-dimensional scalar curvature. Let us consider the mass ratios MH / MW and
MH / MZ, for example. The second equation in (4.11) gives an explicit expression for the
classical mass of the W -like boson in terms of the constant  and the value of ||2 at
the minimum of the potential. At the same time, formula (4.5) gives an expression for
the mass of the Higgs-like boson in terms of similar variables, so we can try to compare
the two masses. The potential V^a,q considered in (3.53) depends on two parameters. We
discussed at length the simplest choice q = 0, and then also mentioned the case q = -1/5.
For each value of q the potential depends on the second parameter a, defined in (3.50),
which also affects the "vacuum expectation value" |0|. Tables 1 and 2 register the
numerically approximated values of |0| and V (|0|2) as the parameter a takes a sequence
of naive, non-optimized values, bigger than the threshold necessary to produce double-
well potentials. Formula (4.11) was then applied to calculate the associated mass 0 MW2
as the parameter varies.

                         43
    Turning to the mass of the Higgs-like boson, recall that in section 3.6 we discussed two

different Lagrangian densities on P , that lead to distinct four-dimensional Lagrangians
LM and L^M after integration over the fibre. The two Lagrangians have the same implicit
potential V , and hence lead to the same values of |0| and MW , but they differ on the
coefficient function D(||2) defined in (3.42) and (3.48). Hence, through formula (4.5),

they lead to distinct masses MH of the Higgs-like boson. Tables 1 and 2 also register the
numerically approximated values of 0 MH, calculated from (4.5), using the same sequence
of values of the parameter a.4 They are presented indirectly through the ratios MH/MW .

                                              0 MH2        MH / MW MH / MZ

a      |0| 0-3 V (|0|2) 0 MW2          LM            L^ M LM L^ M LM L^ M

6.5 0           1             0            0         0     ---        -

6.51 0.04076    1.02          0.00501 0.0406 0.0392 2.85 2.80 1.42 1.40

6.55 0.09040    1.10          0.0251 0.215 0.182 2.92 2.69 1.46 1.34

6.6 0.1266      1.19          0.0505 0.462 0.333 3.02 2.57 1.51 1.28

6.8 0.2110      1.56          0.155 1.91 0.764 3.51 2.22 1.75 1.11

7 0.2621        1.89          0.263 4.63 1.05 4.19 2.00 2.10 1.00

8 0.3794        3.21          0.847 -82.1 2.09 - 1.57 - 0.786

30 0.4912       13.2          14.1 -1758 27.6 - 1.40 - 0.698

100 0.4978      26.5          56.2 -25826 109 - 1.39 - 0.697

500 0.4996      60.8          296 -704802 574 - 1.39 - 0.696

Table 1: Bosonic mass ratios for different values of the parameter a when q = 0.

                                              0 MH2        MH / MW    MH / MZ
                                                           LM L^ M    LM L^ M
  a      |0|    0-3 V (|0|2)  0 MW2    LM            L^ M
14.5       0          17          0                          --         --
14.51                17.0                  0         0     2.63 2.63  1.31 1.31
14.55  0.01977       17.1     0.00117                      2.62 2.62  1.31 1.31
14.6   0.04390       17.2     0.00581  0.00811 0.00811     2.62 2.62  1.31 1.31
14.8   0.06189       17.6     0.0116                       2.62 2.61  1.31 1.30
 15    0.1059        18.0     0.0346   0.0399 0.0399       2.61 2.59  1.31 1.30
 16    0.1352        20.0     0.0574                       2.59 2.55  1.30 1.27
 30    0.2215        44.8      0.168   0.0797 0.0794       2.47 2.36  1.23 1.18
 100   0.4335        149       1.456                       2.41 2.32  1.21 1.16
 500   0.4874        648               0.237 0.235         2.39 2.30  1.20 1.15
       0.4980                   6.89
                                37.0   0.392 0.387

                                       1.13 1.09

                                       8.88 8.13

                                       40.1 37.0

                                       212           196

Table 2: Bosonic mass ratios for different values of the parameter a when q = -1/5.

4Numerical computations using the free online calculator available in https://wims.unice.fr/wims/ .

                                       44
    The experimental values of these ratios are approximately MH / MW  1.56 and
MH / MZ  1.37. Thus, a first observation is that the values in tables 1 and 2 are
certainly inaccurate, but reasonably within the correct order of magnitude, even though
the model does not rely on an independent parameter to adjust the mass of the Higgs-like
boson. Since the classical model works with the inaccurate relation MZ = 2 MW , one
cannot expect it to simultaneously match both experimental MH/M� ratios, but an hy-
pothetical correction to that initial inaccuracy could improve the ratios correspondence
as well. This is most evident in table 2, where a slightly lighter Z and a slightly heavier
W would bring both ratios closer to the experimental values.

    In section 5.2 we will describe a version of the present model where the metrics on
internal space  and g have additional deformation parameters, equivalent to the three
gauge coupling constants of the Standard Model. Using these new parameters one can
adjust the mass ratio MZ/MW at will, and hence improve the adherence of the model
to the experimentally observed values of the bosons' masses. The downside is that more
adjustable parameters diminish the predictive usefulness of the model, of course.

    An interesting facet of the formula for the mass of the W -boson is its relation with the

volume and scalar curvature of the vacuum internal space (K, g0). Direct combinations
of (4.11) with expressions (2.39) and (2.40), from section 2, lead to the relations

    Vol (K, g0)  =                   1 - 2 |0|2 4            (4.12)
                        3 64 5 |0|8  1 - 4 |0|2 7/2

                    MW8 1 - |0|2 3

    R(K, g0)     =  MW2   4 - 25 |0|2 + 33 |0|4 - 8 |0|6  .
                           |0|2 1 - |0|2 1 - 2|0|2

These are determined by the vacuum "expectation value" |0| at the minima of the po-
tential and have the merit of not depending explicitly on the unknown scaling factor
.

Some numerical estimates

Consider again the vector  in su(3) that generates the electromagnetic U(1)-isometries
of the metric g. It was defined in (2.32) as a function of . The normalization condition
(3.57) was applied in the calculations of [Ba], section 2, and lead to a relation between the

positron electromagnetic charge e and the inner-product (, ) in the approximation

where  is constant and equal to its vacuum value 0. This relation is the first equality

in   e2
    6 M
         = (0, 0) =  Tr(0 0) = 2  .                          (4.13)

                          45
The second equality is the definition of the product  and the third equality follows from

calculation (A.6) in the appendix. In Lorentz-Heaviside-Planck units with c =  = 0 =
�0 = 8G = 1, we have that M = 1 and e = 4, where   1/137 is the fine-structure
constant. Thus, we get at estimate for the scale factor  that appears in the definitions

of the metrics  and g,

                              (|0|2)       e2   =                             (4.14)
                                      =                 .

                                         12 M       3

Using this value in formula (4.11) for the mass of the W-bosons, one obtains

      MW2               =        9 |0|2 P2 - 2|0|2            MP2 ,           (4.15)
                                 P2 - |0|2 P2 - 4|0|2


where we have displayed the implicit Planck length P = 8Gc-3 and Planck mass

MP = c/(8G), so that the equation remains valid in any system of units. Recall

that || refers here to the standard norm in C2 of the vector , which is identified with

an element of su(3), i.e. a tangent vector to the internal space K, and thus has the

dimensions of length. But the experimental value of MW is many orders of magnitude
smaller than the Planck mass, so the formula above implies that the vacuum value of the

deformation  must be very small, that is |0| << P inside its usual domain [0; P /2[.

In fact, using the experimental value of MW and calculating to lowest order in the ratio

MW /MP , we get the estimate

                        MW
        3               MP
|0|                           P       1.67 � 10-18 P       1.35 � 10-52 m .   (4.16)

The values of  and |0| coming from these estimates can also be applied to formulae

(2.39) and (2.40), giving the volume and scalar curvature of the vacuum metric g0 on

the internal space K. To lowest order in |0|, we obtain that

                                           2    4          ( 0.27 P )8
Vol (K, g0)  3 5                             3
                                                  P8

      R(K, g0)                   36   P-2  .                                  (4.17)


For very small |0|, formula (4.5) for the mass of the Higgs-like boson also gets simplified.
Since the coefficient function D(|0|2) is finite at the origin, to lowest order in |0|2 we
have the asymptotic expression

      MH2                  2 |0|2 V (|0|2)      2 |0|2 V (|0|2)      .        (4.18)
                                C (|0 |2 )             3 4

Using expansion (3.54) of the potential V (||2), to lowest order in |0|2 the second deriva-
tive is constant,

V (|0|2)  V (0) = 2 30 (18 + 12 ab2 - 24 ab + 8 ad - 36 b2 + 117 b - 36 d) , (4.19)

                                      46
whereas the potential has an absolute minimum for positive but very small |0|2 only if the
constant a is just slightly bigger than the critical value (39 - 36 b)/(6 - 8 b). Substituting
this value of a in the second derivative (4.19), we obtain that, to lowest order in |0|2,

MH2      4 (18 + 16 d - 63 b + 30 b2  - 24 b3)  |0|2  .   (4.20)
                       0 (3 - 4 b)


This asymptotic expression for MH2 can be compared with the behaviour of MW2 and MZ2
for small |0|2, as implied in (4.11). The comparision leads to the mass ratios

MH  =   MH     18 + 16 d - 63 b + 30 b2 - 24 b3           (4.21)
MZ     2 MW                                            .

                            3 (3 - 4 b)

This is the asymptotic value of the ratios when the constant a in the potential tends
from above to the critical value (39 - 36 b)/(6 - 8 b). In other words, when the constant
a is chosen so that V (||2) attains its absolute minima for positive but very small |0|,
as suggested by (4.16). The asymptotic value of the ratio depends on the behaviour of
the function (||2) near the origin, reflected here in the presence of the coefficients b
and d coming from expansion (3.53). In the case of a constant function (||2) = 0, the
coefficients b and d vanish, so we get that MH/MZ  1.41 for very small |0|, in agreement
with the numerical values on top of table 1. In the case of a function (||2) defined by
(3.52) with constant q = -1/5, the expansion coefficients are b = 3/5 and d = 27/25, so
we get an asymptotic mass ratio of MH/MZ  1.31, in agreement with the values on top
of table 2. When the behaviour of (||2) near the origin is determined by coefficients b
and d such that the numerator of (4.20) is negative, or b = 3/4, the derivation of (4.20)
is not valid and the formula is not applicable.

               47
5 Further investigations

Higher-dimensional equations of motion

In section 2.3 we defined the family of left-invariant metrics g on K = SU(3) and studied
several of its properties. Subsequently, in section 2.6, we looked at higher-dimensional
metrics gP on the product P = M4 � K that coincide with g when restricted to the fibres
K. The parameter (x)  C2 was allowed to depend on the fibre in question, i.e. it was
allowed to depend on the coordinate x  M4. Finally, we studied the fibre-integral of the
higher-dimensional density RP - 2P and showed that it defines a Lagrangian on M4 with
terms very similar to those found in the Standard Model Lagrangian. These similarities
include the presence of a Higgs-like field (x) with its usual covariant derivative; the
four-dimensional Yang-Mills terms, as in the familiar Kaluza-Klein calculation; and the
existence of a potential term that, in some cases, has absolute minima for non-zero values
of , leading to spontaneous symmetry breaking and a vacuum metric with U(1) � SU(3)
isometry group, which in turn produces the usual massless gauge bosons.

    However, we have not really justified the initial choice of metric g on the internal
space, other than pointing to its nice features and to the similarities of the resulting geo-
metrical model with the bosonic part of the Standard Model. More importantly, having
always worked with fibre-integrals leading to effective Lagrangians in four dimensions,
we have not investigated whether the internal metrics g would be stable in a fully dy-
namical higher-dimensional theory. The potential V (||2) may govern the dynamics of
the parameter  within the restricted family of metrics g, so that a minimum of the
potential corresponds to a metric that is stable within the family. But nothing was said
about stability in the space of all metrics on P . If all the coefficients of the internal
metric were allowed to be dynamical, besides the parameter (x), what would prevent
an initial metric g to evolve over time to a metric outside that family, according to the
higher-dimensional, classical equations of motion?

    If the higher-dimensional equations of motion are determined by the Lagrangian RP -
2P on P , then the classical solutions are the Einstein metrics. But a cartesian product
of metrics gM � gK is Einstein on M4 � K if and only if both gM and gK are Einstein, with
the same constant, on the respective spaces. Thus, our vacuum metric gM � g0 cannot
be a solution of the full equations of motion, since the left-invariant metrics g are not
Einstein on K, except for the bi-invariant metric at  = 0.

    To justify the last assertion, recall that a metric on an n-dimensional compact manifold

                                                       48
K is Einstein if and only if it is a critical point of the normalized functional

E (g) := (Volg K)(2-n)/n Rg volg .                                                (5.1)

                                                   K

The left-invariant metric g has constant scalar curvature, so the integral above is equal
to (Volg K)2/n Rg. Putting n = 8 and using formula (2.40) we obtain

E (g) = (Volg K)1/4 Rg                                                            (5.2)

=  6         1/4  4 - 25 ||2 + 33 ||4 - 8 ||6         .
        3 5        (1 - ||2)7/4 (1 - 4||2)7/8

If a particular g0 is a critical point of functional (5.1) for general variations of the metric,
then it must define a stationary point of function (5.2) under variations of , since these
are just a special kind of variation of the metric. But a simple plot shows that the only
stationary point of E(g) as a function of || happens at || = 0. Therefore, the only
possible Einstein metric in the family g is the bi-invariant metric, which is well-known
to be Einstein. Notice how the scaling factor (||2) of the metric g is absent from (5.2),
therefore the argument is valid for any choice of scaling function.

    The stability of vacuum metrics under higher-dimensional dynamics is an important
and challenging topic in Kaluza-Klein theories, as already mentioned in the Introduction.
It has been extensively studied and discussed in the literature. See for instance the reviews
in [BL, DNP, Wi1]. Within the small realm of the present model, after recognizing that
the metrics g are not Einstein, once could try to address the problem in several, non-
exclusive ways. The first would be to propose that the higher-dimensional dynamics may
be governed not by the Lagrangian RP - 2P , but by a more elaborate scalar density
whose associated equations of motion could have something like gM � g0 as a classical
solution. A second way would be to study vacuum metrics that are not pure cartesian
products gM � g0, for example letting 0 have a slight dependence on the x coordinate,
and see if this concession leads to an Einstein metric that could be a reasonable candidate
for the vacuum. A third approach, probably the most natural within the limited scope of
our model, would be to slightly adjust the definition of the metric g and accept additional
parameters besides  and the scaling factor . The hope would be to find a solution of
the Einstein condition in this enlarged family of metrics, which in turn would help to fix
the values of the additional parameters. We will now elaborate on this third route.

A more precise version of the model

Motivated by the inaccuracy of the classical relation MZ = 2MW , obtained in section
4.2, as well as the previous discussion about the instability of product metrics gM � g0

                                                       49
under the higher-dimensional equations of motion, we will now adjust the definition of the
metric g on the internal space by including additional deformation parameters that may
help mitigate those problems. The additional parameters essentially correspond to the
three different gauge coupling constants of the Standard Model, so it sounds reasonable
to let them be adjustable.

    Recall that the metric g on SU(3) was defined as the left-invariant extension of the
inner-product on su(3) determined by (2.25). This formula uses the Ad-invariant product
(u, v) =  Tr(u v) on su(3) and, in fact, the deformation g is defined to coincide with
 when restricted to the subspaces (u(2)) and (C2). Let us now relax these definitions
by renouncing to , the most general AdSU(3)-invariant product on the Lie algebra su(3),
and use instead the general AdU(2)-invariant product on su(3), which we will call ~.
Decomposing vectors in su(3) = u(2)  C2 = u(1)  su(2)  C2 as

v = v + v = vY + vW + v ,                            (5.3)

the product ~ on su(3) can be written as a sum

~(u, v) := 1 Tr(uY vY ) + 2 Tr(uW vW ) + 3 Tr (u) v  (5.4)

for positive constants 1, 2 and 3. So the new product ~ is a version of  with an
independent rescaling factor in each component of su(3). Using the finer decomposition
(5.3), the formula for the AdU(2)-action on su(3) can be written as

             - Tr(vY ) -[ (det a) a v ]         

Ad(a)(v) =                                      ,    (5.5)

             (det a) a v vY + Ada(vW )

instead of (2.6), for all matrices a  U(2). It is not difficult to convince oneself that ~
is indeed the most general inner-product on su(3) invariant under such transformations.
The new deformed metric g~ can then be defined in terms of ~ by a formula entirely
analogous to the definition of g in terms of , namely

g~(u, v) := ~(u, v) + ~ ( [u, v] + [v, u],  )        (5.6)
            = ~(u, v) + ~ ( [Ad u, v],  ) .

This definition implies that the product g~ coincides with ~ when restricted to the sub-
spaces u(2) and C2 of the larger su(3), although these subspaces are not g~-orthogonal to
each other. One can check that the orthogonal complements (C2) for the new product

g~ coincides with that calculated for the product g, so is still given by (2.27). Formula
(2.26) for u(2) is no longer valid, however, due to the different rescalings inside u(2).

             50
The transformation rule of g~ under the AdU(2)-action on su(3) remains as calculated for

g, namely

                           (Ad(a)-1 ) g~ = g~(det a)a                            (5.7)

for any a  U(2). The arguments of section 2 carry over to show that when we extend g~ to
a left-invariant metric on K, it has an U(1) � SU(3) isometry group. The electromagnetic

U(1) is generated by the same left-invariant vector field as before, namely L, where the
matrix  is given by (2.32) and is the unique element in the subspace (u(2)) of su(3)
that satisfies [, ()] = 0, up to normalization. The norm of this matrix is now

                  g~(, ) = ~(, ) = (1 + 3 2) / 2 .                               (5.8)

Orthonormal basis and volume form

Let {u0, . . . , u3, w1, . . . , w4} be a ~-orthonormal basis of su(3) = u(1)  su(2)  C2 such
that the vectors {wj} span the subspace (C2) of su(3); the vectors {u1, u2, u3} span the

subspace (su(2)); and u0 is the vector

                           1                      1
                  u0  =     diag(-2i, i, i)   =            (iI2)  ,              (5.9)
                             6 1                   6    1

that spans (u(1)). We want to use these vectors to define a g~-orthonormal basis of
su(3). The subset {w1, . . . , w4} automatically defines an orthonormal basis of (C2), since
g~ coincides with ~ on that subspace. The extension of identity (2.34) to the new setting

is

           g~ u + [u, ], v + [v, ] = 1 - 32-1 ||2 ~(u, v)                        (5.10)

for any vectors u and v in (su(2)). It follows that the vectors

           vj :=             1                          for j = 1, 2, 3,         (5.11)
                      1 - 32-1 ||2 (uj + [uj, ])

are g~-orthonormal and are also orthogonal to the wj. An explicit calculation then shows

that the desired g~-orthonormal basis of su(3) can be completed with the vector

              2-3 1 - ||2                   3  2i  - i||2I2 + 2-3 1i
      2-3 1 - 1 + 3 2-1 1
v0 =                       ||2 u0 +                                              .

                                        21 2-3 1 - ||2 2-3 1 - 1 + 3 2-1 1 ||2

This is the analog of formula (2.36) for the new metric g~, instead of g. Using the or-
thonormal basis {v0, . . . , v3, w1, . . . , w4} of su(3) that has just been constructed, a deriva-
tion entirely similar to that of section 2 leads to the volume form

      vol g~ = 1 - 32-1 ||2 1 - 3 2-1 + 3 1-1 ||2 vol~                           (5.12)

                   = 1 23 34 1 - 3-2 1 ||2 1 - 3 2-1 + 3 -1 1 ||2 vol0 .
This expression reduces to (2.37) in the special case where 1 = 2 = 3 =: , of course.

                                        51
Yang-Mills terms

The substitution of the products  and g on su(3) by the more general ~ and g~ demands
very few changes in the derivation of the four-dimensional Yangs-Mills terms, as obtained
by fibre-integration of the higher-dimensional scalar curvature. One point that does need
to be adapted, however, is the calculation of the fibre-integral of products of right-invariant
vector fields, as (2.30) is no longer valid. Now we will go through these calculations and, at
the end, record the correspondence between the parameters 1, 2 and 3 of the product
g~ and the gauge coupling constants of the model.

    On the general grounds of (2.11) we know that, for any group element h  K,

g~(uR, vR) |h = ~(Adh-1 u, Adh-1 v) + ~ [Adh-1 u, Adh-1 v],  .                    (5.13)

This formula is not as simple as (2.29) because ~, unlike , is not AdSU(3)-invariant. But
~ is still invariant under the adjoint action of the element  = diag(1, -1, -1), so the

calculations immediately below (2.29) carry over to show that

                  g~(uR, vR) vol g~ =          ~(Adh-1 u, Adh-1 v) vol g~ .       (5.14)

           hK                          hK

Since the right-hand side of this equation integrates the Adh-action over all h  K, the
resulting integral must be invariant under AdSU(3)-transformations of the vectors u and
v. In other words, the resulting integral must be proportional to the Cartan-Killing
product Tr(adu adv) on su(3). To determine the constant of proportionality it is enough
to calculate the integral in the case where u and v are both equal to the diagonal matrix
e0 := diag(-2i, i, i) in su(3). For any element h  SU(3), a direct computation with
matrix components yields

                              |h11|2 - 1/3        h11h21                 
                                               |h21|2 - 1/3  h11h31

Adh e0  =  h e0 h  =  -3  i    h11h21             h31h21     h21h31            .  (5.15)


                               h11h31                        |h31|2 - 1/3

The components of Adh e0 defined by decomposition (5.3) can be easily read from the
right-hand side matrix. In terms of the usual isomorphism  : u(1)  su(2)  C2  su(3)
we have that

(Adh e0)Y      3   h11|2 - 1/3 e0                                                 (5.16)
           =

               2

(Adh e0)W = -3        i      |h21|2 + |h11|2 - 1 /2          h21h31

                                       h31h21        |h31|2 + |h11|2 - 1 /2

(Adh e0) = -3  i [ h11h21 h11h31 ]T .

                                       52
The definition of the inner-product ~, as given in (5.4), can then be directly applied to

calculate that

~ Adh e0, Adh e0    = 3 1       9|h11|4 - 6|h11|2 + 1          + 18 3 |h11h21|2 + |h11h31|2
                          2

                       + 9 2       |h21|4     +  |h31|4  -  1  |h11|4  +  2  |h21h31|2  +  |h11|2  -  1  .
                                                            2                                         2

But integrals over SU(3) of complex polynomials in the variables h11, h21 and h31 are
computed in appendix A.1 of [Ba]. Repeated usage of those results yields that

     ~ Adh e0, Adh e0           vol g~  =     6  1 + 3 2 + 4 3            Vol(K, g~)
                                              8
hK

                                        =     1  Tr(e0 e0)     1 + 3 2 + 4 3  Vol(K, g~) .
                                              8

Since integrating with the variables h or h-1 is the same for a bi-invariant volume form

such as vol g~, it follows from identity (5.14) and the comments thereafter that

     g~(uR, vR) vol g~          =  1    1 + 3 2 + 4 3          Tr(u v) Vol(K, g~) ,                   (5.17)
                                   8
hK

for general matrices u, v in su(3). This is the analog of (2.30) for the stretched metric g~

and reduces to that formula when 1 = 2 = 3 =: .

    Having adapted formula (2.30) to the new metric g~, the rest of the derivation of the
four-dimensional Yang-Mills terms induced by the higher-dimensional curvature RP is
entirely analogous to the work done in section 2. The generalization of the main integral

(3.15) is just

   |F |2 vol g~  =  1  gM�  gM  g~(ej, ek) (FAj L )� (FAkL )
                    4                + ~ Tr(ej ek) (FAj R )� (FAkR )
K

                                                                              Vol(K, g~) , (5.18)

where we have simplified the notation by defining the positive constant

                                ~ :=    1     1 + 3 2 + 4 3    .                                      (5.19)
                                        8

Just as in section 2, in the case where the one-forms AL have values in the electroweak

subalgebra u(2) of su(3), then the coefficient g~(ej, ek) in front of the curvature compo-
nents FAL are equal to ~(ej, ek), since the metric g~ coincides with ~ on that subspace.

So for the restricted gauge algebra u(2)  su(3), the expression for the norm of F is

   |F |2 vol g~  =  1  gM�  gM     4
                    4
K                                    ~(ej, ek) (FAj L )� (FAkL )

                                j,k=1

                                           8

                                + ~            Tr(ej ek) (FAj R )� (FAkR )    Vol(K, g~) . (5.20)

                                        j,k=1

                                                 53
This is the analog of formula (3.16) for the new metric g~. The coefficients in front of

the electroweak curvature FAL, which has values in u(2), are proportional to the stretched
products ~(ej, ek). Inspecting the definition of ~ in (5.4), we recognize that the parameters

1 and 2 play the expected role in the Yang-Mills Lagrangian: they are inversely propor-
tional to the squares of the coupling constants g and g of electroweak theory [Ham, Wei2].
The strong coupling constant, on its turn, is related to the combination ~ given by (5.19).

The precise relations between the gauge coupling constants and the parameters j are

calculated in section 2 of [Ba]. The result is

g                                                             
                           3                                  23
   =                                               e=                   (5.21)
2                          1                          1 + 32

g  =                    1                       gs =  2 2            .

2                       2                       2     1 + 3 2 + 4 3

Scalar curvature of g~

Section 2.6 was dedicated to the calculation of the scalar curvature of the left-invariant
metric g. It used the general formula (2.22) applied to the g-orthonormal basis con-
structed in section 2.5. Since the calculation is long, most of the explicit work was omitted
in that section and only the main results were recorded.

    The scalar curvature of the new metric g~ can be calculated in an entirely similar
fashion, using (2.22) and the g~-orthonormal basis of su(3) constructed before (5.12).
The explicit calculation, however, is even longer than that of section 2.6, so it will not be

carried out here. The final formula for Rg~ must generalize (2.40) and, at the same time,
reduce to the scalar curvature of ~ in the case of vanishing . The latter scalar curvature
is much quicker to compute, because the usual ~-orthonormal basis of su(3) is simpler to

manipulate when applied to the general formula (2.22). Using such a basis, we get that

                           R~ = 3  1  +         4  -  1 + 2     .       (5.22)
                                   2            3       2 32

Not having a simple and explicit formula for the scalar curvature of g~ is particularly
unfortunate in light of the discussion of section 5.1. Such a formula could be plugged

into the normalized functional (5.1), together with the volume (5.12), and be used to test
whether the parameters ||2 and 1, 2, 3 can be chosen to define a critical point of that
functional, as this would correspond to a metric in the family g~ with a chance of satisfying
the Einstein condition. In fact, finding a stable Einstein metric on K with isometry group

U(1) � SU(3) would probably be the most desirable development among all the additional

investigations suggested here. It is known that the bi-invariant metric on SU(3) is only a

saddle point of the normalized Einstein-Hilbert functional, not a maximum [Jen]. We also

                                      54
know from (2.40) that the scalar curvature explodes to minus infinity near the boundary
of parameter space defined by a finite value of ||. So the existence of a genuine maximum
of the normalized Einstein-Hilbert functional at a left-invariant metric with small || does
not sound entirely impossible.

The fibre's second fundamental form

In the discussion of section 3, the covariant derivative dA of the Higgs-like parameter
appeared in the calculation of the second fundamental form of the fibres, denoted there
as S. It was the norm |S|2 that gave rise to the term |dA|2 in the four-dimensional
Lagrangian density. Subsequently, in section 4, the classical masses of the Higgs-like and
gauge bosons were calculated from the equations of motion determined by that same
Lagrangian.

    Thus, at this point the natural task is to replicate the calculations of |S|2 and the
simpler |N |2 using the new fibre metric g~, instead of the old g. Unfortunately, once
again the explicit calculation of |S|2 is straightforward but lengthy, more so now than
in section 3, and hence will not be carried out here. Once performed, these calculations
will yield a Lagrangian density analogous (3.41) with explicit expressions for coefficient
functions C~ and D~ in terms of the parameters of the metric g~, i.e. in terms of ||2
and the positive constants 1, 2 and 3. With these expressions at hand, the customary
arguments described in sections 4.1 and 4.2 can be employed to calculate the classical
masses of the Higgs-like and the Z and W bosons, as determined by the new Lagrangian
density. The mass calculation also requires the explicit coefficients of the Yang-Mills terms
associated to g~, but these have already been computed in (5.20).

    Although we do not offer here the generalized expressions for the bosons masses, there
is one instance where the calculations are shorter and can be readily performed. This is
the calculation of the mass ratio of the Z and W bosons. In fact, improving the classical
ratio MZ = 2MW obtained for the fibre metric g was one of the motivations to introduce
and study the new metrics g~. Going through the calculations done back in section 4.2,
we recognize that the linearized equations of motion for the components of the one-form
AL is generalized from (4.6) to the new expression

~(ek, ej) gM� gM  (FAkL)� - C~0 gM� (ALk )� Tr [ej, 0] [ek, 0] = 0 ,  (5.23)

where C~0 is a function of |0|2 and the constants j that we do not calculate here,
as explained. We have also used identity (4.9) to write the quadratic form in a more

su(3)-like appearance. Therefore, picking a basis {ek} of the subspace u(2)  su(3) that
simultaneously diagonalizes the product ~ and the quadratic form Tr [ej, 0] [ek, 0] ,

                                     55
the equations of motion imply that the mass of the gauge bosons is given by

Mass (ALk )� 2 =  C~0 Tr [ek, 0] [ek, 0]  ,                                  (5.24)
                           ~ ek, ek

where no sum over the index k is intended. One such basis is explicitly constructed
in appendix A.1. It comprises the four ~-orthogonal vectors {, z~, w1, w2}. If the
components of the one-form AL on that basis are denoted by

AL = A  + Z z~ + W 1 w1 + W 2 w2 ,

then the classical mass associated to each component field follows directly from (5.24).
Although we do not have an explicit expression for C~0, this factor cancels out in the ratio
MZ/MW . Thus, using algebraic identities (A.6) and (A.9) to calculate the remaining
factors of (5.24) in the case of the wa-components, for a = 1, 2, and using identities
(A.12) and (A.12) to calculate the same factors in the case of the z~-components, we
finally obtain that mass ratio of the Z and W bosons is simply

MZ =              1 + 3 1-1 2 .                                              (5.25)
MW

So the introduction of the positive parameters j in the definition of ~ and g~ allows for

adjusting the mass ratio, as happens in the Standard Model. The parameters 1 and 2 of

g~ are of course essentially equivalent to the usual electroweak gauge coupling constants.

Full SU(3) � SU(3) gauge fields

Additional bosons and their masses

One point where the calculations in this study have not gone far enough is in investigating
the consequences of having gauge fields AL and AR with values in the natural Lie algebra
su(3)  su(3), instead of the Standard Model algebra u(2)  su(3). Recall that the higher-
dimensional metric gP was defined in (3.2) using an horizontal distribution H. This
distribution was made more explicit in formula (3.3), which defines the basic horizontal
vector fields XH on P in terms of one-forms AL and AR on the four-dimensional M4. In
principle, those one-forms can have values in the full space of left or right-invariant vector
fields on K, each identifiable with the algebra su(3). However, in order to reproduce
the usual features of the Standard Model, in many of the calculations we considered the
special case where AR has values in su(3) but AL has values in the subspace u(2) of
su(3). This was done, for example, when calculating the expression for the fibres' second
fundamental form, whose norm |S|2 produced a term |dAL|2 similar to the norm of the
covariant derivative of the traditional Standard Model's Higgs field.

                                                       56
    The main step that used the restriction to u(2) was taken after (3.20). Had we kept
one-forms AL with values in the full su(3), then formula (3.21) would be substituted by
the slightly more involved expression

2 gP ( SuLvL, X) = - (LX g)(u, v) - ALk (X) (LeLk g)(u.v)                        (5.26)

                 = -  [u, v] + [v, u], d(X) - g v, [ AL(X), u ]

                                          - g u, [ AL(X), v ] - (LX log ) g(u, v) ,

valid for any u, v in su(3) and any tangent vector X in T M  T P . This formula does

not display the covariant derivative of the traditional Higgs field , as happens with

(3.21) combined with (3.24), but it still determines the tensor S. Using the definition of

the product g and the orthonormal basis of section 2, one can use the formula above to
calculate the norm |S|2 by methods similar to those employed in section 3. The calculation

seems to be straightforward but considerably longer than that of section 3, now that AL
has values in su(3) rather than u(2). In particular, we will not be able to offer here a
formula for |S|2 as explicit as (3.25). This is unfortunate, because it prevents the direct

calculation of the masses of all the gauge bosons associated to an su(3)-valued one-form

AL.

For now, we register a geometrically natural, though hardly explicit, formula for the

norm of the fibres' second fundamental form. Denote by � , � the inner-product on the
space of symmetric 2-tensors Sym2[su(3)] induced by the product g on su(3). It can be
defined explicitly as

                 h1, h2g :=               h1(ej, ek) h2(ej, ek) ,

                                    j, k

where {ek} is any g-orthonormal basis of su(3). Then formula (5.26) implies the general
decomposition

|S|2  =  1  gM�  LX� g, LX g  +  1  gM�   AkL(X�)  LekL g, LX g
         4                       2

                                 +  1  gM�    ALk (X�)  AjL(X )  LekL g, LeLj g  . (5.27)
                                    4

This expression shows how the fibres' second fundamental form, after fibre-integration,
gives rise to the quadratic terms in the gauge fields AkL that are essential to mass gen-
eration, through spontaneous symmetry breaking, in the four-dimensional Lagrangian.
Quite naturally, the coefficients of these terms are determined by the Lie derivatives of
the fibres' metric along different directions. So the components of AL along Killing vec-
tor fields satisfying LvLg = 0 disappear entirely from |S|2 and correspond to massless
bosons. The classical mass of a gauge boson is a measure of how much the internal metric

                                          57
changes along the flow generated by the corresponding invariant vector field. Formula
(5.27) remains valid when the fibres of the higher-dimensional spacetime P are equipped
with arbitrary left-invariant metrics gK, not necessarily in the family g.

    Notice from (5.26) how the natural objects

(dAgK )(X) := LX gK + ALk (X) (LeLk gK )  (5.28)

are essentially equivalent to the second fundamental form of the fibres. They can be

regarded as the "covariant derivative" of the left-invariant fibre metric gK along a vector
field X in M4. The fibres of P are totally geodesic if and only if their metrics gK are
"covariantly constant" along M4, in the sense that (5.28) vanishes for all vectors X. The
gauge fields AR do not appear in (5.28) because the Lie derivatives LvR gK are identically
zero for left-invariant fibre metrics.

    Observe also that, for arbitrary left-invariant metrics on K, the fibres' mean curva-
ture vector N continues to be independent from the one-forms AL, even for gauge fields
with values in the larger algebra su(3). This is manifest in formula (3.34), for instance,
which was deduced using the unimodularity of K. Thus, the terms in the Lagrangian
proportional to |N |2 and N still do not involve gauge fields.

    Let us now come back to the discussion of the full su(3)-gauge bosons. In section 4.2
we calculated the masses of the components of AL with values in the subspace u(2) of
su(3). These components correspond to the four electroweak gauge bosons. A one-form
AL with values in the full su(3) would imply the existence of four additional bosons. All
of these would be massive in the present model, since   u(2) generates the only left-
invariant Killing field of g, up to normalization. The classical mass of the additional
bosons should be computable using an orthonormal basis applied to (5.26) and (5.27), as
was done in section 3 for the Z and W bosons, although the calculation will be longer
in this case. It would be very interesting to carry it out explicitly; check how the usual
arguments about the unitary gauge can fit in; and investigate the conditions necessary for
the additional four bosons to be significantly heavier than their electroweak counterparts.

    If no significant obstacles are found in the calculation of the masses of the four addi-
tional bosons but, at the end, they turn out not to be heavier than the Z and W bosons,
this would of course be bad news for the present model, as no additional gauge bosons
have been experimentally observed at low energies. One way out would be the usual
route of adjusting the model by introducing a mechanism to spontaneously break the left
SU(3) down to U(2), and therefore make the new bosons heavier. This could be achieved
using a Higgs-like field  : M4  su(3) in the adjoint representation, which can also be
regarded as a simple left-invariant vector field on P , and adding the norm of its covariant
derivative and a new potential U () to the higher-dimensional Lagrangian density. For

58
example, take the AdSU(3)-invariant potential

                                        Tr() - 6              2              (5.29)
              U () :=
                                   4

with positive constants  and  . It is clear that this potential has absolute minima when


the matrix  is in the conjugation class of 0 =  diag(-2i, i, i) inside su(3). The

"vacuum vector" 0 is preserved by the usual subgroup U(2) of SU(3), so the poten-

tial U () would provide the necessary mechanism to make the additional four bosons

heavier without affecting the masses of the Z and W bosons calculated before. How-

ever, after spending considerable effort trying to obtain the all the bosonic components

of the Standard Model Lagrangian from natural objects such as the higher-dimensional

scalar curvature, and therefore suggesting a more geometrical origin for the usual Higgs

covariant derivative and potential, the introduction in the model of new ad hoc fields and

potentials, such as those in (5.29), would not be the most favoured option.

Additional fermionic interactions

The model for fermions described in [Ba] associates them to spinorial functions on the

spacetime P having a prescribed behaviour along the internal space K. This behaviour

determines the Lie derivatives of the functions along vertical vector fields, which in turn de-

termine the fermionic gauge representations obtained in the four-dimensional Lagrangian,

after integration of the Dirac kinetic terms along the fibres. Using the explicit vertical

behaviour suggested in sections 2.2 and 2.3 of [Ba], it is possible to calculate how the

four-dimensional fermions would couple to gauge fields AL with values in the full algebra
su(3). In fact, the necessary work is already done in the aforementioned section 2.3. It

can be summarized by the formulae

A  := d +     ALj eLj (+) Lej (-) + ARj Rej (+) eRj (-) ,                    (5.30)
                                                                             (5.31)
           j

with the coupling to the AL gauge fields determined by

                    a cT                            0            -2 v11 cT
Lv (�) = Lv b D =
                                               2 v11 I3 + v b v D

for all matrices v in su(3). Here a is a single Weyl spinor; b and c are 3-vectors of

Weyl spinors; D is a 3 � 3 matrix of Weyl spinors. They can be identified with the first

generation of fermions according to the rule

                                       R urR uRg ubR 

              a cT                      e-R    dRr  dRg  dRb  
              bD                                              

                                   =                             .           (5.32)

                                               urL  ugL  ubL  
                                       L                      


                                        e-L drL dgL dbL

                                        59
For matrices v with values in the subalgebra (u(2)) of su(3), the transformation (5.31)

gives the usual fermionic couplings to the electroweak gauge group, with the correct

hypercharges and weak isospin. If AL is taken to have values in the full su(3), the same
formula (5.31) suggests what the additional fermionic couplings should be like. The

components of AL with values in the subspace (C2) of su(3) are associated to matrices v

of the form

                          -y   su(3) ,  (5.33)
             v=

                      y

with y  C2. Since the entry v11 is zero, the new components of AL do not couple to
the vector c of (5.31), that is, to the right-handed up quark. However, the matrix v
does act on the vector b and on the columns of the matrix D by mixing their top entries
with the middle and bottom ones. In other words, the new components of AL would mix
the right-handed electron with the left-handed electron and neutrino. They would also
mix the right-handed down quark with the left-handed up and down quarks. The mixing
would be analogous for anti-particles. Thus, the higher-dimensional model described in
[Ba] suggests that the interactions generated by the additional components of AL would
conserve the baryon number but not parity.

    It is also appropriate to recall from [Ba] that once the gauge algebra is extended from
the Standard Model's u(2)su(3) to the larger su(3)su(3), the action on spinors L +R,
described in section 2.3 of that study, no longer defines a Lie algebra homomorphism from
the gauge algebra to the algebra su(12) of transformations in spinor space. It would be
interesting to better understand the implications of this fact.

             60
A Appendices

A.1 A -rotated basis of su(3)

Given a non-zero vector  = [1 2]T in C2, consider the orthogonal vector defined by
~ := �2 - �1 T . It satisfies

              ~ = ~ = 0                                                            (A.1)

               + ~~ = ||2 I2 ,

where  denotes the hermitian conjugate and I2 is the identity matrix. Define the -
oriented Pauli matrices by

              1 := ||-2 (~ + ~)                                                    (A.2)
              2 := i||-2 (~ - ~)
              3 := ||-2 (~~ - ) .

These are traceless hermitian matrices that satisfy the usual algebraic relations

              a b = ab I2 + iabc c                                                 (A.3)

and coincide with the Pauli matrices when  = [0 1]T . They can be regarded as a rotated
version of the latter matrices.

    The matrices j can be used to write down a basis of su(3) that simultaneously
diagonalizes the Ad-invariant inner-product and the quadratic form

              (u, v)  Tr u, ()  v, ()                                              (A.4)

on the Lie algebra. Such a basis is useful in the calculation of the mass of the Z and W
gauge bosons worked out in section 3. Fix the vector   C2 and recall the usual vector
space isomorphism  : u(2)  C2  su(3). We can define four different 3 � 3-matrices in
the subalgebra (u(2)) of su(3) through the formulae

w1 := ( i1 )                   z   :=  1  ( iI2  -   i3 )                          (A.5)
w2 := ( i2 )                           2

                                :=     1   i     I2  +         .
                                             3          i 3 3

                                       2

One can readily check that these matrices are orthogonal to each other with respect to
the Ad-invariant inner-product on su(3), so they span the subspace (u(2)). Their norm
in su(3) is simply

Tr( ) = Tr(z z) = Tr (wa) wa = 2 .                                                 (A.6)

                               61
The commutators in su(3) of these four matrices are

                 [z, ] = 0                                             (A.7)


                 w1, w2 = z - 3 

                 w1,  = 3 w2 = 3 z, w1

                 w2,  = - 3 w1 = 3 z, w2 .

The commutators of these matrices with the element () in su(3) can be checked to be

                 , () = 0                            z, () = 2 ( i )   (A.8)
                 w1, () = ( i~ )                     w2, () = ( ~ ) .

The latter commutators are vectors in the subspace (C2) of su(3). They are orthogonal
to each other and to () with respect to the Ad-invariant inner-product on su(3). So
the three non-zero commutators together with () span the whole subspace (C2). The
norm in su(3) of , () is zero, whereas the other commutators have norm

                 Tr z, ()  z, () = 8 ||2                               (A.9)

                 Tr wa, ()  wa, () = 2 ||2 .

It is clear from (A.8) that {, z, w1, w2} is a basis of (u(2)) that diagonalizes the
quadratic form (A.4) on that subspace of su(3). Moreover, we have the relations

(), () = 0                              (i), () = ||2 (i3) - (iI2)
(~), () = -i ||2 2
                                        (i~), () = -i ||2 1 .          (A.10)

All these commutators are orthogonal to each other with respect to the Ad-invariant
product on su(3). So we recognize that the vectors (), (i), (~) and (i~) form a basis
of (C2) that simultaneously diagonalizes the Ad�invariant product and the quadratic form
(A.4) on that subspace of su(3). Since the subspaces (u(2)) and (C2) are orthogonal

to each other with respect both to the Ad-invariant product and the quadratic form, we
conclude that {, z, w1, w2, (), (i), (~), (i~)} is a basis of su(3) with the desired
properties.

    Section 5.2 describes an inner-product ~ on su(3) that is not fully AdSU(3)-invariant,

only AdU(2)-invariant. We will now describe a basis of su(3) that simultaneously diago-
nalizes the product ~ and the quadratic form (A.4). In fact, this basis can be taken to

coincide with the preceding one, except that the vector z should now be substituted by

the deformation                   1

                 z~  :=               iI2 - 12-1 i3  ,                 (A.11)
                                  2

                                        62
where the positive constants 1 and 2 are those in the definition (5.4) of the product

~. The new vector z~ is orthogonal to , w1 and w2 with respect to the product ~. Its

norm is                                 1   3 + 1
                                        2        2
         ~(z~, z~)                   =                    .                     (A.12)

The commutators in (A.7) involving z are now changed to

         [z~, ] = 0                  [z~, w1] = 1 2-1 w2                        (A.13)
         [z~, w2] = -1 2-1 w1
                                     [w1, w2]  =        4                    .
                                                   3 + 1 -2 1  z~ - 3 

Since the commutator with () is now

                           1            3 + 1 2-1   (i) ,
         [ z~, () ] = 2

the quadratic form (A.4) applied to z~ has the new value

         Tr z~, ()  z~, ()                      1  3 + 1 -2 1 2 ||2 .           (A.14)
                                            =

                                                2

The new formulae involving z~ reduce to the old ones when 1 = 2, of course.

A.2 A proof about the Killing fields of g

In the context of section 2.4, the aim of this discussion is to show that if a left-invariant
vector field uL is Killing for the metric g on SU(3), then the vector u is necessarily in
the subalgebra u(2) of su(3). By formula (2.31), the condition that uL is Killing for g is
equivalent to the condition that

          [v, v], [u, ] +  [[v, u], v] + [[u, v], v],  = 0

for all vectors v in su(3). In particular, choosing v in the subspace (C2) of su(3), which
implies v = 0, we must have that

          [[u, v], v],  =  u, [v, [v, ]] = 0                                    (A.15)

for all vectors v in (C2). From now on, we shall think of u, v and  as complex vectors
in C2 and explicitly write the map  : C2  su(3) whenever it is necessary to regard them
as matrices in su(3). Then a short calculation using matrices of the form (2.24) leads to
the general identity in (C2)

         (v), (v), () =  2 v - v v - |v|2                                       (A.16)

                               =  v,  v + 3 v, i iv - v, v  ,

                                        63
where the brackets on the left-hand side are commutators of matrices in su(3) and �, �
is the canonical real product on C2. The Ad-invariant product  is proportional to the
product 0 written down in (2.4). Thus, following that formula, we recognize that  can
be identified with �, �, up to normalization, when restricted to vectors in the subspace
(C2). This means that condition (A.15) applied to the vector coming from (A.16) is
equivalent to the equation

v,  u, v + 3 v, i u, iv - v, v u,  = 0  (A.17)

for all vectors v  C2. Choosing a non-zero v orthogonal both to  and i in C2, the first
two terms of the equation vanish and the condition reduces to u,  = 0. Thus, any
Killing field uL must have u orthogonal to  in C2. Assume that this is true and now
choose v = 1 + 2i with real constants a. Substituting this vector v into equation
(A.17) yields the condition

4 1 2 ,  u, i = 0 .                     (A.18)

This is satisfied for all scalars a only if u is orthogonal also to i, besides being orthog-
onal to . Assume that this is true and choose v = 1 + 2~, where the new vector
~  C2, defined before (A.1), is orthogonal both to  and i. Substituting this vector v

into equation (A.17) yields the condition

1 2 ,  u, ~ = 0                         (A.19)

for all a. So a Killing field uL will have u orthogonal to the span of {, i, ~}. Finally,
assuming that u satisfies this, choose v = 1 + 2i~ and substitute it into equation
(A.17). Since i~ is also orthogonal to  and i, this yields the last condition

1 2 ,  u, i~ = 0 ,                      (A.20)

which shows that u must also be orthogonal i~. Since the vectors {, i, ~, i~} span
the whole C2, we conclude that u must in fact be zero, and hence u must belong to the
subspace u(2) of su(3). The main discussion in section 2.4 then goes on to show that u
must be proportional to the matrix  defined in (A.5).

A.3 Weyl rescaling of gP

Let  : (P, gP )  (M, gM ) be a Riemannian submersion with fibre K. Denote by n, m
and k the real dimensions of these manifolds, so that n = m + k. Let M : M  R+ be
any positive function on the base and let  :=  M be the corresponding lift to P as

                                                       64
a function constant along the fibres. The Weyl rescalings of the metrics gP and gM are

defined by

                          g~P := 2 gP                   g~M := 2M gM .

Then the projection  : (P, g~P )  (M, g~M ) is still a Riemannian submersion. The volume
forms on P , K and M transform according to

    volg~P = n volg             volg~K = k volgK           volg~M = M m volgM .            (A.21)

A well-known formula for the transformation of the scalar curvature under a rescaling of
the metric says that [Wald]

    Rg~P = -2 RgP - 2(n - 1) gP (log ) - (n - 1)(n - 2) |d log |g2P ,                      (A.22)

where gP denotes the scalar Laplacian on P defined by the metric gP . Moreover, from
the general formula (3.34) it can be deduced that the mean curvature vector of the fibres

transforms as

                             N~ = -2 N - k gradgP (log ) ,                                 (A.23)

which is also as well-known formula. It implies that the norm of N transforms as

               |N~ |g2~P  =  2 |N~ |g2P  =  -2  N   -k  gradgP (log )  2                   (A.24)
                                                                       gP

                          = -2 |N |g2P + k2 |d log |2gP - 2 k (d log )(N ) .

To compute the transformation rule of N , start by recalling expression (3.39) with all

the pull-backs  explicitly written

                                gN = - [ divgM (N ) ] .                                    (A.25)

The right-hand side depends on the metric both through N and through the divergence
operator. For a fixed vector field X in M4, it follows from the general relation LXvolg =
(divg X)volg and the rescaling rule for volume forms that the divergence of X transforms
under Weyl rescalings as

                             divg~M X = divgM X + m (d log M )(X) .                        (A.26)

At the same time, it follows directly from (A.23) that the push-forward N transforms

as

                              N~ = M -2 N - k gradgM (log M ) .                            (A.27)

Combining (A.26) and (A.27), a short calculation then shows that

    divg~M (N~ ) = M -2 divgM (N ) - k gM (log M )

                             +  (m - 2)(d log M )(N )   +  k(2 - m)        d log M  2   .  (A.28)
                                                                                    gM

                                                65
This is a function on the base M and, according to (A.25), we only have to pull it back
to P to obtain the desired formula for g~M N~ . Since  is a Riemannian submersion and
 =  M , it is clear that the last two terms pull-back very simply:

                          (d log M )(N ) = (d log )(N )                               (A.29)
                                   |d log M |2gM = |d log |g2P .

In addition, a formula obtained in [Be] says that the Laplacians in a Riemannian submer-
sion are related by

gP (log ) =  gM (log M ) + gK (log ) - (d log )(N )                                   (A.30)
               =  gM (log M ) - (d log )(N ) ,

where the last equality uses that  is constant on the fibres K. Combining these formulae
with definition (A.25), we finally conclude that

g~P N~ = -2  gP N  +  k  gP (log  )-  (m-3)(d log   )(N )  +  k  (m-2)  d  log    2   . (A.31)
                                                                                  gP

Taking the preceding formulae for Rg~P , |N~ |2g~P and g~P N~ , which all contain the same basic
components, one can look for real constants 1 and 2 such that

Rg~P + 1 |N~ |2g~P + 2 g~P N~ = -2 RgP + 1 |N |2gP + 2 gP N                           (A.32)

for every rescaling function . This defines a system of linear equations for 1 and 2
that has a solution for

                   n-1            n-2                             n-1                 (A.33)
             1 = k           2-                        2 = 2 k .
                                      k

Therefore the function on P

                             n-1         n-2           2        n-1     gP N
             WgP := RgP + k              2-         N  gP  +  2                       (A.34)
                                                 k
                                                                  k

transforms simply as Wg~P = -2 WgP under a rescaling of the submersion metric gP .

                                         66
References

[AY] K. Abe and I. Yokota: Volumes of compact symmetric spaces, Tokyo J. Math. 20
          (1997), 87�105.

[BL] D. Bailin and A. Love: Kaluza-Klein theories, Rep. Prog. Phys. 50 (1987), 1087�
          1170.

[Ba] J. Baptista: Higher-dimensional routes to the Standard Model fermions,
          arXiv:2105.02901 [hep-th].

[Bes] A. Besse: Einstein manifolds, Classics in Mathematics, Springer-Verlag, 1987.

[Be] G. Besson: A Kato type inequality for Riemannian submersions with totally
          geodesic fibers, Ann. Glob. Anal. Geom. 4 (1986), 273�289.

[Ble] D. Bleecker: Gauge theory and variational principles, Addison-Wesley, 1981.

[BD] T. Brocker and T. Dieck: Representations of compact Lie groups, Graduate texts
          in Mathematics, Springer-Verlag, 1985.

[CJ] R. Coquereaux and J. Jadczyk: Geometry of multidimensional universes, Com-
          mun. Math. Phys. 90 (1983), 79�100.

[DNP] M. Duff, B. Nilsson and C. Pope: Kaluza-Klein supergravity, Physics reports 130
          (1986), 1�142.

[EBH] F. Englert and R. Brout: Phys. Rev. Lett. 13 (1964), 321.
          G. Guralnik, C. Hagen and T. Kibble: Phys. Rev. Lett. 13 (1964), 585.
          P. Higgs: Phys. Lett. 12 (1964), 132.

[Ham] M. Hamilton: Mathematical gauge theory: with applications to the Standard Model
          of particle physics, Universitext, Springer International Publishing, 2017.

[Her] R. Hermann: A sufficient condition that a mapping of Riemannian manifolds be
          a fibre bundle, Proc. Amer. Math. Soc. 11 (1960), 236�242.

[Ho] P. Hogan: Kaluza-Klein theory derived from a Riemannian submersion, J. Math.
          Phys. 25 (1984), 2031�2035.

[Jen] G. Jensen: The scalar curvature of left-invariant Riemannian metrics, Indiana U.
          Math. J. 20 (1971), 1125�1144.

                                                       67
[K] T. Kaluza: Sitzungsber. Preuss. Akad. Wiss. Berlin Math. Phys. K1 (1921), 966.
          O. Klein: Z. Phys. 37 (1926), 895.
          B. DeWitt: Lectures at 1963 Les Houches School, Gordon and Breach, 1964.
          R. Kerner: Ann. Inst. H. Poincar�e 9 (1968), 143.
          A. Trautman: Rep. Math. Phys. 1 (1970), 29.
          Y. Cho: J. Math. Phys. 16 (1975), 2029.
          Y. Cho and P. Freund: Phys. Rev. D12 (1975) 1711.
          J. Scherk and J. Schwarz: Phys. Lett. 57B (1975), 463.
          E. Cremmer and J. Scherk: Nucl. Phys. B108 (1976), 409.

[Mil] J. Milnor: Curvature of left invariant metrics on Lie groups, Adv. Math. 21 (1976),
          293�329.

[O'Ne] B. O'Neill: The fundamental equations of a submersion, Michigan Math. J. 13
          (1966), 459�469.

[OW] J. Overduin and P. Wesson: Kaluza-Klein gravity, Physics reports 283 (1997),
          303�380.

[MS] N. Manton and P. Sutcliffe: Topological Solitons, Cambridge Univ. Press, 2004.
[Wald] R. Wald: General relativity, Chicago Univ. Press, 1984.
[Wei] S. Weinberg: A model of leptons, Phys. Rev. Letters 19 (1967), 1264�1266.
[Wei2] S. Weinberg: The quantum theory of fields, vol. 2, Cambridge Univ. Press, 1996.
[Wi1] E. Witten: Search for a realistic Kaluza-Klein theory, Nucl. Phys. B 186 (1981),

          412�428.
[Wi2] E. Witten: Fermion quantum numbers in Kaluza-Klein theory, in Shelter Island

          II, Proceeding of the 1983 Shelter Island conference, MIT Press, 1985, 227�277.

                                                       68
