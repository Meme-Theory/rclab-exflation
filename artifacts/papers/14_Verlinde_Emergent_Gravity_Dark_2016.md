# Verlinde Emergent Gravity Dark 2016

**Source:** `14_Verlinde_Emergent_Gravity_Dark_2016.pdf`

---

arXiv:1611.02269v2 [hep-th] 8 Nov 2016                  Emergent Gravity

                                                     and the Dark Universe

                                                                                   Erik Verlinde1

                                                                   Delta-Institute for Theoretical Physics
                                                                               Institute of Physics,

                                                                           University of Amsterdam
                                                                  Science Park 904, 1090 GL Amsterdam

                                                                                 The Netherlands

                                                                                          Abstract
                                                Recent theoretical progress indicates that spacetime and gravity emerge
                                            together from the entanglement structure of an underlying microscopic theory.
                                            These ideas are best understood in Anti-de Sitter space, where they rely on the
                                            area law for entanglement entropy. The extension to de Sitter space requires
                                            taking into account the entropy and temperature associated with the cosmolog-
                                            ical horizon. Using insights from string theory, black hole physics and quantum
                                            information theory we argue that the positive dark energy leads to a thermal
                                            volume law contribution to the entropy that overtakes the area law precisely at
                                            the cosmological horizon. Due to the competition between area and volume law
                                            entanglement the microscopic de Sitter states do not thermalise at sub-Hubble
                                            scales: they exhibit memory effects in the form of an entropy displacement caused
                                            by matter. The emergent laws of gravity contain an additional `dark' gravita-
                                            tional force describing the `elastic' response due to the entropy displacement. We
                                            derive an estimate of the strength of this extra force in terms of the baryonic
                                            mass, Newton's constant and the Hubble acceleration scale a0 = cH0, and pro-
                                            vide evidence for the fact that this additional `dark gravity force' explains the
                                            observed phenomena in galaxies and clusters currently attributed to dark matter.

                                        1 [email redacted]
Contents

1 Introduction and Summary                                2

1.1 Emergent spacetime and gravity from quantum information . . . . . . . 2

1.2 Emergent gravity in de Sitter space . . . . . . . . . . . . . . . . . . . . 3

1.3 Hints from observations: the missing mass problem . . . . . . . . . . . 5

1.4 Outline: from emergent gravity to apparent dark matter . . . . . . . . 6

2 Dark Energy and the Entropy in de Sitter Space          7

2.1 De Sitter space as a data hiding quantum network . . . . . . . . . . . . 7

2.2 The entropy content of de Sitter space . . . . . . . . . . . . . . . . . . 10

2.3 Towards a string theoretic microscopic description . . . . . . . . . . . . 11

3 Glassy Dynamics and Memory Effects in Emergent Gravity  13

3.1 The glassy dynamics of emergent gravity in de Sitter space . . . . . . . 13

3.2 Memory effects and the `dark' elastic phase of emergent gravity . . . . 14

4 The Effect of Matter on the Entropy and Dark Energy     16

4.1 Entropy and entanglement reduction due to matter . . . . . . . . . . . 17

4.2 An entropic criterion for the dark phase of emergent gravity . . . . . . 18

4.3 Displacement of the entropy content of de Sitter space . . . . . . . . . 20

4.4 A heuristic derivation of the Tully-Fisher scaling relation . . . . . . . . 23

5 The First Law of Horizons and the Definition of Mass    25

5.1 Wald's formalism in de Sitter space . . . . . . . . . . . . . . . . . . . . 25

5.2 An approximate ADM definition of mass in de Sitter . . . . . . . . . . 27

6 The Elastic Phase of Emergent Gravity                   28

6.1 Linear elasticity and the definition of mass . . . . . . . . . . . . . . . . 28

6.2 The elasticity/gravity correspondence in the sub-Newtonian regime . . 30

7 Apparent Dark Matter from Emergent Gravity              33

7.1 From an elastic memory effect to apparent dark matter . . . . . . . . . 33

7.2 A formula for apparent dark matter density in galaxies and clusters . . 37

8 Discussion and Outlook                                  42

8.1 Particle dark matter versus emergent gravity . . . . . . . . . . . . . . . 42

8.2 Emergent gravity and apparent dark matter in cosmological scenarios . 43

9 Acknowledgements                                        45

                            1
1 Introduction and Summary

According to Einstein's theory of general relativity spacetime has no intrinsic properties
other than its curved geometry: it is merely a stage, albeit a dynamical one, on which
matter moves under the influence of forces. There are well motivated reasons, coming
from theory as well as observations, to challenge this conventional point of view. From
the observational side, the fact that 95% of our Universe consists of mysterious forms
of energy or matter gives sufficient motivation to reconsider this basic starting point.
And from a theoretical perspective, insights from black hole physics and string theory
indicate that our `macroscopic' notions of spacetime and gravity are emergent from an
underlying microscopic description in which they have no a priori meaning.

1.1 Emergent spacetime and gravity from quantum information

The first indication of the emergent nature of spacetime and gravity comes from
the laws of black hole thermodynamics [1]. A central role herein is played by the
Bekenstein-Hawking entropy [2, 3] and Hawking temperature [4, 5] given by

       A  and                                                (1.1)
S=             T= .
               2
      4G

Here A denotes the area of the horizon and  equals the surface acceleration. In the
past decades the theoretical understanding of the Bekenstein-Hawking formula has ad-
vanced significantly, starting with the explanation of its microscopic origin in string
theory [6] and the subsequent development of the AdS/CFT correspondence [7]. In
the latter context it was realized that this same formula also determines the amount
of quantum entanglement in the vacuum [8]. It was subsequently argued that quan-
tum entanglement plays a central role in explaining the connectivity of the classical
spacetime [9]. These important insights formed the starting point of the recent theoret-
ical advances that have revealed a deep connection between key concepts of quantum
information theory and the emergence of spacetime and gravity.

    Currently the first steps are being taken towards a new theoretical framework in
which spacetime geometry is viewed as representing the entanglement structure of the
microscopic quantum state. Gravity emerges from this quantum information theoretic
viewpoint as describing the change in entanglement caused by matter. These novel
ideas are best understood in Anti-de Sitter space, where the description in terms of a
dual conformal field theory allows one to compute the microscopic entanglement in a
well defined setting. In this way it was proven [10, 11] that the entanglement entropy
indeed obeys (1.1), when the vacuum state is divided into two parts separated by a
Killing horizon. This fact was afterwards used to extend earlier work on the emergence
of gravity [12, 13, 14] by deriving the (linearized) Einstein equations from general
quantum information theoretic principles [15, 16, 17].

          2
    The fact that the entanglement entropy of the spacetime vacuum obeys an area law
has motivated various proposals that represent spacetime as a network of entangled
units of quantum information, called `tensors'. The first proposal of this kind is the
MERA approach [18, 19] in which the boundary quantum state is (de-)constructed by
a multi-scale entanglement renormalization procedure. More recently it was proposed
that the bulk spacetime operates as a holographic error correcting code [20, 21]. In this
approach the tensor network representing the emergent spacetime produces a unitary
bulk to boundary map defined by entanglement. The language of quantum error cor-
recting codes and tensor networks gives useful insights into the entanglement structure
of spacetime. In particular, it suggests that the microscopic constituents from which
spacetime emerges should be thought of as basic units of quantum information whose
short range entanglement gives rise to the Bekenstein-Hawking area law and provides
the microscopic `bonds' or `glue' responsible for the connectivity of spacetime.

1.2 Emergent gravity in de Sitter space

The conceptual ideas behind the emergence of spacetime and gravity appear to be
general and are in principle applicable to other geometries than Anti-de Sitter space.
Our goal is to identify these general principles and apply them to a universe closer
to our own, namely de Sitter space. Here we have less theoretical control, since at
present there is no complete(ly) satisfactory microscopic description of spacetimes with
a positive cosmological constant. Our strategy will be to apply the same general logic
as in AdS, but to make appropriate adjustments to take into account the differences
that occur in dS spacetimes. The most important aspect we have to deal with is
that de Sitter space has a cosmological horizon. Hence, it carries a finite entropy and
temperature given by (1.1), where the surface acceleration  is given in terms of the
Hubble parameter H0 and Hubble scale L by [22]

              c2                         (1.2)
 = cH0 = L = a0.

The acceleration scale a0 will play a particularly important role in this paper.2
    The fact that de Sitter space has no boundary at spatial infinity casts doubt on the

possible existence of a holographic description. One may try to overcome this difficulty
by viewing dS as an analytic continuation of AdS and use a temporal version of the
holographic correspondence [23] or use the ideas of [24]. We will not adopt such a holo-
graphic approach, since we interpret the presence of the cosmological horizon and the
absence of spatial (or null) infinity as signs that the entanglement structure of de Sitter
space differs in an essential way from that of AdS (or flat space). The horizon entropy

    2In most of this paper we set c = 1, but in the later sections we take a non-relativistic limit and
write our equations in terms of a0 so that they are dimensionally correct without having to introduce c.

3
Figure 1: Two possible quantum entanglement patterns of de Sitter space with a one-sided

horizon. The entanglement between EPR pairs is represented pictorially by tiny ER-bridges.
The entanglement is long range and connects bulk excitations that carry the positive dark
energy either with the states on the horizon (left) or primarily with each other (right). Both
situations leads to a thermal volume law contribution to the entanglement entropy.

and temperature indicate that microscopically de Sitter space corresponds to a thermal
state in which part of the microscopic degrees of freedom are being `thermalized'.

    An important lesson that has come out of the complementarity, firewall [25] and
ER=EPR [26] discussions is that the quantum information counted by the Bekenstein-
Hawking entropy is not localized on the horizon itself [27], but either represents the
entanglement entropy across the horizon (two-sided case) or is interpreted as a thermo-
dynamic entropy (one-sided case) which is stored non-locally . In the latter situation,
the quantum states associated with the horizon entropy are maximally entangled with
bulk excitations carrying a typical energy set by the temperature. In this paper we will
argue that this one-sided perspective also applies to de Sitter space. Furthermore, we
propose that the thermal excitations responsible for the de Sitter entropy constitute the
positive dark energy. In this physical picture the positive dark energy and accelerated
expansion are caused by the slow thermalization of the emergent spacetime [28, 29].

    We propose that microscopically de Sitter space corresponds to an ensemble of
metastable quantum states that together carry the Bekenstein-Hawking entropy asso-
ciated with the cosmological horizon. The metastability has purely an entropic origin:
the high degeneracy together with the ultra-slow dynamics prevent the microscopic
system to relax to the true ground state. At long timescales the microscopic de Sitter
states satisfy the eigenstate thermalization hypothesis (ETH) [30, 31], which implies
that they contain a thermal volume law contribution to the entanglement entropy.

    To derive the Einstein equations one requires a strict area law for the entanglement
entropy. In condensed matter systems a strict area law arises almost exclusively in
ground states of gapped systems with strong short range correlations. A small but non-
zero volume law entropy, for instance due to thermalization, would compete with and
at large distances overwhelm the area law. We propose that precisely this phenomenon
occurs in de Sitter space and is responsible for the presence of a cosmological horizon.
Our aim is to study the emergent laws of gravity in de Sitter space while taking into
account its thermal volume law entropy.

                                                      4
1.3 Hints from observations: the missing mass problem

In this paper we provide evidence for the fact that the observed dark energy and
the phenomena currently attributed to dark matter have a common origin and are
connected to the emergent nature of spacetime and gravity. The observed flattening of
rotation curves, as well as many other observations of dark matter phenomena, indicate
that they are controlled by the Hubble acceleration scale a0, as first pointed out by
Milgrom [32]. It is an empirical fact [33, 34, 35] that the `missing mass problem',
usually interpreted as observational evidence for dark matter, only occurs when the
gravitational acceleration falls below a certain critical value that is of the order of a0.
This criterion can be alternatively formulated in terms of the surface mass density.

    Consider a spherical region with boundary area A(r) = 4r2 that contains matter
with total mass M near its center. We define the surface mass density3 (r) as the
ratio of the mass M and the area A(r). Empirically the directly observed gravitational
phenomena attributed to dark matter, such as the flattening of rotation curves in spiral
galaxies and the evidence from weak lensing data, occur when the surface mass density
falls below a universal value determined by the acceleration scale a0

(r) = M < a0 .                                           (1.3)
          A(r) 8G

The appearance of the cosmological acceleration scale a0 in galactic dynamics is strik-
ing and gives a strong hint towards an explanation in terms of emergent gravity, as
envisaged in [38]. To make this point more clear let us rewrite the above inequality as

                                   2M A(r)
SM =                                   <.                (1.4)
                                   a0 4G

The quantity on the l.h.s. represents the change in the de Sitter entropy caused by

adding the mass M , while the r.h.s. is the entropy of a black hole that would fit inside

the region bounded by the area A.

Our goal is to give a theoretical explanation for why the emergent laws of gravity

differ from those of general relativity precisely when the inequality (1.4) is obeyed.

We will find that this criterion is directly related to the presence of the volume law

contribution to the entanglement entropy. At scales much smaller than the Hubble

radius gravity is in most situations well described by general relativity, because the

entanglement entropy is still dominated by the area law of the vacuum. But at large

distances and long time scales the enormous de Sitter entropy in combination with the

extremely slow thermal dynamics lead to modifications to these familiar laws. We will

determine these modifications and show that precisely when the surface mass density

falls below the value (1.3) the reaction force due to the thermal contribution takes over

from the `normal' gravity force caused by the area law.

    3Astronomers use the `projected' surface mass density obtained by integrating the mass density
along the line of sight. Our somewhat unconventional definition is more convenient for our purposes.

                                   5
1.4 Outline: from emergent gravity to apparent dark matter

