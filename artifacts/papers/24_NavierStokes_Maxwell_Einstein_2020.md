# NavierStokes Maxwell Einstein 2020

**Source:** `24_NavierStokes_Maxwell_Einstein_2020.pdf`

---

Published for SISSA by Springer                             JHEP08(2020)147
                                                                                                              Received: June 1, 2020
                                                                                                             Accepted: July 25, 2020

                                                                                                         Published: August 28, 2020

From Navier-Stokes to Maxwell via Einstein

Cynthia Keeler, Tucker Manton and Nikhil Monga
  Physics Department, Arizona State University,
  Tempe, AZ 85287, U.S.A.
  E-mail: [email redacted], [email redacted], [email redacted]

Abstract: We revisit the cutoff surface formulation of fluid-gravity duality in the context
of the classical double copy. The spacetimes in this fluid-gravity duality are algebraically
special, with Petrov type II when the spacetime is four dimensional. We find two special
classes of fluids whose dual spacetimes exhibit higher algebraic speciality: constant vorticity
flows have type D gravity duals, while potential flows map to type N spacetimes. Using
the Weyl version of the classical double copy, we construct associated single-copy gauge
fields for both cases, finding that constant vorticity fluids map to a solenoid gauge field.
Additionally we find the scalar in a potential flow fluid maps to the zeroth copy scalar.

Keywords: Classical Theories of Gravity, Gauge-gravity correspondence, Scattering Am-
plitudes

ArXiv ePrint: 2005.04242

Open Access, c The Authors.  https://doi.org/10.1007/JHEP08(2020)147
Article funded by SCOAP3.
Contents

1 Introduction                                                 1

2 The hydrodynamic limit and near-horizon expansion            3

3 Classical double copy                                        5

3.1 Kerr-Schild double copy                                    5

3.2 Weyl double copy                                           6                                 JHEP08(2020)147

4 Fluid solutions                                              8

4.1 Petrov type D fluid solutions                              11

4.2 Petrov type N fluid solutions                              11

5 Type D double copy                                           13

5.1 Weyl double copy                                           13

5.2 Effective electric and magnetic fields                     14

5.3 Weyl double copy in the near horizon expansion             16

6 Type N Weyl double copy                                      16

6.1 Planar extensional flows                                   17

6.2 General potential flows                                    18

7 Discussion                                                   19

A Spinor formalism                                             20

B Newman-Penrose formalism                                     22

C Tetrads in the hydrodynamic and the near horizon expansions  24

1 Introduction

The fluctuations of spacetime near a horizon can be described by a fluid equation, as first
found almost forty years ago [1, 2]. Further development of this idea led to the membrane
paradigm [3�9], in which the fluid lives on a stretched horizon. The advent of AdS-CFT
duality twenty years ago allowed for a version of fluid-gravity duality where the dual fluid
arises from the gauge theory living on the AdS boundary [10�19]; for reviews see [14, 20�23].

     More recently, the cutoff surface approach to fluid-gravity duality, pioneered in [24, 25]
and extended in [25�33], built a precise version of the membrane paradigm which defines
the fluid via the extrinsic curvature of an intrinsically flat hyperbolic `cutoff' surface held

                                                        �1�
outside the horizon. In the formulation of cutoff surface fluid-gravity we follow in this         JHEP08(2020)147
paper, [25], the Einstein constraint equations on the hyperbolic cutoff surface become the
nonlinear incompressible Navier-Stokes equations, while solving the remaining Einstein
equations defines the rest of the spacetime. We will work mostly with the low order terms
in the long-wavelength or hydrodynamic limit, which amounts to a gradient expansion; as
shown in [27], this procedure does allow a full perturbative expansion.

     The classical double copy as first presented in [34] builds a map between classical
gravity solutions and classical Yang-Mills solutions, based on the color-kinematics duality
valid at the amplitude level (see [35] for a comprehensive review). Since the metric of
the gravitational solution is built out of two copies of the classical Yang-Mills solution,
the Yang-Mills solution is referred to as the `single copy' of the corresponding metric, and
there is also a corresponding Klein-Gordon scalar solution termed the `zeroth copy'. As an
example, the single copy of the Schwarzschild black hole metric is the field arrangement due
to a color charge at the origin, when the dilaton expectation value is tuned to zero [36].
Many other examples of the classical double copy have been built [37�53], including to
some broad classes of spacetime [54]. Furthermore [55�64] have used this classical mapping
to improve the perturbative series used in analytic calculations of black hole collisions.

     We build herein the single copy gauge fields which map to fluid-dual metrics, for two
different classes of Navier-Stokes solutions. We are able to accomplish this map by relying
on the algebraic speciality of these fluid-dual metrics. A spacetime is algebraically special
if its Weyl tensor exhibits extra symmetry; specifically, if two or more of its principal
null vectors coincide. In four dimensions, spacetimes of Petrov type D have two pairs of
coinciding principle null vectors, while spacetimes of type N have all four principal null
vectors coincident. Using the constrained form of the Weyl tensor for algebraically special
spacetimes, [54] exhibited a single copy gauge field (and zeroth copy scalar field) valid for
every type D vacuum solution to general relativity.

     As [25, 30] note, the spacetime corresponding to the fluid metric is algebraically special;
for four dimensions, the spacetime has Petrov type II. As we will show, further restricting
the fluid results in higher algebraic speciality. We focus on two special fluid classes: con-
stant vorticity fluids and potential flows. Constant vorticity fluids are dual to spacetime
metrics with Petrov type D, while potential flow fluids are dual to metrics with Petrov
type N. Such fluids have also been studied in the context of holography, for instance for
flows with vorticity [65, 66]. Consequently, using the Weyl double copy proposed in [54],
we are able to exhibit the single copy gauge fields whose double copy metric is then dual to
either a constant vorticity fluid or a potential flow fluid. Since these gauge fields are in the
U(1) sector of the Yang-Mills theory, we have thus mapped two classes of Navier-Stokes
solutions to Maxwell solutions.

     The gauge field corresponding to the constant vorticity fluid matches the constant
axial field within a large solenoid, while the zeroth copy is a constant. For the potential
flow fluids, the gauge field is the same for every potential flow; it corresponds to a static
Maxwell field with Poynting vector pointing towards the horizon. We find the scalar flow
potential maps to the zeroth copy scalar field. Thus, just as the nontrivial details of the
constant vorticity fluid map to the single copy field, the nontrivial details of the potential
flow fluid map instead on to the zeroth copy scalar potential.

                                                        �2�
     In section 2 we begin by reviewing the cutoff approach to fluid-gravity duality from [25].
In section 3, we briefly review the classical double copy story, focussing on the Weyl double
copy as developed in [54]. In section 4 we show that constant vorticity fluids map to type
D vacuum metrics, while potential flow fluids map to type N metrics. In sections 5 and 6
we build the single copy for the gauge fields associated with these metrics. In section 7 we
discuss the physical implications of our results and speculate on the viability of a classical
double copy picture for generic fluid-dual spacetimes.

2 The hydrodynamic limit and near-horizon expansion

In this section we review the cutoff surface formulation of fluid-gravity duality and reiterate               JHEP08(2020)147
the equivalence between the hydrodynamic limit and the near horizon expansion explored
in [25]. In order to obtain Navier-Stokes equations from Einstein's equations, we begin with
a background Rindler spacetime written in ingoing Eddington-Finkelstein coordinates:

                                 ds20 = -rd 2 + 2d dr + dxidxi.                      (2.1)

Here i, j will be the spacelike fluid directions; for a fluid in 2 + 1 dimensions, i, j run

over 1, 2 and the associated metric is four-dimensional. Constant r hypersurfaces in these

coordinates are intrinsically flat and foliate the spacetime metric into hyperbolic slices.

     We then choose one such slice, r = rc, and perturb the spacetime there, generating
extrinsic curvature for the r = rc slice as embedded in the full spacetime. We identify this

extrinsic curvature ab with the fluid stress tensor Tab; here a, b run over the directions
along the rc slice (that is, a, b take values  or i, j). The intrinsic metric of this slice ab

thus satisfies

                    ab = -rcd 2 + dxjdxj,                   ab - ab  TaNb S .        (2.2)

For these perturbations, we impose regularity and infalling boundary conditions at the null
horizon r = 0, thus generating the fluid-dual metric1

ds2 = - rd 2 + 2d dr + dxidxi

                -2            r  vidxid   -  2 vi  dxidr
                        1-                    rc
                                                                                     (2.3)
                             rc

                           r     (v2 + 2P )d 2 + vivj dxidxj +   v2 2P         d dr
                + 1-                                    rc          +
                            rc
                                                                 rc rc

                -  (r2  -   rc2) 2vidxid  +  O(    3).
                        rc

The here refers to the order in the hydrodynamic or long wavelength expansion, explicitly

                        i  ,   2, v  , P  2.                                         (2.4)

    1The flat space portion of this metric is written iningoing Eddington-Finkelstein coordinates, which are
obtained from Minkoswki by setting , t+  (t + z)/ 2 and t-  (t - z)/ 2. We then further transform

to r = t+t-/2 and  = 2 log t+. In these coordinates, paths of constant  correspond to ingoing light rays,
while surfaces of constant r correspond to the hyperbolae z2 - t2 = 4r.

                                             �3�
The metric in (2.3) is arranged with background terms of order O( 0) in the first line, O( )
terms in the second, and so on.

     With these identifications, the r = rc constraint components of Einstein's equations,
G and Gi, become incompressibility and the Navier-Stokes equation:

G00 = 0 = ivi = 0,                                                         (2.5)
G0i = 0 =  vi - 2vi + iP + vjjvi = 0,

where the shear viscosity  is identified2 with rc.                                            JHEP08(2020)147
     As in [25], to relate the hydrodynamic limit to the near horizon limit, we introduce

hatted coordinates and variables:

xi = rcx^i ,    =  rc^       ,  r = r^rc,  vi = v^i  P = 2P^.              (2.6)

                     2

Next, we rescale the metric and define a new perturbative parameter :

                          2     z2 - t2 = 4rc  4,              2           (2.7)

ds2  ds^2 = rc2 ds2                                   .
                                                           rc

This new expansion parameter  controls the near horizon expansion. The limit   0
sets the r = rc hypersurface to be null, just like the r = 0 Rindler horizon. In the near
horizon expansion the metric thus becomes

ds^2 = - r^ d^2                                                            (2.8)


        + 2d^dr^ + dx^idx^i - 2(1 - r^)v^idx^id^ + (1 - r^)(v^2 + 2P^)d^2

        +  (1 - r^)v^iv^jdx^idx^j - 2v^idx^idr^ + (v^2 + 2P^)d^dr^
        + (r^ - 1)[-(r^ + 1)^2v^i + (v^2 + 2P^)2v^i + 4^iP^]dx^d^ + O(2).

In this sense [25] demonstrate that the near horizon expansion matches the long wavelength
limit, consistent with the perspective that horizons behave as incompressible fluids.

     As discussed further in appendix C, the replacements

xi  xi,   2, v  v, P  2P.                                                  (2.9)

allow derivation of the incompressible Navier-Stokes equation starting from a solution of
more complicated equations; essentially, any other terms become higher order terms in the

  expansion. Additionally, these replacements will bring a Navier-Stokes solution that is
not initially in the long wavelength limit (2.4) into that limit. The near horizon expansion
makes these replacements explicit, so it is valid for Navier-Stokes solutions that are not
naturally in the hydrodynamic limit, such as vortices. Consequently, although we mostly
use the hydrodynamic expansion below, we will return to the near horizon  expansion
when necessary.

    2Note that in the near horizon expansion   1.

                                �4�
3 Classical double copy

In the past few decades, significant steps have been made towards a deeper understanding
of graviton scattering amplitudes and their relation to gauge scattering amplitudes. Most
relevant for this article is the double copy prescription (see [35] and references within for a
comprehensive review of the subject). Stated simply, the double copy obtains complicated
graviton scattering amplitudes from simpler gauge theory amplitudes. The gauge theory
amplitude AYM is written in a generalized gauge such that it takes the schematic form

                         AYM            nkck ,     (3.1)                                              JHEP08(2020)147
                                      propagators
                                   k

where the sum is over all three-point vertex graphs, the nk are the kinematic numerators
associated with each graph, and the ck are the color factors that satisfy a Jacobi identity of
the form ci + cj + ck = 0. The basic principle in obtaining the graviton amplitude relies on
a particularly simple duality between color and kinematics, the BCJ duality first presented
in [67], being made manifest.

     The double copy prescription then provides the corresponding graviton amplitude,

                         Mgrav          nknk ,     (3.2)
                                      propagators
                                   k

where the color factors ck have been replaced with a second set of kinematic numerators
nk that are organized to also satisfy a Jacobi identity of the same form. There is also a
`zeroth copy' in the amplitudes story, where starting with (3.1), replacing the kinematic
numerators ni with a second set of color factors c~i builds scalar amplitudes of the form

                         Ascalar        ckc~k ,    (3.3)
                                      propagators
                                   k

