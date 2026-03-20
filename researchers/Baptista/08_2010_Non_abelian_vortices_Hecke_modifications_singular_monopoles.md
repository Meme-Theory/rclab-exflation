# 2010 Non abelian vortices Hecke modifications singular monopoles

**Source:** `08_2010_Non_abelian_vortices_Hecke_modifications_singular_monopoles.pdf`

---

arXiv:0907.1752v3 [hep-th] 23 Mar 2010                                                                                                   ITFA-2009-24

                                         Non-abelian vortices, Hecke modifications
                                                       and singular monopoles

                                                                             J. M. Baptista 

                                                                           Institute for Theoretical Physics 
                                                                                 University of Amsterdam

                                                                                 July 2009

                                                                                 Abstract

                                            In this note we show that for the group G = U(N) the space of Hecke modifications
                                        of a rank N vector bundle over a Riemann surface C coincides with the moduli space
                                        of solutions of certain non-abelian vortex equations over C. Through the recent work
                                        of Kapustin and Witten this then leads to an isomorphism between the moduli space of
                                        vortices and the moduli space of singular monopoles on the product of C with a closed
                                        interval I.

                                            e-mail address: [email redacted]
                                            address: Valckenierstraat 65, 1018 XE Amsterdam, The Netherlands
1 Introduction

In the groundbreaking and sizeable article [15], Kapustin and Witten, among many other
insights, gave an interpretation of the Hecke modifications of a G-bundle over a Rie-
mann surface C in terms of singular solutions of the Bogomolny equations over the three-
dimensional product I � C, with I a closed interval. This interpretation allowed them to
establish a natural correspondence between certain Hecke operators that appear in the ge-
ometric Langlands program and certain 't Hooft operators that appear in quantum field
theory, eventually leading to a far-reaching description of the mathematical Langlands
duality in terms of the S-duality in QFT [15, 13].

    With this grand work as background and motivation, in this short note we point out
that at least in the case of the group G = U(N) there exists an alternative gauge theory
description of the Hecke modifications of a bundle. Just as in [15] the Hecke modifications
are related to singular monopoles on I � C, here we will see that they also arise naturally
from non-abelian vortices over C. These vortices are the classical BPS-configurations of
a supersymmetric N = (2, 2) gauged linear sigma-model over the curve C. In particular,
through the Hecke modifications, one can establish a direct relation between the vortex
and the monopole moduli spaces.

    We start by recalling the concept of Hecke modification in the simplest setting of
GC = GL(N, C) bundles.

Definition 1.1. A Hecke modification of a holomorphic vector bundle E-  C at the
points {z1, . . . , zr}  C is a pair (E+, h) consisting of another holomorphic vector bundle
E+  C and an isomorphism

h : E-|C\{z1,...,zr} - E+|C\{z1,...,zr} .  (1)

In the particular case where E- = CN � C is trivial, giving h is the same as giving a
holomorphic trivialization of E+ over the set C \ {z1, . . . , zr}.

    Two Hecke modifications (E+, h) and (E+ , h) are considered equivalent iff there exists
a holomorphic isomorphism E+  E+ that is globally defined over C and takes h to
h. Notice that this definition of equivalence does not treat the bundles E+ and E-
symmetrically. Another important concept is that of type of the modification at a point.

Definition 1.2. A Hecke modification is said to be of type (m1, . . . , mN ) at a point zj  C
when there are local trivializations of E- and E+ with respect to which the isomorphism

                1
h can be written in a punctured neighbourhood of zj as

h(z) = A(z) diag (z - zj)m1, . . . , (z - zj)mN B(z) ,  (2)

where the square matrices A(z) and B(z) are holomorphic and invertible at the point zj.

    By convention one usually orders m1  � � �  mN . Observe also that for a local Hecke
modification factorized as above different choices of the matrix A(z) do not change the
equivalence class of the modification, for A(z) can be regarded as a local automorphism
of E+. This does not mean, however, that the inequivalent modifications of fixed type are
parameterized by B(z), essentially because the factorization (2) is not unique.

    As a final remark we remind the reader that the space of all Hecke modifications of a
rank N vector bundle at a point z0  C coincides with the affine grassmannian GrN for
the group GL(N, C), also called the loop Grassmannian (see for example [19, ch. 8] or [15,
sect. 9.3]). The spaces of modifications of fixed type then define the so-called Schubert
cells inside GrN .

