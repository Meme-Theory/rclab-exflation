# 2004 Special Kahler metrics on SL2C

**Source:** `02_2004_Special_Kahler_metrics_on_SL2C.pdf`

---

arXiv:math-ph/0306060v1 24 Jun 2003                                                                                           DAMTP-2003-59

                                       Some special K�ahler metrics on SL(2, C)
                                          and their holomorphic quantization

                                                                         J. M. Baptista

                                                         Department of Applied Mathematics and Theoretical Physics
                                                                                 University of Cambridge

                                                                Wilberforce Road, Cambridge CB3 0WA, England

                                                                            June 2003

                                                                            Abstract

                                         The group SU(2) � SU(2) acts naturally on SL(2, C) by simultaneous right and
                                     left multiplication. We study the Ka�hler metrics invariant under this action using a
                                     global Ka�hler potential. The volume growth and various curvature quantities are then
                                     explicitly computable. Examples include metrics of positive, negative and zero Ricci
                                     curvature, and the 1-lump metric of the CP 1-model on a sphere.

                                         We then look at the holomorphic quantization of these metrics, where some physi-
                                     cally satisfactory results on the dimension of the Hilbert space can be obtained. These
                                     give rise to an interesting geometrical conjecture, regarding the dimension of this space
                                     for general Stein manifolds in the semi-classical limit.

                                         e-mail address: [email redacted]
Part I

1 Introduction

Among the geometrical procedures for quantization, holomorphic quantization is a
particularly simple and natural one, and can be used whenever the classical system
"lives" on a complex Ka�hler manifold. In this paper the complex manifold under study
will be SL(2, C), and we will consider the Ka�hler metrics on this manifold which are
invariant under a natural action of the group SU(2)�SU(2), namely the action defined
by simultaneous right and left multiplication of the matrix in SL(2, C) by the matrices
in SU(2).

    In the first part of the paper a purely classical study of these Ka�hler metrics is
carried out. We find that each of these metrics has a global invariant Ka�hler potential,
which is essentialy unique, and is in fact a function of only one real variable. We then
use this potential to compute explicitly several properties of the Ka�hler manifold. These
include the scalar curvature, a potential for the Ricci form, the volume and volume
growth, the geodesic distance from the submanifold SU(2)  SL(2, C), and a simple
criterion for completeness. Choosing particular functions as Ka�hler potentials we get
metrics with positive-definite, negative-definite and zero Ricci tensor; the Ricci-flat one
being just the usual Stenzel metric on T S3  SL(2, C).

    A significant application of the above results, which was in fact the original motiva-
tion for this paper, is a closer study of the L2-metric on the moduli space of one lump
on a sphere. These lumps are a particular kind of soliton that appear in CP 1-sigma
models, and have been widely studied [2, 13]. In particular, the special case of one lump
on a sphere has been studied by Speight in [10, 11], where the author also examines
general invariant Ka�hler metrics on SL(2, C) and finds some of the results mentioned
above. The approach there however is rather different, since it is based on the choice
of a particular frame for T SL(2, C), instead of using the perhaps more natural Ka�hler
potentials.

    The second part of the paper examines some aspects of holomorphic quantization on
the manifold SL(2, C) with the Ka�hler metrics described above. We basically look at
two things: the nature and dimension of the quantum Hilbert space, and the quantum
operators corresponding to the classical symmetries of the metric.

    Regarding the latter point, we start by finding the moment map of the SU(2) �
SU(2) action. This map encodes the classical symmetries of the system and, through
the usual prescriptions of geometric quantization, subsequently enables us to give an
explicit formula for the operators corresponding to these symmetries. Regarding the
first point, i.e. the dimension of the Hilbert space, the story is a bit more involved,
and we will now spend a few lines describing the motivation and the results.

                                                      1
    If you apply holomorphic quantization to a compact Ka�hler 2n-manifold, it is a con-

sequence of the Hirzebruch-Riemann-Roch formula that the dimension of the Hilbert
space is finite and grows asymptotically as /(2 )n when  0, where  is the

volume of the manifold. This result is also physically interesting, since it agrees with

some predictions of semi-classical statistical mechanics. Trying to see what happens on

the non-compact SL(2, C) with our invariant metrics, we were thus led to compute the

dimension of the Hilbert space. The results obtained can be summarized as follows.
    The Hilbert space HHQ in our setting is essentially the space of square-integrable

holomorphic functions on SL(2, C), where square-integrable means with respect to

some metric-dependent measure on SL(2, C). Furthermore all these holomorphic func-
tions can be seen as restrictions of holomorphic functions on C4  SL(2, C). Defining
the subspace Hpoly  HHQ of the holomorphic functions which are restrictions of poly-
nomials in C4, we then find that dimHpoly  /(2 )3 as  0 whenever both
members are finite. The exact dimension of Hpoly, which we also compute, depends on
the particular invariant metric one puts on SL(2, C); its asymptotic behaviour how-

ever does not. This leads us to conjecture that, as in the compact Ka�hler case, also for
general Stein manifolds (i.e. complex submanifolds of CN ) this asymptotic behaviour
of dimHpoly is "universal" � see the discussion of section 8.

2 The invariant K�ahler metrics

We start by considering the action of the group G := SU(2) � SU(2) on the complex
manifold M := SL(2, C) defined by

                       : G � M - M , (U1, U2, A)  U1AU2-1 .                                       (1)

This is clearly a smooth action which acts on M through biholomorphisms. A detailed
study of  and its orbits is done in Appendix A. For example one finds there that all
the orbits except one have real dimension 5, the exceptional one being SU(2)  M,
which has dimension 3. For the purposes of this section, however, it is enough to quote
the following result :

Proposition 2.1. Any smooth G-invariant function f~ : M  R can be written as a

composition  f    y,  where  y  :  M    [0, +[  is  defined  by  y(A)  =  cosh-1  [  1  tr(AA)],  and
                                                                                     2
f : R  R is a smooth even function.

    We are now interested in studying Ka�hler metrics and forms over M. To begin with,
the well-known diffeomorphism M  S3 � R3 implies that the de Rham cohomology
of M and S3 are the same. In particular every closed 2-form on M is exact. On the
other hand, regarding C4 as the set of 2 � 2 complex matrices, we have that M is

the hypersurface given as the zero set of the polynomial A  1 - detA. Since the

derivative of this polynomial is injective on the zero set, M is a complex submanifold
of C4. It then follows from standard results in complex analysis of several variables

                                                2
(see th. 5.1.5, 5.2.10 and 5.2.6 of [6]) that M is a Stein manifold with Dolbeault groups
Hp,q(M ) = 0 (except for p = q = 0).

    From all this we get the following lemma:

Lemma      2.2.       Any      closed  (1,1)-form       on    M  can    be     written         =  i  �f~,      where  f~ is  a
                                                                                                  2
smooth function on M. If  is real, then f~ can also be chosen real.

Proof. This is just like the usual proof of the local �-lemma. As argued above,
the closedness of  implies its exactness, hence  = d = 0,1 + �1,0 for some
  H1(M, C). Since 0,1 = �1,0 = 0 (because  is a (1,1)-form) and H1,0(M ) =
H0,1(M ) = 0, we have that 0,1 = �f1 and 1,0 = f2 for some smooth functions fj
           Defining f~ = 2i(f2 - f1) we thus get  =                         i    �f~.                i    �f~
on M.                                                                       2          If  =         2         is  real,  then

1  (f~  +  c.c.)  is  a  real  potential  for  .
2

    Having done this preparatory work, we now head on to the main result of this
section.

Proposition 2.3. Suppose   1,1(M; R) is a closed G-invariant form. Then one
                                     �(f
can     always    write        =  i        y),    where    f    and  y  are    as  in  proposition         2.1     and    f  y
                                  2
is smooth. The function f is unique up to a constant. Furthermore, the hermitian

metric on M associated with  is positive-definite iff f  > 0 on ]0, +[ and f  > 0 on

[0, +[.

Proof.     By the previous lemma               =  i  �f~   for  some    f~     C  (M    ;   R).   Now, for any g             G,
                                                  2
the G-invariance of  and the holomorphy of g imply that

                                       =  g    =     g  i  �f~   =   i  �(f~           g )  .
                                                        2            2

Hence by averaging over g  G if necessary (recall that G is compact), one may
assume that the potential f~ is G-invariant. The first part of the result then follows
from proposition 2.1.

    To establish the second part, recall that the associated hermitian metric is defined
by

                                          H(�, �) = (�, J�) - i (�, �) ,                                                     (2)

where J is the complex structure on M. Since both  and J are G-invariant (the last
one because g is holomorphic), we conclude that also H is G-invariant. Now consider
the complex submanifold   M consisting of the diagonal matrices in M. It follows
from lemma A.1 of Appendix A that  intersects every orbit of . Hence, by the
G-invariance, H is positive-definite on M iff it is positive-definite at every point of .
To obtain the condition for positiveness over  we now use a direct computation.

                                                            3
    Take the neighbourhood U := {A  M : A11 = 0} and the complex chart  of M
defined by

                   : U  C � C2              ,     -1(z1, z2, z3) =         z1      z2                      (3)
                                                                           z3
                                                                                 1+z2 z3
                                                                                    z1

Note that   U and that  is a chart of M adapted to . Defining x(A) = tr(AA)/2
we have that y = cosh-1(x) and

           x  -1(z) =            1  |z1|2 + |z2|2 + |z3|2 + |1 + z2z3|2/|z1|2                 .
                                 2

A direct calculation using the chain rule now shows that, on a point diag(z1, z1-1)  ,
we have

  =  i     �(f    y)  =  i   f (y)    dz1         dz�1  +  2  f (y)    (dz2      dz�2  +  dz3       dz�3)  (4)
     2                   2   |z1|2                            sinh(y)

and hence

           H    =  f (y)    dz1     dz�1  +    2  f (y)       (dz2    dz�2  +  dz3     dz�3)     .         (5)
                   |z1|2                          sinh(y)

Thus at points of  such that y > 0 (i.e. |z1| = 1), we have sinh(y) > 0 and the
positive-definiteness of H is equivalent to f (y), f (y) > 0. On the other hand, since

H and the chart are defined over all of , continuity implies that at a point of  with

y = 0 (i.e. |z1| = 1) we must have

           H      =   f (0)  dz1      dz�1  +     1  f  (0)  (dz2    dz�2  +   dz3     dz�3)  ,
                                                  2

where it was used that

                         lim f (y) = lim f (y) = f (0) .
                         y0+ sinh(y) y0+ y

Thus at this point the positive-definiteness of H is equivalent to f (0) > 0. This
establishes the last part of the proposition.

    To end the proof we finally note that formula (5) implies the uniqueness of f (y),

and hence the uniqueness of f up to a constant.

    Roughly speaking, this proposition guarantees the existence of G-invariant poten-
tials for G-invariant Ka�hler forms. A particular feature of these potentials, which will
be crucial for the explicit calculations later on, is that they are entirely determined by
their values on the diagonal matrices, since every orbit of the G-action contains one of
these. Having this in mind, we now end this section by presenting a technical lemma
which will prove useful on several occasions.

                                                        4
Lemma 2.4. Suppose f~ is a smooth G-invariant function on M, and consider the

submanifold  = {diag(z1, z1-1) :       z1     C} of diagonal matrices                 in M. If h = h(|z1|) is
a smooth function on  such that        �h     = �f~|, then 2f~(z1) =                  h(z1) + h(z1-1) + const.

on the submanifold .

Proof.  The   hypothesis  is that     2h      =      2 f~    on .        Writing z1  C   as      z1 = rei  and
                                    z1z�1          z1  z�1
using the expression for the laplacian in polar coordinates, we have

           0  =  2(f~ - h)    =  1  (f~   -   h)    =     1  (  2   +    1     +  1   2  )(f~ -  h)  .
                  z1z�1          4                        4     r2       r  r     r2  2

But the G-invariance implies that f~ only depends on r; since the same is assumed for

h, we get           2
                    r2
                 (      +  1     )(f~  -  h)  =   0             f~ - h = A log r + B .
                           r  r

Now, G-invariance also implies that f~(z1) = f~(z1-1), thus

2f~(z1) = f~(z1) + f~(z1-1) = h(z1) + h(z1-1) + A(log |z1| + log |z1|-1) + 2B =
         = h(z1) + h(z1-1) + 2B .

3 Curvature and completeness

Throughout this section  will be the Ka�hler form of a G-invariant Ka�hler metric on
M. Thus according to proposition 2.3 we can write

                                           =     i   �(f          y)  ,                                    (6)
                                                 2

where f  y is smooth and f satisfies all the conditions of proposition 2.3.
    The first task now is to calculate the Ricci form  associated to this Ka�hler metric.

More precisely, we will obtain a potential for  expressed in terms of the function f .

Proposition 3.1. The Ricci form of the metric with Ka�hler form  is given by

                            = -i � log                  f (y)         2           .
                                                       sinh(y)
                                                                        f (y)

Proof. The G-invariance of the metric implies the G-invariance of the Ricci form .
Thus, by proposition 2.3,  has a global G-invariant potential ~. Now consider the
chart (U, z1, z2, z3) for M defined in the proof of the same proposition. According to a
standard result, if in this chart

                                    |U    =   i   h    �  dz        dz�     ,
                                              2

                                                     5
then the Ricci form is given by

                                      |U = -i� log(det h �) .

In particular, over the complex submanifold  of diagonal matrices we have

                              i  �~  |       =   |      =   -i� log(det h�) |           .
                              2

But (5) gives us h� over , and so we compute that

                     log(det h�) | = log                      1      f (y)        2           .
                                                            |z1|2   2 sinh y
                                                                                   f (y)

Since this function only depends on |z1|, by lemma 2.4 we get that

                        ~| = -2 log                   f (y)        2          + const. .
                                                      sinh y
                                                                    f (y)

Finally the G-invariance of ~ guarantees that this expression is valid all over M. Thus
                              �~
we  conclude  that      =  i         has     the   stated   form.
                           2

    The next step is the computation of the scalar curvature. Note that the G-invariance
of the metric implies the G-invariance of this function.

Proposition 3.2. The scalar curvature of the Riemannian metric associated with the
Ka�hler form  is

                           s  =     2d                (f    )2  d   log   sinh2 y          .
                                 f (f )2 dy                     dy        f (f )2

Proof. Let us call g(y) := log            sinh2 y     , so that  = i�(g  y). The same calculations
                                          f (f  )2

that led to formula (4) now give

              | = i            g     dz1       dz�1  +   2   g    y (dz2    dz�2  +  dz3      dz�3)  .  (7)
                              |z1|2                         sinh

Writing     =  i  h  �  dz       dz�    and  =           �2irr��.   dz     dz� ,   the  scalar curvature of the
associated     2                        is s = 2h                   Thus   using   (4)  and (7) we can compute

            Riemannian metric

the restriction of s to the submanifold :

                           s|    =   2    g     +  4  g     =      2      d   ((f  )2  g)  .            (8)
                                          f           f         f (f )2   dy

The G-invariance of s then shows that this formula is valid all over M.

                                                            6
In the last part of this section we will make contact with a paper by Patrizio and

Wong [9]: this will give us almost for free some results about the completeness of the

G-invariant metric associated to .

To make contact one just needs to note that the linear transformation on C4 defined

by the matrix

                            1 0 0 -i

                            0 1 -i 0 

                            0 -1 -i                    0  


                                     10 0 i

takes the standard hyperquadric Q4 = {w  C4 : wk2 = 1} to M, and the norm
function w 2 on Q4 to the function x(A) = tr(AA)/2 on M. Therefore all the results
in [9] valid for (Qn, w 2) can be restated here for (M, x). In particular we have that

(1) The function y = cosh-1 x is plurisubharmonic exhaustion on M, and solves the
     homogeneous Monge-Amp`ere equation on M - y-1(0) = M - SU(2) ([9], th.

     1.2).

(2) Suppose f~ = f  y is a strictly plurisubharmonic function on M. Then with
                                            �f~,
respect  to    the  metric  defined  by  i        the  distance  in   M    between  the  level  sets
                                         2
{y = a} and {y = b  a} is ([9], th. 3.3)

               D(a, b) = 1 f(b)          -  (f -1)(t)     dt  =  1      b  f (y) dy .           (9)
                               2 f(a)       (f -1)(t)              2  a

       Furthermore, the distance-minimizing geodesics between these level sets are the
       integral curves of the vector field X/ X , where X is the gradient vector field of
       f~ (one can check directly that X = 0 on M - SU(2)).

As a consistency check, we remark that the strict plurisubharmonicity of f~ = f  y
together with proposition 2.3 garantees that f (y) > 0 on [0, +[= y(M); thus the
integral formula for the distance is well defined. It is now more or less straightforward
to prove the following proposition.

Proposition 3.3. The metric on M with K�ahler form  is complete if and only if

                    D(0, +) = 1        20   +

                                                   f (y) dy = + .

Proof. By Hopf-Rinow, the metric is complete iff the closed bounded sets of (M, )
are compact. So suppose that D(0, +) = + and that B is a closed and bounded
subset of M. Then for b big enough we have

D(0, b) > sup D(0, y(x))  B  y-1([0, b]) = x-1([1, cosh b]) .

                    xB

                                            7
But x is just the usual norm on C4 restricted to M, thus B is also closed and bounded
in C4, and so is compact.

    Conversely, if D(0, +) < +, then M itself is a closed bounded set which is not

compact, and thus the metric is incomplete.

4 Volume and integration

The purpose of this section is to study the integrals over (M, ) of G-invariant functions,
where  is as in (6). More precisely, we want to prove the following result.

Proposition 4.1. Let h~ be a smooth G-invariant function on M, which by proposition
2.1 can be written h~ = h  y, and let Mr be the open submanifold y-1([0, r[)  M. Then
we have that

                                     h~ 3 = 3         r        d  (f (y))3  dy  .                    (10)

                               Mr 3!              30   h(y)  dy

    Notice that 3/3! is the volume form of the metric on M associated with , so with
the particular choice h~  1 we get the volume of Mr. Remark also that with h~  1
or h~  s, where s is the scalar curvature given by proposition 3.2, the integral on the
right-hand side is trivially computable. Thus taking into account the restrictions on f
imposed by propositions 2.1 and 2.3, one gets the following corollary.

Corollary 4.2. For the K�ahler metric on M associated with , the volume of Mr and
the integral of the scalar curvature over Mr are, respectively,

                1  (f   (r))3        and     23   f  (y)2  d   log    sinh2 y              .
                3                                          dy       f (y)f (y)2
                                                                                      y=r

In particular M has finite volume iff f (r) is bounded.

    We now embark on the proof of proposition 4.1. To start with, it will be convenient
to restate here some results used in [10, 11] to study the lump metric.

    Consider the Pauli matrices

                        1 =       0  1    ,  2 =  0   -i       ,   3 =  1    0     ,
                                  1  0            i   0                 0   -1

so  that  {  i  a}  is  a  basis  for   the  Lie  algebra  su(2).   Associated to each  i  a  is  a  left-
             2                                                                          2
invariant 1-form a on SU(2), and {a} is a global trivialization of the cotangent

bundle of SU(2). Then according to [10, 11] and the references therein we have that :

    � There is a diffeomorphism  : SU(2) � R3  M defined by


                           (U, ) = U ( 1 + 2I +  �  ) , with  = || .

                                                      8
� The usual action  of G on M is taken by  to the action ~ on SU(2) � R3 given
  by

                               ~(U1,U2)(U, ) = (U1U U2-1, RU2 ())                       (11)

   where R : SU(2)  SO(3) is the usual double covering; explicitly RU2  SO(3)
                                     1            bU2).
   has  components      (RU2 )ab  =  2  tr(a  U2

� Regarding the a and the da as 1-forms defined over SU(2) � R3, the action ~
  acts on these forms by ~(U1,U2)(, d) = (RU2, RU2d).

� The Euler angles (, , )  ]0, 4[�]0, [�]0, 2[ define an oriented chart of
  SU(2) with dense domain such that, on this domain,

                                  1 = - sin  d + cos  sin  d

                                  2 = cos  d + sin  sin  d                              (12)

                                  3 = cos  d + d .

    The plan now is to use the diffeomorphism  to compute the integrals on SU(2)�R3,
instead of M. Since the {a, a} trivialize the cotangent bundle of SU(2) � R3, the
pull-back by  of the volume form on M can be written

           �     :=        3   =  �^(U, ) 1  2  3  d1  d2  d3 ,
                           3!

for some non-vanishing function �^ on SU(2)�R3. Moreover, � must be invariant under
~, because the volume form on M is invariant under . But notice now that, under ~,

         RU2  1  2  3  det(RU2) 1  2  3 = 1  2  3 ,

because RU2  SO(3). For the same reason, also d1 d2 d3 is invariant, and hence
1  2  3  d1  d2  d3 is invariant too. This fact together with the invariance
of � implies the invariance of the function �^. From the formula (11) for the action ~
it is then clear that �^ only depends on  = ||.

    The computation of the function �^() is now straightforward. First we have

              �^() = �(Id,0,0,)         i  1  ,  i  2,  i  3  ,   ,           ,      =
                                        2        2      2        1           2    3

                        =   1  (3)(Id,0,0,)       (     i  1),   .  .  .  ,       .
                            6                           2                      3

On the other hand, using the chart (3) and (4), at the point q() := (Id, 0, 0, ) =
diag( 1 + 2 + , 1 + 2 - ) of M we also have

1  (3)q()  =  (  i  )3      f (y  )  )2     f (y)          2
6                2      (1  + 2   +        2 sinh y
                                                             dz1  dz�1  dz2  dz�2  dz3  dz�3 .

                                                    9
Finally a tedious calculation that we will not reproduce shows that

                                      i                                    
(dz1 dz�1 dz2 dz�2 dz3 dz�3)q()    (  2  1),  .  .  .  ,    3  = 4i 1 + 2( 1 + 2 +)2 ,

and so we get

                                     1 + 2        f (y  )      2
                                       8         sinh(y  )
               �^(U, ) = �^() =                                 f (y  ) .

Having calculated the volume form on SU(2) � R3, the rest of the proof of proposition

4.1 goes on smoothly.
    Call as usual x(A) = tr(AA)/2 and y = cosh-1(x). A quick calculation shows that

x (U, ) = 1 + 22, and so we have an explicit relation y = y(). From this relation it
is clear that -1(Mr) = SU (2) � Bl, where Bl is the open ball, centered at the origin of
R3, with radius l such that 1 + 2l2 = cosh r. Hence, for any invariant function h~ = h  y

on M we have

    h~  3   =          (h~  ) � =           (h � �^)(y()) 1  2  3  d1  d2  d3
        3!
Mr             -1(Mr )             SU (2)�Bl

            =          1  2  3       l

                 SU (2)              (h � �^)(y()) 42 d .

                                   0

Using the value of �^() and the relation y = y(), a change of variables in the last
integral shows that it coincides with

                             r
                       16
                              h(y) f (y) (f (y))2 dy .

                           0

The first integral can be computed using (12). Namely we have

                                     2  4

                       1  2  3 =                       sin  d d d = 162 .

               SU (2)              0 00

Putting these two results together we finally obtain the formula stated in proposition
4.1.

5 Examples

5.1 The one-lump metric

The so-called moduli space of degree 1 lumps on a sphere, which we will call M, is just
the group of rational maps S2  S2. Identifying S2  CP 1, this group is the same as
the group of projective transformations

                       P GL(2, C) = GL(2, C)/C = SL(2, C)/{�1} .

                                                      10
In the physics literature, M is the space of minimal energy static solutions of the
sigma-model defined on the Lorentzian spacetime S2 � R with S2 as target space. The

kinetic energy functional of this sigma-model induces a certain Riemannian metric on

M, which is also very natural geometrically. It can be defined in the following way.
    Let wt : CP 1  CP 1 be a one parameter family of projective transformations, i.e.

a curve on M, and call w0 its tangent vector at t = 0. For each x  CP 1, t  wt(x)
is a curve in CP 1, and we call v(x)  Tw0(x)CP 1 its tangent vector at t = 0. Then the
Riemannian metric g on M is defined by

                     g(w0 , w0 ) :=              h(v(x), v(x)) volh                            (13)

                                          xCP 1

where h is the Fubini-Study metric on CP 1 and volh is the associated volume form. In

informal terms, one may say that the squared-length of an infinitesimal curve t  wt
in (M, g) is just the average over x  CP 1 of the squared-lengths of the infinitesimal
curves t  wt(x) in (CP 1, h); thus the measure of "displacement" in M is how much
the image points of wt are moved. Using the fact that transformations in P SU(2) 
P GL(2, C) are isometries of (CP 1, h), it is not difficult to check that right and left

multiplication in P GL(2, C) by elements of P SU(2) are in fact isometries of (M, g).

    Now consider the usual chart of the projective space CP 1 \{[0, 1]}  C , [1, z]  z,
and let (u1, u2, u3) be any complex chart of M defined on a neighbourhood of the point

w0. In these charts we have

               w0    =  duj   (0)   
                        dt         uj

               v(z)  =  d   wt(z)    =  d   wu(t)  (z)  =        (wu(z))     duj  (0)  
                        dt              dt                   uj              dt        z

h(     ,          )  =  h1�1  =      2    log(1  +  |z|2)
    z          z                     zz�

               volh  =  i dz  dz�
                        2 (1 + |z|2)2

where the last two equalities are standard properties of the Fubini-Study metric. Call-
ing  := log(1 + |z|2) the local potential of the Fubini-Study metric we get

g(w0 , w0 ) =         2     (w0(z))     (wu(z))     duj    (w�u(z))  du�k    i dz  dz�      =
                     zz�                   uj       dt        u�k    dt      2 (1 + |z|2)2
               zC

    =          duj du�k               2      [(wu(z     ))]  i dz  dz�       =
               dt dt                uj  u�k                  2 (1 + |z|2)2
                              zC

    =          duj du�k 2 i                   [wu(z)]         dz  dz�     .
               dt dt uju�k 2                                 (1 + |z|2)2
                                          zC

                                             11
Since this equation is valid in any chart (uk) of M, we conclude that the function

                     a(w) :=        i        log(1  +   |w(z)|2)   dz  dz�
                                    2                             (1 + |z|2)2
                                         zC

is a global Ka�hler potential for the Ka�hler form on M associated with the Riemannian
                                                               �a.
metric  g.  Calling  this  form  ,  we  thus  have      =   i
                                                            2
It turns out, however, that the integral defining a(w) is difficult to compute for a

general w  P GL(2, C), and so we cannot calculate the potential directly. To circum-

vent this obstacle we proceed in the following way.

Firstly, using the double cover  : SL(2, C)  P GL(2, C), we work on the more
                                                           �(a
palpable group SL(2, C).         Notice that  =         i            ),    because    is  holomorphic.
                                                        2
Moreover, the invariance of g and  by right and left multiplication by elements of

P SU(2), implies that  is invariant by the usual action  of the group G on SL(2, C).
                                                                                                  �f~,
Thus we are on familiar ground.          From proposition 2.3 we get that  =                 i          for
                                                                                             2
some G-invariant function f~. The plan now is to compute f~ using the potential a(w)

and lemma 2.4.

In fact, for a diagonal matrix A = diag(, -1) one can compute that

            a  (A) =       i         log(1 +   z    2    dz  dz�        =
                           2                   2        (1 + |z|2)2
                                 zC                  )

                     =     2       +           r2   )   (1   r       dr    =    log ||4   ,
                                               ||4          + r2)2              ||4 - 1
                                      log(1 +

                                 0

and since                  �(a  )| = -2i()| = �f~| ,

from lemma 2.4 we get that

                                 2f~|    =  2  ||4  +   1   log ||2  .
                                               ||4  -   1

Now using the formulas x(A) = tr(AA)/2 = (||2 + ||-2)/2 and y = cosh-1(x), a little
algebra shows that, over   SL(2, C),

                     f~ =   x                                                                     (14)
                                 x2 - 1  log(x + x2 - 1) =  y coth y .

The G-invariance of f~ finally guarantees that this formula is valid all over SL(2, C). We
have thus obtained an explicit potential for the Ka�hler form . Notice that f~(A) =
f~(-A) for any matrix in SL(2, C), and so f~ descends to a function on P GL(2, C); this
will be a potential for the Ka�hler form  on this space.

    Using the potential function f~ and the results of the previous sections, we will now
derive a series of properties of the metric g. Except for the volume and the Ricci

                                               12
potential computations, these properties were already obtained in [11], using different
methods.

    Substituting expression (14) into propositions 3.1 and 3.2, we obtain a potential for
the Ricci form and the scalar curvature in (M, ). The first is

~(y) = -2 log (y cosh y - sinh y)(sinh 2y - 2y)2/(sinh y)9

and the second has a rather long expression which we will not transcribe. The plot of

this expression, however, coincides with the one in [11] 1, and thus the scalar curvature

is a positive increasing function of y that diverges at infinity. It is worthwhile noting

that, for this metric, the positiveness of the scalar curvature actually comes from the

positive-definiteness of the Ricci tensor, as can be seen by applying proposition 2.3 to

the potential ~. Using the criterion of proposition 3.3 one may also easily verify that

the metric g is incomplete. Finally, from corollary 4.2, and introducing a factor 1/2

to account for the double cover (M, g)  (M, g), we obtain that the volume of the

moduli space is                           6
                                          6
                         vol(M, g)     =        .

5.2 Other metrics

We will briefly mention here other examples of G-invariant metrics on M; these are
interesting for their curvature properties.

    First of all it is clear from proposition 3.1 that any solution of

                 d   (f  (y))3  =  c (sinh y)2  ,  c>0,
                 dy

will give rise to a Ricci-flat metric on M. This metric coincides with the Stenzel metric
on T S3  SL(2, C) [12], as can be seen by using the correspondence M  Q4 described
in section 3 and comparing with section 7 of [12]. It is a complete metric.

    Experimenting with other even functions f (y) one can find metrics with a wide

range of behaviours. For example it follows from propositions 3.3, 3.1 and 2.3 that the
metrics defined by f (y) = y2 and f (y) = cosh y are complete and have, respectively,

positive-definite and negative-definite Ricci tensor. The last one is just the induced
metric by the natural inclusion M  C4. The first one has also the pleasant property
that the parameter y is precisely the geodesic distance from the submanifold SU(2) 

M, and so the volume of Mr grows exactly with the cube of this distance (see (9) and
corollary 4.2).

1Actually our scalar curvature is half of the one in [11], but this must be due to different conventions.

                                   13
Part II

Holomorphic Quantization

In the second part of the paper we want to study the holomorphic quantization of
the Ka�hler manifolds (SL(2, C), ), where  is any G-invariant Ka�hler form. We will
firstly obtain the quantum operators corresponding to the classical symmetries of the
system. After that we will compute the dimension of the Hilbert space of the quantized
system. This last calculation takes a bit of work, but in the end we find some physically
satisfactory results, as described in the Introduction.

6 The classical moment map

Recall  the  action    :  G�M        M  described     in  section     1,  and  suppose    =   i  �(f    y)
                                                                                              2
is any G-invariant Ka�hler form on M (see proposition 2.3). Then, tautologically,  is

a symplectic action on (M, ). Since G is a compact semi-simple Lie group, general

results state that there is a unique moment map � : M  g associated with this

action. We will now give an explicit formula for �.

Proposition 6.1. For any m  M and (a, b)  g = su(2)  su(2) we have

                            �(a, b)  =  i  f (y)   tr(mma        -  mmb)
                                        4  sinh y

where su(2) is identified with the space of 2 � 2 anti-hermitian matrices, and y = y(m)
is the function defined in section 1.

Proof.  Since    =   -d,    where       =  i  (f    y)    is  a  G-invariant   1-form     on  M,    a  well
                                           2
known result (th. 4.2.10 of [1]) states that the moment map satisfies

                                       �(m) [X] = m(X#)                                                (15)

for any m  M and X  g, where X# is the vector field on M generated by the one-
parameter group of biholomorphisms exp(tX) : M  M . Explicitly, for any (a, b) 
g = su(2)  su(2) one can compute

                          (a, b)#m  =  d   (etame-tb  )t=0    =  am - mb ,                             (16)
                                       dt

where we regard TmM  TmGL(2, C)  M(2, C).                                               cosh-1(  1
                                                                                                 2
On      the  other   hand,  for  each  m      M   \  S U (2),    the  formula  y~  :=               trA  A)

gives a local extension of y to a neighbourhood in M(2, C) of m. Since M is a complex

                                                 14
submanifold of M(2, C)  C4, it is then true that (f  y~)|TmM = (f  y)m. Applying
these formulas we thus get

m[(a, b)#]  =  i  f (y)     4   y~  dzk(am - mb)        =
               2          k=1   zk

               i          4        1
               2                2 sinh y
            =     f  (y)                  z�k(m)  dzk(am - mb)        =

                          k=1

               i  f (y)      2                             i  f (y)
               4  sinh y                                   4  sinh y
            =                    m� kl (am - mb)kl      =             tr(mam  -    mmb)   .       (17)

                          k,l=1

Since  and (a, b)# are smooth on M, this formula can be extended by continuity from
M \ SU(2) to M. It coincides with the formula in the statement because of the cyclic
property of the trace.

Remark. Although we will not reproduce the calculations here, a number of properties

of the moment map � can be obtained quite straightforwardly. For example, with
respect to the norm on su(2)  su(2) induced by the norm -tr a2 on su(2), one has

                                 �(m)     2  =    1  f  (y(m))2
                                                  4

�(M) =            (a, b)  su(2)  su(2) : a = b                    [0, 1 f (+)[
                                                                       22

    The moment map obtained above associates to each X  g a function �(�) [X] 
C(M). In the framework of geometric quantization this function is regarded as a
classical observable, and the quantization procedure associates to it a certain hermitian
operator on the quantum Hilbert space. This correspondence is the subject of the next
section.

7 Holomorphic quantization

In this section we want to study the quantization of the classical phase space (M, ). We

will use holomorphic quantization, which is the simplest and most natural quantization

procedure on a Ka�hler manifold. Refinements such as the metaplectic correction will

be left out. For background material consult for example [14]. 2                   �(f

We start with prequantization.            Since   the   Ka�hler  form    =    i           y)  is  ex-
                                                                              2
act on M, the trivial line-bundle B := M � C with the canonical hermitian metric

((m, w1), (m, w2)) = w1w�2 is a prequantum bundle. Now consider the natural unitary

    2A warning about conventions: if (M, ) is a symplectic manifold and H  C(M ), the definition
of the symplectic gradient vector field XH used in [14] differs by a sign from ours.

                                             15
trivialization of this bundle m  (m, 1), and the connection  on B defined by the

1-form                              1
                                    4
                                =      (� - )(f  y)

with respect to this trivialization. The curvature form of  is d = -i -1 and, since

 is pure imaginary, the connection is compatible with the hermitian metric (�, �). Thus

according to the definitions in [14] (B, (�, �), ) is the prequantum data.

The step from prequantization to quantization is made by choosing a polarization

on M. Since M is Ka�hler the natural choice here is the holomorphic polarization, that

is, the polarization spanned by the tangent vectors      .  With this choice, a section
                                                     zk
m  (m) = (m, ~(m)) of B is polarized iff 0,1 = 0, where 0,1 denotes the

anti-holomorphic part of the connection. But

0,1     =  �~ + ~ 0,1  =  �~  +  1  ~ �(f  y)  =  0         ~ =  e-(fy)/4   (18)
                                 4

where  is any holomorphic function on M. Thus the space of polarized sections of B
can be identified with the space of smooth functions on M of the form (18).

    The final step to construct the quantum Hilbert space is to define an inner product
of polarized sections. This is done by the formula

           1, 2 =               (1, 2)  =         1�2e-(fy)/2  ,            (19)

                          M                    M

where  := (2 )-33/3! differs from the metric volume form on (M, ) by the factor
(2 )-3. The quantum Hilbert space of holomorphic quantization, which we denote
HHQ, is then defined as the space of polarized sections of B of finite �, � -norm (see
[14]).

    For a better understanding of this Hilbert space, one should get a clearer picture of
the holomorphic functions  on M. This picture is provided by the next proposition.
Since its proof is rather out of context and may easily be skipped, we defer the proof
to the end of the section.

Proposition 7.1. Regard M = SL(2, C) as the zero set in C4 of the polynomial D(z) =

z1z4 - z2z3 - 1. Then the natural restriction is an isomorphism between the rings of
holomorphic functions O(C4)/J and O(M), where J is the ideal of O(C4) generated

by D(z).

    In other words, this proposition states that every holomorphic function on M is
the restriction of a holomorphic function on C4, and furthermore two holomorphic
functions on C4 restrict to the same function on M iff their difference is divisible by

D(z). We thus get a characterization of holomorphic functions on M in terms of entire
functions on C4, which have a global power series expansion and are generally much

better understood.

                                       16
    For the rest of this section we will look at operators on HHQ. If h  C(M) is
a classical observable, geometric quantization associates to it an operator h^ on HHQ
defined by

                 h^() = i Yh  + h    HHQ ,                             (20)

where Yh is the vector field on M defined by Yh = dh. This observable-operator corre-
spondence does not always work, however, because sometimes the resulting operator h^

takes polarized sections into non-polarized ones. To prevent this, one further demands

that the flow of Yh should preserve the polarization, i.e. the flow should be locally
holomorphic. Thus in principle not all observables h  C(M) can be "quantized" by
this method. It can be shown, however, that if this condition is fullfilled then h^ is a

self-adjoint operator in the Hilbert space (HHQ, �, � ) (see [14] and review [3]).
    We will now apply formula (20) to the observables coming from the classical sym-

metries of (M, ), that is to the functions �X := �(�) [X]  C(M) described in the

previous section. Notice that, by definition of moment map, for each X  g the vector
field Y�X is exactly X# � the vector field generated by the one-parameter group of
biholomorphisms exp(tX) : M  M . In particular the flow of Y�X , which is exp(tX),
preserves the holomorphic polarization, and so formula (20) may be applied to �X.

    Putting together (18), (20) and (15) we get

�^X  = i X# + �X = i (d)(X#) +  (X#) + (X#)  =

=i     (d)(X # )  -  1      d(f    y )(X #)  +  1   (� - )(f  y) (X#)  e-(fy)/4 +
                     4                          4

+   i  (f    y)  (X #)    =  i ()(X#) e-(fy)/4            .            (21)
    2

    For an even more explicit formula, suppose X = (a, b)  su(2)  su(2) and that
  O(M) is the restriction of a certain ~  O(C4). Then using (16) and the fact that
M is a complex submanifold of C4,

                                   4    ~
                                        zk
                 ()m(X#) =                  (m)  z k (am  -  mb)  ,    (22)

                                   k=1

where zk(am-mb) stands for the entry zk of the matrix am-mb under the identification
M(2, C)  C4. Formulas (21) and (22) thus give an explicit description of the operator
�^X on HHQ.

Proof of proposition 7.1. This is a known consequence of textbook results. Let AC4
and AM be the sheaves of germs of holomorphic functions on C4 and M, respectively.
By theorem 7.15 of [6] these are coherent analytic sheaves. Furthermore, calling A~M
the trivial extension to C4 of the sheaf AM over M, it follows from theorems IV-D8
and VI-B5 of [4] that A~M is still coherent analytic and has the same cohomology as

AM .

                                        17
Consider now the short sequence of sheaves over C4:

            0 --- AC4 --D-~ AC4 ---r  A~M --- 0 ,                   (23)

where D~ is the map induced by local multiplication by the polynomial D(z) and r is

defined by

            r|U (f ) =   0 if U  M =                  (U, A~M )
                        f |UM otherwise

for every open set U in C4 and every f  (U, AC4). It is not difficult to check that
(23) is in fact an exact sequence. (Succinctly, D~ is injective because the stalks of
AC4 are integral domains; r is surjective because M is a complex submanifold of C4;
ker r  im D~ by the Nullstellensatz for germs of varieties and the irreducibility of
D(z).)

    We therefore obtain an exact sequence of cohomology groups

      0 --- H0(C4, AC4) --- H0(C4, AC4) --- H0(M, AM ) --- 0 ,

where we have used that Hp(C4, A~M )  Hp(M, AM ) and that, by Cartan's theorem B
[4, p. 243], H1(C4, AC4) = 0. Since the zeroth cohomology groups are just the global

sections of the respective sheaf and, under this identification, the first and second maps

are, respectively, multiplication by D(z) and the natural restriction, we finally obtain

that                                  (C4, AC4)
                                  D(z) � (C4, AC4)
            O(M )  =  (M, AM )                       =  O(C4)/J  .

8 Dimension of the Hilbert space

In this last section of the paper we will be concerned with the dimension of the quantum
Hilbert space associated with the Ka�hler manifold (M, ). More specifically, using the
identification of the previous section

              HHQ    O(M ) = O(C4)/J : ||2e-(fy)/2  < + ,

                                                                                            M

let Hpoly be the subspace of HHQ consisting of the holomorphic functions that can be
represented by polynomials in C4. Then we will be able to compute the dimension of
Hpoly in terms of the Ka�hler potential f . Furthermore, when (M, ) has finite volume
 and Hpoly has finite dimension, we will show that dimCHpoly  /(2 )3 as  0+.
These results are finally discussed in Questions 1, 2 and 3.

    The main step towards proving the stated results is the following proposition, which
will be proved at the end of this section.

                                                      18
Proposition 8.1. Let  be a holomorphic function on M that can be represented by a
polynomial in C4, of degree l, whose homogeneous term of highest degree is not divisible

by z1z4 - z2z3. Then  is in Hpoly if and only if

                             +                      d   [f  (y  )]3  dy     < + .                      (24)
                                                    dy
                                (cosh y)l e-f(y)/2

                           0

    Using this proposition the dimension of Hpoly can be computed quite straightfor-
wardly. In fact, assuming that {l  N : (24) is satisfied} is not empty (which will
be shown to be true when (M, ) has finite volume), and calling m  N  {+} the
maximum of this set, we have:

Corollary       8.2.  The  complex  dimension       of  Hpoly   is   1  (m  +  1)(m  +  2)(2m  +  3).
                                                                     6

Proof. Let Pl  O(C4) be the subspace of homogeneous polynomials of degree l, and
Pm the space 0lm Pl. Calling  : O(C4)  O(M ) the natural homomorphism,
let also | be the restriction of  to Pm.

    By proposition 8.1 we have that Hpoly = (Pm), thus

        dim Hpoly = dim(Pm) - dim(ker |) = dim(Pm) - dim(Pm  ker ) .

But proposition 7.1 states that ker  is the ideal in O(C4) generated by z1z4 - z2z3 - 1,
and so it is clear that the linear map

           Pm-2  Pm  ker  , Q(z)  (z1z4 - z2z3 - 1) � Q(z)

is an isomorphism. Hence dim(Pm  ker ) = dim(Pm-2), and dim Hpoly = dim(Pm 

Pm-1). But it's a well known combinatorial fact that dimPm � the number of ways
                                                                            3+m
of choosing 4 non-negative integers whose sum is m � is                       3  ,   and  the  result  follows

directly.

    In practice, by looking at the asymptotics of the potential f , it is usually not
difficult to compute the integer m.

Example 8.3. The lump metric on M studied in section 5 has a Ka�hler form  =
     �(f
i          y),  with  f (y)  =  y coth y,  and  finite  volume           =  6/3.    From  the  asymptotics
2

                f (y) = y [1 + 2e-2y + 2e-4y + O(e-6y)]                        as y  +

one gets that                                                                  as y  + ,
           (cosh y)l e-f(y)/2 d [f (y)]3 = O(y e(-/2 +l-2)y)
                                 dy

and so m = max{l  N : l < 2 + /2 }.

                                                    19
    An interesting feature of this example is that, if we let  0+, then m  /2 ,
and by corollary 8.1 we obtain

                     dimC Hpoly           m3           3       =        )3    .
                                           3          24 3        (2

This is exactly the answer expected in semi-classical quantum mechanics for the quan-
tization of a phase space of volume  and real dimension 6 [8]. Before discussing the
significance of this coincidence, we will first show that this property is more general,
and is in fact valid for all the G-invariant Ka�hler metrics on M of finite volume.

Proposition  8.4.  Suppose    =  i    �(f     y)     is  the   Ka�hler  form     of    a  metric  on  M      of
                                 2
finite volume . Then the constant m = m(f, ) satisfies

                     (3)1/3   +  k  -  1          m         (3)1/3      +  k  ,
                       2                                      2

where

k = k(f ) := sup          R+0 :       +      ey   d   [f  (y)]3   dy    is finite       [0, +] .
                                    0             dy

Proof. By corollary 4.2 we have that

                     =  3     +  d    [f  (y)]3   dy     =  3     lim [f (y)]3     ,                      (25)
                        3   0    dy                         3
                                                                 y+

thus the finite volume condition implies that k  0 and that D := limy+ f (y) is a
positive finite number. By L'Ho^pital's rule we also get that limy+ y-1f (y) = D. It

then follows that, for  real,

 lim (e-y cosh y)l exp          -   1        f  (y)  -   D       y=           + if  > 0                   (26)
                                    2           y                               0 if  < 0 .
y+

Now, by definition, m is the biggest of the integers l  N such that

                          +                              d   [f  (y)]3  dy                                (27)
                                                         dy
                             (cosh y)l e-f(y)/2

                        0

converges. This integral, however, is the same as

  +    (e-y cosh y)l exp      -  1        f  (y)  -  D      y     e(-+l-D/2        )y  d   [f  (y)]3  dy  .
0                                2           y                                         dy

If l - D/2 > k, then choosing  in the interval ]0 , l - D/2 - k[ and using (26) and
the definition of k, it is clear that (27) diverges; thus m  k + D/2 . If l - D/2 < k,
then choosing  in ]l - D/2 - k , 0[, the same arguments show that (27) converges;
thus m  k + D/2 - 1. Since from (25) we have D = (3)1/3/, the proposition is
proved.

                                                20
Corollary 8.5. Given any G-invariant Ka�hler metric on M of finite volume , let
          �(f
  =  i          y)  be  its  K�ahler  form.  Then  the  associated  quantum  space  Hpoly  is  finite-
     2
dimensional iff k(f ) is finite. In this case dimCHpoly  /(2 )3 as  0+.

Proof. It follows directly from corollary 8.2 and proposition 8.4.

Remark. The lump metric is an example with finite volume and finite-dimensional
Hpoly. There are however metrics of finite volume with infinite dimensional Hpoly. For
example, define f (t) as any extension of t  (1 - e-t2) , t  [1, +[, to a smooth odd
function on R with everywhere positive first derivative. Then calling f any primitive
of f , the metric on M with Ka�hler potential f  y has the desired property.

8.1 Discussion

The asymptotic value /(2 )3 for the complex dimension of the quantum Hilbert
space is both physically and geometrically quite significant. Physically because semi-
classical statistical mechanics predicts that if you quantize a classical system with n
degrees of freedom, thus with 2n-dimensional phase space, you should get one indepen-
dent quantum state of the system for each cell of volume (2 )n on the phase space [8].
Hence if the phase space has finite volume , one gets /(2 )n independent quantum
states.

    The geometrical significance, on the other hand, arises from the fact that this
asymptotic value is expected when the base manifold is compact, but not "a priori"
for the non-compact M = SL(2, C). The compact result is a direct consequence of the
Hirzebruch-Riemann-Roch formula and the Kodaira vanishing theorem [5], and can be
stated as follows.

    On a compact Ka�hler 2n-manifold of volume , the Hilbert space of holomorphic
quantization has finite complex dimension, and this grows asymptotically as /(2 )n
when  0+.

  We are thus led to the following questions.

Question 1. Is there a version of the above result for the non-compact case ?

  Our results suggest that there is, since SL(2, C) is not compact and some of the G-

invariant metrics for which corollary 8.5 holds � for example the lump metric � cannot

be compactified.

  Another example is the manifold C with any U(1)-invariant Ka�hler metric g. In

this case the Ka�hler form also has a U(1)-invariant global potential � which we call 

� and Hpoly is the space of square-integrable complex polynomials on C with respect
                                            �.
to the volume form exp (-/2           )  i      A simplified version of the method used in this
                                         2
paper then shows that, if the volume  of (C, g) and the dimension of Hpoly are both

finite, we also have

                             dimCHpoly  /(2 ) as  0+ .

                                                   21
In an optimistic spirit, we are thus led to formulate the following question.

Question 2. Let S be a closed complex submanifold of CN (i.e. a Stein manifold) of
complex dimension n  N, and let  be any Ka�hler form on S. Since S is Stein,  has
a global potential   C(S; R), and we can define

                  Hpoly :=   C[z1, . . . , zN ] : ||2e-/2 n < + .

                                                                                         S

Then, if the volume  of (M, ) and the dimension of Hpoly are both finite, is it always
true that dimCHpoly  /(2 )n as  0+ ?

    Having in mind our examples, it is also possible that the result only holds for
algebraic submanifolds of CN . Another point which would be worth to clarify is the
relation between the spaces Hpoly and HHQ.

Question 3. In our example of SL(2, C) with a G-invariant Ka�hler metric of finite
volume, is it true that whenever Hpoly is finite-dimensional we have Hpoly = HHQ ?
And for more general Stein manifolds of finite volume ?

    Recall that the finite-dimensionality of Hpoly comes from the fact that the only
polynomials on C4 which are integrable on SL(2, C), are the ones of degree smaller than
a certain constant. The above question asks if, in this case, the entire non-polynomial
functions on C4 are automatically non-integrable on SL(2, C). It is plausible that the
answer is yes, since entire non-polynomial functions have very high growth rates in
certain directions. However, if the answer is no, then perhaps in this case it is wiser to
take Hpoly as the quantum Hilbert space, instead of the traditional HHQ. The finite-
dimensionality of Hpoly ensures completeness and corollary 8.5 supports this choice.

8.2 Proof of proposition 8.1

The "only if " statement. We have to show that

        ||2e-(fy)/2  < +                        (28)

      M

implies condition (24). Notice first that if (28) is satisfied, the "change of variables"
theorem guarantees that for any of the G-action biholomorphisms g : M  M,

      ||2e-(fy)/2  =      |  g|2e-(fy)/2  ,

   M                  M

where we have used the G-invariance of the volume form . So using the invariant
(Haar) integral on G to average over the group, we get that

   ||2e-(fy)/2  =         |  g|2 e-(fy)/2  .    (29)

M                  M  gG

                      22
Now regard (z1, . . . , z4) as a polynomial on C4, and write  = 0 + � � � + l, where k
is homogeneous of degree k. As in Appendix A, consider also the natural extension of
the G-action  to the manifold C4  M. We then have

                                                         l

                               |  g(z)|2 =                       (�kj)  g(z) ,

                     gG                               k,j=0 gG

where each term of the sum is a smooth G-invariant function on C4. In particular, using

the notation and proposition A.4 of Appendix A, each of these terms may be written
as Fkj(x(z), w(z)), where Fkj : B  C is continuous, x(z) = (|z1|2 + � � � + |z4|2)/2 and
w(z) = z1z4 - z2z3. On the other hand, going back to the definition of , we see that
each component of g(z) is just a linear combination of the components of z, and so
in fact we must have

Fkj(x(z), w(z)) =                  (�kj)  g(z) =                 ci1���ikn1���nj z�i1 � � � z�ik zn1 � � � znj .

                               gG

From this formula it is clear that, for any   R0+,

          Fkj(2x(z), 2w(z)) = Fkj(x(z), w(z)) = k+jFkj(x(z), w(z)) ,

and in particular

                          x-l Fkj (x, 1) = x-l+(k+j)/2 Fkj(1, x-1) .

Since k, j  l, using the continuity of Fkj we then obtain that

           lim  x-l  Fkj  (x,  1)  =   lim    x-l+(k+j)/2   Fkj (1,      x-1)  =  lk lj Fll(1, 0) .

          x+                          x+

Defining

                                                                      l

          h(x(z), w(z)) :=                 |  g(z)|2 =                     Fkj(x(z), w(z)) ,

                                      gG                         k,j=0

we therefore have that

                                              l

                 lim x-l h(x, 1) =                 lim      x-l  Fkj  (x,  1)  =  Fll(1, 0)     .                 (30)

                x+                         k,j=0  x+

    Now, it will be shown in lemma 8.6 that 0 < Fll(1, 0) < +, and so (30) implies
that there is a constant c > 0 such that h(x, 1) > c xl for x big enough. On the other

hand, using (29), proposition 4.1 of section 4, and that w(z) = 1 and x(z) = cosh(y(z))

for z  M, we have

          ||2 e-(fy)/2  =                 h(x(z), w(z)) e-(fy)/2  =

M                                     zM

                               =      3            +                              d   [f    (y)]3  dy  
                                   3(2                                            dy
                                          )3          h(cosh y, 1) e-f(y)/2

                                                 0

                                   const.  +       c  3       +                       d     [f  (y)]3  dy  ,
                                                 24                                   dy
                                                                 (cosh y)l e-f(y)/2

                                                            0

                                                      23
where const. is some finite real number. From this inequality it is clear that (28)
implies condition (24) of proposition 8.1.
Lemma 8.6. The constant Fll(1, 0) is in ]0, +[.

Proof. As we have seen above Fll : B  C is continuous and, by definition,

   Fll(x(z), w(z)) =                             ||2  g(z) .                                    (31)

                                             gG

Since (1, 0)  B (see Appendix A), Fll(1, 0) is a well-defined finite number, and from
(31) it is clearly non-negative. Now call V := {z  C4 : z1z4 - z2z3 = 0}, and let q be
any point in V \ {0}. Since q := x(q)-1/2q  V and x(q) = 1, we have

                             |l  g(q)|2 = Fll(x(q), w(q)) = Fll(1, 0) .

                                    gG

Hence, if Fll(1, 0) = 0, we get that l  g(q) = 0 for any g  G, and in particular
l(q) = 0. But l is homogeneous, and so also l(q) = 0. From the arbitrariness of q
it follows that l vanishes on V � the zero set of the irreducible polynomial z1z4 - z2z3.
Finally from Hilbert's Nullstellensatz we conclude that l is divisible by z1z4 - z2z3.
This contradicts the hypothesis of proposition 8.1, and therefore Fll(1, 0) > 0.

The "if " statement. As before, write  = 0 + � � � + l. Then ||2  |0|2 + � � � + |l|2 .
Since x(z) = (|z1|2 + � � � + |z4|2)/2, we have that |zk|  2x(z) for all z. But j is
homogeneous of degree j  l, thus

   |j(z)|2  cj (2x(z))j  cj (2x(z))l , z  C4 ,

for some positive constants cj. Calling c =  l    cj ,  using  proposition  4.1     of   section  4
                                             j=0
and that x(z) = cosh y(z) for z  M, we finally get

                  l

   ||2e-(fy)/2           |j|2e-(fy)/2                          c (2x(z))le-(fy)/2  =

M                 j=0 M                                 zM

                     =    c 2l 3               +                      d   [f    (y  )]3  dy  .
                         3(2 )3                                       dy
                                                  (cosh y)l e-f(y)/2

                                             0

From this inequality it is clear that condition (24) of proposition 8.1 implies (28), and
so   Hpoly.

Acknowledgements. I would like to thank Prof. N. S. Manton for many helpful
discussions and Prof. B. Totaro for some comments regarding proposition 7.1. I am
supported by `Fundac�~ao para a Ci^encia e Tecnologia', Portugal, through the research
grant SFRH/BD/4828/2001.

                                                      24
Appendix A

    In this appendix we study the action  of the group G := SU(n) � SU(n) on the
manifold M(n, C)  Cn2 of complex n � n matrices defined by

 : G � M (n, C)  M (n, C) , (U1, U2, A)  U1AU2-1 .             (32)

The results obtained are used in sections 2 and 8.

    According to [7, p. 396] every matrix M  GL(n, C) can be decomposed in the
form M = KAK, where K, K  U(n) and A is real diagonal with positive entries in
the diagonal. Notice that multiplying K and K by permutation matrices, if necessary,

we may assume that the diagonal entries of A do not decrease with the row index.

Lemma A.1. Every matrix M  M(n, C) may be decomposed in the form M =
U1AU2ei, where U1, U2  SU (n),   R, and A is a real diagonal matrix with non-
negative diagonal entries which do not decrease with the row index.

Proof. Given M  M(n, C) there is a sequence {Mj} in GL(n, C) with Mj  M.
Using the decomposition described above, for each Mj we have

                    Mj = Kj Aj Kj .

Since the sequences {Kj} and {Kj } are in the compact group U(n), there are convergent
subsequences Kjl  K and Kjl  K when l  +, where K, K  U (n). Defining

A  :=       KM (K)  =  lli+m(Kjl )Mjl (Kjl )  =   lim  Ajl  ,

                                                 l+

the fact that Ajl is diagonal with positive ordered diagonal entries, implies that A is
diagonal with non-negative ordered diagonal entries; furthermore KAK = M. Since
K, K  U(n), they can always be written as matrices in SU(n) times a phase, and

this ends the proof.

    We will now find functions on M(n, C) which separate the orbits of , and hence
can be used as coordinates in the space of orbits. For this define the polynomials Pj
on M(n, C) by

                                                                                        n

                                    det(B + I) = j Pj(B) .

                                                                                      j=0

We then have:

Proposition A.2. Two matrices M, N  M(n, C) lie in the same orbit of  if and
only if Pj(M M ) = Pj(N N ) for 1  j  n and det N = det M .

                       25
Proof. If N and M are in the same orbit, i.e. N = U1MU2 for some U1, U2  SU (n),
then N N = U2MMU2, and the stated conditions are clearly satisfied.

    Conversely, suppose that Pj(N N ) = Pj(MM) for 1  j  n and det M = det N .
Then N N and MM have the same characteristic polynomial, and hence the same
eigenvalues. On the other hand, from lemma A.1 we have the decompositions

          M = U  diag(1, . . . , n) U ei and N = U~  diag(~1, . . . , ~n) U~ ei , (33)

so
           M M = U  diag(21, . . . , 2n) U and N N = U~  diag(~12, . . . , ~2n) U~

hguavaeraenitgeeensvtahluaetsth{e12,j.,.~.j,  n2 }  and {~21, . . . , ~n2 }, respectively. Since  lemma   A.1 also
                                              are   non-negative and ordered, we conclude         that j  = ~j for

1  j  n. Hence                                N = U~(U )-1M U -1U~ ei(-) .

If det M = det N = 0, then taking the determinant of the above equation we get that
det(ei(-)I) = 1, and so ei(-)I is in SU (n). This shows that N = U1M U2 for some
U1, U2  SU (n).

    If det M = det N = 0, then (33) implies that the product of the j is zero, therefore
1 = ~1 = 0, because the j are non-negative and ordered. Defining

        := diag(ei(-)(n-1), ei(-), . . . , ei(-))  SU (n)

we then get
  N = U~ diag(1, . . . , n) U~ ei = U~ diag(1, . . . , n) U~ ei = U~(U )-1M U -1U~ ,

which shows that, also in this case, N = U1MU2 for some U1, U2  SU (n).
    These results are now going to be used in the study of G-invariant functions on

M(2, C) and SL(2, C). Define the smooth map

        : M(2, C)  C4  R � C , (z) = (x(z), w(z)) ,

where              1
                   2
       x(z)     =     (|z1|2                  +     �  �  �  +  |z4|2)  and  w(z) = z1z4 - z2z3 .

It follows from the proposition above that two points in M(2, C) lie in the same -orbit
iff they have the same image by . In particular any G-invariant function h~ on M(2, C)
may be written h~ = h  , where h is some function defined on the image of . We will
now show that the continuity of h~ implies the continuity of h � a result used in section

8.

Lemma A.3. The image of  is B := {(a, u)  R � C : a  |u|}.

                                                                26
Proof. From the identity

x(z)2 - |w(z)|2  =        1  (|z1|2  +  |z2|2  -  |z3|2  -  |z4|2)2  +  |z1z�3  +  z2z�4|2    0
                          4

it follows that x(z)  |w(z)|, thus the image of  is contained in B.
    Conversely, defining g : B  C4 by

g(a, u) = u(a + a2 - |u|2)-1/2, 0, 0, (a + a2 - |u|2)1/2 ,                                       (34)

one can easily check that   g(a, u) = (a, u), and so B contains the image of .

Proposition A.4. Let X be a topological space, V a subset of the image of , and
h : V  X a map such that h   is continuous on -1(V). Then h is continuous.

Proof. Consider the map g : B  C4 defined in (34). This map is clearly continuous
on B \ {(0, 0)} and, for (a, u) approaching the origin from this set,

   lim                               u                      lim      a    =     0.
                                     a2 - |u|2                         a
(a,u)(0,0)                   a+                          (a,u)(0,0)

Thus g is also continuous at (0, 0) and vanishes at this point. Finally, since

h(a, u) = (h  )  g(a, u) for all (a, u)  V ,

we conclude that the continuity of h   implies the continuity of h.

    Now suppose we restrict the action  of G to the submanifold SL(2, C)  M(2, C).

Since the function w(z) is identically 1 on SL(2, C), we have that two points in this

submanifold lie in the same -orbit iff they have the same image by x(z). From
lemma A.3 it follows that x(SL(2, C)) = [1, +[, and since cosh-1 is injective on this
interval, we have that y := cosh-1  x also separates orbits in SL(2, C). We can now

prove proposition 2.1 of section 2.

Proof of proposition 2.1. From the paragraph above, it is clear that any smooth G-
invariant function f~ on SL(2, C) may be written as f~ = f  y, for some unique f :
[0, +[ R. Now consider the smooth map h : R  SL(2, C) defined by

                          h(t) =     cosh(t/2)     sinh(t/2)         .
                                     sinh(t/2)     cosh(t/2)

One can easily check that y  h(t) = t for t  0, hence
                            f (t) = (f  y)  h(t) = f~  h(t) , t  0 ,

which implies that f is smooth. Note also that h is defined on R, and from the G-
invariance of f~ we get f~ h(-t) = f~ h(t); thus f can be extended to an even function
on R.

                                               27
References

 [1] R. Abraham and J. Marsden: `Foundations of Mechanics' (3rd ed., Ben-
      jamin/Cummings, Reading Mass., 1978).

 [2] A.M. Din and W.J. Zakrzewski : `Skyrmion dynamics in 2+1 dimensions'; Nucl.
      Phys. B259, 667 (1985).

 [3] A. Echeverria-Enriquez, M.C. Munoz-Lecanda, N. Roman-Roy and C. Victoria-
      Monge: `Mathematical Foundations of Geometric Quantization'; Extracta Math.
      13 135-238 (1998), math-ph/9904008.

 [4] R. Gunning and H. Rossi: `Analytic Functions of Several Complex Variables'
      (Prentice-Hall, Englewood Cliffs N.J., 1965).

 [5] F. Hirzebruch : `Topological Methods in Algebraic Geometry' (3rd ed., Berlin,
      Springer-Verlag, 1978).

 [6] L. H�ormander : `An Introduction to Complex Analysis in Several Complex
      Variables' (3rd rev. ed., Amsterdam, North-Holland, 1990).

 [7] A. Knapp : `Lie groups beyond an introduction' (Birkha�user, Boston, 1996).
 [8] R. Kubo : `Statistical Mechanics' (North-Holland, Amsterdam, 1965).
 [9] G. Patrizio and P.M. Wong : `Stein manifolds with compact symmetric center';

      Math. Ann. 289 (3), 355-382 (1991).
[10] J.M. Speight : `Low energy dynamics of a CP 1 lump on the sphere'; J. Math.

      Phys. 36, 796-813 (1995).
[11] J.M. Speight : `The L2 geometry of spaces of harmonic maps S2  S2 and

      RP 2  RP 2'; to appear in J. Geom. Phys., math.DG/0102038.
[12] M. Stenzel : `Ricci-flat metrics on the complexification of a compact rank one

      symmetric space'; Manuscripta Math. 80 no. 2, 151-163 (1993).
[13] R.S. Ward: `Slowly moving lumps in the CP 1 model in (2+1) dimensions'; Phys.

      Lett. 158B, 424-8 (1985).
[14] N. Woodhouse : `Geometric Quantization' (2nd ed., Clarendon Press, Oxford,

      1997).

                                                      28
