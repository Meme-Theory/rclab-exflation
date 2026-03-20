# 2026 Geometry of CP violation in Kaluza Klein models

**Source:** `18_2026_Geometry_of_CP_violation_in_Kaluza_Klein_models.pdf`

---

arXiv:2601.08902v1 [hep-th] 13 Jan 2026            The geometry of CP violation
                                                        in Kaluza-Klein models

                                                                               Joa~o Baptista
                                                                                January 2026

                                                                                  Abstract

                                         We investigate the free, massless Dirac equation D/  = 0 on a higher-dimensional manifold
                                         M4 � K equipped with a submersion metric. These background metrics generalize the
                                         Kaluza ansatz. They encode 4D massive gauge fields and Higgs-like scalars, alongside the
                                         usual 4D metric and massless gauge fields. We show that the dimensional reduction of the
                                         Dirac equation on these backgrounds naturally violates CP symmetry in four dimensions.
                                         This provides a new geometric path to constructing models with intrinsic CP violation.
                                         In this framework, massive gauge fields can break CP for three different reasons: i) a
                                         misalignment between the mass eigenspinors and the spinors in the representation basis;
                                         ii) a new non-minimal term coupling 4D fermions to massive gauge fields; iii) the presence
                                         of a non-abelian Pauli term. All this derives from the higher-dimensional Dirac equation.
                                         Technically, the paper uses the language of spin geometry and Riemannian submersions.
                                         Along the way, it develops detailed geometric descriptions of several constructions. It
                                         discusses gauge anomalies, fermion generations, and introduces a new Lie derivative of
                                         spinors along non-Killing vector fields induced by actions of compact groups.

                                         Keywords: Kaluza-Klein theories; CP violation; Riemannian submersions; Dirac operator;
                                         weak force; parity transformations; charge conjugation.
Contents

1 Introduction and overview of results . . . . . . . . . . . . . . . . . . . . . . . . . 1
2 Spinors on Riemannian submersions . . . . . . . . . . . . . . . . . . . . . . . . . 8
3 Spinor symmetries on M4 � K induced by 4D reflections and parity . . . . . . . 13
4 Conjugation symmetries on spinor bundles . . . . . . . . . . . . . . . . . . . . . 17
5 Actions of compact groups on K and its spinors . . . . . . . . . . . . . . . . . . 20
6 Representation spaces versus D/ -eigenspaces . . . . . . . . . . . . . . . . . . . . 22
7 Dimensionally reduced equations and CP violation . . . . . . . . . . . . . . . . 26
Appendices
A Conventions for spinors in signature (s, t) . . . . . . . . . . . . . . . . . . . . . . 33
B Relating spinors of different metrics . . . . . . . . . . . . . . . . . . . . . . . . . 38
C Proofs for section 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
D Proofs for section 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
E An example with (SU(3) � SU(2) � U(1))/Z6 symmetries . . . . . . . . . . . . . 53
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56

                                                         i
1. Introduction and overview of results

1.1. Introduction

The discovery of CP violation was the observation that, in nature, left-handed particles
do not interact with the weak force in exactly the same way as right-handed antiparticles
do. The experimental tests of CP violation rely on measuring this asymmetry in a variety
of physical processes [1�4]. Although modest in magnitude, the observed asymmetry can
be regarded as natural. Particles and antiparticles respond differently to the strong and
electromagnetic forces. Why would they respond identically to the weak force?

    The only reason the observed asymmetry seems unexpected is a technical one. In the
Standard Model (SM), one usually goes from particles to antiparticles by complex con-
jugating gauge representations. Conjugating the electromagnetic u(1) representation of a
particle, for instance, or its colour su(3) representation, produces distinct representations
associated with the antiparticle. However, in the same SM framework, the weak gauge
bosons act on fields either trivially or through the fundamental su(2) representation.
Notably, this representation is equivalent to its complex conjugate. So the theoretical
structure of the SM would suggest, at first glance, identical behaviours of particles and
antiparticles when interacting with the weak force.

    Nature insists on the asymmetry, though, despite the equivalence of su(2) represent-
ations. So physicists had to devise an entirely new mechanism to embed the particle-
antiparticle asymmetry into the SM equations. Conjugating fermion representations does
not change anything for the weak force. The skilful solution was to introduce ad hoc
complex phases in the CKM and PMNS matrices [5�7]. This is a minimal adjustment
that works effectively. Those phases are not invariant under complex conjugation. So they
produce the desired inequivalence between the equations for particles and antiparticles.

    A sense of theoretical unease may linger, though. What is the origin of the new
phases? What kind of mathematical structures can produce them and govern their specific
values? Are there natural frameworks in which the equations of motion of particles
and antiparticles, as derived from first principles, differ by something beyond simple
conjugation of gauge representations? Such equations would break CP.

    The purpose of this paper is to show that the Kaluza-Klein (KK) framework has that
formal property. If we take the massless Dirac equation D/  = 0 on P = M4 � K with
appropriate background metrics, then, after dimensional reduction, we obtain massive
Dirac equations on M4 that in general violate CP. In other words, the 4D equations of
motion for particles and antiparticles are not equivalent after a parity transformation and
complex-conjugating all the gauge representations.

                                                        1
    The appropriate backgrounds in question are higher-dimensional submersion metrics.
They are natural generalizations of the Kaluza ansatz. They encode, besides the 4D
metric and massless gauge fields, also massive 4D gauge fields and Higgs-like scalars.
This paper shows that, when the submersion metric on M4 � K encodes non-zero massive
gauge fields, then the dimensionally reduced Dirac equation contains three terms that can
break CP symmetry in 4D.

    Early works studying the discrete symmetries of the Dirac equation in pure higher-
dimensional gravity are [8�10], for example. They establish most of the properties of those
spinor symmetries for different numbers of extra dimensions. Following the traditional
form of the Kaluza ansatz, they focus on higher-dimensional metrics encoding only abelian
or massless 4D gauge fields. This hides the rich spinorial structure that emerges when
the background also encodes 4D massive gauge fields. That structure produces the CP
violations discussed here. More recent studies of CP violation induced by extra dimensions
are [11�16], for example. They investigate models with orbifold compactifications and
higher-dimensional gauge fields, with a phenomenological and brane world bend. More
references in the review [17]. They differ significantly from the pure gravity KK approach
of the present paper.

    Kaluza-Klein models with massive gauge fields based on general submersion metrics
are investigated in [18�20]. The first paper establishes that submersions with fibres that
are not totally geodesic correspond to gauge theories with massive 4D gauge fields and
Higgs-like scalars. It computes the mass of gauge fields in terms of the second fundamental
form of the fibres of the submersion. The paper [19] studies geodesic motion on these
higher-dimensional backgrounds, and how it is physically perceived after projection to
M4. The paper [20] studies the free Dirac equation D/  = 0 and its KK reduction to
4D, like the present one. It establishes that, on the same submersion backgrounds, the
dimensionally reduced Weyl equation in general exhibits chiral couplings of 4D fermions
and massive gauge fields. This is a new way to circumvent well-known no-go arguments
against the existence of chiral fermions in KK models [21�24].

    Extended reviews of the Kaluza-Klein framework can be found in [25�31]. Some
of the early original references are [32�39]. This paper follows the treatment given in
[18�20] of massive gauge fields, Higgs-like scalars and spinors. Clear limitations of the
present analysis are that it is classical, all throughout, and that it investigates mainly the
mathematical properties of the theories. So no phenomenology at this point. It also does
not discuss the dynamical origin of the vaccum metrics on K. It just assumes existence
and stability of some gK. Then it relates the properties of 4D fermions and gauge fields to
the properties of that metric. We now give an overview of the main results in the paper.

                                                        2
1.2. Overview of the main results

Spinors on Riemannian submersions

Section 2 recalls the main properties of spinors on a manifold P = M � K equipped
with a submersion metric gP . The classical results about Riemannian submersions were
developed by O'Neill in [40], after foundational work in [41, 42]. They are presented
in [43, 44], for example. We use the translation of those results to the Kaluza-Klein
language provided in [18]. In that language, submersion metrics on P are equivalent to
triples (gM , A, gK) encoding the metric on M , 4D gauge fields (massless and massive), and
an internal metric gK that can change along M . The higher-dimensional Einstein-Hilbert
action can be decomposed as

  RgP volgP =     RgM  +  RgK  -  1  |FA|2  -  1  |dAgK |2  +  |dA (volgK )|2  volgP .  (1.1)
                                  4            4
P              P

This extends the usual Kaluza-Klein result to the setting of general Riemannian submer-
sions. It suggests that the internal metric gK can be understood as a geometric version
of the traditional Higgs fields. More details can be found in [18, 43].

    For a general submersion metric on P , the gauge one-form A� on M has values in
the full space of vector fields on K, which is the Lie algebra of the diffeomorphism group
Diff(K). So it can be expanded as A�a ea, where {ea} is a set of independent vector fields
on K, some of them Killing and most others non-Killing. The gauge group is Diff(K) or
a subgroup. It need not act on K only through isometries of gK. The classical mass of
the 4D gauge field linked to a divergence-free ea is calculated in [18] to be

                  Mass Aa� 2         K Lea gK , Lea gK  volgK ,                         (1.2)
                                       2 K gK (ea, ea) volgK

where LeagK denotes the Lie derivative of the internal vacuum metric along ea. This
suggests that massive gauge fields, however light, should not be linked to exact isometries
of gK. The derivatives LeagK can be small yet non-zero.

    Spinors on general Riemannian submersions were studied in [20, 45�47]. Section 2
summarizes the results that are most relevant for us in the language of [20], suitable for
explicit Kaluza-Klein physics. Assuming that M is even-dimensional, it describes the
decomposition of higher-dimensional spinors as tensor products of horizontal and vertical
spinors. Using the equivalence gP  (gM , A, gK), it presents the explicit formula for the
Dirac operator on P written in terms of the components of the triple.

                                     3
Reflections and parity transformations on M � K

Reflections and parity inversions on M have natural extensions to diffeomorphisms of
P = M � K that do not change the internal coordinates. The extended diffeomorphisms
are denoted R and P, respectively. They are not isometries of the submersion metric on
P , in general. The transformation rules of gP under pullback by those diffeomorphisms,
for example gP  PgP , encapsulate the usual transformation rules of 4D gauge fields
Aa� and Higgs-like fields under reflections and parity inversions.

    The diffeomorphisms of P induced by reflections and parity inversions also determine
transformations of the higher-dimensional spinors. However, the construction of spinor
bundles depends on the background metric, and gP is not preserved by the diffeomorph-
isms. Thus, reflections and parity inversions relate spinors defined on different bundles
over P . For example, the spinor bundles SgP and SPgP . This is a slight variation from the
usual story on Minkowski space, which deals with isometries of gM and automorphisms of
a single bundle [48�50]. Despite this difference, the KK extensions of reflections and parity
inversions still induce symmetries of the higher-dimensional Dirac equation, D/ P  = 0.
This is the main point for us. Section 3 and appendix C spell out the main properties
of the spinor transformations on M � K induced by those symmetries. The tone is more
geometric than in earlier work [9, 10]. We extend those results to our KK models, with
general submersion metrics and spinor transformations between different bundles.

Conjugations of spinors j�

Section 4 and appendix A give succinct accounts of the conjugation automorphisms j�
of spinor bundles on arbitrary manifolds of signature (s, t). They describe the essential
properties of these symmetries of the massless Dirac equation. Section 4 uses a geo-
metric approach and hides the basis-dependent constructions, with gamma matrices in
special representations, that are generally used to prove the existence of these maps. The
bundle-version of the conjugation maps includes their relations with differential operators
such as covariant derivatives, the Dirac operator and, importantly for us, the Kosmann-
Lichnerowicz derivative of spinors. The spinor conjugation maps in arbitrary signatures
are a well-studied topic in the literature. See for instance [49, 51, 52]. The purpose of sec-
tion 4 is to provide a short and hopefully clean summary that covers the general case of
signature (s, t) and the bundle-related properties. At the end, it also presents results that
help to understand conjugation maps in the specific setting of Riemannian submersions.

                                                        4
Actions of compact groups on K and its spinors

An isometric action of a connected group on a compact spin manifold K has a canonical
lift to an action on the spinors in SgK , after passing to a covering group if necessary. In
its infinitesimal version, this lift defines a Lie derivative of spinors along Killing vector
fields [53]. The standard extension of this derivative to arbitrary vector fields on K is the
Kosmann-Lichnerowicz derivative [54], defined by

                              1                                           (1.3)
     LV  := V  - 8 j, k g(vj V, vk) - g(vk V, vj) vj � vk �  .

This extended derivative couples the 4D gauge fields to internal spinors in general Kaluza-
Klein models, as described in [20]. A drawback of this derivative, however, is that it
satisfies the closure relation (LU LV -LV LU ) = L[U,V ] only when U or V are conformal
Killing for gK. Otherwise, it is not a proper Lie derivative.

    In section 5 we show that, when a connected compact group G acts on K, there is a
useful alternative derivative of spinors given by

LV   =  LV   +  V   =  LV   +  1        g  -1(LV )(vj), vk  vj � vk �  .  (1.4)
                               4
                                  j= k

It coincides with the Kosmann-Lichnerowicz derivative when V is conformal Killing. It
satisfies (LU LV - LV LU ) = L[U,V ] for all fundamental vector fields on K induced by the
G-action, even when U and V are not conformal Killing with respect to gK. So we obtain
a new lift of non-isometric actions to spinors, at least when K is compact.

    The new derivative is defined through a canonical map  : SgK  Sg^K between two
spinor bundles on K, corresponding to the metric gK and its G-averaged metric g^K.
The relations between spinors associated with different Riemannian metrics on the same
manifold have been previously studied in [55�57], for example. The parts of those works
that we need here are summarized in appendix B. That appendix also presents several
new formulas that are necessary for our purposes, mostly related to the transport of the
Kosmann-Lichnerowicz derivative through .

Spinor representation spaces, gauge anomalies and fermion generations

Let g denote the Lie algebra of vector fields on K induced by the action of a compact
group G. The new spinor derivative LV allows us to define a unitary representation of g

                                  5
on the space of spinors in SgK equipped with its natural L2 Hermitian product:

                         1                                                      (1.5)
V () := LV  + 2 divg(V )  .

In section 6, we describe two decompositions of the space of spinors on K as a sum
of finite-dimensional subspaces that are irreducible under . When the G-action is not
isometric, the operators V do not commute with the Dirac operator on SgK . So the
irreducible g-spaces are non-trivially related to the D/ -eigenspaces.

    Following [20], we remark that, for non-isometric G-actions, our KK models can have
chiral fermions. In this case, the chiral interactions generated by the representation  are
free of local gauge anomalies. This happens because  commutes with the internal spinor
conjugation maps j�. So it is a self-conjugate representation. The irreducible g-spaces of
complex type will always appear in conjugate pairs.

    Section 6 also describes a finite subset of spinor transformations that commute with
the representation , but need not commute with the Dirac operator D/ when G acts
non-isometrically on K. Thus, in a KK model, these special spinor transformations can,
in principle, relate 4D fermions in the same g-representations but with different masses,
i.e. can relate distinct generations of fermions. This is not fully proved here, however.

The CP-transformed Dirac equations in 4D

In section 7 we simplify the treatment and assume that the metric gK on the internal space
is constant along M . Then any higher-dimensional spinor can be written as (x, y) =

   H (x)  (y), where x and y are coordinates on M and K, respectively. The 
are spinors on M and the set {} is a L2-orthonormal basis of the space of internal
spinors on K. For a higher-dimensional spinor of this form, the Dirac equation D/ P  = 0
is equivalent to an infinite set of equations on M :

i � XM�  + Aa�   , (ea + ea ) L2  +   , D/ K  L2 

+  1  (FAa)�  , ea � L2 �                          = 0.                         (1.6)
   8

A basis of internal spinors {} formed with eigenspinors of the internal Dirac operator
D/ K, with respective eigenvalues m, is called a mass basis. In such bases, equation (1.6)

reduces to a standard 4D gauged Dirac equation with a mass term and a Pauli term.

    Conjugations of spinors and parity inversions are exact symmetries of the massless
Dirac equation on M � K. So are the compositions j�P. This is described in sections 3
and 4. If a higher-dimensional spinor satisfies D/  = 0, we always have D/ (j�P ) = 0 as

      6
well. In section 7 we determine how the second equation looks after dimensional reduction
to M . In the case of the conjugation j-, the result is the set of equations:

i � M X� cp + (Ap)�a   , (ea + ea ) L2 cp +   , D/ K  L2 cp

+  1  (FAap )�  , ea � L2  � cp                              =  0  (1.7)
   8

where cp = j-M PM () are the CP-transformed spinors in 4D. So the spinors cp satisfy
equations of motion very similar to those satisfied by the original . The differences are
that the gauge form is now the parity-transformed Ap, instead of A, and four types of
matrices -- determined by the operators ea, ea, D/ K, and ea� on the space of internal
spinors -- appear complex-conjugated in the new equation.

CP violation

The higher-dimensional CP transformations are exact symmetries of the massless Dirac
equation on M � K, as stressed before. However, after dimensional reduction to 4D, they
do not act simply by complex conjugating the gauge representations. If we redefine those
representations by ea  ea, equations (1.6) and (1.7) still remain formally different.
Thus, in the Kaluza-Klein setting, there is no reason to expect that left-handed particles
interact with any of the physical 4D forces in exactly the same way that right-handed
antiparticles do. If a force is described by a gauge representation that is equivalent to
its complex conjugate, such as the fundamental SU(2) representation, that fact by itself
is not enough to render (1.6) and (1.7) equivalent. Other terms in the equations remain
different.

    In regions where massive gauge fields A�a are turned on, the respective transformations
ea do not commute with the internal Dirac operator D/ K. They do not preserve the
eigenspaces of D/ K and will mix 4D fermions with different masses. There is an infinite-
dimensional complex matrix relating the D/ K-eigenspinors with the bases of the irreducible
subspaces of the gauge representation . There seems to be no a priori reason to expect the
existence of a clever choice of representation basis {} that renders the CKM-like mass
matrix   , D/ K L2, the Pauli term matrix  , ea � L2, and the new non-minimal
gauge coupling matrix   , ea �  L2, all simultaneously real on general grounds. It
would be interesting to study these matters with explicit examples, based on different
compact spin manifolds K. One interesting example is suggested in appendix E. However,
explicitly solving such examples is no easy task in spinor geometry.

   7
2. Spinors on Riemannian submersions

2.1. Riemannian submersions

This section recalls relevant properties of spinors on manifolds equipped with submersion
metrics. These metrics generalize the Kaluza ansatz by encoding not only the 4D metric
and massless gauge fields, but also 4D massive gauge fields and an internal metric that can
vary along M . The main classical results about Riemannian submersions were developed
in [40�42] and are presented in [43, 44], for example. We use the translation of those
results to the Kaluza-Klein language provided in [18].

    Let gP be a Lorentzian metric on the higher-dimensional space P = M � K such
that the projection P  M is a Riemannian submersion. As described in [18], this is
equivalent to taking a gP determined by three simpler objects:

 i) a Lorentzian metric gM on the base M ;

ii) a family of Riemannian metrics gK(x) on the fibres Kx parameterized by the points
     x  M;

iii) a gauge one-form A on M with values in the Lie algebra of vector fields on K.

These objects determine the higher-dimensional metric through the relations

gP (U, V ) = gK(U, V )                                                       (2.1)
gP (X, V ) = - gK (A(X), V )
gP (X, Y ) = gM (X, Y ) + gK (A(X), A(Y )) ,

valid for all tangent vectors X, Y  T M and vertical vectors U, V  T K. These relations
generalize the usual Kaluza ansatz for gP . Choosing a set {ea} of independent vector
fields on K, the one-form on M can be decomposed as a sum

A(X) = a Aa(X) ea .                                                          (2.2)

The real-valued coefficients Aa(X) are the traditional gauge fields on M . For general
submersion metrics on P , this can be an infinite sum, with {ea} being a basis of the full
space of vector fields on K, which is the Lie algebra of the diffeomorphism group Diff(K).
The gauge group need not act on K only through isometries of gK.

    The curvature FA is a two-form on M with values in the Lie algebra of vector fields

                             8
on K. It can be defined by

                    FA(X, Y ) := (dM Aa)(X, Y ) ea + Aa(X) Ab(Y ) [ea, eb] ,      (2.3)

where the last term is just the Lie bracket [A(X), A(Y )] of vector fields on K.
    The tangent bundle of P has two natural decompositions:

                            TP = TM TK = HV .                                     (2.4)

Here V := T K is the vertical subbundle while its orthogonal complement, H := (T K),
is the horizontal subbundle. So a tangent vector w  T P can be decomposed in two
different ways, w = wM + wK = wH + wV . The relation between them is

wV = wK - A(wM )            wH = wM + A(wM ) .                                    (2.5)

The information contained in the gauge one-form A on M is equivalent to the information
contained in the horizontal distribution H  T P .

    One can construct local, gP -orthonormal trivializations of T P using only horizontal
and vertical vectors. They can take the form {X�H, vj}. Here the vj form an orthonormal
basis of T K with respect to gK(x), for each x  M . The X� form a gM -orthonormal basis
of T M . The horizontal lift of X� to P is denoted X�H. It is given by

                            X�H = X� + Aa(X�) ea .                                (2.6)

Such horizontal lifts are called basic vector fields on P [43, 44].

2.2. Spinors on M4 � K

2.2.1. Horizontal and vertical spinors

The conventions for spinor geometry used in this paper are described in appendix A. In this
section, we recall the specific features pertaining to spinors on Riemannian submersions.
These were investigated in [45�47] and later in [20], for example. Here we use the notation
of [20], which is adapted to the study of Kaluza-Klein physics.

    Locally, spinors on M � K have values on the higher-dimensional spinor space m+k.
This space can be written as the tensor product m  k, where m and k are the
dimensions of M and K. All three spaces have irreducible representations of Clifford
algebras. There is a standard isomorphism between Cl(m + k - 1, 1) and the Z2-graded
tensor product of algebras Cl(m - 1, 1) ^ Cl(k). It is determined by the correspondence

                                                        9
of generators

                             1 = 11                                                            (2.7)
                            � = �  1 for � = 0, . . . , m - 1
                      m-1+j = M  ~j for j = 1, ..., k .

This is a recipe to construct higher-dimensional gamma matrices l from the lower-
dimensional ones. The ~j are Euclidean gamma matrices acting on k and the � are
gamma matrices for the Minkowski metric on M . The complex chirality operators are

                      m-1                                           i  k+1  
                         2                                               2
M              :=  i          0  ���  m-1                 K  :=               ~1  �  �  �  ~k

P              :=  i  m+k-1      0 1 � � � m+k-1  =   (M )k+1  K ,                             (2.8)
                           2

where s denotes the integral part of s. They are normalized so that their square is the
identity operator on the respective spinor spaces m, k and m+k.

    Assume that T K has a topological spin structure in the sense of [58], so a double
cover of its oriented frame bundle. Together with the trivial spin structure on the con-
tractible M , it determines topological spin structures on T P and on the horizontal and
vertical bundles in decomposition (2.4). The metric gP then determines subordinate spin
structures in the usual sense of [59], so double covers of the oriented, orthonormal frame
bundles of T P , V and H. We fix those structures for the rest of the paper.

    Given an oriented, real vector bundle E with a metric and spin structure, its complex
spinor bundle is denoted S(E). For a tangent bundle, the notation is simplified as in
S(T P ) = S(P ) = SgP . Sections of S(H) are called horizontal spinors over P , while
sections of S(V ) are the vertical spinors. Calling  the projection from P to M , there
are natural isomorphisms

                              S(H)  S((T M ))  [S(M )] .                                       (2.9)

In particular, a spinor  on M has a unique lift as a horizontal spinor on P . It coincides
with the pullback  under this isomorphism. It is denoted H and is called the basic lift
of  to P . At the same time, if we fix a point x  M and consider the fibre Kx := {x}�K
inside P with its metric gK(x), there is a natural isomorphism between the restriction of
S(V ) to Kx and the spinor bundle of the fibre,

                                      S(V ) |Kx  S(Kx) .                                       (2.10)

                                                  10
Overall, since M is even-dimensional, there is a natural isomorphism of spinor bundles

S(P )  S(H)  S(V )                    (2.11)

that is compatible with the Clifford multiplication implied by (2.7), in the sense that

  U � (H  ) = (M )H  (U � )           (2.12)
XH � (H  ) = (X � )H   .

Here U is any vertical vector field on P . It is regarded as such on the left-hand side and
as a section of V on the right-hand side. As before, X is any vector in T M and XH
denotes its basic lift to P , as in (2.6).

    Since M is contractible, its spinor bundle S(M ) is trivial. Due to (2.9), so is S(H) as
a bundle over P . This implies that a spinor  on P can always be written as a sum

          2  m  
             2
(x, y) =          Hb (x)  b(x, y)  ,  (2.13)
          b=1

where m is the dimension of M , the b are Dirac spinors on M and the b are vertical
spinors on P . Here x and y denote coordinates on M and K, respectively. When K is

compact, the vertical spinors over a fibre {x} � K can always be written as a (possibly
infinite) sum of eigenspinors of the internal Dirac operator D/ K. Since the metric gK
depends on x, the operator D/ K and its eigenspinors will also change along M , in general.

    Now suppose that the internal metric gK(x) is independent of x. Then an L2-
orthonormal basis of eigenspinors {(y)} on K can be chosen uniformly over M . So
we can take each b in (2.13) and expand its y-dependence as b(x, y) =  cb(x) (y).
Inserting this into (2.13), it is clear that the higher-dimensional spinor can then be written

as a (possibly infinite) sum

(x, y) =  H(x)  (y) .                 (2.14)

Here the  are Dirac spinors on M , the H are their horizontal lifts to P , and the 
are eigenspinors of D/ K independent of the point on M .

2.3. Decomposing the higher-dimensional Dirac operator

The decomposition of spinors on P into a tensor product of horizontal and vertical parts, as
in (2.11), leads to a decomposition of the Levi-Civita connection and the Dirac operator on
P . See [20,47]. To describe it, take an oriented, orthonormal trivialization of T P adapted

                11
to the submersion metric gP  (gM , A, gK). As in section 2.1, this means a trivialization
{X�H, vj} formed by basic and vertical vector fields on P . Then the following formula was
obtained in [20], developing previous work in [45�47].

Proposition 2.1. Consider a spinor on P of the form  = H(x)  (x, y), as in (2.13).
The action of the higher-dimensional Dirac operator on  can be locally decomposed as

D/ P   = gM� (X� � M )H     +  gM� Aa (X� � )H            1
                                                  Lea + 2 div(ea) 

       +    (M )H  D/ K  +  1  (FAa)� (X� � X � M )H  (ea � )            (2.15)
                            8

       + gM� (X� � )H            1  X log  |gK |  
                         X + 2

       + gM� (X� � )H    1     ij gP ([X, vi], vj) - gP ([X, vj], vi) vi � vj �  .
                         8

Here Lea denotes the derivative (1.3) of spinors on K; div(ea) denotes the divergence of
the internal vector field ea with respect to gK; and |gK| is the modulus of the determinant
of the matrix representing gK in a fixed coordinate system on K.

    Formula (2.15) is simpler in regions where the Higgs-like scalars are constant, i.e.
where the internal metric gK does not change along M . In this case [X�, vi] = 0 and
every higher-dimensional spinor can be expressed as a sum of simpler tensor products of
the form (x)H  (y), as in (2.14). In this simpler setting, we have:

Corollary 2.2. In regions where gK is constant along M , the action of the Dirac operator
on a spinor of the form (x)H  (y) can be decomposed as

D/ P (H  )  =  gM� (X� � M )H       +  gM� Aa (X� � )H           1
                                                         Lea + 2 div(ea) 

               +  (M )H  D/ K  +    1  (FAa)� (X� � X � M )H  (ea � ) .  (2.16)
                                    8

    This expression is valid for a general gauge one-form A� = A�a ea on M with values
in the space of vector fields on K. Be they Killing or non-Killing with respect to gK.
The first term on the right-hand side contains the Dirac operator on M . The second
term determines the couplings between gauge fields and fermions. The term with the
internal Dirac operator D/ K generates mass terms for fermions on M . The last term is a
Pauli-type coupling between the gauge field strength and spinors. It is a standard feature
in Kaluza-Klein dimensional reductions. The dimensional reduction of (2.16) to M will
be discussed in section 7.

                                    12
Remark 2.1. Consider the operator on spinors over P defined by the Pauli term,

C(H  )  :=  1  (FAa)� (X� � X � M )H  (ea � ) .                                 (2.17)
            8

It is algebraic and anti-self-adjoint with respect to the pairing �, � of spinors. Thus, the
modified operator D/ P - C retains most of the useful properties of D/ P , such as ellipticity,

anti-self-adjointness with respect to �, �, and the implicit coupling of 4D gauge fields

to spinors through the Kosmann-Lichnerowicz derivative. So one could also consider
(D/ P - C) = 0 as a candidate for the physical equation of motion for spinors on P . An

important conceptual disadvantage of the modified operator, however, is that it is defined

only for submersion metrics of the form gP  (gM , A, gK), not for general metrics on P .

3. Spinor symmetries on M � K induced by reflections
      and parity transformations on M

Let the spacetime P = M � K be equipped with a submersion metric gP equivalent to a
triple (gM , A, gK), as in the previous section. Reflections and parity transformations on
Minkowski space admit natural extensions to diffeomorphisms of P that leave the internal
coordinates unchanged. The extended diffeomorphisms, however, are not isometries of
the submersion metric. The transformation rules of gP under those diffeomorphisms
encapsulate the usual transformation rules of 4D gauge fields A�a and Higgs-like fields
under reflections and parity inversions.

    Now suppose that P has a fixed orientation and topological spin structure. The diffeo-
morphisms of P induced by reflections and parity inversions determine transformations of
the higher-dimensional spinor fields, as we will see. But the construction of spinor bundles
depends on the background metric, and gP is not preserved by those diffeomorphisms.
So reflections and parity inversions will relate spinors defined on different bundles over
P . This is slightly different from the usual 4D story, in which those transformations are
isometries of gM , and hence define automorphisms of the same 4D spinor bundle. Despite
this difference, the Kaluza-Klein extensions of reflections and parity inversions still induce
symmetries of the higher-dimensional Dirac equation D/ P  = 0. This is the main point
for us. The purpose of this section is to describe these matters concisely. It spells out the
main properties of the spinor transformations on P corresponding to those symmetries.
To our knowledge, the extension of the analyses in [9, 10] to our type of KK models, with
general submersion metrics and transformations between different spinor bundles, has not
been described previously in the literature.

               13
Reflections of a single coordinate

Let M be an even-dimensional Minkowski space and R : M  M denote the reflection
diffeomorphism that changes the sign of the -th canonical coordinate. We denote by the
same symbol its natural extension to a diffeomorphism of P . If gP is a submersion metric
on P equivalent to the triple (gM , A, gK), then the pullback tensor RgP is a submersion
metric equivalent to the triple (gM , RA, RgK). Note that reflections are isometries of
the Minkowski metric gM . The extended diffeomorphism R : P  P can also be used to
pushforward vector fields W on P , which are denoted RW .

    Now assume that P has a fixed orientation and topological spin structure, as in section
2.2.1 and appendix A. The metrics gP and RgP determine two distinct spinor bundles
over P , denoted SgP and SRgP , respectively. Then the diffeomorphism R can be lifted to
a map of spinors described in the following proposition.

Proposition 3.1. Given a submersion metric gP on P , there exists a C-linear map of
higher-dimensional spinors, denoted R : (SgP )  (SRgP ), with the following properties:

                     R(f ) = (Rf ) R()                                       (3.1)
                                                                             (3.2)
                     R  R() =                                                (3.3)
                                                                             (3.4)
                     R(W � ) = - (RW ) � R()

                     R(gWP )  =     RgP    [R()]
                                       RW

for all spinors   (SgP ), all functions f  C(P ; C), all vector fields W on P , and for
some phase   U(1). This map is unique up to multiplication by a constant phase.

    In the second equality, we have used the identity RRgP = gP to regard R  R as
an automorphism of SgP . The third equality is a compatibility relation between spinor
reflections and Clifford multiplication. The last equality is a relation between reflections

and the lifted Levi-Civita connections on the spinor bundles SgP and SRgP .

The existence and uniqueness of these maps of higher-dimensional spinors is proved

in appendix 3. Here we only mention that, in appropriately chosen trivializations of the

bundles SgP and SRgP over a domain M � U inside M � K, the representative of the

spinor  is a function U : M � U  m+k, and the representative of the reflected spinor