2 Non-abelian vortex equations and moduli spaces

The vortex equations that we have in mind arise naturally as the classical BPS-
configurations of a N = (2, 2) supersymmetric theory in two dimensions. This theory
is a gauged linear sigma-model with group U(N) and N chiral matter fields in the funda-
mental representation. Since we want to consider BPS vortices over any Riemann surface
C, the model should be topologically A-twisted. The vortex equations then appear as
the instanton equations of the topological theory. From a geometrical perspective the
data that we need are a hermitian vector bundle E  C of rank N and degree d, a
U(N)-connection A on this bundle and a section  of the direct sum of N copies of E.
Observe that the section  can also be regarded as an ordered collection of N sections of
E, or, locally, as a function on C with values on the N � N matrices that transforms in
the fundamental representation of U(N). The vortex equations are then

�A = 0                                                  (3)

 FA - ie2 (  -  1) = 0 ,

where  is the Hodge operator on the Riemann surface and  and e2 are positive constants.
These particular equations were first studied in [5], and then with [1, 14] also appeared in
the physics literature. The first of the equations is invariant under the complexified (i.e.

        2
GL(N, C)) gauge transformations, whereas the second equation is only invariant under
the unitary, or real, gauge transformations. Also, as usual, the second vortex equation
can be formally interpreted as the vanishing condition of the moment map of the action
of the group of real gauge transformations on the space of solutions of the first vortex
equation, which as a space is an infinite-dimensional Ka�hler manifold. Then the usual
correspondence between complex and symplectic quotients says that the space of vortex
solutions modulo the real gauge transformations is isomorphic to the space of stable
solutions of just the first equation modulo the complex transformations. But a solution
of the first equation can be interpreted as a holomorphic structure on E together with
N holomorphic sections, and, crucially, stability in this case means that these N sections
should be linearly independent on the generic fibre of E [5, 6]. Thus we see that each
vortex solution determines a holomorphic structure on E together with a holomorphic
trivialization of the bundle over the curve C minus a finite set of points, and, according
to definition 1.1, this is precisely a Hecke modification of the trivial bundle over C.

    Having seen how a vortex solution naturally determines a Hecke modification, we will
now give a more detailed description of the moduli space of vortex solutions. This space
is to be later related to the space of Hecke modifications.

    The moduli space of the particular kind of non-abelian vortices that we are considering
here has been generally described in [14, 10, 4, 7]. The first two references are concerned
with vortices on the complex plane; [4, 7] also consider vortices over other surfaces, which
is the case we need here. In general, for a compact Riemann surface C of large volume
and for fixed rank and degree of E, the moduli space of solutions of (3) is known to be a
compact and smooth Ka�hler manifold. As a set, it can be described in the following way.

Definition 2.1. A vortex internal structure IN is a set of data consisting of an integer
k0  0 and a sequence (V1, . . . , Vl) of non-zero proper subspaces of CN such that Vj+1 
Vj = {0} for all indices j = 1, . . . , l - 1. The order of the internal structure IN is the
non-negative integer N k0 + l dimCVl.

Theorem 2.2 ([4]). Assume that Vol C > 2(deg E)/(e2 ) and pick any finite set

{(z1, IN1 ), . . . , (zr, INr )} of distinct points on the surface C and associated internal struc-

tures such that  r    order(INl )  =  degree  E.  Then there is  a solution  (A, )  of the non-
                 l=1

abelian vortex equations (3), unique up to gauge equivalence, such that det  has zeros

exactly at the points zj and  factorizes around each zj with internal structure INj . Fur-
thermore, all solutions of (3) with det  not identically zero are obtained in this way.

                                              3
The statement that the matrix  factorizes around a point z0  C with internal

structure IN = (k0, V1, . . . , Vl) just means that, in a neighbourhood of z0, one can write

uniquely

                   (z) = A(z) (z - z0)k0 TVl(z - z0) � � � TV1(z - z0)    (4)

for some matrix A(z) that is holomorphic and invertible around z0. Here the matrix
functions TV (z - z0) are defined as the linear maps

                   TV (z - z0) := (z - z0)V + V : CN - CN

constructed with the help of the natural projections associated with an orthogonal de-

composition CN = V  V . In order to define these decompositions, and hence the maps

TV , we need of course to choose and fix a hermitian product on CN . Theorem 2.2 is then
valid for any such choice. Observe that this product on CN is not in any way related to

the hermitian product on the fibres of the hermitian vector bundle E  C.

    Looking at the definition above, it is clear that TV (z - z0) has kernel V at z0 and
determinant (z - z0)dim V . This implies in particular that det (z) vanishes at z0 with

multiplicity equal to the order of IN . The non-intersection condition in the definition 2.1

of vortex internal structure appears because we want the factorization (4) above to be

unique. If we had allowed the vector spaces Vj to be arbitrary, it would follow for instance

from the identity

                   TV (z - z0) TV (z - z0) = (z - z0)dim V                (5)

that the uniqueness could not hold.

3 Vortex internal structures and Hecke modifications

The aim of this section is to show that the spaces of Hecke modifications at a point and
the spaces of vortex internal structures are one and the same object. This identification
provides a very palpable description � in terms of finite collections of vector spaces � of
the affine Grassmannian and its Schubert cells.

    Firstly, comparing the local factorizations (2) and (4), it is clear that any holomorphic
matrix (z) described by (4) determines a Hecke modification with m1, . . . , mN  0. As
we will see later, the values of the integers mj are related to the dimensions of the different
subspaces Vj. Moreover, since for both vortices and modifications the equivalence relation
is given by the different possible choices of the invertible matrix A(z), the uniqueness of
(4) shows that the degrees of freedom of inequivalent Hecke modifications are precisely

                                                        4
parameterized by the choices of vector spaces Vj, i.e. by the vortex internal structure
IN . The conclusion is then that the space of all local Hecke modifications with finite and
non-negative mj's is the same as the space of all different internal structures IN .

    To make the correspondence more precise, a natural question is to ask what internal
structures IN correspond to modifications of fixed type m1  � � �  mN  0. Observe
that the space of internal structures is the disjoint union of strata labeled by the integers
k0, dim V1  � � �  dim Vl, and that this is analogous to the stratification of the space
of Hecke modifications by the type of the modification. So it is natural to expect the
integers mj to be related to the dimensions of the Vj's. In fact, a careful look at the
factorizations (2) and (4) and at the way internal structures emerge in [4], shows that the
Hecke modifications of type (m1, . . . , mN ) correspond exactly to the internal structures
with

k0 = mN                           (6)

dim Vk = #{j : mj - mN - k  0} .

This formula is a dictionary between the type of the modification and the type of the
vortex internal structure. Now, it is well-known that the spaces of Hecke modifications of
fixed type are not in general compact. Moreover, in [15, Sect. 9.2], the authors describe
how it is possible to obtain a natural compactification of these spaces by completing them
with modifications of different type. Thus another reasonable question is to ask how these
compactifications look like in the vortex picture, and we now turn to this.

    Firstly, suppose that one fixes the type of the vortex internal structure, i.e. that one
fixes the dimensions of the subspaces Vj and only allows them to turn around in CN . If
all the different orientations of the Vj's were allowed, then the resulting space of internal
structures would certainly be compact � it would be a product of Grassmannians. This,
however, is not the case, because certain orientations are excluded by the non-intersection
condition imposed in definition 2.1, and so the spaces of internal structures of fixed type
are also in general non-compact. And what about their natural compactification? One
possible answer would be just to complete these spaces with the forbidden orientations
of the Vj's, and hence compactify them topologically as a product of Grassmannians. If
we do this, however, we are not completing the spaces with genuine internal structures of
different type, because formula (5) and lemma 3.2 say that there is an equivalence relation
among the forbidden orientations of the Vj's. This means that this naive compactification
cannot be the one described in [15]. Instead, looking carefully at the definitions in [15,

         5
Sect. 9.2] and using the dictionary (6) to translate the results, one can check that the

natural compactification of the space of internal structures of type (k0, dim V1, . . . , dim Vl)
is obtained by adding to it all the other internal structures (k0 , V1, . . . , Vl) of the same
order that satisfy

    dim Vr       dim Vr  for all j  N.                     (7)

rj           rj

This is the translation to the vortex picture of the compactification of the space of Hecke
modifications of type (m1, . . . , mN ). It actually corresponds to adding the forbidden
orientations of the Vj's and then quotienting by the equivalences determined by lemma
3.2. This quotient is encapsulated in the map  of the proposition below.

Proposition 3.1. For mj  0, the space Y(m1, . . . , mN ) of Hecke modifications of fixed
type is the same as the space IN (k0, . . . , kl) of vortex internal structures with dimensions
kj = dim Vj determined by (6). Moreover, the natural compactification Y(m1, . . . , mN )
described in [15, sect. 9] coincides with the space IN (k0, . . . , kl) described above in (7).
Finally, these identifications show that there exists a natural surjective map

 : Gr (k1, N ) � � � � � Gr (kl, N ) - Y(m1, . . . , mN )  (8)

that is one-to-one on the inverse image of Y(m1, . . . , mN ), which is an open dense subset
of the domain.

    The construction of the map  is quite simple and goes as follows. Let any collection
of subspaces L = (V1, . . . , Vl) be a point in the domain of . Irrespective of whether these
subspaces satisfy or not the non-intersection condition in definition 2.1, it makes sense to
consider the the linear transformations

                                        T^L(z) := TVl(z) � � � TV1(z)

for all complex z. It is clear that T^L(z) is holomorphic and that det T^L(z) has a single
zero at z = 0 of order j dim Vj. In particular, applying to T^L(z) the factorization (4),
there is a unique internal structure IN = (k0, V1, . . . , Vl) of order j dim Vj such that

                                     T^L(z) = zk0 TVl (z) � � � TV1(z) .

So we just define (L) = IN . Observe that if the subspaces Vj in the original collec-
tion L do satisfy the non-intersection condition of definition 2.1, which is the generic

                 6
case, then they already define a vortex internal structure, and so by the uniqueness of
the factorization (4) necessarily (L) = L. If on the other hand they do not satisfy
the condition, then the factorization (4) will produce a different collection of subspaces
(L) = (k0, V1, . . . , Vl) that defines a genuine internal structure, which can be recursively
determined through lemma 3.2 below. One can subsequently check that this new internal
structure belongs to the compactification Y(m1, . . . , mN ), and that all internal structures
in this compactification can be obtained in this way (for more details, including the proof
of the lemma, see [4, Sect. 4.1]).

Lemma 3.2. Let V1 and V2 be any two subspaces of CN . Then calling W the intersection
V2 V1, the linear transformations TV (z) defined in section 2 satisfy the algebraic identity

TV2 (z) TV1 (z) = TV2  W (z) TW V1(z) .  (9)

Observe moreover that the two subspaces on the right-hand side satisfy the usual non-
intersection condition, i.e. V2  W  has zero intersection with (V1  W ).

    A last observation, before we give two examples, is to note that as long as one is only
interested in the spaces of modifications Y(m1, . . . , mN ) and not on the modifications
themselves, the restriction of having mj  0 is not a serious one. This is so because the
spaces Y(m1, . . . , mN ) are invariant under a simultaneous shift mj  mj+a for any integer
a, as explained for example in [15]. One way to recognize that this is true is to consider the
standard line-bundle O(z0) over C with its standard section sz0 (which has a simple zero at
z0) and, going back to definition 1.1, to note that the map (E+, h)  (E+  O(z0)a, h sza0)
defines an invertible correspondence between the Hecke modifications of the trivial bundle
of type (m1, . . . , mN ) and the modifications of type (m1 + a, . . . , mN + a).

Two particular cases of the identifications in proposition 3.1 are the following.

� To Hecke modifications of type (a, 0, . . . , 0) correspond internal structures with k0 =
  0 and a unidimensional vector spaces V1, . . . , Va of CN . The compactification of this
  space is the space of all possible internal structures IN of order a, and the map 
  takes the product of a copies of CPN-1 onto this compactification.

� To Hecke modifications of type (1, . . . , 1, 0, . . . , 0), with k ones, correspond internal
  structures with vanishing k0, with a k-dimensional V1, and all other vector spaces
  equal to zero. These internal structures are parameterized by the Grassmannian
  Gr (k, N), which is already compact, and  is in this case the identity map.

                                                    7
    Expanding a bit on the first example, it is obvious that for a = 1 the space of all
vortex internal structures of order a is just CPN-1. For N = a = 2 the same space
was shown in [11] to be the weighted projective space W CP(1, 1, 2), which coincides with
the corresponding compactified space of modifications described in [15]. For a = 2 and
arbitrary N the spaces of internal structures can be pictured as the product CPN-1 �
CPN-1 with the diagonal collapsed into a Grassmannian Gr(2, N ) or, alternatively, as a
nice finite-dimensional quotient of a space of matrices [4, 11].

4 Vortices and singular monopoles

4.1 Identification of moduli spaces

Sections 9 and 10 of [15] give an interpretation of the Hecke modifications of a G-bundle in
terms of a three-dimensional gauge field theory. More precisely, they describe an isomor-
phism between the spaces of modifications of fixed type and a moduli space of solutions
of the Bogomolny equations over the product [t-, t+] � C with prescribed boundary con-
ditions and singularities (see also [17, 8]). In this setting, and in our case G = U(N),
one considers a hermitian vector bundle E defined over the manifold [t-, t+] � C minus a
finite set of interior points pi = (ti, zi), and takes as fields a U(N )-connection A on E and
a section  of the adjoint bundle ad E. The restriction of the bundle E to the boundary
curve C- = {t-} � C should be trivial, whereas the restriction to C+, which we call E+,
need not be. One then looks at the standard 3-dimensional Bogomolny equations

                                     FA = A                                    (10)

for the pair (A, ) on I � C \ {pi} with the boundary conditions that: (i) both A |C- and

 |C+ should be trivial and (ii) near each singularity pi the Higgs field should in some

gauge be asymptotically of the form


                 -1
(p)    2  distance(p,                  pi)  diag  [mi1,  .  .  .  ,  miN ]  .  (11)

The relation between this gauge theory problem and the Hecke modifications can then be
roughly encapsulated in the following result.

Proposition 4.1 ([15, 17]). Consider the space of solutions of the Bogomolny equations
(10) subject to the boundary conditions (i) and (ii), modulo gauge transformations on E
that are trivial on C-. If the singularities pi = (ti, zi) all have distinct zi's, then this

                                       8
moduli space is naturally isomorphic to the space of inequivalent Hecke modifications of
the trivial bundle CN � C that have type (mi1, . . . , mNi ) at the respective point zi  C.

    On the other hand, when the integers mij are all non-negative, we have seen in the
previous section that each space of Hecke modifications of fixed type coincides with a
space of vortex internal structures IN with subspaces Vj  CN of fixed dimensions. This
then means that the Bogomolny moduli space of the proposition above is just a cartesian
product of spaces of internal structures with fixed dimensions. Furthermore, from section
2 we also know that a choice of a finite number of pairs (zi, INi ) is the same thing as a
point in the moduli space of vortex solutions. The conclusion is thus that the vortex and
monopole moduli spaces are the same.

Proposition 4.2. Assume that the integers mij are all non-negative. Then the monopole
moduli space of proposition 4.1 is isomorphic to the vortex moduli space of solutions (A, )
of (3) on the bundle E+  C+ such that the matrix  factorizes around the points zi  C
according to internal structures INi with dimensions fixed by the relations (6).

Proposition 4.3. Consider the monopole moduli spaces of proposition 4.1, but leaving the
type and the precise location of the singularities unspecified, so that these are additional
moduli. Demand nonetheless that the singularities have distinct zi's and that their type
satisfies mji  0. Then the resulting monopole moduli space is a smooth complex manifold
of dimension N deg(E+) that is isomorphic to the moduli space of vortex solutions on
E+  C+ described in theorem 2.2.

    These identifications of vortex and monopole moduli spaces have been made through
the picture of the moduli spaces as complex quotients of spaces of stable solutions. Firstly,
the holomorphic structure on E+  C+ induced by a monopole connection A is used as
part of a unique stable pair (A |C+, ) that solves the first vortex equation. Secondly,
the usual the Hitchin-Kobayashi correspondence says that there exists a complex gauge
transformation on E+ that takes this stable pair to a full vortex solution of (3). The
conclusion is that the monopole connection A is related by a complex gauge transformation
on C+ to a unique vortex connection, up to real gauge transformations, and so the moduli
of the monopole theory on I �C are all encapsulated in the vortex theory on the boundary
C+.

                                                        9
5 Open questions

5.1 Are vortices boundaries of singular monopoles?

