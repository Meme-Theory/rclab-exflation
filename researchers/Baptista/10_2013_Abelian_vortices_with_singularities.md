# 2013 Abelian vortices with singularities

**Source:** `10_2013_Abelian_vortices_with_singularities.pdf`

---

arXiv:1207.0863v1 [math.DG] 4 Jul 2012                   ABELIAN VORTICES WITH SINGULARITIES

                                                                          J. M. BAPTISTA AND INDRANIL BISWAS

                                               Abstract. Let L - X be a complex line bundle over a compact connected Riemann
                                               surface. We consider the abelian vortex equations on L when the metric on the surface has
                                               finitely many point degeneracies or conical singularities and the line bundle has parabolic
                                               structure. These conditions appear naturally in the study of vortex configurations with
                                               constraints, or configurations invariant under the action of a finite group. We first
                                               show that the moduli space of singular vortex solutions is the same as in the regular
                                               case. Then we compute the total volume and total scalar curvature of the moduli space
                                               singular vortex solutions. These numbers differ from the case of regular vortices by a
                                               very natural term. Finally we exhibit explicit non-trivial vortex solutions over the thrice
                                               punctured hyperbolic sphere.

                                               1. Introduction

                                           Let X be a connected compact Riemann surface and L - X a complex line bundle
                                        of degree d. For a given Ka�hler metric X on the surface, the abelian vortex equations
                                        on L can be formulated in two equivalent ways [Br]. In the first formulation, one fixes a
                                        hermitian metric h on the line bundle and looks for a unitary connection A and a nonzero
                                        section  that satisfy

                                        (1.1)  �A = 0
                                        (1.2)  FA - ie2 ||h2 -  X = 0 ,

                                        where  and e2 are positive real constants. In the second formulation, one looks for a
                                        holomorphic structure on L, a nonzero holomorphic section  and a hermitian metric h
                                        on L such that

                                        (1.3)  Fh - ie2 ||2h -  X = 0 ,

                                        where Fh denotes the curvature of the corresponding Chern connection. So the condition
                                        in (1.1) follows from the holomorphicity of  in the second formulation, and the metric
                                        h becomes an independent variable in the second formulation; the Chern connection Ah
                                        coincides with the connection in the first formulation. In this article we will use the second
                                        point of view.

                                           The equations above are the original and simplest example of vortex equations. A lot is
                                        known about its solutions. One knows, for instance, that for any given stable pair (L, ),

                                        2000 Mathematics Subject Classification. 53C07, 14H81, 53D30.
                                        Key words and phrases. Vortex, parabolic pair, conical singularity, L2-metric, volume of moduli space.

                                                                                                               1
2      J. M. BAPTISTA AND I. BISWAS

meaning a holomorphic line bundle together with a nonzero holomorphic section, if the
volume of X is sufficiently large, more precisely,

(1.4)  Vol X    >  2   deg L ,
                   e2

then there is exactly one hermitian metric h on L that satisfies (1.3). This means that the
moduli space Mvdort of vortex solutions on a line bundle of degree d is isomorphic to space
of all isomorphism classes of stable pairs (L, ), which, in turn, is the space of degree d
effective divisors on X, or, equivalently, the symmetric product Symd(X). If condition

(1.4) is not satisfied, then there are no solutions of (1.3) for any stable pair.

   Replacing X with higher dimensional Ka�hler manifolds or replacing L with more general
bundles, the vortex equations and their moduli spaces of solutions can be generalized in
many different and useful ways (see, for instance, [BDGW, CGMS]). In this article we
will examine another generalization, distinct from the ones just cited. We will consider
the vortex equation (1.3) on Riemann surfaces with singular or degenerate metrics X,
and on holomorphic line bundles with parabolic structure.

   More precisely, we will consider Ka�hler metrics on X that are C and non-degenerate
on the complement X \ {q1 , � � � , ql} of a finite set of points, and satisfy the following
condition around each singular point qj: there is an open neighborhood Uj  X of qj
and a holomorphic coordinate z : Uj - C, with z(qj) = 0, such that the restriction of
X to Uj \ {qj} is of the form

(1.5)  X |Uj\{qj} = fj(z, z) � |z|2j � dz  dz ,

where j is a real number strictly bigger than -1 and fj is a C function on Uj with
fj(qj) = 0. The above restriction on the weights j guarantees that X has finite total
volume. If j is positive, the metric is continuous but degenerate at the point. When j
is negative the metric is said to have a conical singularity.

   Regarding parabolic singularities on the line bundle, we will consider hermitian metrics
h on L that are C and non-degenerate over the complement X \ {p1 , � � � , pr} of a finite
set of points, and satisfy the following condition around each point pi: for any holomorphic
coordinate function z around the singularity with z(pi) = 0, if s is a holomorphic section
of L defined on Ui with s(pi) = 0, then

(1.6)  s  2  =  gi(z, z) � |z|2i
          h

on Ui \ {pi}, where the weight i is a non-negative real number, gi is a continuous function
on Ui with gi(pi) = 0, and s h is the pointwise norm of the section s with respect to
the hermitian structure h. Choosing a holomorphic local trivialization of L, the Chern
connection Ah of this hermitian metric can be written on an open neighborhood Ui of the
parabolic singularity as

(1.7)  Ah |Ui\{pi} = i z-1dz + i ,
             ABELIAN VORTICES WITH SINGULARITIES       3

where i is a (1, 0)-form on Ui. Since the derivative � annihilates the first term, the
curvature Fh is more regular at the singularity. Using Stokes' theorem it can be shown
that, in the presence of parabolic points with sufficiently regular gis, i  [1 , r], the
curvature of the Chern connection has integral

         -1

(1.8)  2            Fh = deg L +     i =: par-deg L ,

             X \{pi }             i

and this number is usually called the parabolic degree of L. The parabolic singularities
on line bundles that we are considering here are a special instance of the much broader
and richer subject of parabolic structures on vector and principal bundles [MY], [BBN].

     One may wonder what is the motivation to study vortices with singularities. On the
one hand, this article may be regarded as part of an effort to study natural differential
objects on parabolic bundles and on punctured Riemann surfaces; an effort that so far
has been mostly centered on the Hermitian�Einstein equation, Higgs bundles and on
holomorphic curves. In the case of the singular vortex equations important results have
been obtained about the existence of solutions [BG] and, in a broader setting, about
topological properties of the moduli space [MT], but not yet about metric properties of the
moduli space. On the other hand, even if one cares only about smooth vortices, parabolic
bundles and singular metrics appear very naturally as an effective tool to describe vortices
that are invariant under a given symmetry or that are subject to constraints, as we now
explain.

   Suppose that a finite group  acts holomorphically, effectively and isometrically on a
surface Y , and that this action lifts to a holomorphic line bundle L over Y . Then 
also acts on sections, connections and hermitian metrics on L. This action takes vortex
solutions to vortex solutions and commutes with gauge transformations, so we get an
action of  on the moduli space Mvort of smooth vortices. The fixed point subvariety
M  Mvort corresponds to -invariant vortex configurations and, both from a physical
and a mathematical viewpoint, is a natural space to study. One can wonder, for instance,
about the geometry of M. It turns out that perhaps the most efficient way to study
-invariant vortices on Y is to look at usual vortices on the quotient surface X = Y /.
This surface can always be endowed with a complex structure such that the projection
 : Y - X is holomorphic. Crucially, however, the quotient metric on X may have
singularities. If a point p  Y has a non-trivial isotropy group p  , the quotient
metric at (p) will explode like |z|2(1-b)/b, where z is a complex coordinate around (p)
and the integer b is the cardinality of the subgroup p. So we are naturally led to study
vortices on surfaces equipped with singular metrics.

   A second motivational example is the following. Suppose that one wants to study
