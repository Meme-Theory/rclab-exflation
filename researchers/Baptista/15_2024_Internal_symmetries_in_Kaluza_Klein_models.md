# 2024 Internal symmetries in Kaluza Klein models

**Source:** `15_2024_Internal_symmetries_in_Kaluza_Klein_models.pdf`

---

arXiv:2306.01049v3 [hep-th] 27 Mar 2024                    Internal symmetries
                                                        in Kaluza-Klein models

                                                                               Joa~o Baptista

                                                                                  June 2023

                                                                                  Abstract

                                         The usual approach to Kaluza-Klein considers a spacetime of the form M4 � K and
                                         identifies the isometry group of the internal vacuum metric, gK0 , with the gauge group
                                         in four dimensions. In these notes we discuss a variant approach where part of the
                                         gauge group does not come from full isometries of gK0 , but instead comes from weaker
                                         internal symmetries that only preserve the Einstein-Hilbert action on K. Then the weaker
                                         symmetries are spontaneously broken by the choice of vacuum metric and generate massive
                                         gauge bosons within the Kaluza-Klein framework, with no need to introduce ad hoc
                                         Higgs fields. Using the language of Riemannian submersions, the classical mass of a
                                         gauge boson is calculated in terms of the Lie derivatives of gK0 . These massive bosons
                                         can be arbitrarily light and seem able to evade the standard no-go arguments against
                                         chiral fermionic interactions in Kaluza-Klein. As a second main theme, we also question
                                         the traditional assumption of a Kaluza-Klein vacuum represented by a product Einstein
                                         metric. This should not be true when that metric is unstable. In fact, we argue that the
                                         unravelling of the Einstein metric along certain instabilities is a desirable feature of the
                                         model, since it generates inflation and allows some metric components to change length
                                         scale. In the case of the Lie group K = SU(3), the unravelling of the bi-invariant metric
                                         along an unstable perturbation also breaks the isometry group from (SU(3) � SU(3))/Z3
                                         down to (SU(3) � SU(2) � U(1))/Z6, the gauge group of the Standard Model. We briefly
                                         discuss possible ways to stabilize the internal metric after that first symmetry breaking
                                         and produce an electroweak symmetry breaking at a different mass scale.

                                         Keywords: Kaluza-Klein theories; Riemannian submersions; spontaneous symmetry breaking;
                                         unstable Einstein metrics; Standard Model; inflation.
Contents

1 Introduction and overview of results              2

2 Scalar curvature of submersive metrics on M4 � K  17

2.1 Decomposing the higher-dimensional scalar curvature . . . . . . . . . . . . 17

2.2 Yang-Mills terms on M4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.3 Fibres' second fundamental form . . . . . . . . . . . . . . . . . . . . . . . 22

2.4 Mean curvature of the fibres . . . . . . . . . . . . . . . . . . . . . . . . . . 23

2.5 Submersive metrics and gauged sigma-models . . . . . . . . . . . . . . . . 26

3 Dynamical models on M4 � K                        32

3.1 Lagrangian densities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3.2 Mass of the gauge bosons . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

3.3 Stability of product Einstein solutions . . . . . . . . . . . . . . . . . . . . . 36

3.4 Lagrangian in the Einstein frame . . . . . . . . . . . . . . . . . . . . . . . 41

3.5 Gauge coupling constants in the Einstein frame . . . . . . . . . . . . . . . 44

3.6 Unstable modes and scalar field inflation . . . . . . . . . . . . . . . . . . . 46

3.7 Left-invariant metrics on SU(3) . . . . . . . . . . . . . . . . . . . . . . . . 51

3.8 Unstable modes and internal symmetry breaking when K = SU(3) . . . . . 58

3.9 Stabilizing the internal curvature . . . . . . . . . . . . . . . . . . . . . . . 62

4 Comments on fermions                              66

4.1 No-go arguments against chiral fermions . . . . . . . . . . . . . . . . . . . 66

4.2 Spinors and GLk representations . . . . . . . . . . . . . . . . . . . . . . . . 68
4.3 Extended spinors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

4.4 Universal spinors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75

4.5 Lie and covariant derivatives of universal spinors . . . . . . . . . . . . . . . 80

A Appendices                                        85

A.1 Weyl rescalings in Riemannian submersions . . . . . . . . . . . . . . . . . 85

A.2 Bosons' mass in the Einstein frame . . . . . . . . . . . . . . . . . . . . . . 88

A.3 Quadratic forms on su(3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

References                                          91

                              1
1 Introduction and overview of results

This paper describes a collection of geometrical observations about internal symmetries
and mass generation in Kaluza-Klein models. It also explores the natural role that metric
instabilities can play in symmetry breaking and scale change in those models.

    The starting point for the discussion is the observation that while the Einstein-Hilbert
action on M4 � K has a very large group of symmetries--including the whole group
of diffeomorphisms of the internal space--the traditional Kaluza-Klein ansatz associates
gauge fields only to the much smaller internal isometry group, i.e. to the symmetries that
preserve a specific choice of vacuum metric on K. The main reason for this restricted
focus is the sense that any other gauge fields should have bosons with masses in the
Planck scale, so too heavy to be observed experimentally. This is not necessarily true,
however. A small perturbation of an initial vacuum metric can reduce its isometry group,
for example, and the gauge bosons associated to former isometries will acquire non-zero
but arbitrarily small masses. To ignore these gauge fields because they do not preserve
the new vacuum metric then seems unnatural. It also precludes the investigation of
relevant phenomena within the Kaluza-Klein framework, such as spontaneous symmetry
breaking or a possible dependence of the vacuum energy density on the internal geometry.
Thus, the first purpose of these notes is to discuss the consequences of having a theory
that associates gauge fields also to non-isometric diffeomorphisms of internal space, co-
existing with gauge fields that come from full isometries. Since distinct geometric origins
in higher-dimensions lead to gauge fields with different properties in four dimensions, a
primary motivation for the study is the possibility that these variations could be useful
to model the peculiarities of the weak force field in the Standard Model, when compared
to the strong and electromagnetic fields.

    In fact, some of the main difficulties associated with the traditional Kaluza-Klein
framework come from shortfalls in modeling the peculiarities of the weak force. For
instance, the standard viewpoint is that all observed gauge bosons correspond to Killing
vector fields on the internal space and are classically massless. The weak bosons gain
their experimental, extremely small masses (when compared to the Planck mass) through
a quantum mechanism that is not fully understood within the framework. Fermionic
masses, on the other hand, are determined by the eigenvalues of the Dirac operator on K,
or of a natural deformation thereof generally called the internal mass operator. The need
to consider deformations is imposed by the geometric fact that, due to the Schr�odinger-
Lichnerowicz formula, the standard Dirac operator does not have zero modes on a compact
internal space with positive scalar curvature, but a deformation may well have them. In
any case, one expects the internal mass operator to be natural and commute with all

                                                        2
isometries of internal space. However, as pointed out by Witten in [Wi2], a result of
Atiyah and Hirzebruch implies that any gauge group that acts through isometries on
the internal space cannot have complex (chiral) representations on the zero modes of the
internal Dirac operator or, more generally, on the zero modes of such deformations. So
the Kaluza-Klein picture seems to be inconsistent with the chiral nature of fermions when
responding to the weak force.

    Our main suggestion to address this difficulty follows from the calculation that, in a
more complete Kaluza-Klein model, the gauge boson associated to a vector field ea on K
has a mass proportional to the norm of the Lie derivative of the internal vacuum metric:

Mass A�a 2                          K Lea gK0 , Lea gK0  volgK0 .
                                      2 K gK0 (ea, ea) volgK0

So mass generation for gauge bosons should operate through a mechanism that perturbs

the vacuum metric gK0 in a way that ea is no longer an exact Killing field. If the perturb-
ation is small enough, the new bosons will be light. But if a boson is no longer acting

through isometries on the internal space, then it can also evade the Atiyah-Hirzebruch

theorem, and at least part of the gauge group may well have chiral fermionic representa-

tions. In other words, any perturbation of the classical vacuum metric on K that allows

some gauge bosons to gain a small mass should also allow that same part of the gauge

group to evade the Atiyah-Hirzebruch theorem. This could help to understand, within

the Kaluza-Klein framework, the fact that the massive gauge fields in nature are precisely

the ones that have chiral fermionic representations. Note that this observation does not

exhibit an explicit mechanism leading to the appearance of chiral representations. It

merely points out a possible new way to circumvent the no-go arguments described in

[Wi2] that rule out such representations in Kaluza-Klein models. There are other ways

to circumvent those arguments, some of them well-verified but perhaps farther from the

original Kaluza-Klein philosophy, such as adding to the theory gauge fields living on the

higher-dimensional spacetime [CS].

    Another indication that the weak force field may be better modeled by an association
with non-Killing vector fields on the internal space, as suggested here, is the experimental
fact that the weak field mixes fermions with different masses, while the strong and electro-
magnetic fields only mix fermions with the same mass. As previously mentioned, in the
Kaluza-Klein picture fermionic masses in four dimensions are determined by the eigen-
values of a natural, Dirac-like mass operator acting on spinors over K. One expects this
operator to commute with all isometries of internal space. So a gauge field associated with
an isometry of K should preserve the eigenspaces and eigenvalues of the mass operator,
i.e. should not mix fermions with different masses. Since the weak field does not have
this property, it is plausible that it is not associated with exact internal isometries.

                                    3
    A second significant difficulty associated with the traditional Kaluza-Klein framework
is finding classical solutions of the higher-dimensional equations of motion that can be
regarded as good candidates for the vacuum configuration [BL, DNP, CJ, CFD]. If one
takes the simplest option available and chooses the standard Einstein-Hilbert Lagrangian
for the higher-dimensional action, possibly with a non-zero cosmological constant, then
the classical solutions are the Einstein metrics on M4 � K. If one furthermore assumes
that the classical vacuum should be represented by a simple product metric gMe + gKe ,
then the higher-dimensional Einstein equations impose that gMe and gKe are both Einstein
metrics on the respective spaces with the same constant. In particular, if one takes M4 to
be flat Minkowski space or a nearly flat constant curvature space (corresponding to the
observed very small value of the four-dimensional cosmological constant), then the internal
metric gKe would also need to be flat or nearly flat. But Ricci flat metrics on a compact
space cannot have the continuous, non-abelian isometries that are needed in Kaluza-Klein
to model the strong force gauge fields. This problem disappears if we take gKe to have
positive curvature, as there are plenty of examples of positive Einstein metrics with non-
abelian isometry groups. Unfortunately, in all these examples, the inverse scaling relation
between scalar curvature and Riemannian volume raises a new problem: one would need
an Einstein internal space of unreasonably big volume in order to obtain the tiny scalar
curvature of gKe necessary to match the observed curvature of the spacetime vacuum
metric gMe . This unreasonably big internal space would then affect the predicted values of
the gauge coupling constants of the theory. Equivalently, a small internal Einstein space
will have good gauge couplings but large internal curvature, so the higher-dimensional
equations of motion force a way too large four-dimensional curvature and cosmological
constant. Hence the traditional difficulty to reconcile the Kaluza-Klein picture with the
smallness of the spacetime cosmological constant [CFD, ch. V.1].

    Our suggestion regarding this difficulty is based on the observation that Einstein
metrics are often unstable, and when this happens they may not be the best candidate
to describe the vacuum configuration. We will give two examples of such instabilities.
Firstly, it is well-known that a product Einstein metric with positive curvature is always
unstable under a rescaling of the relative size of M and K, even when the metrics gMe
and gKe are both stable on their respective spaces. If we take a function  in C(M ) and
contract the internal metric gKe by a factor e- while expanding the metric on M by an
appropriate power of e, a quadratic analysis of the Einstein-Hilbert action says that this
is an unstable perturbation of the product solution. One can go beyond the quadratic
analysis and flesh out the field  in the full action and its equation of motion. This reveals
a potential V () and confirms that the Einstein metric gMe + gKe should unravel along this
rescaling direction, in a process akin to cosmological inflation controlled by the scalar

                                                        4
field . This process is studied in section 3.6. During this unravelling, the 4D spacetime
curvature will become smaller. Thus, assuming that the deformation represented by 
stabilizes at a given value 0, presumably through a complex process akin to reheating,
the final vacuum configuration can have a spacetime curvature much smaller than the
internal curvature. In particular, after the unravelling of the product Einstein metric
along the -instability, the scale of the gauge couplings no longer has to coincide with the
scale of the spacetime cosmological constant.

    Besides the rescaling represented by , there can be additional interesting instabilities
of a product Einstein metric, such as the ones coming from TT-deformations of the
internal metric gKe . Let us consider the example of the internal space K = SU(3). It is
well-known that the bi-invariant metric on this group is Einstein, has positive curvature
but is unstable, meaning that it is a saddle point of the Einstein-Hilbert action under
TT-deformations of the metric, not a local maximum. Most TT-deformations of the
bi-invariant metric will reduce its scalar curvature, but a particular deformation found
in [Jen] takes the scalar curvature up to positive infinity. Since -RgK plays the role
of a potential for TT-deformations, we see that that particular mode is unstable and
its equation of motion is governed by a potential unbounded from below. Now, instead
of discarding this example as unphysical, let us entertain the possibility of a physical
unravelling of the initial bi-invariant metric along the unstable direction, if that metric
ever represented the internal configuration over an ancient region of spacetime.

    Firstly, we note that when the bi-invariant metric on SU(3) is deformed along that
unstable direction its isometry group is broken from (SU(3) � SU(3))/Z3 down to the
suggestive (SU(3) � SU(2) � U(1))/Z6, the gauge group of the Standard Model. This is
described in section 3.7. Identifying left-invariant metrics on SU(3) with inner-products
on the Lie algebra su(3), one can use the vector space decomposition

             su(3) = u(1)  su(2)  C2 , v = vY + vW + v ,

to write the deformed internal metric as

gK(u, v)  =  e-      15  e2 Tr(uY vY ) + e-2 Tr(uW  vW ) + e Tr (u) v  . (1.1)
                  5  2

Here  and  are positive constants,  is the scalar field on M that controls the rescaling
deformation, as before, while  is the scalar field that controls the TT-deformation and
breaks the internal isometry group. The value  = 0 corresponds to internal bi-invariant
metrics. As  grows, four initially massless gauge bosons acquire a classical mass that
increases with the extent of the TT-deformation, as calculated in section 3.8. But the
higher-dimensional Einstein-Hilbert action implies that the dynamics of the deformation
fields are governed by a classical potential, denoted V (, ), that is unbounded from below

                                          5
for large values of the fields. So will  and  just grow indefinitely, increasing the internal
curvature RgK and the bosons' masses across all orders of magnitude, as the internal space
collapses to zero size or becomes infinitely deformed? Or will new physics kick in at some
point, physics not contained in the Einstein-Hilbert action, and stabilize the deformation?

    Given that physical reality contains phenomena operating at different scales, we ar-
gue that the appearance of runaway instabilities in the metric derived from the simple
Einstein-Hilbert action should be viewed as a desirable feature of the model. As an
opportunity to allow some metric components to transition to other scales. The un-
bounded deformations just describe how those components will change by many orders
of magnitude before encountering new physics at a different scale, physics hidden in a
second part of the Lagrangian that only becomes relevant after the rescalings. In other
words, without the instabilities and runaway deformations at the Einstein-Hilbert level,
everything in the metric would be stuck at Planck scale. There would be no open door
for its components to reach the small scale of the cosmological constant, for instance. To
describe phenomena at those scales we would then need to introduce new fields, besides
the higher-dimensional metric, and this is undesirable in the Kaluza-Klein framework.

Embracing the existence of instabilities at the Einstein-Hilbert level, in section 3.9 we

discuss possible ways to stabilize the runway deformations of the internal geometry. One

of these attempts, for example, is based on the intuitive notion that there should be an

energy cost for increasing the gauge bosons' masses all the way up to infinity. This notion

may very well be false in the classical picture of the vacuum, where Yang-Mills fields can be

exactly zero. In the quantum picture the odds seem more favourable, though, with fields

that are always fluctuating and never vanish entirely. In fact, although the calculation of

the zero-point energy of a quantum field does not seem to be a settled matter, according

to most calculations the renormalized vacuum energy density does increase with the mass

m of the field, for instance as m4 log  m2  [Ma]. Here � is a new mass scale, not necessary
                                        �2

close and presumably smaller than the Planck mass. Adding this vacuum energy density

to the Einstein-Hilbert action we obtain an effective potential that, one calculates, is

now bounded from below as the metric deformation increases. So the unstable TT-

deformation could be stabilized once the gauge bosons associated to the broken part of

the isometry group reach masses that can balance the (Planck scale) contribution of -RgK
to the effective potential. Those heavy gauge bosons would be unobservable at current

experimental energies. Near the new equilibrium point the contributions to the effective

potential of the classical term RgK and of the vacuum energy density would be comparable
to each other. Hence the effective Lagrangian is no longer just the Einstein-Hilbert one,

and the Kaluza-Klein vacuum will not be a classical Einstein metric on M4 � K.

In principle this game can be played with other models for the internal space, besides

                                            6
K = SU(3). One basically needs an Einstein metric gKe whose isometry group contains
GSM and, simultaneously, has unstable TT-deformations that can break the isometry
group down to GSM at Planck scale. The electroweak symmetry breaking at a lighter
mass scale needs separate arguments.

    In any case, the overall message is that unstable Einstein metrics may deserve a second
look in the Kaluza-Klein framework. The existence of unstable directions of perturbation
could be more than a nuisance in the search for the vacuum configuration, more than a
criterion to exclude candidates among possible internal geometries. Firstly, the internal
symmetry breaking caused by unstable perturbations can carve out the peculiar (SU(3)�
SU(2)�U(1))/Z6 as a subgroup of larger, seemingly more natural gauge groups. Secondly,
the rescaling of the components of the unstable metric that fall along steep potentials may
be a good classical model for physical processes that require specific metric components
to change by many orders of magnitude, before encountering new physics at a different
scale. Classically stable Einstein metrics are too nice to have individual components
breaking out of the Planck scale. That is why they are hard to reconcile with a tiny
four-dimensional cosmological constant.

    In the second part of this Introduction we will give a more detailed overview of the
main calculations in this paper. For general reviews of Kaluza-Klein theory see [BL,
Ble, Bou, CJ, OW], for example, and the comprehensive texts [CFD, DNP] stressing the
supergravity viewpoint. Here we do not work with supergravity. We also do not delve into
the beautiful topic of black holes in Kaluza-Klein [GW, HW]. Some of the early original
references for Kaluza-Klein theory are [K], with much more complete lists given in the
mentioned reviews. Although some of the observations in these notes were suggested by
the calculations in [Ba1, Ba2], here we try to provide a broader picture of the models,
generalizing parts of those calculations along the way.

Decomposing the higher-dimensional scalar curvature

Consider the higher-dimensional space P = M4 � K viewed as a fibre-bundle over four-
dimensional spacetime. The fibre over a spacetime point, also called the internal space
over that point, is isomorphic to K. Let gP be a submersive metric on P . As in the usual
Kaluza-Klein framework, it determines three more familiar objects:

   i) through projection, a unique metric gM on the four-dimensional spacetime;

  ii) through restriction to the fibres, a family of metrics gK on the internal spaces;

 iii) gauge fields on spacetime, which can be encapsulated in a one-form A on M4 with
       values in the Lie algebra of vector fields on K.

                                                        7
The equations linking these objects to the higher-dimensional metric gP are

gP (U, V ) = gK(U, V )                                                       (1.2)
gP (X, V ) = - gK (A(X), V )
gP (X, Y ) = gM (X, Y ) + gK (A(X), A(Y )) ,

for all tangent vectors X, Y  T M and vertical vectors U, V  T K. These relations are
usually called the Kaluza-Klein ansatz for gP . They allow one to reconstruct the higher-
dimensional metric from the more familiar data (gM , A, gK). The correspondence between
submersive metrics on P and the data i), ii), iii) is a bijection. It will be described in
more detail in section 2.1.

Choosing a set {ea} of independent vector fields on K, the one-form on spacetime can

be decomposed as a sum

                        A(X) =             Aa(X) ea ,                        (1.3)

                                         a

where the real-valued coefficients Aa(X) are the traditional gauge fields on M4. For general

submersive metrics on P this can be an infinite sum, with {ea} being a basis for the full

space of vector fields on K, which coincides with the Lie algebra of the diffeomorphism

group Diff(K). Most often, however, the approach in Kaluza-Klein is to restrict the

attention to special families of higher-dimensional submersive metrics, such as the ones

obtained when K = G/H is a homogeneous space, the fibre metrics gK are G-invariant,
and the vector fields {ea} on K come from a basis of a finite-dimensional subspace of
Lie(G). For the moment we will not make any such restrictions, so will consider the case

of general submersive metrics on P .

    In these notes we investigate the scalar curvature of the metric gP . We want to express
it, as explicitly as possible, in terms of the equivalent data (gM , A, gK). A standard result
in Riemannian submersions [Bes, ch. 9] says that RgP can be decomposed as

RgP = RgM + RgK - |F |2 - |S|2 - |N |2 - 2 N .

Here RgM and RgK denote the scalar curvatures of the metrics gM and gK, respectively;
|F |2 is the component that originates the Yang-Mills terms |FA|2 in the usual Kaluza-
Klein calculation; the tensor S is the second fundamental form of the fibres K, also called
shape operator; the vector N is the metric trace of S, usually called the mean curvature
vector of the fibres.

    In the lowest-dimensional Kaluza-Klein model, where the internal space K is just
the circle S1, the scalar curvature RgK vanishes and the tensors S and N merge into
the same object. This essentially coincides with the gradient of the Brans-Dicke scalar
field, measuring the variation of the size of the internal circle as one moves along M4.

                                      8
For higher-dimensional K the structure of RgK and S is much richer. In section 2 we
investigate that structure for a general K, extending the results described in [Ba1] in the
particular case where K = SU(3) equipped with a special family of left-invariant metrics.

    For a general Riemannian submersion, one calculates that the third term of the higher-
dimensional scalar curvature can be expressed as

                 |F |2  =  1     gM�  gM  gK(ea, eb)  (FAa )�  (FAb )  ,                   (1.4)
                           4

where the (FAa)� are the components of the curvature of the gauge fields (1.3) on M4. The
right-hand side broadly coincides with the form of the Yang-Mills terms in the Standard
Model Lagrangian. The fact that such terms can be obtained from the higher-dimensional
scalar curvature RgP is a remarkable and very well-known result, sometimes dubbed the
Kaluza-Klein miracle [K].

    The terms |S|2 and |N |2 are much less studied in the Kaluza-Klein literature, where the
assumption of totally geodesic fibres (S = 0) or constant internal geometry are common.
Section 2.3 describes how the term |S|2 is akin to the covariant derivative of a Higgs field.
For a general submersion metric, it can be expressed in terms of the gauge fields and the
Lie derivatives of gP as

|S|2  =  1  gM�  LX� gP , LX gP  +    1   gM�  A�a Lea gP ,   LX gP 
         4                            2

                                                  +   1  gM�  Aa�  Ab Lea gP ,  Leb gP  .  (1.5)
                                                      4

So the fibres' second fundamental form produces the quadratic terms in the gauge fields Aa�
that are necessary for mass generation through spontaneous symmetry breaking. These

terms are encoded in the higher-dimensional scalar curvature RgP , with no need to intro-
duce ad hoc Higgs fields, as in the traditional Brout-Englert-Higgs mechanism [EBH].

    The parallel between the different components of the curvature RgP and those of an
Einstein-Yang-Mills-Higgs Lagrangian is made more explicit in section 2.5. There we
observe that a metric gP on the product M � K determines, by restriction, natural maps
from M to the space of Riemannian metrics and to the space of volume forms on K:

                   gK : M - M(K) ,                       x  gPx ;
                 volgK : M - k(K, R) ,                   x  volgPx .

Here gPx denotes the restriction of the metric gP to the fibre Px  K over the point x in M .
Since the diffeomorphism group Diff(K) acts naturally on the target spaces M(K) and
k(K, R), it is possible to define Diff(K)-gauge transformations and covariant derivatives

                                               9
of these maps. Then one shows that the Einstein-Hilbert action for a submersive metric
gP can be rewritten in terms of these maps as

  RgP volgP =        RgM  + RgK   -  1  |FA|2  -  1  |dAgK  |2  +  |DA (volgK )|2  volgP .
                                     4            4
P                 P

This is essentially an Einstein-Yang-Mills-Higgs Lagrangian. The terms |S|2 and |N |2

become the norms of the covariant derivatives of the scalar fields that describe how the

internal metric gK and its volume form vary from fibre to fibre. The opposite -RgK plays
the role of a classical Higgs potential for those scalar fields.

    If instead of general submersive metrics on P we only consider the homogeneous ones,
namely submersions with homogeneous restrictions to an internal space of the form K =
G/H, then the result is a simpler G-gauge theory, instead of a Diff(K)-gauge theory. That
is the standard setting in the Kaluza-Klein literature (e.g. [BL, CFD, CJ, DNP]). The
Higgs-like maps gK that we discuss here will then have values in the finite-dimensional
space of homogeneous metrics on G/H, instead of the infinite-dimensional M(K).

Mass of the gauge fields

In the simplest case of vector fields ea on K having vanishing divergence with respect
to the vacuum metric, the mass of the associated four-dimensional gauge fields can be

calculated to be

                     Mass Aa� 2      K Lea gK , Lea gK  volgK .                    (1.6)
                                       2 K gK (ea, ea) volgK

Here the internal metric should be taken to be constant at its vacuum value gK = gK0 .

Thus, the classical mass of a gauge field A�a is determined by the geometrical properties

of the vector field ea with respect to the vacuum metric on the internal space. Whenever

ea is Killing, the Lie derivative vanishes and the fields Aa� will be massless.

The precise relation between the gauge bosons' classical mass and the Lie derivatives

depends on whether the calculation is performed with a higher-dimensional Lagrangian

in the Einstein frame or in the Jordan frame. In the latter case, the constant of pro-

portionality in the relation above is the unity (section 3.2). In the Einstein frame the

constant of proportionality depends on the total volume VolgK0 of the vacuum internal
metric (appendix A.2). In general, the bosons' masses scale inversely with the size of the

internal space, but depend on much more than that size.

    If the internal vector field ea is nearly Killing, but not exactly, then the mass of the
boson associated to Aa� will be non-zero and very small. Thus, a natural way to generate
light bosons within the Kaluza-Klein framework would be to start with a classical internal

metric with a larger isometry group, for instance with SU(3) � SU(2) � U(1) isometries,

                                        10
and then suppose that a mechanism operating at a different scale, for example a quantum
mechanism, slightly perturbs the initial metric in a way that some Lie derivatives Lea gK0
become non-zero but remain small. In particular, in a physical system with very light
bosons the true internal vacuum metric should not be the classical metric--a solution
of the Einstein equations at Planck scale. Instead, it should be the perturbed metric
gK0 with nearly Killing vector fields--presumably a solution of equations derived from the
Einstein-Hilbert action added to some effective potential. Such scenarios will be discussed
in section 3.9.

    There are two immediate advantages of generating the gauge bosons' mass through
a perturbation of the classical internal metric, as opposed to using ad hoc Higgs fields.
Firstly, it fits naturally with the Kaluza-Klein framework, where everything should come
from the higher-dimensional metric. Secondly, if the physical internal vacuum metric gK0
has a reduced isometry group, for instance SU(3) � U(1) instead of SU(3) � SU(2) � U(1),
then it can evade the main no-go arguments against chiral fermions in Kaluza-Klein,
since these arguments only rule out chiral interactions with the gauge fields associated to
internal isometries. This will be further discussed in section 4.1.

Gauge couplings in the Einstein frame

A naive dimensional reduction of the Einstein-Hilbert action on M � K produces a Lag-
rangian in four dimensions that is not in the Einstein frame. This means that the gravity


component of the 4D Lagrangian does not appear in the traditional guise RgM -gM , but
instead appears multiplied by a scalar field that depends on the spacetime coordinate.
This field is a hallmark of Kaluza-Klein theories. It is related to the volume of the internal
space over each spacetime point, which can vary along M .

    Since the Einstein frame is generally preferred for a good physical interpretation of the
4D theory [FGN], in section 3.4 we use a Weyl rescaling of the metric gM to transform our
Lagrangian to the Einstein frame. This rescaling is a standard technique in many models.
To apply it to our general Kaluza-Klein model, we first calculate how the geometric terms
|F |2, |S|2 and |N |2 transform under separate Weyl rescalings of gM and gK. This is done
in appendix A.1 and, subsequently, leads to the general Lagrangian (3.28).

    Using those results, in section 3.5 we argue that the traditional formula relating the
scale of the gauge couplings to the size of the internal space is unnecessarily strict. Start-
ing from the Einstein-Hilbert action on M � K, the traditional Kaluza-Klein argument
assumes a constant vacuum metric gK0 and performs the dimensional reduction

 1     (RgP - 2) volgP  =  1           RgM  +  RgK0  -  1  |FA|2  -  2  volgM
2 P                                                     4
     P                     2 M  M

                                11
by fixing the value P := M Vol(K, gK0 ) and integrating over the fibre K. Here M denotes
the four-dimensional Einstein constant. Since gauge fields have values on the vector fields

on K, the norm |FA|2 depends on the internal metric gK0 . This leads to gauge coupling

constants Wein of the order                        82M
                                                     l2
                             W 2 ein                         ,
                                                        gK0

where lgK0 denotes the "average" length of the circumferences on (K, gK0 ) generated by

the vector field associated to the gauge field. This was derived in a very general setting

by Weinberg in [Wei2], with the slightly ajusted conventions described in section 3.5. A

similar relation is stated in most reviews.

    Our point here is that fixing the constant P to a vacuum-dependent value does
not sound like a general approach. For example, if the theory had several local vacua,
associated to internal spaces of different sizes, the derivation of the respective couplings
W 2 ein would run into an ambiguous choice when imposing the normalization of P . A more
general approach to obtain a 4D action in the Einstein frame is to keep P unconstrained
and, instead, redefine the physical metric gM through the Weyl rescaling of section 3.4.
This approach produces a Lagrangian in the Einstein frame even when the internal metric
gK is not constant throughout the spacetime M . Thus, using the Lagrangian of section
3.4, in section 3.5 we adapt the derivation of [Wei2] to obtain a slightly more general
formula for the scale of the gauge couplings in four dimensions:

                             2  82 P .
                                             l2    VolgK0

                                              gK0

This reduces to the traditional expression when P = M VolgK0 , but here P remains
unconstrained. In particular, notice that the 2 derived from the full Lagrangian in the

Einstein frame scales differently from W 2 ein when (K, gK0 ) changes size. This happens
because, in the traditional derivation, the volume factor (VolgK0 )-1 is hidden in the nor-
malization of the constant P , which in fact becomes a non-constant for a rescaling gK0 .

Unstable Einstein metrics and cosmological inflation

Ideally, a classical vacuum configuration on M � K would be characterized by vanishing
gauge fields, a flat or perhaps constant curvature four-dimensional metric gM , and internal
metrics gK that are constant across the different fibres and equal to a fixed metric on K.
In other words, the ideal vacuum configuration of gP would be a product metric gM + gK.
To satisfy the higher-dimensional equations of motion, both metrics gM and gK need to
be Einstein on the respective spaces with the same constant.

                                             12
    But what happens when those Einstein products are unstable? It is well-known that a
product Einstein metric with positive curvature is always unstable under a rescaling of the
relative size of M and K, even when gM and gK are both stable on their respective spaces
[Bes, Kro]. The metric gK may also be unstable under TT-deformations of the internal
geometry. The initial dynamics of those deformations can be studied by considering
submersive metrics of the form

                       gP = e1 gM + e-2 gK () .

Here  and  are four-dimensional scalar fields that parametrize the unstable rescaling
and the unstable internal TT-deformations, respectively, over each spacetime point. The
i are positive constants to be specified later. The gauge fields are taken to vanish
in this approximation, so we are looking at the conditions close to the initial Einstein
product metric gM + gK. Applied to such metrics gP , the higher-dimensional Einstein-
Hilbert action (converted to the Einstein frame) reduces to a four-dimensional action of
the illustrative form

   (RgP - 2 ) volgP =       1  RgM  -   1  |d|g2M  -  5  |d|2gM  -  V (, )  volgM ,
                          2 M           2             2
P                      M

after integration over the fibre K. So the deformation scalars are similar to Klein-Gordon
fields governed by a potential V (, ).

    The overall form of the dimensionally-reduced action is similar to the action found in
scalar models of cosmological inflation. Thus, optimistically, Kaluza-Klein suggests how
the ad hoc scalar fields of inflation could have their origin in the scalar components of the
internal metric that unravel under unstable deformations of a primordial, product Einstein
metric on M � K. This interpretation suggests a new way to generate microscopically
motivated, multi-field models of the initial stages of inflation. Experiment with different
Einstein metrics on K, which will have different TT-instabilities and hence will generate
distinct inflationary models in four dimensions.

    In section 3.6 we study the most basic example, where the internal metric has no un-
stable TT-deformations and the rescaling represented by  is the only instability present.
Then the dimensionally-reduced Einstein-Hilbert action is similar to the inflaton action in
single-field models of inflation. The potential V () has a maximum at  = 0 and generates
inflation as  rolls down from the maximum, during the initial stages of rescaling of the
internal space. However, in this approximation (no TT-instabilities, no gauge fields, etc.),
it does not satisfy the quantitative conditions of slow-roll inflation.

    Section 3.8 illustrates the case where TT-instabilities are also present, working in the
example K = SU(3). The potential V (, ) is seen to have a -maximum and a -saddle

                                    13
point at the values  =  = 0, so the product Einstein metric is manifestly unstable.
The additional instability represented by  breaks the internal symmetry, reducing the
isometry group of K from (SU(3) � SU(3))/Z3 down to (SU(3) � SU(2) � U(1))/Z6.
The action defines a more evolved, two-field model of the initial stages of inflation. The
potential V (, ) is unbounded from below for large values of  and . This suggests that
these components of the higher-dimensional metric can change significantly in a classical
dynamical process, perhaps by many orders of magnitude, before being stabilized at a
different scale by new physics not contained in the Einstein-Hilbert action (if they can be
stabilized at all). Of course at later times also the gauge fields can become non-zero, so
even the classical dynamics is more complicated than what is represented by the simplified,
four-dimensional action written above.

    If the unstable deformations of gP can be stabilized by an effective potential, then
the resulting deformed metric should be a better candidate for the present-time vacuum
configuration than the product Einstein metric. Due to the rescaling represented by , in
that vacuum configuration the scale of the gauge couplings no longer needs to coincide with
the scale of the cosmological constant on M , as discussed previously in this Introduction.

Stabilizing the internal curvature

As described before, one expects the initial Einstein product metric on M � K to unravel
along the unstable deformations represented by  and . When this happens, the internal
space goes through a rescaling and, simultaneously, through a slower TT-deformation
that breaks the isometry group and increases the internal scalar curvature. But will these
deformations of the internal geometry increase indefinitely, across all orders of magnitude
of size and curvature, as indicated by the classical potential V (, )?

    Generally speaking, it is reasonable to expect that new physics may start to be relevant
at other scales of size or curvature. One should not be able to confine quantum particles
in arbitrarily small internal directions, for example. Meanwhile, it is probably a tall
order to ask the (higher-dimensional) Einstein-Hilbert action to cover the phenomena in
all those scales. So the question becomes how to complement that action and model
mathematically the micro-scale effects. For example, is there a natural addition to the
Einstein-Hilbert action that becomes relevant for small internal spaces and prevents a
total collapse of K? Or an effective potential that increases with the internal curvature
and prevents gauge bosons with infinite mass? If they exist, should those additional
terms to the Lagrangian be regarded as purely ad hoc, as in most cosmological models of
inflation and reheating, or can they be justified as having origins in micro-scale physics?
These speculative matters are discussed in section 3.9.

                                                       14
    One possible ideia would be to introduce an effective potential inspired by the QFT
vacuum energy density. Well-known calculations suggest that the renormalized, four-
dimensional vacuum energy density increases with the masses of the quantum fields.
Although the precise formula does not seem to be consensual, the contribution of a gauge
field of mass m to the vacuum energy density should increase as the power m4. The
calculations in [Ma], for instance, suggest a contribution proportional to

m4 log m2 ,                                (1.7)
           �2

where � is a new mass scale. But in a Kaluza-Klein model the (classical) mass of a
gauge field depends on the vacuum internal metric, as expressed by formulae such as (3.7)
or (A.23). So we have a non-trivial dependence m2 = m2(gK), and this means that a
deformation of the internal metric will affect the vacuum energy density:

v4aDc = v4aDc(gK ) .

Adding this density to the classical Einstein-Hilbert Lagrangian creates an effective po-
tential for the internal deformations that, in a favourable setting, could contribute to
stabilize them around a local minimum. In the simplified example of section 3.9, and only
taking into account the contributions of the natural gauge bosons, we have something like

Veff(, ) = V (, ) + m4(, ) log  m2(, )  ,
                                    �2

with a dependence m2(, ) established in (3.84). An inspection of that formula shows
that the power m4(, ) grows as e2 e4 for large, positive values of the deformation
fields. So the second term in Veff will dominate the initial potential V (, ) in this
regime, which decreases as -e e2 for large values of the same fields. This suggests that
the unstable (, )-deformations of the internal metric could in principle be stabilized by
contributions coming from the vacuum energy density. This is just a rough argument,
nonetheless, since the true vacuum energy density is a complex quantity that should
depend on all gauge fields and all fermionic fields.

    The appearance of a new mass scale � in the effective potential is also an interesting
feature. In favourable conditions, some classically massless gauge fields may acquire
a mass dependent on the new scale, which can be distinct from the Planck scale. In
general, adding a new potential term to the classical Einstein-Hilbert action implies the
introduction of new constants and scales in the model. This could help to model the
physical electroweak symmetry breaking within the Kaluza-Klein framework, although
we do not pursue that line here.

15
Comments on fermions
Having gauge fields associated to non-isometric diffeomorphisms of the internal space
creates new opportunities--such as the possibility to generate mass for the gauge bosons
within the Kaluza-Klein framework, or the possibility to evade the Atiyah-Hirzebruch
theorem--but also additional theoretical challenges--such as understanding how fermions
should transform under diffeomorphisms that do not preserve the metric. This challenge
exists in any gravity theory, not just in Kaluza-Klein.

    In section 4.1 we discuss the opportunity to circumvent the traditional no-go arguments
against chiral fermions in Kaluza-Klein. These include the general argument derived
from the Atiyah-Hirzebruch theorem, ruling out chiral fermions in all dimensions, as
well as other arguments applicable only to certain dimensions. For the rest of section 4
we describe three possible geometric approaches to the question of how fermionic fields
should transform under non-isometric diffeomorphisms of the underlying space. This
implies thinking about the definition of spinor itself. More precisely, how to extend
this definition to objects that are not tied down to a fixed background metric, i.e. to
objects that have a natural action of the double cover of the diffeomorphism group. The
approaches described include using GLk+-representations, instead of Spink representations;
using what we call extended spinors; or using more general universal spinors. Some of
these approaches already exist in the literature, in different forms, but do not seem to be
widely explored.

                                                       16
2 Scalar curvature of submersive metrics on M4 � K

2.1 Decomposing the higher-dimensional scalar curvature

