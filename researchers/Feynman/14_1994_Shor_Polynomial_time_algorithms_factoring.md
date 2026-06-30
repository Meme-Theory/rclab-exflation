# Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer

**Author(s):** Peter W. Shor (AT&T Research)
**Year:** 1994 (preliminary version in Proc. 35th Annual Symp. on Foundations of Computer Science, Santa Fe, NM, Nov. 1994, IEEE Computer Society Press, pp. 124–134); the full paper (arXiv v2) is dated 25 Jan 1996.
**Journal:** arXiv preprint quant-ph/9508027 (also published in SIAM J. Computing 26, 1484 (1997))
**arXiv/DOI:** arXiv:quant-ph/9508027
**Relevance:** MEDIUM for phonon-exflation

---

## Abstract
"A digital computer is generally believed to be an efficient universal computing device; that is, it is believed able to simulate any physical computing device with an increase in computation time by at most a polynomial factor. This may not be true when quantum mechanics is taken into consideration. This paper considers factoring integers and finding discrete logarithms, two problems which are generally thought to be hard on a classical computer and which have been used as the basis of several proposed cryptosystems. Efficient randomized algorithms are given for these two problems on a hypothetical quantum computer. These algorithms take a number of steps polynomial in the input size, e.g., the number of digits of the integer to be factored."

Keywords: algorithmic number theory, prime factorization, discrete logarithms, Church's thesis, quantum computers, foundations of quantum mechanics, spin systems, Fourier transforms. AMS classes 81P10, 11Y05, 68Q10, 03D10.

## Key Arguments and Derivations

**§1 Introduction (pp. 2–5).** Introduces the Quantitative (Strong) Church Thesis: any physical computing device can be simulated by a Turing machine with polynomial overhead. Quantum mechanics adds a third resource beyond time and space: **precision** (bits of precision must grow logarithmically in input size). Reviews the lineage Benioff [1980,1982] (quantum-mechanical reversible Turing machine, classical power) → Feynman [1982,1986] (quantum simulation is classically hard) → Deutsch [1985,1989] (quantum Turing machines & circuits) → Bernstein–Vazirani [1993] and Simon [1994] (oracle separations). Shor's result gives polynomial-time quantum algorithms for factoring and discrete logarithm – the first non-oracle superpolynomial-looking separation.

**§2 Quantum computation model (pp. 5–8).** Quantum gate arrays. State of n qubits is a unit vector in C^{2^n}, Σ a_i |S_i> with Σ |a_i|² = 1. Measurement in the canonical basis returns |S_i> with probability |a_i|². Unitary transformations are the only allowed state evolution. Universal set: all one-qubit gates plus the two-qubit CNOT. Example gate (Eq. 2.2–2.3): |00>→|00>, |01>→|01>, |10>→(|10>+|11>)/√2, |11>→(|10>−|11>)/√2. Gate-array uniformity requires (i) classical polynomial-time constructibility of the gate sequence and (ii) computability of the first log n bits of each gate matrix entry in polynomial time.

**§3 Reversible logic and modular exponentiation (pp. 8–13).** Reversibility is a consequence of unitarity – classical gate garbage must be uncomputed. Universal reversible gates: Toffoli and Fredkin (Table 3.1). Bennett's reversible-computation trick (Table 3.2) computes F(x) and then erases both the intermediate RECORD register and the first OUTPUT register, leaving only the input x and F(x). To erase x entirely (replace by F(x)) one additionally needs a polynomial algorithm for F^{-1}. Modular exponentiation x^a mod n: classical longhand multiplication gives O(l^3) time and O(l) space for l-bit n; Schönhage–Strassen gives O(l² log l log log l) time. The pseudocode (p. 11) repeatedly squares x, and for each set bit a_i of the exponent multiplies `power` by x^{2^i} mod n. Multiplication is made reversible via a two-step "forward by c then uncompute by c^{-1}" construction when gcd(c,n)=1; a quantum-Zeno "watchdog" measurement of the scratch b = 0 is suggested to stabilize the computation.

**§4 Quantum Fourier transforms (pp. 13–15).** Define A_q for q = 2^l:

  A_q |a> = (1/√q) Σ_{c=0}^{q−1} exp(2πiac/q) |c>     (Eq. 4.1)

Built from single-qubit Hadamards R_j (Eq. 4.2) and controlled-phase gates S_{j,k} with phase e^{iπ/2^{k−j}} (Eq. 4.3). The Coppersmith/Deutsch sequence (Eq. 4.4) applies R_{l−1}, then S_{l−2,l−1}, R_{l−2}, S_{l−3,l−1}, S_{l−3,l−2}, R_{l−3}, …, R_0 — a total of l(l−1)/2 + l = O(l²) gates. The proof that this implements A_q traces the accumulated phase: each pair (a_j, b_k) contributes π/2^{k−j} when both are 1; summed, this is 2π a c / q (after bit-reversal). Coppersmith's approximate FFT truncates small phases to reduce gate count without harming the factoring accuracy.

**§5 Prime factorization (pp. 15–19).** Reduction (Miller 1976) of factoring to order-finding: choose random x mod n, find r = ord(x) mod n, return gcd(x^{r/2}−1, n). Fails only when r is odd or x^{r/2} ≡ −1 mod n; probability of success is ≥ 1 − 1/2^{k−1} where k is the number of distinct odd prime factors.

**Quantum order-finding algorithm:**

1. Pick q a power of 2 with n² ≤ q < 2n².
2. Uniform superposition in first register: (1/√q) Σ_{a=0}^{q−1} |a>|0>     (Eq. 5.1)
3. Reversibly compute x^a mod n into the second register: (1/√q) Σ_a |a> |x^a mod n>     (Eq. 5.2)
4. Apply A_q to the first register: (1/q) Σ_{a,c} exp(2πiac/q) |c>|x^a mod n>     (Eq. 5.4)
5. Measure. The probability of seeing (c, x^k mod n) with 0 ≤ k < r is

   | (1/q) Σ_{a: x^a ≡ x^k} exp(2πiac/q) |²     (Eq. 5.5)

   Summing over a ≡ k (mod r), writing a = br+k, and replacing rc by its signed residue {rc}_q ∈ (−q/2, q/2]:

   | (1/q) Σ_{b=0}^{⌊(q−k−1)/r⌋} exp(2πi b {rc}_q / q) |²     (Eq. 5.7)

   The sum is large when |{rc}_q| ≤ r/2, i.e. when |c/q − d/r| ≤ 1/(2q) for some d (Eq. 5.13). Because q > n², at most one such fraction d/r with r<n exists, and it is recovered by continued-fraction expansion of c/q. Each such state has probability ≥ 4/(π² r²) ≥ 1/(3r²); there are φ(r) good values of d relatively prime to r and r values of k, giving total success probability ≥ φ(r)/(3r) ≥ δ/log log r (Hardy–Wright Theorem 328). Therefore O(log log r) repetitions suffice. The worked example with r = 10, q = 256 is shown in Fig. 5.1.

**§6 Discrete logarithms (pp. 19–20).** Given prime p, generator g, target x = g^r mod p. Take q a power of 2 with p < q < 2p. Prepare superposition over (a, b) mod p−1, compute g^a x^{−b} mod p in a third register (Eq. 6.1). Apply A_q to both first two registers (Eq. 6.2). Measure. The amplitude on |c, d, g^k mod p> is, using a ≡ br + k (mod p−1),

  (1/((p−1) q)) Σ_{b=0}^{p−2} exp( (2πi/q) [brc + kc + bd − c(p−1) ⌊(br+k)/(p−1)⌋] )     (Eq. 6.6)

As in order-finding, this amplitude concentrates near (c, d) such that the phase is stationary; joint rational approximation of (c/q, d/q) yields r. Two modular exponentiations plus two quantum Fourier transforms.

## Key Results
1. Factoring an l-bit integer n can be done on a quantum computer in O(l² log l log log l) quantum steps plus poly(l) classical post-processing, with bounded error probability — exponentially faster than the best known classical algorithm (number field sieve, sub-exponential).
2. Discrete logarithm mod prime p has the same asymptotic quantum complexity.
3. Reduction of factoring to order-finding + quantum Fourier transform A_q + quantum modular exponentiation + continued-fraction post-processing is the complete pipeline.
4. The quantum Fourier transform on q = 2^l qubits is realized by O(l²) local gates (Hadamards + controlled-phase).
5. Gate-array model is equivalent to quantum Turing machine (Yao 1993), defining the complexity class BQP.
6. Any general classical polynomial-slowdown simulator of quantum mechanics would give a polynomial-time classical factoring algorithm — so either quantum mechanics is classically hard to simulate, or factoring is classically easy.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Amplitude normalization | Σ_i |a_i|² = 1 | Eq. 2.1 |
| Hadamard R_j | |0>→(|0>+|1>)/√2; |1>→(|0>−|1>)/√2 | Eq. 4.2 |
| Controlled-phase S_{j,k} | diag(1, 1, 1, e^{iπ/2^{k−j}}) | Eq. 4.3 |
| QFT A_q | |a> → (1/√q) Σ_c exp(2πiac/q) |c> | Eq. 4.1 |
| Order-finding state | (1/q) Σ_{a,c} exp(2πiac/q) |c>|x^a mod n> | Eq. 5.4 |
| Peak probability | \|(1/q) Σ_b exp(2πi b{rc}_q/q)\|² | Eq. 5.7 |
| Continued-fraction condition | \|c/q − d/r\| ≤ 1/(2q) with q > n² | Eq. 5.13 |
| Single-peak probability | ≥ 4/(π²r²) ≥ 1/(3r²) | p. 18 |
| Factoring reduction | return gcd(x^{r/2}−1, n) | §5 |
| Success probability | ≥ 1 − 1/2^{k−1} (k distinct odd prime factors) | §5 |
| DL register state | (1/(p−1)) Σ_{a,b} \|a,b, g^a x^{−b} mod p> | Eq. 6.1 |

## Relevance to Phonon-Exflation
Shor's algorithm is the archetype of "phase-estimation on a unitary": the order r of x mod n is extracted from the periodicity of the unitary U_x : |a>|y> ↦ |a>|xy mod n>. The same phase-estimation primitive applies to the Dirac operator D_K on Jensen-deformed SU(3): eigenvalues λ_k of D_K would be extracted (in principle) by phase estimation on e^{iD_K t}, and the spectral moments a_0, a_2, a_4 that generate the Standard-Model Lagrangian are polynomial functions of these eigenvalues. So Shor's paper supplies the algorithmic primitive by which a quantum computer (or by extension, the substrate itself as a "universal quantum simulator" in the Feynman 1982 sense) can in principle read off its own spectral data. Framework-relevant implications: (i) the O(l²) QFT gate count tells us that the substrate's spectral decomposition is classically intractable for large-dimensional D_K but quantum-tractable; (ii) the continued-fraction post-processing (Eq. 5.13) is structurally the same device that extracts rational ratios of spectral gaps — relevant to the alpha_s = n_s² − 1 identity and similar spectral-moment relations; (iii) the precision resource scaling (log n bits) is the quantum analog of the regularization-scale dependence in the spectral action, Tr f(D/Λ).