R() is the function

                     (R)U (x, y) = ei  U (R(x), y) .                         (3.5)

Here (x, y) are the coordinates on M � U; the reflection R(x) acts on x  M by changing
the sign of the coordinate x; the factor ei is a fixed complex phase; and  is the gamma
matrix on spinor space m+k corresponding to the coordinate x on M . The local formula

                                    14
(3.5) extends the most common convention for reflections on 4D Minkowski space [49,60].2
Part of the existence proof is to choose and establish the consistency of the trivializations
of T P , SgP and SRgP where this local formula applies. In this process, one should insist
on choosing trivializations consistent with the fixed initial orientation of P , even though
the reflection diffeomorphism inverts that orientation.

    Denote by D/ gP and D/ RgP the standard Dirac operators on SgP and SRgP . Denote by
P the chirality operators both on SgP and SRgP , as defined on (2.8). Then appendix 3
also shows that:

Proposition 3.2. The maps of spinors described in proposition 3.1 satisfy:  (3.6)
                                                                            (3.7)
                                    R (D/ gP ) = - D/ RgP (R )              (3.8)
                                     R (P ) = (-1)k+1 P (R )
                                R 1, R 2 = - (gM ) 1, 2  R

for all spinors   (SgP ). Here k denotes the dimension of K, the inner product of
spinors �, � is defined in (A.3), and  is the index of the reflected coordinate in M .

    The first identity implies that if  is in the kernel of D/ gP , then the reflected spinor
R() is in the kernel of D/ RgP . In this sense, reflections are a symmetry of the higher-
dimensional massless Dirac equation. The second identity shows that spinor reflections are
a symmetry of the Weyl equation only when K is odd-dimensional. The third identity
shows that a reflection will preserve or not the inner product of spinors depending on
whether the reflected coordinate is spacelike or timelike.

 Parity transformations

 Let M be an even-dimensional Minkowski space and P : M  M denote the parity
 diffeomorphism that changes the sign of all spatial coordinates. The extension of this
 diffeomorphism to P is denoted by the same symbol. If gP is a submersion metric on P
 equivalent to the triple (gM , A, gK), then the pullback tensor PgP is a submersion metric
 equivalent to the triple (gM , PA, PgK). The extended diffeomorphism P : P  P can
 also be used to pushforward vector fields W on P , which are denoted PW .

     Assume that P has a fixed orientation and topological spin structure, as in section
 2.2.1 and appendix A. The metrics gP and PgP determine two distinct spinor bundles

2A factor P could be inserted in (3.5). Then identities (3.3), (3.6) and (3.8) would appear with a flipped
 sign for even-dimensional K.

                                                         15
over P , denoted SgP and SPgP , respectively. Then the diffeomorphism P can be lifted to
a map of spinors described in the following proposition.

Proposition 3.3. Given a submersion metric gP on P , there exists a C-linear map of
higher-dimensional spinors, denoted P : (SgP )  (SPgP ), with the following properties:

                      P(f ) = (Pf ) P()              (3.9)
                                                    (3.10)
                      P  P() =                      (3.11)
                                                    (3.12)
                      P(W � ) = - (PW ) � P()

                      P(gWP )  =  P  gP  [P ()]
                                     PW

for all spinors   (SgP ), all functions f  C(P ; C), all vector fields W  (T P ), and
for some phase   U(1). This map is unique up to multiplication by a constant phase.

The parity diffeomorphism of M can be written as a sequence of reflections of the

spatial coordinates,

                      P(x) = R1 � � � Rm-1(x) .     (3.13)

Using the properties of reflections stated in proposition 3.1, one can easily verify that
maps of spinors of the form

                      P() := ei R1 � � � Rm-1       (3.14)

satisfy all the properties of parity maps, as stated in proposition 3.3. This proves the
existence part of proposition 3.3. The uniqueness part can be proved in a way entirely
analogous to the proof of proposition 3.1. In appropriately chosen trivializations of the
spinor bundles SgP and SPgP over a domain M � U , as in the discussion leading to (3.5),
the local formula for the spinor parity transformations is

(P)U (x, y) = ei[+(m-1)] 1 � � � m-1 U (P(x), y) .  (3.15)

Here the l are gamma matrices on m+k corresponding to the spacelike directions in M ,
as in (2.7). We note that after dimensional reduction and the redefinition of 4D spinors
stated in (7.4) -- which is necessary to bring the 4D Dirac equation to its traditional form
-- the 4D component of parity inversion acts through multiplication of the 4D spinor by
0 only, as in the usual prescription. See (7.7).

    Using (3.14) and the properties of reflections stated in proposition 3.2, one can also
verify directly that:

                                  16
Proposition 3.4. The maps of spinors described in proposition 3.3 satisfy:  (3.16)
                                                                            (3.17)
                                       P (D/ gP ) = - D/ PgP (P )           (3.18)
                                        P (P ) = (-1)k+1 P (P )
                                   P 1, P 2 = - 1, 2  P

for all spinors   (SgP ). Here k denotes the dimension of K and �, � is the inner
product of spinors defined in (A.3).

    These identities imply that parity transformations are always a symmetry of the Dirac
equation. They are a symmetry of the Weyl equation only for odd-dimensional K. They
preserve the inner product of spinors only for even-dimensional K.

4. Conjugation symmetries on spinor bundles

This section gives a succinct account of conjugation automorphisms of spinor bundles in
arbitrary signature (s, t). It describes the essential properties of these symmetries of the
massless Dirac equation. It adopts a geometric approach and hides the basis-dependent
constructions, with gamma matrices in special representations, that are generally used
to prove the existence of the maps. The vector bundle conjugation maps are a modest
extension of the vector space version, described in appendix A using the traditional Ma-
jorana forms. The bundle version includes the relations of conjugations with covariant
derivatives, the Kosmann-Lichnerowicz derivative and the Dirac operator. Conjugation
maps in arbitrary signatures are well studied. See [49, 51, 52], for instance. The purpose
of this section is to provide a short and hopefully clean summary that covers the general
signatures and the bundle-related properties. At the end, it also describes results that
help to understand conjugation maps in the specific setting of Riemannian submersions
and their relations with reflections and parity transformations.

    Let P be a general oriented, connected manifold equipped with a metric of signature
(s, t) and a spin structure. Let  denote the Levi-Civita connection on T P and also its
lift to the complex spinor bundle SgP . Define the sets


Hs,t  :=  {-1, 1}          if s - t is even                                 (4.1)

          {(-1)  s-t+1  }  if s - t is odd .
                     2

Proposition 4.1. For each value   Hs,t, there exists a conjugate-linear automorphism

                   17
of spinors, denoted j : (SgP )  (SgP ), with the following properties:

j(1 + f 2) = j(1) + f j(2)                                                    (4.2)
                                                                              (4.3)
j(V � ) =  V � j()                                                            (4.4)
                                                                              (4.5)


            (-1)  s-t      (-)  s-t    if s - t is even
                    4             2    if s - t is odd

jj() =      (-1)  (s-t)2 -1

                       8     


j(V ) = V (j )

for all spinors   (SgP ), all functions f  C(P ; C) and all vector fields V on P . This
automorphism is unique up to multiplication by a constant complex phase.

    A conjugation map with jj = 1 is called a real structure on the spinor bundle.
It allows the consistent imposition of the Majorana condition on spinors, j() = .
A conjugation with jj = -1 is called a quaternionic (or pseudo-real) structure on
SgP . It determines an action of the quaternions on spinors through the representation
(i, j, k)  (i, j, i j). The sign  tells us whether j commutes or anticommutes with
Clifford multiplication and the Dirac operator.

    Let LV  denote the Kosmann-Lichnerowicz derivative of the spinor  along the vector
field V . Let D/ denote the standard Dirac operator on SgP . Let P denote the complex
chirality operator on SgP , normalized so that P P = 1. Then we have:

Proposition 4.2. The automorphisms of proposition 4.1 have the additional properties:

j(LV ) = LV (j)                                                               (4.6)
                                                                              (4.7)
j(D/ ) =  D/ (j )                                                             (4.8)
                                                                              (4.9)


            (-1)  s-t  P j()         if s - t is even
                    2                if s - t is odd

j(P )  =

            P  j ( )


j-() =  P j+()                       if s - t is even .

for all spinors   (SgP ), all vector fields V on P , and some phase   U (1).

    Thus, conjugation maps are always symmetries of the Dirac equation D/  = 0. They
preserve the condition P  =  in all signatures except s - t = 2 (mod 4).

    It is also possible to write useful relations between the conjugation maps j and the
spinor inner products defined by (A.3). These relations follow directly from lemma A.4
and property (4.7).

                       18
Proposition 4.3. The maps j satisfy:


                                                  t(s+1)
            j 1, j 2          =                           t   1,  2     if s - t is even           (4.10)
                                 (-1) 2                                 if s - t is odd            (4.11)

                                 (-1)  st  1,                 2
                                       2


                                                  t(s+1)
            j 1, D/ j 2       =                           t+1  1,   D/  2     if s - t is even
                                 (-1) 2                                       if s - t is odd

                                 (-1)  st+s-t+1               1,  D/ 2
                                              2

for all spinors 1, 2  (SgP ) and for the inner product in (A.3).

    Now suppose that the tangent bundle of P decomposes as a sum of two orthogonal
subbundles, T P = E1E2. Assume that the metric inherited by El is non-degenerate with
signature (sl, tl). Choose orientations on the summands El compatible with the orientation
of T P . If one of the subbundles has even rank, we have an isomorphism of spinor bundles
SgP  S(E1)  S(E2). There is also an inherited Clifford multiplication of vector fields in
El and spinors in S(El). In these conditions, the conjugation automorphisms of SgP can
be reconstructed using the conjugations in the two factors S(El).

Proposition 4.4. Choose a sign   Hs,t. When E1 has even rank, the conjugation
automorphism j of proposition 4.1 can be decomposed as

                                   j = j1  j2                                                      (4.12)

under  the  isomorphism  SgP   S(E1)  S(E2).                  Here  we  have  defined     =  (-1)  s1 -t1  .  It
                                                                                                       2

can be checked that   Hs2,t2.

Composition of conjugations and parity transformations

Suppose now that P is a spacetime of the form M � K, where M is an even-dimensional
Minkowski space. As discussed in section 3, reflections and parity inversions on M extend
to diffeomorphisms of P that can be lifted to transformations of spinors over P . One can
verify that those transformations commute with conjugations of spinors, essentially.

Lemma 4.5. Fix the sign  and the corresponding conjugate-linear automorphisms j of
SgP , SRgP and SPgP . For phase choices in definitions (3.5) and (3.14) satisfying e2i = 
and e2i = 1, all spinor reflections and parity transformations commute with j.

    Choosing such a value for the phase of P, we now consider the composed maps j P =
P j between spinors in SgP and spinors in SPgP .

                                                          19
Proposition 4.6. The composed maps jP satisfy:

jP (D/ ) = -  D/ (jP )                                                   (4.13)
                                                                         (4.14)
                                                                         (4.15)

                             (-1)  m+k    P (jP )   if k is even
                                      2

jP (P )     =

                             P  (j P      )         if k is odd


                           (-1)  m+k+2       1,  2  if k is even
                                      2             if k is odd

jP 1, jP 2  =                    m+k+1
                                      2
                           (-1)           1,    2

for all spinors 1, 2  (SgP ) and for the inner product in (A.3).

    Thus, the transformations jP are always symmetries of the Dirac equation D/  = 0
in higher dimensions. They also preserve the Weyl condition P  =  except when
m + k = 2 (mod 4). That condition is usually imposed in Kaluza-Klein models with
even-dimensional K in order to obtain a correlation between the Minkowski and internal
chiralities of spinors, as described in [20, 22].

5. Actions of compact groups on K and its spinors

Lie derivatives of spinors along fundamental vector fields

Let K be an orientable, connected manifold with a fixed topological spin structure. For
any given Riemannian metric g on K, we have the complex spinor bundle Sg  K. For
any vector field V on K, the Kosmann-Lichnerowicz derivative LV acts on sections of
that bundle as in (1.3). It satisfies the formula

( [LU , LV ] - L[U,V ] )   = 1 girgjsgkl  (LU g)(vr, vk) (LV g)(vs, vl)  (5.1)
                              4

                           - (LU g)(vs, vk) (LV g)(vr, vl) vi � vj �  .

So the closure relation [LU , LV ] = L[U,V ] is satisfied when U or V are conformal Killing
with respect to g, but not in general [54]. In this section we show that, when a compact
group acts on K, there is a natural modification of the Kosmann-Lichnerowicz derivative
that satisfies the closure relation for all fundamental vector fields of the action. Even if
they are not conformal Killing.

    Let G be a compact, connected Lie group. Suppose that G acts on K on the left
through diffeomorphisms that preserve the orientation and the topological spin structure,
but not necessarily the metric g. Denote by g the Lie algebra of fundamental vector fields

                                 20
on K induced by the G-action. These need not be Killing or conformal Killing vector
fields with respect to g. Then we have the following result:

Proposition 5.1. There are natural derivatives of spinors, LV : (Sg)  (Sg), with

       LU+V  = LU  +  LV                                                       (5.2)
LV (1 + f 2) = LV 1 + f LV 2 + (df )(V ) 2                                     (5.3)
                                                                               (5.4)
    LV 1, 2 = LV 1, 2 + 1, LV 2

for all vector fields U and V on K, all   R and f  C(K, C), that also satisfy

[LU , LV ]  = L[U,V ]                                                          (5.5)

when U or V are fundamental fields in g. The operator LV coincides with the Kosmann-
Lichnerowicz derivative when V  g is conformal Killing with respect to g.

    The derivatives LV define a representation of the Lie algebra g on the space of spinors
(Sg). They can be constructed as follows. Define the auxiliary, average metric

g^(U, V ) :=      (rhg)(U, V ) volG .                                          (5.6)

              hG

Here rh is the diffeomorphism K corresponding to h and volG denotes the bi-invariant,
normalized, Haar measure on G. Then g^ is a G-invariant metric on K. All the vector
fields in g are Killing with respect to g^. Thus, denoting L^V the Kosmann-Lichnerowicz
derivative on S^g, it follows from (5.1) applied to g^ that

[ L^U , L^V ] = L^[U,V ] ,                                                     (5.7)

as operators on g^-spinors, when U or V are in g. So these operators satisfy the desired
closure relation, but on the wrong spinor bundle. We have to transport them back to Sg.

    Now, there exists a unique smooth automorphism  : T K  T K that projects to the
identity on K, is positive-definite, and satisfies

g((U ), V ) = g(U, (V ))                                                       (5.8)
    g^(U, V ) = g(-1(U ), -1(V ))                                              (5.9)

for all vector fields U and V on K. This map lifts to an automorphism of spinor bundles
 : Sg  S^g, which we denote by the same symbol. See [55, 56] and appendix B. Then we

              21
define

                                      LV  := -1  L^V  () .                        (5.10)

Due to (5.7), it is clear that the derivatives LV satisfy the closure relation (5.5) on Sg for
all vector fields in g. Using formula (B.12) of appendix B, we also have:

Proposition 5.2. The derivatives LV and LV of spinors in Sg are related by

                 LV     =     LV      +  1        g  -1(LV )(vj), vk  vj � vk �   (5.11)
                                         4
                                            j= k

for all vector fields V on K. Here LV  denotes the standard Lie derivative of .

The two operators coincide when V is conformal Killing. Their first variations also agree
when V is close to being conformal Killing. This follows from proposition B.1 and (B.26).

Remark 5.1. When K is not compact, the average of the metric g with respect to a

maximal compact group acting on K is not necessarily a metric g^ with maximal isometry

group, or with maximal Killing algebra. For example, when K = Rn, it is better to take g^

to be the Euclidean metric. Then the transport of the Kosmann-Lichnerowicz derivative

L^V  =  V  -  1  (j Vk  -kVj  )^j ^k  through the map , as in (5.10), gives us a spinor derivative
              8

on (Rn, g) that satisfies the closure relation for all vector fields induced by the action of

the Euclidean conformal group on Rn.

6. Representation spaces versus D/ -eigenspaces

Spinorial representation spaces

The new derivatives LV determine a representation of the Lie algebra of fundamental
G-vector fields on the space of spinors in Sg(K). For non-isometric G-actions, this rep-
resentation does not preserve the eigenspaces of the Dirac operator. In a Kaluza-Klein
model with K as the internal manifold, it couples the 4D massive gauge fields to fermions.
This coupling can mix fermions with different masses and allows chiral interactions [20].

