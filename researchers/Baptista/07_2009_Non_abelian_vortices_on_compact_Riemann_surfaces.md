# 2009 Non abelian vortices on compact Riemann surfaces

**Source:** `07_2009_Non_abelian_vortices_on_compact_Riemann_surfaces.pdf`

---

arXiv:0810.3220v2 [hep-th] 27 Feb 2009                                                                                                   ITFA-2008-41

                                         Non-abelian vortices on compact Riemann
                                                                   surfaces

                                                                             J. M. Baptista 

                                                                           Institute for Theoretical Physics 
                                                                                 University of Amsterdam

                                                                               October 2008

                                                                                 Abstract

                                            We consider the vortex equations for a U(n) gauge field A coupled to a Higgs field
                                         with values on the n � n matrices. It is known that when these equations are defined
                                        on a compact Riemann surface , their moduli space of solutions is closely related to
                                        a moduli space of  -stable holomorphic n-pairs on that surface. Using this fact and a
                                        local factorization result for the matrix , we show that the vortex solutions are entirely
                                        characterized by the location in  of the zeros of det  and by the choice of a vortex
                                        internal structure at each of these zeros. We describe explicitly the vortex internal spaces
                                        and show that they are compact and connected spaces.

                                            e-mail address: [email redacted]
                                            address: Valckenierstraat 65, 1018 XE Amsterdam, The Netherlands
1 Introduction

1.1 The context

The simplest and earliest-known type of vortex equations appeared in the classical abelian
Higgs model. It involves just one U(1) gauge field and one complex scalar Higgs field.
The solutions to these equations are generally known as Nielsen-Olesen vortices [1], and
the moduli space of such solutions was first described by Taubes for vortices living in the
complex plane [13], and by Bradlow for vortices living in a compact Ka�hler manifold [6].
After that several far-reaching generalizations of the vortex equations have been studied.
In one of these the gauge group can be any compact connected Lie group and the Higgs
field can have values in any Ka�hler manifold equipped with a hamiltonian action of the
group. Among these generalizations, perhaps the simplest ones to deal with and explicitly
describe solutions, are the ones that have a torus as the gauge group and a Higgs field
with values on a toric manifold [4]. These are abelian generalizations, of course. The non-
abelian generalizations, in their turn, are more difficult to analyse, but at the same time
seem to possess a richer structure and present the greatest number of novel features, as for
instance the presence of vortex internal spaces. A great deal of effort has therefore been
dedicated to studying various types of non-abelian vortex equations, and we suggest for
example [7, 14] for succinct reviews -- one from a mathematical and one from a physical
perspective -- and for references to the many original articles.

    In this paper our intent is to focus on what is probably the simplest non-abelian model
for vortices: that with one U(n) gauge field and one linear Higgs field having values on
the space of complex n � n square matrices. We will study these vortex equations when
they are defined on compact Riemann surfaces of large volume and will give an explicit
and rigorous description of their moduli space of solutions. Since an apparent feature of
the literature is that the existent rigorous accounts of non-abelian vortex moduli spaces
seem to be rather hard to be made explicit, and vice-versa, we thought that this study
could be of some interest.

    The data that we need to start with are a compact Riemann surface  and a complex
vector bundle E   of rank n over that surface. Recall that, as a C vector bundle,
E is completely characterized by its degree d, which we assume to be positive. Fixing an
hermitian metric h on E, the variables of our field theory are then the unitary connections
A on the bundle and the sections  of the direct sum nE   of n copies of E. Observe
that locally  can be regarded as a function on  with values on the complex n � n
matrices. The fact that these matrices are square introduces significant simplifications

                                                        1
to the problem, for one can take inverses and determinants at will, just as in the n = 1
abelian case; it is nevertheless possible to go a long way in studying the same non-abelian
model with a different number of copies of E [5, 8].

    The energy functional of the model is the natural Yang-Mills-Higgs functional

E(A, ) =     1   |FA|2  +  |dA|2  +  e2  |    -    1|2  ,  (1)
            2e2                      2


where FA is the curvature of the connection, dA is the covariant derivative and e and 
are positive real parameters of the theory. (Here the hermitian conjugate  is of course
defined with respect to the hermitian metric h on E, so that in a unitary trivialization of E
it is represented by the hermitian conjugate matrix of .) As is well known a Bogomolny-
type argument then shows that this energy is minimized by the fields (A, ) that solve
the vortex equations

          �A = 0                                           (2)

           FA - ie2 (  -  1) = 0 ,

where �A is the anti-holomorphic part of the covariant derivative and  is the Hodge
operator on . If these equations have any solutions at all, then the energy functional at
this minimum will have the value E(A, ) = 2 d.

    The vortex equations as written in (2) were first studied in [5], where they were related
to the problem of finding  -stable holomorphic n-pairs on . That paper was part of a
much wider effort to analyse various types of non-abelian vortex equations and, through
the use of Hitchin-Kobayashi correspondences, relate them to various types of stability
conditions for vector bundles equipped with sections [7].

    A second wave of interest, this time in the physics literature, came after the articles
