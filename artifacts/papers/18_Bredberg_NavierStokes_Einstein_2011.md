# Bredberg NavierStokes Einstein 2011

**Source:** `18_Bredberg_NavierStokes_Einstein_2011.pdf`

---

arXiv:1101.2451v2 [hep-th] 14 Jan 2011                  FROM NAVIER-STOKES TO EINSTEIN

                                                           Irene Bredberg, Cynthia Keeler, Vyacheslav Lysov and Andrew Strominger

                                                                  Center for the Fundamental Laws of Nature, Harvard University
                                                                                             Cambridge, MA, 02138

                                                                                                             Abstract

                                        We show by explicit construction that for every solution of the incompressible Navier-Stokes equation
                                        in p + 1 dimensions, there is a uniquely associated "dual" solution of the vacuum Einstein equations
                                        in p + 2 dimensions. The dual geometry has an intrinsically flat timelike boundary segment c whose
                                        extrinsic curvature is given by the stress tensor of the Navier-Stokes fluid. We consider a "near-horizon"
                                        limit in which c becomes highly accelerated. The near-horizon expansion in gravity is shown to be
                                        mathematically equivalent to the hydrodynamic expansion in fluid dynamics, and the Einstein equation
                                        reduces to the incompressible Navier-Stokes equation. For p = 2, we show that the full dual geometry is
                                        algebraically special Petrov type II. The construction is a mathematically precise realization of suggestions
                                        of a holographic duality relating fluids and horizons which began with the membrane paradigm in the
                                        70's and resurfaced recently in studies of the AdS/CFT correspondence.
Contents

1 Introduction                                      2

2 Relation to previous work                         3

3 The hydrodynamic limit and the -expansion         4

4 Characterizing the dual geometries                4

5 Nonlinear solution in the -expansion              6

5.1 The solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

5.2 Forcing the fluid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

5.3 Singularities at r = � . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

5.4 Uniqueness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

6 Alternate presentation                            9

7 Petrov type                                       10

8 Nonlinear solution in the near-horizon expansion  11

9 Acknowledgements                                  12

A Appendix                                          12

                                        1
1 Introduction

The Einstein equation

                                               G� = 0,  (1)

and the incompressible Navier-Stokes equation

                       vi - 2vi + iP + vjjvi = 0,       (2)

have long played central roles in both mathematics and physics. The Einstein equation universally governs
the long-distance behavior of essentially any gravitating system, while the incompressible Navier-Stokes
equation universally governs the hydrodynamic limit of essentially any fluid. They both display a rich
non-linear structure which has been a continual source of interesting surprises yet remains, centuries
after their discovery, incompletely understood. It is the purpose of this paper to give a mathematically
precise relationship between (1) and (2) and their solutions, and thereby provide a hopefully useful bridge
between the two subjects. For example cosmic censorship could be related to global existence for Navier-
Stokes or the scale separation characterizing turbulent flows related to radial separation in a spacetime
geometry, see e.g. [1, 2].

    Hints of such a connection, summarized in the next section, have surfaced in various forms over the
last three decades [3�28], see [26, 29�32] for reviews. In particular, excitations of a black hole horizon
dissipate very much like those of a fluid [3�5, 12, 13, 28, 33�35], and there has been recent discussion of
a holographic duality relating black holes and fluids [1, 8�10, 12, 14�17, 19, 21, 23, 24]. Inspired by these
suggestions, in this paper we explicitly construct a map from solutions of the nonlinear incompressible
Navier-Stokes equation to solutions of the nonlinear Einstein equation. A key ingredient is the imposition
of boundary conditions which, in a sense to be defined, isolate the horizon dynamics from the rest of the
gravitational dynamics and thereby reduce equation (1) to equation (2).

    Our basic construction is roughly as follows. We begin with the region of p+2-dimensional Minkowski
space inside a hypersurface c given by an equation of the form x2 - t2 = 4rc. c is intrinsically flat
(being the translation of an hyperbola in the t-x plane along the remaining p spatial directions), but has


an extrinsic curvature linked to the constant acceleration a = 1/ 4rc. It asymptotes to its future horizon
H+ which is the null surface x = t. We then study the effect of finite perturbations of the extrinsic
curvature of c while keeping the intrinsic metric flat. These generically lead, when evolved radially
inward with the Einstein equation, to singularities on H+. The special ones which are smooth on H+
are analyzed in the hydrodynamic " -expansion", which is a nonrelativistic, long-wavelength expansion
and, importantly, keeps terms that are nonlinear in the size of the perturbation. It is found that tensor
and scalar modes of the metric decouple in this limit and the remaining degrees of freedom are vector
modes governed by the Navier-Stokes equation in p + 1 dimensions. We present (equation (14) below) the
p + 2-dimensional solution of the Einstein equation through third order in the hydrodynamic expansion
parameter . The first term is flat space. The second and third terms are algebraically constructed from
the velocity field vi and pressure P of an incompressible fluid. The nonlinear spacetime Einstein equation
then reduces to the nonlinear incompressible Navier-Stokes equation for the pair (vi, P ).

    This result is already interesting and non-trivial, but the fact that the Navier-Stokes arises when the
geometric variables are subject to the same kind of expansion used in fluid dynamics might have been
anticipated. A deeper connection appears when we consider an alternate expansion in which, instead of
going to long distances, we take the acceleration of c to infinity. This is a near-horizon limit since it
pushes c towards its horizon H+. We then show that, after a constant overall rescaling of the metric, the
near-horizon expansion is mathematically identical to the hydrodynamic expansion. Hence the solutions of
the Einstein equation (constrained by the boundary conditions of a flat metric on c and smoothness on
H+) in this near-horizon expansion are in one-to-one correspondence with solutions of the incompressible
Navier-Stokes equation. This then is the precise mathematical sense in which horizons are incompressible
fluids.

                                               2
    It is possible that the ultimate origin of this relation is a deep and exact holographic duality relating
