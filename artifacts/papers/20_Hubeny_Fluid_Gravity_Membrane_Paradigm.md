# Hubeny Fluid Gravity Membrane Paradigm

**Source:** `20_Hubeny_Fluid_Gravity_Membrane_Paradigm.pdf`

---

The fluid/gravity correspondence: a new perspective on
                       the membrane paradigm

                                     Veronika E Hubeny

  To cite this version:

Veronika E Hubeny. The fluid/gravity correspondence: a new perspective on the membrane paradigm.
Classical and Quantum Gravity, 2011, 28 (11), pp.114007. 10.1088/0264-9381/28/11/114007. hal-
00705158

         HAL Id: hal-00705158
https://hal.science/hal-00705158v1

                 Submitted on 7 Jun 2012

    HAL is a multi-disciplinary open access              L'archive ouverte pluridisciplinaire HAL, est
archive for the deposit and dissemination of sci-    destin�e au d�p�t et � la diffusion de documents
entific research documents, whether they are pub-    scientifiques de niveau recherche, publi�s ou non,
lished or not. The documents may come from           �manant des �tablissements d'enseignement et de
teaching and research institutions in France or      recherche fran�ais ou �trangers, des laboratoires
abroad, or from public or private research centers.  publics ou priv�s.
                                                                                           DCPT-10/65

           The Fluid/Gravity Correspondence:

           a new perspective on the Membrane Paradigm

                                          Veronika E. Hubeny,

               Centre for Particle Theory & Department of Mathematical Sciences,
             Science Laboratories, South Road, Durham DH1 3LE, United Kingdom.

                                   February 8, 2011

                                                      Abstract
        This talk gives an overview of the recently-formulated Fluid/Gravity correspon-
    dence, which was developed in the context of gauge/gravity duality. Mathematically,
    it posits that Einstein's equations (with negative cosmological constant) in d + 1 di-
    mensions capture the (generalized) Navier-Stokes' equations in d dimensions. Given
    an arbitrary fluid dynamical solution, we can systematically construct a correspond-
    ing asymptotically AdS black hole spacetime with a regular horizon whose properties
    mimic that of the fluid flow. Apart from an overview of this construction, we describe
    some of its applications and implications.

[email redacted]
1 Introduction

Instead of starting by indicating what the title of my talk, The Fluid/Gravity Correspon-
dence, is, I will start by mentioning what it is not. For several decades now, relativists have
been intrigued by the idea that spacetime, or some important part of it like black hole hori-
zons, might resemble a fluid. Already in the 70's, black hole thermodynamics [1, 2, 3] laid its
foundations with the spectacular realization that stationary black hole horizons have thermo-
dynamic properties such as temperature and entropy, much like fluids; in fact the generalized
2nd law of thermodynamics treats black hole entropy on par with external matter entropy.
In the early 80's, analog models of black holes [4] illustrated the converse notion, that fluids
can admit sonic horizons and even the analog of Hawking temperature; indeed they can
reproduce the kinematic aspects of black holes. I should also mention that in many respects,
black holes actually do exhibit behaviour similar to liquid droplets. For example, recently [5]
used fluid analog models to study higher dimensional black string Gregory-Laflamme insta-
bility [6] as a Rayleigh-Plateau instability of liquid droplets [7, 8], and [9] observed fluid-like
recoil behaviour of horizon in studying anti-kick of merging black holes. Perhaps most fa-
mously, the black hole Membrane Paradigm [10, 11] developed in the mid-80s, realizes the
idea that for external observers, black holes behave much like a fluid membrane, endowed
with physical properties such as viscosity, conductivity, etc.. In particular, the dynamics of
this membrane is described by the familiar laws of fluid dynamics, namely the Navier-Stokes
equations, supplemented by Ohm's law and so forth.

    All of these ideas contain the element of black holes sharing certain fluid properties.
However, the Fluid/Gravity correspondence, which is the subject of this talk, is none of
these.

    So let me now preview what the Fluid/Gravity correspondence is. It is a relation between
fluid dynamics on a fixed (3+1)-dimensional background, and gravity (specifically Einstein's
general relativity with negative cosmological constant) in 4 + 1 dimensions. Mathematically,
it posits that Einstein's equations (with negative cosmological constant) in d + 1 dimensions
capture the (generalized) Navier-Stokes equations in d dimensions. Given an arbitrary fluid
dynamical solution, we can systematically construct a corresponding asymptotically AdS
black hole spacetime with a regular horizon whose evolution mimics that of the fluid flow.
The specific correspondence was formulated within the context of the gauge/gravity duality
just a few years ago by Bhattacharyya, Minwalla, Rangamani, and myself in [12], building
on previous works [13, 14, 15] and since then has been generalized and applied in hundreds
of further works.1

    As with most ideas which bridge several fields, there are many potential applications
and opportunities for cross-fertilization between the fields. We saw an example of this in
Gary Horowitz's talk, where gravitational calculations provided insight into certain con-

    1 For recent reviews, see e.g. [16, 17], and in a broader context of time-dependence in AdS/CFT, [18].

                                                          1
