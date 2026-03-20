# Baptista HD Routes Fermions 2021

**Source:** `05_Baptista_HD_Routes_Fermions_2021.pdf`

---

arXiv:2105.02901v1 [hep-th] 6 May 2021               Higher-dimensional routes
                                                 to the Standard Model fermions

                                                                              Jo~ao Baptista

                                                                                 May 2021

                                                                                 Abstract

                                        In the old spirit of Kaluza-Klein, we consider a spacetime of the form P = M4 � K,
                                        where K is the Lie group SU(3) equipped with a left-invariant metric that is not fully
                                        right-invariant. We observe that a complete generation of fermionic fields can be encoded
                                        in the 64 components of a single spinor over the 12-dimensional spacetime. The behaviour
                                        of the spinorial function along the internal space K can be chosen so that, after pairing
                                        and fibre-integration over K, the resulting Dirac kinetic terms in four dimensions couple
                                        to the u(1)  su(2)  su(3) gauge fields in the exact chiral representations present in the
                                        Standard Model. Although we describe the action of the internal Dirac operator on the
                                        12-dimensional spinor, the full calculation of the fermionic mass terms produced by the
                                        model is longer and is not carried out here. We calculate instead the action of the internal
                                        Laplace operator on the spinor components.
Contents

1 Introduction                          3

2 Spinorial functions on M4 � K         7

12-dimensional gamma matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

Spinor behaviour along the internal space K . . . . . . . . . . . . . . . . . . . . 9

Gauge representations induced in four dimensions . . . . . . . . . . . . . . . . . 11

Components D�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Components b�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
Components c�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
Components a�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
Bringing the components together . . . . . . . . . . . . . . . . . . . . . . . 18

Charges and coupling constants . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

Electromagnetic charges . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

Gauge coupling constants . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

Uniqueness of the spinor vertical behaviour . . . . . . . . . . . . . . . . . . . . . 28

3 Masses induced in four dimensions     32

Mass in Kaluza-Klein theories . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

Fermion masses from the internal Dirac operator . . . . . . . . . . . . . . . . . 33

Masses from the internal Laplace operator . . . . . . . . . . . . . . . . . . . . . 35

Components D�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
Components b�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
Components c�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Components a�(x, h) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

Appendices                              41

A Integrals on SU(3)                    41

A.1 Integrals of general polynomials in hk1 and hj1 . . . . . . . . . . . . . . . . 41
A.2 Integrals of fourth order monomials hkj hmn hkj hmn . . . . . . . . . . . . 44

                                     1
A.3 Integrals of functions of the form q(h) h v h . . . . . . . . . . . . . . . . . 45
A.4 Integrals involving the functions s(h) . . . . . . . . . . . . . . . . . . . . . 47

B Laplacian of equivariant functions on SU(3)  51

C HDR to special relativity                    55

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
aspects of the Kaluza-Klein framework. The companion study [Ba] suggest that, besides
the curvature |FA|2 of the gauge fields, there are other natural objets in a Riemannian
submersion that resemble the field content of the Standard Model. When the fibre K is a
Lie group equipped with a left-invariant metric, the second fundamental form of the fibres
generates terms in the four-dimensional Lagrangian sharing notable similarities with the

                                                        3
covariant derivative of a Higgs field, including quadratic terms in the gauge fields that
generate the gauge bosons' mass. When K is chosen to be the group SU(3) equipped with
a specific family of left-invariant metrics, denoted by g, then the terms generated by the
second fundamental form contain the precise covariant derivative dA that appears in the
Standard Model, namely a C2-valued Higgs field coupled to the electroweak gauge fields
through the correct representation.

    In the present study we suggest ways to integrate fermions into this picture. For an
internal space K = SU(3), we regard fermions as spinorial functions on the 12-dimensional
spacetime M4 � K with a prescribed behaviour along K. A complete generation of
fermionic fields can then be encoded in the 64 complex components of a single higher-
dimensional spinor. Moreover, the vertical behaviour of this spinor can be chosen so that,
after fibre-integration over K, the resulting Dirac kinetic terms in four dimensions couple
to the u(1)  su(2)  su(3) gauge fields in the exact chiral representations present in the
Standard Model. Perhaps one could think of the prescribed vertical behaviour as a sort
of elementary, spinorial oscillation along the compact direction K.

Spinorial functions and fermionic gauge couplings

This second part of the Introduction gives a brief description of the calculations underlying
the present study. Spinorial functions on the 12-dimensional spacetime P = M4 � K can
be regarded as functions  with values on a 64-dimensional complex vector space 12
equipped with a hermitian pairing 1, 2  Tr(12). This identification uses the
fact that Lie groups, such as K and M4 � K, have trivial tangent and spin bundles. In
addition, spin structures are unique on simply connected spaces.

    In the usual Kaluza-Klein setting, one considers the action of the higher-dimensional
Dirac operator D/ on spinorial functions. If {Xa} = {X�H, Xj} denotes an orthonormal
basis of the tangent space to P , where the Xj are vectors tangent to K and the X�H are
the horizontal lifts of vectors X� tangent to M4, then we can schematically write the Dirac
operator on P as

        11          3                              11

D/  :=       a a =        � LX�H  +                     j Xj  .  (1.1)

        a=0         �=0                            j=4

Here the a are a set of (11, 1)-dimensional gamma matrices and we have used the triviality

of the Levi-Civita connection on Minkowski space to replace X�H with the Lie derivative
LX�H. A scalar density on P can be obtained through the Dirac pairing of spinors,

0, D/  =        0�, LX�H +                         0j, Xj  ,     (1.2)

             �              j

                       4
where we have used standard hermiticity properties of the gamma matrices (signs may
depend on the conventions). Now, by definition of the higher-dimensional metric gP (see
section 3 of [Ba]), the horizontal lift to P of a vector X� tangent to M4 is given by

X�H := X� + ALj (X�) ejL - AjR(X�) eRj ,                       (1.3)

where AL and AR are one-forms on M4 with values in the Lie algebra su(3); the vectors
{ej} form a basis of su(3); the symbols eLj and eRj denote the extensions of ej as a left or
right-invariant vector field on K = SU(3), respectively. In particular, the kinetic terms

that appear in the first sum of the scalar density have the form

0�, LX�H = 0�, � + AjL(X�) LeLj  - ARj (X�) LejR .             (1.4)

Thus, the coupling of the 12-dimensional spinor  to the gauge fields on M4 is determined
by the Lie derivatives of  along the left and right-invariant vector fields on K.

    Although simple enough, the previous reasoning seems headed towards an apparent

contradiction with a basic property of the Standard Model, namely the fact that leptons do
not couple to the strong force, mediated by the gauge fields that here are called AjR(X�).
Having (1.4) in mind, this property should mean that the Lie derivatives LeRj  of the
leptonic components of  are identically zero. Since this happens for all right-invariant

fields ejR, it follows that these components are invariant functions under left-multiplication
on the group K, i.e. they are simply constant on K. But constant functions on K also

have vanishing derivatives along all left-invariant vector fields ejL, and hence the leptonic
components of  should not couple to the electroweak gauge fields AjL(X�) either, which
is not true.

The gap in the previous argument comes from looking at expression (1.4) and assuming

that the Lie derivatives LeRj  must all vanish when the leptonic component of  do
not couple to the fields AjR(X�). In reality, these derivatives may perfectly well have
plenty of non-zero terms, as long as they integrate to zero along the fibres K, since the

fermionic gauge representations in the four-dimensional Lagrangian are obtained only

after projecting the scalar density (1.4) from M4 � K down to M4. Schematically, down
in four dimensions the couplings of fermions to the fields ARj (X�) should be determined

by the integrals

                                          K 0�, LeRj  volK ,   (1.5)
and similarly for the couplings to the ALj (X�) gauge fields.

    The main purpose of this study is to search for the appropriate spinorial functions
P (x, h), defined on the higher-dimensional spacetime M4 � SU(3), such that the scalar
integrals (1.5) produce the exact fermionic gauge representations present in the Standard

5
Model. More precisely, given a function (x) on M4 with values in 12, we can extend
it to a function P (x, h) on the whole P through a simple "separation of variables"

prescription:

               P (x, h) := S(h) (x) ,                              (1.6)

for all points (x, h) in M4 � K, where S(h) : 12  12 is a linear transformation that
depends smoothly on the point h  K. For spinorial functions of this sort, expansion
(1.3) implies that

               LX�H P = S � + ALj (X�) LejLS  - ARj (X�) LejRS  ,  (1.7)

which is again a function on M4 � K with values on 12. Remarkably, one can then show
that for a relatively simple choice of vertical transformations S(h), the scalar density in
four dimensions obtained after fibre-integration,

                      3  0� P , LX�H P  volK ,                     (1.8)
               K �=0

contains all the kinetic terms present in the Standard Model Lagrangian for one generation
of fermions. This includes the correct hypercharges and gauge representations for all the
leptons and quarks, right-handed and left-handed, particles and anti-particles. All this
information is encoded in the single 12-dimensional spinor P (x, h).

    The next section of this study is dedicated to the definition of the spinor's vertical
transformation S(h) and to the calculation of the gauge representations induced in four
dimensions, after the fibre-integrals (1.8). It is the main section of this study. In section 3
we discuss the action of the internal Dirac and Laplace operators on the spinor P (x, h),
as they are a natural source of fermionic mass terms in the model. The four-dimensional
mass terms induced by this action are explicitly calculated only in the case of the Laplace
operator. In the more pertinent case of the internal Dirac operator, the calculations are
significantly more evolved and are not carried out here. The discussion in this study also
does not encompass the fundamental quantum aspects of the Standard Model.

                         6
2 Spinorial functions on M4 � K

The 12-dimensional gamma matrices

To compare the fibre-integrals (1.8) with the usual kinetic terms of four-dimensional

fermions, we want to find a representation of the 12-dimensional gamma matrices � in

terms of the more familiar Pauli matrices � and four-dimensional gamma matrices �.

Start by identifying the 64-dimensional spinor space 12 with the space of 8 � 8 complex

matrices,

                            12  M8�8(C) .                        (2.1)

Now consider the three Pauli matrices:

            1 = 0 1         2 = 0 -i             3 = 1 0 ,       (2.2)
                      10              i0                   0 -1

satisfying the relations ab = abI2 + i c abcc, and choose a set of four-dimensional
gamma matrices � on Minkowski space equipped with the metric  = diag(-1, 1, 1, 1).

We use the mathematical convention where gamma matrices in space dimensions are

anti-hermitian and correspond to square roots of -1, so that

            �,  = -2 � I4               (0) = 0   (l) = -l ,     (2.3)

for l = 1, 2, 3. The corresponding gamma matrices in four-dimensional Euclidian space

are defined by El = l, for l = 1, 2, 3, and by E4 = i0. It follows that all the Ek are

anti-hermitian and satisfy

                            Ek , El = -2 kl I4 .                 (2.4)

Then the Euclidian operator Ek k is formally self-adjoint with respect to the pairing of
spinors ,  = , while the operator i� � on Minkowski space is formally self-

adjoint with respect to the pairing 0,  . The chiral operator in four dimensions is

defined by

            5 := i 0 1 2 3 = - E1 E2 E3 E4 =: E5 .               (2.5)

Since it coincides in Euclidian and Lorentzian signatures, we will refer to it simply as 5.

It is represented by a hermitian matrix that anti-commutes with all the � and Ek and
satisfies 55 = I4.

    To build the 12-dimensional gamma matrices a out of four-dimensional blocks, we
use the standard Kronecker (tensor) product of matrices. It can be applied to matrices

                                        7
of any dimensions and is defined by

                         a11B � � � a1m B 

AB                  :=    ...  ...   ...        Mmn�mn (C) ,                (2.6)


                          a1mB � � � amm B

where A and B have dimensions m � m and n � n, respectively. It is an associative

product satisfying

                    (A  B) (C  D) = (A C)  (B D)                            (2.7)

                               (A  B) = A  B

                          det(A  B) = (det A)n (det B)m ,

where the last property makes sense only when A and B are square matrices.

    With these pieces in place, we can write down the following set of (11, 1)-dimensional
gamma matrices:

0  = 0  I2                                                                  (2.8)
b  = 05  b 
                                                           b = 1, 2, 3

3+k  = 5  I2  I2  Ek                                       k = 1, 2, 3, 4

7+l  = El E4  I2  3  5                                     l = 1, 2, 3

11  = 5  I2  i2  5 .

These formulae define the action of a on the 8 � 8 matrix  through right and left-

multiplication of  by matrices of the same dimension, which themselves are built out of

2 and 4-dimensional blocks using the Kronecker product. Using the properties of the , E
and  matrices one can readily check that 0 is a hermitian operator with respect to the
pairing 1, 2  Tr(12) in spinor space 12, while all the other a are anti-hermitian.
Furthermore, they satisfy the Clifford relation

a, b = -2 ab I                                 a, b  {0, 1, . . . , 11} ,   (2.9)

as operators on 12, where  is the Lorentzian metric with signature (- + � � � +). Thus,
the gamma matrices define unitary transformations on spinor space. An application of
the properties of the Kronecker product shows that all the a have determinant equal to
one, and therefore are elements of SU(12). Composing the a in sequence, one can also
check that

              i 0 1 2 3  = 5  I2                                            (2.10)
            4 5 � � � 11  = -  1  5
^  := i 0 1 � � � 11  = - 5  I2  1  5 ,

                                          8
where ^ is the chiral operator in (11, 1) dimensions. Decomposing the 8 � 8 matrix  into

four blocks,

               = B1 B2 ,                       (2.11)
                        B3 B4

each of them a 4 � 4 matrix, the first relation in (2.10) implies that blocks B1 and B2 have

"four-dimensional chirality" with opposite sign to that of the bottom blocks B3 and B4,
as determined by the four-dimensional operator 5 = diag(I2, -I2). The 12-dimensional
chiral operator ^, on the other hand, acts on 12 as

              ^  = -B2 5 -B1 5 .               (2.12)
                            B4 5 B3 5

It is clear that ^ ^ = I and that ^ is a hermitian operator with respect to the pairing
Tr(12) on 12. Further ahead, we will establish a correspondence between the entries
of  and the different fermions in the Standard Model. The action of ^ on  will then

correspond to an exchange of particles and anti-particles.

    The explicit formulae for the 12-dimensional gamma matrices allow us to write a for-
mula for the product 0 �, appearing in (1.8), in terms of the lower-dimensional gamma
matrices. From definition (2.8) it is clear that 0 0 = I8 while 0 b = 5  b for
b = 1, 2, 3. Abbreviating ~� := 0 �, we therefore have a four-vector of 8 � 8 matrices,

(~�) 0�3 = (0 �) 0�3 = I8, 5  1, 5  2, 5  2 .  (2.13)

When applied to a spinor   12, as in the Lagrangian density (1.8), this four-vector
describes how the Pauli matrices b act differently on the components of  corresponding
to different eigenspaces of 5, i.e. how the b act differently on left-handed and right-

handed Weyl spinors.

Spinor behaviour along the internal space K

Having laid out some algebraic requisites to manipulate spinors   12, now we want
to define the prescription for the K-dependence of the functions P (x, h) that produces
the correct gauge representations for four-dimensional fermions. To begin with, write the
8 � 8 matrix  as a juxtaposition of two 8 � 4 complex matrices �,

               = + - .                         (2.14)

Each of these two components will have a different (in fact, complex conjugate) depen-
dence on the K-coordinate h. They will correspond to the particle and anti-particle

              9
fermionic representations, respectively. Now consider the map S : SU(3)  M4�4(C)

defined by

                     S(h) :=             s(h)     ,                         (2.15)

                                               h

where h is in SU(3) and the complex number s(h) is determined by the scalar function

on the group

                                                     =       hT h 11     .  (2.16)
              s(h) := 2 (h11)2 + (h21)2 + (h31)2          2

Here we have labelled as hkj the entries of the square matrix h. Then, given any spinorial
function (x) on M4, we extend it to the full spacetime P by

P (x, h) :=          S(h)  I2 +(x) S(h)           S(h)  I2 -(x) S(h) . (2.17)

Since S(h) is a 4 � 4 matrix, the product S(h)  I2 is 8 � 8 and � are 8 � 4 matrices,
all multiplications above are well defined. The symbol S(h) denotes the complex conju-
gate of S(h), not the hermitian conjugate nor the inverse matrix; therefore, the vertical

transformation of � does not follow a SU(3)-representation as h varies.