for bi-adjoint scalars aa . As we will see below, a zeroth copy scalar can also be found in
the classical double copy story; it will play a significant role for the potential flow fluid class.

     When the double copy procedure is applied to pure (non-supersymmetric) Yang-Mills
theory, the resulting theory on the gravity side is general relativity coupled to a two-
form field and a dilaton. Although these amplitude relations are perturbative quantum
statements, the authors of [34] used these relations to inspire a double copy mapping
between classical solutions in general relativity and classical solutions in the U(1) sector of
Yang-Mills.3 This relation is referred to as the classical double copy.

3.1 Kerr-Schild double copy

The key connection between the classical gravity and gauge theory solutions first presented
in [34] is the use of Kerr-Schild coordinates, where

                         g� = � + k�k .            (3.4)

3Some nonabelian behavior is covered in e.g. [40, 53], but here we focus on only the abelian sector.

                                   �5�
Here,  is a scalar function that plays the role of the zeroth copy, and satisfies the wave
equation over the flat background, �� = 0. The vector k� is null with respect to
both the full and background metrics,

                             g� k�k = � k�k = 0.                                      (3.5)

This feature serves to truncate the inverse metric to g� = � - k�k, with the further

consequence that the null vector can be raised with either the background or full metric,

k� = g� k = � k .

The classical double copy states that if g� is a solution to the Einstein equations, then          JHEP08(2020)147

the gauge field given by

                             A�a = cak�                                               (3.6)

is a solution to Yang-Mills theory. Since the ca are just constant color factors in these
solutions, these solutions really live in a U(1) sector of the gauge theory; that is, A� = k�
will be a Maxwell solution. We refer to (3.6) as the single copy, in line with terminology
in the amplitudes story.

     The connection between the classical story and amplitudes story can be seen by re-
placing the color vector ca in (3.6) with the null vector k� in (3.4) to obtain h� from the
gauge theory, akin to replacing ck  nk. Moreover, the zeroth copy analogy can be seen by
replacing k�  ca in (3.6) to get aa = caca , in the same spirit as replacing ni  c~i to
obtain (3.3) from (3.1). The mapping (3.6) has been extensively studied for various exact
solutions living on flat space [34, 37, 41, 42, 45�47, 57, 68�71] and extended to solutions
living on maximally-symmetric backgrounds [43, 44].

     Some classical solutions that have been shown to exhibit a reasonable double copy
necessitate an extension to the ansatz (3.4); [37, 48, 54] write the full metric in double
Kerr-Schild form, where

                             g� = � + k�k + l�l .                                     (3.7)

Here the vectors k and l are individually null as well as orthogonal (orthonullity);

                             k2 = l2 = k � l = 0.                                     (3.8)

Again, the indices for both vectors can be raised and lowered with either the full metric

g� or the background metric �. This form was necessary for the single copy study of the

Taub-NUT solution [37] as well as for the generic type D vacuum solutions in [54], where

the gauge field is given by

                             Aa� = ca k� + l� .                                       (3.9)

3.2 Weyl double copy

In our work, we will utilize a different realization of the classical double copy, referred to as
the Weyl double copy [54]. This prescription for the double copy relies on the spinor for-
mulation of general relativity [72, 73] in conjunction with the Petrov classification (see [74]
chapters 3 and 4 for a review of both concepts) to build the map between the gravitational

                             �6�
and gauge theories. This version of the double copy applies to four-dimensional space-
times, although [39] builds towards an extension to higher dimensions; for now we review
the four-dimensional picture.

     The Petrov classification labels metrics by the multiplicities of the principle null direc-
tions of their Weyl tensors. A principle null direction k� satisfies

k�k� = 0,       k[W�][k]k k = 0,         (3.10)

where W� is the Weyl tensor. All four-dimensional metrics will have four (not necessarily         JHEP08(2020)147
unique) solutions k� to these equations, but they can appear with different multiplicities. A
spacetime is algebraically special if any two or more of these principle null vectors coincide.
If only two coincide, the spacetime is Petrov type II; if two pairs coincide, then it is type
D. If all four principle null vectors coincide, then the spacetime is type N. The Weyl double
copy will apply to type D and type N spacetimes, essentially factoring their principle null
vector pairs.

     Since a basic understanding of curved space spinor formalism is necessary to work with
the Weyl double copy, we review the essentials in appendix A. We rewrite the usual Weyl
tensor W� in terms of the completely symmetric Weyl spinor CABCD using the formula

CABCD      =    1  W�     A�B     CD  ,  (3.11)
                4

where A�B are defined in terms of the Pauli sigma matrices as in (A.7).
     The form of the Weyl spinor CABCD is directly related to the Petrov classification of

spacetimes, since the Weyl spinor can be decomposed as

CABCD = (ABC D),                         (3.12)

where the four principle spinors {A, B, C, D} carry the information of the four principle
null directions of the spacetime. The principle spinors can be related to the principle null
vectors using the Pauli 4-vectors via (B.11).

     Since the spinors composing CABCD are directly related to the principle null vectors,
their multiplicity also depends on the Petrov type. If all four spinors are unique, the
spacetime is algebraically general, of Petrov type I. Otherwise the spacetime is algebraically
special. We focus on Petrov type D, where there are two unique principle spinors with
multiplicity two, and Petrov type N, where there is one unique principle spinor. Their
Weyl spinors can be written

CADBCD  (ABC D),      CANBCD  ABC D,     (3.13)

where here  (and , for type D) are the principle null spinors.
     On the gauge theory side, the spinor field strength fAB is the key object, and can be

obtained from the field strength tensor F� directly using

           fAB  =  1  F�  A�B  .         (3.14)
                   2

                �7�
In the same sense as the Weyl spinor, the fAB corresponding to a type D spacetime can be
written as fADB  (AB), whereas in the type N case we have fANB  AB. Thus we find

              1                             (3.15)
CABCD = S f(ABfCD),

where S is a complex scalar field satisfying the wave equation in the flat background on          JHEP08(2020)147
which fAB lives, and whose real part coincides with the Kerr-Schild scalar  up to an
overall constant. Therefore the scalar S plays the role of the zeroth copy in the Weyl
double copy map.

     We will use the decomposition of the Weyl spinor CABCD in terms of a spinor ba-
sis {oA, B}:

CABCD = 0ABC D - 41o(ABC D) + 62o(AoBC D)   (3.16)
              - 43o(AoBoC D) + 4oAoBoC oD.

Here, the I  C, I = 0, 1, 2, 3, 4 are called Weyl scalars, and are also related to the Petrov
classification (see section 4). We will see that the I , and the invariants built out of them,
play a significant role in the Weyl double copy.

     As [54] shows, solutions built from this Weyl double copy picture match the expecta-
tions from the Kerr-Schild double copy as built in [34]. In addition to specific examples
like the Kerr metric, [54] also shows this matching for the most general type D vacuum
solution as written in Plebanski-Demianski coordinates [75] (see [76] and [77] for an ex-
tended treatment).

     We next look to analyze solutions to Navier-Stokes from the fluid gravity perspective
that result in spacetimes that are candidates for the Weyl double copy. As we will now
show, by constraining the velocity fields in the fluid metric (2.3) in one of two ways, we
find that the resulting spacetime is either Petrov type N or type D, allowing for a double
copy treatment via the Weyl method.

4 Fluid solutions

The eigenbivectors of the Weyl tensor for the fluid metric reveal that it is algebraically
special [25, 30]; specifically it is a type II spacetime according to the Petrov classification,
with two coinciding principal null vectors. Below, we use the Newman-Penrose formalism
to find which fluids correspond to metrics with even higher algebraic speciality. Addi-
tional details pertaining to the formalism and our choice of conventions can be found in
appendix B or in [74].

     Briefly, the Newman-Penrose formalism relies on rewriting the metric in terms of a
tetrad set l, n, m, m� , as in (B.1). The tetrad set is then used to compute the Weyl scalars,
which then can be used to compute the invariants I, J, K, L, and N as in (4.2). While the
Weyl scalars depend on the tetrad choice, the invariants do not and thus we will look at
these invariants to classify our spacetimes.

�8�
     We work in the hydrodynamic limit of the metric (2.3), where the first terms we do
not write explicitly4 arise at O( 3). Thus we only know our Weyl scalars up to the same
order, and our algebraic classification of the spacetime is perturbative as well. In this limit,
our tetrad choice (C.2) yields the following Weyl scalars up to O( 3), which is where we
would start to see contributions from neglected higher terms in the metric (2.3):

0 = 0 + O( 3),

1 = 0 + O( 3),                                              (4.1)                                                JHEP08(2020)147

                  2

2 = -i 4rc (xvy - yvx) + O( 3),
3 = 0 + O( 3),

                2

4 = - 2r (xvx - yvy + i(xvy + yvx)) + O( 3).

2 is proportional to the vorticity of the fluid, while 4 is proportional to the derivative
of vx + ivy with respect to the complex coordinate z�  x - iy.

     In order to evaluate the algebraic speciality of our spacetimes, we compute the invari-
ants I, J, K, L and N, via the following relations:

 I  04 - 413 + 322,                                         (4.2)
       4 3 2

J  3 2 1 ,
       2 1 0

K  124 - 3432 + 233,

L  24 - 23,

N  12L2 - 42I.

For a generic fluid-dual metric, we find

I = 3 4 i xvy - yvx                              2          (4.3)
                  4rc 4rc
                                                  + O( 5),
J = 6 i xvy - yvx
                4rc 4rc                        3

                                                + O( 7).

    4Ref. [30] show that algebraically special spacetimes can be obtained to arbitrary order in the context of
the fluid gravity duality in 5 or higher spacetime dimensions. [78] also consider similar spacetimes in d  5,
however posit that additional constraints may be needed in [30] at higher orders to maintain algebraic
speciailty. [27] construct a formulation that progresses to arbitrary order, however this construction deviates
from algebraic speciality and in doing so relates the higher order pieces in the metric to corrections to the
Navier-Stokes equations. Since our interest is primarily in making connection with the Weyl double copy
picture, we restrict ourselves to the first few nontrivial orders of this metric. For more on convergence of
the gradient expansion in a hydrodynamic and fluid gravity context, see [31, 79].

                                          �9�
These I and J satisfy I3 - 27J2 = 0, or more precisely,                              (4.4)
                                         = I3 - 27J 2 = 0 + O( 13),

which implies that the general fluid metric is Petrov type II up to this order.
     Next we look at the invariants K, L, and N :

K = 0 + O( 7),

L = 4 - xvx + yvy - i yvx - i xvy i yvx - i xvy + O( 5),                             (4.5)
        2r 2r         2r         2r  4rc                             4rc                         JHEP08(2020)147

N =9 8  - xvx + yvy - i yvx - i xvy  2 i yvx - i xvy                      2
        2r 2r         2r         2r           4rc                    4rc
                                                                           + O( 9).

Although K is in fact 0 through this order, that is not enough for further algebraic speciality
(see figure 9.1 in [74]). The nonzero invariants L and N are proportional to both the
vorticity (from 2) and z�(vx + ivy) (from 4).

     Before we begin an analysis of which special fluids have dual metrics with higher
algebraic speciality, we must mention briefly the perturbative nature of the metrics we use
in this paper. While [30] constructed fluid-dual spacetimes by requiring algebraic speciality
to hold at all orders, here we instead constrain ourselves only to the lowest orders necessary
in order to establish the incompressible Navier-Stokes equations. Accordingly, we only
establish the higher algebraic speciality of our spacetimes to lowest order.

     To these orders discussed, the condition that the fluids spacetime is a type II metric,
I3 - 27J2 = 0, is satisfied in either the near-horizon or the hydrodynamic expansion:

        I3 - 27J 2 = 0 + O( 13), I3 - 27J2 = 0 + O().                                (4.6)

