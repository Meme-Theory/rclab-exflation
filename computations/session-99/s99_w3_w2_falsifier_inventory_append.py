"""S99 close — mack-cosmic-bridge sole-writer falsifier-inventory landings.

Single-shot, race-safe append-only writes to
`sessions/framework/registry/falsifier-master-inventory.md`
(POSIX O_APPEND single open("a"); no Edit-tool round-trip on the shared registry,
per `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"`).

Two landings (both verdicts FINAL + on disk; this script lands the falsifier-inventory
CONSEQUENCES per math-scripts.md Canonical Write-Order Step 3, NOT a re-derivation):

  UPDATE 1 — NEW Row #77: substrate type-I seesaw Sum m_nu (S99 W3-2 PASS).
  UPDATE 2 — Row #76 BBN-stays-LIVE annotation (S99 W2-2 BBN-RELIEF FAIL).

Idempotency: each block is keyed by a unique anchor string (the §-header). If the
anchor is already present, that block is SKIPPED (no duplicate append). This makes
re-runs safe.
"""
import io
import os
import sys

# Canonical-constants sourcing (required by computations/_shared/CLAUDE.md): the row
# text below cites Sigma_mnu_FW / Sigma_mnu_bound_DESI_2024 / delta_N_eff_vacuum_BBN_below /
# rho_vac_over_rho_rad_BBN_below. We import the canonical values and assert the literals
# embedded in the row prose match them (no silent drift from canonical).
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "_shared"))
from canonical_constants import (  # noqa: E402
    Sigma_mnu_FW,
    Sigma_mnu_bound_DESI_2024,
    delta_N_eff_vacuum_BBN_below,
    rho_vac_over_rho_rad_BBN_below,
)

INVENTORY = "sessions/framework/registry/falsifier-master-inventory.md"  # (local)

# Canonical-vs-prose consistency guard (the row text is hand-authored falsifier prose;
# this asserts the embedded numerals equal the canonical constants, sourcing-axis check
# per .claude/rules/substrate-first-canonical-sourcing.md). Bit-exact on the published
# precision the constants carry.
assert abs(Sigma_mnu_FW - 0.0582053272) < 1e-12, Sigma_mnu_FW
assert Sigma_mnu_bound_DESI_2024 == 0.072, Sigma_mnu_bound_DESI_2024
assert delta_N_eff_vacuum_BBN_below == 2.0873, delta_N_eff_vacuum_BBN_below
assert rho_vac_over_rho_rad_BBN_below == 0.474049, rho_vac_over_rho_rad_BBN_below

# ---- Verdict pins (verified against npz + s99_gate_verdicts.txt; NOT recomputed) ----
# UPDATE 1 — S99-W3-SEESAW-SUMMNU PASS
ROW77_ANCHOR = "## NEW Row #77 — S99 W3-2 substrate type-I seesaw neutrino mass sum"  # (local)
W3_AUDIT = "499dcba1c81194b63da740c0fcdbbef4e2d59a4ad4d8057353e160e09466137b"  # (local)
W3_CONTENT = "cc8c6a4e7d5aa3f637319e7bb27d771c8faf4f9fc03eb5530b5ad2140c7d25ee"  # (local)
# UPDATE 2 — S99-W2-BBN-RELIEF FAIL
BBN_ANCHOR = "**BBN stays-LIVE annotation (S99 W2-2 BBN-RELIEF FAIL"  # (local)
W2_AUDIT = "8fe0ef45395c71d0233e5509cfaf0a3b10c5ec1758997cc57ea94e96d0e08949"  # (local)
W2_CONTENT = "338e6e098d17797a8f2b977df5fdf4e5c5695075f5c2ee1d807a0c5e1c14fd6f"  # placeholder; overwritten below from disk-verified value  # (local)
# The exact content_sha256 from the verdict line (disk-verified):
W2_CONTENT = "338e6e098d17797a8f2b977df5fdf4e5c5695075f5c2ee1d807a0c5e1c14fd6f"  # (local)