densed matter systems. Broadly speaking, the fluid/gravity correspondence has applications
not only to black hole physics, but also to strongly coupled field theories, as well as fluid
dynamics itself. Since a given fluid solution specifies a corresponding evolving and non-
uniform black hole solution (to arbitrary accuracy in the long-wavelength regime), the fluid
in effect provides a useful window into generic black hole dynamics, no longer constrained
by any symmetries. Conversely, we can use the gravity side to learn about the character-
istic properties of the gauge theory plasma, such as transport coefficients of the conformal
fluid. Such quantities depend on the underlying microscopic structure and are notoriously
difficult to calculate directly on the field theory side; nevertheless within our framework,
gravity actually determines them. This is in fact useful even for experimental physics, since
such conformal fluid to a degree mimics the physics of the quark-gluon plasma currently
observed at the Relativistic Heavy Ion Collider, as well as that of certain condensed matter
systems.2 Finally, since the low-energy effective description of gauge theory is fluid dynam-
ics, the fluid/gravity correspondence suggests intriguing applications to hydrodynamics as
such. Despite decades of theoretical as well as numerical, observational, and experimental
study of hydrodynamics, there are still many deep questions which remain to be answered.
For example, one of the famous Clay Millennium Prize Problems concerns the global reg-
ularity (existence and smoothness) of the Navier-Stokes equations [23]. Intriguingly, the
solutions often include turbulence, which, in spite of its practical importance in science and
engineering, still remains one of the great unsolved problems in physics. The fluid/gravity
framework allows us to `geometrize' the set-up, thereby providing a new perspective on these
long-standing hydrodynamical puzzles.

    The plan for the rest of the talk is the following. I will first briefly present the essential
background, recalling the highlights from the gauge/gravity duality. I will then describe our
starting point, namely the correspondence for the configuration describing a global equilib-
rium. Considering deformations of this `seed' configuration, we will be able to include the
important physics of dissipation and to construct genuinely time-dependent solutions. I will
describe the method of obtaining these solutions in a `boundary-derivative' expansion, first
at the conceptual level and then more formally. Having indicated how to obtain a generic
solution to arbitrary order in this expansion, I will discuss the solution to second order,
obtained in [12, 24, 25]. In particular, I will focus on identifying the event horizon in the
bulk geometry and extracting the transport coefficients in the boundary fluid. Finally, I
will briefly mention some important generalizations of the framework and discuss further
applications of the fluid/gravity correspondence.

    2 For nice reviews, see e.g. [19, 20, 21, 22].

                                                          2
2 Background: gauge/gravity duality

Underlying the fluid/gravity framework is the gauge/gravity (or AdS/CFT) duality. In a
nutshell, this duality [26, 27, 28]3 relates a particular strongly coupled non-abelian gauge
theory in d dimensions to string theory, which in certain regime reduces to classical gravity,
on (d + 1)-dimensional asymptotically Anti de Sitter (AdS) spacetime.

    It is worth noting the key aspects of this correspondence. Most conspicuously, the
gauge/gravity duality relates a gravitational theory to non-gravitational one. In fact, the
gauge theory in a sense provides a formulation of quantum gravity on asymptotically AdS
spacetime. This has fueled a large amount of research during the last decade, as one hopes
to solve many long-standing quantum gravitational problems by recasting them in a non-
gravitational language. More intriguingly, the correspondence is holographic: the two dual
theories live in different number of dimensions.4 A useful conceptualization of the duality is
to think of the gauge theory as `living on the boundary' of AdS. We therefore refer to the
gravity side as the "bulk" and the gauge side as the "boundary" theory. Finally, AdS/CFT
constitutes a strong/weak coupling duality; the strongly-coupled field theory can be accessed
via the semi-classical gravitational dual, which has obvious computational as well as concep-
tual advantages. Hence the information flow, namely using one side of the duality to learn
about the other, proceeds fruitfully in both directions.

    Let me now describe several more specific features of the correspondence. Distinct asymp-
totically AdS (bulk) geometries correspond to distinct states in the (boundary) gauge theory.
The pure AdS bulk geometry, i.e. the maximally symmetric negatively curved spacetime,
corresponds to the vacuum state of the gauge theory. Deforming the bulk geometry (while
maintaining the AdS asymptotics) corresponds to exciting the state (within the same the-
ory). Specifically, such metric perturbations are related to the stress(-energy-momentum)
tensor expectation value in the CFT. More importantly in the present context, a large5
Schwarzschild-AdS black hole corresponds to a thermal state in the gauge theory. This
can be easily conceptualized as the late-time configuration a generic state evolves to: in
the bulk, the combined effect of gravity and negative curvature tends to make a generic
configuration collapse to form a black hole which settles down to the Schwarzschild-AdS
geometry, while in the field theory, a generic excitation will eventually thermalize. Note that

    3 The AdS/CFT correspondence is comprehensively reviewed in the classic reviews [29, 30]. For more
recent reviews see e.g. [21, 31].

    4 In fact, the holographic principle [32, 33], motivated by the peculiar non-extensive nature of black hole
entropy, was proposed already prior to the AdS/CFT correspondence, but its best-understood realization
appears in the AdS/CFT context.

    5 AdS is a space of constant negative curvature, which introduces a length scale, called the AdS scale
RAdS, corresponding to the radius of curvature. The black hole size is then measured in terms of this
AdS scale; large black holes have horizon radius r+ > RAdS. Here we will take the large black hole limit
r+ RAdS, and therefore consider so-called planar Schwarzschild-AdS black holes.

                                                          3
although the underlying theory is supersymmetric, the correspondence applies robustly to
non-supersymmetric states such as the black holes mentioned above. In this sense, super-
symmetry is not needed for the correspondence.

    On the boundary, the essential physical properties of the gauge theory state (such as local
energy density, pressure, temperature, entropy current, etc.) are captured by the boundary
stress tensor, which in turn is induced by the bulk geometry and can be extracted via a
well-defined Brown-York type procedure [34].6 It is important to distinguish the two stress
tensors one might naturally consider. In our framework, the bulk stress tensor appearing
on the RHS of the bulk Einstein's equation is set to zero, so that the bulk solutions gab
correspond to general vacuum black holes with negative cosmological constant but no other
matter content. On the other hand, the boundary stress tensor T � is non-zero; it captures
the matter content of the boundary theory, its conservation determines the dynamics, but it
does not curve the boundary spacetime `a la Einstein's equations since the boundary metric
is non-dynamical and fixed (in our case to the 4-dimensional Minkowski spacetime).

    To summarize,7 the boundary fluid is specified by the boundary stress tensor T �(x�),
while the bulk geometry is specified by the bulk metric gab(r, x�). The bulk dynamics is
determined by Einsteins equations,

                1                                                                    (2.1)
Eab  Rab - 2 R gab +  gab = 0 ,

while the boundary dynamics is determined by stress tensor conservation,

         �T � = 0 .                                                                  (2.2)

In the following, we'll see that (2.2) actually arises from (2.1); in this sense, bulk gravity
gives rise the boundary fluid dynamics.

6 For example, for asymptotically AdSd+1 spacetimes, the prescription of [34] gives

T � = lim dc-2 K� - K � - (d - 1) � - 1        R� - 1 R �
c 16 GN                            d-2         2

where � is the d-dimensional metric induced on a r = c cutoff surface, R� and R are the corresponding
Ricci tensor and scalar, K� and K are the extrinsic curvature and its trace, and GN is the Newton's

constant in d + 1 dimensions. See also [35].
    7 We use the following notation for the coordinates: the bulk line element ds2 = gab dXa dXb depends

on all bulk directions Xa = (r, x�) which consist of the radial direction r and the `boundary' spacetime
directions x� = (t, xi). The d + 1 dimensional bulk action is given by

               1  dd+1X        (R  -  2  )  .
Sbulk = 16 GN              -g

                  4
Fig. 1: Penrose diagram for the planar Schwarzschild-Ads5 black hole given by (3.1). The
top and bottom (red) curves correspond to the curvature singularity, the diagonal dashed
(blue) lines to the horizon, and the vertical (black) lines to the AdS boundaries.

3 Global equilibrium

Let us now examine the planar Schwarzschild-AdS black hole which, as already mentioned,
describes a state in global thermal equilibrium. The metric of the planar Schwarzschild-AdS5
black hole is

      ds2 = r2                                3  +  dr2       ,  where f (r)  1 - r+4 .                       (3.1)
                                                                                         r4
                    -f (r) dt2 + (dxi)2             r2 f (r)

                                i=1

This spacetime has a spacelike curvature singularity at r = 0, cloaked by a regular event

horizon at r = r+, and a timelike boundary at r = . The causal structure of this solution

is described by the Penrose diagram of Fig. 1. An important quantity is the temperature of

this  black  hole,  determined  from  the  surface  gravity      (with  respect  to  (     )a  at  r  =  r+)  to  be
                                                                                        t

                                                 T = r+ .                                                     (3.2)


Note that unlike the usual asymptotically flat Schwarzschild black hole where the tempera-
ture scales inversely with the black hole size, here it scales linearly; this confirms that such
a black hole is thermodynamically stable, as required of thermal equilibrium.

    This solution is static and translationally invariant in the boundary spatial directions xi.
One can in fact generate a 4-parameter family of solutions by scaling r and boosting in R3,1
with normalized 4-velocity u�. Moreover, we can pass to the analog of ingoing Eddington-
Finkelstein coordinates, so as to render the metric manifestly regular on the horizon. This
allows us to express the planar Schwarzschild-AdS5 black hole (3.1) in more convenient
(regular and boundary-covariant) coordinates

                    ds2 = -2 u� dx� dr + r2                 4 T 4       dx� dx ,                              (3.3)
                                                    � + r4 u� u

                                                    5
parameterized by the black hole temperature T and the horizon velocity u�. Note that since
u� u� = -1, (3.3) constitutes a 4-parameter family of solutions of (2.1), describing stationary
black holes.

Let us now turn to the boundary description of such a state. The boundary stress tensor

induced  by  the  bulk  metric  (3.3)  is  (upon  setting      1  =  1)
                                                           16 GN

                                T � = 4 T 4 (� + 4 u� u) .                        (3.4)

This describes a perfect fluid at temperature T , moving with velocity u� on the flat 4-

dimensional background �.       Note that this stress tensor is traceless,  T  �  = 0, as befits a
                                                                               �

conformal fluid. More importantly, there is no dissipation in the system.8 In order to describe

more general time-dependent and dissipative systems, we need to go beyond a perfect fluid

in global equilibrium.

4 Nonlinear deformations away from global equilibrium

We will now motivate how to go about constructing such a general set of solutions. We
first focus on the stress tensor, explaining how its form is determined by the symmetries
of the set-up, leaving us with a finite number of undetermined coefficients. We then recall
how some of these coefficients have been previously obtained from linearized analysis in the
gravity dual. Finally, we explain how to go beyond the linearized regime to construct our
generic solutions in the bulk.

4.1 Fluids with dissipation

Dissipation is a crucial aspect of the physics, allowing the state to settle down at late times. If
the stress tensor is to capture dissipation, it must allow for variations of T and u�. However,
in order to have a sensible fluid description, these variations are constrained to lie in the
so-called long wavelength regime: the scale of variation L of the fluid variables T and u� must
be large compared to the microscopic scale 1/T � otherwise these thermodynamic variables
would be meaningless. This automatically provides a small parameter

                                                  1        1,                     (4.1)

                                                  LT

and naturally allows us to expand the stress tensor T � in `boundary derivatives' �(. . .). In
such an expansion, terms of order (�u)n, . . . , �n u will be suppressed by n. In particular,

    8 This is manifest for stationary fluid, but even if T and u� vary in time, the perfect fluid form of the
stress tensor (3.4) disallows dissipation, as can be verified from the vanishing divergence of corresponding
entropy current.

                                                  6
we can expand the stress tensor as

   T � = 4 T 4 (� + 4 u� u) + �(1) + (�2) + . . . ,                    (4.2)

where �(1) contains dissipative terms composed of single-derivative expressions such as �u,
the next term (�2) contains the second order dissipative terms, and so on. As mentioned
above, the dynamics is determined by the conservation equations (2.2), which become more
complicated as one includes more terms in T �. For the zeroth-order T � given by the perfect

fluid (3.4), this yields mass conservation and Euler equation; when one includes dissipation,
the stress tensor conservation is described by the generalized9 Navier-Stokes equations.

    It turns out that (4.2) is a very useful way to package the stress tensor. At each order,
the form of the stress tensor is actually determined by symmetries, leaving just a finite
number of undetermined transport coefficients. Since we are dealing with a conformal fluid,
the stress tensor has to be Weyl covariant, as well as generally covariant in the boundary
directions. This procedure of using the Weyl-covariant formalism [37] is so robust that we
can equally easily write the form of a more general d-dimensional dissipative stress tensor
for a conformal fluid living on a fixed background with metric �, to second order:

T � = P (� + d u� u) - 2  �

+ 2  1 u D� -  (�  +  �) + C C� u u                                    (4.3)

+    [�    -  P �                     ]  +    [�    +  P �       ]  ,
              d - 1                                    d - 1 

where P is the pressure and we have used various standard quantities built out of the velocity
u� and the background metric �; in particular, � and � are the shear and the vorticity
of the fluid, respectively, P � = � + u� u is the spatial projector, D is the Weyl-covariant
derivative, and C� is the Weyl tensor for �. In the above expression, the 0th and 1st
order terms appear on the first line, whereas the 2nd order terms fill the remaining two lines.

4.2 Transport coefficients from linearized gravity

The shear viscosity  and the five second-order transport coefficients, 1,  , C, , and
, are not determined from the symmetries. These transport coefficients depend on the
microscopic structure of the fluid; they could be in principle measured, or calculated from
first principles. However, both of these approaches are rather difficult, since the gauge
theory is strongly coupled. Nevertheless, as we will shortly see, the bulk dual in fact deter-
mines these transport coefficients uniquely. Although this will occur very naturally within

    9 There are two generalizations to the form described in conventional (non-relativistic) fluid dynamics
[36]: one arises from including terms beyond first order in boundary derivatives, and another from the fact
that our fluid is relativistic, with pressure comparable to the energy density.

                                    7
the fluid/gravity framework, one should note that the transport coefficients can already be
extracted in the linearized regime, from quasinormal modes10 of the planar black hole.

To see how this works in more detail, let us first recall that the black hole quasinormal

modes encode the field theory's return to thermal equilibrium [39]. Most modes decay with

a characteristic timescale related to the size of the black hole r+, but there are also so-
called hydrodynamic modes which can have arbitrarily long wavelength and small frequency,

and therefore fall within the long-wavelength regime discussed above. Such modes with

hydrodynamic dispersion relations were first considered in [41, 42] and describe a propagating

sound mode with linear dispersion and shear mode with damped quadratic dispersion.11 One

can then use linear response theory to compute the transport coefficients. This analysis not

only confirmed the relation between classical dynamics in a black hole background and the

physics of a strongly coupled plasma, but it also prompted the famous bound [45] on the

ratio of shear viscosity to entropy density, /s   1  .  This bound is saturated by a large
                                                  4

class of two-derivative theories of gravity, and it is indeed experimentally satisfied by all

presently-known systems in nature. Intriguingly, cold atoms at unitarity and quark-gluon

plasma both come near to saturating the bound [46].

4.3 Constructing a generic black hole geometry

Rather than restricting attention to linearized gravity around a fixed black hole background,
we now turn to the main task of finding a bulk solution of the full Einstein's equations,
capable of describing arbitrarily large deviations from the stationary planar black hole (3.3)
in the long-wavelength regime. Of course, solving the full Einstein's equations for a generic
ansatze is prohibitively difficult, but we will see that the long-wavelength regime renders the
problem tractable. Before explaining the actual construction, we first provide a conceptual
motivation for the method.

    Let us suppose that the `parameters' T and u� describing the black hole in (3.3) vary
