# PDG Extra Dimensions 2024

**Source:** `08_PDG_Extra_Dimensions_2024.pdf`

---

1  85. Extra Dimensions

   85. Extra Dimensions

Revised August 2023 by Z. Demiragli (Boston U.) and A. Pomarol (U. Aut�noma de Barcelona;
IFAE).

85.1 Introduction

    Proposals for a spacetime with more than three spatial dimensions date back to the 1920s,
mainly through the work of Kaluza and Klein, in an attempt to unify the forces of nature [1].
Although their initial idea failed, the formalism that they and others developed is still useful
nowadays. Around 1980, string theory proposed again to enlarge the number of space dimensions,
this time as a requirement for describing a consistent theory of quantum gravity. The extra
dimensions were supposed to be compactified at a scale close to the Planck scale, and thus not
testable experimentally in the near future.

    A different approach was given by Arkani-Hamed, Dimopoulos, and Dvali (ADD) in their
seminal paper in 1998 [2], where they showed that the weakness of gravity could be explained by
postulating two or more flat extra dimensions in which only gravity could propagate. The size of
these extra dimensions should range between roughly a millimeter and 1/TeV, leading to possible
observable consequences in current and future experiments. A year later, Randall and Sundrum
(RS) [3] found a new possibility using a warped geometry, postulating a five-dimensional Anti-de
Sitter (AdS) spacetime with a compactification scale of order 1/TeV. The origin of the smallness
of the electroweak scale versus the Planck scale was explained by the gravitational redshift factor
present in the warped AdS metric. As in the ADD model, originally only gravity was assumed to
propagate in the extra dimensions, although it was soon clear that this was not necessary in warped
extra dimensions and also the SM gauge fields [4, 5] and SM fermions [6, 7] could propagate in the
five-dimensional spacetime.

    The physics of warped extra-dimensional models has an alternative interpretation by means
of the AdS/CFT correspondence [8�10]. Models with warped extra dimensions are related to
four-dimensional strongly-interacting theories, allowing an understanding of the properties of five-
dimensional fields as those of four-dimensional composite states [11]. This approach has opened
new directions for tackling outstanding questions in particle physics, such as the flavor problem,
grand unification, and the origin of electroweak symmetry breaking or supersymmetry breaking.

85.1.1 Experimental Constraints
    Constraints on extra-dimensional models arise from astrophysical and cosmological considera-

tions, tabletop experiments exploring gravity at sub-mm distances, and collider experiments. Col-
lider limits on extra-dimensional models are dominated by LHC results, which can be found on the
public WWW pages of ATLAS [12] and CMS [13]. This review includes the most recent limits, most
of which are published results based on 140 fb-1LHC data collected in 2015-18 at a center-of-mass
energy of 13 TeV and legacy results from 20 fb-1of 8 TeV data collected in Run 1. For most of the
models, Run 2 results surpass the sensitivity of Run 1.

85.1.2 Kaluza-Klein Theories
    Field theories with compact extra dimensions can be written as theories in ordinary four di-

mensions (4D) by performing a Kaluza-Klein (KK) reduction. As an illustration, consider a simple
example, namely a field theory of a complex scalar in flat five-dimensional (5D) spacetime. The
action will be given by 1

                                S5 = - d4x dy M5 |�|2 + |y|2 + 5||4 ,      (85.1)

   1Our convention for the metric is MN = Diag(-1, 1, 1, 1, 1).

   S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024)
                                    31st May, 2024 10:14am
2                       85. Extra Dimensions

where y refers to the extra (fifth) dimension. A universal scale M5 has been extracted in front of
the action in order to keep the 5D field with the same mass-dimension as in 4D. This theory is
perturbative for energies E < 5M5/5 where 5 = 243 [14].

    Let us now consider that the fifth dimension is compact with the topology of a circle S1 of

radius R, which corresponds to the identification of y with y + 2R. In such a case, the 5D complex

scalar field can be expanded in a Fourier series:

              (x, y) =  1                                                    (85.2)

                                                     einy/R(n)(x) ,
                          2RM5 n=-

that, inserted in Eq. (85.1) and integrating over y, gives

where                      S5 = S4(0) + S4(n) ,                              (85.3)
and,          S4(0) = - d4x |�(0)|2 + 4|(0)|4 ,                              (85.4)

           S4(n) = - d4x                        |�(n)|2 +    n  2

                                                             R   |(n)|2

                                          n=0

              + quartic interactions .                                       (85.5)

The n = 0 mode self-coupling is given by

                                          4  =     5      .                  (85.6)
                                                2RM5

The above action corresponds to a 4D theory with a massless scalar (0), referred to as the zero
mode, and an infinite tower of massive modes (n) with n > 0, known as KK modes. The KK
reduction thus allows a treatment of 5D theories as 4D field theories with an infinite number of
fields. At energies smaller than 1/R, the KK modes can be neglected, leaving the zero-mode action
of Eq. (85.4). The strength of the interaction of the zero-mode, given by Eq. (85.6), decreases as R
increases. Thus, for a large extra dimension R 1/M5, the massless scalar is very weakly coupled.

85.2 Large Extra Dimensions for Gravity

85.2.1 The ADD Scenario
    The ADD scenario [2, 15] (for a review see, for example, [16]) assumes a D = 4 +  dimensional

spacetime, with  compactified spatial dimensions. The apparent weakness of gravity arises since it
propagates in the higher-dimensional space. The SM is assumed to be localized in a 4D subspace,
a 3-brane, as can be found in certain string theory constructions [17, 18]. Gravity is described by
the Einstein-Hilbert action in D = 4 +  spacetime dimensions

       SD  =  - M� D2+  d4xd                         R    +  d4x-gind LSM ,  (85.7)
                   2                           y -g

where x labels the ordinary four coordinates, y the  extra coordinates, g refers to the determinant
of the D-dimensional metric whose Ricci scalar is defined by R, and M�D is called the reduced Planck
scale of the D-dimensional theory. In the second term of Eq. (85.7), which gives the gravitational

interactions of SM fields, the D-dimensional metric reduces to the induced metric on the 3-brane

                                          31st May, 2024
3                             85. Extra Dimensions

where the SM fields propagate. The extra dimensions are assumed to be flat and compactified in

a volume V. As an example, consider a toroidal compactification of equal radii R and volume
V = (2R). After a KK reduction, one finds that the fields that couple to the SM are the spin-2
gravitational field G�(x, y) and a tower of spin-0 KK graviscalars [19]. The graviscalars, however,
only couple to SM fields through the trace of the energy-momentum tensor, resulting in weaker

couplings to the SM fields. The Fourier expansion of the spin-2 field is given by

                 G� (x, y)    =  G�(0)(x)  +    1      ein�y/RG�(n)(x) ,               (85.8)

                                                   n=0
                                                V

where y = (y1, y2, ..., y) are the extra-dimensional coordinates and n = (n1, n2, ..., n). Eq. (85.8)
contains a massless state, the 4D graviton G(�0), and its KK tower G(�n) with masses m2n = |n|2/R2.
At energies below 1/R the action is that of the zero mode

          S4(0)  =  - M� D2+     d4x V -g(0) R(0) +  d4x -gi(n0d) LSM ,                (85.9)
                         2

                                                                                       2.4 � 1018 GeV, as a
where we can identify the 4D reduced Planck mass, MP  1/ 8GN

function of the D-dimensional parameters:

                              MP2 = V M� D2+  RMD2+ .                                  (85.10)

Fixing MD at around the electroweak scale MD  TeV to avoid introducing a new mass scale in
the model, Eq. (85.10) gives a prediction for R:

           = 1, 2, ..., 6  R  109 km , 0.5 mm , ... , 0.1 MeV-1 .                      (85.11)

The option  = 1 is clearly ruled out, as it leads to modifications of Newton's law at solar system
distances. However this is not the case for   2, and possible observable consequences can be
sought in present and future experiments.

    Consistency of the model requires a stabilization mechanism for the radii of the extra dimensions,
