# 2025 Duff Nilsson Pope Kaluza Klein supergravity 2025

**Source:** `11_2025_Duff_Nilsson_Pope_Kaluza_Klein_supergravity_2025.pdf`

---

arXiv:2502.07710v1 [hep-th] 11 Feb 2025                                                       Imperial/TP/2025/mjd/1 MI-HET-851

                                                                  Kaluza-Klein Supergravity 2025*

                                                                                    M. J. Duff
                                                             Blackett Laboratory, Imperial College London

                                                                Prince Consort Road, London SW7 2AZ

                                                                                B. E. W. Nilsson
                                                     Department of Physics, Chalmers University of Technology

                                                                        SE-412 96 Go�teburg, Sweden

                                                                                    C. N. Pope
                                         George P and Cynthia Woods Mitchell Institute for Fundamental Physics and

                                              Astronomy, Texas A&M University, College Station, TX 77843 USA
                                               DAMTP, Centre for Mathematical Sciences, Cambridge University,

                                                             Wilberforce Road, Cambridge CB3 OWA, UK

                                                                                         Abstract
                                         We recall our work in the 1980s taking seriously the maximal eleven dimensions
                                         of supergravity, in particular the round, left squashed and right squashed S7 com-
                                         pactifications to D = 4 yielding N = 8, N = 1 and N = 0, respectively. This
                                         involved Kaluza-Kein techniques that have found wider applications such as spon-
                                         taneous compactification, holonomy and supersymmetry, topology versus geometry,
                                         squashing and Higgs, vacuum stability and consistent truncations.

                                         *Invited contribution to the book Half a Century of Supergravity, eds. A. Ceresole
                                         and G. Dall'Agata.
Contents

1 Why Kaluza-Klein?                              3

2 Spontaneous compactification                   3

3 Holonomy, Killing spinors and supersymmetry    5

4 Topology                                       7

5 Squashing, Higgs and space invaders            8

6 The criterion for vacuum stability             10

7 Consistent truncations                         13

8 The complete form of the squashed S7 spectrum  19

8.1 Improved formalism on general reductive coset spaces G/H . . . . . . . 19

8.2 The full spectrum on the squashed seven-sphere . . . . . . . . . . . . . . 21

                                      2
1 Why Kaluza-Klein?

Forty years ago our Physics Reports [1] began:
    "We do not yet know whether supergravity [2, 3, 4, 5] is a theory of the real world,

nor whether the real world has more than four dimensions as demanded by Kaluza-Klein
theories [6, 7, 8]. However, our research in this area has convinced us that the only way
to do supergravity is via Kaluza-Klein and that the only viable Kaluza-Klein theory is
supergravity." If we swap is for has as its low-energy limit, we think this was a fairly
accurate prophecy [1].

    Noting that that the field equations of N = 1 supergravity in D = 11 dimensions
admit of vacuum solutions corresponding to AdS4 � S7, and noting that the round S7
admits 8 Killing spinors and that its isometry group is SO(8), this gives rise via a Kaluza-
Klein mechanism to an effective D = 4 theory with N = 8 supersymmetry, local SO(8)
invariance with coupling e and cosmological constant  with G  -e2 where G is
Newton's constant [9]. Noting further that the massless sector coincides with the N = 8
gauged supergravity of de Wit and Nicolai [10], we conjectured in 1982 (in the face of
much opposition) that omission of the massive states provided a consistent truncation
[9]. The conjecture was not completely proved until 2012 [11]. It was these observations
which first aroused our interest in Kaluza-Klein theories and provided the stimulus for
our subsequent research. Other sources of inspiration included [12, 13]. Furthermore, we
noted that S7 admits a second Einstein metric, the squashed seven-sphere with N = 1
and isometry Sp2 � Sp1 [14]. A reversal of orientation (skew whiffing) leads to a different
compactification with the same isometry, but N = 0 [15]. Notwithstanding the absence
of supersymmetry, it is classically stable [16]. It was to the seven-sphere, therefore, that
the bulk of our Physics Report was devoted.

    However, the example of S7 revealed novel results and techniques that are valid in a
wider class of Kaluza-Klein theories which we shall also describe.

2 Spontaneous compactification

Soon after Nahm [17] pointed out that D = 11 is the maximum dimension for supergrav-
ity, Cremmer, Julia and Scherk [18] were able to construct the corresponding Lagrangian,
but this was regarded as a mathematical curiosity with no physical significance. A major
goal was to derive (in D = 4) the extended supergravities, especially the one with max-
imal N = 8. Cremmer and Julia [19] were able to do this using Dimensional Reduction
which simply means demanding that all fields be independent of the extra 7 coordinates.

    Gradually, however, theorists began to insist on spontaneous compactification, that
is to look for stable ground state solutions of the field equations for which the metric
describes a product manifold M4 � Xn where M4 is four dimensional spacetime with the
usual signature (-, +, +, +) and Xn is a compact internal space with Euclidean signature
(+, +, +, ...). This would yield Yang-Mills fields in D = 4 with gauge group G, where G

                                                        3
is the isometry group of Xn, with coupling constant e where

                                        e2  Gm2,                                             (1)

and m-1 is the radius of the compact manifold. For better or worse such compactifications
also typically involved a cosmological constant 

                                          -m2.                                               (2)

An important example was the Freund-Rubin compactification described below. Indeed
one of the observation that triggered our combining Kaluza-Klein and supergravity was
that combining (1) and (2) we find

                                        G  -e2,                                              (3)

as in gauged N = 8 supergravity.

The unique D = 11, N = 1 supermultiplet is comprised of a graviton gMN , a gravitino

M and 3-form gauge field AMNP , where M = 0, 1, . . . 10, with 44, 128 and 84 physical

degrees of freedom, respectively. The transformation rule of the gravitino reduces in a

purely bosonic background to          M = D~ M ,

                                                                                             (4)

where the parameter  is a 32-component anticommuting Majorana spinor, and where

              D~ M  =   DM    -   i   (N  P  QR      +  8P QRN M )FNP QR.                    (5)
                                 144              M

Here DM is the usual Riemannian covariant derivative involving the usual Levi-Civita

connection M                                    1
                                                4
                                 DM  =  M    -     M    AB  AB  ,                            (6)

A are the D = 11 Dirac matrices and F = dA. The bosonic field equations are

     RM N     -  1  gM  N  R  =  1   FMP QRFN P QR      -   1  gM  N  F  P  QRS  FP  QRS  ,  (7)
                 2               3                          8

and

                                    d  F + F  F = 0.                                         (8)

The Freund-Rubin ansatz [20] is

                                     F� = 3m�,                                               (9)

where � = 0, 1, 2, 3 and m is a constant with the dimensions of mass. This effects a
spontaneous compactification from D = 11 to D = 4, yielding the product of a four-
dimensional spacetime with negative curvature

                                     R� = -12m2g�,                                           (10)

                                             4
and a seven-dimensional internal space of positive curvature

                                   Rmn = 6m2gmn,                                    (11)

where m = 1, 2, . . . 7. Accordingly, the supercovariant derivative also splits as

     D~ � = D� + m�5,                                                               (12)

and                                          1
                                             2
     D~ m                          =  Dm  -     mm  .                               (13)

If we choose the spacetime to be maximally symmetric but leave the internal space X7

arbitrary, we are led to the D = 11 geometry AdS4 � X7. The first example was pro-
vided by the choice X7 = round S7 [9, 1] which is maximally supersymmetric1. The

next example was the round S7 with parallelizing torsion [21] which preserves no super-

symmetry. However, it was also of interest to look for something in between, and this is

where holonomy comes to the fore.

3 Holonomy, Killing spinors and supersymmetry

Crucial to the whole programme of Kaluza-Klein supergravity are the notions of Killing
spinors [22, 1] and holonomy groups [14, 15, 1]. In 1981, Witten laid down the criterion
for spacetime supersymmetry in Kaluza-Klein theory [12]. The number of spacetime
supersymmetries is given by the number of covariantly constant spinors on the compacti-
fying manifold. To see this, we look for vacuum solutions of the field equations for which
the the gravitino field  vanishes. In order that the vacuum be supersymmetric, there-
fore, it is necessary that the gravitino remains zero when we perform a supersymmetry
transformation and hence that the background supports spinors  satisfying

                                   D~M  = 0.                                        (14)

In the case of a product manifold, this reduces to

                                   D~� (x) = 0,                                     (15)

and                                D~m (y) = 0,

                                                                                    (16)

where (x) is a 4-component anticommuting spinor and (y) is an 8-component commut-
ing spinor. The first equation is satisfied automatically with our choice of AdS4 spacetime

    1The first Ricci flat (m = 0) example of a compactification of D = 11 supergravity was provided by
the choice X7 = T 7 [19] which is also maximally supersymmetric.

                                      5
and hence the number of D = 4 supersymmetries, 0  N  8, devolves upon the number
of Killing spinors on X7. They satisfy the integrability condition

[D~ m,  D~ n]  =  -  1  Cmnab  ab                   =  0,  (17)
                     4

where Cmnab is the Weyl tensor.
    As pointed out in [23] covariantly constant spinors, or Killing spinors are, in their

turn, related to the holonomy group of the corresponding connection. It was well known

that the number of massless gauge bosons was determined by the isometry group of the

compactifying manifold, but it turned out to be the holonomy group that determined

the number of massless gravitinos. The subgroup of Spin(7) generated by these linear

combinations of Spin(7) generators ab corresponds with the holonomy group H .
    The first non-trivial example was provided in 1982 [14] by compactifying D = 11

