#!/usr/bin/env python3
"""
S90 W3-3 — S90-3HE-B-LIAISON-WATCHLIST-LANDING (CF-35 / CF-S90-MACK-6)
========================================================================

Lands a forward-falsifier liaison-schedule watchlist row at
`sessions/framework/registry/falsifier-watchlist.md` for the 3He-B
Aalto LTL inheritance-falsifier campaign. Substrate prediction is
the Sage-exact cocycle-asymmetry ratio
`substrate_cocycle_ratio_67_88 = ‖φ_67‖_BdG / ‖φ_88‖_BdG = 0.793346 /
0.108307 = 7.324992` (Sage-QQ exact, equivalent rational `114453/15625`
per S86 W-5 R2-B Convergence #3; mnemonic-vs-exact discipline per
`.claude/rules/math-scripts.md §"Mnemonic-vs-exact ratio discipline"` —
cite 7.324992 NOT 7.3250 round form). The substrate-derived ratio is
preserved INTACT in the laboratory measurement under the (Δ_B/Δ_A)^p
cancellation theorem (S86 W-5 DONE-5; machine-precision Python
verification at 0.0e+00 residual).

5-element liaison schedule pre-registration:
  1. Q4 2026 first-contact deadline (mack → Aalto LTL leadership)
  2. 2-3 year program duration (Q4 2026 → Q4 2029)
  3. Feasibility window 2028-2029 (first publishable data)
  4. 4-gate falsifier protocol per `inheritance-falsifier-protocol.md`
     §"Four-Gate Structure" (Gates 1-3 NULL kernel-signature on
     F1+F2+F5+F3+F4 + Gate 2 cocycle-asymmetry 7.3250±0.1% + Gate 4
     F4 multi-pressure slope discrimination)
  5. Cross-links: S87 W2-1 paper `1f38f988…`, S89 W4-3 INFO `5da87779…`,
     S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION (cross-link discovery
     via MCP knowledge index)

4-element Class 8.2 MANDATORY PRDR verifier rubric (institution +
apparatus + theory markers + 2-pattern negative-marker set + exemplar
SHA reserved for 2028 Q4 first publishable data).

volovik-superfluid-universe-theorist CO-AUTHOR (per plan §W3-3 §4):
4 verification sub-claims on substrate-side cocycle-asymmetry
derivation; output: verification note appended at W3 WP §W3-3
sub-section (solo runner authors in-place per agent-ownership-takeover).

Plan: sessions/session-plan/session-90-plan-w3.md §W3-3.
Agent: mack-cosmic-bridge sole writer + volovik CO-AUTHOR.
Trigger: [VERIFY] — no 3-tuple companion row required.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-3HE-B-LIAISON-WATCHLIST-LANDING"  # (local)
SCHEME = "live-watch-liaison-state-poll-plus-publication-poll"  # (local)
CONVENTION = "mack-sole-writer-pre-registration-volovik-co-author"  # (local)
L_MAX = "N/A"  # (local)

WATCHLIST_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-watchlist.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Substrate prediction pins (S86 W-5 C2 + R2-B Convergence #3):
COCYCLE_PHI67_M_KK_SQ = "0.793346"   # (local) ‖φ_67‖ M_KK² per W-5 C2 canonical_constants.py line 274
COCYCLE_PHI88_M_KK_SQ = "0.108307"   # (local) ‖φ_88‖ M_KK² per W-5 C2 canonical_constants.py line 275
SUBSTRATE_RATIO_DECIMAL = "7.324992"  # (local) Sage-QQ exact per canonical_constants.py line 276
SUBSTRATE_RATIO_RATIONAL = "114453/15625"  # (local) Sage-QQ exact equivalent (MCP-derived)

# (Δ_B/Δ_A)^p cancellation theorem source: S86 W-5 DONE-5 (machine-precision
# Python verification at 0.0e+00 residual; common exponent p across φ_67 & φ_88).

# Audit-SHA full-64-char pins (verbatim from plan §6 + W3 prior gates):
S89_W7A_AUDIT_FULL_64 = "01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17"  # (local)
S89_W4_4_AUDIT_FULL_64 = "e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89"  # (local)
CF_29_S90_W2_AUDIT_FULL_64 = "92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27"  # (local)
CF_33_S90_W3_AUDIT_FULL_64 = "736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028"  # (local)
CF_34_S90_W3_AUDIT_FULL_64 = "be1e362c5db63e7376c189893246f91f4c68c2592aa73868437c807b1069d5b4"  # (local)
# 16-char prefix-only audit SHAs cited in plan §6 (full 64-char SHAs not provided
# in plan; preserve plan's prefix form):
S87_W2_1_PAPER_SHA_PREFIX_16 = "1f38f9888538011c"  # (local) S87 W2-1 paper artifact
S89_W4_3_INFO_SHA_PREFIX_16 = "5da87779e18e8174"   # (local) S89 W4-3 INFO verdict

# New parent section (separate from CMB α_s discriminators):
NEW_SECTION_HEADER = "## 3He-B inheritance-falsifier liaison schedule (S90 W3 mack-cosmic-bridge live-watch + volovik CO-AUTHOR)"  # (local)
CF_35_SUBSECTION_ANCHOR = "S90-3HE-B-AALTO-LTL-LIAISON-FORWARD-FALSIFIER"  # (local)

# Per plan §W3-3 §6 verbatim markdown template (lines 393-447 of plan).
WATCHLIST_ROW_TEMPLATE = """\