The purpose of this section is to recall the notion of Riemannian submersion on the
higher-dimensional manifold P = M � K. More details can be found in [O'Ne, Bes]. A
submersive metric on P , denoted by gP , is the classical field of a general version of the
Kaluza-Klein ansatz. It can be fed into an action functional E(gP ) such as the Einstein-
Hilbert action. We will spend a few paragraphs recalling the formula for the scalar
curvature of a Riemannian submersion and establishing the associated notation.

    Let  denote the natural projection  : P  M . The inverse image -1(x) of a given
point x in M is called the fibre of P above x, or the internal space above x. It is sometimes
denoted by Px or Kx, and it is of course isomorphic to K. The tangent space to P at
any given point p = (x, h) has a distinguished subspace Vp defined by the kernel of the
derivative map  : TpP  TxM . This is called the vertical subspace of the projection
 and is just the tangent space to the fibre Px. When P is a simple product, it can be
identified with the tangent space ThK. Given an arbitrary Riemannian metric gP on P ,
the orthogonal complement to Vp is called the horizontal subspace Hp of the tangent space
TpP . Then we have a decomposition

TpP = Hp  Vp        E = EH + EV ,                        (2.1)

and every tangent vector E  TpP can be written as a sum of the respective components.
The map  is called a submersion if the derivative  : TpP  TxM is surjective for every
p  P . In this case the derivative induces an isomorphism of vector spaces Hp  TxM .
This is always true in the case of a product manifold P = M � K. The pair (, gP ) is
said to define a Riemannian submersion if it satisfies the property

 E1H =  E2H  =      gP E1H, E1H = gP E2H, E2H            (2.2)

for any horizontal vectors E1H and E2H on T P . In words, horizontal vectors that project
down to the same vector on the base M must have the same gP -norm on P , even if they
are tangent to different points of the same fibre. This is a restriction on the metric gP .

    Any Riemannian submersion (, gP ) defines a metric gM on the base by projection.
To be more precise, given a vector X  TxM , let p be a point on the fibre above x and
let XH be the unique horizontal vector in Hp such that  XH = X. Then one defines

(gM )x(X, X) := gP (XH, XH) .

This definition is independent of the choice of the point p on the fibre -1(x) because of
property (2.2).

                17
    A Riemannian submersion (, gP ) also defines a natural one-form A on M with values
on the space of vertical vector fields. In fact, given point p = (x, h) on P and a tangent

vector X  TxM , the identification TpP = TxM  ThK allows us to regard X also as
vector in TpP . Using this identification and decomposition (2.1) one simply defines

            A(X) |p := - XV ,                               (2.3)

where X is regarded as a vector in TxM on the left-hand side and as a vector in TpP on
the right-hand side. This definition implies that

            (gP )p(A(X), V ) = - (gP )p(X, V )

for every vector V  Vp. The information contained in the one-form A on M is equivalent
to the information contained in the horizontal distribution H  T P associated to gP .
In fact, if a vector field E on P is written as a sum E = EM + EK according to the
decompositon T P = T M  T K, then we have the identities

            EV = EK - A(EM )      EH = EM + A(EM ) .        (2.4)

The one-form A on M is called the connection form, or the Yang-Mills form, of the
submersion. It can also be regarded as the one-form on the base defined by a connection
on a (trivial) Diff(K)-principal bundle over M . This works because the Lie algebra of the
diffeomorphism group Diff(K) is the space of vector fields on K, so precisely the space
where A has its values. In this view P = M � K should be regarded as the bundle
associated to that principal bundle by the natural Diff(K)-action on K.

    Besides determining a metric gM and a one-form A, a Riemannian submersion (, gP )
also defines a family of metrics gK on the internal space by restricting gP to the different
fibres, all isomorphic to K. In other words, gP defines a map from M to the space of
Riemannian metric on K, M  M(K), through the natural restriction x  gP |-1(x).
This point of view will be further discussed in section 2.5.

As described in the Introduction, using (1.2) one can fully reconstruct the submersive

metric gP from the equivalent data (gM , A, gK). So all the natural quantities associated to

gP can also be expressed in terms of that data. For example, it follows from groundwork

in [O'Ne] that the scalar curvature of a submersive metric gP can be written as a sum of

components

            RgP = RgM + RgK - |F |2 - |S|2 - |N |2 - 2 N .  (2.5)

Here RgM and RgK denote the scalar curvatures of gM and gK, respectively, and F , S and
N are the tensors on P that we will now describe (see chapter 9 of [Bes]2).

2The notation here differs from that in [O'Ne, Bes] in the following points: the tensor called A in [O'Ne, Bes]
 is called here F, to avoid confusion with the gauge fields; the tensor called T in [O'Ne, Bes] is called here
 S, to avoid confusion with the energy-momentum tensor.

                              18
Let  denote the Levi-Civita connection of the metric gP ; let U and V denote vertical

vector fields on P ; let W and Z denote horizontal vector fields on P . Then S denotes the

linear map V �V  H that extracts the horizontal component of the covariant derivative

of vertical fields,

                                   SU V := (U V )H .                                     (2.6)

Since U and V are tangent vectors to the fibre K, the map S can be identified with the
second fundamental form of the fibres immersed in P . When S vanishes, all the fibres are
geodesic submanifolds of P and are isometric to each other [Her, Bes].

    On its turn, F is the linear map H � H  V that extracts the vertical component of
the covariant derivative of horizontal fields,

                           FW Z    := (W Z)V     =      1 [W, Z]V .                      (2.7)
                                                        2

The second equality is a standard result for torsionless connections [O'Ne, Bes]. When
F vanishes, the Lie bracket of horizontal fields is also horizontal, and hence H is an
integrable distribution. It is clear from the respective definitions that both S and F are
C-linear when their arguments are multiplied by smooth functions on P .

The vector field N , perpendicular to the fibres of the submersion, is defined as the

metric trace

                                   N :=          j Svj vj ,                              (2.8)

where {vj} denotes a gK-orthonormal basis of the vertical space. So N can be identified
with the mean curvature vector of the fibres of P . The norms of all these objects are

defined by

            |F |2 :=       gK FX�H XH , FX�H XH                                          (2.9)

                      �,

            |S|2 :=        gP Svi vj , Svi vj =         gP (Svivj , X�) gP (Svivj , X�)

                      i,j                        i,j,�

            |N |2 := gP (N, N ) =     gP (N, X�) gP (N, X�) ,

                                   �

where {X�} stands for a gM -orthonormal basis of T M , which lifts to a gP -orthonormal
basis {X�H} of the horizontal subspaces inside T P . Finally, the scalar N is defined as

the negative trace

                           N = -        gP       X�H N, X�H  .                           (2.10)

                                      �

It is useful to note that the scalar N can also be expressed as a the combination of

the norm |N |2 and a total divergence on P . In effect, using the fact that {X�H, vj} is a

                                         19
gP -orthonormal basis of the tangent space to P , we have that

N = - divgP (N ) +                       gP vj N, vj

                                 j

= - divgP (N ) +                         Lvj gP N, vj - gP N, vj vj

                                 j

= - divgP (N ) -                         gP N, Svj vj = - divgP (N ) - |N |2 .           (2.11)

                                 j

Observe that S and N are not independent tensors, as one is the metric trace of the other.

To work with independent degrees of freedom it is convenient to isolate the traceless part

of the fibres' second fundamental form as

                      S�(U, V )  :=      S(U, V )   -  1                                 (2.12)
                                                       k gP (U, V ) N ,

where k denotes the dimension of K. In this case we have the usual identity of norms

|S�|2 :=        gP S�vi vj , S�vi vj

          i,j

=         |S|2  +  1   |N |2          gP (vi, vj)2  -  2       gP Svivj , N gP (vi, vj)
                   k2                                  k
                                 i,j                      i,j

= |S|2 + 1 |N |2 - 2                          gP Svj vj , N       = |S|2 - 1 |N |2 .     (2.13)
                   k                  k                                         k
                                         i,j

The purpose of the next few sections will be to calculate more explicitly these different

components of the higher-dimensional scalar curvature RgP . This will lead to a better
understanding of their role in terms of four-dimensional physics.

2.2 Yang-Mills terms on M4

The content of the famous Kaluza calculation, progressively generalized in [K], is the
verification that the Yang-Mills kinetic terms for the gauge fields on Minkowski space
can be obtained from the higher-dimensional Einstein-Hilbert action, more precisely from
the component |F|2 of the higher-dimensional scalar curvature. In this section we will
verify how this works for general submersive metrics gP on P = M � K, as determined by
the metrics gM and gK and by the one-form A defined in (2.3). Everything develops as
expected, so this is mostly a training exercise in the language of Riemannian submersions.

    Let X be a tangent vector to M . From the identification T P = T M  T K, it can be
regarded also as a tangent vector to P satisfying X = X. From (2.4) we can write the
horizontal component of X as

                XH := X + A(X) = X +                           a  Aa(X) ea ,             (2.14)

                                              20
where A is the one-form on M with values in the Lie algebra of vector fields on K and, in
the rightmost sum, we have picked a basis {ea} for that algebra. The same identification
T P = T M  T K also allows us to think of A as having values on the vertical vector fields
on P . Then an application of (2.14) to the tensor F of (2.7) leads to
 2 FXHY H = [XH, Y H]V

               = [X, Y ]H - A([X, Y ]) + [A(X), Y ] + [X, A(Y )] + [A(X), A(Y )] V
               = - A([X, Y ]) - LY [Aa(X)] ea + LX[Aa(Y )] ea + [A(X), A(Y )] V
               = (dM A)(X, Y ) + [A(X), A(Y )] V .

Here we have used the Einstein summation convention and the standard identity for the
exterior derivative of a one-form:

d(u, v) = Lu[ (v) ] - Lv[ (u) ] - ([u, v]) .                                         (2.15)

Standard properties of the Lie bracket of vector fields on P also allow us to write

[A(X), A(Y )] = Aa(X) Ab(Y ) [ea, eb] - Ab(Y ) d[Aa(X)](eb) ea + Aa(X) d[Ab(Y )](ea) eb
                  = Aa(X) Ab(Y ) [ea, eb] ,

since the Aa(X) are functions on M with constant value along the vertical fibres K. Thus

2 FXHY H = (dM Aa)(X, Y ) ea + Aa(X) Ab(Y ) [ea, eb] =: FA(X, Y )                    (2.16)

has constant values along the fibres and defines a 2-form on the base M with values on
the vertical vector fields of P . This is of course the curvature of the connection one-form
A. To explicitly write down the norm |F|2, let {X�} denote a basis for the tangent space
T M . It follows from (2.16) combined with (2.9) that

|F |2           =  1               gM�  gM  gK(ea, eb)  (FAa )�  (FAb )              (2.17)
                   4

as a scalar function of M � K. Even though the metric gM and the curvature coefficients
FAa only depend on the coordinate x  M , the norm of F is not a constant function along
K, since the inner-products gK(ea, eb) in general do depend on the coordinates on K.

This expression for |F |2 can be integrated over the internal space (K, volgK ) to define

a scalar function on the base M :

   |F |2 volgK  =  1               gM�  gM  (FAa )�  (FAb )    gK (ea, eb) volgK .   (2.18)
                   4
K                                                            K

Observe how the coefficients in front of the curvature components depend solely on the

L2 inner-product of the vector fields ea on K. This scalar density on M broadly coincides
with the form of the Yang-Mills terms in the Standard Model Lagrangian. This very

well-known fact is sometimes dubbed the Kaluza-Klein miracle.

                                            21
2.3 Fibres' second fundamental form

A submersive metric gP on the higher-dimensional M � K, together with a metric con-
nection on the tangent bundle, determines the tensor S defined in (2.6). This tensor
can be identified with the fibres' second fundamental form in the case of the Levi-Civita
connection. The purpose of this section is to understand S and its norm |S|2 in terms of
the data (gM , gK, A), equivalent to the initial metric gP . In the Lagrangian density of a
Kaluza-Klein model, the component |S|2 of the higher-dimensional curvature encapsulates
the kinetic terms for the scalar fields describing how the internal metric gK varies from
fibre to fibre. These scalar fields are the analog of the Higgs field in the Kaluza-Klein
framework. In particular, it is the component |S|2 of the Lagrangian that contains the
quadratic terms in the gauge fields that can lead to mass generation through spontaneous
symmetry breaking.

    Let U and V be vertical vector fields on the total space of a submersion  : P  M
and let  be a metric connection on the tangent bundle T P . In a submersion, the Lie
bracket of vertical fields is always vertical [Bes]. So for torsionless connections it is clear
that SU V , as defined in (2.6), is symmetric:

SU V = (U V )H = V U + [U, V ] + Tor(U, V ) H = SV U .                           (2.19)

It is not strictly necessary to start with a torsionless connection in order to obtain a
symmetric S. It is enough to demand that Tor(U, V ) be a vertical vector field whenever
U and V are vertical. This will be the case when Tor(U, V ) is proportional to the bracket
[U, V ], for instance. Be that as it may, in the calculations ahead we will not explore this
variant and will simply assume that  is the Levi-Civita connection.

    Using the definition of SU V and the properties of the Levi-Civita connection, one can
write for every vector X  T M  T P :

gP SU V, X    = gP U V, XH = LU gP (V, XH) - gP V, U XH )
              = - gP V, XHU + [U, XH] .

But SU V is symmetric in U and V , so using again that  is a metric connection,

2 gP SU V, X  = gP SU V, X + gP SV U, X
              = - LXH gP (U, V ) - gP V, [U, XH] - gP U, [V, XH]
              = - (LXH gP ) U, V ,                                               (2.20)

where the last equality is a standard identity for Lie derivatives of 2-tensors. This formula
provides a concise relation between the tensor SU V and the horizontal Lie derivatives of

              22
the submersion metric gP . Using expression (2.14) for the horizontal lift of X and noting
that the functions Aa(X) are constant along the fibres, so have vanishing Lie derivative
along the vertical fields U and V , we can also write

2 gP SU V, X = - (LX gP )(U, V ) - Aa(X) (Lea gP )(U, V )                          (2.21)

as a scalar function of M � K. The combination of (2.9) and (2.20) allows us to express
the squared-norm of the fibres' second fundamental form as

              |S|2 = 1              (gM )� (LX�H gP )(vi, vj) (LXH gP )(vi, vj) ,  (2.22)
                         4
                            �, i,j

where {vj} is any gK-orthonormal basis of the vertical space. For a general submersive
metric gP the norm |S|2 is not a constant function along the fibres. If we use (2.21)
instead of (2.20), the formula for |S|2 becomes longer but perhaps more suggestive:

|S|2 = 1      �, gM� LX� gP , LX gP + 2 gM� Aa(X�) Lea gP , LX gP 
           4                                 + gM� Aa(X�) Ab(X) Lea gP , Leb gP  . (2.23)

Here � , � denotes the inner-product on the space of vertical, symmetric 2-tensors determ-
ined by the metric gP , or by its restriction gK to the fibres. Explicitly, the inner-product
of two symmetric 2-tensors on the internal space K is defined as

                            h1, h2gK :=        h1(vi, vj) h2(vi, vj) ,             (2.24)

                                         i, j

where {vj} is any local, gK-orthonormal trivialization of T K.

    Expression (2.23) shows how the fibres' second fundamental form gives rise to the
quadratic terms in the gauge fields Aa that are essential to mass generation through
spontaneous symmetry breaking. Quite naturally, the coefficients of those quadratic terms
are determined by the Lie derivative of the fibres' metric along the associated internal
vector field ea. So the components Aa associated to Killing vector fields will disappear
entirely from |S|2, and thus correspond to massless bosons.

2.4 Mean curvature of the fibres

Among the six components of the higher-dimensional scalar curvature RgP in formula
(2.5), only the terms involving the mean curvature vector of the fibres--denoted by N in
that formula--have not yet been calculated in terms of the data (gM , gK, A). That is the
purpose of this section.

                                                       23
    Let p = (x, h) be a fixed point in the product manifold P = M � K. Let {uj} denote
a trivialization of T K in a neighbourhood of h that is orthonormal with respect to the
restriction of the metric gP to the fibre Px = {x} � K. This restriction is denoted by gPx.
If we are talking about a general fibre of P , the vertical restriction of gP is denoted simply
by gK. Having in mind definition (2.8) of the horizontal field N , we start by taking the
trace of (2.20) to write

2 gP (N, X) = 2 gP Suj uj, X = - LXH gP (uj, uj) - 2 gP uj, [uj, XH] . (2.25)

The orthonormality of the vector fields {uj} with respect to gPx implies that the functions
gP (uj, uj) have vanishing Lie derivatives in the vertical directions, so

                   LXH [ gP (uj, uj) ] = LX [ gP (uj, uj) ]

over the slice {x} � K. On the other hand, since X is a vector field on M and uj is a
field on K, the bracket [X, uj] vanishes over the product M � K. So

gP uj, [uj, XH] =           gP uj, uj, Aa(X) ea  =        Aa(X) gP uj, [uj, ea] ,

                   j, a                             j, a

where the last equality uses that the coefficients Aa(X) are constant along the fibres. This
expression can be further simplified by making use of the properties of the Levi-Civita
connection  on the fibre Px. In fact, for any vertical vector field V on K we can write

   gPx uj, [uj, V ] =             gPx uj, uj V - V uj

j                              j

                                                    1
                            =     gPx uj, uj V - 2 LV gPx(uj, uj)

                               j

                            = divgPx (V ) ,                             (2.26)

where the last equality uses that the local vector fields {uj} are orthonormal, besides the
definition of divergence of a vector field. Applying this simplification to (2.25) we get
that, for any vector X  T M  T P ,

2 gP (N, X) = -             LX gP (uj, uj) - 2      Aa(X) divgK (ea) .  (2.27)

                         j                       a

When reading this expression it is important to keep in mind that the vertical restrictions
of the submersive metric gP , generically denoted by gK, may vary across different fibres,
while the basis {uj} was defined to be gK-orthonormal only at the fibre Px. In particular,
the functions gP (uj, uj) have value 1 on Px but need not be constant when moving across
fibres along the flow of X.

                                  24
    Using the Jacobi formula that relates the derivative of the determinant of an invertible
matrix with the derivative of the trace the matrix, one can also write locally

        LX     j        gP (uj, uj) = 2 LX log |gK| .

Here the symbol |gK| denotes the determinant of the square matrix gP (ui, uj) that rep-
resents the fibre metric in the local, fixed, gPx-orthonormal trivialization {uj} of T K. So

   |gK| is the scalar density of the volume forms volgK in this trivialization. Denoting by
volgPx the fixed volume form on K associated to the metric gPx, we can write

                        volgK = |gK | volgPx .

This expression shows that the function |gK| is globally defined on the product M � K.
Now let volg0 be any fixed volume form on K. It can be written as f0 � volgPx for some
function f0 on K that does not depend on M . Since X is a vector field on M , we have

LX log  |gK |  = LX     log  volgK       = LX        log  volgK  + log(f0)
                             volgPx                       volg0

               = LX     log  volgK
                             volg0

as a function on P = M � K. So we can finally write

gP (N, X) = - LX log    volgK         -  a Aa(X) divgK (ea) .               (2.28)
                        volg0

This expression makes it manifest that the mean curvature vector N depends on the
internal metric only through its volume form volgK . More precisely, it measures how volgK
varies along the flows of X in the base M and along the vertical flows of ea. The function
gP (N, X) in general is not constant along the fibres of P , as both volgK and the vertical
divergence of ea vary with the metric gP along both K and M .

    The previous expression for gP (N, X) leads to a remarkably simple integral relation
between both sides of the equation. This happens because the coefficients Aa(X) are
constant along K and the fibre-integral of the divergence divgK (ea) always vanishes. Using
also that the volume form volg0 is fixed on K and does not change with the flow of X
along M , we get simply

   gP (N, X) volgK = -    LX log  volgK  volgK = -           LX (volgK )  volgK
                                  volg0                         volgK
K                       K                                 K

               = - LX (volgK ) = - LX VolgK .                               (2.29)

                             K

                                  25
as a function on the base M . Here VolgK denotes the total volume of the fibre, and the last
equality follows from Leibniz rule for the exchange the order of integrals and derivatives.
The resulting expression is a well-known formula for the first variation of the volume of
the fibres as one moves along the base of a Riemannian submersion (e.g. [Be]3).

The norm |N |2 of the mean curvature vector can be expressed in terms of the data

(gM , volK, A) by substituting (2.28) in the definition (2.9) of the squared-norm. Here we

will not write it down. We will, however, give a slightly simplified expression for the

fibre-integral of the resulting expression, K |N |2 volgK . To this end, note that using again
Leibniz integral rule and the fact that divgK (ea) integrates to zero over the fibre, we have

  divgK (ea) LX� log   volgK         volgK = divgK (ea) LX�(volgK )
                       volg0
K                                                        K

                                     = LX� divgK (ea) volgK - LX� divgK (ea) volgK

                                     K                  K

                                     = - LX� divgK (ea) volgK .                  (2.30)

                                                  K

So the fibre-integral of the full norm of the mean curvature vector can be expressed as

   |N |2 volgK =       gM�           LX� log  volgK     LX log       volgK       volgK
                                              volg0                  volg0
K                 �,              K

                  -2              gM� Aa(X�) LX divgK (ea) volgK

                       �, , a                 K

                  +               gM� Aa(X�) Ab(X ) divgK (ea) divgK (eb) volgK  (2.31)

                       �, , a, b                     K

as a function on the base M . This formula displays explicitly the contribution of the
gauge fields Aa(X�) to this component of the scalar density on M .

2.5 Submersive metrics and gauged sigma-models

 The field theory consisting of a submersive metric on the product M � K governed by
 the higher-dimensional Einstein-Hilbert action has an alternative interpretation as four-
 dimensional gravity plus a gauged sigma-model. This sigma-model is a theory for maps
 M  M(K), where the target is the infinite-dimensional space of Riemannian metrics
 on K acted upon by the gauge group Diff(K), the group of diffeomorphisms of K. The
 nub of this view is the interpretation of the tensor S of the Riemannian submersion as
 a covariant derivative of the fibres' metric as one moves along the base M . This is the
 Kaluza-Klein analog of the covariant derivative of Higgs fields.

3This reference uses the opposite sign convention in the definition of divergence of a vector field.

                                                         26
    The purpose of this section is to describe this alternative viewpoint. The general idea
is partially present in the mathematical literature on Riemannian submersions, where one
studies the Ehresmann connection and holonomy groups associated to a submersion [Bes,
Her]. However, to highlight the correspondence with the objects present in traditional
Yang-Mills-Higgs models, we find it helpful to describe Riemannian submersions also
in terms of explicit Diff(K)-connections, Diff(K)-gauge transformations and covariant
derivatives expressed by local formulae such as (2.35). This seems to be new. Reading
this section is not an essential requisite to follow the arguments in the subsequent sections.
The presentation here is streamlined and we do not write down all the calculations and
proofs.

Covariant derivative of the fibre metric

A higher-dimensional metric gP on the product P = M � K determines by restriction a

natural map

                            gK : M - M(K) , x  gPx                          (2.32)

where gPx denotes the restriction of the metric gP to the fibre Px  K over the point x in
M . Now let X be a vector field on M and let U and V be vertical fields on P . We define
the covariant derivative of the map gK by the expression

             (dAgK)X (U, V ) := (LX gP )(U, V ) + Aa(X) (Lea gP )(U, V ) ,  (2.33)

where we are using the Einstein convention and summing over a basis {ea} of the space
of vector fields on K. The right-hand side of this equation is C(M )-linear in the X
entry and is C(M �K)-linear in the U and V entries, so dAgK is a section of the bundle
T M  Sym2(V ) over M � K. Here V  denotes the dual of the vertical sub-bundle of

T P . Of course by (2.21) we also have that

                            (dAgK)X (U, V ) = - 2 gP (SU V, X) ,            (2.34)

so this covariant derivative is essentially the same object as S in a different notation. To
recognize that the notation is justified, i.e. to recognize that the right-hand side of (2.33)
measures how the fibres' metric gK changes as one moves along the flow of X on the
base M , pick a local coordinate system {x�, yj} on the product M�K and the associated
trivializations of the tangent and cotangent bundles. Then a short calculation shows that
the covariant derivative can be locally written as

                            dAgK = (dAgK )�ij dx�  dyi  dyj

with coefficients given by

(dAgK )�ij := � (gK )ij + Aa� (ea)l l (gK )ij + (gK )li j(ea)l + (gK )lj i(ea)l (2.35)

                            27
as functions on M�K. The first term is just the derivative of the fibres' metric coefficients

gK  ,        along  the  four-dimensional           direction,   which  supports    the    interpretation
                                                x�
    yi yj

of dAgK, and hence S, as a covariant derivative of the fibre metric. From (2.34) it is

clear that the map gK will be "covariantly constant" along M if and only if the fibres of

P are totally geodesic (S = 0). This is consistent with the well-known result that in a

submersion with totally geodesic fibres the metrics of the different fibres are the image of

each  other  under  parallel  transport  [Her,  Bes].  Note  as  well  that  ea  =  (ea)l      was  defined
                                                                                           yl

as vector field on K, so the local coefficients (ea)l only depend on the coordinates yj. The

coefficients (gK)ij depend both on x and y, because the fibres' metric may change as one

moves along the base M . The gauge fields A�a only depend on x.

    To justify the designation of "covariant derivative" one should show that dAgK has
some kind of covariance property with respect to gauge transformations. Here we are

dealing with general Riemannian submersions, and this means that expansion (1.3) can

be taken over a basis {ea} of the full Lie algebra of vector fields on K, which as a space
coincides with the Lie algebra of the infinite-dimensional diffeomorphism group Diff(K).

So we will consider the full group of Diff(K)-gauge transformations on the bundle P  M .

Diff(K)-gauge transformations

A Diff(K)-gauge transformation is defined simply as a diffeomorphism  : P  P that
projects to the identity map on M through the bundle projection  : P  M . So we
have    = . Such a transformation defines a family of diffeomorphisms x : K  K,
parametrized by the points in the base x  M , through the natural identity

                              (x, y) = (x, x(y))

for all (x, y) in M � K. Gauge transformations act on the right on the space of metrics
on P through the pullback operation gP  gP . Since    =  this action preserves
the vertical distribution in T P , the Riemannian submersion property and the metric gM
on the base determined by gP . However, a gauge transformation in general will change
the horizontal distribution determined by gP , so it will have a nontrivial action on the
one-forms A(X) = a Aa(X) ea defined in (2.3). To write down the transformation rule
of A under gauge transformations, start by defining canonical one-forms  on M with
values in the vertical fields on P by

                                           d    x, tX(x)  x-1(y)             |t=0                   (2.36)
                    (X) |(x,y) := dt

where tX : M  M is the flow on M of the vector field X. It is clear that for the
identity gauge transformation x = id the one-form id is identically zero. Moreover, one

                                                28
can show that under composition 1  2 of two gauge transformations the one-forms 
transform as

                             12(X) = 1(X) + (1) [ 2(X) ] ,

where (1) denotes the push-forward of vertical vector fields on P . The transformation
rule A  A of the connection one-form under a gauge tranformation  is defined by

A(X) := -1 [ A(X) - (X) ] = - 1 [ A(X) ] + -1(X)

as vertical vector fields on P , for all vector fields X on the base M . With this rule one
can show that, for any gauge transformation , the covariant derivative (2.33) transforms
according to

 (dAgK )X = dA(gK ) X                                                 (2.37)

as a section of the bundle Sym2(V ) over M � K, for any vector field X on M . Here
gK denotes the map M  M(K) determined by the pullback gP of the higher-
dimensional metric, as in (2.32). Moreover, one can also verify that if a submersive

metric gP is represented by the data (gM , A, gK), in the spirit of (1.2), then the pullback
metric gP is represented by the gauge-transformed data:

gP  (gM , A, gK)           =      gP  (gM , A, gK) .                  (2.38)

Since the covariant derivative dAgK is just the fibres' second fundamental form in another
guise, one can wonder how this transformation rule looks like in terms of the tensor S.
The answer is given by the following identity, valid for all vertical vector fields U and V
on P , all vector fields X on M and all Diff(K)-gauge transformations:

(gP ) (S gP )U V, X =  gP (S gP )U V , X                        .     (2.39)

This is an identity of functions on P . We have also made explicit the dependence of S on
the higher-dimensional metric gP .

    If {vj} is a local trivialization of the vertical bundle V  M � K that is orthonor-
mal with respect to the pull-back metric gP , then the push-forward fields {vj} are
orthonormal with respect to gP . Thus, taking the metric trace of both sides of (2.39) we
get the transformation rule for the mean curvature vector:

(gP ) N , gP X =  gP N gP , X .                                       (2.40)

These rules imply that under gauge transformations the norms of these tensors change as

|S gP |2 gP =  |S gP |g2P         |N   gP  |2    =  |N gP |g2P     ,  (2.41)

                                             gP

                              29
where the notation signals that S, N and the norms all depend on the metric on P . The
standard invariance of integrals under diffeomorphisms then leads to, for instance,

   S vol gP 2      gP  =      S gP  2   volgP    =      S gP  2   volgP  .  (2.42)
                gP                  gP                        gP
P                         P                         P

This of course is very natural and outlines how the different components of the Einstein-
Hilbert action, not just the total action, are invariant under diffeomorphisms of P that
descend to the identity on M .

Covariant derivative of the fibre's volume form

A Riemannian metric on K defines a volume form on the manifold. So composing (2.32)
with this correspondence we get that each higher-dimensional metric gP determines a map

   volgK : M - k(K, R) ,                       x  volgPx .                  (2.43)

For any vector field X on M and any point x on that manifold we define the covariant
derivative of the map volgK by the expression

   DXA (volgK ) |x := d(volgK )x(X) + Aa(X) Lea[volgK (x)] .                (2.44)

This expression is C(M )-linear in the X entry and DXA (volgK ) is just another map
M  k(K). Not by accident, this definition of covariant derivative of the map volgK
determined by the submersive metric gP is very much related to the mean curvature vector
N of the submersion. Using (2.28) it is not difficult to verify the simple identity

                    DXA (volgK ) = - gP (N, X) volgK .                      (2.45)

The diffeomorphism group Diff(K) acts on the right on the space of volume forms,
k(K, R), so Diff(K)-gauge transformations  act on maps M  k(K). It is clear that
the volgK coincides with the map determined through (2.43) by the higher-dimensional,
pullback metric gP . Thus, combining (2.45) with rules (2.40) and (2.38) for the gauge
transformations of N and A, we get that

    DXA (volgK )          = -  gP (N, X) volgK
                          = (gP ) N , gP X volgK
                          = DXA (volgK ) .                                  (2.46)

So DXA (volgK ) deserves its designation as a covariant derivative under Diff(K)-gauge trans-
formations.

                              30
Einstein-Hilbert action in desguise

Combining the definitions and results of this section with decomposition (2.5) of the
higher-dimensional scalar curvature, we can write the Einstein-Hilbert action of a sub-
mersive metric gP as

  RgP volgP =     RgM  + RgK  -  1  |FA|2  -  1  |dAgK  |2  +  |DA (volgK )|2  volgP . (2.47)
                                 4            4
P              P

To derive this expression we have also used (2.11) and ignored the integral over P of the
total divergence term. The definition of the squared-norms of the covariant derivatives
are the natural ones, given the definition of the covariant derivatives themselves presented
before. The right-hand side of (2.47) broadly resembles the action of a four-dimensional
gauged sigma-model for the maps gK with a potential term -RgK and a gravity component
RgM . The difference is the presence of the additional term |DA (volgK )|2 and the fact that
the integral is over P , not over M . These differences can disappear in special situations
where we consider a smaller subset of submersive metrics as the domain of the action
functional. For instance, when K is an unimodular Lie group and we define the functional
only on the set of submersive metrics on M � K that are invariant under left group
multiplication on K and have fibres of unit volume. In this case the gauge group of
the sigma-model can be taken to be K, instead of Diff(K); the maps gK have values
in the finite-dimensional space of left-invariant metrics of unit volume on K, instead of
having values on the whole M(K); and after dimensional reduction by fibre integration
the functional (2.47) becomes the traditional action of four-dimensional gravity plus a
gauged sigma-model on M .

                                     31
3 Dynamical models on M4 � K

3.1 Lagrangian densities

The purpose of this short section is to bring together previous work and write down the
Lagrangian density whose dynamics will be studied subsequently. According to (2.5), in
a Riemannian submersion the higher-dimensional scalar curvature can be written as

RgP = RgM + RgK - |F |2 - |S|2 - |N |2 - 2 N .

From (2.11), the function N can be expressed as combination of the norm |N |2 and the
divergence divgP (N ), so an alternative formula for the scalar curvature on P is

RgP = RgM + RgK - |F |2 - |S|2 + |N |2 + 2 divgP (N )

= RgM + RgK - |F |2 - |S�|2 +       1  |N |2 + 2 divgP (N ) .  (3.1)
                               1-

                                    k

The last equality used identity (2.13) between the squared-norm of S and that of its
traceless part S�. When included in the higher-dimensional Einstein-Hilbert action, each

one of these components will have a different role, or interpretation, in terms of four-
dimensional physics. The term RgM generates four-dimensional gravity; |F |2 is the kinetic
term for the Yang-Mills fields; |S�|2 and |N |2 are the kinetic terms for the scalar fields that
describe how the internal metric gK varies from fibre to fibre, with |S�|2 associated to the
variations that preserve the internal volume form and |N |2 associated to the variations

of volgK ; the opposite -RgK plays the role of a classical potential for those scalar fields;
finally, the total divergence divgP (N ) can be ignored in the action if standard boundary
conditions are assumed on M .

    One point that should be made is that, once the higher-dimensional action E(gP ) is
restricted to the domain of submersive metrics on M �K, instead of all possible metrics on
this space, each of the previously described components gets a life of its own, independent
of the higher-dimensional scalar curvature. By this we mean that RgK , |F |2, |S�|2 and the
remaining terms are all natural geometric functions on M �K that can be included or not
in an action functional for gP . In the gauged sigma-model interpretation of submersive
metrics, each one of those terms is Diff(K)-gauge equivariant, as exemplified in (2.41),
and so produces a Diff(K)-gauge invariant term in the functional E(gP ), as exemplified in
(2.42). Thus, once the domain of the functionals is restricted to submersive metrics, there
are natural generalizations of the Einstein-Hilbert action on M � K, namely any linear
combination of the components RgM , |F |2, |S�|2, etc., not necessarily with the coefficients
that appear in the curvature (3.1).

                          32
    In these notes we will not analyze this general action functional for submersive metrics.
Instead, we will restrict ourselves to studying a modest generalization of the Einstein-
Hilbert action by allowing an arbitrary coefficient of the mean curvature term |N |2. This
is the kinetic term for the fields that control the volume of internal space, which are directly
related to the gauge couplings and play an important role in Kaluza-Klein models. Thus,
here we will consider the higher-dimensional action

                1      RgP -  |N |2 - 2   volgP                                     (3.2)
E(gP ) := 2 P                                                                   volgP ,
                   P

      1               RgM + RgK - |F |2 - |S�|2 -                1  |N |2 - 2 
=                                                      -1+
                   P
    2 P                                                          k

where P ,  and  are real constants and in the last equality we have ignored the total
divergence term. When  = 0 this definition reduces to the traditional Einstein-Hilbert
action, which remains the most natural one because it is also defined for non-submersive
metrics on M � K.

    In a somewhat unrelated drift, before ending this section we note that there is a
nice combination of the scalar curvature RgP with the two functions |N |2 and divgP (N )
that satisfies a particularly simple rule of transformation under Weyl rescalings of the
submersive metric. The combination is

W (gP )  :=  RgP   -  (m + k - 1)(m + k - 2)  N2            (m + k - 1)  divgP N ,  (3.3)
                                   k2              gP  -2

                                                                   k

where m and k denote the dimensions of M and K, respectively. Indeed, if  : P 
R+ is any positive function with constant values on the fibres and g~P := 2 gP is the
corresponding Weyl transformation, it is shown in appendix A.1 that the function W
calculated for the rescaled metric satisfies the simple relation

                      W (g~P ) = -2 W (gP ) .

This contrasts with the complicated behaviour of the curvature RgP under the same Weyl
transformation. It is clear from the results of appendix A.1 that this simple transformation
rule will also hold for any linear combination of W (gP ) with the scalar functions |S�gP |2
and RgK on the higher-dimensional space P .

3.2 Mass of the gauge bosons

The calculations leading to a mass formula for the fields Aa� on M mimic, in every essential
way, the calculations usually performed in the case of the electroweak gauge fields of the
Standard Model [Wei, Wei3, Ham]. One works in the approximation where the gauge

                                                       33
fields Aa� are small, close to their vanishing vacuum value, and where the internal metric
gK (the restriction of gP to the fibres K) is constant as one moves across the fibres and
equal to the vacuum metric gK0 .

    Start by combining definition (3.2) of the action E(gP ) with the results of section 2,
which express the different components of RgP in terms of the data (gM , A, gK), equivalent
to the submersive metric gP . After fibre-integration, one finds that the terms of the four-
dimensional Lagrangian density that depend on the field Aa� are proportional to

1       gM�    gM  (FAa )�  (FAb )  Bab  +  gM� Aa� Da   +  gM� Aa� Ab Cab .        (3.4)
4

The coefficients Bab, Cab and Da depend on the metric on the internal space and are
given by the fibre-integrals

Bab :=         gK0 (ea, eb) volgK0

        K

            1      Lea gK0 , LX gP0  + 4 (1 - ) LX (divgK0 ea)  volgK0
Da := 2
               K

           1       Lea gK0 , Leb gK0  + 4 ( - 1) (divgK0 ea) (divgK0 eb)  volgK0 .  (3.5)
Cab := 4 K

Working with the Levi-Civita connection M on M and ignoring total derivatives, the
first variation of (3.4) with respect to (Aa)� leads to the equations of motion

                   gM� gM (M FAa)� Bab - 2 gM� A�a Cab = 0 .

When the vector fields ea on the internal space K are chosen to simultaneously diagonalize
the quadratic forms Bab and Cab, the equations of motion reduce to

                   gM� (M FAa)�          -  2   Caa  Aa  =  0.                      (3.6)
                                                Baa

The usual arguments using the Lorenz condition �Aa� = 0 (e.g. see [MS, section 2.7])
then say that, to first order in the fields, these equations can be simplified to the Klein-
Gordon equation for fields on M4 of squared-mass equal to 2 Caa/Baa. So we get a formula
for the classical mass of the gauge fields:

Mass Aa� 2 =       K Lea gK0 , Lea gK0  + 4 ( - 1) (divgK0 ea)2 volgK0 .            (3.7)
                                     2 K gK0 (ea, ea) volgK0

Thus, the classical mass of the field A�a is determined by the geometrical properties of the
vector field ea with respect to the vacuum metric gK0 on the internal space. The relevant
quantities are the L2-norm of ea, the divergence of ea and the Lie derivative of the vacuum

                                            34
metric in the direction of ea. For instance, if the vector field ea is Killing with respect
to gK0 , then both the divergence and the Lie derivative vanish, so the fields A�a will be
massless for this particular value of the index a. In a sense, the classical mass of a gauge
boson is a measure of how much the internal metric changes along the flow generated by
the corresponding internal vector field.

    The right-hand side of the mass formula is manifestly non-negative for all vector fields
ea with vanishing divergence on (K, gK0 ), i.e. for all vector fields that preserve the vacuum
volume form volgK0 on the internal space. However, if we associate gauge fields also to
vector fields with non-vanishing divergence on K, we could end up with negative masses,

unless the freedom in the parameter  of the Lagrangian is used to prevent this.

    In general, on a Riemannian manifold the Lie derivative LV g can be decomposed as

                                                  2
                                      LV g = n divg(V ) g + V ,
where n is the dimension of the manifold and V is a symmetric 2-tensor satisfying the
traceless condition j V (vj, vj) = 0, where {vj} denotes a local, g-orthonormal trivializ-
ation of the tangent bundle. Taking the norm of both sides of the equation, a calculation
analogous to (2.12) and (2.13) leads to

                       LV g, LV g         -  4     (divg  V   )2  =  V , V                0,                     (3.8)
                                             n

with equality only if V = 0, i.e. only if V is a conformal Killing vector field with respect
to g. Applying (3.8) to the numerator of the mass formula we obtain that

     Lea gK0 , Lea gK0  + 4 ( - 1) (divgK0 ea)2           =   ea, ea + 4                     1    (divgK0 ea)2 .
                                                                                   -1+

                                                                                             k

Thus  when       >  1-  1  it  is  clear  that     all  gauge     fields  have   non-negative     mass,   with    the
                        k

massless case occurring precisely when the Aa� are associated to Killing vector fields on

the  internal  space.  When    the  parameter             is  equal  to   1-  1    all  the  masses  are  still  non-
                                                                              k

negative, but the massless case occurs in the slightly more general situation of gauge

fields associated to conformal Killing vector fields on K.                      For       <   1-  1  all  the  gauge
                                                                                                  k

fields associated with zero divergence vector fields still have non-negative mass, but for

example any gauge field associated with a conformal Killing vector field that is not Killing

on (K, gK0 ) (if such fields exist) will have negative mass.

    The mass formula for A�a is manifestly invariant under a rescaling of the internal vector
field ea by a positive constant. This is equivalent to a rescaling of the gauge field A�a.
On the other hand, if one considers a constant rescaling of the internal vacuum metric,

g~K0 = 2 gK0 with 2 in R+, it is easy to check that (3.7) rescales as

                               Mass Aa�      2     =      -2      Mass Aa�    2    .                             (3.9)
                                             g~K0                             gK0

                                                          35
This follows from the observation that, for any vector field V on K, the quantities
LV g, LV gg and divg V are both invariant under a constant rescaling of g, which itself
follows from definition (2.24) of the inner-product and formula (2.26) for the divergence.
Thus, reducing the size of the vacuum internal space leads to an increase of the classical
masses of all the massive gauge bosons.

    We would like to end this section with two cautionary comments. Firstly, the tradi-
tional arguments that lead to the identification of the coefficient 2 Caa/Baa in equation
(3.6) as the mass of the gauge field are well-justified only in the case where (M, gM )
is Minkowski space. In curved backgrounds the concept of mass of a gauge field is less
clear-cut and should be used with caution. Secondly, note that the mass formula (3.7) was
derived from the terms (3.4) of the four-dimensional Lagrangian density, which themselves
were obtained by dimensional reduction (through fibre-integration) of the corresponding
terms in the higher-dimensional action E(gP ), written in (3.2). However, a more complete
of analysis of that dimensional reduction shows that it leads to a gravity Lagrangian for
gM that is not in the Einstein frame, but is in the alternative Jordan frame. Since Lag-
rangians in the Jordan frame are generally disfavoured for a good physical interpretation
of four-dimensional theories [FGN], further ahead we will redefine the fields in order to
obtain a higher-dimensional action that produces a 4D Lagrangian in the Einstein frame,
after dimensional reduction. After this process is complete the mass formula for the gauge
fields will be slightly changed, with the appearance of an overall factor related to the total
volume of (K, gK0 ). The new mass formula is calculated in appendix A.2 and the result is
stated in (A.23). It has a scaling behaviour under constant rescalings of gK0 distinct from
(3.9). Namely, formula (A.23) implies that the bosons' squared-mass scales more strongly
as -2-2k/(m-2), where k and m are the dimensions of K and M , respectively, instead of
scaling as -2. In contrast, the relative masses of the different gauge bosons are the same
in (3.7) and (A.23).

3.3 Stability of product Einstein solutions

Submersive metrics on M � K have degrees of freedom associated to the spacetime metric
gM , the gauge fields and the internal metric gK. Decomposing the higher-dimensional
scalar curvature, we recall, allowed us to define a generalized Einstein-Hilbert action

               1     RgM + RgK - |F |2 - |S�|2 +             1  |N |2 - 2   volgP .  (3.10)
E(gP ) = 2 P                                      1--
                  P
                                                            k

In this section we study configurations with vanishing gauge fields, so vanishing tensor F.
Starting with a product Einstein metric gMe + gKe on P , which is solution of the higher-
dimensional equations of motion, we study the second variation of the action functional

                     36
under small perturbations of the internal metric gK. The perturbations can be both
through Weyl rescalings or TT-deformations. The purpose is to calculate the mass of the
four-dimensional perturbation fields and better understand the stability properties of the
initial product Einstein solution. The calculations replicate very standard methods used to
study the stability of general Einstein metrics under the Einstein-Hilbert action, described
for instance in [Bes, Kro], applied to the case of the action (3.10) for submersive metrics
near product Einstein solutions. The main takeaway is that while there is at most a finite
number of unstable TT-deformations of gKe , the number of negative-mass perturbation
modes associated to Weyl recalings of gKe depends on the value of the constant . For
small  there is just one such mode, corresponding to Weyl rescalings that are constant
in the K-direction. For  > 1 - 1/k there will be infinite unstable modes.

Let us perturb the product Einstein metric gMe + gKe by a variation with parameter t:

gPt := gMe + gKt = gMe + gKe + t h + f gKe + LE gKe .              (3.11)

Here h is a transverse, traceless variation of the fibre metrics in the vertical direction, so
that h restricted to each fibre is a TT-tensor on K, although this tensor may vary from
fibre to fibre; f is a real smooth function on M � K; the term LE gKe denotes the Lie
derivative of the Einstein metric along some vertical vector field E on P , so is a variation
of the metric through an infinitesimal diffeomorphism of the fibres. This represents the
most general variation of the fibre metrics gK, as follows from standard results [Bes].

    The variation of gMe + gKe by fibre diffeomorphisms does not change the total Einstein-
Hilbert action nor the integral of its components |S|2 and |N |2. This was observed in (2.41)
and (2.42), for example. So we may as well take E = 0 and ignore the term LE gKe when
calculating the second variation of the total action.

    For vanishing gauge fields, formula (2.21) applied to the variation gPt implies that the
traceless part of the fibres' second fundamental form satisfies

       2 gPt (S�gPt )U V, X |E=0 = - t (LX h)(U, V )

for all vertical vector fields U and V on P and for all fields X in M . Similarly, from (2.28)
it follows that for vanishing gauge fields

             2 gPt (N , gPt X) |E=0 = - t k LX f .

Taken together these formulae imply that the total variation of the squared-norms is

  |S�|2gPt volgPt    =  t2    gM�  LX� h, LX h gKe volgPe + O(t3)
                        4
P                           P

   |N  |2    volgPt  =  t2 k2    gM� (�f ) (f ) volgPe + O(t3) .   (3.12)
                          4
P       gPt                    P

                               37
Note in passing that these last formulae are valid even for non-vanishing E, because
integration kills all variations through diffeomorphisms. In any case we conclude that
the expansion of the components |S�|2 and |N |2 of the higher-dimensional scalar curvature
produces dynamical terms in the action for the perturbation fields h and f , respectively,
involving their derivatives in the four-dimensional spacetime directions.

    In contrast, the fibres' scalar curvature RgKt depends on the deforming tensors h, f
and their derivatives in the vertical, K-directions, with no derivatives in the spacetime
directions. So one recognizes that the fibre integral

                                                RgKt (h, f ) volgKt ,

                                                                    K

which is a scalar function on M , plays the role of a spacetime potential for the perturb-
ation fields. The integral of the internal scalar curvature is invariant under the group of
diffeomorphisms of K, so the variations of the vacuum metric in the directions tangent to
diffeomorphisms preserve this potential. The fields h and f , on the other hand, represent
variations of gKe that are transverse to diffeomorphisms [Bes] and may change the value
of the potential.

    The classical masses of the perturbation fields are essentially the eigenvalues of the
Hessian of the potential evaluated at the initial solution. They can also be extracted from
the linearized equations of motion of the fields. So we should start by considering the
potential-like components of the higher-dimensional Einstein-Hilbert action,

                        P  RgM e + RgKt - 2  volgPt =              M  V(t) volgM e ,

and calculate the second variation of the spacetime potential

     V(t) :=           RgKt - 2  + RgM e           volgKt  =    V(0) +   t2 V(0) + O(t3) .
                                                                         2
                   K

There is no linear term in t because gMe + gKe is a solution of the higher-dimensional
equations of motion and gKe is an Einstein metric on K. The second variation of the
Einstein-Hilbert functional V(t) is very well-known [Bes, Kro]. It can be written as

V(0) = 1           -  h, h - 2 R�gKe h gKe + (k - 2) (k - 1) f gKe f - RgKe f 2             volgKe .
            2
               K

Here gKe denotes the positive Laplacian on K and, in the case of an Einstein manifold,
                                                                                                  gKe
the  operator  in  the  first  term  essentially   coincides  with  the  Lichnerowicz  Laplacian     L

acting on symmetric 2-tensors on K,

                           h         -  2 R�gKe h  =   gKe   h  -   2
                                                          L         k RgKe h .

                                                   38
We have also used the relations

                                          k                    2k
                              RgKe = m RgM e = m + k - 2                                           (3.13)

to eliminate RgM e and  from the end result and write them in terms of RgKe . These
relations follow from the fact that gMe + gKe is an Einstein metric on M � K with higher-
dimensional cosmological constant . The letters m and k denote the dimension of M

and K, respectively. In summary, up to second order in t the action (3.10) is

                 E gMe + gKt  = E gMe + gKe              +     t2  (If  +     Ih)  +  O(t3)
                                                               2

with

        1     - gM�                               1  h,  k  gKe    h    -  2 RgKe h   gKe  volgPe  (3.14)
Ih = 2                    LX� h, LX h gKe - k                  L

           P

        1     k(k - k - 1) gM� (�f ) (f ) + (k - 2) (k - 1) gKe f - RgKe f f                       volgPe
If = 2
           P

Through variation it leads to the linearized equations of motion of the perturbation fields:

           gM� �(LX h)    -   gKe   h  +  2              =  0                                      (3.15)
                                 L        k RgKe h

           k (k - k - 1) gM� �(f ) - (k - 2) (k - 1) gKe f - RgKe f = 0 .

These are equations on the total space M � K. Recall that the fields f and h represent
deformations of the higher-dimensional metric around a classical solution gMe + gKe . These
deformations change the internal metric gK in directions transverse to diffeomorphisms,
while leaving the spacetime metric and the Riemannian product structure unchanged.
For vanishing , the equations above are just the linearization of the Einstein equations
on M � K in the direction of these deformations. There is no equation for the vector field
E of (3.11) because diffeomorphisms preserve the Einstein equations, so the linearization
is trivial in that direction.

To obtain equations of motion in four dimensions from equations (3.15) on M �K, one

should decompose the function f as a sum of eigenfunctions n of the scalar Laplacian

gKe on K. In parallel, one should decompose the field h of TT-tensors as a sum of
                                                     gKe
eigentensors  n  of  the  Lichnerowicz  Laplacian       L   .  Both     these  Laplacians    are   elliptic,  self-

adjoint operators on the compact (K, gKe ) with respect to the L2-inner-product of scalar

functions and TT-tensors, respectively. They have finite-dimensional eigenspaces with

real eigenvalues that form a discrete, increasing sequence in the real line that accumulates

only at + [BHM, Kro]. We write the decompositions as

              h(x, y) =        hn(x) n(y)                   with        gKe   n    =  n n
              f (x, y) =                                                   L
                              n=0
                                                               with gKe n = n n .                  (3.16)
                               f n(x) n(y)

                              n=0

                                                     39
Here x denotes the coordinates on M and y denotes the coordinates on K, so the coeffi-
cients of the expansions are real functions on four-dimensional spacetime. We also assume
that the real eigenvalues n and n are ordered in non-decreasing sequences. Substituting
(3.16) into the equations of motion of h and f we obtain Klein-Gordon equations on M
for the coefficient fields hn(x) and f n(x),

gM� �( hn) +  2           hn = 0                                   (3.17)
              k RgKe - n                                           (3.18)

k (k - k - 1) gM� �( f n) - (k - 2) [(k - 1) n - RgKe ] f n = 0 .

The squared-mass parameters of the fields are then:

(Mass hn)2    =  n        -  2
                             k RgKe

(Mass f n)2 = (k - 2) [(k - 1) n - RgKe ] .                        (3.19)
                           k (k - k - 1)

Since the eigenvalues of the Lichnerowicz Laplacian form a discrete, increasing sequence
that accumulates only at positive infinity, we know that the number of unstable modes
hn will always be finite, if non-zero. Furthermore, for an Einstein metric gKe with positive
scalar curvature that is not a standard sphere, the non-zero eigenvalues of the scalar
Laplacian always satisfy [Ob, Kro]

                                   (k - 1) n > RgKe for n  1 .

This means that for k > 2 and n  1 the squared-mass of the modes f n has the same sign
as the factor (k - k - 1). On the other hand, since the scalar Laplacian has 0 = 0, for
k > 2 and RgKe > 0 we recognize that the squared-mass of the mode f 0 has the opposite
sign to the factor (k - k - 1). So for an Einstein metric gKe with positive scalar curvature
it is not possible to have non-negative squared-masses for all the modes f n unless k = 2, in
which case all the modes will be massless, or unless  = (k - 1)/k, in which case all these
modes are non-dynamical on spacetime and equation (3.18) only has the zero solution.

    Thus, when the constant  is zero or small, corresponding to the traditional Einstein-
Hilbert action on M � K, only the mode f 0 has negative squared-mass among all the
perturbation modes f n.

    Observe also that the kinetic term for the field f in the second integral of (3.14) appears
with a flipped, positive sign unless   (k - 1)/k. Such a positive sign would violate the
requirements of the weak energy principle for coupling the scalar curvature RgM to matter
fields in the four-dimensional Lagrangian [HE]. However, (3.14) is a truncation of the full
higher-dimensional Lagrangian and, after fibre integration, it produces a four-dimensional

                          40
Lagrangian in the Jordan frame, not in the standard Einstein frame where the weak energy
principle is stated. A transformation to the Einstein frame can change the sign of scalar
kinetic terms, as will be seen in detail in the next section. So a definite evocation of the
weak energy principle would require additional care in these circumstances.

3.4 Lagrangian in the Einstein frame

Dimensional reduction of our action (3.2) produces a Lagrangian in four dimensions that
is not in the Einstein frame, but is in the alternative Jordan frame. This means that the


gravity component of the Lagrangian does not appear in the traditional guise RgM -gM ,
but instead appears multiplied by a scalar factor that depends on the spacetime coordin-
ate. This scalar factor is a hallmark of Kaluza-Klein theories. It is related to the volume
of the internal space over each spacetime point, which in general can vary along M .

    Since Lagrangians in the Jordan frame are generally disfavoured for a good physical
interpretation of the four-dimensional theory [FGN], in this section we will use a Weyl
rescaling to redefine what is understood to be the physical, four-dimensional metric gM .
After this redefinition, dimensional reduction does produce a 4D Lagrangian in the Ein-
stein frame. This technique to transform a Lagrangian from the Jordan to the Einstein
frame is very standard [OW, FGN]. In the case of action (3.2) the computations are
somewhat evolved because one first has to obtain the transformation rules of the norms
|F |2, |S|2 and |N |2 under the rescaling, which can then be combined with the standard
transformation of the curvature RgM . These calculations are summarized in appendix A.1.

    In order to study the dynamics of the rescaling field --which, recall, measures the
volume of the internal space--we also want its kinetic term to appear with the standard
Klein-Gordon normalization in the dimensionally-reduced Lagrangian. This requires ad-
ditional care in the definition of . The main output of this section is the expression of
the higher-dimensional action in the Einstein frame registered in (3.22) and (3.28).

    To describe that result, start by recalling that a submersive metric gP on the bundle
M � K  M defines a metric gM on the base, gauge fields on the base and a family of
metrics gK on the internal spaces K, one metric for each fibre. A distinctive degree of
freedom of the internal metrics is their overall scale, and how it varies from fibre to fibre.
This is the variable of interest in this section, so let us autonomize it by explicitly writing

gK = a1 e-b1 g�K ,                    (3.20)

where the metrics g�K on the fibres are arbitrary but have fixed volume over K, normalized
to a given value ; the real function  on M determines the scale of the fibres; a1 and b1

41
are positive constants that we will specify later on. So the field  is similar to the mode
f 0 of last section except for the constants.

    Let us also declare that the "physical" metric gM over spacetime is not the simple
projection of gP down to M , but is instead the rescaled version of the projection that pro-
duces a spacetime Lagrangian in the Einstein frame after dimensional reduction. In other
words, produces a Lagrangian with a gravitational component that coincides with that of
traditional GR. This can be achieved be a redefinition of the form gM  a2 eb2 gM . Thus,
when writing the submersive metric gP as a triple in the spirit of (1.2), the components
can be written in terms of the redefined fields as

       gP  a2 eb2 gM , A , a1 e-b1 g�K .                                  (3.21)

To determine the appropriate value of the constants and to study the dynamics of the

field  we should write action (3.2) in terms of the rescaled variables, that is, we should

write    1

       E(gP ) = 2 P        L(, gM , A, g�K) volg�P ,                      (3.22)

                        P

where g�P denotes the unscaled submersive metric on P ,

         g�P  gM , A , g�K .                                              (3.23)

The calculation of the expanded Lagrangian density L(, gM , A, g�K) is a slightly lengthy
one, using the results of appendix A.1. To write the result in a readable format let us
first introduce some notation. The fixed normalization of the metrics g�K is defined by a
dimensionless, positive constant   R+ through the relation

         Vol(K, g�K) = -M1 P  ,                                           (3.24)

where Vol(K, g�K) denotes to total volume of the manifold and M stands for the Einstein
gravitational constant, so 8Gc-4 in the four-dimensional spacetime. Let us also define
the positive constant

         m + k - 2 1/2                                     m - 2 -1/2
        := 2 M (m - 2)k      1+k                                       ,  (3.25)
                                      m+k-2

where m and k denote the dimensions of M and K, respectively. Here we are assuming

that                     m+k-2

         >-              k(m - 2)                       ,                 (3.26)

otherwise the constant  is not well defined. Then with the choices

                                                    -2                    (3.27)

         a2 = a1 =  m+k-2

                     k                                  k
         b2 = m - 2 b1 = m + k - 2

                         42
the expanded Lagrangian can be written as

                          1  RgM - M |d|2gM + Rg�K e - 2  a2 eb2 - | F |g2�P e-
L(, gM , A, g�K) := 

                             - | S�g�P |g2�P +             1          |Ng�P |2g�P  .               (3.28)
                                                1--

                                                          k

    Now, by definition all the fibres of (P, g�P ) have the same fixed volume, equal to the
normalized volume of g�K, so after fibre-integration we do get

   1    RgM - M |d|g2M volg�P =                                         1  RgM     -    1  |d|g2M  volgM .
2 P  P                                                                2 M               2
                                                                   M

This means that the field redefinitions (3.21), with constants (3.27), produce a dimen-

sionally reduced Lagrangian with a gravitational component in the Einstein frame, as

required, and with the kinetic term of the scalar field appearing in the canonical normal-

ization. This is the main result of this section.

    If condition (3.26) on  were not satisfied, the kinetic term |d|g2M would appear with
the wrong sign in the Lagrangian. If  takes the critical value

                                            m+k-2
                                0 = - k(m - 2)

the kinetic term |d|g2M disappears altogether, so the equation of motion of  becomes just
a constraint.

    The detailed calculation of Lagrangian (3.28) uses the rescaling identities (A.12) of
appendix A.1 in the special case where 2f = -b1 + log a1 and 2 = b2 + log a2. The
metrics g~P and gP in that appendix are taken to stand for the metrics gP and g�P of this
section, respectively. Besides employing these identities, one also needs to use that

          |N |g2P volgP      =  1               (k b1)2  |d|g2�P      +    |Ng�P |2g�P     volg�P
                                                   4
        P                          P

with no cross terms involving both d and Ng�P . This result follows from the last identity
in (A.12) after observing that the cross term is proportional to

        g�P Ng�P , gradg�P  volg�K =                     g�P Ng�P , gradgM  volg�K                 (3.29)

K                                                   K

                                                = - L gradgM  Vol(K, g�K ) ] = 0 .

Here we have used formula (2.29) and the constancy of the fibre-volume Vol(K, g�K) on
M for the normalized metrics g�K. We have also used that the gradient gradg�P , with 
regarded as a function on P that is constant along the fibres, is the horizontal lift to P
of the gradient in the base gradgM , with  regarded as a function on M .

                                                43
    For a clearer interpretation of the re-definition gM  a2 eb2 gM of the physical metric
on M , as carried out in (3.21), it is also worth noting that

                                                                                          2/(2-m)                  (3.30)

                           a2 eb2 = P-1 M Vol(K, gK )

as functions on the base M . This follows from (3.20) combined with (3.24) and (3.27).

    To end this section we will extract the equation of motion of the scalar field  and
compare it with the analogous, simpler equation often discussed in the setting of five-
dimensional Kaluza-Klein. Varying Lagrangian (3.28) with respect to  and ignoring
total derivatives yields the equation:

M (gM )� M � ( ) +  |F |g2�P e- +  Rg�K e - 2  a2 b2 eb2 = 0 . (3.31)

In the traditional, five-dimensional Kaluza-Klein model  is zero and the internal space
is the circle S1. So the internal scalar curvature Rg�K vanishes. Moreover, the usual first-
order analysis of this model takes all fields to be independent of the internal coordinate, so

the only internal degree of freedom is the scaling factor . This means that the normalized

internal  metric  g�K  is  trivial,  the  same  constant  number  everywhere,                            and  the  tensors  Sg�P

and Ng�P  necessarily vanish.        Taking m = 4 and k = 1 we get that                                =       6M and the
previous  equation of motion                                                                          -6                     
                                     reduces  simply  to    M  (M  )�(�)                           =
                                                                                                              |F |2g�P e- 6 M .

Thus, the squared-norm |F |2 should vanish in any region of spacetime where  is approx-

imately constant, as required for the good interpretation of the gauge coupling constants

at present time. This constrains the electromagnetic field and is often cited as a difficulty

of the five-dimensional Kaluza-Klein model. This difficulty appears to be less blatant in

the higher-dimensional models represented by equation (3.31), since in regions where  is

approximately constant we are left with the more evolved constraint

                       |F |2g�P  +   Rg�K e2    -   2  k a2 e(b2+)                                 0  .            (3.32)
                                                   m+k-2

So the squared-norm |F |2 of the Yang-Mills curvature can be non-zero and vary in this

region, as long as those changes are compensated by appropriate spacetime variations of

the normalized internal metric g�K, which determines the function Rg�K . Moreover, these
equations of motion are derived solely from the traditional Einstein-Hilbert action on P ,

which may not tell the whole story in a realistic model operating at different scales.

3.5 Gauge coupling constants in the Einstein frame

The purpose of this section is to write down a formula for the scale of the gauge couplings
as extracted from the Lagrangian in the Einstein frame. We start from the Einstein-
Hilbert action on M � K, assume a vacuum internal metric gK0 that is constant around
present time and adapt a general result of Weinberg [Wei2].

                                                       44
    In the traditional Kaluza-Klein setting, the result [Wei2, eq. 16] says that the gauge
coupling constants are of the order

                           W 2 ein =  82M              82M       ,
                                                         l2
                                      N  l2
                                                            gK0
                                          gK0

where N is a positive integer and lgK0 denotes the average length (root-mean-square) of the
circumferences on the internal space (K, gK0 ) generated by the vector field associated to
the gauge field. The conventions in [Wei2] differ from the ones used here, however. Firstly,
the symbols 2, �2 and ge used there correspond to what we denote here by 2M , 2P
and Wein, respectively. More importantly, [Wei2] does not perform the field redefinitions
to obtain the general, dimensionally-reduced Lagrangian in the Einstein frame, as was

done here on the way to (3.28). Instead, along the lines of the traditional Kaluza-Klein

ansatz, [Wei2] fixes the value of the constant P to be M VolgK0 , which produces a 4D
Lagrangian in the Einstein frame only in the case of a constant internal metric, gK = gK0 .
So the relevant terms of the dimensionally-reduced action considered in [Wei2] are

   1                          1                     |F |2gM +gK0 volgK0
   M 2M RgM - 2 M VolgK0                                                       volgM .                 (3.33)
                                                  K

In contrast, in the present notes the constant P is not constrained a priori because the
metric gM was redefined in order to obtain a Lagrangian in the Einstein frame in all
circumstances, even when the internal metric is not constant throughout spacetime. In

the case of a constant internal metric in the vacuum configuration, the relevant terms of

our Lagrangian (3.28) are

   1                       1               |F |2gM +g�K0 e-0 volg�K0           volgM .                 (3.34)
   M 2M RgM - 2 P 
                                         K

Here we have used (3.23) and the notation |F |g2M+g�K0 means that the norm (2.17) should
be evaluated using the metrics gM and g�K0 . Now we want to write this relation in terms
of the internal vacuum metric gK0 instead of the normalized metric g�K0 . From (3.20) and

definition (2.17) it is clear that

   |F |g2M +g�K0 volg�K0 = a1 e-b1 -1-k/2 |F |2gM +gK0 volgK0 .

Using definitions (3.27) one calculates that

                              k+2     (m-2)(k+2)0                                                 m-4
                           m+k-2          2(m+k-2)
                                                                                   b2 0 2
                                                                               2
a e =  e =  e a e . -b10 -1-k/2                                     0
  1

Applying identity (3.30) we obtain that the terms (3.34) can be re-written as

                                                  m-4
                           -P 1M VolgK0 2-m
     1                            2 P                     |F     |2    volgK0  volgM .                 (3.35)
   2M RgM -
M                                                      K          gK0

                                              45
Since our constant P is unconstrained, we are considering here a slight variation of the
action (3.33) of [Wei2]. If we use our action in the calculations of [Wei2], the end result
for the scale 2 of the gauge coupling constants is instead

                                                                    -2  (3.36)

           2 = -P 1M VolgK0 m-2 W 2 ein .

This is true because the denominators in front of the Yang-Mills term in (3.33) and (3.35)

differ by

               m-4                     -2
           2 P -P 1M VolgK0 m-2 = P-1M VolgK0 m-2 2 M VolgK0 ,

and, as is well-known, a rescaling of those denominators is equivalent to a rescaling of the

squared gauge coupling constants by the same amount. Thus, in the Einstein frame we

obtain

           2         82 M         2.                                    (3.37)

               l2    P-1M VolgK0  m-2

                gK0

This reduces to the traditional expression when P = M VolgK0 , but here P remains
unconstrained. Notice also that the gauge couplings calculated in the Einstein frame
scale exactly as the gauge bosons' masses of (A.23) when the vacuum metric gK0 changes
by a constant factor. This scaling behaviour is different from that of Wein. This happens
because, in the traditional derivation, a volume factor is hidden in the normalization of
the constant P , which in fact becomes a non-constant for a rescaling gK0 .

3.6 Unstable modes and scalar field inflation

Early dynamics of the unstable mode 

The purpose of this section is to study the dynamics of the scaling field  in the approx-
imation where all gauge fields are zero and the other internal scalars are static. This
is a coarse approximation, but could describe the initial stages of the unravelling of an
unstable, higher-dimensional Einstein product metric on M � K. In this regime, the
dynamics of the scaling field is controlled by a simple potential V () that will be written
down and cursorily investigated. When the Einstein metric on K also has TT-instabilities
the initial dynamics of  will be more evolved, since it will develop concurrently with in-
ternal symmetry breaking. Such an example will be described further ahead, in section
3.8, in the case K = SU(3).

    Let us suppose that, over an ancient region of spacetime, the metric on M � K can be
approximated by an Einstein product metric gPe = gMe + gKe with positive constant. The

                     46
scalar curvatures necessarily satisfy

                               2k                    RgM e                                 2m                 (3.38)
                 RgKe = m + k - 2                                                    =                .
                                                                                        m+k-2

This Einstein product is an unstable solution of the higher-dimensional equations of mo-

tion. In section 3.3 we saw that the number of unstable modes of perturbation is finite,

at least for the internal metric. They include the fibre-rescaling mode represented by the

real field  and, depending on the details of gKe , a possibly non-zero but finite number of
perturbations by fields of TT-tensors on K. Let us further assume that the most unstable

direction of perturbation (i.e. the direction with the most negative eigenvalue of the

Hessian) is the rescaling mode represented by . This is true in the example K = SU(3)

studied further ahead. Then one expects that the metric gMe + gKe will first unravel in the
-direction. Thus, in a slightly larger region of spacetime, the metric on M � K would

be well-approximated by a rescaled, warped product metric of the form (3.21), with no

gauge fields and a normalized internal metric g�K that is constant throughout the region
and proportional to the Einstein solution. So let us take the normalized internal metric

of (3.21) to be

                                       P-1M VolgKe              2
                                                           g m-2 e
                         g�K :=                                     K                      ,                  (3.39)

where VolgKe denotes the total volume of gKe and the (so far arbitrary) constant of propor-
tionality has been chosen to simplify the formulae ahead. Standard identities then imply

that the volume forms and scalar curvatures are related by

                                                                                  k                           (3.40)

                 volg�K = P-1M VolgKe m-2 volgKe

                         -P 1M VolgKe            -2

                 Rg�K =                          R m-2     gKe

                  = P-1M Volg�K =                    P-1M VolgKe                              1+     k  .
                                                                                                  m-2

In particular, the higher-dimensional metric (3.21) can be written as

                    -1                 -2         k                                     -     (m-2)        e
                    PM                                                                         m+k-2       K
                 g =   Vol e g + e g , P                                                                      (3.41)
                                       gKe m-2 m+k-2 M

after taking into account the definitions (3.24) and (3.27) of the various constants. So
gP is a warped product of the Einstein metric gKe and the physical spacetime metric gM .
The warping factor is determined by the field . By assumption g�K is constant across the
fibres, so the tensors S� and Ng�P vanish in this region, just as F does. Therefore, after
fibre-integration, the full action (3.22) becomes simply

                      1                -   1  |  d   |2gM  -                         V ()     volgM           (3.42)
                    2 M RgM                2
                 M

                                              47
with a potential

                                                       k                  k                  (m-2)
V ()  =                                             e m+k-2       1-                         e m+k-2  .  (3.43)
                     (P-1M                       2                    m+k-2
                  M
                              VolgKe ) m-2

Using relation (3.38) between the constant  and the scalar curvature of gKe , in the physical
case m = 4 the expression for the potential can also be written as

                                 P RgKe                       k        2     2
                     V ()   =  2 2M VolgKe                        1 + - e k+2                .           (3.44)
                                                           e k+2       k

So the potential depends on the primordial Einstein metric in internal space only through
a multiplicative factor that coincides with the simple ratio of its scalar curvature and
Riemannian volume. A plot of V () for the illustrative values m = 4, k = 8 and  = 0
looks like this:

                               Figure 1: Potential V (). 4

    The pure Einstein product configuration of the metric gP corresponds to  = 0 and
defines a global maximum of the potential, which takes the value

                     V (0)  =                              (m - 2)                           .

                               (m  +  k             -  2)  M   (-P 1M                     2

                                                                       VolgKe ) m-2

In this region spacetime is de Sitter. For non-zero  the potential decreases. It is unboun-
ded from below for positive values of , as the internal space contracts, and it is bounded
by zero for negative , as the internal space expands from its primordial size VolgKe .

    An inspection of the full Kaluza-Klein Lagrangian (3.28), however, also makes it clear
that this simplified potential cannot be used when the tensor F is not negligible, or when
the scalar curvature of g�K departs too much from its initial value. The last condition
can take hold pretty quickly, one expects, if the primordial Einstein metric gKe also has

4All plots were generated with the free online version of Wolfram Alpha.

                                                           48
unstable TT-deformations, besides the -instability. Even though the TT-instabilities can
be milder than the rescaling instability, once the metric starts to unravel in that direction
the curvature Rg�K in Lagrangian (3.28) does change the effective potential felt by . All
in all, one should not expect the potential V () depicted in figure 1 to represent the true,
effective potential for large values of .

    In section 3.8 we will discuss a more complete potential V (, ) in the particular case
K = SU(3). This potential controls the early, joint dynamics of two unstable modes of
the bi-invariant metric on K: the scaling mode represented by  and a TT-deformation
represented by . It would be interesting to analyze in detail how the presence of the -
instability affects the early dynamics of . In section 3.9 we will argue that the rescaling
of the internal space induced by a changing  may not proceed indefinitely, across all
orders of magnitude. At some scale new physics may contribute to form a minimum of
the potential V (, ) and stabilize the rescaling deformation at a finite value  = 0.

A model with scalar inflation

The simplified action (3.42) that controls the early dynamics of the unstable mode  is
similar to the inflaton action that appears in single field models of cosmological inflation
[LL]. The general profile of the potential V () depicted in figure 1 belongs to the family
of hilltop potentials in small-field models. In these models inflation is generated by the
scalar field slowly rolling down from the local maximum of V [BoL, KLL]. The particular
potential (3.43)--a combination of two exponentials in --belongs to a subfamily of hilltop
models studied in [CFM].

    In the next few paragraphs we will verify that the simplified potential (3.43) does
indeed generate four-dimensional inflation, as the Einstein product metric starts to unravel
along the scaling deformation. In principle, the scalar field can roll down to both sides of
the maximum, leading to increasingly positive or negative values of . Inflation can occur
in both situations. However, we will also see that it never satisfies the slow-roll conditions
in this approximation. This happens because the hilltop of V () is not flat enough, so
the roll down of the scalar field from the global maximum will not be slow enough. When
the field rolls down to the  < 0 direction, the profile of the potential in figure 1 is
qualitatively similar to the potentials found in models of quintessential inflation.

Start by observing that the nth derivative of V with respect to  is

V (n)()                      k n                                   k  k      n-1  (m-2)

         =                      (P-1M                     2  e m+k-2  m+k-2       - e m+k-2 .

            (m  +  k  -  2)  M         VolgKe ) m-2

Using this expression one calculates that in the physical, m = 4 case, the slow-roll para-

                                       49
meters associated to the potential are

       1 V 2                2                1 - eb1             2

() :=  2 M V             =  2 M         1    +  2     -  eb1                            (3.45)
                                                k

       1 V                                      2                   (1 - eb1)2 - 8 eb1
() :=             - ()      =                                                           .
            M V                                    2      eb1    2         k (k + 2)
                               2 M      1    +     k  -

Here b1 = 2 /(k + 2), as in definition (3.27) with m = 4. Inflation should occur for values
of the field between  = 0 and () = 1. The last condition is satisfied for

                            k+2                    k                
                   := - 2               log               1�            .
                                             k+2                   2 M

Since  is positive by definition, the - solution is always well defined. The + solution

exists only when         < 1, and in this case + is positive.           However, the value of the
                    2 M

second slow-roll parameter at  = 0 is

                               (0)      =             -2      .

                                                1  +     2k
                                                         k+2

So it does not satisfy the slow-roll condition ||  1 unless the constant  is large. At the
same time, we do not want  to be large because, according to (3.19), that would create
many more unstable deformations of the primordial Einstein metric. Thus, the simplified
potential V () does not seem to be compatible with slow-roll inflation.

    At the end of last section we described the limitations of the approximation leading to
V (). Especially at later times, when the gauge field strength F may become non-zero,
or if the internal metric starts to unravel along TT-instabilities and the scalar curvature
of g�K departs from its initial value. The question is how these additional effects will
modify the description of the inflationary period derived from the simplified potential
V (). In principle it is possible that the dynamics of  coming from the full Kaluza-
Klein Lagrangian (3.28), if properly analyzed, could reveal a more realistic model of the
inflationary process. This would be a multiple-field, microscopic model of inflation, where
the scaling field  dominates the initial stages of the process but soon enough, for instance
after the start of internal symmetry breaking, other internal scalars (other coefficients of
the internal metric) and gauge fields need to be considered to extend the inflationary
period and, eventually, participate in the reheating period.

    A good starting point to investigate the corrections to V () induced by TT-instabilities
may be the example K = SU(3) described in section 3.8. There we write down the explicit
two-field action (3.79) and associated potential V (, ) that control the joint dynamics of
the unstable deformations  and . It would be interesting to understand the properties
of an inflationary period described by this two-field model. Even though this classical

                                             50
Kaluza-Klein picture still ignores fermions and all quantum effects. In section 3.9 we also
discuss the stabilization of the rescaling deformation at a finite value  = 0. That is
relevant to start thinking about the formation of present-time vacuum conditions.

    Important efforts to link the Kaluza-Klein picture to FRW cosmological models are
well-known in the literature. See [BL, ch. 6] for a review. These works generally adapt the
FRW model by assuming two time-dependent scale factors--one for the three-dimensional
space and one for the internal space--on an otherwise static space and internal geometry.
Then they study the equations of motion of the scale factors as derived from the Einstein-
Hilbert action or variations thereof. For example, the initial studies [CD, Fr] worked with
a flat internal space, and with Kasner-type solutions of the higher-dimensional Einstein
equations, to present models for the expansion of the three-dimensional space and simul-
taneous contraction of the internal space. In our language, these conditions lead to a trivial
potential (3.43) (since  = 0) and do not generate inflation. The article [SW] considers
non-standard curvature terms in the higher-dimensional action to obtain a sufficiently
long period of inflation. It works with general internal geometries and a non-minimal
gravity action with suitable parametres. These approaches differ from the one discussed
in section 3.8 because they assume a static internal metric during the entire inflationary
period, apart form the dynamical scaling factors (i.e. no room for TT-instabilities or
internal symmetry breaking).

3.7 Left-invariant metrics on SU(3)

In the following two sections we will take as internal space the simple, eight-dimensional
Lie group K = SU(3). We want to study the behaviour of the Einstein-Hilbert action
when the internal metric varies within a particular family of left-invariant metrics on K.
These metrics are deformations of the bi-invariant, Cartan-Killing metric on SU(3), which
is known to have an unstable TT-perturbation lying within that family.

    The discussion starts with a quick reminder of general properties of left-invariant
metrics on a simple Lie group. For more details see for instance [Mil, Bes, BD, Ba1].
After that we consider the family of deformed metrics on K and determine some of their
basic properties, such as volume, Ricci tensor, scalar curvature and Lie derivatives in
different directions. The behaviour of these metrics in a dynamical theory on M � K will
be addressed only in section 3.8, where we study how the unstable modes appear in the
higher-dimensional Einstein-Hilbert action.

                                                       51
Left-invariant metrics on a group

As a vector space, the Lie algebra of a group is the tangent space to the group at the
identity element. A vector v in the Lie algebra k = su(3) can be extended to a vector
field on the group K in two canonical ways: as a left-invariant vector field vL or as a
right-invariant field vR. The explicit flows of these vector fields can be used to show that
their Lie bracket is also invariant on K and satisfies

[uL, vL] = [u, v]kL  [uR, vR] = -[u, v]Rk                       [uL, vR] = 0 ,  (3.46)

where the bracket [ . , . ]k in the Lie algebra is just the commutator of matrices in the
case of matrix Lie groups. Just as with vectors, any tensor in the Lie algebra k can be
extended to a left or right-invariant tensor field on k. For example, an inner-product g
on k can be extended to a left-invariant metric on K by decreeing that the product of
left-invariant vector fields has the same value everywhere on K and coincides with g at the
identity element of the group. Thus g(uL, vL) = g(u, v). In the opposite direction, every
left-invariant metric on K is fully determined by its restriction to the Lie algebra. When
a left-invariant metric is applied to right-invariant vector fields, the result is a function
on K that is not constant in general, but still simple enough:

g(uL, vR) |h = g(u, Adh-1 v)       g(uR, vR) |h = g(Adh-1 u, Adh-1 v) (3.47)

for all elements h  K and all vectors u, v in the Lie algebra.

    The preceding observations imply that right-invariant fields are always Killing for
left-invariant metrics on K, since

    (LwRg)(uL, vL) = LwR g(uL, vL) - g([wR, uL], vL) - g(uL, [wR, vL]) = 0 . (3.48)
The same is not true for general left-invariant vector fields. The equality

(LwLg)(uL, vL) = LwL g(uL, vL) - g([wL, uL], vL) - g(uL, [wL, vL])              (3.49)
                    = - g([w, u], v) - g(u, [w, v])

entails that the Lie derivative LwLg may be a non-zero, left-invariant 2-tensor on K. In
the special case when g is an Ad-invariant inner-product on k, then g(uR, vR) is also a
constant function on K and the metric g is both left and right-invariant. In this case
left-invariant vector fields are Killing as well. These are the bi-invariant metrics on the
group. When the group is simple they coincide with minus the Killing form, up to a
constant factor.

    The isometry group of a left-invariant metric g on K is isomorphic to

                     Iso(g) = (K �H) / ( Z(K)  H ) ,                            (3.50)

                                   52
where H is the closed subgroup of K that preserves the metric under right-translations.
The subgroup H can be as large as K, for bi-invariant metrics, or as small as the trivial
group. The quotient appears because the central elements x  Z(K) satisfy xhx-1 = h
for all h  K, so when x  Z(K)  H the element (x, x-1) in K �H acts trivially on the
manifold K.

    Let H be a connected, compact subgroup of K. There is a one-to-one correspondence
between left-invariant metrics on K preserved by right H-translations and inner-products
on the Lie algebra k that are preserved by Adh for every h  H. This follows from (3.49).
On the other hand, an AdH-invariant inner-product on k determines a decompositon
k = h  h and the orthogonal subspace h is preserved by AdH. Since the inner-product
restricted to h is still AdH-invariant, of course, standard results say that it determines
a K-invariant metric on the quotient homogenous space K/H [KN, Prop. X.3.1]. So
studying left-invariant metrics on K is an algebraic problem closely related to studying
K-invariant metrics on K/H. Deformations of left-invariant metrics on K can change
their isometry group, so provide a sort of continuous, "upstairs" path between K-invariant
geometries in different homogeneous spaces.

    The Riemannian volume form volg of a left-invariant metric g is always a left-invariant
differential form on the group. In the case of connected, unimodular Lie groups it is also

a right-invariant form, even though the metric itself may not be right-invariant. In this

case we always have

                      (Lh) volg = (Rh) volg = volg ,             (3.51)

where Lh denotes the diffeomorphism of K determined by left-multiplication by the group
element h, and similarly for Rh. This bi-invariant volume form of g coincides, up to
normalization, with the Haar measure on K. The invariance of the volume form together
with (3.47) can be shown to imply that

                               g(uL, vR) volg = 0                (3.52)

                          hK

for all vectors u and v in k and for all left-invariant metrics g. In contrast, by definition
of left-invariant metric, the contraction g(uL, vL) is a constant function on K, so we have

                           g(uL, vL) volg = g(u, v) Vol(K, g) .  (3.53)

                      hK

The integral over K of the product g(uR, vR) is not immediate in general, but it does

follow from the second equality in (3.47) that it is Ad-invariant, and hence proportional
to the Cartan-Killing product on a simple algebra k:

    g(uR, vR) volg =      g(Adh-1 u, Adh-1 v) volg  Tr(adu adv) Vol(K, g) . (3.54)

hK                    hK

                          53
This happens because the second integral above is explicitly averaging the pull-back metric
Adh-1 g over K, and hence is invariant under a change of variable h  hh for any fixed
group element h  K.

    Finally, the Ricci curvature of a left-invariant metric is also a left-invariant tensor on
K. This implies that the scalar curvature is constant on the group. Its value can be
expressed in terms of a g-orthonormal basis {ea} of the Lie algebra k through the formula

                            1                   1
               Rg = -       4 g ([ea, eb], [ea, eb]) + 2 g([ ea, [ea, eb] ], eb) .  (3.55)

                       a,b

This expression is valid for unimodular Lie groups and is a special case of a well-known
formula for the scalar curvature of homogeneous spaces (e.g. see chapter 7 of [Bes]).

A particular family of left-invariant metrics on SU(3)

Think of su(3) as the space of traceless, anti-hermitian 3 � 3 matrices. It has a natural

inner-product

                       0(u, v)  :=  Tr(u v)  =     1                                (3.56)
                                                - B(u, v) ,

                                                   6

where B(u, v) denotes the Cartan-Killing form Tr(adu  adv). Any matrix in su(3) can be

uniquely written as

                            v = -2 vY        -(v)      ,                            (3.57)

                                         v vY I2 + vW

where vY is an imaginary number, vW is a traceless, anti-hermitian matrix in su(2) and
v is a vector in C2. This determines a vector space decomposition

                            su(3) = u(1)  su(2)  C2                                 (3.58)
                                 v = vY + vW + v .

When acting on vectors in these summands, the Lie bracket of su(3) satisfies the relations

                 [ u(1), u(2) ] = {0}              [ u(2), C2 ] = C2                (3.59)
               [ su(2), su(2) ] = su(2)             [ C2, C2 ] = u(2) ,

where of course u(2) = u(1)  su(2). Identifying vY , vW and v with their image matrices
in su(3), one can define an inner-product g^ on su(3) by

               g^(u, v) := 1 Tr(uY vY ) + 2 Tr(uW  vW ) + 3 Tr (u) v                (3.60)

for positive constants 1, 2 and 3. The inner-product g^ determines a naturally reductive
metric on SU(3), so essentially a Killing metric with independent rescaling factors in each

                                         54
component of the Lie algebra decomposition. It is clear that decomposition (3.58) is
orthogonal with respect to g^.

The rescaled inner-product g^ is no longer invariant under the adjoint action on su(3).

However, it is invariant under the restriction of this action to a subgroup of SU(3) iso-

morphic to U(2). This subgroup is the image of the homomorphism  : U(2)  SU(3)

defined by

                                (a) =        (det a)-1           .                           (3.61)

                                                          a

Then the restricted adjoint action on su(3) is given by

                                        - Tr(vY ) -[ (det a) a v ]  

               Ad(a)(v) =                                           ,                        (3.62)

                                        (det a) a v vY + Ada(vW )

for all matrices a  U(2) and vectors v  su(3). The product g^ is the most general
inner-product on su(3) invariant under such transformations.

    Using the standard correspondence between inner-products on the Lie algebra and left-
invariant metrics on the group, it it clear that the left-invariant metric on K determined
by g^ is not bi-invariant. It is invariant under the diffeomorphisms of K determined by
group multiplications on the left. But when it comes to multiplications on the right, it is
invariant only under the subgroup U(2) of SU(3), unless the constants j are all equal.
So the isometry group of that left-invariant metric is U(2) � SU(3) or a finite quotient
thereof. To be more precise, it follows from (3.50) that in the case K = SU(3) the isometry
group of the bi-invariant metric is (SU(3) � SU(3))/Z3, while the isometry group of the
left-invariant metric determined by g^ is

            Iso(g^) = ( SU(3) � U(2) )/ Z3 = ( SU(3) � SU(2) � U(1) )/ Z6 .

This coincides with the gauge group of fermionic representations in the Standard Model.

    Now let {ea}={u0, . . . , u3, w1, . . . , w4} be a g^-orthonormal basis of su(3). The vectors
are chosen so that {wj} spans the subspace C2 of su(3), the vectors {u1, u2, u3} span the
subspace su(2) and u0 is the vector

                                        1
                                u0  =    diag(-2i, i, i) ,                                   (3.63)
                                          6 1

spanning  the  subspace  u(1).  This  basis  is  related  to  a  0  -orthonormal  basis  of  su(3)  by

rescaling the individual vectors with factors of the form a. Using this relation it is

straightforward to show that the volume forms of g^ and 0 are related by

                                vol g^ = 1 23 34 vol0 .                                      (3.64)

                                                 55
Using the orthonormal basis in formula (3.55) for the scalar curvature, one calculates that

                              R g^ = 3  1  +  4   -  1 + 2      .                     (3.65)
                                        2     3        2 32

With some more work on the formulae of [Bes, ch. 7], in appendix A.3 we also calculate
that the Ricci tensor of g^ is related to the metric itself by

Ric g^  =  3 1   g^ |u(1)  +  1  +  2                    3  4   -  1  +   2  g^ |C2
           2 23               2     2 32   g^ |su(2) + 4    3         32

        =  3 21  0 |u(1)   +  1  +  22                   3   4 - 1 + 2       0 |C2 .  (3.66)
           2 23                     2 23   0 |su(2) + 4              3

It is clear that g^ is Einstein only when 1 = 2 = 3. Decomposition (3.58) is orthogonal
with respect both to g^ and to Ric g^.

    For a left-invariant metric g on K the Lie derivatives LvR g always vanish, as remarked
in (3.48). The derivatives LvL g can be non-zero. Using (3.49), the inner-product of these
Lie derivatives, as defined in (2.24), is calculated in appendix A.3 to be

           LuL g^, LvL g^     =3        1  +  1   +  1 + 2   -     4  g^(u, v)        (3.67)
                                        1     2         23         3

for vectors u and v in su(3). The double prime, recall, denotes the C2-component of the
vectors in decomposition (3.58) of su(3).

An unstable deformation of the bi-invariant metric

Consider the one-parameter family of left-invariant metrics on SU(3) obtained from the
general deformation (3.60) by choosing the constants a to be

           1(s) =  e2s              2(s) =  e-2s             3(s) =  es ,             (3.68)

where  is a positive constant and s a real variable. These metrics will be called g^s. At
s = 0 the metric is bi-invariant and from (3.64) we get that, for any value of s,

                              volg^s = volg^0 = 4 vol0 .                              (3.69)

So g^s is a deformation of the bi-invariant metric that preserves the volume form. Taking
the derivative of g^s with respect to s and calculating the divergence of the resulting
2-tensor with respect to g^s, one can also verify that

                                 divg^s    dg^s   = 0.
                                           ds

                                              56
So g^s is a TT-deformation of the bi-invariant metric. The scalar curvature of these metrics
can be obtained from (3.65). Denoting it simply by R(s) and taking derivatives with
respect to the parameter s, we have

             3  2 e2s - 1 + 8 e-s - e-4s  (3.70)
R(s) =
2

R(s) = 6 es - e-2s 2


R(s) = 6 es - e-2s es + 2 e-2s .


The first derivative R(s) is always positive except at s = 0, where it vanishes. So the
scalar curvature is a monotone function of s with a saddle point at the Einstein metric
g^0. At this point also R(0) vanishes, but the third derivative is positive. A plot of R(s)
looks like this

                                    Figure 2: Scalar curvature R(s).

    Whereas most TT-deformations of the bi-invariant metric on SU(3) will reduce its
scalar curvature, this particular deformation increases it for positive values of the para-
meter s. Since the opposite -RgK plays the role of a potential for TT-deformations, we see
that the bi-invariant metric is unstable and can unravel in this direction of perturbation.
This family of metrics on SU(3) was found by Jensen in [Jen].

    It is not clear to the author if there are other unstable TT-deformations of the bi-
invariant metric on SU(3), modulo equivalence by diffeomorphisms. The mathematical
literature does guarantee that the bi-invariant metric is linearly stable [Sch]. This implies
that TT-deformations always have non-positive second derivative R(0), so a deformation
can be unstable only at higher-order. In particular, any TT-instability will always be
milder than the rescaling instability of the product metric on M �K described previously.
Recent results also inform that the bi-invariant metric is isolated in the moduli space of
Einstein metrics on SU(3) [BHMW].

                                                       57
3.8 Unstable modes and internal symmetry breaking when K =
       SU(3)

In this section we study the behaviour of the Einstein-Hilbert action when the internal
metric varies within the family of left-invariant metrics on SU(3) defined previously, in
(3.60) and (3.68). These metrics are unstable deformations of the bi-invariant metric.

    We start by deriving the simplest action that controls the dynamics of the deformation
fields  and . This is done in (3.79). Then we calculate the classical mass of the natural
gauge bosons as the bi-invariant metric on K unravels along that unstable perturbation.
We find that the bosons' mass changes according to formula (3.84). In the next section,
using results of the QFT literature, we will argue that this can affect the vacuum energy
density of the theory, and hence create an effective potential that could stabilize the
unravelling components of the internal metric.

Internal symmetry breaking

In this section we want to study the dynamics of a two-parameter, unstable deformation
of the Einstein product metric gPe = gMe + gKe on M4 � K, where gKe is a bi-invariant metric
on the internal space SU(3). Besides the rescaling field  studied in section 3.6, we also
consider a TT-deformation of the internal metric parameterized by a field  on M4. Start
by writing the internal, bi-invariant Einstein metric as

                            gKe       =  15
                                         2  0

where 0 is the metric defined in (3.56) and the constant factor was chosen to satisfy

the curvature relation (3.38). Consider the spacetime-dependent, TT-deformation of the

Einstein metric

g^K ()           :=    15  e2 0 |u(1)  + e-2 0 |su(2) + e 0 |C2           .  (3.71)
                       2

From (3.69) it is clear that this deformation does not change the volume form on K,

                       volg^K() = volg^K(0) =  15 4                          (3.72)
                                               2  vol0 .

In parallel with definition (3.39) in the case of the deformation parameterized by the
single field , let us take the normalized internal metric of (3.21) to be

                       g�K := P-1M Volg^K() g^K () .                         (3.73)

As in (3.41), this leads to a submersive metric on M � K of the form

                 gP =  P-1M Volg^K()   e g -1 4     +  e-      g^K ()  .     (3.74)
                                                5M          5

                                       58
This is the higher-dimensional metric that we want to study. It is no longer a warped
product metric because g^K() depends on the spacetime coordinates through the field .
Our aim is to calculate how the general Lagrangian (3.28) looks like when restricted to
this family of higher-dimensional metrics.

    Start by observing that the internal volume form associated to g^K() and g�K does not
depend on the spacetime coordinates, due to (3.72). So the fibres' mean curvature vector
determined by the normalized metric g�P , defined in (3.23), will vanish. Since the gauge
fields are also taken to vanish, we have

                             Ng�P = 0 = F .

The kinetic terms for the field  come from the traceless component S� of the fibres' second
fundamental form. To calculate it, observe that the Lie derivative of g^K() along a vector
field X on the base M4 is simply

LX g^K()      15        2 e2 0 |u(1) - 2 e-2 0 |su(2) + e 0 |C2      .  (3.75)
          = d(X)

              2

These Lie derivatives are symmetric 2-tensors on the internal space. Their inner-product
is defined by (2.24) and should be calculated with a g^K()-ortonormal basis {ea} of T K.
Using the explicit form of g^K() coming from (3.71) one can compute that

LX� g^K , LX g^K g^K =  a,b LX� gK (ea, eb) LX gK (ea, eb)

                = (�)() 4 dim u(1) + 4 dim su(2) + dim C2

                = 20 (�)() ,                                            (3.76)

as a function on the base M4. Since a constant rescaling of the internal metric does not
affect these inner-products, for the normalized metric g�K of (3.73) we also have

LX� g�K , LX g�K g�K = LX� g^K , LX g^K g^K = 20 (�)( ) .

It follows from (2.23) that, in the case of vanishing gauge fields, the norm of the fibres'
second fundamental form when calculated with the normalized metric g�P of (3.23) is just

             |Sg�P |2g�P = |S�g�P |g2�P = 5 gM� (�)( ) .                (3.77)

The scalar curvature of g^K() follows from (3.70) and (3.71):

                             2 e2 - 1 + 8 e- - e-4             .
             Rg^K() = 5

So for the normalized internal metric (3.73) we have

Rg�K ()   =     -P 1M Volg^K() -1  2 e2 - 1 + 8 e- - e-4          .
             5

                             59
The remaining constants that appear in the Lagrangian (3.28) are

                             = P-1M Volg�K =             -P 1M Volg^K() 5               (3.78)
                           a2 = a1 = -1/5 =              P-1M Volg^K() -1

                           b2 = 4 /5 = 4 b1 ,

where the relation between the volumes of g�K and g^K() can be obtained directly from
definition (3.73). Bringing together all these formulae, one can finally write down the
Lagrangian (3.28) restricted to higher-dimensional metrics gP of the form (3.74). After
integration over the fibre, the result is

                        1      RgM  -  1  |d|g2M  -  5   |d|2gM  -  V (, )  volgM ,     (3.79)
                      2 M              2             2
   M

where the potential is

                   1       2  a2 e4/5 - e Rg�K                                          (3.80)
V (, ) :=

                2 M

=  2M  P                       e4/5              1   2 e2 - 1 + 8 e- - e-4  e/5
       Volg^K ()                          1-

                                                10

=    P 5                       2    4               1    2 e2 - 1 + 8 e- - e-4 e/5      .
   M 2 Vol0                                  1-
                               15    e4/5            10

The last equality uses the volume identity (3.72). When  = 0 the expression of the

potential in the second line manifestly reduces to (3.43) in the case m = 4 and k = 8, as

it should. Omitting a constant factor, the partial derivatives of the potential are

V  - 1 e 2 e - 2 e-2 2                                                                  (3.81)
                           10

V      4  e4/5                            1  2 e2 - 1 + 8 e- - e-4 e/5               .
                                    1-
                        5                 8

So the only stationary point occurs at vanishing  and , which corresponds to the un-

scaled, bi-invariant metric on K. That is an unstable, saddle point of the potential. Since

the second derivative   2V     also vanishes at this point, while   2V  is negative, the unravel-
                        2                                           2

ling of the product Einstein metric on M � K should start by the rescaling perturbation

represented by , before the slower, TT-perturbation represented by  kicks in to break

the isometry group of the internal metric.

Mass of the natural gauge bosons

In the next few paragraphs we calculate the mass of the gauge bosons associated to the
invariant vector fields eaL and eaR on SU(3) when the vacuum metric is (, )-deformed, i.e.

                                                       60
when the higher-dimensional metric has the form (3.74). Since a right-invariant field eRa is
Killing for any left-invariant metric on K, the bosons associated to eaR are massless. The
squared-mass of the bosons associated to eaL is given by (3.84). These masses are derived
from the Lagrangian in the Einstein frame using the formulae of appendix A.2.

    To start the calculation observe that the vector fields eaL have vanishing divergence
with respect to any left-invariant metric, because the group SU(3) is unimodular and
(3.51) applies. So, according to formula (A.21), in the Einstein frame the squared-mass
of the gauge boson associated with the field eLa is given by

m2(eaL) = e     K Lea g�K , Lea g�K g�K volg�K  = e Lea g�K , Lea g�K g�K .  (3.82)
                   2 K g�K (ea, ea) volg�K                    2 g�K(ea, ea)

The last equality uses the left-invariance (and hence full constancy) of the integrand

functions over K. In the calculation of V (, ) we chose a normalized metric g�K related

to g^K() by the constant rescaling (3.73). Since the inner-product Lea g�K, Lea g�Kg�K is
invariant under such rescalings, we can write

          m2(eLa )  =         e        Lea g^K (), Lea g^K () g^K() .        (3.83)
                       P-1M Volg^K()          2 g^K()(ea, ea)

The rightmost fraction vanishes when ea is in the subspace u(2) of su(3), because eaL is
Killing in this case. When ea is in the subspace C2  su(3), the value of the rightmost
fraction can be calculated by applying (3.67) to the metric g^K() as defined in (3.71).
The result is

 Lea g^K (), Lea g^K () g^K() =  (e - e-2)2 + (1 - e-)2 .
          2 g^K()(ea, ea)             5

Combining this expression with the volume identity

                         Volg^K() =   15 4
                                      2  Vol0 ,

coming from (3.72), we finally obtain that the squared-mass of the gauge field Aa� associ-
ated to eLa is given by

m2(eLa )  =  3      2 5    e          (e - e-2)2 + (1 - e-)2                 (3.84)
             2
                    15 -P 1M Vol0

when ea is in the subspace C2 of su(3). There are four independent gauge fields in that
subspace, and this formula expresses their bosons' mass as a function of the internal
deformation fields, m2 = m2(, ). The bosons associated with the vector fields eLa in
the subspace u(2)  su(3) remain massless under the (, )-deformations of the internal
metric.

                                      61
3.9 Stabilizing the internal curvature

The potential V (, ) described in (3.80) decreases as  becomes non-zero and  takes
increasingly positive values. So one expects that the initial Einstein product metric on
M � K, if it ever represented the system over an ancient region of spacetime, will unravel
along the unstable deformations represented by those fields. This means that the internal
space would go through a global rescaling and, simultaneously, through a slower TT-
deformation that breaks the isometry group and increases the internal scalar curvature.
But will these deformations of the internal geometry increase indefinitely, across all orders
of magnitude of size and curvature, as suggested by the classical potential? Or at some
scale new physics will kick in, physics not contained in the classical Einstein-Hilbert
action, to stabilize the metric deformation?

    Generally speaking, one may expect that new physics will start to be relevant for
sufficiently small internal spaces or for large curvatures. One should not be able to confine
quantum particles in arbitrarily small internal directions, nor is GR tested for arbitrarily
large curvatures. The question would then be how to go beyond the Einstein-Hilbert
action and model mathematically such effects. One can always add to the action new ad
hoc terms that depend on the geometry of K and become relevant for big deformations.
For example, taking

                                         RgP - 2  - W (gP ) volgP

                                                      P

and choosing W =  Rg2K to be a quadratic function of the internal scalar curvature,
which is a well-defined function on P , one can check that for small, positive values of 
the effective potential has a local minimum and the rescaling is stabilized once K attains
a large curvature. More generally, it would be interesting to investigate the behaviour
of Rg2P -gravity or f (RgP )-gravity models in this Kaluza-Klein setting. In another line,
considering connections with torsion in the internal directions would also be interesting.
This is because the Ricci scalar of such a connection will be the traditional scalar curvature
plus a term involving the norm of the torsion. This additional term affects the effective
potential and may help to counterbalance the runaway scalar curvature under some of its
instabilities.

    For internal Einstein metrics with no TT-instabilities, where the rescaling represented
by  is the only instability, one can also follow the tradition of single-field models of
inflation and simply experiment with different ad hoc potentials W (), designed to prevent
an indefinite rescaling of K and, at the same time, complement the V () of (3.43) to
provide a good quantitative model for the initial stages of inflation.

    Yet another possibility would be to introduce an effective potential inspired by the

                                                       62
QFT vacuum energy density. Well-known QFT calculations suggest that the 4D vacuum
energy density depends on the masses of the quantum fields. The contribution of a gauge
field of mass m to the vacuum energy density is calculated in [Ma] (after [Ak]) to be

                     3 m4       log           m2  ,                                     (3.85)

                     642                      �2

where � is a new mass scale, not necessary close and presumably smaller than the Planck

mass. But in Kaluza-Klein models a gauge field's (classical) mass is given by formulae
such as (3.7) or (A.23), that depend on the vacuum internal metric gK0 . So we have
m2 = m2(gK0 ) and a deformation of the internal metric will affect the vacuum energy
density. This creates an effective potential 4vaDc(gK) that can be added to the 4D action.

    For example, when K is a compact, unimodular Lie group, with its invariant and
divergence-free vector fields {eaL} and {eRa }, one could consider a density 4vaDc(gK) propor-
tional to (3.85) with m2 given by the natural term

      P           (gKL )ab LeLa gK , LeLb gK  + (gKR )ab LeRa gK , LeRb gK     volgK .  (3.86)
2 M (VolgK )2
               K

Here (gKL )ab denotes the entries of the inverse matrix of gK(eaL, ebL), and similarly for (gKR )ab.
This term coincides with the sum of the squared-masses of the gauge bosons associated
to the invariant fields eaL and eaR, as given by the mass formula (A.23).

    In our specific example K = SU(3), the masses of these gauge bosons were previously
calculated for the (, )-deformed, higher-dimensional metric (3.74). The bosons associ-
ated to all the fields eRa and to the fields eLa in the subspace u(2)  su(3) remain massless
under (, )-deformations of the internal metric. The four bosons associated to the eaL in
the subspace C2 of su(3) gain a non-zero squared-mass given by (3.84). So the effective
potential would be something like

Veff (, )         =  V (, )  +   3            m4(, ) log  m2(, )            ,           (3.87)
                                642                           �2

where  is a dimensionless, positive constant and there are only four non-zero contributions
to the term m2(, ) of (3.86), each one given by (3.84). Now the question is whether
this effective potential has local minima where the deformation fields can settle, instead
of increasing indefinitely. In other words, can an increase of the vacuum energy density
compensate the falling potential V (, ) for large values of  and ? The power m4(, )
grows as e2 e4 for large positive values of , as is manifest from (3.84). The initial
potential V (, ), given by (3.80), decreases as -e e2 for large values of  and . So
the second term in Veff will dominate the initial potential for large, positive values of
both  and . This means that, in this regime, the unstable (, )-deformations of gK

                                63
could be stabilized by contributions coming from the vacuum energy density. A more
detailed calculation would be needed to analyze the case where  becomes negative when
unraveling from the initial value  = 0.

    We also note that, once the internal deformation is stabilized at a value (0, 0), the
dimensionally-reduced Lagrangian implied by (3.79) and (3.87) is

       1                         (3.88)
M 2 M RgM - Veff (0, 0) volgM .

So the value of the effective potential at its minimum, more precisely M Veff(0, 0), acts
as the de facto 4D cosmological constant. In particular, the unravelling of the primordial
Einstein metric along instabilities, by lowering the potential energy of the fields, does
indeed contribute to reduce the value of that constant. Having in mind the shape of the
rescaling potential of figure 1, it seems that an unraveling of the rescaling instability in the
 < 0 direction could more easily produce a positive, very small value of the cosmological
constant after the corrections contained in Veff are considered.

    The stabilization of the metric deformations at values (0, 0) would fix the present-
time, internal vacuum metric gK0 . This metric determines all the different gauge couplings
and gauge bosons' masses in the model, as described before. The masses of the Higgs
particles, in turn, will be determined by the second derivatives of the effective potential
Veff(gK) at its minimum gK0 , as in the usual Higgs mechanism.

    Finally, we stress that the arguments in this section merely pretend to suggest that
it may be possible to stabilize the deformations of the internal metric using physics not
contained in the Einstein-Hilbert action. For instance, using the QFT vacuum energy
density. These are not fully justified calculations. The usual notion of mass and form-
alism leading to the QFT formula (3.85), for example, are developed on a Minkowski
background, not on a general, or even de Sitter, four-dimensional background. It also
uses the boson's renormalized mass, not the classical bare mass. Even within our Kaluza-
Klein framework, in this section we have considered only the contribution of the most
basic gauge fields--those associated with the invariant vector fields eLa and eaR on K--to
the vacuum energy density, whereas in a general submersion presumably all massive gauge
and scalar fields could contribute. Also fermions should presumably contribute. Lastly,
we note that the stabilization of the TT-deformation field  would follow from both mass
formulae (3.7) or (A.21), while the stabilization of the rescaling field  in this simple
setting only follows in the case of the Einstein frame mass formula (A.21).

64
Electroweak symmetry breaking

In the last few sections we saw how the bi-invariant metric on SU(3) is naturally unstable.
In a dynamical Kaluza-Klein model, it should unravel along a TT-deformation that breaks
the isometry group down to (SU(3) � SU(2) � U(1))/Z6. Then we argued that it may be
possible to stabilize this deformation using an ad hoc potential, as is done in models of
cosmological inflation, or using results from quantum physics, such as the dependency
of the vacuum energy density on the bosons' mass and hence on the internal geometry.
Under the stabilized internal metric, the four gauge bosons associated with the broken
internal symmetries are massive.

    The unavoidable next question is, of course, how to go farther and account for the
electroweak symmetry breaking at a lighter mass scale. It is easy enough to find a second
TT-deformation of the internal metric, represented by a new scalar field ,

                                               g^K = g^K(, ) ,

that further breaks the isometry group down to SU(3) � U(1). An explicit example is
given in [Ba1], formula 5.6. More generally, see the parameterization of inequivalent left-
invariant metrics on SU(3) given in [Coq] for different isometry groups. But will any
such deformation increase the internal scalar curvature, and hence decrease the potential
V (, , ), to allow for a spontaneous metric unravelling in this direction? The answer to
this question should follow from a mechanical but long calculation, using formula (3.55)
for the scalar curvature on K. If the deformation  does decrease the potential, the next
question is how can the newly broken symmetries correspond to light bosons, with a mass
much smaller than the scale (3.37) of the gauge couplings? In other words, how can the
deformation field  be stabilized at a very small value 0, so that some Lie derivatives
LeaL g^K(0, 0) appearing in (A.23) will be non-zero but still have a norm many orders of
magnitude below the unity?

    The answer to this last question, if it exists within the Kaluza-Klein framework, should
probably rely again on physics beyond the classical Einstein-Hilbert action. The addition
of new terms to the action, on the way to an effective potential, entails the introduction
of new constants, such as the numbers  or � appearing in the vacuum energy density
in (3.87). These constants can a priori be very different from the Planck constant, since
they represent the scale of the new physics. They will appear in the extended equations
of motion and, in favourable conditions, can affect the classical field configurations that
minimize the effective potential. Thus, when we go beyond the Einstein-Hilbert action, the
classical vacuum metric gK0 can in principle have small "wrinkles" produced by components
in more than one length scale, so may be able to generate gauge bosons with very different
masses.

                                                       65
4 Comments on fermions

The purpose of this section is to briefly discuss some of the implications for fermions of the
Kaluza-Klein picture described previously in these notes. Having gauge fields associated
to non-isometric diffeomorphisms of the internal space creates both opportunities--such as
the possibility to generate mass for the gauge bosons within the Kaluza-Klein framework,
or the possibility to evade the Atiyah-Hirzebruch theorem--and additional theoretical
challenges--such as understanding how fermions should transform under diffeomorphisms
that do not preserve the metric. This challenge exists in any gravity theory, not just in
Kaluza-Klein.

    We start the section discussing possible new ways to circumvent the traditional no-
go arguments against chiral fermions in Kaluza-Klein. Then we spend most of the time
describing three possible geometric approaches to the transformation of fermionic fields
under non-isometric diffeomorphisms of the underlying space. Some of these approaches
already exist in the literature, in different forms, but do not seem to be too widely
explored. They imply thinking about the definition of spinor itself, and how to extend it
to objects that are not tied down to a fixed background metric.

4.1 No-go arguments against chiral fermions

In the standard Kaluza-Klein framework, as in [Wi2], fermions are represented by spinors
on M � K satisfying a Dirac-like, higher-dimensional equation of motion. The observed
fermions with their light masses (when compared to the Planck mass) are associated to
zero modes of the internal Dirac operator D/ K, or to zero modes of a deformation M/ K
of that operator generally called the internal mass operator. It is necessary to consider
deformations because the Schro�dinger-Lichnerowicz formula implies that D/ K does not
have zero modes on an internal space with positive scalar curvature, such as our K with
the metrics gKe or gK0 , but a deformation M/ K may well have them. If the mass operator on
K still anticommutes with the internal chirality operator, as D/ K does, then it must have
an equal number of zero modes with positive and negative internal chirality, i.e. it must
have a vanishing index. This follows from the fact that D/ K has vanishing index (because
it has no zero modes), together with the invariance of the index under continuous operator
deformations that preserve the anticommutation relation with the chirality operator. This
property of the mass operator does not contradict experiment, even assuming that the
internal chirality is correlated with spacetime chirality, because there is a equal number
of left-handed and right-handed fermions in the Standard Model.

    Let us denote by H the isometry group of the internal vacuum metric gK0 . The Dirac

                                                       66
operator commutes with isometries, and so should the mass operator if we assume it to
be natural. So there is a natural H-representation on the finite-dimensional space of zero
modes of M/ K. The (Kosmann) Lie derivative of a spinor along a Killing vector field
commutes with the chirality operator. So there are separate H-representations on the
spaces of positive and negative chirality zero modes of M/ K. In general these are reducible
representations. Now fix an irreducible H-representation . The number of independent,
positive chirality zero modes of M/ K that transform according to  minus the number
negative chirality zero modes that transform according to the same  is called the -index
of the operator M/ K. A result of Atiyah and Hirzebruch says that the -index of D/ K
vanishes when K is connected, even-dimensional and the group H is compact connected
[AH]. By invariance of the -index under deformations of the operator that preserve its
H-invariance, also the -index of M/ K should vanish under the same conditions. As Witten
famously pointed out in [Wi2], this means that one cannot obtain realistic Kaluza-Klein
models based on a connected, even-dimensional K and an isometry group H = GSM
acting on the zero modes of M/ K with spacetime chirality correlated to internal chirality.
In such a model the right-handed fermions would transform exactly as the left-handed
fermions do under the Standard Model group GSM, and this goes against the observed,
chiral nature of fermions.

    This argument raises a significant difficulty in the traditional Kaluza-Klein framework.
As discussed in the Introduction, to address that difficulty in these notes we suggest that
the Standard Model group GSM should not be identified with the exact isometry group H
of gK0 , but should instead be identified with the larger group G mentioned in the beginning
of the section. This seems quite natural because, in the Kaluza-Klein framework, the
mass of a gauge boson is proportional to the Lie derivative of gK0 along associated internal
symmetry. So only the massless bosons should be associated with exact isometries of
the vacuum metric. Associating the weak force to nearly-Killing, but not exactly-Killing
vector fields on the internal space would have the following advantages:

   i) the weak bosons would gain a non-zero mass within the Kaluza-Klein framework;

   ii) the internal symmetries associated to the weak force would not commute with D/ K
       or M/ K, so the weak field would be able to mix fermions with different masses, as
       happens in the Standard Model;

  iii) The restrictions dictated by the Atiyah-Hirzebruch theorem only apply to repres-
       entations of the isometry group of gK0 , so a priori the weak gauge fields would be
       able to couple differently to the positive and negative chirality zero modes of M/ K,
       potentially circumventing the no-go arguments of [Wi2].

                                                       67
