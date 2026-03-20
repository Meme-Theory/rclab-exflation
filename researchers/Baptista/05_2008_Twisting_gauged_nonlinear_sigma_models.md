# 2008 Twisting gauged nonlinear sigma models

**Source:** `05_2008_Twisting_gauged_nonlinear_sigma_models.pdf`

---

arXiv:0707.2786v2 [hep-th] 26 Mar 2008                                                                                                   ITFA-2007-31

                                          Twisting gauged non-linear sigma-models

                                                                             J. M. Baptista 

                                                                           Institute for Theoretical Physics 
                                                                                 University of Amsterdam

                                                                                 July 2007

                                                                                 Abstract

                                            We consider gauged sigma-models from a Riemann surface into a Ka�hler and hamilto-
                                        nian G-manifold X. The supersymmetric N = 2 theory can always be twisted to produce
                                        a gauged A-model. This model localizes to the moduli space of solutions of the vortex
                                        equations and computes the Hamiltonian Gromov-Witten invariants. When the target
                                        is equivariantly Calabi-Yau, i.e. when its first G-equivariant Chern class vanishes, the
                                        supersymmetric theory can also be twisted into a gauged B-model. This model localizes
                                        to the Ka�hler quotient X//G.

                                            e-mail address: [email redacted]
                                            address: Valckenierstraat 65, 1018 XE Amsterdam, The Netherlands
Contents

1 Introduction                                   1

2 The gauged N = 2 supersymmetric theory         6

2.1 Fields, lagrangian and supersymmetries . . . . . . . . . . . . . . . . . . . . 6

2.2 R-symmetries, anomalies and equivariant Calabi-Yau's . . . . . . . . . . . 9

2.3 Twisting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

3 The gauged A-twist                             17

3.1 Fields, action and the QA-operator . . . . . . . . . . . . . . . . . . . . . . 17

3.2 Observables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

3.3 Localization and moduli space . . . . . . . . . . . . . . . . . . . . . . . . . 21

4 The gauged B-twist and Landau-Ginzburg models  22

4.1 Fields, action and the QB-operator . . . . . . . . . . . . . . . . . . . . . . 22

4.2 Localization, moduli spaces and observables . . . . . . . . . . . . . . . . . 24

A Notation and conventions                       29

1 Introduction

Topological field theories are a major tool to explore complex and symplectic geometry.
The earliest and most well-known examples of their usefulness, dating from almost twenty
years ago, were applications of topological sigma-models and mirror symmetry to predict
Gromov-Witten invariants of Calabi-Yau manifolds. Since then the subject has devel-
oped in several directions: in depth and rigour, with the invention of new computational
techniques for GW-invariants and mathematical frameworks for mirror symmetry; and in
breadth and diversity, with the discovery of new invariants and dualities through the use
of topological strings and other TFT's.

    One such recent development, so far still relatively unexplored, was the definition in
the mathematical literature of the Hamiltonian Gromov-Witten invariants [10]. These
invariants study Ka�hler manifolds equipped with hamiltonian actions of compact Lie
groups. To define them one uses the moduli space of solutions of the vortex equations.
In the special case of a trivial group the vortex equations reduce to the equations for

                            1
holomorphic curves, and hence in this instance the HGW-invariants reduce to the GW-
invariants. Thus these new invariants were introduced as a generalization of the GW-
invariants designed to study hamiltonian actions on symplectic manifolds; moreover, they
also bear natural relations with the original GW-invariants [14] (see also below).

    From a physics point of view, the HGW-invariants clearly must come from supersym-
metric and topological gauged non-linear sigma-models. As far as the author is aware,
however, there is not much literature on this subject. A first motivation for this paper is
thus to provide a framework to study the HGW-invariants within topological field theory.
This is done by considering the N = 2 gauged non-linear sigma-model and, through the
usual procedure, twist it to obtain topological gauged A and B models. Since in the
non-gauged case the physical approach, as mentioned above, has been very successful in
giving predictions and insights into Gromov-Witten theory, we are curious to know how
much of this extends to the gauged theories.

    A second motivation for this study comes from the fact that, even if one is not in-
terested in the HGW-invariants for themselves, the gauged sigma-model with target X
can be used as a tool to investigate the non-gauged model with target X//G. This fact
was first recognized in the celebrated paper [31], where the gauged linear sigma-model
with target X = Cn and group G = U(1) was used to study non-gauged sigma-models
into weighted projective spaces and their Calabi-Yau hypersurfaces. This approach shed
new light on the Calabi-Yau/Landau-Ginzburg correspondence and, at the same time,
proved useful as a tool to compute the GW-invariants of toric Calabi-Yau's (e.g. [25, 19]).
Another application of gauged linear sigma-models was given in [32], where this time the
target X = Ckn and group G = U(k) were used to study the quantum cohomology of
Grassmannians. More recently, in [20], the phase structure and dynamics of these non-
abelian linear models have been further analysed. Thus a natural question in the subject,
and our second motivation, is to ask how much of this can be extended to non-linear
targets X, other quotients X//G and other Calabi-Yau's. In the mathematical literature
these matters have received some investigation in [14], but to the author's knowledge they
have not been addressed on the physics side.

    Our purpose in this paper is to give an impulse to these investigations by describing
in detail the supersymmetric N = 2 gauged non-linear sigma-model, the gauged A and B
models, their observables and localization moduli spaces.

    We now give a rather detailed description of the contents of the paper. We deal with

                                                        2
gauged sigma-models, in other words theories that couple matter and gauge fields. Matter

fields are represented by maps  :   X from a Riemann surface into a Ka�hler target.

Gauge fields are represented by a G-connection A over the Riemann surface. In order to

couple these two fields one also assumes that the gauge group G acts on the target X

in a holomorphic and hamiltonian way. The most important part of the action of these

models is then

                I(A, ) = |FA|2 + |dA|2 + |�  |2 + � � � ,                      (1)


where FA is the curvature of A, dA is a covariant derivative and � : X  Lie G is the

moment map of the G-action. This action reduces to the classical action of sigma-models

if we take G to be trivial. Now, the usual sigma-models have N = 2 supersymmetric ex-

tensions for Ka�hler target X. It is then a fact that, when X has a group G of hamiltoniam

isometries, the N = 2 theory can be gauged while preserving the supersymmetry, i.e. (1)

has a N = 2 supersymmetric extension. Similarly, the topological theories that will be

described here -- the gauged A and B models -- are both extensions of (1) obtained by

considering extra fields and adding more terms to the action. In fact there are basically

two standard ways of constructing this kind of topological theories: one is by twisting the

supersymmetric theory mentioned before; the second is through the use of the Mathai-

Quillen formalism. The latter has a more geometric flavour and was already applied in

[3] to the gauged A-model. Twisting the supersymmetric theory, on the other hand, not

only is more familiar a method to the physicists, but also has the advantage that, in the

non-gauged case, produces two distinct and equally important topological theories: the

A and B models. This does not happen with the Mathai-Quillen formalism, which only

yields the A-theory. Since in this paper our main aim is to extend both models to the

gauged case, we will proceed through the twist. We wish to stress that all these twisting

constructions are very standard in the non-gauged case, and thus, since things are quite

similar here, we present most of the results without detailed calculations. We took some

trouble, nevertheless, in trying to present consistent and detailed formulas.

    In section 2 we spell out the fields, action and supersymmetry transformations of the
N = 2 gauged non-linear sigma-model in two dimensions. These are obtained by dimen-
sional reduction of the N = 1 gauged non-linear sigma-model in four dimensions [13].
This supersymmetric N = 2 model, like its non-gauged counterpart, possesses two classi-
cal U(1)-symmetries. Standard index theorems are then applied to show that one of them,
the vectorial R-symmetry, is always non-anomalous, whereas the other one, the axial R-

                                                        3
symmetry, is in general anomalous. Sometimes, however, the axial anomaly also vanishes,
and a sufficient condition for this to happen is that c1G(T X), the first G-equivariant Chern
class of X, vanishes. Targets X with this property are called equivariant Calabi-Yau's;
they may also be characterized by the fact that they possess a G-invariant and nowhere-
vanishing (n, 0)-form, where n is the complex dimension of X. Now, since the twists of
the supersymmetric theory are performed along the non-anomalous R-symmetries, man-
ifolds with cG1 (T X) = 0 are very special, for they support two distinct twisted theories,
the gauged A and B models. A general Ka�hler target, on the other hand, only supports
the gauged A-model. A pleasant property of equivariant Calabi-Yau's, we find, is that
their Ka�hler quotient X//G is also Calabi-Yau. Three simple examples of equivariant
Calabi-Yau's are presented at the end of section 2.2. The first is complex vector spaces
with special unitary representations of G. The second is when X is the total space of a
sum of line-bundles over a complex base, X = kLk  M, with the circle U(1) acting
on each line-bundle with charge qk, and with the two algebraic conditions k qk = 0
and c1(T M) + k c1(Lk) = 0 satisfied. The third example is hyperka�hler manifolds with
compatible G-actions, and we give a short list of famous spaces of this sort at the end of
2.2.

    While all of these are well known examples of Calabi-Yau's, it is not obvious to the
