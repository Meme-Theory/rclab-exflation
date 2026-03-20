# 2014 Vortices as degenerate metrics

**Source:** `12_2014_Vortices_as_degenerate_metrics.pdf`

---

arXiv:1212.3561v2 [hep-th] 4 Apr 2013            Vortices as degenerate metrics

                                                                             J. M. Baptista
                                                                                April 2013

                                                                                Abstract

                                       We note that the Bogomolny equation for abelian vortices is precisely the condition for
                                       invariance of the Hermitian-Einstein equation under a degenerate conformal transforma-
                                       tion. This leads to a natural interpretation of vortices as degenerate hermitian metrics
                                       that satisfy a certain curvature equation. Using this viewpoint, we rephrase standard
                                       results about vortices and make new observations. We note the existence of a conceptu-
                                       ally simple, non-linear rule for superposing vortex solutions, and we describe the natural
                                       behaviour of the L2-metric on the moduli space upon restriction to a class of submanifolds.

                                        Keywords: Vortex equation; degenerate Hermitian-Einstein metric; vortex superposition;
1 Introduction

The abelian Higgs model at critical coupling is a classical field theory defined on a hermi-
tian line bundle L  M over a Riemannian manifold. The variables are a U(1)-gauge field
A and a complex scalar field , or, geometrically, a hermitian connection and a smooth
section of the bundle. The theory is defined by the static energy functional

E(A, ) =                 1    |FA|2     +  |dA|2  +  e2  ||2 -   2,  (1)
                        2 e2                         2
                (M, g)

where FA is the curvature form, dA is a covariant derivative, and we have explicitly
inserted positive constants e2 and  . When the background (M, g) is a complex Ka�hler
manifold, this functional has the notable property of being minimized precisely by the
field configurations (A, ) that satisfy a set of first-order PDE's, called the abelian vortex
equations [Bra]. Denoting by  the Ka�hler form on (M, g), these equations read

                �A = 0                                               (2)

                i FA + e2 ||2 -  = 0                                 (3)

                FA0,2 = 0 ,                                          (4)

where FA stands for the contraction of the curvature with the Ka�hler form. The
equations make sense on any complex Hermitian manifold. Analytically, it is well known
that solving the abelian vortex equations is equivalent to solving the Kazdan-Warner
equation [Bra]. The latter is a classical, second order PDE, that originally appeared in
the problem of finding Riemannian metrics with prescribed scalar curvature [KW]. So in
some sense abelian vortices should be related to Riemannian metrics. Our aim here is to
formulate this relation in a natural way.

    Roughly speaking, our basic observation is that the vortex equations are precisely
the condition for invariance of the form (iF + e2 )  under the degenerate confor-
mal transformation    -1||2 . Here F denotes the Riemannian curvature form of
the Ka�hler metric on M, although this same observation can be extended to conformal
transformations of hermitian metrics on arbitrary complex vector bundles over M (cf.
Theorem 3.1). This observation has several interesting consequences. The first is that
when M is a Riemann surface, the most important case in the physics literature [MS],
studying abelian vortices is essentially equivalent to studying degenerate metrics on M
that satisfy a natural curvature equation. In Section 2 we explore this fact and rephrase
many of the standard results about vortices on surfaces in terms of degenerate metrics.
Arguably, features like the minimal volume bound and the special role of hyperbolic sur-
faces emerge more naturally from this viewpoint. However, the main new advantage of
the curvature equation is that it exhibits two obvious symmetries that are less manifest
in the traditional vortex equations. These symmetries imply the existence of a concep-
tually simple, non-linear rule for superposing vortex solutions, a fact that is physically

                                     1
and mathematically appealing, and that seems not to have been remarked before. As a
first application, this superposition rule and the interpretation of vortices as degenerate
metrics, taken together, suggest that a system of d vortices living on a surface with one
vortex constrained to a fixed position, should, somehow, be similar to a system of d - 1
free vortices living on that same surface equipped with an appropriately deformed back-
ground metric. Topologically, both systems have the same moduli space. In Section 2 we
define what "appropriately deformed" means and show that, with respect to the natural
L2-metrics, the two moduli spaces are isometric.

    In Section 3 we extend the discussion to vortices living on higher-dimensional Ka�hler
or Hermitian manifolds. We describe the relation between the abelian vortex equations
and the Hermitian-Einstein equation on complex vector bundles, and we examine how the
energy functional transforms under vortex superposition. In a final, brief paragraph, we
note that a slightly modified version of the abelian vortex equations, a version equivalent
to the perturbed Seiberg-Witten equations in the case of a Ka�hler surface, is in fact just
the condition for constant scalar curvature of the deformed metric  -1||2 . Although
we work on compact manifolds, a large part of the discussion is local, so follows through
to the non-compact case.

