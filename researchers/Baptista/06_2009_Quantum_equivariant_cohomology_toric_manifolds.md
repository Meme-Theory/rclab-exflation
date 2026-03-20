# 2009 Quantum equivariant cohomology toric manifolds

**Source:** `06_2009_Quantum_equivariant_cohomology_toric_manifolds.pdf`

---

arXiv:0806.2091v2 [hep-th] 16 Apr 2009                                                                                                   ITFA-2008-21

                                           The quantum equivariant cohomology of
                                          toric manifolds through mirror symmetry

                                                                             J. M. Baptista 

                                                                           Institute for Theoretical Physics 
                                                                                 University of Amsterdam

                                                                                 June 2008

                                                                                 Abstract

                                            Using mirror symmetry as described by Hori and Vafa, we compute the quantum
                                        equivariant cohomology ring of toric manifolds. This ring arises naturally in topological
                                        gauged sigma-models and is related to the Hamiltonian Gromov-Witten invariants of the
                                        target manifold.

                                            e-mail address: [email redacted]
                                            address: Valckenierstraat 65, 1018 XE Amsterdam, The Netherlands
1 Introduction

Mirror symmetry was described by Hori and Vafa in [11] as a duality between sigma-
models and Landau-Ginzburg models. In the special case where the target of the sigma-
model is Calabi-Yau, this symmetry is a duality of the full N = 2 supersymmetric the-
ories, but for certain other targets, namely toric varieties and complete intersections of
hypersurfaces in toric varieties, the symmetry still exists as a duality of the associated
topological theories. The aim of this note is to illustrate in a simple setting how Hori and
Vafa's description of mirror symmetry can be used to study not only sigma-models but
also gauged sigma-models, in our case with toric targets. Since these particular gauged
non-linear models can be obtained as quotients of gauged linear sigma-models (with a
bigger gauge group), the applicability of mirror symmetry is not really a surprise, for
[11] is in fact all about dualities of gauged linear models. Nevertheless, explicit mirror
predictions for gauged sigma-models do not seem to exist in the literature, so we thought
that producing one such example may be interesting.

    The mathematical objects that we study here through the use of mirror symmetry are
the quantum equivariant cohomology rings of toric manifolds. In the usual non-equivariant
case, the quantum cohomology rings are deformations of the de Rham cohomology rings
and encode certain genus zero Gromov-Witten invariants of the target manifold X. In
our equivariant (or gauged) case, the quantum rings will be deformations of the classical
equivariant cohomology rings and will presumably encode certain genus zero Hamilto-
nian Gromov-Witten invariants of X. The latter invariants study symplectic manifolds
equipped with hamiltonian actions and have been rigorously defined and studied in the
mathematical literature [4, 5]. Loosely speaking, they are given by integrals of natural
cohomology classes over the moduli space of solutions of the vortex equations with target
X. Their ring structure, however, does not seem to have been considered so far. The
Hamiltonian Gromov-Witten invariants can be interpreted in the language of quantum
field theory as expectation values of observables in gauged non-linear sigma-models, in a
theory very much analogous to the usual sigma-models/Gromov-Witten one [2]. The BPS
states are then the classical vortex solutions, and the quantum equivariant cohomology
rings are identified with the rings of local observables of the gauged topological theory.

    Another version of equivariant Gromov-Witten theory has been described by Givental
in [7]. That is a different construction from the one we are considering here. In partic-
ular the invariants in [7] are defined by equivariant integration over the moduli space of

                                                        1
holomorphic curves, and so the vortex moduli spaces do not enter the picture. Recently,
however, it has been proposed in [9] that Givental's equivariant invariants are related to
the weak coupling limit of the Hamiltonian (or gauged) Gromov-Witten theory, i.e. to the
limit e2  0 of the gauged sigma-model. How this limit works precisely doesn't seem to
be completely clear yet. Recall that, on the other extreme, the limit e2   has already
been studied for quite some time [6, 10]: it leads to a relation between the Hamiltonian
Gromov-Witten invariants of X and the usual Gromov-Witten invariants of the Ka�hler
quotient of X by the gauge group.

    Coming back to our study, the main result of this note is roughly the following. Let X
