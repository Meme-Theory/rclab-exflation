# 2025 Test particles in Kaluza Klein models

**Source:** `16_2025_Test_particles_in_Kaluza_Klein_models.pdf`

---

arXiv:2406.09503v3 [hep-th] 10 Dec 2024       Test particles in Kaluza-Klein models

                                                                               Jo~ao Baptista
                                                                                  June 2024

                                                                                  Abstract

                                         Geodesics in general relativity describe the behaviour of test particles in a gravitational
                                         field. In 5D Kaluza-Klein, geodesics reproduce the Lorentz force motion of particles in
                                         an electromagnetic field. This paper studies geodesic motion on a higher-dimensional
                                         M4 � K with background metrics encoding general 4D gauge fields and Higgs-like scalars.
                                         It shows that the classical mass and charge of a test particle become variable quantities
                                         when the geodesic traverses regions of spacetime with massive gauge fields, such as the
                                         weak force field, or with non-constant Higgs scalars. This agrees with the physical fact
                                         that interactions mediated by massive bosons can change the mass and charge of particles.
                                         The variation rates of mass and charge along a geodesic are given by natural geometric
                                         formulae. In regions where mass is preserved, there are additional constants of motion,
                                         one for every abelian or simple summand in the Killing algebra of K. The last part of
                                         the paper discusses traditional difficulties of Kaluza-Klein models, such as the low q/m
                                         ratios in the 5D model. It suggests possible ways to circumvent them. It also remarks the
                                         naturalness of a model in which elementary particles always travel at the speed of light
                                         in higher dimensions.

                                         Keywords: Kaluza-Klein theories; geodesic motion; Riemannian submersions; test particles;
                                         momentum; rest mass; charge.
Contents

1 Introduction and overview of results . . . . . . . . . . . . . . . . . . . . . . . . . 1
2 Motion in the vacuum and 4D inertial frames . . . . . . . . . . . . . . . . . . . 10
3 Curves in Riemannian submersions . . . . . . . . . . . . . . . . . . . . . . . . . 11
4 Geodesics in Riemannian submersions . . . . . . . . . . . . . . . . . . . . . . . . 13
5 Constants of motion among massless gauge fields . . . . . . . . . . . . . . . . . 17
6 Higher-dimensional momentum and mass . . . . . . . . . . . . . . . . . . . . . . 21
7 Rest mass variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
8 Charges and charge variation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
9 A unique speed in higher dimensions . . . . . . . . . . . . . . . . . . . . . . . . 27
10 Parameterizing the space of null geodesics . . . . . . . . . . . . . . . . . . . . . 30
11 Difficulties with geodesics on Einstein backgrounds . . . . . . . . . . . . . . . . 34
A Auxiliary results and a remark on notation . . . . . . . . . . . . . . . . . . . . . 40
B Parallel transport in Riemannian submersions . . . . . . . . . . . . . . . . . . . 43
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

                                                         i
1 Introduction and overview of results

This paper studies geodesic motion on a higher-dimensional spacetime M4 � K and how
it is perceived through the lens of 4D physics. The setting is more general than usual,
with background Kaluza-Klein metrics that encode both massless and massive 4D fields.
Geometrically, those metrics determine Riemannian submersions with fibres that need not
be totally geodesic. The main physical motivation is the notion that, in these conditions,
a particle's classical mass and electromagnetic charge should not be strict constants of
motion. When massive gauge fields are present, or when the Higgs fields are not constant,
physical particles can interact with massive bosons, so their own charge and mass can
change. Thus, it would be natural to have definitions of mass and charge of a test particle
that enabled such variations along a geodesic. This would also illustrate how a higher-
dimensional, classical theory can produce 4D effects (particle charge and mass change)
that usually only appear in QFT calculations.

    Thinking along those lines, the author was led to consider how 4D proper time, denoted
 , evolves along an affine geodesic (s) on the spacetime P = M4 � K. In this setting,
the covariantly conserved momentum is the higher-dimensional tangent vector

                            p(s)    =      d   =     d   d   =   m(s)      d  ,                          (1.1)
                                           ds        ds  d                 d

where    is  a   constant  with  dimension     MT-1.    The  factor  m(s) =      d   is  the  particle's  rest
                                                                                 ds

mass, as can be recognized by projecting the relation to M4. So a non-constant rate of

change  d    is  perceived  in  4D  as  a  variable  mass.   As  will  be  seen  later,  it  turns  out   that
        ds

4D proper time and the geodesic parameter s need not be proportional to each other in

regions where the internal geometry is not covariantly constant. So the particle's classical

mass m(s) can vary when the geodesic traverses those regions, as desired.

    It also turns out that the phenomenon of geodesic mass variation had been previously
noticed in the Kaluza-Klein literature. Specifically, in studies of the 5D model, with
K = U(1) and mass variation coming from a non-constant size of the internal circle [1�5].
In that electromagnetic setting, however, it was regarded as an undesirable difficulty of
Kaluza-Klein theory. Rest mass variation is not observed in real electromagnetic interac-
tions, so it was not easy to offer a physical understanding of the phenomenon. Arguments
were proposed to avoid it or find alternative interpretations [6, 7]. Another example was
described in [8], where K is a group manifold with variable size and fixed, bi-invariant
geometry. Still, the physical meaning of mass variation remained unclear.

    A wider perspective seems to be key in this instance. For a higher-dimensional K
with richer geometry, it becomes possible to distinguish the separate effects on geodesics
caused by electromagnetic-like gauge fields, non-abelian massless gauge fields, massive

                                                     1
gauge fields and Higgs-like scalars. And when one recognizes that the only fields able to
change the mass of a test particle are the massive gauge fields (such as the weak force field)
and the Higgs-like scalars, a natural physical interpretation emerges. The phenomenon
of geodesic mass variation seems to describe the physical fact that interactions mediated
by massive fields and massive bosons are able to change the mass of particles.

    What about charge? In the geodesic model, all internal motion is perceived as mass
in four dimensions, but electromagnetic charge is related to the component of internal
momentum along a specific Killing direction inside K. So, in this model, there can be mass
without charge, but not the other way around, which fits observation. The independent
existence of mass and charge can occur only when the dimension of K is greater than
one. Otherwise, there is no meaningful distinction between the internal momentum and
its component along the Killing field.

    The higher-dimensional definition of charge of a test particle has three natural prop-
erties: i) charge is a constant of geodesic motion in regions of spacetime that only have
massless gauge fields and constant Higgs scalars; ii) in those regions, geodesics project
down to Lorentz force motions in four dimensions, as usual in 5D Kaluza-Klein; iii) in
regions of spacetime with massive gauge fields, the test particle's charge can vary along
a geodesic if and only if the bosons associated with the fields are charged. Thus, higher-
dimensional geodesics give a fairly good account of the properties of charged particles, at
least qualitatively. They reflect the physical fact that interactions mediated by charged
gauge bosons, such as the Standard Model's W bosons, can modify the charge of particles,
while interactions mediated by massless or by massive, neutral gauge bosons, cannot. This
property of higher-dimensional geodesics apparently has not been remarked before.

    Another relevant property of the geodesic model is that particles travelling at the
speed of light on M4 cannot interact directly with gauge fields or Higgs-like scalars, at
least classically. More precisely, the projection to M4 of the particle's motion on P is
independent of the values of such fields. This property is incompatible with the motion
of the old massless neutrinos, since they were thought to interact with the weak field
and travel at the speed of light on Minkowski space. So the geodesic model disfavours
the existence of massless neutrinos or similar particles. This also does not seem to have
been remarked before. Of course, one should still bear in mind that geodesic motion is
a classical approximation that disregards back-reaction, quantization and the fermionic
nature of particles.

    Our study of geodesic motion on P = M4 � K, for arbitrary K, relies on classical
geometrical results about Riemannian submersions developed in [9�12] and presented
in [13, 14], for example. Extended reviews of the Kaluza-Klein framework can be found
in [15�22]. Some of the early original references are [23�31]. Geodesic motion has been

                                                        2
studied since the very beginning of Kaluza-Klein literature. The main focus has been on
the 5D case, where calculations are more explicit and differential geometric techniques less
necessary (e.g. [2,23,29,32�36]). This paper follows the notation in [37] and its treatment
of massive gauge fields and Higgs-like fields. More comments about the literature will be
added below, as we give an overview of the main results and observations in this paper.

Rest mass variation

Consider a metric gP on the higher-dimensional spacetime P = M4 � K such that the
projection to M4 is a Riemannian submersion. As described in section 3, this is equivalent
to taking a gP determined by three simpler objects: i) a metric gM on the base M4; ii) a
family of Riemannian metrics gK(x) on the fibres K parametrized by the points x  M4;
iii) a gauge one-form A on M4 with values in the vector fields on K. These objects
determine the higher-dimensional metric through the relations

gP (U, V ) = gK(U, V )
gP (X, V ) = - gK (A(X), V )
gP (X, Y ) = gM (X, Y ) + gK (A(X), A(Y )) ,

valid for all tangent vectors X, Y  T M and vertical vectors U, V  T K. These relations
generalize the usual Kaluza ansatz for gP . Since the gauge one-form has values in the Lie
algebra of vector fields on K, the gauge group is Diff(K) or a subgroup. The gauge group
need not act on K only through isometries of gK.

    Now let (s) be a timelike or null geodesic on (P, gP ) representing the motion of a test
particle. It is a curve satisfying   = 0. Denote by M (s) the projection of this curve
to Minkowski space. The main result of section 7 says that the particle's rest mass, as
defined in (1.1), changes according to

                     c2  d   m2(s)  =  - (dAgK)M (pV , pV ) .  (1.2)
                         ds

Here pV denotes the vertical (internal) component of the particle's momentum vector,

while (dAgK)M is a covariant derivative of the internal metric along the vector M tangent
to M4. So the rest mass of the particle is a constant of geodesic motion in regions where
gK is covariantly constant, but may change elsewhere.

    The derivative dAgK measures how gK changes along M4 up to diffeomorphisms of K.
It is equivariant under Diff(K)-gauge transformations. Geometrically, it can be identified

with the second fundamental form of the fibres of P . As in [37], it can be expressed in

terms of Lie derivatives and the gauge one-forms Aa as

(dAgK)X(U, V ) = (LX gK)(U, V ) + Aa(X) (Lea gK)(U, V ) .      (1.3)

                                       3
Here X is any vector in T M; U and V are vertical vectors in T K; and Lea gK denotes the
Lie derivative along the internal vector field ea. Thus, dAgK vanishes when the internal
metric is constant along M4 and, simultaneously, only gauge fields with values in the
Killing vectors of gK are non-zero. Those are precisely the massless gauge fields, since

                  Mass Aa� 2         K Lea gK , Lea gK volgK                            (1.4)
                                       2 K gK(ea, ea) volgK

for any (divergence-free) vector field ea on a compact K [37]. Therefore, we conclude that
when the geodesic traverses regions of spacetime with changing gK or with massive gauge
fields, such as the weak force field, the particle's classical rest mass m(s) can indeed vary.

    Rest mass variation can be understood as a transfer between 4D momentum and
internal momentum. This transfer does not occur in regions with vacuum-type, product
geometries gM +gK. There, the two momentum components are uncoupled and separately
conserved. If massless gauge fields are turned on, the geometry is no longer a product,
but 4D motion is only lightly coupled to internal motion. The direction of 4D momentum
can change, but its magnitude is still conserved. These are Lorentz force-type motions.
Internal and 4D momenta will just rotate within the vertical and horizontal subspaces,
respectively. In regions where the higher-dimensional geometry is very different from a
product, only the full momentum vector conserves its norm along general geodesics. The
norms of the 4D and internal components can both change, with opposite signs, due to
a rotation of the full momentum mixing those components. This process is perceived
in 4D as a change of the particle's rest mass. The geometry distortions that produce it
correspond to a gP encoding 4D massive gauge fields or a non-constant internal metric.

    Note that having an internal metric that changes along M4 is equivalent to having non-
constant Higgs-like fields. If we regard the components of gK as fields on M4, they play the
exact role of Higgs fields in usual gauge theories. This is apparent from the decomposition
of the higher-dimensional scalar curvature RgP in the Einstein-Hilbert action,

  RgP volgP =  P  RgM  +  RgK  -  1  |FA|2  -  1  |dAgK |2  +  |dA (volgK )|2  volgP .  (1.5)
                                  4            4
P

This formula extends the usual Kaluza-Klein result to the setting of general Riemannian
submersions, where the geometry of the fibres can change. For more details, see [37].

Charges and charge variation

Now let us consider particles' charges. Let  be an electromagnetic-like Killing vector
field of gK. It is an internal Killing field that commutes with all other Killing fields on K.
If a particle's motion is parameterized by a geodesic (s) on P with momentum p =   ,

                                     4
we define the particle's charge with respect to  as the scalar

q(s) := - gP (, p) = - gK(, pV ) .                                              (1.6)

Section 5 shows that q(s) is a constant of geodesic motion in regions where only massless
gauge fields are present and the internal geometry does not change. This is true for any
metric gM on M4. But there are more constants of motion in these regions. Essentially,
there is one constant for every summand in the decomposition

                              k = a1  � � �  am                                 (1.7)

of the Killing algebra of gK as a sum of abelian or simple subalgebras. That constant of
motion measures how orthogonal the derivative vector  (s) is to the subspace of T(s)P
spanned by the Killing fields in the respective summand. And, for a geodesic, this scalar
is independent of s.

    In regions where the internal metric gK is constant but some massive gauge fields are