[11, 2] arrived independently at the same non-abelian equations. The first one gave a
brane-theoretical description of the vortex moduli spaces; the second was concerned with
their applications to confinement in QCD. There was then a sequence of articles providing
alternative and more direct constructions of these moduli spaces, other related non-abelian
moduli spaces and studying their physical implications (closer to the perspective of this
paper, see for example [9, 3, 10], but otherwise also the many others referred to in [14]).
These constructions were carried out mostly for vortices in the complex plane  = C, and
while this choice introduces several topological simplifications, it also prevents the direct
use of the Hitchin-Kobayashi correspondences of [5, 7], for these have so far been proved
only for compact . This means that for  = C the moduli space constructions in the

                        2
physical literature are not yet completely rigorous, though they certainly are very useful
and almost surely true. In the present paper we introduce a novel way to characterize
non-abelian vortex solutions -- in terms of the locations and internal structures of the
zeros of det  -- which is applicable to both compact and non-compact . In the compact
case we can then make use of the correspondences of [5, 7] to confidently describe the
vortex moduli spaces.

1.2 The main result

We now describe the main result of the paper. As a first point, observe that associated to
E there is the natural C complex line-bundle det E  . This determinant bundle also
has degree d, its transition functions are the determinants of the transition functions of
E, and a complex structure on E induces a complex structure on det E. Now, if (A, ) is
a solution of the vortex equations, then it is well known that the connection A determines
a complex structure on E such that the section  :   nE becomes holomorphic [7].
This follows from the first vortex equation. This  then determines a holomorphic section
det  of the determinant bundle det E with the induced complex structure. But being
holomorphic, the section det  either vanishes everywhere or has exactly d zeros, counting
multiplicities. In this paper we concentrate on the latter case, i.e. on vortex solutions
such that det  does not vanish identically.

    Now suppose that zj   is one of these isolated points where det  vanishes. Making
use of local trivializations of nE that are holomorphic with respect to the complex
structure induced by A, the section  can be regarded as a holomorphic function around
zj with values on the n � n square matrices. We want to characterize the behaviour
of  around the point zj where the determinant vanishes, and for this we introduce the
following two definitions.

Definition 1.1. A vortex internal structure In is a set of data consisting of an integer k0 
0 and a sequence (V1, . . . , Vl) of non-zero proper subspaces of Cn such that Vj+1Vj = {0}
for all indices j = 1, . . . , l - 1. The order of the internal structure In is the non-negative
integer n k0 + l dimCVl.

Definition 1.2. Given a subspace V of Cn consider the orthogonal decomposition Cn =
V  V . Calling V and V the associated projections, for any complex scalar z one
defines the elementary linear transformation

                                 TV (z) := zV + V : Cn - Cn .

                                                        3
It is clear that the determinant of TV (z) is zdim V and that, for z = 0, the inverse TV (z)-1
is z-1V + V .

The use of these definitions, and a key point in our results, is that the matrix function

(z) can then be uniquely factorized around zj as

                    (z) = A(z) (z - zj)k0 TVl(z - zj) � � � TV1(z - zj)  (3)

for some internal structure In = (k0, V1, . . . , Vl) with order equal to the multiplicity of the
vanishing of det  at the point zj. Here A(z) is some holomorphic matrix function that
is invertible around zj. Since the structure In is independent of the chosen trivialization
of E, we thus have a canonical way to associate to each zero of det  a correspondent

algebraic internal structure. It then turns out that these internal structures completely

determine the vortex solution up to gauge transformations. More precisely we have the

folllowing result.

Theorem 1.3. Let E   be a complex vector bundle of rank n and degree d over a

compact Riemann surface, and assume that (Vol ) > 2d/(e2  ). Now pick any finite set

{(z1, In1), . . . , (zr, Inr)} of distinct points on the surface and associated internal structures

such that  r    order(Inl )  =  d.  Then there is a solution (A, ) of the non-abelian vortex
           l=1

equations (2), unique up to gauge equivalence, such that det  has zeros exactly at the

points zj and  factorizes around each zj with internal structure Inj . Furthermore, all
solutions of (2) with det  not identically zero are obtained in this way.

    The condition of large volume of  is required in the  -stability results of [5, 7],
which are essential in our proof of the theorem above. At the same time, observe that a
simple integration over  of the second vortex equation shows that no solutions exist if
(Vol ) < 2d/(n e2  ). Thus the general picture that arises is that for small volumes of
 there are no vortex solutions; then for Vol  in the interval between 2d/(n e2  ) and
2d/(e2  ) there is a less well known, and possibly complicated, moduli space of solutions;
and finally for large volumes of  (or big e2, or big  ) the moduli space can be neatly
described as above.

    The layout of the paper is the following. In section 2 we study holomorphic matrix
