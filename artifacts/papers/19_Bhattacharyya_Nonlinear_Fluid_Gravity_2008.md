# Bhattacharyya Nonlinear Fluid Gravity 2008

**Source:** `19_Bhattacharyya_Nonlinear_Fluid_Gravity_2008.pdf`

---

arXiv:0712.2456v4 [hep-th] 2 Apr 2008                                                                                           TIFR/TH/07-44
                                                                                                                                DCPT-07/73
                                                                                                                                NI07097

                                        Nonlinear Fluid Dynamics from Gravity

                                                    Sayantani Bhattacharyyaa, Veronika E Hubenyb,
                                                          Shiraz Minwallaa, Mukund Rangamanib�

                                                aDepartment of Theoretical Physics,Tata Institute of Fundamental Research,
                                                                       Homi Bhabha Rd, Mumbai 400005, India

                                                    b Centre for Particle Theory & Department of Mathematical Sciences,
                                                   Science Laboratories, South Road, Durham DH1 3LE, United Kingdom

                                                                        November 26, 2024

                                                                                            Abstract
                                               Black branes in AdS5 appear in a four parameter family labeled by their velocity
                                           and temperature. Promoting these parameters to Goldstone modes or collective
                                           coordinate fields � arbitrary functions of the coordinates on the boundary of AdS5
                                           � we use Einstein's equations together with regularity requirements and boundary
                                           conditions to determine their dynamics. The resultant equations turn out to be
                                           those of boundary fluid dynamics, with specific values for fluid parameters. Our
                                           analysis is perturbative in the boundary derivative expansion but is valid for arbitrary
                                           amplitudes. Our work may be regarded as a derivation of the nonlinear equations of
                                           boundary fluid dynamics from gravity. As a concrete application we find an explicit
                                           expression for the expansion of this fluid stress tensor including terms up to second
                                           order in the derivative expansion.

                                       [email redacted]
                                       [email redacted]
                                       [email redacted]
                                       �[email redacted]
Contents

1 Introduction                                  2

2 Fluid dynamics from gravity                   5

3 The perturbative expansion                    8

3.1 The basic set up . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

3.2 General structure of perturbation theory . . . . . . . . . . . . . . . . . . . 9

3.2.1 Constraint equations . . . . . . . . . . . . . . . . . . . . . . . . . . 10

3.2.2 Dynamical equations . . . . . . . . . . . . . . . . . . . . . . . . . . 11

3.2.3 Summary of the perturbation analysis . . . . . . . . . . . . . . . . 12

3.3 Outline of the first order computation . . . . . . . . . . . . . . . . . . . . . 12

3.3.1 Solving the constraint equations . . . . . . . . . . . . . . . . . . . . 12

3.3.2 Solving the dynamical equations . . . . . . . . . . . . . . . . . . . . 12

3.3.3 The `Landau' Frame . . . . . . . . . . . . . . . . . . . . . . . . . . 13

3.4 Outline of the second order computation . . . . . . . . . . . . . . . . . . . 14

3.4.1 The constraints at second order . . . . . . . . . . . . . . . . . . . . 14

3.4.2 Nature of source terms . . . . . . . . . . . . . . . . . . . . . . . . . 15

3.4.3 Solution of the constraint equations . . . . . . . . . . . . . . . . . . 16

3.4.4 Solving for g(2) and the second order stress tensor . . . . . . . . . . 16

4 The metric and stress tensor at first order   16

4.1 Scalars of SO(3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

4.2 Vectors of SO(3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

4.3 The symmetric tensors of SO(3) . . . . . . . . . . . . . . . . . . . . . . . . 20

4.4 Global solution to first order in derivatives . . . . . . . . . . . . . . . . . . 22

4.5 Stress tensor to first order . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

5 The metric and stress tensor at second order  23

5.1 Solution in the scalar sector . . . . . . . . . . . . . . . . . . . . . . . . . . 27

5.2 Solution in the vector sector . . . . . . . . . . . . . . . . . . . . . . . . . . 29

5.3 Solution in the tensor sector . . . . . . . . . . . . . . . . . . . . . . . . . . 30

5.4 Global solution to second order in derivatives . . . . . . . . . . . . . . . . 31

5.5 Stress tensor to second order . . . . . . . . . . . . . . . . . . . . . . . . . . 32

6 Second order fluid dynamics                   33

6.1 Weyl transformation of the stress tensor . . . . . . . . . . . . . . . . . . . 33

6.2 Spectrum of small fluctuations . . . . . . . . . . . . . . . . . . . . . . . . . 35

6.3 Comparison with Baier et.al. (added in v2) . . . . . . . . . . . . . . . . . . 36

                               1
7 Discussion     37

1 Introduction

The AdS/CFT correspondence provides an important laboratory to explore both gravita-
tional physics as well as strongly coupled dynamics in a class of quantum field theories.
Using this correspondence it is possible to test general lore about quantum field theory in
a non perturbative setting and so learn general lessons about strongly coupled dynamics.
Conversely, it is also possible to use the AdS/CFT duality to convert strongly held convic-
tions about the behaviour of quantum field theories into general lessons about gravitational
and stringy dynamics.

    In this paper we use the AdS/CFT correspondence to study the effective description
of strongly coupled conformal field theories at long wavelengths. On physical grounds it
is reasonable that any interacting quantum field theory equilibrates locally at high enough
energy densities, and so admits an effective description in terms of fluid dynamics. The
variables of such a description are the local densities of all conserved charges together with
the local fluid velocities. The equations of fluid dynamics are simply the equations of local
conservation of the corresponding charge currents, supplemented by constitutive relations
that express these currents as functions of fluid mechanical variables. As fluid dynamics
is a long wavelength effective theory, these constitutive relations are usually specified in a
derivative expansion. At any given order, thermodynamics plus symmetries determine the
form of this expansion up to a finite number of undetermined coefficients. These coefficients
may then be obtained either from measurements or from microscopic computations.

    The best understood examples of the AdS/CFT correspondence relate the strongly
coupled dynamics of certain conformal field theories to the dynamics of gravitational sys-
tems in AdS spaces. In this paper we will demonstrate that Einstein's equations with
a negative cosmological constant, supplemented with appropriate regularity restrictions
and boundary conditions, reduce to the nonlinear equations of fluid dynamics in an ap-
propriate regime of parameters. We provide a systematic framework to construct this
universal nonlinear fluid dynamics, order by order in a boundary derivative expansion.
Our work builds on earlier derivations of linearized fluid dynamics from linearized gravity
by Policastro, Son and Starinets [1] and on earlier examples of the duality between non-
linear fluid dynamics and gravity by Janik, some of the current authors and collaborators
[2, 3, 4, 5] (cf, [6, 7, 8, 9, 10, 11] for related work and extensions and [12, 13] for some recent
work). There is a large literature in deriving linearized hydrodynamics from AdS/CFT,
see [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] for developments in
this area and [32] for a review and comprehensive set of references.

    Our results, together with those of earlier papers referred to above, may be interpreted

              2
from several points of view. First, one may view them as a confirmation that fluid dy-
namics is the correct long wavelength effective description of strongly coupled field theory
dynamics. Second, one could assume the correctness of the fluid description and view our
results as providing information on the allowed singularities of `legal' solutions of gravity.
Finally, our work may be used to extract the values of all coefficients of the various terms
in the expansion of the stress tensor in the fluid dynamical derivative expansion, for the
fluid dual to gravity on AdS5. The universal behaviour of the shear viscosity - a coefficient
of a term in the expansion of the stress tensor to first order in field theory derivatives - in
fluids dual to gravity [24] has already attracted attention and has impacted experimental
analysis of RHIC data [33, 34, 35]. In this paper we work out the universal values of all
coefficients of (nonlinear) two derivative terms stress tensor of the distinguished conformal
fluid dual to gravity on AdS5.

    Consider any two derivative theory of five dimensional gravity interacting with other
fields, that has AdS5 as a solution. Examples of such theories include IIB supergravity
on AdS5 �M where M is any compact five dimensional Einstein manifold with positive
cosmological constant; for example M = S5, T 1,1 and Y p,q for all p, q. The solution space
of such systems has a universal sub-sector; the solutions of pure gravity with a negative
cosmological constant.1 We will focus on this universal sub-sector in a particular long
wavelength limit. Specifically, we study all solutions that tubewise2 approximate black
branes in AdS5, whose temperature and boost velocities vary as a function of boundary
coordinates x� on a length scale that is large compared to the inverse temperature of the
brane. We investigate all such solutions order by order in a perturbative expansion; the
perturbation parameter is the length scale of boundary variation divided by the thermal
length scale. Within the domain of validity of our perturbative procedure (and subject
to a technical assumption), we establish the existence of a one to one map between these
gravitational solutions and the solutions of the equations of a distinguished system of
boundary conformal fluid dynamics. Implementing our perturbative procedure to second
order, we explicitly construct the fluid dynamical stress tensor of this distinguished fluid
to second order in the derivative expansion.

    Roughly speaking, our construction may be regarded as the `Chiral Lagrangian' for
brane horizons. Recall that the isometry group of AdS5 is SO(4, 2). The Poincare algebra
plus dilatations form a distinguished subalgebra of this group; one that acts mildly on
the boundary. The rotations SO(3) and translations R3,1 that belong to this subalgebra
annihilate the static black brane solution in AdS5. However the remaining symmetry gen-

    1Recall that the Einstein frame Lagrangian contains no interaction terms that are linear in the non
gravitational fluctuations.

    2We will work in AdS spacetimes where the radial coordinate r  (0, ) and will refer to the remaining
coordinates x� = (v, xi)  R1,3 as field theory or boundary coordinates. The tubes referred to in the text
cover a small patch in field theory directions, but include all values of r well separated from the black
brane singularity at r = 0; typically r  rh where rh is the scale set by the putative horizon.

                                                         3
erators � dilatations and boosts � act nontrivially on this brane, generating a 4 parameter
set of brane solutions. These four parameters are simply the temperature and the velocity
of the brane. Our construction effectively promotes these parameters to `Goldstone fields'
(or perhaps more accurately collective coordinate fields) and determines the effective dy-
namics of these collective coordinate fields, order by order in the derivative expansion, but
making no assumption about amplitudes. Of course the collective coordinates method has
a distinguished tradition in theoretic physics; see for instance the derivation of the Nambu-
Goto action in [36]. Our paper, which applies these methods to black brane horizons, is
strongly reminiscent of the membrane paradigm of black hole physics, and may perhaps be
regarded as the precise version of this paradigm in its natural setting, i.e., AdS spacetime.

    Seen from inverse point of view, our construction may be regarded as a map from
solutions of the relativistic fluid dynamics equations on R3,1 to the space of long wavelength,
locally black brane, solutions of gravity in AdS5. That is, we present a systematic procedure
to explicitly construct a metric dual to any solution of the equations of the distinguished
fluid dynamics alluded to above. This metric solves the Einstein's equations to a given
order in the derivative expansion (one higher than the order to which the equations of fluid
dynamics were formulated and solved), asymptotes to AdS5 with a boundary stress tensor
equal to the fluid dynamical stress tensor, and is regular away from the usual singularity
of black branes (chosen by convention to be at r = 0).

    As an important physical input into our procedure, we follow [3, 7, 10] to demand
that all the solutions we study are regular away from the r = 0 curvature singularity of
black branes, and in particular at the the location of the horizon of the black brane tubes
out of which our solution is constructed. We present our construction in the analogue
of Eddington-Finklestein coordinates which extend all the way to the future curvature
singularity. Although we have not yet performed a careful global analysis of our solutions, it
seems rather clear that they each possess a regular event horizon that shields the boundary
from this curvature singularity.

    This paper is organized as follows. We begin in � 2 with the basic outline of the
computation expanding on the ideas presented above. In � 3 we outline in detail the logic
and strategy of our perturbative procedure. We then proceed in � 4 to implement our
perturbative procedure to first order in the derivative expansion. In � 5 we extend our
computation to second order in the same expansion. In � 6 we demonstrate the Weyl
invariance of the fluid dynamical stress tensor we obtain, and further use this stress tensor
to compute corrections to the dispersion relation for sound and shear waves in this fluid.
In � 7 we end with a discussion of our results and of future directions.

Note added: After we had completed writing this paper we learnt of related work soon
to appear [37]. The authors of this paper utilize Weyl invariance to constrain the form of
the second order fluid dynamical stress tensor up to 5 undetermined coefficients. They then

                                                         4
use information from linearized gravitational quasinormal mode calculations together with
an earlier computation of Janik and collaborators to determine 3 of these five coefficients.
As far as we have been able to tell, their results are consistent with the full second order
stress tensor (and prediction for quasinormal mode frequencies) presented herein. This is a
nontrivial check of our results. We thank the authors of [37] for sharing their results with
us prior to publication.
Note added in v2: The preprint [37] appeared simultaneously in an arXiv listing with v1
of this paper. In � 6.3 of this updated version of our preprint we have presented a detailed
comparison of our results with those of [37]; where they overlap we find perfect agreement.

2 Fluid dynamics from gravity

