# 2006 Vortex equations in abelian gauged sigma models

**Source:** `04_2006_Vortex_equations_in_abelian_gauged_sigma_models.pdf`

---

arXiv:math/0411517v2 [math.DG] 10 Nov 2005                                                                                              DAMTP-2004-64

                                                        Vortex equations in abelian
                                                                gauged -models

                                                                                 J. M. Baptista 

                                                            Department of Applied Mathematics and Theoretical Physics 
                                                                                     University of Cambridge

                                                                                     June 2004

                                                                                     Abstract

                                                We consider nonlinear gauged -models with Ka�hler domain and target. For a special
                                            choice of potential these models admit Bogomolny (or self-duality) equations -- the so-
                                            called vortex equations. Here we describe the space of solutions and energy spectrum of
                                            the vortex equations when the gauge group is a torus T n, the domain is compact, and
                                            the target is Cn or CPn. We also obtain a large family of solutions when the target is a
                                            compact Ka�hler toric manifold.

                                                e-mail address: [email redacted]
                                                address: Wilberforce Road, Cambridge CB3 0WA, England
Contents

1 Introduction                                                    2

2 Review of the model                                             5

2.1 The energy functional . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

2.2 The vortex equations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.3 Complex gauge transformations . . . . . . . . . . . . . . . . . . . . . . . . 10

2.4 Torus principal bundles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

3 A simpler case: Cn with T n-action                              12

3.1 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

3.2 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

4 The 2nd vortex equation as an imaginary-gauge fixing condition  17

4.1 Main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

4.2 Proof of theorem 4.1 and corollary 4.3 . . . . . . . . . . . . . . . . . . . . 19

4.3 Proof of theorem 4.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

5 The vortex solutions for target CPn                             23

5.1 The main result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

5.2 Proof of theorem 5.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

5.3 Proof of theorem 5.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

6 Constructing solutions on quotient targets                      35

6.1 Induced solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

6.2 Proof of lemma 6.2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

7 Solutions for target a compact toric manifold                   40

7.1 The canonical Ka�hler toric manifolds . . . . . . . . . . . . . . . . . . . . . 40

7.2 A family of non-trivial solutions . . . . . . . . . . . . . . . . . . . . . . . . 43

8 Some comments                                                   48

A Proof of propositions 5.4 and 5.5                               50

B Complex structures from connections                             55

                                      1
1 Introduction

Among the most general bosonic theories without gravity are the so-called nonlinear

gauged -models, also known as general Yang-Mills theories with matter. These theories

have been studied in the theoretical physics literature for a long time now, and have

recently entered the mathematics literature as well. To define them we need roughly the

following data: two Riemannian manifolds M and F , a fibre bundle E over the base M

with typical fibre F , and a group G acting on F by isometries. The fields of the theory

are then a section  : M  E of the bundle and a G-connection A. The energy functional

is defined as

               E(A, ) =     1  FA 2 +          dA 2 + V () ,  (1)
                            2
                         M

where FA is the curvature of A, dA is a covariant derivative and V () is a potential
term. Notice that when the bundle E is trivial the section  can be regarded as a map

 : M  F , and so for A = 0 this energy reduces to the usual one for (non-gauged)

-models.

In this paper we will be concerned with the case where M and F are complex Ka�hler

manifolds and the action of G on F is holomorphic and hamiltonian. In this case there is

a very special choice of potential V , namely

                         V () = 2 �   2 ,                     (2)

where � is a moment map for the G-action on F . This potential is special for two reasons,
and it is a remarkable (though not uncommon) fact that they occur simultaneously.

    One reason is that with this choice the theory admits a supersymmetric extension, at
least when M is an appropriate euclidean space. This is an important fact well known
in the physics literature (see for example [15]), but we will not make any use of it here.
The other reason is that with the choice (2) the energy functional admits Bogomolny
equations, or in other words has a self-duality property. This fact appears to be less well
known in the physics literature, at least when the -model is nonlinear, and apparently
was first found in [27, 13]. When M is a Riemann surface these Bogomolny equations are

                                            �A = 0
                                              FA + �   = 0 ,

and can be generalized to any Ka�hler M. In this context these equations are usually
called vortex equations, because when F = C and G = U(1) they reduce to the usual

                               2
vortex equations of the abelian Higgs model. The solutions of these equations are exactly
the global minima (within each topological sector) of the energy functional E. In fact
they are also BPS states of the supersymmetric theory, although we will not justify this
here. Hence it is usually interesting to know how many solutions these equations admit
up to gauge transformation, i.e. to describe the space of gauge equivalence classes of
vortex solutions. For instance in the abelian Higgs model (F = C and G = U(1)) this
was originally done by Taubes for M = C [31] and by Bradlow for M compact Ka�hler
[7]. In the more difficult non-abelian case considerable progress has been made (e.g.
[8, 9, 32, 3, 27, 22, 17]), especially in the case where F is a vector space, G a unitary
group and M a Riemann surface.

    As a recent mathematical application, the vortex equations have been used to define
the so-called Hamiltonian Gromov-Witten invariants [27, 13, 14, 28]. This is described
from a topological field theory point of view in [4].

    In this paper we will study the space of solutions of the vortex equations for M any
compact Ka�hler manifold and G an abelian torus. At the end it turns out that we are
able to completely describe this space in the case where G = T n and F = Cn or F = CPn.
In some other cases a (big) family of non-trivial solutions is found, namely when F is
a compact Ka�hler toric manifold. The results obtained show an interesting interplay
between the space of vortex solutions and the geometry of the moment polytope �(F )
obtained from the torus action on F . An informal description of these results is included
in the comments of section 8. For the rest of this introduction we will just give a brief
description of the content of each section.

    Section 2 is just a review of the model, where we try to carefully describe all the
notions involved in the definition of the energy functional and of the equations. Since this
nonlinear version of gauge theory on fibre bundles with arbitrary fibres (as opposed to
vector space fibres) is not the most standard, we felt that this may be useful. At the end
of the section we also recall some standard facts about complex gauge transformations
and torus principal bundles, which will be necessary further ahead.

    In the short section 3 we give the space of solutions and energy spectrum of the vortex
equations in the case G = T n and F = Cn. When n = 1 these are the classical vortex
equations, defined on line bundles over Ka�hler manifolds, and the solutions were described
by Bradlow in [7] and by Garc�ia-Prada in [18]. When n > 1, following work of Schroers
[29], Yang has computed the space of solutions in the case where the base is the complex

                                                        3
plane or a compact Riemann surface [33, p. 121]. The results contained in this section are
for n  1 and any compact Ka�hler base. Their derivation follows quite straightforwardly
from work in [3]. In the rest of the paper we will concentrate on the more delicate case
where F is a compact manifold.

    In section 4 we study the relation between the spaces of solutions up to real gauge
transformations and up to complex gauge transformations. In fact, since the target F is
Ka�hler, the usual G-gauge transformations can be extended to GC-gauge transformations.
Then the first vortex equation is invariant under the GC-transformations whereas the
second equation is invariant only under the G-transformations. Thus it makes sense to
ask if, given a solution of the first equation, there exists a (unique) GC-transformation
that takes it to a solution of the full equations. This question was addressed by Mundet
i Riera in [27], and a general "stability" criterion was found. This criterion, however,
is generally not easy to evaluate in practice. In section 4 we find that for G = T n and
for suitable conditions on F this criterion is hugely simplified, and a direct evaluation
becomes possible. In particular, when F is Ka�hler toric, the answer to the question is
essentially yes, and so there is an almost perfect correspondence between the real and
complex moduli problems. The precise results are stated in section 4.1.

    In section 5 we determine the space of solutions and energy spectrum of the vortex
equations for G = T n, F = CPn and any compact Ka�hler M. The results obtained
generalize the ones in [27] and [30], where the authors determine same quantities in the
case where M is a Riemann surface and n = 1. The calculations in this section require
the results of section 4. The main results are stated in 5.1 and the proofs are contained
in 5.2 and 5.3.

    Section 6 is mainly preparatory. We study some general properties of the vortex
equations under quotients of the target manifold F . Although we deal with a general
group G, the results will be mainly applied to G = T n.

    In section 7 we use the results of sections 4 and 6 to find non-trivial solutions of the
vortex equations for G = T n and F a compact Ka�hler toric manifold. This family is big
enough so that when F = CPn it coincides with the full space of solutions calculated in
section 5. It is therefore natural to ask if, for the other compact toric F , the solutions
exhibited in this section also exhaust the set of vortex solutions.

    Finally in section 8 we make a few informal comments about the results obtained. It
may be helpful for the interested reader to have a look at those before delving into the
technicalities of the theorems.

                                                        4
2 Review of the model

2.1 The energy functional

The data we need to define the -model are the following.

    � Two Ka�hler manifolds M and F , with respective Ka�hler forms M and F .

    � A connected compact Lie group G, with Lie algebra g, and an Ad-invariant positive-
       definite inner product , on g.

    � An effective hamiltonian left action  of G on F such that, for every g  G, the
       transformations g : F  F are holomorphic, and a moment map for this action
       � : F  g.

    � A principal G-bundle P : P  M.

We remark that, in the fullest generality, the complex structure on F need not be assumed
integrable, but we will assume that here. Using the elements above one can define the
associated bundle E = P � F , which is a bundle over M with typical fibre F . It is
defined as the quotient of P � F by the equivalence relation (p, q)  (p � g, g-1 � q), for all
g  G. The bundle projection E : E  M is determined by E  (p, q) = P (p), where
 : P � F  E is the quotient map. As a matter of notation, we will sometimes denote
the equivalence class (p, q) simply by [p, q].

Definition. The convention used here is that a moment map for the action  of G on
(F, F ) is a map � : F  g such that

  (i) d (�, ) =  F in 1(F ) for all   g, where  is the vector field on F defined by
       the flow t  exp(t).

  (ii) g� = Adg  � for all g  G, where Adg is the coadjoint representation of G on g.

If a moment map � exists, it is not in general unique, but all the other moment maps are
of the form � + a, where a  [g, g]0  g is a constant in the annihilator of [g, g]. Recall
also that under the identification g  g provided by an Ad-invariant inner product on g,
the annihilator [g, g]0 is taken to the centre of g.

                                                        5
    The fields of the theory are a connection A on the principal bundle P and a smooth
section  of E. Calling A the space of such connections and (E) the space of such
sections, we define the energy functional E : A � (E)  R0 of the -model by

E(A, ) =                    1   FA 2 +  dA 2 + a2 �   2   M[m] ,  a  R>0.         (3)
                            a2
                         M

In this formula, as throughout the paper, m is the complex dimension of M, and we use
the notation M[k] := Mk /k! for any k  N. In particular M[m] is the metric volume form
on M.

    The various terms under the integral sign have the following meaning. FA is the
curvature of the connection A. It can be regarded as a locally defined 2-form on M
with values in the Lie algebra g. The norm FA 2 is then the natural one, induced
simultaneously by the Ka�hler metric on M and by the inner product , on g. In the
third term of (3), the norm � on g comes from the inner product , , which induces
an inner product on g. By the Ad-invariance of , and by the G-equivariance of the
moment map �, the function E  R0 determined by (p, q)  �(q) 2 is well defined;
the third term is then the composition of this function with .

    As for the second term, its description is a little longer, since one should first explain
the meaning of the covariant derivative dA. This is an extension of the usual notion of
covariant derivatives on vector bundles. We start by considering the differential of the
quotient map, d : T P � T F  T E. A connection A on P induces a horizontal distribu-
tion HA on P . Defining HA = d(HA), it is not difficult to show that the restrictions

dE : HA - T M and d(p,q) : TqF - ker(dE)(p,q)                                     (4)

are isomorphisms, and in particular we get the splitting

                                T E = HA  ker dE .                                (5)

The covariant derivative of a section  : M  E is then defined as the composition

                     dA : T M --d- T E = HA  ker dE -p-r-oj2 ker dE ,

where proj2 is just the projection. Notice that the image of dA is in the tangent space to
the fibres of E, which are isomorphic to F . Thus when F is a vector space, the canonical
isomorphism TvF  F allows us to regard dA as a map of vector bundles T M  E,
that is a section of T M  E, which is the usual notion of covariant derivative on a vector

                                        6
bundle. The norm dA 2 is defined in the usual way, using the metric gM on M and the
metric gF -- transported by the second isomorphism of (4) -- on ker dE.

    Finally notice that the constant a2 can be absorbed by rescaling the inner product on
g.

2.2 The vortex equations

Having explained the meaning of the energy functional (3), we will now see how to ma-
nipulate it in order to get Bogomolny equations. First of all, using the isomorphisms (4)
and the splitting (5), one can transport the complex structures JM and JF of M and F ,
respectively, as well as the Ka�hler metrics gM and gF , to the tangent bundle T E, thus
defining a complex structure and a metric on T E by

          J(A) = JM  JF and g(A) = gM  gF .                                 (6)

These depend on the connection A. Because the metrics gM and gF are Ka�hler, J(A) is

always compatible with g(A), and so (E, J(A), g(A)) is an almost-Hermitian manifold.
Using this complex structure on E and the one on M, one obtains a splitting dA =
A + �A by the usual formulae

�A  =  1  (dA  +  JF    dA     JM )  =  1  proj2    (d + J(A)    d    JM )  (7)
       2                                2
       1
A   =  2  (dA  -  JF    dA     JM ) .                                       (8)

For later convenience we also record here the local (i.e trivialization-dependent) formulae
for dA and �A. Let s : U  P be a local section of P over a domain U in M. Since

E = P � F is an associated bundle, this determines a trivialization of E|U by

               U � F  E|U , (x, q)  [s(x), q] .                             (9)

With respect to these trivializations a section  of E can be locally identified with a
map ^ : U  F , and a connection A on P can be identified with the connection form
sA =   1(U ; g). Then the covariant derivatives dA and �A in (T M   ker d E)

are locally given by

          (dA)q = (d ^)q + (l)q l|^(q)              qU ,                    (10)
          (�A)q = (� ^)q + (l)q0,1 l|^(q)

                                     7
which are 1-forms on TqM with values in T^(q)F . In these formulae {l} is any basis for
g, the l are the vector fields on F described in the definition of moment map (section
2.1), and we have decomposed  = l l.

    We now come to the basic fact of the theory. This was first obtained in [27] and, for
M a Riemann surface, in [13].

Theorem 2.1 ([27] , [13]). For any connection A  A and any section   (E),

E (A, ) = T[] +                            1  FA  +  a  �      2+2   �A        2  +  4   FA0,2  2  M[m] ,  (11)
                                           a                                         a2
                                     M

where the term

                T[] =                      [E ]      M[m-1]   -  1   B2(FA  ,  FA)     M[m-2]              (12)
                                                                 a2
                                        M

does not depend on A, and only on the homotopy class of .

Remark. As is usually the case with these Bogomolny-type manipulations, there is an
alternative formula for E(A, ) which gives rise to the anti-Bogomolny equations. This