supergravity on the squashed S7, an Einstein space whose whose G2 holonomy yields

N = 1 in D = 4. Here we are referring to the holonomy of the supercovariant derivative
D~m that appears in (13). This differs from the Riemannian or Levi-Civita derivative Dm
that you find in the maths textbooks. Similarly, the round S7 has trivial holonomy and

hence yields the maximum N = 8 supersymmetry [22].

    From the Riemannian perspective, G2 corresponds to the weak holonomy of S7. A
7-dimensional Einstein manifold with Rmn = 6m2gmn has weak holonomy G2 if it admits

a 3-form A obeying

        dA = 4m  A.                                        (18)

That such a 3-form exists on the squashed S7 can be proved by invoking the single
(constant) Killing spinor . The required 3-form is then given by [15]

        Amnp = �mnp.                                       (19)

    Although the phenomenologically desirable N = 1 supersymmetry and non-abelian
gauge groups appear in four dimensions, the resulting theory was not realistic, being
vectorlike with gauge group Sp2 � Sp1 and living on AdS4. It nevertheless provided
valuable insight into the workings of modern Kaluza-Klein theories. Forty years later,
G2 manifolds continue to play an important role in D = 11 M-theory for the same
N = 1 reason. But the full M-theory, as opposed to its low energy limit of D = 11
supergravity, admits the possibility of singular G2 compactifications which can yield
chiral (N = 1, D = 4) models living in Minkowski space and with realistic gauge groups
[24, 25].

    Owing to this generalized connection, vacua with m = 0 present subtleties and novel-
ties not present in the m = 0 case, for example the phenomenon of skew-whiffing [15, 1].
For each Freund-Rubin compactification, one may obtain another by reversing the orien-
tation of X7. The two may be distinguished by the labels left and right. An equivalent
way to obtain such vacua is to keep the orientation fixed but to make the replacement
m  -m. So the covariant derivative (13), and hence the condition for a Killing spinor,

                     6
changes but the integrability condition (17) remains the same. With the exception of
the round S7, where both orientations give N = 8, at most one orientation can have
N  0. This is the skew-whiffing theorem. A corollary is that other symmetric spaces,
which necessarily admit an orientation-reversing isometry, can have no supersymmetries.
Examples are provided by products of round spheres. Of course, skew-whiffing is not
the only way to obtain vacua with less than maximal supersymmetry. A summary of
known X7, their supersymmetries and stability properties is given in [1]. Note, however,
that skew-whiffed vacua are automatically stable at the classical level since skew-whiffing
affects only the spin 3/2, 1/2 and 0- towers in the Kaluza-Klein spectrum, whereas the
criterion for classical stability involves only the 0+ tower [16, 1].

    Once again the squashed S7 provided the first non-trivial example: the left squashed
S7 has N = 1 but the right squashed S7 has N = 0. Interestingly enough, this means
that setting the suitably normalized 3-form equal to the D = 11 supergravity 3-form
provides a solution to the field equations, but only in the right squashed case. This
solution is called the right squashed S7 with torsion [15] since Amnp may be interpreted
as a Ricci-flattening torsion [21]. Other examples were provided by the left squashed
N(1, 1) spaces [26], one of which has N = 3 and the other N = 1, while the right
squashed counterparts both have N = 0.

    All this presents a dilemma. If the Killing spinor condition changes but the integra-
bility condition does not, how does one give a holonomic interpretation to the different
supersymmetries? Indeed N = 3 is not allowed by the usual rules. The answer to
this question may be found in a paper [27] written before we knew about skew-whiffing.
The authors note that in (13), the SO(7) generators ab, augmented by presence of
a, together close on SO(8). Hence one may introduce a generalized holonomy group
Hgen  SO(8) and ask how the 8 of SO(8) decomposes under Hgen. In the case of the
left squashed S7, Hgen = SO(7)-, 8  1 + 7 and N = 1, but for the right squashed S7,
Hgen = SO(7)+, 8  8 and N = 0. For more on generalized holonomy, see [28, 29].

    If the space is not simply connected there may be further global obstructions to the
existence of unbroken supersymmetries. For example, solutions of the form T 7/ and
S7/, where  is a discrete group, admit fewer than 8 Killing spinors. A prominent
example of the latter is provided by the ABJM theory [30].

4 Topology

In [22] it was pointed out that Euclidean signature field configurations and their topo-
logical properties (Betti numbers, Euler numbers, Pontryagin numbers, holonomy, index
theorems etc) which feature in gauge and gravitational instanton physics can lead a
second life as internal manifolds Xn appearing in the compactification of the n extra
dimensions in Lorentzian signature Kaluza-Klein theory MD = MD-n � Xn.

    The first non-trivial example of this kind was provided by the K3 manifold2 which is

    2K3 had already entered the physics literature through gravitational instantons [31] and non-linear

                                                        7
four-dimensional, self-dual, and Ricci flat without isometries [22]. It's SU(2) holonomy
yields half the maximum supersymmetry, e.g., (N = 2, D = 6) for K3 and (N =
4, D = 4) for K3 � T 2 starting from (N = 1, D = 10)3. For the first time, the Kaluza-
Klein particle spectrum was dictated by the topology rather than the geometry of the
compactifying manifold. It was thus a forerunner of the six-dimensional Ricci-flat Calabi-
Yau compactifications [34], whose SU(3) holonomy yields (N = 1, D = 4) starting from
(N = 1, D = 10), and the seven-dimensional Ricci-flat Joyce compactifications [35, 36]
whose G2 holonomy yields (N = 1, D = 4) starting from (N = 1, D = 11). K3 continues
to feature prominently in M-theory and its dualities.

    Concerning Calabi-Yau, in 1983 the three authors were visiting Steve Weinberg's
group in Texas. We had recently realized the role played by holonomy in fixing the
fraction of supersymmetry that survives compactification. Having noted that (N =
1, D = 10) supergravity on K3 � T 2 yields (N = 2, D = 4), we then asked ourselves
whether there was an SU(3) analogue yielding (N = 1, D = 4). However, this took us
beyond our mathematical competence, so we went over to the Math Department and
spoke to a well-known geometer who was there at the time. Now we do not want to
blame him, because perhaps we physicists did not articulate clearly what we wanted, but
in any event we came away with the impression that there was no known SU(3) analogue.

    Hence the statement in our paper [22] "we do not know of any solutions... with
H = SU(3)".

5 Squashing, Higgs and space invaders

It was realized already in the early 1980s [37, 15, 1] that the process in which the AdS4
supergravity theory with eight supersymmetries based on the round S7 compactification
is turned into a similar theory based on the left squashed S7 involves various kinds
of Higgs effects4. In particular it was noticed that the eight massless spin-3/2 Rarita-
Schwinger fields responsible for the supersymmetries in AdS4 behave in an unexpected
and interesting way. Instead of being subjected to a standard super-Higgs effect where one
of the eight supersymmetries in the round vacuum survives the squashing one finds that
the eight spin-3/2 fields in a spinor irrep of SO(8) all become massive when the isometry
group breaks from SO(8) to Sp2 � Sp1. This part of the story therefore constitutes a
slightly non-standard super-Higgs effect. In this process the corresponding Goldstinos
must arise in the breaking of the round AdS4 spectrum only to have disappeared in the
squashed vacuum since they are eaten in the process. This has recently been verified to

sigma models [32].
    3In [33] it was pointed out that D = 11 supergravity on R10-n � K3 � T n-3 and the D = 10 heterotic

string on R10-n � T n not only have the same supersymmetry but also the same moduli space of vacua,
namely SO(16 + n, n)/(SO(16 + n) � SO(n)).

    4That deforming the S7 and torsion corresponded to non-zero vevs for scalars and pseudoscalars was
recognised in [37]. But it was [38] that identified the Sp2 � Sp1 singlet in the 300 of SO(8) as the source
of squashing in the Squashed S7.

                                                        8
be compatible with details of the two spectra involved here [39, 40, 41].
    The issue of where the single massless Rarita-Schwinger field in the squashed AdS4

vacuum is coming from was on the other hand established in the 1980s. It was referred
to as the space invaders scenario [1] since here a singlet massive Rarita-Schwinger field,
which is produced in the breaking of a particular round sphere irrep, zooms down to
become massless. It was checked using the results in [42] that this singlet could be traced
under squashing to the new vacuum and that it indeed becomes the massless field needed
to explain the single supersymmetry in this vacuum. Due to the fact that the breaking
pattern is different when going to the right squashed vacuum it is easy to see that this
does not happen there.

    What was not investigated in the early literature on this subject was what happens
to the singlet Goldstino that necessarily must be spat out in this de-Higgsing of the
massive spin-3/2 singlet field. A possible explanation was suggested in [39] and to some
extent verified in [40] by an explicit construction of all the squashed S7 singlet mode
functions5. What seems to be happening is that the singlet spin-3/2 mode that exists
in the squashed S7 spectrum but not in the round one gives rise to a spin-1/2 field that
belongs to a Wess-Zumino multiplet in the N = 1 left squashed theory but generates a
singlet fermionic massive field in the right vacuum. The fact that this spin-3/2 mode is
not present in the round vacuum seems to indicate that an AdS4 field must be eating it
when returning to the round theory. A plausible explanation is that the massless spin-
3/2 field eats it when going from the left vacuum to the round one and a singleton when
going back from the right vacuum.

    To summarize the situation described above in a bit more explicit terms we recall
