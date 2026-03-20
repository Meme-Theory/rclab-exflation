# SM Constants Relationships 2025

**Source:** `12_SM_Constants_Relationships_2025.pdf`

---

Evidence of Relationships Among Fundamental Constants of the Standard Model

                                                                                          S. V. Chekanova, H. Kjellerstrandb

                                                                             aHEP Division, Argonne National Laboratory, 9700 S.Cass, Lemont, 60516, IL, USA
                                                                                           bhakan.org, Sodra Forstadsgatan 40b, Malmo, 21143, Sweden

arXiv:2509.07713v1 [hep-ph] 9 Sep 2025  Abstract

                                        This paper presents an approach to reducing the number of fundamental parameters in the Standard Model (SM) using genetic
                                        programming, a machine learning technique based on evolutionary algorithms. We outline the core principles of our method
                                        and identify the simplest analytic relationships among SM parameters. Our results suggest that the SM parameters associated
                                        with quark and boson masses are not randomly distributed, but instead follow a hierarchical structure within a high-dimensional
                                        functional space. The found analytic solution depends on only two input parameters, representing the simplest mathematical model
                                        that could provide a foundation for developing a future theoretical framework to address the SM.

                                        Keywords: Standard Model constants, quarks, vector bosons, genetic programming, artificial intelligence
                                        PACS: 11.15.-q, 12.15.-y, 12.38.-t, 14.65.-q, 14.70.-e, 06.20.Jr, 06.20.Jr

                                        1. Introduction                                                     too complex for the traditional analysis of symbolic expressions
                                                                                                            employed here. Therefore, our focus is on analytical expres-
                                           The Standard Model (SM) is considered a model rather than        sions derived from constants with physical units. This choice
                                        a complete theory, as it relies on more than 20 fundamental pa-     significantly limits the number of possible solutions.
                                        rameters that must be determined experimentally [1]. This lim-
                                        its its potential for observing new phenomena in particle col-         The aim of this paper is to identify the simplest analytic so-
                                        lisions. Attempts for identification of relationships among the     lutions that align with the general expectations of the SM, and
                                        SM constants have a long history [2, 3, 4], but no convincing ev-   to eliminate spurious relations that arise due to numerical noise.
                                        idence has been found to support the existence of such relation-    For this work, the GP approach was enhanced to incorporate di-
                                        ships. For example, analytic connections between quark masses       mensional analysis -- a capability that was not available for the
                                        are not part of the SM itself. These constants are regarded as      original publication [5]. This technical advancement enables
                                        free parameters, with no obvious underlying connections.            the identification of relevant analytic solutions while ensuring
                                                                                                            the verification of physical units and the preservation of dimen-
                                           When a theory is missing to describe apparently unconnected      sional consistency.
                                        values, the first step is to identify the simplest analytic rela-
                                        tionships between such variables, before constructing a theory         This paper reports on analytic relations between the funda-
                                        based on specific physics principles. In the case of SM pa-         mental constants of the SM that can be regarded the simplest
                                        rameters, this task is complex as it involves many parameters,      mathematical model. They may serve as a basis for a future
                                        some of which carry physical units. The first step in this physics  theory that will describe SM fundamental constants with a min-
                                        program was undertaken in [5] using symbolic regression and         imal number of free parameters.
                                        genetic programming (GP) - a type of evolutionary algorithm
                                        inspired by natural selection and rooted in the broader field       2. Search strategy
                                        of artificial intelligence (AI). The symbolic regression evolves
                                        analytic expressions directly from data [6]. By representing           Table1 lists the fundamental SM parameters commonly used
                                        mathematical expressions as trees and applying evolutionary         in particle physics, as reported by the PDG [1]. These constants,
                                        algorithms, GP explores a wide solution space unconstrained         including those with physical units (e.g., in MeV), are used as
                                        by predefined model structures, enabling the discovery of com-      inputs for GP. Unlike Ref. [5], the masses are not rescaled by
                                        plex, previously hidden relationships.                              the -meson mass, as the limitation due to dimensional analysis
                                                                                                            has been overcome in the present work.
                                           This study relies on the analytic relations created by GP and
                                        reported in [5]. The datasets derived from dimensionless SM            A well-known feature of the SM is that the masses of
                                        constants are well-suited for mathematical reasoning by Large       fermions, as well as those of the Z and W bosons, approach
                                        Language Models (LLMs) and other AI methods, but they are           zero when the Higgs boson mass is set to zero. This behavior
                                                                                                            arises due to their dependence on the Higgs vacuum expecta-
                                             Email addresses: [email redacted] (S. V. Chekanov),            tion value, mediated through Yukawa couplings, which are free
                                        [email redacted] (H. Kjellerstrand)                           parameters [7]. This imposes a certain structure for the possible
                                                                                                            relations between the SM parameters.
Table 1: Physics fundamental constants from the PDG [1] used for the GP al-              Let us elaborate on the last point. This step introduces a prac-
gorithm. We require that the uncertainties for me,  and -1 are at most a factor       tical level of precision for candidate solutions. However, it is
100 higher than for the Higgs boson mass. Making them more precise should             important to note that high numerical precision does not nec-
                                                                                      essarily translate to theoretical significance. For example, al-
not contribute to the results. The table presents both the absolute uncertainties     though the number  can be calculated at an extraordinary num-
(�) and the relative uncertainties (�rel, in percent). When the PDG reports           ber of decimal places, it is still just an irrational number, and the
                                                                                      usage of all its digits is not essential for a physical theory, since
an asymmetric uncertainty, the largest value is used.                                 digits beyond a certain level of precision have no observable
                                                                                      effect on physical processes. It has already been observed [5]
Constant            Name        Value         �    �rel (%)                           that the current precision for the electron mass shown in Table 1
PI                           3.14159       1e-05     0.0003                           does not lead to the GP solutions that satisfy (1) - (3), thus its
Fine-struct. (inv)           137.036       0.001     0.0007                           precision should be reduced.
s at Z0                -1      0.1180     0.0009     0.7627
CKM constants           S    no units                                                    Finally, it is important to note that if we aim to express pre-
12-mix angle                 0.22501          �    �rel (%)                           cisely known masses analytically in terms of parameters that
23-mix angle           12    0.04183    0.00068      0.3022                           are known with a lower precision, there are fundamental limi-
13-mix angle           23   0.003732    0.00079      1.8886                           tations. The technical challenge of deriving high-precision out-
CP-viol. phase         13               9 � 10-5     2.4116                           puts from low-precision inputs cannot be fully overcome, and
Mass                            1.147                2.2668                           this must be kept in mind when evaluating candidate solutions.
electron mass                    MeV       0.026
muon mass                   0.510998          �    �rel (%)                              Previously, the GP algorithm identified several simple ana-
 mass                   me   105.658                 0.0002                           lytic relations [5] connecting quark and the Z/W boson masses
u-quark mass            m�   1776.93        10-6     0.0009                           to the Higgs mass. In the Picat implementation [6], a limitation
d-quark mass            m         2.16     0.001     0.0051                           of the GP required converting masses to dimensionless values
s-quark mass            mu        4.70       0.09    3.2407                           by rescaling with the  meson mass, which served as an auxil-
c-quark mass            md        93.5       0.07    1.4894                           iary parameter.
b-quark mass            ms     1273.0        0.07    0.8556
t-quark mass            mc       4183                0.3614                              In this work, we address this limitation by automatically per-
Z-boson mass            mb    172560          0.8    0.1673                           forming dimensional analysis. Our approach, referred to as the
W-boson mass            mt   91188.0          4.6    0.1796                           "GP method", is based on the analytic snippets from symbolic
H-boson mass           mZ    80369.2                 0.0022                           regression discussed in [5], followed by post-processing steps
                       mW     125200            7    0.0165                           to enforce the conditions 1. - 4. In the search for possible solu-
                       mH                    310     0.0879                           tions, expressions containing integer constants greater than 10
                                              2.0                                     were disregarded, as well as those in which one mass is related
                                             13.3                                     to another mass with the appearance of a single rational num-
                                             110                                      ber serving as a coefficient of proportionality, without any other
                                                                                      physical constants from Table 1. The reason for this is a large
   Based on the discussion above, we adopt the following strat-                       number of rational numbers for multiplication to derive other