The central idea of this paper is that the volume law contribution to the entanglement
entropy, associated with the positive dark energy, turns the otherwise "stiff" geometry
of spacetime into an elastic medium. We find that the elastic response of this `dark
energy' medium takes the form of an extra `dark' gravitational force that appears to
be due to `dark matter'. For spherical situations and under the right circumstances
it is shown that the surface mass densities of the baryonic and apparent dark matter
obey the following scaling relation in d spacetime dimensions

2    MD2  =  A(r)   MB        or                     D2 (r)  =   a0 B(r) .   (1.5)
 a0          4G    d-1                                          8G d - 1

The first equation connects to the criterion (1.4) and makes the thermal and entropic

origin manifest. The second relation can alternatively be written in terms of the grav-

itational acceleration gD and gB due to the apparent dark matter and baryons, which
are related to D and B by

D    =    d  -  2   gD        and                    B  =    d  -  2   gB .  (1.6)
          d  -  3  8G                                        d  -  3  8G

Hence these accelerations obey the scaling relation

                        with                   (d - 3)                       (1.7)
gD = gBaM                          aM = (d - 2)(d - 1) a0.

In d = 4 these equations are equivalent to the baryonic Tully-Fisher relation [36] that
relates the velocity of the flattening galaxy rotation curves and the baryonic mass MB.
In this case one finds aM = a0/6, which is indeed the acceleration scale that appears in
Milgrom's phenomenological fitting formula [34, 35]. We like to emphasise that these
scaling relations are not new laws of gravity or inertia, but appear as estimates of the
strength of the extra dark gravitational force. From our derivation it will become clear
in which circumstances these relations hold, and when they are expected to fail. This
point will be further clarified in the concluding section.

    This paper is organized as follows. In section 2 we present our main hypothesis
regarding the entropy content of de Sitter space. In section 3 we discuss several con-
ceptual issues related to the glassy dynamics and memory effects that occur in emergent
de Sitter gravity. We determine the effect of matter on the entropy content in section
4, and explain the origin of the criterion (1.4). We also give a heuristic derivation of the
scaling relation (1.5). In section 5 we relate the definition of mass in de Sitter to the
reduction of the total entropy using the Wald formalism. This serves as a preparation
for section 6, where we give a detailed correspondence between the gravitational and
elastic equations. Section 7 contains the main result of our paper: here we derive the
apparent dark matter density in terms of the baryonic mass distribution and compare
our findings with known observational facts. Finally, the discussion and conclusions
are presented in section 8.

                              6
2 Dark Energy and the Entropy in de Sitter Space

The main hypothesis from which we will derive the emergent gravitational laws in
de Sitter space, and the effects that lead to phenomena attributed to dark matter, is
contained in the following two statements.

  (i) There exists a microscopic bulk perspective in which the area law for the entan-
       glement entropy is due to the short distance entanglement of neighboring degrees
       of freedom that build the emergent bulk spacetime.

 (ii) The de Sitter entropy is evenly divided over the same microscopic degrees of
       freedom that build the emergent spacetime through their entanglement, and is
       caused by the long range entanglement of part of these degrees of freedom.

We begin in subsection 2.1 by explaining these two postulates from a quantum in-
formation theoretic perspective, and by analogy with condensed matter systems. In
subsection 2.2 we will provide a quantitative description of the entropy content of de
Sitter space. We will associate the entropy with the excitations that carry the positive
dark energy. This interpretation will be motivated in subsection 2.3 by using insights
from string theory and AdS/CFT. The details of the microscopic description will not
be important for the rest of this paper. We will therefore be somewhat brief, and
postpone a detailed discussion of the microscopic perspective to a future publication.

2.1 De Sitter space as a data hiding quantum network

According to our first postulate each region of space is associated with a tensor factor
of the microscopic Hilbert space, so that the entanglement entropy obtained by tracing
over its complement satisfies an area law given by the Bekenstein-Hawking formula.
So the microscopic building blocks of spacetime are (primarily) short range entangled.
This postulate is directly motivated by the Ryu-Takanayagi formula and the tensor
network constructions of emergent spacetime [18, 20, 21], and is in direct analogy with
condensed matter systems that exhibit area law entanglement.

    A strict area law is known to hold in condensed matter systems with gapped ground
states. Indeed, we conjecture that from a microscopic bulk perspective AdS spacetimes
correspond to the gapped ground states of the underlying quantum system. The build-
ing blocks of de Sitter spacetime are, according to our second postulate, not exclusively
short range entangled, but also exhibit long range entanglement at the Hubble scale.
Again by analogy with condensed matter physics this indicates that these de Sitter
states correspond to excited energy eigenstates. Hence, the entanglement entropy con-
tains in addition to the area law also a volume law contribution. In terms of a tensor
network picture this means these states contain an amount of quantum information
which is evenly divided over all tensors in the network.

                                                      7
    This can be formulated more precisely using the language of quantum error correc-
tion. Quantum error correction is based on the principle that the quantum information
contained in k `logical' qubits can be encoded in n > k entangled `physical' qubits, in
such a way that the logical qubits can be recovered even if a subset of the physical
qubits is erased. A particularly intuitive class of error correcting codes makes use of
so-called `stabilizer conditions' [40], each of which reduces the Hilbert space of physical
qubits by a factor of 2. By imposing n - k stabilizer conditions the product Hilbert
space of n-qubits is reduced to the so-called `code subspace' in which the k logical
qubits are stored. The encoded information is robust against erasure of one or more
physical qubits, if n is much larger than k and the transition between two different
states in the code subspace requires the rearrangement of many physical qubits.

    These same principles apply to the entanglement properties of emergent spacetime.
For AdS this idea led to the construction of holographic error correcting tensor networks
[20, 21]. These networks are designed so that they describe an encoding map from the
`logical' bulk states onto the Hilbert space of `physical' boundary states [39]. The
tensors in the bulk of the network are usually not considered to be part of the space
of physical qubits, since they do not participate in storing the quantum information
associated with the logical qubits.

    With our first postulate we take an alternative point of view by regarding all these
bulk tensors as physical qubits, and interpreting the short distance entanglement im-
posed by the network as being due to stabilizer conditions. Schematically, the Hilbert
states of physical qubits are of the form

   |Vx  H         with   |Vx =  Vx... | | | � � �      (2.8)

x                               ,,,...

where x runs over all vertices of the network, and , , , . . . represent indices with a

certain finite range D. In a holographic tensor network the stabilizer conditions are so

restrictive that the bulk qubits are put into a unique `stabilizer state' |0 , obtained by

maximally entangling all bulk indices with neighbouring tensors. Again schematically,

                                        1D
|0 = |xy          where     |xy =             | x| y.  (2.9)
                                        D =1
              xy

The Hilbert space of logical qubits is generated by local bulk operators that act on
individual tensors. The network defines a unitary encoding map from the logical bulk
qubits to the physical boundary qubits, by `pushing' the bulk operators through the
network and representing them as boundary operators. For this one makes use of the
fact that the bulk states are maximally entangled with the boundary states [20, 21].
This can only be achieved if the entanglement entropy in the bulk obeys an area law.
In other words, area law entanglement is a necessary condition for a holographic map
from the bulk to the boundary. The negative curvature is also crucial for a holographic
description, since it ensures that after tracing out the auxiliary tensors in the network,

                         8
bulk excitations remain maximally entangled with the boundary.
    Thermal excitations compete with the boundary state for the entanglement of other

bulk excitations. An individual excitation can lose its entanglement connection with
the boundary by becoming maximally entangled with other bulk excitations. Sim-
ply stated: if the excited bulk states contain more information than the number of
boundary states, the bulk states take over the entanglement and the holographic cor-
respondence breaks down. This statement holds in every part of the network, and is
equivalent to the holographic bound: it puts a limit on how much information can be
contained in bulk excitations before the network loses its holographic properties.

    Our second postulate states that the quantum information measured by the area of
de Sitter horizon spreads over all physical qubits in the bulk and hence becomes delo-
calized into the long range correlations of the microscopic quantum state of the tensor
network. By relaxing the stabilizer conditions, the quantum state of all bulk tensors
is allowed to occupy a set of states |I with a non-zero entropy density. Concretely
this means that the tensors not only carry short range entanglement, but contain some
indices that participate in the long range entanglement as well. The code subspace is
thus contained in the microscopic bulk Hilbert space instead of the boundary Hilbert
space. Since the quantum information is shared by all tensors, it is protected against
disturbances created by local bulk operators, and therefore remains hidden for bulk
observers. These delocalized states are counted by the de Sitter entropy, and contain
the extremely low energy excitations that are responsible for the positive dark energy.

    When the volume becomes larger, due to the positive curvature of de Sitter space,
the total quantum information stored by the collective state of the bulk tensors even-
tually exceeds the holographic bound. At that moment the bulk states take over
the entanglement, and local bulk operators are no longer mapped holographically to
boundary operators. The breakdown of the area law entanglement at the horizon thus
implies that de Sitter space does not have a holographic description at the horizon.
The would-be horizon states themselves become maximally entangled with the thermal
excitations that carry the volume law entropy. As a result they become delocalized
and are spread over the entangled degrees of freedom that build the bulk spacetime.
Note that these arguments are closely related to the discussions that led to the fire-
wall paradox [25], EPR=ER proposal [26] and the ideas of fast scrambling [29] and
computational complexity [41]. The size of the Hilbert space of bulk states is exactly
given by the horizon area, since this is where the volume law exceeds the area law
entanglement entropy. In other words, de Sitter space contains exactly the limit of its
storage capacity determined by the horizon area. In the condensed matter analogy, the
breakdown of holography corresponds to a localization/de-localization transition [48]
from the localized boundary states into delocalized states that occupy the bulk.

                                                      9
2.2 The entropy content of de Sitter space

Next we give a quantitative description of the entropy content of de Sitter space for
the static coordinate patch described by the metric

                                   ds2 = -f (r)dt2 + dr2 + r2d2                  (2.10)
                                                           f (r)                 (2.11)

where the function f (r) is given by
                                                             r2

                                             f (r) = 1 - .
                                                            L2

We take the perspective of an observer near the origin r = 0, so that the edge of his

causal domain coincides with the horizon at r = L. The horizon entropy equals

              A(L)                   with         A(L) = d-2Ld-2,                (2.12)
SDE(L) = 4G

where d-2 is the volume of a (d - 2)-dimensional unit sphere. Our hypothesis is that
this entropy is evenly distributed over microscopic degrees of freedom that make up

the bulk spacetime. To determine the entropy density we view the spatial section at

t = 0 as a ball with radius L bounded by the horizon. The total de Sitter entropy is

divided over this volume so that a ball of radius r centered around the origin contains

an entropy SDE(r) proportional to its volume

            1     (r)                                                d-2  rd-1   (2.13)
SDE (r)  =     V                     with         V      (r)      =           .
            V0                                                       d-1

The subscript DE indicates that the entropy is carried by excitations of the microscopic

degrees of freedom that lift the negative ground state energy to the positive value

associated with the dark energy. This point will be further explained below.

    The value of the volume V0 per unit of entropy follows from the requirement that
the total entropy SDE(L), where we put r = L, equals the Bekenstein-Hawking entropy
associated with the cosmological horizon. By comparing (2.13) for r = L with (2.12)

one obtains that V0 takes the value

                                            4G L                                 (2.14)
                                     V0 = d - 1

where the factor (d-1)/L originates from the relative normalization of the horizon area

A(L) and the volume V (L). This entropy density is thus determined by the Planck

area and the Hubble scale. In fact, this value of the entropy density has been proposed

as a holographic upper bound in a cosmological setting.

An alternative way to write the entropy SDE(r) is in terms of the area A(r) as

             r A(r)                  with         A(r) = d-2rd-2.                (2.15)
SDE(r) = L 4G

From this expression it is immediately clear that when we put r = L we recover the

Bekenstein-Hawking entropy (2.12).

                                     10
2.3 Towards a string theoretic microscopic description

We now like to give a more string theoretic interpretation of these formulas and also
further motivate why we associate this entropy with the positive dark energy. For this
purpose it will be useful to make a comparison between de Sitter space with radius L
and a subregion of AdS that precisely fits in one AdS radius L. We can write the AdS
metric in the same form as (2.10) except with f (r) = 1 + r2/L2. For AdS it is known
[7, 42] that the number of quantum mechanical degrees of freedom associated with a
single region of size L is determined by the central charge of the CFT

          C(L) =  A(L)  = # of degrees of freedom.          (2.16)

                  16G

This is the analogue of the famous Brown-Henneaux formula [43]: for AdS3/CFT2 it
equals c/24, while in other dimensions it is the central charge defined via the two-point
functions of the stress tensor. In string theory these degrees of freedom describe a
matrix or quiver quantum mechanics obtained by dimensional reduction of the CFT.

    We postulated that A(L)/4G corresponds to the entanglement entropy of the
vacuum state when we divide the state into two subsystems inside and outside of the
single AdS regions. This quantity can also be computed in the boundary CFT, where it
corresponds to the so-called `differential entropy' [44]. To obtain this result as a genuine
entanglement entropy one has to extend the microscopic Hilbert space by associating
to each AdS region a tensor factor. This tensor factor represents the Hilbert space of
the (virtual) excitations of the C(L) quantum mechanical degrees of freedom.

    Let us compute the `vacuum' energy in (A)dS contained inside a sphere of radius r

               (d - 1)(d - 2)             r d-1 d - 2       (2.17)
E(A)dS(r) = �                  V (r) = �             C(L).
                  16GL2                       L  L

The negative vacuum energy in AdS can be understood as the Casimir energy as-
sociated with the number of microscopic degrees of freedom; indeed, this is what it
corresponds to in the CFT. We interpret the positive dark energy in de Sitter space as
the excitation energy that lifts the vacuum energy from its ground state value. To mo-
tivate this assumption, let us give a heuristic derivation of the entropy of de Sitter space
as follows. Let us take r = L and write the `vacuum' energy for AdS in terms of C(L) as

                                   d-2
                  EAdS(L) = -           C(L).               (2.18)
                                   L

For dS we write the `vacuum' energy in a similar way in terms of the number of

excitations N (L) of energy (d - 2)/L that have been added to the ground state

EdS(L) =  d-2                      where         N (L) = 2 C(L). (2.19)
                N (L) - C(L)
          L

We now label the microscopic states by all possible ways in which the N (L) excitations
can be distributed over the C(L) degrees of freedom. The computation of the entropy

                               11
then reduces to a familiar combinatoric problem, whose answer is given by the Hardy-
Ramanujan formula4

SDE(L) = 4 C(L) N (L) - C(L) .                                                (2.20)

One easily verifies that this agrees with (2.12). From a string theoretic perspective this
indicates that the C(L) microscopic degrees of freedom live entirely on the so-called
Higgs branch of the underlying matrix or quiver quantum mechanics.

    These C(L) quantum mechanical degrees of freedom do not suffice to explain the