functions on the plane, proving the local factorization (3) and a generalization thereof. In
section 3 we extend this to holomorphic sections of nE   and, using the correspon-
dences of [5, 7], relate them to vortex solutions, thereby proving theorem 1.3. Finally in
section 4 we look at the space of all vortex internal structures of fixed order k, and argue
that it is a compact and connected space. We end up by comparing our description with
the special cases k = 1, 2 already studied in the literature.

                                    4
2 Holomorphic matrix functions on the plane

Matrix functions (z) defined on the plane  = C were studied at length in [9], where
they were called moduli matrices. The word moduli appears because what we really want
to study are the equivalence classes of (z)'s related by the equivalence relation (z) 
V (z) (z), with V (z) any matrix function that is invertible for all z. This equivalence can
be called a complex gauge transformation or, in the language of [9], a V-transformation.

    Our approach here is rather different from the one in [9]. In those articles the classes of
functions (z) are characterized by the coefficients of the various polynomials that appear
in the matrix; here we characterize them by the position in C of the zeros of det (z) and
by the factorization of (z) around each of these zeros. This last method seems to make
easier the generalization to compact . The first step is the following local factorization
result.

Proposition 2.1. Let (z) be a holomorphic function of one complex variable with values
on the square n�n matrices. Suppose that (z) is defined in a neighbourhood of the origin
z = 0 and that the function det (z) has an isolated zero of order k at this point. Then
there exists a unique internal structure In() = (k0, V1, . . . , Vl) such that (z) can be
written around the origin as

(z) = A(z) zk0 TVl(z) � � � TV1(z) ,         (4)

where A(z) is a holomorphic matrix function that is invertible around z = 0. Clearly the
order of this In() is precisely k.

Corollary 2.2. Any internal structure In can be obtained as In() for an appropriate
holomorphic function (z) defined around the origin.

Corollary 2.3. Two holomorphic functions 1(z) and 2(z) determine the same internal
structure if and only if 2(z) = A(z) 1(z) for some invertible matricial function A(z).

Proof. We start by showing how to obtain the structure In() from the function (z).
The integer k0 is defined as the minimal order of the zeros at the origin of the n2 entries
of the matrix (z), or in other words it is the only integer such that 1(z) := z-k0(z) is
holomorphic and does not vanish at the origin. Observe that det 1(z) has a zero of order
k - nk0 at z = 0. If this order is zero, then one takes l = 0 and no vector spaces appear
on In(). If on the other hand k - nk0 > 0, one defines V1 = ker 1(0) as the first proper
subspace of Cn. To continue with the procedure, define the second function

2(z) := 1(z) TV-11(z)

5
By applying this transformation to vectors in V1 and in V1, it is clear that 2(z) is well
defined and holomorphic around the origin, including at the origin itself. Again, if 2(0) is

invertible one takes l = 1 and the sequence of vector spaces terminates. If not, one defines

V2 = ker 2(0) and the sequence of subspaces continues. The fact that 2(0) is injective

on V1 implies that V2  V1 = {0}. Moreover, it follows from definition 1.2 that det 2(z)

vanishes at z = 0 with order k - nk0 - dim V1. Decomposing once more Cn = V2  V2

one can go on with the procedure until k - nk0 -  l    dim  Vj  vanishes  for  some  l.  When
                                                  j=1

this happens the sequence of vector subspaces terminates and the linear transformation

                     l+1(z) := l(z) TV-l1(z) = (z) z-k0 TV-11(z) � � � TV-l1(z)

will be invertible at the origin. This shows the existence of In() and of the decomposition
(4).

    For the uniqueness part, suppose that (z) given by (4) had another decomposition
associated to a second set of data (k0 , V1, . . . , Vl). Then the function z-k0(z) would be
locally given by

A(z) TVl(z) � � � TV1 (z) = zk0 -k0 A(z) TVl (z) � � � TV1(z) .                          (5)

The essential point now is that the conditions Vj+1  Vj = {0} imply that for all s  l
the kernel of

                                     TVl(0) � � � TVs (0) = Vl � � � Vs

is Vs. This is obvious for s = l and then clear by induction. Thus applying this fact to
the left-hand side of (5), we see that z-k0(z) is well defined and has kernel V1 at the
origin. But then looking at the right-hand side, this can be true only if k0 = k0 and
V1 = V1. Arguing in the same way for the function zk0(z)TV-11(z) we would conclude that
also V2 = V2, and so forth for the other Vj's. This finishes the proof of the proposition.

    As for the first corollary, it is enough to note that given an internal structure In =
(k0, V1, . . . , Vl) we can just define

(z) := zk0 TVl (z) � � � TV1(z) .

By the uniqueness of the local factorization it is then obvious that for this choice In() =
In. The second corollary is a direct consequence of the decomposition (4).

Having understood the local internal structures associated to each zero of det , we will
now see how the set of these zeros and internal structures effectively characterizes any
matrix function defined globally on C.

6
Theorem 2.4. Let {z1, . . . , zr} be any finite set of distinct points in the complex plane
and let {In1, . . . , Inr} by any set of internal structures as defined in 1.1. Then there exists a
holomorphic function (z) with values on the n � n matrices such that det (z) has zeros
exactly at the points zj with associated internal structure Inj . This function (z) is unique
up to left multiplication by globally invertible matrix functions.

Proof. The case r = 1 follows directly from proposition 2.1. Arguing by induction,
suppose now that det (z) has zeros at the points z1, . . . , zr-1 with associated internal
structures In1, . . . , Inr-1, and that at the point z = zr the structure of (z) is given by
(k0, V1, . . . , Vl-1). Given any vector subspace Vl  Cn such that Vl  Vl-1 = {0}, we will
construct a new function ~(z) with the same structure as (z) at the points z1, . . . , zr-1
and, at the point z = zr, internal structure (k0, V1, . . . , Vl-1, Vl). This will suffice to prove
the existence part of the theorem.

    To start with, by proposition 2.1 we have that (z) can be written around zr, and
hence globally, as

                        (z) = A(z) (z - zr)k0 TVl-1(z - zr) � � � TV1(z - zr)

for some A(z) invertible around zr. Now define the new function

                                   ~(z) := TVl(z - zr) A(zr)-1 (z) .

Since ~(z) is related to (z) by left multiplication by a matrix invertible around
z1, . . . , zr-1, the internal structures of ~(z) and (z) at these points are the same. Further-
more, observe that the matrix B(z) = TVl(z - zr) A(zr)-1 A(z) has vanishing determinant
at z = zr with order dim Vl and that the kernel of B(zr) is exactly Vl. It then follows
from proposition 2.1 that B(z) can be written as C(z) TVl(z - zr) for some C(z) invertible
around zr. In particular one can also rewrite

                ~(z) = C(z) (z - zr)k0 TVl(z - zr) TVl-1(z - zr) � � � TV1(z - zr) .

Appealing again to proposition 2.1 one concludes that the internal structure of ~(z) at
z = zr is (k0, V1, . . . , Vl), as we wanted.

    For the uniqueness, suppose that both (z) and (z) satisfy the conditions of the
theorem. Then both (z) and (z) can be factorized as in (4) around any of the zj's
with the same internal structure Inj ; only the matrices A(z) in (4) will possibly differ. But
then it is clear that the matrix (z)-1(z) is well defined and invertible around zj. Since
this happens for all of the zj's we conclude that (z)-1(z) is globally well defined and
invertible. Finally the tautology (z) = [(z)-1(z)] (z) concludes the proof.

                                                        7
3 Non-abelian vortices on compact Riemann surfaces

In the first proposition we extend the results of section 2 to compact , i.e. to holomorphic
sections of holomorphic bundles over . After that we use the Hitchin-Kobayashi-type
correspondences of [5, 7] to relate these holomorphic sections to the actual vortex solutions
over , thereby proving theorem 1.3. Finally at the end of the section we state a result
that gives a more practical interpretation of the constant  that appears in the vortex
equations. The proof is omited, because it is almost identical to the n = 1 case proved in
[6].

Proposition 3.1. Let  be a compact Riemann surface, let {z1, . . . , zr} be any set of
distinct points in the surface and let {In1, . . . , Inr} be any set of internal structures. Then
there exists a holomorphic vector bundle E   of rank n and a section  of nE such
that det  has zeros exactly at the points zj with respective internal structure Inj . This pair
(E, ) is unique up to isomorphisms of holomorphic bundles. Moreover, the degree of the
bundle E is equal to the sum of the orders of the Inj 's.

Proof. It is always possible to take a connected open set V0 of  that contains all the
zj's and is simultaneously the domain of a complex chart of the surface. Now, using
theorem 2.4, construct a holomorphic matrix function ~(z) on the open set V0 with zeros
at the points zj and respective internal structure Inj . Considering the complementary set
V1 =  \ {z1, . . . , zr}, we have that the restriction of ~(z) to the intersection V0  V1
-- which we call  -- is a n � n invertible matrix on this set, and so can be taken
as the transition function for some holomorphic vector bundle E   of rank n that
is trivial over V0 and V1. Finally, taking simultaneously the constant function 1n�n on
V1 and the function ~ on V0, we have that over the intersection of the sets they satisfy
the compatibility condition ~(z) = (z) 1n�n, and so these two functions define a global
section  of the direct sum nE. It is clear that this  has the required properties.

    To prove uniqueness, suppose that (E, ) was another pair with the required prop-
erties. Then taking local holomorphic trivializations of E and E and representing the
sections  and  by local holomorphic matrix functions, corollary 2.3 implies that the ma-
trix -1 is holomorphic and invertible throughout the whole domain of trivialization.
Moreover, if we pick different trivializations of E and E related to the initial ones by
transition functions s and s, then the matrix -1 obviously transforms as s-1s-1,
which implies that the matrices -1 actually define a global, holomorphic and invertible
section of Hom(E, E)  , or in other words an isomorphism  : E  E. Since clearly
() = , the uniqueness is proved.

                                                        8
    Finally, to justify the last statement, just observe that the section det  of the deter-
