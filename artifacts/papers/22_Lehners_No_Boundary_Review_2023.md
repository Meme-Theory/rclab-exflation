# Lehners No Boundary Review 2023

**Source:** `22_Lehners_No_Boundary_Review_2023.pdf`

---

arXiv:2303.08802v3 [hep-th] 28 Mar 2024         Review of the No-Boundary Wave Function

                                                                                 Jean-Luc Lehners

                                                    Max�Planck�Institute for Gravitational Physics (Albert�Einstein�Institute)
                                                                                       14476 Potsdam, Germany

                                         Abstract

                                             When the universe is treated as a quantum system, it is described by a wave
                                         function. This wave function is a function not only of the matter fields, but
                                         also of spacetime. The no-boundary proposal is the idea that the wave function
                                         should be calculated by summing over geometries that have no boundary to the
                                         past, and over regular matter configurations on these geometries. Accordingly,
                                         the universe is finite, self-contained and the big bang singularity is avoided.
                                         Moreover, given a dynamical theory, the no-boundary proposal provides proba-
                                         bilities for various solutions of the theory. In this sense it provides a quantum
                                         theory of initial conditions.

                                             This review starts with a general overview of the framework of quantum
                                         cosmology, describing both the canonical and path integral approaches, and
                                         their interpretations. After recalling several heuristic motivations for the no-
                                         boundary proposal, its consequences are illustrated with simple examples, mainly
                                         in the context of cosmic inflation. We review how to include perturbations,
                                         assess the classicality of spacetime and how probabilities may be derived. A
                                         special emphasis is given to explicit implementations in minisuperspace, to
                                         observational consequences, and to the relationship of the no-boundary wave
                                         function with string theory. At each stage, the required analytic and numerical
                                         techniques are explained in detail, including the Picard-Lefschetz approach to
                                         oscillating integrals.

                                         Keywords: cosmology, quantum gravity, big bang, initial conditions
                                         PACS: 98.80.Qc, 98.80.-k, 04.60.-m, 03.70.+k

                                              Email address: [email redacted] (Jean-Luc Lehners)  March 29, 2024
                                         Preprint submitted to Elsevier
Contents

1 Introduction                           3

2 Quantum Cosmology                      6

2.1 The Need for Quantum Gravity . . . . . . . . . . . . . . . . . . . 6

2.2 An Example: Transitions in a de Sitter Universe . . . . . . . . . 10

2.3 Formal Developments: Canonical and Path Integral Quantisations 22

2.4 How to Reconstruct the Universe from the Wave Function . . . . 26

3 The No-Boundary Proposal               32

3.1 Heuristic Motivations . . . . . . . . . . . . . . . . . . . . . . . . 32

3.2 Simple Inflationary Examples . . . . . . . . . . . . . . . . . . . . 38

3.3 Numerical Techniques . . . . . . . . . . . . . . . . . . . . . . . . 44

3.4 Ekpyrotic Examples . . . . . . . . . . . . . . . . . . . . . . . . . 49

3.5 Classical Histories from the No-Boundary Wave Function . . . . 52

3.6 Implementations in Minisuperspace . . . . . . . . . . . . . . . . . 56

3.7 No-Boundary Saddles with Anisotropies and Black Holes . . . . . 76

4 Link to Observations                   83

4.1 Perturbations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83

4.2 Probabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89

4.3 Taking Stock: What Does the No-Boundary Proposal Explain? . 93

5 Link to String Theory                  95

5.1 Robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95

5.2 Link to AdS/CFT and Holographic Definition . . . . . . . . . . . 97

5.3 A Filter on the Landscape . . . . . . . . . . . . . . . . . . . . . . 108

5.4 Allowable Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . 113

6 Discussion and Open Questions          118

Appendix A Canonical Quantisation        120

Appendix B Gravitational Path Integrals  122

Appendix C Picard-Lefschetz theory       124

                            2
1. Introduction

    The principles of quantum theory are the most basic physical principles un-
covered to date. They have been tested over the past century in numerous
experiments, and form the basis of modern electromagnetic and nuclear tech-
nology. What has not been achieved so far is a direct experimental verification
of the quantisation of the fourth fundamental force, namely gravity. The reasons
for this are easily understood to lie in the relative weakness of the gravitational
force compared to electromagnetic and nuclear interactions.

    So even though we are not compelled by experiment to assume that gravity
is quantised, there are good arguments that indicate that it must be. One
such argument, based on the internal consistency of the laws of physics, will be
provided in the next section. Once we contend that gravity is indeed quantised,
and that the laws of quantum theory apply to all interactions, it is clear that
the entire universe must also be considered to be a quantum system. As such,
it must be described by a wave function. This wave function is then not only a
function of the matter fields, but also of spacetime itself. But how should one
calculate the wave function of the universe?

    Note that if the wave function includes a description of space and time, then
it will necessarily also tie in with the question of boundary and initial conditions
of the universe, since these are the conditions at the ends of space and time. In
other words, a wave function of the universe links together the laws of dynamical
evolution and the specification of initial conditions. This is in stark contrast
with a laboratory setting, where initial conditions are carefully prepared by the
experimenter.

    But then what should the conditions be at the ends of space and time? Here
J. Hartle and S. Hawking made a suggestion that is as radical as it is elegant
[1, 2]: they proposed that there should be no such ends! In other words, they
proposed that space and time should have no boundary to our past. And if there
is no boundary, then there is no need for further boundary conditions � hence
(the hope is that) this fully specifies the initial conditions for our universe, and
it indicates how to calculate the wave function of the universe.

    The idea that the universe is entirely self-contained, both in space and in
time, sounds almost like a tautology. What it means is that if there was a
boundary, then one would have to specify conditions at that boundary and they
would link to an evolution on the other side of the boundary � put differently,
if there was a boundary then outside information would be required. But there
is more: in ordinary classical general relativity, the no-boundary condition is
plainly impossible. This is because under reasonable assumptions on the matter
content of the universe, the celebrated singularity theorems [3] imply that in our
past there must have existed a curvature singularity, the big bang. Such a sin-
gularity would be an end point of spacetime. Therefore one cannot impose the
no-boundary condition in classical physics. It is a true quantum gravitational
condition. And it eliminates the big bang singularity. As will be discussed in
detail, the no-boundary condition in fact has similarities with quantum tun-
nelling. Thus one possible interpretation of the no-boundary proposal is that it

                                                   3
eliminates the big bang singularity, and replaces it by describing the origin of
the universe as a tunnelling event from nothing, i.e. from the absence of not
just matter, but also the absence of spacetime.

                                                                      ( elds)

big bang     no-boundary

Figure 1: Left panel: A cartoon of the evolution of a classical, expanding universe with closed
1-dimensional spatial sections. Space is horizontal and time vertical. Going back in time,
one reaches a singularity, the big bang. Right panel: By contrast, the no-boundary proposal
suggests that one should consider geometries that are (smoothly) rounded off in the past, and
that contain no boundary there. Such a condition automatically eliminates the big bang.

    A cartoon of the no-boundary idea is shown in Fig. 1. The figure should
make it clear that no-boundary geometries, though they have no boundary to
the past, do actually have a boundary (but a single one): this boundary may be
thought of as a spatial slice of our universe, either a current slice or a spatial slice
in the early universe. The no-boundary wave function then has as arguments
the field values (or momenta) on this "final" hypersurface. It is not a transition
amplitude in the usual sense, since this would depend on field values or momenta
on two separate hypersurfaces. However, one may at least heuristically think of
it as a transition from nothing to today.

    It should be clear by now that the no-boundary proposal assumes a fully
quantum view of spacetime: actual spacetime does not exist when not measured,
i.e. when not in interaction with either itself or matter. It is the interactions
between the different constituents of the universe that result in our perception of
classical spacetime, and of large scale classical laws of evolution. And vice versa,
going back in time towards the putative big bang, one will necessarily encounter
departures from the classical evolution. A significant part of this review will be
concerned with making these ideas, which may sound rather vague at first, more
precise.

    There is an immediate concern that should be mentioned from the outset.
Let us assume we are given a wave function for the universe. Then it will imply
probabilities for different histories of the universe, or one could say that it will
provide probabilities for different universes. Yet we live in a single universe, so
how can we talk about probabilities for different universes? It should be said
that this issue is not fully resolved. Certainly, inside of the universe probabilities
for the outcomes of experiments make sense, and we will show in some detail
how this comes about. But probabilities are inherently linked to a classical

          4
notion of time (think about any operational definition of probabilities). And
in quantum cosmology, time itself is not a priori classical, it is not fixed from
outside. There is no overarching concept of spacetime in which universes reside
� rather, each universe has its own spacetime. Hence it may not make sense to
compare probabilities for different universes. Nevertheless the common practice
has been to do just that [4, 5], and to ask, given a set of dynamical laws, whether
the no-boundary wave function implies that a universe like ours is typical or
highly unlikely. We will return to this question at various points, and mention
ways in which the interpretation of the wave function might be elucidated. Let
us emphasise though that even within a given universe the no-boundary wave
function can make post- and predictions for observations.

    Besides such conceptual issues, the first challenge in fact is to find a con-
vincing mathematical implementation of the no-boundary proposal. This will
be a central focus of this review, and it is probably also the area in which
most progress has been made in recent years. As we will see, this is directly
linked to an understanding of gravitational path integrals quite generally, and
many connections with string theory have emerged. These connections are now
providing a two-way flow of insights: string theory provides clues regarding
the mathematical implementation of the no-boundary proposal, and the no-
boundary wave function provides a framework in which to address some of the
landscape/swampland-related puzzles of string theory. These connections pro-
vide promising starting points for further research, and one aim of this review
is to provide the necessary background for undertaking such research.

    In brief, the outline of the review is as follows: we will start with a general
overview of quantum cosmology in section 2. This will serve to introduce the
basic concepts one is led to, both in the canonical and path integral quantisa-
tion schemes. Section 3 then introduces the no-boundary proposal, starting from
heuristic motivations and building up in mathematical rigour. Both analytic and
numerical methods for finding no-boundary solutions will be described in detail.
The crucial question of how to extract probabilities from the no-boundary wave
function, and to derive predictions for observations, will be tackled in section 4.
More recent topics, and in particular the above-mentioned connections with
string theory, will be the topic of section 5. To end, we will list a number of
outstanding questions in the discussion section 6. Finally, three appendices fill
in a few details about canonical and path integral quantisation, as well as some
perhaps lesser known mathematical methods, in particular Picard-Lefschetz the-
ory. This review aims to be self-contained, but it assumes prior knowledge of
general relativity, quantum mechanics, and the basics of cosmology and string
theory, with the latter only being required in section 5.

    Notation and conventions: Greek indices run over space and time, lower case
Latin indices only over space, while capital Latin indices run over fields. For
Lorentzian metrics, the signature is taken to be mostly plus, and the conventions
for gravity are R� = � -  � + �  - �  with R� = R� .
We set 8G = 1, but mostly retain  explicitly.

                                                   5
2. Quantum Cosmology

    Quantum cosmology is, simply put, the application of quantum principles to
the whole universe. No less. Despite this highly ambitious mission statement,
this task is, at least to some extent, already within reach of current physics. In
practice, there are two main simplifications that are helpful: the first is based
on the observational fact that the early universe was comparatively simple, in
the sense that it was spatially highly isotropic and homogeneous. This sug-
gests an approximation scheme where one starts with geometries and matter
configurations that are exactly isotropic and homogeneous on spatial slices, and
then includes perturbations as a small correction. A second simplification that
is typically made use of is the semi-classical approximation, i.e. one considers
an expansion in Planck's constant  (or, rather, in the dimensionless inverse
Planck mass) and works to leading or first sub-leading order. Of course, at the
end of the calculations, one has to check whether the approximations used were
justified. As we will see, with these approximations at hand, one may actually
get quite far in describing quantum effects in the early universe.

               1

   1           2

S  2        S

      R        n  R

Figure 2: Left panel: The double slit experiment: a source S emits particles that are detected
on a recording surface R. When two slits are present in the intermediate screen, an interference
pattern is observed, as indicated on the right. Right panel: By opening successively more slits,
one arrives at the picture that the amplitude should be calculated by summing over all possible
paths.

2.1. The Need for Quantum Gravity

    We will start by recalling the famous double slit experiment. This exper-
iment highlights the most striking features of quantum mechanics. Moreover,
it provides a direct motivation for the path integral and, as we will argue, the
quantisation of gravity. Fig. 2 shows the setup. Consider a source S sending
particles, e.g. electrons, through slits 1 and 2, and a recording plane R that
measures the impact of the particles. We call the flux of particles measured at
R, or equivalently the probability of detecting particles, P1 when only slit 1 is
open, P2 when only slit 2 is open, and P when both slits are open. Classically,
we expect P = P1 + P2. However, this is famously not what is observed. Rather,
the probability distribution at R when both slits are open is given by a formula
that is akin to having waves emanating from S, passing through the slits, and

         6
interfering before reaching R,

                                   P = |1 + 2|2 ,                                            (1)

leading to the interference fringes shown in the figure. The crucial point is that
this formula remains valid even when the source is dimmed so much that only
a single particle is emitted during a time interval that is at least as long as
the crossing time. This experiment then directly illustrates the superposition
principle: amplitudes that correspond to the same outcome, but to different
evolutions, are summed. The two possible trajectories of the particle interfere
with each other.

    Above we did not specify how the amplitude is numerically determined. One
guideline is that the amplitude should recover classical physics when  is small.
First note that  has dimensions of action, namely [energy] � [time]. Second,
recall that classical solutions are given by extrema of the action S (S = 0).
Then one may guess that the amplitude should be an oscillating function of
S/. The appropriate choice turns out to be [6]

                                                =  e  i  S  .                                (2)


With this choice, whenever S/ is large, nearby trajectories cancel each other
out, as eiS/ varies rapidly, except near extrema where S = 0. That the ex-

ponent is linear in the action can be derived from the additional requirement

that the amplitude leads to the correct composition property of paths. With the

choice above, for two paths in succession, with actions S1, S2, we get a combined
                              ei                      i           i
amplitude  that  factorises,       (S1  +S2  )  =  e     S1    e     S2  ,  as  it  should.  Moreover, one

may show [6] that for this choice one recovers the standard Schro�dinger equation

by splitting up paths into small intervals.

Now it is just a small step to the path integral. This step is illustrated in the

right panel of Fig. 2. Imagine adding additional slits to the screen, say n slits

in total. Then the amplitude will be given by a sum over trajectories passing

through all of the slits,

                                                i=n

                                        =             ei    Si    ,                          (3)


                                                i=1

and new interference patters will be generated. In fact, we could have added
more screens in between the source and the recording plane, and then opened
slits in all of these intervening screens. By imagining a dense array of screens,
with infinitesimal slits, one arrives at the conclusion that the amplitude should
be given by the sum over all possible trajectories, each trajectory being weighted
by a phase that is the action divided by ,

                                   =            Dx    e  i  S[x]     ,                       (4)


where x denotes the position of the particle and Dx is an appropriate measure
over paths. This is Feynman's path integral approach to quantum theory [6].

                                                   7
In fact, what we have just described is the propagator . Due to Heisenberg's
uncertainty relation, we cannot in general assume a definite initial position of
the particle � rather, we should consider an initial wave function 0.  then
propagates this wave function to a later time t, according to

t(x) =  0(x0)dx0 .                                                                          (5)

That is to say, for each part of the initial wave function one considers a sum
over all possible trajectories to a later configuration. A useful example of an
initial wave function is given by a Gaussian wave packet centered at xi with
spread  and with momentum pi,

              1                               (x0 -xi )2      i
          1/41/2                                   22         
                                         e . -
0(x0)  =                                                  +      pi x0                      (6)

The state is normalised such that  +  |0|2dx0    =        1.  The       limit  of  a  pure  position
                                   -
state is then achieved by considering   0. This yields a delta function in

position, and hence corresponds to a non-normalisable state, but nevertheless

can be a useful idealisation to consider. Above, we implicitly assumed such an

idealisation when saying that the particles were emitted at the source location S.

We just saw that the double slit experiment suggests an approach to quantum

theory in which one sums over all possible particle paths. In extending these

arguments to field theories, one would reach the conclusion that one should

integrate over all possible matter configurations. But what about gravity?

Let us go back briefly to the case with just two slits. Then the amplitude is

well approximated by the contributions from the saddle points

  N e + e , i                                 i

                                   Ssaddle,1     Ssaddle,2                                  (7)

where N is a normalisation factor. Here Ssaddle,1 corresponds to the classical
action for the trajectory that passes through slit 1, and similarly for slit 2. When
gravity is taken into account, this means that it is the action for the trajectory
of particle 1 including the backreaction on the spacetime, as it is the action of a
classical solution to the full equations of motion. In other words, the amplitude
is a superposition not just of two particle paths, but of two spacetimes that each
contain a particle path (for a similar argument, see [7]).

    Note that it would not make sense to assume that there is just one under-
lying spacetime: if we imagine adding more slits, then the backreaction due to
the mass of the particle taking various paths would add up. Considering mul-
tiple slits, finely spaced, one could make the backreaction arbitrarily large, an
absurd conclusion considering that the limit of infinitely many slits corresponds
to having no screens at all, i.e. corresponds to free propagation. Thus we cer-
tainly cannot assume that the various trajectories together lead to a combined
gravitational effect. It makes equally little sense to assume that there is a fixed
background spacetime, maybe given by the "average" backreaction. After all,
classical motions of particles follow geodesics, which depend on the curvature of

                                      8
the spacetime. And this curvature depends on th1e trajectory itself, and hence
must be different for the two trajectories we are considering. Basically, the
gravitation1al force exerted on other objects would2 be ill defined if there was a

fixed background spacetime.

SspacTehtiemoens2l-ywiinthte-mrpartetteart.ioInntohtahtemr awkoersdSsse, ncsoenicsepthtuaatlwlye  have a superposition of
                                                                                                  it makes sense to think

of the double slit experiment as a quantum gravity experiment. It is only the

relative weakness of thRe gravitational force whichn implies thaRt one can ignore
the gravitational backreaction in laboratory experiments (so far). But concep-

tually, requiring internal consistency of the physical laws implies that gravity

and spacetime must be quantised along with matter.

   B                                                                                              hij(t=1)

A                                                                                                 hij(t=0)

Figure 3: Left panel: when calculating the amplitude for a particle to propagate from A to
B, we sum over all paths that connect the end points. Right panel: the analogous situation
in quantum cosmology is to sum over all geometries and matter configurations that connect
two 3-dimensional boundary surfaces (here illustrated as 1-dimensional circles located at
coordinate values t = 0, 1) with metrics hij . In this picture, the connecting geometries are
cylinders, and only two are shown so as not to overload the picture. Each is its own spacetime,
and one should not think of them as existing in an ambient spacetime.

    The path integral then provides an obvious framework to attempt such a
quantisation: it simply implies that we must also sum over geometries, so that
heuristically a wave function  should be calculated as

      =                      Dg�  D  e  i  S[g�  ,]0  ,                                                     (8)


where 0 describes an initial spatial geometry and matter configuration, see
Fig. 3 for an illustration. One can also think of 0 as specifying boundary
conditions. In the following, the rather schematic formula above will be made
much more precise1.

    1The path integral quantisation of gravity can however not represent the full theory of
quantum gravity. This is because gravity is not renormalisable, which implies that when loop
corrections are taken into account effective higher order curvature terms are generated. Only
when the spacetime curvature remains well below the Planck scale can such corrections be
ignored. In the applications we will consider this will always be the case.

                                                   9
2.2. An Example: Transitions in a de Sitter Universe

    We have just given arguments for why gravity should be quantised, and how
one is naturally led to a path integral quantisation scheme. To illustrate this
approach, it is useful to study an example. We will specialise to the simplest,
yet physically relevant, setting, namely that of gravity coupled to a (positive)
cosmological constant , with action (setting 8G = 1)

S = d4x-g              R                     
                       2           +      d3y hK .  (9)
           M              -

                                      M

This theory is a first approximation to the current, dark energy dominated, uni-
verse, and it may also be a good approximation to the early universe, if inflation
took place. The action is integrated over a 4-manifold M, with 3-dimensional
boundaries M and induced 3-metric hij. If one wants to keep the metric fixed
on the boundaries, then one has to include the Gibbons-Hawking-York (GHY)
[8, 9] surface term, which involves the determinant h = det(hij) and the trace
of the extrinsic curvature K, defined in (A.3). It has the effect of eliminat-
ing second derivatives in the action. The GHY term thus allows for so-called
Dirichlet boundary conditions, where one keeps the boundary metric fixed. If
one does not include any surface term, one obtains a Neumann condition in-
stead, meaning that one can keep the momentum conjugate to the metric fixed
on the boundary [10]. This will become clear in the example below.

    At first, we will restrict our analysis to the simplified context of closed
Friedmann-Lema^itre-Roberston-Walker (FLRW) universes with metric

ds2 = -N~ 2(t)dt2 + a2(t)d23 ,                      (10)

where N~ is the lapse function and d32 the metric on the unit three-sphere2.
This symmetry reduced setting is an example of minisuperspace. Not only does
this reduction greatly simplify the analysis, it is also expected to be a good
approximation when describing the universe on the largest scales, and at early
times. The reason for taking the spatial section to be closed is that this prevents
a divergent volume integral. One could for instance also take flat sections, and
assume the topology of a torus.

    With these choices, the action simplifies to

                    1  -3a   a 2   +  3a  -  a3  ,  (11)
                             N~ 2
S = 22 dtN~

                  0

where an overdot stands for a derivative w.r.t. the time coordinate. We are
free to choose the time coordinate such that the integral interpolates between
fixed 3-geometries at coordinate values t = 0, 1; the proper time elapsed is
then determined by the lapse N~ . Note that the kinetic term for the scale factor

    2Explicitly, one can take d23 = d2 + sin2  d2 + sin2  d2 , with 0  (, )  ,
0    2. The unit 3-sphere has volume 22.

                             10
a is negative; this is due to the attractive nature of gravity [11] � it reflects
the inherent instability of gravitational systems. Sometimes, this feature is
referred to as the "conformal mode problem", though it seems more reasonable
to consider it a characteristic of gravity rather than a problem.

    The path integral was heuristically defined in (8) as a sum over all geometries
with given boundary conditions. In making this expression precise, one has to
face a number of issues: for one, we have not specified contours of integration
yet, and moreover we have not dealt with diffeomeorphism invariance. This
is important, as in the sum over geometries we would like to include only in-
equivalent ones, and thus have to eliminate those that are related by changes of
coordinates. The way this is done requires techniques that lie somewhat outside
of the main thrust of this section, and these techniques are outlined separately
in Appendix B. The end result is surprisingly simple: the path integral is given
by

G[a1; a0] = dN~ a=a1 Da eiS(N~ ,a)/ ,                   (12)

           C                 a=a0

where the functional integral over the lapse has been reduced (due to the gauge
fixing) to an ordinary integral. We have yet to specify contours of integration,
an issue we will return to shortly. The expression above has a simple inter-
pretation: The path integral over the scale factor DaeiS(N~,a)/ represents the
amplitude for the universe to evolve from scale factor value a0 to the value a1,
in a fixed proper time N~ . Then the integral over the lapse implies that we
sum over all possible proper durations that this transition can take. Defined in
this way, the path integral corresponds essentially to a gravitational propagator
(Green's function), hence the nomenclature G[a1; a0]. Note that we have im-
plicitly assumed here that the initial wave function corresponds to a "position"
eigenstate, where the size of the universe is known with infinite precision. This
is a convenient idealisation in the present context.

    In order to proceed, it turns out to be useful to redefine our variables some-
what, and to write the metric in the following form [12]:

ds2  =  -   N2         dt2q  +  q(tq )d32     .         (13)
           q(tq )

That is to say, we call the square of the scale factor q(tq), and rescale the lapse.
This is perhaps a rather unfamiliar writing of the metric, and the new time
variable tq does not have a particular physical meaning, but it has the great
advantage that the action becomes quadratic in q, since one obtains

                    1  -   3    q2  +  N  (3  -  q)  ,  (14)
                          4N
S = 22 dtq

                  0

where now   d/dtq. Here we have again chosen the range of the time coordinate
to be 0  tq  1, that is to say tq = 0 on the "initial" 3-dimensional boundary,
and tq = 1 on the "final" one, see also Fig. 3. In deriving the action, the

                          11
GHY surface terms                        =  2    2   3  q  q|ttqq  =1  have      been    incorporated,          and
                      d3y hK                        2N             =0

they have eliminated second derivatives on q, making use also of integration by

parts.

Varying the action w.r.t. q and N results in

S = 22        dtq q    3    q�  -    N        + N            3     2  q2   +  3  -  q      -  32  qq     |ttqq  =1
                      2N                                   4N                                 N                 =0

                                                                                                         (15)

This confirms that we can indeed keep q fixed on the boundaries (q = 0). We
set q(0) = q0 and q(1) = q1. The equation of motion and constraint are then
respectively given by

                      q� =  2   N    2;       3     q2  +  3       =   q   .                             (16)
                             3              4N 2

The equation of motion can be solved easily, and with the chosen boundary
conditions the solution is

              q� =       N  2   tq2  +     -     N  2   +  q1      -   q0     tq + q0 .                  (17)
                      3                       3

Note that this is just a solution of the equation of motion, and not necessarily
of the constraint.

    Now we employ a trick to evaluate the path integral over q, which consists
in shifting the variables of integration such that a general history is written as
a departure from a classical solution,

                                q(tq) = q�(tq) + Q(tq) .                                                 (18)

For consistency with the boundary conditions, we must set Q(0) = Q(1) = 0,
but otherwise Q is not restricted (in particular Q is not required to be small).
With this shift (which is only a change of variables, and not an approximation),
the path integral becomes

                                   dN e22iS0/              Q[1]=0      DQe22iS2/ ,

              G[q1; q0] =                                                                                (19)

                                C                          Q[0]=0

with

        S0 =   1          3        q�2  +  3N    -  N q�           ,      S2  =         3   1            (20)
                      - 4N                                                          - 4N
                 dtq                                                                          dtq Q 2 .

              0                                                                            0

No terms linear in Q have appeared, precisely because q� solves the equation of
motion. But now the integral over Q is a Gaussian, which can be evaluated
exactly [13] (with a uniquely determined contour of integration), yielding

                          Q[1]=0                                       3i        .                       (21)
                                                                       2N 
                                  DQe22iS2/ =

                         Q[0]=0

                                                 12
                                             K4        K3 K2                K1                    N

                        J4                                J3 J2                               J1

                                  4              3                       2             1

                        K4                             K3 K2                                 K1

                                          J4           J3         J2        J1

Figure 4: This sketch shows the placement of the steepest descent (J ) and ascent (K) contours

associated with the four saddle points of the integral (22), in the complexified plane of the

lapse function N. Regions where the integral converges (asymptotically) are shown in green,

and regions of asymptotic divergence in red. (The lines delineating red and green regions

have constant weighting.) The boundary conditions are such that the initial and final scale

factors  are  larger  than   the  Hubble  radius,      q1  >  q0  >   3  .  The  positive  real   line  contour  can  be

deformed into the sum J2 + J1, or equivalently the dashed orange contour. Figure reproduced

from [14].

The time integral in (20) can be evaluated explicitly, so that in the end we are
left with an ordinary integral over the lapse function,

                              G[q1; q0] =            3i           dN e22iS0/ ,                                   (22)

                                                       2 C N 1/2

with

              S0  =   N3  2   +      N  -     (q0    +    q1)  +  3      +  1       -  3  (q1  -  q0)2  .        (23)
                          36               2                                N          4

    We will analyse this integral by performing a saddle point approximation.
The proper tool for doing this systematically is Picard-Lefschetz theory, which
is reviewed in Appendix C. First, we must determine the saddle points, defined
by S0/N = 0. There are four of them, located at

                                     3                     1/2                            1/2
                                          3                                 3
                      N   =   c1              q0  -    1       + c2             q1  -  1          ,              (24)

with c1, c2  {-1, 1}. Moreover, the action at the saddle points is found to be

                                     6                     3/2                             3/2
                                          3                                 3
              S0saddle    =  -c1              q0    -  1       + c2             q1  -  1          .              (25)

    The question we are faced with now is whether all of these saddle points ac-
tually contribute to the integral. This turns out to depend both on the boundary

                                                           13
conditions, and on the integration contour C.

Classical boundary conditions

    We    will  first  look  at   classical           boundary        conditions,  where         q0, q1  >    3  and

consequently the saddle points (24) are real. We will also assume that q1 > q0.

As for the contour C, it makes sense to look back at the definition of the metric

(13): the lapse determines the proper time separation between events. If we want

the propagator to correspond to causal evolution, where time moves forward,

then we can do this by fixing the sign of N, say to be positive. Moreover, at zero

lapse the metric degenerates, and thus zero should be excluded. This suggests

that we should take the positive real half-line as integration contour [15],

                                              C = (0+, ) .                                                       (26)

Note that (22) contains an essential singularity at N = 0, which reflects the
physical intuition that a non-trivial transition cannot occur in zero proper time,
and supports the exclusion of zero from the contour.

    Along the real N line, the integral (22) is only conditionally convergent. Us-
ing Picard-Lefschetz theory, we would like to rewrite it as a sum over absolutely
convergent integrals,

                                     C = (0+, ) = nJ .                                                           (27)


where J are steepest descent contours (thimbles) emanating from the saddle
points and the n can be �1 for contributing thimbles, depending on the chosen
orientation of the thimbles. In the present case, the two saddle points on the
positive real axis clearly contribute to the integral, and one can indeed rewrite
(0+, ) = J2 + J1, where the thimbles are oriented in the increasing Re[N ]
direction, see Fig. 4. Thus the propagator can be approximated as a sum of two
phases,

          G[q1; q0]          e-i     e  i  S  (N2  )  +  e e i   i  S(N1  )                                      (28)
                                  4                          4                                                   (29)

                                     122                            3/2            122                   3/2
                                                      3                 -4          
                             cos                         q0  -   1             e ( ) . -i        q1  -1
                                                                                              3

In  this  approximation,     we      have     also       included     factors  of  e�i     ,  which      arise   from
                                                                                        4

the angle of the Lefschetz thimbles at the saddle points (and are straightfor-

wardly determined by looking at the change in Re(iS0) near the saddle points

[14]).

    A number of questions now arise, foremost: What is the meaning of this

mathematical expression? We will address this quite generally in sections 2.3

and 2.4. For now, we can make progress by recalling the intuition behind the

path integral. All possible histories contribute to the transition, but the saddle

points represent the dominant ones. Hence it is useful to look at the saddle

points in more detail.

                                                             14
             500                      saddle N2                             500                   saddle N1

             400                                     Re[q(t)]               400
                                                               t
             300                                                            300                                 Re[q(t)]
                                                                                                                          t
             200                                                            200

             100                                                            100
                         Im[q(t)]                                                       Im[q(t)]

Figure 5: Saddle point geometries for classical boundary conditions. For this example,  =

 3   ,  q0  = 200, q1 = 500, so that N2                     = 100, N1 = 300.        Saddle 2 is purely expanding,                while
100
                                                                                       3
saddle   1   first  shrinks        to  the  de   Sitter     radius   (with  qmin    =     =       100)  and  then  re-expands.

    As a consequence of satisfying S0/N = 0, the saddle points correspond to
geometries that satisfy not only the equation of motion, but also the constraint
in (16); they are solutions of the full Einstein equations. We may then find the
geometry that they describe by plugging the saddle point values (24) into the
expression for the scale factor (17). The resulting expression is lengthy and not
worth writing out in full. However, it is useful to look at the expansion rate at
t=0:

dq�     (tq  =    0)  =  -            N2    +    q1  -   q0  =    2  -q0    +    3     �2         q0    -    3     q1        -  3   .
dtq                                3                                                                                            

                                                                                                                                   (30)

Since q1 > q0, we can infer that saddle point 2 corresponds to an initially ex-
panding geometry, while saddle 1 is contracting. Explicit examples are shown

in Fig. 5. The classical, maximally symmetric solution to the Einstein equations

with a positive cosmological constant is de Sitter spacetime. In the closed slicing,

where the spatial sections are 3-spheres, it is well known that de Sitter space-

time can be viewed as a hyperboloid (with minimal radius                                                3    )  when  embedded


in a higher-dimensional space. The saddle points correspond to portions of this

hyperboloid, with saddle 2 corresponding to a portion of the hyperboloid on
one side of the minimal radius, while saddle 1 includes the region with minimal

radius and thus contains a classical bounce.

    These geometries provide the dominant contribution to the transition from
q0 to q1. Since we fixed only the initial and final sizes, and since two possible
classical solutions exist which link q0 to q1, it is natural that in (28) we ob-
tained a sum over the two contributions, in complete analogy with the double

slit experiment. In a more realistic model, one would also include matter and
fluctuations of the geometry � such interactions would then cause decoherence

and would therefore lead to separate, non-interfering evolutions of the two sad-

dle points.

Non-classical boundary conditions

     What we discussed above were transitions between large, classically allowed,

scale factor values. But it is interesting to see what happens when we set one

of  the     scale   factors,           say  q0,      to  a   small,  classically       forbidden        value,     i.e.      q0  <  3  .


                                                                     15
                                           K2                                         K1

                   J2              2                                                           1        J1

                                        J2                                         J1
                            K2
                                                                                                   K1

                            J3                                                                     J4

                                   3               K3                           K4           4

                   K3                                                                                K4
                                   J3                                                  J4

Figure 6: A sketch of the steepest ascent/descent lines for boundary conditions where the first

scale  factor  is  smaller  than      the  de  Sitter   radius     (q0  <   3  ),  and    the   second  larger  (q1  >  3  ).  In

the yellow regions, the weighting is in between the weightings of the adjacent saddle points.

The orange integration contour (0+, ) can be deformed into the dashed orange line, which is

the thimble J1 associated with saddle point 1. Thus this is the only saddle point contributing

significantly to the transition. Figure reproduced from [14].

Then the saddle points become complex, with

                                   3                               1/2                             1/2
                                                       3                           3
                       N    =  c1          i   1   -       q0          + c2           q1   -   1        ,                  (31)

again with c1, c2  {-1, 1}. The action at the saddle points also becomes
complex,

                                   6                              3/2                              3/2
                                                       3                           3
               S0saddle   =    c1          i   1   -       q0         - c2            q1  -    1        .                  (32)

Now the steepest ascent/descent contours look quite different, see Fig. 6 for an
illustration.

    As the figure shows, the integration contour C = (0+, ) can be deformed
into the steepest descent contour J1 associated with saddle point 1, with positive
real and imaginary parts. Thus in this case only a single saddle point contributes
significantly to the path integral, and the amplitude can be approximated by

                       G[q1;   q0]            ei   22  S0  (N1  )                                                          (33)
                                                                                                                           (34)

                                                   122                 3/2      122                3/2

                                       e ( ) e ( ) . -     1-      q0       -i             q1  -1
                                                               3                        3

An example of the associated geometry is shown in Fig. 7. Apart from the end
points, the geometry is now complex, reflecting the fact that this transition is
classically impossible, and rather represents quantum tunnelling between the

                                                                16
                        500                        saddle N1

                        400

                        300                                                  Re[q(t)]

                        200

                        100

                        0                                         Im[q(t)]             t

                             0.0 0.2 0.4 0.6 0.8 1.0

Figure 7: Saddle point geometry for a transition from non-classical to classical boundary

conditions.  For  this  example,    =   3   ,  q0  =  75,  q1  =  500,   so  that  N1  =  200 + 50i.  Note  that
                                       100
the scale factor starts and ends with real values, but is complex in between.

two specified scale factor values. In line with this interpretation, note that the

amplitude    (34)  is   suppressed     as  e-  122    (1-      q0)3/2 ,  indicating       that  this  transition
                                                           3

is less likely than classical evolution. Also, the smaller q0 is, the stronger the

suppression. Meanwhile, the classically allowed part of the transition, related

to q1, leads to an oscillating factor in the amplitude (34). This setting is thus

very much in analogy with standard barrier penetration problems in ordinary

quantum mechanics.

Let us highlight what may be a surprising feature: even though the saddle

points are solutions to the classical equations of motion, they can describe quan-

tum effects. This is because the boundary conditions are classically impossible

here, forcing upon us a complex solution to the classical field equations.

Wheeler-DeWitt equation
    The transition amplitudes that we derived above satisfy an important equa-

tion, called the Wheeler-DeWitt (WdW) equation. Later on, we will derive it
formally, but it is already useful to see how it arises for the specific examples
we have just studied.

    The Lagrangian of our system can be inferred from the action (14), and
reads

                             L = 22             3     q2   +   3N  -     N q  .                             (35)
                                            - 4N

Thus, the canonical momentum associated with q is

                                       p   =   L      =    -  32   q  ,                                     (36)
                                               q              N

so that the Hamiltonian can be written as

                   H    =qp  -  L   =     N        p2 + 124(3 - q)                 = N H^ .                 (37)
                                       - 62

                                                      17
In phase-space the action can thus also be written as

    S=            qp - N H^ dtq =              qp        +  N       p2 + 124(3 - q)                   dtq .        (38)
                                                            62

Here we can see that the lapse N is a Lagrange multiplier, and implies the
classical constraint

                                                      H^ = 0 .                                                     (39)

But now we can also quantise the theory directly, in the field representation,

by  promoting      the  momentum           to  its       operator   equivalent,           p     p^ =  -i        .  This
                                                                                                             q
results in the Wheeler-DeWitt equation

                            H^   =  0      2   2         +  124(q        -  3)      =     0  ,                     (40)
                                               q2

with (q) the wave-function of the universe. The corresponding propagator G
satisfies [16]

                                       H^ G = -i62(q0 - q1) ,                                                      (41)

where the Hamiltonian operator acts either on q0 or on q1 (the factor 62 is also
sometimes absorbed into the definition of H^ ). This last equation is referred to
as the inhomogeneous Wheeler-DeWitt equation.

    Now we can go back to the path integral and explicitly show that it satisfies
this equation. Starting from (22) and (23), one can take successive derivatives
(momentarily setting  = 1)

               G   =        3i         dN    22       iS0,q1   e22  iS0
               q1            2        N 1/2

                   =        3i         dN    22       i    N       -   3    (q1  -  q0)         e22iS0 ,           (42)
                             2        N 1/2              -2           2N

and analogously

    2G   =        3i         dN     22iS0,q1q1 - 44S02,q1                e2 2 iS0
    q12            2        N 1/2

         =        3i         dN     -44        N         +      3  (q1   -  q0)  2 32i          e22iS0 .           (43)
                   2        N 1/2              2               2N                  -N

Using first the properties of the thimbles, and then integration by parts, one
can obtain the relation

         N  -  1  e22  iS0             dN   d         N  -  1  e22  iS0
               2                           dN               2
                               =
                            0

                               =   -   1     dN       e2 2 iS0  +   22i          dN       S0,N  e2 2 iS0  .        (44)
                                       2     N3                                  N1

                                                   2                                   2

                                                         18
This is now substituted into (43) to obtain

2G      3i       dN       -124 (q1 - 3k) e22iS0 + 62i                       -  1  e22  iS0  
q12      2      N 1/2                                                          2
     =                                                                   N
                                                                                            0

     = - 124 (q1 - 3) G + 62i           3i      N  -  1  e22  iS0                              (45)
                                                      2
                                                                      ,
                                         2                         0

which is almost the WdW equation already. The Lefschetz thimble we are
integrating over is precisely such that the contribution from N   vanishes.
But near the origin, we have to work a little harder: given that the thimble
there approaches the origin along the imaginary axis, it helps to write N = in,
leading to

        lim  e2 2 iS0  =  2    lim   e-32    (q1 -q0 )2  =     2      (q0      q1)  .          (46)
                           i                       2n         3i
                               n0
        N0 N                                2n                             -

Hence, with  reinstated, we indeed recover the WdW (propagator) equation

             2  2G     +  124  (q1   -  3)  G  =   -     62i(q0    -  q1).                     (47)
                q12

For future reference, let us point out that if we had integrated over a contour
from N = - to N = + (passing around the singularity at N = 0), the right
hand side would have been zero and we would have obtained the homogeneous
WdW equation.

    The WdW equation is the quantum equivalent of the Friedmann equation
in cosmology. In some sense, it is the equivalent of the Schr�odinger equation
when gravity is included. (Later on, we will see that it actually contains the
Schr�odinger equation.) Here we see that, by construction, the path integral
automatically satisfies this equation. We will discuss it in more detail in the
coming sections.

Neumann boundary conditions
    Before proceeding with more formal developments, it is useful to give an

example of the path integral where instead of fixing the scale factor on both
sides of the transition, we fix its conjugate momentum instead (on one side).
This means that we will consider a Neumann, rather than a Dirichlet, condition.
For definiteness, we will impose a Neumann condition on the t = 0 boundary.
This can be achieved by not adding a GHY surface term to the action there.
That is to say, the minisuperspace action is now given by

        S = 22   1         3  qq� +   3  q2  +  N (3     -  q)     -  32   qq|tq  =1           (48)
                          2N         4N                               N
                   dtq

                0

If we now use integration by parts in order to get rid of the second derivative
term in the action, then this will cancel the GHY boundary term at tq = 1 but

                                        19
instead it will generate a surface term at tq = 0,

            S = 22       1            -   3  q2    +    N  (3  -  q)        -      32    qq|tq    =0              (49)
                                         4N                                        N
                           dtq

                        0

Varying w.r.t. the scale factor q, we obtain the same equation of motion as
before, Eq. (16), together with the boundary conditions

                  -   32   q(q)       =  0|tq =0     ,         -  32     q   q  |tq  =1  ,                        (50)
                      N                                           N

confirming  that  we  can  specify       the    momentum              p0    =    -    32    q(tq  =      0)  and  the
                                                                                       N
scale factor q1 = q(tq = 1). With these boundary conditions, the solution to the

equation of motion is

                  q� =     N  2  t2q  -  p0N    tq   +  q1   -        N  2  +    p0N        .                     (51)
                        3                32                       3              32

We can now employ the same trick as before, namely we can shift the integration

variable q = q� + Q(tq). This time, the fluctuation integral satisfies the bound-
ary conditions Q (tq = 0) = 0 and Q(tq = 1) = 0, and with these boundary

conditions it simply evaluates to a constant (independent of the lapse) [17],

                                             1       32Q 2            3i
                                             0          2N            2
                              DQe = - i         dtq                             .                                 (52)


To leading order, this factor is unimportant and we will ignore it. We are then
left again with an ordinary integral over the lapse,

                                         2              p0      2 +(3+      p02                   p0 q1
                                          9             62                124                     22
                           dN e , i 22          N  3-        N                                 +

G[p0; q1] =                                                                      -q1 )N                           (53)

                        C

where we have not specified the integration contour C yet. There are significant
differences with the pure Dirichlet case. For one, the integrand is regular at
N = 0. This makes sense, as we fix the initial momentum and not the initial
size. Hence the path integral sums over a range of initial sizes, and this can
include a transition where the initial size is already equal to the final size �
precisely the N = 0 case, cf. also (51). Moreover, the integral (53) admits only
two saddle points now, located at

                           N�    =        p0     �      3         q1  -   1  ,                                    (54)
                                         22                    3

and with action

                              3p0          p03             122           q1  -     1  3/2
                                         364                          3
                  S(N�)    =          +                                                        .                  (55)


    To proceed, it is again useful to look at examples. For definiteness, let us
use initial momenta p0 that correspond to the momenta for the saddle point

                                                   20
                                                       500                   saddle N-

                                                       400

                                                       300                              Re[q(t)]
                                                                                                  t
             K+                                        200
                         N+                                                             Re[q(t)]
         K_                                            100
N_                J+                                               Im[q(t)]                       t

         J_                                            500                   saddle N+

                                                       400

                                                       300

                                                       200

                                                       100
                                                                   Im[q(t)]

Figure 8: Saddle points and their steepest descent/ascent lines in the complex plane of the

lapse function, for the situation where we have a transition with mixed Neumann-Dirichlet

boundary  conditions.  Here    =   3   ,  p0  =  -62,  q1  =  500,  so       that   N   =   (-300, +100).
                                  100

geometries encountered above for pure Dirichlet boundary conditions. That is

to say, we are choosing initial momenta such that at least one saddle point must

be equal to the one from the Dirichlet case. For the example shown in Figs. 4

and 5, the momenta at t = 0 are real. For saddle 2, which corresponded to an

expanding geometry, we have from (30) that p0 = -32q/N2(t = 0) = -62.

The corresponding thimbles and saddle point geometries are shown in Fig. 8.

We can see that indeed the saddle point N+ corresponds to the expanding

geometry. But what is more surprising is the saddle N-, which is again the

bouncing geometry that we also encountered in the Dirichlet case. How can

this saddle point be present, given that we fixed the initial momentum? The

resolution is that it has a negative lapse, so that the combination of an initially

contracting geometry with a negative lapse can yield the same momentum as an

expanding    universe  with    positive       lapse,  given   that           p=  -  32  q.  The      integration
                                                                                     N
contour for the lapse is essentially unique: the real lapse line can be deformed

into a sum over the two thimbles associated with N�,

                               C = (-, ) = J- + J+ .                                                       (56)

Note that because of the absence of a singularity at N = 0 we must integrate
over the full lapse line in order to obtain an invariant definition of the path
integral. Thus, with this integration contour and with these classical boundary
conditions, we recover the analogous semi-classical amplitude as for the pure
Dirichlet case, namely a sum over two saddles with phases given by (55).

    When we choose an initial momentum that corresponds to the bouncing
saddle (saddle 1) in Figs. 4 and 5, we obtain a very similar situation, but this
time it is the expanding geometry that arises with negative lapse, see Fig. 9. In
fact, the saddles in Figs. 8 and 9 combined reproduce the four saddles of the
Dirichlet case.

    The case with non-classical boundary conditions is however a little different.
In the pure Dirichlet case (cf. Fig. 6), there was a single saddle point that
contributed to the amplitude. Its geometry was complex, though starting and

                                                 21
                                                                             500                   saddle N-

                                                                             400                                 Re[q(t)]
                                                                                                                           t
                                                                             300
                                                                                                                 Re[q(t)]
                   K_                                K+                      200                                           t
               N_                                                N+
                                                                             100
                       J_                                 J+                             Im[q(t)]

                                                                             500                   saddle N+

                                                                             400

                                                                             300

                                                                             200

                                                                             100
                                                                                         Im[q(t)]

Figure 9: Same as Fig.                       8, but with             =   3   ,  p0  =    +62, q1              =  500, so that N       =
                                                                        100
(-100, +300).

ending with real values. Combining (30) and (31), we can infer that the initial
momentum is then pure imaginary. For an example, see Fig. 10. In the mixed
Neumann-Dirichlet case, we recover the same saddle as before, but in addition
we get a second saddle with negative real part of the lapse. The two saddle
points correspond to geometries that are complex conjugates of each other. In
terms of integration contour, a surprise is that we cannot choose the real lapse
line as fundamental contour � the integral simply diverges when integrated over
real lapse values. Thus we must define the integration directly on the thimbles.
Here we have several choice in principle: we could integrate over J-, J+ or
a linear combination J- � J+. If we sum over both thimbles, we obtain the
approximate amplitude

                                                p30                                 3/2                                       3/2
                                             364                122

                                                      ( ) ( ) - i
                                                     e � e 
                                  i  3p0  +                                q1  -1                     122        q1  -1
                                                                        3                          i          3
G[p0, q1]  e                                                                                                                       ,  (57)


which contains a suppression factor (keeping in mind that p0 is imaginary), in
line with this describing a sort of tunnelling process from a classically impossible
scale factor value to a large value. The no-boundary wave function will turn
out to be rather closely related to this amplitude.

    The examples provided in this section serve to illustrate the general frame-
work of quantum cosmology. To be more rigorous, one would also have to
include perturbations and see if the minisuperspace approximation was actually
justified. We will do this once we get to the main topic of interest, namely
the no-boundary wave function. However, there are some general properties of
quantum gravity amplitudes that are useful to derive first. Plus we will see how
amplitudes such as those shown here may best be interpreted. These will be
the topics of the next two subsections.

2.3. Formal Developments: Canonical and Path Integral Quantisations

    The observed homogeneity and isotropy of the early universe imply that for
a broad brush analysis, it is useful to start with metrics that already admit

                                                                     22
                                                                  500

                                                                  400                  saddle N-

J_                                           J                    300                                Re[q(t)]

            K_                                         +          200

    N_                        K+                                  100                             Im[q(t)]
                                       N+                                                                             t
                                                                       0

                                                                -100                   0.4 0.6 0.8 1.0
                                                                      0.0 0.2

                                                                500

                                                                400                    saddle N+

                                                                300                                  Re[q(t)]

                                                                200

                                                                100

                                                                    0        Im[q(t)]                          t

                                                                       0.0 0.2 0.4 0.6 0.8 1.0

Figure 10:  Same as Fig.  8,  but with an imaginary initial momentum.                                Here  =                 3   ,  p0  =
                                                                                                                            100
32i, q1 = 500, so that N� = �200 + 50i. The real lapse line, shown in orange, cannot serve

as integration contour in this case, as it runs into the red, asymptotically divergent regions at

both large negative and positive values.

these symmetries in their spatial sections. Later on, one can then extend the
range of metrics considered, and also add small general perturbations. But such
a restriction to symmetric metrics is also technically very useful, as it leads to
models that are (at least in part) solvable. This minisuperspace context leads
one to consider actions of the following general structure,

            S=            dtN  1  GAB      1              dqA  1  dqB           -  U (qA)         .                                 (58)
                               2           N               dt  N   dt

Here qA are fields that depend solely on time. These could be functions that
form a part of the metric, or these could be matter fields. A field that is always
present is the scale factor, which determines the size of the universe. This field
has the characteristic that it enters with a negative sign kinetic term, cf. (14).
Thus GAB always contains a negative component. One case that is of particular
interest is where one considers the scale factor of the universe, plus a scalar field,
so that qA = (a, ). Then with the metric (10) the action is given by

            S = 22   1            -   3    aa 2           +      1  2     a2  2    +   3a  -      a3V  ()                ,          (59)
                                     N~ 2                      2N~
                       N~ dt

                    0

where V () is the scalar potential, and Gaa = -122a, G = 22a3. We will
mostly focus on this case when exhibiting examples.

    In the present section we will perform the canonical quantisation directly
at the level of the minisuperspace action (58). For readers interested in the
general case, without symmetry reductions, appendix Appendix A provides an
overview. To the action (58) is associated a Hamiltonian

                               H  =  1  GAB               pApB    +       U  ,                                                      (60)
                                     2

                                                          23
with the canonical momenta pa = -122aa /N, p = 22a3/N, and where the
effective potential is given by

                           U = 22 -3a + a3V .                                              (61)

The Hamiltonian is classically zero and corresponds to the Friedmann equa-

tion.  If  one  quantises  the  theory  canonically,          by    replacing  pA    -i        
                                                                                           qA
-iA, one obtains the quantum version of the Hamiltonian constraint, namely

the Wheeler-DeWitt (WdW) equation

                           H^ =      -  2  2  +  U      = 0,                               (62)
                                        2

where  = (a, ) is the wavefunction of the universe. For the second-derivative
operator, there is an ambiguity in terms of the precise placement of the deriva-
tives � a sensible choice is to fix this "factor ordering" issue by writing the
operator as 2 = GABAB, since then it is covariant under field redefinitions.
However, if one is only interested in results to leading order in , then the or-
dering is unimportant. As this will be the case for us, we will simply choose a
convenient ordering when the situation arises. For the model (59), the WdW
equation explicitly reads

                 2   1 2 6 2                  - 3a + a3V () (a, ) = 0 .                    (63)
                484  a a2 - a3 2

    Mathematically, the WdW equation looks just like the Klein-Gordon equa-
tion for a scalar particle. As such, it admits a conserved current, defined as

                           JA  =  -  i  A - A                       .                      (64)
                                     2

One can easily check that AJA = 0 subject to using the WdW equation. This

conserved current will play an important role in the interpretation of the WdW

equation, in section 2.4. For now, let us just observe that it is this current, and

not , that is conserved. Hence the standard assignment of probabilities,

familiar from quantum mechanics, cannot automatically be recovered.

In simple cases the WdW equation can be solved directly. For now, let us

just give a qualitative argument as to the nature of solutions, in the context of

inflation. A first approximation to inflation is to consider a constant potential

V () = . Then one can neglect  in (63). The effective potential looks as

shown in Fig. 11. It is reminiscent of a tunnelling problem. And indeed, for

large a, we obtain the approximate solutions

                                        e�i 42            a3
                                                       3
                                                              .                            (65)

Note that these solutions oscillate, and roughly corresponds to free propagation
(in this case classical expansion of the universe). Meanwhile, at small a the
solution is exponentially growing or damped,

                                        122          a2   )3/2
                                                       3
                                 e . �
                                              (1-               -1                         (66)

                                              24
   -U
0.5

           0.5                                1.0     1.5       a

-0.5

-1.0

-1.5

-2.0

-2.5

Figure 11: The effective potential -U with constant potential .

This is the regime where the scale factor takes non-classical values, smaller than

the classical minimum radius amin =     3   of a de Sitter universe.  One might try
                                        V

to interpret such a regime as describing the quantum tunnelling of a universe

from zero size to a = amin. Later on, we will see that the no-boundary proposal

provides a framework to make this much more precise. For now, let us simply

point out that a difficulty with solving the WdW equation is that one typically

does not know how to fix the integration constants that arise in the solutions.

This issue, as we saw, is much clearer in the path integral approach.

In section 2, we saw with the help of an explicit example that the path

integral satisfies the WdW equation. We can also provide a formal argument

showing that this must be the case generally (see e.g. [18, 16]). The argument

is surprisingly quick. The propagator/wave function can be decomposed into

the lapse integral, plus an amplitude with fixed lapse,


      G[q1; q0] = dN G[q1; q0; N ] .                                   (67)

                      0

For definiteness, we assumed the pure Dirichlet case, with an integration domain
consisting of positive real values of the lapse. The integrand

                                        q=q1       i

      G[q1; q0; N ] =                         Dqe     S(N,q)           (68)

                                        q=q0

is then the amplitude to evolve from q0 to q1 in "time" N . Just like in ordinary
quantum mechanics, this amplitude then satisfies the Schro�dinger equation

      i    G[q1; q0;  N              ]  =   H^ G[q1; q0; N ] .         (69)
               N

The only subtlety is that we must take into account the coincidence condition
that

      lim G[q1; q0; N ] = 62(q0 - q1) .                                (70)
      N 0

                                        25
Again, the factor of 62 simply depends on conventions. It then immediately
follows that the total propagator of minisuperspace models satisfies the inho-
mogeneous WdW equation,


H^ G[q1; q0] = dN H^ G[q1; q0; N ]

    0

=i     dN    G[q1; q0;  N  ]
    0              N

=iG[q1; q0;  N]  N =
                 N =0

= - i62(q0 - q1) .                  (71)

Had the integration domain for the lapse been the entire lapse line, the right
hand side would have been zero above and we would have obtained a solution
to the homogeneous WdW equation.

    In discussing the WdW equation, we encountered the issue of factor ordering,
leading to a potential ambiguity at sub-leading orders in an expansion in . Can
the path integral resolve this? From the point of view of the path integral, the
corresponding question is which integration measure one should choose (note
that changes in measure are also sub-leading in a saddle point approximation).
This could lead to progress, cf. the gauge fixing procedure outlined in appendix
Appendix B, where one uses the Liouville measure on the full path integral,
including all ghost fields. For further discussion of this question, see also [16].

2.4. How to Reconstruct the Universe from the Wave Function

    We just derived the Wheeler-DeWitt equation, and showed that the path
integral satisfies it. An obvious and important question is however how the
equation should be interpreted. In some sense the WdW equation is the ana-
logue of the Schro�dinger equation in quantum mechanics, but the presence of
gravity changes a few things significantly. Most crucially, time cannot, and does
not, appear explicitly. This is because space and time are quantised now, and
must emerge from the solutions, rather than being outside constructs. Never-
theless, we will see that the WdW equation contains the Schr�odinger equation
under appropriate circumstances.

    But let us start with something more basic. Both the path integral and
the WdW equation, as we have formulated them, concern transitions between
3-dimensional hypersurfaces. But that is not really what we observe. When
we look out into the world, we actually receive information about our past light
cone. So, strictly speaking, quantum gravity should deal with this past light
cone and not with spacelike domains. However, if we take a spacelike boundary
at some finite time in our past light cone, then the enclosed spacelike region
has the light cone ending at our brain in its causal future, see the left panel of
Fig. 12. When we look back further and further, ever larger spacelike regions
are encapsulated. But since, to a good approximation, we may assume spatial
isotropy and homogeneity, this presents no complication and nothing physical

       26
A                                                                                          hij(t=0)

   observer                                                  q1(4)

                                                             q1(3)

                                                             q1(2)
                                                             q1(1)

     spacelike
   hypersurface

                                                                                       q0

Figure 12: Left panel: When we observe the universe, we obtain information about our past
light cone (in purple). In this sketch time is vertical and space horizontal. It is however
equivalent (and mathematically easier) to deal with spacelike hypersurfaces whose causal
development would include this light cone. Right panel: We can imagine a succession of
transitions from a given initial condition q0 to a series of final conditions q1(i). When the
wave function is of WKB form, one can infer the physically relevant spacetime from this
succession, as indicated by the dotted green line.

is lost by dealing with spacelike hypersurfaces � mathematically however, this
formulation is much more tractable.

    Still, having an amplitude for a transition between two spacelike hypersur-
faces is not the same as having a full spacetime manifold. So why do we perceive
a continuous evolution in time? In other words, what holds the world together
from one instant to the next, and why does this appear seamless?3

    It turns out that the answer is already included to a large extent in the
saddle point approximation to the path integral. Let us assume that the wave
function can be written in the following suggestive form4,

                           =   e  1  (W  +iS  )  ,                                                   (72)


where W, S are real functions of the fields qA, W being the weighting and S the

phase. We can then expand the WdW equation (62) as a series in  (assuming
W and S to be O(0)), finding to leading and sub-leading orders respectively

   -  1  (W  )2  +  1  (S  )2  +  U  =   0,         W � S = 0,                                       (73)
      2             2

                               2W = 0,              2S = 0,                                          (74)

where e.g. W � S  GABAWBS. There are two equations at each order,
one for the real part and one for the imaginary part of the equation. It is also

    3The even harder question is: why is our consciousness connected to a particular (small
patch of a) hypersurface, but always only one and only for an instant, with a succession of
such quasi-instantaneous connections unfolding?

    4In general, the wave function is given by a superposition of such terms, but in applications
to quantum cosmology a single term typically dominates.

                                  27
useful to write out the conserved current (64),

                              JA    =   e  2  W  AS     .                  (75)


    Vilenkin then developed the following interpretation [19]: if we look at the
left equation in (73), we may notice that if W varies slowly compared to S, then
we recover the classical Hamilton-Jacobi equation,

(W)2  (S)2                                       1  (S     )2  +  U    0,  (76)
                                                 2

with S being identified with the classical action, and the canonical momentum
assignment

                                    pA  =     S   .                        (77)
                                              qA

This is in fact the Wentzel-Kramers-Brillouin (WKB) semi-classical approxima-
tion often used in standard quantum mechanics, namely that the amplitude of
the wave function varies slowly, and the phase fast. The right equation in (73)
then expresses the conservation of the current (75) to leading order, while (74)
ensures conservation at sub-leading order as well.

    Several implications immediately follow. The classical action S describes a
congruence of (classical) trajectories. One can for example think of this congru-
ence as being foliated by constant-S surfaces. Then one can choose trajectories
along a normal vector nA to these surfaces, such that nS > 0 (the locus
S = 0 describes the breakdown of the semi-classical approximation) and de-
fine relative probabilities as

                                 P  =   e  2  W  nS  .                     (78)


How an overall normalisation can be implemented in a mathematically precise

way is an open question, hence the probabilities are only relative. But these

relative probabilities are then positive and conserved along classical trajecto-

ries, and for small  approximately correspond to the standard probabilities in
                           2
quantum mechanics, P    e     W  =  (up to normalisation).                 Also, different

foliations give the same probabilities, as long as the foliations are chosen so as

to intersect each trajectory only once (the foliations must be spacelike with re-

gard to the minisuperspace metric GAB). One can improve upon this procedure

when the amplitude of the wave function vanishes sufficiently fast, W  -,

asymptotically in all directions along the foliation. In this case, a normalisation

is possible and one can obtain absolute (approximate) probabilities, which are

approximately conserved. We will discuss examples in section 3.6.

When the WKB approximation holds, the wave function (72) satisfies

                        pA = -i A  AS                                      (79)

to a good approximation, in agreement with the assignment (77). The wave
function is thus peaked on solutions described by the first order relation pA =

                                           28
AS, i.e. it is peaked on solutions of the classical (Hamiltonian) equations of
motion. However, the boundary conditions can force the solutions to be complex
valued, when they correspond to conditions that are classically not allowed. This
will become clear when we discuss the no-boundary proposal. Note also that a
theory of initial conditions, such as the no-boundary proposal, fixes the initial
conditions required to calculate the action. Thus, in calculating the action, half
of the integration constants are already fixed, and this correspondingly restricts
the solutions allowed by Eq. (79).

    In all the relations above, we are comparing wave functions at different final
boundary conditions. This is how one can verify that the amplitude varies much
more slowly than the phase, (W)2  (S)2. Thus one should really think of a
family of transitions, from fixed initial conditions to a series of final conditions,
cf. the right panel in Fig. 12. When this series of transitions is such that the
WKB conditions hold, then one can assign a relative probability P   to
the associated evolution. The physical spacetime should then be identified with
the collection of such final boundaries, and to leading order in  this sequence of
3-dimensional hypersurfaces will follow a solution of the Einstein equations (but
only for as long as the WKB condition holds). In this vein, it is also sometimes
said that quantum cosmology provides probabilities for "histories" [5].

    There is another interesting consequence that arises for sub-systems [19]. If
we assume that there is a small sub-system characterised by the Hamiltonian
H2, with negligible backreaction on the universe as a whole, then the WdW gets
augmented by a term,

-  2  2  +  U  +  H2   = 0.  (80)
   2

If we now expand the WdW again in powers of , then at sub-leading order we
get the additional equation

   iS � 2 = H22 ,            (81)

where we factorised  = 02 into a product of 0, depending only on the
background variables, and 2, depending also on the perturbations. Now comes
the crucial observation: If one identifies

                             (82)
         S �   t

then one obtains an effective time variable, and one recovers the Schr�odinger
equation

      i     2     =  H22  .  (83)
         t

This is remarkable. From the space- and timeless WdW equation we thus recover
the Schro�dinger equation for sub-systems, as long as the WKB approximation
is applicable. The background wave function itself provides the time. Let us
briefly check that this definition of time makes sense, for a simple case: in

               29
a de Sitter universe, we saw in (65) that at large scale factor the solution is

S  -42          a3.  With  Gaa  =    -122a,         we  obtain
             3

                       S �  = GaaaS a =                    a    a  =!      ,           (84)
                                                        3              t

in agreement with the classical de Sitter solution expressed in physical time t,

a=  3  e  3  t  .  We  should  note  that  in    more   general    cases,  when  more  fields  are


present, one must make sure that the integrability conditions associated with

the change of variables in (82) are everywhere satisfied.

A few more comments are in order. On the mathematical side, let us mention

that there exists a body of work that attempts to make the definition of physical

states, and their associated Hilbert space, rigorous, at least in minisuperspace

models [20, 21, 22, 23]. This is based on the "induced" inner product, and we

will briefly sketch the main idea. The norm based on the Klein-Gordon current

has the well-known problem that it is not positive definite. For example, for

a massive scalar field in flat space we may write out the mode decomposition
(with  = k2 + m2)

          (t, x) =              d3k              a(k)ei(kx-t) + b(k)ei(kx+t)       ,   (85)
                           (2)3/21/2

and this leads to the Klein-Gordon norm (where  is a spacelike hypersurface)

       1, 2KG =                J�d�        -     i     d� (1�2 - 2�1)                  (86)
                                                 2


                                     = d3k (a1(k)a2(k) - b1(k)b2(k)) .                 (87)

As we can see, positive (a) and negative (b) frequency modes enter with a relative

minus sign.  By    co=ntrasdt4,xthe-ignd1uce2d,  inner product starts from    the  Schro�dinger
product 1    , 2                                 which is positive definite   but  can lead to

unwanted divergences in the present context. One then uses the WDW opera-

tor (62) both to define physical states, and to remove an overcounting of gauge

transformations in the product between physical states. This procedure is de-

scribed in some detail in [22, 23, 24], with the end result that for the massive

scalar example above one ends up with

                1, 2phys = 4 d3k (a1(k)a2(k) + b1(k)b2(k)) .                           (88)

Effectively, the induced inner product has changed the relative sign between
positive and negative frequency parts, and has made the product positive def-
inite. It may thus be used to define and find normalised physical states. As
discussed in [24] via application to a number of examples, one then recovers
the heuristic interpretation outlined above when the wave function is of WKB
form; we will consequently use this formulation in what follows. Given that we

                                                 30
will mostly work to leading order in  only, the most important consequence for
us will be to deem wave functions normalisable when their weighting falls off
asymptotically (W  -) in all directions in parameter space, while we will
discard wave functions as unphysical when the weighting grows asymptotically
(W  +) in at least one direction5.

    An important physical effect is that once one adds matter and perturbations
to the universe, then additional classicalisation occurs due to decoherence. This
arises from the interactions present in the system [25, 26], with short wave-
length modes acting as an environment that decoheres the long wavelength
"background". Thus the WKB classicality which we have used above is pre-
sumably mostly relevant for the very early universe. Especially if there was
an early phase of evolution when no matter was present yet, or if we want
to consider the simultaneous emergence of spacetime and matter from a fully
quantum state, then WKB classicality is absolutely crucial in guaranteeing a
classical background.

    In general, the wave function is approximated not just by a single saddle
point, but by a collection thereof,

     e  1  (Wi +iSi )  .  (89)


  i

In such a case, decoherence also plays an important role, as it effectively isolates
the different saddle points into separate universes [27]. For each such universe,
the above treatment of relative probabilities and sub-systems then separately
applies. In fact, it is possible to approach the entire subject of quantum cosmol-
ogy from the point of view of decoherence, focussing on quasi-classical histories
that evolve effectively independently of each other (for a suitably coarse-grained
description). This is the decoherent histories program, see e.g. [28] for a com-
prehensive introduction.

    It is important to realise that the notion of probability derived above is only
approximate, valid semi-classically, to leading order in . Thus unitarity is also
only an approximate concept [19]. This is directly related to the fundamental
role that time plays in quantum mechanics and quantum field theory. Here
time is just part of another quantum field, the metric, and hence our standard
intuition cannot be taken for granted. That said, it is clear that it would be
desirable to further clarify the definition of probabilities in quantum cosmology
� it seems clear that much more can be found out about this topic [29], and we
will mention a few ideas later on.

    Now, given the crucial importance of the WKB approximation, we may ask
under what circumstances we can expect the wave function to take this form. In
fact, at the moment only two early universe scenarios are known to automatically

    5We should alert the reader that this is the best one can do at present � given that we
work in minisuperspace, i.e. with a restricted number of degrees of freedom, one must keep
in mind the possibility that additional degrees of freedom might render an acceptable-looking
minisuperspace wave function non-normalisable.

     31
lead to WKB classicality. They can be determined by noting that, in order for
the WKB approximation to be valid, to leading order the wave function must
be an oscillating function. Then, if we go back to the WdW equation in the
presence of a scalar field, Eq. (63), we can identify the following two regimes:

�  Inflation   [30,  31,  32]  (for  a  review  see    [33]):  V () > 0   and    |V, |     
                                                                                   V    < 2.

   A good approximation to inflation is that the scalar field changes little

   while  the  universe    expands      fast,  so  we  can  assume    1    2       2    .  Then  at
                                                                      a2  2        a2
   large scale factor a we are left with the equation

                                       2     2     +   a3V     =0                            (90)
                                     484a    a2

   which admits an oscillating solution,   eia3/.

�  Ekpyrosis   [34]  (for  a   review   see    [35]):  V () < 0  and      |V, |     
                                                                           |V |  > 6.

   An ekpyrotic phase is essentially the complement to inflation. In this case

   the universe is slowly contracting, and the scalar field races down a steep,

   negative potential.     Thus the first approximation is now that                1    2    2   ,
                                                                                   a2  2     a2
   but since the potential is negative we again get an effective equation with

   oscillating solutions,

                                 2         2       -   a3V      = 0.                         (91)
                               84a3        2

Thus, rather surprisingly, the two dynamical models that can potentially explain
the homogeneity, isotropy and flatness of the early universe, while also providing
mechanisms for amplifying quantum fluctuations into seeds of structure, have
the additional property of rendering the universe classical [36]. This can be
traced to the fact that both mechanisms act as dynamical attractors, and we
will discuss this property in more detail in the next section, when discussing
no-boundary solutions.

    The concepts and formalism developed in this section can now be used, and
arguably find their most intriguing application, in the no-boundary proposal �
the main topic of this review, whose exploration we now begin.

3. The No-Boundary Proposal

3.1. Heuristic Motivations

    The no-boundary proposal is a theory of initial conditions for the universe.
It is a complement to our theories of dynamics, such as quantum field theories
or general relativity, which can be seen as describing what kinds of dynamics
are possible. Rather, given a theory of dynamics, the no-boundary proposal has
as its aim to provide a theory for what kind of dynamics is likely, and what is
unlikely. It is a theory for the quantum state of the universe, and it involves
gravity in a crucial way � thus it can only be formulated in quantum gravity.

                                               32
We built up the necessary background in the previous section, but before pro-
ceeding to a more technical discussion, it is useful to provide several heuristic
motivations that explain rather intuitively what the no-boundary proposal is
about.

Avoiding an infinite regression
    Why did the apple fall from the tree? Physics is built on cause and effect.

Thus we might have noticed that a bird tried to grab the apple, and inadver-
tently knocked it out of the tree. But why did the bird try to grab the apple?
Because it was hungry. And why was it hungry? This kind of questioning, taken
sufficiently far, typically ends up with the question: how did the universe begin?

                                                                                today

                                                                what happened here?

                                                                                                South Pole

Figure 13: Left panel: When we investigate the history of our universe, then we have to supply
boundary conditions at ever earlier times. Right panel: The no-boundary proposal cuts off
the potentially infinite regression by stipulating that there was no boundary in the past. This
in itself then provides initial conditions for the evolution of the universe.

    In cosmology, we know that before the current dark energy era, there was
a period of matter domination. And before that one of radiation dominance.
Going back in time, at each transition from a prior phase of evolution, we have
to supply "initial" conditions, which we can think of as being specified on the
boundary of that period of evolution, cf. Fig. 13. This potentially leads to an
infinite regression, where we go to earlier and earlier phases, without end. The
no-boundary proposal may be seen as a way of cutting the Gordian knot, by
stipulating that there was no boundary in the past [1]. Then there is no need to
specify initial conditions at the "beginning" � the fact that there is no boundary
already supplies the required condition.

    An immediate consequence is that the universe is self-contained, both in
space and in time. This is because, if there was a boundary, we could meaning-
fully ask what is on the other side. But if there is no boundary, the universe
can be finite and yet entirely self-contained, just like the surface of a ball. The
analogy with the surface of a ball is in fact rather accurate: in Lorentzian
(pseudo-Riemannian) geometry, it is not possible to round off the geometry of
the universe in such a manner. If one tried, one would run into a spacetime
singularity, which would again constitute a boundary. But if one allows the
geometry of the universe to become Euclidean, then such a smoothing out is
indeed possible. Thus we may foresee that the no-boundary proposal will induce

                                                  33
us to go beyond Lorentzian geometry.

Ground state of the universe and quantum creation
    The way in which the no-boundary proposal is motivated in the seminal

paper [2] by Hartle and Hawking is by drawing an analogy with ground states in
quantum mechanics. Ground states can be defined by considering a Euclidean
path integral, and integrating from configurations of vanishing action in the
infinite (Euclidean) past,

0(x, 0) =                             Dx  e-  1  IE [x(  )]  ,  (92)


where we ignored an overall normalisation factor and where Euclidean time  is

related to physical time via t = -i. The Euclidean action IE is related to the
Lorentzian one via IE = -iS. To see that this defines the ground state, consider
the amplitude for a particle to propagate from (x = 0, t = t) to (x, t = 0),

x, 0 | 0, t = n(x)�n(0) eiEnt                                   (93)
                                                                (94)
                            n

               = Dx eiS[x(t)] .

In the first line we inserted a complete set of energy eigenstates n with energy
En, and the second line is the definition of the amplitude as a path integral.
Then if we Wick rotate t = -i  and take the limit    -, then only the
lowest energy eigenstate will be left, and consequently (94) becomes (92). Thus
an integral from the infinite Euclidean past defines the ground state (vacuum
state) of the system. Put differently, the integration over Euclidean time is an
alternative manner to implement the ground state as initial state.

    We would now like to propose an analogous definition when gravity is in-
cluded. The question then becomes: what should play the role of the infinite
Euclidean past? As discussed by Hartle and Hawking [2], there are two natural
choices that come to mind. One is Euclidean flat space, and the other are com-
pact Euclidean metrics. Euclidean flat space would be more appropriate for a
scattering amplitude, where particles are modelled to come in from infinity and
fly out to infinity again. But in cosmology we are only measuring the universe
at late (finite) times, and we are measuring from the inside of the universe. This
means that the second option, namely summing over compact metrics, is more
appropriate for cosmology, and this is the proposal of Hartle and Hawking. Note
that this prescription then obviates the need to insert an initial state explicitly,
cf. Eq. (8), the idea being that the Euclidean integral puts the universe in its
ground state.

    As we saw in section 2, the wave function is a function of three-dimensional
spatial slices. The path integral over compact metrics may then be seen as an
amplitude from a slice where the 3-dimensional volume goes to zero, to a final

                                      34
slice with metric hij,

                        HH [hij ] = N Dg� e-IE[g� ] ,    (95)

                                                      C

where the integral is over all (inequivalent) compact metrics C that contain a
surface with metric hij. N here is a normalisation factor. This definition may
be given the interpretation of a transition amplitude from zero size to a given
final size, i.e. it can be interpreted as being the amplitude for the universe to
tunnel from nothing (for early incarnations of this idea, see [37, 38, 39]). This
nothing should be thought of as an absolute nothing, i.e. as the absence of space,
time and matter. Incidentally, when matter is included, then the integral is to
be performed over compact metrics and regular field configurations on these
geometries � if the matter configurations were not regular, they would induce
spacetime singularities, which are explicitly avoided here.

    Note that, comparing with (92), the definition (95) cannot be interpreted
as the lowest energy state of the universe. This is because in a closed universe,
energy cannot be defined unambiguously (in general relativity, energy is usually
defined asymptotically, with respect to a fixed reference metric [40]). Rather, the
definition (95) should be seen as defining a state of minimum excitation. Thus
we would expect, and we will see that this is in fact true, that spacetimes with
fewer wrinkles in them come out as preferred over more crumpled spacetimes.
Thus there is the hope that the no-boundary proposal might be able to explain
why the early universe was in such a simple state.

    The idea of describing the origin of the universe as tunnelling out from
nothing was also proposed independently by Vilenkin, and goes by the name
of tunnelling proposal [41, 42, 43]. Conceptually, the two proposals are very
similar, but there are some technical differences that we will discuss in later
sections. Interestingly, the idea that the ground state might be enough to explain
the structure of the universe was also mentioned already by Dirac as early
as 1939, in a lecture6. Dirac's observation was that the quantum mechanical
ground state is not empty, and might ultimately account for all the structure we
see in the universe. This is very close to the modern point of view. The ground
breaking contribution of Hartle and Hawking was to specify how to include
gravity in this scheme.

    We should point out a few immediate consequences of the definition (95),
which at this point remains rather schematic. The first is that the wave func-

    6Here are Dirac's words, delivered on presentation of the James Scott prize in 1939 [44]:
"Let us now return to dynamical questions. With the new cosmology the universe must have
been started off in some very simple way. What, then, becomes of the initial conditions
required by dynamical theory? Plainly there cannot be any, or they must be trivial. We
are left in a situation which would be untenable with the old mechanics. If the universe were
simply the motion which follows from a given scheme of equations of motion with trivial initial
conditions, it could not contain the complexity we observe. Quantum mechanics provides an
escape from the difficulty. It enables us to ascribe the complexity to the quantum jumps, lying
outside the scheme of equations of motion. The quantum jumps now form the uncalculable
part of natural phenomena, to replace the initial conditions of the old mechanistic view."

                                                  35
A  hij(t=0)

tion is real valued, as thobeseirnvetregral is, at least formally, over Eucql1i(4d) ean compact
metrics. We will later discuss how this can nevertheless lead toq1a(3)n operational
definition of probabilities, in the vein of section 2.4. The seconqd1(2) is that, even
though the formal definition describes a sum over Euclidean meqt1(1r) ics, somehow
our Lorentzian universe must come out. As we will see, this is because the
saddle points of the phaystpphearcseuilrnikfaetceegral (95) will turn out to be complex. Third, by
definition the big bang singularity is avoided. This is possible bq0ecause the ge-
ometry is not forced to remain Lorentzian in regions where the universe shrinks
to zero size � rather, the origin of the geometry is viewed more like a point on
the surface of a ball, and sometimes this point is referred to as the "South Pole"
of the geometry, cf. the right panel in Fig. 13.

                                                                             today

                                                                          asymptotically
                                                                                   at

Figure 14: If the initial state were taken to be Euclidean flat space, then in addition to
geometries directly connecting our current universe to that state, there would be topologically
non-trivial configurations in which the early phase pinches off and a new universe forms
from nothing. The conjecture is that such configurations would dominate the path integral,
effectively recovering a sum over purely compact metrics without boundary [45].

The path integral is effectively of no-boundary type anyway
    What if we had chosen a different initial state in the definition (95)? In par-

ticular, what if we had chosen asymptotically Euclidean flat space as "in" state?
Then, apart from geometries that would connect this asymptotic region directly
to the final hypersurface with metric hij, there would also be geometries that
are disconnected, i.e. for which the initial asymptotic Euclidean region would
round off and come to an end, combined with a configuration where a new uni-
verse is nucleated and this then connects to the final hypersurface. In fact, there
would be many more such topologically non-trivial geometries contributing to
the path integral, and they would in all likelihood vastly dominate over the
configurations directly connected to infinity. Hence, there is a conjecture that
effectively this path integral would again reduce to the one where one sums over
compact metrics [45]. This idea is illustrated in Fig. 14.

Finite action
    In physics, the action plays a central role, since for just about all theories

of physical interest the action provides the definition of the theory. It encodes
the classical equations of motion upon variation of the fields and it provides

                                                  36
the weighting for quantum amplitudes, in Feynman's path integral approach.
Thus a natural requirement on any physically sensible theory might be to ask
for the action to be well defined and, in particular, finite (at least at the saddle
points) [46, 47, 48]. This is a crucial condition in ensuring that the theory
makes sense at the semi-classical level. However, such a requirement is far from
trivial. In particular, it immediately rules out the standard hot big bang model,
once quantum corrections are taken into account. Let us briefly review this
argument [48]. We can focus on the best case scenario, where spatial sections
are homogeneous and isotropic, i.e. we can consider a Robertson-Walker (RW)
metric

               ds2 = -N~ 2dt2 + a(t)2        1  dr2    +      r2(d2  +  sin2  d2)     ,          (96)
                                                - kr2

where k  (-1, 0, 1) parameterises the spatial curvature (respectively open,
flat, closed). When quantising gravity, we expect that loop corrections lead to
additional terms in the action, proportional to higher powers of the Riemann
tensor [49] (there can also be terms involving derivatives of the Riemann tensor,
but for simplicity we will ignore these here). In a RW background, such terms
simplify greatly, as there are only two independent non-trivial components of
the Riemann tensor, namely (for i = j, and with no summation over repeated
indices)

               Rij ij    =  a 2 + kN~ 2        A1 ,    R0i0i  =        a�      A2 .              (97)
                              a2N~ 2                                 aN~ 2

The action will be a function f of (positive) powers of these terms only, more
specifically

          S=   d4               (Riemann)       =  22      dtN~ a3           cp1,p2 A1p1 Ap22 ,  (98)
                     x -gf

                                                                     p1 ,p2

where cp1,p2 are coefficients, and the power of the Riemann terms is given by
p1+p2. Now the point is that for a big bang type model, we have in physical time
N~ = 1 that the scale factor goes to zero as some power of time, a(t)  ts with

s  >  0.  But  then  A1  =  s2  +   k   ,  A2  =   s(s-1)  .  Given  that    quantum     corrections
                            t2     t2s                t2
arise at arbitrarily high order, i.e. p1, p2 can be arbitrarily large, the integral

in (98) will diverge (some terms can be eliminated by using a constraint, but

not all [48]) and the action will not be finite. At the semi-classical level, a

Lorentzian big bang is thus ruled out.

   There are few ways known that render the action well defined and finite.

One possibility is quadratic gravity. In the quantisation of quadratic gravity, no

further higher derivative terms appear [50], and hence it is potentially protected

from the problem mentioned above. In fact, inflationary solutions, starting

from zero size, arise with finite action [51]. However, that theory is potentially

plagued by ghosts [52]. Another possibility is to have an emergent phase, that

is to say a phase of asymptotic flatness out of which the universe arose, see e.g.

                                                  37
[53, 54]. However, the previous motivating paragraph has provided a counter
argument, by conjecturing that in such a situation the quantum amplitude would
in fact be dominated by no-boundary geometries.

    This then leads us to the best understood example that ensures finite action,
namely the no-boundary proposal itself. The smooth rounding-off of the geom-
etry, combined with regular matter fields, is the most robust example known to
lead to finite action solutions. Technically, this is due to the Euclidean nature
of the geometry near the South Pole at t = 0 : there, as we will derive in below,
the solution for the scale factor is of the form a(t) = �it + O(t3) with k = +1,
leading to a 2 + k = O(t2) and consequently regularity of the Riemann terms
A1  A2  O(t0) as t  0. This will be discussed in detail in section 5.1.

    All the above motivations lend an air of inevitability to the no-boundary
proposal in semi-classical gravity. That said, a physical theory should not only
be intuitive and offer good explanations, but must first of all be in agreement
with observations. Thus, we should analyse the no-boundary proposal in detail
before passing judgment.

3.2. Simple Inflationary Examples

    We just discussed a series of intuitive arguments suggesting that the wave
function of the universe might be given by a path integral over compact metrics.
Defining such a path integral in general and in detail is rather complicated, and
we will discuss progress that was made towards this goal later on. From the
discussions in section 2 and Appendix C we know that path integrals can be
well approximated by their saddle points, so we may ask a much more tractable
question first: do compact and regular saddle point solutions actually exist?

    The most relevant context for answering this question is that of gravity
coupled to a scalar field  with potential V (), with action

S = d4x-g     R     1                                         
              2     2  g�  �               V  ()     +        d3y hK .  (99)
           M     -                    -

                                                        M

We will again specialise to FLRW backgrounds (10) and a time dependent scalar
field only. It is useful to redefine the time coordinate, via N~ dt = -id. This
means that when  takes real values, it will correspond to Euclidean time. But
it will be useful to consider  to be complex valued in general. The metric
ansatz is then very simple,

                 ds2 = d 2 + a2( )d32 ,                                 (100)

and the Euclidean action IE = -iS becomes

IE = 22          d     -3aa2 - 3a + a3            1  2  +  V  ,         (101)
                                                  2

where   d/d . The equations of motion are

                       +  3  a    -   V,   =  0   ,                     (102)
                             a                                          (103)
                          a
                 a     +  3  2 + V         =0,

                                38
while the constraint, arising from time reparameterisation invariance, is

a2  -  1  =  a2      1  2  -  V  .                                         (104)
             3       2

In cosmology this equation is usually called the Friedmann equation. Using this
equation, we can simplify the action when it is evaluated on a solution of the
equations of motion (this is called the "on-shell" action)

IEon-shell = 42 d -3a + a3V .                                              (105)

    The no-boundary wave function, for now loosely defined via the formal path
integral (cf. (95))

(b, ) = DaD e-IE(a,)             e-IE (b,) ,                               (106)

                     C

depends on b and , the (late-time) values of the scale factor and scalar field
on the final hypersurface. As indicated, we assume that it can be approximated
by (a sum of) saddle point contributions. These saddle points must satisfy a
number of mathematical and physical requirements [55]: evidently, they must
satisfy the equations of motion and constraints. But moreover, we would like
them to be physically meaningful, and for this reason they should yield normal-
isable wave functions. Moreover, they should lead to physically sensible results,
implementing in particular the idea that in the early universe matter fields were
in their ground states. Concretely, we must find out if there exist solutions
(a( ), ( )), satisfying the following conditions [56, 5]:

� The solution must be compact, so somewhere we must have a(0) = 0. Here
   we have shifted the time coordinate such that  = 0 corresponds to the
   South Pole of the solution, cf. again Fig. 13. At this point, the solution
   must also be regular, by which we mean that the fields and their deriva-
   tives must take finite values. The Friedmann equation (104) then implies
   a(0) = �1, expressing the fact that the geometry must be Euclidean at
   the South Pole. The choice of sign for a is important � we will show later
   on that for physical consistency (normalisability) we must choose

             a(0) = +1 .                                                   (107)

The equation of motion (103) then implies that a =  +O( 3). Meanwhile,
the equation of motion for , Eq. (102), shows that regularity implies
the condition (0) = 0. This means that no-boundary solutions can be
characterised/labelled by the value of the scalar field at the South Pole,
SP = (0). This value will be complex in general.

� There must exist a point f in the complex  plane where the fields take
   their specified values b,   R, that is to say that on the final hypersurface
   we must have

a(f ) = b and (f ) = ,                                                     (108)

                 39
       with b,  being the arguments of the wave function. The non-trivial re-
       quirement is that the fields must take the specified values simultaneously.
       If this cannot occur, no solution exists.

Let us add three remarks: first, note that the action IE(b, ) will be evaluated
along a path starting at  = 0 and ending at  = f . The choice of path
is irrelevant, due to Cauchy's theorem, as long as there are no singularities
or branch points present in the complex  plane. Second, the complex time
path we are talking about here has nothing to do with the complex integration
contours (which are contours over the fields) used to define path integrals using
the Picard-Lefschetz method discussed in Appendix C. Rather, we are talking
about a saddle point of such integrals. But this saddle point itself is complex,
and can be represented in different ways using different complex time paths.
These different representations are physically equivalent, since the action is
invariant under changes of path. And third, a note on nomenclature: solutions
of the type specified above, satisfying the no-boundary conditions, are often
called no-boundary instantons. This is a slight abuse of notation, as instantons
usually refer to purely Euclidean (finite-action) solutions. Here the instantons
are typically complex, and for this reason they have also sometimes been called
"fuzzy instantons".

   t plane

               a  =  sin(     +  it)
                           2

                  = cosh t

   a = sin( )

0           /2

Figure 15: The simplest example of a no-boundary instanton corresponds to a section of
complexified de Sitter spacetime, which can be seen as half of a 4-sphere, in purple, glued at
the Hubble radius to half of the Lorentzian de Sitter hyperboloid, in green. The corresponding
path in the complex time plane is shown on the left; here we have set the Hubble radius to
unity.

    Let us start with the simplest example of a no-boundary solution, which
arises when the scalar potential is constant, V = 3H2. In this case the scalar field
is constant, and the solution for the scale factor corresponds to the maximally
symmetric, constant-curvature de Sitter spacetime, with Hubble radius 1/H. In
terms of Euclidean time, the solution is given by

                     a( )        =    1  sin(H )  .  (109)
                                      H

Note that this indeed satisfies a(0) = 0 and a(0) = 1. The 4-sphere reaches
maximum radius at  = /(2H), where the scale factor attains the Hubble
radius a = 1/H. This is the equator of the 4-sphere, onto which we can glue

                                      40
half of the Lorentzian de Sitter solution by continuing in the Lorentzian time
direction,   /(2H) + it, with t  0, so that the scale factor evolves as

                     a   =   1  sin(/2  +    iH t)  =    1  cosh(Ht) .                   (110)
                             H                           H

The chosen complex time path is illustrated in Fig. 15. Along this path the scale
factor takes real values, and thus we can extend the instanton arbitrarily far
into the future, until the desired final value b of the scale factor is reached. The
corresponding final time is explicitly given by f = /(2H) + i arcosh(Hb)/H.
This is the famous Hartle-Hawking instanton, whose "shuttlecock" shape is
shown in Fig. 15. It is the prototype for all no-boundary solutions.

    We can also calculate the action of this solution, using Eq. (105). The result
is straightforwardly found to be7

                         IE  =  42     -1 + i (H2b2 - 1)3/2        ,                     (111)
                                H2

so that the no-boundary wave function becomes approximately

                                   e 42    [1-i (H2b2-1)3/2]  .                          (112)
                                      H 2

If we now think about a series of instantons with successively larger scale factor
values, we see that the phase of the wave function grows roughly in proportion
to the spatial volume b3, while the amplitude remains constant. Thus, using
the results of section 2.4, we can assign a relative probability

                                                 e 82                                    (113)
                                                    H 2

to the corresponding classical history. Of course, in the present case this is

a rather trivial statement, as there is only a single history, corresponding to

the expanding de Sitter spacetime. However, we could imagine a potential

with several approximately flat regions at different potential heights V = 3H2,

i.e. we could imagine that H could vary. Wherever the potential is very flat,

solutions such as the one above would exist, with their corresponding classical

histories. Then we can see an important feature of the no-boundary proposal:

smaller potential values come out as preferred. The implications of this will be

discussed in section 4.

New features enter when we include a non-trivial scalar potential. The

simplest  potential  to  consider  is  that  of  a  mass    term,  V ()  =  1  m2  2  .  Current
                                                                            2
observations [57] disfavour this model of inflation, but it remains very useful

as an example of no-boundary solutions that can be approximated analytically.

    7The easiest way to represent the solution, and to calculate the action, is to use the
complex time path which combines a Euclidean and a Lorentzian segment. But if one prefers
a smoother representation, without the 90 degree turn in the complex time plane, then one is
in principle free to choose a path that links  = 0 to f in a smooth, infinitely differentiable,
manner.

                                                  41
This was first done in [58] (see also [59] and the generalisation to generic slow-
roll models in [60]). To understand the nature of solutions, it is useful to first
work out a series expansion near the South Pole, imposing the no-boundary
conditions a(0) = 0 and a(0) = 1. This yields

                          a( )  =     -    1     m2  S2 P   3  +  O( 5)      ,              (114)
                                           36                                               (115)

                          ( )   =  SP      +     1  m2  SP     2  +    O( 4) ,
                                                 8

which shows that the entire solution depends on a single parameter, namely

the scalar field value at the South Pole, SP . As we will see momentarily, this
must typically be taken to be complex. However, the analytic approximation

is most accurate when SP is almost real and large, hence we will assume
|ISP |  1  |RSP |, where we are denoting real and imaginary parts by the
superscripts R, I.

    Near the South Pole,  remains approximately constant, and thus Eq. (103)

implies that the corresponding solution for a is given by a sinus function,

                                               mSRP 
                                 6                 6
                       a     mRSP    sin                                 RSP .              (116)

This is again approximately the solution for a 4-sphere with radius determined

by the location of the scalarfield on the potential. The equator of the 4-sphere
                       mRax          6  
is  reached  at  time        =  mSRP    2  .  In  fact,  the   series     expansion  (115)  shows  that

 remains constant up to this point with fractional error 1/(SRP )2.

    We can also find an approximate solution when a is large. This is noth-

ing other than the usual slow-roll approximation for inflationary solutions, but

expressed in Euclidean time,

                                a( )       a e-i m SP    6     +  m2   2  ,                 (117)
                                                                    6                       (118)
                                              0

                                ( )  SP + i                 2  m  .
                                                            3

The scalar field slowly rolls down the potential, to good approximation linearly
with time, while the scale factor expands exponentially when evolving in the
imaginary  direction (that is to say, in Lorentzian time). This approximate
solution is valid until the second term in the exponent for a overtakes the first
term, i.e. until  I  SRP /m.

    There is an important feature to the scalar field solution (118), which is that
when we move in the imaginary  direction, then the imaginary part of  does
not change anymore. We can use this property to match onto a desired real
value  at late times. Also, the late time solution for a will remain approxi-
mately real, when matched to the equator of the 4-sphere solution at small a.
Thus, matching at  R = mRax, we obtain a (approximately) real solution at late

                                                    42
Lorentzian times if we choose (cf. (116) and (118))

                                                        2
                           i6                           3                    
                    a0    mSRP  ,        SI P = -            mmRax    =  - SRP  ,          (119)

which refines the expression for  in (116). One obvious lesson of this is that the

scalar field must be complex at the South Pole in order for it to reach real values

at a late time. This demonstrates explicitly the earlier claim that no-boundary

instantons are typically complex.

We can also approximate the action of these solutions, by using (105). The

integral   from     =0    to  mRax  yields  a   real  value  IER      - 242    for    the  Euclidean

                                                                         m2 2
on-shell action. For the integral along the Lorentzian direction up to f , one can

neglect the term linear in a in (105), since the scale factor becomes exponentially

large. Then one may approximate it as follows,

           f                                                             2            d
                                           d ma2 6a = 22                 3            d
       22         d m22a3 = 22                                                 d   m       (a3)

           m Rax

                                                              22         2  mb3    ,       (120)
                                                                         3

where we assumed slow-roll in the last step. The total contribution of this

instanton to the wave function is thus

                                               122      22
                                            e . V ()
                              (b, )                 -i       2   mb3                       (121)
                                                             3

We find again that low values of the potential come out as preferred, and that
the phase grows in proportion to the spatial volume.

    Note that the wave function is of WKB form, which we recall is a prerequisite
for a probabilistic interpretation, as discussed in section 2.4. It is fairly obvious
by inspection, as the weighting does not depend on the scale factor b while the
phase grows very fast as the universe expands. Nevertheless, we may calculate
this more precisely, using (I)2 = GABAIBI and Gbb = -122b, G =
22b3,

                                       (IER)2           1        ,                         (122)
                                       (IEI )2      m68b6

which is indeed driven to tiny values.

The histories implied by the wave function, i.e. the sequences of (b, ) values

with constant weighting, are in fact those classical solutions that the instantons

approach at late times. Explicitly, they can be obtained by eliminating  from

(117) and (118), resulting in


                                          i6
                                         mRSP         (S2 P  -2
                                    b           e , 1            )                         (123)
                                                   4

and they correspond to an approximately fixed scalar field value SP = RSP -
i
       at the South Pole.       What is important to point out here is that these
  SRP

                                                43
histories are parameterised by a single real parameter, namely RSP , whereas
general classical solutions would have been parameterised by two real param-

eters. This shows one aspect of the predictivity of the no-boundary proposal,

namely that it restricts the possible solutions to a theory. In other words, not

all (b, ) combinations may arise, only those that can be related as in (123).

Having analytically demonstrated the existence of no-boundary saddle points

in a simple inflationary model, we will end this section with a few remarks

regarding the consistency of the no-boundary framework. An obvious point is

that no-boundary solutions actually exist. They have finite action, as seen in

(121), and lead to the prediction of classical expanding universes. These saddle

point solutions are everywhere regular, but what is more, the curvature does

not become large. In fact the spacetime curvature is roughly constant, as these

solutions are close to pure de Sitter spacetime. This means that the curvature


radius is given by the Hubble radius,  3/V (RSP ) = 6/(mSRP ). Hence if

the potential energy is well below the Planck scale, then the curvature radius

RH of the instantons is correspondingly larger than the Planck length lP l. This

means that the expected higher curvature corrections, arising from quantum

corrections to the action, will be suppressed by positive powers of lP l/RH  1.

A final point of importance is the sign choice that we made in (107). If we

had chosen the opposite sign, then we would have found essentially the same

solutions, but the Euclidean action would have come out with the opposite sign

(this alternative sign choice is the one made in the tunnelling proposal [41]).

This would have flipped the relative probabilities, e.g. in (113) we would have

              82
              H 2
obtained      e . -  Then high values of the potential would have been

preferred instead of low values. We will discuss this further in section 4, and

derive the statements that we make here. For now, let us just state the result,

which is that with the alternative choice of sign, perturbations around these

solutions are unstable, in the sense that solutions with large perturbations are

more likely than solutions with small perturbations. Thus, the whole approxi-

mation framework of starting with FLRW metrics becomes inconsistent. With

the choice of sign that we made here, and which was advocated for these rea-

sons by Hartle and Hawking from the inception of the no-boundary proposal,

perturbations are suppressed and the framework is consistent.

3.3. Numerical Techniques

    In the previous section we demonstrated the existence of (inflationary) no-
boundary saddle points, by using analytic approximations in a simple model
containing a massive scalar field. For general potentials, it is however impossible
to find explicit no-boundary solutions by analytic methods. In such cases, we
have to resort to numerical methods. We will describe these here, and show
that they can easily produce large numbers of no-boundary solutions. Moreover,
they have the advantage of being able to access parameter regions that were not
reachable by the approximations made in the previous subsection.

    The strategy for finding numerical no-boundary solutions is as follows [61, 5].

                     44
      30                                                      30                                       

      25                                                      25

      20                                                      20

      15                                                      15

      10                                 Re(a)                10                       Re()

      5                                                       5

         SP                                                      SP

      0                                                       0

          0     2        4           6         8      10          0     2           4      6        8    10

Figure 16: These figures show the complexified  plane, on the left for the scale factor

and on the right for the scalar field. The dark lines show the locus where the fields take real

values (more precisely, the figures show a density plot of log |Im(a( ), ( ))| for a dense grid of

values of  ). The red arrows indicate a useful contour of integration, used in the optimisation

procedure needed to find numerical no-boundary solutions. The present figures show what

this looks like when the desired solution has not been reached yet: the dark lines, where scale

factor and scalar field are real, are located in different regions of the complex  plane. For

this  example,  V ()  =     1  m2  2  ,  m  =  1/10,  and  we     used  the  trial  value  SP    =  6.5 - 0.3i.  The
                            2
values reached at r  6.58 + 22i are a  376 and   4.99 + 0.25i.

      30                                                      30                                       

      25                                                      25

      20                                 a(f)=b               20                              (f)=

      15                                                      15

      10                                                      10

      5                                                       5

      0                        Xopt                           0                            Xopt

          0     2        4           6         8      10          0     2           4      6        8    10

Figure 17: Now we show the same model, but with optimised values SP  6.451 - 0.5037i.
The real a and real  lines now (asymptotically) overlap and a no-boundary solution is ob-
tained. More precisely, the real values b = 300 and  = 5 are obtained at f  5.943 + 21.34i.

                                                          45
First we can choose a value for the scalar field at the South Pole,

           SP = SRP + iSI P = |SP |ei ,                                          (124)

where we will sometimes use a polar representation with argument . It is useful
to start with a value of RSP or |SP | that lies in a region of the potential where
inflationary solutions may be expected to be found, i.e. in a relatively flat
region of the potential � this will make it easier to find the first solution. Then
one should integrate the equations of motion (103) and (102) from the South
Pole, along a chosen contour in the complexified  plane. The South Pole is a
regular singular point, hence one cannot integrate directly from it, but rather
from somewhere close by. This can be done to arbitrary numerical precision,
using the series expansion of no-boundary solutions near the South Pole,

a( )  =    -  V               3  +  8V    2 - 27V,2  5  +   O( 7) ,              (125)
              18                           8640                                  (126)

( )   =  SP   +             V,      2  +  2V     V,  + 3V,  V,    4  +  O( 6) .
                             8                       576

This series expansion is derived by imposing the regularity conditions at  = 0

that were described in section 3.2. In practice, it is useful to start the integration

at  = , with || of order 10-5 or even smaller. The integration contour should

be chosen for convenience. One choice that works well is to integrate first in the

imaginary  direction, followed by a segment in the real  direction, see Fig. 16.

A contour of this shape typically allows one to cross the locus where the scale

factor takes real values, let us denote this point as r. However, the scalar field
will in general not be real at this location, but will take a complex value. The

idea now is to tune the four real parameters SP , r such that one reaches

Re(a) = b, Im(a) = 0, Re() = , Im() = 0 to the desired accuracy. The

tuning can be done by using a Newtonian algorithm, which can straightforwardly

be implemented in such a higher-dimensional parameter space. However, some

trial and error is typically required at first, in order to already find oneself in

the basin of attraction of the solution. Here it is useful to choose target values b

and  that are close to the values a(r) and Re[(r)]. The result of a successful

optimisation is shown in Fig. 17, where the endpoint, at which the fields reach

the real values b, , is now denoted as f .

In Fig. 18 we also plot the field values for the optimised solution, but now

following the more standard contour where we evolve in the Euclidean direction

first, up to Xopt  Re(f ), and then in the Lorentzian direction up to f . Note

that the imaginary parts of the fields quickly decay along the Lorentzian part

of the contour. We can also compare the optimised values with the analytic

estimates of the previous section. There we had found that ISP = -/SRP .

Here we would thus expect SP     =     5-  5  i      5-0.63i, whereas the optimised value

we obtained was SP  6.451 - 0.5037i. The discrepancy can be attributed to

the fact that the scalar field value is not very large here, whereas an assumption

in section 3.2 was that SRP  1. But this is the advantage of the numerical
method, that one can find solutions in regions of the potential where analytic

estimates don't work well.

                                              46
300                                            6                              Re()

250     1000*Im(a)                             4

200                           Re(a)            2

150                                                        Xopt                     

100                                            -2       5        10 15 20 25

50      Xopt                                   -4

                                                           10*Im()

     5        10 15 20 25                      -6

Figure 18: Here we show the field values of the optimised instanton from Fig. 17, along the
path indicated by the dotted line in that figure. The path first evolves from the South Pole in
the Euclidean direction to Xopt  5.943, and then in the Lorentzian direction up to f .  is
a parameter along the path. The left panel shows the real and imaginary values of the scale
factor, while the right panel is for the scalar field. The imaginary parts have been enhanced
for better viewing. Note that the fields become real at the final time, and reach the desired
values b = 300,  = 5.

    Optimised no-boundary solutions typically exhibit another feature, clearly
visible in Fig. 17: there exist lines at constant X along which the scale factor
and the scalar field remain approximately real when evolving in the imaginary
(Lorentzian) time direction. This is due to the inflationary attractor, which has
pulled one close to a classical solution of the equations of motion. However,
strictly speaking, if the scalar field is not residing at an extremum of the po-
tential (where the instanton is pure de Sitter spacetime), the scale factor and
the scalar field only take the real values b and  simultaneously at one location
f , and not along a line segment. Still, due to the inflationary attractor, values
of b,  that are related by classical evolution will correspond to instantons with
essentially the same optimised SP , X = Re(f ) values, and will only differ in
the Lorentzian time location Im(f ) where the final field values are reached.
Also, quite generally, once one has found the first such no-boundary solution,
one can usually easily find nearby solutions with slightly different b,  values,
even when they belong to different classical histories. This allows us to gain a
more global understanding of the existence of solutions.

    Before embarking on this task, let us note a simplification: in order to
perform the numerical calculations, we can scale the potential to an arbitrary
overall normalisation. Indeed, starting from the Euclidean action

        SE = -         d4xg          R  -   1  g�  �             -  V  ()  ,        (127)
                                     2      2

we can perform the scalings (with constant V0)

                � , V  V0V� , g�  V0-1g�� ,                                         (128)
                                                                                    (129)
which result in a new action

        SE    =     1         d4xg�     R�  -  1   g��  ��       �  -  V�  .
                 -                      2      2

                   V0

                                        47
Now the overall scale of the potential appears out front. In fact, this scaling is
not only useful for the numerics, but it also explains the functional dependence
of the wave function on the potential, cf. Eqs. (113) and (121). We will make
use of this scaling freedom below.

                                                                               2500
12

10                                                                                      2000

8
                                                                              1500

6
                                                                              1000

4

                                                                               500
2
V
                                                                               2 Re SE

00         10  20    30        40                                                       00             20  40  60  80

                                                                                                           SP

Figure 19: Left panel: A toy inflationary landscape potential of the form (130). It contains a
plateau region at small field values, and a power law region at large field values. It is normalised
here such that V (0) = 1. This potential serves to illustrate general features of (inflationary)
no-boundary solutions in a potential landscape. Right panel: For the no-boundary solutions in
Fig. 20, we show here the weighting of the action, i.e. the logarithm of the relative probability,
again as a function of |SP |. The dotted lines represent the approximation of the instanton
by a pure de Sitter solution. Low values of the potential come out as preferred. Figures
reproduced from [62].

A model that serves well to illustrate the properties of inflationary no-

boundary solutions is a toy model for a potential energy landscape, with poten-

tial [62]                          1
                                   v4
                         V ()  =                                                        (2    -  v2)2  .               (130)

The potential is illustrated in the left panel of Fig. 19. It consists of two inequiv-
alent inflationary regions, one of plateau type at small , and an approximately
quartic potential at large , with a potential minimum in between. This poten-
tial admits no-boundary solutions in both inflationary regions. The optimised
scalar field values at the South Pole are shown in Fig. 20. Perhaps the most
important thing to note about this figure is that no-boundary solutions do not
exist everywhere on the potential. Rather, when the potential becomes too steep
to support a prolonged inflationary phase, no-boundary solutions cease to exist.
This occurs near the potential minimum at  = 20, and arises because there
is no dynamical attractor at play there, which could drive the solution towards
a classical solution of the equations of motion. In other words, when there is
no attractor, it becomes impossible for the scale factor and scalar field to si-
multaneously become real valued, while also satisfying the regularity conditions
at the South Pole (which, we should recall, require the scalar field to start out

                                   48
with a complex value, cf. (119)). We will discuss the attractor in more detail
in section 3.5.

0.10                                                                                               5

                                                                                      4
0.05

                                                                                      3
0.00

                                                                                      2

0.05
                                                                                      1
 Arg SP
                                                                                        2 Htop X 

0.100  20  40  60         80                                                                       00  20            40  60  80

           SP                                                                                                        SP

Figure 20: For no-boundary solutions in the potential in Fig. 19, we show plots of the
optimised phase  at the South Pole (left panel) and the location X where real values are
reached at late times (right panel), both as a function of |SP |. Here we chose v = 20 while
X is expressed in terms of Htop  V ( = 0)/3 = 1/ 3. All results can be scaled to any
overall scale of the potential using Eqs. (128). Figures reproduced from [62].

    For these solutions, one can also calculate the action. The most interesting
part is the weighting, i.e. the imaginary part of the action (or equivalently
minus the real part of the Euclidean action), and this is shown in the right
panel of Fig. 19. Note that the approximation

               ln   =  -  2   SER  =                                                                      242     ,          (131)
                                                                                                       V (|SP |)

adapted from the pure de Sitter case in (113) and indicated by the dotted
lines, works very well. As one can see, lower values of the potential come out
as preferred. This means that the plateau region of the potential (at small
) is preferred over the power law region at large . This is in good qualitative
agreement with observations of the cosmic microwave background [63]. However,
we should also point out that within each inflationary region, starting lower on
the potential is again preferred, so that short inflationary phases come out as
preferred over long ones, which leads to some tension with observations. A
detailed comparison with observations will be the subject of section 4.

3.4. Ekpyrotic Examples

    The numerical techniques that we just described can also be used to find
no-boundary instantons of a very different type, namely in ekpyrotic theories
containing a steep and negative potential for the scalar field. In such models, the
ekpyrotic phase, during which the universe slowly contracts, plays an analogous
role to the inflationary phase and replaces it [34, 64]. A contracting phase

                              49
with high pressure (in fact with pressure larger than the energy density) has the
effect of rendering the universe homogeneous, isotropic and flat. Moreover, if one
adds a second scalar field, such models can also generate density perturbations
in agreement with observations of the cosmic microwave background [65, 66].
The least understood aspect of these models is how they link the contracting
phase with a subsequent hot expanding phase, but for progress on this issue see
[67].

    It may sound surprising to look for no-boundary solutions when the universe
is supposed to contract rather than expand � how can a contracting universe
arise from nothing? But one has to keep in mind that the South Pole region of
no-boundary solutions does not correspond to a classical spacetime. The idea,
roughly speaking, is that Euclidean space is generated from nothing and then
turns into a Lorentzian spacetime as the universe contracts [68].

           0                           0

-1.� 10-9     V()                  -1.� 10-9   V()
-2.� 10-9                          -2.� 10-9
-3.� 10-9
-4.� 10-9                          -3.� 10-9
-5.� 10-9
                                   -4.� 10-9

                                    -5.� 10-9       

-1.0 -0.8 -0.6 -0.4 -0.2 0.0  0.2      -2.0 -1.5 -1.0 -0.5 0.0 0.5 1.0 1.5

Figure 21: Representative shapes of ekpyrotic (left) and cyclic (right) scalar field potentials.
In the cyclic case, the ekpyrotic part of the potential is sandwiched between a bounce phase
at more negative  values, and a dark energy plateau at positive .

A simple example of an ekpyrotic potential is a negative exponential,

                              V () = V0e-c ,                           (132)


where we take V0 < 0 and c > 6. The latter condition ensures that the

contracting solution is an attractor, cf. section 3.5. Using analogous techniques

to those of the previous section, one may then tune the values of the scalar field

at the South Pole in order to obtain simultaneously real b,  values of the scale

factor and scalar field as the universe contracts. An example is shown in Fig. 22,

taken from [62]. Note that one has to use a somewhat different contour in the

complex time plane to find such solutions (the field values along the indicated

contour are shown in Fig. 23): from the South Pole, the contour first has to

run in the negative imaginary direction. Along this part of the contour, the

solution corresponds to a portion of a large 4-sphere, with a()  -i. Then

the contour runs in the Euclidean direction, and the fields are fully complex

there. Finally, the contour runs in the Lorentzian time direction, and it is along

this segment that the fields become real valued. As one can see from Fig. 23, the

scale factor is shrinking there while the scalar field rolls down the potential fast.

In this simple model, no bounce is included, and hence the evolution necessarily

ends in a crunch. This is also the reason why one cannot see a long vertical

time segment in Fig. 22 along which both the scale factor and scalar field are

                                   50
real to high precision: the crunch occurs shortly after the fields have reached
real values.

          SP                                   SP                        

0.0                                  0.0

0.2                                  0.2

0.4                                  0.4

0.6                     crunch       0.6                         crunch

0.8                                  0.8

     0.0      0.5  1.0          1.5       0.0          0.5  1.0          1.5

Figure 22: An example of an ekpyrotic instanton. The coloured arrowsindicate a contour of
integration that proves useful in finding solutions of this type. Here c = 8 and the optimised
South Pole value is SP = 0.000 - 1.481i. Dark lines again show the locus of real field values,
cf. Figs. 16 and 17. Figures reproduced from [62].

    The action for these solutions can be calculated numerically, and is found to
take a functional form that is very closely related to the one in the inflationary
case, in particular one finds for the weighting that

                                                 s  ,                    (133)

                                     e |V (SP )|

where s is a positive numerical factor that depends on the steepness of the
potential [68]. This implies that ekpyrotic instantons receive a very high proba-
bility if they start high up on the potential. Thus, in contrast to the inflationary
case, a large number of e-folds of ekpyrosis comes out as preferred.

    The overall shape of ekpyrotic no-boundary solutions is shown in Fig. 24,
and it takes the shape of a decanter. In the figure, it is imagined that a bounce
into an expanding phase actually takes place. In [69] a ghost condensate model
of a bounce was included, because it is a simple example of how to model a
classical bounce. In this case, no-boundary instantons with this shape indeed
arise. However, the ghost condensate model is known to contain instabilities
[70], and thus is not consistent on a quantum level. This is in fact the main
problem with classical bounces. In all cases that are known to date, they occur in
theories that also allow for unstable solutions (even if the bounce solution itself
is stable). It remains unclear whether one may consistently treat such theories
as quantum theories, since fluctuations away from the solution of interest might
be able to reach unstable solutions. Thus it remains unknown whether quantum
gravity allows cosmic bounces or not. Note that this question is also important
in assessing whether one of the heuristic motivations given in section 3.1 holds
up, namely whether the quantum wave function is effectively of (inflationary)

                                     51
                                              Re 

1.0                                      0.0

0.5                                      0.5

                  Re a                   1.0
0.0                                                       Im 

                  Im a                   1.5
0.5
                                         2.0

                                         2.5

1.0

0.0  0.5                1.0    1.5  2.0  0.0  0.5              1.0    1.5  2.0


Figure 23: The evolution of the scale factor and scalar field for the ekpyrotic instanton shown
in Fig. 22, along the contour indicated in that figure. Note that along the final segment (in
red), the fields become increasingly real as the universe contracts and the scalar rolls down
the potential. Figures reproduced from [62].

no-boundary type even when the universe has an asymptotic flat region to the
past, cf. again Fig. 14.

    If bounces do make sense, then there exists another possibility for no-boundary
solutions, this time in cyclic extensions of the ekpyrotic model [71]. In those
extensions, there exists a positive plateau region in the potential, where the
current dark energy phase takes place. In the far future, the dark energy decays
and the universe contracts in a renewed ekpyrotic phase. Then the universe
bounces again into a hot big bang phase, followed by dark energy, and another
cycle starts. For a potential of this type, it is possible to find no-boundary
solutions that start in the dark energy phase [62]. This has the advantage of
leading to vastly higher probabilities, since the potential is very low there, cf.
(113). However, this possibility, in the same way as all the other possibilities
discussed in this section, hinges on the viability of cosmic bounces in quantum
gravity.

    The examples of this section highlight an important point, which is that the
no-boundary proposal is a theory of initial conditions that is independent of
the dynamics, in particular it is logically independent of inflation. Rather, it
can be applied to any dynamical model of the universe. However, as we will
discuss in more detail now, whether no-boundary saddle points exist depends
rather crucially on whether or not the dynamical theory in question exhibits an
attractor.

3.5. Classical Histories from the No-Boundary Wave Function

    We have encountered two separate classes of no-boundary solutions so far,
those of inflationary and those of ekpyrotic type. In both cases, satisfying both
the no-boundary conditions and the late-time reality conditions on the fields

                                         52
                            SP

Figure 24: A cartoon of the shape of ekpyrotic instantons. A large Euclidean space is created
from nothing, starting from the South Pole. Then, as the universe contracts, the spacetime
and scalar field become classical and real valued. In the figure, a bounce into the expanding
phase of the universe is indicated. Figure reproduced from [62].

depended crucially on the presence of a dynamical attractor. Since this is such
a basic requirement, it is useful to make it somewhat more precise.

    We can proceed analytically by focusing on models with constant equation
of state. Such models arise when the scalar potential is of exponential form

               V () = V0e-c .                                   (134)

Assuming a flat Robertson-Walker background ds2 = -dt2 + a(t)2dx2, the
equation of motion and constraint read

� + 3H - cV = 0 ,                    3H 2  =  1   2   +V  ,     (135)
                                              2

where H = a /a. They admit a scaling solution, given by

               a(t)  =  a0  |t|   2  ,  H  =      2   ,         (136)
                                 c2              c2t            (137)

(t)  =  1  ln    c4V0       t2       ,  V  =  12 - 2c2       .
        c      12 - 2c2                         c4t2

In the above relations, we have combined two cases: when V0 > 0, we assume

t > 0 and this corresponds to an expanding, inflationary, accelerating solution
when c2 < 2. Meanwhile, when V0 < 0, we take t < 0 and then this corresponds

to a contracting, ekpyrotic solution where we will momentarily see that we must
take c2 > 6. These solutions are called scaling solutions since all the terms in
the equation of motion and constraint scale in the same way, as t-2. If we had
added a spatial curvature term �1/a2 to the constraint in (135), then it would

                        53
have become increasingly subdominant, which justifies our neglect of this term
from the start. The equation of state w is given by the ratio of pressure to
energy density,

                            w    =     p  =  1   2  -  V   =     c2    -   1,                             (138)
                                             2                   3

                                             1   2  +  V
                                             2

and  it  is  indeed  constant,   as  advertised     above.       In    the    inflationary       case  w  <  -  1  ,
                                                                                                                3
while for ekpyrosis we have w > 1.

We can now perturb this solution to assess its stability. In what should be

obvious notation, we obtain

         � + 3 H + 3H  + c2V  = 0 , 6H H =   - cV  ,                                                      (139)

which can be combined into

                         �  +    3H (1    +    2    )     +  c2     V         =   0  .                    (140)
                                             6H 2            2

This equation is solved by

                                                t-1,   t1-    6  .                                        (141)
                                                             c2

The first solution simply corresponds to a shift in initial conditions, cf. (137),

so only the second solution is relevant. From (139), it implies that the fractional

change   in  the  scale  factor  also  evolves  as     a      t1-       6  .  Hence     the   scaling  solution
                                                       a               c2

is an attractor if either the universe is expanding and c2 < 6, or if the universe

is contracting and c2 > 6 [72]. Thus it is an attractor in both the inflationary

and ekpyrotic cases. This is the important property that allows one to reach

real values for the scale factor and scalar field simultaneously, and thus allows

for classicality at late times.

We can even be a little more precise, and derive just how fast the wave

function reaches WKB form [62, 36]. For this it is helpful to realise that, when

the potential is exponential, the action transforms in a simple manner under

shifts of the scalar field. Taking the Euclidean action as the starting point,

                  SE = -    d4xg             R  -   1  g�  �               -   V0e-c          ,           (142)
                                             2      2

one can shift the scalar and perform a related scaling of the metric, thereby
extending the scaling (128),

                            � +  ,                  g�        ec       g��     ,                          (143)
                                                              |V0|                                        (144)

to find that the action has transformed into

             SE      =     ec        d4xg�      R�     -  1  g��    ��        �         e-c�     ,
                         - |V0|                 2         2

                                                   54
where the  sign in front of the potential corresponds to the inflationary resp.
ekpyrotic case. To avoid cluttering due to absolute value signs, we will now
continue the calculation for the inflationary case only, but the ekpyrotic case
works analogously.

    We will set V0 = 1, so that the transformed theory retains the same potential,
i.e. the transformation leaves us in the same theory. Then the relations (143)
imply that the field equations are invariant under

                     a�(t�) = ec/2 a e-c /2t� ,                                              (145)
                     �(t�) =  e-c /2t� +  ,                                                  (146)

where overbars denote the transformed quantities. Under this transformation,
the scaling solution (136), (137) morphs into

a� = a�0 (t�)2/c2 ,  a�0 = exp  (c2 - 2)             a0 ,     V (�)     =  12 - 2c2  1    ,  (147)
                                      2c                                       c4    t�2

which shows that a0 is a constant of motion,

                     a0 = a             12  c4       V  1/c2                                 (148)
                                            - 2c2
                                                              .

This means that we can label different solutions by their value of a0.
    As argued above, at late Lorentzian times, the attractor pulls the solution

close to a real classical solution, and thus the imaginary part of the Euclidean
action scales as (with d = idt)

         SEI  i      dt a3 V            i  a03  (t)-1+   6    i a03  V  1  -   3  .          (149)
                                                        c2              2     c2

Using the constant of motion (148), one can thus determine the dependence on
the final values b,  to be

                                SEI  i b3 V ()1/2 .                                          (150)

Meanwhile, the scaling of the real part of the Euclidean action is governed by
the scaling/shift symmetry, and from (144) we obtain

                                                a�0     2c2
                                                a0
                     S�ER = ec SR =                     c2-2 SER ,                           (151)

so that                         2c2

                     SER        a c2-2          2c2           2  .                           (152)
                                         b c2-2 V () c2-2
                                  0

    Now it becomes straightforward to work out the WKB condition (76), which
says that the amplitude of the wave function should vary slowly compared to its

                                            55
phase. Recalling that (I)2 = GABAIBI with Gbb = -122b, G = 22b3,
we obtain

(SER)2     -3b V 4c2    4
(SEI )2       c2 -2  c2 -2
                             bc2-6 .
           b3V                        (153)

Thus we see a confirmation that classicality is reached under the same conditions
under which we had found a dynamical attractor, namely either for an expanding
universe with c2 < 6, or for a contracting one with c2 > 6. Given that during
inflation the scale factor expands exponentially fast, we may also infer that
classicality is obtained exponentially quickly.

    What is interesting is that this is a purely dynamical way of obtaining classi-
calisation. The usual procedure in quantum mechanics is to invoke decoherence
[73, 74], i.e. the loss of quantum coherence due to interactions of a system with
its environment. Such a process is highly relevant on Earth, where interactions
are extremely common. But it is not available at the creation of the universe, for
two reasons: on the one hand, there is no environment as the universe contains
everything by definition, and is still empty. And on the other hand decoherence
is a process that happens over time, while here we must first address the clas-
sicalisation of space and time. In other words: once time has become classical,
decoherence can take place. Here we have just seen how time (and space) can
become classical in the first place, purely due to cosmological dynamics. In this
way, the no-boundary proposal can explain the classicality of the early universe.

3.6. Implementations in Minisuperspace

    So far we looked only at saddle points, i.e. at (usually complex) solutions
of the classical equations of motion satisfying the no-boundary conditions (107)
and (108). It is reassuring that such saddle points exist, but can we do better?
What exactly are the saddle points approximating? Can we refine the heuristic
definition (95) and define the no-boundary path integral more precisely? In
doing so, there are a number of issues that must be faced:

    � Gravity is not renormalisable, which means that we expect an infinite
       number of correction terms involving ever higher powers of the Riemann
       tensor and ever higher numbers of derivatives. This might however still
       be fine, as long as the curvature remains well below the Planck scale.
       At least for the saddle points we looked at so far, this happened to be
       true: they all had curvatures on the order of the Hubble scale in the early
       universe, which for inflationary examples is constrained by observations
       to be H/MP l  10-5 [57]. Under such circumstances, we may expect the
       path integral to yield reliable semi-classical results (see e.g. [75] and also
       section 5.1).

    � The path integral involves the action, which is integrated over ranges of
       coordinates. Hence, even though the idea of the no-boundary proposal
       consists of the notion that there should be no boundary to the past, we

           56
must still integrate from somewhere, i.e. we must still impose some form
of boundary conditions. The (somewhat Zen-flavoured) question then is:
which boundary conditions correspond best to no-boundary conditions?

� The no-boundary condition that we imposed for saddle points cannot be
   imposed as a condition on the full path integral, as it is in conflict with the
   uncertainty principle. This is because it is a condition on both the field
   value a( = 0) = 0, ensuring compactness, and on the velocity/expansion
   rate a( = 0) = 1, ensuring regularity. Thus we cannot define a path
   integral that sums over metrics that are both compact and regular. It has
   to be one or the other, or perhaps a condition on a linear combination
   of field value and momentum. Note that imposing compactness will not
   guarantee that the saddle points turn out to also be regular, and vice
   versa. We will have to check this at the end of the calculation.

� In the action for gravity coupled to matter, the kinetic term for the scale
   factor of the universe enters with a different sign than all of the other
   kinetic terms, both those of anisotropic components of the metric and
   those of matter fields,

S  dt  - 3aa 2  +  1  a3   2  +  �  �  �  (154)
                   2

This is known as the conformal mode problem, so-called because the scale
factor can be seen as the conformal mode of spatial sections. If the path
integral is defined as a Euclidean integral, then the integrand will thus
be unbounded above and below, regardless of the overall choice of sign.
Hence it is doubtful that the Euclidean path integral might make sense.
A Lorentzian path integral seems more promising as it would not have
this problem (by being a sum over phases), but there we have the issue
that the integral is only conditionally convergent and it has to be defined
carefully to make its meaning unambiguous.

� In situations where several no-boundary saddle points exist, is the defi-
   nition of the path integral unique [76]? Does it uniquely specify which
   saddle points contribute to the wave function, and which do not?

� Finally, it should be expected that the general sum over 4-manifolds is very
   difficult to make precise. One has the freedom to sum over metrics that
   can differ at all spacetime points. Moreover, in analogy with the paths
   integrated over in quantum mechanics (see e.g. [6]), one might expect the
   required manifolds in general not to be differentiable anywhere. What is
   more, even the topology of 4-manifolds remains ill understood. Hence
   it seems difficult at present to properly define a sum over 4-manifolds.
   We will take a more pragmatic approach, and restrict to metrics that have
   certain symmetries, in particular cosmologically relevant symmetries. This
   is the framework of minisuperspace, where the metric is parameterised by
   a finite number of functions of time. One may object to this on the basis

       57
that we are neglecting infinitely many degrees of freedom, and what is
worse, we are setting both these degrees of freedom and their conjugate
momenta to zero simultaneously. Nevertheless, we know from observations
that the early universe was highly symmetric. Hence, we should expect a
realistic theory of initial conditions to predict high probability for precisely
these minisuperspace kinds of metrics. What is crucial then is to check
at the end of our calculations whether or not metrics that are perturbed
around the minisuperspace representation come out as suppressed. If so,
then we may have confidence in our calculations, and justifiably refer to
minisuperspace as an "approximation".

Dirichlet boundary condition
    In their original paper [2], Hartle and Hawking envisioned the no-boundary

proposal as corresponding to a Euclidean path integral over compact metrics.
This then implicitly provides no-boundary conditions: we will take them to
mean that we keep the scale factor fixed at zero size on the initial hypersurface.
We will try to see to what extent such an integral can be realised in a simple
setting, namely gravity with a cosmological constant, with action

              S = d4x-g             R                                        
                                    2                               d3y hK .                              (155)
                         M                  -         �

                                                              M0,1

The GHY surface terms are essential as we intend to keep the field values fixed
both on the initial (M0) and on the final (M1) hypersurface, i.e. we are
imposing Dirichlet conditions at both ends. This is the setting first studied
by Halliwell and Louko in [12]. For closed Robertson-Walker (RW) metrics,
parameterised again with an especially useful definition of the time coordinate
tq ,

                   ds2     =  -      N2     dtq2      +  q(tq )d32  ,                                     (156)
                                    q(tq )

the action simplifies and becomes quadratic in the scale factor squared q,

                                         1     -   3     q2  +  N   (3  -  q)      .                      (157)
                                                  4N
                   Sq = 22 dtq

                                       0

Details of this calculation were already presented in section 2.2, so we will not

repeat all of them here. However, it may be useful to recall that we can choose

the time coordinate to run over the values 0  tq  1, with tq = 0 being the

initial hypersurface on which we fix the scale factor to zero, q(tq = 0) = 0. On

the final hypersurface we will fix q(tq = 1) = q1, with the scale factor being

larger  than  the  Hubble  radius,  q1      >  3  .   The    total  time        elapsed     between  initial

                                                                                1
and final hypersurfaces is determined by the integral                           0  dtq  Nq  ,  and  will  thus

depend on the lapse N.

The no-boundary wave function (with Dirichlet conditions at both ends) is

thus given by the path integral

                                                  q1                ei

                           DD(q1) =                   Dq        dN       Sq  ,                            (158)

                                               0             C

                                                  58
where the contour C for the lapse integral remains to be determined. With the

above  boundary  conditions,  the    equation      of  motion        q� =    2     N  2  is  solved  by
                                                                              3

                 q�(tq )   =      N  2  t2q  +     -     N  2  +  q1      tq .                       (159)
                               3                      3

As described in section 2.2, the path integral over q can then be performed by
shifting variables q(tq) = q�(tq) + Q(tq), with the result that

                 DD(q1) =                    3i        dN      ei   22   S0  ,                       (160)

                                             2 C N 1/2

with                           2                                      3
                               36                     2              4N
                 S0  =     N3        +  N       3  -      q1      -        q12  .                    (161)

Note that the lapse integral contains an essential singularity at N = 0. This

can be understood physically from the impossibility of evolving from size zero

to size q1 = 0 in vanishing time.

    We will analyse this integral by performing a saddle point approximation,

using the tools made available by Picard-Lefschetz theory and reviewed in Ap-

pendix C. There are four saddle points, determined by S0/N = 0, located

at                                                                   1/2

                 N         =  c1  3  i + c2            q1  -   1             ,                       (162)
                                                   3

with c1, c2  {-1, 1}. The action at the saddle points is given by

                                  6                                 3/2
                                                   3
                 S0saddle  =  c1     i - c2           q1   -   1             .                       (163)

The first thing to note is that the saddle points, as well as the corresponding
actions, are complex. This was to be expected, as they describe a combina-
tion of quantum nucleation and classical evolution. The presence of the term
containing i in (163) implies that two saddle points will have a suppressed
weighting e-122/() (those with c1 = +1) and two will have an enhanced
weighting e+122/() (those with c1 = -1). The four saddle points and their
associated steepest descent (Ji) and ascent (Ki) lines in the plane of the lapse
function are shown in Fig. 25. The suppressed saddle points are located in the
upper half plane, and the enhanced ones in the lower half plane. Here we must
recall an important point mentioned at the end of section 3.2 and derived in
detail in section 4.1: the saddle points with suppressed weighting are associ-
ated with enhanced fluctuations, and vice versa. More precisely, if we add a
(linear) gravitational wave perturbation with amplitude h1 and wave number
(frequency) k, then the total weighting becomes e-122/()+32h21/(). This
means that larger fluctuations, i.e. more lumpy universes, come out as pre-
ferred. In other words, these saddle points are unstable when perturbations are

                                             59
                  K2                      K1
J
                                                           J1
 2

K2 2                          J2      J1      1

                                                       K1

J3                                                     J4
      3                                                     K4
                              K3      K4      4

K3                                        J
                    J
                                           4
                           3

Real2                                               1
                         Euclidean
                                      Lorentzian
   3
                                                    4

Figure 25: Saddle points and their associated steepest ascent (Ki) and descent (Ji) paths, in
black, shown in the complexified plane of the lapse function N. Arrows indicate the direction
of descent. Blue lines are lines of equal weighting. In the upper panel, green regions have
lower weighting than the saddles, red regions have higher weighting and yellow regions have
a weighting that is in between those of the adjacent saddle points. Asymptotically, i.e. either
at infinity or near N = 0, the integral converges in green regions and diverges in red regions.
In the lower panel, we exhibit the integration contours described in the main text.

                                  60
included, and thus do not warrant the use of minisuperspace. By contrast, the
saddle points in the lower half plane admit a Gaussian distribution of perturba-
tions e+122/()-32h12/(), and are stable. It is these that we must hope the
path integral will pick up.

    This brings us to the crucial question of contours of integration for the lapse
N, see also Fig. 25. Let us first discuss the Euclidean contour, i.e. a contour
along imaginary values of the lapse function. This contour was originally pro-
posed by Hartle and Hawking. However, as we can see immediately from Fig. 25,
there are regions of asymptotic divergence both at large positive imaginary lapse
values, and at small negative imaginary lapse. This means that the Euclidean
contour, whether defined in the upper or lower half planes, leads to a divergent,
mathematically meaningless, integral. Thus, this simple example shows that
a Euclidean contour is not actually viable. The root of the obstruction is the
conformal mode problem discussed at the beginning of this section.

    If we cannot use a Euclidean contour, then could we use a Lorentzian one?
After all, physics as we know it takes place in Lorentzian spacetime, and thus a
Lorentzian contour would seem to be a physically sensible choice8 [77]. Given
the singularity of the integrand at N = 0, we can either define it over positive
or negative real values of the lapse, but these two choices are just a matter of
convention. If we choose the positive real line, then we can see from Fig. 25 that
it is crossed by a single steepest ascent contour, namely K1. Thus the Lorentzian
integration contour can be deformed to the thimble J1 passing through saddle
point 1. The arc at infinity linking J1 to the real line gives a vanishing contri-
bution to the integral, as ensured by Picard-Lefschetz theory and as one can
verify explicitly [14]. Thus the Lorentzian integral picks up a single saddle point,
though unfortunately it is one of the unstable ones,

   122      122             3/2

-  e ( ) . DD,Lorentzian-iq1-1   (164)
                 3

As argued above, the inclusion of perturbations enhances the weighting, and
signals the breakdown of the minisuperspace "approximation". This signals
an inconsistent calculation � certainly, this choice of integration contour does
not lead to a ground state wave function, as was intended. It is in fact rather
surprising that what appears to be the most sensible contour on physical grounds
ends up giving entirely non-physical answers.

    To circumvent this problem, and based on early considerations in [76], it was
suggested in [78] that one should take the contour labeled "real" in Fig. 25. This
contour may be seen as an integral over the entire real lapse line, but passing
below the singularity at N = 0. The contour is crossed by all four steepest ascent

    8Let us recall however that the saddle points we are interested in are fully complex, yet
they describe the evolution of a Lorentzian universe, as described in section 3.5. From this
point of view, the Lorentzian contour is not a priori distinguished � it is sufficient that the
contour should pick up the saddle point(s) of interest.

61
lines, and thus all four saddle points contribute to the resulting path integral,

   122      122             3/2         122      122                3/2

-  e ( ) + e ( ) + c.c. , DD,real-iq1-1+     -i             q1  -1       (165)
                 3                                       3

where the sum over all saddles renders the wave function real and thus explains
the name given to the contour. This contour was chosen explicitly so that
the desired saddle points in the lower half plane are picked up. It should be
emphasised that this contour, even though it superficially appears to sum mainly
over real lapse values, actually obtains its largest contribution from the large-
weighting region just below N = 0. This explains how the wave function can
obtain the enhanced weighting manifest in (165), even though one must always
flow down from the original integration contour to saddle points that are relevant
(cf. appendix Appendix C). The trouble with the real contour is that it also
picks up the unstable saddle points in the upper half plane. Thus it leads to a
competition of weightings as the fluctuations become large, of the form

            122     -   32  h21      -  122  +  32  h21

            e + e , +                                                    (166)

and it is simply unknown what happens to the integral when h1 becomes large
(for discussions of this issue see [77, 79]). At some point backreaction on the
geometry can no longer be neglected, yet a full understanding would be required
to see what happens for large perturbations. This would be necessary in order
to assess whether this contour gives physically sensible results. In the absence of
a reliable non-perturbative calculation, we cannot trust this contour to provide
us with the definition of the sought-after no-boundary wave function.

    At this point, one may realise that it is pointless to explore different con-
tours in this setting. This is because the steepest descent lines J3,4 emanating
from the desirable saddle points 3 and 4 directly lead to the undesirable saddle
points 1 and 2. This arises because the action (161) is a real function of N , and
thus complex saddle points arise in complex conjugate pairs which lead to the
same phase (and inverse weightings) in the wave function. Since steepest as-
cent/descent lines are defined by having constant phase, the stable and unstable
saddle points are necessarily linked. Thus any contours picking up the stable
saddle points will also include the unstable saddles, leading to the identical
problem with large fluctuations discussed above [77]. Thus in the end we must
conclude that the sum over compact metrics, at least in this simple setting, does
not lead to a trustworthy no-boundary (ground state) wave function.

Neumann boundary condition
    If a sum over compact metrics is problematic, then how can we define the

no-boundary wave function? Heuristically, a possible solution was suggested
above [80]: the uncertainty principle says that we can either put a condition on
the initial size, or on the initial expansion rate. But the initial expansion rate is
Euclidean, and in fact requires a choice of sign, cf. (107). This choice of sign is
precisely what distinguishes the stable from the unstable saddle points that we
just discussed. One may also think of this choice of sign as the choice of Wick

                                 62
rotation, i.e. do we define t = +i or t = -i ? Only one sign assignment leads
to stable, Gaussian distributed fluctuations, and this is the choice a(0) = +1.
So can we define a path integral with this boundary condition?

    A related issue is that when we defined the path integral with fixed initial
size, for consistency we had to include the GHY surface term in (155). But the
spirit of the no-boundary proposal is that there should be no boundary. Hence
why should one include a boundary term? And where should it be placed, if the
intention is that there should be no boundary? From this point of view it seems
much more natural not to include a boundary term. If we do this, it changes
the variational problem, and in fact leads to a Neumann problem, as shown in
section 2.2, allowing us precisely to fix the initial momentum.

    We will now see how this works for the simple setting of gravity plus a
cosmological constant, with closed RW metrics considered above [81]. We will
not add any surface term on the initial hypersurface, yet we will again include
a GHY term on the final boundary, as we wish to keep the metric fixed there,

                S = d4x-g R -  +                                                                        (167)
                                             2                        d3y hK .

                          M                                      M1

We will specialise to the metric (156). Using integration by parts in the action,
the surface term at tq = 1 is eliminated by the GHY term, while a surface term
is then generated at tq = 0,

                S = 22         1       -   3    q2  +  N  (3  -  q)      -    32  q q|tq =0  .          (168)
                                          4N                                  N
                                 dtq

                              0

As shown in section 2.2, variation of this action leads to the equation of motion

q� =  2   N  2  and  the  boundary       condition     that      we  can   fix   q/N     at  tq  =  0.  Recall
       3

that N dtq/q1/2 = dt, so that consequently q/N = 2da/dt implying that we

should fix

                                                 q  = +i .                                              (169)
                                                2N

This is the no-boundary regularity condition (107) expressed in our currently
used variables. On the final hypersurface we will again set q(tq = 1) = q1 > 3/.
With these boundary conditions, the solution to the equation of motion reads

                     q�(tq )  =     N  2tq2  +  2N itq  +  q1    -      N  2  -  2N i .                 (170)
                                 3                                   3

Evaluating the path integral over q in the same manner as before, we then obtain
the following expression for the Neumann-Dirichlet wave function,

                                             e i 22    2   N  3  +iN  2  -q1  N  -3iq1
                                                        9
                     ND(q1) =            dN                                              ,              (171)

                                      C

where once again the contour of integration C for the lapse integral remains
to be specified. But before discussing contours, we may already notice some

                                                    63
1000  saddle N+
 800

600              Re[q(t)]

400

200   Im[q(t)]

0                t

-200                                           J_            K_  K+      J
      0.0 0.2 0.4 0.6 0.8 1.0
                                                                          +

1000                                               N_

800   saddle N-                                                      N+

600              Re[q(t)]

400

200

0     Im[q(t)]   t

-200
      0.0 0.2 0.4 0.6 0.8 1.0

Figure 26: Left panel: an example of the evolution of the scale factor squared for the saddle
points of the no-boundary wave function defined with an initial Neumann/momentum condi-
tion, with  = 3/100, q1 = 1000, so that the saddle points are at N� = �300 - 100i. One can
see that the saddle points are compact, as they start at zero size. Right panel: The saddle
points and their associated steepest ascent/descent lines in the complex plane of the lapse.
The Lorentzian integration contour may be deformed into a sum of the 2 thimbles J�.

important differences with the Dirichlet action (161). There is no singularity
at N = 0, since it is now possible (even if unlikely) that the initial geometry,
satisfying q = 2N i, already coincides with the final geometry, satisfying q = q1.
Also, the action now contains explicit factors of i, due to the boundary condition
(169). Thus we do not expect saddle points to come in complex conjugate pairs
anymore. In fact, there are only two saddle points this time, and they are
located at

                 N�            =  3  -i  �  3      q1  -  1  .               (172)
                                               3

The corresponding field evolutions are shown for an example in Fig. 26. Note
that the saddle points are not only regular, which they are by design, but
also compact: at the saddle points, one may see and verify that q(tq = 0) =
0. Also note that the fields are only becoming real right at the end of the
time evolution, as this now does not correspond to a Euclidean-plus-Lorentzian
contour in the complex time plane, but rather to a solution with fixed (complex)
lapse. Comparing to (162), we see that in fact only the two saddle points in the
lower half plane are left. That is to say, the unstable saddle points have been
eliminated, and we are left purely with the stable saddle points!

    We still have to figure out which integration contour to take. For this, see
Fig. 26, in which the saddle points and their steepest descent paths are shown.
We can now proceed again with an examination of suitable contours. We may
notice right away that the Euclidean contour once again does not work. Since
there is no singularity at N = 0, it would have to be defined over the entire
imaginary lapse line in order to yield an invariant result. However, we can see

                                         64
that there is again a divergence at large positive imaginary values, and again
the Euclidean definition does not make sense.

    By contrast, the Lorentzian contour works [81]. The integral converges both
at negative and positive infinity and since there is no singularity at N = 0,
we must integrate over the entire real N line in order to obtain an invariant
definition. Note that the Lorentzian contour is crossed by both steepest ascent
paths, and hence both saddle points contribute to the integral. In fact, the real
lapse line can be deformed into the sum of both thimbles C = J+ + J-, with
orientations chosen in the direction of increasing real parts of the lapse. The
wave function then becomes approximated by

   122      122             3/2     122      122             3/2

+ (q )  e ( ) + e ( ) , ND 1-iq1-1+      +i          q1  -1       (173)
                 3                                3

Note that it is real, as it is the sum of two complex conjugate contributions,
even though the integral is not defined over a Euclidean contour. This is due to
the symmetry between negative and positive real parts of the lapse. One further
remark: Picard-Lefschetz theory implies that relevant saddle points must have
a lower weighting than that of the defining contour. One may thus wonder how
it is possible to obtain an enhanced weighting from a Lorentzian integral. This
is because even though the starting action (167) is real, the boundary condition
(169) is complex, and this results in a positive weighting in (171), even at real
values of the lapse.

    In fact, there are only a few other contours we could contemplate. One
possibility is to sum over the two thimbles, but with opposite orientations C =
J+ - J-, i.e. to sum from negative imaginary infinity up to negative real
infinity, plus an integral from negative imaginary infinity to positive real infinity.
This choice would give a pure imaginary wave function � however, since we are
ignoring the prefactor, which could be imaginary too, this must be seen as
equivalent to a real wave function. At the semi-classical level, the implications
are however largely unaffected by this choice of orientation of the thimbles.
This is because the two saddle points behave effectively independently, as soon
as perturbations and the resulting decoherence is taken into account. Indeed,
as shown in [27], perturbations quickly decohere the two saddles as the universe
grows, already separating their evolutions when the universe is only a little
larger than the Hubble radius.

    The only remaining contours we could envision are to single out one of the
thimbles J�, by summing from negative imaginary infinity either to positive
or negative real infinity. In this case, we would have no need to talk about
decoherence, as the integral would be approximated by a single saddle point.
However, the wave function would not be real. Still, one attraction of such
contours is that they would constitute a kind of compromise between a Euclidean
and a Lorentzian one.

    Let us now focus our attention a little more on the thimbles. Since the path
integral is redefined by integrals over thimbles, we may wonder what kind of
geometries are actually summed over. In general, there is no particular distin-
guishing feature to these complex geometries. However, a few special locations

                            65
            Z-        Z+

             N-        N+

   N-                                         N+

              Y-      Y+

Figure 27: For the no-boundary wave function with a Neumann initial condition, cf. Fig. 26,
this graph shows the location of singular geometries in which the scale factor passes through
zero (indicated by the red dashed lines) in the plane of the lapse function. The insets show a
zoom of the regions near the saddle points, and demonstrate that the thimbles intersect the
lines of singular geometries. Figure reproduced from [81].

in the lapse plane may be singled out. For instance, at large negative imag-
inary values of the lapse, the geometries may straightforwardly be seen to be
essentially very large Euclidean 4-spheres with their North Pole cap removed
at radius squared q1. The asymptotic regions at large |Re(N )| are similar, but
the radius of the sphere is complex there. We may also wonder whether singular
geometries are included. For this, we can ask whether q�(tq) passes through zero
at some tq (with 0  tq  1). The locus of such geometries is shown in Fig. 27.
As seen there, and calculated in [81], the thimbles actually pass through this
locus, i.e. the thimbles also contain a singular geometry. It is not clear that
this should be considered pathological. In general, one may expect gravitational
path integrals to contain geometries that are not differentiable anywhere, so this
may not be problematic. Also, such singular geometries most likely obtain a
divergent action once perturbations are included, and may thus eliminate them-
selves automatically by virtue of having zero weighting. These considerations
also raise the question of whether it is problematic when q changes sign, sig-
nalling a signature reversal in the metric. This is a question of ongoing research,
and we will return to this issue in section 5.4. The quick answer is that this is
not known yet.

    Having found a minisuperspace path integral implementation of the no-
boundary wave function, we may also study its relation to the WdW equation
[82]. For this purpose, recall from (36) and (37) that the Hamiltonian is given
by

H  =     N  p2 + 124(3 - q)  = N H^ ,             (174)
      - 62

                  66
with    the  canonical    momentum        p  =   -  32  q.   The   WdW    equation     then  corresponds
                                                     N
to the operator version of this equation,

                                                 H^  = 0 ,                                          (175)

with  being the wave function of the universe. Now we have to pay attention to

the boundary conditions we imposed, namely Dirichlet on the final hypersurface

and Neumann on the initial one. The canonical commutation relation [q, p] = i

must be implemented correspondingly. On the final hypersurface, where we

work in field space, so we replace the momentum by a derivative operator p 

p^  =  -i     ,  leading  to
           q

                          H^ (q)    =  0        2     + 124(q - 3)            =  0.                 (176)
                                                q2

By contrast, on the initial hypersurface we impose a momentum condition, so

as  to  obtain   the  WdW        equation    in  momentum          space  we  substitute   q    q^  =  i     ,
                                                                                                          p
leading to

                      H^ (p)     =  0     (p2    +  364)        +  124  i        =   0.             (177)
                                                                           p

There is one subtlety here: because we are imposing this equation on the initial

boundary,        we  had  to  flip  the   sign          -       [82].
                                                 p           p

                       1 � 1034                     
                       5 � 1033
                                                                                       a1
                      -5 � 1033
                                             1            2            3            4

Figure 28:       The no-boundary wave function as         an Airy function, see     (1q718.)T. hHeecroesmthoelowgiacvael
function ,       which is real, is plotted as a function  of the final radius a1 =

constant is set to  = 1. Figure reproduced from [82].

    The momentum space equation (177) is of first order and yields an essentially
unique solution, the exponential of a cubic in p0. Meanwhile, the position
space equation (176) can be identified as an Airy equation, with two linearly
independent solutions, the Ai and Bi functions. Choosing a particular linear
combination is directly related to the choice of contour in the path integral
approach [17], for instance the Lorentzian contour yields the Ai function and
the contour summing both thimbles from negative imaginary infinity yields the
Bi function. Explicitly, if we stick to the Lorentzian integration contour, then

                                                      67
the equivalent, exact, solution to the WdW equation is

                                                    182  2/3           
                                                                       3
(p0,  q1)  =  e3   ip0  +        1    ip30  Ai                   1  -     q1  .  (178)
                           364

with initial momentum given by (169), that is to say

                        p0    =     -  32   q(0)    =  -62i   .                  (179)
                                       N

The wave function is shown in Fig. 28 as a function of the final size q1 = a21. As
one can see there, the wave function rises exponentially (from a non-zero value)
at q1 = 0 and then starts to oscillate once the universe has become larger than
the Hubble radius. These two regimes correspond to quantum tunnelling from
nothing, and subsequent classical evolution, respectively. Note that it remains
unclear how to interpret the fact that the wave function is non-zero at zero size.
In [2] it was suggested that this could be due to the contribution of non-trivial
topologies, but the present calculation did not contain additional topologies.
This question thus deserves further study.

    For the particular value of the initial momentum (179), which was chosen to
ensure regularity, we find from (177) that at the no-boundary point, the wave
function satisfies the additional relation [82]

      i       =    q^      =  0                 no-boundary condition .          (180)
         p

This is particularly suggestive: it says that the no-boundary wave function
satisfies the momentum space equivalent of the zero size condition, that is to
say the regularity condition we imposed on the wave function turns out to be
equivalent to the operator expression for the zero size condition! This certainly
conforms well with the spirit of the no-boundary proposal. It also means that at
the nucleation of the universe, there is no momentum transfer into the universe.
In other words, this condition also expresses the notion that the universe is
self-contained.

    A final comment: a priori, one might think that field space and momentum
space definitions might be equivalent, as they can be Fourier transformed into
each other. However, the Fourier transform would sum over all possible initial
momenta, and would thus also include momenta that correspond to unstable
Wick rotations. This argument also implies that the results obtained so far
are mutually consistent. It might however be interesting to see if a viable field
space wave function could be obtained from a partial Fourier transform of the
momentum space wave function, where only initial momenta of the appropriate
sign are included. This does not seem to have been explored so far.

A model with anisotropies � biaxial Bianchi IX spacetimes
    From the simplest dynamical model above, we learned that a path integral

from zero size gives us saddle points that come in two kinds, with stable (Gaus-
sian distributed) perturbations, and those with unstable (inversely Gaussian)

                                                68
perturbations. This is a general feature, and it makes the definition of the no-
boundary wave function as a path integral from zero size questionable. However,
we also saw that a definition in which we impose a regularity condition instead
works rather well. The regularity condition is a condition on the momentum
conjugate to the spatial metric, and is obtained when we do not add any sur-
face terms to the action. It is instructive to see how this prescription may be
implemented in more complicated models, with anisotropic metrics and, later,
with a scalar field added.

    In fact, only a handful of minisuperspace models are known, which are
tractable in the sense that all integrals except for that over the lapse can be done
easily (and in some cases fully analytically) [83, 84, 85, 86, 87, 79, 88, 89]. Here
we will focus on two representative examples, the first with biaxial Bianchi IX
metrics, and the second with an inflationary scalar field. The techniques used
to analyse these models are analogous to the techniques exhibited above, so we
will be much briefer, and leave some details to the original references.

    First we will stick to the action consisting of gravity with a positive cosmo-
logical constant , but now consider metrics of the form

                    ds2   =    N2   dt2  +   p  (12  +  22)  +  q  32  ,        (181)
                             -               4                  4

                                 q

where p(t), q(t) are time dependent scale factors and 1 = sin d-cos  sin d,
2 = cos d + sin  sin d, and 3 = d + cos d are differential forms on the
three sphere with coordinate ranges 0    4, 0    , and 0    2.

This metric describes Bianchi IX spacetimes on the axes of symmetry (in the

notation of Misner [90] this would correspond to pure + perturbations with
- = 0). This is also known as the Taub spacetime. Locally it can be seen as a
product of a 2-sphere with radius squared p and a circle with radius squared q.

Globally, the metric describes a fibration of S1 over S2, and when p = q we

recover the round 3-sphere. When p = q, we may think of it as a squashed,

anisotropic 3-sphere (see [91]).

We have to be slightly more specific with regards to the action that we are

considering. We would like to sum over manifolds with the metric held fixed on

the final boundary, hence we must add the GHY surface term there. But on

the initial "no-boundary" surface, we will not add any surface term. Thus the

action reads

              S  =  1    d4x-g (R - 2) + (pp + qq) |t=1 ,                       (182)
                    2

where we expressed the GHY term in terms of the scale factors and their con-
jugate momenta

               1    p  =      1     q  +  q  p  ,     1  q      =      1  p  .  (183)
              22          - 2N            p          22            - 2N

When the action is varied (see e.g. [86, 87, 79]), one obtains the following
boundary terms at t = 0

                             pp = 0 , qq = 0 .                                  (184)

                                          69
These must be set to zero in order to obtain a consistent variational problem.
Note that we cannot set both a variable and its conjugate momentum to zero
simultaneously, as this would be in conflict with the commutation relations.
But we see that we also cannot fix both momenta. Thus the geometrical Neu-
mann condition that we imposed translates into a combination of Dirichlet and
Neumann conditions on the variables used. There are two appropriate combi-
nations of interest [79]: we can either choose p0 = 0, q(t = 0) = -22i (NUT,
S2 shrinks to zero) or q0 = 0, p(t = 0) = -22i (Bolt, S1 shrinks to zero),
where in both cases the signs of q,p(t = 0) are again fixed so as to correspond
to the usual, stable sign for the implied Wick rotation.

                                        3            K3          N

                                 J3

                  K2                                     K1

                           2                  1

                           J2                 J1

Figure 29: Saddle points (in orange), steepest ascent (K) and descent (J ) contours for Taub-
NUT metrics, with lapse action (185). The saddles numbered 1 and 2 are physically relevant.
Figure reproduced from [87].

    The first choice leads to a Taub-NUT-dS spacetime, in which the 2-sphere
is shrunk to zero size initially. When the equations of motion for p and q are
solved with these boundary conditions, one is left with an action that depends
purely on the lapse

 1  SN  U  T  (N  )  =  -  p1q1  + iq1  +  N      4  -       p1  -  i     N  2  .  (185)
22                          N                            3             3

This action admits three saddle points, see Fig. 29. One of these is purely
Euclidean, and does not lead to a classical spacetime. The other two saddle
points are of physical interest (they yield a complex action, with a real part
that grows rapidly with increasing p1, q1), and are simply related by a reflection
in the real part of N. They are picked up by the path integral if one chooses a
contour of integration for the lapse that contains their thimbles, i.e. we must
sum over J1 � J2. Note that a Lorentzian integration contour, as we had in the
isotropic case, is not possible this time as the integral simply diverges along such
a contour. If one chooses the contour J1 +J2, then note that it can be deformed
into a closed, circular contour around the singularity at N = 0. Whether a
closed contour makes sense is debatable [87]: if we imagine performing the lapse

                                 70
integral first, before doing the integrals over p and q, then there is no singularity
at N = 0 and the contour can be shrunk to zero, leading to a vanishing result.
This argument indicates that there can be no fundamental meaning to a closed
contour, and thus it might be preferable to sum from negative Euclidean infinity
to the origin along both thimbles. However, in that case we also rely on the fact
that there is a singularity at N = 0 on which the thimbles end. Hence we see
from this example that one cannot claim at present that it is understood how
to define integration contours from first principles. We will take a pragmatic
approach here, and assume that the saddles 1 and 2 are picked up, with the
expectation that a better justification for the required integration contour will
be found in future work.

6                            5.0

5  -Im[SNUT,1 ]              4.5                                                      -Im[SBolt,1 ]

4                            4.0

3
                                                                              3.5

2

1                            3.0                                                   -Im[SBolt,2 ]

                         p1                                                                              p1                     p1

   10  20        30  40  50                                                        5  10             15  20  50  100  150  200

Figure 30: The weightings of different saddle points of interest for Taub metrics. The NUT
case is shown in the left panel, the Bolt case in the middle, and a superposition of these two
cases (with the same colouring) in the right panel. In all cases, we set  = 1 and q1 = 12. For
a detailed description, see the main text.

    When these saddle points are relevant, then we may look at their weighting,
which is the same for both � an example is shown in the left panel of Fig. 30, with
q1 fixed and as a function of p1. Here we can see that the isotropic case p1 = q1
comes out as favoured, while more anisotropic configurations are suppressed.
This supports the notion that the no-boundary wave function describes a state of
minimum excitation. It also confirms the choice of sign in the initial momentum
q(t = 0). A comment regarding normalisability: the weighting approaches zero
for p1  . Thus at this level of approximation, we cannot yet say whether
an integral over all p1 values (or perhaps an integral over all configurations
with fixed volume) would yield a convergent result, as this will depend on a
prefactor. But the prefactor depends on the exact measure in the path integral,
and this measure is not known (the related ambiguity in the WdW equation is
the question of factor ordering). This is an issue that deserves further work -
for more discussion of this point see [79].

    But as we saw above, a second set of boundary conditions is also possible,
q0 = 0, p(t = 0) = -22i, for which the initial circle is shrunk to zero. This
gives rise to so-called Taub-Bolt-dS spacetimes. One can again solve the equa-
tions of motion for p and q with these boundary conditions [79], and perform
the integrations over the scale factors. This time the resulting lapse action is

                                                                                      71
                                        N           (p ~7.8, q =12)  N                                                                      N
                                                 5                              (p =5, q =12)
(p =12, q =12)     5                                                                                 5

                                  4                                                            4
                                                                                                                                         1

                                                       1

4               3      2      13                                                               3        2

                   6                       6        2                                                6

                   7                       7                                                         7

Figure 31: Saddle points and associated thimbles (steepest descent contours, in green) for
Bolt boundary conditions, for the action (186). Also shown are the steepest ascent contours
associated with saddles 1 and 2 (in red). Arrows indicate downwards flow. The left panel
shows an isotropic example (p1 = q1 = 12), and the right panel one with much smaller
p1 = 5. The middle panel shows the cross-over between these two regimes. This is described
by a Stokes phenomenon, where the downwards flows from saddles 2 and 3 link up with the
upwards flow from saddles 1 and 4 (this is shown by the black line). The dashed orange line
is located parallel to the real N line in the lower half plane, and represents the preferred
integration contour.

more complicated, and reads (for  = 1)

                    1  SBolt  (N  )  =  p1          N 4 - 18N 2q1 - 36iN q1 + 9q12
                   22                                       12N 2(N + 3i)

                                        -     N3    +  3iN 2         + (p1  -  12)p1N             .                                         (186)
                                                                     3p1

This action admits 7 saddle points. Examples of the associated thimbles are
shown in Fig. 31. Three saddles are Euclidean and not of physical interest. The
other four are however of potential physical relevance. They arise again in pairs,
with equal weighting. The imaginary parts of the actions of saddles 1 and 2
are shown in the middle panel in Fig. 30. We can see that there is a cross-over
in likelihoods, with the transition between dominance of the two saddles taking
place when p1 is a little smaller than q1. Also, the weighting diverges at small
p1, for saddle number 1. Thus, the predictions depend rather crucially on which
saddles are picked up in the path integral.

    The thimbles are shown in Fig. 31, both for q1 fixed and various values of
p1. Let us first start with the case where the scale factors are equal, see the left
panel in the figure. The obvious contour of interest is the one running parallel
to the real N line, in between the two singularities at N = 0 and N = -3i (in
fact, for convergence, the contour must run below N = -i). This contour can
be deformed into a sum of the four thimbles associated with saddles 1 to 4, and
thus all four saddle points are picked up. The ones with the highest weighting
will dominate the path integral, in this case saddles 2 and 3.

    Now comes a crucial point: if it remains true that all 4 complex saddles
contribute to the path integral, then at small p1 (for fixed q1) saddles 1 and 4
will dominate, and in fact their weighting grows unboundedly at small p1, cf.
again Fig. 30. This would render the wave function non-normalisable and we

                                                       72
would have to conclude that somehow the no-boundary wave function for biaxial
Bianchi IX spacetimes does not exist, cf. also the discussion in section 2.4.
However, a topological change in the steepest ascent/descent paths occurs as p1
shrinks below a critical value (in our numerical example, for p1  7.8), which is
near the point where the dominance of the two saddles switches. This is known
as a Stokes phenomenon9. At the critical p1 value, the steepest descent contour
from saddle 2 coincides with the steepest ascent contour passing through saddle
1, i.e. the actions at both saddles have the same real part (and similarly for
saddles 3 and 4), though the weightings of saddles 2, 3 are still higher than those
of saddles 1, 4. Below this critical value, the thimbles of saddles 2 and 3 run
directly to infinity, and the integration contour for the lapse that we considered
before can now simply be rewritten as the sum of the thimbles associated with
the saddles 2 and 3. In other words, saddles 1 and 4 do not contribute anymore
(their steepest ascent paths do not cross the integration contour, see the right
panel in Fig. 31) after this Stokes phenomenon has occurred. For this to be
true, we must however stick to the same defining contour of integration we had
for larger p1. This shows that, despite the misgivings expressed in the analysis
of the NUT case, we can see clearly that the integration contour is of paramount
importance in figuring out the predictions of gravitational path integrals. For
a more in-depth analysis of Stokes phenomena and integration contours in this
context see [92].

    We can draw two lessons from this analysis: the first is that in general we
must expect to sum over "no-boundary" boundary conditions, as with the NUT
and Bolt cases above. In fact, when both cases are summed, the weighting of
the various saddle points is shown in the right panel of Fig. 30. As one can see
there, for small p1 and up until p1 comfortably exceeds q1, the NUT geometry
dominates (since, for small p1, the saddle represented by the blue line is not
picked up). Then for larger p1 saddles 1 and 4 of the Bolt geometry come to
dominate, and at very large p1 it is saddles 2 and 3 of the Bolt geometry that
give the largest contribution to the path integral. Thus, even in a fairly simple
model, interesting phase transitions may occur [79]. And the second lesson is
that, even though there is no understanding yet of how to define gravitational
integration contours from first principles, they are of clear relevance in elucidat-
ing the consequences of these integrals.

A model with a scalar field
    The realisation that one must sum over boundary conditions is made even

more manifest when considering a model that includes a scalar field. A tractable
model is obtained if one chooses [85]

V () =  cosh  2    .                                                             (187)
              3

This model is of inflationary type, with a de Sitter minimum at  = 0. The

9The analysis of this Stokes phenomenon represents original work by the author.

                                               73
model is not realistic in the sense that the potential is too steep over most of
its range to lead to viable primordial perturbations, and it does not include a
reheating phase. However, it is useful as a toy model for quantum cosmology.
This is because for closed Robertson-Walker metrics of the form

                       ds2      =     N2     dt2  +  a(t)2d32,                           (188)
                                   - a(t)2

one can perform a redefinition of the fields [85],

x(t)  a2(t) cosh             2  (t)    ,     y(t)  a2(t) sinh          2  (t)   ,        (189)
                             3                                         3

which renders the action quadratic

                    1    3   y2 - x 2     + 3 - x       +  32     (yy  -  xx )  |t=0  .  (190)
                       4N 2                                N
S = 22 dtN

                  0

Here, in line with prior discussions, we did not include a GHY surface term
at t = 0, but did include one at t = 1. Integrations by parts then actually
remove the boundary term at t = 1 and generate one at t = 0, resulting in
the action written above. The original fields can be recovered from the inverse
transformations

a(t) = x2(t) - y2(t) 1/4 ,                       (t) =     3  artanh      y(t)  .        (191)
                                                           2              x(t)

The momenta conjugate to the new variables x, y are given by

                       x        =  -  32  x  ,    y  =  32  y  .                         (192)
                                      N                 N

Our boundary conditions are such that we will impose conditions on these mo-
menta at t = 0, while we will fix the final values x(t = 1) = x1, y(t = 1) = y1
on the final hypersurface. To determine which conditions should be imposed on
the initial momenta, we should consider the constraint that will be satisfied by
the saddle points. For the action (190), it is given by

                         1         2x - 2y      + 3 = a2V () .                           (193)
                       124

We would like to obtain saddle points that are not just regular, but also closed,
i.e. we would like the saddle points to satisfy a(t = 0) = 0. Thus we should
impose the following regularity condition [88]

x2 - 2y = -364 at t = 0 (regularity)                                                     (194)

with in addition Im(x) < 0 for stability.
    Perhaps surprisingly, what is found is that two types of saddle points exist.

The first type is the expected compact and regular no-boundary geometry, see

                                             74
3       closed saddle                                                        3.5      unclosed saddle
                                                                             3.0
                            Re[a(t)]                                         2.5                       Im[a(t)]
                                                                             2.0        0.2 0.4 0.6
2                                                                            1.5                                    Re[a(t)]
                                                                             1.0
1                                                                            0.5                                                 t
                                                               t             0.0                                    0.8 1.0
                                                                                                                  Re[(t)]
0                                                                                0.0
                 Im[a(t)]                                                     0.5

   0.0  0.2  0.4       0.6  0.8       1.0                                     0.0

0.07

0.06 closed saddle          Re[(t)]
0.05
                                                                             -0.5

0.04                                                                         -1.0                        unclosed saddle
                                                                             -1.5
0.03         Im[(t)]                                                                  Im[(t)]

0.02

0.01                                  t                                      -2.0
                                                                                                                                            t
0.000.0 0.2 0.4 0.6 0.8 1.0
                                                                             -2.5
                                                                                   0.0 0.2 0.4 0.6 0.8 1.0

Figure 32: Examples of closed and unclosed saddle points for fixed initial momenta, in a

scalar field model with an inflationary potential. The numerical values used here are x 

0.0566 - 59.2i, y  -2.26 + 1.48i, x1 = 10, y1 = 0.5,  = 1 implying a1  3.16, 1  0.0613.

Note that the unclosed saddle has SP = -                          3      i,  a  value  indicated         by  the  green  line.
                                                                  2   2

the left graphs in Fig. 32 for an example. In this case the scale factor starts
at zero size and reaches the desired final value, while the scalar field starts
at a complex value and also reaches the desired final, real value. This saddle
point is completely analogous to the numerical examples we discussed in section
3.2. However, we should note that it only exists for precisely tuned values
of the initial momenta x,y(t = 0). But it is found that, for the same initial
values of the momenta, there can be saddles of a second type, which are in
fact not closed at t = 0, i.e. they start with a non-zero, complex scale factor,
see the right graphs in the figure for an example. This is made possible not
by a becoming zero at t = 0, but rather by the potential V (SP ) becoming
zero, cf. the constraint equation (193) [88]. That such saddles can exist is
implied by Picard's little theorem, which roughly speaking implies that a non-
constant entire function assumes all possible values, hence somewhere (or in fact
at multiple locations) the potential vanishes when analytically continued. For

our potential (187) this occurs when                              2   SP        =     (2n  +   1)     i  with     n    Z.
                                                                  3                                2

It was found in [88] that the weighting of the unclosed saddle is subdomi-

nant to that of the closed, no-boundary, saddle. Hence the unclosed saddle is

unimportant in this example � however, it is not known whether this occurs for

other potentials too.

This brings us to a conceptually important point. The South Pole values of

x,y must be tuned in order for a saddle point to exist, which is compact at t = 0

and reaches the desired final values x1, y1. This is analogous to the tuning of SP

performed in section (3.2). But how does the late universe know which values

                                                                  75
the initial momenta had to have at nucleation? Simply fixing this value by hand
is highly non-local, and does not seem plausible. It would be much more natural,
and in the spirit of the Feynman sum over histories, to sum over all possible
initial values of x,y, subject to the regularity condition (194). In some sense,
locality implies that we really must sum over initial conditions. Such a sum
would then automatically include the closed and regular no-boundary saddle.
But, as we saw above, it would also include other saddle points, that are regular
but not closed. There is no guarantee that these will all be subdominant. Hence
it is not at all clear that the wave function, so defined, will be of no-boundary
type.

    At this point, let us look ahead somewhat to see how this issue might be
resolved. There are two arguments that suggest that the unclosed saddles ul-
timately do not contribute. The first is that when one performs the same cal-
culation, but with a negative potential, i.e. with  < 0 in (187) (where it is
arguably better defined in light of AdS/CFT [93]), then the unclosed saddles
are found to be singular in the sense that the scale factor passes through zero
[88]. This means that when perturbations are added, the action will become
infinite and such "saddles" remove themselves from the path integral. Hence, if
the wave function can be analytically continued in , then one might also expect
the unclosed saddles to be spurious when  > 0. A second argument is that the
scalar field has to become highly complex, in the sense that the imaginary part
must become very large, to reach V () = 0. This might simply not be allowed
at a fundamental level, as such large imaginary parts can lead to divergences in
the path integral for the full theory (when including other matter contributions)
[94, 95]. Thus it seems possible, if not plausible, that a proper definition of the
full path integral will remove such unclosed saddle points. We will return to
this issue in section 5.4.

3.7. No-Boundary Saddles with Anisotropies and Black Holes

    In the previous section, we discussed definitions of the path integral in the
context of minisuperspace models. This was made possible by the simplifications
that arose from using restricted classes of metrics, and special parameterisations
of the fields. For more general models, such simplifications are not known to
occur, and the best we can do is analyse potential saddle points of the path
integral, i.e. try to figure out the properties of compact and regular (typically
complex) solutions of the equations of motion and constraints. This is however
a good starting point in elucidating the consequences of the no-boundary wave
function, and in many situations it seems plausible that the saddle points thus
found are also in fact the dominant ones.

Anisotropies � full Bianchi IX
    Our universe is highly isotropic on the largest scales, but less and less so as

we probe smaller scales. It is thus of interest to study anisotropic models, as
they provide a more realistic description of the universe. The Bianchi IX metric
stands out for several reasons [90]. Locally, it provides a generic description of
spacetime geometry. This is used in the proof that in the approach to a spacelike

                                                  76
(big bang-like) singularity the metric (locally) becomes ever closer to Bianchi IX
form [96]. Hence it is of interest to see what the no-boundary proposal implies for
such metrics, and in particular whether the no-boundary wave function favours
more or less isotropic universes. This topic was explored in a number of papers
over the years, see in particular [97, 98, 99, 100, 101, 102, 103].

    For our analysis, we will again consider agravity-scalar model with an ex-
ponential potential V () = V0ec, with c < 2 in order to obtain inflationary
dynamics. The Bianchi IX metric can be written as [90]

                      a(t)2                                            
ds2IX     -N 2dt2       4       e+(t)+ 3-(t)12 + e+(t)- 3-(t)22 + e-2+(t)32 ,
       =           +

                                                                                        (195)

where the 1-forms i were defined below (181). The scale factor a thus de-
termines the spatial volume, while the � parameterise shape change. When
� = 0 one recovers the isotropic case, while - = 0 is the biaxial case discussed
in section 3.6. The Lorentzian action then reduces to

          S = 22          dtN a      1       -3a 2 + a2      1   2  +  3  +2  +  3  -2
                                    N2                       2         4         4

                                 - a2V () + U (+, -) ,                                  (196)

where a potential arises for the anisotropy parameters,


          U (+, -) = - 2 e2+ + e-+- 3- + e-++ 3-


                                + e-4+ + e2+-2 3- + e2++2 3- .
                                                                                        (197)

This potential has a minimum at U (0, 0) = -3 and at large � exhibits a
triangular symmetry in �-space.

    Varying with respect to the lapse N yields the Friedman equation

       3a 2 = a2   1   2  +  3  +2  +  3  -2    + N 2 a2V () + U (+, -) ,               (198)
                   2         4         4

while the equations of motion for � and  are given (in constant N gauge) by

                             ��  +     3  a  �  +  2  N2  U,�   =   0,                  (199)
                                          a        3  a2                                (200)

                             �  +   3  a     +  N 2V,  =  0  .
                                       a

    No-boundary solutions must be compact and regular. We may again solve
the equations of motion and constraint perturbatively around the South Pole,
imposing compactness and regularity. The result, in terms of Euclidean time

                                                77
                                      |()|                                                        |()|


                                                                                                               0

                                                           0                                                   -2

                                                                                                               -4

                                                           - 10                                                -6


                                                           - 20                                                -8

                                                                                                                                                                                                                       - 10
                                                           - 30


                                     |( + )|                                                     |( - )|


                                                           0                                                   0

                                                           -5                                                  -5

                                                           - 10                                                - 10

                                                           - 15                                                - 15

                                                                                                                                                                                                                       - 20
                                                           - 20

                                                                                                                                                                                                                       - 25


Figure 33: An anisotropic instanton, optimised to reach the real values b = 10000,  =

-2, b+ = 1, b- = 1 on the final boundary, for V0 = 1, c = 1/3. These values are reached
at f = 2.33 + 18.0 i, with the South Pole values SP = 0.942 - 0.554 i, SP + = -0.926 +
0.173 i, SP - = -0.00373 + 0.000697 i. Note the presence of branch points and associated cuts
in the lower right parts of the figures. The style of the figures coincides with that of Figs. 16

and 17. Figures reproduced from [103].

(N = i), is [103]

a  =     -  1   V0  ecSP      3
            18

      +    1    ((-216(SP                        +)2  -  216(SP -)2      +  (8    -  27c2)V02e2cSP             ) 5                                                                                                           +  �  �  �
         8640
                                                                                                                                                                                                                                (201)

   =  SP    +   c  V0  ecSP                   2  +  c(2  + 3c2   )  V02  e2cSP    4  +  ���                                                                                                                                     (202)
                8                                        576

+  =  1  SP        2  +   1   (45(SP                  -)2  + SP +(-45SP -               + 7V0ecSP )) 4                                                                                                                       +���
      2                  144
             +

                                                                                                                                                                                                                                (203)

-  =  1  SP  -     2  +   1   SP                    (90SP        + 7V0ecSP ) 4          +���              ,                                                                                                                     (204)
      2                  144
                                                 -            +

where we used a prime to denote derivatives w.r.t. Euclidean time  = it.
These expansions are needed to form a well-defined numerical problem, cf. the
discussion in section 3.2. This time there are three free parameters, which

                                                                 78
characterise solutions. They are

                      SP , SP +, SP - ,                                 (205)

which can all three assume complex values. Note that the regularity condition
forces the anisotropy parameters, as well as their first derivatives, to vanish at
the South Pole. Thus all instantons are created isotropically, but subsequently
anisotropies can grow, as the second derivative can be non-zero.

     ()                              ()


  ()                                 


-
-                                             ()                      
-
-                                                           
                                           -
 ( + )                              -
                                           -
                                           -
                                           -
                                           -

                                                ( + )                 


 ( - )                                       -

                                             -

                                             -
                                    -

                                                ( - )


                                             -
                                             -
                                             -
                                    -

Figure 34: The evolution of the fields a, , � along the magenta contour drawn in Fig. 33.
The contour is parameterised by , and the dashed lines indicate the changes of direction of
the contour. All fields become real on the final hypersurface. Note that the anisotropies start
out at zero and then grow to reach the desired final values. Figures reproduced from [103].

    A numerical example of an anisotorpic no-boundary instanton is presented
in Figs. 33 and 34. Obtaining such solutions requires again an optimisation
procedure to tune the South Pole values of the scalar field and of the anisotropy
parameters. This can be done using a higher-dimensional Newtonian algorithm.
Compared to the numerical solutions discussed in section 3.2, a new feature
arises here, namely that singularities appear in the complex time plane, see
Fig. 33. These imply that one cannot use a Euclidean-plus-Lorentzian contour to
reach the final hypersurface. If one tried, one would in fact not reach coincident

                                                  79
real field values at all, but one would end up on the wrong sheet of the solution
(sticking to such a contour would put a limit on how large anisotropies can be
[102]). It proves useful to use a contour that is Lorentzian first, then Euclidean,
and followed by a further Lorentzian segment. The field evolutions along such
a contour are shown in Fig. 34. A sketch of this situation is presented in the
left panel of Fig. 35. When using this alternative contour, arbitrarily large
anisotropies can be obtained.


                                           f

    x  x

SP        x  x

Figure 35: Left panel: The presence of singularities (marked by purple crosses) prohibits
the use of a standard "Hawking" contour (in red). Rather, one must use a contour that
stays to the left of the singularities, such as the contour marked in green. Right panel:
The imaginary part of the Lorentzian action, as a function of final anisotropy values b�, for
b = 100,  = -1/2. Since the weighting scales as Exp[-Im(S)/], isotropic solutions have
higher weighting. Figures reproduced from [103].

    One can also calculate the action of these no-boundary solutions numerically.
The right panel in Fig. 35 shows the imaginary part of the action as a function
of the final anisotropy parameters, for fixed values of the final scale factor b and
final scalar field . This graph shows that isotropic solutions receive a higher
weighting e-Im(S)/, and are hence preferred. In a sense, this result confirm the
minisuperspace approach pursued previously, as anisotropic deviations are seen
to be suppressed. It also means that the no-boundary proposal assigns expo-
nentially higher probability to an isotropic than to an anisotropic beginning of
the universe.

Black holes
    The question of primordial black holes has recently come into renewed focus

� due to the observations of black hole collisions of various masses, as dark
matter candidates, and because of the existence of supermassive black holes in
the centers of very early galaxies. Primordial black holes could play a central
role in explaining these phenomena [104]. For such an explanation to be viable,
a reliable formation mechanism has to be discovered. Many current works focus
on specific dynamics during inflation, such as a phase of ultra-slow roll (for an
overview, see e.g. [105]). Such scenarios operate when the universe as a whole
is already very classical, and the predictions of such scenarios will be largely
unchanged by the no-boundary framework. However, another possibility might

                                                  80
be that black holes have been formed directly by quantum nucleation at the
creation of the universe. This is the question we will be concerned with here. In
other words, does the no-boundary wave function predict a significant quantum
creation of primordial black holes?

    This question was considered in a series of works by Bousso and Hawking
[106, 107, 108] and extended in [109, 110, 111, 112]. To start, it is helpful to look
at the relevant solution describing black holes in the presence of a cosmological
constant, i.e. the Schwarzschild-de Sitter (Kottler) solution

                           ds2  =    -f (r)dt2   +  dr2    +  r2d22  ,               (206)
                                                    f (r)

with  f (r)  =  1-  2M  -       r2.  There  are  two  horizons,  sitting    at  the  positive  so-
                     r       3
lutions to the equation f (r) = 0. The smaller horizon is the black hole horizon,

and the larger one the cosmological horizon. When M = 0, the black hole hori-

zon disappears and the solution describes a portion of de Sitter spacetime. Its

Euclidean version, as we have seen, is just the 4-sphere � in the Euclidean ver-

sion, the cosmological horizon becomes a regular point, as long as the Euclidean

time coordinate is made periodic with a suitable period [113]. The 4-sphere

is rounded off, and thus naturally satisfies the no-boundary requirements of

compactness and regularity at the South Pole.

What if M = 0? In that case there are two horizons, and in trying to form

a regular Euclidean solution, one is faced with the problem of specifying the

periodicity of the Euclidean time coordinate. At best one can render one of the

horizons smooth, but then at the location of the second horizon there will be a

conical deficit. If we insist on having an entirely smooth solution, then, apart

from pure de Sitter spacetime, we are only left with the possibility of making

the two horizons equal in size, by increasing the black hole parameter M to its
maximal value MN = 1/(3 ). This is known as the Nariai spacetime [114].
Interestingly, even though the two horizons are equal in size, the space between

them does not vanish, as shown in detail in [115]. The resulting Euclidean

metric can be written as

                        ds2  =  d 2  +  1                     +  1  d22  .           (207)
                                            sin(  )2dx2          


This is simply the product of two 2-spheres, each with radius 1/ . Again

this spacetime is appropriately compact and rounded off, and hence may serve

as a no-boundary instanton, with the no-boundary South Pole identified with

the South Pole of one of the two spheres.

The reason for writing the metric in the above form is that one can see

that if  is analytically continued back to Lorentzian time, the first 2-sphere

turns into a two-dimensional de Sitter line element. In analogy with the simplest

no-boundary solutions, cf. Eqs. (109) and (110), one performs this analytic con-

tinuation at the equator of the sphere containing the no-boundary South Pole.

Thus the Lorentzian spacetime that results from this instanton is a product

of two-dimensional de Sitter spacetime with a constant 2-sphere. The spatial

                                            81
sections have topology S1 � S2, which can be regarded as a 3-sphere with
holes punched through the North and South Poles, describing a pair of black
holes [106].

    Since we are interested in the probability for creating such black holes, we
must calculate the Euclidean action, which will determine the rate of creation.
It arises from one 2-sphere, plus one hemisphere of the second 2-sphere. A
general result for spacetimes with multiple horizons is that it is given by a
quarter of the sum of horizon areas (reinstating 8G momentarily) [108, 109,
110],

                       IE  =      1   (Ab.h.  horizon  +  Acosm.      horizon)   .           (208)
                               - 4G

For a product of two 2-spheres, one obtains, with 8G = 1, IE = -2 � 2 � A =
   162
-       .  Since  for  Nariai  black  hole  pair  creation   we       only  include    one   hemisphere

of one of the spheres, we must halve this result to obtain

                                         IE,N  =    82    .                                  (209)
                                                  -


Hence the rate N of nucleating regions of spacetime containing Nariai black
holes, compared to creating the universe as a purely de Sitter spacetime, is

                  N    =   N N        =  e-2IE,N      = e 162      -  242   =  e-  82  .     (210)
                           dS dS         e-2IE,dS                                  

When the vacuum energy scale  is a few orders of magnitude below the Planck

scale, then this rate is heavily suppressed.

   We may also ask what happens if we allow for the creation of smaller mass

black holes. As discussed above, these have conical deficits at least at the

location of one horizon. But they have actions that are perfectly regular, and

again given by the general formula (208); the actions interpolate between the

Nariai and pure de Sitter cases. These solutions have been argued to arise as

constrained instantons, i.e. as saddle points not of an ordinary path integral,

but of one in which an additional constraint has been put on the mass [111, 112].

One may then integrate over all masses, to find that the total rate of nucleation

of black holes in de Sitter spacetime can be approximated as (see [112] for the

details of this calculation)

                  MN                                         
             IE,N - IE,dS                                       
                               1 - e2(IE,dS -IE,N )       =  242           1  -  e-  82   .  (211)


Interestingly, this rate contains a perturbative contribution, which significantly
enhances the result. Still, for inflationary models in agreement with data, we
expect the vacuum energy to have been many orders of magnitude below the
Planck scale, and thus the rate of quantum formation of black holes from noth-
ing remains small. In a way, this may be seen as further confirmation that the
no-boundary wave function prefers the nucleation of homogeneous and isotropic
universes.

                                                  82
4. Link to Observations

    The simple models that we considered up to now were particularly suitable to
a detailed, and in many parts exact, treatment. However, when we make contact
with observations, we must include perturbations describing the actual distri-
bution of matter in the early universe. The most obvious point of contact of the
no-boundary wave function with observations occurs for the cosmic microwave
background radiation (CMB), which provides us with the earliest electromag-
netic picture of the universe. A specific and crucial question is whether the
no-boundary wave function, in combination with a suitable dynamical model,
can explain not only the homogeneous, isotropic and flat background spacetime,
but also the distribution of temperature fluctuations in the CMB. In order to
discuss this question, we will first review how perturbations are included in the
no-boundary framework. Then we will analyse the implications for observa-
tions, and confront no-boundary probabilities with what we know about the
early universe.

4.1. Perturbations

    We wish to extend our analysis to include cosmological perturbations. The
most important ones are scalar and tensor perturbations, leading respectively to
density perturbations and gravitational waves. We will treat perturbations at
leading order, which means that we must consider their action up to quadratic
order in perturbations. For definiteness, we will write out the analysis for tensor
perturbations below � these are always present, as they form a part of the
metric. The analysis of scalar perturbations proceeds in close analogy, and we
will simply quote the results at the end. The standard theory of cosmological
perturbations is discussed in numerous references, see e.g. [116].

    Tensor perturbations arise as transverse, traceless perturbations of the spa-
tial metric,

gij with gii = 0, Digij = 0 ,                                  (212)

where Di denotes a covariant derivative formed from the spatial background

metric, which is the metric on a 3-sphere here. Tensor perturbations arise in

two polarisation states +, �, each of which may be decomposed in terms of har-

monics on the 3-sphere, gj+k,� = h(t)Gj(lk) = h(t)  l    n     clnm (Gj k )lnm ,
                                                    n=2  m=-n

satisfying the eigenvalue equation

DiDiG(jlk) = -[l(l + 2) - 2]G(jlk) ,                l  2,      (213)

where l is the principal quantum number on the sphere and cnl m are Fourier
coefficients [117]. We will consider a single such mode, with amplitude h(t),
as at leading order these modes evolve independently. The treatment can be
extended straightforwardly to include a collection of modes, with the total wave
function becoming a product of the individual wave functions for all modes.

                                    83
    Thus our aim is to calculate the no-boundary wave function including a
single tensor harmonic

                                                      a1      h1            ei

                       (a1, h1) = dN                     Da          Dh          S  ,          (214)

                                                C

where h1 denotes the (real valued) amplitude of the tensor perturbation on the
final hypersurface. This type of calculation was first performed by Halliwell and
Hawking [118]. The total action S = S(0)[a, N ] + S(2)[a, N, h] now consists of

the background part we had before, plus a term for the tensor perturbation

                                                              2                              
                                            N dt a3
           S(2)[a, N, h]       =   1                       h       - a l(l + 2) h2 ,           (215)
                                   2                       N

where we assumed the background metric ds2 = -N 2dt2 + a(t)2d23 and where
the spatial term arises from the eigenvalue equation (213) combined with a

curvature term [119].       The equation of motion that follows from this action
reads
                                         a        N2
                               h�  +  3  a  h  +  a2  l(l  +  2)h  =  0  .                     (216)

We will assume that the backreaction of the perturbations on the background

is negligible. This means that the background part of the path integral can be
performed independently, and moreover will be approximated by a collection of

saddle points. The path integral over tensor perturbations is then performed

with the background fields taking their saddle point values. That is to say, the
path integral for tensor modes is a quadratic integral in perturbations, and can

thus be performed exactly. All that is required is the saddle point solution. In

other words, we must solve the perturbation equation (216) on no-boundary

saddle point geometries.

With a cosmological constant   3H2, the no-boundary saddle point is

given  by  a( )  =  1  sin(H ),    cf.   section   3.2.    Here       denotes       Euclidean  time,  i.e.
                    H
N = i and  = it. The equation for the tensor perturbations then becomes

                       h,   +  3H  cot(H )h,          -    H2l(l + 2)       h  =  0    .       (217)
                                                           (sin(H ))2

This equation possesses two solutions,

                    F1( )   =  (1 - cos(H ))l/2(cos(H ) + l                    + 1)       ,    (218)
                                        (1 + cos(H ))(l+1)/2                                   (219)

                    F2( )   =  (1 + cos(H ))l/2(cos(H ) - l                    -  1)      ,
                                        (1 - cos(H ))(l+1)/2

so that the general solution is a linear combination of these. Note that these
solutions behave very differently near the South Pole  = 0. Most importantly,
F2( ) diverges as   0, and regularity at the South Pole forces us to eliminate

                                                   84
this solution and retain only F1( ). In fact, near  = 0, we have F1( )   l, i.e.
this mode vanishes at the South Pole and grows away from there. Moreover,
the shorter the mode, the more suppressed it is near the South Pole. Thus the
correct solution, satisfying regularity at the South Pole and reaching the value
h( = f ) = h1 is given by

                             h( )  =   F1( )   h1  .                           (220)
                                       F1(f )

For a numerical example see Fig. 36. In the example, the mode function is
plotted along the usual Hawking contour, i.e. following a Euclidean time path
until the background 4-sphere has grown to its equator, followed by Lorentzian
evolution along the de Sitter hyperboloid. In the Euclidean regime, the mode
function is growing monotonically, while in the Lorentzian region it is oscillating.
For completeness, let us also write out the relevant solution in physical time,

                    i     l             i      -      l+2         i(l + 1)
               sinh(H t)           sinh(H t)            2        sinh(H t)
                          2

F1(t) =  1  +                1  -                          1  -             .  (221)

This way of writing the solution makes it clear that at late times F1  1. This
solution represents the Bunch-Davies vacuum [120], for a closed spatial slicing.

            4

            2                Re[h(t)]

            0

            -2               Im[h(t)]

            -4                                                   

                0  5 10 15 20 25 30 35

Figure 36: An example of a tensor perturbation mode, with H = 1/10, l = 15, h1 = 1. The
solution is plotted along the standard Euclidean-plus-Lorentzian contour, parameterised by
a parameter . The transition from Euclidean to Lorentzian is indicated by the thin vertical
line at  = 5.

    We are also interested in the action of the perturbations. On-shell, we may
use the equation of motion (216) in the action (215), which turns it into a surface

                                       85
term

       So(2n)-shell[a, N, h]  =   1       dt a3h 2 + a3hh� + 3a2a hh
                                 2N

                              =   1    a3hh     |t=tf
                                 2N

                              =  ia21  l  +  1   l(l  + 2)        -  1 h21                              (222)
                                  2             -i     H 2 a12                                          (223)

                              =  -  l(l   + 2)a1  h12  +  i  l(l  + 1)(l    +  2)   h12  +  O(a1-1)  ,
                                           H                        2H 2

where we used the fact that the perturbation vanishes on the initial hypersurface,
and where we expanded at large final scale factor a1 to obtain the last line. This
implies that, for a1  l/H, the wave function receives the following factors at
the saddle points, for each wave number and polarisation,

                                             -  l(l+1)(l+2)  h21 -i  l(l+2)a1  h21
                                                     2H 2                 H
                                   e . (2)                                                              (224)

Note that the weighting is a Gaussian, and independent of a1. The dependence
on l3/H2 implies that the spectrum is scale invariant (because the background

is exact de Sitter space here), and the amplitude of perturbations scales as the

inverse of the square of the Hubble rate. The phase grows with the scale factor

a1, as a reflection of the approximate classical behaviour of perturbations on

super-Hubble scales. Thus we recover standard results in inflationary cosmology.

But there is a crucial difference: here we did not have to assume the initial

Bunch-Davies vacuum state (220) or (221) � rather, regularity at the South

Pole forced us to choose this solution. Thus the no-boundary wave function

automatically implies the Bunch-Davies state for perturbations.

    We are now in a position to explain a result that we have used repeatedly

in this review, and which concerns the distinction between stable and unstable

saddle points. Above, we calculated the wave function for tensor perturbations

on a Hartle-Hawking saddle point geometry. This geometry may be specified

by a combination of Euclidean and Lorentzian parts, as detailed in Eqs. (109)

and (110). The geometry we focused on corresponds to one of the saddle points

in the lower half plane of the lapse function in section 3.6. However, because

the Einstein equations are real, the complex conjugates of these geometries are

also solutions to the equations of motion. Moreover, since the final scale factor

is real, they also obey the imposed final boundary condition (and in fact, these

saddle points are picked out in the tunneling proposal [41, 42, 43]). The only

thing that changes is the regularity condition at the South Pole, which changes

from a = +i to a = -i (in physical time). This seemingly innocent change has

profound consequences [121]: it changes the mode function (221) and the action

(223) to their complex conjugate values (note that the South Pole then resides

at  t  =  -i      rather      than  t  =  i      ).   Then,     for perturbations,          we  would obtain
              2H                             2H
factors of the form

                                                     l(l+1)(l+2)  h21 -i  l(l+2)a1  h12
                                                          2H 2                 H
                                e . (2)          +                                                      (225)

                                 unstable

                                                       86
Thus, the distribution of perturbations would be given by an inverse Gaussian.
It might appear that this is not problematic per se, as the path integral con-
verges and leads to a finite result. However, extrapolating this result to large
amplitudes one concludes that such a wave function is not normalisable and
thus does not represent a physically acceptable state. Even if one were to imag-
ine that at large amplitudes the weighting would turn around and render the
wave function normalisable, the physical implications would point to an incon-
sistency: larger perturbations would be more likely than smaller perturbations.
The most likely outcome would then be the largest fluctuations for which we
still trust our calculation, for all perturbation modes. This is completely at
odds with observations: fields would be in the opposite of their ground state �
all fields would be predicted to fluctuate wildly, which is simply not seen. An
isotropic universe would be a highly unlikely outcome. One might speculate that
the problem arises by the choices made near the South Pole, and that different
UV-physics (e.g. in the guise of modified dispersion relations) might cure the
problem, but this option has also been shown to be unlikely to work [122]. For
these reasons, we term such saddle points unstable, and they must be avoided
if we are to trust our calculations.

    The last point can also be turned around: in the no-boundary wave function
perturbations are predicted to be in their ground state, and as such perturba-
tions are likely to be small. This provides a physical justification for the minisu-
perspace simplification we used before, since it implies that highly symmetric
spacetimes are in fact favoured and this renders the results of minisuperspace
calculations believable.

    Analogous results can be obtained for other perturbations, in particular
scalar perturbations. These give rise to density perturbations in the early uni-
verse. They can be described rigorously in terms of a gauge-invariant curvature
perturbation  (see in particular [119, 123, 124]) with action

S = dt a32 - a(n2 - 1)2 ,  (226)

where  = -H /H2 = 2/(2H2) is the slow-roll parameter and with mode
numbers n  N. The action for scalar perturbations is suppressed by the
slow-roll parameter  [125, 33] (in the exact de Sitter limit,  = 0, the scalar
perturbation is pure gauge). The analysis proceeds entirely in parallel with that
of tensor fluctuations, and leads to the following approximate weighting factors
in the wave function (at large scale factor values)

| |    e-  n3   12  .      (227)
           H 2

Compared to the tensor fluctuations, the main difference is that the amplitude
of scalar fluctuations is enhanced when the potential is suitably flat, i.e. when
 is small. But apart from that difference, we obtain the same consequences,
namely fluctuations that start with zero amplitude at the South Pole, in the
Bunch-Davies vacuum state, and that subsequently grow to reach real values 1
(with a Gaussian probability distribution) at late times.

       87
    The analysis of perturbations can be generalised to situations in which the
background itself is not isotropic, see for example [79]; in a sense one is then
dealing with small perturbations superimposed on larger perturbations.

    Moreover, fermions can be included [126] (see also the briefer description in
[127], and for extensions including supersymmetry see e.g. [128, 129, 130]), and
it is again found that they start out being zero at the South Pole. This is a
very general feature of the no-boundary proposal, namely that it implies that
quantum fields start out in their vacua.

    Up to now, we analysed perturbations evaluated at the saddle points of the
background. Can we also say something about the perturbations off-shell? For
this, we take another look at the simplest minisuperspace model, which is that
of section 3.6 containing a cosmological constant and considering RW metrics.
We will specialise to the case where we impose an initial momentum condition10.
Off-shell in the lapse, the scale factor is given by (cf. Eq. (170))

         q�(tq) = H2N 2(tq2 - 1) + 2N i(tq - 1) + q1 ,                        (228)

and in these variables, the perturbation equation (216) reads

                 h�   +  2 qq�� h  +  N2   l(l  +  2)h  =  0,                 (229)
                                      q�2

with a dot denoting a derivative w.r.t. tq here. The solution to this equation is
given in terms of Legendre functions,

h(tq) = q�-1/2 (c1 LegendreP[1, , x] + c2 LegendreQ[1, , x])                  (230)

=  1  -          l(l  + 2)            ,         x=             H2Nt + i    ,
                 +    i)2 -
         (H 2 N              H 2 q1                     (H2N + i)2 - H2q1

where c1,2 are integration constants that need to be fixed to satisfy the bound-
ary conditions. We are only concerned here with the question of whether such
perturbations are well behaved, or whether they can be singular. Clearly, the
solutions above blow up when q� passes through zero, unless the Legendre func-
tions vanish suitably fast at those events. But this happens only at the saddle
points, where from the results above we know that perturbation modes vanish
as hsaddle  tql/2.

    Further, it is known that the Legendre functions have branch points at x =
�1. In fact, it can be seen straightforwardly that the condition for having branch
points is equivalent to the condition that q� passes through zero. Thus, off-shell,
the perturbation modes are well behaved unless the background passes through
zero. The locus of such points was already discussed in section 3.6, with the
results shown in Fig. 27. Thus, the red dashed lines in this figure correspond
to locations where the perturbations blow up, and where we cannot trust our

  10The case with an initial Dirichlet condition was discussed in [77, 79]. The results discussed
here are original work.

                                                  88
analysis. In defining integration contours, it would therefore be prudent to
circumvent those singular curves. In the present example, this can be done
without changing the asymptotic regions of the contours of integration, i.e.
without changing the results obtained at background level. Note however that
the saddle points themselves sit right on the boundary of the singular curves.
We will encounter a closely related phenomenon in section 5.4, where we will
discuss further criteria that geometries might have to satisfy to be considered
reliable. We should also remark that studies of off-shell perturbations have
been rather few in number so far, and that this topic provides opportunities for
further research.

4.2. Probabilities

    In section 2.4 we saw how one may define relative probabilities in quan-
tum cosmology. A requirement is that the wave function becomes of WKB
form, which we saw occurs for the no-boundary wave function under certain
conditions. The two examples we encountered are an inflationary phase and an
ekpyrotic phase, in both cases lasting at least a few e-folds, cf. also section 3.5.
No-boundary saddle point solutions then receive a significant weighting, which
is conserved for a series of instantons with final boundaries following a classical
history. These weightings lead to relative probabilities which, in the presence
of a scalar field with an appropriate potential, we recall are given by

                          242      s
                                   P  e , ekp  (231)
Pinf  e V (SP ) ,                  |V (SP )|

where s > 0 is a numerical factor depending on the slope of the potential. The
probabilities are relative since the overall normalisation of the wave function is
unknown, and presumably depends on the UV completion of the theory under
consideration. If several such saddle points contribute to the wave function,
then once perturbations are amplified these have the characteristic that they
decohere the saddle points [26], which from then on evolve as essentially separate
universes [27]. We may thus focus on individual saddle points at this stage. We
will discuss the implications for inflation and ekpyrosis in turn, and at the end
compare them.

    The most striking feature of the expressions in (231) is that they favour low
values of the potential. For inflationary models, this leads to two immediate
puzzles. The first is that it would be vastly preferable for the universe to nucleate
in the current dark energy phase, rather than at a much higher, inflationary
value of the potential [131], see also Fig. 37. The current dark energy phase
is equally suitable in bringing about a classical universe, as it entails the same
kind of attractor behaviour as an inflationary phase, only with a vastly lower
expansion rate. This would however result in an essentially empty universe.
One might object that the thermal fluctuations [113] implied by a quasi-de
Sitter phase would eventually produce conscious observers (so-called Boltzmann
brains), and that the combined probability of nucleating a vast empty universe
and then forming Boltzmann brains would still be higher than nucleating a
small, inflationary universe [131]. However, serious doubts as to the long-term

                               89
stability of de Sitter spacetime have arisen in recent years, in particular the
issues codified in the corresponding swampland conjectures [132, 133]. From
these it seems plausible that the current dark energy phase will simply not last
long enough to make the presence of Boltzmann brains a realistic prospect. This
is in fact something that can be tested, in the sense that this hypothesis implies
that the dark energy equation of state cannot be constant. Future dark energy
surveys will eventually be able to tell.

    Given that we are not directly interested in the bare probability for nu-
cleating a universe, but rather in the conditional probabilities for nucleating
universes that may include observers (this could be weakened to the require-
ment of containing large, durable structures such as galaxies) [134, 135, 45], we
should thus focus on no-boundary instantons that start out on the inflation-
ary part of the potential. Here we encounter the second puzzle: the preference
for low values of the potential means that, amongst inflationary histories, the
favoured ones appear to be those that last only a few e-folds. The most likely
histories in fact would be those lasting the bare minimum of e-folds required to
satisfy the conditions for e.g. the occurrence of galaxies. Yet our observations
are not compatible with such a short inflationary phase, they indicate that a
minimum of about 60 e-folds is required to explain the observations of the CMB
[33]. There currently exists no consensus on how this second puzzle may be
resolved, or whether it in fact invalidates the no-boundary proposal. We will
discuss a few possible resolutions.

 2.x 10 -10  In ation          why nucleate          1.x 10 -8  Cyclic  likely to nucleate
1.5x 10 -10                    here?                 5.x 10 -9          here, or here
                 why not here
 1.x 10 -10      or here?                       V()           0
                                                                   V()
5.x 10 -11
                                                     -5.x10 -9

0                               -1.x10-8                                                    

-2.0 -1.5 -1.0 -0.5 0.0 0.5 1.0 1.5                  -2.0 -1.5 -1.0 -0.5 0.0 0.5 1.0 1.5

Figure 37: Left panel: An inflationary potential. Why should the universe start high up on
the potential, when, at least naively, the probability to nucleate at lower values appears to be
higher? Right panel: A cyclic potential. The highest likelihood is to nucleate at low absolute
values of the potential, meaning either at the onset of the ekpyrotic phase or during the dark
energy phase.

    The first is to resort to strong anthropic reasoning [135]: if it happens to
be the case that conscious observers require an old universe, that is roughly
spatially flat and contains many galaxies, then a long inflationary phase is es-
sentially required by fiat. In such a case, the main purpose of the no-boundary
proposal would be to explain other features of the universe, such as correlations
in the fluctuations of the CMB. Such strong anthropic reasoning can never be
logically ruled out, yet (and to some extent because of this) it closes the road
to finding deeper, and more useful, explanations. There is a clear risk that

                                                  90
the road block is simply due to our lack of imagination. Also, if the anthropic

argument really were true, we should expect to be living right at the edge of

possible existence. This does not appear to be the case: the universe could

have developed more galaxies, or fewer, and the spatial curvature could have

been more positive, or more negative, yet this would hardly have affected the

emergence of life on Earth.

It has also been suggested that, because we are interested in the conditional

probability of us observing the universe to be in a particular state, we should

allow for the fact that we could be in any possible location in the universe. Put

differently, if there is a certain likelihood for observers to come into existence,

then if the universe is larger then the total probability ought to be higher,

precisely in proportion to the spatial volume. This is known as volume weighting

[61, 5]. Let us see what the consequences would be for inflationary predictions. If

there are Ne e-folds of inflation, the probability measure should thus be adjusted

according to

              Pvolume weighted  =  e3Ne       =  e3Ne  +      242  )  .  (232)
                                                          V (SP

For small Ne the probability decreases with increasing potential, but we may
hope that for large Ne it will increase again. Thus we may ask where on the
potential the minimum probability occurs. This can be estimated as follows,

              0 = P,               242  +  3     V   d
                                    V            V,
                                                          ,

                             =  -  242V,   +  3  V
                                      V2         V,

                                   V,2  =   1    .                       (233)
                                   V3      82

In terms of the slow-roll parameter the last condition can also be written as
V  , and in fact it corresponds to the onset of eternal inflation. Thus we
obtain the result that it is only in the regime of eternal inflation where the
volume weighted probability starts going up again. But in eternal inflation
the spatial volume in fact becomes infinite. If one took this seriously, after
normalization there would be zero probability for non-eternal inflation, and all
the probability would be concentrated in the eternal regime, without a clear
preference for different parts of the potential. In fact assigning probabilities in
the eternal inflation regime is a notoriously intractable problem. The underlying
reason for this might simply be that eternal inflation is not physical. It leads
to ill-defined semi-classical amplitudes [48], and in fact is also conjectured to
conflict with quantum gravity consistency conditions [136, 137].

    Though volume weighting did not produce the expected turn-around in prob-
abilities, it could still be that we do not understand the total probability mea-
sure well enough yet. This might be due to oversimplifying the model. Infla-
tion is a dynamical attractor, and many originally slightly inhomogeneous and
anisotropic universes would lead to essentially the same final outcome. Hence,
it might be that many more histories are effectively indistinguishable from the

                                   91
Robertson-Walker background we assumed in calculations. These would en-
hance the total probability for a long inflationary phase. Another effect is that
a higher potential also leads to more structure formation, i.e. more galaxies.
It is conceivable, though this is plain conjecture at the moment, that when all
these effects are taken into account, the probability for a long inflationary phase
could become very significant, especially near a broad maximum in the potential
(a broader maximum would allow for more histories with quasi-indistinguishable
outcomes). Performing this calculation will however require us to go beyond the
minisuperspace framework, and this is currently an open problem.

    Let us mention one by-product: if there exist several regions in the scalar
potential that could all lead to long inflationary phases and viable universes,
then the lowest such region would seem to come out as preferred, due to the
basic preference for low potential values [127]. This would imply that plateau
models of inflation would be preferred over power-law potentials, and in fact one
would then also expect the tensor-to-scalar ratio to be small. From this point of
view, the present non-detection of primordial scale-invariant gravitational waves
is not surprising.

    A further possibility is that the early universe history is more complicated
than a purely inflationary expansion phase. In particular, it has been suggested
in [138] that after a modest initial expansion, the universe could recollapse,
then bounce due to the spatial curvature and subsequently enter a much longer
inflationary phase. This would have the advantage that the scalar field could nu-
cleate much lower on the potential (and thus with higher probability) and then
run up the scalar potential during the collapse and bounce phases. Multiple
bounces are also conceivable, though with each additional bounce the required
initial conditions become more finely tuned. In such a case the wave function
would contain various histories in competition with each other [139], but deter-
mining which one truly dominates the wave function currently remains out of
reach, as the measure on the full set of geometries is unknown.

    All this being said, let us mention that inflationary models are quite gener-
ally in tension with string theory, in the sense that no unambiguous embedding
of inflation into string theory has been found to date. Simple string compact-
ifications, and their swampland codifications [132, 133], certainly seem to be
in conflict with the inflationary no-boundary wave function [140]. Most likely,
one will therefore have to go beyond the simplest framework, and include non-
perturbative effects as well as typical string theory objects such as orientifolds
and various branes, to obtain realistic inflationary vacua [141]. This is an active
research area.

    Turning our attention to ekpyrotic models, we can see from (231) that the
situation is reversed. The preference for a low initial absolute value of the
potential translates into a preference for a long ekpyrotic phase [68]. If there
is a potential landscape with several ekpyrotic regions, this preference for low
values would however not easily distinguish between different regions, as the
predictions of ekpyrotic models are determined by what occurs further down
the potential. In cyclic models, there is also the possibility of nucleating a
universe in the dark energy phase [62], see Fig. 37. Though this universe would

                                                  92
again be empty at first, just as in inflationary models, it would not remain so,
as the universe would collapse and at the bounce matter and radiation would
be produced for the subsequent expanding phase. Let us mention that with
simple effective models for the bounce, one can extend the quantum cosmology
framework to include the bounce phase, and obtain instantons that contain
the phases of nucleation, contraction, bounce and expansion [69]. However,
as discussed previously, it remains an open question whether bounce models
can be consistently quantised in general, i.e. whether they are also consistent
and instability-free away from RW backgrounds. Unfortunately, this attaches a
question mark to all bounce models. Moreover, ekpyrotic potentials may be just
as hard to obtain in string theory as inflationary potentials, due to the extreme
steepness they require [142]. But if both ekpyrotic and inflationary models turn
out to be possible, then the basic preference for low potential values expressed
in (231) would give the edge to ekpyrotic, bouncing cosmologies.

4.3. Taking Stock: What Does the No-Boundary Proposal Explain?

    It seems like a good point now to take stock, and crystallise the main ex-
planations that the no-boundary wave function may offer. Here we will focus
on the achievements of the no-boundary proposal in a 4-dimensional effective
approach to cosmology. A more detailed discussion of links to string theory and
open questions will follow in sections 5 and 6. The list is rather impressive:

� The no-boundary proposal specifies a single quantum state for the entire
   universe, and as such provides a theory of (probabilistic) initial conditions.

� In fact, it provides a unification of quantum gravity dynamics and initial
   conditions, expressed in the path integral approach to quantum theory,
   [143]

           f     i

(f ) =        e     S  .  (234)

        C

The dynamics is encoded in the action S, and the state in the boundary
conditions and integration ranges C of the integral. Thus a single mathe-
matical object combines the dynamics and the specification of the state.
This is why it is so important to understand the proper definition of grav-
itational path integrals. Moreover, the wave function depends on the final
field values f , and this dependence of the wave function on spatial hyper-
surfaces in some sense makes the integral also an intrinsically holographic
object. This property will be discussed further in section 5.2.

� The no-boundary wave function explains how space and time became clas-
   sical at the early stages of evolution of the universe. This classicalisation
   moreover requires the presence of a dynamical attractor, such as inflation
   or ekpyrosis. The attractor drives spacetime to classicality, and allows for
   the definition of probabilities for different classical histories of the universe.

93
� Once spacetime has become classical, one naturally obtains the framework
   of quantum field theory in curved spacetime.

� The big bang singularity is resolved. No-boundary instantons are finite
   and regular, and simply do not contain a big bang singularity. We can
   only say things with confidence about the universe in the regime where
   spacetime has already become effectively classical. Going back in time,
   there is no operational way of saying something about the phase when
   the radius of the universe was smaller than the primordial Hubble scale.
   The latter phase is better thought of as a quantum tunneling/nucleation
   event, which was required to produce space and time in the first place.

� Two immediate implications of the no-boundary idea are that the universe
   is finite in spatial extent, and that the overall average spatial curvature is
   positive. However, the spatial curvature might very well have been diluted
   to such an extent as not to be measurable today.

� Quantum fields are predicted to initially have been in their vacua. The
   dynamics of the universe may then excite certain fields.

� Homogeneous and isotropic initial conditions are favoured over less sym-
   metric ones. The initial state of the universe is thus one of relative sim-
   plicity. Combined with the previous item stating that quantum fields start
   out in their vacua, this provides appropriate low entropy initial conditions
   for the universe. This also provides an appropriate starting point for the
   2nd Law of thermodynamics.

� At the nucleation of the universe, only scalar fields may have a non-zero

energy density. Other matter fields are not permitted. This follows from

the  equation  of  continuity    +  3  a  (  +  p)  =  0.  At  zero  scale  factor  this
                                       a
equation remains regular only if the sum of energy density and pressure

+p vanishes, which in turn only a scalar field can (momentarily) achieve,

when its kinetic energy is zero, cf. (138). Thus no initial radiation or

ordinary matter are allowed � these must be created later, for example

during reheating. This setting fits well with cosmological models that use

scalar fields as their main dynamical matter ingredient.

Some potential additional explanations that the no-boundary proposal may offer
should still be considered to be works in progress. This concerns the predictions
regarding inflation in particular. As we saw, it is not yet clear whether the no-
boundary wave function assigns high probabilities to long inflationary phases or
not, or to which particular type of inflationary background. Tied to this is also
the question of whether or not the observed near-flatness of the current universe
is explained, i.e. whether the positive spatial curvature of no-boundary solutions
is sufficiently diluted. These important questions will require more work.

                                    94
5. Link to String Theory

    The no-boundary proposal is formulated in 4 dimensions, with the theory of
gravity being general relativity. However, it is widely expected that quantum
gravity will require further, or different, fundamental ingredients. In the present
section, we will ask whether the no-boundary proposal is compatible with quan-
tum gravity, and with string theory in particular. Is it perhaps even required
under some circumstances? And what do we learn by applying no-boundary
ideas to string theory?

    Before embarking on this, let us make a comment of principle. In string
theory, one starts with the quantisation of a string. Classically, the world sheet
admits a conformal/Weyl symmetry, which must be preserved under quantisa-
tion. This leads to non-trivial requirements, specifically that the spacetime in
which the string moves must satisfy the equations of motion of certain super-
gravity theories (plus corrections thereof at higher orders in the string length
) [144]. One may now wonder whether it is consistent to consider a path in-
tegral of this effective higher-dimensional supergravity theory, since one is then
in some sense quantising the theory again. In well-known examples (meaning
examples with significant amounts of preserved supersymmetry) this procedure
is known to be consistent, for a striking example see [145]. However, as quite
generally in string theory, not much is known in non-supersymmetric situations.
We will proceed with optimism.

5.1. Robustness

When gravity is quantised, effective terms with higher derivatives are gener-

ated from graviton loops at higher orders in  [49]. These terms typically arrange

themselves as higher powers of the Riemann tensor, and derivatives thereof. A

pertinent question, even when sticking to an effective 4-dimensional descrip-

tion of gravity, is thus whether no-boundary solutions are still good (regular,

finite action) solutions of the corrected theory. In other words, are no-boundary

solutions robust to the inclusion of quantum corrections? In string theory, such

higher order terms also arise, now accompanied by coefficients that contain

powers of the string tension . Thus, the analogous question arises there too.

The most crucial aspect of this question is to see whether the rounded-off

region near the South Pole of no-boundary instantons remains an acceptable

solution. We analysed this question briefly in section 3.1, and in fact used it to

motivate the no-boundary proposal. We will fill in a few more details here.

As we discussed in section 4.1, perturbations with wave number l decay near

the South Pole as tl. Hence we may actually focus on homogeneous and isotropic

backgrounds, knowing that perturbations may arise away from the South Pole,

but that they play no crucial part in the question of whether such solutions

exist at all. As stated in section 3.1, see Eqs. (97) and (98), once we restrict to

closed RW universes (96), with lapse N , the only non-zero components of the

Riemann tensor   are given in terms of A1  =  a 2+N 2  and  A2  =    a�  2  .  An  action
                                               a2N 2               aN
which is a function of the Riemann tensor may be expanded in terms of these

                 95
combinations as

    S=    d4x-gf (Riemann) = 22                       dtN a3           cp1,p2 Ap11 Ap22 ,   (235)

                                                               p1 ,p2

where cp1,p2 are coefficients, and the power of the Riemann terms is given by
P = p1 + p2. The constraint equation can be found by taking a derivative of the
action with respect to the lapse function, with the result [146]

0=  S  = 22          cp1 ,p2  2p1(p2   -   1)  aa 2  Ap22 A1p1-1  +  (1  -  p2)a3Ap22 A1p1
    N                                          N2
             p1 ,p2

             +    p2(p2  -    1)  aa a(3)  A2p2-2Ap11  -   p2(2p1    +  p2  -  3)  aa 2  A2p2-1Ap11  .
                                   N4                                              N2

                                                                                            (236)

The equation of motion for the scale factor follows from taking a time derivative
of the constraint, and hence we do not need to consider it separately. The
constraint is in fact invariant under the following transformation,

                         t  -t,                                                             (237)
                                         a(-t) = -a(t) ,

                         a  -a,

which implies that the scale factor is odd in t. The no-boundary ansatz, with
its Euclidean rounding off at a = 0 then corresponds to a series expansion

                              =   a1t  +   a3  t3  +  a5   t5  +  O(t7)  ;                  (238)
                     a(t)                  6          120

                     a21 = -N 2 .

In physical time, we have a12 = -1 i.e. a1 = �i. For any solution, there exists a
time-reversed solution obtained by sending t  -t, and moreover the solutions
come in complex conjugate pairs. Hence there are always four related solutions
(two of which can be eliminated by fixing the initial expansion rate). With this
ansatz, the components of the Riemann tensor read

       =  -  a3   +  a23 - a1a5   t2 +     a3a5 - a1a7         t4 + O(t6) ;
A1           a13        12a41                  360a41


A2     =  -  a3   +  a32 - a1a5   t2 -     10a33 - 13a1a3a5 + 3a21a7               t4 + O(t6) .
             a31         6a41                          360a51
                                                                                            (239)

Importantly, the series expansions start at order t0, and not t-2 as naively

expected, and this is the main reason why no-boundary solutions can have

finite action. Solving the constraint equation leads to the following expressions

                                               96
at the leading orders,

Order t :                cp1 ,p2  a14-P  a3P  -1  p2 - p1    = 0;                         (240)
Order t3 :               N 2P                                                           = 0,
                p1 ,p2
                                                                                          (241)
                         cp1 ,p2  a13-P a3P -2    a23 � G3[p1, p2] + a1a5 � G5[p1, p2]
                         N 2P
                p1 ,p2

with

                         G3[p1, p2]  =   1    p21 - 15p1 + 6 - 4p22 + 12p2      ,       (242)
                                         6                                              (243)

                         G5[p1, p2]  =   p1(1 -   p1)  -   2p2(1 -     p2)  .
                                              6                  3

Again it is a consequence of the no-boundary ansatz that there are no non-

trivial conditions at negative powers of t. The order t condition is most easily

solved by cp1,p2 = cp2,p1 , which turns out to be satisfied quite generally, in
particular for all terms that are powers of the Ricci scalar R = 6(A1 + A2) and
all terms involving the quadratic combinations R�R� = 6 A12 + A22 and
R� R� = 12 A12 + A1A2 + A22 [147, 148]. The condition at order t3 then fixes
a5 in terms of a3, [146]

a5    �         cp1 ,p2  a13-P a3P -2G5[p1, p2]   =  -  a23  �         cp1 ,p2  a31-P a3P -2G3[p1, p2] .
                N 2P                                    a1             N 2P
        p1 ,p2                                                 p1 ,p2

                                                                                        (244)

At higher orders, the next coefficients a7, a9, etc. are then fixed in turn. Thus,

a full solution, with manifestly finite action, is obtained, with free parameter a3.

This parameter specifies the early expansion rate and, in the case where a scalar

field is added, is linked to the initial value of the scalar field. An explicit example,

considering the inclusion of a Gauss-Bonnet term, appeared in [149].

In string theory, additional terms appear, in particular with derivatives act-

ing on Riemann tensors. It is not possible to analyse such terms in full generality,

but it was shown in [146] that the first few correction terms, both in heterotic

and type IIB string theory, still admit no-boundary solutions with finite ac-

tion. This indicates a basic compatibility of string theory with the no-boundary

proposal.

5.2. Link to AdS/CFT and Holographic Definition

    The best understood example of quantum gravity is the AdS/CFT corre-
spondence [93]. In this correspondence, quantum gravity with fields that asymp-
totically approach Anti-de Sitter (AdS) spacetime is related to a conformal field
theory (CFT) that lives on a spacetime that is given by the conformal geome-
try of the asymptotic boundary. The manifold that the conformal field theory
lives on has one dimension fewer than the bulk gravitational theory, which is
why this setting is holographic. The great advantage is that conformal field

                                                  97
theories are very well understood, so that one can use this knowledge to learn
about quantum gravity. The drawback is that this only works for asymptoti-
cally AdS spacetimes, which do not correspond to our universe. Nevertheless,
it seems plausible that quantum gravity contains universal features which one
can uncover in this setting.

    There are two approaches that have been pursued in connection with quan-
tum cosmology: the first is to study AdS/CFT in order to gain insight into
gravitational path integrals. One can then try to translate this knowledge into
a cosmological context. And the second is to try to directly define the wave
function holographically, by linking it to AdS/CFT. We will describe both ap-
proaches in turn.

Gravitational path integrals in AdS

Gravity in asymptotically AdS spacetimes is generally better understood

than gravity in dS-like spacetimes. To some extent this is due to the fact that

in asymptotically AdS spacetimes there exists a clear (timelike) boundary, and

it is straightforward to fix the asymptotic geometry11. Connected to this is

the conjecture that one may describe the physics of such spacetimes by a dual

quantum field theory that lives on the (fixed) asymptotic geometry, and thus

does not involve gravity at all. In this way arose the realisation that a quantum

field theory can encode the same physics as a theory containing gravity and

describing dynamical spacetime of one dimension higher [93, 150]. This can be

used in some situations to check gravitational calculations by comparing with

known quantum field theory results. These considerations motivate us to look

at path integrals in the presence of a negative cosmological constant. In this

way we may hope to learn general lessons for quantum cosmology [17].

Specifically, we will analyse two setups: one in which we perform the ana-

logue of the Robertson-Walker calculation of the wave function in section 3.6,

and one in which we will add black holes. These calculations turn out to support

the implementation of the no-boundary wave function as a path integral with

a momentum condition. We will be brief here � full details were presented in

[17, 82]. As in [17], we will keep Newton's constant explicit here and write the

cosmological constant      -  3   in  terms of the   radius of curvature  l  (not to be
                              l2
confused with the wave number of perturbations in section 4.1).

We will once again look at the path integral (95) in minisuperspace, with

RW metrics of the form (156). We will impose a final Dirichlet condition q(t =

1) = R32 (i.e. the "final" radius of the 3-sphere is fixed to be R3) and an initial
momentum condition which we will parameterise by

                                  p0  =  -  3     ,                          (245)
                                            4G

intentionally leaving  arbitrary at first. Then, in complete analogy with the
calculations surrounding Eq. (171) in section 3.6, one may derive that the saddle

  11In dS this is conceptually more complicated due to the presence of a (observer dependent)
horizon, which shields observers from far-away regions.

                                                  98
points are located at

                                          N� = l2 � il R32 + l2 ,                                              (246a)
                                                                                                               (246b)
                                4G  S0(N�   )  =  (3   +  2)l2      �  2i      R32 + l2 3/2 ,
                                                                       l

where we also wrote out the action at the saddle points. It is instructive to look
at the saddle point geometries, which are given by

q�(tq) |N� = -             l � i                     2              l2 � il         R32 + l2     tq - l2(1 + 2) .
                                                                                                               (247)
                                    R32 + l2 tq2 + 2

We can immediately see that if we would like to have saddle point geometries
that close at t = 0, then we should choose  = �i. This is necessary, as otherwise
we do not include the entire bulk spacetime. With  being imaginary, note that
the saddle points reside on the Euclidean lapse axis, and as a consequence t
has become a spatial coordinate. The saddle point geometries are then purely
Euclidean geometries.

Figure 38: Left panel: Saddle points and steepest descent lines, for the case of AdS spacetimes

(all  q1  =  R32 )     or  for  dS  (small  universes  with  q1  <  3  ),  in  the  complexified    plane  of  the  lapse

                                                                                                    2
N.    Green regions indicate asymptotic convergence at angles 0 <  <                          3  ,   3  <  <  and

4     <    <  5     .  When         < 0,  the  upper  saddle  point  is    N+  and  the  lower  N-,     and  vice   versa
 3             3
for  > 0. Right panel: Geometry of the saddle points for  < 0. As the final scale factor

q1 = R32 is increased, the saddle points move apart. Figures reproduced from [82].

    We can restrict  further. When  = +i, the saddle point N- corresponds
to Euclidean AdS space. The second saddle point, N+, also describes a sec-
tion of complexified AdS space, but this time it includes a piece of reversed-
signature Euclidean AdS glued onto a part of Euclidean AdS. In other words,
this geometry contains a point where the scale factor passes through zero. Once

                                                             99
perturbations are included, we expect them to blow up at this point. Therefore,
this saddle point can actually be treated as being singular. Meanwhile, when
 = -i the situation is reversed and the two geometries are exchanged. The
flow lines in Fig. 38 indicate that N- is always the dominant saddle point. Thus
we find that we must choose  = +i in order for the dominant geometry to be
regular and closed. This is in fact the same condition that we imposed in the
no-boundary case, with positive cosmological constant, in (179) (and it is the
choice that leads to stable perturbations). Thus we see that the momentum
condition is vindicated by the AdS calculation.

    But there is more. The only integration contour for the lapse function that
completely projects out the singular saddle point is the combination of contours
C2 - C1, see Fig. 38. This combination in fact results in an Airy Bi function, of
the form [17]

                                              3         2
                                             4Gl
                        (R3)  Bi                        3               .                (248)

                                                           R32 + l2

In AdS one has to add counter terms to regulate the volume divergence (since
the volume contributes to the weighting of the wave function rather than to
the phase, as in the dS case). When these terms are added, one finds complete
agreement with the CFT result, which is known [151, 152], and is also given
by an Airy function. Since this takes us away from the cosmological context of
interest, we refer to [153, 17] for detailed discussions.

    For us, two things are worth noting: the first is that the required contour
of integration is neither Lorentzian nor Euclidean, but fully complex. The "av-
erage" of the two paths C2, -C1 is the Euclidean contour, but the individual
contributions are fully complex. Thus, even though the wave function is real,
we are forced to sum over complex metrics. The second point is that we can use
the AdS result and analytically continue it to positive values of the cosmological
constant. A priori, it is not clear that this is justified, as there is no understand-
ing what the intermediate complex values of the cosmological constant might
mean. However, mathematically we can simply perform the continuation to see
what we obtain. Reinstating , we can use the following formula

         182       2/3                                     182  2/3           
         -                     3             = 3 Ai                           3
    Bi                  1  -       q1                                   1  -     q1  ,   (249)

which shows that for positive  the wave function is better thought of as being

proportional to an Ai rather than a Bi function. When this calculation is done

in full [82], one recovers precisely the result (178).

    Let us mention a few more properties of the Airy function, which may clarify

some aspects of the calculation performed in section 3.6. When the final radius

of  the  universe  is  small,  q1  <   3  ,  then  the  saddle  points  are   Euclidean  (we  are

still in the nucleation phase), and the flow lines are essentially identical to the

AdS case in Fig. 38. But to obtain the Ai result rather than Bi, the contour

must be different, and this time the required contour is C0, which picks up the

                                             100
Figure 39: This graph shows the geometry of the saddle points when  > 0. At small scale

factor  q1    3  they   are   Euclidean,  but  then  turn  complex  for    q1  >  3   ,  with  increasingly   large

Lorentzian dS sections. Figure reproduced from [82].

upper saddle point only. In the dS case, this is the geometry that is regular
and does not have the scale factor passing through zero, see also Fig. 39. Note
that this means that at the nucleation of the universe, when q1 = 0, only the
vanishing geometry contributes and not the full sphere. In a sense this indicates
that non-trivial topologies do not contribute to the no-boundary wave function,
even though the wave function is non-zero when q1 = 0 � the latter property
was originally interpreted as suggesting that non-trivial topologies must be the
reason why (0) = 0 [2]. Here we see that an explicit calculation does not
support this interpretation, and a better explanation should be searched for.

Figure  40:  Saddle  points   and  steepest   descent  lines  when  q1  =  3   (left  panel)   and  when  q1  >  3

(right panel). A Stokes phenomenon occurs, and for large scale factors there are two saddle

points contributing to the path integral. This Stokes phenomenon is related to the appearance

of time. Figure reproduced from [82].

As the universe grows, the saddle points approach each other until they

coalesce     at  q1  =  3  ,  see  Fig.  40.  At  larger  values    of  the   final   scale    factor,  q1  >    3  ,

this degenerate saddle point splits into two saddles, which are now both relevant

                                                     101
to the path integral. Thus a Stokes phenomenon has occurred, and from having
a single Euclidean relevant saddle point we have gone to having two complex
geometries that are equally dominant. These complex saddle points contain a
Lorentzian section near the final boundary, that is to say time has emerged.
The wave function still remains real, as it is a sum over two complex conjugate
contributions, one from each complex saddle point. Thus, the overall wave
function remains timeless, yet the two complex saddles each contain time �
in a sense time flows in opposite directions in both saddles. It remains an
open question whether there could have been any significant interference effects
between these two saddle points in the very early stages of the universe.

    More insights can be learned by including black holes in the AdS calculation.
The calculation is relatively lengthy and we will simply mention the results here
� for details see [17]. Euclidean Schwarzschild-AdS black holes are described by
the line element

           ds2 =              d2             +      2   +  1  -   2M     d 2 + 2d22 ,              (250)
                                                    l2             
                         2    +1-  2M
                         l2         

where M denotes the mass of the black hole. The horizon radius r+ is given by

the  real  root  of  3   +  - 2M       =  0.  One   can      then     invert  this   relation  to  obtain
                     l2
the mass as a function of the horizon size

                                   M   =     1  r+  1   +    r+2      .                            (251)
                                             2               l2

The Euclidean manifold contains a conical singularity at  = r+ unless one
periodically identifies the  coordinate, with period [154]

                                             =  4l2r+         .                                    (252)
                                                3r+2 + l2

AdS/CFT then relates the mass M in (251) to the expectation value of the
Hamiltonian of a conformal field theory in a thermal state at an inverse tem-
perature  [155].

    The path integral can be performed by using a suitable choice of metric.
The appropriate variables were found in [84], and read

                         ds2  =  c(r)  d  2  -  b(r)    N  2dr2   +   b2(r)d22    .                (253)
                                 b(r)           c(r)

There is a radial direction r with 0  r  1, and the spatial slices have the
topology S1 � S2. As "outer" boundary conditions, we must fix the size of the

spatial slices to be

                         b(r = 1)  R2 ,                 c(r   =   1)          R1  .                (254)
                                                        b(r   =   1)

                                                102
                                                             N

                                      Large b.h.
                                      Small b.h.

Figure 41: Saddle points and steepest descent contours for R1 = 12, R2 = 10, l = 1. Arrows
indicate directions of descent. There are two singularities indicated by the small circles, one
at the origin and one on the positive imaginary axis. The dashed orange line is a possible
contour of integration, capturing the large black hole saddle, but also including the small
black hole and a further subdominant saddle point. Figure reproduced from [17].

On the inner boundary one can impose a regularity condition  (which is a
condition on c/(N b)(r = 0)) that implements the periodicity (252).

    The path integral/partition function then becomes

      Z(R1, R2) =                  dN  e  i  (SND (N )-SEAdS )  ,           (255)


where the background Euclidean AdS action is subtracted to regulate the vol-
ume divergence. The path integral admits five saddle points, whose nature and
locations depend on the final boundary conditions [17]. An illustrative example
is given in Fig. 41. Two of the saddle points describe black holes, one large
and one small. There are three additional saddle points that describe Euclidean
geometries � these are subdominant, or irrelevant, depending on the contour of
integration. Their CFT counterpart is currently unknown. A possible integra-
tion contour for the lapse is shown in the figure. As one can see, it is again
necessarily complex, and to obtain a real wave function (as expected in the
CFT) one should sum this contour with its reflection across the imaginary lapse
axis. The large black hole is always found to dominate over the small black
hole, which agrees with thermodynamic expectations [154].

    The partition function is interpreted as representing the canonical ensemble
at fixed temperature 1/, given that the size of the outer boundary is kept fixed.
One obtains


ln Z  =  R2       1+  R22          -  2M     -    1  +  R22    +   r+2   .  (256)
         T l2P        l2              R2                l2          l2P

                                   103
where lP =  G      is  the  Planck  length.  Using   standard        thermodynamic   relations
            c3

[156] one can calculate the expectation value of the energy


E  =        kB  T  2   ln Z  =   kB R2       1  +    R22  -     1  +  R22  -   2M    (257)
                       T           lP2               l2               l2       R2


as well as the entropy

                   S   = kB ln Z +     E   =    kB   r+2  =     kB    Area  .        (258)
                                        T       lP2             l2P     4

These relations satisfy the Quantum Statistical Relation [9]

                                 -kBT ln Z = E - T S .                               (259)

Now comes a crucial point: if we had imposed a Dirichlet condition at r = 0,

instead of the regularity condition , then we would have obtained an additional
surface term of magnitude r+2 at the horizon r+, and the partition function
would have come out as

                            -kB  ln Z    E    -S     +S      =  E     .              (260)
                                          T                      T

This would have corresponded more closely to the microcanonical ensemble, in
which one considers states at fixed energy. However, this does not agree with
the fact that we kept the size of the outer boundary fixed, which corresponds to
fixing the temperature. Hence, a proper physical interpretation of the AdS black
hole calculation requires the absence of a surface term on the inner boundary.
By direct analogy, this provides further support for the implementation of the
no-boundary wave function with a momentum condition.

    To summarise, we have found that AdS path integrals share many common
features with the no-boundary proposal, in particular the absence of a surface
term and the ensuing regularity/momentum condition at the "no-boundary"
point; the sign of the momentum condition corresponding to the standard Wick
rotation of quantum field theory; a sum over all field values implementing the
momentum condition; and a sum over complex (that is to say neither Lorentzian
nor Euclidean) metrics.

A Holographic Definition
    The previous discussion was rather conservative in that it tried to compare

no-boundary path integrals with similar integrals performed in the context of
AdS/CFT, and this showed that surprisingly similar features arise in the two
settings. However, there has also been a program, initiated by Hertog and Hartle
in [157] and developed in [158, 159, 160, 161, 162], to define the no-boundary
wave function more directly in terms of AdS/CFT (earlier ideas in this direction
include [163, 164, 165]). We will review this proposal here.

                                             104
                    y                                                

                    yf                                      f
                                                         d
                    yh
                                        h

                    a

                          SP
                                                      /(2H) x

Figure 42: Time contours used to represent the de Sitter instanton: the standard Euclidean-
plus-Lorentzian contour in red, and the "holographic" contour in green.

    To understand the proposal, we must return to the de Sitter saddle point

geometry, as described at the beginning of section 3.2. In terms of Euclidean
time  and with  = 3H2, the dS solution is given by

                          ds2  =   d 2  +   1  sin2(H )d32     .                       (261)
                                           H2

The usual contour used to represent this solution runs from the South Pole in
the Euclidean direction to the equator of the 4-sphere at  = /(2H), followed
by a segment in the Lorentzian direction defined by  = /(2H) + iy with
0  y  yf along which the metric is that of Lorentzian dS

                          ds2  =  -dy2  +   1  cosh2 (H y)d23     .                    (262)
                                           H2

The  scale  factor  then  reaches  the  final  value  b  =  1  cosh(H yf  )  at  time  f  =
                                                            H
/(2H) + iyf , cf. also Fig. 42.

But the physical consequences are unchanged if we deform the time contour,

as long as no singularities are present. In particular, the value of the action of the

saddle point (which is the quantity that enters the semi-classical wave function)

does not change. Consider then the contour marked in green in Fig. 42, and

which we will refer to as the holographic contour. The first segment, labelled

"a", starts at the South Pole in a Lorentzian direction, for  = iy with 0  y 

yh. Along this contour the metric reads

                          ds2  =  -dy2  -   1  sinh2 (H y)d32     .                    (263)
                                           H2

                                           105
This is the metric of Euclidean AdS (EAdS) spacetime, with cosmological con-

stant -, except that there is an overall minus sign in the metric, i.e. the

signature has been reversed. The scale factor reaches a final value that is imag-

inary,   with  magnitude      bh  =   1  sinh(H yh ).    The      second       segment,      labelled  "h",
                                      H
then interpolates horizontally between the EAdS region and the Lorentzian dS

region   along    =   x + iyh     with   0    x         .     The     metric      is  fully  complex  along
                                                    2H
this segment. Finally, on the last segment marked "d", the metric is that of

Lorentzian dS spacetime, see Eq. (262). The final value of the scale factor is

b  =  1  cosh(Hyf ).  It  is  larger  than    the  magnitude          of  the  scale     factor  bh  reached
      H
along the EAdS part of the contour.

    It is straightforward to evaluate the action along the various segments. For
this we may use the action (11) with N~ appropriately chosen along the different

segments, to find

                      Sa  =   -i  42     1 - cosh3(Hyh)            ,                                  (264)
                                  H2                                                                  (265)
                                                                                                      (266)
                      Sh  =   -i  42     cosh3(Hyh) - i sinh3(Hyh)                    ,
                                  H2

                      Sd  =   42      sinh3(Hyh) - sinh3(Hyf )                 .
                              H2

The sum of these actions of course recovers the standard result for dS saddle
points, cf. Eq. (111),

                  Stotal  =   Sa  + Sh   + Sd    =  42        -i - sinh3(Hyf )           .            (267)
                                                    H2

But the holographic contour suggests a new interpretation based on the actions
along the different segments.

    First consider the action along the first segment. It diverges in the large yh
limit, but since the geometry along this part of the contour is EAdS, this is in fact
expected. In AdS/CFT one adds counter terms to cancel the volume divergence.
These counter terms are constructed from geometrical quantities involving solely
the boundary metric. In 4 dimensions, these are given by [155, 166]

Sct(yh) = i                    2H     +   1   R(3)    =    i  42      sinh3 (H yh )      +   3  sinh(H yh )
                  d3y -h                 2H                   H2                             2

                                                                                                      (268)

These cancel the volume divergence and keep the action finite in the yh  
                                                                                             42
limit.   In fact, if we define the regulated action via IAredgS(bh)                          H2  ,  then  the

result along the a contour can be rewritten as

                          Sa = -iIAredgS + Sct(yh) + O(e-Hyh ) .                                      (269)

Next note that the total weighting is given precisely by the regulated EAdS
weighting

                                      Im(Stotal) = -IAredgS .                                         (270)

                                                 106
Thus one can say that the requirement to reach the classical part d of the
contour regulates the divergence automatically, as the horizontal connecting
part precisely implements the counter terms, up to terms that vanish in the
large volume limit,

                     iIm(Sh) = -Sct(yh) + O(e-Hyh ) .                                  (271)

In the end, one can write the total action as

            Stotal = -iIAredgS (bh) + iSct(yf ) + O(e-Hyf ) ,                          (272)

where  the  counter  terms  are  now  evaluated  at  the  final  point       f  =      + iyf .
                                                                                   2H
As seen from the final dS part of the contour, the counter terms in fact provide

the phase of the wave function, which is responsible for the classical evolution.

By contrast, the weighting, which remains constant as yf evolves to ever later

times, is determined by the EAdS part of the contour alone.

This rewriting of the action now suggests a new definition of the no-boundary

wave function. The idea is to use the EAdS part of the contour to relate the

wave function to the partition function of a dual quantum field theory. (It is

not a conformal field theory as the boundary resides at a finite value). From

the Euclidean version of AdS/CFT one expects that in the supergravity limit

                     e-IAredgS (bh,h) = ZQF T (bh, h) ,                                (273)

where the correspondence can be extended to include matter fields, here indi-
cated in the form of a scalar field with boundary value h. (The precise definition
of the dual quantum field theory depends on the matter content of the gravita-
tional theory, see [162] for an example.) Putting (272) and (273) together, we
arrive at the proposal for a holographic no-boundary wave function [157],

            (b, bh, , h, )       =         1              e  i  Sct (b,)  .            (274)

                                      ZQF T (bh, h, )

It is implicitly understood that the final EAdS scale factor bh and the final
dS scale factor b are related via the asymptotic equations of motion, at the
saddle point. When a scalar field is added, the contour is slightly shifted to
smaller Euclidean times, in analogy with the examples described in section 3.2.
However, the general analysis proceeds in complete analogy with that of pure
dS [157], and thus we will not spell it out here.

    The definition (274) is semi-classical in nature, as it builds on the supergrav-
ity limit of the gravitational side of the theory, and moreover implicitly assumes
the validity of the saddle point equations of motion. Related to this is the fact
that the definition naturally includes a cut-off labelled  above. Consider for
instance linearised perturbations around the cosmological backgrounds, as de-
scribed in section 4.1. There we saw that these only behave classically when
they have been stretched to super-Hubble scales, the requirement on the wave
number is roughly l  Hb. This suggests that there is a length scale   1/(Hb)

                                      107
below which we simply do not treat the spacetime as classical. Put differ-
ently, the spacetime is coarse-grained on those scales. When the universe is still
small, the coarse-graining is significant. As it grows,  shrinks and more and
more modes have become classical. In the infinite b limit we obtain the most
fine-grained description. In the dual QFT,  becomes a high energy cut-off,
specifying the energy scale above which modes are to be integrated out. In this
way, the cosmological evolution becomes related to (inverse) renormalisation
group flow of the QFT, realising an idea suggested in [167, 168].

    The main advantage of the holographic definition is that it provides a direct
implementation of the no-boundary proposal in string theory. It relies on the
expectation that the no-boundary condition is "universal", applying generally in
gravitational theories, and being implied by dual quantum field theories. Several
nice properties emerge, in particular that the counter terms need not be put in
by hand, but rather arise from the requirement for classicality. Also, as we have
just described, cosmological evolution and renormalisation group flow become
linked.

    Many open questions remain, which offer multiple avenues for further anal-
ysis. A general question is whether the proposal is not only conceptually at-
tractive, but whether the dual quantum field theory leads to new observational
predictions for early universe cosmology. Another general question is whether
signature reversal of metrics is admissible in quantum gravity. We will discuss
this issue in a little more detail in section 5.4. Somewhat related to this is the
question of how to include generic matter fields. For vector fields, for example,
it seems that the sources on the QFT side must be complex [169, 160]. Is this
consistent from the QFT point of view? Also, the EAdS part of the gravita-
tional theory has the inverse potential to the potential in the dS part. Thus,
when the AdS potential contains additional fields with positive, stable poten-
tials, these turn into unstable directions in the cosmological part. Even if such
unstable modes are set to be zero at background level, do their fluctuations and
couplings to other fields cause instabilities [160]? Another question concerns the
fact that the EAdS and dS parts of the contour are separated (in the example
above, these were the a and d segments, respectively). Is this separation guar-
anteed, and unique? Should the wave function not depend solely on measurable
quantities, and thus not depend on the (fiducial) EAdS part of the contour?
This concern would be eliminated if one could show how to uniquely determine
the EAdS part (bh, h) from the arguments (b, ), in general. And how does
this proposal work for non-inflationary potentials, for example for ekpyrotic ones
for which, as we saw in section 3.4, no-boundary solutions also exist, yet are
markedly different? Opportunities for further research abound.

5.3. A Filter on the Landscape

    String theory predicts the existence of additional spatial dimensions. In or-
der to be compatible with observations, these extra dimensions should either
be sufficiently small in volume [170], or be highly curved [171, 172], so that
gravity appears 4-dimensional at observationally accessible scales. The volume

                                                  108
and shape of the additional dimensions determine the features of the observ-
able universe, in particular the nature of fundamental forces and their coupling
constants. Since coupling constants have not been measured to vary over the
currently probed history of the universe [173], a further requirement is that the
additional spatial dimensions must be stable and essentially non-evolving over
the last 13.8 billion years. This leads to immediate questions of cosmological
relevance: what determines the size and shape of extra dimensions? How are
compactified spacetimes created in the first place? Can the compactification
change over time?

    Added to these questions is the obvious question of whether suitable com-
pactifications, giving rise both to realistic particle physics and cosmological evo-
lution, exist. This turns out to be a far harder question than initially thought.
Even though myriads of solutions of string theory were conjectured [174], it
turned out that constructing concrete examples is severely hampered by gen-
eral quantum gravitational consistency conditions, known as swampland con-
straints [175]. In particular, it is thought to be impossible to find de Sitter
solutions in perturbative string theory [132]. A more realistic goal is to search
for inflationary potentials, but even those are hard to find [133, 176] (and like-
wise, ekpyrotic potentials may be just as difficult to construct [142]). The most
promising examples to date require a careful balancing of perturbative and non-
perturbative effects [141], with many approximations that remain debated (for
recent criticism, see e.g. [177]).

    Still, it seems plausible that non-perturbative string theory contains solu-
tions that undergo accelerated expansion (in fact, it is necessary if string theory
is to be compatible with the current era of dark energy domination that we find
ourselves in). We will proceed on the assumption that this is the case. Then, in
these solutions, the shape and volume of the extra dimensions will be described
by many so-called moduli fields, which can be thought of as the parameters of
the solutions. These must be stabilised, which can be achieved for example with
the inclusion of non-trivial flux fields in the internal dimensions [178, 179].

    If we then ask which compactifications are preferred, we are really asking
which values of the moduli fields are preferred. In turn, this corresponds to
searching for a probability distribution over the ingredients of the compacti-
fications, i.e. over fluxes, branes, orientifolds etc. In this section, we would
like to analyse whether the no-boundary wave function could provide precisely
such a probability distribution. In other words, we are asking whether the no-
boundary wave function can act as a vacuum selection principle, determining
which kinds of universes are likely to be created from nothing, and which are
unlikely [45, 180]. In addition, we must keep in mind the possibility of tran-
sitions within an existing universe, to another vacuum/compactification, e.g.
via nucleation of membranes [181]. This certainly seems possible, but is always
suppressed since it is a non-perturbative process. We will restrict our attention
here purely to the creation phase of space, time and matter.

    In fact, since not much detailed knowledge exists about the landscape of
realistic string theory solutions, all we can do is study a toy model [182]. Still,
this serves to illustrate how a probability distribution over compactifications

                                                  109
might ultimately arise.

                                                               0.010
                                                               0.008
                                                               0.006
                                                               0.004
                                                               0.002


                                                                            3.0 3.5 4.0 4.5 5.0 5.5 6.0

Figure 43: The potential (278) for ~ = 1 and n4 = 13. Left panel: Two-field potential, with
V = 0 indicated in blue for reference. Right panel: A slice of the potential at  = 6. One can

see that there is the possibility for  to be stabilised at min  2.8. Figures reproduced from
[182].

    We will use a toy model that is defined in 8 dimensions, and includes a non-
perturbative R4 correction term [183, 184]. This term leads to an inflationary
potential, very much in analogy to the Starobinsky model in 4 dimensions [185].
Moreover, the model includes 4-form flux. Both features are known to arise in
11-dimensional supergravity [186, 145]. The action is given by

                S   =  1          d8x        -g^        R^  +  R^4      -   2  1     e2F(24)     ,  (275)
                       2                                                       � 4!

where e is a coupling constant. We then perform two steps: the first is to

redefine the metric via a conformal transformation in order to go to Einstein
                                                               2                        6           1 + 4R^3.
frame.  Specifically,  we   define           g^�            e     42    g�  with     e  7     =                The

second is to dimensionally reduce on a 4-sphere, with 4-form flux wrapping

the sphere, in order to land in 4 spacetime dimensions,

              ds28  =  e-   2       ds42  +  e    1       d24  ,        F(4) = 2n4vol(S4) .         (276)
                               3                     3

The resulting theory in 4 dimensions contains gravity with 2 scalars and a
potential,

        S  =  164           dt      -3  aa 2      +     a3     2 +  2          + 3N a - N a3V (, )
                3                       N               2N

             +      3  a2a  -     a3                  ,                                             (277)
V (, ) = ~             N                                                                            (278)
                                             surf ace
                                    6N

                                  6       4  e- 2                                          
                                  7       3            3
                    1 - e-                                  +  n24e-2 3        -     6e- 3    .

where ~ is a constant. The surface term on the final boundary is removed by
the inclusion of a GHY boundary term. On the initial boundary, we do not add

                                                        110
a surface term, as discussed several times in this review. However, it vanishes
in any case when the saddle point geometry is compact, a(t = 0) = 0. In the
above, it is important that the flux on the 4-sphere is quantised [187], and thus
n4 is proportional to an integer,

                n4  =   2e   2       z  =                                3        z  ,      z  Z.                              (279)
                            vol(S4)                                     8e

The shape of the potential is shown in Fig. 43 for an interesting example of
parameter values. One can see that it contains a valley at   2.8, where  and
thus the size of the 4-sphere can be stabilised. In the orthogonal  direction,
inflation can occur. The model is not fully realistic, as the inflationary phase
eventually ends when the potential drops to negative values. However it is
realistic enough to address the nucleation of universes.

100                                                                     100

          Im(a)                                                                     Im()

 80                                                                      80

60                                                                      60                                 Lorentzian

40                                                                      40

20                                                                      20

 0                                                                          South           Euclidean
     0                                                                      Pole
                                                                        0

            10  20  30  40  50  60      70                                  0      10   20  30         40  50          60  70

Figure 44: An example of a no-boundary instanton in the potential (278), with  stabilised
on the valley floor at   2.8. The dark lines show the locus of real a and  values, and the
red dot indicates the final time  = 53.185 + 83.538i, at which the fields reach the designated
real values a1 = 200, 1 = 6. For this, the scalar field value has been tuned at the South Pole
to the value SP = 6.1104 - 0.09991i. Figures reproduced from [182].

Re[a] , 1000*Im[a]                                                      Re[] , 10*Im[]
      200                                                                       6

    150                                                                        5

                                                                               4

    100                                                                        3

        50                                                                     2

                                                                               1

                                                                                     20 40 60 80 100 120                   
                20 40 60 80 100 120
                                                                            -1

Figure 45: Field evolutions along the dashed line path indicated in Fig. 44. The real parts
are shown in blue, and the imaginary parts (magnified for better visibility) in orange. Figures
reproduced from [182].

    As we saw in section 3.2, it is imperative that a dynamical attractor exists
in order for no-boundary solutions to exist. Here the inflationary valley can
play precisely this role. Thus no-boundary solutions are expected to exist, with
 stabilised and  slowly rolling down the valley floor. Using the numerical

                                        111
techniques described in section 3.3, this expectation is borne out � an example
is shown in Fig. 44, with the field values in Fig. 45. It has all the usual no-
boundary characteristics, with the fields reaching a quasi-Lorentzian evolution
at late times. Closely related solutions, with inflation lasting more or less long,
can then be constructed with the same techniques [182]. In this potential, there
also exist no-boundary solutions at large , cf. the inflationary slope shown in
the right panel of Fig. 43. However, for these solutions the sphere size modulus
 rolls to large values, and consequently the solutions decompactify and are not
of phenomenological relevance.

    What is interesting about this model is not just that inflationary no-boundary
instantons, with stable internal dimensions, exist at all. The point is that they
only exist for a range of values of the flux parameter n4. When n4 is larger, the
inflationary valley floor rises until the valley actually disappears, and only de-
compactifying solutions are left. And when n4 is too small, the valley floor sinks
to negative values of the potential, eliminating the possibility of an inflationary
solution. In the present example, the viable range is found to be [182]

             11.7  n4  15.1 (~ = 1) .                            (280)

Note that the no-boundary solutions that exist in this range have the property
that the 4-sphere is present from the outset, i.e. the universe nucleates as a
product of a fixed 4-sphere with a geometry that starts at zero size and then
grows into a Lorentzian quasi-dS spacetime. (This is a higher-dimensional ana-
logue of the Nariai instanton described in section 3.7.) As usual, no-boundary
solutions that exist for lower potential values come out as preferred. This means
that in the present toy model, the no-boundary wave function implies a proba-
bility distribution of initial conditions, where the initial conditions include the
parameters of the 8-dimensional compactification [182]. This translates into a
probability distribution over the fluxes, as sketched in Fig. 46.

Probability

Negative potential  No-boundary solution  No-boundary solution,
    No solution                  &        but decompactifying

                        stable internal      extra dimensions
                          dimensions

                                                                                                               Flux (quantised)

Figure 46: The no-boundary wave function implies a probability distribution over compact-
ifications, linked here to a probability distribution over fluxes. In this example [182], no-
boundary instantons with stable internal dimensions are only possible for a narrow range of
fluxes. Figure reproduced from [182].

                    112
    In more realistic compactifications, we expect many more parameters to be
present. Once a better understanding of realistic compactifications becomes
available, including both particle physics and cosmological aspects, it will be in-
teresting to see how these different facets of the solutions influence each other.
A crucial question will be whether universes like ours come out as being rather
likely or unlikely. In particular, one will be able to investigate which kinds of
effective lower-dimensional laws of physics are likely, and which not. Only those
tied to a universe that can actually come into existence by virtue of its cosmo-
logical dynamics stand a chance of being assigned a high probability. In this
way, as one can already see in embryonic form in the example described above,
the micro and macro properties of the universe become intimately linked, and
the no-boundary proposal can act as a filter on the possible higher-dimensional
worlds.

5.4. Allowable Metrics

    Throughout this review, we have seen that the no-boundary proposal is
intimately connected with complex metrics. The usefulness of complex metrics
became appreciated through the study of complex black hole metrics, which
provide the quickest way of deriving (and to some extent, understanding) the
thermodynamic properties of black holes [9]. However, not all complexified
metrics make sense. Witten gives the example of zero-action wormholes, which
would render tunnelling via wormholes just as likely as classical evolution, if they
were permitted [94]12. Hence, there must be some kind of criterion that tells us
which complex metrics should be included, and which not. This is important,
as in our examples in sections 3.2, 3.4 and 3.6 in particular, we saw that it is
not only the saddle points that are complex, but the integration contours are
typically also over complex metrics. Thus the definition of gravitational path
integrals is potentially sensitive to any such allowability criterion.

    Louko and Sorkin analysed this question in a simplified two-dimensional
context in [188], allowing complex metrics only when they admit a well-defined
(that is to say, convergent) scalar field theory on them. In a similar vein,
though independently, Kontsevich and Segal proposed to define quantum field
theories on fixed complex backgrounds under the condition that the complex
backgrounds allow for well-defined theories of arbitrary p-form matter fields
[189]. The reason for highlighting p-forms of arbitrary rank is that these lead
to local covariant stress-energy tensors [190], and as such provide a rather gen-
eral description of matter suitable for local quantum field theories. Let us briefly
review the criterion here: the idea is to require a path integral over real val-
ued p-form matter fields, with field strengths Fj1j2���jp+1 , to converge. It is

  12These are easy to construct. Take flat space in polar coordinates ds2 = dR2 + R2d32
and promote R  R(u) for a real parameter u. Now if R(u) interpolates between asymptotic
regions R  � while avoiding R = 0 by passing around the origin in the complexified R
plane, then this solution interpolates between two asymptotically flat regions of spacetime
and describes a complex wormhole in between. But since the metric is simply obtained by a
coordinate change from flat space, the Ricci curvature remains zero and so does the action.

                                                  113
enough to focus on the kinetic terms, which already provide all of the necessary
conditions. Thus, we require

|e  i  S|  <  1  or  |e-    1  IE  |  <  1  implying           (281)
                                                               (282)

Re ggj1k1 � � � g F jp+1kp+1 j1���jp+1 Fk1���kp+1 > 0 .

Pointwise, one can always write the metric in diagonal form

                               gjk = jkj                       (283)

where the j are now complex numbers. As an example, for p = 0 and in 4
dimensions, the condition (282) becomes

- < Arg(1) + Arg(2) + Arg(3) + Arg(4) <  .                     (284)

For higher p, some of the signs are flipped. Writing these conditions out for all
p, i.e. for all possible sign combinations, leads to the concise condition [189]

                      |Arg(j)| <  ,                            (285)

                               j

which must hold everywhere in spacetime.
    When dynamical gravity is included, it is not clear that this is the correct

condition. However, Witten observed that it indeed eliminates known patho-
logical metrics, while allowing many useful ones [94]. Thus, it makes sense to
investigate the consequences that this criterion would have on no-boundary path
integrals. This question was studied in some detail in [94, 191, 192, 95] and we
will review the main results below.

    First note that standard Lorentzian metrics saturate the bound (285) (they
have  = ), and thus reside right on the edge of the allowed domain of metrics.
This is reasonable, as Lorentzian path integrals are only conditionally conver-
gent, and the bound expresses the condition for absolute convergence. Any
Lorentzian metric can be easily regulated to satisfy the bound, e.g. for RW
metrics we may write

              ds2 = -(1  i)dt2 + a(t)2d2 ,                     (286)

for a small real number . One can then imagine taking the limit   0 at the
end of calculations. However, it is crucial that  must not change sign. Thus,
in a sense, the bound (285) already divides the space of metrics into two.

    What can we say about no-boundary geometries? The saddle points in
section 3.6 were obtained in a gauge where the lapse is constant, cf. Eq. (172).
These may be transformed to physical time by defining Nq dt  dT, which leads
to

                 T  (t)  =  2i  arsinh      N t       -     .  (287)
              3                              6i          2

                                      114
                          H1                            5
                          1.5

                          1.0  Lorentzian time          4                        |Arg i |


                                                        3

                          0.5                           2

                                                        1

H0     Euclidean time                                                                           t
 -1.5
       -1.0  -0.5                                                  0.2     0.4  0.6        0.8  1.0

Figure 47: Left Panel: A no-boundary saddle point solution, interpolating between an initial
hypersurface H0 (South Pole) and a final one H1, via two different paths in the complex time
plane. The paths are described in the main text. Right panel: the sum of arguments , as
defined in (285), along the two time contours. Figures reproduced from [191].

In Fig. 47 the resulting path in the complex T plane is plotted in blue in the
left panel. In the right panel, we plot the sum  of absolute values of arguments
of the metric components, as defined in (285). What may come as a surprise
is that the bound is seen to be violated. Thus, in the constant lapse gauge,
the saddle points appear to violate the allowability bound (285). However, as
we discussed previously, the action, and thus also the physical consequences,
are unchanged when the path is deformed. In fact, the original Euclidean-
plus-Lorentzian contour gives  = 0 along the Euclidean segment, and  = 
along the Lorentzian one, and thus implies that no-boundary saddle points
actually saturate the allowability bound. But one may worry that this contour
is non-smooth. Let us therefore consider a smooth family of paths, obtained by
specifying T = (t) with

             (t)       =  -     (1              -  t)n  +  T  (1)  tn   ,  0  t  1.                  (288)
                             2

In Fig. 47 an example with n = 3 is plotted in orange. There we can see that
now the bound is indeed satisfied, and saturated only at the end point.

    The previous example should make it clear that it is in general difficult to
assess whether a metric is allowable or not, if we permit such changes of time
path. Techniques were developed in [192] to deal with this situation, and we
refer to this paper for details. The results for no-boundary integrals, both with
a Neumann initial condition and for a Dirichlet initial condition, are shown in
Fig. 48. Both cases share the characteristic that the real lapse line constitutes
a boundary that cannot be traversed. And in both cases, the steepest descent
contours run into regions that are not allowed. This means that, if this allowa-
bility criterion is strictly enforced, then we can no longer define the sums over
metrics along thimbles. It is unclear at present what this implies.

    One interesting feature in the Neumann case is that, as seen in the plane
of the lapse function, the saddle points reside right at the edge of the allow-
able domain. This can be understood analytically: for the path integral with

                                                        115
      6                                                  6
      4                                                  4
      2                                                  2
      0                                                  0
    -2                                                 -2
    -4                                                 -4
    -6                                                 -6
       -6 -4 -2 0 2 4 6                                   -6 -4 -2 0 2 4 6

Figure 48: Allowable metrics (in light blue) in the plane of the complex lapse function;
disallowed metrics are shown in red. Left panel: with an initial Neumann condition. Right
panel: with an initial Dirichlet condition. The saddle points and steepest descent contours
are also shown. Here  = 3, q1 = 10. Figures reproduced from [192].

Neumann initial conditions, the initial size of the geometries is not fixed. In
fact, this initial size can become complex off-shell, and by itself it can cause the
allowability bound to be violated. Indeed, near the saddle point let us write
N = N� + , and work to linear order in . Then from (170) we obtain

                              q(0)        �2(      q1  -  1)1/2  ,                         (289)
                                                3

where  we  assume   that  q1     >  3  .  This  implies   that      for  N-  we  get  the  condi-

tion 3|Arg()| < . Consequently, starting from the saddle point, the allowed

directions are  limited to -        <     Arg()    <      . For   N+ one analogously       finds
                                 3                     3  even   though they are fully     com-
2   <  Arg()    <  4   .  Hence  the saddle points,
 3                  3
plex, are at the edge of the allowed domain, and thus the steepest descent

contours are cut in "half" by the allowability criterion, with only the lower

portion remaining.

    For the case with Dirichlet initial conditions, the fact that the upper half

plane gets separated from the lower half plane of the lapse function may be

interesting. As we saw in section 4.1, the unstable saddle points are in the

upper half plane, while the stable ones are in the lower half plane. Therefore, if

one is not allowed to cross the real lapse line, then a definition of the integral in

terms of exclusively stable metrics becomes a possibility. This is an idea worth

pursuing.

    The bound (285) was derived with the assumption that the matter fields take

real values. However, we saw in sections 3.2 and 3.4 that when a scalar field is

added, it is typically required to take complex values at the South Pole. Might

this lead to a conflict? It has been observed in [95] that there are situations in

which it may be natural to allow for complex scalars. In particular, when there

are additional dimensions that are compactified, then the lower-dimensional

                                          116
theory contains scalar fields (moduli) that arise from the higher-dimensional
metric. We saw an example in section 5.3. In this case, if the bound (285)
is imposed in the higher-dimensional parent theory, then it is clear that it will
allow for the lower-dimensional scalars to be complex, to a certain extent. What
one finds is that the imaginary part of the scalar is bounded. The precise
bound depends on the situation; we will just give one example, focusing on
the scalar field  that determines the volume of the internal manifold. The
compactification ansatz reads [193]

                gMN dxM dxN = e2ag� dx�dx + e2bgij dxidxj ,                                      (290)

with Latin indices running over the (D - d)-dimensional internal manifold, and
Greek indices over the d-dimensional external manifold. To obtain a canonically
normalised scalar, we must choose

                      a  =  -    D  -  d   b  ,     b=     (D    d-2    -  2)  .                 (291)
                                 d  -  2                       - d)(D

We can immediately see from (290) that it will be the imaginary part of ,
rather than its argument, that will contribute to .

    Now, as an example, if we look near the South Pole of putative no-boundary
solutions, and assume that g�, gij are Euclidean there, then we get

             = d         (D   D-d             2)    +    (D - d)(d - 2)       2|Im ()| .         (292)
                             - 2)(d -                         D-2

For instance, if we compactify from D down to 4 dimensions, we get the bound

             D  -  4  |Im  ()|   <      ,     or    |Im ()| <        D  -  2               .     (293)
62           D  -  2                                                 D  -  4           10
                                                                              62

Meanwhile, no-boundary solutions require (see section 3.2 and [60])

                                    Im(SP           )    - V,     .                              (294)
                                                            V  2

which  then  translates    into  |V, |        1  .  Hence  only  sufficiently  flat  potentials  would
                                   V          5
allow for no-boundary solutions in this example [95].

Note that we have only analysed what happens near the South Pole in this

example, the full no-boundary geometry might very well lead to a stronger con-

dition on the potential. This has started being explored very recently and leads

to promising results concerning observational predictions, in particular regard-

ing the tensor-to-scalar ratio [194] and the overall size of the universe [195].

This direction of research appears highly promising at present.

                                                    117
6. Discussion and Open Questions

    According to our current understanding, the fundamental principles for phys-
ical laws are the principles of quantum theory. When they are applied to the
universe as a whole, it follows that the universe must admit a quantum state.
If we knew this state, we could infer probabilities for different initial condi-
tions and for subsequent evolutions of the universe. The no-boundary proposal
provides a prescription for calculating this quantum state.

    The prescription combines quantum theory, gravity, and what one may term
a containment principle, namely the idea that the universe is entirely self-
contained in space and time. When formulated in terms of gravitational path
integrals, the idea is that the dominant geometries, i.e. the saddle points of
the path integral, consist of closed and regular spacetimes, with regular mat-
ter configurations on them, admitting as their only boundary the present-day
configuration of the universe. In other words, there is no boundary to the past
at which "outside" conditions might come into relevance. This may be inter-
preted as describing the emergence of the universe out of nothing � or, perhaps,
one should rather say that it describes the existence of the universe in a self-
consistent manner.

    The no-boundary condition appears as a very natural, almost inevitable,
condition to put on path integrals. This is also confirmed by studies of anal-
ogous integrals in a non-cosmological, asymptotically AdS, setting. That said,
the precise mathematical implementation of the no-boundary condition can be
tricky and has so far been studied only on a case by case basis, and only in simple
minisuperspace models. These studies have suggested that instead of summing
over closed metrics, as initially advocated by Hartle and Hawking, it might be
more appropriate to impose a regularity condition on the geometries that are
summed over. However, a general prescription is still lacking, and this is one of
the outstanding open questions related to the no-boundary wave function.

    But before discussing open issues, let us briefly recap what the no-boundary
wave function already manages to explain (a fuller discussion was already pre-
sented in section 4.3). The most important feature of the no-boundary wave
function is that it can explain the emergence of space and time, and how space-
time becomes classical. In doing so, the big bang singularity is automatically
avoided, as only initially regular geometries enter the path integral. A further
consequence is that matter fields are predicted to have been in their ground
states at the nucleation of the universe. All these features explain aspects of
our universe that, without clear justification, were simply assumed to hold. But
according to the no-boundary wave function, not every type of universe can
emerge from nothing. In fact, a dynamical attractor is required in order for
no-boundary solutions to exist. Two such attractors are currently known, infla-
tion and ekpyrosis, and we discussed the corresponding no-boundary solutions
in sections 3.2 and 3.4. The requirement of an attractor shows that the no-
boundary proposal also leads to vacuum selection, by strongly restricting the
possible early universe dynamics.

    What is currently less well understood are the precise predictions for cosmo-

                                                  118
logical observables. Naively, the no-boundary measure favors short inflationary
phases at low values of the potential, and long ekpyrotic phases. However, as
discussed in section 4.2, these probabilities have so far only been inferred from
highly simplified models, and may still be subject to revision. Also, in the ekpy-
rotic case, the transition from contraction to expansion remains ill understood
at the quantum gravitational level. These are certainly important topics for
future work.

    The remarks above lead us to the many opportunities for further research
that the no-boundary framework brings into the open. Let us begin with more
mathematical questions. A basic one is whether a general prescription may be
found that would determine the integration contours over fields, in particular
the integration over the lapse function. As we saw in section 5.4, if there exist
physical restrictions on the complex metrics that are summed over, then this
will have important consequences for the possible contours of integration. Let us
highlight here that it appears so far that neither of the two "obvious" physical
choices, that is to say neither Euclidean nor Lorentzian contours of integration,
have been found to work in general. This fact encourages us to study complex
metrics much more seriously in the future. A related open question is which
kinds of singularities ought to be allowed in the off-shell geometries, and whether
or not such singularities play a role. An evident long-term goal is to extend
the treatment of path integrals beyond minisuperspace. This is a topic that
unfortunately has not seen much progress over several decades.

    And then there is a host of questions that are more conceptual in nature. For
example, what is the meaning of the fact that the no-boundary wave function
does not vanish at zero size? The simplest non-trivial topologies do not seem
to contribute to the wave function (see section 5.2), thus reinforcing the puzzle.
Also, saddle points typically come in pairs, which may be thought of as time re-
verses of each other. Can there be interesting interference effects between these
saddles when the universe is still very small? And can the definition of proba-
bilities be refined? So far, it is based on mathematical/WKB properties of the
wave function. But can it be made more physical, highlighting the importance
of interactions between sub-systems in the universe? Very generally, what is the
meaning of probability when we only get to observe a single universe? Another
very general question is whether there can be any other dynamical attractors,
besides inflation and ekpyrosis, that allow for no-boundary solutions. If so, then
this might yet again significantly affect our thinking about the early universe.

    A final set of questions concerns the interplay of the no-boundary proposal
and string theory. For instance, can the effects of winding modes be included?
How does one describe no-boundary solutions containing branes and orien-
tifolds? Can one construct models with at least semi-realistic particle physics
and cosmological dynamics, to see how these features affect each other � in par-
ticular, it would be interesting to see which vacua receive high probability and
which are excluded. Can a bounce be included in a consistent manner? And
two very general questions to end: first, is the holographic definition, described
in section 5.2, correct? And second, if the cobordism conjecture (which states
that all possible asymptotic field configurations can be related by interpolating

                                                  119
spacetimes [196]) is correct, then how does it affect the no-boundary frame-
work? At least naively, it would seem to imply the existence of no-boundary
saddles with arbitrarily large numbers of transitions between various cosmologi-
cal epochs. Will the simple examples that have been studied so far end up being
good approximations to the preferred route to our present day conditions?

    One can look forward to the insights that will be gained from pursuing these
questions.

Acknowledgments

    I have learned a great many things (and not just about quantum cosmology)
from discussions with Andr�es Anabalo�n, Lorenzo Battarra, Sebastian Bram-
berger, Alice Di Tucci, Job Feldbrugge, Shane Farnsworth, Jonathan Halliwell,
Jim Hartle, Arthur Hebecker, Michal Heller, Thomas Hertog, Oliver Janssen,
Caroline Jonas, Claus Kiefer, Axel Kleinschmidt, Michael Ko�hn, George Lavre-
lashvili, Rahim Leung, Vincent Meyer, Hermann Nicolai, Burt Ovrut, J�er^ome
Quintin, Laura Sberna, Paul Steinhardt, Kelly Stelle, Stefan Theisen, Neil
Turok, and Alex Vilenkin. Thank you!

    I gratefully acknowledge the support of the European Research Council via
the ERC Consolidator Grant CoG 772295 "Qosmology".

Appendix A. Canonical Quantisation

    In the main text, we concentrated on minisuperspace models where spatial
isotropy and homogeneity is assumed from the outset. This was the most rel-
evant example, but some readers may be interested in seeing the more general
framework, where such a symmetry reduction is not made. We will focus on
the gravitational part of the action, with the matter content being left implicit.
Thus the action is taken to be (setting 8G = 1)

                S  =  1     d4          -  2)  +  Sboundary     + Smatter  (A.1)
                      2         x -g(R

                         M

The choice of boundary term determines which boundary conditions can be con-

sistently imposed. It is then useful to write the metric in (1 + 3) decomposition

[40],

                   ds2 = -N 2dt2 + hij dxi + N idt dxj + N jdt ,           (A.2)

where N is the lapse and Ni the shift. A useful quantity is the extrinsic curvature

                         Kij    =   1  - hij   + 2D(iNj)     ,             (A.3)
                                   2N      t

where Di is the covariant derivative on the three-surface. The aim is to rewrite
the action in terms of N, N i, hij and Kij. This can be done using the Gauss-

Codazzi relation between 4-curvature and 3-curvature, yielding

       S  =  1                                                             (A.4)
             2     d3x dt N h Kij Kij - K2 + 3R - 2 + Smatter .

                                        120
The Hamiltonian form of the action is given by [40]

                   S = d3x dt h ij ij - N H - N iHi                               (A.5)


              L            h
where ij  =  h ij  =  -   2   Kij - hij K       are the momenta conjugate to hij.

The Hamiltonian is a sum of constraints, with the lapse N and shift N i being

Lagrange multipliers. There is the momentum constraint,

                      Hi = -2Dj ij + Hmi atter = 0 ,                              (A.6)

and the Hamiltonian constraint

             H  =  2Gijklij kl    -    1          -  2)  +  Hmatter      =  0  ,  (A.7)
                                       2    h(3R

where Gijkl is the DeWitt metric [197]

                   Gijkl  =    1  (hik hj l    + hilhjk  -  hij hkl)  .           (A.8)
                              2h

These constraints are essentially equivalent to the 0i and 00 components of the
classical Einstein equations. The constraints play a central role in the canonical
quantisation procedure.

    Canonical quantisation amounts to imposing the constraints as operator
equations, in the field representation with the substitution

                                  ij        -i                                    (A.9)
                                                  hij

and similarly for the matter momenta. This results in four equations: the
momentum constraint

                      Hi      =  2iDj        +  Hmi atter   =    0,               (A.10)
                                       hij

and the Wheeler-DeWitt equation [197, 198]

H(hij , matter) =         -Gijkl                            - 2) +    Hmatter      = 0.
                                  hij     hkl  - h(3R

                                                                                  (A.11)

We should point out that there is an ambiguity in factor ordering, as the precise
placement of the functional derivatives is not fixed. In explicit examples, sensible
choices can often be found, e.g. by requiring invariance under field redefinitions
[16].

    Since the constraints are so central, it is worthwhile investigating their mean-
ing. To understand the momentum constraint better [199], consider a change
of coordinates on the three-surface, xi  xi - i. Then

                [hij + D(ij)] = [hij ] +               d3x  D(i  j)               (A.12)
                                                                     hij

                                          121
Integrating by parts in the last term, and dropping the boundary term (assuming
the three-manifold is compact), one finds that the change in  is given by

 = -  d3x j Di       =  -  1   d3x iHi  (A.13)
                hij        2i

This will be zero when the momentum constraint is imposed. Hence it expresses
spatial diffeomorphism invariance.

    The Wheeler-DeWitt equation (A.11), due to its association with the lapse
function, is similarly related to time reparameterisation invariance. It combines
spacetime geometry and matter into a single quantum equation, as expected in
quantum gravity. One variable stands out: the scale factor (or size) of the uni-
verse, given by the appropriate power of det(hij): it enters with a negative sign
in the DeWitt metric, as we also saw in explicit examples, see e.g. (11). Other
metric deformations, as well as matter fields, enter with a positive sign. Note
that the Wheeler-DeWitt equation does not contain any explicit dependence
on coordinates, in particular on time. This is different from ordinary quantum
mechanics, where time plays a privileged role. It makes sense here, since we do
not measure time directly, but rather correlations between field configurations
(e.g. the arrow on the watch points towards the 12 and the sun is high in the
sky).

    The Wheeler-DeWitt equation should be solved at every point in spacetime.
For general metrics this is technically impossible. The general configuration
space consists of spatial metrics and matter configurations, up to diffeomor-
phisms (this is called superspace). One then typically restricts to homogeneous
spatial metrics, containing just a few time-dependent functions and fixed spatial
dependence. This is known as minisuperspace. One drawback is that one has
set all other metric deformations to zero, including their momenta (which is in
conflict with the uncertainty principle). However, we know that our universe is
rather homogeneous, hence one may hope to obtain a self-consistent "approxi-
mation". In practice one has to see if perturbations around the minisuperspace
geometries are suppressed, and above we found that for no-boundary saddle
points this was always the case.

Appendix B. Gravitational Path Integrals

    When gravity is included, the path integral includes a sum over geometries.
Defining this requires some care, because of diffeomorphism invariance. One has
to make sure not to overcount, as geometries might be related to each other via
changes of coordinates. Hence it is important to properly fix the gauge. The
general procedure was first worked out by Teitelboim in [200, 201], and applied
to minisuperspace models by Halliwell in [16]. Here we will outline how this is
done; additional details can be found in the original papers.

    For simplicity, we will consider a minisuperspace action with a single degree
of freedom, namely the scale factor a of the universe (and its conjugate momen-
tum p). Models with more degrees of freedom can be dealt with analogously.

                122
The action is thus given by

                                             1                                             (B.1)

                                S = dt (pa - N H)

                                           0

with  the  Hamiltonian   H   =   1  p2  +  U (a).  Classically,      the Hamiltonian       would
                                 2
vanish. The metric is of the form ds2 = -N (t)2dt2 +a(t)2d23, and overcounting

may arise due to time reparameterisation invariance. Hence we must fix a gauge.

This gauge must be chosen such that any history can be deformed into one that

satisfies the gauge condition, and the gauge must be fixed completely. An

appropriate choice is [200]

                                    N = f (a, p, N ) ,                                     (B.2)

where f is an arbitrary function of the fields, but not of their time derivatives.
Such a gauge choice can be implemented with a Lagrange multiplier (t), by
adding the following term to the action

                                             1                                             (B.3)

                             Sgf = dt N - f .

                                           0

This term fixes the gauge, but this is not enough yet. We also have to make
sure that the path integral is actually independent of the choice of gauge fixing
function f. This at first seems rather tricky to establish, but can be achieved
using the formalism developed by Batalin, Fradkin and Vilkovisky [202, 203]
(based on [204]). The idea is first to add ghost fields. More specifically, one
adds the anticommuting fields C, C� and their conjugate momenta P, P�. Then one
uses the extended action to define a new symmetry, a so-called BRS symmetry,
which will help establish invariance under changes of gauge. Some educated
guesses are required at this step, see e.g. [16]. It turns out that if the action for
the ghosts is taken to be

           Sgh =   1        P�C  +  C�P  -   P�P   +  C {f ,  H }C�  +  P   f  C�      ,   (B.4)
                                                                            N
                     dt

                  0

where  {f, H}  =  f H   -   f H     is  the  Poisson    bracket,        then  the   total  action  is
                  a p       p a
invariant under a BRS transformation with anticommuting parameter ,

               a  =  C   H   ,   p  =   -C   H     ,  N  =       P   ,      =  0,
                         p                   a

               C = 0 , P = 0 , C� = - , P� = -H ,                                          (B.5)

subject to the boundary conditions that , C and C� vanish at the end points
t = 0, 1. Now the path integral is defined by using the Liouville measure and
integrating over the total action, including the gauge fixing and ghost terms,

               =     DaDpDN         DDC      DP    DC�  DP�   e  i  (S+Sgf  +Sgh )  .      (B.6)


                                             123
The punch line now is that this path integral is indeed independent of the choice
of gauge fixing function f. This can be shown explicitly by performing a BRS
transformation with the special choice of parameter

                                       = i           1                                              (B.7)
                                             0
                                                      dt(f - f~) .

The total action is evidently invariant, since the transformations (B.5) were

chosen specifically for this to be the case for any . And when calculating the
(super-)Jacobian J of this transformation, one obtains a factor [205]

                                    i        C {f~-f ,H }C� +P         (f~-f )  C�
                                                                          N
                     J = e                , dt                                                      (B.8)

which has the effect of replacing f by f~ in the ghost action (B.4). Thus the
path integral is indeed independent of the choice of f. Note that this greatly
simplifies the analysis. Not only can one perform the path integral with N fixed
for metrics of the form (10), but also for more involved choices such as the useful
version in (13).

    For now, we may make use of this freedom and choose f = 0 to further
evaluate the integrals. With this choice, the ghost integrals factorise out, and
one can see immediately that they must yield a purely numerical factor, as they
have become independent of the other fields. The integrals over anti-commuting
variables can be evaluated straightforwardly [16], resulting in a factor of unity

DC  DP  DC�  DP�  e  i  1  dt(P�       C  +C�P  -P�  P  )  =     e[C�(1)-C�(0))(C(1)-C(0)]   =  1,  (B.9)
                        0

where one has to make use of the boundary conditions that C(0) = C(1) =
C�(0) = C�(1) = 0. Meanwhile, the integral over the lapse and its conjugate
momentum also simplifies drastically,

             DN         D  e  i           1  dtN     =        DN (N ) =                dN ,         (B.10)
                                          0

that is to say, the path integral over the lapse reduces to an ordinary integral
over N. This is a huge simplification, which is at the root of the tractability of
minisuperspace models. In the end, we are therefore left with the expression

                        =              dN    DaD     p  e  i     1  dt(pa -N  H)    .               (B.11)
                                                                 0

One can of course also switch from this phase space integral to one purely in
field space, as is used in the main text. For further details, for example on how
to extend the analysis to first loop order, see e.g. [206].

Appendix C. Picard-Lefschetz theory

    At various instances in this review, we have to evaluate an oscillating integral
(usually for the lapse), of the form

                                       I=            dx    e  i  S[x]  .                            (C.1)


                                                  C

                                                     124
We take S[x] to be a real function,  is a real parameter and C is the domain

of integration, typically the positive real line, or the full real line. Such an

integral is only conditionally convergent, as the integrand has modulus 1 ev-

erywhere, in particular there are no regions where the modulus drops off and

where convergence could be guaranteed. Still, intuitively one might guess that

the oscillations lead to cancellations, and that many integrals of this type might

in fact lead to sensible results.

The problem with such integrals is best illustrated by an example using

a discrete version of an oscillating integral, e.g. the series                         n=0  (-1)n.     The

value of such a sum depends on how we define the order of summation, e.g.

[1 + (-1)] + [1 + (-1)] + � � � = 0, or 1 + [-1 + 1] + [-1 + 1] + � � � = 1. And some

sums and integrals of this sort do not converge at all. Picard-Lefschetz theory is

a useful tool in dealing with such integrals [207]. Its main idea is to rewrite the

conditionally convergent integral as a sum of absolutely convergent integrals. It

also shows when a rewriting of this kind is possible, and when not. When it is,

this procedure defines the integral unambiguously. We will give an elementary

overview here (based on [14]), sufficient for our purposes. For a more in depth

treatment, see [208]. A few additional aspects are discussed in [14, 77].

    The first step is to let the variable x become complex, x  C, and to view
S[x] as a holomorphic function of x. We will also write x = u1 + iu2 for real

u1, u2. Then one can try to deform the integration domain C, using Cauchy's

theorem, into a complex contour such that the integral becomes manifestly con-

vergent. Ideal integration contours are steepest descent contours, along which

the modulus of the integrand falls off as fast as possible. Such contours are also

called "Lefschetz thimbles". They are associated with critical points (in fact

saddle points13) of S[x], i.e. they fall off from saddle points. (If a neighbour-

hood of a critical point is like a horse's saddle, then the thimble is made of the

legs of the rider.)

As a simple example, consider S[x] = x2, which has a critical point at x = 0.

Then Re[iS[x]] = -2u1u2. The magnitude of the integrand decreases most

rapidly along the contour u1 = u2, and this is the Lefschetz thimble. Conversely,

the modulus of the integrand increases most rapidly along u1 = -u2, and this

is the steepest ascent contour. We denote thimbles by J and steepest ascent

contours by K.

Now in more detail: decompose the exponent as I = iS/ = W + iP, where

W determines the weighting and P is the phase. Mathematically, W is also

known as the Morse function. Then downward flow is defined by

                                          dui  =  -gij     W     ,                                     (C.2)
                                          d                uj

where  is a parameter along the flow and gij is a (Riemannian) metric on the

13For a complex function f (x), critical points are necessarily saddle points: expanding near

a critical point xc  one  finds  f (x)    f (xc)  +  1  f   (xc  )[(u1)2  -  (u2)2  +  2iu1u2],  i.e.  there is
                                                     2
always at least one direction along which the function increases, and at least one along which

it decreases.

                                                  125
          K                                    eW

J


                     J

                                                                       J

       K

Figure C.49: Left panel: A sketch of the complex x plane. A saddle point  is shown, with
its steepest descent (J) and ascent K) contours. Arrows indicate the direction of descent.
Regions in which the weighting is smaller than at the saddle point are shown in green, and
regions with higher weighting in red. These regions are separated by blue lines, along which
the weighting equals that of the saddle point. Right panel: Sketch of the weighting along a
Lefschetz thimble (steepest descent contour).

complex plane. To verify that W indeed decreases along such a flow, consider

dW  =    W dui  =-      i  W    2 < 0. To proceed, it is useful to choose a
d      i ui d              ui
metric. One may choose this for convenience, in our case we will simply take

it to be the flat Cartesian metric, ds2 = |dx|2. With complex coordinates,

(u, u�) = u1 + iu2, u1 - iu2 , the metric is guu = gu�u� = 0, guu� = gu�u = 1/2.
Then W = (I + I�)/2 and the flow equations (C.2) become

                      du   =   -  I�  ,  du�   =   -  I  .             (C.3)
                      d           u�     d            u

From these a most useful property immediately follows,

          dP    =  1 d(I - I�)    =  1     I du I� du�      = 0.       (C.4)
          d        2i d              2i    u d - u� d

That is to say, the phase P is constant along a steepest descent flow. This
provides both a useful way of finding thimbles numerically (just plot the locus
of points with the same phases as those of the saddle points), and it leads to
a huge simplification of the integral, because now along a thimble it does not
oscillate anymore! Rather, it is maximally convergent, see Fig. C.49. In fact,
the integral along a thimble is convergent if

          dxeiS[x]/        |dx| eiS[x]/ =             |dx|eW (x) <  .  (C.5)

       J                J                          J

If we denote the length along the curve as l = |dx|, then we will get convergence
if W (x(l)) < - ln(l) + A, for some constant A, as l  . Thus only fairly weak
assumptions must be made to guarantee convergence.

    In an analogous manner to downwards flows, one can define upwards flows,

                           dui    =      +gij  W   ,                   (C.6)
                           d                   uj

                                      126
and along such flows the phase P is consequently also fixed. Hence we arrive

at the picture that from saddle points  emanate equal numbers of thimbles J

and steepest ascent contours K.

We should discuss a subtlety: it can happen that what departs from one

saddle point as a steepest descent contour arrives at another saddle point with

lower weighting (and thus looks like a steepest ascent contour from the point of

view of the second saddle point). Such a degeneracy can arise for example when

saddle points occur in complex conjugate pairs. To deal with such a situation

unambiguously, one can add a symmetry breaking term to S[x], multiplied by

a parameter . This will break the degeneracy, and then one can let   0 at

the end of the calculation. Note that all thimbles then run as far as they can,

meaning W  - and the integrand always falls off to zero along thimbles.

Likewise, steepest ascent contours reach W  +.

One important question remains to be addressed: it is not clear yet which

saddles, and thus which thimbles, contribute to the integral and which do not.

Do they all contribute, or only some? If possible degeneracies are resolved as

described above, then we can associate a single saddle point to every thimble,

and to every steepest ascent contour. As an equation, we can express this as an

intersection

              Int(J, K ) =  ,                   (C.7)

where we have implicitly chosen a direction for the contours. Our goal is to
write the integration contour as a sum of thimbles,

              C = nJ ,                          (C.8)


where the coefficients n take the values 0 or �1 (the sign depends on the
relative orientation of C and the thimbles). Now it is easy to determine these
coefficients, we just intersect both sides of the above equation with K , to
obtain

              n = Int(C, K) .                   (C.9)

In words, this means that a saddle point contributes if its steepest ascent con-
tour intersects the original integration contour. This makes complete sense: we
have an oscillating integral along the original contour; this will contain many
cancellations. Now we want to deform this into a non-oscillating integral. Along
the new contour, the modulus of the integrand must be smaller, because there
will be no cancellations along this new integration domain. Hence, from the
original integration contour, we must be able to flow down towards a saddle
point, if it is to be relevant. Or, equivalently, from the saddle point we must be
able to flow up to the original contour.

    Usually, an invariant definition requires that C runs between singularities,
either at finite locations or at infinity. But then it may happen that the thimbles
approach the singularities, or infinity, at different angles than C. Hence one must
make sure that in addition, the arcs either near a singularity or at infinity, linking

                                 127
C to the appropriate thimble, give zero contribution to the integral. In fact, this
is easy to verify in simple models. The reason is simply that the weighting runs
to minus infinity along the thimbles, and if these are to be relevant then they
must directly link up to C, without an intervening region of divergence. For a
more detailed treatment of this point, see [14].

    Using the rewriting of the integration domain, we can now express the orig-
inal, conditionally convergent integral as a sum over absolutely convergent in-
tegrals along thimbles,

I=     dx  e  i  S[x]  =      n       dx  e  i  S[x]  .  (C.10)


    C                            J

This is the result we wanted to arrive at. It defines the original integral in
a precise and unambiguous manner. For higher-dimensional integrals, this is
especially important, as it guarantees that one can use Fubini's theorem, which
states that the order of performing the integrals does not matter, as long as they
are all absolutely convergent. (This justifies the procedure done repeatedly in
the main text, namely to perform the integral over the scale factor first, and
then that over the lapse.)

    It can occur that when the parameters of the integral are varied, different
thimbles become relevant, i.e. the n can change. This important effect is
called a Stokes phenomenon, and it can have interesting consequences as saddle
points that are unimportant for some parameters can become dominant in other
parameter ranges. We will encounter examples of this effect in the main text.

    But there is more: the rewriting (C.10) also allows for a useful approximation
scheme, called the saddle point approximation. This is because the integral
along each thimble is strongly peaked around the saddle point x. And this the
more so, the smaller  is. Since in physical applications  is indeed very small,
this approximation is typically highly accurate. Furthermore, we can pull out
the phase from each integral along thimbles, since it is constant there. Putting
all this together, we obtain

I = dx eiS[x]/ =          n ei P (x)      eW dx          (C.11)

C                                     J

                  n eiS(x)/ [A + O()] .                  (C.12)


Here A is a factor that one can get by integrating over fluctuations around the
saddle point, i.e. by performing a Gaussian integral over the action expanded to
second order. Further sub-leading terms can be calculated perturbatively, but
in fact very often the leading, saddle point contribution is all we will require.

    Thus Picard-Lefschetz theory provides a highly useful tool for defining and
evaluating oscillating integrals.

References

   [1] S. W. Hawking, The Boundary Conditions of the Universe, Pontif. Acad.
       Sci. Scr. Varia 48 (1982) 563�574.

                         128
 [2] J. B. Hartle, S. W. Hawking, Wave Function of the Universe, Phys. Rev.
      D 28 (1983) 2960�2975. doi:10.1103/PhysRevD.28.2960.

 [3] S. W. Hawking, R. Penrose, The Singularities of gravitational collapse and
      cosmology, Proc. Roy. Soc. Lond. A 314 (1970) 529�548. doi:10.1098/
      rspa.1970.0021.

 [4] J. J. Halliwell, INTRODUCTORY LECTURES ON QUANTUM COS-
      MOLOGY, in: 7th Jerusalem Winter School for Theoretical Physics:
      Quantum Cosmology and Baby Universes, 1989. arXiv:0909.2566.

 [5] J. B. Hartle, S. W. Hawking, T. Hertog, The Classical Universes of the
      No-Boundary Quantum State, Phys. Rev. D 77 (2008) 123537. arXiv:
      0803.1663, doi:10.1103/PhysRevD.77.123537.

 [6] R. Feynman, A. Hibbs, D. Styer, Quantum Mechanics and Path Integrals,
      Dover Books on Physics, Dover Publications, 2010.
      URL https://books.google.de/books?id=JkMuDAAAQBAJ

 [7] R. P. Feynman, Feynman lectures on gravitation, 1996.

 [8] J. W. York, Jr., Role of conformal three geometry in the dynamics
      of gravitation, Phys. Rev. Lett. 28 (1972) 1082�1085. doi:10.1103/
      PhysRevLett.28.1082.

 [9] G. W. Gibbons, S. W. Hawking, Action Integrals and Partition Functions
      in Quantum Gravity, Phys. Rev. D 15 (1977) 2752�2756. doi:10.1103/
      PhysRevD.15.2752.

[10] C. Krishnan, A. Raju, A Neumann Boundary Term for Gravity, Mod.
      Phys. Lett. A 32 (14) (2017) 1750077. arXiv:1605.01603, doi:10.1142/
      S0217732317500778.

[11] D. Giulini, C. Kiefer, Wheeler-DeWitt metric and the attractivity of
      gravity, Phys. Lett. A 193 (1994) 21�24. arXiv:gr-qc/9405040, doi:
      10.1016/0375-9601(94)00651-2.

[12] J. J. Halliwell, J. Louko, Steepest Descent Contours in the Path Inte-
      gral Approach to Quantum Cosmology. 1. The De Sitter Minisuperspace
      Model, Phys. Rev. D 39 (1989) 2206. doi:10.1103/PhysRevD.39.2206.

[13] C. Grosche, F. Steiner, Handbook of Feynman Path Integrals, Vol. 145,
      Springer, 1998.

[14] J. Feldbrugge, J.-L. Lehners, N. Turok, Lorentzian Quantum Cosmology,
      Phys. Rev. D 95 (10) (2017) 103508. arXiv:1703.02076, doi:10.1103/
      PhysRevD.95.103508.

[15] C. Teitelboim, Causality Versus Gauge Invariance in Quantum Grav-
      ity and Supergravity, Phys. Rev. Lett. 50 (1983) 705. doi:10.1103/
      PhysRevLett.50.705.

                                                129
[16] J. J. Halliwell, Derivation of the Wheeler-De Witt Equation from a Path
      Integral for Minisuperspace Models, Phys. Rev. D 38 (1988) 2468. doi:
      10.1103/PhysRevD.38.2468.

[17] A. Di Tucci, M. P. Heller, J.-L. Lehners, Lessons for quantum cosmol-
      ogy from anti�de Sitter black holes, Phys. Rev. D 102 (8) (2020) 086011.
      arXiv:2007.04872, doi:10.1103/PhysRevD.102.086011.

[18] H. Leutwyler, Gravitational field: Equivalence of Feynman quantization
      and canonical quantization, Phys. Rev. 134 (1964) B1155�B1182. doi:
      10.1103/PhysRev.134.B1155.

[19] A. Vilenkin, The Interpretation of the Wave Function of the Universe,
      Phys. Rev. D 39 (1989) 1116. doi:10.1103/PhysRevD.39.1116.

[20] D. Marolf, Quantum observables and recollapsing dynamics, Class. Quant.
      Grav. 12 (1995) 1199�1220. arXiv:gr-qc/9404053, doi:10.1088/
      0264-9381/12/5/011.

[21] A. Ashtekar, J. Lewandowski, D. Marolf, J. Mourao, T. Thiemann,
      Quantization of diffeomorphism invariant theories of connections with lo-
      cal degrees of freedom, J. Math. Phys. 36 (1995) 6456�6493. arXiv:
      gr-qc/9504018, doi:10.1063/1.531252.

[22] J. B. Hartle, D. Marolf, Comparing formulations of generalized quantum
      mechanics for reparametrization - invariant systems, Phys. Rev. D 56
      (1997) 6247�6257. arXiv:gr-qc/9703021, doi:10.1103/PhysRevD.56.
      6247.

[23] F. Embacher, Hand-waving refined algebraic quantization, Hadronic J. 21
      (1998) 337�350. arXiv:gr-qc/9708016.

[24] J. J. Halliwell, Probabilities in Quantum Cosmological Models: A Deco-
      herent Histories Analysis Using a Complex Potential, Phys. Rev. D 80
      (2009) 124032. arXiv:0909.2597, doi:10.1103/PhysRevD.80.124032.

[25] E. Joos, WHY DO WE OBSERVE A CLASSICAL SPACE-TIME?, Phys.
      Lett. A 116 (1986) 6�8. doi:10.1016/0375-9601(86)90345-2.

[26] C. Kiefer, Continuous Measurement of Minisuperspace Variables by
      Higher Multipoles, Class. Quant. Grav. 4 (1987) 1369. doi:10.1088/
      0264-9381/4/5/031.

[27] J. J. Halliwell, Decoherence in Quantum Cosmology, Phys. Rev. D 39
      (1989) 2912. doi:10.1103/PhysRevD.39.2912.

[28] J. B. Hartle, Space-time quantum mechanics and the quantum mechan-
      ics of space-time, in: Les Houches Summer School on Gravitation and
      Quantizations, Session 57, 1992, pp. 0285�480. arXiv:gr-qc/9304006.

                                                130
[29] L. Chataignier, Construction of quantum Dirac observables and the emer-
      gence of WKB time, Phys. Rev. D 101 (8) (2020) 086001. arXiv:
      1910.02998, doi:10.1103/PhysRevD.101.086001.

[30] A. H. Guth, The Inflationary Universe: A Possible Solution to the Horizon
      and Flatness Problems, Phys. Rev. D 23 (1981) 347�356. doi:10.1103/
      PhysRevD.23.347.

[31] A. D. Linde, A New Inflationary Universe Scenario: A Possible Solu-
      tion of the Horizon, Flatness, Homogeneity, Isotropy and Primordial
      Monopole Problems, Phys. Lett. B 108 (1982) 389�393. doi:10.1016/
      0370-2693(82)91219-9.

[32] A. Albrecht, P. J. Steinhardt, Cosmology for Grand Unified Theories
      with Radiatively Induced Symmetry Breaking, Phys. Rev. Lett. 48 (1982)
      1220�1223. doi:10.1103/PhysRevLett.48.1220.

[33] D. Baumann, Inflation, in: Theoretical Advanced Study Institute in Ele-
      mentary Particle Physics: Physics of the Large and the Small, 2011, pp.
      523�686. arXiv:0907.5424, doi:10.1142/97898143271830010.

[34] J. Khoury, B. A. Ovrut, P. J. Steinhardt, N. Turok, The Ekpyrotic uni-
      verse: Colliding branes and the origin of the hot big bang, Phys. Rev. D
      64 (2001) 123522. arXiv:hep-th/0103239, doi:10.1103/PhysRevD.64.
      123522.

[35] J.-L. Lehners, Ekpyrotic and Cyclic Cosmology, Phys. Rept. 465 (2008)
      223�263. arXiv:0806.1245, doi:10.1016/j.physrep.2008.06.001.

[36] J.-L. Lehners, Classical Inflationary and Ekpyrotic Universes in the No-
      Boundary Wavefunction, Phys. Rev. D 91 (8) (2015) 083525. arXiv:
      1502.00629, doi:10.1103/PhysRevD.91.083525.

[37] G. Lemaitre, Republication of: The beginning of the world from the
      point of view of quantum theory, Nature 127 (1931) 706. doi:10.1007/
      s10714-011-1214-6.

[38] E. P. Tryon, Is the universe a vacuum fluctuation, Nature 246 (1973) 396.
      doi:10.1038/246396a0.

[39] R. Brout, F. Englert, E. Gunzig, The Creation of the Universe as a
      Quantum Phenomenon, Annals Phys. 115 (1978) 78. doi:10.1016/
      0003-4916(78)90176-8.

[40] R. L. Arnowitt, S. Deser, C. W. Misner, The Dynamics of general rel-
      ativity, Gen. Rel. Grav. 40 (2008) 1997�2027. arXiv:gr-qc/0405109,
      doi:10.1007/s10714-008-0661-1.

[41] A. Vilenkin, Creation of Universes from Nothing, Phys. Lett. B 117 (1982)
      25�28. doi:10.1016/0370-2693(82)90866-8.

                                                131
[42] A. Vilenkin, The Birth of Inflationary Universes, Phys. Rev. D 27 (1983)
      2848. doi:10.1103/PhysRevD.27.2848.

[43] A. Vilenkin, Quantum Creation of Universes, Phys. Rev. D 30 (1984)
      509�511. doi:10.1103/PhysRevD.30.509.

[44] P. A. M. Dirac, The Relation between Mathematics and Physics, Proc.
      Roy. Soc. (Edinburgh) 59, Part II (1939) 122�129.

[45] S. W. Hawking, T. Hertog, Populating the landscape: A Top down
      approach, Phys. Rev. D 73 (2006) 123527. arXiv:hep-th/0602091,
      doi:10.1103/PhysRevD.73.123527.

[46] J. D. Barrow, F. J. Tipler, Action principles in nature, Nature 331 (1988)
      31�34. doi:10.1038/331031a0.

[47] J. D. Barrow, Finite Action Principle Revisited, Phys. Rev. D
      101 (2) (2020) 023527. arXiv:1912.12926, doi:10.1103/PhysRevD.101.
      023527.

[48] C. Jonas, J.-L. Lehners, J. Quintin, Cosmological consequences of a
      principle of finite amplitudes, Phys. Rev. D 103 (10) (2021) 103525.
      arXiv:2102.05550, doi:10.1103/PhysRevD.103.103525.

[49] M. H. Goroff, A. Sagnotti, The Ultraviolet Behavior of Einstein Grav-
      ity, Nucl. Phys. B 266 (1986) 709�736. doi:10.1016/0550-3213(86)
      90193-8.

[50] K. S. Stelle, Renormalization of Higher Derivative Quantum Gravity,
      Phys. Rev. D 16 (1977) 953�969. doi:10.1103/PhysRevD.16.953.

[51] J.-L. Lehners, K. S. Stelle, A Safe Beginning for the Universe?, Phys. Rev.
      D 100 (8) (2019) 083540. arXiv:1909.01169, doi:10.1103/PhysRevD.
      100.083540.

[52] K. S. Stelle, Classical Gravity with Higher Derivatives, Gen. Rel. Grav. 9
      (1978) 353�371. doi:10.1007/BF00760427.

[53] R. H. Brandenberger, C. Vafa, Superstrings in the Early Universe, Nucl.
      Phys. B 316 (1989) 391�410. doi:10.1016/0550-3213(89)90037-0.

[54] P. Creminelli, A. Nicolis, E. Trincherini, Galilean Genesis: An Alterna-
      tive to inflation, JCAP 11 (2010) 021. arXiv:1007.0027, doi:10.1088/
      1475-7516/2010/11/021.

[55] J. J. Halliwell, J. B. Hartle, T. Hertog, What is the No-Boundary Wave
      Function of the Universe?, Phys. Rev. D 99 (4) (2019) 043526. arXiv:
      1812.01760, doi:10.1103/PhysRevD.99.043526.

[56] S. W. Hawking, The Quantum State of the Universe, Nucl. Phys. B 239
      (1984) 257. doi:10.1016/0550-3213(84)90093-2.

                                                132
[57] Y. Akrami, et al., Planck 2018 results. X. Constraints on inflation, As-
      tron. Astrophys. 641 (2020) A10. arXiv:1807.06211, doi:10.1051/
      0004-6361/201833887.

[58] G. W. Lyons, Complex solutions for the scalar field model of the universe,
      Phys. Rev. D 46 (1992) 1546�1550. doi:10.1103/PhysRevD.46.1546.

[59] G. Esposito, G. Platania, Inflationary Solutions in Quantum Cosmology,
      Class. Quant. Grav. 5 (1988) 937�949. arXiv:gr-qc/9509003, doi:10.
      1088/0264-9381/5/7/003.

[60] O. Janssen, Slow-roll approximation in quantum cosmology, Class.
      Quant. Grav. 38 (9) (2021) 095003. arXiv:2009.06282, doi:10.1088/
      1361-6382/abe143.

[61] J. B. Hartle, S. W. Hawking, T. Hertog, No-Boundary Measure of the
      Universe, Phys. Rev. Lett. 100 (2008) 201301. arXiv:0711.4630, doi:
      10.1103/PhysRevLett.100.201301.

[62] L. Battarra, J.-L. Lehners, On the No-Boundary Proposal for Ekpyrotic
      and Cyclic Cosmologies, JCAP 12 (2014) 023. arXiv:1407.4814, doi:
      10.1088/1475-7516/2014/12/023.

[63] T. Hertog, Predicting a Prior for Planck, JCAP 02 (2014) 043. arXiv:
      1305.6135, doi:10.1088/1475-7516/2014/02/043.

[64] J. K. Erickson, D. H. Wesley, P. J. Steinhardt, N. Turok, Kasner and
      mixmaster behavior in universes with equation of state w >= 1, Phys. Rev.
      D 69 (2004) 063514. arXiv:hep-th/0312009, doi:10.1103/PhysRevD.
      69.063514.

[65] J.-L. Lehners, P. McFadden, N. Turok, P. J. Steinhardt, Generating ekpy-
      rotic curvature perturbations before the big bang, Phys. Rev. D 76 (2007)
      103501. arXiv:hep-th/0702153, doi:10.1103/PhysRevD.76.103501.

[66] A. Ijjas, J.-L. Lehners, P. J. Steinhardt, General mechanism for pro-
      ducing scale-invariant perturbations and small non-Gaussianity in ekpy-
      rotic models, Phys. Rev. D 89 (12) (2014) 123520. arXiv:1404.1265,
      doi:10.1103/PhysRevD.89.123520.

[67] A. Ijjas, P. J. Steinhardt, Fully stable cosmological solutions with a non-
      singular classical bounce, Phys. Lett. B 764 (2017) 289�294. arXiv:1609.
      01253, doi:10.1016/j.physletb.2016.11.047.

[68] L. Battarra, J.-L. Lehners, On the Creation of the Universe via Ekpyrotic
      Instantons, Phys. Lett. B 742 (2015) 167�171. arXiv:1406.5896, doi:
      10.1016/j.physletb.2015.01.028.

[69] J.-L. Lehners, New Ekpyrotic Quantum Cosmology, Phys. Lett. B 750
      (2015) 242�246. arXiv:1504.02467, doi:10.1016/j.physletb.2015.
      09.032.

                                                133
[70] N. Arkani-Hamed, H.-C. Cheng, M. A. Luty, S. Mukohyama, Ghost con-
      densation and a consistent infrared modification of gravity, JHEP 05
      (2004) 074. arXiv:hep-th/0312099, doi:10.1088/1126-6708/2004/05/
      074.

[71] P. J. Steinhardt, N. Turok, Cosmic evolution in a cyclic universe,
      Phys. Rev. D 65 (2002) 126003. arXiv:hep-th/0111098, doi:10.1103/
      PhysRevD.65.126003.

[72] I. P. C. Heard, D. Wands, Cosmology with positive and negative ex-
      ponential potentials, Class. Quant. Grav. 19 (2002) 5435�5448. arXiv:
      gr-qc/0206085, doi:10.1088/0264-9381/19/21/309.

[73] E. Joos, H. D. Zeh, The Emergence of classical properties through in-
      teraction with the environment, Z. Phys. B 59 (1985) 223�243. doi:
      10.1007/BF01725541.

[74] W. H. Zurek, Decoherence, einselection, and the quantum origins of the
      classical, Rev. Mod. Phys. 75 (2003) 715�775. arXiv:quant-ph/0105127,
      doi:10.1103/RevModPhys.75.715.

[75] R. P. Woodard, Perturbative Quantum Gravity Comes of Age, Int. J.
      Mod. Phys. D 23 (09) (2014) 1430020. arXiv:1407.4748, doi:10.1142/
      S0218271814300201.

[76] J. J. Halliwell, J. B. Hartle, Integration Contours for the No Boundary
      Wave Function of the Universe, Phys. Rev. D 41 (1990) 1815. doi:10.
      1103/PhysRevD.41.1815.

[77] J. Feldbrugge, J.-L. Lehners, N. Turok, No rescue for the no boundary
      proposal: Pointers to the future of quantum cosmology, Phys. Rev. D
      97 (2) (2018) 023509. arXiv:1708.05104, doi:10.1103/PhysRevD.97.
      023509.

[78] J. Diaz Dorronsoro, J. J. Halliwell, J. B. Hartle, T. Hertog, O. Janssen,
      Real no-boundary wave function in Lorentzian quantum cosmology,
      Phys. Rev. D 96 (4) (2017) 043505. arXiv:1705.05340, doi:10.1103/
      PhysRevD.96.043505.

[79] O. Janssen, J. J. Halliwell, T. Hertog, No-boundary proposal in biaxial
      Bianchi IX minisuperspace, Phys. Rev. D 99 (12) (2019) 123531. arXiv:
      1904.11602, doi:10.1103/PhysRevD.99.123531.

[80] A. Di Tucci, J.-L. Lehners, No-Boundary Proposal as a Path Integral with
      Robin Boundary Conditions, Phys. Rev. Lett. 122 (20) (2019) 201302.
      arXiv:1903.06757, doi:10.1103/PhysRevLett.122.201302.

[81] A. Di Tucci, J.-L. Lehners, L. Sberna, No-boundary prescriptions in
      Lorentzian quantum cosmology, Phys. Rev. D 100 (12) (2019) 123543.
      arXiv:1911.06701, doi:10.1103/PhysRevD.100.123543.

                                                134
[82] J.-L. Lehners, Wave function of simple universes analytically continued
      from negative to positive potentials, Phys. Rev. D 104 (6) (2021) 063527.
      arXiv:2105.12075, doi:10.1103/PhysRevD.104.063527.

[83] J. J. Halliwell, J. Louko, Steepest Descent Contours in the Path Integral
      Approach to Quantum Cosmology. 2. Microsuperspace, Phys. Rev. D 40
      (1989) 1868. doi:10.1103/PhysRevD.40.1868.

[84] J. J. Halliwell, J. Louko, Steepest Descent Contours in the Path Integral
      Approach to Quantum Cosmology. 3. A General Method With Appli-
      cations to Anisotropic Minisuperspace Models, Phys. Rev. D 42 (1990)
      3997�4031. doi:10.1103/PhysRevD.42.3997.

[85] L. J. Garay, J. J. Halliwell, G. A. Mena Marugan, Path integral quantum
      cosmology: A Class of exactly soluble scalar field minisuperspace models
      with exponential potentials, Phys. Rev. D 43 (1991) 2572�2589. doi:
      10.1103/PhysRevD.43.2572.

[86] J. Diaz Dorronsoro, J. J. Halliwell, J. B. Hartle, T. Hertog, O. Janssen,
      Y. Vreys, Damped perturbations in the no-boundary state, Phys.
      Rev. Lett. 121 (8) (2018) 081302. arXiv:1804.01102, doi:10.1103/
      PhysRevLett.121.081302.

[87] J. Feldbrugge, J.-L. Lehners, N. Turok, Inconsistencies of the New No-
      Boundary Proposal, Universe 4 (10) (2018) 100. arXiv:1805.01609, doi:
      10.3390/universe4100100.

[88] C. Jonas, J.-L. Lehners, V. Meyer, Revisiting the no-boundary proposal
      with a scalar field, Phys. Rev. D 105 (4) (2022) 043529. arXiv:2112.
      07986, doi:10.1103/PhysRevD.105.043529.

[89] G. Fanaras, A. Vilenkin, Jackiw-Teitelboim and Kantowski-Sachs quan-
      tum cosmology, JCAP 03 (03) (2022) 056. arXiv:2112.00919, doi:
      10.1088/1475-7516/2022/03/056.

[90] C. W. Misner, Mixmaster universe, Phys. Rev. Lett. 22 (1969) 1071�1074.
      doi:10.1103/PhysRevLett.22.1071.

[91] A. Daughton, J. Louko, R. D. Sorkin, Instantons and unitarity in quantum
      cosmology with fixed four volume, Phys. Rev. D 58 (1998) 084008. arXiv:
      gr-qc/9805101, doi:10.1103/PhysRevD.58.084008.

[92] J.-L. Lehners, NUTs, Bolts and Stokes Phenomena in the No-Boundary
      Wave Function (2 2024). arXiv:2402.10501.

[93] J. M. Maldacena, The Large N limit of superconformal field theories and
      supergravity, Adv. Theor. Math. Phys. 2 (1998) 231�252. arXiv:hep-th/
      9711200, doi:10.1023/A:1026654312961.

                                                135
 [94] E. Witten, A Note On Complex Spacetime Metrics (11 2021). arXiv:
       2111.06514.

 [95] J.-L. Lehners, Allowable complex scalars from Kaluza-Klein compacti-
       fications and metric rescalings, Phys. Rev. D 107 (4) (2023) 046004.
       arXiv:2209.14669, doi:10.1103/PhysRevD.107.046004.

 [96] V. A. Belinsky, I. M. Khalatnikov, E. M. Lifshitz, Oscillatory approach
       to a singular point in the relativistic cosmology, Adv. Phys. 19 (1970)
       525�573. doi:10.1080/00018737000101171.

 [97] S. W. Hawking, J. C. Luttrell, The Isotropy of the Universe, Phys. Lett.
       B 143 (1984) 83. doi:10.1016/0370-2693(84)90809-8.

 [98] W. A. Wright, I. G. Moss, The Anisotropy of the Universe, Phys. Lett. B
       154 (1985) 115�119. doi:10.1016/0370-2693(85)90569-6.

 [99] P. Amsterdamski, WAVE FUNCTION OF AN ANISOTROPIC UNI-
       VERSE, Phys. Rev. D 31 (1985) 3073�3078. doi:10.1103/PhysRevD.
       31.3073.

[100] M. J. Duncan, L. G. Jensen, The Quantum Cosmology of an
       Anisotropic Universe, Nucl. Phys. B 312 (1989) 662�672. doi:10.1016/
       0550-3213(89)90576-2.

[101] S. del Campo, A. Vilenkin, Tunneling Wave Function for Anisotropic
       Universe, Phys. Lett. B 224 (1989) 45�48. doi:10.1016/0370-2693(89)
       91047-2.

[102] K. Fujio, T. Futamase, Appearance of classical Mixmaster Universe from
       the No-Boundary Quantum State, Phys. Rev. D 80 (2009) 023504. arXiv:
       0906.2616, doi:10.1103/PhysRevD.80.023504.

[103] S. F. Bramberger, S. Farnsworth, J.-L. Lehners, Wavefunction of
       anisotropic inflationary universes with no-boundary conditions, Phys.
       Rev. D 95 (8) (2017) 083513. arXiv:1701.05753, doi:10.1103/
       PhysRevD.95.083513.

[104] B. Carr, K. Kohri, Y. Sendouda, J. Yokoyama, Constraints on primordial
       black holes, Rept. Prog. Phys. 84 (11) (2021) 116902. arXiv:2002.12778,
       doi:10.1088/1361-6633/ac1e31.

[105] O. O� zsoy, G. Tasinato, Inflation and Primordial Black Holes (1 2023).
       arXiv:2301.03600.

[106] R. Bousso, S. W. Hawking, The Probability for primordial black holes,
       Phys. Rev. D 52 (1995) 5659�5664. arXiv:gr-qc/9506047, doi:10.1103/
       PhysRevD.52.5659.

                                                  136
[107] R. Bousso, S. W. Hawking, Pair creation of black holes during inflation,
       Phys. Rev. D 54 (1996) 6312�6322. arXiv:gr-qc/9606052, doi:10.1103/
       PhysRevD.54.6312.

[108] R. Bousso, S. W. Hawking, Lorentzian condition in quantum gravity,
       Phys. Rev. D 59 (1999) 103501, [Erratum: Phys.Rev.D 60, 109903 (1999)].
       arXiv:hep-th/9807148, doi:10.1103/PhysRevD.59.103501.

[109] W.-Z. Chao, Quantum creation of a black hole, Int. J. Mod. Phys. D 6
       (1997) 199. arXiv:gr-qc/9801020, doi:10.1142/S0218271897000121.

[110] R. Gregory, I. G. Moss, B. Withers, Black holes as bubble nucleation sites,
       JHEP 03 (2014) 081. arXiv:1401.0017, doi:10.1007/JHEP03(2014)
       081.

[111] P. Draper, S. Farkas, de Sitter black holes as constrained states in the
       Euclidean path integral, Phys. Rev. D 105 (12) (2022) 126022. arXiv:
       2203.02426, doi:10.1103/PhysRevD.105.126022.

[112] E. K. Morvan, J. P. van der Schaar, M. R. Visser, On the Euclidean
       Action of de Sitter Black Holes and Constrained Instantons (3 2022).
       arXiv:2203.06155.

[113] G. W. Gibbons, S. W. Hawking, Cosmological Event Horizons, Ther-
       modynamics, and Particle Creation, Phys. Rev. D 15 (1977) 2738�2751.
       doi:10.1103/PhysRevD.15.2738.

[114] H. Nariai, On a new cosmological solution of Einstein's field equations of
       gravitation, Sci. Rep. Tohoku Univ. 35 (1951) 62.

[115] P. H. Ginsparg, M. J. Perry, Semiclassical Perdurance of de Sitter
       Space, Nucl. Phys. B 222 (1983) 245�268. doi:10.1016/0550-3213(83)
       90636-3.

[116] V. F. Mukhanov, H. A. Feldman, R. H. Brandenberger, Theory of cosmo-
       logical perturbations. Part 1. Classical perturbations. Part 2. Quantum
       theory of perturbations. Part 3. Extensions, Phys. Rept. 215 (1992) 203�
       333. doi:10.1016/0370-1573(92)90044-Z.

[117] U. H. Gerlach, U. K. Sengupta, Homogeneous Collapsing Star: Tensor
       and Vector Harmonics for Matter and Field Asymmetries, Phys. Rev. D
       18 (1978) 1773�1784. doi:10.1103/PhysRevD.18.1773.

[118] J. J. Halliwell, S. W. Hawking, The Origin of Structure in the Universe,
       Phys. Rev. D 31 (1985) 1777. doi:10.1103/PhysRevD.31.1777.

[119] J. Garriga, X. Montes, M. Sasaki, T. Tanaka, Canonical quantization of
       cosmological perturbations in the one-bubble open universe, Nucl. Phys. B
       513 (1998) 343�374, [Erratum: Nucl.Phys.B 551, 511�511 (1999)]. arXiv:
       astro-ph/9706229, doi:10.1016/S0550-3213(97)00780-3.

                                                  137
[120] T. S. Bunch, P. C. W. Davies, Quantum Field Theory in de Sitter Space:
       Renormalization by Point Splitting, Proc. Roy. Soc. Lond. A 360 (1978)
       117�134. doi:10.1098/rspa.1978.0060.

[121] J. Feldbrugge, J.-L. Lehners, N. Turok, No smooth beginning for space-
       time, Phys. Rev. Lett. 119 (17) (2017) 171301. arXiv:1705.00192,
       doi:10.1103/PhysRevLett.119.171301.

[122] H. Matsui, S. Mukohyama, A. Naruko, No smooth spacetime in
       Lorentzian quantum cosmology and trans-Planckian physics, Phys. Rev.
       D 107 (4) (2023) 043511. arXiv:2211.05306, doi:10.1103/PhysRevD.
       107.043511.

[123] J. Garriga, X. Montes, M. Sasaki, T. Tanaka, Spectrum of cosmological
       perturbations in the one bubble open universe, Nucl. Phys. B 551 (1999)
       317�373. arXiv:astro-ph/9811257, doi:10.1016/S0550-3213(99)
       00181-9.

[124] S. Gratton, N. Turok, Cosmological perturbations from the no bound-
       ary Euclidean path integral, Phys. Rev. D 60 (1999) 123507. arXiv:
       astro-ph/9902265, doi:10.1103/PhysRevD.60.123507.

[125] J. M. Maldacena, Non-Gaussian features of primordial fluctuations in sin-
       gle field inflationary models, JHEP 05 (2003) 013. arXiv:astro-ph/
       0210603, doi:10.1088/1126-6708/2003/05/013.

[126] P. D. D'Eath, J. J. Halliwell, Fermions in Quantum Cosmology, Phys.
       Rev. D 35 (1987) 1100. doi:10.1103/PhysRevD.35.1100.

[127] T. Hertog, G. Tartaglino-Mazzucchelli, G. Venken, Spinors in Super-
       symmetric dS/CFT, JHEP 10 (2019) 117. arXiv:1905.01322, doi:
       10.1007/JHEP10(2019)117.

[128] P. V. Moniz, Supersymmetric quantum cosmology: Shaken not stirred,
       Int. J. Mod. Phys. A 11 (1996) 4321�4382. arXiv:gr-qc/9604025, doi:
       10.1142/S0217751X96002017.

[129] P. V. Moniz, Origin of structure in a supersymmetric quantum universe,
       Phys. Rev. D 57 (1998) 7071�7074. arXiv:gr-qc/9710113, doi:10.1103/
       PhysRevD.57.R7071.

[130] P. Vargas Moniz, Quantum cosmology - the supersymmetric per-
       spective: Vol. 1: Fundamentals, Vol. 803, 2010. doi:10.1007/
       978-3-642-11575-2.

[131] D. N. Page, Susskind's challenge to the Hartle-Hawking no-boundary pro-
       posal and possible resolutions, JCAP 01 (2007) 004. arXiv:hep-th/
       0610199, doi:10.1088/1475-7516/2007/01/004.

                                                  138
[132] G. Obied, H. Ooguri, L. Spodyneiko, C. Vafa, De Sitter Space and the
       Swampland (6 2018). arXiv:1806.08362.

[133] S. K. Garg, C. Krishnan, Bounds on Slow Roll and the de Sitter
       Swampland, JHEP 11 (2019) 075. arXiv:1807.05193, doi:10.1007/
       JHEP11(2019)075.

[134] S. W. Hawking, T. Hertog, Why does inflation start at the top of the hill?,
       Phys. Rev. D 66 (2002) 123509. arXiv:hep-th/0204212, doi:10.1103/
       PhysRevD.66.123509.

[135] J. B. Hartle, Anthropic reasoning and quantum cosmology, AIP Conf.
       Proc. 743 (1) (2004) 298�304. arXiv:gr-qc/0406104, doi:10.1063/1.
       1848335.

[136] S. Brahma, S. Shandera, Stochastic eternal inflation is in the swampland,
       JHEP 11 (2019) 016. arXiv:1904.10979, doi:10.1007/JHEP11(2019)
       016.

[137] T. Rudelius, Conditions for (No) Eternal Inflation, JCAP 08 (2019) 009.
       arXiv:1905.05198, doi:10.1088/1475-7516/2019/08/009.

[138] H. Matsui, F. Takahashi, T. Terada, Non-singular bouncing cosmology
       with positive spatial curvature and flat scalar potential, Phys. Lett. B 795
       (2019) 152�159. arXiv:1904.12312, doi:10.1016/j.physletb.2019.
       06.013.

[139] J.-L. Lehners, J. Quintin, Delicate curvature bounces in the no-boundary
       wave function and in the late universe (3 2024). arXiv:2403.15205.

[140] H. Matsui, T. Terada, Swampland Constraints on No-Boundary Quan-
       tum Cosmology, JHEP 10 (2020) 162. arXiv:2006.03443, doi:10.1007/
       JHEP10(2020)162.

[141] S. Kachru, R. Kallosh, A. D. Linde, S. P. Trivedi, De Sitter vacua in
       string theory, Phys. Rev. D 68 (2003) 046005. arXiv:hep-th/0301240,
       doi:10.1103/PhysRevD.68.046005.

[142] J.-L. Lehners, Small-Field and Scale-Free: Inflation and Ekpyrosis at
       their Extremes, JCAP 11 (2018) 001. arXiv:1807.05240, doi:10.1088/
       1475-7516/2018/11/001.

[143] J. B. Hartle, The State of the universe, in: Workshop on Conference
       on the Future of Theoretical Physics and Cosmology in Honor of Steven
       Hawking's 60th Birthday, 2002, pp. 615�620. arXiv:gr-qc/0209046.

[144] E. S. Fradkin, A. A. Tseytlin, Effective Field Theory from Quantized
       Strings, Phys. Lett. B 158 (1985) 316�322. doi:10.1016/0370-2693(85)
       91190-6.

                                                  139
[145] M. B. Green, M. Gutperle, P. Vanhove, One loop in eleven-dimensions,
       Phys. Lett. B 409 (1997) 177�184. arXiv:hep-th/9706175, doi:10.
       1016/S0370-2693(97)00931-3.

[146] C. Jonas, J.-L. Lehners, No-boundary solutions are robust to quantum
       gravity corrections, Phys. Rev. D 102 (2020) 123539. arXiv:2008.04134,
       doi:10.1103/PhysRevD.102.123539.

[147] S. W. Hawking, J. C. Luttrell, Higher Derivatives in Quantum Cos-
       mology. 1. The Isotropic Case, Nucl. Phys. B 247 (1984) 250. doi:
       10.1016/0550-3213(84)90380-8.

[148] P. A. Cano, K. Fransen, T. Hertog, Novel higher-curvature variations of
       R2 inflation, Phys. Rev. D 103 (10) (2021) 103531. arXiv:2011.13933,
       doi:10.1103/PhysRevD.103.103531.

[149] G. Narain, Surprises in Lorentzian path-integral of Gauss-Bonnet gravity,
       JHEP 04 (2022) 153. arXiv:2203.05475, doi:10.1007/JHEP04(2022)
       153.

[150] O. Aharony, S. S. Gubser, J. M. Maldacena, H. Ooguri, Y. Oz, Large N
       field theories, string theory and gravity, Phys. Rept. 323 (2000) 183�386.
       arXiv:hep-th/9905111, doi:10.1016/S0370-1573(99)00083-6.

[151] H. Fuji, S. Hirano, S. Moriyama, Summing Up All Genus Free Energy
       of ABJM Matrix Model, JHEP 08 (2011) 001. arXiv:1106.4631, doi:
       10.1007/JHEP08(2011)001.

[152] M. Marino, P. Putrov, ABJM theory as a Fermi gas, J. Stat. Mech. 1203
       (2012) P03001. arXiv:1110.4066, doi:10.1088/1742-5468/2012/03/
       P03001.

[153] P. Caputa, S. Hirano, Airy Function and 4d Quantum Gravity, JHEP 06
       (2018) 106. arXiv:1804.00942, doi:10.1007/JHEP06(2018)106.

[154] S. W. Hawking, D. N. Page, Thermodynamics of Black Holes in anti-
       De Sitter Space, Commun. Math. Phys. 87 (1983) 577. doi:10.1007/
       BF01208266.

[155] V. Balasubramanian, P. Kraus, A Stress tensor for Anti-de Sitter gravity,
       Commun. Math. Phys. 208 (1999) 413�428. arXiv:hep-th/9902121, doi:
       10.1007/s002200050764.

[156] J. D. Brown, J. Creighton, R. B. Mann, Temperature, energy and heat
       capacity of asymptotically anti-de Sitter black holes, Phys. Rev. D 50
       (1994) 6394�6403. arXiv:gr-qc/9405007, doi:10.1103/PhysRevD.50.
       6394.

[157] T. Hertog, J. Hartle, Holographic No-Boundary Measure, JHEP 05 (2012)
       095. arXiv:1111.6090, doi:10.1007/JHEP05(2012)095.

                                                  140
[158] J. B. Hartle, S. W. Hawking, T. Hertog, Accelerated Expansion from
       Negative  (5 2012). arXiv:1205.3807.

[159] J. B. Hartle, S. W. Hawking, T. Hertog, Quantum Probabilities for
       Inflation from Holography, JCAP 01 (2014) 015. arXiv:1207.6653,
       doi:10.1088/1475-7516/2014/01/015.

[160] J. B. Hartle, S. W. Hawking, T. Hertog, Vector Fields in Holographic
       Cosmology, JHEP 11 (2013) 201. arXiv:1305.7190, doi:10.1007/
       JHEP11(2013)201.

[161] T. Hertog, E. van der Woerd, Primordial fluctuations from complex AdS
       saddle points, JCAP 02 (2016) 010. arXiv:1509.03291, doi:10.1088/
       1475-7516/2016/02/010.

[162] G. Conti, T. Hertog, Y. Vreys, Squashed Holography with Scalar Con-
       densates, JHEP 09 (2018) 068. arXiv:1707.09663, doi:10.1007/
       JHEP09(2018)068.

[163] S. W. Hawking, T. Hertog, H. S. Reall, Brane new world, Phys. Rev. D
       62 (2000) 043501. arXiv:hep-th/0003052, doi:10.1103/PhysRevD.62.
       043501.

[164] G. T. Horowitz, J. M. Maldacena, The Black hole final state, JHEP 02
       (2004) 008. arXiv:hep-th/0310281, doi:10.1088/1126-6708/2004/02/
       008.

[165] H. Ooguri, C. Vafa, E. P. Verlinde, Hartle-Hawking wave-function for flux
       compactifications, Lett. Math. Phys. 74 (2005) 311�342. arXiv:hep-th/
       0502211, doi:10.1007/s11005-005-0022-x.

[166] S. de Haro, S. N. Solodukhin, K. Skenderis, Holographic reconstruction
       of space-time and renormalization in the AdS / CFT correspondence,
       Commun. Math. Phys. 217 (2001) 595�622. arXiv:hep-th/0002230, doi:
       10.1007/s002200100381.

[167] A. Strominger, The dS / CFT correspondence, JHEP 10 (2001) 034.
       arXiv:hep-th/0106113, doi:10.1088/1126-6708/2001/10/034.

[168] A. Strominger, Inflation and the dS / CFT correspondence, JHEP 11
       (2001) 049. arXiv:hep-th/0110087, doi:10.1088/1126-6708/2001/11/
       049.

[169] A. T. Mithani, A. Vilenkin, Inflation with negative potentials and the
       signature reversal symmetry, JCAP 04 (2013) 024. arXiv:1302.0568,
       doi:10.1088/1475-7516/2013/04/024.

[170] P. Candelas, G. T. Horowitz, A. Strominger, E. Witten, Vacuum Con-
       figurations for Superstrings, Nucl. Phys. B 258 (1985) 46�74. doi:
       10.1016/0550-3213(85)90602-9.

                                                  141
[171] L. Randall, R. Sundrum, An Alternative to compactification, Phys.
       Rev. Lett. 83 (1999) 4690�4693. arXiv:hep-th/9906064, doi:10.1103/
       PhysRevLett.83.4690.

[172] B. Crampton, C. N. Pope, K. S. Stelle, Braneworld localisation in hyper-
       bolic spacetime, JHEP 12 (2014) 035. arXiv:1408.7072, doi:10.1007/
       JHEP12(2014)035.

[173] J.-P. Uzan, The Fundamental Constants and Their Variation: Observa-
       tional Status and Theoretical Motivations, Rev. Mod. Phys. 75 (2003)
       403. arXiv:hep-ph/0205340, doi:10.1103/RevModPhys.75.403.

[174] W. Taylor, Y.-N. Wang, The F-theory geometry with most flux vacua,
       JHEP 12 (2015) 164. arXiv:1511.03209, doi:10.1007/JHEP12(2015)
       164.

[175] E. Palti, The Swampland: Introduction and Review, Fortsch. Phys. 67 (6)
       (2019) 1900037. arXiv:1903.06239, doi:10.1002/prop.201900037.

[176] P. Agrawal, G. Obied, P. J. Steinhardt, C. Vafa, On the Cosmological
       Implications of the String Swampland, Phys. Lett. B 784 (2018) 271�276.
       arXiv:1806.09718, doi:10.1016/j.physletb.2018.07.040.

[177] S. Lu�st, C. Vafa, M. Wiesner, K. Xu, Holography and the KKLT scenario,
       JHEP 10 (2022) 188. arXiv:2204.07171, doi:10.1007/JHEP10(2022)
       188.

[178] S. Sethi, C. Vafa, E. Witten, Constraints on low dimensional string
       compactifications, Nucl. Phys. B 480 (1996) 213�224. arXiv:hep-th/
       9606122, doi:10.1016/S0550-3213(96)00483-X.

[179] S. B. Giddings, S. Kachru, J. Polchinski, Hierarchies from fluxes in
       string compactifications, Phys. Rev. D 66 (2002) 106006. arXiv:hep-th/
       0105097, doi:10.1103/PhysRevD.66.106006.

[180] J. Hartle, S. W. Hawking, T. Hertog, Local Observation in Eternal in-
       flation, Phys. Rev. Lett. 106 (2011) 141302. arXiv:1009.2525, doi:
       10.1103/PhysRevLett.106.141302.

[181] J. D. Brown, C. Teitelboim, Neutralization of the Cosmological Constant
       by Membrane Creation, Nucl. Phys. B 297 (1988) 787�836. doi:10.1016/
       0550-3213(88)90559-7.

[182] J.-L. Lehners, R. Leung, K. S. Stelle, How to create universes with internal
       flux, Phys. Rev. D 107 (4) (2023) 046006. arXiv:2209.08960, doi:10.
       1103/PhysRevD.107.046006.

[183] S. V. Ketov, H. Nakada, Inflation from (R + Rn - 2) Gravity in Higher
       Dimensions, Phys. Rev. D 95 (10) (2017) 103507. arXiv:1701.08239,
       doi:10.1103/PhysRevD.95.103507.

                                                  142
[184] S. P. Otero, F. G. Pedro, C. Wieck, R + Rn Inflation in higher-
       dimensional Space-times, JHEP 05 (2017) 058. arXiv:1702.08311, doi:
       10.1007/JHEP05(2017)058.

[185] A. A. Starobinsky, A New Type of Isotropic Cosmological Models
       Without Singularity, Phys. Lett. B 91 (1980) 99�102. doi:10.1016/
       0370-2693(80)90670-X.

[186] E. Cremmer, B. Julia, J. Scherk, Supergravity Theory in Eleven-
       Dimensions, Phys. Lett. B 76 (1978) 409�412. doi:10.1016/
       0370-2693(78)90894-8.

[187] M. Henneaux, C. Teitelboim, P form electrodynamics, Found. Phys. 16
       (1986) 593�617. doi:10.1007/BF01889624.

[188] J. Louko, R. D. Sorkin, Complex actions in two-dimensional topology
       change, Class. Quant. Grav. 14 (1997) 179�204. arXiv:gr-qc/9511023,
       doi:10.1088/0264-9381/14/1/018.

[189] M. Kontsevich, G. Segal, Wick Rotation and the Positivity of Energy
       in Quantum Field Theory, Quart. J. Math. Oxford Ser. 72 (1-2) (2021)
       673�699. arXiv:2105.10161, doi:10.1093/qmath/haab027.

[190] S. Weinberg, E. Witten, Limits on Massless Particles, Phys. Lett. B 96
       (1980) 59�62. doi:10.1016/0370-2693(80)90212-9.

[191] J.-L. Lehners, Allowable complex metrics in minisuperspace quantum
       cosmology, Phys. Rev. D 105 (2) (2022) 026022. arXiv:2111.07816,
       doi:10.1103/PhysRevD.105.026022.

[192] C. Jonas, J.-L. Lehners, J. Quintin, Uses of complex metrics in cosmology,
       JHEP 08 (2022) 284. arXiv:2205.15332, doi:10.1007/JHEP08(2022)
       284.

[193] M. J. Duff, B. E. W. Nilsson, C. N. Pope, Kaluza-Klein Supergravity,
       Phys. Rept. 130 (1986) 1�142. doi:10.1016/0370-1573(86)90163-8.

[194] T. Hertog, O. Janssen, J. Karlsson, Kontsevich-Segal Criterion in the No-
       Boundary State Constrains Inflation, Phys. Rev. Lett. 131 (19) (2023)
       191501. arXiv:2305.15440, doi:10.1103/PhysRevLett.131.191501.

[195] J.-L. Lehners, J. Quintin, A small Universe, Phys. Lett. B 850 (2024)
       138488. arXiv:2309.03272, doi:10.1016/j.physletb.2024.138488.

[196] J. McNamara, C. Vafa, Cobordism Classes and the Swampland (9 2019).
       arXiv:1909.10355.

[197] B. S. DeWitt, Quantum Theory of Gravity. 1. The Canonical Theory,
       Phys. Rev. 160 (1967) 1113�1148. doi:10.1103/PhysRev.160.1113.

                                                  143
[198] Battelle rencontres - 1967 lectures in mathematics and physics: Seattle,
       WA, USA, 16 - 31 July 1967, W. A. Benjamin, New York, NY, 1968.

[199] P. W. Higgs, Integration of Secondary Constraints in Quantized General
       Relativity, Phys. Rev. Lett. 1 (1958) 373�374, [Erratum: Phys.Rev.Lett.
       3, 66�67 (1959)]. doi:10.1103/PhysRevLett.1.373.

[200] C. Teitelboim, Quantum Mechanics of the Gravitational Field, Phys. Rev.
       D 25 (1982) 3159. doi:10.1103/PhysRevD.25.3159.

[201] C. Teitelboim, The Proper Time Gauge in Quantum Theory of Gravita-
       tion, Phys. Rev. D 28 (1983) 297. doi:10.1103/PhysRevD.28.297.

[202] E. S. Fradkin, G. A. Vilkovisky, QUANTIZATION OF RELATIVISTIC
       SYSTEMS WITH CONSTRAINTS, Phys. Lett. B 55 (1975) 224�226.
       doi:10.1016/0370-2693(75)90448-7.

[203] I. A. Batalin, G. A. Vilkovisky, Relativistic S Matrix of Dynamical Sys-
       tems with Boson and Fermion Constraints, Phys. Lett. B 69 (1977) 309�
       312. doi:10.1016/0370-2693(77)90553-6.

[204] L. D. Faddeev, V. N. Popov, Covariant quantization of the gravi-
       tational field, Usp. Fiz. Nauk 111 (1973) 427�450. doi:10.1070/
       PU1974v016n06ABEH004089.

[205] M. Henneaux, Hamiltonian Form of the Path Integral for Theories
       with a Gauge Freedom, Phys. Rept. 126 (1985) 1�66. doi:10.1016/
       0370-1573(85)90103-6.

[206] G. Esposito, Quantum gravity, quantum cosmology and Lorentzian ge-
       ometries, Vol. 12, 1992. doi:10.1007/978-3-540-47295-7.

[207] S. Lefschetz, Applications of Algebraic Topology. Graphs and Networks.
       the Picard-Lefschetz Theory and Feynman Integrals, 1975.

[208] E. Witten, Analytic Continuation Of Chern-Simons Theory, AMS/IP
       Stud. Adv. Math. 50 (2011) 347�446. arXiv:1001.2933.

                                                  144