non-zero, the charges described above are well-defined but are not constants of motion
anymore. For example, section 8 shows that an electromagnetic-like charge evolves as

              d   q (s)       =  Aa( M ) gP ([, ea], p)                         (1.8)
              ds

along a higher-dimensional geodesic (s) with momentum p(s). So the test particle's
-charge may vary when Aa is non-zero and the associated gauge boson is -charged (i.e.
when [, ea] = 0 as a vector field on K). This effect apparently has not been reported
before. It agrees with the physical fact that interactions mediated by massive, charged
gauge bosons, such as the Standard Model's W bosons, can modify the charge of particles.

    The charge variation formula can be extended to the scalars associated to the simple
summands ar in the Killing algebra of gK. This variation is different from the rotation of
isospin along a geodesic found in [29, 38] and reviewed in [39]. More details in section 8.

Equations of geodesic motion

In section 4 we write down the equation of geodesic motion for a general submersive
metric on M4 � K, as translated from [12]. The differences in notation between [12] and
the present paper are described in appendix A. The horizontal component of that equation
says that the projection of the geodesic to four dimensions, denoted M (s), satisfies

gM MM  M , X  =   gK(ea,  V ) FAa( M , X)        +  1  (dAgK)X ( V  ,  V  )  .  (1.9)
                                                    2

This is a generalization of the equation derived by Kerner when K is a Lie group with
a constant bi-invariant metric [29]. It also extends the equations obtained when K is a

                                 5
circle or group manifold of variable size [1�3, 5, 8]. It is valid for arbitrary gauge fields,
arbitrary K, and internal metrics gK(x) that can vary arbitrarily along M4.

    In regions where there are no massive gauge fields and the internal geometry is con-
stant, the term dAgK vanishes and the equation simplifies. It reduces to the usual Lorentz
force equation when only an electromagnetic-like gauge field is present, as in the 5D cal-
culation. This is verified in section 8 using the previous definitions of mass and charge.
It justifies the interpretation of the scalar q(s) as a charge.

A unique speed in higher dimensions

In section 9, we remark the naturalness of the hypothesis that elementary particles always
travel at the speed of light in higher dimensions. It is the projection of velocities to three
dimensions that appears to produce speeds in the range [0, c], as observed macroscopically.
This is equivalent to saying that particles always follow null paths on P .

    This hypothesis is not entirely unreasonable because null paths on P always project
down to timelike or null paths on M4, in the Kaluza-Klein framework. They never project
down to spacelike paths. Higher-dimensional null paths can cover all types of causal
motion on Minkowski space. So timelike paths on P do not seem necessary. Thus, it is
natural to forgo them provisionally and investigate the consistency of a dynamical model
entirely based on null paths on P .

    In these conditions, all particles obey an energy-momentum relation similar to that
of photons, but in higher dimensions. It projects down to the usual energy-momentum
relation in four dimensions. For example, when gP = gM + gK is a simple product
metric, the higher-dimensional momentum vector can be written in an inertial frame as
p = (E, p + pK), where E is the particle's energy, p and pK are its 3-momentum and
internal momentum vectors, respectively, and we have put c = 1. So when p is null with
respect to gP , we get that

                       E2 = gP (p + pK, p + pK) = |p|2 + gK(pK, pK ) .

The first equality is a photon-like energy-momentum relation in higher dimensions. The
second equality becomes the usual 4D energy-momentum relation if the particle's rest
mass is identified with the norm of its internal momentum, m2 = gK(pK, pK).

    If the higher-dimensional speed is always c, as advocated, a particle at rest on 3D
space is necessarily moving at full speed c along K. Then the associated kinetic energy
is a natural source of the particle's energy at spatial rest, E0 = mc2. It is appealing to
think that rest energy is simply the kinetic energy of internal motion, with no need for
alternative mechanisms to store energy in a point-like mass.

                                                        6
    The hypothesis of a unique speed in higher dimensions provides a natural origin for
3D rest energy. Conversely, the assumption of a fully kinetic origin of rest energy, if
granted, also implies that timelike geodesics in higher-dimensions should not be allowed
to represent physical motions. Otherwise, a timelike particle moving with a 3-dimensional
speed lower than c could very well have zero velocity along K and hence have no rest
energy or rest mass. And such particles have never been observed. Thus, when 3D
rest energy is identified with the internal kinetic energy, only allowing null geodesics on
P derives from the experimental fact that massless particles always travel at the speed
of light on M4. Having a unique finite speed c for all elementary particles is also a
mathematically attractive feature, simpler than having a closed interval [0, c] of possible
speeds. The inescapable price is having to work with a higher-dimensional spacetime, of
course.

    As described in section 9, the hypothesis of a unique speed in higher dimensions for
all elementary particles would not be tenable in the traditional 5D Kaluza-Klein model.
Even forgetting about the strong and weak forces. This is because the null geodesics of
a 5D metric with circle isometry do not have enough degrees of freedom to reproduce all
the combinations of mass and electromagnetic charge observed in elementary particles.
This objection disappears for a higher-dimensional K. So a geodesic model entirely based
on null paths seems to be more tenable in this case. It also fits better with the commonly
stated aim of representing fermions by solutions of a single, massless, Dirac-like equation
for higher-dimensional spinors.

Spaces of null geodesics

Let Nh+ denote the space of null geodesics starting at a point h in P and moving forward
in time. Each geodesic (s) in this space is characterized by its null tangent vector  (0)
at h. In section 10 we describe two distinct parameterizations of Nh+, one relying on the
particles' momenta and the other on the celestial sphere of velocities.

    Different geodesics in Nh+ represent the motion of particles with different masses and
electromagnetic charges. Fixing the values of those constants carves out a smaller sub-
space Nh+(m, q) inside Nh+. In section 10 it is shown that


                                       if |q| > m c ||
                                       if |q| = m c ||
                                       if |q| < m c || .


Nh+(m, q)                                                 (1.10)

                              R3


                            R3 � Sk-2

Here || denotes the Riemannian length (gK)h(, ) of the Killing vector field at the
point h. Thus, in this model, particles with a given classical mass cannot have arbitrarily

                                  7
strong charge. This is natural because, according to (6.6), mass is related to the norm of
vertical momentum, while q measures the component of that same momentum along .

Some traditional difficulties in Kaluza-Klein

Kaluza-Klein models are often studied under strong simplifying assumptions, such as
minimal 5D dimensions, or constant internal geometry, or the assumption that all relev-
ant gauge fields are associated with internal isometries. Those simplifications facilitate
the analysis but also create problems. In fact, we argue that some of the difficulties
traditionally attributed to the Kaluza-Klein framework are due to those simplifications.

    For example, the physical weak force field is usually associated with an SU(2)-isometry
of internal space. But its bosons are massive, albeit light when compared to the Planck
mass. So the mass formula (1.4) suggests that the weak field should not be associated with
exact isometries of gK. The Lie derivatives LeagK can be small yet non-zero. Abandoning
the exact isometry assumption has an extra advantage, as described in [37]. It offers a
possible way out of the main no-go arguments against having chiral fermions in Kaluza-
Klein, such as the arguments based on the Atiyah-Hirzebruch theorem [40].

    Another often-cited difficulty, in the 5D model, is that the Lorentz force equation
of motion can be recovered from geodesics only in regions where the internal circle has
constant size. And if this condition is granted, the full 5D equations of motion force the
norm |FA|2 of the electromagnetic field strength to vanish in those same regions, which
is not realistic [20, 21]. Moreover, even ignoring that problem, the range of 4D motions
projected by 5D geodesics has severe limitations. Due to the normalization condition of
the Killing field , all 5D geodesics project down to Lorentz force motions on M4 with q/m
ratios that are too low when compared to the physical ratios for elementary particles [2,4].
So timelike or null 5D geodesics cannot describe the 4D motion of charged elementary
particles. One needs spacelike 5D geodesics [33].

    Our first point is that these difficulties are less acute in higher-dimensional models.
For example, for higher-dimensional K, after transforming the Lagrangian in (11.1) to
the Einstein frame, the local constancy of internal volume only implies that2

    P    2                                     +  RgK  -  2k   = 0,  (1.11)
M VolgK                                                   k+2
          gK (ea, eb) (FAa)� (FAb )�

where k denotes the dimension of K. So there is room for |FA|2 to vary, as long as
those changes are compensated by variations of the internal metric gK that change the
scalar curvature RgK without affecting the total volume. For example TT-deformations of

2This equation can be derived from the last equation in section 3.4 of [37] after expressing the normalized
 metric g�K of that section in terms of the plain, un-normalized metric gK.

         8
gK. Moreover, these constraints are derived solely from the Einstein-Hilbert action on P ,
which should not tell the whole story for realistic models operating at different scales [37].

    In section 11, we discuss the second difficulty, the small q/m ratios implied in 5D
geodesics. It is shown that, for higher-dimensional K, the normalization of the Killing
field no longer determines the value of gK(, ). Only the average value of that norm
over K. This makes the problem less acute, because that average can be significantly
different from the point value gK(, ) that appears in the geodesic equation. Moreover,
the usual normalization condition of  assumes that the background metric on P satisfies
the higher-dimensional Einstein equations. For different backgrounds, the normalization
condition of  can be less problematic.

    Another point discussed in section 11 is that, if the background metric satisfies the
Einstein equations on P , then its projection to M4 should not be identified with the
physical 4D metric, in general. Only with a rescaled version of it. This is related to
the well-known need to transform the dimensionally-reduced Lagrangian from the Jordan
frame to the Einstein frame. So one should be careful when studying geodesics on such
backgrounds. Different strategies to deal with this issue are discussed in that final section.

Conceptual simplicity

Kaluza-Klein models strive for conceptual unification at the classical level, before thinking
about quantization. Traditionally, they mainly deal with the unification of gauge fields and
the 4D metric as components of a unique, higher-dimensional metric. Both in abelian and
non-abelian gauge theories. It should also be possible to describe spontaneous symmetry
breaking as a dynamical process of the internal metric, in which the isometry group of gK
is broken to generate the gauge bosons' mass according to formula (1.4) [37].

    The main message of the present paper, in turn, is that conceptual unification can
be taken farther in simple, higher-dimensional models, hopefully without contradicting
observation. At the level of test particles and geodesic motion, one can construct a model
where massive and massless particles both travel at the speed of light in higher dimensions,
satisfying a photon-like energy-momentum relation that projects down to the usual 4D
relation on M4. A model where mass, charges, and 4D momentum describe different
aspects of a unique higher-dimensional momentum vector, which is covariantly conserved
along geodesics. A model where the energy stored in the 3D rest mass of classical particles
is simply the kinetic energy of internal motion.

    In this picture, the classical rest mass is not a constant attribute of a test particle. It
is a dynamical quantity measuring the internal component of the particle's momentum.
It can vary along geodesics if the background geometry is sufficiently distorted away from

                                                        9
the vacuum configuration, since this enables transfers between the horizontal and vertical
components of momentum. In particular, the geodesic model illustrates how a higher-
dimensional, classical theory can exhibit qualitative features (particle charge and mass
change) that are usually reserved for QFT calculations.

    The geodesic model also has clear limitations, of course. There is no quantization of
charge, mass or energy. Particles do not back-react on fields and their fermionic nature is
ignored. As in the case of GR, geodesics offer a very simplified picture of how a particle
interacts with fields. But that classical preview could be useful, nonetheless. A natural
heuristic picture may help to guide deeper studies of higher-dimensional models.

2 Motion in the vacuum and 4D inertial frames

To establish notation, we start by considering motion on P = M4 � K equipped with a
product metric gM + gK. Consider an inertial frame on M4 with coordinates (t, x1, x2, x3)
and write the Minkowski metric as

gM = dx1  dx1 + dx2  dx2 + dx3  dx3 - c2 dt  dt .                    (2.1)

Take arbitrary local coordinates yj on the internal space K. In an inertial frame related
by a boost with speed u along the x1-axis, the new coordinates satisfy the usual relations

dx1 = dx1 - u dt                        dt = dt - u dx1/c2
             1 - u2/c2                               1 - u2/c2

dxn = dxn for n = 2, 3                  dyj = dyj .                  (2.2)

All coordinates transversal to the boost remain invariant, including the internal ones.
A particle moving on M4 � K can be parameterized by a curve (s) = (M (s), K(s)).
Taking the derivative with respect to s, we have the tangent vectors

d   (s)                 =    =    M  +  K ,
ds

with M tangent to M4 and  K tangent to K. They satisfy the relation

gK( K,  K) - gP ( ,  ) = - gM ( M ,  M ) =   c  d    2               (2.3)
                                                ds
                                                       ,

where  denotes the particle's 4D proper time. Since gK is Riemannian by assumption,
the term gK( K,  K) is always non-negative. Thus, if  is a timelike curve on P , the
projection M will also be timelike on M4. If  is null on P , the projection M will
generically be timelike on M4, but can also be null when K is zero. In principle, even
some spacelike curves on P can project down to timelike curves on M4, if the norm

                             10
gK( K, K) is sufficiently large. We will not consider that possibility here. In a Kaluza-
Klein model the additional dimensions are interpreted to be physical as well, so they are

subject to the same causal restrictions as the Minkowski dimensions. So we will only

consider curves such that gP ( ,  ) is negative or zero.

A particle's velocity in the inertial frame (t, x1, x2, x3, yj) is the derivative of its position

with respect to the time coordinate. So the internal velocity of the test particle represented

by (s) is given by

                    vK  =     dK   =  ds dK   =           1    K  ,
                               dt     dt ds                0

which is a vector tangent to K at the point K(s). Similarly, the particle's 3D velocity in

the frame is                  dn          1                
                               dt xn       0              xn
                        v  =          =        n              ,

