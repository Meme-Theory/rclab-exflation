# Holographic Principle Finiteness 2024

**Source:** `23_Holographic_Principle_Finiteness_2024.pdf`

---

arXiv:2407.14551v1 [physics.gen-ph] 17 Jul 2024   The holographic principle comes from finiteness of the universe's
                                                                                    geometry

                                                                                                  Arkady Bolotin
                                                                        Ben-Gurion University of the Negev, Beersheba (Israel)

                                                                                                   July 23, 2024

                                                                                                                 Abstract
                                                         Discovered as an apparent pattern, a universal relation between geometry and information
                                                         called the holographic principle has yet to be explained. This relation is unfolded in the present
                                                         paper. As it is demonstrated there, the origin of the holographic principle lies in the fact that
                                                         a geometry of physical space has only a finite number of points. Furthermore, it is shown that
                                                         the puzzlement of the holographic principle can be explained by a magnification of grid cells
                                                         used to discretize geometrical magnitudes such as areas and volumes into sets of points. To wit,
                                                         when grid cells of the Planck scale are projected from the surface of the observable universe into
                                                         its interior, they become enlarged. For that reason, the space inside the observable universe is
                                                         described by the set of points whose cardinality is equal to the number of points that constitute
                                                         the universe's surface.

                                                         Keywords: holographic principle; finite geometry; entropy; black hole; holographic image;
                                                         magnification.

                                                 1 Introduction

                                                 The holographic principle has arisen in physics as an universal relation between geometry and
                                                 information both uncontradicted and unexplained by existing theories. The basis of this relation is
                                                 that a spatial volume V with a boundary of area A is fully described by no more than A/42P bits
                                                 of information, i.e., 1 bit per each 4 Planck areas P2 (where P is the Planck scale approximately
                                                 equal to 1.6 � 10-35 m) [1, 2, 3].

                                                 The discovered relation is not trivial. To be sure, discretizing a flat 3-space into an array of primitive
                                                 cubes of edge length P and assuming that there is a quantum harmonic oscillator in each Planck
                                                 cube, one can envision a region of volume V in this space as a lattice of V /P3 oscillators. The
                                                 lattice has N V/P3 states, where N is the number of states of each oscillator. Provided N  2 and V
                                                 is finite, one would expect the number of degrees of freedom contained in the region to grow with V
                                                 in the way that V /3P � log N . But, as it has been proven to hold in a wide range of examples [4], the

                                                     Email : [email redacted]

                                                                                                                 1
said number is not exceeding the value A/4P2 � log N , where A is the area of the boundary to the
region. This is deeply puzzling. For example, let V be the volume of a cube with the edge length
a  P . Then, in accordance with the discovered relation, one would have a3/3P < 3a2/2P2 , i.e.,
a contradiction: a < 3P /2.

The universality of the aforementioned relation suggests that it is an imprint of some general law in
science. Usually, this law is considered to be due to string theory [5]. Particularly, it was observed
that string theory admits a lower-dimensional description in which gravity emerges from it [6]. This
observation was the starting point for AdS/CFT correspondence asserting that the boundary of
anti-de Sitter space (AdS for short), which is used in string-based theories of quantum gravity, can
be regarded as the "spacetime" for a conformal field theory (abbreviated as CFT), which is used
to describe elementary particles [7].

As influential as AdS/CFT has proven to be, there is growing skepticism about whether it is ad-
equate to faithfully represent real-world systems. Suffice it to say that the spacetime on which
string-based gravitational theories live has more than 4 dimensions. In that light, AdS/CFT cor-
respondence (or at least the most famous version of it) does not provide a realistic description of
gravity. As to the versions of AdS/CFT that may offer a (slightly more) realistic description of
gravity, they all imply models of spacetime that are characterized by supersymmetry having no
place in our universe [8].

In contrast, the present paper will demonstrate that the relation between geometry and information
is due to finiteness of geometry that describes physical space.

2 Physical space has a finite geometry

There are reasonable grounds to believe that space contains a finite number of points, the corollary
being that a geometry of physical space is finite [9]. Let us review those grounds.

In axiomatic set theories, it is imposed that axioms for logic and mathematics must be formulated
only on pure or hereditary sets, i.e., ones endowed with no features at all. Contrastively, a vector
space � a set with linear operations defined upon it � is not pure: It contains urelements, i.e., objects
(vectors) that are not sets but may be elements of sets [10]. So, in accordance with the aforesaid
imposition, axioms that are new to or different from ZF, the set of the axioms of Zermelo�Fraenkel
set theory, cannot be acquired by interchanging "sets" with "vector spaces" in ZF.