be a k-dimensional toric manifold obtained as the Ka�hler quotient of Cn by a linear action
of the torus T n-k with charges Qaj , where the indices run as 1  j  n and 1  a  n - k.
We assume that X is Fano, i.e. that it has positive definite first Chern class. Then for
any of the natural T k-actions on X, the quantum equivariant cohomology ring of this
manifold is the polynomial ring

QHT (X) = C[w1, . . . , wn] / Q(X) ,                           (1)

where Q(X) is the ideal generated by the binomials

(wj )Qaj - e-ta                                     (wj )-Qja  (2)

{j:Qaj 0}        {j:Qaj <0}

for all a = 1, . . . , n - k. Recall that the usual (non-equivariant) quantum cohomology
rings of toric manifolds have been rigorously computed [3, 8, 5], and are

QH(X) = C[w1, . . . , wn] / (I + Q(X)) ,

where I is a certain ideal of linear relations. Thus the result presented here shows a clear
analogy with the classical case, where the cohomology rings of toric manifolds are

    H(X) = C[w1, . . . , wn] / (I + J) and HT (X) = C[w1, . . . , wn] / J , (3)
with J being the classical Stanley-Reisner ideal [3, 13].

    Three questions that arise directly from the work in this note are the following. Firstly,
to check the prediction of mirror symmetry by computing the quantum equivariant ring
directly on the sigma-model side. This would presumably involve computing a few genus

                                                        2
zero Hamiltonian Gromov-Witten invariants of X. For toric X we note that quite a
few methods and results are already available [5, 1, 12]. The second question is to go
on to see whether mirror symmetry can be used to predict the Hamiltonian Gromov-
Witten themselves, not just the resulting quantum ring. This will involve computing the
correlation functions in the dual Landau-Ginzburg model and then mapping them to the
invariants of the gauged sigma-model. Finally, the third question would be to generalize
our computations to gauged non-abelian models with Grassmannian targets. The best
shot here is probably to use the non-abelian mirror conjecture of [11].

    The outline of the note is as follows. In section 2 we describe with more care the toric
manifolds and actions that will be considered here. In section 3 we use the results of [11]
to derive the Landau-Ginzburg model that is dual to the gauged sigma-model with target
X. In section 4 we look at the associated gauged topological theory to recognize the
observables and the role of the gauge fields. In section 5 we finally compute the quantum
equivariant cohomology ring, illustrating the result with the example of projective spaces.

2 Toric manifolds and actions

Let X be any k-dimensional Ka�hler toric manifold that can be realized as the Ka�hler
quotient of Cn by a linear action of a torus T n-k. We will denote by Qja the integral
weights, or charges, of this torus action, where the indices run as 1  j  n and 1  a 
n - k. Then X is the space of T n-k-orbits in a subset of Cn defined by equations of the

form

      �(z) :=     Qja |zj |2 = ra ,  z  Cn .  (4)

               j

Observe that the quotient space X(r) := �-1(r)/T n-k depends on the chosen value of
the parameter r  Rn-k, and only for a certain range of r will X(r) be isomorphic to

the initial X as a complex manifold. This range can be shown to be a convex cone in
the parameter space Rn-k, and is called the Ka�hler cone of X. For r outside the Ka�hler
cone the quotient X(r) can be very different from X, and can in particular be singular
or have smaller dimension. In general the parameter space Rn-k will be subdivided into

a number of non-intersecting cones of different dimensions, each cone corresponding to
an isomorphism class of quotients. Varying r inside each of these cones will only affect
the Ka�hler metric induced on the quotient X(r), not the complex manifold itself. It can

                  3
then be shown that for such a variation the Ka�hler class of the induced metric depends
linearly on r. More precisely, for r inside the Ka�hler cone of X there exists a basis {a}
of the cohomology H2(X; Z) such that the Ka�hler form X(r) can be written as

X(r) =               raa .

           a

This shows how, inside each cone, the ra's are effectively a parametrization of the Ka�hler
class.

    Another standard fact in toric geometry is that there exists a set of primitive vectors
v1, . . . , vn  Zk that span Zk and satisfy the condition

   Qaj vj = 0                 (5)

