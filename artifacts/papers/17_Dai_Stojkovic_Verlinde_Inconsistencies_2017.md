# Dai Stojkovic Verlinde Inconsistencies 2017

**Source:** `17_Dai_Stojkovic_Verlinde_Inconsistencies_2017.pdf`

---

arXiv:1710.00946v2 [gr-qc] 8 Nov 2017  Prepared for submission to JHEP

                                       Inconsistencies in Verlinde's emergent gravity

                                       De-Chang Daia Dejan Stojkovic b
                                       aInstitute of Natural Sciences,
                                         Shanghai Key Lab for Particle Physics and Cosmology,
                                         and Center for Astrophysics and Astronomy,
                                         Department of Physics and Astronomy,
                                         Shanghai Jiao Tong University,
                                         Shanghai 200240, China
                                        bHEPCOS, Department of Physics,
                                         SUNY at Buffalo,
                                         Buffalo, NY 14260-1500, USA
                                         E-mail: [email redacted], [email redacted]

                                       Abstract: We point out that recent Verlinde's proposal of emergent gravity suffers from
                                       some internal inconsistencies. The main idea in this proposal is to preserve general relativity
                                       at short scales where numerous tests verified its validity, but modify it on large scales where
                                       we meet puzzles raised by observations (in particular dark matter), by using some entropic
                                       concepts. We first point out that gravity as a conservative force is very difficult (if possible
                                       at all) to portray as an entropic force. We then show that the derivation of the MOND
                                       relation using the elastic strain idea is not self-consistent. When properly done, Verlinde's
                                       elaborate procedure recovers the standard Newtonian gravity instead of MOND.
Contents

1 Introduction                                      1

2 Gravity cannot be an entropic force               1

3 Inconsistency in derivation of the MOND relation  2

4 Conclusions                                       5

1 Introduction

The idea of emergent gravity, put forward in [1, 2], is an interesting attempt to attack the
longstanding problems in gravity and cosmology from a new perspective. As such, it is very
valuable since it is very unlikely that the problems we are facing will be resolved by some
straightforward extension of the existing models. Then in [3], an explicit Lagrangian cap-
turing some features of this proposal was proposed (see also [4] for important corrections).
The purpose of this note is, however, to point out that, as it stands now, the proposal
detailed in [1, 2] does not appear to be self-consistent.

2 Gravity cannot be an entropic force

We start with the first and most important premise of the entropic gravity proposal. The
main claim that relates entropy and gravitational force can be found around equation (3.7)
in the first Verlinde's paper [1].

     "The basic idea is to use the analogy with osmosis across a semi-permeable membrane.
When a particle has an entropic reason to be on one side of the membrane and the membrane
carries a temperature, it will experience an effective force equal to

                F x=T S                             (2.1)

This is the entropic force." [F is gravitational force, x is the displacement, T is the
temperature of the system, and S is the change in entropy.]

     This implies that the particle moves because the entropy of the system increases when
it moves. However, this very first premise cannot be true. Namely, Newtonian gravitational
force is conservative. An essential feature of conservative forces is that their action is always
reversible. A system in a free fall will never increase its entropy, because this is a reversible
process. We need some kind of dissipation (e.g. collisions) to increase entropy and make
it irreversible. In general relativity this is realized by emission of gravitons which increase
entropy. However, even in general relativity, it is possible to construct a freely falling

                �1�
(collapsing) system which does not radiate gravitons or any other radiation (for example a
spherically symmetric case). Therefore gravity cannot be interpreted as an entropic force.

     In fact, it is easy to see what is technically wrong with equation (3.7) in [1]. The right
hand side of that equation is work done by the gravity. The full expression should read

                              F x = T S + Ek                                                    (2.2)

where Ek is the change in the kinetic energy of this system. Thus, gravitational force can
perform work which results in the change of kinetic energy, while the entropy of the system
remains constant all the time. In [1], the author omitted Ek and concluded that gravity
was an entropic force.

     Thus, gravity cannot be an entropic force, at least as long as entropy is the usual
thermodynamical entropy as used in Eqs. (2.1) and (2.2).