Proposition 6.1. The map  : g � (Sg)  (Sg) given by

                                                       1                          (6.1)
                              V () := LV  + 2 divg(V ) 

defines a unitary representation of the Lie algebra g on the space of complex spinors
equipped with its natural L2 Hermitian product.

                                                     22
    Now consider the Dirac operator D/ on Sg. When K is compact, the space of L2-
integrable spinors can be decomposed as an infinite, orthogonal sum of D/ -eigenspaces,

L2(Sg) =          Em .                                                    (6.2)

              mZ

When the dimension of K is not 3 (mod 4), the spectrum of D/ is symmetric and the
eigenvalues associated to Em satisfy �(-m) = -�(m) [61]. The D/ -eigenspaces Em are
not preserved by  and the derivatives LV , in general. When G does not act on K through
isometries, (B.15) implies that V does not commute with D/ .

    Nevertheless, it is possible to define a second decomposition of the space of spinors as
a sum of finite-dimensional, complex spaces on which g acts irreducibly through . These
are the G-representation spaces Wm,. They are defined by taking decomposition (6.2)
for the spinors of the averaged metric g^; decomposing the D/^g-eigenspaces into irreducible
subspaces E^m,; and then transporting these subspaces back to Sg through the map .
So Wm, = -1(E^m,). This is explained in appendix D, which contains all the proofs for
this section.

Proposition 6.2. When K is compact, there is an orthogonal decomposition

L2(Sg) =       nm, Wm, ,                                                  (6.3)

          mZ 

preserved by the representation 6.1. Here nm,  N0 and the Wm, are finite-dimensional
spaces of spinors on which the g-representation (6.1) is equivalent to the irreducible rep-
resentation . If G acts on K isometrically, and hence preserves the D/ -eigenspaces in
(6.2), the representation spaces can be chosen so that Wm,  Em.

Remark 6.1. In (6.3), the sum  ranges over all inequivalent irreducible representations
of the compact Lie algebra g. The non-negative integers nm, are the multiplicities of the
representations. For any fixed value of m, only a finite number of them are non-zero as
 varies. The representations Wm, may be real, complex or quaternionic type. For the
complex ones, one can guarantee that nm, = nm, when the dimension of K is not 1 (mod
4). The real representations appear with even multiplicity when K has dimension 3, 4, 6
(mod 8). The quaternionic ones appear with even multiplicity when K has dimension 0,
2, 7 (mod 8). All this is justified in appendix D.

    When the manifold K is even-dimensional, this decomposition of the space of spinors
can be organized differently. We can use the splitting Sg = Sg+  Sg- and require the
representation spaces to be made of Weyl spinors. So we get a third decomposition:

          23
Proposition 6.3. When K is compact and even-dimensional, there is an orthogonal

decomposition

               L2(Sg) =               nm, (Wm+,  Wm-,) ,  (6.4)

                         mN0 

preserved by the representation (6.1). Here nm,  N0 and the Wm�, are finite-dimensional
spaces of Weyl spinors on which the g-representation (6.1) is equivalent to the irreducible

representation . If G acts on K isometrically, the representation spaces can be chosen

so that W0�,  E0 and, for all m > 0,

               Wm+,  Wm-, = Em,  E-m,                     (6.5)

where E�m, is a subspace of E�m on which g acts irreducibly through .

Remark 6.2. As before, in (6.4) the sum  ranges over all inequivalent irreducible g-
representations. For fixed m, only a finite number of multiplicities nm, are non-zero as
 varies. For the representations of complex type, one can again guarantee that nm, =
nm,. When the dimension of K is 0 (mod 8), the multiplicity nm, of any quaternionic
representation  must be even. When the dimension of K is 4 (mod 8), the multiplicity
nm, of any real representation  must be even. The proof of this is in appendix D.

    The observation below helps to interpret the effect of conjugations on spinors. It
will be useful in the KK setting (see remark 7.4). It extends well-known properties of
conjugations on finite-dimensional vector spaces. It is proved in appendix D.

Lemma 6.4. There exists an L2-orthonormal basis {} of spinors in Sg satisfying:

1) Each spinor  belongs to one of the irreducible representation spaces Wm, in (6.3),
    when k is odd, and to one of the irreducible spaces Wm�, in (6.4), when k is even.

2) The conjugation maps j may preserve some basis spinors, up to a phase, and
    otherwise will swap them in pairs and multiply them by phases.

Chiral fermions and local gauge anomalies

Consider the case of even-dimensional K. In decomposition (6.4), the chiral subspaces
Wm+, and Wm-, transform under the same g-representation and appear with the same
multiplicity nm,. So the Lie algebra g acts isomorphically on the two big spaces of Weyl
spinors, L2(Sg+) and L2(Sg-). However, this does not imply that g acts identically on the
two chiral components of any given D/ -eigenspinor,  = + + -. Just as in [20], a simple

                                      24
calculation using the properties of D/ and K yields

K   , [D/, V ] K  volg = (� + �)  +, V +  -  -, V -  volg . (6.6)
   K

Here  and  are two D/ -eigenspinors with positive eigenvalues � and �. When the G-
action on K is non-isometric, the commutator [D/, V ] is in general non-zero, as follows
from (B.15). So we should have different matrix elements  +, V + L2 =  -, V - L2.
In contrast, when G acts on K through isometries, we have V = LV and [D/, V ] = 0.
So the g-action on D/ -eigenspinors cannot have chiral asymmetries. A detailed discussion
of the appearance of chiral couplings for non-isometric actions on K is given in [20].

    Note that although Wm+, and Wm-, transform under the same gauge representation,
for non-isometric actions the two spaces can be spanned by D/ -eigenspinors with different
eigenvalues, or by distinct linear combinations of D/ -eigenspinors with different eigenval-
ues. How would these variations be perceived in 4D, in a KK model with internal space K?
For example, as in the Standard Model, suppose that we have light fermions interacting
with a force only through the left-handed chiral components. These variations suggest
the existence of fermions interacting similarly with that force through the right-handed
components, but allow them to be heavy fermions. They need not have the same mass.

    Remark 6.2 says that we always have an equality of multiplicities nm, = nm, in
decomposition (6.4). In particular, inside each chiral subspace Wm� =  nm, Wm�,, the
irreducible representations of complex type always appear in conjugate pairs. This has
useful consequences in our Kaluza-Klein models with internal space K. It guarantees that
the chiral interactions of 4D fermions generated by the g-representation  are free of local
gauge anomalies [50, sec. 75]. It does not say anything about the interactions generated
by the higher order correction terms ea in the Dirac equations (7.5).

Group representations and fermion generations

The irreducible representations of the Lie algebra g on the finite-dimensional spaces of
spinors Wm, and Wm�, can be integrated to representations of a covering group G~ of G
on the same spaces. So we obtain a lift of non-isometric G-actions on K (preserving the
topological spin structure) to unitary G~-representations on the space of spinors on K.
This lift seems to be new and extends the usual one for isometric actions.

    The elements in the kernel of the covering G~  G act trivially on K, but may act non-
trivially on its spinors. When the compact group G is semisimple, the cover G~ is compact
semisimple as well. In this case, the centre of G~ is a finite subgroup, and so is the kernel
of the covering map. Now let g  g be the subalgebra of fundamental Killing fields

      25
on K. Assume that it is semisimple. Let G~  G~ be the corresponding exponentiated
subgroup. The Dirac operator on K commutes with the infinitesimal transformations
V when V  g is Killing. So it also commutes with the exponentiated transformations
determined by the elements of G~.

    An intriguing point about the lifts to spinors of non-isometric actions on K is the
following. Any element in the centre of G~ defines a transformation of spinors that com-
mutes with the infinitesimal gauge transformations V , for all V  g. However, some
of these central elements may lie outside the subgroup G~. So the corresponding spinor
transformations need not commute with the Dirac operator on K. Therefore, in the
Kaluza-Klein model on M � K, and assuming that G is semisimple, we get a finite set of
transformations that permute 4D fermions with the same g-representations but with pos-
sibly different masses. The 4D fermions permuted by such transformations are potential
candidates to model different generations of the same type of particle.

    We use the expression potential candidates because we have not demonstrated that
this mechanism works effectively in practice. Only that it could work. One needs to
verify that the proposed transformations really do not commute with D/ . Moreover, there
may exist other mechanisms that also produce fermion generations in KK. It would be
useful to study explicit examples on this topic.

    For instance, take the case where K is the group manifold SU(3) equipped with a
left-invariant metric. Then G is the maximal compact group (SU(3) � SU(3))/Z3 acting
effectively on K. The action is not isometric. The universal cover G~ is SU(3)�SU(3). The
centre of G~ is Z3 � Z3. The first Z3 factor lies inside G~, because the metric on K is left-
invariant. So it determines spinor transformations that commute with the Dirac operator
on K. The second Z3 factor generally lies outside G~. So we get a Z3 of transformations
that permute spinors in the same g-representations but with potentially different D/ -
eigenvalues. It would be interesting to verify this explicitly.

7. Dimensionally reduced equations and CP violation

7.1. Dimensional reduction of the Dirac equation on M4 � K

In this section, we take M to be 4D Minkowski space. For simplicity, we also assume
that the submersion metric gP  (gM , A, gK) has constant internal geometry. So the
metric gK is constant along M . After the work in sections 5 and 6, the action of the

                                                       26
higher-dimensional Dirac operator (2.16) on a spinor H   can be written as

D/ P (H  ) = gM� (X� � M  )H   + gM� Aa (X� � )H  [ (ea + ea)  ]

+  (M )H  D/ K          +     1  (FAa)� (X� � X � M )H  (ea � ) .                   (7.1)
                              8

Here ea() is a unitary representation of the gauge algebra g on the space of internal
spinors, as defined in (6.1). The term ea() is the non-minimal coupling

ea ()  =      1         g  -1(Lea)(vj), vk  vj � vk �                               (7.2)
           -
                 j= k
              4

that emerged in (5.10) and (5.11). From proposition B.1, we know that it vanishes when

the internal vector field ea is conformal Killing for the metric gK. In fact, even the first
variation of ea() vanishes when ea is close to being conformal Killing, as shown by
(B.26). Thus, we expect this non-minimal coupling to be very small for gauge fields A�a
with small mass, for which the Lie derivatives LeagK appearing in (1.2) are small.

    Now take a general higher-dimensional spinor and write it in the form  =  ~H (x)
(y), as in (2.14). The internal spinors {} are all independent and form a L2-

orthonormal basis of the space of sections of SgK . Thus, decomposition (7.1) implies
that the equation D/ P  = 0 over P is equivalent to an infinite set of equations over M4
for the 4D spinors ~. These equations read

� XM� ~ + A�a   , (ea + ea) L2 ~ +   , D/ K  L2 5 ~

                     +     1  (FAa)�  , ea  � L2  �     5 ~                   = 0,  (7.3)
                           8

where we sum over  and use the traditional � notation. When  is an eigenspinor of
D/ K with eigenvalue m, the 4D equations (7.3) are similar to, but not identical to, the

usual gauged Dirac equations. Besides the non-minimal coupling ea and the Pauli term,
they have extra 5 factors and a non-standard kinetic term. However, denoting

           1
       :=        (I  +  i5)   ~   =  exp (i5/4) ~ ,                                 (7.4)
             2

as in [26, p. 22], it is easy to check that the redefined 4D spinors satisfy

i � XM�  + A�a   , (ea + ea ) L2  +   , D/ K  L2 

                        +     1  (FAa)�  , ea � L2 �                          = 0.  (7.5)
                              8

                              27
So the 5 factors disappear and we get the traditional Dirac kinetic term in Minkowski
space with signature - + ++ and the gamma matrices conventions in appendix A. This
equation is the main result of this section.

Remark 7.1. Let G be a subgroup of G that acts on K through isometries, and let g  g
be its algebra of fundamental Killing fields on K. Then the gauge fields Aa� are massless
and the operators ea and D/ K commute for all ea  g. Thus, as described in section 6, it
is possible to choose a L2-orthonormal, complex basis {} formed by D/ K-eigenspinors
that transform in irreducible representations of G. In other words, it is possible to align
the mass basis and the G-representation basis of the internal spinors. For the non-Killing
vector fields ea in g \ g, which are linked to massive 4D gauge fields, this basis alignment
should not be possible in general.

Remark 7.2. The appearance of a 4D Pauli term is a departure from the prescriptions of
the Standard Model. In the case of the abelian 5D Kaluza-Klein model, this term induces
a correction to the electric dipole moment of the electron. It has been estimated that
the magnitude of the correction is negligible, beyond the reach of current experimental
measurements (e.g. [8, 62]). However, those estimates rely on the assumption that the
higher-dimensional vacuum metric is determined by the simple Einstein-Hilbert action
on P . That assumption should not hold in realistic models. Higher-order corrections
to that action seem necessary to introduce the different mass scales observed in reality.
Also, in certain versions of the model, to stabilize the vacuum metric on P [18]. So the
physical contribution of the Pauli term is not completely clear yet. This term can always
be removed as in remark 2.1, although somewhat artificially.

    Observe that a systematic application of the field redefinition (7.4) also affects how
reflections and parity inversion act on spinors on M4. Denoting by R~M the operator before
the redefinition and by RM the operator after, we have

RM             =  e R~ e i5 -  i  5     =  e i    5   R~M    =     i 5 R~M  =  i ei 5  ,     (7.6)
                      4        4               2
                        M

where the last equality follows from definition (3.5). Similarly, for 4D parity inversion,

PM             =  5e P~ e i -  i  5  =     e i    5  P~M   =    i 5 P~M     =  - ei[+3] 0 ,  (7.7)
                      4        4               2
                     M

where the last equality uses (3.15). The precise phases that appear in these transform-

ations are not essential. The 4D conjugation maps, in contrast, are not affected by the

field redefinition. From (4.8) we know that jM is conjugate-linear and anticommutes with

5, so we have

                  e j e i5M    -  i  5  =         e e j i5-  i  5  M  =     jM .             (7.8)
                      4           4                   4      4     

                                                  28
7.2. The CP-transformed equation in 4D

Conjugations of spinors and parity inversions are exact symmetries of the massless Dirac
equation on M4 � K. So is their composition jP. This was described in sections 3 and
4. So if a higher-dimensional spinor satisfies D/  = 0, we will always have D/ (jP ) = 0
as well. The purpose of this section is to determine how the second equation looks after
dimensional reduction to 4D.

    When the internal metric gK is constant along M4, any higher-dimensional spinor can
be decomposed as  =  ~H(x)  (y), as in (2.14). Here {} is a L2-orthonormal
basis of the space of internal spinors in SgK . Combining proposition (4.4) with the local
formula (3.15) for parity inversions, it is clear that the action of jP on such spinors is

j P () = [jM P~M ~(x)]H  [j-K (y)] .             (7.9)


Here P~M is the raw parity inversion in 4D, before the field redefinition (7.4). Now denote
the CP-transformed spinor in 4D by the abbreviated symbol

~cp := jM P~M ~ .                                (7.10)

Just as was done in (7.3), in the previous section, we can rewrite the higher-dimensional
equation D/ (jP) = 0 as an infinite set of equations for spinors over M4. The only
differences are that we now have ~cp instead of ~, and the internal basis j-K  instead
of . However, identity (4.10) in the Riemannian case, together with the commutation
relations of j with Clifford multiplication and the Dirac operator, imply that

  j-K , D/ K (j-K) L2 = -  j-K , j-K(D/ K ) L2 = -  , D/ K  L2 (7.11)
    j-K , ea � (j-K)L2 = -  j-K , j-K(ea � )L2 = -   , ea � L2 .

Moreover, (4.10) and the fact that j commutes with the internal operators Lea, ea and
ea, produce the third identity

 j-K , (ea + ea )(j-K) L2 =   , (ea + ea ) L2 .  (7.12)

So the same arguments that led to (7.3) now imply that D/ (jP ) = 0 is equivalent to

29
the set of 4D equations

� M X� ~cp + (Ap)a�   , (ea + ea ) L2 ~cp -    , D/ K  L2 5 ~cp

                             -      (FAap )�  , ea � L2 � 5 ~cp      = 0.  (7.13)
                                 8

Here we have used that jP  is a spinor in SPgP , as discussed in section 3, not in the
original bundle SgP . In particular, if the submersion metric gP is equivalent to the triple
(gM , A, gK), with gM the Minkowski metric and gK constant along M4, then the pullback
metric PgP is equivalent to (gM , Ap, gK), where the new connection 1-form is just the
pullback Ap := PA of the original one. Explicitly, it is of course given by

