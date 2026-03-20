# 2025 Chiral interactions fermions massive gauge fields KK

**Source:** `17_2025_Chiral_interactions_fermions_massive_gauge_fields_KK.pdf`

---

arXiv:2506.09126v1 [hep-th] 10 Jun 2025         Chiral interactions of fermions and
                                         massive gauge fields in Kaluza-Klein models

                                                                               Joa~o Baptista
                                                                                  June 2025

                                                                                  Abstract

                                         In Kaluza-Klein theory, gauge fields on M4 arise as components of a higher-dimensional
                                         metric defined on M4 � K. The traditional expectation is that all the gauge fields of the
                                         Standard Model are linked to exact Killing vector fields on the internal space. This paper
                                         questions that assumption and investigates the properties of 4D gauge fields linked to
                                         non-Killing fields on K. It is shown that they have massive yet arbitrarily light bosons;
                                         they can mix fermions with different masses; and they can have asymmetric couplings
                                         to left- and right-handed fermions. None of these properties is easily satisfied by gauge
                                         fields linked to internal isometries. So the massive gauge fields produced in this manner
                                         circumvent traditional no-go arguments and offer a geometric source of chiral interactions
                                         with fermions. This may help to model the weak force within the Kaluza-Klein framework.
                                         Technically, the paper uses the language of spin geometry and Riemannian submersions.
                                         It studies the higher-dimensional Dirac operator with non-trivial background metrics.
                                         The results are derived for a general K. They are illustrated explicitly in the simpler
                                         cases where K is the two-sphere and the two-torus.

                                         Keywords: Kaluza-Klein theories; chiral fermions; Riemannian submersions; Dirac operator;
                                         weak force.
Contents

1 Introduction and overview of results . . . . . . . . . . . . . . . . . . . . . . . . . 1
2 Spinors on Riemannian submersions . . . . . . . . . . . . . . . . . . . . . . . . . 9
3 Higher-dimensional Dirac operator . . . . . . . . . . . . . . . . . . . . . . . . . 14
4 Properties of the Kosmann-Lichnerowicz derivative . . . . . . . . . . . . . . . . 18
5 Chiral fermions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
6 Explicit example: K = T 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
7 Explicit example: K = S2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
8 Conserved currents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
Appendices
A Fibre-integral projection of a vector field . . . . . . . . . . . . . . . . . . . . . . 36
B Proofs for section 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
C Proofs for sections 5 and 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44

                                                         i
1. Introduction and overview of results

The weak force is a special interaction in the Standard Model. Notable properties that
distinguish it from the strong and electromagnetic forces include:

1. It has massive gauge bosons;
2. It mixes fermions with different masses;
3. It has asymmetric (chiral) couplings to left- and right-handed fermions.

This paper describes how, in a general Kaluza-Klein framework, these three properties
of 4D gauge fields are manifestations of a single higher-dimensional feature. So the three
properties should generally appear together. Massive gauge bosons, however light, should
have chiral interactions with fermions, whereas massless gauge bosons should not.

    To introduce that higher-dimensional feature, recall that Kaluza-Klein theory encodes
4D gauge fields as components of a metric defined on P = M4 � K. The usual assumption
is that all the gauge fields of the Standard Model are linked to isometries of the internal
vacuum metric. In other words, they are linked to exact Killing vector fields on K [1�6].
This paper probes that assumption and shows that a 4D gauge field linked to non-Killing
vector fields will in general exhibit properties 1, 2 and 3, while a gauge field linked to
isometries of K will not. So the standard view appears well-founded in the case of the
strong and electromagnetic fields. However, it may be preferable to link the weak gauge
field to non-Killing vector fields on K that are small perturbations of Killing ones.

    Non-Killing vector fields generate non-isometric diffeomorphisms of the internal space.
These transformations do not preserve the vacuum metric gK but do preserve the Einstein-
Hilbert action, which is diffeomorphism-invariant. This is reminiscent of the standard
Brout-Englert-Higgs mechanism [7�9], which uses gauge transformations that preserve the
action but do not preserve the vacuum value of the Higgs field. The internal metric gK
can therefore be understood as a more geometrical version of the traditional Higgs fields.
This is apparent from the decomposition of the higher-dimensional scalar curvature RgP
in the Einstein-Hilbert action,

  RgP volgP =     RgM  +  RgK  -  1  |FA|2  -  1  |dAgK |2  +  |dA (volgK )|2  volgP .  (1.1)
                                  4            4
P              P

This formula extends the usual Kaluza-Klein result to the setting of general Riemannian
submersions, where the geometry of the fibres can change. For more details, see [10, 11].
As in [10], one can then calculate that a 4D gauge boson linked to a divergence-free vector

                                     1
field ea on K has a classical mass given by

Mass Aa� 2   K Lea gK , Lea gK  volgK ,         (1.2)
               2 K gK (ea, ea) volgK

where LeagK denotes the Lie derivative of the internal vacuum metric along ea.

    Formula 1.2 is significant. It suggests that massive gauge fields, however light, should
not be linked to exact isometries of gK. The derivatives LeagK can be small yet non-zero.
Thus, a natural way to obtain light gauge bosons within the Kaluza-Klein framework is to
start with an internal metric with a large isometry group, for example an Einstein metric,
and assume that a perturbation operating at a different scale2 slightly shifts the vacuum
metric and breaks its isometry group. Some Lie derivatives LeagK will then become non-
zero and the corresponding gauge fields will become massive. If the perturbation is small,
the masses will be small too. Once those gauge fields are linked to non-Killing vector
fields on K, they can satisfy conditions 1, 2 and 3.

    Among the three listed properties of gauge fields linked to non-Killing internal fields,
the least predictable one is perhaps the emergence of chiral interactions with fermions.
In fact, the literature has several no-go arguments against the existence of chiral fermions
in Kaluza-Klein models. Firstly, the basic Kaluza-Klein mechanism to explain 4D chiral
fermions relies on the correlation between internal and 4D chiralities, which only works
when K is even-dimensional [12�14]. But an analysis of conjugation in the spin represent-
ations excludes internal spaces of dimension 4k [13�16]. Additionally, a prominent no-go
argument presented by Witten in [14] excludes all internal spaces with even dimensions.
This argument is based on an index result of Atiyah and Hirzebruch [17], so remains valid
even if the Dirac operator is continuously deformed, for instance through the addition of
torsion to the metric connection.

    Nonetheless, an inspection of these no-go arguments reveals a common assumption:
that all 4D gauge fields of interest are linked to exact Killing vector fields on K. Thus,
gauge fields linked to non-Killing fields on K have the potential to evade the arguments,
as noted in [10]. Even light 4D gauge fields, linked to very small perturbations of internal
Killing fields, should be able to evade the no-go arguments. This paper confirms this is
indeed the case. It shows that arbitrarily light gauge fields have chiral interactions with
fermions. Explicit examples are given when K = S2 and K = T 2.

    There are other well-known proposals in the literature to circumvent the no-go argu-
ments against chiral fermions in Kaluza-Klein. For example, one can add to the model
gauge fields living on the higher-dimensional spacetime [12, 13, 18�21]. The additional

2Presumably, a higher-order correction to the Einstein-Hilbert action, or a quantum effective potential.
 In the usual Higgs mechanism, the ad-hoc Higgs potential forces the shift of the vacuum.

                                             2
fields will twist the internal Dirac operator and can lead to the appearance of fermionic
zero modes with chiral interactions. One can also use non-compact internal spaces [22].
One can construct models using generalized versions of Riemannian geometry [22�24].
One can consider metric connections with topologically non-trivial torsion [25,26]. And a
fifth, prominent strategy is to abandon the smoothness assumption and consider vacuum
internal spaces with singularities, for example orbifolds. Then one can impose chiral
boundary conditions at the singularity and obtain models with 4D chiral fermions [27�34].

    To this author's prejudice, however, the mechanism proposed in the present paper
seems somewhat more natural. It does not introduce any new bosonic fields besides
the higher-dimensional metric, in accordance with the original Kaluza-Klein philosophy.
Chiral interactions follow from the properties of the standard Dirac operator in higher-
dimensions, with no need for more complicated operators. It uses smooth, compact in-
ternal spaces and the ordinary version of Riemannian geometry. And, importantly, the
fermionic interactions generated in this manner can be chiral only for gauge fields with
non-zero mass, as observed in nature.

    Extended reviews of the Kaluza-Klein framework can be found in [1�6, 35]. Some of
the early original references are [36�43]. This paper follows the notation and treatment
given in [10, 44] of massive gauge fields and Higgs-like scalars. More comments about the
literature will be added below, as we give an overview of the main results in the paper.

Overview of the general results

Section 2 starts by describing properties of spinors on the manifold P = M4 � K equipped
with a metric gP  (gM , A, gK) defining a Riemannian submersion. These metrics gener-
alize the Kaluza ansatz by encoding not only the 4D metric and 4D massless gauge fields,
but also massive gauge fields and an internal metric gK that can change along M4. The
main classical results about Riemannian submersions were developed by O'Neill in [45],
after foundational work in [46,47]. They are presented in [11,48], for example. We use the
translation of those results to the Kaluza-Klein language provided in [10], which considers
the case of general fibres that need not be totally geodesic. Spinors on general Riemannian
submersions have been previously studied by Moroianu [49] and, later, by Loubeau and
Slobodeanu [50] and Reynolds [51] for general conformal submersions. Section 2 reframes
that geometric setting in the explicit language suitable for Kaluza-Klein physics.

    Section 3 uses that same language to describe the covariant derivatives of spinors over
Riemannian submersions. They split into derivatives along vertical fields (vector fields
on K) and along horizontal fields (lifts of vector fields on M4). These two cases come
together in the expression for the standard Dirac operator on P = M4 � K. This formula

                                                        3
is spelled out in proposition 3.8, for the case of a constant internal metric gK, and in
proposition 3.3 for the general case. Although mathematically equivalent to a special
case of the formulae given by Reynolds in [51], the expressions given in these propositions
look quite different. They have two advantages for our purposes. First, they use the
physical language of Kaluza-Klein models. Second, by explicitly developing certain terms
left unexpanded in [51], they show that general gauge fields couple to 4D spinors through
the Kosmann-Lichnerowicz derivative LX of the internal component of those spinors.
This fact is well-known in the physics literature for gauge fields linked to internal Killing
vector fields [14, 16]. The generalization to gauge fields linked to a non-Killing X over a
general Riemannian submersion does not seem to have been established yet. Thus, very
schematically, one can write

              D/ P  =   3   � (� + A�a Lea)  + D/ K  + � � � ,

                                                                                   (1.3)

                       �=0

where  is a higher-dimensional spinor and D/ P and D/ K denote the standard Dirac op-
erators on P and K. When  is an eigenspinor of the internal Dirac operator, the term
D/ K  produces a mass term in four-dimensions, as is customary in Kaluza-Klein models.
The gauge fields have values in the Lie algebra of vector fields on K. So the {ea} form a
basis of such vector fields. Some of them will be Killing and others non-Killing.

Due to its appearance in decomposition (1.3), the Kosmann-Lichnerowicz derivative

LX plays a major role in this story. So we take section 4 to collect useful properties
of this operator for non-Killing X. Almost all of them can be found in the literature

in the Riemannian case [52, 53], but are somewhat dispersed and stated using various
conventions. One property that is especially relevant for us is the commutator [LX, D/ K].

Given a vector field X and a spinor  on (K, gK), that commutator is

[D/ K, LX ]      1     (LX gK )(vi, vj) vi � vj  +                                 (1.4)
              =
                    i,j
                 2

                    1
              +             [vi(LX gK )](vi, vj) - [vj (LX gK )](vi, vi)  vj �  .
                 4 i,j

Here  denotes the Levi-Civita connection and LXgK is the Lie derivative of gK along
X. The {vj} are a local, orthonormal trivialization of the tangent bundle T K. So the
commutator vanishes when X is a Killing vector field, but in general does not. In light of
(1.3), this says that a gauge field A�a will mix fermions with different masses only when
the respective vector field ea is not Killing on K. This is one reason why the weak gauge
field should be linked to non-Killing internal vector fields.

    Now assume that K is even-dimensional and let K denote the complex chirality
operator on K, normalized so that (K)2 = 1. We can decompose the complex spinor

                            4
bundle  as  SC (K )  =  S + (K )   S-(K)   and  write  each  spinor  as  a  sum  of  chiral  components,
                          C             C

                      = + + -                   with      �  =  1                            (1.5)
                                                                2 (1 � K)  .

The Kosmann-Lichnerowicz derivative LX always commutes with K. So it preserves the
spaces of sections of the half-spinor bundles, denoted V �. These are infinite-dimensional
spaces of Weyl spinors. The question we want to study in section 5 is whether LX acts
similarly on V + and V -. Using the standard assumption of correlation between 4D and
internal chiralities [14], that is equivalent to asking whether the gauge field linked to X
acts symmetrically on left- and right-handed 4D spinors.

    When LX acts similarly on V + and V -, we say that it has chiral symmetry. This
notion should imply an identity of matrix elements +, LX+ = -, LX- for all D/ K-
eigenspinors  and  with positive eigenvalues. In fact, in section 5 we will distinguish

two notions of chiral symmetry: when that identity holds exactly (strong symmetry), and
when it holds only up to a unitary redefinition of the D/ K-eigenspinors (weak symmetry).

In the latter case, the redefinitions must respect the mass eigenvalues and the symmetries

of spinors induced by the isometry group of gK.
    Let us probe the main question. Consider two D/ K-eigenspinors m and m with

positive eigenvalues m and m. The Dirac operator anti-commutes with K and is formally
self-adjoint with respect to the L2-inner-product of spinors. The operator K is self-adjoint
with respect to that same product. So a simple calculation yields

    m, [D/ K, LX ] K m  volgK = (m + m)  K m, LX m  volgK                                    (1.6)

K                                                      K

                                  = (m + m)                m+ , LX m+  -  m- , LX m-  volgK .

                                                       K

When X is Killing on K, the commutator [D/ K, LX] vanishes and the matrix elements of
LX are the same on left- and right-handed spinors. When X is not Killing, LX should
in general act differently on m+ and m-. So it will not have strong chiral symmetry.

    The traditional no-go arguments against the existence of chiral fermions in Kaluza-
Klein models are encapsulated in the following important result:

Proposition 1.1 ([14, 17]). If X is a Killing vector field on a compact, connected, even-
dimensional spin manifold K, the derivative LX has strong chiral symmetry.3

     This symmetry, together with the correlation between internal and 4D chiralities,
 forces all massless gauge fields to have the same couplings to left- and right-handed 4D
 fermions. The main message of the present paper, in contrast, is that this property of LX

3This result does not follow directly from (1.6) because that formula is uninformative when m = m = 0.

                                                5
is specific to Killing fields. It should not be generic. It will not hold for most non-Killing
vector fields on K, even if they are small perturbations of Killing fields. In fact, the
explicit calculations on the sphere described in section 7 show that:

Proposition 1.2. Let X be a generic divergence-free vector field on K = S2 equipped
with its unique spin structure. Then the derivative LX of spinors does not have strong
chiral symmetry.

    The calculations on the torus described in section 6 go further. They show that it is
not possible to rotate the eigenspinors of D/ within their eigenspaces so that the action of
LX on V + looks similar to its action on V -.
Proposition 1.3. Let X be a generic Hamiltonian vector field on the torus K = T 2
equipped with its trivial spin structure. Then the derivative LX does not have strong nor
weak chiral symmetries.

    The precise definitions of strong and weak chiral symmetries are given in section 5.2.
The fact that LX does not have such symmetries for a non-Killing X should hold much
more generally, beyond the simple cases illustrated in this paper.

    Thus, the broad picture provided in this paper is that the solutions of the equation
D/ P  = 0 do not involve chiral fermionic interactions in regions where the background
metric is a simple product, gP = gM + gK, or where it is a submersion metric gP 
(gM , A, gK) with constant gK and only massless gauge fields. In regions where massive
gauge fields are present, in contrast, the background geometry becomes very different
from a product and, in general, chiral fermionic interactions will emerge.

Explicit example: K = S2

Choose K = S2 equipped with its round metric and unique spin structure. Its space of
spinors has an infinite basis formed by eigenspinors l, n of the internal Dirac operator.
Each eigenspinor determines the properties of the 4D fermion  coupled to it in the tensor
product  =   l, n, which is a spinor over M4 � S2. The half-integer l accounts for
the D/ K-eigenvalue of l, n. It determines the 4D mass of . The half-integer n is in the
range {-l, -l +1, . . . , l} and reflects the eigenvalue of l, n under the action of the internal
operator L. Here  is the Killing vector field generating azimuthal rotations on S2.
That eigenvalue measures the charge of  when responding to the massless 4D gauge field
linked to , as follows from (1.3). Thus, the only characteristic numbers of 4D fermions
in this model are their mass and -charge.

    Now suppose that a 4D gauge field is linked to an internal, divergence-free vector field
X on S2. On the sphere, X is necessarily the Hamiltonian vector field Xh of some real

                                                        6
function h. This simplifies the calculation of LXh. For example, when acting on the

internal        spinor        1      ,  1,   a     direct  computation          in    section  7.2  says    that
                                  2
                                        2

              l+, n ,         LXh         +          -    l-, n  ,  LXh   -           volgK    =

  S2                                      1  ,  1                         1  ,  1
                                          2     2                         2     2

                                                           =        i l+n 3                         1         Y0                  volgK  .  (1.7)
                                                                                   l- l-                                       h
                                                                    8 2 l             2             2     S2  l-  1  ,  n-  1
                                                                                                                  2         2

Here  Y0        1          1  denotes              the  scalar      spherical      harmonic       on   S2.    This formula shows that
        l-      2   ,  n-  2

the massive 4D gauge field linked to Xh will generically have chiral interactions with the

lightest 4D fermion, i.e. with the fermion  appearing in the higher-dimensional spinor

      1      ,  1.     The amount of chirality depends on Xh through the harmonic components
          2
                2

of the Hamiltonian function h. One can check that for the Killing choice Xh =  the

right-hand side of (1.7) always vanishes. Note also that chirality is manifest only in the

higher  mass           components of                 LXh    , 1     ,  1  namely,     in the  components      with      l      5/2.  Returning
                                                               2       2

to the Kaluza-Klein model over M4 � S2, this means that the lightest 4D fermions can

have chiral interactions only when higher mass fermions are also involved, not when the

interaction involves only the lightest fermions.

Explicit example: K = T 2

The simplest example to calculate is when K is the two-torus T 2 = R2/Z2 with its
flat metric and trivial spin structure. Then the Dirac operator D/ K has eigenspinors

l1, l2 characterized by two integers (l1, l2)  Z2. The spinors l1, l2 together with their
counterparts K l1, l2 form a basis of the space of all spinors on T 2. The kernel of D/ K is

spanned by 0, 0 and K 0, 0. The eigenspinors of the Dirac operator on the flat torus,

for all possible spin structures, are described in [54, 55].

    Each eigenspinor l1, l2 determines the properties of the 4D fermion  coupled to it in
 =   l1, l2, which is a spinor over M4 � T 2. For instance, the integer lj determines
the charge of  with respect to the 4D gauge field linked to the Killing field xj on K.
Here (x1, x2) are the periodic Euclidean coordinates on the torus.

    Now consider a 4D gauge field linked to an arbitrary vector field X on T 2, not ne-

cessarily Killing. It couples to fermions through the derivative LX. Decompose the
D/ K-eigenspinors as sums of Weyl components, l1, l2 = l+1, l2 + l-1, l2. Section 6 shows that

                              LX        �            =    2i (X1l1 + X2l2) l�1, l2                i   div(J   X)  l�1,  l2  ,               (1.8)
                                          l1, l2                                                  4

where J denotes the complex structure on T 2. So when div(JX) is not zero, LX will act
differently on V + and V - and will not have strong chiral symmetry. The Killing vector

                                                                                   7
fields J xj , however, do have vanishing divergence on T 2. So the Lxj and their linear
combinations define the same T 2-representations on V + and V -, as expected.

    Finally, denote by LX� the restriction of the Kosmann-Lichnerowicz derivative to V �.
Consider the simpler case where Xh is a Hamiltonian vector field determined by a function
h on the torus. Section 6 also establishes that, for a generic Xh, there exists no invertible,
unitary, T 2-equivariant linear map  : V +  V - that commutes with D/ 2 and satisfies
-1LX-h = LX+h. So LXh does not have weak chiral symmetries.

Conserved currents and an additional comment

Section 8 briefly investigates the conserved currents associated with solutions of the Dirac
equation on P . Proposition 8.1 describes a natural relation between higher-dimensional
and 4D currents. This follows from a general procedure to average higher-dimensional
vector fields along the fibres of P , described in appendix A. Section 8 also defines charge
currents associated with Killing vector fields on P .

    Now a final note. This paper investigates the properties of spinors satisfying the
higher-dimensional Dirac equation D/ P  = 0, or the Weyl equation with constraints
P  = �. It studies how these spinors couple to the 4D objects that determine the
background metric on P , such as the metric gM , the gauge fields A�a, and the Higgs-like
scalars coming from the components of gK. These couplings determine how the higher-
dimensional spinors are perceived in 4D. In this paper we are primarily concerned with the
features that produce chiral interactions of fermions and 4D gauge fields. However, let us
also mention a different point. A very well-known and elegant feature of the Kaluza-Klein
framework is that the massless equation D/ P  = 0 produces non-zero mass terms in the
4D Dirac equation, after dimensional reduction. This also arises in section 3, of course.
Thus, if D/ P  = 0 or its Weyl counterpart were the physical equations of motion, this
would mean that the fermionic masses observed in 4D are entirely due to the vibration of
the higher-dimensional spinor along the internal space. In the heuristic picture provided
by geodesics, this corresponds to the statement that the 4D rest energy of test particles
is entirely due to their internal motion along K. As stressed in [44], this is equivalent to
saying that elementary particles always travel at the speed of light in higher dimensions.
It is the projection of velocities to three dimensions that appears to produce speeds in
the range [0, c], as observed macroscopically. This simple and attractive picture is one of
the conceptual rewards of working with a higher-dimensional spacetime.

                                                        8
2. Spinors on Riemannian submersions

2.1. Riemannian submersions

This section describes properties of spinors on manifolds equipped with metrics defining
Riemannian submersions. These metrics generalize the Kaluza ansatz by encoding not
only the 4D metric and 4D massless gauge fields, but also massive gauge fields and an
internal metric that can vary along M4. The main classical results about Riemannian
submersions were developed in [45�47] and are presented in [11, 48], for example. We use
the translation of those results to the Kaluza-Klein language provided in [10]. Spinors on
Riemannian submersions have been previously studied in [49] and more generally in [51].
In this section, we introduce all the notation and reframe the geometric formalism using
the explicit language suitable for Kaluza-Klein physics. It does not present new results.

    Take a Lorentzian metric gP on the higher-dimensional space P = M4 � K such
that the projection P  M4 is a Riemannian submersion. As described in [10], this is
equivalent to taking a gP determined by three simpler objects:

 i) a Lorentzian metric gM on the base M4;

ii) a family of Riemannian metrics gK(x) on the fibres Kx parameterized by the points
     x  M4;

iii) a gauge one-form A on M4 with values in the Lie algebra of vector fields on K.

These objects determine the higher-dimensional metric through the relations

gP (U, V ) = gK(U, V )                                                       (2.1)
gP (X, V ) = - gK (A(X), V )
gP (X, Y ) = gM (X, Y ) + gK (A(X), A(Y )) ,

valid for all tangent vectors X, Y  T M and vertical vectors U, V  T K. These relations
generalize the usual Kaluza ansatz for gP . Choosing a set {ea} of independent vector
fields on K, the one-form on spacetime can be decomposed as a sum

A(X) = a Aa(X) ea ,                                                          (2.2)

where the real-valued coefficients Aa(X) are the traditional gauge fields on M4. For
general submersive metrics on P this can be an infinite sum, with {ea} being a basis of
the full space of vector fields on K, which is the Lie algebra of the diffeomorphism group
Diff(K). The gauge group need not act on K only through isometries of gK.

                             9
    The curvature FA is a two-form on M4 with values in the Lie algebra of vector fields
on K. It can be defined by

FA(X, Y ) := (dM Aa)(X, Y ) ea + Aa(X) Ab(Y ) [ea, eb] ,     (2.3)

where the last term is just the Lie bracket [A(X), A(Y )] of vector fields on K.

    The tangent space to P has a natural decomposition T P = T M  T K. Then T K is
the kernel of the projection T P  T M . It is also called the vertical sub-bundle V of T P .
Its gP -orthogonal complement, denoted H := (T K), is called the horizontal sub-bundle.
So we get a second, gP -dependent decomposition

TP = HV .                                                    (2.4)

Using these two decompositions, any tangent vector w  T P can be written as a sum
w = wM + wK = wH + wV in two different ways. The relation between them is

wV = wK - A(wM )      wH = wM + A(wM ) .                     (2.5)

So the information contained in the gauge one-form A on M is equivalent to the inform-
ation contained in the horizontal distribution H  T P . For example, the curvature FA is
the obstruction to the integrability of the distribution H [11].

    One can construct local, gP -orthonormal trivializations of T P using only horizontal
and vertical vectors. They can take the form {X�H, vj}. Here the vj form an orthonormal
basis of T K with respect to gK(x), for each x. The X� form a gM -orthonormal basis of
T M . The horizontal lift of X� to P is denoted X�H, and is given by

X�H = X� + Aa(X�) ea .                                       (2.6)

Such horizontal lifts are called basic vector fields on P .

2.2. Decomposing the covariant derivative of vector fields

As before, let  : P  M be a Riemannian submersion with a metric gP equivalent to
a triple (gM , A, gK), as in (2.1). Denote by , M and K the Levi-Civita connections
on P , on M , and on each fibre Kx. Let U , V and W be vertical vector fields on P and
let X, Y and Z be vector fields on the base M . Then we have the standard geometrical

                  10
identities [11, p. 240]:

                          [XH, Y H]V = FAa(X, Y ) ea                     (2.7a)
                                                                         (2.7b)
                          gP (XHY H, U )  =  1  FAa(X, Y ) gP (ea, U )   (2.7c)
                                             2                           (2.7d)
                                                                         (2.7e)
                          gP (XHY H, ZH) = gM (M X Y, Z)

                          gP (U V, XH)    =  -  1  (dAgK  )X  (U,  V  )
                                                2

                          gP (U V, W ) = gK(UKV, W )

These are identities of vector fields and functions on P . Functions defined on M , namely
FAa(X, Y ) and gM (XM Y, Z), are regarded as functions on P that are constant along the
fibres. The derivative dAgK can be identified with the second fundamental form of the
fibres of P . It measures how gK changes along M4 up to diffeomorphisms of K. It is
equivariant under Diff(K)-gauge transformations. As in [10], it can be expressed in terms
of Lie derivatives and the gauge one-forms Aa as

(dAgK)X (U, V ) = (LX gK)(U, V ) + Aa(X) (Lea gK)(U, V ) .               (2.8)

Here Lea gK denotes the Lie derivative along the internal vector field ea.

Remark on notation. The notation used in this paper differs from the notation in the
literature on Riemannian submersions. The modification is necessary to avoid a conflict
with the traditional notation in physics. Namely, the tensor A in [11, 45, 48] is essentially
what we call FA here, since it represents the physical gauge field strength. The tensor T
in [11, 45, 48] is called here dAgK. This avoids confusion with torsion and emphasizes its
physical role as the covariant derivative of Higgs-like fields. The precise relation is

(dAgK)X (U, V ) = (LXHgP )(U, V ) = - 2 gP (TU V, XH) = - 2 gP (U V, XH) . (2.9)

The last equality is the definition of T in [11, 45, 48]. The first two equalities are derived
in sections 2.3 and 2.5 of [10].

2.3. Spinors on M4 � K

2.3.1. Gamma matrices and chirality operators

Let k denote the dimension of the internal space K. The higher-dimensional spinor space
3+k,1 can be written as the tensor product 3,1  k. These spaces have irreducible
representations of Clifford algebras. There is a standard isomorphism between Cl(3+k, 1)

                                                       11
and the Z2-graded tensor product of algebras Cl(3, 1) ^ Cl(k). It is determined by the
correspondence of generators

                       1=11            for � = 0, 1, 2, 3                             (2.10)
                     � = �  1          for j = 1, ..., k
                   3+j = 5  j

This is a recipe to construct higher-dimensional gamma matrices l from the lower-
dimensional ones. The j are gamma matrices acting on k, and the � are 4D gamma
matrices for the metric  = diag(-1, 1, 1, 1). The convention used here is that gamma
matrices in spatial dimensions are square roots of -1 and are anti-self-adjoint with respect
to the positive-definite inner-product of spinors ,  = . This is the most common
convention in Riemannian geometry [55�57]. So for example

{�, } = -2 � I4                        (0) = 0      (l) = -l ,                        (2.11)

for l = 1, 2, 3. On a Lorentzian space, one can define an indefinite inner-product of spinors
with respect to which all gamma matrices are self-adjoint operators. This is

                         , 0 := 0 ,  .                                                (2.12)

The complex chirality operators on the spinor spaces 3C,1, kC and C3+k,1 are defined by

5 := i 0 1 2 3                                  K   :=     i[  k+1  ]  1  �  �  �  k
                                                                 2

P  :=  i[  k+3  ]  0  1  � � � k+3  =  (5)k+1  K ,                                    (2.13)
             2

where [s] denotes the integral part of s. The choices of i-factors are very standard for 5
in the Minkowski case and for K in the Riemannian case. Using the Clifford relations,
such as (2.11), one can check that these operators square as

       5 5 = 1           K K = 1                    P P = 1                           (2.14)

on the respective spinor spaces. The three operators are self-adjoint with respect to the
positive inner-product � , � of spinors. Moreover, 5 is anti-self-adjoint with respect to
the �, �0 pairing while P satisfies

                    , P  0 = (-1)k+1  P ,  0 .                                        (2.15)

2.3.2. Horizontal and vertical spinors

If E is an oriented, real vector bundle with a spin structure, its complexified spinor
bundle is denoted by SC(E). For a tangent bundle, the notation is simplified, as in

                                                       12
SC(T P ) = SC(P ). Now assume that K has a spin structure. Together with the trivial
spin structure on M4, it determines a unique spin structure on P = M4 � K. We fix those
structures for the rest of the paper.

    The horizontal and vertical bundles in decomposition (2.4) have their own associ-
ated spinor bundles, denoted SC(H) and SC(V ). Sections of SC(H) are called horizontal
spinors, while sections of SC(V ) are the vertical spinors. Calling  the projection from
P to M4, there is a natural isomorphism H  (T M ) as Lorentzian vector bundles over
P . So the respective spinor bundles are isomorphic too,

SC(H)  SC((T M ))  [SC(M )] .  (2.16)

In particular, a spinor  on M4 has a unique lift as a horizontal spinor that coincides with
the pull-back  under that isomorphism. This is denoted H and called the basic lift of
 to P . At the same time, if we fix a point x  M4 and consider the fibre Kx := {x} � K
inside P with its metric gK(x), there is a natural isomorphism between the restriction of
SC(V ) to Kx and the spinor bundle of the fibre,

SC(V ) |Kx  SC(Kx) .           (2.17)

Now let X be a vector field on M4 and let XH denote its basic lift to P , as in (2.6). Then
Clifford multiplication in SC(M ) and SC(H) satisfies the equivariance property

(X � )H = XH � H               (2.18)

for any spinor  on M4. Moreover, a dissection of these constructions, as done in [51],
shows that there is a natural isomorphism of spinor bundles

SC(P )  SC(H)  SC(V )          (2.19)

that is compatible with the Clifford multiplication implied by (2.10), in the sense that

  U � (H  ) = (5 � )H  (U � )  (2.20)
XH � (H  ) = (X � )H   .

Here U is any vertical vector field on P . It is regarded as such on the left-hand side and
as a section of V on the right-hand side. As before, X is any vector in T M .

    Since M4 is contractible, its spinor bundle SC(M ) is trivial. Due to (2.16), so is SC(H)
as a bundle over P . This implies that a spinor  on P can always be written as a sum

                        4      (2.21)

(x, y) = bH(x)  b(x, y) ,

                      b=1

13
where b is a Dirac spinor on M4 and b is a vertical spinor on P . Here x and y denote
coordinates on M4 and K, respectively.

    Regarding Dirac operators, let {X�} denote a gM -orthonormal trivialization of T M
and let {vj} denote a local, gK-orthonormal trivialization of the vertical bundle V  P .
Using the Levi-Civita connections of gM and gK, one can define the Dirac operators

    D/ M  = i gM� X� � M X         D/ K  = gMij vi � Kvj  .                  (2.22)

The first acts on spinors on M4; the second acts on vertical spinors over P . With the
conventions (2.11), the first is self-adjoint with respect to the L2-pairing 0, L2 of
spinors on M4. The second is self-adjoint with respect to the product , L2 of vertical
spinors, where the integration is taken over K only.

    When K is compact, the vertical spinors over a fibre {x} � K can always be written
as a (possibly infinite) sum of eigenspinors of the internal Dirac operator D/ K. Since the
metric gK depends on x, the operator D/ K and its eigenspinors will also change along M4,
in general. Now suppose that the internal metric gK(x) is independent of x. Then an
L2-orthonormal basis of eigenspinors {(y)} on K applies transversally throughout M4.
In particular, we can take each b in (2.21) and expand its y-dependence as b(x, y) =

   cb (x) (y). Inserting this in (2.21), it is clear that the higher-dimensional spinor can
then be written as a (possibly infinite) sum

                (x, y) =  H(x)  (y) .                                        (2.23)

Here the  are Dirac spinors on M4, the H are their horizontal lifts to P , and the 
are eigenspinors of D/ K independent of the point on M4.

3. Higher-dimensional Dirac operator

3.1. Decomposing the covariant derivative of spinors

The Levi-Civita connection on the tangent bundle T P can be lifted to a connection on
the spinor bundle. Denoting both connections by , the standard local formula is [57]:

X   :=  X ~  +  1  gPir  gPjs  gP (X ui, uj) ur  �  us  �  ~                 (3.1)
                4

    = X~ +      1  gPir  gPjs  gP (X ui, uj) - gP (X uj, ui)  ur � us � ~ .
                8

Here {ur} denotes a local, oriented, gP -orthonormal trivialization of T P , while ~ rep-
resents the spinor  in the induced trivialization of SC(P ). So ~ is a local function on

                               14
P with values in some Cr and we denote by X~ = (d~ )(X) its directional derivative.
We are also using the fact that gP (Xui, uj) is anti-symmetric in the two indices, for
the Levi-Civita connection. Since the metric is Lorentzian, the elements gPrs can be �1.
Below, we will most often abuse notation and simply write  instead of ~ .

    On a Lorentzian manifold, the lifted Levi-Civita connection is compatible with the
�, �0 inner-product of spinors defined in (2.12), in the sense that

             LX , 0 = X  , 0 +  , X 0                                                        (3.2)

for any vector field X. On a Riemannian manifold, the lifted Levi-Civita connection is
compatible with the positive-definite inner-product �, �.

    As described in section 2, for a Riemannian submersion gP  (gM , A, gK), we can take
the orthonormal trivialization of T P to be of the form {X�H, vj}, so a collection of basic
and vertical vector fields on P . In this adapted trivialization, the covariant derivatives
are given by the following formulae, proved in appendix B.

Proposition 3.1. Consider a spinor on P of the form  = H(x)  (x, y), as in (2.21).
Its covariant derivative along a vertical vector field U is given by

U   = H  (U )               -  1  gM� gM (FAa)� gK (ea, U ) (X � X � )H  
                               8

       +  1    gM� gKij  (dAgK)X�(U, vi) (X � 5 � )H  (vj � )  .                             (3.3)
          4

Its covariant derivative along a horizontal, basic vector field Y H on P is given by

Y H = (M Y )H   + Aa(Y ) H  Lea                                                              (3.4)
                                                                                             .
    +  1  gM�  FAa(Y, X�)      (X � 5 � )H  (ea � )
       4

    + H        Y         +  1  gKir gKjs  gP ( [Y, vi], vj) - gP ( [Y, vj], vi)  vr � vs � 
                            8

Here Lea denotes the Kosmann-Lichnerowicz derivative of spinors on the fibres K.

    These expressions are more explicit and expanded versions of those given in [51] for
the case of simple submersions. Importantly, they reveal that the 4D gauge fields Aa
couple to spinors through the Kosmann-Lichnerowicz derivative Lea written in (4.1).

    These expressions are simpler in regions where the Higgs-like scalars are constant, i.e.
where the internal metric gK does not vary along M4. There, the orthonormal vector
fields {vj} on K can be taken to be independent of the coordinate x  M4. So [Y, vi] = 0,
since Y is a vector field on M4. If the vertical spinor is also taken to be independent of
x, as in (2.23), the last line of (3.4) vanishes entirely and we get:

                                          15
Corollary 3.2. In regions where the internal metric gK and the vertical spinor  are
independent of the coordinate x  M4, the previous expressions reduce to

       U   = H  (U )        -  1    gM� gM (FAa)� gK (ea, U ) (X � X � )H  
                               8

           +  1  gM�  gKij  Aa(X�)   (LeagK )(U, vi)  (X     � 5   � )H   (vj  � )  (3.5)
              4

Y H = (YM )H   + Aa(Y ) H  Lea

           +  1  gM�  FAa(Y, X�)    (X  �  5  �  )H   (ea    �  )  .                (3.6)
              4

Here LeagK denotes the Lie derivative of gK along the internal vector field ea. This term
comes from the simplification of dAgK in (3.3), using definition (2.8) and the fact that gK
is constant along the flow of X� in M4.

3.2. Decomposing the higher-dimensional Dirac operator

The decomposition of the spinor connection given in proposition 3.1 leads directly to a
decomposition of the Dirac operator on P . For a higher-dimensional spinor of the form
H  , this is described in the next result, proved in appendix B.

Proposition 3.3. Consider a spinor on P of the form  = H(x)  (x, y), as in (2.21).
The action of the higher-dimensional Dirac operator on  can be locally decomposed as

D/ P   = gM� (X� � M  )H       +     gM� Aa (X� � )H                    1
                                                                Lea + 2 div(ea) 

       +   (5 � )H  D/ K    +     1  (FAa)� (X� � X � 5 � )H  (ea � )               (3.7)
                                  8

       + gM� (X� � )H               1      X log      |gK |     
                            X + 2

       + gM� (X� � )H       1        ij gP ([X, vi], vj) - gP ([X, vj], vi) vi � vj �  .
                            8

Here Lea denotes the derivative (4.1) of spinors on K; div(ea) denotes the divergence of
the internal vector field ea with respect to gK; and |gK| is the modulus of the determinant
of the matrix representing gK in a fixed coordinate system on K.

    This expression is a more explicit and expanded version of that given in [51]. The
detail is necessary to better understand the underlying physics. Formula (3.7) simplifies
in regions where the Higgs-like scalars are constant, i.e. where the internal metric gK does
not change along M4. In this case [X, vi] = 0, as before, and every higher-dimensional
spinor can be expressed as a sum of simpler tensor products of the form (x)H  (y), as
in (2.23). Thus, in this simpler setting, the Dirac operator acts as follows.

                                           16
Corollary 3.4. In regions where gK is constant along M4, the action of the Dirac operator
on a spinor of the form (x)H  (y) can be decomposed as

D/ P (H  )   =  gM� (X� � M  )H           +   gM�  Aa (X� � )H           1
                                                                 Lea + 2 div(ea) 

                +  (5 � )H  D/ K       +   1  (FAa)� (X� � X � 5 � )H  (ea � ) .     (3.8)
                                           8

    This expression is valid for a general gauge one-form A� = Aa� ea on M4 with values
in the space of vector fields on K, be they Killing or non-Killing with respect to gK. The
first term in (3.8) contains the Dirac operator in 4D. The second term determines the

couplings between gauge fields and fermions. The term with the internal Dirac operator

generates mass terms for fermions in 4D. The last term is a Pauli-type coupling between

the gauge field strength and spinors. It is a standard feature in Kaluza-Klein dimensional

reductions.

    Now suppose that a higher-dimensional spinor of the form (x, y) = H(x)  (y),
as in (2.23), satisfies the massless Dirac equation D/ P  = 0. The {} form an L2-

orthonormal basis of D/ K-eigenspinors on K. In particular, they are independent of each

other. Thus, writing m for the respective eigenvalue and using the traditional � nota-

tion, equation (3.8) implies that each  must satisfy the equation over M4:

� M X�, A       +  m 5 �       +   1  (FAa)�  , ea � L2   � 5                =   0.  (3.9)
                                   8

Here we are summing over the index  and the 4D covariant derivative is defined by

             M X�, A  := M X�  + Aa�                      1                          (3.10)
                                            , Lea + 2 div(ea)  L2  .

The reader may notice that (3.9) is similar to, but not identical to the 4D Dirac equation.

Besides the Pauli term, it has extra 5 factors and a non-standard kinetic term. However,

denoting

                          1
                      :=       (I  +  i5)      =   exp (i5/4)  ,                     (3.11)
                            2

as in [2, p. 22], it is easy to check that the redefined 4D spinors satisfy

i � M X�, A        +  m      +    1   (FAa)�  , ea  � L2  �       =          0.      (3.12)
                                  8

This is the traditional Dirac equation, with a Pauli term, written in Minkowski space with

signature - + ++ and the gamma matrix conventions described in 2.3.1.

Thus, the physical couplings of gauge fields to 4D fermions, as given by the covariant

derivative (3.10), are determined by the matrix elements of Lea in the basis {} of
eigenspinors of D/ K. These matrix elements are anti-hermitian. The identity

             1                                      1
          Lea + 2 div(ea)  ,        +      , Lea + 2 div(ea)  L2 = 0                 (3.13)

                                L2

follows from the general property (4.9) of the Kosmann-Lichnerowicz derivative.

                                           17
Remark 3.1. The appearance of a 4D Pauli term in the decomposition of the higher-
dimensional Dirac operator represents a variation from the prescriptions of the Standard
Model. In the case of the abelian 5D Kaluza-Klein model, this term induces a correction
to the electric dipole moment of the electron, as is well-known. It has been estimated that
the magnitude of the correction is negligible, beyond the reach of current experimental
measurements (e.g. [58]). However, those estimates rely on the assumption that the
higher-dimensional vacuum metric is entirely determined by the simple Einstein-Hilbert
action on P . That assumption should not hold in realistic Kaluza-Klein models. Higher-
order corrections to that action seem necessary for several reasons. For example, to
introduce the different mass scales observed in reality and, in certain versions of the
model, to stabilize the vacuum metric on P [10].

Remark 3.2. Consider the operator on spinors over P defined by the Pauli term,

C(H  )  :=  1  (FAa)� (X� � X � 5 � )H  (ea � ) .                               (3.14)
            8

