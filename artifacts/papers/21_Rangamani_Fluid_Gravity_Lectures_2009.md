# Rangamani Fluid Gravity Lectures 2009

**Source:** `21_Rangamani_Fluid_Gravity_Lectures_2009.pdf`

---

arXiv:0905.4352v3 [hep-th] 28 Oct 2009                                                                                             DCPT-09/33
                                                                                                                                   NSF-KITP-09-65

                                                    Gravity & Hydrodynamics:
                                        Lectures on the fluid-gravity correspondence

                                                                          Mukund Rangamani

                                                         Centre for Particle Theory & Department of Mathematical Sciences,
                                                       Science Laboratories, South Road, Durham DH1 3LE, United Kingdom

                                                                             Kavli Institute for Theoretical Physics,
                                                                 University of California, Santa Barbara, CA 93015, USA

                                                                           November 26, 2024

                                                                                                Abstract
                                                  We discuss recent developments in the hydrodynamic description of strongly cou-
                                              pled conformal field theories using the AdS/CFT correspondence. In particular, we
                                              review aspects of the fluid-gravity correspondence which provides a map between a
                                              class of inhomogeneous, dynamical, black hole solutions in asymptotically AdS space-
                                              times and arbitrary fluid flows in the strongly interacting boundary field theory. We
                                              explain how the geometric duals to the fluid dynamics are constructed in a boundary
                                              derivative expansion and use the construction to extract the hydrodynamic transport
                                              coefficients. In addition we also describe the recent developments extending the cor-
                                              respondence to incorporate matter fields and to non-relativistic systems. Based on
                                              lectures given at the CERN Winter School on Supergravity, Strings and Gauge Theo-
                                              ries, Geneva, Switzerland (February 2009).

                                          [email redacted]
Contents

1 Introduction                                         1

2 Elements of fluid dynamics                           7

2.1 Ideal fluids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

2.2 Dissipative fluids . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

2.3 Causality issues in relativistic viscous fluids . . . . . . . . . . . . . . . . . . 14

3 Conformal fluids                                     16

3.1 Weyl transformation of the stress tensor . . . . . . . . . . . . . . . . . . . . 16

3.2 Weyl covariant formulation of conformal fluid dynamics . . . . . . . . . . . . 19

3.3 Non-linear conformal fluids . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20

3.4 The non-linear conformal stress tensor . . . . . . . . . . . . . . . . . . . . . 21

4 Non-linear fluid dynamics from gravity               23

4.1 The universal sector: gravity in AdSd+1 . . . . . . . . . . . . . . . . . . . . . 24
4.2 Preliminaries: Schwarzschild black holes in AdSd+1 . . . . . . . . . . . . . . 26
4.3 Regularity and choice of coordinate chart . . . . . . . . . . . . . . . . . . . . 27

4.4 The perturbative expansion in gravity . . . . . . . . . . . . . . . . . . . . . . 30

4.5 Details of the long-wavelength perturbation expansion . . . . . . . . . . . . . 32

5 Gravitational analysis: Metrics dual to fluids       34

5.1 The gravitational dual to non-linear viscous fluid . . . . . . . . . . . . . . . 34

5.2 The boundary stress tensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

5.3 Event horizons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36

5.4 Boundary entropy current . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

6 Generalizations of the fluid-gravity correspondence  43

6.1 Fluid-gravity and the inclusion of matter . . . . . . . . . . . . . . . . . . . . 44

6.2 Non-relativistic fluids from gravity . . . . . . . . . . . . . . . . . . . . . . . 46

7 Discussion                                           50

A Weyl covariant curvature tensors                     52

1 Introduction

One of the important questions in modern theoretical physics involves understanding the
dynamics of strongly coupled quantum field theories. Not only is this of theoretical interest,
but there is a large class of real world physical systems where conventional perturbation
theory is a poor description of the actual physics. A case in point which is partly relevant

                                    1
to the current discussion is the fascinating state of matter discovered in heavy ion collisions,
the Quark Gluon Plasma (QGP), which is known to behave as a nearly ideal fluid.

    An important tool in the theoretician's toolkit to address strong coupling dynamics is
the AdS/CFT correspondence [1, 2, 3], which provides us with a holographic reformulation
of field theory dynamics in terms of classical gravitational dynamics (in a higher dimensional
spacetime). In general the AdS/CFT correspondence relates two seemingly disparate systems
� it provides a deep inter-connection between an interacting quantum field theory on the one
hand and string theory in a curved background on the other. The field theories of interest are
typically large N gauge theories (obeying large N factorization in the planar limit) and the
holographic dual is in terms of string theory in an asymptotically AdS background. While at
generic values in parameter space one is dealing with two intrinsically complicated theories,
at corners of parameter/coupling space one or the other description simplifies. Clearly, one
has a simple field theoretic description when the coupling parameter is taken to be small;
perturbation theory becomes reliable. In this regime the holographic dual description is
in terms of string propagating in a highly curved background. In the opposite limit when
we dial the field theory coupling to be strong, we simplify the string theory into classical
(super-)gravity.

    There is a way of thinking about the AdS/CFT correspondence that chimes well with
intuition for large N gauge theories which is worth bearing in mind. On general grounds one
expects that the large N limit of a quantum gauge theory behaves effectively classically i.e.,
quantum fluctuations are suppressed by 1/N. Said differently, the full quantum dynamics
in this planar limit should be encoded in terms of a classical gauge field configurations,
the "Master field" which controls the dynamics in this regime. While we have no concrete
candidate for this Master field in large N QCD, for a wide class of supersymmetric gauge
theories which arise as the world-volume theories on D-branes, the AdS/CFT correspondence
identifies a candidate Master field � this is just string theory (or classical gravity) in an
asymptotically AdS spacetime. In the strong coupling regime of the field theory the dynamics
of single trace operators is captured completely by classical Einstein gravity coupled to other
fields.

    In the course of these lectures we are going to be interested in a specific limit of the
correspondence � we wish in particular to simplify the dynamics of the field theory to that of
an effective classical fluid dynamics. As we shall see there is a precise sense in which this can
be done for any interacting quantum field theory, by focussing on near-equilibrium dynamics
and restricting attention to long wavelength physics. Under the holographic map we are
led to consider a particular class of gravitational solutions, which turn out to be dynamical
black hole spacetimes. This limit of the AdS/CFT correspondence which provides a concrete
relation between the physics of fluids and that of gravity is what we call the fluid-gravity
correspondence [4]. In the course of these lectures we will derive this correspondence and
see its utility in various contexts. Before delving into the detail however it is worthwhile to
pause and take stock of the reasons for why this is an interesting endeavour.

                                                          2
Fluid dynamics: As a classical dynamical system fluid dynamics provides interesting the-
oretical challenges. It is well known that for non-relativistic incompressible viscous fluids
described by the Navier-Stokes equations the issue of finding globally regular solutions re-
mains a open challenge, see for e.g., [5]. At the same time fluid dynamical evolution shows
very intriguing physics such as turbulence whose detailed understanding is still lacking. Fur-
thermore, the behaviour of energy cascade in turbulent flows and the corresponding inverse
cascade in lower dimensions are intriguing phenomena that beg for a better explanation.

    A holographic mapping of the fluid dynamical system into classical gravitational dynamics
could in principle help in unearthing some of these mysteries, at the very least by providing
a new perspective on the problem. To be sure, much of the physics of turbulence and global
regularity are of interest in the context of non-relativistic, incompressible Navier-Stokes
equations, while a natural realization of hydrodynamics in the fluid-gravity correspondence
leads to relativistic conformal fluids. This however is not a primary obstacle, for as we will
discuss towards the end, generalizations of the fluid-gravity correspondence to relax these
constraints already exist. An obvious fantasy would be to hope that one can formulate a
holographic dual of turbulence, but this is beyond the scope of these lectures.

Gravitational solutions: Over the past decade new remarkable stationary solutions to
higher dimensional gravity have been discovered and have served to highlight the limita-
tions of the folk-lore about gravitational dynamics built on our intuition for gravity in four
dimensions (for a review see [6]). An excellent illustration of this are the black hole unique-
ness theorems which fail to generalize straightforwardly to higher dimensions. The problem
of stability of the solutions in higher dimensions is also reveals some differences from the
lower dimensional analogs. One encounters for instance Gregory-Laflamme instabilities for
black strings and black branes [7] and closely related instabilities for spinning black holes
[8]. Understanding the stability domain of a given classical solution is important to get a
clear picture of the classical phase space of higher dimensional solutions.

    Fluid dynamics provides an interesting window to understand the physics of black holes.
The idea of applying hydrodynamic intuition to black holes dates back to the works on the
membrane paradigm [9, 10], wherein one modeled the black hole horizon by a membrane
equipped with fluid like properties. More recently, analog models for black hole stability
problem have been proposed whereby the Rayleigh-Plateau instabilities of liquid droplets
was associated with Gregory-Laflamme instabilities of black holes [11]. However, in these
applications the fluid dynamics is merely an analogy, a mnemonic to understand the qualita-
tive physical details in the complex gravitational setting by invoking a simpler fluid model.

    The fluid-gravity correspondence however provides a real duality between the hydrody-
namic description and the gravitational dynamics. This in particular implies that one can
draw a precise quantitative connection between the two and thus enables us to understand
aspects of the phase structure of black holes solutions and their stability in terms of the fluid
model. More pertinently for our current discussion this holographic duality also allows us to

                                                          3
systematically construct dynamical black hole solutions. As we will see in the course of the
lectures every fluid flow in the boundary field theory will map to a black hole spacetime in
the bulk geometric description with a regular event horizon. In fact, the fluid-gravity corre-
spondence will enable us to algorithmically construct black hole geometries given solutions
to the fluid equations of motion.1

Relevance to real world physics: Theoretical understanding of the state of matter
produced in heavy-ion collisions at RHIC (and perhaps soon at LHC), the QGP, requires
knowledge of dynamics in strongly coupled QCD. Current understanding is that subsequent
to the collision of the ions, the resulting constituents of the system rapidly thermalize and
comes into local thermal equilibrium and thenceforth evolve according to hydrodynamics
until the local temperature falls back below the deconfinement temperature and the QGP
hadronizes. The hydrodynamic regime is characterized by a set of transport coefficients;
in particular, since much of the flow in the QGP is the shear driven elliptic flow, it is the
shear viscosity of the plasma that is of most relevance. Ideally, one would like to be able
to start from the microscopic description in terms of QCD and be able to compute these
transport coefficients. However, with the QCD coupling constant remaining strong near the
deconfinement temperature one needs to find a way to go beyond perturbation theory. The
obvious choice, Lattice QCD is somewhat handicapped in this respect since it is ill-equipped
to deal with real time physics and Lorentzian correlation functions.2

    The AdS/CFT correspondence provides a theoretical framework to understand some of
the qualitative features of the hydrodynamics seen in QGP, by providing us with an efficient
way to access strongly coupled physics in a class of superconformal field theories. While
these field theories are qualitatively different from QCD in their vacuum, one might argue
that at finite temperature some of these differences are perhaps mitigated. An interesting
observation based on lattice simulations of QCD free energy, is that there appears to be
a range of temperatures say between 2 Tc and 5 Tc (recall that Tc  175 MeV for QCD)
where the energy density as a function of temperature shows Stefan-Boltzmann scaling with
a numerical pre-factor which is about 80% of the free field value. This could be taken as
prima-facie evidence for an effective description as a strongly coupled CFT for it is very
similar to the situation in N = 4 Super-Yang Mills (SYM) theory, whose strong coupling
free energy is exactly 3/4 the free field value [18]. However, other observables such as pressure
deviate from the value predicted by conformal invariance, thereby weakening the analogy. It
is therefore worth keeping in mind that the theories one is discussing are not quite QCD.

    That said it is rather remarkable that the only class of strong coupling field theories
for which we can compute hydrodynamic transport coefficients exhibit a remarkable quan-

    1In fact there are several results in the literature exploring the phase structure [12, 13, 14] and stability
[15, 16] of black holes using the dual fluid dynamics in the context of field theories compactified on spatial
circles with supersymmetry breaking boundary conditions. These boundary conditions break conformal
invariance and the field theories are confining in the infra-red.

    2For recent developments on lattice computations see [17] and references therein.

                                                          4
titative agreement with those arising from numerical fits to RHIC data. For instance the
universal behaviour of the shear viscosity in hydrodynamic description of field theories with
gravitational holographic duals [19] has already attracted attention and has impacted exper-
imental analysis of RHIC data, see for example [20, 21, 22, 23].3 In any event, independent
of applications to heavy-ion collisions one can view the superconformal field theories as toy
models; it is certainly quite remarkable that the holographic map allows us to explicitly
determine the transport properties of a strongly coupled non-abelian plasma.

Summary of the lectures: In these lectures we use the AdS/CFT correspondence to
study the effective description of strongly coupled conformal field theories at long wave-
lengths. On physical grounds it is reasonable that any interacting quantum field theory
equilibrates locally at high enough energy densities, and so admits an effective description
in terms of fluid dynamics. The variables of such a description are the local densities of
all conserved charges together with the local fluid velocities. The equations of fluid dynam-
ics are simply the equations of local conservation of the corresponding charge currents and
energy-momentum tensor, supplemented by constitutive relations that express these currents
as functions of fluid mechanical variables. As fluid dynamics is a long wavelength effective
theory, these constitutive relations are usually specified in a derivative expansion. At any
given order, thermodynamics plus symmetries determine the form of this expansion up to a
finite number of undetermined coefficients. These coefficients may then be obtained either
from measurements or from microscopic computations.

    The best understood examples of the AdS/CFT correspondence relate the strongly cou-
pled dynamics of certain (super-)conformal field theories to the dynamics of gravitational
systems in AdS spaces. In particular, we will demonstrate that Einstein's equations with a
negative cosmological constant, supplemented with appropriate regularity restrictions and
boundary conditions, reduce to the nonlinear equations of fluid dynamics in an appropriate
regime of parameters. We provide a systematic framework to construct this universal non-
linear fluid dynamics, order by order in a boundary derivative expansion i.e., as an effective
theory.

    There is a rather rich history of studying hydrodynamics of non-abelian plasmas using
holographic methods provided by the AdS/CFT correspondence. The early work of [25] was
the first to relate the process of thermalization in the field theory with the study of black hole
quasi-normal modes. Subsequently, the seminal work of Policastro, Son and Starinets [26]
began the investigation of linearized fluid dynamics from linearized gravity in asymptotically
AdS black hole backgrounds. The exploration of linearized hydrodynamics has been carried
out in various different contexts over the years in [19, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
37, 38, 39, 40, 41, 42, 43, 44, 45, 46] and we refer the reader to the excellent review [47] for
other references on the subject. The fluid-gravity correspondence [4] itself was motivated in

    3For a recent account of the nearly ideal fluids in encountered nature, such as the QCP and cold atoms
at unitarity, see [24].

                                                          5
part by these studies and the attempts to construct the holographic dual of the so called
Bjorken flow [48, 49]4 which is believed to be relevant to understanding the central region of
heavy-ion collisions hydrodynamically [64]. At the same time the investigations of the fluid
dynamical regime of stationary black holes in asymptotically AdS spacetimes [65] paved the
way for a clear understanding of the hydrodynamic regime in the gravitational context.

    The fluid-gravity correspondence was originally discussed in [4] in the context of gravita-
tional duals of four dimensional superconformal field theories whose holographic dual is given
by AdS5 �X5 where X5 a Sasaki-Einstein manifold which determines the CFT. A special
case is the N = 4 SYM where X5 = S5. In [66] the global aspects of the bulk geometry were
discussed and a geometric construction of the fluid entropy current was given. Subsequently,
this discussion was generalized to other dimensions in [67, 68, 69]. In addition [70] described
how to include external forcing in the hydrodynamic description by placing the fluid on a
curved manifold (and also explicitly included dilaton couplings). There is also a discussion
of charged fluid dynamics [71, 72, 73, 74], which in the context of N = 4 SYM corresponds
to looking at the grand-canonical ensemble with chemical potential for U(1)R charges, and
in addition inclusion of magnetic and dyonic charges in AdS4 [75, 76]. While all these dis-
cussions are for conformal fluids whose duals are asymptotically AdS spacetimes, one can
extend the discussion to non-conformal fluids living on Dp-brane world-volumes [77, 78] as
well as explorations involving higher derivative terms in the gravitational description [79].
Finally, the restriction of relativistic invariance can be relaxed to consider non-relativistic
conformal fluids [80] as well as duals to incompressible Navier-Stokes flow [81]. For a review
of some of the developments on the subject see also [82]. We will mainly review the basic
features of the correspondence in these lectures and will discuss some of the generalizations
towards the end in �6.

    The essential physical points arising from the fluid-gravity correspondence which we will
describe in detail below can be summarized as follows:

    � The gravitational derivation of the relativistic Navier-Stokes equations and its higher-
       order generalizations confirms the basic intuition that fluid dynamics is indeed the
       correct long-wavelength effective description of strongly coupled field theory dynamics.

    � The geometries dual to fluid dynamics turn out to be black hole spacetimes with
       regular event horizons [66]. This indicates that the hydrodynamic regime is special
       and in particular can be interpreted to indicate that the fluid dynamical stress tensors
       lead to regular gravity solutions respecting cosmic censorship.

    � The explicit construction of the fluid dynamical stress tensor leads to a precise deter-
       mination of higher order transport coefficients for the dual field theory. The results we

    4For further explorations of the spacetime geometry dual to Bjorken flow see [50, 51, 52, 53, 54, 55, 56,
57, 58, 59] and [60] for a review. More recently, these class of geometries have been understood within the
framework of the fluid-gravity correspondence in [61, 62, 63].

                                                          6
       present for the transport coefficients for four dimensional superconformal field theories
       with holographic duals were also derived in [83].

Outline of the lectures: We will begin with a review of relativistic fluid dynamics in �2
and then discuss various aspects of conformally invariant fluids in �3, reviewing in particular
the extremely useful Weyl covariant formalism developed in [84] in �3.2. In �4 we will review
the basic scheme to construct gravitational solutions dual to fluid dynamics following [4].
We then turn to a discussion of the physical properties of our solutions in �5. Finally in �6
we will discuss various generalizations of the fluid-gravity correspondence and conclude with
a discussion in �7.

2 Elements of fluid dynamics

Fluid dynamics is the low energy effective description of any interacting quantum field theory,
valid for fluctuations that are of sufficiently long wavelength. This description is intrinsi-
cally statistical in nature, for it is the collective physics of a large number of microscopic
constituents. Usually one thinks of the hydrodynamic description as the effective continuum
model valid on macroscopic scales. For an excellent introduction to the basic ideas in fluid
dynamics see [85] (see also [86] for relativistic fluids).

    To understand the statistical origins of the fluid dynamical description, consider a quan-