(among other things) quantum black holes to fluids as has been suggested by string theoretic investiga-
tions. However in this paper we have concentrated on simply establishing the mathematical relationship
between (1) and (2) in a manner which makes no assumptions about or reference to this tantalizing
possibility.

    This paper is organized as follows. In section 2 we briefly describe precursors of our construction
going back to the 70's. Section 3 briefly reviews the hydrodynamic expansion in the study of fluids, and
the emergence of the incompressible Navier-Stokes equation in the hydrodynamic limit. In section 4 we
specify the boundary conditions, explained roughly above, used to isolate horizon dynamics. In section
5 we present the general solution of the nonlinear Einstein equation with these boundary conditions
through the first three orders in the hydrodynamic expansion, and show that the first nontrivial term
corresponds to the velocity field of an incompressible fluid. We also discuss the geometric analog of forcing
the fluid, argue for uniqueness, and discuss the possible formation of black hole type singularities. Section
6 presents a simpler form of the metric and shows that, up to an overall rescaling and after an appropriate
coordinate transformation, it depends only on the product of the leading-order acceleration of c and the
hydrodynamic expansion parameter . In section 7 we show that the geometries are, through the order
constructed, of a special type known in four dimensions as Petrov type II. This may enable a connection of
the present work with the large literature on algebraically special spacetimes [36�38]. Finally in section
8 we demonstrate, using the simplified metric of section 6, the equivalence of the hydrodynamic and
near-horizon expansions.

2 Relation to previous work

The first suggestion of a relation between horizon and Navier-Stokes dynamics appears in the prescient
thesis of Damour [3]. This work contains an expression now known as the Damour-Navier-Stokes equation
[39] governing the geometric data on any null surface. Although tantalizingly similar, it is not quite the
Navier-Stokes equation as it has too many variables (eliminated herein by an appropriate boundary
condition) and an extra nonlinear term. To get precisely Navier-Stokes we found it necessary to consider
the near-null limit of a highly accelerated timelike surface. Such a surface was introduced by Price and
Thorne [5] and coined the stretched horizon (analogous to our c). Although similar in spirit their limit
is slightly different from ours. They obtain a compressible fluid with a negative bulk viscosity and an
extra term not present in Navier-Stokes. This approach was developed into the membrane paradigm
and is reviewed in the book [40]. Much more recently Policastro, Starinets and Son [9] made the striking
observation, in the context of the AdS/CFT correspondence, that the dissipative behavior of a large black
hole in AdS agrees with that of the hydrodynamics of the holographically dual CFT. This observation
has been developed in many directions [10, 12, 29, 41�51]. Although far from obvious at first glance, these
results from AdS/CFT are compatible with, and in some cases equivalent to, the earlier results from pure
gravity [10,23,28,52,53]. In the AdS/CFT context Bhattacharya, Minwalla and Wadia [1,23] showed that
in asymptotically AdS spacetimes at finite temperature, the asymptotic AdS boundary data is governed
in a hydrodynamic limit by the Navier-Stokes equation. They use the Navier-Stokes data to construct
a bulk solution of the Einstein equation with negative cosmological constant. Our dual bulk geometry
in equation (14) is a refinement of expression (4.4) in [1] in which the cosmological constant is taken to
zero and the boundary can be pushed to any radius - in particular to the interesting near-horizon region.
Finally we rely heavily on our previous paper [28] which solves the linear case within the framework
adopted herein.

                                                                    3
3 The hydrodynamic limit and the -expansion

The incompressible Navier-Stokes equation has a well-known scaling symmetry which is important in the
following and briefly reviewed here. Let the pair (vi, P ) solve the incompressible Navier-Stokes equation

ivi = 0,   vi - 2vi + iP + vj j vi = 0,                       (3)

where  is the kinematic viscosity and i = 1, ...p. Now consider a family of pairs (vi , P ) in which
frequencies and wavelengths are non-relativistically dilated and amplitudes scaled down by the parameter
 :

          vi (xi,  ) = vi( xi, 2 ),                           (4)

          Pi (xi,  ) = 2P ( xi, 2 ).

It is easy to check that (3) directly implies

 vi - 2vi + iP + v j j vi = 0.                                (5)

Hence (4) generates from the original solution a family of solutions parameterized by .
    In real fluids there are always corrections to the Navier-Stokes equation. Galilean invariance requires

that these vanish for constant vi. Typical corrections are for example of the form

 vi - 2vi + iP + vj j vi + vkvj kj vi + 2vi = 0.              (6)

If (vi, P ) obey this equation, the rescaled quantities obey

 vi - 2vi + iP + v j j vi + 2 v kv j kj vi + 2vi ) = 0.       (7)

The limit  0 is the hydrodynamic limit. In this limit these corrections become irrelevant. Similarly
the speed of sound goes to infinity and compressible fluids become incompressible. It is not hard to show
that all reasonable types of corrections are scaled away, and the incompressible Navier-Stokes equation
universally governs the hydrodynamic limit of essentially any fluid. The limit is an incredibly rich and
interesting one because, even though the amplitudes are scaled to zero, nonlinearities survive. It is this
hydrodynamic limit of a fluid that we will match to a near-horizon limit in gravity.

4 Characterizing the dual geometries

We seek a relation between the (p+2)-dimensional Einstein and (p+1)-dimensional Navier-Stokes equa-
tions. Of course, the former has a much larger solution space than the latter so only a special type of
Einstein geometry is relevant. Roughly speaking, the relevant geometries are non-singular perturbations
of a horizon. Let us now make this more precise.

    We consider geometries of the type depicted in Figure 1 with an outer "cutoff" boundary denoted