It is algebraic and anti-self-adjoint with respect to the pairing �, �0 of spinors. Thus, the
modified operator D/ P - C retains most of the useful properties of D/ P , such as ellipticity,

anti-self-adjointness with respect to �, �0, and the implicit coupling of 4D gauge fields
to spinors through the Kosmann-Lichnerowicz derivative. So one could also consider
(D/ P - C) = 0 as a candidate for the physical equation of motion for spinors on P . An

important conceptual disadvantage of the modified operator, however, is that it is defined

only for submersive metrics of the form gP  (gM , A, gK), not for general metrics on P .

4. Properties of the Kosmann-Lichnerowicz derivative

4.1. General properties

This section collects several useful properties of the Kosmann-Lichnerowicz derivative of
spinors, denoted LX. This operator was introduced by Lichnerowicz for a Killing X in
[59]. Later, Kosmann extended it to any X and thoroughly investigated its properties [52].
Most results presented here can be found in the literature in the Riemannian case [52,53],
but are somewhat dispersed and are stated using various conventions. The simple formulae
in lemma 4.1 are necessary for sections 6 and 7 but do not seem to exists in the literature.
So their proofs are given here. All formulae written in the present section 4.1 remain valid
in the semi-Riemannian case.

    Let (K, g) be a semi-Riemannian manifold with a fixed spin structure and spinor
bundle SC(K)  K. Given a vector field X and a spinor  on K, the Kosmann-

               18
Lichnerowicz derivative is defined by

LX     :=  X      -   1 girgjs         g(vr X, vs) - g(vsX, vs)         vi � vj �              (4.1)
                      8

       =   X ~ +      1 girgjs         g([X, vr], vs) - g([X, vs], vr)  vi � vj � ~ .
                      8

Here  denotes both the Levi-Civita connection on T K and its standard lift (3.1) to the

spinor bundle. The dot denotes the Clifford action of vectors on spinors. The vectors

vj form a g-orthonormal, oriented, local trivialization of T K. The second line is a local
expression using the representative ~ of  with respect to the trivialization of SC(K)
induced by {vj}. It follows from definition (3.1) and a direct application of the Koszul
formula for . When X is Killing, the coefficients gK(vr X, vs) and gK([X, vr], vs) are
both anti-symmetric in r and s.

    The operator LX is C-linear and acts as a derivation when the spinor is multiplied by
a function in C(K),

       LX (1 + f 2) = LX 1 + f LX 2 + (LX f ) 2 .                                              (4.2)

Its commutation relation with the Clifford multiplication of vectors and spinors is

LX (Y  � )  -  Y  � LX   =             [X, Y ] �   +  1  gij  (LX g)(vi, Y  )  vj  �    .      (4.3)
                                                      2

Unlike the covariant derivative, it does not behave nicely when the vector field X is
multiplied by a scalar function:

                             1                                                                 (4.4)
LfX  = f LX + 8 (gradf ) � X - X � (gradf ) �  .

Using that the volume element is covariantly constant on K, one can derive that LX
always commutes with the chirality operator:

                      LX K  = K LX  .                                                          (4.5)

The commutator of LX with the covariant derivative  is encapsulated in

(LX )Y  := LX (Y ) - Y (LX ) - [X,Y ]                                                          (4.6)

       =    1 girgjs  [vr (LX g)](vs, Y )          -  [vs(LX g)](vr, Y )           vi � vj � 
            8

The operator LX is also called the derivative of the connection . The symbol LXg
denotes the Lie derivative of the metric g along X. It is again a section of T K  T K,
like the metric itself, and has a covariant derivative (LXg).

                                       19
The commutator of LX with the standard Dirac operator is given by

[D/ , LX]   =  1          girgjs (LX g)(vr, vs)  vi  � vj                               (4.7)
               2

               + 1 girgjs  [vr (LX g)](vi, vj)       -      [vj (LX g)](vi, vr)  vs � 
                  4

Just like the Levi-Civita connection (3.1), the Kosmann-Lichnerowicz derivative is com-

patible with the inner-product of spinors. This means that

               (LX 1, 2) + (1, LX 2) = LX (1, 2) ,                                      (4.8)

where LX denotes the standard Lie derivative of functions on K. Using Stokes' theorem,
this implies that for compactly supported spinors we have

    (LX 1, 2) + (1, LX 2) + div(X) (1, 2) volg = 0 ,                                    (4.9)

K

where div(X) denotes the divergence of X on (K, g). So LX is formally anti-self-adjoint

for a divergence-free X.

Remark 4.1. In formulae (4.8) and (4.9), the inner-product of spinors should be inter-
preted with care. If the metric g has a signature with r minus signs, then (�, �) denotes
the inner-product such that

                          (X � 1, 2) = (-1)r-1(1, X � 2)                                (4.10)

for any X  T K [60, p. 68]. Thus, it is the positive-definite pairing ,  =  in the
Riemannian case and the indefinite pairing , 0 = 0,  in the Lorentzian case
(see the conventions in section 2.3).

The Kosmann-Lichnerowicz derivative is not a proper Lie derivative of spinors, since

it does not satisfy the usual closure relation. In general we have

( [LX , LY ] - L[X,Y ] )   = 1 girgjsgkl             (LX g)(vr, vk) (LY g)(vs, vl)      (4.11)
                              4

                           - (LX g)(vs, vk) (LY g)(vr, vl) vi � vj �  .

However, the right-hand side does vanish when either X or Y are Killing or conformal
Killing vector fields on K. When this is not the case, the right-hand side only vanishes
to first order in the Lie derivatives of g.

Remark 4.2. Despite being a higher-order correction, the right-hand side of (4.11) rep-
resents a significant conceptual variation from current practice in the Standard Model and
grand unified theories [61,62]. It shows how there are natural equations of motion, in this
case the equation D/  = 0 of a Kaluza-Klein model, in which only the unbroken part of
the 4D gauge group couples to fermions through an exact Lie algebra representation. The
broken part does not, and understandably so. It does not preserve the internal vacuum
metric, and, since spinors are objects that depend on the metric, it does not induce a
standard symmetry transformation of spinors.

                                                 20
4.2. Kosmann-Lichnerowicz derivative on Riemann surfaces

This section derives two formulae for LX that will be needed in the examples in sections
6 and 7. Let K be a Riemann surface with metric g and compatible complex structure
J. As with general K�ahler manifolds [11, ch. 2], we have the compatibility relations

               g(JX, JY ) = g(X, Y )      volg(X, Y ) = g(JX, Y )
                 X(JY ) = J XY
                                                                   (4.12)

for any vector fields X and Y on K. Choosing isothermal coordinates on K [63, sec. 1.5],
the metric can be locally written as

                   g = 2(x, y) [ (dx)2 + (dy)2 ]                   (4.13)

for some positive function . The complex structure acts on the coordinate vector fields as
J(x) = y and J(y) = -x, so z = x + iy is a complex coordinate on K. Thus, the local
vector fields v1 = -1x and v2 = -1y form an oriented, g-orthornomal trivialization
of T K satisfying Jv1 = v2.

    Now fix a spin structure and spinor bundle SC(K). This is a rank-two complex vector
bundle over K. Definition (2.13) says that the chirality operator acts on spinors as

                   K  = i v1 � v2 �  .                             (4.14)

Then we have:

Lemma 4.1. The Kosmann-Lichnerowicz derivative of a spinor on a Riemann surface

can be written as                           i
                   LX = X - 4 div(JX) K 
                                                                   (4.15)

for any vector field X on K. In particular, when Xh is a Hamiltonian vector field de-

termined by a function h, we have

                                                              i    (4.16)
                                   LXh = Xh - 4 (h) K  ,
where h denotes the Laplacian of h.

Proof. Using the compatibility relations (4.12), the divergence of the vector field JX is

div(J X) = j g(vj J X, vj) = j g(J vj X, vj) = -                 j g(vj X, J vj)
            = g(v2X, v1) - g(v1X, v2) .                                             (4.17)

                                      21
Then (4.15) follows by combining (4.17), (4.14) and the definition (4.1) of LX. Now let
h be a real, smooth function on K and let Xh denote its Hamiltonian vector field [66]. It
is a divergence-free vector field determined by the equality of 1-forms

                                            dh = Xhvolg .                                              (4.18)
                                                                                                       (4.19)
It follows from (4.12) that

                                            JXh = grad h

as vector fields on K. So div(JXh) = h and (4.16) follows from (4.15).

    Hamiltonian vector fields always have vanishing divergence. When K = S2, every
divergence-free vector field is Hamiltonian for an appropriately chosen function h. This
holds because the first de Rham cohomology group of S2 vanishes.

5. Chiral fermions

5.1. Correlation between internal and 4D chiralities

This section starts by reviewing well-known observations about the correlation between
internal and 4D chiralities (e.g. [14]) in our setting of general Riemannian submersions.
This is a mechanism to explain how the chirality of interactions between 4D fermions and
gauge fields can be caused, in principle, by an asymmetry of the action of the Kosmann-
Lichnerowicz derivative LX on left- and right-handed internal spinors. Section 5.2 then
studies the chiral properties of LX in more detail. It defines the concepts of chiral
isomorphism and strong and weak chiral symmetries.

     In this section, we assume that K is a compact, connected, even-dimensional, spin

manifold with a fixed topological spin structure. For any metric gK, the chirality operator

satisfies KK = 1. It has eigenvalues �1 and its eigenspaces determine a decomposition

of  the  complex   spinor  bundle   as  a  sum  of   half-spinor   bundles,  SC (K )  =  S + (K )    S - (K ).
                                                                                           C           C

Since this is true for any metric, the isomorphisms (2.17) on the fibres determine a splitting

of the vertical bundle on P as a sum SC+(V )  SC-(V ). Similarly, the decomposition

SC(M4) = SC+(M4)SC-(M4) on the base together with the isomorphism (2.16) determines

a   splitting  of  the  horizontal  bundle  as  S+(H)  S-(H).         Using  the  formula  P  =    5  K,
                                                  C         C

which comes from (2.13) for an even-dimensional K, it is clear that these decompositions

are  related   to  the  higher-dimensional      splitting  SC(P )  =  S+(P )      S-(P )  simply   by
                                                                        C           C

                        S+(P )      S+(H)         SC+(V  )     S-(H)    SC-(V     )                    (5.1)
                          C           C                          C

                        S-(P )      S+(H)         SC-(V  )     S-(H)    SC+(V     )   .
                          C           C                          C

                                                     22
Sections of S�(P ) are the Weyl spinors on P . Now suppose that the higher-dimensional
                         C

physical spinors are taken to be sections of SC+(P ), say, instead on sections of SC(P ). In

other words, suppose that physical spinors are taken to satisfy the right-handed Weyl

equation:

                                   D/ P  = 0                P  =  .                                   (5.2)

Then it follows from (5.1) that the solutions will be sums of spinors of the form

                      (x, y) = +(x)  +(x, y) + -(x)  -(x, y) .                                        (5.3)

So the right-handed 4D fermions are coupled only to right-handed internal spinors, and

similarly for their left-handed counterparts. The higher-dimensional Weyl equation im-

poses a correlation between 4D and internal chiralities. Now suppose that a 4D gauge

field is linked to a vector field X on K and the derivative LX acts differently on the

spaces  of  sections  of  SC+(V )  and  S-   (V  ).  Then,  it  follows  from  (3.10)  that  the  4D  chiral
                                          C

components � will have different couplings to that gauge field. So the emergence of

chiral fermions in 4D could be due to an asymmetry of the action of LX on the chiral
components � of vertical spinors.

    Given the isomorphisms (2.17), our task is therefore to study the symmetries of LX
when acting on the spaces of sections of SC�(K), denoted V �. That is the aim of section
5.2. For now, let us introduce notation and recall standard facts that will be necessary

there. For a compact K, the Dirac operator D/ gK is elliptic and self-adjoint with respect
to the L2-inner-product of complex spinors

                                    ,  L2 :=  ,   volgK .                                             (5.4)
                                                                  K

Here  ,   denotes the positive-definite, hermitian pairing that is i-linear in the second
entry and i-antilinear in the first one. The Dirac operator has finite-dimensional eigen-
spaces, denoted Vm, with eigenvalues m that are real, discrete and accumulate only at
infinity. The space of L2-integrable spinors then decomposes as an orthogonal Hilbert
direct sum of the different Vm.

    For a compact K, the isometry group of gK is a compact Lie group, and we denote by
G its connected component. We always assume that the G-action on K can be lifted to

an action on the spin structure. When G is non-trivial, the index of the Dirac operator
vanishes for a connected, even-dimensional K [17]. This means that the kernel of D/ gK
splits into a sum of two K-eigenspaces of equal dimension, V0 = V0+  V0-. When
G is trivial, the index of D/ gK can still vanish. This will happen when K admits any
metric with positive scalar curvature, for example. When gK itself has this property, the
Schro�dinger-Lichnerowicz formula guarantees that the kernel of D/ gK is trivial.

                                                     23
5.2. Internal chiral symmetries

Assume that K is a compact, connected, even-dimensional, spin manifold with a fixed
metric gK and spin structure. Its spinor bundle decomposes as a direct sum of half-spinor
bundles, S�(K), whose space of sections are denoted V �. The Kosmann-Lichnerowicz

                    C

derivative LX always commutes with the chirality operator K. So it preserves the
spaces V �. We want to study whether LX acts similarly on V + and V -. When this
happens, we say that LX has chiral symmetry. This notion should imply an identity of
matrix elements +, LX+ = -, LX- for all D/ -eigenspinors  and  with positive
eigenvalues. In fact, we will distinguish two notions of chiral symmetry: when that identity
holds exactly (strong symmetry), and when it holds only up to a unitary redefinition of
the D/ -eigenspinors (weak symmetry). In the latter case, the redefinitions must respect
the symmetries of spinors induced by the isometry group of gK.

    Any spinor on K can be written as a sum of its chiral components  = + + -, as in
(1.5). Let Vm denote the eigenspace of D/ with real eigenvalue m. Since K anti-commutes
with D/ , it preserves V0 and takes Vm isomorphically to V-m when m = 0. In particular,
it preserves the sums Vm  V-m for all m > 0. These are eigenspaces of D/ 2. Since K
squares to the identity, each of these invariant spaces can be further decomposed into
eigenspaces of K with eigenvalues �1. We write

         V0 = V0+  V0-                            (5.5)
Vm  V-m = Vm+  Vm- ,
                                      m>0.

