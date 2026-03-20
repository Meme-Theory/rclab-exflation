# Church KK Stanford 2022

**Source:** `02_Church_KK_Stanford_2022.pdf`

---

Kaluza-Klein Theory

                                     Benjamin Church
                                     December 3, 2022

Contents

1 Kaluza-Klein Theory                                  2

subsection1.1 A Five-Dimensional Space-Time2

1.2 Gauge Transformations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

subsection1.3 The Five-Dimensional Christoel Symbols3

1.4 The Einstein-Hilbert Action for Kaluza-Klein Theory . . . . . . . . . . . . . . 4

subsection1.5 The Field Equations5

1.6 The Lorentz Force Law . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

subsection1.7 Charge Quantization6

                                    1
1 Kaluza-Klein Theory

In a 1919 letter to Einstein, Kaluza proposed that a 5-dimensional theory of general relativity
could unify gravity and electromagnetism through a purely geometric theory. Although
Kaluza-Klein theory makes incorrect predictions about the charges and masses of elementary
particles, the framework has become one the foundational pillars of modern physics leading
to Yang-Mills theories.

1.1 A Five-Dimensional Space-Time

Remark 1.1.1. It will be convnient to use the (-, +, +, +) convention for this chapter.

Consider a metric,

                                  g~� =   g�  g�5
                                          g5  g55

where tildes will indicate 5-dimensional quantities. Adding a whole new space-time di-

mension provides far too much dyamical freedom. We require the fth dimension to be

compactied, rolled-up in a small circle, explaining the fact that an extra spatial dimension

cannot be observed. The 5-dimensional space-time we construct has the topology of a ber

bundle of the circle S1 over a usual four dimensional Minkowski-like manifold M 4. This
means the space looks locally like M 4 � S1. Often, we will take the space to gobally have
the topology M 4 � S1 which we refer to a trivial bundle.

In general, the 5th basis vector will not be orthogonal to the basis e� so g�5 = e� � e5 = 0.
We can decompose e� = e� + e� where e�  e5 and e�  e5. We then write, e� = B�e5

and thus,

                 g~� = (e� + e�) � (e + e) = e� � e + e� � e = g� + 2B�B

Where,

        g = e� � e  and  2 = g~55 = e5 � e5   and  B�  =  e� � e5  =  e� � e5  =  g~�5
                                                          e5 � e5     e5 � e5     g~55

Therefore, the entire 5D metric becomes,

                         g~� =    g� + 2B�B        2B�
                                       2B           2

A simple calculation shows that,

                         g~� =    g�              -B�
                                  -B         -2 + BB

Furthermore,

                                  g~ = det g~� = 2g

where index juggling is performed with the 4D metric g� . To be able to project physics

down into the base 4D space-time, we impose the cylinder condition,

                                  5g~� = 0

so physical quantities should not change while moving along the circular fth dimension.

                                          2
1.2 Gauge Transformations

Suppose we make a coordinate transformation by rotating about the local copy of S1 by

an amount dependent on 4D space-time position. As we will see, such a transformation is

exactly a local gauge transformation which is why Kaluza-Klein is considered a U (1) gauge
theory. Explicitly, consider the transformation, x� = x� and x5 = x5 - (x�). Then,

consider the change in components of the metric,

                                           g~�    =  x~    x~
                                                     x~�   x~ g~

In particular,

                                  2  =  g~5 5  =  x~    x~          =  g~55  =  2
                                                  x~5   x~5 g~

since the coordinate transformation does not depend on x5. However,

      2B�       =  g~� 5  =  x~   x~       =   g~�5  +  x5          =  g~�5  + 2 �    =   2(B�   + �)
                             x~�  x~5 g~                x� g~55

Therefore, since  = , we see that B� transforms as a gauge eld,

                                               B� = B� + �

Finally, the 4D part of the metric transforms as,

g~�   =  g~�  +    x~5       +  x~5  g~�5  +   x~5   x~5   g~55  =  g~�  +   �g~5  +  g~�5   +   g~55� 
                   x� g~5       x              x�    x

Using our introduced elds,

         g�  + 2B� B = g� + 2 B�B + �B + B�  = g� + 2B� B

and thus the 4D space-time metric is left invariant under the gauge transformation.

                                                     g�  = g�
Therefore, rotating locally around the S1 components only changes the gauge eld B�,

                                   B�  B� + � g�  g�

1.3 The Five-Dimensional Christoel Symbols

Starting directly from the 5D metric, the Christoel symbols are easily calculated in terms
of their 4D counterparts. For the 4D components,

~ �      =  1 g~   (�g~      +   g~�  -    g~� )
            2

         =  �      +  1 g    �2BB +  2B�B - 2B�B                                +  1 g~5  (�g~5  +   g~�5)
                      2                                                            2

         = � + 2g W�B + B�W - B�B  ln 2

where I have used the cyclindrical condition 5g� = 0 and dened the quantity,

                                           W� = �B -  B�

                                                        3
Furthermore,

~ �5  =  1 g~  (�g~5  - g~�5)  =   1 g2           �B - B� + B� ln 2 - B� ln 2                      +  1  g~5�g~55
         2                         2                                                                  2

      = 1 g2   W� - B� ln 2
         2

and nally,

                               ~ 55  =   -  1  g~    g~55  =  -  1  g     2
                                            2                    2

where I can restrict to  = 5 by the cylindrical condition.

1.4 The Einstein-Hilbert Action for Kaluza-Klein Theory

To study the dynamics of the Kaluza-Klein metric, we need to calculate the Christoel
symbols and then the curvature tensor. This is a straightforward yet exceedingly tedius
calculation so I will simply write down the results. We postulate a 5D Einstein-Hilbert

action proportional to the simplest curvature invariant, R the Ricci curvature scalar. This

is the exact same form as the action for 4D general relativity. Consider the action,

                                        S~KK =       1 R~ g~ d5x
                                                     2~

Therefore, we need to examine the form of the 5-dimensional quantity R~. The expression
for R~ follows formally from the form of the metric and the Christoel symbols,

                               R~  =  R  -     1  2W�    W  �  -    2  �  �
                                               4                    

This is our rst hint of the so called Kaluza Miricle since term,

                                         LEM      =  -  1  W�  W    �
                                                        4

has exactly the form of the electromagnetic Lagrangian. Therefore, the action becomes,

               S~KK =  1             -  1            �           d5x   -     �   �       d5x
                          R             8~ W� W            g                          g

                       2~

By the cylinder condition, none of these quantities depends on x5 so we can integrate out by
x5. Suppose that C is the period of x5 or equivalently the circumference of the compactied

dimension. Then the Kaluza-Klein action becomes,

               S~KK =  C       -     C   2W�      W  �           d4x   -  C      �  �         d4x
                          R          8~                    g                               g

                       2~

Now, one last bit of alchemy. Since the constant ~ is arbitrary, set,
                                                          8GC

                                                    ~ = c4

Then we dene the vector potential A� =               C   B�   and   the   force  tensor  F�   =  �A  -  A�.
                                                     2~

Then,

                                      F� F �      =  C   2W�     W     �
                                                     2~

                                                     4
And at last, the Kaluza Miracle,

S~KK =  c4     R         d4x  -  1    F�  F  �  3        d4x  -  C     �  �           d4  n  =  SGR +SEM  + SS F
                      g          4                   g                             g
        16G

the Kaluza-Klien action becomes the action of general relativity plus the action of electro-
magnetism plus the action of a scalar eld. However, there is one sublty, the GR and EM

Lagrangians are multiplied by the scalar eld . However, if  is slowly varying then we can

approximate it as a constant and absorb it as a constant multiple of the enire Lagrangian.

When   0 a constant, the action literally reduces to,

                                               S~KK = SGR + SEM

1.5 The Field Equations

We have seen that the Einstein-Hilbert action for the 5D Kaluza-Klein theory gives rise to
a 4D Einstein-Hilbert action and the Lagrangian of an electromagnetic-like theory. Varying
this action with respect to the elds, we recover the Einstein eld equations with an elec-
tromagnetic source term from varying the 4D metric, Maxwell's equations from varying the

eld A� and an equation of motion for the scalar eld by varying . These results can also

be obtained with a slightly dierent avor by runing the derivation with the oposite order.
Since the Kaluza-Klein action is simple the 5D Einstein Hilbert action,

                                 S~KK =         1   R~   +  L~M        g~ d5x
                                                2~

varying with respect to the 5D metric g~� will recover a 5D version of the Einstein eld

equations with exactly the same form as its 4D general relativity counterpart,

                                      R~�    -  1  R~g~�    =  ~T~�
                                                2

As before, I will restrict to 5D vacuua in which T� = 0. We shall consider the dierent

components of the Einstein eld equations. First, the 4D space-time part,

                                          R~�   -  1  R~g~�    =  0
                                                   2

gives when expanded in term of 4D quantities,

        R�  -  1         =  8G   2    F�F          -  1  g�   F     F       1
               2 Rg�         c4                       2                  +  (�  - g� )

which is the 4D Einstein eld equations with an electromagnetic energy-momentum tensor
and a strange scalar eld energy-momentum. Using the fact that,

                                 R~�  -  1  R~g~�  =0       =     R~�  =0
                                         2

by the standard trace trick then we get,

                                 R~5� = 0 =         1        3F �      =0
                                                    2 

                                                      5
For a slowly varying  eld this tells us that,
                                                     F � = 0

which is the Maxwell equations. Finally,

                   R~55 = 0  =            ��      =           1  4F    F  
                                                              4

which tells us that the electromagnetic eld is the source of this strange new scalar eld.

1.6 The Lorentz Force Law

We now want to consider the geodesics in this 5D Kaluza-Klein spacetime. In particular, we

care about the 4D projections of these trajectories. Unfortunatly, the full geodesic equation

has many many terms. Specially, we want to look at the terms contracted with ~� and
~�5. We get,

dU~ �  +  �U~ U~   +     8G   g�          2  F - A ln 2                      U~ U~ 5 + O(A3) = 0
 ds                       c4

Furthermore, the cylinder condition tells us that 5g = 0 therefore, the constant vector
� = (0, 0, 0, 0, 1) is a Killing vector so the quantity,

                                          �U~� = U~5

is conserved along geodesics. Therefore, we can write,

          dU~ �  + �U~ U~     =              8G   2           U~ 5  F  �U~   +  O(A2)
           ds                                 c4

This is the Lorentz force law if we set,

                               q                8G    U~      5
                                   =             c4

                              mc

The velocity in the compactied dimension is the charge to mass ratio of the particle!

1.7 Charge Quantization

Now we add a tad bit of quantum mechainics! We have particles constrained to a closed

periodic circle in the x5 direction. Therefore, a quantum particle cannot have an arbitrary
momentum in the x5 direction. If we want to have denite momentum (corresponding to
a state with denite charge) then we need to have a standing wave in the x5 direction.
Therefore we need to have C be an integer number of wavelengths n. Thus,

                                                    hhC
                                               = p = mU~ 5 = n

Therefore, solving for U~ 5 we arrive at a condition on the charge,


                                                        n h 8G
                                                  q=

                                                        Cc

and therefore charge is quantized in units of,


                                                         1 h 8G
                                                 qQ = C c

                                             6