configurations of m smooth vortices on X with the constraint that at least l < m vortices
are located at a given point p  X. These configurations define a subvariety Ml.p 
Mvmort that is biholomorphic, but not isometric, to the smaller moduli space Mvmor-tl. This
4       J. M. BAPTISTA AND I. BISWAS

subvariety is the image of the holomorphic embedding Mvmor-tl - Mvmort defined by adding
l vortices at the location p, or, more formally, by the map

(1.9)   (L ,  , h) - L  OX (p)l , .(sp)l , h.(hp)l ,

where OX (p) is the holomorphic line bundle over X that has a section sp with a single
zero located at the point p, and hp is the singular hermitian metric on OX(p) determined
by |sp|2hp = 1. The inverse of the map in (1.9) allows us to identify vortex configurations
(L, , h) in the subvariety Ml.p with unconstrained configurations of (m - l) vortices �
a significant simplification. The price to pay for this simplification is that the resulting
unconstrained vortices will now be degenerate at the point p. In fact, since hp explodes
at p, the metric h = h.(hp)l will be an honest hermitian metric on L = L  OX (p)l
only if the metric h vanishes at p. In this case h must behave like |z|2l around p.
Thus constrained vortex configurations can be identified with unconstrained vortices with
degeneracies, and we are naturally led to study vortices on line bundles with degenerate
hermitian metrics.

   An outline of the article is the following. In Section 2 we prove the existence of vortex
solutions on parabolic line bundles over surfaces with degenerate or singular Ka�hler met-
rics. When these Ka�hler metrics are smooth, the existence of parabolic solutions to the
(coupled) vortex equations has been established by Biquard and Garc�ia-Prada [BG].

   In Sections 3 and 4 we study the natural L2-metric on the moduli space Mvort of vortex
solutions. Roughly speaking, if (t, ht) is a one-parameter family of vortex solutions, a
tangent vector to this path on the moduli space can be represented by the derivative 
of the section and the derivative Ah of the Chern connection. The metric on the moduli
space is then determined by the L2-norm

(1.10)  |Ah + |2 =      1   |Ah|2  +  | |h2  X
                       4e2
                    X

applied to the horizontal part of the tangent vector, i.e., to the component of (Ah, )
perpendicular to all vectors tangent to gauge transformations. We show that this metric
is well-defined in the case of vortices with singularities and, extending results already
established in the smooth case [MN, Pe, Ba], compute the total volume and the total
scalar curvature of the moduli space for this metric.

   In Section 5 we look at the vortex equations for abelian n-pairs, also called semilocal
vortices, in the presence of singularities. Once again we start by establishing the existence
of vortex solutions, then compute the total volume and scalar curvature of the L2-metric
on the moduli space and, finally, as in [Ba], use those computations to conjecture a formula
for the L2-volume of the space of holomorphic curves from X to projective space. Finally
in Section 6 we have a brief look at (singular) vortices on hyperbolic surfaces, extend an
observation of Manton and Rink [MR], and exhibit explicit and nontrivial vortex solutions
on the thrice punctured hyperbolic sphere.
                                  ABELIAN VORTICES WITH SINGULARITIES                                       5

   As a simple and concrete illustration of our results, namely those of Sections 2-4, take
the example of  = Zb acting on the sphere Y = CP1 by discrete rotations around the
vertical axis. Let MlmN ,lS  M m be the moduli space of -invariant m-vortex configurations
such that at least lN vortices are located at the north pole and lS vortices are located

at the south pole. Then these configurations are equivalent to configurations of m -
lN - lS vortices on the surface X = CP1/Zb  CP1 equipped with a Ka�hler metric X

with conical singularities at the poles of weight  = (1 - b)/b, and a hermitian metric

h with parabolic singularities of weight N = lN /b (respectively, S = lS/b) at the

north (respectively, south) pole. Our results for vortices with singularities then say that

Mm            Symm-lN -lS (CP1) and that, with respect to L2-metric inherited from the moduli
    lN ,lS
space Mvmort = Symm(CP1), the volume of the subvariety is

Vol MlmN ,lS      =      m-lN -lS             Vol Y  -   2   (lN  +  lS )      -  2   (m  -  lN  - lS)  m-lN -lS
                      (m - lN - lS)!  b                  e2                       e2
                                                                                                                  .

This coincides with the L2-volume of the moduli space of m-lN -lS regular vortices living
on a sphere CP1 of Riemannian volume b-1 (Vol Y - 2(lN + lS)/(e2 ) ). Heuristically,

this decrease in the effective volume of Y can be interpreted by saying that each vortex

fixed at the poles of CP1 occupies a volume equal to 2/(e2 ), and the remaining volume

of the sphere is divided by b due to the imposed Zb symmetry.

Beyond this simple example, the results of Sections 2-4 are applicable to more general

settings of higher genus surfaces, other groups , and also to metrics  and h whose

singularities and degeneracies cannot be obtained as quotients of regular metrics by actions

of finite groups.

                                  2. Existence of vortex solutions

Let X be a compact connected Riemann surface, and let  be a Ka�hler metric on X

with a finite number of singularities. Let L - X be a holomorphic line bundle equipped

with a nonzero holomorphic section  and parabolic weights {1 , � � � , r} at the parabolic

points {p1 , � � � , pr}. We assume that the parabolic weights satisfy i  0; in particular

we allow i  1. We assume that the singularities of  are represented by a formal sum

l      j    qj ,  in  the  sense  of  (1.5),  with  weights  j  > -1.      In  particular,   (X, )  has  a  finite
j=1

volume. In the case X = CP1 we make the additional assumption

       � The set {j  {1, . . . , l} : j < 0} has cardinality different from 1.

In this section we will show that there exists a hermitian metric h on L that satisfies

the vortex equation (1.3) and is compatible with the parabolic data in the sense of (1.5)

and (1.6). This extends the classic Hitchin-Kobayashi correspondence for abelian vortices

[Br, BG] to our singular setting. As usual, integrating the vortex equation (1.3) over X,

one recognizes that a necessary condition for existence of a solution is that

(2.1)                                 Vol X   >     2    deg L +           i ,
                                                     e2
                                                                     i
6                            J. M. BAPTISTA AND I. BISWAS

at least for solutions such that the Chern formula (2.2) given below remains valid. Theo-
rem 2.1 shows that, just as in the smooth case, once this inequality is satisfied then there
are no more obstacles to the existence of vortex solutions.

   For convenience in the statement of the theorem, we will consider the parabolic weights
{1 , � � � , r} as a function  on X defined as follows: (pi) = i for all i  {1 , � � � , r}
and (z) = 0 if z  {p1 , � � � , pr}. Similarly, we consider the weights of the singular
metric  as a function  on X defined as (qj) = j for all j  {1 , � � � , l} and (z) = 0
if z  {q1 , � � � , ql}.

Theorem 2.1. If condition (2.1) is satisfied there exists a unique smooth hermitian metric

h on L over X \ ({p1 , � � � , pr}  {q1 , � � � , ql}) that satisfies the vortex equation and has
the form h(z) = e2u|z|2(z0) on a neighborhood of each singular point z0. The function
u is of class Ck((z0),(z0)) at the singular point, where the integer k((z0), (z0))  0 is

defined in (2.3). For this solution of the vortex equation, the integral of the curvature of

the Chern connection is

(2.2)                                                                                     i .
                            Fh = -2 -1 deg L +

                         X                              i

Definition. For any two real numbers   0 and  > -1 we call

(2.3)  k(, ) := 2 + min (), ( + ) if   0
                            0                               if 0 >  > -1 ,

where () = + if  is an integer and is the integral part () = [] otherwise.