tum system in a grand canonical ensemble, where we prescribe the temperature and chemical
potentials for various conserved charges. In global thermal equilibrium we calculate observ-
ables by computing correlation functions in the grand canonical density matrix. One can also
perturb away from this global equilibrium scenario and allow the thermodynamic variables
to fluctuate. For fluctuations whose wavelengths are large compared to the scale set by the
local energy density or temperature, one describes the system in terms of fluid dynamics.

    One can pictorially think of the situation as follows; sufficiently long-wavelength fluctu-
ations variations are slow on the scale of the local energy density/temperature. Then about
any given point in the system we expect to encounter a domain where the local temperature
is roughly constant � in this domain we can use the grand canonical ensemble to extract
the physical characteristics of the field theory. Of course, different domains will described
by different values for the intrinsic thermodynamic variables. Fluid dynamics describes how
these different domains interact and exchange thermodynamic quantities.

    A more formal way to define the hydrodynamic regime is the following. In any interact-
ing system there is an intrinsic length scale, the mean free path length mfp, which is the
characteristic length scale of the interacting system. This is most familiar from the kinetic
theory picture of gases, but applies equally well to fluids. In the kinetic theory context the
mfp simply characterizes the length scale for the free motion of the constituents between
successive interactions. To achieve the hydrodynamic limit we are simply requiring that
we examine the system at length scales which are large compared to the mfp, so that the

                                                          7
microscopic inhomogeneities are sufficiently smeared out.

The dynamical content of the hydrodynamic equation is simply conservation of energy

and other conserved global charges. These can be succinctly summarized by giving the stress
tensor T �, which is a symmetric two tensor, and the charge currents JI�, where I = {1, 2, � � � }
indexes the set of conserved charges characterizing the system. The dynamical equations

then are given as

                   �T � = 0 ,     �JI� = 0 .                             (2.1)

To specify the system further we just need to find expressions for the stress tensor and

charge currents. Since the fluid dynamical description is only valid when the underlying

microscopic QFT achieves local thermal equilibrium, we should be able to use the basic

thermodynamic variables to characterize the system. Furthermore, we need to describe

how the different domains of local thermally equilibrated fluid interact with each other. To

understand how this can be achieved, let us focus on a fluid element which is characterized

by the local values of the thermodynamic variables. As the fluid element can exchange its

characteristics with neighbouring fluid elements, we should associate to this fluid element a

velocity field u�, which describes the flow of thermodynamic quantities. It turns out that

the thermodynamic variables together with the velocity field serve to characterize the fluid

completely.

    Consider a QFT living on a d-spacetime dimensional background Bd with (non-dynamical)
metric g�. The coordinates on Bd will be denoted henceforth as x�. We can summarize the

dynamical degrees of freedom characterizing the hydrodynamic description of this interacting

QFT as:

� Extrinsic quantities: Local energy density  and charge densities qI .

� Fluid velocity u� (normalized g� u� u = -1).

� Intrinsic quantities: Pressure P , temperature T , and chemical potentials �I determined
   by equation of state.

All that remains is to express the stress tensor and charge currents in terms of these variables.

2.1 Ideal fluids

Let us focus first on the description of an ideal fluid which has no dissipation. Then by
passing to a local rest frame, where we choose the velocity field to be aligned in the direction
of energy flow, we can identify the components of the stress tensor as the energy density
(temporal component longitudinal to the flow) and pressure (spatial components transverse
to the velocity field). Similarly, in this local rest frame the components of the charge current
are the charge density itself (along the velocity field). Putting this together, we learn that
for an ideal fluid

                   (T � )ideal =  u� u + P (g� + u� u) ,                 (2.2)
                    (JI�)ideal = qI u�.

                               8
Before proceeding to incorporate the physics of dissipation, let us pause to introduce

some notation that will be useful in what follows. Since the d-velocity u� is oriented along

the temporal direction, we can use it to decompose the spacetime into spatial slices with

induced metric

                              P � = g� + u� u.                                          (2.3)

We can view P � as a projector onto spatial directions; it is a symmetric positive definite
tensor which satisfies the following identities:

                P � u� = 0 ,  P � P  =  P  �  = P � g    ,   P�� = d - 1.               (2.4)


In terms of this projector we can express the ideal fluid stress tensor more simply as

                              (T � )ideal =  u� u + P P � .                             (2.5)

While the decomposition of T � into the temporal and spatial components is not very in-
teresting at the level of ideal fluids, it will play a more important role when we include the
effects of dissipation.

    In addition to the stress tensor and charge currents, there is another quantity which we
would like to keep track of, viz., the entropy current. Pictorially the entropy current keeps
track of how the local entropy density varies in the fluid. For an ideal fluid given the entropy
density s(x) the entropy current takes the simple form

                              (JS�)ideal = s u�.                                        (2.6)

Using the equations of motion (2.1) for an ideal fluid (2.2) and standard thermodynamic
relations, it is easy to show that the entropy current is conserved

                              � (JS�)ideal = 0.                                         (2.7)

i.e., the fluid flow involves no production of entropy.

2.2 Dissipative fluids

Ideal fluids with stress tensor given by (2.5) are an approximation; they don't include any
physics of dissipation. This is clearly seen by the conservation the entropy current. In general
we expect that the flow of the fluid results in the creation of entropy consistent with the sec-
ond law of thermodynamics. More pertinently, dissipation is necessary for a fluid dynamical
system to equilibrate when perturbed away from a given equilibrium configuration. Micro-
scopically one can understand the dissipative effects as arising from the interaction terms
in the underlying QFT. As a result the terms incorporating the effects of dissipation in the
stress tensor and charge currents will depend on the coupling constants of the underlying
QFT.

                                           9
    To model a hydrodynamical system incorporating the effects of dissipation we only need
to add extra pieces to the stress tensor and charge currents. Let us denote the dissipative
part of the stress tensor by � as the corresponding part of the charge currents by �:

(T � )dissipative =  u� u + P (g� + u� u ) + � ,  (2.8)
 (JI�)dissipative = qI u� + �.

To complete specification of the hydrodynamic system we should determine � and � in
terms of the dynamical variables the velocity field, u�, and the thermodynamic variables ,
P , qI, etc..

    The traditional way to determine the dependence of the dissipative components of the
stress tensor and charge currents is somewhat phenomenological. One employs the second
law of thermodynamics (positive divergence of the entropy current), cf., [85, 86], to determine
the set of allowed terms in the most general form of the constitutive equations. While this
makes some sense for incorporating the leading non-linearities in the fluid description, at
higher orders the procedure starts to be fraught with ambiguities as exemplified by the Israel-
Stewart formalism [87, 88]. We will take a different viewpoint on this and in fact outline a
procedure to unambiguously construct a non-linear stress tensor for hydrodynamics.

    The procedure we have in mind is inspired by the manner one constructs effective field
theories. When one writes down an effective field theory for a QFT, at any given order
one takes into account all possible terms that can appear in the effective lagrangian con-
sistent with the underlying symmetry. These irrelevant operators are suppressed by power
counting in momenta and appear with arbitrary coefficients in the effective lagrangian. We
have argued that hydrodynamics is best thought of as an effective classical description of
any interacting field theory valid when the system achieves local thermal equilibrium. Hence
following the logic of effective field theories we should allow in the hydrodynamic approxima-
tion all possible operators consistent with the symmetries. These irrelevant operators in the
present case are nothing but derivatives of the velocity field and thermodynamic variables.
Thus one can cleanly express the fluid dynamical stress tensor in a gradient expansion.5

    Before proceeding to enumerate the various operators that can contribute to the stress
tensor, let us constrain the dissipative components. First of all we have a choice of frame
which is related to how we choose the fluid velocity. Secondly when we enumerate gradient
terms at any given order we are free to use the lower order equations of motion to reduce
the set of gradient terms. Let us discuss these two issues in turn and see how they serve to
constrain the dissipative terms.

Defining the velocity field: Since we are discussing relativistic fluids, the fluid velocity
field needs to be defined with some care. The issue is simply that in relativistic dynamics one

    5The power counting scheme we have in mind for fluid dynamical operators is the following: each spacetime
derivative will count as dimension 1 for book keeping purposes. It is important to bear in mind that the
actual scaling dimension of the operator (as discussed in �3) which follows from the transformation of the
stress tensor under scale transformations is different.

                                                         10
cannot distinguish between mass and energy in a clean fashion. Usually in non-relativistic
fluids one would talk about heat flow between different fluid elements, but for a relativistic
fluid heat flux necessarily leads to mass or momentum transfer and hence to energy flow.
By picking the velocity field appropriately we can fix this ambiguity; the precise fashion in
which we choose to do so is simply a matter of convention.

    For ideal fluids we picked the velocity field such that in the local rest frame of a fluid
element, the stress tensor components longitudinal to the velocity gave the local energy
density in the fluid. One can in fact demand the same to be true when we incorporate the
effects of dissipation. This leads to the so called Landau frame which is defined by demanding
that the dissipative contributions be orthogonal to the velocity field i.e,.

     � u� = 0 ,      � u� = 0 .                 (2.9)

Formally, one can define the Landau frame as follows: the stress tensor which is a symmetric
two-tensor on the background manifold Bd has a single timelike eigenvector. In the Landau
frame we define the velocity field u� to be given by this eigenvector (unit normalized), so
that the definition of the velocity field is tied to the energy-momentum transport in the
system. For charged fluids one has the possibility of working in the so called Eckart frame
where the fluid velocity is tuned to charge transport � here we define the velocity field to
be the determined by the charge current. In what follows we will work exclusively in the
Landau frame and hence apply (2.9) to constrain the dissipative terms of the stress tensor
and charge currents.

Enumerating independent operators: The issue of enumerating the independent op-
erators at any given order is completely analogous to the discussion in effective field theory.
Suppose we are interested in generalizing the ideal fluid (2.2) to first order in the gradient
expansion. For the stress tensor we would write down all possible symmetric two tensors
built out of the gradients of the velocity field and thermodynamic variables. However, the
ideal fluid equations of motion (2.1) themselves are first order in derivatives, and therefore
relate the derivatives of the thermodynamic potentials to the gradients of the velocity field.
Employing these relations we can simplify the expression for the first order stress tensor
to be given in terms of derivatives of the velocity field alone. This process can clearly be
iterated to higher orders.

Decomposing velocity gradients: We are interested in analyzing various combinations
of derivatives of the velocity field. First let us consider the decomposition of the velocity
gradient u� into a part along the velocity, given by the acceleration a�, and a transverse
part. The latter can in turn be decomposed into a trace, the divergence , and the remaining
traceless part with symmetric and antisymmetric components, respectively given by the shear
� and vorticity �. The decomposition can then be written as follows:

 u�  =  -a� u  + �  + �  +     1       P  �  ,  (2.10)
                               -
                            d     1

                 11
where the divergence, acceleration, shear, and vorticity, are defined as:6

             = �u� = P � �u

            a� = u  u�  D u�

            �    =  (�u)    +  u(�  a)   -     1       P �  =   P �  P    (u)  -          1      P �               (2.11)
                                               -                                          -
                                            d     1                                  d       1

            � = [�u] + u[� a] = P � P  [u] .

For future reference we note that we will also have occasion to use a the following notation to

indicate symmetric traceless projections transverse to the velocity field. For any two tensor

T � we define:                                                    1
                                                                d-1
                               T  �  =   P � P  T()         -             P �  P  T  .                             (2.12)

    Note that we can write the projectors a bit more compactly: P � P  ( u) = P (�u)
and P � P  [ u] = P [�u]. It is easy to verify all the previously asserted properties,
in addition to u� a� = 0 and P� a� = a:

                            � u� = 0 ,               � P = � ,                 �� = 0 ,                            (2.13)
                            � u� = 0 ,               � P = � ,                 �� = 0 .

    We are now in possession of sufficient amount of data to write down the dissipative part
of the stress tensor to leading order in the derivative expansion. First of all let us notice
that the zeroth order equations of motion i.e., those arising from the ideal fluid description
relate the gradients of the energy density and pressure to those of the u�. The quickest
way to derive the required relation is to consider projections of the conservation equation
� (T �)ideal = 0, along the velocity field and transverse to it, i.e.,

                     u � (T � )ideal = 0 = ( + P ) �u� + u�� = 0                                                   (2.14)
                    P � (T � )ideal = 0 = P��P + ( + P ) P u� �u = 0 .

respectively. To characterize the stress-tensor at leading order in the gradient expansion
our task is reduced to writing down symmetric two tensors that can be built solely from
velocity gradients and we should furthermore account for the Landau frame condition. These
conditions in fact isolate just two terms which can appear in the expression for �:

                                         �(1) = -2  � -   P � ,                                                    (2.15)

where we have introduced two new parameters the shear viscosity, , and the bulk viscosity,
.

    Likewise for the charge current � we will obtain contributions which are first order in the
derivatives of the thermodynamic variables  and qI and also the velocity field (where now

    6Note that we use standard symmetrization and anti-symmetrization conventions. For any tensor Fab
                                            1                                                             1
we  define  the  symmetric  part  F(ab)  =  2  (Fab + Fba)      and  the  anti-symmetric  part  F[ab]  =  2  (Fab  -  Fba )

respectively. We also use D to indicate the velocity projected covariant derivative: D  u� �.

                                                            12
the acceleration contributes). We will choose this time to eliminate the acceleration term
using zeroth order equation of motion (2.14) and express derivatives of energy density and
charge density. Usually these are the only contributions which are considered for the charge
current. However, there is another potential contribution from a pseudo-vector [71, 72],

                      � = � u u,                                   (2.16)

provided we are willing to mix contributions with different parity structure at the first order.

In fact, for fluid dynamics derived from the AdS/CFT correspondence for the N = 4 Super

Yang-Mills fluid, there is indeed a contribution of this sort to the charge current (in a specific

ensemble).7 Putting things together we find that we have a first order contribution to the

charge current:

                      (�1)I = -IJ P �  qJ - I P �   - I � ,        (2.17)

where we again have new coefficients, IJ is the matrix of charge diffusion coefficients, I
indicates the contribution of the energy density to the charge current, and I which are the
pseudo-vector transport coefficients. For later purposes, it will be convenient to re-express

the charge current in terms of the intensive parameters �I and T (chemical potential and
temperature), so that (2.18) can be recast equivalently as8

                      �(1)I = -IJ P �   �J  - I � - I P � T .      (2.18)
                                        T

    Assembling all the pieces together we claim that a generic charged fluid flow will satisfy
the dynamical equations (2.1) with the stress tensor and charge currents at leading order in
gradient expansion (dropping therefore higher derivative operators):

                 T � =  u� u + P (g� + u� u) - 2  � -   P � ,

                 JI�  = qI u� - IJ P �      �J  - I � - I P � T .  (2.19)
                                            T

Following conventional terminology we will refer to the fluid dynamical system specified by
(2.19) as a viscous fluid or relativistic Navier-Stokes equations.9

    Apart from the thermodynamic potentials, we have a set of transport coefficients , ,
IJ , I and I which need to be determined to completely specify the relativistic viscous
fluid. If the QFT whose hydrodynamic description we seek is weakly coupled then we can
in principle determine these coefficients in perturbation theory. This is per se not a trivial
exercise, for a discussion of the computation of transport coefficients in perturbative gauge
theory see [89, 90]. We will however be interested in deriving these coefficients for a strongly
coupled quantum field theory using a dual holographic description.

    7This contribution can be traced to Chern-Simons couplings of the bulk gauge field in the gravitational

description, c.f., [71, 72].
    8One can relate the transport coefficients {IJ , I } to the original coefficients {IJ , I } in terms of

various susceptibilities. However, getting explicit expressions for these in general will require knowledge of

the precise thermodynamic functions. We thank R. Loganayagam for useful discussion in this regard.
    9We will review the conventional non-relativistic equations later, see �6.2.

                                        13
Finally, let us turn to the other quantity of interest, viz., the entropy current. Including

the effects of dissipation we learn that entropy is no longer conserved. Under fluid evo-

lution we should have entropy production since the system is generically evolving from a

non-equilibrium state to an equilibrium state. Entropy increase consistent with the second

law can be rephrased as the statement that the entropy current should have non-negative
divergence. For a relativistic viscous fluid we will therefore have an entropy current JS� with

�JS�  0 .                                                        (2.20)

It is possible to show that for uncharged fluids involving pure energy momentum transport
one has a entropy current statisfying:

�JS�  =  2       ,                                               (2.21)
         T

which is non-negative as long as the shear viscosity is positive. We will return to a detailed

discussion of the entropy current for conformal fluids in �5.4.

2.3 Causality issues in relativistic viscous fluids

A natural question is whether the relativistic viscous fluids can be extended to higher or-
ders.10 To determine this we should just follow the conventional philosophy of effective field
theory and try to write down the full set of operators at the desired order in gradient ex-
pansion. These higher order terms will be less and less important (they are irrelevant in the
low energy effective theory) as we go to longer wavelengths and are thus somewhat inconse-
quential for the hydrodynamic evolution. The leading order terms which we incorporated in
the viscous fluid (2.19) are singled out because of their importance in realizing a channel for
the fluid to relax back to equilibrium � they are the leading dissipative terms in the theory.

    However, in conventional relativistic fluid literature one usually encounters a different
rationale having to do with causality issues and the initial value problem. Consider the
viscous fluid system (2.19) with the dynamical equations (2.1). This system of equations is
first order in time derivatives,11 and as a result the system of partial differential equations
equations describing a relativistic viscous fluid is parabolic.

    In order to have a relativistic system with a well defined initial value problem the equa-
tions of motion are required to be hyperbolic. Only for hyperbolic partial differential equa-
tions is it possible to evolve initial data specified on a Cauchy surface. Usually lack of
hyperbolicity leads to formation of singularities and manifests itself by acausal behaviour. A
useful analogy to keep in mind, which is in fact central to the current discussion, is the heat
equation, which being first order in time derivatives is parabolic. Solutions to the heat equa-
tion show diffusive behaviour which leads to acausal propagation of signals (when viewed
with respect to the light-cone of the underlying Lorentzian manifold Bd).

  10We will refer the generalized system of fluid dynamical equations as non-linear viscous hydrodynamics,
notwithstanding the fact that the relativistic Navier-Stokes equations themselves are non-linear.

  11The simplest way to see this is to work in the local inertial frame and realize that the gradient terms in
(2.19) only involve spatial derivatives owing to the projector P � .

         14
This issue has led several people to come up with so called "causal relativistic hydro-

dynamics", the most prominent among which is the phenomenologically motivated Israel-

Muller-Stewart formalism [87, 88].12 For sake of completeness we will briefly review the

Israel-Stewart formalism and in particular will argue that the issue of causality violation in

the hydrodynamic description is a red-herring.

The Israel-Stewart idea is to add higher order terms to the relativistic viscous fluid system

(2.19). The terms that are added are such that the resulting entropy current satisfies the

second law (2.20). However, it is worth noting that their phenomenological formalism doesn't

fully account for all the irrelevant operators one can add at the corresponding order [83]. We

will illustrate the formalism with a simple toy model which captures the basic idea behind

their approach.

Consider the derivation of the diffusion equation from the continuity equation, which is

a conservation equation13            
                                     t
                                         +     �   j  =  0  ,                             (2.22)

