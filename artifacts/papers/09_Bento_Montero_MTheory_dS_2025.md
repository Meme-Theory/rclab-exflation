# Bento Montero MTheory dS 2025

**Source:** `09_Bento_Montero_MTheory_dS_2025.pdf`

---

arXiv:2507.02037v2 [hep-th] 21 Jul 2025                                                                                                             IFT-25-070

                                         An M-theory dS maximum from Casimir energies
                                         on Riemann-flat manifolds

                                         Bruno Valeixo Bento and Miguel Montero
                                           Instituto de F�isica Te�orica IFT-UAM/CSIC, C/ Nicol�as Cabrera 13-15, Campus de Cantoblanco,
                                           28049 Madrid, Spain
                                           E-mail: [email redacted], [email redacted]

                                         Abstract: We initiate the study of flux compactifications on non-supersymmetric Riemann-
                                         flat manifolds (RFM's) with Casimir energy. While curvature and other corrections are
                                         suppressed in RFM's, the inclusion of Casimir energies allows one to evade standard dS
                                         no-go theorems, and the absence of orientifolds or other singular sources means that the
                                         construction is completely captured by ten or eleven-dimensional supergravity. We obtain
                                         a fully explicit formula for the Casimir stress-energy in a general RFM, including its ten
                                         or eleven-dimensional profile. The Casimir energy localizes in particular loci of the RFM,
                                         which we call "Casimir branes". The tension of Casimir branes sometimes cancels exactly,
                                         due to a spacetime analog of worldsheet Atkin-Lehner symmetry. We use Casimir energies
                                         to construct an explicit dS5 maximum solution of a flux compactification of M-theory on a
                                         specific 6-dimensional RFM. The resulting solution is scale-separated, has a vacuum energy of
                                         10-15 in five-dimensional Planck units, the Hubble radius is 107 Planck lengths, and the light
                                         fields have masses of order H. This is a fully explicit, top-down de Sitter maximum in M-
                                         theory, with precisely computable vacuum energy. While the solution is not parametric, it is
                                         under extraordinary control: higher derivative and loop corrections to the vacuum energy are
                                         suppressed in powers of a small parameter V /V  10-10, and M2 and M5-brane instantons
                                         are negligible. In short, the solution survives all known corrections. Nevertheless, it might be
                                         sensitive to more exotic ones, such as e.g. loops of 11d Planckian virtual black holes if there
                                         were a large enough number of them. We also extend the Ewald numerical method for lattice
                                         sums to arbitrary dimensions and develop an efficient numerical implementation.
Contents

1 Introduction and basic idea                                   2

2 Warm-up: A dS7 from M-theory on T 4                           7

3 A review of Riemann-flat Manifolds (RFM's)                    14

4 Casimir energy in RFM's                                       20

4.1 Casimir energy of massless free fields                      20

4.2 Free fields in a quotient space: the method of images       22

4.3 Casimir energy formula for RFM's                            25

4.4 Explict formula for RFM Casimir energy & "Casimir branes"   27

4.5 Casimir branes and Atkin-Lehner symmetry                    42

4.6 Numerical evaluation of Casimir energies                    44

5 A dS5 maximum in M-theory                                     47

5.1 The Riemann-flat manifold F6                                47

5.2 Casimir energy                                              52

5.3 Flux potential                                              56

5.4 The dS5 maximum                                             59

5.5 Characterization and control of the solutions               61

5.6 The dS5 � F6 vacuum of M-theory: An executive summary       68

6 A scan for M-theory dS4 maxima                                70

6.1 Cyclic Riemann-flat manifolds in 7d                         70

6.2 Example: F7 = T 7/Z7                                        73

7 Conclusions                                                   78

A G4 flux quantization in M-theory                              82

B Lattice sums on RFM's with 1-dimensional invariant subspaces  83

C Ewald summation                                               84

D Numerical estimate                                            88

E Alternative derivations of the Casimir formula for RFM's      88

E.1 Direct evaluation in position space                         89

E.2 RFM Casimir formula from Ewald expressions                  91

                                         �1�
F Lorentz group traces for Casimir energies  94

G Cyclic 7d RFM's with S1 base               99

1 Introduction and basic idea

One of the most pressing open questions in String Theory is to ascertain beyond doubt
whether it can accommodate long-lived accelerated expansion. The foremost reason for this
is to connect to observations [1, 2]. However, independently of any observational implications,
whether long-lived accelerating expansion exists or not is an essential question about the non-
supersymmetric Landscape that we must elucidate. There are arguments (some of them older
than the authors of this paper [3]) to the effect that we do not expect to have accelerating
cosmologies near the boundaries of moduli space, where strings are arbitrarily weakly coupled
or we have some other control parameter that can be tuned arbitrarily [4, 5]. Together with
the lack of explicit string constructions, these have led to concrete Swampland conjectures
[6, 7] that acceleration may not exist in asymptotic regions of moduli space [8�13], a statement
for which there is now ample systematic evidence (see e.g. [14�16]).

     In practice, all of the above means that any stringy attempt at long-lived phases of
accelerated expansion is pushed away from the asymptotic boundaries of moduli space. Since
it is hard to imagine a fully non-perturbative gravitational setup where we would have any
measure of control, most accelerated expansion scenarios end up living on the edge between
asymptotic and non-perturbative, where a description in terms of string perturbation theory,
or a large internal space may still be expected to hold, but where additional non-asymptotic
ingredients are added to the mix, in order to avoid the asymptotic no-go theorems. This
is certainly the case of the existing de Sitter scenarios, such as KKLT1 [18] and LVS [19],
whose fate is still under debate (see e.g. [20�32]) in large part because the mix of ingredients
required is quite difficult to control. The origin of this complexity can be traced in part to
one particular no-go theorem [33, 34] which ensures that no de Sitter critical point may be
achieved only through the use of classical supergravity ingredients (fluxes and curvature).
To circumvent this, existing dS scenarios include stringy sources such as orientifolds, non-
perturbative effects, and/or higher-derivative corrections, all of which are beyond the reach
of 10 or 11-dimensional supergravity, and are intrinsically complicated, leading to questions
such as e.g. the backreaction of the singular sources introduced [20] and so on.

     The goal of this paper is to sidetrack all of this discussion, by looking at a different,
much simpler way to avoid the no-go theorem of [34], and which can be fully analyzed us-
ing supergravity tools: Casimir energy [35, 36], the quantum response of matter fields to a
non-supersymmetric background. This idea, pioneered in [37], exploits the fact that Casimir

    1See also [17] for heterotic orbifold models that include KKLT-like ingredients, such as hidden sector gaugino
condensation, with de Sitter maxima and a supersymmetric Standard Model.

                                                         �2�
energy (which can violate the energy condition assumed in [34]) can be computed explicitly
and reliably, using standard techniques (see e.g. [35, 36, 38]). This can be done for many
theories, including 11-dimensional supergravity, as well as in all 10-dimensional supergravities
arising as the low-energy limits of String Theory. On top of the key ingredient of Casimir
energy, the approach of [37] also involves a non-trivial warping throughout the compactifi-
cation manifold (but much weaker than in the strongly warped throats appearing in KKLT
and LVS), due to the class of manifolds considered, which are hyperbolic.2 Although warping
is a classical phenomenon, fully accounted for in supergravity, it can lead to complicated
non-linear equations that are hard to solve explicitly. In this paper, we will instead look at
compactifications involving Casimir energy and fluxes on manifolds equipped with a metric
that is Riemann flat on a first approximation; as a result, warping will be very small every-
where, and we will be able to solve and describe the solutions fully explicitly as a perturbative
series around the flat metric, where each term will be less important than the preceding one.3

     The main technical result is a fully explicit formula to compute Casimir energies in a
general Riemann-flat manifold (RFM). Interestingly, we find that the Casimir energy is a
sum of contributions, each of which is localized on a specific submanifold of the RFM, which
we also determine explicitly. Since the contributions are localized, we may think of them
as effective "Casimir branes"; the Casimir energy may then be replaced by a system of such
branes which behaves in a similar way to the usual D-branes and orientifolds of more standard
string compactifications. Therefore, the Casimir brane picture allows us to pull back a lot of
the intuition from these models and use it effectively for model building with Casimir energies.

     Furthermore, the Casimir formula that we obtained allows us to determine not just the
contribution of Casimir energies to the lower-dimensional vacuum energy, but the explicit
11d profile of the vacuum energy as well. In other words, we go beyond the "smearing
approximation" [44, 45], which is where most analysis of 4d effective field theories derived
from string theory stop. We obtain in this way completely smooth sources of negative energy
in 11 dimensions; the "Casimir branes" have a finite thickness which we compute explicitly,
unlike the singular orientifolds commonly used as a source of negative energy, and whose
ten-dimensional backreaction is a source of confusion [46�48]. To put it in another way, when
it comes to computing the backreacted higher-dimensional solution, our non-supersymmetric
solutions are in a much better position that e.g. DGKT [49].

     In some special cases, we will find that the tensions of different Casimir branes all add
up to zero, so that the corresponding contribution to Casimir energy vanishes. As we will

    2Hyperbolic manifolds were also used in the minimal dS constructions of [39, 40], in which smeared D-
brane/O-plane sources are used instead of Casimir energies. Negative curvature spaces (together with non-zero
Romans mass) were identified as necessary complements to a Type IIA setup with fluxes and localised sources
in order to obtain de Sitter solutions. The presence of the localised sources, which was dealt in that reference
by means of a smearing approximation, brings in the complexity that is also present in models like KKLT and
LVS.

    3In [41�43] non-supersymmetric heterotic string models with D-term uplifts are studied in the free fermionic
formulation, where higher-loop contributions that arise after a stringy Scherk-Schwarz spontaneous supersym-
metry breaking seem to allow for positive vacuum energies. Whether these dS solutions survive full stabilisation
of the moduli (including the dilaton) requires further study.

                                                         �3�
see in Subsection 4.5, this phenomenon is a spacetime analog of an exotic mechanism to
produce a vanishing cosmological constant in string perturbation theory, dubbed "Atkin-
Lehner symmetry" [50�52]. The mechanism had so far only been realized in very stringy
models with a two-dimensional target space (see also [53] for a recent string-inspired discussion
on generalizations of this). The version that we find works in higher dimensions, requires no
worldsheet description, and can be reliably analyzed with EFT techniques. The resulting
enlargement of the class of quantum gravity models where we can find a symmetry reason for
a vanishing vacuum energy may have interesting implications for the construction of top-down
models with a vanishing cosmological constant.

     Armed with this picture and the explicit Casimir energy formula, we embark on a sys-
tematic exploration of the landscape of flux compactifications of RFM's--focusing on the
M-theory corner--and look for de Sitter critical points. A major technical obstacle is that
the tension of Casimir branes in general depends on moduli in an intricate way, via an infi-
nite sum that converges slowly; we overcome this obstacle by extending the method of Ewald
summation (used for similar sums that appear in physical chemistry) to arbitrary dimensions,
and constructing an efficient numerical implementation for it.

     Even within the M-theory corner, the landscape of RFM compactifications is vast. In
this paper we restrict to compactifications of M-theory down to four and five dimensions,
with G4-flux turned on. In an upcoming paper [54], we will show that dS4 minima cannot
be found from an M-theory compactification on an RFM with only these ingredients due to
tadpole restrictions. Here, instead, we will look for dS saddle points (that is, positive saddles
of the vacuum energy with at least one unstable direction4). These provide a clean and
clear example of the qualities of RFM compactifications. Furthermore, recent DESI results
[59�62] have provided some evidence for dynamical dark energy as opposed to a cosmological
constant. If this is the case, a dS maximum like the ones described in this paper would
be phenomenologically favored over a minimum [63]. Furthermore, the maxima we find are
always at enhanced symmetry points, which could help addressing the question of initial
conditions that one inevitably faces when describing Dark Energy with a maximum of the
potential via e.g. a thermal Coleman-Weinberg-like transition.

     After an exhaustive study of 2-moduli dS4 compactifications of M-theory on an RFM
of cyclic holonomy, we have found no dS maximum. While dS4 maxima in M-theory may
well exist when compactifying on RFM's of non-cyclic holonomy, the focus of our paper is
instead a dS5 solution that we found in five dimensions, and which we describe in the following
paragraphs.

The main result: A dS5 � F6 maximum in M-theory
We found a concrete Riemann-flat manifold F6 = T 6/Z8 such that an M-theory compactifi-
cation on F6 with G4 flux along a particular 2-cycle yields a five-dimensional de Sitter solu-
tion of M-theory, with vacuum energy Vsaddle = 3.68 � 10-15 5-5. The solution is supported

    4The persistence of unstable directions in de Sitter solutions was previously noted e.g. in [55�58] for the
Type IIA constructions with O-plane sources like the ones mentioned in footnote 2 [39, 40].

                                                         �4�
by a balance of Casimir energy and G4-flux. It is also scale separated, with a hierarchy
KK  2.5 � 10-5H0-1. The scalar sector of the low-energy EFT contains five saxionic scalars,
with masses mi2 = {90.45, 23.82, -309.55, -47.43, -45.16} � H02, as well as five axions that get
negligible masses from non-perturbative effects. See Table 2 for more details on the solution
and its properties.

     To our knowledge, this is the first time a concrete, top-down dS maximum compactifica-
tion in string or M-theory has been realized in sufficient detail to compute the vacuum energy
precisely, as well as the spectrum of low-lying excitations. For contrast, recent work [64]
has robust arguments for the existence of dS maxima in stringy regimes, but the vacuum is
estimated to be only around 10-3 in Planck units and there is not enough control to reliably
compute the vacuum energy or the masses of low-lying fields. Similar control issues affect
other proposals of dS maxima within supergravity [39, 40, 64�68], and all the more so other
constructions of dS minima [18, 19, 37], where the intricate nature of the construction means
that some O(1) guesswork (e.g. in the values of Pfaffian factors, effects of stringy corrections,
etc) becomes all but necessary. Furthermore, a controlled dS5 saddle can also be related to a
dS4 via the dS/dS correspondence [69, 70].

     The property that sets our solution apart from these proposals is that the Riemann-
flat manifold affords us extraordinary control over corrections, which we discuss in detail in
Section 5.5. As explained above, our explicit Casimir formula provides a completely smooth
picture at the 11-dimensional level, which in turn allows us to estimate the classical 11d
backreaction explictly (and would allow for a systematic, rigorous treatment of the full 11d
profile in future work). Higher-derivative and loop corrections are similarly suppressed, all in
powers of a small parameter   10-10, related to the smallness of the vacuum energy and
the large volume of the internal space. M2 and M5-brane instantons are negligible. Since
there are no singular sources (branes, orientifolds), or non-perturbative effects, this means
that our solution survives all the known effects that are normally discussed in the context
of string compactifications. An explicit non-supersymmetric compactification, constructed
in a perturbative expansion around an exact solution of the classical equations of motion,
like the one we will find here, also aligns with the considerations in [71], which argued that
the calculation of quantum effects around classically time-dependent vacua is fraught with
subtleties, and that we lack the proper framework to do so in flux compactifications of String
Theory. In that same reference, it was suggested that, whenever applicable, supergravity
might be an appropriate substitute, that is, as long as volumes are large and there are no
stringy ingredients such as branes, etc. The solutions constructed here are in precisely that
regime.

     The question remains whether there could be unknown effects that destabilize the solu-
tion. The smallest closed geodesic is only 6.1 eleven-dimensional Planck lengths long, so one
could imagine loops of 11-dimensional virtual black holes around this circle. Although we
estimate the effect of a single black hole to be small, based both on Bose-Fermi cancellation
and general properties of the Casimir energy, we do not really know how many long-lived
black holes M-theory has at Planckian energy. If there is an unexpectedly large number of

                                                         �5�
these (larger than what a na�ive extrapolation of the BH entropy formula would suggest),
they could destabilize the solution. Because of this, we cannot tell rigorously whether the
solution survives or not, but the larger point is that the Landscape of RFM flux compacti-
fications is a promising arena where we may get closer than ever to a fully controlled string
compactification exhibiting positive vacuum energy.

     The paper is organised as follows:

    In Section 2 we present a simple example of a dS7 from M-theory on T 4 that will serve
       as a warm-up for the constructions studied in the following sections.

    In Section 3, we briefly introduce Riemann-flat manifolds and their properties, as well
       as the necessary tools for the compactifications studied here; this includes the mathe-
       matical description of RFM's, their invariant metrics and allowed spin structures; we
       also comment on their classification and focus on the particular case of cyclic RFM's.

    Section 4 is devoted to the computation of Casimir energies in Riemann-flat manifolds;
       starting with the Casimir energy of massless free fields, we explain how it can be com-
       puted in quotient spaces through the method of images and derive an explicit formula
       for the Casimir energy on Riemann-flat manifolds; we show in particular how the com-
       putation of the Casimir energy on RFM's is always reduced to a similar computation
       performed on the invariant subspace with respect to each element of the holonomy group
       of the RFM, which often has dimension lower than the RFM, and introduce the concept
       of "Casimir branes"; we also explain how the vacuum energy can sometimes vanish as
       a result of a spacetime version of an Atkin-Lehner symmetry. We end this section by
       extending the technique of Ewald resummation to arbitrary dimensions, which allows
       for an efficient evaluation of the sums over lattices required for the Casimir energies,
       especially when the invariant subspace has lower dimension.

    In Section 5, we apply the results of Sections 3 and 4 to M-theory compactified on a 6-
       dimensional Riemann-flat manifold, which results in a controlled dS5 solution; we work
       through this construction in detail, carefully computing the Casimir and flux potentials,
       analysing the 5d saddle point and discussing the control of this solution.

    Finally, in Section 6 we scan a full family of cyclic 7-dimensional RFM's in the search
       for a dS4 solution, showing that none of the RFM's whose study can be reduced to a
       2-moduli problem through the use of symmetry arguments can provide a saddle for the
       Casimir potential; we also comment on cases that remain open, all of which require the
       study of at least three moduli.

    We conclude in Section 7, where we summarise our results and discuss their relation to
       current and future work. Several appendices contain details or alternative derivations
       of results in the main text.

Finally, the following list summarizes some aspects of our notation:

                                                         �6�
    We are interested in compactifications of M-theory or other higher-dimensional string
       theories, with spacetime dimension D. The dimension of the compactification manifold
       will be k, and the lower-dimensional theory has dimension d = D - k.

    We use a mostly minus metric convention, and greek indices denote D-dimensional
       tensor components.

    The coordinates in the internal k-dimensional manifold will be denoted as z or zi.

    When we write an RFM as Euclidean space Rk modulo a group, that group is called B,
       i.e. RFM = Rk/B. An element of B is an affine transformation of Rk, of the form D +b,
       and will be denoted abstractly as b  B. The quotient group that captures holonomies
       in an RFM is called , and    is a generic element. Whenever we want to emphasize
       the image of a given b represented as D +b, via the projection map to , we will write
       D + b. Since we will be looking at cases where  is cyclic, we will often choose a
       specific generator of , which we will call g (for generator), and work with Dg + bg.
       The order of a group  will be denoted as ||.

    We denote the trace of an element D under a given representation r of SO(D - 2) as
       Trr(D). We will sometimes collect the traces under all bosonic and fermionic represen-
       tations using the notation TrB(D) and TrF(D), respectively.

Note added: As this work was nearing completion we learned of [72], which also discusses
Casimir energies in Riemann-flat manifolds in the context of supergravity theories.

2 Warm-up: A dS7 from M-theory on T 4

The key idea in this paper is to use quantum effects to evade no-go theorems like [34] and
achieve de Sitter solutions. In this section, we will take a first step towards this goal by explain-
ing the general idea and a simple implementation of it, which will motivate the central topic of
this paper--an exploration of the Landscape of Riemann-flat manifolds, or RFM's for short.
To evade the no-go theorem of [34] we need sources of stress-energy in the compactification
that violate the null energy condition. Popular choices are orientifolds or higher-derivative
effects [73�75], but here we will choose Casimir energies [35], which we will now review; a
good source is [36], or the textbook [38].

     Consider a D-dimensional QFT in a background spacetime M equipped with a metric
g. This may be a bona fide QFT or merely a low-energy EFT, possibly coupled to gravity;
if so, we will also take into account the standard linearized graviton and its standard Fierz-
Pauli action and couplings to matter. Other than the linearized fluctuation, which will be
treated as just another quantum field on M, the background geometry will be taken to be
non-dynamical. Finally, if the QFT is spin or has any other symmetries, we will also consider
M to be equipped with the appropriate background fields. We will however set to zero any

                                                         �7�
background gauge fields for continuous symmetries (see [36, 76, 77] for a case where this
dependence is taken into account in a particular example).

     The basic observable in any QFT like the one just described is the stress-energy tensor
T�, and its expectation value in the vacuum state,

                     T� M.                                             (2.1)

When there is no ambiguity, we will omit the M subscript. In the general case, absent
any symmetries, the vev T� is a generic, non-zero tensor field on M. It is the quantum
stress-energy of the QFT on the given background, and it is called the "Casimir stress-energy
tensor" or, more vaguely, "Casimir energy". In some special cases, when the background
M preserves some symmetries, the vev T� can be constrained. For instance, if M is a
maximally symmetric space (such as dS, Minkowski, or AdS spaces) then T� =  g�. If
the QFT additionally preserves supersymmetry in a maximally symmetric M, then  = 0; in
general, unbroken supercharges can constrain some components of T�M.

     We will postpone a detailed exposition of how to compute Casimir energies to Section 4
and describe now the basic approach that we will follow in this paper. Much like in [37],
we are after dS solutions of Einstein's equations where the effects of the Casimir energy are
taken into account. In other words, we seek to solve Einstein's equations

                     G� = 8G T�Cl + T � M ,                            (2.2)

where T�Cl is some classical piece, which in our case will come entirely from fluxes in the
internal space. We will then balance the classical and Casimir pieces against each other, to

find a backreacted solution of Einstein's equations (2.2) with a positive cosmological constant.

      One may wonder how this approach could be self-consistent, given that T �M was

computed in a background geometry, on which it now backreacts via (2.2). The idea is that,

under favorable circumstances, it is possible to treat the right-hand side of (2.2) as a small

perturbation, and solve the problem iteratively. More concretely, suppose that the manifold

M admits a Ricci-flat metric g(0) (which therefore solves the vacuum Einstein equations), on

top of which the Casimir energy and flux term in (2.2) turn out to be small in Planck units,

i.e.

                     T�Cl  T � M   MPD,   1.                           (2.3)

We can then perturb

           g(0)  g(0) +  g(1) + . . . , T� =  T�(0) + 2 T�(1) + . . .  (2.4)

and expand Einstein's equations as a perturbative series in (2.2), to obtain a system of

equations

                     G�(n) = 8G T�(n-1) ,                              (2.5)

which can be solved iteratively in . Each of these is a linear differential equation, for which

                     �8�
a solution typically exists (and can be ensured by rigororous theorems in the elliptic case
[78, 79]). Importantly, the right-hand side of (2.5) at order n only depends on quantities
computed at order n - 1, as is standard in perturbation theory. The whole system can then
be solved iteratively. For small enough , one expects this expansion to be convergent, and
a solution to the full D-dimensional backreacted Einstein's equations to be achievable by
this procedure. The smallness of the parameter  also ensures the irrelevance of e.g. higher-
derivative corrections (which are proportional to a power of ).

     In this paper, we will only carry out the first level of the perturbative analysis (2.5) at
n = 1. However, as remarked in the Introduction, the fact that the only ingredients in (2.2)
are Casimir energies and fluxes, and both are under good control from ten/eleven-dimensional
supergravity, means that going to higher n is conceptually straightforward (albeit technically
cumbersome). The point is that a fully explicit 10d/11d uplift of the solutions we propose
here is certainly feasible, via the procedure just outlined. To our knowledge, this is not the
case for any other proposal for dS minima or maxima in String Theory, including [64, 66�
68]. The fact that the backreaction of our dS solutions can be studied explicitly in eleven
dimensions is a remarkable property, which we wish to emphasize. It means that the fate
of these vacua can be ascertained with a finite amount of work, and have a small chance
of leading to endless discussions. Even some supersymmetric AdS vacua, such as DGKT
[49], do not have a fully clear 10d uplift, due to the presence of singular, stringy sources
as orientifolds [46�48] that complicate the 10d analysis. Nothing like that can happen for
the vacua presented here. In the proposal of [37], which also uses Casimir energies as a
key ingredient to achieve de Sitter, one may also solve for the 11-dimensional backreaction
explicitly, since there are no ingredients beyond supergravity; however, unlike for an RFM,
there is no analog of the "unperturbed" metric g(0), since hyperbolic manifolds do not carry a
metric that solves Einstein's equations before Casimir energies are included. As a result, one
must solve the eleven-dimensional equations all at once, in contrast to the easier situation in
an RFM.

     We can now particularize our discussion to the compactification ansatz we are interested
in. Specifically M will be of the form

M = RD-k � Nk,                                                       (2.6)

where the manifold Nk is compact and the metric on M is of the form

ds2M = ds2 + ds2Nk ,                                                 (2.7)

with ds2 being a maximally symmetric Lorentzian metric with cosmological constant 5.
Due to the maximal symmetry of the non-compact dimensions, the stress-energy tensor vev

    5In general, we would have to introduce a warping function e in front of the first term of (2.7). However,
since our starting metric g(0) will be Riemann-flat and thus unwarped,  will not appear until second order in

the  expansion. We will not reach this level in this paper and hence ignore  altogether.

�9�
T�M has a similar decomposition to the metric in (2.7), so that

T� RD-k�Nk = ^ g�RD-k,  + T�Nk .                                 (2.8)

Crucially, the function ^ can have either sign; we will be interested in the case ^ < 0, where

the corresponding term in the stress-energy tensor violates the (D - k)-dimensional version
of the null energy condition. The tensor T�Nk only has legs along the compact manifold Nk.
In general, ^ is related to T�Nk by stress-energy tensor conservation (absent gravitational
anomalies) �T �M = 0. For a CFT, there is an additional relation coming from the trace
anomaly, but there are no other general relationships between ^ and T�Nk . However, typically
these quantities have to be computed on a case-by-case basis.

     As explained above, in this paper we just aim to find the backreacted lower-dimensional

cosmological constant at first order, and leave the higher-order analysis to further work. An

explicit formula for the cosmological constant at this order can be obtained by taking the

00 component of Einstein's equations (2.2) and integrating over the compact space Nk. The
resulting system is described by a (D - k = d)�dimensional effective field theory, where the

flux piece is described by the standard flux potential [73], and the Casimir stress-energy is

obtained from an effective potential

VCas =  dk  z         ^  ,                                       (2.9)
                 -g0

by integrating the Casimir stress-energy tensor over the whole of the internal compact space
Nk. Since it will not cause ambiguity for us, we will refer to the quantity VCas as the Casimir
potential or Casimir energy of the compactification. In general, VCas receives contributions
from both massless and massive D-dimensional fields, but the contributions of massive states
are suppressed by factors of e-mR [36], where m is the mass of the field and R is a quantity
with units of length that measures the volume of Nk according to the metric g(0) (so that
Rk  Vol(Nk), possibly up to O(1) constants). In this work, we will focus on compactifications
of 10d and 11d quantum gravities, where the gap to the first massive state is controlled by the
higher-dimensional Planck or string scale. As a result, we will ignore contributions of massive
states, and focus solely on the Casimir potential generated by the massless, D-dimensional
fields. Since the Casimir energy is the response function of the QFT in the background
spacetime metric g(0), which we take to be Riemann-flat, the only dimensionful parameter
VCas can depend on in a scale-invariant theory is R. Therefore, dimensional analysis fixes

             C                                                   (2.10)
VCas  - Rd ,

where the quantity C (that may depend on dimensionless moduli of Nk) is the Casimir coef-
ficient. The extra minus sign has been introduced for reasons that will become clear below.

        � 10 �
The total lower-dimensional scalar potential is then given by

                 V (d) = VFluxes + VCas ,                                (2.11)

and our goal will be to find saddles of (2.11) where V (d) > 0. The flux term contributes a
sum of positive terms, all of which scale as powers of R [73]; specifically, a p-form field flux
in the internal space produces a contribution to VFluxes scaling like

                                 n2p   .                                 (2.12)
                               R2p-k

After rescaling to the lower-dimensional Einstein frame, one gets a potential schematically of

the form

          V (d)    1                    n2p  -  C   .                    (2.13)
                                      R2p-k     Rd
          MPd      Rd       k  p
                       d-2

that is a sum of negative powers of R. It follows that, to achieve a saddle with V (d) > 0, at
least one term has to be negative. Since the flux terms are positive definite, our only chance
is C > 0. Indeed, when C > 0 the stress-energy tensor violates the null-energy condition,
and can thus evade the no-go of [34]. This is why C was defined with an extra minus sign in
(2.13). An analogous role is played by orientifolds in standard flux compactifications [73].

     We will look for maxima of (2.13) where the Casimir contribution is balanced by fluxes,
as illustrated in Figure 1. One could try to add more fluxes to get a dS minimum, analogously
to the construction in [37]. Finding a minimum is trickier than it seems at first glance, due to
tadpoles and other stringy features, and we leave a detailed discussion to a future publication
[54]. However, finding a maximum does not seem hard at all! We will finish this section by
describing one such concrete first attempt, a close relative of the non-susy AdS vacuum in
the Appendix of [80] (see also [81]).

     Consider M-theory on T 4, threaded by n4 units of G4-flux. The resulting seven-
dimensional theory has 10 geometric moduli, coming from the size R of the T 4 and its shape
moduli. Although the Casimir coefficient C can in principle depend on all of these, there
are special points of moduli space where we can ensure that the dependence of C on these
moduli vanishes at first order, due to symmetries. Specifically, suppose we are at a point in
T 4 moduli space where the lattice  defining the T 4  R4/ has a non-trivial symmetry
group. For instance, we could take the lattice  to be the root lattice of the C4 Lie algebra
rescaled by R. This is the lattice generated by the vectors

          (R, -R, 0, 0), (0, R, -R, 0), (0, 0, R, -R) and (0, 0, 0, 2R)  (2.14)

in R4 equipped with its standard inner product. Then the T 4 and the Casimir energy are
invariant under the action of the Weyl group W (C4), and this action fixes all T 4 moduli to
a single point. As a result, the gradient C with respect to T 4 shape moduli transforms

nontrivially under W (C4), and invariance under it means it has to vanish. Thus, at the C4

                               � 11 �
point in moduli space, we can ignore all shape moduli of T 4, and the problem is effectively
one-dimensional--we only need to care about the size modulus R. The use of symmetries to
find saddle points of functions has a long history, but see [81] for recent applications (also
involving Casimir energy) and [64] where a version of this idea including stringy symmetries
was applied to the search of dS maxima.

V(R)

                                                            Vflux
                                                            VCas
                                                            Vtotal

                                                                    R

Figure 1. In this paper, we will look for dS maxima solutions where a negative Casimir energy
contribution (blue dashed line) and a flux contribution (red dashed line) generate a combined potential
(black solid line) for the volume modulus R with a maximum. There is no curvature contribution since
the manifold is Riemann-flat. Due to Einstein frame rescalings, the value of the maximum can easily
become small in Planck units even for moderately large R. Other moduli not included in this picture
will also be saddle points due to additional symmetries present at the maximum.

With these provisions, the scalar potential (2.13) becomes

V (7d)  191  7       2    n24       C
 M77 =  2R4  5    2  3  2R4131      R7

                                 -        ,                 C  8.827 .  (2.15)

The factors of  in front of the flux piece come from imposing the correct quantization

conditions for the M-theory G4 flux; see [82�85] and Appendix A for details. The value of
the Casimir coefficient for M-theory on T 4 in (2.15) will be calculated in Section 4.3; for now,
we merely remark that it depends on the spin structure on T 4, and that the number quoted
above corresponds to an antiperiodic spin structure along all cycles of the T 4. Finally, we

have rescaled to Einstein frame by reducing the 11d integrated potential and expressing it in

units of the reduced seven-dimensional Planck's mass

             M75    Vol(T 4)  =  2 R4  ,                                (2.16)
                       191       191

where 11 is the reduced 11-dimensional Planck length. The potential (2.15) does have a

                     � 12 �
maximum, at

             R      2.58 11  ,  V (7d)    6.85 � 10-6 n442/5 .  (2.17)
                      n24/3      M77

Even taking the smallest possible value n4 = 1, the radius is Planckian, with higher values
of n4 leading to even smaller radii6. The upshot is that by this simple means we do get a
de Sitter maximum. The vacuum energy is only 10-6 7-7, due to a favorable combination of
numerical factors. This means that the dS maximum would have a Hubble radius equal to

[88]

             1   =  15           1480 (7d Planck lengths) ,     (2.18)

             H0     V (7d)

and hence seven-dimensional gravitational backreaction will not immediately kill the vacuum.

The hierarchy between KK and Hubble scales is around 234, so it is also a little bit scale

separated. What about 11-dimensional backreaction? The energy density in the flux piece is
around 1.7 � 10-4 -1111, and so any M-theory higher-derivative corrections of the form

                                |G4|2n                          (2.19)

will be suppressed as roughly 10-4n. Of course, the O(1) coefficients in front of (2.19), about
which little is known, are a source of trouble (see however [89�93]). If they are large enough
they could spoil the solution, but on the other hand we expect these to form an asymptotic
series, with each coefficient smaller than the next. Finally, any terms involving the 11d
Riemann tensor in combination with curvature,

                                R�k|G4|2n ,                     (2.20)

will vanish to leading order in our solution, since the leading metric on T 4 is Riemann-
flat. They will start contributing at order 2 in the expansion (2.4) where, as we have seen,
  10-4 for this solution. Therefore, they might be similarly small. Finally, using the explicit

expression for the M2-brane tension in Appendix A, these can be shown to give negligible

contributions.

     All in all, we find that the solution (2.17) is not obviously closed by any explicitly known

effects, and it might turn out to actually survive as a true M-theory vacuum. At the same
time, such a small T 4 (R  2.58) might be corrected by exotic, non-supersymmetric M-theory

effects that we know nothing about. Rather than exploring the consistency of the solution

any further, we will try to improve on it, by finding similar compactifications of M-theory

    6This is to be contrasted with the supersymmetric Freund-Rubin AdS7 � S4 compactification of M-theory
[86, 87], where increasing the 4-form flux leads to bigger radii. In that case, the AdS minimum is achieved by
a balance of the G4 flux and a curvature term, which scales as R- with  smaller than the exponent of the
flux term. On the other hand, the Casimir vacua in the main text scale as R- with  bigger than the flux
contribution. This explains the different behaviors. For the same reason, the Casimir vacua are automatically
scale-separated, while Freund-Rubin compactifications are not.

                                � 13 �
that lead to larger values of R, while at the same time preserving the nice features that
lead to increased control--chief among which is a background metric g(0) that is exactly
Riemann-flat. The next sections will further develop this approach.

3 A review of Riemann-flat Manifolds (RFM's)

Most of the mileage in the construction of Section 2 comes from the fact that the unper-
turbed metric g(0) in the compactification manifold T 4 is Riemann-flat. There are many
more Riemann-flat manifolds (RFM's) than T 4, and they share or even enhance many of

the nice properties (control under corrections, computable Casimir energy) that we used in

Section 2. This section serves as a brief introduction to RFM's and their properties. The

subject of RFM's is amply discussed in the mathematical literature, see e.g. [94].

     A k-dimensional Riemann-flat manifold Fk is equipped with a metric for which the Rie-
mann tensor exactly vanishes, so that the metric is exactly flat. Thus, these manifolds look

like Euclidean space in a finite neighbourhood of any point. In fact, the universal cover of any
Riemann-flat manifold Fk is Euclidean space Rk; this means that all RFM's arise as a quo-
tient of Rk with its standard Euclidean metric, by a subgroup B  ISO(k) of the Euclidean
group in k dimensions (the group of isometries of the standard flat metric in Rk),

Fk = Rk/B .                                   (3.1)

Importantly, the group action is free, meaning that no b  B has fixed points. This ensures
that the quotient is a manifold and not an orbifold.

     A general isometry in ISO(k) can be written as a rotation followed by a translation,

b  ISO(k) : z  D z + b , D  SO(k) ,           (3.2)

so every element in B can be presented in this form. There is a natural normal subgroup of

B, corresponding to all those b  B with D = I; this is called the translation subgroup. The
corresponding vectors bi generate a lattice   Rk, that can be identified with the translation
subgroup itself. The quotient (3.1) producing Fk can be taken in two steps, where in the
first we quotient Rk by the lattice  to produce a torus (since we are interested in compact
manifolds, we will take the lattice  to be of full rank k),

T k = Rk/ .                                   (3.3)

This torus is then quotiented by , the group of isometries of T k defined as the quotient of
B by the translation subgroup,

  B/  , b  b iff b  b-1   .                   (3.4)

In practice, representatives of an element    are given by affine transformations of the
form (3.2) where b is taken modulo translations. Furthermore, elements in  must preserve

� 14 �
the lattice , or otherwise the quotient would be empty. This also means that  is a finite

group of isometries of T k. In mathspeak, one says that these groups fit into an exact sequence

of abelian groups,

                    0 -  - B -  - 1 ,                                            (3.5)

and that the group  is a subgroup of the automorphism group of the lattice . Whenever
we want to specify the class  corresponding to a given affine transformation, we will indicate
it via a subscript, as in D z + b. The group  is also called the point group or holonomy
group of the RFM, since as an abstract group, it is isomorphic to the group of rotation ma-
trices D, which are entirely responsible for any holonomy that vectors take upon following
a closed curve, since the manifold is Riemann-flat. Thus RFM's have finite holonomy groups
and, in fact, they are the only manifolds with this property [95]. The fact that  is isomor-
phic to a subgroup of SO(n) that preserves the lattice  (equipped with the standard inner
product) means that it is a crystallographic group in k dimensions, about which much is
known. Hence one may think of RFM's as "crystals", similar to the familiar Brillouin zone
of condensed matter systems [96]. However, not any crystallographic group gives rise to an
RFM--demanding absence of fixed points in the  action (called torsion-freeness of B in the
math literature) leads to constraints on the pairs (D,b). For instance, one such restriction
is that the fixed-point equation for each generator individually,

                    D z + b = z + l , l   ,                                      (3.6)

has no solution. This can be rearranged to give

                    (D - I) z + b = 0 mod  .                                     (3.7)

Since the operator on the left-hand side is the projector onto the non-invariant subspace of
D, this equation will have a solution unless b has a non-zero component along the invariant
subspace of D. Thus, D must have a non-trivial invariant subspace, which is not true for
general crystallographic actions.

     Even with torsion-freeness taken into account, there is still a large Landscape of RFM's.
One can prove [95] that

    Two RFM's with defining groups B , B are isomorphic if and only if there is an a 
       ISO(k) such that B = a  B  a-1 (i.e. one group is the same as the other up to a global
       rotation+translation), and

 There are only finitely many isomorphism classes of RFM's in each dimension k.

The second theorem tells us that the Landscape of string compactifications in RFM's is finite,
and aligns well with expected finiteness properties of the Quantum Gravity Landscape [97�
99]. The classification program for RFM's has been completed in dimensions up to six [100];
in dimension 7 and higher, it is hindered by the fact that the classification of crystallographic

                    � 15 �
groups themselves is an open problem [101]. M and F-theory compactifications to four dimen-
sions require seven and eight-dimensional manifolds, respectively, so a classification would be
highly benefitial for a detailed exploration of this corner of the string Landscape.

     Since the above discussion has been a bit abstract, we will now illustrate it with the
simplest example of RFM that is not a torus: the Klein bottle (KB). This is customarily
presented as the quotient of the complex plane C by the group of isometries generated by

                                       i                   (3.8)
                        z  -z� + , z  z +  .

                                       2

These two actions define the group B for the KB. Writing the complex number z = z1 + iz2
as a vector z = (z1, z2), we can recast the above transformations as

                        -1 0              0                (3.9)
b1 : z  0 1 z + 1/2 , b2 : z  z + 0 ,

which is more reminiscent of (3.2). The translation group is generated by b21 (which equals
translation by the vector (0, 1)) and b2, while the group  is generated by b1 with entries

taken modulo 1, and is isomorphic to Z2.

The Klein bottle is the only two-dimensional flat manifold with holonomy Z2, and is

uniquely specified by the data (, ). However, in more general examples, this data (with

 read as an abstract group) does not fully specify an RFM, since the extension problem

(3.5) may have more than one solution. An example in 3d is given by  = Z3 and  = Z2,

generated by either of

                        1 0 0                     1 0 1

                         0 -1 0  or  0 -1 0  .             (3.10)

                        001                       001

These two related RFM's were used in [102] to identify a discrete  angle in an eight-
dimensional compactification of M-theory. In general, different B's with the same (, )
can differ by the action of the matrices D and vectors b. The possibilities for D can be
somewhat constrained, using results from representation theory of integer matrices [103] as
we now explain. First, it is always possible to perform a change of coordinates in the ambient
space Rk such that the lattice  becomes exactly  = Zk, the standard integer lattice. The
price one pays for this is that the ambient metric (and hence, the induced metric on the
RFM) are no longer standard, but are replaced by some other flat metric G. However, now
the matrices D preserve the lattice Zk, and are hence represented by integer matrices of
unit determinant--matrices in SL(k, Z). Representation theory of conjugacy classes of such

                                          � 16 �
matrices tells us that they are all conjugate to block-diagonal form,

                 0    ...  ...  ... 
        B1 0

            ...                      
     0
                 0    v1   ���  vl   


             0 Bi ...      ...  ...  
            ��� 0 ...      ...       
       0
       0
D                                                                      (3.11)


       ...       ...                 

            0                       
                      � � � Il�l � � � 

                           ...     
         0 ��� 0                ...

where the diagonal blocks Bi are standard and determined by the order of the matrix [103],
and l is the dimension of its invariant subspace; we will see a detailed example of this in
Section 5. The only ambiguity is left in the choice of the upper-right entries, which must be
analyzed on a case-by-case basis.

     Since the canonical form (3.11) is achieved by conjugation in SL(k, Z), it is not very useful
when  is non-abelian -- there may not exist a similarity transformation that simultaneously
puts all D in the form (3.11). However, when  is abelian, and in particular, when  = Zn
has a single generator, (3.11) can be used to produce a complete classification of RFM's (see
[95, 104]). In the remainder of this paper, we will focus solely on this case--Riemann-flat
manifolds of cyclic holonomy--as they are significantly easier to study and provide a nice
entry point to the RFM landscape. However, we hope to return to the more interesting case
of non-cyclic RFM's in the future.

     In the same way that we have just classified the possible D's, it is also possible to classify
the vectors b associated to them. For a given D, the affine change of basis z  U z + u
(with inverse U-1 z - U-1u) acts on the transformation as

D z + b  U � D � U-1 z - U � D � U-1u + Ub + u .                       (3.12)

If we require that D remains invariant, for instance for U = Dq for some integer q, the
above becomes a transformation of the vector b,

b  Dq b + (I - D)u = Dq b + u ,                                        (3.13)

where u is the projection of any integer vector onto the subspace orthogonal to the invariant
subspace of D. In other words, we are free to rotate the transverse component of b by any

power of D and shift it by the transverse projection of any vector. The set of equivalence
classes of b vectors is the set of solutions of the equation

   b = D b mod u ,                                                     (3.14)

where u is the lattice generated by all the u, and we take into account that the vectors

            � 17 �
b satisfy pb  Zk, where p is the order of . In many cases, there is just one equivalence
class, and we can set b = 0, but not always, as we will see in Section 5.

     Another point of physical interest to us is to determine how many geometric moduli the

RFM has. These are by definition deformations of the ambient metric G that preserve the

Riemann-flat condition. Even in absence of supersymmetry, they correspond to classically
massless scalars, that may be lifted by classical or quantum corrections. The torus T k has

                k(k + 1)               (3.15)
                    2

geometric moduli, including its overall volume. The additional quotient by  has the appealing
effect of projecting some of those. This is because the invariant metrics G satisfy the condition

                DT � G � D = G ,  D ,  (3.16)

which freeze some of the T k moduli to specific values. For instance, in the case of the Klein

bottle discussed above, the complex structure of the covering T 2 is forced to have Re( ) = 0

or 1/2. To find the dimension of the moduli space and the perturbations explicitly, we simply

perturb the metric G in (3.16) by a small symmetric perturbation G. Invariance leads to a

linear system,

                G � D = (DT )-1 � G .  (3.17)

From (3.17), we see that the volume is never frozen by the RFM, and that any invariant vector
v under D will lead to an invariant deformation G  v  v. Since, as explained around
equation (3.7), D always has a non-trivial invariant subspace, an RFM always has at least
two geometric moduli [105]7. All the frozen T k moduli are absent at very low energies, but
since their higher KK modes are not projected out, in some sense they should be regarded
as having attained masses of order the Kaluza-Klein scale. This will be relevant in Section 5,
where we study the backreaction of an RFM compactification.

     Determining the full KK spectrum for fields of any spin in an RFM is a relatively easy
(if cumbersome) task, since fields on an RFM Fk can be described equivariantly as those
field modes on the covering T k invariant under the  action. Thus, it suffices to determine
the KK spectrum of the T k, and project down to the subspace invariant under . For the
particular case of zero modes of p-form fields, this can be done efficiently by algebraic methods.
Interestingly, there are examples of non-isomorphic RFM's with identical KK spectrum for
scalar fields [107] and p-forms [108], which provide a negative answer to the famous question
of whether one can "hear the shape of a drum" in higher dimensions.

     The final topic we need to review in this section about generalities of RFM's is their spin
structures. We will be considering compactifications of supergravity theories on RFM's, and
therefore, we must choose boundary conditions for fermionic as well as bosonic fields. Along
a non-trivial 1-cycle, fermions can be either periodic or antiperiodic, and such a choice is

7There are (non-cyclic) examples where this lower bound is saturated, as will be described in [106].

                � 18 �
called a spin structure. Not every manifold admits a spin structure and, interestingly, there

are examples of non-spin RFM's in dimensions 4 and above [109, 110], so we must be careful

to choose RFM's that do. While the classification of spin structures for general RFM's is

a convoluted topic [111], it is possible to provide a concrete characterization for manifolds

of cyclic holonomy [112]. In this paper, we will focus on a subclass of RFM's with cyclic

holonomy where

                                Fk = T l-1 � T k-l+1 � S1                                (3.18)
                                                          Zn

and the group B is generated by a single element Dg z + bg, where the last circle factor in
(3.18) is in the invariant subspace of Dg. Such manifolds are called mapping tori, and they
are featured prominently in topology and the study of global anomalies [113, 114]. A mapping
torus can be regarded as a cylinder T k-l+1 � [0, 1] where the two ends of the cylinder are
identified with a certain diffeomorphism of the T k-l+1 fiber. A mapping torus admits a spin

structure if and only if there are spinors in the torus cover invariant under the quotienting
action or, equivalently, if the gluing diffeomorphism preserves the spin structure of the T k-l+1

fiber.
     On the torus T k, a spin structure can be specified by the periodicity of spinor fields (z)

under lattice transformations,

                                (z + n) = e2ih�n (z) .                                   (3.19)

The diffeomorphism Dg acts on spinor fields of T k-l+1 as

                                (z)  Dg(Dg z ),                                          (3.20)

where Dg is one of the two spin lifts of Dg (related by a sign). Using (3.19), we get that

                Dg(Dg (z + n)) = e2ih�Dgn Dg(Dg z) ,                                     (3.21)

so to preserve the spin structure, the vector h must satisfy the consistency condition8

                                (DgT - I) � h  Zk-l+1 .                                  (3.22)

On top of this, there is one more condition, related to the component hS1 of the vector h
along the base. Suppose Dg is of order p. Then, acting with the generator p times yields

    8This can also be derived directly from the condition (4.14) that one-dimensional projective representations
of any group (such as spinors) represent elements in the same conjugacy class by the same phase. Consider
a one-dimensional representation of B where translations by n are represented as e2i h�n. The conjugation
b Tk b- 1, where Tk is translation by k corresponds to a pure translation, since

                                             Dg(Dg-1z - D-g 1bg + k) + bg = z + Dg � k .

Demanding that the phase representing the above is independent of b amounts to (3.22).

                                � 19 �
a translation along the vector pbg, which therefore must be in the lattice Zk. On the other
hand, in the spin representation the chosen spin lift satisfies Dgp = (-1)sg I, i.e. it is the
identity up to a sign. Therefore, the choice of spin structure on the covering T k along the

direction pbg is correlated with the choice of spin lift, and we must have

sg  2 p h � bg mod 2Z .  (3.23)

Note that for even order groups , we have sg = 0 regardless of the choice of spin lift,
constraining the vector h directly. Since due to (3.7) the vector bg necessarily has a component
along the direction of hS1, equation (3.23) correlates the spin structures on the base and fiber
of the covering torus. The combined system of equations given by (3.22) and (3.23) always
has a solution, which correlates with the fact that all cyclic, mapping tori RFM's admit a spin
structure [112]. Finally, the conditions (3.22) and (3.23) can also be derived by demanding
that the Casimir energy of fermionic fields as will be computed in Section 4 is a well-defined
function on the RFM.

     The techniques reviewed in this section allow one to determine the classical low-energy
EFT that arises from dimensional reduction on any RFM. We are now ready to tackle the
main point of this paper--the calculation of quantum effects (Casimir energies) in an RFM.

4 Casimir energy in RFM's

We now explain the central theme of this paper, which is the derivation of an explicit formula
to compute Casimir energies in RFM's. The general features of Casimir energies were already
discussed in Section 2. Here we will zoom in on the simpler case of free fields and the method
of images to compute the Casimir energy for free fields in quotient spaces; finally, we will
particularize this general result to the case of RFM's. There are many references for the
methods we will use here, including [35, 36, 38].

4.1 Casimir energy of massless free fields

As discussed in Section 2, absent any symmetries, there is no general expression for the
Casimir stress-energy tensor T�M. However, for the particular case of free fields, a concrete
answer may be obtained by the method of point-splitting regularization [38]. Free fields are
directly relevant to compactifications of ten-dimensional strings or M-theory, since the 10 or
11d low-energy supergravities are all free at energies much below the string or Planck scales.
For this reason, although a generalization to massive fields is not complicated (see [36, 38]),
we will focus on Casimir energies of massless fields only. The contributions of these fields
always dominate the Casimir energy in the limit of very large compatification manifolds. In
this subsection and the following we provide explicit expressions for T� and ^, in the case
of a massless, free field  of arbitrary spin s  2. Since the discussion at this level will be
formal, we omit Lorentz and internal symmetry indices;  could represent a scalar, spinor,
Rarita-Schwinger field, or vector. All such free fields are described by quadratic actions, of

� 20 �
the schematic form                         1

                      S = -g L =           2       -g  � D �  = 0 ,        (4.1)
                                                                           (4.2)
leading to an equation of motion

                                           D = 0 .

Here, D is an appropriate linear differential operator of order at most two, which also couples

to the background metric and gauge fields. Standard examples are the covariant derivative for

vector or scalar fields, the Dirac or Rarita-Schwinger operators for fermions, and the Fierz-

Pauli Lagrangian for spin two fields. From (4.1), the stress-energy tensor can be computed,

as                            -2 S                  D 1

                      T�             g�    =  �    g� - 2 g� D  .          (4.3)
                                -g

The crucial feature of (4.3) is that, for a free theory, T� is quadratic in the field  and its

derivatives and, therefore, its expectation value is directly related to the differential operator

in (4.3) acting on the two-point function. As usual in QFT, the na�ive evaluation of T�

in terms of (x)(x) produces divergences due to the contact singularity on the two-point

function. The idea of the point-splitting method is to regularize this by separating the two

points in the propagator slightly, and then taking the limit as the separation vanishes. This

leads to a regularized expression for the stress-energy tensor at any point x in the manifold,

as                                         D 1

                      T� (x)      =  lim   g� - 2 g� D  (x) (y)            (4.4)

                                     yx

where the derivatives in D are taken with respect to either x, y, or a combination of both--

these only correspond to different choices of regularization scheme. The regularization (4.4)

works for any free field, of any spin. As an example, for a masssless, free scalar field, with

stress-energy tensor

                      T�sc    =   1  (2�         -  g�  ) ,                (4.5)
                                  2

the point-splitting formula (4.4) becomes

                    T�sc    1        � + �  - g�                G(x, y) ,  (4.6)
                              lim

                            2 xy

in terms of the scalar Green's function G(x, y). As we will see in the next subsection, UV di-
vergences will cancel automatically in certain spaces when using this regularization, including
the ones of interest. To compute the components of the stress-energy tensor along the internal
dimensions, one needs to evaluate (4.4) for all massless fields of any spin in the theory under
consideration. However, if one is only interested in the components along the non-compact
directions--in other words, the value of the Casimir energy ^--as we are in this paper, then
a small trick allows us to treat all fields of any spin simultaneously, using only (4.6). To do
this, we will momentarily compactify all spatial directions on a torus of side L and compute
T00. When one does this, the Lorentz symmetry of the theory is broken completely, there is

                                           � 21 �
no spin since there is no Lorentz group in zero dimensions, and the operator Dab can be di-
agonalized into a basis of internal polarizations. From this point of view, all that remains are
scalar fields. The (0+1)-dimensional Lagrangian therefore becomes a sum of free fields, with
g (the number of physical degrees of freedom of the field ) copies of a free scalar for bosonic
fields in higher dimensions, or a sum of free fermions for fermionic fields. Since fermion and
boson contributions only differ by a sign, the Casimir energy can then be computed as

^ = -T00 = -                                 (-1)F T0s0c ,  (4.7)

                              Polarizations

where T�sc is the expectation value of the stress-energy for a scalar field, and the contribution
is positive for bosonic fields while negative for fermionic fields. Finally, nothing in (4.7)
depends on L (save for a trivial volume factor), so we can take L   and still use the
formula (4.7).

     The Casimir energy of arbitrary spin fields is then computed using (4.6); as we will see
in the next subsection, UV divergences will cancel automatically in certain spaces when using
this regularization, including the ones of interest, yielding a completely finite result. There is
just one important caveat: the formula (4.6) depends on a scalar propagator G(x, y), but in
general this is not unique. Although we have managed to reduce the calculation of Casimir
energy of an arbitrary spin field to a sum of scalar fields corresponding to the different
polarizations, each polarization may transform differently under the Lorentz symmetry of
the ten-dimensional theory, and therefore involve a different scalar field propagator (i.e. the
propagator of a scalar field with twisted boundary conditions along the cycles of the covering
torus). The source of the ambiguity lies in the fact that the covariant derivative  seen by
each polarization may be coupled to an additional background connection, for an internal or
spacetime symmetry, and thus different polarizations are affected differently. We will see an
example of this in the next subsection.

4.2 Free fields in a quotient space: the method of images

Armed with a way to regularize and compute ^, we now focus our attention on the computa-

tion where Nk is of the form         N~k ,
                                     B
                              Nk  =                         (4.8)

and where B is a group of isometries of the manifold N~k9, which we assume to act freely
(so that there are no fixed points and Nk is indeed a manifold). The particular case of
the Riemann-flat manifolds studied in Section 3 has N~k = Rk, and will be the subject of
Subsection 4.3; here, we explain how to compute the propagator and hence free energy for

a general manifold of the form (4.8). There is a technique to compute the propagator of a
scalar field on Nk, given one on N~k which is B-symmetric, known as the method of images

    9This can be generalized to the case where B includes internal symmetries by including the transformation
law for each charged field, but we will not study these cases in this paper.

                              � 22 �
[115]. Since the underlying equation of motion is linear, one can construct a single-valued

propagator on Nk by starting with a propagator GN~k (x, y) on the covering space and summing
over the images of any point under the group B,

             GNk (x, y) = GN~k (x, b(y)) .                             (4.9)

                                    bB

The resulting expression is manifestly single-valued as a function of y, and also as a function

of x, since

             GNk (b(x), y) = GN~k (b(x), b(y)) = GN~k (x, b-1  b(y)),  (4.10)

             bB                       bB

where we have used that the parent propagator GN~k (x, y) respects the isometry group B.
     The method of images combines very nicely with the point-splitting regularization of

the previous subsection, since the y  x divergence of the two-point function in the sum

(4.9) comes entirely from the contribution where b is the identity in the sum over B. This
contribution is, in turn, identical to the original propagator on the covering space N~k, and does
not see the B quotient at all. As such, this term of the sum in (4.10) (or in the corresponding

sum in (4.6)) inherits any properties that the propagator or Casimir energy might have on
N~k. For instance, if the physical theory is supersymmetric, and the background N~k preserves
supersymmetries, such that there is a Bose-Fermi cancellation on N~k, such cancellation will
also happen in the identity term of (4.10). But since all divergencies in (4.6) come from

this term alone, we reach the conclusion that the Casimir energy (4.7) of a supersymmetric
theory on Nk will be manifestly UV-finite whenever N~k preserves supersymmetry, even if no
supercharges are preserved by Nk. One could perhaps say that the supersymmetries of N~k live
on Nk as some form of "non-invertible" supersymmetry [116], an idea that deserves further
exploration.

     We also note in passing that, even on a general Nk not of the form (4.8), some universal di-
vergences are expected to cancel in the Casimir energy formula (4.7)--for instance, those that

correspond to a higher-dimensional cosmological constant (which in the point-splitting regu-

larization correspond to the ultralocal limit where one replaces the compactification manifold
by RD)--but in general, we do expect to have divergences in the one-loop Casimir energy, as-
sociated to unprotected counterterms of the higher-dimensional theory that might contribute

to the lower-dimensional vacuum energy. See [117] for a more detailed exposition. The pro-

tection due to the quotient, however, is much stronger, in particular for the case of RFM's,
where N~k is maximally supersymmetric flat space.

     At any rate, once we remove the divergent identity contribution, the propagator is finite,

             GrNekn.(x, y) =         GN~k (x, b(y)) ,                  (4.11)

                              b= IB

corresponding to a finite expression for the vacuum energy via (4.7).
     The regularized propagator (4.11) is not the only one that can be constructed via the

                              � 23 �
method of images. For instance, if  is a complex scalar field (as the polarizations of a
higher-dimensional field would be), any expression of the form

GNrekn,.(x, y) =                   ei(b)GN~k (x, b(y)) ,                      (4.12)

                          b=Id.B

where ei(b) is a one-dimensional representation of B, is a valid propagator on Nk.10 However,
the resulting expression GNrekn,.(x, y) is in general not a well-defined function on Nk, as the
phases spoil the proof of invariance in equation (4.10). Rather, it becomes the appropriate

expression for a propagator of a field  which is a section of a non-trivial line bundle over

Nk. When studying spinning fields as described in the previous subsection, we could decom-
pose them into different polarizations, each described by a complex scalar field which will

transform in non-trivial line bundles over Nk; the associated phases will be an example of the
phenomenon, discussed in Subsection 4.1, that different polarizations may involve different

propagators.

     Even though (4.12) is not a single-valued function on Nk, the Casimir energy that we
derive from it should be. As we will see below, the Casimir energy is obtained after taking
two derivatives of GNrekn,.(x, x), so this function should be single-valued as a function of x. For
any b0  B,

GrNekn,.(b0(x), b0(x)) =           ei(b)GN~k (b0(x), b  b0(y))

                          b=Id.B

=                                  ei(b)GN~k (x, b-0 1  b  b0(y)) ,           (4.13)

                          b= Id.B

so the Casimir energy will be single-valued if                                (4.14)
                                       ei(b-0 1 b  b0(y)) = ei(b) , b0 , b .

This condition, which is automatically true for any one-dimensional representation of B, tells
us more generally that the most general shift in the propagator must be given by a one-
dimensional function of conjugacy classes � a character� of B. We will see momentarily that
this is indeed the case, even when the representation under B is not one-dimensional.

     Another, equivalent, point of view comes from generalizing (4.11) to fields transforming
in higher-dimensional representations of B. Since B is a subgroup of isometries, the trans-
formation properties of a field a are induced by its d-dimensional transformation properties
under the Lorentz group. This generalizes (4.12) to

GNrekn,. ab(x, y) =                Rca(b) GNc~bk (x, b(y)) ,                  (4.15)

                          b= IB

where Rca(b) is a higher-dimensional representation of B. When using the formula for the

  10For  real, this phase is at most a sign.

                          � 24 �
Casimir energy (4.7), the sums over polarizations should be replaced by traces over the

matrices Rca(b)--in both cases, the resulting expressions are equivalent, and we learn that we
need to include traces of the matrices Rca when inserting (4.15) into (4.7).

     Finally, we will be interested in some cases where the group B acts on the fields only

projectively. In this paper, where all concrete examples will involve purely geometric actions,

this will only be the case for fermionic fields, and the projectivity corresponds to the familiar

fact that spinors represent a 2 rotation as multiplication by -1. In cases like this, all the

results of this paper are still valid, and we can use an expression such as (4.15), but with the
group B replaced by a central extension B^ (which is represented linearly), fitting into a short

exact sequence

                1 - Z - B^ - B - 1 .                            (4.16)

The group Z in the extension will be Z2 in the examples considered in this paper (correspond-
ing to the fact that Spin is a Z2 extension of SO), but in general it can be more convoluted11.

4.3 Casimir energy formula for RFM's

We are now ready to explain how to compute the Casimir energy for RFM's, which will be
the main technical result of this paper. More concretely, we wish to compute the quantity ^
and its integral for the RFM's described in Section 3, using the method of images outlined in
the previous subsection. We denote a point in Rk (the universal cover of the k-dimensional
RFM Fk) as a k-dimensional vector z. Points in Fk will then be equivalence classes of these
under B. Consider a field , which transforms under B as

                a(z)  Rca(b) c(b(z)) = Rca(b) c(D z + b + n) ,  (4.17)

where we have used the decomposition (3.2) and the fact that isometries of Rk act linearly.
Using (4.15) together with (4.6), and plugging it into (4.7), one obtains a sum over images of
derivatives of flat-space propagators,

                              D                 Tr(R)           (4.18)
                ^(z) = -      2       |z - (D z + b + n)|D ,

                2D/2

                                 nZk

where we have replaced the sum over B by a sum over the lattice  = Zk and the group
 defined in Section 3. The tilde over the sum means that the identity in B is excluded
from the sum (although, for a supersymmetric theory, we can put it back in and it will not
make a difference, as explained in Subsection 4.2). The trace Tr(R) replaces the sum over
polarizations in (4.7); it is the same sum, written in a basis-independent way as explained
near the end of Subsection 4.2. An important point is that since Casimir energy is a sum
over physical degrees of freedom, the matrices R = Rca are in Lorentzian signature--they
represent elements of the group SO(D - 1, 1). This automatically takes into account a proper

11For instance, for type IIB compactifications, it could involve subgroups of the SL(2, Z) duality group [118].

                                 � 25 �
counting of physical polarizations for any field, since under the decomposition

SO(D - 1, 1)  SO(D - k - 1, 1) � SO(k)                                           (4.19)

the D-dimensional field a decomposes into representations,

rSO(D-1,1)              riSO(D-k-1,1)  ~riSO(k) ,                                (4.20)

                  i

and since B only ever involves an action in a subgroup of the SO(k) factor, the trace can be
grouped in terms of the corresponding (D - k)�dimensional irreps, as

Tr = rSO(D-1,1)         g Tr riSO(D-k-1,1) ~riSO(k)                              (4.21)

                     i

where again gr is the number of physical polarizations of a (D - k)�dimensional massless field
in representation r of the lower-dimensional Lorentz group (for instance, a four-dimensional
massless vector has only two polarizations and so on). Alternatively, since there are only
massless fields in higher dimensions, we can work with the massless little group of the D-
dimensional theory, which is SO(D - 2). Since we will focus on M-theory compactifications,
for the concrete examples in Sections 5 and 6 we will have to evaluate these traces for the
11-dimensional supergravity fields--graviton, gravitino, and 3-form. Details on how to do
this can be found in Appendix F.

     Equation (4.17) admits further simplification. The matrix R representing a pure trans-
lation must be proportional to the identity, since translations are a central element in B and
we are allowing for a projective representation. Bloch's theorem [96] tells us that the most
general such representation is of the form

              Tn  e2ih�n � I ,                                                   (4.22)

where Tn is a translation by integer vector n and h is a vector defining the representation.
As mentioned at the end of Subsection 4.2, in this paper projective representations will only

appear for fermions, via the spin lift of SO elements in B. As a result, the phase must be
a sign, and the vectors h must have all integer or half-integer coordinates; in fact, h is the
vector that quantifies spin structures in the RFM (or its covering T k) introduced in Section 3.

     Using this, we can finally recast (4.18) as

^(z)  =  -    D              Trr(D ) e2ih�n                 .                    (4.23)
              2             - (D z + b + n)|D

            2D/2        |z

                  nZk

This is a concrete, UV-finite expression for ^(z) for a given free field in a representation r. It
takes the form of an explicit lattice sum over Zk, together with a sum over the finite group .

                     � 26 �
The phase factors e2ih�n account for the presence of non-trivial spin structures for fermionic
fields (or, more generally, for non-trivial bundles for discrete symmetries on T k). Finally,
there is an overall (-) sign if the field is fermionic. As advertised in the previous subsection,
the formula is finite, and UV-finite for a supersymmetric theory. In fact, at one loop, this is a
property of the spectrum only, so any theory for which the number of bosonic and fermionic
degrees of freedom match in D dimensions would yield a finite one-loop Casimir energy when
compactified on Riemann-flat manifolds, even if it was non-supersymmetric.

     Although we have derived an explicit formula for ^, we are more interested in its integral
over the compact manifold Fk; only after integration will we obtain the effective potential
in (D - k) dimensions that can be used to search for dS maxima, as in Section 5. This will
be the subject of the next subsection, but we finish this one by noticing that the explicit
expression for ^, as well as the implicit expressions for all components of the stress-energy
tensor that we obtained in Subsection 4.1, provide us with a fully explicit, D-dimensional
result for the Casimir stress-energy tensor, which can be used as a starting point in any
detailed study of backreaction and control issues in these solutions. That such an explicit
D-dimensional backreaction is available means that including higher-order corrections in this
analysis is a matter of calculation, and no ambiguities (e.g. due to subtleties in field profiles
around localized sources, as in [46�48]) can arise. We hope to return to this exciting but
probably grueling question in the future.

4.4 Explict formula for RFM Casimir energy & "Casimir branes"

The lower-dimensional Casimir energy (the effective potential coming from the Casimir term)
is given by an integral of ^(z) in (4.23) over the compact space Fk. In other words, we have

VCas =      dkz       ^(z)  =  -  (s)   1               dkz       |z   Trr(D ) e2ih�n    .  (4.24)
                   G              2s   ||                      G      - (D z + b + n)|D

        Fk                                      [0,1]k

                                           nZk

Here, we have replaced the integral over the manifold Fk by an integral over the covering torus
T k = Rk/Zk (so that the fundamental domain over which we integrate is [0, 1)k), equipped

with a general metric Gij. The factor of 1/||, where || is the order of the finite group  of

Section 3, accounts for the fact that the torus is covering Fk a total of || times. The sum is
taken over all    and n  Zk such that the denominator does not vanish, as indicated by
the  over it. In other words, the sum excludes the term for which |z - f(z) + n|2 = 0. Due

to the fixed-point-freeness condition of the group B, such a divergence only happens for  = I,
n = 0. The vector h encodes twisted boundary conditions of various fields, that transform as
a phase under translations, as described in the previous subsection12.

  12Whenever the vector h = 0, there is a covering torus T~k  T k on which the bundle specified by the
vector h is trivial, and hence we can take h = 0 on the covering torus. In other words, by passing to a central
extension of the group B, we can always take h = 0. As a concrete example of this, in the case of S1 with
antiperiodic boundary conditions, we have h = 1/2 on the S1 identified as x  x + L; but the boundary

condition is periodic under the transformation x  x + 2L, which defines a double cover circle.

                                           � 27 �
     The core problem in determining Casimir energies in Riemann-flat manifolds is then the
evaluation of sum-integrals of the form

                  (s) 1                                      dV  e2ih�n                ,  (4.25)
                  E()  - 2s ||
                                                       [0,1]k    |(I - D)z + b + n|2s
                                                  nZk

where the lattice is taken to be Zk with inner product given by Gijninj, we have introduced
s  D/2, and the induced volume element is

                                                                                          (4.26)
                               dV = G dz1  . . .  dzk .

We can then rewrite (4.24) as

                               VCas =                  Trr(D) E() .                       (4.27)

                                       r 

Each E() therefore corresponds to the contribution of a given "twisted sector"13, where the

propagators are shifted from those in flat space. The case of flat space,  = I, corresponds

exactly to the Casimir energy of the covering torus. Notice also that this is the only term

where there is a divergence, for n = 0; in other words, for  = I, the sum over n in (4.25) has

no restrictions.

The basic technical challenge that we solve in this paper is to evaluate the sum-integral

(4.25) in full generality. In this subsection, we will explain how to perform the integral in

(4.25), producing an explicit result in terms of an infinite sum, and discuss the physical

interpretation of the result. Subsection 4.6 then outlines an efficient way to evaluate this sum

numerically.

Since evaluating the integral in (4.25) is a cornerstone for the results of this paper, and

we need to be sure of its validity, we have done it in three independent ways. We now present

the most straightforward derivation, based on Mellin transform techniques, and relegate the

other two cross-checks (one from an explicit evaluation of the integral and the other from the

expressions developed in Section 4.6) to Appendix E.

To evaluate the z integral in the expression for E(), we will use the so-called Mellin

transform14 [94]                                        

                                             1             dt ts-1f ,                     (4.28)
                               Ms[f ]  (s)
                                                       0

  13Not to be confused with the usual worldsheet twisted sectors that arise in perturbative string orbifolds.
An RFM is a free orbifold and therefore all worldsheet twisted sectors are very massive (consisting entirely of
winding states) in any perturbative string construction involving them.

  14The Mellin transform, and more generally Mellin space, takes a fundamental role in conformal field theories,
the AdS/CFT correspondence and QFT in AdS, see e.g. [119�123]. Mellin space is analogous to Fourier space,
except scale invariance now takes the role that belongs to translation symmetry in the more familiar Fourier
case.

                                                       � 28 �
and in particular the identity

     1                                  1                                                        (4.29)
                                   =
|(I - D) z - b + n|2s (s) 0                                dt ts-1e-|(I-D ) z-b +n|2t.

This implies that our sum is simply the Mellin transform of a sum of exponential terms of
the form e-|(I-D) z-b+n|2t. After permuting integrals and sums, we get

                                                     dkz           e-|(I-D )z+b +n|2t+2i h�n .   (4.30)
            (s) G 1
E() = - 2s � || (s)                 dt ts-1  [0,1]k          nZk

                                0

We then complete the square,

-|n +  |2t + 2i h � n = -(n +  )T (t G)(n +  ) + 2i h � n

                                = -(n +  - i G-1h)T (t G)(n +  - i G-1h)
                                                     t                               t

                                - 2i  � h - 2hT G-1h ,                                           (4.31)
                                                  t                                              (4.32)

with  = (I - D)z + b, so that the sum can be written as

     e-| +n|2t+2i h�n           =  e-2i       �h-    2   hT  G-1h       e-|n+ -  i   G-1h|2t  .
                                                      t                           t

nZk                                                                nZk

Now consider the general form of Poisson resummation [124],

                                   f (n) = F[f ](q) ,                                            (4.33)
                                                                                                 (4.34)
                                n              q

where F[f ] is the Fourier transform of f and  the lattice dual to ,

          {q  Rk | n � q  Z , n  } ,

together with the following property of multidimensional Fourier transforms [125]

     F [f (Az + b)]() = e2ib�(A-1)T  F [f (z)]((AT )-1) .                                        (4.35)
                                 | det A |

Since the metric G can always be written as a Graham matrix G = MT M (simply by finding
an orthonormal basis), we have that


                                vT (t G)v = ( t Mv)T ( t Mv) ,                                   (4.36)

                                             � 29 �
so that we may write

                          M)(n         +  ))]()        =       e2i �q                                                        (4.37)
                F[f (( t                                                         � F [f (n)](( t MT )-1q) ,
                                                           | det t M |

with    =    -  i  G-1h.     The    Fourier    transform            is  then
                t

                                                              k
                                                           2                                           2  qT  G-1 q
                F  e-|n+ -      i   G-1h|2  t  =                        �  e2i( -  i   G-1h)�q  �  e-         t              (4.38)
                                 t                                                  t                                        (4.39)
                                                       k
                                                    t 2 | det M |

                                                           k
                                                    2                   2
                                               = k               �  e-   t  (qT  G-1q-2 G-1h�q)    �  e2i   �q  .

                                                    t2 G

The space coordinate z now only appears in the simple exponential term e2i �q, and thus the
spatial integrals over z can be performed directly, term by term. We can then write (4.30) as

                             k                 ts-  k  -1
           (s) G  2                                 2
E() = - 2s � || (s)                      dt                      e-  2     (q-h)T  G-1(q-h)+2ib �(q-h)          �  Ik (D ),  (4.40)
                                                                      t

                                    0               G qZk

where we have introduced the integral

        Ik(D) =              dkz e2i [(I-D )z]�(q-h) =                           dkz e2i z�[(I-D )T �(q-h)] .                (4.41)

                     [0,1]k                                              [0,1]k

The result of all these steps is now clear: the integral over the compact space (more precisely,
over the covering torus T k) can be performed explicitly,

                                                       k e2i [(I-D )T �(q-h)]j - 1
                                    Ik(D) =                                            .                                     (4.42)
                                                           [(I - D)T � (q - h)]j
                                                      j=1

Recalling the consistency condition (3.22), namely that

                                               (I - D)T � h  Zk ,                                                            (4.43)

which limits the possible choices of h compatible with a consistent spin structure, that q  Zk
and that D  GL(k, Z), we conclude that the components [(I - D)T � (q - h)]j are always
integers. Consequently, each factor in this product is only non-zero if [(I-D)T �(q -h)]j = 0,

in which case it simply gives 1,

                                                           k

                                       Ik(D) =                 0,[(I-D )T �(q-h)]j .                                         (4.44)

                                                          j=1

In other words, the integral is only non-vanishing along the invariant subpace of DT defined

                                                              � 30 �
by

                                        (I - D)T (q - h) = 0.                                     (4.45)

A solution to this equation takes the form q =  + , where  is a generic vector of the
sublattice  defined as the intersection of Zk with the invariant subspace of DT , and   Zk
is any integer vector that satisfies

                                   (I - D)T  = (I - D)Th .                                        (4.46)

Note that there might not be a solution to this equation; in particular, one cannot generically
choose h itself since its components may be half-integers. Whenever no solution for   Zk

exists, the sum vanishes identically--we will keep track of this condition by including in the
final result a factor ^h which evaluates to 1 if a solution exists and to 0 otherwise. The factor
^h is related to a field theory version of Atkin-Lehner symmetry [50�52]; we elaborate on this
in Subsection 4.5. In any case, after imposing (4.46) the sum over q  Zk is thus restricted
to a sum over   ,

                                k          ts-  k  -1             2
                   (s)      G 2                 2                  t
    E ( )  =  -^h  2s   �  || (s)       dt                    e-      (-)T  G- 1(-)+2ib  �(-)  ,  (4.47)

                                   0            G


where   h -     Q. In effect, the Casimir sum collapses into a sum over the invariant
subspace of DT , which has dimension k  k. Notice that the invariant subspace is never
empty, since otherwise the corresponding element    would have fixed points, as explained

in Section 3. Finally, the inner products are now restricted onto this invariant subspace, with
induced metric G and norm | � |. The vector b is the projection of b onto this same
subspace.

     Continuing with our derivation, at this stage, one can perform Poisson resummation back
to position space from this reduced sum over the k-dimensional lattice ,

                                   k-k                            G
                      (s)      G 2
    E ( )     =  -^h  2s   �  || (s)         dt    ts-  k-k   -1            e-|+b |2t+2i � .      (4.48)
                                                           2

                                        0                             G 

obtaining a sum over a lattice , dual to . Since

                                      (DT ) �  =  � (D ),                                         (4.49)

the dual lattice  is naturally identified with those vectors in the invariant subspace of D
which have integer inner products with every   ,

                       = ()  {  Rk |  �   Z, D =  ,   } ,                                         (4.50)

where the � denotes the standard pairing between a space and its dual. We will now show

                                                 � 31 �
that  as defined above can be identified with the orthogonal projection of the defining lattice

Zk onto the invariant subspace of D with respect to the Gij inner product. To show this,

notice that, since  is a primitive sublattice of Zk (as it is defined by a linear equation),

there is a basis {i}, i = 1, . . . k of Zk where the k first vectors form a basis of  (see e.g.
[126]). Consider the corresponding dual basis {i}. The first k vectors of this basis satisfy
i � j = ij, and therefore satisfy all conditions to be a basis of  in (4.50), except for the
fact that they might not lie on the invariant subspace of D. However, any vector  can be

decomposed as

                                                =  + Inv,                                             (4.51)

where Inv is the orthogonal projection onto the invariant subspace and  is orthogonal to

it. Since

                                                �  =  � Inv                                           (4.52)

for any   , we may replace the vectors  by their orthogonal projection to construct a
basis, and thus  is indeed the projection of Zk onto the invariant subspace of D.

     Finally, performing the Mellin transform in (4.48), we find

       VCas =             Trr(D) E() ,    E ( )     =  -^h  (s )    �   G           e2i  �    ,       (4.53)
                                                            2s         ||          | + b |2s
                  r                                                            

where  s   =  s-  k-k  ,  the  lattice    and  the  vector   ,  as  well  as  the  projected  metric  G  and
                    2

inner product | � |, depend on the element   .

Equation (4.53) is the final expression we were looking for. The lower-dimensional Casimir

energy is expressed as an infinite sum, with no integrals left, where each    gives a definite

contribution E(). Notice that for the identity element in , the invariant subspace is the full

lattice Zk and the sum stays k-dimensional.

The fact that  is just the invariant lattice of D allows for a nice physical interpretation

of our final result for E() (4.53). This expression is a lattice sum just like the one that would

be used to compute Casimir energies on a torus, only that it is localized on the invariant

subspace of D. Since the volume element of this subspace is precisely G, we find that
E() behaves exactly as the contribution to the effective potential that would come from an

effective k-dimensional "Casimir brane" wrapped on the invariant subspace of D, of tension

given by (4.53). In fact, already from (4.25), before performing the z integral, we can tell

that the region of highest energy density in E() comes from the invariant subspaces, which is

where the denominator becomes largest. What (4.53) tells us is that this qualitative feature

survives a detailed treatment of the problem.

The usefulness of the Casimir brane picture is that the total Casimir energy can be un-

derstood as a sum over contributions corresponding to different effective "Casimir branes"

wrapped on different submanifolds of the RFM. For instance, the D = I contribution cor-

responds to a space-filling Casimir brane; a D with a one-dimensional invariant subspace

                                                    � 32 �
corresponds to a (d + 1)-dimensional Casimir brane; and so on (see Figure 2 for an explicit
example). This allows much of the intuition that one has from D-brane model building to be
imported to settings with Casimir energies--in particular, it provides a D-dimensional pic-
ture of the backreaction in the internal space--although one must keep in mind that (unlike
ordinary D-branes and orientifolds) the tension of a Casimir brane depends on the precise
submanifold on which it is wrapped. In fact, its overal scalling is fixed by the size of the sub-
manifold it wraps. Furthermore, unlike D-branes, but just like orientifolds, Casimir branes
can have a negative tension, which is why they evade the no-go theorem of [34] and can
provide classical saddle points.

     A point of curiosity is the ^h factor. When it evaluates to zero, the Casimir energy
vanishes, but as we will see in examples below, in general this happens because there are
several Casimir branes whose tensions exactly cancel! Due to the symmetries of the problem,
one is forced to introduce localized objects of equal and opposite tension. This is reminiscent
of what happens in e.g. orientifold compactifications with 16 supercharges [127], but now
the phenomenon is happening at one-loop and in a non-supersymmetric context. In Section
4.5 we explain this vanishing via a spacetime version of Atkin-Lehner symmetry [50�52]. We
believe this warrants further study, since having a symmetry reason for the vanishing of (some
terms of) a one-loop Casimir energy by what looks like an extreme fine-tuning of the tension
of Casimir branes might give us a way to engineer anomalously small vacuum energies and
address aspects of the cosmological hierarchy problem.

     In this paper we will not rely heavily on the Casimir brane picture, but we believe it may
be a useful tool going forward. Furthermore, the fact that the RFM Casimir energy takes
the form of a sum of branes may suggest the existence of a dual picture where the Casimir
branes are identified with contributions of more standard branes or orientifolds wrapping
non-supersymmetric cycles. For the time being we will ignore these interesting questions and
finish this subsection describing the checks we performed to verify (4.53).

     On top of the three separate derivations for (4.53), provided here and in Appendix E, we
have also checked it numerically, by first performing the sum in (4.25) using the method of
Ewald summation described in Subsection 4.6 and then integrating over z numerically, for two
simple cases in two and three dimensions which we describe below. A direct numerical check
of the formula for higher dimensional sums quickly becomes prohibitive, since the evaluation
of the integrand takes longer time.

     The first example we study is the Klein bottle. This is the simplest 2-dimensional RFM
(k = 2), corresponding to the quotient T 2/Z2 with the Z2 group generated by

Dg =  -1 0                                      , bg =     0  .  (4.54)
      01
                                                           1

                                                           2

The most general metric on the Klein bottle is

      G = R2  x0                                        ,        (4.55)
              0 x-1

      � 33 �
             (a) T 2/Z2 (Klein bottle)                                                    (b) T 3/Z3

                            Figure 2. Casimir branes for Klein bottle and 3d RFM.

                                                                        z2

                                                                     fg

                                                          fg

                                            Dg                                fg

                                                                                                                  z1
                                                                            (1,0)

                                                     Dg

Figure 3. Lattice of the Klein bottle T 2/Z2, with invariant (up to T 2 identifications--blue, bold

arrow)  points   z1    {0,  1  }  corresponding  to  the  locations  of  the  Casimir     branes     (red,            bold).  Note  that
                            2

Casimir branes connect pairs of identified points that are the closest and therefore contribute the most

to the Casimir energy. For comparison we show a point that is not invariant under Dg and is thus
further apart from its images under fg(z) = Dg z + bg (green, dashed).

and the subspace left invariant by Dg is one-dimensional (k = 1),

        (I - Dg) z =              2z1  =! 0 mod Z2            =                   1                                             (4.56)
                                   0                                     z1       0,      , z2  [0, 1) .
                                                                                     2

This  gives  us  the   positions  of   the  Casimir  branes,      located     at  z1      {0,  1  }  and              wrapping  the  z2
                                                                                               2

direction (figure 2). Note that the conditions (3.22) and (3.23) force any consistent choice of

h to satisfy

                                       2h1  Z , sg = 2h2 mod 2Z .                                                               (4.57)

                                                          � 34 �
Hence we are free to choose any h1, which will fix a specific Pin+ lift15, i.e. Dg2 = (-1)2h2I.

We must take this into account when taking traces over fermionic representations. For this

element,  we    then  have  sg     =     s  -  1  ,  G      =  (R2 x-1)   and  g       =  h  -  g,    with  g  any    vector  in
                                               2

Z2 satisfying (4.46), which reads 21 = 2h1. We conclude that the contribution from Dg is

only non-vanishing if h1 = 0 mod Z, i.e. for untwisted boundary conditions around the z1

direction.

   The contribution from Dg is then

                (sg)       xsg  -  1           e2i h2                (sg)      xsg  -  1
                2sg                2                                 2sg               2
E  (g)  =    -        �                                        =  -         �             (22sg  - 1)(2sg)h2,0 .      (4.58)
                         2R2sg -1              |  +   1  |2sg                  R2sg -1
                                      Z               2

The fact that the invariant subspace is 1-dimensional allows us to obtain analytical results for

the Klein bottle. Moreover, we find that the Casimir energy vanishes whenever the boundary

condition around any of the two cycles is twisted, i.e. only for h = (0, 0) do we find non-

vanishing    Casimir  energy.      For      s  =  11  ,  which    would   be   appropriate       for  the  study  of  M-theory
                                                  2

on the Klein bottle, we have

                                                         1245 x9/2            40.2 x9/2
                                      E(g) = -                    R9  -                   .                           (4.59)
                                                    945                        R9

This result exactly matches the direct numerical integration of (4.25), which we also performed

separately. Plotting the integrand, we can explicitly see the regions where the Casimir energy

is localised, i.e.    the  Casimir          branes       located  at  z1       {0,  1  }  and  wrapping     the   z2  direction
                                                                                    2

(figure 2).

     In M-theory one must include the contributions of the graviton, 3-form and gravitino;
as we just argued, any choice of boundary conditions other than h = {0, 0} will result in a

vanishing contribution from Dg. Finally, we need the traces of Dg in these three represen-

tations to weigh the respective contributions in the sum (4.53). Following the discussion in
Appendix F with  = {�, 0, 0, 0}, we find

                         Tr44(Dg) = 16 , Tr84(Dg) = 0 , Tr128(Dg) = 0 ,                                               (4.60)

regardless of the choice of spin lift Dg. On the other hand, the identity term I contributes as

                                VC(Ia)s  =       (s)     �  128 x2s          1 - e2i h�n         .                    (4.61)
                                               - 2s         2R2s-2          |x2n12 + n22|2s
                                                                      n Z2

Due to the presence of x inside the sum, this term must be summed numerically. For com-

  15The Klein bottle is not an orientable space, and so it does not admit a spin structure. There is however a
non-orientable generalization of this, called "Pin" structures, that works the same in practice. There are two
kinds, Pin+ and Pin-, of which Pin+ is in some sense closest to an ordinary spin structure. Since we are just
giving this example for illuistrative purposes, we skip the subtletites associated to the construction of a Pin+
structure on the Klein bottle. See e.g. [128] for further information.

                                                               � 35 �
parison, when x = 1, these can be summed analytically to get

         VC(Ia)s = 0 , for h = (0, 0),                                                                                                  (4.62)
                                                                                                                                        (4.63)
         VC(Ia)s  =    (s)     �  128 x2s    � 4(s)[(s) - (s)]                           0.56         ,    for h =    1
                     - 2s         2R2s-2                                               - R9                            ,0 .

                                                                                                                      2

                                                                             z2

                                                                                     (1,1) (1,0)

                                                                   Dg

                                                                                                           z1

                                                Dg                               Dg

Figure 4. Lattice of the T 3/Z3 RFM at z3 = 0, with invariant (up to T 3 identifications--blue, bold

arrows)  points      (z1, z2)     {(0,  0),  (  1  ,  2  ),  (  2  ,  1  )}  corresponding        to  the  locations  of  the  Casimir  branes
                                                3     3         3     3

(red, filled points). Note that these are not fixed points since each action of Dg is acompanied by a

shift by bg along z3, not shown here (see figure 5).

Let us consider a second example, the Riemann-flat manifold T 3/Z3 with the Z3 group

generated by

                                                 0 -1 0                                     0                                           (4.64)
                                        Dg =  1 -1 0  ,                              bg =  0  .

                                                    001                                            1
                                                                                                   3

This manifold was used in [102] to construct new compactifications of string theory to seven

dimensions and sixteen supercharges involving discrete  angles. The most general metric on

this RFM is

                                                                 2 -1 0                                                                 (4.65)
                                                G = R2 x4/3 -1 2 0  ,

                                                                    0 0 x-2

and the subspace invariant under Dg is again 1-dimensional,

                                                     z1 + z2 
                                  (I - Dg) z =  -z1 + 2z2  =! 0 mod Z3

                                                             0

                                                                             � 36 �
Figure 5. Casimir branes on T 3/Z3 RFM corresponding to the points that remain invariant under
Dg (red, bold lines). Note that the Casimir branes connect the pairs of points identified by the Z3
symmetries that are the closest to each other and therefore contribute the most to the Casimir energy.

We show for comparison a point that is not invariant under Dg so that its image is further apart and
will thus contribute less to the Casimir energy (green, dotted line).

                         12 21                                    (4.66)
=  (z1, z2)     (0, 0),   ,           ,   ,       , z3  [0, 1) ,
                         33              33

which specifies the locations of the Casimir branes (see figures 2, 4, and 5).
     For the element Dg, we have sg = s - 1, G = (R2 x-2/3), and g = h - g, with g

any vector in Z3 satisfying (4.46). For the choices of h allowed by the consistency condition

(3.22), which forces h1, h2 = 0 mod Z, any vector g satisfies (4.46); in particular we can
choose g = 0. Finally, we must also have

                sg = 2h3 mod 2Z ,                                 (4.67)

so that a choice of h3 is tied to a choice of specific spin lift �Dg satisfying Dg3 = (-1)2h3I .
As before, we must take this into account when taking traces over fermionic representations.

     The contribution from Dg is then

   E (g)  =  -  (sg)  �       2sg -1     e2i h3         .         (4.68)
                2sg
                          x3          Z  |  +  1  |2sg
                         3R2sg -1              3

                         � 37 �
When h3 = 0, for untwisted boundary conditions, we find

                              (sg)           2sg -1                                                                                    8
                              2sg           x3                     1                          2
               E (g)   =   -            �  3R2sg -1          2sg, 3           +         2sg, 3                  221.4 x 3                      (4.69)
                                                                                                            - R8 .

As for the Klein bottle, having a 1-dimensional invariant subspace allows us to obtain this

analytical     result  (see  Appendix        B);   we  have   used      again        s     =     11  as  in   M-theory          for       the  numer-
                                                                                                 2

ical check. This result matches exactly the direct numerical integration of (4.25). Plotting

the integrand, we can explicitly see the regions where the Casimir energy is localised, i.e.

the  Casimir   branes      located      at  (z1, z2)      {(0,  0),  (  1  ,  2  ),  (  2  ,  1  )}  and   wrapping             the       z3  direction
                                                                        3     3         3     3
                                                          1
(figure  2).   Alternatively,     the      choice  h3  =  2   gives

                  (sg)       xsg  -  1      1              1                        1                          2                      5
                  2sg                3     22s       2sg, 6                   2sg, 3                     2sg, 3                 2sg, 6
     E (g)  =  -        �                                        -                               -                        +                    .
                           3R2sg -1

                                                                                                                                               (4.70)

Funnily enough, we see that the contribution of twisted sectors to the Casimir sums (i.e. the

tensions of Casimir branes) can often be computed analytically, even when the untwisted term

(corresponding to the parent T 3 contribution) cannot! The traces of Dg over the M-theory

representations are

                        Tr44(Dg) = 20 , Tr84(Dg) = 21 , Tr128(Dg) = 40 .                                                                       (4.71)

This 3d RFM contains one more non-trivial element, namely D2g. Repeating the exact same

steps for this element, we find that the result with h3 = 0 is the same as for Dg. However,

when h3 =      1  we have E(g2) = -E(g).                  This is not a coincidence; it follows from the fact
               2

that g2 = g-1. In Appendix B we show that for cyclic RFM's with 1-dimensional invariant

subspaces, we always find

                                                     E(gj) = -E(gp-j) ,                                                                        (4.72)

where p = ||, the order of the cyclic group. On the other hand, the explicit formulas for the
traces in Appendix F together with the fact that the eigenvalue arguments i are pth roots
of unity, i.e. p i = 2Z, imply that the traces of Djg and Dgp-j are the same over bosonic

representations.

     Consider an alternative 3-dimensional RFM with holonomy group Z4, namely the mani-
fold T 3/Z4 with the group generated by

                                                0 1           0                      0                                                         (4.73)
                                        Dg =  -1 0            0 ,             bg =  0  .
                                                              1
                                                    00                                      1
                                                                                            4

Our  condition    (3.22)     allows     for  the   choices    h  =   (0, 0, h3)               and    h  =  (  1  ,  1  ,  h3);  furthermore       we
                                                                                                              2     2

                                                             � 38 �
           (a) Periodic h = (0, 0, 0).                                    (b)  Anti-periodic  h  =   (  1  ,  1  ,  0).
                                                                                                        2     2

Figure 6. Casimir energy density from a field with periodic (anti-periodic) boundary conditions

around the fibre.  In  both    cases  we   identify  clearly  the     Casimir  branes  at  (z1, z2)        {(0,     0),      (  1  ,  1  )};
                                                                                                                                2     2

for periodic boundary conditions, the two Casimir branes have positive tension, but for anti-periodic

boundary conditions they have opposite tension, which results in a cancellation for the total Casimir

energy. We will discuss this phenomenon in detail in Section 4.5.

must satisfy the additional condition (3.23),

                                              sg = 2h3 mod 2Z .                                                                 (4.74)

For  the  Z4  action   (4.73),    we  have  Dg4  =   -I   and       thus  sg   =  1,   which  constrains               h3          =     1  .
                                                                                                                                         2

According  to  (4.46),   only the     choice  h  =   (0,  0,  1  )  gives a  non-zero Casimir        energy.              We can
                                                              2

clearly see this effect by plotting the integrand for both choices: when the field has twisted

boundary conditions around the fibre, regions of positive energy density cancel against regions

of negative energy density (figure 6). We can interpret this result as the cancellation between

two Casimir branes of opposite tension. For this RFM the Casimir branes are indeed localised

at (z1, z2)    (0, 0) ,  1  ,  1      and  wrapping  z3;         the  Casimir  brane   at  (z1, z2)           =     (  1  ,  1  )     has
                         2     2                                                                                       2     2

negative tension when anti-periodic boundary conditions are chosen.

     One can use these two 3-dimensional RFM's to visualise the spin structure consistency

condition (3.22), recalling its derivation in Section 3 (figure 7), by omitting the subspace left

invariant by Dg (in both cases the z3 direction). The condition (3.23) can also be understood
from these pictures: the action Dg3 leaves all lattice vectors invariant, Dg3 z = z; the only
effect of this action is therefore a translation by the lattice vector (0, 0, 1) = 3bg, which must
be compatible with the corresponding action (-1)2h3. This must then be the sign of Dg3.

     Finally, let us compare our method with a result known in the literature. We will use

(4.53) to compute the Casimir energy for M-theory on the interval S1/Z2 and compare the

                                                     � 39 �
                   (a) T 3/Z3                                                   (b) T 3/Z4

Figure 7. Visualising the constraints on spin structures that are preserved under the diffeomorphisms
Dg for the Z3 (4.64) and Z4 (4.73) actions on T 3. The action on a fermionic field under a translation
by a lattice vector n is given by (-1)2h�n. For example, since the vector (1, 0) is mapped to (0, 1) under
the Z3 action Dg, a consistent spin structure must give the same action (sign) upon a translation by
(1, 0) and (0, 1); thus h1 = h2 mod Z. Moreover, since (0, 1) is in turn mapped to (-1, -1)  (1, 1)
on the covering T 3, a translation by (0, 1) must have the same effect on a spinor as a translation by

(1, 1), i.e. h2 = h1 + h2 mod Z. Together, these restrictions fix h1 = h2 = 0 mod Z. Repeating the
exercise with the Z4 action, one still finds h1 = h2 mod Z, but both signs remain consistent as long as
they are shared by the two directions.

result with equations (2.12) and (2.13) of [129]16,

VCMa-stheory       on  S1/Z2  =     J   ,   J   =    (  11  )  211 -  1   (11)    1.206 � 10-2 .        (4.75)
                                 - L10                  2        213

                                                     211/2

Strictly speaking, this case is outside of the realm of validity of our method, since the Z2
leading to the Horava-Fabinger interval S1/Z2 has fixed points (it acts by sending z 

-z). Therefore, this is not an RFM, but rather, a Riemann-flat orbifold (away from the
singularities). In our notation, this would correspond to Dg = -1, bg = 0. Nonetheless

we may still apply our formula (4.53), summing over the two elements of this Z2, to find

precisely the result (4.75). In fact this contribution comes uniquely from the identity term,

since our formula is proportional to the size of the invariant subspace, which for the non-trivial

element  of  this  Z2  action  corresponds  to  the  two  individual     fixed  points  z    {0,  1  }  that  have
                                                                                                  2

zero volume. More accurately, the twisted sector only contributes through the divergences

associated with the orbifold (and so, in this case, it is a twisted sector in the standard sense).

However since the twisted sectors correspond to a Horava-Witten E8 brane and its antibrane

  16Equation (2.13) in [129] is written in terms of the Jacobi theta function 4(0, i ) and only argued to be
convergent and positive. However, one can compute it analytically using Poisson resummation and a Mellin
transform--just as in the derivation of our general formula--to find (4.75).

                                                � 40 �
in this example, we know the twisted sector contribution vanishes. It is also important to note
that L used here denotes the size of the interval, which is related to the size of the covering
S1 as R = 2L.

     We are now in a position to compute the Casimir potential for our 7d solution of M-theory
on T 4 discussed in Section 2. It is simply

                                      T4           11               Tr44(I)    +  Tr84(I) - Tr128(I) e2ih�n
                                             -     2        G                            |n|11
            VCMa-stheory          on      =                                                                  ,  (4.76)

                                             211/2             nZ4

since there is no quotienting and thus the only element in the    sum is the identity (cover-

ing T 4); we also include the sum over the representations in M-theory, i.e. the graviton (44),

the 3-form (84) and the gravitino (128), which for the identity are simply their respective

dimensions. For the specific symmetric point in moduli space where the lattice  defining

the T 4 is the root lattice of C4 with its standard inner product, written in a basis in which it

takes the form                                                      2 -1 0 1 

                                                       G  =    R2  -1      2   -1   0                           (4.77)
                                                                          -1    2  -1
                                                                       0


                                                                       1 0 -1 2

and choosing boundary conditions for the gravitino that are twisted around every direction,

h  =  {  1  ,  1  ,  1  ,  1  },  the  Casimir   energy    is
         2     2     2     2

                                      T4              945                 1 - (-1)n1+n2+n3+n4  8.827
                                                      645
            VCMa-stheory          on      =  -128  �       �   2R4                              - R7 ,          (4.78)

                                                                    nZ4            |n|11

which is precisely the Casimir contribution to the potential (2.15) in our dS7 example of
Section 2. Note that we chose a basis that does not correspond to the inner-product matrix
in the C4 root-basis17,

                                                            2 -1 0 0 

                                                           -1        2    -1    0   ,                           (4.79)
                                                                    -1     2   -2
                                                               0


                                                               0 0 -2 4

but is rather related to it through the transformation

                                                 z1  1 0 0 1  z1

                                                 z2                 0  1  0    1   z2     .                     (4.80)
                                                 z3                 0  0  1    1
                                                                                    z3


                                                      z4            0 0 0 1 z4

  17Recall that for a non-simply laced group such as C4 the inner-product matrix for the root lattice does not
directly match its Cartan matrix.

                                                                       � 41 �
We will see in Section 5 that it is the form (4.77) that naturally appears at special points in
the T 6/Z8 moduli space--of course, the lattice is still the C4 root lattice.

4.5 Casimir branes and Atkin-Lehner symmetry

The main goal of this paper is to achieve Casimir-de Sitter vacua. In this section, which

is somewhat out of this main line of development, we wish to emphasize a very interesting

phenomenon that we observed while deriving (4.53). As explained in the discussion right after
this equation, the expression for the integrated Casimir energy contains a factor ^h which
evaluates to zero whenever a certain condition on the h vector of spin structures (equation

(4.46)) is not satisfied. Within our context, this can only happen for fermionic fields18.

Therefore, we have found a mechanism that will ensure the vanishing of (one-loop, twisted)

contributions to the Casimir energy of fermions, even in the absence of supersymmetry--we

would like to understand this in some detail.
     First, consider Figure 6b, which shows a plot of the Casimir energy where ^h vanishes.

We see that there are two Casimir branes at different locations, so the energy density is non-

trivial. The vanishing vacuum energy is achieved by a detailed cancellation of the tensions

between these two branes. This is reminiscent of what happens at tree level in supersym-

metric orientifold compactifications--but now, it is happening at one-loop, and in a fully

non-supersymmetric context.

The apparent symmetry of Figure 6b suggests that to explain this vanishing we should

look for a translation symmetry under which the integrand of (4.25) is odd. Indeed, a shift

z  z + e in the integrand can be compensated by a shift of the summation variable n

whenever

                               (I - D) � e  Zk ,      (4.81)

at the cost of a phase factor

                               e2i [(I-Dg)T h]�e.     (4.82)

If the integral is not to vanish identically, for any solution to (4.81) the corresponding phase
(4.82) must be trivial. In other words, we must have

          h � (I - D) e  Z, whenever (I - D) e  Zk .  (4.83)

If (4.46) holds, so that ^h = 1, then h can be replaced by   Zk and (4.83) holds automatically.
Conversely, equation (4.83) is the statement that h is in the dual lattice to the lattice of vectors

of the form (I-D) e  Zk. This lattice is primitive in Zk, and therefore, by arguments similar

to those leading to (4.49), we can conclude that the dual lattice is spanned by vectors of the

form

          (I - D)T  + Inv,   Zk, DT Inv = Inv .       (4.84)

  18Whenever one considers non-trivial bundles for discrete symmetries in an RFM, this will also happen for
bosons. However, it can never happen for the zero mode of the graviton, which is necessarily uncharged under
all internal symmetries.

                               � 42 �
The statement that h is in the dual lattice is then (4.46). Thus, ^h only vanishes when one
can find a non-trivial vector e.

     In summary, what happens is the following: We have an explicit formula for the Casimir
energy, equation (4.25), which gives us (a contribution to) the one-loop vacuum energy as an
integral of some function (the 11-dimensional energy density ^(z)) on a domain (the RFM),

                             VCas                 ^(z) dV ,  (4.85)

                                        RFM

and we have found an "anomalous" symmetry of the integrand, by which we merely mean
that it transforms with a non-trivial phase,

                             ^(z + e) = ei(e) ^(z) ,         (4.86)

and which is also a symmetry of the integration region (the RFM, since it is flat). As a result,

the integral VCas vanishes due to cancellations between different regions of the integration
domain. Phrased in this way, the phenomenon we have found is quite reminiscent of Atkin-

Lehner symmetry [50�52], a proposed mechanism to achieve vanishing vacuum energy at

higher loops in perturbative string theory. In Atkin-Lehner symmetry, one writes the one-

loop contribution to the vacuum energy in the worldsheet as the usual integral over the

fundamental domain F [127],

                             V 1-loop                    d2  (4.87)
                                                  Z( ) .
                                                  2
                                               F

The idea of Atkin-Lehner symmetry is that one may find special worldsheet CFT's where the

theory is symmetric with respect to additional torus diffeomorphsims not included in SL(2, Z)

(for instance,   -1/(2 )), but where this symmetry is anomalous, so that the partition

function transforms with a non-trivial phase,

                                     1         = eiA Z( ) .  (4.88)
                             Z-
                             2

As a result of (4.88) and the fact that   -1/(2 ) is a symmetry of the integration domain
F, the integral vanishes.

     To our knowledge, Atkin-Lehner symmetry has only ever been discussed in perturbative
string theory and, in fact, explicit examples of worldsheet CFT's realizing it have only been
constructed with a two-dimensional target space [51, 52, 130]. Yet this mechanism is totally
analogous to what we have just described for Casimir energies, under the correspondence

                                        � 43 �
Worldsheet Atkin-Lehner symmetry RFM Casimir energy symmetry

Torus worldsheet partition function Z( ) Higher-dim. Casimir energy density ^(z)

SL(2, Z)                                                        RFM defining group B

SL(2, Z) fundamental domain           Riemann-flat manifold (integration region)

Atkin-Lehner symmetry Z( )  eiA Z( )       Symmetry ^(z + e) = ei(e) ^(z)

Thus, in some sense RFM's exhibit what may be the first example of a spacetime Atkin-
Lehner-like symmetry. This suggests that the mechanism of [51] is not intrinsically stringy,
and similar phenomena are also under the reach of EFT. One important difference with respect
to the worldsheet Atkin-Lehner symmetry is that, in the original formulation, the mechanism
ensures the vanishing of the complete one-loop vacuum energy, while the field-theoretic version
we have found in RFM's only works for some contributions (twisted sectors) to the vacuum
energy, and for fermionic fields only (or more generally, for fields charged under internal
symmetries with a non-trivial bundle on the RFM). Nevertheless, it seems possible to e.g.
engineer QFT's with vanishing one-loop vacuum energy when compactified on appropriate
RFM's. Perhaps thinking along these lines can provide a new way to engineer solutions with
an anomalously small vacuum energy. We hope to return to these very interesting questions
in the near future.

4.6 Numerical evaluation of Casimir energies

Although we have now a fully explicit, analytic formula to compute Casimir energies (i.e. the

tension of Casimir branes), there is still the matter of evaluating (4.53) explicitly in concrete

examples. In general, there is no analytic expression for sums like (4.53) [94], so we must

restort to numerical methods. A sum like (4.53) is convergent, but the speed of convergence
can be very slow depending on s and . Furthermore, we will need to evaluate these sums for

high-dimensional lattices, up to dimension 7 for the examples in Section 6. Moreover, to scan

for dS maxima we will need to evaluate the sum many times, for different values of the moduli.

Under these circumstances a direct attack, by first truncating the sum, evaluating it, and then

performing the integral numerically, will quickly become computationally prohibitive19.

However, we are in luck: a sum like (4.53) is a higher-dimensional analog of the sums

employed to compute lattice energies of ionic crystals, for which efficient numerical methods

have been developed. So to evaluate the sums efficiently, we will use the technique of Ewald

resummation [131], which is standard in computational chemistry (see e.g. [132]). The idea

of the technique is as follows: Suppose one wants to evaluate a sum like that appearing in

(4.53), schematically of the form

                                           e2ih�n                                     (4.89)
                                         |n + c|2s .

                                   n= -c

If the quantity we are summing over was a smooth function of n, we could do Poisson re-
summation and use the Fourier-converted sum to quickly compute the tails of the sum in

19We tried anyway, just to be sure, and it is indeed very bad.

                                   � 44 �
position space. However, the function |n + c|-2s has a pole at n + c = 0, and therefore, a
direct application of Poisson resummation will not yield convergent results. Instead, Ewald
resummation proceeds by splitting the sum as

                      e2ih�n              F (n) e2ih�n     (1 - F (n)) e2ih�n  ,  (4.90)
                      |n + c|2s =         |n + c|2s +
             n= -c                 n= -c                n          |n + c|2s

where the function F (n) is chosen such that

 lim  1 - F (y)    is finite, and F (y)  0 as |y|   faster than a polynomial .    (4.91)

y-c   |y  + c|2s

Under these circumstances, the first sum in (4.90) can be evaluated directly and converges
quickly in real space. The second sum now is over all n, and the conditions (4.91) ensure that
it can be evaluated by Poisson resummation. As the function being summed over is smooth,
its Fourier coefficients will decay quickly, and the momentum space sum will also converge
rapidly. Which precise form of F (n) is best depends on the particular sum being evaluated;
the Coulomb case s = 1/2, k = 3 most often studied in chemistry is customarily tackled with
F (n)  erfc(|n|) [132]. Exactly the more general sum (4.89) was studied in [133], but only
in three dimensions. We have extended these techniques to arbitrary dimension (details20
can be found in Appendix C). The general result, applied to the integrand in (4.25), reads as
follows:

         e2ih�n
        |n + c|2s =

n+c=0

        e2ih�n (s, |n + c|2)              2s-  k           k - s, 2|h - k|D2      e-2i(h-k)�c
                                               2                                  |h - k|kD-2s
                                   +                    
        |n + c|2s        (s)              (s) G k-h= 0     2                                  (4.92)

n+c=0

             k  s-k/2            s e-2ih�c
+  h,0    G  2                -  (s + 1) Zk (c).

             (s)   s  -    k
                           2

In practice, we will evaluate these sums numerically, including a hard cutoff in momentum and

position sums, and using the freedom in choosing  to ensure the value of fastest convergence

(which will depend on the parameters of the sum and the cutoff in the sums, see Appendix

D). In these expressions,                            

                                   (s, z)              ts-1e-t dt                 (4.93)

                                                  z

  20Shortly after we independently derived these results, [134] appeared, which uses similar ideas to achieve
efficient evaluation of Ewald sums. The final expressions of [134] are equivalent to ours; the only practical differ-
ence is that the numerical implementation provided in [134] becomes significantly slow for higher-dimensional
sums, due to details on how the sample points for the sum are selected in the numerical code. We produced an
independent implementation which is more efficient for higher-dimensional cases, and was used for all results
in this paper.

                                            � 45 �
is the incomplete  function, and Zk (c) is the characteristic function of the integers (it is
1 when all components of c are integers, and zero otherwise). Since c  [0, 1)k as discussed
above, this can only happen when c = 0. The norms in the second sum have a D subscript
to indicate that they are dual lattice sums, where the inner products are to be taken with
respect to G-1, the natural metric in the dual space, as befits to a momentum space sum.

Finally,  > 0 is a free parameter. The actual value of the sum does not depend on , but the

relative contribution of the different terms do;  may then be chosen to optimize the speed

of convergence of the overall sum. Since the incomplete  function has the asymptotics

(s, z)  (s) - zs + O(zs+1),  |z|  1,  (4.94)
                      s      |z|  1,

(s, z)  e-z zs-1 1 + O(z-1)

in the limit   0 the momentum space sum is completely suppressed, and one recovers the

original expression in (4.89). On the other hand, when  is very large, the position space

sum is negligible, and the sum is dominated by the momentum space term. Notice that,
in the regime of interest 2s > k, the terms |h - k|D in the momentum sum diverge badly,
so the regulating effect is due to the oscillating phases e-2i(h-k)�c, which introduce large
cancellations whenever c = 0. When c = 0 or h = 0, the terms in the second line of (4.92)

are crucial for convergence, as is the  function factor.

     All numerical results for Casimir energies in this paper were computed via the Ewald

formula (4.92). While these are not really necessary for lower-dimensional examples, such as

the two or three-dimensional examples at the end of the previous subsection where brute force

suffices, an efficient implementation is a key requirement for the higher-dimensional sums that

we will encounter in Sections 5 and 6.

     Finally, there is a nice physical interpretation of the Ewald result (4.92), when particu-

larized to Casimir sums of the form (4.53). In that expression, the dual space sum (second
term) in (4.92) is over the lattice , dual to , which contains precisely the momenta k for
which the plane wave e2ik�y is well-defined as a function on the RFM. These vectors are then
shifted by e2ih�y, which implements twisted boundary conditions. In other words, the second
sum in (4.92) is a sum over the KK spectrum of the RFM, and |h - k| is precisely the mass

of the corresponding KK mode. Since 2s = D, the total spacetime dimension, we have that

k - 2s = -d, where d is the number of non-compact spacetime dimensions, and the second

term in (4.92) can be recast as a regularized version of the sum

              mKd K,                  (4.95)

KK spectrum

of zero-point energies of KK modes, over the whole KK spectrum. We recognize the standard,
UV divergent, computation of vacuum energies as a sum of one-loop diagrams/zero-point
energies over the particle spectrum of the lower-dimensional theory. Doing this sum directly
in lower-dimensional EFT leads to divergences that have to be regularized and removed e.g.

� 46 �
by imposing higher-dimensional Lorentz invariance in the decompactification limit. This is the
standard sum of one-loop vacuum bubble diagrams commonly employed to compute Casimir
energies [36] in momentum space, and is dual to the position space point-splitting method
we used here to regularize the Casimir stress-energy tensor in Subsection 4.1. The Ewald
expression (4.92) then provides a regularization for both terms, and includes a parameter 
that smoothly interpolates between a purely momentum (at   ) or a purely position
sum (at   0). One can then regard the -independence of the result as a consequence of
the fact that physical results are independent of the regularization scheme. The advantage
of the position space point-splitting method over the momentum one is that it also produces
an expression for the full higher-dimensional backreacted stress-energy tensor, as stressed in
Section 2, which means that the higher-order corrections can in principle be computed and
evaluated explicitly, as discussed there.

5 A dS5 maximum in M-theory

After setting up all the groundwork, we are finally ready to come to the main point of this
paper: an explicit de Sitter maximum solution which is under theoretical control. The vacuum
we have in mind is a compactification of M-theory on dS5 � F6, where F6 is a particular
Riemann-flat manifold, threaded by G4-flux. The four-dimensional scalar potential will arise
from just two sources: a Casimir and a G4-flux piece,

                             V (5d) = VCas + VG4 ,                                     (5.1)

where the fluxes will be carefully chosen to ensure that V (5d) has a saddle point in all
directions--including the volume. We will first present the manifold F6, then study its Casimir
potential using the formulae in Section 4.3, followed by a detailed study of the flux potential,
and a determination of the maximum parameters. Finally, we will study corrections to the
solution, describing in which sense they are small.

5.1 The Riemann-flat manifold F6

To construct our de Sitter maximum, we will compactify M-theory on the RFM F6, described
as follows. Consider a T 6 parametrized by coordinates z = (z1, z2, z3, z4, z5, z6), subject to

the identifications

                             zi  zi + 1 .                                              (5.2)

We will quotient by the Z8 action generated by the affine transformation

                                     0 0 0 -1 0 0                            0

                                    1 0 0 0 0 0                              0

z  g(z) = Dg z + bg ,  with  Dg       0     1  0  0  0  0    ,  bg        =    0    .  (5.3)
                                      0     0  1  0  0  0                      0  


                                      0     0  0  0  1  0                      0  


                                      000001                                   1

                                                                               8

                                    � 47 �
This action has no fixed points on T 6, since the vector bg lies in the invariant subspace of
Dg. The matrix Dg is of order 8, and the manifold F6 is defined as the quotient

                                          F6  T 6/Z8 .                            (5.4)

We must now endow F6 with a Riemann-flat metric. As discussed in Section 3, they all come
from Riemann-flat metrics on the covering T 6 that are invariant under Dg. The most general

possibility is

ds2 = Gijdzi dzj ,

       ( + 2)R22 -( + 1)R22                     0        ( + 1)R22 0 0 

       -( + 1)R22 ( + 2)R22 -( + 1)R22                      0     0 0

             0         -( + 1)R22 ( + 2)R22 -( + 1)R22            0    0     
        ( + 1)R22                                                 0    0
G  =                   0                  -( + 1)R22 ( + 2)R22                 .  (5.5)


                    0  0                        0           0     R12  R12   


                    0  0                        0           0     R12 -1R12

There are five moduli, parametrized here as {R1, R2, , , }--this means that 16 of the 21
moduli of T 6 have been fixed by the quotient (5.4). Since we are looking for a dS maximum,

we do not need to stabilize all these moduli; a saddle point, where the first derivative of

the potential vanishes, will suffice. We will now identify a subspace of the moduli space,

given by specific values {, , }, where the partial derivatives along these directions vanish

automatically due to symmetry arguments (see also [81, 88]); we will not have to worry about
them henceforth. To do this, notice that an affine transformation z  f (z) = A z + b of the
parent T 6 will descend to a well-defined diffeomorphism of F6 if the points z and A z + b of
T 6 are in the same Z8 orbit generated by (5.3), or in other words, if

                          f (g(z)) = gn1+1(f (z)) .                               (5.6)

This is the condition that the affine transformation f (z) is in the normalizer of the Z8 gener-
ated by g(z). By adjusting the vector b appropriately, (5.6) becomes the same condition in

terms of matrices,

                       A � Dg � A-1 = Dng1 , n1  Z .                              (5.7)

For Dg as in (5.3), one possibility is

                                        1 0 0 0 0 0

                                        0 1 0 0 0 0

                                          0  0  1  0  0  0  
                                          0  0  0  1  0  0
                       A  =                                    ,                  (5.8)


                                          0  0  0  0  0  1  


                                          0 0 0 0 -1 0

                                             � 48 �
a matrix of order 4 that in fact commutes with Dg. The matrix (5.8) therefore descends to
a well-defined diffeomorphism on F6. Its action on the metric

                        ( + 2)R22 -( + 1)R22                        0          ( + 1)R22 0              0

                        -( + 1)R22 ( + 2)R22 -( + 1)R22                                 0          0 0

                              0        -( + 1)R22 ( + 2)R22 -( + 1)R22                             0    0     
                         ( + 1)R22                                                                 0          
G   AT  �  G  �  A  =  
                                             0              -( + 1)R22 ( + 2)R22                        0     


                              0              0                      0                   0        -1R12  -R12  


                              0              0                      0                   0        -R12 R12

                                                                                                              (5.9)

maps   -,   -1, and hence at  = 0,  = 1 it becomes a Z4 isometry. The

components of the gradient (V, V ) transform as a vector under this Z4, and therefore, if

the G4 flux choice respects this isometry (something that will be ensured in Subsection 5.3),

we will have V = V = 0 as desired.

We can run a similar argument with

                                        1 -1 1 0 0 0 

                                        1 -1 0 1 0 0 

                                 A  =     1     0 -1 1           0   0      ,                              (5.10)
                                          0     1 -1 1           0   0    


                                          0     0     0     0    1   0    


                                          000001

which acts on G by sending   -. Since (5.10) is of order 2, at  = 0 this is a Z2 isometry
under which V picks up a sign. It follows that, as long as fluxes are chosen appropriately
to respect these symmetries, at the locus of moduli space given by

                         0 0 0 0 0 0                                2 -1 0 1 0 0 

                         0 0 0 0 0 0                                -1 2 -1 0 0 0 

                           0  0   0    0  0  0                         0  -1 2 -1          0  0  
                           0  0   0    0  0  0                         1  0 -1 2           0  0  
           G     =  R12                                  +  R22                                    ,       (5.11)


                           0  0   0    0  1  0                         0  0    0     0     0  0  


                           000001                                      000000

the potential is automatically a saddle for all moduli except maybe {R1, R2}. In fact, after a
change of basis where the first four coordinates are transformed as

                            z1   1 0 0 -1   z1 

                            z2               0     1     0     -1    �    z2      ,                        (5.12)
                                             0     0     1     -1         z3   
                              z3                                               


                              z4             0001                         z4

the upper left block of the term proportional to R2 in (5.11) becomes precisely the Cartan

matrix of the C4 algebra. Thus, the special locus of moduli space we have found is such that
the parent T 6 defining lattice is C4(R2)  Z2(R1)--the C4 root lattice, rescaled by a factor of

                                                � 49 �
R2, times a square lattice21. The transformation (5.10) is precisely one of the reflections in
the Weyl group of the C4 lattice. Describing the root lattice in terms of an ambient R4 space
with basis {e1, e2, e3, e4} equipped with standard inner product, the C4 roots are vectors of
the form �(ei - ej) plus �2ei. The Weyl group acts by permuting the roots and flipping the
sign of any number of them [135]. In terms of these variables, (5.10) corresponds simply to

the Z2 transformation that sends

                              e1  e1 , e2  e4 , e3  -e3 .                                                 (5.13)

In short, the reason why this special locus of moduli space exists is because the T 6 lattice

becomes a root lattice for some simple Lie algebra, and has a large isometry group correspond-

ing to the Weyl group of the lattice. This technique to find saddle points of the potential by

searching for root lattices will also be helpful in other setups, such as those of Section 6.2.

     For the question of Casimir energies it will be important to specify the spin structure
on F6. As explained in Section 3, the choices of spin structure are labelled by a vector h

whose components are all 0 or 1/2 modulo 1, and encode the periodicity of fermions along

the six cycles of T 6. However, not every spin structure on T 6 descends to a well-defined

spin structure on F6; the allowed ones are determined by solving equations (3.22) and (3.23).

Since we are quotienting by a group of even order, the spin lift of the generator Dg satisfies

Dg8 = I. For F6, there are then 2 possibilities for h compatible with the isometries discussed

above,

                              (0, 0, 0, 0, 0, 0) or            1111                                       (5.14)
                                                                , , , , 0, 0 .

                                                               2222

In other words, we may only choose the spin structure on the C4 lattice (it is fixed to be

periodic  on  the  Z2),  and  we  will  choose  (  1  ,  1  ,  1  ,  1  ,  0,  0),  where  fermions  are  antiperiodic
                                                   2     2     2     2

along all coordinates of C4, since the alternative will not yield a dS saddle. As we will

see in Section 6, most cyclic RFM's do not allow for an antiperiodic spin structure on the

subspace where the point action acts transitively; in fact, out of all the possibilities discussed

in Section 6, only the one used in this section and those closely related to it (by which we

mean that they have the same Z8 block as the one discussed here) allow for antiperiodic

boundary conditions. These turn out to be crucial to achieve a saddle point, which explains

our particular choice (5.3) in this section. Relatedly, any SL(6, Z) transformation with the

same block decomposition (in the sense of Section 3) as Dg can be brought, via an SL(6, Z)

  21The D4 and C4 root lattices are identical, so all the discussion here can be equivalently phrased in terms
of the D4 root lattice. In this picture the transformation (5.11) is not part of the Weyl group of D4; rather,
an element in this Weyl group needs to be combined with an outer automorphism of the D4 algebra of order
2 to obtain (5.11). The two pictures are of course equivalent.

                                                � 50 �
change of basis (is conjugate) to either Dg or the closely related transformation

                                        0 0 0 1 0 0

                                        1 0 0 0 0 0

                                            0  1  0    0   0      0  
                                               0  1    0   1      0
                                                                       .                               (5.15)
                                            0                        


                                            0  0  0    0   1      0  


                                            000001

Using this instead of Dg in (5.3) does not allow for an antiperiodic spin structure in the

first four components; as a result we do not study it either. The only other freedom is
in choosing the shift vector bg. For the example we are discussing there is more than one
inequivalent choice of vector bg. As explained in Section 3, the choices of bg are in one-to-one

correspondence with solutions to the equation

                                            Dg bg = bg mod Z ,                                         (5.16)

which in our case has two inequivalent solutions,

                        bg =             ab            or     1111ab                                   (5.17)
                              0, 0, 0, 0, ,                    ,,,,, ,

                                         88                   222288

where a, b are integers constrained such that the first multiple of bg to be a lattice vector is
precisely 8bg. Thus, we see that (5.3) provides only a particularly simple choice of bg. We

have also explored all others, and they are either as good as this one or worse in terms of

Casimir energy and the size of the space, as explained in Subsection 5.2.

     All of the above explains our choice of F6 via (5.3) and spin structure on the parent T 6.

We just need to study the scalar potential as a function of (R1, R2). Our last task in this
subsection is to perform a convenient change of variables. The volume of the covering T 6 in

our locus of moduli space is

                                            Vol(T 6) = 2 R24 R12 .                                     (5.18)

The volume of the RFM is reduced by a factor of 8 from this. We will introduce new variables

(x, R) defined by

                                        R6  R24 R12,       x  R2 .                                     (5.19)
                                                                 R1

The  variable  R  is  essentially  the  volume    modulus     of  F6   (we  have  Vol(F6)  =  1  R6),  while  x
                                                                                              4

measures the aspect ratio between the C4 and Z2 factors of the RFM discussed above. The

inverse relation reads                         R

                                        R1  =       ,  R2 = R x1/3 .                                   (5.20)
                                               x2/3

                                                  � 51 �
5.2 Casimir energy

We must now calculate the Casimir energy term VCas in (5.1), using the formula (4.53). In five
dimensions, the Casimir energy is a moduli-dependent quantity with units of length-5 which
is obtained from a one-loop calculation of the massless fields. Since the only dimensionful
modulus in (5.19) is R, dimensional analysis forces a Casimir term of the form

                                                        C(x)                                                                              (5.21)
                                            VCas = - 4 R5 ,

where we have packed all non-trivial dependence in a Casimir function C(x). We have also
introduced an overal minus sign in the definition of (5.21) to take into account the fact that
Casimir energies of periodic fields are usually negative; hence, we expect C(x) to be a positive
function. In this section we will study C(x) in some detail, but it is important to keep in
mind that the actual physical energy contains an additional minus sign.

     Recall that the Casimir energy VCas on F6 = T 6/Z8 is given by,

                            (s)      d6z            7            TrB(Dgj ) - TrF(Dgj ) � e2ih�n                       ,                   (5.22)
                VCas = - 2s �                 G    j=0             |(I - Dgj ) z - j bg + n|2s
                                  F6
                                                         nZ6

with s = D/2 = 11/2 for M-theory. The contribution of each group element (apart from the

Figure 8. Integrands of E(Dg) (4.25) for a bosonic and a fermionic degree of freedom, respectively,

with  the  fermionic  boundary  conditions  being  fixed  by  our  choice          of    spin     structure  h    =  (  1  ,  1  ,  1  ,  1  ,  0,  0).
                                                                                                                        2     2     2     2

By rotating the axes appropriately and plotting on the plane (z1 + z2 + z3 + z4 , z1 - z2 - z3 + z4), we

can  see  both  Casimir  branes,  one  at  (0, 0, 0, 0)  and  one  at  (  1  ,  1  ,  1  ,  1  )  on  the  fibre  T4     that       wrap        the
                                                                          2     2     2     2
base T 2. While for bosons both Casimir branes have positive tension, for fermions they have opposite

tension and cancel each other out upon integration over the covering T 6.

                                                         � 52 �
identity)         can  be   seen   as  the            energy      of  two  Casimir        branes  localised    at     (0,      0,    0,  0)   and      (  1  ,  1  ,  1  ,  1  )
                                                                                                                                                          2     2     2     2

on the T 4 fibre and wrapping the base T 2, corresponding to the subspaces invariant under

Dg, i.e. Dg z = z mod Z6 (see figure 8). The location of Casimir branes is the same for

every non-trivial   . The identity element contributes as a space-filling Casimir brane,

wrapping the whole of F6. Given the block diagonal structure of the invariant metric (5.11),

the norm splits into two pieces

VCas          =     (s)     �   2R12R24            �   7          d4z                TrB(Djg) - TrF(Dgj ) � e2ih�(n,m )                                s.          (5.23)
                  - 2s           |Z8|                 j=0                         R22 |(I - Dgj ) z + n|2 + R12 |m - j bg|2
                                                              T6       nZ4

                                                                       m Z2

We also split the 6d vector n into a 4d vector n along the fibre and a 2d vector m along the
base. Substituting in the order of |Z8| = 8 and performing the change of variables (5.20), we
have

                                               4s          7                               TrB(Dgj ) - TrF(Dgj ) � e2ih�(n,m )
                                                                                          x2 |(I - Dgj ) z + n|2 + |m - j bg|2
                      (s) x 3                                         d4z
VCas = - 2s � 4 � R2s-6 �                                                                                                                              s.          (5.24)

                                                        j=0       T6         nZ4

                                                                           m Z2

For     the   choice        of  fermionic               boundary       conditions         given   by   h  =        (  1  ,  1  ,  1  ,  1  ,  0,  0),  we       find        a
                                                                                                                      2     2     2     2

potential of the form (5.21), with

                       (s)               7                 d4z             TrB(Djg) - TrF(Dgj ) � ei(n1+n2+n3+n4)
                                                                             x2 |(I - Dgj ) z + n|2 + |m - j bg|2 s
                                   22                   T6
           C(x) = 2s � x 3                                                                                                                        .                (5.25)

                                       j=0                        nZ4

                                                                  m Z2

Note that the Casimir potential is a sum over the 8 elements of Z8. As we show in Section
4.3, the terms corresponding to non-trivial elements Dgj , j  {1, ..., 7}, collapse into a 2d sum

over the base T 2 corresponding to the invariant sublattice under Dg,

                                                           (s - 2)                 7                   TrB(Dgj )

                                                                             10
                               Ctwisted(x) = 2s-2 � x 3
                                                                                j=1 m Z2  m12 +        m2      -      j     2 s-2
                                                                                                                      8

                                                      =    1.538  �    106   �     10  .                                                                           (5.26)

                                                                                x3

Note that the fermionic contribution drops out due to the factor ^h in (4.53), since there is no
solution to equation (4.46) with   Z6. The traces of each element in the graviton, 3-form
and gravitino representations were obtained using the formulas in Appendix F.22

     The twisted terms contribute with a very large numerical coefficient, which is going to
be crucial for our dS solution; this large coefficient benefits from the fact that the gravitino,

22The generator of our Z8 action (5.5), embedded as an SO(9) matrix, has eigenvalue arguments  =

{0, 0,     ,  3   }.  Note  that,  since           our  quotient      group  has  even    order,  the  choice  of  spin        lift  Dg       does   not     affect      the
        4      4
sign of Dg8 = I, which forces us to set h6 = 0 through (3.23) as argued above.

                                                                                � 53 �
              k                0        1    2        3              4         5             6      7

           Tr44(Djg) 44 14 12                         14             4         14            12 14

         Tr84(Dgj )         84       10       20         10          -4     10                20      10
         Tr128(Dgj )        128              -32                      0                      -32       
                                   16 2                                                             16 2
                                                      -16 2              -16 2

whose contribution comes with an overall minus sign, ends up not contributing at all through
the twisted terms. Recalling the overall minus sign in the Casimir energy (5.21), we conclude
that by going to the quotient RFM, the energy becomes very large and negative, allowing for
large dS solutions.

     On the other hand, the term corresponding to the identity element Dg0 = I cannot be
simplified--the whole lattice remains invariant under this element--and is a full 6d infinite
lattice sum that we must compute numerically,

                                   (s)            22                 1 - ei(n1+n2+n3+n4)
                    CI(x) = 2s � 128 � x 3                                              s.                 (5.27)
                                                                     x2 |n|2 + |m |2
                                                                nZ4
                                                      m Z2

Even though we cannot obtain analytically the exact dependence of CI(x) for all x, we can

find its asymptotic behaviour for small and large x. For x  1, the dominant term in the

sum would be the one with |n| = 0, as all other terms will be strongly suppressed at large x.

However, due to our spin structure with h5 = h6 = 0, this term vanishes--only terms with

4    ni  odd  contribute       to  (5.27).   This type of cancellation is responsible for the absence
i=1

of saddle points in the 4d settings we study in Section 6; there instead it is the boundary

conditions around the fibre that are forced to be periodic. We find

                                   CI(x)  6.31 � x-5/3 , as x   ,                                          (5.28)

using the Mellin transform followed by Poisson resummation, as we did to compute analyti-
cally some of the sums in Section 4.3. Although here we cannot obtain the exact analytical
result, we can take the zero mode in the Poisson sum over the base T 2 and neglect the expo-
nentially suppressed terms to derive this asymptotic behaviour. In the opposite limit, when
x  1, the biggest contribution to the sum comes from the terms with m = 0, since these
come with an x-2s enhancement compared to terms with m = 0,

CI(x)      (s)   �  128  �  x  22  -2s       1 - ei(n1+ ...+ n4)        4.414  �  x-  11  ,     as  x  0.  (5.29)
           2s                  3                     |n|2s                            3

                                        nZ4

This is sufficient to guaranty a critical point for some value of x. The function C(x) will
have a minimum arising from the interplay between the twisted and untwisted terms. We
can compare this behaviour with the numerical evaluation of the sums (figure 9)--we find a

                                                  � 54 �
minimum at (cf. figure 10)

                                         C(xmin = 0.1637)  7046.54 .                                                                                 (5.30)

                                   C1(x)  ~          4.44  x-  11
                                                               3

                        109        C1(x)  ~          6.31  x-  5
                                                               3

                                   C twisted(x)      ~  1.54      �  106  x  10
                                                                             3

                        106

                1000

                        1

                0.001        0.05  0.10                           0.50       1                          5             10

                                                                                 x

Figure 9. Casimir energy evaluated numerically for the twisted and untwisted sectors. We overlap
the analytical result found for the twisted contribution in (5.26), as well as the asymptotic behaviour
of the untwisted contribution for small x (5.29) and large x (5.28).

                        105

                        104

                1000                                                                        C1(x)
                                                                                            Ctwisted(x)
                 100                                                                        C(x) = C1(x) + Ctwisted(x)
                                                0.1
                                                                                       0.2                    0.3            0.4

                                                                                 x

Figure 10. Casimir energy evaluated numerically for the twisted and untwisted sectors, in a denser
region around the minimum at xmin = 0.1636, where the Casimir coefficient is C(x) = 7046.54.

    Note  that  having  twisted    boundary                    conditions           h       =  (  1  ,  1  ,  1    ,  1   )  around  the  fibre  is  crucial
                                                                                                  2     2     2       2

for a minimum to exist. This can be seen from (5.29), where the dependence on the fibre

components of h becomes explicit--if h = 0, the small x contribution to CI(x) that goes as

x-  11  will vanish and the minimum disappears.                                     This is a crucial difference with respect to
    3

the Z7 quotient we will discuss in Section 6--since in that case we are not allowed to choose

twisted boundary conditions around cycles belonging to the 6d fibre, the behaviour of CI(x)

as x  0 will not provide a minimum for C(x); in other words, for the Z7 quotient, the

                                                                        � 55 �
terms corresponding to zero modes with respect to the base S1 will necessarily cancel out,

affecting the small x behaviour of C(x). The same reasoning can be applied to the large x

behaviour, now in terms of the spin structure around the base T 2; for our Z8 quotient, these

are not twisted and so CI(x) decreases as x  . If they were twisted, CI(x) would increase

as x   and the identity Casimir contribution (i.e. the one corresponding to the covering

torus without a quotient) would have a minimum on its own--note however that it would be

orders of magnitude smaller than the one we find from the interplay with the twisted terms.

         We have also scanned through different choices of shift vector (5.17) allowed by (3.14)--

note in particular that there are choices of a and b that allow for fully twisted boundary

conditions, removing the constraint on h6 imposed by (3.23). We find that the choice bg =

(0,  0,  0,       0,   0,          1     )  maximizes                 the     minimum   value             C(xmin).
                                   8

105                                                   =  0,0,0,0,0,   1                                           105      =      1  ,  1  ,  1  ,  1  ,0,0         =    1  ,  1  ,  1  ,  1  ,0,   1  
                                                                      8                                                           2     2     2     2                    2     2     2     2        8
                  h = (0,0,0,0,0,0)               bg                                                                    h                                       bg

104                                                                                                               104

1000                                                                                                              1000

100                                                                                                               100

 10                                                                           C1(x)                                            C1(x)
                                                                              Ctwisted(x)
   1                                                                          C(x) = C1(x) + Ctwisted(x)          10           Ctwisted(x)
           0.1
                                                                                                                               C(x) = C1(x) + Ctwisted(x)

                                                         0.2                  0.3  0.4  0.5                       1                                                      0.2                             0.3  0.4  0.5
                                                                                                                          0.1
                                                                x
                                                                                                                                                                                        x

105               =    1  ,  1  ,  1  ,  1  ,0,0      =  0,0,0,0,  1  ,  1                                        105          =    1   ,  1  ,  1  ,  1  ,0,0      =    0,0,0,0,             3  ,  1  
                       2     2     2     2                         8     8                                                          2      2     2     2                                      8     8
         h                                        bg                                                                    h                                       bg

104                                                                                                               104

1000                                                                                                              1000            C1(x)

100                                                                                                                               Ctwisted(x)

                     C1(x)                                                                                        100

                                                                                                                                  C(x) = C1(x) + Ctwisted(x)

     10              Ctwisted(x)                                                                                  10

                     C(x) = C1(x) + Ctwisted(x)

     1                                                   0.2                  0.3  0.4  0.5                       1                                                      0.2                             0.3  0.4  0.5
             0.1                                                                                                          0.1

                                                              x                                                                                                                         x

Figure 11. Plots of the Casimir energy computed numerically for different choices of spin structures
h and shift vectors bg. In the top row we see the effect of untwisting the C4 fibre boundary conditions
for the gravitino (left), showing that the boundary conditions around the fibre must be twisted for a
minimum to exist; we also show that choosing the only other allowed shift vector bg (5.17) along the
fibre does not affect the results. In the bottom row, we show different choices of shift vector along
the base T 2, and verify that while they preserve the minimum for C(x), the corresponding Casimir

coefficient Cmin(x) will be smaller.

5.3 Flux potential

We will now determine the flux piece VG4 of the scalar potential (5.1). In our setup, this
comes entirely from M-theory G4 flux. The G4 kinetic term is proportional to the Hodge

                                                                                                          � 56 �
norm |G4|2, so we will compute that first. We must take into account that G4 is quantized,

                                            G4  Z ,  C4  H4(F6, Z) .                  (5.31)

                                                         C4

Using Poincar�e duality, this can be equivalently rewritten as

                    G4  Z ,    H2(F6, Z) .                                            (5.32)

               F6

If we choose a basis {i} of H2(F6, Z), we may satisfy (5.31) and (5.32) by expanding G4 in
terms of the Hodge-dual forms {i} (which will not, in general, have quantized periods) as

               G4 = ni Gi-j1  j , ni  Z ,                                             (5.33)

                          i,j

where we have defined            Gij  i  j .                                          (5.34)
With these definitions, we have
                                              F6

                                     |G4|2 = Gi-j1 ninj .                             (5.35)

                                 F6  i,j

The only task left is to determine the Hodge norm acting on 2-forms (5.34). To do this, we
must construct a basis of H2(F6, Z). Because of the natural projection map p : T 6  F6, we
may work instead in the covering T 6. We have

                                 1      p(i)  p(j) ,                                  (5.36)
               F6 i  j = 8
                                     T6

where the factor of 1/8 appears because the fundamental class of F6 pulls back to 8 times
the fundamental class of T 6, so the Hodge duals in T 6 are rescaled by a factor of 1/8 with
respect to Hodge duals in F6 (in other words, T 6 is an eightfold covering of F6, which can
be identified with a subset of T 6 with 1/8 its volume). The pullback p(i)  H2(T 6, Z) is
represented by a 2-form on T 6 invariant under the action (5.3). Out of the fifteen 2-cycles of
T 6, only a three-dimensional subspace is invariant under (5.3), generated by the 2-forms

1  dz1  dz2 + dz1  dz4 + dz2  dz3 + dz3  dz4 - dz1  dz3 - dz2  dz4 ,

2  dz1  dz2 + dz1  dz4 + dz2  dz3 + dz3  dz4 - 2dz1  dz3 - 2dz2  dz4 ,

3  dz5  dz6 .                                                                         (5.37)

Furthermore, the forms i are all invariant under (5.8) and transform under (5.10) as

               1  1, 2  -2, 3  3,                                                     (5.38)

                                     � 57 �
This means that if the 2 piece of G4-flux vanishes, the flux potential will respect both
symmetries used in Subsection 5.1 to ensure a saddle along ,  and .

     The pullback pH2(F6, Z) is a sublattice of the invariant subspace generated by the
i. To determine this sublattice, we can recall that classes in H2(X, Z) are in one-to-one
correspondence (via the Chern class) with U (1) bundles over X. These, in turn, are fully
characterized by the field-strength F of the gauge bundle (an element of H2(X, R)) and by

the holonomies

                                                 W () = exp 2i A                     (5.39)


of the gauge field A evaluated on any closed line  23. The quantity W () must be a well-

defined function from the space of closed lines of X to U (1), and this condition can be used
to determine a basis of H2(X, Z) in terms of differential forms. We will first illustrate how
this is done for T 6. A gauge field in R6 can be expanded into 1-forms A = A � dz and
there are no identifications since all bundles on R6 are trivial. The holonomies (5.39) can be

written as integrals of a field-strength and are all well-defined. When passing to the quotient
T 6  R6/Z6, we must impose the well-definedness of W () for any 1-cycle in the torus. These
are parametrized as  = z0 + t n where t  [0, 1) and n  Z6. Without loss of generality,
we will restrict to gauge fields where the components are linear, so that A = F � z with F
antisymmetric24. The holonomy is W () = exp (2 i n � F � z0), and for it to be a well-defined

function on the torus it must be invariant under shifts by lattice vectors z0  z0 + m , or in

other words that

                                                        n � F � m  Z ,               (5.40)

which is the familiar quantization condition. The only difference in the case of F6 is that the
Z8 quotient introduces additional identifications, z0  Djg z0 + j bg, and additional 1-cycles,

parametrized as

                                 1 = (1 - t)z0 + t (Dgj z0 + j bg) t  [0, 1) .       (5.41)

The corresponding condition is that the quantity

                                 [(Dgl z0 + lbg + n)] � F � [(Djg - I) z0 + j bg] ,  (5.42)

is independent of k, l, n. Taking F to be invariant under the Z8, and using that bg is in our
case invariant under Dg, turns the above into the condition

                                                        n � F � bg  Z ,              (5.43)

which is what we need to determine the sublattice pH2(F6, Z): it is generated by 1, 2 and

  23From a math point of view, this characterization comes from the long exact sequence . . .  H1(X, U (1)) 
H2(X, Z)  H2(X, R)  . . . arising from the short exact sequence 1  Z  R  R/Z = U (1)  1. The

map sending holonomies to the corresponding Chern class is an example of a Bockstein homomorphism, see

e.g [136] for some more details.

24So  that  it  is  represented  as  1  Fij dzi    dzj  in  form  notation.
                                     2

                                                            � 58 �
8 3. Notice that the forms 1, 2 are fully localized along the T 4 fiber, while 3 lies along the
base; the result we just obtained then matches an intuitive picture where F6 is identified with
a fundamental domain for the Z8 action; since it acts freely on cycles along the fiber, forms
which were integer-quantized and located along the fiber still have integer periods. However,

the 2-cycle along the base is replaced by a domain with 1/8 its volume, so proper quantization

requires us to rescale 3 by a factor of 8.

We can now determine the metric Gij using (5.36), which gives Gij = Vol(F6) i ij. The

orthogonality is due to the fact that 1, 2 have different eigenvalues25 with respect to (5.10).

We have                                   1                2                        64

                     1 = R24 , 2 = R24 , 3 = R14 .                                                       (5.44)

Using (5.35), we finally arrive to our flux potential,

                         |G4|2               =      1    4n12x4/3     +       n23          .             (5.45)
                                                   R2                       16x8/3
                     F6

where we have set the piece proportional to 2 to zero already. As we will see in the next
subsection, the factor of 16 in the denominator of (5.45), which comes from the effect of the
Z8 quotient involved in defining F6, is an example of yet another boon of RFM's: the quotient
decreases the flux quantum allowing for finer choices of flux that lead to more vacua in the
parent torus.

5.4 The dS5 maximum

We can now combine the results of Subsections 5.2 and 5.3 to obtain the scalar potential.
The M-theory flux potential for the reduction on F6 is (see Appendix A)

                 (22)    1                |G4|2          (2  2  )  1     4n12x4/3            n32
                         3                                         3                       16x8/3
         VG4 = 2131                                   =                                 +             .  (5.46)
                                                         2R2131
                            F6

We see that VG4 has dimensions of length-5, as befits a five-dimensional energy density. We
will now set 11 = 1 and add the Casimir term (5.21), to construct the total scalar potential
(5.1) explictly as a function of the moduli,

                     10     (2               2  )  1                       n23             C(x)
                     23                            3                     16x8/3         - 4 R5
         V (5d)  =   R10                               4n21x4/3       +                            .     (5.47)
                                          2R2

                             2(2+2)                                              

25The more general result for  = 0 is  (2-2)2R24           -  (    2   8    R24

                                                                      -2)2       .  We see that a linear, off-diagonal term

                                                    8         4( 2 +2)

                                          -  ( 2 -2)2 R24  ( 2 -2)2 R24

proportional to  appears, which is due to the fact that (5.10) is no longer an isometry, and the invariant

subspaces no longer have to be orthogonal. Thus, when an 2 flux piece is turned on, the potential no longer

has a saddle for  = 0 in the  direction.

                                                       � 59 �
We also included an overall Weyl rescalling factor, required to go to Einstein frame in 5d. All
that is left to do is to find extrema of this potential--denoting by C the first derivative of C
with respect to x, the extremum conditions are

                                    R3   =      C     �      10x8/3      n32  ,                     (5.48a)
                                            (22)1/3      64n21 x4 +                                 (5.48b)

                              x C        =  10  �     32n21 x4 - n32  .
                               C            3         64n21 x4 + n32

     We want to find the solution with the biggest possible R, since this will give us the most
control. It is clear from the R equation (5.48a) that we want the largest possible C(x) and
the smallest allowed fluxes--this is where the large contribution of the twisted sector becomes
key. We find solutions for either n1 = 0 or n3 = 0, since the x equation (5.48b) reduces to

                              x C(x) 10               and            x C(x) 5
                                       =-                                     =,
                              C(x)          3                         C(x) 3

respectively,  and  we  know  from  the  asymptotics     of   C(x)    that  x C(x)    -  11  ,  10  . For non-zero
                                                                              C(x)       3      3

n1 and n3, we could also find a critical point close to the Casimir potential extremum C  0

as long as n32  32n21x4, and thus

                              R3         C(xmax) 10                      3034    .                  (5.49)
                                                                          n12
                                         (22    )  1  96n12 xm4/a3x
                                                   3

We want to choose n1 as small as possible, while still making sure that both n1 and n3 
4 2 n1 x2max  0.15 n1 are integers. For example, when n1 = 7 , n3 = 1, which gives R  4.

               n1 n3 R              x       1  R1                     vol(F6)         Vsaddle
                                            8           2 R2

               0 1 5.45 0.105 3.06 3.64 6.59 � 103 9.99 � 10-8

               1 0 16.2 0.191 6.11 13.18 4.50 � 106 3.68 � 10-15

               7 1 4.00 0.166 1.65 3.12 1.03 � 103 4.06 � 10-6

Table 1. Choices of fluxes leading to the smallest values of the vacuum energy. We also list the
length of the smallest curves in the base and fiber of F6, in 11-dimensional Planck units, as well as
the volume of the space; the vacuum energy is given in 5-dimensional Planck units.

     By scanning more systematically over (n1, n3), we conclude that the best solution (as

shown in Table 1)--the one that is best controlled--is found for the choice of fluxes n1 = 1,
n3 = 0, for which the vacuum energy is Vsaddle = 3.68 � 10-15 5-5. This is a factor of 109 better
than the na�ive T 4 solution in Section 226.

  26And still, it is not as good as one might have expected. The dS saddle we found arises as a balance of a
large twisted sector and a small untwisted one, to the effect that the actual saddle is at a not-so-large R. In
future work we will explore situations where the saddle comes from balancing two twisted sectors, where one
may expect much larger results.

                                                      � 60 �
     Table 1 also shows the values of the moduli R1 and R2. These are the radii of the covering
T 6, and as such, they do not directly measure the diameters of closed curves in F6. To get
these, notice that the smallest 1-cycles of F6 will be either entirely contained in the T 4 fiber or
in the T 2 base. Since the T 4 fiber is the C4 Cartan torus rescaled by R2, and the root lattice
of C4 is even, physical 1-cycles along the fiber have a minimal length of 2 R2. Similarly,
R1 is the size of the torus base--but the physical size of one of the sides of T 2 is eight times

smaller due to the Z8 quotient. Therefore, the sizes of physical closed curves on F6 are

                 R1        and                                          (5.50)
                  8                   2 R2 ,

which are the parameters quoted in Table 1.
     From the results of the table we see that, although the value of the vacuum energy is much

improved with respect to the solution in Section 2, the size of the torus is still Planckian--
which again raises issues of control. We now turn to a systematic discussion of these issues.

5.5 Characterization and control of the solutions

       "A common mistake that people make when trying to design something
     completely foolproof is to underestimate the ingenuity of complete fools."

                               Douglas Adams, A Hitchhiker's Guide to the Galaxy

     The solution with n1 = 1 in Table 1 is the most interesting one--it has a very small
vacuum energy of 10-15 in five-dimensional Planck units, and radii which are one order of

magnitude larger than what we obtained in Section 2. We will now provide some more details

about this solution, and discuss at length just how under control it is.
     We will first determine the spectrum of light fields and masses around the VSaddle  10-15

solution, since the smaller value of the vacuum energy makes it far more interesting than the

others. To compute these masses, we need the properly normalized kinetic terms of the

moduli in RFM's. Since these are all quotients of tori, the kinetic terms from dimensional
reduction of the (D = d + k)�dimensional theory on T k are enough.

     Just like in Section 3, we will parametrize the moduli of T k by the k � k inner product
matrix G that describes the inner product when the torus lattice is just Zk, an n � n matrix
M whose columns are the vectors spanning the torus lattice. The kinetic terms of the moduli
coming from the Einstein-Hilbert action on T k are [137]

 1   ddx         D-2       (d  log         G))2    +  1 Tr((G-1G)2)  .  (5.51)
22d         -gd                       det
                 k(d - 2)                             4

One can check that this gives e.g. the standard metric on the upper half-plane for the case of
T 2, agreeing e.g. with (4.9) of [137] and Appendix A of [138] for the canonical normalization of
the volume modulus of T k, which is precisely det G. Using these, it is possible to determine

                           � 61 �
the mass of the moduli fields {R, x, , , } from the eigenvalues of the Hessian normalized
with respect to the proper kinetic term. They are

                  {90.45 , 23.82 , -309.55 , -47.43 , -45.16} � H02 ,  (5.52)

so that our solution is a stable minimum along two directions and an unstable maximum

along the remaining three. The masses acquired by the five moduli are of the order of the

Hubble scale H0  2.48 � 10-8 MP(5l) (5.57).
     On top of these geometric moduli, we also get two KK vectors from the base T 2, and

additional fields from the dimensional reduction of C3, the RR axion. The free part of the

F6 cohomology is

                       p 01 2 3 4 56                                   (5.53)
                  Hp(F6, R) R 2R 3R 4R 3R 2R R

so from dimensional reduction of C3 we get another five vectors and five axions, four from
C3 periods and another one from the five-dimensional dual of C3 with no legs on T 6. All of
these fields are massless to a first approximation; the axions constitute compact directions
of the moduli space, which receive a non-perturbative potential due to M2 and M5 brane
instantons [139]. We will study this potential in detail in the next section; while we have
not computed their exact minimum, the smallness of the potential together with the compact
range of the scalars ensures that they give a negligible correction to the solution, and can be
treated in practice as a moduli space. The shift symmetry of the axions ensures that there
are no perturbative corrections [140]. In some cases, one can use the parity symmetry of
M-theory to ensure that the exact C3-axion potential will have a minimum at zero; it is not
possible to do this for all five components of the axion fields in this case, due to the G4 flux
that breaks some of these parity symmetries.

     The fact that we have a dS solution with masssless vector fields means that we could
check the Festina Lente bound [141]. This is a proposed dS Swampland condition setting
a lower bound on the mass of charged states under any U (1) gauge field, stating that the
masses of all charged states must satisfy

                  m2  g q H,                                           (5.54)
                            G

in terms of the Hubble scale, the gauge coupling g, the integer quantized charge q of the
particle, and Newton's constant G. Although the arguments supporting the bound do not
work for dS maxima [141, 142], it is perhaps interesting that (5.54) is satisfied nonetheless. For
the two KK photons, the content of the FL bound is equivalent to the statement mKK  V 1/2
[142]; as we have seen, this is satisfied in our vacuum. For the vectors obtained from C3, we
know that the charged states obtained from M2 and M5 branes saturate the Weak Gravity
Conjecture, so m  gMp and (5.54) becomes the statement g/ G  H. In terms of 11-

                  � 62 �
dimensional quantities, we have

                                  g     Vol(2)     R2     H  ,                       (5.55)
                                           311     131

                                   G

for electric C3 vectors (those that come from reduction of C3 with two legs on F6), where
Vol(2) is the volume of the 2-cycle corresponding to the C3 vector field under consideration.
Therefore, FL is satisfied in this case. We should also consider magnetic vectors, obtained
from dimensional reduction of the dual potential C6 on a five-cycle of F6. In this case, the
electrically charged object is an M5 brane wrapping this same five-cycle, leading to

                                  g     Vol(5)     R5     H,                         (5.56)
                                           611     161

                                   G

so FL is satisified for these gauge fields as well.
     Finally, there are no light fermions in our solution, since F6 is the quotient of a T 6 where

we have chosen an antiperiodic spin structure around four of the six 1-cycles. This means
that the Dirac operator has no zero modes, nor does the Rarita-Schwinger field since the
tangent bundle of T 6 is flat. As a result, our five-dimensional 5d theory is purely bosonic,
even though we started with a maximally supersymmetric theory in 11 dimensions.

     Having described the EFT, we now turn to the values of the parameters involved in it.
With such a small vacuum energy, the dS radius is

H0-1 =                                     6       4.04 � 107 5 .                    (5.57)
                                        VSaddle

The ratio of the 5d and 11d Planck lengths is

                                 11 = R2  165.14 ,                                   (5.58)
                                 5 41/3

so the solution is very much scale separated (like the AdS example of [80]), and the five-
dimensional EFT is valid for a large range of energies--up to, roughly, 6 � 10-3 MP(5).

     We now turn to the question of just how under control the solution is. The average

energy density of the 11-dimensional solution, obtained by dividing the 5d vacuum energy by

the volume of the internal manifold, is

                                 11d = 1.00 � 10-10 -1111 ,                          (5.59)

which arises as a balance of a flux and Casimir terms each of which is, on average,

Cas  -4.02 � 10-10-1111 G4  5.02 � 10-10 1-111 .                                     (5.60)

We see that the 11-dimensional energy densities are very small; in fact, this small number

                                        � 63 �
coincides with the  of the iterative approach to solving Einstein's equations discussed in
Section 2, which means that the leading-order curvatures go like 10-10, too. Taken together,
this means that any higher-derivative correction to the action of the schematic form

P (R�, |G4|),            (5.61)

where P is some polynomial, will be suppressed by powers of 10-10. While we do not know
the coefficients in front of these higher derivative corrections (save for a few cases [89�93]),
we expect them to become smaller and smaller as corrections get larger; in fact, if we assume
that 11d supergravity has a cutoff  (which we would naturally expect to appear at or around
the 11d Planck scale), then [143] would imply that coefficients of higher-derivative operators
cannot be more than O(1) in units of the cutoff to ensure unitarity of the S-matrix (although,
strictly speaking, we are outside of the regime of validity of this result, since M-theory is not
weakly coupled at the cutoff scale); as a result, the solution we found seems quite safe under
na�ive higher-derivative and classical corrections, at least at the homogeneous level. In this
regard, it is quite important that the RFM does not contain a non-trivial tadpole equation
that would force higher-derivative terms to be a relevant part of the classical solution, avoiding
an important subtlety present in standard flux compactifications [71].

     We must also analyze whether our solution has inhomogeneites that are strong enough to
invalidate the above analysis; for instance, if the internal profile on F6 of the energy density
has very steep gradients, these will show up in corrections like (5.61), and will affect the
estimate of , which was roughly speaking the maximum value of the energy density on the
internal space. To leading order, the flux term yields a homogeneous 11-dimensional energy
density, so we do not have to worry about it. However, this is not so for the Casimir term; as
we saw in Section 4, the energy density coalesces around the location of the Casimir branes.
In our case, we therefore expect a Casimir energy profile that is homogeneous along the
directions of the base T 2, but inhomogeneous on the fiber T 4. From (4.25), we can estimate
the inhomogeneities in the Casimir energy by evaluating the energy density at the origin,
where a Casimir brane is located, which is

^(0)  1.28 � 10-9 -1111  (5.62)

This is certainly larger than the average value (5.60), and we should update our estimate of
the control parameter to 10-9, but it is still very small, so all the arguments above still apply.
To estimate the average gradient of the Casimir energy, we can also estimate ^ far away
from a Casimir brane, which is of order 10-13 -- smaller than the average by two orders of
magnitude, as expected. Thus, while there is up to four orders of magnitude inhomogeneity in
the Casimir energy, the gradients are still very small in Planck units. In particular, they are
much smaller than 1/R, so the effective field theory is under control. Had this not been the
case, all the KK modes of the internal space (including KK copies of T 6 moduli frozen by the
Z8 quotient) would have been excited, ruining the solution. In other words, we have shown

� 64 �
that internal space inhomogeneities do not ruin the na�ive scale separation we obtained27.
     What about higher loop corrections? Since our solution relies on an unexpectedly large

Casimir coefficient, one might wonder whether higher-order loops can be even larger, thereby
destroying the solution28. On dimensional grounds, the loop expansion of the Casimir energy
(in 11d Planck units) is of the form

           1              11 9l ,  (5.63)
VCas  4R5                 R
              C + Ci

                     l=1

where the power of 11 is determined by the fact that the loop expansion in M-theory is in
powers of Newton's constant G  191. Our Casimir coefficient, C, is just the leading one in an
infinite series. The higher-order Casimir coefficients Ci will come from divergent loop integrals
requiring regularization, unlike C, since at higher loops there are unprotected higher-derivative
terms in the M-theory action that can contribute to the vacuum energy. The question is then
whether the higher-order effects in (5.63) can spoil our solution. However, even though the
Casimir coefficient is large, the overall contribution of the Casimir energy is quite small in
11-dimensional Planck units, since R  16.1 11. This is why we obtained a Hubble radius as
large as (5.57); it was necessary in order to argue stability against classical corrections, and
it means that the loop counting parameter in (5.63) is

11            9                    (5.64)

R                1.31 � 10-11 .

This is comparable to the classical parameter  controlling classical corrections, and it means
that, in order to overcome the classical contribution C  106 to the Casimir energy, the higher
Casimir coefficients would have to satisfy

    Ci  106+11l.                   (5.65)

While we have not computed the coefficients Ci, the estimate (5.65) is reassuring. It means
that, even if the Ci are enhanced in the same way that C0 was, they still have to beat a
factor (5.64) of loop suppression to significantly affect the solution. In other words, since
11d is small in Planck units, the configuration is quite classical, and quantum corrections are
expected to be smaller still. Nevertheless, it would be nice to check the above via a smart
estimate of the coefficients Ci, for which explicit expressions as sums over the KK spectrum
can be obtained.

     An important point is that our solution is a perturbative expansion around a static,
classical solution of the equations of motion (the RFM), and as such, we expect correc-

  27This is something that we cannot do conclusively for some supersymmetric solutions, such as DGKT [49],
due to the presence of singularities in the internal space. All of that is avoided here, since the Casimir branes
are smooth, with a core profile that we have determined explicitly.

  28We thank A. Hebecker for bringing up this point.

              � 65 �
tions to be convergent when computed around the true static vacuum. This contrasts with
what happens in more general, time-dependent situations [71, 144�147]. For instance, in a
non-supersymmetric model with open strings, the one-loop vacuum energy diverges when
computed at constant dilaton [82, 147], reflecting the fact that a constant  is not a solution
of the classical equations of motion. In our case, the one-loop calculation is finite since the
RFM is a solution to the classical equations of motion. Were we to compute the higher Ci, we
would have to do it in an iterative process where the (n + 1)-loop calculation is done around
an n-loop corrected vacuum. For instance, the two-loop Casimir energy will diverge unless
computed at the precise point of moduli space where we found a one-loop maximum. While
they certainly complicate a detailed treatment, these are all standard issues and we do not
view them as a fundamental obstacle to finding a corrected solution.

     If the solution is safe from loop and higher-derivative corrections, what about non-
perturbative effects? In M-theory, well-known non-perturbative effects come from Euclidean
M2 and M5 branes wrapping cycles of F6. Using the formulae of Appendix A, we can estimate
the size of these effects as

          e-SM2  e-TM2       R1 R22   e-716.9 ,            e-SM5        e-TM5  R6   e-5.24�106 ,       (5.66)
                                4                                               4

so they are completely negligible.

    Since our solution is non-supersymmetric, we may also have to worry about other non-

perturbative effects, such as e.g. gravitational instantons. Any instanton which may be

described by 11d supergravity would have, on dimensional grounds, an action scaling as

(R 11)11, and therefore would be even more suppressed than the M2, M5 branes described

above.

    So it seems that the solution is stable against higher-derivative, classical, and quantum

corrections! How does this square with the natural instinct that one should not trust a

solution  whose  smallest    physical   closed  curve  is  just  1  R1    6.1 11?  Even  if  all  the  corrections
                                                                 8

we know are under control, we must also worry about unknown ones. More concretely, the

analysis here has pushed 11-dimensional supergravity all the way to a few Planck lengths.

We do not know if this is correct: there could be e.g. additional, non-supersymmetric states,

not controlled by supergravity, appearing at a mass scale �  M11. If such states exist, they
are necessarily non-supersymmetric, but we have no evidence that this is in fact the case--it

is just a worry at this point. In fact, if � is close to M11, they could be thought of as "small"

quantum-mechanical black holes. On general grounds, we expect such objects to exist in the

theory. In at least one class of examples, that of AdS3 quantum gravity, where there is more

control, we know that there are BTZ black hole states with � = 1/(8G), and every quantum

gravity in AdS3 must have at least one operator other than the graviton with �  3/(32 G)

[148]. To estimate      the  effect of  such particles, we will pretend the compactification is on a
                        and     2 R2.   Since R2 > R1, we will first compactify on the small circle
T5  with  radii  1  R1
                 8

and integrate the resulting vacuum energy over the large T 4. A particle with mass �  1/R1

                                                 � 66 �
would then be expected to yield a contribution to the 5d vacuum energy of the form [36]

                       V (5d)  =          3  R6       2�11 K 11 (�nR1)                .                  (5.67)
                                              4                                    2
                                      2 10
                                      R10                     11            11
                                                  n=1 (2) 2 (�nR1) 2

Even for � = 1 we have V (5d)  1.8 � 10-16, which is still a factor of 20 smaller than our

result. Actually, this value is not so far from the �  0 limit, in which the above becomes

just another contribution to the vacuum energy of an additional massless field, contributing

an amount comparable to our final result. In either case, we get that one very light additional

light state or e.g.  20 states at � = 1 might have a contribution large enough to significantly

impact our solution.

    However, estimating the effect of these states via (5.67) like this neglects the fact that the

spin structure is periodic along the circle of radius R1; because of this, we expect approximate

Bose-Fermi cancellation even at the level of M-theory Planckian black hole microstates. Under

these circumstances, it is more appropriate to first reduce to 10d on the supersymmetric circle,

and consider the contribution of 11d black holes after compactifying on a non-supersymmetric

T 4. In practice, this amounts (up to O(1) factors) to replacing R1  R2 in the above formula.
In this case, the contribution of a �  1 black hole is 10-22. We would need 107 such black

hole microstates to even begin to affect our solution, which contrast with the expectation

that a Planckian black hole has O(1) entropy--but we do not know for sure.

    The comments above also apply to e.g. string states, that may arise from wrapping an

M2  brane  along  the  small  circle  of  radius  1  R1.  If  the  radius   was       subplanckian,  we  would  be
                                                  8

in the type IIA regime, and the wound M2 states would give us perturbative string states.

Since our radius is slightly superplanckian instead, we are in the M-theory regime, and the

states are heavy; the associated mass scale is

                                             (22)1/3 R1            16.48 ,                               (5.68)
                                        T                 8

so the wound M2 states are heavier than the black hole states we considered above, and
are therefore more suppressed. In fact, since the string is so heavy, these string states will
automatically be within the Schwarzschild radius, and therefore, they are part of the black
hole spectrum we estimated.

     In any case, there are many subtleties in estimating the effect of these Planckian states:
what is the effect of including interactions, what is the lifetime of these states (they would
not contribute if they are extremely short-lived), are we even allowed to run black holes in
loops in the na�ive way that we just did. Furthermore, there are other possibilities we do not
know how to even begin to quantify properly. Suppose (again along one of the lines in [71])
that someone comes and tells us they have discovered an exotic gravitational instanton in M-
theory, with a singular core (so that its action cannot be reliably computed by supergravity),
and that its action is small enough to destabilize our solution. We cannot rigorously rule
out such possibility (although if true, it would have implications far beyond our solution, as

                                                  � 67 �
it would mean the presence of unexpectedly light instantons in M-theory compactifications).

The punchline is that, although things seem fine in the crude analysis we just did, we do not

have a way to control corrections such as those in equation (5.67), since we do not know the

spectrum of metastable Planckian states in M-theory. To some extent, this aligns with the

intuition  that  1  R1   6.1 11  is  dangerous.
                 8

Absent new windows into non-perturbative M-theory, there is no way to ensure our

solution is protected against these "black hole loops". The solution might actually be there,

or it might not. On the other hand, we did achieve a huge improvement over the solution

in Section 2. We see the RFM compactification studied here as a proof of principle, which

illustrates that this not so well-known corner of the String Landscape may harbor hidden

gems. Perhaps, by choosing a better RFM in one setup or another, we can push the size of

the internal manifold to a regime where we feel safer from black hole and exotic states.

5.6 The dS5 � F6 vacuum of M-theory: An executive summary

The main point of this section--and of the whole paper--is that we achieved a dS5 � F6
solution of 11-dimensional supergravity, where

                                     F6 = T 6/Z8         (5.69)

is a quotient of T 6 by a fixed-point free Z8 isometry that breaks all supersymmetries. Casimir
energies and G4 flux balance each other to produce a classical maximum. The vacuum energy
is small in Planck units, the masses of tachyons and other light fields are of order Hubble
scale, the solution is scale separated, and is protected against all known higher-derivative,
loop, and classical corrections. We summarize some salient features of the solution in Table
2 for rapid reference, with pointers to parts of the paper that discuss each of these in more
detail.

                                                 � 68 �
        Property                              Value                                 Comments                                            Details in . . .

        5d vacuum energy         V (5d)  3.68 � 10-155-3                            Quite small due to large                            Subsections 5.4, 5.5
                                                                                      Casimir coefficient C

        Hubble radius            H0-1  4.04 � 107 5 = 2.45 � 105 11                          11/5  165.14                               Subsection 5.5
                                                                                    (species vs. 5d Planck scales)

        Internal space volume    V = 4.50 � 106 611 = 9.1 � 1019 56                 Large volume helps with control                     Subsections 5.4, 5.5
        Internal manifold radii                                                         Potential impact of black                       Subsections 5.4, 5.5
                                   1  R1    6.1  11  =    1009  5,
            Scale separation                                                         hole-like states due to small Ri                      Subsection 5.5
           Geometric moduli      8                                                     Facilitates 5d EFT validity                         Subsection 5.5
                                 2 R2  13.2 11 = 2176 5                                                                                    Subsection 5.5
                  Axions                                                              All masses light, of order H02;
                                 Yes:  1  R1  =  2.50  �  10-5  H0-1                         complies with [10]
                                       8
                                                                                    Generated by Euclidean M2, M5
                                 Five, with masses m2i =

� 69 �                           {90.45 , 23.82 , -309.55 , -47.43 , -45.16} � H02

                                 Five, with negligible masses

        Vectors                  Seven: two KK photons, five from C3                Exactly massless                                    Subsection 5.5

        Light fermions                        None                                  Due to antiperiodic spin                            Subsection 5.5
                                                                                    structure in covering T 6

         11d average             11d = 1.00 � 10-101-111                            Control parameter for corrections Subsections 2, 5.5
        energy density

           Flux & Casimir        Cas  -4.02 � 10-10 1-111, G4  5.02 � 10-10 -1111 Each contribution larger than 11d;                    Subsection 5.5
        contributions to 11d                                                                                 they partially cancel out

        Internal gradients                11d2  10-9                                  Larger than average, but                          Subsection 5.5
                                                                                    much smaller than KK scale

        Table 2. Summary of some properties of the dS5 � F6 solution we found. Here 11 is the 11-dimensional reduced Planck length, defined by
        121 = 191, and 5 is the five-dimensional reduced Planck length, analogously defined.
6 A scan for M-theory dS4 maxima

As mentioned in Section 3, we will focus on cyclic RFM's. The reason for this is twofold--on
the one hand the group  for cyclic RFM's has a single generator, which makes the explicit
computation of the Casimir energies more tractable and expressible in terms of that generator
alone; on the other hand, it also allows us to scan a family of RFM's, since a full set of cyclic
RFM's can be obtained for a given dimension.

6.1 Cyclic Riemann-flat manifolds in 7d
Consider the compactification of M-theory down to 4d, which requires a 7-dimensional RFM,

                                                  T7                            (6.1)
                                           F7 =  .

We know that M-theory on F7 will not admit a dS4 minimum, since we are not allowed to
turn on both G4 and G7 fluxes without causing a runaway for an axion that descends from
C3 [54]. Here instead we will look for a maximum, as discussed in previous sections.

     Recall that we want the RFM to contribute in two key ways: we want it to freeze as
many geometric moduli as possible and to enhance the Casimir energy contribution. While
the former follows directly from the Dg associated with the single generator g of the cyclic
group , the latter requires a choice of spin structure that avoids cancellations between boson
and fermion contributions. In choosing F7, we must therefore look for the number of moduli
and allowed spin structures of all 7d RFM's generated by a cyclic group , which for RFM's
with an S1 base have generators of the form29

g : Dg =                                   A0      ,bg =         0           ,  (6.2)
                                           01                  |A|-1

for finite order 6 � 6 matrices A, i.e. An = I for some finite n. To classify these we will

follow standard techniques; see [149] for a more detailed explanation and the results of interest

in our case. The smallest such n gives the order of A, which we denote as |A|. Any finite
matrix must have a minimal polynomial mA(x) that divides both xn - 1 and its characteristic
polynomial (cf. Cayley�Hamilton theorem), so that a large class of finite order matrices30
A  GL(6, Z) can be obtained by factorising xn-1 into cyclotomic polynomials31 and building

  29As explained in Section 3, we can generalise the shift vector bg to any vector such that Dg bg = bg mod Z
and nbg  Z7 = n  |A| (3.14). Here we restrict to the simplest case, as this does not affect any of the

conclusions of this section.
  30These matrices correspond to the torsion elements of GL(6, Z).
  31The nth cyclotomic polynomial is the unique irreducible polynomial with integer coefficients that is a

divisor of xn - 1 and does not divide xk - 1 for any k < n. It is given by

                                           n(x) =       (x  -  e2i  k  )  ,
                                                                    n

                                                   1kn

with gcd(k, n) = 1, i.e. k and n coprime.

                                                   � 70 �
matrices A that are direct sums of the companion matrices of these cyclotomic polynomials
[150] (the precise statement is that any matrix of finite order and integer entries is conjugate
over SL(6, Q) to one of the matrices we construct here). We must therefore look for all
possible products of cyclotomic polynomials n(x) whose degrees--given by Euler's totient
function (n)--add up to 6.

     Let us illustrate this with a concrete example that will be relevant in what follows. The
cyclotomic polynomial 7(x) has degree 6 and has companion matrix A such that A7 -I = 0,
i.e. an order 7 matrix. This matrix can be used to define a 7d RFM with S1 base whose
quotient group  = Z7 is generated by

                                    0 0 0 0 0 -1 0                              0

                                    1 0 0 0 0 -1 0                              0

                                      0  1  0  0   0 -1    0                       0  


                           Dg   =     0  0  1  0   0  -1   0    ,      bg    =     0    .                      (6.3)


                                      0  0  0  1   0 -1    0                       0  


                                      0  0  0  0   1 -1    0                       0  


                                      0000001                                      1
                                                                                   7

The condition G � Dg = (DgT )-1 � G (3.17) leaves 4 invariant moduli and (I - Dg)T �h  Z7

(3.22)  only  allows  for  the  spin  structure h  =  (0, ..., 0, h7)  with  h7    {0,  1  }.  We  will  come  back
                                                                                        2

to this example shortly.

Since (5) + (6) = 6, a less direct example is a block diagonal matrix whose blocks are

the companion matrices of 5(x) and 6(x), which has order lcm(5, 6) = 30 and can be used
to define a 7d RFM with base S1 and holonomy group  = Z30 generated by

                                    0 0 0 -1 0 0 0                              0

                                    1 0 0 -1 0 0 0                              0

                                      0  1  0 -1 0    0    0                       0  


                      Dg       =      0  0  1 -1 0    0    0    ,      bg  =       0       .                   (6.4)


                                      0  0  0  0   0 -1    0                       0  


                                   0 0 0 0 1 1 0                                0

                                      0000001                                     1
                                                                                  30

Note that this is not the only order 30 matrix that we can build, since (3) + (10) =
(6) + (10) = 6 and lcm(3, 10) = lcm(6, 10) = lcm(5, 6) = 30. All of these leave 4 invariant
moduli and only allow for periodic spin structures, due to the constraints (3.22) and (3.23).

     From all combinations of n(x) such that (n) = 6, one can build in this way 78
finite matrices A that correspond to generators of finite groups  and therefore cyclic RFM's
(including the identity, i.e. the trivial group). We will say that cyclic RFM's of this form are
of diagonal type. In Appendix G we summarise all 77 non-trivial cyclic diagonal RFM's with
base S1, giving their generators (Dg,bg), group order, number of moduli and allowed spin
structures. Generically, bigger groups tend to fix more moduli and to have more constrained
spin structures. It is also important to note the structure of the generator Dg--it always

                                                   � 71 �
contains at least two blocks (the base and the fibre), but in many cases it contains more.
In order to work with a 2-moduli potential and, in particular, a Casimir potential that only
depends on one modulus, we can look for enhanced symmetry points that allow us to fix some
of the remaining moduli at a point that is guaranteed to be a critical point of the potential, as
we did in Section 5.1. This will generally require the fibre to be a single block--that is the case
of the Z7 example, but not of the Z30 that always contains three blocks. Therefore, while the
T 7/Z7 compactification can be reduced to a 2-moduli problem, working with T 7/Z30 (which
could provide a bigger enhancement of the Casimir potential) will always require the study
of at least three moduli. Moreover, RFM's with more than two blocks will also have a richer
structure regarding their Casimir branes (i.e. the invariant subspaces under each element
in the group); for example, the Casimir energy on the Z30 quotient defined by (6.4) can be
seen as the sum over 200 codimension-five, 20 codimension-three, 10 codimension-one and 1
space-filling Casimir branes wrapping appropriate cycles of the RFM (for comparison, the Z7
quotient studied in the next subsection can be seen as the sum of a total of 42 codimension-
six and 1 space-filling Casimir branes). Since the behavior of the Casimir potential depends
crucially on the properties of the invariant subspaces, a proper study of these RFM's and
their potential saddles requires a detailed analysis of their Casimir brane structures.

     In order for a finite matrix A to be a single 6 � 6 block, the factorisation in terms of
cyclotomic polynomials must contain a single n(x) of degree 6. These matrices will then
be the order-n companion matrices of n(x) for each n such that (n) = 6; there are 4 such
cases, (7) = (9) = (14) = (18) = 6, which define RFM's that are Z7 , Z9 , Z14 and Z18
quotients of T 7 (see Appendix G). All these RFM's have invariant metrics G with 4 moduli
and, while the odd Z7 and Z9 quotients allow for the spin structures h = {0, 0, 0, 0, 0, 0, h7},
the even ones Z14 and Z18 are further constrained by (3.23) to have a periodic spin structure
along every cycle. As we will see explicitly for the Z7 case in the next subsection, the periodic
spin structure along the fibre does not allow for a critical point of the Casimir potential and
prevents us from finding a dS4 saddle point. This result can be extended to the Z9, Z14 and
Z18 quotients, as we will explain at the end of the section.

                                                         � 72 �
6.2 Example: F7 = T 7/Z7

Let us focus on F7 = T 7/Z7. The most general Riemann-flat metric on F7, i.e. a metric on
T 7 that is invariant under Dg, is

       2 R22  - R22             - -  - -                                 
                                                                      0

          -  R22  2 R22      - R22                                         
                                                 - -  - -  0 


                   - R22 2 R22  - R22                         - -     0  


G  =    -  -                 - R22 2 R22  - R22                       0  ,   (6.5)


                                       - R22         2 R22     - R22     
       - -  - -                                                       0


                  - -  - -                        - R22 2 R22         0  


          0          0          0          0         0           0 R12

which has 4 moduli {R1, R2, , }--out of the 28 moduli of T 7, the Z7 quotient has fixed 24.
     The metric (6.5) has a rather suggestive form--at the point  =  = 0 in moduli space,

the upper-left block is precisely the Cartan matrix of SU(7) (A6) rescaled by R22. As explained
in detail in Section 5.1, one may choose a transformation in the normalizer of Z7 that becomes
an isometry of the metric at this special point  =  = 0, therefore guaranteeing a critical

point of the potential along these directions.
     Consider the transformation z  Q z, with

                     1 0 0 0 0 0 0

                      1 -1 1 0 0 0 0 

                         1  -1     1  -1      1  0   0      


              Q   =      1  -1     1  -1      1  -1  0        ,              (6.6)


                         0  0      1  -1      1  -1  0      


                         0  0      0  0       1  -1  0      


                         0000001

which is a finite matrix of order 3. This transformation is in the normalizer of Z7, i.e. it
leaves the Z7 group invariant. The metric (6.5) is invariant under this transformation, i.e.
QT � G � Q = G, on the subspace with  =  = 0 and thus this becomes a Z3 isometry32.
Since the components of the gradient (V, V ) transform as a vector under this Z3, if our
choice of G4 flux respects this isometry we will necessarily have V = V = 0. Therefore,

  32In order to pick such a transformation Q, we can focus on the metric G we are aiming for: the Cartan
matrix of A6. One can pick a transformation that only leaves the subspace with  =  = 0 invariant from
the Weyl group of A6, i.e. the symmetric group S6, which is guaranteed to leave the Cartan matrix of A6
invariant. We must also check that such a Q belongs to the normalizer of Z7 in order for it to be a symmetry
of the RFM.

                                   � 73 �
at points in moduli space such that

              0 0 0 0 0 0 0                                       2 -1 0 0 0 0 0 

               0 0 0 0 0 0 0   -1 2 -1 0 0 0 0 

                   0  0  0      0    0      0    0                   0  -1      2  -1  0  0       0  


G     =  R12       0  0  0      0    0      0    0       +  R22      0  0 -1 2 -1 0               0         ,      (6.7)


                   0  0  0      0    0      0    0                   0  0       0  -1  2  -1      0  


              0 0 0 0 0 0 0                                       0 0 0 0 -1 2 0 

                   0000001                                           0000000

the potential is automatically a saddle along all directions apart from {R1, R2}.
     The Casimir potential can be written in terms of 7 sums over the covering T 7 lattice, one

for each element of Z7. Since we are dealing with a cyclic group, these elements are simply
(Dgj , j �bg), for j = 0, ..., 6, with D0g = I. Recall that the Casimir energy VCas on F7 = T 7/Z7
is given by,

                     (s)                             6           TrB(Dhj ) - TrF(Dgj ) � e2ih�n      ,             (6.8)
         VCas = - 2s �             d7z G            j=0            |(I - Dgj ) z - j bg + n|2s
                                                         nZ7
                                F7

with s = 11/2 for M-theory. The contribution of each group element (apart from the identity)
can be seen as the energy of seven Casimir branes localised at

                               654321 531642 415263                                                                (6.9)
         (0, 0, 0, 0, 0, 0), , , , , , , , , , , , , , , , , , ,

                               777777 777777 777777
            362514 246135 123456

             ,,,,, , ,,,,, , ,,,,,
            777777 777777 777777

on the T 6 fibre and wrapping the base S1, corresponding to the subspaces invariant under
Dg, i.e. Dg z = z mod Z7. The identity element contributes as a space-filling Casimir brane,
wrapping the whole of F7. Given the block diagonal structure of the invariant metric (6.7),
the norm splits into two pieces

VCas  =    (s)  �            �   6          d6z               TrB(Djg) - TrF(Djg) � e2i m h7                   s,  (6.10)
         - 2s        7R1R26     j=0
                      |Z7|              T7       nZ6        R22 |(I  -  Djg) z  + n|2  +  R12 |m  -  j  |2
                                                                                                     7
                                                 mZ

where we also split the 7d vector n into a 6d vector n along the fibre and 1d vector m = m
along the base, and used the only allowed spin structure on F7, h = (0, 0, 0, 0, 0, 0, h7).

Substituting in |Z7| = 7 and performing the change of variables

                                              R          R2 = R x1/7 ,                                             (6.11)
                                     R1 = x6/7 ,

                                                    � 74 �
the Casimir potential can be written as

                                        66         6                          TrB(Dgj ) - TrF(Dgj ) � e2i m h7

                (s) x 7                                    d6z
      VCas = - 2s     �                        �                                                                                s.     (6.12)
                           7 � R4 j=0                                                     Djg)                           j
                                                      T6         nZ6          x2  |(I  -           z  +  n|2  +   |m  -  7  |2

                                                                 mZ

Note that the constraint (3.23) correlates our choice of h7 with a choice of spin lift �Dg, since
Dg7 = (-1)sg I is such that

                                            sg = 2 � 7 h � bg mod 2Z = 2h7 mod 2Z .                                                    (6.13)

Thus the traces over bosons and fermions are

                                               j           0 123456

                               TrB(Dgj ) 128 2 2 2 2 2 2
                               TrF(Djg) 128 �2 2 �2 2 �2 2

with  the  (+)  sign  for  h7  =            0  and    the  (-)  sign        for  h7  =    1  .  We    see  immediately          that   choosing
                                                                                          2

h7 = 0 gives VCas = 0, reflecting the fact that supersymmetry is preserved by this choice.

Indeed, four spinor components are left invariant by Dg, which therefore preserves four su-

percharges  and  results   in               a  4d  N  =2      theory.       We    must       therefore     choose     h7    =   1  in  order  to
                                                                                                                                2

break this SUSY.

Except for the identity D0g = I, all elements Dgj in the sum have the same 1-dimensional

invariant subspace, and we can use (4.53) to write their contribution to the potential as

                 VCtwasisted   =              (s - 3)      �      24  2   6          1 - (-1)j+m
                                            - 2s-3                       j=1
                                                              x7              mZ     (m      -  j  )2s-6
                                                              7R4                               7

                                               (s - 3)           24      22s-6 - 1        72s-6 - 1

                                                              x7
                               = - 2s-3 � 7R4 � 22s-7                                                      (2s - 6) .                  (6.14)

We thus find the Casimir potential

                                               -   CI(x)      (  5    )  �  25 - 1      75 - 1                24  ,
                                                    R4           2            24
                                                                                                           x7
                           VCas             =              -                         �       7 (5) � R4                                (6.15)
                                                                    5

                                                              2 2

                                                                                 733.1

including the identity term CI(x),

                                                                       66               1 - (-1)m
                                                      (s) 128 x 7                                       s.
                              CI(x) = 2s �                                                                                             (6.16)
                                                                  7                    x2 |n|2 + m2
                                                                            nZ6
                                                                            mZ

Note in particular that all terms with even m vanish, independently of n, due to the

                                                                      � 75 �
fact that we have twisted boundary conditions for the fermions around the S1 base,

h  =      (0,   0,  0,    0,  0,  0,  1  ).        Although CI(x) must be summed numerically, we can study its
                                      2

asymptotic behaviour as x  0 and x  . For large x, the dominant terms in the sum

have n = 0, so that

                                         66                                    (  11  )       (211 - 1)(11)
                (s) x 7                                          1                2                  
   CI(x)                     �                                              =              �                                             66            as x   . (6.17)
                2s               7 � 22s-8                   |m  +  1  |2s     211/2                47
                                                                    2                                                                 x7

                                                         mZ

                                                                                              9.337

On the other hand, for small x, the dominant terms would correspond to m = 0, since these
would get an x-11 enhancement--however, all these terms cancel and cannot contribute to
the sum. Consequently, in this limit we find

                                                                186(5) 24                        24
                                                CI(x)  72 x 7  2.791 x 7 as x  0 ,                                                                        (6.18)

which we obtain using the Mellin transform followed by Poisson resummation, as we did

to compute analytically some of the sums in Section 4.3. Although here we cannot obtain

the exact analytical result, we can take the zero mode in the Poisson sum and neglect the

exponentially suppressed terms to derive this asymptotic behaviour.

   106          C1(x)                                                                 106                  24
                                                                                                     C1(x) ~ 2.792 x 7
                Ctwisted(x)
                                                                                                                                  66
                    C(x) = C1(x) + Ctwisted(x)
                                                                                                     C1(x) ~ 9.338 x 7
   1000
                                                                                    1000                                                  24

                                                                                                     Ctwisted(x) ~ 733.1 x 7

   1                                                                                  1

   0.001                                                                          0.001                                                                   C1(x)
                                                                                                                                                          Ctwisted (x)

          0.05      0.10                           0.50      1                             0.05      0.10                                        0.50  1

                                                x                                                                                             x

Figure 12. Casimir energy on F7 = T 7/Z7, evaluated numerically for the twisted and untwisted
sectors. Notice that, unlike in the F6 example of the previous section, there is no saddle.

     We find that the restriction on the choice of spin structure does not allow us to break
the 11-dimensional supersymmetry of M-theory and avoid the cancellations between bosons
and fermions in the Casimir energy. Since these cancellations follow from the supersymmetry
of the higher-dimensional theory, an antiperiodic spin structure would not be required if
one started with a non-supersymmetric theory directly. However, if the starting theory is
supersymmetric, one must be able to break this symmetry through the choice of compact
manifold and associated spin structure--in some cases, like for F7, this is not possible.

     Note that the corresponding equation (5.48b) for a general RFM Fk = T k/ with an S1

                                                                            � 76 �
base takes the form33 [54]

         x C                =      d(k + 4) - 8   (k  - p)np2   x2 - p n~2p  ,  (6.19)
          C                      k(k + (d - 2)p)        np2 x2  + n~2p

when we restrict to a single p-form flux that may have legs only along the fibre (np) or also

along the base (n~p). For an M-theory compactification on F7 with G4 flux, the equation

becomes                     x C            3np2 x2 - 4 n~2p
                             C              n2p x2 + n~2p
                                 =  12  �                        48 36  .       (6.20)
                                    35                         -,

                                                                 35 35

Although a critical point for C(x) is not strictly necessary for a dS maximum, all maxima we
have found (such as the dS5 solution of Section 5) appear in the vicinity of a critical point of
C(x). In this case, we see from (6.20) and the form of C(x), for which

                                 x C 24 66            120 330
                                    , = ,                           ,           (6.21)
                                 C         77                35 35

that there is no critical point for x. As a result, we do not expect to find a dS maximum in
this setup. This argument does not depend on the precise choice of fluxes (including their
proper quantisation) and therefore follows through without analysing the flux potential in
detail. It will also apply to other 7d RFM's whose spin structures must be periodic around
the fibre--this covers the Z9, Z14 and Z18 quotients discussed at the end of the previous
subsection that are reducible to a 2-moduli problem like the Z7 quotient, and whose twisted-
sector can be seen as multiple copies of the same Casimir branes (i.e. all non-trivial elements
have the same invariant subspace). Thus, there does not seem to be any dS4 maxima in
RFM flux compactifications with Casimir energies in four dimensions. This contrasts with
the maximum we found in Section 5, which after symmetry truncations could be reduced to
a two-modulus problem.

     Another important feature of the solution in Section 5 was the antiperiodic spin structure
along the fibre. The biggest order group that allows for antiperiodic spin structure along
the fibre is Z24, which requires the study of at least 3 moduli and several sets of Casimir
branes (in particular, a Z24 quotient will lead to 192 codimension-six, 32 codimention-four,
6 codimension-one and one space-filling Casimir branes). While cases such as these, with
more than one modulus, might indeed harbour non-trivial maxima, in this paper we restrict
our analysis to the setups in which, due to symmetries, the problem contains at most two
moduli. It would be very interesting to study cases with three or more moduli not fixed by
symmetries, a task that we leave for the future.

     Since we have just argued that no diagonal cyclic RFM with periodic spin structure is
likely to give us a dS saddle, what about those where an antiperiodic spin structure can be
chosen? The largest holonomy group on this list of cyclic RFM's that admits a fully twisted

  33We cannot apply this expression to the compactification studied in Section 5 since F6 has base T 2.

                                           � 77 �
spin structure on the fibre is Z8, for which there is an RFM that fixes all but four moduli of
the T 7 and is defined by

        0 -1 0 0 0 0 0                      0

       1 0 0 0 0 0 0                        0

         0  0  0  0  0  -1   0                0  


Dg  =    0  01    0  00      0    ,  bg  =    0    .  (6.22)


         0  0  0  1  0  0    0                0  


       0 0 0 0 1 0 0                        0

         0000001                              1
                                              8

This is the direct sum of the 4(x) and 8(x) companion matrices, giving rise to a finite
matrix of order lcm(4, 8) = 8. The block corresponding to 8(x) of order 8 is precisely what
we used for the T 6 quotient studied in Section 5, so in some sense it is a "cousin" of F6.
We did not study this example in detail, since it is a three-modulus problem and one must
identify suitable fluxes, etc. Nevertheless, we do not see an obstruction to the existence of
dS4 maxima, and therefore this is a promising candidate to study in the future.

7 Conclusions

In this paper, we have taken a few steps in the exploration of a new class of solutions in String
Theory, based on Riemann-flat manifolds (RFM's), where hopefully the existence of de Sitter
minima and maxima, as well as other accelerated cosmologies, can be ascertained beyond
any reasonable doubt. The landscape of RFM's offers unique opportunities for this, since it
removes the need for stringy sources (orientifolds, branes, strong warping) that significantly
complicate the analysis in other approaches to accelerated expansion in String Theory [18, 19],
while allowing us to break supersymmetry and compute quantum effects very explicitly in
a perturbative expansion around a flat minimum. We have described in detail a systematic
framework to study Riemann-flat manifolds and determine their Casimir energies, and started
a systematic exploration of their flux compactifications.

     The technical backbone of the results in this paper is the explicit formula for Casimir
energies in RFM's derived in Section 4. We found that the Casimir energy tends to lump
on certain cycles of the internal space, and can be effectively modeled as fictitious "Casimir
branes" wrapping different loci of the RFM. This allows one to pull back all the intuition
from standard string compactifications with branes [73], and it is tempting to speculate that
the Casimir branes may turn into actual branes in some cases via some chain of dualities.
Along these lines, it is worth pointing out that in the setup of [37], the Casimir energy also
tends to lump in localized objects (there, related to small cycles of the geometry), which may
suggest that the Casimir branes phenomenon is general. In practice the Casimir energy can
be captured via an effective "Casimir brane tension", for which we provide an explicit formula
that can be evaluated numerically. In some cases, the tension of the Casimir branes can be

                     � 78 �
anomalously large and negative, which is helpful in attaining solutions with large volume,
similarly to what happens e.g. in a Calabi-Yau with a large orientifold tadpole.

     Another very interesting phenomenon we encountered is that Casimir branes sometimes
appear in pairs of exactly opposite tension, in which case their contribution to the Casimir
energy exactly vanishes. As we showed in Section 4.5, this phenomenon can be understood as
a spacetime version of Atkin-Lehner symmetry [50�52], since the explicit formula for Casimir
energy that we obtain (arising as an integral of an 11d energy density over a compact space)
is structurally analogous to the worldsheet integral of the partition function over the (su-
per)moduli space of Riemann surfaces. Our spacetime version of Atkin-Lehner works for
pure QFT, and provides us with a mechanism to engineer compactifications of both QFT's
and EFT's arising from String Theory where the vacuum energy would be anomalously small,
potentially giving a novel way to attack the cosmological hierarchy problem. We believe a
systematic exploration of this phenomenon is important, and hope to return to it in the near
future.

     Using the Casimir formula, we have explored flux compactifications of M-theory to four
and five dimensions, where the flux term is matched with a Casimir energy to obtain dS
maximum saddles. A four-dimensional dS maximum remains a viable alternative to explain
the current accelerating phase of the universe [1, 2], and it might be even favoured in light of
recent DESI data [59�62]. Unfortunately, we could not find a dS maximum within the class
of four-dimensional compactifications of M-theory on a 7-dimensional, cyclic RFM that we
studied, which only have two moduli. However, given our results in five dimensions described
below, a dS4 maximum from Riemann-flat manifolds appears to be a very likely possibility to
us, and we cannot refrain from emphasizing the analysis in Appendix A of [151] where such a
scenario was found (together with a minimal matter coupling, which also arises automatically
in our setup) to describe the recent DESI observations quite satisfactorily. We did not look for
dS4 minima (which would involve at least two fluxes pitted against the Casimir term) because
they do not exist in the classical M-theory RFM landscape, as is explored in a companion
paper [54].

     Instead, our main achievement is in five dimensions, via the very explicit solution of
Section 5. It is a dS5 � (T 6/Z8) maximum solution of M-theory, supported by a balance of
G4 flux and Casimir effects. The solution has a positive vacuum energy V (5d) = 3.89 � 10-15
in 5d Planck units, a Hubble radius of H0-1  107, and is scale separated, with H0R  106
for R a characteristic length scale of the internal manifold. The solution is only a de Sitter
maximum, with three negative directions, all of which have a mass squared of order H02.
Due in part to the smallness of the vacuum energy, and in part to the fact that the internal
space is Riemann-flat to leading order, our solution seems protected against classical, higher-
derivative, and loop corrections. We point the reader to Section 5 and Table 2 for more
details.

     The solution we obtained is, to our knowledge, the first fully explicit example of a dS
saddle point with these properties. For instance, in the solutions of [64], the superpotential can
be computed reliably, but the K�ahler potential remains uncontrolled. By looking for solutions

                                                         � 79 �
within the regime of validity of supergravity, the full effective action can be determined, and
we can provide precise numerical calculations of the parameters of the solution. We believe
that being able to produce concrete numbers should be a litmus test of any would-be dS
construction, as providing a very explicit solution will allow the community to explore it
thoroughly. If our solution survives all corrections, then it has implications for a number of
Swampland constraints. It satisfies the Refined de Sitter Conjecture [10], and it can be used
to put bounds on the O(1) coefficients in the conjecture statement. Interestingly, although the
mass of scalars is of order Hubble, our dS maximum is too steep to harbor eternal inflation,
so our solution provides some evidence for the conjecture [152] that eternal inflation may
be in the Swampland. Another dS-specific Swampland Conjecture, the FL bound [141], is
satisfied in our solution, which may therefore be regarded as giving evidence for the bound
(although weak, since the bound was originally formulated for metastable dS saddles). There
is also a conjecture in [153] that classical dS saddles can live in an EFT with at most four
supercharges; our results suggest that quantum effects evade this conclusion. On the other
hand, several works [154�157] have discussed or argued for different versions of the conjecture
that cosmological or apparent horizons are in the Swampland; although it is difficult to
define apparent horizons rigorously, it appears to us that the instantaneous dS horizon in our
solution may qualify as apparent horizon. On the other hand, it certainly does not qualify as
a cosmological horizon, since these are defined in terms of the asymptotic future.

     An important issue in any compactification obtained as a solution to a lower-dimensional
EFT is that of 11-dimensional backrection. Here, too, the RFM solutions we found are in very
good position. We have explicit expressions for the 11d stress-energy tensor, coming both
from Casimir energies and fluxes, and they are everywhere smooth, although inhomogeneous,
in the internal space. We have checked that the inhomogeneities and general backreaction
are small enough not to destroy the solution, and the explicit expressions we obtained can be
used to follow up on that, constructing an iterative procedure which will converge to a full
solution. We expect to come back to this interesting question in the future but, at any rate, the
perturbations we obtained are so small (10-10 in Planck units) that we expect the first-order
result to be a very good approximation to the actual solution. In this aspect, our solution
contrasts to standard dS minima proposals of ST [18, 19], or even some supersymmetric
solutions like DGKT [49], where the presence of singular sources and strong warping makes
the higher-dimensional analysis significantly harder. It shares this feature with the Casimir
M-theory compactifications of [37], with the additional difference that in an RFM the warping
is very small as opposed to O(1). In this sense, it is similar to the dS3 construction in [158],
where the warping variations are also very small.

     Another point to emphasize is that the smallness of the cosmological constant that we
find arises due to a combination of Einstein frame rescaling and the fact that the Casimir
energy scales simply as R-D, and D = 11 in M theory. Even moderately large R can yield
very small numbers. In other words, to get a small cosmological constant, one does not need
delicate cancellations between terms; in this case, it is simply a consequence that the volume
of the internal manifold is large ( 107) in 11-dimensional Planck units. Using the M-theory

                                                         � 80 �
scaling, achieving V  10-120 would require R  109 in 4d Planck units. While this estimate
is certainly too na�ive (it crucially ignores the contribution of SM fields to the cosmological
constant, and uses a very na�ive scaling of the Casimir term, ignoring its stabilization), the
point that a small vacuum energy might be a natural consequence of a relatively large internal
space still stands.

     Even though the solution survives all known higher-derivative and loop corrections, there
might be other, unknown, effects that may destabilize it. The internal manifold has a systole
(the length of the smallest closed geodesic that cannot be contracted to a point) of just 6.1
eleven-dimensional Planck lengths. While we have checked that M2 and M5 instantons are
negligible, loops of e.g. Planckian states are more difficult to control. Although we have
estimated that there would have to be  107 novel, long-lived states of Planckian mass in
M-theory to significantly affect our solution, we do not know a way to accurately determine
whether this is the case or not. While we certainly expect M-theory to have black hole states
starting at a roughly Planckian threshold, we do not really know their number, lifetime, or
even how to include them in a vacuum energy calculation accurately. The only approaches
which would be able in principle to access some of this information would be holography, or
perhaps S-matrix unitarity arguments, but either seems currently far from achieving this.

     In short, we are inclined to believe our solution is probably actually there, but it is difficult
to tell with certainty34. Plus, due to the nature of the difficulties, the question is unlikely to
be resolved rigorously in the near future. We believe it will be more productive to take the
smallness of the vacuum energy and general properties attained here as a signpost encouraging
us to focus on the exploration of the broader RFM Landscape, where better, more controlled
models may lie, ideally finding a dS maximum that can accommodate observations. We will
certainly look into this in the near future, and hope that this manuscript can entice others to
join us in this exciting quest--the Earth is certainly not flat [159], but the extra dimensions
just might be!

     Acknowledgements: We are indebted to David Andriot, Carlo Angelantonj, Ivano
Basile, Alek Bedroya, Jan de Boer, Veronica Collazuol, Gianguido Dall'Agata, Bruno de Luca,
Alon Faraggi, Bjorn Friedrich, Bernardo Fraiman, Arthur Hebecker, Luis Ib�an~ez, Rafal Lu-
towski, Andriana Makridou, Fernando Marchesano, Jakob Moritz, Sonia Paban, Tony Padilla,
Susha Parameswaran, Hector Parra de Freitas, Fernando Quevedo, Salvatore Raucci, Igna-
cio Ruiz, Augusto Sagnotti, Marco Serra, Gary Shiu, Eva Silverstein, John Stout, Michelan-
gelo Tartaglia, Houri-Christina Tarazi, Alessandro Tomasiello, Flavio Tonioni, A� ngel Uranga,
Cumrun Vafa, Damian Van de Heisteeg, Thomas Van Riet and Irene Valenzuela for very
valuable discussions and comments on the draft. MM thanks the SCGP for hospitality and a
stimulating environment during the Summer '23 workshop, where this project was initiated,
and Summer '24, where it was advanced, and the KITP program "What is String Theory?"
where an early version of these results was presented. This research was supported in part

  34Admittedly, after so much effort, psychological factors might also play a role in our belief.

                                                         � 81 �
by grant NSF PHY-2309135 to the Kavli Institute for Theoretical Physics (KITP). We also
thank CERN and the Harvard Swampland Initiative for hospitality during part of this work,
and the Aspen Center for Physics, which is supported by National Science Foundation grant
PHY-2210452 and a grant from the Simons Foundation (1161654, Troyer), for providing a
stimulating environment during its completion. The authors gratefully acknowledge the sup-
port of an Atraccion del Talento Fellowship 2022-T1/TIC-23956 from Comunidad de Madrid,
which supported both authors in the early stages of this project, as well as the Spanish State
Research Agency (Agencia Estatal de Investigacion) through the grants IFT Centro de Ex-
celencia Severo Ochoa CEX2020-001007-S, PID2021-123017NB-I00, and Europa Excelencia
EUR2024-153547. MM is currently supported by the RyC grant RYC2022-037545-I from
AEI.

A G4 flux quantization in M-theory

The de Sitter maxima we look for have G4 flux as an essential ingredient--in this appendix
we work out the normalization of the kinetic term from first principles, finding agreement
with [82�85]. We start from the 11-dimensional M-theory action, whose bosonic part is [82]

2211 SM-theory =       d11  x        R  -  1  |G~4|2     1       G~4  G~4  C~3 .  (A.1)
                                 -g        2          -

                                                         6

The 4-form G~4 does not have integer-quantized periods. The appropriate quantization con-
dition can be determined from demanding that the Chern-Simons coupling is appropriately
quantized [83, 84], and it is such that

                      1                3                                          (A.2)
                    2211
                               G~4 = 2 n, n  Z .

From this, it follows that the action (A.1) can be rewritten as

SM-theory =  d11x             1   R  -   1    |G4|2        1      G4  G4  C3 ,    (A.3)
                     -g     2211        2g32          - 242

in terms of a G4 whose periods are quantized in multiples of 2 (so that M2-brane charges
are integer-quantized), and

g32  2 � (22)2/312/13 = 2 � (22)2/3 161  (3.822 311)2                             (A.4)

is the M-theory 3-form gauge coupling, where in the last equality we have also introduced the
11-dimensional reduced Planck length, defined by 121 = 911. Using the formulae of [160], the
tensions of the BPS M2 and M5 branes are

TM2 =        1 g32  =  (22)1/3    ,     TM5 =         1 42           1   1   .    (A.5)
             2 121        311                         2 g32121 =  2  3  161

                                     � 82 �
These agree with the expressions in [84]. Writing G4 = 2n4 4, where 4 is a 4-form with
integer periods, the flux term of the potential becomes

                                             1    |G4|2       =           2     n24     |4|2 ,                              (A.6)
                                            2g32                    2     3

                                                                             311

which is the expression used in the main text.

B Lattice sums on RFM's with 1-dimensional invariant subspaces

Our formula (4.53) for the tension of Casimir branes in RFM's does not generally admit an

analytic expression, and we must resort to numerical methods to evaluate it. This is what

happens in many simple cases, such as a torus with no quotients [161]. In this appendix,

however, we describe a particular case where the sums can be evaluated analytically and

explicitly, in terms of  functions. This happens when the Casimir brane is one-dimensional

in the compact space (i.e. when we are computing E() for a  which has a one-dimensional

invariant subspace),

                                                              G-(s     -  1  )         e2i  n
                                                                          2          |n - b |2s
                                               (s )
                              E ( )   =     -  2s          �     ||                                .                        (B.1)

                                                                                nZ

In this case we can perform the sum analytically to obtain

                              (2s  ,  b     )  +     (2s   ,  1  -  b  )                               if  = 0 mod Z


           e2i  n        


    nZ |n - b |2s    = 22s          (2s ,         b  )  -   (2s ,      1-b      )                                        .  (B.2)
                                                  2                      2

                                      + (2s ,           1  -  b  )  -   (2s ,        1  -  1-b  )      if   =  1  mod Z
                                                              2                              2                 2


Together with the fact that each    has an inverse -1  , whose invariant subspace is
the same as that of ,

                         (I - D-1)n = 0 mod Z  (I - D)n = 0 mod Z ,                                                         (B.3)

and with b-1 = -b  1 - b , this implies that E(-1) = (-1)2E(). If  is an element

of  order  2,  i.e.  -1  = ,  the  contribution               with        =     1    vanishes;     otherwise,     the  contributions
                                                                                2

from  and -1 will add up or subtract depending on the traces weighing the sum,

      VCas =                                  1                     Trr(D) + (-1)2r Trr(D-1) E() .                          (B.4)
                         Trr(D) E() = 2
               r                                        r 

For bosonic fields, which always have  = 0 and satisfy TrBoson(D-1) = TrBoson(D) (see

Appendix F), the contributions add up. The largest contribution will come from the term

with  smaller  b ,   with   (2s ,     1  )        p2s      giving      a  good       estimate      of  the  enhancement     to  the
                                      p

                                                              � 83 �
Casimir potential on cyclic RFM's of order p. However, for fermionic fields, the result will

depend on the choice of boundary conditions r (compatible with the allowed spin structures
of the RFM); the trace of D-1 will be the same as that of D up to a sign (cf. Appendix F).

     In Appendix F we show that on a cyclic RFM of order p = ||, spinor traces are related

as

    TrSpinor(D- 1) = (-1) ni TrSpinor(D ) , with p � i = 2ni ,                      (B.5)

where i are the angles (eigenvalue arguments) of the rotations associated with Dg (including
the choice of spin lift). When the order of the cyclic RFM is odd, the pairity of ni is
the same as that of sg in Dgp = (-1)sg I, and correspondingly correlated with r through the
constraint (3.23) on h. For example, the T 7/Z7 we study in Section 6.2 is constrained to have
2r = 2h7 = ni mod 2, so that the fermion contributions add up, rather than cancel.

     On the other hand, if the cyclic RFM has even order, sg is independent of the choice of
spin lift and thus of the parity of ni. One can then choose the spin lift with ni odd, so
that the traces of D and D-1 differ by a sign, while 2r is constrained to be even--in this
case, the fermion contributions will will cancel pairwise. One can do this, for example, on the
Z18 quotient (see tables in Appendix G).

     Remarkably, if all the elements in  for a cyclic RFM, except for the identity, have a
one-dimensional invariant subspace--which is the case in particular for the RFM's identified
in Section 6 that may be left with only two moduli in special points in moduli space--fermion
fields may have no twisted sector terms at all, and only contribute through the identity
element as they would on the covering torus. Whether this cancellation happens can depend
on the spin structure of the RFM and its order. This interesting feature/cancellation appears
in the absence of supersymmetry, and is similar in form and details to the vanishing of fiber
contributions when the ^h vanishes in the main text. Having a part of the spectrum not
contributing to the vacuum energy is a quite surprising phenomenon, and variants of it could
be used e.g. to provide new solutions for the cosmological constant problem, where the
contribution to the vacuum energy of some fields is cancelled by variants of this mechanism.
It would be very interesting to understand if there is an underlying symmetry reason for this
phenomenon, and whether it can be generalized.

C Ewald summation

In this appendix, we generalize the Ewald summation technique for sums of the form

                                   e2ih�n                                           (C.1)
                                  |n + c|2s ,

                          n+c=0

developed in [133] for the three-dimensional case, to higher-dimensional setups. We will also

consider a general norm,

                          |n|2 = Gijninj.                                           (C.2)

                          � 84 �
The sum we wish to regularize is

                                         e2ih�n                                           (C.3)
                                        |n + c|2s ,

where there is a constant shift vector c, and whose Fourier transform is

   F   e2ih�n    (k)      dkn     e2i(h-k)�n     =  2k-2sk/2      k  -  s    e-2ih�c      (C.4)
      |n + c|2s                    |n + c|2s                 (s)  2        |h - k|k-2s .

Following [133], we take

                 F (n)    (s, |n + c|2)  ,        (s, x)                                  (C.5)

                                  (s)                            ts-1e-t dt .

                                                           x

For s = 1/2, the typical case of Coulomb interactions, the above becomes the usual erfc
regulator used in physical chemistry. The function

                                                    (s, |n + c|2)                         (C.6)
                          f (n)  1 - F (n) =

                                                          (s)

has the required property that f (0) = 0 and in fact, for small n + c it goes as |n + c|2s, so
that it cancels the denominator divergence in (C.1). More precisely, we have that

                           lim f (n)  e2ih�n     =  s e-2ih�c  Zk (c) ,                   (C.7)

                          n+c0        |n + c|2s     (s + 1)

and since terms with n + c = 0 are excluded from the original sum, we will need to include a
correction term equal to the negative of (C.7) if c is a vector of integer coordinates.

     The resulting sum can then be evaluated in momentum space via Poisson resummation.
The Fourier transform of the product can be evaluated directly, as

F  e2ih�n (s, |n + c|2)           (k)   dkn      e-2ik�n   e2ih�n    �  (s, |n + c|2)
   |n + c|2s �                                            |n + c|2s           (s)
                 (s)

        1  dkn   e2i(h-k)�n            + c|2)  =  e-2i(h-k)�c        dkn e2i(h-k)�n (s, |n|2) .
   =              |n + c|2s (s, |n                    (s)                      |n|2s
                                                                                                      (C.8)
      (s)

Next, we find a similarity transformation diagonalizing the metric G,

                                  G = MT M , m = M n ,                                    (C.9)

                                        � 85 �
so that the norms become the standard ones, and we define the variable                                (C.10)
                                                  q  G-1(h - k) ,

which turns the inner product in the Fourier transform phase into the metric one. We then
have (after a change of variables to spherical coordinates in the second line, with z axis
antiparallel to the vector q, and with Sk-2 the volume of the (k - 2)-dimensional sphere)

      e2ih�n (s, |n + c|2)            (k)  =  e-2i(h-k)�c        dkm    e2i((M-1)T (h-k))�m      (s,  |m |2)
F  |n + c|2s �                                                                  |m |2s
                        (s)                     (s) G

      e-2i(h-k)�c                (s, r2)          
   =             Sk-2          0 dr r2s-k+1
      (s) G                                         d (sin )k-2e-2i|q|r cos 

                                                 0

      (2  )  k  e-2i(h-k)�c        1              (s, r2)
             2
   =                                                dr                  J k-2    (2|q|r)
             (s) G             (2|q|)k-1-2s             (2|q|r)2s-   k
                                              0                      2        2

      (2  )  k  e-2i(h-k)�c       1                     s,           2
             2                                              (2|q|)2
   =                           (2|q|)k-2s 0 d                           J k-2 ( )
             (s) G                                          2s-  k
                                                                 2            2

   =  2k-2s     k    k         2|q|2       e-2i(h-k)�c      .                                         (C.11)
                2     - s,

        (s)          2                     G (2|q|)k-2s

In the above derivation, we have used one of the definitions of the Bessel J function,

                                          t                                                           (C.12)
                            J (t) = (2)+1 S2
                                                           e-it cos  sin2  d .

                                                        0

The chain of manipulations in (C.11) is only valid when |q| = 0; since h is a vector whose
components are all in [0, 1), vanishing |q| can only happen when h = 0 and k = 0. Then, we

obtain a term

                  Sk-2        (s, r2)               d (sin )k-2      =           k  s-k/2     .       (C.13)
                (s) G       0 dr r2s-k+1         0                               2

                                                                          G (s) s -        k
                                                                                           2

Therefore, the Ewald summation formula we will use is

         e2ih�n
        |n + c|2s =

n+c= 0

        e2ih�n (s, |n + c|2)                  2s-  k                 k - s, 2|h - k|2D        e-2i(h-k)�c
                                                   2                                          |h - k|kD-2s
                                      +                        
        |n + c|2s           (s)            (s) G k-h=0               2                                   (C.14)

n+c= 0

                  k  s-k/2        s e-2ih�c
+  h,0    G       2            -   (s + 1) Zk (c) .

                (s)  s  -   k
                            2

                                                 � 86 �
     In these expressions, |v|D2  G-ij1vivj is the canonical norm in momentum space. The
first term in the second line is there to take into account the special case q = 0 that only
happens when h = 0; in this case, the term k = 0 is not included in the second sum, and the

h,0 function term of the second line appears instead. The second term in the second line is
the correction (C.7) that only appears if the vector c has all integer coordinates; the function

Zk (c) is 1 in this case, and zero otherwise.
     The expression (C.14) is exact for any ; in practice, we will truncate both the sum over

n and the one over k, and choose an optimal value of  to maximize the speed of convergence.
As a first check, when s = 3/2 the above formula does become the expression of [133]35. We

have also checked numerically the validity of (C.14) for several concrete sums that can be

found in the literature, including

     (-1)m             4 ln 2              (-1)m+n                          
     m2 + mn + n2 = -            ,                      =  -       ln  1+     5,  [162]
                          33               m2    + 5n2          5                 [163]
n=0                                 n= 0                                          [164]

               (-1)n1+n2+n3                      s = 12s(2s - 1),                   (C.15)

     n1  +  1  2+  n2  +  1  2+     n3  +  1  2
            6             6                6
nR3

     (-1) i ni                                             1           256
nR8-{0} |n|2s = -16(s)(s - 3), nR8 |n + 1/2|2s = 2s (s - 3)(s),

which provide examples in 2, 3, and 8 dimensions. In our numerical implementation, the
sums are performed by first determining the set of vectors of norm smaller than the cutoff,
and performing the sum only after this set of vectors has been fully identified and stored in
memory. This provides a large speedup over implementations such as that in [134] (which
uses a similar approach to ours, and appeared as we were evaluating these sums), where the
approach is to sum over a large square box of points. This means one does not need to
spend computer resources identifying the set of points for the sum, but it comes at a hefty
price, since many points of very large norm are included, whose contribution to the sum is
negligible, but where nevertheless one spends some time evaluating the integrand. This is
particularly important in larger dimension where there are many points in the unit cube that
are not contained in the unit ball for a generic norm.

     Furthermore, for larger values of s and completely alternating sums (where the phase is
oscillating quickly in the unit cell), evaluating the sum at small  and truncating the direct
sum to just a single term served to produce outstanding results very quickly. This is because
for large s, the contribution from points away from the origin decays very quickly, all the
more so for alternating sums.

   35Modulo an additional term, related to the last term of (C.14), that appears in [133] because that reference
always excludes the contribution from n = 0 to the sum, which we do include here. Also, when h = 0, the
k = 0 term of the second sum should be replaced by its limiting value, which is convergent.

                                              � 87 �
D Numerical estimate

For the numerical evaluation of the sum (C.14), it is also convenient to have an estimate of
when the second term becomes small. In practice, the sum will yield accurate results as long
as the terms which have been neglected are beyond the exponential tail of the incomplete 
function. Defining   |h - k|2, we want that

                            k         -  s,  2      (k/2) 
                            2                 
                                                             . k-1                      (D.1)
                                      k/2-s          2k/2  2

The quantity dividing  on the right-hand side times the prefactor is the area of a sphere of
radius , so the denominator ensures that upon summing over all points of norm , their
total contribution is less than or equal to . Thus,  directly controls the precision of the sum;
setting  = 0.1 will produce results at least accurate to the first digit after the decimal point,
and so on.

     The above can be rearranged to

                      k  -  s,        2         (k/2)    2 s-1/2
                      2                                              ,
                                                                                        (D.2)
                                      1/2-s      2k/2    
                      2


and using the fact that the incomplete  function is upper bounded by its leading asymptote,

                                         (a, z) e-z                                     (D.3)
                                                 ,
                                             za       z

the bound (D.1) will be satisfied if

                      e-   2                 (k/2)   2 s-1/2
                                                                  ,                     (D.4)
                                          2k/2                                          (D.5)
                         2                           


which results in

                                             2k/2  s-1/2             .
                      2 W (k/2)  2

where W is the Lambert function. We use (D.5) in order to determine the cutoff value in the
momentum space sums as a function of  in the numerical implementation.

E Alternative derivations of the Casimir formula for RFM's

In this appendix, we recover the result (4.53) of the main text in two different ways.

                                             � 88 �
E.1 Direct evaluation in position space

We will first show how (4.53) may be recovered by a "direct" method, in which the integrals
are evaluated without using additional analytical tools. Our starting point is again (4.25),
which we reproduce here for convenience:

             dV                          e2ih�n  .                              (E.1)

       [0,1]k nZk |(I - D ) z + b + n|2s

To evaluate this sum, notice that D is an SL(n, Z) transformation, that maps the lattice Zk
to itself. As a result, the image of the lattice Zk by (I - D) is a sublattice of Zk,

               (I - D) Zk  Zk.                                                  (E.2)

We will denote its dimension by k.  is a sublattice of another lattice, , defined as the

intersection of   R with Zk. We can similarly define the lattice of vectors invariant under

D 36,

               {n  Zk | (I - D)n = 0} .                                         (E.3)

This is a lattice of dimension k = k - k. The lattices  and  are orthogonal with respect
to the inner product G. Their sum is a lattice

                       Zk                                                       (E.4)

of dimension k, and hence, it is a sublattice of Zk of finite index. The group

                   Zk/                                                          (E.5)

is a finite abelian group. Each    can be represented by a vector  of integer coordinates
in a particular unit cell of  (say, the Brillouin zone), with the group law being vector addition
modulo . With these provisions, any vector n  Zk can be written as

                 n = k + l + ,                                                  (E.6)

where k   and l  . As a result, the sum over n in (E.1) can be rewritten as

                                   e2ih�[k+l+]                                  (E.7)
             [0,1]k dV |(I - D) x + k + b + l + |2s .
          k
       l,

  36Notice that this is different from the definition of  in the rest of the paper, which uses the transpose of
D. The definition in terms of D is used in this subsection of this appendix only.

                 � 89 �
Now recall the consistency condition (3.22), discussed in Section 3, that

             h � (I - D)l = 0 mod Z .                                      (E.8)

Since k = (I - D)l for some l by virtue of being an element in , the e2ih�k term in the
numerator in (E.7) is trivial. In fact, writing x = x + x where x, are the orthogonal

projections of x onto   R and   R, respectively, the whole integrand is independent of
x since this is annihilated by (I - D). The integral over x can be carried out directly and
gives an overall factor of V, where V is the volume of the unit cell of the  lattice. The
range of the variable (I - D) x is that of the unit cell of , so the combined variable

             y  (I - D) x + k                                              (E.9)

runs over all of Rk. This means that, after changing variables to y (and including the

resulting Jacobian factor |det(I - D)|-1), the sum over k and the integral over x can be
combined into a single integral over Rk,

           V                  dV      e2ih�(+l)    .                       (E.10)

    |det(I - D)| l            Rk |y + b + l + |2s


Notice that |det(I - D)| counts precisely the number of elements of the finite abelian group
 = /. The integral over y can be carried out now by elementary methods. First, by

a shift of the y variable, we can replace

    y + b + l +   y + b + l + ,                                            (E.11)

where v denotes the projection of v onto   R. Then, the norm splits as

    |y + b + l + |2 = |y|2 + 2, 2  |b + l + |2.                            (E.12)

The resulting integral can be evaluated directly by performing a change of coordinates to
make the metric diagonal, and using spherical coordinates, to obtain

dV        k   yk-1 dy                       k    k-k (s) 1                 (E.13)

    2 2                               2 2
Rk (|y|2 + 2)s = (k/2) 0 (y2 + 2)s = (k/2) =  2 (s) 2s ,

where we have used the variables k = k - k and s = s + (k - k)/2, as in the main text.
We can already recognize the numerical prefactor of (4.53). Putting everything together, we

                              � 90 �
get that (4.25) equals

                          k-k (s)  V                   e2ih�(+l)          (E.14)
                        2                                              .
                        (s) |det(I - D)| l |b + l + |2s


Now, any vector in  but not in  will yield a  with  = 0. For any such element, the

argument of the sum in (4.25) only depends on  via the phase of the numerator. Denoting

the set of all such  by , the sum over  in (E.14) can be performed first over these,

yielding

                              e2ih� = |det(I - D )| ^h ,                  (E.15)


where we have used that the cardinality of  equals |det(I - D)|, as explained above, and

defined

                        ^h  1 iff h � l  Z, l  , and 0 otherwise.         (E.16)

The condition for ^h = 1 is precisely that h, the orthogonal projection of h onto   R,
coincides with the same projection for some lattice vector n  Zk. This is equivalent to the
existence of some   Zk such that

                        (I - D)T � h = (I - D)T � ,                       (E.17)

which is precisely the consistency condition (E.24). As in the main text, (E.17) means that
h =  + , where  is in   Q. Finally, we can combine w  l + . All vectors w have
the property that w � l  Z for all l  Zk, and they all lie in   Q. Therefore they span
the projection of the dual lattice to  onto itself. Denoting this lattice as , relabelling

V  G in terms of the induced metric, and noticing that

                        h � w =  � w +  � w =  � w mod Z                  (E.18)

for all w  , the Casimir energy becomes

                                   k-k (s)             e2i�w
                        G  2                                  ,           (E.19)
                                   (s) w  |w + b |2s

which agrees with expression (4.53) in the main text.

E.2 RFM Casimir formula from Ewald expressions

A second cross-check of (4.53) comes from using the Ewald resummation expressions of Sub-
section 4.6 and Appendix C. We now start by ignoring momentarily the integral in (E.1), and
focusing on the sum inside the integral first. This sum can be tackled by Ewald methods,

                                         � 91 �
and indeed the Ewald resummation formula (4.92) applies directly provided that we identify

                                c = (I - D) z + b .                        (E.20)

One key advantage of the expression (4.92) is that after Ewald resummation, the integral
over z can be performed directly in the momentum sum (just like in the Mellin transform
derivation of Subsection 4.4), since the dependence on z is purely oscillatory. The integral
one needs to evaluate is

               dk z  e-2i(h-k)�[(I-D ) z+b ]  =       e-2i(h-k)�b          dkz e-2i(h-k)�[(I-D ) z]
  G                                                G

       [0,1]k                                                      [0,1]k

                             k  e2iql - 1
             G                              ,
       =        e-2i(h-k)�b  l=1 2iql            q  -(I - D)T (h - k) ,    (E.21)

where ql is the l-th component of the vector q. Further simplification is not possible without
additional assumptions on the vector h. However, the consistency condition on spin structures

(3.22), discussed in Section 3, that

                                h � (I - D)l  Z, l  Zk ,                   (E.22)

implies that (I - D)T � h is a vector of integer coordinates, and therefore, that q is as well.

Since                           e2iql - 1
                                  2iql  ql,0 for ql  Z,
                                                                           (E.23)

the integrals simplify to a delta function q,0 imposing that the sum is restricted to the
sublattice satisfying

                                  (I - D)T (h - k) = 0,  k =  + ,

where  is a generic vector of the lattice  defined as the intersection of Zk with the invariant
subspace of DT , and   Zk is any particular vector of integer coordinates satisfying

                                (I - D)T  = (I - D)Th .                    (E.24)

If there is no   Zk satisfying this equation, then the sum vanishes identically. We will

remember this by including in the final result a factor ^h in the sum which evaluates to 1
when (E.24) is satisfied, and to 0 otherwise. Notice that the vector   h -  lies in   Q.
We can similarly define b as the projection of b onto the subspace invariant under D. We

have that

                                ( - k) � b = ( - k) � b .                  (E.25)

                                                 � 92 �
    Taking these into account, the integral over expression (4.92) takes the form

                     Sposition  +  2s-      k             k - s, 2| - |D2            e-2i(-)�b
                                            2                                        | - |Dk-2s

                                      (s)                   2         

                                               -=0

                                   k  s-k/2           
                                   2                    G s
                     + h,0 (s)                    - (s + 1) (D,b),                                            (E.26)
                                      s  -     k
                                               2

where by Sposition denotes the integral over x of the first term in (4.92), which we did not
evaluate explicitly. Notice that the last term in (E.26), which comes from the integral in the
last term of (4.92), is only present for the identity contribution D = I, b = 0, where the

integral over x is trivial anyway. For any other element of B, the Zk (c) term localizes the
last term in (4.92) to a zero-measure set of the unit cube, so we will drop it from now on.

     Denoting k  dim(), and writing  = V � l where V is a matrix whose columns form
a basis of , and l  Zr, we can rewrite (E.26) as a sum over l. Using the definitions37

|v|I  vT � GI � v ,         GI  VT GDV ,                 d  V-1  ,    v  VT b ,        s = k - k + s , (E.27)
                                                                                                2

equation (E.26) can be rewritten as

                2s  -k+  k                  k - s, 2|d - l|I2         e-2i(d-l)�v           k    s  -k    /2
                         2                                                                  2
Sposition  +                                                                         + d,0 (s)                . (E.28)
                 (s)                        2                         |d - l|kI -2s              s  -     k
                            lZk                                                                           2

                            l-d= 0

In  particular,  if  we  multiply        the   whole  sum   by  a   common  factor   (s)   k /2  1     ,  where  GI  
                                                                                     k/2  (s)      GI

det(GI ), we obtain

    (s)       k/2      1                          2s  -  k            k - s, 2|d - l|2I     e-2i(d-l)�v
    k/2       (s)                                        2                                  |d - l|Ik-2s
                            Sposition    +                          
                       GI                      (s) GI                 2                                     (E.29)
                                                            lZk
                                                            l-d=0

                         k  s   -k/2
                         2
    +      d,0                                 .
                       (s)      s     -  k
                   GI                    2

The last two terms now look exactly like the momentum piece of a Ewald sum (4.92), in k
dimensions instead of k, and with different metric and shift vectors. According to (4.92),
the momentum piece gives the exact result as   , where the position piece becomes
negligible. Since S, being an integral of a similar position term, also becomes neglibile as

  37In general, given a rectangular matrix V, there is more than one pseudoinverse V-1. Since b lies in the
invariant space of D , we will choose the particular pseudoinverse such that the columns of (V -1)T generate

the invariant subspace of D .

                                                            � 93 �
  , (E.28) must equal the Ewald sum, which means that for any  we can replace S
with the position term. Putting everything together, adding the prefactor in (4.18) coming
from the volume of the sphere and the propagator derivatives, and the extra sign due to our
definition of the Casimir coefficient, the Casimir energy E of (4.25) evaluates to

           E ( )    =  -  ^h  (s)  �      G        e2id�m         (E.30)
                              2s         ||  m |m + v |2s ,

where | � |2 is the norm with respect to G = GI-1, and the definitions of the various quantities
appearing in (E.30) are as follows: let as above V be matrix whose columns form a basis of
the invariant subspace of Zk with respect to DT , of dimension k. Then

G = V-1 G (V-1)T ,     v = VT � b ,      d  V-1,  s = k - k + s.  (E.31)
                                                           2

where b is the projection of b onto the invariant subspace of D, and  is defined in (E.24).

In short, the integral over z localizes the sum to a lower-dimensional sublattice, but the

resulting sum is still like that of (4.89), and can be evaluated numerically in an efficient way

via the Ewald formula (4.92). Finally, (E.30) can also be written in terms of the original

metric as                                    e2i �

           E ( )    =  -^h    (s)     �  G                        (E.32)
                              2s
                                         ||   | + b |2s

where  is the lattice spanned by the columns of (V-1)T . As explained above, these can be
taken to lie in the invariant subspace of . By the same argument as that around equation
(4.46), the lattice spanned by these is precisely the projection of the ambient lattice onto the
D invariant subspace. Equation (E.32) is our final result, and it agrees with (4.53) of the
main text. In short, it turns out that performing the z integral in the sum (4.25) turns it into
another sum of the same form, which can be evaluated efficiently via Ewald methods.

F Lorentz group traces for Casimir energies

In this appendix we collect some information regarding the calculation of traces of several
matrices that appear in the calculation of Casimir energies in the main text. As described
there, the Casimir energy involves traces over representations of a certain group action acting
on the Hilbert space of the massless particles in d dimensions. The little group acting on
D-dimensional massless particles is SO(D - 2), which decomposes as

           SO(D - 2)  SO(k) � SO(d - 2) ,                         (F.1)

as we compactify the theory on a k-dimensional manifold down to d = D - k dimensions.
The geometric action we use to obtain a Riemann-flat manifold as a quotient of T k is in the

                                   � 94 �
SO(k) factor, but it is useful to work in terms of SO(D - 2) matrices. Hence, we will embed
the SO(k) matrix in the vector representation as a block-diagonal SO(D - 2) matrix, with
an additional (d - 2) � (d - 2) block representing the identity.

     In this paper, we focus on M-theory compactifications, and thus start with a 9 � 9 ma-
trix M representing an element of SO(9) in the vector representation. To compute Casimir
energies we must compute the trace of the matrices that represent this element in the repre-
sentations of SO(9) that correspond to the fields of 11-dimensional supergravity--the graviton
g�, transforming in the symmetric-traceless 44 representation; the 3-form C�, transform-
ing in the antisymmetric, three-index 84 representation; and the gravitino, transforming in
the spin-3/2 128 representation. Notice that the little group accurately counts the physical
polarizations (degrees of freedom) for each field, and that the total number of bosonic d.o.f.
equals the number of fermionic d.o.f., as befits a supersymmetric theory.

     In principle, the matrix M must be orthogonal. However, because all the formulas below
will involve traces, and the trace of a matrix is invariant under similarity transformations, M
can be replaced by XMX-1 for any non-singular matrix X. In particular, we may replace
the orthogonal matrices by non-orthogonal representatives of themselves (for instance, by the
SL(n, Z) matrix D that implements the action in the lattice basis), which is what we do in
the main text.

     How do we relate the trace of M to the trace of MSym., the representative in the symmetric
tensor representation relevant for the graviton? If va and wa both transform in the vector
representation of SO(n), one can construct the tensor representation whose objects are two-
index tensors T ab, and for which a basis can be constructed via bivectors vawb. The SO(n)
action on the tensor representation is

        vawb  McaMdbvcwd ,                      (F.2)

and the pairing to a dual basis is given by the tensor cadb. Hence, the trace in the tensor
representation is simply

Tr(MTens.) = acbdMcaMdb = (Tr(M))2 .            (F.3)

The tensor representation is reducible, and it decomposes as a sum of symmetric traceless,
antisymmetric, and singlet representations. The corresponding projection operators are

PSym.   T ab  =  1 (T ab  +  T ba)  -  T ab  ,
                 2                     n

PASym.  T ab  =  1 (T ab  -  T ba) ,
                 2

PSing.  T ab  =  T ab  .                        (F.4)
                 n

One can check that each of these squares to themselves, as a projection operator must, and
that the sum of the three equals the identity. The trace in the symmetric tensor representation

                 � 95 �
is just the trace in the tensor representation of the projected matrix,

     Tr(MSym.) = 1 Tr(M)2 + Tr(M2) - 1 ,                                                         (F.5)
                       2

where the -1 comes from the singlet contribution which is proportional to (1/n)Tr(MT M) =
1 since M is (similar to) an orthogonal matrix. As a check, when M = I we get

  Tr(ISym.) = n2                             11        �n=  n(n + 1)  -1,                        (F.6)
                                               -
                                       22n                  2

which is the correct dimension for the symmetric traceless representation.
     For the three-index antisymmetric representation, the corresponding projector acts as

P3-Antisym. T abc  =             1     T abc + T bca + T cab - T bac - T acb - T cba  ,          (F.7)
                                 6

and, consequently, the trace is

Tr(M3-Antisym.) = 1 Tr(M)3 - 3 Tr(M2) � Tr(M) + 2 Tr(M3) .                                       (F.8)
                        6

Evaluating this for the identity matrix gives

Tr(I3-Antisym.) = 1 (n3 - 3n2 + 2n) = n(n - 1)(n - 2) = n ,                                      (F.9)
                                 6                             6              3

which is the correct dimension for the three-index antisymmetric representation. This is a
special case of a more general formula [165] encoding the character of a fully antisymmetric
representation38 via a generating function,

                                                       -(-x)l Tr(Ml)

     xkTr(Mk-Antisym.) = exp                                          l    .                     (F.10)

k=0                                             l=1

     Finally, to evaluate the traces in the gravitino (Rarita-Schwinger) representation, we may
realize it as the tensor product of a vector with a spinor a , where a is as before a vector
index and  is a spinor index, and then substract a spinor with opposite chirality,

                                 PR.S  a  =  a  -  1   ab(b)a  ,                                 (F.11)
                                                   n2

where the relative factor of 1/n2 comes from the property ab(b)(a) = n2 of  matrices.
Taking traces on both sides of this equation, one obtains

                                Tr(MR.S.) = (Tr(M) - 1) Tr(MSpinor) ,                            (F.12)

38Note a typo in the rhs of (49) of [165], the term ChR(lF ) should be divided by l [166, 167].

                                             � 96 �
and the only thing left to do is to express Tr(MSpinor) in terms of Tr(M). To do this, we can

employ  the  fact  that,  for  n  =  2k  +  1  odd,  the  spinor       representation         2  k    satisfies
                                                                                                 2

                                                                    k  n                                         (F.13)
                                                                           ,
                                               2k  2k =                l

                                                          l=1

i.e. it becomes a sum of fully antisymmetrized representations. The dimensions also agree, as
can be checked using Pascal's identity. Combining this with (F.10), we obtain an expression
for the spinor traces, which for the particular case of interest n = 9 becomes

Tr(MSpinor)2 = 1 + Tr(M) + 1 (Tr(M)2 - Tr(M2))
                                       2

             + 1 (Tr(M)3 - 3 Tr(M)Tr(M2) + 2 Tr(M3))                                                             (F.14)
                6

             + 1 (Tr(M)4 - 6 Tr(M)2Tr(M2) + 3 Tr(M2)2 + 8 Tr(M)Tr(M3) - 6 Tr(M4)),
                24

and together with (F.12) fully determines the traces in the gravitino representation, up to a
sign ambiguity in taking the square root in (F.15). This ambiguity is physical, and corresponds
to the two lifts (related by a sign) that a given SO element has in Spin. With these expressions,
we get Tr(IR.S.) = 128, which is the correct result for the Rarita-Schwinger representation.

     All these formulae can be checked by evaluating them explicitly for SO(9) matrices in
Cartan form, in terms of Cartan angles. We can write any SO(9) element in the form

                           cos 1 sin 1 0 0                             0 0

                          - sin 1 cos 1 0 0                            0 0

                                               ...      ...               ...  ...  
                                               ���   cos 4             sin 4        
                                  0      0                                            =  exp  iE3     ,          (F.15)
                   M=                    0
                                  0                                            0


                                  0      0 � � � - sin 4 cos 4 0


                                  0      0 ��� 0                       01

where E3 is a diagonal generator that is a linear combination of the Cartan generators of
SO(9), i.e. E3 = ||-2( � H), with  a root of SO(9) and Hi, i = 1, ..., 4 the Cartan
generators. Since we can decompose each representation into eigenstates |� of Hi labelled
by a weight vector � , once we know each decomposition in terms of its weights we can take

the trace in some representation R as

                                     TrR(M) = exp i  � � ,                                                       (F.16)

                                                         � R

where �  R includes all weight vectors � in the representation R (e.g. there are 9 such vectors
in the fundamental representation and 44 in the rank-2 symmetric traceless representation).
We then find that the traces computed in this way match the ones computed using the
character formulas above. For example, the weights of the vector representation correspond

                                                     � 97 �
to all possible permutations of (�1, 0, 0, 0) plus (0, 0, 0, 0), which is indeed a 9-dimensional
representation. Using (F.16) we find

                                                              4                                             (F.17)

                                      Tr9(M) = 2 cos i + 1 ,

                                                            i=1

which matches the trace of M. Taking instead the spinor representation of SO(9), corre-

sponding  to  weight  vectors  {�  1  ,  �  1  ,  �  1  ,  �  1  }  (which  does    add  up  to  24  =  16  d.o.f.),  we
                                   2        2        2        2

find                                                                4

                                      TrSpinor(M) =                      2 cos i .                          (F.18)
                                                                                2
                                                                    i=1

For spinor representations we should keep in mind that the transformation M has two spin

lifts �M related by a sign. If we choose this set of i to define +M, then -M corresponds
to any choice of i = i + 2i such that i  (2Z + 1). Indeed, we find that

                                              4            i  +     i
                                                           2
              TrSpinor(-M) = 2 cos

                                   i=1

                               = (-1) i 4 2 cos i = (-1)                            i TrSpinor(M) ,         (F.19)
                                                         2

                                                   i=1

with the trace differing by a sign whenever i is odd.

     When we consider cyclic RFM's, as we do in this paper, all elements in the group  are
powers of the generator, i.e.  = {I, Dg, ..., Dpg-1}, where p = || is the order of the finite
group . Correspondingly the angles i(j) for a given element Dgj are just multiples of the
angles ig of the generator, i(j) = j � ig, which gives the traces in the vector representation

                                                        4                                                   (F.20)

                               Tr9(Dgj ) = 2 cos(j � ig) + 1 .

                                                      i=1

Since Dpg = I, we have that p i = 2ni, with ni  Z, and the trace is indeed 9, the dimension
of the vector representation. For spinor representations,

                                                   4                                                        (F.21)

                      TrSpinor(Dpg) = 2 cos( ni) = (-1) ni � 16 ,

                                                  i=1

whose sign depends on the choice of angles i, i.e. on the choice of spin lift �Dg. Changing
the spin lift by shifting i  i + 2i, with i odd, as in (F.19), corresponds to a shift
ni  ni + p i and thus ni  ni + p i; this changes the spinor trace by a factor
(-1)p i which is 1 for p even and (-1) for p odd. Note the relation to our constraint

(3.23)--for even p, sg does on depend on the specific choice of spin lift and thus the phase

                                                           � 98 �
vector h is constrained in the directions not orthogonal to bg.
     Finally taking the representations of M-theory, the traces of a given element Dgj   in

the case of cyclic groups are

                   4                                                      4

Tr44(Djg) =              2 cos(2j ag) + 2 cos(j ag) + 1 + 2 cos(j ag) cos(jbg)           (F.22)

                   a=1                                                 b=1

                                                                       j=i

for the graviton,


                         4                                       4

                   Tr84(Dg) = 1 + 6 cos(j ag) + 2 cos(j ag) cos(j bg)


                         a=1                                     b=1

                                                                 j= i


                           4    4
                         +
                                       cos(j ag) cos(j bg) cos(j cg) ,                   (F.23)
                           3                                              

                              b,c=1

                              b= c= a

for the three-form, and

                                                   4             4              j ag  ,  (F.24)
                                                                                2
                   Tr128(Dgj ) = 2 cos(j ag)                        2 cos

                                     a=1                         a=1

for the gravitino, in terms of the eigenvalue arguments ig of the generator Dg and keeping
in mind the choice of spin lift Dg.

     Note that the traces over bosonic representions are invariant under the change j  p - j
and thus the traces of Dgj and Dpg-j = (Dgj )-1 are the same. However, for the gravitino

representation (as would also be in the spinor representation) we have

                                                    4  4         j ag        ,  with     p � i = 2ni . (F.25)
                                                                       2
Tr128(Dpg-j) = (-1) ni 2 cos(j ag)                        2 cos

                         a=1                           a=1

The traces in the gravitino representation will then be the same up to a sign, which is
determined by the eigenvalues of the generator Dg. Note that this sign is only affected
by the specific choice of spin lift when p is odd, but not when p is even.

G Cyclic 7d RFM's with S1 base

This appendix contains a list of all the Riemann-flat manifolds of cyclic holonomy that we
analyzed for the work in Section 6. While this list is not exhaustive, there is at least one
representative for each Q-equivalence class of SL(7, Z) matrices. As explained in the main
text, we could not find a dS saddle point in any of these, although we only studied carefully

                                                       � 99 �
the examples with two moduli only. The data listed includes: the explicit expression for the
generator z  Dg z +bg, the order of the group , the number of moduli that the RFM has,
and the possible choices for the vector h of spin structures. Each entry hi not fixed to zero
can take values 0 (corresponding to periodic boundary conditions) or 1/2 (corresponding to
antiperiodic boundary conditions).

                                                        � 100 �
           Dg                bg     || Moduli                h
                                                   (0, 0, 0, 0, 0, 0, 0)
 0 -1 0 0 0 0 0   0                                (0, 0, 0, 0, 0, 0, 0)
                                                   (0, 0, 0, 0, 0, 0, 0)
  1 -1 0 0 0 0 0             0                  (0, 0, h3, h3, h3, h3, 0)
                                                (0, 0, h3, h3, h3, h3, 0)
 0 0 0 0 0 -1 0              0                   (h1, h1, 0, 0, 0, 0, 0)
                                                 (h1, h1, 0, 0, 0, 0, 0)
  0  0  1  0   0  1   0      0      30       4


  0  0  0  1   0  -1  0      0   


0 0 0 0 1 1 0              0

  0000001                    1

                             30

 0 -1 0 0 0 0 0   0 

  1100000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  1   0      0      30       4


  0  0  0  1   0  -1  0      0   


0 0 0 0 1 1 0              0

  0000001                    1

                             30

 0 0 0 -1 0 0 0   0 

  1 0 0 -1 0 0 0             0   

  0  1  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0      30       4


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       30

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      24       4


  0  0  0  1   0  0   0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       24

 0 -1 0 0 0 0 0   0 

  1100000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      24       4


  0  0  0  1   0  0   0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       24

 0 -1 0 0 0 0 0   0 

  1000000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  -1  0      0      20       4


  0  0  0  1   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                 1
  0000001                       20

 0 -1 0 0 0 0 0   0 

  1000000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  1   0      0      20       4


  0  0  0  1   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       20

                                    � 101 �
           Dg                bg     || Moduli              h
                                                 (0, 0, 0, 0, 0, 0, 0)
 0 0 0 0 0 -1 0   0                             (0, 0, 0, 0, 0, 0, h7)
                                                 (0, 0, 0, 0, 0, 0, 0)
  1000000                    0                  (h1, h1, 0, 0, 0, 0, 0)
                                                 (0, 0, 0, 0, 0, 0, 0)
0 1 0 0 0 0 0                0                   (0, 0, 0, 0, 0, 0, 0)
                                                (h1, h2, 0, 0, 0, 0, 0)
  0  0  1  0   0  1   0      0      18       4


  0  0  0  1   0  0   0      0   


0 0 0 0 1 0 0              0

  0000001                    1

                             18

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  -1  0      0      15       4


  0  0  0  1   0  -1  0      0   


 0 0 0 0 1 -1 0            0

  0000001                    1

                             15

 0 0 0 0 0 -1 0   0 

  1000010                    0   

  0  1  0  0   0  -1  0      0

  0  0  1  0   0  1   0      0      14       4


  0  0  0  1   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       14

 0 -1 0 0 0 0 0   0 

  1000000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      12       4


  0  0  0  1   0  1   0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      12       4


  0  0  0  1   0  1   0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

 0 -1 0 0 0 0 0   0 

  1100000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      12       4


  0  0  0  1   0  1   0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      12       6


  0  0  0  1   0  1   0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

                                    � 102 �
           Dg                bg     || Moduli                h
                                                 (h1, h2, 0, 0, 0, 0, 0)
1 0 0 0 0 0 0 0                                  (h1, h2, 0, 0, 0, 0, 0)
                                                (h1, h1, h3, h3, 0, 0, 0)
  0 -1 0 0 0 0 0             0                   (h1, h1, 0, 0, 0, 0, 0)
                                                (0, 0, h3, h3, h5, h5, 0)
 0 0 0 0 0 -1 0              0                   (0, 0, h3, h3, 0, 0, 0)
                                                 (0, 0, 0, 0, h5, h5, 0)
  0  0  1  0   0  0   0      0      12       6


  0  0  0  1   0  1   0      0   


0 0 0 0 1 0 0              0

  0000001                    1

                             12

1 0 0 0 0 0 0 0

  0100000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      12       8


  0  0  0  1   0  1   0      0   


0 0 0 0 1 0 0              0

  0000001                    1

                             12

 0 -1 0 0 0 0 0   0 

  1000000                    0   

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0      12       6


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       12

 0 -1 0 0 0 0 0   0 

  1000000                    0   

  0  0  0 -1 0    0   0      0

  0  0  1  1   0  0   0      0      12       6


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       12

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0   

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0      12       6


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0   

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0      12       4


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       12

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0   

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0      12       6


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

                                    � 103 �
           Dg                bg     || Moduli                h
                                                (h1, h2, h3, h3, 0, 0, 0)
 -1 0 0 0 0 0 0   0                             (h1, h2, 0, 0, h5, h5, 0)
                                                (h1, h2, h3, h3, 0, 0, 0)
  0 -1 0 0 0 0 0             0                  (h1, h2, 0, 0, h5, h5, 0)
                                                (h1, h2, h3, h3, 0, 0, 0)
 0 0 0 -1 0 0 0              0                  (h1, h2, 0, 0, h5, h5, 0)

  0  0  1  0   0  0   0      0      12       6   (h1, h2, 0, 0, 0, 0, 0)


  0  0  0  0   0  -1  0      0   


0 0 0 0 1 1 0              0

  0000001                    1

                             12

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0   

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0      12       6


  0  0  0  0   0  -1  0      0   


0 0 0 0 1 0 0              0

  0000001                    1

                             12

1 0 0 0 0 0 0 0

  0 -1 0 0 0 0 0             0   

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0      12       6


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       12

1 0 0 0 0 0 0 0

  0 -1 0 0 0 0 0             0   

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0      12       6


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

1 0 0 0 0 0 0 0

  0100000                    0   

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0      12       8


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       12

1 0 0 0 0 0 0 0

  0100000                    0   

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0      12       8


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                 1
  0000001                       12

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  -1  0      0      10       6


  0  0  0  1   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                 1
  0000001                       10

                                    � 104 �
           Dg                bg     || Moduli              h
                                                (h1, h2, 0, 0, 0, 0, 0)
 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0   

 0 0 0 0 0 -1 0              0

  0  0  1  0   0  1   0      0      10       6


  0  0  0  1   0  -1  0      0   


0 0 0 0 1 1 0              0

  0000001                    1

                             10

1 0 0 0 0 0 0 0

  0 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  -1  0      0      10       6  (h1, h2, 0, 0, 0, 0, 0)


  0  0  0  1   0  -1  0      0   


 0 0 0 0 1 -1 0            0

  0000001                    1

                             10

1 0 0 0 0 0 0 0

  0 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  1   0      0      10       6  (h1, h2, 0, 0, 0, 0, 0)


  0  0  0  1   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       10

1 0 0 0 0 0 0 0

  0100000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  1   0      0      10       8  (h1, h2, 0, 0, 0, 0, 0)


  0  0  0  1   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                 1
  0000001                       10

 0 0 0 0 0 -1 0   0 

  1000000                    0   

  0  1  0  0   0  0   0      0

  0  0  1  0   0  -1  0      0      9        4  (0, 0, 0, 0, 0, 0, h7)


  0  0  0  1   0  0   0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       9

 0 -1 0 0 0 0 0   0 

  1000000                    0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      8        4  (h1, h1, h3, h3, h3, h3, 0)


  0  0  0  1   0  0   0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       8

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0   

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0      8        6  (h1, h2, h3, h3, h3, h3, 0)


  0  0  0  1   0  0   0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       8

                                    � 105 �
           Dg              bg      || Moduli    h

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

 0 0 0 0 0 -1 0              0

  0  0  1  0   0  0   0      0     8        6   (h1, h2, h3, h3, h3, h3, 0)


  0  0  0  1   0  0   0      0  


0 0 0 0 1 0 0              0

  0000001                    1

                             8

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  0   0      0     8        8   (h1, h2, h3, h3, h3, h3, 0)


  0  0  0  1   0  0   0      0  


0 0 0 0 1 0 0              0

  0000001                    1

                             8

 0 0 0 0 0 -1 0   0 

  1 0 0 0 0 -1 0             0  

  0  1  0  0   0  -1  0      0

  0  0  1  0   0  -1  0      0     7        4   (0, 0, 0, 0, 0, 0, h7)


  0  0  0  1   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       7

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0     6        6   (0, 0, 0, 0, 0, 0, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1  1   0  0   0      0     6        6   (0, 0, 0, 0, 0, 0, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 0 -1 0 0 0 0 0   0 

  1100000                    0  

  0  0  0 -1 0    0   0      0

  0  0  1  1   0  0   0      0     6        10  (0, 0, 0, 0, 0, 0, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0     6        8   (h1, h2, 0, 0, 0, 0, 0)


  0  0  0  0   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       6

                                   � 106 �
           Dg              bg      || Moduli               h
                                                (h1, h2, 0, 0, 0, 0, 0)
 -1 0 0 0 0 0 0   0                             (h1, h2, 0, 0, 0, 0, 0)
                                                (h1, h2, 0, 0, 0, 0, 0)
  0 -1 0 0 0 0 0             0                  (h1, h2, 0, 0, 0, 0, 0)
                                                (h1, h2, 0, 0, 0, 0, 0)
 0 0 0 -1 0 0 0              0                  (h1, h2, 0, 0, 0, 0, 0)
                                                (h1, h2, 0, 0, 0, 0, 0)
  0  0  1 -1 0    0   0      0     6        6


  0  0  0  0   0  -1  0      0  


0 0 0 0 1 1 0              0

  0000001                    1

                             6

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1  1   0  0   0      0     6        8


  0  0  0  0   0  -1  0      0  


0 0 0 0 1 1 0              0

  0000001                    1

                             6

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0     6        8


  0  0  0  0   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0     6        6


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1  1   0  0   0      0     6        8


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0     6        8


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  0 -1 0    0   0      0

  0  0  1  1   0  0   0      0     6        10


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

                                   � 107 �
           Dg              bg      || Moduli                 h
                                                (h1, h2, h3, h4, 0, 0, 0)
 -1 0 0 0 0 0 0   0                             (h1, h2, h3, h4, 0, 0, 0)
                                                (h1, h2, h3, h4, 0, 0, 0)
  0 -1 0 0 0 0 0             0                  (h1, h2, h3, h4, 0, 0, 0)
                                                (h1, h2, h3, h4, 0, 0, 0)
 0 0 -1 0 0 0 0              0                  (h1, h2, h3, h4, 0, 0, 0)
                                                (h1, h2, h3, h4, 0, 0, 0)
  0  0  0 -1 0    0   0      0     6        12


  0  0  0  0   0  -1  0      0  


 0 0 0 0 1 -1 0            0

  0000001                    1

                             6

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     6        12


  0  0  0  0   0  -1  0      0  


0 0 0 0 1 1 0              0

  0000001                    1

                             6

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     6        10


  0  0  0  0   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     6        10


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     6        10


  0  0  0  0   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     6        10


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 1 0
                                1
  0000001                       6

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  1  0   0  0   0      0

  0  0  0 -1 0    0   0      0     6        12


  0  0  0  0   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       6

                                   � 108 �
           Dg              bg      || Moduli                 h
                                                (h1, h2, h3, h4, 0, 0, 0)
 1 0 0 0 0 0 0  0

  0100000                    0  

0 0 1 0 0 0 0                0

  0  0  0 -1 0    0   0      0     6        12


  0  0  0  0   0  -1  0      0  


0 0 0 0 1 1 0              0

  0000001                    1

                             6

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  1  0   0  0   0      0

  0  0  0  1   0  0   0      0     6        16  (h1, h2, h3, h4, 0, 0, 0)


  0  0  0  0   0  -1  0      0  


 0 0 0 0 1 1 0  0
                             1
  0000001                    6

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  0  0   0  -1  0      0

  0  0  1  0   0  -1  0      0     5        8   (h1, h2, 0, 0, 0, 0, h7)


  0  0  0  1   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       5

 0 -1 0 0 0 0 0   0 

  1000000                    0  

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0     4        10  (h1, h1, h3, h3, h5, h5, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       4

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0     4        8   (h1, h2, h3, h3, h5, h5, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       4

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0     4        8   (h1, h2, h3, h3, h5, h5, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       4

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  0 -1 0    0   0      0

  0  0  1  0   0  0   0      0     4        10  (h1, h2, h3, h3, h5, h5, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       4

                                   � 109 �
           Dg              bg      || Moduli    h

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0  

 0 0 -1 0 0 0 0              0

  0  0  0 -1 0    0   0      0     4        12  (h1, h2, h3, h4, h5, h5, 0)


  0  0  0  0   0  -1  0      0  


0 0 0 0 1 0 0              0

  0000001                    1

                             4

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     4        10  (h1, h2, h3, h4, h5, h5, 0)


  0  0  0  0   0  -1  0      0  


0 0 0 0 1 0 0              0

  0000001                    1

                             4

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     4        10  (h1, h2, h3, h4, h5, h5, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       4

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  1  0   0  0   0      0

  0  0  0 -1 0    0   0      0     4        12  (h1, h2, h3, h4, h5, h5, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       4

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  1  0   0  0   0      0

  0  0  0  1   0  0   0      0     4        16  (h1, h2, h3, h4, h5, h5, 0)


  0  0  0  0   0  -1  0    0

                           0
0 0 0 0 1 0 0
                                1
  0000001                       4

 0 -1 0 0 0 0 0   0 

  1 -1 0 0 0 0 0             0  

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0     3        10  (0, 0, 0, 0, 0, 0, h7)


  0  0  0  0   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       3

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  0 -1 0    0   0      0

  0  0  1 -1 0    0   0      0     3        10  (h1, h2, 0, 0, 0, 0, h7)


  0  0  0  0   0  -1  0    0

                           0
 0 0 0 0 1 -1 0 
                                1
  0000001                       3

                                   � 110 �
           Dg              bg      || Moduli    h

 1 0 0 0 0 0 0  0

  0100000                    0  

0 0 1 0 0 0 0                0

  0  0  0  1   0  0   0      0     3        16  (h1, h2, h3, h4, 0, 0, h7)


  0  0  0  0   0  -1  0      0  


 0 0 0 0 1 -1 0   0 
                             1
  0000001                    3

 -1 0 0 0 0 0 0   0 

  0 -1 0 0 0 0 0             0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     2        22  (h1, h2, h3, h4, h5, h6, 0)


  0  0  0  0 -1 0     0      0  


 0 0 0 0 0 -1 0            0

  0000001                    1

                             2

 1 0 0 0 0 0 0  0

  0 -1 0 0 0 0 0             0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     2        18  (h1, h2, h3, h4, h5, h6, 0)


  0  0  0  0 -1 0     0    0

                           0
 0 0 0 0 0 -1 0 
                                1
  0000001                       2

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0 -1 0    0  0   0      0

  0  0  0 -1 0    0   0      0     2        16  (h1, h2, h3, h4, h5, h6, 0)


  0  0  0  0 -1 0     0    0

                           0
 0 0 0 0 0 -1 0 
                                1
  0000001                       2

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  1  0   0  0   0      0

  0  0  0 -1 0    0   0      0     2        16  (h1, h2, h3, h4, h5, h6, 0)


  0  0  0  0 -1 0     0    0

                           0
 0 0 0 0 0 -1 0 
                                1
  0000001                       2

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  1  0   0  0   0      0

  0  0  0  1   0  0   0      0     2        18  (h1, h2, h3, h4, h5, h6, 0)


  0  0  0  0 -1 0     0    0

                           0
 0 0 0 0 0 -1 0 
                                1
  0000001                       2

 1 0 0 0 0 0 0  0

  0100000                    0  

  0  0  1  0   0  0   0      0

  0  0  0  1   0  0   0      0     2        22  (h1, h2, h3, h4, h5, h6, 0)


  0  0  0  0   1  0   0    0

                           0
 0 0 0 0 0 -1 0 
                                1
  0000001                       2

                                   � 111 �
References

   [1] Supernova Cosmology Project Collaboration, S. Perlmutter et al., "Measurements of 
        and  from 42 High Redshift Supernovae", Astrophys. J. 517 (1999) 565�586,
        arXiv:astro-ph/9812133.

   [2] Supernova Search Team Collaboration, A. G. Riess et al., "Observational evidence from
        supernovae for an accelerating universe and a cosmological constant", Astron. J. 116 (1998)
        1009�1038, arXiv:astro-ph/9805201.

   [3] M. Dine and N. Seiberg, "Is the Superstring Weakly Coupled?", Phys. Lett. B 162 (1985)
        299�302.

   [4] H. Ooguri and C. Vafa, "On the Geometry of the String Landscape and the Swampland",
        Nucl. Phys. B 766 (2007) 21�33, arXiv:hep-th/0605264.

   [5] S.-J. Lee, W. Lerche, and T. Weigand, "Emergent strings from infinite distance limits", JHEP
        02 (2022) 190, arXiv:1910.01135 [hep-th].

   [6] E. Palti, "The Swampland: Introduction and Review", Fortsch. Phys. 67 (2019) no. 6,
        1900037, arXiv:1903.06239 [hep-th].

   [7] M. van Beest, J. Calder�on-Infante, D. Mirfendereski, and I. Valenzuela, "Lectures on the
        Swampland Program in String Compactifications", Phys. Rept. 989 (2022) 1�50,
        arXiv:2102.01111 [hep-th].

   [8] U. H. Danielsson and T. Van Riet, "What if string theory has no de Sitter vacua?", Int. J.
        Mod. Phys. D 27 (2018) no. 12, 1830007, arXiv:1804.01120 [hep-th].

   [9] G. Obied, H. Ooguri, L. Spodyneiko, and C. Vafa, "De Sitter Space and the Swampland",
        arXiv:1806.08362 [hep-th].

  [10] H. Ooguri, E. Palti, G. Shiu, and C. Vafa, "Distance and de Sitter Conjectures on the
        Swampland", Phys. Lett. B 788 (2019) 180�184, arXiv:1810.05506 [hep-th].

  [11] D. Andriot, "On the de Sitter swampland criterion", Phys. Lett. B 785 (2018) 570�573,
        arXiv:1806.10999 [hep-th].

  [12] D. Andriot and C. Roupec, "Further refining the de Sitter swampland conjecture", Fortsch.
        Phys. 67 (2019) no. 1-2, 1800105, arXiv:1811.08889 [hep-th].

  [13] A. Bedroya and C. Vafa, "Trans-Planckian Censorship and the Swampland", JHEP 09 (2020)
        123, arXiv:1909.11063 [hep-th].

  [14] T. W. Grimm, C. Li, and I. Valenzuela, "Asymptotic Flux Compactifications and the
        Swampland", JHEP 06 (2020) 009, arXiv:1910.09549 [hep-th]. [Erratum: JHEP 01, 007
        (2021)].

  [15] J. Caldero�n-Infante, I. Ruiz, and I. Valenzuela, "Asymptotic accelerated expansion in string
        theory and the Swampland", JHEP 06 (2023) 129, arXiv:2209.11821 [hep-th].

  [16] M. Etheredge, B. Heidenreich, T. Rudelius, I. Ruiz, and I. Valenzuela, "Taxonomy of infinite
        distance limits", JHEP 03 (2025) 213, arXiv:2405.20332 [hep-th].

  [17] S. L. Parameswaran, S. Ramos-Sanchez, and I. Zavala, "On Moduli Stabilisation and de Sitter
        Vacua in MSSM Heterotic Orbifolds", JHEP 01 (2011) 071, arXiv:1009.3931 [hep-th].

                                                        � 112 �
[18] S. Kachru, R. Kallosh, A. D. Linde, and S. P. Trivedi, "De Sitter vacua in string theory",
      Phys. Rev. D 68 (2003) 046005, arXiv:hep-th/0301240.

[19] V. Balasubramanian, P. Berglund, J. P. Conlon, and F. Quevedo, "Systematics of moduli
      stabilisation in Calabi-Yau flux compactifications", JHEP 03 (2005) 007,
      arXiv:hep-th/0502058.

[20] X. Gao, A. Hebecker, and D. Junghans, "Control issues of KKLT", Fortsch. Phys. 68 (2020)
      2000089, arXiv:2009.03914 [hep-th].

[21] M. Demirtas, M. Kim, L. McAllister, J. Moritz, and A. Rios-Tascon, "Small cosmological
      constants in string theory", JHEP 12 (2021) 136, arXiv:2107.09064 [hep-th].

[22] D. Junghans, "LVS de Sitter vacua are probably in the swampland", Nucl. Phys. B 990 (2023)
      116179, arXiv:2201.03572 [hep-th].

[23] I. Bena, E. Dudas, M. Gran~a, G. Lo Monaco, and D. Toulikas, "Bare-bones de Sitter vacua",
      Phys. Rev. D 108 (2023) no. 2, L021901, arXiv:2202.02327 [hep-th].

[24] X. Gao, A. Hebecker, S. Schreyer, and V. Venken, "The LVS parametric tadpole constraint",
      JHEP 07 (2022) 056, arXiv:2202.04087 [hep-th].

[25] S. Lu�st, C. Vafa, M. Wiesner, and K. Xu, "Holography and the KKLT scenario", JHEP 10
      (2022) 188, arXiv:2204.07171 [hep-th].

[26] S. Lu�st and L. Randall, "Effective Theory of Warped Compactifications and the Implications
      for KKLT", Fortsch. Phys. 70 (2022) no. 7-8, 2200103, arXiv:2206.04708 [hep-th].

[27] A. Hebecker, S. Schreyer, and V. Venken, "Curvature corrections to KPV: do we need deep
      throats?", JHEP 10 (2022) 166, arXiv:2208.02826 [hep-th].

[28] I. Bena, E. Dudas, M. Gran~a, G. Lo Monaco, and D. Toulikas, "D3-branes and gaugino
      condensation", JHEP 12 (2023) 019, arXiv:2211.14381 [hep-th].

[29] B. Valeixo Bento, D. Chakraborty, S. Parameswaran, and I. Zavala, "De Sitter vacua -- when
      are `subleading corrections' really subleading?", JHEP 11 (2023) 075, arXiv:2306.07332
      [hep-th].

[30] L. McAllister, J. Moritz, R. Nally, and A. Schachner, "Candidate de Sitter vacua", Phys. Rev.
      D 111 (2025) no. 8, 086015, arXiv:2406.13751 [hep-th].

[31] M. Kim, "String perturbation theory of Klebanov-Strassler throat", arXiv:2409.19048
      [hep-th].

[32] J. Moritz, "G2-manifolds from Diophantine equations", arXiv:2505.15883 [hep-th].
[33] G. W. Gibbons, "ASPECTS OF SUPERGRAVITY THEORIES", in XV GIFT Seminar on

      Supersymmetry and Supergravity. 6, 1984.
[34] J. M. Maldacena and C. Nunez, "Supergravity description of field theories on curved manifolds

      and a no go theorem", Int. J. Mod. Phys. A 16 (2001) 822�855, arXiv:hep-th/0007018.
[35] T. Appelquist and A. Chodos, "The Quantum Dynamics of Kaluza-Klein Theories", Phys.

      Rev. D 28 (1983) 772.
[36] N. Arkani-Hamed, S. Dubovsky, A. Nicolis, and G. Villadoro, "Quantum Horizons of the

      Standard Model Landscape", JHEP 06 (2007) 078, arXiv:hep-th/0703067.

                                                      � 113 �
[37] G. B. De Luca, E. Silverstein, and G. Torroba, "Hyperbolic compactification of M-theory and
      de Sitter quantum gravity", SciPost Phys. 12 (2022) no. 3, 083, arXiv:2104.13380 [hep-th].

[38] N. D. Birrell and P. C. W. Davies, Quantum Fields in Curved Space. Cambridge Monographs
      on Mathematical Physics. Cambridge University Press, Cambridge, UK, 1982.

[39] S. S. Haque, G. Shiu, B. Underwood, and T. Van Riet, "Minimal simple de Sitter solutions",
      Phys. Rev. D 79 (2009) 086005, arXiv:0810.5328 [hep-th].

[40] U. H. Danielsson, S. S. Haque, G. Shiu, and T. Van Riet, "Towards Classical de Sitter
      Solutions in String Theory", JHEP 09 (2009) 114, arXiv:0907.2041 [hep-th].

[41] A. R. D. Avalos, A. E. Faraggi, V. G. Matyas, and B. Percival, "Fayet�Iliopoulos D-term in
      non-supersymmetric heterotic string orbifolds", Eur. Phys. J. C 83 (2023) no. 10, 926,
      arXiv:2302.10075 [hep-th].

[42] A. R. D. Avalos, A. E. Faraggi, V. G. Matyas, and B. Percival, "D-term uplifts in
      nonsupersymmetric heterotic string models", Phys. Rev. D 108 (2023) no. 8, 086007,
      arXiv:2306.16878 [hep-th].

[43] L. A. Detraux, A. R. D. Avalos, A. E. Faraggi, and B. Percival, "Vacuum energy of
      nonsupersymmetric S~ heterotic string models", Phys. Rev. D 110 (2024) no. 8, 086006,
      arXiv:2407.19980 [hep-th].

[44] B. S. Acharya, F. Benini, and R. Valandro, "Fixing moduli in exact type IIA flux vacua",
      JHEP 02 (2007) 018, arXiv:hep-th/0607223.

[45] S. Baines and T. Van Riet, "Smearing orientifolds in flux compactifications can be OK",
      Class. Quant. Grav. 37 (2020) no. 19, 195015, arXiv:2005.09501 [hep-th].

[46] F. Saracco and A. Tomasiello, "Localized O6-plane solutions with Romans mass", JHEP 07
      (2012) 077, arXiv:1201.5378 [hep-th].

[47] D. Junghans, "O-Plane Backreaction and Scale Separation in Type IIA Flux Vacua", Fortsch.
      Phys. 68 (2020) no. 6, 2000040, arXiv:2003.06274 [hep-th].

[48] F. Marchesano, E. Palti, J. Quirant, and A. Tomasiello, "On supersymmetric AdS4 orientifold
      vacua", JHEP 08 (2020) 087, arXiv:2003.13578 [hep-th].

[49] O. DeWolfe, A. Giryavets, S. Kachru, and W. Taylor, "Type IIA moduli stabilization", JHEP
      07 (2005) 066, arXiv:hep-th/0505160.

[50] A. O. Atkin and J. Lehner, "Hecke operators on 0(m)", Mathematische Annalen 185 (1970)
      134�160.

[51] G. W. Moore, "ATKIN-LEHNER SYMMETRY", Nucl. Phys. B 293 (1987) 139. [Erratum:
      Nucl.Phys.B 299, 847 (1988)].

[52] K. R. Dienes, "Generalized Atkin-Lehner symmetry", Phys. Rev. D 42 (1990) 2004�2021.
[53] Y. Satoh and Y. Sugawara, "Notes on a vanishing cosmological constant without Bose�Fermi

      cancellation", PTEP 2022 (2022) no. 5, 053B04, arXiv:2111.09663 [hep-th].
[54] B. Valeixo Bento and M. Montero, "A No-go on dS minima from Casimir energies on

      Riemann-flat manifolds". In preparation, 2025.

                                                      � 114 �
[55] U. H. Danielsson, S. S. Haque, P. Koerber, G. Shiu, T. Van Riet, and T. Wrase, "De Sitter
      hunting in a classical landscape", Fortsch. Phys. 59 (2011) 897�933, arXiv:1103.4858
      [hep-th].

[56] U. H. Danielsson, G. Shiu, T. Van Riet, and T. Wrase, "A note on obstinate tachyons in
      classical dS solutions", JHEP 03 (2013) 138, arXiv:1212.5178 [hep-th].

[57] G. Shiu and Y. Sumitomo, "Stability Constraints on Classical de Sitter Vacua", JHEP 09
      (2011) 052, arXiv:1107.2925 [hep-th].

[58] X. Chen, G. Shiu, Y. Sumitomo, and S. H. H. Tye, "A Global View on The Search for de-Sitter
      Vacua in (type IIA) String Theory", JHEP 04 (2012) 026, arXiv:1112.3338 [hep-th].

[59] DESI Collaboration, A. G. Adame et al., "DESI 2024 VI: cosmological constraints from the
      measurements of baryon acoustic oscillations", JCAP 02 (2025) 021, arXiv:2404.03002
      [astro-ph.CO].

[60] DESI Collaboration, K. Lodha et al., "DESI 2024: Constraints on physics-focused aspects of
      dark energy using DESI DR1 BAO data", Phys. Rev. D 111 (2025) no. 2, 023532,
      arXiv:2405.13588 [astro-ph.CO].

[61] DESI Collaboration, M. Abdul Karim et al., "DESI DR2 Results II: Measurements of Baryon
      Acoustic Oscillations and Cosmological Constraints", arXiv:2503.14738 [astro-ph.CO].

[62] DESI Collaboration, K. Lodha et al., "Extended Dark Energy analysis using DESI DR2 BAO
      measurements", arXiv:2503.14743 [astro-ph.CO].

[63] P. Agrawal and G. Obied, "Dark Energy and the Refined de Sitter Conjecture", JHEP 06
      (2019) 103, arXiv:1811.00554 [hep-ph].

[64] S. Chen, D. van de Heisteeg, and C. Vafa, "Symmetries and M-theory-like Vacua in Four
      Dimensions", arXiv:2503.16599 [hep-th].

[65] D. Andriot, "Tachyonic de Sitter Solutions of 10d Type II Supergravities", Fortsch. Phys. 69
      (2021) no. 7, 2100063, arXiv:2101.06251 [hep-th].

[66] D. Andriot, P. Marconnet, M. Rajaguru, and T. Wrase, "Automated consistent truncations
      and stability of flux compactifications", JHEP 12 (2022) 026, arXiv:2209.08015 [hep-th].
      [Addendum: JHEP 04, 044 (2023)].

[67] D. Andriot, L. Horer, and P. Marconnet, "Charting the landscape of (anti-) de Sitter and
      Minkowski solutions of 10d supergravities", JHEP 06 (2022) 131, arXiv:2201.04152
      [hep-th].

[68] D. Andriot and F. Ruehle, "On classical de Sitter solutions and parametric control", JHEP 06
      (2024) 101, arXiv:2403.07065 [hep-th].

[69] M. Alishahiha, A. Karch, E. Silverstein, and D. Tong, "The dS/dS correspondence", AIP
      Conf. Proc. 743 (2004) no. 1, 393�409, arXiv:hep-th/0407125.

[70] V. Gorbenko, E. Silverstein, and G. Torroba, "dS/dS and T T ", JHEP 03 (2019) 085,
      arXiv:1811.07965 [hep-th].

[71] S. Sethi, "Supersymmetry Breaking by Fluxes", JHEP 10 (2018) 022, arXiv:1709.03554
      [hep-th].

                                                      � 115 �
[72] G. Dall'Agata and F. Zwirner, "Supersymmetry-breaking compactifications on Riemann-flat
      manifolds", 2025.

[73] M. Grana, "Flux compactifications in string theory: A Comprehensive review", Phys. Rept.
      423 (2006) 91�158, arXiv:hep-th/0509003.

[74] F. Denef, M. R. Douglas, and S. Kachru, "Physics of String Flux Compactifications", Ann.
      Rev. Nucl. Part. Sci. 57 (2007) 119�144, arXiv:hep-th/0701050.

[75] J. Bl�ab�ack, U. Danielsson, G. Dibitetto, and S. Giri, "Constructing stable de Sitter in
      M-theory from higher curvature corrections", JHEP 09 (2019) 042, arXiv:1902.04053
      [hep-th].

[76] L. E. Ibanez, V. Martin-Lozano, and I. Valenzuela, "Constraining Neutrino Masses, the
      Cosmological Constant and BSM Physics from the Weak Gravity Conjecture", JHEP 11
      (2017) 066, arXiv:1706.05392 [hep-th].

[77] Y. Hamada and G. Shiu, "Weak Gravity Conjecture, Multiple Point Principle and the
      Standard Model Landscape", JHEP 11 (2017) 043, arXiv:1707.06326 [hep-th].

[78] D. Gilbarg and N. Trudinger, Elliptic Partial Differential Equations of Second Order. Classics
      in Mathematics. Springer Berlin Heidelberg, 2001.
      https://books.google.com/books?id=eoiGTf4cmhwC.

[79] L. Evans, Partial Differential Equations. Graduate studies in mathematics. American
      Mathematical Society, 2010. https://books.google.com/books?id=Xnu0o_EJrCQC.

[80] G. B. D. Luca, N. De Ponti, A. Mondino, and A. Tomasiello, "Gravity from thermodynamics:
      Optimal transport and negative effective dimensions", SciPost Phys. 15 (2023) no. 2, 039,
      arXiv:2212.02511 [hep-th].

[81] S. Parameswaran and M. Serra, "On (A)dS solutions from Scherk-Schwarz orbifolds", JHEP
      10 (2024) 039, arXiv:2407.16781 [hep-th].

[82] J. Polchinski, String theory. Vol. 2: Superstring theory and beyond. Cambridge Monographs
      on Mathematical Physics. Cambridge University Press, 12, 2007.

[83] E. Witten, "On flux quantization in M -theory and the effective action", J. Geom. Phys. 22
      (1997) 1�13, arXiv:hep-th/9609122.

[84] S. P. de Alwis, "A Note on brane tension and M theory", Phys. Lett. B 388 (1996) 291�295,
      arXiv:hep-th/9607011.

[85] S. P. de Alwis, "Anomaly cancellation in M theory", Phys. Lett. B 392 (1997) 332�334,
      arXiv:hep-th/9609211.

[86] P. G. O. Freund and M. A. Rubin, "Dynamics of Dimensional Reduction", Phys. Lett. B 97
      (1980) 233�235.

[87] O. Aharony, O. Bergman, D. L. Jafferis, and J. Maldacena, "N=6 superconformal
      Chern-Simons-matter theories, M2-branes and their gravity duals", JHEP 10 (2008) 091,
      arXiv:0806.1218 [hep-th].

[88] S. Chen, G. W. Gibbons, Y. Li, and Y. Yang, "Friedmann's Equations in All Dimensions and
      Chebyshev's Theorem", JCAP 12 (2014) 035, arXiv:1409.3352 [astro-ph.CO].

                                                      � 116 �
 [89] T. W. Grimm, K. Mayer, and M. Weissenbacher, "Higher derivatives in Type II and M-theory
       on Calabi-Yau threefolds", JHEP 02 (2018) 127, arXiv:1702.08404 [hep-th].

 [90] T. W. Grimm, K. Mayer, and M. Weissenbacher, "One-modulus Calabi-Yau fourfold
       reductions with higher-derivative terms", JHEP 04 (2018) 021, arXiv:1712.07074 [hep-th].

 [91] Y. Hyakutake and S. Ogushi, "R**4 corrections to eleven dimensional supergravity via
       supersymmetry", Phys. Rev. D 74 (2006) 025022, arXiv:hep-th/0508204.

 [92] Y. Hyakutake, "Toward the Determination of R**3 F**2 Terms in M-theory", Prog. Theor.
       Phys. 118 (2007) 109, arXiv:hep-th/0703154.

 [93] Y. Hyakutake and S. Ogushi, "Higher derivative corrections to eleven dimensional
       supergravity via local supersymmetry", JHEP 02 (2006) 068, arXiv:hep-th/0601092.

 [94] J. M. Borwein, Lattice sums then and now. 150. Cambridge University Press, 2013.
 [95] L. S. Charlap, "Compact flat riemannian manifolds: I", Annals of Mathematics 81 (1965)

       no. 1, 15�30. http://www.jstor.org/stable/1970379.
 [96] N. Ashcroft and N. Mermin, Solid State Physics. Cengage Learning, 2011.

       https://books.google.com/books?id=x_s_YAAACAAJ.
 [97] J. J. Heckman and C. Vafa, "Fine Tuning, Sequestering, and the Swampland", Phys. Lett. B

       798 (2019) 135004, arXiv:1905.06342 [hep-th].
 [98] Y. Hamada, M. Montero, C. Vafa, and I. Valenzuela, "Finiteness and the swampland", J.

       Phys. A 55 (2022) no. 22, 224005, arXiv:2111.00015 [hep-th].
 [99] M. Delgado, D. van de Heisteeg, S. Raman, E. Torres, C. Vafa, and K. Xu, "Finiteness and

       the Emergence of Dualities", arXiv:2412.03640 [hep-th].
[100] C. Cid and T. Schulz, "Computation of five- and six-dimensional bieberbach groups.",

       Experimental Mathematics 10 (2001) no. 1, 109�115. http://eudml.org/doc/224616.
[101] P. Moeck, "On classification approaches for crystallographic symmetries of noisy 2d periodic

       patterns", IEEE Transactions on Nanotechnology 18 (2019) 1166�1173.
       http://dx.doi.org/10.1109/TNANO.2019.2946597.
[102] M. Montero and H. Parra de Freitas, "New supersymmetric string theories from discrete theta
       angles", JHEP 01 (2023) 091, arXiv:2209.03361 [hep-th].
[103] T. J. Laffey, "Lectures on integer matrices". Unpublished lecture notes, 1997.
       https://citeseerx.ist.psu.edu/documentrepid=rep1&type=pdf&doi=
       3dfe5776999aaee5e4663b8c06a332b19d41164d.
[104] L. S. Charlap and A. T. Vasquez, "Compact flat riemannian manifolds ii: The cohomology of
       zp-manifolds", American Journal of Mathematics 87 (1965) no. 3, 551�563.
       http://www.jstor.org/stable/2373062.
[105] R. G. Bettiol, A. Derdzinski, and P. Piccione, "Teichmu�ller theory and collapse of flat
       manifolds", Annali di Matematica Pura ed Applicata (1923-) 197 (2018) 1247�1268.
[106] B. S. Acharya, B. Fraiman, M. Montero, and H. Parra de Freitas, "Work in progress", 2025.
[107] I. D. Miatello and R. J. Miatello, "Isospectral compact flat manifolds", Duke Mathematical
       Journal 68 (1992) no. 3, 489 � 498. https://doi.org/10.1215/S0012-7094-92-06820-7.

                                                       � 117 �
[108] R. J. Miatello and J. P. Rossetti, "Flat manifolds isospectral on p-forms",
       arXiv:math/0303276 [math.DG]. https://arxiv.org/abs/math/0303276.

[109] K. Dekimpe, M. Sadowski, and A. Szczepan�ski, "Spin structures on flat manifolds",
       Monatshefte fu�r Mathematik 148 (2006) no. 4, 283�296.
       https://doi.org/10.1007/s00605-005-0367-3.

[110] B. Putrycz and A. Szczepan�ski, "Existence of spin structures on flat four-manifolds", Advances
       in Geometry 10 (2010) no. 2, 323�332. https://doi.org/10.1515/advgeom.2010.013.

[111] R. Lutowski and B. Putrycz, "Spin structures on flat manifolds", Journal of Algebra 436
       (2015) 277�291.

[112] G. Hiss and A. S. and, "Spin structures on flat manifolds with cyclic holonomy",
       Communications in Algebra 36 (2008) no. 1, 11�22.

[113] W. P. Thurston, "On the geometry and dynamics of diffeomorphisms of surfaces", Bulletin
       (New Series) of the American Mathematical Society 19 (1988) no. 2, 417 � 431.

[114] E. Witten, "GLOBAL GRAVITATIONAL ANOMALIES", Commun. Math. Phys. 100 (1985)
       197.

[115] R. P. Feynman, R. B. Leighton, and M. L. Sands, The Feynman Lectures on Physics, Vol. II:
       Mainly Electromagnetism and Matter. Addison-Wesley Pub. Co., Reading, Mass., 1966.
       Originally published 1963-1965.

[116] J. J. Heckman, J. McNamara, M. Montero, A. Sharon, C. Vafa, and I. Valenzuela, "Fate of
       stringy noninvertible symmetries", Phys. Rev. D 110 (2024) no. 10, 106001,
       arXiv:2402.00118 [hep-th].

[117] C. P. Burgess and F. Quevedo, "Perils of towers in the swamp: dark dimensions and the
       robustness of EFTs", JHEP 09 (2023) 159, arXiv:2304.03902 [hep-th].

[118] Y. Tachikawa and K. Yonekura, "Why are fractional charges of orientifolds compatible with
       Dirac quantization?", SciPost Phys. 7 (2019) no. 5, 058, arXiv:1805.02772 [hep-th].

[119] G. Mack, "D-independent representation of Conformal Field Theories in D dimensions via
       transformation to auxiliary Dual Resonance Models. Scalar amplitudes", arXiv:0907.2407
       [hep-th].

[120] J. Penedones, "Writing CFT correlation functions as AdS scattering amplitudes", JHEP 03
       (2011) 025, arXiv:1011.1485 [hep-th].

[121] R. Gopakumar, A. Kaviraj, K. Sen, and A. Sinha, "A Mellin space approach to the conformal
       bootstrap", JHEP 05 (2017) 027, arXiv:1611.08407 [hep-th].

[122] A. L. Fitzpatrick, J. Kaplan, J. Penedones, S. Raju, and B. C. van Rees, "A Natural Language
       for AdS/CFT Correlators", JHEP 11 (2011) 095, arXiv:1107.1499 [hep-th].

[123] A. A. Nizami, A. Rudra, S. Sarkar, and M. Verma, "Exploring Perturbative Conformal Field
       Theory in Mellin space", JHEP 01 (2017) 102, arXiv:1607.07334 [hep-th].

[124] E. M. Stein and G. Weiss, Introduction to Fourier Analysis on Euclidean Spaces (PMS-32).
       Princeton University Press, 1971. http://www.jstor.org/stable/j.ctt1bpm9w6.

                                                       � 118 �
[125] B. Osgood, Lectures on the Fourier Transform and Its Applications. Pure and Applied
       Undergraduate Texts. American Mathematical Society, 2019.
       https://books.google.com/books?id=T8GEDwAAQBAJ.

[126] S. S. Magliveras, T. van Trung, and W. Wei, "Primitive sets in a lattice", Austral. J. Comb.
       40 (2008) 173�186.

[127] L. E. Ibanez and A. M. Uranga, String theory and particle physics: An introduction to string
       phenomenology. Cambridge University Press, 2, 2012.

[128] E. Witten, "Fermion Path Integrals And Topological Phases", Rev. Mod. Phys. 88 (2016)
       no. 3, 035001, arXiv:1508.04715 [cond-mat.mes-hall].

[129] M. Fabinger and P. Horava, "Casimir effect between world branes in heterotic M theory",
       Nucl. Phys. B 580 (2000) 243�263, arXiv:hep-th/0002073.

[130] T. Gannon and C. S. Lam, "Can a lattice string have a vanishing cosmological constant?",
       Phys. Rev. D 46 (1992) 1710�1720, arXiv:hep-th/9201028.

[131] P. P. Ewald, "Die berechnung optischer und elektrostatischer gitterpotentiale", Annalen der
       Physik 369 (1921) no. 3, 253�287,
       https://onlinelibrary.wiley.com/doi/pdf/10.1002/andp.19213690304.
       https://onlinelibrary.wiley.com/doi/abs/10.1002/andp.19213690304.

[132] A. Y. Toukmaji and J. A. Board, "Ewald summation techniques in perspective: a survey",
       Computer Physics Communications 95 (1996) no. 2, 73�92.
       https://www.sciencedirect.com/science/article/pii/0010465596000161.

[133] B. Nijboer and F. De Wette, "On the calculation of lattice sums", Physica 23 (1957) no. 1,
       309�321. https://www.sciencedirect.com/science/article/pii/S0031891457921249.

[134] A. A. Buchheit, J. Busse, and R. Gutendorf, "Computation and properties of the epstein zeta
       function with high-performance implementation in epsteinlib", arXiv:2412.16317
       [math.NA]. https://arxiv.org/abs/2412.16317.

[135] R. W. Carter, "Conjugacy classes in the weyl group", Compositio Mathematica 25 (1972)
       no. 1, 1�59. http://eudml.org/doc/89111.

[136] J. Davighi, B. Gripaios, and O. Randal-Williams, "Differential cohomology and topological
       actions in physics", Adv. Theor. Math. Phys. 27 (2023) no. 7, 2045�2085, arXiv:2011.05768
       [hep-th].

[137] M. Etheredge, B. Heidenreich, S. Kaya, Y. Qiu, and T. Rudelius, "Sharpening the Distance
       Conjecture in diverse dimensions", JHEP 12 (2022) 114, arXiv:2206.04063 [hep-th].

[138] A. Castellano, I. Ruiz, and I. Valenzuela, "Stringy evidence for a universal pattern at infinite
       distance", JHEP 06 (2024) 037, arXiv:2311.01536 [hep-th].

[139] J. A. Harvey and G. W. Moore, "Superpotentials and membrane instantons",
       arXiv:hep-th/9907026.

[140] M. Dine and N. Seiberg, "Nonrenormalization Theorems in Superstring Theory", Phys. Rev.
       Lett. 57 (1986) 2625.

[141] M. Montero, T. Van Riet, and V. Venken, "Festina Lente: EFT Constraints from Charged
       Black Hole Evaporation in de Sitter", JHEP 01 (2020) 039, arXiv:1910.01648 [hep-th].

                                                       � 119 �
[142] M. Montero, C. Vafa, T. Van Riet, and V. Venken, "The FL bound and its phenomenological
       implications", JHEP 10 (2021) 009, arXiv:2106.07650 [hep-th].

[143] S. Caron-Huot, Y.-Z. Li, J. Parra-Martinez, and D. Simmons-Duffin, "Causality constraints on
       corrections to Einstein gravity", JHEP 05 (2023) 122, arXiv:2201.06602 [hep-th].

[144] C. G. Callan, Jr., C. Lovelace, C. R. Nappi, and S. A. Yost, "String Loop Corrections to beta
       Functions", Nucl. Phys. B 288 (1987) 525�550.

[145] C. Angelantonj and A. Sagnotti, "Open strings", Phys. Rept. 371 (2002) 1�150,
       arXiv:hep-th/0204089. [Erratum: Phys.Rept. 376, 407 (2003)].

[146] E. Dudas, G. Pradisi, M. Nicolosi, and A. Sagnotti, "On tadpoles and vacuum redefinitions in
       string theory", Nucl. Phys. B 708 (2005) 3�44, arXiv:hep-th/0410101.

[147] S. Raucci, Spacetime aspects of non-supersymmetric strings. PhD thesis, Pisa, Scuola Normale
       Superiore, 9, 2024. arXiv:2409.19395 [hep-th].

[148] N. Benjamin, H. Ooguri, S.-H. Shao, and Y. Wang, "Light-cone modular bootstrap and pure
       gravity", Phys. Rev. D 100 (2019) no. 6, 066029, arXiv:1906.04184 [hep-th].

[149] M. Ono, "Classification of Lattices With Z(m) Symmetry", Commun. Math. Phys. 126 (1989)
       25.

[150] R. Koo, "A classification of matrices of finite order over c, r and q", Mathematics Magazine 76
       (2003) no. 2, 143�148. http://www.jstor.org/stable/3219311.

[151] D. Andriot, "Phantom matters", arXiv:2505.10410 [hep-th].
[152] T. Rudelius, "Conditions for (No) Eternal Inflation", JCAP 08 (2019) 009,

       arXiv:1905.05198 [hep-th].
[153] D. Andriot and L. Horer, "(Quasi-) de Sitter solutions across dimensions and the TCC

       bound", JHEP 01 (2023) 020, arXiv:2208.14462 [hep-th].
[154] A. Hebecker and T. Wrase, "The Asymptotic dS Swampland Conjecture - a Simplified

       Derivation and a Potential Loophole", Fortsch. Phys. 67 (2019) no. 1-2, 1800097,
       arXiv:1810.08182 [hep-th].
[155] D. Andriot, D. Tsimpis, and T. Wrase, "Accelerated expansion of an open universe and string
       theory realizations", Phys. Rev. D 108 (2023) no. 12, 123515, arXiv:2309.03938 [hep-th].
[156] D. Andriot, N. Cribiori, and T. Van Riet, "Scale separation, rolling solutions and entropy
       bounds", arXiv:2504.08634 [hep-th].
[157] B. Friedrich, A. Hebecker, and D. Schiller, "Localized Gravity, de Sitter, and the Horizon
       Criterion", arXiv:2505.07934 [hep-th].
[158] X. Dong, B. Horn, E. Silverstein, and G. Torroba, "Micromanaging de Sitter holography",
       Class. Quant. Grav. 27 (2010) 245020, arXiv:1005.5403 [hep-th].
[159] Several Greek Philosophers. Ancient sources, around 5th century B.C.
       https://antigonejournal.com/2023/09/ancient-greeks-earth-round/.
[160] B. Heidenreich, M. Reece, and T. Rudelius, "Sharpening the Weak Gravity Conjecture with
       Dimensional Reduction", JHEP 02 (2016) 140, arXiv:1509.06374 [hep-th].

                                                       � 120 �
[161] T. P. Lambert, J. G. Ratcliffe, and S. T. Tschantz, "Closed flat riemannian 4-manifolds",
       arXiv:1306.6613 (2013) .

[162] I. J. Zucker and M. M. Robertson, "Exact values of some two-dimensional lattice sums",
       Journal of Physics A: Mathematical and General 8 (1975) no. 6, 874.

[163] J. Borwein and P. Borwein, Pi and the AGM: A Study in Analytic Number Theory and
       Computational Complexity. Wiley, 1998.
       https://books.google.com/books?id=UynfQwAACAAJ.

[164] I. J. Zucker, "Exact results for some lattice sums in 2, 4, 6 and 8 dimensions", Journal of
       Physics A: Mathematical, Nuclear and General 7 (1974) no. 13, 1568.

[165] T. van Ritbergen, A. N. Schellekens, and J. A. M. Vermaseren, "Group theory factors for
       Feynman diagrams", Int. J. Mod. Phys. A 14 (1999) 41�96, arXiv:hep-ph/9802376.

[166] H. Weyl, The classical groups: their invariants and representations. Princeton university
       press, 1946.

[167] A. N. Schellekens and N. P. Warner, "Anomalies, Characters and Strings", Nucl. Phys. B 287
       (1987) 317.

                                                       � 121 �
