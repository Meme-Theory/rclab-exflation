# 2005 Topological gauged sigma model

**Source:** `03_2005_Topological_gauged_sigma_model.pdf`

---

arXiv:hep-th/0502152v2 25 Nov 2005                                                                                              DAMTP-2005-18

                                           A topological gauged sigma-model

                                                                         J. M. Baptista 

                                                    Department of Applied Mathematics and Theoretical Physics 
                                                                             University of Cambridge

                                                                          February 2005

                                                                             Abstract

                                        We describe a topological field theory that studies the moduli space of solutions of the
                                    symplectic vortex equations. It contains as special cases the topological sigma-model and
                                    topological Yang-Mills over Ka�hler surfaces. The correlation functions of the theory are
                                    closely related to the recently introduced Hamiltonian Gromov-Witten invariants.

                                        e-mail address: [email redacted]
                                        address: Wilberforce Road, Cambridge CB3 0WA, England
Contents

1 Introduction                                1

2 The vortex equations                        4

3 The manifold of fields                      7

4 The topological action                      12

5 Observables I -- definition                 16

6 Observables II -- "universal" construction  21

7 Invariants and localization                 28

A The localization bundle                     36

B A proof from Section 7                      39

1 Introduction

Topological field theories are one of the cornerstones of the modern relations between
theoretical physics and mathematics. Their originality stems from the fact that they
employ methods of quantum field theory to study problems in geometry; most notably,
they use path-integrals to obtain invariants of manifolds. The first explicit examples of
these theories were topological Yang-Mills and the topological sigma-model, introduced
by Witten in [15] and [16]. Topological Yang-Mills studies the moduli space of instantons
over a four-manifold. Its correlation functions are then closely related to the Donaldson
invariants. The topological sigma-model studies pseudo-holomorphic curves on an almost
Ka�hler manifold, and its correlation functions are essentially the Gromov-Witten invari-
ants. After these initial examples several other topological theories were introduced, for
instance 2D topological gravity, Chern-Simons theory and topological string theory, each
studying different moduli spaces and invariants. This, however, is very well known story.

    The aim of this paper is to define a topological field theory that studies the moduli
space of solutions of the symplectic vortex equations. Its correlation functions, as we will
see, are then closely related to the so-called Hamiltonian Gromov-Witten invariants. Both

                                                        1
the vortex equations and the latter invariants were recently introduced in the mathematics
literature by Mundet i Riera in [13], and by Cieliebak, Gaio and Salamon in [6]. They
have been further studied in [7, 9, 14]. Here we want to give a topological field theory
version of the subject.

    The setting for the theory is a non-linear gauged sigma-model with Ka�hler domain M

and almost Ka�hler target X. The manifold X should also be equipped with a hamiltonian

and holomorphic action of the gauge group G. The fields of the theory are then the maps

 between M and X and the G-connections A over M. The energy functional is defined

as

    E(A, ) =     FA 2 + dA 2 + �   2 ,

              M

where FA is the curvature of A, dA is a covariant derivative, and � is a moment map for
the G-action on X. Notice that we are not simply gauging the usual sigma-model, since

a Maxwell term and a very important potential term are also present. By a Bogomolny

argument it can be shown that the energy is minimized by the solutions of

              �A = 0

              FA + �   = 0
              FA0,2 = 0 ,

which are the general vortex equations. All the notation is explained in detail in the next
section. Notice that when the group G is trivial the energy functional and the vortex
equations reduce to the usual sigma-model. When the manifold M is four-dimensional
and X is a point, we obtain instead the Yang-Mills energy and the equations FA = 0 and
FA0,2 = 0, which are just the anti-self-duality equations in disguise. Thus the topological
field theory that we want to define will contain as special cases the topological sigma-
model (or more precisely the A-model) and topological Yang-Mills over Ka�hler surfaces.
It should also contain the topological gauged linear sigma-model constructed by Witten
in [17]; this corresponds to taking M a Riemann surface, X a complex vector space, and
G a unitary group.

    All throughout the paper we approach the topological theory from the point of view of
infinite-dimensional differential geometry and equivariant cohomology. This geometrical
point of view was pioneered in [1] for topological Yang-Mills, and was subsequently applied
to many other field theories. It is reviewed for example in [4, 5, 8]. Also, here the manifold

                 2
X is always assumed to be Ka�hler, although the formalism could presumably be extended
to the almost Ka�hler case.

    We will now give a brief description of the content of each section. Sections 2 and
3 are introductory. In the first one we review the basic facts about the Yang-Mills-
Higgs functional and the general vortex equations. In the second one we introduce the
geometrical approach to the space of fields of the gauged sigma-model. This consists of
an informal presentation of the infinite-dimensional manifold of fields, its tangent space
and 1-forms, the action of the group of gauge transformations, and the associated Cartan
model for equivariant cohomology. Here we try to give a careful exposition and introduce
some necessary notation, but all the material is standard.

    In Section 4 we contruct the topological Lagrangian for the gauged sigma-model. As
is usually the case for cohomological field theories, this Lagrangian can be obtained from
purely geometrical considerations. Roughly speaking, it comes directly from the Mathai-
Quillen representative of the Thom class of a certain infinite-dimensional vector bundle
over the moduli space of fields [1, 4, 5, 8]. In Appendix A we explain how the gauged
sigma-model can be fitted into this geometrical approach. The results obtained there can
then be fed into the standard procedures of [1, 4, 5, 8] in order to justify many of the
apparently arbitrary choices in Section 4. The approach of Section 4, by itself, is a very
"nuts and bolts" one, more along the lines of the original constructions in [15, 16].

    In Section 5 we define the natural observables of the theory. In the geometric picture,
these observables are just a set of closed elements of the equivariant complex of the space of
fields. Section 6 is then spent explaining in detail the relation between these "quantum"
observables and the more traditional ways of defining invariants, namely the so-called
universal contructions. All the work of this section (and of most of the paper, by the
way) is just a matter of suitably combining and generalizing well known constructions
from topological Yang-Mills and the topological sigma-model.

    In the first part of Section 7 we apply standard localization to write down the correla-
tion functions as integrals of differential forms over the moduli space of vortex solutions.
Using the results of Section 6, this finally allows us to compare the correlation functions
of the topological theory with the Hamiltonian Gromov-Witten invariants defined in [7].
In this reference the invariants have been rigorously defined for M a Riemann surface and
a suitable class of G-manifolds X. The last two subsections are then mostly informative:
in 7.2 we discuss the moduli space of vortex solutions in the case where M is a Riemann

                                                        3
surface; in 7.3 we comment on some features of the invariants, namely the wall-crossing
phenomena and the adiabatic limit of the vortex equations. Appendix B contains the
proof of a proposition stated in 7.2 about the vortex moduli space for torus actions.

2 The vortex equations

In this section we will go through a quick review of the gauged sigma-model that admits
vortex equations. For more details see for example the original references [13, 6] or the
first section of [2].

    The data we need to define the sigma-model are the following.

    � Two Ka�hler manifolds M and X, with respective Ka�hler forms M and X.

    � A connected compact Lie group G with Lie algebra g, and an Ad-invariant positive-
       definite inner product (�, �) on g.

    � An effective, hamiltonian, left action  of G on X such that, for every g  G, the
       transformations g : X  X are holomorphic, and a moment map for this action
       � : X  g.

    � A principal G-bundle P : P  M.

We remark that, in the fullest generality, the complex structure on X need not be assumed
integrable, but we will assume that here. Using the elements above one can define the
associated bundle E = P � X, which is a bundle over M with typical fiber X. It is
defined as the quotient of P � X by the equivalence relation (p � g, q)  (p, g � q), for all
g  G. The bundle projection E : E  M is determined by E([p, q]) = P (p), where
[p, q] denotes the equivalence class in E of the point (p, q) in P � X.

Definition. The convention used here is that a moment map for the action  of G on
(X, X ) is a map � : X  g such that

  (i) d �,  = ^ X in 1(X) for all   g, where ^ is the vector field on X defined by
       the flow t  exp(t).

  (ii) g � = Adg  � for all g  G, where Adg is the coadjoint representation of G on g.

                                                        4
If a moment map � exists, it is not in general unique, but all the other moment maps are
of the form � + c, where c  [g, g]0  g is a constant in the annihilator of [g, g]. Recall
also that under the identification g  g provided by an Ad-invariant inner product on g,
the annihilator [g, g]0 is taken to the centre of g.

    The fields of the theory are a connection A on the principal bundle P and a smooth

section  of E. Calling A the space of such connections and (E) the space of such
sections, we define the energy functional E : A � (E)  R+0 of the sigma-model by

    E(A, ) =    1     1   FA 2 +     dA 2 + e2         � 2 ,            e  R+.       (2)
                2     e2
                   M

In this formula FA is the curvature of the connection A, and dA is the covariant derivative
of  induced by A. The norms are defined in the natural way, using the metrics on M, X

and g. The last term is well defined because of the G-equivariance of the moment map

and the AdG-invariance of the inner product .

    For later convenience we will record here the local (i.e trivialization-dependent) for-
mulae for dA and �A. Let s : U  P be a local section of P over a domain U in M.

Since E = P � X is an associated bundle, this determines a trivialization of E|U by

              U � X  E|U , (x, q)  [s(x), q] .                                       (3)

With respect to these trivializations a section  of E can be locally identified with a
map ^ : U  X, and a connection A on P can be identified with the connection form

sA = A� dx�  1(U ; g). Then the covariant derivative dA, which is a section of the
bundle T M   ker d E  M, is locally given by

    dA     =  d ^  +  sAa e^a  =  (�^r         + Aa�  e^ra)  dx�    ^(      )  .     (4)
                                                                        ur