But on the other hand, there are no mathematical grounds for preferring pure sets to sets containing
urelements [11]. What is even more crucial, the metamathematical imposition of pure sets brings
about one of the most serious problems in modern physics, viz., the emergence of infinities in
well-formed formulas of the classical and quantum formalisms.

Thus, it makes sense to present Hilbert space theory, fundamental to quantum mechanics, in the
form of the axiomatic set theory STHil wherein "sets" are replaced with "vector spaces". As it
turned out, all but two axioms of ZF � the axiom of empty set denoted Empty and the axiom of
infinity denoted Inf � can be translated into the formal language of Hilbert space theory in this
manner.

                                                                2
The cause for the exclusion of the axiom Empty is the fact that a set of vectors must include at
least the zero vector 0 to be a vector space. Therefore, the notion of empty set is not translatable
into the notion of empty vector space. Furthermore, unlike the original axiom Inf stating that the
cardinality of a set capable of including some set X together with all successors of X is infinite, the
translation of Inf into the language of Hilbert space theory asserts that the cardinality of a vector
space capable of including some vector space X plus all successors of X can be finite, in particular
1. Indeed, any vector space must have at least one element, namely, the zero vector space {0}.
Since each successor of {0} is {0}+ := {0}  {{0}} = {0}  {0} = {0}, i.e., the zero vector space
again, it implies that the vector space {0} including all the successors of itself is the same {0}.
With all that, the cardinality of {0} is obviously 1.

In this way, STHil can be considered to be the set of axioms ZF wherein the axioms Empty and Inf
have been replaced with their negations, �Empty and �Inf. In symbols,

STHil = ZFfin := ZFbase  {�Empty, �Inf} ,             (1)

where ZFbase denotes the "basic" set theory, namely,

ZFbase := ZF \ {Empty, Inf} .                         (2)

While on the subject, let us note down that an -model of ZFfin is a model in which every set has
at most finitely many elements (as viewed externally).

Consequently, the formal language of quantum mechanics, L(QM), which has the axioms of Hilbert
space theory at its core [12], can be expressed by the formal language of the finite set theory ZFfin in
conjunction with Xqsystem, the set of axioms of quantum mechanics that are absent in a set theory.
This can be displayed by the following bijection:

f: L(QM)  L ZFfin  Xqsystem .                         (3)

Consistent with the above mapping, the formal language of classical mechanics, L(CM), must be
expressed by the bijection

f: L(CM)  L ZFfin  Xsystem ,                          (4)

meaning that everything which can be expressed through L(CM) can also be expressed through the
collection of axioms of the finite set theory ZFfin in conjunction with Xsystem, the set of axioms
(non-existent in a set theory) determined by a classical mechanical system being a subject of study
(the set Xsystem is a proper subset of Xqsystem, i.e., Xsystem Xqsystem, otherwise classical mechanics
cannot be reducible to quantum mechanics).

In line with the reductionist approach [13], the transition from a classical field to a quantum
operator field should be analogous to the promotion of a classical harmonic oscillator to a quantum

                                                                3
harmonic oscillator. Accordingly, for each field theory FT and its quantum counterpart QFT, the
following bijections must hold

f: L(FT)  L (ZFfin  Xfield) ,                                                                     (5)

f: L(QFT)  L ZFfin  Xqfield ,                                                                     (6)

where Xfield and Xqfield denote the sets of axioms that are not present in a set theory, to be specific,
Xfield comprises axioms that depend on a classical filed being studied and Xqfield is the proper
superset of Xfield, i.e., Xqfield Xfield.

On condition that any FT and QFT are decidable, every well-formed formula in the formal languages
L(FT) and L(QFT) must be consistent with the axiom �Inf. This implies that calculations made
with FT and QFT are expected to be free from the infinite elements + and -.

To check this, let us calculate the zero-point energy 0|H^F |0 of a particle field Hamiltonian H^F .
This calculation can be viewed as a summation over quantum harmonic oscillators with the zero-
point energy /2 at all points in space:

0|H^F |0  =             1                                        .                                (7)
                2
                   n=1

Since the axiom �Inf is a part of quantum formalism L(QFT), the existence of an endless sequence