c. The boundary hypersurface c is taken to be asymptotically null in both the far future and far past.
In the Minkowskian coordinates dsp2+2 = -dudv + dxidxi, past null infinity I- is the union of the null
surfaces v  - together with u  - and c is the timelike hypersurface uv = -4rc with v > 0.
Past (future) event horizons H- (H+) are defined by the boundaries of the causal future (past) of c.
The dual geometries will be constructed in two a priori different expansions about Minkowski space: the
near-horizon and the hydrodynamic -expansion. Ultimately the two expansions will be shown to be
equivalent.

    Initial data can be specified on the union of c and I-. We consider initial data which is asymp-
totically Minkowskian and flat (no incoming waves) on I- (or equivalently H-). On c we generally
demand that the intrinsic metric ab be flat,

          ab = ab, a, b = 0, ...p                             (8)

                                               4
    r        r0
          H

                  r rc

                        c

          H

Figure 1: This figure depicts the Einstein geometry holographically dual to a fluid. The accelerated boundary hypersurface
c at radius r = rc is intrinsically flat but the extrinsic curvature is given by the fluid stress tensor. This extrinsic curvature
leads to gravity waves which propagate radially inward. The leading-order condition that these waves do not cross the past
horizon H- of c at  = - or produce singularities on the future horizon H+ at r = 0 is the non-linear incompressible
Navier-Stokes equation for the fluid.

although we will later consider "forcing" the system by perturbing ab.
    We wish to consider the general solution of the Einstein equations consistent with this initial data

and smooth on H+.1 In particular, so far we have not specified the extrinsic curvature Kab on c or
equivalently (and more conveniently) the Brown-York stress tensor on c2

Tab  2(abK - Kab).                                                      (9)

If no initial data were prescribed on I-, any Tab on c consistent with the constraint equations could be
chosen. This data could then in general be evolved radially inwards to produce a spacetime everywhere

inside of c. In general, such a spacetime will have gravitational flux (if not singularities) going up to
v =  (I+) as well as down to I-. Hence we have a "shooting problem" to find those special allowed
choices of Tab which produce a spacetime smooth on H+ with no flux coming up from I-.

    We solved this problem in [28] to leading order in a double expansion in long wavelengths and weak
fields.3 Ingoing Rindler coordinates were used for which the leading order flat metric is

ds2p+2 = -rd 2 + 2d dr + dxidxi.                                        (10)

c is the accelerated surface r = rc, H- is  = - and H+ is r = 0. These coordinates are conve-
nient for analyzing smoothness on H+. It was found that the allowed choices of Tab are precisely those
corresponding to the linearized fluid:

rc3/2T i = vi, rc3/2T ij = -(ivj),                                      (11)

where the (kinematic) viscosity here is given by the formula

                                                              = rc,     (12)

1Here we allow for incoming flux where I- meets c at u = -, v = 0.
2Our normalization here agrees with the conventional one for G = 1/16.
3Our conventions here differ from [28].

       5
while vi obeys the linearized incompressible Navier-Stokes equation

                                             ivi = 0,  vi - 2vi = 0.                                                          (13)

If we choose any value for the viscosity other than (12), the constraint equations on c are still obeyed,
but gravitational waves are propagated down to I- and there is a singularity at r = 0.

    In this paper we go one step further and solve the problem in certain hydrodynamic and near-horizon
limits without making a linearized approximation, enabling us to see a direct connection between the
nonlinear structures of the Navier-Stokes and Einstein equations.

5 Nonlinear solution in the -expansion

In this section we will improve on the analysis of [28] by solving the shooting problem in the long
wavelength -expansion without a simultaneous linearized expansion. The general solution will be pa-
rameterized by a solution vi(xi,  ), P (xi,  ) of the full nonlinear Navier-Stokes equation with viscosity
(12) together with the parameter .

5.1 The solution

Consider the metric

                 dsp2+2 = - rd 2 + 2d dr + dxidxi

                          -2              r  vidxid   -  2 vi  dxidr                                                          (14)
                                    1-                    rc

                                         rc

                                     r       (v2 + 2P )d 2 + vivj dxidxj +               v2 2P       d dr
                          + 1-                                    rc                        +
                                                                                         rc rc
                                    rc

                          -    (r2  -   rc2) 2vidxid  +  ...
                                    rc

where vi = vi(xi,  ) and P (xi,  ) are independent of r. Here and henceforth i, j = 1, ..p indices are raised
and lowered with ij and we take

                             vi  O( ), P  O( 2), i  O( ),   O( 2)                                                             (15)

as in the hydrodynamic scaling of section 3. It follows that the first line on the right hand side of (14) is
O( 0) and each subsequent line is one higher order in . The linearization of this expression in vi agrees
with the linearized solution studied in [28].

    On the cutoff surface c, r = rc and the induced metric is flat:

                                             abdxadxb = -rcd 2 + dxidxi,                                                      (16)

and hence satisfies the desired boundary condition. Here and henceforth xa  (xi,  ). The extrinsic
curvature and unit normal on c are

        1            1             1      cdTcd       N ��        1                           P         vi               3).
