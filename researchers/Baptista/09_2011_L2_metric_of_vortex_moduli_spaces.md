# 2011 L2 metric of vortex moduli spaces

**Source:** `09_2011_L2_metric_of_vortex_moduli_spaces.pdf`

---

arXiv:1003.1296v3 [hep-th] 11 Apr 2010                                                                                                   ITFA-2010-09

                                          On the L2-metric of vortex moduli spaces

                                                                             J. M. Baptista 

                                                                           Institute for Theoretical Physics 
                                                                                 University of Amsterdam

                                                                                March 2010

                                                                                 Abstract

                                            We derive general expressions for the Ka�hler form of the L2-metric in terms of standard
                                        2-forms on vortex moduli spaces. In the case of abelian vortices in gauged linear sigma-
                                        models, this allows us to compute explicitly the Ka�hler class of the L2-metric. As an
                                        application we compute the total volume of the moduli space of abelian semi-local vortices.
                                        In the strong coupling limit, this then leads to conjectural formulae for the volume of the
                                        space of holomorphic maps from a compact Riemann surface to projective space. Finally
                                        we show that the localization results of Samols in the abelian Higgs model extend to
                                        more general models. These include linear non-abelian vortices and vortices in gauged
                                        toric sigma-models.

                                            e-mail address: [email redacted]
                                            address: Valckenierstraat 65, 1018 XE Amsterdam, The Netherlands
Contents

1 Introduction                                                         1

2 The vortex K�ahler form                                              4

3 Simplication for linear targets                                      8

4 The vortex K�ahler class in abelian linear models                    11

5 Application: volume of simple moduli spaces                          16

6 Samols' localization for vortex metrics                              22

7 Examples of localization                                             25

8 Appendix                                                             31

1 Introduction

Vortices are the natural solitons of gauged sigma-models at critical coupling. Within each
topological sector they minimize the Yang-Mills-Higgs energy functional

            E(A, ) =           1    |FA|2  +  |dA|2  +  2 e2 |�  |2 .  (1)
                              2 e2


To construct this functional and define the model we need two Ka�hler manifolds  and
X, and a hamiltonian action of a Lie group G on X. The fields of the theory are then a
connection A on a principal G-bundle P   and a section  of the associated bundle
P �G X  . This section  can be locally regarded as a map   X, so one can
compose it with the moment map � : X  Lie G and take the squared norm using an
Ad-invariant inner product on the Lie algebra. The resulting function |�  |2 is then used
as the potential at critical coupling in the energy (1). The remaining two terms in the
functional are the usual Maxwell term � the squared norm of the curvature of A � and a
standard covariant derivative term.

    The well-known Bogomolny argument can be used to show that the energy (1) is

                                           1
minimized by the field configurations (A, ) that satisfy

�A = 0                                                                           (2)

FA + 2e2 �   = 0
FA0,2 = 0 ,

which are usually called the vortex equations. Here the symbol FA represents the inner
product , FA of the curvature with the Ka�hler form of . In the special and important
case when  is a Riemann surface, the last equation is trivially satisfied and the vortex
equations reduce to

�A = 0                                                                           (3)

 FA + 2e2 �   = 0 ,

where  is the Hodge star operator on . This general version of the vortex equations
was first found in [25, 11] and extends to arbitrary hamiltonian targets X the previ-
ously known versions of the equations, which had been written mostly for linear targets
acted upon by linear G-representations. For example the classical abelian Higgs model
corresponds to the choices G = U(1) and X = C. These general vortex equations can
be used to define the so-called Hamiltonian (or gauged) Gromov-Witten invariants of X
[10]. From a physics perspective, the vortex solutions in two dimensions are the BPS
configurations of a N = 2 supersymetric gauged sigma-model [4].

    When studying the vortex equations one of the main objects of interest is the moduli
space M of solutions, i.e. the set of vortex solutions quotiented by the action of the group
of G-gauge transformations. In general this is a complicated space that is very hard to
describe, but it is also a space with many interesting features. One of the most interesting
properties of M is that it possesses natural homology and cohomology classes, and so
by taking cup products and intersections one can obtain natural intersection numbers
associated to M, which is exactly how the Hamiltonian Gromov-Witten invariants are
defined [10, 3]. Another important property of M is that is possesses a natural Ka�hler
structure (see e.g. [25]), with Riemannian metric defined by

gM(A1 + 1, A2 + 2) =     1   kab               A 1a       A 2b  +  gX(1, 2) vol  (4)
                        4e2


and a compatible complex structure defined by

JM (A , ) = ( -iA dz + iA� dz�� , JX  ) ,                                        (5)

                             2
where {z} and  are, respectively, a set of complex coordinates and the Hodge operator
on . Observe that (4) in fact defines a metric in the space V of all vortex solutions (A, ),
but since the tangent space T[A,]M can be identified with the subspace of T(A,)V that is
orthogonal to gauge transformations, i.e. orthogonal to the kernel of the natural projection
T(A,)V  T[A,]M, the same expression (4) also determines a metric on M. Besides
being geometrically very natural, this L2-metric on the moduli space is also physically
important, essentially because the induced norm || (A, ) ||2Mcan be interpreted as the
kinetic energy of a dynamical vortex solution that evolves slowly with time. This fact was
firstly recognized by Manton for the case of monopoles on R3 [20], and constitutes the
basis of an approximation method that has been widely used to describe the low-energy
dynamics of various types on solitons [23].

    In the case of vortices, though, the problem of describing the metric gM has proved to
be a difficult one, essentially because no non-trivial vortex solutions are known explicitly.
This study is more developed in the simplest case of vortices with G = U(1) and X = C,
i.e. in the abelian Higgs model, where some of the most remarkable results are Samols'
formula for gM in terms of the local behaviour of ||2 near its zeros [28], the computation of
the cohomology class [M] of the vortex Ka�hler form [21, 26], and an asymptotic formula
for gM in the region of the moduli space where the vortices are well-separated [22]. In
this article we basically extend the first two results beyond the abelian Higgs model, i.e.
to vortices with different groups G and targets X. On the one hand we compute the
Ka�hler class [M] for models where G is a torus acting linearly on the target X = Cn;
on the other hand we show that Samols' localization happens whenever the complexified
GC-action is free and transitive on an open dense subset of the target X. A more detailed
description of the content of the article follows below. Other recent results on vortex
metrics include [9].

    In section 2 we write down a formula for the Ka�hler form M of the L2-metric in
terms of standard 2-forms on the moduli space, namely in terms of the curvature FA
of the universal connection and the pull-back by the evaluation map of the equivariant
Ka�hler form XG of the target X. When the target is a complex vector space this formula
simplifies considerably, and we can express M solely in terms of the curvature FA. This
simplified formula is obtained in section 3, and generalizes a formula derived by Perutz
for the abelian Higgs model [26]. In section 4 we apply the cohomological version of
this formula to the case of abelian linear sigma-models, i.e. to the case where G is a

                                                        3
torus acting with weights Qja on a vector space X = Cn. Since in this abelian case there
exists a rather explicit description of M [24, 31], this allows us to deduce an equally
explicit formula for [M], a formula that generalizes the result of Manton and Nasir for
the abelian Higgs model [21]. As an application, in section 5 we compute the total volume
and the Einstein-Hilbert action of (M, gM) in the case of abelian semi-local vortices, i.e.
in the case where G = U(1) acts by scalar multiplication on X = Cn. Taking the large
coupling limit e2  , this leads directly to conjectural formulae for the total volume and
Einstein-Hilbert action of the space of holomorphic maps   CPn-1 equipped with its
natural L2-metric. This limit is explained in section 5.2. Finally, in the last two sections of
the paper (which can be read independently) we explain how the localization phenomena
described by Samols in the abelian Higgs model extend to the more general cases where
the complexified group GC acts freely and transitively on an open dense subset Xo  X
of the target. This extension of Samols' localization is illustrated more concretely in two
different examples: the case of linear non-abelian vortices with group G=U(N) acting on
the space of complex square matrices X = MN�N ; and the case of abelian vortices where
a torus G = T k acts on a toric manifold of complex dimension k.

Note: A week before this article was completed, a paper that contains some overlap with
the material of section 7.1 in the case  = C appeared on the arXiv [16]. This reference
also addresses the question of finding the asymptotic form of gM for well-separated, linear
non-abelian vortices, an interesting subject that is not discussed here.

2 The vortex K�ahler form

2.1 Universal bundle and connection

This is essentially a preparatory section. We recall the well-known concept of universal
bundle with its universal connection A, and state the definition of the natural 2-forms FA
and evXG on the cartesian product M � .

    Let V be the space of solutions of the vortex equations and let G be the group of
gauge transformations. We assume that there exists an open subset V  V of irreducible
solutions where the gauge transformations act freely and the quotient V/G =: Msmooth
is a finite-dimensional smooth manifold. The quotient Msmooth can be regarded as the
smooth part of the moduli space M, and in some special instances � e.g. the cases treated

                                                        4
in sections 5 and 6 � it can actually be shown that Msmooth = M.
    The right-action of G on the space of vortex solutions induces a linear map from the Lie

algebra of G to the tangent spaces of V. These derivative maps correspond to infinitesimal
gauge transformations and are explicitly given by

          C(A,) : 0(; P �Ad g) - T(A,)V                         (6)

           = aea - A - ae^a ,

where {ea} is a basis of the Lie algebra g, the e^a's are the vector fields on X induced by
ea and the left G-action, and A is the covariant derivative induced by A on the adjoint
bundle P �Ad g  . The image of this map in T(A,)V corresponds to the tangent vectors
parallel to gauge transformations, or in other words to the kernel of the natural projection

T(A,)V  T[A,]M.
    Now, besides acting on the vortex solutions, the group G of gauge transformations

also acts on the total space of the principal bundle P  , so one can define the smooth

quotient

          P = (V � P ) / G .                                    (7)

This finite-dimensional space has a natural free G-action induced by the G-action on P ,
and so can be regarded as a principal bundle

          G  P - Msmooth �  .                                   (8)

It is usually called the universal (or Poincar�e) bundle. An important property of P is
that its restriction to  coincides with P , or more precisely that for any chosen point
[A, ]  Msmooth there exists an isomorphism of G-bundles

          P |[A,]�  P -  .                                      (9)

The particular isomorphism depends of course on the initial choice of [A, ].
    Another important property of P is that it comes equipped with a natural G-

connection A, sometimes called the universal connection. The curvature FA of the uni-
versal connection can be regarded locally as a 2-form on Msmooth �  with values on the
Lie algebra g. It is determined by the formulae [13, 4]

                        FA(v1, v2) |(A,,x) = FA(v1, v2) |x      (10)
                    FA(A + , v) |(A,,x) = A (v) |x
          FA(A 1 + 1, A 2 + 2) |(A,,x) = [C(A,)C(A,)]-1() |x ,

          5
where the v's are tangent vectors in Tx; the A +  are tangent vectors at (A, ) that are
orthogonal to gauge transformations, and hence represent a vector in T[A,]M; and  is
the section of the adjoint bundle P �Ad g   defined by the formula

 = - 4e2 kab (gX )ts 1r 2s (e^b)rt + 2 (g)� [(A 1), (A 2)�] ea .           (11)

Finally, a third important property of P is that it also comes equipped with a natural

G-equivariant map

                   ev : P - X , [A, , p] - (p) ,                           (12)

called the evaluation map. (Here we are regarding  as a G-equivariant map P  X,
which is the same thing as a section of P �G X  .) This evaluation map can be used
to pull-back G-equivariant differential forms

                   ev : G� (X) - �G(P)  �(Msmooth � ) ,                    (13)

where the last identification is just the usual Weil homomorphism defined by the connec-
tion A [6, 12, 4]. This pull-back by the evaluation map can in particular be applied to
the G-equivariant Ka�hler form of X

                   XG = X - a �a               2G(X)                       (14)

to obtain a standard 2-form evXG on the cartesian product Msmooth � .

2.2 The vortex K�ahler form

The aim of this short section is to write down an expression for the K�ahler form M of
the vortex metric in terms of the natural 2-forms FA and evXG described above. The
latter 2-forms are very standard in gauge theory, and their cohomology classes are used
to define the so-called Hamiltonian (or gauged) Gromov-Witten invariants. The existence
of such a formula for M shows that the Ka�hler class [M] can be expressed in terms of
these standard cohomology classes of M, and hence that, at least in principle, quantities
such as the total volume of the moduli space can be expressed in terms of Hamiltonian
Gromov-Witten invariants.

Theorem 2.1. Over the smooth region Msmooth  M of the vortex moduli space the

K�ahler form of the metric gM is given by the formula

M =                 (evXG )    m   -      1   kab FAa  FAb      m-1     ,  (15)
                               m!        4e2                  (m - 1)!


where m is the complex dimension of  and XG and FA are as in section 2.1.

                                      6
Remark. The integrand in the formula above is a 2(m+1)-form over the product M�.
Applying to it fibrewise integration over  yields a 2-form over M, as desired.

Proof. Using the definitions of XG and ev of section 2.1 we have that

            (evXG)  m = (evX )  m - (�a  ) FAa  m .                                                    (16)

Using the second vortex equation and standard Ka�hler geometry the second term above

can be written as

                   - (�a  ) FAa  m        =     1   kab     (FA)bFAa         m                         (17)
                                               2e2
                                               m
                                          =    2e2  kab  FAa       FAb    m-1       ,

where k is an Ad-invariant product on g. But looking at the different components of the

definition (10) of FA, we see that for the purpose of integration over ,

  kab FAa  FAb  m-1 =           kab (2FAa  FAb + �a  dx�  b  dx )  m-1 , (18)

where {x�} are coordinates on  and by definition (�a  dx�)(A + , v) = Aa�v�. This is

because a form over M �  contributes to the integral only if it has degree 2m on the

-side. Bringing everything together we see that the form M defined by (15) can be

written as

  M =               (evX )    m    +       1   kab �a     b    dx�       dx              m-1     .     (19)
                              m!          4e2                                          (m - 1)!


This means that, when contracted with tangent vectors (A + ) orthogonal to gauge

transformations, M satisfies

M(A1 + 1, A 2 + 2) =            X  ( 1,    2)  m         +    1    kab A a1   A 2b       m-1        .  (20)
                                               m!            4e2                       (m - 1)!


But the definition of the complex structure JM and standard manipulations in Hodge

theory of Ka�hler manifolds (see for example [30], page 150) also yield the formula

                              (JM  A )      m-1          =    A .                                      (21)
                                          (m - 1)!

This finally implies that

  M(A1 + 1, JM(A2 + 2)) =                      X  ( 1 ,  JX   2 )  m    +     1     kab  A 1a    A 2b
                                                                   m!        4e2


                                   = gM(A 1 + 1, A2 + 2) ,

and confirms that M is the Ka�hler form associated to the metric gM.

                                               7
3 Simplication for linear targets

In this section we will see how formula (15) can be further simplified when the target
X  Cn is a complex vector space and G acts through a unitary representation  : G 

U(n). With these choices the fibre bundle P �G X becomes simply a rank n complex
vector bundle V  . Moreover, if we choose the standard Ka�hler form on Cn

                           Cn      =  i          dwk  dw�k ,
                                      2
                                           k

the moment map � : Cn  g is given by the formula

                   �(w)         =  1  [iw  (d)(ea)  w  +    a] ea     ,                      (22)
                                   2

where d : g  u(n) is the derivative of the representation , and  = aea is any element
of the dual g that annihilates the subspace [g, g] of g. A first observation concerns the

cohomology class [M] in H2(M) of the Ka�hler form.

Proposition 3.1. Over the smooth region Msmooth of the moduli space the cohomology
class of the K�ahler form is