author whether all of them, or their quotients, can be studied within the framework of
the gauged linear models, i.e. as hypersurfaces or complete intersections in toric varieties
or Grassmanians. If this is not the case, then there may be some scope for these models
as tools to investigate Calabi-Yau's; the hope is that, just as in the linear case, some
aspects of the theories may be easier to study in their gauged (or unquotiented) version
than in the ungauged version on the quotient space. At least aspects related to the phase
structure of the theory and, more ambitiously, to mirror symmetry, seem to fit well with
gauged theories [31, 19]. Another point of view would be to be less concerned about
the quotients and just decide to study hamiltonian actions on symplectic manifolds, in
which case the framework of non-linear gauged sigma-models and HGW-invariants is the
appropriate one.

    In section 3 we turn to the topological theories, starting with the gauged A-model.
The fields, action and QA-operator are written down in the explicit formulas derived from
the supersymmetric theory. These formulas had already been obtained in [3] through
the Mathai-Quillen formalism. (The material in this section, in fact, is almost entirely

                                                        4
contained either in [3] or in [29], and so the section can be regarded as a review, or
at most a check that the supersymmetric twist agrees with the Mathai-Quillen result.)
Concerning the observables of the theory, recall that in the non-gauged A-model they are
constructed using de Rham cohomology classes of the target X; in the gauged A-model,
not surprisingly, they are constructed via the G-equivariant cohomology of X. In the
non-gauged theory, moreover, the path-integrals that compute the expectation values of
the observables get localized to integrals over the finite-dimensional space of holomorphic
curves; in the gauged A-model, on the other hand, the localization is to the moduli space
of solutions of the general vortex equations. These expectation values are then closely
related to the Hamiltonian Gromov-Witten invariants of X [3, 10], a type of invariants
that studies vortex moduli spaces and generalizes (at least part of) the usual Gromov-
Witten theory.

    Finally in section 4 we look at the B-twist of the gauged supersymmetric theory.
Since this topological theory is not accessible through the Mathai-Quillen formalism, it
was not considered in [3], and also seems not to have been much studied anywhere else.
In section 4 we spell out the fields, action and QB-transformations of this theory. In
this section we include in the theory a non-zero superpotential W (in itself just a G-
invariant and holomorphic function on X), and thus obtain a gauged Landau-Ginzburg
model. As in the non-gauged case this is possible because a non-zero W does not spoil the
axial symmetry (used, recall, to define the B-twist), whereas it usually spoils the vector
symmetry. Regarding localization, it is argued in section 4.2 that the path-integrals of the
B-theory localize to a set of field configurations that is smaller than the set of QB-fixed
points. This is related to the usual decomposition QB = Q+ + Q- and to the fact that
the B-action is simultaneously Q+- and Q--exact, up to topological terms. It is then
shown that in favourable cases, including whenever  has genus zero, this smaller set can
be identified with the Ka�hler quotient X//G, which, as said before, is Calabi-Yau. For a
non-zero superpotential W the localization set is furthermore restricted to the critical set
of W in X//G.

    Generally speaking the work in this paper extends in the natural way some classical
aspects of the non-gauged and the gauged linear sigma-models. Not addressed here are the
important quantum aspects of the theory, especially the RG-flow, the -function and the
singularities in the Fayet-Iliopoulos parameter space (here equal to the center of g). For

                                                        5
instance, naively extending [31], one would expect that  = 0 at one loop for equivariant
Calabi-Yau's and that the quantum singularities will appear for values of the FI-parameter
such that the set �-1(0) contains points with non-trivial G-stabilizer. As in [31], the
analysis of these problems is essential to investigate the existence of Calabi-Yau/Landau-
Ginzburg correspondences and mirror dualities in these gauged models. Another possible
direction is to study the coupling of these gauged sigma-models to gravity, or, maybe
better, to the complex structure of the worldsheet.

2 The gauged N = 2 supersymmetric theory

2.1 Fields, lagrangian and supersymmetries

In two dimensions, globally supersymmetric theories are defined only on flat spacetimes,
so in this section we take  to be either the complex plane, the cylinder or the torus. The
two main fields of the gauged sigma-model are a connection A on a principal G-bundle
P   and a section  :   E of the associated bundle E := P �G X. Observe that
locally E looks like the product  � X, and so locally  looks like a map   X. This
is globally true when P is the trivial G-bundle. Besides the scalar section  and the
connection A, the other fields of the supersymmetric theory are:

     0+(;     C  )             F  +0 (;  ker dE)  (2)

            gP

�  -0 (; S�   ker dE)          D  +0 (; gP )

�    -0 (;  S�        C  )

                    gP

Here, as in the rest of the paper, the notation �p (; V ) represents the space of p-forms
on  with values on the bundle V  ; the signs in subscript distinguish bosonic fields

(+) from fermionic ones (�). The bundles that appear in (2) are: the adjoint bundle
gP := P �Ad g -- where g denotes the Lie algebra of G -- and its complexification gPC ; the
spinor bundles of the Riemann surface S� = K�1/2, with K = 1,0 being the canonical
bundle of ; the bundle ker dE  E, which locally looks like  � T X   � X, and is
just the sub-bundle of T E  E defined as the kernel of the derivative of the projection
E : E  ; and finally (ker dE)  , the pull-back of ker dE by the section . Thus
in the end we have one adjoint scalar field , four fermionic fields � and �, and two
scalar auxiliary fields F and D.

                            6
    Using all these fields one can define the Lagrangian of the euclidean supersymmetric
theory as

                          LSUSY = Lmatter + Lgauge + LW + L,B ,                                        (3)

where the various components are as follows. The matter part, which upon putting A = 0

reduces to the lagrangian of the non-gauged sigma-model, is

Lmatter =|dA|2 + |ae^a|2 + |�ae^a|2 + 2 i hjk� +k (A)z+j - 2 i hjk� -k (A)z�-j

            -    2  i hjk� (l e^ja) (a-k +l + �a+k -l )      +   Ri�jk�l +i -k -j  +l
            -       hjk� (+a e^ja -k - a- e^aj +k - a+ e^ak  -j   + -a e^ka +j )

                 2

            - hjk�(F j - ijl +i -l )(F k - mk n -m +n ) .

Here {ea} denotes a basis of the Lie algebra g and e^a the vector field on X associated to

ea by the left G-action. The lagrangian Lgauge, which upon putting X = point reduces to

the pure Yang-Mills lagrangian, is

Lgauge  =  1    1  |FA|2  + |dA|2  +   1  |[,  �]|2  -  1  |D|2  + 2 e2 �a Da
           e2   2  (�+)a  zAa+ -   2i  2                2  
               2i                                                               
           +                           (�-)aAz� a- -         2i  �-a [, +]a  -    2  i  �a+[�  ,  -]a  ,

where � : X  g is a moment map of the G-action on X (for the standard definition of
� see appendix A). The superpotential term is

        LW  =  1   F k(kW ) +  1  -j +k (jkW ) +        1  F k(k�W ) +  1  +k  -j (�j k�W )       ,
               2               2                        2               2

where W , the superpotential, is a fixed, non-dynamical, G-invariant and holomorphic

function on X. Notice that if X is compact only LW = 0 is possible. Finally the theta

and B-field terms are                                 i
                                                     2
                                  L,B = i B    -           (,  FA)  ,

where B is an arbitrary, but fixed, G-invariant and closed 2-form on X1;  is a constant2

in [g, g]0, the subspace of g that annihilates commutators; and (�, �) is the natural pairing

g � g  R.

    1In fact the supersymmetric N = (2, 2) theory admits a more general H-flux term, instead of the B-
field term presented here. This is related to the fact that it also admits more general targets X, namely
(twisted) generalized Ka�hler manifolds, instead of just the K�ahler targets to which we have restricted
ourselves here. For these matters see [21] and the references therein.

    2Recall that the moment map � is also defined only up to a constant in [g, g]0, so that both these
constants can be combined into an element of the complexified space [g, g]C0 . This complex constant,
as usual, is the important parameter of the quantum theory. Note, moreover, that the inner product 
allows the identification of [g, g]0 with the centre of g.

                                               7
The supersymmetric lagrangian (3) is a N = (2, 2) lagrangian, and so is invariant (up

to total derivatives) under four independent fermionic symmetries, whose parameters are

denoted � and ��. The general supersymmetry transformations are, for the matter fields,


k = 2(+-k - -+k )                                                                                (4)

k        =  -   2(�+-k  -  �-+k )

+k = 2 2i�-(dAz� k) + 2+F k + 2i�+�ae^ak
+k       =  -2  2i-(dAz� k)   +    2�+F k - 2i+ae^ak