To descend into more detail without overburdening the notation, we will write the

8 � 4 matrices � as

                     � =                a� cT�                              (2.18)
                                        b� D�

and regard them as 4 � 4 matrices whose entries are two-component Weyl spinors. Thus,

a� are simple Weyl spinors; b� and c� are 3-vectors of Weyl spinors; and D� are 3 � 3
matrices of such spinors. This notation is analogous to the usual way of writing a Dirac
spinor in four dimensions as [R L]T , i.e. as a 2-vector whose entries are Weyl spinors.
With these conventions, the vertical transformations of the components of P (x, h) along
K, as determined by rule (2.17), can be written as

            aP�(x, h) = s(h) 2 a�(x)                                        (2.19)
             b+P (x, h) = s(h) h b+(x)
             c+P (x, h) = s(h) h c+(x)          bP-(x, h) = s(h) h b-(x)
            D+P (x, h) = h D+(x) h              c-P (x, h) = s(h) hT c-(x)
                                               D-P (x, h) = h D-(x) h ,

where hT and h denote the transpose and complex conjugate matrices of h, respectively.
It is implicit in these formulae that when a matrix h of SU(3) multiplies the vectors b�
and c�, or the matrices D�, it produces a linear mix of their entries (which are Weyl
spinors) but does not act inside the two-component Weyl spinors themselves. A more

                                        10
complete notation would be to write (h  I2) b+ instead of h b+, for instance, but this
would make the formulae ahead somewhat less transparent.

    Consider again the main scalar Lagrangian density (1.8). Since the pairing 1, 2 is
just the matrix trace Tr(12), it is clear that the decomposition P = +P -P leads
to a simple sum of traces

                3   0�+    P         +P   + Tr           0�-     P         -P   volK .
                                                                                    (2.20)
                Tr             LX�H                                  LX�H

      K �=0

The decomposition of � into components a, b, c and D will further break these two big
traces into a sum of traces of the smaller components, leading to integrals of the general

form

                              Tr     D2P  L         D1P  volK ,                 (2.21)
                                               X�H
                           K

and analogous integrals for the remaining components a, b and c. Here we have used

two different generic matrices D1 and D2 to account for the fact that, inside the traces
in (2.20), one of the � appears multiplied by 0� while the other does not. It is also
implicit that both matrices DjP (x, h) transform along K according to the rules (2.19).

    Recalling expression (1.3) for the horizontal vector fields X�H in terms of the gauge
fields ALj (X�) and ARj (X�) on M4, the overall conclusion of the previous observations is

that, in order to obtain the couplings of the gauge fields to the different components of

the spinor   12, we will have to calculate several fibre-integrals of the form

         Tr D2P  LvL D1P      volK                     Tr D2P  LvR D1P volK ,

      K                                             K

where v is any vector in the Lie algebra su(3); vL and vR denote the extension of v

to a left and right-invariant vector field on SU(3); and the matrix functions DjP (x, h)
behave along K according to (2.19). Analogous integrals should be calculated for the

other components aP , bP and cP of �P . These calculations will reveal the correspondence
between the components of P and the fermions of the Standard Model. It will be the

work of the next section.

Gauge representations induced in four dimensions

Components D�(x, h)

We start by describing the procedure in detail in the simplest example: the matrix com-
ponents D� of �. Simplifying the notation of (2.19) for the case D+, we write

                                  DP (h) = h D h ,                              (2.22)

                                          11
where it is implicit that the 3 �3 matrix D may depend on the coordinate x. Let v denote
any vector in su(3) and let vL and vR denote its extension as left and right-invariant vector
fields on SU(3). Then the Lie derivatives of DP along these fields are simple enough:

           LvL DP  (h)  =  d   DP  h � exp(tv)  |t=0  =  hvDh + hDhv            (2.23)
                           dt

           LvR DP  (h)  =  d   DP  exp(tv) � h  |t=0  =  vhDh + hDvh .
                           dt

As usual, one should be aware that the flux associated to a left-invariant field vL on a
group K is given by right-multiplication by exp(tv), and vice-versa for the fields vR. If
we have two matrix functions D1P and D2P , it is possible to construct the pairing

           Tr D2P  LvL D1P            = Tr D2 v D1 + D2 D1 h v hT               (2.24)

           Tr D2P  LvR D1P            = Tr D2 h v h D1 + D2 D1 v ,

where hT = h denotes the transpose matrix and we used the cyclic properties of the trace.

Integrating along the fibre K = SU(3) equipped with a bi-invariant volume form volK
leads to a significant simplification, since it can be shown that (see (A.7) and subsequent

comments)

                           h v hT volK =          h v h volK = 0                (2.25)

                   hK                         hK

for any traceless matrix v  su(3). Thus, we get the simpler expressions

K  Tr D2P  LvL D1P volK = Tr D2 v D1 (Vol K) =                K  Tr D2P  v D1 P volK

K  Tr D2P  LvRD1P volK = Tr D2 D1 v (Vol K) =                 K  Tr D2P  D1 v P volK .

It therefore seems that, after pairing and fibre-integration, taking the Lie derivative LvLD1P
looks just like multiplying D1 on the left by the matrix v, while the derivative LvRD1P
looks like (D1 v P . Combining these results with decomposition (1.3) of horizontal fields
X�H on P , we get the nice expression

              Tr D2P  LX�H D1P volK = Tr D2 �AD1 (Vol K) ,                      (2.26)
                                                                                (2.27)
           K

where we have abbreviated

                                   4                     8

           �AD1 := �D1 +              ALj (X�) ej D1 -        ARj (X�) D1 ej .

                               j=1                       j=1

Recall from section 3 of [Ba] that {ej} denotes a basis of matrices of su(3) such that the
subset {ej : 1  j  4} spans the subalgebra (u(2)) inside su(3). Therefore, we conclude

                                          12
that the gauge fields on M4 couple to the 3 � 3 matrix function D1(x) in a rather simple
form, after the fibre-integrals kill half of the terms coming from (2.23). Let us look at
this coupling in more detail by decomposing the matrix D1 into its three lines:

                 u1T 

      D1     =      uT2                                              (2.28)


                    u3T

with ua  C3. Since the matrices ej are anti-hermitian, we have that

      uTa ej = ej ua T = - ej ua T .                                 (2.29)

Thus, the gauge fields AjR(X�) in (2.27), which according to [Ba] can be identified with
the strong force fields, act on the vector ua through simple left-multiplication ua  ejua
by the corresponding matrix in the su(3) basis. At the Lie algebra level, this is the action
corresponding to the fundamental representation of SU(3) on C3. Therefore, the three
lines of D1(x) couple to the fields AjR(X�) just as quarks couple to gluons in the Standard
Model.

    To analyze the coupling to D1(x) of the fields AjL(X�), which according to [Ba] can
be identified with the electroweak fields, recall that the subspace (u(2)) of su(3) spanned
the basis subset {ej : 1  j  4} consists of matrices of the form

      (a) =  - Tr(a)           ,                                     (2.30)

                           a

with a  u(2). The terms associated with AjL(X�) in the covariant derivative (2.27) say
that these matrices act on D1(x) simply by left-multiplication (a) D1(x). In particular,
when a is in the smaller subspace su(2)  u(2), i.e. when Tr(a) = 0, we recognize that
the corresponding gauge field ALj (X�) does not couple to the first line of D1(x), while it
mixes the second and third lines as in the fundamental SU(2)-action on this doublet of

3-vectors. Finally, when a is the diagonal generator of the subspace u(1)  u(2), that is

when

      (a) =  -2 i                 ,                                  (2.31)

                          iI2

with   R, formula (2.27) for the covariant derivative tells us that the hypercharge

associated to the first line of D1(x) is minus twice the hypercharge associated to the
second and third lines.

    Comparing with a table of fermionic representations in the Standard Model [BH, Ham],
we recognize that the gauge couplings of D1(x) fit very well if we identify its first line

                13
with the right-handed down quark dR and its second and third lines with the doublet of
left-handed up and down quarks, to exemplify with the first fermionic generation only.
Thus, the behaviour of D+P (x, h) along K prescribed by rule (2.17) originates the correct
strong and electroweak gauge representations if we identify the lines of this 3 � 3 matrix
with quark fields according to

                                                 dR(x)T 

                                     D+(x)   =      uL(x)T      .                            (2.32)


                                                    dL(x)T

A similar procedure can be used to analyze the behaviour along K of the components
D-(x) of -, as determined by the transformation rule (2.19). It leads to an identification
analogous to (2.32), but with the particle fields on the right-hand side exchanged by the
corresponding antiparticle fields.

Components b�(x, h)

We will analyze the behaviour along K of the components bP+(x, h) of the matrix +P , as
defined in (2.19). In simplified notation, this behaviour is

                                     bP+(x, h) = s(h) h b ,                                  (2.33)

where h  SU(3) and it is implicit that the vector b  C3 may depend on the coordinate x
of Minkowski space. The Lie derivatives of bP along left and right-invariant vector fields
on K are

                                LvL bP = LvL s h b + s(h) h v b                              (2.34)
                                LvR bP = LvR s h b + s(h) v h b ,

for any matrix v in su(3). If we have two vectorial functions b1P and b2P , it is possible to
take the hermitian products

                      b2P  LvL b1P = s LvL s b2 b1 + |s|2 b2 v b1                            (2.35)

                      b2P  LvR bP1 = s LvR s b2 b1 + |s|2 b2 h v h b1 .

Using  the  explicit  form  of  the  scalar  function  s(h)  =       (hT  h)11  defined  in  (2.16),  one
                                                                  2

can readily calculate that

                                                                                             (2.36)
       LvL s (h) = 2 2 (hT h v)11                      LvR s (h) = 2 2 (hT v h)11 .

                                                14
But the integrals (A.20), (A.23) and (A.24) calculated in appendix A.4 say that

      s LvR s volK = 0 =          |s|2 h v h volK                                (2.37)

   K                         K

      s LvL s volK = 2 v11 |s|2 volK ,

   K                         K

for any v  su(3) and any bi-invariant volume form volK on the group K = SU(3). This
produces a significant simplification of the integrals of the hermitian products,

K  b2P  LvL bP1 volK = b2 (2 v11I3 + v) b1 |s|2 volK
                                                             K

    bP2  LvR b1P volK = 0 .                                                      (2.38)

K

Having in mind decomposition (1.3), expressing the horizontal lift of X� in terms of the
gauge fields Aj(X�) on M4, we get that

                              b2P  LX�H bP1 volK = b2 A� b1    |s|2 volK ,       (2.39)

                                      K                      K

where we have abbreviated

                4

A� b1 := �b1 +        AjL(X�) 2 ej )11 I3 + ej b1 ,                              (2.40)

                j=1

which is a function on M4 with values in C3. The first conclusion is that the gauge fields
ARj (X�), representing the strong force, do not couple to the components of the 3-vector
b1(x). So these components must represent leptonic fields.

    To analyze the coupling of the fields AjL(X�) to b1(x), recall that the vectors {ej : 1 
j  4} span the subspace (u(2)) of su(3) consisting of block-diagonal matrices of the
form (a) = diag - Tr(a), a , with a  u(2). For matrices with this structure we have

2 (a) ]11 I3 + (a) =   -3 Tr(a)                        .                         (2.41)
                                  a - 2 Tr(a)I2

In particular, when a is in the subspace su(2)  u(2), i.e. when Tr(a) = 0, we see that
the gauge field AjL(X�) corresponding to ej = (a) does not couple to the top scalar
component of b1(x)  C3, while it mixes the second and third components as in the
fundamental SU(2)-action on this doublet. On the other hand, when a = diag(i, i)

is a generator of the diagonal subspace u(1)  u(2), we have that (a) = e1 is just the
diagonal matrix diag(-2i, i, i) in su(3), and thus

   2 e1 )11 I3 + e1 =      -6  i                .                                (2.42)
                                  -3  i I2

                       15
Inserting this result into formula (2.40) for the covariant derivative and comparing with a

table of fermionic representations in the Standard Model [BH, Ham], we see that the gauge
field A1L(X�) corresponding to the basis vector e1 couples to the top component of b(x)
just like the Standard Model's subgroup U(1)Y couples to the right-handed electron field
e-R, whereas the coupling of AL1 (X�) to the second and third components of b(x) is like the
coupling of U(1)Y to the doublet formed by the left-handed electron and electron-neutrino.
The conclusion is that the behaviour of the components bP+(x, h) along K prescribed by
(2.17) originates the correct strong and electroweak gauge representations if we identify

                                      e-R (x) 

                        b+(x)     =      L(x)        .      (2.43)


                                         e-L (x)

A similar analysis applied to the component b-(x) of - leads to an identification anal-
ogous to (2.43), but with the particle fields on the right-hand side exchanged by the
corresponding antiparticles.

Components c�(x, h)

The vertical behaviour along K of the components c�(x, h) of +P , as defined in (2.19),
can be written in simplified notation as

                        cP+(x, h) = s(h) h c ,              (2.44)

being implicit that the vector c  C3 may depend on the coordinate x of M4. The Lie
derivatives of cP along left and right-invariant vector fields on K are

                        LvL cP =  LvL s h c - s v h c       (2.45)
                        LvR cP =  LvR s h c - s h v c ,

for any matrix v in su(3). If we have two vectorial functions cP1 and c2P , it is possible to
take the hermitian products

cP2  LvL cP1            = s LvL s c2 c1 - |s|2 c2 h v h c1  (2.46)
c2P  LvR cP1            = s LvR s c2 c1 - |s|2 c2 v c1 .

Complex conjugation of functions commutes with Lie derivatives and integration over K,
so the integrals in (2.37) imply that

                        s LvR s volK = 0                    (2.47)

                     K

                        s LvL s volK = -2 v11 |s|2 volK ,

                     K                            K

                                     16
where we have used that v11 = -v11 because v  su(3). Furthermore, for traceless v the
integrals (A.20) calculated in the appendix say that

                                             s(h) 2 h v h volK = 0                   (2.48)

                                                              K

for any bi-invariant volume form volK. Therefore, we get the simplified results:

      K  c2P  LvL c1P volK = c2 (-2 v11 c1) |s|2 volK
                                                                K

         cP2  LvR cP1 volK = c2 (- v c1) |s|2 volK                                   (2.49)

      K                                                      K

for all matrices v in su(3). Combining this last calculation with decomposition (1.3),
where the X�H are written in terms of the gauge fields Aj(X�) on M4, we get that

                              c2P  LX�H c1P volK = c2 A� c1    |s|2 volK ,           (2.50)

                                      K                      K

together with the definition

                        4                                       8

      A� c1 := �c1 - 2       ALj (X�) (ej)11 c1 +                  ARj (X�) ej c1 .  (2.51)

                        j=1                                  j=1

This covariant derivative of c1 is a function on M4 with values in C3. As before, we will
analyze its couplings to the gauge fields Aj(X�) and try to identify the components of
c1(x) with standard fermionic fields.

    The strong force gauge fields ARj (X�) act on c1 through simple multiplication c1  ej c1
by the generators of su(3). At the Lie algebra level, this is the action corresponding to
the fundamental representation of SU(3) on C3, so the three components of c1(x) should
be interpreted as quark fields.

    To analyze the coupling of the AjL(X�) to c1(x), recall that the subset of generators
{ej : 1  j  4} spans the subspace of su(3) consisting of block-diagonal matrices of the

form (a) = diag - Tr(a), a , with a in u(2). Thus, when the matrix a is in the subspace
su(2)  u(2), i.e. when Tr(a) = 0, the gauge fields ALj corresponding to the generator
ej = (a) do not couple to c1(x), since (ej)11 = 0 in this case. This is the same as saying
that the components of c1(x) do not couple to the weak force. On the other hand, when

a = diag(i, i) is a generator of the diagonal subspace u(1)  u(2), the corresponding

generator e1 = (a) in su(3) is just the diagonal matrix diag(-2i, i, i). So we have

that

         - 2 AL1 (X�) (e1)11 c1 = AL1 (X�) (4  i c1) .                               (2.52)

Comparing with a table of fermionic representations in the Standard Model and its hy-
percharge assignment [BH, Ham], we conclude that the fields ALj (X�) couple to c1(x) just

                             17
as the electroweak fields couple to the right-handed up quark uR with its three colour
components. Thus, we identify

                                     c+(x) = uR(x) .                                  (2.53)

A similar analysis applied to the component c-(x) of - leads to an identification of this
vector with the antiparticle of uR, namely uL with its three colour components.

Components a�(x, h)