with an implicit sum over n = 1, 2, 3. The dot denotes derivation with respect to s.

    An affine geodesic on P is a curve (s) satisfying   = 0, where  denotes the
Levi-Civita connection of gP . When gP is a product metric, the projected curves M (s)
and K(s) are also geodesics on the respective spaces. For more general gP they are not.
Although the geodesic equation is defined here using the Levi-Civita connection of gP , any
connection with totally anti-symmetric torsion would lead to the same equation, hence to
the same geodesics on P .

3 Curves in Riemannian submersions

Take a Lorentzian metric gP on the higher-dimensional space P = M4 � K such that
the projection  : P  M4 is a Riemannian submersion. As in the usual Kaluza-Klein
framework, this metric determines three more familiar objects:

 i) through projection, a unique Lorentzian metric gM on M4;

ii) through restriction to the fibres {x} � K, a family of Riemannian metrics gK(x) on
     the internal spaces parameterized by the points in M4;

iii) gauge fields on spacetime, encapsulated in a one-form A on M4 with values in the
     Lie algebra of vector fields on K.

The equations linking these objects to the higher-dimensional metric gP are           (3.1)

                            gP (U, V ) = gK(U, V )
                           gP (X, V ) = - gK (A(X), V )
                           gP (X, Y ) = gM (X, Y ) + gK (A(X), A(Y )) ,

                                      11
for all tangent vectors X, Y  T M and vertical vectors U, V  T K. These relations
generalize the usual Kaluza ansatz for gP . They show how to reconstruct the higher-
dimensional metric from the data (gM , A, gK). The correspondence between submersive
metrics on P and that data is a bijection. This is described in more detail in [37].

Choosing a set {ea} of independent vector fields on K, the one-form on spacetime can

be decomposed as a sum

                               A(X) = a Aa(X) ea ,                  (3.2)

where the real-valued coefficients Aa(X) are the traditional gauge fields on M4. For general
submersive metrics on P this can be an infinite sum, with {ea} being a basis for the full

space of vector fields on K, which coincides with the Lie algebra of the diffeomorphism

group Diff(K). The curvature FA is a two-form on M4 with values in the Lie algebra of

vector fields on K. It can be defined by

FA(X, Y ) := (dM Aa)(X, Y ) ea + Aa(X) Ab(Y ) [ea, eb] ,

where the last term is just the Lie bracket [A(X), A(Y )] of vector fields on K.

    The tangent space to P = M4 � K has a natural decomposition T P = T M  T K.
Since T K is the kernel of the projection T P  T M, it is also called the vertical sub-
bundle V of T P . The higher-dimensional metric gP determines an orthogonal complement
H  (T K), called the horizontal sub-bundle. So from gP we get a second decomposition

                                 TP = HV .                          (3.3)

Every tangent vector E  T P can be written as a sum of components EH + EV . The rela-
tion between the two decompositions of T P is quite simple in a Riemannian submersion.
Writing E = EM + EK for the components according to T P = T M  T K, we have

EV = EK - A(EM )                                EH = EM + A(EM ) .  (3.4)

So the information contained in the gauge one-form A on M is equivalent to the inform-
ation contained in the horizontal distribution H  T P . Geometrically, it is well known
that the curvature FA is the obstruction to the integrability of the distribution H, in the
sense that it vanishes if and only if P can be foliated by horizontal submanifolds whose
tangent space coincides with H [13].

    Now let (s) be a curve on P parameterized by s. Let M (s) and K(s) denote its
projections onto the factors M4 and K. The tangent vectors to P obtained by derivation
with respect to s have two decompositions

                        d   =    =   M    +  K  =   V  +  H .       (3.5)
                        ds

                                          12
According to (3.4) these are related by

                          V =  K - Aa( M ) ea                                     (3.6)
                          H =  M + Aa( M ) ea .

Since gP restricted to horizontal vectors projects down to gM and the second decomposi-
tion is gP -orthogonal, we have that

- gM ( M ,  M ) = - gP ( H,  H) = gP ( V ,  V ) - gP ( ,  ) .                     (3.7)

The restriction of gP to vertical vectors is the Riemannian metric gK on the fibre. Hence,
the first term on the right-hand side is always non-negative. So is the second term when
(s) is a null or timelike curve on P . In that case, the projection M (s) is also a null
or timelike curve on M4. The particle's proper time on Minkowski space along the path
M (s) is measured by

c [ (s1) -  (s2)] =  s2  -gM (M ,  M ) ds =  s2  gK( V ,  V ) - gP ( ,  ) ds . (3.8)

                     s1                      s1

The last integral depends on gK and on the gauge fields, as is clear from (3.6).

4 Geodesics in Riemannian submersions

Equations of motion

This section describes the main mathematical results in the paper. Some readers may
wish to glance through the details in a first reading and only extract the main outputs,
such as formulae (4.3), (4.5), (4.6) and propositions 4.1 and 4.2.

    Let (s) be a general curve on P and let  denote the Levi-Civita connection on
T P associated with the metric gP . The covariant derivative   determines the parallel
transport of the tangent vector  along the path (s). When P = M4 � K and the metric
gP defines a Riemannian submersion, one can ask how   decomposes into horizontal
and vertical parts. Adapting the notation and using the properties of the tensors involved,
as in [37], classic results of O'Neill [12, corollary 1] imply that

gP   , V  = gP   V , V - gP SV  V ,  H                                            (4.1)
gP   , Z
          = gM M M  M , Z + FAa(Z,  M ) gP ea,  + gP S V  V , Z

for any curve (s) on P , any vertical vector V and any horizontal vector Z in T P . The first
equation determines the vertical component of   ; the second its horizontal part. The

                                         13
notation follows section 3 and [37, sec. 2]. It differs from the conventional notation in the
literature about Riemannian submersions since the latter clashes with established physics
notation (see the remark in appendix A). So we use the decomposition T P = H  V ;
the curvature FA is a two-form on M4 with values on the vector fields on K; the tensor
S : V �V  H is the second fundamental form of the fibres of the projection  : P  M4,
which can be idientified with the covariant derivative dAgK of (1.3) through formula (4.5);
the symbol M denotes the Levi-Civita connection on (M4, gM ). The covariant derivative
MM  M is a vector field along the curve M (s) on M4. It does not vanish in general, since
the projected curve M =    need not be a geodesic on the base (M4, gM ).

    Now let (s) be a geodesic curve on P satisfying   = 0. The first equation in (4.1)
implies that the norm of the vertical component  V evolves according to

d   gP      V ,  V     = 2 gP   V ,  V   = 2 gP S V  V ,  H .               (4.2)
ds

Using (3.7) and the fact that gP ( ,  ) is constant along a geodesic, this implies that

d          d   2          d              = 2 gP S V  V ,  H .
ds         ds             ds
        c           =  -      gM  M , M                                     (4.3)

So the norm on M4 of the tangent M may not be constant as the parameter s varies.
Note that the norm of the full tangent vector  is always preserved along the geodesic.
It is only the norm of the components  V and  H that may change, with opposite signs,
in regions where the tensor S is non-zero, i.e. in regions where the fibres of P are not
totally geodesic.

    Now consider the second equation in (4.1). If (s) is a geodesic on P , it implies that
the projected curve M =    on Minkowski space satisfies

gM MM  M , Z = - gP (ea,  ) FAa Z,  M - gP S V  V , Z                       (4.4)

for all horizontal vectors Z  T P . The restriction of gP to the fibres, denoted gK, is
a family of Riemannian metrics on K parameterized by the points in M4. The second
fundamental form S is equivalent to the covariant derivative of gK along vectors on M4,
as defined in (1.3). This follows from the identity

               (dAgK)Z(U, V ) = - 2 gP (SU V, Z) ,                          (4.5)

justified in [37, sec. 2]. Therefore, denoting by X the projection Z in T M and using
that ea is a vertical vector, the equation above can also be written as

gM MM  M , X        =  gK(ea,  V ) FAa( M , X)  +  1  (dAgK)X ( V  ,  V  )  (4.6)
                                                   2

for any X in T M. This equation generalizes the Lorentz force equation of motion to

regions of spacetime where S = 0, i.e. to regions where the internal metric gK is not

                                  14
covariantly constant as one moves along M4. It generalizes the equation derived by Kerner
when K is a Lie group and gK is a bi-invariant metric [29], and also the equations for
geodesic motion when K is a circle or a group manifold with variable size [1�3, 5, 8]. The
motion M (s) on M4 is coupled to the internal motion K(s) through the combination
 V = K - Aa( M ) ea, described in (3.6).

Horizontal geodesics

Equations (4.1) imply that a horizontal curve hor(s) on P , i.e. a curve whose tangent
has a vanishing component ( hor)V , satisfies the relation

gP  hor  hor, E       = gM  M           Mhor,  E
                                M hor

for every tangent vector E in T P . So the curve hor is a geodesic on P if and only if its
projection Mhor is a geodesic on M4. Thus, a direct consequence of (4.1) is that

Proposition 4.1 ( [12]). The horizontal geodesics on (P, gP ) are exactly the horizontal
lifts of geodesics on the base (M4, gM ).

    In particular, if the gauge fields Aa and the internal metrics gK change but the metric
gM on the base does not, then the horizontal geodesics will change as curves on P , but
their projection to M4 will remain identical.

    Now suppose that (s) is a causal (timelike or null) curve on P that projects down to a
null curve on M4. This means that the particle represented by  is moving at the speed of
light on Minkowski space. Using that gK( V ,  V ) and -gP ( ,  ) are both non-negative,
it follows from (3.7) that a zero gM ( M ,  M ) implies that those two terms must be zero
as well. In other words,  projects down to a null curve on M4 if and only if  itself is
horizontal and null on P . Thus, we conclude that particles moving at the speed of light
on M4 are always represented by horizontal, null geodesics on P . Combining this with
the previous observations about horizontal geodesics, we get that:

Physical implication. In a causal, higher-dimensional geodesic model, particles moving
at the speed of light on M4 are always represented by horizontal, null geodesics on P .
Their 4D motion is not affected by the configuration of gauge fields and internal metrics
on P . They follow the null geodesics on M4 determined by gM alone.

    This is not true for particles travelling at lower speeds on M4. In that case, the
corresponding geodesics on P can have a non-zero vertical component  V that, according

to (4.6), couples M (s) to the gauge fields and internal geometry through the tensors
FA and dAgK. As mentioned in the Introduction, this property of the geodesic model is

                      15
incompatible with the motion of the old massless neutrinos, since they were thought to
interact with the weak field and travel at the speed of light on Minkowski space. So a
causal, geodesic model on M4 �K disfavours the existence of massless neutrinos or similar
particles. This does not seem to have been remarked before.

Vertical Killing fields

In the next few paragraphs, we will study the conditions necessary for a Killing field of
gK to be a Killing field of gP  (gM , A, gK) as well. When this happens, we get additional
constants of the higher-dimensional, geodesic motion.

    Let (s) be a geodesic for gP and let V be a vertical vector field on P . In general,
the inner-product gP (V,  ) is not constant along the geodesic. Using lemma A.3 in the
appendix, its dependence on the parameter s is calculated to be

       2  d   gP (V,  )  =  2 gP   V,   = (LV gP )( ,  )                                       (4.7)
          ds

                         = (LV gP )  H,  H + 2 LV gP )( H,  V          + (LV gP )  V ,  V

                         = (LV gK)  V ,  V + 2 gK [ H, V ],  V

                         = (LV gK)  V ,  V + 2 gK dAM V,  V .

In the last equality, we used the Diff(K)-covariant derivative of a vertical field V on P
along a vector field X on M. Using the Lie bracket of vector fields on P , it is defined
through the expression

dXA V     :=  [XH, V ]   =  [X, V ]  +  [A(X), V ]  =  (dV  j  )(X  )      + Aa(X) [ea, V ] ,  (4.8)
                                                                       yj

where the yj are any coordinates on K. So dXA V is another vertical field on P . These
equalities use the fact that V is vertical; that the functions Aa(X) do not depend on the
coordinates yj; and that the Lie bracket [X, /yj] vanishes, since these are vector fields
on different manifolds. The covariant derivative dA is an interesting object of study. As
in [37, sec. 2.5], one can check that it is C(M)-linear in both entries and is equivariant
with respect to Diff(K)-gauge transformations of V and the gauge one-form A.

    Now, at a fixed point on P there are geodesics passing through with arbitrary vectors
 V and M . So formula (4.7) implies the equivalence of conditions 2 and 3 below.

Proposition 4.2. Let V be a vertical vector field on P and let gP  (gM , A, gK) be a
submersive metric. Then the following conditions are equivalent:

1. V is a Killing vector field of the higher-dimensional metric gP ;
                                                    16
2. The restriction of V to each fibre is Killing and dAX V vanishes for all X  T M;
3. The inner-products gP (V,  ) are constant for all geodesics (s) on P .
The equivalence of conditions 1 and 2 follows from lemma A.3 in the appendix.

5 Constants of motion among massless gauge fields

Simplified geodesic equation

The aim of this section is to identify constants of geodesic motion in certain regions of
spacetime, namely, regions where the Higgs-like scalars are constant and where all massive
gauge fields vanish. In the physical world, this would allow an electromagnetic field but
would exclude a non-zero weak field, for example. Under these conditions, the classical
mass and charge of physical particles are constant. So the definitions of mass and charge
adopted in the geodesic model should be searched among quantities that are constants of
motion in these regions.

    Consider a higher-dimensional submersive metric characterized by the equivalent data
gP  (gM , A, gK), as before. In this section, we will assume :

H1) The internal metrics gK are the same for all fibres;
H2) The one-form A(X) has values in the space of Killing vector fields on (K, gK).