Let G denote the connected component of the isometry group of gK. Its action on spinors
preserves the eigenspaces Vm�. This follows because LY commutes with K and D/ when
Y is Killing. Thus, for a non-trivial G, we can further decompose each Vm� as a sum
of irreducible representation G-spaces. The summands are labelled by the respective D/ -

eigenvalue m, the representation  and a non-negative integer nm, accounting for the
representation multiplicity. So we write4

V� =      Vm� =                       nm, Vm�, .  (5.6)

      m0                         m0 

The integers nm, are the same for both decompositions �. This is because, for all m > 0,
there is a natural, unitary, G-equivariant isomorphism

Im : Vm+ - Vm-                    - m-1D/  .      (5.7)

4For the trivial representation, Vm�, is unidimensional and nm, is the dimension of the subspace of Vm�
 where G acts trivially.

                                                         24
Each Im is just a scalar multiple of the Dirac operator inside Vm+. Its G-equivariance
follows from the fact that D/ commutes with the G-action on spinors. Since D/ anti-

commutes with K, the definitions (1.5) of chiral projections imply that

Im(+) = -                                (5.8)

for all  in the D/ -eigenspaces Vm with eigenvalue m > 0. In the case m = 0, the map
Im is not well defined. So the difference n0+, - n0-, could be non-zero. This difference is
called the -index of D/ . However, a result of Atiyah and Hirzebruch guarantees that it

does vanish for a compact K with non-trivial G. Thus, in this case, even for m = 0, the
subspaces V0+ and V0- have the same decomposition into irreducible G-spaces [14, 17].

Definition 5.1. A chirality isomorphism is an invertible, unitary, G-equivariant, linear
map  : V +  V - that commutes with D/ 2.

    Such isomorphisms exist if and only if the index of D/ vanishes. If V0+ and V0- do
not have the same dimension, such invertible maps cannot be constructed. In the other
direction, if V0+ and V0- have the same dimension, there exists a non-canonical unitary
isomorphism 0 between them. If G is non-trivial, the aforementioned result of Atiyah
and Hirzebruch guarantees that 0 can be chosen to be G-equivariant. Then a full
isomorphism  can be defined by making it coincide with the map Im of (5.7) over Vm+,
for each m > 0, and coinciding with 0 over V0+.

    Now let X be a vector field on K and let LX� denote the restriction of the Kosmann-
Lichnerowicz derivative to the spaces V � of Weyl spinors. We define:

Definition 5.2. The derivative LX is said to have weak chiral symmetry if there exists
a chirality isomorphism  such that -1LX-  = LX+ as operators on V +.

Since chirality isomorphisms are unitary, this is the same as saying that

 , LX  L2 =   , LX   L2                  (5.9)

for all spinors  and  in V +. The particular  that fulfils this condition may depend on
X, of course. If it can be chosen to coincide with the map Im for all indices m > 0 while
preserving property (5.9), we will say that LX has strong chiral symmetry. In this case,
for any  in Vm and  in Vm with m, m > 0, it follows from (5.8) and (5.9) that

+, LX +L2 = Im+, LX Im+L2 = -, LX -L2 .  (5.10)

In contrast, for spinors in V0 the natural map Im of (5.7) is not defined. So in that subspace
we must keep using the non-canonical isomorphism . In the definition of strong chiral

25
symmetry we also demand that LX preserves V0. In general, the Kosmann-Lichnerowicz
derivative LX preserves the eigenspaces V � of K, but a priori need not preserve the
smaller subspaces Vm� and Vm�, when X is not Killing.

Definition 5.3. The derivative LX is said to have strong chiral symmetry if

1. +, LX +L2 = -, LX -L2 for all spinors  and  in Vm>0;
2. It preserves the kernel of D/ ;

   3. There exists a unitary, G-equivariant, linear map 0 : V0+  V0- such that
       , LX L2 = 0 , LX 0 L2 for all spinors  and  in V0+.

Remark 5.1. It is clear that a derivative LX satisfying the conditions of strong chiral
symmetry will also satisfy those of weak symmetry. Keeping identities (5.10) in mind, the
map  of definition 5.2 can be constructed to coincide with Im over each Vm+ with m > 0
and coinciding with the map 0 of definition 5.3 over V0+.

    The traditional no-go arguments against the existence of chiral fermions in Kaluza-
Klein models essentially amount to the statement that, when X is Killing with respect
to gK, the derivative LX has strong chiral symmetry. This is the content of proposition
1.1. This symmetry, together with the correlation of internal and 4D chiralities, forces
left- and right-handed 4D fermions to have the same couplings to massless gauge fields.

    The main message of the present paper, in contrast, is that the symmetries observed
in the Killing case are not generic. They will not hold for most non-Killing vector fields
on K, even if they are small perturbations of Killing fields. The explicit calculations in
section 7 show that, for a generic Hamiltonian vector field on K = S2, the derivative LX
does not have strong chiral symmetry. This is the content of proposition 1.2.

    The calculations in section 6 go further. They consider the case where Xh is a Hamilto-
nian vector field on the torus K = T 2 equipped with its trivial spin structure. They show
that, for a generic Xh, the derivative LXh does not have strong nor weak chiral symmet-
ries. This is the content of proposition 1.3. The absence of chiral symmetries should hold
much more generally, beyond the explicit examples illustrated in this paper.

    We end this section with a result that helps understand points 1 and 2 in the definition
of strong chiral symmetry. Consider the following L2-orthogonal decompositions of the
space of sections of SC(K):

V = Vm>0  V0  Vm<0 = Vm+>0  Vm->0  V0+  V0- .                                (5.11)

Here we have defined Vm�>0 := m>0 Vm� and the second equality uses decompositions
(5.5). Then we have the following result, proved in appendix C:

26
Proposition 5.1. Let X be a divergence-free vector field on a compact, even-dimensional,
spin manifold (K, gK). The following conditions are equivalent:

   1. LX preserves the subspace of spinors Vm>0;
   2. LX preserves all the subspaces appearing in decompositions (5.11);
   3. the commutator [LX, D/ ] preserves the subspace Vm>0;
   4. +, LX +L2 = -, LX -L2 for all  in Vm>0 and all  in Vm0.

Moreover, points 1 and 2 in the definition of strong chiral symmetry can be replaced by
any one of these conditions.

6. Explicit example: K = T 2

This section describes the simplest explicit example of the ideas discussed so far. It
considers the case where K is the two-torus T 2 = R2/Z2 equipped with its flat metric of
total volume 1 and trivial spin structure. The basic facts about spinors on flat tori are
very well-known, even for the non-trivial spin structures. See, for example, references [54]
and [55, ch. 2.1]. After introducing the notation and the basic facts, the main results are
presented in formulae (6.5), (6.7) and in proposition 6.2.

    The spinor bundle SC(T 2) determined by the trivial spin structure is a trivial, rank
two complex vector bundle over T 2. Consider the family of sections characterized by the

integers (l1, l2)  Z2,


                        l1, l2   =  12  e2i(l1 x1+l2 x2)       1        (6.1)
                                                                  .
                                                               cl1, l2

Here (x1, x2) are the periodic Euclidean coordinates on T 2 with the constant cl1, l2 defined
as 1 if l1 = l2 = 0 and as the phase (l1 - i l2) / |l1 - i l2| otherwise. These spinors and their

counterparts K l, n are all eigenspinors of the Dirac operator,

D/ l1, l2 = 2  l12 + l22 l1, l2         D/ (K l1, l2) = - 2  l12 + l22 K l1, l2 . (6.2)

These are all the eigenspinors of the Dirac operator, up to linear combinations. So the
l1, l2 and K l1, l2 form a basis of the space of smooth spinors on T 2. This basis is
orthonormal with respect to the L2-inner-product (5.4).

    Now denote by xj the Killing vector field on T 2 generated by the coordinate xj.
Any vector field on T 2 can be decomposed as X = X1x1 + X2x2. The Levi-Civita
connection of the flat metric on T 2 is trivial, in the sense that its Christoffel symbols

                                        27
xj xi vanish. So it follows from (4.15) and the definition of l1, l2 that the Kosmann-
Lichnerowicz derivatives are given by

                   LX l1, l2      =    2i (X1l1 + X2l2) l1, l2     -   i                                        (6.3)
                                                                       4 div(J X) K l1, l2 .

For the flat metric and natural complex structure on T 2 = R2/Z2, the divergence factor
is simply div(JX) = x2X1 - x1X2. In particular,

                                            Lxj (l1, l2 ) = 2 i lj l1, l2 .                                     (6.4)

Returning to the Kaluza-Klein model on M4 � T 2, this means that the integer lj will be
interpreted in four dimensions as the xj -charge of the 4D fermion  appearing in the
tensor product   l1, l2. In other words, it represents the charge of  when responding
to the massless gauge field on M4 linked to the internal Killing field xj .

    Now decompose the D/ -eigenspinors as sums of their chiral components, l1, l2 = l+1, l2 +
l-1, l2. Formula (6.3) implies that

                   LX        �         =  2i (X1l1 + X2l2) l�1, l2       i  div(J  X)  l�1,  l2  .              (6.5)
                               l1, l2                                    4

So LX preserves the subspaces of spinors V �, as it should. It is also clear that LX will
act differently on V + and V - when div(JX) is not zero. Thus, in general, LX does not

have strong chiral symmetry. However, the Killing fields xj do have vanishing divergence
on T 2. So the Lxj and their linear combinations have strong symmetry, as expected.

       To investigate the possible existence of weak chiral symmetry, start by observing that,

in our torus setting, all the spaces Vm�, in decompositions (5.6) are one-dimensional and

have multiplicity nm, = 1. In particular, the restrictions of unitary chirality isomorphisms

    :  V+          V-        can  differ  only  by  complex   phases.  Thus,  according      to     definition  (5.9)
         l1, l2      l1, l2

of  weak  chiral   symmetry,           the  question  is  whether  we  can  redefine  the    Weyl   spinors     -
                                                                                                                  l1, l2

through those phases in order to obtain a perfect match

                             l+1, l2 , LXh n+1, n2 L2 =? l-1, l2 , LXh n-1, n2 L2                               (6.6)

for all integers lj and nj.

    Consider the simpler case where Xh is a Hamiltonian vector field determined by a
function h on the torus. Its components are Xh1 = x2h and Xh2 = -x1h. Then a
straightforward computation using Stokes' theorem yields:

Proposition 6.1. For a Hamiltonian vector field Xh on T 2 and any integers lj and nj,

                   l+1, l2 , LXh n+1, n2 L2 = i r h l1,l2,n1,n2 (l1-n1,l2-n2)                                   (6.7)
                   l-1, l2 , LXh n-1, n2 L2 = - i cl1,l2 cn1,n2 rl1,l2,n1,n2 h(l1-n1,l2-n2) .

                                                          28
    Here we have denoted the Fourier coefficients of a function on T 2 as

                                 h(l1,l2) :=        h       e-2i(l1 x1+l2 x2) volgK  .                          (6.8)

                                                 T2

The complex phases cl1,l2 are as in (6.1) and we have defined the complex numbers

                   rl1,l2,n1,n2  :=    1 2    (l1 - n1)2 + (l2 - n2)2 + 4i (l1n2 - l2n1)               .        (6.9)
                                       2

The matrix elements (6.7) vanish when lj = nj. Since the cl1,l2 are phases, it is clear that

the � matrix elements of LXh always have the same absolute value for a Hamiltonian Xh.

Nonetheless,       it  is  not  possible  to  redefine  the  Weyl    spinors    -         through      complex  phases
                                                                                  l1, l2

to obtain the match (6.6). To recognize this, write

          l+1, l2 , LXh n+1, n2 L2        =   al1,l2,n1,n2   cl1,l2  l-1, l2 ,  LXh  cn1,n2  -         L2       (6.10)
                                                                                               n1, n2

with coefficients                         a = - rr . l1,l2,n1,n2

                                                             l1,l2,n1,n2                                        (6.11)
                                                             l1,l2,n1,n2

defined when (l1, l2) = (n1, n2). Although these coefficients are complex phases, they
are not separable and cannot be written as a product al1,l2,n1,n2 =? al1,l2 an1,n2 for a fixed

function al,n on Z2 with values in U (1). This is because they do not satisfy the identity

                                 a a = a a ?                                                                    (6.12)
                                   l1,l2,n1,n2 l1 ,l2 ,n1 ,n2
                                                             l1,l2,n1,n2 l1 ,l2 ,n1,n2

for all values of the integer labels, as can be easily checked. Thus, the desired redefinition

of  the  -         is  not  possible,  and   we  conclude    that:
           l1, l2

Proposition 6.2. Let Xh be a generic Hamiltonian vector field on the torus K = T 2
equipped with its trivial spin structure. Then the Kosmann-Lichnerowicz derivative LXh
does not have strong or weak chiral symmetries.

    Returning to the Kaluza-Klein model on M4 � T 2, this means that, generically, the
massive 4D gauge field linked to Xh has unavoidable chiral interactions with the 4D
fermion  appearing in the tensor product   n1, n2 for (n1, n2) = (0, 0). This is the 4D
fermion with abelian charges (n1, n2). The amount of chirality depends on Xh through
the Fourier components of the function h on the torus.

7. Explicit example: K = S2

7.1. Spinors on S2
This section provides a second explicit example of chiral interactions. For the vacuum
internal space we take the two-sphere S2  CP1 equipped with its round metric of radius

                                                       29
1, positive curvature and total volume 4. Part 7.1 reviews standard facts about spinors
on S2. See references [64] and [65, ch. 9.A], for example. After the notation and basic facts
are set, section 7.2 presents the calculations showing the emergence of chiral fermions.

    Spheres have unique spin structures and spinor bundles. The complexified spinor
bundle SC(S2) is a trivial, rank-two complex vector bundle. It can be written as a direct
sum of two non-trivial complex line bundles,

                                         SC(S2)     =   S+    S- .                                                  (7.1)
                                                          C          C

Then S+ coincides with the hyperplane line bundle and S- with its dual, the tautological
     C                                                                   C

bundle. The holomorphic tangent and cotangent bundles of S2 can be written in terms

of these two line bundles as T S2  S+  S+ and T S2  S-  S-.
                                               C    C                       C              C

    The infinite-dimensional space of L2-integrable sections of S� has a standard orthonor-
                                                                                  C
                                                                   1
mal  basis,  the  spin-weighted    spherical      harmonics  Y�    2    [71, 72].       We denote them simply

                                                             l, n