Besides the transversal argument based on the Atiyah-Hirzebruch theorem, there are
other arguments in the literature that rule out the existence of chiral fermions in specific
dimensions, for example restricting realistic Kaluza-Klein theories to internal spaces of
dimension k = 4n+2. These arguments are based on a study of the spinor representations
in different dimensions and their interplay with the chirality operator and complex conjug-
ation [Wi1, Wet1, Wi2]. Once again, these arguments do not directly apply to weak gauge
fields associated with non-Killing vector fields on the internal space, essentially because
it is unclear how fermionic fields should transform under non-isometric diffeomorphisms
of internal space. The usual definitions of spin structure, spin bundle and spinor all start
with a manifold equipped with a fixed background metric. The spin groups themselves
are double covers of the special orthogonal groups in different dimensions and signatures.
When the background metric is allowed to change under full diffeomorphism symmetries,
as in genuine gravity or Kaluza-Klein theories, the transformation laws of spinors and
fermionic fields are not established as a settled matter.

    This brings us to the next part of these comments, which turns around the question of
how fermions should transform under non-isometric diffeomorphisms. We describe three
possible geometric approaches to address this question. Two of these approaches already
exist in the literature, in different forms, but do not seem to be too widely explored. It
would be interesting to further study them while having the Kaluza-Klein framework in
mind. The purpose would be to investigate if they can be useful to model any properties
of the interactions of the weak force with fermions.

    Before finishing this section, however, we should also point out that the classical