area law entanglement at sub-AdS scales. For this it is necessary to extend the Hilbert
space even further by introducing additional auxiliary degrees of freedom that represent
additional tensor factors for much smaller regions, say of size <L. The total number
of degrees of freedom has increased by a factor L/ and equals

Ld-1 A( )                                                                     (2.21)
                   = # of auxiliary degrees of freedom.

 d-1 16G

In the tensor network represents the spacing between the vertices of a fine grained net-
work, while in the quiver matrix quantum mechanics one can view as the `fractional
string scale' of a fine grained matrix quiver quantum mechanics model. The precise
value of the UV scale turns out to be unimportant for the macroscopic description of
the emergent spacetime. For instance, in the tensor network one can combine several
tensors to form a larger tensor without changing the large scale entanglement proper-
ties, while in the string theoretic description one can view as the `fractional string
scale' of a fine grained matrix quiver quantum mechanics model.

    By increasing the number of degrees of freedom by a factor L/ one also has in-
creased the energy gap required to excite a single auxiliary degree of freedom with the
same factor. Hence, instead of (d - 2)/L the energy gap is now equal to (d - 2)/ .
This means that the number of excitations has decreased by a factor /L, since the
total energy has remained the same. One can show that this combined operation leaves
the total entropy SDE(L) invariant. In string theory this procedure is known as the
`fractional string' picture, which is the inverse of the `long string phenomenon'. Each
region of size in de Sitter space contains a fraction ( /L)d-1 of the total number
of auxiliary degrees of freedom, as well as a fraction ( /L)d-1 of the total number of
excitations. This means it also carries a fraction ( /L)d-1 of the total entropy

               A( )                                                           (2.22)
SDE( ) = L 4G .

Since the scale can be chosen freely, we learn that the entropy content of a spherical

region with arbitrary radius r is found by putting = r in (2.22). A more detailed

discussion of this string theoretic perspective will be presented elsewhere.

    4 The result (2.20) looks identical to the Cardy formula, but does not require the existence of
2d-CFT. Similar expressions for the holographic entropy have been found in [45, 46].

12
3 Glassy Dynamics and Memory Effects in Emergent Gravity

In this section we address an important conceptual question. How can a theory of
emergent gravity lead to observable consequences at astronomical and cosmological
scales? We also discuss important features of the microscopic de Sitter states such
as their glassy behaviour and occurrence of memory effects. These phenomena play a
central role in our derivation of the emergent laws of gravity at large scales.

3.1 The glassy dynamics of emergent gravity in de Sitter space

The idea that emergent gravity has observational consequences at cosmological scales
may be counter-intuitive and appears to be at odds with the common believe that
effective field theory gives a reliable description of all infrared physics. With the fol-
lowing discussion we like to point out a loophole in this common wisdom. In short, the
standard arguments overlook the fact that it is logically possible that the laws which
govern the long time and distance scale dynamics in our universe are decoupled from
the emergent local laws of physics described by our current effective field theories.

    The physics that drives the evolution of our universe at large scales is, according
to our proposal, hidden in the slow dynamics of a large number of delocalized states
whose degeneracy, presence and dynamics are invisible at small scales. Together these
states carry the de Sitter entropy, but they store this information in a non-local way.
So our universe contains a large amount of quantum information in extremely long
range correlations of the underlying microscopic degrees of freedom. The present local
laws of physics are not capable of detecting or describing these delocalized states.

    The basic principle that prevents a local observer from accessing these states is
similar to the way a quantum computer protects its quantum information from local
disturbances. It is also analogous to the slow dynamics of a glassy system that is
unobservable on human timescales. At short observation times a glassy state is indis-
tinguishable from a crystalline state, and its effective description would be identical.
Its long timescale dynamics, however, differs drastically. Glassy systems exhibit exotic
long timescale behavior such as slow relaxation, aging and memory effects. At the
glass transition the fast short distance degrees of freedom fall out of equilibrium, while
the slow long distance dynamics remains ergodic. Therefore, the long time phenomena
of a glassy system cannot be derived from the same effective description as the short
time behavior, since the latter is identical to that of the crystalline state. To develop
an effective theory for the slow dynamics of a glassy state one has to go back to the
microscopic description and properly understand the origin of its glassy behavior.

    We propose that microscopically the same physical picture applies to our universe.
De Sitter space behaves as a glassy system with a very high information density that is
slowly being manipulated by the microscopic dynamics. The short range `entanglement
bonds' between the microscopic degrees of freedom, which give rise to the area law

                                                      13
entanglement entropy, are very hard to change without either invoking extremely high
energies or having to overcome huge entropic barriers. The slow dynamics together
with the large degeneracy causes the microscopic states to remain trapped in a local
minimum of an extremely large free energy landscape. Quantum mechanically this
means these states violate ETH at short distance and time scales. We believe this can
be understood as a manifestation of many-body localization: a quantum analogue of
the glass transition known to imply area law entanglement [47, 48].

3.2 Memory effects and the `dark' elastic phase of emergent gravity

Matter normally arises by adding excitations to the ground state. In our description of
de Sitter space there is an alternative possibility, since it already contains delocalized
excitations that constitute the dark energy. Matter particles correspond to localized
excitations. Hence, it is natural to assume that at some moment in the cosmological
evolution these localized excitations appeared via some transition in the delocalized
dark energy excitations. The string theoretic perspective described in section 2.3 sug-
gests that the dark energy excitations are the basic constituents in our universe. Matter
particles correspond to bound states of these basic excitations, that have escaped the
dark energy medium. In string theory jargon these degrees of freedom have escaped
from the `Higgs branch' onto the `Coulomb branch'.

    The dark energy medium corresponds to the entropic phase in which the excitations
distribute themselves freely over all available degrees of freedom: this is known as the
Higgs branch. Particles correspond to bound states that can move freely in the vacuum
spacetime. These excitations live on the Coulomb branch and carry a much smaller
entropy. Hence, the transition from dark energy to matter particles is associated with
a reduction of the energy and entropy content of the dark energy medium.

    After the transition the total system contains a dark energy component as well
as localized particle states. This means that the microscopic theory corresponds to a
matrix or quiver quantum mechanics that is in a mixed Coulomb-Higgs phase.5 We
are interested in the question how the forces that act on the particles on the Coulomb
branch are influenced by the presence of the excitations on the Higgs branch. Instead
of trying to solve this problem using a microscopic description, we will use an effective
macroscopic description based on general physics arguments.

    The transition by which matter appeared has removed an amount of energy and
entropy from the underlying microscopic state. The resulting redistribution of the
entropy density with respect to its equilibrium position is described by a displacement
vector ui. Since we have a system with a non-zero temperature, the displacement of
entropy leads to a change in the free energy density. The effective theory that describes
the response due to the displacement of the free energy density already exists for a long
time, and is older than general relativity itself: it is the theory of elasticity.

    5The possibility of a mixed Higgs-Coulomb branch in matrix QM was first pointed out in [49].

                                                      14
Figure 2: In AdS (left) the entanglement entropy obeys a strict area law and all information

is stored on the boundary. In dS (right) the information delocalizes into the bulk volume.
Only in dS the matter creates a memory effect in the dark energy medium by removing the
entropy from an inclusion region.

    As we have argued, due to the competition between the area law and volume law
entanglement, the microscopic de Sitter states exhibit glassy behavior leading to slow
relaxation and memory effects. For our problem this means the displacement of the
local entropy density due to matter is not immediately erased, but leaves behind a
memory imprint in the underlying quantum state. This results in a residual strain and
stress in the dark energy medium, which can only relax very slowly.

    In our calculations we will make use of concepts and methods that have been de-