to the values shown in Eq. (85.11). The fact that we need R 1/MD leads to a new hierarchy
problem, the solution of which might require imposing supersymmetry in the extra-dimensional
bulk (for the case of two extra dimensions see for example [20]).

85.2.2 Tests of the Gravitational Force Law at Sub-mm Distances

   The KK modes of the graviton give rise to deviations from Newton's law of gravitation for

distances < R. Such deviations are usually parameterized by a modified Newtonian potential of

the form                                   m1m2
                                              r
                    V  (r)    =  -GN               1 +  e-r/  .                        (85.12)

For a 2-torus compactification,  = 16/3 and  = R. Searches for deviations from Newton's law
of gravitation have been performed in several experiments [21�24]. From Ref. [23] we have the
constraint R < 30�m at 95% CL for  = 2, corresponding to MD > 4.0 TeV. We see then that
bounds from Newton's law deviations are already pushing the scale MD beyond the TeV for two
extra dimensions.

85.2.3 Astrophysical and Cosmological Constraints
    The light KK gravitons could be copiously produced in stars, carrying away energy. Ensuring

that the graviton luminosity is low enough to preserve the agreement of stellar models with observa-
tions provides powerful bounds on the scale MD. The most stringent bound arises from supernova

                                 31st May, 2024
4  85. Extra Dimensions

SN1987A, giving MD > 27 (2.4) TeV for  = 2 (3) [25]. After a supernova explosion, most of
the KK gravitons stay gravitationally trapped in the remnant neutron star. The requirement that
neutron stars are not excessively heated by KK decays into photons leads to MD > 1700 (76) TeV
for  = 2 (3) [26].

    Cosmological constraints are also quite stringent [27]. To avoid overclosure of the Universe
by relic gravitons one needs MD > 7 TeV for  = 2. Relic KK gravitons decaying into photons
contribute to the cosmic diffuse gamma radiation, from which one can derive the bound MD > 100
TeV for  = 2.

    We must mention however that bounds coming from the decays of KK gravitons into photons
can be reduced if we assume that KK gravitons decay mainly into other non-SM states. This could
happen, for example, if there were other 3-branes with hidden sectors residing on them [15].

85.2.4 Collider Signals

85.2.4.1 Graviton and Other Particle Production

    Although each KK graviton has a purely gravitational coupling, suppressed by 1/MP , inclusive
processes in which one sums over the almost continuous spectrum of available gravitons have cross
sections suppressed only by powers of MD. Processes involving gravitons are therefore detectable
in collider experiments if MD  TeV. A number of experimental searches for evidence of large extra
dimensions have been performed at colliders, and interpreted in the context of the ADD model.

    One signature arises from direct graviton emission. By making a derivative expansion of Einstein
gravity, one can construct an effective theory, valid for energies much lower than MD, and use it
to make predictions for graviton-emission processes at colliders [19, 28, 29]. Gravitons produced in
the final state would escape detection, giving rise to missing transverse momentum (pmTiss). The
results quoted below are 95% CL lower limits on MD for a range of values of  between 2 and 6,
with more stringent limits corresponding to lower  values.

    At hadron colliders, experimentally sensitive channels include the jet (j) + pTmiss and  + pmTiss
final states. ATLAS (CMS) j + pmTiss results with 139 (137) fb-1 of 13 TeV data provide limits
of MD > 5.9 - 11.2 TeV [30] (MD > 5.5 - 10.7 TeV [31]). For these analyses, both experiments
are assuming leading order (LO) cross sections. Since the effective theory is only valid for energies
much less than MD, the results are quoted for the full space, and include theinformation that
suppressing the graviton cross section by a factor MD4 /s^2 for s^ > MD, where s^ is the parton-
level center-of-mass energy of the hard collision, weakens the limits on MD by a negligible amount
for  = 2 (3% for  = 6). Less stringent limits are obtained by CMS [32] from analysis of 36 fb-1of
13 TeV data in the  + pmTiss final state (MD > 2.85 - 2.90 TeV for  = 3 - 6). The analogous
ATLAS search [33] uses full Run 2 statistics but does not quote ADD interpretation of the results.

    In models in which the ADD scenario is embedded in a string theory at the TeV scale [18],
we expect the string scale Ms to be smaller than MD, and therefore expect production of string
resonances at the LHC [34]. A result from CMS analyzing the dijet invariant mass distribution for
137 fb-1of 13 TeV data excludes string resonances that decay predominantly to q + g with masses
below 7.9 TeV [35]. ATLAS dijet analysis [36] provides their results in the context of model-
independent limits on the cross section times acceptance for generic resonances of a variety of
possible widths, from which one can deduce similar lower mass limits  8 TeV for string resonances
decaying to q + g.

85.2.4.2 Virtual graviton effects

    One can also search for virtual graviton effects, the calculation of which however depends on the
ultraviolet cut-off of the theory and is therefore very model dependent. In the literature, several
different formulations exist [19,29,37] for the dimension-eight operator for gravity exchange at tree

                                                                           31st May, 2024
5                             85. Extra Dimensions

level:

                             4  T� T �       -          1  2 T��T  ,                        (85.13)
                 L8 = � MT4T                            +

where T� is the energy-momentum tensor and MT T is related to MD by some model-dependent
coefficient [38]. The relations with the parametrization of Refs. [37] and [19] are, respectively,
MT T = MS and MT T = (2/)1/4T . The experimental results below are given as 95% CL lower
limits on MT T , including in some cases the possibility of both constructive or destructive interfer-
ence, depending on the sign chosen in Eq. (9).

    The most stringent limits arise from LHC analyses of the dijet angular distribution. Using
35.9 fb-1of 13 TeV data, CMS [39] obtains results that correspond to an approximate limit of
MT T > 9 TeV.

    The next most restrictive results come from the analyses of diphoton (MT T > 6.1 TeV from
ATLAS [40] and MT T > 7.0 TeV from CMS [41]) and dilepton mass spectra (MT T > 6.5 TeV from
CMS [42]). The complete Run 2 (139 fb-1) analysis of ATLAS di-lepton data [43] does not quote

the limits on ADD.

    At the one-loop level, gravitons can also generate dimension-six operators with coefficients

that are also model dependent. Experimental bounds on these operators can also give stringent

constraints on MD [38].

85.2.4.3 Black Hole Production
    The physics at energies s  MD is sensitive to the details of the unknown quantum theory

of gravity. Nevertheless, in the transplanckian regime, s MD, one can rely on a semiclassical
description of gravity to obtain predictions. An interesting feature of transplanckian physics is the
creation of black holes [44, 45] (for a review see, for example, [46]). A black hole is expected to be
formed in a collision in which the impact parameter is smaller than the Schwarzschild radius [47]:

                           1  2 (-3)/2       +3            MBH     1/(+1)
                 RS = MD                       2
                                                           MD              ,                (85.14)
                                 +2

where MBH is the mass of the black hole, which would roughly correspond to the total energy

in the collision. The cross section for black hole production can be estimated to be of the same

order   as  the  geometric area   RS2 . For MD        TeV, this gives a  production of       107 black
holes   at  the    s = 14 TeV LHC with an integrated  luminosity of 30   fb-1 [44, 45].  A  black hole

would provide a striking experimental signature since it is expected to thermally radiate with a

Hawking temperature TH = ( + 1)/(4RS), and therefore would evaporate democratically into all
SM states. Nevertheless, given the present constraints on MD, the LHC will not be able to reach
energies much above MD. This implies that predictions based on the semiclassical approximation
could receive sizable modifications from model-dependent quantum-gravity effects.

   The most stringent limits on microscopic black holes arise from LHC searches which observed

no excesses above the SM background in high-multiplicity final states. The results are usually

quoted as model-independent limits on the cross section for new physics in the final state and

kinematic region analyzed. These results can then be used to provide constraints of models of

low-scale gravity and weakly-coupled string theory. In addition, limits are sometimes quoted on

particular implementations of models, which are used as benchmarks to illustrate the sensitivity.

   A CMS analysis [48] of multi-object final states using 36 fb-1of 13 TeV data, excludes semi-