minant bundle det E   vanishes exactly at the points zj with multiplicity equal to the
order of the respective Inj . Well-known properties of line-bundles then imply that det E,
and hence E, have degree equal to the sum of the orders of the Inj 's.

    After studying the holomorphic part of the problem, i.e. after constructing the holo-
morphic vector bundles and the holomorphic sections with the required zeros and internal
structures, we are now in position to relate them to the actual solutions of the vortex
equations.

Proof of theorem 1.3. In short, the key point here comes from the results of [5, 7],
which guarantee that under the volume assumption (Vol ) > 2d/(e2  ) each pair (E, )
constructed in proposition 3.1 is in fact a  -stable n-pair, and hence there is a complex
gauge transformation that takes it to a solution of the vortex equations.

    To understand more clearly what this means, suppose that we are given a C vector
bundle E and a finite set of pairs (zj, Inj ) satisfying the conditions of theorem 1.3. Then
by the proposition above there is a complex structure on E and a holomorphic section 
of nE such that det  vanishes at the zj's with internal structure Inj . Using the fixed
hermitian metric h on E, this complex structure on its turn defines a natural connection
A on E -- the so-called Chern connection -- such that �A = 0. We thus have a
solution (A, ) of the first vortex equation. Observe now that while this first equation
is invariant under complex gauge transformations, i.e. gauge transformations with the
complexification U(n)C = SL(n, C) as the gauge group, the second vortex equation is
certainly not invariant. This entitles us to ask whether a complex gauge transformation
can take our pair (A, ), which a priori only satisfies the first equation, to a solution of
also the second equation, and hence to a full vortex solution. The answer is that this is
possible whenever the initial holomorphic (E, ) is a  -stable n-pair, and that in this case
the required complex gauge transformation is unique up to real gauge transformations.
We thus see how the results of [5, 7] give a vortex solution for each (E, ) constructed in
proposition 3.1.

    To end the proof of theorem 1.3 there are a few more points that should be checked.
The first is to note that complex gauge transformations on (A, ) do not change the
holomorphic structure on E induced by A (up to equivalence) and that, furthermore, they
transform  through holomorphic isomorphisms of the bundles. This means that in the
local factorization (3) the only thing that changes under complex gauge transformations is
the matrix A(z), and hence the vortex solutions that were obtained in the last paragraph

                                                        9
by means of complex transformations have exactly the same internal structures Inj at the
zeros zj as the solutions  constructed in proposition 3.1.

    The second thing to check is the uniqueness. If we were given two vortex solutions with
the same zeros of det  and internal structures, then, as described in the introduction,
we would get two complex structures on E and respective holomorphic sections with the
same zeros and In's. From the uniqueness in proposition 3.1, however, it follows that these
two holomorphic pairs (E, ) would in fact be isomorphic. Finally from the uniqueness in
the results of [5, 7] for the required complex gauge tranformations, we get that the initial
vortex solutions must have been related by a real gauge transformation.

    The last point to check is the final assertion of theorem 1.3. Here the justification
comes from the fact that, as described in the introduction, to any given vortex solution
on  with det  = 0 we can associate a finite set of pairs (zj, Inj )'s. Using these pairs
to construct our own vortex solution according to the prescriptions of this section, the
uniqueness part in theorem 1.3, which is already proved, assures us that the given vortex
solution is in fact gauge equivalent to the constructed one.

    Another interesting property of the non-abelian vortex solutions, proved as in [6], is
the following.

Proposition 3.2. Let (A, ) be a solution of the vortex equations (2) on a C hermitian
bundle (E, h) of rank n. Then the norm of each of the n components j of the section the
section  :   nE satisfies the majoration |j(z)|2h   for all z in .

4 On the space of vortex internal structures

4.1 Connectedness and compactness

In the introduction to this paper we defined an internal structure In as a set consisting of
an integer plus a sequence of vector subspaces of Cn satisfying a non-intersection condition.
The advantages of this characterization are that it is simple enough, general for all n and,
through the local factorization (3), directly related to the actual behaviour of the vortex
solutions. A significant disadvantage is that it does not reveal transparently the main
geometric and topological properties of the space of all internal structures, i.e. of the
internal configuration space of the vortex. For example a priori one could think that the
non-intersection condition would imply that these internal spaces are non-compact, a fact
that is not true. In this final section of the paper we will spend some time looking at

                                                       10
these matters, and will conclude that in a natural topology the space In,k of all internal

structures of fixed order k is in fact compact and connected.

To begin with observe that one can divide the space In,k into disjoint strata according

to the dimensions of the vector spaces at each point In = (k0, V1, . . . , Vl). Calling kj the

dimension of Vj, the fixed order condition means that nk0 + k1 + � � � + kl = k, and then

each vector of integers (k0, k1, . . . , kl) satisfying this equality labels exactly one of these