from [40] that the singlet spinorial modes in the different vacua are: One spin-1/2 and
no spin-3/2 in the round S7 SO(8) spectrum broken down to the squashed isometry
Sp2 � Sp1, and in the left and right squashed vacua, one spin-1/2 and one spin-3/2.

    The modes are of course the same on the left and right spheres but their operator
eigenvalues differ, when letting m  -m, which will affect the masses of the correspond-
ing spin-1/2 and 3/2 fields in the AdS4 theory. To explain this mode-field connection we
recall that, via the mass-operator relations (see, e.g., [1]), spin-3/2 modes generate only
spin-1/2 fields in AdS4 while spin-1/2 modes give rise to both spin-1/2 and 3/2 fields in
AdS4. The modes listed above therefore imply the following AdS4 singlet field content
in the various cases [40]:

Round vacuum: One massive spin-3/2 field and one massive spin-1/2 field both com-

    5We emphasize here that this and the following discussions will often refer to modes and fields. These
must be kept apart: modes refer to Fourier modes used in the expansions of tensor fields on S7 while fields
always are objects in the effective low energy field theory in AdS4. Fields in AdS4 are in unitary irreps
of SO(2, 3) denoted D(E0, s) where E0 is the energy value of the lowest weight in the weight diagram
and s its spin [43]. Modes and fields are, however, connected through relations like E0 = E0(M 2),
M 2 = M 2(p) and p = p(CG) where CG is the Casimir of the isometry group G. For details, see [1]
and for the squashed S7 case the more recent and complete results in [44, 41]. Partial results can also
be found in [45].

                                                        9
patible with the N = 8 supersymmetric SO(8) spectrum broken down to Sp2 � Sp1.
Left squashed vacuum: One massless spin-3/2 field and two massive spin-1/2 fermions
all compatible with N = 1 supersymmetry.
Right squashed vacuum: One massive spin-3/2 field, together with one massive spin-
1/2 and one spin-1/2 singleton field.

    The only way to make these three cases compatible with each other seems to be to
introduce a new kind of Higgs effect whereby a singleton can absorb a massive field of
the same spin to become a new massive field. This way both the left and right squashed
singlet spectra can be related to the round one, and to each other. Note that in both
squashed cases a spin-1/2 field must be eaten since it does not appear in the round
spectrum. In the left case it is the massless spin-3/2 field that is doing the eating and in
the right case it is the fermionic singleton.

    As argued in [41] we can use the results of [42] to follow the massless spin-1/2 field
in the irrep (0, 0; 2), that is the superpartner of the gauge field in this irrep in the left
squashed vacuum, back to the round S7. It turns out that it ends up as a singleton in
the round case.

6 The criterion for vacuum stability

The question of whether or not a particular vacuum solution in supergravity is stable
can be addressed at various levels. The most basic one concerns the classical stability of
the solution. Since the equations of motion are non-linear, addressing even this classical
question can be quite tricky, but at the linearised level, it becomes relatively straight-
forward. Thus one can linearise the equations of motion around the chosen "vacuum,"
i.e. the background solution, and study the modes describing the linearised fluctua-
tions. In the Kaluza-Klein context, this amounts to studying the spectra of all towers
of lower-dimensional fields. The signal for a classical instability would then be if any of
the lower-dimensional modes had a complex frequency, since the imaginary part would
be associated with a fluctuation that could grow exponentially in time.

    If the lower-dimensional background were just a Minkowski spacetime then the cri-
terion for classical linearised stability would simply be that the masses of all the modes
should be real. However, because we are concerned here with anti-de Sitter ground
states, account must be taken of the fact that it is now AdS representations, rather than
Poincar�e representations, that are relevant. This was addressed in detail in the work of
Breitenlohner and Freedman [46]. The upshot is that scalar fields in four-dimensional
AdS spacetime can actually have unitary representations (with real frequencies) even if
the (mass)2 is negative, provided that it is not too negative. Specifically, the criterion is
that if the mass obeys M2  -m2, where the cosmological constant of the AdS4 space-
time is given by R� =  g� and  = -12m2, then the representation will be unitary.
This is the so-called Breitenlohner-Freedman (BF) bound.

    A detailed analysis of the mass spectrum for an arbitrary Freund-Rubin compacti-

                                                       10
fication of eleven-dimensional supergravity was described in [1], with the mass spectra

of the various four-dimensional fields given in terms of the eigenvalue spectra of certain

differential operators on the internal seven-dimensional compactifying space. It turns out

that there is only one tower of four-dimensional modes that is at risk of giving rise to

classical instabilities [16], and that is one of the scalar field towers for which the masses

are given by

                                                M 2 = L - 4m2 ,                                         (20)

where L is the Lichnerowicz operator that acts on transverse, tracefree symmetric ten-
sors Ymn on the internal seven-dimensional manifold:

L Ymn = - Ymn - 2Rmpnq Y pq + 2R(mp Yn) p , m Ymn = 0 , gmn Ymn = 0 . (21)

Thus the criterion for classical linearised stability is that the eigenvalues of the Lich-
nerowicz operator should be such that [16]

                                                     L  3m2 .                                           (22)

    Establishing the classical stability of a given Freund-Rubin background thus reduces

to the problem of finding the lower bound on the eigenvalues of the Lichnerowicz operator

on the compact Einstein seven-manifold X7.

    It can be shown straightforwardly that any X7 that admits Killing spinors will be such
that L  3m2 [16], and thus all supersymmetric compactifications will be classically

stable. This accords with the usual expectation that supersymmetry protects solutions

against instabilities. It is also noteworthy that for any X7 admitting fewer than the
maximal N = 8 Killing spinors of the round S7, then if the orientation of the manifold is

reversed the resulting compactification will admit no supersymmetries. Thus classically,

these "skew-whiffed" non-supersymmetric compactifications will also be classically stable

[1, 16].

    It can easily be seen that if X7 is a direct product of two Einstein manifolds, X7 =

X(1) � X(2), where the two product manifolds have dimensions N1 and N2, then an

unstable mode can constructed very simply, by taking Ymn to be of the form Ymn =
          g(1)           g(2)
diag  (1    m1 n1  ,  2    m2 n2  ),  where  1  and  2  are  constants  such  that  N1 1 + N2 2  =  0.  This

mode describes a perturbation in which one factor in the product expands uniformly

while the other contracts, keeping the overall volume of X7 fixed. It can easily be seen
that it has eigenvalue L = 0, and hence it violates the BF stability condition (22).

    In general, the investigation of the classical stability of a given Freund-Rubin com-

pactification requires a detailed study of the spectrum of the Lichnerowicz operator on

X7. This was carried out for various classes of coset-space examples in [47, 48, 26].
The technique employed in these papers was to show by an integration by parts on the

compact Einstein manifold X7 that

    Y mn L Ymn dV =                       -4Y mn Rmpnq Y pq +24m2 Y mn Ymn+3(m Y np m Ynp) dV .

X7                                    X7

                                                                                                        (23)

                                                        11
Since the last term on the right-hand side is manifestly non-negative, this means that the

Lichnerowicz operator can be bounded from below in terms of the upper bound on the

eigenvalues of the Riemann tensor. That is to say, the Riemann tensor has 27 eigenvalues

, defined by

                                   Rmpnq X pq =  Xmn ,                                          (24)

where Xmn denotes a symmetric eigentensor. Because the X7 manifolds considered in
[47, 48, 26] were all coset spaces, the eigenvalues  were all simply constants. A criterion
(22) for classical vacuum stability will then be satisfied for all the modes if the condition

                                   max            21  m2  ,                                     (25)
                                                  4

holds, where max denotes the largest eigenvalue of the Riemann tensor. Since the Rie-
mann tensor can be calculated explicitly for all the coset space examples, this means

that the eigenvalues can be obtained explicitly too. Note that the inequality (25) is a

sufficient condition for classical stability, but it is not necessarily necessary.

    As an example, consider the class of Mmn coset spaces that were discussed in [47],

which can be thought of as taking the form SU(3) � SU(2)/(SU(2) � U(1)), with the

integers m and n characterising the embedding of the denominator group in the numer-

ator. If m = 3 and m = 2 there exist two Killing spinors, and the vacuum has N = 2

supersymmetry; this case, of course, will necessarily be classically stable. There exists

an Einstein metric on Mmn for all integers m and n. It was shown in [47] that of the

27  eigenvalues  of  the  Riemann  tensor,  26  always  satisfy  the  stability  bound      21  m2,
                                                                                            4
and so the possibility for a classical instability hinges upon the 27th eigenvalue, which is

max. This turns out to violate the bound (25) if the ratio 2m/(3n) lies sufficiently far

away, in either direction, from the 2m/(3n) = 1 supersymmetric case. This establishes

that in cases outside the range Cmin  2m/(3n)  Cmax, the possibility of a classical
instability is not ruled out. It was furthermore then shown in [47], by explicit construc-

tion, that a mode that violates the bound (25) does in fact exist if 2m/(3n) < Cmin
or 2m/(3n) > Cmax. Thus putting these results together, it was shown that the Mmn