In these formulae {ea} is a basis of g, e^a is the vector field on X induced by ea and
the left G-action, and we have picked real coordinates {x� : 1  �  2m} on M and
{ur : 1  r  2n} on X. Similarly, by picking complex coordinates {z : 1    m} on
M and {wj : 1  j  n} on X, one can also write down the anti-holomorphic part of dA

as                                                                         
                                                                          wj
    �A  =  � ^  +  (sAa)0,1 e^a   =  (� ^j     +  Aa�  e^aj )  dz�    ^(       )  .  (5)

Having recorded these formulae we now come to the first basic fact of the theory, namely

the existence of a set of first order equations -- the vortex equations -- whose solutions

                                     5
minimize the energy functional. This was first found in [13] and [6] for this general
non-linear sigma-model.

Theorem ([13, 6]). For any connection A  A and any section   (E),

E (A, ) = T[] +                         �A 2 + 1      1  FA  +  e  �     2+   2      FA0,2 2 ,  (6)
                                                   2  e                       e2
                                     M

where the term

T[]  =          1     (m  1  1)!        [E ]    Mm-1     -      ab  2)!  FAa    FAb    Mm-2     (7)
                2         -                                 e2(m -
                   M

does not depend on A, and only on the homotopy class of .

Corollary ([13, 6]). Within each homotopy class of the sections  we have that E(A, ) 
T[], and there is an equality if and only if the pair (A, ) in A�(E) satisfies the equations

                                        �A = 0                                                  (8a)

                                        FA + e2 �   = 0                                         (8b)

                                        FA0,2 = 0 .                                             (8c)

These first order equations are usually called vortex equations.

    Besides �A, several new terms appear in (6) when compared with (2); their meaning
is the following. The operator  : �(M)  �-2(M) is the adjoint, with respect to the
metric gM on M, of the operator   M   on �(M). By well known formulae,

                      FA = (M  FA) = gM (FA, M ) ,                                              (9)

and so FA can be seen as a locally defined function on M with values in g, just as �  .
(More properly, they should be both regarded as global sections of P �AdG g). Next, FA0,2 is
just the (0, 2)-component of FA under the usual decomposition 2(M ) = 2,0 1,1 0,2.
Finally [E] is a cohomology class in H2(E) that does not depend on A. Using the Cartan

complex for the G-equivariant cohomology of X, [E] is just the image by the Chern-Weil
homomorphism of the cohomology class in HG2 (X) determined by the equivariantly closed
form X - b�b  G2 (X) (see for example [3, ch. VII]).

                                                6
3 The manifold of fields

3.1 The manifold

Here we continue the exposition of the previous section by recalling some well known
properties of the infinite-dimensional manifold A � (E), which is our space of fields.
Namely, we describe its natural Ka�hler structure and the action of the group of gauge
transformations G. For more details see for example [13] and the references therein. Along
the way we will also write down some explicit expressions that will be needed in Section 4.
In subsections 3.2 and 3.3 the first basic elements of the topological gauged sigma-model
are introduced, like the BRST operator Q and a few "anticommuting fields". These are
all described in terms of the G-equivariant cohomology of A � (E).

    To start the study of the manifold A � (E) we first look at its tangent space. Recall
that, given a connection A  A, the tangent space TAA can be identified with 1(M; gP )
-- the space of 1-forms on M with values in the bundle gP := P �AdG g. Likewise, given
a section   (E), the tangent space T(E) can be identified with the space of sections
of Vert  M. Here Vert  E is the sub-bundle of T E  E defined by the kernel of
dE : T E  T M, and Vert is the pull-back bundle. Thus

                          T(A,)(A � (E))  1(M ; gP )  (Vert) .

Both summands on the right hand side have a natural metric and complex structure,
induced by the ones on M and X, respectivelly. Hence the manifold A � (E) has a
natural metric and complex structure. Moreover, it can be shown that this complex
structure is integrable, compatible with the metric, and that the K�ahler form is closed.
So A � (E) is a Ka�hler manifold.

    More explicitly, suppose that we are given tangent vectors

                      = �a dx�  ea  1(M ; gP )                                    (10)

                     V  =  V  r  ^(      )   (Vert) ,
                                     ur

which are here written down in terms of their local representatives with respect to trivi-

alizations of gP and E induced by a local trivialization of P . Then the Ka�hler metric on

A � (E) is given by

gA�(E)(1 + V1, 2 + V2) =             (1)a� (2)b (gM )� ab + e2 V1r V2s (gX )rs .

                                 M

                                         7
    We now turn to the action of gauge transformations on the fields in A � (E). Recall
that the group G of gauge transformations is the group of G-equivariant automorphisms
of the bundle P  M which descend to the identity map on the base M. Equivalently, G
is the group of sections of the associated bundle P �AdG G. Using the local trivializations
(3), each of these sections g  G is locally represented by a map from U  M to G. The
Lie algebra of G is the space G = 0(M; gP ) of sections of the bundle gP  M; each of
these sections can be locally represented by a map from U to g.

    The group G has a natural right action on the manifold of fields A � (E). For any
g  G this action is determined by the formulae

     A � g = Adg  A - P (g-1 dg) ;                               (11)

     (x) = [p, q]  =     ( � g)(x) = [p, gp-1(q)] .

In the last formula,  is the left G-action on X and gp is the only element of G such that
g  P (p) = [p, gp] in P �AdG G. For our purposes the most relevant facts about these
gauge transformations is that they preserve the Ka�hler metric on A � (E), as well as the

energy functional E(A, ) and the vortex equations. In particular, if (A, ) is a solution

of the vortex equations, then so is (A � g,  � g) for any g  G.

The right action of G on the manifold A�(E) induces linear maps from the Lie algebra

G to the tangent spaces T(A,)(A � (E)). These maps correspond to the infinitesimal
gauge transformations and are explicitly given by

     C(A,) : 0(M ; gP ) - 1(M ; gP )  (Vert)                     (12)

      = aea - ( DA , -a ^(e^a) ) .

Here DA is the covariant derivative on gP  M induced by the connection A on P , and,

as explained before, e^a is the vector field on X induced by ea  g and the left action of

G on X. Using the inner products on G and on the tangent space to A � (E), one can
also consider the adjoint linear maps C(A,) = CA  C. A standard calculation shows
that these are given by

     CA : 1(M ; gP ) - 0(M ; gP )                                (13)

      - -(gM )�( � - � + [A, �] )

and

     C : (Vert) - 0(M ; gP )                                     (14)

                   V - - e2 ab (gX )rs (e^b)r V s ea ,

                      8
where the �'s are the Christoffel symbols for the Levi-Civita connection on M.
    Finally, there is a moment map for the right action of G on the Ka�hler manifold

A � (E). This is a map �A�(E) : A � (E)  G, and can be shown to be

                                 �A�(E)(A, ) = - FA - e2 �   ,

where we are using the inner product on G to identify this space with a subspace of G.
Notice that the second vortex equation (8b) is exactly the vanishing condition for this
moment map.

3.2 Basic differential forms

Here we will informally define some basic "coordinate" functions and differential forms on

the infinite-dimensional manifold A � (E), which is our space of fields. As we will see,

the definition of these forms depends on a choice of a local trivialization of the bundle

P  M and of a point x in the domain of this trivialization. This just means that the

forms can be tensored with sections of other appropriate bundles in order to define global

sections of a bigger bundle over the space of fields.

    More concretely, one proceeds as follows. Let s be a local trivialization of the bundle

P over a domain U in M. Then given a connection A  A and a section   (E), this
trivialization allows us to pick local representatives sA = Aa� dx� ea and (. . . , ^r, . . .)
for A and ; just as in (3) and (4). Now, keeping fixed the trivialization s, the point
x  U, and the indices a, � and r, the maps A  A�a(x) and   ^r(x) are actually
smooth functions on A and on an open set of (E), respectivelly. (This is the open set of
sections  such that the representative ^(x) has values in the domain of the chart {ur}
of X.) Using the exterior derivative d~ on the manifolds A and (E), we can thus define

the 1-forms

�a(x) = d~ [A�a(x)]            1(A)                  (15)

r(x) = d~ [^r(x)]              1(open set of (E)) .  (16)

It follows from the definition that, acting on the tangent vectors   TAA and V  T(E)
of (10), these forms give

�a(x) [ ] = �a(x) ,                                  (17)

r(x) [V ] = V r(x) .

                              9
These trivialization-dependent forms can be combined to define the fields

        = �a  dx�  ea and                                                          (18)

         =  r  ^                          (      )  ,                              (19)
                                             ur

which are global sections of the bundles

       2(A � M )  gP - A � M                           and

       T (E)  Vert - (E) � M ,

respectively. Here Vert is the pull-back of Vert  E by the natural evaluation map

        : (E) � M - E , (, x)  (x) .                                               (20)

Having in mind the expressions (17), it is also clear that the operators CA and C of (13)
and (14) can be written as

       CA = - (gM )� (DA)a� ea                         and                         (21)

       C = - e2 ab (gX )rs (e^b)r s ea ,

where

       (DA)a� = �a - � a + [A , �]a .                                              (22)

3.3 The G-equivariant complex

Using the differential forms defined above, let us now look into the G-equivariant complex

of the manifold A � (E). This will lead to the definition of the BRST operator Q.

For the sake of clarity we first recall a finite-dimensional example, for instance the

G-equivariant complex of X in the Cartan model [3, 10]. This complex is defined as the

space

       G(X) := (S�(g)  �(X))G

of G-invariant elements in the tensor product of the symmetric algebra S�(g) with the
de Rham algebra �(X). The differential operator acting on this space is defined to be
dC = d - ea  -e^a, where d is the exterior derivative on X, {ea} is the basis of g dual
to the basis {ea} of g, and -e^a are the vector fields on X induced by ea and the right
G-action. Notice also that, for any   �(X) and v  g,

       (ea  -e^a ) [v] = -vae^a  = C(v) ,                                          (23)

                                             10
where C : g  (T X) is the linear map induced by the right G-action on X.

    In the case of the infinite-dimensional manifold A � (E) with right G-action, this
picture becomes the following. The G-equivariant complex �G(A � (E)) is the space of
G-invariant sections of the bundle

           S�(G)  �(A � (E)) - A � (E) ,                                     (24)

where the first factor in the tensor product is the trivial bundle over A � (E) with fibre
S�(G), and the second factor is the exterior bundle of the base. The appropriate analog
of the differential dC, which will be specified below, is then what is usually called the
BRST operator Q.

    To define more explicitly the operator Q we start by introducing the elements a(x) 
G, which are defined by

           a(x) [v] = va(x)  for any v = va(x) ea  0(M ; gP ) .              (25)

These elements depend on the choice of local trivialization, but can be combined to define

the field

                              = a(x) ea ,                                    (26)

which is a global section of the bundle

                             G  gP - M .

Now, having in mind the definition of dC, it is clear that the analog Q must act on
functions on A � (E) just like d~, the exterior derivative. It must also annihilate a(x),

just as dC annihilates ea. Thus

           Q A�a(x) = �a(x) ;                Q a(x) = 0 ;                    (27)

           Q ^r(x) = r(x) .

Furthermore, using expressions (12), (17) and (25), one has that for any v  0(M; gP ),

           C(v) �a(x) |A = (DAv)�a (x) = (DA)a�(x) [v] ,
           C(v) r(x) | = -va(x) e^ar  ^(x) = -a(x) e^ra  ^(x) [v] .

So it follows from the definition of dC, (23) and the identity d~2 = 0 that

           Q �a(x) = -(DA)�a(x) ;                                            (28)

           Q r(x) = a(x) e^ra  ^(x) .

                                         11
Just as the Cartan operator dC, one has that Q2 = 0 when acting on G-invariant sections
of the bundle (24). When acting on other sections, such as the Aa�(x), Q2 is just like an
infinitesimal gauge transformation parametrized by .

4 The topological action

The aim of this section is to write down an expression for the action of the topological
gauged sigma-model. The approach is a practical one: we introduce the necessary fields,
explain what calculations should be performed, and spell out the final answer in (38) and
(39). As explained in the Introduction, underlying our calculations there is a more fun-
damental geometrical picture, which justifies the numerous apparently arbitrary choices
made here. For more details on this geometrical picture we refer the reader to Appendix
A and the reviews [8, 5].

    The conventions used here are the following. The greek indices �, ,  . . . and , ,  . . .
refer to real and complex charts, respectivelly {x� : 1  �  2m} and {z : 1    m},
on the manifold M. The latin indices r, s, t . . . and i, j, k . . . refer to real and complex
charts, respectivelly and {ur : 1  r  2n} and {wj : 1  j  n}, on the manifold X.
The relations between the real and complex coordinates are the usual ones

z = x2-1 + ix2        and  wj = u2j-1 + iu2j .

Just as in the real case of Section 3, the complex charts on M and X induce complex
coordinates and forms on A � (E). These are related to the real ones by

^jC = ^2j-1 + i^2j ;  (AC)a = (AC)a� = (A2a-1 - iAa2)/2 ;  (29)
jC = 2j-1 + i2j ;      (C)a = (C)a� = (2a-1 - i2a)/2 .

In the future we will omit the subscript C and use the type of indices to distinguish real
from complex; as for the charts, � and r means real,  and j means complex, etc.

    Regarding the Ka�hler geometry of M and X, we always work with the holomorphic
tangent bundles, not the complexified ones. The hermitian metric h is related to the real
metric and the Ka�hler form by

h = h� dz  dz� = g - i  .

                      12
The hermitian (Levi-Civita) connection satisfies

                 =                              =  h� (h�)        ,
     z  z                            z                      z

and the curvature components are

R�� = -�h� + h� (h�) (�h�) .

The type of indices used distinguishes whether we are working on M or on X.

    Having stated the conventions, we will now construct the topological action. Firstly
we need to introduce several new fields, the so-called antighosts. These are the fields

ba��(z),                          ca(z),        dj� (z ),  a(z),

of respective ghost number -1, -1, -1 and -2, and their partners

Ba��(z),                          C a(z ),      Dj� (z ),  a(z),

of respective ghost number 0, 0, 0 and -1. The BRST operator Q acts on these fields
according to the rules

Q ba�� = Ba�� ;                                    Q Ba�� = fbac b bc�� ;

Q ca = Ca ;                                        Q Ca = fbac b cc ;

Q dj� = Dj� - ijk k di� ;
Q Dj� = Rik�lm� hjk�l mdi� - kj lDk�l + a(e^a)jkdk� ;

Q a = a ;                                          Q a = fbac b c ;          (30)

where the fbac are the structure constants of the Lie algebra g. A geometric interpretation
of the antighost fields and of this Q-action is given in Appendix A. Here we only remark
that the relations

Q b = B , Q c = C , Q d = D - � � � and Q  = 

should be regarded as defining the fields B, C and D. In particular, it is the field D that
depends explicitly on the metric of the manifold X, not the operator Q. In fact, Q is a
geometric operator that only depends on M and on the G-manifold X.

                                            13
    As is usually the case with cohomological field theories, the action for our model will
be Q-exact, i.e. will be of the form

                                   I = Q,

where  is the so-called gauge fermion. This gauge fermion can be split into two parts

                     = localization + projection ,                                     (31)

which play different roles in the geometric interpretation of the action. Moreover, in

cohomological field theories there is a fairly standard procedure to construct explicit

expressions for the gauge fermions. This is reviewed for example in [8]. Going through

that procedure in the case of our gauged sigma-model, one gets at the end


                                  i ( c ,                    2i
       loc  =  � i ( d , �A )  �    2e     FA + e2�    )  �  e   (  b  ,  FA0,2  )  +

               + t(b, B ) + t(c, C ) + t(d, D) ;

       proj = - i (  , CA + C ) ;

where in the first expression t is an arbitrary positive parameter and there are two possible
choices of signs. The pairings (�, �) are the natural inner products on the respective spaces.
Explicitly, using complex coordinates,

                 ( d , �A ) = 2 e dj� (�A)k� h� hk�j ,                                 (32)
                                                         M                             (33)
                                                                                       (34)
               ( c , FA + e2 �   ) =       ca (FAb + e2bc �c  ) ab ,

                                      M

                 ( b , FA0,2 ) = 2 e       M  ba�� (FA)c�� h� h� ac ,

and the expressions for (c, C), (d, D) and (b, B) are analogous. Rewritting the operators
C of (21) in complex coordinates, we also have that

(  , CA + C ) =     a ab e - 4h� (DA)b � - e2 bc hjk� (e^c)j k ,                       (35)

                 M

where

                    (DA)a� =  a + fbac Ab c .                                          (36)

                                      14
    The final step is to go from the gauge fermion to the Lagrangian, and this is just

a computational matter. One acts with the operator Q on  and integrates out the

auxiliary fields B, C and D. A few important intermediary stages in this calculation are

the following. The section FA can be written in real and complex coordinates as

                      FAa   =   1  g�  g    �  (FAa)  =  2 m[ h� (FAa)� ] ,
                                2

where

       FAa  =  1  (FAa)�   dx�     dx  =    e [ (FAa) dz  dz  + (FAa)� dz  dz� ] .
               2

So

                                Q FAa = 4 m [ h� (DA)a� ] .

Using the definition of moment map,

                                Q (�c  ) = m [ hjk� (e^c)j k ] .

Furthermore, using the holomorphy of the vector fields e^a and the properties of the her-
mitian connection  on X, one gets that

       Q [ (�A)j� hjk� ] = ((A)0,1)j� + a� (e^a)j hjk� + (�A)j� hj�l kl m m .

In this last expression

                  [ (A)0,1 ]j� = �j + Aa� k (e^a)kj + kj l (�^k) l                        (37)

is the anti-holomorphic part of the connection A on the bundle Vert  M induced

by A and the hermitian connection on X. All throughout the calculation one should also
bear in mind that functions on X such as hjk� or (e^a)j depend implicitly on , because
they are to be evaluated at the point ^(x), with x  M. This implies for example that

                                Q hjk� = (lhjk�) l + (�lhjk�) l .

    At the end of the calculation, what we get for the localization part of the action is

       Iloc    =  1     �A      2  +    1   FA + e2�     2  +e22   FA0,2    2             (38)
                  4t            M      2e2               M                  M

                   i ( d , (A)0,1 + a� dz�  e^a )             2i   (  b  ,  (DA)0,2  )  
                                                              e

                   i             ca m 4 ab h� (DA)b� - e2hjk� (e^a)j k         -
                        2e
                               M

                  - t ( b , [, b] ) - t ( c , [, c] ) +

                  + 2t         Ri�jk�l di� dj� k l h� + e a (e^a)ik di� dj� hk�j h� ,

                            M

                                               15
where (�, �) are the natural inner products of (32)-(34), and the norms � M come from
these inner products. In the expression above we have already integrated out the fields
B, C and D. Observe that, up to a factor, the bosonic part of Iloc is equal to the classical
energy minus the energy T[] (see expression (6)). This quantity is minimized exactly by
the vortex solutions.

    The calculations for the projection part of the action give

        Iproj = - i (  , CA + C ) +                                   (39)

                   + i a e 4 ab h� ( fbac b c - (DADA)b � )
                                 M

                   + e2 hjk� (e^a)j (e^c)k c + e2 hjk� (e^a)jl l k ,

where the first term is similar to (35) and

        (DADA)b� = �(DA)b + fcbd Ac (DA)b .

5 Observables I -- definition

5.1 The homomorphism O

After having defined the field content and Lagrangian of our theory, the next natural
step is to find an interesting set of observables whose correlation functions we would like
to compute. The purpose of this section is then to define one such a set. Observables
are by definition Q-closed elements of �G(A � (E)) -- the equivariant complex of the
space of fields. In this section, roughly speaking, we will define one observable for each
given element of �G(X) -- the equivariant complex of X. The construction presented
here just combines into a single formalism the constructions of observables given in [15]
for topological Yang-Mills and in [16] for sigma-models coupled to gauge fields.

Consider the trivial extension of the G-action on A � (E) to the product manifold

A � (E) � M, and denote by �G(A � (E) � M) the associated G-equivariant complex.
Recall that, as a vector space, this complex is just the space of G-invariant sections of the

bundle

        S�(G)  �(A � (E) � M ) - A � (E) � M .                        (40)

                                             16
The first step towards defining our set of observables will be to construct a homomorphism

of complexes

                        O : �G(X) - �G(A � (E) � M ) .                                   (41)

This construction involves the sections ,  and  defined in (26), (18) and (19), respec-
tivelly, as well as the new sections

                               F : A � M - 2(M )  gP                                     (42)

                               (A, x) - (FA)a(x) ea

and

                   D : A � (E) � M - 1(M)  Vert                                          (43)

                               (A, , x)           -     (dA ^)j (x)     ^(      )  .
                                                                            wj

In these formulae FA is the curvature of the connection A, and dA is the covariant
derivative of expression (4). Notice also that both  and D can be regarded as sections
of the "bigger" bundle

                 �(A � (E) � M)  Vert - A � (E) � M ,                                    (44)

while ,  and F can be regarded as sections of

              S�(G)  �(A � (E) � M )  gP - A � (E) � M .                                 (45)

    The homomorphism O can now be defined as follows. Let  be any element of the
complex G� (X) = [S�(g)  �(X)]G. It can be locally written as

                   =     1     a1���akr1���rl (u)   a1  � � � ak  dur1   � � �  durl  ,  (46)
                        k! l!

where u  X and the coefficients a1���akr1���rl are symmetric on the aj's and anti-symmetric
on the rj's. Then the section O  �G(A � (E) � M) is defined by the local formula

O(A, , x)     =   1     (a1 ���ak r1 ���rl    ^)   k                          l
                 k! l!
                                                     ( +  + FA)aj              ( + dA^)ri , (47)

                                                  j=1                       i=1

where, on the right hand side, we have omitted the dependence on x  M.

                                                   17
    It is not obvious a priori that the homomorphism O is globally well defined. This
is because the local components ( +  + F )a, ( + dA^)r and a1���akr1���rl  ^ depend
on the choice of trivialization of P , which determines the trivializations of gP and E.
Furthermore, one should also check the invariance of O under the G-action on the bundle
(40). We will now sketch how all this is done.

    Consider a gauge transformation g  G. It can be locally represented by maps g^ :
U  G, where U is a domain in M. One needs to compute the transformation rules of
the components ( +  + F )a and ( + dA^)r under the action of g. Notice as well that,
since a local gauge transformation is equivalent to a local change of trivialization of P
(determined by the transition function g^), these rules coincide with the transformation
rules of the various components under change of trivialization of P .

    Let us start with the fields ,  and F , which are sections of the bundle (45). The left
G-action on this bundle is induced by the coadjoint action on G, the pull-back action on
�(A � (E) � M), and the usual action on gP . Using the respective definitions one can
compute that, under the action of g  G, the components of the fields transform as

a(x)  (Adg^(x)-1 )ba b(x) ;         F a(x)  (Adg^(x)-1 )ab F b(x) ;
�a(x)  (Adg^(x)-1 )ba �b (x) .

On the other hand, the local sections ea(x) of gP transform as

                ea(x)  (Adg^(x))ba eb(x) .

This makes apparent the following two facts. Firstly, regarding g^ as a transition function,
the sections ,  and F defined by (26), (18) and (42) are well defined, i.e. are trivial-
ization independent. Secondly, regarding g^ as a local gauge transformation, the sections
,  and F are G-invariant.

    The remaining fields  and D are sections of the bundle (44). The left G-action on this
bundle is induced by the pull-back action on �(A � (E) � M) and the push-forward
action on Vert. Using the respective definitions one can compute that, under the action
of g  G, the components of these fields tranform as

         r~(x)  (dg^(x)-1 )rs~  ^(x) s(x) ;
         Dr~(x)  (dg^(x)-1 )rs~  ^(x) Ds(x) ;

where the tilde over the index r allows for a possible change of chart on the target X. On

the other hand the local sections of Vert transform as

(g-1  �  )x  (       )    (dg^(x))rs~  (g-1 � )(x)      (           )  .
                u~r                                             us

                                18
As before, this makes apparent that  and D are globally well defined as sections of
the bundle (44), and that, moreover, they are G-invariant. Finally, substituting all the
transformation rules into expression (47), which defines O, one can compute that

                          (g � O)(A,,x) = (Og^(x)�)(A,,x) = (O)(A,,x) .

Here the notation g^(x) �  refers to the natural G-action on S�(g)  �(X), and in the
last equality we have used that, by assumption,  is G-invariant. As before, this shows
at the same time that O is well defined and G-invariant.

    Up to now we have only established that the map O of (41) is well defined. Since the
claim is that O is a homomorphism of complexes, we must also show that it intertwines
the differential operators.

    By definition, the differential operator on the G-equivariant complex of A � (E) is
the operator Q, presented in Section 3. Thus for the trivial extension of the G-action to
A�(E)�M, the differential operator on the complex �G(A�(E)�M) is dM +Q, where
dM denotes the exterior derivative on M regarded as acting on forms over A � (E) � M.
Calling dC the usual equivariant differential on �G(X), our aim is to show that

                                          OdC = (dM + Q) O

for all  in �G(X). This implies in particular that O induces a homomorphism of coho-
mology groups HG� (X)  HG�(A � (E) � M). Having in mind the definition (47) of O,
the first step is to see how dM + Q acts on the fields , , F ,  and D. This computation
requires the formulae of (27) and (28). After some algebra and several cancelations one
gets

(dM + Q) ( +  + FA)a = - dx� [A�,  +  + FA]a ;
    (dM + Q) ( + dA^)r = ( +  + FA)a(e^a)r - Aa s(e^a)r ( + dA^)s .

This computation also uses the identity

Aa Ac (se^ra) e^cs                       =   1  [A, A]a  e^ar  ,
                                             2

which follows from the usual formula [e^a, e^c]r = -fabce^b. Applying these formulae to the
definition (47) of O, a rearrangement of terms shows that

(dM + Q) O = OdC + Aa Oea� ,

                                         19
where ea �  refers to the representation of g on S�(g) � �(X) induced by the right
G-action on this space. Since by assumption   G� (X) is G-invariant, we have that
ea �  = 0, and so the result follows.

5.2 Natural observables

Observables of our topological field theory are, by definition, Q-closed elements of G� (A�
(E)). Thus an observable determines a cohomology class in HG�(A � (E)). Making use
of the homomorphism O defined above, it is now straightforward to construct a large set
of observables for our theory. This construction goes just as in references [15, 16].

    Let   G� (X) be any equivariantly closed form, and consider its image O 
G� (A � (E) � M), which is (dM + Q)-closed. Decomposing O according to the form

degree on the M factor, one can write

                                     O = O(0) + � � � + O(2m) ,

where the restriction of O(j) to each slice (a, A, ) � M is a j-form. Moreover, decom-
posing the identity

                                             (dM + Q) O = 0

according to the form degree on the M factor, one gets the descent equations

dM O2m = 0 ,           0  j  2m - 1 ,
 dM Oj = - Q Oj+1 ,
         0 = Q O(0) .

Now let  be any j-dimensional homology cycle in M, and define

W (, ) :=    Oj         G� (A � (E)) .                         (48)


As usual, it follows from the descent equations and Stokes' theorem that W (, ) is Q-

closed, so it is an observable. Moreover, the cohomology class of W (, ) in HG�(A�(E))
only depends on the classes of  and  in HG� (X) and Hj(M), respectively.

                 20
6 Observables II -- "universal" construction

6.1 The universal construction

In the last section we saw how to associate with each equivariantly closed form   G� (X)
another closed form O  G� (A � (E) � M). As we will see later, the form O can then
be "projected down" to a form in (A � (E))/G � M by, roughly speaking, multiplying
it by e-Iproj and performing a certain path integral. This construction corresponds to the
"quantum" way of obtaining the topological invariants.

    In this section we will describe an alternative "universal" construction that, also
roughly speaking, associates directly with each  a certain differential form on the quo-
tient space (A � (E))/G � M. This construction corresponds to the more traditional
geometrical approach to the invariants. We will then spend most of the time establishing
a result that will later allow us to relate these two constructions. (This result is formula
(51), and if the reader is willing to accept it, the subsections 6.2 and 6.3 can be skipped.)

    Besides acting on A � (E), the group of gauge transformations G also acts on the
principal bundle P . This action is effective and commutes with the natural G-action on
P . Thus there is a natural action of the group G � G on the product space A � (E) � P .
Now let V be any G-invariant open subset or submanifold of A � (E) where G acts freely.
Then the action of G � G on V � P has no fixed points, and in the commutative diagram

V � P ---3 (V � P )/G


1      4               (49)

V � M --- V/G � M
                   2

all the quotient maps are principal bundles. More specifically, 1 and 4 are G-bundles,
whereas 3 and 2 are G-bundles. We will see later that there are natural connection
forms   1(V � M; G) on the bundle 2 and   1((V � P )/G; g) on the bundle 4.

    At this point recall the evaluation map  : (E) � M  E defined in (20). Since
elements of (E) can be identified with G-equivariant maps P  X, the evaluation map
 can be identified with a map (E) � P  X, and this can be trivially extended to

                                      ~ : A � (E) � P - X .

   21
It follows straightforwardly from the definitions that ~ is G-equivariant and is constant
on the G-orbits in A � (E) � P . Thus, restricting to V, ~ induces a G-equivariant map

^ : (V � P )/G - X.

Hence given any equivariantly closed form   �G(X), we get by pull-back another
equivariantly closed form ^   G� ((V � P )/G).

    Now it is true on general grounds that the equivariant cohomology of the total space

of a principal bundle is isomorphic to the de Rham cohomology of the base space of the

bundle. An explicit isomorphism may be constructed by choosing a connection on the

bundle and applying the Weil homomorphism [3, 8]. In our present problem, we can use

the connections  and  to define Weil homomorphisms

w : G� ((V � P )/G) - �((V � P )/G)G-basic  �(V/G � M )  (50)

w : G� (V � M ) - �(V � M )G-basic  �(V/G � M ) .

The aim of this section is to show that

w(^ ) = w(O)                                             (51)

as differential forms on the moduli space V/G � M. This result is important for the iden-
tification of the invariants obtained by quantum field theory methods, with the invariants
obtained by more traditional geometrical approaches.

Remark. In Section 7 we will take V to be the space of solutions of the vortex equations,
and it is not always true that G acts freely on this space. In fact, in the special case of pure
Yang-Mills, this never happens, and there one is forced to work with framed connections
and deal with the reducible instantons. In the case of our gauged sigma-model one can
hope that in some instances this problem will be less acute. This is because a gauge
transformation that preserves the connection A in (A, )  A � (E) may not preserve
the section , and so the G-stabilizers will in general be "smaller". This is confirmed
in some examples in Section 7.2. This problem nevertheless still requires a more careful
study.

6.2 The natural connections  and 

The purpose of this subsection is to describe the natural connection forms  and  men-
tioned in the discussion above. We will also give some formulae for the curvature forms of

                                                       22
these connections. The presentation is rather summarized, and most of the calculations
are omitted.

    We will start with the connection . As described in Section 3, the right G-action on
V induces operators

C(A,) = CA + C : G - T(A,)V .                                                      (52)

Using the G-invariant metrics on V and G, one then defines the adjoints

C(A,) = CA + C : T(A,)V - G ,                                                      (53)

and C can be regarded as a 1-form on V with values in G. Since the action of G on V is
free, the maps C(A,) are injective. Moreover, since the kernel of C(A,) is the orthogonal
complement to the image of C(A,), the linear map

C(A,)C(A,) : G - C(A,)(T(A,)V )                                                    (54)

is an isomorphism. One can therefore define a G-valued form  on V by the formula
                                  (A,) = C(A,)C(A,) -1  C(A,) .

The G-equivariance of this form follows from the G-invariance of the metrics on V and G.
Since it is also clear that (A,)  C(A,) = idG, one concludes that  is a connection form
for the bundle V  V/G. This form can be trivially extended to a G-valued form on the
product V � M, which we also call . This extension is a connection form for the bundle
2 : V � M  V/G � M.

    Now we denote by H and F , respectivelly, the horizontal distribution and the curva-
ture form on V determined by the connection . It is clear from the definition of  that
H is just the orthogonal complement in T V to the image of C(A,). As for the curvature
F , which is a G-valued 2-form on V, one can compute that

F(A,)(a1 + V1 , a2 + V2) = (d~)(A,) (a1 + V1 , a2 + V2) =
                                  = - 2 (CC)-1 { [e2 ab (gX )ts V1r V2s (e^b)tr +
                                        +(gM )� (a1)c (a2)d� fcad ] ea}

for any horizontal vectors ai + Vi  H  T(A,)V  TAA  T(E). The vertical vectors
in T V are of course annihilated by F .

23
    Having dealt with , we now describe the connection  on the bundle 4. For this we
start by recalling the injective linear map

                           I : k(M ; gP ) - k(P ; g)

determined by the formula

(P )p (Y1, . . . , Yk) = [ p , I() (Y1, . . . , Yk) ]   (gP )P (p) .

Here  is any form in k(M; gP ), p is any point in P , and Yj is any vector in TpP . The
image of this map is exactly the set of G-equivariant horizontal forms in k(P ; g). In

other words, it is the set of forms   k(P ; g) that satisfy Rh = Adh   and Y  = 0
for all h in G and all Y in ker(dP ). The map I and the connection form   1(V; G)
allow us to define a form I    1(V � P ; g) by the formula

(I  )(A,,p)(a + V + Y ) = I[ (A,)(a + V ) ] |p               g,

where a + V is any vector in T(A,)V  TAA  T(E) and Y is any vector in TpP .
    Besides I  , there is another natural form in 1(V � P ; g), which is actually a

connection form on the bundle 1. This is the form  defined by the formula

(A,,p)(a + V + Y ) = Ap(Y )                             g.            (55)

Thus we can form the combination  + I  , which is a g-valued 1-form on the manifold
V � P . A more careful study of this form, which we omit here, then shows that  + I  
descends to a form on the quotient (V � P )/G, i.e.

                            + I   = 3                                 (56)

for a unique   1((V � P )/G; g). Moreover, one can also show that this natural form
 defines a connection on the bundle 4, as desired.

    Now denote by F the curvature of the connection , which is an element of 2((V �
P )/G; g). A computation using (56) shows that

(3 F)(A,,p)(Y1, Y2) = (FA)p(Y1, Y2)                                   (57)
(3 F)(A,,p)(a1 + V1, a2 + V2) = I( F(A,)(a1 + V1 , a2 + V2) ) |p
(3 F)(A,,p)(a + V, Y ) = I(a)p [Y ]

                           24
for any horizontal vectors aj + Vj  H  T(A,)V and Yj  HA  TpP .
    What we really need for the next subsection, however, is the pull-back of 3 F by any

local section of the bundle 1, and this is what we will now compute. Let s : U  P be
a local section of P over a domain U  M. It determines a local frame of gP by

x - eb(x) := [s(x), eb]  (gP )x

for all x  U and eb in a basis of g. Any form  in k(M; gP ) can then be locally written
as  = b(x) eb(x), and it follows from the definition of the map I that

b = s I()b for all b = 1, . . . , dim g .                                           (58)

In particular we have that, for any v  TxU and any a  1(M; gP ),
              I(a)s(x) [ (ds)x(v) ] = abx(v) eb(x) = (�b  dx�)(A,,x)(a, v) eb(x) ,

where in the last term we regard a as an element of TAA. Thus considering (57), (58)
and the fact that FA and F(A,) are horizontal forms, we get that

(s3 F )(A,,x)(v1, v2) = (sFA)x(v1, v2)                                              (59)
(s3 F )(A,,x)(a1 + V1, a2 + V2) = F(A,)(a1 + V1 , a2 + V2) |x
(s3 F )(A,,x)(a + V, v) = (�  dx�)H(A,,TxM ) (a + V, v)

for any aj + Vj  T(A,)V and vj  TxM . In this formula the symbol

(�  dx�)HT M

denotes the composition of the form �  dx� on V � M with the projection of vectors

T (V � M ) = ker(d2)  H  T M - H  T M ,                                             (60)

i.e. the horizontal part of �  dx� with respect to the connection  on the bundle 2.
By an abuse of notation, we have also used the same symbol for the section s and its
trivial extension s : V � U  V � P . The forms s3F  2(V � U ; g) that we have just
calculated will be essential in the next subsection to establish the identity (51).

25
6.3 Comparing the two constructions

The aim of this subsection is to justify equality (51). This equality is the fundamental
relation between the "quantum" approach of Section 5 and the universal construction of
6.1.

    Start by considering the Weil homomorphisms (50), and regard the forms w(^ )
and w(O) as basic forms on (V �P )/G and V �M, respectivelly. Since both these forms
descend to V/G � M, the commutativity of diagram (49) implies that (51) is equivalent
to

                                       3 w(^ ) = 1 w(O) .

It is enough to establish this identity locally, so all we have to do is to show that

                         w(O) = s3 w(^ ) ,

where s : V � U  V � P is the local trivialization of 1 described at the end of the last
subsection.

    Now let the equivariant form  be as in (46), so that

       ^   =       1     ( a1���akr1���rl   ^ )   a1  � � � ak  (^ dur1)   � � �  (^ durl)  .
                  k! l!

By definition of the Weil homomorphism, this form is taken to

w(^ )  =    1     ( a1���akr1���rl  ^ )    Fa1   � � �  Fak      (^ dur1)hor  � � �  (^ durl)hor  ,  (61)
           k! l!

which is a G-basic form on (V � P )/G. Here the subscript "hor" means the horizontal
part of the forms with respect to the connection .

    Now in general, for any form  in 1(X), we have that
                                  (^ )hor = ^  - a (^ )[ea] ,

where ea is the vector field on (V � P )/G associated to ea  g by the right action of G.
But from the G-equivariance of the map ^ it is also clear that

                                            (d^ )(ea) = -(e^a) ,

                                                 26
where e^a, as usual, is the vector field on X associated to ea  g by the left G-action on
X. Hence one obtains that

                           (^ )hor = ^  + a (e^a)  ^ ,

and therefore

               3 (^ )hor = ~  + (3a) (e^a)  ~ .                            (62)

On the other hand, it follows from (56), (55) and (58) that

                           s 3 a |(A,,x) = (sAa)x + (aA,) .

Moreover, tautologically,

                                 ~  s (A, , x) = ^(x) ,                    (63)

where ^ : U  X is the local representative of   (E) with respect to the trivialization
of E induced by s. Thus the pull-back by s of equation (62) is

               s 3 (^ )hor |(A,,x) = s ~  + (e^a)  ^ [sAa + a] ,           (64)

where on the right hand side we have omitted the dependence on x  M.

    The equation above will now be applied to the particular case where  is the local
1-form dur. Denoting by d~ the exterior derivative on A � (E) � M, and noting that
d~ coincides with the equivariant differential dM + Q when acting on functions, it follows

from (63) that

               s ~  dur |(A,,x) = d~[^r(x)] = (d^r)x + r(x) | .

On the other hand, considering the horizontal projection (60), one can compute that the
component in H  T M of the 1-form r(x)  T(A,,x)(V � M ) is given by

[r(x)]HT M (a + V + v) = r(x) a + V + v - C(A,)  (a + V + v) =
                                  = [ r(x) + e^rb  ^(x) b ] (a + V + v) .

Hence it follows from (64) that

               s 3 (^  dur)hor |(A,,x) = (dA^r)x + [r(x)](HA,,TxM ) .      (65)

                                 27
With the formula above at hand, it is now possible to compute the pull-back by 3  s of
equation (61). In fact, making use of (59) and (65), we have that

s 3 w(^ ) |(A,,x)  =   1     a1 ���ak r1 ���rl   ^(x)                        (66)
                      k! l!

                             (F aj + �aj  dx� + F aj )(A,,x)       HT M


                        1jk

                                  (ri + dA^ri )(A,,x)  HT M

                                                                ,

                             1il

where we have also used that F(aA,), (FAa)x and (dA^r)x, regarded as forms in (�A,,x)(V �
M), are already horizontal with respect to the projection T (V � M)  H  T M.

    The final step is to compare the expression above with the definition of the equivariant
form O. It is then clear that (66) can be obtained from (47) by substituting a  F a
and taking the H  T M-component of the resulting form. But as is well known, this is
precisely the definition of the Weil homomorphism

w : �G(V � M ) - �(V � M )G-basic

associated with the connection  on the bundle V � M  V/G � M. Thus the right hand
side of (51) coincides with w(O), as desired.

7 Invariants and localization

7.1 Correlation functions and localization

The purpose of this final section is to study the correlation functions of the observables
W (, ) defined in Section 5. As is usual in topological field theory, the importance of
these correlation functions stems from the fact that they are expected to be invariant under
deformations of the metric and complex structure of the manifolds M and X. This means
that they essentially only depend on the G-action and on the differentiable/symplectic
structures of M and X, and hence are potentially able to distinguish inequivalent man-
ifolds and G-actions. Another important property of the correlation functions is that,
while they are defined by a certain path-integral over the space of all fields, their com-
putation can be reduced to an integral over the moduli space of solutions of the vortex
equations.

                                  28
    We point out that the methods of this first subsection are standard, as the localization
arguments that apply to topological Yang-Mills, for instance, can be straightforwardly
transposed to our gauged sigma-model; at least at a heuristical level. Thus, besides the
original references [15, 16], we follow closely the review [8, ch.14].

The correlation functions of the observables W (, ) are of the form

Z(1, 1, . . . , k, k) :=  D(b, c, d, , , , A, , , ) e-Iloc-Iproj     W (i, i) . (67)

                                                                  i

Since the path-integral measure is assumed not to depend on the metric and complex

structure on M and X, the dependence of Z on these quantities is contained in

                          Iloc + Iproj = Q (loc + proj) .

Therefore under a small deformation g� of the metric on M, for example, the change
Z is given by the path-integral of

          e Q -Iloc-Iproj (loc + proj)             W (i, i) ,

                                                i

where we have used that the W s are Q-closed and that the differential Q does not de-

pend on g� (see the remarks after (30)). This last path-integral represents the vacuum
expectation value of a Q-exact quantity, and by standard heuristical arguments it van-

ishes [15, 16]. One therefore expects the correlation functions Z to be invariant under

deformations of the metric and complex structure of M and X (see however Section 7.3).

    On the other hand there is the localization argument, which reduces the path-integral
defining Z to an integral over the moduli space of vortex solutions. In order to state this
result, let V denote the space of solutions of the vortex equations, and assume that G acts
freely on V. The basic localization result, as stated in [8], asserts that

Z=                 D(A, , , , , , )               Wi  E (cok O  V) e-Iproj

       (A,)V                                    i

=                  w(Wi)  E(cok O/G  V/G) .                                    (68)

       V/G i

We now explain the notation in this formula. O is the linear operator defined at each

(A, )  A � (E) by

O(A,)  =  (~ s)(A,)         1     C(A,)  :  T(A,)(A � (E))  -     W(A,)  G ,   (69)
                              2e

                                            29
where we use the notation of Appendix A. At each vortex solution (A, )  V, identifying
the target of O with the space

0,1(M ; Vert)  0,2(M ; (gP )C)  +0 (M ; gP )  0(M ; gP ) ,

a calculation shows that this operator can be written in local coordinates as

                  [ (A)0,1]j� + a� e^aj  dz�    ^(      )      
                                                    wj

            1        (DA)a - (DA)a       (dz�  dz�) ea         
              2e                                               

O(A,)  =             4 h� (DA)a� + e2 ab hjk� e^bk j             .             (70)

            1     m                                        ea  
              2e                                               

                     4 h� (DA)a� + e2 ab hjk� e^bk j           

            -1    e                                        ea
              2e

The first three components of O(A,) correspond to the operators obtained from the
linearization of the three vortex equations at the point (A, )  V. The last com-
ponent of O(A,), roughly speaking, measures the orthogonality of a tangent vector in
T(A,)(A � (E)) to the G-orbit of (A, ). The cokernels of the operators O(A,) for all
(A, ) in V define a vector bundle cok O  V. Taking the quotient by G one obtains
another vector bundle, and the symbol E(cok O/G  V/G) denotes the Euler class of this
bundle. Finally, the symbol w represents the Weil homomorphism (50). More precisely,
what we mean in formula (68) is

                                     w [ W (, ) ] := w[ O ] .


    Thus we see that the correlation functions Z can be computed by integrating certain
closed differential forms over the moduli space V/G. Moreover, using the results of Section
6, we have that

Z=                   w (^ i)  E(cok O/G  V/G) .                                (71)

          V /G i i

Comparing this formula with the definition of the Hamiltonian Gromov-Witten invari-

ants in [7], one recognizes that, in the case where cok O = 0, our correlation functions
essentially coincide with those invariants.

7.2 The moduli space of vortex solutions

As was seen above, the moduli space V/G is of the utmost importance for the calculation
of the correlation functions of our theory. In this subsection we will report some properties

                                                       30
of this moduli space. The majority of the results here comes from references [13, 6, 7]. As
in those references, we will restrict ourselves to the case where M is a compact Riemann
surface.

    For the general gauged sigma-model the moduli space V/G is not necessarily a smooth
manifold. When it is a smooth manifold, or at least in each smooth region, the tangent
space T[A,]V/G can be identified with the kernel of the operator O(A,). In the light of the
discussion below (70) this identification is very natural, since a tangent vector belongs to
ker O(A,) exactly if it satisfies the linearized vortex equations and is perpendicular to the
G-orbit of (A, ). More generally, to decide whether V/G is or is not smooth, one should
study in detail the linearized equations and the orthogonality condition, i.e. the operator
O. In fact, the kernel, cokernel and index of O are the relevant objects that characterize
the local structure of V/G.

    Following this cue, the first important result is the virtual dimension of the space V/G.
This is given by the real index of the Fredholm operator O, and coincides with the actual
dimension of V/G on smooth regions. Notice that, for M a Riemann surface, the second
component of this operator in (70) should be discarded, as the vortex equation FA0,2 = 0 is
trivially satisfied. The computation of the index of O was performed in references [6, 13],
and the result is

                 ind O(A,) = dim ker O(A,) - dim cok O(A,)
                               = (dimC X - dim G) (2 - 2g) + 2 cG1 (T X), [] .

In this formula g is the genus of M, c1G(T X) is the equivariant first Chern class of T X --
which belongs to HG2 (X; Z) -- and [] is the class in H2G(X; Z) determined by the section
. In practice we have that c1G(T X), [] equals the first Chern number of the bundle
Vert  M .

    Observe that different connected components of the moduli space V/G may have dif-
ferent dimensions, depending on the class []. In fact, in formulas such as (67) and (68),
one usually fixes a class B  H2G(M; Z), and then only integrates over the fields  such
that [] = B. In the case of the vortex solutions this defines a subset VB  V which can
be shown to be G-invariant.

    Still regarding the smoothness of the moduli space, the best one can usually do is
to guarantee this smoothness on the (typically open) subset V  V of the so-called

                                                       31
irreducible solutions. In fact, over the irreducible solutions, a sufficient condition for this
smoothness is the vanishing of the cokernel of O(A,), or in other words the surjectivity of
this operator. We will now give the definition of irreducible solution and state a condition
that is equivalent to the surjectivity of O(A,). Both of these come from Reference [7].

Definition. A solution (A, ) of the vortex equations is called irreducible if there exists
a point z  M such that the stabilizer of ^(z)  X is trivial, and the intersection
g^^(z)  JX g^^(z) is zero. (Here g^^(z) denotes the image of the linear map g  T^(z)X
associated to the G-action on X.) We note that the subset V  V of irreducible vortex
solutions is G-invariant, and that G acts freely on it.

Proposition 7.1. Consider the operator

  L(A,) : 0(M ; Vert)  0,1(M ; (gP )C) - 0,1(M ; Vert) ,
                             ( V , �a(z) dz�  ea ) - (A)0,1 V + �a(z) dz�  (e^a)^(z)

where (A)0,1 is as in (37). Then O(A,) is surjective if and only if both C(A,) and the
adjoint L(A,) are injective.

Remark. An immediate consequence of the results above is that if L(A,) is injective for
all (A, )  V, then the moduli space V/G has a natural structure of smooth manifold.

Remark. The statement of proposition 7.1 is a bit stronger than proposition 4.8 (iii) of
[7], but follows directly from the proof presented there. More specifically, refer back to
that proof, call LC the operator

1(M ; (gP )C) - 1(M ; Vert) ,    �a(x) dx�  (e^a)^(x) ,

and L its restriction to 1(M ; gP ). Then it is enough to notice that 2(LL)0,1 =
LC (LC ) for all  in 0,1(M ; Vert). Moreover, (LC) = 0 if and only if L = L( 

JM ) = 0.

    One of the issues raised by the previous proposition is the injectivity of C(A,), the
operator in (12) that represents the infinitesimal gauge transformations. This issue is
interesting for its own sake, and also came up in the discussion below (53). In fact, notice
that C(A,) is injective if and only if the G-stabilizer of (A, ) is discrete. Regarding these
matters there exists the following result.

32
[7] Suppose that M and �-1(0) are compact, and that 0 is a regular value of � (resp. G acts
freely on �-1(0)). Then there exists a constant K > 0 such that, if e2(Vol M)  K T[],
every solution (A, ) of the vortex equations with [] = [] has a discrete (resp. trivial)
G-stabilizer.

    Here []  H2G(M; Z) is the equivariant homology class already mentioned above
(which, by the way, is the same for homotopic sections ), and T[] is the topological
energy of (7). This result means that for large enough Riemann surfaces the group of
gauge transformations acts (locally) freely on the space of vortex solutions.

    In the case of abelian actions we prove the following result in Appendix B.

Suppose that G is a torus, that M and X are compact, and that the constant
(deg P )/(e2 Vol M ) is a regular value of � (see the appendix for the definition of deg P ).
Then every solution of the vortex equations has a discrete G-stabilizer. If, furthermore,
the torus action on X has no non-trivial finite stabilizers, then the G-action on the set of
vortex solutions is free.

Remark. The last two propositions are true even if dimC M > 1. In the second one, the
condition of compact X can be very much weakened (see the remark in Appendix B); in
particular the result is still valid for linear torus actions on Cn.

Remark. Suppose that G is a n-torus, that X is compact of complex dimension n, and
that the constant (deg P )/(e2 Vol M) lies in the interior of the polytope �(X). Then it
is not difficult to show that the G-action on V = V is free and that the operators L(A,)
are injective for every vortex solution (A, ). (We omit the proof here.) According to
the discussion above, this implies the smoothness of the moduli space V/G, in agreement
with the results of [2].

7.3 About the invariants

Wall-crossing phenomena

In this subsection we want to illustrate the so-called wall-crossing phenomena for the
Hamiltonian Gromov-Witten invariants [6]. These refer to the occurrences where a finite
deformation of the parameters of the topological Lagrangian leads to a change in the value
of the invariants. This is in apparent contradiction with the argument evoked at the end

                                                       33
of 7.1 about the vanishing of the vacuum expectation value of Q-exact operators. In fact,
it will be very clear in the example below how this argument can indeed sometimes fail.

    For our illustrative example we will consider the case of a toric action on X = CPn.
Defining the constant

                       0 := (deg P )/(e2 Vol M )  g  Rn ,

it was shown in [2] that the moduli space of vortex solutions is a fixed non-empty manifold
V whenever 0 lies in the interior of the convex polytope �(X). If 0 lies outside this
polytope the moduli space is empty.

    Now suppose that we deform the moment map � by adding to it a constant   Rn.
This corresponds to a deformation of the parameters of the topological Lagrangian, and
so the heuristical arguments of Section 7.1 would seem to imply that that the correlation
functions are invariant by this deformation. In particular all the correlation functions
should vanish, since for  big enough 0 lies outside �(X), and so the integral in (68)
is over the empty set. But in Reference [13] it was computed that for X = CP1 and
0  int �(X) there is a non-zero Hamiltonian Gromov-Witten invariant, so the heuristical
argument must fail at some point. We will now see explicitly how this failure comes about.

    Take the gauge fermion  of (31) and substitute � for �+, where  is a small constant
in Rn. Then the change in Q is

                                 Q  = �ie (C, ) ,
                                                  2

and so the partition function, which is the simplest invariant, changes by

                       Z =  D(fields) ie (C, ) e-Q  .
                                                       2

Using the explicit formula for Q and integrating out the field C, the corresponding

equation of motion is              i
                                  2 2et
                       C     =           (FA   +  e2  �    )  ,

and so one recognizes that Z is just the vacuum expectation value of

      -   1              ab (FA + e2 �  )a b   =      e (Vol M)  (v, )  ,
         4et                                              4t
                       M

with                                      1
                                      (Vol M)
                          v  =  0  -             � .

                                               M

                                         34
Now, if 0 lies in the interior of �(X), then the vector v may have any orientation in Rn
as  varies, and so it is certainly possible that the expectation value of (v, ) vanishes.
However, when 0 lies in the boundary or exterior of �(X), the vector v always lies in the
same semi-space of Rn, independently of . Hence in this case the expectation value of
(v, ) cannot vanish for a generic infinitesimal deformation , and so Z will not vanish.

    We conclude that a finite deformation of � may well leave the partition function Z
invariant, but only as long as 0 remains in the interior of the polytope �(X). When
0 crosses the boundary of �(X), a jump in the value of Z is expected. This point of
0 crossing the boundary of �(X) corresponds as well to a drastic change in the ground
states of the theory, as the moduli space of vortex solutions jumps from V to the empty
set. All this is very similar to the runaway vacua phenomena in supersymmetric quantum
mechanics [8, ch. 12.6].

    The picture that seems to arise is that, in general, the space of parameters of the
topological lagrangian (and these include metrics, complex structures, ...) is divided into
different regions by internal walls. A small deformation of the parameters will leave the
correlation functions invariant, but when a wall is crossed the correlation functions may
jump.

Adiabatic limit and Gromov-Witten invariants

In this final paragraph we would like to mention another interesting property of the
vortex equations, namely the correspondence between pseudo-holomorphic curves in the
symplectic quotient X//G and solutions of the vortex equations in the adiabatic limit
e  . We assume here that G acts freely in �-1(0), so that the symplectic quotient
X//G := �-1(0)/G is in a natural way an almost Ka�hler manifold.

    In the limit e   the vortex equations (8) for M a Riemann surface become

�A = 0 ; �   = 0 .                            (72)

It is not difficult to show that any solution of these equations descends to a pseudo-
holomorphic map � : M  X//G, and that gauge-equivalent solutions descend to the
same map. Furthermore, any pseudo-holomorphic curve � lifts to a solution of (72) on
the bundle P = �(�-1(0)  X//G), and any two different lifts are gauge equivalent
[9]. (In passing, the connection A of the lift is the pull-back by � of the connection A�

on �-1(0)  X//G determined by the G-invariant metric on �-1(0).) One can therefore

35
identify the moduli space of solutions of (72) with the space of pseudo-holomorphic curves
on X//G such that P  �(�-1(0)  X//G).

    On the other hand one would expect that for e big enough there should be some sort of
close correspondence betweeen the solutions of the vortex equations (8) and the solutions
of (72). In particular the Hamiltonian Gromov-Witten invariants of X -- which study the
moduli space of vortex solutions -- should be able to tell something about the Gromov-
Witten invariants of X//G -- which study the space of pseudo-holomorphic curves. These
matters were studied in detail in Reference [9], and under suitable conditions on M and
X, one such relation was established. In the particular case where X is a complex vector
space acted by a torus and X//G is a toric variety, a very strong correspondence had been
previously established in [12].

Acknowledgements. I would like to thank Prof. N. S. Manton for his encouragement,
Professor Sir Michael Atiyah for a useful discussion, and Dr. David Tong for pointing out
references [12, 17]. I am supported by `Fundac�~ao para a Ci^encia e Tecnologia', Portugal,
through the research grant SFRH/BD/4828/2001.

Appendices

A The localization bundle

In this appendix we sketch how the gauged sigma-model can be fitted into the geomet-
rical method for obtaining topological Lagrangians. We will have in mind the abstract
description of this method given in [8, ch.14], so only the features that are particular to
our model will be described here.

    One starts by considering the vector bundle over the space of fields W  A � (E),
whose fibre at a point (A, ) of the base is

                 W(A,) = 0,1(M ; Vert)  +0 (M ; gP )  0,2(M ; (gP )C) .  (A1)
In this formula 0+(M ; gP ) is the subspace of 0(M ; gP ) defined by

                         +0 (M ; gP ) := (2(M ; gP )) + 0(M ; (g0)P ) ,

where  is the operator of (9), and (g0)P is the sub-bundle of gP constructed from the

            36
AdG-invariant subspace

                                       g0 := span{�(X)}  g.

We note in passing that, in the case where X is a point and dimR M = 4, the space W(A,)
defined above is isomorphic to the space of anti-self-dual gP -valued forms on M. This is
important because we want our construction to contain topological Yang-Mills theory as

a special case.

    The vector bundle W has a natural section defined by


                                                 1                                  2
                   s (A, ) =           �A ,        2e   (FA     +  e2  �     )  ,  e    FA0,2   .          (A2)

Notice that the zero set of s is the set of solutions of the vortex equations, and that the
squared norm of s is the non-topological term of the energy functional (6).

    The group of gauge transformations G has a natural right action on the total space of
the bundle W which lifts the usual G-action on A � (E). The section s is equivariant
with respect to these actions, and so defines a section s� of the quotient bundle

                                       W/G - (A � (E))/G .

This last bundle over the moduli space of fields is what is usually called the localization
bundle. Although our Lagrangian and observables are ultimately meant to be defined on
this bundle, it is easier to work "upstairs" on the bundle W, and then include a "projection
term" that brings all these quantities down to the quotient bundle (see [8]).

    In Section 3 the fields Aa (z) and ^j(z) were introduced as local coordinate functions
on the space A � (E), which is the base of the bundle W. Here we introduce the odd

fields

                                dj�(z) ,         ca(z)          and          ba��(z) ,

that should be regarded as odd coordinates on the fibre of W, or to be more specific,
respectivelly on the spaces

         0,1(M ; Vert) ,                     +0 (M ; gP )            and        0,2(M ; (gP )C) .

So  for  example,  if    =  �j  dz�    ^(        )  is  an  element    of  0,1(M ;      Vert),  then  the  function
                                             wj
dj�(z) evaluated at  gives

                                           dj�(z) [] = �j (z) .

                                                            37
    In Section 3 the operator Q was defined as the differential of the G-equivariant complex
of A � (E). Here we extend that picture and define Q to be the differential of the G-
equivariant complex of the total space of the bundle W. When acting on functions, Q
obviously coincides with the exterior derivative d~ on W, so

                   Q ba��(z) = d~[ba��(z)] =: Ba��(z)
                   Q ca(z) = d~[ca(z)] =: Ca(z)
                   Q dj�(z) = d~[dj�(z)] =: Dj�(z) - ijk  ^(z) k(z) di�(z) .

The rightmost equalities define the fields B, C and D, which are odd 1-forms on W.
Using the explicit (local) expression for the action of G on W, and, as in Section 3, the
definition of the differential Q of the G-equivariant complex, one can then compute what
the action of Q on B, C and D is. The result is given in the expressions (30).

    The bundle W  A � (E) that we have been discussing has a natural connection ~ .
This connection is trivial on the sub-bundles corresponding to the last two summands of
(A1), and, on the sub-bundle corresponding to the first summand, it is naturally induced
by the Levi-Civita connection of X. More explicitly, let S be any section of W and,
according to (A1), decompose it as

                                       S = S1 + S2 + S3 ,

where, locally,

                 S1(A, )           =   [  (S1 )j� (z )  ](A,)  dz�    ^(      )
                                                                          wj

                 S2(A, ) = [ (S2)a(z) ](A,) ea

                 S3(A, ) = [ (S3)a��(z) ](A,) (dz�  dz�) ea .

Then the connection ~ acts on each of these terms as                      dz�      ^(      )
                                                                                       wj
             ~ S1 = d~[ (S1)j�(z) ] + jkl  ^(z) l(z) (S1)k�(z)
             ~ S2 = d~[ (S2)a(z) ] ea
             ~ S3 = d~[ (S3)a��(z) ] (dz�  dz�) ea .

Notice also that this can be rewritten as

~ S  =           S  [Dj� ]  dz�    ^(      )  +  S[Ca] ea      +      S[Ba��] (dz�  dz�) ea .
                                       wj

                                                 38
    As mentioned in Section 4, once the field content of the theory is established and the
Q-action on the fields is known, there is a fairly standard procedure to construct a Q-exact
Lagrangian for the topological theory. The abstract method is very well described in [8],
and the necessary calculations are described in Section 4.

B A proof from Section 7

In this appendix we want to prove the third proposition of Section 7.2. The assumptions
are that G = T n, M and X are compact, and that the constant (deg P )/(e2 VolM) is a
regular value of the moment map �. Here

                    deg P := - FA                   g  Rn ,

                                                M

and it is not difficult to check that this constant does not depend on the connection A.
    For the first part of the proposition, it is enough to show that for every vortex solution

(A, ) the operator C(A,) = CA + C of (52) is injective. So let   G  C(M ; Rn) be
an infinitesimal gauge transformation such that

                    CA() = DA = d = 0 ;
                    C() = -a(x) ^(e^a) = 0 .

The first equation tells us that  is constant. Calling   Rn the constant value of , the
second equation tells us that ^ |^(x) = 0, where ^ is the vector field on X induced by .
Using the definition of moment map, this means that ^(x)  X is a critical point of the

function H := �,  for all x  M. Now denote by Br the connected components of the
critical set Crit(H)  X. These components are preserved by the torus action, since �
is T n-invariant and the orbits of the action are connected. One can therefore define the

associated bundles

                    Er := P �T n Br ,

which are connected subsets of E = P �T n X. Since (M)  E is connected, the discussion
above implies that (M) is contained in one of the Er's, say E0. Thus

                    �  (M )  �(E0) = �(B0) .

                    39
Now by the lemma below, �(B0) is a convex polytope in Rn, and so the constant

 deg P   =     -1      FA     =    1     �
e2 VolM     e2 VolM              VolM
                     m                 M

certainly belongs to this polytope. This finally shows that, unless  = 0, the constant
(deg P )/(e2 VolM) is a critical value of �, and the proof of the first part is complete.

    For the second part of the proposition, assume furthermore that all the G-stabilizers
in X are either trivial or a subtorus of T n. To obtain at the end a contradiction, suppose
that there existed a non-trivial gauge transformation g  C(M; T n) that preserved the
pair (A, ). The condition that g preserves the connection A implies that g is a constant
map, as is well known, and we call its image also g  G \ {id}. The condition g() = ,
on the other hand, implies that

                                     (M )  P �T n Fix(g)  E ,

where Fix(g)  X is the set of fixed points of the map g, and so is T n-invariant. But
the initial assumption on the G-stabilizers in X then implies that each point of Fix(g)
is preserved by a full subtorus of T n, and in particular is a critical point of �. Thus

                                     (M )  P �T n Crit(�)  E .
Now, the proofs of theorem 5.47 and lemma 5.53 in [11] show that

         Crit(�) =           Crit(H)

                     Zn\{0}

and that each Crit(H) -- the critical set of H -- is a proper complex submanifold of X.
Thus defining E := P �T n Crit(H), we have that

            (M)               E ,                                              (B1)

                     Zn \{0}

and that each E is a proper complex submanifold of E equipped with the integrable
complex structure induced by A (see Section 2.2 in [2]). On the other hand, since �A = 0,

also (M) is a complex submanifold of E (see [13]). This implies that the intersections

(M)  E are analytic subvarieties of (M), and so it follows from (B1) and Baire's
category theorem that there exists at least one  = 0 such that (M)  E. Finally,
arguing just as at the end of the proof of the first part, one concludes that the constant
(deg P )/(e2 VolM) must be a critical value of �, which contradicts the assumptions.

                     40
Lemma. The image �(B0) is a convex polytope in Rn.
Proof. Along the proof above we saw that Crit(H) and B0 are compact Ka�hler subman-
ifolds of X that are preserved by the T n-action. Thus the restriction of � to B0 is a
moment map for the T n-action on B0. The lemma then follows directly from the well
known convexity theorem.

Remark. Inspecting the proof of the proposition presented here, it is clear that the
assumption of compact X is only needed to guarantee the validity of the lemma above.
Thus as long as the images by � of the connected components of the critical sets Crit(H)
are convex sets, the proposition is still valid, even if X is not compact. This happens for
instance with the linear torus actions on Cn .

References

 [1] M.F. Atiyah and L. Jeffrey : `Topological Lagrangians and cohomology '; J. Geom.
      Phys. 7 (1990), 119�136.

 [2] J.M. Baptista : `Vortex equations in abelian gauged sigma-models'; to appear in
      Commun. Math. Phys., math.DG/0411517.

 [3] N. Berline, E. Getzler and M. Vergne : `Heat Kernels and Dirac Operators'; Springer-
      Verlag, Berlin, 1992.

 [4] D. Birmingham, M. Blau, M. Rakowski and G. Thompson : `Topological field theory';
      Phys. Rep. 209 (1991), 129�340.

 [5] M. Blau : `The Mathai-Quillen formalism and topological field theory'; J. Geom.
      Phys. 11 (1993), 95�127.

 [6] K. Cieliebak, A.R. Gaio and D. Salamon : `J-holomorphic curves, moment maps, and
      invariants of Hamiltonian group actions'; Internat. Math. Res. Notices 16 (2000),
      831�882.

 [7] K. Cieliebak, R.A. Gaio, I. Mundet i Riera and D.A Salamon : `The symplectic
      vortex equations and invariants of Hamiltonian group actions'; J. Symplectic Geom.
      1 (2002), 543�645.

                                                       41
 [8] S. Cordes, G. Moore and S. Ramgoolam : `Lectures on 2D Yang-Mills theory, equiv-
      ariant cohomology and topological field theories'; hep-th/9411210.

 [9] R. Gaio and D. Salamon : `Gromov-Witten invariants of symplectic quotients and
      adiabatic limits'; math.SG/0106157.

[10] V. Guillemin and S. Sternberg : `Supersymmetry and equivariant de Rham theory';
      Springer-Verlag, Berlin, 1999.

[11] D. McDuff and D. Salamon : `Introduction to symplectic topology '; 2nd edition,
      Oxford University Press, New York, 1998.

[12] D. Morrison and M. Plesser : `Summing the instantons: quantum cohomology and
      mirror symmetry in toric varieties'; Nuclear Phys. B 440 (1995), 279�354.

[13] I. Mundet i Riera : `Hamiltonian Gromov-Witten invariants'; Topology 42 (2003),
      525�553.
      I. Mundet i Riera : `Yang-Mills-Higgs theory for symplectic fibrations '; Ph.D. Thesis,
      UAM (Madrid), April 1999, math.SG/9912150.

[14] I. Mundet i Riera and G. Tian : `A compactification of the moduli space of twisted
      holomorphic maps'; math.SG/0404407.

[15] E. Witten : `Topological quantum field theory'; Comm. Math. Phys. 117 (1988),
      353�386.

[16] E. Witten : `Topological sigma models'; Comm. Math. Phys. 118 (1988), 411�449.
[17] E. Witten : `Phases of N=2 theories in two dimensions'; Nucl. Phys. B403 (1993),

      159�222.

                                                       42