(Ap)a� |x := (-1)1+0� A�a |P(x)                   (no sum over �) .        (7.14)

The last step in the derivation is the customary redefinition of the 4D spinors, in order
to obtain Dirac equations in their traditional guise. As in (7.4), we define

                         cp  :=     i  5  ~cp  =  jM PM  .                 (7.15)

                                 e4

The second equality is a consequence of the transformation rules (7.7) and (7.8). In terms
of the redefined spinors, equation (7.13) then takes the final form

i � XM� cp + (Ap)a�   , (ea + ea ) L2 cp -    , D/ K  L2 cp

                                 -        (FAap )�  , ea � L2 � cp   = 0.  (7.16)
                                    8

This is the main result of this section. It says that the CP-transformed spinors cp satisfy
equations of motion on M4 very similar to those satisfied by the original , i.e. to (7.5).
The differences are that the gauge form is now Ap, instead of A; we have two different

signs when  = 1; and four types of matrices -- determined by the operators ea, ea,
D/ K, and ea� on the space of internal spinors -- appear complex-conjugated in the new

equation.

Remark 7.3. When K is even-dimensional, hence so is P , there are two higher-dimensional
conjugations, j� = j�M jK. See (4.1) and (4.4). They are both symmetries of the equation
D/ P  = 0. Since j-K anticommutes with the internal Dirac operator D/ K, the conjugation
j+M  j-K flips the signs of all the mass terms in the 4D equations, after dimensional
reduction. So the conjugation that most closely adheres to the usual conventions of 4D
physics is j- = j-M  j+K. It exists when the dimension of K is not 3 (mod 4).

Remark 7.4. The action of the higher-dimensional conjugations j appearing in (7.9)

                                          30
and (4.4) can be better interpreted with the help of lemma 6.4. In a basis of internal
spinors {} with the properties stated in the lemma, we see that j just C-transforms
the 4D spinors , multiplies them by phases, and swaps some of them in pairs.

    To end this section, we note that when the dimension of K is not 2 (mod 4), the higher-
dimensional transformation jP preserves the conditions for Weyl spinors, P  = �.
This follows from (4.14). The CP-transformation spinors on M4, in contrast, always
preserves the Weyl conditions. Using the definition M = i0123 = 5, it is clear from
(7.15) and properties (7.7) and (4.8) that  = � 5  is equivalent to cp = � 5 cp ,
as usual in 4D.

7.3. CP violation

In this discussion we will assume that the gauge fields A�a with light bosons are all linked
to internal vector fields ea induced by a G-action on K, which needs not be isometric.
In other words, the vacuum metric on K is such that the remaining vector fields in the
infinite basis {ea} have large Lie derivatives LeagK, and hence the corresponding 4D
gauge bosons have large masses. We also assume that we are in a region of Minkowski
spacetime where the only non-zero gauge fields A�a are those with massless or light bosons.
So no excitations at Planck scale. In this case, all the relevant operators ea in the Dirac
equations (7.5) belong to a proper g-representation on the space of spinors on K.

    We now turn to the main point. Equations (7.5) and (7.16) for the 4D spinors  and
the CP-transformed cp both describe solutions of the massless Dirac equation on M �K.
They are broadly similar equations, but not entirely equivalent. Even if we redefine the
gauge representations by complex conjugation, ea  ea, the two equations still remain
formally different. Thus, in our Kaluza-Klein setting, there is no reason to expect that
left-handed particles interact with any of the physical 4D forces in exactly the same way
that right-handed antiparticles do. If a force is described by a gauge representation that
is equivalent to its complex conjugate, such as the fundamental SU(2) representation,
that fact by itself is not enough to render (7.5) and (7.16) equivalent. Other terms in the
equations remain different. So the 4D equations produced by Kaluza-Klein models are
not invariant under the traditional formulation of CP symmetry.

    The specific sources of CP violation, however, depend on the details of the higher-
dimensional metric gP . When only massless gauge fields Aa� are turned on, the relevant
vector fields ea on K are solely the Killing ones. These satisfy the identities

                   D/ K, ea = 0 and ea = 0 .  (7.17)

                   31
The first identity implies that the transformations ea preserve the D/ K-eigenspaces. So
there are L2-orthonormal bases of the irreducible representation spaces Wm, composed
entirely of D/ K-eigenspinors. In other words, the Kaluza-Klein model will have a repres-

entation basis of 4D fermions that, at the same time, is a mass basis. With this choice of

basis, the equations of motion (7.16) for antiparticles become

i � XM� cp + (Ap)�a   , ea  L2 cp -  m cp

-     (FAap )�  , ea � L2                  � cp  =  0,  (7.18)
   8

where the masses m are the real D/ K-eigenvalues. Thus, if we redefine the gauge rep-
resentation by complex conjugation, for  = -1 the only source of inequivalence when

compared to the particle equations (7.5) is the Pauli term. This term is often considered

negligible in KK models [8, 62] (but do see remarks 2.1 and 7.2). In the simpler abelian
5D KK model, the Killing vector field ea is gK -parallel on K = S1. One can then show
that a sign change of the gauge field Ap� is enough to render (7.18) completely equivalent
to (7.16), when  = -1. So there is no CP violation in the traditional 5D KK model.

    In regions where massive gauge fields Aa� are turned on these properties no longer hold,
even if all the gauge bosons are light. Some non-Killing internal vector fields ea become
relevant too. The respective transformations ea do not commute with D/ K anymore, so
do not preserve the D/ K-eigenspaces. There is an infinite-dimensional complex matrix
relating the D/ K-eigenspinors to the orthonormal bases of the irreducible representation

spaces -- the spaces Wm, of proposition 6.2. To our knowledge, there is no a priori reason
to expect that this CKM-like matrix can be rendered entirely real on general grounds.

This is one of the sources of inequivalence between equations (7.5) and (7.16).

    Another source is the Pauli term, as before. Finally, the third source of CP violation

is the new non-minimal gauge coupling matrix   , ea �  L2, which becomes non-zero
when ea is not Killing and the gauge field A�a is massive. This is an anti-Hermitian matrix
acting on the space of internal spinors. Overall, to our knowledge, there is no a priori
reason to expect the existence of a clever choice of representation basis {} that renders
the CKM-like mass matrix   , D/ K L2, the Pauli term matrix  , ea � L2, and
the new non-minimal gauge coupling matrix   , ea �  L2, all simultaneously real on
general grounds. It would be interesting, nevertheless, to investigate these matters in

explicit examples based on different compact spin manifolds K.

      32
Appendices

A. Conventions for spinors in signature (s, t)

Gamma matrices, inner products and chirality operator

Consider the vector space Rn equipped with the standard, non-degenerate metric  of
signature (s, t). It has s independent vectors of positive norm. Our convention is that

these vectors represent space-like directions. So the internal space K of a Kaluza-Klein

model has a Riemannian metric with positive signature.

The  spinor  space  n  is  the  complex       coordinate     space  of  dimension  2  n  .  For each
                                                                                      2

choice of signature (s, t), there are n matrices j that act on n and satisfy the relations

                           j k + k j = -2 jk I .                                            (A.1)

These matrices are not unique and can be rotated with Os,t similarity transformations.
They can be chosen to have the hermiticity properties


                       (k) =  k                  if 1  k  t                                 (A.2)

                                     - k if t < k  t + s .

Thus, the gamma matrices in spatial dimensions are square roots of -1 and are anti-
self-adjoint with respect to the product  of spinors in n. This is the most common
convention in Riemannian geometry [58,59,61,63,64]. It is also used in the QFT textbook
[50].3 Vectors in Rn act on spinors through the Clifford multiplication v �  := j vjj .
This determines an irreducible representation of the Clifford algebra Cls,t on the spinor
space. So n also carries representations of the groups Pins,t and Spins,t, which are
contained inside the Clifford algebra.

    When t  1, the positive-definite Hermitian product on n is not invariant under the
action of the connected component of the identity of the spin group, denoted Spin0s,t. So
one usually works with a different, Spins0,t-invariant inner product. It is defined by

                                      1

                                            2                   if t = 0
                                                                if t  1 .

                    1, 2        :=       t    1                                             (A.3)
                                         2
                                      i          1  � � � t  2


3The dominant convention in physics textbooks is to write the Clifford relation (A.1) with the opposite
 sign. So our gamma matrices in signature (s, t) are their gamma matrices in signature (t, s).

                                                         33
Here a denotes the integral part of a. This product satisfies 1, 2 = 2, 1 and,

for  t       1,  has  indefinite   signature    (2  n  -1,  2  n  -1   ).  Under     Clifford  multiplication,
                                                    2          2

                                   v � 1, 2 = (-1)t-1 1, v � 2 .                                                (A.4)

The complex chirality operator  : n  n in signature (s, t) is defined by

                                                 :=    i  s-t+1    1 � � � n      .                             (A.5)
                                                              2

It satisfies the algebraic relations

                                               =                                                                (A.6)
                                          (v � ) = (-1)n-1 v � ( )                                              (A.7)
                                         1, 2 = (-1)t(n-1) 1,  2 .                                              (A.8)

In particular,  commutes with the elements in the Lie algebra spins,t  Cls(2,t). So it
commutes with the action of the connected group Spin0s,t on spinors.

Majorana forms and conjugation automorphisms

Consider again the vector space Rn equipped with the standard metric of signature (s, t)
                          n
and     let  n   =    C2  2    be  the  complex  spinor     space.        Define  the  set


                                        In  :=  {-1, 1} if n is even                                            (A.9)

                                                {(-1)       n-1   }    if n is odd .
                                                              2

Proposition A.1. For each value   In, there exists a C-bilinear form on n such that

                                   C (v � 1, 2) =  C (1, v � 2)                                                 (A.10)
                                      C (1, 2) = (n,  ) C (2, 1)                                                (A.11)

for all spinors j  n and vectors v  Rn. The symmetry sign is                                                    (A.12)


                                                       (-1)  n         n   if n is even
                                                             4         2   if n is odd .

                                   (n,  )   :=               n2 -1
                                                                8
                                                       (-1)


Property (A.10) is valid for gamma matrices of any signature with s + t = n. The form
C can be chosen so that it is represented by a unitary matrix in any complex basis of n

                                                            34
orthonormal with respect to the product  .

    The bilinear forms C are called Majorana forms on n. They only depend on the
dimension n, not on the signature. The properties in proposition A.1 determine them
uniquely, up to a complex phase. Property (A.10) implies that, in all signatures:

Proposition A.2. The Majorana forms satisfy:

C (  1, 2 )  =   (-1)(n-1)                     n    C ( 1,   2 )  (A.13)
                                               2                  (A.14)
                                                                  (A.15)
C (b � 1, 2) = - C (1, b � 2)

C ( � 1,  � 2) = C (1, 2) .

Here  is the chirality operator on n, b is any element in the Lie algebra spins,t, and 
is any element in the connected group Spins0,t.

    The Majorana forms in proposition A.1 can be explicitly constructed using a set of
Euclidean gamma matrices in a special representation, in which they are all symmetric
or anti-symmetric. See [49, 51]. The content of the proposition, which we will not prove
here, encodes the essential properties in a concise way.

    Using the non-degenerate Majorana forms and the sesquilinear inner product (A.3),
one can define natural, conjugate-linear automorphisms of n. Consider the sets


Hs,t  :=  {-1, 1}                              if s - t is even   (A.16)

          {(-1)  s-t+1                      }  if s - t is odd .
                     2

Definition A.1. For each value   Hs,t, the conjugation map j : n  n is defined by

       j 1, 2  := C()(1, 2)                                       (A.17)

for all j  n. Here  () = (-1)t+1 and the inner product  �, �  is the one in (A.3).

    Although the Majorana form C does not depend on the signature of the gamma
matrices, the inner product  �, �  does. So the properties of the conjugation maps j do
depend on the signature.

                   35
Proposition A.3. The maps j are conjugate-linear and satisfy:

                        j(v � ) =  v � j()                                                          (A.18)
                                                                                                    (A.19)
                                                                                                    (A.20)

                                           (-1)  s-t     (-)           s-t    if s - t is even
                                                   4                     2    if s - t is odd

                        j j() =            (-1)  (s-t)2 -1

                                                      8             


                                           (-1)  s-t      j()               if s - t is even
                                                   2

                          j( )       =

                                              j ( )                         if s - t is odd ,


for all spinors   n and all vectors v  Rn. When s - t is even, the map j- coincides
with   j+ up to a complex phase.

    A conjugation with jj = 1 is called a real structure on n. It allows the consistent
imposition of the Majorana condition on spinors, j() = . A conjugation with jj =
-1 is called a quaternionic structure on n. It defines an action of the quaternions on
spinors through the representation (i, j, k)  (i, j, i j).

    Using the definition of j and properties (A.11) and (A.19), one also calculates that

Lemma A.4. The maps j satisfy:


                                                            t(s+1)
                    j 1, j 2            =                           t  1,   2     if s - t is even  (A.21)
                                           (-1) 2                                 if s - t is odd

                                           (-1)  st      1,            2
                                                 2

for all spinors 1, 2  n and for the inner product in (A.3).

Spinor bundles, connections and Dirac operator

Let M be an oriented manifold of dimension n. A topological spin structure on M is a

double   cover      :  F        +    FGL+  of the bundle of oriented n-frames on T M .              This cover

                          GL               +

should have a right action of GLn , the universal cover of the connected component of the

identity of GLn(R). The cover should be equivariant with respect to the right actions of
      +
         and  GL+n  on  the  respective    bundles.      See        for  example  [58].
GLn

Let g be a metric on M of signature (s, t). Considering only the oriented, g-orthonormal

frames on T M defines a subbundle FSO(g) inside FGL+. The cover  can be restricted to
a double cover FSpin(g)  FSO(g) that is equivariant with respect to the right actions of
the connected groups Spins0,t and SOs0,t on the respective bundles. We call this restriction
a metric spin structure on M subordinate to the topological one. See for example [65,66].

The complex spinor bundle Sg  M is the associated vector bundle FSpin(g)�Spin0s,t n.

                                                         36
The sections of Sg are spinor fields . There is a natural action of vector fields on spinor
fields by Clifford multiplication on each fibre. This extends to a left action of the Clifford
bundle on Sg. The inner product �, � and the Majorana forms C on spinor space n
are Spins0,t-invariant. So they have natural extensions to the spinor bundle Sg, denoted by
the same symbols. Similarly, the chirality operator  and the conjugation automorphisms
j commute with the Spins0,t-action on spinor space. This follows from (A.7) and (A.18),
respectively. So they have natural extensions as automorphisms of the spinor bundle.

    The Levi-Civita connection  on the tangent bundle (T M, g) has a standard lift
to the spinor bundle that is compatible with the inner product �, � and with Clifford
multiplication. One can also check that it preserves the chirality operator, the Majorana
forms and the conjugation automorphisms. In other words,

 U (V � ) = V � (U ) + (U V ) �                                                      (A.22)
LU 1, 2 = U 1, 2 + 1, U 2                                                            (A.23)
                                                                                     (A.24)
           = C = j = 0 .

An explicit, local formula for the covariant derivative of spinors is [58]:

X   :=  X ~  +                          1  gir  gjs  g(X vi, vj) vr  �  vs  �  ~  .  (A.25)
                                        4

Here {vr} denotes a local, oriented, g-orthonormal trivialization of T M , while ~ represents
the spinor  in the induced trivialization of Sg. So ~ is a local function on P with values
in n and we denote by X~ = (d~ )(X) its directional derivative. Since the metric is

pseudo-Riemannian, the elements grs can be �1. We will most often abuse notation and
simply write  instead of ~ .

The Dirac operator on M can be defined by the local formula

                                          D/  := gjk vj � vk  .                      (A.26)
For spinor fields with compact support, it satisfies

   D/ 1, 2 volg = (-1)t 1, D/ 2 volg ,                                               (A.27)

M                                                    M

where �, � is the inner product (A.3).

                                                37
B. Relating spinors of different metrics

Transporting the Levi-Civita connection and the Dirac operator