Note that the highest non-error order available in the near-horizon  expansion differs from
the hydrodynamic expansions, but both spacetimes satisfy the type II constraint to at
least one nontrivial order.

     Specifically, in the near-horizon expansion, we find

                I  =     3       -   x vy )2  +  O(),
                      - 16 (yvx
                                                                                     (4.7)
                         i
                J  =  - 64 (yvx  -   x vy )3  +  O(),

which matches (4.3) except for the expansion order. Since the order of terms differs between
the two expansions, in the near-horizon expansion it turns out to be necessary to account
for terms of order O(2) in the metric (2.8), as was done in [25]. Accordingly we use the
generic form of the tetrad (C.3) to perform computations in this expansion.

     Since the fluid constraints required to produce higher algebraic speciality are the same
at the lowest order of both expansions, we thus concentrate on only the hydrodynamic
expansion for the remainder of this section. As we show below, constant vorticity fluids
will correspond to type D spacetimes while potential flows correspond to type N metrics.

                          � 10 �
4.1 Petrov type D fluid solutions                                                    (4.8)
A Petrov type D spacetime satisfies the following conditions for the invariants:

                             I3 - 27J2 = 0; I, J = 0; K = N = 0.

Based on the forms of L and N in (4.5) and I and J in (4.3), these conditions imply

                xvy - yvx = 0, -xvx + yvy - i yvx + xvy = 0.                         (4.9)

These constraints imply that each component of the velocity satisfies Laplace's equation           JHEP08(2020)147
2vi = 0, where i  {x, y}.

     These conditions are solved by the fluid velocities

                               vx(, y) = -y + hx( ),                              (4.10)
                               vy(, x) = x + hy( ),

with pressures

                2   x2 + y2    +  hy -  hx x -  hx +  hy             y + c( ).    (4.11)
P (, x, y) =

                 2

     In this paper, we will concentrate on the steady state solution centered at the origin;
that is, we set hi( ) = c( ) = 0. Turning these functions on would correspond to a
vortex whose center follows the path (x0( ), y0( )) = ( hxd, hyd ) as time  passes;
a diffeomorphism returning to coordinates centered on the moving vortex would tune the
effective time dependence back to zero.

     Thus the fluid profile we study as representative of fluids dual to type D metrics satisfies

                vx(, y) = -y,     vy(, x) = x,  P          =  2 (x2  + y2)        (4.12)
                                                                            ,
                                                                     2

consistent with vanishing pressure and velocity at the origin as would be expected for a
fluid rotating with constant vorticity, centered at the origin.

4.2 Petrov type N fluid solutions
To obtain a type N spacetime, the invariants must satisfy

                    I = 0, J = 0, K = 0, L = 0, N = 0.                            (4.13)

For the general fluid metric, we already have K = 0 and the invariants I, J (4.3) and

L (4.5) are each proportional to a positive power of the vorticity, so setting the fluid

vorticity xvy - yvx to zero leaves us with a type N dual metric.
     The velocity and pressure profiles of vorticity-free fluids can be written in terms of a

scalar potential :

                    vi = i, iP = -i  - jij.                                       (4.14)

For incompressible fluids,  satisfies Laplace's equation 2 = x2 + y2 = 0, so vorticity-
free incompressible fluids are referred to as potential flows.

                                  � 11 �
     These potential flows can be written cleanly in complex coordinates, i.e. using z 
x + iy. Since 2 = 0, we can rewrite a general solution for the potential  using the sum
of a holomorphic function f and an antiholomorphic function g:

               zz� = 0,  = f (z) + g(z�).                                                      (4.15)

Imposing reality conditions so as to obtain real velocity and pressure fields requires that
the antiholomorphic function g(z) must be the complex conjugate of the function f (z):

                = f (z) + f�(z�), f�(z�)  (f (z)).                                             (4.16)        JHEP08(2020)147

     Returning to the dual fluid metric, the vorticity-free condition sets 2 = 0, leaving
only 4 nonzero. We can express this nonzero Weyl scalar compactly as

                         4   =    -  2  z�2  =  -  2  z�2f�(z�),                               (4.17)
                                     r             r

while the Weyl tensor becomes

                         CABCD = 4oAoBoC oD.                                                   (4.18)

     Since the function f (z) is holomorphic, we can write a general fluid solution as a
Laurent series in z (and z� for f�):


                         =              n+2zn+2 + c.c.,                                        (4.19)

                               n=-

where n are in general complex valued coefficients and the holomorphic function f (z) 

     n+2zn+2.  Consequently  the  Weyl  scalar  4     can  also   be  written  as  a  Laurent  series.
n=-

It is instructive to look at the forms of the fluid potential and the Weyl scalars for a

few specific fluid solutions here5. We begin by turning on only the n = 0 term in (4.19).

For convenience we additionally choose 2 = -/4, with  real, obtaining the potential

                             (z, z�) = -  (z2 + z�2).                                          (4.20)
                                            4

The corresponding fluid velocity and pressure profiles become

               vx = -x,      vy = y,            P     =  P0 - 2   x2 + y2                      (4.21)
                                                                           .

                                                                      2

This fluid profile is known as planar extensional flow; extensional flows have been well
studied in the fluid-mechanics/materials science community, see e.g. [80]. Our main interest
in this fluid will be its simplicity in terms of the double copy prescription, as we will
see below.

    5Note as for the type D case, we neglect the time dependence that could be allowed in the  coefficients
of the fluid potential and instead consider only steady state flows. As before, time dependence here will
correspond to translating these steady state solutions.

                                        � 12 �
Type of fluid solution Fluid Potential (x, y)                   (z, z�)                   4
                                                                 ln(zz�)             2  r-1z�-2
Source/Sink                  ln(x2 + y2)

Source to Sink (dipole)              x                              z+z�             2 r-1z�-3
       Line Vortex                 x2 +y 2                          2 zz�
                                                                                     i r-1z�-2
    Extensional flow         arctan(y/x)                            ln  z
                                                                2i      z�                    
                                                                                              r
                            -            (x2  -  y2)         -     (z2  +   z�2)
                                      2                         4

Table 1. Some examples of standard fluid solutions and the corresponding non-vanishing scalar 4          JHEP08(2020)147
for type N solutions. For the dipole flow,  refers to the distance between the source and the sink.

Using (4.17), for this fluid we find

                                                                                                 (4.22)
                                         4    =    .
                                                 r

Due to its simplicity and utility as a physical example, we begin with this fluid when we

study the double copy prescription for the Type N fluid dual metrics in section 6.1.

     Other potential flows can also be written compactly in terms of z and z�, using the
form (4.19), as in table 1. We will study the double copy of type N metrics dual to the

generic potential flow fluid with potential (4.19) in section 6.2 below.

5 Type D double copy

5.1 Weyl double copy

Now that we've obtained velocity and pressure fields that correspond to either Petrov
type D or type N, we look to build the Weyl double copy (3.15) corresponding to the
particular fluid solutions. Accordingly, we use our results for the Weyl scalars (4.1) and
the expansion of the Weyl spinor CABCD, given by (3.16). As we showed in section 4.1, the
type D constraint leaves us with constant vorticity fluid solutions. The time-independent
solution (4.10) and (4.11) takes the form

vx = -y,                    vy = x,                   P   =    2 (x2    +     y2)                (5.1)
                                                                                  .
                                                                        2

From the expression for the Weyl scalars I for arbitrary velocity fields (4.1), we find that
the solution (5.1) leaves us with

                         2  =         -i  2      +    O(  3),                                    (5.2)
                                           2rc

while all other I vanish to O( 3). Consequently, the Weyl spinor is CABCD =
62o(AoBC D).

     Using the Weyl double copy as defined in (3.15), we find the zeroth copy scalar and

single copy gauge field are, to lowest order, at O( ) for fAB and O(1) for S,

S = irc e2i,                                  fAB = ei         10          ,                     (5.3)
        3                                                      0 -1

                                          � 13 �
where  is a constant (global) phase to be interpreted shortly. Since the double copy

relation (3.15) and the vanishing of all I=2 force fAB  oAB, the matrix structure of
fAB here arises from the form of oA and B as in (B.11).

Next, we use the relation between the spacetime formalism and the spinor formalism as

reviewed in appendix A to obtain the tensor form of the field strength F � from the spinor

fAB. These relationships necessitate a vierbein for the background on which the gauge

fields live. As the perturbations about the Rindler background generate the correspondence

between the Einstein and Navier-Stokes equations, the gauge fields most naturally live on

the Rindler background as well. We will shortly see that choosing the Rindler background

also provides a straightforward interpretation of the gauge field solutions. The metric is of   JHEP08(2020)147

the form

          ds(20) = -rd 2 + 2drd + dx2 + dy2,     (5.4)

where the scalar satisfies the wave equation, (0)��(0)S = (0)S = 0. The (�0) are the
covariant derivatives with respect to (5.4). From (B.10), we obtain the vierbeins

          e(�0),0 =  -        1    r  , 0, 0  ,
          e�(0),1 =       r,

                           1                     (5.5)
                     0, -  , 0, 0 ,

                             r

          e�(0),2 = (0, 0, 1, 0),

          e�(0),3 = (0, 0, 0, 1).

Using (A.13) to obtain F � in terms of fAB, the Pauli matrices, and the vierbeins, we find
the only nonzero components are

          F r = - cos , F xy = - sin .           (5.6)

Recalling that the gauge field is in the U(1) sector of Yang-Mills, the Maxwell equations

          (0)F � = 0,         ([�0)F] = 0,       (5.7)

indeed show that the field strength (5.6) is a vacuum solution. This is to be expected,
since the fluid solutions are obtained by demanding the Einstein equations are satisfied in
vacuum, G� = 0, so we expect the single copy to follow suit. In the classical double copy,
it is possible for the spacetime to have a singularity that maps to a gauge field source, as
the point mass maps to a point charge in the Schwarzschild solution [34] when parameters
are chosen to turn off the dilaton [36, 52]. Because Rindler space is free from singularities,
no sources will be found on the gauge theory side, consistent with (5.7).

5.2 Effective electric and magnetic fields

Interpreting the single copy gauge field strength (5.6) as a Maxwell solution allows us to
discuss the electric and magnetic fields whose double copy generates the metric dual to a

                     � 14 �
constant vorticity fluid.6 These fields are defined covariantly by

                           E = F��,               B      =  1  �      F     �,                       (5.8)
                                                            2

where  is the (timelike) Killing vector  =  . For the field strength under consideration,

we find

                           E =  cos r,                B = - sin r.                                   (5.9)

We       interpret  these  fields  by  choosing  the  global   phase     to  be      =  3  ,  which  leaves  us
                                                                                        2

with a constant magnetic field pointing in the r direction, perpendicular to the x - y plane.

Under this choice of , the classical vector potential A, which constructs the magnetic field                     JHEP08(2020)147

by B =  � A, coincides with the velocity fields directly: A  v. Since the magnetic field

is unchanged when the vector potential shifts by a constant, we see that the single copy

gauge fields will similarly be unchanged when we shift the velocity by a constant.

We also compute the electromagnetic stress tensor

                                   T   =  F �F �  -   1  g     F�  F  �  ,                           (5.10)
                                                      4

finding the nonzero components

                           Tr  =     2    T rr   =      r2     T xy      =   2                       (5.11)
                                   -,                 -,                        .
                                       2                 2                   2

The associated energy with respect to the Killing vector  is given by

                                          T � � = 2r/2,                                              (5.12)

while the spatial components of the Poynting vector, from T ��, become zero.
     Physically, we can understand the fluid (5.1) as the solution inside of a slowly rotating

cylinder with its axis along the r-direction and no-slip boundary conditions at the wall,
where we have taken the radius of the cylinder to be large (with respect to all other scales
in the problem). The corresponding single copy gauge field, B = r^, matches the uniform
magnetic field along the axis of a solenoid with n turns per unit length whose current I
is proportional to /n. The axis of the solenoid is aligned with the axis of the cylinder
containing the fluid.7 The double copy mapping therefore associates the vorticity of the
fluid with the magnitude of the current sourcing the magnetic field. The field moreover has
energy dependent on the radial location r, but has vanishing Poynting vector as expected
for a pure magnetic field. In addition, we see from (5.3) that the zeroth copy S plays
a passive role in that it trivially solves the wave equation. We thus find that all of the
nontrivial information that is mapped through the double copy is contained in the field
strengths fAB or F � for the type D spacetime.

    6Note that unlike references [45] and [50], which discuss gauge and gravity solutions with vorticity, we
are discussing metrics dual to fluids with vorticity.

    7The velocity fields rotate counter-clockwise in the x - y plane. After exchanging the vorticity param-
eter with a current parameter, the resulting magnetic field then points along positive r^, consistent with
choosing  = 3/2.

                                                 � 15 �
5.3 Weyl double copy in the near horizon expansion

The hydrodynamic limit can be related to a near horizon expansion of the metric by
rescaling the metric as in (2.7) [25]. Since the full fluid solution (5.1) does not actually lie
in the hydrodynamic regime,8we repeat here the same analysis as in section 5.1, repeated
in the near horizon expansion (2.8). We again find the same results.

     Using the tetrad (C.3), we find the Weyl scalars for the near horizon metric (2.8) with
the constant vorticity fluid (5.1). The only nonzero Weyl scalar is

                             i                                  (5.13)
                     2 = 2 + O().
                                                                                                                   JHEP08(2020)147
All other Weyl scalars vanish at O(1), and have contributions from neglected pieces of the
metric at O() or higher. Following the method in section 5.1, we identify the zeroth copy
scalar and single copy gauge field spinor:

                     S = 1 ei(+2),    fAB = ei         10    .  (5.14)
                           3                           0 -1

As before, we obtain the appropriate flat space vierbien by setting the velocities and pres-
sures to zero in the full tetrad and using eq. (B.10); we find

                                     r+     r-  0 0
                                             2
                                         2

                     e(0�),a  =       -1    -1  0 0             (5.15)
                                       0     0      .

                                                1 0

                                      0 0 01

Using this flat space vierbien the gauge field strength tensor in the  expansion becomes

                     F r = - cos , F xy = - sin ,               (5.16)

which should be thought of as living on a flat Rindler background. We then identify effective

electric and magnetic fields, which are identical to the previous result (5.9) obtained in the

hydrodynamic limit:

                     E =  cos  r,           B = - sin  r.       (5.17)

6 Type N Weyl double copy

In this section we will analyze the single copy gauge fields and zeroth copy scalar fields
corresponding to the metrics dual to potential flow fluids. As we saw in section (4.2),
these potential flows are the most general solution whose dual metrics satisfy the Petrov
type N constraint. As potential flows, their velocity can be written as the gradient of a

    8The fluid solution (5.1) is only in the hydrodynamic regime (2.4) for x, y  -1 while the vorticity
satisfies   2. For either small x, y or large vorticity, the solution exits the hydrodynamic regime,
although of course it still solves Navier-Stokes. Because of this technicality, the metric (2.3) is not trustable
for small x, y. However, in the near-horizon expansion, because of the rescaling (2.7), the fluid solution
does not need to be in the hydrodynamic regime, since this expansion is rewritten explicitly in terms of
the hatted coordinates in (2.6) that are of O(1). Here we explore an explicit realization of the near-horizon
expansion, for completeness, as provided in equation (2.8).

                                    � 16 �
scalar potential, vi = i, where  satisfies Laplace's equation in R2. For convenience, we
defined z = x + iy and its conjugate z� so that we may write the Laplacian as 2 = zz�,
decomposing the scalar potential as (z, z�) = f (z) + f�(z�). The resulting Weyl scalar, 4,

is given by (4.17), and all others vanish. Therefore the Weyl double copy should satisfy

                           CABCD   =  -  2   z�2f�(z�)oAoB  oC  oD  =  1                                   (6.1)
                                         r                             S fABfCD.

6.1 Planar extensional flows

Let  us  start  with  the  simple  case  of  planar  extensional    flow,  where  (z, z�)  =  -     (z  2  +  z�2)
                                                                                                 4
                                                                                                                    JHEP08(2020)147
with  a real constant. The corresponding velocity fields are (4.21) vx = -x and vy = y.

     We can satisfy the double copy relation (6.1) by choosing

                                         e2i                   ei 1 1
                                   S= ,        fAB   =                     ,                               (6.2)
                                                                 r  11


where we again allow for a global phase . Here, since we have I=4 = 0, we have fAB 
oAoB, therefore the matrix structure in (6.2) arises from (B.11). Although we could make
another choice for S, this constant choice trivially satisfies (0)S = 0, and fAB is the only
choice which will satisfy the gauge field equations as we show below.

     As for the type D case, we specify our background spacetime by using (B.10) to find the
vierbeins corresponding to the tetrads used to compute 4, and then setting vi = P = 0.
The resulting vierbeins turn out to have the same form as (5.5). We then obtain the gauge
field strength tensor via (A.13), finding

                      F rx = - sin ,         F ry = - cos ,            F x = - 2 sin  .                    (6.3)
                                                                                      r

As in the type D case, since this field strength has no nontrivial color factor dependence,
we treat it as an effective Maxwell field; indeed it satisfies the vacuum Maxwell equations
over the Rindler background (5.4) for arbitrary .

     We obtain the electric and magnetic fields using the covariant expressions (5.8), yielding

                                      E = (0, 0, sin , - cos )                                             (6.4)

and

                                      B = (0, 0, cos , - sin ).                                            (6.5)

Again, as in the type D case, we choose  = 3/2 as a convenient parametrization; picking
another  will just result in a rotation in the x, y plane. Computing the electromagnetic
stress tensor (5.10), we find

                                   T  =  4     Tr    =      2   T rr = 1.                                  (6.6)
                                         r2 ,                ,
                                                            r

The energy becomes

                                              T � � = 1,                                                   (6.7)

                                               � 17 �
while the spatial components of the Poynting vector become

                             Si = -ri .                        (6.8)

We interpret this gauge field as the single copy field necessary to build up any fluid which
has a potential component. Since any two-dimensional vector field can be decomposed, via
the two-dimensional version of Helmholtz decomposition, we can write the velocity field as

                             vi = i + ijkj Ak,                 (6.9)

where the vector fluid potential for the two-dimensional case satisfies A = |A|(x^ � y^), and      JHEP08(2020)147
i, j, k run over the directions x and y as well as the direction x^ � y^. For the potential flows
whose gravity duals are type N, we have only the first term; that is, |A| = 0. Most of the
information in  will be carried instead by the scalar S, so the field profile (6.3) is only
building up the fluid-dual spacetime necessary to support a velocity field with a nonzero
i term.

     The nonzero Poynting vector (6.8) indicates the dissipative nature of these flows. The
gravitational dual is carrying energy away from the r = rc hypersurface, towards the null
horizon, satisfying the infalling Rindler boundary conditions that underlie the derivation
of the fluid-dual metric (2.3). The same flow of energy towards the null horizon arises in
the Poynting vector aligned in the -r^ direction.

6.2 General potential flows

As we will show, the analysis in section 6.1 will work very similarly for a potential flow
 = f (z) + f�(z�) with generic holomorphic function f (z).

Since (0) on the Rindler background (5.4) will give zero when acting on any function

which is a sum of holomorphic and antiholomorphic terms independent of  and r, we can

satisfy the type N Weyl double copy relation (6.1) for the metric dual to a generic potential

flow with

                     e2i                 ei     11
           S = - z�2f�(z�) ,  fAB     =         11          .  (6.10)
                                           r

It is now the case that (0)S = 0 is nontrivially satisfied, and the resulting gauge field
strength is unchanged from the analysis for the planar extensional flow. Thus for all
potential flow fluids, such as those in table 1, the Weyl double copy admits the same single
copy gauge field as in the extensional flow, (6.3). The information for a potential flow on the
fluid side resides entirely in the potential ; similarly, under the double copy prescription,
we find that the information from the potential resides entirely in the zeroth copy scalar
field S, whereas the single copy gauge field is the same for all potential flows.

     Since the single copy field profile is again (6.3), our interpretation of this field as
building the fluid-dual spacetime for fluids with nonzero potential terms holds again. We
do note that the fields (6.4) and (6.5) are constant; we expect that inclusion of higher order
terms in the expansion could alter this result, since here we are really considering only a
hydrodynamic expansion in small around the original r = rc cutoff surface.

                              � 18 �
7 Discussion                                                                                     JHEP08(2020)147

We have used the Weyl double copy prescription to find the single copy gauge fields and
zeroth copy scalar fields arising from two classes of fluid-dual metrics. The first class,
fluids with constant vorticity, maps to spacetime metrics with Petrov type D. The second
class, potential flow fluids, maps to spacetime metrics with Petrov type N. For the type D
spacetimes dual to fluids with constant vorticity, we find an (effectively abelian) dual gauge
field with vanishing Poynting vector. For the type N spacetimes dual to potential flows, we
find a gauge field whose Poynting vector points in towards the Rindler horizon, indicating
that the dissipation in these fluids maps in the spacetime to energy flowing across the
horizon due to the infalling boundary conditions there.

     We also saw that the single and zeroth copy fields mapping to the two sets of fluid-dual
metric classes store their information differently. In the type D case, the vector potential
for the magnetic field corresponds to the fluid velocity profile, while the zeroth-copy scalar
field is just a constant; only the single-copy gauge field is carrying nontrivial information
about the fluid. For type N spacetimes, the story is in some sense opposite: the nontrivial
components of the fluid are entirely due to the potential, which shows up only in the
zeroth-copy scalar field. Here, the gauge field is fixed and appears to be the field necessary
to build the fluid-dual spacetime for all potential flow fluids.

     In fact, the two fluid classes we have studied fall into two simple classes under the
Helmholtz decomposition, which rewrites the fluid vector field in terms of its rotational
component and its irrotational or potential component, as in (6.9). The constant vorticity
solutions which map to type D spacetimes have  = 0 while the potential flow solutions that
map to type N spacetimes have A = 0. Under the double copy prescription, solutions with
nonzero A map to a nontrivial gauge field whose behavior depends on the fluid velocity,
but to a constant (trivial) zeroth copy scalar. Similarly, solutions with nonzero  all map
to the same gauge field (6.3), so instead the zeroth copy scalar carries the fluid information:
it is proportional to the second derivative of the fluid potential as in (6.10). Consequently,
we propose that any fluid-dual metric may be mapped to a single copy gauge field and
zeroth copy scalar, each of which is a sum of the corresponding pieces from the rotational
and irrotational components in the Helmholtz decomposition. We hope to explore this idea
in future work.

     We should note throughout that we work only to the lowest order in a perturbative
expansion (mainly the hydrodynamic expansion). A more complete treatment may require
understanding of the double copy prescription beyond a linear order; all double Kerr-Schild
prescriptions are essentially linear due to the linearization of the equations of motion in
those coordinates. The Weyl double copy itself is not linear in nature, but is unclear how it
might relate to more advanced treatments that would go beyond a perturbative expansion
as in [38], such as the convolution prescription in [36, 52]. Further development of this
convolution prescription to include algebraically special spacetimes would be of interest.

     The double-copy treatment in the fluid-gravity duality context may also be amenable
to analysis using solution generating techniques. For example, the Ehler's transformations
as implemented in [81] for fluids and further studied in [82, 83] in the context of the double

                                                       � 19 �
copy could allow access to a larger set of double-copy treatments for fluid-dual spacetimes.        JHEP08(2020)147
Indeed, such an analysis could shed light on the nature of single and zeroth copies for such
spacetimes.

     Since fluid-gravity duality itself can be understood from an AdS-CFT perspective
(including the cutoff-prescription formulation, whose relationship to AdS-CFT was first
understood in [26]), we hope the mapping here from fluid solutions to gravities and then
through the double copy prescription to gauge theories (and scalars) can provide perspective
both regarding the relationship of the double copy prescription to AdS-CFT duality, and
also the understanding of fluid-gravity duality itself, including a deeper understanding of
fluids as in [84].

Acknowledgments

We would like to thank J.J. Carrasco, Damien Easson, and Andres Luna for useful and
enlightening conversations while this work was in progress. This work is supported by the
U.S. Department of Energy under grant number DE-SC0019470.

A Spinor formalism

In our notation, spacetime indices are given by {�, , , . . .}, frame indices by {a, b, c, . . .}
and the spinor indices as {A, B, C, . . .} with their conjugates {A, B , C , . . .}. The essential

objects that translate between the spinor and tensor formalisms are the Pauli 4-vectors

           Aa A     =   1    1,   AA ,            = (x, y, z).              (A.1)
                          2

The  are the standard SU(2) generators,

                    01                0 -i                      10          (A.2)
           x = 1 0 ,         y = i 0 ,                 z = 0 -1 .

     A spacetime vector is obtained from a frame vector by V� = e�aVa, where the e�a
are vierbeins that construct the full metric as g� = e�aebab. Here, ab = ab =

diag(-1, 1, 1, 1). The frame indices are raised and lowered with the diagonal Minkowski

space ab, while spinor indices are raised and lowered with a Levi-Civita symbol, which we
define as

                        AB = -AB =               01    .                    (A.3)
                                                 -1 0

A vector can be written in spinor indices or in frame indices using (A.1);

           VAA = VaAa A ,                        Va = aAA V AA ,            (A.4)

where aAA = abAb A and V AA = ABVBB B A . The (inverse) vierbein constructs the Pauli
4-vector in spacetime indices A�A = e�aAa A which, with its inverse �AA = g� ABB B B A ,

satisfies

                    A�A AA = �,            A�A �BB = AB AB .                (A.5)

                                         � 20 �
Any tensor can be written as its spinor counterpart using the index doubling procedure.
The Weyl tensor W� becomes

W�  WAABB CC DD = CABCDAB C D + C�AB C D AB CD,                                    (A.6)

where the CABCD and C�AB C D are symmetric in their indices and related by complex
conjugation. The object9

A�B = A[�C �] C C CB ,  with     ��AA = e�a�aAA,                  �aAA = 1 1, - AA (A.7)
                                                                               2

serves to directly obtain the spinor form of a given tensor. For the Weyl spinor,                 JHEP08(2020)147

                        CABCD       =  1    W�     A�B     CD  .                   (A.8)
                                       4

For the field strength tensor F�, we write

                        F�  FAABB = fABAB + f�AB AB,                               (A.9)

where the spinor field strength can be computed as

                              fAB   =       1  F�  A(0B)�  ,                       (A.10)
                                            2

which is also symmetric in its spinor indices. In the above expression, the zero superscript

is meant to remind that since F� lives on flat space, the vierbein that's used to construct
the A�A in (A.10) is that which constructs the flat space,

A(0A)� = e(0a)�Aa A ,                          e(�0)ae(0)bab = g�(0).              (A.11)

For example in section 5.1, g�(0) is Rindler space (5.4) and the e(�0)a are (5.5). The vierbeins
that are used to build A�B in (A.8) instead construct the full spacetime. For conciseness
we will drop the 0-superscript in what follows.

     To invert (A.10), it is tedious though straightforward to show

F �                        i  �                �AD fAB BD�D D,
                        -  2        F       =                                      (A.12)
                                -g

where g = detg�. F � can be obtained directly by adding the complex conjugate of the
right hand side in (A.12), yielding

F � = 1                 �AD fAB BD�D D + �ADf�AB B D �DD               .           (A.13)
         2

For the second term in (A.13), the  denotes standard complex conjugation, i.e.

                        AaA   =   1    1, x, -y, z               .                 (A.14)

                                                              A A
                                   2

9Brackets denote antisymmetrization, and we use the convention [A, B] = AB - BA.

                                       � 21 �
B Newman-Penrose formalism

We now briefly describe the Newman-Penrose (NP) formalism which we use to compute
geometric quantities of interest such as the Weyl spinor. The NP formalism utilizes spinor
language in order to simplify computations ([72�74]). There primarily are four sets of
objects of interest for us in the NP formalism. Briefly, one rewrites the metric in terms of
a tetrad set, this tetrad set then is used to compute spin coefficients,10

g� = -l(�n) + m(�m).                                                     (B.1)

Bilinears of the spin coefficients then give the set of Weyl scalars {0, 1, 2, 3, 4, },                    JHEP08(2020)147

0 = D -  - ( + � + 3 + �) + ( - � + � + 3)                               (B.2)
1 = D -  - ( + ) - (� - �) + (� + ) + (� - �)
2 = D� -  + ( + � - �)� + (� -  - �) +  -  - R/12
3 = � -  + ( + ) - ( + ) + (� - ��) + (� - �)
4 = � -  - (� + �� + 3 - �) + (3 + � +  - �),

where the following are directional derivatives,

D = l��,  = n��,  = m��, � = m� ��.                                      (B.3)

Finally in terms of these Weyl scalars one can rewrite the Weyl Spinor.

CABCD = 0ABC D - 41o(ABC D) + 62o(AoBC D)                                (B.4)
              - 43o(AoBoC D) + 4oAoBoC oD

Finally in order to test the algebraic speciality of the spacetime we compute tetrad invariant
combinations of the Weyl scalars; the equation below is equivalent to (4.2) in the main text
as included here for completeness:

 I  04 - 413 + 322,                                                      (B.5)

       4 3 2
J  3 2 1 ,

       2 1 0

K  142 - 3432 + 233 ,

L  24 - 32,

N  12L2 - 42I.

The spinors oA, A are related to the frame metric choice one makes. We will make explicit
this connection now. The metric written in terms of vierbiens has the form,

g� = e�aebab where ab = diag{-1, 1, 1, 1}.                               (B.6)

  10We utilize the method outlined in [85] to obtain spin-coefficients, this approach comes with the com-
putational benefit of replacing certain covariant derivatives with partial derivatives.

                            � 22 �
The frame metric ab can itself be written as outer products of a tetrad set, this will allow
us to make identifications between the vierbiens and the tetrad set.

                                   ab = -^l(an^b) + m^ (am^ b)                                         (B.7)
                             = g� = e�aeb(-^l(an^b) + m^ (am^ b))
                             = g� = -l(�n) + m(�m)

Where in the last step we have made the identifications,

                 e�a^la = l� e�an^a = n� e�am^ a = m� e�am^ a = m�                                     (B.8)  JHEP08(2020)147

Now the tetrad set that reproduces the Minkowski frame metric is,

                                       ^la  =     1  {1, -1, 0, 0}

                                                 2

                                                 1
                                       n^a  =     {1, 1, 0, 0}
                                                   2
                                                                                                       (B.9)
                                                 1
                                  m^ a      =     {0, 0, i, 1}
                                                   2

                                  m^ a      =     1  {0, 0, -i, 1}

                                                 2

The expression B.8 can be inverted to go from tetrads to vierbiens via the following,

                 e�0         1                            e�1      1
                      =           (l�  +    n�)                =       (l�  -  n�)
                               2                                    2
                                                                                          (B.10)
                             i                                     1
                 e�2  =           (m� �  -  m�)           e�3  =       (m�  +  m� �)
                               2                                    2

In order to obtain the spinors we write these four vectors in an SL(2,C) represen-

tation by contracting them with relevant  matrices. Note in our conventions we have

Aa A  = {I, },   while the curved space equivalents can be obtained                   by  contracting  these
with  vierbiens  (i.e. A�A = e�a Aa A ). For eg., for {oA, A} we have,

                             oAoA           ^la  Aa A  =  1    11
                                                          2    11

                                                          1
                                         =       oA =      {1, 1}
                                                            2
                                                                                          (B.11)

                                AA          n^a Aa A   =  1     1 -1
                                                          2    -1 1

                                                          1
                                         =       A =       {1, -1}
                                                            2

Further noting that one can transform from SL(2,C) left to right by complex conjuga-

tion we use the convention,

                                            (oA)  oA                                      (B.12)

                                                 � 23 �
This further verifies that the two remaining contractions will hold the following relations
correctly,

                                  m^ a Aa A  =  1      11           = AoA
                                                2     -1 -1

                                                                                                       (B.13)

                                  m^ a Aa A  =  1     1 -1      = oAA
                                                2     1 -1

C Tetrads in the hydrodynamic and the near horizon expansions

In the hydrodynamic limit as discussed in section 2 in the body of the paper, the velocities                       JHEP08(2020)147
and the pressure must satisfy the scaling (2.4), where i runs over x and y, the spacelike
coordinates on the cutoff surface r = rc. We can make this scaling of derivatives explicit
by making the following identifications to simplify keeping track of the orders:

                        vi  vi,  vi( 2, xi), P  P  P ( 2, xi).                                         (C.1)

With these identifications having been established we can now write out the tetrad set we

use for the computation in the hydrodynamic expansion:

                 r
    l� = -  , 0, 0, 0
                 2

          +2          r  4rcP     +  (3r  -  2rc)     vx2,  + vy2,       r   vx2, + vy2,  , 0, 0  + O( 3);

                 -                     4 2rc2                        ,       2 2rc2

                    r2
    n� =     -       ,    , 0, 0
                    2    r

          +2     - (r - 2rc)      4rcP    +r    vx2,  + vy2,        , 0, 0, 0 + O( 3);

                                     4rc2 2r

                        i1
    m� =     0, 0, -  , 
                       22

          + 2 0, 0, i(r -rc)vx2, , i(r - rc)vy,(2vx, + ivy, ) + O( 3);
                         2 2rc2                       2 2rc2

    m� � = m�.                                                                                         (C.2)

    The mathematical equivalence between the hydrodynamic expansion and the near

horizon expansion involves a rescaling of the metric as was shown in [25]. In computations

we  present  in  the    near  horizon  expansion,     we    utilize  the    expansion     parameter          2  .

                                                                                                            rc

Because the  expansion has reorganized the series, we write below the tetrad set used

for the near horizon computation, in particular for the type D or rotational velocity and

pressure profiles in (5.1). Note that in this expansion, the coordinates we work with are

rescaled to be really x^ and y^; for clarity in the expressions below we have dropped the hats.

    The near horizon tetrad we use for the fluid metric dual to (5.1) is

       1                      3r2 x2 + y2                     + 2         2 x2 + y2
l� =   , 0, 0, 0        +                        , 0, 0, 0           0, -  , 0, 0
          2                          42                                      22

      + 3    9r r2 - 4 6 x2 + y2 3 r4 x2 + y2 2                              + O(4);
                                             ,-                      , 0, 0
                         64 2                               22

                                                   � 24 �
n� = -1     r , 0, 0, 0 +                ((r - 2)r + 2)2 x2 + y2  ry rx
              2                       -                                  , - 2, -  , 
                                                      22                                 22

+           3r4      x2 + y2    2 r2         x2 + y2      (r - 1)   4qx  +     (r  -  2)y3  x2 + y2  ,
                                 ,                    ,-                           
                     42                      2                                 22

            (r - 1)     (r - 2)x3        x2 + y2      - 4qy

                                22

+ 2 0,  2(r - 2)ygr(2x) - 2(r - 2)xgr(2y) + 3(r - 1)3 x2 + y2 2 ,
                                              22

             4(r-2)ygx(2x) +(r-1) x2 +y2 12rqx +(r-1)y3 4(r+1)x2 +(5r+2)y2 ,                                   JHEP08(2020)147
                                                           82

                     4(r-2)xgy(2y) +(r-1)         x2 +y2      (r - 1)x3        (5r+2)x2 +6ry2  -12rqy
            -                                                 
                                                              82

            + O(3);

            (r - 2)(x - iy) i 1
m� = -                          , 0,  , 
                22                     22

            3r23(x - iy) x2 + y2 (x - iy) (r - 1)y2(x - iy)
+                                            , ,                                      ,
                            82                        2             22

                (r - 1)x2(x - iy)
            -                
                            22

+ 2         0,  4igr(2x)  +  4gr(2y)  +  (r  - 2)3(x  -  iy)2(x  +  iy)  ,

                                             42

            4igx(2x) + (r - 1)2y4            2x3 - ix2y + 2xy2 - iy3        ,

                                             82

            4gy(2y)  -  (r  -  1)2x24        x2 + y2     + O(3);

                               82

m� � = m�.                                                                                              (C.3)

In the above expressions, the functions qi and gi(j2) refer to higher order terms necessary in
the  expansion to ensure that Einstein's equations are appropriately satisfied, as in [25].
These functions do not appear in the lowest order Petrov invariants. Note that this tetrad
has been chosen to ensure that 2 is the only nonzero I ; the invariants (B.5) do not
change under tetrad rotations, but the explicit form of the CABCD in terms of  and o does
change. For simplicity, we thus choose a tetrad which preserves (5.2).

Open Access. This article is distributed under the terms of the Creative Commons
Attribution License (CC-BY 4.0), which permits any use, distribution and reproduction in
any medium, provided the original author(s) and source are credited.

References

 [1] T. Damour, Black hole Eddy currents, Phys. Rev. D 18 (1978) 3598 [INSPIRE].

                                                      � 25 �
 [2] T. Damour, Quelques proprietes mecaniques, electromagnetiques, thermodynamiques et         JHEP08(2020)147
      quantiques des trous noir, Ph.D. thesis, University of Paris, Paris U.S.A. (1979),
      http://pagesperso.ihes.fr/damour/Articles/.

 [3] K.S. Thorne, R. Price and D. Macdonald, Black holes: the membrane paradigm, Yale
      University Press, U.S.A. (1986).

 [4] M. Parikh and F. Wilczek, An action for black hole membranes, Phys. Rev. D 58 (1998)
      064011 [gr-qc/9712077] [INSPIRE].

 [5] C. Eling and Y. Oz, Relativistic CFT hydrodynamics from the membrane paradigm, JHEP
      02 (2010) 069 [arXiv:0906.4999] [INSPIRE].

 [6] C. Eling, I. Fouxon and Y. Oz, The incompressible Navier-Stokes equations from membrane
      dynamics, Phys. Lett. B 680 (2009) 496 [arXiv:0905.3638] [INSPIRE].

 [7] E. Gourgoulhon and J.L. Jaramillo, A 3 + 1 perspective on null hypersurfaces and isolated
      horizons, Phys. Rept. 423 (2006) 159 [gr-qc/0503113] [INSPIRE].

 [8] E. Gourgoulhon, A generalized Damour-Navier-Stokes equation applied to trapping horizons,
      Phys. Rev. D 72 (2005) 104007 [gr-qc/0508003] [INSPIRE].

 [9] E. Gourgoulhon and J.L. Jaramillo, New theoretical approaches to black holes, New Astron.
      Rev. 51 (2008) 791 [arXiv:0803.2944] [INSPIRE].

[10] G. Policastro, D.T. Son and A.O. Starinets, The Shear viscosity of strongly coupled N = 4
      supersymmetric Yang-Mills plasma, Phys. Rev. Lett. 87 (2001) 081601 [hep-th/0104066]
      [INSPIRE].

[11] G. Policastro, D.T. Son and A.O. Starinets, From AdS/CFT correspondence to
      hydrodynamics, JHEP 09 (2002) 043 [hep-th/0205052] [INSPIRE].

[12] P. Kovtun, D.T. Son and A.O. Starinets, Holography and hydrodynamics: diffusion on
      stretched horizons, JHEP 10 (2003) 064 [hep-th/0309213] [INSPIRE].

[13] P. Kovtun, D.T. Son and A.O. Starinets, Viscosity in strongly interacting quantum field
      theories from black hole physics, Phys. Rev. Lett. 94 (2005) 111601 [hep-th/0405231]
      [INSPIRE].

[14] D.T. Son and A.O. Starinets, Viscosity, black holes, and quantum field theory, Ann. Rev.
      Nucl. Part. Sci. 57 (2007) 95 [arXiv:0704.0240] [INSPIRE].

[15] S. Bhattacharyya, S. Minwalla and S.R. Wadia, The incompressible non-relativistic
      Navier-Stokes equation from gravity, JHEP 08 (2009) 059 [arXiv:0810.1545] [INSPIRE].

[16] N. Iqbal and H. Liu, Universality of the hydrodynamic limit in AdS/CFT and the membrane
      paradigm, Phys. Rev. D 79 (2009) 025023 [arXiv:0809.3808] [INSPIRE].

[17] Y. Oz and M. Rabinovich, The Penrose inequality and the fluid/gravity correspondence,
      JHEP 02 (2011) 070 [arXiv:1011.5895] [INSPIRE].

[18] T. Faulkner, H. Liu and M. Rangamani, Integrating out geometry: holographic wilsonian RG
      and the membrane paradigm, JHEP 08 (2011) 051 [arXiv:1010.4036] [INSPIRE].

[19] C. Eling and Y. Oz, Holographic vorticity in the fluid/gravity correspondence, JHEP 11
      (2013) 079 [arXiv:1308.1651] [INSPIRE].

[20] T. Damour and M. Lilley, String theory, gravity and experiment, Les Houches 87 (2008) 371
      [arXiv:0802.4169] [INSPIRE].

                                                       � 26 �
[21] M. Rangamani, Gravity and hydrodynamics: lectures on the fluid-gravity correspondence,           JHEP08(2020)147
      Class. Quant. Grav. 26 (2009) 224003 [arXiv:0905.4352] [INSPIRE].

[22] T. Padmanabhan, Thermodynamical aspects of gravity: new insights, Rept. Prog. Phys. 73
      (2010) 046901 [arXiv:0911.5004] [INSPIRE].

[23] V.E. Hubeny, S. Minwalla and M. Rangamani, The fluid/gravity correspondence, in the
      proceedings of the Theoretical Advanced Study Institute in elementary particle physics: string
      theory and its applications: from meV to the Planck Scale, June 1�25, Boulder, U.S.A.
      (2012), arXiv:1107.5780 [INSPIRE].

[24] I. Bredberg, C. Keeler, V. Lysov and A. Strominger, Wilsonian approach to fluid/gravity
      duality, JHEP 03 (2011) 141 [arXiv:1006.1902] [INSPIRE].

[25] I. Bredberg, C. Keeler, V. Lysov and A. Strominger, From Navier-Stokes to Einstein, JHEP
      07 (2012) 146 [arXiv:1101.2451] [INSPIRE].

[26] D. Brattan, J. Camps, R. Loganayagam and M. Rangamani, CFT dual of the AdS Dirichlet
      problem: fluid/gravity on cut-off surfaces, JHEP 12 (2011) 090 [arXiv:1106.2577]
      [INSPIRE].

[27] G. Compere, P. McFadden, K. Skenderis and M. Taylor, The holographic fluid dual to
      vacuum Einstein gravity, JHEP 07 (2011) 050 [arXiv:1103.3022] [INSPIRE].

[28] G. Compere, P. McFadden, K. Skenderis and M. Taylor, The relativistic fluid dual to vacuum
      Einstein gravity, JHEP 03 (2012) 076 [arXiv:1201.2678] [INSPIRE].

[29] M. Taylor, TT deformations in general dimensions, arXiv:1805.10287 [INSPIRE].
[30] V. Lysov and A. Strominger, From Petrov-Einstein to Navier-Stokes, arXiv:1104.5502

      [INSPIRE].

[31] N. Pinzani-Fokeeva and M. Taylor, Towards a general fluid/gravity correspondence, Phys.
      Rev. D 91 (2015) 044001 [arXiv:1401.5975] [INSPIRE].

[32] S. De, S. Dey and B.R. Majhi, Effective metric in fluid-gravity duality through parallel
      transport: a proposal, Phys. Rev. D 99 (2019) 124024 [arXiv:1901.05735] [INSPIRE].

[33] S. Dey, S. De and B. Ranjan Majhi, Gravity dual of Navier-Stokes equation in a rotating
      frame through parallel transport, arXiv:2002.06801 [INSPIRE].

[34] R. Monteiro, D. O'Connell and C.D. White, Black holes and the double copy, JHEP 12
      (2014) 056 [arXiv:1410.0239] [INSPIRE].

[35] Z. Bern, J.J. Carrasco, M. Chiodaroli, H. Johansson and R. Roiban, The duality between
      color and kinematics and its applications, arXiv:1909.01358 [INSPIRE].

[36] A. Luna, S. Nagy and C. White, The convolutional double copy: a case study with a point,
      arXiv:2004.11254 [INSPIRE].

[37] A. Luna, R. Monteiro, D. O'Connell and C.D. White, The classical double copy for
      Taub-NUT spacetime, Phys. Lett. B 750 (2015) 272 [arXiv:1507.01869] [INSPIRE].

[38] A. Luna et al., Perturbative spacetimes from Yang-Mills theory, JHEP 04 (2017) 069
      [arXiv:1611.07508] [INSPIRE].

[39] R. Monteiro, I. Nicholson and D. O'Connell, Spinor-helicity and the algebraic classification of
      higher-dimensional spacetimes, Class. Quant. Grav. 36 (2019) 065006 [arXiv:1809.03906]
      [INSPIRE].

                                                       � 27 �
[40] L. Alfonsi, C.D. White and S. Wikeley, Topology and Wilson lines: global aspects of the        JHEP08(2020)147
      double copy, JHEP 07 (2020) 091 [arXiv:2004.07181] [INSPIRE].

[41] A.K. Ridgway and M.B. Wise, Static spherically symmetric Kerr-Schild metrics and
      implications for the classical double copy, Phys. Rev. D 94 (2016) 044023
      [arXiv:1512.02243] [INSPIRE].

[42] T. Adamo, E. Casali, L. Mason and S. Nekovar, Scattering on plane waves and the double
      copy, Class. Quant. Grav. 35 (2018) 015004 [arXiv:1706.08925] [INSPIRE].

[43] N. Bahjat-Abbas, A. Luna and C.D. White, The Kerr-Schild double copy in curved
      spacetime, JHEP 12 (2017) 004 [arXiv:1710.01953] [INSPIRE].

[44] M. Carrillo-Gonz�alez, R. Penco and M. Trodden, The classical double copy in maximally
      symmetric spacetimes, JHEP 04 (2018) 028 [arXiv:1711.01296] [INSPIRE].

[45] A. Ilderton, Screw-symmetric gravitational waves: a double copy of the vortex, Phys. Lett. B
      782 (2018) 22 [arXiv:1804.07290] [INSPIRE].

[46] M. Gurses and B. Tekin, Classical double copy: Kerr-Schild-Kundt metrics from Yang-Mills
      theory, Phys. Rev. D 98 (2018) 126017 [arXiv:1810.03411] [INSPIRE].

[47] M. Carrillo Gonza�lez, B. Melcher, K. Ratliff, S. Watson and C.D. White, The classical double
      copy in three spacetime dimensions, JHEP 07 (2019) 167 [arXiv:1904.11001] [INSPIRE].

[48] K. Lee, Kerr-Schild double field theory and classical double copy, JHEP 10 (2018) 027
      [arXiv:1807.08443] [INSPIRE].

[49] I. Bah, R. Dempsey and P. Weck, Kerr-Schild double copy and complex worldlines, JHEP 02
      (2020) 180 [arXiv:1910.04197] [INSPIRE].

[50] K. Andrzejewski and S. Prencel, From polarized gravitational waves to analytically solvable
      electromagnetic beams, Phys. Rev. D 100 (2019) 045006 [arXiv:1901.05255] [INSPIRE].

[51] W.D. Goldberger and J. Li, Strings, extended objects, and the classical double copy, JHEP
      02 (2020) 092 [arXiv:1912.01650] [INSPIRE].

[52] K. Kim, K. Lee, R. Monteiro, I. Nicholson and D. Peinador Veiga, The classical double copy
      of a point charge, JHEP 02 (2020) 046 [arXiv:1912.02177] [INSPIRE].

[53] N. Bahjat-Abbas, R. Stark-Mucha~o and C.D. White, Monopoles, shockwaves and the
      classical double copy, JHEP 04 (2020) 102 [arXiv:2001.09918] [INSPIRE].

[54] A. Luna, R. Monteiro, I. Nicholson and D. O'Connell, Type D spacetimes and the Weyl
      double copy, Class. Quant. Grav. 36 (2019) 065003 [arXiv:1810.08183] [INSPIRE].

[55] W.D. Goldberger, S.G. Prabhu and J.O. Thompson, Classical gluon and graviton radiation
      from the bi-adjoint scalar double copy, Phys. Rev. D 96 (2017) 065009 [arXiv:1705.09263]
      [INSPIRE].

[56] A. Luna, I. Nicholson, D. O'Connell and C.D. White, Inelastic black hole scattering from
      charged scalar amplitudes, JHEP 03 (2018) 044 [arXiv:1711.03901] [INSPIRE].

[57] W.D. Goldberger and A.K. Ridgway, Bound states and the classical double copy, Phys. Rev.
      D 97 (2018) 085019 [arXiv:1711.09493] [INSPIRE].

[58] C.-H. Shen, Gravitational radiation from color-kinematics duality, JHEP 11 (2018) 162
      [arXiv:1806.07388] [INSPIRE].

                                                       � 28 �
[59] C. Cheung, I.Z. Rothstein and M.P. Solon, From scattering amplitudes to classical potentials  JHEP08(2020)147
      in the post-Minkowskian expansion, Phys. Rev. Lett. 121 (2018) 251101 [arXiv:1808.02489]
      [INSPIRE].

[60] D.A. Kosower, B. Maybee and D. O'Connell, Amplitudes, observables, and classical
      scattering, JHEP 02 (2019) 137 [arXiv:1811.10950] [INSPIRE].

[61] Z. Bern, C. Cheung, R. Roiban, C.-H. Shen, M.P. Solon and M. Zeng, Scattering amplitudes
      and the conservative Hamiltonian for binary systems at third post-Minkowskian order, Phys.
      Rev. Lett. 122 (2019) 201603 [arXiv:1901.04424] [INSPIRE].

[62] A. Antonelli, A. Buonanno, J. Steinhoff, M. van de Meent and J. Vines, Energetics of
      two-body Hamiltonians in post-Minkowskian gravity, Phys. Rev. D 99 (2019) 104004
      [arXiv:1901.07102] [INSPIRE].

[63] Z. Bern, C. Cheung, R. Roiban, C.-H. Shen, M.P. Solon and M. Zeng, Black hole binary
      dynamics from the double copy and effective theory, JHEP 10 (2019) 206
      [arXiv:1908.01493] [INSPIRE].

[64] G. Ka�lin and R.A. Porto, From boundary data to bound states, JHEP 01 (2020) 072
      [arXiv:1910.03008] [INSPIRE].

[65] R.G. Leigh, A.C. Petkou and P. Petropoulos, Holographic three-dimensional fluids with
      nontrivial vorticity, Phys. Rev. D 85 (2012) 086010 [arXiv:1108.1393] [INSPIRE].

[66] R.G. Leigh, A.C. Petkou and P. Petropoulos, Holographic fluids with vorticity and analogue
      gravity, JHEP 11 (2012) 121 [arXiv:1205.6140] [INSPIRE].

[67] Z. Bern, J.J.M. Carrasco and H. Johansson, New relations for gauge-theory amplitudes, Phys.
      Rev. D 78 (2008) 085011 [arXiv:0805.3993] [INSPIRE].

[68] A. Luna, R. Monteiro, I. Nicholson, D. O'Connell and C.D. White, The double copy:
      bremsstrahlung and accelerating black holes, JHEP 06 (2016) 023 [arXiv:1603.05737]
      [INSPIRE].

[69] W.D. Goldberger and A.K. Ridgway, Radiation and the classical double copy for color
      charges, Phys. Rev. D 95 (2017) 125010 [arXiv:1611.03493] [INSPIRE].

[70] D.S. Berman, E. Chac�on, A. Luna and C.D. White, The self-dual classical double copy, and
      the Eguchi-Hanson instanton, JHEP 01 (2019) 107 [arXiv:1809.04063] [INSPIRE].

[71] A.P.V. and A. Manu, Classical double copy from Color Kinematics duality: A proof in the
      soft limit, Phys. Rev. D 101 (2020) 046014 [arXiv:1907.10021] [INSPIRE].

[72] R. Penrose and W. Rindler, Spinors and space-time, Cambridge Monographs on
      Mathematical Physics, Cambridge University Press, Cambridge U.K. (2011) [INSPIRE].

[73] R. Penrose and W. Rindler, Spinors and space-time. Volume 2: spinor and twistor methods
      in space-time geometry, Cambridge Monographs on Mathematical Physics, Cambridge
      University Press, Cambridge U.K. (1988) [INSPIRE].

[74] H. Stephani, D. Kramer, M.A.H. MacCallum, C. Hoenselaers and E. Herlt, Exact solutions
      of Einstein's field equations, Cambridge Monographs on Mathematical Physics, Cambridge
      University Press, Cambridge U.K. (2003) [INSPIRE].

[75] J.F. Plebanski and M. Demianski, Rotating, charged, and uniformly accelerating mass in
      general relativity, Annals Phys. 98 (1976) 98 [INSPIRE].

                                                       � 29 �
[76] J.B. Griffiths and J. Podolsky, A new look at the Plebanski-Demianski family of solutions,       JHEP08(2020)147
      Int. J. Mod. Phys. D 15 (2006) 335 [gr-qc/0511091] [INSPIRE].

[77] J. Podolsky, O. Hruska and J.B. Griffiths, Non-expanding Pleban�ski-Demian�ski space-times,
      Class. Quant. Grav. 35 (2018) 165011 [arXiv:1804.01519] [INSPIRE].

[78] R.-G. Cai, L. Li, Q. Yang and Y.-L. Zhang, Petrov type-I condition and dual fluid dynamics,
      JHEP 04 (2013) 118 [arXiv:1302.2016] [INSPIRE].

[79] S. Grozdanov, P.K. Kovtun, A.O. Starinets and P. Tadi�c, Convergence of the gradient
      expansion in hydrodynamics, Phys. Rev. Lett. 122 (2019) 251601 [arXiv:1904.01018]
      [INSPIRE].

[80] H. Barnes, K. John Fletcher Hutton, J. Hutton and K. Walters, An introduction to rheology,
      Rheology Series, Elsevier Science, The Netherlands (1989).

[81] J. Berkeley and D.S. Berman, The Navier-Stokes equation and solution generating
      symmetries from holography, JHEP 04 (2013) 092 [arXiv:1211.1983] [INSPIRE].

[82] R. Alawadhi, D.S. Berman, B. Spence and D. Peinador Veiga, S-duality and the double copy,
      JHEP 03 (2020) 059 [arXiv:1911.06797] [INSPIRE].

[83] Y.-T. Huang, U. Kol and D. O'Connell, The double copy of electric-magnetic duality, Phys.
      Rev. D 102 (2020) 046005 [arXiv:1911.06318] [INSPIRE].

[84] F.M. Haehl, R. Loganayagam and M. Rangamani, The fluid manifesto: emergent symmetries,
      hydrodynamics, and black holes, JHEP 01 (2016) 184 [arXiv:1510.02494] [INSPIRE].

[85] W.J. Cocke, Table for constructing the spin coefficients in general relativity, Phys. Rev. D 40
      (1989) 650.

                                                       � 30 �
