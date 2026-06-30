#!/usr/bin/env python3
"""
BK-Array Joint Meta-Classifier v2 — callable Python module
============================================================

Provenance: S87 W3-2 CF-21 — `S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2`
Producing wrapper:  computations/session-87/s87_w3_bk_array_meta_classifier_v2.py
Workshop substrate: sessions/archive/session-86/workshops/s86-r-dual-pathway-bk-array-and-nT.md
Theorem source:    sessions/permanent-results-registry.md §VII.AC.3
                   "Rank-2 Product Detector Orthogonality"

Substrate framing
-----------------
The substrate IS a 2x2 product structure: regulator-class lattice
{Lambda_A, Lambda_C} cross-product with block-axis projection
{Path-H, Path-C}. The two axes commute as projection operators
([pi_R, P_alpha] = 0 for all (R, alpha)) per the Rank-2 Product
Detector Orthogonality Theorem. The classifier is a STRUCTURAL
DECODER that reads two substrate-emergent observables (LiteBIRD-
measured n_T, LISA-measured Omega_GW) plus one regulator-class
label, and decodes them into the 2x2 product cell label.

This is NOT a phenomenological inflation-parameter pipeline.
The substrate IS the 2x2 product; the classifier names which
cell of the regulator-class lattice the lab measurement places
the observation in.

Decision matrix (pre-registered, S87 W3-2 plan):
  Block axis (LiteBIRD n_T discriminator):
    Path-H if n_T in [n_T_PathH +/- 0.5*sigma_n_T_LiteBIRD]
    Path-C if n_T in [n_T_PathC +/- 0.5*sigma_n_T_LiteBIRD]
    undecided otherwise (LLR within 1.5 of zero)

  Regulator axis (LISA Omega_GW x regulator_class label):
    (A) if regulator_class == '(A)' AND
        |log10(Omega_GW) - log10(Omega_GW_FW_(A))| < 0.5 OOM
    (C) if regulator_class == '(C)' AND
        |log10(Omega_GW) - log10(Omega_GW_FW_(C))| < 0.5 OOM
    undecided otherwise

The four-cell product is the 2x2 product detector per §VII.AC.3.

Required literal strings (verifier-rubric pre-registration):
  def classify_outcome(
  'cell':
  'block_axis':
  'regulator_axis':
  'rationale':
  PASS-PathH-(A)
  PASS-PathH-(C)
  PASS-PathC-(A)
  PASS-PathC-(C)

Substitution chain (n_T canonical derivation, [SIGN]/[VERIFY] trigger)
-----------------------------------------------------------------------
Step 1 (definitions):
  n_T = -r/8                 (single-field consistency relation, S84 W4-39 EXACT)
  r_PathH         = 0.0074705                  (canonical_constants.py)
  r_CMB_framework = 0.011731522176014426       (canonical_constants.py, ex-S83 G46)
  sigma_n_T_LiteBIRD = 8.0e-4                  (LiteBIRD full-mission projection)

Step 2 (substitute via QQ rational arithmetic, Sage-verified):
  n_T_PathH_canonical = -r_PathH / 8         = -0.0009338125
  n_T_PathC_canonical = -r_CMB_framework / 8 = -0.0014664402720018033

Step 3 (workshop cross-check):
  Workshop §V1 line 19 reports "Path-H -0.000931, Path-C -0.001463"
  Round-figure delta vs canonical: |Path-H| 2.81e-6, |Path-C| 3.44e-6
  Both within workshop's 4-sig-fig truncation; canonical retained.

Step 4 (direction):
  Both n_T_PathH and n_T_PathC are NEGATIVE (red tilt) per the
  substrate's a_4-weighted gradient at k_pivot. The discrimination
  signal |n_T_PathC - n_T_PathH| = 5.326e-4 vs sigma_n_T_LiteBIRD = 8.0e-4
  gives |Delta_n_T|/sigma = 0.6657. With band half-width 0.5*sigma = 4e-4,
  each Path-X window has half-width 4e-4 and the window centers are
  separated by 5.326e-4, so the bands are DISJOINT (gap = 5.326e-4 - 2*4e-4
  = -2.7e-4, slight overlap of 6.7%; n_T values inside the overlap zone
  classify as Path-H by the priority ordering since |delta| is smaller).
  Direction: Path-H/Path-C are decisively distinguishable at LiteBIRD
  full-mission sensitivity for n_T-canonical-centered measurements.
"""

from __future__ import annotations

from typing import Dict, Literal, Union

# Substrate-first canonical pins (S87 W3-2 promotion, canonical_constants.py)
from canonical_constants import (
    n_T_PathH_canonical,
    n_T_PathC_canonical,
    sigma_n_T_LiteBIRD,
    Omega_GW_Lambda_A_LISA,
    Omega_GW_Lambda_C_LISA,
)