classical black holes below masses of up to 10.1 TeV for MD = 2 TeV and  = 6. Analogous Run 2
ATLAS analysis [49], using 3.0 fb-1of 13 TeV data, excludes black hole masses up to 9.0 - 9.7 TeV,

depending on MD, for  = 6. Another ATLAS search [50] for an excess of events with multiple

                              31st May, 2024
6            85. Extra Dimensions

high transverse momentum objects, including charged leptons and jets, using 3.2 fb-1of 13 TeV
data, excludes semiclassical black holes below masses of  8.7 TeV for MD = 2 TeV and  = 6.

    A complementary approach is to look for jet extinction at high transverse momenta, as we
expect hard short distance scattering processes to be highly suppressed at energies above MD [51].
The CMS analysis [52] of inclusive jet pT spectrum in 10.7 fb-1of 8 TeV data set a lower limit of
3.3 TeV on the extinction mass scale.

    For black hole masses near MD, the semi-classical approximation is not valid, and one could
instead expect quantum black holes (QBH) that decay primarily into two-body final states [53].
In the context of both ADD model with  = 6 the QBHs have been searched in few final state
analysis (based on 2.3 fb-1 [54]), dijet [36, 39, 55], (same and different flavor) dilepton [56�60],
photon+jet [61, 62] and lepton+jet [63] channels by both ATLAS and CMS experiments. The Run
2 results at 13 TeV provide lower limits on QBH masses of up-to 9.4 TeV in an ADD model with
 = 6. The strongest constraints are from dijet searches.

    In weakly-coupled string models the semiclassical description of gravity fails in the energy
range between Ms and Ms/gs2 where stringy effects are important. In this regime one expects,
instead of black holes, the formation of string balls, made of highly excited long strings, that could
be copiously produced at the LHC for Ms  TeV [64], and would evaporate thermally at the
Hagedorn temperature giving rise to high-multiplicity events. The same analyses used to search
for black holes can be interpreted in the context of string balls. For example, for the case of  = 6
with Ms = MD/1.26 = 3 TeV, the ATLAS multiple high transverse momentum object analysis [49]
excludes string balls with masses below 6.5 to 9.0 TeV for values of 0.2 < gs < 0.8. The CMS
multi-object analysis [48] studies string ball production in two scenarios, both assuming  = 6.
For the constant gs = 0.2 and 1 < Ms < 3.5 TeV the string ball masses below 7.2 to 9.4 TeV are
excluded, while at constant Ms = 3.6 TeV and 0.2 < gs < 0.4 masses below 7.2 to 8.1 TeV are
excluded.

85.3 TeV-Scale Extra Dimensions

85.3.1 Warped Extra Dimensions
    The RS model [3] is the most attractive setup of warped extra dimensions at the TeV scale, since

it provides an alternative solution to the hierarchy problem. The RS model is based on a 5D theory
with the extra dimension compactified in an orbifold, S1/Z2, a circle S1 with the extra identification
of y with -y. This corresponds to the segment y  [0, R], a manifold with boundaries at y = 0
and y = R. Let us now assume that this 5D theory has a cosmological constant in the bulk ,
and on the two boundaries 0 and R. The action is given by

   S5 = -    d4x dy        1  M53  R  +       
                       -g  2               + -g0 (y)0


   + -gR (y - R)R ,                                    (85.15)

where g0 and gR are the values of the determinant of the induced metric on the two respective
boundaries. Einstein's equations can be solved, giving in this case the metric

   ds2 = a(y)2dx�dx � + dy2 , a(y) = e-ky ,            (85.16)

where k = -/6M53. Consistency of the solution requires 0 = -R = -/k. The metric
in Eq. (85.16) corresponds to a 5D AdS space. The factor a(y) is called the "warp" factor and
determines how 4D scales change as a function of the position in the extra dimension. In particular,
this implies that energy scales for 4D fields localized at the boundary at y = R are red-shifted by a

                     31st May, 2024
7                                  85. Extra Dimensions

factor e-kR with respect to those localized at y = 0. For this reason, the boundaries at y = 0 and
y = R are usually referred to as the ultraviolet (UV) and infrared (IR) boundaries, respectively.

    As in the ADD case, we can perform a KK reduction and obtain the low-energy effective theory
of the 4D massless graviton. In this case we obtain

   MP2 =   R                       dy  e-2ky M53  =  M53  1 - e-2kR  .  (85.17)
          0                                          2k

Taking M5  k  MP , we can generate an IR-boundary scale of order ke-kR  TeV for an extra
dimension of radius R 11/k. Mechanisms to stabilize R to this value have been proposed [65, 66]
that, contrary to the ADD case, do not require introducing any new small or large parameter.
Therefore a natural solution to the hierarchy problem can be achieved in this framework if the Higgs
field, whose vacuum expectation value (VEV) is responsible for electroweak symmetry breaking, is
localized at the IR-boundary where the effective mass scales are of order TeV. The radion field
is generically heavy in models with a stabilized R. Nevertheless, it has been recently discussed
that under some conditions a naturally light radion can arise [67�70]. In these cases the radion is
identified with the dilaton, the Nambu-Goldstone boson associated to the spontaneous breaking of
scale invariance, and its mass can be naturally below ke-kR  TeV.

    In the RS model [3], all the SM fields were assumed to be localized on the IR-boundary. Nev-
ertheless, for the hierarchy problem, only the Higgs field has to be localized there. SM gauge
bosons and fermions can propagate in the 5D bulk [4�7] (for a review see, for example, [71, 72]).
By performing a KK reduction from the 5D action of a gauge boson, we find [4, 5]

                                   1   R 1 R
                                   g42 = 0 dy g52 = g52 ,               (85.18)

where gD (D = 4, 5) is the gauge coupling in D-dimensions. Therefore the 4D gauge couplings can

be of order one, as is the case of the SM, if one demands g52  R. Using kR  10 and g4  0.5,

one obtains the 5D gauge coupling                 

                                       g5  4/ k .                       (85.19)

Boundary kinetic terms for the gauge bosons can modify this relation, allowing for larger values of
g5 k.

    Fermions propagating in a warped extra dimension have 4D massless zero-modes with wave-
functions which vary as f0  exp[(1/2 - cf )ky], where cf k is their 5D mass [7, 73]. Depending on
the free parameter cf k, fermions can be localized either towards the UV-boundary (cf > 1/2) or
IR-boundary (cf < 1/2). Since the Higgs boson is localized on the IR-boundary, one can generate
exponentially suppressed Yukawa couplings by having the fermion zero-modes localized towards
the UV-boundary, generating naturally the light SM fermion spectrum [7]. A large overlap with
the wavefunction of the Higgs is needed for the top quark, in order to generate its large mass,
thus requiring it to be localized towards the IR-boundary. In conclusion, the large mass hierarchies
present in the SM fermion spectrum can be easily obtained in warped models via suitable choices
of the order-one parameters cf [74]. In these scenarios, deviations in flavor physics from the SM
predictions are expected to arise from flavor-changing KK gluon couplings [75], putting certain
constraints on the parameters of the models and predicting new physics effects to be observed in
B-physics processes (see, for example, [76, 77]).

    The masses of the KK states can also be calculated. One finds [7]

          mn                                1          ke-kR ,          (85.20)
                                       n+ -
                                       24

                                       31st May, 2024
8  85. Extra Dimensions

where n = 1, 2, ... and  = {|cf - 1/2|, 0, 1} for KK fermions, KK gauge bosons and KK gravitons,
respectively. Their masses are of order ke-kR  TeV (for this reason we refer to these scenarios as
TeV-scale extra dimensions). The first KK state of the gauge bosons would be the lightest, while
gravitons are expected to be the heaviest.

85.3.1.1 Models of Electroweak Symmetry Breaking
    Theories in warped extra dimensions can be used to implement symmetry breaking at low