The purpose of this appendix is to describe the formulas to transport objects between the
spinors bundles determined by two different Riemannian metrics on the same manifold
with fixed topological spin structure. These objects are the spinors themselves, their
covariant derivatives, the Dirac operator and the Kosmann-Lichnerowicz derivatives. Im-
portant references on this topic include [55�57]. Here we simplify some of the formulas
given by Wang in section 1 of [57]. Then we extend the calculations to the case of the
transported Kosmann-Lichnerowicz derivative, which does not appear to have been con-
sidered before. The notation used here is mostly that of [57]. We omit the proofs of
the formulas that follow from straightforward, though often not short, calculations. The
results in this appendix are used in section 5 to define a new Lie derivative of spinors
along the fundamental vector fields of a G-action.

    Let (M, g) be an oriented, Riemannian manifold with a fixed spin structure. Let
 : T M  T M be an invertible map that is linear on the fibres and projects down to the
identity on M . Assume also that  is g-symmetric, i.e. that g((U ), V ) = g(U, (V ))
for all tangent vectors U and V . Then we can define a new Riemannian metric on M by

                             g(U, V ) := g(-1(U ), -1(V )) .        (B.1)

The Levi-Civita connections of the new and old metrics are denoted g and g = .
Using Koszul's formula, one finds that the transport of g by the automorphism  is:

( -1  gV  ) U                =  V U  +  1       [  V  - (V ) ] U .  (B.2)
                                        2

Here V : T M  T M is the endomorphism given by

V : U -   ((U)-2)(V ) +   (V -1)(U )                                (B.3)

and (V ) denotes its adjoint with respect to the metric g. Since  is a metric connection
on T M , it follows from (B.2) that -1  g   is a metric connection too.

    The automorphism  of T M can be lifted to a map  : Sg  Sg between different
spinor bundles, which we denote by the same symbol. The lift is equivariant with respect

to Clifford multiplication:

                             (V � ) = (V ) � ()                     (B.4)

for any vector V  T M and spinor   Sg (see [56, lem. 2.3.4]). Let �, � be the inner

                                38
product of spinors defined in (A.3). It is positive-definite in Euclidean signature. Let M
be the chirality operator on spinor bundles determined by (A.5). Let j be any of the
conjugation automorphisms in definition A.1, after extension to the spinor bundles. We
use the same symbols to denote the inner products, chirality operators and conjugations
on Sg and Sg. Then one can check that the lift  : Sg  Sg has the natural properties:

                  (1), (2) = 1, 2                                                 (B.5)
                         (M ) = M ()                                              (B.6)
                           j() = j  () .                                          (B.7)

The two Levi-Civita connections on T M admit standard lifts to the respective spinor
bundles, which we still denote g and . These are connections on different bundles,
Sg and Sg. To compare them we need to transport g back to Sg, so to consider instead
the covariant derivative -1  gV  . Using (A.25) and (B.2), one calculates that

   -1  Vg   ()    =  V         +  1        g(V (vi), vj) vi � vj �  ,             (B.8)
                                  4
                                      i=j

where {vk} denotes any local, oriented, g-orthonormal trivialization of T M . This is a

simplification of the formula given in [57]. One can also calculate how the Dirac operator
on Sg, denoted D/ g, appears when transported to Sg. The result is:

-1  D/ g    =                            1                                        (B.9)
                  k (vk) � vk - 2  +  grad(log det ) � 

               +  1            -1  ((vi))(vj),  vk  vi � vj � vk �  .
                            g

                  4 i= j=k

In this formula, det  is the function on M relating volume forms, volg = (det ) volg.
The vector field  on M is defined by  = - k (vk)(vk). The sum over i = j = k
means that all three indices should be different. Formula (B.9) is a slightly more developed
version of the one given in [57]. It isolates the contributions of the volume change det 
and the divergence  to the new operator. Using (B.9), one can then calculate that

   -1  D/ g   1, 2 volg =             1, -1  D/ g   2                             (B.10)

M                              M

                                      + 1,  grad(log det ) � 2 volg .

This implies that the elliptic, first-order differential operator on Sg given by

     -         -1  D/ g  () +         1                  �                        (B.11)
                                         grad(log det )
                                      2

                                  39
is formally self-adjoint with respect to the L2 metric on spinors induced by g. Just as the
Dirac operator D/ g is. The calculation that leads to (B.10) is similar to the calculation in

the usual proof that the Dirac operator is self-adjoint (e.g. [58, lemma 2.28]).

Transporting the Kosmann-Lichnerowicz derivative

Consider now the Kosmann-Lichnerowicz derivative LVg on the spinor bundle Sg, defined
in (1.3). Again, one can transport it to Sg and compare it with the native derivative LVg.

A calculation using (B.2) and (B.8), applied to definition (1.3), shows that

-1  LVg   ()          =    LVg   +  1        g  -1(LV )(vj), vk  vj � vk �            (B.12)
                                    4
                                       j= k

Here LV  denotes the standard Lie derivative of the automorphism . In the special case
where LV  vanishes, the operator -1  LVg   coincides with LVg. The same thing
happens when -1(LV ) is self-adjoint with respect to g. In this case, the coefficients
g(-1(LV )(vj), vk) are symmetric in j, k, and hence the sum in (B.12) vanishes.

    Just as the original LVg, the transported Kosmann-Lichnerowicz derivative commutes
with the chirality operator K and is compatible with the inner product of spinors,

 -1 LVg  (1) , 2  +  1 , -1 LVg  (2)  = LV  1 , 2  .                                  (B.13)

However, it acts on the Clifford multiplication of vector and spinor fields through

-1 LVg  ( U �  ) = [V, U ] �  + U � -1 LVg  () + HV(U, vk) vk �  . (B.14)

                                                                                                                     k

Its commutator with the Dirac operator on Sg is

D/ , -1 LVg        =       HV(vj, vk) vj � vk   +  1        (viHV)(vj, vk)  vi  � vj  � vk  �
                                                   4
                      j,k                             i= j= k

                          1      (vk HV)(vj, vk) - (vj HV)(vk, vk) vj �  .            (B.15)
                      +

                          2 j,k

In the last two identities, HV is the 2-tensor on M defined by

HV(X, Y ) :=  1  (LV g)(X, Y ) + g -1(LV )(X), Y      - g -1(LV )(Y ), X              (B.16)
              2

for all vector fields X and Y . It has manifestly symmetric and anti-symmetric parts. This
tensor vanishes if and only if V is Killing and -1(LV ) is self-adjoint with respect to

                                       40
g. These properties of the transported Kosmann-Lichnerowicz derivative can be proved
using the analogous ones of LVg, as stated for example in [20], and then calculating the
corrections due to the second term on the right-hand side of (B.12).

Proposition B.1. Take a g-symmetric automorphism  : T M  T M that is positive-
definite. As before, also call  the lifted spinor map Sg  Sg, where the metric g is as
in (B.1). If a vector field V is conformal Killing both for g and g, then

                           -1  LVg   = LVg                                  (B.17)

as differential operators on spinors in Sg.

Proof. Using the definition of g and the properties of Lie derivatives, one calculates that

(LV g)(X, Y ) = (LV g)(-2(X), Y ) + g((LV -2)(X), Y )                       (B.18)

for all vector fields X and Y on M . The assumptions on V mean that there are real
functions f and f on M such that

                  LV g = f g                     LV g = f g                 (B.19)

as 2-tensors on M . Applying this to (B.18) and using the non-degeneracy of g, leads to

                  LV (-2) = (f - f ) -2                                     (B.20)

as automorphisms of T M . Now, the fact that  is g-symmetric and positive-definite
implies that -1 is as well. So there is a local, g-orthonormal trivialization of T M in
which the automorphism -1 is represented by a diagonal matrix diag(1, . . . , m). Here
m = dim M and the j are local, positive functions on M . Denote by aij the entries of
the matrix representing LV (-1) in the same trivialization. Then (B.20) implies that

                  (i + j) aij = (f - f ) ij 2j                              (B.21)

for all i and j. Since i + j is always positive, it follows that

2 aij = (f - f ) ij j                            2 LV (-1) = (f - f ) -1 .  (B.22)

So one also gets

                  -1(LV )  =  - (LV -1)          =  1                       (B.23)
                                                    2 (f - f) I .

Finally, using this expression in (B.12), it is clear that the sum on the right-hand side of

                                             41
that equation will vanish. So we obtain the desired identity of differential operators.

Transport to first order

Let (M, g) be an oriented, Riemannian manifold with a fixed topological spin structure.

Let t be a smooth 1-parameter family of invertible automorphisms T M that project to

the identity on M , starting at 0 = Id. Assume that all the t are g-symmetric, which

implies that the t-1 are as well.          The    derivative          :=  d     |t=0  is  then  a  g-symmetric
                                                                          dt

endomorphism of T M . So are the covariant derivatives V  for all vector fields V on M .

    For small t, define the family of Riemannian metrics gt on M by (B.1). As before, the
automorphisms t of T M can be lifted to maps t : Sg  Sgt between spinor bundles.
These lifts can be used to transport the various differential operators between the two

spinor bundles. The first-order variations of the transported operators are then given by:

d   (  t-1  gt    t  )(U )  |t=0  =  - (U  )(V )  +           g (vj  )(V ), U             vj              (B.24)
dt             V

                                                      j

d      (  t-1  gt    t  )   |t=0  =     1      g  (V  )(vi)        +  2 (vi )(V ) , vj        vi � vj �   (B.25)
dt                V                  -
                                        4  i=j

d      (  t-1  L gt     )         =     1      (LV g)( (vi) ,      vj) vi � vj                            (B.26)
dt                V  t      |t=0     -                                          �
                                        4  i= j

d      ( t-1 D/ gt   t  )   |t=0  =                             1   + grad(trg  )             � .         (B.27)
dt                                          (vj) � vj  - 2
                                     j

Formula (B.27) for the Dirac operator was given long ago in [57]. Formula (B.26) for
the Kosmann-Lichnerowicz derivative appears to be new. It shows that the first variation
vanishes when V is conformal Killing on M .

C. Proofs for section 3

Proof of uniqueness in proposition 3.1. Suppose that R^ and R~ are two C-linear

maps of spinors (SgP )  (SRgP ) with the four properties listed in proposition 3.1.
Property (3.2) implies that R^ and R~ are both invertible maps. The composition

                            R^ R~ : (SgP )  (SRRgP ) = (SgP )                                             (C.1)

                                                  42
is then an automorphism of (SgP ). From property (3.1) of R^ and R~, it follows that, for
any complex function f on P ,

R^ R~(f ) = (RRf ) (R^ R~ ) = f (R^ R~ ) .        (C.2)

So the map R^ R~ is C(P )-linear, and hence must be induced by a C-linear automorphisms
of the bundle SgP that preserves its fibres. Moreover, it follows from property (3.3) of R^
and R~ that, for any vector field W on P ,

R^ R~(W � ) = (RRW ) � (R^ R~ ) = W � (R^ R~ ) .  (C.3)

This means that the automorphism of the fibres of SgP determined by R^ R~ commutes with
Clifford multiplication of vectors and spinors. Hence, it commutes with the action of the

whole Clifford algebra on the fibre of SgP . But these fibres are isomorphic to the complex
spinor space m+k, on which the Clifford algebra acts irreducibly, by definition. Thus,
Schur's lemma implies that the composition R^ R~ is proportional to the identity on each

fibre, and hence must be of the form

R^ R~() =                                         (C.4)

for some complex function  on P . From property (3.4) of R^ and R~, we also have that

 W  = R^ R~(W ) = RRW (R^ R~ ) = W ( ) =  W  + d(W ) 

for all vector fields W and spinors . So d must vanish and the function  is constant
on P . This constant cannot be zero because R^ and R~ are invertible maps, so R^ R~ must
be too. Finally, using property (3.2) of the maps R^ and R~ and denoting by ^ and ~ the

respective constants in U(1), it follows from (C.4) that

 R^ () = R^( ) = R^ R^ R~() = ^ R~()              (C.5)

 R~ () = R^ R~ R~ () = R^ (~ ) = ~ R^ () = ~ -1  R^ () = ~ -1 ^ R~()

for all spinors . So 2 = ~ ^ and  must be a complex phase, just as ^ and ~ are.
Thus, it follows from (C.5), for example, that R^ and R~ differ only by a constant complex

phase.

Construction of the spinor map in proposition 3.1. In this part of the proof of
proposition 3.1, we will construct the spinor reflection map from a local formula and show
that it is globally well-defined. The first task is to define oriented, local trivializations of

                                                       43
the spinor bundles SgP and SRgP where the local formula (3.5) can be applied. Start by

picking an oriented, gP -orthonormal trivialization of the tangent bundle T P = H  V

over a domain M � U formed entirely of horizontal and vertical vector fields. So a

trivialization of the form {X�H, vj}, as described at the end of section 2.1. The vj form

an orthonormal basis of T K over the domain U  K with respect to the metric gK(x),

for each x  M . The X� form a gM -orthonormal basis of T M and their horizontal lift to

P is

      X�H = X� + Aa(X�) ea .                      (C.6)

As usual, this local trivialization of T P induces a trivialization of the spinor bundle SgP
over the same domain M � U. Now define a different, RgP -orthonormal trivialization
{X~�H, v~j} of T P by putting

       v~j := R vj                                (C.7)
      X~�H := (-1)� R(X�H) = X� + (RA)a(X�) ea .  (C.8)

Here we have used the identity RX� = (-1)� X� and the fact that R ea = ea, since ea
is a vector field on K. The trivialization {X~�H, v~j} has the same orientation as {X�H, vj}.
It induces a trivialization of the second spinor bundle SRgP over the same domain M �U.

    To define the spinor reflection map, let  be any spinor on SgP . With respect to the
trivialization of this bundle induced by {X�H, vj}, the spinor is represented by a function
(x, y) : M � U  m+k. Then we declare that the reflected spinor R() should be
represented by the function

      (R )(x, y) := ei  (R(x), y)                 (C.9)

with respect to the trivialization of SRgP induced by the second trivialization {X~�H, v~j}
of T P . Here ei is a constant complex phase, and  is the gamma matrix on m+k
corresponding to the coordinate x of M that changes sign in the reflection. To see that

R() is globally well-defined, we have to check that the local definitions are consistent on

intersections of trivialization domains.

    Suppose that M � U is another domain in P with two oriented trivializations of T P ,
denoted {X�H, vj} and {X~�H, v~j}, constructed in a way analogous to the previous ones.

On the intersection we have the transition functions b : M � (U  U)  SO(k) defined

by

      vj =  i (b)ij vi .                          (C.10)

From the definition (C.7) of v~j, it is clear that the transition functions for the second

            44
family of trivializations are just the pullback functions

~b = Rb .                                                  (C.11)

Now, the fixed topological spin structure on K and its extension to M � K, determines a
lift of the functions b to functions B : M � (U  U)  Spin(k) satisfying the usual
consistency conditions on triple intersections. The transition functions of the bundle
SgP = S(H)  S(V ) are then

(I  B) : M � (U  U)  Spin(m - 1, 1) � Spin(k) .            (C.12)

One can then check that the pullback functions I  RB also satisfy all the consistency
conditions on triple intersections and form a set of transition functions for the bundle
SRgP covering the functions ~b. Using these two sets of transition functions for the two
spinor bundles, we finally calculate that, on the intersection of domains M � (U  U),

(R )(x, y) = ei  (R(x), y)                                 (C.13)
                 = ei (  I) [I  B(R(x), y)] (R(x), y)
                 = ei [I  (RB)(x, y)] (  I) (R(x), y)
                 = [I  (RB)(x, y)] (R )(x, y) .

In the second equality we have used the construction of the higher-dimensional gamma
matrices from (2.7). Formula (C.13) shows that the local representatives of the reflected
spinor R , as defined in (C.9), transform as they should in order to be a section of the
bundle SRgP . So the spinor R() is globally well-defined on M � K and hence the map
R : (SgP )  (SRgP ) is well-defined too.

Verification of the four properties in proposition 3.1. Using the local definition of
spinor reflection in (C.9) and the standard pullback of a function, we have

      [R (f )](x, y) = ei  f (R(x), y) (R(x), y) = (Rf )(x, y) (R )(x, y) .

The properties of the gamma matrices and the chirality operator on m+k also imply that
                   [R R ()](x, y) = e2i ()2 (R R(x), y) =  (x, y)

for the complex phase  = - e2i (gM ). These identities are valid on arbitrary domains
M � U, so we obtain that properties (3.1) and (3.2) of proposition 3.1 are valid globally.

                                                       45
    Let V be a vertical vector field on P , expressed locally as V j vj. Then the local
representative of the Clifford product V �  is the function V j j with values on m+k.