We begin with a description of the procedure we use to construct a map from solutions
of fluid dynamics to solutions of gravity. We then summarize the results obtained by
implementing this procedure to second order in the derivative expansion.

    Consider a theory of pure gravity with a negative cosmological constant. With a par-
ticular choice of units (RAdS = 1) Einstein's equations are given by3

      EM N  =  RM N   -        1  gM  N  R  - 6 gMN  =  0        (2.1)
                               2

      = RMN + 4 gMN = 0, R = -20.

    Of course the equations (2.1) admit AdS5 solutions. Another class of solutions to these
equations is given by the `boosted black branes'4

      ds2 = -2 u� dx�dr - r2 f (b r) u� u dx�dx + r2 P� dx�dx ,  (2.2)

with

            f (r)  =  1        -  1
                                  r4
                                  1
               uv =
                                  1 - 2                          (2.3)

               ui =               i         ,

                                  1 - 2

    3We use upper case Latin indices {M, N, � � � } to denote bulk directions, while lower case Greek indices
{�, , � � � } refer to field theory or boundary directions. Finally, we use lower case Latin indices {i, j, � � � }

to denote the spatial directions in the boundary.
    4The indices in the boundary are raised and lowered with the Minkowski metric i.e., u� = � u.

                               5
where    the  temperature  T  =         1  and  velocities  i  are  all  constants   with  2  =    j    j,  and
                                       b

                                                P � = u�u + �                                               (2.4)

is the projector onto spatial directions. The metrics (2.2) describe the uniform black brane
written in ingoing Eddington-Finkelstein coordinates, at temperature T , moving at velocity
 i .5

    Now consider the metric (2.2) with the constant parameter b and the velocities i
replaced by slowly varying functions b(x�), i(x�) of the boundary coordinates.

ds2 = -2 u�(x) dx� dr - r2 f (b(x) r) u�(x) u(x) dx� dx + r2 P� (x) dx� dx . (2.6)

Generically, such a metric (we will denote it by g(0)(b(x�), i(x�)) is not a solution to
Einstein's equations. Nevertheless it has two attractive features. Firstly, away from r = 0,
this deformed metric is everywhere non-singular. This pleasant feature is tied to our
use of Eddington-Finkelstein6 coordinates.7 Secondly, if all derivatives of the parameters
b(x�) and i(x�) are small, g(0) is tubewise8 well approximated by a boosted black brane.
Consequently, for slowly varying functions b(x�), i(x�), it might seem intuitively plausible
that (2.6) is a good approximation to a true solution of Einstein's equations with a regular

event horizon. The main result of our paper is that this intuition is correct, provided the
functions b(x�) and i(x�) obey a set of equations of motion, which turn out simply to be
the equations of boundary fluid dynamics.

    Einstein's equations, when evaluated on the metric g(0), yield terms of first and second
order in field theory (i.e., (xi, v)  x�) derivatives of the temperature and velocity fields.9
By performing a scaling of coordinates to set b to unity (in a local patch), it is possible to
show that field theory derivatives of either ln b(x�) or i(x�) always appear together with a
factor of b. As a result, the contribution of n derivative terms to the Einstein's equations is
suppressed (relative to terms with no derivatives) by a factor of (b/L)n  1/(T L)n. Here L

5 As we have explained above, the 4 parameter set of metrics (2.2) may all be obtained from

                                       ds2 = 2 dv dr - r2 f (r) dv2 + r2 dx2 ,                              (2.5)

with  f  = 1-  1   via  a  coordinate  transform.  The  coordinate  transformations  in  question  are  generated  by
               r4
a subalgebra of the isometry group of AdS5.
6It is perhaps better to call these generalized Gaussian null coordinates as they are constructed with

the aim of having the putative horizon located at the hypersurface r(x�) = rh.
    7A similar ansatz for a black branes in (for instance) Fefferman-Graham coordinates i.e., Schwarzschild

like coordinates respecting Poincar�e symmetry, is singular at r b = 1.

8As explained above, any given tube consists of all values of r well separated from r = 0, but only a

small region of the boundary coordinates x�.

9As g(0) is an exact solution to Einstein's equations when these fields are constants, terms with no

derivatives are absent from this expansion.

                                                        6
is the length scale of variations of the temperature and velocity fields in the neighbourhood
of a particular point, and T is the temperature at that point. Therefore, provided L T  1,
it is sensible to solve Einstein's equations perturbatively in the number of field theory
derivatives.10

    In � 3 we formulate the perturbation theory described in the previous paragraph, and
explicitly implement this expansion to second order in 1/(L T ). As we have mentioned
above it turns out to be possible to find a gravity solution dual to a boundary velocity and
temperature profile only when these fields obey the equation of motion

                               �T � = 0                                              (2.7)

where the rescaled11 stress tensor T � (to second order in derivatives) is given by

       T � =( T )4 (� + 4 u�u) - 2 ( T )3 �

       + (T )2     (ln 2) T2�a + 2 T2�b + (2 - ln 2)  1  T2�c  +  T2�d  +  T2�e      (2.8)
                                                      3

where

       �        =  P �P   (u) -        1  P  �  u
                                       3

       T2�a = (� ) u 

       T2�b     =  �    -   1  P �   
                            3
       T2�c = u �
                                                                                     (2.9)

       T2�d     =  Du�  Du  -  1  P �  Du    Du
                               3
                                             1
       T2�e = P � P  D         (u)        -  3  P �  P   D  ( u )

       � = � u u.

Our conventions are 0123 = -0123 = 1 and D  u and the brackets () around the
indices to denote symmetrization, i.e., a(b) = (ab + ab)/2.

    These constraints are simply the equations of fluid dynamics expanded to second order
in the derivative expansion. The first few terms in the expansion (2.8) are familiar. The
derivative free terms describe a perfect fluid with pressure (i.e., negative free energy den-
sity) 4 T 4, and so (via thermodynamics) entropy density s = 44 T 3. The viscosity  of

  10Note that the variation in the radial direction, r, is never slow. Although we work order by order in
the field theory derivatives, we will always solve all differential equations in the r direction exactly.

  11Throughout this paper T � = 16 G5 t� where G5 is the five dimensional Newton and t� is the
conventionally defined stress tensor, i.e., the charge conjugate to translations of the coordinate v.

                                    7
this fluid may be read off from the coefficient of � and is given by 3 T 3. Notice that
/s = 1/(4), in agreement with the famous result of Policastro, Son and Starinets [1].

    Our computation of the two derivative terms in (2.8) is new; the coefficients of these
terms are presumably related to the various `relaxation times' discussed in the literature
(see for instance [38]). As promised earlier, the fact that we are dealing with a particular
conformal fluid, one that is dual to gravitational dynamics in asymptotically AdS space-
times, leads to the coefficients being determined as fixed numbers. It would be interesting
to check whether the stress tensor determined above fits into the framework of the so called
Israel-Stewart formalism [39] (see [38, 40] for reviews). R. Loganayagam [41] is currently
investigating this issue.

    In � 6.1 we have checked that the minimal covariantization of the stress tensor (2.8)
transforms as T �  e-6 T � under the Weyl transformation �  e2 � , T  e- T ,
u  e- u, for an arbitrary function (x�).12 This transformation (together with the
manifest tracelessness of T �) ensures Weyl invariance of the fluid dynamical equation
(2.7). Note that we have computed the fluid dynamical stress tensor only in flat space.
The generalization of our expression above to an arbitrary curved space could well in-
clude contributions proportional to the spacetime curvature tensor. The fact that (2.8)
is Weyl invariant by itself is a bit of a (pleasant) surprise. It implies that that the sum
of all curvature dependent contributions to the stress tensor must be independently Weyl
invariant.

3 The perturbative expansion

As we have described in � 2, our goal is to set up a perturbative procedure to solve Ein-
stein's equations in asymptotically AdS spacetimes order by order in a boundary derivative
expansion. In this section we will explain the structure of this perturbative expansion, and
outline our implementation of this expansion to second order, leaving the details of com-
putation to future sections.

3.1 The basic set up

In order to mathematically implement our perturbation theory, it is useful to regard b and
i described in � 2 as functions of the rescaled field theory coordinates  x� where  is a
formal parameter that will eventually be set to unity. Notice that every derivative of i
or b produces a power of , consequently powers of  count the number of derivatives. We
now describe a procedure to solve Einstein's equations in a power series in . Consider the

  12R. Loganayagam [41] informs us that he has succeeded in rewriting our stress tensor in a number of
different compact forms, one of which makes its covariance under Weyl transformations manifest.

                                                         8
metric13

          g = g(0)(i, b) +  g(1)(i, b) + 2 g(2)(i, b) + O 3 ,    (3.1)

where g(0) is the metric (2.6) and g(1), g(2) etc are correction metrics that are yet to be

determined. As we will explain below, perturbative solutions to the gravitational equations

exist only when the velocity and temperature fields obey certain equations of motion. These

equations are corrected order by order in the  expansion; this forces us to correct the

velocity and temperature fields themselves, order by order in this expansion. Consequently

we set

          i = i(0) +  i(1) + O 2 ,     b = b(0) +  b(1) + O 2 ,  (3.2)

where i(m) and b(n) are all functions of  x�.
    In order to proceed with the calculation, it will be useful to fix a gauge. We work with

the `background field' gauge

          grr = 0 ,  gr�  u� ,      Tr (g(0))-1g(n) = 0  n > 0.  (3.3)

Notice that the gauge condition at the point x� is given only once we know u�(v, xi). In
other words, the choice above amounts to choosing different gauges for different solutions,
and is conceptually similar to the background field gauge routinely used in effective action
computations for non abelian gauge theories.

3.2 General structure of perturbation theory

Let us imagine that we have solved the perturbation theory to the (n - 1)th order, i.e.,
we have determined g(m) for m  n - 1, and have determined the functions i(m) and b(m)
for m  n - 2. Plugging the expansion (3.1) into Einstein's equations, and extracting the
coefficient of n, we obtain an equation of the form

                     H g(0)(i(0), b(0)) g(n)(x�) = sn.           (3.4)

Here H is a linear differential operator of second order in the variable r alone. As g(n) is
already of order n, and since every boundary derivative appears with an additional power
of , H is an ultralocal operator in the field theory directions. It is important to note that
H is a differential operator only in the variable r and does not depend on the variables x�.
Moreover, the precise form of this operator at the point x� depends only on the values of
i(0) and b(0) at x� but not on the derivatives of these functions at that point. Furthermore,
the operator H is independent of n; we have the same homogeneous operator at every

  13For convenience of notation we are dropping the spacetime indices in g(n). We also suppress the
dependence of b and i on x�.

                                    9
order in perturbation theory.

    The source term sn however is different at different orders in perturbation theory. It
is a local expression of nth order in boundary derivatives of i(0) and b(0), as well as of
(n - k)th order in i(k), b(k) for all k  n - 1. Note that i(n) and b(n) do not enter the nth
order equations as constant (derivative free) shifts of velocities and temperatures solve the

Einstein's equations.
    The expressions (3.4) form a set of 5 � 6/2 = 15 equations. It turns out that four of

these equations do not involve the unknown function g(n) at all; they simply constrain the

velocity functions b and i. There is one redundancy among the remaining 11 equations
which leaves 10 independent `dynamical' equations. These may be used to solve for the 10
unknown functions in our gauge fixed metric correction g(n), as we describe in more detail

below.

3.2.1 Constraint equations

By abuse of nomenclature, we will refer to those of the Einstein's equations that are of
first order in r derivatives as constraint equations. Constraint equations are obtained by
dotting the tensor EMN with the vector dual to the one-form dr. Four of the five constraint
equations (i.e., those whose free index is a � index) have an especially simple boundary
interpretation; they are simply the equations of boundary energy momentum conservation.
In the context of our perturbative analysis, these equations simply reduce to

�T(n�- 1) = 0  (3.5)