energies by boundary conditions (for a review see, for example, [78]). For example, for a U (1) gauge
symmetry in the 5D bulk, this can be easily achieved by imposing a Dirichlet boundary condition on
the IR-boundary for the gauge-boson field, A�|y=R = 0. This makes the zero-mode gauge boson
get a mass, given by mA = g4 2k/g52 e-kR. A very different situation occurs if the Dirichlet
boundary condition is imposed on the UV-boundary, A�|y=0 = 0. In this case the zero-mode gauge
boson disappears from the spectrum. Finally, if a Dirichlet boundary condition is imposed on the
two boundaries, one obtains a massless 4D scalar corresponding to the fifth component of the 5D
gauge boson, A5. Thus, different scenarios can be implemented by appropriately choosing the 5D
bulk gauge symmetry, G5, and the symmetries to which it reduces on the UV and IR-boundary,
HUV and HIR, respectively. In all cases the KK spectrum comes in representations of the group
G5.

    Among the most interesting scenarios are those called gauge-Higgs unified models, where the
Higgs boson appears as the fifth component of a 5D gauge boson, A5. The Higgs mass is protected
by the 5D gauge invariance and can only get a nonzero value from non-local one-loop effects [79].
To guarantee the relation MW2 MZ2 cos2 W , a custodial SU (2)V symmetry is needed in the bulk
and IR-boundary [80]. The simplest realization [81, 82] has

                                             G5 = SU (3)c � SO(5) � U (1)X ,

                                          HIR = SU (3)c � SO(4) � U (1)X ,

                                          HUV = GSM .

The Higgs boson gets a potential at the one-loop level that triggers a VEV, breaking the electroweak
symmetry. In these models there is a light Higgs boson whose mass can be around 125 GeV, as
required by the discovered Higgs boson [83]. This state, as will be explained in Sec. 85.3.2, behaves
as a composite pseudo-Nambu-Goldstone boson with couplings that deviate from the SM Higgs [84].
The present experimental determination of the Higgs couplings at the LHC, that agrees with the
SM predictions, put important constraints on these scenarios [83]. The lightest KK modes of the
model are color fermions with charges Q = -1/3, 2/3 and 5/3 [85].

85.3.1.2 Constraints from Electroweak Precision Tests
    Models in which the SM gauge bosons propagate in 1/TeV-sized extra dimensions give generi-

cally large corrections to electroweak observables. When the SM fermions are confined on a bound-
ary these corrections are universal and can be parameterized by four quantities: S, T , W and Y ,
as defined in Ref. [86]. For warped models, where the 5D gauge coupling of Eq. (85.19) is large,
the most relevant parameter is T , which gives the bound mKK > 10 TeV [71]. When a custodial
symmetry is imposed [80], the main constraint comes from the S parameter, requiring mKK > 3
TeV, independent of the value of g5. Corrections to the ZbL�bL coupling can also be important [71],
especially in warped models for electroweak symmetry breaking as the ones described above.

85.3.1.3 Kaluza-Klein Searches
    The main prediction of 1/TeV-sized extra dimensions is the presence of a discretized KK spec-

trum, with masses around the TeV scale, associated with the SM fields that propagate in the extra
dimension.

                                                                           31st May, 2024
9                   85. Extra Dimensions

   In the RS model [3], only gravity propagates in the 5D bulk. Experimental searches have been

performed for the lightest KK graviton through its decay to a variety of SM particle-antiparticle

pairs. The results are usually interpreted in the plane of the dimensionless coupling k/MP versus

m1, where MP is the reduced Planck mass defined previously and m1 is the mass of the lightest

KK   excitation of  the graviton. Since the AdS curvature  k cannot    exceed the  cut-off scale of
the  model, which   is estimated to be 15/3M5 [38], one must demand k       2 5MP      40MP . The

most stringent limits currently arise from LHC searches for resonances in the dilepton and diphoton

final states, using 13 TeV collisions. Searches with the  final state are an especially powerful

approach, given that these final states have a branching fraction twice that of any individual lepton

flavor. The CMS analysis [41] of 36 fb-1of 13 TeV data excludes KK gravitons below 2.3 to 4.6

TeV, depending on the value of the coupling k/MP , which is varied between 0.01 and 0.2, while
ATLAS [87] uses the full 139 fb-1and provides a lower limit on the KK graviton mass of 4.5 TeV

for the coupling parameter 0.1. The CMS [42] dilepton analyses, combining results from the ee and

�� channels, exclude KK gravitons with masses 2.47�4.78 TeV for k/MP values of 0.01�0.1. The
ATLAS [88] analysis of 139 fb-1of Run 2 data does not include a RS KK graviton interpretation

of the results. Less stringent limits on the KK graviton mass can be derived from analyses of the

dijet [35, 36, 89, 90], HH [91�99], and V V [100�104] final states, where V can represent either a W

or Z boson.

    In addition, both ATLAS and CMS experiments directly search for heavy radions, with masses
above 1 TeV where the dominant decay mode is to pairs of bosons. The main production mechanism
is gluon fusion. ATLAS [102] (CMS [105]) excludes radion masses below 3.2 TeV (3.1 TeV) for a
radion decaying into W W, ZZ. Radions are also searched in final states with pairs of Higgs bosons
HH [91, 94, 96, 97, 99, 106], and dijet final states [107] with additional gluons. Bounds for a light
radion (1 keV�10 GeV mass range) can be found in [108].

    In warped extra-dimensional models in which the SM fields propagate in the 5D bulk, the
couplings of the KK graviton to ee/��/ are suppressed [109], and the above bounds do not
apply. Furthermore, the KK graviton is the heaviest KK state (see Eq. (85.20)), and therefore
experimental searches for KK gauge bosons and fermions are more appropriate discovery channels
in these scenarios. For the scenarios discussed above in which only the Higgs boson and the top
quark are localized close to the IR-boundary, the KK gauge bosons mainly decay into top quarks,
longitudinal W/Z bosons, and Higgs bosons. Couplings to light SM fermions are suppressed by a

factor g/ g52k  0.2 [7] for the value of Eq. (85.19) that is considered from now on. Searches have
been made for evidence of the lightest KK excitation of the gluon, through its decay to tt pairs. The
searches take into account the natural KK gluon width, which is typically  15% of its mass. The
decay of a heavy particle to tt would tend to produce highly boosted top (anti-)quarks in the final
state. Products of the subsequent top decays would therefore tend to be close to each other in the
detector. In the case of t  W b  jjb decays, the three jets could overlap with one another and not
be individually reconstructed with the standard jet algorithms, while t  W b  b decays could
result in the lepton failing standard isolation requirements due to its proximity to the b-jet; in both
cases, the efficiency for properly reconstructing the final state would fall as the mass of the original
particle increases. To avoid the loss in sensitivity which would result, a number of techniques,
known generally as top quark tagging [110, 111], have been developed to reconstruct and identify
highly boosted top quarks, for example by using a single wide jet to contain all the decay products
of a hadronic top decay. The large backgrounds from QCD jets can then be reduced by requiring
the jet mass be consistent with that of a top quark, and also by examining the substructure of the
wide jet for indication that it resulted from the hadronic decay of a top quark. These techniques
are key to extending to very high masses the range of accessible resonances decaying to tt pairs.

                    31st May, 2024
10  85. Extra Dimensions

While the ATLAS search in 139 fb-1of Run 2 data [112] does not provide a KK interpretation,
dedicated analysis from CMS [113] of 36 fb-1 of 13 TeV data combines di-lepton, lepton-plus-jet,
and all-hadronic tt decays and excludes KK gluons with masses below 4.55 TeV. ATLAS uses
all-hadronic [114] and lepton-plus-jet [115] final states to exclude KK gluons up to 3.4 and 3.8 TeV
respectively with 36fb-1of 13 TeV data. The results are not directly comparable between the two
LHC experiments, since they employ in their respective analyses different implementations of the
theoretical model. For masses between 3 and 5 TeV, the cross-section limits are around 20 fb for
CMS analysis of 36 fb-1and 30 fb (4 fb) for ATLAS analyses of 36 (139) fb-1.

    A gauge boson KK excitation could be also sought through its decay to longitudinal W/Z