of units such as 1, 1, 1, . . . = (1) n=1, where the symbol  denotes an unbounded limit, is not
allowed. The implication of this is that the series n=1 1 must end up convergent. Thence, the
vacuum energy ought to be finite. By contrast, if the axiom Inf, not its negation, were to be a

part of L(QFT), then the infinite sequence of additions 1 + 1 + 1 + � � � =       1  would  have  the
                                                                             n=1

right to be in (7) resulting in the infinite zero-point energy.

Then again, the zero-point energy could always be finite if space were to have a finite number of
points, id est, if a geometry of physical space were to be finite.

Before proceeding further, allow us to clarify the difference between finite geometries, bounded
(finite) metric geometries and discrete geometries. For the purpose of the current presentation,
one can define a geometry as a system of axioms that identify what "things" are which constitute
"points", "lines", "planes", and so forth.

In terms of this definition, a finite geometry is any of axiomatic systems that have only a finite
number of points.

A finite metric geometry, on the other hand, is an axiomatic system whose set of points is bounded,
i.e., all of its points are within a certain (finite) distance of each other [14].

At the same time, a discrete geometry (including the causal set program [15, 16, 17] whereby
spacetime is a collection of points randomly selected in a background continuous space) takes up
only objects in which points are isolated from each other in some sense, as for example, the set of
natural numbers is a discrete set, i.e., a set of isolated points.

             4
Most important of all, neither a finite metric geometry nor a discrete geometry need to have a finite
number of points.

Unless otherwise stipulated, henceforth the statements will relate to finite and non-finite geometries
alike.

Let M denote a manifold (such as a surface or a space). Assume that the manifold M admits a
notion of distance between its points; so, M is equipped with measures of its regions (i.e., connected
parts of M ) such as area A and volume V .

Consider a manifold R that is taken to be a region in another manifold M , which means that R
is deemed to be a subset of M having the same dimension as M does. For instance, R can be a
3-ball in Euclidean 3-space.

Conceding that the characteristic length L(R) defining the linear scale of the region R is the ratio
of the region volume V (R) to the area A(R) of the region boundary, i.e.,

                 L(R)           =  V (R)                    ,           (8)
                                   A(R)

and on condition that  is given by the expression

                             =   2c                      ,              (9)
                                L(R)

one finds

           0|H^F |0          =   c                    �  Pvac     .     (10)
                                L(R)

where Pvac denotes the series 1 + 1 + � � � = n=1 1.

3 The holographic principle

Naturally, the zero-point energy 0|H^F |0 can be presented as the result of multiplying the vacuum
energy density vac by the region volume V (R). So, by allowing vac to be proportional to the
effective cosmological constant eff , namely,

                 vac         =   c4                � eff       ,        (11)
                                8G

one can express the cardinality of the region R (the number of points constituting R) in terms of
eff :

           Pvac  =  eff         � V (R) � L(R)                       ,  (12)
                                  822P

                                   5
where P = G/c3.
At this juncture, let us establish two positive dimensionless ratios:

     :=    eff � DU2     ,                                             (13)
              82

   (R)     :=   L(R)     ,                                             (14)
                 DU

in which DU stands for the comoving ("static") diameter of the observable universe. As eff and
DU are both nonnegative constants, the ratio  is expected to remain constant in time. Using 
and (R), one can present (12) as the equality

Pvac = V (R) � V (R) = A(R) � A(R) ,                                   (15)

where V (R) and A(R) denote the volumetric density and the areal density of the cardinality of
the region R, respectively,

V  (R)  =    �    2(R)         ,                                       (16)
                L(R) � P2

A(R)     =      �  2(R)     .                                          (17)
                     2P

This enables the holographic principle: points that compose a region are entirely contained in the
boundary to the region.

4 The entropy in a manifold

Let C(R) be a system of coordinates, i.e., a set of numbers, that specify the position of each point
in a region R. To be qualified as systems of coordinates, C(R) must be such that the operations of
addition, subtraction, multiplication, and division are defined and satisfy the closure under addition
and subtraction. Considering this, the system of coordinates C(R) must be a field [18].

In a geometry that has only a finite number of points, the cardinality of the field C(R) is a prime
power, i.e.,

   card (C(R)) = pq ,                                                  (18)

where p is a prime number and q is the number of points comprising the region R. This means that
the system of coordinates C(R) has pq elements, q log p degrees of freedom and can store q log2 p
bits of information (that is, log2 p bits per each point in R).

                                                                6