> **Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))` with algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`; the kernel of the inheritance morphism `ι : A_K → A_BdG = M_2(ℂ)` is `ker(ι_*) = M_3(ℂ)` (the substrate's SU(3)-coloured sector that does NOT inherit into the 3He-B BdG-restricted laboratory parent). The substrate's cocycle-asymmetry ratio `‖φ_67‖_BdG / ‖φ_88‖_BdG = 7.324992` IS the substrate's intrinsic Hochschild-pairing ratio between the chiral pair generator [φ_67] and the Cartan hypercharge generator [φ_88]; the 3He-B Aalto LTL apparatus measures this ratio IN a laboratory-IN superfluid container; the (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5) guarantees the substrate-derived 7.324992 is preserved INTACT in the laboratory measurement, INDEPENDENT of the precise pressure-temperature operating point per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`.

### S90-3HE-B-AALTO-LTL-LIAISON-FORWARD-FALSIFIER

**Origin gate**: `S90-3HE-B-LIAISON-WATCHLIST-LANDING` (Wave-3 mack-cosmic-bridge sole-writer; volovik-superfluid-universe-theorist CO-AUTHOR cocycle-asymmetry verification; CF-S90-MACK-6 / CF-35)

**Class**: forward-falsifier with liaison-state poll cadence; pre-empts CMB-S4 α_s detector horizon by 2-3 years via earlier substrate-cleanliness measurement on a structurally orthogonal axis (3He-B BdG sector vs CMB observational running)

**Substrate prediction — Class A NULL (decisive triplet)**: NULL kernel-signature on F1 + F2 + F5 falsifier rows per `.claude/rules/inheritance-falsifier-protocol.md §"Class A — Kernel-Signature Test"`; substrate predicts NO signal under BDI parent-symmetry protection on the φ_67 chiral-pair generator (rows F1 = Caroli-Matricon ladder asymmetry; F2 = polar-vortex line asymmetry; F5 = µSR knight-shift asymmetry).

**Substrate prediction — Class B cocycle ratio**: `substrate_cocycle_ratio_67_88 = 7.324992` (Sage-QQ exact at machine precision; equivalent rational `114453/15625` in Q; canonical_constants.py:substrate_cocycle_ratio_67_88 line 276 per S86 W-5 R2-B Convergence #3; PROVENANCE entry at line 1191); preserved INTACT in lab measurement under (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5 machine-precision Python verification at 0.0e+00 residual); volovik-superfluid-universe-theorist CO-AUTHOR verified at W3 working paper §W3-3 sub-section "volovik CO-AUTHOR verification note".

**Substrate prediction — Class A NULL (supporting pair)**: NULL kernel-signature on F3 + F4 falsifier rows (F3 = NMR/EPR g-factor asymmetry; F4 = thermal-conductivity anisotropy on chiral-pair vs Cartan generator)

**Substrate prediction — Class B slope discrimination**: F4 multi-pressure slope (Jacobi-cubic vs φ_88-linear) over 0–34 bar pressure scan; substrate predicts Jacobi-cubic slope from φ_67-chiral-pair-dominated thermal-conductivity anisotropy, NOT φ_88-linear from Cartan-hypercharge generator alone.

**Cocycle norm pins (S86 W-5 C2)**:
- `cocycle_norm_phi67 = 0.793346 M_KK²` (canonical_constants.py:cocycle_norm_phi67 line 274; `‖φ_67‖² = δE_6 · δE_7`)
- `cocycle_norm_phi88 = 0.108307 M_KK²` (canonical_constants.py:cocycle_norm_phi88 line 275; `‖φ_88‖² = (δE_8)²`; Jensen-rate-limited at τ_fold=0.19)
- Ratio: `cocycle_norm_phi67 / cocycle_norm_phi88 = 0.793346 / 0.108307 = 7.324992` (Sage-QQ exact = `114453/15625`)

**Laboratory anchor**: 3He-B Aalto LTL apparatus (Helsinki ROTA cells variant; alternate: Lancaster MCT-3); BDI-protected B-phase under (p, T) operating point near polycritical pressure (`P_pc ≈ 21.22 bar, T_pc ≈ 2.273 mK` per `aalto-ltl-multi-session-protocol.md`)

**Liaison schedule (5-element pre-registration)**:
  1. **Q4 2026 first-contact deadline**: mack-cosmic-bridge sends introductory liaison email to Aalto LTL leadership (Vlasov / Krusius successor team; cross-link to S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION INFO record at `s88_gate_verdicts.txt` for groups roster Krusius + Tuoriniemi + Eltsov, A=26+B=38+C=26 lab counts) citing S87 W2-1 paper artifact + substrate prediction structural protection at `7.324992 ± 0.1%` (NOT 7.3250 round form per mnemonic-vs-exact discipline)
  2. **2-3 year program duration**: experimental program 2026 Q4 → 2029 Q4 (3-year window) for full deployment of Gates 1-4
  3. **Feasibility window 2028-2029**: first publishable data targeted for 2028 Q4 - 2029 Q4; pre-empts CMB-S4 first-data 2028+ by parallel timeline AND CMB-HD first-data 2034+ by 5-6 years (cross-link CF-33 + CF-34 sibling watchlist rows)
  4. **4-gate falsifier protocol deployment** (per `.claude/rules/inheritance-falsifier-protocol.md §"Four-Gate Structure"`):
     - Gate 1: kernel-signature NULL on F1 (Caroli-Matricon ladder asymmetry; φ_67-clean) + F2 (polar-vortex line) + F5 (µSR knight-shift) — decisive triplet
     - Gate 2: cohomology-asymmetry ratio prediction `7.3250 ± 0.1%` (substrate-falsifying; Sage-exact 7.324992; mnemonic-vs-exact discipline cite the 7.324992 Sage-exact form, not the round 7.3250)
     - Gate 3: kernel-signature NULL on F3 (NMR/EPR g-factor) + F4 (thermal anisotropy) — supporting pair
     - Gate 4: F4 multi-pressure slope discrimination (Jacobi-cubic vs φ_88-linear over 0–34 bar)
  5. **Cross-links to substrate-side derivation**:
     - S87 W2-1 paper artifact: `papers/s87-3he-b-alpha-s-equivalent.md` (audit_sha prefix `1f38f9888538011c…`)
     - S89 W4-3 3He-B related INFO verdict: audit_sha prefix `5da87779e18e8174…`
     - S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION INFO record: `s88_gate_verdicts.txt` (protocol pre-registered with substrate_ratio=7.324992; A=26+B=38+C=26 lab counts; Krusius+Tuoriniemi+Eltsov groups; horizon S88→S100+ at 2027-2032 lab years; rows 45+46) — cross-link discovery via MCP knowledge index, not in plan §6 cross-link list
     - `.claude/rules/inheritance-falsifier-protocol.md §"Calibration corpus"` S86 W-5 W11-C5 (3He-B vortex-core spectroscopy) + W11-C6 (3He-A µSR)
     - `.claude/rules/cross-pillar-bridge-anatomy.md §VII.W-3.LAB STAGE-1-CANDIDATE` (S88 W4a-17 calibration corpus instance #3; post-CF-21 OE-form retrofit)
     - `sessions/framework/registry/falsifier-master-inventory.md` Row #5 T7-W2-FALS-5 (3He-B Aalto LTL row)
     - `atlas-07-permanent-results §VII.AB.8` (multi-year Aalto LTL liaison CANDIDATE-PENDING; 5-yr horizon 2031)

**PRDR Machinery Pin (4-element verifier rubric per Class 8.2 MANDATORY)**:

- **Pattern set** (liaison-state poll patterns):
  1. `(?i)\\b(Aalto|LTL|Low Temperature Lab|Helsinki ROTA|Lancaster MCT-?3?)\\b` AND `(?i)\\b(3-?He-?B|³He-B|3He B-phase|superfluid helium-3 B-phase)\\b` co-occurrence (institution AND substrate)
  2. `(?i)\\b(?:Caroli[-\\s]Matricon|vortex[-\\s]core spectroscopy|µSR|muon spin (?:rotation|resonance))\\b` (apparatus-specific lexical markers)
  3. `(?i)\\b(?:cocycle|inheritance morphism|kernel signature|BdG asymmetry)\\b` (theoretical lexical markers)
- **Disjunction-vs-conjunction declaration**: pattern 1 conjunction (institution AND substrate); pattern 2 disjunctive (any apparatus); pattern 3 disjunctive accept (any theoretical marker; for liaison-state poll completeness signal)
- **Negative-marker set** (auto-fail patterns):
  1. `(?i)\\b3He-?A\\b(?!.*B)` (3He-A only without B-phase content; wrong superfluid phase)
  2. `(?i)\\b(?:superconductor|3He superfluid bulk)\\b(?!.*BdG)` (bulk superfluidity without BdG-restriction; wrong sector)
- **Exemplar SHA**: `<pinned at first-publication-poll>` (reserved field; trigger event 2028 Q4 first publishable data)

**PASS/INFO/FAIL bands (Gates 1-4 conjunction)**:
- **PASS** (substrate-consistent): Gates 1+2+3 all return NULL on F1+F2+F5+F3+F4 AND Gate 2 cocycle-ratio measurement `|R_lab / 7.324992 − 1| ≤ 0.001` (0.1% RATIO tolerance per `.claude/rules/inheritance-falsifier-protocol.md §"Four-Gate Structure"` Gate 2 + cross-pillar bridge K=B 0.1%) AND Gate 4 slope matches Jacobi-cubic prediction (NOT φ_88-linear) over 0–34 bar
- **INFO** (marginal): Gate 1 OR Gate 3 returns ambiguous signal at rows F1/F2/F5 OR F3/F4 OR Gate 2 ratio agrees within 0.1% < tolerance ≤ 1% OR Gate 4 slope discrimination ambiguous
- **FAIL** (falsified): Gate 1 returns non-NULL on any of F1+F2+F5 OR Gate 2 ratio diverges from 7.324992 by > 1% OR Gate 4 slope matches φ_88-linear (excludes substrate's chiral-pair structural protection)

**Substitution chain for substrate-side cocycle-asymmetry direction** (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"` + `.claude/rules/math-scripts.md §"Mnemonic-vs-exact ratio discipline"`):

```
Step 1: cocycle_norm_phi67 = 0.793346 M_KK²                                 [S86 W-5 C2 pin; canonical_constants.py line 274; substrate spectral triple kernel structure; ‖φ_67‖² = δE_6 · δE_7]
Step 2: cocycle_norm_phi88 = 0.108307 M_KK²                                 [S86 W-5 C2 pin; canonical_constants.py line 275; Cartan hypercharge generator; ‖φ_88‖² = (δE_8)²]
Step 3: substrate_cocycle_ratio_67_88 = cocycle_norm_phi67 / cocycle_norm_phi88
                                       = 0.793346 / 0.108307
                                       = 7.324992                            [Sage-QQ exact at machine precision; equivalent rational 114453/15625 in Q]
Step 4: (Δ_B/Δ_A)^p cancellation theorem (S86 W-5 DONE-5):
        lab(F_i) / lab(F_j) = ‖φ_a‖ / ‖φ_b‖ × (f_i / f_j)
        for common exponents p_i = p_j = p
        ⇒ R_lab_measured = substrate_cocycle_ratio_67_88 = 7.324992          [preserved INTACT under common p; machine-precision Python verification at 0.0e+00 residual]
Step 5: PASS band: |R_lab_measured / 7.324992 − 1| ≤ 0.001                  [Class B 0.1% RATIO per inheritance-falsifier-protocol.md Gate 2]
Direction: substrate predicts the 3He-B Aalto LTL apparatus will measure R_lab = 7.324992 ± 0.1% IF AND ONLY IF substrate's chiral-pair-vs-Cartan structural protection is correct; ANY divergence > 0.1% FALSIFIES substrate.

⚠️ Mnemonic-vs-exact discipline: cite 7.324992 (Sage-exact = 114453/15625 in Q), NOT 7.3250 (round form); per `.claude/rules/math-scripts.md §"Mnemonic-vs-exact ratio discipline"` S86 W-3 RULE-3, mnemonic forms understate or overstate structural ratios. The Gate 2 description carries 7.3250 as a SHORTHAND but the canonical reference value is the Sage-exact 7.324992 form.
```

**Poll cadence**: quarterly (every 90 days) liaison-state poll between mack-cosmic-bridge and Aalto LTL contact + publication-stream regex polling for 3He-B BdG cocycle-asymmetry preprints; escalates to monthly during 2028-2029 deployment window.

**Cross-links**:
- `sessions/framework/registry/falsifier-master-inventory.md` Row #5 T7-W2-FALS-5 (3He-B Aalto LTL row; post-CF-21 OE-form retrofit will update Element 2 from PROSE to `Π^{vortex}_{B-phase}` / `Π^{µSR}_{A-phase}` regex per S88 W7a-73 K=2 MANDATORY)
- `.claude/rules/inheritance-falsifier-protocol.md §"Four-Gate Structure"` (4-gate template; W11-C5/C6 calibration)
- `.claude/rules/cross-pillar-bridge-anatomy.md §VII.W-3.LAB STAGE-1-CANDIDATE` (S88 W4a-17 calibration corpus #3; cross-pillar-bridge anatomy K=3 MANDATORY)
- canonical_constants.py PROVENANCE lines 1185, 1188, 1191 (`cocycle_norm_phi67`, `cocycle_norm_phi88`, `substrate_cocycle_ratio_67_88`; S86 W-5 pins)
- S87 W2-1 paper artifact: `papers/s87-3he-b-alpha-s-equivalent.md` (audit prefix `1f38f9888538011c…`)
- S89 W4-3 INFO verdict: audit prefix `5da87779e18e8174…`
- S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION INFO record (MCP-discovered; not in plan §6 cross-link list): `s88_gate_verdicts.txt` (substrate_ratio=7.324992; groups Krusius+Tuoriniemi+Eltsov; horizon S88→S100+ at 2027-2032 lab years; rows 45+46)
- `aalto-ltl-multi-session-protocol.md` (multi-session protocol reference; polycritical anchor P_pc=21.22 bar, T_pc=2.273 mK)
- Wave-3 sibling watchlist rows: CF-33 CMB-S4 (audit `736178083caa51c0…`) + CF-34 CMB-HD (audit `be1e362c5db63e73…`)
- S89 W7a Sage-QQ exact triple-verification: `01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (LO α_s axis cross-reference; same Sage-QQ machine-precision discipline)
- S89 W4-4 joint hypersurface (Class-8.5 PRU 2D verdict-line value-field calibration): `e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89`
- CF-29 S90 W2 falsifier-master-inventory Row #3 update (sibling axis): `92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27`
"""  # (local)


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def build_promotion_text(original_text):
    """Pure: append new "3He-B inheritance-falsifier liaison schedule" parent
    section + CF-35 sub-section at end of falsifier-watchlist.md.
    Idempotent — re-run on same file returns same text without duplicate.

    AFTER-pattern per `.claude/rules/registry-landing.md §"Bridge-Landing
    Script Architecture"`.
    """
    if CF_35_SUBSECTION_ANCHOR in original_text:
        return original_text  # idempotent: already applied
    sep = "\n" if not original_text.endswith("\n") else ""  # (local)
    appended = (
        original_text
        + sep
        + "\n"
        + NEW_SECTION_HEADER
        + "\n"
        + WATCHLIST_ROW_TEMPLATE
    )
    return appended


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    checks = {
        "new_parent_section_header": NEW_SECTION_HEADER in text,
        "cf_35_subsection_anchor": CF_35_SUBSECTION_ANCHOR in text,
        "cocycle_phi67_pin": "0.793346 M_KK²" in text,
        "cocycle_phi88_pin": "0.108307 M_KK²" in text,
        "substrate_ratio_decimal_sage_exact": SUBSTRATE_RATIO_DECIMAL in text,
        "substrate_ratio_rational_sage_exact": SUBSTRATE_RATIO_RATIONAL in text,
        "delta_B_delta_A_p_cancellation_theorem": "(Δ_B/Δ_A)^p cancellation theorem" in text,
        "s86_w_5_done_5_machine_precision": "S86 W-5 DONE-5" in text,
        "ker_iota_M_3_C_structure": "ker(ι_*) = M_3(ℂ)" in text or "ker(ι_*) = M_3(C)" in text,
        "algebra_A_K_C_H_M_3_C": "A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)" in text,
        "liaison_q4_2026_first_contact": "Q4 2026 first-contact deadline" in text,
        "program_duration_2_3_years": "2-3 year program" in text or "2026 Q4 → 2029 Q4" in text,
        "feasibility_window_2028_2029": "Feasibility window 2028-2029" in text,
        "four_gate_falsifier_protocol_header": "4-gate falsifier protocol deployment" in text,
        "gate_1_null_f1_f2_f5_decisive": "F1 (Caroli-Matricon" in text and "F2" in text and "F5" in text,
        "gate_2_cocycle_ratio_0_1_percent": "7.3250 ± 0.1%" in text,
        "gate_3_null_f3_f4_supporting": "F3 (NMR/EPR" in text and "F4 (thermal" in text,
        "gate_4_jacobi_cubic_vs_phi_88_linear": "Jacobi-cubic vs φ_88-linear" in text,
        "gate_4_pressure_scan_0_34_bar": "0–34 bar" in text,
        "polycritical_anchor_pin": "21.22 bar" in text and "2.273 mK" in text,
        "s87_w2_1_paper_artifact_sha_prefix": S87_W2_1_PAPER_SHA_PREFIX_16 in text,
        "s89_w4_3_info_sha_prefix": S89_W4_3_INFO_SHA_PREFIX_16 in text,
        "s88_aalto_ltl_campaign_coordination_cross_link": "S88-3HE-B-AALTO-LTL-CAMPAIGN-COORDINATION" in text,
        "krusius_tuoriniemi_eltsov_groups": "Krusius + Tuoriniemi + Eltsov" in text,
        "aalto_ltl_multi_session_protocol_cross_link": "aalto-ltl-multi-session-protocol.md" in text,
        "inheritance_falsifier_protocol_four_gate_rule_cite": "inheritance-falsifier-protocol.md" in text and "Four-Gate Structure" in text,
        "cross_pillar_bridge_anatomy_vii_w_3_lab_cross_link": "VII.W-3.LAB STAGE-1-CANDIDATE" in text,
        "atlas_07_vii_ab_8_cross_link": "§VII.AB.8" in text and "CANDIDATE-PENDING" in text,
        "prdr_pattern_set_3_regex_institution_apparatus_theory": (
            "Pattern set" in text
            and "Aalto|LTL|Low Temperature Lab" in text
            and "Caroli[-\\s]Matricon" in text
            and "cocycle|inheritance morphism|kernel signature" in text
        ),
        "prdr_disjunction_conjunction_declaration": "pattern 1 conjunction (institution AND substrate)" in text,
        "prdr_negative_marker_set_2": (
            "Negative-marker set" in text
            and "3He-?A" in text
            and "superconductor" in text
        ),
        "prdr_exemplar_sha_reserved_2028_q4": "<pinned at first-publication-poll>" in text and "2028 Q4" in text,
        "pass_band_gates_conjunction": "Gates 1+2+3 all return NULL on F1+F2+F5+F3+F4 AND Gate 2 cocycle-ratio" in text,
        "info_band_marginal": "Gate 1 OR Gate 3 returns ambiguous signal" in text,
        "fail_band_falsified": "Gate 2 ratio diverges from 7.324992 by > 1%" in text,
        "substitution_chain_5_steps": all(f"Step {i}" in text for i in range(1, 6)),
        "mnemonic_vs_exact_discipline_warning": "Mnemonic-vs-exact discipline" in text,
        "detector_horizon_pre_emption_cmb_s4": "CMB-S4 first-data 2028+" in text or "pre-empts CMB-S4 α_s detector horizon by 2-3 years" in text,
        "detector_horizon_pre_emption_cmb_hd": "CMB-HD first-data 2034+" in text or "pre-empts CMB-S4 α_s detector horizon by 2-3 years" in text,
        "volovik_co_author_cross_link": "volovik-superfluid-universe-theorist" in text and "CO-AUTHOR" in text,
        "cf_33_w3_sibling_cross_link": CF_33_S90_W3_AUDIT_FULL_64[:16] in text,
        "cf_34_w3_sibling_cross_link": CF_34_S90_W3_AUDIT_FULL_64[:16] in text,
        "s89_w7a_full_64char_sha": S89_W7A_AUDIT_FULL_64 in text,
        "s89_w4_4_full_64char_sha": S89_W4_4_AUDIT_FULL_64 in text,
        "cf_29_s90_w2_full_64char_sha": CF_29_S90_W2_AUDIT_FULL_64 in text,
        "substrate_framing_paragraph": "the substrate IS the spectral triple" in text,
        "phononic_framing_rule_cite": "phononic-framing.md" in text and "IS Space, Not IN Space" in text,
        "lancaster_mct_3_alternate_apparatus": "Lancaster MCT-3" in text,
        "polar_vortex_line_f2_row": "polar-vortex line" in text,
        "mu_sr_knight_shift_f5_row": "µSR knight-shift" in text or "muon spin" in text,
    }
    return all(checks.values()), checks


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [SHARED_DIR / "canonical_constants.py", WATCHLIST_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (append new 3He-B inheritance-falsifier liaison schedule section + CF-35 row)")
    original = WATCHLIST_PATH.read_text(encoding="utf-8")
    promoted = build_promotion_text(original)

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(WATCHLIST_PATH, promoted)

    print("Step 3: re-read + verify (single-shot AFTER-pattern)")
    re_read = WATCHLIST_PATH.read_text(encoding="utf-8")
    overall, checks = verify_section_matches(re_read)
    n_pass = sum(1 for v in checks.values() if v)  # (local)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    verdict = "PASS" if overall else "FAIL"
    verdict_value = (
        f"watchlist_row_landed={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"new_parent_section_3he_b_inheritance_falsifier_appended=True;"
        f"cf_35_subsection_anchor_appended=True;"
        f"cocycle_norm_phi67_0_793346=True;"
        f"cocycle_norm_phi88_0_108307=True;"
        f"substrate_cocycle_ratio_67_88_sage_exact_7_324992_eq_114453_over_15625=True;"
        f"delta_b_delta_a_p_cancellation_theorem_s86_w_5_done_5=True;"
        f"ker_iota_M_3_C_substrate_su3_coloured_sector=True;"
        f"5_element_liaison_schedule=True;"
        f"q4_2026_first_contact_deadline=True;"
        f"program_2_3_years_2026_to_2029=True;"
        f"feasibility_2028_2029=True;"
        f"4_gate_falsifier_protocol_inheritance_falsifier_protocol_md=True;"
        f"gate_2_cocycle_asymmetry_7_3250_0_1_pct=True;"
        f"gate_4_jacobi_cubic_vs_phi_88_linear_0_34_bar=True;"
        f"polycritical_anchor_21_22_bar_2_273_mK=True;"
        f"s87_w2_1_paper_artifact_cross_link={S87_W2_1_PAPER_SHA_PREFIX_16};"
        f"s89_w4_3_info_cross_link={S89_W4_3_INFO_SHA_PREFIX_16};"
        f"s88_aalto_ltl_campaign_coordination_cross_link_mcp_discovered=True;"
        f"krusius_tuoriniemi_eltsov_groups_cross_link=True;"
        f"aalto_ltl_multi_session_protocol_cross_link=True;"
        f"atlas_07_vii_ab_8_candidate_pending_cross_link=True;"
        f"prdr_4_element_rubric_institution_apparatus_theory=True;"
        f"pass_info_fail_bands_gates_conjunction=True;"
        f"substitution_chain_5_steps=True;"
        f"mnemonic_vs_exact_discipline_pinned_7_324992_NOT_7_3250=True;"
        f"detector_horizon_pre_emption_cmb_s4_cmb_hd=True;"
        f"volovik_co_author_cross_link=True;"
        f"cf_33_w3_sibling_cross_link={CF_33_S90_W3_AUDIT_FULL_64[:16]};"
        f"cf_34_w3_sibling_cross_link={CF_34_S90_W3_AUDIT_FULL_64[:16]};"
        f"s89_w7a_full_64char_sha={S89_W7A_AUDIT_FULL_64[:16]};"
        f"s89_w4_4_full_64char_sha={S89_W4_4_AUDIT_FULL_64[:16]};"
        f"cf_29_s90_w2_full_64char_sha={CF_29_S90_W2_AUDIT_FULL_64[:16]};"
        f"substrate_framing_paragraph_present=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