formula can be obtained from the one above by changing the sign of the first term of T[],
substituting �A for A, and changing the plus to a minus sign inside the first squared

norm. The proof of [27] is still applicable, with minimal changes.

Corollary 2.2 ([27] ,[13]). Within each homotopy class of the sections  we have that
E(A, )  T[], and there is an equality if and only if the pair (A, ) in A � (E) satisfies
the equations

                                              �A = 0                                                       (13a)
                                              FA + a2 �   = 0                                              (13b)
                                              FA0,2 = 0 .                                                  (13c)

These first order equations are usually called vortex equations.

    Apart from �A, several new terms appear in (11) when compared with (3); their
meaning is the following. The operator  : (M)  -2(M) is the adjoint, with
respect to gM , of the operator   M   on (M). By well known formulae,

                FA = (M  FA) = gM (FA, M ) ,                                                               (14)

                                                           8
and so FA can be seen as a locally defined function on M with values in g, just as �  .
(More properly, they should be both regarded as global sections of P �AdG g.) Next, FA0,2 is
just the (0, 2)-component of FA under the usual decomposition 2(M ) = 2,0 1,1 0,2.

The form B2(FA, FA) can be explicitly written as

B2(FA, FA) = FAj  FAk j, k ,  (15)

where {j} is a basis of g and we have decomposed FA = FAj j; it represents the charac-
teristic class of P associated with the Ad-invariant polynomial �, � : g � g  R.

    Finally [E] is a cohomology class in H2(E), and is defined as follows. Consider the

2-form on P � F

(A) := F - d(�, A) ,          (16)

where we regard the connection A as a form in 1(P, g), in the usual sense, and (�, �) :
g � g  R is the natural pairing. The quotient map  : P � F  E is in a natural
way a principal G-bundle, and it is not difficult to check that the form (A) is invariant
under the associated G-action (p, q)  (p � g, g-1 � q) on P � F . Furthermore (A) is also a
horizontal form, in the sense that it annihilates vectors in ker d, and so (A) descends to
E, that is (A) = E(A) for some E(A) in 2(E). The form E(A) on E is sometimes
called the minimal coupling form. Now, since (A) is closed, E(A) is also closed, and it
is not difficult to show that its cohomology class in H2(E) does not depend on A. We
can therefore define [E] to be the cohomology class of the forms E(A).

Remark. There is another way to look at the class [E] on H2(E), using the Cartan

complex for the G-equivariant cohomology of F . In this context, [E] is just the image
by the Chern-Weil homomorphism of the cohomology class in HG2 (F ) determined by the
equivariantly closed form F - Xb�b  2G(F ) (see for example [5, ch. VII]) .

    Observe that the term T[] does not depend on the connection A, since the cohomology
classes E and [B2(FA, FA)] are A-independent. Furthermore, because homotopic sections
 : M  E induce the same map  : H(E)  H(M) on the cohomology [6], by Stokes
theorem T[] only depends on the homotopy class of .

    To end this subsection we state two results that, to some extent, clarify the meaning
of the first and the third vortex equations. The first proposition is well known [27]. As
for the second proposition, we relegate its proof to appendix B, since it is a bit long and,
moreover, is just a mild extension of well known calculations [24, p. 9].

                                                        9
Proposition 2.3. Let A  A be any connection and let  be a section of E. Then
�A = 0 if and only if  is holomorphic as a map (M, JM )  (E, J(A)).

Proposition 2.4. The condition FA0,2 = 0 implies that the almost-complex structure J(A)
on E is integrable. The converse is also true if at least one point in F has a discrete
isotropy group (contained in G).

2.3 Complex gauge transformations

Here we recall the notions of complexified Lie group, complexified action, and complex
gauge transformation. To any compact Lie group G one can associate a complex analytic
Lie group GC, called the complexification of G. The Lie algebra of GC can be identified
with the complexification gC = g  ig of the Lie algebra of G. Both G and g can be
naturally embedded into GC and gC, respectively, as fixed points of natural involutions
-- called conjugations -- in these spaces [11]. Furthermore, when the group G acts
holomorphically on a compact Ka�hler manifold F , this action can be canonically extended
to a holomorphic action of GC on F [20]. At a Lie algebra level this extension is defined
by

(u + iv) = u + JF v                 u, v  g ,  (17)

where we denote by v the vector field on F defined by the flow t  exp(tv), and JF is
the complex structure on F .

    This extension of the action on F allows us to define complex gauge transformations
on the bundle E = P �G F , which extend to GC the original G-gauge transformations. A
complex gauge transformation g is a section of the bundle P �AdG GC over M. The set of
these sections forms a group, denoted by GC. Each g  GC determines an automorphism
of E by the formula

[p, q]  [p, gp(q)] ,                           (18)

where  is the extended GC-action and gp is the only element of GC such that g  P (p) =
[p, gp]. If we compose a section   (E) with this automorphism of E we get another
section, which we denote by g(). Complex gauge transformations can also be made to
act on the space A of connections on P , in such a way as to extend the action of the
original G-gauge transformations. This extension is defined by the formula

g(A) = Adg  A - P (g-1�g + g�-1g�) .           (19)

10
An important fact about these complex gauge transformations is that both the first and
the third vortex equations are invariant by them, whereas the second equation is invariant
by real gauge transformations only.

    For later convenience we also record here the following standard definition.

Definition. A divisor D on M is a locally finite formal linear combination

D=     ai � Zi ,  ai  Z ,

    i

of irreducible analytic hypersurfaces Zi of M. The divisor D is called effective if ai  0
for all i. The support of D, written supp D, is the subset of M formed by the union of
the hypersurfaces Zi with non-zero coefficient ai.

2.4 Torus principal bundles

In this last subsection we will introduce some notation and recall some standard results
about T n-principal bundles used in the rest of the paper.

    Let P  M be any principal T n-bundle, let ^ be the natural action of T n on Cn,
denote by ^j the restriction of ^ to the j-th factor C in Cn, and let L^j = P �^j C be the
associated line bundle. We begin by stating a standard result, whose proof we omit.

Proposition 2.5. Given any n classes j  H2(M; Z) there is exactly one principal T n-
bundle P  M, up to isomorphism, such that j coincides with the first Chern class
c1 (L^ j ).

    This proposition shows that the correspondence P  (P ), with j(P ) = c1(L^j),
defines a bijection between the set of principal T n-bundles over M (up to isomorphism),
and the n-fold cartesian product of H2(M; Z). Now identify the Lie algebra tn with Rn
in such a way that the exponential map tn  Rn is

exp(w1, . . . , wn) = (e2iw1, . . . , e2iwn) ,  wk  R.                      (20)

With this identification, for any principal T n-bundle P  M we define

deg P = - FA M[m] ,                                                         (21)

       M

where A is any connection on P . This constant does not depend on A. In fact, having
in mind the above identification of tn with Rn, it is clear that 2i(FA)j coincides with

       11
the curvature on the base of the connection on L^j induced by A. In particular c1(L^j) =
-[(FA)j], and so it follows from (14) and proposition 2.5 that

deg P = - FA  M =                      (P )  M[m-1]               Rn .             (22)

                             M      M

We also define the constant

                           c(a, P, M ) := (a2 Vol M )-1 deg P ,                    (23)

which will appear often in the subsequent sections.

    Finally, to end this subsection, we will state a lemma necessary for section 6. Let
 : T d  T n be any homomorphism of tori. These have the general form

(g1, . . . , gd) = (. . . , 1ld (gl)al, . . .)1an ,              with al  Z .

Given a principal T d-bundle P  M, the associated bundle P  = P � T n is in a natural
way a principal T n-bundle over M. Then the following naturality property is easy to

check.

Lemma 2.6. The classes in H2(M; Z) associated with P  are a(P ) =       d      al  l(P )
                                                                        l=1

for all a = 1, . . . , n.

3 A simpler case: Cn with T n-action

3.1 Results

In this section we give the space of solutions and energy spectrum of the vortex equations
in the case F = Cn and G = T n. The results are contained in theorems 3.1 and 3.2.

One starts with the action of T n on Cn given by

(g1,...,gn) (z1, . . . , zn) = ( � � � , zk j (gj)Ckj , � � � )1kn ,               (24)

where the matrix C belongs to SL(n; Z). It is an effective hamiltonian action. Identifying
tn  Rn in the usual way (20), the general form of a moment map � : Cn  Rn for this
action is

�(z1, . . . , zn) = -  � � � , Cjk |zj|2, � � �                  + t,              (25)

                                j                    1kn

                                12
where t is any constant in Rn.
    Now consider the associated vector bundle E = P �Cn. Denoting by j the restriction

of the action  to the j-th component C of Cn, we have that

                                           E = L1  � � �  Ln ,

where Lj = P �j C is the associated line bundle. Notice that the natural hermitian
products on Cn and C induce hermitian metrics on the bundles E and Lj, because the
actions  and j are unitary. We denote by h and hj these hermitian metrics.

    Finally, an integrable connection A  A1,1(P ) induces a metric-compatible integrable
connection  (resp. j) on the vector bundle E (resp. Lj). In turn, this integrable
connection defines a unique holomorphic structure on E (resp. Lj) such that  (resp.
j) is the hermitian connection of this bundle [24]. The bundles E and Lj equipped
with these holomorphic structures will be denoted by EA and LjA. Notice that, also as
holomorphic hermitian bundles,

                  EA = LA1  � � �  LAn .                                    (26)

Recalling the constants c(P, M, a)  Rn and (P )  H2(M; Z)n defined in section 2.4, we
have the following results.

Theorem 3.1. In the setting described above, the vortex equations (13) have solutions
only if the constant c(P, M, a) is in �(Cn). When this constant lies in the interior of
�(Cn), the set of solutions can be described as follows. For each j = 1, . . . , n pick an
effective divisor Dj = i aji � Zi on M representing the homology class Poincar�e dual
to k Cjk k(P ). Then there is a solution (A, ) of (13) such that Dj is the divisor of
the zero set of j (the j-th component of  under the decomposition (26)) regarded as a
holomorphic section of LjA. This solution is unique up to gauge transformations, and all
solutions of (13) are obtained in this way.

Theorem 3.2. The topological energy (12) of any solution of the vortex equations is

T=                tk k(P )  M[m-1]  -  1   k(P  )    k(P )       M[m-2]  ,  (27)
                                       a2
              Mk

where t  Rn is the arbitrary constant in the moment map (25).

    In theorem 3.1 it is of course implicit that, if it is impossible to find a suitable set of
divisors Dj, then the set of vortex solutions is empty. Notice as well that the statement of

                  13
these results is especially simple when M is a Riemann surface, due to the isomorphism
H2(M; Z)  Z. In fact, in this case it is apparent from theorem 3.1 that the moduli space
of vortex solutions can be identified with the product of symmetric powers SN1M � � � � �
SNnM , where Nj is the integer k Cjk k(P ). If any of these integers is negative, then
the moduli space is empty. For M a Riemann surface the topological energy also reduces
to T = t � (P ). Another interesting fact regarding the topological energy is that, unlike
the CPn case of theorem 5.1, here the energy is completely determined by the bundle P ; it
does not depend on the particular solution chosen. This difference between the Cn and the
CPn cases is analogous to the fact that the degree of a line bundle completely determines
the number of zeros of a holomorphic section, but not of a meromorphic section.

    The key ingredient to prove theorem 3.1 is the following proposition, which follows
quite straightforwardly from the "stability" criterion of [3].
Proposition 3.3. Assume that c(P, M, a) lies in the interior of �(Cn), and let (A, ) 
A1,1(P )�(E) be any pair such that �A = 0 and j is not identically zero for any j. Then
there exists a complex gauge transformation g : M  (C)n, unique up to multiplication
by real gauge transformations, such that the pair (g(A), g()) is a solution of the vortex
equations.

    When the target of the -model is a compact manifold, instead of Cn, things get rather
more complicated. In the next section we will try to find results analogous to proposition
3.3 in the compact setting. For this we will use results of [2] and a more general "stability"
criterion of [27].

3.2 Proofs

The proofs below may be regarded as a warm up to the calculations of sections 4 and 5.
Nevertheless, in order to avoid repetition, we will occasionally invoke results from those
sections.
Proof of proposition 3.3. The proof is based on the Hitchin-Kobayashi correspondence
of [27, 3]. In the case G = T n and X = Cn this correspondence reduces to the following
statement.

    Given a simple pair (A, )  A1,1 � (E), there exists a complex gauge transformation
that takes this pair to a solution of (13b) iff

     v � (deg P + a2(VolM) t) < 0 for all v  Rn \ {0} such that (Cv)j  0 . (28)

                                                       14
When it exists, this transformation is unique up to composition with real gauge transfor-
mations.

    Now notice that condition (28) is equivalent to

        v � (C-1)T (c(P, M, a) + t) < 0 for all v  Rn \ {0} such that vj  0 ,

or in other words, to the condition that the constant (C-1)T (c(P, M, a) + t) lies in the set

                                          {x  Rn : xj < 0 j} .

But this is the same as demanding that c(P, M, a) should lie in the interior of �(Cn), and
this is satisfied by assumption. Thus in order to prove the proposition it is enough to
show that (A, ) is a simple pair. This can be done just as in the proof of Proposition
4.7.

Proof of theorem 3.1. The first statement of the theorem can be proved by integrating
the second vortex equation over M, just as in the proof of Theorem 4.1.

    For the rest of the theorem, assume that c(P, M, a) lies in the interior of �(Cn), and
consider the divisors Dj described in the theorem. Since

             Lj =         (L^j )Ckj ,

                   1jn

where the line bundles L^j were defined in section 2.4, we have that

PD(Dj) =     Cjk k(P ) =     Cjk c1(L^k) = c1(Lj) .

          k               k

So it follows from well known results that the divisor Dj determines a holomorphic struc-
ture on Lj together with a non-zero holomorphic section j of this bundle such that
Dj is the zero set divisor of j [19]. Denoting by j the hermitian connection of (Lj, hj)
equipped with this holomorphic structure, by construction we have that j0,1j = 0. Now,
just as in the first part of the proof of Lemma A.3, there exists a connection A on P such
that j is the connection on Lj = P �j C induced by A. So using the decomposition
(26) to define

                                      := (1, . . . , n)  (E) ,

we have that �A = (. . . , j0,1j, . . .) = 0. The existence part of Theorem 3.1 then follows
from Proposition 3.3 together with the fact that complex gauge transformations do not
change the zero set divisor of a section (see Lemma A.5).

                   15
    As for the unicity of the solutions, suppose that (A1, 1) and (A2, 2) are two solutions
of the vortex equations such that the zero set divisors of 1 and 2 are well defined and
equal. Then Lemma A.5 tells us that the components (1)j and (2)j, and therefore also
1 and 2, are complex-gauge equivalent. The unicity statement of Proposition 3.3 then
guarantees that 1 and 2 are real-gauge equivalent, as required.

    Finally, to recognize that all solutions of the vortex equations are of the kind described