According to [37] and the mass formula (1.4), these assumptions correspond to regions of
M4 where the Higgs-like scalars are constant and only massless gauge fields are present.
In particular, the second fundamental form of the fibres (denoted S in section 4), which
is equivalent to the covariant derivative dAgK of (1.3), vanishes. With these assumptions,
the equations of section 4 for higher-dimensional geodesics simplify considerably.

    For example, since the norm gP ( ,  ) is always a constant of geodesic motion, equa-
tions (3.7) and (4.2) imply that, for geodesics,

d                      d   2        d                     d        V ,  V
ds                     ds           ds                    ds
    c                         =  -      gM ( M ,  M )  =      gP            =0.           (5.1)

So, in these regions,  the rate of change of proper time,     d   ,  is  a  constant  of  motion.  In
                                                              ds

section 6 we will relate it to the mass of the test particle. Moreover, since dAgK vanishes

and  is a geodesic by assumption, the two equations in (4.1) are simplified to

                          gP (  V , V ) = 0                                               (5.2)
                       gM MM  M , X = gP (ea,  ) FAa( M , X) .

                                        17
Here V is any vertical vector in T P and X is any vector in T M. The first equation
describes the vertical component  V of the tangent  . It says that, although the vectors
 V are not parallelly transported along the geodesic, as the  are, at least the vertical part
of the covariant derivative   V vanishes. The second equation says that the projection
of the geodesic to M4 is a curve M (s) satisfying something similar to a Lorentz force
law [41, sec. 4.3], but with more gauge fields involved. It reduces to the equation derived
by Kerner when K is a Lie group and gK is a bi-invariant metric [29]. The inner-products
gP (ea,  ) play the role of "charges", coupling the 4D motion M (s) to the curvature FAa
of the background gauge fields. The next few paragraphs will investigate the extent to
which these inner-products are constant along the geodesics, so that (5.2) truly resembles
a Lorentz force equation of motion.

Constants of geodesic motion

Consider a general geodesic (s) on the higher-dimensional P . As usual, if Z is a Killing
vector field with respect to gP , we have that

d   gP ( ,  Z)  |(s)  =       gP (  , Z)  +  gP ( ,  Z)      =  0.
ds

So the inner-product gP ( , Z) is constant along the geodesic (s).

    For a simple product metric, gP = gM + gK, the Killing fields of gP are sums of Killing
fields of gM and gK. So all the Killing fields of gK determine constants of geodesic motion,
besides those determined by the isometries of M4. However, these additional constants
cannot be perceived from the 4D projection of motion. A product metric has vanishing
gauge fields and constant internal geometry, so the second relation in (5.2) says that M
is a pure geodesic of gM , uncoupled to the internal metric and to internal motion.

    When the gauge fields are non-zero, some of the Killing fields of gK may no longer
preserve the higher-dimensional metric gP  (gM , A, gK) on M4 �K. So the description of
the constants of motion becomes less straightforward. It is still simple enough, however,
if we assume that gP satisfies conditions H1 and H2. Let us start by describing how the
general formulae of section 4 are simplified under H1.

Lemma 5.1. Let gP  (gM , A, gK) be a submersive metric on P satisfying assumption
H1. Let (s) be a geodesic of gP . If V is a Killing field of gK, we have that

    d       gP (V,     )      =  Aa( M ) gP ([ea, V ],  ) .         (5.3)
    ds

Proof. Assumption H1 says that the internal metric is the same for all fibres. So if V is
a Killing field of gK, the term with LV gK vanishes in (4.7). Moreover, if we regard V as

                                 18
a vector field on M4 � K that is constant along the M4 direction, the Lie bracket [X, V ]
vanishes for arbitrary vector fields X on M4. This simplifies (4.8). The result follows
from the combination of the simplified forms of (4.7) and (4.8).

    Now, according to assumption H2, the gauge one-form A(X) has values on the space of
Killing fields of gK. So when V commutes with all other Killing fields on K, formula (5.3)
implies that gP (V,  ) has vanishing derivative with respect to the geodesic parameter s.
Using the equivalence relations in proposition 4.2, we conclude that:

Lemma 5.2. Let gP  (gM , A, gK) be a submersive metric on P satisfying assumptions
H1 and H2. Let  be a Killing vector field on (K, gK) that commutes with all other Killing
fields of gK. Then  is also a Killing field on (P, gP ) and the inner-product gP (,  ) is a
constant of motion for every geodesic  on P .

    If the vector field  does not commute with all other Killing fields of gK, then, in
general,  will not be Killing for gP . However, it is still possible to extract a constant of
motion from the subalgebra of the Killing algebra that contains . To see how this comes
about, we must describe the Killing algebra of gK in more detail.

    Since K is a compact manifold by assumption, the isometry group of gK is a finite-
dimensional, compact Lie group. The corresponding Lie algebra can be identified with
the algebra k of Killing vector fields on K. It admits a decomposition of the form

k = a1  � � �  am ,  (5.4)

where the ar are either u(1) lines or simple, non-abelian Lie algebras. To describe the
constants of motion associated to the summands, let {r,b : 1  b  dim ar} denote a
basis of ar. Each r,b is a Killing field of gK. Since K is compact, it is possible to choose
the basis so that its elements are L2-orthonormal on (K, gK) and the structure constants
defined by [r,b, r,c] = (fr)dbc r,d are totally anti-symmetric in their three indices (see
lemma A.6). With this choice, we can consider the scalar function

b [ gP (r,b,  ) ]2   (5.5)

associated to the Lie subalgebra ar and the curve (s) on P . Later, in section 8, we will
call it the squared ar-charge of the particle represented by , up to a constant factor. This
function is independent of the choice of basis {r,b} because, by assumption, this is a L2-
orthonormal basis of ar. And all such bases are related to each other by linear orthonormal
transformations, which preserve the sum of squares (5.5). With these definitions, we have
the following result.

19
Proposition 5.3. Let gP  (gM , A, gK) be a submersive metric on P satisfying assump-
tions H1 and H2. For each subalgebra ar of the Killing algebra of gK, the scalar (5.5) is
a constant of motion for every geodesic (s) on P .

Proof. To justify the assertion, observe that formula (5.3) implies that

d   [ gP (r,b,  ) ]2  =  2 gP (r,b,  )  d   gP (r,b,  )  =  2 gP (r,b,  ) gP ([A( M ), r,b],  ) .
ds                                      ds

By assumption H2, the contraction A(M ) is a Killing vector field on K, so a vector
in the Killing algebra (5.4). Its component in the subspace ar to which r,b belongs is
just c Ac( M ) r,c. Since (5.4) is a Lie algebra decomposition, not just a vector space
decomposition, this component is the only one that matters when calculating the bracket
[A( M ), r,b]. All other components commute with r,b. So we have that

        [A( M ), r,b] =     Ac( M ) [r,c, r,b] =                 Ac( M ) (fr)cdb r,d .

                         c                                  c,d

Thus, we finally get that the derivative is

    d      [ gP (r,b,  ) ]2 = 2             gP (r,b,  ) Ac( M ) (fr)cdb gP (r,d,  ) = 0 ,
    ds
        b                        b,c,d

where the last equality follows from the anti-symmetry of the structure constants fr in
the indices b and d.

    This proposition gives us constants of geodesic motion in regions of spacetime where
all gauge fields are massless and the internal metric is constant. However, inspecting the
calculation in the proof, one quickly realizes that some of the original assumptions may
be relaxed. We can drop H2 and accept non-zero massive gauge fields as long as those
fields commute with the Killing fields of gK. More precisely, the previous proposition can
be generalized by a similar calculation to the following result.

Proposition 5.4. Let gP  (gM , A, gK) be a submersive metric on P satisfying assump-
tion H1. Suppose that the gauge one-form A(X) has values in a subspace of vector fields
on K of the form ar  h with the commutation relation [ar, h] = 0. Then the scalar (5.5)
is a constant of motion for every geodesic (s) on P .

    The difference between the two propositions can be illustrated in the case where K = G
is a compact, simple Lie group and gK is a generic left-invariant metric. For more details
about these metrics, see [37, 42], for example. The Killing algebra of gK is the space
of right-invariant vector fields on G, denoted gR. If {b} is a basis of Lie(G) that is
orthonormal with respect to the Killing form, then its right-invariant extension to G,

                                             20
{bR}, is a basis of gR with totally anti-symmetric structure constants. The left-invariant
vector fields on G are not Killing, but their Lie bracket with the right-invariant fields does
vanish. So we are in the conditions of Proposition 5.4, with ar = gR and h = gL. This
means that the scalar b [ gP (bR,  ) ]2 will be a constant of motion even in the presence
of the massive gauge fields associated to the left-invariant vector fields on K.

    A similar example shows that these constants of geodesic motion are not necessarily
all independent of each other. To this end, still take K to be a compact, simple Lie group,
but now let gK be a bi-invariant metric. Then the Killing algebra of gK is the sum of the
spaces of left-invariant and right-invariant vector fields, gL gR. If {b} is a basis of Lie(G)
orthonormal with respect to the Killing form, then its left-invariant extension, denoted
{bL}, is a basis of gL with totally anti-symmetric structure constants. Moreover, at every
point of G, the vector fields bL are gK-orthogonal to each other and span the tangent space
to the point. Similarly for the right-invariant extensions {bR}. Then it is straightforward
to check that the two constants of geodesic motion associated by proposition 5.3 to the
summands gL and gR coincide with each other for all geodesics. Both are equal to the
norm gK( V ,  V ), up to a constant factor.

6 Higher-dimensional momentum and mass

After the mostly geometrical content of sections 4 and 5, in this section we come back
to physics. The motion of test particles on the higher-dimensional space P is parameter-
ized by timelike or null geodesics. Let (s) be such a geodesic. The higher-dimensional
momentum vector of the associated particle is the vector tangent to P defined simply by

p(s)  :=    d   =    (s) .                                (6.1)
            ds

Here  is a positive constant with dimension MT-1. Since  is geodesic, the momentum

vectors are covariantly constant along the curve,  p = 0. The higher-dimensional

momentum vector can be decomposed in two different ways:

p(s) = pH + pV = pM + pK .                                (6.2)

As in (3.5) and (3.6), writing the curve (s) on M4 � K as ( M (s), K(s) ), the different
components of momentum are given by

pM =  M                                                   (6.3)
pK =  K
pH =   H = pM + Aa(pM ) ea
pV =   V = pK - Aa(pM ) ea .

            21
For each value of s the vectors pM and pK can be regarded as tangent to M4 and K, but
they are not gP -orthogonal to each other. The vectors pH and pV are orthogonal on P ,
but they depend on the gauge fields and mix the components along M4 and K.

   Since  is timelike or null, by (3.7) the same is true for its projection M to M4. So

gM ( M ,  M ) is non-positive. The particle's 4D proper time  is defined, up to an additive

constant, by                                   d
                                               ds
                                           c        =        - gM ( M ,  M ) .                       (6.4)

When this derivative is non-zero,  can also be used as a parameter for the curve. Then

the higher-dimensional momentum vector can be written as

                                                   p(s)  =   m(s)   d   ,                            (6.5)
                                                                    d

where we have defined the particle's rest mass function

      m(s)    :=        d     =     1      -gM (pM , pM )        =  1   gP (pV , pV ) - gP (p, p) .  (6.6)
                        ds          c                               c

The last equality uses (3.7). The mass function is independent of the 4D frame because it

is defined in terms of proper time. It is positive for all geodesics on P that project down

to timelike curves M (s) on M4. It vanishes only when (s) projects to a null curve on

M4. Combining (6.5) with formula (6.3) for the momentum components, it is clear that

in 4D we have                                                       dM
                                                                     d
                                               pM        =   m(s)       .

Thus, as long as pM is identified with the particle's 4-momentum on M4, this relation im-

plies that m(s) is the particle's mass. In particular, given inertial coordinates (t, x1, x2, x3)

on M4, the energy E and 3-momentum p of the particle parameterized by (s) should be
read from the projection pM through the usual (coordinate-dependent) relation3

                        pM          =  E       +    p1           +  p2      +      p3          .     (6.7)
                                       c2 t                 x1          x2             x3

    Now consider the case where  projects down to a null curve on M4. By the discussion
below proposition 4.1,  itself must be a horizontal, null curve on P . Then relation
(6.4) says that d /ds vanishes, and hence proper time cannot be used to parameterize
M (s) = (0(s), n(s)). In this case, the relation between momentum and mass expressed
in (6.5) is no longer valid, but the original definitions in (6.3) still are. Assuming that the
derivative  0 does not vanish, the projected momentum pM can be written as

                        pM    =        dM      =         dt  dM     =   0              +    v     ,  (6.8)
                                        ds               ds   dt                   t

3The energy of the particle measured by an observer at rest in the frame determined by (t, x1, x2, x3) is

E  =  - gM (pM ,     )  [41,  sec.  4.3].  So  for  the  Minkowski  metric  (2.1)  we  get  (6.7).
                  t

                                                             22
with |v| = c because M (s) is null on M4. Thus, to keep (6.7) valid, we must relate the

(massless) particle's energy and 3-momentum to the components of pM through

E   =       0                pn  =    0 vn    =    dt  dn   =    n .         (6.9)
c2                                                 ds   dt

In particular, using Einstein's relation for photons, the frequency associated to the mass-

less particle represented by the null curve M (s), in the frame (t, x1, x2, x3), is just
 =  c2  0 / h.

    Observe that, in this picture, there is no physical freedom to reparameterize affine
