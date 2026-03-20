# Algorithms for Quantum Computation: Discrete Logarithms and Factoring

**Author:** Peter W. Shor
**Year:** 1994
**Journal:** Proceedings of the 35th Annual Symposium on Foundations of Computer Science (FOCS), 124--134; expanded journal version in *SIAM Journal on Computing*, 26(5), 1484--1509 (1997)

---

## Abstract

Shor demonstrates that a quantum computer can factor integers and compute discrete logarithms in polynomial time, providing the first concrete evidence that quantum computers are exponentially more powerful than classical computers for a problem of major practical significance. The best known classical factoring algorithms (the general number field sieve) run in sub-exponential time $\exp(O(n^{1/3}(\log n)^{2/3}))$ for an $n$-bit number, while Shor's quantum algorithm runs in time $O(n^2 \log n \log\log n)$ using $O(n)$ qubits. The algorithm reduces factoring to the problem of finding the period of a modular exponential function, then solves the period-finding problem using the quantum Fourier transform (QFT) -- a unitary transformation that can be implemented efficiently on a quantum computer. This paper is the direct realization of Feynman's 1982 vision that quantum computers could outperform classical ones, and it transformed quantum computing from a theoretical curiosity into a global research priority due to the implications for cryptography and computational complexity.

---

## Historical Context

### The RSA Cryptosystem

The practical significance of integer factoring arises from the RSA cryptosystem (Rivest, Shamir, Adleman, 1977), which underpins the security of nearly all electronic commerce, banking, and secure communications. RSA security relies on the assumption that factoring the product of two large primes is computationally intractable: while multiplying two 2048-bit primes takes microseconds, no known classical algorithm can factor their product in a reasonable time.

As of the mid-1990s, the best classical factoring algorithms were:
- **Trial division:** $O(\sqrt{N})$ -- exponential in the number of digits
- **Pollard's rho:** $O(N^{1/4})$ -- still exponential
- **Quadratic sieve:** $\exp(O(n^{1/2}(\log n)^{1/2}))$ -- sub-exponential
- **Number field sieve (NFS):** $\exp(O(n^{1/3}(\log n)^{2/3}))$ -- the best known

All are super-polynomial. The question of whether factoring is fundamentally hard (in the class NP-hard, or even NP-intermediate) is a major open problem in computational complexity.

### Prior Quantum Computing Results

Before Shor's algorithm:
- **Feynman** (1982): argued quantum computers are needed to simulate quantum systems
- **Deutsch** (1985): defined the quantum Turing machine, showed a quantum speedup for a simple problem
- **Deutsch-Jozsa** (1992): exponential quantum speedup for determining if a function is constant or balanced (a contrived problem)
- **Bernstein-Vazirani** (1993): quantum algorithm for finding a hidden linear function
- **Simon** (1994): exponential quantum speedup for finding the period of a function over $\{0,1\}^n$ (the direct precursor to Shor)

Simon's algorithm was the breakthrough that inspired Shor. Simon showed that a quantum computer could find the period of a function $f: \{0,1\}^n \to \{0,1\}^n$ with the property $f(x) = f(y)$ iff $x \oplus y \in \{0, s\}$ (where $s$ is the hidden period) using $O(n)$ quantum queries, compared to $\Omega(2^{n/2})$ classical queries. Shor recognized that a similar approach could solve the period-finding problem for modular arithmetic, which reduces to factoring.

---

## Key Arguments and Derivations

### 1. Reduction of Factoring to Period Finding

The first step is to reduce the factoring problem to a number-theoretic problem that a quantum computer can solve. Given an integer $N$ to factor:

**Step 1:** Choose a random integer $a$ with $1 < a < N$ and $\gcd(a, N) = 1$. (If $\gcd(a,N) > 1$, we have already found a factor.)

**Step 2:** Find the period $r$ of the function $f(x) = a^x \bmod N$. That is, find the smallest positive integer $r$ such that $a^r \equiv 1 \pmod{N}$.