3 Inconsistency in derivation of the MOND relation

Recently, the original proposal was extended and refined in a new paper [2]. The main goal

now is to solve the dark matter problem using the entropic gravity idea. In section 7.1

of [2], the author tries to prove that the surface mass density, D, for the apparent dark
matter in terms of the Newtonian potential for the baryonic matter, B, is (equation 7.37

in [2])

                              8G         2 d-2             i  B     ni                          (3.1)
                               a0 D        =                  a0
                                              d-1

where d is the number of dimensions in space, while ni is a normalized eigenvector satisfying
|n|2 = 1. The parameter a0 is an acceleration scale determined by the Hubble constant,

H0, and the speed of light, c, as a0 = cH0. If we take a point particle of mass M as an

example,  the  corresponding  Newtonian  potential     is  B  =     -   GM   .  From  equation  (3.1),  one
                                                                          r

finds the surface mass density for dark matter as

                                  D =           2M a0                                           (3.2)

                                                962G .
                                                 r

Since the surface mass density drops as 1/r, the total mass grows with distance as r, so this
behavior reproduces the MOdified Newtonian Dynamics (MOND), and can explain the flat
galactic rotational curves at large distances.

     However, to put the discussion in terms of the spacetime metric, the author introduces
the displacement field, ui, which is an analog of the gravitational potential, and the corre-
sponding elastic strain tensor, ij, which is an analog of the gravitational acceleration. The
displacement field is defined in equation 6.4 in [2] as

                                         ui  =  B   ni,                                         (3.3)
                                                a0