2 Vortices on Riemann surfaces

The curvature equation

Let M be a compact Riemann surface equipped with a Ka�hler form . Let L  M be a

hermitian line bundle over that surface and suppose that we are given a connection A and a
non-trivial section  of L such that �A = 0 . This condition means that  is a holomorphic
section with respect to the holomorphic structure on L induced by the connection A. In

particular,  vanishes at isolated points qj  M with a well defined, positive multiplicity
nj  Z. So a solution of (2) determines an effective divisor D = nj qj on the surface
M. Consider now the degenerate Ka�hler form on the surface defined by

                         := 1 ||2  .         (5)


This is a smooth 2-form on M that vanishes around each point qj as |z|2nj , where z is
a complex coordinate on M centered at qj. We will say that a Ka�hler metric with this
property is degenerate along the divisor D. Since on a surface equation (4) is always
satisfied, our basic question is the following: suppose that the pair (A, ) satisfies also the
vortex equation (3). What does this imply for the degenerate form ?

Proposition 2.1. The pair (A, ) satisfies the vortex equation (3) on M if and only if
the metric  is degenerate along D and satisfies

                        iF + e2  = iF + e2   (6)

                        2
over M \ {qj}, where F denotes the curvature form of the K�ahler metric .

Proof. The basic observation is that, away from the zeroes of , the curvatures are related
by FA = � log ||2 = F - F. See the proof of Theorem 3.1 for more details.

So the vortex equation is precisely the condition for the conformal transformation (5) to
preserve the form iF + e2 . Studying abelian vortices on (M, ) is the same thing
as studying Ka�hler metrics  that satisfy equation (6). Abelian vortices define such
degenerate metrics and, conversely, all vortex solutions are given by quotients of the form
/. The well known fact that there exists only one vortex solution (A, ) with nowhere
vanishing , up to gauge transformations, and that this solution has constant norm ||2 =
 , just means that  =  is the unique non-degenerate solution to the curvature equation
(6). Given an effective divisor D = nj qj on M, the well known fact that there exists
only one vortex solution (A, ) associated to D, up to gauge transformations [Bra, Gar,
JT], tells us that there exists a unique metric  on the Riemann surface that satisfies (6)
and is degenerate at the points qj  M with multiplicity nj.

Vortices on hyperbolic surfaces

Suppose that the initial metric  on the surface has constant scalar curvature equal to
-e2 . Equation (6) then reduces to iF +e2  = 0, whose solutions are again hyperbolic
metrics. Thus each vortex solution on (M, ) defines through (5) a degenerate hyperbolic
metric  with the same curvature -e2 . Conversely, all vortex solutions on (M, )
can be obtained as quotients  / of hyperbolic metrics. This is a familiar fact when
M = H is the hyperbolic half-plane. In this case, all degenerate hyperbolic metrics on
H can be obtained as pullbacks  = f  of the Poincar�e metric by Blaschke products
f : H  H. So all vortex solutions can be explicitly written as quotients (f )/, a fact
that was originally noted by Witten [Wi]. When (M, ) is a compact hyperbolic surface,
Manton and Rink noted that one can also obtain vortex solutions as quotients (f Y )/,
where (Y, Y ) is a second hyperbolic surface and f : M  Y is a ramified holomorphic
map [MR]. Unfortunately these maps are rare, so only isolated and non-explicit vortex
solutions can be obtained in this way (an upset that improves marginally if we accept
vortices with singularities [BB]). Our observation here is that, even in the compact case,
all vortex solutions can still be written as quotients of hyperbolic metrics on M. The
difficulty is that the degenerate metrics f Y provided by ramified maps represent only
a tiny subset of all the degenerate hyperbolic metrics on M.

Degenerate metrics

A word now about standard properties of degenerate metrics. Firstly, observe that the
Riemannian curvature form F has a smooth extension to the degenerate points, even

                                                        3
though the local 1-forms A of the Chern connection do not. In fact, around each qj  M

we can write

                         = |z|2nj fj  ,            (7)

where fj is a smooth and positive function locally defined around qj. It follows that the
Levi-Civita (or Chern) connection is given by

              A = A + nj z-1dz + (log fj)

in a local holomorphic trivialization of T M. So the connection is singular at the degenerate
points and the residues nj can be probed by integrating A around small circles centered
at the qj's. On the other hand, the curvature

                                   F = dA = F + �(log fj)

can be smoothly extended to the degenerate points qj. Note that the last term in the
equation above, although locally exact, is not globally exact, since the functions fj are
not globally defined. In fact, one can check that if  is defined by (5) and the pair (A, )
solves the holomorphy equation (2), then away from the zeroes of  we have

                        F = F + FA ,               (8)

where, again, FA is the curvature of the U(1)-connection A. This identity is another way
to recognize that F can be smoothly extended to the whole M. However, note that this
smooth extension is not globally a curvature form, because the Levi-Civita connection
has singularities. In particular, one cannot directly apply Stokes' theorem to F over
domains that contain degenerate points. The Gauss-Bonnet theorem in its usual form is
also not applicable to the smooth extension of F, as the integral of identity (8) yields

               i          F = (2 - 2g) +     nj ,  (9)
              2
                  M \{qj }                j

where g is the genus of M. To remedy these undesirable features, one usually considers
an extension of the curvature F to the degenerate points that is different from the
smooth one. This second extension regards the curvature of the degenerate metric as an
integration current, and is defined by

              F :=  dA     over M \ {qj}           (10)

                    2i nj (qj) at each point qj ,

where (qj) is the delta function. Thus, at the price of considering distributions, the usual
formulae are applicable to the curvature, and we have for instance

                     i    F = (2 - 2g) .
                    2
                        M

                        4
Defining the curvature of a degenerate metric to have delta functions at the points qj also
makes sense if we think of the degenerate metric as a limit of non-degenerate metrics.
In this case one can check that the curvature of the non-degenerate metrics increases at
qj as these metrics tend to zero at qj, and the limit will be a delta function. Moreover,
since the curvature of all the non-degenerate metrics satisfies Gauss-Bonnet, it is natural
to define a limit curvature F that also satisfies Gauss-Bonnet. Observe that if we use
integration currents on M, the curvature equation (6) should be rewritten as

iF + e2  = iF + e2  - 2 nj (qj) ,                  (11)

                                          j

and this is an equation over the whole surface. Comparing with (6), we see that the delta
functions encode the boundary conditions for  at the degenerate points. They play
exactly the same role here as in the original Taubes' equation for abelian vortices [JT].

Minimal volume bound

Integrating the curvature equation (6) over M \ {qj}, or integrating equation (11) over
the whole M, we see that each solution  must satisfy

Vol(M, )              =  Vol(M, )  -  2      nj .
                                      e2
                                          j

Thus each additional degeneracy (i.e. vortex) reduces the volume of the metric  by
2/(e2 ). Since any Riemannian metric with a finite number of degenerate points certainly
has positive volume, we also conclude that a necessary condition for the existence of
solutions of the curvature equation is that

                                      2 nj < e2 Vol(M, ) .

                                                                  j

This, of course, is just the standard condition for the existence of vortex solutions asso-
ciated to a non-zero divisor on M [Bra].

Remark. The interpretation of vortices as a deformation of the background Riemannian
metric satisfies basic intuitive properties. For instance, it is known that the rescaling
factor  -1||2 tends exponentially fast to the vacuum value 1 as one gets away from the
vortex core, at least for vortices on the flat plane [JT]. So the background metric  is
substantially deformed only in a very localized region around the vortices. Moreover,
an application of the maximum principle says that the conformal factor is bounded by
0   -1||2  1 over the entire surface M [JT, Bra]. Hence the total deformation of the
background metric  can be measured by the diference of volumes Vol (M, )-Vol (M, ),
which is proportional to the vortex number.

                         5
Hidden symmetries and vortex superposition

The interpretation of abelian vortices as degenerate metrics exposes two symmetries of
the vortex equations that are less manifest in their usual form. The first is the fact that
the curvature equation (6) is essentially symmetric in  and . If  is a solution on
the background (M, ), then  is a solution on the background (M, ). To interpret this
in terms of the usual vortex equations requires working with meromorphic sections .
The observation is that if (L, , A) is a solution of (3) on (M, ), then (L-1, -1, -A) is
a solution on the background (M,  -1||2 ). Meromorphic sections appear because the
boundary conditions at the degenerate points make the curvature equation not exactly
symmetric in  and . This is most manifest in the form (11) of the equation, where an
interchange of the two metrics requires an accompanying change of sign of the divisor in
order to preserve the equation.

    The second hidden symmetry is a transitivity property. If  is a solution of the
curvature equation (6) on the background (M, ) and  is a solution on the background
(M, ), then  is a solution on the background (M, ). This is evident from

                        iF + e2  = iF + e2  = iF + e2  .

In the usual formulation of vortices, this transitivity corresponds to the observation that
if (L1, 1, A1) is a vortex solution on (M, ) and (L2, 2, A2) is a vortex solution on the
degenerate background (M,  -1|1|2 ), then the tensor product of hermitian bundles
(L2  L1,  -1/22 1, A2 + A1) is a vortex solution on the original background (M, ). It
is straightforward to check this directly using equation (3). The basic identity is