where T(n�- 1) is the boundary stress tensor dual the solution expanded up to O (n-1).
Recall that each of g(0), g(1)... are local functions of b, i. It follows that the stress tensor
T(n�- 1) is also a local function (with at most n - 1 derivatives) of these temperature and
velocity fields. Of course the stress tensor T(n�- 1) also respects 4 dimensional conformal
invariance. Consequently it is a `fluid dynamical' stress tensor with n - 1 derivatives, the

term simply being used for the most general stress tensor (with n - 1 derivatives), written
as a function of u� and T , that respects all boundary symmetries.

    Consequently, in order to solve the constraint equations at nth order one must solve
the equations of fluid dynamics to (n - 1)th order. As we have already been handed a

solution to fluid dynamics at order n - 2, all we need to do is to correct this solution to

one higher order. Though the question of how one goes about improving this solution is

not the topic of our paper (we wish only to establish a map between the solutions of fluid

mechanics and gravity, not to investigate how to find the set of all such solutions) a few

words in this connection may be in order. The only quantity in (3.5) that is not already
known from the results of perturbation theory at lower orders are i(n-1) and b(n-1). The

10
four equations (3.5) are linear differential equations in these unknowns that presumably
always have a solution. There is a non-uniqueness in these solutions given by the zero
modes obtained by linearizing the equations of stress energy conservation at zeroth order.
These zero modes may always be absorbed into a redefinition of i(0), b(0), and so do not
correspond to a physical non-uniqueness (i.e., this ambiguity goes away once you specify
more clearly what your zeroth order solution really is).

    Our discussion so far may be summarized as follows: the first step in solving Einstein's
equations at nth order is to solve the constraint equations � this amounts to solving the
equations of fluid dynamics at (n - 1)th order (3.5). As we explain below, while it is of
course difficult in general to solve these differential equations throughout R3,1, it is easy
to solve them locally in a derivative expansion about any point; this is in fact sufficient to
implement our ultralocal perturbative procedure.

3.2.2 Dynamical equations

The remaining constraint Err and the `dynamical' Einstein's equations E� may be used
to solve for the unknown function g(n). Roughly speaking, it turns out to be possible to
make a judicious choice of variables such that the operator H is converted into a decoupled
system of first order differential operators. It is then simple to solve the equation (3.4)
for an arbitrary source sn by direct integration. This procedure actually yields a whole
linear space of solutions. The undetermined constants of integration in this procedure are
arbitrary functions of x� and multiply zero modes of the operator (3.4). As we will see
below, for an arbitrary non-singular and appropriately normalizable source sn (of the sort
that one expects to be generated in perturbation theory14), it is always possible to choose
these constants to ensure that g(n) is appropriately normalizable at r =  and non-singular
at all nonzero r. These requirements do not yet completely specify the solution for g(n), as
H possesses a set of zero modes that satisfy both these requirements. A basis for the linear
space of zero modes, denoted gb and gi, is obtained by differentiating the 4 parameter class
of solutions (2.2) with respect to the parameters b and i. In other words these zero modes
correspond exactly to infinitesimal shifts of i(0) and b(0) and so may be absorbed into a
redefinition of these quantities. They reflect only an ambiguity of convention, and may be
fixed by a `renormalization' prescription, as we will do below.

  14Provided the solution at order n - 1 is non-singular at all nonzero r, it is guaranteed to produce a
non-singular source at all nonzero r. Consequently, the non-singularlity of sn follows inductively. We think
is possible to make a similar inductive argument for the large r behaviour of the source, but have not yet
formulated this argument precisely enough to call it a proof.

                                                        11
3.2.3 Summary of the perturbation analysis

In summary, it is always possible to find a physically unique solution for the metric g(n),
which, in turn, yields the form of the nth order fluid dynamical stress tensor (using the
usual AdS/CFT dictionary). This process, being iterative, can be used to recover the fluid
dynamics stress tensor to any desired order in the derivative expansion.

    In � 3.3 and � 3.4 we will provide a few more details of our perturbative procedure,
in the context of implementing this procedure to first and second order in the derivative
expansion.

3.3 Outline of the first order computation

We now present the strategy to implement the general procedure discussed above to first
order in the derivative expansion.

3.3.1 Solving the constraint equations

The Einstein constraint equations at first order require that the zero order velocity and
temperature fields obey the equations of perfect fluid dynamics

                                    �T(�0) = 0 ,                  (3.6)

where up to an overall constant

T(�0)                            =     1     � + 4 u�(0) u(0)  .  (3.7)
                                    (b(0))4

    While it is difficult to find the general solution to these equations at all x�, in order to
carry out our ultralocal perturbative procedure at a given point y�, we only need to solve

these constraints to first order in a Taylor expansion of the fields b and i about the point
y�. This is, of course, easily achieved. The four equations (3.6) may be used to solve for
the 4 derivatives of the temperature field at y� in terms of first derivatives of the velocity
fields at the same point. This determines the Taylor expansion of b to first order about y�

in terms of the expansion, to first order, of the field i about the same point. We will only
require the first order terms in the Taylor expansion of velocity and temperature fields in
order to compute g(1)(y�).

3.3.2 Solving the dynamical equations

As described in the previous section, we expand Einstein's equations to first order and
find the equations (3.4). Using the `solution' of � 3.3.1, all source terms may be regarded

                                             12
as functions of first derivatives of velocity fields only. The equations (3.4) are then easily
integrated subject to boundary conditions and we find (3.4) is given by

               g(1) = gP(1) + fb(xi, v) gb + fi(xj, v) gi,         (3.8)

where gP(1) is a particular solution to (3.4), and fb and fi are a basis for the zero modes of
H that were described in the � 3.2. Plugging in this solution, the full metric g(0) + g(1),

when expanded to order first order in , is (3.1)

               g = g(0) +  gP(1) + (fb + b(1))gb + (fi + (1))gi ,  (3.9)

where the four functions of x�, fb + b(1), fi + i(1) are all completely unconstrained by the
equations at order .

3.3.3 The `Landau' Frame

Our solution (3.8) for the first order metric has a four function non-uniqueness in it. As
fb and fi may be absorbed into b(1) and i(1) this non-uniqueness simply represents an

ambiguity of convention, and may be fixed by a `renormalization' choice. We describe our

choice below.

Given g(1), it is straightforward to use the AdS/CFT correspondence to recover the

stress tensor. To first order in  the boundary stress tensor dual to the metric (3.9)

evaluates to                 1                       2
                             b4                      b3
               T �        =      (�  +  4  u�u )  -      T(�1)  ,  (3.10)

where

                           b = b(0) + (b(1) + fb)                  (3.11)
                          i = (i(1) + fi)

where T(�1) , defined by (3.10), is an expression linear in x� derivatives of the velocity fields
and temperature fields. Notice that our definition of T(�1) , via (3.10), depends explicitly on
the value of the coefficients fi, fb of the homogeneous modes of the differential equation
(3.4). These coefficients depend on the specific choice of the particular solution gP(1), which is
of course ambiguous up to addition of homogenous solutions. Any given solution (3.8) may

be broken up in many different ways into particular and homogeneous solutions, resulting
in an ambiguity of shifts of the coefficients of fb, fi and thereby an ambiguity in T(�1). It
is always possible to use the freedom provided by this ambiguity to set u(0)� T(�1) = 0.
This choice completely fixes the particular solution gP(1). We adopt this convention for the

                                     13
particular solution and then simply simply set g(1) = gP(1) i.e., choose fb = fi = 0. T(�1) is
now unambiguously defined and may be evaluated by explicit computation; it turns out

that

      T(�1) = � .

    The discussion of the previous paragraph has a natural generalization to perturbation

theory at any order. As the operator H is the same at every order in perturbation theory,
the ambiguity for the solution of g(n) in perturbation theory is always of the form described
in (3.9). We will always fix the ambiguity in this solution by choosing u� T(�k) = 0. The
convention dependence of this procedure has a well known counterpart in fluid dynamics;

it is simply the ambiguity of the stress tensor under field redefinitions of the temperature
and u�. Indeed this field redefinition ambiguity is standardly fixed by precisely the `gauge'
choice u�T(�1) = 0. This is the so called `Landau frame' widely used in studies of fluid
dynamics.15

    We present the details of the first order computation in � 4 below.

3.4 Outline of the second order computation

Assuming that we have implemented the first order calculation described in � 3.3, it is
then possible to find a solution to Einstein's equations at the next order. In this case care
should be taken in implementing the constraints as we discuss below.

3.4.1 The constraints at second order

The general discussion of � 3.2 allows us to obtain the second order solution to Einstein's
equations once we have solved the first order system as outlined in � 3.3. However, we
need to confront an important issue before proceeding, owing to the way we have set up
the perturbation expansion. Of course perturbation theory at second order is well defined
only once the first order equations have been solved. While in principle we should solve
these equations everywhere in R3,1, in the previous subsection we did not quite achieve
that; we were content to solve the constraint equation (3.6) only to first order in the Taylor
expansion about our special point y�. While that was good enough to obtain g(1), in order
to carry out the second order calculation we first need to do better; we must ensure that
the first order constraint is obeyed to second order in the Taylor expansion of the fields
b(0) and i(0) about y�. That is, we require

      �T(�0) (y) = 0.                  (3.12)

  15Conventionally, one writes in fluid mechanics the stress tensor as the perfect fluid part and a dissipative
part i.e., T � = Tp�erfect + Td�issipative. The Landau gauge condition we choose at every order simply
amounts to u� Td�issipative = 0.

      14
    Essentially, we require that T(�0) satisfy the conservation equation (3.6) to order 2 before
we attempt to find the second order stress tensor. In general, we would have need (3.6)

to be satisfied globally before proceeding; however, the ultralocality manifest in our set-up

implies that it suffices that the conservation holds only to the order we are working. If we
were interested in say the nth order stress tensor T(�n) we would need to ensure that the
stress tensor up to order n - 1 satisfies the conservation equation to order O (n-1).

    The equations (3.12) may be thought of as a set of 16 linear constraints on the coeffi-
cients of the (40+78) two derivative terms involving b(0) and i(0). We use these equations
to solve for 16 coefficients, and treat the remaining coefficients as independent. This pro-

cess is the conceptual analogue of our zeroth order `solution' of fluid dynamics at the point
y� (described in the previous subsection), obtained by solving for the first derivatives of

temperature in terms of the first derivatives of velocities. Indeed it is an extension of that
procedure to the next order in derivatives. See � 5 for the details of the implementation
of this procedure. In summary, before we even start trying to solve for g(2), we need to
plug a solution of (3.12) into g(0) + g(1) expanded in a Taylor series expansion about y�.

Otherwise we would be expanding the second order equations about a background that

does not solve the first order fluid dynamics.

3.4.2 Nature of source terms

As we have explained above, the Einstein's equations, to second order, take the schematic

form described in (3.4)

                         H g(0)(i(0), b(0)) g(2) = sa + sb  (3.13)

We have broken up the source term above into two pieces, sa and sb, for conceptual
convenience. sa is a local functional of i(0) and b(0) of up to second order in field theory
derivatives. Terms contributing to sa have their origin both in two field theory derivatives
acting on the metric g(0) and exactly one field theory derivative acting on g(1) (recall that
g(1) itself is a local function of i(0) and b(0) of first order in derivatives). The source term
sb is new: it arises from first order derivatives of the velocity and temperature corrections
i(1) and b(1). This has no analogue in the first order computation.

    As we have explained above, i(0), b(0) are absolutely any functions that obey the equa-
tions (3.6). In particular, if it turns of that the functions i(0) +  i(1) and b(0) +  b(1) obey
that equation (to first order in ) then i(1) and b(1) may each simply be set to zero by an
appropriate redefinition of i(0) and b(i0). This results in a `gauge' ambiguity of the func-
tions i(1), b(1). In our ultralocal perturbative procedure, we choose to fix this ambiguity
by setting i(1) to zero (at our distinguished point y�) while leaving b(1) arbitrary.16

  16 The functions b(i1), i(1) have sixteen independent first derivatives, all but four of which may be fixed
by the gauge freedom. We choose use this freedom to set all velocity derivatives to zero.

                              15
3.4.3 Solution of the constraint equations

With the source terms in place, the procedure to solve for g(2) proceeds in direct imitation
of the first order calculation. The constraint equations reduce to the expansion to order 
of the equation of conservation of the stress tensor

T �  =  1   (4 u�u  +   � )  -  2    1   �  (3.14)
        b4                           b3

with i = (0), b = b(0) +  b(1). These four equations may be used to solve for the four

derivatives �b(1) at x�. Consequently the constraint equations plus our choice of gauge,
uniquely determined the first order correction of the temperature field b(1) and velocity
field i(1) as a function of the zeroth order solution.

    Note that the gauge i(1)(y�) = 0 may be consistently chosen at any one point y�,
but not at all x�. Nonetheless the results for g(2) that we obtain using this gauge will,

when appropriately covariantized be simultaneously applicable to every spacetime point
x�. The reason for this is that all source terms depend on b(1) and i(1) only through the
expansion to order  of �T � = 0 with T � given by (3.14). Note that this source term is
`gauge invariant' (recall that `gauge' transformations are simply shifts of b(1) and i(1) by
zero modes of this equation). It follows that g(2) determined via this procedure does not

depend on our choice of gauge, which was made purely for convenience.

3.4.4 Solving for g(2) and the second order stress tensor

Now plugging this solution for b(1) into the source terms it is straightforward to integrate
(3.13) to obtain g(2). We fix the ambiguity in the choice of homogeneous mode in this
solution as before, by requiring T(�2) u(0) = 0. This condition yields a unique solution for
g(2) as well as for the second order correction to the fluid dynamical stress tensor T(�2),
giving rise to the result (2.9). We present the details of the second order computation in
� 5.

    In the rest of this paper we will present our implementation of our perturbative proce-
dure described above, to first and second order in the derivative expansion.

4 The metric and stress tensor at first order

In this section we will determine the solution, to first order in the derivative expansion. As
we have described in � 3, the equations that determine g(1) at x� are ultralocal; consequently
we are able to solve the problem point by point. It is always possible to choose coordinates
to set u� = (1, 0, 0, 0) and b(0) = 1 at any given point x�. Making that choice, the metric
(2.6) expanded to first order in derivatives in the neighbourhood of x� (chosen to be the

                    16
origin of R3,1 for notational simplicity) is given by

ds(20) = 2 dv dr - r2 f (r) dv2 + r2 dxi dxi