bosons. Recent analyses from ATLAS [116] (and CMS [117]) with 139 (137) fb-1of 13 TeV data
searching for heavy vector resonances decaying to a W or Z boson and a Higgs in the qq�b�b final
state have set a lower limit on the mass of these KK of 3.2(3.7) TeV (warped models are equivalent
to the Model B considered in the analyses with gV  g5 k). The decay to a pair of intermediate
vector bosons has also been exploited to search for KK gravitons in models in which the SM fields
propagate in the 5D bulk. The analyses typically reconstruct hadronic W/Z decays using variants
of the boosted techniques mentioned previously. An ATLAS analysis [118] combines leptonic and
hadronic final states from the KK graviton decay G  V V , where V can represent either a W or
Z boson, exclude KK gravitons with masses below 2.3 TeV, for a value of k/MP = 1. CMS V V
analyses [105, 119, 120] using 137 fb-1of 13 TeV data also exclude KK gravitons with masses below
1.8 TeV in the context of bulk gravitons for a maximum value of k/MP = 0.5.

    The lightest KK states are, in certain models, the partners of the top quark. For example, in
5D composite Higgs models these are colored states with charges Q = -1/3, 2/3 and 5/3 (arising
from SU (2)L doublets with Y = 7/6, 1/6), and masses expected to be below the TeV [85]. They can
be either singly or pair-produced, and mainly decay into a combination of W/Z with top/bottom
quarks [121�124]. An exhaustive review of these searches can be found in Ref. [125]. Of particular
note, the Q = 5/3 state decays mainly into W +t  W +W +b, giving a very clean signature of a
pair of same-sign leptons in the final state. An analysis by ATLAS [126] searching in the lepton-
plus-jets final state for evidence of pair production of the Q = 5/3 state provides a lower mass limit
of 1.25 TeV. A CMS analysis [127] searching for pair production of the Q = 5/3 state using both
lepton-plus-jets and same sign lepton final states excludes masses below 1.3 TeV. Similarly, searches
for single production of the Q = 5/3 state [128], also excludes masses up to 0.9 to 1.5 TeV depending
on the model parameters. Both LHC experiments have searched for pair production of vector-like
quarks T and B of charges Q = 2/3 and -1/3 respectively, assuming the allowable decays are
T  W b/Zt/Ht and B  W t/Zb/Hb. In each case, it is assumed the branching fractions of the
three decay modes sum to unity, but the individual branching fractions, which are model-dependent,
are allowed to vary within this constraint. Both ATLAS [129�131] and CMS [132,133] obtain lower
limits on the mass of the T and B vector-like quarks up to 1.5 TeV and 1.6 TeV respectively.

    Analyses from ATLAS [134�138] and CMS [128, 139�142] also search for a single top partner
and single bottom partner production, the cross section for which is model-dependent [143] but
does not carry the kinematic penalty for producing two heavy objects.

85.3.2 Connection with Strongly Coupled Models via the AdS/CFT Correspondence

    The AdS/CFT correspondence [8] provides a connection between warped extra-dimensional
models and strongly-coupled theories in ordinary 4D. Although the exact connection is only known
for certain cases, the AdS/CFT techniques have been very useful to obtain, at the qualitative level,
a 4D holographic description of the various phenomena in warped extra-dimensional models [11,72].

    The connection goes as follows. The physics of the bulk AdS5 models can be interpreted as that
of a 4D conformal field theory (CFT) which is strongly coupled. The extra-dimensional coordinate

                                                                           31st May, 2024
11  85. Extra Dimensions

y plays the role of the renormalization scale � of the CFT by means of the identification �  ke-ky.
Therefore the UV-boundary corresponds in the CFT to a UV cut-off scale at UV = k  MP ,
breaking explicitly conformal invariance, while the IR-boundary can be interpreted as a spontaneous
breaking of the conformal symmetry at energies ke-kR  TeV. Fields localized on the UV-boundary
are elementary fields external to the CFT, while fields localized on the IR-boundary and KK states
corresponds to composite resonances of the CFT. Furthermore, local gauge symmetries in the 5D
models, G5, correspond to global symmetries of the CFT, while the UV-boundary symmetry can be
interpreted as a gauging of the subgroup HUV of G5 in the CFT. Breaking gauge symmetries by IR-
boundary conditions corresponds to the spontaneous breaking G5  HIR in the CFT at energies
 ke-kR. Using this correspondence one can easily derive the 4D massless spectrum of the
compactified AdS5 models. One also has the identification k3/M53  162/N 2 and g52k  162/N r
(r = 1 or 2 for CFT fields in the fundamental or adjoint representation of the gauge group), where
N plays the role of the number of colors of the CFT. Therefore the weak-coupling limit in AdS5
corresponds to a large-N expansion in the CFT.

    Following the above AdS/CFT dictionary one can understand the RS solution to the hierarchy
problem from a 4D viewpoint. The equivalent 4D model is a CFT with a TeV mass gap and a
Higgs boson emerging as a composite state. In the particular case where the Higgs is the fifth-
component of the gauge-boson, A5 [144], this corresponds to models, similar to those proposed in
Ref. [145�148], where the Higgs is a composite pseudo-Nambu-Goldstone boson arising from the
spontaneous breaking G5  HIR in the CFT. The AdS/CFT dictionary tells us that KK states
must behave as composite resonances. For example, if the SM gauge bosons propagate in the 5D
bulk, the lowest KK SU (2)L-gauge boson must have properties similar to those of the Techni-rho
T [125] with a coupling to longitudinal W/Z bosons given by g5 k  gT , while the coupling to
elementary fermions is g2/ g52k  g2FT /MT .

    Fermions in compactified AdS5 also have a simple 4D holographic interpretation. The 4D
massless mode described in Sec. 85.3.1 corresponds to an external fermion i linearly coupled to a
fermionic CFT operator Oi: Lint = i�iOi + h.c.. The dimension of the operator Oi is related to
the 5D fermion mass according to Dim[Oi] = |cf + 1/2| - 1. Therefore, by varying cf one varies
Dim[Oi], making the coupling i irrelevant (cf > 1/2), marginal (cf = 1/2) or relevant (cf < 1/2).
When irrelevant, the coupling is exponentially suppressed at low energies, and then the coupling of
i to the CFT (and eventually to the composite Higgs) is very small. When relevant, the coupling
grows in the IR and become as large as g5 (in units of k), meaning that the fermion is as strongly
coupled as the CFT states [81]. In this latter case i behaves as a composite fermion.

85.3.3 Linear dilaton geometry

    The warp factor a(y) in Eq. (85.16) can be different from the exponential considered above,
giving rise to a different KK mass spectrum. A particularly interesting case is the linear dilaton
geometry [149] where the KK states become very narrowly-spaced. These scenarios can also be
understood in 4D via the clockwork mechanism [150], and for this reason are usually referred to
as Clockwork/Linear Dilaton (CW/LD) models. The collider phenomenology becomes different in
these models since the decay of the narrowly-spaced KK spectrum appears as a periodic signal in
the invariant mass of the decaying products. An excellent detector resolution is needed in order
to resolve these KK modes which can be done by looking at 2 electrons or 2 photons in the final
state. A search for this type of KK gravitons decaying into ee [151] and  [151, 152] put bounds
for M5 in the range of 10 TeV to 1 TeV for values of the lightest KK graviton mass (referred as k
in [151, 152]) in the range of few TeVs.

                                                                           31st May, 2024
12  85. Extra Dimensions

85.3.4 Flat Extra Dimensions
    Models with quantum gravity at the TeV scale, as in the ADD scenario, can have extra (flat)

dimensions of 1/TeV size, as happens in string scenarios (see, for example, [153]). All SM fields may
propagate in these extra dimensions, leading to the possibility of observing their corresponding KK
states.

    A simple example is to assume that the SM gauge bosons propagate in a flat five-dimensional