Freund-Rubin compactifications are classically stable if Cmin  (2m/(3n)  Cmax, and

that they are classically unstable otherwise [47].

    A much more difficult case to analyse is if one is considering an inhomogeneous

metric on the compact manifold X7. One could, for example, consider inhomogeneous
Einstein metrics on S7. As was shown by Bohm [49], there exists a discrete infinity

of inequivalent Einstein metrics in this class. There exist no Killing spinors in any

of the inhomogeneous metrics, and so there is no particular reason to expect that the

corresponding Freund-Rubin vacuum solutions would be classically stable. The Bohm

metrics are of cohomogeneity one, so the analysis of the Lichnerowicz operator involves

the study of ordinary differential equations. Some procedures for obtaining numerical

bounds on the eigenvalues of the Lichnerowicz operator were discussed in [50].

    In the last decade, the issue of the stability of AdS compactifications has become one

of the key questions addressed in the Swampland project. It has been conjectured by

                                                12
Ooguri and Vafa [51] that any non-supersymmetric compactification containing an AdS
factor must be unstable. Of the many such compactifications that have appeared over the
years a vast majority have already been proven unstable by appealing to various kinds of
decay modes. As it turns out, the right-squashed S7 is one of a very small number that
has still not been proven to be unstable. This remains an interesting topic for further
research.

7 Consistent truncations

Kaluza-Klein supergravity has evolved in many different ways in the period since the
publication of our Physics Reports [1]. Some of these have been as a consequence of
totally unexpected developments, of which perhaps the most surprising was the AdS/CFT
correspondence, which was first conjectured in 1997 [52, 53, 54].

    In the years following the writing of our Physics Reports the notion that the four-
dimensional theories obtained by compactifying D = 11 supergravity on a compact coset
space such as a sphere might directly be interpretable as candidate theories of the real
world was becoming less and less tenable. For one thing, it would be difficult, to say
the least, to reconcile the concomitant huge negative cosmological constant with our
everyday experience and with astronomical observations. It had also been shown by
Witten that there would never be any hope of obtaining a four-dimensional theory with
a chiral fermionic sector, which would be more or less a sine qua non for any realistic
theory of the world [12]. At the same time, dramatic progress was being made in string
theory, with the floodgates opening on the development of quasi-realistic four-dimensional
models, following the breakthrough paper of Candelas, Horowitz, Strominger and Witten
on the compactification of the heterotic string on Calabi-Yau 3-folds [34].

    Impressive and elegant though the new string theory results were, this new direction
in the quest for a unifying theory was perhaps a little disappointing for those who had
been working previously in Kaluza-Klein supergravity. One of the most appealing aspects
of the traditional Kaluza-Klein approach, which had attracted many researchers, was the
idea that the local symmetries of the gauge fields in the lower dimensional theory found
their origin in the geometrical symmetries (isometries) of the compactifying space. By
contrast, in the Calabi-Yau compactifications of the heterotic string the internal Calabi-
Yau manifold has no continuous symmetries at all, and the gauge fields that are present
in the lower dimension are more or less the same, or a subset, of those that were already
present in ten dimensions.

    It was at this point, in 1997, that the AdS/CFT correspondence burst onto the scene.
Suddenly, supergravity compactifications with AdS vacua were fashionable again. All the
technology that had been developed in the halcyon days of the coset compactifications
had an application again. No longer, admittedly, in the role of providing (or failing to
provide) realistic four-dimensional unified theories of the fundamental forces, but as the
key player on one side of the new duality symmetries, relating properties of classical
fields in AdS supergravity in D + 1 dimensions to the quantum properties of operators

                                                       13
in D-dimensional boundary conformal field theories at strong coupling.
    As well as providing a new arena in which the coset compactifications of supergravities

had a leading role, the AdS/CFT correspondence gave a new stimulus to another aspect
of the coset compactifications, which had long been a source of fascination to those who
had played around with the Kaluza-Klein reductions, but which had perhaps always
seemed a bit like a solution in search of a problem. The object of this fascination is the
notion of consistent reductions.

    The earliest Kaluza-Klein compactifications that were considered involved just re-
ducing a higher-dimensional theory on a circle. The idea then is that one assumes all
the higher-dimensional fields are independent of the circle coordinate, say z. One can
think of this as first performing Fourier expansions of all the higher-dimensional fields
with respect to the z coordinate, and then retaining only the zero mode in each of the
Fourier expansions. The resulting lower-dimensional theory is then guaranteed to be
a consistent truncation of the complete lower-dimensional theory, comprising infinitely-
many fields, that would have been obtained if all the infinite towers of Fourier modes had
been retained. The notion of consistency here means that any solution of the truncated
lower-dimensional theory will also be a solution of the full untruncated theory. To put it
another way, any solution of the lower-dimensional truncated theory will lift, by invert-
ing the Kaluza-Klein reduction step, to give a solution of the original higher-dimensional
theory.

    One way of stating the consistency of the truncation is that prior to truncation, the
full lower-dimensional equations of motion for the untruncated non-zero mode fields will
be such that it is consistent to set all the non-zero mode fields to zero. That is to say,
there cannot be any source terms in the full non-zero mode equations that are formed
purely from the zero-mode fields that are eventually to be retained. It is easy to see
in this example why this is guaranteed to be true. Namely, the non-zero mode fields
are all charged under the U(1) symmetry group that acts on the circle, while the zero-
mode terms are all uncharged. No matter how non-linear the equations may be, it is
impossible for powers of purely uncharged fields to generate a term that could act as a
source for a charged field. Put yet another way, the consistency is guaranteed because
one is truncating to the singlet sector of the U(1) group that acts on the circle.6

    The consistency of the truncation in the circle reduction generalises immediately to
the multi-step reduction on a number of circles; that is, a reduction on a torus. It also

    6Of course, for the argument of consistency to work, it is essential to retain all the singlet fields
in the truncation. An example where consistency in a circle reduction would fail is if one reduced
five-dimensional pure gravity on a circle, and failed to retain all the U (1) singlets in the truncated four-
dimensional theory. The full set of singlets comprises the four-dimensional metric, the Kaluza-Klein
vector originating from the mixed (�z) components of the higher-dimensional metric g^MN , and the
dilatonic scalar originating from the (zz) component of g^MN . In some early attempts at Kaluza-Klein
reduction the dilatonic scalar was erroneously truncated out, seemingly giving a nice Einstein-Maxwell
theory in four dimensions. However, the solutions of Einstein-Maxwell do not lift back to solutions of
the five-dimensional Einstein theory, because the Maxwell field would actually act as a source, via an
F � F� term, for the dilaton that was supposedly set to zero.

                                                       14
straightforwardly generalises to another class of reductions, where the compactifying
space is taken to be a group manifold G. The manifold G admits a bi-invariant metric,
invariant under independent left and right actions of the group G. Each of these groups
GL and GR acts transitively on G. As was observed by Bryce DeWitt in 1963, one can
write down a reduction ansatz for a higher-dimensional metric in which the gauge bosons
of just one of these symmetry factors, say GR, are retained [55]. This is guaranteed to
be a consistent reduction, because the fields that are being retained comprise all the
singlets under the action of the group GL, while all the fields that have been truncated
are non-singlets under GL. The consistency follows because powers of GL singlets cannot
act as sources for GL non-singlets. Because GL acts transitively, there will be just a
finite number of fields in the truncated subset. Consistent reductions of this kind are
sometimes referred to as DeWitt reductions.

    The consistency of a reduction on a general coset space G/H is a totally different
story. First, we should clarify that the truncations we have in mind in all these cases are
ones in which one retains, among other fields, the gauge bosons of the isometry group
G of the coset. In other words, we are interested in consistent truncations where the
original Kaluza-Klein dream of obtaining the gauge symmetries of the lower-dimensional
fields from the geometric isometry symmetries of the compactifying manifold is realised.
This was an idea that had occurred to Pauli in 1953. He wrote a letter to A. Pais,
proposing the idea that one might reduce six-dimensional Einstein gravity on a 2-sphere,
thereby obtaining a four-dimensional theory with SU(2) Yang-Mills fields (they weren't
called Yang-Mills fields in those days). But he also killed off his own idea in the same
letter, because he had appreciated that it would not be a consistent reduction. (An
account of this early proposal for a non-abelian Kaluza-Klein reduction can be found in
[56, 57].) In terms of the discussion given above, if one expanded the components of the
six-dimensional metric in terms of spherical harmonics on the 2-sphere, then one would
find that the non-zero modes in the expansion of the four-dimensional metric components
(i.e. spin-2 tensor fields in four dimensions) would have source terms built from the SU(2)
Yang-Mills fields one wishes to retain. Thus it would be inconsistent to set the massive
spin-2 fields to zero.

    Blissfully ignorant of the potential pitfalls ahead, in the early 1980s we and others
in the supergravity community began to explore the idea of obtaining four-dimensional
SO(8)-gauged N = 8 supergravity by compactifying D = 11 supergravity on the 7-
sphere. All the portents in a linearised analysis looked good; the sphere has an SO(8)
isometry, and the Freund-Rubin AS4 � S7 vacuum solution has N = 8 supersymmetry
[9].

    The first person to rain on the parade was Gary Gibbons, who simply said "it won't
work." He even went so far as to declare that he would "eat his hat" if it worked.
When we finally understood what he was talking about, we realised that indeed he had a
point; this was seemingly a situation very like the one Pauli had encountered thirty years
before (although we didn't know about Pauli's attempts back then). Indeed, it looked
dangerously likely that the truncation would not be consistent beyond the linearised level;

                                                       15
the SO(8) Yang-Mills fields would seemingly act as sources for massive spin-2 fields in
the four-dimensional Kaluza-Klein towers. We persevered anyway, somehow convincing
ourselves that "the 7-sphere knows what it's doing," and that something would emerge
to save the day. And indeed, not long after, we found a glimmer of hope in a calculation
we did with Nick Warner [58]. We examined the expected leading-order stumbling block
to the consistency of the truncation, namely the term where quadratic products of SO(8)
Yang-Mills fields would act as sources for massive spin-2 fields. Remarkably, it turned out
that the coefficient of this dangerous coupling was exactly zero, by virtue of a seemingly
miraculous conspiracy between two separate contributions, one being from the metric
contribution in the Einstein equations (just as Pauli would have had), and the other
being a contribution from the SO(8) gauge fields in the reduction ansatz for the eleven-
dimensional 4-form field strength and its energy-momentum tensor. So indeed it seemed
the 7-sphere "knew what it was doing," but in a rather subtle way that involved a
conspiracy with the D = 11 supergravity theory as well. It gave us hope that the
miracles would continue, and that the consistency of the truncation would persist to all
orders.

    Not long after that, in a true tour de force, Bernard de Wit and Hermann Nicolai
constructed a complete metric reduction ansatz, and provided a demonstration of the
full consistency of the 7-sphere truncation [59] (a few loose ends involving the explicit
forms of some of the components of the 4-form reduction ansatz were only sorted out a
while later; see, for example, [11, 60]).

    To those who had been involved in the efforts to demonstrate the consistency of the
reduction, it was almost magical the way the pieces of the puzzle fitted together, and the
whole picture was one of great beauty. Not everyone shared the wonderment, however,
and it was not uncommon in those days to face scepticism, or worse, from audience
members at a seminar whose reaction was along the lines of "why should we care about
consistency, we are only interested in the low-energy effective theory anyway."

    Undeterred, others who appreciated the elegance of the Pauli type of consistent reduc-
tions continued investigating other instances where they can arise. A nice example was
obtained by Horatiu Nastase, Diana Vaman and Peter van Nieuwenhuizen, where they
constructed the consistent reduction of D = 11 supergravity on the 4-sphere, thereby
arriving at maximal gauged supergravity in seven dimensions [61, 62]. This example
is actually rather simpler than the 7-sphere reduction, largely because the scalar field
sector of the reduction is easier to handle.7 In fact, the 4-sphere reduction pointed the
way to various other examples of consistent reductions, including the SL(2, R)-singlet
subsector of the consistent truncation for the 5-sphere reduction of type IIB supergravity
[63]. The construction of the full consistent truncation of type IIB supergravity on S5,
to give maximal gauged supergravity in five dimensions, proved to be more recalcitrant,
owing once again to a rather tricky scalar sector, and it was only following another crucial
development, to be chronicled below, that this one was finally achieved.

    7It is always the scalar sector that creates the biggest headaches in the construction of consistent
truncations.

                                                       16
    One nice footnote to these developments takes us forward to 2006, when a conference
in honour of Gary Gibbons' 60th birthday took place in Cambridge. Hermann Nicolai
had secretly arranged with Fitzbillies in Cambridge to create a cake in the shape of a
hat, and at the end of his talk at the conference Hermann presented Gary with the cake
and invited him to eat his hat. Very gamely, Gary proceeded to consume it in front of
the conference audience, thus fulfilling a promise he had made more than twenty years
before.

    Things began to change, in some quarters at least, with the developments in the
AdS/CFT correspondence. Now, properties of the AdS field theories that arose from
the sphere reductions of higher-dimensional supergravities translated into properties of
the amplitudes for quantum operators on the CFT side of the duality. It could be very
helpful to know whether or not one was dealing with a properly self-contained subset
of the complete towers of lower-dimensional fields in the AdS background. Also, the
existence of a consistent truncation meant that one could sometimes exploit it in order to
construct exact solutions in the higher dimension by starting with more easily constructed
exact solutions in the lower dimension, and then lifting them up by using the consistent
reduction ansatz in reverse.

    One important application of the AdS/CFT correspondence is the ABJM theory [30],
which provides a holographic dual of M-theory compactified on AdS4 � S7/Zk, thus
providing a holographic description of the 3-dimensional world-volume theory of M2-
branes. The near-horizon geometry of the M2-brane is AdS4 �S7 [64]. In fact some of the
ideas employed in the ABJM theory were foreshadowed by a paper written almost 25 years
previously [65], where it was observed that since the 7-sphere can be viewed as a U(1)
bundle over CP3 , one could make a Kaluza-Klein reduction of the S7 compactification
of D = 11 supergravity on the Hopf circle, and interpret it as compactification of D = 10
type IIA supergravity on CP3 = SU(4)/U(3). Keeping only the U(1) singlets in the
usual fashion, this means that only an N = 6 supersymmetry survives, since the 8 of
SO(8) gravitini from S7 decompose as a 60 + 12 + 1-2 under SU (4) � U (1). Of course,
the truncation is guaranteed to be a consistent one.

    The next major development in the story of consistent reductions takes us into the
realm of generalised geometry and exceptional field theory (ExFT). Perhaps one of the
earliest precursors of these ideas goes back to another paper by de Wit and Nicolai, in
1985 [66], where they showed how D = 11 supergravity could be written in terms of four-
dimensional fields in a manner suggestive of the way one would carry out a consistent
truncation on the 7-torus, but without actually making any truncation of the fields. This
new formulation of the D = 11 theory has a local SU(8) invariance, with the bosonic
quantities relating to the scalar fields carrying 56 and 133 dimensional representations
of the E7(7) Cremmer-Julia global symmetry of the usual toroidally-compactified the-
ory. The idea of adding extra coordinates in the description of duality symmetries in
membrane theory was also introduced, in [67].

    The notions of generalised geometry and exceptional field theory push the ideas of
de Wit and Nicolai further. In order to exploit the symmetries further, one now in-

                                                       17
troduces additional coordinates, in order to reformulate the supergravity theory in such
a way that the E7(7) Cremmer-Julia global symmetry of the 7-torus truncation is now
realised as a symmetry of the extended theory without any truncation being performed.
Geometric structures, such as a generalised Lie derivative, are then defined on the ex-
tended space. The corresponding algebra of generalised diffeomorphisms closes, provided
that one imposes a so-called section condition. The section condition itself is written
in an E7(7)-covariant way. Any specific solution of the section condition amounts to a
restriction in which the fields are allowed to depend only on a subset of the extended
system of coordinates, and correspondingly the E7(7) symmetry is broken.8 However,
since the formulation of the extended theory itself is E7(7) covariant, prior to choosing
a specific solution to the section condition, this provides a framework within which the
E7(7) symmetry can be employed in order to construct truncations whose consistency
can be understood rather straightforwardly. In fact it turns out that the formalism can
provide an understanding of why a non-trivial Pauli type of sphere reduction can actually
yield a consistent truncation. Essentially, it can be recast as a statement of truncation to
fields that are singlets under the enlarged symmetry group of the extended formulation,
thereby making the consistency of the truncation manifest.

    As stated above, the construction was rather specific to reformulating D = 11 su-
pergravity in an extended (4 + 7)-dimensional language. Similar reformulations in an
([11 - n] + n)-dimensional language are also possible for a range of n, corresponding to
the cases where the there would be an En(n) global symmetry in a consistent truncation
on the n-torus. An analogous set of generalisations of type IIB supergravity, viewed from
a ([10 - n] + n)-dimensional standpoint, are also possible. One of these, namely the
(5 + 5) generalisation, was employed a few years ago to realise the long-standing goal of
constructing the consistent truncation of type IIB supergravity on S5, yielding maximal
gauged five-dimensional supergravity [68]. In another notable paper, the methods of gen-
eralised geometry and exceptional field theory were used in order to revisit the consistent
truncation of D = 11 supergravity on the 7-sphere [69].

    The ExFT methods that were used in order to construct the consistent reduction
of D = 11 supergravity on S7 to give the N = 8 maximal gauged supergravity in
four dimensions were subsequently generalised in order to find the Kaluza-Klein spectra
for any vacuum that can be described as a deformation of the N = 8 vacuum that is
implemented by fields living in the N = 8 supermultiplet [70, 71]. This includes the
wide class of known extrema of the N = 8 supergravity potential. Not included in this
class, however, is the N = 1 squashed S7 vacuum, since in this case it corresponds to a
deformation of the round S7 vacuum by fields that lie outside those of N = 8 supergravity
(see, for example, [1]). Recently, even for this case the Kaluza-Klein spectrum was
constructed using ExFT techniques [45]. The results are compatible with those obtained

    8This feature of generalised geometry has been known to give conference speakers an uncomfortable
time in the question session. However, it is perhaps rather reminiscent of the situation in gauge theory,
where the gauge symmetry is introduced, but is then eventually lost again when restricting to the sector
of physical states.

                                                       18
recently in [41], where the full Kaluza-Klein spectra in the N = 1 and N = 0 squashed
S7 vacua were obtained by using coset-space harmonic analysis.

8 The complete form of the squashed S7 spectrum

In this section we first present some of the more recent developments concerning the
improved techniques used to solve eigenvalue equations on complicated coset spaces like
the squashed S7 [44, 41]. We then apply it to the squashed S7 and give a brief account of
the key results that have been obtained this way. The explicit construction of the 2-form
mode functions in [41] is a novel result in this context which used ideas that appeared
first in [42]. With these eigenmodes at hand their eigenvalues can be computed which
makes it possible to obtain a detailed understanding of the entire N = 1 supermultiplet
spectrum for the left squashed S7 compactification.These new developments that started
in 2018 with the derivation of the complete isometry irrep spectrum [39] fill in more or
less all gaps that were left when the subject came to a halt at the end of the 1980s.
At that point only the spectra of 0, iD/ 1/2 [42] and 1 [72] were understood in detail.
In addition the eigenvalues of the Lichnerowicz operator L were quoted in [1] without
proof. Some of the issues that still remain to be clarified are mentioned at the end of
this section.

8.1 Improved formalism on general reductive coset spaces G/H

The eigenvalue equations that we need to solve on any internal manifold K7 used in a
Freund-Rubin compactification of D = 11 supergravity in order to find the mass spectrum
in the AdS4 supergravity theory involve the following operators:

p = d + d (p = 0, 1, 2, 3), L, Q = d, iD/ 1/2, iD/ 3/2,              (26)

where 3 = Q2 and L is the Lichnerowicz operator which arises in the variation of the
Ricci tensor. By squaring also the two spinorial operators in this list we get a set of
operators that can be collectively be written in terms of the Riemann tensor as [73, 44]

           = - - Rabcdabcd,                                          (27)

where ab are the generators of the tangent space group SO(7). This form is a rather
trivial but extremely useful rewriting of the standard expressions for these operators.

    A convenient form of the Riemann tensor in this context is [74]

Rabcd  =  fabificd  +  1  fab  efecd  +  1  f[a|c|efb]e  d  .        (28)
                       2                 2

Here the structure constants are the ones for a reductive coset manifold G/H where the
generators TA of the isometry group G are split into Ti of the subgroup H and the rest
Ta. The non-zero commutators are thus

[Ti, Tj] = fijkTk, [Ti, Ta] = fiabTb, [Ta, Tb] = fabi Ti + fabc Tc.  (29)

                          19
    In the application of these equations to non-trivial coset spaces like the one of the
squashed S7, that is (Sp2 � SpC1 )/(Sp1A � SpB1 +C)9, there is an extremely useful relation
that expresses an H-covariant derivative algebraically [13, 1]:

                             D a    Da     +  1  fabcbc  =      -Ta                (30)
                                              2

where Da is the covariant derivative on the tangent space of G/H, with dimension n =
dim(G) - dim(H), and ab are the SO(n) generators. This implies that

                            D aD a = TaT a = -(CG - CH),                           (31)

where C is a Casimir operator. There are at least two aspects of this equation that
we need to address. First, it is not  that appears in the eigenvalue equations we are
interested in but rather . It is however a trivial exercise to derive a formula relating 

to the . It reads                                   1
                                                    4
                          =  +    fabcabD c      -     fabc  f  ade  bcde  .       (32)

The second aspect is that the spectrum is supposed to depend only on the Casimir

of the isometry group G and not of the isotropy group H. However, using the above

equations we find the following general form of the universal Laplacian [44, 41]

                   =  CG  +  fabcabD c  -  1  (3fabcf  a     -  2fabdf  acebcde).  (33)
                                           4            de

We see here that the Casimir for the isotropy group H has cancelled out which is a
necessary feature for this to work.

    Now the crucial issue is how one is supposed to use the equations above. There are

two possible ways to proceed:
a) One can start squaring fabcabD c in (33) in order to find non-linear equations for it
which hopefully can be solved. In this case one needs also the Ricci identity for D a which
in terms of the H generators T i reads

                          [D a, D b] = (T i)ab(Ti)cdcd + fabcD c.                  (34)

This approach will produce eigenvalues with no reference to the actual eigenmodes and
hence one will have a rather poor understanding of the structure of the spectrum.
b) A much more powerful way to use the above equations would be to first explicitly
construct all the eigenmodes and then hit them with fabcabD c. This will give rise to
matrix equations that are quite complicated but can be solved using some algebraic
computer program.
c) A final point concerns the probable proliferation of H irreps to study if the analysis
cannot take advantage of some more structure in the equations. The reason why some

9The factor Sp1B+C is the diagonal subgroup of SpC1 and Sp1B from the Sp2 subgroup SpA1 � Sp1B.

                                              20
additional structure may be expected is that it is known to occur in the case of the
squashed seven-sphere. In that case the extra structure is connected to the holonomy
group which is G2. In this particular case we have the sequence of groups [1]

     SO(7)  G2  H = Sp2 � SpC1 .                                             (35)

As we will see in the next subsection the use of the structure connected to the group
G2 when solving the eigenvalue equations will simplify the procedure enormously. This
will be particularly clear when the explicit 2-form mode functions are presented below.
The group G2 will also give us the opportunity to make use of octonions. It would be
interesting to see if the use of the holonomy group G2 and octonions has a counterpart
in other examples of Kaluza-Klein compactifications.

8.2 The full spectrum on the squashed seven-sphere