-  2  x�  �i(0)  dxi  dr  -  2 x��i(0)  r2    (1  -  f (r))  dxi  dv  -       4  x�   �b(0)    dv2  .  (4.1)
                                                                                      r2

In order to implement the perturbation programme described in the previous section, we
need to find the first order metric g(1) which, when added to (4.1), gives a solution to
Einstein's equations to first order in derivatives.

    The metric (4.1) together with g(1) has a background piece (the first line in (4.1))
which is simply the metric of a uniform black brane. In addition it has small first derivative
corrections, some of which are known (the second line of (4.1)), and the remainder of which
(g(1)) we have to determine. Now note that the background black brane metric preserves
a spatial SO(3) rotational symmetry. This symmetry allows us to solve separately for the
SO(3) scalars, the SO(3) vector and SO(3) symmetric traceless two tensor (5) components
of g(1) and lies at the heart of the separability of the matrix valued linear operator H into
a set of ordinary linear operators.

    In the following we will discuss each of these sectors separately and determine g(1).
Subsequently, in � 4.4 we present the full solution to order  and proceed to calculate the
stress tensor in � 4.5.

4.1 Scalars of SO(3)

The scalar components of g(1) are parameterized by the functions h1(r) and k1(r) according
to17

                             gi(i1)(r) = 3 r2 h1(r)

                             gv(1v)(r)  =     k1(r)                                                    (4.2)
                                               r2
                             gv(1r)(r) = - 23 h1(r).

Here gi(i1) and gv(1r) are related to each other by our gauge choice T r((g(0))-1g(1)) = 0.
    The scalar Einstein's equations (i.e., those equations that transform as a scalar of

SO(3)) may be divided up into constraints and dynamical equations. The constraint
equations are obtained by contracting Einstein's equations (the first line of (2.1)) with the

17In the spatial R3  R3,1 we will often for ease of notation, avoid the use of covariant and contravariant

indices and adopt a summation convention for repeated indices i.e., gi(i1) =     3    gi(i1).
                                                                                 i=1

                                        17
vector dual to the one form dr. The first scalar constraint is

                                         r2 f (r) Evr + Evv = 0 ,                                (4.3)

which evaluates to                                        ii(0)
                                                            3
                                               v b(0)  =         .                               (4.4)

Below, we will interpret (4.4) as the expansion of the fluid dynamical stress energy conser-

vation, expanded to first order. The second constraint equation,

                                         r2 f (r) Err + Evr = 0 ,                                (4.5)

leads to                                                                            ii(0)
                                                                                      3
                    12  r3  h1(r)  +     (3r4  -  1)  h1 (r)  -  k1 (r)  =  -6  r2         .     (4.6)

To this set of constraints we need add only one dynamical scalar equation,18 the simplest

of which turns out to be

                                         5 h1(r) + r h1(r) = 0 .                                 (4.7)

The LHS of (4.7) and (4.6) are the restriction of the operator H of (3.4) to the scalar

sector. The RHS of the same equations are the scalar parts of the source terms s1. Notice
that H is a first order operator in the variables h1 (r) and k1(r). Consequently the equation
(4.7) may be integrated for an arbitrary source term. The resulting solution is regular at all

nonzero r provided that the source shares this property, and the growth h1(r) at infinity

is slower than a constant � the behaviour of a non normalizable operator deformation

� provided the source in (4.7) grows slower than 1/r at large r. Once h1(r) has been

obtained k1(r) may be determined from (4.6) by integration, for an arbitrary source term.
Once again, the solution will be regular and grows no faster than r3 at large r, provided

the source in that equation is regular and normalizable. The two source terms of this

subsection satisfy these regularity and growth requirements, and it seems clear that this

result will extend to arbitrary order in perturbation theory (see the next section).

The general solution to the system (4.6) and (4.7), obtained by the integration described

above, is

           h1(r)        =   s  +  t   ,        k1(r)   =  2 r3 ii(0)     +  3 r4 s -  t   +u  ,  (4.8)
                                  r4                           3                      r4

where s, t and u are arbitrary constants (in the variable r). In the solution above, the
parameter s multiplies a non normalizable mode (which represents a deformation of the field

  18We have explicitly checked that the equations listed here imply that the second dynamical equation
is automatically satisfied.

                                                       18
theory metric) and so is forced to zero by our boundary conditions. A linear combination of

the pieces multiplied by t and u is generated by the action of the coordinate transformation
r = r (1 + a/r4) and so is pure gauge, and may be set to zero without loss of generality.

The remaining coefficient u corresponds to an infinitesimal temperature variation, and is
forced to be zero by our renormalization condition on the stress tensor u(�0) T� = 0 (see
the subsection on the stress tensor below). In summary, each of s, t, u may be set to zero
and the scalar part of the metric g(1), denoted gS(1), is

    gS(1)    dxdx  =  2  r ii(0) dv2.                (4.9)
                      3

    Two comments about this solution are in order. First note that k1(r) is manifestly
regular at the unperturbed `horizon' r = 1, as we require. Second, it grows at large
r like r3. This is intermediate between the r0 growth of finite energy fluctuations and
the r4 growth of a field theory metric deformation. As g(0) + g(1) obeys the Einstein's

equations to leading order in derivatives, the usual Fefferman-Graham expansion assures
us that the sum of first order fluctuations in g(0) + g(1) must (in the appropriate coordinate
system) die off like 1/r4 compared to terms that appear in the zeroth order metric (this

would correspond to k1(r) constant at infinity). Consequently the unusually slow fall off
at infinity of our metric g(1) must be compensated for by an equal but opposite effect from

a first order fluctuation piece in the second line of (4.1). This indeed turns out to be the

case. While an explicit computation of the boundary stress tensor dual to (4.1) yields a
result that diverges like r3, this divergence is precisely cancelled when we add g(1) above
to the metric, and the correct value of the stress dual to g(0) + g(1) is in fact zero in the
scalar sector, in agreement with our renormalization condition u(0)� T � = 0.

4.2 Vectors of SO(3)

In the vector channel the relevant Einstein's equations are the constraint r2 f (r) Eri+Evi =
0 and a dynamical equation which can be chosen to be any linear combination of the
Einstein's equations Eri = 0 and Evi = 0. The constraint evaluates to

             ib(0) = vi(0) ,                         (4.10)

which we will later interpret as a consequence of the conservation of boundary momentum.

In order to explore the content of the dynamical equation (we choose Eri = 0), it is

convenient to parameterize the vector part of the fluctuation metric by the functions ji(1),

as

    gV(1)  dxdx = 2 r2 (1 - f (r)) ji(1)(r) dv dxi.  (4.11)

             19
The dynamical equation for ji(r) turns out to be

d   1   d   ji(1)(r)  =  -  3                     v i(0).  (4.12)
dr  r3  dr                  r2

The LHS of (4.12) is the restriction of the operator H of (3.4) to the vector sector, and
the RHS of this equation is the projection of s1 to the vector sector. H is of first order in
the variable j(1) (r) and so may be integrated for an arbitrary source term. The resulting
solution is regular and normalizable provided the source is regular and decays at infinity
faster than 1/r. This condition is obeyed in (4.12); it seems rather clear that it will continue
to be obeyed at arbitrary order in perturbation theory (see the next section).

    Returning to (4.12), the general solution of this equation is

ji(1)(r) = vi(0) r3 + ai r4 + ci                           (4.13)

for arbitrary constants ai, ci. The coefficient ai multiplies a non-normalizable metric defor-
mation, and so is forced to zero by our choice of boundary conditions. The other integration
constant ci multiplies an infinitesimal shift in the velocity of the brane. It turns out (see
below) that a nonzero value for ci leads to a nonzero value for T0i which violates our
`renormalization' condition, consequently ci must be set to zero. In summary,

gV(1)  dxdx = 2 r vi(0) dv dxi.                            (4.14)

    As in the scalar sector above, this solution grows by a factor of r3 faster at the boundary
than the shear zero mode. This slow fall off leads to a divergent contribution to the stress
tensor which precisely cancels an equal and opposite divergence from terms in the expansion
of g(0) to first order in derivatives. As we will see below, the full contribution of g(0) + g(1)
to the vector part of the boundary stress tensor is just zero, again in agreement with our
renormalization conditions.

4.3 The symmetric tensors of SO(3)

We now turn to gT(1), the part of g(1) that transforms in the 5, the symmetric traceless two
tensor representation, of SO(3). Let us parameterize our metric fluctuation by

gT(1)  dx dx = r2 i(j1)(r) dxi dxj,                        (4.15)

            20
where ij is traceless and symmetric. The Einstein's equation Eij = 0 yield

                               d     r5   f  (r)  d   i(j1)     = -6 r2 i(j0) ,                     (4.16)
                               dr                 dr

where we have defined a symmetric traceless matrix

                                   i(j0)  =  (ij(0) )  -     1  ij  mm(0)  .                        (4.17)
                                                             3

    The LHS of (4.16) is the restriction of the operator H of (3.4) to the tensor sector, and

the RHS of this equation is the tensor part of the source term s1. Note that H is a first
order operator in the variable i(j1)(r) and so may be integrated for an arbitrary source
term. The solution to this equation with arbitrary source term s(r) is given by (dropping

the tensor indices):                              dx                  x
                                                r f (x) x5
                               (1) = -                                 s(y) dy .                    (4.18)

                                                                    1

Note that the lower limit of the inner integral in (4.18) has been chosen to be unity.

Provided that s(x) is regular at x = 1 (this is true of (4.16) and will be true at every order

in perturbation theory),    x  s(x)  has     a  zero at x = 1.        It follows that the outer integrand
                            1

in (4.18) is regular at nonzero x (and in particular at x = 1) despite the explicit zero in

the factor f (x) in the denominator. The solution for (1) is also normalizable provided the

source is regular and grows at infinity slower than r3. This condition is obeyed in (4.16)

and is expected to continue to be obeyed at arbitrary order in perturbation theory (see the

next section).

    Applying (4.18) to the source term in (4.16) we find that the solution for i(j1) is given

by

                            (gT(1)) dxdx = 2 r2 F (r) i(j0) dxidxj.                                 (4.19)

with