in Theorem 3.1, it is enough to show that if (A, ) is a solution then the zero set divisor
of j  (LjA) is well defined, that is j is not the zero section for any j. But if this were
not true, the image �  (M) would be contained in one of the boundary faces of �(Cn),
and then integrating the second vortex equation over M one would obtain a contradiction
with the fact that c(P, M, a) does not belong to this face (see the analogous result in
Theorem 4.1).

Proof of theorem 3.2. Let (A, ) be any solution of the vortex equations. We start by
considering the 1-form on P � Cn

                           =  i     zk dz�k - (� - t) � A .
                              2
                                 k

It is not difficult to check that this form annihilates vectors in the kernel of the quotient
map  : P �Cn  E, and that it is invariant under the right action (p, v)�g = (p�g, g-1v)
of T n on P � Cn. Thus  descends to a form on E, that is  = E for some complex
1-form E on E. On the other hand, using (16), we have that

        d  =  i          dzk  dz�k - d(� � A) + t � dA = (A) + t � P FA ,
              2
                 k

where FA is the curvature form on the base M of the connection A. But by the commu-

tativity of the diagram          P � Cn --- E


                                          E

we get that on P � Cn              P --- M
                                                    P

                              P FA =  E FA ,

and so

                          d E = d  = ( E(A) + t � E FA ) .

                                      16
This implies that

                      E(A) = d E - t � E FA ,

and using Stokes theorem we get that

                   M   E(A)  M[m-1] = - t �  M  FA  M[m-1] .

The formula for the topological energy then follows from the definition (12) and the
identification j(P ) = -[(FA)j] in H2(M) given in section 2.4.

4 The 2nd vortex equation as an imaginary-gauge fix-

     ing condition

4.1 Main results

As was mentioned in section 2.3, an important fact about the complex gauge transforma-
tions is that both the first and the third vortex equations are invariant by them, whereas
the second equation is not. Hence, given a pair (A, ) that solves (13a) and (13c), it makes
sense to ask whether there is a complex gauge transformation g such that (g(A), g())
solves (13b), and therefore all the vortex equations [27]. The ideal answer would be that
such a transformation always exists and is unique up to real gauge transformations. This
would mean that equation (13b) acts as a sort of imaginary-gauge fixing condition, and
that the set of solutions of (13) up to real gauge transformations is the same as the set of
solutions of (13a) and (13c) up to complex gauge transformations.

    The purpose of this section is to study this problem when the gauge group is T n and
the target F is compact. The basic results obtained are expressed in theorems 4.1 and
4.2. As a kind of corollary we find that although the ideal answer stated above is not
in general true, it comes very close to being completely true when the target manifold
F is a "simple" one -- for example when F is toric (see corollary 4.3 and the following
remark). This will eventually allow us to compute the moduli space of solutions when
F = CPn (section 5), and to find a big set of non-trivial solutions for more general toric
F 's (section 7).

    In order to state the basic results of this section we first need to establish some
notation. The complexified torus is TCn  (C)n, and its Lie algebra is identified with

                                                       17
tn  itn  Cn in such a way that the exponential map is

exp(w1, . . . , wn) = (e2iw1, . . . , e2iwn) ,         wk  C.  (29)

The inner product on tn  Rn is just the euclidean one. For any point p in F we call Op
and OpC its T n-orbit and TCn-orbit, respectively; similarly, the real and complex isotropy
groups of p are denoted by Gp and GpC.

    Also a word about polytopes. By the convexity theorem, if � : F  tn  Rn is a
moment map for a torus action on F , which is assumed compact, its image �(F ) is a
convex polytope in Rn (see for example [2] or [26]). As a set, �(F ) is the disjoint union of
its k-dimensional open faces, or k-cells, for k = 0, . . . , dim �(F ). Thus for example �(F )

has only one open face of maximal dimension, and the 0-dimensional open faces are the

vertices of �(F ). We are now ready to state the main results of this section.

Theorem 4.1. A necessary condition for the equation FA + a2 �   = 0 to have a
solution is that the constant c(a, P, M) (c.f. (23)) lies in �(F ). If this is satisfied, let c
be the only open face of the polytope �(F ) that contains this point, and let �c denote its
closure. Then for any (A, ) solution of (13b), the image �  (M) is contained in �c and
is not entirely contained in any of the closed faces of �c \ c.

Theorem 4.2. Let (A, )  A � (E) be a pair such that, for all x in some open dense
subset of M, the conditions

  (i) OC(x)  �-1(c) =  ;

 (ii) G(x) has dimension n - dim c ;

are satisfied. Then there exists a complex gauge transformation g : M  TCn that takes
(A, ) to a solution of (13b). This transformation is unique up to multiplication by trans-
formations whose imaginary part is a constant in exp(ic).

Remark. Here we will only prove this theorem in the generic case where the constant
c(P, M, a) lies in the interior of �(F ), i.e. when dim c = n. This is the only case needed
in the subsequent sections. The proof is based on a very general criterion of [27]. For a
hint of the proof in the general case see the remark in section 4.3.

Corollary 4.3. Assume that the orbit OpC of any point p  �-1(c) satisfies �(OpC) = c.
Then, given any pair (A, )  A1,1 �(E) such that �A = 0, there exists a complex gauge

18
transformation that takes (A, ) to a solution of (13b) if and only if the image �  (M) is
contained in �c but not in any of the closed faces of �c \ c. Furthermore, when it exists,
this transformation is unique up to multiplication by transformations whose imaginary
part is a constant in exp(ic).

Remark. The condition of this corollary, namely �(OpC) = c for any p  �-1(c), is very
restrictive. It is satisfied, however, when the action is effective and dimC F = n = dimR T n.
In this case F becomes a compact Ka�hler toric manifold, and it is well known that for such
manifolds there is a one-to-one correspondence between open faces of �(F ) and TCn-orbits
in F , which is given by   �-1(). This is valid for all Ka�hler toric manifolds, not just
the canonical ones described in section 7.1.

4.2 Proof of theorem 4.1 and corollary 4.3

We begin this subsection with the proof of theorem 4.1. After establishing two auxiliary
lemmas, we end it with the proof of corollary 4.3.

Proof of theorem 4.1. Let (A, ) be a solution of (13b). Integrating this equation over
M and using (21) and (23) one has that

   (�   - c) M[m] = 0   Rn.  (30)

M

If c  �(F ), from the convexity of �(F ) it is clear that for all v  �(F ) the vectors v - c
will lie in the same open half-space of Rn. In particular the same thing happens with
the vectors �  (x) - c for all x  M, and thus it is impossible for (30) to hold -- a
contradiction.

    Now suppose that c lies in some open face  of �(F ). If  is n-dimensional, it is obvious
that �  (M)  � = �(F ). If the dimension of  is k < n, let A1, . . . , An-k be the closed
(n - 1)-dimensional faces of �(F ) whose intersection is �, and let nj be an outward
normal vector to Aj. Then, from the convexity of �(F ), one has that nj � (v - c)  0 for
all v  �(F ), and the equality holds iff v  Aj. But (30) implies that

                                         nj � (�  (x) - c) M[m] = 0 ,

                                                      xM

and so we conclude that �  (x)  Aj for all x  M. Since this is true for all j we actually
have that �  (M)  �, as required.

   19
    On the other hand, let B be any closed face of � \  -- which is also a (k - 1)-
dimensional closed face of �(F ) -- and let u be a vector normal to B, parallel to �, and
pointing outward of �(F ). Then, because c   and � is convex, one has that u�(v-c) > 0
for all v  B. In particular it is impossible that �  (M)  B, otherwise one would have
that

                                         u � (�  (x) - c) M[m] > 0 ,

                                                     xM

which contradicts (30).

Lemma 4.4. Let  be any open face of the polytope �(F ), and denote by � its closure.
Then

  (i) �-1(�) is a connected complex submanifold of F ;

 (ii) �-1() is invariant under the TCn-action.

    This lemma is a well known result. Statement (i) follows rather straightforwardly from
lemmas 5.53 and 5.54 of [26] and their proof; statement (ii) follows from Theorem 2 of
[2].

Lemma 4.5. Let  : M  E be a section of E such that �A = 0 for some connection
A  A1,1(P ). Then for any open face  of �(F ) the inverse image (�  )-1(�) is an
analytic subvariety of M.

Proof. To avoid any confusion, in this proof we will use different symbols for the moment
map � : F  Rn and its lift �~ : E  Rn. To start with, notice that � is a disjoint union
of open faces of �(F ), possibly with different dimensions, and so it follows from lemma
4.4 that �-1(�) is a complex submanifold of F which is invariant by the T n-action. It is
not difficult to check that this implies that E = P �T n �-1(�) is a complex submanifold
of E = P �T n F , where the complex structure on E is J(A). Furthermore, from the
definition �~  (p, q) = �(q) (see section 2.1), we also have that E = �~-1(�).

    On the other hand, by proposition 2.3, the section  is a holomorphic map from
M to (E, J(A)). This map is proper because M is compact, and since a section is
always an immersion, we conclude that (M) is actually a complex submanifold of E, and
 : M  (M) is a biholomorphism. It is then clear that E (M), being an intersection
of complex submanifolds, is an analytic subvariety of (M). Hence -1(�~(�)) = -1(E 
(M)) is an analytic subvariety of M.

                                                       20
Proof of corollary 4.3. We denote by () the condition "�  (M) is contained in �c
but not entirely in any of the closed faces of �c \ c". The proof of necessity is fast, due
to theorem 4.1. In fact, it follows from part (ii) of lemma 4.4 that, if a section   (E)
satisfies (), so does its entire complex gauge equivalence class. (We are using that the
closed faces of �c are themselves a union of open faces of �(F ), and so their inverse image
by � is also TCn-invariant.) The necessity of () is then a direct consequence of theorem
4.1.

    To prove the sufficiency and uniqueness statements we will use theorem 4.2. If �A = 0
and () is satisfied, by lemma 4.5 it is true that for each closed face B of �c \c, the inverse
image (�  )-1(B) is an analytic subvariety of M which is not the entire M; in particular
this set has zero measure in M. Since this is true for all the faces of �c \ c, we conclude
that (�)-1(c) is open and dense in M . Now if x  (�)-1(c), that is (x)  �-1(c),
by assumption �(OC(x)) = c. Hence on the one hand, since c(P, M, a)  c, this implies
that condition (i) of theorem 4.2 is satisfied; on the other hand, using lemma 4.6, this
implies that condition (ii) of theorem 4.2 is satisfied as well. Applying this theorem we
obtain the sufficiency and uniqueness parts.

4.3 Proof of theorem 4.2

We first derive an auxiliary lemma and then prove theorem 4.2 in the case where c(P, M, a)
lies in the interior of �(F ). At the end of the subsection we make a remark about the
proof in the general case.

    The lemma is the following. Given p  F , let p denote the only open face of �(F )
that contains the point �(p). Then by lemma 4.4 and theorem 2 of [2], the image �(OpC)
is a convex open polytope contained in p.

Lemma 4.6. Given p  F , the Lie algebra of the isotropy subgroup Gp  T n is the
subspace of tn formed by the vectors orthogonal to �(OpC). In particular Lie Gp contains
the subspace p.

Proof. Theorem 2 of [2] guarantees that the restriction of � to OpC induces a homeo-
morphism OpC/T n  �(OpC). Since the dimension of the isotropy subgroup GpC  TCn is
twice the dimension of Gp, we conclude that OpC/T n, and therefore �(OpC), have dimension
n - dim Gp. On the other hand, for any v  tn, property (i) of the definition of a moment
map (see section 2.1) implies that

                v  Image(d�)p  (v)p = 0  v  Lie Gp .

                                                       21
Since

       Image(d �)p  (d �)p(TpOpC) = T�(p) �(OpC) ,

after identifying T�(p)tn  tn we obtain that Lie Gp is contained in the subspace of tn
orthogonal to �(OpC). Comparing the dimensions, we conclude that Lie Gp is in fact equal
to that subspace.

Proposition 4.7. Theorem 4.2 is true when dim c = n.

Proof. To prove this proposition we will use the results of [2] and the Hitchin-Kobayashi
correspondence of [27]. The latter result is hugely simplified for abelian G, which is the
case that matters to us, and can be stated in the following form [27].

    Given a simple pair (A, )  A1,1 � (E), there exists a complex gauge transformation
that takes this pair to a solution of (13b) iff

       -v � degP + a2          ((x), v) > 0 f or all v  Rn .          (31)

                           xM

When it exists, this transformation is unique up to composition with real gauge transfor-
mations.

    Thus to prove the lemma we only have to show that the pair (A, ) of theorem 4.2
is simple and satisfies (31). The definition of the function  under the integral is the
following. Let tv : F  F be the gradient flow of the function v � � : F  R, and write
(x) = (p, q) (see section 2.1); then

             ((x), v)          :=   lim  v � �(tv(q)) .

                                   t+

The integral of  over M is not in general an easy number to estimate. However, when
the assumptions of theorem 4.2 hold, this obstacle evaporates, and we will now see how.
Take x  M such that (i) and (ii) hold. By (i) the constant c is in the open polytope
Qx := �(OC(x)); by (ii) and lemma 4.6, this polytope has dimension n. Therefore using
lemma 3.1 of [2], we have that

        lim  v � �(tv(q))  =    sup v � �(p)  =  sup v � u  >  v�c ,

       t+                      pOC(x)            uQx

where the strict inequality follows from Qx being open and having dimension n (in par-
ticular v cannot be orthogonal to Qx). Since this holds for all x in an open dense subset

                                   22
of M, we conclude that

     ((x), v) > (Vol M) v � c  for all v  Rn ,

xM

which is equivalent to (31).
    To prove that the pair (A, ) is simple (for the definition of simple pair see [27]), it is

enough to show that any infinitesimal gauge transformation s : M  Lie TCn = Cn that
leaves (A, ) fixed is necessarily zero. Let A be the space of connections on P , and as
usual identify TAA  1(M, tn). The infinitesimal gauge transformation s produces a
tangent vector in TAA, and by the transformation rules (19) this is given by

                        �s + s�  1(M, tn) .

But if s leaves A fixed, that is �s + s� = 0, the decomposition 1 = 1,0  0,1 implies
that �s = 0, and since M is compact the function s must be constant. On the other hand
for any x  M such that (ii) is satisfied we have that Lie G(x) = {0}, and so s(x) leaves
(x)  E fixed iff s(x) = 0. By the constancy of s we finally conclude that s = 0, and

this finishes the proof.

Remark. The proof for the general case dim c  n goes along the following lines. If
c(P, M, a) lies in the boundary of �(F ), by assumption (i) and lemma 4.4 so does the
image �  (M). Lemma 4.6 then tells us that there is a subtorus of T n that acts trivially
on . The strategy of the proof is to eliminate this subtorus by formulating the problem
in terms of the quotient group and quotient principal bundle. The isotropy groups G(x)
of assumption (ii) will then have dimension zero, and we will be reduced to the case
dim c = n.