veloped in totally different contexts: the first is the study by Eshelby [58] of residual
strain and stress that occur in manufactured metals that undergo a martensite tran-
sition in small regions (called `inclusions'). The second is a computation by Deutsch
[59] of memory effects due to the microscopic dynamics of entangled polymer melts. In
all these situations the elastic stress originates from a transition that has occurred in
part of the medium, without the system being able to relax to a stress-free state due
to the slow `arrested' dynamics of the microscopic state and its enormous degeneracy.

    The fact that matter causes a displacement of the dark energy medium implies
that the medium also causes a reaction force on the matter. The magnitude of this
elastic force is determined in terms of the residual elastic strain and stress. We propose
that this force leads to the excess gravity that is currently attributed to dark matter.
Indeed, we will show that the observed relationship between the surface mass densities
of the apparent dark matter and the baryonic matter naturally follows by applying old
and well-known elements of the (linear) theory of elasticity. The main input that we
need to determine the residual strain and stress is the amount of entropy SM that is
removed by matter.

    In the following section we make use of our knowledge of emergent gravity in Anti-
de Sitter space (and flat space) to determine how much entropy is associated with a
mass M . The basic idea is that in these situations the underlying quantum state only

                                                      15
Figure 3: The Penrose diagram of global de Sitter space with a mass in the center of the

static patch. The global solution requires that an equal mass is put at the anti-podal point.

carries area law entanglement. Hence, we can determine the entropy SM associated
with the mass M by studying first the effect of matter on the area entanglement using
general relativity. Once we know this amount, we subsequently apply this in de Sitter
space to determine the reduction of the entropy density. From there it becomes a
straightforward application of linear elasticity to derive the stress and the elastic force.

    To derive the strength of this dark gravitational force we assume that a transition
occurs in the medium by which a certain amount SM of the entropy is being removed
from the underlying microscopic state locally inside a certain region VM . Following
[58] we will refer to the region VM as the `inclusion'. It is surrounded by the original
medium, which will be called the `matrix'.

4 The Effect of Matter on the Entropy and Dark Energy

In this section we determine the effect of matter on the entropy content in de Sitter
space. First we will determine the change in the total de Sitter entropy when matter
with a total mass M is added at or near the center of the causal domain. After that
we also derive an estimate of the change in the entanglement entropy by computing
the deficit in (growth of the) the area as a function of distance. We will find that this
quantity is directly related to the ADM and Brown-York definitions of mass in general
relativity. We subsequently determine the reduction of the entropy content of de Sitter
space within a radius r due to (the appearance of) matter and compute the resulting
displacement field. Using an analogy with the theory of elasticity we then present a
heuristic derivation of the Tully-Fisher scaling law.

                                                      16
4.1 Entropy and entanglement reduction due to matter

We start by showing that adding matter to de Sitter space decreases its entropy content.
This fact is of central importance to our arguments in this and the next sections. In
the global two sided perspective on de Sitter space the Bekenstein-Hawking entropy
of the horizon can be interpreted as quantifying the amount of entanglement between
the two static patches on opposite sides of the horizon. As depicted in figure 3, the
addition of a mass M on one side of the horizon needs to be accompanied an identical
mass M on the other side, if the metric outside of the masses is to be described by the
de Sitter-Schwarzschild solution. This metric still takes the form (2.10) but with

               r2      where         (r) = -  8GM              .  (4.23)
f (r) = 1 - + 2(r)
                                              (d - 2)d-2 rd-3
              L2

is the Newton potential due the mass M . The horizon is located at the radius r at
which f (r) = 0. Without the mass M the horizon is located at r = L and the total
entropy associated with de Sitter space is given by (2.12). To determine the change in
entropy due the addition of the mass M we calculate the displacement of the location
of the horizon. In the approximation (L) << 1 one finds that it is displaced from its
initial value L to the new value

L  L + u(L)            with          u(L) = (L)L.                 (4.24)

Note that the displacement is negative, u(L) < 0, hence the horizon size is being
reduced by the addition of the mass M . As a result, the total de Sitter entropy
changes by a negative amount SM (L) given by

                       d A(L)        =-  2M L                     (4.25)
SM (L)              =  u(L)
                             dL  4G

where in the last step we inserted the explicit expression for the Newtonian potential.
    This entropy change corresponds to a reduction of the amount of entanglement be-

tween the two sides of the horizon due the addition of the mass M . Apparently, adding
matter to spacetime reduces the amount of entanglement entropy. Our interpretation
of general relativity and the Einstein equations is that it describes the response of the
area law entanglement of the vacuum spacetime to matter. To get a better under-
standing of the relationship between the reduction of the entanglement and the total
de Sitter entropy, let us calculate the effect of matter on the area of regions that are
much smaller than the horizon. Hence we now take r << L, so that we can drop the
term r2/L2 in the metric. As we will now show, the mass reduces the growth rate
of the area as a function of the geodesic distance. This fact is directly related to the
ADM and Brown-York [54] definitions of mass in general relativity, as emphasized by
Brewin [55].

                                 17
    So let us compare the increase of the area as a function of the geodesic distance in
the situation with and without the mass. To match the two geometries we take spheres
with equal area, hence the same value of r. Without the mass the geodesic distance
is equal to r, while in the presence of the mass M a small increment dr leads to an
increase in the geodesic distance ds, since dr = (1 + (r))ds, as is easily verified from
the Schwarzschild metric. It then follows that

       d A(r) M=0             d A(r)           2M                 (4.26)
                   = (r)                   =- .
       ds 4G M=0             dr 4G

The notation on the l.h.s. indicates that we are taking the difference between the
situations with and without the mass.

    We reinterpret (4.26) as an equation for the amount of entanglement entropy SM (r)
that the mass M takes away from a spherical region with size r. This quantity is
somewhat tricky to define, since one has to specify how to identify the two geometries
with and without the mass. To circumvent this issue we define SM (r) through its
derivative with respect to r, which we identify with the left hand side of equation
(4.26). In other words, we propose that the following relation holds

       dSM (r)            =     2M     .                          (4.27)
                              -
                   dr

Here we used the fact that in the weak gravity regime the increase in geodesic distance

ds and dr are approximately equal. Now note that by integrating this equation one

finds                         2M r

       SM (r) = -                      ,                          (4.28)

which up to a sign is the familiar Bekenstein bound [56], which together with the re-
sults of [57] suggests that the definition of mass in emergent gravity is given in terms of
relative entropy. We conclude that the mass M reduces the amount of entanglement en-
tropy of the surrounding spacetime by SM (r). This happens in all spacetimes, whether
it is AdS, flat space or de Sitter, hence it is logically different from the reduction of
the total de Sitter entropy. Nevertheless, the results agree: when we put r = L we
reproduce the change of the de Sitter entropy (4.25). We find that the mass M reduces
the entanglement entropy of the region with radius r by a fraction r/L of SM (L).

4.2 An entropic criterion for the dark phase of emergent gravity

Consider a spherical region with radius r that is close to the center of the de Sitter
static patch. According to our hypothesis in section 2 the de Sitter entropy inside a
spherical region with radius r is given by

                       1         =  r A(r)  .
       SDE (r)     =      V (r)                                   (4.29)
                       V0           L  4G

                          18
Figure 4: The one-sided perspective on de Sitter space with a mass M in the center. The

entropy associated with the horizon area is contained in delocalized states that occupy the bulk.
The mass M removes part of, and therefore displaces, the entropy content in the interior.

Note that the same factor r/L appears in this expression as in the ratio between the

removed entropy SM (r) within a radius r and the total removed entropy SM (L). This
observation has an important consequence and allows us to re-express the criterion

mentioned in the introduction that separates the regimes where the `missing mass'

becomes visible. We can now reformulate this criterion as a condition on the ratio

between the removed entropy SM (r) and the entropy content SDE(r) of the dark energy.
Concretely, the condition that 2M L/ is either smaller or larger than A/4G implies

that                                        2M r r A(r)

      SM (r)  SDE(r)              or                 L 4G .      (4.30)

We can re-express this criterion as a condition on the volume VM (r) that contains the
same amount of entropy that is taken away by the mass M inside a sphere of radius r.

This volume is given by

                     1                with      V0  =  4G L      (4.31)
      SM (r) = - V0 VM (r)                                    .
                                                       d-1

The criterion (4.30) then becomes equivalent to the statement that the ratio of the
volume VM (r) and the volume V (r) of the ball of radius r is smaller or larger than one

                         M (r)    VM (r)    1.                   (4.32)
                                  V (r)

The observations on galaxy rotation curves therefore tell us that the nature of gravity
changes depending on whether matter removes all or just a fraction of the entropy

                                  19
content of de Sitter. One finds that the volume VM (r) is given by

                       8G M r
             VM (r) =             .                                        (4.33)
                       a0  d-1

Here we replaced the Hubble length L by the acceleration scale a0 to arrive at a formula
that is dimensionally correct. In other words, this volume does not depend on or c.
In fact, as we will see, the elastic description that we are about to present only depends
on the constants G and a0 and hence naturally contains precisely those parameters that
are observed in the phenomena attributed to dark matter.

    A related comment is that the ratio M (r) can be used to determine the value of
the surface mass density M (r) = M/A(r) in terms of a0 and G via

                        8G                                                 (4.34)
             M (r) = a0 M (r).

This relation follows immediately by inserting the expressions (4.31) and the result
(4.28) for the removed entropy SM (r) into (4.32). We also reinstated factors of the
speed of light to obtain an expression that is dimensionally correct. The regime where
SM (r) < SDE(r) corresponds to M (r) < 1, hence in this regime we are dealing with
low surface mass density and low gravitational acceleration. For this reason it will be
referred to as the `sub-Newtonian' or `dark gravity' regime.

4.3 Displacement of the entropy content of de Sitter space

In the regime where only part of the de Sitter entropy is removed by matter, the

remaining entropy contained in the delocalized de Sitter states starts to have a non-

negligible effect. This leads to modifications to the usual gravitational laws, since the

latter only take into account the effect of the area law entanglement. To determine

these modifications we have to keep track of the displacement of the entropy content

due to matter. In the present context, where we are dealing with a central mass M

we can represent this displacement as a scalar function u(r) that keeps track of the

distance over which the information is displaced in the radial direction.

In an elastic medium one encounters a purely radial displacement u(r) when one

removes (or adds) a certain amount of the medium in a symmetric way from inside

a spherical region. The value of the displacement field u(r) determines how much of

the medium has been removed. If we assume that the medium outside of the region

where the volume is removed is incompressible, the change in volume is given by that

of a thin shell with thickness u(r) and area A(r). The sign of u(r) determines whether

the change in volume was positive or negative. We further assume that the change in

volume is proportional to the removed entropy SM (r). In this way we obtain a relation

of the form               1
             SM (r) = V0 u(r)A(r)
                                                                           (4.35)

                       20
Figure 5: When a certain amount of volume V0 is being removed from an incompressible

elastic medium it leads to a displacement u(r) = -V0/A(r).

where the volume V0 is assumed to be of the same order as the volume V0 per unit of
entropy. To determine the value of V0 we impose that at the horizon the displacement
u(L) is identified with the shift of the position of the horizon: u(L) = (L)/a0. From

the fact that the removed entropy SM (r) is linear in r we deduce that the displacement
u(r) falls off like 1/rd-3 just like Newton's potential (r). This means that at an

arbitrary radius r we can express u(r) in terms of (r) as

                   u(r) = (r)L.                           (4.36)

By combining the expressions (4.28) and (4.36) and inserting the explicit form of the
Newtonian potential (4.23) one finds that the volume V0 is slightly larger than V0

V0  =  4G L        hence         V0 = d - 1 .             (4.37)
       d-2                       V0 d - 2

The total removed volume is therefore slightly larger than VM (r) by the same factor.
We will denote the volume that has been removed from inside a spherial region B(r)
by VM (r). The displacement u(r) can thus be written as

u(r) = - VM (r)    where         VM (r)  =  8G M r     .  (4.38)
             A(r)                            a0 d - 2

The relative factor between VM (r) and VM (r) can be directly traced back to the fact
that we are dealing with a transition from area law to volume law entanglement.

    In a elastic medium a displacement field leads to an elastic strain and corresponding
stress, which in general are described by tensor valued fields. For the present discussion
we are only interested in the normal components of the strain and the stress, hence to

                   21
simplify our notation we will suppress tensor indices and denote the normal strain and
normal stress simply by (r) and (r). Our proposed explanation of the gravitational
phenomena associated to `dark matter' is that in the regime where only part of the
entropy is removed, that is where M (r) < 1, the remaining entropy associated to the
dark energy behaves as an incompressible elastic medium. Specifically, we propose that
the entropy SM (r) is only removed from a local inclusion region VM (r) with volume
VM (r). We represent the region VM (r) as the intersection of a fixed region VM (L) with
a ball B(r) with radius r centered around the origin,

VM (r) = VM (L)  B(r).  (4.39)

The precise shape or topology of the region VM (L) will not be important for our
discussion.

    To deal with the fact that the removed volume VM (r) depends on the radius r, we
make use of the linearity of elasticity to decompose the region VM (r) in small ball-
shaped regions Bi with volume NiV0. From each Bi a fixed volume NiV0 has been
removed corresponding to Ni units of entropy. We first determine the displacement for
each region, and then compute the total displacement by adding the different contri-

butions.

    Let us consider the displacement field u(r) resulting from the removal of a vol-
ume N V0 from a single ball-shaped region B0 with volume N V0. For simplicity and
definiteness, let us assume that B0 is centered at the origin of de Sitter space. The
displacement field outside of B0 is given by

u(r) = - N V0 .         (4.40)
            A(r)

The normal strain (r) corresponds to the r-r component of the strain tensor and is
given by the radial derivative (r) = u (r). Hence

(r) = N V0 .            (4.41)
         V (r)

Here we absorbed a factor (d - 2)/(d - 1) by making the substitution V0  V0. Since
the volume of B0 is equal to N V0, we find that the normal strain (r) at its boundary
is precisely equal to one. Note that to obtain this natural result we made use of the
specific ratio of V0 and V0.

    This same calculation can be performed for each small ball Bi and leads to a dis-
placement field ui and strain i identical to (4.40) and (4.41) where the radius is defined
with respect to the center of Bi and the number of units of removed entropy is equal
to Ni. By adding all these different contributions we can in principle determine the
total displacement and strain due to the removal of the entropy SM (r) from the region
VM . Here we have to distinguish two regimes. When VM (r) > V (r) we are inside the

22
region VM and `all the available volume' has been removed. This means, the entropy
reduction due to the mass is larger than the available thermal entropy. In this region

the response to the entropy reduction due to the mass M is controlled by the area law

entanglement, which leads to the usual gravity laws. We are interested in the other

regime where VM (r) < V (r), since this is where the modifications due to the volume
law will appear.

    The total amount of entropy that is removed within a radius r is equal to SM (r).
Hence, at first we may simply try to replace N by SM (r) so that the removed volume
N V0 becomes equal to VM (r), and N V0 to the volume VM (r) of the region VM (r).
Indeed, if we make the substitutions

                N V0 - VM (r)  and            N V0 - VM (r)             (4.42)

the displacement u(r) becomes equal to (4.38) and the expression (4.41) for (r) be-

comes identical to the quantity M (r) introduced in (4.32). In other words, we find
that the apparent DM criterion can be interpreted as a condition on the normal elas-

tic strain (r): the transition from standard Newtonian gravity to the apparent dark

matter regime occurs when the elastic strain drops in value below one.

The quantity (r), as we have now defined it, equals the normal strain in the regime

where the removed volume is kept constant: in other words, where the medium is

treated as incompressible. As we will explain in more detail in section 7, in this regime

the normal strain (r) determines the value of the apparent surface mass density (r)

precisely through the relation (4.34), which for convenience we repeat here in slightly

different form                 (r) = a0 (r).
                                         8G
                                                                        (4.43)

In the next subsection we will use this relation to determine the apparent surface mass

density in the regime (r) < 1. Here the volume VM (r) is smaller than the volume
V (r) of the sphere with radius r. Hence, it is not clear anymore that one can simply

take the relation (4.41) and make the substitution (4.42). A more precise derivation

would involve adding all these separate contributions of the small balls Bi that together
compose the region VM (r). We will now show that this leads through the relation (4.43)
to a surface mass density that includes the contribution of the apparent dark matter.

4.4 A heuristic derivation of the Tully-Fisher scaling relation

After having introduced all relevant quantities, we are now ready to present our pro-
posed explanation of the observed phenomena attributed with dark matter. It is based
on the idea that the standard laws of Newton and general relativity describe the re-
sponse of the area law entanglement to matter, while in the regime (r) < 1 the gravi-
tational force is dominated by the elastic response due to the volume law contribution.
We will show that the Tully-Fisher scaling law for the surface mass densities of the

                               23
apparent dark matter and the baryonic matter is derived from a quantitive estimate of

the strain and stress caused by the entropy SM (r) removed by matter.
    Let us go back to the result (4.41) for the strain outside a small region B0 of size

N V0, and let us compute the integral of the square 2(r) over the region outside of B0
with V (r) > N V0. We denote this region as the complement B0 of the ball B0. The
integral is easy to perform and simply gives the volume of the region B0 from which
the entropy was removed

                                                         N V0  2                 (4.44)
                                                          V
                      2(r)A(r)dr =                              dV = N V0.

                  B0          N V0

This result is well known in the theory of `elastic inclusions' [58]. In this context

equation (4.44) is used to estimate the elastic energy caused by the presence of the

inclusion. This same method has also been applied to calculate memory effects in

entangled polymer melts [60].

    We can repeat this calculation for all the small balls Bi that together make up the
region VM (r) to show that the integral of i2 over the region outside of Bi is given by
NiV0. Since i quickly falls off like 1/r(d-1) with the distance from the center, the main
contribution to the integral comes from the neighbourhood of Bi. We now assume
that, in the regime where VM (r) < V (r), all the small regions Bi are disjoint, and are
separated enough in distance so that the elastic strain i for each ball Bi is primarily
localized in its own neighbourhood. This means that the integral of the square of the
total strain is equal to the sum of the contributions of the individual squares i2 for all
the balls Bi. In other words, the cross terms between i and j can be ignored when
i = j. In section 7 we will show that this can be proven to hold exactly. The integral of
2 over the ball B(r) with radius r thus decomposes into a sum of contributions coming

from the neighbourhoods of each small region Bi

         2dV          2i dV                              i2dV =  NiV0 = VM (r).  (4.45)

B(r)           i  BiB(r)      BiB(r) Bi                          BiB(r)

Each of these integrals is to a good approximation equal to the volume NiV0 of Bi,
and since these together constitute the region VM , we find that the total sum gives the
volume VM (r). We will further make the simplifying assumption that in the spherically
symmetric situation the resulting strain is just a function of the radius r. In this way

we find                     r

                           2(r )A(r )dr = VM (r).                                (4.46)

                          0

To arrive at the Tully-Fisher scaling relation between the surface mass density of the

apparent dark matter and the baryonic dark matter we differentiate this expression

with respect to the radius. If we assume that the mass distribution is well localised

                              24
near the origin, we can treat the mass M as a constant. In that case we obtain

      2(r) = 1 dVM (r) = 1 8G M                                                 (4.47)
              A(r) dr        A(r) a0 d - 1

We now make the identification of the apparent surface mass density with (r). We
obtain a relationship for the square surface mass density of the apparent dark matter
and surface mass density of the visible baryonic matter. To distinguish the apparent
surface mass density from the one defined in terms of the mass M we will denote the
first as D and the latter as B. These quantities are defined as

          a0  (r)                                         B(r) =  M             (4.48)
D(r)  =  8G             and                                             .
                                                                  A(r)

With these definitions we precisely recover the relation

              D(r)2  =   a0  B(r) .                                             (4.49)
                        8G   d-1

which was shown to be equivalent to the Tully-Fisher relation.
    In the remainder of this paper we will again go over the arguments that lead us

to the proposed elastic phase of emergent de Sitter gravity and further develop the
correspondence between the familiar gravity laws and the tensorial description of the
elastic phase. In particular, we will clarify the relation between the elastic strain and
stress and the apparent surface mass density. We will also revisit the derivation of
the Tully-Fisher scaling relations and present the details of the calculation at a less
heuristic level. This will clarify under what assumptions and conditions this relation
is expected to hold.

5 The First Law of Horizons and the Definition of Mass

Our goal in this section is to understand the reduction of the de Sitter entropy due to
matter in more detail. For this purpose we will make use of Wald's formalism [50] and
methods similar to those developed in [15, 16, 17] for the derivation of the (linearized)
Einstein equations from the area law entanglement. We will generalise some of these
methods to de Sitter space and discuss the modifications that occur in this context.
Our presentation closely follows that of Jacobson [17].

5.1 Wald's formalism in de Sitter space

In Wald's formalism [50] the entropy associated to a Killing horizon is expressed as the
Noether charge for the associated Killing symmetry. For Einstein gravity the explicit

                        25
expression is6

                            S=    Q[] = -     1         ab ab.                    (5.1)
                         2
                                  hor      16G        hor

Here the normalization of the Killing vector a is chosen so that S precisely equals

A/4G , where A is the area of the horizon. When there is no stress energy in the bulk,

the variation Q[] of the integrand can be extended to a closed form by imposing the

(linearized) Einstein equations for the (variation of) the background geometry. For

black holes this fact is used to deform the integral over the horizon to the boundary at

infinity, which leads to the first law of black hole thermodynamics.

These same ideas can be applied to de Sitter space. Here the situation is `inverted'

compared to the black hole case, since we are dealing with a cosmological horizon and

there is no asymptotic infinity. In fact, when there is no stress energy in the bulk the

variation of the horizon entropy vanishes, since there is no boundary term at infinity.

The first law of horizon thermodynamics in this case reads [17, 22]

                   S  +  H  =  0       where                 H = aTab db          (5.2)
                2
                                                                             C

represents the variation of the Hamiltonian associated with the Killing symmetry. It is

expressed as an integral of the stress energy tensor over the Cauchy surface C for the

static patch. We are interested in a situation where the stress is concentrated in a small

region around the origin, with a radius r that is much smaller than the Hubble scale.
This means that the integrand of H only has support in this region. Furthermore,
the variation Q[] of integrand of the Noether charge can be extended to a closed form

almost everywhere in the bulk, except in the region with the stress energy. This means

we can deform the surface integral over the horizon to an integral over a surface S
well outside the region with the stress energy. Following Wald's recipe we can write

this integral as

                                  H = Q[] -  � B                                  (5.3)

                                                  S

where we included an extra contribution  � B which vanishes on the horizon.

The Hamiltanian H is proportional to the generator of time translations in the

static coordinates of de Sitter space, where the constant of proportionality given by

the surface gravity a0 on the cosmological horizon. Hence we have

                a         1            which implies                        M
                      =                                             H =        ,  (5.4)
                  xa a0 t                                                   a0

where M denotes the change in the total mass or energy contained in de Sitter space.
With this identification the first law takes an almost familiar form

                      T S = -M         with                      T = a0 .         (5.5)
                                                                    2

6Here we use the notation of [15] by introducing the symbol  ab  =      1   abc1...cd-2 dxc1. . .dxcd-2 .
                                                                    (d-2)!

                                       26
The negative sign can be understood as follows. In deforming the Noether integral
(5.1) from the horizon to the surface S we have to keep the same orientation of the
integration surface. However, in the definition of the mass the normal points outward,
while the opposite direction is used in the definition of the entropy.

5.2 An approximate ADM definition of mass in de Sitter

We would like to integrate the second equation in (5.4) to obtain a definition of the
mass M similar to the ADM mass. Strictly speaking, the ADM mass can only be
defined at spatial infinity. However, suppose we choose the radius r that defines
the integration surface S to be (i) sufficiently large so that the gravitational field
of the mass M is extremely weak, and (ii) small enough so that r is still negligible
compared to the Hubble scale L. In that situation it is reasonable to assume that to
a good approximation one can use the standard ADM expression for the mass. By
following the same steps as discussed in [50, 51] for the ADM mass, we obtain the
following surface integral expression for the mass M [52, 53]

M=     (Q[t] - t � B) =                    1       jhij - ihjj dAi.       (5.6)

    S                                 16G      S

Here hij is defined in terms of the spatial metric.
    We assume now that we are in a Newtonian regime in which Newton's potential 

is much smaller than one, and furthermore far away from the central mass distribution
so that  depends only on the distance to the center of the mass distribution. In this
regime the metric takes the following form

ds2        =  -dt2                 + dx2i  - 2(x)      dt2 + (xidxi)2  .  (5.7)
    |x|=r                                                        |x|2

We will assume that the matter is localized well inside the region |x| < r. This means
that the Newtonian potential is in good approximation only a function of the radius.

When we insert the spatial metric

hij = ij - 2(x)ninj                            with      nj    xj         (5.8)
                                                               |x|

into the ADM integral (5.6) and choose a spherical surface with a fixed radius r we
find the following expression for the mass

                                   1
           M =-                               (x)jnj dA                   (5.9)
                    8G
                                           r

where dA = nidAi. It is easy to check the validity of this expression using the explicit
form of (x) (4.23) and the fact that for a spherical surface

                                           d-2
                                   jnj =            .                     (5.10)
                                               |x|

                                           27
6 The Elastic Phase of Emergent Gravity

We now return to the central idea of this paper. As we explained, the effect of matter
is to displace the entropy content of de Sitter space. Our aim is to describe in detail
how the resulting elastic back reaction translates into an effective gravitational force.
We will describe this response using the standard linear theory of elasticity.

6.1 Linear elasticity and the definition of mass

The basic variable in elasticity is the displacement field ui. The linear strain tensor is

given in terms of ui by             1
                             ij = 2 (iuj + jui) .
                                                        (6.1)

In the linear theory of elasticity the stress tensor ij obeys the tensorial version of
Hooke's law. For isotropic and homogeneous elastic media there are two independent

elastic moduli conventionally denoted by  and �. These so-called Lam�e parameters

appear in the stress tensor as follows

                             ij =  kkij + 2� ij.        (6.2)

The combination K =  + 2�/(d - 1) is called the bulk modulus. The shear modulus
is equal to �: it determines the velocity of shear waves, while the velocity of pressure
waves is determined by  + 2�. Requiring that both velocities are real-valued leads to
the following inequalities on the Lam�e parameters

                         �0             and   + 2�  0.  (6.3)

Our aim is to relate all these elastic quantities to corresponding gravitational quantities.
In particular, we will give a map from the displacement field, the strain and the stress
tensors to the apparent Newton's potential, gravitational acceleration and surface mass
density. In addition we will express the elastic moduli in terms of Newton's constant
G and the Hubble acceleration a0.

    Since de Sitter space has no asymptotic infinity, the precise definition of mass is
somewhat problematic. In general, the mass can only be precisely defined with the help
of a particular reference frame. In an asymptotically flat or AdS space, this reference
frame is provided by the asymptotic geometry. We propose that in de Sitter space the
role of this auxiliary reference frame, and hence the definition of the mass, is provided
by the elastic medium associated with the volume law contribution to the entanglement
entropy. In other words, the reference frame with respect to which we define the mass
M has to be chosen at the location where the standard Newtonian gravity regime makes
the transition to the elastic phase. This implies that the definition of mass depends
on the value of the displacement field and its corresponding strain and stress tensor in
the elastic medium.

                                        28
    We will now show that the ADM definition of mass can be naturally translated into
an expression for the elastic strain tensor or, alternatively, for the stress tensor. In
section 4, we found that the displacement field ui at the horizon is given by

                                             with            ni   =  xi   (6.4)
                     ui = a0 ni                                      |x|

and we argued that a similar identification holds in the interior of de Sitter space.

Alternatively, we can introduce the displacement field ui in terms of the spatial metric

hij via the Ansatz                         a0
                                           c2
                           hij   =  ij  -      (uinj  +  niuj) .          (6.5)

Eventually we take a non-relativistic limit in which we take L and c to infinity, while

keeping a0 = c2/L fixed. Hence we will work almost exclusively in the Newtonian
regime, and will not attempt to make a correspondence with the full relativistic gravi-

tational equations.

It is an amusing calculation to show that the expression (5.9) for the mass M can

be rewritten in the following suggestive way in terms of the strain tensor ij for the
displacement field ui defined in (6.4)

                           M = a0           njij - nijj dAi .             (6.6)
                                  8G
                                        S

In this calculation we used the fact that the integration surface is far away from the
matter distribution, so that  only depends on the distance |x| to the center of mass.
This same result can be derived by inserting the expression (6.5) together with (6.4)
into the standard ADM integral (5.6). It is interesting to note that the first term
corresponds to Q[t] while the second term is equal to -t � B. We again point out that
the prefactor a0/8G in (6.6) is identical to the observed critical value for the surface
mass density.

    When we multiply the expression (6.6) for M by the acceleration scale a0 we obtain
a physical quantity with the dimension of a force. This motivates us to re-express the
right hand side as

                                 M a0 = ijnj dAi                          (6.7)

                                                  S

where we identified the stress tensor ij with the following expression in terms of the

strain tensor                           a02
                                       8G
                              ij    =          ij - kkij  .               (6.8)

By comparing with (6.2) we learn that the elastic moduli of the dark elastic medium

take the following values

                     � = a02               and             + 2� = 0.      (6.9)
                           16G

                                             29
We thus find that the shear modulus has a positive value, but that the P-wave modulus
vanishes. The shear modulus has the dimension of energy density, as it should, and is
up to a factor (d - 1)(d - 2) equal to the cosmological energy density.

    In the theory of elasticity the integrand of the right hand side of (6.7) represents
the outward traction force ijnj. The left hand side on the other hand is the outward
force on a mass shell with total mass M when it experiences an outward acceleration
equal to the surface acceleration a0 at the horizon. Hence, it is natural to interpret the
equation (6.7) as expressing a balance of forces.

    The precise value (6.9) of the shear modulus is dictated by the following calcula-
tion. Let us consider the special situation in which the surface S corresponds to an
equipotential surface. In this case we can equate the gravitational self-energy enclosed
by S exactly with the elastic self energy

                          1  M =  1    ijuj dAi .            (6.10)

                          2       2  S

In the next subsection we further elaborate these correspondence rules between the
elastic phase and the Newtonian regime of emergent gravity. Specifically, we will show
that the elastic equations naturally lead to an effective Newtonian description in terms
of an apparent surface mass density.

6.2 The elasticity/gravity correspondence in the sub-Newtonian regime

First we start by rewriting the familiar laws of Newtonian gravity in terms of a surface
mass density vector. We introduce a vector field i defined in terms of the Newtonian
potential  via

i = -              d-2     gi            where     gi = -i   (6.11)
                   d-3    8G

is the standard gravitational acceleration. By working with i instead of gi we avoid
some annoying dimension dependent factors, and make the correspondence with the
elastic quantities more straightforward. The normalization is chosen so that the grav-
itational analogue of Gauss' law simply reads

                   ii =        or                 i dAi = M  (6.12)

                                                S

where M is the total mass inside the region enclosed by the surface S. We will refer to

i as the surface mass density. The gravitational self-energy of a mass configuration
can be expressed in terms of the acceleration field gi and the surface mass density

vector field i as                      1
                             Ugrav = 2 dV gii.
                                                             (6.13)

                                     30
We are interested in the force on a small point mass m located at some point P .
Its Newtonian potential (m) and surface mass density (m) are sourced by the mass
density (m) = m (x-xP ). The force that acts on the point mass is derived from the
gravitational potential, which obeys the representation formula

m(P ) = dAi (m)i -  i(m) .            (6.14)

                      S

Here the surface S is chosen so that it encloses the mass distribution that sources the
field  and i.

    All these equations have direct analogues in the linear theory of elasticity. The
displacement field ui is analogous to the Newtonian potential , the strain tensor ij
plays a similar role as the gravitational acceleration gi, and the stress tensor ij is the
direct counterpart of the surface mass density i. For instance, our definition (6.11) of
the surface mass density i is the direct analogue of the definition (6.2) of the stress
tensor ij, with the obvious correspondence between the expressions for gi in terms of
 and ij in terms of ui. The counterparts of the Poisson equation and Gauss' law read

iij + bj = 0  and    ij dAj + Fi = 0  (6.15)

                   S

where the body force bj represents the force per unit of volume that acts on the medium
and Fj is the total force acting on the part of the medium enclosed by the surface S.
Also the elastic energy is given, except for the sign, in a completely analogous way

                        1             (6.16)
              Uelas = 2 dV ijij.

The elastic equivalent of the point mass is a point force described by a delta-function
supported body force b(if) = fi (x - xP ). It acts as a point source for the elastic
displacement field u(if) and stress tensor i(jf). The elastic potential that determines the
elastic force acting on a point force satisfies an analogous representation formula as for

the gravitational case

- fiui(P ) = dAi uj(f)ji - uji(jf) .  (6.17)

                           S

Here the integration surface S has been chosen such that it contains the body forces
that source ui and ij.

    It is striking that the correspondence between gravitational and elastic quantities
only requires two dimensionful constants: Newton's constant G and the Hubble accel-
eration scale a0. All the other constants of nature, like the speed of light, Planck's
constant or Boltzmann's constant, do not play a role. We already announced that
the elastic moduli take the values given in (6.9), but we have not yet justified why

              31
we chose this specific value for the shear modulus. The reason is that only with this
identification all elastic quantities, including the expressions of the elastic potentials,
are precisely mapped onto the corresponding gravitational quantities.

    Note, however, that due to the difference in the tensorial character of the corre-
sponding quantities, we also need to make use of a vector field. Since the elastic strain
and stress tensors are symmetric and linearly related, they can be simultaneously di-
agonalised. Their eigenvalues are called the principle strain and stress values. We are
particularly interested in the largest principle strain and stress. Let us introduce the
so-called deviatoric strain tensor ij, which is defined as the traceless part of ij

                                         1            (6.18)
                        ij = ij - d - 1 kkij

The direction of the large principle strain and stress coincides with the eigenvector ni
of the deviatoric strain ij. We will denote the corresponding eigenvalue with , since
it plays the identical role as the parameter introduced in the previous section, as will

become clear below. Hence, we have

                               ijnj =  ni.            (6.19)

Here ni is a normalized eigenvector satisfying |n|2 = nini = 1.
    We now come to our matching formulas between the elastic phase and the Newto-

nian regime. The identifications between the elastic and gravitational quantities will
be made at a surface interface S that is perpendicular to the maximal strain. Hence,
the normal to S is chosen so that it coincides with the unit vector ni. In the following
table we list all gravitational and elastic quantities and their correspondences. These
correspondence equations allow us to translate the response of the dark energy medium
described by the displacement field, strain and stress tensors in the form of an apparent
gravitational potential, acceleration and surface mass density.

Gravitational quantity         Elastic quantity       Correspondence

Newtonian potential            displacement field ui      ui = ni/a0
                                                      ijnj = -gi/a0
gravitational acceleration gi  strain tensor     ij   ijnj = ia0

surface mass density    i      stress tensor     ij       bi = - a0ni
                                                          fi = -m a0ni
mass density                   body force        bi

point mass              m      point force       fi

                               32
7 Apparent Dark Matter from Emergent Gravity

In this section we return to the derivation of the Tully-Fisher scaling relation for the
apparent surface mass density. For this we will use the linear elastic description of the
response of the dark energy medium due the presence of matter. The stress tensor and
strain tensor are related by Hooke's law(6.8), which for convenience we repeat here

        ij  =   a20  ij - kkij                             (7.20)
               8G

We begin with a comment about this specific form of the stress tensor. As we remarked,
it corresponds to a medium with vanishing P-wave modulus. This means that pressure
waves have zero velocity and thus exist as static configurations. The decomposition of
elastic waves in pressure and shear waves makes use of the fact that every vector field
ui can be written as a sum of a gradient i and a curl part jij with (ij) = 0.
Pressure waves obey [iuj] = 0 and are of the first kind, while shear waves satisfy
iui = 0 and hence are of the second kind. It follows from the fact that the P-wave
modulus vanishes that a displacement field which is a pure gradient automatically leads
to a conserved stress energy tensor. In other words,

ui = i         implies that     iij = 0.                   (7.21)

In this paper we only consider quasi-static situations in which the elastic medium is
in equilibrium. This means that without external body forces the stress tensor should
be conserved, which together with the above observation tells us that the displacement
field will take the form of a pure gradient. Note that the field ui = ni indeed
satisfies this requirement in the case that ni points in the same direction as i. The
observation that a displacement field ui of the form (7.21) automatically leads to a
conserved stress tensor will become useful in our calculations below.

7.1 From an elastic memory effect to apparent dark matter

We now arrive at the derivation of our main result: the scaling relation between the
apparent surface mass density D and the actual surface mass density B of the (bary-
onic) matter. We will follow essentially the same steps as in our heuristic derivation,
but along the way we will fill in some of the gaps that we left open in our initial
reasoning.

    The amount of de Sitter entropy inside a general connected subregion B is given by
the generalizations of (2.15) and (4.29)

              1    dV =         xi dAi .                   (7.22)
SDE(B) = V0                  B L 4G
                 B

The first expression makes clear that the entropy content is proportional to the volume,
while the second expression (which is equivalent through Stokes theorem) exhibits the

                     33
`fractionalization' of the quantum information. Each Planckian cell of the surface B
contributes a fraction determined by the ratio of the proper distances of a central point,
say the origin, to this cell and the horizon.

    A central assumption is that the matter has removed an amount of entropy SM (L)
from a inclusion region VM (L) whose total volume VM (L) is proportional to the mass
M . Furthermore, we will also use the fact that the amount of entropy that is removed
from a subregion grows linearly with its size. Let us choose such a large connected
subregion B, which one may think of as a large ball of a given radius. The amount of
entropy that is removed from this region is given by

               1           dV  =     1    ui dAi.       (7.23)
        SM (B) = - V0
                       BVM           V0  B

Here and throughout this section we denote the entire inclusion region VM (L) simply
by VM . The last expression is the generalization of equation (4.35). Since the entropy
is only removed from the region VM we can treat the medium as being incompressible
outside of VM . This means that iui vanishes everywhere except inside VM , where,
as we will show below, it must be constant. By applying Stokes' theorem to the last

expression we then learn that inside the region B we have

        iui =  -V0/V0         inside B  VM              (7.24)
                   0          outside B  VM

We will assume that the dark elastic medium is in equilibrium and hence that the stress
tensor ij is conserved. We can then make use of our observation (7.21) and represent
ui as a pure gradient. Given the location of the region VM we thus find the following
solution for the displacement field ui inside the region B

ui = i  with   2 =             -  d-1    inside B  VM   (7.25)
                                  d-2    outside B  VM

                                  0

Here we inserted the known value (4.37) for the ratio V0/V0. The full solution for ui is
obtained by extending B to the entire space. The volume of the intersection of B with

the inclusion region VM will be denoted as

               VM (B)  dV                               (7.26)

                                    BVM

and equals VM (r) given in (4.33) for the case that B represents a sphere of size r.
    We like to determine the apparent surface mass density D in this region outside

of VM . According to the correspondence rules obtained in the subsection the surface
mass density D can be expressed in terms of the largest principle stress  as

                       where             ijnj = ni.     (7.27)
D = a0

                       34
We now make use of the fact that the strain and stress tensor are purely deviatoric

outside of VM . This implies that the stress tensor is proportional to the deviatoric
strain tensor ij, and hence that the largest principle stress  is directly related to the
largest principle strain  introduced in (6.19). Given the value of the shear modulus

(6.9) we thus recover the same relation (4.43) as in our heuristic derivation

                    D    =   a0                 where              ijnj = ni.               (7.28)
                            8G

Our goal is to explain the baryonic Tully-Fisher relation for the surface mass density
D in terms of the surface mass density for the mass M . For this we will follow a
similar reasoning as in our heuristic derivation. In particular, we like to derive the
analogous relation to equation (4.46). It turns out, however, that we can only derive
the following inequality on the value of the largest principle strain 

                                              2dV  VM (B)                                   (7.29)

                                            B

where VM (B) is defined in (7.26). When we take B to be a spherical region with radius
r, and with the equality sign we recover equation (4.46) from which we derived the

Tully-Fisher relation. Our derivation of the inequality will make clear under which

conditions the equality sign is expected to hold.

    The deviatoric strain ij not only describes shear deformations, but also shape
deformations where for instance one direction is elongated (compressed) and the other

perpendicular directions are compressed (elongated) in such a way that the local volume

is preserved. One can derive an upper limit on the value of the largest principle

strain  in terms of the matrix elements of the deviatoric strain ij by asking the
following question: given the value of ij2, what is the maximal possible value for the

largest principle strain ? Clearly,  is maximal when all the other principle strains

perpendicular to ni are equal in magnitude, and have the opposite sign to  so that

the sum of all principle strains vanishes. Hence, in this situation all the perpendicular

principle  strains  are  equal  to  -    .  We  thus  obtain  the  following  upper  bound  on  
                                    d-2

                                         2      d-2    ij 2.                                (7.30)
                                                d-1

The proof of the inequality (7.29) now becomes elementary and straightforward. First
we replace 2 by the right hand side of (7.30) and express ij in terms of  by inserting
the solution (7.25) for ui. Next we extend the integration region from B to the entire

space, and perform a double partial integration to express the integrand entirely in
terms of 2 by using

                                    (ij)2dV = 2 2dV.                                        (7.31)

                                                35
Here it is important to verify that  falls of rapidly enough so that there are no
boundary terms. After these steps we are left with an integral whose support is entirely
contained in the intersection of B with VM . The dimension dependent numerical factors
work out precisely so that the integrand is equal to one in this intersection region. In
this way one shows that the following relation holds exactly

                   d-2    ij2dV = dV.                             (7.32)
               a
                                               BVM
                   d-1

So the inequality sign in (7.29) will turn into an (approximate) equality sign if two as-
sumptions are true: the first is that the largest principle strain  is given to a good ap-
proximation by its maximal possible value. This means that the perpendicular strains
are all approximately equal. The other assumption is that the contribution of the in-
tegral (7.32) outside of B can be ignored. This is also reasonable, since the value of 
falls of as 1/ad-1 where a is the distance to the boundary of B  VM .

    We will now present a slightly different derivation of the same relation (7.32). Let
us assume that the strain tensor ij is purely hydrostatic inside of B  VM , which
means that the deviatoric strain ij is only supported outside of the region B  VM .
This condition is equivalent to the assumption that the boundary of B  VM is normal
to the direction of the largest principle strain and that the value of the normal strain
 is equal to one. This can be shown for instance as follows. Consider the integral of
the elastic energy density both inside as well as outside B  VM . Conservation of the
stress tensor gives us that these energies are equal in size but opposite in sign. Again,
by partial integration one finds

1                 1            ij ij dV       a20         uidAi.
2       ij ij dV  =-                     =  16G                   (7.33)
                       2  BVM                       (BVM )
   BV M

The first integral in (7.33) gives the contribution of the deviatoric strain and stress,
while the middle integral represents the elastic energy due to the hydrostatic strain
and stress inside the inclusion. Finally, the integral on the right hand side represents
the volume of the dark elastic medium that is removed by matter from the region B.

    The hydrostatic part of the elastic energy is easily calculated using the fact that
the strain and stress tensor are proportional to ij. In this way we learn from (7.33)
that the deviatoric part of the elastic energy equals

1    ij ij dV  =    a20   d-1            dV = a20     uidAi       (7.34)
2                 16G     d-2               16G
   B                           BVM                  B

where we used the fact that the iui = 0 outside of B  VM to move the boundary
integral from (B  VM ) to B. Note that the first equality is equivalent to (7.32). To
complete the derivation of the baryonic Tully-Fisher relation we now make use of our
assumption that the volume of the region B VM only depends on the mass distribution

                          36
of the actual matter that is present inside the region B. Indeed, we assume that the
result of the boundary integral in the last expression in (7.34) can be evaluated by
replacing the displacement field by the corresponding expression in terms of Newton's
potential B of the ordinary `baryonic' matter. Hence, we will make the identification

                   uidAi =      B      nidAi.              (7.35)
                                a0
                  B         B

Here we will make the assumption that the surface B can be chosen so that its
normal coincides with the direction ni. This is a natural assumption in the case that
B coincides with an equipotential surface of B.

    We are finally in a position to combine all ingredients and obtain the main result
of our analysis. First we use (7.28) to express the largest principle strain  in terms
of D. Next we assume that the conditions for the equality sign in (7.29) hold, and
the identification (7.35) can be made. Combined with (7.34) this leads to the following
integral relation for the surface mass density D for the apparent dark matter in terms
of the Newtonian potential for the baryonic matter

                  8G 2          d-2            B   nidAi.  (7.36)
                  a0 D  dV =                   a0
               B                  d-1  B

Since the integration region B can be chosen arbitrarily, we can also derive a local
relation by first converting the right hand side into a volume integral by applying
Stokes' theorem and then equating the integrands. In this way we obtain

                  8G 2      d-2     i  B       ni  .       (7.37)
                   a0 D =   d-1        a0

In the next subsection we will use this relation for a spherically symmetric situation
to derive the mass density for the apparent dark matter from a given distribution of
baryonic matter. For this situation we can take ni = xi/|x|, and easily evaluate the
right hand side in terms of the mass distribution B of the baryonic matter.

7.2 A formula for apparent dark matter density in galaxies and clusters

To be able to compare our results with observations it will be useful to re-express our

results directly as a relation between the densities B and D of the baryonic matter
and apparent dark matter. It is not a straightforward task to do this for a general mass

distribution, so we will specialize to the case that the baryonic matter is spherically

symmetric. We will also put the number of spacetime dimensions equal to d = 4.

Let us begin by reminding ourselves of the relation (5.9) between the surface mass

density and Newton's potential. For a spherically symmetric situation this relation can

be written as              1 (r) M (r)

                  (r) = -        =                         (7.38)
                           4G r A(r)

                            37
where                                  r

                  M (r) = (r )A(r )dr                                         (7.39)

                                    0

is the total mass inside a radius r. With the help of these equations it is straigthforward

to re-express the integral relation (7.36) in terms of the apparent dark matter mass

MD(r) and baryonic mass MB(r). This leads to

                    r      GMD2 (r  )  dr  =  MB(r)a0r .                      (7.40)
                  0            r2                  6

This is the main formula and central result of our paper, since it allows one to make a
direct comparison with observations. It describes the amount of apparent dark matter
MD(r) in terms of the amount of baryonic matter MB(r) for (approximately) spheri-
cally symmetric and isolated astronomical systems in non-dynamical situations. After
having determined MD(r) one can then compute the total acceleration

                           g(r) = gB(r) + gD(r)                               (7.41)

where the gravitational accelerations gB and gD are given by their usual Newtonian
expressions

       gB (r)  =  GMB (r)           and          gD(r)    =   GMD(r) .        (7.42)
                      r2                                          r2

We will now discuss the consequences of equation (7.40) and present it in different

forms so that the comparison with observations becomes more straightforward.

First we note that the same relation (7.40) can also be obtained from the simple

heuristic derivation presented in section 4.4. By taking equation (4.46) and inserting

all relevant definitions for the strain and the volume of the inclusion, one precisely

recovers our main formula (7.40). In the special case that the baryonic mass MB is
entirely centered in the origin it is easy to derive the well-known form of the baryonic

Tully-Fisher relation. In this case one can simply differentiate with respect to the

radius while keeping the baryonic mass MB constant. It is easily verified that this
leads to the relation

       gD(r) = aM gB(r)                    with           aM  =  a0 .         (7.43)
                                                                 6

The parameter aM is the famous acceleration scale introduced by Milgrom [32] in his
phenomenological fitting formula for galaxy rotation curves. We have thus given an
explanation for the phenomenological success of Milgrom's fitting formula, in particular
in reproducing the flattening of rotation curves. An alternative way to express (7.43)
is as a result for the asymptotic velocity vf of the flattened galaxy rotation curve

       vf4 = aM GMB                    where     gD(r)        =  vf2 .        (7.44)
                                                                 r

                                       38
This is known as the baryonic Tully-Fisher relation and has been well tested by obser-
vations [36, 37] of a very large number of spiral galaxies.

    We like to emphasize that we have not derived the theory of modified Newtonian
dynamics as proposed by Milgrom. In our description there is no modification of the
law of inertia, nor is our result (7.43) to be interpreted as a modified gravitational field
equation. It is derived from an estimate of an effect induced by the displacement of the
free energy of the underlying microscopic state of de Sitter space due to matter. This
elastic response is then reformulated as an estimate of the gravitational self-energy
due to the apparent dark matter in the form of the integral relation (7.40). Hence,
although we derived the same relation as modified Newtonian dynamics, the physics
is very different. For this reason we referred to the relation (7.43) as a fitting formula,
since it is important to make a clear separation between an empirical relation and
a proposed law of nature. There is little dispute about the observed scaling relation
(7.43), but the disagreement in the scientific community has mainly been about whether
it represents a new law of physics. In our description it does not.

    The validity of (7.40) depends on a number of assumptions and holds only when
certain conditions are being satisfied. These conditions include that one is dealing with
a centralized, spherically symmetric mass distribution, which has been in dynamical
equilibrium during its evolution. Dynamical situations as those that occur in the
Bullet cluster are not described by these same equations. The system should also be
sufficiently isolated so that it does not experience significant effects of nearby mass
distributions. Finally, in the previous subsection we actually derived an inequality,
which means that to get to equation (7.40) we have made an assumption about the
largest principle strain . While this assumption is presumably true in quite general
circumstances, in particular sufficiently near the main mass distribution where the
apparent dark matter first becomes noticable. But as one gets further out, or when
other mass distributions come into play, we are left only with an inequality.

    It is known that the formula (7.43) fails to explain the observed gravitational ac-
celeration in clusters, since it underestimates the amount of apparent dark matter. To
get the right amount one would need to multiply aM by about a factor of 3 according
to [33, 35]. Equation (7.43) also can not account for the observed strong gravitational
lensing due to dark matter in the central parts of the cluster, since the projected surface
mass densities required for strong lensing are larger than the expected value aM /G by
about factor of 6 [61]. For these reasons proponents of modified newtonian dynamics
still have to assume a form of particle dark matter at the cluster scale.

    These discrepancies can be significantly reduced and perhaps completely explained
away in our theoretical description. To go from (7.40) to (7.43) we assumed that the
matter is entirely located in the origin, since in taking the derivative with respect to
r we kept MB constant. In most galaxies this is indeed a good approximation, but
this assumption is not justified in clusters. Most of the baryonic mass in clusters is
contained in X-ray emitting gas, which extends all the way to the outer parts of the

                                                      39
cluster. In fact, even for galaxies a more precise treatment requires the use of the mass
density profile B(r) instead of a point mass approximation.

    So let us go back to (7.40) and take its derivative while taking into account the
r dependence of MB(r). We introduce the averaged mass densitities B(r) and D(r)
inside a sphere of radius r by writing the integrated masses MB(r) and MD(r) as

                  4r3                                     4r3
MB(r) = 3 B(r)                   and        MD(r) = 3 D(r).                  (7.45)

We also introduce the slope parameters

 B (r)         =    d  log B(r)  and        D(r)  =       -  d  log D(r)  .  (7.46)
                  -    d log r                                  d log r

When these slope parameters are approximately constant they give us the power law

behavior of the averaged mass densitities. By differentiating (7.36) with respect to r

and rewriting the result using (7.45) one finds that the average apparent dark matter

density obeys

                       2D(r) =   4 - B(r)    a0 B(r) .                       (7.47)
                                            8G r

For a central point mass MB the slope parameter B is equal to 3, hence the prefactor
would be equal to one. The apparent dark matter has in that case a distribution with
a slope D = 2, which means that it falls off like 1/r2. A similar formula as (7.47)
holds in modified Newtonian dynamics, except without the prefactor.

    In the central parts of a cluster the slope parameter of the mass distribution is
generally observed to be smaller than 1 or even close to 0, while in the outer parts the
slope can still be significantly smaller than 3. We thus find that in our description we
gain a factor in between 1.5 and 3.5 depending on the region of the cluster compared
to modified Newtonian dynamics. This means that the `missing mass problem' in
clusters is significantly reduced and given the uncertainty about the amount of baryons,
possibly entirely removed. In fact, at this point it is good to mention that also other
matter particles, whatever they are, would in our description have to be counted in
the baryonic mass density. This means that they would also lead to an increase in the
apparent dark matter component.

    Given the averaged mass density D(r) one can find the actual mass density D(r)
for the apparent dark matter via the relation

                                                   1                         (7.48)
                                 D(r) = 1 - 3 D(r) D(r).

We now like to illustrate that these equations can, in contrast to modified Newton
dynamics, lead to strong lensing phenomena in the cores of clusters in cases where
there is a significant dark matter contribution. For this purpose let us consider an

                                        40
idealized situation in which the dark matter and baryonic matter in the core region

r < r0 have exactly the same density profile with B = D = 1. This corresponds to

the case where the surface mass densities B and D are both equal to the maximal

value a0/8G corresponding to  = 1. The total mass density profile inside the core is

then given by                              a0
                                         4Gr
                     B (r)  =  D(r)  =              for r < r0.  (7.49)

One then finds that the projected surface mass density proj(< r0) of the entire core
region, as astrophysicists would define it by integrating along the line of sight, is equal

to cH0/G, which should be sufficient to cause strong gravitational lensing, especially
in the inner parts of the core region. This strong lensing effect would in this case be

equally due to baryonic and dark matter.

As a final fun comment let us, just out of curiosity, take the formula (7.47) and

apply it to the entire universe. By this we mean the following: we assume a constant

baryonic mass density, so we set B = 0, and in addition we take the radius to be equal
to the Hubble radius, i.e. we put r = L. Now we note that the critical mass density of

the universe equals

                               crit  =  3H02  =  3a0  1          (7.50)
                                        8G       8G     .

                                                      L

Hence, when we put r = L in the formula (7.47) we obtain a relation between the

standard cosmological density parameters B = B/crit and D = D/crit of the
baryonic and dark matter. We find

                                     D2  =    4                  (7.51)
                                              3 B.

This relation holds remarkably well for the values of D and B obtained by the WMAP
and Planck collaborations. We ask the reader not to read too much in this striking and
somewhat surprising fact. Because it is far from clear that our derivation of the density
formula (7.47) would be applicable to the entire universe. For instance, an immediate
question that comes to mind is whether this relation continues to hold throughout the
cosmological evolution of the universe. We have worked exclusively in a static situation
near the center of the static patch of a dark energy dominated universe. Any questions
regarding the cosmological evolution of the universe are beyond the scope of this paper,
and will hopefully be addressed in future work. This point will be reiterated in our
conclusion.

                                          41
8 Discussion and Outlook

8.1 Particle dark matter versus emergent gravity

The observational evidence for the presence of dark matter appears to be overwhelming.
The first known indications came from the observed velocity profiles in (clusters of)
galaxies. Other strong evidence comes from strong and weak gravitational lensing
data, which show signs of what appears to be additional clumpy matter in clusters and
around (groups of) galaxies. Dark matter also plays a crucial role in the explanation
of the spectrum of fluctuation in the cosmic microwave background and the theory of
structure formation.

    Since up to now there appeared to be no evidence that general relativity or New-
tonian gravity could be wrong at the scales in question, the most generally accepted
point of view is that these observations indicate that our universe contains an enor-
mous amount of a yet unknown form of dark matter particle. However, the discrepancy
between the observed gravitational force and the one caused by the visible baryonic
matter is so enormous that it is hard to claim that these observations provide evidence
for the validity of general relativity or Newtonian gravity in these situations. Purely
based on the observations it is more appropriate to say that these familiar gravitational
theories can only be saved by assuming the presence of dark matter. Therefore, with-
out further knowledge, the evidence in favour of dark matter is just as much evidence
for the possible breakdown of the currently known laws of gravity.

    The real reason why most physicists believe in the existence of particle dark matter
is not the observations, but because there was no theoretical evidence nor a conceptual
argument for the breakdown of these laws at the scales where the new phenomena
are being observed. It has been the aim of this paper to provide a theoretical and
conceptual basis for the claim that this situation changes when one regards gravity as
an emergent phenomena. We have shown that the emergent laws of gravity, when one
takes into account the volume law contribution to the entropy, start to deviate from
the familiar gravitational laws precisely in those situations where the observations tell
us they do. We have only made use of the natural constants of nature, and provided
reasonably straightforward arguments and calculations to derive the scales and the
behavior of the observed phenomena. Especially the natural appearance of the accel-
eration scale a0 should in our view be seen as a particularly convincing aspect of our
approach.

    In our view this undercuts the common assumption that the laws of gravity should
stay as they are, and hence it removes the rationale of the dark matter hypothesis. Once
there is a conceptual reason for a new phase of the gravitational force, which is governed
by different laws, and this is combined with a confirmation of its quantitative behavior,
the weight of the evidence tips in the other direction. Admittedly, the observed scaling
relations have played a role in developing the theoretical description, and motivated our
hypothesis that the entropy of de Sitter space is distributed over de bulk of spacetime.

                                                      42
But the theoretical arguments that support this hypothesis together with the successful
derivation of the observed scaling relations are in our view sufficient proof of hypothesis.
Our main conclusion therefore is:

The observed phenomena that are currently attributed to dark matter are the
conesquence of the emergent nature of gravity and are caused by an elastic response
due to the volume law contribution to the entanglement entropy in our universe.

In order to explain the observed phenomena we did not postulate the existence of
a dark matter particle, nor did we modify the gravitational laws in an ad hoc way.
Instead we have to tried to understand their origin and their mutual relation by taking
seriously the theoretical indications coming from string theory and black hole physics
that spacetime and gravity are emergent. We believe this approach and the results we
obtained tell us that the phenomena associated with dark matter are an unavoidable
and logical consequence of the emergent nature of space time itself. The net effect
should be that in our conventional framework one has to add a dark component to
the stress energy tensor, which behaves very much like the cold dark matter needed
to explain structure formation, but which in its true origin is an intrinsic property
of spacetime rather than being caused by some unknown particle. Indeed, we have
argued that the observed dark matter phenomena are a remnant, a memory effect, of
the emergence of spacetime together with the ordinary matter in it.

    In particular, we have made clear why the apparent dark matter behaves exactly in
the right way to explain the phenomenological success of modified Newtonian dynamics,
as well as its failures, without the introduction of any freely adjustable parameters. We
have found that in many, but not all, aspects the apparent dark matter behaves similar
to as one would expect from particle dark matter. In particular, the excess gravity and
the gravitational potential wells that play a role in these scenarios also appear in our
description.

    Perhaps superficially our approach is similar in spirit to some earlier works [62, 63,
64, 65, 66] on the relationship between dark matter and the thermodynamics of space-
time. But the details of our derivations and especially the conceptual argumentation
differs significantly from these papers. Our theoretical framework incorporates and
has been motivated by the recent developments on emergent gravity from quantum
information, and is in our view a logical extension of this promising research direction.

8.2 Emergent gravity and apparent dark matter in cosmological scenarios

In this paper we have focussed on the explanation of the observed gravitational phe-
nomena attributed to dark matter. By this we mean the excess in the gravitational
force or the missing mass that is observed in spiral or elliptical galaxies and in galaxy
clusters. Of course, dark matter plays a central role in many other aspects of the cur-
rent cosmological paradigm, in particular in structure formation and the explanation

                                                      43
of the acoustic peaks in the cosmic microwave background. In none of these scenarios
is it required that dark matter is a particle: all that is needed is that its cosmologi-
cal evolution and dynamics is consistent with a pressureless fluid. In our description
we eventually end up with an estimate of the apparent dark matter density that in
many respects behaves as required for structure formation and perhaps even for the
explanation of the CMB spectrum. Namely, effectively the apparent dark matter that
comes out of our emergent gravity description also leads to a gravitational potential
that attracts the baryonic matter as cold dark matter would do.

    However, the arguments and calculations that we presented in this paper are not yet
sufficient to answer the questions regarding the cosmological evolution of our equations.
In particular, we made use of the value of the present-day Hubble parameter H0 in
our equations, which immediately raises the question whether one should use another
value for the Hubble parameter at other cosmological times. In our calculations the
parameter H0 was assumed to be constant, since we made the approximation that our
universe is entirely dominated by dark energy and that ordinary matter only leads to
a small perturbation. This suggests that H0 or rather a0 should actually be defined
in terms of the dark energy density, or the value of the cosmological constant. This
would imply that a0 is indeed constant, even though it takes a slightly different value.

    A related issue is that in our analysis we assumed that dark energy is the dominant
contribution to the energy density of our universe. According to our standard cosmo-
logical scenarios this is no longer true in the early times of our universe, in particular
at the time of decoupling. This poses again the question whether a theory in which
(apparent) dark matter is explained via emergent gravity would be able to reproduce
the successful description of the CMB spectrum, the large scale structure and galaxy
formation. These questions need to be understood before we can make any claim that
our description of dark matter phenomena is as successful as the CDM paradigm in
describing the early universe and cosmology at large scales.

    By changing the way we view gravity, namely as an emergent phenomenon in which
the Einstein equations need be derived from the thermodynamics of quantum entan-
glement, one also has to change the way we view the evolution of the universe. In
particular, one should be able to derive the cosmological evolution equations from
emergent gravity. For this one needs to first properly understand the role of quantum
entanglement and the evolution of the total entropy of our universe. So it is still an
open question if and how the standard cosmological picture is incorporated in a theory
of emergent gravity. How does one interpret the expansion of the universe from this
perspective? Or does inflation still play a role in an emergent cosmological scenario?

    All these questions are beyond the scope of the present paper. So we will not make
an attempt to answer all or even a part of these questions. This also means that before
these questions are investigated it is too early to make a judgement on whether our
emergent gravity description of dark matter will also be able to replace the current
particle dark matter paradigm in early cosmological scenarios.

                                                      44
9 Acknowledgements

This work has been performed during the past 6 years and I have benefitted from
discussions and received encouragement from many colleagues. I like to begin by
thanking Herman Verlinde for sharing his insights, encouragement and for collaboration
on projects that are closely related to the ideas presented in this paper and which have
influenced my thinking. I have benefitted from discussions at different stages and
on different aspects of this work, with Jan de Boer, Kyriakos Papadodimas, Bartek
Czech, David Berenstein, Irfan Ilgin, Ted Jacobson, Justin Khoury, Tom Banks, G't
Hooft, Lenny Susskind and Juan Maldacena. A special thanks goes to Sander Mooij for
stimulating discussions and enthusiastic support, and to Manus Visser for discussions,
verifying the calculations and his invaluable help in correcting this manuscript.

    I am also grateful for encouragement from Stanley Deser, Robbert Dijkgraaf, Eliezer
Rabinovic, Neil Turok, Paul Steinhardt, Coby Sonnenschein, John Preskill, Steve
Shenker, and especially David Gross, whose critical and sharp questions have helped
me to stay focussed on the main issues.

    I thank the participants of the Bits and Branes program at KITP and summer
workshop at the Aspen center in 2014 for many discussions (among others with Joe
Polchinski and Don Marolf on the Firewall Paradox) that helped sharpen my ideas for
this work as well. Also I am grateful for the hospitality of the Caltech theory group in
the past years.

    I like to thank various astronomers and cosmologists whose knowledge benefitted
this work and whose support I have appreciated greatly. These include Moti Milgrom,
Pavel Kroupa, Hongsheng Zhao and Bob Sanders. Finally, I regret that Jacob Beken-
stein is no longer around to be able to read this finished work, since his ideas and
interests are playing a central role.

    This research has been made possible by the EMERGRAV advanced grant from the
European Research Council (ERC), the Spinoza Grant of the Dutch Science Organisa-
tion (NWO), and the NWO Gravitation Program for the Delta Institute for Theoretical
Physics.

                                                      45
References

  [1] J. M. Bardeen, B. Carter and S. W. Hawking, "The Four laws of black hole
       mechanics," Commun. Math. Phys. 31, 161 (1973).

  [2] J. D. Bekenstein, "Black holes and entropy," Phys. Rev. D 7, 2333 (1973).

  [3] S . W. Hawking , "Particle Creation By Black Holes," Commun Math. Phys. 43,
       199-220, (1975).

  [4] P. C. W. Davies, "Scalar particle production in Schwarzschild and Rindler met-
       rics," J. Phys. A 8, 609 (1975).

  [5] W. G. Unruh, "Notes on black hole evaporation," Phys. Rev. D 14, 870 (1976).

  [6] A. Strominger and C. Vafa, "Microscopic origin of the Bekenstein-Hawking en-
       tropy," Phys. Lett. B 379 (1996) 99, [hep-th/9601029].

  [7] J. M. Maldacena, "The large N limit of superconformal field theories and super-
       gravity," Adv. Theor. Math. Phys. 2, 231 (1998) [arXiv:hep-th/9711200].

  [8] S. Ryu and T. Takayanagi, "Holographic derivation of entanglement entropy from
       AdS/CFT," Phys. Rev. Lett. 96, 181602 (2006) [arXiv:hep-th/0603001]; "As-
       pects of holographic entanglement entropy," JHEP 0608, 045 (2006) [arXiv:hep-
       th/0605073].

  [9] M. Van Raamsdonk, "Building up spacetime with quantum entanglement," Gen.
       Rel. Grav. 42 (2010) 2323 [Int. J. Mod. Phys. D 19 (2010) 2429] [arXiv:1005.3035
       [hep-th]].

 [10] H. Casini, M. Huerta and R. C. Myers, "Towards a derivation of holographic
       entanglement entropy," JHEP 1105 (2011) 036, [arXiv:1102.0440].

 [11] A. Lewkowycz and J. Maldacena, "Generalized gravitational entropy," JHEP
       1308 (2013) 090 [arXiv:1304.4926].

 [12] T. Jacobson, "Thermodynamics of space-time: The Einstein equation of state,"
       Phys. Rev. Lett. 75, 1260 (1995) [gr-qc/9504004].

 [13] T. Padmanabhan, "Thermodynamical Aspects of Gravity: New insights,"
       arXiv:0911.5004 [gr-qc], and references therein. See also: T. Padmanabhan,
       "Atoms of Spacetime and the Nature of Gravity," J. Phys. Conf. Ser. 701 (2016)
       no.1, 012018. doi:10.1088/1742-6596/701/1/012018.

 [14] E. P. Verlinde, "On the Origin of Gravity and the Laws of Newton," JHEP 1104
       (2011) 029 [arXiv:1001.0785 [hep-th]].

                                                      46
[15] T. Faulkner, M. Guica, T. Hartman, R. C. Myers and M. Van Raamsdonk,
      "Gravitation from Entanglement in Holographic CFTs," JHEP 1403 (2014) 051
      [arXiv:1312.7856].

[16] B. Swingle and M. Van Raamsdonk, "Universality of Gravity from Entangle-
      ment," arXiv:1405.2933 [hep-th].

[17] T. Jacobson, "Entanglement Equilibrium and the Einstein Equation," Phys. Rev.
      Lett. 116, no. 20, 201101 (2016) [arXiv:1505.04753 [gr-qc]].

[18] G. Vidal, "Entanglement Renormalization," Phys. Rev. Lett. 99, 220405 (2007).

[19] B. Swingle, "Entanglement Renormalization and Holography," Phys. Rev. D 86
      (2012) 065007 [arXiv:0905.1317 [cond-mat.str-el]].

[20] F. Pastawski, B. Yoshida, D. Harlow and J. Preskill, "Holographic quantum error-
      correcting codes: Toy models for the bulk/boundary correspondence," JHEP
      1506 (2015) 149, [arXiv:1503.06237].

[21] Z. Yang, P. Hayden and X. L. Qi, "Bidirectional holographic codes and sub-AdS
      locality," JHEP 1601 (2016) 175, [arXiv:1510.03784]; P. Hayden, S. Nezami,
      X. L. Qi, N. Thomas, M. Walter and Z. Yang, "Holographic duality from random
      tensor networks," arXiv:1601.01694.

[22] G. W. Gibbons and S. W. Hawking, "Cosmological Event Horizons, Thermody-
      namics, and Particle Creation," Phys. Rev. D 15 (1977) 2738.

[23] A. Strominger, "The dS/CFT correspondence," JHEP 0110 (2001) 034 [hep-
      th/0106113].

[24] T. Banks and W. Fischler, "Holographic Space-time and Newton's Law,"
      [arXiv:1310.6052]; T. Banks, "Holographic Space-Time: The Takeaway,"
      [arXiv:1109.2435], "Lectures on Holographic Space Time," [arXiv:1311.0755].

[25] A. Almheiri, D. Marolf, J. Polchinski and J. Sully, "Black Holes: Complemen-
      tarity or Firewalls?," JHEP 1302 (2013) 062, [arXiv:1207.3123].

[26] J. Maldacena and L. Susskind, "Cool horizons for entangled black holes," Fortsch.
      Phys. 61 (2013) 781, [arXiv:1306.0533].

[27] S. B. Giddings, "Nonviolent nonlocality," Phys. Rev. D 88, 064023 (2013)
      [arXiv:1211.7070 [hep-th]].

[28] E.P. Verlinde, `The Hidden Phase Space of Our Universe', presentation at Strings
      2011. Lectures and Talks at the Jerusalem Winterschool in 2012, Latsis conference
      Zurich 2013, Cargese Summerschool June 2014.

                                                    47
[29] Y. Sekino and L. Susskind, "Fast Scramblers," JHEP 0810 (2008)
      065 [arXiv:0808.2096]; L. Susskind, "Addendum to Fast Scramblers,"
      [arXiv:1101.6048].

[30] J.M. Deutsch, "Quantum statistical mechanics in a closed system," Physical
      Review A 43 (4): 2046-2049.

[31] M. Srednicki, "Chaos and Quantum Thermalization," Physical Review E 50 (2):
      888 [arXiv:cond-mat/9403051v2].

[32] M. Milgrom, "A Modification of the Newtonian dynamics as a possible alternative
      to the hidden mass hypothesis," Astrophys. J. 270 (1983) 365; M. Milgrom, "A
      Modification of the Newtonian dynamics: Implications for galaxies," Astrophys.
      J. 270 (1983) 371.

[33] J. Bekenstein and M. Milgrom, "Does the missing mass problem signal the break-
      down of Newtonian gravity?," Astrophys. J. 286 (1984) 7.

[34] M. Milgrom, "MOND laws of galactic dynamics," Mon. Not. Roy. Astron. Soc.
      437, no. 3, 2531 (2014) [arXiv:1212.2568]; M. Milgrom, "MOND theory," Can.
      J. Phys. 93, no. 2, 107 (2015) [arXiv:1404.7661].

[35] R. H. Sanders, "A historical perspective on modified Newtonian dynamics," Can.
      J. Phys. 93, no. 2, 126 (2015) [arXiv:1404.0531].

[36] W. J. G. de Blok, S.S. McGaugh, J.M. Schombert, G.D. Bothun, and W.J.G. de
      Blok, "The Baryonic Tully-Fisher Relation," Astrophys.J. 533 (2000) L99-L102.

[37] S. McGaugh, F. Lelli, J. Schombert,"The Radial Acceleration Relation in Rota-
      tionally Supported Galaxies," [arXiv:1609.05917].

[38] M. Milgrom, "The modified dynamics as a vacuum effect," Phys. Lett. A 253,
      273 (1999), [astro-ph/9805346].

[39] A. Almheiri, X. Dong and D. Harlow, "Bulk Locality and Quantum Error Cor-
      rection in AdS/CFT," JHEP 1504 (2015) 163 [arXiv:1411.7041].

[40] D. Gottesman, "Stabilizer codes and quantum error correction," quant-
      ph/9705052.

[41] A. R. Brown, D. A. Roberts, L. Susskind, B. Swingle and Y. Zhao, "Complexity,
      action, and black holes," Phys. Rev. D 93, no. 8, 086006 (2016) [arXiv:1512.04993
      [hep-th]].