j

for all values of a. In the algebraic picture of toric manifolds these v's are generators
of the regular fan associated to X. In fact, given the v's corresponding to X, we can
take the Qa's to be a basis of the (n - k)-dimensional lattice that solves (5). As can be
easily checked, after a redefinition of the ra's if necessary, these new Q's define the same
quotient X as the old ones. The linear transformation that takes the new Q's to the
old ones is invertible over the reals but in general not over the integers. These vectors
v1, . . . , vn  Zk that generate the fan encode much of the information about X. For
example the ideal I that appears in the (non-equivariant) cohomology ring of X is simply
defined by the linear relations

 n                   t  Rk .

     vi, t wi = 0 ,

i=1

    In this paper we will be considering abelian gauged sigma-models with X as target
manifold. Since the models are gauged, to define them we need an abelian action on X.
This action can be constructed through any abelian action on Cn that commutes with the
T n-k-action used in the definition of X, and so descends to X. For definiteness we will
take the T k-action on X induced by the linear action of this group on Cn with integral
weights ubj, where the indices run as 1  j  n and 1  b  k. Taking the u's such that
the vectors u1, . . . , uk  Zn complete the set of Qa's to form a basis of Rn, we get at the
end a hamiltonian T k-action on X that operates through holomorphic transformations
and whose generic orbits have real dimension k.

        4
Gauged sigma-models are theories of maps  from a Riemann surface to the target

manifold X coupled to gauge fields A. These gauge fields should be regarded as con-

nections on a principal bundle over the Riemann surface, or worldsheet. If the classical

models admit a supersymmetric extension, then in addition to  and A there will be sev-

eral other bosonic and fermionic fields. The case that concerns us are the N = 2 gauged,
supersymmetric and abelian sigma-models with target Cn or the toric manifold X. In this

case both the lagrangian and the several other fields of the theory can be conveniently
rewritten in term of superfields using the Grassmann variables � and ��. Following the

conventions of [11] we will need the chiral fields


                  = (w�) + 2  (w�) + 2 +- F (w�)                                              (6)

and the twisted chiral fields

Y  =  y(w~�)  +  i22++��++((w~w~��))+-i2 2�-�--(-w~(w�~)�+) +2  +�- G(w~�)                    (7)
   =  (w~�)   +                                                 2 +�- [D -
                                                                            i(FA)01](w~�)  ,

where one should expand the various fields as functions of the variables w� = x� - i���
and w~� = x�  i���, with x� = x0 � x1 being the light-cone coordinates on the
Minkowski worldsheet. The last superfield, the superfield , is not a fundamental field;
it is instead the superfield-strength of the vector multiplet V associated to the abelian
connection A, written in the Wess-Zumino gauge. In terms of these superfields the various
supersymmetric lagrangians that we will use can all be written in a more compact and
convenient form.

3 The dual gauged lagrangian

Recall that the stated purpose of this note is to use mirror symmetry to study some
basic properties of the gauged sigma-model with toric target X and group T k. Our first
task is therefore to write down the lagrangian of this model and, more importantly, the
lagrangian of the mirror theory. This task is in fact quite simple given the results of [11].
One starts by considering the theory before the quotients, i.e. the gauged sigma-model

                                 5
with target Cn and group T k � T n-k. Its lagrangian is

                      n                                                      1   k
                                                                            2e2
L=             d4          � j  exp (2 Qja Va) + exp (2 ujb Vb)    j  -               � b b  (8)

                      j=1                                                        b=1

                 1    n-k                      1
               2(e)2                           2
            -              � a a  -               d2~ ta a + tb b + c.c. ,

                      a=1

where e and e are the gauge coupling constants corresponding to the two tori of the

gauge theory, while t and t are the usual complex parameters of gauged sigma-models,

i.e. the complex combination r - i of the Fayet-Iliopoulos parameter and the theta

angle. For those less familiar with the jargon, the terms in the first and second integrals

are respectively called the D-terms and the F-terms of the lagrangian. Now, according

to Hori and Vafa, the mirror of this theory is another gauged sigma-model with twisted