Kab  =  2 LN ab  =  -     Tab  -   p  ab         ,             =            + rc         1-       r  +        i  +  O(        (17)
                      2                                             rc                                    rc
                                                                                              rc

The Brown-York stress tensor is

     Tabdxadxb   =  dxi2  +   v2   d 2  - 2 vi dxid   +  (vi   vj + P   ij  )  dxi  dxj  - 2 ivj dxidxj  +    O(    3).       (18)
                      rc                       rc                rc3/2                          rc
                               rc

    We wish to solve the Einstein equations as a power series in . We first consider the necessary but
not sufficient condition that the constraints be satisfied on c. At order 0 the metric is flat and Tab

                                                         6
is constant so they are trivially satisfied. The only way to get an order term is with one power of vi
and no derivatives. Such a linear term cannot appear because the constant vi terms in (14) can, through

quadratic order, be obtained from a boost of flat space. The first nontrivial equation is encountered at

order 2:

                                    rc3/2aT a = ivi = 0.                                     (19)

This equation is satisfied if and only if vi is the velocity field of an incompressible fluid. Taking this to

be the case, one finds at order 3:

                   rc3/2aTai =  vi - 2vi + iP + vj j vi = 0.                                 (20)

This is satisfied if and only if vi solves the Navier-Stokes equation with pressure P and viscosity  = rc.
    Once the constraints are satisfied it is ordinarily possible to evolve the solution off the hypersurface,

in this case in the radial direction, at least for a finite distance. Here we have the danger of singularities
at the horizon H+ near r = 0, or equivalently waves coming up from I-. We know from [28] that such
singularities are absent in the linearized analysis provided the fluid viscosity takes the required value
(12). We have checked by direct computation that this absence of singularities extends to the nonlinear
case as well. That is all components obey

                                    Gra, Gab, Grr = O( 4)                                    (21)

and are nonsingular for finite values of r. Presumably the order 4 and higher terms in the metric can
be chosen so that the Einstein equations are solved exactly.

    It turns out that it is still possible to solve the Einstein equations analytically through order 3 with
the "wrong" value of the viscosity (i.e.  = rc ) even in the nonlinear case. As expected these solutions
develop a singularity at r = 0 near H+, and are presented in Appendix A .

5.2 Forcing the fluid

Solutions of the linearized Navier-Stokes equation decay exponentially in the future. There is some
expectation - although no proof - that nonlinear solutions eventually decay as well. Therefore the extrinsic
curvature on c in our examples is expected to become constant.

    On the other hand, already at the linear level, Navier-Stokes solutions grow exponentially in the far
past and typically are singular at  = - . Therefore we expect that the dual geometry is also singular
at  = -, which is the past horizon H- of c. This singularity is not problematic for real fluids, as we
are typically interested in cases where forcing terms correct the Navier-Stokes equation. For example we
might consider a fluid which is initially at rest, stirred at time  =  , and then left to evolve according
to the unforced Navier-Stokes equation.

    In fact this kind of situation is also very natural to consider on the gravity side. Consider flat
Minkowski spacetime with a flat metric and constant extrinsic curvature on the boundary c for  < .
We then stir it at  =  by momentarily perturbing the boundary condition that the induced metric
on c be flat. This will send out a gravitational shock wave along  =  and excite the geometry for
 > . The result should be an appropriate gluing of (14) along a null hypersurface to flat Minkowski
space. This is depicted in Figure 2.

    At the linear level, it is possible to explicitly construct the glued geometry describing this situation
through order 3. The metric is

ds2 = - rd 2 + 2d dr + dxidxi

          -  2(1 - r/rc)vidxid + (1 - r/rc) (jvi + ivj) dxidxj - 2        r2        2vidxid
                                                                    r - 2rc - rc/2

          - ( - )                        2  dxid  -  2   ij dxidxj  +...                     (22)
                   4(1 - r/rc)Fi + rc i              rc

                                            7


                                                                              c

Figure 2: On the c surface, prior to  = , all initial data is trivial. At  = , a gravitational shock wave arrives. The
shock forces the fluid on c, and consequently the vi is nontrivial on c after .

where Fi is an arbitrary function of xi obeying iF i = 0. ij and i (which is divergence free) are both
functions of xi and related to Fi by

                        j j i = Fi,       ij = ij + j i.                                               (23)

Since the metric on c is no longer flat, the constraint equations become linearized Navier-Stokes with a
forcing term similar to that described in [28]. For this configuration we have

                         vi - 2vi = F i(x)( - ).                                                       (24)

Clearly, since vi(x,  ) is taken to vanish for  < , the forcing term will cause it to jump to Fi(xi)
at  = , after which it will evolve according to Navier-Stokes. Given (24) this geometry solves the
linearized Einstein equations everywhere, and is characterized by an arbitrary divergence-free vector field
Fi(x). Before  =   it is flat, while afterward it is, up to a coordinate transformation, the linearization
of (14).

    At the nonlinear level, the equations are cumbersome and we have been unable to explicitly construct
the analog of (22) away from c. However it seems plausible that qualitatively similar solutions persist
at the nonlinear level.

5.3 Singularities at r = �

The square of the Riemann tensor for the solution (14) is given by

R2  =      3   (ivj  -  j vi)2  -    r    2vi2vi + 3ivj                          j 2vi - i2vj  + ....  (25)
       - 2rc2                      2 rc2

This expression diverges at r = �. Of course perturbation theory cannot be trusted when |r| is of order
1 , so the computation is unreliable in this regime. Whether or not there are actual divergences in these
regions will depend on the details of the solution. In general, at r = -, black hole type singularities
may plausibly arise.

    The divergence at r = + is outside the cutoff surface, so a priori need not concern us. Still we may
ask what happens if we try to extend the solution to this region. In general relativity with no cosmological

                                          8
constant it is hard to find solutions which are asymptotically flat in codimension one: i.e. there are no
codimension one black holes. This suggests that many configurations will be singular if extended to
r = +. On the other hand, if we add a negative cosmological constant, there are codimension one
asymptotically AdS black holes. At large r the cosmological term tends to dominate, and we expect in
this case many solutions to have nonsingular extensions to this region. However, as we will see below,
the hydrodynamic regime is small r so the large r behavior is of limited interest for the present purposes.

5.4 Uniqueness

Equation (14) gives the first three orders in the -expansion of metrics satisfying the Einstein equations
with the prescribed boundary data. These solutions are constructed from nonlinear solutions of the
incompressible Navier-Stokes equations. The latter are in turn, assuming existence and uniqueness for
Navier-Stokes, specified by a divergence-free vector field vi(x, ) at a moment of time .

    One may ask whether or not (14) is the unique solution with the prescribed boundary data (up to
coordinate transformations and field redefinitions) associated to a given vi(x, ). This can be addressed
in the context of a combined weak-field expansion and -expansion. The problem was solved to leading
nontrivial order in the weak-field expansion in [28]. The unique solution is the first two lines of (14), but
with a vi obeying the linearized Navier-Stokes equation. Generally one does not expect the dimension of
the solution space in weak-field perturbation theory to change unless there is a linearization instability
and associated obstruction. In the present case, the only potential obstruction is the Navier-Stokes
equation which we are assuming can be solved. Hence one expects the solution (14) to be unique at each
order in the -expansion, up to the usual ambiguity of adding solutions of the leading order equations at
subleading orders.

6 Alternate presentation

In this section we give an alternate presentation of the metric (14) in which all the factors of appear
explicitly, without being hidden in the functional dependence on the coordinates. This is accomplished
by first transforming to hatted coordinates

                                                     xi = rcx^i ,             =  rc^      ,    r = rcr^                             (26)

                                                                                   2

so  that  ^  =  O(   0)  and  we     denote      ^i      =        =   O(    0).  In       the  new        coordinates
                                                            x^i

                     dsp2+2   =  -     r^rc3  d^2    +   2rc2  d^dr^     +  rc2  dx^idx^i

                                         4                 2                 2

                                 -   2rc2     1  -   r^  v^idx^i  d^  -  2rcv^idx^idr^                                              (27)

                                                  2

                                 + (1 - r^)          rc2  v^2  + 2P^     d^2  +  rc v^i v^j dx^i dx^j     + rc(v^2 + 2P^)d^dr^

                                                                 2

                                 - (r^2 - 1)rc^2v^idx^id^ + . . . ,                                                                 (28)

where P^(x^, ^) =    1   P  (x(x^),    (^)),     v^i(x^, ^)       =   1 vi(x(x^),  (^)), v^2  v^iijv^j         and i, j indices are raised and

                      2

lowered with ij. The usual Navier-Stokes equation for v, P with  = rc implies

                                                     ^v^j - ^2v^j + v^k^kv^j + ^jP^ = 0.                                            (29)

This is the Navier-Stokes equation with  = 1 and no factors of or rc.

    Finally  let us  consider     the  rescaled             metric    ds^p2+2    =          2  dsp2+2  .  The  Einstein tensor  is  invariant under

                                                                                          rc2

such constant metric rescalings. Rearranging terms and defining

                                                                                       2                                            (30)

                                                                           rc

                                                                              9
one finds

      ds^2p+2     =  -  r^ d^2


                     + 2d^dr^ + dx^idx^i - 2(1 - r^)v^idx^id^ + (1 - r^)(v^2 + 2P^)d^2                               (31)

                     +  (1 - r^)v^iv^jdx^idx^j - 2v^idx^idr^ + (v^2 + 2P^)d^dr^ + (1 - r^2)^2v^idx^id^ + . . . .

The Brown-York stress tensor is

                                                             T^ji  =    1   ji    +          v^iv^j + P^ji - 2^iv^j  + O(3/2). (32)
T^^^ = - v^2,             T^i^ = - v^i,                                                


                                                                                                                                                                                                            2

The important point here is that the geometry depends only on the ratio  = rc and not or rc separately.
    Given that the rescaled geometry depends only on  and the -dependence (21) of the unrescaled

geometry (14) we conclude that in the hatted coordinates

                                      G^^   =  rc2  G              O(0),           G^i^j  =  rc2  Gij    O(),

                                                4                                             2

                                      Gr^^  =  rc2  Grr            O(),        Gr^r^ = rc2Grr  O(2)

                                                2

                                      G^^i  =  rc2  G     i     O(1/2),            Gr^^i = rc2 Gri  O(3/2).          (33)

                                                3

Given the explicit factor of -1 in g^^, it is not immediately obvious in this presentation that in a direct
computation the Einstein tensor will even have a good Taylor expansion in . What happens is that,
because gr^r^ = 0, there are only a limited number of powers of g^^ that can appear in the Einstein tensor,
and one may thereby directly recover (33). In fact, direct computation reveals we do slightly better; the
last line may be replaced by

                                      G^^i  =  rc2    G   i        O(1),           Gr^^i = rc2 Gri  O(2).            (34)

                                                3

    Notice that G^^ in (33) is of order 0 rather than 1. We can improve this by computing a few higher
order pieces of the metric. Specifically, we add to (31)

                          -2(1 - r^)q^idx^id^ + 22gr(^2i)dr^dx^i + 2gi(j2)dx^idx^j + . . .                           (35)

Demanding that the r-independent pieces of G^^ = 0 be solved through order 0 then fixes q^i(^, x^):

                                ^iq^i    =  ^2v^2     -      1  v^i^i  v^2  -  3  ^v^2    -  1    ^iv^j + ^jv^i  2   (36)
                                                             2                 2             2
                                                                                                                  .

Apparently q^i is a kind of heat current. Demanding that the entire G^^ = 0 through order 0 gives us a
differential equation for the combination Q^(r^, ^, x^)  -2^igr(^2i) + r^gii(2):

Q^ +  2r^r^Q^  =  2^iq^i  - 2v^i q^i  +  3r^^2v^2  -  r^     ^iv^j + ^jv^i         2 +2^iv^j^jv^i -v^j^jv^2 + v^2 2 -2v^i^iP^ +2P^v^2. (37)
                                                      2

Choosing q^i, Q^ accordingly, we find that as desired all components of the Einstein equations vanish for
  0:

                                                             Gr^a^, Ga^^b, Gr^r^ = O().                              (38)

7 Petrov type

Interestingly, this geometry is of an algebraically special type. We consider the case of p = 2 to connect
to the well-studied Petrov classification of spacetimes [37]). A geometry is Petrov type II if there exists
a real null vector k� such that the Weyl tensor satisfies

                                                                W�[k]k k = 0.                                        (39)

                                                                               10
This happens if the invariant I3 - 27J2 vanishes where I, J are both specific combinations of Weyl tensor
components which can be found in [37]. For the metric (14), the lowest nonzero entries for I, J are at
O( 4) and O( 6) respectively. Hence, the first contribution to the invariant would be at O( 12); however
the invariant vanishes through O( 13). At higher order in , it gets modified by corrections to (14); we
expect that including higher order terms in (14) enables (39) to be satisfied exactly.

8 Nonlinear solution in the near-horizon expansion

In section 4, the nonlinear Einstein equations with certain boundary conditions were solved in the non-
relativistic, long-wavelength hydrodynamic -expansion. This generalized the analysis given in [28] of
the -expansion for linearized modes. [28] also considered, for linearized modes, a second, near-horizon
expansion. Although physically inequivalent, the two expansions were found to be equivalent mathemat-
ically and reduce to the linearized dynamics of an incompressible fluid. In this section, we consider the
nonlinear version of the near-horizon expansion and find that it is again mathematically equivalent to
the nonlinear -expansion.

    In the -expansion one solves the shooting problem for long-wavelength perturbations of c with a
fixed leading-order extrinsic curvature. The proper acceleration of a worldline at fixed xi in c is to
leading order just proportional to K , so we may also view this as fixing the acceleration away from the
origin. In the near-horizon expansion, instead of expanding in the wavelength one expands in the inverse
acceleration. We begin with the flat metric on the Rindler wedge

                                        ds2p+2 = -rd 2 + 2d dr + dxidxi.                                                  (40)

To avoid confusion with the notation of the previous section we put the boundary on the accelerating

surface

                                                                r = r~c,                                                  (41)

so that r  r~c. The near-horizon, large acceleration, limit is r~c  0. In order to exhibit the r~c-dependence

explicitly  in  the     metric  we   transform  to  r = r~cr^,    =   ^    so   that  r1  and
                                                                      r~c

                                        ds2p+2      =   - r^ d^2  +   2d^dr^ +  dxidxi.                                   (42)
                                                          r~c

In these coordinates the near-horizon limit rescales to infinity the coefficient of d^2 at any finite r^.
    We now wish to consider perturbations of this metric solving the Einstein equations order by order

in the near-horizon expansion parameter r~c that are consistent with a flat induced metric at r^ = 1. At
the level of linear perturbations, the most general solution was found in [28] (characterized in terms of
the data at r = r~c). This solution is (for all r)

ds^2p+2  =  -   r^   d^2  +  2d^dr^  +  dxidxi  -  2(1  -  r^)vidxid^  +   r~c  (1 - r^2)2vidxid^ - 2vidxidr^  + O(r~c2)  (43)
                r~c

where ivi = 0 and ^vi - 2vi = 0. That is, vi is an incompressible fluid flow obeying the linearized
Navier-Stokes equation with unit kinematic viscosity.

    The nonlinear generalization of (43) which solves the nonlinear Einstein equations to O(r~c) is

ds^p2+2  =     r^  d^2
            -

              r~c

         + 2d^dr^ + dxidxi - 2(1 - r^)vidxid^ + (1 - r^)(v2 + 2P^)d^2

         + r~c (1 - r^)vivjdxidxj - 2vidxidr^ + (v2 + 2P^)d^dr^ + (1 - r^2)2vidxid^ - 2(1 - r^)q^i(^, r^, x)dxid^

         + r~c2 2gr(^2i)(^, r^, x)dxidr^ + gi(j2)(^, r^, x)dxidxj + O(r~c2)                                               (44)

                                                                  11
provided ivi = 0, ^vj - 2vj + vkkvj + jP^ = 0. q^i, gr(^2i), gi(j2) are solutions of first order differential
equations of the type (36) and (37). Further O(r~c2) pieces do not affect the equations of motion to this

order.

We can now see explicitly that making the notation change v  v^, xi  x^i and r~c   in (44)

gives us the rescaled solution (31) in section 6. Hence the near-horizon and hydrodynamic expansions

are mathematically equivalent.

                                                                                               2

Since we are identifying r~c =  = rc , rc   in the metric (14) is actually equivalent to the near-

horizon limit r~c  0 in (44). This may at first seem odd, but the near-horizon-hydrodynamic equivalence

involves  a  constant    rescaling     of  (14)  by  a   factor    of  1    ,  the  proper     distance  to  the  cutoff  surface  in  the
                                                                       rc2
                                                   1
rescaled  metric  (44)   indeed  behaves      as     rc  .

9 Acknowledgements

We are grateful to D. Christodoulou, S. Cremonini, T. Damour, B. Freivogel, S. Gubser, S. Hartnoll,
S. Kachru, R. Loganayagam, A. Maloney, S. Minwalla, D. Nelson, P. Petrov, S. Sachdev, O. Saremi, J.
Smoller, K. Thorne, E. Verlinde and S. T. Yau for illuminating conversations. This work was supported
by DOE grant DE-FG0291ER40654 and the Fundamental Laws Initiative at Harvard.

A Appendix

In the -expansion,

dsp2+2 = - rd 2 + 2d dr + dxidxi - 2                     r  vidxid             -  2 vi  dxidr
                                                   1-                              rc

                                                        rc

                     r       (v2 + 2P )d 2 + vivj dxidxj +                     v2 2P       d dr + c1 log     r    (ivj + j vi) dxidxj
          + 1-                                     rc                             +                          rc

                    rc                                                         rc rc

          -  (r2  -   rc2) 2vidxid     -   2        r       qidxid - 2c1 (r log r - rc log rc) 2vidxid                                 (45)
                  rc                          1-

                                                   rc

          - 2c1 log      r   vj (ivj + j vi) dxid + 2c1                      r          vjjvidxid + O( 4)
                         rc                                            1-

                                                                            rc