slowly in x�. Then at each x�0 , the geometry should look approximately like a black hole
with temperature T (x0) and velocity u�(x0). We refer to the bulk spacetime region in the
neighborhood of a fixed x� but extended over all r as a `tube'; and we say that in the long-
wavelength regime, the bulk geometry `tubewise' approximates a planar black hole with
specific velocity and temperature. We illustrate this idea in the cartoon of Fig. 2, where the
curve indicates the variation of the temperature T (x�) and the color-coding the variation

  10 These modes describe small fluctuations of a black hole, namely its ringing and settling down. Math-
ematically, they are related to the poles of the retarded Green's function. A good pre-AdS/CFT review is
[38], in AdS/CFT context these were first discussed in [39], and a recent extensive review of quasinormal
modes in context relevant to the present set-up appears in [40].

  11 Extracting linearized hydrodynamics from linearized gravity has been pursued vigorously over the years;
for a nice review, see [43]. For the dispersion relation describing the sound and shear modes of AdS black
holes, see e.g. Fig.7 and Fig.4 of [44], respectively.

                                                          8
r                                       r

                               x                                             x

Fig. 2: Cartoon of `tubewise approximation' of slowly-varying configuration by a correspond-
ing piecewise-constant one.

of (some component of) the velocity. The slower such variations are, the better can we
approximate the configuration with piecewise-constant tubes. Our task then is to patch
such tubes together to construct a non-uniform and time-evolving black hole.

    Of course, if we just replace u� and T in the metric (3.3) by T (x) and u�(x), the resulting
metric (call it ga(0b)) will no longer solve Einstein's equations (2.1). However, it is a manifestly

regular metric which approaches a solution in the limit of infinitely slow variations. This
enables us to use the metric ga(0b) as a starting point for constructing an iterative solution.

The requirement of slow variations can be written schematically as

                   � log T  O( ) ,         �u  O( )                             (4.4)
                      T                     T

where is a small parameter. In terms of the fluid description, it is indeed the same parameter
(4.1) (counting the number of x� derivatives) which ensured that the configuration is in local
equilibrium and therefore describable as a fluid. Using as an expansion parameter, we
expand the metric and the fields u�(x) and T (x) as


   gab =           k ga(kb) ,  T=       k T (k) ,  u� =           k u�(k) .     (4.5)

              k=0                  k=0                       k=0

We can then substitute the expansion (4.5) into Einstein's equations (2.1), and find the
solution order by order in . The term ga(kb) corrects the metric at the kth order, such that
Einstein's equations will be satisfied to O( k) provided the functions T (x) and u�(x) obey a

certain set of equations of motion, which turn out to be precisely the stress tensor conserva-
tion equations (2.2) of boundary fluid dynamics at O( k-1). Hence the resulting corrected

metric can be constructed systematically to any desired order. Importantly, the expansion

remains valid well inside the event horizon, which allows verification of the regularity of such

a solution.

    Let us examine the structure of the equations a bit more explicitly. Einstein's equations
(2.1) split up into two kinds: Constraint equations, Er� = 0 which implement stress-tensor

                                     9
conservation (at one lower order), and Dynamical equations E� = 0 and Err = 0 which
allow determination of g(k). Schematically, the latter take a miraculously simple form:

H g(0)(u(�0), T (0)) g(k) = sk ,        (4.6)

where H is a second-order linear differential operator in the variable r alone and sk are
regular source terms which are built out of g(n) with n  k - 1. Since g(k)(x�) is already of
O( k), and since every boundary derivative appears with an additional power of , H is an
ultra-local operator in the field theory directions. Moreover, at a given x�, the precise form
of this operator H depends only on the local values of T and u� but not on their derivatives at
x�. Furthermore, we have the same homogeneous operator H at every order in perturbation

theory. This allows us to find an explicit solution of (4.6) systematically at any order. The

source term sk however gets more complicated with each order, and reflects the nonlinear
nature of the theory. We solve the dynamical equations

g(k) = particular(sk) + homogeneous(H)

subject to regularity in the interior and asymptotically AdS boundary conditions. The
solution is guaranteed to exist,12 provided the constraint equations are solved.

    Before turning to the solution itself, let us summarize the key points of our construction.
The iterative construction can in principle be systematically implemented to arbitrary order
in (which obtains correspondingly accurate solution). The resulting black hole spacetimes
actually correspond to not just a single solution or even a finite family of solutions, but rather
a continuously-infinite set of (approximate) solutions, specified by four functions, T (x) and
u�(x), of four variables. The flip side of the coin is that while very general, such a metric is
not fully explicit: in order to be so, we need to use a given solution to fluid dynamics, which
relates the functions T (x) and u�(x), as input. Nevertheless, given any such solution, the
construction guarantees that the bulk geometry describes a black hole with regular event
horizon.

5 General solution

The solution for the bulk metric gab(r, x�) and the boundary stress tensor T �(x�) (written
in terms of the temperature and velocity fields T (x�) and u(x�)) was explicitly constructed
to second order in the boundary derivative expansion in [12]. This solution was further
studied in [24], where its regularity was confirmed by identifying the event horizon. This

  12 Using the rotational symmetry group of the seed solution (3.3) it turns out to be possible to make a
judicious choice of variables such that the operator H is converted into a decoupled system of first order
differential operators. It is then simple to solve the equation (4.6) for an arbitrary source sk by direct
integration. For the details of the procedure, as well as discussion of convenient gauge choice, etc., see the
original work [12] or the review [16].

                                                         10
construction was subsequently generalized to other contexts, as reviewed in [16]. Since the
solution for the second-order metric is page-long, here we only report the solution to first
order for illustration.

   To first order the bulk metric takes the form

      ds2 = -2 u� dx�dr + r2 (� + [1 - f (r/T )] u� u) dx�dx

                       +  2r     r  F (r/T ) �        +  1  u�u  u     -    1  u (uu�)       dx�dx ,       (5.1)
                                T                        3                  2

where f (r) is defined in (3.1), F (r) is given by

                                x2 + x + 1            1         (1 + r)2(1 + r2)

   F (r)                 dx x(x + 1) (x2 + 1) = 4 ln                   r4             - 2 arctan(r) +  ,

                    r

�  =  P �P             (u)   -  1  P �   u  is    the  shear,   and  T (x)  and  u�(x)  are  any     slowly-varying
                                3

functions which satisfy the conservation equation (2.2) for the zeroth order perfect fluid

stress tensor (3.4). Note that the first line of (5.1) corresponds to the zeroth order solution

(3.3), whereas each of the terms in the second line have exactly one boundary derivative.13

    As mentioned previously, this bulk solution is `tubewise' approximated by a planar black