Finally, the behaviour along K of the components a+P (x, h) of +P , as defined in (2.19), is

just

                      aP (x, h) = |s(h)|2 a ,                                         (2.54)

being implicit that the component a may depend on the coordinate x of M4. The Lie
derivatives of aP along left and right-invariant vector fields on K are simply

                      LvL aP =       LvL |s(h)|2 a                                    (2.55)
                      LvR aP =       LvR |s(h)|2 a .

Given two scalar functions aP1 and a2P we can take the hermitian products

      a2P  LvL/R a1P  = |s|2 LvL/R |s|2 a2 a1 = LvL/R    1           |s|4  a2  a1  .  (2.56)
                                                         2

This is a total derivative, and therefore for any bi-invariant volume form volK on the

group K we have

                          a2P  LvL/R aP1 volK = 0 ,                                   (2.57)

                      K

both for right-invariant and left-invariant vector fields on K. Combining with decompo-

sition (1.3) of horizontal vector fields X�H on P , it follows that

                      aP2  LX�H a1P volK = a2 (�a1) |s|4 volK .                       (2.58)

                 K                                    K

Since none of the gauge fields ALj (X�) and ARj (X�) couple to the function a1(x), we

can identify a+(x) with the right-handed neutrino field R(x). Similarly, a-(x) can be

identified with its antiparticle L.

Bringing the components together

All in all, the preceding calculations show that if we take a spinor P (x, h) on the product
manifold P = M4 � K and endow it with the vertical behaviour along K prescribed by
rule (2.17), namely

P (x, h) :=         S(h)  I2 +(x) S(h)   S(h)  I2 -(x) S(h) , (2.59)

                                     18
then the fibre-integral in (1.8) produces kinetic terms on M4 of the desired form:

      0� P , LX�H P volK = Tr 0�  A�  (Vol K)                                       (2.60)

K

                                         = Tr  0�  I2  A�  (Vol K) ,

where � are the gamma matrices on M4 and the covariant derivative of the matrix
 = [ + - ] can be written as

A  := d +                 ALj Lej (+) eLj (-) + AjR Rej (+) eRj (-) .               (2.61)

                       j

Here {ej} denotes a basis of su(3); the actions L and R are determined by the formulae

                    a cT                     0               -2 v11 cT
Lv (�) = vL b D =
                                             2 v11 I3 + v b v D

Rv (�) = vR               a cT   =           0 (v c)T                               (2.62)
                          bD                 0 -Dv

for all matrices v in su(3); and the one-form d is obtained by differentiation along the

coordinates x� of M4,

                          d� :=   �a �cT        dx� .                               (2.63)
                                  �b �D

The awkward factor  appearing in front of the derivatives of a� comes from (2.58).
Following the calculation in (A.18), it is equal to

                           := (Vol K)-1    |s|4 volK   =  4  .                      (2.64)
                                                          3
                                         K

This factor cannot be made to disappear by rescaling s(h) because we have already nor-
malized this function so that the integral of |s|2 over K equals Vol K. This normalization
choice ensures that no similarly awkward factors appear in front of the components �b
and �c (see (2.38) and (2.38)), since such factors would affect the classical electromag-
netic charges associated to those fields. The fermionic fields a�(x), on the other hand, do
not couple to any gauge fields, so an overall factor  in front of its kinetic terms does not
affect the equations of motion and seems comparatively harmless.

    Let us now make some general remarks about the actions L and R that determine
the fermionic gauge couplings. Since the matrices v  su(3) are traceless and anti-
hermitian, it is not difficult do check from definition (2.62) that the linear transformations
vL and vR on M4�4(C) are also traceless and anti-hermitian with respect to the product of

                                         19
matrices Tr(AB). Therefore, regarding vL and vR as transformations of the larger space
M4�4(C)  12, they are elements in su(12). Moreover, from definition (2.62) one can
readily calculate that the commutators of L and R satisfy

Ru , vR - [Ru,v] (�) = 0                                      (2.65)

          Ru , vL (�) = 0

Lu, vL - L[u,v]  a cT                0         2 [u, v]11 cT
                            =
                 bD             -2 [u, v]11 b       0

for all matrices u and v in su(3). These relations say that R defines a Lie algebra
homomorphism from su(3) to su(M4�4), whereas L does not. In particular, starting
from two copies of su(3), the direct sum L + R does not define a homomorphism from
su(3)  su(3) to su(M4�4), and hence to the larger su(12). This fact is in agreement with
the observation in [GG] saying that the fermionic gauge representations of the Standard
Model cannot be obtained simply by restricting to U(1) � SU(2) � SU(3) a well-chosen
representation of the larger group SU(3) � SU(3). Notice, however, that when u and v are
in the subspace u(1)su(2) = u(2) of the original su(3), then the number [u, v]11 is always
zero, so it follows from (2.65) that L + R does define a Lie algebra homomorphism from
u(2)  su(3) to the algebras su(M4�4) and su(12). In fact, u(2)  su(3) is the largest
subalgebra of su(3)  su(3) such that the map L + R is a homomorphism.

    These observations fit well with the discussion in the preceding subsections, where
we showed that when AL has values in the subspace u(2) of su(3) and AR has values
on the whole su(3), the associated action L + R on the components of +(x) coincides
with the gauge representations of the different Standard Model fermions. In fact, the
discussion in those sections, together with (2.61), (2.62) and (2.13), allows us to conclude
that the scalar density (2.60) produces kinetic terms on M4 that coincide with those of
a fermionic generation of fields, provided that we identify the components of the spinor
matrix (x) = [ +(x) -(x) ] as

         R uRr ugR uRb L uLr uLg uLb 

          e-R    dRr  dgR  dbR  eL+  drL  dgL  dLb  


(x)  =                                                 .      (2.66)

          L      urL  ugL  uLb  R    uRr  ugR  uRb  


          eL- dLr dLg dLb e+R dRr dgR dbR

This should be regarded as an 8 � 8 matrix field on Minkowski space M4, since each of its
entries is a Weyl spinor with two complex components. The conventions for naming the

particles and anti-particles are as in [BH], with {r, g, b} being the colour indices of quarks.
Observe how the 12-dimensional chiral operator ^, described in (2.12), acts on the matrix

                           20
 by exchanging each particle with the corresponding anti-particle and changing half of
the signs:

        -L               -urL   uLg   uLb  -R       -uRr   ugR  ubR 
                         -dLr   dLg   dbL  -e-R     -drR   dgR
^        -e+L             urR  -uRg  -uRb   L        uLr  -ugL  dRb   
                          drR  -dRg  -dRb   eL-      dLr  -dgL        

    =                                                                   .       (2.67)

         R                                                      -uLb  


         e+R                                                    -dLb

In particular, this implies that the eigenvectors of ^ are elementary linear combinations
of the particle and anti-particle fields.

    It seems remarkable that all the fields of a fermionic generation can be orderly fit into
an 8�8 matrix representing a single spinor over the 12-dimensional spacetime M4 �SU(3).
In other words, the plethora of degrees of freedom of elementary fermions in one generation
-- spin, chirality, weak isospin, lepton or quark, colour, particle or anti-particle -- can
perhaps be regarded as a veiled reflection of the 64 degrees of freedom of a spinor in 12
dimensions. They look very different from each other because the individual components
of the spinor are associated either to the M4 or the SU(3) factors of spacetime and couple
to the gauge fields according to different representations.

Charges and coupling constants

Electromagnetic charges

The discussion in the previous section was slightly rushed when we identified the compo-
nents of the matrix +(x) with the usual fermionic fields. There was a small gap in the
argument for associating the lower components of b+(x) and D+(x) with the left-handed
particles. As a result, identification (2.66) is strictly valid only in the special case where
the "Higgs vector"   C2, as used in the definition of the "vacuum" metric g on the
internal space, is chosen to be proportional to [0 1]T in the unitary gauge, which is the
traditional choice in the literature. In the next few paragraphs we want to clarify how
this small detail comes about. In the process, and more importantly, we want to verify
explicitly how the photon gauge field A couples to the different components of , i.e. we
want to calculate the electromagnetic charges implicit in the model.

Let us consider the case of b+(x), for instance, which we identified before as

                                      e-R (x) 

                         b+(x)           L(x)       .                           (2.68)


                                         e-L (x)

                                     21
In the previous section we concluded that none of these components couples to the strong
force fields AR, while only the bottom two components couple to the weak fields AL
with values in the subspace (su(2)) of su(3). From this observation and the consistent
assignment of hypercharges, we concluded that the bottom two components of b+ must
correspond to the left-handed leptons. However, nothing in the reasoning showed that
the middle component corresponds to L and the bottom one to eL-, and not the other
way around. In general, the bottom and middle components of b+ may correspond to
independent linear combinations of L and eL-, and to distinguish them one should verify
how they couple to the photon field AL, since electrons and neutrinos have different
charges.

    Recall from section 2 of [Ba] that, among the left-invariant vector fields on K = SU(3),
there is a special one that is a Killing field of the metric g. It is generated by a vector
 in the subalgebra (u(2)) of su(3) that satisfies [, ()] = 0. Explicitly and up to a
normalization factor, it is given by

                    :=  i        -1                       su(3),                  (2.69)
                          3            2I2 - 3 ||-2  

where   C2 is the parameter in the definition of the metric g. Decomposing su(3) into
the sum of the span of  and its orthogonal complement, the photon field AL is defined
as the component of AL with values in the line of su(3) generated by .

    The fermionic couplings of the photon field AL are obtained simply by substituting
v =  in formula (2.62) for the vL actions (the couplings of the Z and W gauge fields
can be similarly obtained from the respective generators). Thus, we get that

                        -1                 b+            L (c+)  =  - 2 i   c+
L (b+) = i 3                  -||2                                       3

L (D+)  =  i            -1                         D+ .                           (2.70)
             3                2 I2 - 3||2 

With the traditional choice for Higgs field in the unitary gauge   [0 1]T , the action of

L is represented by the simpler diagonal matrices

                                                                    -2  ,  -2  ,  -2  c+
L(b+) = i 3 diag (-1, 0, -1) b+                L (c+) = i 3 diag     3      3      3

                    -1  ,  2  ,  -1  D+ .                                         (2.71)
L (D+) = i 3 diag    3     3      3

Thus, we obtain the correct relative assignment of electromagnetic charges if the compo-
nents of b+, c+ and D+ are identified with the fermions e-, , u and d through (2.66),

                                           22
as in the preceding section. It is also clear, however, that identification (2.66) produces
the correct charges only when   [0 1]T . In the case of a general non-zero   C2,
the doublets of left-handed particles inside the 8 � 8 matrix (2.66) should be modified
according to the rule

                  L    -              eL- ||-1  + L ||-1 ~       C2                       (2.72)
                  eL-                                            C2 ,

                  uL   -              dL ||-1  + uL ||-1 ~
                  dL

where we define the vector ~ := [2 - 1]T whenever  = [1 2]T . Using (2.70), one
can check that with these choices the fields e-L , L, uL and dL will again couple to AL with
the correct relative charges. The modifications of (2.66) for the anti-particle fields are
analogous.

    So far in this section we have discussed only the relative electromagnetic charges of the
components of (x), as induced by the Lagrangian density (1.8). We have not discussed
the absolute value of the charges implicit in the model. To address this topic, one should
go back to the calculations of [Ba] and combine the Yang-Mills density on M4 obtained
there with the fermionic kinetic terms proposed here. The classical fermionic charges
can then be read from the coupling of the Maxwell term |FAL|2 with the Dirac terms
(AL)� , 0� L () .

    More precisely, recall that the Maxwell density |FAL|2 for the photon field on M4 was
derived in [Ba] from the scalar curvature RP of the higher-dimensional metric gP on P
using fibre-integration over K, as in the standard Kaluza-Klein calculation. So we can
combine the bosonic Lagrangian density of [Ba] with the fermionic density (1.8) in a single
fibre-integral:

       1                                                 3  0� P , LX�H P  volK ,         (2.73)
      2 P
            K     RP - 2 P + i

                                                       �=0

where  is a positive constant. All the terms of this integral involving the photon field
AL have been calculated in the previous section and in sections 3 and 5 of [Ba]. A careful
collection of these terms yields an expression of the form

-  1  (ek,  ej )  (FAkL )� (FAj L )�  +  i (AL)� Tr              (0�  I2) L ()  Vol K  .  (2.74)
   4                                                                             2 P

There are no additional terms coming from the covariant derivative dA because the
commutator , () vanishes in su(3), by definition of . In this formula, the symbol

                                                            23
 may stand either for the AdSU(3)-invariant inner-product on su(3), as in section 3 of
[Ba], or for the more general AdU(2)-invariant product ~ described in section 5.

    Now, working near the vacuum configuration where  = constant = 0, we have
already identified the normalization  of the vector  that is necessary for the curva-
ture FAL to appear in the four-dimensional Lagrangian LM as it does in the traditional
Einstein-Maxwell Lagrangian. These normalization conditions are standard in the Kaluza-

Klein approach and were discussed in section 3.7 of [Ba] as necessary for both Lagrangians

to produce the same linearized equations of motion. It was observed that we should have

                           P = M Vol(K, g)

and that the vector  that leads to the canonical normalization of the photon field AL
should satisfy

                                            (, ) = 2 M .

Therefore, if we choose the coefficient of the fermionic kinetic term to have the same
value,  = 2 M , it will also cancel the (Vol K) (2 P )-1 factor and produce canonically
normalized terms in the approximation where  is nearly constant:

-  1  (FAL )� (FAL )�      + i (AL )� Tr           (0�     I2)  L   ()  .                                                         (2.75)
   4                                                              

Hence the electromagnetic charges of the components of  are just the eigenvalues of the

matrix -iL [Ham, Wei2]. But the relation between the normalized and non-normalized
vectors is simply

       =                     2 M          =  2     M            .                                                                 (2.76)
                           (, )                 1 + 3 2

Thus, working with the non-normalized vector (2.69), the electromagnetic charges are the

eigenvalues of the matrix

                           -i           2 M     L     ,                                                                           (2.77)
                                      (, )

winh(ic2h.71a)reshinovwaerdiatnhtautndLerhraesscaanlineiggeonfvalubeyoaf n-yp3oisiftoivrethfaecetolerc.trFoinnafilelyld, stheeL-  calculation
                                                                                                                                  and e-R , so

we conclude that the electromagnetic charge of the positron in the model determined by

Lagrangian (2.73) is given simply by

                           e=           6 M        .                                                                              (2.78)
                                      (, )

Recall again that we are working in the vacuum approximation and that in these formulae
the parameter  stands for the vacuum value 0.

                                      24
    The formula for the charge of the positron can be recast using the relation between
the norm (, ) and the Riemannian length of the circle inside SU(3) defined by the
one-parameter subgroup generated by . To obtain this relation, start with definition
(2.69) of  and observe that, since   commutes with I2,

exp  t i    2I2 - 3 ||-2                    = exp  t  2i    I2             
         3                                              3       exp -it 3 ||-2  

as 2 � 2 matrices. Moreover, we have that ( )n = ||2n-2  for any positive integer

n, so the second exponential is just


     exp -it 3||-2   = I2 + e-it 3 - 1 ||-2   .

It follows that the one-parameter subgroup of SU(3) generated by  is


                        e-it/1
     exp(t )         =         3                                                   .  (2.79)

                                                                     ||-2  
                                            ei 3 t I2 +  1 - ei 3 t


This subgroup defines a circle inside SU(3) as the parameter t ranges from 0 to 2 3 .
Since the metric g is left-invariant and coincides with the product  when restricted to
the subalgebra u(2) of su(3), the length  of this circle is simply

                      = 2  3 g(, ) = 2  3 (, ) .                                      (2.80)

So we conclude that                         
                                            6  2 M
                                      e  =               .                            (2.81)

This formula agrees with the result obtained by Weinberg in [Wei] on more general

grounds1. In Lorentz-Heaviside-Planck units with c = = 0 = �0 = 8G = 1, we
have M = 1 and e = 4, so the formula implies a length of the internal "electromag-
netic circle" of

                                    88.0 P  7.13 � 10-33 m ,


where P is the rationalized Planck length 8G c-3. It is similar to the estimates

obtained in 5D Kaluza-Klein theory.

1Provided that one makes the following adjustments: 1) the gravitational constant  of [Wei] is related
 to the definition used here by 2 = 2 M ; 2) formula 16 of [Wei] represents the value of the positive
 elementary charge of which all other charges are integer multiples, so it is the antiquark charge e/3; 3)
 for an isometry subgroup U(1)L acting on the internal space K = SU(3) one should take Ne = 1 in the
 cited formula.

                                                         25