solves the Einstein equations through O( 3) if vi obeys the incompressible Navier-Stokes equation with
the "wrong" viscosity  = rc (1 + c1) where c1 is a nonzero constant. For this geometry, the square of
the Riemann tensor is

             R2       =      3   (ivj  -   j vi)2  +  c1    (c1 +  2)  2ivj j vi        +  1   (ivj  -  j vi)2    + O( 6)              (46)
                         - 2rc2                               r2                           2

which clearly diverges at r = 0 unless c1 vanishes or c1 = -2. The last possibility is the time reverse of
the first and exponentially growing in the future.

References

 [1] S. Bhattacharyya, S. Minwalla, and S. R. Wadia, "The Incompressible Non-Relativistic
      Navier-Stokes Equation from Gravity," JHEP 08 (2009) 059, arXiv:0810.1545 [hep-th].

 [2] Y. Oz and M. Rabinovich, "The Penrose Inequality and the Fluid/Gravity Correspondence,"
      arXiv:1011.5895 [hep-th].

 [3] T. Damour, "Quelques propri�et�es m�ecaniques, �electromagn�etiques, thermodynamiques et
      quantiques des trous noirs,". Th`ese de Doctorat d'Etat, Universit�e Pierre et Marie Curie, Paris VI,
      1979.

                                                                   12
 [4] T. Damour, "Surface effects in Black Hole Physics," Proceedings of the second Marcel Grossmann
      Meeting on General Relativity (1982) Ed. R. Ruffini, North Holland.

 [5] R. H. Price and K. S. Thorne, "Membrane viewpoint on black holes: properties and evolution of
      the stretched horizon," Phys. Rev. D33 (1986) 915�941.

 [6] T. Jacobson, "Thermodynamics of space-time: The Einstein equation of state," Phys. Rev. Lett.
      75 (1995) 1260�1263, arXiv:gr-qc/9504004.

 [7] R. Bousso, "A Covariant entropy conjecture," JHEP 9907 (1999) 004, arXiv:hep-th/9905177
      [hep-th].

 [8] G. Policastro, D. T. Son, and A. O. Starinets, "The shear viscosity of strongly coupled N = 4
      supersymmetric Yang-Mills plasma," Phys. Rev. Lett. 87 (2001) 081601, arXiv:hep-th/0104066.

 [9] G. Policastro, D. T. Son, and A. O. Starinets, "From AdS/CFT correspondence to
      hydrodynamics," JHEP 09 (2002) 043, arXiv:hep-th/0205052.

[10] P. Kovtun, D. T. Son, and A. O. Starinets, "Holography and hydrodynamics: Diffusion on
      stretched horizons," JHEP 10 (2003) 064, arXiv:hep-th/0309213.

[11] A. Karch, "Experimental tests of the holographic entropy bound," arXiv:hep-th/0311116.

[12] P. Kovtun, D. T. Son, and A. O. Starinets, "Viscosity in strongly interacting quantum field
      theories from black hole physics," Phys. Rev. Lett. 94 (2005) 111601, arXiv:hep-th/0405231.

[13] E. Gourgoulhon and J. L. Jaramillo, "A 3+1 perspective on null hypersurfaces and isolated
      horizons," Phys. Rept. 423 (2006) 159�294, arXiv:gr-qc/0503113.

[14] P. K. Kovtun and A. O. Starinets, "Quasinormal modes and holography," Phys. Rev. D72 (2005)
      086009, arXiv:hep-th/0506184.

[15] V. E. Hubeny, M. Rangamani, S. Minwalla, and M. Van Raamsdonk, "The fluid-gravity
      correspondence: The membrane at the end of the universe," Int. J. Mod. Phys. D17 (2009)
      2571�2576.

[16] S. Bhattacharyya, V. E. Hubeny, S. Minwalla, and M. Rangamani, "Nonlinear Fluid Dynamics
      from Gravity," JHEP 02 (2008) 045, arXiv:0712.2456 [hep-th].

[17] S. Bhattacharyya, R. Loganayagam, S. Minwalla, S. Nampuri, S. P. Trivedi, and S. R. Wadia,
      "Forced Fluid Dynamics from Gravity," JHEP 02 (2009) 018, arXiv:0806.0006 [hep-th].

[18] C. Eling, "Hydrodynamics of spacetime and vacuum viscosity," JHEP 11 (2008) 048,
      arXiv:0806.3165 [hep-th].

[19] S. Bhattacharyya, R. Loganayagam, I. Mandal, S. Minwalla, and A. Sharma, "Conformal
      Nonlinear Fluid Dynamics from Gravity in Arbitrary Dimensions," JHEP 12 (2008) 116,
      arXiv:0809.4272 [hep-th].

[20] I. Fouxon and Y. Oz, "Conformal Field Theory as Microscopic Dynamics of Incompressible Euler
      and Navier-Stokes Equations," Phys. Rev. Lett. 101 (2008) 261602, arXiv:0809.4512 [hep-th].

[21] R. K. Gupta and A. Mukhopadhyay, "On the universal hydrodynamics of strongly coupled CFTs
      with gravity duals," JHEP 03 (2009) 067, arXiv:0810.4851 [hep-th].

[22] I. Fouxon and Y. Oz, "CFT Hydrodynamics: Symmetries, Exact Solutions and Gravity," JHEP 03
      (2009) 120, arXiv:0812.1266 [hep-th].

                                                                   13
