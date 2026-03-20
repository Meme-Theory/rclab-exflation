# DAMTP Extra Dimensions 2015

**Source:** `03_DAMTP_Extra_Dimensions_2015.pdf`

---

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.     2015 Part III Lectures on Extra
                                                                                                                Dimensions

                                                                                                                                         Fernando Quevedo
                                                                                              (Second part of the course Supersymmetry and Extra Dimensions with Ben Allanach)
Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.

                                                                                              2
                                                                                              Contents

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  1 Extra dimensions                          5

                                                                                              1.1 Basics of Higher Dimensional Theories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

                                                                                              1.1.1 Why Consider D  4 Dimensions? . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

                                                                                              1.1.2 Brief History . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

                                                                                              1.2 Bosonic Field theories in extra dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

                                                                                              1.2.1 Scalar field in 5 dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

                                                                                              1.2.2 Vector fields in 5 dimensions and higher . . . . . . . . . . . . . . . . . . . . . . . . 8

                                                                                              1.2.3 Antisymmetric tensor fields, Duality and p-branes . . . . . . . . . . . . . . . . . . 10

                                                                                              1.2.4 Gravitation in extra dimensions: Kaluza Klein theory . . . . . . . . . . . . . . . . 12

                                                                                              1.3 The brane world scenario . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

                                                                                              1.3.1 Large extra dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

                                                                                              1.3.2 Warped compactifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

                                                                                              1.3.3 Brane world scenarios and the hierarchy problem . . . . . . . . . . . . . . . . . . . 19

                                                                                              2 Supersymmetry in higher dimensions        21

                                                                                              2.1 Spinors in higher dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

                                                                                              2.1.1 Spinor representations in even dimensions D = 2n . . . . . . . . . . . . . . . . . . 21

                                                                                              2.1.2 Spinor representations in odd dimensions D = 2n + 1 . . . . . . . . . . . . . . . . 22

                                                                                              2.1.3 Majorana spinors (extra material not covered in lectures) . . . . . . . . . . . . . . 23

                                                                                              2.2 Supersymmetry algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

                                                                                              2.2.1 Representations of supersymmetry algebra in higher dimensions . . . . . . . . . . . 24

                                                                                              2.2.2 Supersymmetry Algebra and p-Branes . . . . . . . . . . . . . . . . . . . . . . . . . 26

                                                                                              2.3 Dimensional Reduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

                                                                                              3 A brief overview of compactifications     29

                                                                                              3.1 Toroidal Compactifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

                                                                                              3.2 Freund-Rubin Compactifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

                                                                                              3.3 Calabi-Yau Compactifications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

                                                                                              3.4 Final Remarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

                                                                                                                                       3
Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.

                                                                                              4

                                                                                              CONTENTS
                                                                                              Chapter 1

                                                                                              Extra dimensions

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  1.1 Basics of Higher Dimensional Theories

                                                                                              1.1.1 Why Consider D  4 Dimensions?

                                                                                              � One argument against D  4 . The gravitational force between two bodies F  1/R2 (potential
                                                                                                   1/R) for distance between bodies R in 4-dimensions and in general dimension D, F  1/RD-2
                                                                                                 (  1/RD-3). Only potentials   1/R have stable orbits. So only in 4D there can be stable
                                                                                                 planetary systems. Exercise: Prove it.

                                                                                              � However. Experimentally we observe D = 4. But we know this only puts a bound on the size of
                                                                                                 the extra dimensions. Extra time dimensions are complicated (usually imply closed time-like curves
                                                                                                 affecting causaliy) but there may be as many extra space-like dimensions as long as they are small
                                                                                                 enough not to have been observed (r 10-18m for nongravitational physics and r 10-6m for
                                                                                                 gravity).

                                                                                              Gauss' law implies for the electric field E and its potential  of a point charge Q:

                                                                                                  E � dS = Q =                    E         1     ,         1          4 dimensions
                                                                                                                                           R2               R          5 dimensions
                                                                                              S2
                                                                                                                                  E         1     ,          1
                                                                                                  E � dS = Q =                             R3               R2

                                                                                              S3

                                                                                              So in D spacetime dimensions

                                                                                                                            E           1   ,               1    .
                                                                                                                                     RD-2                RD-3

                                                                                              If one dimension is compactified (radius r) like in M4 � S1, then

                                                                                                                                               1     : R<r
                                                                                                                                                     : Rr
                                                                                                                                            R13
                                                                                                                               E            R2              .


                                                                                              Analogues arguments hold for gravitational fields and their potentials.

                                                                                              � Another argument against D  4. Only in 4 dimensions gauge couplings are dimensionless S =
                                                                                                 -1/g2 dDxFMN F MN + � � � . Since [AM ] = 1, [FMN ] = 2, so [g] = (4 - D)/2. So properly

                                                                                                                                         5
                                                                                              6                                          CHAPTER 1. EXTRA DIMENSIONS

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.        defined quantum field theories of gauge fields exist only in 4 dimensions (gauge field theories in
                                                                                                    D  4 are non-renormalisable). However knowing that gravity is non-renormalisable already in four
                                                                                                    dimensions, a theory including both gravity and gauge interactions is already non renormalisable.

                                                                                                 � Another curiosity. Gravity is `non-trivial' for D  4 (in the sense that the graviton field has no
                                                                                                    propagating degrees of freedom in lower dimensions).

                                                                                                 � Enhancing spacetime symmetries. It is important to look for alternative ways to address the prob-
                                                                                                    lems that supersymmetry solves and also to address other trouble spots of the Standard Model.
                                                                                                    We mentioned in the first lecture that supersymmetry and extra dimensions are the natural exten-
                                                                                                    sions of spacetime symmetries that may play an important role in our understanding of nature and
                                                                                                    addressing the problems of the Standard Model.

                                                                                                 � Technical simplifications. Often supersymmetric theories in 4D are easier to define starting from
                                                                                                    D  4.

                                                                                                 � Potential part of fundamental theories?. String/M-theory consistent in D = 10, 11.

                                                                                                 � Maybe best argument. Why not? After all the best way to address the question of why we observe
                                                                                                    4-dimensions is to study physics in arbitrary number of dimensions.

                                                                                                 Here we will start the discussion of physics in extra dimensions.

                                                                                              1.1.2 Brief History

                                                                                                  �  150 AD Ptolemy "On dimensionality"

                                                                                                 � 19th century Cayley, Mo�bius, Riemann N -dimensional geometry, ...

                                                                                                 � In 1914 Nordstrom and 1919 - 1921 Kaluza independently tried to unify gravity and electro-
                                                                                                    magnetism. Nordstrom was attempting an unsuccessful theory of gravity in terms of scalar fields,
                                                                                                    prior to Einstein. Kaluza used general relativity extended to five dimensions. His concepts were
                                                                                                    based on Weyl's ideas.

                                                                                                 � 1926 Klein: cylindric universe with 5th dimension of small radius R

                                                                                                 � After 1926, several people developed the KK ideas (Einstein, Jordan, Pauli, Ehrenfest,...)

                                                                                                 � 1960's: de Witt obtaining 4 dimensional Yang Mills theories in 4d from D > 5. Also strings with
                                                                                                    D = 26.

                                                                                                 � In 1970's and 1980's: Superstrings required D = 10. Developments in supergravity required extra

                                                                                                 dimensions and possible maximum numbers of dimensions for SUSY were discussed: D = 11 turned

                                                                                                 out to be the maximum number of dimensions (Nahm). Witten examined the coset

                                                                                                 G/H  =  SU (3) � SU (2) � U (1)
                                                                                                          SU (2) � U (1) � U (1)

                                                                                                 dim(G/H) = (8 + 3 + 1) - (3 + 1 + 1) = 7

                                                                                                 which also implied D = 11 to be the minimum. 11 dimensions, however, do not admit chirality
                                                                                                 since in odd dimensions, there is no analogue of the 5 matrix in four dimensions.
                                                                                              1.2. BOSONIC FIELD THEORIES IN EXTRA DIMENSIONS                                              7

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Figure 1.1: Example of a five dimensional spacetime M 4 � S1 where S1 is a circular extra dimension in addition to four

                                                                                              dimensional M 4.

                                                                                                  � 1990's-2000's: Superstrings revived D = 11 (M theory). Brane world scenario (large extra dimen-
                                                                                                     sions). AdSD/CF TD-1 dualities...

                                                                                              Exercise: Consider the Schr�odinger equation for a particle moving in two dimensions x and y. The
                                                                                              second dimension is a circle or radius r. The potential corresponds to a square well (V (x) = 0 for
                                                                                              x  (0, a) and V =  otherwise). Derive the energy levels for the two-dimensional Schr�odinger equation
                                                                                              and compare the result with the standard one-dimensional situation in the limit r  a.

                                                                                              1.2 Bosonic Field theories in extra dimensions

                                                                                              1.2.1 Scalar field in 5 dimensions

                                                                                              Before discussing higher dimensional gravity, we will start with the simpler cases of scalar fields in extra
                                                                                              dimensions, followed by vector fields and other bosonic fields of helicity   1. This will illustrate the
                                                                                              effects of having extra dimensions in simple terms. We will be building up on the level of complexity to
                                                                                              reach gravitational theories in five and higher dimensions. In the next chapter we extend the discussion
                                                                                              to include fermionic fields.
                                                                                              Consider a massless 5D scalar field (xM ) , M = 0, 1, ..., 4 with action

                                                                                                                          S5D =     d5x M  M  .

                                                                                              Set the extra dimension x4 = y defining a circle of radius r with y  y + 2r.

                                                                                              Our spacetime is now M4 � S1. Periodicity in y direction implies discrete Fourier expansion

                                                                                                                                                  iny
                                                                                                                                                   r
                                                                                                                       (x�, y) =       n(x�) exp       .

                                                                                                                                  n=-

                                                                                              Notice that the Fourier coefficients are functions of the standard 4D coordinates and therefore are (an

                                                                                              infinite number of) 4D scalar fields. The equations of motion for the Fourier modes are (in general

                                                                                              massive) wave equations

                                                                                              M M  = 0                 =          ��   -  n2  n(x�) exp   iny               =0
                                                                                                                          n=-             r2               r
                                                                                              8                                                                              CHAPTER 1. EXTRA DIMENSIONS

                                                                                                                                =        ��n(x�)            -  n2     n(x�)    =       0.
                                                                                                                                                               r2

                                                                                              These are then an infinite number of Klein Gordon equations for massive 4D fields. This means that

                                                                                              each  Fourier  mode  n   is  a  4D  particle   with  mass  m2n   =  n2  .  Only  the  zero   mode  (n  =  0)   is  massless.   One
                                                                                                                                                                  r2

                                                                                              can visualize the states as an infinite tower of massive states (with increasing mass proportional to n).

                                                                                              This is called Kaluza Klein tower and the massive states (n = 0) are called Kaluza Klein- or momentum

                                                                                              states, since they come from the momentum in the extra dimension:

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Figure 1.2: The Kaluza Klein tower of massive states due to an extra S1 dimension. Masses mn = |n|/r grow linearly

                                                                                              with the fifth dimension's wave number n  Z.

                                                                                              In order to obtain the effective action in 4D for all these particles, let us plug the mode expansion of 

                                                                                              into the original 5D action,

                                                                                                    S5D =              d4x dy M M  =                                     �n(x�) �n(x�)               -  n2   |n  |2
                                                                                                                                                                                                        r2
                                                                                                                                                         d4x

                                                                                                                                                            n=-

                                                                                                             = 2  r d4x �0(x�) �0(x�) + ... = S4D + ... .

                                                                                              This means that the 5D action reduces to one 4D action for a massless scalar field plus an infinite sum

                                                                                              of  massive  scalar  actions  in  4D.  If  we  are   only  interested      in  energies  smaller  than    the  1   scale,  we  may
                                                                                                                                                                                                             r

                                                                                              concentrate only on the 0 mode action. If we restrict our attention to the zero mode (like Kaluza

                                                                                              did), then (xM ) = (x�). This would be equivalent to just truncating all the massive fields. In this

                                                                                              case speak of dimensional reduction. More generally, if we keep all the massive modes we talk about

                                                                                              compactification, meaning that the extra dimension is compact and its existence is taken into account as

                                                                                              long as the Fourier modes are included.

                                                                                              1.2.2 Vector fields in 5 dimensions and higher

                                                                                              Let us now move to the next simpler case of an abelian vector field in 5D, similar to an electromagnetic

                                                                                              field in 4D. We can split a massless vector field AM (xM ) into


                                                                                                                              AM =  A�                   (vector in 4 dimensions)
                                                                                                                                                                                            .
                                                                                                                                          A4 =:  (scalar in 4 dimensions)

                                                                                              Each component has a discrete Fourier expansion

                                                                                                                   A�  =                           iny   ,               =                      iny     .
                                                                                                                                                    r                                            r
                                                                                                                                        A�n exp                                      n exp

                                                                                                                                n=-                                          n=-
                                                                                              1.2. BOSONIC FIELD THEORIES IN EXTRA DIMENSIONS                                             9

                                                                                              Consider the action          S5D =              d5x   1    FMN F MN
                                                                                              with field strength                                  g52D
                                                                                              implying
                                                                                              Choose a gauge, e.g. Lorenz  FMN := M AN - N AM

                                                                                                                           M M AN - M N AM = 0 .

                                                                                                                           M AM = 0 = M M AN = 0 ,

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  then this obviously becomes equivalent to the scalar field case (for each component AM ) indicating an
                                                                                              infinite tower of massive states for each massless state in 5D. In order to find the 4D effective action we
                                                                                              once again plug this into the 5D action:

                                                                                              S5D  S4D =                   d4x    2r          F(0) �  F(0)�  +  2r    �0 �0  +  ...  ,
                                                                                                                                  g52D                          g52D

                                                                                              Therefore we end up with a 4D theory of a gauge particle (massless), a massless scalar and infinite towers

                                                                                              of massive vector and scalar fields. Notice that the gauge couplings of 4- and 5 dimensional actions
                                                                                              (coefficients of FMN F MN and F� F � ) are related by

                                                                                                                                  1           =    2r    .
                                                                                                                                  g42              g52

                                                                                              In D spacetime dimensions, this generalises to

                                                                                                                                  1           =    VD-4
                                                                                                                                  g42               gD2

                                                                                              where Vn is the volume of the n dimensional compact space (e.g. an n sphere of radius r). Higher
                                                                                              dimensional electromagnetic fields have further interesting issues that we pass to discuss.

                                                                                              Comments on spin and degree of freedom counting

                                                                                              We know that a gauge particle in 4 dimensions has spin one and carries two degrees of freedom. We may
                                                                                              ask about the generalization of these results to a higher dimensional gauge field.
                                                                                              Recall Lorentz algebra in 4 dimension

                                                                                              M � , M  = i � M  +  M � -  M � - � M 

                                                                                                                           Ji = ijk Mjk ,                J  M23 .

                                                                                              For finite dimensional massless representations in D dimensions, O(D - 2) is little group:

                                                                                                                                                P � = (E, E , 0 , ... , 0)

                                                                                                                                                                                                         O(D-2)

                                                                                              The Lorentz algebra is just like in 4 dimensions, replace �, , ... by M , N , ..., so M23 commutes with
                                                                                              M45 and M67 for example. Define the spin to be the maximum eigenvalue of any M i(i+1). The number
                                                                                              of degrees of freedom in 4 dimensions is 2 (A�  Ai with i = 2, 3) corresponding to the 2 photon
                                                                                              polarizations and (D - 2) in D dimension, AM  Ai where i = 1, 2, ..., D - 2.
                                                                                              10                                                            CHAPTER 1. EXTRA DIMENSIONS

                                                                                              1.2.3 Antisymmetric tensor fields, Duality and p-branes

                                                                                              So far we considered scalar- and vector fields:

                                                                                                  D=4  scalar                                   vector      index - range
                                                                                                  D>4  (x�)                                     A�(x�)       � = 0, 1, 2, 3
                                                                                                       (xM )                                   AM (xM )  M = 0, 1, ..., D - 1

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  We will see now that in extra dimensions there are further fields corresponding to bosonic particles of
                                                                                              helicity   1. These are antisymmetric tensor fields, which in 4D are just equivalent to scalars or vector
                                                                                              fields by a symmetry known as duality. But in extra dimensions these will be new types of particles (that
                                                                                              play an important role in string theory for instance).
                                                                                              Consider for example

                                                                                                  � Massless antisymmetric tensor B� in D = 4 with field strength H�[�B] with action S =
                                                                                                     1/g2 d4xH�H�

                                                                                                                                H� = [�B] = F~ = � H� = a

                                                                                                  The action S can be shown to be equivalent to S  g2 d4x �a�a (see example sheet). Therefore
                                                                                                  a two-index massless antisymmetric tensor B� is said to be dual to a massless scalar a.

                                                                                                  � In 4 dimensions, define a dual field strength to the Faraday tensor F � via

                                                                                                            F~�                                :=  1     �  F  ,
                                                                                                                                                   2

                                                                                                  then Maxwell's equations in vacuo read:

                                                                                                  �F� = 0                                                      (field equations)
                                                                                                  �F~� = 0                                                  (Bianchi identities)

                                                                                                  The exchange F  F~ (the electromagnetic duality) corresponding to E  B swaps field equations
                                                                                                  and Bianchi identities.

                                                                                                  Similarly in 5 dimensions, one could define in analogy

                                                                                                       F~MNP = MNP QR FQR .

                                                                                                  � D=6
                                                                                                     So far in D = 4, 5 antisymmetric tensors of higher rank have been shown to be equivalent (dual) to
                                                                                                     known objects such as scalars and electromagnetic fields. However in D = 6 and higher they can
                                                                                                     be seen to be a new kind of physical fields.

                                                                                                                    FMNP = [M BNP ] = F~QRS = MNP QRS F MNP = [QB~RS]
                                                                                                     Here the potentials BNP  B~RS are of the same type. Contrary to the D = 4, 5 cases these are
                                                                                                     NEW objects that are not dual to scalaras or vectors.

                                                                                                  One can generally start with an antisymmetric (p + 1) - tensor BM1...Mp+1 and derive a field strength

                                                                                                                                            HM1...Mp+2 = [M1 AM2...Mp+2]
                                                                                              1.2. BOSONIC FIELD THEORIES IN EXTRA DIMENSIONS                                           11

                                                                                              and its dual (with D - (p + 2) indices)

                                                                                                                    H~ M1...MD-p-2 =  H . M1...MD MD-p-1...MD

                                                                                              Note that under duality, couplings g are mapped to (multiples of) their inverses,

                                                                                                              L  =  1   ([M1 BM2...Mp+2])2         g2  ([M1     B~ )2                .
                                                                                                                    g2
                                                                                                                                                                   M2 ...MD-(p+2) ]

                                                                                              In these simple cases the g2 factors can in principle be absorbed in the redefinition of the fields but for

                                                                                              more general cases, such as supersymmetric Yang-Mills theories (or discrete cases like the Ising model)

                                                                                              the duality actually maps strong coupling to weak couplings [3].

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Exercise: Consider the following Lagrangian

                                                                                                                 S=       d4x          1   H� H �  +   a � �H      .
                                                                                                                                       g2

                                                                                              Solve the equation of motion for the Lagrange multiplier a to obtain an action for a propagating massless

                                                                                              Kalb-Ramond field B�. Alternatively, solve the equation of motion for the field H, to obtain an action
                                                                                              for the propagating axion field a. What happens to the coupling g under this transformation?

                                                                                              The procedure mentioned in the previous exercise can be generalised to any system that has a global

                                                                                              symmetry. That is a sufficient condition for the existence of a dual theory is the existence of a global

                                                                                              symmetry. The steps to dualisation are then: 1. Gauge the global symmetry by introducing a gauge

                                                                                              field, 2. Introduce a Lagrange multplier constrain that sets the corresponding field strength to zero,

                                                                                              3. Change the order of integration to obtain the dual theory after fixing an appropriate gauge. For

                                                                                              instance let us take the simplest case: a tensor of rank 0 (scalar) in 2-dimensions. The action S =

                                                                                              R2 d2�X�X, the global symmetry is X  X + c. Gauging it means we change �X  D�X =
                                                                                              �X + A�. Then we set the field strength to zero by adding a Lagrange multiplier constraint to the

                                                                                              action: S = d2 (D�XD�X + � F� ) integrating over  sets F� = �A -  A� = 0 then the
                                                                                              gauge field is a pure gauge and can set the gauge choice A� = 0 and then get back the original action.

                                                                                              But instead of integrating over  we integrate by parts the Lagrange multiplier term and solve for A�
                                                                                              and fix the gauge X = 0 leads to the dual action S~ = (2R)-2 d2��. This is the case for the
                                                                                              worldsheet of string theory with one of the coordinates X living on a circle of radius R. This duality

                                                                                              maps large radius to small radius R  1/2R and is called T - duality. For the general antisymmetric

                                                                                              tensor BM1���Mq the global symmetry is BM1���Mq  BM1���Mq + cM1���Mq and the gauge field would be a
                                                                                              q + 1 rank tensor. All the steps are the same as above. Notice that the path integrals are gaussian and

                                                                                              so solving the equations of motion are the same as integrating out.

                                                                                              Antisymmetric tensors carry spin 1 or less, e.g. in 6 dimensions:


                                                                                                                         B�                : rank two tensor in 4 dimensions

                                                                                                              BMN =       B�5 , B�6         : 2 vectors in 4 dimensions
                                                                                                                         B56                    : scalar in 4 dimensions

                                                                                              To see the number of degrees of freedom, consider the little group and count the number of components
                                                                                              in the transverse dimensions

                                                                                                                 BM1...Mp+1  Bi1...ip+1 ,          ik = 1, ..., (D - 2) .

                                                                                              These are  D-2  independent components.
                                                                                                         p+1
                                                                                              12                                                                 CHAPTER 1. EXTRA DIMENSIONS

                                                                                              p branes

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Antisymmetric tensors of different ranks introduce new kinds of extended objects known as p branes
                                                                                              which are extended objects with p spatial dimensions spanning a p + 1 dimensional worldvolume while
                                                                                              they move in D > p + 1 dimensions.

                                                                                                  Let us recall the situation with point particles in D = 4. Electromagnetic fields couple to the worldline
                                                                                              of particles via

                                                                                                                                                      S  A� dx� ,

                                                                                              This can be seen as follows: the electromagnetic field couples to a conserved current in 4 dimensions as
                                                                                                d4xA�J� (with Dirac current J� = �� for an electron field for instance). For a particle of charge q,

                                                                                              the current can be written as an integral over the world line of the particle J� = q d�4(x - ) such
                                                                                              that J 0d3x = q and so the coupling becomes d4xJ �A� = q d�A�.
                                                                                              We can extend this idea for higher dimensional theories with higher rank tensors. For a potential B[MN]
                                                                                              with two indices, the analogue is

                                                                                                                                                        BMN dxM  dxN ,

                                                                                              i.e. need a string (or 1-brane) with 2 dimensional worldsheet to couple. Further generalisations are

                                                                                                          BMNP dxM  dxN  dxP                                     (membrane or 2-brane)
                                                                                                          BM1...Mp+1 dxM1  ...  dxMp+1                                             (p brane)

                                                                                              Therefore we can see that antisymmetric tensors of higher rank couple naturally to extended objects.
                                                                                              This leads to the concept of a p brane as a generalisation of a particle that couples to antisymmetric
                                                                                              tensors of rank p + 1.

                                                                                                  A particle carries charge under a vector field, such as electromagnetism Q = d3xJ0 with J� the
                                                                                              conserved current. In the same sense, p branes carry a new kind of charge with respect to a higher
                                                                                              rank antisymmetric tensor Zi1...ip = dD-1x J 0i1...ip . In the same way that in D = 4 there are dual
                                                                                              objects corresponding to point-like magnetic monopoles, in arbitrary dimensions D the dual objects are
                                                                                              (magnetic) D - p - 4 branes that couple to the dual fields B~M1...MD-p-3 .

                                                                                              1.2.4 Gravitation in extra dimensions: Kaluza Klein theory

                                                                                              After discussing scalar-, vector- and antisymmetric tensor fields

                                                                                                                                       scalar           spin     deg. of freedom
                                                                                                                                     vector AM            0            1+1
                                                                                                                       antisymmetric tensor AM1...Mp+1                 D-2
                                                                                                                                                        0, 1
                                                                                                                                                        0, 1                D-2
                                                                                                                                                                            p+1

                                                                                              we are now ready to consider the graviton GMN of Kaluza Klein theory. Let us start again with D = 5

                                                                                              dimensions                      

                                                                                                                               G� graviton

                                                                                                                       GMN =            G�4 vectors
                                                                                                                               G44 scalar

                                                                                              where �,  = 0, 1, 2, 3.
                                                                                              1.2. BOSONIC FIELD THEORIES IN EXTRA DIMENSIONS                                                                         13

                                                                                              The background metric appears in the 5 dimensional Einstein Hilbert action and field equations

                                                                                                                           S = -M3 d5x |G| (5)R ,                       (5)RMN = 0 .

                                                                                              Here M is the fundamental mass scale of the high dimensional theory (not to be confused with the
                                                                                              four-dimensional Planck mass!). One possible solution is the 5 dimensional Minkowski metric GMN =
                                                                                              MN = (+, -, -, -, -), another one is that of 4 dimensional Minkowski spacetime M4 times a circle S1,
                                                                                              i.e. the metric is of the M4 � S1 type

                                                                                                                                         ds2 = W (y) � dx� dx - dy2

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  where M3 � S1 � S1 is equally valid. In this setting, W (y) is a warp factor that is allowed by the
                                                                                              symmetries of the background and y is restricted to the interval [0, 2r]. For simplicity we will set the
                                                                                              warp factor to a constant but will consider it later where it will play an important role.

                                                                                              Consider the physical excitations to the background metric


                                                                                                                           GM N       =  -     1      g� - 2  A� A              -  A�
                                                                                                                                               3                                            

                                                                                                                                                              -  A                 -

                                                                                              where  is a constant to be fixed. Performing the Fourier expansion


                                                                                                                g� =             g�n einy/r ,       A� =         A�neiny/r ,          = neiny/r

                                                                                                                         -                                 -                                 -

                                                                                              we can write


                                                                                                                                                                 - (0) A�(0)  +  tower of massive modes
                                                                                                    GM N     =  (0)-  1       g�(0) - 2 (0) A�(0) A(0)
                                                                                                                      3              - (0) A(0)                      -(0)

                                                                                                                                         Kaluza Klein ansatz

                                                                                              and plug the zero mode part into the Einstein Hilbert action:

                                                                                                       S4D = -           d4x     |g|     Mp2l (4)R +  1  (0)     F�(0)  F (0)�  +    Mp2l �(0) �(0)       + ...
                                                                                                                                                      4
                                                                                                                                                                                     6      ((0))2

                                                                                              Where in order to absorb the constant in the Maxwell term we have set -1 = Mpl = hc/G the
                                                                                              4-dimensional Planck scale. Notice we have obtained a unified theory of gravity, electromagnetism and
                                                                                              scalar fields!

                                                                                              Exercise: Show that the last equation follows from a pure gravitational theory in five-dimensions, using

                                                                                              (5)R  =  (4)R  -  2e- 2 e  -    1  e2 F�   F  �  where  G55     =  e2 .  Relate   the  gauge  coupling  to  the  U (1)  isometry
                                                                                                                              4

                                                                                              of the compact space.

                                                                                              Comment

                                                                                              The Planck mass Mp2l = M3 � 2r is a derived quantity. We know experimentally that Mpl  1019 GeV,
                                                                                              therefore we can adjust M and r to give the right result. But there is no other constraint to fix M and
                                                                                              r. So at this level M can only be determined after the radius of the circle is fixed.
                                                                                              14                                                             CHAPTER 1. EXTRA DIMENSIONS

                                                                                              Symmetries

                                                                                              From the Kaluza-Klein ansatz we can write the line element as

                                                                                                                      ds2  =  (0)-  1  g�(0)dx�dx - (0) dy + kaA(�0)dx� 2
                                                                                                                                    3

                                                                                              From here we can explicitly see the symetries of the low energy effective action in D = 4.

                                                                                                  � general 4 dimensional coordinate transformations

                                                                                                                           x�  x�(x ) ,        g�(0) (graviton) ,     A�(0) (vector)

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.      � y transformation

                                                                                                                                         y  y = F (x�, y)

                                                                                                  In order to leave ds2 invariant, need

                                                                                                  F (x�, y) = y + f (x�)            =    dy    =  dy  +  f   dx�   ,    A�(0)  =       A(�0)  -      1    f
                                                                                                                                                         x�                                               x�

                                                                                                  which are gauge transformation for a massless field A(�0)! This is the way to understand that
                                                                                                  standard gauge symmetries can be derived from general coordinate transformations in extra dimen-
                                                                                                  sions, explaining the Kaluza Klein programme of unifying all the interactions by means of extra
                                                                                                  dimensions.

                                                                                                  � overall scaling

                                                                                                  y  y ,                      A�(0)   A(�0) ,     (0)        1     (0)  =      ds2            2      ds2
                                                                                                                                                             2                                    3

                                                                                                  (0) is a massless modulus field, a flat direction in the potential, so (0) and therefore the size of
                                                                                                  the 5th dimension is arbitrary. (0) is called breathing mode, radion or dilaton. This is a major
                                                                                                  problem for these theories: It looks like all the values of the radius (or volume in general) of the
                                                                                                  extra dimensions are equally good and the theory does not provide a way to fix this size. It is
                                                                                                  a manifestation of the problem that the theory cannot prefer a flat 5D Minkowski space (infinite
                                                                                                  radius) over M4 � S1 (or M3 � S1 � S1, etc.). This is the moduli problem of extra dimensional
                                                                                                  theories. String theories share this problem. Recent developments in string theory allows to fix the
                                                                                                  value of the volume and shape of the extra dimension, leading to a large but discrete set of solutions.
                                                                                                  This is the so-called "landscape" of string solutions (each one describing a different universe and
                                                                                                  ours is only one among a huge number of them).

                                                                                              Generalization to more dimensions


                                                                                                                                                                    mn Kin Ai� 
                                                                                                                     GM N  =    g� + 2 mnKimKjnAi� Aj
                                                                                                                                          mn Kim Ai                     mn

                                                                                              The Kim are Killing vectors of an internal manifold MD-4 with metric mn. The theory corresponds
                                                                                              to Yang Mills in 4 dimensions with gauge group corresponding to the isometry of the extra dimensional

                                                                                              manifold. Note that the Planck mass now behaves like

                                                                                                                     Mp2l = MD-2 VD-4  MD-2 rD-4 = M2 (M r)D-4.
                                                                                              1.3. THE BRANE WORLD SCENARIO                                               15

                                                                                              In general we know that the highest energies explored so far require M > 1 TeV and r < 10-16 cm since
                                                                                              no signature of extra dimensions has been seen in any experiment. In Kaluza Klein theories there is no
                                                                                              reason to expect a large value of the volume and it has been usually assumed that M  Mpl.

                                                                                                  Finally we can also count the number of degrees of freedom of a graviton in D dimensions using again
                                                                                              the transverse dimensions.

                                                                                                           Ndof  =  (D  - 2)(D  -  1)  -  1  =   D(D - 3)
                                                                                                                            2                         2

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Corresponding to the number of components of a traceless symmetric tensor in the D - 2 transverse
                                                                                              dimensions. Notice that only in D = 4 the graviton and the photon have the same number of degrees of
                                                                                              freedom (Ndof = 2).

                                                                                              1.3 The brane world scenario

                                                                                              So far we have been discussion the standard Kaluza Klein theory in which our universe is higher dimen-
                                                                                              sional. We have not seen the extra dimensions because they are very small (smaller than the smallest
                                                                                              scale that can be probed experimentally at colliders which is 10-16 cm).
                                                                                              We will introduce now a different and more general higher dimensional scenario. The idea here is that
                                                                                              our universe is a p brane, or a surface inside a higher dimensional bulk spacetime. A typical example of
                                                                                              this is as follows: all the Standard Model particles (quarks, leptons but also gauge fields) are trapped on
                                                                                              a 3 dimensional spatial surface (the brane) inside a higher dimensional spacetime (the bulk). Gravity on
                                                                                              the other hand lives on the full bulk spacetime and therefore only gravity probes the extra dimensions.
                                                                                              The total action can be written as:

                                                                                                                             S = Sbulk + Sbrane

                                                                                              with

                                                                                                                 Sbulk = -MD-2 dDx |G|(D)R

                                                                                              and
                                                                                                                                             Sbrane = d4x || (L(matter))

                                                                                              where � is the induced metric on the brane, which for simplicity we are considering it to be a p = 3
                                                                                              brane but in principle it could be any other dimensionality p  D - 1.

                                                                                              Therefore we have to distinguish the D dimensional bulk space (background spacetime) from the (p + 1)

                                                                                              world volume coordinates of a p brane. Matter lives in the d(= 4) dimensions of the brane, whereas

                                                                                              gravity takes place in the D bulk dimensions. This scenario seems very ad hoc at first sight but it is

                                                                                              naturally realized in string theory where matter tends to live on D branes (a particular class of p branes

                                                                                              corresponding to surfaces where ends of open strings are attached to). Whereas gravity, coming from

                                                                                              closed strings can leave in the full higher dimensional (D = 10) spacetime. Then the correspondence is

                                                                                              as follows:

                                                                                                                    gravity  closed strings

                                                                                                                    matter  open strings
                                                                                              16  CHAPTER 1. EXTRA DIMENSIONS

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Figure 1.3: Brane world scenario with matter corresponding to open strings which start and end on the brane and gravity

                                                                                              incorporated by closed strings probing the full bulk spacetime.

                                                                                              For phenomenological purposes we can distinguish two different classes of brane world scenarios.

                                                                                              1.3.1 Large extra dimensions

                                                                                              Let us first consider an unwarped compactification, that is a constant warp factor W (y). We have
                                                                                              remarked that the fundamental higher dimensional scale M is limited to be M  1 TeV in order to not
                                                                                              contradict experimental observations which can probe up to that energy. By the same argument we have
                                                                                              constrained the size of the extra dimensions r to be r < 10-16 cm because this is the length associated
                                                                                              to the TeV scale of that accelerators can probe. However, in the brane world scenario, if only gravity
                                                                                              feels the extra dimensions, we have to use the constraints for gravity only. Since gravity is so weak, it
                                                                                              is difficult to test experimentally and so far the best experiments can only test it to scales larger than
                                                                                               0.1 mm. This is much larger than the 10-16 cm of the Standard Model. Therefore, in the brane world
                                                                                              scenario it is possible to have extra dimensions as large as 0.1 mm without contradicting any experiment!
                                                                                              This has an important implication also as to the value of M (which is usually taken to be of order Mpl)
                                                                                              in Kaluza Klein theories. From the Einstein Hilbert action, the Planck mass Mpl is still given by

                                                                                                                                                    Mp2l = MD-2 VD-4
                                                                                              with VD-4  rD-4 denoting the volume of the extra dimensions. But now we can have a much smaller
                                                                                              fundamental scale M if we allow the volume to be large enough. We may even try to have the fundamental
                                                                                              1.3. THE BRANE WORLD SCENARIO                                                                         17

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  scale to be of order M  1 TeV. In five dimensions, this will require a size of the extra dimension to be of
                                                                                              order r  108 km in order to have a Planck mass of the observed value Mpl  1018 GeV (where we have
                                                                                              used r = Mp2l/M3). This is clearly ruled out by experiments. However, starting with a 6 dimensional
                                                                                              spacetime we get r2 = Mp2l/M4, which gives r  0.1mm for M = 1 TeV. This is then consistent with all
                                                                                              gravitational experiments as well as Standard Model tests. Higher dimensions would give smaller values
                                                                                              of r and will also be consistent. The interesting thing about the 6 dimensional case is that it is possible to
                                                                                              be tested by the next round of experiments in both, the accelerator experiments probing scales of order
                                                                                              TeV and gravity experiments, studying deviations of the squared law at scales smaller than 0.1mm.

                                                                                                  Notice that this set up changes the nature of the hierarchy problem because now the small scale (i.e.
                                                                                              Mew  M  1 TeV) is fundamental whereas the large Planck scale is a derived quantity. The hierarchy
                                                                                              problem now is changed to explain why the size of the extra dimensions is so large to generate the Planck
                                                                                              scale of 1018 GeV starting from a small scale M  1 TeV. This changes the nature of the hierarchy
                                                                                              problem, because it turns it into a dynamical question of how to fix the size of the extra dimensions.
                                                                                              Notice that this will require exponentially large extra dimensions (in units of the inverse fundamental
                                                                                              scale M). The hierarchy problem then becomes the problem of finding a mechanism that gives rise to
                                                                                              exponentially large sizes of the extra dimensions.

                                                                                              Number of extra dimensions                  Size of r for M = 1TeV
                                                                                                               1                                      1011m
                                                                                                               2                                      10-4m
                                                                                                               3                                      10-9m
                                                                                                               6                                     10-12m

                                                                                              Exercise: Demonstrate that the volume of a N - 1 sphere of radius r is

                                                                                                                                VN -1  =  2N/2   rN -1                                              (1.1)
                                                                                                                                          (N/2)

                                                                                              Hint: It may help to consider the integral IN = dN xe-2 with 2 =  N     x2i .  Use  this  result  to  derive
                                                                                                                                                                i=1

                                                                                              an expression for the electric (and gravitational) potential in D dimensions. Show that the potential due

                                                                                              to a point particle in five dimensions reduces to the 4-dimensional potential at distances much larger than

                                                                                              the size of the fifth dimension.

                                                                                              1.3.2 Warped compactifications

                                                                                              This is the so-called Randall Sundrum scenario. The simplest case is again a 5 dimensional theory but
                                                                                              with the following properties. Instead of the extra dimension being a circle S1, it is now an interval I
                                                                                              (which can be defined as an orbifold of S1 by identifying the points y  -y, if the original circle had
                                                                                              length 2r, the interval I will have half that size, r). The surfaces at each end of the interval play a role
                                                                                              similar to a brane, being 3 dimensional surfaces inside a 5 dimensional spacetime. The second important
                                                                                              ingredient is that the warp factor W (y) is determined by solving Einstein's equations in this background.
                                                                                              We then have warped geometries with a y dependent warp factor exp W (y) , in 5 dimensions

                                                                                                                                       ds2 = exp W (y) � dx� dx - dy2 .
                                                                                              18  CHAPTER 1. EXTRA DIMENSIONS

                                                                                              The volume VD-4 has a factor

                                                                                                                                                                                          +

                                                                                                                                              VD-4  dy exp W (y) .

                                                                                                                                                                                        -

                                                                                              Consider then the two branes,one at y = 0 ("the Planck brane") and one at y = r ("the Standard Model

                                                                                              brane"), the total action has contributions from the two branes and the bulk itself:

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Figure 1.4: Brane configuration in the Randall-Sundrum scenario: The warped geometry in the y direction gives rise to a

                                                                                              mass hierarchy between the Planck brane at y = 0 and the Standard Model brane at y = r. Notice this is only a cartoon.
                                                                                              The energy scales are redshifted so that we can have Planck scale on the left brane and the TeV scale on the right brane.

                                                                                                                                             S = Sy=0 + Sy=r + Sbulk

                                                                                              Einstein's equations imply W (y)  e-|ky| with k a constant (see [5] and example sheet 4), so the metric
                                                                                              changes from y = 0 to y = r via � - exp(-kr)�. This means that all the length and energy
                                                                                              scales change with y. If the fundamental scale is M  Mpl, the y = 0 brane carries physics at Mpl, but
                                                                                              as long as we move away from this end of the interval, all the energy scales will be "red shifted" by the
                                                                                              factor e-|ky| until we reach the other end of the interval in which y = r . This exponential changes of
                                                                                              scales is appropriate for the hierarchy problem. If the fundamental scale is the Planck scale, at y = 0
                                                                                              the physics will be governed by this scale but at y = r we will have an exponentially smaller scale. In
                                                                                              particular we can have the electroweak scale Mew  Mpl � e-kr  1 TeV if r is only slightly bigger than
                                                                                              the Planck length r  50 pl. This is a more elegant way to "solve' the hierarchy problem. We only need
                                                                                              to find a mechanism to fix the value of r of order 50 pl! Notice that in this scenario 5 dimensions are
                                                                                              compatible with experiment (unlike the unwarped case that required a radius many kilometers large).

                                                                                              Exercise: Consider a five dimensional gravity theory with a negative cosmological constant  < 0,
                                                                                              compactified on an interval (0, ). Each end of the interval corresponds to a '3-brane' which we choose
                                                                                              to have tension �/k respectively. Here k is a common scale to be determined later in terms of the
                                                                                              fundamental scale in 5D M and . Verify that the warped metric

                                                                                                                                        ds2 = e-2W () � dx� dx - r2 d2
                                                                                              1.3. THE BRANE WORLD SCENARIO                                                             19

                                                                                              satisfies Einstein's equations. Here e-2W () is the warp factor and r is a constant measuring the size of
                                                                                              the interval. You can use that Einstein's equations reduce to

                                                                                                    6 W 2     =     -      3  ,              3 W     =              ( - ) - () .
                                                                                                      r2               2M                      r2          2 M3 kr

                                                                                              Solve for W () and use the warp factor to show that the effective 4D Planck scale is now

                                                                                                                                                           M3
                                                                                                                                                            k
                                                                                                           Mp2l     = M3 r                   d e-2W     =           1 - e-2kr  .

                                                                                                                                 -

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Find the value of the constant k. Consider the Higgs Lagrangian on the brane at  = , bring it into
                                                                                              canonical form and show that the mass is proportional to the factor e-kr. How large can r be in order to
                                                                                              reproduce the electroweak scale from the Planck scale? Does this solve the hierarchy problem? How does

                                                                                              the Planck scale differ from the 5D scale M ?

                                                                                              1.3.3 Brane world scenarios and the hierarchy problem

                                                                                              Large and warped extra dimensions are alternatives to supersymmetry to address the hierarchy problem.
                                                                                              In the large extra dimensions scenario the hierarchy problem is exchanged to the problem of finding
                                                                                              compactifications with very large volumes.

                                                                                                  In the warped case the `solution' is more elegant as we can see on the simple D = 5 example mentioned
                                                                                              above (Randall-Sundrum).

                                                                                                  The Higgs Lagrangian is

                                                                                              Svis                     d4x |gvis| gv�is D�H D H -  (|H|2 - v02)2
                                                                                                                       d4x |g4| e-4kr g4� e2kr D�H D H -  (|H|2 - v02)2
                                                                                                     gvis=e-2kr g4     d4x |g4| g4� D�H D H -  (|H|2 - e-2krv02)2

                                                                                                    = Hekr H

                                                                                              In the last step we canonically normalised the Higgs field such that the kinetic terms are canonical. The
                                                                                              Higgs mass then is given by mH = e-krv0 and depends on the warp factor. The natural scale for v0 is
                                                                                              the Planck scale. To obtain a Higgs mass at the weak scale we need kr  50. The 4-dim Planck scale
                                                                                              and the 5-dim scale M are here comparable as e-2kr is tiny.

                                                                                                                                                      mH  e-kr Mpl

                                                                                              This solves the hierarchy problem through warping as long as a mechanism can be found to stabilise
                                                                                              the radius r to the required value. The advantage over the large extra dimensions is that it looks more
                                                                                              factible to stabilise r to values kr  50 than the hierarchically large values needed for the volume in the
                                                                                              unwarped case.

                                                                                                  Building concrete models that include the standard model and addressing its other problems on a
                                                                                              brane is not straightforward. Notice that in both scenarios, the problem of solving the hierarchy problem
                                                                                              has been turned into the problem of fixing the size of the extra dimensions. It is worth remarking that both
                                                                                              mechanisms have been found to be realised in string theory (putting them on firmer theoretical grounds
                                                                                              since otherwise they are adhoc scenarios based on higher dimensional (nonrenormalisable) gravitational
                                                                                              theories). Studying mechanisms to fix the moduli that determines the size and shape of extra dimensions
                                                                                              is one of the most active areas of research within string theory and higher dimensional theories in general.
Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.

                                                                                              20

                                                                                              CHAPTER 1. EXTRA DIMENSIONS
                                                                                              Chapter 2

                                                                                              Supersymmetry in higher dimensions

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  So far we have discussed the possible bosonic fields in extra dimensions (scalars, vectors, antisymmetric
                                                                                              tensors and metrics). What about fermionic fields in extra dimensions? Good references for the technical
                                                                                              aspects are [6, 8, 9].

                                                                                              2.1 Spinors in higher dimensions

                                                                                              For a theory of fermions in more than four dimensions, need some analogue of the four dimensional Dirac

                                                                                               matrices, i.e. representations of the Clifford algebra

                                                                                                                  M , N = 2 MN ,                       M N     =  i  M , N        ,
                                                                                                                                                                  4

                                                                                              where the MN are generators of SO(1, D - 1) subject to the Lorentz algebra

                                                                                                  MN , P Q = i MQ NP + NP MQ - MP NQ - NQ MP .

                                                                                              2.1.1 Spinor representations in even dimensions D = 2n

                                                                                              Define n pairs of ladder operators

                                                                                              a0  :=           i  0 + 1               =  (a0)      =   i  -0 + 1
                                                                                                               2                                       2

                                                                                              aj  :=           i  2j - i2j+1          =  (aj )     =   i  2j + i2j+1        ,     j = 1, ..., n - 1 ,
                                                                                                               2                                       2

                                                                                              whose hermiticity properties are due to (0) = +0 and (M=0) = -M=0. From the Clifford algebra

                                                                                              in MN = diag(+1, -1, ..., -1) signature, it follows that the aj (where j = 0, 1, ..., n - 1 now) furnish

                                                                                              a set of n fermionic oscillators

                                                                                                                  ai , (aj ) = ij ,      ai , aj = (ai) , (aj ) = 0 .

                                                                                              Let |0 denote the vacuum such that ai|0 = 0, then there are states

                                                                                                                  states |0 (ai) |0 (ai) (aj) |0 � � � (an) (an-1) ... (a1) |0

                                                                                                               number 1            n     (  n   )         ���           1
                                                                                                                                            2

                                                                                              of total number

                                                                                                                                                       n  

                                                                                                                                    n                          n     =  2n     =     2D     .
                                                                                                                  1 + n +   + ... + 1 =                                                  2

                                                                                                                                2                      k=0 k

                                                                                                                                                   21
                                                                                              22                                                   CHAPTER 2. SUPERSYMMETRY IN HIGHER DIMENSIONS

                                                                                              States    in  the  spinor  representations        are    defined    by     n  =  D/2     quantum     numbers          si  =  �  1
                                                                                                                                                                                                                              2

                                                                                                                                |s0, ... , sn-1        :=     (a0)(s0+      1  )  ...  (an-1 )(sn-1 +  1  )  |0  .
                                                                                                                                                                            2                          2

                                                                                              Note that the generators (2i)(2i+1) mutually commute. So we diagonalize all of

                                                                                                                                (a0) a0     -      1    =      +  1      0 , 1          = -i01
                                                                                                                                                   2              4                     = (2j)(2j+1)

                                                                                                                                (aj ) aj    -      1    =      i     2j , 2j+1
                                                                                                                                                   2           4

                                                                                              and find the |s0, ..., sn-1 defined above to be the simultaneous eigenstates of


                                                                                                                            Si  :=      (a0) a0            -   1     =      -i01             : i=0
                                                                                                                                                               2

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.                                            (ai) ai            -   1     =      (2i)(2i+1)       : i = 1, ..., n - 1
                                                                                                                                                               2

                                                                                              in the sense that

                                                                                                                                           Si |s0, ... , sn-1 = si |s0, ... , sn-1 .

                                                                                              Call those |s0, ..., sn-1         Dirac  spinors.    In  D   =4     dimensions           with  n  =  2,  for   instance,     the    states  |  �  1  ,  �  1
                                                                                                                                                                                                                                                2        2

                                                                                              form a 4 component spinor.

                                                                                              Representations in even dimensions are reducible, since the generalization of 5,

                                                                                                                                            2n+1 := in-1 0 1 ... 2n-1 ,

                                                                                              satisfies

                                                                                                                 2n+1 , M = 0 ,                            2n+1 , MN = 0 ,                             (2n+1)2 = 1 .

                                                                                              It follows from

                                                                                                                                                           1         i      n-1
                                                                                                                                                           4         4
                                                                                                                 2n S0 S1 ... Sn-1              =      2n         +                    0 , 1 ... 2n-2 , 2n-1

                                                                                                                                                = in-10 1 ... 2n-1 = 2n+1 .

                                                                                              that all the |s0, ..., sn-1 are eigenstates to 2n+1

                                                                                                                                       2n+1 |s0, ... , sn-1 = �|s0, ... , sn-1

                                                                                              with   eigenvalue  +1      for    even  numbers      of  si  =   -  1  and    -1    for  odd   ones.     This      property     is  called     chirality,
                                                                                                                                                                  2

                                                                                              and spinors of definite chirality are referred to as Weyl spinors.

                                                                                              2.1.2 Spinor representations in odd dimensions D = 2n + 1

                                                                                              Just add i2n+1 = in01 ... 2n-1 to the M matrices of D = 2n dimensions. From its properties

                                                                                              {2n+1, M } = 0 and (2n+1)2 = 1, it perfectly extends the Clifford algebra in D = 2n dimensions to

                                                                                              D = 2n + 1 with extended metric � = (+1, -1, ..., -1).

                                                                                              Since there is no further  matrix with which 2n+1 could be paired to a further ai operator, the

                                                                                              representation is the same as for D = 2n, but now irreducible. The SO(1, 2n) generators in addition to

                                                                                              those  of  SO(1, 2n - 1)          are given   by  i  M    2n+1      with      M     = 0, 1, ..., 2n - 1.       Since      odd dimensions do not
                                                                                                                                                2

                                                                                              have   a  "5",     there  is  no  chirality.  The    spinor      representations'        dimension       is    2 . D-1
                                                                                                                                                                                                                    2

                                                                                              In general, define ND to give the number of spinor components:


                                                                                                                                                           2n  =  2D           : D = 2n even
                                                                                                                                                                      2
                                                                                                                                       ND   :=
                                                                                                                                                           2n  =  2 D-1        : D = 2n + 1 odd
                                                                                                                                                                         2
                                                                                              2.2. SUPERSYMMETRY ALGEBRA                             23

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  2.1.3 Majorana spinors (extra material not covered in lectures)

                                                                                              Let us now introduce the notion of reality for spinors in Minkowski spacetime. Under infinitesimal Lorentz
                                                                                              transformations, spinors  transform into  =  + iMN MN . Since the MN are in general complex,
                                                                                              it is not guaranteed that relations between  and its complex conjugate  are consistent with Lorentz
                                                                                              transformations.
                                                                                              A relation between    is referred to as the Majorana condition. It has to be of the form  = C0
                                                                                              where C is the charge conjugation matrix. Consistency requires (C0)  C0 = 1 which is possible in
                                                                                              dimensions D = 0, 1, 2, 3, 4 mod 8. In other words, among the physically sensible dimensions, D = 5, 6, 7
                                                                                              do not admit a Majorana condition.
                                                                                              A Majorana condition can be imposed on a Weyl spinor if D = 0, 1, 2, 3, 4 mod 8 and the Weyl represen-
                                                                                              tation is conjugate to itself. Weyl spinors exist in even dimensions D = 2n, and by analyzing the complex
                                                                                              conjugate of the chirality matrix

                                                                                                                                     (2n+1) = (-1)n+1 C-1 0-1 2n+1 0 C ,

                                                                                              it turns out that charge conjugation only preserves the spinors' chirality if (-1)n+1 = +1. If n is even,
                                                                                              i.e. in D = 4, 8, 12, ... dimensions, the two inequivalent Weyl representations are complex conjugate to
                                                                                              each other, and one can either impose the Weyl or Majorana condition, but not both! In dimensions
                                                                                              D = 2 mod 8, the Weyl representations are self conjugate and compatible with the Majorana condition,
                                                                                              so Majorana Weyl spinors are possible in dimensions D = 2 and D = 10.

                                                                                              2.2 Supersymmetry algebra

                                                                                              The SUSY algebra in D dimensions consists of generators MMN , PM , QA last of which are spinors in
                                                                                              D dimensions (with index A counting the number of supersymmetries as in the extended SUSY case in

                                                                                              D = 4). The algebra has the same structure as in 4 dimensions, with the bosonic generators defining a
                                                                                              standard Poincar�e algebra in higher dimensions, QA transforming as spinors imply:

                                                                                              [M MN , QA ] = -                     M N    QA


                                                                                                  where MN as defined above represent the Lorentz transformation in the spinorial representation.
                                                                                              Finally the pure spinorial part:

                                                                                              QA , QB                              = AB M PM + ZAB

                                                                                                                        M

                                                                                              where AB are dimension-dependent constants and the central charges ZAB now can also include
                                                                                              brane charges. This is the D > 4 Coleman Mandula- or HLS generalization of the D = 4 algebra. The
                                                                                              arguments for the proof are identical to those in 4 dimensions and we will skip them here.
                                                                                              A new feature of the Poincar�e algebra is that all the generators M (2j)(2j+1) commute with each other
                                                                                              and can thus be simultaneously diagonalized as we have seen in the discussion of the higher dimensional
                                                                                              spinorial representation. Then we can have several "spins" defined as the eigenvalues of these operators.
                                                                                              Of particular relevance is the generator M 01. This is used to define a weight w of an operator O by

                                                                                                                                   M 01 , O = -iw O

                                                                                              where O and O have the same weight.
                                                                                              24                                                 CHAPTER 2. SUPERSYMMETRY IN HIGHER DIMENSIONS

                                                                                              2.2.1 Representations of supersymmetry algebra in higher dimensions

                                                                                              Similar to the 4-dimensional case we consider the massless states defined by momenta
                                                                                                                                                   P � = (E , E , 0 , ... , 0)

                                                                                              again the little group (ISO(D - 2)) has infinite dimensional representations. If we limit to only finite
                                                                                              dimensional representations we restrict to the smaller little group O(D - 2)1. We define the spin to be
                                                                                              the maximum eigenvalue of MMN in the representation. Notice that for the momentum of a massless
                                                                                              particle P 1 - P 0 = 0 and that

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.                                             M 01 , P 1 � P 0 = i P 1 � P 0 .

                                                                                              Therefore the weight of P 1 � P 0 is w = �1. As the "-" combination P 1 - P 0 is zero in massless

                                                                                              representations, the weight w = -1 can be excluded and we only need to consider combinations of

                                                                                              {Q, Q}  in   which  both   Q's  have    weight        w     =      +  1  .
                                                                                                                                                                    2

                                                                                              So if we start with arbitrary spinors Q of the form

                                                                                                                              Q       =  |�      1  ,  �      1  ,  �     1  ,   ���      ,  �   1    ,          = 1, ..., ND
                                                                                                                                                 2            2           2                      2

                                                                                              with ND    components (recall that         ND  =         2D     for      even and ND                  =     2 D-1     for odd dimensionality           respectively),
                                                                                                                                                           2                                                     2

                                                                                              requiring   weight  +  1   means   that    (,  as  a     special            case         of    [M MN , Q] =           -MN Q,)
                                                                                                                     2

                                                                                                                              M 01 , Q           =           -01 Q                        =      -iS0 Q             =!    -  i  Q      ,
                                                                                                                                                                                                                             2

                                                                                              so Q has to be of the form

                                                                                                                         Q    w=+  1     =             1  ,   �     1  ,     �   1  ,     ��� ,  �  1     ,             =  1,   ...,  ND   .
                                                                                                                                   2                   2            2            2                  2                                  2
                                                                                                                                             |+

                                                                                              This  leads  to  half  of  the  number     of  components                      of  Q           in  the     massless       case,    namely       ND  .
                                                                                                                                                                                                                                               2

                                                                                              Furthermore, we can separate the Q's into Q+ and Q- according to eigenvalues of M23 (standard spin in

                                                                                              4d). They furnish an algebra of the form {Q+, Q+} = {Q-, Q-} = 0 and {Q+, Q-} = 0 corresponding

                                                                                              to creation- and annihilation operators. To see this, consider the commutator

                                                                                                       M (2j)(2j+1) , Q( Q) = -Q( Sj Q) - Sj Q( Q) = -(s(j) + sj()) Q( Q) .

                                                                                              Using the super Poincar�e algebra, we can also show this expression to be a linear combination of the
                                                                                              P 2...P D-1 which are all zero in our case P � = (E , E , 0 , ... , 0). Consequently, all the combinations
                                                                                              sj() + sj() have to vanish leaving {Q+ , Q-=} as the only nonzero anticommutators.
                                                                                              This implies that a supersymmetric multiplet can be constructed starting from a "vacuum" state | of
                                                                                              helicity  annihilated by the Q- operators, Q-| = 0, and the rest of the states in the multiplet are
                                                                                              generated by acting on Q+. Therefore they will be of the form

                                                                                                                         Q+   w=+  1     =   |   +     1  ,         1     ,  �   1     ,  ��� ,     �  1     ,            =  1,  ...,  ND
                                                                                                                                   2                   2            2            2                     2                                4
                                                                                                                                                              +

                                                                                                  1Notice that restricting to only finite dimensional representations is a strong assumption. It is less justified than the

                                                                                              4-dimensional case in which it can be argued that there is no physical evidence for the infinite dimensional massless

                                                                                              representations. However in higher dimensions this is a less clear argument since extra dimensions themselves have not

                                                                                              been observed. This issue needs better understanding.
                                                                                              2.2. SUPERSYMMETRY ALGEBRA                                                                                                                             25

                                                                                              and  the  total  number   will  be   ND  .
                                                                                                                                    4

                                                                                              Given some state | of helicity  (i.e. M23| = | ), the action of any Q+ will lower the M 23 eigenvalue:

                                                                                                          M 23 Q+ | = M 23 , Q+ | + Q+ M 23 | = -23 Q+ | +  Q+ |

                                                                                                                            =             -   1  Q+ |
                                                                                                                                              2

                                                                                              We   therefore   obtain  the  follwing   helicities    by   application        of  the      Q+       w=+  1
                                                                                                                                                                                                        2

                                                                                                                                   | ,           |     -  1  ,         ...   ,   | -      1  �  ND  .
                                                                                                                                                          2                               2      4

                                                                                              It follows for the range of occurring 's that

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.                                      max - min            =     -               -   ND             =   ND      ,
                                                                                                                                                                                  8                  8

                                                                                              imposing ||  2 thus requires ND  32.                     But      remembering               that     ND   =      2 , 2 D  D-1   for even and odd

                                                                                                                                                                                                               2           2

                                                                                              dimensionality, this implies a maximum number of spacetime dimensions D = 10, 11.

                                                                                              Notice the similarity of this argument with the previous proof that the maximum number of supersym-

                                                                                              metries in 4 dimensions was N = 8. We will see later that precisely N = 8 supergravity is obtained from

                                                                                              the supersymmetric theories in D = 10 and D = 11.

                                                                                              Let us take a closer look at the spectrum of D = 11 and D = 10:

                                                                                                  � D = 11
                                                                                                     Only N = 1 SUSY is possible. The only multiplet consists of

                                                                                                                                  gMN ,               M  ,                          AM N P

                                                                                                                                 graviton           gravitino          antisymmetric tensor (non-chiral)

                                                                                                   In order to count the (on shell) degrees of freedom for each field we have to perform the analysis

                                                                                                   based  on   the  little  group  O(D-2).       The graviton in       D        dimensions          carries    (D-2)(D-1)     -1        components,
                                                                                                                                                                                                                        2

                                                                                                   corresponding to a symmetric tensor in D - 2 dimensions minus the trace, which is 45 - 1 = 44 in

                                                                                                   the D = 11 case. An antisymmetric tensor of rank p + 1 in D dimensions has                                                 D-2           degrees of
                                                                                                                                                                                                                              p+1

                                                                                                   freedom,    in  the  case  of  AM N P      with  p + 1 = 3,         this  is  (  9  )  =  84.
                                                                                                                                                                                    3

                                                                                                   For  the    gravitino spinor    �,     we  have  2  D-3   � (D  - 2) - 2      D-3      independent components:             The first        factor
                                                                                                                                                          2                         2

                                                                                                   is the product of the spinor components times the vector components of the gravitino (since it carries

                                                                                                   both  indices),     and  the   subtraction    of    the   2 D-3     degrees      of    freedom       of  a  spin     1     particle  is  similar  to
                                                                                                                                                                    2                                                   2

                                                                                                   the subtraction of the trace for the graviton. In terms of su(2) representations (1)                                       1         =   3    1   ,
                                                                                                                                                                                                                              2             2    2

                                                                                                   one can say that the spin           1  contribution on the right hand side is discarded.                                   More generally, a
                                                                                                                                       2

                                                                                                   vector spinor M only furnishes an irreducible Lorentz representation if contractions with any

                                                                                                   invariant tensor (such as the metric and the higher dimensional  matrices) vanish. If the "gamma

                                                                                                   trace" M M  was nonzero, then it would be a lower irreducible representation on its own right.
                                                                                                   In D = 11, we obtain 9 � 24 - 24 = 128 components for the gravitino which matches the number of

                                                                                                   bosonic degrees of freedom 84 + 44.

                                                                                                  � D = 10

                                                                                                     This allows two different N = 2 theories and one N = 1 corresponding to the massless spectrum of
                                                                                                     type IIA, type IIB string theories (N = 2) and type I or heterotic (N = 1). The spectrum for each
                                                                                                     of these theories is written in the table.
                                                                                              26                                            CHAPTER 2. SUPERSYMMETRY IN HIGHER DIMENSIONS

                                                                                                                IIA gMN 2 � M                       BM N                       AM N P         AM        2�

                                                                                                                IIB gMN 2 � M  2 � BMN 2 �  AM  NP Q 2 � 

                                                                                                                      I (gMN BMN                                   M  ) (gravity) (AM ) (chiral)

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Here the fermions in type IIA case have opposite chirality (so the theory is not chiral) and the fermions
                                                                                              in type IIB have the same chirality (so the theory is chiral). Also in the IIB case the field strength of the
                                                                                              4-index field AM  NP Q is self dual. It is easy to check that the number of bosonic and fermionic degrees
                                                                                              of freedom in both IIA and IIB cases adds up to 128. In the type I case there are two different types of
                                                                                              N = 1 multiplets, the unique gravitational one with 64 + 64 degrees of freedom and the chiral or matter
                                                                                              multiplets with 8 + 8 degrees of freedom each.

                                                                                              2.2.2 Supersymmetry Algebra and p-Branes

                                                                                              Recall that about general antisymmetric tensors BM1...Mp+1 of spin 0 or 1, we know:
                                                                                                  � BM couples to a particle BM dxM , where dxM refers to the world line
                                                                                                  � BMN couples to a string BMN dxM  dxN (world sheet)
                                                                                                  � BMNP to a membrane ...
                                                                                                  � BM1...Mp+1 to a p brane

                                                                                              The coupling is dependent of the object's charges Zi1...ip = dD-1J 0i1...ip :

                                                                                                                                       object            charge        couples to
                                                                                                                                      particle              q              AM
                                                                                                                                                                          BM N
                                                                                                                                        string             ZM
                                                                                                                                      p brane           ZM1 ...Mp      BM1 ...Mp+1

                                                                                              Charges of p-branes are new examples of central charges in the SUSY algebra:

                                                                                                                                          Q , Q  a P + bM1...Mp ZM1...Mp

                                                                                                  For instance in D = 11 the presence of the AMNP tensor implies they couple to 2-branes. The
                                                                                              dual tensor corresponds to AMNP QRS (its seven index field strength is dual to the 4-index field strength
                                                                                              of AMNP ) which couples to the (magnetic) p = 5 branes. So the natural extended objects in D =
                                                                                              11 supergravity are 2-branes and 5-branes. The corresponding charges are then ZMN and ZMNP QR.
                                                                                              Therefore the SUSY algebra can be written as

                                                                                                                Q, Q = CM  PM + CMN  ZMN + CMNP QR  ZMNP QR

                                                                                              Where C is the charge conjugation matrix. A test to count the number of independent components of

                                                                                              this algebra is that on the LHS there are 32 � 33/2 = 528 independent components (since the dimension

                                                                                              of the spinors in D = 11 is 32) whereas in the LHS, the first term has 11 components from PM the second

                                                                                              11 � 10/2  =  55  from  ZM N  and  the  last  one  (  11  )  =  462  so  giving  a  total  for  the  LHS  of  11 + 55 + 462  =  528
                                                                                                                                                    5

                                                                                              the same as the number of components of the RHS. So we do not expect more surprises to add to the

                                                                                              algebra.
                                                                                              2.3. DIMENSIONAL REDUCTION                                                                                                                        27

                                                                                                  The central charges as in the case of extended supersymmetry in D = 4 play an important role
                                                                                              defining the BPS states. The p-branes can be the corresponding BPS objects. The generalisation of the
                                                                                              BPS condition is setting their charges equal to their tension (like the mass/charge relation in the case of
                                                                                              pointlike objects in D = 4). Usually the charge that appears in the BPS condition is the projection to
                                                                                              the brane of the tensorial charges Z. The sign if this charge defines branes versus antibranes that carry
                                                                                              same tension but opposite charges of the corresponding brane. p-branes also appear as solitonic solutions
                                                                                              of the supergravity field equations. They appear as black hole kind of solutions known as black-branes of
                                                                                              the supergravity with the singularity not being point-like but of higher dimension (p). The BPS condition
                                                                                              as usual implies that branes preserve part of the original supersymmetry.

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  2.3 Dimensional Reduction

                                                                                              Let us review the general procedure of reducing any number of dimensions bigger than 4 to d = 4. Recall
                                                                                              the example of a scalar in 5 dimensions M5 = M4 � S1 (the last of which has radius R) where field in
                                                                                              5 dimensions could be replaced by  many fields in d = 4. If  is massless,

                                                                                                                                 M M  = 0                   =      ��n             -   n2     n     =              0,
                                                                                                                                                                                       R2

                                                                                              then  the  Fourier  mode        n  with    respect      to  the  S1  dimension       has     a  mass       of  n     .
                                                                                                                                                                                                             R

                                                                                              For dimensional reduction, only keep the n = 0 mode,

                                                                                                                           (xM )  (x�)

                                                                                                                        AM (xM )  A�(x�) , Am(x�) , m = 4, ..., D - 1

                                                                                                                                                                     scalars

                                                                                                                               BMN  B� ,                       B�n ,              Bmn

                                                                                                                                                               vectors            scalars

                                                                                                                                                                     .

                                                                                                                                 2n            1  2n  4D-spinors
                                                                                                                                               4

                                                                                              Consider e.g. the reduction of D = 11 to d = 4: The fundamental fields are graviton gMN that carries

                                                                                              9�10  -1   =  44  degrees    of  freedom   and      the     gravitino  M       with  9   �  2  9-1    - 2 9-1        =   8 � 16  =  128  components.
                                                                                                2                                                                                              2                2

                                                                                              Again, the subtraction is an extra spinor degree of freedom. The final field is an antisymmetric tensor

                                                                                              AM N P  that  carries  (  9  )  =  84  degrees   of     freedom.     Note      that  we  have       128    bosonic       degrees    of   freedom  and
                                                                                                                        3

                                                                                              128 fermionic degrees of freedom. Dimensional reduction to d = 4 leads to:

                                                                                                              gMN  g� ,                               g�m ,                        gmn

                                                                                                                                     graviton     7 vectors             7�8  =28  scalars  (symmetry!)
                                                                                                                                                                         2
                                                                                                            AMNP  A� ,
                                                                                                                                                  A�m ,                 A�mn ,                                     Amnp

                                                                                                                                               7 tensors           21 vectors                7�6�5  =35  scalars       (antisymmetry!)
                                                                                                                                                                                             1�2�3
                                                                                                                                                    m
                                                                                                                M   � ,

                                                                                                                                 32  =8        7�8=56 fermions
                                                                                                                                  4

                                                                                              Recall here that a three index antisymmetric tensor A� in 4 dimensions carries no degrees of freedom
                                                                                              and that two index antisymmetric tensors A�m are dual to scalars. The spectrum is the same as the
                                                                                              28                                   CHAPTER 2. SUPERSYMMETRY IN HIGHER DIMENSIONS

                                                                                              N = 8 supergravity in 4 dimensions:

                                                                                                  number  helicity  particle type  on shell degrees of freedom in d = 4
                                                                                                      1               graviton
                                                                                                      8       2       gravitino        1�  (4-2)(4-1)           -  1  =1�2=2
                                                                                                     28                 vector                     2
                                                                                                     56        3       fermion
                                                                                                     70        2        scalar     8�  2 4-2    �  (4    -  2)  -  2 4-2    = 8 � 2 = 16
                                                                                                                                             2                           2
                                                                                                              1
                                                                                                                                       (7 + 21) � (4 - 2) = 28 � 2 = 56
                                                                                                               1
                                                                                                               2                           56      �  2  4-2  =  56 � 2     =  112
                                                                                                                                                           2
                                                                                                              0
                                                                                                                                                   28 + 7 + 35 = 70

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  There is a theory of N = 8 supergravity based on the gMN and AMNP . Reducing the dimension from 11
                                                                                              to 4 has an effect of N = 1  N = 8. This N = 8 model is non-chiral, but other compactifications and p
                                                                                              branes in a 10 dimensional string theory can provide chiral N = 1 models close to the MSSM. Notice that
                                                                                              the statement of why the maximum dimensionality of supersymmetric theories is 11 is identical to the
                                                                                              statement that the maximum number of supersymmetries in 4 dimensions is N = 8 since both theories are
                                                                                              related by dimensional reduction. Actually, the explicit construction of extended supergravity theories
                                                                                              was originally done by going to the simpler theory in extra dimensions and dimensionally reduce it.

                                                                                                  Other interesting dimensional reductions are: from D = 11 to D = 10 it gives precisely the spectrum of
                                                                                              IIA supergravity. Also starting from the N = 1 matter multiplet in D = 10 and performing dimensional
                                                                                              reduction to D = 4 gives rise to the spectrum of N = 4 vector multplet in D = 4 and in general
                                                                                              dimensional reduction of D = 10, N = 1 supergravity gives rise to D = 4, N = 4 supergravity.
Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Chapter 3

                                                                                              A brief overview of compactifications

                                                                                              So far we have mostly concentrated on dimensional reduction and the only discussion of the geometry of
                                                                                              extra dimensions was through the simplest circle compactifications. The study of compactifications for
                                                                                              general geometries is very broad and here we will only touch some of the main points.

                                                                                                  The typical starting point is a supergravity theory in high dimensions for which we will search for
                                                                                              solutions preserving maximal symmetry in four dimensions times some compact manifold for the extra
                                                                                              dimensions. The relevant fields are the bosonic fields in the massless spectrum of the theory that include
                                                                                              the metric GMN , antisymmetric tensors of different ranks BM1...Mq and some scalars . The effective
                                                                                              field theory is determined by the action:

                                                                                              S = - dDx |G| MD-2DR + M M  + f ()HM1...Mq+1 HM1...Mq+1 + ...  (3.1)

                                                                                                  where the � � � stand for terms including fermions which are not relevant for our purposes and higher
                                                                                              order bosonic terms, such as higher derivatives terms including powers of the curvature, etc.. The
                                                                                              antisymmetric tensor term is actually a sum over the different values of q present in the spectrum. The
                                                                                              functions f () have a well defined dependence on the fields . Each supergravity theory has an spectrum
                                                                                              of antisymmetric tensors and very few scalars.

                                                                                                  The field equations take the general schematic form:

                                                                                                              RMN = TMN (G, H, )                             (3.2)
                                                                                              DP f HP M1...Mq = A(G, H, )                                    (3.3)
                                                                                                                                                             (3.4)
                                                                                                                    = B(G, H, )

                                                                                                  where TMN is the corresponding stress energy tensor and A, B simple functions of their arguments,
                                                                                              explicitly known case by case, that vanish with H and . The issue is to find explicit solutions of these
                                                                                              equations for values of GMN , H and  such that the geometry is of the type M4  MD-4 where
                                                                                              M4 represents maximally symmetric spacetime in D = 4 that can be Minkowski, de Sitter or anti de
                                                                                              Sitter depending if the value of the vacuum energy vanishes or is positive or negative respectively. MD-4
                                                                                              is a finite volume, usually compact euclidean manifold that needs to be determined.

                                                                                                  Notice first that the simplest solution of these equations is to have GMN = MN and HMN =
                                                                                               DM  = 0 which is the full D dimensional Minkowski space. This solution usually preserves all super-
                                                                                              symmetries and then is stable under quantum corrections. Since it does not clearly describe our world

                                                                                                                                                                 29
                                                                                              30            CHAPTER 3. A BRIEF OVERVIEW OF COMPACTIFICATIONS

                                                                                              we will have to live with the idea that there will be more than one, probably many, solutions and the
                                                                                              geometry of our universe with four, almost flat dimensions and small extra dimensions, is only one of
                                                                                              them (if at all).

                                                                                              3.1 Toroidal Compactifications

                                                                                              The second simplest case is the case where M4 is 4-dimensional Minkowski space and MD-4 = TD-4
                                                                                              with TD-4 = (S1)D-4 the D - 4 dimensional torus. This is a valid solution as the one-dimensional circle

                                                                                              was in the five dimensional case. It also preserves all supersymmetries and therefore has extended SUSY

                                                                                              in four dimensions. Implying non-chirality and therefore unrealistic spectrum to describe our world with

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  chiral weak interactions. The extra-dimensional components of the metric Gmn with m, n = 1, � � � , D - 4
                                                                                              are massless scalar fields in four dimensions with a flat potential energy. Similarly for antisymmetric

                                                                                              tensors, e.g. for a rank two tensor the components Bmn will be massless scalar fields in four dimensions.
                                                                                              These fields play an important role in compactifications and are called moduli fields since they measure

                                                                                              the size and shape of the extra dimensions.

                                                                                                  Let us discuss the simplest case of two extra dimensions. The independent components of the metric

                                                                                              and tw0-index tensor in the two extra dimensions are


                                                                                                  Gmn  =        G11                        G12      Bmn =      0B         


                                                                                                              G12 G22                                          -B 0

                                                                                                  We can collect the four independent components in terms of two complex scalar fields as follows:

                                                                                                                                             G12        
                                                                                                                                             G11          G
                                                                                                                     U                              +i  G22

                                                                                                                     T  B+i G                                               (3.5)

                                                                                                  Where here G = G11G22 - G212 is the determinant of the two-dimensional metric. The field U is
                                                                                              the standard complex structure of a two-dimensional torus. Changing the value of U changes the shape
                                                                                              of the torus. T is called the Ka�hler structure modulus since the two-dimensional torus is a Ka�hler
                                                                                              manifold. Changing the Ka�hler modulus T changes the size of the torus (since the volume is deter-


                                                                                              mined by G). These are typical fields that also appear in more general compactifications. Each of
                                                                                              them parametrise a plane defined by the coset space SL(2, R)/O(2). The full moduli space is then
                                                                                              SL(2, R)/O(2)  SL(2, R)/O(2) = O(2, 2, R)/O(2)2. Since U is the complex structure of the torus it
                                                                                              implies the standard SL(2, Z) geometric invariance

                                                                                                       U    aU  +b                         a, b, c, d  Z     ad - bc = 1    (3.6)
                                                                                                            cU  +d

                                                                                              which is just a manifestation of the invariance under deformations of the torus T2. In string theory
                                                                                              there is a further SL(2, Z) invariance of the spectrum and partition function associated to the T field
                                                                                              T  (aT + b)/(cT + d) which includes the `large' to `small' size duality (a = d = 0, b = -c = 1). This
                                                                                              is the generalisation of R  1/R duality for a circle and is called T duality. The c = 0, a = d = 1 case
                                                                                              reflects the shift symmetry for antisymetric tensors, B  B + k, k  Z. Furthermore in string theory
                                                                                              compactifications there is further a symmetry exchanging the U and T fields U  T which is called
                                                                                              mirror symmetry. Some of these results can be generalised. For a Td torus for d = D - 4, the moduli
                                                                                              space generalises to O(d, d, R)/O(d)2.
                                                                                              3.2. FREUND-RUBIN COMPACTIFICATIONS                                                   31

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.      Moduli fields give rise to beautiful mathematics. However they are problematic for several reasons.
                                                                                              The fact that they can be changed arbitrarily means that we do not know the size and shape of the extra
                                                                                              dimensions. But as we have seen before knowing the size of the extra dimensions is crucial to determine
                                                                                              the physical quantities such as the Planck mass. We also know that most values of the volume are
                                                                                              incompatible with experiments since we know that only very small volumes are allowed to explain why
                                                                                              we have not observed more than four dimensions. Furthermore having scalar fields with flat potentials
                                                                                              imply these massless particles will mediate long-range interactions that would give rise to a fifth force-
                                                                                              type of new forces for which there are very strong experimental constraints. Therefore theories of extra
                                                                                              dimensions with moduli fields are ruled out by experiments and therefore we need to look for solutions
                                                                                              of the field equations which have all moduli stabilised. This is the major challenge for theories of extra
                                                                                              dimensions.

                                                                                              3.2 Freund-Rubin Compactifications

                                                                                              Notice that in the toroidal case the only field that has a non-trivial background is the metric GMN . But
                                                                                              we know there are usually many other bosonic fields in extra dimensions that can take non trivial values
                                                                                              without breaking Lorentz invariance in four dimensions. In particular the scalars and field strengths of
                                                                                              antisymmetric tensors can be non-vanishing in general and setting them to zero is very arbitrary.

                                                                                                  Let us consider the simplest such a case. Starting with six dimensional gravity-Maxwell theory:

                                                                                                      S = - d6x |G| (6)R + F MN FMN                                                 (3.7)

                                                                                              The Maxwell field FMN may be non-vanishing but the only components that can be different from zero
                                                                                              are Fmn, m, n = 4, 5 since nonzero values for F�, �,  = 0, 1, 2, 3 would break Lorentz invariance. If we
                                                                                              want maximal symmetry in four dimensions we can write the background fields as:


                                                                                              Gmn  =      g�  0                        FM N   = f  00                             
                                                                                                                  ,

                                                                                                        0 gmn                                      0 mn

                                                                                                  Here g� is the metric of a maximally symmetric four-dimensional spacetimes (Minkowski, de Sitter
                                                                                              or anti-de Sitter), gmn the metric of a maximally symmetric compact two dimensional space (sphere),
                                                                                              f an arbitrary constant and mn the Levi-Civita tensor in two dimensions. Plugging these expressions
                                                                                              in the field equations give solutions with the compact space a two-dimensional sphere of radius R. The
                                                                                              nontrivial value of the Maxwell field on a sphere is actually the same as a magnetic monopole flux that
                                                                                              has to be quantised from the Dirac quantisation condition:

                                                                                                                 F = N,                N Z                                          (3.8)

                                                                                                              S2

                                                                                              Plugging this in the field equations (and doing a Weyl transformation of the metric to have the standard

                                                                                              Einstein-Hilbert term in four dimensions) gives rise a potential for the radius R:

                                                                                                              V (R)                N2  -   1                                        (3.9)
                                                                                                                                   R6     R4

                                                                                              The first term coming from the F MN FMN term of the action and the second term from the curvature.
                                                                                              This potential has a minimum at R  N and therefore fixes the size of the extra dimensions! The value
                                                                                              32  CHAPTER 3. A BRIEF OVERVIEW OF COMPACTIFICATIONS

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  of the potential at the minimum is negative V  -1/N 4 which means a negative value of the vacuum
                                                                                              energy. Therefore the four dimensional space is not Minkowski but anti-de Sitter.

                                                                                                  Notice that fluxes of the electromagnetic field provided the key ingredient to stabilise the size of the
                                                                                              extra dimension. As usual the fluxes are quantised but the value of the integer N is not fully determined.
                                                                                              each value gives rise to a different solution and therefore to a different four-dimensional universe. Notice
                                                                                              also that the fact that the antisymmetric field strength tensor FMN has two indices allowed a natural
                                                                                              factorisation of the six dimensional space between a four dimensional and a two dimensional space, in
                                                                                              this case AdS4 � S2. This type of compactification is called `spontaneous compactification' to make the
                                                                                              analogy with the spontaneous symmetry breaking in gauge theories (in this case the symmetry breaking
                                                                                              could be the symmetries of full six-dimensional space broken to the independent symmetries of the four
                                                                                              and two dimensional spaces) and was introduced by Freund and Rubin in the 1980's. Adding extra
                                                                                              terms to the action, such as a positive cosmological constant adds extra terms to the scalar potential and
                                                                                              allows the possibility of a minimum with vanishing vacuum energy, that is M4 � S2 with M4 the four
                                                                                              dimensional Minkowski spacetime. This is the case for compactification of a supergravity theory in six
                                                                                              dimensions found by Salam and Sezgin in 1984. Their solution also preserves N = 1 supersymmetry and
                                                                                              contrary to toroidal compactifications the spectrum is chiral in four dimensions. For these reasons it has
                                                                                              attracted much attention over the years.

                                                                                                  Generalisations of the Freund-Rubin ansatz to higher dimensions provide interesting compactifica-
                                                                                              tions. In particular, starting from D = 11 supergravity that has a three-form field with rank-four field
                                                                                              strength FMNP Q, assuming maximal symmetric spaces this allows for F�  � gives rise to a
                                                                                              factorisation of the eleven-dimensional spacetime into either AdS7 � S4 or AdS4 � X7 where X7 is a
                                                                                              maximally symmetric space, such as a seven-sphere S7. Another generalisation os for IIB supergrav-
                                                                                              ity in ten dimensions that has a rank-five field strength FM1���M5 that gives rise to backgrounds such
                                                                                              as AdS5 � S5 which has been the starting point of the celebrated AdS/CF T correspondence in which
                                                                                              this compactification is claimed to be equivalent to a four-dimensional non-gravitational conformal field
                                                                                              theory.

                                                                                              3.3 Calabi-Yau Compactifications

                                                                                              Starting from (chiral) N = 1, D = 10 supergravity (type I) motivated by string compactifications we
                                                                                              can search for compactifications that preserve N = 1 supersymmetry in D = 4 in order to have chiral
                                                                                              theories and still benefit from the properties of supersymmetric theories, as for addressing the hierarchy
                                                                                              problem and also having a flat four-dimensional spacetime. These requirements put strong constraints
                                                                                              on the nature of the compact six-dimensional manifolds. They have to be Ricci flat (Rmn = 0) just
                                                                                              as torii but the defining property is that to preserve N = 1 supersymmetry they have to be manifolds
                                                                                              with SU (3) holonomy group. Roughly speaking the holonomy group G is the group defined by parallel
                                                                                              transporting a vector around a closed trajectory on the corresponding manifold and the resulting vector
                                                                                              is related to the original one by a G transformation. In six dimensions G is a subgroup of the rotation
                                                                                              group SO(6). Being holonomy SU (3) defines the manifold to be a Calabi-Yau manifold.

                                                                                                  The knowledge of Calabi-Yau manifolds is limited since it is known they admit Ricci flat metrics but
                                                                                              explicit metrics are not known since in particular the manifold has no isometries. This makes them not
                                                                                              suitable for the Kaluza-Klein realisation of gauge symmetries. The origin of gauge symmetries in four
                                                                                              3.3. CALABI-YAU COMPACTIFICATIONS              33

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  dimensions then comes from gauge symmetries already existing in the extra dimensional theory. A great
                                                                                              amount of knowledge has been accumulated about these manifolds mostly on the topological side, using
                                                                                              techniques of algebraic topology.

                                                                                                  It is beyond the scope of these notes to discuss further the details of Calabi-Yau manifolds. However
                                                                                              a few relevant properties can be mentioned. The two-dimensional version of a Calabi-Yau manifold is
                                                                                              the two-torus T2 we have discussed. We know that T2 has two types of topologically non-trivial one-
                                                                                              cycles (dual to each other). Being six-dimensional Calabi-Yau manifold have topologically non-trivial
                                                                                              cycles of dimension 2, 3, 4. The 2-and 4-cycles are dual to each other and two types of 3-cycles (there
                                                                                              are not non-trivial 1 or 5 cycles). The size of the three cycles are the complex structure moduli Ua with
                                                                                              a = 1, � � � , h12. The size of the 2- or 4-cycles are the Ka�hler moduli Ti with i = 1, � � � , h11. Here h12 and
                                                                                              h11 are the Hodge numbers of the manifold. They determine the Euler number  = 2(h12 - h11). Their
                                                                                              typical values are of order  103 - 104 for the known Calabi-Yau manifolds. This gives us an idea of
                                                                                              the number of solutions of the field equations that these manifolds provide: the number of Calabi-Yau
                                                                                              manifolds is not even known to be finite. For each Calabi-Yau there are many fluxes that can be turned
                                                                                              on like

                                                                                                                                    H3 = Ni  (3.10)

                                                                                                                                 i

                                                                                                  for each three-index antisymmetric tensor field strength Hmnp and each non-trivial 3-cycle i, i =
                                                                                              1, � � � h12. This is the main source of what is known as the string landscape with a number of solutions for
                                                                                              each Calabi-Yau manifold estimated to be of order 10500 or more. When all moduli are stabilised each
                                                                                              of these solutions will come with a different value of the vacuum energy (or cosmological constant). This
                                                                                              has been proposed as a concrete way to address the cosmological constant problem. The idea is that the
                                                                                              density of solutions with different values of the cosmological constant is high enough so that whatever
                                                                                              value of the cosmological constant is obtained after all quantum corrections to the vacuum energy are
                                                                                              computed, there will be a vacuum with the right value of the vacuum energy to give the total vacuum
                                                                                              energy of the order of the observed one. This is an unusual 'solution' to one of the main problems of
                                                                                              physics. It only indicates that what we thought it was a major question to be answered by first principles
                                                                                              (what is the value of the cosmological constant) happens to be only an environmental fact related to our
                                                                                              own universe, within what is usually (mis) named the anthropic principle. This may be disappointing
                                                                                              for theoretical physicists searching for proper explanations of nature. It has some scientific merit in the
                                                                                              sense that Weinberg predicted the current observed value of the cosmological constant by these kind of
                                                                                              arguments almost 10 years before the discovery of the acceleration of the universe.

                                                                                                  For the purpose of this course it has a merit in the sense that the main motivation for supersymmetry
                                                                                              at low energies is the solution to the hierarchy problem. For which the main criticism is that since we do
                                                                                              not know what solves the cosmological constant problem, any proposal to address the hierarchy problem
                                                                                              neglecting the cosmological constant problem is not well justified. If the cosmological constant is only an
                                                                                              environmental question then it is justified to neglect this problem in addressing the hierarchy problem.
                                                                                              However it may be argued that probably the hierarchy problem could also be environmental. This is an
                                                                                              unsolved issue but fortunately for this case experimental searches in the near future may give us an idea.
                                                                                              34                 CHAPTER 3. A BRIEF OVERVIEW OF COMPACTIFICATIONS

                                                                                              3.4 Final Remarks

                                                                                              This is the end of these lectures. We have seen that both supersymmetry and extra dimensions provide
                                                                                              the natural way to extend the spacetime symmetries of standard field theories.
                                                                                              They both have a set of beautiful formal properties, but they also address important unsolved physical
                                                                                              questions such as the hierarchy problem for instance.
                                                                                              For supersymmetry we can say that it is a very elegant and unique extension of spacetime symmetry:

                                                                                                  � It may be realized at low energies, the energy of SUSY breaking of 1 TeV is within experimental
                                                                                                     reach (hierarchy, unification, dark matter)

Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.      � It may be an essential ingredient of fundamental theory (M theory, strings).

                                                                                                  � It is a powerful tool to understand QFTs, especially non-perturbatively (S-duality, Seiberg-Witten,
                                                                                                     AdS/CFT).

                                                                                                  Extra dimensions are in some sense competing proposals to address the hierarchy problem both from
                                                                                              the warped and unwarped cases. They are also important ingredients of fundamental theories (string/M
                                                                                              theories). It is then compelling to study the physical implications of supersymmetric theories in extra
                                                                                              dimensions.

                                                                                                  However the lack of evidence of new physics from LHC already puts all the proposals to address the
                                                                                              hierarchy problem (supersymmetry, extra dimensions and other alternatives) in tension with experiments.
                                                                                              Some amount of fine tuning may be needed and therefore the whole naturalness issue may be under
                                                                                              question.

                                                                                                  Both supersymmetry and extra dimensions may be subject to be further tested soon in experiments.
                                                                                              Notice that they are both basic ingredients of string theory (that addresses the problem of quantum
                                                                                              gravity) and as such deserve further study, but they may be relevant only at higher energies than those
                                                                                              available in the near future, we need to remain patient. Independent of any experimental verification
                                                                                              they have expanded our understanding of physical theories which is a good argument to continue their
                                                                                              study.
Copyright � 2015 University of Cambridge. Not to be quoted or reproduced without permission.  Bibliography

                                                                                                       [1] F. Quevedo, S. Krippendorf and O. Schlotterer, Cambridge Lectures on Supersymmetry and
                                                                                                            Extra Dimensions, arXiv:1011.1491 [hep-th].

                                                                                                       [2] S. Weinberg, The quantum theory of fields, Volume I Foundations, CUP (1995).
                                                                                                       [3] For a recent discussion of dualities see: J. Polchinski, Dualities of Fields and Strings,

                                                                                                            arXiv:1412.5704 [hep-th].
                                                                                                       [4] N. Arkani-Hamed, S. Dimopoulos and G. R. Dvali, Phenomenology, astrophysics and cosmology

                                                                                                            of theories with submillimeter dimensions and TeV scale quantum gravity, Phys. Rev. D 59
                                                                                                            (1999) 086004 [arXiv:hep-ph/9807344].
                                                                                                       [5] L. Randall and R. Sundrum, A large mass hierarchy from a small extra dimension, Phys. Rev.
                                                                                                            Lett. 83 (1999) 3370 [arXiv:hep-ph/9905221].
                                                                                                       [6] P. C. West, Supergravity, brane dynamics and string duality, arXiv:hep-th/9811101.
                                                                                                       [7] S. Weinberg, The quantum theory of fields, Volume III Foundations, CUP (1998).
                                                                                                       [8] J. Polchinski, Superstring Theory and beyond, Volume II, CUP 2005.
                                                                                                       [9] J. A. Strathdee, Extended Poincar�e Supersymmetry, Int. J. Mod. Phys. A 2 (1987) 273.

                                                                                                                                                                 35
