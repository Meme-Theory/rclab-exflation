# 2003 Dynamics of vortices on S2 near Bradlow limit

**Source:** `01_2003_Dynamics_of_vortices_on_S2_near_Bradlow_limit.pdf`

---

arXiv:hep-th/0208001v1 1 Aug 2002                                                                                                         DAMTP-2002-94

                                                   The dynamics of vortices on S2
                                                         near the Bradlow limit

                                                                     J. M. Baptista and N. S. Manton

                                                               Department of Applied Mathematics and Theoretical Physics
                                                                                       University of Cambridge

                                                                      Wilberforce Road, Cambridge CB3 0WA, England

                                                                                      July 2002

                                                                                     Abstract

                                        The explicit solutions of the Bogomolny equations for N vortices on a sphere of radius
                                   R2 > N are not known. In particular, this has prevented the use of the geodesic approximation
                                   to describe the low energy vortex dynamics. In this paper we introduce an approximate general
                                   solution of the equations, valid for R2 N , which has many properties of the true solutions,
                                   including the same moduli space CPN . Within the framework of the geodesic approximation,
                                   the metric on the moduli space is then computed to be proportional to the Fubini-Study metric,
                                   which leads to a complete description of the particle dynamics.

                                       e-mail address: [email redacted]
                                       e-mail address: [email redacted]
1 Introduction

The abelian Higgs model in the plane is one of the most studied examples of a field theory
with topological solitons. The solitons are vortices. At critical coupling there are Bogomolny
equations, and it is known that there is a 2N -dimensional manifold of gauge-inequivalent N -
vortex solutions [6]. This is known as the N -vortex moduli space, and denoted MN . As a
manifold, MN = CN . There is a natural metric on MN , arising from the kinetic terms in
the Lagrangian of the model, and it has been proved by Stuart [13] that, at least for finite
time intervals, geodesic trajectories on the moduli space give a good approximation to the true
dynamics of slowly moving vortices.

     It is convenient to introduce the standard complex coordinate z on the plane. The locations
of the vortices are the N unordered points where the Higgs field vanishes. These points may be
regarded as the roots of a monic polynomial in z (monic means that the coefficient of zN is 1),
and the natural coordinates on moduli space are the N complex coefficients of such a polynomial.
If a particular geodesic motion is known, then the time-dependence of the polynomial is known,
and hence the time-dependence of the roots can be calculated.

     Now, a general formula for the metric on moduli space has been given by Samols [12], but
it is not explicit, so only very special geodesics, with a high degree of symmetry, are understood
in detail for N > 2 [1, 9]. One vortex just moves at constant speed along a straight line.
The geodesic motion for two vortices has been calculated by Samols numerically. The most
interesting phenomenon is that, in a head-on collision, two vortices scatter at right angles.
Recently, Manton and Speight [11] have found an explicit metric for N well separated vortices,
from which the geodesic motion could be computed.

     In this paper we are interested in the opposite limit. It is possible to consider the abelian
Higgs model with fields defined on any compact surface. We shall only consider the case of
a 2-sphere with its standard round metric, parametrized by its radius R. There are again
Bogomolny equations and a 2N -dimensional moduli space of N -vortex solutions. As a manifold
this is CPN . However, there is an important geometrical constraint, discovered by Bradlow [2].
This is that the area of the sphere must be greater than 4N for non-trivial solutions of the
Bogomolny equations to exist. Equivalently, R2 > N . The metric on moduli space is known to
collapse to zero size as the Bradlow limit R2  N is approached. We shall be interested here
in the case where R2 is slightly greater than N . One should think of this as a situation where
the vortices are densely squeezed together. We shall present an approximate general solution
of the Bogomolny equations, and using this, calculate the metric on moduli space directly from
its definition. Again the solutions involve a polynomial, and the natural coordinates are the
complex coefficients of the polynomial. We shall find that the metric is that of Fubini-Study,
with an overall scale factor that depends on R2 - N .

     The geodesics on Fubini-Study are quite simple, and hence, in principle, the motion of
vortices can be calculated straightforwardly. However, this does involve finding the roots of
polynomials with time-varying coefficients, which is not algebraically trivial for three or more
vortices. We shall present examples, mainly of two vortex motion. We should also remark that
Stuart's proof of the validity of the geodesic approximation for vortex motion does not extend
automatically to this regime of being close to the Bradlow limit, so our results on vortex motion
remain rather formal at this stage. The particle dynamics we obtain at the end is, nevertheless,
quite "physical".

                                                              1
     The paper is structured as follows. In Section 2 we introduce the Bogomolny equations
on S2, which is identified with CP1. As in [2, 4], the equations are defined on complex line
bundles over this surface. In Sections 3 and 4 we explain our approximation for R2 close to
N , and proceed to compute the metric on the moduli space of the approximate solutions. The
geodesics of this Fubini-Study metric are then used in Section 5 to give an explicit description
of the N -vortex dynamics. Some examples of motions are presented in Section 6, and finally in
Section 7 a general result concerning the number of vortex collisions is proved.

