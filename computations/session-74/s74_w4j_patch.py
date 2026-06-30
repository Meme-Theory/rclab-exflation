#!/usr/bin/env python3
"""
Atomic patch: replace the W4-J placeholder block in
sessions/archive/session-74/session-74-results-workingpaper.md with the
computed STRUCTURE-RG-SCALE-74 result block.

This script is used to work around concurrent-writer contention
on the shared session results file.  It is idempotent: if the
block has already been replaced (i.e. the placeholder text is
absent), it exits silently with code 0.
"""

import os
import sys

RESULT_BODY = r"""### W4-J: STRUCTURE-RG-SCALE-74 -- 80/20 Partition BAO or Galaxy Bias Feature (phonon-first-cosmologist)

**Status**: COMPLETE
**Gate**: `STRUCTURE-RG-SCALE-74`. PASS if k_RG matches BAO k_peak within 10%. INFO if matches within 30%. FAIL if > 30% off.

**Gate verdict**: **FAIL**. Under both projection conventions the R-G level-spacing scale lies orders of magnitude away from the BAO peak. Interpretation A (physical-wavelength stretch, prompt formula): `k_RG = 6.11e-05 Mpc^{-1}`, `-3.21` OOM below `k_BAO = 0.1 Mpc^{-1}`. Interpretation B (comoving convention, no stretch, matches S73B): `k_RG = 2.03e+53 Mpc^{-1}`, `+54.31` OOM above. The substrate level-spacing does NOT leave a direct imprint at the BAO scale.

**Framing (SUBSTRATE -- mandatory correction).** The R-G level spectrum is NOT a cosmological feature that has been "stretched by expansion". It is a property of the Dirac operator `D_K` on the Jensen-deformed fibre, specifically of the post-transit 4-cell / N_pair=4 / 8-mode BdG block used to certify multi-cell integrability in S73B. In the substrate picture, BAO peaks are emergent interference patterns of GGE acoustic excitations reorganising the `a_2(tau)` spectral weight after the fold. The question of this gate is: is the substrate's INTERNAL mean level spacing -- the fabric-intrinsic resolution of the level spectrum -- secretly the same scale as the emergent BAO peak? A priori there is no reason it should be. The BAO peak emerges from the sound horizon at matter-radiation decoupling (`r_drag ~ 147` Mpc), a scale governed by the GGE equation of state and the post-fold cosmological H(t), not by the level spacing of `D_K`. The gate tests a non-trivial coincidence hypothesis; FAIL confirms the scales are genuinely distinct and the 80/20 partition does NOT have a hidden BAO signature in this direction.

**Two projection conventions (both computed).** There is a factor-of-`exp(N_total)` ambiguity in how an energy scale at the fold projects to a wavenumber today:

- **Interpretation A -- physical-wavelength stretch (prompt-literal).** Treat `<Delta E>` as a physical frequency at the fold; the wavelength `lambda_fold = 2 pi hbar c / <Delta E>` stretches by `a_today / a_fold = exp(N_total) = 3.32e+57` on the way to today. Then `k_RG_today = <Delta E> * M_KK / (hbar_c * exp(N_total))`.
- **Interpretation B -- comoving invariant (S73B convention).** Treat `<Delta E>` as defining a comoving wavenumber in M_KK natural units; k_comoving is conserved so `k_RG_today = <Delta E> * M_KK / hbar_c` in Mpc^{-1} directly. This matches how S73B mapped `k_pivot = 0.05 Mpc^{-1}` to `k_pivot_MKK = 4.30e-57` WITHOUT any `exp(N_total)` factor.

Under A the answer is physically meaningful (R-G scale sits near the cosmological horizon). Under B the answer is a UV scale far above BAO, confirming the level spacing is an internal-geometry quantity, not a cosmological one. The gate is primarily evaluated on A (prompt formula); B is retained as a consistency cross-check.

**Key numbers**:

| Quantity | Value | Unit |
|:---|:---|:---|
| Mean NN spacing `<Delta E>` (all 4 momentum sectors pooled) | `1.749661e-02` | M_KK |
| Median NN spacing | `8.389291e-04` | M_KK |
| Std of NN spacing | `5.191931e-01` | M_KK |
| `<Delta E>` in physical units | `1.299764e+15` | GeV |
| Total eigenvalues pooled | `35960` | -- |
| R-G integrability marker `<r>_overall` | `0.4044` | -- (Poisson 0.386, GOE 0.536) |
| `N_total` (fold -> today, from S73B EFOLD-MAPPING) | `132.4488` | e-folds |
| `exp(N_total) = a_today / a_fold` | `3.3249e+57` | -- |
| `z_fold` (S73B, = T_rh/T_CMB, radiation era only) | `9.6687e+29` | -- |
| `H_phys_fold` | `0.3958` / `2.941e+16` | M_KK / GeV |
| `k_RG_today` -- Interpretation A (prompt-literal, physical stretch) | `6.1130e-05` | Mpc^{-1} |
| `k_RG_today` -- Interpretation B (comoving, S73B convention) | `2.0325e+53` | Mpc^{-1} |
| `k_BAO_peak` (prompt target) | `0.1000` | Mpc^{-1} |
| `k_BAO_sound_horizon` (`2 pi / r_drag`, `r_drag = 147` Mpc) | `0.0427` | Mpc^{-1} |
| `k_CMB_pivot` (Planck) | `0.0500` | Mpc^{-1} |
| `log10(k_RG_A / k_BAO_peak)` | `-3.21` | -- |
| `log10(k_RG_B / k_BAO_peak)` | `+54.31` | -- |
| `|k_RG_A - k_BAO| / k_BAO` (gate metric, primary) | `9.99e-01` | -- |
| `<Delta E>` that WOULD make A coincide with `k_BAO_peak` | `28.62` | M_KK (exceeds full spectral range) |

**Per-sector mean spacings** (M_KK):

| k-sector | `<Delta E>` |
|:---|:---|
| `k = 0` (R-G sector) | `0.0217` |
| `k = pi/2` | `0.0160` |
| `k = pi` | `0.0159` |
| `k = 3 pi / 2` | `0.0160` |

The k=0 sector is modestly larger because it includes 9024 eigenvalues on a slightly wider support; the three non-zero momentum sectors are nearly identical, consistent with S73B's multi-cell R-G homogeneity across momenta.

**Cross-checks**:

1. **Unit-path consistency (primary arithmetic).** Two independent paths from `<Delta E>` (GeV) to `k_fold` (Mpc^{-1}) -- (i) direct via `1/hbar_c * Mpc_to_m` and (ii) via the `Mpc_to_GeV_inv` bridge -- agree to `2.1e-16` relative. The numerical conversion itself is exact to machine epsilon.
2. **S73B `exp(N_total)` vs S73B `z_fold`.** These disagree by a factor of `3.44e+27`. Reason: S73B's `z_fold = T_rh / T_CMB = 9.67e+29` measures ONLY the radiation-era redshift from reheating to today; the pre-reheat modulus/stiff epoch contributes an additional `~6.3e+10` of the total `exp(N_total) = 3.32e+57`. For a fold-epoch-to-today projection we use `exp(N_total)`, which is the correct scale factor ratio across ALL four S73B expansion epochs (stiff, GGE, radiation, matter/Lambda).
3. **Inverse-map sanity on k_pivot.** S73B stores `k_pivot_MKK = 4.30e-57` for `k_pivot = 0.05 Mpc^{-1}` today. Mapping S73B's `k_pivot_MKK` through our Interpretation A path (divide by `exp(N_total)`) does NOT recover `0.05 Mpc^{-1}` -- it gives `1.5e-59 Mpc^{-1}`. This confirms S73B's `k_pivot_MKK` uses Interpretation B (no stretch, one-step dimensional conversion `0.05 Mpc^{-1} -> GeV -> M_KK`). The two interpretations are mutually inconsistent, and a self-consistent cross-session comparison requires fixing the convention once. S73B's sub-horizon test `k_pivot / (aH)|_fold = 1.09e-56` is correct under its own convention (comoving invariant), and says the CMB pivot is massively sub-horizon at the fold.
4. **Cross-check C: what `<Delta E>` would hit `k_BAO`?** Under Interpretation A, inverting the gate: `dE_needed = k_BAO_peak * exp(N_total) * hbar_c / (Mpc_to_m * M_KK) = 28.62` M_KK. That is ~1500x larger than the observed mean spacing and exceeds the full spectral range `|eval_max - eval_min| = 196.8` M_KK per sector only by a factor ~7 -- meaning no single level-spacing quantum in the computed R-G spectrum matches BAO scale. The closest observed NN spacing would be quantile-zero, which is `< 1e-4` M_KK -- five orders of magnitude too small.
5. **Cross-check D: alternative BAO-family targets (`k_BAO_sound_horizon = 0.0427`, `k_BAO_secondary = 0.06`, `k_CMB_pivot = 0.05` Mpc^{-1}).** All yield FAIL at log10 distances of (`-2.84`, `-2.99`, `-2.91`) under Interpretation A, and (`+54.68`, `+54.53`, `+54.61`) under Interpretation B. No BAO-family scale matches the R-G level spacing on either interpretation.
6. **Cross-check: r-statistic consistency.** The S73B pre-registered `<r>_overall = 0.4044 < 0.45` confirming multi-cell integrability is reproduced here from the loaded eigenvalue arrays directly. The NN spacing distribution is Poissonian (confirmed by the integrable label), so `mean NN spacing = 1 / rho(E)` at each energy; the global mean `<Delta E> = 1.75e-2 M_KK` is consistent with `(range)/(N-1) = 5.5e-3` within the factor expected from a non-uniform level density.

**Assessment**:

- **Substrate reading.** The fabric's INTERNAL mean level spacing is a property of `D_K` in the Jensen-deformed fibre, carrying energy scales of order `(1-2) * 10^{-2} M_KK ~ 10^{14}-10^{15}` GeV -- near the GUT scale. This is the scale of the Cooper pair / BCS block structure that governs post-transit R-G integrability. It is NOT the scale of emergent acoustic cosmology. BAO peaks are a feature of the EMERGENT GGE fluid's sound horizon, set by post-fold Hubble evolution, not by `D_K`'s level spectrum.
- **Classification**. GEOMETRIC (internal level spacing of `D_K`) with PHONONIC implication (it would have been PHONONIC if it had matched an acoustic feature, but the gate shows it does not). The result constrains one direction of the 80/20 partition hypothesis -- it says the 20% R-G sector's internal-energy spectrum does NOT directly set the BAO scale.
- **Constraint on solution space.** The 80/20 partition from S73B phonon-first-hawking workshop (80% coherent ballistic transport + 20% R-G DC-permanence sector) is NOT a coincidence detector for the BAO peak. Any BAO signature from the substrate must arise from a DIFFERENT structural route -- e.g., the post-fold GGE acoustic sound horizon at matter-radiation equality, or an interference pattern in the `a_2` spectral weight distribution across cells. The level-spacing-to-k_BAO coincidence channel is now CLOSED. This narrows the carry-forward: W4-J was the simplest test ("is the level spacing secretly the BAO scale?"), and we have ruled it out at 3.2 OOM (Interpretation A) / 54 OOM (Interpretation B).
- **Wrong question vs wrong answer.** Interpretation A's 3.2 OOM miss is in a physically interpretable direction: `k_RG_A ~ 6e-5 Mpc^{-1}` corresponds to a wavelength `~10^{5} Mpc`, which is cosmological-horizon-scale. This is NOT BAO but it IS the order of magnitude where super-horizon modes live today. The level spacing is MUCH finer than the acoustic scale `H_fold = 0.396 M_KK` (by a factor `0.396 / 0.0175 = 22.6`) -- so the spacing represents modes much LONGER than the fold horizon, and after stretching lands on modes much LONGER than BAO.
- **Relation to SUBSTRATE-INFO-PARTITION-THEOREM-74 (W4-K).** This FAIL sharpens W4-K: the 20% R-G "DC-permanence" sector cannot be sold as "it IS the BAO peak". Any theorem formulation of the partition must treat the R-G and coherent sectors as distinct information channels whose observable correlators are reconstructed through the post-fold GGE evolution, not through direct scale matching.

**Output files**:

- Script: `computations/session-74/s74_structure_rg_scale.py`
- Data: `computations/session-74/s74_structure_rg_scale.npz` (all numbers above, both interpretations, per-sector spacings)

**Structural carry-forward to W4-K / S75**: The direct level-spacing-to-BAO coincidence is closed at 3+ OOM. The remaining route for a substrate BAO imprint is the GGE sound horizon computed from the post-fold acoustic sector. If W4-K formalises the 20/80 partition, it must name which information the R-G sector carries (not a wavenumber in Mpc^{-1}) and which the ballistic sector carries (phase coherence that then sets emergent horizons)."""