and the phenomenological Fick's law

                                         j = -D  ,                                        (2.23)

where D is the diffusion constant. Eliminating the current j we find the diffusion equation

                                         -  D  2      =  0     .                          (2.24)
                                     t

    The equation (2.24) of course has a diffusive spectrum   -i k�k and is a simple example
of a parabolic PDE which doesn't have a well defined initial value problem. The problem is
that any perturbation to the system instantaneously spreads out to arbitrary spatial scales �
essentially the fluctuations don't relax quickly enough. In the diffusion equation (2.24), due
to absence of quadratic term in time derivatives, the velocity of propagation of disturbances
is infinite. Equivalently, in the absence of density fluctuations there is nothing forcing the
current to relax to its stationary equilibrium value. Ideally, the current should damp out
exponentially in time. This can be achieved by phenomenologically modifying Fick's law
(2.23). Consider introducing a relaxation time scale  so that (2.23) is modified to

                                  j = -D  -  tj ,                                         (2.25)

One can think of the deformation to Fick's law described above as an example of the leading
irrelevant operator that we include in the system. Now eliminating the current between
(2.22) and (2.25) we find a hyperbolic equation, for

                 -  D  2   -      �  tj  =  0               -     D  2  +    t2  =  0  .  (2.26)
t                                                     t

  12For reviews on this subject we refer the reader to [86, 91]. In the context of heavy-ion collisions an
excellent discussion complemtenting our presentation here can be found in [92]. See also [58] for related

discussion in the holographic context.
  13For the sake of simplicity we will momentarily switch to a non-relativistic system; for the present

discussion  is a spatial gradient.

                                               15
Note that we have used the fact that we are interested in the lowest order terms in the
gradient expansion and are therefore free to use the lower order equations of motion (2.24)
to simplify the dynamical equations. (2.26) has a finite velocity for the propagation of the
density fluctuations, vprop = D/.

    The toy model illustrates the basic idea involved in the Israel-Stewart construction of
"causal relativistic hydrodynamics" � in their construction one adds a class of second deriva-
tive terms to the viscous relativistic hydrodynamics (2.19). It transpires that their construc-
tion actually ignores some of the two derivative operators allowed by the symmetries, see
the discussion in [83] in the context of conformal fluids.

    However, as clearly described in [93] this whole discussion is rather misleading. The
essential point is that the effects of the higher order terms which are added to render the
theory causal are of decreasing relevance deep into the hydrodynamic regime. From the
effective field theory viewpoint emphasized here this is completely obvious � the irrelevant
operators have diminishing role to play as we move into the deep infra-red. Modes which
manifest acausal behaviour are outside the long-wavelength regime and are not part of the
hydrodynamic description. Curing this causality problem completely requires us to actually
go back to the microscopic description of the theory. It is nevertheless interesting to ask
what the systematic procedure to extend the relativistic viscous hydrodynamics is and we
will address this question to second order in derivatives in the rest of these lectures.

3 Conformal fluids

So far our discussion of fluid dynamics has been quite general and is valid for the hydrody-
namic limit of any interacting Lorentz invariant quantum field theory. We now turn to a
discussion of field theories which are conformally invariant. After briefly reviewing the con-
formal transformation properties of the stress tensor, we turn to the construction of operators
in the gradient expansion that transform homogeneously under conformal transformations.
This will allow us to classify the set of operators that can appear in conformal hydrodynam-
ics beyond leading order; for pure energy momentum transport this was first undertaken in
[83]. We will then undertake a brief overview of an extremely useful framework for discussing
conformal fluids, the so called Weyl covariant formalism [84]. This will be useful when we
construct gravitational duals to conformal fluids in �4.

3.1 Weyl transformation of the stress tensor

Consider a relativistic fluid on a background manifold Bd with metric g�. We wish to
consider a local Weyl rescaling of the metric and understand the transformation of the stress
tensor. Given a Weyl transformation of the boundary metric

g� = e2 g�  g� = e-2g� ,  (3.1)

16
it is clear that the velocity field appearing in the stress tenor transforms as

                                          u� = e- u� ,                                               (3.2)

which is a direct consequence of the normalization of the velocity field, u� u� = -1. It
follows from (3.1) and (3.2) that the spatial projector transforms homogeneously as well:

P � = g� + u�u = e-2 P � .

    We are interested in the behaviour of the stress tensor under conformal transformations.

In  general  a  tensor  Q  with  components  Q1���m       is  said  to   be  conformally  invariant  if  it
                                                �1 ����n

transforms homogeneously under Weyl rescalings of the metric, i.e., Q = e-w  Q under (3.1).

The real number w is the conformal weight of the tensor. It is important to remember that

the weight of a tensor operator under Weyl transformations depends on the index positions.14

We also should require that the dynamical equations satisfied by Q remain invariant under

conformal transformations.

    It is easy to work out the constraints on the stress tensor using the dynamical equation

at hand (2.1). We find that first of all the conformal invariance requires that the stress

tensor be traceless T�� = 0 and that it transforms homogeneously under Weyl rescalings of
the metric with weight d + 2

                                 T � = e-(d+2)  T � .                                                (3.3)

These statements follow from the conservation equation (2.1) for the stress tensor, written
in the Weyl transformed frame. We refer the reader to Appendix D of [94] for a derivation of
these results. The tracelessness condition in fact supplies the equation of state for conformal
fluids. Going back to the ideal fluid (2.2), we find that

                                 T�� = 0  =  P   =        d   1  1    .                              (3.4)
                                                              -

This relation between pressure and energy density fixes the speed of sound in conformal

fluids to be a simple function of the spacetime dimension:               cs =  1      .  Likewise it is not
                                                                                 d-1

hard to show the charge current transforms homogeneously with weight d under conformal

transformations

                                          J � = e-d  J �.                                            (3.5)

    Another piece of data we need is the information of the scaling dimensions of the ther-
modynamic variables. It is for instance easy to see that the temperature scales under the
conformal transformation with weight 1. Similarly it follows from the thermodynamic Gibbs-
Duhem relation, P +  = s T + �I qI, that the chemical potentials �I also have weight 1.
Hence using (3.3) and (3.1) it follows that the energy density is given by a simple scaling
law (a natural extension of the Stefan-Boltzmann scaling to d spacetime dimensions)

                                 T = e- T~ =   T d                                                   (3.6)

  14One could equivalently talk about the invariant conformal dimension which involves a shift by a simple
linear combination of the number of upper and lower indices: winv = w - nlower + nupper. This follows from
accounting for the weight of the metric.

                                             17
These results together imply that an ideal conformal fluid has a stress tensor

                              (T �)ideal =  T d (g� + d u� u) ,                 (3.7)

where  is a dimensionless normalization constant which depends on the underlying micro-
scopic CFT.

    To construct the fluid stress tensor at higher orders we simply need to enumerate the
set of operators in our gradient expansion which transform homogeneously under (3.1). Let
us consider the situation at first order in derivatives explicitly. Using the fact that the
Christoffel symbols transform as [94]

                               � = � +  � + �  - g� g  ,
we can show that the covariant derivative of u� transforms inhomogeneously:

            �u = �u + � u = e- � u + � u  - g� u g  .                           (3.8)

This equation can be used to derive the transformation of various quantities of interest in
fluid dynamics, such as the acceleration a�, shear �, etc..

             = �u� = e- �u� + (d - 1) u  = e-  + (d - 1) D ,

            a = D u = u��u = e-2 a + P   ,                                      (3.9)

            �  =  P (�u)      -  d  1  1  P �  u  =  e-3   � ,
                                    -

            � = u �u = e-2  � ,

where in the last equation we have accounted for the fact that all epsilon symbols should be

treated as  tensor densities  dinetceurrmviendansptsacie.e. .,Theobjects -wgit,hacnodrrecttensor1-tgr,anfrsofomrmwahtiiochn
properties  scale as metric

it is easy to infer their scaling behaviour under conformal transformations; in particular,

 = e4  and  = e-4  .
    Armed with this information we can examine the terms appearing in the first order

conformal fluid. From (3.9) we learn that the expansion , transforms inhomogeneously

implying that the coefficient of the bulk viscosity should vanish for a conformal fluid  =

0.15 Likewise, for the charge current we can show that the contribution from the chemical

potential and temperature should be in the combination �I/T ; the term involving gradient of
the temperature P � T transforms inhomogeneously under Weyl transformations requiring
I = 0. Therefore a conformal viscous fluid has a stress tensor which to first order in the
gradient expansion takes the form

                  T � =  T d (g� + d u� u) - 2  � ,

                  JI�         = qI u� - IJ P �             �J   - I � ,         (3.10)
                                                           T

15Equivalently, this follows from the tracelessness of the stress tensor.

                                               18
where we have used the generalized Stefan-Boltazmann expression for the pressure. We also
can deduce the conformal properties of the transport coefficients; in particular,

 = T d-1 ^ (�I/T ) .                                        (3.11)

3.2 Weyl covariant formulation of conformal fluid dynamics

It is straightforward to carry out this exercise to higher orders in the gradient expansion by
again analyzing the transformation properties of the various operators under Weyl rescalings.
This was carried out for uncharged fluids in [83] to second order and a detailed check of this
for the specific second order stress tensor derived holographically is given in [4]. However,
it is useful to work a little more abstractly and exploit a little more of the structure of the
conformal symmetry to present the answer compactly in a Weyl covariant form. We therefore
will pause to review some details of this presentation following the beautiful work of [84].

    The basic point is as follows: when we are discussing a conformal field theory and the
associated hydrodynamic description on a background manifold Bd we are not interested in
the metric data on Bd, but rather on the conformal structure on this background manifold.
We can exploit this fact to simplify the structure of the derivative expansion by directly
working with the conformal class of metrics on Bd. For brevity, let us denote the background
with this conformal class of metrics as (Bd, C).

    On (Bd, C) we will define a new derivative operator that keeps track of the Weyl trans-
formation properties better. A key fact that we will exploit is that fluid dynamics comes
equipped with a distinguished vector field, the velocity, which as emphasized earlier is just
the timelike unit normalized eigenvector of the stress tensor. We start by defining a torsion-
less connection called the Weyl connection, whose associated covariant derivative captures
the fact that the metric transforms homogeneously under conformal transformations (with
weight -2). In particular, the Weyl connection Weyl requires that for every metric in the
conformal class C there exists a connection one-form A� such that

Weylg� = 2 A g� .                                           (3.12)

Given this derivative structure, we can go ahead and define a Weyl covariant derivative D�

as whose action on tensors transforming homogeneously with weight w under i.e., Q������� =
e-w  Q������� is given by

DQ�������  Q������� + w A Q�������                          (3.13)
                + (g A� - � A - � A) Q������ + � � �
                - (g A -  A -  A) Q������� - � � � .

The nice thing about this definition is that DQ������� = e-w  DQ�������, i.e., the Weyl covariant
derivative of a conformally invariant tensor transforms homogeneously with the same weight

as the tensor itself.

19
    One can view the Weyl covariant derivative as being determined in terms of the Weyl
connection via D� = W � eyl + w A�. From this description it follows immediately that the
Weyl connection is metric compatible Dg� = 0 which follows from (3.12) and the fact
that w = -2 for g�. In addition, in fluid dynamics we will require that the Weyl covariant
derivative of the fluid velocity be transverse and traceless, i.e.,

                u Du� = 0 ,         Du = 0 .                      (3.14)

These conditions enable to uniquely determine the connection one-form A� to be the the
distinguished vector field

A�        =  u  u�  -  d  1  1  u�  u    a�  -  d  1  1    u�  ,  (3.15)
                          -                        -

built from the velocity field of fluid dynamics.
    One can rewrite the various quantities appearing in the gradient expansion of the stress

tensor in this Weyl covariant notation. For instance at first order in derivatives we have the
objects constructed from the velocity field

             � = D(�u) ,            � = -D[�u] ,                  (3.16)

both of which can be seen to have weight w = 3. The dynamical equations of fluid dynamics
(2.1) can be recast into the Weyl covariant form. For instance, stress tensor conservation
can be easily seen to be D� T � = 0; for

D�T � = � T � + w A� T � + g� A� - �� A - � A� T  + g� A - � A -  A� T �

= � T � + (w - d - 2) A� T � - A T��

= �T � ,                                                                                        (3.17)

where we used the conformal weight w = d + 2 of the stress tensor and the tracelessness
condition to remove the inhomogeneous terms. For CFTs on curved manifolds one has the
possibility of encountering a conformal anomaly in even spacetime dimensions; incorporating
the trace anomaly W we can write the fluid dynamical equation as

             D�T � = �T � + A T�� - W = 0 .                       (3.18)

3.3 Non-linear conformal fluids

We will now discuss the general conformal fluids to second order in derivative expansion using
the Weyl covariant formalism, with an aim to cast fluid mechanics in manifestly conformal
language. In order to achieve this we need to write down the set of two derivative operators
that transform homogeneously under conformal transformations. These operators involve
either two derivatives acting on the dynamical degrees of freedom or terms involving squares
of first derivatives. We now proceed to enumerate these operators:

                                20
    For operators built out solely from the fluid velocity, one has the following terms which
explicitly have two derivatives

D�Du = D�  + D� = e-D�Du~                                       (3.19)

    D� = e D� ,                                D� = e D� .

In addition we can have terms which have the combinations:

�  = e-4  �  ,  �  = e-4  �  ,                 �  = e-4  �  , (3.20)

which involve the squares of the first derivative operators.
    In addition to the operators built out of the velocity field we should also consider terms

which involve the temperature T and various chemical potentials �I. Recalling that both of
these have weight 1 under conformal transformations, i.e., T = e- T and �I = e- �~I, we
can write down the relevant operators involving no more than two derivatives:

D�  �I          = D�  �I                ,      D�T = e-D�T
    T                 T                         DDT = e- DDT .
                                                                (3.21)
    �I                    �I
DD  T           = DD      T

    To complete the classification of the various tensors that can be constructed at the second
derivative level, we need to study the curvature tensors that appear via the commutators of
two covariant derivatives. These appear because the fluid couples to the background metric
g� on the manifold Bd and the curvature terms arise at second order in derivatives. These
terms will be of particular importance in the holographic context; for example in deriving
the fluid dynamical behaviour of N = 4 SYM on S3 � R we encounter curvature terms. We
review the definition of the curvature tensors in the Weyl covariant formalism in Appendix
A. For the present we just record the symmetric traceless tensor involving two derivatives
of the background metric on Bd,

                C� u u = C� u~ u~                               (3.22)

where C� is the Weyl tensor see (A.8).

3.4 The non-linear conformal stress tensor

We are now in a position to discuss the non-linear hydrodynamics for conformal fluids. For
the sake of brevity we will confine attention to fluids which have no conserved charges. This
is equivalent to working in the canonical ensemble and focussing just on energy momentum
transport. The results we derive here will be universal for a wide class of conformal fluids.

    Let us classify all the operators which are Weyl invariant at various orders in the derivative
expansion. The results of the previous section �3.3 can be summarized as follows: at first two

                                           21
orders in derivatives the set of symmetric traceless tensors which transform homogeneously
under Weyl rescalings are given to be16

            First order : �

            Second order : T�1 = 2 u D� , T2� = C� u u ,

                               T�3 = 4  �  ,             T�4 = 2  �  ,                      T5�   =      �    


where we have introduced a notation for the second derivative operators which will be useful

to write compact expressions for the stress tensor below. Armed with this data we can

immediately write down the general contribution to the stress tensor as:

                      (�1) = -2  �                                                                                   (3.23)
                      �(2) =   T1� +  T2� + 1 T�3 + 2 T�4 + 3 T�5 .

There are therefore have six transport coefficients , , , i for i = {1, 2, 3}, which char-
acterize the flow of a non-linear viscous fluid.

    For a fluid with holographic dual using the explicit result of the gravitation solution (5.1)
(see �5.1) and the holographic stress tensor [95, 96] we find explicit values for the transport
coefficients. In particular, for the N = 4 SYM fluid one has17 [4, 83]

                               =     N2  (T )3     =            =  1     ,
                                     8                       s     4

                                  =  2 - ln 2   ,          =                                                         (3.24)
                                      2 T                       T

                            1     =          ,     2     =    ln 2  ,             3 = 0 .
                                     2 T                      T

where in the first line we have used the standard entropy density for thermal N = 4 SYM

at  strong  coupling  s  =  3  N2    T3  to     exhibit  the    famous      ratio       of  shear    viscosity   to  entropy
                            2

density [19].

    The general analysis in AdSd+1 of carried out in [68, 69] in fact allows us to write down
the transport coefficients described above in arbitrary dimensions in nice closed form.18 The

transport coefficients for conformal fluids in d-dimensional boundary Bd are:

                            1            4      d-1                      1
                            GN(d+1)      d                      s        4
                 =    16                    T            =         =           ,

                 =      d      1   +  1  Harmonic        2   -  1     ,             =   2    d       2)              (3.25)
                      4 T             d                  d                                  (d -         T

               1 =    d        ,        2  =    1  Harmonic         2    -  1           ,         3 = 0 .
                      8     T                   2                   d               T

16Various papers in the literature seem to use slightly different conventions for the normalization of the

operators. We will for convenience present the results in the normalizations used initially in [83]. This is the

source of the factors of 2 appearing in the definition of the tensors Ti, see [4] for a discussion.

17The result for generic N = 1 superconformal field theories which are dual to gravity on AdS5 �X5 are
                           N2
given by simply replacing  82  by  the  corresponding    central   charge of      the   SCFT.
  18For d = 3 the general                                          [67]. See      also  [59] for
                           results were initially derived in                                      determination  of  some  of

these coefficients in d = 3 and d = 6.

                                                         22
where Harmonic(x) is the harmonic number function.19

4 Non-linear fluid dynamics from gravity

Our discussion of fluid dynamics has thus far been very general and in fact is valid for

any interacting field theory. As we have seen one can distill the information in this low

energy effective description into the specification of a finite number of transport coefficients.

The transport coefficients can in principle be determined from the microscopic field theory.

However, if we are interested in systems which are intrinsically strongly coupled then we

need to find a technique to extract the non-perturbative values of the transport coefficients.

In the rest of these lectures we will focus on such strongly coupled scenarios. As is well

known, for a class of such theories one can exploit the AdS/CFT correspondence to extract

the hydrodynamical parameters and this will be our prime focus.

    Let us consider a d dimensional field theory on a background manifold Bd which is holo-
graphically dual to string theory on an asympotically AdSd+1 spacetime (which is perhaps
warped with some internal compact manifold to be a critical string background). The pro-

totype example which we should keep in mind is the classic duality between Type IIB string

theory on AdS5 �S5 and the dynamics of N = 4 SYM. Following standard parlance we will
refer to the field theory as living on the boundary of the asymptotically AdS spacetime.20

In the example of N = 4 SYM we have two dimensionless parameters in the field theory,

the 't Hooft coupling  and the rank of the gauge group N (we will consider unitary gauge

group SU(N)). In the limit of large N and large  the field theory dynamics is captured by