[42] L. Susskind and E. Witten, "The Holographic bound in anti-de Sitter space,"
      hep-th/9805114.

                                                    48
[43] J. D. Brown and M. Henneaux, "Central Charges in the Canonical Realization of
      Asymptotic Symmetries: An Example from Three-Dimensional Gravity," Com-
      mun. Math. Phys. 104 (1986) 207. doi:10.1007/BF01211590.

[44] V. Balasubramanian, B. Czech, B. D. Chowdhury and J. de Boer, "The en-
      tropy of a hole in spacetime," JHEP 1310, 220 (2013) [arXiv:1305.0856 [hep-
      th]]; V. Balasubramanian, B. Czech, B. D. Chowdhury, J. de Boer, M. Heller,
      "A hole-ographic spacetime," Phys. Rev. D 89, 086004 (2014), [arXiv:1310.4204
      [hep-th]].

[45] E.P. Verlinde, "On the Holographic Principle in a Radiation Dominated Uni-
      verse," [hep-th/0008140].

[46] B. R. Majhi and T. Padmanabhan, "Noether Current, Horizon Virasoro Algebra
      and Entropy," Phys. Rev. D 85 (2012) 084040 [arXiv:1111.1809]; "Noether cur-
      rent from the surface term of gravitational action, Virasoro algebra and horizon
      entropy," Phys. Rev. D 86 (2012) 101501 [arXiv:1204.1422].