A measure of ignorance about the position of the points in R can be taken to be proportional to
2q, i.e., the smallest possible size of a coordinate system for a given region. For that reason, the

entropy in the region R can be determined as

H(R) = kB � log2 card (C(R)) = kB � q ,                                    (19)

where kB is the Boltzmann constant. The above allows to construe each point in space as a bit of
information.

Recalling that q = Pvac and using the equality (15), one finds that the entropy in a volume V (R)
is equivalent to the entropy in the area A(R) of the boundary to R. In symbols,

kB � Pvac = H(V (R)) = H(A(R)) ,                                           (20)

where H(V (R)) and H(A(R)) denote the entropy in V (R) and A(R) such that

H(V (R))  =  kB  � V V (R)  =  kB  �   2(R)        � V (R)     ,           (21)
                                      L(R) � 2P

H (A(R))  =  kB  �  AA(R)   =  kB     �  2(R)   �  A(R)     .              (22)
                                            P2

5 The cosmological constant problem

Thanks to the factor  = 8G/c4, the upper bound on the effective cosmological constant eff =
 � vac laid by observations is interpreted as an observational bound on the vacuum energy density
vac. The problem is that the zero-point energy calculated along the lines of the axiom of infinity
Inf comes out infinite: Recall that the series Pvac := 1 + 1 + � � � = n=1 1 diverges under the
assumption that Inf holds true. And even though the formalism based on Inf can produce (at the
quantitative level) finite values of vac using one or another renormalization scheme, such finite,
renormalized, values end up being greater than the observational bound by at least 40 orders
of magnitude [19, 20, 21]. This constitutes the conundrum known as "the cosmological constant
problem".

In contrast, within the formalism wherein the axiom �Inf is a part, the number of points Pvac
constituting space is finite, which, in turn, indicates that the vacuum energy is intrinsically finite.

What is more, on large scales, the space wherein the universe lives is well approximated as three-
dimensional and flat [22]. Given that, the manifold MU associated with the universe can be esti-
mated as a 3-dimensional Euclidean space. By the same token, the region RU  MU representing
the space of the observable universe can be looked upon as an ordinary ball (i.e., a 3-ball) of volume
V (RU ) with the boundary of area A(RU ). Accordingly, L(RU ) = RU /3 and (RU ) = 1/6.

                            7
Hence, considering that (a) a black hole is the most entropic object one can put inside the spherical
surface enclosing the region of the observable universe RU , and (b) the observable universe is not
a black hole, one can find the upper bound of the entropy in the area A(RU ):

                                  H(A(RU )) < HBH(A(RU )) ,                  (23)

where HBH is the Bekenstein-Hawking entropy [23, 24]

                                  HBH(A(R))      =  kB  �  A(R)              (24)
                                                            4P2

in which R = RU .

As to the entropy H(A(RU )), using (22) it can be evaluated as

                   H(A(RU ))              =  kB  ��     1   � A(RU )  .      (25)
                                                      622P

Thus, the bound (23) produces

                                             <9 .                            (26)

Due to the fact that the ratio  is on a par with 1, the effective cosmological constant eff is close
to zero. To wit,

                   eff         =  82   �  <  182      9.3 � 10-52 m-2    ,   (27)
                                  DU2        RU2

where RU is the comoving radius of the observable universe.                  10-52 m-2 [25] by

The above result exceeds the bound implied by cosmological observations eff
only one order of magnitude.

6 The volume inside a black hole

The relation between geometry and information may help to define a meaningful notion of volume
inside a black hole.

For convenience of reference, let us denote the region of a black hole by RBH. Unlike A(RBH), the
area of the horizon (i.e., surface) of a black hole remaining the same for all observers, the volume
inside a black hole, V (RBH), is not a precisely defined concept: V (RBH) depends on an arbitrary
choice of coordinates, and as such can be time dependent, or even zero [26, 27, 28].

This implies that the characteristic length of the black hole's interior,

                                                                8
             L(RBH)     =     V (RBH)         ,                                              (28)
                              A(RBH)

is undefined and so is the ratio (RBH) = L(RBH)/2RU . As a result, one can only argue that the
amount of information inside a black hole is contained on the surface of the black hole, namely,

   H(V (RBH)) = H(A(RBH)) .                                                                  (29)

This begs the question: If V (RBH) were to be undefined, how could this expression be true?
But then, in accordance with (22) the said amount of information can be calculated as

H (A(RBH ))  =   kB  �     �  L2(RBH)      �  A(RBH)     .                                   (30)
                                 4RU2            2P

Comparing the above with the Bekenstein-Hawking entropy (24) in which R = RBH gives

          L(RBH)        =  RU    >  RU           .                                           (31)
                                     3

Hence, the Bekenstein-Hawking assumption of black hole entropy is equivalent to the supposition
that L(RBH) is one and the same for all black holes and it is commensurate with the comoving
radius of the observable universe.

Therefore, the unique interior volume of a black hole (invariable for all observers) can be believed
to be

V  (RBH)  =  RU  �  A(RBH)       >  1  RU  �     A(RBH)  .                                   (32)
                                    3

Owing to the term h > RU /3, the volume V (RBH) = h � A(RBH) is extremely large. By way of

example, for a Schwarzschild black hole with the area of the horizon of radius RS  3 km, V (RBH)
is greater than the volume of the sphere in 3-space R3 with the radius rsphere comparable with the

distance from the Sun to Mars:

   rsphere > 3 RU RS2  226 million km .                                                      (33)

Concerning a geometric shape of the interior region of a black hole, it can be imagined in agreement
with the formula (32) as a figure resembling a cylinder with the base of area A(RBH) and the height
h. Providing the surface area of the hole's interior coincides with the area of the event horizon, the
surface area of the cylinder should be made up of just one component, A(RBH). This means that
the said cylinder must be devoid of its side and one of its bases. Needless to say, a geometric shape
like this cannot exist in a three-dimensional Euclidean space.

                              9
7 Magnification of a holographic image

The product of V (R) and V (R) determines the amount of information contained in a region R of
volume V . Therefore, V (R) can be considered to be the three-dimensional (volumetric) density
of information. Likewise, A(R) can be seen as the two-dimensional (areal) density of information
contained in the boundary to the region R.

Consider R = RU . In line with (16) and (17), the degrees of information concentration in RU are:

                     V   (RU     )  =     �      1        ,                  (34)
                                             12RU 2P

                     A(RU )            =     �    1    .                     (35)
                                                622P

From here it follows that the area containing 1 bit of information is

                          A1 = -1 (6P )2 ,                                   (36)

at the same time as the volume composed of 1 bit of information is

                     V1  =    1  RU    � -1 (6P )2        .                  (37)
                              3

In a mathematical formalism embracing the axiom �Empty, the minimum cardinality of a manifold

must be 1. This requires that all A and V must be bounded from below such that A  A1 and

V  V1. Providing sphericalness of A and A1, as well as V and V1, it means rA  rA1 and rV  rV1,
where

                  rA1 = 3 P > 1 P  P ,                                       (38)

rV1 =  3   1  RU  �  (6P  )2  >     3  1  RU    �  P2   3.3 � 10-15 m  s  .  (39)
          4                            

As appears, the minimal length scale in a two-dimensional manifold is the Planck length P , while

the said scale in a three-dimensional manifold is equivalent to the approximate limit of the strong

interaction s  3.0 � 10-15 m. That is to say, there are two different minimal length scales in

physical space: P and s. Such cannot be unless the sphere of radius rV1      s is an enlarged
holographic image of the circle of radius rA1 P .

This enlargement explains the puzzlement of the holographic principle. Definitely, suppose, for a

moment, that there is no enlargement. Then, covering a surface of the observable universe with

primitive circles of radius rA1 would be holographically projected as filling in the interior of the
universe with spheres of radius rA1. Since rA1  RU , the universe's interior could be considered

                                       10
as a set of points with the cardinality greatly surpassing the number of points that constitute the
universe's surface:

RU3   =     4RU2    � RU      4RU2  .  (40)
rA31     -1 (6P )2   rA1        A1

Obviously, that would be contradictory to the holographic principle. However, due to the holo-
graphic enlargement, the universe's interior is discretized by spheres of radius rV1, therefore,

RU3   =     4RU2    �  RU  =  4RU2  .  (41)
rV31     -1 (6P )2     RU      A1

Magnification of a holographic image projected from the surface of the observable universe into its
interior can be quantified by the ratio

         rV = 3 RU .                   (42)
         rA            rA

The above means that if the size of the image is rV , then the "true" size of a projected object rA
can be estimated as

         rA =       rV3    .           (43)
                    RU