[23] C. Eling, I. Fouxon, and Y. Oz, "The Incompressible Navier-Stokes Equations From Membrane
      Dynamics," Phys. Lett. B680 (2009) 496�499, arXiv:0905.3638 [hep-th].

[24] C. Eling and Y. Oz, "Relativistic CFT Hydrodynamics from the Membrane Paradigm," JHEP 02
      (2010) 069, arXiv:0906.4999 [hep-th].

[25] M. F. Paulos, "Transport coefficients, membrane couplings and universality at extremality," JHEP
      02 (2010) 067, arXiv:0910.4602 [hep-th].

[26] T. Padmanabhan, "Thermodynamical Aspects of Gravity: New insights," Rept. Prog. Phys. 73
      (2010) 046901, arXiv:0911.5004 [gr-qc].

[27] C. Eling, I. Fouxon, and Y. Oz, "Gravity and a Geometrization of Turbulence: An Intriguing
      Correspondence," arXiv:1004.2632 [hep-th].

[28] I. Bredberg, C. Keeler, V. Lysov, and A. Strominger, "Wilsonian Approach to Fluid/Gravity
      Duality," arXiv:1006.1902 [hep-th].

[29] D. T. Son and A. O. Starinets, "Viscosity, Black Holes, and Quantum Field Theory," Ann. Rev.
      Nucl. Part. Sci. 57 (2007) 95�118, arXiv:0704.0240 [hep-th].

[30] T. Damour and M. Lilley, "String theory, gravity and experiment," arXiv:0802.4169 [hep-th].

[31] M. Rangamani, "Gravity and Hydrodynamics: Lectures on the fluid-gravity correspondence,"
      Class. Quant. Grav. 26 (2009) 224003, arXiv:0905.4352 [hep-th].

[32] V. E. Hubeny, "The Fluid/Gravity Correspondence: a new perspective on the Membrane
      Paradigm," arXiv:1011.4948 [gr-qc].

[33] S. W. Hawking and J. B. Hartle, "Energy and angular momentum flow into a black hole,"
      Commun. Math. Phys. 27 (1972) 283�290.

[34] J. B. Hartle, "Tidal Friction in Slowly Rotating Black Holes," Phys. Rev. D8 (1973) 1010�1024.

[35] J. B. Hartle, "Tidal shapes and shifts on rotating black holes," Phys. Rev. D9 (1974) 2749�2759.

[36] A. Petrov, Einstein Spaces. Pergamon Press, 1969.

[37] E. Hertl, C. Hoenselaers, D. Kramer, M. Maccallum, and H. Stephani, Exact solutions of Einstein's
      field equations. Cambridge Univ. Pr., 2003.

[38] R. Milson, A. Coley, V. Pravda, and A. Pravdova, "Alignment and algebraically special tensors in
      Lorentzian geometry," Int. J. Geom. Meth. Mod. Phys. 2 (2005) 41�61, arXiv:gr-qc/0401010.

[39] E. Gourgoulhon, "A generalized Damour-Navier-Stokes equation applied to trapping horizons,"
      Phys. Rev. D72 (2005) 104007, arXiv:gr-qc/0508003.

[40] K. S. Thorne, R. H. Price, and D. A. Macdonald, Black Holes: the Membrane Paradigm. New
      Haven, USA: Yale Univ. Pr., 1986.

[41] G. Policastro, D. T. Son, and A. O. Starinets, "From AdS/CFT correspondence to hydrodynamics.
      II: Sound waves," JHEP 12 (2002) 054, arXiv:hep-th/0210220.

[42] O. Saremi, "Shear waves, sound waves on a shimmering horizon," arXiv:hep-th/0703170.

[43] R. Baier, P. Romatschke, D. T. Son, A. O. Starinets, and M. A. Stephanov, "Relativistic viscous
      hydrodynamics, conformal invariance, and holography," JHEP 04 (2008) 100, arXiv:0712.2451
      [hep-th].

                                                                   14
[44] R. Brustein and A. J. M. Medved, "The ratio of shear viscosity to entropy density in generalized
      theories of gravity," Phys. Rev. D79 (2009) 021901, arXiv:0808.3498 [hep-th].

[45] M. Rangamani, S. F. Ross, D. T. Son, and E. G. Thompson, "Conformal non-relativistic
      hydrodynamics from gravity," JHEP 01 (2009) 075, arXiv:0811.2049 [hep-th].

[46] M. Mia, K. Dasgupta, C. Gale, and S. Jeon, "Five Easy Pieces: The Dynamics of Quarks in
      Strongly Coupled Plasmas," Nucl. Phys. B839 (2010) 187�293, arXiv:0902.1540 [hep-th].

[47] S. A. Hartnoll, "Lectures on holographic methods for condensed matter physics," Class. Quant.
      Grav. 26 (2009) 224002, arXiv:0903.3246 [hep-th].

[48] J. McGreevy, "Holographic duality with a view toward many-body physics," Adv. High Energy
      Phys. 2010 (2010) 723105, arXiv:0909.0518 [hep-th].

[49] S. Sachdev, "Condensed matter and AdS/CFT," arXiv:1002.2947 [hep-th].
[50] V. E. Hubeny and M. Rangamani, "A holographic view on physics out of equilibrium,"

      arXiv:1006.3675 [hep-th].
[51] T. Faulkner, H. Liu, and M. Rangamani, "Integrating out geometry: Holographic Wilsonian RG

      and the membrane paradigm," arXiv:1010.4036 [hep-th].
[52] A. O. Starinets, "Quasinormal spectrum and the black hole membrane paradigm," Phys. Lett.

      B670 (2009) 442�445, arXiv:0806.3797 [hep-th].
[53] N. Iqbal and H. Liu, "Universality of the hydrodynamic limit in AdS/CFT and the membrane

      paradigm," Phys. Rev. D79 (2009) 025023, arXiv:0809.3808 [hep-th].

                                                                   15