hole. This means that in each tube, defined by a small neighborhood of given x�, but fully
extended in the radial direction r, the radial dependence of the metric is approximately that
of a boosted planar black hole at some temperature T and horizon velocity u�, with correc-
tions suppressed by the rate of variation, . These parameters vary from one position x� to
another in a manner consistent with fluid dynamics. Our choice of coordinates is such that
each tube extends along an ingoing radial null geodesic; see Fig. 3. Apart from technical
advantages, this is conceptually rather pleasing, since it suggests a mapping between the
boundary and the bulk which is natural from causality considerations. Physically, the solu-
tion (5.1) and its higher-order improvements of course describe a dynamically evolving black
hole with infinitely extended but non-uniform event horizon. The causal structure of this
solution is preserved; in fact, dissipation will cause the black hole to approach a stationary
solution (3.3) at late times.

    Let us now focus on the most salient feature of this geometry, namely its event horizon.
Assuming the dissipation causes our configuration to settle down to a stationary state at late
times, we can find the event horizon as the unique null hypersurface with the correct late-
time behavior. This can be solved algebraically, order-by-order in , and takes the schematic
form [24]

      r+(x)               =    T (x)  +     1     (#  � (x)     � (x)  +  #    � (x)   � (x))  +  .  .  .  (5.2)
                                           T (x)

  13 Note that (5.1) does not have any �T terms appearing explicitly, since by implementing the zeroth
order stress tensor conservation, we have expressed the temperature derivatives in terms of the velocity
derivatives.

                                                            11
Fig. 3: The causal structure of the spacetimes dual to fluid mechanics illustrating the tube
structure. The dashed line denotes the future event horizon H+ generated by A, while the
shaded tube indicates the region of spacetime over which the solution is well approximated
by a tube of the uniform black brane.

Intriguingly, it turns out that within this derivative expansion, the location of the event
horizon r+(x�) in the bulk is determined locally by the behavior of the temperature and
velocity at a point x� (in particular it is insensitive to the metric at later times), rather than
globally as usual in general relativity. This curious locality is in fact allowed by the long
wavelength regime, wherein the horizon position varies sufficiently slowly.

    Fig. 4 gives a cartoon of the behaviour (for simplicity just the local temperature) of
the event horizon for some generic fluid configuration. We see that even if at early times
(bottom of the sketch) the horizon is highly non-uniform, its evolution will tend to dissipate
the inhomogeneities. At late times (top part of the sketch), the horizon settles down to a
stationary configuration. Throughout, the evolution proceeds in such a way that the horizon
area grows, as can be verified by explicit calculation. This has an important consequence for
the dual fluid dynamical description. The pull-back of the area form on the horizon provides
a natural entropy current in the dual fluid. Such entropy current then automatically satisfies
the 2nd Law of thermodynamics.

    Let us now turn to the induced fluid stress tensor on the boundary. The stress tensor to
first order in boundary derivatives can be easily obtained from the bulk metric (5.1), and
takes the simple form

T � = 4 T 4 (4 u�u + �) - 2 3 T 3 � .  (5.3)

Here the first two (derivative-free) terms describe a perfect fluid with pressure 4 T 4, and
correspondingly (using thermodynamics) entropy density s = 4 4 T 3. The shear viscosity 

12
Fig. 4: A cartoon of the event horizon r = r+(x�) sketched as a function of the time t and
one of the spatial coordinates xi (the other two spatial coordinates are suppressed).

of this fluid may be read off from the coefficient of � and is given by 3 T 3. Notice that

this verifies that our system indeed saturates the famous bound [45] on viscosity-to-entropy-

density  ratio     =   1  ,  in  agreement  with  the  well-known  result  of  [13].
                s     4

While we only verified previously-known results using the first-order stress tensor, at

second order we can start making new predictions. We have already written the form of

the stress tensor in (4.3), leaving only several coefficients to fix. These transport coefficients

are however important in determining the physical properties of the fluid. For fluids in 3+1

dimensional flat spacetime, the second order transport coefficients were obtained in [12] (and

concurrently by [47]), but here we will quote the more general result [25, 48] pertaining to

                                                       13
conformal fluids in d-dimensional curved spacetime � with the stress tensor (4.3):

P=        1     4 T d

    16GN d

    s        1            4 T d-1
= =
    4 16GN d

       d     1-            yd-2 - 1
1 = 4 T                   dy
                       1     y (yd - 1)                                             (5.4)

       d      yd-2 - 1
=               dy
    4 T 1 y (yd - 1)

                d
 = C = 4 T 2 

 = 0 .

Note that written suggestively in this way, we can discern intriguing relations between the
coefficients, which hint at the specific nature of any conformal fluid which admits a gravita-
tional dual. For example, the results that  = C and  = 0 are universal but non-trivial
from the fluid standpoint. More intriguingly, we see that14  = 2  (1 +  ) for all d.

6 Concluding remarks

The results summarized above have since been extended and generalized in a number of
useful directions. As already indicated, one immediate set of generalizations involved relat-
ing a d-dimensional conformal fluid to asymptotically AdSd+1 black hole (see [49] for the
interesting case of d = 3 and [48, 25] for general d). An intriguing observation of [49] is the
striking difference between the phenomenology of non-relativistic turbulent flows in 3+1 and
2+1 dimensions. In the 3+1 dimensional turbulent energy cascade, large scale eddies give
rise to smaller scale eddies, eventually transferring energy down to scales where viscosity
becomes important and energy is dissipated. In contrast, 2+1 dimensional turbulent flows
are characterized by an inverse cascade, in which smaller scale eddies merge into large scale
eddies, creating large long-lived vortical structures. If these qualitative differences extend to
relativistic fluids, they would suggest a profound difference in gravitational dynamics in four
and five dimensions. In particular, we might predict that black holes in AdS4 would take
much longer to equilibrate than AdS5 black holes. From the gravitational standpoint, this
would certainly seem very surprising.

    More ambitiously, one may also consider fluids on curved manifolds (rather than just
the Minkowski spacetime Rd-1,1), as has been initiated in [50]. In addition, one can include
matter in the bulk. This allows for richer dynamics, but typically at the expense of losing

  14 in fact this relation continues to hold even for charged black holes mentioned in �6 [48, 25].

                                                         14
universality. Early examples of such extensions include considering the dilaton (which cor-
responds to forcing of the fluid) in [50], Maxwell U (1) field [51, 52], multiple Maxwell fields
and scalars, magnetic and dyonic charges, as well as more exotic models (see e.g. [16] for fur-
ther references). Moreover, one can even extend the correspondence to non-conformal fluids
[53, 54] as well as to non-relativistic fluids [55, 56], which allows us to make closer contact
with familiar everyday systems. Nevertheless, many future directions and puzzles remain,
as well the need for further generalizations. For example, of particular current interest is
to understand the fluid/gravity correspondence for extremal fluids (and in particular super-
fluids) which are presently attracting much attention. Also, to mimic many of the familiar
aspects of fluid flows, we need to understand how to confine the fluid within walls in the
gravity dual. Still more ambitiously, to understand the rich phenomena rooted in quantum
processes, we would like to get a better handle on stringy and quantum effects.

    The fluid/gravity correspondence has a number of useful implications. Among these is
an improvement on the Israel-Stewart formalism [57]. At first order, relativistic viscous
fluid is described by a parabolic system, which leads to apparent causality violations. The
Israel-Stewart formalism renders the system hyperbolic by adding some 2nd order terms,
but it does not capture all possible ones. The fluid/gravity construction in effect prescribes
the correct completion to render the full system causal. Another intriguing consequence is
the appearance of a new pseudo-vector contribution to the charge current,15 which has been
ignored by Landau&Lifshitz [36], but which may have potentially observable effects [58]. At
a more general level, the framework of the fluid/gravity correspondence is rather reminiscent
of the recently-developed `blackfold approach' to constructing higher-dimensional black holes
[59, 60]. Whereas the former has an independent physical description of the bulk black hole
provided by the dual conformal fluid, the latter is applicable to black holes with any asymp-
totics, as long as there is a separation of scales. As a final example of useful application of the
fluid/gravity correspondence, we note that the framework suggests a convenient rewriting
of rotating AdS black holes in terms of fluid variables [50], which is useful for analyzing its
properties.

    To summarize, one of the most intriguing features of the fluid/gravity correspondence is
that it provides us with a window into the generic behavior of gravity in a nonlinear regime,
mapping long-wavelength (but arbitrary amplitude) perturbations of AdS black holes to the
more familiar physics of fluid dynamics. Apart from the obvious conceptual advantages, one
has a tremendous computational simplification for numerical studies of gravitational solu-
tions since the fluid dynamics lives in one lower dimension. The boundary fluid stress tensor
likewise contains new quantities of interest, namely the various transport coefficients which
characterize the fluid. This has been of interest in QCD phenomenology, especially in under-
standing certain characteristic features of the quark-gluon plasma. Hence the fluid/gravity

15 Specifically, for Maxwell-Chern-Simons charged fluid, in addition to standard dissipative terms, a new

(parity-violating but CP preserving) 1st order term appears in charge current:  �=        �  u    u  .


15
correspondence provides a useful tool for not only studying behavior of generic black holes
in AdS, but also for geometrizing fluid dynamics and for gaining insight into behavior of
strongly coupled field theories, which exhibit similar features to certain real-world systems.
This is still a young and rapidly-expanding area of research, promising many further appli-
cations and fruitful developments.

    Finally, let me close by revisiting the subtitle of my talk, so as to specify the new perspec-
tive on the black hole membrane paradigm that the fluid/gravity correspondence offers [61].
As described earlier, the conventional membrane paradigm [10] provides a simple picture of
black hole dynamics in terms of a fluid living on a `membrane' (the stretched horizon) just
outside the event horizon. Stepping back to take a more general view of trying to encode the
black hole dynamics by fluid dynamics localized on a membrane in the spacetime, a natural
question is where should such a membrane live? Perhaps the most obvious candidate is the
event horizon; but this is problematic due to its null nature, and more importantly, because
it is defined globally, requiring the knowledge of full future evolution of the spacetime. Alter-
nately, several (quasi)local notions of a black hole have been proposed, such as the so-called
dynamical horizon [62, 63], which however are spacelike surfaces inside the event horizon,
and therefore do not admit the standard notion of evolution. A more popular suggestion
is the stretched horizon, which is the formulation given by the membrane paradigm [10].
However, there likewise remain ambiguities in localizing the stretched horizon. Within the
fluid/gravity correspondence, the entire spacetime evolution is mapped to the dynamics of
a conformal fluid, which, albeit reminiscent of the membrane paradigm, has one important
twist: the membrane lives on the boundary of the spacetime (which is unambiguously de-
fined and admits a fluid description with well-defined dynamics), and gives a perfect mirror
of the full bulk physics. This "membrane at the end of the universe" picture is a natural
consequence of the holographic nature of the fluid/gravity correspondence.

Acknowledgements

It is a pleasure to thank my collaborators, Sayantani Bhattacharyya, R. Loganayagam,
Gautam Mandal, Shiraz Minwalla, Takeshi Morita, Mukund Rangamani, Harvey Reall, and
Mark Van Raamsdonk for wonderful collaborations on various aspects discussed in this
review. VH is partly supported by STFC Rolling grant.

References

 [1] J. D. Bekenstein, "Black holes and entropy," Phys. Rev. D7 (1973) 2333�2346.

 [2] S. W. Hawking, "Particle Creation by Black Holes,"
      Commun. Math. Phys. 43 (1975) 199�220.

                                                         16
 [3] J. M. Bardeen, B. Carter, and S. W. Hawking, "The Four laws of black hole
      mechanics," Commun. Math. Phys. 31 (1973) 161�170.

 [4] W. G. Unruh, "Experimental black hole evaporation,"
      Phys. Rev. Lett. 46 (1981) 1351�1353.

 [5] V. Cardoso and O. J. C. Dias, "Gregory-Laflamme and Rayleigh-Plateau
      instabilities," Phys. Rev. Lett. 96 (2006) 181601, arXiv:hep-th/0602017.

 [6] R. Gregory and R. Laflamme, "Black strings and p-branes are unstable,"
      Phys. Rev. Lett. 70 (1993) 2837�2840, arXiv:hep-th/9301052.

 [7] J. Plateau, Statique Experimentale et Theorique des Liquides Soumis aux Seules
      Forces Moleculaires. Gauthier-Villars, 1873.

 [8] L. Rayleigh Proc. Lond. Math. Soc. 10 (1878) 4.

 [9] L. Rezzolla, R. P. Macedo and J. L. Jaramillo, "Understanding the `anti-kick' in the
      merger of binary black holes," Phys. Rev. Lett. 104 (2010) 221101,
      arXiv:1003.0873 [gr-qc].

[10] K. S. Thorne, R. H. Price, and D. A. MacDonald, Black Holes: The Membrane
      Paradigm. Yale University Press, New Haven, 1986.

[11] T. Damour, "Black Hole Eddy Currents," Phys. Rev. D18 (1978) 3598�3604.

[12] S. Bhattacharyya, V. E. Hubeny, S. Minwalla, and M. Rangamani, "Nonlinear Fluid
      Dynamics from Gravity," JHEP 02 (2008) 045, arXiv:0712.2456 [hep-th].

[13] G. Policastro, D. T. Son, and A. O. Starinets, "The shear viscosity of strongly coupled
      N = 4 supersymmetric Yang-Mills plasma," Phys. Rev. Lett. 87 (2001) 081601,
      arXiv:hep-th/0104066.

[14] R. A. Janik and R. B. Peschanski, "Asymptotic perfect fluid dynamics as a
      consequence of AdS/CFT," Phys. Rev. D73 (2006) 045013, arXiv:hep-th/0512162.

[15] S. Bhattacharyya, S. Lahiri, R. Loganayagam, and S. Minwalla, "Large rotating AdS
      black holes from fluid mechanics," JHEP 09 (2008) 054, arXiv:0708.1770 [hep-th].

[16] M. Rangamani, "Gravity & Hydrodynamics: Lectures on the fluid-gravity
      correspondence," Class. Quant. Grav. 26 (2009) 224003, arXiv:0905.4352 [hep-th].

[17] V. E. Hubeny, "Fluid dynamics from gravity," From Gravity to Thermal Gauge
      Theories, Lecture Notes in Physics 828, Springer (2011).
      http://www.springer.com/physics/book/978-3-642-04863-0.

                                                         17
[18] V. E. Hubeny and M. Rangamani, "A Holographic view on physics out of
      equilibrium," arXiv:1006.3675 [hep-th].

[19] D. Mateos, "String Theory and Quantum Chromodynamics,"
      Class. Quant. Grav. 24 (2007) S713�S740, arXiv:0709.1523 [hep-th].

[20] S. S. Gubser and A. Karch, "From gauge-string duality to strong interactions: a
      Pedestrian's Guide," Ann. Rev. Nucl. Part. Sci. 59 (2009) 145�168,
      arXiv:0901.0935 [hep-th].

[21] J. McGreevy, "Holographic duality with a view toward many-body physics,"
      arXiv:0909.0518 [hep-th].

[22] S. A. Hartnoll, "Lectures on holographic methods for condensed matter physics,"
      Class. Quant. Grav. 26 (2009) 224002, arXiv:0903.3246 [hep-th].

[23] C. Fefferman, "Existence and smoothness of the Navier-Stokes equation," Clay
      Millenium Problems (2000).

[24] S. Bhattacharyya, V. E. Hubeny, R. Loganayagam, G. Mandal, S. Minwalla,
      T. Morita, M. Rangamani, and H. S. Reall, "Local Fluid Dynamical Entropy from
      Gravity," JHEP 06 (2008) 055, arXiv:0803.2526 [hep-th].

[25] S. Bhattacharyya, R. Loganayagam, I. Mandal, S. Minwalla, and A. Sharma,
      "Conformal Nonlinear Fluid Dynamics from Gravity in Arbitrary Dimensions,"
      JHEP 12 (2008) 116, arXiv:0809.4272 [hep-th].

[26] J. M. Maldacena, "The large N limit of superconformal field theories and
      supergravity," Adv. Theor. Math. Phys. 2 (1998) 231�252, arXiv:hep-th/9711200.

[27] S. S. Gubser, I. R. Klebanov, and A. M. Polyakov, "Gauge theory correlators from
      non-critical string theory," Phys. Lett. B428 (1998) 105�114, arXiv:hep-th/9802109.

[28] E. Witten, "Anti-de Sitter space and holography," Adv. Theor. Math. Phys. 2 (1998)
      253�291, arXiv:hep-th/9802150.

[29] O. Aharony, S. S. Gubser, J. M. Maldacena, H. Ooguri, and Y. Oz, "Large N field
      theories, string theory and gravity," Phys. Rept. 323 (2000) 183�386,
      arXiv:hep-th/9905111.

[30] E. D'Hoker and D. Z. Freedman, "Supersymmetric gauge theories and the AdS/CFT
      correspondence," arXiv:hep-th/0201253.

[31] J. Polchinski, "Introduction to Gauge/Gravity Duality," arXiv:1010.6134 [hep-th].

[32] G. 't Hooft, "Dimensional reduction in quantum gravity," arXiv:gr-qc/9310026.

                                                         18
[33] L. Susskind, "The World as a hologram," J. Math. Phys. 36 (1995) 6377�6396,
      arXiv:hep-th/9409089.

[34] V. Balasubramanian and P. Kraus, "A stress tensor for anti-de Sitter gravity,"
      Commun. Math. Phys. 208 (1999) 413�428, arXiv:hep-th/9902121.

[35] S. de Haro, S. N. Solodukhin, and K. Skenderis, "Holographic reconstruction of
      spacetime and renormalization in the AdS/CFT correspondence,"
      Commun. Math. Phys. 217 (2001) 595�622, arXiv:hep-th/0002230.

[36] L. D. Landau and E. M. Lifshitz, Fluid Mechanics (Course of Theoretical Physics,
      Vol. 6). Butterworth-Heinemann, 1965.

[37] R. Loganayagam, "Entropy Current in Conformal Hydrodynamics,"
      JHEP 05 (2008) 087, arXiv:0801.3701 [hep-th].

[38] K. D. Kokkotas and B. G. Schmidt, "Quasi-normal modes of stars and black holes,"
      Living Rev. Rel. 2 (1999) 2, arXiv:gr-qc/9909058.

[39] G. T. Horowitz and V. E. Hubeny, "Quasinormal modes of AdS black holes and the
      approach to thermal equilibrium," Phys. Rev. D62 (2000) 024027,
      arXiv:hep-th/9909056.

[40] E. Berti, V. Cardoso, and A. O. Starinets, "Quasinormal modes of black holes and
      black branes," Class. Quant. Grav. 26 (2009) 163001, arXiv:0905.2975 [gr-qc].

[41] G. Policastro, D. T. Son, and A. O. Starinets, "From AdS/CFT correspondence to
      hydrodynamics," JHEP 09 (2002) 043, arXiv:hep-th/0205052.

[42] G. Policastro, D. T. Son, and A. O. Starinets, "From AdS/CFT correspondence to
      hydrodynamics. II: Sound waves," JHEP 12 (2002) 054, arXiv:hep-th/0210220.

[43] D. T. Son and A. O. Starinets, "Viscosity, Black Holes, and Quantum Field Theory,"
      Ann. Rev. Nucl. Part. Sci. 57 (2007) 95�118, arXiv:0704.0240 [hep-th].

[44] J. Morgan, V. Cardoso, A. S. Miranda, C. Molina, and V. T. Zanchin, "Gravitational
      quasinormal modes of AdS black branes in d spacetime dimensions,"
      JHEP 09 (2009) 117, arXiv:0907.5011 [hep-th].

[45] P. Kovtun, D. T. Son, and A. O. Starinets, "Viscosity in strongly interacting quantum
      field theories from black hole physics," Phys. Rev. Lett. 94 (2005) 111601,
      arXiv:hep-th/0405231.

[46] T. Schafer and D. Teaney, "Nearly Perfect Fluidity: From Cold Atomic Gases to Hot
      Quark Gluon Plasmas," Rept. Prog. Phys. 72 (2009) 126001,
      arXiv:0904.3107 [hep-ph].

                                                         19
[47] R. Baier, P. Romatschke, D. T. Son, A. O. Starinets, and M. A. Stephanov,
      "Relativistic viscous hydrodynamics, conformal invariance, and holography,"
      JHEP 04 (2008) 100, arXiv:0712.2451 [hep-th].

[48] M. Haack and A. Yarom, "Nonlinear viscous hydrodynamics in various dimensions
      using AdS/CFT," JHEP 10 (2008) 063, arXiv:0806.4602 [hep-th].

[49] M. Van Raamsdonk, "Black Hole Dynamics From Atmospheric Science,"
      JHEP 05 (2008) 106, arXiv:0802.3224 [hep-th].

[50] S. Bhattacharyya, R. Loganayagam, S. Minwalla, S. Nampuri, S. P. Trivedi, and S. R.
      Wadia, "Forced Fluid Dynamics from Gravity," JHEP 02 (2009) 018,
      arXiv:0806.0006 [hep-th].

[51] J. Erdmenger, M. Haack, M. Kaminski, and A. Yarom, "Fluid dynamics of R-charged
      black holes," JHEP 01 (2009) 055, arXiv:0809.2488 [hep-th].

[52] N. Banerjee, J. Bhattacharya, S. Bhattacharyya, S. Dutta, R. Loganayagam, and
      P. Surowka, "Hydrodynamics from charged black branes,"
      arXiv:0809.2596 [hep-th].

[53] I. Kanitscheider and K. Skenderis, "Universal hydrodynamics of non-conformal
      branes," JHEP 04 (2009) 062, arXiv:0901.1487 [hep-th].

[54] J. R. David, M. Mahato, and S. R. Wadia, "Hydrodynamics from the D1-brane,"
      JHEP 04 (2009) 042, arXiv:0901.2013 [hep-th].

[55] M. Rangamani, S. F. Ross, D. T. Son, and E. G. Thompson, "Conformal
      non-relativistic hydrodynamics from gravity," JHEP 01 (2009) 075,
      arXiv:0811.2049 [hep-th].

[56] S. Bhattacharyya, S. Minwalla, and S. R. Wadia, "The Incompressible
      Non-Relativistic Navier-Stokes Equation from Gravity," JHEP 08 (2009) 059,
      arXiv:0810.1545 [hep-th].

[57] W. Israel and J. M. Stewart, "Transient relativistic thermodynamics and kinetic
      theory," Ann. Phys. 118 (1979) 341�372.

[58] D. T. Son and P. Surowka, "Hydrodynamics with Triangle Anomalies,"
      Phys.Rev.Lett. 103 (2009) 191601, arXiv:0906.5044 [hep-th].

[59] R. Emparan, T. Harmark, V. Niarchos, and N. A. Obers, "Blackfolds,"
      Phys. Rev. Lett. 102 (2009) 191301, arXiv:0902.0427 [hep-th].

[60] R. Emparan, T. Harmark, V. Niarchos, and N. A. Obers, "Essentials of Blackfold
      Dynamics," arXiv:0910.1601 [Unknown].

                                                         20
[61] V. E. Hubeny, M. Rangamani, S. Minwalla, and M. Van Raamsdonk, "The
      fluid-gravity correspondence: The membrane at the end of the universe,"
      Int. J. Mod. Phys. D17 (2009) 2571�2576.

[62] I. Booth, "Black hole boundaries," Can. J. Phys. 83 (2005) 1073�1099,
      arXiv:gr-qc/0508107.

[63] A. Ashtekar and B. Krishnan, "Isolated and dynamical horizons and their
      applications," Living Rev. Rel. 7 (2004) 10, arXiv:gr-qc/0407042.

                                                         21