For example, the Solar System whose radius is rV  4.5 billion kilometers can be believed to be
a holographic image of a two-dimension structure of size rA  455.1 kilometers "painted" on the
boundary to the observable universe.

By the same token, the "true" distance between the Sun and the nearest known planetary system
(Proxima Centauri system) equal to 4.2 light-years when measured through a region of space would
be 377.6 million kilometers (about the distance from the Sun to the asteroid belt occupying the
orbit between Mars and Jupiter) if it were to be measured on the surface of the observable universe.

In passing, it should be noted this. Because the weak force has an effective range w which is shorter
than s (namely, w is around 10-17 to 10-16 m), it can be inferred that the weak interaction takes
place only on a surface of the observable universe. Certainly, had 3w been a holographic projection
of some area on the surface of the observable universe, its "true" scale would have been  1.5�10-39
m in accordance with (43), i.e., much less than the Planck length P . This may explain why the
weak interaction does not produce a bound state, i.e., one in which a particle tends to remain
localized in a region of space.

               11
8 Concluding remarks

The following critical comments could be passed on the claims put forward in this paper.

The existence of a minimal length scale modifies the Heisenberg uncertainty principle, so that it is
impossible to localize a test particle in essence. Subsequently, the notion of "point" breaks down
causing the cardinality of a physical manifold (i.e., the number of points constituting this manifold)
to become an ill-defined measure. Due to this, talking about the finiteness of the physical manifold
has little sense.

To reply to this criticism, let us first recall that gravity � instead of spoiling the renormalizability
of quantum field theories � has long been suggested to lead to an effective cutoff in the ultraviolet,
i.e. a minimal length scale 0 [29, 30]. Logically 0 implies a nonzero minimal uncertainty x0 in
position measurements. The latter can be implemented by generalizing the Heisenberg uncertainty
principle.

For example, in one dimension, the simplest generalized uncertainty relation incorporates a new
term in the right hand side proportional to (p)2, namely, xp  /2 + (p)2, where  is a
positive parameter independent of x and p. So, when p increases, the new term precludes x
from becoming arbitrarily small. This results in a nonzero minimal uncertainty x0.

Be that as it may, the existence of x0 does not necessarily mean that there is a minimal length
scale 0 [31]. In fact, the implication 0  x0 is identical to that of �0  x0. The last reads:
"It is true to say that there is x0 but no such thing as 0".

Secondly, in accordance with the expression for the entropy in the manifold proposed in this paper
(see for example Eq. (19)), each point constituting the physical manifold equates with a bit of
information. Accordingly, the finiteness of the manifold is the notion defined as well as it gets. By
way of illustration, the finiteness of the space of the observable universe signifies that the amount
of information required to describe this space is limited.

Thirdly, the existence of cutoffs is necessary for treating infinities that arise in calculated quantities
of quantum field theories. Whatever such cutoffs are, they all involve nontrivial assumptions like
the presence of unknown new physics [32, 33]. Meanwhile, another, almost trivial way to avoid
infinities in physics in the first place is to negate the axiom of infinity Inf of Zermelo-Fraenkel set
theory. This is exactly what has been demonstrated in the present paper.

Conflict of interest

The author states that there is no conflict of interest.

Data Availability Statement

The original contributions presented in the study are included in the article, further inquiries can
be directed to the corresponding author.

                                                               12
References

 [1] Gerard 't Hooft. Black holes and the dimensionality of space-time. In Ulf Lindstr�m, editor,
      The Oskar Klein Centenary. Proceedings of the Symposium, 19-21 Sept. 1994, Stockholm,
      Sweden, pages 122�137. World Scientific, 1995.

 [2] Leonard Susskind. The World as a Hologram. J. Math. Phys., 36:6377�6396, 1995.

 [3] Daniela Bigatti and Leonard Susskind. TASI lectures on the Holographic Principle.
      https://arxiv.org/abs/hep-th/0002044, Feb 2000.

 [4] Raphael Bousso. The holographic principle. Reviews of Modern Physics, 74:825�874, 2002.

 [5] Michio Kaku. Introduction to Superstrings and M-Theory. Springer, 2011.

 [6] Martin Ammon and Johanna Erdmenger. Gauge/Gravity Duality: Foundations and Applica-
      tions (1 ed.). Cambridge University Press, 2015.

 [7] Juan Maldacena. The Large N limit of superconformal field theories and supergravity. Ad-
      vances in Theoretical and Mathematical Physics, 2:231�252, 1998.

 [8] Larry McLerran. Theory Summary: Quark Matter 2006. Journal of Physics G: Nuclear and
      Particle Physics, 34(8):S583�S592, 2007.

 [9] Arkady Bolotin. Physics in a finite geometry. https://arxiv.org/abs/2212.02915, Dec 2022.