The identifications of vortex and monopole moduli spaces described in the last section
implied that the monopole connection A is related by a complex gauge transformation on
C+ to the corresponding vortex connection. Given this fact, it is natural to ask if there is
a more direct correspondence between the monopole solutions and the vortex solutions,
i.e. if the latter complex gauge transformation can in fact be a real transformation. To
see what this means, start by breaking up the Bogomolny equation (10) into components
as in [15]:

                            (FA)zz� = At  (C )zz�   (12)
                            (FA)tz = i zA
                            (FA)tz� = -i Az�  ,

where C is the Ka�hler form on the Riemann surface. Comparing (3) and (12), the
question is therefore if given a vortex solution (A, ) there is a corresponding monopole
solution satisfying the additional boundary condition

tA =? ie2 (  -  1) on C+ .                          (13)

This monopole solution would then necessarily be unique up to real gauge transformations
that are trivial on both boundaries.

    In general one should not expect (13) to be true. One reason is that in the monopole
moduli space of proposition 4.1 the coordinates ti of the singularities are not specified,
and different choices of ti should produce monopole solutions which are not real gauge
equivalent on C+, and so cannot all be real gauge equivalent to any given vortex solution.
It is tempting, nevertheless, to imagine that if we are considering a single monopole
singularity, or if all the ti's are chosen with the same value � say equal to t0  (t-, t+) �
then the answer to (13) could be affirmative. In this case the only value of the parameter
 for which this could possibly be true would be a function of the position of t0 in the
interval (t-, t+), and it would be interesting to find what this function is. An alternative
approach1, would be to scrap the original Dirichlet boundary condition  |C+ = 0 of
section 4, substitute it by the inhomogeneous Neumann condition (13), and then see if
each vortex solution on C+ determines in this way to a unique monopole solution on the
bulk with the prescribed singularities.

1suggested by Nuno Roma~o.

                            10
5.2 Meromorphic vortices

Another natural question is whether it is possible to eliminate from proposition 4.2 the
bothersome condition mij  0. As explained in [15] and in section 3, as long as one is
only interested in the spaces of modifications and not in the modifications themselves,
or in the monopole moduli spaces and not in the monopole solutions themselves, this
restriction of having non-negative mj's does not lead to any loss of generality, since all
these spaces are isomorphic under a simultaneous shift of the mj's by an arbitrary constant
integer. However, when one starts trying to relate concrete monopole solutions and Hecke
modifications to concrete vortex solutions on C+, it is clear that this is not directly
possible with negative mj's, because so far we have assumed that in a vortex solution the
section  is holomorphic, and comparing (2) with (4), a Hecke modification with negative
mj's clearly demands that we allow vortex solutions with meromorphic  as well. Thus
one possible strategy to eliminate the restriction on the mj's is just that: to consider
meromorphic solutions of (3) and then work to see if the usual correspondence between
full vortex solutions and stable solutions of �A = 0 still holds in the meromorphic setting.
An alternative method would be to stick with the manifestly holomorphic sections and
assume instead that  has values in some compactification of the space of N �N matrices.
One can then subsequently use the Hitchin-Kobayashi correspondence of [18] to relate
stable sections with vortex solutions. The latter method works at least in the simple
G = U(1) example. In this case E+ is a principal U(1)-bundle and the target of the
section  is taken to be CP1 with the standard circle action. Then the moduli space of
solutions of the corresponding vortex equations is basically just the space of divisors on
C+ [21, 3], and, as desired, it coincides with the space of Hecke modifications of the trivial
line-bundle on C, with no restriction on the mi's.

    Understanding the vortices related to Hecke modifications with arbitrary mji is also
relevant to the vortex/modification correspondence for groups G other than U(N). For
instance the Hecke modifications for G = SU(N) are the same as those for U(N) with just
the additional constraint j mj = 0, which if it is to be non-trivial requires also negative
mj's. Vortices with different groups G have been studied for example in [2, 18, 3, 12].

5.3 Hanany-Tong construction versus Nahm equations with sin-
       gularities

The relations between the vortex and monopole moduli spaces described in section 4
ought to be visible as well after performing ADHM-like transformations. For the case of

                                                       11