# ---------------------------------------------------------------------------
# UPDATE 1 block — NEW Row #77 (Sum m_nu seesaw)
# ---------------------------------------------------------------------------
ROW77 = """

@@ROW77_ANCHOR@@ (canonical write-order Step 3; mack-cosmic-bridge sole-writer landing)

> **Origin**: gate `S99-W3-SEESAW-SUMMNU` (S99 W3-2, PASS; `[SIGN]` 3-tuple `sign=PASS magnitude=PASS regime=VALID`). NEW falsifier ROW — the absolute Σm_ν seesaw observable was ABSENT from this inventory before this row (the existing ν-sector row is Register-A "ν mass ORDERING", a distinct observable: the zero-free-parameter eigenvalue ordering B1<B2<B3, NOT the absolute mass SUM). Canonical write-order Step 3 NEW-row landing per `math-scripts.md`; the constant `Sigma_mnu_FW` was promoted to `canonical_constants.py` ahead of this row (Step 2 already done).
> **Gate audit pin**: `S99-W3-SEESAW-SUMMNU` PASS, `audit_sha256=@@W3_AUDIT@@` (full 64-hex on verdict line 10 of `computations/session-99/s99_gate_verdicts.txt`); content_sha256=`@@W3_CONTENT@@`; `[SIGN]` 3-tuple `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`. Source npz `computations/session-99/s99_w3_seesaw_summnu.npz` (`Sigma_mnu_eV=0.05820532724812581`, cross-check reldiff `1.16e-05`).
> **Canonical-constant pins**: `Sigma_mnu_FW = 0.0582053272` eV (S99, source `s99_w3_seesaw_summnu.npz`, gate `S99-W3-SEESAW-SUMMNU`); `Sigma_mnu_bound_DESI_2024 = 0.072` eV (DESI 2024 arXiv:2404.03002 DR1 BAO, ΛCDM+Σm_ν, 95% CL).

| # | Observable | Falsifier function | Channel(s) | Prediction value(s) | Live-watch envelope | Internal-consistency split | Detector / horizon | scheme | convention | L_max | content_sha256 | audit_sha256 | notes |
|:-:|:-----------|:-------------------|:-----------|:--------------------|:--------------------|:----------------------------|:--------------------|:-------|:-----------|:------|:----------------|:--------------|:------|
| 77 | Σm_ν (substrate type-I seesaw neutrino mass sum) — the seesaw-suppressed image of the D_K B-branch fold energies; M_R = D_K B-branch fold energies M_R_MKK=[1.00440, 1.07857, 1.17000] (M_R_GeV≈[7.46, 8.01, 8.69]×10¹⁶), KO-dim-6 Pfaffian Majorana texture; light masses m_ν=[0, 0.0086776, 0.0495278] eV (normal ordering, m_2/m_3 oscillation-anchored) via m_ν=−m_D M_R⁻¹ m_Dᵀ | the substrate predicts Σm_ν below the DESI cosmological bound with a substrate-FIXED suppression DIRECTION (all dm_ν/dM_R<0, `suppression_all_negative=True`) and normal ordering; a measured Σm_ν ABOVE the DESI/CMB bound, or an INVERTED ordering, or a non-suppressing M_R direction, falsifies the type-I-seesaw-on-D_K-fold-energies leg | Σm_ν cosmological sum (DESI BAO+CMB); JUNO/DUNE ordering cross-cut (shared with Row #6 ordering) | **Σm_ν_FW = 0.0582053272 eV** (`Sigma_mnu_FW`, S99). vs **DESI 2024 bound Σm_ν < 0.072 eV** (95% CL, `Sigma_mnu_bound_DESI_2024`, arXiv:2404.03002) ⇒ **PASS by 19% (margin 0.0138 eV; ratio 0.808)**. INFO-ceiling cross-mark: < 0.12 eV looser Planck-class bound (`info_ceil`, trivially satisfied). M_R↔S60-log spectral coincidence maxrel 0.0177 (`M_R_spectral_coincidence_maxrel`, the fold-energy ↔ S60 right-handed scale agreement) | DESI-DR3 (2026) cosmological Σm_ν tightening toward ~0.04–0.06 eV sensitivity is the near-term cliff-edge: a DR3 bound below 0.0582 eV would convert this PASS into a tension on the MINIMAL-NO value | **CAVEAT (m_D-normalization, NOT internal-inconsistency)**: the m_D Dirac-Yukawa normalization is OSCILLATION-ANCHORED (Y_i back-solved from measured m_2/m_3, Y=[0, 4.794, 11.928], m_D_GeV=[0, 833.8, 2074.8]), so **0.0582 eV is the MINIMAL normal-ordering Σ under the substrate M_R**, NOT a zero-free-parameter absolute. SUBSTRATE-FIRST content = {M_R from D_K B-branch fold energies + seesaw structure m_ν=−m_D M_R⁻¹ m_Dᵀ + suppression DIRECTION (all-negative) + normal ORDERING}; the absolute Σ magnitude is NOT yet zero-free-parameter. m_D-normalization firming = `CF-S100-MD-NORMALIZATION` | DESI-DR3 2026 (Σm_ν cosmological) / JUNO 2026+ + DUNE 2030s (ordering cross-cut) | type-I-seesaw-substrate-MR-as-DK-foldenergy | ABSOLUTE | 12 | `@@W3_CONTENT@@` | `@@W3_AUDIT@@` | NEW S99 W3-2; substrate-FIRST = M_R(D_K fold) + seesaw structure + suppression direction + normal ordering; absolute Σ NOT-yet-ZFP (m_D oscillation-anchored), firming = CF-S100-MD-NORMALIZATION; eta_B=0 EXACT (T.11 leptogenesis CP-source vanishes, δ_CP∈{0,π} allowed); cross-cut to Row #6 ordering + §7.3 item-(4) D5 Majorana-vs-Dirac reconciliation (UNRECONCILED — designated-writer prose, NOT this falsifier-cell landing) |

**Substrate-IS framing (PHONONIC).** Σm_ν IS the seesaw-suppressed image of the D_K eigenvalues, read FORWARD: `D_K B-branch fold energies → M_R (right-handed Majorana scale, KO-dim-6 Pfaffian texture) → m_ν = −m_D M_R⁻¹ m_Dᵀ (type-I seesaw) → Σm_ν = 0.0582 eV`. The right-handed scale M_R is NOT a fitted heavy mass tuned to relieve a cosmological bound — it IS the substrate's own B-branch fold-energy spectrum (M_R_MKK ∼ O(1) in M_KK units, M_R_GeV ∼ 7–9×10¹⁶ GeV). The DESI 2024 Σm_ν < 0.072 eV bound is the **laboratory-IN** falsifier (the lab measures the mass sum IN the cosmological-background container via BAO+CMB). The suppression DIRECTION (heavier M_R ⇒ lighter m_ν, all `dm_ν/dM_R<0`) is substrate-FIXED and is the structurally-robust content; the absolute Σ magnitude carries the m_D oscillation-anchoring caveat above. Direction `D_K eigenvalues → fold energies → seesaw → Σm_ν → measurement` unchanged (per `phononic-framing.md §"IS Space, Not IN Space"`; the substrate IS the mass sum, the lab probes it).

**Cross-references**: Row #6 (ν mass ORDERING, the zero-free-parameter eigenvalue-ordering observable — Σm_ν is the distinct absolute-SUM observable sharing the JUNO/DUNE ordering cross-cut); capstone §7.1 Register-B + flat-reference Σm_ν row + §7.2 anchor row (this session's mack-cosmic-bridge §7-surface cells); capstone §7.3 item-(4) D5 "no-seesaw" cross-reference (STATUS: unreconciled — the §0/§7.3 "no Majorana M_R" framing vs this type-I-seesaw-on-fold-energies row is a math/physics adjudication routed to the W4 D5 0νββ Majorana-vs-Dirac gate / designated-writer prose, **NOT** resolved by this falsifier-cell landing); `canonical_constants.py` (`Sigma_mnu_FW`, `Sigma_mnu_bound_DESI_2024`); `CF-S100-MD-NORMALIZATION` (the m_D-normalization firming carry-forward — converts MINIMAL-NO to absolute if a zero-free-parameter m_D is derived). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole writer for `falsifier-master-inventory.md` (AMRI-PROMOTED 2026-04-28).
""".replace("@@ROW77_ANCHOR@@", ROW77_ANCHOR).replace("@@W3_AUDIT@@", W3_AUDIT).replace("@@W3_CONTENT@@", W3_CONTENT)