iFA2+A1 + e2  -1|12|2-  = iFA2 + e2 |2|2- ( -1|1|2) + iFA1 + e2 |1|2-  .

This property of vortex solutions is very appealing and, apparently, has not been remarked
before. It says that we can construct a (d1+d2)-vortex solution on (M, ) by first obtaining
a d1-vortex solution on (M, ), then deforming the background  to the degenerate metric
 -1|1|2  dictated by that first solution, and finally solving the equation for d2-vortices on
the deformed background. We can also do it the other way around, of course, solving for
d1-vortices on the background deformed by d2-vortices. This amounts to a conceptually
simple, non-linear rule for superposing vortices. Again, it states that instead of na�ively
multiplying vortex solutions obtained on the same background, the correct prescription to
superpose vortices implies using a second solution obtained on the background deformed
by the first solution. If one knew how to solve the 1-vortex equation on any background,
a recursive application of this rule would yield the d-vortex solution on any background.

Energy functional

As mentioned in the introduction, a basic fact about the vortex equations is that they
minimize the static energy of the abelian Higgs model at critical coupling, i.e. they

                                                        6
minimize the energy functional (1). One may thus wonder how to rephrase this in terms

of degenerate metrics. Given an effective divisor D = njqj on a surface (M, ), we
define the energy density of a Ka�hler metric  that degenerates along D by

E ()     :=    1   |F  -  F |2  +   2 |d  / |2   +          e2 2  |  -  |2  .  (12)
              2e2                                            2

This a smooth function on M \ {qj}. It can be rewritten as

E ()  =   1   F - F - ie2 ( - ) 2         +  i   F - F + �(/)
         2e2

over that domain, where  is the Hodge operator with respect to . Using equation (9)
and Stokes' theorem, it is clear that the total energy functional satisfies

              E() :=                E ()   2 nj ,

                          M \{qj }               j

with the equality standing precisely when  satisfies the curvature equation (6) over
M \ {qj}. This is the analog of the usual Bogomolny argument for vortices.

Remark. At first sight one could be worried that the square root term appearing in the
energy density (12) may lead to singularites at the points where  vanishes. However, a
direct calculation shows that if  vanishes at qj as |z|2nj , the squared norm |d / |2
is smooth at that point for any integer nj  0.

Remark. In this discussion we have fixed the degeneration divisor D, have only consid-
ered metrics  with the boundary conditions prescribed by D, and the integrals are over
the domain M \ supp D. An equivalent approach would be to consider the curvature F
as an integration current over the entire M, as in (10), and then encode the boundary
conditions in delta functions appearing in the energy density. In this case one should
substitute the term F - F in the formulae above by F - F + 2(D) and perform
the integrations over the whole M.

Metric on the moduli space

It is well known that for each effective divisor D = njqj on the surface M there is exactly
one solution of the vortex equations (2) and (3), up to U(1)-gauge transformations, such
that D is the zero-set divisor of the Higgs field . So if we fix the degree of D to be
d and let the points qj vary in M, we get a moduli space Md of vortex solutions that
is isomorphic to the symmetric product SymdM of the surface. In terms of degenerate
metrics, Md is the space of solutions of the curvature equation (6) such that the Ka�hler
metric  has d degenerate points on M, counting multiplicities.

    The space Md has a natural Ka�hler metric induced by its interpretation as a vortex
moduli space [MS]. Using the language of [Ba, Sect.7], the corresponding Ka�hler form

                                                        7
M can be written in terms of the degenerate metrics as

M  =  -1       z u�k log f z�uj log f dz  dz� duj  du�k ,  (13)
      2 e2
            M

where f (, p) := (/)(p) is a non-negative smooth function on the cartesian product

Md � M, and we chose arbitrary local complex coordinates z on M and {uk} on Md.

Observe that in (13) the integrand 2-form is exact outside the points where log f explodes,

i.e. outside the degenerate points of the metric . By Stokes' theorem, the integral

therefore localizes to a sum of integrals around small circles centered at these degenerates

points, which of course is just the standard Samols' localization for vortices [Sa, Ba]. Note

also that due to the presence of the partial derivatives u�k and uj , the form M does
not depend explicitly on the background metric  on the surface, though it does depend

implicitly through the solutions .

    Formula (13) and the superposition rule for vortices imply that the metric M on the