by  Yl�, n.  The  index  l  runs  through  the    positive  half-integers      {  1  ,  3  ,  .  .  .}.  For  each  value  of
                                                                                  2     2

l, the index n runs through {-l, -l + 1, . . . , l}. Note that the Yl�, n are not scalar functions

on S2; they are sections of non-trivial bundles. So their value at a point depends on the

coordinates being used.

    These spherical harmonics can be used to define sections of the spinor bundle. Using

decomposition (7.1), define

                                         l, n   :=   1       Yl+, n   .                                             (7.2)


                                                       2 i Yl-, n

These spinors and their counterparts Kl, n are all eigenspinors of the Dirac operator,

             D/ l, n =      1                          D/ K l, n                                 1                  (7.3)
                            l+     l, n                                  =-          l+             K l, n .
                                2                                                        2

Let (, ) be the usual spherical coordinates on S2 and denote by  the Killing vector field
generated by the azimuthal angle. One can directly calculate the Kosmann-Lichnerowicz
derivatives

                  L (l, n) = i n l, n                   L (K l, n) = i n K l, n .                                   (7.4)

So the spinors l, n over S2 are entirely characterized by their eigenvalues with respect
to the commuting operators D/ and L. For a Kaluza-Klein model on M4 � S2, the
eigenvalues of these internal operators determine the mass and the -charge of a 4D
fermion  appearing in the higher-dimensional spinor   l, n.

    Since the spin-weighted spherical harmonics form a basis of the space of sections of S�,
                                                                                                                                                                        C

it follows from (7.1) that the l, n and Kl, n form a basis of the space of L2-integrable
spinors on S2. This basis is orthonormal with respect to the inner-product (5.4). On

                                                    30
the sphere, the eigenspinors of D/ with the smallest eigenvalues �1 are actually Killing
spinors. For any vector field X on S2, they satisfy

  X                   =      -     1     X  �  1                            X        K                       =  1  X  �  K    1                .        (7.5)
                                                   2                                                                              2
       1  ,  �  1                  2                  ,  �     1                              1  ,  �  1        2                    ,  �  1
       2        2                                              2                              2        2                                   2

    Identifying the punctured sphere S2 \ {N } with the complex plane through stereo-
graphic projection, the normalized Killing spinors can be written in coordinates as


                      (z,    z�)      =        11                                                (z  ,  z�)  =     1 z�                    ,            (7.6)
                                            2                                                                      2
             1  ,  1                                                                 1  ,  -  1                                    
             2     2                                                                 2        2
                                                         q        i  z                                                   q     -  i

where we have defined the function q := 1 + |z|2.

7.2. Chiral fermions with K = S2

The aim of this section is to state and prove proposition 7.2. It illustrates the emergence

of chiral interactions of spinors on S2.                                    Start  by      considering          the   Killing        spinors            1      ,  �  1
                                                                                                                                                            2        2

written in (7.6). Let Xh be any Hamiltonian vector field on S2, defined as in (4.18). The

following auxiliary result is proved in appendix C.

Lemma  7.1.        For   any          complex            function       f   on  the  sphere,            the  derivatives    LXh         1      ,  �  1  satisfy
                                                                                                                                            2        2

the identities

       K           f  1      ,  �  1  ,  L  Xh           1  ,  �  1   volg           i          ( f�         �  2i Lf�) h      volg                     (7.7)
                          2        2                     2        2         =-
S2                                                                                            S2
                                                                                   16

                                                                                     1                       f�, Y10, 1 h volg .
       K           f  1               ,  L  Xh                        volg  =   �
                          2  ,  �  1                     1  ,     1                2 6              S2
S2                                 2                     2        2

    Here Lf� is the Lie derivative of the scalar function along the vector field  on S2.
The Poisson bracket of real functions [66, sec. 18.3] is defined by

                                               { h1, h2 } := volg(Xh1, Xh2) .                                                                           (7.8)

It is extended to complex functions by i-linearity on both entries. The scalar spherical
harmonics Y10, �1 are given by

                      Y10, -1 =                3 z�                                3 (sin ) e-i                 =  - Y10, 1 ,                           (7.9)
                                                              =                    8

                                               2 1 + |z|2

using both spherical and complex coordinates on the sphere.

    We want to calculate the right-hand side of (7.7) when f is a general spherical harmonic
Yl0, n. These are eigenfunctions of the Laplacian and of the Lie derivative along ,

                                                                  Yl0, n = - l (l + 1) Yl0, n                                                           (7.10)

                                                         L (Yl0, n) = i n Yl0, n .

                                                                            31
See, for example, formulae (9.99), (9.102) and (9.104) in [67]. Moreover, since the Yl0, n
form an orthonormal basis of the space of L2-integrable complex functions on S2, the
Poisson bracket of two spherical harmonics can itself be written as a linear combination
of spherical harmonics. For our purposes, we only need the formula

                           {Yl0, n , Y10, �1} =  i                                    3           (l  n) (l � n + 1) Yl0, n�1 .                                               (7.11)
                                                                                      8

It is a special case of the expression above (10.18) in reference [68]5. The general formula

was first derived in [69] using slightly different normalizations.

Combining (7.7) with (7.10) and (7.11), one obtains that

         K     Yl0, n  1      ,  �  1  ,     L  Xh    1  ,  �     1  L2     =           i         [     l(l  +  1)    2n    ]    Yl0, n,     h     L2                         (7.12)
                           2        2                 2           2                   16 

         K     Yl0, n  1      ,  �  1  ,     L  Xh    1  ,        1  L2     =             i             (l  n)(l � n + 1)  Yl0, n�1, h L2 .
                           2        2                 2           2                   -

                                                                                         8

These formulae are very useful because any spinor l, n can be written as a linear com-

bination   of  products                of    the   form           Yl0, n    1      ,  �  1  .  So       the  matrix         elements            (7.12)             give   us  all       we
                                                                            2            2

need to obtain (1.7). More precisely, combining formulae (2.6) and (3.153) of [70], each

spinor l, n can be decomposed as

         l, n =            2(l -             n)    Y0                       1                  +             2(l +   n)     Y0                     1               .          (7.13)
                                l                                               2                                 l                                    2
                                                   l-       1  ,  n+  1            ,  -  1                                     l-  1  ,  n-  1            ,  1
                                                            2         2                  2                                         2         2               2

Combining (7.13) with (7.12), a straightforward calculation finally yields

Proposition      7.2.            Given          a  Hamiltonian                        vector         field   Xh     on      S2,  the        derivatives               LXh     1      ,  �  1
                                                                                                                                                                                  2        2

of the Killing spinors satisfy the integral identities

       l+, n ,  L   +                              -      l-, n ,           L   -                               =   c�l, n  Y0                     ,  h L2                    (7.14)
                       Xh        1  ,  �  1  L2                             Xh              1  ,  �  1  L2                       l-   1  ,  n   1
                                 2        2                                                 2        2                                2         2

with  coefficients     cl�, n          :=    i     l�n            l  -   3         l  -        1  .
                                             8     2 l                   2                     2

This is the final expression in this section. It shows that the massive 4D gauge field

linked to Xh will generically have chiral interactions with the lightest 4D fermion, i.e.

with  the  fermion               appearing               in       the     higher-dimensional                         spinor                     1  ,  1   .     The       amount        of
                                                                                                                                                2     2

chirality depends on Xh through the harmonic components of the Hamiltonian function h.

The Killing choice Xh =  corresponds to a choice of Hamiltonian function proportional

to the spherical harmonic Y10,0. Since spherical harmonics with different indices are L2-

orthogonal, the integral on the right-hand side of (7.14) will vanish unless l = 3/2 and

n = 1/2. But in this case the whole right-hand side of (7.14) still vanishes. Thus, in the

Killing  case,  the    derivative                  LX          does       not         have        chiral        interactions             with       , 1      ,  1     as  expected.
                                                                                                                                                       2        2

5In this reference, the Hamiltonian field Xh is defined with the opposite sign of (4.18). These signs cancel
 in the definition (7.8) of Poisson bracket.

                                                                                            32
8. Conserved currents

Let be  and  be two complex spinors on P = M4 � K equipped with a Lorentzian,
submersive metric gP  (gM , A, gK). General properties of the Dirac operator say that

 D/ P ,  0 +  , D/ P  0 = divgP [ jP (, ) ] .    (8.1)

Here �, �0 is the pairing (2.12) while jP is the complex vector field on P defined by

jP (, ) := gPrs  , ur �  0 us ,                  (8.2)

where {ur} is a local, gP -orthonormal trivialization of T P . In the Riemannian case,
formula (8.1) is derived in [57, sec. 2.3.4], for example, and the Lorentzian case is similar.
So when  and  are in the kernel of D/ P , the vector field jP (, ) has vanishing divergence
on P . Note also that we have the general identity jP (P , P ) = jP (, ) and that, for
the particular choices  =  and  = P , the respective jP are real vector fields on P .
All this follows from definition (8.2) and the algebraic properties stated in section 2.3.1,
such as (2.14), (2.15), and the fact that Clifford multiplication by a vector is self-adjoint
with respect to the �, �0 pairing on a Lorentzian manifold.

    Now let {X�} be a gM -orthonormal trivialization of T M4 and denote by X�H the
respective basic lifts to P . Define a vector field on M4 through the fibre integrals

jM (, ) := gM�             , X�H �  0 volgK X .  (8.3)

                       K

Then jM is a section of T M4  C. Its divergence with respect to gM is nicely related to
the higher-dimensional divergence of jP .

Proposition 8.1. Let  and  be any two spinors on P equipped with a Lorentzian,
submersive metric gP  (gM , A, gK). Then the divergence of the four-dimensional vector
field jM (, ) is given by the fibre-integral

divgM [ jM (, ) ] = divgP [ jP (, ) ] volgK .    (8.4)
                                          K

In particular, when  and  are in the kernel of D/ P , it follows from (8.1) that the
divergence of jM (, ) vanishes on M4.

    This result is a special case of proposition A.1, proved in the appendices. Now let

 be a Killing vector field on (P, gP ). As was seen in (4.7), the Kosmann-Lichnerowicz
derivative L commutes with the Dirac operator D/ P . Thus, if D/ P  = 0, the spinor
 = L is also in the kernel of D/ P . So we get the first part of:

                          33
Corollary 8.2. Let  be a complex spinor in the kernel of D/ P and let  be a Killing
vector field on P . Then the vector field jM (L, ) on M4 has vanishing divergence with
respect to gM . When  is vertical on P , the vector field jM is purely imaginary.

    The last assertion is proved in appendix A. It uses the following result:

Lemma 8.3 ([44], lemma A.3). Let gP  (gM , A, gK) be a submersive metric on P . Then
a vertical vector field  is Killing with respect to gP if and only if its restriction to each
fibre is Killing with respect to gK and, additionally, the Lie bracket [, XH] vanishes for
every vector field X on M4.

    This lemma shows that finding Killing vector fields on P is not easy when the sub-
mersion geometry is non-trivial. When the gauge fields are turned on, even if the internal
metric gK remains constant throughout M4, the Killing fields of gK may no longer be
Killing fields of gP . If  is a Killing field of gK and we regard it as vertical vector field on
P that is constant along M4, its Lie bracket with a basic field is

[, XH] = [, X] + [, Aa(X) ea] = Aa(X) [, ea] .  (8.5)

The right-hand side does not vanish in general. So lemma 8.3 says that  is not Killing
on P and we do not get conserved currents associated with . A nice exception occurs if
we assume that the geometry of P satisfies the following conditions:

 i) the internal metric gK is constant along M4;
ii) the gauge one-form A(X) has values in the space of Killing vector fields on K;
iii)  is a Killing field of gK that commutes with all other Killing fields on K.

Then clearly (8.5) vanishes for all X. So  will be Killing on P and will define a non-
trivial, conserved, charge current in 4D. Physically, the conditions i�iii) say that we are
in regions of spacetime where the Higgs-like scalars are constant; the non-zero gauge
fields are all massless; and the internal Killing field  is linked to an abelian, massless,
electromagnetic-like gauge field on M4. In this physical setting there are no background
fields with -charged bosons. So it is natural to find a conserved 4D fermionic current
corresponding to the -charge. For more perspective on this interpretation please compare
with the geodesic picture described in [44, sec. 5].

Remark 8.1. The example of a conserved current associated with L for a Killing  can
be generalized. Let S and R be linear operators on spinors such that D/ P S  = R D/ P  for
all . Then if  is in the kernel of D/ P , so is  = S. Thus, proposition 8.1 implies that

the 4D complex vector field jM (S, ) has vanishing divergence with respect to gM . So a

34
Kaluza-Klein model can have additional 4D conserved currents besides those defined by
Killing fields. This will happen if the metric gP supports conformal Killing vector fields
or conformal Killing-Yano forms, for example. The symmetries of the Dirac operator are
a well-studied, beautiful topic. See, for instance, [73, 74] for general accounts.

Acknowledgements

It is a pleasure to thank Nuno Roma~o for helpful comments on an earlier version of this
paper.

                                                       35
Appendices

A. Fibre-integral projection of a vector field

Let W be a vector field on P = M � K with compact support on the fibres. It determines
a vector field on the base M through the fibre-integral

          W^ M := gM�            gP (W, X�H) volgK X .                       (A.1)

                              K

Here the X� form a gM -orthonormal trivialization of T M and the X�H are their basic lifts

to P , as in (2.6). When W is itself a basic vector field on P , its projection to the base
W is well-defined and the fibre-integrals simplify to yield W^ M = (VolgK ) W . In the
general case W^ M is a more complicated average, but the following identity always holds.

Proposition A.1. Let gP  (gM , A, gK) be a submersive metric and W a vector field on

P . Then

                                divgP (W ) volgK = divgM (W^ M )             (A.2)

                              K

as functions on the base M .

Proof. Choose a local, gP -orthonormal trivialization {ur} of T P adapted to the sub-
mersion, i.e. a trivialization of the form {X�H, vj}, where the X� form a gM -orthonormal
trivialization of T M and the vj form a gK-orthonormal trivialization of T K. On a Rieman-
nian submersion the inner-product gP (X�H, XH) is constant along the fibres and equal to
gM (X�, X). So we can decompose

          W = W V + W H = W V + � X�H                                        (A.3)

with coefficient functions � := gM� gP (W, XH) that vary both along the base and the
fibres. This leads to a decomposition of the divergence into four terms:

          divgP (W ) := gPrs gP (ur W, us)                                   (A.4)
                       = gKij gP (viW V , vj) + gKij gP (vi W H, vj)
                           + gM� gP (X�H W V , XH) + gM� gP (X�H W H, XH) .