egy to identify the simplest relations between the SM constants:                      masses, leading to a large number of spurious expressions.

  1. Pass dimensional analysis: All solutions must pass di-                           3. Results
      mensional analysis. Since our target is particle masses,
      the expressions on the right-hand side should have units of                        The GP method yields the following simplest solution con-
      MeV.                                                                            necting the SM masses with the Higgs mass:

  2. Behavior in the Limit mH  0: All solutions for particle
      masses should approach zero values as mH  0. In partic-
      ular, we will focus on solutions in which a given mass is
      proportional to the Higgs mass.

3. Simplicity criterion: Among all possible solutions, we                             mu = mH /(3 (-1)2),         r = 17, (1)
   choose the ones that are the simplest, i.e. with the smallest                      md = mH 133/2/6,            r = 22, (2)
   rank defined in [5]. It is reasonable to assume that any                           ms = mH 13/5,               r = 12, (3)
   theory capable of unifying all these parameters, if it exists,                     mc = mH 113/2/6,            r = 17, (4)
   should be formulated as simply as possible, employing the                          mb = mH 9 13 (1 - 13),      r = 21, (5)
   fewest parameters and the least mathematical complexity.                            mt = mH ( + /5),           r = 16, (6)
   If there are several solutions with similar analytic ranks,                        mW = mH/ arctan((10 - )2),  r = 22, (7)
   we prefer the one that uses a constant already encountered                         mZ = mW  cos( - 1),         r = 22. (8)
   before, thus avoiding the introduction of a new parameter,
   even if the overall analytic rank may slightly increase.

4. Refinement by precision reduction: If no acceptable so-                            The analytic rank, denoted by the letter r and defined in [5],
   lution is found for a particular mass, we reduce the preci-                        is indicated for each relation. The total rank of this system of
   sion required for that mass and repeat the GP search.                              equations is 149. It is calculated as the sum of all individual

                                                                                   2
ranks. For the found solution, 8 masses are connected via mH           mu = me ( + 1),      r = 10,  (9)
and 3 other parameters: -1,  and 13 from Table 1. The mass             md = mu ( + 1),
of mZ agrees with the PDG value when using  = 1.1472, i.e.             ms = md (6 + 1),     r = 10,  (10)
within its experimental uncertainty. Note that the connection          mc = ms (4 + 1),
between mZ with mH was not found.                                      mb = mc ( + 1/7),    r = 16,  (11)
                                                                        mt = mb ( + 10),
   We have also found a second solution, but its overall rank          mW = mt /( + 1),     r = 16,  (12)
was much higher, 154. Another, a third solution, had a lower           mZ = mW  cos( - 1),
total rank 137, but the price to pay was the introduction of a                              r = 17,  (13)
new parameter, S .
                                                                                            r = 16,  (14)
   The obtained relations are the result of the GP method, thus
all masses agree with Table 1 within the PDG uncertainties. It                              r = 11,  (15)
is interesting that when expressing the masses via the Higgs
mass, the parameter 13 becomes a dominant constant, which                                   r = 22.  (16)
may suggest certain dynamical effect.
                                                                       The analytic rank of each relation is indicated. The sum of
   We also identified relations in which each mass was propor-         these ranks is 118. For these 8 relations, the fundamental