moduli space has an interesting property upon restrictions, which we now explain. Let
Mpd  Md be the complex submanifold determined by fixing one vortex at position p  M,
i.e. Mdp is the subset of unordered multiples in SymdM of the form (x1, . . . , xd-1, p) with
varying xk  M. As a complex manifold, Mdp clearly is isomorphic to Md-1. However, the
Ka�hler metric on Mpd induced by the embedding in (Md, M) is different from the natural
metric on Md-1 regarded as the moduli space of d - 1 vortices living on (M, ). In other

words, the remaining d - 1 vortices "feel" the presence of the vortex fixed at p. But how,
precisely, does this presence translate into the metric on Mpd? In view of superposition
rule discussed before, a natural guess is that the vortex fixed at p deforms the background
metric  on the surface M to another metric , a metric that is degenerate at p, and
then the remaining d - 1 vortices behave as free vortices on the surface (M, ). To be

more precise:

Theorem 2.2. Let  be the unique solution of the curvature equation (6) on (M, )

with a single simple degeneracy at the point p  M. Then the submanifold Mpd equipped
with the metric inherited from (Md, M) is isometric to the moduli space Md-1 of d - 1
vortices living on the background surface (M, ).

Proof. Take a local chart {uk} of the moduli space Md adapted to the submanifold Mpd.
This means that in this chart Mdp is determined by the equation ud = 0 and {u1, . . . , ud-1}
are good complex coordinates on Mpd. For any solution   Mpd of the curvature equation

on (M, ), we can always factorize

                                      =       .


The crucial observation is that the factor / is constant on the submanifold Mdp, it
does not depend on the positions of the remaining d - 1 vortices. So for the coordinates
{u1, . . . , ud-1} we have

                                    uj log(/) = uj log(/)

                                         8
over Mpd, and the same applies to the anti-holomorphic derivatives. Thus the restriction
of the Ka�hler form (13) to the submanifold Mdp is given by the same formula (13), except
that we only use the coordinates {u1, . . . , ud-1} and the function f is now /. This

coincides with the formula for the Ka�hler form on the moduli space Md-1 of d -1 vortices

living on the background surface (M, ).

    There is an obvious extension of this property to the lower dimensional submanifolds

Md              of  the  moduli     space  Md  determined   by   fixing  the  positions  of  l  <  d  vortices.
     p1,...,pl

It  says  that      Md              equipped  with  the  metric  inherited  from  (Md, M)       is    isometric
                         p1,...,pl

to the moduli space Md-l of d - l vortices living on the background surface (M, ),

where this time  is the unique solution of the curvature equation on (M, ) with simple

degeneracies at the points p1, . . . , pl.

Vortices with parabolic singularities

So far we have only considered degenerate metrics  on M that vanish with a positive
integral power |z|2nj at the degenerate points qj. However, pretty much the whole story
can be extended to metrics that vanish as |z|2j for real numbers j > 0. These correspond
to abelian vortices on (M, ) with parabolic singularities.

    Suppose that we are given a divisor j qj on M with positive real coefficients.
Denote by [j]  Z the integral part of j, and call L  M the complex line bundle of
degree j[j]. Let h be a hermitian metric on L with parabolic singularities of weight
j - [j] at the points qj. This means that if s is a smooth local section of L that does
not vanish at qj, the squared norm of s is of the form

                                        |s|h2 = |z|2(j -[j]) fj(z, z�)

for some smooth and positive function fj defined around qj. So h is degenerate at the
points qj, and all unitary connections on (L, h) will have logarithmic singularities at those
points. However, this degeneracy does not affect the existence of vortex solutions. There
still exists a smooth section  of L and a unitary connection A that solve the vortex
equations (2) and (3) over M \ {qj}, and such that  vanishes precisely at points qj with
multiplicity [j]. Moreover, this pair (A, ) is unique up to U(1)-gauge transformations
on M [BiGa]. Observe that for this solution the squared norm ||h2 vanishes as |z|2j at
the point qj. Therefore the Riemannian metric  :=  -1||h2  satisfies the curvature
equation (6) over M \ {qj} and is degenerate along the divisor jqj, as required. All in
all, we see that studying vortices on (M, ) with parabolic singularities is the same thing
as studying solutions  of (6) that vanish with positive real weights. All the formulae
presented above remain valid if we substitute the integers nj by the real weights j.

Remark. The existence and uniqueness of vortex solutions, and hence of solutions to (6)
with prescribed degeneracies, has also been extended to the case where the background

                                                         9
metric  is allowed to have degeneracies or conical singularies, meaning that at a finite

number of points pk  M, possibly coincident with the qj's, the background Ka�hler form
 behaves as |z|2k with real weights k > -1 [BB].

3 Vortices in higher dimensions