[47] R. Nandkishore and D. A. Huse,"Many-Body Localization and Thermalization in
      Quantum Statistical Mechanics," Annual Review of Condensed Matter Physics
      Vol. 6: 15-38 (2015); D. A. Huse, R. Nandkishore, V. Oganesyan, A. Pal, S.L.
      Sondhi, "Localization protected quantum order," arXiv:1304.1158.

[48] T. Grover, "Certain General Constraints on the Many-Body Localization Tran-
      sition," arXiv:1405.1471 [cond-mat.dis-nn].

[49] E. Witten, "On the conformal field theory of the Higgs branch," JHEP 9707,
      003 (1997) [hep-th/9707093].

[50] R. M. Wald, "Black hole entropy is Noether charge," Phys. Rev. D 48, 3427
      (1993) [arXiv:gr-qc/9307038]; T. Jacobson, G. Kang and R. C. Myers, "On Black
      Hole Entropy," Phys. Rev. D 49, 6587 (1994) [arXiv:gr-qc/9312023].

[51] V. Iyer and R. M. Wald, "Some properties of Noether charge and a proposal for
      dynamical black hole entropy," Phys. Rev. D 50 (1994) 846 [gr-qc/9403028].

[52] R. Arnowitt, S. Deser, and C. W. Misner. The dynamics of general relativity.
      In L. Witten, editor, Gravitation: An Introduction to Current Research, pages
      227265. Wiley, 1962.