PLACEHOLDER = (
    "### W4-J: STRUCTURE-RG-SCALE-74 -- 80/20 Partition BAO or Galaxy Bias Feature (phonon-first-cosmologist)\n"
    "\n"
    "**Status**: NOT STARTED\n"
    "**Gate**: `STRUCTURE-RG-SCALE-74`. PASS if k_RG matches BAO k_peak within 10%. INFO if matches within 30%. FAIL if > 30% off.\n"
    "\n"
    "**Results**:\n"
    "\n"
    "*(Agent writes here)*"
)


def main():
    path = os.path.join(
        "sessions", "session-74", "session-74-results-workingpaper.md"
    )
    # Read
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    # Check idempotence
    if PLACEHOLDER not in text:
        # Already replaced or block missing.  Verify our result body is
        # present; if so, nothing to do.
        if "### W4-J: STRUCTURE-RG-SCALE-74" in text and "Gate verdict**: **FAIL" in text:
            print("W4-J block already populated. Exiting idempotently.")
            return 0
        print("ERROR: W4-J placeholder not found and result not present.")
        print("File may have an unexpected W4-J state. Aborting.")
        return 1
    # Count occurrences -- should be exactly 1 for a clean substitution
    n = text.count(PLACEHOLDER)
    if n != 1:
        print(f"ERROR: Placeholder matched {n} times, expected 1. Aborting.")
        return 1
    # Replace
    new_text = text.replace(PLACEHOLDER, RESULT_BODY)
    # Atomic write: temp file + rename
    tmp_path = path + ".w4j.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    os.replace(tmp_path, path)
    print(f"W4-J block written. File length: {len(new_text)} bytes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