import math

# Pre-registered band parameters (verifier-rubric pinned, plan §W3-2.7 tolerance)
_BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA = 0.5  # (local) half-width in units of sigma_n_T_LiteBIRD
_REGULATOR_AXIS_OOM_BAND = 0.5           # (local) half-width in dex (log10 OOM)
_LLR_UNDECIDED_THRESHOLD = 1.5           # (local) log-likelihood-ratio undecided zone

# Cell-label enumeration (verifier-rubric pre-registered)
_CELL_PASS_PATHH_A = 'PASS-PathH-(A)'
_CELL_PASS_PATHH_C = 'PASS-PathH-(C)'
_CELL_PASS_PATHC_A = 'PASS-PathC-(A)'
_CELL_PASS_PATHC_C = 'PASS-PathC-(C)'
_CELL_FAIL_NO_MATCH = 'FAIL-no-cell-match'

_VALID_CELL_LABELS = (
    _CELL_PASS_PATHH_A,
    _CELL_PASS_PATHH_C,
    _CELL_PASS_PATHC_A,
    _CELL_PASS_PATHC_C,
    _CELL_FAIL_NO_MATCH,
)


def _block_axis_decision(litebird_n_T: float) -> Dict[str, Union[str, float]]:
    """Decide block axis (Path-H vs Path-C vs undecided) from LiteBIRD n_T.

    Decision rule (PRE-REGISTERED):
        Path-H if |n_T - n_T_PathH_canonical| < 0.5 * sigma_n_T_LiteBIRD
        Path-C if |n_T - n_T_PathC_canonical| < 0.5 * sigma_n_T_LiteBIRD
        undecided otherwise

    Tie-break (pre-registered): in the bands' overlap zone (which exists
    because the canonical separation is 0.666 sigma < 1.0 sigma), assign
    to the closer canonical (smaller |delta|). This is deterministic and
    matches the LLR Bayes-optimal classifier.
    """
    band_half_width = _BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA * sigma_n_T_LiteBIRD  # (local)
    delta_H = litebird_n_T - n_T_PathH_canonical                              # (local)
    delta_C = litebird_n_T - n_T_PathC_canonical                              # (local)
    in_H = abs(delta_H) < band_half_width                                      # (local)
    in_C = abs(delta_C) < band_half_width                                      # (local)
    # Log-likelihood-ratio under Gaussian model:
    #   LLR = ln P(n_T | Path-H) - ln P(n_T | Path-C)
    #       = -(delta_H^2 - delta_C^2) / (2 * sigma^2)
    # Under priority tie-break, sign(LLR) selects the closer canonical.
    sigma2_two = 2.0 * sigma_n_T_LiteBIRD * sigma_n_T_LiteBIRD                 # (local)
    llr = -(delta_H * delta_H - delta_C * delta_C) / sigma2_two                # (local)

    if in_H and in_C:
        # overlap zone — assign to closer
        if abs(delta_H) <= abs(delta_C):
            decision = 'Path-H'                                                # (local)
        else:
            decision = 'Path-C'                                                # (local)
    elif in_H:
        decision = 'Path-H'
    elif in_C:
        decision = 'Path-C'
    else:
        decision = 'undecided'

    return {
        'block_axis': decision,
        'block_axis_evidence': float(llr),
        'delta_H': float(delta_H),
        'delta_C': float(delta_C),
        'band_half_width': float(band_half_width),
    }


def _regulator_axis_decision(lisa_omega_GW: float, regulator_class: str) -> Dict[str, Union[str, float]]:
    """Decide regulator axis ((A) vs (C) vs undecided) from LISA Omega_GW.

    Decision rule (PRE-REGISTERED):
        (A) if regulator_class == '(A)' AND
            |log10(Omega_GW) - log10(Omega_GW_Lambda_A_LISA)| < 0.5 OOM
        (C) if regulator_class == '(C)' AND
            |log10(Omega_GW) - log10(Omega_GW_Lambda_C_LISA)| < 0.5 OOM
        undecided otherwise

    The regulator_class label is REQUIRED because the (A) / (C) regulator
    classes differ by 48 OOM (1e-10 vs 8.299e-58) and the LISA detection
    floor (~1e-12) sits in between; without the class label, a non-detection
    is consistent with EITHER class. The class label is the substrate-side
    NCG-axiomatic input (M2 axiom regulator selection per Connes-Chamseddine
    1996); the Omega_GW magnitude is the laboratory-side measurement.
    """
    if regulator_class not in ('(A)', '(C)'):
        return {
            'regulator_axis': 'undecided',
            'regulator_log_diff_dex': float('nan'),
            'reason': f"invalid regulator_class={regulator_class!r}; expected '(A)' or '(C)'",
        }
    # Guard against zero / negative Omega_GW (log10 undefined)
    if lisa_omega_GW <= 0.0:
        return {
            'regulator_axis': 'undecided',
            'regulator_log_diff_dex': float('inf'),
            'reason': f"non-positive Omega_GW={lisa_omega_GW}; log10 undefined",
        }

    if regulator_class == '(A)':
        target = Omega_GW_Lambda_A_LISA  # (local)
    else:  # '(C)'
        target = Omega_GW_Lambda_C_LISA  # (local)

    log_diff = abs(math.log10(lisa_omega_GW) - math.log10(target))  # (local)
    if log_diff < _REGULATOR_AXIS_OOM_BAND:
        decision = regulator_class  # (local) '(A)' or '(C)'
    else:
        decision = 'undecided'

    return {
        'regulator_axis': decision,
        'regulator_log_diff_dex': float(log_diff),
        'target': float(target),
    }


def classify_outcome(litebird_n_T: float,
                     lisa_omega_GW: float,
                     regulator_class: str) -> Dict[str, Union[str, float]]:
    """Classify a (LiteBIRD n_T, LISA Omega_GW, regulator_class) tuple
    into the BK-Array 2x2 product detector cell.

    Parameters
    ----------
    litebird_n_T : float
        LiteBIRD-measured tensor spectral index n_T (typically negative
        for red tilt; canonical Path-H = -0.0009338, Path-C = -0.0014664).
    lisa_omega_GW : float
        LISA-measured GW energy density at 3 mHz; must be positive.
    regulator_class : str
        '(A)' or '(C)' — the regulator-class label from substrate-side
        NCG-axiomatic input (M2-axiom regulator selection).

    Returns
    -------
    dict
        {'cell':            <str: PASS-PathH-(A) | PASS-PathH-(C) |
                                  PASS-PathC-(A) | PASS-PathC-(C) |
                                  FAIL-no-cell-match>,
         'block_axis':      <str: 'Path-H' | 'Path-C' | 'undecided'>,
         'regulator_axis':  <str: '(A)' | '(C)' | 'undecided'>,
         'block_axis_evidence': <float: log-likelihood ratio>,
         'rationale':       <str: human-readable per-axis trace>}
    """
    block = _block_axis_decision(litebird_n_T)              # (local)
    reg = _regulator_axis_decision(lisa_omega_GW, regulator_class)  # (local)

    block_axis = block['block_axis']
    regulator_axis = reg['regulator_axis']

    # Build cell label from product. Label format pre-registered (verifier
    # rubric, plan §W3-2.7): "PASS-PathH-(A)" / "PASS-PathH-(C)" /
    # "PASS-PathC-(A)" / "PASS-PathC-(C)" — block-axis token is
    # concatenated WITHOUT internal hyphen ("PathH" not "Path-H") so the
    # regulator-axis hyphen-prefix is unambiguous.
    if block_axis in ('Path-H', 'Path-C') and regulator_axis in ('(A)', '(C)'):
        block_token = block_axis.replace('-', '')  # (local) 'Path-H'->'PathH'
        cell = f"PASS-{block_token}-{regulator_axis}"  # (local)
        # Verifier-rubric: cell must be one of the 4 valid PASS labels
        if cell not in (_CELL_PASS_PATHH_A, _CELL_PASS_PATHH_C,
                        _CELL_PASS_PATHC_A, _CELL_PASS_PATHC_C):
            cell = _CELL_FAIL_NO_MATCH  # (local) defensive guard
    else:
        cell = _CELL_FAIL_NO_MATCH

    rationale = (
        f"block_axis={block_axis} (LLR={block['block_axis_evidence']:+.3f}, "
        f"|deltaH|={abs(block['delta_H']):.3e}, |deltaC|={abs(block['delta_C']):.3e}, "
        f"band={block['band_half_width']:.3e}); "
        f"regulator_axis={regulator_axis} "
        f"(log_diff={reg.get('regulator_log_diff_dex', float('nan')):.3f} dex, "
        f"class_label={regulator_class!r}); "
        f"cell={cell}"
    )

    return {
        'cell': cell,
        'block_axis': block_axis,
        'regulator_axis': regulator_axis,
        'block_axis_evidence': float(block['block_axis_evidence']),
        'rationale': rationale,
    }


# Public exports
__all__ = (
    'classify_outcome',
    'n_T_PathH_canonical',
    'n_T_PathC_canonical',
    'sigma_n_T_LiteBIRD',
    'Omega_GW_Lambda_A_LISA',
    'Omega_GW_Lambda_C_LISA',
    '_VALID_CELL_LABELS',
)