non-abelian vortices on the complex plane C = C, in the article [14] Hanany and Tong
used D-branes to produce a description of the vortex moduli spaces as finite-dimensional
symplectic quotients of matrix spaces, a result analogous to the ADHM quotients for
instantons. This description was then more explicitly related to the vortex solutions
in [10]. On the other hand it is well-known that monopoles with singularities can be
described by singular solutions of Nahm's equations [9, 16, 20]. It then seems natural to
ask whether one can directly relate the symplectic quotients of [14] to the moduli spaces
of singular solutions of Nahm's equations.

Acknowledgements. I would like to thank Nuno Roma~o for comments on the first
version of this manuscript. I am partially supported by the Netherlands Organisation for
Scientific Research (NWO) through the Veni grant 639.031.616.

References

 [1] R. Auzzi, S. Bolognesi, J. Evslin, K. Konishi and A. Yung : `Nonabelian Super-
      conductors: Vortices and Confinement in N = 2 SQCD'; Nucl. Phys. B673 (2003),
      187�216.

 [2] D. Banfield : `Stable pairs and principal bundles'; Q. J. Math. 51 (2000), 417�436.
 [3] J.M. Baptista : `Vortex equations in abelian gauged sigma-models'; Commun. Math.

      Phys. 261 (2006), 161�194.
 [4] J.M. Baptista : `Non-abelian vortices on compact Riemann surfaces'; Commun.

      Math. Phys. 291 (2009), 799�812.
 [5] A. Bertram, G. Daskalopoulos and R. Wentworth : `Gromov invariants for holomor-

      phic maps from Riemann surfaces to grassmannians'; J. Amer. Math. Soc. 9 (1996),
      529�571.
 [6] S. Bradlow, G. Daskalopoulos, O. Garc�ia-Prada, R. Wentworth : `Stable augmented
      bundles over Riemann surfaces'; in "Vector bundles in algebraic geometry", London
      Math. Soc. Lecture Note Ser. 208, CUP, Cambridge, 1995, 15�67.
 [7] I. Biswas and N. Roma~o : `Moduli of vortices and Grassmann manifolds'; in prepa-
      ration.
 [8] B. Charbonneau and J. Hurtubise : `Singular Hermitian-Einstein monopoles on the
      product of a circle and a Riemann surface'; arXiv: 0812.0221.

                                                       12
 [9] S. Cherkis and B. Durcan : `Singular monopoles via the Nahm transform'; JHEP
      0804 (2008), 070.

[10] M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Moduli space of non-abelian
      vortices'; Phys. Rev. Lett. 96 (2006), 161601.
      M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Solitons in the Higgs phase
      � the moduli matrix approach �'; J. Phys. A39 (2006), R315�R392.

[11] M. Eto, K. Konishi, G. Marmorini, M. Nitta, K. Ohashi, W. Vinci and N. Yokoi :
      `Non-abelian vortices of higher winding numbers'; Phys. Rev. D74 (2006), 065021.

[12] M. Eto, T. Fujimori, S. Gudnason, K. Konishi, T. Nagashima, M. Nitta, K. Ohashi
      and W. Vinci: `Non-abelian vortices in SO(N) and USp(N) gauge theories'; JHEP
      0906 (2009), 004.

[13] E. Frenkel : `Gauge theory and Langlands duality'; arXiv: 0906.2747.
[14] A. Hanany and D. Tong : `Vortices, instantons and branes'; JHEP 0307 (2003) 037.
[15] A. Kapustin and E. Witten : `Electric-magnetic duality and the geometric Langlands

      program'; arXiv: 0604151.
[16] P. Kronheimer : `Instantons and the geometry of the nilpotent variety'; J. Differential

      Geom. 32 (1990), 473�490.
[17] P. Norbury : `Magnetic monopoles on manifolds with boundary'; arXiv: 0804.3649.
[18] I. Mundet i Riera : `A Hitchin-Kobayashi correspondence for Ka�hler fibrations'; J.

      Reine Angew. Math. 528 (2000), 41�80.
[19] A. Pressley and G. Segal : `Loop groups'; Oxford University Press, 1986.
[20] E Witten : `Geometric Langlands and the equations of Nahm and Bogomolny ';

      arXiv: 0905.4795.
[21] Y. Yang : `Solitons in field theory and nonlinear analysis'; Springer-Verlag, New

      York, 2001.

                                                       13