[10] Eric W. Weisstein. Urelement. In From MathWorld � A Wolfram Web Resource.
      https://mathworld.wolfram.com/Urelement.html, 2022.

[11] Ralph Gregory Taylor. Zermelo, Reductionism, and the Philosophy of Mathematics. Notre
      Dame Journal of Formal Logic, 34(4):539�563, 1993.

[12] David Edwards. The Mathematical Foundations of Quantum Mechanics. Synthese, 42(1):1�70,
      1979.

[13] Alyssa Ney. Reductionism. In The Internet Encyclopedia of Philosophy. ISSN 2161-0002.
      https://iep.utm.edu/red-ism/, 2022.

[14] Dmitri Burago, Yuri Burago, and Sergei Ivanov. A Course in Metric Geometry. American
      Mathematical Society, Providence, Rhode Island, 2000.

[15] Graham Brightwell and Ruth Gregory. Structure of Random Discrete Spacetime. Physical
      Review Letters, 66(3):260�263, 1991.

[16] Raphael Sorkin. Causal sets: Discrete gravity. In A. Gomberoff and D.Marolf, editors, Lectures
      on Quantum Gravity, volume Pan-American Advanced Studies Institute, School on Quantum
      Gravity, pages 305�327. Springer, 2005.

[17] K�roly Bezdek. Classical Topics in Discrete Geometry. Springer, New York, NY, 2010.

[18] Gary L. Mullen and Daniel Panario. Handbook of Finite Fields. Chapman and Hall/CRC,
      New York, 2013.

                                                               13
[19] Svend E. Rugh and Henrik Zinkernagel. The Quantum Vacuum and the Cosmological Constant
      Problem. Studies in History and Philosophy of Modern Physics, 33(4):663�705, 2001.

[20] Sean M. Carroll. The Cosmological Constant. Living Reviews in Relativity, 4(1):1�56, 2001.
[21] Phillip James Edwin Peebles and Bharat Ratra. The cosmological constant and dark energy.

      Reviews of Modern Physics, 75(2):559�606, 2003.
[22] Andrew Liddle. An Introduction to Modern Cosmology. Third Edition. Wiley, UK, 2015.
[23] Jacob D. Bekenstein. Holographic bound from second law of thermodynamics. Physics Letters

      B, 481:339�345, 2000.
[24] Stephen W. Hawking. Black hole explosions? Nature, 248(5443):30�31, 1974.
[25] Planck Collaboration: P. A. R. Ade et al. Planck 2015 results - XIII. Cosmological parameters.

      Astronomy & Astrophysics, 594:A13, 2016.
[26] Maulik K. Parikh. Volume of black holes. Physical Review D, 73(124021):1�5, 2006.
[27] Brandon DiNunno and Richard A. Matzner. The Volume Inside a Black Hole. General Rela-

      tivity and Gravitation, 42:63�76, 2010.
[28] Marios Christodoulou and Carlo Rovelli. How big is a black hole? Phys. Rev. D, 91(064046):1�

      7, 2015.
[29] Achim Kempf, Gianpiero Mangano, and Robert B. Mann. Hilbert Space Representation of

      the Minimal Length Uncertainty Relation. Phys. Rev. D, 52(1108), 1995.
[30] Kourosh Nozari and Amir Etemadi. Minimal length, maximal momentum and Hilbert space

      representation of quantum mechanics. Phys. Rev. D, 85(104029), 2012.
[31] Sabine Hossenfelder. Minimal Length Scale Scenarios for Quantum Gravity. Living Reviews

      in Relativity, 16(2):1�90, 2013.
[32] G. 't Hooft and M. Veltman. Regularization and renormalization of gauge fields. Nuclear

      Physics B, 44:189�213, 1972.
[33] Tian Yu Cao and Silvan S. Schweber. The Conceptual Foundations and the Philosophical

      Aspects of Renormalization Theory. Synthese, 97:33�108, 1993.

                                                               14