while the linear strain tensor is defined in equation 6.1 in [2] as

                                  =      1      iuj +      j ui ).                              (3.4)
                                          (
                              ij         2

                                             �2�
In the point particle case, the strain must be proportional to 1/r2, because it is just a

derivative of ui.
     In equation (7.28) in [2], the author writes down the relation between the apparent

dark matter surface density and the principal strain (r)

                                           D    =   a0       (r)               (3.5)
                                                   8G

where (r) is defined as

                                                     1                         (3.6)
                               (r)ni = ij - d - 1 kkij nj.

If the principal strain (r) has the same general behavior as the strain tensor ij, i.e. falls

off as 1/r2, then                                a0
                                                8G
                                     D     =              (r)  r-2.            (3.7)

This is very different from the desired form in equation (3.2). Since equations (3.2) and

(3.7) cannot be both right at the same time, the author goes through an elaborate construct

to justify his choices. Basically, he is trying to force (r) to drop as 1/r rather than 1/r2.

We will now go through the main steps, pointing out a major problem.

    The main observation that the author utilizes in [2] is that the presence of ordinary

matter in some subregion B of the de Sitter space removes the amount of entropy SM (B)

out of the total de Sitter entropy. The removed entropy is proportional to the displacement

ui as                                                  1

                                     SM (B) = V0             uidAi             (3.8)

                                                          B

where the integral goes over the area of the subregion B. Here V0 is a constant normalization

term. The author expects that a point mass removes entropy within radius r as

                                                          2M r                 (3.9)
                                           SM (r) = -

This is consistent with ui  1/r, and justifies equation (3.3). Next, the author proposes that
the removed entropy is not perfectly spherically distributed. Ordinary matter is located in
many smaller "inclusion regions" labeled VM (L). The displacement field now satisfies

                            iui = -V0/V0                  inside B  VM (L)     (3.10)
                                      0                   outside B  VM (L)

     Since these inclusion regions are randomly scattered in space (as in figure 1), the
displacement ui is not exactly the same as in equation (3.3). It must be corrected to

                                     ui    =  B   ni   +  (x, y,  z)           (3.11)
                                              a0

where (x, y, z) is the fluctuation caused by the non-uniform distribution of removed entropy

regions. If the fluctuations are random, then in large areas they cancel out on average, or

at  least  they  are  much  smaller  than  the  first  term,  B   ni,  i.e.
                                                              a0

                            |        (x, y, z) � dA|      |   B   ni   dAi|.   (3.12)
                                                              a0

                                                  �3�
Figure 1. The black solid circles are the inclusion regions, VM (L), where matter is present. Within
these regions entropy is removed, and the displacement satisfies iui = -V0/V0. Outside of these
regions entropy is not removed, and the displacement satisfies iui = 0.

In this context, averaging means integration. The random distribution of inclusion regions

also modifies the strain as                  H
                                     (r) = r2 + f (x, y, z)
                                                                                           (3.13)

where H is some constant which is not very important, while f (x, y, z) is the fluctuation in

the strain induced by the fluctuation in the displacement (x, y, z). We can now compute

the volume integral of (r)2 as

                        (r)2dV =  H2                  H                   f (x, y, z)2dV.  (3.14)
                                  r4 dV + 2           r2 f (x, y, z)dV +

The term          H2    dV  is the standard average behavior.    The term linear in f (x, y, z), i.e.
                  r4
H
r2  f  (x,  y  ,  z)dV  will be canceled out on average.         However, the term quadratic in fluctua-

tions, f (x, y, z)2dV , survives and corresponds to an additional contribution to the strain

from the random distribution of inclusion regions. The author expects that on average

                            (r)2dV = d - 2       uidAi      =    d-2      B   nidAi.       (3.15)
                                         d-1                              a0
                                              B                  d-1  B

In the last step, the fluctuation  in equation (3.11) is removed after averaging. Thus, from
equations (3.14) and (3.15) one gets

                            H2       f (x, y, z)2dV  d - 2                B   nidAi        (3.16)
                            r4 dV +                       d-1             a0
                                                                      B

As already mentioned, the term 2     H   f    (x,  y  ,  z  )dV  is removed because it is linear in fluctu-
                                     r2
            H2
ations.     r4    dV    is the regular term, which decays like r-1.   To obtain the correct right hand

                                                   �4�
side which is proportional to r, the extra contribution term f (x, y, z)2dV must grow like
r. This implies that the fluctuation f (x, y, z) falls off as 1/r. The singularity at r = 0 is
neglected, because point particle description will fail at some small finite radius. Using the
relation in equation (3.5), the author also rewrites equation (3.15) in terms of the surface
density (it is equation 7.36 in [2]) as

                              8G 2         d-2               B                                (3.17)
                              a0 D     dV =                  a0   ni  dAi.
                                               d-1
                           B                        B

One then applies Stokes theorem to obtain the crucial equation (3.1). This is how Verlinde

derives the MOND relation in section 7.1 of [2].

What is wrong with this procedure? The main technical point is that averaging was

applied to remove contribution from the fluctuation , or equivalently 2       H   f  (x,  y,  z)dV  in
                                                                              r2

equation (3.14). So again, after integration of equation (3.13) one gets

                              (r)2dV   H2           f (x, y, z)2dV.                           (3.18)
                                       r4 dV +

This is all that one can conclude at this point. By equating the terms under the integral,

one can naively find that

                              (r)      H2  +      f (x, y,  z)2.                              (3.19)
                                       r4

Since f (x, y, z) falls off as 1/r, at large distances the strain and thus the surface density

D (because of equation (3.5)) falls off as 1/r, exactly as needed for MOND. However, this
is incorrect. The cross term in equation (3.14) is gone only after the integration because

of the averaging, so one cannot go back and extract (r) this way. For the same reason

equation (3.15) cannot be applied to recover (r), because  is removed by averaging.

To avoid this mistake, one has to go back to equation (3.13). On average, the surface

density is

                     1         a0 (r)dA =                                                     (3.20)
            D = A             8G
            1 a0
            A 8G              H                           1  a0       H
                              r2 + f (x, y, z)    dA                  r2 dA,
                                                            A 8G

where A is the area over which one integrates. The linear term f (x, y, z)dA is again
suppressed. The final result is that the surface density falls off as 1/r2, not as desired
1/r. This is the same behavior as in Newtonian gravity, not MOND. Therefore, the crucial
MOND relation written in equation (3.1) cannot be self-consistently derived in this way.

4 Conclusions

In this paper we pointed out two major problems that plague Verlinde's proposal of emergent
gravity. While the proposal contains some attractive features, a self-consistent formulation
(if possible at all) requires addressing the problems we outlined here. The first problem is

                                       �5�
that the equation (2.1) on which the entropic reasoning is based in incomplete, and instead
equation (2.2) should be used. Then it will become clear that gravity as a conservative
force cannot have an entropic origin. The second problem appears when an attempt was
made to derive the MOND relation in equation (3.1). The averaging procedure was not
applied appropriately, and instead of the regular mean the root mean square was used. We
showed that when the averaging is properly done, the contribution from the strain behaves
like ordinary Newton's gravity instead of MOND.

     Entropic reasoning from the section 2 was also criticized in [5], where Eq. (2.1) was gen-
eralized to multiple heat baths with multiple temperatures and multiple entropies. However,
a more complete Eq. (2.2) was not discussed in [5].

     It is also instructive to note that our discussion from the section 2 does not apply
(at least not in a straightforward way) to different approaches that can be found in the
literature. For example, it was argued in [6, 7] that a thermodynamic interpretation of the
relativistic Einstein equations might be possible (as opposed to the Newtonian force like
in Verlinde's proposal). However, neither of these proposals is explicitly using the form
of Eq. (2.1). In particular, in [6], to argue that the Einstein equations are an analog of a
thermodynamical equation of state, the relation Q = T dS was used, which is technically
correct, while Eq. (2.1) is incomplete. In [7], the author gives an interpretation that the
Einstein's gravitational action represents the free energy of the spacetime geometry. Since
this interpretation does not involve any incomplete thermodynamical relations, our criticism
does not apply to it.

     Our discussion from the section 3 does not apply to earlier approaches in [6, 7] since it
crucially depends on the elaborate procedure in [2]. For some recent approaches to emergent
spacetime see also [8�10].

Acknowledgments

D.C Dai was supported by the National Science Foundation of China (Grant No. 11433001
and 11447601), National Basic Research Program of China (973 Program 2015CB857001),
the key laboratory grant from the Office of Science and Technology in Shanghai Munici-
pal Government (No. 11DZ2260700) and the Program of Shanghai Academic/Technology
Research Leader under Grant No. 16XD1401600. D.S. was partially supported by the US
National Science Foundation, under Grant No. PHY-1417317.

References

 [1] E. P. Verlinde, JHEP 1104, 029 (2011) doi:10.1007/JHEP04(2011)029 [arXiv:1001.0785
      [hep-th]].

 [2] E. P. Verlinde, SciPost Phys. 2, 016 (2017) doi:10.21468/SciPostPhys.2.3.016
      [arXiv:1611.02269 [hep-th]].

 [3] S. Hossenfelder, Phys. Rev. D 95, no. 12, 124018 (2017) doi:10.1103/PhysRevD.95.124018
      [arXiv:1703.01415 [gr-qc]].

 [4] D. C. Dai and D. Stojkovic, arXiv:1706.07854 [gr-qc].

                                                        �6�
 [5] M. Visser, JHEP 1110, 140 (2011) doi:10.1007/JHEP10(2011)140 [arXiv:1108.5240 [hep-th]].
 [6] T. Jacobson, Phys. Rev. Lett. 75, 1260 (1995) doi:10.1103/PhysRevLett.75.1260

      [gr-qc/9504004].
 [7] T. Padmanabhan, Astrophys. Space Sci. 285, 407 (2003) doi:10.1023/A:1025448712533

      [gr-qc/0209088].
 [8] N. Afshordi and D. Stojkovic, Phys. Lett. B 739, 117 (2014)

      doi:10.1016/j.physletb.2014.10.048 [arXiv:1405.3297 [hep-th]].
 [9] D. Edmonds, D. Farrah, D. Minic, Y. J. Ng and T. Takeuchi, arXiv:1709.04388

      [astro-ph.CO].
[10] M. Cadoni, R. Casadio, A. Giusti, W. Mueck and M. Tuveri, arXiv:1707.09945 [gr-qc].

                                                       �7�
