# Holographic Limitations QI 2024

**Source:** `25_Holographic_Limitations_QI_2024.pdf`

---

arXiv:2310.09377v1 [math.CO] 13 Oct 2023        Off-diagonal online size Ramsey numbers for paths

                                                                            Malgorzata Bednarska-Bzde�ga

                                            Faculty of Mathematics and CS, Adam Mickiewicz University, Poznan�, Poland

                                                                                    October 17, 2023

                                                                                                          Abstract

                                                      Consider the following Ramsey game played on the edge set of KN. In every round, Builder
                                                  selects an edge and Painter colours it red or blue. Builder's goal is to force Painter to create
                                                  a red copy of a path Pk on k vertices or a blue copy of Pn as soon as possible. The online
                                                  (size) Ramsey number r~(Pk, Pn) is the number of rounds in the game provided Builder and
                                                  Painter play optimally. We prove that r~(Pk, Pn)  (5/3 + o(1))n provided k = o(n) and
                                                  n  . We also show that r~(P4, Pn)  7n/5 - 1 for n  10, which improves the upper bound
                                                  obtained by J. Cyman, T. Dzido, J. Lapinskas, and A. Lo and implies their conjecture that
                                                  r~(P4, Pn) = 7n/5 - 1.

                                          1 Introduction

                                          Let G and H be finite graphs. Consider the following game R~(G, H) played on the infinite board
                                          KN (i.e. the board is a complete graph with the vertex set N). In every round, Builder chooses a
                                          previously unselected edge of KN and Painter colours it red or blue. The game ends when there is
                                          a red copy of G or a blue copy of a H on the board. Builder aims to finish the game as soon as
                                          possible, while Painter tries to avoid a red G and a blue H as long as possible. By r~(G, H) we denote
                                          the number of rounds in the game R~(G, H), provided both players play optimally and we call it the
                                          online size Ramsey number for G and H. In the literature online size Ramsey numbers are called
                                          also online Ramsey numbers. The online size Ramsey numbers r~(G, H) are game counterparts of
                                          well known size Ramsey numbers; the size Ramsey number r^(G, H) is the minimum number of edges
                                          in a graph with the property that every two-colouring of its edges results in a red copy of G or a
                                          blue copy of H. Clearly r~(G, H)  r^(G, H).

                                              In this paper we study online size Ramsey numbers for G = Pk and H = Pn, where Pt denotes
                                          a path on t vertices. Games in which Builder tries to force Painter to create a monochromatic
                                          path were considered also in other variants: the induced version of the online Ramsey number was
                                          studied in [3], ordered path games on the infinite (ordered) complete graph and hypergraphs � in
                                          [1] and [6]. Studying size Ramsey numbers for paths has much longer history. Let us mention the
                                          breakthrough result by Beck [2] that r^(Pn, Pn) is linear. This result implies that also r~(Pn, Pn) is
                                          linear, as well as r~(Pk, Pn) for a fixed k, since r~(Pk, Pn)  r^(Pk, Pn) and we have also an easy general
                                          bound r~(G, H)  |E(G)| + |E(H)| - 1. However, it seems not easy to find a multiplicative constant
                                          c (if exists) such that r~(Pk, Pn) = cn + o(n). In general, we have r~(Pk, Pn)  2n + 2k - 7 for every
                                          k, n  2, proved by Grytczuk, Kierstead and Pralat [5], while the best lower bound for n  k  5

                                                                                                         1
is r~(Pk, Pn)  3n/2 + k/2 - 7/2 by Cyman, Dzido, Lapinskas and Lo [4]. Thus we know that
3n/2 + o(n)  r~(Pk, Pn)  2n + o(n) for k fixed and n  . The authors of [4] posed the following
conjecture.

Conjecture 1.1 ([4]). For every k  5

                              r~(Pk, Pn)  3 if n  .
                                      n   2

We make a step towards this conjecture and prove that r~(Pk, Pn)  5n/3 + o(n).

Theorem 1.2. Let n, k  N and k  5. Then

                                             5     +  12k.
                              r~(Pk, Pn)      n
                                             3

    We made no effort to optimise the constant 12 in this theorem. Section 3 contains the proof.
    There are very few exact results for r~(Pk, Pn). It is known that r~(P3, Pn) = 5(n - 1)/4 for n  3
([4]) and there are computer calculated numbers r~(Pk, Pn) for all k, n  9 by Pralat [7]. It is proved
in [4] that 7n/5 - 1  r~(P4, Pn)  7n/5 + 9 for n  4 and the authors conjectured that the lower
bound is tight.

Conjecture 1.3 ([4]). For every n  4

                                             7        - 1.
                              r~(P4, Pn) =    n
                                             5

    In view of the above mentioned computer calculation, the conjecture is true for n  9. We prove
that it is true also for n  10, by improving the upper bound in [4].

Theorem 1.4. For every n  10

                                                7
                              r~(P4, Pn)         n - 1.
                                                5

    We prove this theorem in Section 5. Our argument is inductive, technically quite complicated,
and it is quite different from the argument in [4]. Lately Theorem 1.4 has been proved independently
by Yanbo Zhang and Yixin Zhang [8].

2 Preliminaries

For a graph H = (V, E), we put v(H) = |V | and e(H) = |E|. By the sum of graphs G and G we
mean the union G  G = (V (G)  V (G), E(G)  E(G)).

    We say that a graph H is coloured if every its edge is blue or red. A graph is red (or blue) if all its
edges are red (blue). We assume that also  is a coloured graph, which is somewhat non-standard.
Thus it may happen that a coloured graph or a subgraph of a coloured graph has 0 vertices.

    Let H be a coloured graph. By a component of H we mean a maximal (in sense of inclusion)
connected coloured subgraph contained in H. If A, B  V (H), then EH(A, B) denotes the set of all
coloured edges of H with one end in A and the other end in B.

    Given n  k  2, and a coloured graph H (it may be empty), consider the following auxiliary
game RRH(Pk, Pn). The board of the game is KN, with exactly e(H) edges coloured and these edges
induce a copy of H in KN. The rules of selecting and colouring edges by Builder and Painter are

                                                               2
the same as in the standard game R~(Pk, Pn), however, Painter is not allowed to colour an edge red
if that would create a red Pk. Builder wins RRH(Pk, Pn) at the moment a blue copy of Pn appears
on the board. It is not hard to observe that if Builder has a strategy such that RR(Pk, Pn) ends
within at most t rounds, then Builder in R~(Pk, Pn) can apply such a strategy as well and finish the
game within at most t rounds.

    After every round of RRH(Pk, Pn), the coloured graph induced by all edges coloured in the game
so far (including the edges of H) is called the host graph. We say a vertex of KN is free in a round
of the game if it is not a vertex of the host graph.

    We say that Builder forces an edge uw blue if he selects uw and Painter has to colour it blue
according to the rules of the game, i.e. one of u, w, say u, is an end of a red path on k - 1 vertices,
all distinct from w.

3 Proof of Theorem 1.2

Let n, k  N and k  5. It is enough to show a strategy for Builder in RR(Pk, Pn) such that the
game ends after at most 5n/3 + 12k rounds,

    In order to simplify the description of Builder's strategy, we assume that Builder can select an
edge already coloured. In such a round Painter "colours" it with the same colour the edge already
had. Clearly allowing such moves cannot help Builder and may only increase the length of the game.

    We divide the game RR(Pk, Pn) into three stages. Roughly speaking, in the first stage Builder
creates many blue paths on 3 vertices. In the second stage he connects them into at most k - 1
longer paths, while in the last stage he connects a small number of blue paths into a blue path Pn.
In order to simplify the description of all three stages, we present a few lemmata.

Lemma 3.1. Let n, k  N and T = n/3 + k. Builder has a strategy in RR(Pk, Pn) such that after
at most 3T + 2(k - 1) rounds the host graph contains T blue, vertex-disjoint paths of length 2.

Proof. We will describe the strategy of Builder based on a definition of active and inactive edges.
After every round we will call every coloured edge either active or inactive. An active edge may
become inactive after a few rounds but an inactive edge stays inactive forever. Given a round of the
game, the coloured graph induced by all active edges is called the active graph, while by the inactive
graph we mean the coloured graph induced by all inactive edges. Here is the inductive definition of
active and inactive edges.

    Before the first round there are no active nor inactive edges and the active and inactive graphs
are empty sets. Let t  0 and suppose that after t rounds we have the active graph A and the
inactive graph I. In the next round Builder chooses an end x of a longest red path P in the active
graph (if A = , then x is any free vertex) and selects xy, where y is any free vertex of the board.

    Suppose Painter colours xy red. It means that P had less than k - 2 vertices, otherwise a red Pk
would have appeared. Then the red edge xy becomes active. After the (t + 1)-th round the set of
active edges is E(A)  {xy} and E(I) is the set of inactive edges.

    Suppose Painter colours xy blue. Then we have two possibilities. First assume there is a blue
edge e = xy incident to x. Then the edges xy and e become inactive. If P has a positive length,
then the red edge xx, with some x  V (P ), also becomes inactive. Let S = {xy, e, xx} if P has a
positive length; otherwise let S = {xy, e}. Hence after the (t + 1)-th round the set of active edges is
E(A) \ S, while E(I)  S is the set of inactive edges.

    Assume now that there is no blue edge e = xy incident to x. Then the edge xy becomes active.
After the (t + 1)-th round the set of active edges is E(A)  {xy} and E(I) is the set of inactive edges.

                                                               3
    Builder continues selecting edges in the above way until the graph induced by all blue inactive
edges has at least n + 3k vertices, then he stops. Let us verify that such a strategy satisfies the
assertion of the lemma.

    A routine inductive argument implies that after every round of the game the following holds.

Proposition 3.2. After every round (until Builder stops the game) the active graph A and the
inactive graph I satisfies the following conditions.

  (i) E(A)  E(I) = .

(ii) No inactive blue edge has an endpoint in V (A).

(iii) A is a sum of a red path P on less than k vertices and a blue matching M such that every edge
      of M has exactly one end in V (P ).

(iv) I is the sum of vertex-disjoint blue paths of length 2 and at most m red edges, where m is the
       number of these paths.

    It follows from the above proposition that the game ends at the moment that the inactive graph
I contains exactly (n + 3k)/3 = n/3 + k = T blue, vertex-disjoint paths of length 2 and at most
T red edges. At this moment the active graph A has less than 2(k - 1) edges, in view of part (iii)
of the proposition. Thus Builder obtains the required T blue paths within less than 3T + 2(k - 1)
rounds.

    The following definition will be useful in two next lemmata. Given s, d, m  N with d  s  m,
we say that a coloured graph F is an essential (s, d, m)-graph, if it contains s vertex-disjoint paths
G1, G2, . . . , Gs satisfying the following conditions.

  (i) The paths G1, G2, . . . , Gs =  are blue.

(ii) F contains a red path P = u1u2 . . . ud on d vertices such that ui is an end of the path Gi, for
     i = 1, 2, . . . d.

(iii)  s     v(Gi)  =    m.
       i=1

Then we say that F has the essential red path P and s essential blue paths G1, . . . , Gs.

Lemma 3.3. Suppose that 1  d < k  s  m and after some rounds of the game there is an essential

(s, d, m)-graph present on the board, its essential blue paths are G1, G2, . . . , Gs and P = u1u2 . . . ud is
its essential red path P . Assume that in the next round Builder selects the edge udud+1, where ud+1 is
an end of the path Gd+1. Then after every response of Painter there is an essential (s, d, m)-graph
on the board such that either d = d + 1 and s = s, or s = s - 1 and d  {d, d - 1}.

Proof. Let us consider two possible situations after colouring udud+1 by Painter. If udud+1 is red,

then P  = P  {udud+1} is a red path on d = d + 1 vertices. It is not hard to verify that the sum

of s blue paths Gi and the red path P  is an essential (s, d, m)-graph that satisfies the required

conditions.

Suppose that udud+1 is blue. Then we define blue paths Gi = Gi for i = 1, 2, . . . , d - 1, Gd =

Gd  Gd+1  {udud+1} and Gi = Gi+1 for i = d + 1, d + 2. . . . , s - 1. We also define ends ui of the

paths Gi such that ui = ui for i = 1, 2, . . . , d - 1 and ui = ui+1 for i = d + 1, d + 2. . . . , s - 1, while ud

is one of the ends of Gd . As for the red path, we put P  = u1u2 . . . ud-1 if d  2; otherwise P  = u1 .

Thus the red path P  has d = 1 or d - 1 vertices, we have s - 1 vertex-disjoint blue paths Gi and
s                   s
i=1    v(Gi )  =    i=1  v(Gi  ).  Thus  the  sum  of  the  red  path  P  and  the  blue  paths  G1, . . . , Gs-1  satisfies

the required conditions.

                                                            4
Lemma 3.4. Let n, k, T  N and G be a coloured graph containing T blue, vertex-disjoint paths of
length 2. Builder has a strategy in RRG(Pk, Pn) such that after at most 2T - k rounds the host graph
contains less than k blue, vertex-disjoint paths on 3T vertices in total.

Proof. Let B  G be the sum of T blue, vertex-disjoint paths of length 2. Then B is a (T, 1, 3T )-
essential graph, with the essential red path of length 0, consisting of an end of the first path of B.
Without loss of generality we assume that G = B.

    If T < k, the Builder in RRB(Pk, Pn) achieves his goal without making any move. Otherwise,
Builder selects the edges according to Lemma 3.3, as long as the number of essential blue paths is
at least k. In view of this lemma, we can have rounds of two kinds: when the length of the essential
red path increases (and the number of essential blue paths does not grow) or when the number of
essential blue paths decreases (while the length of the essential red path changes by at most 1). A
round of the first kind will be called a red-round while a round of the second kind � a blue-round.

    We will prove that after 2T - k rounds or sooner the assertion of the lemma holds. Assume for a
contradiction that at the end of the (2T - k)-th round the number of essential blue paths is at least
k. It means that there where at most T - k rounds such that the number of essential blue paths
decreased. Hence the number of rounds such that the length of the essential red path increased was
at least T . Thus the length of the essential red path at the end of the (2T - k)-th round is at least
T - (T - k) = k, which contradicts the rules of RRG(Pk, Pn).

    Thus after at most 2T - k rounds the host graph contains a sum B of less than k vertex-disjoint,
blue paths such that v(B) = v(B) = 3T , what follows from Lemma 3.3.

    Next two lemmata, useful in the analysis of the third stage, need a definition of a fence.
    Given s, d, m  N with s  m, a coloured graph F is called an (s, d, m)-fence, if it contains s
vertex-disjoint paths G1, G2, . . . , Gs satisfying the following conditions.

  (i) The path G1 = w1 . . . wdwd+1 . . . wj has at least one vertex, the path P = w1 . . . wd is red, while
       the path G0 = wdwd+1 . . . wj is blue.

(ii) Paths G2, . . . , Gs =  are blue.

(iii) v(G0) +  s    v(Gi)  =  m.
               i=2

Then we say that F has the red picket P and s blue pickets G0, G2, . . . , Gs.

Lemma 3.5. Suppose that m, s  2, d  1, and there is an (s, d, m)-fence on the board. Then
Builder can play in such a way that after two rounds the host graph contains an (s, d, m)-fence such
that m  m - 1 and either d  d + 1 and s  s, or s  s - 1 and d  d - 1.

Proof. Suppose there is an (s, d, m)-fence on the board, with the red picket P = w1 . . . wd and blue
pickets G0, G2, . . . , Gs. Assume that wd is an end of G0, while u2, u2 are the ends of G2. Builder
selects the edge wdu2.

First assume that Painter colours wdu2 red. Then in the next round Builder selects the same

edge wdu2. After this pair of rounds we define a red path P  = w1 . . . wdu2 and the blue paths

G0 = G2, G2 = G0 \ {wd}, Gi = Gi for i = 3, 4, . . . , s. The paths G1 = G0  P , G2, G3 , . . . , Gs
                                                                  s
are vertex-disjoint, the red path P  has d + 1 vertices, v(G0) +  i=2  v(Gi     )  =  m  -  1,  and  among

G0, G2 , G3 , . . . , Gs only G2 may be the empty set. So is: Gi= Gi is an (s, d + 1, m - 1)-fence with
s  {s, s - 1}.

    Now assume that Painter colours wdu2 blue. Then in the next round Builder selects the edge
wd-1u2 , provided d  2 (if d = 1, then Builder selects the same edge wdu2). Painter colours it red or

                                        5
blue. After thise pair of rounds we define a red path P  in the following way: If d = 1, then P  = u2 ;

otherwise if wd-1u2 is red, then P  = w1 . . . wd-1u2, while if wd-1u2 is blue, then P  = w1 . . . wd-1.

We also define blue paths Gi = Gi for i = 3, 4, . . . , s and a path G0: if wd-1u2 is red or d = 1,

then G0 = G0  G2  {wdu2}; if wd-1u2 is blue, then G0 = G0  G2  {wdu2, wd-1u2}. Notice that

the paths G1 = G0  P , G3, G4 , . . . , Gs are vertex-disjoint, the red path P  has d or d - 1 vertices,
           s
v(G0 ) +   i=3  v(Gi)      {m, m  +  1},  and  every   path  G0 , G2 , G3, . . . , Gs  has  at  least  one  vertex.  So

G1 +  s    Gi  is  an  (s  -  1, d, m)-fence  with  d    d  and  m    m.
      i=3

In both cases the assertion follows.

Lemma 3.6. Let n, k, t  N and G be a coloured graph containing a sum B of t blue, vertex-disjoint
paths. Then Builder has a strategy in RRG(Pk, Pn) such that after at most 4t + 2k rounds the host
graph contains a blue path on at least v(B) - 2t - k vertices.

Proof. Without loss of generality we assume that G = B. Observe than B consisting of t blue,
vertex-disjoint paths is a (t, 1, v(B))-fence, provided we define the red picket of length 0 to consist
of an end of the first path of B.

    Builder in RRB(Pk, Pn) selects the edges according to Lemma 3.5, as long as the number of blue
pickets is at least 2. In view of this lemma, we have pairs of rounds of two kinds: when the length of
the red picket increases (and the number of blue pickets does not grow) or when the number of blue
pickets decreases (while the length of the red picket decreases by at most 1). A pair of rounds of the
first kind will be called a red pair of rounds while a pair of rounds of the second kind � a blue-pair
of rounds. After every pair of rounds (red or blue) the sum of the number of vertices in blue pickets
decreases by at most one.

    We will prove that after at most 2t + k pairs of rounds Builder achieves his goal. Assume for
a contradiction that at the end of (2t + k)-th pair of rounds there are at least two blue pickets. It
means that there where at most t - 2 blue-pairs of rounds. Hence the number of red-pairs of rounds
was greater than t + k. Thus the length of the red picket is greater than (t + k) - (t - 2) > k, which
contradicts the rules of RRG(Pk, Pn).

    Thus after at most 2(2t + k) = 4t + 2k rounds the host graph contains only one blue picket and,
in view of Lemma 3.5, the number of its vertices is at least v(B) - (2t + k).

We are ready to prove the main theorem.

Proof of Theorem 1.2. We present Builder's strategy in the game RR(Pk, Pn) in three stages. Let
T = n/3 + k.

Stage 1.

    Builder plays according to a strategy whose existence is guaranteed by Lemma 3.1 and within at
most 3T + 2(k - 1) rounds he obtains a coloured graph G containing T blue, vertex-disjoint paths
of length 2. The game proceeds to the second stage, equivalent to the game RRG(Pk, Pn).
Stage 2.

    In this stage Builder selects the edges according to Lemma 3.4 and within at most 2T - k rounds
of Stage 2 he obtains a coloured graph G containing a sum B of t < k blue, vertex-disjoint paths,
such that v(B) = 3T . The game proceeds to the third stage, equivalent to the game RRG(Pk, Pn).
Stage 3.

    In the last stage Builder applies a strategy from Lemma 3.6 and after at most 4t + 2k rounds of
Stage 3 the host graph contains a blue path P on at least v(B) - 2t - k vertices. Then Stage 3 ends.

                                                         6
    Let us analyse the host graph after all three stages of the game. For the blue path P obtained at
the end of Stage 3 we have

v(P )  v(B) - 2t - k > v(B) - 3k = 3T - 3k  n + 3k - 3k = n.

The number of rounds in all stages is not greater than

                                                        n               5
(3T + 2(k - 1)) + (2T - k) + (4t + 2k)  5T + 7k - 6 < 5 + k + 7k = n + 12k.
                                                        3               3

So a blue path on n vertices was created within at most 5n/3 + 12k rounds and the proof of Theorem
1.2 is complete.

4 Tools for studying the P4 versus Pn game

Before the proof of Theorem 1.4 we need a few additional definitions and lemmata.
    If G and G are coloured graphs and G  G, then we denote by RedG(G) and BlueG(G) the

sets of all red edges and blue edges of G respectively, with at least one end in V (G). After every
round of a game RRH(P4, Pn), if G is the host graph, for every coloured graph G  G we define
Red(G) = RedG(G) and Blue(G) = BlueG(G).

    Let c1, c2, . . . , ck  {b, r} be consecutive edge colours of a coloured path Pk+1. Then the coloured
path is called a c1c2 . . . ck-path. Suppose P  KN is a blue path with ends x1, x2, and there is a red
path of length li  0 with an end xi, for i = 1, 2. Then P is called a blue (l1, l2)-path and xi is
called its li-end. The coloured path u1u2 . . . ukuk+1  KN such that k  2, the edge ukuk+1 is red
and u1u2 . . . uk is a blue (2, 0)-path with a 2-end uk, will be called an extended (2, 0)-path with the
blue end u1, the transition vertex uk and the red end uk+1.

    Here are two examples of coloured graphs containing a (1, 1)-path P with V (P ) = {u1, u2, u3, u4, u5}
and 1-ends u1, u5:

u1 u2 u3 u4 u5                                          u1 u2 u3 u4 u5

    Below there are two examples of coloured graphs containing an extended (2, 0)-path P on the
vertex set V (P ) = {u1, u2, u3, u4, u5, u6}, with the blue end u1, the red end u6 and the transition
vertex u5:

u1 u2 u3 u4 u5 u6                                       u1 u2 u3 u4 u5 u6

The following coloured graph with one red and three blue edges will be called a limb.
                                               x1 x2 x3 x4

                                                           x5

    Suppose that H is a coloured graph that contains vertex-disjoint coloured subgraphs G0, G1, G2, L
satisfying the following conditions.

                                                               7
(A) Either L = , or L is a limb and it is a component of H.

(B) Either V (G0) = , or G0 is a blue path on at least one vertex such that G0  RedH(G0) is a

component of G. Furthermore |RedH(G0)|     2  v(G0)      - 1.
                                           5

(C) G2 =  or G2 is an extended (2, 0)-path on at least three vertices. Either G1 = , or G1

is a blue (1, 1)-path on at least one vertex such that neither of its 1-ends is adjacent in G

to any of: the blue end of G2, the transition vertex of G2, the red end of G2. Furthermore

BlueH(G1  G2) \ E(G1  G2) =  and |RedH(G1  G2)|                 2  v(G1    G2)     .
                                                                5

(D) The set of all blue edges of H is equal to BlueH(G0  G1  G2  L).

(E) The set of all red edges of H is equal to RedH(G0  G1  G2  L).

(F) 5 | v(G0) or 5 | v(G1  G2).

Then we call H a good graph with essential subgraphs (G0, G1, G2, L). We say that V (L)  V (G0) 
V (G1)  V (G2) is the set of essential vertices of H and denote the number of essential vertices of H
by ess(H). A good graph is very good if it satisfies the additional condition

(G) 5 | v(G0) and 5 | v(G1  G2).

    By a simple good graph we mean a good graph such that at least three of its essential subgraphs
are empty sets. Similarly we define a simple very good graph H, if H is a very good graph.

    Below we present some observations, following immediately from the definition of a good graph,
which will be often used, sometimes implicitly, in the paper.

Proposition 4.1. Suppose that k  N and H is a good graph with essential subgraphs (G0, G1, G2, L).
Then the following holds.

(i) The number of red edges of H is not greater than  2  ess(H  )  and, if G0 = , not greater than
                                                      5
2
5  ess(H    )     - 1. The number of blue edges of H is not greater than ess(H) - 1.

(ii) e(H)      7  ess(H  )  - 1.
               5

(iii) H \ G0 is a good graph, also H \ L is good. If H is very good, then also H \ G0 and H \ L are
      very good.

(iv) If 5 | v(H), then H is very good.

(v) If H is a sum of a blue path P on k  1 vertices and at most          2  k  - 1 red edges incident
                                                                         5
to the path, then H is a simple good graph, with k essential vertices and essential subgraphs

(P, , , ). Furthermore, if 5 | k, then H is simple very good.

(vi) If H is a sum of a blue (1, 1)-path P on k  1 vertices and at most         2  k  red edges incident
                                                                                5
to the path, then H is a simple good graph, with k essential vertices and essential subgraphs

(, P, , ). Furthermore, if 5 | k, then H is simple very good.

(vii) If H is a sum of an extended (2, 0)-path P on k  3 vertices and at most         2  k  red edges
                                                                                      5
incident to the path, then H is a simple good graph, with k essential vertices and essential

subgraphs (, , P, ). Furthermore, if 5 | k, then H is simple very good.

                                        8
    We omit the uncomplicated justification of Proposition 4.1. The following lemma says, among
other things, that two disjoint very good graphs can be efficiently connected by Builder, if one of
them is simple and different from a limb.

Lemma 4.2. Suppose that H is a very good graph and H is a simple good graph with its essential

subgraph different from a limb. Then Builder has a strategy in RRHH(P4, Pn) such that after a
finite number of rounds the graph G induced by all coloured edges of the board is a good graph with
ess(H) + ess(H) vertices.

    Furthermore, if H is a simple very good graph, then the resulting graph G is very good.

Proof. Let (G0, G1, G2, L) be essential subgraphs of H. Since H is very good, we have 5 | v(G0) and
5 | v(G1  G2).

    We split the argument into a few parts, depending on the essential subgraph of H. If H = ,
the assertion trivially holds so let H = .

Case 1. H has the essential subgraphs (, P, , ).

    Thus P is a blue path (1, 1)-path on at least 1 vertex and, in view of Condition (C), we have
|RedH(P )|  2v(P )/5. If G1 =  then, since 5 | v(G0), clearly H  H is a good graph with
essential subgraphs (G0, P, G2, L). Thus the required good graph is obtained without any move in
the game.

    Assume further that G1 = . Let x, y be the 1-ends of P and u1, u1 be the 1-ends of G1. Builder
in RRHH(P4, Pn) forces the edge xu1 blue. Then a blue (1, 1)-path G1 with 1-ends u1 , y appears
on the board and it has v(G1) + v(P ) vertices. Let G be the host graph at this moment. Since
5 | v(G1  G2), we have

|RedG(G1  G2)|  =                                             2   2
                   |RedH (G1  G2)| + |RedH(P )|  5 v(G1  G2) +     v(P )

                                                                  5

                =  2                        =  2  v(G1    G2)  .
                   5 v(G1) + v(P ) + v(G2)     5

Furthermore RedG(G0) = RedH(G0), BlueG(G0) = BlueH(G0), RedG(L) = RedH(L), BlueG(L) =

BlueH(L), and 5 | v(G0) by the assumption that H is very good, so in view of the above estimation
of |RedG(G1  G2)|, we conclude that G is a good graph with essential subgraphs (G0, G1 , G2, L) and
ess(G) = ess(H) + ess(H).

Case 2. H has the essential subgraphs (, , P, ).

    Thus P is an extended (2, 0)-path on at least 3 vertices, with |RedH(P )|  2v(P )/5. If G2 = ,
then H  H is the required good graph, with essential subgraphs (G0, G2, P, L). Assume further that

G2 = .

    Let y, x, z be the blue end, the red end and the transition vertex of P , respectively. Similarly, let
u2 , u2, w2 be the blue end, the red end and the transition vertex of G2.

    Builder in RRHH(P4, Pn) forces the edge zu2 blue. Then we obtain an extended (2, 0)-path G2
on the vertex set V (G2  (P \ {x}), with its blue end y and its red end u2, and the blue (1, 1)-path

on one vertex x.
    If G1 = , we define G1 = x; otherwise let u1, u1 be the 1-ends of G1. In the latter case, in the

next round Builder forces the edge xu1 blue and we define G1 = G1  {xu1}. In both cases G1 is a
blue (1, 1)-path on the vertex set V (G1)  {x}. Let us estimate the number of red edges incident to
vertices of G1  G2 at this moment of the game, bearing in mind the assumption 5 | v(G1  G2). We

                   9
have

      |Red(G1  G2)|  =  |RedH(P )| + |RedH (G1  G2)|              2          2
                                                                   v(P )  + 5 v(G1  G2)

                                                                  5

                     =  2       G1        G2)    =  2  v(G1    G2)  .
                         v(P                        5
                        5

As in the previous case, adding a blue edge xu1 to the host graph does not change the set of edges
incident to any vertex of G0 and L, and we have 5 | v(G0), thus the obtained host graph is a good
graph with essential subgraphs (G0, G1, G2, L), with ess(H) + ess(H) essential vertices.
Case 3. H has the essential subgraphs (P, , , ).

    Thus P is a blue path on at least 1 vertex and |RedH(P )|  2v(P )/5 - 1. If G0 =  then,
since 5 | v(G1  G2), clearly H  H is a good graph with essential subgraphs (P, G1, G2, L). Thus
the required good graph is obtained at once.

    Assume further that G0 = , u0, u0 are the ends of G0 and x, y are the ends of P . Builder starts
RRHH(P4, Pn) with selecting the edge xu0.

    If Painter colours xu0 blue, then we obtain a blue path G0 on v(G0) + v(P ) vertices and

      |Red(G0 )|     =                                      2             2       -1
                        |RedH(G0)| + |RedH(P )|  5 v(G0) - 1 +             v(P )

                                                                          5

                     =  2                      -2<     2  v(G0 )  - 1.
                        5 (v(G0) + v(P ))              5

The above estimation and the fact that adding the blue edge xu0 does not affect the set of edges

incident to G1, G2 or L, implies that for 5 | v(G1  G2), the obtained host graph is a good graph
with essential subgraphs (G0 , G1, G2, L) and v(G0) + v(G1  G2) + v(L) = ess(H) + ess(H) essential
vertices.

    Now assume that Painter colours xu0 red. Then Builder selects yu0 . If Painter colours it blue,
then a blue (1, 1)-path G1 with 1-ends u0, x appears on the board. Suppose Painter colours yu0 red.
Then, if P has more than one vertex, Builder forces the edge yu0 blue, and thereby obtains a blue
(1, 1)-path P  with 1-ends u0 , x. If P has only one vertex, we get an extended (2, 0)-path P , with
its blue end u0 and its red end x, containing the red edge u0x. In all cases the obtained path P  has
v(G0) + v(P ) vertices and, since at most two new red edges (incident to vertices of P ) were selected

in the game, we have

      |Red(P )|                                                2          2       -1+2
                     |RedH(G0)| + |RedH(P )| + 2  5 v(G0) - 1 +            v(P )

                                                                          5

                 =   2                    =  2 v(P ) .
                     5 (v(G0) + v(P ))       5

Let H be the sum of P  and all (at most two) red edges selected in the game. Then the above
estimation and Proposition 4.1(vi),(vii) imply that H is a simple good graph. Furthermore, in view

of Proposition 4.1(iii), the graph H \ G0 is very good. Let F be the host graph at this moment of the
game. Observe that F is the sum of (H \ G0) and H and all assumptions of Lemma 4.2 are fulfilled
by the graphs H \ G0 and H. We have already proved Lemma 4.2 if the simple good graph contains
an extended (2, 0)-path (Case 2) or a blue (1, 1)-path (Case 1) so we argue that after a few rounds

of RRF (P4, Pn) the obtained host graph is a good graph such that its number of essential vertices is

ess(H\G0)+ess(H) = v(G1G2)+v(L)+v(P ) = v(G1G2)+v(L)+v(G0)+v(P ) = ess(H)+ess(H).

                                             10
Hence the first part of the assertion follows.

    The second part of the assertion is a consequence of Proposition 4.1(iv) and the fact that if both
graphs H and H are very good, then 5 | ess(H) + ess(H).

The next lemma is crucial to the inductive argument in the proof of Theorem 1.4.

Lemma 4.3. Suppose that n  10, 5  k  n, 5 | k, and H is a coloured graph. Assume that H is
good and has k - 5 essential vertices. Then Builder has a strategy in RRH(P4, Pn) such that after a
finite number of rounds the host graph is a very good graph with k essential vertices.

Proof. Suppose that H satisfies the assumption of the lemma and has essential subgraphs (G0, G1, G2, L).

Note that H is very good, in view of 4.1(iv).

Suppose   that      KN  contains  the  coloured  graph  H  and   K       KN  is  the  complete    graph,  vertex-
                                                                    N
                                                                                       of K ,
disjoint  from  H.  Builder  starts  RRH (P4, Pn)  by selecting  two   adjacent edges          N  say  ab and bc.

We consider all Painter's responses.

Case 1. ab and bc are red.

    Builder selects edges ax and cy for any free, distinct x, y  V (K ). According to the rules of the
                                                                                                                                  N

game RRH(P4, Pn), Painter has to colour them blue so the brrb-path is obtained:

                                       xab cy

Then Builder forces xc blue and the following coloured graph appears:
                                                 xab cy

Thus it contains an extended (2, 0)-path ycxab. In view of Proposition 4.1(vii), the coloured graph
H induced by the five edges selected in the game is a simple very good graph with five essential
vertices. Since the host graph at this moment is the sum of vertex-disjoint very good graphs H and
H, we can apply Lemma 4.2 and we infer that Builder can continue the game so that after some
rounds the host graph is a very good graph, with ess(H) + ess(H) = k essential vertices.

Case 2. ab and bc are blue.

    In the next two rounds Builder selects edges cx and xy for any free, distinct x, y  V (K ). Let
                                                                                                                                                                                   N

us consider four cases, depending on Painter's response.
    If Painter colours them blue, we obtain a blue path H = abcxy such that no red edge is incident

to it. Based on Proposition 4.1(v), it is a simple very good graph on five vertices and again we apply
Lemma 4.2 to H and H. Thereby we infer that after some rounds Builder obtains a very good host
graph with ess(H) + ess(H) = k essential vertices.

    If Painter colours cx and xy red, then Builder forces the edge ay blue and we obtain an extended
(2, 0)-path cbayx.

                                                 ab cxy

    The coloured graph H induced by the five edges selected in the game is a simple very good graph
with five essential vertices, we apply Lemma 4.2 again, and conclude that after some rounds Builder
obtains a very good graph with ess(H) + ess(H) = k essential vertices.

    Suppose Painter colours cx red and xy blue. So we obtain a bbrb-path:

                                                               11
                                                 ab cxy

Then Builder selects ay. If Painter colours it blue, we receive a blue (1, 1)-path on five vertices, with
1-ends x, c. If Painter colours ay red, Builder forces cy blue and we receive the following coloured
graph.

                                                 ab cxy

It is a blue (1, 1)-path with 1-ends x, a.
    Thus, regardless of whether Painter coloured ay red or blue, Builder obtains a graph H which

is a sum of a blue (1, 1)-path on five vertices and at most two red edges incident to the path. As
before, we apply Proposition 4.1(vi), then Lemma 4.2 to H and H, and conclude the assertion.

    Suppose Painter colours cx blue and xy red. Then Builder selects ay. If Painter colours it blue,
we receive a blue (1, 1)-path on five vertices, with 1-ends x, y. If Painter colours ay red, we receive
an extended (2, 0)-path abcxy. The analysis is analogous as before and we conclude the assertion in
a similar way.
Case 3. ab and bc have different colours, i.e. ab is, say, blue and bc is red.

    Suppose first that L = . Builder selects cx for any free x  V (K ).
                                                                                                                                     N

    If Painter colours it red, then Builder forces an edge xy blue for any free y  V (K ), then he
                                                                                                                                                                           N

forces ax blue. The following coloured graph is obtained:
                                                 ab cxy

Such a graph with an extended (2, 0)-path has been already analysed in Case 1.
    Suppose Painter colours cx blue. Then Builder selects by for any free y  V (K ). If Painter

                                                                                                                                                                      N

colours it blue, the four edges selected in the game so far form a limb L, vertex-disjoint with H.
Hence, since H is very good and L = , also H  L is a very good graph. It has ess(H) + 5 = k
essential vertices and the assertion follows. Assume that Painter colours by red. We receive the
following coloured graph at K :

                                                          N

                                                     ab cx

                                                            y

Then Builder forces edges ac and xy blue and we obtain a graph H which is a sum of a blue (2, 1)-
path (which is also a (1, 1)-path) yxcab and a red path of length 2, as we illustrate in the following
picture.

                                                     ab cx

                                                            y

                                                               12
Such a graph is simple very good so based on Lemma 4.2 applied to H and H, after some rounds
Builder obtains a very good graph with ess(H) + ess(H) = k essential vertices.

    Now suppose that L = . Then Builder selects an edge xy for any free x, y  V (K ).
                                                                                                                                                                      N

    If Painter colours xy blue, then Builder selects cx. No matter how Painter colours it, the four
edges selected in the game form either a brrb-path considered in Case 1 or a bbrb-path, which we
considered in Case 2. Therefore further we assume that Painter colours xy red. Then Builder selects
ax.

    If Painter colours ax blue, then Builder forces by and cy blue. The following graph is obtained:
                                                 xab cy

Such a stage of the game has been already analysed in Case 2.
    Further we assume that ax is red. Consider two components of the coloured graph induced by

all coloured edges present on the board KN: the rrbr-path created in the four rounds of the game
and the limb L, with its vertices denoted as in the following picture.

                                                  yxab c

                                                 w1 u1 u2 w3

                                                        w2

In the next five rounds Builder forces blue edges: yw1, yw3, cu2, cx, aw2. After we obtain the
following coloured graph H:

                                                  yxab c

                                                 w1 u1 u2 w3

                                                        w2

Thus H is a sum of a blue (1, 1)-path on 10 vertices and four red edges. We know by Proposition
4.1(vi) that such a graph is simple very good, and that, by Proposition 4.1(iii), the graph H \ L is
very good. The very good graphs H and H \ L are vertex-disjoint and they satisfy the assumption
of Lemma 4.2. Similarly to the previous analysis, based on Lemma 4.2 Builder obtains a very good
graph with ess(H \ L) + ess(H) = k essential vertices.

    An immediate consequence of Lemma 4.3 and the inductive argument is the following corollary.
Corollary 4.4. Suppose that n  10. Then Builder has a strategy in RR(P4, Pn) such that after a
finite number of rounds the host graph is a very good graph with 5n/5 essential vertices.

    So far Lemma 4.2 was applied to very good graphs only. In the next section we will use it also in
case of a simple good graph H which is not very good, i.e. with the number of vertices not divisible
by 5.

                                                               13
5 Proof of Theorem 1.4

Let n = m + r with 5 | m, m  10 and 0  r  4. It is enough to show a strategy for Builder
in RR(P4, Pn) such that the game ends after at most 7n/5 - 1 rounds. We divide the game
RR(P4, Pn) into three stages. Roughly speaking, in the first stage Builder creates a big very good
graph and in the second stage he increases it to a good graph with n essential vertices. In the last
stage he connects parts of the good graph into a blue path Pn.
Stage 1.

    In the first stage, based on Corollary 4.4, Builder uses a strategy which guarantees that after some
round the host graph is a very good graph H with m essential vertices. Then the first stage ends.
Assume that the very good graph H has essential subgraphs (G0, G1, G2, L). The game proceeds to
the next stage, equivalent to the game RRH(P4, Pn).
Stage 2.

    Let KN  KN be a complete graph, vertex-disjoint from H. Builder begins by selecting r - 1
edges of a path on r vertices in K (if r  1, he does nothing). After Painter colours them, we obtain

                                                               N

a coloured path P on r vertices. For r = 0 we put P = , for r = 1 we have a trivial path P . We
consider a few cases in order to define a new coloured component H. The only case not listed below
is when r = 2 and P is a red edge. We call it the exceptional case, assume that the second stage
ended here and consider this case later.

Case 1. 0  r  4 and P is blue.
    Then we put H = P . There is no red edges incident to the path H so it is a simple good graph

with ess(H) = r.

Case 2. r = 3, P = abc and it is an rr-path.
    Then Builder forces blue edges ax, xc with any free x  V (K ). Hence we obtain a coloured

                                                                                                                                  N

graph H that is the sum of a blue (1, 1)-path G1 = axc and two red edges. H is a simple good
graph since |Red(H)| = 2 = 2v(G1)/5. Clearly ess(H) = r.
Case 3. r = 3, P = abc and it is a br-path.

    Then Builder selects ac. No matter how Painter colours it, the coloured graph induced by the
three edges form a simple good graph H with 3 essential vertices. Indeed, if ac is blue, then H
contains a blue (1, 1)-path cab; if ac is red, then H contains an extended (2, 0)-path abc.

Case 4. r = 4, P = abcd and at least one edge of P is red.

    Then Builder selects ad. Thus the four selected edges form a cycle. If three edges of the cycle
are blue, we get a blue (1, 1)-path on 4 vertices. If two edges of the cycle are blue and two red
edges are adjacent, we get an extended (2, 0)-path on 4 vertices. If the two red edges are disjoint,
say ab and cd, then Builder forces a blue edge ac and we obtain a blue (1, 1)-path on 4 vertices.
Obviously, the cycle cannot have exactly one edge blue, since Painter never creates a red P4. Thus
in all cases for r = 4 the four coloured edges form a simple good graph and we denote it by H. We
have ess(H) = 4.

    It follows from the argument above that for every r  4, in every case apart from the exceptional
case (r = 2 and P red) the new component H is a simple good graph with r essential vertices.
Furthermore, H and H satisfy the assumption of Lemma 4.2. Thus within some further rounds
Builder creates a good graph G with ess(G) = m+r = n and with essential subgraphs (G0 , G1, G2 , L).

    The second stage ends and the game proceeds to the third stage, equivalent to the game RRG(P4, Pn).
Stage 3.

                                                               14
    Let us recall that we still exclude the exceptional case from the analysis. Builder begins by
transforming the limb L (if L = ) into a blue (1, 0)-path. Suppose the vertices of L are denoted as
in the following picture.

                                                    x1 x2 x3 x4

                                                           x5

Builder selects x4x5. If Painter colours it blue, we obtain a blue (1, 0)-path P  = x3x4x5x2x1. If
Painter colours x4x5 red, Builder forces the edge x5x3 blue and we get a blue (1, 0)-path P  =
x1x2x5x3x4, as shown in the following picture.

                                                    x1 x2 x3 x4

                                        x5

    Without loss of generality we can assume that x4 is an 1-end of the path P . Clearly |Red(P )| 

2 = 2v(P )/5. If G1 = , we put F1 = P ; otherwise for an 1-end u1 of G1, Builder forces the edge
x4u1 blue. Then we define F1 = P   G1  {x4u1}.

    For L =  we define F1 = G1 . Thus in both cases (L empty or not) F1 is a (1, 0)-path or F1 = .
Observe also that in both cases at this moment of the game we have v(F1) = v(L) + v(G1) and

|Red(L)| = 2v(L)/5.

If F1 =  or G2 = , we define D = F1  G2. Suppose now that F1, G2 = . Let f1 be an 1-end of

the path F1, f1 be its other 1-end, and let u2 , w2, u2 denote the blue end, the transition vertex and

the red end of G2 , respectively. Breaker forces the edges f1u2 and w2f1 blue. After there is a blue

(1, 0)-path D on v(F1) + v(G2) vertices on the board, with an 1-end u2 and the other end u2.

In both cases (F1, G2 =  or not) we have v(D) = v(F1) + v(G2 ) = v(L) + v(G1 ) + v(G2 ) and every

red edge incident to a vertex of D is either a red edge of G incident to G1 or G2, or it is incident to

L. Thus                                                                      2
                                                                              v(L).
         |Red(D)|  =  |RedG(G2    G1)|  +  |Red(L)|  =  |RedG(G2    G1)|  +                   (1)
                                                                             5

Furthermore, every blue edge of L  G1  G2 is a blue edge of D.
    It remains to connect D and G0 into a blue path D. Let x be an 1-end of D and x be the other

end of it. If G0 = , then we define D = D. Clearly then |Red(D)| = |Red(D)| and

         |Red(D)|       |RedG(G2    G1 )|   +  2        2  v(G1     G2)      2
                                                v(L)    5                 + v(L)

                                               5                             5

                        2                       2          2
                      = (ess(G) - v(L)) + v(L) = ess(G) .
                        5                       5          5

    Suppose that G0 = . Let u0 and u0 be the ends of the path G0. Builder selects the edge xu0. If
Painter colours it blue, then we define D = D  G0  {xu0}. Suppose Painter colours xu0 red. Then
u0 becomes a 2-end of G0 . We also know that there is a red edge, say e, incident to x but different
from xu0. If e is not incident to x, then Builder forces the edge u0x blue. If e is incident to x, then

x is a 2-end of D now and Builder can force blue either the edge xu0 if u0 = u0, or an edge xy with

                                            15
a free y if u0 = u0. We denote by D the resulting blue path on v(D) + v(G0 ) vertices. Since at most
one red edge incident to its vertex was selected while connecting D and G0 , in view of (1) we have

|Red(D)|    |RedG(G2     G1)|   +   2      +  |RedG(G0 )|      +  1
                                     v(L)

                                    5

            2  v(G1    G2 )        2          2  v(G0)  =      2
            5                   + v(L) +      5                 ess(G) .

                                   5                           5

In the last equality we used the property of a good graph that one of the numbers v(G1  G2), v(G0 )
is divisible by 5 and, clearly, 2v(L)/5 is integer.

    In all cases we obtain a blue path D on v(L) + v(G0 ) + v(G1 ) + v(G2 ) + v(L) = ess(G) = n
vertices, such that |Red(D)|  2ess(G)/5 = 2n/5. The third stage ends.

    Observe that the set Red(D) for the path D obtained at the end of Stage 3 is also the set of all red

edges selected in the game. Indeed, G was good at the end of Stage 2 so every red edge was incident
to G0  G1  G2  L then. Furthermore every red edge selected during the third stage was incident
to L or to the path D with V (D) = V (L)  V (G1)  V (G2). It follows from the construction of D
that D  D. It may have happened that G0  D, but only if G0 had one vertex. However, in such
a case at the end of Stage 2 the number of red edges incident to G0 was at most 2v(G0)/5 - 1 = 0.
Thus the number of red edges selected in the game is |Red(D)|  2n/5.

    Notice also that at the end of the third stage there are no blue edges on the board other than
the edges of D so the number of blue edges selected in the game RR(P4, Pn) is n - 1.

    Summarising, the number of all coloured edges (and thus the number of rounds of the game

RR(P4, Pn)) is not greater than

                             2      7
               n - 1 + n = n - 1.
                             5      5

This ends the proof in all cases apart from the exceptional case.
    We proceed to the exceptional case. Let us recall that then we assume that r = 2, after the

second stage the position on the board consists of a red path P = ab and the coloured graph H
(vertex-disjoint from P ) which is very good, with essential subgraphs (G0, G1, G2, L) and m essential
vertices. The game proceeds to the third stage.

Stage 3 in the exceptional case.

    We consider three subcases, depending on the essential subgraphs of H.

Subcase 1. G0 = .
    Let u0, u0 be the ends of G0. Builder selects edges u0a and u0 b. Since Painter avoids a red P4,

he has to colour blue at least one of these edges. If both are blue, we obtain a blue (1, 1) path B
with 1-ends a, b, on v(G0) + v(P ) vertices. If exactly one of the edges is blue, we get an extended
(2, 0)-path on v(G0) + 2 vertices. In both cases, since 5 | v(G0), the new coloured component
H = B  P  {u0a, u0b} on the board satisfies

                         2                       2                2          2
|Red(B)|  |RedH(G0)| + |Red(P )|  5 v(G0) - 1 + 2 = 5 v(G0) +      v(P )  =   v(B) .
                                                                  5          5

Thus H is a simple good graph. Since H \ G0 is very good, the assumption of Lemma 4.2 is satisfied
by H \ G0 and H. Based on this lemma, after a few further rounds the host graph is a good graph

G with
                          ess(G) = ess(H \ G0) + ess(H) = ess(H) + 2 = m + r = n.

                                16
Further analysis is the same as in Stage 3 for non-exceptional cases above. It leads to the conclusion
that a blue path of length n - 1 is created and the number of edges on the board at this moment is
not greater than 7n/5 - 1.

Subcase 2. G0 =  and G1 = .

    Let u1, u1 be the 1-ends of G1. Builder forces blue edges u1a and u1 b. As a result we obtain a
blue (1, 1)-path G1 with 1-ends a and b, on v(G1) + v(P ) vertices. Let G = H  P  {u1a, u1 b}. Since
5 | v(G1  G2), the subgraph G1  G2 of the coloured graph G satisfies

|RedG(G1  G2)|                                                      2                         2                   2
                          |RedH(G1  G2)| + |RedG(P )|  5 v(G1  G2) + 1 = 5 v(G1  G2) +                             v(P )

                                                                                                                  5

                      =      2                             =     2  (v(G1    G2))    .
                             5 (v(G1  G2) + v(P ))               5

It is not hard to verify that G satisfies all conditions of a good graph and its essential subgraphs are
(, G1 , G2, L). Again we use the same argument as in Stage 3 for non-exceptional cases and conclude
the assertion.

Subcase 3. G0 =  and G1 = .

Then G2 =  since G has at least 10 essential vertices. Let w2 be the transition vertex of G2 and

u2 be its red end. Let us recall that the edge w2u2 is red. Builder forces blue edges: w2a, au2 and

u2b. Thereby we obtain a blue (1, 0)-path F on v(G2) + v(P ) vertices and its 1-end b.

Apart from the extended (2, 0)-path G2 , H may contain also a limb. Then, as in Stage 3 for

non-exceptional case, Builder transforms the limb into a blue (1, 0)-path P  with an 1-end x4 and

|Red(P )|  2 =  2     v(L).  Afterwards, Builder forces the edge x4b blue and a longer blue path B                        is
                5

obtained.

Let B = F  P   {x4a} if L = , while otherwise we put B = F and define P  = . Note that

|Red(P )|    2  v(L)  in  both  cases  (L  =    or  not).  Notice   also   that  in  both  cases    V  (B)  =  V  (G2 LP )
             5

so v(B) = ess(H) + 2 = n + r = n. So there is a blue path on n vertices on the board and Builder

wins.

Furthermore, since 5 | v(G2  G1) = v(G2), we have

             |Red(B)|           |RedH (G2)|     + |Red(P )|      +  |Red(P )|        2        +  1  +  2
                                                                                     5 v(G2)            v(L)

                                                                                                       5

                                2               2             2            2
                             =  5 v(G2) +        v(P )     + v(L) =         v(B) .
                                                5             5            5

It follows from the strategy of Builder that Red(B) consists of all red edges of the game RR(P4, Pn)
and the blue path B contains all blue edges present on the board. Thus the number of rounds in the

game is

                                                           7                     7
                                e(B) + |Red(B)|  v(B) - 1 = n - 1.
                                                           5                     5

This ends the proof in the exceptional case and the proof of Theorem 1.4.

References

 [1] J. Balogh, F. Clemen, E. Heath, M. Lavrov, A strengthening of the Erdos-Szekeres Theorem,
      European Journal of Combinatorics 101 (2022), 103456.

                                                           17
[2] J. Beck, On size Ramsey number of paths, trees and cycles I, Journal of Graph Theory 7 (1983),
    115�130.

[3] V. Blazej, P. Dvor�ak, T. Valla, On induced online Ramsey number of paths, cycles, and trees,
    The 14th International Computer Science Symposium in Russia, Lecture Notes in Computer
    Science. vol. 11532, Springer, 2019, 60�69.

[4] J. Cyman, T. Dzido, J. Lapinskas, A. Lo, On-line Ramsey numbers for paths and cycles, Electron.
    J. Comb. 22 (2015) no. P1.15.

[5] J. Grytczuk, H. Kierstead, P. Pralat, On-line Ramsey numbers for paths and stars, Discrete
    Mathematics and Theoretical Computer Science 10 (2008), 63�74.

[6] X. P�erez-Gim�enez, P. Pralat, D. B. West, On-line size Ramsey number for monotone k-uniform
    ordered paths with uniform looseness, European Journal of Combinatorics 92 (2021), 103242.

[7] P. Pralat, A note on off-diagonal small on-line Ramsey numbers for paths, Ars Combinatoria
    107 (2012), 295�306.

[8] Y. Zhang, Y. Zhang Proof of a conjecture on online Ramsey numbers of paths, preprint,
    http://arxiv.org/abs/2302.13640.

                                                             18