orbifold S1/Z2 of radius R, with the fermions localized on a 4D boundary. The KK gauge bosons
behave as sequential SM gauge bosons with a coupling to fermions enhanced by a factor 2 [153].
The experimental limits on such sequential gauge bosons could therefore be recast as limits on KK
gauge bosons. Such an interpretation of the ATLAS 7 TeV dilepton analysis [154] yielded the bound
1/R > 4.16 TeV, while a CMS 8 TeV search with a lepton and missing transverse energy in the final
state [155] give 1/R > 3.4 TeV. Indirect bounds from LEP2 require however 1/R > 6 TeV [86, 156],
a bound that can considerably improve in the future by high-energy measurements of the dilepton
invariant mass spectrum from Drell-Yan processes at the LHC [157]. More recent LHC limits
on leptonically decaying gauge bosons [88, 158�162] are not interpreted as bounds on 1/R by the
collaborations, but the published results allow for independent derivation of such bounds.

    An alternative scenario, known as Universal Extra Dimensions (UED) [163] (for a review see,
for example, [164]), assumes that all SM fields propagate universally in a flat orbifold S1/Z2 with
an extra Z2 parity, called KK-parity, that interchanges the two boundaries. In this case, the lowest
KK state is stable and is a Dark Matter candidate. At colliders, the KK particles would have to be
created in pairs, and would then cascade decay to the lightest KK particle, which would be stable
and escape detection. The UED mass-spectrum depends not only on the extra-dimensional radius
R, but also on the cut-off of the 5D theory , since quantum corrections sensitive to R induce
mass-splittings between the KK states. Experimental signatures, such as jets or leptons and pTmiss,
would be similar to those of typical R-parity conserving SUSY searches. An interpretation of the
recent LHC experimental SUSY searches for UED models has been presented in Refs. [165, 166]. A
lower bound 1/R > 1.4 - 1.5 TeV was derived for R in the range 5 - 35 [165]. A recent analysis
is given in Ref. [167] where it is shown that the minimal UED model is ruled out when LHC data
is combined with Dark Matter relic density data. Extensions to the minimal UED model where
boundary terms are included can however be compatible with experiments [167].

    Finally, realistic models of electroweak symmetry breaking can also be constructed with flat
extra spatial dimensions, similarly to those in the warped case, requiring, however, the presence
of sizeable boundary kinetic terms [168]. There is also the possibility of breaking supersymmetry
by boundary conditions [169]. Models of this type could explain naturally the presence of a Higgs
boson lighter than MD  TeV (see, for example, [170�172]).

References
   [1] For a comprehensive collection of the original papers see, "Modern Kaluza-Klein Theories",
       edited by T. Appelquist et al., Addison-Wesley (1987).

   [2] N. Arkani-Hamed, S. Dimopoulos and G. Dvali, Phys. Lett. B429, 263 (1998), [hep-
       ph/9803315].

   [3] L. Randall and R. Sundrum, Phys. Rev. Lett. 83, 3370 (1999), [hep-ph/9905221].

   [4] H. Davoudiasl, J. L. Hewett and T. G. Rizzo, Phys. Lett. B473, 43 (2000), [hep-ph/9911262].

   [5] A. Pomarol, Phys. Lett. B486, 153 (2000), [hep-ph/9911294].

   [6] S. Chang et al., Phys. Rev. D62, 084025 (2000), [hep-ph/9912498].

   [7] T. Gherghetta and A. Pomarol, Nucl. Phys. B586, 141 (2000), [hep-ph/0003129].

                                                                           31st May, 2024
13  85. Extra Dimensions

 [8] J. M. Maldacena, Int. J. Theor. Phys. 38, 1113 (1999), [Adv. Theor. Math. Phys.2,231(1998)],
      [hep-th/9711200].

 [9] E. Witten, Adv. Theor. Math. Phys. 2, 253 (1998), [hep-th/9802150].
[10] S. S. Gubser, I. R. Klebanov and A. M. Polyakov, Phys. Lett. B428, 105 (1998), [hep-

      th/9802109].
[11] N. Arkani-Hamed, M. Porrati and L. Randall, JHEP 08, 017 (2001), [hep-th/0012148].
[12] ATLAS public results are available on WWW at

      https://twiki.cern.ch/twiki/bin/view/AtlasPublic.
[13] CMS public results are available on WWW at

      https://cms-results.web.cern.ch/cms-results/public-results/publications.
[14] Z. Chacko, M. A. Luty and E. Ponton, JHEP 07, 036 (2000), [hep-ph/9909248].
[15] N. Arkani-Hamed, S. Dimopoulos and G. R. Dvali, Phys. Rev. D59, 086004 (1999), [hep-

      ph/9807344].
[16] R. Rattazzi, hep-ph/0607055 (2006); I. Antoniadis, Yellow report CERN-2002-002 (2002).
[17] J. D. Lykken, Phys. Rev. D54, R3693 (1996), [hep-th/9603133].
[18] I. Antoniadis et al., Phys. Lett. B436, 257 (1998), [hep-ph/9804398].
[19] G. F. Giudice, R. Rattazzi and J. D. Wells, Nucl. Phys. B544, 3 (1999), [hep-ph/9811291].
[20] N. Arkani-Hamed et al., Phys. Rev. D62, 105002 (2000), [hep-ph/9912453].
[21] E. G. Adelberger et al., Prog. Part. Nucl. Phys. 62, 102 (2009).
[22] J. Murata and S. Tanaka, Class. Quant. Grav. 32, 3, 033001 (2015), [arXiv:1408.3588].
[23] W.-H. Tan et al., Phys. Rev. Lett. 116, 13, 131101 (2016).
[24] J. G. Lee et al., Phys. Rev. Lett. 124, 101101 (2020), [arXiv:2002.11761].
[25] C. Hanhart et al., Phys. Lett. B509, 1 (2001), [arXiv:astro-ph/0102063].
[26] S. Hannestad and G. G. Raffelt, Phys. Rev. D67, 125008 (2003), [Erratum: Phys.

      Rev.D69,029901(2004)], [hep-ph/0304029].
[27] L. J. Hall and D. Tucker-Smith, Phys. Rev. D60, 085008 (1999), [hep-ph/9904267].
[28] E. A. Mirabelli, M. Perelstein and M. E. Peskin, Phys. Rev. Lett. 82, 2236 (1999), [hep-

      ph/9811337].
[29] T. Han, J. D. Lykken and R.-J. Zhang, Phys. Rev. D59, 105006 (1999), [hep-ph/9811350].
[30] G. AaD et al. (ATLAS), Phys. Rev. D 103, 112006 (2021), [arXiv:2102.10874].
[31] A. Tumasyan et al. (CMS), JHEP 11, 153 (2021), [arXiv:2107.13021].
[32] A. M. Sirunyan et al. (CMS), JHEP 02, 074 (2019), [arXiv:1810.00196].
[33] G. Aad et al. (ATLAS), JHEP 02, 226 (2021), [arXiv:2011.05259].
[34] S. Cullen, M. Perelstein and M. E. Peskin, Phys. Rev. D62, 055012 (2000), [hep-ph/0001166].
[35] A. M. Sirunyan et al. (CMS), JHEP 05, 033 (2020), [arXiv:1911.03947].
[36] G. Aad et al. (ATLAS), JHEP 03, 145 (2020), [arXiv:1910.08447].
[37] J. L. Hewett, Phys. Rev. Lett. 82, 4765 (1999), [hep-ph/9811356].
[38] G. F. Giudice and A. Strumia, Nucl. Phys. B663, 377 (2003), [hep-ph/0301232].
[39] A. M. Sirunyan et al. (CMS), Eur. Phys. J. C78, 9, 789 (2018), [arXiv:1803.08030].
[40] M. Aaboud et al. (ATLAS), Phys. Lett. B775, 105 (2017), [arXiv:1707.04147].

                                                                         31st May, 2024
14  85. Extra Dimensions