geodesics on P . More precisely, if ~(s) := ( s) is a reparameterization of  by a positive
constant, then ~(s) is still a geodesic on P , of course, but it now represents the motion of
a test particle with a different higher-dimensional momentum. Evaluating the momentum
at the point ~(s) in P , we have

p~ |~(s)  =    d~  |~(s)  =        d   |( s)  =   p |( s)   =  p |~(s) .
               ds                  ds

So p~ =  p as vector fields over the locus on P of the curve. Also, at the point q = ~(s),
the masses of the particles represented by ~ and , as written in (6.6), are related to each
other by

m~ 2 |q = - c-2 gP p~H, p~H |q = - c-2 2 gP pH, pH |q = 2 m2 |q .

So ~ and  parameterize the motion on P of different physical particles. In the case where
~ and  are horizontal geodesics, both m~ and m vanish, of course. But a similar argument
implies that the 4-momenta on M4 of the respective particles are related by

                          p~M |(q) =  pM |(q) .

Hence, the two geodesics describe the motion of two massless particles with different
energies in the frame (t, x1, x2, x3).

7 Rest mass variation

This section studies one of the most interesting features of Kaluza-Klein models: the
possibility of rest mass variation of a test particle in free fall along a higher-dimensional
geodesic. According to (4.3), the scalar m(s) defined in (6.6) is a constant of motion
when the geodesic traverses regions in P with totally geodesic fibres, i.e. regions where
S = dAgK = 0. In those regions, the geodesic parameterizes the motion of a test particle
with fixed rest mass. In regions where the internal metric gK is not covariantly constant,
the same formula (4.3) implies that the mass function can vary according to

c2  d     m2(s)    =  2 gP   SpV pV ,  H      = - (dAgK)M (pV , pV ) .       (7.1)
    ds

                                    23
The last equality uses (4.5). At the same time, identity (3.7) says that the different
components of the momentum vector defined in (6.3) are related by

            - gM (pM , pM ) = - gP (pH, pH) = gP (pV , pV ) - gP (p, p) .     (7.2)

Since norm of the full momentum gP (p, p) is a constant of geodesic motion, it follows from

(6.6) that

            d   gP (pV  ,  pV  )  =  -  d   gP (pH, pH)  =  c2  d   m2(s)  .  (7.3)
            ds                          ds                      ds

So the norms of the horizontal and vertical components of momentum may change with

opposite signs along the motion, while the norm of the full momentum p remains con-

stant. The picture is that, in regions with non-vanishing dAgK, the higher-dimensional
geometry is distorted, so forces a transfer between the horizontal and vertical components

of momentum of particles in free fall along geodesics. Since the norm of the horizontal

momentum corresponds in 4D to the particle's rest mass, in those regions we observe a

phenomenon of rest mass variation.

    For example, suppose that for s < s1 a geodesic (s) traverses a region of P with
vanishing tensor dAgK; after that, it enters a region where massive gauge fields are present
and the internal scalars are not constant; then, for s > s2 it comes out into another region
with vanishing dAgK. The test particle parameterized by this geodesic has a well-defined
and constant mass inside the first and third regions. Those two masses may not coincide,
because the geodesic traversed a region with changing internal geometry, which is able
to transfer between vertical momentum and horizontal momentum. The classical mass
change in the overall process is given by

            m2(s2)  -      m2(s1)    =  -   1    s2
                                            c2
                                                s1 (dAgK )M (pV , pV ) ds .

Qualitatively, this property of geodesics agrees with the physical fact that in regions where
massive gauge fields are present, or where massive scalar fields (such as the Higgs field)
are non-constant, particles may interact with the respective massive bosons and undergo
a process of mass change. Of course, in this case, we would not call the incoming and
outgoing objects the same particle anymore, since, by convention, particles with different
rest masses are called different names.

8 Charges and charge variation

After mass, we consider charge. Let  be a Killing vector field on (K, gK) that commutes
with all other Killing fields of gK. Let (s) be a geodesic on P parameterizing the motion

                                            24
of a test particle with momentum p =   . We define the particle's charge with respect

to  to be the scalar

                      q(s) := - gP (, p) = - gK(, pV ) .                    (8.1)

So q(s) measures the component of the particle's momentum along the vertical Killing
field . According to lemma 5.2, this scalar is a constant of motion when the geodesic
traverses regions of P that satisfy conditions H1 and H2. Just like the particle's mass
m(s). Now suppose that in those regions the gauge form has values in the span of , i.e.
suppose that we can write A(X) = A(X)  for all X tangent to M4. Then formula (5.2)
says that the projection to M4 of the geodesic (s) satisfies

                      gM MM  M , Y            =  1   q (s)  FA  Y, M  .


But by definition of m(s) we have

                           M        =   dM       =   m(s)   dM  .
                                         ds                  d

Thus, in terms of the 4-velocity dM /d on Minkowski space, we get

                      gM  M         dM  ,  Y     =   q  FA  Y,  dM       .  (8.2)
                               dM    d               m           d
                                 d

So the projection to M4 of the particle's motion satisfies a Lorentz force equation [41, sec.
4.3], as long as we identify the scalar q(s) with the particle's charge. This calculation
justifies that interpretation of the conserved scalar. It is very familiar from 5D Kaluza-
Klein [1, 2, 4, 23, 43]. So when the electromagnetic field is the only gauge field present,
higher-dimensional Kaluza-Klein is similar to the 5D version. It is not quite the same
though, and this can be used to mitigate some of the traditional difficulties of the 5D
setting, as will be discussed in section 11.

A curious consequence of the definitions of charge and mass of a test particle is that

|q|2 = |gK(, pV )|2  gK (, ) gK(pV , pV )  gK(, ) m2 c2 .                   (8.3)

The last inequality uses (6.6) and the fact that gP (p, p) is non-positive for any timelike
or null geodesic on P . Therefore, in this geodesic model, test particles with a given
classical mass at a point (s) cannot have arbitrarily strong charge. There is a maximum
limit determined by the norm of the Killing field at that point. The inequality above
is saturated only when the particle's momentum p is null and, additionally, its vertical
component is proportional to  at the point.

    Now suppose that condition H1 of section 5 is satisfied but condition H2 is not. In
other words, we are in a region of P where the internal metrics gK are constant but there

                                                 25
are both massive and massless gauge fields present. Let  denote the same Killing field of
gK as before. It is a direct consequence of lemma 5.1 and definition (8.1) that the charge
of the test particle represented by a geodesic (s) will evolve according to

d   q (s)  =  -  d   gP (, p)  =  Aa( M ) gP ([, ea], p) .  (8.4)
ds               ds

Now, by assumption,  is an electromagnetic-like internal Killing field, i.e. it is a Killing
field that commutes with all other Killing fields of gK. So if only massless gauge fields are
non-zero, the corresponding Lie brackets [, ea] will vanish on K, and charge is conserved.
This is the content of lemma 5.2 of course. If there are massive gauge fields around, but
the corresponding internal fields ea are such that [, ea] = 0, then charge is still conserved.
This is a special case of proposition 5.4. However, if we are in a region of spacetime with
non-zero massive gauge fields Aa such that [, ea] does not vanish, then the charge q(s)
may no longer be a constant of geodesic motion. It will indeed vary if the particle's
internal momentum pV is not orthogonal to [, ea] in the tangent space to K.

    These properties of geodesic motion agree with the physical fact that gauge interactions
mediated by massive bosons will preserve a particle's charge if the bosons are neutral (i.e.
if [, ea] vanishes). This is illustrated by the Z boson of the Standard Model. But the
interactions will not preserve the particle's charge if the gauge bosons are charged (i.e.
if [, ea] is non-zero), as in the case of the two W bosons. So there is a natural physical
interpretation of the phenomenon of geodesic charge variation described by (8.4).

    The fact that 4D electromagnetic charge may vary along a geodesic in higher dimen-
sions, as in (8.4), apparently has not been reported before. That may be related to the
fact that massive gauge fields are usually discarded in the Kaluza-Klein literature, after
the quick remark that their bosons will have masses in the Planck scale. This remark is
not fully justified, in the author's view, having in mind the mass formula (1.4) (see the
discussion in [37]). For point particles, the general relations between mass, charges, and
the direction of internal motion also do not seem to be entirely clear in the literature.
That may be related to the fact that, in the thoroughly studied 5D setting, with its
unidimensional internal space, it is not possible to distinguish between the direction of
internal motion and the direction of the internal Killing vector field.

    As in section 5, under assumption H1 of a constant internal metric, it is possible to
define a scalar function associated with the path (s) and each summand ar in decom-
position (5.4) of the Killing algebra of gK. To define it, let {r,b} be a set of Killing fields
forming an L2-orthonormal basis of ar. Using that the higher-dimensional momentum
vector is p(s) =  , we write

           a2r,(s) :=                            2          (8.5)

                       b gP (r,b, p) .

                       26
We call this function the (squared) ar-charge of the particle represented by the curve .
It measures how orthogonal the particle's momentum vector is to the subspace of T(s)P
spanned by the Killing fields in the summand ar. It is a constant of geodesic motion if
only massless gauge fields are present, as shown in proposition 5.3. When massive gauge
fields are non-zero, the scalar evolves along a geodesic (s) according to

d   a2r , (s)  =  2  b gP (r,b, p) gP [A( M ), r,b], p .  (8.6)
ds

The derivation of this formula is similar to that of (8.4). It is justified in the proof of
proposition 5.4. As shown in proposition 5.3, after the decomposition A = a Aa ea of
the gauge form on M4, the massless components Aa do not contribute to the right-hand
side of (8.6). Only massive gauge fields do. Moreover, a massive gauge field Aa such
that the associated internal vector field satisfies [ea, v] = 0 for all v  ar, will also not
contribute to the right-hand side of (8.6). This is the content of proposition 5.4, of course.
By analogy with the electromagnetic case, it can be called a ar-neutral gauge field. A
gauge field that does not satisfy the commutation condition can be called a ar-charged
field. Then, by definition of decomposition (5.4), all massless gauge fields are ar-neutral
except those with values in ar itself. Those will be ar-charged (resp. ar-neutral) when ar
is a non-abelian (resp. an abelian) subalgebra of the Killing algebra of K. Massive gauge
fields on M4, in turn, will generically be ar-charged, but some can be ar-neutral.

    To end this section, we note that the charge variation described by (8.4) and (8.6) is
different from the rotation of non-abelian isospin along a geodesic, found by Kerner and
Wong in [29, 38] and reviewed in [39], for example. The rotation of isospin was derived
in the conditions of constant internal metric gK and massless gauge fields. It is trivial
for abelian charges. In contrast, the charge variation described by (8.4) and (8.6) is due
to massive gauge fields and is non-trivial for abelian charges. The relation between the
two effects can be summarized by saying that the constants of motion of isospin rotation
become variable quantities when massive gauge fields are introduced in the picture. Then
(8.6) describes the variation along a geodesic of those former constants of motion.

9 A unique speed in higher dimensions

Kaluza-Klein models strive for conceptual simplicity at the classical level, before thinking
about quantization. Following this motto, in this section we remark the naturalness of the
hypothesis that all elementary particles travel at the speed of light in higher dimensions.
It is the projection of velocities to three dimensions that appears to produce speeds in the
range [0, c], as observed macroscopically. Under this assumption, the previous geodesic
model is simplified, as we will see. Both massless and massive particles satisfy a photon-

                                                       27
like energy-momentum relation in higher dimensions, which projects down to the usual
energy-momentum relation in 4D. The energy stored in 3D rest mass of classical particles
becomes entirely due to the kinetic energy of internal motion.

    Let us then assume that test particles always follow null geodesics on P . In a Rieman-
nian submersion, we know that tangent vectors to a null path (s) satisfy

- gM ( M , M ) = - gP ( H,  H) = gP ( V ,  V ) .                                 (9.1)

This is just a simplification of (3.7). Since  V is tangent to the fibres and the restrictions
of gP to those fibres are the Riemannian metrics gK, the right-hand side is always non-
negative. It is zero only if  V vanishes. So the four-dimensional projection M (s) of
the null path is timelike on M4 when  has a vertical component and is null when  is
completely horizontal. The projection of a null path on P can never be spacelike on M4.
Thus, higher-dimensional null paths on P can describe all types of causal motion on M4
and never correspond to acausal ones. In the name of simplicity, it is natural to investigate
the consistency of a dynamical model entirely based on higher-dimensional null paths.

    From (3.8), the 4D proper time of a particle moving along a null curve on P satisfies
the simplified relation

c [ (s1) -  (s2)] =      s2

                     s1      gK( V ,  V ) ds .

When there are no gauge fields around, we have  V = K and proper time is just a
measure of the Riemannian distance travelled by the particle in the internal space.

Regarding mass, for a null path in higher dimensions, relation (6.6) reduces to

m(s) = c-1 gP (pV , pV ) .                                                       (9.2)

So the test particle's rest mass is simply the norm of its vertical momentum. Internal
motion is the sole source of rest energy. Mass vanishes for particles travelling along
horizontal, null paths on P , which of course also project down to null paths on M4. So
mass vanishes if and only if the particle has speed c on Minkowski space. Rest mass will
vary if there is a transfer between the horizontal and vertical components of momentum.
This can happen when the geometry of P is sufficiently distorted in comparison to the
vacuum geometry gM + gK. More precisely, when dAgK does not vanish, as described
in section 7. The total momentum p(s) is always covariantly conserved along a higher-
dimensional geodesic.

    For a null curve on P , relation (9.1) implies that the momentum components satisfy

- gM (pM , pM ) = - gP (pH, pH) = gP (pV , pV ) = c2 m2 .                        (9.3)

                     28