classical gravity as the dual string coupling is small and one moreover has a macroscopically

large AdS5 spacetime.
    In the planar large N limit, the field theory dynamics truncates to the dynamics of

single  trace  operators  O  =  1  Tr ()  where    is  a  collection  of  the  basic  fields  appearing  in
                                N

the Lagrangian. For N = 4 SYM one has the bosonic R-charge scalars transforming in the

vector representation of the SU(4) R-symmetry, the gauge fields, and fermions; schematically

 = {Xi, D�, }. The dynamics in the single trace sector in the planar limit is classical due
to large N factorization, but the general structure is hard to derive even for the particularly

symmetric case of N = 4 SYM. From a field theory viewpoint issues such a locality of

this effective classical description are rather mysterious. However, once we pass to the

holographic dual we encounter a manifestly local description in terms of two derivative

gravity coupled to a bunch of matter fields in an asymptotically AdS5 spacetime. In making

19The harmonic number function may be in fact be re-expressed in terms of the digamma function, or

more simply as

                                   Harmonic(x)   = e +    (x)  ,
                                                          (x)

where e is Euler's constant; see [97] for a discussion of its properties.
  20For four dimensional boundary field theories we can replace the S5 by a Sasaki-Einstein manifold X5

such as T 1,1 or Lp,q,r. In these cases one recovers N = 1 quiver superconformal gauge theories on the

boundary.

                                                 23
this statement we are assuming that we have performed a Kaluza-Klein reduction of the
Type IIB supergravity fields over the compact S5 leading to an infinite tower of massive
fields coupled to the gravitational degrees of freedom.

    The general structure of this effective five-dimensional lagrangian is not only complicated
but it also depends on the details of the internal space. Were one to replace the S5 by a
Sasaki-Einstein five manifold X5 one would end up with a different effective description
corresponding to a different field theory fixed point in four dimensions. However, there is a
universal sub-sector of Type IIB supergravity which we can focus on � this is just the sector
of solely gravitational dynamics in AdS5 i.e., we set all the Kaluza-Klein harmonics of the
graviton modes on S5 and other matter degrees of freedom consistently to zero. We will
restrict attention to this sub-sector which corresponds in the dual field theory to focussing
on just the dynamics of the energy-momentum tensor.

4.1 The universal sector: gravity in AdSd+1

As discussed above we will concentrate on pure gravitational dynamics in asymptotically
AdS spacetimes. This in particular allows us to work without loss of generality in arbitrary
dimensions as the form the gravitational action is independent of the number of spacetime
dimensions. Let us therefore consider starting with a string or M-theory background of
the form AdSd+1 �X where X is some compact internal manifold ensuring that one has a
consistent string/M-theory vacuum.21 The universal sector of this theory which we focus on
is the dynamics of Einstein gravity with a negative cosmological constant, i.e.,

Sbulk  =       1                                                                  (4.1)
          16 GN(d+1)     dd+1x -G (R - 2 ) .

With a particular choice of units (RAdS = 1) Einstein's equations are given by22

EM N      =  RM N  -  1  GMN R  -            d(d -  1)  GM N  =  0
                      2                          2
                                                                                  (4.2)

= RMN + d GMN = 0, R = -d(d + 1).

    Of course the equations (4.2) admit AdSd+1 solutions, which correspond to the vacuum
state of the dual field theory. Recall that global AdSd+1 has as its boundary the Einstein
static universe, R�Sd-1. We are free to consider other choices of boundary manifolds Bd; for
instance to discuss field theory on Minkowski space Rd-1,1 we would focus on the Poincar�e

patch of AdSd+1. Given a metric g on the boundary Bd we have the bulk geometry to zeroth

  21We will be interested in d > 2. As discussed in [66, 69] there is no interesting hydrodynamic limit for a
1 + 1 dimensional CFT. A conserved traceless stress tensor is simply made up of left and right moving waves
which propagate with no dissipation.

  22We use upper case Latin indices {M, N, � � � } to denote bulk directions, while lower case Greek indices
{�, , � � � } refer to field theory or boundary directions. Finally, we use lower case Latin indices {i, j, � � � } to
denote the spatial directions in the boundary.

                         24
order in the Fefferman-Graham expansion given by23

                                    ds2  =  1    dz2 + g� dx� dx .                                                   (4.3)
                                            z2

We will refer to these spacetimes as asymptotically AdSd+1 although this terminology is
strictly speaking incorrect in a strict general relativistic sense. We will return to the issue
of how to find solutions to (4.2) with this prescribed boundary metric, after discussing some
issues related to fluid dynamics.

    We are interested in the description of the field theory in the canonical ensemble and
in particular on situations where the field theory only attains local thermal equilibrium.
There is usually an interesting phase structure for the field theories on non-trivial boundary
manifolds Bd. Usually this arises from the fact that one can have dimensionless ratios of
length scales arising from the non-trivial geometry of the background. The classic example
is Bd = R � Sd-1 where the low temperature phase is described to be the confined phase
with O (1) free energy while the high temperature phase is the deconfined phase with O (N2)
free energy [98]. The former phase is dual to a thermal gas in AdSd+1 while latter phase has
a geometric description in terms of a Schwarzschild black hole in AdSd+1.

    To discuss hydrodynamics we need to be in the long-wavelength regime which is achieved
only in the deconfined phase at high temperatures [65]. A simple way to see this is to
note that in conformal field theories the phase structure is determined by the dimensionless
ratio of length scales � if Bd has curvature scale Rc and we are interested in the canonical
ensemble at temperature T , then the phase structure depends on Rc T . However, since the
mean free path of the system mfp  1/T from conformal invariance, we see that in order
for the gradient expansion to be valid we require that Rc T  1. This can equivalently be
interpreted as the statement that variations in the curvature of the background are small in
units of the local temperature which means that we can approximate the boundary metric
to be locally flat. This discussion is in perfect accord with the fact that for the CFT on
Minkowski space the absence of any length scales in the background means that one has a
trivial phase structure � the field theory is always deconfined on Rd-1,1.

    Therefore to construct the dual of hydrodynamics on a curved boundary manifold Bd
we can use as our starting point a flat boundary and systematically account for curvature
terms as we proceed in the gradient expansion. In fact, the leading order viscous hydrody-
namics is insensitive to the boundary curvature terms which only show up at second order
in derivatives.

    23In fact, if g� is Ricci flat then (4.3) satisfies the Einstein's equations (4.2). Similar constructions

can be made for Einstein metrics on the boundary, albeit with a different warping function i.e., ds2 =

1   dz2 + F (z) g� dx� dx  for  an  appropriate  choice  of  F (z).  For  instance  F (z)  =  (1 +  z2  )2  for  an  Einstein
z2                                                                                                  4
manifold with negative curvature.

                                                 25
4.2 Preliminaries: Schwarzschild black holes in AdSd+1

Let us consider the geometry dual to thermal field theory on Minkowski space, which is given
by the planar Schwarzschild-AdSd+1 black hole which in Schwarzschild type coordinates is
given by

                    ds2     =  -r2  f (b r) dt2    +     dr2       +  r2 ij  dxi dxj  ,
                                                      r2 f (b r)
                                                                                                (4.4)
                                    1
                    f (r) = 1 -     rd   .

While this is a one-parameter family of solutions labeled by the horizon size r+ which sets

the temperature of the black hole                      d
                                                      4 b
                                                T  =         ,                                  (4.5)

it is easy to generate a d parameter family of solutions by boosting the solution along the

translationally invariant spatial directions xi, leading to a solution:24

                    ds2  =  r2  dr2      +  r2  (-f (b r) u�    u  +  P� )   dx�  dx            (4.6)
                                f (b r)

with

                                            uv =          1
                                            ui =
                                                      1 - 2                                     (4.7)

                                                      i         ,

                                                      1 - 2

where the temperature T and velocities i are all constants with 2 = j j, and P � =
u�u + � is the projector onto spatial directions. These solutions are generated by a

simple coordinate transformation from (4.4) and can be understood physically as follows.

The isometry group of AdSd+1 is SO(d, 2). The Poincare algebra plus dilatations form a
distinguished subalgebra of this group. The rotations SO(d) and translations R1,d-1 that

belong to this subalgebra annihilate the static black brane solution (4.4) in AdSd+1. This is
manifest from the symmetries of the background (4.4). However, the remaining symmetry

generators, which are the dilatations and boosts, act nontrivially on this brane, generating a

d parameter set of black hole solutions. The parameters which characterize the bulk solution

are precisely the basic hydrodynamical degrees of freedom, viz., temperature and the velocity

of the black hole.

    The boosted black hole (4.6) is an asymptotically AdSd+1 solution which has a holo-
graphic stress tensor on the boundary. It is in fact not hard to see that the stress tensor

for this solution is the ideal conformal fluid stress tensor (3.7) with a particular value of the

normalization constant  =           . d     This is not surprising as the solution is stationary

                                16 G(Nd+1)

24The indices in the boundary are raised and lowered with the Minkowski metric i.e., u� = � u.

                                                      26
and therefore corresponds to the global thermal equilibrium. To describe hydrodynamics we
should perturb the system away from global equilibrium. Based on our discussion in �2 it is
natural to consider a situation where the thermodynamic variables vary along the boundary
directions. This can be simply achieved by promoting the parameters b, i to functions
of the boundary coordinates and furthermore letting the boundary metric vary to account
for curvature couplings. As long as the variations are of large wavelength we can work in
the effective field theory framework and construct a solution order by order in boundary
derivative expansion.

    Roughly speaking, our construction may be regarded as the `Chiral Lagrangian' for brane
horizons. We have hitherto discussed how the dilatation and boost generators of the con-
formal algebra act on the space of black hole solutions which is described by a point in d
dimensional parameter space. Our construction effectively promotes these parameters to
`Goldstone fields' (or perhaps more accurately collective coordinate fields) and determines
the effective dynamics of these collective coordinate fields, order by order in the derivative
expansion, but making no assumption about amplitudes.25

4.3 Regularity and choice of coordinate chart

Whilst it is straightforward to promote the parameters b and i appearing in (4.6) to func-
tions depending on (t, xi), there is a subtlety we need to consider. The issue is that the
Schwarzschild coordinates used to write the metric in (4.6) are not regular on the future
horizon. We would like to work with coordinates which are manifestly regular everywhere
except for the singularity at the origin r = 0 in (4.6), for we expect that the class of stress
tensors that are fluid dynamical in nature should be special from a general relativistic view-
point (we will shortly review why). In fact, we will show that the fluid dynamical stress
tensors give rise to regular black hole spacetimes as their holographic duals.

    One can motivate the special nature of fluid dynamical form for the stress tensor by the
following observation: consider the Fefferman-Graham form of the AdSd+1 metric (4.3). It
is well known that in order to find an asympotically AdSd+1 spacetime with a prescribed
boundary Bd, one has to give in addition to the metric g� on Bd another piece of data which
corresponds to the boundary stress tensor. Armed with g� and T� one can construct a bulk
solution order by order in a perturbative expansion in the Fefferman-Graham radial variable
z. To leading order the solution is simply

ds2  =  1   dz2 + g� + a zd T�                 dx� dx .  (4.8)
        z2

This scheme for constructing a bulk spacetime with prescribed boundary data is well devel-
oped in the formalism of holographic renormalization [99]. However, this scheme is not likely
to generically reproduce regular bulk spacetimes. To see why one just needs to a do a simple

  25Another useful way to think about the hydrodynamic description in gravity language is to view it as
the collective field theory of the lowest quasi-normal mode, the mode with vanishing frequency at zero
momentum, of the black hole geometry.

            27
degrees  of  freedom  counting.  A  traceless,  symmetric  stress  tensor  on  Bd  has  d(d+1)  -  1  degrees
                                                                                            2

of freedom. But the dynamical equations of motion are simply the conservation equations

(2.1) which are just d equations leading to a vastly underdetermined system when d > 2.

However, a fluid dynamical stress tensor is a special class of conserved stress tensors for it

is described by precisely d degrees of freedom, the temperature and velocity.26

In order to make regularity manifest, we will describe how to construct gravitational

black hole solutions dual to arbitrary fluid flows using a coordinate chart that is regular on

the future horizon.27 We work with a set of generalized Gaussian null coordinates which

are constructed with the aim of having the putative horizon located at some hypersurface

r(x�) = rH(x�).28 So as the starting point for our analysis we consider the boosted planar
Schwarzschild-AdSd+1 black hole solution:

             ds2 = -2 u� dx�dr - r2 f (b r) u� u dx�dx + r2 P� dx�dx ,                                (4.9)

where we have written the metric in ingoing Eddington-Finkelstein coordinates. We should
note that it is possible to recast (4.9) in a Weyl covariant form when the boundary metric
on Bd is curved � we have [69]:

ds2 = -2 u� dx� (dr + r A� dx�) + r2 (1 - f (b r)) u� u dx�dx + r2 g� dx�dx . (4.10)

    The main rationale behind switching to these Eddington-Finkelstein coordinates apart
from making issues of regularity more transparent, is that they provide a clear physical pic-
ture of the locally equilibrated fluid dynamical domains in the bulk geometry. The boundary
domains where local thermal equilibrium is attained in fact extend along ingoing radial null
geodesics into the bulk. So a given boundary domain corresponds to an entire tube of width
set by the scale of variation in the boundary, see Fig. 1 for an illustration. In the Eddington-
Finkelstein coordinates one just has to patch together these tubes to obtain a solution to
Einstein's equations and moreover this patching can be done order by order in boundary
derivatives, just as in fluid dynamics. We now proceed to outline a perturbation scheme
which allows us to construct the desired gravity solution dual to fluid dynamics.

    As the starting point consider the metric (4.9) with the constant parameter b and the
velocities i replaced by slowly varying functions b(x�), i(x�) of the boundary coordinates.

ds2 = -2 u�(x) dx� dr - r2 f (b(x) r) u�(x) u(x) dx� dx + r2 P� (x) dx� dx . (4.11)

Generically, such a metric (we will denote it by G(0)(b(x�), i(x�)) is not a solution to Ein-
stein's equations. Nevertheless it has two attractive features. Firstly, away from r = 0,
this deformed metric is everywhere non-singular. This pleasant feature is tied to our use of
Eddington-Finkelstein coordinates. Secondly, if all derivatives of the parameters b(x�) and

  26Similar arguments can be given if we want to consider fluids which carry conserved global charges.
  27For a discussion on the Fefferman-Graham coordinates and regularity see [100].
  28We will determine explicitly the location of the horizon after sketching the construction of the solution.

                                                28
Fig. 1: Penrose diagram of the uniform black brane and the causal structure of the spacetimes dual to

            fluid mechanics illustrating the tube structure. The dashed line in the second figure denotes
            the future event horizon, while the shaded tube indicates the region of spacetime over which
            the solution is well approximated by a tube of the uniform black brane.

i(x�) are small, G(0) is "tubewise" well approximated by a boosted black brane. Conse-
quently, for slowly varying functions b(x�), i(x�), it might seem intuitively plausible that

(4.11) is a good approximation to a true solution of Einstein's equations with a regular event

horizon. In [4] this intuition is shown to be correct, provided the functions b(x�) and i(x�)
obey a set of equations of motion, which turn out simply to be the equations of boundary

fluid dynamics.

Einstein's equations, when evaluated on the metric G(0), yield terms which involve deriva-

tives of the temperature and velocity fields in the boundary directions (i.e., (xi, v)  x�)
which we can organise order by order in a gradient expansion. Note that since G(0) is an

exact solution to Einstein's equations when these fields are constants, terms with no deriva-

tives are absent from this expansion. It is then possible to show that field theory derivatives

of either ln b(x�) or i(x�) always appear together with a factor of b. As a result, the con-
tribution of n derivative terms to the Einstein's equations is suppressed (relative to terms

with no derivatives) by a factor of (b/L)n  1/(T L)n. Here L is the length scale of varia-

tions of the temperature and velocity fields in the neighbourhood of a particular point, and

T is the temperature at that point. Therefore, provided L T  1, it is sensible to solve

Einstein's equations perturbatively in the number of field theory derivatives.29 Essentially

we are requiring that  u�       log  T
                        T        T
                           ,             O ()  1  (4.12)

  29Note that the variation in the radial direction, r, is never slow. Although we work order by order in
the field theory derivatives, we will always solve all differential equations in the r direction exactly. This
should be contrasted with the holographic renormalization group which is a perturbative expansion in the
Fefferman-Graham radial coordinate [99].

                                     29
where we introduce a book-keeping parameter  which keeps track of derivatives in the
boundary directions. It is useful to regard b and i as functions of the rescaled field theory
coordinates  x� where  is a formal parameter which we eventually set to unity. This way
every derivative of i or b produces a power of , consequently powers of  count the number
of derivatives.

4.4 The perturbative expansion in gravity

We now describe a procedure to solve Einstein's equations in a power series in . Consider

the metric30

              G = G(0)(i, b) +  G(1)(i, b) + 2 G(2)(i, b) + O 3 ,         (4.13)

where G(0) is the metric (4.11) and G(1), G(2) etc., are correction metrics that are yet to be
determined. We will see that perturbative solutions to the gravitational equations exist only
when the velocity and temperature fields obey certain equations of motion. These equations
are corrected order by order in the  expansion; this forces us to correct the velocity and
temperature fields themselves, order by order in this expansion. Consequently we set

              i = i(0) +  i(1) + O 2 ,      b = b(0) +  b(1) + O 2 ,      (4.14)

where i(m) and b(n) are all functions of  x�.
    In order to proceed with the calculation, it will be useful to fix a gauge. In [4] it was