[41] A. M. Sirunyan et al. (CMS), Phys. Rev. D98, 9, 092001 (2018), [arXiv:1809.00327].
[42] A. M. Sirunyan et al., JHEP 07, 7 (2021), [arXiv:2103.02708].
[43] G. Aad et al., JHEP 11, 005 (2020), [arXiv:2006.12946].
[44] S. B. Giddings and S. D. Thomas, Phys. Rev. D65, 056010 (2002), [hep-ph/0106219].
[45] S. Dimopoulos and G. L. Landsberg, Phys. Rev. Lett. 87, 161602 (2001), [hep-ph/0106295].
[46] P. Kanti, Int. J. Mod. Phys. A19, 4899 (2004), [hep-ph/0402168].
[47] R. C. Myers and M. J. Perry, Annals Phys. 172, 304 (1986).
[48] A. M. Sirunyan et al. (CMS), JHEP 11, 042 (2018), [arXiv:1805.06013].
[49] G. Aad et al. (ATLAS), JHEP 03, 026 (2016), [arXiv:1512.02586].
[50] M. Aaboud et al. (ATLAS), Phys. Lett. B760, 520 (2016), [arXiv:1606.02265].
[51] C. Kilic et al., Phys. Rev. D89, 1, 016003 (2014), [arXiv:1207.3525].
[52] V. Khachatryan et al. (CMS), Phys. Rev. D90, 3, 032005 (2014), [arXiv:1405.7653].
[53] P. Meade and L. Randall, JHEP 05, 003 (2008), [arXiv:0708.3017].
[54] A. M. Sirunyan et al. (CMS), Phys. Lett. B774, 279 (2017), [arXiv:1705.01403].
[55] G. Aad et al. (ATLAS), Phys. Lett. B 754, 302 (2016), [arXiv:1512.01530].
[56] G. Aad et al. (ATLAS) (2023), [arXiv:2307.08567].
[57] M. Aaboud et al. (ATLAS), Eur. Phys. J. C 76, 10, 541 (2016), [arXiv:1607.08079].
[58] M. Aaboud et al. (ATLAS), Phys. Rev. D98, 9, 092008 (2018), [arXiv:1807.06573].
[59] A. Tumasyan et al. (CMS), JHEP 05, 227 (2023), [arXiv:2205.06709].
[60] A. M. Sirunyan et al. (CMS), JHEP 04, 073 (2018), [arXiv:1802.01122].
[61] A. Tumasyan et al. (CMS) (2023), [arXiv:2305.07998].
[62] M. Aaboud et al. (ATLAS), Eur. Phys. J. C 78, 2, 102 (2018), [arXiv:1709.10440].
[63] G. Aad et al. (ATLAS) (2023), [arXiv:2307.14967].
[64] S. Dimopoulos and R. Emparan, Phys. Lett. B526, 393 (2002), [hep-ph/0108060].
[65] W. D. Goldberger and M. B. Wise, Phys. Rev. Lett. 83, 4922 (1999), [hep-ph/9907447].
[66] J. Garriga and A. Pomarol, Phys. Lett. B560, 91 (2003), [hep-th/0212227].
[67] See talk by R. Rattazzi at Planck 2010, CERN,

      http://indico.cern.ch/getFile.py/access?contribId=163&resId=0&materialId=slides&confId=75810.
[68] B. Bellazzini et al., Eur. Phys. J. C74, 2790 (2014), [arXiv:1305.3919].
[69] F. Coradeschi et al., JHEP 11, 057 (2013), [arXiv:1306.4601].
[70] E. Megias and O. Pujolas, JHEP 08, 081 (2014), [arXiv:1401.4998].
[71] E. P. H. Davoudiasl, S. Gopalakrishna and J. Santiago, New J. Phys. 12, 075011 (2010),

      [arXiv:0908.1968].
[72] T. Gherghetta, in "Physics of the large and the small, TASI 09, proceedings of the Theoretical

      Advanced Study Institute in Elementary Particle Physics, Boulder, Colorado, USA, 1-26 June
      2009," 165�232 (2011), [arXiv:1008.2570].
[73] Y. Grossman and M. Neubert, Phys. Lett. B474, 361 (2000), [hep-ph/9912408].
[74] S. J. Huber and Q. Shafi, Phys. Lett. B498, 256 (2001), [hep-ph/0010195].
[75] A. Delgado, A. Pomarol and M. Quiros, JHEP 01, 030 (2000), [hep-ph/9911252].
[76] K. Agashe, G. Perez and A. Soni, Phys. Rev. D71, 016002 (2005), [hep-ph/0408134].

                                                                         31st May, 2024
15  85. Extra Dimensions

 [77] M. Bauer et al., JHEP 09, 017 (2010), [arXiv:0912.1625].
 [78] A. Pomarol, Int. J. Mod. Phys. A24, 61 (2009), [ In Kane, Gordon (ed.) et al.: Perspectives

       on LHC physics ,259(2008)].
 [79] Y. Hosotani, Phys. Lett. 126B, 309 (1983).
 [80] K. Agashe et al., JHEP 08, 050 (2003), [hep-ph/0308036].
 [81] K. Agashe, R. Contino and A. Pomarol, Nucl. Phys. B719, 165 (2005), [hep-ph/0412089].
 [82] For a review see, for example, R. Contino, arXiv:1005.4269.
 [83] See, for example, PDG review of Higgs boson in this Review.
 [84] G. F. Giudice et al., JHEP 06, 045 (2007), [hep-ph/0703164].
 [85] R. Contino, L. Da Rold and A. Pomarol, Phys. Rev. D75, 055014 (2007), [hep-ph/0612048].
 [86] R. Barbieri et al., Nucl. Phys. B703, 127 (2004), [hep-ph/0405040].
 [87] G. Aad et al. (ATLAS) (2021), [arXiv:2102.13405].
 [88] G. Aad et al. (ATLAS), Phys. Lett. B796, 68 (2019), [arXiv:1903.06248].
 [89] A. M. Sirunyan et al. (CMS), JHEP 08, 130 (2018), [arXiv:1806.00843].
 [90] G. Aad et al. (ATLAS), Phys. Rev. Lett. 125, 13, 131801 (2020), [arXiv:2005.02983].
 [91] A. M. Sirunyan et al. (CMS), Phys. Rev. Lett. 122, 12, 121803 (2019), [arXiv:1811.09689].
 [92] M. Aaboud et al. (ATLAS), JHEP 01, 030 (2019), [arXiv:1804.06174].
 [93] G. Aad et al. (ATLAS), Phys. Lett. B 800, 135103 (2020), [arXiv:1906.02025].
 [94] G. Aad et al. (ATLAS), Phys. Rev. D 106, 5, 052001 (2022), [arXiv:2112.11876].
 [95] G. Aad et al. (ATLAS), JHEP 11, 163 (2020), [arXiv:2007.14811].
 [96] A. M. Sirunyan et al. (CMS), Phys. Rev. D 102, 3, 032003 (2020), [arXiv:2006.06391].
 [97] A. Tumasyan et al. (CMS), JHEP 05, 005 (2022), [arXiv:2112.03161].
 [98] A. Tumasyan et al. (CMS) (2021), [arXiv:2106.10361].
 [99] A. Tumasyan et al. (CMS), JHEP 07, 095 (2023), [arXiv:2206.10268].
[100] G. Aad et al. (ATLAS), JHEP 09, 091 (2019), [Erratum: JHEP 06, 042 (2020)],

       [arXiv:1906.08589].