5 The vortex solutions for target CPn

5.1 The main result

We start with the natural action of T n+1 on CPn, given in homogeneous coordinates by
                            (g0, . . . , gn) � [z0, . . . , zn] = [g0z0, . . . , gnzn] .

Although this is not an effective action, it induces an effective hamiltonian action of the
quotient group T n+1/N , where N denotes the diagonal circle inside T n+1. Now, this

                                                       23
quotient group is isomorphic to T n but, since there is no canonical choice of isomorphism,
there are several different ways of implementing the T n+1/N -action as an action of T n on
CPn. The general formula for these T n-actions is

(g1,...,gn) ( [z0, . . . , zn] ) = [z0 , j (gj)C1j z1 , . . . , j(gj)Cnj zn ] ,  (32)

where the matrix C is in SL(n, Z). The different choices of C correspond to the different
possible isomorphisms T n+1/N  T n. These actions are all hamiltonian and, using the
identification (tn)  tn  Rn determined by (20), the general form of a moment map
� : CPn  Rn is

�([z0, . . . , zn]) =  -        (. . . ,      Cjk|zj|2, . . .)1kn  +  const. .   (33)
                       i |zi|2
                                          j1

We denote by  the image �(CPn) in Rn. This is clearly a convex polytope, since it is
the image of the standard n-simplex

{x  Rn : 0  xk  1 and k xk  1}

by the invertible linear transformation - CT , possibly composed with a translation.

    The aim of this section is to prove theorems 5.1 and 5.2, stated below. They charac-
terize the space of solutions and energy spectrum, respectively, of the vortex equations for
target CPn with the T n-action described above. Also theorem 5.3, which appears here as
an intermediate step to prove theorem 5.1, may have some independent interest. Before
stating these theorems, however, some notation must be introduced.

    Let B0, . . . , Bn be the (n - 1)-dimensional faces of the polytope . We denote by
j  Zn the unique primitive normal vector to Bj that points to the exterior of . For
each j = 0, . . . , n define

                        Fj = �-1(Bj) = {[z0, . . . , zn]  CPn : zj = 0 } ,

which is a CPn-1 inside CPn. Since Fj is a T n-invariant complex submanifold of CPn, as
in the proof of lemma 4.5 one can define the sub-bundles Ej = P � Fj of E; these are
complex submanifolds of (E, J(A)), where J(A) is the complex structure on E induced
by an integrable connection A on P . Recalling also the constants c(P, M, a)  Rn and
(P )  H2(M; Z)n defined in section 2.4, we have the following results.

                                                       24
Theorem 5.1. In the setting described above, the vortex equations (13) have solutions
only if the constant c(P, M, a) is in . When this constant lies in the interior of , the
set of solutions can be described as follows. For each j = 0, . . . , n pick an effective divisor
Dj = i aij � Zi on M such that

  (i) the intersection of hypersurfaces supp D0  � � �  supp Dn is empty;

 (ii) the Poincar�e duals (PD) of the fundamental homology cycles carried by the divisors
       Dj satisfy (P ) = j j PD(Dj) in H2(M ; Z)n.

Then there is a solution (A, ) of (13), unique up to gauge equivalence, such that the
intersection multiplicities of the complex submanifolds (M) and Ej satisfy

                   mult(Zi)(Ej, (M )) = aji .

Furthermore all the solutions of (13) are obtained in this way.

Theorem 5.2. Assume that c(P, M, a) lies in the interior of , and let (A, ) be a
solution of the vortex equations characterized by divisors Dj, as in the theorem above.
Then the topological energy (12) of this solution is

                                          n
                                     n+1
T[]             =  e(P, M, �, a)  +              PD(Dj )  M[m-1] ,

                                          j=0  M

where the constant e does not depend on (A, ). Denoting by b  Rn the barycentre of the
polytope , the value of this constant is

             n     bk k(P )  M[m-1]  -    1    k(P )    k(P      )    M[m-2]  .
                                          a2
e=              M

           k=1

Remark. The statement of these results is especially simple when M is a Riemann

surface, for in this case the hypersurfaces Zi are just points and, under the isomorphism
H2(M; Z)  Z, there is an identification PD(Dj)  i aji  Z. In fact, consider the
symmetric products SNj M of the surface. Each point in SNj M is an unordered multiplet

(p1, . . . , pNj ) of points in M . Now let N0,...,Nn(M ) denote the open dense subset of
SN0M � � � � � SNnM obtained by excluding the points that contain a common p  M
in all the n + 1 multiplets corresponding to the different SNj M factors. Then it is clear

from theorem 5.1 that the moduli space of vortex solutions can be identified with the

                                     25
disjoint union of all the N0,...,Nn(M ) such that the non-negative integers Nj satisfy the
condition (P ) = j j Nj in Zn. By the argument after expression (42) this condition
is just Nl - N0 = k Clk k(P ) for all l = 1, . . . , n. The topological energy of each vortex
solution also reduces to

T[]  =  b � (P )  +             Nj .
                      n+1
                           0jn

Remark. It is manifest in theorem 5.1 that the vortex moduli space does not change
when the constant c(P, M, a) or the moment map � are deformed by a translation, as
long as this constant remains in the interior or exterior of the image polytope �(F ) = .
When the constant c(P, M, a) lies in the boundary of , then according to theorem 4.1 the
solutions (A, ) of the vortex equations are constrained to satisfy (M)  Ej1  � � �  Ejk ,
where n - k is the dimension of the open face of  that contains c(P, M, a). Thus in
some sense this case corresponds to sigma-models with target CPn-k and gauge group
T n. Since this gauge group is too big and has a subtorus T k that acts trivially on the
sections , these cases are somewhat degenerate.

5.2 Proof of theorem 5.1

Equivalent theorem

The first statement of theorem 5.1 follows from theorem 4.1 and corollary 4.3. As for the
rest of theorem 5.1, we will prove it by stating and proving the equivalent theorem 5.3.

    Let S be the set of solutions of the vortex equations (13), and define

   B = (A, )  A1,1(P ) � (E) : �A = 0 and (M )  Ej for all 0  j  n .

The first thing to notice is that by theorem 4.1, corollary 4.3 and the subsequent remark,
the natural inclusion of S in B actually induces a bijection of quotient spaces

S/(real gauge transf.)  B/(complex gauge transf.) .  (34)

On the other hand the action of TCn  (C)n on CPn is given by (32), with gj  C, so it
is clear from the definitions of Fj and Ej that

-1(Ej) = (g � )-1(Ej)      M

                  26
for any complex gauge transformation g : M  TCn. Moreover, it is a direct consequence
of propositions 5.4 and 5.5, stated below, that for any irreducible hypersurface Z  M
the intersection multiplicities satisfy

mult(Z)(Ej, (M )) = mult(g�)(Z)(Ej, (g � )(M )) ,

or in other words they are complex-gauge invariant. This fact together with the bijection
(34) (which, recall, is induced by the inclusion S  B ) show that theorem 5.1 is equivalent
to the following result.

Theorem 5.3. Assume that c(P, M, a) lies in the interior of , and for each j = 0, . . . , n
pick an effective divisor Dj = i aji � Zi on M such that conditions (i) and (ii) of the-
orem 5.1 are satisfied. Then there exists a pair (A, )  B, unique up to complex gauge

equivalence, such that

mult(Zi)(Ej, (M )) = aij .                                          (35)

Furthermore all pairs in B can be obtained in this way.

    The method that we will use to prove this theorem is not intrinsic, in the sense that it
is based on the use of the usual local charts from CPn to Cn. In informal terms, we use the
fact that the domains of these charts are T n-invariant and dense in CPn to transfer the
problem of finding holomorphic sections of E -- which has fibre CPn -- to the problem
of finding meromorphic sections of vector bundles with fibre Cn.

Proof of the equivalent theorem

As always, we start by introducing some notation. For each j = 0, . . . , n define the
action j of T n on C by restricting the action  of formula (32) to the j-th homogeneous
coordinate of CPn. Thus for example 0 is the trivial action, while for j = 0 the actions
j depend on the matrix C. Define also the associated line bundles Lj = P �j C.

    Now consider the usual complex charts j : Uj  Cn of CPn, defined by

Uj = CPn \ Fj = {[z0, . . . , zn]  CPn : zj = 0} ,

j([z0, . . . , zn]) = zj-1 (z0, . . . , zj-1, zj+1, . . . , zn) .   (36)

From formula (32) and the definition of j it is clear that Uj is T n-invariant and that, for
any g  T n,

j  g = . . . , (j)g-1 � (k)g, . . .                      k=j   j .

                                 27
Thus defining the vector bundle over M

Vj = (Lj)-1  (L0  � � �  Lj-1  Lj+1  � � �  Ln) ,                                  (37)

and recalling that

                       E \ Ej =  [p, x]  P � CPn : x  Uj ,

one has that the maps

                       ~j : E \ Ej  Vj , [p, x]  [p, j(x)]                         (38)

are well defined. These maps clearly are fibre-preserving diffeomorphisms. As a matter of
notation, we will sometimes call Lj,k the k-th line bundle in the direct sum decomposition
(37); thus for example

     L0,k = (L0)-1  Lk , Ln,k = (Ln)-1  Lk-1 and Vj = 1kn Lj,k . (39)

Since the actions j preserve the canonical hermitian product on C, the line bundles Lj,k
are all equipped with a natural hermitian metric, denoted hj,k. Another standard fact is
that a connection A on P induces connections on the associated line bundles Lj and Lj,k.
These connections are hj,k-compatible. If the connection A is integrable, i.e FA0,2 = 0,
then the induced connections on the Lj,k are integrable as well, i.e. their curvature form
is in 1,1(M ).

    The reason why we are interested in these integrable connections is that, according to
a well known result, an integrable, metric-compatible connection  on a C hermitian
vector bundle (V, h)  M, induces a unique holomorphic structure H on V such that  is
the hermitian connection of (V, h, H) [24]. The bundle V equipped with this holomorphic
structure will be denoted by V . We will often apply this result to the line bundles Lj,k.
When the integrable connection on Lj,k comes from a connection A on P , we denote by
LAj,k the line bundle together with the induced holomorphic structure.

    Using all these conventions we define

              C = {(1, 1, . . . , n, n) : conditions (1) and (2) are satisfied} ,
where the conditions are

(1) k is an h0,k-compatible connection on L0,k and k is a non-zero meromorphic section
     of L0,kk ;

                                        28
  (2) the divisors on M associated to the sections k satisfy (1)- = � � � = (n)- =: ()-,
       and the intersection supp ()-  supp (1)+  � � �  supp (n)+ is empty.

In the last condition we have decomposed a divisor D = D+ - D- into its positive
and negative parts. The main tools to prove theorem 5.3 are then the following two
propositions.

Proposition 5.4. There exists a bijection  : B  C determined by the following condi-
tions.

  (i) k is the connection on L0,k induced by the connection A on P .

 (ii) ~0  (q) = (1(q), . . . , n(q)) in V0 for all q  M \ -1(E0).

Furthermore, let (A, ) and (A, ) be two pairs in B and let (. . . , k, k, . . .) and
(. . . , k, k , . . .) be their images by . Then (A, ) and (A, ) are complex gauge equiv-
alent if and only if for all k the meromorphic sections k and k have the same associated
divisor in M.

Proposition 5.5. Given a pair (A, ) in B, let (. . . , k, k, . . .) be its image in C by
the bijection . Then for any irreducible analytic hypersurface Z  M and for any
j = 0, . . . , n, the multiplicity of intersection of Ej and (M) along (Z) is given by

mult(Z)(Ej, (M )) = ordZ (j) - min {ordZ(k)} ,     (40)
                                  0kn

where we define ordZ(0) = 0.

Remark. Formula (40) implies that, for fixed Z, the multiplicities mult(Z)(Ej, (M))
are non-negative integers, with at least one of them being zero. On the other hand, given
such a set of multiplicities, put

ordZ(j) = mult(Z)(Ej, (M )) - mult(Z)(E0, (M )) .  (41)

It is then apparent that formulae (40) and (41) define inverse maps between the set of
sets of n arbitrary integers ordZ(j), and the set of sets of n + 1 non-negative, and not all
positive, integers.

    The proofs of these propositions, especially the first one, are rather long and uninter-
esting, so will be exiled to appendix A. We are now ready to prove theorem 5.3.

                              29
Proof of theorem 5.3. Let D0, . . . , Dn be divisors on M satisfying conditions (i) and
(ii) of theorem 5.1. We will first show the existence of a pair (A, )  B satisfying (35).
By definition of the actions j, the line bundle L0 is trivial and, for k > 0,

                 Lk =       (L^l)Ckl ,

                       1ln

where the line bundles L^j were defined in section 2.4. In particular, using (39), this
implies that

c1(L0,k) =          Ckl c1(L^l) =            Ckl l(P ) .                         (42)

                 l                 l

Now denote by e1, . . . , en the standard basis of Rn and by e0 the vector -e1 - � � � - en. It
is not difficult to check directly that, for a = 0, . . . , n, the vector a = C-1ea is a primitive
vector in Zn normal to one of the (n - 1)-dimensional faces of the polytope . Moreover

this is an outward pointing normal vector, and so the a's coincide with the j's that
appear in condition (ii) of theorem 5.1. Hence by this condition

c1(L0,k) =       Ckl (C-1ea)l PD(Da) = PD(Dk - D0) .

            a,l

Thus the divisor Dk - D0 defines a holomorphic structure on L0,k together with a mero-
morphic section k of this line bundle (see [24] or [19]). Now denote by k the hermitian
connection on the hermitian bundle (L0,k, h0,k) equipped with that holomorphic struc-
ture. Then by construction the multiplet (1, 1, . . . , n, n) satisfies condition (1) of the
definition of C. Since (k)+ = Dk and (k)- = D0, it also satisfies condition (2), as follows
from the requirement (i) of theorem 5.1. Thus

                                       (. . . , k, k, . . .)1kn  C .
According to propositions 5.4 and 5.5 this determines a pair (A, )  B such that

    mult(Zi) (Ej, (M )) = (aji - ai0) - 0mkinn{aik - ai0} = aji - 0mkinn{aki } = aij ,

where in the last equality we have used again the requirement (i) on the divisors Dk. This
settles the existence part of theorem 5.3.

    We will now prove the uniqueness statement. Keeping the same divisors Dj = i aij �Zi
as above, suppose that (A, )  B is another pair that satisfies (35), and denote by

                 (. . . , k , k , . . .)  C

                       30
the image of this pair by the bijection . Since we are assuming that the intersection
divisors of (M) and (M) with Ej are the same, proposition 5.5 and formula (41) in
the subsequent remark imply that

                                  ordZi(j) = aij - a0i = ordZi(j ) .