strata. Now inside each stratum, by definition, the dimensions of Vj are fixed, so the
only degrees of freedom are the spacial orientations of these subspaces inside Cn, and

these are parametrized by the grassmannian Gr(kj, n). Note however that due to the

non-intersection conditions not all spacial orientations are allowed, and the degrees of

freedom are parametrized only by a dense open subset of the grassmannian. This implies

that in general the different strata are not necessarily compact, although as we will see

the full space In,k is.

Now, the complex dimension of a stratum labelled by (k0, . . . , kl) is of course

l    kj  (n  -  kj ),  where  each  term  in  the  sum  is  the  dimension  of  a  grassmannian.  One
j=1

can then show that, under the constraint imposed by the fixed order, this sum is strictly

maximized with the choice k0 = 0, l = k and kj = 1 for j  1, where it has value k(n - 1).
This means that the highest dimensional stratum in In,k, i.e. the generic part of the
internal space, can be discribed as a choice of k lines in Cn, or in other words as a dense

open subset of the k-fold cartesian product of CPn-1. Moreover, we will see how the com-

plement in �k CPn-1 of this dense open subset in fact describes all the remaining strata

of In,k, although different points in the complement can represent the same non-generic
point of In,k. More precisely we have the following result.

Proposition 4.1. There is a natural surjective map  : �k CPn-1  In,k that is one-
to-one on the dense open subset of �k CPn-1 defined by the multiplets (L1, . . . , Lk) that
satisfy the non-intersection condition Lj+1  Lj = {0}. Since this map is surjective,
the set of internal structures In,k equipped with the quotient topology is a compact and

connected space.

Proof. The argument for the proof is quite simple and goes as follows. Let L =
(L1, . . . , Lk) be a point in �k CPn-1. Irrespective of whether L satisfies or not the non-
intersection condition, it makes sense to consider the the linear transformations

                                       T^L(z) := TLk (z) � � � TL1(z)
for all complex z. It is clear that T^L(z) is holomorphic and that det T^L(z) has a single
zero at z = 0 of vanishing order k. Thus applying theorem 2.4 there is a unique internal

                                                   11
structure In = (k0, V1, . . . , Vl) of order k such that
                                     T^L(z) = zk0 TVl(z) � � � TV1(z) ,

and this defines the map .
    Now call U0 the set of L's in �k CPn-1 that satisfy the non-intersection condition, i.e.

the set of L's that are proper internal structures. It is clear that  restricted to U0 is
injective with image the generic stratum of In,k; this is a tautology, for in fact  restricted
to U0 is the identity. Outside U0, on the other hand, the story is different, for if Lj+1  Lj
is non-zero then Lj+1  Lj, and it is easy to check that in this case

                 TLj+1 (z) TLj (z) = TLj+1Lj (z) .                                    (6)

This equality is a special instance of the more general lemma 4.2. It means that if Lj+1
and Lj have non-zero intersection the map  only depends on the direct sum Lj+1  Lj,
and so is clearly not injective.

    The identities (6) and (7) can also be applied recursively to show that for any vector
subspace V of Cn there exist lines L1, . . . , Ldim V such that

                 TV (z) = TLdim V (z) � � � TL1(z) .

In fact any set of orthogonal lines such that V = L1  � � �  Ldim V will do the job. This
shows that  is a surjective map.

Lemma 4.2. Let V1 and V2 be any two subspaces of Cn. Then calling W the intersection
V2  V1, the linear transformations of definition 1.2 satisfy the algebraic identity

              TV2 (z) TV1 (z) = TV2  W (z) TW V1(z) .                                 (7)

Observe moreover that the two subspaces on the right-hand side satisfy the usual non-
intersection condition, i.e. V2  W  has zero intersection with (V1  W ).

Proof. It is clear from definition 1.2 that the identity above is equivalent to the three
separate identities

(i) V2 V1 = W V2 W V1 ;

(ii)   V2 V1  =           W V1  ;
                    W V2

(iii)  V2 V1 + V2 V1      =           W V1  +                            W V2 W V1 .
                                W V2

                             12
Since the proofs of these equalities are rather cumbersome and similar to each other, here
we will restrict ourselves to prove (i).

    The first step is to note that the general identity of subspaces (A + B) = A  B
implies that each of the decompositions

Cn = V1  W  (W   V1)     (8)

= V2  W  (W   V2)        (9)

is orthogonal. Having this in mind, suppose now that v is a vector in W . Then we have
that

                      W V2 W V1 (v) = W V2 (v) = 0 = V1 (v) ,

and so both sides of (i) annihilate v. If on the other hand v belongs to the subspace
W   V1 = (W  V1), we have that

W V1 (v) = 0 = V1 (v) ,

and so also in this case both sides of (i) annihilate v. Finally suppose that v sits in V1. It
is clear that

                                      W V1 (v) = v = V1 (v) ,

and hence we only have to check that

                                         V2 (v) = W V2 (v) .

But V1 being orthogonal to W , we can use the decomposition (9) to write v = v2 +w2 with
v2  V2 and w2  W   V2. Then obviously W V2(v) = w2. Now since V2(v2) = 0
and w2  V2, we finally have that V2(v) = V2(w2) = w2, which concludes the proof of
(i).

4.2 The case k = 2: comparison with the literature

The space of vortex internal structures has been described previously in the literature in
the cases k = 1 and k = 2. The case k = 1 is simple enough: it follows directly from
definition 2 that In,1  CPn-1, as was known. The case k = 2 has been studied in [3, 12]
for n = 2 and in [10] for general n. Here we will compare our results with those of [10],
finding in the end that they are consistent.

13
    We start with our results. According to the previous subsection the highest dimen-
sional stratum of In,2 has dimension 2(n - 1) and isomorphic to

                 U0 = (CPn-1 � CPn-1) \ S ,

where S is the submanifold defined by L2  L1 = {0}, or in other words by L2  L1.
This is the domain U0 where the map  of proposition 4.1 is injective. Outside U0, i.e.
on S, the line L2 is perpendicular to L1, and so it follows from (6) that in this case
(L1, L2) = L1  L2  Cn, i.e. the internal structure associated to (L1, L2)  S is
the 2-dimensional vector space L1  L2. Since these vector spaces are parametrized by
the grassmannian Gr(2, n) we recognize that, in informal terms, In,2 is isomorphic to
CPn-1 � CPn-1 with the submanifold S collapsed into the grassmannian Gr(2, n).

    (Incidentally, identifying the orthogonal space L with the tangent space to CPn-1 at
the point L, it is manifest that the submanifold S is itself isomorphic to the projectiviza-
tion of the tangent bundle T CPn-1, which is a bundle over CPn-1 with fibre CPn-2.)

    In the paper [10], on the other hand, the space of vortex internal structures for k = 2
was described in the following terms. Let M be the space of 2 � (n + 1) matrices of rank
2. We can write every element M  M in the form

                 M=  2T v2                      = [ v] ,
                     1T v1

with 1, 2  Cn and v  C2. Consider now the left action of the group C � SL(2, C)

on M defined by

                 (, A) � [  v ] = [ A Av ] .              (10)

Then according to [10] there is an isomorphism

                 In,2  M / C � SL(2, C) .                 (11)

To compare this result with our previous description we will study in detail the equivalence
classes in this quotient.

    Firstly, under the action of C �SL(2, C) one can distinguish two types of orbits in M:
those with v = 0 and those with v = 0. The points in the orbits with v = 0 have linearly
independent 1 and 2, for M must have rank 2. When C �SL(2, C) acts on these points
the only invariant is the subspace V = spanC{1, 2}, and these subspaces are exactly
parametrized by the grassmannian Gr(2, n). Thus decomposing M = Mv=0  Mv=0 we
see that

                                 Mv=0 / C � SL(2, C) = Gr(2, n) ,

                     14
which is part of the internal space described in our results. Now we want to prove that
there is also an isomorphism

       : Mv=0 / C � SL(2, C) - (CPn-1 � CPn-1) \ S ,                  (12)

and so conclude that there exists a bijection between the full internal spaces In,2 as
described here and in [10].

    So consider the equivalence classes of the points [  v ] with v = 0. Since SL(2, C)
acts transitively on C2\{0}, any such equivalence class has a representative of the form

                         2T  1     .                                  (13)
                         1T  0

Observe that here 1 = 0, since the rank of the matrix must be 2. The representative (13),
however, is not unique; on the one hand because it can be acted upon by the C subgroup,

and on the other hand because the vector [1 0]T has a one dimensional stabilizer under

the SL(2, C)-action. All in all, the representative is unique up to transformations of the

form

      2T 1  -   1  a  �  2T     1     =  (2 + a1)T 1               ,  (14)
      1T 0      0  1     1T     0
                                          1T                    0

where   C and a  C. Now notice that the complex lines in Cn

            L1 := spanC{1}                                            (15)

            L2 := spanC{1 + L1(2)}

are well defined and are invariants of the transformations (14). Moreover, it is not difficult
to recognize that these lines actually distinguish the orbits of these transformations, i.e.
that two matrices of the form (13) that define different lines cannot be related by a
transformation (14), and hence lie on different C � SL(2, C) orbits. To sum up, through
the representative (13) and the definition (15) we have constructed an injective map that
takes any orbit in Mv=0 / C � SL(2, C) to a pair of complex lines (L1, L2). These lines
are clearly non-orthogonal, and it is manifest that any pair of non-orthogonal lines can be
obtained through (15) for an appropriate choice of . This finally shows that the injective
map that we constructed has image (CPn-1 � CPn-1)\S, and hence is the isomorphism
(12) that we were seeking.

    As a curiosity, the inverse of the isomorphism  can be written down very simply as

      (L1, L2) - equivalence class of    L1 (w2) 1           ,
                                         L1 (w2) 0

                         15