chiral fields Y 1, . . . , Y n and lagrangian

                                                   1      k                1 n-k
                                                  2e2                    2(e)2
Ldual =     d4     kinetic term (Y j, Y� j)    -             � b b    -               � a a

                                                        b=1                      a=1

            1                                                            n
            2
         +      d2~ a Qaj Y j - ta + b ubjY j - tb +                          exp (-Y j) + c.c. .

                                                                         j=1

In the derivation of [11] the first two F-terms of Ldual come from the application of T-
duality to L, whereas the exponential F-term is a non-perturbative contribution from
instantons. A very important property of Ldual is that at a D-term level the matter and
gauge fields become uncoupled; furthermore, in Ldual the gauge fields appear only through
the gauge field strengths , with no explicit mention of the vector multiplet V .

    The point now is to go to the limit e   on both theories, the original and the
dual. For the original L it is well known that this limit takes us to the sigma-model with
quotient target Cn//T n-k = X [10]. It is here that the Fano assumption on X enters,
as is also explained in [10]. The resulting quotient model is still gauged, with group T k,
because we have kept the constant e finite. On the dual side, on the other hand, the limit
e   just imposes the constraints

                      Qaj Y j - ta = 0 for all a = 1, . . . , n - k.

As in [11], these constraints are solved by

                                                     k

                                  Y j = sj +              vbj b ,                            (9)

                                                     b=1

                                                  6
where the 1, . . . , k are new twisted chiral fields associated to new complex coordinates,
and the constants s1, . . . , sn  C are any particular solution of the algebraic equation
Qaj sj = ta. Finally, inserting (9) into the limit of Ldual and denoting by �, � the canonical
inner product on Rk, we get that as e   the lagrangian Ldual reduces to

L^dual =     d4  kinetic term (b, � b) -   1   � ,                                   (10)
                                          2e2                                     + c.c. .
                                                                  n
          +  1   d2~  , uj  vj,  + sj -                              - vj,  - sj
             2                                 , t + exp

                                                                j=1

This lagrangian is expected to be dual to the e   limit of L, i.e. dual to the lagrangian
of the gauged sigma-model with target X and group T k. The superpotential of this dual
Landau-Ginzburg theory is thus

                                               n

          W = , uj vj,  + sj - , t + exp - vj,  - sj .                            (11)

                                               j=1

We stress that these calculations are basically the same as in [11], the only difference being
that here we have kept the gauge terms in the quotient theory. In [11] all the gauge terms
were gotten rid of, because there one is only interested in the non-gauged sigma-model
with target X.

4 Observables of the dual topological theory

Our work up to this point has been to identify the Landau-Ginzburg theory dual to the
original gauged sigma-model with target X and group T k. We concluded that the dual
theory has lagrangian (10) and superpotential (11). We can now start to use this dual to
extract properties of the gauged sigma-model.

    The main object that concerns us in this note is the (small) quantum equivariant
cohomology ring of the target X. As is well known in the non-equivariant case, this
ring coincides with, or can be defined as, the ring of local observables of the A-twisted
topological sigma-model with target X. This topological theory is obtained by twisting
the original supersymmetric theory along its vectorial R-symmetry. Now the vectorial
R-symmetry is also a symmetry of the dual model, the gauged Landau-Ginzburg model,
and in particular one can also twist the latter model to obtain a topological theory,
which is then expected to be the dual of the gauged A-theory on X. The ring of local

                                                        7
observables of that topological Landau-Ginzburg model will then coincide with the ring of
local observables of the A-twisted gauged sigma-model, i.e. with the quantum equivariant
cohomology ring of X. Thus, given this rationale, we at present have the two following
tasks: firstly to twist the dual theory (10) along its vectorial R-symmetry, and, secondly,
to compute the ring of observables of the resulting topological theory.

    The whole of this recipe is very familiar from the non-gauged case. In that case the