We will analyze each term separately. Using (2.7e), we have that

          gKij gP (viW V , vj) = gKij gK (vKi W V , vj) = divgK (W V ) .     (A.5)

                                 36
Using (2.7b) and the fact that the curvature FAa is anti-symmetric,

   gM� gP (X�H W V , XH) = - gM� gP (W V , X�H XH)

                               =  -  1      gM�  FAa (X� ,  X )  gK  (ea,  W  V  )  =  0.        (A.6)
                                     2

Using (2.7d) and the calculation (B.14) of the trace of the second fundamental form,

   gKij gP (vi W H, vj)  =  - gKij gP (W H, vi vj)  =       1    �   gKij  (dAgK )X�(vi,   vj )
                                                            2

                         = � X� log |gK | + Aa� divgK (ea) .                                     (A.7)

Finally, using (2.7c), decomposition (A.3) and the definition of basic lift XH,

gM gP (XH W H, XH) = � gM gM (M X X�, X) + gM (gM )� (d�)(XH)

                         = � divgM X� + (d�)(X�) + A�a (d�)(ea) .                                (A.8)

Thus, the combination of all four terms is

divgP (W ) = divgK ( W V + A�a � ea ) + � � log |gK | + �� + � divgM X� . (A.9)

Defining the vertical field U = W V + Aa� � ea, it follows that

divgP (W ) volgK = LU (volgK ) + �(� volgK ) + � (divgM X�) volgK .                              (A.10)

Now denote � := � volgK . The fibre-integral K � is a function on the base M . So
integrating (A.10) over the fibre, using Stokes' theorem and changing the order of the
fibre-integral and a directional derivative on the base,

   divgP (W ) volgK = � � + (divgM X� ) � = divgM X� � .                                         (A.11)

K                           K                    K                                  K

This concludes the proof of proposition A.1.

Proof of corollary 8.2. The first assertion follows from proposition 8.1 with the choice
 = LW . For the second assertion, note that (4.8), remark 4.1 and relation (4.3)
applied to the Killing case imply that

 LW , X�H �  0 = - , LW (X�H � ) 0 + LW  , X�H �  0                                              (A.12)

   = -  , X�H � LW  0 -  , [W, X�H] �  0 + LW  , X�H �  0.

                                            37
Now, if W is Killing and vertical on P , lemma A.3 in [44] implies that [W, X�H] is always
zero and the restriction of W to the fibres is Killing with respect to gK. In particular
divgK W = 0. So it follows from Stokes' theorem and (4.10) that

              LW , X�H �  0 volgK = -  , X�H � LW  0 volgK                                                        (A.13)

          K                                                     K

                                                       = -  X�H � , LW  0 volgK
                                                                    K

                                                       = -  LW , X�H �  0 volgK
                                                                    K

is a purely imaginary number.

B. Proofs for section 3

This appendix contains proofs of propositions in section 3. It deals with the decompos-
ition of the higher-dimensional spinor connection and Dirac operator on a Riemannian
submersion P = M � K. The notation is as in sections 2 and 3.

Proof of proposition 3.1. First consider the case of a vertical vector field U . In the local
trivialization {X�H, vj} of T P , formula (3.1) decomposes as

U   =  U     +    1     gM�  gM  gP (U X�H, XH) XH              �  XH      �  
                  4

    +  1  gKij    gKrs  gP  (U vi,  vr)  vj  �  vs  �    +   1  gM�  gKij  gP  (U  X�H,  vi)  XH   �  vj  �    .  (B.1)
       4                                                     2

We want to simplify this expression when the higher-dimensional spinor is of the form

 = H(x)  (x, y), as in (2.21). Since U is vertical and  does not depend on the

coordinate on K,

                                 U (H  ) = H  (U ) .                                                              (B.2)

Using that  has no torsion, that [U, XH] is a vertical vector field, that gP (U, X�H) van-
ishes, that gP (X�H, XH) is constant along the fibres, and also formula (2.7b), we get

          gP (U X�H, XH) = gP (X�HU, XH) = - gP (U, X�HXH)

                                       =        1   gP (FA(X�, X), U ) .                                          (B.3)
                                             -
                                                2

Using that  is gP -compatible, that gP (X�H, vi) vanishes, and identity (2.7d), we get

          gP (U X�H, vi) = LU [ gP (X�H, vi) ] - gP (X�H, U vi)                                                   (B.4)

                                    =    - gP (X�H, U vi)          =  1       (dAgK )X�(U, vi)  .
                                                                      2

                                                         38
Combining these formulae and using (2.20), decomposition (B.1) becomes (3.3), as desired.

    Next, consider the case of a basic vector field Y H. In the local trivialization {X�H, vj}
of T P , formula (3.1) decomposes as

Y H     =     Y H         +  1  gM�   gM   gP (Y H X�H, XH) XH              �  XH  �  
                             4

   +    1     gKir  gKjs  gP (Y Hvi, vj) vr  �  vs   �     +  1   gM� gKij  gP (Y H X�H, vi) XH � vj       �  .  (B.5)
        4                                                     2

Take a spinor on P of the form  = H(x)(x, y), as in (2.21). First, from the definition
(2.6) of Y H, the directional derivative of the local functions representing the spinors is

                  Y H(H  ) = (Y )H   + H  Y  + Aa(Y ) ea .                                                       (B.6)
Secondly, using (2.7c) and (2.20),

gP (Y HX�H, XH) XH � XH � (H  ) = gM (Y X�, X) (X � X � )H   . (B.7)

Thirdly, using (2.7b) and (2.20), the last term in (B.5) becomes

1  gM�  gKij  FAa(Y, X�)     gP (ea,  vi)  (X    �   5  �  )H      (vj  �  )
4

                                                    =     1  gM�  FAa(Y, X�)    (X    � 5  � )H    (ea  �  )  .  (B.8)
                                                          4

Fourthly, from relation (2.20) between Clifford multiplication on SC(P ) and SC(V ),

gKir gKjs gP (Y Hvi, vj) vr � vs � (H  ) = gKir gKjs gP (Y Hvi, vj) H  (vr � vs � ) . (B.9)

This last expression can be further developed to make the gauge fields Aa(Y ) appear
explicitly. Using that  has no torsion, the definition (2.6) of horizontal lift, and the fact
that the Aa(Y ) are constant functions along the fibres, we have

   gP (Y Hvi, vj) = gP ( viY H + [Y H, vi], vj )                                                                 (B.10)

                          = - gP ( Y H, vivj ) + gP ( [Y, vi] + Aa(Y )[ea, vi], vj )

                          =  1  (dAgK  )Y  (vi,  vj  )  +    gP ( [Y, vi], vj)  +     Aa(Y ) gK([ea, vi], vj) .
                             2

The last equality also uses identity (2.7d) for the second fundamental form of the fibres.

Since the connection  is metric, gP (Y Hvi, vj) is anti-symmetric in the indices i and j.
In contrast, the first term in the last line is symmetric. So we can eliminate it through

              2 gP (Y Hvi, vj) = gP (Y Hvi, vj) - gP (Y Hvj, vi)                                                 (B.11)
                                  = gP ( [Y, vi], vj) - gP ( [Y, vj], vi)
                                      + Aa(Y ) gK([ea, vi], vj) - gK([ea, vj], vi) .

                                                             39
Finally, substituting (B.6), (B.7), (B.8) and (B.9) into decomposition (B.5), using the
standard definition of the covariant derivative M  on M (analogous to (3.1)), and using
the definition of Kosmann-Lichnerowicz derivative in (4.1), we get formula (3.4) for the
higher-dimensional covariant derivative Y H, as desired.

Proof of proposition 3.3. We first calculate the vertical part of the higher-dimensional
Dirac operator. It follows from (3.3) and (2.20) that

vj � vj  = (5 � )H  (vj � vj )                                                 (B.12)

               -  1  gM� gM (FAa)� gK (ea, vj) (5 � X � X � )H  (vj � )
                  8

               +  1  gM�  i (dAgK )X�(vj, vi) (5 � X � 5 � )H  (vj � vi � ) .
                  4

Now, the covariant derivative (dAgK)X�(vj, vi) is symmetric in i and j, while the Clifford

product vj � vi is anti-symmetric for i = j. So a sum over j simplifies to

ij (dAgK )X�(vj, vi) vj � vi �  = j (dAgK )X�(vj, vj) vj � vj �                (B.13)

                                                    = - j (dAgK )X�(vj, vj)  .
But formulae (2.25) and (2.28) in section 2.4 of [10] say that the metric trace of dAgK is

            j(dAgK )X�(vj, vj) = - 2 j gP (vj vj, X�H)

                             = 2 X� log |gK| + Aa� div(ea) .                   (B.14)

In geometric terms, the trace of the second fundamental form of the fibres is their mean
curvature vector N . Then (B.14) is just the inner-product -2gP (N, X�H) written in a way
that makes explicit the dependence on the gauge fields, as in [10].

Thus, summing (B.12) over j and using that 5 5 = 1, the result is

j vj � vj   = (5 � )H  (D/ K)     -  1  (FAa)� (5 � X� � X � )H  (ea � )       (B.15)
                                     8

               +  1  gM�  X� log  |gK| + A�a div(ea) (X � )H   .
                  2

To calculate the horizontal part of D/ P , take (3.4) and observe that

X�H � XH = (X� � XM )H   + Aa (X� � )H  Lea                                    (B.16)

            +  1  gM  FAa(X, X)   (X� � X � 5 � )H  (ea � )
               4

            + (X� � )H  X 

            + (X� � )H    1       ij gP ([X, vi], vj) - gP ([X, vj], vi) vi � vj �  .
                          8

Contracting this expression with gM� and summing with B.15 leads directly to 3.7.

                                     40
C. Proofs for sections 5 and 7

Proof of proposition 5.1. Assume condition 1. The chirality operator K anti-commutes
with D/ and maps Vm>0  Vm<0 isomorphically. Since LX commutes with K, it is clear
that LX also preserves Vm<0. But if LX preserves Vm>0  Vm<0, the inner-product

LX , L2 = - , LX L2                      (C.1)

must vanish for all  in Vm>0  Vm<0 and all  in V0. This follows from the orthogonality
of decompositions (5.11) and the fact that, due to (4.9), LX is anti-self-adjoint with
respect to the L2-inner-product for a divergence-free X. So the spinor LX does not
have components in Vm>0  Vm<0 for any  in V0. We conclude that LX must be in
V0 for any  in V0, and hence LX preserves V0. Moreover, since LX commutes with K,
it must also preserve its eigenspaces V0� inside V0. Similarly, it must preserve the two
K-eigenspaces Vm�>0 inside Vm>0  Vm<0. This concludes the proof that condition 1 is
equivalent to condition 2.

    The definition of the chiral projections � in (1.5) implies the identity

+, LX +L2 - -, LX -L2 =  K , LX  L2 .    (C.2)

Since K preserves V0 and maps Vm>0 isomorphically onto Vm<0, condition 4 can be
rephrased as

4'.  , LX  L2 = 0 for all  in Vm>0 and all  in Vm0.

It says that LX is in the orthogonal complement of Vm0 for all  in Vm>0. But that
orthogonal complement is Vm>0 itself. So condition 4 is equivalent to condition 1.

    Now suppose that  is an eigenspinor of D/ with positive eigenvalue m > 0 and that
 is an eigenspinor with non-positive eigenvalue -�  0. Since D/ is formally self-adjoint
with respect to the L2-inner-product of spinors, we have

 , [LX , D/ ]  L2 = (� + m)  , LX  L2 .  (C.3)

The real factor (� + m) is always positive, so  , [LX, D/ ] L2 vanishes if and only if
 , LX L2 vanishes. So [LX, D/ ] is orthogonal to Vm0 if and only if LX is. In other
words, [LX, D/ ] is in Vm>0 if and only if LX is in that space. Hence, condition 3 is

equivalent to condition 1.

    To prove the last assertion in proposition 5.1, assume that points 1 and 2 of definition

5.3 are satisfied. Point 1 almost implies the full condition 4 of proposition 5.1. We only
need to check that +, LX +L2 = -, LX -L2 for all  in Vm>0 and all  in V0.
Using identity (C.2) and the fact that K is in V0 iff  belongs to that space, that is

41
equivalent to verifying that  , LX L2 vanishes for all  in Vm>0 and  in V0. But point
2 says that LX preserves V0, so LX, L2 always vanishes. For a divergence-free X,
identity (C.1) then guarantees that  , LX L2 also vanishes, as desired. Thus, points 1
and 2 of definition 5.3 imply condition 4 of proposition 5.1, and hence all of its conditions.

    In the opposite direction, suppose that LX satisfies the four equivalent conditions of
proposition 5.1. Then, conditions 2 and 4 directly imply points 2 and 1 of the definition
5.3, respectively. So we conclude that the desired equivalence holds.

Proof of lemma 7.1. Identify the punctured sphere S2 \ {N } with the complex plane
through stereographic projection and let z = x + iy be the standard complex coordinate
on C. In this chart, the round metric on S2 with total volume 4 takes the form

                                          g = 4 [ (dx)2 + (dy)2 ] ,                         (C.4)
                                                 q2

where q := 1 + |z|2.   Then the vector fields v1 =                   q  x  and v2  =  q  y  define an oriented,
                                                                     2                2

g-orthonormal frame on the tangent spaces. The standard complex structure on S2 acts

on them as Jv1 = v2. The coordinate vector field corresponding to the azimuthal angle
0 <  < 2 on the sphere is

                                              = - y x + x y .                               (C.5)

It is a Killing vector field with respect to g. The gamma matrices in two Euclidean
dimensions can be taken to be


                          =               0 -i                          =  0 -1             (C.6)
                       1                                         2               .
                                                                               0

                                     -i            0                        1

They are anti-hermitian matrices satisfying {a, b} = -ab I2. The chirality operator

(4.14) takes the form


                                       K        =            =     10                       (C.7)
                                                   i 1 2                   .
                                                                        -1

                                                                  0

A vector field X = X1v1 + X2v2 on S2 acts on spinors as X �  = (X11 + X22) . Then
a direct computation using formula (7.6) for the Killing spinors leads to the identities

                        1                    X  �    1       =       i  g(X, )              (C.8)
                             2            ,            2         
                                 ,  �  1           ,   �  1         4
                                       2                  2