[53] R. M. Wald, "General Relativity," The University of Chicago Press, 1984.

[54] J.D. Brown and J.W. York Jr, "Quasilocal energy and conserved charges derived
      from the gravitational action," Phys.Rev. D, 47:1407 1419, 1993.

                                                    49
[55] L. Brewin, "A Simple expression for the ADM mass," Gen. Rel. Grav. 39 (2007)
      521 [gr-qc/0609079].

[56] J. D. Bekenstein, "A Universal Upper Bound On The Entropy To Energy Ratio
      For Bounded Systems," Phys. Rev. D 23 (1981) 287.

[57] H. Casini, "Relative entropy and the Bekenstein bound," Class. Quant. Grav. 25
      (2008) 205021 [arXiv:0804.2182].

[58] Eshelby, J.D., "The determination of the elastic field of an ellipsoidal inclusion,
      and related problems," Proceedings of the Royal Society A 241 Issue:1226, 376-
      396, (1957); Eshelby, J.D., "The elastic field outside an ellipsoidal inclusion,"
      Proceedings of the Royal Society A 252 Issue:1271, 561-569, (1959).

[59] J. M. Deutsch, "The Dynamics of Entangled Polymers," J. Phys (Paris) 48,
      141(1987).

[60] M. Rubinstein and S. P. Obukhov, "Memory Effects in Entangled Polymer
      Melts," Phys. Rev. Lett. 71 (1856).

[61] R. H. Sanders, "Resolving the virial discrepancy in clusters of galaxies with mod-
      ified newtonian dynamics," Astrophys. J. 512, L23 (1999) [astro-ph/9807023].

[62] F. R. Klinkhamer and M. Kopp, "Entropic gravity, minimum temperature,
      and modified Newtonian dynamics," Mod. Phys. Lett. A 26, 2783 (2011)
      [arXiv:1104.2022].

[63] P. V. Pikhitsa, "MOND reveals the thermodynamics of gravity,"
      [arXiv:1010.0318].

[64] C. M. Ho, D. Minic and Y. J. Ng, "Cold Dark Matter with MOND Scaling,"
      Phys. Lett. B 693 (2010) 567 [arXiv:1005.3537].

[65] D. Edmonds, D. Farrah, C. M. Ho, D. Minic, Y. J. Ng and T. Takeuchi, "Test-
      ing MONDian Dark Matter with Galactic Rotation Curves," Astrophys. J. 793
      (2014) 41 [arXiv:1308.3252 [astro-ph.CO]]; "Testing Modified Dark Matter with
      Galaxy Clusters: Does Dark Matter know about the Cosmological Constant?,"
      [arXiv:1601.00662].

[66] Y. J. Ng, D. Edmonds, D. Farrah, D. Minic, T. Takeuchi and C. M. Ho, "Modified
      Dark Matter," [arXiv:1602.00055].

                                                    50