final result is that the ring of local observables, or chiral ring, is a ring of polynomials
quotiented by the ideal generated by the first partial derivatives of the superpotential W .
Here in the gauged case, however, we must pay a little extra attention to the gauge fields.
In fact, although the twisted chiral field strengths  appear in the superpotential (11) side
by side with the twisted chiral matter fields , they are not exactly in the same footing
as the latter. As we will see, at the end it turns out that the 's do contribute to the ring
of polynomials that corresponds to the observables but, on the other hand, they do not
contribute to the ideal by which one should mod-out, i.e. the partial derivatives of W in
the directions of the 's do not appear in the result. The reason is that the observables
determined by these partial derivatives are not trivial in the topological theory, and so
cannot be moded-out. In contrast, the derivatives of W with respect to the matter
fields are still trivial (or Q-exact) observables, and hence as usual must be moded-out.
This difference is explicitly revealed in the expressions for the action of the topological
Q-operator obtained below in (13).

    So we now want to determine the observables of the topological theory derived from
the Landau-Ginzburg model (10). This model has the general form

L^ =  d4  K(Y, Y� ) -   1   � ,   +  1  d2~ W (, Y ) + c.c. ,  (12)
                       2e2           2

where the 's and Y 's are the twisted chiral superfields of expressions (7). As usual, after
twisting, the space of fields of the topological theory will be acted by a natural fermionic
operator, Q, and the observables of the theory will be the corresponding Q-cohomology
classes. At the end of the section, after writing down the explicit form of Q, we will
conclude that the local observables of the topological theory are the holomorphic functions
f (b, yj) modulo the ideal generated by the Q-exact functions yj W . As mentioned before,
the derivatives bW do not appear. This is, in fact, all that we will subsequently need,
so the reader may wish at this point to just note the result and smoothly fly over to the
next section. If not, then here is a brief justification. Starting with the lagrangian (12)

                            8
and superfields (7), the first task is to twist the theory along the vectorial R-symmetry.
This symmetry is defined by

                                        Y - Y (e-i�, ei��)
                                         - (e-i�, ei��) ,

and in components reads                               �+ - e-i�+
                                �+ - e-i�+           - - ei- ,
                                - - ei-

with all the other fields remaining invariant. Applying the usual rules for twisting a theory

along an R-symmetry [14, 10], we can reinterpret the various component fields as sections

of different bundles and subsequently combine them into a new set of fields, the fields of the

topological theory. These new fields will all be scalars or one-forms on the worldsheet with

values either on the Lie algebra or on the pull-back bundle yT X. The lagrangian of the

topological theory is then obtained by writing down (12) in components and substituting

in the new set of fields. Now, because the fields involved are many and we do not really

need the explicit topological lagrangian for our purposes, we will skip writing it down here.

Instead we proceed directly to compute the form of the topological operator Q, which is

the only knowledge required to identify the ring of local observables. As usual, the action

of Q on the different fields can be read out of the N = 2 supersymmetry transformations.

These are written down for instance in [11] for the gauge fields and in [10] for the matter

fields of the twisted chiral multiplet. Since the definition of the topological operator is
Q = Q- + Q�+, to obtain the explicit Q-action over the fields one only needs to put the

fermionic parameters + = �- = 1 and - = �+ = 0 in these transformations (see the
conventions of [11]). After integrating out the auxiliary fields Da and Gj and rotating to

euclidean worldsheet (because topological theories are euclidean), this yields the result:

Q Aaz = -i-a           Q -a                       =  -2     2 za                              (13)
Q Aza� = i�+a          Q �a+                      =   
                                                     2 2 z�a

Q a = 0                Q                    (�-a  +  +a ) = 0      2i[FAa     e2Re
Q �a = -i2(�-a + +a )  Q                    (�-a  -  a+)  =  -2            +        (a W  )]
Q yj = 0               Q                    -j    =       
Q y�j = 2(j+ - �j-)    Q                    �j+   =  -2i    2 zyj
Q (j+ - �j-) = 0                                       
                                                     2i 2 z�yj

                       Q [2 2 hj�l(+l + �-l )] = - yj W .

                                                  9
Here z is the complex coordinate on the euclidean worldsheet and hj�l = -j�lK is the
hermitian metric on the geometry T k-dual to X. It is apparent from these expressions
that the only natural Q-closed operators that may not be Q-exact are the holomorphic
combinations of the fields y and . Furthermore, one such holomorphic combination will
be Q-exact if and only if it has any of the derivatives yj W as a factor. Observe also
that the partial derivatives bW appear in (13) only through their real part, which is
not holomorphic and therefore not even Q-closed.

5 The chiral ring of the gauged models

Applying the results of the previous section to the lagrangian (10), we see that the local
observables of the dual topological theory are the holomorphic functions f (b, b) modulo
the ideal of functions generated by the partial derivatives bW . Now, in analogy to
what is done in the non-gauged case, instead of considering all the holomorphic functions
in the definition of chiral ring, we restrict ourselves to finite degree polynomials in the
variables b and (xb)�1 := exp (b). This is related to the fact that in the definition of
the equivariant de Rham complex we only consider finite degree forms and polynomials
in the Lie algebra. Then the chiral ring of the dual theory is

               C[1, . . . , k, (x1)�1, . . . , (xk)�1] / D(W ) ,              (14)

where D(W ) is the ideal generated by the derivatives

                                 n                                     k

               b W = -xb xb W =       ubj  , vj        - e-sj (xc)vcj .       (15)

                                 j=1                                 c=1

This result can be cast in a different and perhaps simpler form. Consider the ring homo-
morphism

 : C[1, . . . , k, w1, . . . , wn] - C[1, . . . , k, (x1)�1, . . . , (xk)�1]  (16)

determined by

                                                       k

               b - c vcj ubj     and       wj - e-sj        (xc)vcj .         (17)

                                                       c=1

It is not difficult to recognize that the matrix Bcb := ujbvcj is invertible over R. Basically
this follows from the fact that both {Qa, ub} and {Qa, vb} are basis of Rn. It is then clear

                                      10
that, restricted to the subring of polynomials in the 's, the map  is an isomorphism to
its image, which is exactly the same subring. Furthermore, because of the assumption that
the vectors v1, . . . , vn span the full Zk, it is also clear that the image by  of the subring
C[w1, . . . , wn] is the full subring of Laurent polynomials C[(x1)�1, . . . , (xk)�1]. Hence, we
conclude,  is surjective. (Observe in passing that this was the first step that required
the stated property of set of v's, a property which comes from the regularity of the fan
corresponding to X; in particular the derivation of (14) did not require the regularity
assumption on X.)

    Now, by construction, the ideal D(W ) of (15) is the image by  of the ideal D~ in the
domain generated by the polynomials

b - ubj wj  for b = 1, . . . , k .

Furthermore, just as in [3], it is apparent that the kernel of  is the ideal Q(X) generated
by the binomials (2) described in the introduction. Hence we finally conclude that, up to
isomorphism of rings,

QHT (X) = C[1, . . . , k, w1, . . . , wn] / (D~ + Q(X))  (18)

= C[w1, . . . , wn] / Q(X) .

    Having arrived at this result, a number of conclusions can be drawn in analogy with the
non-equivariant case. Firstly observe that, through the definition (2) of the ideal Q(X),
the chiral ring seems to depend on the complex parameter t = r - i in Cn-k. It is
easy to recognize, however, that this dependence is only apparent, and that by redefining
the variables wj one can absorb any finite variation of t. This means that the chiral
ring of our gauged sigma-model does not depend on the value of t, at least as long as the
assumption that the target X(r) is a smooth Fano manifold of dimension k remains valid.
This is analogous to the non-gauged case [3, 13], and leads to the conclusion that toric
targets that are isomorphic in codimension 1 have the same quantum equivariant ring.
The usual example here is toric targets related by flop-type birational transformations,
for in this case they can be realized as quotients X(r) with the same charges Qja and
parameters r belonging to adjacent cones in the parameter space Rn-k.

    Another conclusion follows from the result in [3] that says that if t belongs to the
Ka�hler cone of X and  is a real scalar, then the formal limit   + of the relations
(2) that define the ideal Qt(X) is actually the set of relations that define the classical
Stanley-Reisner ideal J(X). Comparing (1) and (3) this shows that, as expected, the clas-
sical equivariant cohomology ring of X can be obtained as a formal limit of the quantum

            11
equivariant cohomology ring. This formal limit, however, depends on the choice of the
cone in Cn-k to which t belongs. This corresponds to the fact that the classical equiv-
ariant ring of the quotient X(r) also depends on the cone, in contrast with the quantum
equivariant ring.

    We thus conclude that much of the story of mirror symmetry and quantum cohomology
of toric manifolds extends to the equivariant case.

Example: projective spaces. The compact toric manifolds X = CPk correspond to
the assignments n = k + 1 and Q = (1, . . . , 1)  Zk+1 in the general picture above. The
result (18) then states that the quantum equivariant cohomology ring of these manifolds
is the polynomial ring

                      QHTk (CPk) = C[w1, . . . , wk+1]/(w1 � � � wk+1 - e-t ) .

The parameter space is here one-dimensional, and in the limit t  + this ring formally
reduces to the classical T k-equivariant cohomology of CPk, which is

                            HTk (CPk) = C[w1, . . . , wk+1]/(w1 � � � wk+1) .

To put this in context, recall that the usual (non-equivariant) cohomology rings of CPk
are

QH(CPk) = C[w]/(wk+1 - e-t)  and  H(CPk) = C[w]/(wk+1) .

Acknowledgements. I would like to thank Marcos Marin~o and Jan de Boer for help-
ful conversations and the referee for suggesting several improvements. I am partially
supported by the Netherlands Organisation for Scientific Research (NWO), Veni grant
639.031.616.

References

 [1] J. Baptista : `Vortex equations in abelian gauged sigma-models'; Commun. Math.
      Phys. 261 (2006), 161�194.

                                                       12
 [2] J. Baptista : `A topological gauged sigma-model'; Adv. Theor. Math. Phys. 9 (2005),
      1007�1047.
      J. Baptista : `Twisting gauged non-linear sigma-models '; JHEP 0802 (2008) 096.
      R. Zucchini : `Gauging the Poisson sigma model'; JHEP 0805 (2008) 018.

 [3] V. Batyrev : `Quantum cohomology rings of toric manifolds'; Ast�erisque 218 (1993),
      9�34.

 [4] K. Cieliebak, R. Gaio, I. Mundet i Riera and D. Salamon : `The symplectic vor-
      tex equations and invariants of Hamiltonian group actions'; J. Symplectic Geom. 1
      (2002), 543�645.
      I. Mundet i Riera and G. Tian : `A compactification of the moduli space of twisted
      holomorphic maps'; arXiv: math/0404407 [math.SG].

 [5] K. Cieliebak and D. Salamon : `Wall crossing for symplectic vortices and quantum
      cohomology'; Math. Ann. 335 (2006), 133�192.

 [6] R. Gaio and D. Salamon : `Gromov-Witten invariants of symplectic quotients and
      adiabatic limits'; J. Symplectic Geom. 3 (2005), 55�159.

 [7] A. Givental : `Equivariant Gromov-Witten invariants'; Internat. Math. Res. Notices
      (1996), 613�663.
      T. Coates and A. Givental : `Quantum Riemann-Roch, Lefschetz and Serre'; Ann.
      of Math. (2) 165 (2007), 15�53.

 [8] A. Givental : `A mirror theorem for toric complete intersections'; Progr. Math. 160,
      141�175, Birkh�auser Boston, Boston, 1998.

 [9] E. Gonzalez and C. Woodward : `Area dependence in gauged Gromov-Witten theory';
      arXiv: math/0811.3358.

[10] K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil and
      E. Zaslow : `Mirror symmetry'; Amer. Math. Soc., Providence; Clay Mathematics
      Institute, Cambridge, 2003.

[11] K. Hori and C. Vafa : `Mirror symmetry'; arXiv: hep-th/0002222.
[12] I. Melnikov and M. Plesser : `A-model correlators from the Coulomb branch'; arXiv:

      hep-th/0507187.
[13] D. Morrison and M. Plesser : `Summing the instantons: quantum cohomology and

      mirror symmetry in toric varieties'; Nucl. Phys. B 440 (1995), 279�354.
[14] E. Witten : `Topological sigma models'; Comm. Math. Phys. 118 (1988), 411�449.

                                                       13