K                         1               ,  X  �    1       =       1  g(JX, )
                              2                        2         �
                                 ,  �  1           ,   �  1         4
                                       2                  2

K                         1      ,  �  1  ,  X  �  ,  1   1  =    1        d(Y10, 1)(X) .
                              2        2               2  2           6

                                                             42
In the last equality, the functions Y10, �1 are the scalar spherical harmonics on S2 written
explicitly in (7.9).

Now,  since  the       1        ,  �  1     are         Killing  spinors,           identities   (7.5)      allow        us    to    simplify  formula
                           2          2

(4.15) for the Kosmann-Lichnerowicz derivative and write

                    L  X                          =        -  1  X  �  1               -      i  div(J X )  K     1               .            (C.9)
                                                                           2                                          2
                                   1  ,  �  1                 2               ,  �  1         4                          ,  �  1
                                   2        2                                       2                                          2

Combining this formula with (C.8) yields

K                                  LX         1               =           1         � g(JX, )        +      i                        f�        (C.10)
      f      1               ,                  2                -                                            div(J X )
                 2  ,  �  1                          ,  �  1        8
                          2                                2                                                2

K     f      1      ,  �  1  ,     LX         1      ,     1  =  �      1              f�  d(Y10, 1)(X)     .
                 2        2                     2          2           2 6

Next, consider the case where Xh is a Hamiltonian vector field on S2 determined by a
function h, as in (4.18). Then formula (4.19) leads to the first two equalities in

                                            div(JXh) =  h                                                                                      (C.11)

                                     g(J Xh, ) = g( grad h,  ) = L h
                                   d(Y10, �1)(Xh) = LXh Y10, �1 = {Y10, �1 , h} .

The last equality follows from the definition of Poisson bracket (e.g. [66, sec. 18.3]). Thus

             K                  1                 ,     LXh                   =            1                +     i               f�           (C.12)
                             f      2                           1                      -         � L h              h
                                         ,  �  1                  2,�  1                  8
                                               2                       2                                          2

             K               f  1        ,  �  1  ,     LXh     1,     1      =        �     1   f�  {Y10, 1   ,  h}        .
                                    2          2                  2    2                    
                                                                                           2 6

Lemma 7.1 is concerned with the integrals over S2 of the matrix elements (C.12). But

the Laplacian is self-adjoint with respect to the L2-product of functions, so

                                                           f� h volg = (f�) h volg .                                                           (C.13)
                                                  S2                                   S2

Since  is Killing with respect to g, it has zero divergence, so from Stokes' theorem:

                                         S2 f� (Lh) volg = - S2(Lf�) h volg .                                                                  (C.14)

Moreover, for any three functions the Poisson bracket satisfies the identity [66, sec. 18.3]

                                   {f1 , f2 f3} = {f1 , f2} f3 + f2 {f1 , f3} .                                                                (C.15)

Since Hamiltonian vector fields have zero divergence, the integral of the Poisson bracket of
any two functions always vanishes. So the integral of the left-hand side of (C.15) vanishes,
and, for the obvious choices of fj, we get that

S2 f� {Y10, �1 , h} volg = - S2{Y10, �1 , f�} h volg =                                                 {f�,    Y10, �1} h            volg  .   (C.16)

                                                                                                     S2

Combining (C.12) with the integral identities (C.13), (C.14) and (C.16), we finally get

the formulae (7.7) in lemma 7.1.

                                                                                 43
References

 [1] E. Witten: Search for a realistic Kaluza-Klein theory, Nucl. Phys. B186 (1981),
      412�428.

 [2] M. Duff, B. Nilsson and C. Pope: Kaluza-Klein supergravity, Phys. Reports 130
      (1986), 1�142.

 [3] D. Bailin and A. Love: Kaluza-Klein theories, Rep. Prog. Phys. 50 (1987), 1087�1170.

 [4] R. Coquereaux and A. Jadczyk: Riemannian geometry, fiber bundles, Kaluza-Klein
      theories and all that...., World Scientific Publishing, 1988.

 [5] L. Castellani, P. Fr�e and R. D'Auria: Supergravity and superstrings: a geometric
      perspective, Vol. 2, Part five, World Scientific Publishing, 1991.

 [6] J. Overduin and P. Wesson: Kaluza-Klein gravity, Phys. Reports 283 (1997), 303�
      380.

 [7] F. Englert and R. Brout: Phys. Rev. Lett. 13 (1964), 321.

 [8] G. Guralnik, C. Hagen and T. Kibble: Phys. Rev. Lett. 13 (1964), 585.

 [9] P. Higgs: Phys. Lett. 12 (1964), 132.

[10] J. Baptista: Internal symmetries in Kaluza-Klein models, J. High Energ. Phys. 2024
      (2024), 178.

[11] A. Besse: Einstein manifolds, Classics in Mathematics, Springer-Verlag, 1987.

[12] N. Manton: Fermions and parity violation in dimensional reduction schemes, Nucl.
      Phys. B193 (1981), 502�516.

[13] G. Chapline and R. Slansky: Dimensional reduction and flavor chirality, Nucl. Phys.
      B209 (1982), 461�483.

[14] E. Witten: Fermion quantum numbers in Kaluza-Klein theory, in Shelter Island II,
      Proc. of the 1983 Shelter Island conference, MIT Press, 1985.

[15] C. Wetterich: Massless spinors in more than four dimensions, Nucl. Phys. B211
      (1983), 177�188.

[16] C. Wetterich: Dimensional reduction of Weyl, Majorana and Majorana-Weyl spinors,
      Nucl. Phys. B222 (1983), 20�44.

                                                       44
[17] M. Atiyah and F. Hirzebruch: Spin-manifolds and group actions, in Essays on To-
      pology and Related Subjects, Springer-Verlag, 1970, 18�28.

[18] G. Chapline and N. Manton: The geometrical significance of certain Higgs potentials:
      an approach to grand unification, Nucl. Phys. B184 (1981), 391�405.

[19] S. Randjbar-Daemi, A. Salam and J. Strathdee: Spontaneous compactification in
      six-dimensional Einstein-Maxwell theory, Nucl. Phys. B214 (1983), 491�512.

[20] P. Frampton and K. Yamamoto: Unitary flavor unification through higher dimen-
      sionality, Phys. Rev. Lett. 52 (1984), 2016�2018.

[21] D. Cremades, L. Ibanez and F. Marchesano: Computing Yukawa couplings from
      magnetized extra dimensions, J. High Energ. Phys. 05 (2004), 079.

[22] C. Wetterich: Dimensional reduction of fermions in generalized gravity, Nucl. Phys.
      B242 (1984), 473�502.

[23] S. Weinberg: Quasi-riemannian theories of gravitation in more than four dimensions,
      Phys. Letters 138B (1984), 47�51.

[24] J. Moffat: Chiral fermions in non-Riemannian Kaluza�Klein theory, J. Math. Phys.
      26 (1985), 528�531.

[25] D. Neville: Torsion and chiral fermions in Kaluza-Klein theories, Phys. Rev. D33
      (1986), 363�369.

[26] D. Tchrakian: Comment on `Torsion and chiral fermions in Kaluza-Klein theories',
      Phys. Rev. D34 (1986), 3930�3931.

[27] L. Dixon, J. Harvey, C. Vafa and E. Witten: Strings on orbifolds, Nucl. Phys. B261
      (1985), 678�686.

[28] L. Dixon, J. Harvey, C. Vafa and E. Witten: Strings on orbifolds (II), Nucl. Phys.
      B274 (1986), 285�314.

[29] A. Pomarol and M. Quiro�s: The standard model from extra dimensions, Phys. Letters
      438B (1998), 255�260.

[30] K. Dienes, E. Dudas and T. Gherghetta: Grand unification at intermediate mass
      scales through extra dimensions, Nuclear Phys. B537 (1999), 47�108.

[31] H. Cheng, B. Dobrescu and C. Hill: Electroweak symmetry breaking and extra di-
      mensions, Nuclear Phys. B589 (2000), 249�268.

                                                       45
[32] H. Georgi, A. Grant and G. Hailu: Chiral fermions, orbifolds, scalars and fat branes,
      Phys. Rev. D63 (2001), 064027.

[33] R. Sundrum: TASI 2004 lectures: to the fifth dimension and back, in Physics in
      D >= 4, Proc. Theor. Adv. St. Inst. Elementary Particle Physics (2005), 585�630.

[34] C. Cs�aki, J. Hubisz and P. Meade: TASI lectures on electroweak symmetry breaking
      from extra dimensions, in Physics in D >= 4, Proc. Theor. Adv. St. Inst. Elementary
      Particle Physics (2005), 703�776.

[35] J. Bourguignon: A mathematician's visit to Kaluza-Klein theory, Rend. Sem. Mat.
      Univ. Politec. Torino (1989), 143�163.

[36] T. Kaluza: Zum Unitt�asproblem in der Physik, Sitzungsber. Preuss. Akad. Wiss.
      Berlin Math. Phys. K1 (1921), 966�972.

[37] O. Klein: Quantentheorie und fu�nfdimensionale Relativita�tstheorie, Zeitschrift Phys.
      37 (1926), 895�906.

[38] A. Einstein and P. Bergmann: On a generalization of Kaluza's theory of electricity,
      Annals Math. 39 (1938), 683�701.

[39] P. Jordan: Relativistische Gravitationstheorie mit variabler Gravitationskonstante,
      Naturwissenschaften 33 (1946), 250�251.

[40] Y. Thiry: Les �equations de la th�eorie unitaire de Kaluza, Comptes Rendus Acad.
      Sci. Paris 226 (1948), 216�218.

[41] B. DeWitt: Dynamical theory of groups and fields, in Lectures at 1963 Les Houches
      School, Gordon and Breach, 1964, 585�820.

[42] R. Kerner: Generalization of the Kaluza-Klein theory for an arbitrary non-abelian
      gauge group, Ann. Inst. H. Poincar�e 9 (1968), 143�152.

[43] Y. Cho: Higher-dimensional unifications of gravitation and gauge theories, J. Math.
      Phys. 16 (1975), 2029�2035.

[44] J. Baptista: Test particles in Kaluza-Klein models, Class. Quantum Grav. 42 (2025),
      045007.

[45] B. O'Neill: The fundamental equations of a submersion, Michigan Math. J. 13 (1966),
      459�469.

                                                       46
[46] C. Ehresmann: Les connexions infinit�esimales dans un espace fibr�e diff�erentiable,
      Colloque de Topologie (1950), 29�55.

[47] R. Hermann: A sufficient condition that a mapping of Riemannian manifolds be a
      fibre bundle, Proc. Amer. Math. Soc. 11 (1960), 236�242.

[48] M. Falcitelli, S. Ianus and A. Pastore: Riemannian submersions and related topics,
      World Scientific Publishing, 2004.

[49] A. Moroianu, Op�erateur de Dirac et submersions riemanniennes. Ph.D. thesis. E�cole
      Polytechnique, Paris, 1996.

[50] E. Loubeau and R. Slobodeanu: A characterization of Dirac morphisms, Commun.
      Math. Phys. 288 (2009), 1089�1102.

[51] P. Reynolds, On conformal submersions and manifolds with exceptional structure
      groups, PhD Thesis, University of Edinburgh, 2011.

[52] Y. Kosmann: D�eriv�ees de Lie des spineurs, Ann. di Matematica Pura ed Applicata
      91 (1971), 317�395.

[53] I. Benn and R. Tucker: An introduction to spinors and geometry with applications in
      physics, IOP Publishing, 1987.

[54] T. Friedrich: Zur Abha�ngigkeit des Dirac-Operators von der Spin-Struktur, Coll.
      Math. 48 (1984), 57�62.

[55] N. Ginoux: The Dirac spectrum, Springer, 2009.

[56] H. Lawson and M. Michelsohn: Spin geometry, Princeton Univ. Press, 1989.

[57] J. Bourguignon, O. Hijazi, J. Milhorat, A. Moroianu and S. Moroianu: A spinorial
      approach to Riemannian and conformal geometry, European Mathematical Society,
      2015.

[58] B. Dolan: On the elimination of Pauli couplings in Kaluza-Klein theories using tor-
      sion, Phys. Letters 159B (1985), 279�283.

[59] A. Lichnerowicz: Spineurs harmoniques, Comptes rendus Acad. Sc. Paris, groupe 1
      257 (1963), 7�9.

[60] H. Baum: Spin-Strukturen und Dirac-Operatoren u�ber pseudoriemannschen Mannig-
      faltigkeiten, B. G. Teubner, 1981.

                                                       47
[61] M. Hamilton: Mathematical gauge theory: with applications to the Standard Model
      of particle physics, Universitext, Springer International Publishing, 2017.

[62] J. Baez and J. Huerta: The algebra of grand unified theories, Bull. Amer. Math. Soc.
      47 (2010), 483�552.

[63] Y. Imayoshi and M. Taniguchi: An introduction to Teichmu�ller spaces, Springer-
      Verlag, 1992.

[64] C. Ba�r: The Dirac operator on space forms of positive curvature, J. Math. Soc. Japan
      48 (1996), 69�83.

[65] J. Gracia-Bond�ia, J. Va�rilly and H. Figueroa: Elements of noncommutative geometry,
      Birkha�user, 2001.

[66] A. Silva: Lectures in symplectic geometry, Springer, 2008.
[67] J. Jackson: Classical electrodynamics, 3rd ed., John Wiley & Sons, 1998.
[68] P. Rios and E. Straume: Symbol correspondences for spin systems, Birkha�user, 2014.
[69] L. Freidel and K. Krasnov: The fuzzy sphere -product and spin networks, J. Math.

      Phys. 43 (2002), 1737�1754.
[70] G. Torres del Castillo: 3-D Spinors, spin-weighted functions and their applications,

      Springer, 2003.
[71] E. Newman and R. Penrose: Note on the Bondi-Metzner-Sachs group, J. Math. Phys.

      7 (1966), 863�870.
[72] J. Goldberg, A. Macfarlane, E. Newman, F. Rohrlich and E. Sudarshan: Spin-s

      spherical harmonics and �, J. Math. Phys. 8 (1967), 2155�2161.
[73] I. Benn and J. Kress: First-order Dirac symmetry operators, Class. Quantum Grav.

      21 (2004), 427�431.
[74] M. Cariglia, P. Krtous and D. Kubizna�k: Commuting symmetry operators of the

      Dirac equation, Killing-Yano and Schouten-Nijenhuis brackets, Phys. Rev. D84
      (2011), 024004.

                                                       48