Remark. Observe that k(, ) =  precisely if  and  are integers. In this case the
function u and the curvature Fh are C at the singularity. If   0, then k( , )  2,
and so we can still guarantee that u is at least C2 and that Fh is at least continuous.
For negative , the curvature Fh has finite flux (it is integrable) but can explode at the
singularity � a fact that is apparent directly from the vortex equation.

Remark. Theorem 2.1 says that once the prescription of singularities is fixed, there is
a unique vortex solution for each choice of holomorphic structure on L together with a
nonzero holomorphic section . Since the latter choices are parametrized by the set of
effective divisors on the surface X, we conclude that, just as in the smooth case, the
moduli space Msd-vort of vortices with singularities is isomorphic to the symmetric product
Symd(X ).

The Yang-Mills-Higgs functional of a field configuration (A, ) is defined by the integral

                                       E(A, ) := E(A, ) X

                                                                                       X

of the standard energy density

       E(A, )            :=     1   |FA|2  +  |dA|2  +  e2                                ||2 -   2,
                               2e2                      2
       ABELIAN VORTICES WITH SINGULARITIES  7

where the norms are induced by the metric X on the surface and the hermitian metric
h on the line bundle. When the field configuration (Ah, ) is that of a vortex solution
with singularities, one can perform the integral over the punctured surface X \ {pi, qj} to
obtain:

Proposition 2.2. The vortex solutions of Theorem 2.1 have energy

                                 E(Ah, ) = 2 deg L + i .

                                                                                                           i

Thus, when singular fields are allowed, the energy of a vortex solution is no longer re-
stricted to be an integral multiple of 2 . A parabolic point where the hermitian metric
h degenerates (so the corresponding Chern connection Ah has a logarithmic singularity,
as in (1.7)) contributes to the total energy with an amount proportional to the parabolic
weight.

Proof of Theorem 2.1. The case where all j are nonnegative is treated in Lemma 2.3
below. We assume that some j is negative.

   Let nj be a positive integer such that j  (1 - nj)/nj and call j  [0 , +[ the
difference j - (1 - nj)/nj. From [Na, p. 29, Theorem 1.2.15] we know that there is a
finite (ramified) Galois covering

(2.4)  f : Y - X

such that each point in the inverse image f -1(qj) has ramification index nj - 1. Note
that to use [Na, Theorem 1.2.1], we need the assumption made earlier for X = CP1.
Then around each point of f -1(qj) the map f is like z - znj , and the pullback of 
behaves like f   |z|2jnj dz  dz�. Notice that by definition of nj we have jnj  0. In
particular, the Ka�hler form f  on Y satisfies the conditions of Lemma 2.3. So consider

the pullback bundle f L - Y equipped with the pullback section f s. The parabolic

weight at the point f -1(pi) is i if pi  {q1 , � � � , ql}, and it is nji if pi = qj. In other
words, the parabolic data on f L is the formal sum i(rf-1(pi) + 1) i f -1(pi), where rx
is the ramification index at x. Denoting by m the number of sheets of f , we have that

       2 par-deg (f L) -  e2 Volf Y = m 2 par-deg (L) -  e2 Vol X < 0 .

We can therefore apply Lemma 2.3 to obtain a hermitian metric h that satisfies the vortex
equation for (f L, f s) on the surface (Y, f ) and is compatible with the parabolic data.
This hermitian metric is continuous everywhere and is C away from the inverse images
f -1(pi) and f -1(qj).

   By uniqueness of vortex solutions on Y , the metric h must be invariant under the
action of the Galois group of the cover f , and in particular h descends to a continuous
hermitian metric h on the line bundle L - X. Since f is a local biholomorphism and
isometry away from the ramification points, h satisfies the vortex equation for (L, s, )
and all the statements of the theorem are true on the domain X \ {qj | j < 0}.
8            J. M. BAPTISTA AND I. BISWAS

   Now choose a point qj  X such that j < 0. As was seen above, at each point in
f -1(qj), the pull-back metric f  has a singularity with weight  = jnj. Since qj may
coincide with one of the parabolic points pi, we must also allow for a (possibly zero)
parabolic weight j at qj, so a parabolic weight  = njj at f -1(qj). Then Lemma 2.3
asserts that at each point in f -1(qj) the Gal(f )�invariant hermitian metric h is of the
form e2u|z|2, where u is also invariant and is Ck(,), with

              k(, ) = 2 + min (njj + nj - 1), (njj + njj + nj - 1) .

Since the cover map at the ramification point is like z - w = znj , the metric h downstairs
will be of the form e2u|w|2j , where u, being the quotient of u, is continuous at qj.

   The formula for the integral of the Chern curvature Fh follows from the integral of Fh
as given by Lemma 2.3:

          Fh = m-1 Fh = m-1 deg(f L) + m-1 deg              (rf-1(pi) + 1) i f -1(pi)

       X  Y                                               i

          = deg L + i ,

                                     i

where m is the degree of the covering f . Finally, uniqueness of the vortex solution on
(L, s, ) follows from the uniqueness on (f L, f s, f ).

Lemma 2.3. Theorem 2.1 is true when the weights j are non-negative.

Proof. Let h0 be a background hermitian metric on L representing the parabolic data
   i pi. Any other hermitian metric with the same parabolic data can be written as

h = e2uh0 for some real function u on X. Let 0 be a background Ka�hler metric on X
with no singularities or degeneracies and the same volume as . One can write  =  0,
where  is a positive function representing the divisor j qj in the sense of (1.5). As
originally observed by Bradlow in [Br], the vortex equation (1.3) for h is then equivalent

to

(2.5)                                   0u = Ke2u - K1 ,

where 0 is the positive-definite Laplacian of the metric 0 and the coefficients are

          K = -e2  |s|2h0               and  K1     =               - e2  .
                                                         -1 � 0Fh0

Here 0Fh0 denotes the contraction of the curvature Fh0 with the metric 0. The functions
K and K1 are clearly C away from the points {qj} and {pi}. At those points they are
continuous, since the weights j and j are non-negative. Moreover, these coefficient
functions satisfy

          (i) K  0 and is strictly negative on a non-empty domain,

          (ii) K1 0 = 2 deg L + i - e2  VolX < 0 .

          X                                      i
                              ABELIAN VORTICES WITH SINGULARITIES                                9

It then follows from the classical results of Kazdan and Warner (see in particular Corollary

10.13 and the proof leading to Theorem 10.5 in [KW]) that (2.5) has a unique solution
u  C2(X), and that this solution is C on the domain X \ {{qj}, {pi}}. Moreover,
if the functions K and K1 are Ck at a given point, then u will be C2+k at that point.
Thus formula (2.3) in the case   0 follows from the straightforward observation that

if  and  are the weights of  and h0, respectively, at a given singularity, then 0Fh0 is
C, while  is C() and  |s|2h0 is C(+) at the singularity. Finally, using that h0 is a
parabolic metric in the sense (1.6) with smooth coefficients gi, and that u is at least C2
on the whole X, we can apply Stokes' theorem to obtain

                    Fh =        Fh0 - �u =        Fh0 = -2i deg L + j ,

                           X  X                X                              j

completing the proof.

Proof of Proposition 2.2. We start by proving the result in the case where the metric

on the Riemann surface does not explode, meaning in the case where the weights satisfy

j  0. The standard Bogomolny argument for the Yang-Mills-Higgs functional [Br]

allows us to rewrite

E(A, ) =   1     FA - -1e2 ||2 -           X   2  +  2  �A   2    +           -          h � dA  .
          2e2                                                          -1 FA       -1 d

When the vortex equations are satisfied, the first two terms vanish. By Theorem 2.1, the

integral over X of the third term is 2 deg L + j j . So we only need to show that
the integral over X of the last term vanishes. In the smooth case this is standard and

obviously true, by Stokes' theorem. When the connection Ah has logarithmic singularities
at the parabolic points, we can still localize the surface integral to a sum of line integrals
over small circles CRj around the parabolic points,

                                 d h � dA =             lim       h � dA .
                                                         R0  CRj
                              X                   pj

To evaluate the circle integrals, around each parabolic point take the local holomorphic

trivialization of L defined by  = 1. Since Ah is the Chern connection in this trivial-
ization, we have Ah = h-1h, and so h � dA = (h�) = h. It follows that, in this

trivialization,

                                2     -1R            1                 -1R         2
                              0        2             2                  2
   h � dA =                                Rh     +      h   d =                     Rh d

CR                                                                               0

                                      2
                      = -1
                                          R2+1 e2u Ru +  R2 e2u d ;

                                   0

here we have used that near each parabolic point the hermitian metric can be written in
the form h(z) = e2u|z|2, with   0. But Theorem 2.1 says that when the weights j
are non-negative, the function u is at least of class C2, and in particular both e2u and
10           J. M. BAPTISTA AND I. BISWAS

Ru are continuous in a neighborhood of the parabolic point. Thus clearly

                lim                     h � dA = 0 ,
                R0 CR

completing the proof in the case j  0.

   The proof of the proposition in the general case j > -1 can be reduced to the case
proved above by the method employed in the proof of Theorem 2.1. Namely, we take the

Galois covering map f : Y - X as in that proof and consider the vortex equations
on the line bundle f L over the Riemann surface with hermitian structure (Y, f X)
equipped with the holomorphic section f . By construction all the singular points of
the metric f X have non-negative weights, so from the first part of the proof of the
proposition we know that all vortex solutions on (f L, Y, f X) have energy

             2 par-deg (f L) = 2 m par-deg (L) ,

where m is the number of sheets of the cover (the degree of f ). At the same time, from the
proof of Theorem 2.1 we know that the vortex solution for (f L, f , Y, f X) is invariant
under the action of the Galois group Gal(f ), that it descends to the vortex solution for
(L, , X, X), and that all the vortex solutions downstairs on X can be obtained in this
way. So for any vortex solution on X we have

             EX (A, ) = E (A, ) X = m-1 f  E (A, ) f X

             X                          Y

             = m-1 EY (f A, f ) = 2 par-deg (L) ,

as desired.

       3. Ka�hler metric on moduli space of singular abelian vortices

   In this section we will check that the L2 metric on the vortex moduli space is well
defined even when singularities are allowed, that is, when we allow the hermitian metric
on the line bundle to be degenerate at the parabolic points and the Ka�hler metric on the
surface X to have point degeneracies or conical singularities.

   Take a parabolic abelian pair y := (L , s)  Symd(X). The hermitian structure on L
given by Theorem 2.1 for the pair (L , s) will be denoted by hy. The Chern connection on
L over X := X \ {p1 , � � � , pr} for hy will be denoted by y. For any  > 0, define

             D := {t  C | |t| < } .

Take a holomorphic family of parabolic abelian pairs parametrized by D, where  is
sufficiently small, that deforms the given pair (L , s). This means that we have a holo-
morphic line bundle L over X � D, together with a holomorphic section S of L, such
that L|X�{0} = L and S|X�{0} = s. Let

(3.1)                v  TySymd(X)
                          ABELIAN VORTICES WITH SINGULARITIES                                          11

be the holomorphic tangent vector given by this family. For any t  D, let ht be the
hermitian structure on L|X�{t} given by Theorem 2.1 for the pair (L|X�{t} , S|X�{t}).

   The hermitian structures ht, t  D, together define a hermitian structure h on L|X�D.
Consider the Chern connection on L|X�D for this hermitian structure h. For any point
x  X, taking parallel translations of the fiber L(x,0) along the radial lines in the disk
{x} � D, we get an identification of L(x,0) with L(x,t) for each t  D. In this way, a C
isomorphism between the hermitian line bundles L|X�{t} and L|X�{0} is obtained.

   The Chern connection on L|X�{t} for ht will be denoted by t. So, 0 = y. Using
the above identification between L|X�{t} and L|X�{0}, we have

(3.2)                     t = y + t and S|X�{t} = s + t ,

where t is a smooth 1�form on X and t is a smooth section of L|X�{0} = L over X.

Then define the norm

(3.3)        v     2  :=  1       (  dt  (0))    (  dt   (0))  +         dt  (0)  2 � X ,
                          2          dt             dt                   dt
                               X                                   X

where t and t are constructed in (3.2), and v is the tangent vector in (3.1). To complete
the definition, we need to show that the integrals in (3.3) are finite. Note that both the
(1 , 1)�forms on X that are being integrated in (3.3) are positive.

Lemma  3.1.  Both  the    (1 , 1)�forms  (     dt  (0))    (   dt  (0))  and  dt  (0)  2 � X  over  X  in
                                               dt              dt             dt

(3.3) have a finite integral.

Proof. Take any parabolic abelian pair y := (L , s) over X. As before, let v  TySymd(X)
be the holomorphic tangent vector given by a holomorphic family of parabolic abelian pairs
(L , S) parametrized by D. Let t and t be as in (3.2).

   Consider the covering Y in (2.4). The abelian pair on Y corresponding to

                                         (L|X�{t} , S|X�{t})

will be denoted by (Lt , t). Let ht be the hermitian structure on Lt solving the vortex
equation for the pair (Lt , t) with respect to the Ka�hler form Y . Let t be the Chern

connection for ht. Write as before,

(3.4)                          t = 0 + t and t = 0 + t .

   Recall that the Ka�hler form Y on Y is the extension of the pullback (f X)|f-1(X),
where f is the covering map in (2.4). Also recall that the section t is the pullback of
S|X�{t}. The pullback, over f -1(X), of the hermitian structure ht on L|X�{t} extends to

a hermitian structure on Lt over Y , and this extension satisfies the vortex equation for
(Lt , t). Therefore, we conclude that

(3.5)                             t = f t and t = f t
12                         J. M. BAPTISTA AND I. BISWAS

over X, where t and t (respectively, t and t) are constructed in (3.4) (respectively,
(3.2)). From (3.5) we conclude that

(3.6)     1          (  dt  (0))     (  dt    (0))  +          dt  (0)  2 � Y
          2             dt              dt                     dt
                  Y                                      Y

       =      1   )  (  1     (  dt  (0))     (  dt  (0))   +         dt  (0)  2 � X ) .
          #Gal(f        2        dt              dt                   dt
                           X                                     X

The right�hand side of (3.6) is a finite number because the left�hand side of (3.6) is a
finite number. Since the right�hand side of (3.6) coincides with the right�hand side of
(3.3), the lemma follows.

       4. Ka�hler class, volume and total scalar curvature

   Let Z be a compact connected Riemann surface equipped with a smooth and non-
degenerate Ka�hler metric. The cohomology class of the Ka�hler form vort of the L2�metric
on the vortex moduli space M = Symd(Z) is explicitly known [MN, Pe, Ba]. It can be

written as a linear combination

(4.1)        [vort] =                  Vol(Z )    -   2   d        +    22  
                                                      e2                e2

of two natural cohomology classes  and  in H2(Symd(Z), R); their definitions are recalled
below. In this section we will see that when the vortices are defined on parabolic line
bundles, instead of regular line bundles, or when the metric on the Riemann surface has
conical singularities, the expression for the Ka�hler class is a suitable modification of (4.1).

Theorem 4.1. Let X be a compact Riemann surface equipped with a Ka�hler metric 

with a finite number of singularities, as in (1.5), and assume that the weights at these

singularities satisfy  > -1. Let L - X be a holomorphic line bundle equipped with
parabolic data i pi, where i  0. Then the Ka�hler class of the natural L2-metric on
the moduli space Symd(X) of d vortices on L - (X, ) is

                                              2             r                 22
                                              e2                              e2
(4.2)     [sd-vort] =            Vol  X    -      (d  +        i)       +           .

                                                          i=1

Thus the only difference with the nonsingular case considered in [Ba] is that the usual
degree is replaced by the parabolic degree. Equivalently, the volume of the surface
X is replaced by Vol X - i 2i/(e2 ). In particular, an intersection calculation on
H(Symd(X), R) similar to the one performed in [MN, Ba] for regular vortices gives the
total volume and the total scalar curvature of the moduli space of parabolic vortices.
                             ABELIAN VORTICES WITH SINGULARITIES                                   13

These numbers are the following:

Vol Msd-vort =  Symd (X )    sd-vort / d!

               min{g,d}            g!              (4)i    Vol X     -  2   r        -   2   d  d-i
                                                                        e2               e2
   = d                       i! (d - i)! (g - i)!                              j

                        i=0                                                 j=1

for the volume, and for the total scalar curvature is

         s(s-vort) sd-vort / d! =

Symd (X )

=             min{g,d}   g! d + 1 - 2g + i        (2)i     Vol X  -  2      r     -      d  d-1-i
                        i! (d - 1 - i)! (g - i)!        2            e2              e2
   (2)d                                                                        j

   i=0                                                                   j=1

Observe that these formulae reduce to the usual results for regular vortices when the

weights i of the parabolic singularities vanish.

Remark. One usually thinks of abelian vortices as finite-size objects, since the energy

density of the vortex solutions is concentrated on "effective disks" of area 2/(e2 ) cen-

tered around the zeros of the section . This physical image is supported by the term

Vol X - 2d/(e2 ) that appears in the Bradlow condition (1.4) and in the usual formulae

for the volume of the moduli space of d vortices. In the parabolic case, the corresponding

term is Vol X - 2(d + i i)/(e2 ), so we are lead to the heuristic interpretation that
each parabolic singularity occupies a disk on the surface X of effective area 2i/(e2 ).

To study the statistical-mechanical properties of a "gas" of vortices [MN], the relevant

quantity is the asymptotic behavior of Vol Mvdort(X) in the thermodynamical limit where

d   and Vol(X)   with constant density d/Vol X. When singularities are present,

everything works as in the regular case with the volume of X reduced by           r    2i/(e2      ).
                                                                                  i=1

Remark. The localization technique in topological field theory developed by Moore,
Nekrasov and Shatashvili in [MNS] has been recently applied to evaluate and predict
volumes of vortex moduli spaces [MOS]. It would be interesting to see if those techniques
can be used in the case of parabolic vortices and punctured Riemann surfaces.

   Before proving Theorem 4.1, we recall the definition of the cohomology classes  and
 lying in H2(Symd(X), R). The class denoted by  is the Poincar�e dual of the im-
age of Symd-1(X) in Symd(X) by the embedding that sends any {x1 , � � � , xd-1} to
{x0 , x1 , � � � , xd-1}, where x0  X is a fixed point (for convenience, we take Sym0(X)
to be a point); so the image of Symd-1(X) is the subvariety of Symd(X) parametrizing

all d�tuples that contain the fixed point x0. This integral cohomology class  is clearly
independent of the choice of the base point x0.

   To define the cohomology class , let Picd(X) be the component of the Picard group

of X parametrizing all isomorphism classes of holomorphic line bundles over X of degree
d. The variety Picd(X) is isomorphic to the Jacobian of X. The cohomology group
14                       J. M. BAPTISTA AND I. BISWAS

H2(Picd(X), R) is canonically identified with 2 H1(X, R). The anti�symmetric pairing
on H1(X, R) defined by

                                              ,  -   

                                                                                          X

defines a homomorphism H1(X, R) - H1(X, R) = H1(X, R). This homomorphism

is an isomorphism because the above pairing is nondegenerate. The inverse homomor-
phism H1(X, R) - H1(X, R) produces an element of 2 H1(X, R). Let

                                        Picd(X)  H2(Picd(X), R)

be the element corresponding to it by the above identification between 2 H1(X, R) and
H2(Picd(X), R). This element is usually called the theta class of Picd(X). Now let

(4.3)          X,d : Symd(X) - Picd(X)

be the morphism that sends any {x1 , � � � , xd} to the holomorphic line bundle OX (  d    xi).
                                                                                      i=1
For convenience, we define define X,0(Sym0(X)) to be the trivial line bundle OX . Then

by definition

(4.4)           := X ,d Picd(X)  H2(Symd(X), R) .

Theorem 4.1 will be proved by establishing a sequence of lemmas.

Lemma 4.2. Theorem 4.1 is true when the Ka�hler form  on X is smooth, i.e., when
the weights at the singularities are j = 0.

Proof. In this setting the only singularities present are the parabolic singularities of the

hermitian metric on the line bundle. Recall from [BG] and Section 2 that, as a complex
manifold, the moduli space Msd-vort vortices with parabolic singularities is isomorphic to
Symd(X) � the moduli space of the usual and regular vortices. Using exactly the argu-

ments as in [Pe, BS, Ba] for the case of regular vortices, one can construct a universal
line bundle L - Msd-vort � X for vortices with parabolic singularities. In fact, as a holo-
morphic bundle, L is the same whether the solutions we consider have parabolic points

or not. This universal bundle also comes equipped with a natural holomorphic section S

and a natural hermitian metric H with the property that, for any equivalence class of vor-
tex solutions q = [L, s, h]  Msd-vort, the restriction of (L, S, H) to the one-dimensional
complex submanifold {q} � X  X  Msd-vort � X coincides with (L, s, h). Since the
hermitian metric h has degeneracies at the parabolic points, so does H. As a function on
the product Msd-vort � X, we have that:

                         |S|H2 ([L, s, h], z) = |s|2h (z) .

Calculations similar the ones performed in [Pe, BS, Ba] show that the Ka�hler form of the

natural L2-metric on the moduli space Msd-vort satisfies

                            -1            1
(4.5)          s-vort =     2   FH    +  4e2              FH  FH ,

                         X
                          ABELIAN VORTICES WITH SINGULARITIES                           15

where FH stands for the curvature of the Chern connection on (L, H). In the parabolic
case, however, the metric H has degeneracies, so the Chern connection will not be smooth
everywhere. In particular, the curvature FH , even though continuous, does not necessarily
represent the Chern class of L.

Now let  be a fixed smooth and non-negative function on X that represents the real

divisor i pi. Then H0 := -1 � H is a hermitian metric on L with no degeneracies and

it is at least C2. So

(4.6)  [FH ]  =  [FH0 + � log()]   =            �  c1(L)  -  [�  log()]     H2(Msd-vort � X, R)
                                      -2 -1

as a cohomology class of the base Msd-vort � X. Since the function  does not depend on
the coordinates on the moduli space, the last term is proportional to the fundamental

class of X. The proportionality constant is

                   � log() =    j  lim       z� log() dz� =            
                                                                    2 -1 � j ,
                 X                 R0   DjR
                                                                 j

where we have used Stokes' theorem to express the surface integral as a sum of loop
integrals around the boundaries of small disks DjR of radius R centered at the singular
points pj  X. Then it follows from (4.5) and (4.6) that

              [s-vort] =        -  2 j j        c1(L)        -   2   c1(L)    c1(L)  .
                                   e2 Vol X                      e2
                          X

Thus the class [s-vort] is given by the same formula as the class [vort], except that one
should make the substitution

                                   -  -              2 j     .
                                                   e2 Vol X
                                             j

Comparing with (4.1), this proves the lemma.

Lemma 4.3. Formula (4.2) is still valid when the K�ahler form  on X has degeneracies
represented by a real divisor j jqj, with j  0.

Proof. Going through the arguments in [Ba], one can check that formula (4.5) for the
Ka�hler form on the moduli space Symd(X) still holds when  has point degeneracies.

Then the proof of the previous lemma can be applied without any modifications.

To complete the proof of Theorem 4.1, we will reduce the general case j > -1 to the case
j  0 treated above. This will be done using the method used in the proof of Theorem
2.1.

   Let f : Y - X be the m-sheeted Galois cover described in the proof of Theorem 2.1.
The pull-back operation h - f h defines a one-to-one correspondence between vortex
solutions on (L, s, ) with parabolic data i ipi and Gal(f )�invariant vortex solutions on
(f L, f s, f ) with parabolic data i(rf-1(pi) +1) i f -1(pi), where rx is the ramification
16     J. M. BAPTISTA AND I. BISWAS

index of f at the point x. This correspondence induces the holomorphic embedding of
moduli spaces

(4.7)  f : Symd(X) - Symm.d(Y )

                                       d        d

                                          xj - f -1(xj)

       j=1                                      j=1

where f -1(xj) is the inverse image counted with multiplicities. The image of f is the
subvariety of Galois-invariant solutions inside the whole moduli space of solutions.

Lemma 4.4. Suppose that the metric on the surface X has singularities with negative

weight  > -1. Then the K�ahler form of the L2 metric sd-vort on the moduli space
Symd(X) is well-defined and satisfies the identity

(4.8)  sd-vort(X )                        =  1  f  sm-v.dort(Y ) ,
                                             m

where f is the map in (4.7) and sm-v.dort(Y ) is the Ka�hler form of the L2-metric on the
moduli space of m.d vortices on the surface Y equipped with the metric f .

   This lemma will be proved below. Its importance relies on the fact that the singularities
of the Ka�hler form f  on the cover Y all have non-negative weight, as observed in the

proof of Theorem 2.1. So Lemma 4.3 is applicable, and using the parabolic weights at the
inverse images f -1(pi) specified in the proof of Theorem 2.1, we obtain that

                  [sm-vdort(Y )] =   Vol Y - 4 m d + i  + 42  ,

                                                                                                         i

where the classes  and  in H2(Symmd(Y ), R) are defined in the same way as  ,  
H2(Symd(X), R) were defined above. Since the metric on Y is the pullback of the metric

on X, the total volumes are related by Vol Y = m Vol X = #Gal(f ) � Vol X. So in view of
(4.8) to calculate the cohomology class [sd-vort(X)] we only need to compute the pullback
classes f  and f .

   For the first one, take a point y  Y such that f is unramified at y. Take x :=
f (y)  X. Let Hx  Symd(X) (respectively, Hy  Symm.d(Y )) be the hypersurface
defined by the image of Symd-1(X) (respectively, Symmd-1(Y )) under the embedding

(x1 , � � � , xd-1) - (x , x1 , � � � , xd-1) (respectively, (y1 , � � � , ymd-1) - (y , y1 , � � � , ymd-1)).
So Hx and Hy represent the cohomology classes  and  respectively. We have

       Hy f (Symd(X)) = Hx .

From this it follows immediately that

(4.9)                                     f =  .

Thus Theorem 4.1 is a consequence of Lemma 4.5 below.

Lemma 4.5. The pullback f   H2(Symd(X), R) coincides with m � .
            ABELIAN VORTICES WITH SINGULARITIES                                17

Proof. Let

            f : Picd(X) - Picm�d(Y )

be the morphism defined by  - f . The following diagram is evidently commutative:

             Symdf(X )          -X,d      Picd (fX )
            Symm�d(Y )          - Y,m�d  Picm�d(Y )

where Y,m�d is constructed just as X,d is constructed in (4.3). Therefore, to prove the
lemma, it suffices to show that

(4.10)         f Picm�d(Y ) = m � Picd(X) .

For any  ,   H1(X, R), we have

(4.11)         (f )  (f ) = m    .

            Y                            X

As noted before, suing the cup product on H1(X, R) (respectively, H1(Y, R)), the ho-

mology H1(X, R) (respectively, H1(Y, R)) gets identified with H1(X, R) (respectively,
H1(Y, R)). From (4.11) it follows that the composition

            H1(X, R) -f H1(Y, R) = H1(Y, R) -f H1(X, R) = H1(X, R)

coincides with multiplication by m. From this the equality in (4.10) follows.

Proof of Lemma 4.4. Fix the pulled back Ka�hler form Y on Y . Take any positive
integer m. Let

                                             Mvmort = Symm(Y )

be the moduli space of abelian pairs on Y of degree m. This moduli space Symm(Y )
is equipped with a Ka�hler form vmort(Y ) constructed using Y ; see [Mu], [BS, p. 840,
Definition 6.1], [Ba, p. 309, (4)]. Below, we will briefly recall the construction of vmort(Y ).

   Take an abelian pair y := (L , )  Symm(Y ). The hermitian structure on L that

satisfies the vortex equation for y with respect to Y will be denoted by hy. The Chern
connection on L for hy will be denoted by y. Let

(4.12)         v  TySymm(Y )

be the holomorphic tangent vector given by a holomorphic family of abelian pairs (Lt , t),
t  D, with (L0 , 0) = (L , ). Let ht be the hermitian structure on Lt that satisfies
the vortex equation for (Lt , t) with respect to Y . Let  be the Chern connection on
L for the family (Lt , ht) of holomorphic hermitian line bundles. For any y  Y , taking
parallel translations, with respect to , along the radii of the disk {y} � D, we get a C
trivialization of the family of hermitian line bundles Lt. The Chern connection on Lt for
ht will be denoted by t. Using the above C trivialization of the family of holomorphic
line bundles Lt, we have t = y + t and t =  + t, where t is a 1�form on Y and
18                                  J. M. BAPTISTA AND I. BISWAS

t is a smooth section of L0 = L. The Ka�hler form vmort(Y ) on Symm(Y ) is given by the

formula                   1            dt             dt                d
                          2            dt             dt                dt
         v         2  :=            (      (0))    (      (0))  +           (0)  2 � Y  ,

                                 Y                                   Y

where v is the tangent vector in (4.12). The lemma follows from this description of Ka�hler

form on Symm(Y ).

                                       5. Abelian n-pairs

5.1. Existence of solutions and volume of the moduli space. In this section we will

consider the vortex equations for abelian n-pairs. These are sometimes called semilocal

vortices. An abelian n-pair is a holomorphic line bundle L - X together with n

holomorphic sections 1, . . . , n, and we will assume that at least one of these sections is

nonzero. The vortex equation for a hermitian metric h on L is then

(5.1)              Fh - -1e2 |1|h2 + � � � + |n|h2 -  X = 0 .

Just as in the n = 1 case treated before, if the line bundle L is equipped with parabolic
data we can consider the vortex equations with parabolic singularities. This means that
we require h to behave asymptotically like (1.6) at each singular point pi  X. We also
allow finitely many degeneracies or conical singularities of the metric X on the surface,
so that it behaves like (1.5) around each singular point qj  X.

Proposition 5.1. Theorem 2.1 is valid for the vortex equation (5.1) with singularities.

Proof. The proof of Theorem 2.1 applies unchanged.

   Now call Msd-,vnort the moduli space of n-vortices with singularities. Just as for n = 1, it
follows from the proposition above that Msd-,vnort is isomorphic the space of abelian n-pairs
on L - X and that, as a complex manifold, it does not depend on the prescription

of singularities. Thus it is the same as in the case of smooth n-vortices. In particular,

for degree d > 2gX - 2, the manifold Msd-,vnort is a projective bundle over the Jacobian
Picd(X) with fiber CPn(d+1-g)-1. The natural L2-metric on the moduli space, however,

does depend on the existence of singularities. In [Ba] it was shown that in the smooth

case the Ka�hler class of the L2-metric is

                      [vdo,nrt]     =        Vol   X  -   2   d      +  22       ,
                                                          e2            e2

where  is the generator of the cohomology of the projective fiber and  is the pull-back to
Mvdo,nrt of the theta class in Picd(X). (In the n = 1 case, these classes  and  coincide with

the classes with the same name used earlier.) For semilocal vortices with singularities the

analogous result is the following:

Proposition 5.2. Assume that the degree of the line bundle satisfies  e2 (Vol X)/(2) -
   i i > d > 2gX - 2. Then the Ka�hler class of the natural L2-metric on the moduli space
                          ABELIAN VORTICES WITH SINGULARITIES                                        19

Msd-,vnort of singular vortices is      Vol  X  -  2             r    +     22    .
                      [sd-,vnort] =                e2                       e2
                                                       d + i

                                                               i=1

Proof. Consider the natural projection 0 : Msd-,vnort - Picd(X) that takes the class
of a n-pair (L, 1, . . . , n) to the class of the line bundle L in the Picard group. Since
d > 2gX - 2 this projection defines a projective bundle, and we can write the Ka�hler class
of the L2 metric on the moduli space as

                                          [sd-,vnort] =   + 0  ,

where  is a scalar and  is a cohomology 2-class on the base Picd(X). Now let

                                             : Msd-,v1ort - Msd-,vnort

be the isometric embedding that takes (L, h, ) to (L, h, , 0, � � � , 0). The image of  is a
sub-bundle of Msd-,vnort - Picd(X) with fiber CPd-g, so clearly  =  and 0 = 1,
where 1 is the restriction of 0 to the sub-bundle. In other words,

                                 [sd-,v1ort] = [sd-,vnort] =   + 1  .

Comparing with (4.2) we conclude that  and  are as stated in the proposition. This
completes the proof.

   Since the Ka�hler class is known and Msd-,vnort is a projective bundle, the intersection
calculations to compute the volume and total scalar curvature are quite simple [Ba]. For

example we have

                    g           g! ng-i                2 i                  2           2      l-i
                          i! (l - i)! (g - i)!         e2                   e2          e2
Vol Msd-,vnort = l                                           Vol X -              i  -      d     ,

                    i=0                                                  i

where l = g + n(d + 1 - g) - 1. Both the volume and the total scalar curvature of

the moduli space of vortices with singularities can be obtained from the corresponding

values for the moduli space of vortices without singularities by the usual substitution

Vol X - Vol X -        i  2     i  .
                          e2

5.2. Volume of spaces of holomorphic curves. For d  2g the manifold Msd-,vnort can
be regarded as a compactification of the space Hd,n-1 of holomorphic maps X - CPn-1

of degree d (see [BDW, Ba]). A heuristic argument similar to the one given in the last

reference for regular vortices suggests that the pointwise limit as e2   of the form
sd-,vnort over the domain Hd,n-1  Msd-,vnort coincides with the Ka�hler form md,anp-1 of the
natural L2-metric on the space of maps (X, X) - (CPn-1,  � FS), where FS is

the normalized Fubini-Study form (its cohomology class is the generator of the integral

cohomology). Then the limit

 lim  Vol           Msd-,vnort  =                  ng                Vol X n(d+1-g)+g-1

e2                                    n(d + 1 - g) + g - 1 !
20                              J. M. BAPTISTA AND I. BISWAS

should presumably be interpreted as the volume of the non-compact Riemannian manifold

                                              (Hd,n-1, md,anp-1) .

Notice that the weights i disappear in this limit, and the result depends on X only
through the volume Vol X. This suggests that the conjectural formulae in [Ba] for the
volume and total scalar curvature of Hd,n-1 should hold unchanged when X has isolated
singularities of the form (1.5).

                         6. Vortices on hyperbolic surfaces

    Let f : Y - X be a holomorphic map between two connected Riemann surfaces.

The derivative df is a section of the holomorphic line bundle L := T Y  f T X. This

bundle has a natural hermitian metric h induced by the Riemannian metrics on the

surfaces. The curvature form of this hermitian metric is

(6.1)             Fh  =  -FY    + f FX     =    -1(KY  - |df |2 KX ) volY

as a 2-form over Y , where KX and KY are the scalar curvatures of the surfaces. So if
we take X and Y to be hyperbolic surfaces, i.e. if we take the scalar curvatures to be
negative and constant, we see that (L, df, h) satisfies the abelian vortex equations over
Y . This curious fact was first observed by Witten [Wi] in the case where X and Y are the
hyperbolic plane; an observation that allowed him to explicitly construct all the vortex
solutions on H2. Recently, after phrasing the observation in a more geometric language,
Manton and Rink [MR] have used it to study vortices on many other hyperbolic surfaces.
An extension of this result is the following.

Proposition 6.1. Let f : Y - X be a holomorphic map between hyperbolic surfaces
of scalar curvature KY = KX = - /2. If (L , h) - X is a hermitian line bundle with
a section  that satisfies the vortex equations over X, then the triple (L , h , ), where

    (1) L := T Y  f T X  f L
    (2) h := gY � f gX � f h
    (3)  := df  f  ,

satisfies the vortex equations over Y .

Remark. This means that for hyperbolic surfaces there is a natural way of obtaining

vortex solutions  by pull-back  of  other solutions. The  o=bserv.atOiobnseorvf e[Wthia] tanthde[MsecRt]iocnor-
responds to the   case where L  is  trivial, h = 1 and 

vanishes exactly at the ramification points of f plus the inverse image of the zeroes of .

Proof. Using the vortex equation on X, the curvature of (L, h) is

Fh     =  -FY  + f (FX + Fh)    =                  -            -     1  |f  |2h  +  1    )  f volX
                                       -1 KY volY        -1(KX        2              2

          -1                                  -1
       =  2    (-  +  |df |2|f |2h)  volY  =  2    ||2h -     volY .
                      ABELIAN VORTICES WITH SINGULARITIES                  21

So the vortex equation on Y is satisfied.

Remark. A similar calculation shows that the result also holds when L is a vector
bundle over X. In this case, if (L , h , ) satisfies the non-abelian vortex equations, so
will (L , h , ). A version of it holds for the coupled vortex equations as well.

When the surfaces X and Y are compact the utility of Proposition 6.1 as tool to obtain

smooth vortex solutions on Y is limited, as pointed out in [MR]. This is because smooth

hyperbolic metrics only exist for surfaces with genus 2 or more, by Gauss-Bonnet, and in

this case the few holomorphic maps f : Y - X that exist are isolated, i.e. do not have
moduli. But notice that Proposition 6.1 is equally valid when the metrics gX , gY and h
have point singularities. In this case, of course, h will in general be singular as well. It

follows from the definition of h that if gY has a conical singularity of order Y at a point
z = z0 and the metrics gX and h have a singularities of order X and , respectively, at
f (z0), then the metric h on L has a parabolic point of weight  = X - Y +  at the
point z0. So if are willing to consider vortex solutions with singularities, Proposition 6.1
allows us to construct much bigger families of solutions. For example punctured Riemann
spheres and punctured tori admit hyperbolic metrics, and moreover any meromorphic
function on Y defines a holomorphic map Y - CP1.

   As for explicit vortex solutions, a large family of them can be obtained if we take the
surfaces X and Y to be the thrice punctured Riemann sphere and the map f to be any
rational map CP1 - CP1. In this case the unique hyperbolic metric on CP1 \ {0, 1, }
with singularities of order

(6.2) - 1 < 0 < 0 , -1 < 1 < 0 , -1 <  < 0 , 0 + 1 +  < -2

has been written down explicitly in recent work of Kraus, Roth and Sugawa [KRS]. Since

rational maps on the sphere are also explicit, we can write very non-trivial singular vortex

solutions on the punctured sphere. Although perfectly valid, most of these solutions will

not fall within the class that has been studied in this article, because they will have points

with negative parabolic weight  = X - Y + . In other words, the hermitian metric
h may explode at points in the inverse image f -1({0, 1, }). Nevertheless, we can still

write a simple example where this explicit construction gives a continuous and non-trivial

vortex  solution  h.  Ju;stantadkechfootsoe  be the identity  map; L   to  be the trivial bundle with
h = 1   and       =                          the hyperbolic   metrics  gY  and gX on the punctured

sphere CP1 \ {0, 1, } with negative weights at the three singularities satisfying (6.2) and

                   (Y )0  (X )0 , (Y )1  (X )1 , (Y )  (X ) .


Then L is the trivial bundle, the section  is constant and equal to  , and the hermitian
metric

(6.3)                 h = gX, X / gY, Y

is a non-trivial vortex solution on L - (Y, gY ) with parabolic weight (X )p - (Y )p at
each of the three singular points p = 0, 1, . Using the formulae of the Appendix, this
22                       J. M. BAPTISTA AND I. BISWAS

vortex solution h can be written down in terms of hypergeometric functions on C \ {0, 1}.
The relation between vortex solutions and hyperbolic metrics illustrated in this example
will be clarified in future work.

Acknowledgements. The second author wishes to thank Instituto Superior T�ecnico,
where a large part of the work was carried out, for its hospitality. The visit to IST was
funded by the FCT project PTDC/MAT/099275/2008. The first author thanks CAMGSD
and Project PTDC/MAT/119689/2010 of FCT - POPH/FSE for a generous fellowship.

                                         Appendix

   For the sake of completeness we will reproduce here, using our notation, the explicit
hyperbolic metrics on CP1 \ {0, 1, } of curvature -1 found by Kraus, Roth and Sugawa
[KRS]. By (6.3) they determine explicit and non-trivial vortex solutions. Identify the
thrice punctured sphere with the punctured plane C \ {0, 1} and choose weights on the
singularities satisfying -1 < 0, 1 ,  < 0 and 0 + 1 +  < -2. Define the constants

       := -(0 + 1 - )/2 ,  := -(0 + 1 +  - 2)/2 ,  := -0 .

Then 0 <    and  +  <  < 1. Consider the hypergeometric functions on the plane

             1(z) := F (, , ; z) , 2(z) := F (, ,  +  -  + 1; 1 - z) ,

so that 1 is analytic on C\[1, +) and 2 is analytic on C\(-, 0]. Then the hyperbolic
metric on the thrice punctured sphere with the chosen weights is given by

                         g = g0,1,(z) dz  dz� ,

where the coefficient function is

           g0,1, (z)  =  K1 |1(z)|2      +  2 |z|0 |1 - z|1 K3                ,
                                            K2 |2(z)|2 + 2 Re(1(z) 2(z�))

and the remaining constants are defined by

       K1  :=  -  ( - )  (         -  )     K2  :=  -  (   +  1 - )  (  +  1  -  )  ,
                  () (   -         -  )                (1  -  ) (    +  +  1  -  )

       K3 :=             sin() sin()            �   ( +  + 1 - ) ()        .
                  sin(( - )) sin(( - ))                    () ()

                                         References

[BBN]  V. Balaji, I. Biswas, and D. S. Nagaraj: Principal bundles over projective manifolds with
       parabolic structure over a divisor, Tohoku Math. Jour. 53 (2001), 337�367.
[Ba]   J. M. Baptista: On the L2-metric of vortex moduli spaces, Nucl. Phys. B 844 (2011), 308�333.
[BDW]  A. Bertram, G. Daskalopoulos and R. Wentworth: Gromov invariants for holomorphic maps
       from Riemann surfaces to grassmannians, Jour. Amer. Math. Soc. 9 (1996), 529�571.
[BG]   O. Biquard and O. Garc�ia-Prada: Parabolic vortex equations and instantons of infinite energy,
       Jour. Geom. Phys. 21 (1997), 238�254.
[BS]   I. Biswas and G. Schumacher: Coupled vortex equations and moduli: Deformation theoretic
       approach and Ka�hler geometry, Math. Ann. 343 (2009), 825�851.
ABELIAN VORTICES WITH SINGULARITIES  23

[Br] S. Bradlow: Vortices in holomorphic line bundles over closed K�ahler manifolds, Comm. Math.
            Phys. 135 (1990), 1�17.

[BDGW] S. Bradlow, G. Daskalopoulos, O. Garc�ia-Prada and R. Wentworth: Stable augmented bundles
            over Riemann surfaces, Vector bundles in algebraic geometry (Durham, 1993), 1567, London
            Math. Soc. Lecture Note Ser., 208, Cambridge Univ. Press, Cambridge, 1995.

[CGMS] K. Cieliebak, R. Gaio, I. Mundet i Riera and D. Salamon: The symplectic vortex equations and
            invariants of Hamiltonian group actions, J. Symplectic Geom. 1 (2002), 543�645.

[KW] J. Kazdan and F. Warner: Curvature Functions for Compact 2-Manifolds, Ann. Math. 99
            (1974), 14�47.

[KRS] D. Kraus, O. Roth and T. Sugawa: Metrics with conical singularities on the sphere and sharp
            extensions of the theorems of Landau and Schottky, Math. Zeit. 267 (2009), 1�19.

[MN] N. Manton and S. Nasir: Volume of vortex moduli spaces, Comm. Math. Phys. 199 (1999),
            591�604.

[MR] N. Manton and N. Rink: Vortices on hyperbolic surfaces, Jour. Phys. A 43 (2010), 434024.
[MY] M. Maruyama and K. Yokogawa: Moduli of parabolic stable sheaves, Math. Ann. 293 (1992),

            77�99.
[MS] V. B. Mehta and C. S. Seshadri: Moduli of vector bundles on curves with parabolic structures,

            Math. Ann. 248 (1980), 205�239.
[MOS] A. Miyake, K. Ohta and N. Sakai: Volume of moduli space of vortex equations and localization,

            Prog. Theor. Phys. 126 (2011), 637�680.
[MNS] G. Moore, N. Nekrasov and S. Shatashvili: Integrating over Higgs branches, Comm. Math. Phys.

            209 (2000), 97�121.
[Mu] I. Mundet i Riera: A Hitchin-Kobayashi correspondence for K�ahler fibrations, Jour. Reine

            Angew. Math. 528 (2000), 41�80.
[MT] I. Mundet i Riera and G. Tian: A compactification of the moduli space of twisted holomorphic

            maps, Adv. Math. 222 (2009), 1117�1196.
[Na] M. Namba: Branched coverings and algebraic functions, Research Notes in Mathematics 161,

            Pitman-Longman, John Wiley & Sons Inc., New York, 1987.
[Pe] T. Perutz: Symplectic fibrations and the abelian vortex equations, Comm. Math. Phys. 278

            (2008), 289�306.
[Wi] E. Witten: Some exact multipseudoparticle solutions of classical Yang-Mills theory, Phys. Rev.

            Lett. 38 (1977), 121�124.

   Centre for Mathematical Analysis, Geometry, and Dynamical Systems (CAMGSD),
Instituto Superior Te�cnico, Av. Rovisco Pais, 1049-001 Lisbon, Portugal

   E-mail address: [email redacted]

   School of Mathematics, Tata Institute of Fundamental Research, Homi Bhabha Road,
Bombay 400005, India

   E-mail address: [email redacted]