convenient to work with the `background field' gauge

              Grr = 0 ,  Gr�  u� ,      Tr (G(0))-1G(n) = 0  n > 0.       (4.15)

One could equivalently work with a slightly different gauge choice [69]:

                         Grr = 0 ,          Gr� = u� .                    (4.16)

With this gauge choice it transpires that curves of x� = constant are in fact affinely parame-

terized null geodesics in the resulting spacetime, with the radial coordinate r being the affine

parameter. With the former gauge choice (4.15) of course x� = constant are null geodesics;

however, r is not an affine parameter for this geodesic congruence.

With this picture in place one can plug in the ansatz (4.13) and (4.14) into Einstein's

equations (4.2) and expand them order by order in . Let us imagine that we have solved

the perturbation theory to the (n - 1)th order, i.e., we have determined G(m) for m  n - 1,
and have determined the functions i(m) and b(m) for m  n - 2. Plugging the expansion
(4.13) into Einstein's equations, and extracting the coefficient of n, we obtain an equation

of the form

                         H G(0)(i(0), b(0)) G(n)(x�) = sn.                (4.17)

  30For convenience of notation we are dropping the spacetime indices in G(n). We also suppress the
dependence of b and i on x�.

                                        30
Here H is a linear differential operator of second order in the variable r alone. As G(n) is

already of order n, and since every boundary derivative appears with an additional power

of , H is an ultralocal operator in the field theory directions. In fact not only is H is a

differential operator only in the variable r independent of x�, but also its precise form at the
point x� depends only on the values of i(0) and b(0) at x�, and not on the derivatives of these

functions at that point. Furthermore, the operator H is independent of n; we have the same

homogeneous operator at every order in perturbation theory. This makes the perturbation

expansion in  ultra-local in the boundary directions; we can solve the equations point by

point on the boundary!

    The source term sn however is different at different orders in perturbation theory. It
is a local expression of nth order in boundary derivatives of i(0) and b(0), as well as of
(n - k)th order in i(k), b(k) for all k  n - 1. Note that i(n) and b(n) do not enter the nth

order equations as constant (derivative free) shifts of velocities and temperatures solve the

Einstein's equations.

The  gravitational equation        (4.17)  form a set   of  (d+1)(d+2)  equations.  It  is useful  to  split
                                                                   2

these into two classes of equations: (i) a class that determines the metric data we need,

comprising  of  d(d+1)  equations  which  we  view  as  dynamical  equations  and   (ii)  a  second  set  of
                    2

d equations which are essentially constraint equations.

Constraint equations: We will refer to those of the Einstein's equations that are of
first order in r derivatives as constraint equations. These are obtained by contracting the
equations with the one-form normal to the boundary

                                           EM(c) = EMN N                                             (4.18)

where for our considerations N = dr. Of these equations, those with legs along the boundary
direction are simply the equations of boundary energy momentum conservation:

                                           �T(n�- 1) = 0 .                                           (4.19)

Here T(n�- 1) is the boundary stress tensor dual the solution expanded up to O (n-1) and is a
local function of the temperature and velocity fields involving no more than n-1 derivatives.

Furthermore, it is conformally covariant and consequently it is a fluid dynamical stress tensor

with n - 1 derivatives.
    These constraint equations can be used to determine b(n-1) and i(n-1); this is essentially

solving the fluid dynamics equations at order O (n) in the gradient expansion assuming that

the solutions at preceding orders are known. There is a non-uniqueness in these solutions

given by the zero modes obtained by linearizing the equations of stress energy conservation
at zeroth order. These can be absorbed into a redefinition of the i(0), b(0), and do not
correspond to a physical non-uniqueness.

                                              31
Dynamical equations: The remaining constraint Err and the dynamical Einstein's equa-
tions E� can then be used to solve for the unknown function g(n). By exploiting the un-
derlying symmetries of the zeroth order solution, specifically the rotational symmetry in the
spatial sections on the boundary, SO(d-1), it is possible to decouple the system of equations
into a set of first order differential operators. Having performed this diagonalization of the
system of equations one has a formal solution of the form:

      G(n) = particular(sn) + homogeneous(H)                                     (4.20)

To determine the solution uniquely we need to prescribe boundary conditions: we impose that
our solution is normalizable so that the spacetime is asymptotically AdSd+1 and also demand
regularity at all r = 0. In particular, the solution should be regular at the hypersurface
b r = 1. It has been shown in [4] that for an arbitrary non-singular and appropriately
normalizable source sn encountered in perturbation theory, it is always possible to choose
these constants to ensure that G(n) is appropriately normalizable at r =  and non-singular
at all nonzero r. Furthermore, if the solution at order n - 1 is non-singular at all nonzero
r, it is guaranteed to produce a non-singular source at all nonzero r. Consequently, the
non-singularlity of sn follows inductively.31

4.5 Details of the long-wavelength perturbation expansion

We have described how to perturbatively construct solutions to (4.2) by working order by

order in boundary derivatives. We now briefly illustrate how to carry this out in practice to

first order in derivatives and refer the reader to the original references [4, 69] for the detailed

derivation of the results given herein.
    Consider the zeroth order metric G(0) given in (4.11). If we want to work to first order

in boundary derivatives, we can pick a point on the boundary x� = x�0 , which by exploiting
the Killing symmetries of the background can be chosen to be the origin. At x�0 we can use
the local scaling symmetry to set b(0) = 1 and pass to a local inertial frame so that i(0) = 0.
Expanding (4.11) to O () at this point we find

ds2(0) = 2 dv dr - r2 f (r) dv2 + r2 dxi dxi

-  2  i(0)  dxi  dr  -  2  i(0)  r2  (1  -  f (r))  dxi  dv  -  d  b(0)  dv2  ,  (4.21)
                                                                   rd-2

where we have introduced a short-hand i(0) = x� �i(0) and b(0) = x� �b(0) which are the
leading terms in the Taylor expansion of the velocity and temperature fields at x0� (taken to
be the origin).

    We now need to pick an ansatz for the metric correction at O (), G(1), which we wish

to determine. As mentioned earlier it is useful to exploit the SO(d - 1) spatial rotation

  31There is a slight subtlety which needs to be borne in mind here: the requirements above do not completely
fix G(n) since the differential operator H has some zero modes. These can however be fixed by appropriately

absorbing the zero modes into redefinition of the local temperature and velocity fields.

                                 32
symmetry at x�0 to decompose modes into various representations of this symmetry. Modes
of G(1) transforming under different representations decouple from each other by symmetry.

We have the following decomposition into SO(d - 1) irreps:

scalars:                                     Gv(1v), G(v1r),             G(ii1),

vectors:                                                           i                   (4.22)
tensors:
                                             G(v1i),
                                             Gi(j1)

We work sector by sector and solve the constraint and the dynamical Einstein's equations.
    In the scalar sector, we find that the constraint equations imply that

                                    d  1  1  ii(0)   =   v b(0)       ,                (4.23)
                                       -

while in the vector sector we have

                                       ib(0) = vi(0) .                                 (4.24)

These two equations are simply the equations of energy momentum conservation (2.1) at the
point x�0 . The remaining dynamical equations are to be solved for the functions appearing
in G(1) � we refer the reader to [4, 69] for the specifics and just record here the form of the

differential operator we obtain in various sectors:32

vector :                            Hd-1O    =   d        1      d       O
tensor :                                         dr      rd-1    dr

                                    H O d(d+1)   =   d   rd+1            f (r)  d   O  (4.25)
                                                     dr                         dr
                                              2

which as advertised earlier are simple differential operators in the radial variable alone and
clearly can be inverted to find the function O once the source sn is specified.

    The calculation can in principle be carried out to any desired order in the  expansion.
As we have discussed earlier the form of the differential operator (4.25) remains invariant in
the course of the perturbation expansion. What one needs to compute at any given order
are the source terms sn. In addition one has to always ensure that the lower order stress
tensor conservation equations are satisfied. For instance in order for the source terms which
appear in the determination of G(2) at second order to be ultra-local at our chosen boundary
point x0� we have to ensure that the first order fluid equations of motion are satisfied. This
is encapsulated in our discussion of the constraint equations in the bulk (4.19).

  32We have indexed the operator H by the representation label of the SO(d - 1) rotational symmetry. The
scalar sector involves some mixing between different fields and is slightly more involved, see [4, 69] for details.

                                                 33
5 Gravitational analysis: Metrics dual to fluids

We have thus far discussed how to solve to Einstein's equations order by order in boundary
derivatives. We now present the result for the general fluid dynamical metric up to second
order in boundary derivatives and then describe how one extracts the stress tensor quoted in
�3.4. Subsequently, we will analyze the physical properties of these solutions and argue that
they are regular black hole solutions with an event horizon. Following that we will discuss
how one can use the black hole nature of the solution to understand aspects of the fluid
dynamics such as the entropy current.

5.1 The gravitational dual to non-linear viscous fluid

We have described how one can consistently solve for the bulk metric in �4 � in particular,
in �4.5 we have given a sketch of how the perturbation scheme works. It turns out that the
bulk metric resulting from the explicit computation can schematically be cast into the form:

ds2 = GMN dXM dXN = -2 S(r, x) u�(x) dx� dr + � (r, x) dx� dx .  (5.1)

This was the form of the metric originally derived in [4], where the functions S(r, x) and
(r, x) are explicit functions of the radial coordinate r, whilst being given in terms of a
gradient expansion in the boundary directions x�. Note that the bulk metric is actually
given in the gauge (4.15). The expressions for the functions S(r, x) and (r, x) are rather
cumbersome and we will not record them here, but rather refer the interested reader to the
original source [4, 66]. Instead we will record the explicit metric below making manifest
the Weyl covariant structures, following [69] which makes for a more compact presentation.
Before we do that however, it is useful to understand the geometry in the somewhat simpler
form of the metric given above, since it captures much of the essential physical features.

    First of all, it is useful to realize that in the metric (5.1) lines of constant x� are radially
ingoing null geodesics. If the function S(r, x�) is gauge fixed to unity then in fact the radial
coordinate r is actually an affine parameter along this null congruence. One can visualize this
as follows: consider a null geodesic congruence i.e., a family of null geodesics with exactly
one geodesic passing through each point, in some region of an arbitrary spacetime. Let  be
a hypersurface that intersects each geodesic once. Let x� be coordinates on . Now ascribe
coordinates (, x�) to the point at an affine parameter distance  from , along the geodesic
through the point on  with coordinates x�. Hence the geodesics in the congruence are lines
of constant x�. In this chart, this metric takes the form

ds2 = -2 u�(x) d dx� + � (, x) dx� dx,                           (5.2)

where the geodesic equation implies that u� is independent of . It is convenient to generalize
slightly to allow for non-affine parametrization of the geodesics: let r be a parameter related
to  by d/dr = S(r, x). Then, in coordinates (r, x), the metric takes the form given in (5.1).
Note that  could be spacelike, timelike, or null. We shall take  to be timelike.

34
    The metric (5.1) has determinant -S2�u�u det , where � is the inverse of �,
where the indices are raised with the boundary metric; for (5.1) the induced metric on the

boundary Bd is simply                                 1
                                                      r2
                                          g�  = lim       � (r,  x)   .
                                                  r

Hence the metric and its inverse will be smooth if S, u� and � are smooth, with S = 0, �
invertible, and � u� timelike. These conditions are satisfied on, and outside, the horizons
of the solutions that we shall discuss below. Finally, note that the inverse metric,33 GMN ,

can be determined easily to be

Grr  =          1     ,         Gr =         S  u         ,      G        =  S2 u  u               -         ,
        -S2 u� u �                        -S2 u� u �                                 -S2 u� u      �

                                                                                                         (5.3)

using GMK GKN = MN .

Weyl covariant form of fluid metric: As remarked above the coordinates in which we
present the fluid metric (5.1) do not make explicit the Weyl covariant structures. An alternate
form of the metric was written down in general for asymptotically AdSd+1 spacetimes in [69]
which takes the form:

     ds2 = GMN dXM dXN = -2 u�(x) dx� (dr + V(r, x) dx ) + G� (r, x) dx� dx , (5.4)

where the fields V� and G� are functions of r and x� which admit an expansion in the
boundary derivatives. In the parameterization used in [69] one finds the metric functions are
given up to second order in derivatives as:

     V� = r A� - S� u - v1(b r) P� D

           + u�  1  r2   f  (b  r)  +  1  (1 - f (b r))          + v2(b r)    
                 2                     4                                      d-1

G� = r2 P� - �  + 2 (b r)2 g1(b r)                    1  �   +  g1(b  r)  �           -  g2(b  r)        P�
                                                      b                                             d-1

           - g3(b r)     T1�    +   1  T3�    +  2 T2�    + g4(b r) [T1� + T4�] .
                                    2

                                                                                                         (5.5)

where we are using the tensors defined earlier in (3.23) and also introduce the Schouten

tensor S� (a particular combination of curvature tensors) which is defined in (A.6). The

tensor G� is clearly transverse, since it is built out of operators that are orthogonal to the
                                             the relation (G-1)� G
velocity,  and it can be inverted via                                        =  P  �  .  We also note that the


coordinate chart used to write (5.1) is consistent with the bulk gauge choice (4.16). For

future reference we record the induced metric on the boundary in these coordinates

                                    g�    =  lim  1     G� - u(� V) ,                                    (5.6)
                                                  r2
                                             r

33Note that the `inverse d-metric' � is defined via �  = �.

                                                      35
which is crucially used to raise and lower the boundary indices (lowercase Greek indices).

The various functions appearing in the metric are given in terms of definite integrals

     g1(y) =         d       d-1  -  1
               y            (d    -  1)

     g2(y) = 2 y2      d            
                     y 2
                                      d 2 g1 ()2


     g3(y) = y2            d    d-2  -   1
                   y           (d    -   1)

     g4(y) = y2      d                                 1 + (d - 1)  g1() + 2 2 g1()         (5.7)
                   y  (d - 1)
                                            d  d-3

                                         1

     v1(y)  =    2                           d  3   -1
               yd-2                                 (d - 1)
                           d d-1

                       y

     v2(y)  =     1          d       1 -  ( - 1) g1 () - 2 (d - 1) d-1
               2 yd-2      y 2


               + 2 (d - 1) d - (d - 2)                  d 2 g1()2 .


The asymptotic behaviour of these functions gi(y) and vi(y) which are relevant for the stress
tensor computation can be found in [69].

5.2 The boundary stress tensor

Once the bulk black hole solution is determined it is straightforward to use the holographic

prescription of [95, 96] to compute the boundary stress tensor. To perform the computation

we regulate the asymptotically AdSd+1 spacetime at some cut-off hypersurface r = c and

consider the induced metric on this surface, which up to a scale factor involving c is our

boundary metric g�. The holographic stress tensor is given in terms of the extrinsic curva-

ture K� and metric data of this cut-off hypersurface. Denoting the unit outward normal to

the surface by n� we have

                                         K� = g� n                                          (5.8)

For example for asymptotically AdS5 spacetimes the prescription of [96] gives

T �  = lim     dc-2           K �  -  K  g�  -  (d  -  1)  g�  -  d  1  2  R�  -  1  R  g�  (5.9)
         c  16 GN(d+1)                                               -            2

where K� is the extrinsic curvature of the boundary. Implementing this procedure for the

metric (5.4) and utilizing the asymptotic form of the functions given in (5.7) we recover the

stress tensor quoted in (3.23) with the precise transport coefficients (3.25).

5.3 Event horizons

Having understood the geometric aspects of the coordinate chart employed for metrics dual
to arbitrary fluid flows in the boundary, we are now in a position to address our assertion

                                                36
that these metrics are in fact black hole spacetimes with regular event horizon. In general
determining the event horizon of a black hole spacetime requires that we know the entire
future evolution of the spacetime geometry. This is basically due to the definition of an event
horizon, which is teleological in nature.

    Formally one defines the event horizon of a given spacetime as follows: the future event
horizon H+ is the boundary of past set of future null infinity. This is the mathematical
way to capture the physical statement that the spacetime events inside the event horizon of
the black hole cannot communicate to the asymptotic region. It is important to note that
the future null infinity I + corresponds to where the future directed null geodesics in the
spacetime end and is in fact timelike for asymptotically AdS spacetimes. Since H+ is the
boundary of a causal set, it is a null surface which is in particular generated by null geodesics
in the spacetime. One can determine the event horizon by shooting null geodesics from the
interior of the spacetime and checking whether they make it out to I +. By fine tuning the
initial conditions of the geodesic one can zero onto H+. Alternately, if one knows the late
time generators of the event horizon, then one can evolve the geodesic equation backwards
with these generators as the future boundary condition.

    For the metrics dual to boundary fluid dynamics, we will make an important assumption:
since fluid dynamical evolution tends generically to smooth out inhomogeneities, we will
assume that the late time solution is one corresponding to global equilibrium wherein the
fluid settles down. Then at late times we have a clear idea of where the event horizon is
located � its location in the radial direction in the asymptotically AdSd+1 bulk spacetime is
specified by the value of the local temperature. Armed with this data one can in principle
evolve the null generators of the horizon backwards to construct the entire surface H+.34
However, it will turn out that in the long-wavelength approximation one can as usual work
order by order in the boundary derivative expansion and in fact determine the location of
the horizon.

    For the spacetime (5.1), let us suppose that the null hypersurface corresponding to H+
that we are after is given by the equation

                     SH(r, x) = 0 , with SH(r, x) = r - rH (x) .                                    (5.10)

As we are working in a derivative expansion and assuming that the dissipative fluid dynamics

drives  us  towards  global  equilibrium  with  a  local  temperature   T (x)  =      d   we  take
                                                                                  4 b(x)

                                              1        
                                             b(x)
                             rH (x)       =        +       k r(k)(x) .                              (5.11)

                                                      k=1

where r(k)(x) denote the corrections away from the late time hypersurface in the spacetime.

  34As has been recently discussed in the context of dynamical fluid flows [63] there are examples such as the
the Bjorken flow and the conformal soliton flow where despite the long wavelength approximation required
for fluid dynamics to be valid being upheld, one nevertheless has non-trivial late time boundary conditions
which change the nature of the event horizon.

                                                   37
By demanding that the hypersurface defined by (5.10) be null i.e.,

                       GAB ASH BSH = 0                              (5.12)

we can solve for the functions r(k)(x) order by order in the  expansion. In addition to the

location of the horizon we will also be interested in the normal vector to the event horizon

by A: by definition,

                       A = GAB BSH(r, x)                            (5.13)

which also has an  expansion. Using the explicit form of the metric (5.1) or (5.4) one
can easily write down the equation determining the location of the event horizon (5.12) to
arbitrary order in  explicitly. For instance in the simpler situation of the non-Weyl covariant
metric (5.1) we have the equation

0  =          1  �     1 - 2  S  u rH - 2 S2    -                   u u rH  rH  ,
      -S2 u� u

                                                                    (5.14)

which is actually an algebraic equation for the functions r(k) at any given order in  and
hence easy to solve. For the Weyl covariant metric (5.4), the horizon location is determined

by the equation [69]:  G-1 � �  = 2 u� � ,

                                                                    (5.15)

with

                       � = �rH + V�(rH(x), x) ,                     (5.16)

where we have left the powers of  implicit. In terms of � one can determine the components
of the normal vector to the horizon hypersurface as

                 A A = n� (� + �rH r) , with n� = u� - G-1 �  .     (5.17)

    Rather than illustrate the computation of the event horizon for the metrics (5.4) or (5.4)
we will just give the resulting answer of the computation, referring the reader to the original
derivation presented in [66, 69]. However, before doing so we would like to present a toy
model computation which illustrates the key features of the computation.

Toy model for event horizon detection: The general situation we are interested in has
dependence on all the boundary directions x� � a simpler situation to consider would be
to look at a case where we have dependence only on one variable, say time. Furthermore,
there is nothing really special about asymptotically AdS spacetimes for the detection of the
event horizon. One could just as readily have made similar arguments for asymptotically
flat spacetimes. As a result we will focus on a simple example of the Vaidya spacetime which
describes a spherically symmetric black hole with infalling null matter. As we are interested
in just the geometric properties of the spacetime, we will just focus on the metric and not
worry about solving Einstein's equations.

                       38
Consider the Vaidya spacetime, whose metric is given as:

                ds2 = -            1  -  2  m(v)     dv2 + 2 dv dr + r2 d2 .            (5.18)
                                             r

We want to determine the location of the horizon, which by spherical symmetry has to lie
on the locus r = r(v). The normal one-form to this surface is clearly just n = dr - r dv.
Demanding that this be null gives us a differential equation for the null surface

                                   r(v) = 2 m(v) + 2 r(v) r(v) ,                        (5.19)

which is the analog of (5.14) for the Vaidya metric (5.18). The equation we have at hand

is a first order ODE for the function r(v), solving which we would determine the location

of the horizon non-locally in terms of m(v). This would of course be the case for a generic

function m(v).

However, to make contact with our earlier discussion, suppose we assume that the mass

function m(v) is slowly varying and moreover that it asymptotes to a constant for late times,

i.e.,

       m (v) = O () , m m� = O 2 etc.,                          and  lim   m(v)  =  m0  (5.20)

                                                                     v

then we can solve (5.19) in a derivative expansion. Consider the ansatz,

                                                                                        (5.21)

                                r(v) = 2 m(v) + k r(k)(v)

                                                                k=1

which leads to the solution

                r(1) = 8 m m , r(2) = 64 m m 2 + 32 m� m2, etc..                        (5.22)

Thus, by invoking the slow variation ansatz we obtain a local expression for the location of
the horizon in a derivative expansion.

Horizon location for fluid metrics: An analogous analysis can be carried out for the
the equation (5.15) � we quote here just the final result (once again dropping  for brevity)

                rH (x)  =     1    +  b(x)    1   + 2   + 3 R                           (5.23)
                             b(x)