[M]  =  -     a    [FAa ]       [m]   +          1  1)!  [  kab  FAa     FAb  ]    [m-1]  .  (23)
             2 m!                          4e2(m -


Proof. We have only to recall that when X is a vector space acted by a linear repre-

sentation, deformation invariance implies that two closed G-equivariant forms are coho-
mologous in HG� (X) if and only if they coincide at the origin of the vector space (see for
example [18]). This shows that in HG2 (Cn) :

           [XG]G = [Cn - ea  �a(w)]G = [-ea  a/2]G .                                         (24)

This is a great simplification, for then we have that

             ev[XG]G = ev[-ea  a/2]G = -[FAa ] a/2                                           (25)

in H2(Msmooth � ), as desired.

    Imposing an additional condition on the representation , it is a remarkable fact
that formula (23) holds also for the differential forms themselves. This has already been
recognized in the literature in several instances.

                                              8
Proposition 3.2. Assume that the derivative d : g  u(n) of the representation  is
such that

(i) the matrix i1n�n belongs to the image d(g) ;

(ii) the inner products on the Lie algebras are preserved up to rescaling.

Then over the smooth part of the moduli space

M  =  -      a               FAa    m  +        1  1)!  kab  FAa   FAb    m-1  .  (26)
            2 m!                          4e2(m -


Remark. This formula was first obtained by Perutz [26] in the case of G = U(1) acting
by multiplication on X = C and m = 1. A similar formula was found by Biswas and
Schumacher in [8] for G = U(n) and the moduli space of solutions of the coupled vortex
equations. Our proof is an extension of Perutz's.

Proof. Using theorem 2.1 and the formulae for Cn and �Cn, we only need to show that
if (i) and (ii) are satisfied, then

  ev  i     (dwk  dw�k)                -  i  w(d)(ea)w       ea      n = 0 .      (27)
      2                                   2
         k

The first step is an algebraic manipulation to prove that

ev[wd(aea)w]                 =     d(aea)      =    1   Tr[d        C C (aea )]   (28)
                                                  2e2

as functions on M �  with imaginary values. Here C is the matter part of the opera-
tor defined in (6) associated with infinitesimal gauge transformations, C is the adjoint
operator and  is some positive real number. The general expression for the composition

         CC : 0(; P �Ad g) - 0(; P �Ad g)

is written down in [4] and, in the case of complex vector spaces, reduces to

CC(aea) = -e2 kab c  d(ec)d(eb) + d(eb)d(ec)  ea .                                (29)

From this one computes that

Tr d  CC(aea) = -e2 kab c  d(ec), d(eb)  Tr d(ea)                                 (30)

                                  = -ie2  B, d(cec)  ,

                                          9
where {�, �} is the anti-commutator and

  B = kab (d)(eb) Tr - id(ea) .

Now observe that assumption (ii) implies that, for all ea,

Tr[Bd(ec)] = kab Tr d(eb) d(ec) Tr - id(ea)                         (31)

  = kab  kbc Tr - i d(ea) =  Tr (i 1n�n)d(ec)

for some positive real . This means that B - i1n�n belongs to the subspace of u(n)
orthogonal to d(g). But B belongs to d(g) and, by assumption (i), so does i1n�n, hence
the vector B - i1n�n necessarily vanishes in u(n). This shows that B is proportional to
the identity matrix, and hence (30) leads to the equality (28).

    The second step in the proof is to consider the gauge part CA of the infinitesimal gauge
transformations (6). Using the formulae given in [4], we have that

Tr d  CA CA(aea) = Tr d - g� (� a - � a) ea                         (32)

  = dd Tr[ d(aea) ] ,

where dd is the Hodge laplacian acting on functions on . Given that this term has a
vanishing integral over , we conclude that

  Tr  d  C(A,)C(A,)() m = 2e2  d()  m                               (33)


for all sections  in 0(; P �Ad g). Using then the definition of the pull-back ev and

the Weil homomorphism in (13), and using also formula (10) for the curvature FA, it is
clear that as a 2-form on M acting on a tangent vector (A1 + 1, A2 + 2),

  ev wd(ea)w  ea  m =  d(ea)  FAa  m                                (34)


                                             =    1    Tr  d() m ,
                                                2e2


where  is the section of the adjoint bundle P �Ad g   defined in (11). But in the case
of the linear target X = Cn this definition simplifies, and we get

Tr  d() = -2 e2 kab Tr d(ea) 2 (d)(eb) 1 + c.c.                     (35)

  = -2 i e2 2 B 1 - 1 B 2 = 2  e2 2 1 - 1 2

  = 2  e2 ev( dwk  dw�k) (A1 + 1, A2 + 2) .

  k

                                         10
Finally, bringing together (34) and (27), we conclude that formula (26) in the statement
of the proposition is true.

4 The vortex K�ahler class in abelian linear models

The formulae for the Ka�hler form M that we have obtained so far all depend on the
curvature FA of the universal connection, and so are not particularly explicit. But while
this lack of explicitness is unfortunate, it is as far as one can expect to go at such a
general level, because in most cases we know very little about the vortex moduli space
M, sometimes not even knowing whether it is a non-empty set. There are, however, a
few notable exceptions to this generic ignorance. The main example is the vortex moduli
space in abelian gauged linear sigma-models, i.e. when we pick the target X to be a
complex vector space acted by a torus through a linear representation. This example is
important in physics [32, 24] and a rather concrete description of M is known [24, 31].
In this section we will use that description to give an equally concrete formula for the
cohomology class [M] of the Ka�hler form for abelian linear models.

To fix notation, we now take  to be a compact Riemann surface and the target X to

be Cn acted be a linear representation  of the k-torus with integral weights, or charges,

Qaj , where the indices run as 1  j  n and 1  a  k. We take P   to be a
T k-principal bundle of integral degree deg P  Zk and define Lj = P �j C to be the

line-bundle over  associated with the restriction of the representation to the j-th copy

of C inside Cn. Then                  k

                           deg(Lj) =       Qja (deg P )a .

                                      a=1

With these conventions  is a section of the vector bundle nj=1Lj over , and the vortex

equations read

                �A = 0                                             (36)

                 FAa - e2     Qja|j| -  a = 0  a = 1, . . . , k ,

                           j

where the  a's are fixed real constants. The moduli space of solutions to these equations
depends on the values of the constants deg P , Qaj and  a, and as these values change it
can range from anything as interesting as the empty set to a complicated singular toric

                                      11
variety. In favourable cases, however, the moduli space M can also be a smooth complex

manifold, and this is the case we will treat in this section. The conditions on the constants
Qja and  a that ensure the smoothness of M are similar to the conditions that ensure the
smoothness of the symplectic quotient �-1(0)/T k. They can be stated as follows (see [31]

and the appendix).

Assumption (i) 4.1. The two vectors  and  - 2(deg P )/(e2 Vol ) in the Lie algebra
t  Rk can be written as a linear combinations jI cjQj with positive coefficients for
some index set I  {1, . . . , n} and, furthermore, for all such I's the set of weight vectors
{Qj : j  I} generates the integer lattice Zk in Rk.

To this requirement we also add:

Assumption (ii) 4.2. For all j = 1, . . . , n the integers dj = deg Lj = Qaj (deg P )a are
positive and bigger than 2g - 2 � the Euler characteristic of .

    The second assumption is here to guarantee that M, besides being smooth, has the
following simple description.

Theorem 4.3 ([24, 31] and appendix). Under assumptions (i) and (ii) the vortex moduli
space M is a smooth fibre-bundle over the k-fold cartesian product of the jacobian J.
The fibre of M  �kJ is isomorphic to the toric manifold Fdj, of positive dimension
d = j(1 - g + dj) - k defined as -1(0)/T k, where

  (a) the torus T k acts on Cd+k with the same weight Qaj on the coordinates
       wj,1, . . . , wj,1-g+dj , for all j = 1, . . . , n;

(b)  is the moment map Cd+k  Rk of this action, given by

                                     1     n  1-g+dj
                                     2
(w)  =                            -     (             Qj |wj,lj |2) -  .  (37)

                                           j=1 lj =1

Remark. As is well-known, the jacobian manifold of a Riemann surface of genus g is
isomorphic to T 2g. In the special case where  is the 2-sphere the jacobian is a point,
and therefore the moduli space M coincides with the toric manifold Fdj, .
Remark. The description of M contained in theorem 4.3 is valid in more general cir-
cumstances. For example if the weights Qja are such that the quotient Fdj, = -1(0)/T k
is an orbifold, then although M will not be smooth, it will still be a fibration over �kJ
with (singular) fibre Fdj, .

                                                       12
    We will not describe here how theorem 4.3 can be proved. A sketch of the proof is

given in the appendix and the original arguments can be found in references [24, 31]. One
important point for us, though, is that the fibre bundle M described in the theorem is
constructed as the quotient of a certain vector bundle V  �kJ by a (C)k-action on
the fibre. In fact, the bundle V splits as the direct sum V = jVj of natural complex
vector bundles Vj  �kJ of rank 1 - g + dj. If we then let (C)k act on the fibres of each
Vj by multiplication with weight Qj, we get a global action on the sum V that on each
fibre looks like the action (a) of theorem 4.3. The moduli space M is then the quotient
of the stable set by this (C)k-action, or equivalently, the quotient of -1(0) by the real
T k-action.

    This construction is relevant for our purposes because it allows us to define a set of
natural cohomology classes a on the moduli space. In fact, observing that -1(0)  M
is a principal T k-bundle, we can define a to be the first Chern class of the associated
line-bundle La = -1(0) �U(1)a C  M. (Here the notation means that T k acts on C by
simple multiplication of the a-th U(1)-factor inside T k.) Thus, for the record,

a := c1(La)                                       in H2(M; Z) for a = 1, . . . , k.      (38)

These cohomology classes are standard in toric geometry and are known to generate the
cohomology ring of the toric quotient Fdj, . Thus, in the case of genus zero, the a's
generate the whole cohomology of M. For higher genus they generate the cohomology of
the toric fibres of M  �kJ.

    In the higher genus case there is another set of natural cohomology classes on M.
These are the pull-backs of the cohomology classes of the jacobians J  T 2g by the
projection M  �kJ. If for each jacobian inside the product �kJ we call a the
Poincar�e-dual of the theta divisor, then after pulling-back to M we get the natural set
of classes a  H2(M; Z). Using both these sets of cohomology classes we can now state
the main result of this section.

Theorem 4.4. For the vortex moduli space M described in theorem 4.3, the cohomology
class of the vortex K�ahler form is

                                            k  a  Vol    -      (deg  P )a  a  +      a  (39)
                                               2            e2                    e2
                  [M] = 2

                                          a=1

inside H2(M; R).

                                                       13
Remark. This result extends to more general abelian gauged linear sigma-models the
formula found in [21, 26] for the classical abelian Higgs model. Our formula is formally
very similar to the latter, the main difference being that for non-trivial charges Qja the
interpretation of the classes a is more evolved. Note also that in [21] the Ka�hler form
M is normalized so that the global 2 factor disappears.

Proof. To prove this result we use proposition 3.1 and examine carefully the class [FAa]
defined by the curvature of the connection A on the universal bundle P  M � . The
first thing to observe is that the group G of gauge transformations acts freely on the full
set of vortex solutions. This is so because only constant gauge transformations preserve
the connection A, and, due to the holomorphy condition A� = 0 and assumption (i),
the T k-stabilizer of (z) is trivial for a generic point z  . This observation actually
belongs to the proof of theorem 4.3, so we need not justify it here further; in any case, it
shows that both M = V/G and P = (V � P )/G are globally smooth. Now, as described
in section 2.1, the construction of the universal bundle P implies that its restriction to
[A, ] �  is isomorphic to P  , and so

            -1  [FAa ]  |[A,]�  =  -1  [FAa ]  =  (deg P )a  in Z  H2(; Z) .  (40)
            2                      2

On the other hand, if we pick any point p   and define the subgroup of gauge trans-

formations

                Gp := {g :   T k such that g(p) = (1, . . . , 1) } ,

it is clear that G splits as Gp � T k and that

                P |M�{p} = (V � Pp) / G = [(V � Pp)/Gp] / T k                 (41)

                                = [(V/Gp) � Pp] / T k  V / Gp ,

where in the last step we have used that the T k-action on the fibre Pp is free and transitive.
So we conclude that the restriction of P to M � {p} is isomorphic to the T k-bundle
V/Gp  M.

    Consider now the space of holomorphic sections

                                   B = {(A, ) : �A = 0}

and the open subset B  B where the group GC of complex gauge transformations acts
freely. As sketched in the appendix, the proof of theorem 4.3 defines the total space of

                                               14
the vector bundle V  �kJ as the quotient of B by the subgroup GC/(T k)C  GpC. The
natural (C)k = (T k)C action on V then comes from the residual (C)k action on B/GpC,
and this is free exactly on B/GpC. But the same proof also says that any (A, ) in B is
in the GC-orbit of a vortex solution in V, and that this solution is unique up to real gauge

transformations. This means not only that there is an identification of the full quotients

M = V/G  B/GC, but also that V/Gp can be identified with any submanifold of B/GpC
of real codimension k that intersects once all the (C)k-orbits in B/GpC. Finally, through
the identification of B/Gp with the stable subset of V mentioned before, we see that one
such submanifold is exactly -1(0)  V , where  : V  Rk is the moment map defined

fibrewise by (37). Hence the T k-bundle V/Gp  M is isomorphic both to P |M�p and to
-1(0)  M. The conclusion is then that

-1                           [FAa ]  |M�{p}  =  c1(P |M�p �U(1)a C)    =  c1(La)   =  a         (42)
2

in H2(M; Z).
    Having computed the restriction of the curvature class [FA] to both [A, ] �  and

M � {p}, the only remaining task is to describe the components of [FA] that have one
leg in  and one leg in M. For this we consider the standard set {l, l+g : l = 1, . . . , g}
of generators of H1(, Z) and write

                             -1                    g
                             2
                                     [FA]mixed  =       ja  j + ja+g  j+g                       (43)

                                                   j=1

in the cohomology H2(M � ; Z). Then the 's are uniquely determined elements of
H1(M; Z) that contain all the relevant information about [FA]mixed. Leaving them un-
specified for the moment, we can press on with the Ka�hler class computation and substi-
tute in the integral of proposition 3.1 (with m = 1) the various components (40), (42),
(43) of the curvature. This leads to the expression

                                                   2                      22  g
                                                   e2                     e2
[M] =                                 a (Vol) -        (deg  P  )a  a  +           ja  ja+g  ,  (44)

                          a                                                   j=1

and is almost the formula stated in the theorem. The only task left is to identify the
class j ja  ja+g with the class a in H2(M; Z). This can be done through the following
indirect observation.

    Looking at the formulae for the action of the curvature form FA on tangent vectors, one
sees that the second line in (10) depends only on v  T  and on A , not on . This means

                                                        15
that the leg of (FA)mixed resting on M actually rests only on the base of the fibration
M  �kJ, because it is the base that parametrizes the different complex structures on
the Lj's (which, recall, determine and are determined by the different connections A).
In other words, since the mixed part of FA does not depend on , it is the same as in
the vortex equations with target X = point, and this is just the pure gauge theory with
moduli space Mpure gauge = �kJ. This means that the a's in formula (43) are actually
classes in �kJ pulled back to M and that, as classes in �kJ, they do not really depend
on the matter part of the gauged linear model we are working on. Comparing with the
simpler abelian Higgs model of [21, 26, 7], we conclude that the class l la  la+g, as
a class in the a-th jacobian J  T 2g, is just the standard integral symplectic form on
this torus, or in other words it is the Poincar�e-dual a of the theta-divisor in J. This
concludes the proof.

5 Application: volume of simple moduli spaces

5.1 Volume of spaces of abelian semi-local vortices

On any given compact Ka�hler manifold there are several interesting metric quantities
that can be computed with a very limited knowledge of the local details of the metric.
Two important examples are the overall volume of the manifold and the global integral
of the scalar curvature, which depend solely on the Ka�hler class of metric and on the
cohomology ring of manifold. Here we are interested in exploiting these facts in the
case of vortex moduli spaces and metrics. Observe in particular that for the abelian
models studied in the last section our odds look quite promising, for we already have a
topological description of the moduli space (theorem 4.3) and of the Ka�hler class of the
metric (theorem 4.4). It turns out, however, that for the general toric fibrations Fdj, 
M  �kJ of section 4, the intersection combinatorics on M can be complicated, and so
the volume computation is not straightforward. A nice and easy exception, nevertheless,
occurs when we consider the simple case of the vortex moduli space for group G = U(1)
acting by scalar multiplication on the target X = Cn. In this case all the toric manifolds
Fdj, become projective spaces, which have a simple cohomology ring, and so we can easily
carry out the computations to the end.

    The volume computations presented here extend several results that can be found in
the literature. These include the case n = 1 and arbitrary  calculated in [21], and the

                                                       16
case of arbitrary n  1 and special  = T 2 calculated in [15] through a heuristic brane
construction. A third method to compute the volume of M in the case  = CP1 and
n = 1 was described in [27]. The scalar curvature integrals presented here, on the other
hand, had not been considered before.

    As described above, in this section we will take  to be a compact Riemann surface
and consider the special case of vortices with group U(1) acting by scalar multiplication
on the target Cn. These are sometimes called abelian semi-local vortices. In the notation
of section 4, they correspond to the choice k = 1 and charges Q11 = � � � = Qn1 = 1. Applied
to this particular case, theorem 4.3 and its proof say that if deg P = d is positive and
satisfies d > 2g - 2, then for sufficiently big volume of the surface  the moduli space M
of vortex solutions is isomorphic to a projective bundle. More specifically, there exists a
complex vector bundle V  J of rank n(1 - g + d) over the jacobian of  such that

        M  P(V )  J .                       (45)

The total Chern class of this vector bundle has the very simple form c(V ) = e-n, where
 has the same meaning as in section 4, i.e. it is the degree 2 cohomology class on J that
is Poincar�e-dual to the theta divisor [7]. Also, with these choices, the formula in theorem
4.4 for the cohomology class of the vortex Ka�hler form specializes to

[M]  =      Vol    -   2   d    +  22    .  (46)
                       e2          e2

Observe that this description of the moduli space is valid only if the constant  e2 Vol 
is bigger than 2d (assumption (i) of section 4). If it is smaller, it is well-known that M
is actually the empty set, as can be easily recognized by integrating over  the second
vortex equation. Now, to make further computations with this expression for [M], it is
important to understand clearly the meaning of the class   H2(M, Z). Firstly, define
V  := V \ {zero section} and consider it as a principal C-bundle over the jacobian. A
careful inspection of the definition of  in section 4 and of the proof of theorem 4.4, shows
that  is the first Chern class of the associated bundle V  �C C. But this bundle is
defined by the simple equivalence relation (v, w)  (v, w) in the product V  � C, and it
is a standard fact that this relation defines nothing more than the dual of the tautological
line-bundle L  P(V ) over the projectivization. Thus, going back to definition (38),
we conclude that L  L and that the class  is just the first Chern class of the anti-
tautological bundle L  P(V ).

                   17
    As a last preparatory point we also need to write down the first Chern class of the
moduli space M. This will be necessary for the evaluation of the scalar curvature integral.
General results for projective bundles P(V )  J say that the total Chern classes satisfy

                                     c[T P(V )] = c(V  L) c(T J) .

Using the fact that in our case the base of the fibration is the jacobian � a group manifold
with trivial tangent bundle � this formula then implies that

                     c1(T M) = (rank V ) c1(L) + c1(V )           (47)

                                = n(d + 1 - g)  - n .

    Having registred these general formulae, we can now turn our attention to the integrals
that directly concern us, namely

                     Vol M =          volM =  1     [M]r          (48)
                                              r!
                                   M              M

for the volume, and

                        s volM  =     2         c1(M)  [M]r-1     (49)
                                   (r - 1)!
                     M                       M

for the total scalar curvature. Here r = g + n(d + 1 - g) - 1 is the complex dimension
of the moduli space and, in both expressions, the last equalities are well-known facts of
Ka�hler geometry. Now, calling  the natural projection on the fibre bundle M  J,
standard integration over the fibre yields the first equality of

                        r-i  i =     (r-i)  i     =  ng-ig!    .  (50)
                                                     (g - i)!
                     M             J

The last equality, on its turn, is a consequence of the following two facts. Firstly, using

our previous interpretation of the class , a simple manipulation explained in [7] says that

                     (r-i) = (n )g-i/(g - i)! .                   (51)

Secondly, the identification of  = l l  l+g with the standard symplectic form on the
jacobian torus (explained at the end of section 4) leads straightforwardly to

                                                     g = g! .

                                                                           J

And this is all we need to know. Combining (50) with expressions (46) and (47) for the
Ka�hler and first Chern classes of M, a final direct computation yields

                                   18
Theorem 5.1. Consider the vortex equations with group U(1) acting on the target Cn

by scalar multiplication, and assume that the degree d = c1(P ) is positive and satisfies
 e2 (Vol )/(2) > d > 2g - 2. Then the vortex metric gM on the moduli space has total

volume                   g        g! ng-i
                            i! (r - i)! (g - i)!
        Vol M = r                                 2 i        Vol    -  2    d   r-i           (52)
                                                  e2                   e2
                    i=0

and total scalar curvature (or Einstein-Hilbert action)

   s volM  =  (2)r   g      g! ng-i r + 1 - 2g + i       i        Vol    -      d    r-1-i    (53)
                    i=0      i! (r - 1 - i)! (g - i)!    e2  2              e2
M                                                                                          ,

where the integer r is defined by r = g + n(d + 1 - g) - 1. If the degree d is bigger than
 e2 (Vol )/(2), then M is the empty set.

Remark. To compare our volume result with the ones obtained in [21] and [15], we
first observe that in both these references the natural vortex metric (4) is defined with a
prefactor of 1/, chosen to make the global factor r disappear in the end result. Then
with the choices  = 1 and e2 = 1/2, our formula (52) reduces exactly to the result
presented in [21] for n = 1. Moreover, in the genus one case, (52) also reduces to the
formula of [15], showing that for  = T 2 the heuristic brane methods remarkably predict
the correct result.

Remark. Having computed both the total volume and the total scalar curvature of the
vortex metrics gM, it is possible to obtain the explicit values of the Yamabe functional
I(gM) = ( M s volM) / (Vol M)r/(r-1) for these metrics. For example in the simplest case
of genus zero the moduli space is M = CPr and we have I(gM) = 2r(r + 1) / (r!)1/r,
which no longer depends on the volume of  and on the constants  and e2.

5.2 Volume of spaces of holomorphic curves

The vortex moduli spaces that we have been considering in this section are very closely
related to the spaces of holomorphic maps from the Riemann surface to projective spaces.
In fact, as explained for example in [7], for each degree d  2g the moduli space M,d of
vortices with group U(1) and target Cn is a smooth compactification of the space H,d
of holomorphic maps   CP n-1 of the same degree. Moreover, each vortex solution
(A, ) such that (z) never vanishes as a section of nL   defines in a natural way a

                            19
holomorphic map � :   CP n-1 by the formula

�(z) = 1(z), . . . , n(z) ,                    (54)

where the components j are written using any local holomorphic trivialization of L
(holomorphic with respect to the complex structure on L induced by A), and using ho-
mogeneous coordinates on the projective space. Observe that the map (54) is invariant
under complex gauge transformations of the section . Calling Mo  M the open dense
subset of vortex solutions such that the components of (z) never vanish simultaneously,
the formula above then defines a biholomorphism Mo ,d  H,d (see [7] for more details).

    Once we have these identifications in mind, it is obvious to ask whether the natural
L2-metric on the vortex moduli spaces bears any relation to the natural L2-metric on the

spaces of holomorphic maps. Looking at the definition (4) of the vortex metric, it is clear
that the hope lies in the limit e2  , for in this case the terms that depend on A drop

out and leave the bilinear form on the space of tangent vectors determined by

(A , ), (A , ) - ||2 vol .                     (55)


Now, although this quadratic form clearly does not define a metric on the space of all
tangent vectors (A , ), it is easy to check that if the (A, )'s satisfy the linearized version
of �A = 0 and are tangent at a point (A, ) where (z) never vanishes, then (55) is

actually positive definite. This means that (55) does define a metric on the space of vortex
solutions above Mo, and since this metric is invariant by real gauge transformations, also
a metric on Mo itself. This metric corresponds to keeping just the second term on the
right-hand side of (4), and as the constant e2 becomes larger it differs less and less from

the vortex metric.
    And what is the limit of both these metrics when e2 goes to infinity? To start answering

this question, observe that although the vortex solutions change as e2 increases, they

only change by a complex gauge transformation. This is so because the usual Hitchin-

Kobayashi correspondence tells us that any vortex solution, independently of the value of
e2, is complex gauge equivalent to a solution of �A = 0. In particular this implies that
the induced holomorphic map � :   CP n-1 of formula (54) does not depend on e2.

20
Consider now the formal limit of the vortex equations (36)as e2  . It reads

                          �A = 0                                             (56)

                          �  =  1   -          |j|2 = 0 ,
                                2
                                            j

and corresponds to holomorphic sections  whose image is entirely contained in the subset
�-1(0)  Cn. Such a section also descends to a map �, and it is shown in [11] that for n > 1

this correspondence establishes a bijection Mo  H between the space of equivalence
classes of solutions of (56) and the space of holomorphic curves to CP n-1. Now, if the

image (z) is always contained in the zero level �-1(0), then it follows from the very

definition of the induced metric CPn-1 on the symplectic quotient �-1(0) / U (1)  CP n-1
that the metric on the moduli space Mo determined by (55) corresponds under the
identification Mo  H to the usual metric on the space of holomorphic maps � to the
Ka�hler target (CP n-1, CPn-1). Thus the hope is that if as e2 increases the vortex solutions
on Mo would "nicely" approach the solutions of (56), then the metric on Mo determined

by (55) � and hence also the vortex metric � would "nicely" approach the metric on

M o determined by the same formula, which, as we have seen, under the identifications
M o  H  Mo is nothing but the natural L2-metric on H.

Conjecture 5.2. With the identification Mo  H described by (54), the pointwise limit
of the vortex metric as e2   is the natural L2-metric on the space of holomorphic maps
  CP n-1, where the target �-1(0)/U (1)  CP n-1 should be endowed with the quotient

Ka�hler metric.

It is straightforward to check that for the moment map specified in (56) this quotient

metric is just

                             CP n-1 =  norm. FS ,                            (57)

where norm. FS denotes the normalized Fubini-Study form on the projective space (the
generator of the integer cohomology). This conjecture can perhaps be made rigorous

through a careful study of the analytic results in [17] that describe how the vortex solutions
approach the solutions of (56) in the adiabatic limit e2  . Similar results may also be

true for vortex equations with other targets and gauge groups.

Pressing forward with this hypothesis, one can then use theorem 5.1 and the informal

manipulation

                 Vol H =    volH =      elim(volM)  =  lim (Vol M)           (58)

                          H         Mo                 e

                                        21
to obtain conjectural formulae for the integrals over the non-compact spaces H.

Conjecture 5.3. For n > 1 and d  2g, the total volume and the total scalar curvature of
the natural L2-metric on the space H of degree d holomorphic maps   (CP n-1, CPn-1)
are given by

Vol H =     ng                       Vol  n(d+1-g)+g-1                           (59)

            n(d + 1 - g) + g - 1 !

  s volH =  2 ng n(d + 1 - g) - g    Vol  n(d+1-g)+g-2 .                         (60)

H           n(d + 1 - g) + g - 2 !

Remark. As far as the author is aware, the only instance where these integrals have been

computed so far is the direct volume integration in [2] for the very special case of degree
one CP 1-lumps on the sphere. This corresponds to the choices g = 0, d = 1 and n = 2

in the formulae above. Taking into account that in [2] the Fubiny-Study metrics on both
CP 1's were chosen with volume  � and hence for the target space this corresponds to
the choice  = 1 � we see that (59) reduces exactly to the value 6/6 obtained there.1

6 Samols' localization for vortex metrics

The definition (4) of the vortex Ka�hler metric involves an integration over the manifold
, hence its common designation as the L2-metric. In very special cases, however, it
turns out that this integral can be localized, and appears as a sum of contributions from
complex codimension-1 submanifolds of . This phenomenon was first studied in detail by
Samols in the case of the classical abelian Higgs model over a Riemann surface [28], where
the group U(1) acts on the target C and the submanifolds of  are just points. It is not,
however, a peculiarity of that single example. In fact, as we will see, one should expect
something similar to happen roughly whenever the Ka�hler quotient X//G is a point, or in
other words, whenever the complexified GC-action is free and transitive on an open dense
subset Xo  X. Here the two main examples that we will keep in mind are the vortex
equations with group G = U(N) acting on the space of N � N square matrices, studied
for example in [7, 1, 19, 14, 5], and the abelian equations with G a torus and X a toric
manifold [3].

    1Since the first version of the present paper appeared, Speight has rigorously verified the volume
formula (59) also in the case g = 0, d = 1 and arbitrary n [29].

                                                       22
    This section can be read independently of the previous four, and the notation will

be as follows. The local complex coordinates on the base  and on the target X are,
respectively, {z} and {wj}. With respect to these the Ka�hler forms are written as
 = (i/2)h� dz  dz� and X = (i/2)hjk� dwj  dwk�. The group G has Lie algebra g
with a basis {ea}, and for each vector v  g the corresponding vector field on X induced
by the left action is called v^. Observe then that over the open subset set Xo  X where
GC acts freely and transitively, the complex span of the vectors e^a is the full tangent
space.

    The definition (4) of the vortex L2-metric gM says that for a tangent vector (A , )
orthogonal to gauge transformations (also called a horizontal tangent vector) the L2-norm

is given by

|| (A , ) ||2L2 =    E(A , ) vol =          1   kab  A a      A b   +  gX(, ) vol .  (61)
                                           4e2


The localization of this integral follows from the fact that the energy density E(A, ) vol
is actually an exact differential form on the inverse image -1(Xo)  .

Proposition 6.1. Let (A, ) be a vortex solution such that o := -1(Xo) is an open
dense subset of . Then for any horizontal tangent vector at (A, ) to the space of vortex
solutions, we have that

                   E(A, )  =        -  2   h�        (kab �a A b�)                   (62)
                                       e2

over o, where the complex a's are defined by  = a e^a in T X. In particular the density
E(A , ) vol is an exact differential form over o.

Proof. In local coordinates the first vortex equation in (2) can be written as

                   �j + Aa� e^aj = 0 ,                                               (63)

where the quantities defined on the target X are implicitly being evaluated at the point
(z). Its linearization therefore reads

                   �j + Aa� (ke^j) k + A a� e^ja = 0 .                               (64)

Substituting into this expression the definition j = a e^ja and using the standard fact
that

                                             [e^a, e^b] = -facb e^c ,

                                         23
where the facb's are the structure constants of the Lie algebra, this linearized equation

reduces to

                           (�a + A a� + facb Ab� c) e^a = 0 ,                     (65)

which over o implies that

                                A a� = -A� a .                                    (66)

The linearization of the second vortex equation, on its turn, can be combined with the
horizontallity condition into the single complex equation [4]

            2 h� (A A �) + e2 kab hjk� e^kb j = 0 .                               (67)

(Recall that the horizontallity condition, which is the real part of (67), is called in physics
Gauss' law, and just demands orthogonality between (A , ) and all vectors tangent to

real gauge transformations.) Using (66) and (67) it is then straightforward to check that

            h� kab A a A b� = -h� kab  (�a A b�) - �a (A A b�)

                             =  -h�  (kab �a A b�)         -  e2   hjk� k   j  ,  (68)
                                                              2

and (62) readily follows. Finally, defining the real 1-form on o

                             =  2     kab �a A b�  dz�  +  c.c. ,                 (69)
                                e2

standard manipulations in Ka�hler geometry show that

            E(A, ) vol       =  -  1  g(, d)       vol     =  -    1  d           (70)
                                   2                               2
                             = d(-12   ) ,

where we have used that  is harmonic, and hence d-closed. This confirms the second
assertion of the proposition.

    Making use of Stokes' theorem, it is clear that the result of this proposition leads
directly to the localization of the energy integral (61). To make the discussion simpler,
we assume for the rest of this section that  is a Riemann surface. Then the condition of
proposition 6.1 means that o should be equal to  minus a finite set of points z1, . . . , zr.
Let now DsR be a small disk of radius R around the point zs, and let DsR be the circular
boundary of the disk with the conventional boundary orientation. Then Stokes' theorem
leads to the following result.

                                      24
Corollary 6.2. Assume that  is a Riemann surface. Then under the conditions of
proposition 6.1 the L2-norm of horizontal tangent vectors is given by

                                          r                      i
                                                                 2
                 || (A , ) ||L2 2 =             lim           (     kab �a A zb�)  dz�  .           (71)

                                       s=1      R0      DsR

This result implies in particular that the right-hand side of (71) is a real number, a fact

that a priori is not obvious. It is also not difficult to argue that each of the loop integrals

in (71) is finite, not just their sum. This follows for example from the observation that,

for any R1 > R,

lim       ( kab �a A bz� ) dz� =                  E(A , ) vol +        DsR1 ( kab �a A bz� ) dz� ,

R0   DsR                                     DsR1

and the right-hand side is finite.

7 Examples of localization

7.1 Linear non-abelian vortices

In this section we will apply the localization results obtained above to particular examples
of vortex equations. We will always assume that  has complex dimension one, i.e. that
it is a Riemann surface. Our first example is the equations with group G = U(N) acting
by left multiplication on the target space X = MN�N of complex square matrices. Note
that in this case Xo  X is the submanifold of matrices with non-vanishing determinant.
Also, with the usual identifications on linear spaces, the vector field induced by v  g and
the left action at a point M  MN�N can be written as

                 v^ |M = v M in TM (MN�N )  MN�N .                                                  (72)

The Ka�hler form on the target is chosen to be

                        X              =     i  Tr  (dM       dM )  ,                               (73)
                                             2

so that with the natural choice of Ad-invariant inner product on the Lie algebra

                                    k(v1, v2) = Tr (v1 v2) ,

the moment map becomes simply

                 �(M )  =           -  i  (M M       -    1)         u(N) ,                         (74)
                                       2

                                                    25
with  a real constant. This particular example of vortex equations has been thoroughly

studied, and it is well-known that if (A, ) is a solution with det  not identically zero,

then necessarily det  vanishes only at a finite number of points z1, . . . , zr   [5, 14].

This means that the first condition of proposition 6.1 is satisfied, so that localization is

applicable.
    Now let (A, ) be a horizontal tangent vector at (A, ). It follows from the definition

of a in proposition 6.1 that the vectors  = aea in the complexified Lie algebra are

given by

                       (z) =  -1               for z = zj .           (75)

Using the first vortex equation, expression (66) then becomes

                A z� = -(z�) -1 + (z�) -1  -1 ,                       (76)

which leads to

                kab �aA zb� = - Tr  z�[()-1] ()-1 .                   (77)

Consider now the gauge-invariant function

                f :  � M - {hermitian matrices}                       (78)

                       (z, [A, ]) -  (z) .

Using the definition (5) of the natural complex structure JM on the moduli space, it is
easy to check that

          (Mf ) (A, )  =  1  (df )(A, ) - i (df )(JM(A , ))    =   ,  (79)
                          2

and similarly

                             (�Mf ) (A , ) =   .                      (80)

Thus if   T[A,]M is a tangent vector represented by (A , ), the combination (77) can
be rewritten as

               kab �aA zb� = -Tr f -1(�Mf )() z�(f -1Mf )()           (81)

                = -Tr f -1(u�k f ) z�(f -1uj f ) (duj  du�k)(, ) ,    (82)

where {uj} is any set of local complex coordinates on the moduli space. Finally, the
localization of the previous section leads to the following formulae.

                                           26
Proposition 7.1. For any choice of complex coordinates {uj} on the vortex moduli space,
the K�ahler form of the L2-metric is locally given by

M  =  i       Tr hzz� z (f -1 u�k f ) z�(f -1 uj f )  vol duj  du�k             (83)
      e2                                                                        (84)


       1    r
      2 e2
   =             lim         Tr (f -1 u�k f ) z�(f -1 uj f )  dz�  duj  du�k ,

                    R0  DsR
            s=1

where f is the gauge invariant matrix function  on the product  � M, and the DsR's
are small circles of radius R around the points zs   where det  vanishes.

Remark. Although the function f -1 is singular at the points zj, the very way in which
the formulae were obtained shows that the integrand of (83) is a smooth function all over
. It is not, however, the exterior derivative of something everywhere smooth, hence the
localization to the circle integrals around the points zj. Note also that in (84) we are
not assuming that det  vanishes at zj with multiplicity 1 � the formula is valid for any
multiplicity.

    To take the calculation farther we would like to perform the contour integrals along
the small circles DsR, and this requires some knowledge about the singularity of f -1
at the zeros z = zs. For simplicity we assume at this point that we are calculating in
the region Mseparated of the moduli space where the vortices do not coincide, which is an
open dense subset of M. In this case det  vanishes at z = zs with multiplicity one and
the kernel ker (zs)  CN has dimension one. In fact, it can be shown that the moduli
space of d separated vortices is parameterized precisely by the different possible choices

of distinct points zs   where det  vanishes and the choices of corresponding kernels
Ls = ker (zs)  CPN-1, i.e.

Mdseparated  {(zs, Ls)   � CPN-1 : 1  s  d and zs = zr for s = r} .             (85)

This identification is a special case of a result proved in [5] for compact  and is generally
assumed (on strong grounds) to be true also for  = C [14].

    As a first step in the residue calculation we will deal initially with the N = 1 abelian
case, thereby reproducing Samols' original result. The generalization to arbitray N will
follow.

                        27
7.1.1 N = 1 abelian case (Samols' result)

For non-coincident vortices it can be shown that around the zero zs each vortex solution
can be uniquely factorized as

                              = (z - zs) a(z, z�) ,                                  (86)

where the function a is smooth and does not vanish at z = zs. Alternatively, in terms of

gauge invariant quantities,

                             ||2 = |z - zs|2 |a|2 .                                  (87)

Substituting this expression in the contour integrals of (84) it is then easy to compute the
residue

lim       Tr (f -1 u�k f ) z�(f -1 uj f )  dz� = 2i (u�k z�s) z�uj log |a|2 |z=zs .  (88)

R0   DsR

Taking as coordinates on the moduli space Mseparated the positions of the vortices, i.e.
ur = zr, the expression for the Ka�hler form becomes simply

     M  =  i                    d                    2  |z=zr  dzs  dz�r ,           (89)
           e2                                z - zr
                                   z�zs log

                             r,s=1

and this is Samols' result for the metric in terms of the local behaviour of ||2 around its
zeros.

Remark. As described above, the argument of the logarithm in (89) is the smooth and
positive function |a|2, so there is no singularity here. The precise expression of the metric
given by Samols in [28] can be recovered by expanding log |a|2 as a Taylor series around
zr and expressing (89) in terms of the Taylor coefficients.

7.1.2 N > 1 non-abelian case

Our aim here is to explain how Proposition 7.1 can be used to write down an expression
for the vortex Ka�hler metric in terms of complex coordinates on Mseparated. Using the
identification (85), we will take as coordinates on the moduli space the location zs of
the zeros of det  and a standard set of coordinates on CPN-1. For this we will assume
that we are on a region of the moduli space where the lines Ls = ker (zs)  CN can
be written as the span of a vector of the form (ws1, . . . , wsN-1, 1). The wsi 's are then the
required coordinates on the projective space. Notice that this assumption does not entail

                                           28
any real loss of generality, because such a configuration can always be reached through a
transformation of the type (z)  (z)U, with U  U(N), which is both a symmetry of
the vortex equations and an isometry of the moduli space.

    The first step in the calculation is to note that on Mseparated each vortex solution can
be uniquely factorized around the zero zs as

              = A(z, z�) H(z, zs, Ls) ,                                             (90)

where the matrix function A is smooth and invertible at z = zs and H is defined as

                                      1          -ws1 

                                         ...     ...       

             H(z, zs, Ls)  =                                  ,                     (91)


                                              1  -wsN  -1  


                                                 z - zs

with all the blank entries equal to zero. This factorization has been widely used since

[14], and the results of [5] justify it at least for compact . Observe that by construction

the matrix H satisfies det H = z - zs, at the point z = zs has kernel Ls, and depends
holomorphically on z, zs and Ls. These are the essential properties of H, and we could
have chosen a different representative in (91) with these same properties. A different choice

of representative, however, would entail a different factorization (90) and a less simple

form of the end result (94). In terms of gauge invariant quantities, the factorization above

becomes

              = H (AA) H .                                                          (92)

It is then easy to compute that the argument of (84) becomes

Tr (f -1 u�k f ) z�(f -1 uj f ) = Tr    (u�k H) H-1  uj z�(AA) (AA)-1               (93)

             + terms without poles .

Choosing the coordinates uk on the moduli space to be the zs's and the wsl 's leads to a
particularly simple formula for the residue, because the matrices (uk H)H-1 then have

only one non-zero entry. More precisely, if for all values of r = 1, . . . , d we name the

coordinates

             url = wrl                   for 1  l  N - 1
             urN = zr

                                        29
the final expression for the vortex Ka�hler form becomes simply

      i   d       N
      e2
M  =                   usj  (z�F ) F -1 | Nk z=urN dujs  du�rk ,                (94)

          r,s=1 j,k=1

where the matrix function F = AA = (H-1)H-1 is gauge invariant, smooth and
invertible around z = zr = urN . This generalizes Samols' result to these particularly well
studied non-abelian vortices.

7.2 Toric sigma-models

Our second example generalizes Samols' localization results in a different direction. We

consider here the vortex equations with a torus group G = T k and a toric target X.

In this case dimR G = dimC X and the complexified group GC = (C)k acts freely and

transitively on an open dense subset of the target, so proposition 6.1 is applicable. The

main example that we have in mind is the case X = CPk, for which the vortex moduli

space was described in [3]. Just as in the classical abelian Higgs model with X = C, the

moduli space is also parametrized by the different possible locations of special points zs
in , except that for X = CPk there are k + 1 distinct types of points, with each type

being mapped by  to a different submanifold CPk-1 inside CPk. (In the classical abelian

Higgs model, recall, there is only one type of special points in  � the points that  maps

to the origin in C.) So for instance in the simplest case X = CP1, the moduli space is

parametrized by the location in  of two distinct types of points � the points zs+ that get
mapped to the south pole of CP1, and the points zr- such that (zr-) is the north pole.
Identifying maps to CP1 with meromorphic functions, one can say that M is parametrized

by the location in  of the zeros and poles of .

    Now, since these toric examples are abelian, both the curvature FA and the moment
map �   are gauge invariant, and so descend to functions on the product  � M with

values on the Lie algebra Lie T k  iRk. Using the definition (5) of the complex structure

JM on the moduli space, it is easy to check that for a fixed z  

M(FA)azz� (A , )        =  zAA az�  =   -        e2  (h)zz� (hX )bc� kca  b  ,  (95)
                                                 2

where the last equality is the complex Gauss' law (67) and we have written (hX )bc� for the
invertible hermitian matrix hX (e^b, e^c). Substituting the curvature for the moment map

as prescribed by the second vortex equation, we then get

a = 2i (hX )a�b M(�  )b (A , ) = 2i (hX )a�b uk (�  )b u k ,                    (96)

                                    30
where {uk} is any set of complex coordinates on M. Thus, just as in the example of
linear vortices, after using (62) and (66) we conclude that the Ka�hler form on the moduli
space is given by

M  =  4i        kab (h)zz� z (hX )ca� u�k (�  )c z� (hX )bd� uj (�  )d  vol duj  du�k .
      e2


The integrand in this expression is the total derivative of something that is smooth ev-
erywhere on  except at the points where the matrix (hX)bc�  (z) is not invertible.
Accordingly, the surface integral will localize to a sum of contributions of those singular
points. As would be expected, in the X = CPk example these singular points are exactly
the points whose image by  lies in one of the k + 1 natural CPk-1's inside CPk. Thus
the local behaviour of  around these points completely determines the Ka�hler form M.

    For instance in the case of the simplest target X = CP1, the moment map � : CP1 
iR is essentially the height map on the sphere, and a calculation similar to that of section
7.1.1 shows that

   M      =  i                           z�uj log           2  |z=zs+  duj  dz�s+
             e2                                    z - zs+
                 j     zs+ {zeros of }

                    +                   z�uj log (z - zr-)  2 |z=zr- duj  dz�r- ,

                       zr- {poles of }

where for notational convenience we have called {uj} the complete set of coordinates
{zs+, zr-} on the moduli space. This is the natural generalization of Samols' formula for
meromorphic vortices.

Acknowledgements. I would like to thank Nuno Roma~o for useful discussions about
Samols' localization, and Martin Speight for a conversation about the conjectures of sec-
tion 5.2. I am partially supported by the Netherlands Organisation for Scientific Research
(NWO) through the Veni grant 639.031.616.

8 Appendix

In very informal terms, the description of the vortex moduli space in theorem 4.3 can be
understood as follows. Under the assumptions (i) and (ii) of section 4, the usual Hitchin-
Kobayashi-type correspondences guarantee that the moduli space M is isomorphic to

                                                       31
the moduli space of stable solutions of the single equation �A = 0 modulo complex
gauge transformations. (See [25] for the general theory of these correspondences and [3]
for the toric case.) But this remaining equation �A = 0 just states that  should be
a holomorphic section of jLj, where the holomorphic structure on this vector bundle
is induced by the holomorphic structure on P   determined by the connection A.
Therefore, up to complex gauge equivalence, giving a pair (A, ) that solves this equation
is the same as giving a holomorphic structure on P and a holomorphic section of jLj. The
point now is that the inequivalent holomorphic structures on a k-torus bundle over  are
parameterized by the k-fold product of the jacobian J. Furthermore, after fixing one such
holomorphic structure on P , i.e. after fixing a point in �kJ, the space of holomorphic
sections of each Lj   is canonically defined and, by Riemann-Roch, has complex
dimension 1 - g + dj. Letting this point in �kJ vary we get a collection of vector spaces
� one vector space for each different point � and this determines a complex vector bundle
Vj  �kJ of rank 1 - g + dj, as well as the direct sum bundle V = jVj. Each point of
the total space of V then corresponds to a holomorphic structure on P and a holomorphic
section of jLj, or in other words to a solution (A, ) of the equation �A = 0. These
solutions, however, are not all complex gauge inequivalent, because a constant gauge
transformation acting on (A, ) leaves A invariant but shifts the holomorphic section
, and so identifies different points on the fibres of V . Finally, quotienting by these
residual constant gauge transformations corresponds to quotienting the fibres of V by the
(complex) torus action (a) described in theorem 4.3. The resulting quotient in each fibre
is therefore isomorphic to the toric manifold Fdj, , and the moduli space M becomes the
fibre bundle of the theorem.

References

 [1] R. Auzzi, S. Bolognesi, J. Evslin, K. Konishi and A. Yung : `Nonabelian Super-
      conductors: Vortices and Confinement in N = 2 SQCD'; Nucl. Phys. B673 (2003),
      187�216.

 [2] J. Baptista : `Some special Ka�hler metrics on SL(2, C) and their holomorphic quan-
      tization '; J. Geom. Phys. 50 (2004), 1�27.

 [3] J. Baptista : `Vortex equations in abelian gauged sigma-models'; Commun. Math.
      Phys. 261 (2006), 161�194.

                                                       32
 [4] J. Baptista : `A topological gauged sigma-model'; Adv. Theor. Math. Phys. 9 (2005),
      1007�1047.
      J. Baptista : `Twisting gauged non-linear sigma-models '; JHEP 0802 (2008) 096.

 [5] J. Baptista : `Non-abelian vortices on compact Riemann surfaces'; Commun. Math.
      Phys. 291 (2009), 799�812.

 [6] N. Berline, E. Getzler, M. Vergne : `Heat kernels and Dirac operators'; Springer-
      Verlag, 1991.

 [7] A. Bertram, G. Daskalopoulos and R. Wentworth : `Gromov invariants for holomor-
      phic maps from Riemann surfaces to grassmannians'; J. Amer. Math. Soc.9 (1996),
      529�571.

 [8] I. Biswas and G. Schumacher : `Coupled vortex equations and moduli: deformation
      theoretic approach and Ka�hler geometry '; Math. Ann. 343 (2009), 825�851.

 [9] H. Chen and N. Manton : `The Kaehler potential of abelian Higgs vortices'; J. Math.
      Phys. 46 (2005), 052305.
      M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Manifestly supersymmetric
      effective lagrangians on BPS solitons'; Phys. Rev. D 73 (2006), 125008.
      S. Krusch and J. M. Speight : `Exact moduli space metrics for hyperbolic vortices';
      arXiv:0906.2007 [hep-th].
      N. Manton : `One-vortex moduli space and Ricci flow'; J. Geom. Phys. 58 (2008),
      1772�1783.

[10] K. Cieliebak, R. Gaio, I. Mundet i Riera and D. Salamon : `The symplectic vor-
      tex equations and invariants of Hamiltonian group actions'; J. Symplectic Geom. 1
      (2002), 543�645.

[11] K. Cieliebak, R. Gaio and D. Salamon : `J-holomorphic curves, moment maps, and
      invariants of Hamiltonian group actions '; International Math. Res. Notices 16 (2000),
      831�882.

[12] S. Cordes, G. Moore and S. Rangoolam `Lectures on 2D Yang-Mills theory, equiv-
      ariant cohomology and topological field theories'; Nucl. Phys. B (Proc. Suppl.) 41
      (1995), 184�244.

[13] S. Donaldson and P. Kronheimer : `The geometry of four-manifolds'; Oxford Univ.
      Press, 1990.

                                                       33
[14] M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Moduli space of non-abelian
      vortices'; Phys. Rev. Lett. 96 (2006), 161601.
      M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Solitons in the Higgs phase
      � the moduli matrix approach �'; J. Phys. A39 (2006), R315�R392.

[15] M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Statistical mechanics of
      vortices from D-branes and T-duality'; Nucl. Phys. B788 (2008), 120�136.

[16] T. Fujimori, G. Marmorini, M. Nitta, K. Ohashi and N. Sakai : `The moduli space
      metric for well-separated non-abelian vortices'; arXiv: 1002.4580.

[17] R. Gaio and D. Salamon : `Gromov-Witten invariants of symplectic quotients and
      adiabatic limits'; J. Symplectic Geom. 3 (2005), 55�159.

[18] V. Guillemin, V. Ginzburg and Y. Karshon : `Moment maps, cobordisms, and Hamil-
      tonian group actions'; Amer. Math. Soc., 2002.

[19] A. Hanany and D. Tong : `Vortices, instantons and branes'; JHEP 0307 (2003) 037.
[20] N. Manton : `A remark on the scattering of BPS monopoles'; Phys. Lett. 110B

      (1982), 54�56.
[21] N. Manton and S. Nasir : `Volume of vortex moduli spaces'; Commun. Math. Phys.

      199 (1999), 591�604.
[22] N. Manton and J.M. Speight `Asymptotic interactions of critically coupled vortices';

      Commun. Math. Phys. 236 (2003), 535�555.
[23] N. Manton and P. Sutcliffe : `Topological solitons'; Cambridge Univ. Press, 2004.
[24] D. Morrison and M. Plesser : `Summing the instantons: quantum cohomology and

      mirror symmetry in toric varieties'; Nucl. Phys. B440 (1995), 279�354.
[25] I. Mundet i Riera : `A Hitchin-Kobayashi correspondence for Ka�hler fibrations '; J.

      Reine Angew. Math. 528 (2000), 41�80.
[26] T. Perutz : `Symplectic fibrations and the abelian vortex equations'; Commun. Math.

      Phys. 278 (2008), 289�306.
[27] N. Roma~o: `Gauged vortices in a background'; J. Phys. A38 (2005), 9127�9144.
[28] T. Samols : `Vortex scattering'; Commun. Math. Phys. 145 (1992), 149�179.
[29] J.M. Speight : `The volume of the space of holomorphic maps from S2 to CP k';

      arXiv: 1003.5556.

                                                       34
[30] C. Voisin : `Hodge theory and complex algebraic geometry'; Vol. 1, Cambrige Univ.
      Press, 2002.

[31] J. Wehrheim : `Vortex invariants and toric manifolds'; arXiv: 0812.0299.
[32] E. Witten : `Phases of N=2 theories in two dimensions'; Nucl. Phys. B403 (1993),

      159�222.

                                                       35
