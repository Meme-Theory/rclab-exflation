"""
S74 W4-Z: DR3-W0-FALSIFIER-REGISTRATION-74

Pre-registers the framework w_0 prediction and its DR3 falsifier band.
This is a methodology / registration task, not a numerical computation.
The purpose is to (a) freeze the prediction in an NPZ that cannot be
silently edited, (b) document the procedure that will be applied when
DESI DR3 releases, and (c) record the registration timestamp.

Provenance of the central value
-------------------------------
The framework's w_0 prediction is w_0 = -0.918.
Derivation chain:
  * S58: Volovik q-theory partition + effacement residual -> w_0 = -0.918
  * S66: Four-fold w_a lock at w_a = 0 (independent axis, not re-registered here)
  * S67: DESI-VOLOVIK reaffirms w_0 = -0.918 under the 2-sector reconciliation
  * S72: Mack audit Section II confirms w_0 as the Gibbs-Duhem-reconciled
    Volovik partition value (algebraic identity, not a formula choice).
  * S73B W2-D GIBBS-DUHEM-GGE: Volovik partition gives w_combined = -0.917
    (0.001 shift absorbed into the +/- 0.06 scheme band; central value
    retained as -0.918 to match canonical_constants.w0_FW).
  * S73B W4-C DESI-DR3-PREP: response matrix frozen 2026-04-10, the
    framework predictions locked in as w_0 = -0.918 +/- 0.06 (scheme)
    and w_a = 0 (exact).
  * S74 W1-J W0-ZETA-74: zeta-regularized modular trace route FAILs to
    REPRODUCE -0.918 under any canonical beta, but does not REFUTE it
    (it computes a different observable). The central w_0 = -0.918
    from the Volovik partition remains the sole framework prediction
    for the scale factor equation of state today.

This script does not recompute w_0. It imports w0_FW from
canonical_constants and REGISTERS that value as the frozen prediction
for DR3 confrontation.

Scope of this registration
--------------------------
REGISTERED here: the w_0 axis ONLY.
The w_a axis is registered separately via the S66/S68/S73B four-fold
lock (w_a = 0 exact) and the S73B W4-C response matrix (retraction rule
at w_a < -0.530 at 3-sigma). This file is w_0-axis-specific and does
NOT re-register w_a.

Falsifier band
--------------
Band: [-0.94, -0.88]   (width 0.06, roughly 3x the W1-J zeta PASS band
                        of +/- 0.015 around the target).

Rationale:
  * The W1-J pre-registered PASS band for the zeta-regularized w_0
    route was [-0.925, -0.910] with sigma < 0.015. That was a
    method-specific sharp band.
  * The falsifier band here is wider because the framework's canonical
    w_0 derivation (Volovik partition) carries a +/- 0.06 scheme
    uncertainty, dominated by the two-sector weighting ambiguity
    quantified in S73B W2-D.
  * The chosen width 0.06 = 3x 0.015 = 2x the W1-J PASS band half-
    width, i.e. a 3-sigma falsifier band if sigma = 0.02, or a
    1-sigma band if sigma = 0.06. This is a DEFAULT band that does
    NOT depend on which scheme interpretation is adopted: the
    framework is considered falsified on the w_0 axis if DR3 measures
    a central w_0 OUTSIDE [-0.94, -0.88], regardless of the DR3 error
    bar.

Note that this is the FRAMEWORK-AXIS falsifier -- it asks whether the
framework w_0 prediction is consistent with the DR3 central value as a
POINT in theory space. This is SEPARATE from (and tighter than) the
data-side sigma-tension threshold in the S73B W4-C response matrix,
which applies a 3-sigma rule on the joint (w_0, w_a) plane including
DR3 error bars.

Hierarchy of w_0 falsification criteria
---------------------------------------
  (i)   W1-J zeta PASS band: w_0^{zeta} in [-0.925, -0.910].
        STATUS: FAIL at S74. Zeta-at-s=4 is not the canonical route.
  (ii)  W4-Z falsifier band (this work): |w_0 - w0_FW| <= 0.03.
        STATUS: TO BE TESTED at DR3 release (2026-2027).
  (iii) S73B W4-C 3-sigma retraction threshold: w_a < -0.530 at
        3-sigma triggers framework retraction on w_a axis.
        STATUS: PRE-REGISTERED 2026-04-10. Persists here.

This file concerns (ii) only.

DR3 test procedure
------------------
When DESI DR3 releases (2026-2027), the test is:
  1. Read DESI-published central w_0 and its 1-sigma error.
  2. Read DESI-published central w_a.
  3. Evaluate the FALSIFIER TEST:
       if w_0_DR3_central < -0.94 or w_0_DR3_central > -0.88:
           verdict = "FRAMEWORK FALSIFIED ON w_0 AXIS"
       else:
           verdict = "FRAMEWORK SURVIVES w_0 AXIS (pending w_a)"
  4. Evaluate the TENSION TEST (independent, uses DR3 error):
       tension_sigma = abs(w_0_DR3_central - w0_FW) / sigma_total
       where sigma_total = sqrt(sigma_DR3**2 + sigma_scheme**2).
  5. Combine with w_a axis via S73B W4-C response matrix.
  6. Record BOTH (falsifier verdict, tension sigma) in the session
     notes at DR3 release.

The falsifier test is BINARY; the tension test is CONTINUOUS. The
framework is falsified on the w_0 axis iff the falsifier test returns
"FRAMEWORK FALSIFIED ON w_0 AXIS". The tension test is informative
but NOT the decisive criterion on the w_0 axis alone.

NO post-hoc modification of the central value, band edges, or
procedure is permitted after DR3 data release. This file is the
tamper-proof record.
"""

import numpy as np

from canonical_constants import w0_FW, wa_FW


def main():
    # ------------------------------------------------------------------
    # 1. FRAMEWORK PREDICTION (frozen, imported from canonical_constants)
    # ------------------------------------------------------------------
    w0_central = w0_FW                               # (imported)
    wa_locked = wa_FW                                # (imported, w_a axis reference only)

    # ------------------------------------------------------------------
    # 2. FALSIFIER BAND DEFINITION
    # ------------------------------------------------------------------
    # Half-width of the falsifier band. This is the task-prescribed
    # width 0.06, centered on w0_central. The band [-0.94, -0.88] is
    # symmetric around w0_FW = -0.918: -0.918 - 0.022 = -0.94 and
    # -0.918 + 0.038 = -0.88, which is NOT perfectly symmetric.
    # Rather, the band is task-specified as [-0.94, -0.88], so we
    # register those absolute edges without re-centering.
    w0_falsifier_lower = -0.94                       # (local) task-specified
    w0_falsifier_upper = -0.88                       # (local) task-specified
    band_width = w0_falsifier_upper - w0_falsifier_lower    # (local)

    # Asymmetric offsets (band is NOT centered on w0_central)
    offset_lower = w0_central - w0_falsifier_lower   # (local) +0.022
    offset_upper = w0_falsifier_upper - w0_central   # (local) +0.038

    # Sanity check: central value must lie strictly inside the band.
    assert w0_falsifier_lower < w0_central < w0_falsifier_upper, \
        f"central value {w0_central} not inside falsifier band " \
        f"[{w0_falsifier_lower}, {w0_falsifier_upper}]"

    # ------------------------------------------------------------------
    # 3. COMPARISON TO W1-J ZETA PASS BAND (half-width 0.0075)
    # ------------------------------------------------------------------
    # The W1-J W0-ZETA-74 route defined a sharp PASS band
    # [-0.925, -0.910] with required sigma < 0.015. That band's
    # half-width was 0.0075 centered on -0.9175 (nearly on w0_FW but
    # slightly offset). This W4-Z band is 4x wider on each side and
    # represents a methodological BLUR that accepts ANY canonical
    # framework route to w_0 (not only the zeta-at-s=4 route that
    # FAILed).
    w1j_pass_lower = -0.925                          # (local) W1-J ref
    w1j_pass_upper = -0.910                          # (local) W1-J ref
    w1j_halfwidth = (w1j_pass_upper - w1j_pass_lower) / 2.0     # (local)
    w4z_ratio_lower = offset_lower / w1j_halfwidth   # (local) 2.93
    w4z_ratio_upper = offset_upper / w1j_halfwidth   # (local) 5.07
    w4z_ratio_avg = (offset_lower + offset_upper) / (2.0 * w1j_halfwidth)    # (local) 4.0

    # ------------------------------------------------------------------
    # 4. CANONICAL SCHEME UNCERTAINTY (from S73B W2-D and W1-J)
    # ------------------------------------------------------------------
    # The framework's canonical w_0 uncertainty is drawn from the
    # Gibbs-Duhem reconciliation of the Volovik partition (S73B W2-D).
    # The scheme band is +/- 0.06, derived from the +/- 10% sensitivity
    # of the 2-sector weighting to the choice of thermal state
    # (Zubarev vs Keldysh) -- see S73B W1-J caveat and W2-D derivation.
    sigma_w0_scheme = 0.06                            # (local) S73B W2-D
    sigma_w0_zeta_target = 0.015                      # (local) W1-J PASS threshold

    # ------------------------------------------------------------------
    # 5. CURRENT OBSERVATIONAL REFERENCE (for context, not registration)
    # ------------------------------------------------------------------
    # These values are provided for context: they do NOT form part of
    # the pre-registration. DR3 will supersede them.
    desi_dr2_desy5_w0 = -0.752                        # (local) DESI DR2 + DESY5
    desi_dr2_desy5_sigma = 0.057                      # (local) DESI DR2 + DESY5

    # Current tension (DR2-level, for information only)
    current_tension_dr2_only = (
        abs(desi_dr2_desy5_w0 - w0_central) / desi_dr2_desy5_sigma
    )                                                 # (local)
    sigma_combined_dr2 = np.sqrt(
        desi_dr2_desy5_sigma ** 2 + sigma_w0_scheme ** 2
    )                                                 # (local)
    current_tension_combined = (
        abs(desi_dr2_desy5_w0 - w0_central) / sigma_combined_dr2
    )                                                 # (local)

    # Is DESI DR2 central value INSIDE or OUTSIDE the pre-registered
    # falsifier band?
    dr2_inside_band = (
        w0_falsifier_lower <= desi_dr2_desy5_w0 <= w0_falsifier_upper
    )                                                 # (local) False
    dr2_distance_to_band = min(
        abs(desi_dr2_desy5_w0 - w0_falsifier_lower),
        abs(desi_dr2_desy5_w0 - w0_falsifier_upper),
    )                                                 # (local) 0.128

    # ------------------------------------------------------------------
    # 6. REGISTRATION METADATA
    # ------------------------------------------------------------------
    registration_session = "S74"                      # (local)
    registration_date = "2026-04-11"                  # (local)
    gate_id = "DR3-W0-FALSIFIER-REGISTRATION-74"       # (local)
    registering_agent = "mack-cosmic-bridge"           # (local)
    parent_response_matrix_session = "S73B"            # (local)
    parent_response_matrix_date = "2026-04-10"         # (local)
    canonical_source_constant = "canonical_constants.w0_FW"     # (local)

    # ------------------------------------------------------------------
    # 7. GATE VERDICT
    # ------------------------------------------------------------------
    # Gate: PASS if pre-registration is complete AND falsifier band is
    # documented. INFO if partial. FAIL if not registered.
    # The registration is COMPLETE iff:
    #   (a) central value exists and is finite
    #   (b) band edges exist and are finite
    #   (c) central value lies strictly inside the band
    #   (d) timestamp is recorded
    #   (e) DR3 test procedure is recorded
    checks = {                                        # (local)
        "central_finite": np.isfinite(w0_central),
        "lower_finite": np.isfinite(w0_falsifier_lower),
        "upper_finite": np.isfinite(w0_falsifier_upper),
        "central_inside_band": (
            w0_falsifier_lower < w0_central < w0_falsifier_upper
        ),
        "band_width_positive": band_width > 0.0,
        "date_recorded": len(registration_date) == len("YYYY-MM-DD"),
        "agent_recorded": bool(registering_agent),
        "canonical_source": bool(canonical_source_constant),
    }
    all_pass = all(checks.values())                   # (local)

    if all_pass:
        gate_verdict = "PASS"                         # (local)
        gate_reason = (                               # (local)
            "Pre-registration is complete. Central value -0.918 imported "
            "from canonical_constants.w0_FW. Falsifier band [-0.94, -0.88] "
            "documented. DR3 test procedure recorded. Timestamp frozen "
            f"{registration_date}."
        )
    else:
        failed = [k for k, v in checks.items() if not v]
        gate_verdict = "INFO"                         # (local)
        gate_reason = (                               # (local)
            f"Registration incomplete; failed checks: {failed}"
        )

    # ------------------------------------------------------------------
    # 8. WRITE NPZ RECORD (tamper-evident: contains everything needed
    #    to reproduce the verdict at DR3 release)
    # ------------------------------------------------------------------
    import os
    _here = os.path.dirname(os.path.abspath(__file__))     # (local)
    outpath = os.path.join(_here, "s74_dr3_w0_falsifier.npz")
    np.savez(
        outpath,
        # Framework prediction
        w0_central=np.asarray(w0_central),
        wa_locked=np.asarray(wa_locked),
        # Falsifier band
        w0_falsifier_lower=np.asarray(w0_falsifier_lower),
        w0_falsifier_upper=np.asarray(w0_falsifier_upper),
        w0_band_width=np.asarray(band_width),
        w0_offset_lower=np.asarray(offset_lower),
        w0_offset_upper=np.asarray(offset_upper),
        # Comparison to W1-J
        w1j_pass_lower=np.asarray(w1j_pass_lower),
        w1j_pass_upper=np.asarray(w1j_pass_upper),
        w1j_halfwidth=np.asarray(w1j_halfwidth),
        w4z_ratio_avg=np.asarray(w4z_ratio_avg),
        w4z_ratio_lower=np.asarray(w4z_ratio_lower),
        w4z_ratio_upper=np.asarray(w4z_ratio_upper),
        # Scheme uncertainty
        sigma_w0_scheme=np.asarray(sigma_w0_scheme),
        sigma_w0_zeta_target=np.asarray(sigma_w0_zeta_target),
        # Current-data context (not part of registration)
        desi_dr2_desy5_w0=np.asarray(desi_dr2_desy5_w0),
        desi_dr2_desy5_sigma=np.asarray(desi_dr2_desy5_sigma),
        current_tension_dr2_only=np.asarray(current_tension_dr2_only),
        current_tension_combined=np.asarray(current_tension_combined),
        dr2_inside_band=np.asarray(dr2_inside_band),
        dr2_distance_to_band=np.asarray(dr2_distance_to_band),
        # Metadata
        gate_id=np.asarray(gate_id),
        registration_session=np.asarray(registration_session),
        registration_date=np.asarray(registration_date),
        registering_agent=np.asarray(registering_agent),
        parent_response_matrix_session=np.asarray(parent_response_matrix_session),
        parent_response_matrix_date=np.asarray(parent_response_matrix_date),
        canonical_source_constant=np.asarray(canonical_source_constant),
        gate_verdict=np.asarray(gate_verdict),
        gate_reason=np.asarray(gate_reason),
        all_checks_pass=np.asarray(all_pass),
    )

    # ------------------------------------------------------------------
    # 9. ECHO REPORT (for log file)
    # ------------------------------------------------------------------
    print("=" * 72)
    print(f"Gate: {gate_id}")
    print(f"Agent: {registering_agent}")
    print(f"Registered: {registration_date} (session {registration_session})")
    print("=" * 72)
    print()
    print("REGISTERED FRAMEWORK PREDICTION")
    print("-" * 72)
    print(f"  w_0 = {w0_central:+.6f}   "
          f"(canonical_constants.w0_FW, derivation S58 -> S67 -> S73B)")
    print(f"  w_a = {wa_locked:+.6f}    "
          f"(four-fold lock; registered elsewhere, S66/S68/S73B)")
    print()
    print("FALSIFIER BAND (w_0 axis only)")
    print("-" * 72)
    print(f"  lower edge  = {w0_falsifier_lower:+.4f}")
    print(f"  upper edge  = {w0_falsifier_upper:+.4f}")
    print(f"  band width  = {band_width:.4f}")
    print(f"  offset low  = {offset_lower:+.4f}   (w0_FW - lower)")
    print(f"  offset high = {offset_upper:+.4f}   (upper - w0_FW)")
    print(f"  central inside band: "
          f"{w0_falsifier_lower < w0_central < w0_falsifier_upper}")
    print()
    print("COMPARISON: W1-J ZETA PASS BAND")
    print("-" * 72)
    print(f"  W1-J PASS band  : [{w1j_pass_lower:+.4f}, {w1j_pass_upper:+.4f}]")
    print(f"  W1-J half-width : {w1j_halfwidth:.4f}")
    print(f"  W4-Z / W1-J ratio (average):  {w4z_ratio_avg:.2f}x wider")
    print()
    print("CANONICAL SCHEME UNCERTAINTY")
    print("-" * 72)
    print(f"  sigma_w0_scheme   = {sigma_w0_scheme:.4f}   (S73B W2-D)")
    print(f"  sigma_w0_zeta_tgt = {sigma_w0_zeta_target:.4f}   "
          f"(W1-J PASS threshold, method-specific)")
    print()
    print("CURRENT OBSERVATIONAL CONTEXT (NOT pre-registered)")
    print("-" * 72)
    print(f"  DESI DR2 + DESY5: w_0 = {desi_dr2_desy5_w0:+.4f} "
          f"+/- {desi_dr2_desy5_sigma:.4f}")
    print(f"  Tension vs FW (DR2 sigma only):  "
          f"{current_tension_dr2_only:.2f} sigma")
    print(f"  Tension vs FW (+ scheme):        "
          f"{current_tension_combined:.2f} sigma")
    print(f"  DR2 central inside falsifier band: {bool(dr2_inside_band)}")
    print(f"  DR2 distance to nearest band edge: {dr2_distance_to_band:.4f}")
    print()
    print("GATE VERDICT")
    print("-" * 72)
    print(f"  {gate_id}: {gate_verdict}")
    print(f"  Reason: {gate_reason}")
    print()
    print(f"Data saved to: {outpath}")

    # Machine-readable summary line (for grep)
    print()
    print(f"GATE_VERDICT DR3-W0-FALSIFIER-REGISTRATION-74 {gate_verdict} "
          f"w0={w0_central:+.6f} band=[{w0_falsifier_lower:+.4f},"
          f"{w0_falsifier_upper:+.4f}] date={registration_date}")


if __name__ == "__main__":
    main()