2 The Bogomolny equations

According to Bradlow's generalization of the classical vortices over R2 [2], when the base manifold
is the sphere S2 = CP1, the setup for the problem is a complex line bundle  : E  S2 of degree

N equipped with a hermitian metric h. The Higgs field  is now a section of this bundle, and

the gauge potentials are the local 1-forms of an h-compatible connection D on the bundle. We
will take the metric on S2 to be gR := R2 � (standard metric on S2) , so that the volume of
(S2, gR) is 4R2.

     Letting A := {h-compatible connections on E} and (E) := {global C sections of E} ,

the Bogomolny equations for (D, )  A � (E) are ([2, 4]) :

         D0,1 = 0                             (1)

F  +  1  (||h2             -  1)(volR)  =  0  (2)
      2

where D0,1 is the anti-holomorphic part of D, volR  2(S2, R) is the volume form of the metric
gR, and -iF is the globally defined curvature form of D, so that F  2(S2, R).

     We remark that the problem does not depend essentially on (E, h), because all complex
line bundles over S2 of a given degree N are isomorphic. In fact, for another choice (E, h)
there will always be an isomorphism f : E  E such that f (h) = h . It is then not difficult
to check that (D, ) is a solution of (1) and (2) on (E, h) if and only if (f D , f -1  ) is
a solution on (E, h), where f D is the pull-back connection on E. Notice in particular that
  (E) and f -1    (E) have the same zeros on S2, and hence correspond to the same

vortex configuration.

     We will now define the particular pair (E, h) which is to be used in the remainder of this
paper. Let U1 = CP1 \ {[0, 1]}, U2 = CP1 \ {[1, 0]}, where we use the standard homogeneous
coordinates [z0, z1] for points on CP1, and let i : Ui  C be the standard complex charts of
CP1 with transition functions 1  2-1 = 2  -1 1 : z  1/z . Define gij : Ui  Uj  U (1) by

                        g21  2-1(z) = (z/|z|)N , g12 = 1/g21 , g11 = g22 = 1 .

Since the gij satisfy the usual cocycle conditions, it is possible to construct a complex line bundle
 : E  CP1 with trivializations i : -1(Ui)  Ui � C such that i  j-1(p, y) = (p , gij(p) y).
The hermitian metric h on E is defined by requiring the unitarity of the trivializations i , that
is |i-1(p, y)|h2 = |y|2 ; it is well defined because gij has values in U (1).

                           2
We should now check that deg E = N . Define the real valued 1-forms Ai  1(Ui, R) by

           Ai = i A            with     A  :=     -iN      |2)  (z�  dz  -    z  dz�)   1(C, R) .             (3)
                                               2(1 + |z

On U1  U2 one has              1                        |z|  N           z       N
         (-2 1)(A1 - A2) =     z                        z                |z|
                                   A -A = i                    d                    = i (2-1)(g12 dg21) ,

or equivalently

                                  (-iA1) - (-iA2) = g12 dg21 ,

which shows that the local forms -iA1 and -iA2 define a connection DN on E. The curvature
-iFN of DN is a global 2-form on CP1 determined by FN = dAj on Uj. In particular, one can
compute that

                 (1-1)FN    =  dA    =  (1     iN       dz      dz�  =   (-1 1   )(    1  volN )  ,
                                              + |z|2)2                                 2

and hence                       i                            1
                               2                             2
                 deg E    :=             (-iFN ) =                    (1-1)FN          = N.

                                     CP1                             C

     Integrating equation (2) over CP1, and using that CP1 F = 2 deg E = 2N , it is clear
that for R2 < N the Bogomolny equations have no solution, and that for R2 = N any solution

(D, ) must satisfy  = 0 and F        =     1  volN      =    FN .    Since we have already constructed a
                                           2
connection DN on E with curvature -iFN , we have an explicit solution of the Bogomolny

equations for the case R2 = N (which is called the Bradlow limit), and it can be shown that it

is unique up to gauge transformations.

     For R2 > N Bradlow has shown [2], in a more general context, that for any solution (D, ) of
(1) and (2), the section  has exactly N zeros (which are called vortices), counting multiplicities.
Moreover, the moduli space MN of these solutions up to gauge tranformations, is parametrized
by the positions in CP1 of these N vortices. Since the vortices are indistinguishable, this moduli

� � space is identified with (CP1)N / N , where N is the group of permutations of N elements.
   � Now consider the map  : (CP1)N / N  CPN defined in homogeneous coordinates by

[u1, v1] , . . . , [uN , vN ] - . . . ,             v(1) � � � v(k)u(k+1) � � � u(N) , . . .         0kN   .

                                              �  N

With some care, one can verify that  is a bijection. In fact, its inverse may be described in
the following way . Given [w0, . . . , wN ]  CPN , consider the non-zero polynomial

                                        N              N!
                                                  k!(N -
                            P (z) =        (-1)k             k)!     wk zN-k     ,

                                     k=0

which has degree l  N . Calling z1, . . . , zl the complex roots of P (z), one has

                 -1 [w0, . . . , wN ] = [1, z1], . . . , [1, zl] , [0, 1], . . . , [0, 1] .

Using this bijection, MN can also be identified with CPN .

                                                    3
3 Vortices near the Bradlow limit

Although we have an accurate description of the moduli space MN , the explicit form of
the solutions (D, ) of (1) and (2) is not known. In particular, this has prevented any
successful attempt to describe the dynamics of the vortices by means of the well-known geodesic
approximation. The purpose of this paper is to show that by replacing the exact Bogomolny
equations by two other conditions, which should be a good approximation near the Bradlow
limit R2  N , one can obtain the solutions explicitly; they also have CPN as their moduli
space, and furthermore the dynamics of these "pseudo-vortices" is completely computable in
the framework of the geodesic approximation.

     Since for R2 = N the pair (DN , 0)  A � (E) is an exact solution of (1) and (2), we
may expect that for R2 close to N the solutions (D, ) will have D  DN (after a gauge

transformation if necessary). We therefore impose D = DN and look for   (E) such that :

      � (DN , ) is a solution of (1), i.e. DN0,1 = 0 ;                                                          (4)

      � (DN , ) satisfies (2) "on average", i.e.                    FN     +  1  (||h2  -  1) volR  =0;         (5)
                                                                              2
                                                             CP1

( We note in passing that eq.(4) is analogous to the equation for electron wavefunctions of the

first Landau level in the uniform background magnetic field FN ; eq.(5) is then a wavefunction
normalization condition. )

     We will now find the explicit solutions of (4) and (5), and then describe their moduli space.
Using the local trivialization 1 of E and the chart 1 of CP1 defined before, the equation
DN0,1 = 0 over the domain U1 is the same as (� - iA0,1)1 = 0 , or explicitly, using (3):

                                       1     =     -N z           1     ,                                       (6)
                                       z�       2(1 + |z|2)

where 1  C(C) is the representative of  with respect to 1 .
     Equation (6) has the general solution 1 = f (z)(1 + |z|2)-N/2 , with f holomorphic on C.

The section  of E determined by 1, which is only defined over U1 , has a representative 2
                                                    1
with  respect  to  2  given  by  2(z)  =  g12(z)1(  z  )  ,  which  is  smooth   on     C\{0}.  But  since  we  are

looking for global solutions of (4),  must be extensible to all of CP1, and this will happen iff

2(z) is smoothly extensible to C. Writing f as a Taylor series, it is then not difficult to check
that this requires that the coefficient of zn vanishes for all n > N . Thus any solution  of (4)

must have a representative 1 over U1 of the form

                                       1(z)  =  a0zN + � � � + aN          ,                                    (7)
                                                  (1 + |z|2)N/2

and conversely any 1 of this form determines a global section  of E which is a solution of (4)
over U1, and by continuity over all of CP1.

     If  is represented by 1 as in (7), then the representative 2 will be

                                       2(z)  =  a0 + � � � + aN zN
                                                  (1 + |z|2)N/2

                                                    4
and hence, as for (1) and (2), any solution  of (4) has exactly N zeros over CP1, counting
multiplicities.

     We now turn to condition (5). Using that -iFN is the curvature form of a degree N bundle,
(5) is equivalent to

                                                  2iR2                            N    k!(N - k)!
                                                  + |z|2                                (N + 1)!
4(R2 - N ) =      ||2h volR =         |1  |2  (1          )2  dz  dz�  =     4R2                   |ak|2  ,

              CP1                  C                                              k=0

where the last integral is calculated in the appendix for 1 of the form (7). We can therefore

conclude that 1 represents a solution  of (4) and (5) iff 1 is of the form (7) and satisfies the

normalization condition      N

                                   k!(N - k)!     |ak |2  =   1-  N    .
                                    (N + 1)!                      R2
                             k=0

Calling D  A � (E) the subspace of solutions of (4) and (5), we thus get a bijection  : D 
S2N+1  CN+1 that maps each   D, represented by a 1 like in (7), to the point

              1  -       N   -1/2  ... ,  k!(N - k)!          1/2                      .                  (8)
                         R2                (N + 1)!
                                                                 ak , . . .  0kN

     The following step is to determine when two solutions in D are gauge equivalent. Let
therefore (DN , ) and (DN , ~) be a pair of solutions, an suppose g : CP1  U (1) is a gauge
transformation on E that takes one into the other. Using the usual transformation rule for
connection forms under g, and the key fact that the connection is fixed, it is readily shown that
g must be constant. So ~ = ei for some   R. Since the converse is clear, we conclude that
(DN , ) and (DN , ~) are gauge equivalent iff

                         ~ = ei   ~1 = ei1  c~ = ei c

for some   R, where c, c~  S2N+1 are the images of (DN , ) and (DN , ~) under the bijection
. Furthermore, notice that this last condition is also equivalent to (c~) = (c) in CPN , where
 : S2N+1  CPN is the usual principal U (1)-bundle.

     Calling MN the moduli space of solutions of (4) and (5) up to gauge transformations, and
p : D  MN the natural projection, we therefore have :

                                      D --- S2N+1


                                      p                                                                   (9)

                                   MN ---~  CPN

where ~, defined by the commutativity of the diagram, is, like , a bijection. The right-hand
side of this diagram is a concrete model for the space of solutions D and its moduli space.

                                                  5
4 The metric on the moduli space

Using the usual prescriptions of the geodesic approximation (first described in [10]), we will now
obtain the metric m on MN which, within the framework of this approximation, determines
the dynamics of the "pseudo-vortices" (which from now on will be just called vortices).

Suppose one has a curve  in D:
                   t - (DN , (t))  D - (w0(t), . . . , wN (t))  S2N+1 .

A natural hermitian metric on D is defined by

                               d   ,  d   (t) :=    1          h (t), (t)          volR ,                                   (10)
                               dt     dt            2
                                                           CP1

where the dot stands for the time derivative. Notice that in this case, as opposed to what

happens in [12], the gauge potentials do not contribute to the metric, since the connection in

our space D is fixed, and thus time independent.

Writing                                             a0(t) zN + � � � + aN (t)
                                                          (1 + |z|2)N/2
                                      1(t)   =

for the usual representative of (t), using the unitarity of 1, and noting that
1 = (1 + |z|2)-N/2(a 0zN + � � � + a N ) , one has that

d               d           1                2iR2                                     N  k!(N - k)!
dt              dt          2             (1 + |z|2)2                                     (N + 1)!
             ,      (t)  =       | 1 |2                    dz  dz�    =     2R2                            a k  a� k  =

                               C                                                   k=0

                                             N

                         = 2(R2 - N ) w k w� k ,

                                             k=0

again using the integral calculated in the appendix. We conclude that the hermitian L2 metric
on D corresponds via the map  to the restriction to S2N+1 of the canonical hermitian metric
on CN+1, up to the constant factor 2(R2 - N ). This metric will also be called �, � .

According to the usual procedure, the metric m on MN is induced from �, � on D in
                                                                         d                          d
the following way.  Given q  D and a tangent vector                      dt        TqD ,    let  (  dt  )  be   its   component

perpendicular to the subspace of TqD formed by the vectors tangent to curves on D which are

pure gauge transformations, that is perpendicular to ker(p)q. Then

                               (pm)q      (  d   ,  d   )  :=  (  d   ),    (  d   )  q  .
                                             dt     dt            dt           dt

We will now compute the metric on CPN corresponding to m by the identification ~. It will

also be called m.

Using the diagram (9), the subspace ker(p)q  TqD corresponds to the subspace
ker()(q)  T(q)S2N+1. Given w  S2N+1  CN+1 , we have that ker()w is the one-

dimensional  real   subspace   generated     by     the  vector   d   (eit  w)(0)  =     iw.  Therefore,   given         a  tangent
                                                                  dt

                                                           6
vector  d   = (0, . . .  ,  N )       Tw S 2N +1        TwCN+1,                  we  have
        dt

                                                (  d   )     =        d   -      d   ,  w  w  ,
                                                   dt                 dt         dt

                                                                                 w, w

so

    (  d   ),  (  d   )     =     d   ,  d   -     d      ,  w        w,  d                                       N
       dt         dt              dt     dt        dt                     dt
                         w                                                          = 2(R2 - N ) (jk - w�jwk) j � k ,
                                                             w, w
                                                                                                         j,k=0

where the computation in the last step uses that w, w = 2(R2 - N ), since w  S2N+1. Thus
m is the restriction to S2N+1 of the 2-tensor in CN+1

                                                                       N

                                  2(R2 - N ) (jk - w�jwk) dwj  dw�k .

                                                                     j,k=0

Now consider the Ka�hler form � associated to m. It is defined, as usual, using the imaginary
part of m: � = -Im m  2(CPN , R). We have

�       =  (-Im m)          =  -Im(m)           =      2(R2           -   N   )  i   N                             |S 2N +1
                                                                                 2
                                                                                         (jk - w�j wk) dwj  dw�k

                                                                                    j,k=0

                            i  N                   jk                                           w�j wk
                            2                      ���+                                       +���+
        =  2(R2   -   N  )               |w0|2  +               |wN |2       -      (|w0|2               |wN |2)2  dwj  dw�k |S2N+1

                               j,k=0

        =  2(R2   -   N  )  i  �  log(|w0|2     +  �   �  �  +  |wN       |2)    |S 2N +1     = 2(R2 - N ) �FS
                            2

where �FS is the Fubini-Study form on CPN , and the last equality is a well-known result [8, p.
160]. Since  and ()w are both surjective,

                      � = (2(R2 - N )�FS) implies � = 2(R2 - N )�FS .

Therefore m = 2(R2 - N )mFS , where mFS is the Fubini-Study metric on CPN , because a
hermitian metric is uniquely determined by its Ka�hler form.

5 Vortex dynamics

Having determined the metric m on the moduli space MN = CPN , we will now proceed to
explicitly describe its geodesics, which provide an approximate description of the low-energy

particle dynamics. Note that m  mFS implies that the geodesics of m are exactly the Fubini-
Study geodesics. These are well-known [8, p. 277] but nevertheless we will rederive them here

again.
     Let  : CN+1 \{0} - CPN be the natural projection and 0 : U0 - CN one of the

standard charts of CPN , where U0 = {[w0, . . . , wN ]  CPN : w0 = 0}. Calling (c1, . . . , cN ) the

coordinate functions of this chart, then by definition of the Fubini-Study metric we have on U0 :

                  �FS    =  i  �  log(1  +   |c1|2        +  �  �  �  +   |cN  |2)   =     i  hjk�  dcj    dc�k    and
                            2                                                              2

                  mFS = hjk� dcj  dc�k ,

                                                                          7
with

                                     hjk�     =  1  jk       -   (1  ck c�j         .                             (11)
                                                    + |c|2           + |c|2)2

For a general Ka�hler metric the geodesic equations have the simplified form [14, p. 4]:

       c�k  =  -     hjs�  hks�  cl  cj    ,              where hks� := (sk entry of [hi�j ]-1) .
                     cl

In our case hks� = (1 + |c|2)(sk + ckc�s), and so the geodesic equations for (CPN , mFS) in the
chart 0 are

                                              c� =      2 < c ,  c>    c     ,                                    (12)
                                                       1+ < c    ,c >

where c(t) is a curve in CN and < �, � > is the canonical hermitian product.
     Now consider curves in S2N+1  CN+1 of the form:

                         (t) = sin(t) y + cos(t) x ,                                      tR                      (13)

where x, y  CN+1 are orthonormal with respect to the canonical hermitian product of CN+1.
If x0 = 0, then   (t) / U0 only for a discrete set D of non-zero values of t, and a short
computation shows that, in R\D,

               c(t)  :=  0        (t)         =     c(0)  +  c(0)  (y0          x0 sin(t)                         (14)
                                                                             sin(t) + x0 cos(t))

where

       ck (0)  =     xk    and                ck (0)   =  (ykx0 - xky0)                ,  k = 1, . . . , N .      (15)
                     x0                                         (x0)2

     One can verify directly that this c(t) satisfies (12), and therefore   (t) is a geodesic for
t in R \ D, and by continuity for all t. If x0 = 0 , a similar computation in one of the other
standard charts of CPN would establish that, also in this case,   (t) is a geodesic.

     On the other hand, it is not difficult to verify that every geodesic of (CPN , mFS) can be

written as , where  has the form (13). Although one could give a general, chart-independent

argument for this, for later convenience we will proceed unnaturally. Namely, using (15), one
may simply check that given any c(0)  CN and c(0)  Tc(0)CN = CN , the geodesic   (t) with

       x = (1 + |c(0)|2)-1/2 1 , c(0)

       y = -1(1 + |c(0)|2)-1/2                   -  < c(0), c(0) >        ,  c(0) -       < c(0), c(0)   >  c(0)
                                                      1 + |c(0)|2                           1 + |c(0)|2
                                                                                                                  (16)

                                                       |  <  c(0), c(0) >       |2  1/2
                                                             1 + |c(0)|2
        = (1 + |c(0)|2)-1/2          |c(0)|2        -

has initial position and velocity -0 1(c(0)) and (0-1)(c(0)), respectively. This shows that every
geodesic starting in U0 is of the form   (t). Similar calculations in the other standard charts
would extend the result to all of CPN .

                                                             8
     We now note two general properties of the geodesics   (t). Firstly, using (11) and

(15), one can compute that the velocity of the geodesic, which is a constant of motion, is ||.
Secondly, notice that all the geodesics of (CPN , mF S) are periodic. It is not difficult to show
that for  = 0 the period is /||.

     We will now use our knowledge of the geodesics on the moduli space (CPN , m) to give an

explicit description of the vortex dynamics.

     Recall from Section 3 that the solutions (DN , )  D with the vortices (zeros of ) in
positions -1 1(z1), . . . , -1 1(zN ) in CP1, are represented by a function 1 of the form (7), where
we now have

                                  a0zN + � � � + aN  (z - z1) � � � (z - zN ) ,

and therefore

               ak = A (-1)k Sk(z1, . . . , zN ) , k = 0, . . . , N

where the Sj are the usual elementary symmetric polynomials, and A is a normalization factor
which is non-zero for R2 > N . Thus such solutions (DN , )  D correspond by    to (see (8) )

. . . , (-1)k  k!(N - k)!        1/2                                        CPN = MN
                (N + 1)!
                                    Sk(z1, . . . , zN ) , . . .  0kN

and by 0     to c = (c1, . . . , cN )  CN , where

                              ck = (-1)k  N  -1/2                                     (17)
                                          k
                                                  Sk(z1, . . . , zN ) .

     Inverting these relations, we can obtain the positions of the N vortices as a function of the
coordinates ck of a given point in the moduli space CPN . In particular, to the geodesics c(t) of

the form (14) corresponds a motion of the vortices determined by:

                           N  N  1/2                                                  (18)
                              k
               wN +                 ck(t) wN-k = (w - z1(t)) � � � (w - zN (t))

               k=1

where the zi(t) are the coordinates of the vortices in the chart (1 , U1) of CP1. Thus, since
we know all the geodesics of (CPN , m), we can determine all the possible N -vortex motions by
finding the roots of polynomials of degree N -- either analytically for N  4 or numerically for
N > 4.

     Now suppose we are given initial positions zi(0) and initial velocities zi(0) for the vortices,
where we assume that the zi(0) are all different. Through (17) and its derivative we can get the
corresponding values c(0), c(0)  CN , then use (16) to determine which geodesic c(t) corresponds

to this initial data, and finally solve (18) to get the motions zi(t). This general procedure has
been used to obtain the various special vortex motions shown below.

     We remark that, because (17) is a local diffeomorphism only in the region where the vortices

do not coincide, only in this region can we guarantee that the final result zi(t) has indeed the
prescribed initial velocities. This is why we take the zi(0) all different. If the zi(0) are not
all different there are some values of zi(0) that do not correspond to any zi(t) coming from a
geodesic motion.

                                             9
6 Examples of motions

Using the method described in the previous Section, we now give a few examples of 2-and 3-

vortex motions on the sphere . The trajectories are shown in the complex plane through the use
of the stereographic projection 1 : S2\{N }  C. The particular initial positions and velocities
used in each case are listed in Table 1.

z1(0)     1(a)    1(b)   1(c)     1(d)    2(a)   2(b)       2(c)  2(d)     3
z 1 (0)                                
z2(0)     1+i     1+i      1              1/2    1/2        1/2   1/2    a>0
z 2 (0)  -1 - i  -1 - i   -3    -2 i/ 3     i      i          i     i       i
z3(0)            -1 - i   -1     2 i/ 3     2      2          2     2
z 3 (0)     0     1+i      1    1 + i/ 3                     4i           -a
            0             --   -1 - i/3   0.6 i  3.7 i       --   4.5 i   -i
           --      --     --   -1 + i/ 3   --     --         --    --      --
           --      --           1 - i/ 3   --     --               --      --

                 Table 1: Initial positions and velocities

     To help with the interpretation of the figures, we recall that the stereographic projection
has the property of mapping circles of S2 (not necessarily great circles) to circles and straight
lines in the plane. The inverse 1-1 has the converse property. Also the circle of unit radius is
always shown in a dashed line; the northern (southern) hemisphere of S2 projects to the exterior

(interior) of that circle.

                         Fig. 1(a)                                Fig. 1(b)

                         Fig. 1(c)                                Fig. 1(d)

     Figure 1 :

(a) Two colliding vortices, one of which is at rest.
       One of the particles describes a great circle on the sphere that passes through the static
       position of the other.

                                    10
(b) Head-on collision of two vortices with the same speed.
       There are two collisions at antipodal points. The total trajectory is the union of two great
       circles.

(c) Head-on collision of two vortices with different initial speeds.
       Again two collisions occur. The total trajectory is the union of a great circle and another
       circle.

(d) Symmetrical collision of three vortices with equal speeds.
       The three vortices collide twice at antipodal points. The total trajectory is the union of
       three great circles.

Fig. 2(a)  Fig. 2(b)

Fig. 2(c)  Fig. 2(d)

     Figure 2 :

Except for 2(c), no collisions occur, and each vortex returns to its initial position after one
period. The degenerate case 2(c) is the same as 1(c) -- one great circle and another circle -- in
a different orientation.

                                                                               Fig. 3

     Figure 3 (with a=2) :

No collision takes place and the vortices exchange positions after one period. The coordinate
c1(t) of expressions (14) and (18) is always zero. The coordinate c2(t) is of the form
-a2 + 2a(1 + a4)/[2a3 + i cot(t)] . Taking one of the roots z(t) = x(t) + i y(t) of (18) and
eliminating t from the system x(t), y(t) , one obtains that the trajectory on the plane has the
simple equation (x2 + y2)2 + (1/a2 - a2)(x2 - y2) - 1 = 0. These are special cases of Cassini's
ovals and, when projected back to the sphere, look like the joint of a tennis ball.

                                                             11
7 Coincident particles and collisions

In this Section we start by finding an algebraic condition which determines when a point in
the moduli space MN = CPN corresponds to a vortex configuration where at least two of the
vortices coincide. We then use this condition to show that, for a system of N vortices starting
in different positions with arbitrary initial velocities, there are at most 2N - 2 collisions during
one period of the motion.

Using diagram (9) and the definition (8) of the bijection , it is not difficult to recognize that

a point [w0, . . . , wN ]  CPN corresponds by ~-1 to the equivalence class in MN of a solution 

represented by

                                                            N      wk

                    1(z)  =     A (1 + |z|2)-N/2            k=0 (k!(N - k)!)1/2           z N -k  ,

where A is a non-zero normalization factor. Thus, asserting that [w0, . . . , wN ] corresponds to
a solution with at least two coincident vortices is equivalent to saying that one of the following
conditions holds :

�  P (z)        :=   N   (k!(N  wk              z N -k      has a root of multiplicity at least two ;
                    k=0         - k)!)1/2

� w0 = w1 = 0 , which corresponds to a double zero of  at [0, 1]  CP1 .

We now use the following result, whose proof is at the end of this section :

Lemma: For any n  N, there is a homogeneous polynomial S in n + 1 variables of
                                                                       n
degree 2n - 2, such that S(a0, . . . , an) = 0 if and only if          k=0          ak    z  n-k  has  a  multiple  root  or

a0 = a1 = 0 .

An explicit formula for S is given in the proof and we note that, up to a sign, S coin-
cides with the discriminant of k akzN-k whenever a0 = 0 .

     Using this lemma, it is clear that the points [w0, . . . , wN ]  CPN which correspond to at

least two coincident vortices, are exactly those of the algebraic hypersurface H of degree 2N - 2
in CPN determined by the equation

                    S~(. . . , wk, . . . )  :=  S( . . . ,  (k!(N  wk         ,  .  .  .  )  =    0.
                                                                   - k)!)1/2

     As we have seen in Section 5, any motion of N vortices in S2 corresponds to a Fubini-Study
geodesic in CPN , and these are all of the form t  (sin(t)y + cos(t)x), with x, y  CN+1
orthonormal and  being the projection from CN+1 to CPN . By the discussion above, it is also

clear that this motion will have a collision of two or more vortices iff the corresponding geodesic
intersects H. But since this geodesic lies on the projective line L = (spanC{x, y})  CPN ,

and does not intersect itself during one period, we conclude that the number of collisions is not

bigger than the cardinality of L  H.

     It is, however, a standard result in algebraic geometry that either L  H or # (L  H) 
deg H = 2N - 2 . In fact, denoting x = (x0, . . . , xN ) and y = (y0, . . . , yN ) in CN+1, it follows

                                                            12
that a point (ux + vy) in L, with (u, v)  C2\{0}, belongs to H iff

                     Q(u, v) := S~(ux0 + vy0, . . . , uxN + vyN ) = 0 .

But since S~ is homogeneous of degree 2N - 2, so is Q, and therefore there is a factorization (see

[7, p. 31] )

                         2N -2

              Q(u, v) =         (iu + iv) ,                for some (i, i)  C2 .

                         i=1

If Q is identically zero we have L  H. If Q is not identically zero then the roots of Q are

(i, -i) = 0 i , and it is apparent that L  H consists of the points (ix - iy), which are
at most 2N - 2.

We finally conclude that, either the vortices have a motion with at least two of them

coincident for all time, which corresponds to L  H, or there are at most 2N - 2 collisions in

one period.

Proof of the lemma :

This lemma is a slight generalization of well-known algebraic results, as stated for example in
                                              n                                                  nk=1(n -
[5, p. 168] or [3, p. 178]. Consider P (z) =  k=0      ak  zn-k  and  its  derivative  P (z)  =

k + 1)ak-1zn-k, and form the usual resultant

                                           a0          ���            an
                                                  ...                       ...
                                                       a0
              RP,P (a0, . . . , an) := na0             ���       ���             an
                                                  ...
                                                        na0      an-1
                                                                          ...

                                                                 ���             an-1

where there are n - 1 rows with the coefficients of P and n rows with the coefficients of P , so
that the matrix is (2n - 1) � (2n - 1). Applying the usual expansion to the first column of this
determinant we get

                                       RP,P (a0, . . . , an) = a0 S(a0, . . . , an)

with

S(a0, . . . , an) =

a0            ���        an                                      a1 � � � an

              ...               ...                              a0 � � �        an

                     a0 � � �         an                              ...               ...

= (n - 1)a1 � � � an-1                        + (-1)n n                      a0 � � �            an .

na0 � � �               an-1                                     na0 � � �       an-1
           ...                   ...                                    ...               ...

                     na0 � � �        an-1                                   na0 � � �           an-1

                                              13
Expanding again the first columns of the determinants in S(0, a1, . . . , an) we get

S(0, a1, . . . , an) = (-1)n(n - 1) a1 RQ,Q + (-1)nn a1 RQ,Q = (-1)n(2n - 1) a1 RQ,Q

where Q(z) =  n    ak  zn-k  .
              k=1

Now, if a0 = 0 , by standard results in basic algebra (see [5, 3]),

                                 RP,P  = (-1)n(n-1)/2a0 D(P ) ,

where D(P ) is the discriminant of P , and therefore

              S(a0, . . . , an) = 0  D(P ) = 0  P has a multiple root .

If a0 = 0 then P (z) = Q(z) and

              S(a0, . . . , an) = S(0, a1, . . . , an) = 0  a1 = 0 or RQ,Q = 0 .

But when a1 = 0, by the same algebraic results, RQ,Q = 0  Q = P has a multiple root.
     We finally conclude that

              S(a0, . . . , an) = 0  P has a multiple root or a0 = a1 = 0 .

                                                Acknowledgements

NSM thanks Michael Singer for discussions about the Fubini-Study metric, and also thanks the
Pure Mathematics Department, University of Adelaide, for hospitality at the time this work was
initiated. JMB is supported by the `Funda�ca~o para a Ci^encia e Tecnologia', Portugal, through
the research grant SFRH/BD/4828/2001.

                                 14
Appendix

In this appendix we compute integrals of the form

                            �  (1  2iR2      dz      dz�  =         �  (1  +   4R2      y2)2   dx  dy
                                   + |z|2)2                                    x2 +
                       C                                      R2

where  = (1 + |z|2)-N/2(a0zN + � � � + aN ) and  = (1 + |z|2)-N/2(b0zN + � � � + bN ) .
     Write

                 N

          � =              aN-j �bN-k fkj(z) ,                with fkj(z) = z�kzj (1 + |z|2)-N .

                 k,j=0

Using polar coordinates and integration by parts,

I(k, j, N ) : =              fkj (z)     =       2                         (1   rk+j           r  dr   =
                       R2 (1 + |z|2)2                               0          + r2)N+2
                                                    ei(j-k) d

                                                0

                                       r2k+1                      -               r2k  d             1
                               0   (1 + r2)N+2                   N+                    dr     (1 + r2)N+1
             = 2 jk                                  dr   =  jk        1                                            dr =

                                                                           0

             =   jk         2k           (1  r2k-1        dr  =   jk   N   k   1  I (k  -  1,  k  -   1,  N  -  1)
                           N +1       0      + r2)N+1                      +

where the vanishing of the boundary terms in the integration by parts is valid for N  k  1.
Since

I(0, 0, N - k) = 2                (1  +    r         dr   =       -                    1                             
                            0            r2 )N -k+2           N -k+1           (1 + r2)N-k+1                    N -k+1
                                                                                                          =

                                                                                                       0

we have

         I(k, j, N )   =   jk  (N       k(k - 1) � � � 1      I(0, 0, N    - k)   =     k!(N - k)!           j  k   .
                                      + 1) � � � (N + 2 - k)                             (N + 1)!

The final result is therefore

             2iR2                            N                                                 N      k!(N - k)!
             + |z|2)2                                                                                  (N + 1)!
     �   (1            dz    dz�   =  4R2         I(k, k, N ) aN-k �bN-k = 4R2                                         ak  �bk  .

C                                            k=0                                              k=0

                                                          15
References

 [1] K. Arthur and J. Burzlaff, Lett. Math. Phys. 36, 311 (1996)
 [2] S. Bradlow, Commun. Math. Phys. 135, 1 (1990)
 [3] P.M. Cohn, `Algebra', vol. 1, John Wiley & Sons (1974)
 [4] O. Garc�ia-Prada, Commun. Math. Phys. 156, 527 (1993)
 [5] P. Grillet, `Algebra', John Wiley & Sons (1999)
 [6] A. Jaffe and C. Taubes, `Vortices and Monopoles', Boston, Birkh�auser (1980)
 [7] F. Kirwan `Complex Algebraic Curves', London Math. Soc. Student Texts 23, Cambridge

      University Press (1992)
 [8] S. Kobayashi and K. Nomizu `Foundations of Differential Geometry', vol. 2, Interscience

      Publishers (1969)
 [9] R. MacKenzie Phys. Lett. B 352, 96 (1995)
[10] N.S. Manton, Phys. Lett. B 110, 54 (1982)
[11] N.S. Manton, J.M. Speight, hep-th/0205307
[12] T.M. Samols, Commun. Math. Phys. 145, 149 (1992)
[13] D. Stuart, Commun. Math. Phys. 159, 51 (1994)
[14] G. Tian, `Canonical metrics in Ka�hler geometry', Lectures in Mathematics EHT Zu�rich,

      Birkhauser (2000)

                                                             16