tional to mt, mW , or mZ. The calculated total analytic ranks were     masses are expressed using only me and . Setting me = 0
142, 142, and 141, respectively. We did not find a solution with       forces all these masses to vanish, in accordance with our main
fewer than three functional arguments. Thus, such solutions are        search criterion - that the Higgs mass determines the masses of
consistent in terms of analytic complexity with Eqs. (1)�(8).          all leptons, quarks, and vector bosons. To continue the same
                                                                       logic when an equation contains a lower-mass particle, the GP
   The individual relations in which each mass is proportional         method reports the following relations: mH = mW (6/(5 - ))
to me have ranks in the range 18�23. However, we could not             and mt = mH ( + 1)/3.
obtain a complete system of relations for all 8 masses, since no
solution has been found in which mW is proportional to me.

4. Alternative solution                                                   The alternative solution Eqs. (9)-(16) differs drastically from
                                                                       Eqs. (1)�(8). It suggests that the equations become analyti-
   In general, we expect a large number of possible solutions,         cally simpler when the masses are related through a hierarchical
which are tedious to examine without dedicated AI analyses. In         chain, from low to high mass, rather than when each mass is di-
this study, we have chosen to focus on the simplest case, where        rectly proportional to the Higgs mass (or to the mt, mW or mZ
the masses exhibit a hierarchical dependence on one another            mass). In addition, this alternative solution has only two mea-
and are not directly related to the Higgs mass. In this case, one      sured parameters ( and me), with a prominent appearance of 
can treat me as the argument that defines the mass of the light        and ( � 1). The latter may suggest a mathematical pattern, po-
quarks. Although such a relation is unknown in the SM, it is           tentially indicative of underlying physical mechanism or some
proposed in the Grand Unified Theories (see [8] for a review).         hidden symmetry.

   The GP identifies the relation mu = me ( + 1) as having                According to the definitions of the GP algorithm, the equa-
the smallest analytic rank of 6, while preserving the dimen-           tions Eqs. (9)-(16) hold true considering each argument to be
sional condition. The above solution satisfies our requirement         taken from Table 1. However, when considering them as a
of mu = 0 when mH  0, since the electron mass in the SM is             self-contained system of equations, they exhibit some discrep-
proportional to the Higgs mass through the Yukawa coupling.            ancies with the experimental masses. The input values me =
                                                                       0.510998(1) and  = 1.147(26) for Eqs. (9)�(16) lead to some
   In the alternative model, all particle masses were arranged         tensions with Table 1 when each mass is evaluated using the
in increasing order, starting with quarks (from the up quark to        preceding expressions. This is because small shifts within the
the top quark) and then vector bosons (W and Z). In the SM,            uncertainty of each mass pile up in the hierarchy of relations.
the top quark decays almost exclusively via a W boson (and a           For example, the accumulation of the shifts in the chain of the
b quark), since the weak interaction couples quarks of different       values produces mZ = 87827 MeV, which is far away from the
generations through the CKM matrix. Therefore, it is natural           nominal mass of the Z boson. Thus, Eqs. (9)�(16), with a total
to expect a connection between the mt and mW masses. The               rank of 118, can be considered an ideal simplest mathematical
top quark and the Z boson are also linked in the SM, as the            model obtainable by the GP method.
Z boson couples directly to a top�antitop pair. Furthermore,
the masses of W and Z bosons in the SM are related at tree                The solution for the above problem can be the following.
level via mW = mZ cos(A), where A is the Weinberg angle [7].           Since we already know how the structure of the relations should
Thus, the GP approach encounters an ambiguity regarding the            look, one can re-run the GP method a second time, when using
relationship between mW , mZ, and mt.                                  the masses as input for each relation in the chain Eqs. (9)-(16),
                                                                       and vary the input parameter  within its allowed experimental
   Our analysis of the GP results finds the simplest solution that     range. The obtained solution is:
links each mass to the preceding one:

                                                                    3
                     r = 17,         (17)                                   We ran the GP algorithm and searched for the solutions that
mu = me 4 ,                                                              passed the dimensional analysis and have the following charac-
md = mu ( + 1),      r = 10,         (18)                                teristics:
ms = md 9 tan(),
mc = ms (4 + 1),     r = 18,         (19)                                 (a) Solutions where every constant with a physical unit is pro-
mb = mc ( + 1/7),                                                              portional to another constant with the unit, that is, c, d, e or
 mt = mb ( + 10),    r = 16,         (20)                                      f . For example, one solution is where all three constants d,
mW = mt /( + 1),                                                               e and f are proportional to c, such that they vanish when
mZ = mW  cos( - 1),  r = 16,         (21)                                      c  0. Note that there are several combinatorial com-
                                                                               binations of this structure. Such solutions are similar to
                     r = 16,         (22)                                      Eqs. (1) - (8).

                     r = 11,         (23)                                (b) Solutions organized in hierarchical order, from lowest to
                                                                               highest values, but proportional to a value of the previous
                     r = 22,         (24)                                      relation, i.e. as in Eq. (25), or similar to Eqs. (9) - (16).

assuming  = 1.1471, i.e. within the allowed uncertainty. This            Complete sets of equations with the behavior (a), with 3 rela-
set of relations has the required property: Each derived mass            tions in each, were not found up to the analytical rank of 40
is within the experimental uncertainty, and uses the mass cal-           of the individual expressions, suggesting that the total analytic
culated from the preceding expression. The total analytic rank           ranks of the "non-hierarchical" system are significantly larger
is 126. It is somewhat larger than for Eqs. (9)-(16), but it is          than for Eq. (25). Most of the separate relations, which did not
still substantially smaller than for Eqs. (1)-(8), or any solution       form a complete solution with a set of 3 equations in each, had
where mt, mZ or mW are used as the multiplicative factor.                the analytic ranks 18 and above.

   Although the above relations precisely reproduce the mea-                The GP method found the solution (b), identical to Eq. (25),
sured masses from Table 1, one can obtain simpler relations for          with the lowest rank 32 among all possible solutions. We re-
the light-quarks masses, by sacrificing their accuracy. It should        peated this test with several values generated using Eq. (25),
be mentioned that the masses of light quarks are the least pre-          including uniform relative uncertainties, and for each test we
cisely measured. They are evaluated indirectly in the specific           could identify this system of relations. Thus, if the underlying
subtraction scheme (MS ), and are somewhat contentious [1].              mathematical behavior exhibits a hierarchical structure of con-
Often, the elegance of a mathematical description is more im-            nected values, similar to Eq. (25), it would be observed in this
portant than an exact match to experimental values. However,             exact form when analyzing the GP relations. Solutions of the
since we do not have a guiding physics principle for simplify-           type (a) would not be preferable, as their analytic ranks are sig-
ing these relations, we will refrain from proposing relations for        nificantly higher than those of (b). This test confirms that the
light quarks with lower analytic ranks.                                  GP method accurately reproduces the underlying mathematical
                                                                         relationships.
5. Closure test
                                                                         6. Random sampling test
It is important to check how well the analytic rank reflects
                                                                            It was also examined whether the preference for the chain
the underlying connection between masses -- i.e., whether the            structure (b) (or Eq. (9)�(16)), over the multiplicative solution
                                                                         (a) is merely an artifact of the ordering of relative experimen-
small overall analytic rank observed for Eq. (9) - (16) is a reflec-     tal errors in Table 1, since these errors typically decrease with
                                                                         increasing SM mass.
tion of the existing functional structure. We used the following
                                                                            We created 15 pseudo-experiments. Each experiment had 19
simple benchmark model with six constants defined by the con-            parameters with the same names as in Table 1. The values of
                                                                         the CKM constants and the masses of quarks and bosons were
nected equations:                                                        generated using a uniform random distribution in the range
                                                                         [di - Xii, di + Xii], where di are the nominal SM constants,
                                                                         i are the corresponding experimental uncertainties, and Xi are
d = c a, e = d (2 + ), f = e b - e.  (25)                                scaling factors chosen to ensure sufficient random smearing.
                                                                         The Xi was set to 20 for the CKM matrix and the u-quarks mass.
Here, d, e and f are determined by a, b and c constants. The             Then Xi is increased by 20 for every subsequent mass, i.e. it is
total analytic rank of this mathematical model is 32. The input          set to 40 for the d-mass, 60 for the s-mass and so on, up to 180
for GP was created by Eq. (25) as:                                       for the Higgs mass. This approach provides significant ran-
                                                                         dom smearing of the values around the nominal SM constants,
a = 9.15(2), b = 5.24(1),                                                but prevents overlap in values, i.e. it preserves the hierarchical
c = 3.335(1) u, d = 10.088(2) u,                                         structure of masses, from the smallest mass for the u-quarks to
e = 51.868(5) u, f = 219.92(1) u,

where a, b and c are selected arbitrarily. a and b do not have
physical units, while other values have the same physical unit
denoted with "u". The uncertainties are given in round brackets.
Note that the uncertainties of d, e and f are not given by the
equations but are set to reproduce the experimental behavior of
uncertainties similar to the SM masses, i.e. in the decreasing
order relative to masses.

                                                                      4
Ca                                                                                 (b)             Picat
                                                   Cb
885500 (a)        Picat                                                        550000     Standard Model
                                                                                          Standard Model (adjusted)
880000      Standard Model                                                     440000     Random variations
775500      Random variations
770000
665500                                                                         330000
660000
555500                                                                         220000
550000
445500                                                                         110000
                                                                                      00
00 0.2 0.4 0.6 0.8 11 1.2                                                                 0.2 0.4 0.6 0.8 11 1.2
         Nr of missing equations                                                             Nr of missing equations

              (a) Solution type (a).                                                        (b) Solution type (b).

Figure 1: The summary of random variations of the SM parameters around their nominal values (open symbols). The Y-axis shows the total complexity of the
system of equations, C, defined as the product of the total analytic rank and the number of free parameters. The filled symbols show the system of equations using
SM parameters, i.e. Eqs. (1) - (8) (Fig. 1a) and Eqs. (9) - (16) (Fig. 1b). The symbols marked with "adjusted" indicate the solution Eqs. (17) - (24). The randomized
data were processed with the help of a Picat code and then the solution type (a) and (b) were found. When some relations cannot be identified, C cannot be compared
on equal footing with the values of the complete equation systems.

the heaviest mass for the t-quarks. For every random value, the                for the solutions that miss one or two relations. Such missing
uncertainties were re-calculated to maintain the same relative                 relations are most often associated with the mt, mW , and mZ
uncertainties �rel as in Table 1. We limit the GP production                   masses.
of analytic relations only to the SM masses, producing about
400,000 snippets per random test. Each set required 5,000 CPU                     We did not attempt to use random data to reconstruct the
hours with the Intel E5-2650 v4 processor for the Picat program                "connected" system, as shown in Eqs. (17)�(24), where each
[9]. The produced GP analytic snippets are available in [10].                  mass depends on the previously calculated one. The results are
Then, solution types (a) and (b) were automatically identified                 expected to be essentially identical to those shown in Fig. 1b,
within the generated GP data.                                                  apart from minor adjustments in the relations involving the least
                                                                               precisely determined light-flavor quark masses.
   First, we checked the analytic connection between mZ and
mH, which was not found for the SM parameters in Sect. 3.                         According to these tests, it was concluded that obtaining the
However, we did find such expressions in 4 out of 15 random                    complete set of 8 relations using the solution (b) (Eqs. (9) -
sets, indicating that the probability of observing such relations              (16)) is more difficult, than for the solutions (a) (Eqs. (1) - (8)).
is not small. After this test, we focus only on the relationship               However, the solution (b) is easier to find with fewer free pa-
between mZ and mW , as in Eq. (8) and (16).                                    rameters, though many such solutions do not lead to systems
                                                                               with 8 equations. One test for the solution (a) showed a better
   The summary of random variations of the SM parameters                       total rank, with 3 independent variables, see Fig. 1a. But this
around their nominal values is presented in Fig. 1. The rela-                  random dataset has the value Cb = 287 in Fig. 1b, which is far
tions were searched up to the analytical rank 40 of the indi-                  from Cb = 118 of the SM solution type (b).
vidual relations. The X-axis represents the completeness of the
system of relations, with 0 indicating full completeness. The Y-                  To estimate the probability of observing the overall func-
axis shows the analytic rank of the equation system multiplied                 tional complexity of Eqs. (1)�(8) and (9)�(16) from the 15 ran-
by the number of free parameters, denoted with the symbol C.                   dom tests, we calculated the distribution of Ca + Cb for each
When calculating the number of free parameters, we do not in-                  test. In cases where one relation was not found, we calculated
clude mH (for the solution (a)) and me (for the solution (b)).                 Ca,b from the incomplete system of equations, incrementing the
These two masses are used for setting all masses to zero to sat-               number of free parameters by one, treating it as a hidden vari-
isfy the SM requirement. The value of Ca (for the solution (a))                able that restores the full set of equations. The resulting dis-
or Cb (for the solution (b)) serves as a measure of the complex-               tribution was symmetric, consistent with a normal distribution,
ity of the system of relations. This value, however, is unknown1               with a mean of 890 and a width of 125. For comparison, the

1We do not exclude the existence of the solutions beyond rank 40, but such     expressions are expected to be complex, and may not be too useful for our
                                                                               comparison.

                                                                            5
SM corresponds to a total complexity value of Ca + Cb = 565,           connection to the vacuum expectation value, all other masses
which was obtained adding 146 � 3 (for Eqs. (1)�(8)) and 118           also become zero.
(for Eqs. (9)�(16)). The probability of obtaining a value as low
as 565 from the random tests, assuming a one-sided normal dis-            One remarkable observation is that the SM parameters prefer
tribution, is 0.46%. For the most likely solution (b) and Fig. 1b,     to be related in a chain of equations, i.e. each mass is connected
the distribution of Cb has a mean of 304 and a width of 76. The        to a particle with a lower mass, rather than to the Higgs boson
one-sided probability of observing Cb  118 is 0.72%. Thus,             mass directly. This "hierarchical" structure exhibits the lowest
our tests provide evidence against the possibility of reproducing      analytic rank among all combinations examined in this paper. It
Eqs. (1)�(8) and (9)�(16) in the random experiments by chance.         is also interesting that the dominant constant in Eq. (1) - (8) is
A stronger conclusion may be possible in the future with greater       13, while the alternative solution Eq. (9) - (16) is dominated by
CPU availability and a more autonomous evaluation of the GP            ( � 1) and the constant . Our tests provide statistical evidence
expressions using AI.                                                  that values randomly smeared around the nominal SM constants
                                                                       are unlikely to reproduce the complexity of the two proposed
   In summary, we conclude that the obtained GP relationships          systems of equations.
among the SM parameters are unlikely to be numerical arti-
facts, but rather carry the signature of an underlying theory that        All of the above suggests that the SM parameters are not en-
unifies these fundamental constants.                                   tirely random. Instead, they are likely interconnected within a
                                                                       high-dimensional functional space, pointing to an underlying
7. The lepton masses                                                   dynamical mechanism or symmetry pattern that has yet to be
                                                                       fully understood.
   The lepton masses are the most difficult part of the analysis.
The GP method could not identify connections of the electron              In the alternative solution, the eight masses of the SM par-
mass with the Higgs mass, unless the experimental uncertainty          ticles (six quarks and two vector bosons) are expressed using
on the electron mass is drastically increased, and we have to          only two constants:  and me. This represents a substantial
use our 4th principle "Refinement by precision reduction" men-         reduction in the number of free parameters. It should be em-
tioned in Sect. 2. We assume that me is the input free parameter       phasized that the found system of relations is a simplest mathe-
to define the other lepton masses. At the lowest analytical rank,      matical model guided by the data from GP, rather than a physics
the mass of muons and -leptons can be relatively well repro-           model, since assumptions about specific symmetry principles or
duced by the GP method:                                                dynamical features were not used. We find these results suffi-
                                                                       ciently intriguing, as they demonstrate the potential in reducing
               m� = mt             -1    (26)                          the number of the SM constants to just a few. Whether these
                        -1 5 + -1                                      expressions constitute a viable theoretical framework, or will
                                      ,                                continue to hold as the precision of measured SM constants im-
                                                                       proves, remains to be studied in the future.
               m = mH 1/-1 + 1/(-1 + 8)  (27)
                                                                       Acknowledgments
leading to the evaluated value of 105.659 MeV and
1776.14 MeV. Although such masses are slightly outside the                The submitted manuscript has been created by UChicago Ar-
modern experimental uncertainties, their values are still quite        gonne, LLC, Operator of Argonne National Laboratory ("Ar-
precise. The analytic rank 21 and 20 of these expressions, on          gonne"). Argonne, a U.S. Department of Energy Office of
average, are higher than for the most expressions related to the       Science laboratory, is operated under Contract No. DE-AC02-
quark masses.                                                          06CH11357. Argonne National Laboratory's work was funded
                                                                       by the U.S. Department of Energy, Office of High Energy
8. Conclusion                                                          Physics under contract DE-AC02-06CH11357.

   We present a promising method based on genetic program-             References
ming for uncovering underlying mathematical relationships di-
rectly from data. The first step follows a traditional symbolic         [1] Particle Data Group Collaboration, S. Navas, et al., Re-
regression approach: deriving analytical expressions from the                view of particle physics, Phys. Rev. D 110 (3) (2024)
data and generating a large set of candidate relations [5]. The              030001. doi:10.1103/PhysRevD.110.030001.
second step involves identifying simplest connecting patterns
among these relations, dominated by numerical coincidences.             [2] S. Weinberg, Dreams of a Final Theory, Pantheon Books,
This step leverages dimensional analysis and general SM ex-                  1994.
pectations to reveal possible analytic structures within a high-
dimensional functional space.                                           [3] H. B. Nielsen, C. Surlykke, S. E. Rugh, Seeking inspira-
                                                                             tion from the standard model in order to go beyond it, in:
   The above method was applied to the fundamental constants                 4th Hellenic School on Elementary Particle Physics, 1994,
that are presently treated in the SM as free parameters. We                  pp. 476�501. arXiv:hep-th/9407012.
considered two possible solutions that satisfy the key feature
of the SM: when the Higgs mass mH is set to zero, due to its

                                                                    6
[4] C. D. Froggatt, H. B. Nielsen, Trying to under-

stand the standard model parameters, Surveys

in High Energy Physics 18 (1�4) (2003) 55�75.

doi:10.1080/0142241032000156559.

URL    http://dx.doi.org/10.1080/

0142241032000156559

[5] S. V. Chekanov, H. Kjellerstrand, Discovering the under-
     lying analytic structure within Standard Model constants
     using artificial intelligence (2025). arXiv:2507.00225.

[6] J. R. Koza, Genetic Programming, MIT Press, 1992.

[7] S. Weinberg, A model of leptons, Phys. Rev. Lett. 19

(1967) 1264�1266. doi:10.1103/PhysRevLett.19.

1264.

URL    https://link.aps.org/doi/10.1103/

PhysRevLett.19.1264

[8] S. Raby, Grand Unified Theories, in: 2nd World Sum-
     mit: Physics Beyond the Standard Model, 2006. arXiv:
     hep-ph/0608183.

[9] N.-F. Zhou, H. Kjellerstrand, J. Fruhman, Picat pro-
     gramming language, https://picat-lang.org, [On-
     line; accessed September 10, 2025] (2013).

[10] S. V. Chekanov, H. Kjellerstrand, GC4PhysicalConstants
      - Genetic computing for physical constants, https:
      //github.com/chekanov/GC4PhysicalConstants,
      GitHub Repository (2025).

                                                               7