**Step 3:** If $r$ is even and $a^{r/2} \not\equiv -1 \pmod{N}$, then:

$$a^r - 1 = (a^{r/2} - 1)(a^{r/2} + 1) \equiv 0 \pmod{N}$$

so $N$ divides $(a^{r/2} - 1)(a^{r/2} + 1)$ but $N$ does not divide either factor individually (by assumption). Therefore, $\gcd(a^{r/2} - 1, N)$ is a non-trivial factor of $N$.

The probability that a random $a$ gives a useful $r$ (even, with $a^{r/2} \not\equiv -1$) is at least $1/2$ for any composite $N$ that is not a prime power. So the algorithm succeeds with high probability after a few random choices of $a$.

The classical difficulty is Step 2: finding the period $r$. Classically, this requires evaluating $a^x \bmod N$ for many values of $x$ and detecting the period, which takes time exponential in the number of digits of $N$. Shor shows that a quantum computer can find $r$ in polynomial time.

### 2. The Quantum Fourier Transform

The quantum Fourier transform (QFT) over $\mathbb{Z}_M$ is the unitary transformation:

$$\text{QFT}: |j\rangle \to \frac{1}{\sqrt{M}}\sum_{k=0}^{M-1} e^{2\pi ijk/M}|k\rangle$$

For $M = 2^n$, the QFT can be decomposed into a circuit of $O(n^2)$ elementary gates (Hadamard gates and controlled phase rotations):

$$\text{QFT}|j\rangle = \frac{1}{\sqrt{2^n}}\bigotimes_{\ell=1}^{n}\left(|0\rangle + e^{2\pi i j/2^\ell}|1\rangle\right)$$

The explicit circuit consists of:
- $n$ Hadamard gates
- $n(n-1)/2$ controlled-$R_k$ gates, where $R_k = \text{diag}(1, e^{2\pi i/2^k})$
- Bit-reversal permutation at the end

The total gate count is $O(n^2)$, which is exponentially more efficient than the classical Fast Fourier Transform (which requires $O(2^n \cdot n)$ operations to transform a vector of length $2^n$). This exponential advantage is possible because the QFT acts on amplitudes (which are already encoded in $n$ qubits) rather than on explicitly stored vector components.

### 3. The Period-Finding Algorithm

The quantum period-finding algorithm proceeds as follows:

**Setup:** Use two registers: the first with $n = \lceil 2\log_2 N \rceil$ qubits (initialized to $|0\rangle^{\otimes n}$), the second with $\lceil \log_2 N \rceil$ qubits (also initialized to $|0\rangle^{\otimes \lceil\log_2 N\rceil}$).

**Step 1: Create superposition.** Apply Hadamard gates to the first register:

$$|0\rangle^{\otimes n}|0\rangle \to \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n - 1}|x\rangle|0\rangle$$

**Step 2: Compute $f(x) = a^x \bmod N$.** Apply the modular exponentiation oracle:

$$\frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n - 1}|x\rangle|0\rangle \to \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n - 1}|x\rangle|a^x \bmod N\rangle$$

This is the most expensive step, requiring $O(n^3)$ elementary gates using repeated squaring and modular multiplication.

**Step 3: Apply QFT to the first register.** This transforms the amplitudes from the "time domain" (values of $x$) to the "frequency domain" (multiples of $2^n/r$):

$$\to \frac{1}{2^n}\sum_{x=0}^{2^n - 1}\sum_{y=0}^{2^n - 1} e^{2\pi ixy/2^n}|y\rangle|a^x \bmod N\rangle$$

**Step 4: Measure the first register.** The measurement yields a value $y$ that, with high probability, is close to a multiple of $2^n/r$:

$$y \approx j \cdot \frac{2^n}{r} \quad \text{for some integer } j \in \{0, 1, \ldots, r-1\}$$

**Step 5: Classical post-processing.** From $y/2^n \approx j/r$, use the continued fraction algorithm to extract $r$ (or a factor of $r$). Repeat $O(\log\log N)$ times if necessary to find $r$ with high probability.