Kaluza-Klein literature contains several alternative proposals to circumvent the no-go
arguments that rule out the existence of chiral fermions. Those proposals include using
non-compact internal spaces [Wet2], adding gauge fields to the higher-dimensional theory
[CM, CS] or generalizing the assumptions of Riemannian geometry [Wei4], each having its
own advantages and drawbacks. More references can be found in the reviews [BL, CFD].

4.2 Spinors and GLk representations

One approach to discussing the transformation of fermions under general diffeomorphisms
is to work with GLk+ groups and representations, instead of working with the traditional
spin groups. The next few paragraphs give a quick outline of the geometrical setting,
although we do not study the GLk+-representations themselves. In the physics literature
this approach is generally considered in the case of four-dimensional spinors and Lorent-
zian geometry (e.g. [Ne, Mi, DP, NS]). Due to our Kaluza-Klein setting, here we will
mostly be thinking about the Riemannian geometry of spinors in the internal space.

                                                       68
    For k  3 the identity component of the general linear group, denoted by GL+k , has a
universal double cover that satisfies the commutative diagram

Spink(R)       GLk+(R)   (4.1)


SOk(R)         GLk+(R)

Here the vertical arrows are double covers and the horizontal arrows are inclusions of

groups. There is an infinite number of inequivalent representations of Spink(R) on finite-
dimensional vector spaces, the usual spinor representations. In contrast, it is well-known
that the enlarged group GL+k (R) has no faithful finite-dimensional representations [LM,
ch. II.5]. All its finite-dimensional representations factor through GLk+(R) and hence
are not fermionic in nature. There are, however, genuine GL+k (R)-representations on
infinite-dimensional vector spaces. Consider one such representation

 : GL+k (R) �  -  .