So the horizontal and vertical momenta have the same norm but opposite signs. This
follows from the vanishing of gP (p, p), of course. Now suppose that gM is the Minkowski
metric (2.1), choose coordinates (t, x1, x2, x3) on M4 and decompose the 4-momentum as

pM  =  E      +                                        p,
       c2  t

as in (6.7). Then the momentum relation (9.3) can be rewritten as the 4D relation

E2 = c2 |p|2 + m2 c4 ,

or, alternatively, as the higher-dimensional relation

E2 = c2 gP pH + pV , pH + pV .                                                     (9.4)

The former is the usual 4D energy-momentum relation. The latter is similar to the energy-
momentum relation of photons, but in higher dimensions. This is not surprising, because
we are assuming that test particles follow null paths on P , just as photons do in 4D.

    Dividing equation (9.4) by ( c  0)2 and using (6.8) and (6.9), we obtain the relation
for velocities in the chosen frame,

c2 = gP vH + vV , vH + vV = gM (v, v) + gK vV , vV .                               (9.5)

Thus, for non-trivial, null geodesics on P , the norm of the velocity vector in R3 � K
is always c. Test particles always travel at the speed of light in higher dimensions, as
expected. The projection of velocities to three dimensions is the sole reason for the
appearance of speeds in the range [0, c].

    A final remark now. Since the very beginnings of Kaluza-Klein, it has been well known
that null geodesics in higher dimensions can describe the 4D motion of massive particles.
However, in the traditional 5D model, it is not tenable to advocate that all elementary
particles move along null geodesics on M4 � S1. Even forgetting about the strong and
weak forces. This is because the null geodesics of a 5D metric with circle isometry cannot
reproduce all the combinations of mass and electromagnetic charge observed in elementary
particles. For example, null geodesics in 5D cannot naturally describe particles with zero
charge and non-zero mass, such as neutrinos. Or the existence of particles with the same
charge but different masses moving on a common background 5D metric. In fact, when
the internal space is unidimensional, mass and charge are proportional to each other for
particles following null geodesics. This is a consequence of (9.2) and (8.1). For this reason,
in the 5D model, it is desirable to keep timelike geodesics on M4 � S1 as representations
of physical motions. The norm of the tangent to a timelike geodesic is a useful free
parameter to adjust the rest mass of a particle without affecting its charge. In a geodesic

       29
model with a higher-dimensional K, however, the situation is very different. Now we can
have arbitrary angles between the direction of internal motion and the electromagnetic
Killing field on K. So (9.2) and (8.1) imply that the mass and charge of a particle following
a null geodesic become independent quantities, except for inequality (8.3). Thus, for a
higher-dimensional K, it does not seem necessary to use timelike geodesics on M4 � K
to model the masses and (abelian or non-abelian) charges of different particles. Null
geodesics seem to suffice. The exclusive use of null geodesics in higher dimensions also
fits better with the commonly stated aim of representing fermions by solutions of a single,
massless, Dirac-like equation for higher-dimensional spinors.

10 Parameterizing the space of null geodesics

Motivated by the model described in the last section, we will now have a closer look at
null geodesics on P . Denote by Nh the space of non-trivial, null geodesics (s) passing
through a point h in P at the parameter value s = 0. The trivial geodesic we are excluding
is the one with image h for all s. Standard properties of the geodesic equation say that
Nh can be parameterized by the non-zero, null vectors  (0) in the tangent space ThP .
Each of these vectors is parallelly transported along the geodesic it determines, so if  is
non-zero and null at s = 0, it will have the same properties for every value of s.

    Now pick a local coordinate system (t, xn, yj) on M4 � K, where the xn and yj are the
coordinates in R3 and K, respectively. Write the geodesic as

      (s) = M (s), K(s) = 0(s), n(s), j(s) .

Since  (s) is null and non-zero, the time component  0(s) must be non-zero for all s. In
particular, it is always positive or always negative. So the function s  0(s) is strictly
monotonous. According to the sign of  0 we can divide the space of geodesics Nh into
its components Nh+ and Nh-, corresponding to particles moving forward and backward in
time, respectively.

    Each of these components is isomorphic to R3+k \{0}, where k denotes the dimension
of K. For example, thinking of Nh+ as a subset of ThP , there is a bijection

1 : R3+k \{0} - Nh+                           (u1, u2, u3, wj) - (uH, w) ,  (10.1)

where we have defined

u :=  3                un                        w :=  j  wj   
      n=1                  xn                                 yj

u := u + c-1               |u|2  +  gK(w, w)                                (10.2)
                                              t

                                    30
and the horizontal lift uH is taken according to (3.4). By construction, 1(u, w) is always
a non-zero, null vector in ThP .

    The bijection 1 parameterizes all the null geodesics starting at h and moving forward
in time. These represent the motion on P of particles with different masses. Fixing
the mass of the particle means restricting to a subset Nh+(m) of the full space Nh+.
According to (6.6), after the simplification gP (p, p) = 0, the mass of a particle at h is
just c-1 gP (pV , pV ). So it essentially corresponds to the norm of the vertical vector
w in (10.2). Thus, under the bijection 1, the space of null geodesics at h of mass m
corresponds to the subset

Nh+(m)  (u1, u2, u3, wj)  R3+k \{0} : (gK |h)ij wiwj = -2 c2 m2  (10.3)

of the full R3+k \{0}. Topologically, it is clear that Nh+(m) is isomorphic to R3 � Sk-1
for non-zero m and to R3 \{0} for vanishing mass.

    When the internal metric gK has isometries in the region around the point h, we can
also consider the space of null geodesics representing particles with given charges, besides
a given mass. For example, one can consider the subset Nh+(q)  Nh+ representing
particles with electromagnetic charge q with respect to a Killing field  of gK. The
charge condition (8.1) imposes the constraint

                       (gK |h)ij i wj = - -1 q                   (10.4)

on the coordinates wj of R3+k \{0}. So the subspaces Nh+(q) are isomorphic to R2+k \{0}.

    Fixing mass and electromagnetic charge simultaneously defines the smaller subspaces
Nh+(m, q) = Nh+(m)  Nh+(q) inside the space of null geodesics Nh+. Adding the mass
condition in (10.3) to the charge condition (10.4), it is clear that these spaces are iso-

morphic to


                                    if |q| > m c ||
                                    if |q| = m c ||
                                    if |q| < m c || .


            Nh+(m, q)                                            (10.5)

                           R3


                         R3 � Sk-2

Here || denotes the Riemannian length (gK)h(, ) of the Killing vector field at the
point h. The upper bound for the charge of a test particle at the point h, given the value
of its mass, is of course the same as in formula (8.3) of section 8.

    The higher-dimensional momenta of particles with the strongest possible charge, |q| =
m c ||, have fewer degrees of freedom. This happens because the vertical component of
momentum must be completely aligned with . Hence, the motion of a particle of max-
imum charge is completely determined by an initial point in P and by the 3D momentum
vector at that point. For particles with weaker charges, the situation is different. One

                               31
also needs to choose the components of the vertical momentum at the initial point, and
there is a Sk-2 of possible choices compatible with the mass and charge of the particle.

    If we fix more constants of motion of the particle besides mass and electromagnetic
charge, for example, the constants described in proposition 5.3, then the space of repres-
entative null geodesics at h will be further constrained.

Celestial spheres

We will now describe a second parameterization of the space of null geodesics Nh+. It uses
physical velocities instead of momenta. Its construction relies on the fact that the time

component  0 is always positive for geodesics in Nh+. Given a null geodesic, define

                              v   :=  1                                              (10.6)
                                       0

as a tangent vector in ThP . Recalling that 0(s) is just the time coordinate of the geodesic,
the projection of v to the 4D tangent space T(h)M4 can be written as

(v) =  d0          -1 4 dn        =               +    3  dn          =     + v.
       ds             n=1 ds  xn      t              n=1   dt  xn        t

Here v is the derivative of position in R3 with respect to time, so it is the 3-dimensional

velocity vector of the particle in the coordinates (t, x1, x2, x3). Decomposing v into its

horizontal and vertical components, we then have

                   v = vH + vV =          +          v   H     vV  .
                                      t
                                                            +

The vector vH +vV is the derivative of position in R3 �K with respect to time. So it is the
higher-dimensional velocity vector of the particle represented by (s), in the coordinate
system. Since  and v are null vectors at h, we have gP (v, v) = 0, and hence

c2 = - gM             ,       = - gP                 H    H
                   t     t                t               t
                                                      ,

       = gP vH + vV , vH + vV = gM (v, v) + gK vV , vV .                             (10.7)

Here we have also used the form (2.1) of the Minkowski metric and the fact that gP
applied to horizontal vectors coincides with gM applied to the 4D projection of those
vectors. Thus, the velocity vectors vH + vV associated with null geodesics at h define
a Euclidean sphere Sck+2 of dimension k + 2 and radius c inside the tangent space ThP .
Generalizing the terminology of the 4D case, this will be called the celestial sphere at h.

    It is clear from this discussion that the correspondence between geodesics in Nh+ and
points in the celestial sphere of velocities is surjective but not injective. A reparameteriza-
tion of the geodesic produces a constant factor in  that cancels out in the quotient (10.6),

                                  32
so leads to the same velocity vector v. Such constant factors can be explicitly controlled
by the time component  0 of the derivative of (s) at h. But, according to (6.9), this
component is proportional to the energy of the particle in the coordinate system,

E =  c2  0 .                                                             (10.8)

This means that the correspondence that takes a non-zero, null geodesic at h to the
velocity vector plus the energy of the particle it represents,

2 : Nh+ - Sck+2 � R+                         h - vH + vV , E

defines a second bijection that can be used to parameterize Nh+. Of course, topologically,
Sck+2 � R+ is isomorphic to the parameter space R3+k \ {0} used in bijection (10.1).
The virtue of the second parameterization is that it is expressed in terms of clear physical
quantities, namely the velocity and energy of the particle represented by the null geodesic.

    The next question is how the subsets of geodesics with fixed mass, previously denoted
by Nh+(m), look like under the parameterization 2. In other words, how are they carved
out from the full parameter space Sck+2 � R+. Using definition (6.6) for the mass of the
particle associated with a geodesic, on the one hand, and using relation (6.9) for the
energy associated with the particle in the frame, on the other hand, it is not difficult to
recognize that under the parameterization 2 we have:

Nh+(m)  vH + vV , E  Sck+2 � R+ : E2 gK(vV , vV ) = m2 c6 .              (10.9)

Thus, when m = 0, the mass condition is satisfied if and only if vV vanishes. When m > 0,
the mass condition only allows points in the celestial sphere with non-zero vV , and then
the component E in R+ is fully determined by the norm of vV . So, for m > 0, the space
Nh+(m) is parameterized by the sphere Sck+2 after the exclusion of an S2 corresponding
to the points with vanishing vV . The excluded points correspond to the 4D motions at
the speed of light, of course.

    Combining (10.6), (10.8), and the mass condition in (10.9), one can check that the
inverse of the parameterization 2 satisfies

-2 1 : Sck+2 \ S2 - Nh+(m)                                               (10.10)
         vH + vV -  (0) =
                                           mc             +v  H       .
                                         gK(vV , vV )  t
                                                                + vV

    Finally, it is relevant to mention that the parameterizations 1 and 2 of Nh+ are not
canonical, in the sense that they both rely on a choice of coordinates on Minkowski space.

                                         33
11 Difficulties with geodesics on Einstein backgrounds

Throughout this paper we have studied geodesic motion on the product P = M4 � K
equipped with an arbitrary submersive metric gP  (gM , A, gK). But what are the most

appropriate background metrics? Where do they come from? A natural answer is that

background metrics should be solutions of a higher-dimensional field equation. In Kaluza-

Klein models, the most common choice is considering solutions of the Einstein equations

on P , obtained by variation of the Einstein-Hilbert action

E(g~P )  =    1    ( Rg~P - 2 ) volg~P                                                              (11.1)
            2 P                                                                                   volg~P .
                 P

         =    1  P      Rg~M  - 2 + Rg~K        -  1  |FA|2  -  1  |dAg~K |2   +  |dA(volg~K )|2
            2 P                                    4            4

The last equality is just (1.5). Although this is a natural choice of action, its relation with

the traditional equations of 4D physics is not trivial. The description of geodesic motion

on such backgrounds has a few subtleties and difficulties.

Dimensional reduction of the Einstein-Hilbert action

A first difficulty is that, for a submersive metric g~P that solves the Einstein equations on
P , its projection g~M to M4 does not satisfy a field equation resembling the traditional 4D
Einstein equation, in general. Dimensional reduction of the relevant term in E(g~P ) yields

                              P  Rg~M volg~P =     M  (Volg~K ) Rg~M volg~M .                     (11.2)

So the gravity component of the 4D Lagrangian does not appear in the traditional guise

Rg~M volg~M , but instead appears multiplied by a scalar field that can vary across M4. This
means that g~M is not the usual 4D metric of GR.

The established procedure to overcome this difficulty is to transform the 4D Lagrangian

from the Jordan frame to the Einstein frame through a Weyl rescaling of g~M [44, 45].
In practice, this means that, given a higher-dimensional metric g~P  (g~M , A, g~K), one
declares that the physical metric in 4D is not g~M -- the simple projection of g~P to the
base M4-- but, instead, is the metric gM related to it by the rescaling

                 gM = e2 g~M            with           e2 := P-1 M Volg~K .                       (11.3)

Using the standard transformation rules of the Riemannian volume form and scalar

curvature under Weyl rescalings [37, 41], one then calculates that

  1        Rg~M volg~P  =        1     M (Volg~K ) e-2       RgM + 6           gM  - 6 |d|2gM volgM
2 P                                                                                                    (11.4)
         P                    2 M   M   P

                        =       1   M RgM - 6 |d|2gM volgM .
                              2 M

                                                   34
So the kinetic term of the new metric gM appears in the precise GR form. It is accompan-
ied by the kinetic term of the scalar field  on M4, measuring the volume of the internal
space. The field equation for gM coming from the action (11.1) will therefore resemble
the 4D Einstein equation with scalar matter and radiation.

    Now consider the Yang-Mills part of E(g~P ). After dimensional reduction, it will not
appear with the canonical normalization of 4D physics for a general, varying internal
metric g~K. When g~K changes, its isometry group can also change, and so can the structure
of massive / massless gauge fields in the model. Thus, the structure of Yang-Mills terms
in the Standard Model cannot correspond to a global property of the Kaluza-Klein model.
Only to a local one, valid in regions of M4 where g~K is approximately constant and close
to its vacuum value g~K0 , which one assumes to be the present-time conditions. Thus,
the aim after dimensional reduction is to obtain 4D Yang-Mills terms with the canonical
normalization only in regions of spacetime where g~K  g~K0 . With this principle established,
one observes that

            P  |FA|2 volg~P =  M   g~M� g~M (FAa)� (FAb )         K  g~K (ea, eb) volg~K volg~M

                            =  M   gM� gM (FAa)� (FAb )           K  g~K(ea, eb) volg~K volgM .

The last equality reflects the invariance of the 4D Yang-Mills action under Weyl rescalings

of gM . Therefore, in the vacuum conditions g~K  g~K0 , dimensional reduction of E(g~P ) will

produce  terms   with  the  canonical     normalization  -  1  (FAa  )�  (FAa)�  if  and    only  if
                                                            4

                                   K g~K0 (ea, eb) volg~K0 = 2 P ab .                                 (11.5)

This is a normalization condition for the vector fields ea on K. It will be important below.

Geodesics and rescalings of the 4D metric

Our previous study of geodesic motion on P assumed that the projection to M4 of the

background metric gP  (gM , A, gK) is the physical 4D metric. For example, section 6

used  that  the  4D  proper  time  of  a  particle  following  a  geodesic  is   c   d   =  -gM ( M ,  M ).
                                                                                     ds

However, in this section we have seen that if g~P is a solution of the Einstein equations on

P with varying internal volume, then its projection g~M should not be identified with the

physical 4D metric gM , only with a rescaled version of it. So we have a potential problem

when interpreting the geodesics of g~P . Three possible strategies to deal with it are:

1) Restrict the action E(g~P ) to metrics of fixed internal volume, satisfying the normal-
    ization condition M Volg~K = P . Use the solutions of the respective field equations
    as backgrounds for geodesics. Due to the normalization, g~M can be identified with
    the physical 4D metric gM in (11.3). The formulae in sections 6 to 10 are unchanged.

                                                    35
   2) Take arbitrary solutions of the Einstein equations on P as backgrounds for geodesics,
       but rescale the identification between the physical 4D-momentum of a test particle
       and the projection to M4 of the momentum vector on P . The formulae in sections
       6 to 10 need some adjustments.

   3) Declare that the physical background metrics gP  (gM , A, gK) should not be solu-
       tions of the Einstein equations on P , but, instead, should be solutions of alternative
       equations that allow a direct identification of gM with the physical 4D metric. For
       such backgrounds, the formulae in sections 6 to 10 will remain unchanged.

Strategy 1 is clear enough. Let us now describe the options 2 and 3 in more detail.

Option 2

All solutions g~P of the Einstein equations on P can be background metrics. Test particles
follow affine geodesics (s) of these metrics. For non-normalized solutions, the physical
metric on M4 is related to the projection g~M of g~P through the rescaling

               gM = P-1 M (Volg~K ) g~M = e2 g~M .                                 (11.6)

The higher-dimensional momentum vector is still p~ =  , but the physical 4-momentum

of the test particle should not be identified with p~M = M , the projection of p~ to M4.

Instead, the 4-momentum pM in (6.7) should be identified with the rescaled projection

               pM      =  e- p~M  =    e-  d   dM  .                               (11.7)
                                           ds   d

So the 3D rest mass of the particle represented by the geodesic (s) now satisfies

m(s) :=  e- d =  e- c-1           -gM ( M ,  M ) = c-1       -gM (pM , pM )
                    ds

               = c-1 -g~M (p~M , p~M ) = c-1 g~K(p~V , p~V ) - g~P (p~, p~) .      (11.8)

This generalizes (6.6) to the case where the physical 4D metric gM does not coincide with
the projection g~M of the metric g~P that appears in the geodesic equation. One can check
that, after the rescalings, the formula for rest mass variation remains unchanged,

               c2  d   m2(s)  =   - (dAg~K)M (p~V , p~V ) .                        (11.9)
                   ds

In regions where the internal geometry is constant, g~K  g~K0 , the definition of charge

should now be

                       q(s) := - e0 g~K(, p~V ) ,                                  (11.10)

instead of (8.1), in order to preserve the form (8.2) of the Lorentz force equation of motion.
Since e20 = P-1 M Volg~K0 is constant in these regions, the charge variation formula (8.4)
changes only by a constant factor e0 on its right-hand side.

                                  36
Option 3

The simple Einstein-Hilbert functional E(gP ) is the most natural action to generate field
equations for background metrics on P . However, due to the difficulties it creates upon
dimensional reduction, one could consider alternative actions for submersive backgrounds
gP  (gM , A, gK) on P . A first example of alternative functional is:

E (gP ) :=     1     e-2 ( RgP - 2 ) volgP                                                    (11.11)
             2 P
                   P

          =  M    1  (RgM  -  2)volgM  +    1    P  e-2 RgK  -  1  e-2  |FA|2  -  ��    �     volgP .
                2 M                       2 P                   4

Here e2 is the scalar -P 1M VolgK and we have used the second equality in (11.1). As in
the calculations leading to (11.5), this functional requires the normalization condition

                   K gK0 (ea, eb) volgK0 = 2 P e2 ab = 2 M VolgK0 ab                          (11.12)

to produce a canonically normalized Yang-Mills term in regions where the internal metric
is close to its vacuum value, gK  gK0 . By construction, in the second line of (11.11) the 4D
gravity term already appears in the Einstein frame. So the projection of the background
metric gP to M4, denoted here gM , can be directly identified with the physical 4D metric.

    A second example of alternative action for background, submersive metrics gP 
(gM , A, gK) is the deformation of the Einstein-Hilbert action E defined by:

E (gM , A, gK) := E (e2 gM , A, gK)                                                           (11.13)

                =    1    (RgM  -  6 |d|2)volgM  +   1  P  e4 RgK  -    1  |FA|2  -  �  �  �  volgP .
                   2M                               2P                  4
                        M

The second equality uses (11.1) and (11.4). For this functional, (11.5) is the normalization
condition necessary to obtain a canonically normalized Yang-Mills term in regions where
gK  gK0 . Once again, the 4D gravity term already appears in the Einstein frame, so the
projection gM of the background metric to M4 can be directly identified with the physical
4D metric. Due to the first line in (11.13), the field equations for gP  (gM , A, gK)
determined by the action E coincide with those obtained by substituting g~M  e2gM
and g~K  gK in the Einstein equations for g~P  (g~M , A, g~K).

    Perhaps the biggest conceptual disadvantage of action (11.13) is that it is not defined
for arbitrary metrics on P . Only for submersive metrics that can be decomposed into
triples (gM , A, gK). So the associated Kaluza-Klein model cannot be interpreted as a
simple transposition of GR to higher dimensions.

                                          37
Electromagnetic q/m ratios

As described in section 8, in regions where the internal metric is constant and only an
electromagnetic-like gauge field is present, the projections to M4 of higher-dimensional
geodesics resemble the usual Lorentz force motions of charged particles in 4D. This was
the original Kaluza "miracle" in the 5D model.

    However, when the background metric comes from the Einstein-Hilbert action on P ,
the range of 4D motions projected by higher-dimensional geodesics has severe limitations.
For example, in the 5D model, all causal geodesics project down to Lorentz force motions
on M4 with q/m ratios that are much lower than the physical ratios for elementary
particles [2, 4]. Spacelike geodesics on P are able produce higher q/m ratios [33], but in
a causal model we would prefer to avoid them.

    Let us examine the problem in more detail. If we set the constant P to be M VolgK0 ,
as in [2], the normalization condition (11.5) implies that

                             1     K gK0 (ea, eb) volgK0  = 2 M ab .            (11.14)
                           VolgK0

In the 5D model, with gK0 being the round metric on K = S1 and ea =  being its standard
Killing field, the function gK0 (, ) is constant along the circle K. So the normalization

condition for  reduces to

                                     gK0 (, ) = 2 M .                           (11.15)

This creates a problem when comparing to the Lorentz force motions coming from the

geodesic picture. For instance, formula (8.3) says that for non-trivial geodesics on M4 �S1

we must have               q                             
                           m            gK0 (, ) = c 2 M ,
                                     c                                          (11.16)

while the charge-to-mass ratio of the electron is many orders of magnitude above this

value. This is the low q/m ratios problem of the 5D geodesic model [2, 4, 33].

A first observation is that it is only for unidimensional fibres that (11.14) actually fixes

the value of gK0 (, ). In higher dimensions, only the average of gK0 (, ) over the manifold
(K, gK0 ) is fixed. And, in principle, that average can be significantly different from the
point values that appear in the geodesic equation. So a geodesic passing through points

in P   where the norm gK0 (, ) is higher than average     can project down to a 4D Lorentz
force  motion with a q/m ratio higher than c 2 M .        If the geometry of (K, gK0 ) is very

heterogeneous -- for instance if gK0 hasa singularity -- the q/m ratios of the projected
4D motions can be much higher than c 2 M .

A second observation is that the normalization conditions (11.5) and (11.14) assume

that the background metric for geodesics comes from the simple Einstein-Hilbert action on

                                        38
P . For example, for the alternative action (11.13), which is directly in the Einstein frame,
the normalization (11.5) is still necessary but we no longer have to fix the value of P to
be M Volg~K0 , in order to obtain a canonically normalized Yang-Mills term. So (11.14) is
no longer valid. Thus, choosing a sufficiently big P , the higher bound on the q/m ratios
imposed by the normalization of the Killing field  no longer excludes the charge-to-mass
ratios of elementary particles. In other words, the action (11.13) generates backgrounds
without q/m ratios problems. More generally, in a realistic model the Einstein-Hilbert
action on P may need higher order corrections to describe the appearance of physical
particles with masses at very different scales. Such higher order terms can affect the
normalization condition for the Killing fields, and the corrected condition may be less
problematic than (11.5).

Acknowledgements

It is a pleasure to thank Nick Manton and Nuno Rom~ao for helpful comments on an earlier
version of this paper.

                                                       39
Appendices

A Auxiliary results and a remark on notation

Remark. The notation used in this paper differs significantly from the conventional
notation in the literature about Riemannian submersions. The modification is necessary
because the latter clashes with the traditional notation in physics. Namely, the tensor
called A in [11�14] is essentially what we call FA here, since it represents the physical
gauge fields strength. More precisely, the relation is

            FA(X, Y ) = 2 A~XH Y H = [XH, Y H]V ,  (A.1)

where X, Y are vector fields on the base M; the symbols XH and Y H denote their lifts as
basic vector fields on P ; we have denoted by A~ the tensor called A in [11�14]; and the last
equality is a standard result in Riemannian submersions. The tensor called T in [11�14]
is what we call here dAgK (or S less often). This avoids confusion with torsion or with the
energy-momentum tensor. It also emphasizes its physical role as a covariant derivative of
Higgs-like fields. The precise relation is

(dAgK)X(U, V ) = (LXHgP )(U, V ) = - 2 gP (TU V, XH) = - 2 gP (U V, XH) , (A.2)

where X is a vector field on M and U, V are vertical vector fields on P . The last equality
is the definition of the tensor T in [11�14] in terms of the Levi-Civita connection on P .
The first two equalities are derived in sections 2.3 and 2.5 of [37].

Now the auxiliary results. Classical work of Ehresmann and Hermann [9,10] implies that:

Proposition A.1. Let  : (P, gP )  (M, gM ) be a Riemannian submersion. If the metric
gP is complete, then  defines a locally trivial fibration. In this case, given a path M (s)
on M starting at a point x and given a point p in P such that (p) = x, there exist a
unique path (s) on P starting at p such that M =    and the derivatives  are always
horizontal vectors on P . This  is called a horizontal lift of M .

Regarding horizontal geodesics, O'Neill has the following result:

Proposition A.2 ( [12]). Let  : (P, gP )  (M, gM ) be a Riemannian submersion and let
(s) be a geodesic on P . If the derivative  is a horizontal vector at some point, then it
is always horizontal. Moreover, in this case the projection M (s) =   (s) is a geodesic
on (M, gM ).

Using basic properties of Riemannian submersions (e.g. see [13, sec. 9]), we show that:

            40
Lemma A.3. Let  : P  M be a Riemannian submersion with metric gP determined
by the equivalent data (gM , gK, A). Let U and V be vertical vector fields and let Z be a
basic vector field on P . Then

(LV gP )(U, U ) = (LV gK)(U, U )       (LV gP )(Z, Z) = 0
(LV gP )(Z, U ) = gK([Z, V ], U ) .
                                                                                 (A.3)

In particular, V is Killing with respect to gP if and only if the restriction of V to each
fibre is Killing with respect to gK and, additionally, the Lie bracket [V, Z] vanishes for
every basic vector field Z on P .

Proof. The horizontal basic field Z is -related to a well-defined vector field Z on the
base M. Since V is vertical, we have [V, Z] = [V, Z] = 0, and the bracket [V, Z] is
also vertical. So by definition of Lie derivative:

(LV gP )(Z, Z) = LV ( gP (Z, Z) ) - 2gP ([V, Z], Z) = LV ( gM (Z, Z) ) = 0 .

Using that U and [V, U] are both vertical, so are both orthogonal to Z, we have

(LV gP )(Z, U ) = LV ( gP (Z, U ) ) - gP ([V, Z], U ) - gP (Z, [V, U ]) = gP ([Z, V ], U ) .

Finally, since U, V and [U, V ] are all vertical and gK just denotes the restriction of gP to
the fibres, it is clear that

(LV gP )(U, U ) = LV ( gP (U, U ) ) - 2 gP ([V, U ], U )                         (A.4)
                   = LV ( gK(U, U ) ) - 2 gK([V, U ], U ) = (LV gK)(U, U ) .

Now suppose that LV gP vanishes. Then by (A.3) we get that (LV gK)(U, U) vanishes for
all U. Since LV gK is symmetric in both entries, it must also vanish. Moreover, also by
(A.3), the vanishing of (LV gP )(Z, U) for all U and the non-degeneracy of gK imply that
[Z, V ] vanishes for all basic Z. This confirms the "only if" part of the last statement,
while the converse is clear.

Lemma A.4. Let  : P  M be a Riemannian submersion with metric gP determined by
the equivalent data (gM , gK, A). Let Y and Z be basic vector fields and let U be a vertical
vector field on P . Then

(LY gP )(Z, Z) =  [(LY gM )(Z, Z)]     (LY gP )(U, U ) = (dAgK)Y (U, U )
(LY gP )(Z, U ) = gP (FA(Y, Z), U ) .                                         (A.5)

In particular, Y is Killing with respect to gP if and only if the projection Y is Killing
with respect to gM , the covariant derivative (dAgK)Y vanishes as a tensor on P and,
additionally, the contraction FA(Y, �) vanishes as a one-form on M.

41
Proof. By definition, basic vector fields on P are horizontal and hence orthogonal to
vertical vector fields. Moreover, the Lie bracket of a basic field with a vertical field is
always vertical on P , hence orthogonal to Z. So we have that

(LY gP )(Z, U ) = LY ( gP (Z, U ) ) - gP ([Y, Z], U ) - gP (Z, [Y, U ])  (A.6)
                   = - gP ([Y, Z], U ) = gP (FA(Y, Z), U ) ,

where the last equality follows from (A.1).

    A basic vector field on P is -related to a unique, well-defined vector field on the base
M. So we have that [Y, Z] = [Y, Z] as vector fields on the base M. Then

(LY gP )(Z, Z) = LY ( gP (Z, Z) ) - 2 gP ([Y, Z], Z)                     (A.7)
                   = LY ( gM (Z, Z) ) - 2 gP ([Y, Z]H, Z)
                   =  LY ( gM (Z, Z) ) - 2  [gM ([Y, Z], Z)]
                   =  [(LY gM )(Z, Z)]

as functions on P , as desired. The last identity

(LY gP )(U, U ) = (dAgK)Y (U, U )

is tautological. It comes from the definition of covariant derivative of gK, as explained
in (A.1) and [37]. Finally, the necessary and sufficient condition for Y to be Killing with
respect to gP is clear from the formulae above, considering that Z can be any basic field
and U can be any vertical field on P .

The following observation, stated in [13, sec. 9F], is a consequence of results in [10, 11].

Proposition A.5. Let the metric gP  (gM , A, gK) define a Riemannian submersion on
P with totally geodesic fibres, i.e. with dAgK = 0. Then the curvature form FA(X, Y ) has
values in the Killing vector fields of gK for every X, Y  T M.

In section 5 we use the following standard result.

Lemma A.6. Let {uj} be a basis of the space of Killing vector fields on a compact
Riemannian manifold (K, gK). Define the structure constants with respect to this basis
by the relations [ui, uj] = filj ul. If the basis is orthonormal with respect to the L2-inner
product on (K, gK), then the filj are totally anti-symmetric in their three indices.

Proof. The Lie derivatives of the metric gK and volume form volgK both vanish along
Killing vector fields. Using this fact, the definition of the L2-inner product of vector fields

42
and Stokes' theorem, we can write

l filj ul, uk L2 =  [ui, uj], uk L2 =               gK([ui, uj], uk) volgK

                                                  K

             =      K  Lui gK(uj, uk) - gK(uj, [ui, uk]) volgK

             = Lui gK(uj, uk) volgK - gK(uj, [ui, uk]) volgK
                    K                                             K

             = - gK(uj, [ui, uk]) volgK = -                               l filk uj, ul L2 .
                           K

Thus, when the basis {uj} is L2-orthonormal, we get that

          l filj lk + filk jl = 0  fikj = - fijk .

The anti-symmetry of filj in the lower two indices follows from its definition and is true
for any basis.

B Parallel transport in Riemannian submersions

For reference, in this appendix we write down the equations of parallel transport of vectors
along general curves (s) on the higher-dimensional space P = M � K. That space is
assumed to be equipped with a submersive metric gP  (gM , A, gK). Parallel transport
is determined by its Levi-Civita connection . As in section 3, a vector E in T P can
be decomposed into horizontal and vertical components, E = EH + EV , defined through
(3.4). The projection of the curve (s) to the base M is denoted by M (s), so that
M =   . The Levi-Civita connection on M determined by the projected metric gM is
denoted by M .

    With this notation, the equations in [12] for the horizontal and vertical components
of the covariant derivative  E along (s) can be written as:

gP  E, V  = gP  EV , V             +  1  FAa( M ,     EM )  gP (ea,   V)  -  gP  SV  V , EH
gP  E, Z                              2

          = gM MM EM , Z                 +  1  FAa(Z,        M )  gP  ea, EV
                                            2

          +  1  FAa(Z,             EM )  gP (ea,   )  +  gP  S V EV , Z                       (B.1)
             2

Here Z and V are any horizontal and vertical vectors in T P , respectively. We have also
translated O'Neill's notation to the one used in this paper, as described in the remark of
appendix A. As in section 4, the tensor S is the second fundamental form of the fibres of
P . It is essentially coincides with our dAgK, as expressed in (4.5).

                                         43
    The general equations B.1 reduce to (4.1) when we take E =  . The equations satisfied
by a parallelly transported vector field E(s) can be obtained from B.1 by setting  E = 0
on the left-hand sides.

                                                       44
References

 [1] D. Kovacs: The geodesic equation in five-dimensional relativity theory of Kaluza-
      Klein, Gen. Relat. Gravit. 16 (1984), 645�655.

 [2] J. Gegenberg and G. Kunstatter: The motion of charged particles in Kaluza-Klein
      space-time, Phys. Letters 106A (1984), 410�414.

 [3] Y. Cho and D. Park: Higher-dimensional unification and fifth force, Il Nuovo Ci-
      mento, 105 B (1990), 817�829.

 [4] R. Coquereaux and G. Esposito-Farese: The theory of Kaluza-Klein-Jordan-Thiry
      revisited, Ann. Inst. H. Poincar�e 52 (1990), 113�150.

 [5] H. Liu and B. Mashhoon: Spacetime measurements in Kaluza�Klein gravity, Phys.
      Letters 272A (2000), 26�31.

 [6] S. Seahra and P. Wesson: Null geodesics in five-dimensional manifolds, Gen. Relat.
      Gravit., 33 (2001), 1731�1752.

 [7] E. Minguzzi: Proper time and conformal problem in Kaluza�Klein theory, Int. J.
      Geom. Meth. Mod. Phys. 12 (2015), 1550063.

 [8] L. Feh�er: Classical motion of coloured test particles along geodesics of a Kaluza-Klein
      spacetime, Acta Phys. Hungarica 59 (1986), 437�444.

 [9] C. Ehresmann: Les connexions infinit�esimales dans un espace fibr�e diff�erentiable,
      Colloque de Topologie (1950), 29�55.

[10] R. Hermann: A sufficient condition that a mapping of Riemannian manifolds be a
      fibre bundle, Proc. Amer. Math. Soc. 11 (1960), 236�242.

[11] B. O'Neill: The fundamental equations of a submersion, Michigan Math. J. 13 (1966),
      459�469.

[12] B. O'Neill: Submersions and geodesics, Duke Math. J. 34 (1967), 363�373.

[13] A. Besse: Einstein manifolds, Classics in Mathematics, Springer-Verlag, 1987.

[14] M. Falcitelli, S. Ianus and A. Pastore: Riemannian submersions and related topics,
      World Scientific Publishing, 2004.

[15] D. Bailin and A. Love: Kaluza-Klein theories, Rep. Prog. Phys. 50 (1987), 1087�1170.

                                                       45
[16] D. Bleecker: Gauge theory and variational principles, Addison-Wesley, 1981.

[17] J. Bourguignon: A mathematician's visit to Kaluza-Klein theory, Rend. Sem. Mat.
      Univ. Politec. Torino (1989), 143�163.

[18] L. Castellani, P. Fr�e and R. D'Auria: Supergravity and superstrings: a geometric
      perspective, Vol. 2, Part five, World Scientific Publishing, 1991.

[19] R. Coquereaux and A. Jadczyk: Riemannian geometry, fiber bundles, Kaluza-Klein
      theories and all that...., World Scientific Publishing, 1988.

[20] M. Duff, B. Nilsson and C. Pope: Kaluza-Klein supergravity, Phys. Reports 130
      (1986), 1�142.

[21] J. Overduin and P. Wesson: Kaluza-Klein gravity, Phys. Reports 283 (1997), 303�
      380.

[22] E. Witten: Search for a realistic Kaluza-Klein theory, Nucl. Phys. B186 (1981),
      412�428.

[23] T. Kaluza: Zum Unitt�asproblem in der Physik, Sitzungsber. Preuss. Akad. Wiss.
      Berlin Math. Phys. K1 (1921), 966�972.

[24] O. Klein: Quantentheorie und fu�nfdimensionale Relativit�atstheorie, Zeitschrift Phys.
      37 (1926), 895�906.

[25] A. Einstein and P. Bergmann: On a generalization of Kaluza's theory of electricity,
      Annals Math. 39 (1938), 683�701.

[26] P. Jordan: Relativistische Gravitationstheorie mit variabler Gravitationskonstante,
      Naturwissenschaften 33 (1946), 250�251.

[27] Y. Thiry: Les �equations de la th�eorie unitaire de Kaluza, Comptes Rendus Acad.
      Sci. Paris 226 (1948), 216�218.

[28] B. DeWitt: Dynamical theory of groups and fields, in Lectures at 1963 Les Houches
      School, Gordon and Breach, 1964, 585�820.

[29] R. Kerner: Generalization of the Kaluza-Klein theory for an arbitrary non-abelian
      gauge group, Ann. Inst. H. Poincar�e 9 (1968), 143�152.

[30] A. Trautman: Fiber bundles associated with space-time, Rep. Math. Phys. 1 (1970),
      29�62.

                                                       46
[31] Y. Cho: Higher-dimensional unifications of gravitation and gauge theories, J. Math.
      Phys. 16 (1975), 2029�2035.

[32] E. Leibowitz and N. Rosen: Five-dimensional relativity theory, Gen. Relat. Gravit.
      4 (1973), 449�474.

[33] A. Davidson and D. Owen: Elementary particles as higher-dimensional tachyons,
      Phys. Lett. 177B (1986), 77�81.

[34] L. Feh�er and P. Horvathy: Dynamical symmetry of the Kaluza-Klein monopole, in
      Proc. Symmetries in Science III, Plenum, 1989, 399�417.

[35] P. Wesson and J. Leon: The equations of motion in Kaluza-Klein cosmology and its
      implications for astrophysics, Astron. Astrophys. 294 (1995), 1�7.

[36] V. Lacquaniti, G. Montani and D. Pugliese: Massive test particle motion in 5-
      dimensional electromagnetic-free Kaluza-Klein theory, Gen. Relat. Gravit. 43 (2011),
      1103�1120.

[37] J. Baptista: Internal symmetries in Kaluza-Klein models, J. High Energ. Phys. 2024
      (2024), 178.

[38] S. Wong: Field and particle equations for the classical Yang-Mills field and particles
      with isotopic spin, Nuovo Cimento 65 (1970), 689�694.

[39] P. Horvathy and P. Zhang: Kerner equation for motion in a non-abelian gauge field,
      Universe 9 (2023), 519.

[40] E. Witten: Fermion quantum numbers in Kaluza-Klein theory, in Shelter Island II,
      Proceeding of the 1983 Shelter Island conference, MIT Press, 1985, 227�277.

[41] R. Wald: General relativity, Chicago Univ. Press, 1984.
[42] J. Milnor: Curvature of left invariant metrics on Lie groups, Adv. Math. 21 (1976),

      293�329.

[43] R. Kerner, J. Martin, S. Mignemi and J. Holten: Geodesic deviation in Kaluza-Klein
      theories, Phys. Rev. D63 (2000), 027502.

[44] V. Faraoni, E. Gunzig and P. Nardone: Conformal transformations in classical grav-
      itational theories and in cosmology, Fund. Cosmic Phys. 20 (1999), 121�175.

[45] Y. Cho: Unified cosmology, Phys. Rev. D41 (1990) 2462�2471.

                                                       47