In the previous Section we have seen how the vortex equation (3) can be regarded as the
condition for the conformal transformation (5) to preserve the form iF + e2 . Observe
that the metric  plays here a double role, both as a Riemannian metric on M and as
a hermitian metric on T M with curvature F. If we separate these roles and substitute
T M by an arbitrary holomorphic vector bundle, it becomes clear that the vortex equation
is in fact the condition for invariance of the general Hermitian-Einstein equation under a
conformal transformation. Moreover, this is true on any Hermitian manifold M, not just
on Riemann surfaces.

Let (M, ) be a compact Hermitian manifold and let L  M be a hermitian line

bundle. Suppose that we are given a connection A and a non-trivial section  of L such

that

             �A = 0 ,        FA0,2 = 0 .                                          (14)

Then  is a holomorphic section with respect to the holomorphic structure on L induced by

the connection A. In particular, its zero set determines an effective divisor D = j nj Zj
of analytic hypersurfaces on M. The squared norm ||2 is a smooth function on M that

vanishes along the support of D. Now let V  M be a holomorphic vector bundle

equipped with a hermitian metric f . We can consider the double rescaling

      f  :=  1  ||2  f  and    :=  1      ||2                                     (15)


for any exponent  = 0. Then , for instance, is a smooth 2-form on M that vanishes
at each hypersurface Zj as |z|2nj , where z is a complex coordinate on M such that Zj is
locally defined by the equation z = 0. In the language of Section 2, the degeneracies of 
and f  are prescribed by the divisors D and D, respectively. Once again, our question

is the following: suppose that the pair (A, ) satisfies the vortex equation (3). What does
this imply for the degenerate metrics f  and ?

Theorem 3.1. The pair (A, ) satisfies the vortex equation (3) on M if and only if the
metrics  and f  defined by the conformal transformation (15) satisfy the equation

      i Ff + e2    = iFf + e2                                                     (16)

over M \ jZj, where Ff denotes the curvature of the Chern connection on (V, f ).

In other words, the abelian vortex equation (3) is precisely the condition for invariance of
the form iFf + e2   under the degenerate conformal transformation (15). The

                        10
existence of smooth vortex solutions has been proved by Bradlow in the case of Ka�hler
(M, ) [Bra], and by Lupascu in the case of Hermitian manifolds [Lu].

Remark. Choose V = T M, f =  and  = 1. Observe that if the initial metric 
satisfies the Hermitian-Einstein condition iF + e2 I = 0, then each vortex solution
on (M, ) gives us a new degenerate metric  on M that satisfies the same condition.
Taking the trace in equation (16), we see that if the initial metric  has constant scalar
curvature s = Tr(iF) = -e2 dimC M (not necessarily being Hermitian-Einstein),
then each vortex solution on (M, ) gives us a new degenerate metric  with the same
scalar curvature. However, note that if (M, ) is a higher-dimensional Ka�hler manifold,
the rescaled forms  are no longer d-closed for non-trivial , and hence will only define
Hermitian metrics on M.

Remark. Just as in the case of Riemann surfaces, if we regard the curvature Ff of a
degenerate metric as an integration current, the domain of equation (16) can be extended
to the entire manifold M. In this case one should add a delta function term the curvature
equation, a term that encodes the boundary conditions in (16). The equation over M
then becomes

iFf + e2    = iFf + e2    - 2 D ,  (17)

where D denotes the current of integration over the divisor D. That this is the correct
term to add, is a consequence of the Poincar�e-Lelong formula �(log ||2) = FA + 2iD

applied to the line bundle L.

Proof of Theorem 3.1. Let h denote the background hermitian metric on L. Since the
pair (A, ) satisfies equations (14), there exists a holomorphic structure on L such that A
coincides with the Chern connection and  is a holomorphic section. In a local holomorphic
trivialization of L, the curvature of the Chern connection A is given by FA = �(log h).
Since  is holomorphic, away from its vanishing set we have that � log(�) = 0. Hence
on M \ jZj the curvature is given by FA = �(log ||2h). On the other hand, in a local
holomorphic trivialization of the vector bundle V , the curvature of the Chern connection
is given by the analogous formula Ff = �[(f )f -1], where the hermitian metric f should
be locally regarded as a square matrix of dimension equal to the rank of V [CCL, p. 256].
In particular

Ff - Ff = � (f )(f )-1 - (f )f -1 = � (f )f -1(f f -1)-1 + (f f -1)-1f (f -1)
              = � [ (f )f -1 + f (f -1) ] (f f -1)-1 = � log (f f -1) =  FA I ,

where I stands for the identity automorphism of V and we have used that f f -1 =
||2 ( )-1 I commutes with all matrices. Thus on M \ jZj we have that

         iFA + e2 ||2 -    = i(Ff)  - i(Ff )  + e2   ( - ) ,

and the result follows.

11
Vortex superposition and the energy functional

The curvature equation (16) has the same symmetry and transitivity properties that were
discussed in the case of vortices on Riemann surfaces. It follows that the superposition
rule of Section 2 is still valid for abelian vortices over higher-dimensional M. In the
traditional form of the vortex equations, this follows from the Leibniz rule

              �A2+A1( -1/2 2 1) =  -1/2 2 �A1 1 +  -1/2 1 �A2 2 ,

from the A-linearity of the curvature of abelian connections

                             F 0,2        =    FA02,2  + FA01,2 ,
                               A2 +A1

and from the identity

   iFA2+A1 + e2  -1|12|2 -   = i FA2 + e2 |2|2 -   +

                                                                      + iFA1 + e2 |1|2 -   ,

where  denotes the deformed hermitian metric  -1|1|2. So if D1 and D2 are two
effective divisors on a Hermitian manifold (M, ), we can construct the vortex solution
associated to D1 + D2 by first obtaining the solution (A1, 1) on (M, ) associated to D1,
then deforming the background  to the degenerate metric  =  -1|1|2  dictated by
that first solution, and finally obtaining the D2-vortex solution on the new background.

    One may wonder if this superposition rule for BPS vortices could be a reflex of a
stronger structural symmetry of the theory, for instance a decomposition rule of the energy
functional when evaluated on composed fields like (A1 + A2,  -1/212). Unfortunately
such a strong symmetry does not seem to hold in general. However, it may be worth to
present a few observations in this direction. Start by recalling the energy functional of
the abelian Higgs model defined in (1). A version of the Bogomolny argument [Bra] says
that this functional can be rewritten as

                       E(A, , ) = T (A, , ) + E(A, , ) ,                                     (18)

                                                           M

where we have separated the non-negative density

E(A, , ) :=             1    iFA + e2      2-          2   +  2  �A  2  +  2   FA0,2  2  m
                       2e2                                                 e2            m!

from the remaining integral

T (A, , ) :=     i     FA      m-1     +   1   FA      FA       m-2     -  id , dA           m-1    .
                             (m - 1)!     2e2                 (m - 2)!                   (m
              M                                                                              - 1)!

(Here the inner product , dA = h � dA uses the background hermitian metric h
on L.) The non-negative density E vanishes precisely when the vortex equations are

                                               12
satisfied. The integral T is independent of the fields (A, ) whenever the form  is closed,
i.e. whenever the background (M, ) is Ka�hler. The well known conclusion is that for
Ka�hler  the field configurations that minimize the total energy E(A, , ) are precisely
the vortex solutions. For a general Hermitian background, a priori this need not be true.

    Our first observation follows from a direct computation using the definition of E.

Proposition 3.2. Let (A1, 1) be a vortex solution on a Hermitian manifold (M, ) and,
as usual, let  denote the deformed metric  -1|1|2 . Then we have that

E (A + A1,  -1/2 1, ) =  -1|1|2 2-m E (A, , )                                         (19)

for arbitrary fields (A, ).

This is a remarkably simple transformation rule. In particular, if the fields (A, ) are
a vortex solution on (M, ), the density E(A, , ) vanishes everywhere, and so does
the density on the left-hand-side of (19), which in turn means that the superposed fields
(A + A1,  -1/2 1) satisfy the vortex equations on (M, ). So the vortex superposition
rule can be directly read from (19).

    Moreover, notice the special stand of complex dimension m = 2 in identity (19) . In
this dimension the operation of superposing a vortex solution to arbitrary fields can be
entirely absorbed in a deformation of the background metric , as far as the density E is
concerned. Unfortunately the same statement does not hold for the full energy functional
E(A, , ). The reason is that the deformed metric  is not Ka�hler, and hence the term
T (A, , ) is no longer topological, i.e. it depends on the fields (A, ). This means that
the energy E is no longer the same, up to a constant, as the integral of E. However,
one can define a "corrected" energy E^ that does transform nicely upon composition with
vortex solutions. Still in complex dimension m = 2, put

              E^(A, , ) := E(A, , ) + -i FA   + i d , dA   .

                                                                                   M

Bearing in mind identities (18) and (19), it is manifest that:

(i) On a fixed compact Ka�hler background (M, ), the functionals E and E^ differ only
     by a topological constant.

(ii) On a general compact Hermitian background (M, ), given a vortex solution (A1, 1),
      the functional E^ satisfies

                             E^(A + A1,  -1/2 1, ) = E^(A, , )                        (20)