We now apply the above formalism to the case of the squashed seven-sphere10. The
extra information we then have is the explicit expressions for the structure constants. In
particular we find a direct connection to the octonions via

               fabc  =  -  1    aabc                                         (36)
                             5

where aabc are the octonionic structure constants [74]. This leads to the following property
of the H-covariant derivative Da [78]

               D a abcd = 0.                                                 (37)

    When looking for supersymmetry in the squashed S7 vacuum one solves the Killing
spinor equation which involves a covariant derivative with G2 holonomy. This derivative
is just Da when acting on the single solution to the Killing spinor equation . The
perhaps surprising relation above to the octonionic structure constants is in fact rather
natural in view of the following connection to the D = 7 gamma matrices

               aabc = i�abc.                                                 (38)

    By defining some relevant Casimir operators in terms of the structure constants fABC
and using the fact that the definition of  above involves two SO(7) generators one finds
a remarkably simple and general formula for  [41]:

  =  CG  +  6  CSO(7)  -  3  CG2  -   1    aabc bc  D a  .                   (39)
            5             2             5

Thus it has now become obvious that for the eigenvalue equations and the mode functions
the only relevant tensor properties are the ones of the tangent space group SO(7) and
the holonomy group G2, in addition to those of the isometry group G of course.

10The full spectrum of the round seven sphere may be found in [75, 76, 77].

                        21
    As an example we apply the above  to the 2-form mode functions Yab, see [44] for
the details. The 2-form eigenvalue equation in terms of  then becomes

                           2Yab      =  (CG  +  3P7     -   2    D [2])Yab  =  22Yab,                    (40)
                                                              5

where we have defined D[2]  a[acdD|dYc|b]. To arrive at the above form of the eigenvalue

equation we have used the fact that under SO(7)  G2 we have 21  14  7 and then

used CSO(7)(21) = 5, CG2(7) = 2 and CG2(14) = 4. This also explains the presence of
                                  1
the  G2  projector  (P7)abcd   =  6  aabe acde  in  the  equation  above.      As  explained  in  [44],  and  in

fact even earlier in [78], splitting the 2-form Yab and the eigenvalue equation into their
7 and 14 pieces a short calculating, based on squaring D[2], gives the result (using 2

instead of 22 and m2 = 9/20)

                               (21)     =  CG   +   18  =   m2   (20CG  +   72),                         (41)
                                                    5        9

         (22�)  =   CG  +  11  �  2        CG   +   49   =  m2   20CG + 44 � 4         20CG + 49 .       (42)
                           5        5               20       9

                                        2(3)    =   CG   =  m2   20CG,                                   (43)
                                                             9

     Although these results do not tell us which modes (i.e., isometry irreps) are associated

with which eigenvalues we can make the observation that the 5-fold degeneracy of some

(many in fact) irreps are not met by the same number of independent eigenvalues. In

fact, as we see above there are only four of these. Thus, some eigenmodes must have

the same eigenvalues. This will be demonstrated in detail when we now turn to the

eigenmode calculations.

    Previous attempts to construct all the 21 two-form mode functions met which con-
siderable complications which were overcome using the insights of the key role played

by G2 and octonions [41]. Another important feature that made this mode construction
feasible was that the appearance of a double derivative (see Ya(6b)i below) could easily be
verified using the improved formalism presented above. A more fundamental argument

for this double derivative mode will be presented in [79] which also contains a streamlined

explanation of the whole approach used here.

     Before we start discussing the structure of the mode functions we need to figure

out which isometry irreps they will carry. This question can be answered in two ways,

either by breaking the SO(8) irreps of all modes in the round sphere spectrum down to
Sp2�SpC1 irreps, or by constructing them directly in the squashed coset. Both approaches
were used in [39] and the result was presented in terms of so called cross diagrams for

the irreps (p, q; r). It turns out that there is a small set of irreps that appear only in one

of the two vacua seemingly making a one-to-one relation of the modes in the two vacua

impossible. That this discrepancy is really there in the spectra is strongly supported by
the construction of all N = 1 supermultiplets in the squashed vacuum [41].

                                                        22
The ingredients needed to obtain the explicit form of the mode functions are:

1. The octonionic structure constants aabc and their dual cabcd.
2. The derivative Da satisfying Daabcd = 0.

3. The Killing vector of the isometry group Sp1C: si = siaa satisfying [si, sj] = ijksk,

and [42]  D a sib = -3ijksaj skb .

                                                                               (44)

    It can be argued that the 21 independent mode functions of Yab must appear in irreps
of the isometry group factor Sp1C as the sum of one 1, five 3, and one 5. This leads to the
following mode operators, which by letting them act on scalar mode functions produces

a complete set of two-form mode functions:

           Ya(1b) = aabcD c, Ya(2b)i = aabcsci,                                (45)
           Ya(3b)i = ijksajsbk, Ya(4b)i = s[aiD b],                            (46)
           Ya(5b)i = cabcdsciD d, Ya(6b)i = a[a|cdsciD d|b],                   (47)
          Ya(7b)ij = s[a{i|ab]cdsc|j}D d                                       (48)

    One new feature of these mode operators is the double derivative in Ya(6b)i. In the