[101] A. M. Sirunyan et al. (CMS) (2019), [arXiv:1906.05977].
[102] G. Aad et al. (ATLAS), Eur. Phys. J. C 80, 12, 1165 (2020), [arXiv:2004.14636].
[103] G. Aad et al. (ATLAS), Eur. Phys. J. C 81, 4, 332 (2021), [arXiv:2009.14791].
[104] A. Tumasyan et al. (CMS), Phys. Lett. B 844, 137813 (2023), [arXiv:2210.00043].
[105] A. Tumasyan et al. (CMS), Phys. Rev. D 105, 3, 032008 (2022), [arXiv:2109.06055].
[106] A. M. Sirunyan et al. (CMS), JHEP 01, 051 (2019), [arXiv:1808.01365].
[107] A. Tumasyan et al. (CMS), Phys. Lett. B 832, 137263 (2022), [arXiv:2201.02140].
[108] F. Abu-Ajamieh, J. S. Lee and J. Terning, JHEP 10, 050 (2018), [arXiv:1711.02697].
[109] K. Agashe et al., Phys. Rev. D76, 036006 (2007), [hep-ph/0701186].
[110] M. Aaboud et al. (ATLAS), Eur. Phys. J. C 79, 5, 375 (2019), [arXiv:1808.07858].
[111] A. M. Sirunyan et al. (CMS), JINST 15, 06, P06005 (2020), [arXiv:2004.08262].
[112] G. Aad et al. (ATLAS), JHEP 10, 061 (2020), [arXiv:2005.05138].
[113] A. M. Sirunyan et al. (CMS), JHEP 04, 031 (2019), [arXiv:1810.05905].
[114] M. Aaboud et al. (ATLAS), Phys. Rev. D99, 9, 092004 (2019), [arXiv:1902.10077].

                                                                           31st May, 2024
16  85. Extra Dimensions

[115] M. Aaboud et al. (ATLAS), Eur. Phys. J. C78, 7, 565 (2018), [arXiv:1804.10823].
[116] G. Aad et al. (ATLAS), Phys. Rev. D 102, 11, 112008 (2020), [arXiv:2007.05293].
[117] A. M. Sirunyan et al. (CMS), Eur. Phys. J. C 81, 8, 688 (2021), [arXiv:2102.08198].
[118] M. Aaboud et al. (ATLAS), Phys. Rev. D98, 5, 052008 (2018), [arXiv:1808.02380].
[119] A. Tumasyan et al. (CMS), Phys. Rev. D 106, 1, 012004 (2022), [arXiv:2109.08268].
[120] A. Tumasyan et al. (CMS), JHEP 04, 087 (2022), [arXiv:2111.13669].
[121] R. Contino and G. Servant, JHEP 06, 026 (2008), [arXiv:0801.1679].
[122] J. A. Aguilar-Saavedra, JHEP 11, 030 (2009), [arXiv:0907.3155].
[123] J. Mrazek and A. Wulzer, Phys. Rev. D81, 075006 (2010), [arXiv:0909.3977].
[124] G. Dissertori et al., JHEP 09, 019 (2010), [arXiv:1005.4414].
[125] See, for example, PDG review of Technicolor searches in this volume.
[126] M. Aaboud et al. (ATLAS), JHEP 10, 141 (2017), [arXiv:1707.03347].
[127] A. M. Sirunyan et al. (CMS), JHEP 03, 082 (2019), [arXiv:1810.03188].
[128] A. M. Sirunyan et al. (CMS), Eur. Phys. J. C 79, 90 (2019), [arXiv:1809.08597].
[129] G. Aad et al. (ATLAS), Eur. Phys. J. C 83, 8, 719 (2023), [arXiv:2212.05263].
[130] G. Aad et al. (ATLAS), Phys. Lett. B 843, 138019 (2023), [arXiv:2210.15413].
[131] M. Aaboud et al. (ATLAS), Phys. Rev. Lett. 121, 21, 211801 (2018), [arXiv:1808.02343].
[132] A. Tumasyan et al. (CMS), JHEP 07, 020 (2023), [arXiv:2209.07327].
[133] A. M. Sirunyan et al. (CMS), Phys. Rev. D 102, 112004 (2020), [arXiv:2008.09835].
[134] G. Aad et al. (ATLAS) (2023), [arXiv:2308.02595].
[135] G. Aad et al. (ATLAS) (2023), [arXiv:2307.07584].
[136] G. Aad et al. (ATLAS) (2023), [arXiv:2305.03401].
[137] G. Aad et al. (ATLAS), Phys. Rev. D 105, 9, 092012 (2022), [arXiv:2201.07045].
[138] M. Aaboud et al. (ATLAS), JHEP 05, 164 (2019), [arXiv:1812.07343].
[139] (2023), [arXiv:2302.12802].
[140] A. Tumasyan et al. (CMS), JHEP 05, 093 (2022), [arXiv:2201.02227].
[141] A. M. Sirunyan et al. (CMS), JHEP 01, 036 (2020), [arXiv:1909.04721].
[142] A. M. Sirunyan et al. (CMS), JHEP 06, 031 (2018), [arXiv:1802.01486].
[143] A. De Simone et al., JHEP 04, 004 (2013), [arXiv:1211.5663].
[144] R. Contino, Y. Nomura and A. Pomarol, Nucl. Phys. B671, 148 (2003), [hep-ph/0306259].
[145] D. B. Kaplan and H. Georgi, Phys. Lett. 136B, 183 (1984).
[146] D. B. Kaplan, H. Georgi and S. Dimopoulos, Phys. Lett. B 136, 187 (1984).
[147] T. Banks, Nucl. Phys. B 243, 125 (1984).
[148] H. Georgi, D. B. Kaplan and P. Galison, Phys. Lett. 143B, 152 (1984).
[149] I. Antoniadis et al., Phys. Rev. Lett. 108, 081602 (2012), [arXiv:1102.4043].
[150] G. F. Giudice and M. McCullough, JHEP 02, 036 (2017), [arXiv:1610.07962].
[151] G. Aad et al. (ATLAS) (2023), [arXiv:2305.10894].
[152] A. M. Sirunyan et al. (CMS), Phys. Rev. D 98, 9, 092001 (2018), [arXiv:1809.00327].
[153] I. Antoniadis and K. Benakli, Int. J. Mod. Phys. A15, 4237 (2000), [hep-ph/0007226].

                                                                           31st May, 2024
17  85. Extra Dimensions

[154] G. Aad et al. (ATLAS), JHEP 11, 138 (2012), [arXiv:1209.2535].
[155] V. Khachatryan et al. (CMS), Phys. Rev. D91, 9, 092005 (2015), [arXiv:1408.2745].
[156] K. Cheung and G. L. Landsberg, Phys. Rev. D65, 076003 (2002), [hep-ph/0110346].
[157] M. Farina et al., Phys. Lett. B772, 210 (2017), [arXiv:1609.08157].
[158] M. Aaboud et al. (ATLAS), Eur. Phys. J. C 78, 5, 401 (2018), [arXiv:1706.04786].
[159] G. Aad et al. (ATLAS) (2019), [arXiv:1906.05609].
[160] A. M. Sirunyan et al. (CMS), JHEP 06, 128 (2018), [arXiv:1803.11133].
[161] A. M. Sirunyan et al. (CMS), JHEP 06, 120 (2018), [arXiv:1803.06292].
[162] A. Tumasyan et al. (CMS), JHEP 09, 051 (2023), [arXiv:2212.12604].
[163] T. Appelquist, H.-C. Cheng and B. A. Dobrescu, Phys. Rev. D64, 035002 (2001), [hep-

       ph/0012100].
[164] A. Datta, K. Kong and K. T. Matchev, New J. Phys. 12, 075017 (2010), [arXiv:1002.4624].
[165] N. Deutschmann, T. Flacke and J. S. Kim, Phys. Lett. B771, 515 (2017), [arXiv:1702.00410].
[166] J. Beuria et al., Comput. Phys. Commun. 226, 187 (2018), [arXiv:1702.00413].
[167] Avnish et al., Phys. Rev. D 103, 115011 (2021), [arXiv:2012.15137].
[168] G. Panico, M. Safari and M. Serone, JHEP 02, 103 (2011), [arXiv:1012.2875].
[169] J. Scherk and J. H. Schwarz, Phys. Lett. 82B, 60 (1979).
[170] A. Pomarol and M. Quiros, Phys. Lett. B438, 255 (1998), [hep-ph/9806263].
[171] I. Antoniadis et al., Nucl. Phys. B544, 503 (1999), [hep-ph/9810410].
[172] R. Barbieri, L. J. Hall and Y. Nomura, Phys. Rev. D63, 105007 (2001), [hep-ph/0011311].

    31st May, 2024