Thus the meromorphic sections j and j have the same divisor in M, and from proposition
5.4 we conclude that (A, ) is complex gauge equivalent to (A, ), as required.

    To complete the proof of theorem 5.3 we just need to justify the last assertion, i.e. that
for every pair (A, )  B the divisors Dj = i aji � Zi defined by (35) satisfy conditions
(i) and (ii) of theorem 5.1. In the first place, the definition of B tells us that (M)  Ej,
so -1(Ej) is a union of irreducible hypersurfaces of M. In particular the intersection
multiplicities of (35) are finite integers, and the divisors Dj are well defined. Secondly,
by the definition of Dj as the inverse image by  of the intersection divisor of (M) and
Ej, we have that (supp Dj)  Ej. This implies that (i) is satisfied, because jEj = .
Finally, to recognize that the divisors Dj associated to  satisfy (ii) as well, consider the
sections k = (~0  )k of proposition 5.4. From proposition 5.5 and formula (41) it is
clear that Dk - D0 is just the divisor of k. But k is a meromorphic section of L0A,k, and
so by standard results the Poincar�e dual of the divisor of k is c1(L0,k). Using these facts,
(42), and the formula a = C-1ea established earlier, we then get that

     C a PD(Da) =       ek PD(Dk - D0) =       ek c1(L0,k) = C (P )

0an                1kn                    1kn

in H2(M; Z)n. Multiplying on the left by the matrix C-1 we obtain that (ii) is indeed
satisfied.

5.3 Proof of theorem 5.2

The main task is to express the cohomology class [E]  H2(E; R) in terms of the Poincar�e
dual of [Ej]  H2(m+n)-2(E; Z). We start by noticing that, up to exact forms, any closed
2-form on M may be written as s1 M + , where s1  R, and   2(M) is such that
  Mm-1 = 0. This is a consequence of the Lefschetz decomposition on Ka�hler manifolds
[19]. Furthermore it is apparent from expression (46) below that the class of E(A), when
restricted to the fibres Ex  CPn of E, generates the group H2(Ex; R)  R. It is then
a consequence of the Leray-Hirsch theorem [6] that PD(Ej), and in fact any element of

                                                       31
H2(E; R), is of the form

             PD(Ej) = s0 [E] + s1 E [M ] + E [] ,

where s0, s1  R. Hence we have that

          s0 [E ]  M[m-1] =             PD(Ej )  M[m-1] - s1 m M[m] .
          M                          M                       M

Now, by well known properties of the Poincar�e duality, the restriction of PD(Ej) to (M)
is just the Poincar�e dual in (M) of the intersection divisor of Ej and (M) 1. But
because of (35) this divisor is just i aij � (Zi) = (Dj), and since  : M  (M) is a
biholomorphism we obtain that

           PD(Ej) =  PD( Dj) = PD(Dj) in H2(M ; Z) .

Thus

          s0 [E]  M[m-1] = -s1 m (Vol M ) +            PD(Dj )  M[m-1] .      (43)

          M                                         M

The task now is to compute the constants s0 and s1. Firstly we remark that

         E[n-1]  E M[m] =      E[n-1]  E M[m]  PD(Ej) = n s0 E[n]  E M[m] .   (44)

       Ej                   E                                E

Also

          E[n]  E M[m-1] =        E[n]  E M[m-1]  PD(Ej ) =                   (45)

      Ej                       E

                          = (n + 1)s0 E[n+1]  E M[m-1] + m s1 E[n]  E M[m] .
                                     E                          E

The constants s0 and s1 are therefore determined by the value of the integrals in (44) and
(45). To compute these integrals, recall from section 2.2 that [E] is the cohomology class
of the closed 2-form E(A) in E, and that

             E(A) = F - d(�, A) in 2(P � F ) .

As in (9), a local section s : U  P-1(U) of P determines a trivialization E|U  U � F ,
and it is not difficult to check that with respect to this trivialization we have

             E(A) |U = F - d(�, sA) in 2(U � F ) .                            (46)

1I thank Dr. J.M. Woolf for explaining this to me.

                                        32
It follows that for any k  N

    E(A)[k] = F[k] - F[k-1]  d(�, sA) + � � �                   in 2k(U � F ) ,

and integrating along the fibre [6] we get that


                                      Vol F               if k = n
                                                          if k = n + 1 .
    (E) (E(A)[k])
                                  =        -  FAl     �l


                                                   F

Using the standard properties of the homomorphism (E) (see [6]), we therefore have
that

    E[n]  E M[m] =      (E)(E[n])  M[m] = (Vol F ) (Vol M ) ,                          (47)

E                   M

E   E[n+1]  E M[m-1] =  M     (E )(E[n+1])  M[m-1] = -            �l    FAl  M[m-1] . (48)

                                                                F     M

Now consider the inclusions iFj : Fj  F and iEj : Ej  E. Using the restriction iFj F
as a Ka�hler form on Fj, and �  iFj as a moment map for the T n-action on Fj, one can

define the 2-form Ej (A) on Ej = P �T n Fj, which is the analogue of E(A) on E. But

                       iE j E(A) = iF j F - d(�  iFj , A) =  Ej (A) ,

and so Ej (A) is just iE j E(A). Since Ej = E  iEj as well, by analogy with (47) and
(48) we have that

Ej  iE j (E[n-1]  E M[m]) =   Ej  E[nj-1]  E j M[m] = (Vol Fj ) (Vol M )

Ej  iE j (E[n]  E M[m-1]) =   Ej  E[nj]  (Ej )M[m-1] = -          �l  iFj    FAl  M[m-1].

                                                                Fj         M

From the value of these integrals it is straightforward to compute the constants s0 and
s1; it is enough to use (44), (45) and the fact that CPk with the Fubini-Study metric has
volume k/k!. Doing this and substituting the result into (43), one obtains that

      [E ]  M[m-1]  =        n!   (n + 1)    � -        �  iFj  �       -FA  M[m-1] +
                             n
    M                                      F          Fj              M

                                                                +  PD(Dj)  M[m-1] .
                                                                          M

                                           33
Now on the one hand, as mentioned in section 2.4, the cohomology class of -FA is just
(P ). On the other hand, since the equality above is valid for all j, we may as well sum
over j and divide by n+1. Doing this, applying lemma 5.6 below and using the definitions
(12) and (15), we obtain the formula of theorem 5.2.

Lemma 5.6. Denoting by b  Rn the barycentre of the polytope , one has that

n!                                       n                       1
n                               +                             Vol 
    (n + 1)           �  -  n      1          �  iFj       =               v     = b.  (49)

                    F                 j=0   Fj                         v

Proof. Instead of computing these integrals directly, using (33), we will evaluate them
using the Duistermaat-Heckman theorem (see for instance [26, 21, 12]). Since F = CPn
is a toric manifold, the Duistermaat-Heckman polynomial is piecewise a constant; with
our conventions it is 1 in the interior of  and 0 in the exterior. Therefore

                                         �=          v,

                                      F           v

where the integral on the right-hand side is taken with respect to the Lebesgue measure
in Rn. To evaluate the other integrals of lemma 5.6, take a T n-1-action on Fj  CP n-1
of the same kind as (32), and let �j : Fj  Rn-1 be a moment map for it. Since �  iFj is
T n-1-invariant, it is clear that it can be written as

                            �  iFj = S  �j + const. ,

where S : Rn-1  Rn is some linear embedding. Thus using again the Duistermaat-

Heckman theorem we obtain that

      �  iFj =                    S(v) + const.      =     Vol �j(Fj)          v,
                                                           Vol �(Fj)
    Fj                   v�j (Fj )                                     v�(Fj )

where the prefactor of the last term is just the inverse of the determinant of S as a linear
map from Rn-1 to its image. Finally a third application of the Duistermaat-Heckman

theorem shows that

    Vol             =  Vol F    =     n     =     Vol  Fj  =     Vol   �j (Fj )  .
                                      n!       n              n

Hence the left-hand side of (49) is equal to

    n+1                                 n      n        1
    Vol                               n+1
                             v  -              j=0 Vol �(Fj)             v.            (50)

                         v                                       v�(Fj )

                                              34
Now notice that the first term in the expression above is n + 1 times the barycentre vector

of , while the second term is n(n + 1)-1 times the sum of the barycentre vectors of

the faces �(Fj) of . But for a polytope   Rn with vertices p0, . . . , pn the barycentre

vector is                   1                     1
                         Vol                      +
                 b=                  v      =  n     1    (p0  +  ���  +  pn)   Rn .

                                 v

In particular, applying this expression to the faces �(Fj) of , we get that the last term

of (50) is just

           n     n    1                                            n
           +          n                                            +
-  n          1          (p0  +  ���+  p^j  +  ���+  pn)  =    -n      1  (p0  + � � � + pn)  =  -n b .

                 j=0

Substituting this into (50) we get the required result.

6 Constructing solutions on quotient targets

6.1 Induced solutions

Consider the gauged -model determined by the data of section 2.1, and let H be a closed
normal subgroup of G. In informal terms, the aim of this section is to compare the vortex
equations defined for target F with G-action, and the vortex equations defined for target
F/HC with G/H-action. The main result obtained is theorem 6.3. We point out that
this operation of quotient on the target is more delicate than, for example, the product
of targets. In particular, the second vortex equation does not have any natural behaviour
under these quotients, and so theorem 6.3 only concerns the set S^ of solutions of the
first and third vortex equations. Nevertheless, the results in this section are still useful,
because in section 4 we showed that, in the abelian case, the quotients S^/GC are often
very similar to the usual quotients S/G of vortex solutions. All this will eventually be
used in section 7 to exhibit non-trivial solutions of the vortex equations when the target
F is a Ka�hler toric manifold.

    We now formalize the problem. Denote by h  g the Lie algebra of H, by G = G/H
the quotient group, and by g  g/h the Lie algebra of G. The invariant inner product on
g induces a splitting g = h  h with associated projections 1 : g  h and 2 : g  h;
it also induces natural identifications g  g, h  h and (g)  g  h. Using these

                                                       35
identifications it is not difficult to check that 1  � : F  h is a moment map for the
action of H on F .

    Suppose, moreover, that HC acts freely on F , and that there exists an element a 
1  �(F ) which is invariant by the coadjoint action of H on h. Then, by standard results
[23], the quotient F/HC is a Ka�hler manifold in a natural way. The Ka�hler structure on
F  := F/HC depends on the choice of a and can be characterized as follows. The complex
structure on F  is the only one such that the projection F : F  F  is holomorphic; the
symplectic form F  on F  is determined by the condition

                                           iZa F F  = iZ a F ,

where Za is the inverse image (1  �)-1(a), and iZa is the inclusion Za  F . Note that
it can be shown that Za is a H-invariant submanifold of F , and that F  = Za/H [23].

Remark. When F is compact it is never possible to find hamiltonian H-actions such that

HC acts freely. On the other hand, denoting by �H the moment map of the H-action, there
is a canonical choice of an AdH-invariant element a  �H(F ), which is a = xF �H(x).
It can then be shown that if H acts freely on �-H1(a), then HC � �H-1(a) is an open subset
of F where the action of HC is free [23].

The group G acts naturally on F  by the rule

G(g) � F (p) = F (g � p)                       g  G, p  F ,  (51)

where G : G  G is the quotient map. It is not difficult to check that this is still a
holomorphic hamiltonian action. In fact, a moment map � : F   g  h for this
action is determined by the formula

iZ a F � = iZ a (2  �) .                                     (52)

Besides acting on F , the subgroup H also acts freely on the principal bundle P . Let P 
be the quotient space P/H and let  : P  P  be the quotient map. The group G acts
naturally and freely on P , and if we define the projection P  : P   M by

P    = P ,

it is apparent that P  is the total space of a G-bundle over M. If A  1(P ; g) is a
connection on P , it is clear that (dG)  A descends to a form A  1(P ; g). This is a

36
connection form on the bundle P  [25, p. 79]. Using that P �AdG g  P  �AdG g, the
curvature form of A is dG  FA  2(M ; P �AdG g), where FA  2(M ; P �AdG g) is the

curvature form of A. Identifying g  h this curvature form is just 2  FA. In particular

FA0,2 = 0  FA0,2 = 2  FA0,2 = 0 .                                              (53)

Consider now the associated bundle E = P �AdG F  = P  �AdG F . There is a natural
bundle map E  E determined by the formula

[p, q]  [p, F (q)]                               p  P, q  F .                  (54)

As always, this induces a map on the space of sections

(E) - (E),    .

Using the definition (7) and the holomorphy of F it is then not difficult to check that

�A = 0  �A = 0 .                                                               (55)

Hence, in terms of the spaces of solutions

S(P, E) = {(A, )  A(P ) � (E) : equations (13) are satisfied }            and

S^(P, E) = {(A, )  A(P ) � (E) : equations (13a) and (13c) are satisfied } ,

we have that the correspondence (A, )  (A, ) defines a map

 : S^(P, E) - S^(P , E) .                                                      (56)

We will now see how  behaves when we quotient by complex gauge transformations.

    To start with, recall that the quotient map G can be extended to a homomorphism
(G)C : GC  GC , and that this homomorphism induces an identification GC  GC/HC.
The homomorphism (G)C then defines a natural bundle map

P �AdG GC - P �AdG GC ,                         [p, g]  [ p, (G)C(g) ] .       (57)

As always, composition with this bundle map defines a map of sections

GC : GC - GC ,                                  g  g .

This map clearly is a homomorphism of gauge groups. One can also check that it has the
following naturality property.

                                            37
Lemma 6.1. Let (A, ) be any pair in A(P ) � (E) and g any gauge transformation in
GC. Then g() = g() in (E) and g(A) = g(A) in A(P ).

    A direct consequence of this lemma is that the map  descends to a map of quotient
spaces S^(P, E)/GC  S^(P , E)/GC . Another important property of  is the following.

Lemma 6.2. Let (A1, 1) and (A2, 2) be two pairs in S^(P, E). Then (A1, 1) = (A2 , 2 )
if and only if there exists a gauge transformation g  HC such that 2 = g(1) and
A2 = g(A1). When it exists, this transformation is unique.

    This is proved using the assumptions that HC acts freely on F , the rules (18) and
(19) for gauge transformations, and the fact that the (Aj, j) satisfy the vortex equations
(13a) and (13c). The details are exiled to section 6.2. Combining the two lemmas above
one directly obtains the main result of this section, which is the following.

Theorem 6.3. The induced map  : S^(P, E)/GC - S^(P , E)/GC(GC) is injective.

Remark. In many cases of interest the homomorphism GC is surjective, and so we actu-
ally get an injection  : S^(P, E)/GC  S^(P , E)/GC . This happens, for example, when
the group G can be factorized as G = H � W , where W is some other subgroup of G. In
this case GC  HC � WC and GC  WC, and so it is clear that any section of P �AdG GC
can be lifted to a section of P �AdG GC.