### 4. Analysis of the Measurement Outcome

The probability of measuring $y$ in the first register, given that the second register contains a specific value $a^{x_0} \bmod N$, is:

$$P(y) = \frac{1}{2^{2n}}\left|\sum_{j=0}^{r'-1} e^{2\pi i(x_0 + jr)y/2^n}\right|^2$$

where $r'$ is the number of values $x$ in $\{0, \ldots, 2^n - 1\}$ that give the same $a^x \bmod N$. The geometric series evaluates to:

$$P(y) = \frac{1}{2^{2n}} \cdot \frac{\sin^2(\pi r' r y / 2^n)}{\sin^2(\pi r y / 2^n)}$$

This is a sharply peaked function with maxima near $ry/2^n \approx$ integer, i.e., $y \approx j \cdot 2^n/r$. The width of each peak is approximately $1/r'$, so the probability of landing within $1/(2r)$ of a peak is at least $4/\pi^2 \approx 0.4$ per measurement.

### 5. The Continued Fraction Algorithm

Given the measured value $y$, we need to extract $r$ from the relation $y/2^n \approx j/r$. The continued fraction expansion of $y/2^n$ is:

$$\frac{y}{2^n} = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{\ddots}}}$$

The convergents $p_k/q_k$ of this continued fraction are the best rational approximations to $y/2^n$ with denominators $\leq q_k$. Since $|y/2^n - j/r| < 1/(2 \cdot 2^n) < 1/(2r^2)$ (because $2^n > r^2$), the fraction $j/r$ must appear as a convergent. The denominator of this convergent is $r$ (or a divisor of $r$).

The continued fraction algorithm runs in $O(n)$ steps (where $n = \log_2(2^n)$ is the number of bits), making the classical post-processing efficient.

### 6. Discrete Logarithms

Shor also gives a quantum algorithm for discrete logarithms. Given a cyclic group $G = \langle g \rangle$ of order $r$ and an element $h = g^s$, find $s$. The algorithm is similar to the period-finding algorithm:

1. Prepare two registers in uniform superpositions over $\mathbb{Z}_r$.
2. Compute $g^a h^{-b} = g^{a - sb}$ in a third register.
3. Apply QFT to both registers.
4. Measure to extract $s$.

The algorithm runs in $O((\log r)^2 \log\log r)$ quantum gate operations.

### 7. Complexity Analysis

The total resource requirements for Shor's factoring algorithm:

| Resource | Requirement |
|----------|-------------|
| Qubits | $O(n)$ where $n = \log_2 N$ |
| Quantum gates | $O(n^2 \log n \log\log n)$ |
| Classical post-processing | $O(n^3)$ (continued fractions, GCD) |
| Repetitions | $O(1)$ (constant number of trials) |
| Success probability | $\geq 1 - 1/\text{poly}(n)$ per trial |

Compared to the classical number field sieve with complexity $\exp(O(n^{1/3}(\log n)^{2/3}))$, Shor's algorithm is exponentially faster. For a 2048-bit RSA key (the current standard), classical factoring would take longer than the age of the universe, while Shor's algorithm would require approximately $4000$ logical qubits and $10^9$ gates -- feasible for a fault-tolerant quantum computer.

---

## Physical Interpretation

### Quantum Parallelism and Interference

Shor's algorithm exploits two distinctly quantum resources:

1. **Quantum parallelism:** The superposition $\frac{1}{\sqrt{2^n}}\sum_x |x\rangle$ evaluates $f(x) = a^x \bmod N$ for all $2^n$ inputs simultaneously with a single application of the modular exponentiation circuit.

2. **Quantum interference (QFT):** The quantum Fourier transform converts the periodic structure in the amplitudes (period $r$ in the $x$-register) into a concentrated distribution in the frequency domain (peaks at multiples of $2^n/r$). This is constructive interference at the right frequencies and destructive interference elsewhere.

Neither resource alone is sufficient. Quantum parallelism without interference would give a random function value upon measurement (useless). Interference without parallelism would not access the function's periodicity. The combination is the key.

### The Number-Theoretic Structure

The efficiency of Shor's algorithm depends critically on the number-theoretic structure of modular arithmetic. The function $f(x) = a^x \bmod N$ has exact periodicity (not approximate), and the period has a direct relationship to the factors of $N$. This structure is exploited by the QFT, which is perfectly suited to detecting exact periodicities.

For generic functions without special structure, quantum computers offer only a polynomial (Grover) speedup, not an exponential one. Shor's exponential speedup is a consequence of the mathematical structure of the problem, not a universal property of quantum computation.

---

## Impact and Legacy

### Cryptographic Implications

Shor's algorithm made quantum computing a matter of national security. If a large-scale quantum computer is built, all RSA-based cryptography (and elliptic curve cryptography, which also falls to Shor's discrete logarithm algorithm) would be broken. This has motivated:

- **Post-quantum cryptography:** Development of cryptographic systems resistant to quantum attacks (lattice-based, hash-based, code-based, isogeny-based). NIST selected four post-quantum standards in 2022 (CRYSTALS-Kyber, CRYSTALS-Dilithium, FALCON, SPHINCS+).
- **Quantum key distribution (QKD):** Using quantum mechanics to distribute encryption keys with provable security (BB84 protocol, Bennett and Brassard, 1984).
- **Government investment:** The prospect of breaking RSA drove massive government investment in quantum computing research worldwide.

### Quantum Error Correction

The practical realization of Shor's algorithm requires thousands of logical qubits with very low error rates. This motivated the development of:
- Quantum error-correcting codes (Shor 1995, Steane 1996)
- The threshold theorem (Aharonov-Ben-Or, Kitaev, Knill-Laflamme-Zurek)
- Surface codes and topological quantum error correction
- The entire field of fault-tolerant quantum computing

### Quantum Complexity Theory

Shor's algorithm showed that factoring is in BQP (bounded-error quantum polynomial time). Since factoring is believed to be outside P (but not NP-complete), this provides evidence that BQP is strictly larger than P:

$$\text{P} \subseteq \text{BQP} \subseteq \text{PSPACE}$$

with the first inclusion believed to be strict. The relationship between BQP and NP remains unknown.

---

## Connections to Modern Physics

1. **Quantum hardware milestones:** IBM, Google, and others are building quantum computers with the explicit goal of eventually running Shor's algorithm on cryptographically relevant key sizes. Current estimates suggest this will require $\sim 20$ million physical qubits (with surface code error correction) for factoring a 2048-bit number.

2. **Quantum simulation and Shor:** The QFT, developed by Shor for factoring, is also a key subroutine in quantum simulation algorithms (quantum phase estimation), connecting Shor's work directly back to Feynman's original motivation.

3. **Hidden subgroup problem:** Shor's algorithm solves the hidden subgroup problem (HSP) for Abelian groups. Extending this to non-Abelian groups (which would solve graph isomorphism and certain lattice problems) remains an open challenge in quantum algorithms research.

4. **Topological quantum computing:** The quest for fault-tolerant qubits to run Shor's algorithm has motivated the development of topological quantum computing, where qubits are encoded in topologically protected states (non-Abelian anyons) that are inherently robust against local errors.

5. **Quantum advantage experiments:** While Shor's algorithm has not yet been run on cryptographically relevant numbers (the largest number factored by Shor's algorithm on a quantum computer is 21), demonstrations of quantum advantage for related tasks (random circuit sampling, boson sampling) validate the computational model on which Shor's algorithm is based.

6. **Feynman's legacy:** Shor's algorithm is the most dramatic vindication of Feynman's 1982 conjecture. Feynman argued that quantum computers would be more powerful than classical ones; Shor proved it for a problem of enormous practical importance. The line from Feynman (1982) through Deutsch (1985), Simon (1994), and Shor (1994) is one of the clearest examples in science of a foundational insight leading to a transformative discovery.