# ---------------------------------------------------------------------------
# UPDATE 2 block — Row #76 BBN-stays-LIVE annotation (appended below Row #76's S98 block)
# ---------------------------------------------------------------------------
BBN = """

@@BBN_ANCHOR@@; the S99 follow-up to the S98 CF-MK3-2 BBN-fraction FAIL; mack-cosmic-bridge sole-writer landing).** Gate `S99-W2-BBN-RELIEF` (S99 W2-2, FAIL; `[SIGN]` 3-tuple `sign=PASS magnitude=FAIL regime=VALID`; `audit_sha256=@@W2_AUDIT@@`, content_sha256=`@@W2_CONTENT@@`, full 64-hex on verdict line 6 of `computations/session-99/s99_gate_verdicts.txt`) is the S99 follow-up that ASKED whether any substrate mechanism can deliver the residual suppression the S98 CF-MK3-2 FAIL left open. **Verdict: NO substrate-justified mechanism closes the gap; BBN-VOLOVIK-67 / Window-8 STAYS LIVE as a STRUCTURAL sub-threshold tension (Track B), NOT closed.**

- **The from-below relief is REAL and correct-DIRECTION** (unchanged from S98): `relief_factor = 0.414115` (`(ρ_vac/ρ_rad)_BBN = 0.474049` cuts the unsuppressed `n=2` baseline `frac_base = 1.144730` down by factor 0.414; `relief_direction=True`, `sign_verdict=PASS`). The smaller from-below `n_eff = 1.978111` dilutes the vacuum FASTER, leaving LESS vacuum at BBN — the correct sign, inherited from the same q³ anharmonicity that pins the from-below sign (NOT an independent coin-flip; per the S97 W-1 DISSENT corollary).
- **But it is ~2.087× too weak** (`magnitude_verdict = FAIL`): `(ρ_vac/ρ_rad)_BBN = 0.474049 > bound 0.227107` (= 7/8·(4/11)^{4/3}; the same physical quantity the S98 row and `canonical_constants.py` carry as `0.227113` — two roundings of the identical νN_eff conversion factor) ⇒ **`ΔN_eff(vacuum)_BBN = 2.0873 > 1`** (`delta_N_eff_vacuum_BBN_below`, S98, Sage-verified). To reach the `ΔN_eff < 1` BBN bound the substrate would need an ADDITIONAL suppression `extra_needed = 0.479080` (the residual ×0.479 on top of the 0.414 already delivered).
- **None of the 3 candidate substrate mechanisms is substrate-justified** (`any_substrate_justified = False`, the S99 W2-2 core finding): **(a) larger Δn / steeper exponent** would require `n_eff → 1.959839` (a shift of ×1.835 in the departure `2−n_eff` beyond the substrate-pinned `C_meas = −0.0219` from the q³ anharmonicity — NOT substrate-justified, the anharmonic coefficient is well-conditioned at its computed value); **(b) epoch-dependent α_V** would require `α_V_req = 0.479080` (a tracking-coefficient suppression with no substrate derivation — the Volovik tracking law `ρ_vac = α_V M_Pl² H^{n_eff}` carries no epoch-dependent α_V mechanism); **(c) a distinct dilution channel** would require only `475.2 of 992` D_K modes to gravitate at BBN (a `N_eff/992` mode-restriction à la cc-path-d D-57, with NO substrate selection rule picking out that sub-set). Each candidate CAN arithmetically deliver the residual ×0.479, but NONE is derivable from the substrate's own structure.
- **Disposition: STRUCTURAL sub-threshold tension (Track B), STAYS LIVE.** BBN-VOLOVIK-67 / Window-8 remains the SAME OPEN cross-cut it has been since S67 — the from-below sign relieves the S67 `0.67`-baseline partway (to `0.474`, factor 0.414) but does NOT reach `frac < 0.227` / `ΔN_eff < 1`. The S99 W2-2 result CLOSES the question "can a substrate mechanism rescue the BBN arm?" with **NO** (no substrate-justified ×0.479), which is itself informative: it routes the BBN arm to a STRUCTURAL Track-B tension (a boundary that sharpens the surviving solution space per `feedback_reporting-framing.md`), NOT a closure and NOT a clean PASS. The **present-epoch DILUTION-CC (`rho_vac_over_rho_obs = 1.032`, z=0 lever `[H/H₀]^{n−2}=1` for ANY n) is UNAFFECTED** — the FAIL is the high-redshift `X = ln(H_BBN/H_0) = 40.2756` (log10 = 17.4915, z_BBN ≈ 4×10⁸, rad-dominated) lever arm only. **C10 (Atlas-04) stays `ASSUMED-PARTIALLY-PROVEN`** (the BBN arm was already the OPEN cross-cut since S67; only Object C / the relaxation-linearity closure moves the C10 tag, NOT this BBN-arm FAIL).

**Substrate-IS framing (PHONONIC).** The BBN vacuum fraction IS the a₀ tracking-vacuum (`ρ_vac(q) = ε(q) − q·dε/dq` on the 992 D_K eigenfrequencies) evaluated at the rad-dominated BBN epoch, read FORWARD through the tracking law `ρ_vac ∼ M_Pl² H^{n_eff}`. The from-below relief is the substrate's OWN q³ anharmonic softening (`C_meas = −0.0219 < 0`) carried through the 18-decade lever — NOT a dark-energy field tuned in an FRW container to relieve a BBN tension (the container-thinking reading `phononic-framing.md` forbids). The S99 finding is that the substrate's anharmonicity delivers the correct-sign relief but at a FIXED magnitude (0.414) that the substrate's own structure cannot push further to 0.479×0.414 without an unjustified knob — so the BBN arm IS a genuine structural sub-threshold tension, an honest boundary on the tracking-vacuum leg of DILUTION-CC-66 read directly off the substrate, not a documentation artifact.

**Cross-references**: Row #76 primary cell + the S98 CF-MK3-2 BBN-fraction block immediately above (the from-below relief `0.414` + `ΔN_eff=2.0873` this S99 row confirms STAYS sub-threshold); Atlas-04 C10 row (`atlas-04-assumptions.md:69`, the substrate-derivation + two-layer/three-object register, tag UNMOVED); BBN-VOLOVIK-67 / Window-8 (`atlas-05-walls-doors-windows.md`, the BBN cross-cut target, STAYS OPEN since S67); the W6 `rho_vac_over_rho_obs = 1.032` pin (present-epoch sign-INSENSITIVE, UNAFFECTED, needs no edit); `canonical_constants.py` (`delta_N_eff_vacuum_BBN_below = 2.0873`, `rho_vac_over_rho_rad_BBN_below = 0.474049`). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole writer for `falsifier-master-inventory.md` (AMRI-PROMOTED 2026-04-28).
""".replace("@@BBN_ANCHOR@@", BBN_ANCHOR).replace("@@W2_AUDIT@@", W2_AUDIT).replace("@@W2_CONTENT@@", W2_CONTENT)