6.2 Proof of lemma 6.2

We first establish a preparatory lemma, and then prove Lemma 6.2.
    The proof of theorem 6.3 is essentially contained in proposition 6.2 below. We state

and prove this proposition after establishing a preparatory lemma. Finally a few lines are
spent completing the proof of theorem 6.3.

Lemma 6.4. Let 1 and 2 be two sections of E. Then 1 = 2 in (E) if and only if
there exists a gauge transformation g  HC such that 2 = g(1). When it exists, this
transformation is unique.

Proof. Since HC acts freely on F , the gauge group HC acts freely on (E), and so the
uniqueness of g is clear. Furthermore, the sufficiency part is apparent from the formula
g() = g() of lemma 6.1, so we just need to prove the necessity.

                                                       38
    Suppose then that 1 = 2 , and take local trivializations of E = P �GF and E = P �G
F  induced by the same local trivialization of P . With respect to these trivializations, if
the i are represented by local maps ^i : U  F , the i are represented by F ^i : U  F .
But the equality of the i's implies that F  ^1 = F  ^2, and since F : F  F  is a
principal HC-bundle we conclude that there exists a unique smooth map g^ : U  HC such

that

^2(x) = g^(x) � ^1(x) for all x  U .           (58)

Had we chosen initially a different trivialization of P , related to the first one by a transition
function  : U  G, we would get the maps (�)-1 � ^i(�) : U  F as representatives of
the i's. In particular

           (x)-1 � ^2(x) = (x)-1g^(x) (x) � (x)-1^1(x) for all x  U ,

which shows that the local maps g^(�) transform as sections of the bundle P �AdG HC. By
their local uniqueness, these maps can be "glued" together to define a global section of
the latter bundle, i.e. an element g of HC. It then follows from (58) that 2 = g(1).

Proof of Lemma 6.2 . By the previous lemma, the condition 1 = 2 is equivalent to
the existence of a unique g  HC such that 2 = g(1). We now have to show that, for
this transformation g, A2 = A1 if and only if A2 = g(A1).

    A first observation is that, since H is normal in G, for any h  H and v  g the vector

Adh(v) - v is in h. It is then apparent from the gauge transformation rule

g(A) = Adg  A - P (g-1�g + g�-1g�) ,  g  HC ,

that, for any connection A on P , the difference g(A) - A is in 1(P ; h). Therefore, if
A2 = g(A1), using the definition of Aj in the paragraph after (52), we have that

(A2 - A1 ) = (dG)(A2 - A1) = 0 ,

which implies that A2 = A1. Conversely, suppose that A2 = A1 . Then by the previous
formula A2 - A1  1(P ; h), and therefore

g(A1) - A2 = g(A1) - A1 + A1 - A2  1(P ; h).   (59)

39
On the other hand the assumptions of the proposition are that (Ai, i)  S^(P, E), and
since equation (13a) is invariant by complex gauge transformations,

�A2 2 = �A1 1 = �g(A1)g(1) = �g(A1)2 = 0 .                                 (60)

Now let s : U  P be a local trivialization, and let ^i : U  F be the representative of
i with respect to the associated trivialization of E = P �G F . From (60) and (10) we
get that

[ (sA2)x(�) ] |^2(x) = [ (sg(A1))x(�) ] |^2(x)  for all x  U .

Since the correspondence  : g  TqF, v  v|q is linear, this is the same as

[ s(A2 - g(A1))x (�) ] |^2(x) = 0  for all x  U .                          (61)

But by assumption the action of H on F is free, and so the restriction of  to h  g
is injective. From (59) and (61) it then follows that s(A2 - g(A1)) = 0, and since the
trivialization s was arbitrary we conclude that A2 = g(A1).

7 Solutions for target a compact toric manifold

7.1 The canonical K�ahler toric manifolds

A compact Ka�hler toric manifold F is by definition a compact Ka�hler manifold equipped
with an effective hamiltonian action of T n -- where n is the complex dimension of F --
which operates by holomorphic transformations. If � : F  Rn is a moment map for this
action, it is well known that the image �(F ) is a special kind of polytope in Rn, usually
called a Delzant polytope, and that this polytope determines F up to T n-equivariant
symplectomorphisms [16].
Definition. A Delzant polytope  in Rn is a convex polytope such that:

    � there are n edges meeting at each vertex;

    � the edges meeting at the vertex p are rational, in the sense that they are of the form
       p + tvi, t  R, with vi  Zn;

    � these v1, . . . , vn can be chosen to be a basis of Zn.

40
    The symplectomorphism mentioned above, however, does not necessarily preserve the
complex structure on F , and so the polytope �(F ) does not determine F as a Ka�hler man-
ifold. In other words, this means that several inequivalent Ka�hler toric manifolds may give
rise to the same image polytope �(F ). Although lacking injectivity, the correspondence
between Ka�hler toric manifolds and Delzant polytopes is certainly surjective. This is be-
cause, given any Delzant polytope  in Rn, there is a natural way to construct a Ka�hler
toric manifold F such that �(F) = . We will now briefly recall this construction; for
more details see for example [21] or [12].

    Let  be a Delzant polytope in Rn with (n-1)-dimensional faces, or facets, B1, . . . , Bd,
where d > n. Then one can uniquely choose vectors u1, . . . , ud  Zn such that ui is a
primitive, outward pointing, normal vector to Bi. The polytope  is then the intersection
of half-spaces

                                {x  Rn : ui � x  i , i = 1, . . . , d} ,

for some i  R. Denoting by e1, . . . , ed the standard basis of Rd, define the linear map

   : Rd - Rn , ej  uj ,

and its i-linear extension C : Cd  Cn. It is not difficult to show that (Zd) = Zn, and
so these maps descend to homomorphisms of tori

Rd --- Rn                                 Cd ---C Cn


T d ---~ T n                              TCd --~-C TCn .

In both these diagrams the vertical arrows represent the exponential map (29). The
subspace n = ker  of Rd exponentiates to the subgroups

 N = ker ~ = exp (n)                         Td
NC = ker ~C = exp (n) � exp (in)             TCd ,

and one has the short exact sequence

  0 - NC - TCd - TCn - 0 .                                                  (62)

Now consider the natural action of T d on the Ka�hler manifold Cd given by

(g1, . . . , gd) � (z1, . . . , zd) = (g1z1, . . . , gdzd) .                (63)

                                      41
This action operates by holomorphic transformations and has moment map

           � : Cd - Rd , (z1, . . . , zd)  -(|z1|2, . . . , |zd|2) + (1, . . . , d) .

The restriction of this action to the subgroup N has moment map 1  � : Cd  n, where
1 is the orthogonal projection from Rd to n. Notice also that the action (63) has a natural
extension to the complexified group TCd; this is given by the same formula, but with the
gj's belonging to C. Now define the subset

Cd = (z1, . . . , zd)  Cd : zj1 = � � � = zjk = 0 is allowed only if       Bjl =  .

                                                                      1lk

It is shown in appendix 1 of [21] that Cd is an open dense subset of Cd where NC acts
freely. Furthermore the inverse image Z = (1  �)-1(0) is contained in Cd, and in fact
Cd = NC � Z. Hence, by the quotient construction described in section 6, the quotient
manifold F = Cd/NC has a unique structure of Ka�hler manifold such that the projection
F : Cd  F is holomorphic and

iZ F F = iZ Cd .

Just as in section 6, the quotient group T d/N acts naturally on F by holomorphic
transformations. Identifying T d/N  T n through ~, this action has a moment map

� : F  Rn determined by

                                          iZ F � = iZ (  �) .

It can be shown that �(F) = . The Ka�hler manifold F equipped with this T n-action
is the canonical Ka�hler toric manifold we were looking for.

Example. When  is the Delzant polytope

 = {x  Rn : xj  0 and j xj  -} ,

one gets that Cd = Cn+1 \ {0} and that N  T 1 is the diagonal subgroup of T d = T n+1.
It is then clear that F = Cd /NC = CPn, and one can check that the induced Ka�hler
metric on CPn is the Fubini-Study one.

    Besides the result �(F) =  described above, in the next section we will also use
that for any facet Bj of 

(�  F )-1(Bj) = {z  Cd : zj = 0} .                                         (64)

This fact also follows from the results in the appendix 1 of [21].

42
7.2 A family of non-trivial solutions

Let F be a compact Ka�hler toric manifold, let � : F  Rn be a moment map for the
associated torus action, and call  the image �(F ), which is a Delzant polytope in Rn.
Denote by B1, . . . , Bd the (n - 1)-dimensional faces of , and by j  Zn the unique
primitive, outward pointing, normal vector to Bj. Finally identify tn  Rn through (29),
and take the euclidean inner product on Rn to identify tn  (tn).

    Now take any principal T n-bundle P  over the Ka�hler manifold M, and denote by
(P )  H2(M; Z)n the vector of cohomology classes described in section 2.4. Using this
principal bundle one can define the associated bundle E = P  �T n F , which has base M
and typical fibre F . From lemma 4.4 we know that the subsets

Fj := (�)-1(Bj)

are T n-invariant complex submanifolds of F . Furthermore, as described in the proof of
lemma 4.5, the associated bundles

                                              Ej := P  �T n Fj

are complex submanifolds of (E, J(A)), where J(A) is the complex structure on E in-
duced by an integrable connection A on P  (see section 2.2). The aim of this section is to
prove the following result.

Theorem 7.1. In the setting described above the vortex equations (13) have solutions
only if the constant c(P , M, a) is in . When this constant lies in the interior of , a
set of solutions can be described as follows. For each j = 1, . . . , d pick an effective divisor
Dj = i aji � Zi on M such that

  (i) if 1lk Bjl =  for some indices j1, . . . , jk, then the intersection of hypersurfaces
       supp Dj1  � � �  supp Djk is empty as well;

(ii) the Poincar�e duals of the fundamental homology cycles carried by the divisors Dj
     satisfy (P ) = j j PD(Dj) in H2(M ; Z)n.

Then there is a solution (A, )  S(P , E) of the vortex equations such that the intersec-
tion multiplicities of the complex submanifolds (M) and Ej satisfy

mult(Zi)(Ej , (M )) = aij .                                          (65)

Different choices of divisors provide gauge inequivalent solutions.

43
    Comparing with theorem 5.1 one recognizes that, when F = CPn, the set of solutions
obtained in theorem 7.1 actually coincides with the full set of solutions, up to gauge
transformations. This motivates the following question.

Question. Let F be any compact Ka�hler toric manifold, and suppose that the constant
c(P , M, a) lies in the interior of . Do the solutions described in theorem 7.1 represent
the full space of vortex solutions, up to gauge equivalence ?

Proof of theorem 7.1. We first prove the theorem in the case where F is the canonical
manifold F. At the end we will deal with the case of any F such that �(F ) = .

    Given the divisors Dj, by proposition 2.5 there is a principal T d-bundle P  M such
that PD(Dj) = j(P ) = c1(Lj) for all j = 1, . . . , d. Let

E = P �T d Cd = L1  � � �  Ld                                                              (66)

be the associated bundle. Using the notation of section 7.1, define also the bundle E =

P �T d Cd , which is an open dense subset of E.
    Now consider the spaces of solutions S(P, E) and S^(P, E) defined before (56). As in

section 3 (with C = Id), since PD(Dj) = c1(Lj), there exists a pair (A, )  S^(P, E)

such that Dj is the divisor of the zero set of j -- the j-th component of  under the
decomposition (66) -- regarded as a holomorphic section of LAj . Notice that condition
(i) on the divisors implies that if 1lk Bjl =  the intersection 1lk j-l1(0) is empty;
thus, having in mind the definition of Cd , we conclude that (M)  E , and the pair
(A, ) may be regarded as belonging to S^(P, E ).

    At this point we want to apply the results of section 6 in order to obtain solutions
in S^(P , E). Going back to this section, put G = T d, H = N and F = Cd. The
homomorphism ~ : T d  T n, which has kernel N , provides identifications T d/N  T n

and P/N  P �~ T n. But by lemma 2.6 and condition (ii) we have that

a(P �~ T n) =     al l(P ) = a(P )  for all a = 1, . . . , n.

               l

Thus the bundles P/N and P  are isomorphic, and so the P  of section 6 coincides with

the P  of this section. On the other hand, since F is the Ka�hler quotient Cd /NC with
the T n-action provided by the identification of T d/N with T n through ~, the F  and E

of section 6 are just the F and E of this section. Applying the results of section 6 we
therefore have that the map  takes (A, ) to a solution (A, ) in S^(P , E). By lemma

7.2 below, this solution satisfies the condition (ii) on the intersection multiplicities.

                  44
    We now use the results of section 4, namely corollary 4.3 and the subsequent remark.
These guarantee that (A, ) is complex gauge equivalent to a solution (A~, ~)  S(P , E)
of the full vortex equations. By the proof of lemma 7.3 below, the intersection multiplic-
ities of (M) and ~(M) with the submanifolds Ej are the same, and so (A~, ~) satisfies
condition (ii). This proves the existence part of the theorem. As for the last assertion of
the theorem, it follows directly from lemma 7.3 and the fact that the (A~, ~) are complex
gauge equivalent to the (A, ). This finishes the proof for F.

    To show that the theorem remains valid for any F with �(F ) = , we first remark
that such an F is equivariantly biholomorphic to F [1]. In particular, since the vortex
equations (13a) and (13c) only depend on the T n-action and complex structure on F , not
on the symplectic form, the spaces S^(P , E) are the same in the F and F cases. This
shows that the solution (A, ) constructed above for the F case also provides a solution
for the F case. Repeating the argument of the paragraph above we conclude that the
theorem also holds for F .

Lemma 7.2. Let (A, )  S^(P, E ) be the pair constructed above, and let (A, ) 
S^(P , E) be its image by the map  of section 6. Then

                                      mult(Zi)(Ej , (M )) = aji .

Proof. Denote by E : E  E the bundle map defined in (54), and let Ej be the
sub-bundle k=j Lk of E. It follows from (64) and the definition of Ej that

                E- 1(Ej ) = Ej  E .                                      (67)

Since the section  of E is by definition E  , we then have that

-1(Ej ) = -1(Ej  E ) = -1(Ej) .

Writing this analytic hypersurface in M as a union iI Zi of irreducible hypersurfaces,
it is tautological that

Ej  (M ) =      (Zi) and Ej  (M ) =                              (Zi) .

            iI                       iI

Notice that (Zi) and (Zi) are irreducible analytic hypersurfaces in (M) and (M),
respectively, for it was shown in the proof of lemma 4.5 that  and  are biholomorphisms
onto their images.

                45
    Now, given any generic point p  Zi, let the submanifolds Ej  E and Ej  E be
locally defined around (p) and (p) by holomorphic functions f and f , respectively. This

means that f is a locally defined holomorphic function whose germ at (p) is irreducible in
the ring O(p)(E), and such that the zero locus of f coincides with Ej in a neighbourhood
of (p). Similarly for f . Then from the formulae of [19, p. 65, 130 and 395] it follows
that