Gauge coupling constants

The purpose of the next paragraphs is to read from the four-dimensional Lagrangian the
value of the classical electroweak and strong coupling constants of the model. Their values
will be expressed in terms of the three positive constants -- 1, 2 and 3 -- that were
used in section 5 of [Ba] to write the general AdU(2)-invariant metric on su(3) that appears
in the Lagrangian density.

    Consider the Yang-Mills and Dirac terms coming from Lagrangian (2.73) that involve
the electroweak fields AL, which are taken with values in the subspace u(2) of su(3):

      -  1  (ek,  ej )  (FAkL )� (FAj L )�  +  i (AjL)� Tr   (0�  I2) Lej ()  Vol K  .       (2.82)
         4                                                                     2 P

Consider first the case of the diagonal matrix Y := (iI2) = diag(-2i, i, i) in su(3). Just
as in the case of the electromagnetic charge, the coupling constant g/2 associated to the

subgroup U(1)Y can be read from Lagrangian (2.82) by looking at the eigenvalues of the


matrix -i L using the normalization Y of Y such that
                      Y

                                            =  = 2 M = 2 P (Vol K)-1.                        (2.83)

                         Y, Y

Indeed, with this normalization the components of the gauge fields associated to the


direction Y  su(3) define a canonically normalized Lagrangian inside (2.82), so the

coupling constant g/2 is minus the eigenvalue of the matrix -i L when applied to a
                                                                       Y

fermionic field of hypercharge -1, say the electron field eL-   [Ham, Wei2].                 and Y
                                                                              But Y

are related by the factor 2 M / (Y, Y ). Thus, working with the non-normalized vector,

g/2 is minus the eigenvalue of the matrix

                                            -i      2 M     LY                               (2.84)
                                                  (Y, Y )

acting on the left-handed electron field. The definition of  in (2.62) says that -i LY
has an eigenvalue of -3 when acting on eL-. Hence we conclude that the U(1)Y coupling

constant of the model is given by

                                            g  =  3    2 M .                                 (2.85)
                                            2         Y, Y

The coupling constant of the weak SU(2) subgroup of the the Standard Model group can be

obtained in a similar way. Take the generator i3 of su(2) and consider the corresponding


matrix T3 := (i3) regarded as an element of su(3). Take the normalization T3 of T3 such

that

                                                                                             (2.86)

                                  T3, T3 =  = 2 M .

                                                     26


Then the components of the gauge fields associated to the direction T3  su(3) define

a canonically normalized Lagrangian inside (2.82), so the coupling constant g/2 is the

eigenvalue of the matrix -i L when applied to a fermionic field of weak isospin 1/2,
                                                          T3


say the neutrino field L [Ham, Wei2]. The matrices T3 and T3 are related by the factor

2 M / (T3, T3). Thus, working with the non-normalized vector, g/2 is the eigenvalue

of the matrix

                                    -i                2 M             TL3                               (2.87)
                                                    (T3, T3)

acting on the left-handed neutrino field. The definition of  in (2.62) says that -i LT3 has
an eigenvalue of 1 when acting on L, so we conclude that the coupling constant is just

                                    g           =          2 M .                                        (2.88)
                                    2                    T3, T3

Finally, to obtain the strong coupling constant, denoted by gs, start by considering the
four-dimensional density (2.73) and collect all the terms involving the gluon fields AjR.
These terms have been calculated in the previous section and in section 5 of [Ba], yielding

an expression of the form

     -  1  ~  Tr(ek   ej )  (FAkR )� (FAj R )�  + i (AjR)� Tr          (0�  I2) Rej ()            Vol K  .
        4                                                                                          2 P

                                                                                                        (2.89)

Now consider the generator t3 := i diag(1, -1, 0) of su(3), which is just the anti-hermitian

version of the third Gell-Mann matrix. For a canonically normalized Lagrangian, the

coupling constant gs/2 can be defined as the eigenvalue of the matrix -i tR3 when applied

to a red quark field, say the field uRr [Ham]. For the Lagrangian (2.89) we should look at

the  eigenvalues  of  the   matrix  -i L        using   the  normalization          of  t3  such  that
                                            t3                                t3

                                    ~ Tr        t3      =  = 2 M .                                      (2.90)

                                                    t3


The matrices t3 and t3 are related by

                                    ~           2 M          t3  =         M  t3 .
                                                Tr(t3 t3)                  ~
                            t3 =

Thus, working with the non-normalized vector, gs/2 is the eigenvalue of the matrix

                                                -i      M        Rt3                                    (2.91)
                                                        ~

acting on the quark field uRr . The definition of  in (2.62), together with the fermion
identifications (2.53) and (2.66), say that -i tR3 has an eigenvalue of 1 when acting on uRr ,

                                                        27
so we conclude that the strong coupling constant is

                             gs  =        M      .                     (2.92)
                             2            ~

These results for the gauge coupling constants can be recast in terms of the three constants

1, 2 and 3 that were used in section 5 of [Ba] to define the AdU(2)-invariant metric
on su(3), which was denoted there by ~ but is called here simply . A straightforward

calculation using the definition of that metric yields

 Y, Y = 6 1                   T3, T3 = 2 2            ,  = (1 + 3 2)/2 .

Combining with the definition of the constant ~ as the weighted average (1+32+43)/8,

and keeping in mind that in Lorentz-Heaviside-Planck units M = 1, we finally obtain

the relations                                        

               g  =     3                 e = 2 3                      (2.93)
               2        1                            1 + 32

               g  =     1                 gs  =       22            .
               2          2               2          1 + 3 2 + 4 3

Uniqueness of the spinor vertical behaviour

A natural question to ask about the model described in the last few sections is whether
the vertical transformation rule (2.17) for the spinor components P (x, h) is unique, in
the sense that it is the only possible behaviour of  along K = SU(3) that projects down,
after fibre-integration, to the correct fermionic representations in the four-dimensional
Lagrangian. The answer is no, it is not unique. Even leaving alone the non-abelian 3 � 3
components of the transformation matrix S(h), as in (2.15), one can check that there
exists more than one scalar function s(h) that produces the same representations in M4.
To recognize this fact, start by observing that the calculations of section 2.3 only require
that the complex function s : K  C satisfies the following integral identities:

                     s LvR s volK = 0                                  (2.94)

                  K

                        s LvL s volK = 2 v11 |s|2 volK

                     K                        K

                        |s|2 h v h volK = |s|2 h v h volK = 0 ,

                  K                    K

for all matrices v in su(3). Any normalized function s(h) that satisfies these identities,
and hence also the complex conjugate identities, may be plugged into definition (2.15) of
S(h) without affecting the overall conclusions of section 2.3.

                                    28
    Looking into the detailed calculation of the integrals above, one of the salient features
of the original function

          s1(h) := (h11)2 + (h21)2 + (h31)2 ,                 (2.95)

leading to the second integral identity, is its equivariance under the action of the embedded
subgroup U(2)  SU(3). Namely,

          s1 h � (a) = (det a)-2 s1(h) ,                      (2.96)

for all matrices a  U(2), with the usual notation (a) = diag det a-1, a . In addition,

for the first integral in (2.94) to vanish it was also helpful that s1(h) is symmetric in its
three variables, since this produces a factor v11 + v22 + v33 that is zero for all v  su(3).
Therefore, one promising possibility to change the function s1(h) would be to multiply it
by a totally symmetric real polynomial p |h11|2, |h21|2, |h31|2 , as this would not disturb
the equivariance property (2.96). A more detailed analysis of the integral calculations

shows that this is indeed a viable option. One can rigorously prove that the new scalar

function

          p |h11|2, |h21|2, |h31|2 s1(h)                      (2.97)

also satisfies identities (2.94), and hence leads to the correct fermionic representations in

M4 after normalization. In fact, more is true: given a second symmetric polynomial in
the same variables, p2 |h11|2, |h21|2, |h31|2 , one may generalize the transformation S(h)
of (2.15) to

          S(h) := p(h) s1(h)  p2(h) h                      ,  (2.98)

and still the components of P (x, h) will project down to the fermionic representations

found in the Standard Model. Hence a first conclusion seems to be that there are infinitely

many vertical transformations S(h) of (x) that produce the correct representations in

M4, after fibre-integration along K, as long as we keep increasing the degree of the scalar
polynomials involved. Heuristically, higher-degree polynomials on the entries of h  SU(3)

will produce vertical functions S(h) with more "oscillations" along K, and hence would

presumably correspond to larger eigenvalues of the Laplacian and Dirac operators on K.

In other words, would correspond to higher masses of the fermionic components of (x)

after projecting down to the four-dimensional Lagrangian.

    What if we do not want to increase the degree of the polynomials involved? The
original scalar function s1(h) has degree two in the entries hk1 of h, and there exists a
second symmetric polynomial of the same degree in these variables, namely

          s2(h) := h11h21 + h11h31 + h21h31 .                 (2.99)

          29
Since s2(h) has the same equivariant behaviour as s1(h) under right-multiplication h 
h � (a), satisfying (2.96), it follows that s2(h) also satisfies the second integral identity in
(2.94). However, the results in appendix A.4 show that

   s2 LvR s2  volK   =  2i  Im(v12    +    v13    +  v23)     |s2|2 volK             (2.100)
                        3
K                                                          K

                        1        0 1 1
                        10
   |s2|2 h v h volK  =      v11    1       0  1         |s2|2 volK
                                           1    
K                                                    K
                                   1          0

   |s2|2 h v h volK  =  i   Im(v12         + v13  + v23) diag(-2, 1, 1)      |s2|2 volK ,
                        15
K                                                                         K

for all matrices v  su(3). This is very different from (2.94), so the scalar function s2(h)

on K = SU(3) does not have the required behaviour along K to produce the correct

projections to M4 of the spinor P (x, h).

This is not the end of the story for degree two polynomials, though. Persevering in

the calculations of slightly more general integrals over SU(3), one can show that linear
combinations of both polynomials

                     s(h) := 1 s1(h) + 2 s2(h) ,                                     (2.101)

actually do satisfy identities (2.94) whenever the constants 1 and 2 are related by

                     |2|2 + 2 (1 2 + 1 2) = 0 .                                      (2.102)

Given an arbitrary 1  C, the general solution to this equation is just               (2.103)
                                            2 = 2 (1 + ei2) 1