for arbitrary fields (A, ).

This means that in the classical theory defined by E^, composing the fields with a vortex
solution is fully equivalent to deforming the background metric.

                             13
The modified vortex equation

As before, let L  M be a hermitian line bundle and let (A, ) be a pair that satisfies

the holomorphy equations (14). We assume that  is non-trivial, so that its zero set

determines an effective divisor D = j nj Zj on M. A modified version of the vortex
equation has been often considered, namely

                       i FA      +         1   ||2 + s          = 0,  (21)
                                       dimC M

where s = i Tr(F) denotes the scalar curvature of (M, ). When M is a Ka�hler
surface, this equation is equivalent to a perturbation of the Seiberg-Witten equations

[BG]. For compact Ka�hler (M, ), it can be shown that the existence of solutions to (21)

depends only on the average value

                                 s�  :=        1             s
                                          Vol (M, )
                                                       (M,)

of the scalar curvature of . Solutions (A, ) of (21) exist if and only if the vortex

equation (3) with  = -s� has solutions [BG]. In particular, we must have s� < 0
for non-trivial solutions to exist. For a general compact Hermitian manifold (M, ), the

existence condition is slightly more evolved [Lu]. Equation (21) also has a very simple

interpretation in terms of degenerate metrics. As usual, for given data (L, M, , A, ),

define the deformed metric                    -1
                                              s�
                                          :=      ||2    .

Proposition 3.3. The pair (A, ) satisfies the modified vortex equation (21) on M if and

only if the degenerate metric  has constant scalar curvature s = s� over M \ jZj.

Proof. If K  M denotes the canonical line bundle, the induced hermitian metric on K

rescales as                               -1         dimC M
                                          s�
                            det  =             ||2h          det  .

Using that FA = �(log ||2) away from the vanishing set of , as before, it is clear that

the real Ricci form transforms as

                        = i� log(det ) = i (dimC M ) FA + 

over M \ jZj. Thus over this domain we get that

i FA  +          1  M  ||h2 + s        =      1      (  )  - ()  - s�  + s 
             dimC                         dimC M

and the result follows from the identity  = s.

Acknowledgements. It is a pleasure to thank Dennis Eriksson and Nick Manton for
helpful discussions about integration currents and vortex superposition, respectively. I
also thank CAMGSD and Project PTDC/MAT/120411/2010 of FCT - POPH/FSE for a
generous fellowship.

                                                       14
References

[Ba] J. Baptista: On the L2-metric of vortex moduli spaces, Nucl. Phys. B 844 (2011),
          308�333.

[BB] J. Baptista and I. Biswas: Abelian vortices with singularities, arXiv:1207.0863.
[BiGa] O. Biquard and O. Garc�ia-Prada: Parabolic vortex equations and instantons of

          infinite energy, Jour. Geom. Phys. 21 (1997), 238�254.
[Bra] S. Bradlow: Vortices in holomorphic line bundles over closed Ka�hler manifolds,

          Commun. Math. Phys. 135 (1990), 1�17.
[BG] S. Bradlow and O. Garc�ia-Prada: Non-abelian monopoles and vortices, Geometry

          and Physics, Lecture Notes in Pure and Appl. Math. 184, 567�589, Dekker, 1997.
[CCL] S. Chern, W. Chen and K. Lam: Lectures on Differential Geometry, World Sci-

          entific, 1998.
[Gar] O. Garc�ia-Prada: Invariant connections and vortices, Commun. Math. Phys, 156

          (1993), 527�546.
[JT] A. Jaffe and C. Taubes: Vortices and monopoles, Birkhauser, 1980.
[KW] J. Kazdan and F. Warner: Curvature functions for compact 2-manifolds, Annals

          of Math. 99 (1974), 14�47.
[Lu] P. Lupascu: The abelian vortex equations on Hermitian manifolds, Math. Nachr.

          230 (2001), 99�115.
[MR] N. Manton and N. Rink: Vortices on hyperbolic surfaces, Jour. Phys. A 43 (2010),

          434024.
[MS] N. Manton and P. Sutcliffe: Topological Solitons, Cambridge Univ. Press, 2004.
[Sa] T. Samols : Vortex scattering, Commun. Math. Phys. 145 (1992), 149�179.
[Wi] E. Witten: Some exact multipseudoparticle solutions of classical Yang-Mills the-

          ory, Phys. Rev. Lett. 38 (1977), 121�124.

Centre for Mathematical Analysis, Geometry, and Dynamical Systems (CAMGSD),
Instituto Superior Te�cnico, Av. Rovisco Pais, 1049-001 Lisbon, Portugal

Email address: [email redacted]

                                                       15