mult(Zi)(Ej , (M )) = ord(Zi), (p) (f |(M)) = ordZi, p(f )    and  (68)
                                                                   (69)
mult(Zi)(Ej , (M )) = ord(Zi), (p) (f |(M)) = ordZi, p(f ) ,

where in the rightmost equalities we used that both  and  are biholomorphisms onto

their image. But it is shown in lemma 7.4 below that if Ej is locally defined by f , then
Ej is locally defined by f   E . Therefore from the definition  = E   we obtain that

mult(Zi)(Ej, (M )) = mult(Zi)(Ej , (M )) .

To finish the proof, pick local holomorphic trivializations of the line bundles LAj with
complex coordinates wj on the fibre. These induce a holomorphic trivialization of

EA = L1A  � � �  LAd

with complex coordinates w1, . . . , wd on the fibre. It is clear that the submanifold Ej is
locally defined by the holomorphic function wj, and from (68) we get that

                             mult(Zi)(Ej, (M )) = ordZi, p (j) = aij ,

where in the last equality we used that, by construction of , Dj = i aij � Zi is the divisor
of the zero set of j regarded as a holomorphic section of LjA.

Lemma 7.3. In the construction above, different choices of divisors Dj lead to complex-
gauge inequivalent solutions (A, )  S^(P , E).

Proof. Let {Dj(1)} and {Dj(2)} be two sets of divisors satisfying conditions (i) and (ii),
and for r = 1, 2 let (Ar, r)  S^(P(r), E(r)) and (Ar , r )  S^(P , E) be the solutions
obtained by the construction above. Suppose furthermore that there exists a complex
gauge transformation g^ : M  TCn such that (A2, 2 ) = g^(A1, 1).

    It is shown in [21, p. 12 and 115] that there exists a subgroup H of T d such that
TCd = NC � HC, and so the exact sequence (62) splits. In particular there exists a gauge

                                                       46
transformation g : M  TCd such that g^ = ~C  g = g. From lemma 6.1 we then get
that [g(A1, 1)] = (A2 , 2 ). In particular, by lemma 7.2 and its proof, Dj(2) is just the
divisor of the zero set of g(1)j regarded as a holomorphic section of (L(1))gj(A1). But it is

well known that a complex gauge transformation does not change the zero set divisor of

a section of a line bundle, and so Dj2 coincides with the zero set divisor of (1)j regarded
as a holomorphic section of (L(1))jA1, which by construction of 1 is just Dj(1). This proves

the lemma.

Lemma 7.4. Fix a connection A  A1,1(P ) and take the complex structures on the
bundles E = P �T d Cd and E = P �T d F = P  �T d/N F to be the ones induced by A,
as in section 2.2. Let p be any point in Ej  E and suppose that, in some neighbourhood
of E (p), the submanifold Ej  E is locally defined by a holomorphic function f . Then
the submanifold Ej  E is locally defined by the holomorphic function f   E in some
neighbourhood of p.

Proof. Consider the projection E : E  E defined in (54). With respect to local
trivializations of E and E induced by the same trivialization of P , as in (9), the map E
is locally given by

E : U � Cd - U � F , (x, q)  (x, F (q)) ,                                        (70)

where F : Cd  F is the holomorphic quotient map. Now, using the local formula for
the complex structure J(A) on E and E, using the holomorphy of F , and using that

dF () = () for any vector   Rd  td, it is not difficult to show that dE commutes

with the complex structures J(A), i.e. that E is a holomorphic map. From the local

formula (70) it is also clear that E is a surjective submersion. Therefore, by the local
form of holomorphic submersions, there are neighbourhoods V  E of p, V   E of E (p)
and V   Cd-n of the origin such that E factorises as

E : V --- V  � V  --- V  ,                                                       (71)

where  is a biholomorphism and the rightmost arrow in the canonical projection.
    On the other hand, if f  is a holomorphic function on V  such that

                                   V   Ej = {x  V  : f (x) = 0} ,
then f   E is holomorphic on V and, by (67),

                                V  Ej = {x  V : f   E (x) = 0} .

47
Hence we only have to show that if the germ of f  at E (p) is irreducible, the germ of
f   E at p is irreducible as well. To do this, suppose that the germ of f   E is reducible.
Then shrinking the neighbourhoods V, V  and V  if necessary, we may assume that

f   E = h1 � h2  on V ,

where h1 and h2 are holomorphic functions of V that vanish at p. But (71) implies that
for all q  V 

                f (q) = f   E  -1(q, 0) = h1  -1(q, 0) � h2  -1(q, 0) .

Since the two functions hi  -1(�, 0) are holomorphic on V  and vanish at E (p), we
conclude that the germ of f  at E (p) is reducible as well, and this ends the proof.

8 Some comments

In this short and last section we will just make a few informal and not completely rigorous
comments about the general pattern of the vortex solutions found in sections 3, 5.1 and
7.2.

    In all the cases the solutions are characterized by a choice of hypersurfaces in M. These
cannot be arbitrary hypersurfaces, but must satisfy some topological constraints relating
their Poincar�e duals with the Chern numbers of the bundle P where the connection A
is defined. Once an allowed choice of hypersurfaces is made, there is a unique solution
of the vortex equations (up to gauge equivalence) such that the section  : M  E has
some prescribed values along the hypersurfaces. This prescription usually means that
along a given hypersurface the map , which can be locally regarded as having values
on the fibre F , is forced to have values on a certain complex submanifold of F . For
F = Cn and F = CPn these complex submanifolds are just the natural Cn-1's and
CPn-1's, respectively, contained in F . When F is a compact Ka�hler toric manifold these
submanifolds are the inverse images by the moment map � : F  Rn of the (n - 1)-
dimensional faces of the Delzant polytope   Rn characterizing F .

    The overall picture becomes clearer if one looks at simple examples, for instance F = C
or F = CP1. In the former case there is only one type of hypersurface to choose in M;
along these the Higgs field  vanishes and they are interpreted as the locations of the
usual vortices. In the latter case there are two types of hypersurface to choose in M: the

                                                       48
ones taken by  to the south-pole of CP1 (vortices), and the ones with image the north-
pole (anti-vortices). Still in the F = CP1 case, theorem 5.2 tells us that all hypersurfaces
contribute equally to the total energy of a solution (A, ), independently of their type.

    The significance of the hypersurfaces of M that characterize the solutions of the vortex
equations can be better understood by varying the real parameter a in these equations.
In order to do this fix the principal bundle P where the connection A is defined, fix an
allowed choice of hypersurfaces, and choose a moment map � : F  Rn such that the
origin is in the interior of the image polytope  = �(F ). Then for arbitrarily large a the
constant c(a, P, M) of (23) is in , and so solutions exist. Furthermore, by theorem 5.2,
the energy of these solutions tends to a finite constant as a  +. Now, if the energy
is to be kept constant, it is evident from (3) that as a grows the value of �   should
approach zero almost everywhere. On the other hand we know that along the chosen
hypersurfaces �   has values in some face of , and this is independent of a. Thus �  
tends to zero everywhere except along the hypersurfaces.

    Consider now the second vortex equation (13b). It tells us that, in the regions where �
 = 0 as a  +, the quantity FA must also become very large. Thus in some sense the
curvature of A, or the magnetic field, becomes localised around the chosen hypersurfaces
as a  +. Notice also that, becoming localised around the hypersurfaces, the curvature
FA should be related in some way to the Poincar�e duals of these hypersurfaces; this is in
fact what is expressed by condition (ii) of theorems 5.1 and 7.1.

    Thus as a tends to infinity the general picture is that the solutions (A, ) tend to
the vacuum solutions of the theory -- which are characterized by P trivial, A = 0 and
 = const.  �-1(0) -- except at the chosen hypersurfaces.

    The opposite limit is when the parameter a tends to zero. In this case it is apparent
from (3) that the energy functional tends to the pure Yang-Mills functional, and that the
section  does not contribute to the energy. The only relevant equations are then (13b)
and (13c), which become the Hermite-Einstein equations.

