# Islands and the de Sitter Entropy Bound

**Author(s):** Daniele Teresi
**Year:** 2022
**Journal:** CERN-TH-2021-213 (preprint: arXiv:2112.03922)
**arXiv:** 2112.03922
**Relevance:** MEDIUM

---

## Abstract

The de Sitter (dS) entropy bound gives the maximal number of e-folds that non-eternal inflation can last before violating the thermodynamical interpretation of dS space. This semiclassical argument is the analogue, for dS space, of the Black-Hole information paradox. We use techniques developed to address the latter, namely the island formula, to calculate semiclassically the fine-grained entropy as seen by a Minkowskian observer after inflation and find that this follows a Page-like curve, never exceeding the thermodynamic dS entropy. This calculation, performed for a CFT in 2D gravity, suggests that the semiclassical expectation should be modified in such a way that the entropy bound might actually not be present.

---

## Key Arguments and Derivations

### The dS Entropy Bound (Sec. II.A)

Starting from a single Hubble patch, $N_e$ e-folds of inflation populates $e^{(D-1)N_e}$ patches in $D$ spacetime dimensions. A Minkowskian observer can associate entropy $S \sim N_e$ to the inflationary modes. When this exceeds the thermodynamic dS entropy $S_{\text{dS}} \sim M_{\text{Pl}}^2/H^2$ (in 4D), a paradox analogous to the BH information paradox arises. This gives the entropy bound $N_e \lesssim S_{\text{dS}}$.

### 2D Gravity Framework (Sec. II.B)

The setup uses dS Jackiw-Teitelboim gravity:
$$S_{\text{JT}} = \frac{1}{16\pi G}\int d^2x \sqrt{-g}\left[\phi_0 R + \phi(R - 2H^2)\right]$$

The global dS solution in global coordinates:
$$ds^2 = \frac{1}{H^2\cos^2\sigma}(-d\sigma^2 + d\varphi^2), \quad \phi = \phi_r \tan\sigma$$

A CFT with large central charge $c \gg 1$ is added. The Bunch-Davies vacuum entanglement entropy for a single interval is:
$$S = \frac{c}{6}\log\frac{2[\cos(\sigma_2 - \sigma_1) - \cos(\varphi_2 - \varphi_1)]}{\cos\sigma_1 \cos\sigma_2 H^2 \epsilon_1 \epsilon_2}$$

### Semiclassical Entropy (Sec. II.C)

The region $R$ is an interval $(-x, x)$ at fixed reheating time $t_0$. Using UV cutoff $\epsilon \sim 1/H$ (modes frozen during inflation), the semiclassical entropy is:
$$S_{\text{semi}} \approx \frac{c}{3}\log(H l_R)$$
where $l_R = 2e^{Ht_0}x$ is the proper length of $R$. This reproduces the entropy bound argument.

### Island Calculation (Sec. III)

Applying the island formula with the two-interval entropy for $c$ free fermions, the total entropy with island is:
$$S(\sigma_I, \varphi_I) = 2\phi_0 + 2\phi_r\tan\sigma_I + S_{\text{semi}}(R \cup I)$$

The dominant island is found in the distant past of the dS evolution. The fine-grained entropy follows a Page-like curve:
$$S(R) \approx \min\left\{\frac{c}{3}\log\frac{2e^{Ht_0}x}{\epsilon},\; 2\phi_0 - \phi_r Hx + \frac{c}{3}\left(\log\frac{2e^{Ht_0}c}{9\phi_r H^2 \epsilon_{\text{RG}}\epsilon} - 1\right)\right\}$$

The entropy never exceeds the thermodynamic dS entropy $S_{\text{dS}} \approx 2\phi_0$.

---

## Key Results

1. The fine-grained entropy of a Minkowskian observer after inflation follows a Page-like curve
2. The entropy never exceeds the thermodynamic dS entropy $2\phi_0$, suggesting the entropy bound may not exist
3. The dominant island is found in the distant past of dS space (time-like separated from $R$)
4. The result passes the strong-subadditivity check (unlike the minimax island of Chen-Gorbenko-Maldacena)
5. If extrapolable to 4D, the dS entropy bound $N_e \lesssim S_{\text{dS}}$ would disappear

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| JT action | $S_{\text{JT}} = \frac{1}{16\pi G}\int d^2x\sqrt{-g}[\phi_0 R + \phi(R - 2H^2)]$ | Eq. (1) |
| dS metric | $ds^2 = \frac{1}{H^2\cos^2\sigma}(-d\sigma^2 + d\varphi^2)$ | Eq. (2) |
| Single-interval entropy | $S = \frac{c}{6}\log\frac{2[\cos(\sigma_2-\sigma_1)-\cos(\varphi_2-\varphi_1)]}{\cos\sigma_1\cos\sigma_2 H^2\epsilon_1\epsilon_2}$ | Eq. (5) |
| Semiclassical entropy | $S_{\text{semi}} \approx \frac{c}{3}\log(Hl_R)$ | Eq. (8) |
| Island entropy | $S = 2\phi_0 + 2\phi_r\tan\sigma_I + S_{\text{semi}}(R \cup I)$ | Eq. (14) |
| Page-like curve | $S(R) \approx \min\{S_{\text{no-island}}, S_{\text{island}}\}$ | Eq. (16) |

## Relevance to Phonon-Exflation

The dS entropy bound and island formula are part of the active tension in understanding de Sitter thermodynamics, which remains unresolved in the framework. The framework's spectral action (free energy) picture is consistent with the thermodynamic interpretation of dS space, but the phonon-exflation model does not require eternal inflation -- the tau transit is finite -- so the entropy bound question has a different character. The island calculation demonstrates that semiclassical entropy computations receive significant corrections from gravitational path integral saddles, a lesson relevant to the framework's GGE relic predictions.