Restricting  to the maximal compact subgroup Spink(R) inside GLk+(R), the infinite-
dimensional space  decomposes as sum


=              m ,       (4.2)

          m=1

where each m is a finite-dimensional, irreducible representation space of Spink(R). The
spin action preserves the subspaces m but the GLk+-action will in general mix them,
and so will the action of any subgroup of GL+k not contained in the spin group. Exactly
which inequivalent spin representations appear in decomposition (4.2), as well as their
multiplicities, depends of course on the initial GLk+-representation . It is not clear to the
author which collections of irreducible spin representations {m : m  N} can be obtained
by restricting some infinite-dimensional GLk+-representation. For example, is there a 
such that all its components m are equivalent to the basic half-spin representations?

    The next step is to go from representations to spinors on manifolds, so one needs to
talk about spin structures. Let F +(K)  K denote the bundle of oriented frames in the
tangent bundle T K. A topological spin structure on K is a double cover  : F +(K) 
F +(K) equipped with a GL+k -action on the right that satisfies

(p � h) = (p) � (h)      (4.3)

for all spinorial frames p  F +(K) and all group elements h in GL+k (R) [BHM, ch. 2].
Here  is the double cover map of diagram (4.1). When the manifold K has a metric g

          69
there is a canonical relation between this notion of spin structure and the standard one.
With a metric one can pick the orthonormal frames of T K among all the oriented ones,
and so define the sub-bundle FSO(K, g) of orthonormal oriented frames inside F +(K).
Restricting the double cover  to the inverse image of FSO(K, g), we get a submanifold
FSpin(K, g)  F +(K) that is a double cover of FSO(K, g). Due to the commutation of (4.1),
it satisfies the equivariance property (4.3) for any h in Spink(R). In other words, for each
metric g on K the topological spin structure  restricts to a standard spin structure
FSpin(K, g) that fits in the commutative diagram of principal bundles over K:

               FSpin(K, g)                  F +(K)    (4.4)


               FSO(K, g)                    F +(K)

Here the vertical arrows are double covers and the horizontal arrows are inclusions. The
spinor bundle of S is defined as the associated vector bundle

               S := F +(K) �  - K .

Its fibres are isomorphic to the infinite-dimensional representation space . Each metric

g on K defines a different sub-bundle FSpin(K, g)  F +(K) and, from (4.2), a different

decomposition


               S =                          Sm (g) .  (4.5)

                                       m=1

The components Sm (g) are finite-dimensional vector bundles over K. For two different
metrics on K the respective decompositions are related by an automorphism of S, in

other words by a GLk+-gauge transformation, so there are isomorphisms Sm (g)  Sm (g)

between the component vector bundles.

    Now let  denote a left-action of a connected Lie group G on the manifold K. Using
the derivative maps,  has a lift to a G-action on the tangent bundle T K that is linear
on the fibres. Since a frame is just a collection of tangent vectors,  also has a lift to
a G-action on the frame bundle F +(K). This lifted left-action, denoted by  as well,
commutes with the standard right-action of GLk+(R) on F +(K).

    Since the topological spin structure F +(K)  F +(K) is a double cover and G is
connected, standard results guarantee that the action G � F +(K)  F +(K) lifts to a G-
action on F +(K) or, at worst, to an action of a double cover group G~ of G (e.g. [Bre, Th.

                                       70
I.9.1]). This lifted action, denoted by ~, fits into the commutative diagram of left-actions

                     G~ � F +(K)      ~  F +(K)

                     G � F +(K)  F +(K)          (4.6)

                     G�K                 K

Since the left-action  commutes with the right-action of GL+k (R) on F +(K), it follows
that the lift ~ commutes with the right GL+k (R)-action on F +(K). This implies that
~ induces a left-action on the total space of the associated bundle F +(K) � , which

of course is the spinor bundle S. This action is linear on the fibres and fits into the

commutative diagram

                     G~ � S           ~  S

                                                 (4.7)

                                              G�K  K

If the manifold K is equipped with a metric g and the group G acts through isometries,
then the lifted action ~ preserves the spinor sub-bundles Sm (g) in decomposition (4.5). In
this case the G-action does not mix spinors with values in different representation spaces
m, even though some of these spaces may just be copies of each other. In contrast, if G
does not act through isometries and only a subgroup G  G does, then G preserves the
representation spaces but another part of G can mix them.

    Coming back to our proposed Kaluza-Klein models, where a gauge group GSM acts on
the internal space K but only a subgroup G preserves the vacuum metric, that interplay
of the group representations with the different m is not too dissimilar from the way that
the distinct parts of GSM preserve or mix the different fermionic generations.

    In the eight-dimensional example K = SU(3), the smallest non-trivial representation
spaces of Spin8(R) are of course the eight-dimensional representation spaces v, + and
-, related to each other by the triality outer-automorphisms of Spin8(R). It would be
interesting to understand how different infinite-dimensional representations of GL+8 (R)
mix these three subspaces when restricted to compact subgroups not entirely contained
in Spin8(R). For instance when restricted to U(2)-subgroups with U (2)Spin8(R) = U (1).

    The existence of the lifted action ~ on the spinor bundle S, depicted in diagram (4.7),
also guarantees that there is a well-defined notion of Lie derivative LX of a GL+-spinor
along any vector field X on K. This derivative can be defined by a formula analogous to
(4.20). It satisfies the standard identity [LX, LY ] = L[X,Y ] for all fields X and Y . In

                                  71
contrast, the usual Kosmann-Lichnerowicz derivative of traditional spinors on S(g, K)
satisfies this identity only when X or Y are Killing fields on (K, g) [Kos].

4.3 Extended spinors

A second approach to modeling the transformation of fermions under non-isometric dif-
feomorphisms would be to work with what we call extended spinors, a simpler version of
universal spinors. These fields have values on a spin representation space , for example
the usual, finite-dimensional, spin-1/2 representation spaces, but instead of being defined
on the manifold K, the fields are now defined on the total space of the inner-product
bundle P (K) over K. For our purposes, the main advantage of working with extended
spinors is that they have a natural transformation rule under non-isometric diffeomorph-
isms of K, unlike the traditional spinors. They exist whenever K has a spin structure and
restrict to the traditional spinors once a metric on K is chosen. We now describe their
construction, which we have not been able to find in the literature.

    The oriented frame bundle F +(K)  K has a right-action of GLk+(R) mixing the
vectors that compose the frame. It is a free and transitive action. Identifying frames
related by the subgroup of SOk(R)-transformations, we can consider the quotient space

P (K) := F +(K) / SOk(R) = F +(K) / Spink(R) .  (4.8)

Then P (K) is a bundle over K with fibres isomorphic to GLk+/SOk, so of real dimension
k(k+1)/2. We will call it the inner-product bundle of T K. Each point in P (K) over a base

point x  K represents a SOk-equivalence class of frames on the tangent space TxK, and
hence determines a unique inner-product on TxK. In other words, P (K) can be thought
of as the space of pairs (x, hx), where x is a point in K and hx is an inner-product on
TxK. The bundle P (K) is the open subset of the symmetric bundle Sym2(T K) defined
by picking only the positive-definite products on the fibres. A section of P (K)  K is just

a metric on the tangent bundle of K. The inner-product bundle fits in the commutative

diagram of bundles over K:

                            F +(K)      F +(K)

                                                (4.9)

                                        P (K)

Here the horizontal arrow is a double cover, the vertical arrow is a principal SOk(R)-
bundle and the diagonal arrow is a principal Spink(R)-bundle. We are of course assuming
the existence of a topological spin structure F +(K) on K, as described near (4.3). For a

given spin representation  : Spink(R) �   , which now can be finite-dimensional,

                                    72
the extended spinor bundle of S is defined as the associated vector bundle

                   S(K) := F +(K) �  - P (K) .                              (4.10)

So it is a bundle with fibre  over the larger base P (K). In particular, when  is the usual
spin-1/2 representation space, with its Clifford multiplication of spinors by SOk-vectors,
there will also be a canonical multiplication of extended spinors by vectors tangent to
K, as happens with the usual spinors. A section of S(K) is locally represented by a
-valued map (x, hx) on the total space of the inner-product bundle.

    The relation between the extended spinor bundle and the usual spinor bundles over
K can be described as follows. A metric g on K is the same thing as a section of the
inner-product bundle P (K)  K, so defines a map

                   g : K - P (K) .

The pullback by this map of the extended spinor bundle S(K)  P (K) is a vector
bundle over K with fibre . This pullback bundle is then isomorphic to the usual spinor
bundle S(K, g)  K determined by the representation , the metric g and the spin
structure on K obtained by restriction of the topological spin structure, as in (4.4). So
for every metric g on K we can write simply

                   g(S(K))  S(K, g) - K

as vector bundles over K. Thus, in a sense, the extended spinor bundle over P (K) contains
all the usual spinor bundles over K determined by the different metrics on that manifold.

    There is a second natural construction of the extended spinor bundle, which we now
describe. Take the principal SOk(R)-bundle F +(K)  P (K) depicted in the commutative
diagram (4.9). Using the fundamental representation of this group, we can consider the

associated bundle

                   E(K) := F +(K) �SOk Rk - P (K) .                         (4.11)

It is a bundle with typical fibre Rk over the base P (K). It is isomorphic to the pullback
bundle

                                            E(K)  (T K) ,

where  : P (K)  K denotes the natural projection. Since a point q in P (K) represents
an inner-product on the tangent space T(q)K, it follows that the vector bundle E(K) 
P (K) has a canonical inner-product on its fibres, defined simply by

                   u, vq := q(u, v) ,

                   73
where u and v are vectors in the fibre Eq  T(q)K. Moreover, since E(K) is a pullback of
the tangent bundle T K, the topological spin structure on K determines a topological spin
structure on the vector bundle of oriented frames of E(K), which can then be restricted to
the �, �-orthogonal frames. So for a given spin representation  we have another natural
spinor bundle over P (K), namely the spinor bundle S(E) associated to E, to �, � and
that spin structure [LM]. There is, however, an isomorphism of vector bundles

S(E)  S(K) - P (K) ,

so this is just a second description of the same extended spinor bundle (4.10).

    The main advantage of working with the extended spinor bundle over the restricted
spinor bundles is that it has a natural action of general diffeomorphisms of K, even when
they are not isometries. We will now describe how this comes about. Let  denote a
left-action of a connected Lie group G on the manifold K. This group can be as large
as the identity component of the diffeomorphism group of K, denoted by Diff0(K). As
noted in diagram (4.6),  can be lifted to left G-actions on the tangent bundle T K and
on the oriented frame bundle F +(K). The latter commutes with the right GLk-action
on that bundle, so it follows from definition (4.8) that it descends to a G-action on the
inner-product bundle P (K). As also noted near diagram (4.6), after passing to a double
cover G~ of G if necessary, standard results (e.g. [Bre, Th. I.9.1]) guarantee the action 
has another lift ~ to the double cover F +(K) that commutes with the right GLk+-action
on that cover. So there are induced actions on the associated bundles (4.11) and (4.10)
that fit in the commutative diagrams

G � E(K)  E(K)                                  G~ � S(K)  ~  S  (K )

G � P (K)  P (K)                                G � P (K)  P (K)                 (4.12)

G�K  K                                          G�K           K

Extended spinors are defined to be the sections of S(K). Therefore, as desired, there is

a natural Diff0(K)-action on extended spinors.

    Let us write down these actions in somewhat more detail. For any group element
f  G the transformation f is a diffeomorphism of K. It acts on points in K; through
the derivative map it acts on vectors tangent to K; and through pullback it acts on inner-
products on the tangent spaces to K. The inner-product bundle P (K) can be thought of
as the space of pairs (x, hx), where hx is an inner-product on the tangent space TxK. So
the induced left-action on P (K) can be written as

(x, hx) - f (x), (f-1)(hx) .

                  74
A point in the associated bundle E(K), as defined in (4.11), can be written as an equival-
ence class [x, hx, {ea}, v], where v is a vector in Rk, x is point in K, hx is an inner-product
on TxK and {ea} is an oriented, hx-orthonormal frame of TxK. Then the lifted G-action
on E(K) is determined by the transformation rule

                     x, hx, {ea}, v - f (x), (-f 1)(hx), {(f ) ea}, v ,

where (f ) ea denotes the pushforward of the vector ea in the frame. The action is well-
defined because (f ) commutes with the right SOk-action that mixes the vectors ea of
the hx-orthonormal frame. Note also that the base {(f ) ea} is still orthonormal with
respect to the pullback inner-product (-f 1)(hx) on the tangent space Tf (x)K.

    The lifted G~-action on the extended spinor bundle S(K) can be written down in
similar terms. A point in this bundle is an equivalence class [x, hx, {e~a}, s], where s is a
vector in  and {e~a} is a lift to F +(K) of an oriented, hx-orthonormal frame {ea} of TxK.
The action of f~  G~ on the total space of S(K) is then determined by the transformation
rule

                     [ x, hx, {e~a}, s ] - f (x), (f-1)(hx), {~f~ (e~a)}, s .
The spin frame {~f~ (e~a)} is a lift to F +(K) of the (f-1)(hx)-orthonormal frame {(f ) ea}
of the tangent space Tf (x)K.

    Extended spinors have an operation of Clifford multiplication and a natural inner-
product. They can also be differentiated using Lie derivatives and a compatible covariant
derivative. These derivations are described in section 4.5 for universal spinors but also
apply to the special case of extended spinors.

4.4 Universal spinors

A third approach to modeling the transformation of fermions under non-isometric diffeo-
morphisms of internal space is to work with universal spinors, a sort of spinors that are
defined for all metrics simultaneously. We now describe this approach. Universal spinors
have been considered before in the mathematical literature, although rarely, it seems,
and sometimes in slightly different guises (e.g. [Swi, Am]). The extended spinors of the
previous section can be regarded as a special, finite-dimensional case of universal spinors,
a relation that we also describe below.

    Let K be a connected manifold and let M be the space of Riemannian metrics on it.
Universal spinors are sections (g, x) of a universal spinor bundle S  M � K. This
vector bundle restricts to the usual S(g, K) over each slice {g} � K, has an operation of
Clifford multiplication, has a natural inner-product on the fibres, and also comes equipped

                                                       75
with a compatible connection. Unlike the restricted spinor bundles, the universal bundle
has an action of the double cover of the diffeomorphism group of K. This means that
universal spinors have a natural transformation rule under general diffeomorphisms of K.

    The construction of the universal spinor bundle is very similar to the construction of
the extended spinor bundle described in the last section. The reader may want to skip the
details. We start be considering a sort of universal tangent bundle, i.e. a vector bundle
E  M � K whose fibres are isomorphic to the tangent spaces to K. More precisely,
take the projection 2 : M � K  K and use the pullback of bundles to define

                   E := 2(T K) - M � K .                             (4.13)

So E is a vector bundle over M � K with fibres E(g,x)  TxK. This vector bundle has a
natural inner-product �, � on the fibres. Given two vectors u and v in a fibre E(g,x), it is

defined simply by

                   u, v(g,x) := gx(u, v) .                           (4.14)

The diffeomorphism group of K acts both on K and, by pullback, on the metrics in M.
So there is a natural left-action

            : Diff(K) � M � K - M � K  f (g, x) := (f -1)g, f (x) .

This action lifts to the total space of the vector bundle E  M � K. Given a diffeo-

morphism f and a vector v in the fibre E(g,x)  TxK, the derivative map of f allows one
to define

                   f (v) := (df )x(v)  Tf(x)K  Ef (g,x) .            (4.15)

Using the definition of �, �, it is clear that the inner-product of any two sections of E

satisfies

                    f (u), f (v)   f = u, v                          (4.16)

as a function on M � K. So the lifted action preserves the natural inner-product on E.

    To talk about universal spinors we also need a spin structure on the vector bundle E.
So let us take the usual path and denote by FSO(E)  M � K the bundle of oriented
frames on E that are orthonormal with respect to �, �. It is a principal bundle with a
natural right-action of SOk(R). The restriction of FSO(E) to a slice {g} � K is isomorphic
to the bundle FSO(K, g) of orthonormal frames on (T K, g). A spin structure on E is a
double cover

                                         : FSpin(E) - FSO(E)

equipped with a Spink(R)-action on the right that satisfies

                   (p � h) = (p) � (h)                               (4.17)

                   76
for all p  FSpin(E) and all group elements h in Spink(R). Here  denotes the standard
double cover of groups Spink(R)  SOk(R). Since E is a pullback of the tangent bundle
T K, a topological spin structure on K, as defined in (4.3), determines a topological spin
structure on the bundle of oriented frames of E, which can then be restricted to the �, �-
orthogonal frames. So any topological spin structure on K determines a spin structure
on the bundle E  M � K, i.e. the cover FSpin(E) exists whenever K is spin.

    Given this fact, the universal spinor bundles are defined in the usual way. For a fixed
representation  : Spink(R) �   , the universal spinor bundle S(K) is just the
associated bundle

                              S(K) := FSpin(E) �  - M � K .

Since the restriction of the principal bundle FSpin(E) to a slice {g} � K is isomorphic to
the bundle FSpin(K, g) over K determined by the same topological spin structure on K,
it follows that the restriction of S(K) to {g} � K is isomorphic to the classical spinor
bundle S(K, g)  K determined by FSpin(K, g).

    We have already seen that the left-action  of Diff(K) on the product M � K lifts to
an action on E that is linear on the fibres and preserves the inner-product �, �. Since
a frame on E is just a collection of vectors,  also induces an action on FSO(E) of the
identity component Diff0(K) of the diffeomorphism group. The restriction to the identity
component guarantees the transformed frames, besides being orthonormal, are oriented
as well. This induced left-action, also denoted by , commutes with the right-action of
SOk(R) on FSO(E).

    Now let G denote the identity component Diff0(K) or a connected subgroup of it.
Since FSpin(E)  FSO(E) is a double cover and G is connected, standard results guarantee
that the action G � FSO(E)  FSO(E) lifts to an action of G on FSpin(E) or, at worst,
to an action of a double cover group G~  G (e.g. [Bre, Th. I.9.1]). This lifted action,
denoted by ~, therefore fits into the commutative diagram of left-actions

                                       G~ � FSpin(E) ~ FSpin(E)

                                       G � FSO(E)  FSO(E)

                                       G�M�K  M�K

Since the left-action  commutes with the right-action of SOk(R) on FSO(E), it follows
that the lift ~ commutes with the right Spink(R)-action on FSpin(E). This implies that
~ induces a left-action on the total space of associated bundles FSpin(E) � , which of

                                                       77
course are the spinor bundles S(K). This action is linear on the fibres and preserves the
inner-product on S(K). So we have another commutative diagram

                               G~ � S(K)      ~  S  (K )

                                                                              (4.18)

                               G�M�K  M�K

Universal spinors are defined to be the sections of the universal bundle S(K). Therefore,
as desired, there is a natural Diff0(K)-action on universal spinors, but not on the usual
restricted spinors, defined for a fixed background metric g on K.

When  is the fundamental spin representation, the lifts of  to the spinor bundle

S(K) and to the universal tangent bundle E defined in (4.13) are compatible with each
other under Clifford multiplication. This means that for every spin diffeomorphism f~ in
G~ we have

                               ~f~(v � ) = (f~)(v) � ~f~()                    (4.19)

as sections of S(K). Here  denotes the double cover map G~  G, v is any section of E

and  is any universal spinor.

Relation between universal and extended spinors

Universal spinors are -valued maps (g, x) defined on the product space M � K. Phys-
ically, it seems natural to introduce the following locality conditions on these fields:

L1) (g, x) = (g, x) whenever the metrics g and g coincide in a neighbourhood of the
      point x  K;

L2) (g, x) = (g, x) whenever the metrics g and g coincide at the point x  K.

Both conditions are diffeomorphism-invariant. If they are satisfied by a given universal
spinor , then they are satisfied by all the transformed spinors ~h(), where h  Diff0(K)
and ~ is the action defined in (4.18). A universal spinor  that satisfies L2 will automat-
ically satisfy L1, so the second condition is more restrictive. It is equivalent to saying that
 descends to a field on the inner-product bundle P (K), defined in the previous section.
In this sense, the extended spinors of the previous section can be regarded as the special
family of universal spinors satisfying L2. In contrast, condition L1 is equivalent to saying
that the universal spinor  descends to a field on the total space of germs of metrics over
K, denoted here by P(K). Now consider the natural projection maps

M � K -1 P(K) -2 P (K)                        (g, x) - ([gx], x) - (gx, x) .

                                          78
It is clear that the universal bundles E and S(K), as defined in this section, are iso-
morphic to the pullbacks by 2  1 of the analog bundles defined in the previous section
for extended spinors:

Euni(K)  (2  1) Eext(K)  Suni(K)  (2  1) Sext(K) .

It also clear that by considering the pullback bundles 2 Eext(K) and 2 Sext(K) over the
space of germs P(K), one can define a third notion of spinors, larger than the extended
spinors of the previous section and smaller than the universal spinors of this section.
Those spinors will be -valued maps defined on the total space of P(K). They will also
have an action of the spin diffeomorphism group Diff0(K).

Fermions and universal spinors

The relevant question for Kaluza-Klein is whether physical fermions in a gravity theory
can be modeled by any of these enlarged notions of spinor. In this case fermions would
not be represented by simple fields (x) on spacetime, but would also depend explicitly
on the background metric. They would be modeled by fields (g, x) on the product space
M � K, in the case of universal spinors, or by fields (x, hx) on the total space of the
inner-product bundle P (K), in the case of extended spinors.

    One can also conceive that physical fermions could be modeled by objects that depend
only on the spacetime coordinates and on the vacuum metric. In this case, denoting by
M0  M the subset of vacuum metrics on K, one would restrict the universal spinor
bundle to the domain M0 � K and consider sections of that bundle. So fermions would be
modeled by -valued maps (g, x) defined on M0 �K. These maps still have an action of
the group Diff0(K) provided that M0 is preserved by diffeomorphisms, which will be true
for any diffeomorphism-invariant action for the metric. Note that the space M0 may no
longer be contractible to a point, as happens for M in the case of Riemannian metrics, so
may be a space with non-trivial topology. In the limit, one can even try to model fermions
with universal spinors restricted to the product Og0 � K, where Og0  M0 denotes the
orbit of the chosen vacuum metric under the diffeomorphisms of K. These restricted
universal spinors would still transform naturally under non-isometric diffeomorphisms of
the vacuum and would still generalize the usual spinors, which are defined only over
{g0} � K for a fixed vacuum metric.

    A finite-dimensional version of this setting can be studied when K is a Lie group
and, instead of considering all metrics and all diffeomorphisms, one considers only left-
invariant metrics on K and the canonical diffeomorphisms determined by left and right-
multiplication on the group. In this case the space ML of left-invariant metrics is finite-

                                                       79
dimensional and the vacuum submanifold ML0 can be compact. If one restricts universal
spinors (g, x) to the domain ML0 � K, then a harmonic expansion of  can be obtained
from the tensor product of harmonic expansions in the K-component and in the M0L-
component. This would increase the multiplicity that each mode of the Dirac operator

on K appears in the overall harmonic expansion, in a phenomenon reminiscent of the

fermionic generations. Only the non-isometric diffeomorphisms of K coming from right-
multiplication act non-trivially on the component M0L, so only these diffeomorphisms
would be able to mix K-modes associated to different M0L-harmonics in the tensor product
expansion.

4.5 Lie and covariant derivatives of universal spinors

The next few paragraphs describe the existence of natural derivations of universal spinors.
Their main properties are stated below and will be justified in more detail elsewhere.
Although we work with the more general universal spinors, analog derivations with similar
properties also exist for the extended spinors of section 4.3.

    We have seen before that the universal spinor bundle S(K)  M � K has an action
~ of the double cover of the identity component of the diffeomorphism group of K. This
covers the natural Diff0(K)-action  on the product M � K, as in diagram (4.18). These
actions induce a natural Lie derivative LX of universal spinors through the definition

(LX)(g, x)  :=     d   ~X t                           -1    (g  ,  x)  |t=0 .  (4.20)
                -                                       tX

                   dt

Here X is any vector field on K and Xt denotes its flux, so an element of Diff0(K). This
definition of Lie derivative is quite general. It can be applied to sections of any vector
bundle with an action that is linear on the fibres. In particular one can use it to define
Lie derivatives of extended spinors or of the spinors of section 4.2.

Definition (4.20) implies the standard identities:

LX LY  - LY LX  = L[X,Y ]                                                      (4.21)
     LX (1 + f 2) = LX 1 + f LX 2 + df (XM�K ) 2

for all vector fields X and Y on K and for all scalar functions f on M � K. Here XM�K
denotes the vector field on M � K induced by X and the action , i.e.

                      d                                                        (4.22)
XM�K |(g,x) := dt tX (g, x) |t=0 = - LX g + X |x

as a tangent vector in T(g,x)(M � K), which is isomorphic to Sym2(T K)  TxK. In
contrast, note that the standard Kosmann-Lichnerowicz derivative of the usual spinors

                       80
on S(K, g)  K satisfies the first identity in (4.21) only when X or Y are Killing fields
on (K, g) [Kos].

    The action ~ preserves the natural inner-product on the fibres of S(K), which are
isomorphic to the spin representation space . This property implies that the induced
Lie derivative satisfies

LX 1, 2 + 1, LX 2 = [d1, 2] (XM�K) ,                             (4.23)

as functions on M � K, for all vector fields X on K.

    The vector bundle E  M � K, defined in (4.13), also has a left-action of the
identity component of the diffeomorphism group of K, as described in (4.15). So a formula
analogous to (4.20) can be used to define a natural Lie derivative LXv of the sections of
E. This guarantees that the derivative will have properties analogous to (4.21). Since
this Diff0(K)-action preserves the natural inner-product on E, as described in (4.16), the
corresponding Lie derivative will also satisfy a formula analogous to (4.23).

    Because E is just the pullback bundle 2(T K), a section v of E can also be viewed
as a vector field on the product manifold M � K. It is a vector field that projects to
zero under the pushforward map (1), where 1 : M � K  M denotes the natural
projection. Using the explicit form of the action on E, described in (4.15), one can then
derive the simple formula

                                           LX v = [XM�K, v] .

On the right-hand side we are taking the Lie bracket of vector fields on M � K. Note
that XM�K is a field on M � K projectable to M. In fact we have

(1)(XM�K ) |g = - LX g

by formula (4.22). Then standard identities of submersions [Bes, ch. 9.C] imply that

                      (1) ([XM�K, v]) = [(1) (XM�K) , (1) (v)] = 0 ,

because v projects to zero. So the bracket [XM�K, v] projects to zero under (1), and
hence is a well-defined section of E.

    When  is the fundamental spin representation, it follows from (4.19) and definition
(4.20) that the Lie derivatives LXv and LX are compatible with each other under Clifford
multiplication, in the sense that

                                 LX(v � ) = (LXv) �  + v � (LX)  (4.24)
for all vector fields X on K.

81
    The universal spinor bundle S(K)  M � K has a natural connection . This
connection restricts to the Levi-Civita connection for derivations along vector fields on
K. For derivations along vector fields on M, it restricts to the connection described by
Bourguignon and Gauduchon, defining the parallel transport of spinors under a change of
metric [BG]. The connection  is compatible with the natural inner-product of universal
spinors, in the sense that

W 1, 2 + 1, W 2 = [d1, 2] (W )                            (4.25)

for all vector fields W on M � K. It is also compatible with the Lie derivative of universal
spinors along vectors fields on K, in the sense that

LX (W ) = LXW  + W (LX )                                  (4.26)

for all vector fields X on K and all fields W on M � K. The connection  is not flat.
Its curvature has non-zero components when restricted to the K-factor in the product
M � K, also when restricted to the M-factor, and also for the mixed components with
one leg in each factor.

    The vector bundle E  M � K also has a connection  compatible with the natural
inner-product on its fibres, defined in (4.14). It satisfies identities analogous to (4.25)
and (4.26), but applied to vector sections v instead of spinor sections . When  is
the fundamental spin representation, the natural connections on E and on S(K) are
compatible with Clifford multiplication, in the sense that

W (v � ) = (W v) �  + v � (W )                            (4.27)

for all vector fields W on M � K.

    One can also write down a formula expressing the Lie derivative of universal spinors
in terms of the connection  on the vector bundles E and S(K). It is

1                      eaX, eb - ebX, ea (d)(ea � eb)  .  (4.28)
LX  = XM+X  - 8
                 a, b

Here {ea} denotes a local trivialization of E  M � K that is orthonormal with respect
to �, �; the linear map d : spink  End() is the derivative of the spin representation
; the vector field X on K can be viewed as a field on M � K or as a section of E that

does not depend on M; and finally XM denotes the vector field on M induced by X and
the action of Diff0(K) on M, as in (4.22), so that

                       XM |g = - LX g

                       82
as an element of TgM  Sym2(T K). This local expression for the Lie derivative of
universal spinors is very similar to the standard Kosmann-Lichnerowicz formula in the
case of regular spinors with fixed background metric [Kos]. The only difference is the
appearance of the field XM on M and the fact that  is a connection on the universal
bundle S(K)  M � K, not on the restricted spinor bundles S(K, g)  K. It follows
that the restriction of LX to a slice {g} � K inside M � K coincides with the Kosmann-
Lichnerowicz derivative only when XM |g = - LXg = 0, i.e. only when X is Killing for
the metric g.

    These canonical derivations can be used to construct natural operators on universal
spinors. For example, if {ea} denotes a local, �, �-orthonormal trivialization of the bundle
E  M � K, one can define

D/ K  :=     a ea � ea .                       (4.29)

Since the connection  on the universal bundle restricts to the Levi-Civita connection g

over each slice {g} � K inside M � K, the operator D/ K restricts to the standard Dirac
operator D/ gK over those slices, of course.

Operators on universal spinors on a Lie group

Let us now consider the case where the internal space K is a Lie group and restrict
universal spinors to the product ML � K, where ML denotes the finite-dimensional space
of left-invariant metrics on K. Then the tangent bundle T K and the universal bundles
E and S(K) are all trivial bundles. Let us pick a global, oriented, �, �-orthonormal
trivialization {ea} of the bundle E  M � K such that the restriction of ea to the slices
{g} � K are left-invariant vector fields on K. Any such two trivializations are related by
a transformation B : ML  SOk such that

ea |(g,x) =  b Bab(g) eb |(g,x) .              (4.30)

The components Bab(g) do not depend on the point x  K because both ea and ea are
left-invariant vector fields. Now denote by (ea)M the vector field on ML induced by the
section ea of E, i.e.

                                        (ea)M |g := - Lea(g,�)g ,

where ea(g, �) denotes the restriction of ea to the slice {g} � K. The right-hand side is
a left-invariant, symmetric 2-tensor on K, so an element of TgML. Since the right-hand
side is also C(ML)-linear on the ea entry and the transformation components Bab(g) do
not depend on x, it follows from (4.30) that also for the induced fields

(ea)M |g =   b Bab(g) (eb)M |g .               (4.31)

             83
This transformation rule makes it clear that one can define another operator on universal
spinors on a Lie group, besides (4.29), by

                           D/ M  :=        a ea � (ea)M  .          (4.32)

Using the Lie derivative of universal spinors, as written in formula (4.28), one can check

that also the operator

                                 L/  :=    a ea � Lea               (4.33)

is well-defined and independent of the choice of left-invariant trivialization {ea} of E.

Using the Kosmann-Lichnerowicz derivative

                        1        eaX, eb - ebX, ea (d)(ea � eb)  ,  (4.34)
LX  := X  - 8
                           a, b

which is similar to LX but does not satisfy the first identity in (4.21), one can also
consider the operator on universal spinors

                                 L/  :=    a ea � Lea  .            (4.35)

This operator does not involve any derivation along the M-component in the cartesian

product M � K. So it is also well-defined for traditional spinors on a Lie group equipped
with a fixed left-invariant metric. From formula (4.28) it is clear that L/ = L/ + D/ M.

All these operators are invariant under the Diff0(K)-action on the universal spinor

bundle. In fact, one can check that

[LX, D/ K] = [LX, D/ M] = [LX, L/ ] = [LX, L/] = 0

as operators on universal spinors for all vector fields X on K. These commutation relations
are not valid in general if the Kosmann-Lichnerowicz derivative LX is used instead of the
Lie derivative LX. For example, [LX, L/] vanishes only when X is Killing. If fermions in
Kaluza-Klein were to be modeled by universal (or extended) spinors on a Lie group, it
would be natural to look for combinations of these operators as models for the internal
mass operator.

Acknowledgements

It is a pleasure to thank Kirill Krasnov and Nick Manton for helpful comments on an
earlier version of these notes.

                                                       84
A Appendices

A.1 Weyl rescalings in Riemannian submersions

Let  : (P, gP )  (M, gM ) be a Riemannian submersion with fibre K. In this appendix
we consider Weyl rescalings of the higher-dimensional metric that act differently on its
horizontal and vertical parts, while preserving the submersive structure. As described
near (1.2), a submersive metric gP is equivalent to a triple (gM , A, gK) formed by a metric
on the base M , the gauge fields A and a family of metrics gK on K, one for each fibre.
Thus, given any pair of smooth functions f and  on the base M (which can also be
regarded as functions on P that are constant along the fibres), one can define a new
higher-dimensional metric g~P through the rescaled data

                          (g~M , A, g~K) := (e2 gM , A, e2f gK) .     (A.1)

Then the projection  : (P, g~P )  (M, g~M ) is still a Riemannian submersion. Denote by
m and k the real dimensions of the manifolds M and K. The volume forms transform
according to

    volg~P = em+kf volgP  volg~K = ekf volgK              volg~M = em volgM . (A.2)

Since the function f is constant along the fibres, the scalar curvature of the fibre metrics

rescales simply as

                          Rg~K = e-2f RgK .                           (A.3)

For the metric on the base, a well-known formula for the transformation of the scalar

curvature under rescalings says that [Wald]

    Rg~M = e-2 RgM - 2(m - 1) gM  - (m - 1)(m - 2) |d|2gM ,           (A.4)

where gM = gM� � denotes the negative Laplacian acting on functions on M . Since
the gauge fields (the one-form A on M with values on the vertical vector fields on P ) are

not rescaled in (A.1), the tensor F of (2.7) also remains unchanged. The squared-norm

|F|2, however, depends explicitly on the metrics, so it follows from (2.17) that it changes

as

                          | F |g2~P = e2(f-2) | F |g2P .              (A.5)

The transformation rule for the second fundamental form of the fibres can be deduced

from (2.21). Using the properties of the Lie derivative of a 2-tensor and the fact that f

is constant along the fibres, one first calculates that

    (Leag~P )(U, V ) = e2f (LeagP )(U, V )
    (LXg~P )(U, V ) = e2f [ (LXgP )(U, V ) + 2 df (X) gP (U, V ) ] .

                          85
Then from (2.21) one can derive that

                     S~U V = e2(f-) SU V - gP (U, V ) (gradgP f )                  (A.6)

for any vertical vector fields U and V on P . Taking the metric trace of this expression over

the vertical sub-bundle produces the transformation rule of the mean curvature vector of

the fibres:

                                N~ = e-2 N - k (gradgP f ) .                       (A.7)

This is an equality of horizontal vector fields on P . Combining the previous two expres-

sions, it is easy to check that the traceless component of the fibres' second fundamental

form, defined by

                                S�U V  := SU V         1                 ,
                                                   - k gP (U, V ) N

transforms under the rescalings as

                                       S�~U V = e2(f-) S�U V .                     (A.8)

The squared-norms of these tensors, as defined in (2.9), transform as

                     S�~ 2 = e-2 S� 2
                     g~P                  gP

                     |N~ |g2~P  =  e2 |N~ |2gP  =  e-2         N - k gradgP f  2.  (A.9)

                                                                               gP

To compute the transformation rule of divgP N , start by observing that it depends on the
metric both through N and through the divergence operator. For a fixed vector field Z
on P , it follows from the general relation LZvolg = (divg Z)volg and the rescaling rule for
volume forms that the divergence of Z transforms under Weyl rescalings as

                     divg~P Z = divgP Z + m d(Z) + k df (Z) .                      (A.10)

Combining (A.10) with expression (A.7) for N~ , a short calculation then shows that

divg~P (N~ ) = e-2 divgP (N ) + d kf + (m - 2) ( N - k gradgP f ) - k gP f (A.11)

as a real function on P . For reference, the transformation rules of the components of RgP
that appear in the action are written below after multiplication by the volume form:

Rg~K volg~P = em+(k-2)f RgK volgP

Rg~M volg~P = e(m-2)+kf RgM - 2(m - 1) gM  - (m - 1)(m - 2) |d|g2M                 volgP
                                                                                     (A.12)
|F |g2~P volg~P = e(m-4)+(k+2)f |F |g2P volgP

|S�~|2g~P volg~P = e(m-2)+kf |S�|2gP volgP

|N~ |g2~P volg~P  =  e(m-2)+kf     N   -  k     gradgP  f  2   volgP  .
                                                           gP

                                                   86
In the particular case where ef = e =: , the higher-dimensional metric as a whole

transforms as

                                          g~P = 2 gP .                               (A.13)

One can then check that the transformation rules listed above, when applied to the dif-
ferent components of decomposition (2.5) and (2.11), imply that the scalar curvature RgP
as a whole transforms as

Rg~P = -2 RgP - 2(n - 1) gP (log ) - (n - 1)(n - 2) |d log |2gP ,                    (A.14)

where n = m + k is the total dimension of P . This of course coincides with the usual
transformation of the scalar curvature under a simple Weyl rescaling [Wald]. When f =
 = log  the rules above also imply that

               |N~ |g2~P = -2 |N |g2P + k2 |d log |g2P - 2 k (d log )(N ) ,

and that

divg~P (N~ ) = -2   divgP (N )  -  k  gP (log ) +  (n - 2)(d log )(N )  +  k(2 - n)  d log   2
                                                                                             gP

as real functions on P . Taking these formulae for Rg~P , |N~ |g2~P and divg~P (N~ ), one can look
for constants 1 and 2 such that

Rg~P + 1 |N~ |2g~P + 2 divg~P (N~ ) = -2 RgP + 1 |N |g2P + 2 divgP (N )              (A.15)

for every rescaling function . This defines a system of linear equations for 1 and 2
that has a solution for

                   1 = -  (n - 1)(n - 2)                              n-1            (A.16)
                                                        2 = - 2 k .
                                      k2

Therefore the function on P

               WgP  :=  RgP     -  (n - 1)(n - 2)  N2        (n - 1)    divgP N      (A.17)
                                          k2       gP   -2
                                                        k

transforms simply as Wg~P = -2 WgP under the rescaling (A.13).

                                          87
A.2 Bosons' mass in the Einstein frame

The purpose of this short section is to register how the gauge bosons' mass formula (3.7)

gets adjusted when we use the Einstein frame Lagrangian (3.28) instead of the Jordan

frame Lagrangian in (3.2). Replicating the calculation of section 3.2, one works in the
approximation where the gauge fields Aa� are small, close to their vanishing "vacuum"
value, and where the internal metric is constant and equal to gK0 as one moves across the
fibres. After integrating over the fibre, the terms of Lagrangian (3.28) that depend on Aa�
are proportional to

1  gM�         gM  (FAa )�  (FAb )  Bab      +  gM� A�a Da  +  gM� A�a Ab Cab ,               (A.18)
4

but in the case of the Einstein frame the coefficients Bab, Cab and Da are now given by

Bab := e-0            g�K0 (ea, eb) volg�K0

                   K

            1      Lea g�K0 , LX g�P0  + 4 (1 - ) LX (divg�K0 ea)         volg�K0
Da := 2
               K

           1       Lea g�K0 , Leb g�K0  + 4 ( - 1) (divg�K0 ea) (divg�K0 eb)       volg�K0 ,  (A.19)
Cab := 4
               K

instead of (3.5). Following the argument described in section 3.2, choosing vector fields
ea on K that simultaneously diagonalize the quadratic forms Bab and Cab, the four-
dimensional equations of motion for the gauge fields are then

                            gM� (M  FAa)�       -  2  Caa  Aa  =  0.                          (A.20)
                                                      Baa

The coefficient 2 Caa/Baa will be called the squared-mass of the gauge field. It is now
given by

Mass A�a 2 = e0       K        Lea g�K0 , Lea g�K0 g�K0 + 4 ( - 1) (divg�K0 ea)2 volg�K0 ,    (A.21)
                                              2 K g�K0 (ea, ea) volg�K0

instead of (3.7). So the difference is the appearance of the factor e0 and the use of

the normalized version g�K0 of the internal vacuum metric instead of the simple vacuum
metric gK0 . The symbol � , �g�K0 on the right-hand side means that the internal product
of 2-tensors defined in (2.24) should be taken with respect to the metric g�K0 .

    We would prefer to write the mass formula in terms of the proper vacuum metric gK0 ,
instead of the normalized metric g�K0 and the vacuum value of the rescaling field . The
defining relation for  was, in (3.21) and (3.27),

                                                               (m-2)
                                                                m+k-2
                      gK    =  a1 e-b1 g�K      =   e g� . -2-
                                                       m+k-2
                                                                       K

                                                88
Taking the volume of the metrics on both sides of the equation and using (3.24) we get

                                                         2          -2  +  2                      -  (m-2)
                                                         k      m+k-2      k                          m+k-2

                                                gK
                            Vol =  e , -1
                            PM

and so

                              -       2(m+k-2)                                                 2                    2(m+k-2)
                                        k(m-2)                                                                        k(m-2)
e   =       2    Vol = -1                                   P-1M Volg�K k                            -P 1M VolgK    . -             (A.22)
                 PM
        k                 gK

On the other hand the inner-product Lea gK, Lea gKgK and the divergence (divgK ea) are
both invariant under constant rescalings of the internal metric gK, so take the same value
when calculated with respect to gK or to g�K. This implies that the quotient

                          K [ Lea gK , Lea gK  + 4 ( - 1) (divgK ea)2 ] volgK
                                2 (P-1M VolgK )-2/k K gK (ea, ea) volgK

is also invariant under constant rescalings of gK. Combining this fact with (A.22) one
recognizes that the right-hand side of (A.21) can be written as

                     1                K  Lea gK0 , Lea gK0  + 4 ( - 1)(divgK0 ea)2                                       volgK0  .
                                           2 (-P 1M VolgK0 )-2/k K gK0 (ea, ea) volgK0
        (  Vol ) -1         2(m+k-2)
            PM
                     gK0 k(m-2)

Here the rightmost fraction is invariant under constant rescalings of gK0 . Simplifying the
denominators we finally get

        Mass Aa� 2 =      K  Lea gK0 , Lea gK0 gK0 + 4( - 1)(divgK0 ea)2 volgK0 .                                                   (A.23)
                              2 P-1M VolgK0 2/(m-2) K gK0 (ea, ea) volgK0

This formula describes how the classical mass of the gauge bosons depends on the vacuum

geometry of the internal space, determined by the metric gK0 . In the physical case m = 4,

it  indicates  that  all  squared-masses        should      scale  as   (VolgK0                      )-1-  2  when  the  internal   space
                                                                                                           k

changes in size. Importantly, when the calculation is performed in the Einstein frame,

the scale of the bosons' masses also depends on the free parameter P appearing in the
higher-dimensional action (3.2). So that scale can be very different from -M1. In other
words, the Kaluza-Klein framework does not force masses to be in the Planck scale.

    As a word of caution, however, note that the notion of mass of a Klein-Gordon field
is not particularly clear outside of the flat Minkowski case. The physical interpretation
of the coefficient 2 Caa/Baa that appears in the equation of motion (A.20), written in the
vacuum approximation, should require additional care on curved backgrounds.

                                                            89
A.3 Quadratic forms on su(3)

Let g be a left-invariant metric on K = SU(3) and let u and v be vectors in the Lie
algebra su(3). Identifying these vectors with left-invariant vector fields uL and vL on the
group manifold, the product g(uL, vL) is a constant function on K. So the Lie derivative
of the metric becomes

                           (LwLg)(uL, vL) = - g([w, u], v) - g(u, [w, v])

for any vector w in su(3), as in (3.49). Choosing a g-orthonormal basis {ea} of the Lie
algebra, the inner-product of Lie derivatives can be expressed as

LuL g , LuL g  =        (LuLg)(ea, eb) (LuLg)(ea, eb)

                  a, b

               = 2 g([u, ea], eb)2 + g([u, ea], eb) g([u, eb], ea)

                         a, b

               = 2 g([u, ea], [u, ea]) + g([u, [u, ea]], ea)

                           a

               = 2 Ag(u, u) + 2 B(u, u) .                                        (A.24)

In the last equality we have denoted by A the quadratic form on the Lie algebra

               Ag(u, v) :=    a  g([u, ea], [v, ea])                             (A.25)

and by B(u, v) the Killing form Tr(adu  adv).

    Now let g be the special metric g^ defined in (3.60). The commutation rules (3.59) and
the g^-orthogonality of decomposition (3.58) imply that

                  Ag^ u(2), C2 = {0} .

The AdU(2)-invariance of the metric g^ implies that Ag^ is also AdU(2)-invariant. Since any
element u  su(2) can be taken to its opposite by an AdU(2)-transformation and the
element u0  u(1) is invariant under the same transformation, we also have that

               Ag^(u0, u) = Ag^(u0, -u) = 0 .

Hence the decomposition su(3) = u(1)  su(2)  C2 is fully orthogonal with respect to
Ag^. Since the AdU(2)-transformations are transitive on the maximal spheres inside each
component of the decomposition, the AdU(2)-invariance of both Ag^ and g^ implies that
these quadratic forms are proportional to each other inside each component, i.e.

Ag^ = �1 g^ |u(1) + �2 g^ |su(2) + �3 g^ |C2
                        90
for positive constants �k. The value of these constants can be deduced from explicit
calculations using the g^-orthonormal basis {u0, . . . , u3, w1, . . . , w4} of su(3). For example,
one calculates that

   4                          = 6 (1 + 2) -3 2                        3                        =0
                              = 6 -1 1                                                         = 12 2-1
      g^ [wj, wk], [wj, wk]                                             g^ [u0, uj], [u0, uj]
                                                                                                   (A.26)
j,k=1                                                               j=1

     4                                                               3

       g^ [u0, wj], [u0, wj]                                            g^ [uj, uk], [uj, uk]

   j=1                                                            j,k=1

     4                        = 2 2-1 for k = 1, 2, 3.

       g^ [uk, wj], [uk, wj]

   j=1

Taking these results and their sums, one can extract the values of the �k to conclude that

           6                     6                     3   1 + 2          1  +  1
Ag^ = 1 g^ |u(1) + 2 g^ |su(2) + 2                            23       +  1     2  g^ |C2 .            (A.27)

Substituting this result for Ag^ into expression (A.24) and using the relation between the
Killing form and the product g^, as in (3.56) and (3.60), we obtain

           Lu g^, Lu g^          =3          1  +      1  +  1 + 2     -  4     g^(u, u) ,             (A.28)
                                             1         2        23        3

where u denotes the component of u in the subspace C2 of su(3). Now consider the
second quadratic form on the Lie algebra

                 Cg^(u, v) := a,b g^([ea, eb], u) g^([ea, eb], v) .                                    (A.29)

A similar reasoning, using the AdU(2)-invariance of this form and the explicit results
(A.26), allows one to calculate that

Cg^     =  6 1  g^ |u(1)      +     2     2        22     g^ |su(2) +     33                           (A.30)
           32                       2        +     32                         +    g^ |C2 .
                                                                          1 2

A well-known formula for the Ricci tensor of left-invariant metrics on unimodular Lie

groups [Bes, ch. 7] then says that

                                                1         -  1         1
                              Ricg     =     - 2 Ag            B  +    4 Cg ,
                                                             2

where B stands for the Killing form on the Lie algebra. Substituting the results for Ag^ and
Cg^ into this expression and using the relation between the Killing form and the products
0 and g^, as in (3.56) and (3.60), one can write

Ric g^  =  3 1   g^ |u(1)     +        1     +  2                      3     4  -  1 + 2     g^ |C2 .
           2 23                        2        2 32      g^ |su(2) + 4      3        23

                                                       91
References

[Ak] E. Akhmedov: Vacuum energy and relativistic invariance, arXiv:hep-th/0204048.

[Am] B. Ammann, H. Weiss and F. Witt: A spinorial energy functional: critical points
          and gradient flow, Math. Annalen 365 (2016), 1559�1602.

[AH] M. Atiyah and F. Hirzebruch: Spin-manifolds and group actions, in Essays on
          Topology and Related Subjects, Springer-Verlag, 1970, 18�28.

[BL] D. Bailin and A. Love: Kaluza-Klein theories, Rep. Prog. Phys. 50 (1987), 1087�
          1170.

[Ba1] J. Baptista: Higher-dimensional routes to the Standard Model bosons,
          arXiv:2105.02899 [hep-th].

[Ba2] J. Baptista: Higher-dimensional routes to the Standard Model fermions,
          arXiv:2105.02901 [hep-th].

[BHMW] W. Batat, S. Hall, T. Murphy and J. Waldron: Rigidity of SUn-type symmetric
          spaces, arXiv:2102.07168v2 [math.DG].

[Bes] A. Besse: Einstein manifolds, Classics in Mathematics, Springer-Verlag, 1987.

[Be] G. Besson: A Kato type inequality for Riemannian submersions with totally
          geodesic fibers, Ann. Glob. Anal. Geom. 4 (1986), 273�289.

[Ble] D. Bleecker: Gauge theory and variational principles, Addison-Wesley, 1981.

[BoL] L. Boubekeur and D. Lyth: Hilltop inflation, JCAP 7 (2005), 010.

[Bou] J. Bourguignon: A mathematician's visit to Kaluza-Klein theory, Rend. Sem.
          Mat. Univ. Politec. Torino (1989), 143�163.

[BG] J. Bourguignon and P. Gauduchon: Spineurs, op�erateurs de dirac et variations de
          m�etriques, Comm. Math. Phys. 144 (1992), 581�599.

[BHM] J. Bourguignon, O. Hijazi, J. Milhorat, A. Moroianu and S. Moroianu: A spinorial
          approach to Riemannian and conformal geometry, European Mathematical Soci-
          ety, 2015.

[Bre] G. Brendon: Introduction to compact transformation groups, Academic Press,
          1972.

                                                       92
[BD] T. Brocker and T. Dieck: Representations of compact Lie groups, Graduate texts
          in Mathematics, Springer-Verlag, 1985.

[CFD] L. Castellani, P. Fr�e and R. D'Auria: Supergravity and superstrings: a geometric
          perspective, Vol. 2, Part five, World Scientific Publishing, 1991.

[CFM] M. Cadoni, E. Franzin and S. Mignemi: Inflation as de Sitter instability, Eur.
          Phys. Journal C 76 (2015), 1�11.

[CM] G. Chapline and N. Manton: The geometrical significance of certain Higgs poten-
          tials: an approach to grand unification, Nucl. Phys. B184 (1981), 391�405.

[CS] G. Chapline and R. Slansky: Dimensional reduction and flavor chirality, Nucl.
          Phys. B209 (1982), 461�483.

[CD] A. Chodos and S. Detweiler: Where has the fifth dimension gone?, Phys. Rev. D
          21 (1980), 2167.

[CJ] R. Coquereaux and A. Jadczyk: Riemannian geometry, fiber bundles, Kaluza-
          Klein theories and all that...., World Scientific Publishing, 1988.

[Coq]  R. Coquereaux: About left-invariant geometry and homogeneous pseudo-
       Riemannian Einstein structures on the Lie group SU(3), arXiv:2107.12285
       [math.DG].

[DP] L. Da�browski and R. Percacci: Spinors and diffeomorphisms, Comm. Math. Phys.
          106 (1986), 691�704.

[DNP] M. Duff, B. Nilsson and C. Pope: Kaluza-Klein supergravity, Phys. Reports 130
          (1986), 1�142.

[EBH] F. Englert and R. Brout: Phys. Rev. Lett. 13 (1964), 321.
          G. Guralnik, C. Hagen and T. Kibble: Phys. Rev. Lett. 13 (1964), 585.
          P. Higgs: Phys. Lett. 12 (1964), 132.

[FGN] V. Faraoni, E. Gunzig and P. Nardone: Conformal transformations in classical
          gravitational theories and in cosmology, Fund. Cosmic Phys. 20 (1999), 121�175.

[Fr] P. Freund: Kaluza-Klein cosmologies, Nucl. Phys. B209 (1982), 146�156.

[GW] G. Gibbons and D. Wiltshire: Black holes in Kaluza-Klein theory, Ann. Phys.
          167 (1986), 201�223.

       93
[Ham] M. Hamilton: Mathematical gauge theory: with applications to the Standard Model
          of particle physics, Universitext, Springer International Publishing, 2017.

[HE] S. Hawking and G. Ellis: The large scale structure of space-time, Cambridge Univ.
          Press, 1973.

[Her] R. Hermann: A sufficient condition that a mapping of Riemannian manifolds be
          a fibre bundle, Proc. Amer. Math. Soc. 11 (1960), 236�242.

[HW] G. Horowitz and T. Wiseman: General black holes in Kaluza�Klein theory, in
          Black Holes in Higher Dimensions, Cambridge Univ. Press, 2012, 69�98.

[Jen] G. Jensen: The scalar curvature of left invariant Riemannian metrics, Indiana
          Univ. Math. J. 20 (1971), 1125�1143.

[K] T. Kaluza: Sitzungsber. Preuss. Akad. Wiss. Berlin Math. Phys. K1 (1921), 966.
          O. Klein: Z. Phys. 37 (1926), 895.
          A. Einstein and P. Bergmann: Annals Math. 39 (1938), 683.
          P. Jordan: Naturwissenschaften 11 (1946), 250.
          Y. Thiry: Comptes Rendus Acad. Sci. Paris 226 (1948), 216.
          B. DeWitt: Lectures at 1963 Les Houches School, Gordon and Breach, 1964.
          R. Kerner: Ann. Inst. H. Poincar�e 9 (1968), 143.
          A. Trautman: Rep. Math. Phys. 1 (1970), 29.
          Y. Cho: J. Math. Phys. 16 (1975), 2029.
          Y. Cho and P. Freund: Phys. Rev. D12 (1975) 1711.
          J. Scherk and J. Schwarz: Phys. Lett. 57B (1975), 463.
          E. Cremmer and J. Scherk: Nucl. Phys. B108 (1976), 409.

[KN] S. Kobayashi and K. Nomizu: Foundations of differential geometry, vol. 2, Wiley,
          1969.

[KLL] K. Kohri, C. Lin and D. Lyth: More hilltop inflation models, JCAP 12 (2007),
          004.

[Kos] Y. Kosmann: D�eriv�ees de Lie des spineurs, Ann. di Matematica Pura ed Applicata
          91 (1971), 317�395.

[Kro] K. Kr�oncke: Stability of Einstein Manifolds, Doctoral thesis, Univ. of Potsdam,
          2013. https://publishup.uni-potsdam.de/frontdoor/index/index/docId/6723

[LM] H. Lawson and M. Michelsohn: Spin geometry, Princeton Univ. Press, 1989.

                                                       94
[LL] A. Liddle and D. Lyth: Cosmological inflation and large-scale structure, Cam-
          bridge Univ. Press, 2000.

[MS] N. Manton and P. Sutcliffe: Topological solitons, Cambridge Univ. Press, 2004.

[Ma] J. Martin: Everything you always wanted to know about the cosmological con-
          stant problem (but were afraid to ask), Comptes Rendus Phys. 13 (2012), 566�665.

[Mi] J. Mickelsson: On GL(4, R)-covariant extensions of the Dirac equation, Comm.
          Math. Phys. 88 (1983), 551�567.

[Mil] J. Milnor: Curvature of left invariant metrics on Lie groups, Adv. Math. 21 (1976),
          293�329.

[Ne] Y. Ne'eman: Gravitational interaction of hadrons: band-spinor representations
          of GL(n, R), Proc. Nat. Acad. Sci. USA 74 (1977), 4157�4159.

[NS] Y. Ne'eman and D. Sijacki: GL(4, R) group-topology, covariance and curved-space
          spinors, Int. J. Modern Phys. 2 (1987), 1665�1668.

[Ob] M. Obata: Certain conditions for a Riemannian manifold to be isometric with a
          sphere, J. Math. Soc. Japan 14 (1962), 333�340.

[O'Ne] B. O'Neill: The fundamental equations of a submersion, Michigan Math. J. 13
          (1966), 459�469.

[Sch] P. Schwahn: Stability of Einstein metrics on symmetric spaces of compact type,
          Ann. Global Analysis and Geometry 61 (2022), 333�357.

[SW] Q. Shafi and C. Wetterich: Cosmology from higher-dimensional gravity, Phys.
          Letters 129B (1983), 387�391.

[Swi] S. Swift: Natural bundles. II. Spin and the diffeomorphism group, J. Math. Phys.
          34 (1993), 3825�3840.

[Wald] R. Wald: General relativity, Chicago Univ. Press, 1984.

[OW] J. Overduin and P. Wesson: Kaluza-Klein gravity, Phys. Reports 283 (1997),
          303�380.

[Wei] S. Weinberg: A model of leptons, Phys. Rev. Letters 19 (1967), 1264�1266.

[Wei2] S. Weinberg: Charges from extra dimensions, Phys. Letters 125B (1983), 265�
          269.

                                                       95
[Wei4] S. Weinberg: Quasi-riemannian theories of gravitation in more than four dimen-
          sions, Phys. Letters 138B (1984), 47�51.

[Wei3] S. Weinberg: The quantum theory of fields, vol. 2, Cambridge Univ. Press, 1996.
[Wet1] C. Wetterich: Dimensional reduction of Weyl, Majorana and Majorana-Weyl

          spinors, Nucl. Phys. B222 (1983), 20�44.
[Wet2] C. Wetterich: Dimensional reduction of fermions in generalized gravity, Nucl.

          Phys. B242 (1983), 473�502.
[Wi1] E. Witten: Search for a realistic Kaluza-Klein theory, Nucl. Phys. B186 (1981),

          412�428.
[Wi2] E. Witten: Fermion quantum numbers in Kaluza-Klein theory, in Shelter Island

          II, Proceeding of the 1983 Shelter Island conference, MIT Press, 1985, 227�277.

                                                       96