for some phase   [0; [. Thus, for 1 = 0 we get 2 = 0 as well, and there is no
non-trivial solution. For 1 = 0 we get a "circle" of solutions parametrized by :

              s(h) :=  s1(h) - 2 (1 + ei2) s2(h) ,                                   (2.104)

apart from the overall normalization factor . The simplest solution s1(h), discussed in
the previous section, is recovered when  = /2.

    The conclusion is thatthe whole discussion of sections 2.2 and 2.3 remains valid if,
instead of the choice s = 2 s1 used there, we choose as s(h) any degree two polynomial

belonging to the family s(h) defined by (2.104). Observe also that the formulae (A.19)
in appendix A.4 imply that the integrals of |s(h)|2 and |s(h)|4 are

   |s|2 volK  =      1  ||2   1 + 8 cos2()           (Vol K)                         (2.105)
                     2
K

   |s|4 volK  =      1   ||4     5 + 144 cos2() + 256 cos4()              (Vol K) .
                     15
K

                                           30
The discussion in section 2.3 assumed a function s normalized so that the fibre-integral of
|s|2 would be equal to Vol K. Thus, the complex constant  in definition (2.104) should

be picked to satisfy                 2
                              1 + 8 cos2()
                      ||2  =                .                                    (2.106)

The normalized functions s are then parameterized by two circles, not just one.

    In the present section 2 we have identified relatively simple functions and vertical
behaviours of the spinor P (x, h) that generate, after pairing and fibre-integration, the

complete set of fermionic gauge representations appearing in the Standard Model. It

would be desirable to find a more fundamental, a priori justification for the emergence of

these particular vertical functions, other than the fact that they generate the experimen-

tally observed gauge representations in four dimensions. Studying the properties of the
spinors P (x, h) under the action of natural Dirac operators on SU(3) could be a useful

starting point.

                              31
3 Masses induced in four dimensions

Mass in Kaluza-Klein theories

Traditional Kaluza-Klein theories regard the mass of particle fields as being due to the
vibrations of the higher-dimensional fields along the internal space K, proposing that
the energy associated to those movements will be perceived in four dimensions as the
particle's mass. More precisely, if we endow P = M4 � K with a "vacuum" product
metric, the higher-dimensional Laplacian can be written as a sum of its lower-dimensional
counterparts, P = M + K. Therefore, if a scalar particle field behaves along K as
an eigenfunction of the internal operator K, the kinetic term of the higher-dimensional
Lagrangian will produce both kinetic and mass terms in the four-dimensional, Klein-
Gordon Lagrangian:

K = - �2   =   , P  = , M  - �2 ,  . (3.1)

For fermions the argument is similar. The higher-dimensional spinor space can be fac-
torized as a tensor product 12 = 4  8. If  =    is a spinor in this space, the
higher-dimensional Dirac operator acts on it as

           D/ P (  ) = (D/ M )   + (5)  (D/ K) ,

where 5 = diag(I2, -I2). In particular, if  is an eigenspinor of D/ K with a real eigen-
value �, then the classic Dirac kinetic term on the higher-dimensional manifold can be
decomposed as

i 0, D/ P  = i 0, D/ M  ,  + i� 0, 5 ,               (3.2)
                    = i 0, D/ M  - � 0,  .

In the last equality, the spinor  on Minkowski space was redefined through an isomor-
phism of 4 in order to obtain the four-dimensional kinetic and mass terms in their
traditional form [DNP, p. 22]:

 :=        ,   I4 + i5  =          ,  exp (i5/4)  .
            2

    We now want to investigate the extent to which this attractive general picture can be
applied to the 12-dimensional spinor P (x, h) with its prescribed behaviour along K. Does

the h-dependence prescribed by (2.17) determine anything close to an eigenfunction of
K or D/ K? In line with our discussion so far, we do not really need exact eigenfunctions:

the right-hand side of equations (3.1) and (3.2) may have additional terms, as long as they

                               32
integrate to zero when performing the integrals over K that generate the four-dimensional
Lagrangian.

    What we aim to calculate, in fact, are the integrals of the pairings P , KP and
 0P , (5  D/ K)P over the group K = SU(3) equipped with a left-invariant metric
similar to the metrics g defined in [Ba]. Between these two pairings, the most relevant is
the one involving the Dirac operator. Since its counterpart 0P , D/ M P produces the
fermionic kinetic terms of the Standard Model Lagrangian, as studied in section 2.3, it
would be great if the second pairing 0P , (5 D/ K)P would produce the mass terms
of the same Lagrangian, after fibre-integration over K. The algebra involved in the explicit
calculation of the latter pairing seems to be relatively straightforward but more extended
than what we can tackle here. Although we give a few preparatory details in the next
short section, we will not carry out the full algebraic calculations here, so will not be able
to offer a clear picture of the mass terms that appear in four dimensions after projecting
 0P , (5  D/ K)P down from P through fibre-integration. This is a consequential
point that deserves further investigation in the study of the present geometrical model.

    The calculations are shorter in the case of the scalar Laplacian K over K, since it can
be expressed purely in terms of Lie derivatives LvL, with no gamma matrices mixing the
components of P . We will therefore be able to calculate the explicit mass terms produced
by the pairing P , KP after projection to four dimensions. These calculations will
occupy us in the latter parts of the present section.

Fermion masses from the internal Dirac operator

By definition of left-invariant metric, if {ej} is a g-orthonormal basis of su(3), the corre-
sponding left-invariant vector fields {ejL} will be everywhere orthonormal on K. Therefore,
the Dirac operator on (K, g) can be written on general grounds [BHM] as

D/ K  =     j vsjLpin =     j  LvjL   +  1       g vjL vkL, vlL k l  ,           (3.3)
                                         2
         j               j                  k<l

where {j} is a set of gamma matrices corresponding to {ej}, and  is the original
connection on the tangent bundle T K that leads to the connection  spin on the spin
bundle. When  is the Levi-Civita connection of a left-invariant metric, the Koszul
formula allows us to express it in purely algebraic terms:

g vjL vkL, vlL  =  1     g([vj, vk], vl) - g([vk, vl], vj) + g([vl, vj], vk)  ,  (3.4)
                   2

where we have used that the product g(vjL, vkL) = g(vj, vk) is constant on K and that
[vjL, vkL] = [vj, vk]L. Moreover, using the properties of gamma matrices and the fact that

                               33
left-invariant vector fields have vanishing divergence on a unimodular Lie group equipped
with a left-invariant metric,

                               g vjL vkL, vjL = divg(vkL) = 0 ,                                    (3.5)

                            j

the general formula for the Dirac operator on (K, g) can be further simplified to [Bar]

             D/ K  =              j LvjL  +                 jkl j k l  .                           (3.6)

                            j                   j<k<l

Here the totally anti-symmetric real coefficients jkl are defined by

        jkl  :=  1      g([vj, vk], vl) + g([vk, vl], vj) + g([vl, vj], vk)         .              (3.7)
                 4

Observe that when g is a bi-invariant metric on K, the three terms in the preceding sum
are equal to each other, so the formula for jkl is simpler. This simplification does not
occur in the case of the left-invariant metrics g and g~ defined in sections 2 and 5 of [Ba].
Denoting by v = v + v the standard decomposition of a vector in su(3)  u(2) C2, as in
[Ba], and inserting the definition of g into the expression for jkl, a little algebra shows
that these coefficients may be written in terms of the Ad-invariant metric  on su(3) as

jkl  =  3    [vj, vk],  vl  +     1      ,  [vj , vk ], vl  +  [vk , vl], vj     +  [vl, vj ], vk
        4                         2

     =  3    [vj, vk],  vl  +     1       , [v (j), v (k)], v(l)              ,                    (3.8)
        4                         2


where the last sum is over the circular permutations of {j, k, l}. Therefore, the Dirac

operator (3.6) depends in two ways on the parameter  of g: implicitly, through the
choice of orthonormal basis {ej} of su(3); explicitly, in the formula for the coefficients
jkl. The Dirac operator on K will be simpler if the original connection  on the tangent
bundle is taken to be the flat Schouten connection 0, instead of the usual Levi-Civita
connection. This is a g-compatible connection with torsion T 0(uL, vL) = [u, v]L, and the

coefficients jkl of the corresponding Dirac operator are identically zero. In Minkowski
space M4 these two connections coincide, since the Lie bracket of the abelian translations
group is trivial and 0 is torsionless too.

    In any case, the first step in the calculation of the projection of 0P , (5  D/ K)P
down to M4 should probably be dealing with the derivative terms j LvjL of the full D/ K.
More precisely, in analogy with the integrals (1.8) that lead to the fermionic kinetic terms

in M4, one may try to calculate the fibre-integrals

                               8     03+l P , LelL P           volK ,                              (3.9)
                        K l=1

                                            34
and see what kind of mass terms they induce in four dimensions. Here {el} is a g-
orthonormal basis of su(3) but the a are the gamma matrices of the 12-dimensional
M4 � SU(3) defined in (2.8). So 3+l is the gamma matrix corresponding to el. This
calculation is simplified by the work done in section 2.3, where it was shown that for

general 8 � 8 matrices 1(x), 2(x) and for any vector v in su(3):

   P2 , LvL 1P volK =     2P , (vL 1)P volK .  (3.10)

K                      K

The algebraic action of vL on the components � of  was explicitly written in (2.62). In
the case of interest we have 2 = 03+l and 1 = , so the basic task of the calculation
will be to keep track of the components of the 8 � 8 matrices 03+l for l = 1, . . . , 8, in
order to calculate the sum of all pairings 03+l, Lv  . The integrals over K coming
from the right-hand side of (3.10), on the other hand, are easily computable. This is

so because 2 and Lv 1 do not depend on the coordinate h  K, and the prescription
  P that extends them to functions on K is such that, when dealing with a product
Tr (P2 ) P1 , the only emerging integrals are those of the scalar functions |s(h)|2 and
|s(h)|4, both of which have already been computed here.

    In the case of  being the Levi-Civita connection on K, the explicit calculation of the
coefficients jkl should be a second extended algebraic task.

    Finally, let us comment that even if the whole algebraic calculation would develop
smoothly, its ideal result should not be too simple a set of mass terms on M4, as we have
not touched upon the subject of fermion generation mixing. In order to replicate the
full mass structure of the Standard Model, one would ideally hope to find at least three
distinct 12-dimensional spinor fields -- P1 (x, h), 2P (x, h) and P3 (x, h) -- all of them
having slightly different behaviour along the internal space K, though still projecting
down to the correct gauge representations on M4 (see the last part of section 2), and then
calculate that only non-trivial linear combinations of the three spinors would behave as
eigenfunctions of D/ K, after pairing and projection to M4. This is an idealized scenario,
of course, and should be taken as wishful speculation.

Masses from the internal Laplace operator

On a connected, unimodular Lie group, such as K = SU(3), every left-invariant volume
form is also right-invariant. Hence the natural volume form of a left-invariant Riemannian
metric g on K will be fully bi-invariant, and both the right and left-invariant vector fields
will have zero divergence on (K, g). So if we take an orthonormal basis {ej} of the Lie
algebra and extend it to left-invariant vector fields {ejL}, the scalar Laplacian on (K, g)

                                                       35
may be written, in terms of these orthonormal fields, simply as

                              8

                     Kg f =         LejL LejL f                                 (3.11)

                              j=1

for any scalar function f on K [DN]. This formula does not work with the right-invariant
fields {ejR}, as they generally are not orthonormal with respect to the left-invariant g.

    Proceeding as in section 2, in order to calculate g P more explicitly, we will de-
compose the 12-dimensional spinor P = [ +P -P ] into several components that are not
mixed by the Lie derivatives LejL, and hence by the Laplacian:

                     �P =     aP� (cP�)T .                                      (3.12)
                              b�P D�P

Each of these components transforms along the internal space K according to the rules
(2.19). Since the full pairing P2 , g P1 is just a trace Tr (P2 ) g 1P , it is clear
that it will break into a sum of traces of the smaller components. Thus, the integral along

K of the full pairing breaks into a sum of fibre-integrals of the general form

                                 8

   Tr (D2P ) g D1P volK =          Tr  (D2P ) LeLj LeLj D1P             volK ,  (3.13)

K                          K  j=1

and analogous integrals for the remaining components a, b and c of . Using the explicit
expressions for the K-dependence of DP (x, h) and the other components, as stated in
(2.19), we will now compute the Lie derivatives and integrals above.

Components D�(x, h)

Simplifying the notation of (2.19) for the transformation of D+, write          (3.14)
                                             DP (h) = h D h ,

where it is implicit that the 3 � 3 matrix D may depend on the coordinate x of M4. The
Lie derivatives of this function along any left-invariant vector fields uL and vL on K are

LuL LvL DP (h) = h u v D h + h v D h u + h u D h v + h D h u v ,                (3.15)

where u and v are 3 � 3 matrices in su(3). If we have two matrix functions D1P and D2P ,
it is possible to construct the pairing

Tr (D2P ) LuL LvL D1P = Tr D2 u v D1 +D2 v D1 h u h +D2 u D1 h v h +D2 D1 h u v h ,

                              36
where the equality uses the cyclic properties of the trace. Integrating the right-hand side
along the fibre K leads to a significant simplification, since the integrals in appendix A.4
imply that

                                h u h volK = h v h volK = 0                            (3.16)
                                                                                       (3.17)
                             K                      K

                           h u v h volK  =      1   Tr(u v) I3  ,
                                                3
                        K

for any traceless matrices u, v in su(3). So we get

   Tr (D2P ) LuL LvL D1P volK =          Tr D2 u v D1      +    1  Tr(D2 D1)  Tr(u v)  (Vol K) .
                                                                3
K

Using expression (3.11) for the Laplacian, we finally obtain

   Tr (D2P ) Kg D1P volK = Tr D2 gD D1 (Vol K) ,                                       (3.18)

K

where Dg is a 3 � 3 hermitian matrix that can be written in terms of the g-orthonormal

basis {ej} of su(3) as

                                    8               1
                                                    3
                             Dg :=       ej ej  +      Tr  ej ej   I3 .                (3.19)

                                    j=1

An explicit expression for the matrix j ej ej is given in appendix B, together with its
eigenvalues and eigenvectors. All of these depend on the Higgs-like vector   C2 that

defines the metric g on K, of course.

    Choosing a basis of C3 that diagonalizes gD and taking the particular case where
D2P = D1P = D+P (x, h), the fibre-integral of the higher-dimensional scalar density is simply

           Tr (D+P ) Kg D+P volK = Tr D+(x)  diag(�1, �2, �3) D+(x) (Vol K) ,

             K

where �a are the eigenvalues of gD. In other words, after fibre-integration along K, the
scalar density Tr (D+P ) gKD+P on the product P = M4 � K generates Klein-Gordon
mass terms for the fields D+(x) on M4. The mass parameters are the eigenvalues �a.

Components b�(x, h)

Simplifying the notation of (2.19), the vertical behaviour along K of the component

bP+(x, h) can be written as

                                    bP (h) = s(h) h b ,

                                                37
where s : K  C is any of the scalar functions defined in (2.104). It is implicit that the
vector b  C3 may depend on the coordinate x of M4. The Lie derivatives of bP along
left-invariant vector fields uL and vL on K are

    LuL LvL bP (h) = (LuL LvL s) h b + (LvL s) h u b + (LuL s) h v b + s h u v b ,

where u and v are matrices in su(3). If we have two vectorial functions bP1 and bP2 , it is
possible to take the hermitian product

(b2P ) LuL LvL b1P  = s (LuL LvL s) b2 b1 + s (LvL s) b2 u b1
                                                + s (LuL s) b2 v b1 + |s|2 b2 u v b1 . (3.20)

The integrals calculated in (A.26) and (A.28) of appendix A.4 then say that

          s (LvL s) volK = 2 v11 |s|2 volK

   K                                         K

      s (LuL LvL s) volK  =         2     u11 v11  +   1  +  8  1        (uv)11      |s|2 volK
                                                                cos2()
   K                                                                               K

for any traceless matrices u, v in su(3). Applying these integral identities to the right-hand

side of (3.20) we obtain

  (b2P ) LuL LvL b1P     volK = b2     2  u11 v11   +     1  +  8  1       (uv)11  I3
                                                                   cos2()
K

                                             + 2 v11 u + 2 u11 v + u v b1 |s|2 volK .

                                                                                                            K

Coming back to expression (3.11) for the Laplacian, we finally get that

   (b2P ) Kg b1P volK = b2 bg b1                |s|2 volK = (b2P ) bg bP1 volK , (3.21)
K                                            K                        K

where gb is a 3 � 3 hermitian matrix that can be written in terms of the g-orthonormal
basis {ej} of su(3) as

          8                                                           1
                                                                      cos2()
   gb :=            ej ej + 4 (ej)11 ej + 2  (ej )211  +     1  +  8          (ej  ej )11  I3 .  (3.22)

          j=1

Expression (3.21) says that, after pairing and fibre-integration over K, the action of the

vertical Laplacian Kg on the functions bP corresponds to the simpler algebraic action of
the matrix bg on the vector b  C3. Taking the particular case where b2 = b1 = b+ is
an eigenvector of gb with eigenvalue �, the fibre-integral of the vertical Laplacian kinetic
term produces a simple Klein-Gordon mass term on M4:

                         (bP+) gK bP+ volK = � b+ b+ |s|2 volK .                                 (3.23)

                      K                                            K

                                                38
The matrix bg and its eigenvalues depend on the Higgs-like vector   C2 used in defini-
tion of the left-invariant metric g. The explicit dependence of bg on  may be derived
from the formulae in the first part of appendix B.

Components c�(x, h)

The components cP+(x, h) of +P behave along K according to the rule (2.19), which may
be written in simplified notation as

                                          c+P (x, h) = s(h) h c ,

where s : K  C is the scalar function defined in (2.104). It is implicit that the vector
c  C3 may depend on the coordinate x of M4. Given vectors u and v in su(3), the Lie
derivatives of cP along left-invariant vector fields uL and vL on K are

 LuL LvL cP (h) = (LuL LvL s) h c - (LvL s) u h c - (LuL s) v h c + s v u h c ,

where u and v are matrices in su(3). If we have two vectorial functions cP1 and cP2 , it is
possible to take the hermitian product

(c2P ) LuL LvL cP1  = s (LuL LvL s) c2 c1 - s (LvL s) c2 h u h c1
                                     - s (LuL s) c2 h v h c1 + |s|2 c2 h v u h c1 . (3.24)

The integral identities presented in (A.20) and (A.27) of appendix A.4 then say that, for
any traceless u and v in su(3),

                    s (LvL s) h v h volK = 0

                 K

                        |s|2 h v u h volK  =    1  Tr(vu) I3        |s|2 volK .
                                                3
                      K                                           K

This means that two terms in the right-hand side of (3.24) are killed off by fibre-integration

over K, with a third term having a relatively simple form. The additional integral identity

   s (LuL LvL s) volK  =         2     u11 v11  +  1  +  8  1        (vu)11      |s|2 volK
                                                            cos2()
K                                                                              K

from the same appendix, then allows us to write the integral of equation (3.24) in the

simplified form

  (c2P ) LuL LvL cP1  volK = c2     2  u11 v11  +     1  +  8  1       (vu)11
                                                               cos2()
K

                                                               +  1  Tr(vu)    c1    |s|2 volK .
                                                                  3
                                                                                   K

                                           39
Coming back to expression (3.11) for the Laplacian, we finally get that

      (cP2 ) gK c1P volK = c2 gc c1                   |s|2 volK = (c2P ) cg cP1 volK , (3.25)
   K                                               K                        K

where gc is a 3 � 3 hermitian matrix proportional to the identity I3. In terms of a
g-orthonormal basis {ej} of su(3), it may be written as

                       8  2  (ej )211  +  1  +  8  1       (ej  ej  )11  +  1  Tr(ej ej )  I3 .  (3.26)
                                                   cos2()                   3
      cg :=

                     j=1

Expression (3.25) says that, after pairing and fibre-integration, the vertical Laplacian gK
acts on the vectors c  C3 as simple scalar multiplication by the real coefficient of cg.
The middle expression in (3.25) is a Klein-Gordon mass term for the field c(x) on M4.

Components a�(x, h)
The scalar component a+P (x, h) of +P behave along K according to the simple rule (2.19),

                                        aP (x, h) = |s(h)|2 a(x) ,

where s : K  C is the function defined in (2.104) and a(x) is a complex number.
Therefore, using standard properties of the Laplacian and an orthonormal basis {ej} of
su(3),

K  (aP ) Kg aP volK = aP 2 |s|2 gK|s|2 volK = - aP 2                                       grad |s|2 2 volK
                                          K                                    K                         (3.27)

                             = - aP 2                 Lej |s|2 2 volK .

                                             Kj

We do not offer here a more explicit formula for the last integral.

                                                      40
Appendices

A Integrals on SU(3)

A.1 Integrals of general polynomials in hk1 and hj1

Let K be the Lie group SU(3) equipped with a bi-invariant volume form volK. Denote
by hkj the entries of a matrix h in SU(3) and consider the function P : SU(3)  C
determined by a general monomial in the entries of the first column of h:

          P (h) := (h11)k1 (h21)k2 (h31)k2 (h11)n1 (h21)n2 (h31)n3 ,                 (A.1)

where the exponents kj and nj are all non-negative integers. The aim of this appendix is
to prove that

I[P ] :=       P (h) volK  =  k1n1  k2n2  k3n3      (2   2 k1! k2! k3!     Vol K  .  (A.2)
                                                        + k1 + k2 + k3)!
          hK

Observe that, by the symmetry of the problem, this result is valid also for monomials in
the entries of any column of h  SU(3), other than the first column hk1, or monomials in
the entries of any line of h.

First part of the calculation

We start by showing that the integral (A.2) vanishes if kj = nj for some j in {1, 2, 3}. To
this end, notice that the bi-invariance of the volume form volK implies that the integral
is invariant under a change of variable of integration of the form h   h or h  h , for
any fixed group element   K.

    Choosing  of the form diag(e-2i, ei, ei), we have that (h )k1 = e-2i hk1, and hence

                               P (h ) = e-2i(k1+k2+k3-n1-n2-n3) P (h) .

The invariance under change of variable then says that, for any phase ,

          I[P ] =      P (h ) volK = e-2i(k1+k2+k3-n1-n2-n3) I [P ] .

                   hK

So if the sum k1 + k2 + k3 - n1 - n2 - n3 is not zero, then I[P ] necessarily vanishes.

    Now assume that k1 +k2 +k3 = n1 +n2 +n3. After pairing all the factors hk1 with their
complex conjugates in P (h), as much as possible, the initial monomial can be written in

the form

                   P (h) =    hm111 h2m12 h3m13  2  hj111  hj221  h j1+j2            (A.3)
                                                                    31

                                    41
for non-negative integers mi and ji, or else in a similar form related to the one above
by complex conjugation or by permutation of the entries {h11, h21, h31}. To simplify the
discussion, we will now assume that P (h) has the form (A.3), but the arguments used
below work equally well for the complex conjugate monomial or for the monomials related
to (A.3) by permutations of the entries. So there is no loss of generality.

    Multiplying h on the left by the element  = diag(e-2i, ei, ei), it is clear from (A.3)
that the monomial transforms as

                         P ( h) = ei(-2j1+j2-j1-j2) P (h) = e-3j1 P (h) .

As before, the invariance of the integral I[P ] under the change of variable h   h then
implies that the integral must vanish whenever j1 = 0. In the remaining case where
j1 = 0, the monomial (A.3) takes the simplified form

P (h) = h1m11 h2m12 hm313 2 hj221 h3j21 .                   (A.4)

Then choose the element ~ = diag(e, e-2i, ei) in SU(3) and multiply h by it on the left.
It follows from (A.4) that

P (~ h) = ei(-2j2-j2) P (h) = e-3j2 P (h) .

So the invariance of I[P ] by this operation implies that the integral also vanishes whenever
j2 = 0. Therefore, the integral I[P ] can be non-zero only when the monomial P (h) is a
simple norm hm111 h2m12 hm313 2, and this concludes the proof of the first part of the result.

Second part of the calculation
The second part of the proof of formula (A.2) is to compute the integrals

I[k1, k2, k3] :=             hk111 hk212 h3k13 2 volK .

                  hK

Let volHaar be the Haar volume form on K, i.e. the unique bi-invariant volume form with
total volume normalized to 1 [BD]. Since all bi-invariant volume forms are proportional
to each other,

I[k1, k2, k3] = (Vol K)      hk111 hk212 hk313 2 volHaar .

                         hK

The monomial P (h) = hk111 hk212 hk313 2 is invariant under right-multiplication of h by group
elements of the form (a) = diag(det a-1, a), for any a  U(2), since this multiplies the

entries hk1 by a phase only. Thus, P (h) descends to the quotient SU(3)/U(2)  CP 2.
In other words, there exists a complex function p on CP 2 such that P = p  , where

                         42
 : SU(3)  CP 2 is the projection associated to the quotient. A well-know result about
fibre-integration (see Proposition 5.16 of [BD]) then says that

                          P (h) volHaar =             p(z) volFS ,                       (A.5)

                      hK                       zCP 2

where volFS is the unique volume form on CP 2 that is invariant under the SU(3)-action
on this space and has total volume equal to 1. In other words, volFS is the normalized
volume form of the Fubini-Study metric on CP 2.

    Using homogeneous coordinates on projective space, the projection  : SU(3)  CP 2
has the simple form

                                         (h) = [ h11, h21, h31 ] .

It follows that the function p(z) on CP 2 corresponding to the monomial P can be repre-
sented in homogeneous coordinates as

      p([z1, z2, z3]) =                      z1k1 z2k2 z3k3 2       .
                                   |z1|2 + |z2|2 + |z3|2 k1+k2+k3

Indeed, the entries of any matrix h on SU(3) satisfy the identity k |hk1|2 = 1, so it is
clear that p  (h) = P (h).

    Now take the standard chart of projective space defined by the map (z1, z2)  [z1, z2, 1]
from C2 to CP 2. In this chart the function p looks like

      p^(z1, z2) = p([z1, z2, 1]) =                      z1k1 z2k2 2       .
                                               |z1|2 + |z2|2 + 1 k1+k2+k3

Moreover, in this standard chart the normalized Fubini-Study volume form is just

      volFS =         2          2             3 dx1  dy1  dx2  dy2 ,
                          1 + |z1|2 + |z2|2

where we have written zk = xk + iyk. Thus, the integral of p in the chart's coordinates is

       p(z) volFS  =  2                    z1k1 z2k2  2           dx1  dy1  dx2  dy2
                      2         1 + |z1|2 + |z2|2     3+k1+k2+k3
zCP 2                     C2

                      2            + +              r12k1+1 r22k2+1
                      2                        1 + r12 + r22 3+k1+k2+k3
                   =      (2)2                                                dr1 dr2 ,

                                0       0

where rk := |zk|. Changing the variables of integration from (r1, r2) to (r1, ), with the
new coordinate defined by tan  := r2/ 1 + r12, the preceding integral becomes

      + /2                 r12k1+1
                         + r12 2+k1+k3
8                     1                 (sin )2k2+1 (cos )2k1+2k3+3    d dr1  .

   0  0

                                           43
Defining a second change of variable by r1 = tan , the integral becomes

      /2 /2

8                        (sin )2k1+1 (cos )2k3+1 (sin )2k2+1 (cos )2k1+2k3+3 d d .

   0               0

But these integrals are related to the well-known beta function, which satisfies

   B(n, m)            =  2    /2                              =   (m - 1)! (n - 1)!      ,
                                                                    (m + n - 1)!
                                (sin )2n-1 (cos )2m-1 d

                            0

for any positive integers m and n. Thus, our main integral in just

       p(z) volFS     =  2 B(k1 + 1, k3 + 1) B(k2 + 1, k1 + k3 + 2)       =       2 k1! k2! k3!   .
                                                                             (2 + k1 + k2 + k3)!
zCP 2

This concludes the second part of the calculation.

A.2 Integrals of fourth order monomials hkj hmn hkj hmn

This part of the appendix lists a few explicit integrals over SU(N) than can be calculated
using general formulae found in [Cr]. The integrals are calculated either with respect to
the Haar volume form volHaar, which has total volume equal to one; or with respect to a
general bi-invariant top form volK, which will be proportional to volHaar and have total
volume Vol K.

Formula (23) in [Cr] says that, for any indices ki and li in {1, . . . , N },

                                  h h          volHaar  =  1    k1l2 l1k2 .                 (A.6)
                                    k1l1 k2l2              N
                         hSU(N )

Using this formula one can calculate that, for any bi-invariant volume form volK and any
square matrix v  MN (C),

                                 h v hT volK = 0                                            (A.7)

                            hK

                                 h v h volK    =   1    Tr(v) (Vol K) IN
                                                   N
                            hK

                                 h v h volK    =   1  (Vol K) vT  .
                                                   N
                            hK

The first formula in (A.7) is valid only when N > 2. By general invariance properties

under the change of variable of integration, as described in section 2 of [Ba], these integrals
remains unchanged if we substitute h by h, hT or h in the integrand function. Now

consider the integral of the fourth order monomial

   I(i1 j1 i2 j2; k1 l1 k2 l2) :=                       h h h h              volHaar  .     (A.8)
                                                        i1j1 i2j2 k1l1 k2l2
                                             hSU(N )

                                               44
Formulae (25) and (26) of [Cr] say that, for any values of the indices2,

N (N 2 - 1) I (i1 j1 i2 j2; k1 l1 k2 l2) = N     i1l1 i2l2 j1k1 j2k2 +     i1l2 i2l1 j1k2 j2k1
                                             -     i1l1 i2l2 j1k2 j2k1 +     i1l2 i2l1 j1k1 j2k2 . (A.9)

Using the preceding formula, after some index manipulation one can calculate that, for
any bi-invariant volume form volK and any square matrix v  MN (C),

    h h v h h volK =            h h v h h volK                            (A.10)

hK                          hK

                         =     Vol K     N v + (N 2 - 2) Tr(v) IN
                            N (N 2 - 1)

     hT h v (hT h) volK  =  Vol K  vT + Tr(v) IN  .                       (A.11)
                            N +1
hK

The value of the integrals remains unchanged if we substitute h by h, hT or h in the
integrand function.

A.3 Integrals of functions of the form q(h) h v h

The aim of this appendix is to establish two identities that are useful in the calculations
of the fibre-integrals studied in sections 2 and 3. They are identities for the integrals on
K of functions of the form q(h) h v h, where q(h) is a scalar function on the group having
certain invariance properties.

Proposition.

Let K be the Lie group SU(N) equipped with a bi-invariant volume form volK. Let v
be any square matrix on MN (C). Let q : K  C be a scalar function invariant under
left-multiplication on K by the following group elements:

   1. The element 1 = diag(-1, -1, 1, . . . , 1) and its conjugates k obtained by permuting
       the diagonal entries.

   2. The block-diagonal element 1 = diag(, -1, 1, . . . , 1) and its conjugates j obtained
       by permuting the diagonal blocks.

2Formula (25) of [Cr] is missing the factor j1k1 that appears in the first term on the right-hand side of
 (A.9). It is a typo and the factor should be there.

                                                         45
Here we have denoted

                                      := 0 1 .
                                               10

Then the function q(h) satisfies the following integral identities:

     q(h) h v h volK =             q(h) h v h volK  =  1  Tr(v) IN        q(h) volK . (A.12)
                                                       N
hK                            hK                                     hK

In particular, the first two integrals vanish when v is traceless.

Proof.
Consider the matrix-valued integral

                              Iq(v) :=      q(h) h v h volK .

                                        hK

Since the volume form volK is bi-invariant, the integral is invariant under a change of
variable of integration h  hh for any fixed element h in SU(N ). If furthermore q(h) =
q(hh) for the chosen element, then the integral satisfies the identity

                                     Iq(v) = h Iq(v) (h)                       (A.13)

in the space of N � N complex matrices. Choosing h among the diagonal group elements
k, it is clear that (A.13) can be true for all k only if Iq(v) is a diagonal matrix. Choosing
h among the matrices j, identity (A.13) further implies that the diagonal components
of Iq(v) must be equal to each other, that is, Iq(v) must be proportional to the identity
matrix IN . But in this case we have that

Iq(v) =  1  Tr  Iq(v)  IN  =  1  IN       q(h) Tr(h v h) volK  =  1  Tr(v) IN       q(h) volK,
         N                    N                                   N
                                     hK                                        hK

as required. Now consider the second matrix-valued integral

                              Jq(v) :=      q(h) h v h volK .

                                        hK

Using the bi-invariance of volK, the same argument as before says that if q(h) = q(hh)
for a fixed group element h and all h in SU(N ), then

                                     Jq(v) = Jq (h) v h                        (A.14)

in the space of N � N complex matrices. Since the integral identities (A.12) are linear in
the matrix v, it is enough to prove them for matrices with a single non-zero component.
If the non-zero component of v is off the main diagonal, then by choosing h to be the
appropriate element k, one can achieve that (h) v h = -v, and so identity (A.14) implies

                                            46
that Jq(v) vanishes in this case, in agreement with (A.12). If the non-zero component of
v is in the main diagonal, then by choosing h to be the appropriate element among the
j or their products, one can achieve that (h) v h has the same non-zero component as
v but in a different, arbitrary position within the main diagonal. Thus,

   Jq diag(1, . . . , N )  = Jq diag(1, 0, . . . , 0) + � � � + Jq diag(0, . . . , 0, N )
as required.
                           = (1 + � � � + N ) Jq diag(1, 0, . . . , 0)  =     Tr(v)  1  Jq(IN )
                                                                                     N

                           =  1  Tr(v)       q(h) volK ,                                   (A.15)
                              N
                                        hK

A.4 Integrals involving the functions s(h)

Let K be the Lie group SU(3) equipped with a bi-invariant volume form volK. Denote by
hkj the entries of a matrix h  K. In this appendix we will present the values of several
integrals over SU(3) involving the scalar functions

                                  s1(h) := h211 + h221 + h231                              (A.16)
                                  s2(h) := h11h21 + h11h31 + h21h31
                                   s(h) := 1 s1(h) + 2 s2(h) ,

where 1 and 2 are any complex constants.

Integrals of |s|2 and |s|4

The integrals of the functions |sa|2 and |sa|4 over (K, volK) can be calculated from the
general formula (A.2) for the integrals of complex polynomials in the entries hk1. The
results are

   |s1|2 volK = 2                          |s2|2 volK =   1  (Vol       K  )               (A.17)
                                                          2
K                                       K

   s1 s2 volK = 0

K

                                        47
for integrals quadratic in the functions sa. For integrals involving four-fold products of
those functions we have

                           |s1|4 volK   =    1  (Vol  K  )                                 (A.18)
                                             3
                        K

                           |s2|4 volK =            |s1 s2|2 volK  =  1   (Vol  K)
                                                                     10
                        K                       K

                    |s2|2 s1 s2 volK    =    1   (Vol  K    )
                                             30
                 K

                    |s1|2 s1 s2 volK = 0 .

                 K

From these results, one obtains that any linear combination s = 1s1 + 2s2 satisfies

   |s|2 volK  =  1   2 |1|2 + |2|2 (Vol K)                                                 (A.19)
                 4
K

   |s|4 volK  =  1      10 |1|4 + 3 |2|4 + 18 |12|2 + 2 |2|2(12 + 12)                   (Vol K) .
                 30
K

Integrals of the form |s|2 h v h

For any square matrix v  M3(C) one can show that

                           |s|2 h v h volK = B1                   |s|2 volK                (A.20)

                        K                                      K

                           |s|2 h v h volK = B2                   |s|2 volK ,

                        K                                      K

where the matrices B1 and B2 are defined by

B1  :=  1  Tr(v) I3  +  1   (2  v11  -  v22  -  v33)  |2|2  + 2 (12 + 12)          0    1  1
        3               30                                  2 |1|2 + |2|2          1    0  1
                                                                                        1

                                                                                     1     0

B2  :=  1  Tr(v) I3  +  1   |2|2 + 2 (12 + 12)                      vjk diag(-2, 1, 1) .   (A.21)
        3               30        2 |1|2 + |2|2
                                                               j=k

Observe how B2 is a diagonal matrix, unlike B1. Both these matrices are much simpler
when the coefficients a are such that |2|2 + 2 (12 + 12) vanishes, i.e. when the
function s(h) coincides with one of the functions s(h) defined in (2.104). They are also
simpler when v is a traceless matrix.

    These formulae are manifestly true when v is proportional to the identity matrix I3,
for in this case h v h = h v h = v and also B1 = B2 = v. Since any square matrix in

                                                 48
M3(C) can be decomposed as sum v = I3 + w + iu, where  is a complex number and
u and w are matrices in su(3), it is clear that the formulae will be true in general if they
hold for matrices in su(3). The calculation for the case v  su(3) takes several pages.
It can be done considering separately the integrals of the functions s1(h) and s2(h) and
using the results in appendices A.1 and A.3. It is also useful to consider separately the
case where v belongs to the subspaces (su(2)) or (C2) of su(3), since in this case many
of the integrals involved can be shown to vanish by symmetry arguments. The calculation
in the case where v is proportional to diag(-2i, i, i), on the other hand, uses the results
of appendix A.1. A relevant intermediate step is the calculation that

   Re  1 s1 2 s2   h v h volK  =   1   (Vol  K   )       vjk   (12 + 12) diag(-2, 1, 1)
                                  120
K                                                   j=k

                                   1                                            0 1 1
                                  120
  Re 1 s1 2 s2     h v h volK  =       (Vol  K )(2v11  -  v22  -  v33)(12    +  12)  1  0  1
                                                                                        1    
K                                                                                    1
                                                                                           0

These two integrals hold also in the general case v  M3(C).

Integrals involving Lie derivatives of s(h)

Here we list the values of a group of integrals involving the Lie derivatives LvL and LvR
of the functions sa(h) and s(h) along left and right-invariant vector fields on K = SU(3).
These functions depend on the entries hk1 of the matrix h  SU(3), so their Lie derivatives
depend on the basic derivatives

                   LvL hkj     =  d    h exp(tv) kj |t=0       =  (h v)kj               (A.22)
                   LvR hkj        dt

                               =  d    exp(tv) h kj |t=0 = (v h)kj ,
                                  dt

where v is any matrix in su(3). The calculation of the integrals involving the Lie deriva-
tives of s(h) makes extensive use of formula (A.2) for the integrals of complex polynomials
in the entries of any column or row of h  SU(3).

For indices a, b  {1, 2}, the basic integrals involving Lie derivatives along left-invariant

vector fields are

                      sa LvL sb volK = 2 ab v11                |sa|2 volK ,             (A.23)

                   K                                      K

where no sum is intended over the repeated index a. The analogous integrals for deriva-

                                             49
tives along right-invariant vector fields are

         s1  LvR s1  volK   =0                                                                (A.24)
             LvR s2  volK
      K      LvR s2  volK   =  1           vjk        |s2|2 volK
                               3
         s2                         j, k           K

      K                     =          s2  LvR s1     volK      =  1   (Vol  K)        vjk .
                                                                   6
         s1                         K                                            j, k

      K

Notice that for any matrix in su(3) the sum of its entries is an imaginary number,

      vjk =          vjk =          vjk - vjk = 2 i Im v12 + v13 + v23 .                      (A.25)

j, k         j=k            j<k

Combining the preceding integrals for the functions s1 and s2, one gets that linear com-
binations s = 1s1 + 2s2 satisfy

   s LvL s         volK    = 2 v11        |s|2 volK                                           (A.26)
                   volK
K                                   K

   s LvR s                 = |2|2 + 2 (12 + 12)                        vjk      |s|2 volK .
                                   3 2 |1|2 + |2|2
K                                                                  j, k      K

The integral in the second line vanishes for all right-invariant fields vR whenever the
coefficients a are such that |2|2 + 2 (12 + 12) equals zero, i.e. when the function
s(h) coincides with one of the functions s(h) defined in (2.104).

    The scalar Laplacian on K equipped with a left-invariant metric can be written as
s = k LekL LekL s, where {ek} is an orthonormal basis of the Lie algebra. The calcu-
lations of section 4.3 deal with those Laplacians and the following integral identities are
used there. Firstly, for any v  su(3) and any square matrix u  M3(C), we have

         sa        LvL sb  h u h volK      =   -   2  ab   v11  Tr(u)     |sa|2 volK          (A.27)
                                                   3
      K                                                                K

                s  LvL s   h u h volK      =   -   2  v11  Tr(u)      |s|2 volK .
                                                   3
             K                                                     K

Secondly, for any pair of matrices u, v in su(3), we have that

   s1 LuLLvL s2 volK =            s2 LuLLvLs1 volK = 0                                          (A.28)

K                              K                                                    |s|2 volK .

     s LuLLvL s volK =         2 u11 v11       +   2     4 |1|2        (uv)11    K
                                                      |1|2 + |2|2
   K

                                               50
A final group of integral identities involving the derivatives of the functions sa are

   |s1|2 s2  LvR s2  volK  =   7   (Vol  K   )        vjk  =-        |s1|2 s2  LvR s2  volK
                              180
K                                               j, k              K

   |s2|2 s1  LvR s1  volK  =  1    (Vol  K)           vjk = -        |s2|2 s1  LvR s1  volK ,  (A.29)
                              45
K                                               j, k              K

for any matrix v  su(3).

B Laplacian of equivariant functions on SU(3)

Let  : SU(3) � V  V be a linear group representation and let d : su(3) � V  V
be the induced Lie algebra representation. For a fixed inner-product g on su(3), pick an
orthonormal basis {ej} of this space and define an endomorphism g : V  V by

                                             8

                              g :=              (d)ej (d)ej .                                  (B.1)

                                         j=1

It is easy to check that g does not depend on the choice of orthonormal basis. This
operator on V is the Casimir element associated to the product g and the representation
d of su(3). It emerges naturally when studying the action of the scalar Laplacian Kg
on functions SU(3)  V that are equivariant with respect to the representation. Such
functions are determined by their value at the identity element, since f (h) = h f (I3) .
Their Lie derivatives with respect to left-invariant vector fields are simply

(LvLf )(h)   =  d    f  h exp(tv)  |t=0  =      d     h  exp(tv)  f (I3)  |t=0 = h  (d)v       f (I3)
                dt                              dt

(LuL LvLf )(h) = h  (d)u  (d)v f (I3) .

If the product g on su(3) is extended to a left-invariant metric on the whole group K =
SU(3), then it follows from the general formula (3.11) for the scalar Laplacian that

(Kg f )(h) =                  h  (d)ej  (d)ej f (I3) = h  g f (I3) .

                           j

This means that gKf is also -equivariant on SU(3) and that its value at the identity is
just g f (I3) . In particular, if the vector f (I3) is an eigenvalue of the algebraic operator
g, then the function f is an eigenfunction of gK with the same eigenvalue.

                                                51
Fundamental representation

In the case where  : SU(3) � C3  C3 is the fundamental representation, then

                                              8

                                       g =       ej ej                          (B.2)

                                            j=1

is the 3 � 3 hermitian matrix that appears in section 3.3. More precisely, it appears in

formulae (3.19), (3.22) and (3.26) that define the matrices Dg , gb and cg, respectively.
The latter matrices determine the action of the internal Laplacian gK on the components
of the higher-dimensional spinors P (x, h), after pairing and fibre-integration.

    When the inner-product on su(3) is the one defined in section 2 of [Ba], denoted by
g, the explicit orthonormal basis {v0, . . . , v3, w1, . . . , w4} constructed there can be used
to calculate that

g  =               -1                 8 - 25||2 + 8||4           3 (1 - 4||2)   .
      3  (1 - ||2) (1 - 4||2)
                                       3 (1 - 4||2)  (8 - 34||2 + 8||4)I2 + 9 

This matrix is manifestly hermitian and only depends on the parameters  and ||2 that
appear in the definition of g. In the special case where the deformation parameter
vanishes,  = 0, the product g reduces to the usual Ad-invariant product  on su(3) and
the matrix g is proportional to the identity matrix,

                                         =  -     8  I3  .
                                                 3

When  = 0, one can calculate that the matrix g has the following three independent

eigenvectors in C3:

                                0                            �|| 

                         u1  =     2             u�      =    1  .


                                   -1                         2

Their respective eigenvalues are found to be

                     �1  =   -    8 - 34||2 + 8||4                              (B.3)
                                3  (1 - ||2) (1 - 4||2)

                     ��  =   -  8  -  25||2 + 8||4 � 3 || (1 - 4||2)  .
                                        3  (1 - ||2) (1 - 4||2)

They reduce to the unique value -8/(3 ) when the parameter  vanishes, of course. The
formulae of section 3.3 also include the scalars Tr(g) and (g)11. When g = g, these
can be easily read from the explicit formula of g given above. Other related scalars and

                                            52
matrices that appear in the same formulae of section 3.3 are

               8                     2 (1  -  ||2)
                                      (1   -  4||2)
                  (ej )121  =  -  3                                                          (B.4)

             j=1

          8                            1             -2 (1 - ||2)         3 
                               3  (1 - 4||2)
               (ej )11 ej   =                            3         6  + (1 - 4||2) I2     .

          j=1

Both these identities were calculated using the explicit g-orthonormal basis of su(3)
described in [Ba]. Although the actual calculation of g is not presented here, we will
finish this section by writing down some of the intermediary expressions that lead to the
formula below (B.2). Using the basis {v0, . . . , v3, w1, . . . , w4} mentioned above, we get

                      3                       -1        3 ||2              3 
                                                                 (3 + 2||2) I2 - 
                        va va =      2  (1 - ||2) 3 

                    a=1              -1 2 0          ,                                       (B.5)
                                       0 I2
                    4

                       wk wk =

                  k=1

and the longer expression

v0 v0  =               -1                     4 + ||2 + 4||4              -3 (1 - 4||2)      .
          6  (1 - ||2) (1 - 4||2)
                                              -3 (1 - 4||2)  (1 - 4||2)2 I2 + 3 (7 - 4||2) 

Adjoint representation

In the case where  : SU(3) � su(3)  su(3) is the adjoint representation, the Casimir
element associated to g is the following endomorphism of su(3):

                                           8                8

                               g :=           adej adej =          ej, [ej, � ] .

                                     j=1                    j=1

When the inner-product on su(3) is the one defined in section 2 of [Ba], denoted by g,
an explicit calculation using the orthonormal basis of su(3) defined there shows that

                            g ()           =  -         6 (1 - 2 ||2)     ()       ,
                                                   (1 - ||2) (1 - 4 ||2)

where   C2 is the deformation parameter of g and  : u(2)  C2  su(3) is the vector
space isomorphism used in [Ba]. This exhibits the first eigenvector and eigenvalue of g
for deformed metrics with  = 0. Four more eigenvectors can be written down using the
matrices w1 and w2 defined in the first appendix of [Ba]. These matrices belong to the

                                                     53
subspace [su(2)] of su(3) and an explicit calculation shows that

         g w1 � ||-1 w1, ()     = - �� w1 � ||-1 w1, ()                               (B.6)
         g w2 � ||-1 w2, ()     = - �� w2 � ||-1 w2, () ,

where the two degenerate eigenvalues �� are the real numbers

              ��     :=  6  -  23 ||2 + 8 ||4 � || (1 - 4 ||2)    .                   (B.7)
                                   (1 - ||2) (1 - 4 ||2)

We have exhibited five eigenvectors of g so far. Since this operator is self-adjoint
with respect the Ad-invariant product  on su(3), we know that the three remaining
eigenvectors will lie in the -orthogonal complement to the subspace generated by the
first five eigenvectors. This -orthogonal complement is spanned by the three matrices:

e1   =   1    (iI2)      e2 = ||-1 (i)     e3 =  2i ||-2  - i I2 .
           3

The span of these matrices is necessarily an invariant subspace of su(3) under the action
of g. In fact, in the basis {e1, e2, e3} the operator can be identified with the 3 �3 matrix

                     g      =               1          ^ g  ,                         (B.8)
                                (1 - ||2) (1 - 4 ||2)

where ^ g stands for the symmetric matrix

          3 (-2 + 7||2 - 2||4)                                     ||2         2||2)  
                                  3 3 || (1 - 2||2)            -3
                                -2 (3 - 10||2 + 4||4)                   (1  +
           3 3 || (1 - 2||2)
^ g  :=                              || (10||2 - 1)               || (10||2 - 1)        .


           - 3 ||2 (1 + 2||2)                                  -6 + 23||2 - 2||4

We will not be able to offer an explicit expression for the eigenvalues and eigenvectors of
^ g as a function of ||2.

                                54
C HDR to special relativity

Null geodesics on the higher-dimensional spacetime

In this secluded appendix we discuss a kinematic model for particles moving in the higher-
dimensional spacetime P = M4 � K equipped with a product metric gP = gM � gK. The
metric on Minkowski space is taken with the usual form

                 gM = dx1  dx1 + dx2  dx2 + dx3  dx3 - c2 dt  dt .

The model's framework is that physical particles always follow null geodesics on P and, as
usual in Kaluza-Klein theories, a particle's mass and electromagnetic charge are quantities
related to its motion along the internal space K. Thus, the null geodesic of a particle at
spatial rest in Minkowski space must correspond to a vertical movement in internal space
K at full speed c. That would be the source of the energy of a particle at three-dimensional
rest. Conversely, a particle moving at speed c on Minkowski space corresponds to a
horizontal null geodesic that cannot have any additional vertical component, and hence
the particle has no mass or charge in the frame. While all vertical movement is perceived
as mass in four dimensions, electromagnetic charge is related to the component of internal
velocity along a specific Killing direction inside K. So there can be mass without charge
but not the other way around. These classical rules incorporate the fact that a particle is
massless if and only if it travels at speed c in M4, and that no charged massless particles
have ever been observed. Having a unique finite speed c for all fundamental particles is
also an attractive feature, simpler than having a closed interval [0; c] of possible speeds.
The inescapable price is having to work with a higher-dimensional spacetime, of course.

    Let (s) be a null geodesic on P and let M (s) and K(s) be its projections onto the
factors M4 and K, respectively. Since the metric on P is the product metric, the curves
M (s) and K(s) are geodesics on the respective spaces. Denote by  (s) =  M +  K the
tangent vectors to P obtained by derivation of (s) with respect to the parameter s. The
fact that the geodesic is null is equivalent to

                                gK( K,  K) = - gM ( M ,  M ) .                                             (C.1)

Since the left-hand side is non-negative for any Riemannian metric on K, the projection

M (s) must be a time-like or null geodesic on Minkowski space. The quantity gK( K,  K)

then  coincides  with  the  square    of  c  times  d   ,  the  rate  of  change   with   respect  to   s  of  the
                                                    ds

proper time  associated to the particle in free fall along the geodesic M (s).

Let us describe this in more detail.                Since      the  vector  field     is  Killing  on  M4,     the
                                                                                   t

internal  product  gM ( M ,     )  =  -c2 (dt)( M )        is  constant   and  independent  of     the  param-
                             t

eter s. In particular, after an affine reparameterization if necessary, we may pick the

                                                    55
parameter s of the geodesic so that (dt)( M ) is equal to 1 everywhere along the curve. It
is possible to do this for every null geodesic (s) except the trivial one. It is equivalent

to choosing the time coordinate t as the parameter of the geodesic. With this choice, the
quantities (dxk)( M ) can be identified with the particle's physical velocities vMk along the
xk-direction, for k = 1, 2, 3, in the given coordinate system on M4. So the particle's speed
along Minkowski space in this frame is

    vM := (vM1 )2 + (vM2 )2 + (vM3 )2 =               gM   dM     ,  dM   + c2 .
                                                            dt        dt

The particle's speed along the internal space K, as seen in the same frame with time

coordinate t, is given by

                               vK :=  gK      dK   ,  dK   .
                                               dt      dt

The condition that the geodesic (t) is null can then be rephrased as

                               vM2 + vK2 = c2 .                                   (C.2)

Thus, the particle's speed along M4 always lies between zero and c, for any null geodesic
on P and any Minkowski coordinates. In a coordinate system on M4 where the particle
is at rest, i.e. a coordinate system with vM = 0, the time coordinate t =  must be
such that the speed of the particle along the internal space has the value vK = c. In a
coordinate system with vM > 0, the time coordinate t is such that the internal speed is

   c2 - vM2 . The Riemannian distance travelled by the particle along the internal space
K, as the geodesic's parameter evolves from s1 to s2, is related to the particle's proper
time by

s2                         s2                               (s2)

    gK ( K,  K) ds =           -gM (M , M ) ds =                  c d = c  (s1) -  (s2) .

s1                         s1                               (s1)

Thus, in this model the particle's proper time is a direct measure of the distance travelled
in internal space. Expression (C.2) also tells us that the set of null geodesics starting from
a fixed point in P and moving forward in time, up to affine reparameterizations, defines
a "celestial" sphere inside a space of velocities of dimension dim M4 - 1 + dim K. In
other words, it is a set parameterized by a topological sphere of dimension 2 + dim K.

    Since a geodesic on P can be reconstructed from its components on M4 and K, let us
spend a few lines discussing the geodesics K(s) on internal space. When the group K
is equipped with a general left-invariant metric gK, the problem of finding its geodesics
is not a simple one. It is well-known that the second order geodesic equation can be
replaced by two natural, first-order differential equations: the Euler-Arnold equation for

                                          56
a curve w(s) in the Lie algebra k of K; and a linear differential equation to reconstruct
the geodesic K(s) on the group from the solution w(s) on k. In the case of a matrix
group, these two equations can be written as [Ar, MP]

    gK(w , u) = gK w, [w, u]            for all u  k
           K = K(s) w(s) .
                                                             (C.3)

Although these equations are difficult to solve in general, simple solutions can be written
when the metric gK has left-invariant Killing fields. If w  k is a vector such that
LwLgK = 0, then the formula for this derivative presented in section 2.2 of [Ba] says
that gK(w, [w, u]) vanishes for all u  k. So the constant function w(s) = w and the
curve (s) = h exp(s w) are solutions of (C.3), and hence define a geodesic on K starting
at the point h. In the special case of a bi-invariant metric gK, the vector fields wL are
Killing for all w  k, so this procedure generates all the geodesics on K. In the case
where K = SU(3) is equipped with the left-invariant metrics g, or with the more general
variants g~ defined in [Ba], the isometry group is U(1) � SU(3). Up to normalization, only
the electromagnetic vector e  su(3) defines a left-invariant Killing field eL on the group
manifold.3 Thus, the closed curves s  h exp(s e) are the only explicit geodesics of the
metric g constructed in this way.

    Now consider again a general geodesic (s) on the higher-dimensional P . As usual, if
X is a Killing vector field for the metric gP , we have that

d   gP ( ,  X)  |(s)  =  gP (  , X)  +  gP ( ,  X)    =  0.
ds

So the internal product gP ( , X) is constant along the geodesic (s). For a product metric
gP = gM � gK this means that, besides the constants of motion associated to the Killing
fields of Minkowski space, for every geodesic there are additional constants of motion
related to the Killing fields of the internal metric gK. In the case where K = SU(3) is
equipped the left-invariant metrics g of [Ba], we have nine constants of geodesic motion
associated to the isometry group U(1) � SU(3). These are the products of  K with the
right-invariant vector fields, g( K, vR), for any v  su(3), and the product g( K, eL)
with the left-invariant field generated by the electromagnetic vector e  su(3). In the
next paragraph we will verify that, as usual in Kaluza-Klein theories, the constant of
motion g( K, eL) can be identified with the particle's charge to mass ratio.

3The electromagnetic vector inside su(3) is denoted by  in [Ba] and in the other sections of the present
 study. In this section it is denoted by e to avoid confusion with the notation  for the geodesics.

                                                         57
Turning on the gauge fields

As in section 3 of [Ba], let the higher-dimensional spacetime P = M4 � K be equipped
with a metric gP determined by: a metric gM on M4; a fixed metric gK on the fibres K;
one-forms AL and AR on M4 with values in the Lie algebra of K. By construction, the map
 : P  M4 is a Riemannian submersion. Any curve (s) on P can still be reconstructed
from its projections M (s) and K(s). However, the decomposition  (s) =  M + K of
the tangent vector is no longer orthogonal with respect to gP . Instead, the orthogonal
decomposition defined by the metric gP is now  (s) =  V +  H. The two decompositions
are related by

            V =  K - ALj ( M ) eLj + ARj ( M ) eRj    (C.4)
            H =  M + ALj ( M ) eLj - ARj ( M ) ejR ,

where {ej} is a basis of the Lie algebra of K. Writing the geodesic equation on P as
P  , where P is the Levi-Civita connection associated to gP , one can ask how this
equation looks like once decomposed into its horizontal and vertical components. This
decomposition can be obtained from a more general calculation in [O'N] about parallel
transport in Riemannian submersions. Adapting the notation, it implies that for any
vertical vector V and horizontal vector X on T P ,

gP P  , V  = gP P  V , V - gP SV  V ,  H                              (C.5)
gP P  , X  = gM MM  M , X + 2 gP FX  H,  V  + gP S V  V , X .

The notation here is as in section 3 of [Ba]. So the tensor S : V � V  H is the second

fundamental form of the fibres K; the tensor F : H � H  V is essentially the curvature
of the gauge fields; the covariant derivative MM M is a vector field on the curve M (s)
over M4.

    Let M (s) be an arbitrary curve on M4 and let (s) be a horizontal lift of that curve
to P . Then  V = 0 by definition. Inspecting (C.5), it is clear that in these conditions the
product gP P  , V vanishes for all vertical V , while the product gP P  , X vanishes
precisely if gP MM  M , X is zero. Thus, we recognize that P  = 0 is equivalent
to M M  M = 0. A horizontal curve (s) is a geodesic on P if and only if its projection
M (s) is a geodesic on M. If the horizontal curve (s) is null on P , then we have that
0 = gP ( H,  H) = gM ( M ,  M ), and the curve M (s) is null on M too. Thus, in this model
all particles that travel at speed c on M4 are following horizontal null geodesics on P that
project down to null geodesics on M4. In particular, the motion in M4 of particles that
travel at speed c is not directly affected by the presence of the gauge fields AL and AR,
they follow geodesics determined by gM solely. In other words, although the metric gP

                             58
and the geodesic motion on P are affected by the presence of gauge fields, the projection
of this motion down to M4 is independent of the gauge fields in the case of particles
travelling at speed c on M4. This will not be the case for particles travelling at lower
speeds on M4, since the corresponding geodesics on P have non-zero vertical components
 V that, according to (C.5), couple to the gauge fields through the non-vanishing tensors
F and S.

    Let (s) be a general geodesic on P satisfying P  = 0. Then the first equation in
(C.5) implies that the norm of the vertical component  V evolves according to

            d         gP   V ,  V   = 2 gP P  V ,  V         = 2 gP S V  V ,  H .  (C.6)
            ds

If the geodesic (s) is null on P , then we also have that

                          gP  V ,  V = -gP  H,  H = -gM  M ,  M .

So the norm in M4 of the tangent to the projected curve M (s) may not be constant as
the parameter s varies. The (zero) norm of the full tangent vector  is always preserved

along the geodesic, but the norm of the individual components  V and  H may change,

with opposite signs, in regions of Minkowski space where the tensor S is non-zero, i.e. in

regions where the fibres of P are not totally geodesic. In those regions the rate of change

of  proper  time  d   may  not  be  constant  along  M (s).
                  ds

    Applying the formula for the tensor F given in section 3 of [Ba], the term FX  H can
be written more explicitly in terms of the curvature forms of the gauge fields,

                  2 FX  H = FAj L X,  H eLj - FAj R X,  H eRj .                    (C.7)

Since the projection  H is just  M , it follows from the second equation in (C.5) that
the curve M (s) on Minkowski space obtained by projecting down a geodesic (s) on P
satisfies the equation of motion

gM MM  M , Y = gP (ejR,  ) FAj R Y,  M - gP (ejL,  ) FAj L Y,  M - gM  S V  V , Y

for all vectors Y  T M. Unless the fibre-metric gK is bi-invariant, this equation for the
curve M (s) on M4 is still strongly coupled to the vertical component of the geodesic (s),
through factors like gP (eLj ,  ) and the vector S V  V .

    The decomposition (C.5) of the geodesic equation on P simplifies considerably in
regions of Minkowski space where the tensor S vanishes. This happens, for example, in
regions where the left-invariant fibre metric gK is constant across the fibres and where
the only non-vanishing gauge fields are the massless ones. More precisely, let us assume
that we are in a region U of M4 where the background metric gP satisfies the following
two conditions:

                                              59
� The inner-product gP (uL, vL) is a constant function on -1(U ) for any left-invariant
   vector fields uL and vL on K, regarded as fields on P .

� The one-form AR is arbitrary but AL is such that the vertical fields ALj (X) ejL are
   Killing for the fibre metric gK, for all tangent vectors X  T U.

In this case, it follows from the formula of section 5.3 of [Ba]:

            2 gP ( SuLvL, XH) = - LX gP (uL, vL) - AkL(X) (LeLk gK)(uL.vL) ,

that the tensor S -- the second fundamental form of the fibres -- vanishes identically
over the region U, and so the fibres are totally geodesic. If we take a null geodesic
(s) on P and project it down to Minkowski space, M =   , it is a consequence of
(C.6) that the norms of the horizontal and vertical components of  , namely gM M , M
and gP  V ,  V , will both be constant along (s). Moreover, the decomposition (C.5) is
simpler in this region of P . It implies that for a geodesic (s), any vertical vector V  T P
and any Y tangent to M4, we have

           gP (  V , V ) = 0                                                (C.8)
        gM MM  M , Y = gP (ejR,  ) FAj R Y,  M - gP (ejL,  ) FAj L Y,  M .

Thus, the projection on Minkowski space of the higher-dimensional geodesic is a curve
M (s) satisfying an equation of motion on M4 similar to the Lorentz-force law, only with
more gauge fields involved. The inner-products gP (eRj ,  ) and gP (eLj ,  ) play the role of
"charges", coupling the geodesic equation for M with the curvature of the background
gauge fields. We will now investigate the extent to which these inner-products are constant
along the geodesic (s), so that (C.8) truly resembles a Lorentz-force equation of motion.

    Let V be a vector field on K, regarded as a field on P that is constant along the
M4-directions. Then along a geodesic (s) we have that

d   gP  V,   = gP  V,   = gP  H V,  H + gP  V V,  H
ds                                     + gP  H V,  V + gP  V V,  V . (C.9)

The first term on the right-hand side always vanishes. Indeed, using that  is the Levi-
Civita connection, that V is vertical and hence orthogonal to  H, and the definition of
the tensor FXY and its anti-symmetry, one calculates that

gP  H V,  H = L H gP V,  H - gP V,  H  H = - gP V, F H  H = 0 .

                        60
The second term on the right-hand side of (C.9) can be written in terms of the second
fundamental form of the fibres, which vanishes on -1(U) as already discussed,

             gP  V V,  H = gP S V V,  H = 0 .

The last term on the right-hand side of (C.9) only involves vertical fields, so well-known
properties of Riemannian submersions [Bes, section 9.C] say that it can be calculated
using the fibres' Levi-Civita connection K. In particular, if V is a Killing field of the
fibre metric gK, we have

             gP  V V,  V = gK K V V,  V = 0 .

To calculate the third term on the right-hand side of (C.9), let us take care and consider
an extension of  to a local vector field ^ defined on an open set of P around the curve
(s). By assumption, the geodesic (s) is non-trivial and null, so the projection M = 
is locally injective and the extension ^ can be taken of the form

                                  3

^(x, h) = ^H(x, h) + ^V (x, h) =        a�(x) X�H |(x,h) +     bj(x) eLj |h .

                                  �=0                       j

Here (x, h) are the coordinates on M4 � K; the coefficients a�(x) and bj(x) are real
functions on an open set of M4; we have picked a basis {ej} for the Lie algebra k and
a basis {X�} for the tangent space T M; the symbol X�H denotes the lift of X� to a
horizontal, basic vector field on P . Using the properties of the Levi-Civita connection on

P , we then have that

        gP ^H V, ^V  = gP V ^H + ^H, V , ^V                                         (C.10)
                     = - gP ^H, V ^V + gP ^H, V , ^V
                     = - gP ^H, SV ^V + gP ^H, V , ^V
                     = a� bj gP X�H, V , ejL .

Using the explicit expression of the basic lift X�H, as appears in the definition of the
higher-dimensional metric gP , we can also write

        X�H, V = X�, V + AiL(X�) eLi , V - AiR(X�) eRi , V .

But V is a vector field on K while X� is a field on M4, so the bracket X�, V necessarily
vanishes on P . Moreover, by definition of the extension ^, we have that bj ejL =  V and
that a� AiL/R(X�) = AiL/R( M ) over the curve (s). Thus, bringing all the calculations
together, we obtain that for any Killing field V on the internal space K, regarded as a

vector field on P , the inner-product with the tangent  to the geodesic evolves as

d   gP  V,   = ALi ( M ) gP  eiL, V ,   - AiR( M ) gP  eiR, V ,                     (C.11)
ds

                                  61
in the region -1(U) where the fibres of P are totally geodesic. In the special case where
the Killing field V is a purely left-invariant or right-invariant one, then making use of the
general relations between the Lie bracket of invariant vector fields and the bracket on the
Lie algebra,

[uL, vL] = [u, v]Lk            [uR, vR] = -[u, v]Rk               [uL, vR] = 0 ,

we obtain the simpler evolution equations

    d                gP  vL,   = gP            AL( M ), v L,                      (C.12)
    ds

    d                gP  vR,   = gP            AR( M ), v R,   .
    ds

Again, bear in mind that these equations are valid only when vL or vR are Killing for gK
and in regions of Minkowski space with totally geodesic fibres.

    To finish this appendix, let us now come back to the case where K = SU(3) is equipped
with the left-invariant fibre metric gK = g with U(1) � SU(3) isometry, as studied in
[Ba]. Suppose that the Higgs-like field  is constant over a region of Minkwoski space
where the one-form AR is arbitrary but AL = ALe e has values in the line spanned by
the electromagnetic vector e inside su(3). This means that the strong-force and elec-
tromagnetic gauge fields are arbitrary but all the weak-force gauge fields vanish. Since
the left-invariant extension eL is Killing for g, and all right-invariant fields are Killing
as well, we are in the conditions where the tensor S vanishes and the simpler equations
(C.8) and (C.12) are valid. In particular, for any geodesic (s) on P we have that

d   gP  eL,              = ALe ( M ) gP        e, e L,         = 0.
ds

This means that in the second equation of (C.8), which now reads

gM M M  M , Y = - gP (eL,  ) FAeL Y,  M +            gP (ejR,  ) FAj R Y,  M ,

                                               j

the coefficient gP eL,  of the electromagnetic field-strength FAeL is constant along (s).
As usual in five-dimensional Kaluza-Klein theories, comparing with the Lorentz-force
equation of motion of a moving charge in M4, one recognizes that the constant -gP eL, 
can be identified with the charge to mass ratio q/m of the particle in free fall along the

higher-dimensional geodesic (s).

                                           62
References

[Ar] V. Arnold: Sur la g�eom�etrie diff�erentielle des groupes de Lie de dimension infinie
          et ses applications a` l'hydrodynamique des fluides parfaits, Ann. Inst. Fourier 16
          (1966), 319�361.

[BH] J. Baez and J. Huerta: The algebra of grand unified theories, Bull. Amer. Math.
          Soc. 47 (2010), 483�552.

[BL] D. Bailin and A. Love: Kaluza-Klein theories, Rep. Prog. Phys. 50 (1987), 1087�
          1170.

[Ba] J. Baptista: Higher-dimensional routes to the Standard Model bosons.

[Bar] C. B�ar: The Dirac operator on homogeneous spaces and its spectrum on 3-
          dimensional lens spaces, Arch. Math. 59 (1992), 65�79.

[Bes] A. Besse: Einstein manifolds, Classics in Mathematics, Springer-Verlag, 1987.

[Ble] D. Bleecker: Gauge theory and variational principles, Addison-Wesley, 1981.

[BHM] J. Bourguignon, O. Hijazi, J. Milhorat, A. Moroianu and S. Moroianu: A spino-
          rial approach to Riemannian and conformal geometry, European Mathematical
          Society, 2015.

[BD] T. Brocker and T. Dieck: Representations of compact Lie groups, Graduate texts
          in Mathematics, Springer-Verlag, 1985.

[CJ] R. Coquereaux and J. Jadczyk: Geometry of multidimensional universes, Com-
          mun. Math. Phys. 90 (1983), 79�100.

[Cr] M. Creutz: On invariant integration over SU(N), J. Math. Phys. 19 (1978), 2043�
          2046.

[DN] J. D'Atri and H. Nickerson: The existence of special orthonormal frames, J. Diff.
          Geom. 2 (1968), 393�409.

[DNP] M. Duff, B. Nilsson and C. Pope: Kaluza-Klein supergravity, Physics Reports
          130 (1986), 1�142.

[GG] H. Georgi and S. Glashow: Unity of all elementary-particle forces, Phys. Rev.
          Lett. 32 (1974), 438�441.

                                                       63
[Ham] M. Hamilton: Mathematical gauge theory: with applications to the Standard Model
          of particle physics, Universitext, Springer International Publishing, 2017.

[Ho] P. Hogan: Kaluza-Klein theory derived from a Riemannian submersion, J. Math.
          Phys. 25 (1984), 2031�2035.

[K] T. Kaluza: Sitzungsber. Preuss. Akad. Wiss. Berlin Math. Phys. K1 (1921), 966.
          O. Klein: Z. Phys. 37 (1926), 895.
          B. DeWitt: Lectures at 1963 Les Houches School, Gordon and Breach, 1964.
          R. Kerner: Ann. Inst. H. Poincar�e 9 (1968), 143.
          A. Trautman: Rep. Math. Phys. 1 (1970), 29.
          Y. Cho: J. Math. Phys. 16 (1975), 2029.
          Y. Cho and P. Freund: Phys. Rev. D12 (1975) 1711.
          J. Scherk and J. Schwarz: Phys. Lett. 57B (1975), 463.
          E. Cremmer and J. Scherk: Nucl. Phys. B108 (1976), 409.

[MP] K. Modin, M. Perlmutter, S. Marsland and R. McLachlan: On Euler-Arnold
          equations and totally geodesic subgroups, J. Geom. Phys. 61 (2011), 1446�1461.

[O'N] B. O'Neill: Submersions and geodesics, Duke Math. J. 34 (1967), 363�373.
[OW] J. Overduin and P. Wesson: Kaluza-Klein gravity, Physics Reports 283 (1997),

          303�380.
[Wei] S. Weinberg: Charges from extra dimensions, Physics Letters 125B (1983), 265�

          269.
[Wei2] S. Weinberg: The quantum theory of fields, vol. 2, Cambridge Univ. Press, 1996.
[Wi1] E. Witten: Search for a realistic Kaluza-Klein theory, Nucl. Phys. B 186 (1981),

          412�428.
[Wi2] E. Witten: Fermion quantum numbers in Kaluza-Klein theory, Print-83-1056,

          Princeton (1981).

                                                       64