-k = 2 2i�+(dzAk) + 2-F k - 2i�-ae^ak
-k       =  -2  2i+(dzAk)     +    (2je^�-ka)Fk+j +) -2i2-�2ai�e^-ak (z�-k
F k      =                    Aaz
            2 2i�+(z+k +                                                    +  Aza�(j e^ka)-j )

         + 2�-a+ e^ka - 2�+a- e^ak - 2i�+�a(je^ka)-j - 2i�-a(je^ka)+j

F     k  =  2 2i+(z+k      +  Aaz (je^ka)+j )  -  2 2i-(z�-k                +  Aza�(j e^ka)-j )

         - 2-+a e^ka + 2+-a e^ak - 2i+a(je^ak)-j - 2i-�a(je^ka)+j .

The gauge fields, at the same time, transform as

Aaz = -i-�-a - i�-a-                                                                             (5)

Aaz�  =  i+�a+ + i�+a+             �+a
a     =  -2i�+     a-   -  2i-     a+
�a    =  -    2i+  �-a  -    2i�-

+a    =  22-(zA� �a)       +  +(i(FA)a12   +   [,  �]a  +  iDa)
�a+   =  2 2�-(zA� a)      +  �+(i(FA)1a2  -   [,  �]a  -  iDa)

-a    =  -22+(Az a)           +  -(-i(FA)a12   -   [,   �]a  +  iDa)
�a-   =  -2 2�+(zA�a)         +  �-(-i(FA)a12  +   [,   �]a  -  iDa)

Da =+2�+2(+zA[,+a�)--]a 2+�-(2zA�-[�a-,)�-+]2a-+(2Az ��+a+[�) ,+-2]a--(Az� �2�a--)[, +]a .

    In the lagrangian and supersymmetry transformations written above we have made
use of the covariant derivatives induced by A on the bundles E, gP and  ker dE over

                                        8
. These covariant derivatives have the local form

                        dAk = dk + Aa e^ak                                    (6)

                        Aa = da + [A, ]a

(A)k = dk + Aajje^ak + kjl(dj)l ,

where  is locally regarded as a map   X,  as a map   g,  as a (fermionic) map
  T X and A as a local 1-form on .

2.2 R-symmetries, anomalies and equivariant Calabi-Yau's

The vector and axial symmetries

The gauged supersymmetric lagrangian (3) has, as usual, more symmetries besides the
galilean, gauge and supersymmetry invariances. These are the two U(1)-symmetries called
vector and axial R-symmetries. The vector symmetry is

� - e-i�                                           F - e-2iF                  (7)
� - ei� ,

with the conjugate fields transforming in the conjugate representation and all other fields
remaining invariant. The axial symmetry is

(+, +) - e-i(+, +)                                  - e2i                     (8)
(-, -) - ei(-, -) ,

with, again, the conjugate fields transforming in the conjugate representation and all other
fields remaining invariant.

    A priori these R-symmetries are only symmetries of the classical theory. To decide
whether they are also symmetries of the quantum theory, i.e. whether they preserve
the measure of the path-integral, one should, as usual, look at the kinetic terms of the
fermions and analyse their zero-modes. In our case the relevant kinetic terms of the
supersymmetric lagrangian are

2 i hjk� +k (A)z+j - 2 i hjk� -k (A)z�-j + 2 i (�+)azAa+ - 2 i (�-)aAz� -a ,

and thus, for example,

                        #{+ zero modes} = dim ker(A)z .

                                 9
Calculating on the compact torus, Stokes' theorem also allows one to write

T2  2 i hjk� +k (A)z+j =    T2  2 i hjk� +j (A)z�+k ,

so that (A)z� is the adjoint operator of (A)z and

#{+ zero modes} = dim ker(A)z� = dim coker(A)z .

Similar calculations determine the number of zero modes of the other fermionic fields.
Now, the standard heuristic analysis of the path-integral measure says that if a fermion
field  is acted by a U(1)-symmetry with charge q(), then the functional measure D
transforms under this symmetry with a charge -q() times the number of  zero modes.
This means in our examples that

D�D�D�D� - e-iA D�D�D�D� ,

where the anomaly A is

              A = [q(-) - q(+)](index Az� ) + [q(-) - q(+)](index Az� ) .

Notice that this quantity automatically vanishes for the vector symmetry (7), as expected,
and so also in the gauged model this symmetry is non-anomalous. As for the axial
symmmetry, its anomaly depends on the index of the Cauchy-Riemann operators

(A)0,1 : 0(; gP ) - 0,1(; gP )                                              (9)

(A)0,1 : 0(;  ker dE) - 0,1(;  ker dE) .

This index is easily obtained from the Hirzebruch-Riemann-Roch theorem, and the result
for a general compact  is

index(A)0,1 = c1(gP  ) + (dimG)(1 - g)                                      (10)

index(A)0,1 = c1( ker dE  ) + (dimCX)(1 - g) .

This is the complex index of the operators. For a compact Lie group, however, the Chern
number c1(gP ) always vanishes, and since we are calculating on a torus the final result
for the axial anomaly is

A(axial) = 2 c1( ker dE  ) = 2 c1G(T X) , () .

                        10
The right-hand-side way of representing the Chern number c1( ker dE) was noted in
[10] and requires a little explanation. The quantity c1G(T X) is the first G-equivariant
Chern class of the tangent bundle T X, and thus belongs to the equivariant cohomology
space HG2 (X); the symbol () represents here the equivariant homology class in H2G(X)
obtained by push-forward by  of the fundamental class of ; finally the brackets are
just the natural bilinear pairing HG2 (X) � H2G(X)  R (for more details on equivariant
cohomology see [5, 16, 17]). The merit of this right-hand-side representation is that it

shows manifestly that a sufficient condition for the axial anomaly to vanish for all  is

that

                                    cG1 (T X) = 0 ,                              (11)

which may be called the equivariant Calabi-Yau condition.

On equivariant Calabi-Yau's

As is well known, in the usual non-equivariant case the vanishing of the first Chern class

is equivalent to the triviality of the Ricci class, or, in other words, to the triviality of

the canonical bundle. Similar results hold in the equivariant case. We will now describe

how this goes and, at the end of the section, present two simple examples of equivariant

Calabi-Yau's.

    Recall that the G-equivariant complex G� (X) of the manifold X is, in the Cartan
model, the set of G-invariant elements in the tensor product S�(g)  �(X). Here

S�(g) denotes the symmetric algebra of g and �(X) the de Rham complex of X. The

differential operator of this complex is dG = 1  d + ea  e^a, and since (dG)2 = 0 on
elements of G� (X), one can consider the equivariant cohomology HG� (X) of the complex
(see, again, [5, 16, 17] for more details). Now, according to the results of [5] and [7], the

Chern class c1G(T X) is represented in the Cartan model by the equivariant form

                 =   i  TrC(R       +  ea    e^a)     G2 (X) .                   (12)
                    2

Here R is the curvature form of the Levi-Civita connection, thus an element of

2(X; EndCT X), and e^a belongs to 0(X; EndCT X). Notice that on a common Rie-
mannian manifold these forms have values on the real endomorphism bundle EndRT X;

however, when X is Ka�hler and e^a is holomorphic Killing, one can show that they actually
are J-linear and have values on the complex anti-hermitian endomorphisms of T X. As a

representative of a characteristic class, the form  must necessarily be dG-closed, a fact

that can also be checked directly.

                                           11
    A second way of writing (12) follows from the standard fact iTrCR = , where 
denotes the Ricci form of X, and the identities

2i TrC(v^) = 4 va hjk� jk� �a = -(�, v) ,

which are valid on hamiltonian Ka�hler manifolds. One can thus write3

  =  1    -     1  ea    �a  .
     2          4

Finally, the Calabi-Yau condition (11) is equivalent to the dG-exactness of , or in other
words to the existence of a G-invariant real form   1(X) such that

                   for all v  g .
d = 

v^ = -(�, v)/2

    Another (related) characterization of the equivariant Calabi-Yau condition comes from
considering the canonical line-bundle K = n,0X  X, where n is the complex dimension
of X. This bundle inherits from X a natural G-action that preserves its natural hermitian
metric. It follows from the definitions of [5] or [7] that the G-equivariant curvature form
of K  X is

                                           -i + ea  TrC(e^a) ,

and therefore that c1G(K) = c1G(T X). In particular the Calabi-Yau condition is equivalent
to cG1 (K) = 0, and by the classification of complex G-equivariant line-bundles [26], this is
the same as demanding the equivariant triviality of K. In conclusion, X is equivariantly
Calabi-Yau if and only if there exists a nowhere-vanishing and G-invariant form  
n,0(X). This form, of course, is unique up to multiplication by nowhere-vanishing G-
invariant complex functions.

    One pleasant feature of equivariant Calabi-Yau's is their relation to Ka�hler quotients,
namely that the quotient of an equivariant Calabi-Yau is Calabi-Yau. To justify this
suppose that X is a Ka�hler manifold equipped with a hamiltonian and holomorphic G-
action such that G acts freely on �-1(0). Then the Ka�hler quotient X//G exists as a
smooth Ka�hler manifold. If in addition X is equivariantly Calabi-Yau, let   n,0(X)

    3This formula suggests that the natural analog in the hamiltonian setting of a Ricci-flat K�ahler metric
is a G-invariant Ricci-flat Ka�hler metric whose moment map is harmonic.

          12
be the G-invariant and nowhere-vanishing form described above. Then it is not difficult
to show that the form

~ := |det kab|e^1 � � � e^r  ,                           r = dim g ,

after restriction to �-1(0), descends to a nowhere-vanishing (n - r)-form on the quotient
�-1(0)/G = X//G. Using the definition of the complex structure on X//G induced by
X one can, moreover, verify that this is in fact a (n - r, 0)-form, and so X//G is Calabi-
Yau. A straightforward generalization of this argument shows also that if H is a normal
subgroup of G, then the quotient X//H is a G/H-equivariant Calabi-Yau.

Examples of equivariant Calabi-Yau's

To close this section we will give a few examples of equivariant Calabi-Yau's. For the first
one, let X be a complex vector space equipped with a hermitian product, and let r be
a unitary representation of G on X. Then dr, the associated representation of the Lie
algebra g, has values on the anti-hermitian endomorphisms of X. Now, by deformation
invariance [16, Appendix C], two dG-closed forms in G� (X) are cohomologous iff they
coincide at the origin of the vector space X. Therefore []G = 0 iff

 |origin = TrC(v^) |origin = 0 for all v  g .

But since X has no curvature, we have that   0 and that

                                    v^  =  [dr(v)]kj wk   
                                                         wj

(v^)kj = [dr(v)]kj ,

and so c1G(T X) = 0 if and only if

TrC[dr(v)] = [dr(v)]kk = 0 for all v  g .

Using the connectedness of G, this is the same as saying that r is a special-unitary
representation. In the much studied abelian linear sigma-model, which has X = Cn,
G = U (1) and r() = diag(q1, . . . , qn), the equivariant Calabi-Yau condition is thus just

   k qk = 0, as found in [31].

Our second example is a generalization of the abelian sigma-model. Let
                                      X = k Vk ---X M
                                                   13
be a sum of holomorphic vector bundles over a complex manifold M. Then, after choosing
a covariant derivative on X  M, there is a natural isomorphism between the tangent
bundle T X  X and the pull-back bundle

X (T M  X) - X .  (13)

Now let the circle U(1) act on each Vk by scalar multiplication with charge qk. This
defines a global and holomorphic action of U(1) on X. This action, of course, lifts to T X,
and under the isomorphism with (13) the lift corresponds to the sum of the trivial action
on T M and the "non-lifted" action on X. The usual properties of Chern classes, which
also hold in the equivariant case, then allow us to compute that

               cG1 (T X) = X cG1 (T M  X) = X [c1(T M ) + c1G(Vk)]

                                                                                                                 k

                          = X c1(T M ) + [c1(Vk) - e1  qk(rank Vk)/(2)] ,

                                                                            k

where e1 is the single generator of the Lie algebra u(1). Thus the manifold X with this
action is topologically an equivariant Calabi-Yau if and only if


                                      k qk(rank Vk) = 0
                                     c1(T M ) + k c1(Vk) = 0 .

Observe that when M is a Riemann surface the second equation is just the numerical
condition (2 - 2gM ) + k deg Vk = 0. This agrees with [9], where these equivariant
Calabi-Yau's were constructed for M a Riemann surface and X  M the sum of two line
bundles.

    Finally, for the third example4, let (X, g) be a 4n-dimensional hyperka�hler manifold
with complex structures I, J and K, and associated Ka�hler forms 1, 2 and 3. It is then
well known that the combination  := 2+i3 is a closed and non-degenerate 2-form on X
that is holomorphic with respect to the complex structure I [18]. In particular this implies
that the wedge product  := n is a trivialization of the canonical bundle of (X, I). Now,
if X is also equipped with a G-action that preserves the hyperka�hler structure, then it
is clear that  will be G-invariant, or in other words X will be G-equivariantly Calabi-
Yau. Moreover, if the G-action on X is tri-hamiltonian, i.e. if there exists a hyperka�hler

    4This came up in a conversation with Andriy Haydys.

                                                       14
moment map (�1, �2, �3) : X  R3  g, then by definition the action on (X, I, 1) is
hamiltonian with moment map �1. All this, of course, would certainly be expectable, as
the hyperka�hler condition is stronger than the Calabi-Yau one, and so compatibility of the
G-action with the hyperka�hler structure naturally entails compatibility with the Calabi-
Yau structure. The advantage here is that there already exists a good pool of non-trivial
examples of hyperka�hler manifolds with compatible G-actions, both in the abelian and
non-abelian cases, and so we obtain for free examples of equivariant Calabi-Yau's. We
list below a few of the most famous among these tri-hamiltonian hyperka�hler manifolds.

    (i) The well known Taub-NUT and gravitational multi-instanton spaces, as well as
the Calabi spaces T CPn, all possess hyperka�hler structures invariant under the action of
at least circles (see [15]).

    (ii) The toric hyperka�hler manifolds of [6] are all equipped with tri-hamiltonian actions
of the torus T n, where 4n is the real dimension of the manifold.

    (iii) Let G be a compact Lie group and GC its complexification. Then the cotagent
bundle T GC carries a natural hyperka�hler structure that is invariant with respect to the
G � G-action induced by the left and right translations on the group. This hyperka�hler
structure is defined through the identification of X = T GC with the space of solutions
of Nahm's equations on the closed interval [0, 1], modulo gauge transformations that are
fixed at the boundary of the interval [22].

    (iv) Assume that the compact group G is semi-simple, and let T be a maximal
subtorus. Then the quotient GC/T C also carries hyperka�hler structures that are invariant
under the natural G-action on this space. These structures are obtained by identifying
X = GC/T C with the moduli space of certain classes of instantons over R4\{0} [23].

    (v) Let (S, g) be a 3-Sasakian manifold acted by a compact connected group G of
3-Sasakian isometries. Then the cone C(S) := R+ � S with metric g� = dt2 + t2g has a
natural hyperka�hler structure which is invariant by the trivial extension to C(S) of the
G-action on S [8].

2.3 Twisting

Twisting a N = (2, 2) supersymmetric theory is a very standard procedure; see [28, 29] for
the original constructions and [30, 19] for detailed reviews in the case of non-gauged sigma-
models. Twisting is performed along the non-anomalous R-symmetries of the theory, and
so for a general Ka�hler target X there is only one twist, the A-twist, performed along the
vector R-symmetry; if X is in addition equivariantly Calabi-Yau, i.e. cG1 (T X) = 0, then

                                                       15
twisting along the axial symmetry provides a second topological theory, the B-theory.

Twisting, in practice, leads to a reinterpretation of the fields of the supersymmetric

theory such that the lagrangian makes sense on any Riemann surface , not just the flat

's of the SUSY theory; this reinterpretation is done according to precise rules and at

the end, for example, all the spinor fields are regarded either as scalars or one-forms on

 (with values on vector bundles). These precise rules are as follows. Each of the fields

in (2) is in a space of sections 0(; L  V ), where V     can be (ker dE), gP  or    C  ,  and

                                                                                  gP

L is either K�1/2 or the trivial bundle C. On the other hand, each field of (2) is acted by

the vectorial R-symmetry (7) with charge qV and by the axial symmetry (8) with charge

qA. The rules then say that, after the topological twist, the field in question should be
regarded as a section of L  V , where L = L  KqV /2 for the A-twist and L = L  KqA/2

for the B-twist. Applying this rule to all the fields of the gauged sigma-model one gets

the following nice little table, in the manner of [19],

       SUSY          A-twist B-twist

U (1)V U (1)A L                                           L     L
                                                          C     K
- -1   1     K 1/2                                              C
�- 1                                                      K    K -1
       -1 K1/2                                           K -1   C

+ -1   -1 K-1/2                                           C     C
�+ 1                                                     K -1
       1     K -1/2

F -2   0     C

F2     0     C                                           K     C                          (14)

- 1    1     K 1/2                                       K      K
�- -1                                                           C
       -1 K1/2                                           C     K -1
+ 1                                                             C
�+ -1  -1 K-1/2                                          C
                                                                K
0      1     K-1/2 K-1

       2     C                                           C

� 0    -2    C                                           C     K -1

D0     0     C                                           C     C

    In addition to the "reinterpreted" fields, each twisted theory is endowed with a
fermionic operator whose action on the fields is just a particular combination of the su-
persymmetry transformations (4) and (5). More explicitly, and following the convention
of [19], define the operators Q� and Q� by

 = +Q- - -Q+ - �+Q- + �-Q+ ,                                                              (15)

             16
where  is given by (4) and (5). Then the fermionic operator of the A-twist is defined as
QA = Q- + Q+ and the operator of the B-model as QB = Q- + Q+.

3 The gauged A-twist

3.1 Fields, action and the QA-operator

Proceeding impartially by alphabetical order, we start with the A-model. Define formally

a new set of fields by the formulae:

                                          za = -i-a              (16)
k = 2-k
k = 2+k                                   z�a = ia+    +k
a = -2 2 ia                               kz�  =    2

                                          zk� = 2 -k
 a = �a/(2 2)
                                          ca = i(-a - a+)
 a = (-a + a+)/2i
Hz�k = 4idAz� k + 2(F k - ikj +i -j )     Ca = 2(FA)a12 + 2Da .

The interpretation of the new fields as scalars or 1-forms comes, as explained before, from
table (14). These local components can be combined to define the global fields

  -0 (;  ker dE)                          , , C  +0 (; gP )
   -0,1(;  ker dE)                            , c  -0 (; gP )
H  0+,1(;  ker dE)                                1-(; gP ) .

The other "overlined" fields are then to be interpreted as the local complex conjugates of
these ones.

    The action of the fermionic operator QA = Q- + Q+ on the new fields follows from the
supersymmetry transformations (4), (5) and the definition (15) of Q- and Q+. In fact, one
simply needs to substitute the new fields (16) into the supersymmetry transformations,
put + = �- = 1 and - = �+ = 0, and finally write the result in an invariant form that

                                      17
makes sense on any Riemann surface . This procedure yields:

   QA k = k                                                                                              QA A =                          (17)
   QA k = ae^ka
                                                                                                         QA  = -A
     QA  = 
                                                                                                         QA c = C
     QA  = [, ]
    QA k = Hk - ikj ij                                                                                   QA C = [, c]
   QA H k = Ri�jlm� hk�j lmi - kjlH jl + a(je^ak)j .
                                                                                                         QA  = 0

The apparently random numerical factors in (16) were chosen such as to render these
last transformations as simple as possible. The result also agrees with [3], modulo the

notations.
    The topological action of the A-theory is also obtained by simple substitution of the

new fields into the supersymmetric lagrangian (3). The result, including the auxiliary
fields, is

   IA =       1         |FA  |2  +  |dA|2         +  2e2|�      |2   +    i     A, A                     +        1    |[,   ]|2
             2e2                                                          e2                                     2e2


             +       1   [,  ]aa       +     1    [,     c]aca  -   1     |  1  C  -     FA      -       2e2     �     |2
                    2e2                     8e2                    2e2       2
             - 81 |H - 4i�A|2 + ihjk�(ab + ba)e^ja e^kb + 2ihjk�(le^ja)alk
                                    1                                     1
             +      ihj k� ( a   +  2  ca)  e^ka  j  +   ihj k� ( a  -    2  ca)   e^aj  k           vol

             +      i   aA          a  -     1       ca  Aa       +  i  Ri�jkm� (i               j )k m
                    e2                      2e2                      8
                    i                       1                                      1
             -      e2  a[,      ]a    +    2  hjk�  j      (A)k                +  2     hj  k�  k       (A)j

             +      i  hjk�a(le^j      )l    k       +   1  hjk�  e^aj a        k  +     1       hj  k�  e^ak  a       j  .
                    8                                    2                               2

This action is QA-exact up to topological terms, just as in the non-gauged model of [29].

One can in fact check that

                                       IA = QA + [E]                                                                                     (18)


with gauge fermion

=     1   ca(FA         +  2e2�        )a   +      1     caC a  +     1   a[,      ]a        +   ihjk�         a(e^ja  k   +  e^ka  j )     vol
     2e2                                          8e2                2e2


     +   i   a(A           a)    -      i   hjk�  k      (H     -  8i�A)j          +      i      hjk�    j       (H    -  8i�A)k         .
         e2                            16                                                16

                                                         18
The topological term on the right-hand-side of (18) can be described as follows. The

symbol [E] represents a cohomology class in H2(E). It is the class represented by the

2-form

        E(A) = X - d(�aAa)   2(P � X) ,

which descends to E = P �G X. This form is manifestly closed, for the Ka�hler form
X on X is closed, and its cohomology class does not to depend on A. It is also clear
that  [E] does not change under deformation of , since the pull-back map is always
homotopy invariant, so this term is indeed topological.

    Finally, if desired, the auxiliary fields C and H can be eliminated from the action and

the QA-transformations through their equations of motion

        Ca = 2  FAa + 4e2 �a  
        Hz�k = 4idAz� k .

    One should also observe that the topological action IA is gauge invariant. The standard
methods of local quantum field theory therefore recommend that it be gauge-fixed through
the introduction of Fadeev-Popov ghost fields. This can presumably be done as explained
in [4], and would simply amount to adding to IA a further QA-exact term.

3.2 Observables

Having described the field content, the lagrangian and the QA-transformations of the
theory, the next step is to look for an interesting set of observables whose correlation
functions we would like to compute. In the non-gauged A-model the standard procedure
is to construct such observables from the de Rham cohomology classes of the target X.
In the gauged model, of course, the analog procedure uses instead the G-equivariant
cohomology classes of X. This construction was first described in [29], and then with a
little more detail in [3].

    Recall that the G-equivariant complex G� (X) is the set of G-invariant elements in the
tensor product S�(g)  �(X). A typical equivariant form  may thus be locally written
as

          = a1���ark1���kpl�1���l�q (w)  a1 � � �  ak dwk1  � � �  dwkp  dw�l1  � � �  dw�lq ,

where the coefficients a1���ark1���kpl�1���l�q are symmetric on the aj's and anti-symmetric on
the kj's and lj's. To each such form one can associate an operator O in the topological

        19
field theory defined by the local formula

O = (a1���ar k1���kpl�1���l�q  )    r                 p                   q

                                     ( +  + FA)aj       (ki + dAki)         (li + dAli) .

                                  j=1                i=1                 i=1

                                                                                           (19)

It can then be checked that this correspondence is globally well defined and that, further-

more,

                                  (d + QA) O = OdG ,                           (20)

where d is the exterior derivative on  and dG is the Cartan operator on G� (X). Now
assume that  is dG-closed and decompose O according to the form degree over , i.e.
write

                                     O = O(0) + O(1) + O(2) ,

where for example

       O(0) = (a1���ar k1���kpl�1���l�q  )    r               p       q        (21)

                                                aj               ki      li .

                                            j=1              i=1     i=1

Then in terms of this decomposition identity (20) breaks into

                                  d O(2) = 0 ,
                                  d O(1) = - QA O(2) ,
                                  d O(0) = - QA O(1) ,
                                  QA O(0) = 0 ,

which are the descent equations of the model. Finally let  be any j-dimensional homology
cycle in  and define the new operators

                                  W (, ) :=          O(j) .


These are then the natural observables associated with the gauged A-model. In fact it

follows as usual from the descent equations and Stokes' theorem that W (, ) is QA-closed,

so is indeed an observable. Moreover, the QA-cohomology class of W (, ) only depends
on the classes of  and  in HG� (X) and Hj(M), respectively. The typical correlation
functions of the theory can then be written down as path-integrals of the form

                   D(A, , , , , , c, , ) e-IA                W (i, i) ,        (22)

                                                     i

where the integration is taken over all fields, but with  restricted to a fixed topological

sector, or more precisely with fixed class []  H2G(X).

                                            20
3.3 Localization and moduli space

The usual credo says that a path-integral with a fermionic symmetry localizes to the
bosonic field configurations that are fixed points of the symmetry. Since QA can be
regarded as a generator of one such symmetry, we will be interested in the bosonic field
configurations annihilated by QA. These field configurations can be read from (17) and,
after eliminating the auxiliary fields, are precisely the solutions of

�A = 0                                    (23)

 FA + 2e2�   = 0
A = a(e^a  ) = 0 .

The first two equations are known as the general vortex equations on a Riemann surface.
They were first written down in [11] and generalize the usual Nielsen-Olsen vortex equa-
tions. The two equations involving , although in general non-trivial, in many cases of
interest only have the  = 0 solution, and so in these cases can be discarded. It can be
shown, for example, that if 0 is a regular value of the moment map �, then given any fixed
homotopy class of sections of E, for a sufficiently big value of the constant e2 (Vol ) any
solution of (23) with  in that class has zero  [10, lem. 4.2]. Another instance, in the
abelian case: if G is a torus, X is compact connected and (  FA)/(e2Vol ) is a regular
value of �, then any solution of (23) has zero  [3]. Nonetheless, even after discarding
the last line of (23), the two remaining (vortex) equations are very non-trivial. For ex-
ample, unlike monopoles or instantons, no explicit non-trivial solution of these equations
is known, and this for any , X or G, including the non-compact  = C.

    For the topological field theory, however, the main objects of interest are not the
solutions themselves, but rather the spaces of all solutions, or more precisely the moduli
spaces of solutions up to gauge equivalence. These vortex moduli spaces are in general
finite-dimensional, have a natural Ka�hler structure, but may contain singularities and be
non-compact. Their virtual complex dimension, as given by elliptic theory, is

(dimCX - dimG)(1 - g) + cG1 (T X) , () ,  (24)

and is basically just the difference of the indices of the operators in (9) [10].
    The standard heuristic arguments of TFT [28, 29] then say that, in favourable cases,

the path-integrals (22) reduce to finite-dimensional integrals of differential forms over
the vortex moduli spaces. These finite-dimensional integrals are completely classical ob-

        21
jects and, modulo (in fact very difficult) problems related to the singularities and non-
compactness of the moduli spaces, make sense in the realm of traditional mathematics, as
opposed to the path-integrals. The numbers provided be these finite-dimensional integrals
can in fact be identified with the so-called Hamiltonian Gromov-Witten invariants of X,
which have been defined using a very different, rigourous, universal construction. All this
story is analogous to the well known case of the non-gauged sigma-model, which leads to
the Gromov-Witten invariants; it is spelled out in detail in [3].

    Another important fact is that in the limit e2  + the gauged sigma-model with
target X tends to a non-gauged sigma-model with target X//G. This is just as in the
linear case of [31]. As a consequence one expects some relation to exist between the
HGW-invariants of X and the GW-invariants of X//G [14].

    We now end this section with a few references. Regarding the vortex moduli spaces,
there has been a longstanding interest in them. Starting with the simplest case of the
abelian Higgs models -- where X = C and G = U(1) -- about thirty years ago, the struc-
ture of these spaces has been investigated in several particular examples, mainly with X
a vector space. A hectic set of references is for example [2] within the more mathematical
literature and [1, 31, 25] within theoretical physics. The Hamiltonian Gromov-Witten
invariants, in comparison, have only recently been defined [10, 11]. They have been fur-
thermore studied in [12, 14].

4 The gauged B-twist and Landau-Ginzburg models

4.1 Fields, action and the QB-operator

Starting with the supersymmetric model of section 2, keep the fields A,  and D unchanged

and, with the others, define formally a new set of fields through the expressions


zk = 2i-k                     k = 2(+k + -k )                                      (25)

zk� = - 2i+k                  k  =    2  hk�j (-j  -  +j )

za  =  -ia/        2          za = -a

z�a = i�a/ 2                  z�a = a+

a   =  i  (�a-  +  �+a )      F k = F k - ikj +i -j
       2
       i
a   =  2  (�a-  -  �+a )      F k = F k - ikj -i +j .

                          22
These local components can be combined to define the global fields

                   -1 (;  ker dE)                                  1+(; gP )
                   -0 (;  ker dE)                             ,   0-(; gP )
                    -0 (; (ker dE))
                F  +0 (;  ker dE)                                 -1 (; gP )
                                                                D  0+(; gP ) .

These latter fields, together with A,  and D, form the field content of the gauged B-
model.

    The action of the fermionic operator QB = Q+ + Q- follows from the supersymmetry
transformations (4),(5) and the definition (15) of Q�. One simply needs to substitute the
new fields (25) into the supersymmetry transformations and then write the result in an
invariant form that makes sense on any Riemann surface . This procedure yields:

QB k = 0                                                                   QB k = 0             (26)

QB k = k                                                                   QB k = 4hjk� F k

QB  = 4dA+i                                                                QB F k = -rkl F r l

QB A = -i                                                                  QB  = 

QB  = A   + D                                                              QB  = 0

QB      =     FA  -  1  [, ] + iA                                          QB D = -  A+i  
                     2
                             i
QB  Fk  =  i    ( A+i )k  +  8  (s�ikj  )  s    (i    j )  -  4i ae^ka  ,

where  is the Hodge operator on . Observe that the complex connection

                                        A = A + i

emerges naturally in these transformations. It is a QB-closed field and has curvature
                                       FA = FA - 12[, ] + iA .

    The topological action of the B-theory is also obtained by simple substitution of the
new fields into the supersymmetric lagrangian (3). After discarding a total derivative

                                                23
term d[ia(dA�a)/2] in that lagrangian the result is

IB =     1    |FA     -     1  [,  ]|2  +  |dA|2       +   2e2|�      |2     +   |ae^a|2   +   1   |A|2
        2e2                 2                                                                 2e2


        +   1   |A            |2   -   1   |D   -   2e2�        |2    +  ie^aj (aj      -  hj k� a  k )
           2e2                        2e2
                      1                      1                                 1
        -  |F  +      2     gradCW |2   +    4  hj  k� (j  W  )(k   W    )  +  8  hrk�  r  j  (k��j W       )  vol

        -  1  hj  k�   k ( A-i )             j  +   i  j   (A+i          )j    -  i     (s�jnk)    s  n     j    k
           4                                        4                             32
           i                               i                             1                                i
        -  2  hj  k�  e^ka  a      j    +  e2  a    (A-i      a)      -  e2  a(A-i            a)    -    16    (j    k)(kjW )  .

When the superpotential W is taken to be zero this action is QB-exact, just as in the
usual non-gauged case [24, 30]. In fact after a few integrations by parts on can check that

                                                       IB = QB 

with gauge fermion

                      =           1     a    FAa-i     -   1  hj  k�(j   )     dA+i k      -  1  F    j  j  vol
                                2e2                        4                                  4

                                   +     1   a(a             a  +   4e2�a           -   Da)   vol     .
                                        2e2

If desired, the auxiliary fields F and D can be eliminated from the action and the QB-
transformations through their equations of motion

                                                    Fk       =  -  1  hk�l �l W
                                                                   2

                                                    Da = 2e2�a   .

4.2 Localization, moduli spaces and observables

Localization

As can be read from (26), after eliminating the auxiliary fields the fixed points of QB are
the bosonic field configurations that satisfy

                  dA = 0                                                                                 FA = 0      (27)
                   A   + 2e2�   = 0
                                                                                    (gradCW )   = 0 .

                                                                  24
Accordingly, one expects the path-integrals to localize to these configurations. Now, were
this the A-model or the non-gauged B-model, nothing of major import would need to be
added; in the present case of the gauged B-model, however, there is one extra subtlety
(already noted in [31] in the linear case) that allows us to take the localization argument a
bit further. To explain this start by recalling that the operator QB is defined as Q+ + Q-,
where each of these two operators is defined through (15) and makes perfect sense when
acting on the B-model fields (25) defined on any Riemann surface. The first point to note
is then that the action IB is not only QB-exact, but also, up to topological terms, Q+-
and Q--exact. One can in fact check that

                                      IB = Q�� � 2 (A) ,


where the last term is topological, as in (18), and the gauge fermions are5

� =    hjk� hzz�(zj�/z dzA/z�k - ijz/z� z�a/z e^ak) + 2(a � a)(�  )a


         1  hj  k�  F  j  Qk  �  1   Q(aa)  vol .
         2                       e2

These fermions are just the components of  that transform with different charges under
the axial symmetry (8), so that  = (+ + -)/2; one can also check that Q+- =
Q-+ = 0. Now, with an action that is both Q+- and Q--exact, the expectation values
of Q�-closed operators (such as G-invariant holomorphic functions on X) will localize to
the simultaneous fixed points of Q+ and Q-. These field configurations are of course also
QB fixed points, since QB = Q+ + Q-, but the converse needs not be true. While in the
A-model and in the non-gauged models these two sets of fixed points do in fact coincide,
and so we do not need to care about all this, in the gauged B-model the simultaneous

fixed points of Q+ and Q- are the solutions to the seven equations

dA = FA - [, ]/2 = 0                               � = 0                                         (28)
A = A   = ae^a = 0
                                            (gradCW )   = 0 ,

which a priori seem to be stronger than (27).

    5The notation z�/z means that the first option, here z�, is to be taken for +, and the second for -;
similarly for the other fields.

                                 25
Moduli spaces

In this section we will determine (in easy cases) the moduli space MB of solutions of
equations (28) up to gauge equivalence. Since MB is the localization locus of the path-
integrals, it is of course a very important object in the B-model.

    The easiest situation to analyse occurs when the Riemann surface  has genus zero,
so is a sphere. In this case it is well known that

               dim { : A = A   = 0} = dim HA1 (S2; gP ) = 0

for every connection A, so that equations (28) imply that  = 0 and that FA = 0. But
on a sphere there are no monodromies, and the only possible flat connection is the trivial
connection on the trivial principal G-bundle, up to gauge equivalence. This means that
one can find a gauge transformation such that dA = d = 0, and hence  is gauge-
equivalent to a constant map to the subset �-1(0) of X. This gauge transformation,
however, is unique only up to multiplication by a constant in G, and so it is clear that
for genus zero


                 if P is non-trivial,


MB  �-1(0)/G = X//G if P is trivial and W = 0 ,                    (29)


               (�-1(0)  Crit W )/G if P is trivial and W = 0 ,

where constant maps have been identified with their target point.

    Although a priori not so evident, this result is also valid for  of any genus provided
that we assume that G acts freely on �-1(0), i.e. provided that the symplectic quotient
X//G is smooth. To justify this we will now make a short detour. Start by noticing that
the local equation

                                        dA = d + Aa(e^a  ) = 0

implies that the image of a solution  is contained in a single G-orbit in X; more precisely,
there exists a point q  �-1(0) such that the image of  :   E is contained in the
sub-bundle

                             Eq = {[p, q]  E = P �G X : p  P }  E .

Observe also that Eg�q = Eq for any g  G and that, by the assumed triviality of the
stabilizer of q, the map

                                        fq : P - Eq , p  [p, q]

                                                       26
is actually a fibre-preserving diffeomorphism. It is then clear that fq-1   :   P is
a global section, and so P must be trivial. Now consider the connection A. As is well
known, such an object induces splittings of the tangent bundles

T P = HA  ker dP  T Eq = HA  ker d(E|Eq )
T E = HA  ker dE

into horizontal and vertical sub-bundles. In this picture the covariant derivative of  is
just the composition

                               dA : T  --d- T E -p-ro-je-c-tion ker dE ,

and so dA = 0 means that the image of d is entirely contained in HA. But by the
very definition of HA we have that dfq(HA) = HA, which implies that fq-1   is in fact
a horizontal section of P , and this in turn shows that A is gauge-equivalent to the trivial
connection. From here onwards the same arguments as in the  = S2 case lead to the
conclusion that the moduli space MB is given by (29).

    The cases where G does not act freely on �-1(0) are of course more complicated
and difficult to analyse. Among these, the simplest situation occurs when G acts freely
everywhere in �-1(0) except at k fixed points. In this case, calling C,P the moduli space
of solutions of

                                  A = A   = FA - [, ]/2 = 0 ,

it is rather clear that the space MB will just consist of k copies of C,P when P is non-
trivial and, when P is trivial, will be isomorphic to X//G except that each singularity in
this quotient (which corresponds to a fixed point in �-1(0)) is to be substituted by a copy
of C,P . Observe as well that in the abelian case C,P is just

                C,P  H1()dim G � (moduli space of flat connections on P ) .

These are of course only loose comments, and we will not pursue them here any further.

Observables

The first natural observables of the B-theory are the holonomies, or Wilson loop oper-
ators, associated to the QB-closed complex connection A. These observables, however,
completely ignore the target manifold X, and so if not coupled to other observables will

                                                       27
have expectation values that only reflect properties of the 2D-Yang-Mills. Another set of
observables, this time dependent on X, are the G-invariant holomorphic functions on X.
If f is holomorphic on X then the rules

      QBk = Q�k = 0                                    QBk = 2Q�k = -2kW

show that f  , besides being QB-closed, is QB-exact iff f can be written as

                                        f = vkkW = dW (v)                                       (30)

for some G-invariant holomorphic vector field v on X. Thus the chiral ring of the gauged
B-model is the ring of G-invariant holomorphic functions on X divided by the ideal of
functions of the form (30). All this is analogous to the non-gauged sigma-model [19], one
only has to add here the word G-invariant. Observe also that G-invariant holomorphic
functions on X descend to holomorphic functions on X//G, which, after localization, is
in some sense the "effective target" of the model. The author doesn't know, however, if
every holomorphic function on X//G can be obtained in this way, or more generally, how
different is the G-invariant chiral ring of X from the standard chiral ring of X//G.

    Finally, in the special case where the superpotential W vanishes, a G-invariant form

V  =  V j1���jq     dwi1    �  �  �    dwip            �  �  �                    0,p(X; qT X)
        i�1 ���i�p                             wj1                wjq

determines an associated operator in the field theory by

                            OV       =  V j1���jq    i1 � � � ip j1 � � � jq  .                 (31)
                                          i�1���i�p

One can directly check that QBOV = O�V , and so this correspondence defines a ho-
momorphism between the �-cohomology of G-invariant forms in 0,p(X; qT X) and the

QB-cohomology of operators in the B-model. Again, all this mimicks the non-gauged
model with the added G-invariant condition. Note, however, that (31) is not in general

Q�-closed, and so more care is needed when localizing the expectation values of these
observables, as explained at the beginning of section 4.2. This problem does not arise in

the non-gauged B-model.

Acknowledgements. I would like to thank Guillaume Bossard, Lotte Hollands, Andriy
Haydys, Sheer El-Showk and David Tong for helpful conversations, as well as the JHEP
referee for his comments. I am partially supported by the Netherlands Organisation for
Scientific Research (NWO), Veni grant 639.031.616.

                                                       28
A Notation and conventions

Manifolds, group action and bundles

For reference, here is a list of the conventions and notation used in the paper.

�  is a Riemann surface of genus g and X is a complex Ka�hler manifold. G is a compact
connected Lie group that acts on X on the left. The G-transformations preserve the
symplectic and complex structures of X. The Lie algebra of G is called g, has a basis
{ea} and is equipped with an Ad-invariant inner product , which may be used to identify
g with the dual space g. An element   g induces a vector field ^ on X whose flow is
p  exp(t) � p. With this convention the Lie bracket on g is related to the Lie bracket of
vector fields through [1, 2] = -[^1, ^2].

� The G-action on X is assumed hamiltonian, i.e. there should exist a moment map
� : X  g. In the convention used here the moment map satisfies

  (i) d(�, ) = ^ X for all   g, where X is the Ka�hler form on X and (�, �) is the
       natural pairing g � g  R;

  (ii) g � = Adg  � for all g  G, where  denotes the G-action on X and Ad is the
       coadjoint representation on g.

If a moment map � exists, it is not in general unique, but all the other moment maps
have the form � + r, where r  [g, g]0  g is a constant in the annihilator of [g, g].
Under the identification g  g provided by , the inner product, the annihilator [g, g]0
is identified with the centre of g. The constant r is then the Fayet-Iliopoulos parameter
of the supersymmetric theory.

� P : P   is a principal G-bundle. E : E   and gP   are the associated
bundles E = P �G X and gP = P �Ad g. These have typical fibres X and g, respectively.
The Higgs field  :   E is a section of E. The vector bundle ker dE  E is the kernel
of the derivative dE : T E  T .

K�ahler geometry

Regarding the Ka�hler geometry of  and X, we always work with the holomorphic tangent
bundles T  and T X. The local complex coordinates on  and X are z = x1 + ix2 and

                                                       29
{wk}, respectively. The hermitian metric hX is related to the real metric gX and the

Ka�hler form X by

                   h = hjk� dwj  dw�k = gX - i X .

This implies that, with the most usual conventions for the wedge product, X =
(i/2)hjk� dwj  dw�k. The hermitian (Levi-Civita) connection on T X satisfies

                                =  ljk      =  hlr� (j hkr�)      .
                        wj  wk          wl                    wl

Its curvature components and Ricci form are then given by

                                Rjk�lr� = -lr�hjk� + hmn�(lhjn�)(r�hmk�)
                                      = -i � log(det h) .

For any   g one can check that the holomorphic and Killing vector field ^ satisfies

                                           hjk� l^k = -hlk� j ^k
                                          2 k�(�, ) = ihjk� ^j .

    The Hodge star operator on  satisfies

                    = 1                        dz = -idz
                     1 =                       dz� = idz� .

    In sections 3 and 4 we have often used that a connection A on some bundle V  
can be extended to an operator r(; V )  r+1(; V ), so beyond its usual r = 0
definition. For instance if  = zdz + z�dz� is a one-form with values on V then A =
(zAz� - z�z)dz  dz�.

The N = 2 lagrangian and supersymmetry transformations

In section 2 we spelled out the euclidean lagrangian and supersymmetry transformations
for the N = 2 gauged non-linear sigma-model in two dimensions. These formulae are
related to their counterparts on Minkowski space-time through the substitutions

2dzA�  d1A + d0A                              2zA�/z  1A � 0A
2dAz  dA1 - d0A                         2(A)z�/z  (A)1 � (A)0
F12  iF01

                                        30
and a global sign change. Here (x0, x1) are the Minkowski coordinates on  = R1,1 with
signature (-, +) and x1 + ix2 = z is the complex coordinate on the euclidean  = C. The
Minkowski lagrangian is real, i.e. invariant under complex conjugation, while the euclidean
lagrangian is not. The conventional rules for conjugating fermions in Minkowski signature
are  =  and 12 = 2 1. In euclidean signature these rules do not apply. In fact, the
barred and unbarred euclidean fermionic fields should be regarded as independent [13],
and in rigour should have been denoted by different letters in section 2.

    The Minkowski version of the lagrangian and supersymmetry transformations of sec-
tion 2 were obtained by dimensional reduction of the N = 1 formulae in four dimensions
presented in [13]. Since the conventions of [13] differ from the most commonly used
in the physics literature we have adjusted the various i and 2 factors so that, upon
specialization to the gauged linear sigma-model, our formulae agree with [31, 32].

    This specialization to the linear sigma-model and group G = U(n) should, neverthe-
less, be done with some care, since the physicists identify the Lie algebra of U(n) with the
hermitian matrices while in mathematics the conventional identification is with the anti-
hermitian matrices. In the physics convention a Lie algebra valued field such as  = aea
is identified with a hermitian matrix ~; our complex conjugate field � = �aea becomes the
hermitian conjugate matrix ~; the Lie brackets [, �] = a�b[ea, eb] become, on the other
hand, i[~, ~]. This implies that the covariant derivative A of (6) becomes d~ + i[A~, ~].
Finally, for the natural action of G = U(n) on Cn, one can calculate that the vector fields
on T Cn  Cn become

a(e^a  ) - i~         ake^ja - i~kj
�a(e^a  ) - i~ .

Systematically applying these substitutions to all the fields in the lagrangian of section
2 (rotated to Minkowski space) we get exactly the lagrangian of [31, 32]. As for the
supersymmetry transformations, they agree with all the expressions of [32] except that in
the formulae for D, +, �+, - and �- extra �i factors appear in the commutators.
This factors also appear in the dimensional reduction of the formulae of [27] and, we
believe, should be there. Of course in the abelian case this makes no difference, so our
formulas agree with [31].

                  31
References

 [1] R. Auzzi, S. Bolognesi, J. Evslin, K. Konishi and A. Yung : `Nonabelian Super-
      conductors: Vortices and Confinement in N = 2 SQCD'; Nucl. Phys. B673 (2003)
      187�216.
      M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Moduli space of non-abelian
      vortices'; Phys. Rev. Lett. 96 (2006), 161601.
      M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Solitons in the Higgs phase
      � the moduli matrix approach �'; J. Phys. A39 (2006), R315�R392.
      A. Hanany and D. Tong : `Vortices, Instantons and Branes'; JHEP 0307 (2003), 037.
      D. Tong : `TASI lectures on solitons: Instantons, monopoles, vortices and kinks';
      hep-th/0509216.

 [2] D. Banfield : `Stable pairs and principal bundles'; Q. J. Math. 51 (2000), 417�436.
      J. Baptista : `Vortex equations in abelian gauged sigma-models'; Commun. Math.
      Phys. 261 (2006), 161�194.
      S. Bradlow : `Vortices in holomorphic line bundles over closed Ka�hler manifolds';
      Commun. Math. Phys. 135 (1990), 1�17.
      S. Bradlow : `Special metrics and stability for holomorphic bundles with global
      sections'; J. Differential Geom. 33 (1991), 169�213.
      S. Bradlow and G. Daskalopoulos : `Moduli of stable pairs for holomorphic bundles
      over Riemann surfaces'; Internat. J. Math. 2 (1991), 477�513.
      U. Frauenfelder : `Vortices on the cylinder'; Internat. Math. Res. Notices 2006,
      63130.
      O. Garc�ia-Prada : `Invariant connections and vortices'; Comm. Math. Phys. 156
      (1993), 527�546.
      I. Mundet i Riera : `A Hitchin-Kobayashi correspondence for Ka�hler fibrations'; J.
      Reine Angew. Math. 528 (2000), 41�80.
      C.H. Taubes : `Arbitrary N-vortex solutions to the first order Ginzburg-Landau
      equations'; Commun. Math. Phys. 72 (1980), 277�292.
      Y. Yang : `Solitons in field theory and nonlinear analysis'; Springer-Verlag, New
      York, 2001.

 [3] J. Baptista : `A topological gauged sigma model'; Adv. Theor. Math. Phys. 9 (2005),
      1007�1047.

 [4] L. Baulieu and I. Singer : `Topological Yang-Mills symmetry'; Nucl. Phys. B Proc.
      Suppl. 5B (1988), 12�19.

                                                       32
      S. Cordes, G. Moore and S. Ramgoolam : `Lectures on 2D Yang-Mills theory, equiv-
      ariant cohomology and topological field theories'; hep-th/9411210
 [5] N. Berline, E. Getzler and M. Vergne : `Heat Kernels and Dirac Operators'; Springer-
      Verlag, Berlin, 1992.
 [6] R. Bielawski and A. Dancer : `The geometry and topology of toric hyperka�hler
      manifolds'; Commun. Anal. Geom. 8 (2000), 727�760.
 [7] R. Bott and L. Tu : `Equivariant characteristic classes in the Cartan model'; in
      "Geometry, analysis and applications", World Sci. Publ., River Edge, 2001.
 [8] C. Boyer, K. Galicki and B. Mann : `The geometry and topology of 3-Sasakian
      manifolds'; J. Reine Angew. Math. 455 (1994), 183�220.
 [9] J. Bryan and R. Pandharipande : `The local Gromov-Witten theory of curves';
      arXiv:math/0411037v3 [math.AG].
[10] K. Cieliebak, A.Rita Gaio, I. Mundet i Riera and D. Salamon : `The symplectic
      vortex equations and invariants of Hamiltonian group actions'; J. Symplectic Geom.
      1 (2002), 543�645.
[11] K. Cieliebak, A. Rita Gaio and D. Salamon : `J-holomorphic curves, moment maps,
      and invariants of Hamiltonian group actions'; Internat. Math. Res. Notices 16 (2000),
      831�882.
      I. Mundet i Riera : `Hamiltonian Gromov-Witten invariants'; Topology 42 (2003),
      525�553.
[12] K. Cieliebak and D. Salamon : `Wall crossing for symplectic vortices and quantum
      cohomology'; Math. Ann. 335 (2006), 133�192.
      I. Mundet i Riera and G. Tian : `A compactification of the moduli space of twisted
      holomorphic maps'; arXiv:math/0404407v1 [math.SG].
[13] P. Deligne and D. Freed : `Supersolutions.' in "Quantum fields and strings: a course
      for mathematicians", Vol. 1; Amer. Math. Soc., Providence, 1999.
[14] A. Rita Gaio and D. Salamon : `Gromov-Witten invariants of symplectic quotients
      and adiabatic limits'; J. Symplectic Geom. 3 (2005), 55�159.
[15] G. Gibbons, P. Rychenkova and R. Goto : `Hyper-Ka�hler quotient construction of
      BPS monopole moduli spaces'; Commun. Math. Phys. 186 (1997), 581�599.
[16] V. Guillemin, V. Ginzburg and Y. Karshon : `Moment maps, cobordisms, and Hamil-
      tonian group actions'; Amer. Math. Soc., Providence, 2002.
[17] V. Guillemin and S. Sternberg : `Supersymmetry and equivariant de Rham theory';
      Springer-Verlag, Berlin, 1999.

                                                       33
[18] N. Hitchin, A. Karlhede, U. Lindstro�m and M. Rocek : `Hyperka�hler metrics and
      supersymmetry'; Commun. Math. Phys. 108 (1987), 535�589.

[19] K. Hori, S. Katz, A. Klemm, R. Pandharipande, R. Thomas, C. Vafa, R. Vakil and
      E. Zaslow : `Mirror symmetry'; Amer. Math. Soc., Providence; Clay Mathematics
      Institute, Cambridge, 2003.

[20] K. Hori and D. Tong : `Aspects of non-abelian gauge dynamics in two-dimensional
      N=(2,2) theories'; JHEP 0705 (2007), 079.

[21] A. Kapustin and A. Tomasiello : `The general (2,2) gauged sigma model with three�
      form flux'; arXiv:hep-th/0610210v2.

[22] P. Kronheimer : `A hyperkahler structure on the cotangent bundle of a complex Lie
      group'; arXiv:math/0409253.
      A. Dancer and A. Swann : `Hyper-Khler metrics associated to compact Lie groups';
      Math. Proc. Cambridge Philos. Soc. 120 (1996), 61�69.

[23] P. Kronheimer : `A hyper-Khlerian structure on coadjoint orbits of a semisimple
      complex group'; J. London Math. Soc. 42 (1990), 193�208.

[24] J. Labastida and P. Llatas : `Topological matter in two dimensions'; Nucl. Phys.
      B379 (1992), 220�258.
      J. Labastida and M. Marino : `Type B topological matter, Kodaira-Spencer theory,
      and mirror symmetry'; Phys. Lett. B333 (1994), 386�395.

[25] D. Morrison and M. Plesser : `Summing the instantons: quantum cohomology and
      mirror symmetry in toric varieties'; Nucl. Phys. B 440 (1995), 279�354.

[26] I. Mundet i Riera : `Yang-Mills-Higgs theory for symplectic fibrations'; Ph.D. Thesis,
      UAM (Madrid), April 1999, arXiv:math/9912150v1 [math.SG].

[27] J. Wess and J. Bagger : `Supersymmetry and supergravity'; Princeton Univ. Press,
      Princeton, 1983.

[28] E. Witten : `Topological quantum field theory'; Comm. Math. Phys. 117 (1988),
      353�386.

[29] E. Witten : `Topological sigma models'; Comm. Math. Phys. 118 (1988), 411�449.
[30] E. Witten : `Mirror manifolds and topological field theory'; in "Essays on mirror

      manifolds", Int. Press, Hong Kong, 1992.
[31] E. Witten : `Phases of N=2 theories in two dimensions'; Nucl. Phys. B403 (1993),

      159�222.
[32] E. Witten : `The Verlinde algebra and the cohomology of the Grassmannian'; in

      "Geometry, topology and physics", Int. Press, Cambridge MA, 1995.

                                                       34