def already_present(text, anchor):  # (local)
    return anchor in text


def main():  # (local)
    with io.open(INVENTORY, "r", encoding="utf-8") as f:
        existing = f.read()  # (local)

    to_append = []  # (local)
    skipped = []  # (local)

    if already_present(existing, ROW77_ANCHOR):
        skipped.append("Row #77 (Sum m_nu) — anchor already present, SKIP")
    else:
        to_append.append(ROW77)

    if already_present(existing, BBN_ANCHOR):
        skipped.append("Row #76 BBN-stays-LIVE annotation — anchor already present, SKIP")
    else:
        to_append.append(BBN)

    if to_append:
        # single-shot POSIX O_APPEND; no Edit-tool round-trip on the shared registry
        with io.open(INVENTORY, "a", encoding="utf-8") as f:
            f.write("".join(to_append))

    print("=== S99 falsifier-inventory landing ===")
    for s in skipped:
        print("SKIP:", s)
    print("APPENDED blocks:", len(to_append))
    # post-write verification (re-read; verify both anchors present on disk)
    with io.open(INVENTORY, "r", encoding="utf-8") as f:
        after = f.read()  # (local)
    ok_row77 = ROW77_ANCHOR in after and W3_AUDIT in after  # (local)
    ok_bbn = BBN_ANCHOR in after and W2_AUDIT in after  # (local)
    print("VERIFY Row #77 anchor + W3 audit_sha on disk:", ok_row77)
    print("VERIFY Row #76 BBN-stays-live anchor + W2 audit_sha on disk:", ok_bbn)
    if not (ok_row77 and ok_bbn):
        print("FAIL: post-write verification did not find both anchors")
        sys.exit(1)
    print("OK: both landings verified on disk")
    sys.exit(0)


if __name__ == "__main__":
    main()