F (r) =         dx      x2 + x + 1  1)    =  1    ln   (1 + r)2(1 + r2)           - 2 arctan(r) +   (4.20)
         r          x(x + 1) (x2 +           4                 r4

At large r it evaluates to

                      (gT(1)) dxdx = 2                 r     -   1    i(j0) dxidxj .                (4.21)
                                                                4 r2

As in the previous subsections, the first term in (4.21) yields a contribution to the stress
tensor that diverges like r3, but precisely cancels the corresponding divergence from first
derivative terms in the expansion of g(0). However the second term in this expansion yields

                                                       21
an important finite contribution to the stress tensor, as we will see below.

Summary of the first order calculation: In summary, our final answer for g(0) + g(1),
expanded to first order in boundary derivatives about y� = 0, is given explicitly as

ds2 = 2 dv dr - r2f (r) dv2 + r2 dxi dxi

   -  2   x�  �i(0)   dr     dxi  -  2  x�  �   i(0)r2(1  -  f (r))  dv  dxi  -  4  x�  �b(0)  dv2    (4.22)
                                                                                        r2
                                          2
   +  2   r2  F (r)   i(j0)  dxi  dxj  +  3  r  ii(0)  dv2  +  2  r  v i(0)  dv  dxi.

    This metric solves Einstein's equations to first order in the neighbourhood of x� = 0
provided the functions b(0) and i(0) satisfy

                                             v b(0)  =   ii(0)                                        (4.23)
                                                           3

                                             ib(0) = vi(0).

4.4 Global solution to first order in derivatives

In the previous subsection we have computed the metric g(1) about x� assuming that
b(0) = 1 and i(0) = 0 at the origin. Since it is possible to choose coordinates to set an
arbitrary velocity to zero and an arbitrary b(0) to unity at any given point (and since our

perturbation procedure is ultralocal), the results of the previous subsection contain enough

information to write down the metric g(1) about any point. A simple way to do this is to

construct a covariant metric19, as a function of u� and b, which reduces to (4.22) when
b(0) = 1 and i(0) = 0. It is easy to check that

ds2 = -2 u� dx�dr - r2 f (b r) u�u dx�dx + r2 P� dx�dx

+  2  r2  b F (b  r)  �  dx�dx         +  2  r  u�u  u      dx�dx    -   r   u      (u u�)  dx� dx ,  (4.24)
                                          3

does the job, up to terms of second or higher order in derivatives. Here we have written
the metric in terms of � defined in (2.9) and the function F (r) introduced in (4.20).
Furthermore, it is easy to check that the metric above is the unique choice respecting the
symmetries (again up to terms of second or higher order in derivatives). It follows that
(4.24) is the metric g(0) + g(1). It is also easily verified that the covariant version of (4.23)

  19By abuse of notation, we will refer to expressions transformation covariantly in the boundary metric
(chosen here to be � ) as covariant. In particular, we are not interested in full bulk covariance as we will
continue to restrict attention to a specific coordinatization of the fifth direction.

                                                     22
is (3.6). We will interpret this as an equation of stress energy conservation in the next
subsection.

4.5 Stress tensor to first order

Given the solution to the first order equations, we can utilize the AdS/CFT dictionary to
construct the boundary stress tensor using the prescription of [42] (see also [43]). For the
metric (4.24) it is not difficult to compute the stress tensor; all we need to do is compute
the extrinsic curvature tensor K� to the surface at fixed r. By convention, we choose the
unit normal to this surface to be outward pointing, i.e. pointing towards the boundary, in
the definition of K�. Using then the definition

T�      =   -2  lim r4  (K�  -  �)  ,                          (4.25)

                r

on our solution (4.24), we find the result is given simply as

T �  =  1   (4 u�u  +   � )  -  2   � .                        (4.26)
        b4                      b3

where � was defined in (2.9) and all field theory indices are raised and lowered with the
boundary metric �. As explained in the introduction, this stress tensor implies that the
ratio of viscosity to entropy density of our fluid is 1/(4). Note that as mentioned previ-
ously, the expression (4.26) is only correct up to first derivative terms in the temperature
(T = 1/b) and velocities.

5 The metric and stress tensor at second order

In order to obtain the metric and stress tensor at second order in the derivative expansion,
we follow the method outlined in � 3 and implemented in detail in � 4 to leading order.
Concretely, we choose coordinates such that i(0) = 0 and b(0) = 1 at the point x� = 0.
The metric g(0) + g(1) given in (4.24) may be expanded to second order in derivatives.
This involves Taylor expanding g(0) to second order and g(1) to first order, the second order
analogue of (4.1). As we have explained in � 3.4, at this stage we also make the substitution
b(0)  b(0) + b(1), and treat b(1) as an order  term, and so retain only those expressions
that are of first derivative order in b(1) (and contain no other derivatives). This process is
straightforward and we will not record the (rather lengthy) resultant expression here. To

                23
this expression we add the as yet undetermined metric fluctuation

g(2)  dxdx  =  -3 h2(r) dv  dr  +  r2  h2(r) dxi  dxi  +  k2(r)  dv2  +  2  ji(2)(r)  dv  dxi  +  r2i(j2)  dxi  dxj .
                                                           r2                 r2
                                                                                                           (5.1)

    We plug this metric into Einstein's equations and obtain a set of linear second order
differential equations that determine h2, k2, ji(2), i(j2). As in the previous section, SO(3)
symmetry ensures that the equations for the scalars h2, k2, the vectors ji(2), and the tensor
i(j2) do not mix. Moreover, as we have explained in � 3, the equations that determine
these unknown functions are identical to their first order counterparts in the homogeneous

terms, but differ from those equations in the sources. As a result, the only new calculation

we have to perform in order to obtain the metric at second order is the computation of the

source terms. Once these terms are available, the corresponding equations may easily be

integrated, as in the previous section.

    Recall that the input metric into Einstein's equations includes terms that arise out
of the Taylor expansion of g(0) + g(1) that have explicit factors of the coordinates x�.

Nonetheless, a very simple argument assures us that the source terms in the equations
that determine g(2) must all be independent of x�. The argument runs as follows: We
have explicitly constructed g(1) in the previous section so that EMN g(0) + g(1) = OMN
where OMN is a local expression constructed out of second order or higher x� derivatives
of velocity and temperature fields. It follows that x� dependence of sources, which may be
obtained by Taylor expanding OMN about x� = 0, occurs only at the three derivative level
or higher. It follows that source terms at the two derivative level have no x� dependence.

Clearly, this argument has a direct analogue at arbitrary order in perturbation theory.
    A crucial input into the argument of the last paragraph was the fact that g(0) + g(1)

satisfies Einstein's equations in a neighbourhood of x� = 0 (and not just at that point).

As we have seen in the previous section, the fact that the energy conservation equation is
obeyed at x� = 0 allows us to express all first derivatives of temperature in terms of first
derivatives of velocities (see (4.10) and (4.4)). In addition, i(0) and b(0) must be chosen
so that (3.12) is satisfied. The sixteen equations (3.12) can be grouped into sets that

transform under SO(3) as two scalars, three vectors and one tensor (i.e., 5). We will now

explain how these constraints may be used to solve for 16 of the independent expressions

of second order in derivatives of velocity and temperature fields.

    In order to do this, let us first list all two derivative `source' terms that can be built
out of second derivatives of b(0) or i(0), or out of squares of first derivatives of i(0). These
expressions may be separated according to their transformation properties under SO(3) as

scalars, vectors and tensors and higher order terms. The higher order pieces will not be

of interest to us. An exhaustive list of these expressions that transform in the 1, 3 or 5 is

                                                  24
given in Table 1.20 We define the vector i as the curl of the velocity i.e.,

1 of SO(3)     3 of SO(3)                         5 of SO(3)

s1  =  1  v2b  v1i  =  1  i v b             t1ij  =  1  i j b  -  1  s3 ij
       b               b                             b            3

s2 = vii       v2i = v2i                    t2ij = (ij)

s3  =  1  2b   v3i = vi                     t3ij = vij
       b

S1 = vi vi     v4i  =  9  j  ji  -  2i      T1ij  =  v i   v j    -     1  S1 ij
                       5                                                3

S2 = i vi      v5i = 2i                     T2ij  =  (i vj)       -  1  S2 ij
                                                                     3

S3 = (ii)2     V1i  =  1  (v  i)(j    j  )  T3ij  =  2 kl(i vk       j )  l   +  2  S2 ij
                       3                                                         3

S4 = i i       V2i = -ijk j vk              T4ij = kk ij

S5 = ij ij     V3i = ij vj                  T5ij  =  i  j  -   1  S4    ij
                                                               3

               V4i = i jj                   T6ij  =  ik  jk    -  1  S5 ij
                                                                  3

               V5i = ij j                   T7ij = 2 mn(i lm jn)

Table 1: An exhaustive list of two derivative terms in made up from the temperature
and velocity fields. In order to present the results economically, we have dropped the
superscript on the velocities i and the inverse temperature b, leaving it implicit that these
expressions are only valid at second order in the derivative expansion.

                             i = ijk j k ,                                                 (5.2)

and the symmetric traceless tensor ij has been previously defined in (4.17).
    As a simple check on the completeness of expressions in Table 1, notice that the number

of degrees of freedom in those of the tabulated expressions that are formed from a product
of two single derivatives is 5 (in the scalar sector), 5 � 3 (in the vector sector), and 7

  20Note that the tensors are symmetric in their indices. The symmetrization as usual is indicated by
parentheses.

                                    25
� 5 in the tensor sector, leading to a total of 55 real parameters. Together with degrees

of freedom from the two 7s and one 9 that can also be formed from the product of two

derivatives (but will play no role in our analysis) this gives 78 degrees of freedom. This

is  in  agreement  with  the   expected      1  � 12 � 13       =78    ways    of  getting  a  symmetric  object
                                             2

from twelve parameters (the first derivatives of the velocity fields). On the other hand, the

genuinely two derivative terms in Table 1 have 3 � 1 + 5 � 3 + 3 � 5 = 33 degrees of freedom

which together with a two derivative term that transforms in the 7 (which however plays

no role in our analysis) is the expected number 40 = 10 � 4 of two derivative terms arising

from temperature and velocity fields.

    Assuming that we have already employed the first order conservation equation (3.6) to

eliminate the first derivatives of b, we have to deal with the constraint equation (3.12) at

the second order. Using the list of second order quantities given in Table 1, it is possible to

show that (3.12) take the form of the following linear relations between these two derivative

terms:

                         s1    =  1  s3  -  S1     +  1  S3  +  1  S4  -    1  S5
                                  3                   9         6           3
                                                   1
                         s2    =  s3  -  S1  +     2  S4  -    S5

                         v1i   =  10  v4i   +   1  v5i   +  1  V1i  -  1  V2i  -   2  V3i
                                  9             9           3          3           3
                                  10            1           2          1           5                      (5.3)
                                  9             9           3          6           3
                         v2i   =      v4i   +      v5i   -     V1i  +     V2i  -      V3i

                         v3i   =  -  1  V4i  +   V5i
                                     3
                                                      1            1
                         t1ij  =  t3ij  +  T1ij    +  3  T4ij  +   4  T5ij  +  T6ij   .

Given these relations we now proceed to analyze the potential source terms arising from
the metric (4.24) at O (2). The analysis, as before, can be done sector by sector � the
computations for the scalar, vector and tensor sectors are given in � 5.1, � 5.2 and � 5.3,
respectively.

                                                         26
5.1 Solution in the scalar sector

Given the general second order fluctuation (5.1), we parameterize scalar components of
g(2) in terms of the functions h2(r) and k2(r) according to

                                    gi(i2)(r) = 3 r2 h2(r)

                                    gv(2v)(r)  =   k2(r)                                        (5.4)
                                                    r2
                                                       3
                                    gv(2r)(r)  =   -   2  h2(r)  .

As we have explained in the � 4.1, the constraint Einstein's equations in this sector are
given by the r and v component of the one-form formed by contracting the Einstein tensor
with the vector dual to the one-form dr. The v component of this constraint, i.e. the
second order expansion of (4.3), evaluates to

                                     1    v  b(1)  =    1    S5     .                           (5.5)
                                    b(0)               b(1)

This equation enables us to solve for the first v derivative of b(1) in terms of two derivative
terms made up of i(0), but imposes no further constraints on b(0), i(0). (5.5) has a simple
physical interpretation; it is simply the time component of the conservation equation for

the stress tensor (4.26), expanded to second order in derivatives. Consequently (5.5) is the

Navier Stokes equation!
    The r component of the constraint, i.e. (4.5), gives us one relation between the functions

h2(r) and k2(r) and their derivatives. As in � 4.1, to this constraint we must add one
dynamical equation. We obtain the following equations

       5 h2 (r) + r h2(r) = Sh(r)                                                               (5.6)
                     k2 (r) = Sk(r)
                            = 12 r3 h2(r) + (3 r4 - 1) h2 (r) + Sk(r) ,

where

       Sh(r)     1    S4   +  1  Wh(r)       S5
                3 r3          2
                                                                                                (5.7)
                   4r                        2r              1  + 2 r4         1
       Sk(r)    -  3   s3  +  2  r  S1    -  9     S3  +        6 r3    S4  +  2  Wk(r)  S5  .

                                                   27
The functions Wh(r) and Wk(r) are given by

    Wh(r) =        4  (r2 + r + 1)2 - 2 (3 r2 + 2r + 1)             F (r)  ,
                   3             r (r + 1)2 (r2 + 1)2

    Wk(r) =        2  4  (r2 + r + 1)    (3 r4 - 1) F (r) - (2r5 + 2r4 + 2r3 - r - 1)              .
                   3                            r (r + 1) (r2 + 1)

As advertised, it is clear that the differential operator acting on the functions h2(r) and
k2(r) is identical to the one encountered in the first order computation in � 4.1. The
equation (5.6) can be explicitly integrated; to do so it is useful to record the leading large
r behaviour of the source term Sh(r):

                         Sh(r)        1     Sh        1      1  S4  +  2  S5      .                   (5.8)
                                      r3              r3     3         3

The first equation in (5.6) can be integrated given this asymptotic value to obtain the
leading behaviour of the function h2(r). One finds

    h2(r)             =  -   1    Sh  +       dx                       Sh(y)  -      1   Sh  .        (5.9)
                            4 r2            r x5                                     y3
                                                              dy y4

                                                          x

The integral expression above can be shown to be of O (r-5) and hence the asymptotic

behaviour of h2(r) is controlled by sh. Given h2(r), one can integrate up the second

equation of (5.6) for k2(r). The leading large r behaviour of the source term Sk(r) is given

by

    Sk(r)  r Sk  r                       -  4  s3  +  2  S1  -  2  S3  -   1  S4  +  7   S5     ,     (5.10)
                                            3                   9          6         3

and hence we have                    r2              
                                     2
                         k2(r)    =      Sk    -       dx (Sk(x) - x Sk) .                            (5.11)

                                                   r

In this case the integral makes a subleading contribution starting at O (r-1). As in � 4.1,

we have chosen the coefficients of homogeneous solutions to this differential equation so as

to ensure normalizability and vanishing scalar contribution to the stress tensor (according

to our renormalization conditions).

                                                      28
5.2 Solution in the vector sector

The analysis of the vector fluctuations at second order mimics the computation described
in � 4.2. The vector fluctuation in g(2) is chosen as described in (5.1) to be

                                  gv(2i) =     ji(2)  .                             (5.12)
                                               r2

Once again, the analysis is easily done by looking at the constraint equations which are
obtained by contracting the tensor EMN with the vector dual to dr. The ith constraint
equation evaluates to

      18 ib(1)  =  5  v4i  +  5 v5i     +  15 V1i        -  15  V2i  -  33  V3i  .  (5.13)
                                                            4           2

This equation allows us to solve for the spatial derivatives of b(1) in terms of derivatives of
i(0) and b(0). (5.13) is simply the expansion to second order in derivatives of the conserva-
tion of momentum of the stress tensor (4.26).

    To complete the solution in the vector channel, we need to solve for j(2)(r), which can

be shown to satisfy a dynamical equation

                      d       1   d     ji(2)  (r)    = Bi(r).                      (5.14)
                      dr      r3  dr

Note that the LHS of this expression has the vector part of the operator H acting on j(2).
Here Bi(r) is the source term which is built out of the second derivative terms transforming
in the 3 of SO(3) given in Table 1.

                      B(r)  =        p(r) B + Bfin              1)                  (5.15)
                                  18 r3 (r + 1) (r2 +

with

      B = 4 (10 v4 + v5 + 3 V1 - 3 V2 - 6 V3)                                       (5.16)
      Bfin = 9 (20 v4 - 5 V2 - 6 V3) ,

and we have introduced the polynomial:

                      p(r) = 2 r3 + 2r2 + 2 r - 3 .                                 (5.17)

Clearly p(r) determines the large r behaviour of the vector perturbation; asymptotically

                                           29
B(r)     1    B.  Hence,   integrating       (5.14)     we  find   that     j(2)(r)  is  given  as
        9 r3

              ji(2)(r)  =  - r2   Bi    +                                 Bi(y)      -   1    Bi     ,            (5.18)
                             36                                                         9 y3
                                                  dx x3           dy

                                              r               x

where once again we have chosen the coefficients of homogeneous modes in order to main-
tain normalizability and our renormalization condition. As with the first order computation
described in � 4.2, the solution (5.18) makes no contribution to the stress tensor of the field
theory.

5.3 Solution in the tensor sector

Finally, we turn to the tensor modes at second order where we shall recover the explicit
form of the second order contributions to the stress tensor. Our task is now to determine
the functions i(j2)(r) in (5.1). As in � 4.3, in the symmetric traceless sector of SO(3) one
has only the dynamical equation given by

                           1d          r5    1  -  1       d    i(j2)(r)    = Aij(r)                              (5.19)
                           2 r dr                  r4      dr

where

       Aij(r) = a1(r)      T1ij  +  1  T4ij   +   t3ij     +  a5(r)   T5ij  +  a6(r)     T6ij  -  1  a7(r)  T7ij
                                    3                                                             4

with the coefficient functions

                           a1(r)  =    3 p(r) + 11      -  3r   F (r)
                                        p(r) + 5

                           a5(r)  =    1   1   +  1
                                       2          r4
                                                                                                                  (5.20)
                                       4   r2  p(r) + 3     r2  -  r  -  1
                           a6(r) =     r2           p(r)    +   5           -  6  r  F  (r)

                           a7(r)  =  2    p(r)  +  1    -  6 r F (r)  .
                                          p(r)  +  5

The functions F (r) and p(r) are defined in (4.20) and (5.17), respectively.
    The desired solution to (5.19) can be found by intergrating the right hand side of the

equation twice and choosing the solution to the homogenous solution such that we retain
regularity21 at r = 1 and appropriate normalizability at infinity. The solution with these

  21We have imposed the requirement that all metric functions are well behaved in its neighbourhood of

                                                        30
properties is                                     dx                   x
                                                r x (x4 - 1)
                           i(j2)(r) = -                                 dy 2 y Aij(y)

                                                                     1

    The quantity of prime interest to us is the leading large r behaviour of i(j2). This can
be inferred from the expressions for the coefficient functions given in (5.20) and evaluates

to

    i(j2)(r)      =   1    -    1  T7ij  +  T6ij  -  1  T5ij
                      r2        2                    4
                                                                                                         (5.21)
                       1              ln 2      1                             ln 2
                  +   2r4       1  -   2        3  T4ij  +  T1ij  +  t3ij  +   4     T7ij  +  T6ij

The leading term here will give a divergent contribution to the stress tensor, which is
necessary to cancel the divergence arising from the expansion of g(0) + g(1) to second order.
The subleading piece in (5.21) is the term that will provide us with the second order stress
tensor. Before proceeding to evaluate the stress tensor we present the full solution to
second order, appropriately covariantized.

5.4 Global solution to second order in derivatives
Consider the following metric

ds2 = -2 u� dx�dr-r2 f (b r) u�u dx�dx +r2 P� dx�dx+3 b2 h2(b r) u� dx�dr+G� dx�dx ,
                                                                                                            (5.22)

where we have defined a symmetric tensor G� by combing the contributions in the field
theory directions from the first and second order metrics g(0) + g(1)

    G� = r2       2 b F (b r) � + b2 �(2)(b r)          +  1   2  r3  u    u�     u  +  k2(b  r)  u�  u
                                                           r2  3                          b2
                                                                                                         (5.23)
                                            1                     1
               +  r2  b2  h2(b  r)  P�   +  r2     -2  r3  Du  +  b2  j(2)(b  r)     P u� .

The covariant expression for �(2) is given by (5.19) with the replacements

    T1ij  (T2d)� ,                    T4ij  (T2c)� ,                 T5ij         �     -  1  P�         (5.24)
    T6ij  (T2b)� ,                    T7ij  2 (T2a)� ,                                     3

                                                                      t3ij  (T2e)� .

r = 1, a regular point in the spacetime manifold. Note that r = 1 will not represent the horizon of our
perturbed solution, but may well lie very near this horizon manifold.

                                                           31
Further, j�(2) given by (5.18) with Bi(r)  B(r), where Bi(r) is given by (5.15) and we
make the following replacements

v4i        9    P   P       ( u)   -     1  P   P     u    - P� P   u�
           5                             3         

v5i  P� P u�                                                                             (5.25)

V1i  u Du ,                     V2i   u Du  ,                       V3i   Du .

Finally, h2(r) and k2(r) are given by (5.9) and (5.11) respectively, and in the functions
Sh(r), Sk(r), Sh and Sk defined in (5.8) and (5.10) we are required to make the replace-
ments

     s3        1    P       b(0)         S1  Du Du ,                S2  � Du�
              b(0)
                                                                                         (5.26)
     S3  (�u�)2 ,
                                   S4  � � ,               S5  � � .

    It may be checked that this metric is the unique (up to terms that differ at third or

higher order in derivatives) covariant expression that reduces to two derivative solution

determined in the previous subsections, in the neighbourhood of any point y� after making
the coordinate change that sets b(0) = 1 and i(0) = 0 at that point. It follows that (5.22)
is the desired metric g(0) + g(1) + g(2).

5.5 Stress tensor to second order

The stress tensor dual to the solution to second order described in � 5.4 can be obtained
by using the standard formula (4.25). To determine the extrinsic curvature at large r, it
suffices to know the asymptotic form of the metric since we are interested in terms that
have a finite limit as we take r  . Consequently, in order to compute the stress tensor it
is sufficient to replace the various functions of r that have appeared in the computation in
� 5.1, � 5.2 and � 5.3 by their large r asymptotics. The stress tensor may the be computed
in a straightforward fashion, yielding

     (T2)vv = (T2)vi = 0 ,

     (T2)ij  =  -   ln 2  T7ij  -  T6ij  +  -1  +    ln 2  t3ij  +  T1ij  +  1  T4ij  .  (5.27)
                     4                                2                      3

The vanishing of (T2)v� is actually guaranteed by our renormalization condition. It is easy
to check that the covariant form of the expression (5.27) is indeed the stress tensor quoted
in (2.8). This result is the main prediction of our fluctuation analysis to second order in
the derivative expansion.

                                                   32
6 Second order fluid dynamics

In the previous section we have derived the precise form of the fluid dynamical stress
tensor dual to gravity on AdS5 including all terms with no more than two derivatives. In
this section we initiate a study of the physics of this stress tensor. In � 6.1 below we will
demonstrate that our stress tensor transforms homogeneously under Weyl transformations.
In � 6.2 we compute the dispersion relation for low frequency sound and shear waves that
follows from our stress tensor. In � 6.3 we compare our predictions for the transport
coefficients at second order with those of [37].

6.1 Weyl transformation of the stress tensor

Thus far we have extracted the stress tensor for a conformal fluid in flat space R3,1. We
would like to ensure that the second order stress tensor we have derived transforms homo-
geneously under Weyl rescaling. In order to check this we perform the obvious minimal
covariantization of our stress tensor to generalize it to a fluid stress tensor about an arbi-
trary boundary metric g�.22 and study its Weyl transformation properties.

    Consider the Weyl transformation of the boundary metric

g� = e2 g�  g� = e-2g�                     (6.1)

& u� = e- u� ,  T = e-T .

    It is well known that the first order truncation of the stress tensor (2.8) transforms as
T � = e-6  T � under this transformation (see for instance Appendix D of [44]). We pro-
ceed to show that this transformation rule holds for the two derivative stress tensor as well.
This transformation property, together with the tracelessness of the stress tensor, ensures
Weyl invariance of the fluid dynamical equations �T �, appropriate for a conformal fluid.

    It follows from (6.1) that P � = g� + u�u = e-2 P �. The Christoffel symbols
transform as [44]

                              � = � +  � + �  - g� g  .

The transformation of the covariant derivative of u� is given by

�u = �u + � u = e- � u + � u  - g� u g  .  (6.2)

This equation can be used to derive the transformation of various quantities of interest in

  22All metrics in this subsection refer to the metric on the boundary, i.e.., the background spacetime on
which the fluid is propagating.

33
fluid dynamics, such as the acceleration a�, shear �, etc..

                    = �u� = e- �u� + 3 u  = e-  + 3 D ,

                   a = Du = u��u = e-2 a + P   ,                                                             (6.3)

                 �  =  P (�u)         -  1   P � u            =  e-3   � ,
                                         3

                   � = u � u = e-2 �

where in the last equation we have accounted for the fact that all epsilon symbols in (2.9)

should be generalized in curved space to their                covariant     counterparts.  The      objects  witgh,
correct tensor transformation properties scale                as metric     determinants   i.e.,     

and   1g , from which it is easy to infer their scaling behaviour under conformal

transformations; in particular,  = e4  and  = e-4  .

The Weyl transformation of the two derivative terms that occur in the stress tensor

(2.9) is given by

                   TA� = e-4 TA� ,                                  for A = {2a, 2b}                         (6.4)
                                                                    for B = {2c, 2d, 2e}
                   TB� = e-4         TB�   +         �     ,

                                               T B

where the inhomogeneous terms arising in the Weyl transformation are:

T2�c  = 3 D        (�u)   +  u(�  a)  -   1    P �
                                          3

T2�d   =  2 a(�  )  +  2 u(�  a)  D     -   2  a  
                                            3
                                                        1                                     1
          + 2 u(� ) D + u� u               (D)2      -  3  P �   (D)2       + �  -            3  P  �    

T2�e   =  -(�u)     D  -  3  u(�a)   D     +   1  P �     D      -  2  a(�  )  +  2  P �   a     
                                               3                                  3
                              1                                                            1
          -  u�    u (D)2  +  3   P  �  (D)2      -  2  u(�   )     D       -  �     +     3  P �      

                                                                                                             (6.5)

    While the conformal transformation involves the inhomogeneous terms presented in
(6.5) we need to ensure that the full stress tensor is Weyl covariant. Satisfyingly, these
inhomogeneous terms cancel among themselves in the precise combination that occurs in
(2.8); consequently the linear combination of terms that occurs in the stress tensor trans-
forms covariantly. Note that the cancelation of inhomogeneous terms depends sensitively
on the ratio of coefficients of T2c, T2d and T2e; and so provides a check of our results. Note

                                                     34
however that T2a and T2b are separately Weyl covariant. In summary, our result for the
two derivative stress tensor is a linear combination (with precisely determined coefficients)
of three independently Weyl covariant forms, with scaling weight -4 (for upper indices).

    Using the transformation of the temperature (6.1) it follow that the full stress tensor
transforms under Weyl transformation as

                   T � = e-6 T � .                                        (6.6)

R. Loganayagam [41] informs us that he has found a compact way of rewriting our stress
tensor T � (2.8) that makes the Weyl invariance of each of its three pieces manifest.

6.2 Spectrum of small fluctuations

Consider a static bath of homogeneous fluid at temperature T . Given the two derivative
stress tensor derived above (2.9), it is trivial to solve for the spectrum of small oscillations
of fluid dynamical modes about this background. As the background is translationally
invariant, these fluctuations can be taken to have the form

              i(v, xj) = i ei  v+i kjxj                                   (6.7)
              T (v, xj) = 1 + T ei  v+i kjxj

Plugging (6.7) into the equations of fluid dynamics (2.7), and working to first order in
i and T , these equations reduce to a set of four homogeneous linear equations in the
amplitudes i and T . The coefficients of these equations are functions of  and ki. These
equations have nontrivial solutions if and only if the matrix formed out of these coefficient
functions has zero determinant. Setting the determinant of the matrix of coefficients to
zero one can find the following two dispersion relations:

Sound mode :  (k)  =  � k      +  i k2  �  (3 -ln 4)   k3  +   O   k4  ,  (6.8)
                           3       6         24 3

Shear mode :  (k)     =  i k2  +  i     (2 - ln 2)     k4 + O  k6  ,      (6.9)
                          4       32

where we have defined the rescaled energy and momenta

              =          ,        k=     k  .                             (6.10)
                   T                    T

    It would be interesting to check our prediction against the quasinormal mode analysis
of [25].

                            35
6.3 Comparison with Baier et.al. (added in v2)

In this subsection we compare our results with those of the preprint [37] which appeared

in an arXiv listing simultaneously with the first version of this paper. Where our results

overlap we find perfect agreement.
    The authors of [37] demonstrated that conformal invariance determines the two deriva-

tive fluid dynamical stress tensor of any conformal field th eory to upto five parameters

(see also [41] for an alternate derivation of this result). The five undetermined parameters

are the coefficients of the various Weyl invariant two derivative expressions built out of

velocity. These coefficients which are named ,  and 1,2,3 by [37], are defined via the

equation23

                  T(�2) = ~  T1� +  T2� + ~1 T3� + ~2 T4� + 3 T5� ,                         (6.11)

with24

                  T1� =        D�   +  1   �         1  T2�c  + T2�d  + T2�e  ,
                                       3             3

                  T2� = R � - 2 R �  u u ,

                  T3� =  �   T2�b ,                                                         (6.12)

                  T4�  =         �        1  T2�a
                                          2

                  T5� =  �  .

Here the quantities  and  are defined previously (6.3) and � = -P � P  [u] is the
antisymmetric two tensor built from velocity derivatives. In (6.12) we have also reexpressed
the operators T1�, � � � , T5� of [37] as linear combinations of the tensors we have used in
our paper. These relations are easy to verify given the definitions (2.9) and (6.3).

    The analysis of [37] was able to determine three of the five coefficients above. Specifi-

cally, for N = 4 Yang Mills they find:

            ~  =  2 - ln 2  ,    =           ,       ~1    =  2  ,       =          N2  T3  (6.13)
                    T                  T                      T                  8

The coefficients 2 and 3 were undetermined by their analysis. Translating the results
of our paper for the second order stress tensor into the language of this subsection and

23Note that � as defined in (2.9) differs from that of [37] by a factor of 2 and we define � = -�.

We have introduced the tilded quantities ~ etc., to account for the normalization difference. We have
~ = 2 , ~1 = 4 1 and ~2 = -2 2.

  24We have used the notation of [37] to indicate the symmetric, transverse tracelessness; for any two

tensor F �                                              1
                                                        3
                            F �  =  P �  P   F()     -     P �  P   F

                                                36
reinstating the overall normalization25 we find

~                 =     2 - ln 2  ,  ~1  =  2       ,   ~2  =  2  ln 2  ,       3 = 0.              (6.14)
                          T                 T                    T

As the coeffient  does not enter the equations of fluid dynamics in flat space, our analysis
leaves this coefficient undetermined.

    In summary our results for  and 1 are in agreement with those of [37]. Putting
together the results of our paper with the value of  determined in [37] we have a pre-
diction for the full two fluid dynamical stress tensor of a conformal fluid dual to gravity,
propagating on an arbitrary curved background.

    We can also directly compare the dispersion relations presented in the previous subsec-
tion with those obtained in [37]. Our sound wave dispersion relation (6.8) agrees with the
direct computation of quasinormal modes presented in [37]. The shear mode dispersion
relation of the previous subsection also agrees with the direct quasinormal mode analysis
of [37] upto the order that it should, i.e.. upto terms of order k3. Note that the k4 con-
tribution to the dispersion of the shear quasinormal mode of [37] does not agree with the
coefficient of k4 in (6.9), but (as explained in [37]) there is no reason that it should. As
terms of order k4 are two orders subleading compared to terms of order k2 (the order at
which the first order stress tensor contributes to the shear quazinnormal mode) the coef-
ficient of k4 in the shear quasinormal mode potentially receives contributions from third
order terms in the fluid dynamics stress tensor that we have not accounted for in (6.9).

7 Discussion

We have demonstrated how to start from a general, stationary black brane solution de-
scribing perfect fluid dynamics and promote the parameters in the gravitational solution to
physical fluctuation modes. This procedure allows us to set up a fluctuation analysis which
can be used to extract the boundary stress tensor of fluids dual to gravity in asymptotically
AdS5 spacetimes, in a derivative expansion. Our procedure is ultralocal: we obtain our
solution by patching together local tubes of the black brane solution into a global solution
of Einstein's equations. The fact that our solutions tubewise approximate black branes
(see [3, 7, 10] for related observations) is the gravitational analogue of the fact that the
fluid dynamics approximation only works when the fluid is in local equilibrium. We find
this structure of our solutions quite fascinating and feel that it might have the potential
to teach us important lessons about black brane dynamics.

25Recall that in  writing  (2.9) we  scaled out an  overall factor of 16  GN ,  which evaluates to  N2  for
                                                                                                    82
N = 4 SYM. The value for any other conformal field theory with gravitational dual is simply determined

by the central charge.

                                                    37
    Equation (2.9) is a prediction for the stress tensor of all four dimensional conformal flu-
ids that admit a dual gravitational description. As we have described in the introduction,
there exists an infinite number of examples of conformal field theories with a gravitational
dual that differ substantially in their field content, spectrum of operators, etc. Nonethe-
less, up to an overall normalization, each of these theories has the same fluid dynamical
expansion! Consequently, the fluid dynamics described in this paper has a degree of uni-
versality associated with it. At the one derivative level, the fluid stress tensor has a single
undetermined parameter - the shear viscosity. The value of  that we find is in agreement
with earlier work, /s = 1/(4 ). This relationship has been shown to have a larger degree
of universality than is apparent from our work; it applies to all field theories, whether
conformal or not, that have a gravitational dual. This relationship has also been conjec-
tured to act as a lower bound on the viscosity of a relativistic field theory. It would be
interesting to investigate whether any of the new two derivative coefficients we have found
in this paper display extended universality features and also whether they are sensitive
to higher derivative terms as discussed recently for the shear viscosity to entropy ratio in
[45, 46].

    As we have remarked in � 2, it would be interesting to investigate whether our result
for the stress tensor is consistent with the so called Israel-Stewart formulation of fluid
dynamics [41], a framework that has been employed in several practical investigations of
fluid flows.

    Relatedly, we note that recent claims [47] that the RHIC plasma violate the viscosity
to entropy bound referred to above are based on the analysis of RHIC plasma flows using
first order fluid dynamics. However, a satisfactory analysis of these flows should include
contributions from higher order terms in the fluid dynamical expansion. It is possible that
the stress tensor derived in this paper will be useful in this regard.26

    It may be possible to use the formalism presented in this paper to obtain a better
understanding of the formal structure of the fluid dynamical expansion of quantum field
theories. In this context it is useful to recall that the spectrum of regular small oscillations
about a uniform black brane hosts an infinite spectrum of quasinormal modes. In this
paper we have effectively constructed the `chiral Lagrangian' corresponding to those of
the quasinormal fluctuations that are Goldstone modes (and so have zero frequency when
at zero k). The remaining quasinormal modes played no role in our analysis, as they
are nonperturbatively massive in the inverse temperature (  T = 1/b). The existence
of these non perturbative modes probably implies that the fluid dynamical expansion is
asymptotic rather than convergent, and might allow us to predict the location of the first
singularity in the Borel transform of this perturbation series.

    Recall that metric fluctuation, for any asymptotically AdS5 solution to Einstein's equa-

  26We thank O. Aharony for this suggestion.

                                                        38
tions, decays at large r like 1/r4 relative to the background. The coefficients of this 1/r4
decay are functions of the four field theory coordinates x�; in a particular gauge these
functions may be identified with the 9 components of the traceless boundary stress tensor.
This stress tensor is constrained to obey the equations of energy momentum conserva-
tion, but is otherwise unconstrained by local analysis. The Fefferman-Graham [48] method
(or equivalently the formalism of holographic renormalization, see [49, 50] for reviews)
demonstrates that any such conserved stress tensor, regarded as a boundary condition to
Einstein's equations, leads to a unique and well defined power series expansion (in 1/r) of
an asymptotically AdS metric. Local analysis near the boundary thus appears to indicate
that the space of solutions to Einstein's equations in AdS space is parameterized by the
set of all conserved energy momentum tensors in four dimensions. This would be very
surprising from the dual field theory viewpoint, as a set of four equations does not define
a well posed initial value problem for nine functions.

    The results of our paper suggest a (perhaps not unanticipated) resolution to this puzzle.
In the derivative expansion in which we work, all except a four function set of this naive
nine function class of metrics are unacceptably singular and so do not constitute a legal
solution to Einstein's equations. Generic data result in singularities that develop at a finite
value of r (r = 1/b in our set up) and so are not easily visible in the Fefferman-Graham
expansion, which is guaranteed to work only in an open neighbourhood of the boundary.
The class of boundary stress tensors that generate acceptable metrics are parameterized
by four functions (i(x�) and b(x�)) rather than nine. These four functions are further
constrained to obey the four equations of stress energy conservation. As four equations
constitute a well defined27 initial value problem for a set of four functions, the set of
legal solutions to Einstein's equations are parameterized by data that consists of functions
of 3 spatial rather than 4 spacetime boundary variables, in agreement with field theory
expectations. It would of course be of very great interest to understand how these results
of the previous paragraph generalize beyond the boundary derivative expansion.

    In this context it is also relevant to note that the equations of fluid dynamics themselves
develop singularities under certain situations. It would be interesting to investigate the
gravitational dual of this process of singularity formation.28 More generally, the map
from solutions of fluid dynamics to solutions of gravity could allow one to use the insight
gained from the hundred year long study of the equations of fluid dynamics to understand
qualitatively new gravitational solutions. For example, one might hope to learn about
stationary inhomogeneous brane solutions (analogous to those discovered in the study

  27Note that our notion of a well posed PDE system is simply that we do not have an under-constrained
system of equations. We are not making any claim regarding the well posedness of generic initial data; only
initial data in the regime of our perturbation analysis together with the boundary conditions is guaranteed
to lead to regular solutions. The general question of global regularity of Navier-Stokes equation is of course
an interesting open problem.

  28We thank D. Berenstein for discussions on this question.

                                                        39
of Gregory-Laflamme instabilities of black strings and branes) using the fluid dynamical
description.

    As we have described, in this paper we have derived explicit formulae for the metric dual
to any solution of the Navier-Stokes equations. We have not yet investigated the global
structure of the resulting spacetime. It seems very plausible that (under suitable physical
conditions) the spacetimes we have constructed have regular event horizons. The event
horizon is a null surface; we expect it to closely approximate29 the surface r b(x�) = 1.
If this is the case we should be able to compute an explicit expression for this surface
order by order in perturbation theory. It may then be possible to use our understanding
of the horizon to define a locally positive divergence entropy current (a `pullback' of the
one-form dual to the natural null generators of the horizon back to the boundary might
play a role in such a construction). In the most optimistic scenario such an exercise could
relate classic results about the positivity of null congruence expansions (resulting from the
Raychaudhuri's equation with the usual proviso of energy conditions) to the local positivity
of entropy production in fluid dynamics; a result that would be of obvious interest. The
language of dynamical horizons30 [51] may well prove to be the appropriate framework for
such a discussion. We hope to return to this intriguing issue in the future.

    Recall that the construction presented in this paper yields the gravitational dual of
every solution of the equations of fluid dynamics. Standard field theory lore asserts that
generic field theory evolutions are well described by solutions to the equations of fluid
dynamics in the regime of interest to this paper. Consequently the AdS/CFT correspon-
dence seems to imply that the construction described here yields the generic legal solution
of gravity in AdS5, within its domain of applicability. If our guess of the previous para-
graph is correct � i.e., if all our solutions possess a regular event horizon that shield the
boundary from the singularity � then our results appear to be of relevance to the cosmic
censorship conjecture [52, 53]. However we emphasize that our analysis applies only in a
long wavelength expansion, and so presumably does not apply to several classes of scenarios
that putatively violate this conjecture. More physically, fluid dynamics applies only under
the assumption of local thermal equilibrium. Presumably naked singularities (if they exist)
are dual to `far from local equilibrium' boundary physics.

    Several other natural generalizations of the work presented in this paper immediately
suggest themselves. First, the results of our paper are likely to have an analogue for d
dimensional gravitational theories with a negative cosmological constant for every d  4.
Second, it should be possible to extend the results of our paper to spaces that asymptote
to AdSd+1 in global coordinates (and whose dual description is, therefore, fluid dynamics

  29We would like to thank H. Reall for many useful discussions on this point.
  30Note that the homogeneous spacetime background being simply the uniform black brane, has a trapped
surface; under the fluctuations we generically expect the trapped surface to be generated earlier in the
radial evolution i.e., at a larger radial coordinate (assuming of course appropriate energy conditions).

                                                        40
on Sd-1 � Rt). More ambitiously, it may be possible to extend the results of our work to
field theories whose spacetime metric asymptotes to

ds2  =  dr2  +  r2  ds2bdy
        r2

for a more general class of metrics ds2bdy. In particular, the generalization to time dependent
metrics would permit the study of the gravitational dual of forced fluids, a subject of
interest to the study of turbulence. Finally, it should not be difficult to generalize our
study to two derivative theories of gravity interacting with gauge fields. We expect that
the dual description of such a system will be the fluid dynamics of a system with a number
of additional conserved charges (equal to the number of commuting vector fields). Note
however that unlike the uncharged system, this charged fluid dynamics will not be universal
at nonlinear order, as gauged supergravities do not in general admit a consistent truncation
to the Einstein-Maxwell sector. For instance couplings of the form f ()F�F �, for an
arbitrary scalar field , constitute a source for ; this is an effect that plays an important
role in studies of the attractor mechanism.

    Despite this non universality, IIB supergravity on AdS5 �S5 (for instance) should be
dual to a completely well defined charged fluid dynamics. It would be of interest to use
the methods of this paper determine the form of this fluid dynamical stress tensor. Among
other things, this exercise would allow us to zero in on the origin of the worrying apparent
discrepancy between the formulas of charged black hole thermodynamics and the formulas
of fluid dynamics, as reported in [5].

    It should prove relatively straightforward to generalize the study of this paper to the
fluid dynamics of non conformal backgrounds of gravity. For example, Scherk-Schwarz
compactifications of AdS spaces yield a particularly simple set of gravitational backgrounds
dual to confining gauge theories. Indeed, a moment's thought is enough to convince oneself
that the deconfined phase fluid dynamical stress tensor of the 2+1 dimensional confining
gauge theory (dual to Scherk-Schwarz compactified N = 4 Yang Mills) is simply the
dimensional reduction of the stress tensor of d = 4, N = 4 Yang Mills (i.e., the stress tensor
presented in this paper, (2.8)) plus a constant additive piece. This seemingly trival additive
piece is physically very important; it leads to qualitatively new phenomena. For instance,
[54, 55] have plasmaballs and plasmarings; static finite lumps of fluid with a boundary. Such
configurations have qualitatively new classes of excitations; localized collective coordinates
associated with fluctuations of the boundary. These new collective coordinates will interact
with those studied in this paper. If it proves to be technically possible, it would be
fascinating to formulate and study the resulting dynamics.

        41
Acknowledgements

It is a pleasure to thank R. Loganayagam, H. Reall and T. Wiseman for collaboration
at the initial stages of this project, and for several invaluable comments and discussions
throughout its execution. We thank the authors of [37] for sharing their results with us
prior to publication. We would like to thank P. Basu, D. Berenstein, R. Gopakumar,
S. Gupta, M. Headrick, H. Liu, J. Lucietti, G. Mandal, S. Trivedi, S. Wadia and all the
students in the TIFR theory room for useful discussions. We would also like to thank
O. Aharony, R. Gopakumar, S. Lahiri, N. Seiberg, A. Strominger, M. Van Raamsdonk,
S. Wadia and T. Wiseman for comments on an advance version of this manuscript. We
would also like to thank M. Headrick for his excellent Mathematica package for performing
gravity computations. VH, SM and MR would like to thank the Issac Newton Institute,
Cambridge for hospitality during the workshop, "Strong Fields, Strings and Integrability"
where this project was initiated. VH and MR are supported in part by STFC. The work
of SM was supported in part by a Swarnajayanti Fellowship. Two of us (SB and SM) must
also acknowledge our debt to the steady and generous support of the people of India for
research in basic science.

References

 [1] G. Policastro, D. T. Son, and A. O. Starinets, "The shear viscosity of strongly
      coupled N = 4 supersymmetric Yang-Mills plasma," Phys. Rev. Lett. 87 (2001)
      081601, hep-th/0104066.

 [2] R. A. Janik and R. Peschanski, "Asymptotic perfect fluid dynamics as a consequence
      of AdS/CFT," Phys. Rev. D73 (2006) 045013, hep-th/0512162.

 [3] R. A. Janik and R. Peschanski, "Gauge / gravity duality and thermalization of a
      boost- invariant perfect fluid," Phys. Rev. D74 (2006) 046007, hep-th/0606149.

 [4] S. Nakamura and S.-J. Sin, "A holographic dual of hydrodynamics," JHEP 09
      (2006) 020, hep-th/0607123.

 [5] S. Bhattacharyya, S. Lahiri, R. Loganayagam, and S. Minwalla, "Large rotating AdS
      black holes from fluid mechanics," arXiv:0708.1770 [hep-th].

 [6] S.-J. Sin, S. Nakamura, and S. P. Kim, "Elliptic flow, Kasner universe and
      holographic dual of RHIC fireball," JHEP 12 (2006) 075, hep-th/0610113.

 [7] R. A. Janik, "Viscous plasma evolution from gravity using AdS/CFT," Phys. Rev.
      Lett. 98 (2007) 022302, hep-th/0610144.

                                                        42
 [8] J. J. Friess, S. S. Gubser, G. Michalogiorgakis, and S. S. Pufu, "Expanding plasmas
      and quasinormal modes of anti-de Sitter black holes," JHEP 04 (2007) 080,
      hep-th/0611005.

 [9] K. Kajantie and T. Tahkokallio, "Spherically expanding matter in AdS/CFT," Phys.
      Rev. D75 (2007) 066003, hep-th/0612226.

[10] M. P. Heller and R. A. Janik, "Viscous hydrodynamics relaxation time from
      AdS/CFT," Phys. Rev. D76 (2007) 025027, hep-th/0703243.

[11] K. Kajantie, J. Louko, and T. Tahkokallio, "Gravity dual of 1+1 dimensional
      Bjorken expansion," Phys. Rev. D76 (2007) 106006, arXiv:0705.1791 [hep-th].

[12] P. M. Chesler and L. G. Yaffe, "The stress-energy tensor of a quark moving through
      a strongly-coupled N=4 supersymmetric Yang-Mills plasma: comparing
      hydrodynamics and AdS/CFT," arXiv:0712.0050 [hep-th].

[13] P. Benincasa, A. Buchel, M. P. Heller, and R. A. Janik, "On the supergravity
      description of boost invariant conformal plasma at strong coupling,"
      arXiv:0712.2025 [hep-th].

[14] C. P. Herzog, "The hydrodynamics of M-theory," JHEP 12 (2002) 026,
      hep-th/0210126.

[15] G. Policastro, D. T. Son, and A. O. Starinets, "From AdS/CFT correspondence to
      hydrodynamics. II: Sound waves," JHEP 12 (2002) 054, hep-th/0210220.

[16] G. Policastro, D. T. Son, and A. O. Starinets, "From AdS/CFT correspondence to
      hydrodynamics," JHEP 09 (2002) 043, hep-th/0205052.

[17] D. T. Son and A. O. Starinets, "Minkowski-space correlators in AdS/CFT
      correspondence: Recipe and applications," JHEP 09 (2002) 042, hep-th/0205051.

[18] C. P. Herzog and D. T. Son, "Schwinger-Keldysh propagators from AdS/CFT
      correspondence," JHEP 03 (2003) 046, hep-th/0212072.

[19] C. P. Herzog, "The sound of M-theory," Phys. Rev. D68 (2003) 024013,
      hep-th/0302086.

[20] P. Kovtun, D. T. Son, and A. O. Starinets, "Holography and hydrodynamics:
      Diffusion on stretched horizons," JHEP 10 (2003) 064, hep-th/0309213.

[21] A. Buchel and J. T. Liu, "Universality of the shear viscosity in supergravity," Phys.
      Rev. Lett. 93 (2004) 090602, hep-th/0311175.

                                                        43
[22] A. Buchel, J. T. Liu, and A. O. Starinets, "Coupling constant dependence of the
      shear viscosity in N=4 supersymmetric Yang-Mills theory," Nucl. Phys. B707 (2005)
      56�68, hep-th/0406264.

[23] A. Buchel, "On universality of stress-energy tensor correlation functions in
      supergravity," Phys. Lett. B609 (2005) 392�401, hep-th/0408095.

[24] P. Kovtun, D. T. Son, and A. O. Starinets, "Viscosity in strongly interacting
      quantum field theories from black hole physics," Phys. Rev. Lett. 94 (2005) 111601,
      hep-th/0405231.

[25] P. K. Kovtun and A. O. Starinets, "Quasinormal modes and holography," Phys. Rev.
      D72 (2005) 086009, hep-th/0506184.

[26] P. Benincasa, A. Buchel, and A. O. Starinets, "Sound waves in strongly coupled
      non-conformal gauge theory plasma," Nucl. Phys. B733 (2006) 160�187,
      hep-th/0507026.

[27] K. Maeda, M. Natsuume, and T. Okamura, "Viscosity of gauge theory plasma with
      a chemical potential from AdS/CFT," Phys. Rev. D73 (2006) 066013,
      hep-th/0602010.

[28] J. Mas, "Shear viscosity from R-charged AdS black holes," JHEP 03 (2006) 016,
      hep-th/0601144.

[29] O. Saremi, "The viscosity bound conjecture and hydrodynamics of M2-brane theory
      at finite chemical potential," JHEP 10 (2006) 083, hep-th/0601159.

[30] D. T. Son and A. O. Starinets, "Hydrodynamics of R-charged black holes," JHEP
      03 (2006) 052, hep-th/0601157.

[31] P. Benincasa, A. Buchel, and R. Naryshkin, "The shear viscosity of gauge theory
      plasma with chemical potentials," Phys. Lett. B645 (2007) 309�313,
      hep-th/0610145.

[32] D. T. Son and A. O. Starinets, "Viscosity, Black Holes, and Quantum Field Theory,"
      arXiv:0704.0240 [hep-th].

[33] E. Shuryak, "Why does the quark gluon plasma at RHIC behave as a nearly ideal
      fluid?," Prog. Part. Nucl. Phys. 53 (2004) 273�303, hep-ph/0312227.

[34] E. V. Shuryak, "What RHIC experiments and theory tell us about properties of
      quark-gluon plasma?," Nucl. Phys. A750 (2005) 64�83, hep-ph/0405066.

                                                        44
[35] E. V. Shuryak, "Strongly coupled quark-gluon plasma: The status report,"
      hep-ph/0608177.

[36] J.-L. Gervais and B. Sakita, "Quantized relativistic string as a strong coupling limit
      of the Higgs model," Nucl. Phys. B91 (1975) 301.

[37] R. Baier, P. Romatschke, D. T. Son, A. O. Starinets, and M. A. Stephanov,
      "Relativistic viscous hydrodynamics, conformal invariance, and holography,"
      arXiv:0712.2451 [hep-th].

[38] A. Muronga, "Causal Theories of Dissipative Relativistic Fluid Dynamics for
      Nuclear Collisions," Phys. Rev. C69 (2004) 034903, nucl-th/0309055.

[39] W. Israel and J. M. Stewart, "Transient relativistic thermodynamics and kinetic
      theory," Ann. Phys. 118 (1979) 341�372.

[40] N. Andersson and G. L. Comer, "Relativistic Fluid Dynamics: Physics for Many
      Different Scales," Living Reviews in Relativity 10 (2007), no. 1,.

[41] R. Loganayagam, Work in progress, to appear.

[42] V. Balasubramanian and P. Kraus, "A stress tensor for anti-de Sitter gravity,"
      Commun. Math. Phys. 208 (1999) 413�428, hep-th/9902121.

[43] M. Henningson and K. Skenderis, "The holographic Weyl anomaly," JHEP 07
      (1998) 023, hep-th/9806087.

[44] R. Wald, "General relativity," Chicago, University of Chicago Press, 1984, 504 p.
      (1984).

[45] M. Brigante, H. Liu, R. C. Myers, S. Shenker, and S. Yaida, "Viscosity Bound
      Violation in Higher Derivative Gravity," arXiv:0712.0805 [hep-th].

[46] Y. Kats and P. Petrov, "Effect of curvature squared corrections in AdS on the
      viscosity of the dual gauge theory," arXiv:0712.0743 [hep-th].

[47] P. Romatschke and U. Romatschke, "Viscosity Information from Relativistic Nuclear
      Collisions: How Perfect is the Fluid Observed at RHIC?," Phys. Rev. Lett. 99 (2007)
      172301, arXiv:0706.1522 [nucl-th].

[48] C. Fefferman and C. Graham, "Conformal invariants," Elie Cartan et les
      Mathematiques d'Aujourd'hui, Asterisque 95 (1985).

[49] K. Skenderis, "Lecture notes on holographic renormalization," Class. Quant. Grav.
      19 (2002) 5849�5876, hep-th/0209067.

                                                        45
[50] I. Papadimitriou and K. Skenderis, "AdS / CFT correspondence and geometry,"
      hep-th/0404176.

[51] A. Ashtekar and B. Krishnan, "Dynamical horizons and their properties," Phys.
      Rev. D68 (2003) 104030, gr-qc/0308033.

[52] R. Penrose, "Gravitational collapse: The role of general relativity," Riv. Nuovo Cim.
      1 (1969) 252�276.

[53] R. M. Wald, "Gravitational collapse and cosmic censorship," gr-qc/9710068.
[54] O. Aharony, S. Minwalla, and T. Wiseman, "Plasma-balls in large N gauge theories

      and localized black holes," Class. Quant. Grav. 23 (2006) 2171�2210,
      hep-th/0507219.
[55] S. Lahiri and S. Minwalla, "Plasmarings as dual black rings," arXiv:0705.3404
      [hep-th].

                                                        46