Since j anti-commutes with , it is clear from definition (C.9) that property (3.3) in

the proposition is valid for vertical vector fields. Now consider the horizontal, basic vector

field X�H of (C.6). Using the local definition (C.9) and the fact that X�H is part of the gP -
orthonormal trivialization of T P while X~�H is part of the RgP -orthonormal trivialization,
we calculate that the local representative of R(X�H � ) satisfies

[ R(X�H � ) ] |(x,y) = ei  (X�H � ) |(R(x),y)                             (C.14)
                         = ei  �  |(R(x),y)
                         = - (-1)� � ei   |(R(x),y)
                         = - (-1)� � (R ) |(x,y)
                         = - (-1)� X~�H � (R )  |(x,y)
                         = - [ (R X�H) � (R ) ] |(x,y) .

This last step uses the definition (C.8) of X~�H. The calculation shows that property (3.3)
in the proposition is valid for horizontal vector fields too, and hence is always true.

    At this point, the only piece missing to finish the proof of proposition 3.1 is the
verification of property (3.4) of spinor reflections. We will do this using the local formula
(A.25) for the spinorial lift of the Levi-Civita connection. Taking the first term in that
formula and using the local definition (C.9) of reflections, we get

R (W ) |(x,y) = ei  (W ) |(R(x),y)                                        (C.15)
                    = ei  (RW ) |(x,y)
                    = W [ ei  (R) ] |(x,y)
                    = W [(R ) ] |(x,y) .

As for the second term in (A.25), the previously established properties (3.1) and (3.3) of
spinor reflections guarantee that

R [ g(gW ui, uj) ui � uj �  ] = R[ g(W g ui, uj) ] (Rui) � (Ruj) � R() .  (C.16)

Here {uj} denotes an oriented, gP -orthonormal, local trivialization of T P . But the space-
time reflection R : (P, gP )  (P, RgP ) is an isometry of pseudo-Riemannian manifolds.
So the naturality properties of the Levi-Civita connection say that the pullback connec-
tion R(Rg) coincides with RRg = g. See [67, prop. 5.13]. Therefore, the usual

46
properties of pullback connections imply that, for all vector fields V and W on P,

                                    R(W g V )             =   Rg            (RV   )   .                               (C.17)
                                                                 RW

See [67, lem. 4.37], for example. Thus we get

    R[ g(gW V, U ) ]   =       (Rg)(RW g V, RU )                   =        (Rg)      Rg        (RV     ),  RU     .  (C.18)
                                                                                         RW

Applying this identity to (C.16), we get

R [ g(W g ui, uj) ui � uj �  ] =         (Rg)       Rg        (Rui       ),  Ruj            (Rui) � (Ruj) � R() . (C.19)
                                                       RW

Now, {Ruj} is a RgP -orthonormal, local trivialization of T P . However, it is not an
oriented trivialization, as reflections invert the orientation. But the right-hand side of

(C.19) is invariant under a change of sign of any of the vectors Ruj, which would make this

an oriented, RgP -orthonormal trivialization. So the right-hand side of (C.19) coincides

with  the    second  term  of  the  covariant          derivative           Rg     (R)          as  it  would      appear  in  an
                                                                               RW

application of formula (A.25). Combining this fact with (C.15) and using again (A.25),

we  finally  conclude  that  R(gW )         =    Rg           (R).
                                                    RW

Proof of proposition 3.2. Property (3.6) in the proposition is a direct consequence
of the application of identities (3.1) and (3.3) to the definition of the Dirac operator.
Property (3.7) can be obtained from identity (3.3) through the calculation

             R (P )    =   i   m+k-1     R  (u0  �  �  �  um+k-1      �  )                                            (C.20)
                                    2

                       =   i   m+k-1     (-1)m+k          (R  u0)  �  �  �  (R  um+k-1)     �   (R  )
                                    2

                       =   (-1)k+1       i  m+k-1      (-R    u0)     �  (R  u1)   �  �  �  (R  um+k-1)     �  (R  )
                                                 2

                       = (-1)k+1 P (R ) .

Here we have used the definition (A.5) of the chirality operator and noted that, if {uj}
is a local, oriented, orthonormal trivialization of T P with respect to the metric gP , then
{-Ru0, Ru1, . . . , Rum+k-1} is an oriented, orthonormal trivialization with respect to
RgP . We have also used that the dimension m of M is even by assumption. Finally,
property (3.8) follows directly from the local definition (C.9) of spinor reflection, the
definition (A.3) of the inner product of spinors, the hermiticity properties of the gamma
matrices, and the observation that, in our conventions (A.1), we have

                                 = - gP (XH, XH) = - (gM ) .
                                                      47
D. Proofs for section 6

Proof of proposition 6.1. Using the definition of  and property (5.3) of LV , we have

                               1  (divgU ) LV  + (divgV ) LU  + [ LU (divgV ) ] 
U V () = LU LV  + 2                                                        1

                                                                       + 4 (divgU )(divgV ) .  (D.1)

Cancelling the terms that are symmetric in U and V ,

                                                             1                                 (D.2)
      (U V - V U ) = (LU LV - LV LU ) + 2 LU (divgV ) - LV (divgU )  .
From the definition of divergence, LV volg = (divgV )volg, we also have that

   (divg[U, V ]) volg = L[U,V ] volg = (LU LV - LV LU ) volg                                   (D.3)
                         = LU (divgV ) - LV (divgU ) volg .                                    (D.4)

Thus, using property (5.5) of LV , we get

                                             1                                                 (D.5)
   (U V - V U )  = L[U,V ] + 2 (divg[U, V ])  = [U,V ]  .

This shows that indeed  defines a Lie algebra representation. Finally, using property
(5.4), together with the definition of divergence and Stokes' theorem,

   V 1, 2 + 1, V 2 volg = LV 1, 2 + 1, LV 2 + 1, 2(divgV ) volg
K                                 K

                                  = LV 1, 2 volg + 1, 2 (LV volg)
                                         K

                                  = LV 1, 2volg = 0 .                                          (D.6)
                                         K

So the representation is unitary with respect to the L2 Hermitian product.

Proof of proposition 6.2. Take the averaged metric g^ defined in (5.6) and consider the
Dirac operator D/^g on the spinor bundle S^g. We have the D/^g-eigenspace decomposition

                                  L2(S^g) =        E^m .                                       (D.7)

                                               mZ

By construction, all the vector fields in g are Killing with respect to g^. So the Kosmann-
Lichnerowicz derivatives L^V commute with D/^g for all V in g. Hence, they preserve all the

                                           48
finite-dimensional eigenspaces E^m. By (5.7), the derivatives L^V define a representation
of the compact Lie algebra g on E^m, so we have the decomposition

                E^m =    nm, E^m, ,                                        (D.8)


where only a finite number of the integers nm,  0 are non-zero as  varies. Consider
now the linear, invertible automorphism  : Sg  S^g. It induces an invertible linear map
L2(Sg)  L2(S^g). This map does not preserve the L2-metrics, because (B.5) implies that

    (1), (2)  vol^g = 1, 2 (det ) volg ,                                   (D.9)

K                            K

and in general det  is not 1. However, it is clear that the corrected map

                ~ := (det )-1/2                                            (D.10)

does preserve the L2 inner products. Using the corrected map to transport L^V , a direct
calculation shows that

~-1  L^V  ~  =  -1  L^V      -  1 (det )-1                LV (det )        (D.11)
                                2

But V is Killing with respect to g^, by construction, so

0 = LV vol^g = LV [(det ) volg] = [ LV (det ) + (det )(divgV ) ] volg .    (D.12)

This gives us a formula for divgV in terms of det  that we can use in (D.11). Using also
definition (5.10), we obtain

   ~-1  L^V  ~ = LV              1                        =: V             (D.13)
                             + 2 divgV

as operators on spinors in Sg. In other words, the g-representation on the D/^g-eigenspaces
E^m determined by the derivatives L^V is transported by the isometry of Hilbert spaces
~-1 : L2(S^g)  L2(Sg) to the representation  on the image spaces ~-1(E^m). Thus, if we
simply define Wm, := ~-1(E^m,), the isometry ~-1 will take the orthogonal decomposi-

tions (D.7) and (D.8) to the orthogonal decomposition

             L2(Sg) =        nm, Wm, ,                                     (D.14)

                       mZ 

with the restriction of  to the subspace Wm, being equivalent to the irreducible g-
representation . Since the Lie group G is compact connected, the g-representations on

                         49
the subspaces Wm, can be exponentiated, leading to a G-representation on the space of
spinors on Sg which we also call .

    Finally, to conclude the proof of proposition 6.2, it is enough to observe that when G
acts isometrically on (K, g), then g^ = g, the automorphisms  = ~ = I are trivial, and
Wm, = E^m,  E^m = Em.

Proof of proposition 6.3. Suppose that K is even-dimensional. Recall the definitions

in the previous proof and consider again the g-representation on the finite-dimensional
D/^g-eigenspaces E^m determined by the derivatives L^V . The chirality operator K satisfies

KK = 1 and anti-commutes with the Dirac operator. So K commutes with the square
(D/^g)2 and preserves its eigenspaces E^0 and E^m  E^-m, for all m > 0. This allows us to
decompose the (D/^g)2-eigenspaces as a sum of chiral subspaces

E^0 = E^0+  E^0-             E^m  E^-m = E^m+  E^m-  (D.15)

for m > 0. Now, the chirality operator K always commutes with Kosmann-Lichnerowicz
derivatives. So the g-representation determined by the L^V preserves the chiral subspaces
E^m�. Thus, we can decompose these subspaces as a sum of irreducible representations,

E^m� =            nm, E^m�,  for all m  0 .          (D.16)


As discussed in section 5.2 of [20], the integers nm, are the same for both decompositions
�. For m > 0, this happens because the Dirac operator determines a g-equivariant
isomorphism between E^m+ and E^m-. For m = 0, the proof uses an index result of Atiyah
and Hirzebruch [22, 68]. Thus, all in all, we get the orthogonal decomposition

L2(S^g) =               nm, (E^m+,  E^m-,) .         (D.17)

                  mN0 

This decomposition can be transported to the spinor bundle Sg through the isometry ~-1 :
L2(S^g)  L2(Sg) defined in the proof of proposition 6.2, more precisely in (D.10). Due
to (B.6), the maps ~ and ~-1 commute with the chirality operators, and hence preserve
the chiral subspaces. So if we define the subspaces of Weyl spinors Wm�, := ~-1(E^m�,)
inside (Sg), we get the orthogonal decomposition (6.4) stated in the proposition.

    Finally, when G acts isometrically on (K, g), then g^ = g, the derivatives LV commute
with D/ g for all V in g, and the automorphisms  = ~ = I are trivial. In this case, we
have the identity Wm�, = E^m�, = Em�,. For m > 0, the space Wm+,  Wm-, is the same
as the (D/ g)2-eigenspace Em+,  Em-,, which, in turn, can be decomposed according to the

                        50
D/ g-eigenvalues as Em,  E-m,.

Proof of remark 6.1. The only assertions that remain to be proved concern the mul-
tiplicities of the representations. To this end, observe that, when the dimension of K is
not 1 (mod 4), there exist conjugation maps j+ of spinors on Sg and Sg^. This follows
from the construction of the set (4.1) in proposition 4.1. These maps commute with the
Dirac operator and Kosmann-Lichnerowicz derivatives on the respective bundles, as fol-
lows from (4.7) and (4.6). So j+ preserves the D/^g-eigenspaces E^m in decomposition (D.8)
and is equivariant with respect to the g-action on them. This implies that the g-action
on E^m is self-conjugate. In particular, the irreducible g-spaces of complex type inside
E^m will always appear in conjugate pairs. Thus, we have nm, = nm, in decomposition
(D.8). Since the multiplicities nm, are the same in decompositions (D.8) and (6.3), by
construction of the latter, we conclude that nm, = nm, also holds in (6.3).

    When K has dimension 0, 2, 7 (mod 8), the conjugation j+ defines a real structure on
E^m, as follows from (4.4). So the quaternionic summands in decomposition (D.8) must
appear with even multiplicity (see [69, ch. II, sec. 6, exercise 10]). When K has dimension
3, 4, 6 (mod 8), the conjugation j+ defines a quaternionic structure on E^m. So the real
summands in (D.8) must appear with even multiplicity. Once again, these properties of
the multiplicities in decomposition (D.8) are directly transferable to decomposition (6.3),
which finishes the proof.

Proof of remark 6.2. This remark only deals with even-dimensional K. From the proof
of proposition 6.3, we know that the g-action preserves the D/^g-eigenspaces E^m and the
chiral spaces E^m� in (D.16). From the proof of remark 6.1, we know that j+ is g-equivariant
and preserves all the eigenspaces E^m.

    Thus, when K has dimension 0 (mod 4), it follows from the commutation relation
(4.8) in Riemannian signature that the conjugation map j+ also preserves the chiral
spaces E^m�. This implies that the g-representation on E^m� is self-conjugate. In particular,
the irreducible g-spaces of complex type inside E^m+ will always appear in conjugate pairs.
Thus, nm, = nm, in decompositions (D.16) and (D.17). Moreover, when K has dimension
0 (mod 8), the conjugation j+ defines real structures E^m�, as follows from (4.4). So
the quaternionic summands in decomposition (D.16) must appear with even multiplicity
(see [69, ch. II, sec. 6, exercise 10]). When K has dimension 4 (mod 8), the conjugation
j+ defines quaternionic structures on E^m�. So the real summands in (D.16) must appear
with even multiplicity. Since the properties of the multiplicities in decomposition (D.17)

                                                       51
are directly transferable to decomposition (6.4), as before, this finishes the proof of all
the assertions about dimension 0 (mod 4).

    When K has dimension 2 (mod 4), we know that j+ preserves the eigenspace E^0 and
the sums E^m  E^-m = E^m+  E^m- for m > 0. Since j+ is g-equivariant, it follows that the
g-action on these spaces must be self-conjugate. So the irreducible g-spaces of complex
type inside E^0 and E^m+  E^m- will always appear in conjugate pairs. This is possible only
if nm, = nm, in decomposition (D.17). Again, this equality of multiplicities is directly
transferable to decomposition (6.4), as desired.

Proof of lemma 6.4. Suppose that K has odd dimension k. Then only one of the
conjugation maps exists, as follows from (4.1). When k = 1 (mod 4), it is j+. This
map commutes with the G-action on spinors and preserves the representation spaces
Wm =  nm, Wm,. Since the Wm, are irreducible, the G-invariant conjugation will
preserve some of them and will map isomorphically pairs of others. The preserved ones
must correspond to real or quaternionic representations . In the real case, Wm, has a
complex basis consisting of j+-invariant vectors. In the quaternionic case, Wm, has a
complex basis consisting of pairs of vectors that are swapped by j+, up to a sign. In the
case of spaces Wm, that are not preserved by j+, but are instead mapped isomorphically
in pairs, it is enough to choose a complex basis of the first space in the pair, and then
apply j+ to define a basis of the second space in the pair. Uniting the bases in all these
cases, we get a basis of Wm with the required properties.

    When K has dimension 3 (mod 4), only j- exists. This conjugation commutes with the
G-action and maps the representation spaces Wm and W-m isomorphically. For m > 0,
take a complex basis {m } of Wm formed by spinors in the irreducible subspaces Wm,.
Then the set {m , j-(m )} forms a basis of Wm  W-m with the required properties. For
m = 0, we know that j- is G-equivariant and preserves W0. So an argument similar to
the one used in the case of dimension 1 (mod 4) guarantees the existence of the required
basis also for W0.

    Now suppose that K has even dimension. The two conjugations exist simultaneously
and are G-equivariant. When K has dimension 2 (mod 4), the two conjugations map Wm+
isomorphically to Wm-. Pick a basis {(m+)} of Wm+ formed by spinors in the irreducible
subspaces Wm+,. Then the set {(m+), j+(m+)} forms a basis of Wm+  Wm- whose
elements simply get swapped by j+, up to a phase. Since these basis elements are chiral
and j- =  K j+, according to (4.9), we recognize that also j- acts on them by simple
swappings of pairs and multiplication by phases, as desired.

    Finally, when k = 0 (mod 4), both commute with the chirality operator K and

                                                       52
preserve the spaces Wm� =  nm, Wm�,. So an argument similar to the one used in
the case of dimension 1 (mod 4) guarantees the existence of bases of Wm+ and Wm- whose
elements are in the respective irreducible spaces and are either invariant or get swapped
in pairs by j+. Since these bases are made of chiral elements, it follows again from the
identity j- =  K j+ that also j- acts on them as desired.