where w2 is any non-zero vector in L2. Furthermore, picking any non-zero vector w1 in
L1 and decomposing w2 = w1 + L1(w2), with  the complex scalar w�1T w2/|w1|2, even
the full isomorphism

                   ~ : In,2 = (CPn-1 � CPn-1)) /  - M / C � SL(2, C)

can be written down in the single expression                     L1 (w2) 
             ~ : equiv. class of (L1, L2) - equiv. class of
                                                                              w1   0

for  all  L1,  L2  in CPn-1.  To check that   ~ is really  well defined and does not depend on  the
                              must of course  make use     of the C � SL(2, C)-equivalences.
sign choice in , one

     We also note that in general the internal spaces In,k, although well-defined compact

topological spaces, are not necessarily smooth manifolds outside of the highest dimensional

stratum. This has been illustrated at         length in [10] in  otfhecasine  k=   2. In the discussion
above a reflection of this singularity is     the appearance                  the  isomorphism ~.

Acknowledgements. It is a pleasure to thank Minoru Eto, Muneto Nitta, Keisuke
Ohashi and Norisuke Sakai for kindly hosting me during a visit to TITech, Tokyo, three
years ago. I am grateful to them and to David Tong for explaining me their work on non-
abelian vortices. I am partially supported by the Netherlands Organisation for Scientific
Research (NWO) through the Veni grant 639.031.616.

References

 [1] A. Abrikosov : `On the magnetic properties of superconductors of second group';
      Sov. Phys. JETP 5 (1957), 1174 [Zh. Eksp. Teor. Fiz. 32 (1957), 1442].
      H. Nielsen and P. Olesen : `Vortex-line models for dual strings'; Nucl. Phys. B61
      (1973), 45.

 [2] R. Auzzi, S. Bolognesi, J. Evslin, K. Konishi and A. Yung : `Nonabelian Super-
      conductors: Vortices and Confinement in N = 2 SQCD'; Nucl. Phys. B673 (2003),
      187�216.

 [3] R. Auzzi, M. Shifman and A. Yung : `Composite non-abelian flux tubes in N=2
      SQCD'; Phys. Rev. D73 (2006), 105012.

                                              16
 [4] J.M. Baptista : `Vortex equations in abelian gauged sigma-models'; Commun. Math.
      Phys. 261 (2006), 161�194.

 [5] A. Bertram, G. Daskalopoulos and R. Wentworth : `Gromov invariants for holomor-
      phic maps from Riemann surfaces to grassmannians'; J. Amer. Math. Soc.9 (1996),
      529�571.

 [6] S. Bradlow : `Vortices in holomorphic line bundles over closed Ka�hler manifolds';
      Commun. Math. Phys. 135 (1990), 1�17.

 [7] S. Bradlow, G. Daskalopoulos, O. Garc�ia-Prada, R. Wentworth : `Stable augmented
      bundles over Riemann surfaces'; in "Vector bundles in algebraic geometry", London
      Math. Soc. Lecture Note Ser. 208, CUP, Cambridge, 1995, 15�67.

 [8] M. Eto, J. Evslin, K. Konishi, G. Marmorini, M. Nitta, K. Ohashi, W. Vinci and
      N. Yokoi : `On the moduli space of semilocal strings and lumps'; Phys. Rev. D76
      (2007), 105002.
      M. Shifman and A. Yung : `Non-abelian semilocal strings in N=2 supersymmetric
      QCD '; Phys. Rev. D73 (2006), 125012.
      A. Popov : `Non-abelian vortices on Riemann surfaces: an integrable case'; Lett.
      Math. Phys. 84 (2008), 139�148.

 [9] M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Moduli space of non-abelian
      vortices'; Phys. Rev. Lett. 96 (2006), 161601.
      M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Solitons in the Higgs phase
      � the moduli matrix approach �'; J. Phys. A39 (2006), R315�R392.
      M. Eto, T. Fujimori, S. Gudnason, K. Konishi, M. Nitta, K. Ohashi and W. Vinci:
      `Constructing non-abelian vortices with arbitrary gauge groups'; arXiv: 0802.1020
      [hep-th].

[10] M. Eto, K. Konishi, G. Marmorini, M. Nitta, K. Ohashi, W. Vinci and N. Yokoi :
      `Non-abelian vortices of higher winding numbers'; Phys. Rev. D74 (2006), 065021.

[11] A. Hanany and D. Tong : `Vortices, instantons and branes'; JHEP 0307 (2003) 037.

[12] K. Hashimoto and D. Tong : `Reconnection of non-abelian cosmic strings'; JCAP
      0509 (2005), 004.

[13] C.H. Taubes : `Arbitrary N-vortex solutions to the first order Ginzburg-Landau
      equations'; Commun. Math. Phys. 72 (1980), 277�292.

[14] D. Tong : `Quantum vortex strings: a review'; arXiv: 0809.5060 [hep-th].

                                                       17