new improved formalism it is a fairly easy exercise to check that such an operator must
be introduced. It is also a straightforward but rather lengthy computation, best done
in Mathematica, to obtain both the transverse modes and their eigenvalues. A detailed
account of this can be found in [41].

    Once an exact relation between the 2 eigenvalues and the eigenmodes is established
one confirms that there is a degeneracy in this spectrum. This feature permeates then
into parts of spectrum of N = 1 Heidenreich supermultiplets [80] as can be seen in the
tables presented in [41]. Interestingly enough, this seems to afflict only supermultiplets
containing scalar fields which are tied to the Lichnerowicz operator.

    Another somewhat surprising property of the left squashed spectrum is that for one
of the fourteen towers of Wess-Zumino multiplets supersymmetry can be implemented in
two different ways [41]. This is made possible by choosing different boundary conditions
and hence different signs in the equations relating E0 to the mass of spin zero and 1/2
fields in AdS4.

    Furthermore, if one assumes that there is a one to one connection between the round
and squashed spectra it seems necessary to introduce singletons as part of the spectrum,
as suggested in [39, 40, 41]. Singletons were discovered by Dirac in 1963 [81] and have
been studied since the 1970s by Fronsdal and collaborators and many others. See, for
example [82, 83, 84, 85, 86]. They were discussed as a possible sector of the round S7
spectrum in [76, 87, 88].

    The squashed S7 vacuum supergroup OSp(4, 1) is not a subgroup of the round
OSp(4, 8) since the massless gravitino is not one of the original 8. It is not obvious

          23
that it should obey the same rules as conventional Higgs and Superhiggs in AdS4 11.
Their similarities and differences remain an interesting topic for future enquiry.

Acknowledgements

MJD is grateful to Massimo Porrati and Leron Borsten for useful conversations and STFC
Consolidated Grants ST/T000791/1 and ST/X000575 for support. The work of C.N.P.
is supported in part by DOE grant DE-SC0010813. B.E.W.N is grateful to Joel Karlsson
for a very stimulating and productive collaboration that generated some of the results
reviewed here. B.E.W.N. thanks Chalmers University of Technology, Go�teborg, for the
continued affiliation and partial funding of this work.

References

 [1] M.J. Duff, B.E.W. Nilsson and C.N. Pope, "Kaluza-Klein Supergravity", Phys. Rept.
      130, 1-142 (1986).

 [2] D. Z. Freedman, P. van Nieuwenhuizen and S. Ferrara, "Progress Toward a Theory
      of Supergravity," Phys. Rev. D 13, 3214-3218 (1976).

 [3] S. Deser and B. Zumino, "Consistent Supergravity," Phys. Lett. B 62, 335 (1976).
 [4] P. Fayet and S. Ferrara, "Supersymmetry," Phys. Rept. 32, 249-334 (1977).
 [5] P. van Nieuwenhuizen, "Supergravity", Phys. Rep. 68 (1981) 189.
 [6] Th. Kaluza, "On the problem of unity in Physics," Sitzungsber. Preuss. Akad. Wiss.

      Berlin. Math. Phys. K1(1921) 966.
 [7] O. Klein, "Quantum theory and 5-dimensional theory of relativity", Z. Phys. 37

      (1926) 895.
 [8] O. Klein, "The atomicity of electricity as a quantum theory law", Nature 118 (1926)

      516.
 [9] M.J. Duff and C.N. Pope, "Kaluza-Klein Supergravity and the Seven Sphere," Lec-

      tures delivered at the September School on Supergravity, ICTP Trieste, 1982. Pub-
      lished in Supergravity '82, eds S. Ferrara, J.G. Taylor and P. van Nieuwenhuizen, pp
      183 - 226.
[10] B. de Wit and H. Nicolai, "N = 8 Supergravity", Nucl. Phys. B 208, 323 (1982).
[11] H. Nicolai and K. Pilch, "Consistent Truncation of d = 11 Supergravity on AdS4 �
      S7", JHEP 03 (2012) 099, arXiv:1112.6131 hep-th.
[12] E. Witten, "Search for a realistic Kaluza-Klein theory", Nucl. Phys. B186 (1981)
      412-428.

  11See for example the decomposition rules for SO(2, 3) reps of Fronsdal [89] and Porrati [90].

                                                       24
[13] A. Salam and J. A. Strathdee, "On Kaluza-Klein Theory," Annals Phys. 141 (1982),
      316-352.

[14] M. A. Awada, M. J. Duff and C. N. Pope, "N = 8 Supergravity Breaks Down to N
      = 1," Phys. Rev. Lett. 50 (1983), 294.

[15] M. J. Duff, B. E. W. Nilsson and C. N. Pope, "Spontaneous Supersymmetry Breaking
      by the Squashed Seven Sphere," Phys. Rev. Lett. 50 (1983) no.26, 2043. Erratum:
      [Phys. Rev. Lett. 51 (1983) no.9, 846].

[16] M. J. Duff, B. E. W. Nilsson and C. N. Pope, "The Criterion for Vacuum Stability
      in Kaluza-Klein Supergravity," Phys. Lett. 139B (1984) 154.

[17] W. Nahm, "Supersymmetries and Their Representations," Nucl. Phys. B 135 (1978),
      149.

[18] E. Cremmer, B. Julia and J. Scherk, "Supergravity theory in eleven-dimensions",
      Phys. Lett. B76 (1978) 409.

[19] E. Cremmer and B. Julia, "The SO(8) supergravity", Nucl. Phys. B159 (1979) 141.

[20] P. G. O. Freund and M. A. Rubin, "Dynamics of dimensional reduction", Phys.
      Lett. B97 (1980) 233.

[21] F. Englert, "Spontaneous compactification of eleven dimensional supergravity",
      Phys. Lett. B119 (1982) 339.

[22] M. J. Duff, B. E. W. Nilsson and C. N. Pope, "Compactification of D = 11 super-
      gravity on K3 � T 3", Phys. Lett. B129 (1983) 39.

[23] M. A. Awada, M. J. Duff and C. N. Pope, "N = 8 supergravity breaks down to
      N = 1", Phys. Rev. Lett. 50 (1983) 294.

[24] B. S. Acharya, F. Denef, C. Hofman and N. Lambert, "Freund-Rubin revisited,"
      [arXiv:hep-th/0308046 [hep-th]].

[25] M. Atiyah and E. Witten, "M theory dynamics on a manifold of G(2) holonomy,"
      Adv. Theor. Math. Phys. 6 (2003), 1-106 [arXiv:hep-th/0107177 [hep-th]].

[26] D.N. Page and C.N. Pope, "New Squashed Solutions of D = 11 Supergravity", Phys.
      Lett. B 147, 55-60 (1984).

[27] L. Castellani, R. D. Auria, P. Fre and P. van Nieuwenhuizen, "Holonomy groups,
      sesquidual torsion fields and SU(8) in d = 11 supergravity", J. Math. Phys. 25 (1984)
      3209.

[28] M. J. Duff and J. T. Liu, "Hidden space-time symmetries and generalized holonomy
      in M theory," Nucl. Phys. B 674, 217-230 (2003), [arXiv:hep-th/0303140 [hep-th]].

[29] C. Hull, "Holonomy and symmetry in M-theory", hep-th/0305039.

[30] O. Aharony, O. Bergman, D.L. Jafferis and J. Maldacena, "N=6 superconformal
      Chern-Simons-matter theories, M2-branes and their gravity duals," JHEP 10, 091
      (2008), [arXiv:0806.1218 [hep-th]].

                                                       25
[31] S. W. Hawking and C. N. Pope, "Symmetry Breaking By Instantons In Supergravity,
      Nucl. Phys. B146, 381 (1978).

[32] L. Alvarez-Gaume and D. Z. Freedman, "Ricci Flat Kahler Manifolds And Super-
      symmetry, Phys. Lett. B94, 171 (1980).

[33] M. J. Duff and B. E. W. Nilsson, "Four-dimensional String Theory From the K3
      Lattice," Phys. Lett. B 175 (1986), 417-422.

[34] P. Candelas, G.T. Horowitz, A. Strominger and E. Witten, "Vacuum configurations
      for superstrings," Nucl. Phys. B 258, 46-74 (1985).

[35] D. Joyce, "Compact Riemannian 7-manifolds with holonomy G2. Part I", J. Diff.
      Geom. 43 (1996) 291.

[36] D. Joyce, "Compact Riemannian 7-manifolds with holonomy G2. Part II", J. Diff.
      Geom. 43 (1996) 329.

[37] M. J. Duff, "Supergravity, the Seven Sphere, and Spontaneous Symmetry Breaking,"
      Nucl. Phys. B 219, 389 (1983).

[38] D.N. Page, "Classical stability of round and squashed seven spheres in eleven imen-
      sional supergravity", Phys. Rev. D 28, 2976 (1983),

[39] B. E. W. Nilsson, A. Padellaro and C. N. Pope, "The role of singletons in S7 com-
      pactifications," JHEP 07 (2019), 124 [arXiv:1811.06228 [hep-th]].

[40] B. E. W. Nilsson and C. N. Pope, "De-Higgsing in eleven-dimensional supergravity
      on the squashed S 7," J. Phys. A 57 (2024) no.4, 045402 [arXiv:2302.03842 [hep-th]].

[41] J. Karlsson and B. E. W. Nilsson, "The complete Kaluza-Klein spectra of N = 1 and
      N = 0 M-theory on AdS4 � squashed S7)," JHEP 02 (2024), 144 [arXiv:2305.00916
      [hep-th]].