E. An example with (SU(3) � SU(2) � U(1))/Z6 symmetries

The approach to Kaluza-Klein models followed in this paper is quite general. We have
allowed the internal space K to be an arbitrary compact spin manifold, only sometimes
restricting it to even dimensions. While the properties established in this manner become
robust and transverse, it is also interesting to delve into explicit models, with particular
choices of internal geometry. This is indispensable from a physical viewpoint, as one tries
to find the specific geometries that, after dimensional reduction, most closely resemble
the properties of the Standard Model. Studying explicit examples, however, is no easy
task in spin geometry. There are very few examples of compact manifolds in which the
Dirac operator is explicitly understood, with its spectrum of eigenvalues, eigenspaces, and
spinor representations of the isometry group [61]. The purpose of this appendix is to point
out a particular geometry that may be interesting to further investigate. The motivation
comes from a speculative physical scenario outlined in [18].

    Let K be the 8-dimensional group manifold SU(3) equipped with its bi-invariant met-
ric, which is unique up to a scale factor. This metric is Einstein, has positive curvature,
and isometry group (SU(3) � SU(3))/Z3. As described in section 6, the action of this
group on K can always be lifted to an action of SU(3) � SU(3) on the spinors over K.

    The bi-invariant metric on SU(3) is an unstable saddle point of the Einstein-Hilbert
action under TT-deformations of the metric, not a local maximum. Most TT-deformations
of the bi-invariant metric reduce its scalar curvature, but a particular deformation found
in [70] takes the scalar curvature up to positive infinity. Since -RgK plays the role of
a potential for the internal metric in KK models, the initial bi-invariant metric should
unravel along that unstable direction. When this happens, the isometry group of the
metric is broken down to GSM = (SU(3) � SU(2) � U(1))/Z6, as pointed out in [18]. The
broken symmetries cause 4 gauge bosons to gain a mass at the Planck scale.

    The unraveling of the bi-invariant metric will continue indefinitely, leading to an in-
ternal space of infinite curvature, unless the Einstein-Hilbert Lagrangian is not the full
story and there are higher-order corrections to the action on M � K. If that is the case,
the correction terms can become relevant as the curvature of K grows, and can contribute

                                                       53
to stabilize the unraveling at a scale distinct from the Planck one. The stabilized metric
would define the KK internal vacuum. Due to the correction terms, its isometry group can
be further broken from GSM down to a smaller subgroup. This second symmetry breaking
happens at the mass scale of the correction terms (presumably the electroweak scale),
not at the Planck scale. So it could produce light gauge bosons, in principle, beyond the
already present 4 heavy ones.

    This story is a motivation to study the Dirac operator on SU(3) and the gauge rep-
resentations (6.1) induced on its spinors. First, using the simpler bi-invariant metric.
That would be already enough to get an idea of the spinor gauge representations, since
decompositions (6.3) and (6.4) into irreducibles preserve the structure of decompositions
(D.8) and (D.17) for the average metric. (Here, the more symmetric average metric is the
bi-invariant one.) The next step would be to understand the eigenspaces and eigenvalues
of the Dirac operator on the deformed metric with (SU(3) � SU(2) � U(1))/Z6 isometry
group. This metric is written down explicitly in [18]. The metric deformation can lift
degeneracies and make some of the initial Dirac eigenvalues (i.e. masses of 4D fermions)
much larger, and others smaller. With a SU(3) � SU(3) spinor representation on a mani-
fold with the smaller GSM isometry group, the relation between the representation spaces
and the D/ K-eigenspaces becomes non-trivial. Chiral interactions between the massive
gauge fields and the 4D fermions should now appear, as described in [20].

    The third step would be to study the Dirac operator on SU(3) equipped with a per-
turbed left-invariant metric that breaks the isometry group from GSM to SU(3) � U(1).
This is the perturbation that would presumably come from the higher-order corrections to
the Einstein-Hilbert Lagrangian, as described in the speculative scenario above. Explicit
metrics on SU(3) with this smaller isometry group and a Higgs-like parameter with values
in C2 are written down in [71]. See also the broader discussion in [72]. With those metrics,
3 more gauge bosons gain a non-zero mass, now at the perturbation scale.

    Now recall the suggestions about fermion generations made at the end of section 6.
With the notation of that section, the gauge group G is the maximal compact group
(SU(3) � SU(3))/Z3 acting effectively on K. The universal cover G~ is SU(3) � SU(3).
The centre of G~ is Z3 � Z3. The first Z3 factor lies inside G~, because the final vacuum
metric on gK is left-invariant with isometry group SU(3) � U(1), after the two stages of
symmetry breaking. So the first Z3 determines spinor transformations (possibly trivial)
that commute with the internal Dirac operator and do not change fermion masses in
the KK model. The second Z3 factor in the centre of G~ generically lies outside G~ 
SU(3) � U(1), apart from the identity element. Thus, in the KK model, that Z3 permutes
4D fermions in the same g-representations and with possibly different masses. These
transformations, if non-trivial, could relate three generations of 4D fermions.

                                                       54
    Finally, note that before the second stage of symmetry breaking, when the vacuum
isometry group was still GSM = (SU(3) � U(2))/Z3, the second Z3 would have lain inside
the isometric transformations in G~  SU(3) � U(2). In this case, that Z3 would not
have related fermions with different masses. It would act trivially or relate degenerate
fermions with the same mass. Since the second stage of symmetry breaking happens at
the perturbation scale, not at the Planck scale, we expect the distinct masses related by
the second Z3 in the final vacuum to differ by magnitudes of the order of the perturbation
scale (presumably, the electroweak scale), not in the order of the Planck scale.

                                                       55
References

 [1] J. Christenson, J. Cronin, V. Fitch and R. Turlay: Evidence for the 2 decay of the
      K20 meson, Phys. Rev. Lett. 13 (1964), 138�140.

 [2] V. Fanti et al.: A new measurement of direct CP violation in two pion decays of the
      neutral kaon, Phys. Lett. B 465 (1999), 335�348.

 [3] A. Alavi-Harati et al.: Observation of direct CP violation in KS,L   decays,
      Phys. Rev. Lett. 83 (1999), 22�27.

 [4] S. Navas et al. (Particle Data Group): Review of particle physics, Phys. Rev. D 110
      (2024), 030001.

 [5] M. Kobayashi and T. Maskawa: CP-violation in the renormalizable theory of weak
      interaction, Progr. Theor. Phys. 49 (1973), 652�657.

 [6] G. Branco, L. Lavoura and J. Silva: CP violation, Oxford Univ. Press, 1999.

 [7] I. Bigi and A. Sanda: CP violation, 2nd ed., Cambridge Univ. Press, 2016.

 [8] W. Thirring, Fivedimensional theories and CP-violation, Acta Phys. Austriaca 9
      (1972), 256�271.

 [9] M. Gavela and R. Nepomechie: Discrete symmetries in Kaluza-Klein theories, Class.
      Quantum Grav. 1 (1984), L21�L28.

[10] C. Wetterich: Discrete symmetries in Kaluza-Klein theories, Nucl. Phys B234
      (1984), 413�444.

[11] D. Chang and R. Mohopatra: Geometric CP violation with extra dimensions, Phys.
      Rev. Lett. 87 (2001), 211601.

[12] G. Branco, A. Gouv^ea and M. Rebelo: Split fermions in extra dimensions and CP
      violation, Phys. Lett. B 506 (2001), 115�122.

[13] C. Huang, T. Li, L. Wei and Q. Yan: CP violation and extra dimensions, Eur. Phys.
      J. C 23 (2002), 195�199.

[14] B. Grzadkowski and J. Wudka: Majorana fermions and CP violation from 5-
      dimensional theories: a systematic approach, Phys. Rev. D 72 (2005), 125012.

[15] C. Lim, N. Maru and K. Nishiwaki: CP violation due to compactification, Phys. Rev.
      D 81 (2010), 076006.

                                                       56
[16] J. Fr`ere, M. Libanov and S. Mollet: CP violation from pure gauge in extra dimensions,
      J. High Energ. Phys. 2014 (2014), 103.

[17] T. Ibrahim and P. Nath: CP violation from the standard model to strings, Rev. Mod.
      Phys. 80 (2008), 577�631.

[18] J. Baptista: Internal symmetries in Kaluza-Klein models, J. High Energ. Phys. 2024
      (2024), 178.

[19] J. Baptista: Test particles in Kaluza-Klein models, Class. Quantum Grav. 42 (2025),
      045007.

[20] J. Baptista: Chiral interactions of fermions and massive gauge fields in Kaluza-Klein
      models, arXiv:2506.09126 [hep-th].

[21] G. Chapline and R. Slansky: Dimensional reduction and flavor chirality, Nucl. Phys.
      B209 (1982), 461�483.

[22] E. Witten: Fermion quantum numbers in Kaluza-Klein theory, in Shelter Island II,
      Proc. of the 1983 Shelter Island conference, MIT Press, 1985.

[23] C. Wetterich: Massless spinors in more than four dimensions, Nucl. Phys. B211
      (1983), 177�188.

[24] C. Wetterich: Dimensional reduction of Weyl, Majorana and Majorana-Weyl spinors,
      Nucl. Phys. B222 (1983), 20�44.

[25] E. Witten: Search for a realistic Kaluza-Klein theory, Nucl. Phys. B186 (1981),
      412�428.

[26] M. Duff, B. Nilsson and C. Pope: Kaluza-Klein supergravity, Phys. Reports 130
      (1986), 1�142.

[27] D. Bailin and A. Love: Kaluza-Klein theories, Rep. Prog. Phys. 50 (1987), 1087�1170.

[28] R. Coquereaux and A. Jadczyk: Riemannian geometry, fiber bundles, Kaluza-Klein
      theories and all that...., World Scientific Publishing, 1988.

[29] L. Castellani, P. Fr�e and R. D'Auria: Supergravity and superstrings: a geometric
      perspective, Vol. 2, Part five, World Scientific Publishing, 1991.

[30] J. Overduin and P. Wesson: Kaluza-Klein gravity, Phys. Reports 283 (1997), 303�
      380.

                                                       57
[31] J. Bourguignon: A mathematician's visit to Kaluza-Klein theory, Rend. Sem. Mat.
      Univ. Politec. Torino (1989), 143�163.

[32] T. Kaluza: Zum Unitt�asproblem in der Physik, Sitzungsber. Preuss. Akad. Wiss.
      Berlin Math. Phys. K1 (1921), 966�972.

[33] O. Klein: Quantentheorie und fu�nfdimensionale Relativita�tstheorie, Zeitschrift Phys.
      37 (1926), 895�906.

[34] A. Einstein and P. Bergmann: On a generalization of Kaluza's theory of electricity,
      Annals Math. 39 (1938), 683�701.

[35] P. Jordan: Relativistische Gravitationstheorie mit variabler Gravitationskonstante,
      Naturwissenschaften 33 (1946), 250�251.

[36] Y. Thiry: Les �equations de la th�eorie unitaire de Kaluza, Comptes Rendus Acad.
      Sci. Paris 226 (1948), 216�218.

[37] B. DeWitt: Dynamical theory of groups and fields, in Lectures at 1963 Les Houches
      School, Gordon and Breach, 1964, 585�820.

[38] R. Kerner: Generalization of the Kaluza-Klein theory for an arbitrary non-abelian
      gauge group, Ann. Inst. H. Poincar�e 9 (1968), 143�152.

[39] Y. Cho: Higher-dimensional unifications of gravitation and gauge theories, J. Math.
      Phys. 16 (1975), 2029�2035.

[40] B. O'Neill: The fundamental equations of a submersion, Michigan Math. J. 13 (1966),
      459�469.

[41] C. Ehresmann: Les connexions infinit�esimales dans un espace fibr�e diff�erentiable,
      Colloque de Topologie (1950), 29�55.

[42] R. Hermann: A sufficient condition that a mapping of Riemannian manifolds be a
      fibre bundle, Proc. Amer. Math. Soc. 11 (1960), 236�242.

[43] A. Besse: Einstein manifolds, Classics in Mathematics, Springer-Verlag, 1987.

[44] M. Falcitelli, S. Ianus and A. Pastore: Riemannian submersions and related topics,
      World Scientific Publishing, 2004.

[45] A. Moroianu, Op�erateur de Dirac et submersions riemanniennes. Ph.D. thesis, E�cole
      Polytechnique, Paris, 1996.

                                                       58
[46] E. Loubeau and R. Slobodeanu: A characterization of Dirac morphisms, Commun.
      Math. Phys. 288 (2009), 1089�1102.

[47] P. Reynolds, On conformal submersions and manifolds with exceptional structure
      groups, PhD thesis, Univ. Edinburgh, 2011.

[48] M. Hamilton: Mathematical gauge theory: with applications to the Standard Model
      of particle physics, Universitext, Springer International Publishing, 2017.

[49] M. Stone: Gamma matrices, Majorana fermions, and discrete symmetries in
      Minkowski and Euclidean signature, J. Phys. A: Math. Theor. 55 (2022), 205401.

[50] M. Srednicki, Quantum field theory, Cambridge Univ. Press, 2007.

[51] H. Murayama: Notes on Clifford algebra and Spin(N) representations,
      http://hitoshi.berkeley.edu/230A/clifford.pdf .

[52] J. Figueroa-O'Farril: Majorana Spinors, https://www.maths.ed.ac.uk/~jmf/
      Teaching/Lectures/Majorana.pdf

[53] A. Lichnerowicz: Spineurs harmoniques, Comptes rendus Acad. Sc. Paris, groupe 1
      257 (1963), 7�9.

[54] Y. Kosmann: D�eriv�ees de Lie des spineurs, Ann. di Matematica Pura ed Applicata
      91 (1971), 317�395.

[55] J. Bourguignon and P. Gauduchon: Spineurs, op�erateurs de Dirac et variations de
      m�etriques, Comm. Math. Phys. 144 (1992), 581�599.

[56] A. Hermann: Dirac eigenspinors for generic metrics, PhD thesis, Univ. Regensburg,
      2012.

[57] M. Wang: Preserving parallel spinors under metric deformations, Indiana Univ.
      Math. J. 40 (1991), 815�844.

[58] J. Bourguignon, O. Hijazi, J. Milhorat, A. Moroianu and S. Moroianu: A spinorial
      approach to Riemannian and conformal geometry, European Mathematical Society,
      2015.

[59] H. Lawson and M. Michelsohn: Spin geometry, Princeton Univ. Press, 1989.

[60] E. Witten, Fermion path integrals and topological phases, Rev. Mod. Phys. 88 (2016),
      35001�40.

                                                       59
[61] N. Ginoux: The Dirac spectrum, Springer, 2009.
[62] B. Dolan: On the elimination of Pauli couplings in Kaluza-Klein theories using tor-

      sion, Phys. Letters 159B (1985), 279�283.
[63] M. Atiyah, R. Bott and A. Shapiro: Clifford modules, Topology. 3 (1964), 3�38.
[64] T. Friedrich: Zur Abha�ngigkeit des Dirac-Operators von der Spin-Struktur, Coll.

      Math. 48 (1984), 57�62.
[65] H. Baum: Spin-Strukturen und Dirac-Operatoren u�ber pseudoriemannschen Mannig-

      faltigkeiten, B. G. Teubner, 1981.
[66] C. Ba�r: Spin geometry, Lecture notes, Univ. Potsdam, 2011.

      https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Geometrie/
      Dokumente/Lehre/Veranstaltungen/SS11/spingeo.pdf
[67] J. Lee, Introduction to Riemannian manifolds, 2nd ed., Springer, 2018.
[68] M. Atiyah and F. Hirzebruch: Spin-manifolds and group actions, in Essays on To-
      pology and Related Subjects, Springer-Verlag, 1970, 18�28.
[69] T. Brocker and T. Dieck: Representations of compact Lie groups, Graduate texts in
      Mathematics, Springer-Verlag, 1985.
[70] G. Jensen: The scalar curvature of left invariant Riemannian metrics, Indiana Univ.
      Math. J. 20 (1971), 1125�1143.
[71] J. Baptista: Higher-dimensional routes to the Standard Model bosons,
      arXiv:2105.02899 [hep-th].
[72] R. Coquereaux: About left-invariant geometry and homogeneous pseudo-Riemannian
      Einstein structures on the Lie group SU(3), arXiv:2107.12285 [math.DG].

                                                       60