with                                    2 (d2 + d - 4)           2 v2(1)
                                      d2 (d - 1) (d - 2)        d (d - 1)
                             1  =                           -

                             2  =     -2   d+2    2)                                    (5.24)
                                          d (d -

                             3  =     -d  (d  -   1  (d  -  2)
                                                 1)

R here is the Weyl covariant boundary Ricci scalar, which is defined in (A.4). This establishes
the claim made in the �1 that spacetimes dual to hydrodynamical evolution in the boundary
field theory are regular black hole spacetimes. See Fig. 2 for an illustration of the event
horizon in the spacetime.

                                                  39
Fig. 2: The event horizon r = rH (x�) sketched as a function of the time t and one of the spatial

            coordinates x (the other two spatial coordinates are suppressed).

5.4 Boundary entropy current

As we discussed in �2.2 the flow of a dissipative fluid is characterized by entropy production.
Given that we have constructed a gravitational dual which is a black hole it is natural to
ask whether one can associate the entropy of the fluid with a geometric feature in the bulk
spacetime. There is a natural object which one is tempted to use for this purpose, which is
the area of the event horizon in the bulk geometry.

    In general when we consider deviations from equilibrium it is a-priori not clear that
there should exist an unambiguous notion of entropy. In fact, since all we require of the
entropy current is to satisfy the second law (2.20), we can use any local function having
positive divergence to characterize the irreversibility of the fluid dynamical flow. The only
constraint we would demand on this putative Boltzmann H-function is that it agrees with the
thermodynamic notion of entropy in global equilibrium. For a stationary black hole, which
corresponds to global thermal equilibrium, the area of the event horizon does indeed capture

                                                         40
the entropy of the dual field theory. It seems therefore natural to associate the entropy of
the field theory with the area of the event horizon. This actually turns out to be a bit more
subtle as discussed recently in [63]� we will return to this point after providing a sketch of
the argument given in [66] for constructing an entropy current dual to fluid flows using event
horizon data.35

Entropy current from geometry: We have established that the spacetimes dual to

boundary fluid dynamics are in fact black hole geometries with a regular future event horizon
H+. Given a black hole spacetime one can associate an entropy with the area of the event

horizon, which is the usual Bekenstein-Hawking entropy of the back hole. However, the field

theory lives on the boundary of the spacetime and we would like to define an entropy current

directly in the field theory. To this end, consider spatial sections of the event horizon, which
are co-dimension two surfaces in the spacetime, which we label as Hv+. We are working
in a coordinate chart where the coordinates i for i = {1, � � � d - 1} define a chart on the

spatial section and we use as affine parameter, the boundary coordinate v, to propagate these
surfaces forward along the horizon generator A. On the surface Hv+ it is natural to define
an area (d - 1)-form, whose integral gives the area of the spatial section. From the area

theorem for black holes, it follows that the area of the spatial sections will be non-decreasing
with v.36

    Once we have a geometric object such as the area-form on the horizon, we can pull it

back to the boundary and have a candidate entropy function, for the pull-back too will

have non-negative divergence. The only issue is the precise manner in which we implement

the pull-back. It turns out to be natural to pull-back the area form on the horizon using

radially ingoing null geodesics, which provide an isomorphism between the spatial sections
on the boundary and the corresponding Hv+ on H+. This procedure was described in detail
in [66] and was used there to construct a boundary entropy current explicitly. One can give

a compact formula for the boundary entropy current based on this discussion as follows. Let
us suppose that the induced metric on the spatial slices of the horizon Hv+ is given by hij
and as usual the boundary metric is g�. Under the split of the future horizons into spatial
sections Hv+ we can also split the vector n� defined in (5.17) which essentially gives us the
projection of the null generator of the event horizon into the boundary directions. Armed

with this set of geometric data we define an entropy current

JS� =      1         detd-1 h  n�                                                 (5.25)
       4 GN(d+1)  nv - det g

which implements the pull-back procedure from the event horizon to the boundary.

  35The rationale behind postponing the discussion of the subtleties is that the event horizon serves to
illustrate the general idea of defining a boundary entropy current; it is trivial to generalize the construction

to other quasi-local horizons.
  36We assume that the null energy condition is satisfied. This is clearly true of the lagrangian (4.1), but

we will demand the same to be true for the general discussion (6.1).

                  41
Boundary entropy current: The entropy current in d dimensions has to be a Weyl
covariant vector of weight d. This follows from the fact that the entropy density scales like the
inverse spatial volume, the total entropy being dimensionless, and the scaling of the velocity
field given by(3.2). In [84] the general constraints on entropy currents were analyzed in the
Weyl covariant formalism and a particular entropy current for four dimensional CFTs was
constructed. This analysis was slightly generalized in [66] to argue for a five parameter family
of fluid dynamical entropy currents in four dimensional CFTs. A similar analysis was carried
out in arbitrary dimensions in [69], who found a four parameter family of hydrodynamical
entropy currents. The extra parameter which appears in d = 4 is related to the fact that one
can have pseudo-vector contributions to the entropy current involving � defined in (2.16).
In general d dimensions the entropy current takes the form:37

       JS� = s u� + s b2 u� A1   + A2   + A3 R                                             (5.26)
             + s b2 B1 D� + B2 D� + � � �

where s is the entropy density and A1,2,3, B1,2 are arbitrary numerical coefficients. Requiring
positivity of the divergence one finds a single linear relation between two of the coefficients:

                                         B1 + 2 A3 = 0 .                                   (5.27)

    The gravitational analysis described above leads to a specific entropy current, with the
parameters fixed by the geometric data encoded in the metric (5.4). The essential data is
captured the entropy density, which in general is given by the Bekenstein-Hawking formula
in terms of the area of the event horizon38

                     s=               1       1    ,  b=             d  .                  (5.28)
                                  4 GN(d+1)  bd-1                  4 T

The coefficients appearing in (5.26) are given in terms of the numerical (dimension) depen-

dent constants satisfying (5.27)

A1     =  2   (d  +  2)           -   1  g2(1)  +  2  v2(1)     ,
          d2                          2            d
                                                                                           (5.29)
              1                                           2                         1
A2     =  -  2d   ,               B1  =  -2 A3   =    d (d - 2)    ,       B2  =  d-2  .

Furthermore, it is possible to show that one can write the divergence of this gravitational
entropy current as

D�JS�  =  2       �  +            1     d    (1  + A1 d)     -        u D�        2        (5.30)
          T                       2   4 T
                                                                                   +��� ,

  37The contribution from the pseudo-vector in four dimensions takes the form C1 s b � + C2 s b2 u D�.
The positivity condition on the divergence of the entropy current demands C1 + C2 = 0.

  38As discussed above in the situations where the temporal variation is suitably slow the ateleological
behaviour of the event horizon doesn't play an important role. Furthermore, the various quasi-local horizons
are `sufficiently near' the actual event horizon which makes it possible to use the area of the event horizon
for our purposes.

                                                 42
which is accurate up to third order in the derivative expansion and clearly satisfies the
requirement of non-negative divergence to that order. We have recast this expression purely
in terms of fluid dynamical variables and it generalizes the result for viscous relativistic fluids
(2.21).

Event horizon vs. quasi-local horizons: We now turn briefly to the subtlety mentioned
at the beginning of this sub-section with regard to using the area of the event horizon for
capturing the entropy of the dual field theory in situations out of global equilibrium. A key
feature of the event horizon is its teleological nature, i.e., the fact that one needs to know
the entire future evolution of the spacetime in order to determine its location. This aspect of
event horizons generically implies that one typically may encounter a horizon in the bulk even
before we perturb the system � the event horizon grows in anticipation of the perturbation
one is about to impart. Associating an entropy current with the event horizon as a result
leads to a non-local and acausal definition of entropy as has been recently noted in [101]
(cf., [63]). From an underlying statistical description, we would like however to define an
entropy current a la Boltzmann, a local H-function which is defined purely based on the local
dynamics of the fluid, with no recourse to late time boundary conditions. Moreover, there
is a simple hydrodynamic flow on Rd-1,1, the conformal soliton flow [53], where it has been
shown that the event horizon area does not capture the entropy of the dual field theory [63].
Based on the latter analysis, it appears that in in certain dynamical situations one should
use the area of apparent horizons (more precisely dynamical horizons), to define the entropy
current.39 However, this statement glosses over certain subtleties involved in defining such
quasi-local horizons40 � for an account of the issues involved we refer the reader to [63].

6 Generalizations of the fluid-gravity correspondence

In �4 and �5 we have discussed how one can construct gravitational solutions dual to fluid
dynamics concentrating just on energy-momentum flow. One of the advantages of focussing
on the stress tensor T � is that in the holographic context one deals purely with gravitational
dynamics in AdSd+1. This allows for an universal description; the Lagrangian (4.1) is a
consistent truncation of the bulk string theory in the AdS/CFT context (all matter field
interact at best quadratically with the gravitational field). Nevertheless, one can incorporate
other fields into the fluid-gravity correspondence and by now there is a large body of literature
exploring these issues as discussed at the end of �1. We will describe the key features of
these investigations using an abstract model and suggest some future generalizations.

  39Another piece of evidence in favour of quasi-local horizons comes from the analysis of holographic
entanglement entropy (for specified regions on the boundary) in time dependent states of the dual field
theory, see the discussion in [102].

  40As explained in [63] we use the term apparent horizon to denote a co-dimension one surface in the
spacetime, which in conventional general relativity literature would correspond to a marginally outer trapped
tube.

                                                         43
6.1 Fluid-gravity and the inclusion of matter

Consider a situation where we have a gravitational action which is described by the Einstein-
Hilbert action with negative cosmological constant coupled to some matter fields which we
collectively denote as . To be precise,

Sbulk  =       1                                                    (6.1)
          16 GN(d+1)  dd+1x -G (R - 2 ) + Lmatter (, GMN )

where we have included metric contributions into the matter Lagrangian explicitly to allow

for situations where we consider higher derivative theories of gravity (say for example the
Gauss-Bonnet term in d  4 as discussed in [79]).

    We will assume that the action (6.1) admits stationary asymptotically AdSd+1 black
hole solutions41 which correspond to global thermal equilibrium, which by picking suitable
coordinates we can write as42

ds2 = -2 S(r, Q) u� dx� dr - r2 V(r, Q) u� u dx� dx + r2 P� dx� dx  (6.2)
  = (r, u�, Q)

where we have once again resorted to the ingoing Eddington-Finkelstein coordinates. The
coordinate x� as before span the boundary directions with � = {0, � � � , d - 1}. Furthermore,

we assume that we have translational invariance in the spatial directions which we have

exploited to boost the black hole solution so as to allow for the velocity field. This of course

requires that the matter field  supporting the black hole to respect the symmetries of the

metric. We have captured all the parameters describing the black hole into a single variable

Q, which enters into the metric and the matter field and corresponds to all the physical

charges we wish to ascribe to the geometry, such as temperature T , Maxwell charges qI
(or equivalently chemical potentials �I), etc.. Depending on the boundary conditions on
the matter field  we would find ourselves working in the canonical or the grand canonical
ensemble.43 It is possible to relax some of the assumptions described above at the expense

of complicating the discussion.

    To obtain a geometry dual to fluid dynamics we want to promote the parameters of the

background to fields as in conventional collective coordinate quantization. In order to do

so we need to identify the full set of zero-modes. It is worthwhile to pause to take stock of

some of the examples that have been discussed in the literature to orient ourselves:

  41The general scheme we describe below is not restricted to asymptotically AdS spacetimes. The only
reason to focus on these cases is the gauge-gravity duality which allows us to relate the bulk gravity dynamics
to that of a boundary field theory and in particular allows us via the holographic renormalization scheme to
extract a boundary stress tensor. One can construct inhomogeneous dynamical black holes using the slow
variation ansatz for any desired asymptopia (including asymptotically flat spacetimes). We will discuss an
example with different asymptopia in �6.2.

  42In the following discussion we eschew the use of the Weyl covariant form since our disucssion would also
be applicable to non-conformal fluids.

  43Recall that for charged black holes which corresponds to the situation where  is a bulk Maxwell field,
the grand canonical ensemble corresponds to non-zero value for the scalar potential A0 which is the boundary
chemical potential �.

                      44
1. In the forced fluid dynamics discussed in [70],  is just the dilaton and doesn't in-
   troduce new conserved quantities. So the parameter Q is just the temperature of the
   Schwarzschild-AdS black hole.

2. For the U(1)R-charged fluids discussed by [71, 72, 73] one has  to be the bulk Maxwell
   field which gives rise to an extra parameter, q, corresponding to the black hole charge.

3. The recent analysis of [74] incorporates three U(1) R-charges in AdS5. The matter con-
   tent of the gravitation theory comprises of three Maxwell fields and three bulk scalars.
   The black holes are described by four parameters, three charges and a temperature,
   collected here into Q in addition to the velocity field.44

4. One can also consider more exotic situations involving phase transitions. For instance
   in the Abelian-Higgs model coupled to gravity in AdS4 one has novel scalar hair black
   hole solutions [103]. Here  comprises of bulk Maxwell field and a charged scalar
   field. The set of parameters Q depends on which sector of the theory one considers
   since the bulk description involves non-trivial phase structure. In the U(1) symmetric
   phase Q just comprises of the temperature and chemical potential, whilst in the phase
   with broken U(1), one also has to incorporate the Goldstone mode. The latter phase
   gives rise to superfluid dynamics with a Landau two-fluid description. This has been
   discussed at linearized level in [104, 105] (see also [106]) and can indeed be incorporated
   into the fluid-gravity correspondence [107] (albeit with some effort since the background
   solutions are only known numerically).

    Having identified the set of parameters Q for a given example, we are in a position to
promote them to fields depending on the coordinates x and proceed to solve the equations of
motion (6.1) order by order in a derivative expansion. As described extensively above, this
involves identifying two pieces of information. The first is to determine the linear operator
H that acts on the correction terms to the metric. This operator by virtue of the Killing
symmetries in the background spacetime (which we assume) and matter fields (6.2) is just a
second order ordinary differential operator involving r. The second part involves identifying
the source sn which involves a bit of work at each order. Schematically, if we promote
Q  Q(x) and u�  u�(x) and work by expanding the solution (6.2) in the variations about
the background value. Specifically, consider

u� = u(�0) + u�(x) = u�(0) +  x u�(x) + O 2 ,  (6.3)
Q = Q(0) + Q =  Q(x) +  x� �Q(0) + O 2 .

For simplicity of discussion consider backgrounds which are stationary, so that by passing to
the local inertial frame we can always choose u(�0) = -�v and ui(1) = x� �i as before using

  44Unlike the uncharged case discussed in �5, for the fluid solutions dual to gravity which have been
constructed so far the issue of regularity is not clear; all the analyses so far do not demand regularity of the
Maxwell potential on the future horizon.

45
(4.7). Plugging these expansions into the metric we obtain the leading terms that contribute
to the sources. Using

            S(r, Q(x))      = S(r, Q(0)) +           S(r, Q)           Q                            (6.4)
                                                        Q
                                                               Q=Q(0)

we obtain the leading order expansion of the background metric and matter fields

ds2 = 2 S(r, Q) dv dr - r2 V(r, Q) dv2 + r2 ij dxi dxj

     +2  S  Q    dv  dr  -  2  S  i      dxi  dr  -  r2  V  Q  dv2  -  2  r2  i  (1  -  V )dxi  dv
         Q                                               Q

  =  (r,  Q(0))  +       u     +            Q                                                       (6.5)
                    u                    Q

which can then be used to solve for the higher order corrections to the metric G(k) and matter
fields (k). This has been carried out for a wide class of models and we refer the reader to
the original literature described at the end of �1 for details of the construction in the specific
cases.

Universality of transport coefficients: One of the interesting results arising from the
explorations so far concerns the universality of transport coefficients in gravity duals. As
is well known for two derivative gravity theories dual to boundary fluid dynamics, one has
the famous ratio [19] of shear viscosity to entropy density saturating the conjectured bound
/s  1/4. This can in fact be derived directly from the abstract discussion above, for
the backgrounds (6.2) which respect spatial translational symmetry in global equilibrium for
asymptotically AdSd+1 spacetimes [107, 108].

    It is interesting to ask whether the higher order transport coefficients exhibit similar
properties. Based on the general analysis of gravity coupled to scalars and Maxwell fields
and assuming that the theory doesn't exhibit any phase transitions (such as spontaneously
Higgsing of the bulk gauge field), it was shown in [108] that

                                         4 1 + 2 = 2                                                (6.6)

which is of course satisfied by (3.25).

6.2 Non-relativistic fluids from gravity

We have concentrated thus far on the dynamics of relativistic conformal fluids and con-
structed holographic duals for them. We now briefly comment on deriving the dynamics of
non-relativistic fluids from gravitational description. There are essentially two approaches
taken in the literature so far: in [81] gravity duals were obtained by taking a the non-
relativistic limit of the relativistic system, while in [80] conformal non-relativistic fluids were
discussed in the context of Galilean holography.

                                              46
Non-relativistic ideal hydrodynamics is described by the continuity equation,

                                    tnr + i nr vi = 0,                                       (6.7)

together with the equation of momentum conservation, (here i = 1, . . . , d)

   t(nr vi) + jij = 0,                               ij = nr vi vj + ij Pnr ,                (6.8)

and the equation of energy conservation,

t  nr  +  1                 nr  v2    + i ji = 0,         ji  =   1  (nr  +  Pnr) v2  vi  .  (6.9)
          2                                                       2

where v2 = vi vi. Here nr is the particle number density and Pnr, nr is the pressure and
energy density of the non-relativistic system under consideration and we use vi to denote the
non-relativistic velocity. These equations can be derived from the relativistic stress tensor
(2.2) by writing the conservation equation (2.1) in light-cone coordinates and demanding that
the fluid variables be independent of one of the light-cone directions. Using the light-cone
version of (2.1)

+T ++ + iT +i = 0 ,                 +T +i + jT ij = 0 ,              +T +- + iT -i = 0,      (6.10)

we can map the relativistic system in d dimensions into the non-relativistic equations in d-2
spatial directions with the following identifications: T ++ is identified with the mass density,
T +i with the mass flux (which is equal to the momentum density), T ij with the stress tensor,
T +- with the energy density, and T -i with the energy flux,

                            T ++ = nr, T +i = nr vi, T ij = ij ,

                            T  +-  =  nr  +   1  nr  v2,      T -i = ji.                     (6.11)
                                              2

    It is now easy to convince oneself based on (6.11) that the precise mapping between
relativistic and non-relativistic hydrodynamic variables is

          u+ =                        1      nr      ,       ui = u+ vi,
                                      2   nr + Pnr         = 2 nr + Pnr.

          P = Pnr ,                                                                          (6.12)

The component of the relativistic velocity u- can be determined using the normalization

condition u� u� = -1 to be

                                    u-  =  1      1  +    u+  v2  .                          (6.13)
                                           2     u+

    This maps makes it clear that the transport coefficients of the non-relativistic theory
are inherited from the parent relativistic hydrodynamics. In this description it is clear that
non-relativistic fluids with holographic duals will saturate the conjectured viscosity bound

                                                 47
/s = 1/4, which was verified explicitly in [109, 110]. Furthermore, it is also possible to
use this light-cone reduction to infer the heat conductivity of the non-relativistic fluid:

                                    nr  =  2  nr  nr +   Pnr  .                                       (6.14)
                                                    nr   T

which can be rephased as the statement that the Prandtl number of the fluid is unity. We

recall that the Prandtl number is defined as the ratio of the kinematic viscosity nr and the

thermal diffusivity nr,                           nr
                                                  nr
                                        Pr    =       ,                                               (6.15)

where                               nr                       nr
                                    nr                      nr cp
                              nr =         ,      nr     =         ,                                  (6.16)

where cp is the specific heat at constant pressure.

   The general idea of using slow variation in certain directions to construct inhomogeneous

dynamical black hole spacetimes is of course not restricted to asymptotically AdS spacetimes

and one can exploit this scheme to construct new solutions with different asymptotics. For

general asymptotics one does not recover any interesting boundary dynamics. However, in

recent years we have seen interesting generalizations of the AdS/CFT correspondence, such
as the holographic duals for field theories with non-relativistic Schr�odinger symmetry as
originally discussed in [111, 112] and later embedded into string theory in [109, 110, 113]. In

these examples one has spacetimes with non-trivial asymptotic structure and the dual field
theory is a non-local deformation of a relativistic superconformal field theory such as N = 4

SYM.

    In [80] the holographic duals for fluids with non-relativistic conformal symmetry i.e.,
Schr�odinger invariance was constructed. In this case one can achieve the holographic dual in
two equivalent ways: either by implementing the general procedure outlined in the lectures

(taking into account the reduced symmetries of the problem) or equivalently by exploiting a

specific duality transformation in string theory, the so called Null Melvin Twist [114] or the

TsT transformation [113]. To be specific, [80] constructed fluid dynamical solutions for the

five-dimensional effective action involving a scalar field  and a massive vector AM

S  =       1     d5x-G     R  -  4  (M  )(M   )   -      1  e-8/3  FM  N  F  M  N  -  4  AM AM  -  V  ()  ,
       16 GN(5)                  3                       4

                                                                                                      (6.17)

where

                                 V () = 4 e2/3(e2 - 4) ,                                              (6.18)

which asymptote to the Schr5 spacetime,

                 ds2 = r2  -2 dx+ dx- - 2 r2 (dx+)2 + dx22                   +  dr2   .               (6.19)
                                                                                r2

    Consider the general form of the fluid dynamical metrics in AdS5 given by (5.1) with
d = 4. We introduce light cone coordinates x� on the boundary directions. Restricting to

                                              48
configurations which have - as an isometry, after a TsT transformation on the metric (5.1)
we get a new metric of the form

      ds2E  =  e-  2    -2 u� S dx� dr +   AB  -    A B       dXA dXB  ,
                   3                               1 + --

      A = e2 A dXA,

      e2    =  1    1   ,                                                 (6.20)
                  + --

with

                           A = A- - u- S Ar .                             (6.21)

The TsT transform converts the asymptotically AdS5 spacetime (5.1) to an asymptotically
Schr5 spacetime, which depends on the paramters b, , ui which are arbitrary functions of
(x+, x). The relativistic velocity field u� in fact descends naturally into a non-relativistic

velocity field vi via the map

                        u+ = ,  ui =   vi  +   1   i(b  )  .              (6.22)
                                              4 2

which can be inferred from the light-cone reduction of the stress tensor [80]. In the field
theory description b is related to the temperture, while  sets the chemical potential for the
non-relativistic particle number.

    Conformal non-relativistic fluids with Schr�odinger symmetry are in general compressible;
this follows from the fact that the energy density is related to the pressure 2 nr = d Pnr
through the equation of state (which in turn follows from scale invariance). To make contact
with the usual studies of incompressible Navier-Stokes equations we need to ensure that we
can decouple the fluctuations in the density. This can be achieved by looking at low frequency
modes which do not excite the propagating sound mode in a hydrodynamic system, i.e., by
focussing on the shear mode. In fact, this limit was discussed recently in the context of the
fluid-gravity correspondence in [81] (see also [115, 116] for closely related results), where the
authors showed that starting from a parent relativistic conformal fluid dynamical system
one can recover incompressible Navier-Stokes equations in a suitable scaling limit. This
scaling limit reveals an interesting structure in the fluid equations � they are scale invariant
under a new scaling symmetry, which is the Galilean conformal algebra discussed recently in
[117]. This symmetry is different from the Schr�odinger symmetry enjoyed by the conformal
non-relativistic fluids discussed above (see also [118], [119]).

    One can view these two constructions as follows: given a relativistic theory, in particular
relativistic fluid dynamics, one can attain a non-relativistic limit either by (i) taking the
speed of light to infinity or (ii) by a light-cone reduction. The former procedure is related
to contracting the Poincar�e algebra to the Galilean algebra and when implemented on the
relativistic Navier-Stokes equations leads to the incompressible non-relativistic Navier-Stokes
fluid of [81]. The latter procedure of light-cone reduction converts d dimensional relativistic

                                       49
fluid dynamics into a d - 2 spatial dimensional non-relativistic fluid dynamics. Since one
requires a null vector to reduce on the light-cone, we end up losing an effective dimension in
our field theoretic description.

7 Discussion

In the course of these lectures we have discussed the essential features which relate the
physics of inhomogeneous, dynamical, black hole solutions of general relativity in asymptot-
ically AdS spacetimes, to fluid dynamics of strongly coupled superconformal field theories
living on the boundary of these AdS geometries. In particular, given any solution to the
relativistic Navier-Stokes equations and their non-linear generalizations (with the strong cou-
pling values of the transport coefficients), one can construct an asymptotically AdS black
hole solution. Alternately, the general construction described here can be viewed as a deriva-
tion of the hydrodynamic stress tensor of the dual superconformal field theories. While we
have discussed the construction to second order in derivatives, it is clear that the general con-
struction can in principle be extended to arbitrary orders in the gradient expansion (albeit
with increasing computational complexity in evaluating the source terms).

    We have also described how one can use the geometric description to understand the field
theory entropy and constructed a specific gravitational entropy current. An important issue
which we have briefly discussed concerns the geometric description of entropy and subtleties
associated with identifying the entropy with the area of the event horizon. While it seems
reasonable to associate the area of the event horizon to the field theory entropy in situations
where one has slow variations, it seems clear that this cannot be true in general as exemplified
by the conformal soliton flow described in [63].

    Furthermore, we have reviewed various generalizations of the correspondence over the
past year or so which have led to interesting new insights into forced fluid dynamics and
charge transport, etc.. These provide an interesting arena for further exploration � in princi-
ple it should be possible to derive the complete stress tensor and charge currents for N = 4
SYM up to two derivatives incorporating the three U(1) R-charge and angular momentum
chemical potential. In addition, it is clear that there are many interesting directions that
can be tackled within this framework, most notably the issues which were raised in �1 as
part of the motivation for the correspondence.

    One issue we have not touched upon in these lectures is the relation of the fluid-gravity
correspondence to the membrane paradigm [9]. Both purport to identify the dynamics of
black holes with hydrodynamics, and indeed the correspondence offers a important new per-
spective on this issue [120].45 Since in the fluid-gravity correspondence the entire spacetime
dynamics is mapped unambiguously into the boundary fluid dynamics, it is natural to argue
that the correspondence in fact implements the ideas inherent in the membrane paradigm,

  45An earlier discussion of the membrane paradigm in the context of hydrodynamics in AdS/CFT can be
found in [33]. Also see [121] for a recent discussion of the membrane paradigm in the holographic context.

                                                         50
albeit with a new wrinkle: the membrane is not located at the stretched horizon, but rather
at the boundary of the spacetime. Despite its location, this `membrane at the end of the
universe' faithfully captures the entire bulk spacetime dynamics and implements the mem-
brane paradigm holographically, as is clear from the fact that we not only recover the stress
tensor of the fluid, but also a particular gravitational entropy current. Note that in the
conventional membrane paradigm, the dynamics of the stretched horizon only captures the
physics of the region behind the black hole horizon and not of the entire spacetime. One
can of course use the AdS/CFT correspondence to interpolate between these two extreme
descriptions [122]: if one so wishes, it is possible to define a fiducial membrane at some other
radial location (and in particular on the stretched horizon) and identify the fluid dynamics
on this surface. The dynamics on this surface is related to the boundary fluid dynamics by
an appropriate flow equation which can be derived from the bulk gravitation equations using
techniques analogous to the holographic renormalization group.

    Finally, we should mention recent investigations of gravitational duals of field theories
perturbed away from equilibrium [101, 123]. As we have emphasized the hydrodynamic
behaviour comes into play only when the field theory achieves local thermal equilibrium.
In general, large perturbations will evolve outside the fluid regime, till such a time the
system thermalizes and achieves local equilibrium. Correspondingly, in the dual gravity
description, black hole formation is outside the long-wavelength hydrodynamic regime. The
remarkable aspect of the recent discussion of [123] is that the system tends to "thermalize"
rapidly � in effect the hydrodynamic description takes over almost instantaneously after the
perturbation is switched off.46 It would be interesting to understand this passage to local
thermal equilibrium for a generic perturbation in a strongly coupled field theory in greater
detail.

Acknowledgements

It is a pleasure to thank my collaborators, Sayantani Bhattacharyya, Veronika Hubeny,
R. Loganayagam, Gautum Mandal, Shiraz Minwalla, Takeshi Morita, Harvey Reall, Simon
Ross, Dam Son, Ethan Thompson and Mark Van Raamsdonk for wonderful collaborations
on various aspects of fluid dynamics. I would also like to thank the students of the CERN
Winter school for their enthusiasm and detailed questions. It is furthermore a great pleasure
to the organizers, especially Angel Uranga for putting together an excellent winter school. I
would like to thank CERN and KITP for their hospitality. This work is supported in part
by STFC Rolling grant and by the National Science Foundation under the Grant No. NSF
PHY05-51164.

  46To be sure, this is a statement that the one point functions display thermal behaviour at time-scales
much shorter than that set by the thermal wavelength. Furthermore, this statement is seen to hold only for
small amplitudes of the perturbation.

                                                         51
A Weyl covariant curvature tensors

One can define a curvature associated with the Weyl covariant derivative by the usual pro-
cedure of evaluating the commutator between two covariant derivatives. Defining a field
strength for the Weyl connection

                                F� = �A - A�                                       (A.1)

we find a Riemann curvature tensor R�:

            R� = R� + 4 [�g][]          A   +  AA  -        A2  g   - F� g         (A.2)
                                                             2

These two tensors are in an appropriate sense Weyl invariant; it is not hard to check from
the definitions that F� = F� and R� = R�. It should be borne in mind that the
Weyl covariant Riemann tensor defined above (A.2) has different symmetry properties from
the conventional Riemann tensor. Most importantly, it is not anti-symmetric under the
exchange of the last two indices. For example,

                             R� + R� = -2 F� g                                     (A.3)
                             R� - R� = [�g][] F - F� g + F g�
            R� V  V  - R� V  V  = -F� V  V

    With the basic definitions (A.1) and (A.2) in place we can proceed to define analogous
expressions for various other tensors often encountered in differential geometry, such as the
Ricci tensor, Ricci scalar:

   R�  R�  = R� - (d - 2) �A + A�A - A2g� - g�A - F� = R� (A.4)
     R  R = R - 2(d - 1)A + (d - 2)(d - 1)A2 = e-2R .

In addition it is also worth noting that the conformal tensors of the underlying spacetime
manifold appear as a subset of conformal observables in hydrodynamics. These conformal
tensors are the Weyl-covariant tensors that are independent of the background fluid velocity,
for we have already accounted for the terms involving velocity derivatives explicity above. A
well known example of this class of operators is the Weyl curvature C� which is the trace
free part of the Riemann tensor. In d  3 it is given as

               C�  R� + 4 [�g][]S = C� - F� g = e2 C�                              (A.5)

where we introduced the Schouten tensor S� is defined as47

S�    d  1  2  R�  -   Rg�      = S� -  �A  +  A�A  -       A2  g�  -  F�   =  S�  (A.6)
         -            2(d - 1)                               2         d-2

                                        52
    From equation (A.5), it is clear that C� = C� + F�g is clearly a conformal
tensor. Such an analysis can in principle be repeated for the other known conformal tensors
in arbitrary dimensions.

    The Weyl Tensor C� has the same symmetry properties as that of Riemann Tensor
R�  ,

            C� = -C� = -C� = C�                                (A.8)
                   and C� = 0 .

It follows that C� u u is a symmetric traceless and transverse tensor, which is why it
shows up as a second order contribution in the conformal hydrodynamical stress tensor.

References

[1] J. M. Maldacena, The large N limit of superconformal field theories and supergravity,
    Adv. Theor. Math. Phys. 2 (1998) 231�252, [hep-th/9711200].

[2] S. S. Gubser, I. R. Klebanov, and A. M. Polyakov, Gauge theory correlators from
    non-critical string theory, Phys. Lett. B 428, 105 (1998) 105�114, [hep-th/9802109].

[3] E. Witten, Anti-de sitter space and holography, Adv. Theor. Math. Phys. 2 (1998)
    253�291, [hep-th/9802150].

[4] S. Bhattacharyya, V. E. Hubeny, S. Minwalla, and M. Rangamani, Nonlinear fluid
    dynamics from gravity, JHEP 0802, 045 (2008), arXiv:0712.2456 [hep-th].

[5] C. Fefferman, Existence and smoothness of the Navier-Stokes equation, Clay
    Millenium Problems (2000).

[6] R. Emparan and H. S. Reall, Black Holes in Higher Dimensions, Living Rev. Rel. 11,
    6 (2008), arXiv:0801.3471 [hep-th].

[7] R. Gregory and R. Laflamme, Black strings and p-branes are unstable, Phys. Rev.
    Lett. 70 (1993) 2837�2840, [hep-th/9301052].

[8] R. Emparan and R. C. Myers, Instability of ultra-spinning black holes, JHEP 09
    (2003) 025, [hep-th/0308056].

  47Often in the study of conformal tensors, it is useful to rewrite other curvature tensors in terms of the
Schouten and the Weyl curvature tensors-

            R� = C� - [�g][]S ,         R = 2(d - 1)S                               (A.7)
              R� = (d - 2)S� + Sg� ,  G� = (d - 2)(S� - Sg� )

            53
 [9] K. Thorne, D. Macdonald, and R. Price, Black Holes: The Membrane Paradigm.
      Yale University Press, 1986.

[10] T. Damour and M. Lilley, String theory, gravity and experiment,
      arXiv:0802.4169 [hep-th].

[11] V. Cardoso and O. J. C. Dias, Gregory-Laflamme and Rayleigh-Plateau instabilities,
      Phys. Rev. Lett. 96 (2006) 181601, [hep-th/0602017].

[12] S. Lahiri and S. Minwalla, Plasmarings as dual black rings, 0705.3404 [hep-th].

[13] S. Bhardwaj and J. Bhattacharya, Thermodynamics of Plasmaballs and Plasmarings
      in 3+1 Dimensions, JHEP 0903, 101 (2009), arXiv:0806.1897 [hep-th].

[14] J. Bhattacharya and S. Lahiri, Lumps of plasma in arbitrary dimensions,
      arXiv:0903.4734 [hep-th].

[15] M. M. Caldarelli, O. J. C. Dias, R. Emparan, and D. Klemm, Black Holes as Lumps
      of Fluid, JHEP 0904, 024 (2009), arXiv:0811.2381 [hep-th].

[16] K.-i. Maeda and U. Miyamoto, Black hole-black string phase transitions from
      hydrodynamics, JHEP 0903, 066 (2009), arXiv:0811.2305 [hep-th].

[17] G. Aarts, Two complex problems on the lattice: transport coefficients and finite
      chemical potential, Nucl. Phys. A820 (2009) 57c�64c, arXiv:0811.1850 [hep-ph].

[18] S. S. Gubser, I. R. Klebanov, and A. W. Peet, Entropy and temperature of black
      3-branes, Phys. Rev. D54 (1996) 3915�3919, [hep-th/9602135].

[19] P. Kovtun, D. T. Son, and A. O. Starinets, Viscosity in strongly interacting quantum
      field theories from black hole physics, Phys. Rev. Lett. 94 (2005) 111601,
      [hep-th/0405231].

[20] E. Shuryak, Why does the quark gluon plasma at RHIC behave as a nearly ideal
      fluid?, Prog. Part. Nucl. Phys. 53 (2004) 273�303, [hep-ph/0312227].

[21] E. V. Shuryak, What RHIC experiments and theory tell us about properties of
      quark-gluon plasma?, Nucl. Phys. A750 (2005) 64�83, [hep-ph/0405066].

[22] E. V. Shuryak, Strongly coupled quark-gluon plasma: The status report,
      hep-ph/0608177.

[23] E. Shuryak, Physics of Strongly coupled Quark-Gluon Plasma, Prog. Part. Nucl.
      Phys. 62 (2009) 48�101, [arXiv:0807.3033].

[24] T. Schaefer and D. Teaney, Nearly Perfect Fluidity: From Cold Atomic Gases to Hot
      Quark Gluon Plasmas, arXiv:0904.3107.

                                                        54
[25] G. T. Horowitz and V. E. Hubeny, Quasinormal modes of AdS black holes and the
      approach to thermal equilibrium, Phys. Rev. D62 (2000) 024027, [hep-th/9909056].

[26] G. Policastro, D. T. Son, and A. O. Starinets, The shear viscosity of strongly coupled
      N = 4 supersymmetric yang-mills plasma, Phys. Rev. Lett. 87 (2001) 081601,
      [hep-th/0104066].

[27] C. P. Herzog, The hydrodynamics of M-theory, JHEP 12 (2002) 026,
      [hep-th/0210126].

[28] G. Policastro, D. T. Son, and A. O. Starinets, From AdS/CFT correspondence to
      hydrodynamics, JHEP 09 (2002) 043, [hep-th/0205052].

[29] G. Policastro, D. T. Son, and A. O. Starinets, From AdS/CFT correspondence to
      hydrodynamics. II: Sound waves, JHEP 12 (2002) 054, [hep-th/0210220].

[30] D. T. Son and A. O. Starinets, Minkowski-space correlators in AdS/CFT
      correspondence: Recipe and applications, JHEP 09 (2002) 042, [hep-th/0205051].

[31] C. P. Herzog and D. T. Son, Schwinger-keldysh propagators from AdS/CFT
      correspondence, JHEP 03 (2003) 046, [hep-th/0212072].

[32] C. P. Herzog, The sound of M-theory, Phys. Rev. D68 (2003) 024013,
      [hep-th/0302086].

[33] P. Kovtun, D. T. Son, and A. O. Starinets, Holography and hydrodynamics: Diffusion
      on stretched horizons, JHEP 10 (2003) 064, [hep-th/0309213].

[34] A. Buchel and J. T. Liu, Universality of the shear viscosity in supergravity, Phys.
      Rev. Lett. 93 (2004) 090602, [hep-th/0311175].

[35] A. Buchel, J. T. Liu, and A. O. Starinets, Coupling constant dependence of the shear
      viscosity in N=4 supersymmetric Yang-Mills theory, Nucl. Phys. B707 (2005) 56�68,
      [hep-th/0406264].

[36] A. Buchel, On universality of stress-energy tensor correlation functions in
      supergravity, Phys. Lett. B609 (2005) 392�401, [hep-th/0408095].

[37] P. K. Kovtun and A. O. Starinets, Quasinormal modes and holography, Phys. Rev.
      D72 (2005) 086009, [hep-th/0506184].

[38] P. Benincasa, A. Buchel, and A. O. Starinets, Sound waves in strongly coupled
      non-conformal gauge theory plasma, Nucl. Phys. B733 (2006) 160�187,
      [hep-th/0507026].

                                                        55
[39] K. Maeda, M. Natsuume, and T. Okamura, Viscosity of gauge theory plasma with a
      chemical potential from AdS/CFT, Phys. Rev. D73 (2006) 066013,
      [hep-th/0602010].

[40] J. Mas, Shear viscosity from R-charged AdS black holes, JHEP 03 (2006) 016,
      [hep-th/0601144].

[41] O. Saremi, The viscosity bound conjecture and hydrodynamics of M2-brane theory at
      finite chemical potential, JHEP 10 (2006) 083, [hep-th/0601159].

[42] D. T. Son and A. O. Starinets, Hydrodynamics of R-charged black holes, JHEP 03
      (2006) 052, [hep-th/0601157].

[43] P. Benincasa, A. Buchel, and R. Naryshkin, The shear viscosity of gauge theory
      plasma with chemical potentials, Phys. Lett. B645 (2007) 309�313,
      [hep-th/0610145].

[44] R. C. Myers, M. F. Paulos and A. Sinha, Quantum corrections to eta/s, Phys. Rev.
      D79 (2009) 041901, arXiv:0806.2156 [hep-th].

[45] M. R. Garousi and A. Ghodsi, Hydrodynamics of N=6 Superconformal Chern-Simons
      Theories at Strong Coupling, Nucl. Phys. B 812, 470 (2009),
      arXiv:0808.0411 [hep-th].

[46] A. Ghodsi and M. Alishahiha, Non-relativistic D3-brane in the presence of higher
      derivative corrections, arXiv:0901.3431 [hep-th].

[47] D. T. Son and A. O. Starinets, Viscosity, black holes, and quantum field theory,
      arXiv: 0704.024 [hep-th].

[48] R. A. Janik and R. Peschanski, Asymptotic perfect fluid dynamics as a consequence
      of ads/cft, Phys. Rev. D73 (2006) 045013, [hep-th/0512162].

[49] R. A. Janik and R. Peschanski, Gauge / gravity duality and thermalization of a
      boost-invariant perfect fluid, Phys. Rev. D74 (2006) 046007, [hep-th/0606149].

[50] S. Nakamura and S.-J. Sin, A holographic dual of hydrodynamics, JHEP 09 (2006)
      020, [hep-th/0607123].

[51] S.-J. Sin, S. Nakamura, and S. P. Kim, Elliptic flow, Kasner universe and holographic
      dual of RHIC fireball, JHEP 12 (2006) 075, [hep-th/0610113].

[52] R. A. Janik, Viscous plasma evolution from gravity using AdS/CFT, Phys. Rev.
      Lett. 98 (2007) 022302, [hep-th/0610144].

                                                        56
[53] J. J. Friess, S. S. Gubser, G. Michalogiorgakis, and S. S. Pufu, Expanding plasmas
      and quasinormal modes of Anti-de Sitter black holes, JHEP 04 (2007) 080,
      [hep-th/0611005].

[54] K. Kajantie and T. Tahkokallio, Spherically expanding matter in AdS/CFT, Phys.
      Rev. D75 (2007) 066003, [hep-th/0612226].

[55] M. P. Heller and R. A. Janik, Viscous hydrodynamics relaxation time from AdS/CFT,
      Phys. Rev. D76 (2007) 025027, [hep-th/0703243].

[56] K. Kajantie, J. Louko, and T. Tahkokallio, Gravity dual of 1+1 dimensional Bjorken
      expansion, Phys. Rev. D76 (2007) 106006, arXiv:0705.1791 [hep-th].

[57] P. Benincasa, A. Buchel, M. P. Heller, and R. A. Janik, On the supergravity
      description of boost invariant conformal plasma at strong coupling, Phys. Rev. D 77,
      046006 (2008), arXiv:0712.2025 [hep-th].

[58] M. Natsuume and T. Okamura, Causal hydrodynamics of gauge theory plasmas from
      AdS/CFT duality, Phys. Rev. D77 (2008) 066014, arXiv:0712.2916 [hep-th].

[59] M. Natsuume and T. Okamura, A note on causal hydrodynamics for M-theory branes,
      Prog. Theor. Phys. 120 (2008) 1217�1222, arXiv:0801.1797 [hep-th].

[60] M. P. Heller, R. A. Janik, and R. . Peschanski, Hydrodynamic Flow of the
      Quark-Gluon Plasma and Gauge/Gravity Correspondence, Acta Phys. Polon. B 39,
      3183 (2008), arXiv:0811.3113 [hep-th].

[61] M. P. Heller, R. Loganayagam, M. Spalinski, P. Surowka, and S. E. Vazquez, On a
      consistent AdS/CFT description of boost-invariant plasma,
      arXiv:0805.3774 [hep-th].

[62] S. Kinoshita, S. Mukohyama, S. Nakamura, and K.-y. Oda, A Holographic Dual of
      Bjorken Flow, Prog. Theor. Phys. 121, 121 (2009), arXiv:0807.3797 [hep-th].

[63] P. Figueras, V. E. Hubeny, M. Rangamani, and S. F. Ross, Dynamical black holes
      and expanding plasmas, arXiv:0902.4696 [hep-th].

[64] J. D. Bjorken, Highly relativistic nucleus-nucleus collisions: The central rapidity
      region, Phys. Rev. D27 (1983) 140�151.

[65] S. Bhattacharyya, S. Lahiri, R. Loganayagam, and S. Minwalla, Large rotating AdS
      black holes from fluid mechanics, arXiv:0708.1770 [hep-th].

[66] S. Bhattacharyya, V. E. Hubeny, R. Loganayagam, G. Mandal, S. Minwalla,
      T. Morita, M. Rangamani, and H. S. Reall, Local Fluid Dynamical Entropy from
      Gravity, JHEP 0806, 055 (2008), arXiv:0803.2526 [hep-th].

                                                        57
[67] M. Van Raamsdonk, Black Hole Dynamics From Atmospheric Science, JHEP 05
      (2008) 106, arXiv:0802.3224 [hep-th].

[68] M. Haack and A. Yarom, Nonlinear viscous hydrodynamics in various dimensions
      using AdS/CFT, JHEP 10 (2008) 063, arXiv:0806.4602 [hep-th].

[69] S. Bhattacharyya, R. Loganayagam, I. Mandal, S. Minwalla, and A. Sharma,
      Conformal Nonlinear Fluid Dynamics from Gravity in Arbitrary Dimensions, JHEP
      0812, 116 (2008), arXiv:0809.4272 [hep-th].

[70] S. Bhattacharyya, R. Loganayagam, S. Minwalla, S. Nampuri, S. P. Trivedi, and
      S. R. Wadia, Forced Fluid Dynamics from Gravity, JHEP 0902, 018 (2009),
      arXiv:0806.0006 [hep-th].

[71] J. Erdmenger, M. Haack, M. Kaminski, and A. Yarom, Fluid dynamics of R-charged
      black holes, JHEP 0901, 055 (2009), arXiv:0809.2488 [hep-th].

[72] N. Banerjee, J. Bhattacharya, S. Bhattacharyya, S. Dutta, R. Loganayagam, and
      P. Surowka, Hydrodynamics from charged black branes, arXiv:0809.2596 [hep-th].

[73] J. Hur, K. K. Kim, and S.-J. Sin, Hydrodynamics with conserved current from the
      gravity dual, JHEP 03 (2009) 036, arXiv:0809.4541 [hep-th].

[74] M. Torabian and H.-U. Yee, Holographic nonlinear hydrodynamics from AdS/CFT
      with multiple/non-Abelian symmetries, arXiv:0903.4894 [hep-th].

[75] J. Hansen and P. Kraus, Nonlinear Magnetohydrodynamics from Gravity, JHEP 04
      (2009) 048, [arXiv:0811.3468 [hep-th]].

[76] M. M. Caldarelli, O. J. C. Dias, and D. Klemm, Dyonic AdS black holes from
      magnetohydrodynamics, JHEP 03 (2009) 025, [arXiv:0812.0801 [hep-th]].

[77] I. Kanitscheider and K. Skenderis, Universal hydrodynamics of non-conformal branes,
      JHEP 04 (2009) 062, arXiv:0901.1487 [hep-th].

[78] J. R. David, M. Mahato, and S. R. Wadia, Hydrodynamics from the D1-brane, JHEP
      04 (2009) 042, arXiv:0901.2013 [hep-th].

[79] S. Dutta, Higher Derivative Corrections to Locally Black Brane Metrics,
      arXiv:0804.2453 [hep-th].

[80] M. Rangamani, S. F. Ross, D. T. Son, and E. G. Thompson, Conformal
      non-relativistic hydrodynamics from gravity, JHEP 0901, 075 (2009),
      arXiv:0811.2049 [hep-th].

                                                        58
[81] S. Bhattacharyya, S. Minwalla, and S. R. Wadia, The Incompressible Non-Relativistic
      Navier-Stokes Equation from Gravity, arXiv:0810.1545 [hep-th].

[82] N. Ambrosetti, J. Charbonneau, and S. Weinfurtner, The fluid/gravity
      correspondence: Lectures notes from the 2008 Summer School on Particles, Fields,
      and Strings, arXiv:0810.2631 [gr-qc].

[83] R. Baier, P. Romatschke, D. T. Son, A. O. Starinets, and M. A. Stephanov,
      Relativistic viscous hydrodynamics, conformal invariance,and holography, JHEP
      0804, 100 (2008), arXiv:0712.2451 [hep-th].

[84] R. Loganayagam, Entropy current in conformal hydrodynamics, JHEP 0805, 087
      (2008), arXiv:0801.3701 [hep-th].

[85] L. Landau and E. Lifshitz, Fluid Mechanics: Course of Theoretical Physics, Vol. 6,
      Butterworth-Heinemann, 1965.

[86] N. Andersson and G. L. Comer, Relativistic fluid dynamics: Physics for many
      different scales, Living Reviews in Relativity 10 (2007) 1, arXiv:gr-qc/0605010.

[87] W. Israel, Nonstationary irreversible thermodynamics: A Causal relativistic theory,
      Ann. Phys. 100 (1976) 310�331.

[88] W. Israel and J. M. Stewart, Transient relativistic thermodynamics and kinetic
      theory, Ann. Phys. 118 (1979) 341�372.

[89] P. Arnold, G. D. Moore, and L. G. Yaffe, Transport coefficients in high temperature
      gauge theories: (I) Leading-log results, JHEP 11 (2000) 001, [hep-ph/0010177].

[90] P. Arnold, G. D. Moore, and L. G. Yaffe, Transport coefficients in high temperature
      gauge theories. II: Beyond leading log, JHEP 05 (2003) 051, [hep-ph/0302165].

[91] A. Muronga, Causal theories of dissipative relativistic fluid dynamics for nuclear
      collisions, Phys. Rev. C69 (2004) 034903, [nucl-th/0309055].

[92] P. Romatschke, New Developments in Relativistic Viscous Hydrodynamics,
      arXiv:0902.3663 [hep-ph].

[93] R. P. Geroch, On Hyperbolic "Theories" of Relativistic Dissipative Fluids,
      gr-qc/0103112.

[94] R. Wald, General relativity, Chicago, University of Chicago Press, 1984, 504 p.
      (1984).

[95] M. Henningson and K. Skenderis, The holographic weyl anomaly, JHEP 07 (1998)
      023, [hep-th/9806087].

                                                        59
 [96] V. Balasubramanian and P. Kraus, A stress tensor for anti-de sitter gravity,
       Commun. Math. Phys. 208 (1999) 413�428, [hep-th/9902121].

 [97] J. Sondow and E. W. Weisstein, Harmonic Number, MathWorld - A Wolfram Web
       Resource (05, 2009). Mathworld:Harmonic number

 [98] E. Witten, Anti-de sitter space, thermal phase transition, and confinement in gauge
       theories, Adv. Theor. Math. Phys. 2 (1998) 505�532, [hep-th/9803131].

 [99] S. de Haro, S. N. Solodukhin, and K. Skenderis, Holographic reconstruction of
       spacetime and renormalization in the AdS/CFT correspondence, Commun. Math.
       Phys. 217 (2001) 595�622, [hep-th/0002230].

[100] R. K. Gupta and A. Mukhopadhyay, On the universal hydrodynamics of strongly
       coupled CFTs with gravity duals, JHEP 0903, 067 (2009),
       arXiv:0810.4851 [hep-th].

[101] P. M. Chesler and L. G. Yaffe, Horizon formation and far-from-equilibrium
       isotropization in supersymmetric Yang-Mills plasma, arXiv:0812.2053 [hep-th].

[102] V. E. Hubeny, M. Rangamani, and T. Takayanagi, A covariant holographic
       entanglement entropy proposal, JHEP 07 (2007) 062, [arXiv:0705.0016].

[103] S. A. Hartnoll, C. P. Herzog, and G. T. Horowitz, Holographic Superconductors,
       JHEP 0812, 015 (2008), arXiv:0810.1563 [hep-th].

[104] C. P. Herzog, P. K. Kovtun, and D. T. Son, Holographic model of superfluidity,
       arXiv:0809.4870 [hep-th].

[105] A. Yarom, Fourth sound of holographic superfluids, arXiv:0903.1353 [hep-th].

[106] P. Basu, A. Mukherjee and H. H. Shieh, Supercurrent: Vector Hair for an AdS Black
       Hole, arXiv: 0809.4494 [hep-th].

[107] V. E. Hubeny and M. Rangamani, unpublished.

[108] M. Haack and A. Yarom, Universality of second order transport coefficients from the
       gauge-string duality, Nucl. Phys. B 813, 140 (2009), arXiv:0811.1794 [hep-th].

[109] C. P. Herzog, M. Rangamani, and S. F. Ross, Heating up Galilean holography, JHEP
       0811, 080 (2008), arXiv:0807.1099 [hep-th].

[110] A. Adams, K. Balasubramanian, and J. McGreevy, Hot Spacetimes for Cold Atoms,
       JHEP 0811, 059 (2008), arXiv:0807.1111 [hep-th].

                                                         60
[111] D. T. Son, Toward an AdS/cold atoms correspondence: a geometric realization of the
       Schroedinger symmetry, Phys. Rev. D 78, 046003 (2008),
       arXiv:0804.3972 [hep-th].

[112] K. Balasubramanian and J. McGreevy, Gravity duals for non-relativistic CFTs, Phys.
       Rev. Lett. 101, 061601 (2008), arXiv:0804.4053 [hep-th].

[113] J. Maldacena, D. Martelli, and Y. Tachikawa, Comments on string theory
       backgrounds with non-relativistic conformal symmetry, JHEP 0810, 072 (2008)
       arXiv:0807.1100 [hep-th].

[114] E. G. Gimon, A. Hashimoto, V. E. Hubeny, O. Lunin, and M. Rangamani, Black
       strings in asymptotically plane wave geometries, JHEP 08 (2003) 035,
       [hep-th/0306131].

[115] I. Fouxon and Y. Oz, Conformal Field Theory as Microscopic Dynamics of
       Incompressible Euler and Navier-Stokes Equations, Phys. Rev. Lett. 101, 261602
       (2008), arXiv:0809.4512 [hep-th].

[116] I. Fouxon and Y. Oz, CFT Hydrodynamics: Symmetries, Exact Solutions and
       Gravity, JHEP 0903, 120 (2009), arXiv:0812.1266 [hep-th].

[117] A. Bagchi and R. Gopakumar, Galilean Conformal Algebras and AdS/CFT,
       arXiv:0902.1385 [hep-th].

[118] V. N. Gusyatnikova and V. A. Yamaguzhin, Symmetries and Conservation Laws of
       Navier-Stokes Equations, Acta. Appl. Math., 15, (1989) 65�81.

[119] M. Hassaine and P. A. Horv�athy , Field�dependent symmetries of a non-relativistic
       fluid model, Ann. Phys. (N. Y.) 282, 218 (2000), [math-ph/9904022].

[120] V. E. Hubeny, M. Rangamani, S. Minwalla, and M. Van Raamsdonk, The
       fluid-gravity correspondence: The membrane at the end of the universe, Int. J. Mod.
       Phys. D17 (2009) 2571�2576.

[121] C. Eling, I. Fouxon, and Y. Oz, The Incompressible Navier-Stokes Equations From
       Membrane Dynamics, arXiv:0905.3638 [hep-th].

[122] N. Iqbal and H. Liu, Universality of the hydrodynamic limit in AdS/CFT and the
       membrane paradigm, Phys. Rev. D79 (2009) 025023, arXiv:0809.3808 [hep-th].

[123] S. Bhattacharyya and S. Minwalla, Weak Field Black Hole Formation in
       Asymptotically AdS Spacetimes, arXiv:0904.0464 [hep-th].

                                                         61