[42] B. E. W. Nilsson and C. N. Pope, "Scalar and Dirac Eigenfunctions on the Squashed
      Seven Sphere," Phys. Lett. 133B (1983) 67.

[43] H. Nicolai, "Representations of supersymmetry in anti-de Sitter space", CERN-TH-
      3882, April 1984.

[44] J. Karlsson, "Compactifications of String/M-Theory and the Swampland: A Study
      of the AdS4 Mass Spectrum of Eleven-Dimensional Supergravity on the Squashed
      Seven-Sphere," [arXiv:2110.09885 [hep-th]]. Chalmers Univ. of Tech., Go�teborg, MSc
      thesis (2020).

[45] B. Duboeuf, E. Malek and H. Samtleben, "Kaluza-Klein spectrometry beyond con-
      sistent truncations: the squashed S7," JHEP 04, 062 (2023), [arXiv:2212.01135 [hep-
      th]].

[46] P. Breitenlohner and D.Z. Freedman, "Stability in Gauged Extended Supergravity,"
      Annals Phys. 144 (1982), 249.

                                                       26
[47] D.N. Page and C.N. Pope, "Stability Analysis of Compactifications of D = 11
      Supergravity With SU(3) � SU(2) � U(1) Symmetry," Phys. Lett. B 145, 337-341
      (1984).

[48] D.N. Page and C.N. Pope, "Which Compactifications of D = 11 Supergravity Are
      Stable?", Phys. Lett. B 144, 346-350 (1984).

[49] C. Bohm, "Inhomogeneous Einstein metrics on low-dimensional spheres and other
      low-dimensional spaces", Invent. Math. 134, 145 (1998).

[50] G.W. Gibbons, S.A. Hartnoll and C.N. Pope, "Bohm and Einstein-Sasaki metrics,
      black holes and cosmological event horizons," Phys. Rev. D 67, 084024 (2003),
      [arXiv:hep-th/0208031 [hep-th]].

[51] H. Ooguri and C. Vafa, "Non-supersymmetric AdS and the Swampland," Adv.
      Theor. Math. Phys. 21, 1787-1801 (2017), [arXiv:1610.01533 [hep-th]].

[52] J. Maldacena, "The large N limit of superconformal field theories and supergravity,"
      Adv. Theor. Math. Phys. 2 (1998) 231, hep-th/9711200.

[53] S.S. Gubser, I.R. Klebanov and A.M. Polyakov, "Gauge theory correlators from
      non-critical string theory," Phys. Lett. B428 (1998) 105, hep-th/9802109.

[54] E. Witten, "Anti-de Sitter space and holography," Adv. Theor. Math. Phys. 2 (1998)
      253, hep-th/9802150.

[55] B.S. DeWitt in Relativity, Groups and Topology, Les Houches 1963 (Gordon and
      Breach, 1964).

[56] N. Straumann, "On Pauli's invention of non-Abelian Kaluza-Klein theory in 1953,"
      [arXiv:gr-qc/0012054 [gr-qc]].

[57] L. O'Raifeartaigh and N. Straumann, "Early history of gauge theories and Kaluza-
      Klein theories," [arXiv:hep-ph/9810524 [hep-ph]].

[58] M.J. Duff, B.E.W. Nilsson, C.N. Pope and N.P. Warner, "On the Consistency of the
      Kaluza-Klein Ansatz," Phys. Lett. B 149, 90-94 (1984).

[59] B. de Wit and H. Nicolai, "The Consistency of the S7 Truncation in D = 11 Super-
      gravity," Nucl. Phys. B 281, 211-240 (1987).

[60] H. Godazgar, M. Godazgar and H. Nicolai, "Nonlinear Kaluza-Klein theory for dual
      fields," Phys. Rev. D 88, no.12, 125002 (2013), [arXiv:1309.0266 [hep-th]].

[61] H. Nastase, D. Vaman and P. van Nieuwenhuizen, "Consistent nonlinear KK reduc-
      tion of 11-d supergravity on AdS7 � SW 4 and selfduality in odd dimensions," Phys.
      Lett. B 469, 96-102 (1999), [arXiv:hep-th/9905075 [hep-th]].

[62] H. Nastase, D. Vaman and P. van Nieuwenhuizen, "Consistency of the AdS7 � S4
      reduction and the origin of selfduality in odd dimensions," Nucl. Phys. B 581, 179-
      239 (2000), [arXiv:hep-th/9911238 [hep-th]].

                                                       27
[63] M. Cvetic, H. Lu�, C.N. Pope, A. Sadrzadeh and T.A. Tran, "Consistent SO(6)
      reduction of type IIB supergravity on S5," Nucl. Phys. B 586, 275-286 (2000),
      [arXiv:hep-th/0003103 [hep-th]].

[64] M. J. Duff and K. S. Stelle, "Multi-membrane solutions of D = 11 supergravity,"
      Phys. Lett. B 253, 113-118 (1991).

[65] B.E.W. Nilsson and C.N. Pope, "Hopf Fibration of Eleven-dimensional Supergrav-
      ity," Class. Quant. Grav. 1, 499 (1984).

[66] B. de Wit and H. Nicolai, "Hidden Symmetry in d = 11 Supergravity," Phys. Lett.
      B 155, 47-53 (1985),

[67] M.J. Duff and J.X. Lu, "Duality Rotations in Membrane Theory," Nucl. Phys. B
      347, 394-419 (1990),

[68] A. Baguet, O. Hohm and H. Samtleben, "Consistent Type IIB Reductions to Max-
      imal 5D Supergravity," Phys. Rev. D 92, no.6, 065004 (2015), [arXiv:1506.01385
      [hep-th]].

[69] O. Varela, "Complete D = 11 embedding of SO(8) supergravity," Phys. Rev. D 97,
      no.4, 045010 (2018), [arXiv:1512.04943 [hep-th]].

[70] E. Malek and H. Samtleben, "Kaluza-Klein Spectrometry for Supergravity," Phys.
      Rev. Lett. 124, no.10, 101601 (2020), [arXiv:1911.12640 [hep-th]].

[71] E. Malek and H. Samtleben, "Kaluza-Klein Spectrometry from Exceptional Field
      Theory," Phys. Rev. D 102, no.10, 106016 (2020), [arXiv:2009.03347 [hep-th]].

[72] K. Yamagishi, "Mass Spectra of Vector Particles in D = 11 Supergravity Compact-
      ified on Squashed Seven Sphere," Phys. Lett. B 137 (1984), 165-168.

[73] S. M. Christensen and M. J. Duff, "New Gravitational Index Theorems and Su-
      pertheorems," Nucl. Phys. B 154 (1979), 301-342.

[74] F. A. Bais, H. Nicolai and P. van Nieuwenhuizen, "Geometry of Coset Spaces and
      Massless Modes of the Squashed Seven Sphere in Supergravity," Nucl. Phys. B 228
      (1983), 333-350.

[75] F. Englert and H. Nicolai, "Supergravity in eleven-dimensional space-time", CERN-
      TH-3711.

[76] E. Sezgin, "The Spectrum of the Eleven-dimensional Supergravity Compactified on
      the Round Seven Sphere," Phys. Lett. B 138 (1984), 57-62.

[77] B. Biran, A. Casher, F. Englert, M. Rooman and P. Spindel, "The Fluctuating Seven
      Sphere in Eleven-dimensional Supergravity," Phys. Lett. B 134 (1984), 179.

[78] S. Ekhammar and B. E. W. Nilsson, "On the squashed seven-sphere operator spec-
      trum," JHEP 12 (2021), 057 [arXiv:2105.05229 [hep-th]].

[79] J. Karlsson and B. E. W. Nilsson, to appear.

                                                       28
[80] W. Heidenreich, "All linear unitary irreducible representations of de Sitter super-
      symmetry with positive energy", Phys. Lett. B 110 (1982), 461-464.

[81] P. A. M. Dirac, "A Remarkable representation of the 3 + 2 de Sitter group," J.
      Math. Phys. 4 (1963), 901-909.

[82] M. Flato, C. Fronsdal and D. Sternheimer, "Singleton physics,"
      [arXiv:hep-th/9901043 [hep-th]].

[83] A. Starinets, "Singleton field theory and Flato-Fronsdal dipole equation," Lett.
      Math. Phys. 50 (1999), 283-300 [arXiv:math-ph/9809014 [math-ph]].

[84] H. Nicolai and E. Sezgin, "Singleton Representations of Osp(N,4)," Phys. Lett. B
      143 (1984), 389-395.

[85] M. P. Blencowe and M. J. Duff, "Supersingletons," Phys. Lett. B 203, 229-236
      (1988).

[86] H. Samtleben and E. Sezgin, "Singletons in supersymmetric field theories and in
      supergravity," [arXiv:2409.03000 [hep-th]].

[87] A. Casher, F. Englert, H. Nicolai and M. Rooman, "The Mass Spectrum of Super-
      gravity on the Round Seven Sphere," Nucl. Phys. B 243 (1984), 173.

[88] E. Sezgin, "11D supergravity on AdS4 � S7 versus AdS7 � S4," J. Phys. A 53 (2020)
      no.36, 364003, [arXiv:2003.01135 [hep-th]].

[89] C. Fronsdal, "Singletons and Massless, Integral Spin Fields on de Sitter Space"
      Elementary Particles in a Curved Space. 7., Phys. Rev. D 20 (1979) 848-856.

[90] M. Porrati, "Higgs phenomenon for 4-D gravity in anti-de Sitter space," JHEP 04,
      058 (2002), [arXiv:hep-th/0112166 [hep-th]].

                                                       29