Acknowledgements. I am pleased to thank Prof. N. S. Manton for many discussions
and some observations included in section 8. I also thank the referee for his detailed
comments. I am supported by `Fundac�~ao para a Ci^encia e Tecnologia', Portugal, through
the research grant SFRH/BD/4828/2001.

                                                       49
Appendices

A Proof of propositions 5.4 and 5.5

The proof of proposition 5.4 is divided into the sequence of lemmas A.1-A.5. Lemma
A.1 is just auxiliary; lemmas A.2 and A.3 show that the map  is well defined and a
bijection, respectively; lemmas A.4 and A.5 establish the second assertion of proposition
5.4. Finally in the last two pages of this note we prove proposition 5.5.

    The proofs of lemmas A.1 and A.4 will be omitted, because they only consist of a
careful unwinding of definitions. We will not prove lemma A.5 either, since this is a
standard result.

Lemma A.1. Let A be a connection on P ,  a section of E, and denote by j and j,k
the connections induced by A on Vj and Lj,k, respectively. Then

            dA = 0  j(~j  ) = 0  j,k (~j  )k = 0 k ,

where (~j)k  (Lj,k) denotes the k-th component of ~j under the decomposition Vj =
   1kn Lj,k. Similar results hold when (dA, j, j,k) is substituted by (�A, j0,1, j0,,k1) or

(A, 1j,0, j1,,k0).

Lemma A.2. Let  : M  E be a section such that (M) Ej for all j, and let
A  A1,1(P ) be such that �A = 0. Then (~0  )k  (L0,k) is a non-zero meromorphic
section of L0A,k for all k = 1, . . . , n. Furthermore the condition (2) in the definition of C
is satisfied.

Proof. Given a point p  M pick a neighbourhood U of p and an index j  {0, . . . , n} such

that (U)  Ej = . By lemma A.1 we have that (~j  )k restricted to U is a holomorphic
section of LjA,k for all k = 1, . . . , n. Notice that these are non-zero sections, otherwise
(M) would be contained in some Ek, which contradicts the assumptions. Therefore, if
j = 0, we have just proved the result around p. If j = 0, then it follows from the definition
of Lj,k (see (39)) that L0,k = Lj,r  Lj-,11, where r is appropriately chosen among the values
k, k + 1 or  (in which case the term labelled by r should be omitted). Furthermore, the

form of the transition functions 0  j implies that

(~0  )k = (~0  ~j-1  ~j  )k = (~j  )r � [(~j  )1]-1  (A1)

            50
over U  -1(E \ Ej). But it follows from the definitions of the induced connections that,
also as holomorphic bundles,

                                         L0A,k = LAj,r  (LAj,1)-1 ,

and hence (~0 )k, being the quotient of two non-zero holomorphic sections, is a non-zero
meromorphic section over U.

    To end the proof we must now show that condition (2) is satisfied. From formula (A1)
and the holomorphy of the (~j  )l it is clear that the first part of (2) is obeyed, since the
negative part of the divisor of (~0  )k is just the divisor of (~j  )1. Moreover, for the
particular value k = j, the appropriate choice of r in (A1) is r = , and so the first factor
on the r.h.s. of (A1) should be omitted. This implies that the positive part of the divisor
of (~0  )j is zero, and hence the second part of condition (2) is trivially satisfied.

Lemma A.3. Let (1, 1, . . . , n, n) be a multiplet in the set C defined in section 5.2.
Then there is a unique connection A  A1,1(P ) and a unique section  : M  E such
that

  (i) �A = 0 and (M) Ej for all j;

 (ii) ~0  (q) = (1(q), . . . , n(q))  V0 for all q  -1(E \ E0);

(iii) The connection induced on L0,k by A is k.

Proof. We start by showing how to construct the connection A. Let s : U  P |U be
any local trivialization of P , and let sk : L0,k|U  U � C be the associated trivializations
of L0,k = Lk = P �k C. Since the connection k is both integrable and h0,k-compatible,
its connection 1-form associated to the hermitian trivialization sk satisfies ak  1(U; iR)
and dak  1,1(U ; iR). We then define the connection A  1(P ; tn) by the requirement

sA = . . . , (C-1)jk ak, . . .        1(U ; iRn  tn).  (A2)

k                               1jn

The usual standard calculation can be used to show that the connection thus defined does
not depend on the trivialization s, and so A is globally defined on P . Also FA = d (sA) is
in 1,1, because dak  1,1, and so A  A1,1(P ). Finally, by formula (32) the differential

   51
dk : tn  t can be identified with the matrix (Ckj) in M1�n(Z), and so the connection
1-form with respect to sk of the connection on L0,k induced by A is

d k  sA =       Ckj(C-1)jl al = ak .           (A3)

           j,l

This shows that the covariant derivative induced by A coincides with k, and so (iii)
is satisfied. From this construction it is also clear that the connection 1-forms (A2) are
the only ones that satisfy (A3) for all k = 1, . . . , n. This implies that the connection A
constructed above is the only connection on P that satisfies (iii).

    Now the construction of . Denoting by Wk  M the hypersurface of singular points
of the section k, we have that the map

~ := ~-0 1  (1, . . . , n) : M \ kWk - E \ E0  (A4)

is smooth, and we want to show that it can be extended to a smooth section  : M  E.
    Given an arbitrary q  kWk, choose a neighbourhood V of q and holomorphic triv-

ializations of the bundles L0,kk defined over V . With respect to these trivializations the
sections k are represented by non-zero meromorphic functions k , and shrinking V if
necessary, these can be written as k = fk/uk, where fk and uk are non-zero holomorphic
functions on V . Notice that, by the first part of condition (2) in the definition of C, the
functions uk can be chosen such that u1 = � � � = un =: u. Now, with respect to the
trivializations sk described at the beginning of the proof, the representatives of k are of
the form k = gk k , where gk is the transition function between sk and the holomorphic
trivialization of L0,k. Using (38) and the definitions of the charts 0, we therefore have
that

            ~0-1  (1, . . . , n) = s, [1, 1, . . . , n] = s, [ u, g1 f1, . . . , gn fn ]

over the domain V \ kWk. But the second part of condition (2) in the definition of C
says that the functions u, f1, . . . , fn never vanish simultaneously, and so the formula above
shows explicitly that ~ can be smoothly extended to V . By continuity this extension does

not depend on the various choices made, and by the arbitrariness of q we actually get a
global extension  : M  E. It is then obvious from (A4) that property (ii) is satisfied.

Furthermore, due to their meromorphy, the sections k are zero or singular only over
analytic hypersurfaces of M, and so there exists q  M such that the vectors j(q) are all
defined and non-zero. By formula (38), for example, we then get that (q)  Ej for all j,
and so the second part of (i) is also satisfied. Finally, using properties (ii), (iii) and lemma

                52
A.1 , we conclude that �A = 0 over M \ kWk; since both A and  are defined over the
entire M, by continuity we must have �A = 0 on M, and this establishes the existence

of the section . The uniqueness of  follows from condition (ii), also by continuity.

Lemma A.4. Let (A, ) and (A, ) be two pairs in B, and let (. . . , k, k, . . .) and
(. . . , k , k , . . .) be their images by . Then (A, ) and (A, ) are complex gauge equiva-
lent if and only if in each L0,k there is a complex gauge transformation that takes (k, k)
to (k , k ).

Lemma A.5. Let L  M be a complex line bundle equipped with a hermitian metric
h. Let also 1 and 2 be integrable h-compatible connections on L, and 1 and 2 be
non-zero meromorphic sections of L1 and L2, respectively. Then the pairs (1, 1) and
(2, 2) are complex gauge equivalent in L if and only if the meromorphic sections 1 and
2 have the same associated divisors in M.

Proof of proposition 5.5. We consider E equipped with the complex structure J(A).
Let Z  -1(Ej)  M be any irreducible analytic hypersurface, and let p be a generic
smooth point of Z. Take a local complex chart (z1, � � � , zm, w1, . . . , wn) of E, defined
around (p), such that the zk's are coordinates on the base M, the wk's are coordinates
on the fibre, and the submanifold Ej  E is given by the equation wr = 0. We will
construct such charts later on. Since p is a smooth point of Z, we may as well assume that
Z is locally defined by the equation z1 = 0. With respect to this chart, the holomorphic
section  : M  E is locally given by

        : z - (z, f1(z), . . . , fn(z)) ,

where z is the multiplet (z1, . . . , zm) and the fk's are locally defined holomorphic functions.

Write

       fr(z1, . . . , zm) = (z1)a g(z1, . . . , zm) ,  (A5)

where a  N0 and g is a holomorphic function such that g(0, z2, . . . , zm)  0. According
to the definition of [19, p. 130], we then have that

                                              a = ordZ,p(fr) .

    The idea now is to use the formula of [19, p. 65] to compute the intersection multiplicity
mult(Z)(Ej, (M)). Let H be the local submanifold of E defined by the equations z2 =

                                                       53
. . . = zm = 0. The tangent space T(p)H is C-generated by the vectors

                            ,      ,  .  .  .  ,      .
                        z1     w1                 wn

On the other hand, since  : M  (M) is a biholomorphism (see the proof of lemma
4.5), (p) is a smooth point of the irreducible variety (Z)  E, and the tangent space
T(p)(Z) is C-generated by

 + fl  : 2  k  m .
zk                      l zk wl

It is clear that T(p)E = T(p)H + T(p)(Z), i.e. H and (Z) intersect transversely at
(p).

    Now, using the inverse function theorem, it is not difficult to check that z1 together
with w~k = wk - fk(z1, 0, . . . , 0) define a local chart for H around p. On this chart
H  (M) is defined by the equations w~1 = � � � = w~n = 0, whereas H  Ej is defined
by wr = w~r + fr(z1, 0, . . . , 0) = 0. In particular H  (M) is a submanifold of H with
dimension 1 and coordinate z1. Hence, we have that for a generic smooth point p  Z,

mult(p) H  Ej, H  (M )  = ord(p) wr|H(M)                 = ordz1=0 fr(z1, 0, . . . , 0)
                        = a = ordZ,p(fr) ,

where we have used (A5) and that, for a generic p, g(0, . . . , 0) = 0. It then follows from
the formula of [19, p. 65] that

                                  mult(Z)(Ej, (M )) = ordZ,p(fr) .

We will now see what the right hand side of the above equality is.
    Start by noticing that, as in the proof of lemma A.2, there is an index l  {0, . . . , n}

such that, around p, (~l  )k is a holomorphic section of LlA,k for all k. Consider then the
local chart of E defined by

                                    ~l : E \ El - LlA,1  � � �  LlA,n ,

by local holomorphic trivializations of the LlA,k, and by a chart (z1, . . . , zm) of M around
p. This chart looks just like the one described at the beginning of the proof, with fk being
the representative function of (~l  )k with respect to the holomorphic trivialization of

                                   54
LAl,k. By the form of the charts l in (36), the submanifold Ej  E is then given by the
equation wr = 0, where r = j + 1 if j < l and r = j if j > l. Notice that j = l, by the
choice of l. In any case, by formulae analogous to (A1),

                          (~l  )r = [(~0  )l]-1 � (~0  )j = l-1 � j ,
where one should omit any  with index 0. Therefore

ordZ,p(fr) = ordZ (~l  )r = ordZ (j) - ordZ(l) .

Finally, by the holomorphy around p of

                          (~l  )k =     l-1 � k       if k > l
                                        l-1 � k-1     if k  l

for all 1  k  n, where one should omit any  with index 0, we conclude that

                          ordZ (l)      =  min  ordZ  (k  )  .

                                           0kn

This finishes the proof.

B Complex structures from connections

In this appendix we will prove proposition 2.4. This is a relatively straightforward exten-
sion of the proof given in [24] for the case where F is a vector space.

    Use the local trivialization (9) to identify E|U  U � F , where U is a domain in M,
and denote by JA the complex structure on U �F corresponding to J(A) on E|U . A vector
v  T (U � F ) with components v in T U and v in T F corresponds by the trivialization
to the vector

                          v~ = d [ds(v) + v]  T E .                         (B1)

Now decompose the vector ds(v) in T (P � F ) as

ds(v) = [ds(v) - A(ds(v))] + [(sA)(v) - (sA)(v)] + (sA)(v) , (B2)

where for any a  g we denote by a the associated fundamental vector field on P , and
by a the vector field on F induced by the left G-action. Then the first term of (B2) is

                                           55
in the horizontal space HA, the second in ker d, and the third in T F . By definition, the
complex structure J(A) preserves HA, ker dE, and satisfies

              dE  J(A)  d = JM  dE  d = JM  dP                      on HA
              J(A)  d = d  JF                                       on T F .

Hence on the one hand

dE  J(A)  d [ ds(v) - (sA)(v) ] = JM (v)
                                                    = dE  d [ ds  JM (v) - (sA)(JM v) ],

and since dE : HA  T M is an isomorphism,                                              (B3)

        J(A)  d [ ds(v) - (sA)(v) ] = d [ ds  JM (v) - (sA)(JM v) ]
                                                    = d [ ds  JM (v) - (sA)(JM v) ] .

On the other hand

J(A)  d [ v + (sA)(v) ] = d  JF [ v + (sA)(v) ] .                                      (B4)

Using (B1)-(B4) and the convention (17) we then obtain that

[JA(v)] = J(A) [v~]

            = d ds  JM (v) + JF [v + ( (sA)(v) + i(sA)(JM v) ) ]
            = JM (v) + JF [v + 2(sA)0,1(v) ]  .

Since the map v  v~ of (B1) is an isomorphism, we finally get that

JA (v) = JM�F [v + 2(sA)0,1(v)]                   T (U � F ) ,                         (B5)

where JM�F denotes the natural complex structure on the product M � F . This is
an explicit formula for the complex structure J(A) as seen through the trivialization
E|U  U � F ; we will rely on it to study the integrability of J(A).

Let U  � V   U � F be the domain of a complex chart {zj, wr} of U � F , where the

zj's and the wr's are coordinates on U  and V , respectively. For a given basis {k} of the

Lie algebra g, write over V                
                                          wr
                              (k)  =  kr      .

                                      56
Since the action transformations g : F  F are holomorphic, the vector fields k and the
functions kr are both holomorphic over V . Now consider the set of 1-forms over U  � V 

D = d zj, d wr + (sAk)0,1 kr : j = 1, . . . , dimC M and r = 1, . . . , dimC F .

Using formula (B5) and the fact that, with respect to JM�F , the forms dzj and dwr
are of type (1, 0) while (sA)0,1 is of type (0, 1), it is not difficult to check that all the

forms in D are of type (1, 0) with respect to JA. It is also apparent that they are linearly
independent at each point of U�V , and so we conclude that they generate the submodule
A1,0(U  � V ) of 1(U  � V ), where the splitting 1 = A1,0  A0,1 is with respect to the
complex structure JA. Now by basic results on complex manifolds, the complex structure
JA is integrable iff d 1A,0  2A,0  A1,1, and this last condition is clearly equivalent to

                         d   2A,0  1A,1                   for all   D .                      (B6)

Thus the problem is reduced to a simple computation. This computation yields

                                        d (d zj) = 0

and, modulo 2A,0  1A,1,

d (dwr + (sAk)0,1kr )  =    kr    (dwl  +     (sAn)0,1nl  )    (s Ak )0,1  -
                            wl
                                  kr              nr
                         -  1     wl    nl    -   wl  kl    (sAn)0,1  (sAk)0,1 + kr d(sAk)0,1
                            2

                       =    -  1  [n ,  k ]r  (sAn)0,1    (s Ak )0,1  + (k )r �(sAk)0,1
                               2

                               1                                                        0,2
                               2
                       =          ( [n, k]    )r  (sAn)      (s Ak )  +  (k )r  d(sAk)

                       = FA0,2 k k r ,

where FA is the curvature form on the base M. Hence (B6) is satisfied if and only if

                                  (FA0,2)kk = 0           on U  ,                            (B7)

and the first statement of the proposition is obviously true. As for the second statement,

suppose that at least one point in F has a discrete isotropy group. Then by well known

results almost every point in F has this property [10, p. 179]. In particular, for any point
p in an open dense subset of M, the linear map g  TpF defined by    is injective
and the vectors k |p are linearly independent. In this case if J(A) is integrable, i.e. if
(B7) is satisfied, necessarily FA0,2 = 0.

                                                  57
References

 [1] M. Abreu : `Ka�hler geometry of toric manifolds in symplectic coordinates'; in "Sym-
      plectic and contact topology: interactions and perspectives" , Fields Inst. Commun.,
      Vol. 35, Amer. Math. Soc., 2003.

 [2] M.F. Atiyah : `Convexity and commuting Hamiltonians'; Bull. London Math. Soc.
      14 (1982), 1�15.

 [3] D. Banfield : `Stable pairs and principal bundles'; Q. J. Math. 51 (2000), 417�436.

 [4] J.M. Baptista : `A topological gauged sigma model'; to appear in Adv. Theor. Math.
      Phys., hep-th/0502152.

 [5] N. Berline, E. Getzler and M. Vergne : `Heat Kernels and Dirac Operators'; Springer-
      Verlag, Berlin, 1992.

 [6] R. Bott and L. Tu : `Differential forms in algebraic topology'; Springer-Verlag, New
      York-Berlin, 1982.

 [7] S. Bradlow : `Vortices in holomorphic line bundles over closed Ka�hler manifolds';
      Commun. Math. Phys. 135 (1990), 1�17.

 [8] S. Bradlow : `Special metrics and stability for holomorphic bundles with global
      sections'; J. Differential Geom. 33 (1991), 169�213.

 [9] S. Bradlow and G. Daskalopoulos : `Moduli of stable pairs for holomorphic bundles
      over Riemann surfaces'; Internat. J. Math. 2 (1991), 477�513.

[10] G. Bredon : `Introduction to compact transformation groups '; Academic Press, New
      York - London, 1972.

[11] T. Bro�cker and T. tom Dieck : `Representations of compact Lie groups'; Springer-
      Verlag, New York, 1985.

[12] A. Cannas da Silva : `Lectures on symplectic geometry'; Springer-Verlag, Berlin,
      2001.

[13] K. Cieliebak, A.R. Gaio and D. Salamon : `J-holomorphic curves, moment maps, and
      invariants of Hamiltonian group actions'; Internat. Math. Res. Notices 16 (2000),
      831�882.

                                                       58
[14] K. Cieliebak, R.A. Gaio, I. Mundet i Riera and D.A Salamon : `The symplectic
      vortex equations and invariants of Hamiltonian group actions' J. Symplectic Geom.
      1 (2002), 543�645.

[15] P. Deligne and D. Freed : `Supersolutions.' in "Quantum fields and strings: a course
      for mathematicians", Vol. 1; Amer. Math. Soc., Providence, 1999.

[16] T. Delzant : `Hamiltoniens p�eriodiques et images convexes de l'application moment';
      Bull. Soc. Math. France 116 (1988), 315�339.

[17] M. Eto, Y. Isozumi, M. Nitta, K. Ohashi and N. Sakai : `Moduli space of non-abelian
      vortices'; hep-th/0511088.

[18] O. Garc�ia-Prada : `Invariant connections and vortices'; Comm. Math. Phys. 156
      (1993), 527�546.

[19] P. Griffiths and J. Harris : `Principles of algebraic geometry'; Wiley, New York, 1994.

[20] V. Guillemin and S. Sternberg : `Geometric quantization and multiplicities of group
      representations'; Invent. Math. 67 (1982), 515�538.

[21] V. Guillemin : `Moment maps and combinatorial invariants of Hamiltonian T n-
      spaces'; Birkh�auser, Boston, MA, 1994.

[22] A. Hanany and D. Tong : `Vortices, Instantons and Branes'; JHEP 0307 (2003) 037.

[23] F.C. Kirwan : `Cohomology of quotients in symplectic and algebraic geometry';
      Princeton University Press, Princeton, NJ, 1984.

[24] S. Kobayashi : `Differential geometry of complex vector bundles'; Princeton Univer-
      sity Press, Princeton, NJ; Iwanami Shoten, Tokyo, 1987.

[25] S. Kobayashi and K. Nomizu : `Foundations of differential geometry ', Vol. I; Wiley,
      New York, 1996.

[26] D. McDuff and D. Salamon : `Introduction to symplectic topology '; 2nd edition,
      Oxford University Press, New York, 1998.

[27] I. Mundet i Riera : `A Hitchin-Kobayashi correspondence for Ka�hler fibrations '; J.
      Reine Angew. Math. 528 (2000), 41�80.

                                                       59
      I. Mundet i Riera : `Yang-Mills-Higgs theory for symplectic fibrations '; Ph.D. Thesis,
      UAM (Madrid), April 1999, math.SG/9912150.
[28] I. Mundet i Riera and G. Tian : `A compactification of the moduli space of twisted
      holomorphic maps'; math.SG/0404407.
[29] B.J. Schroers : `The spectrum of Bogomol' nyi solitons in gauged linear sigma mod-
      els'; Nuclear Phys. B 475 (1996), 440�468.
[30] L. Sibner, R. Sibner and Y. Yang : `Abelian gauge theory on Riemann surfaces and
      new topological invariants'; Proc. Roy. Soc. London A 456 (2000), 593�613.
[31] C.H. Taubes : `Arbitrary N-vortex solutions to the first order Ginzburg-Landau
      equations'; Commun. Math. Phys. 72 (1980), 277�292.
[32] M. Thaddeus : `Stable pairs, linear systems and the Verlinde formula'; Invent. Math.
      117 (1994), 317�353.
[33] Y. Yang : `Solitons in field theory and nonlinear analysis '; Springer-Verlag, New
      York, 2001.

                                                       60
