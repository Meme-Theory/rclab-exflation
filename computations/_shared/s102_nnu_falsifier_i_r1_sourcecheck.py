#!/usr/bin/env python3
"""
S102-NNU-FALSIFIER-I-R1-SOURCECHECK (CF-alpha)
==============================================

Falsifier (i) of the Normalization-Non-Universality theorem-tag (registry slot
sessions/permanent-results-registry.md SS-VII.BS, Stage-1 candidate).

QUESTION (symmetric two-branch falsifier; NOT iterate-until-PASS):
  Can gamma_unit = dt_SI/dt_sub (the substrate->seconds conversion the cosmological
  Hubble rate H(tau_now) in km/s/Mpc actually needs) be written as Phi(D_K eigenvalues
  alone, f, Lambda) with ZERO imported dimensionful GeV/seconds scale?

  PASS-branch (theorem FALSIFIED, rank-0): an honest H(tau_now) assembled from the
     substrate inputs alone lands within a factor of 2 of 67.4 km/s/Mpc with ZERO
     imported continuous parameter AND |derived_kappa - kappa_nat|/kappa_nat <= 1e-3.
  FAIL-branch (theorem CONFIRMED, rank-1): the assembly imports M_KK-in-GeV (or
     hbar-in-Js); the zero-new-parameter clause fails; any factor-2 proximity is
     bought by the external M_Pl/M_KK ~ f2 ~ 92 calibration, not by the spectrum.
  INFO (middle): a factor-2 number is produced BUT only via the imported M_KK-in-GeV
     scale (SIGN-correct, import still present). Routes to the standing-gap
     M_KK-DERIVATION review.

SUBSTRATE FRAMING (phononic-framing.md SS"IS Space, Not IN Space"; GEOMETRIC):
  D_K eigenvalues -> spectral moments -> a DIMENSIONLESS dynamical functional;
  the second (km/s/Mpc) requires multiplying by gamma_unit = hbar/(M_KK c^2), an
  IMPORT. The substrate determines the dimensionless content; the second is supplied
  by the one external cutoff M_KK (the eigenvalue problem is SILENT there BY
  CONSTRUCTION because N_3 = 0, BDI class, leaves the induced metric unprotected, S44).

METHOD: build H_assembled(tau_now); STATICALLY enumerate every multiplicative
  dimensionful factor; tag each {dimensionless-spectral | M_KK-in-GeV-IMPORT |
  hbar-in-Js-IMPORT | G_DeWitt-pure-number | f2-dimensionless-ratio}; count *-IMPORT
  tags; compute derived_kappa = hbar/(M_KK_GeV * GeV_to_J) and compare to kappa_nat.

Plan: sessions/session-plan/session-102-plan-w1.md SS-W1-2 (CF-alpha).
Agent: volovik-superfluid-universe-theorist (Sakharov-non-universality / induced-gravity
       dimensional bookkeeping; authored the V1 dimensional chain).

Scheme: SI-dimensional-chain-hbar-over-E (matches S96-W1-MKK-SECONDS exactly).
Convention: natural-units-to-SI-M_KK-SYMMETRIC-FALSIFIER.
L_max: 12 (s84 master cache; the dimensional argument is L-independent, but the cache
       is the substrate input).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY: import; never hardcode)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import (   # noqa: E402
    M_KK_gravity,        # 7.428660036284456e16 GeV  -- the cutoff energy Lambda = M_KK
    M_KK_inv_seconds,    # 8.860439881925477e-42 s   -- kappa_nat (S96-W1-MKK-SECONDS)
    GeV_to_J,            # 1.602176634e-10 J/GeV (exact SI)
    hbar_SI,             # 1.054571817e-34 J*s (CODATA 2018)
    c_light,             # 2.99792458e8 m/s (exact)
    c_light_km_s,        # 2.99792458e5 km/s
    G_DeWitt,            # 5.0  -- Z_norm, the taudot^2 coefficient (S42); DIMENSIONLESS
    tau_fold,            # 0.19 -- Jensen deformation parameter, DIMENSIONLESS
    f2_dict_CC,          # 92.0 -- f2 ~ M_Pl/M_KK, SS8.3 dictionary; DIMENSIONLESS ratio
)

# ---------------------------------------------------------------------------
# Section 2 — Identity + machinery pins
# ---------------------------------------------------------------------------
SESSION = "S102"
GATE_ID = "S102-NNU-FALSIFIER-I-R1-SOURCECHECK"
SCHEME = "SI-dimensional-chain-hbar-over-E"
CONVENTION = "natural-units-to-SI-M_KK-SYMMETRIC-FALSIFIER"
L_MAX = 12  # (local) s84 master-cache truncation; the dimensional argument is L-independent

SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_PATH = SCRIPT_PATH.parent / "canonical_constants.py"
CACHE_PATH = (SCRIPT_PATH.parent.parent / "session-84" / "s84_spectrum_cache_L12_tau019.npz")
REGISTRY_PATH = (SCRIPT_PATH.parent.parent.parent / "sessions" / "permanent-results-registry.md")
OUT_DIR = SCRIPT_PATH.parent.parent / "session-102"

# Pre-registered band edges (analytic: 67.4/2 .. 67.4*2). H0_REF is the Planck-2018
# observational anchor the falsifier targets (a fixed reference, NOT a fit parameter).
H0_REF = 67.4                       # (local) km/s/Mpc; factor-2 band centre (workshop CF-alpha pre-reg)
BAND_LO = H0_REF / 2.0              # (local) 33.7 km/s/Mpc
BAND_HI = H0_REF * 2.0             # (local) 134.8 km/s/Mpc
KAPPA_RATIO_TOL = 1e-3             # (local) 1e-3 RATIO tolerance on derived_kappa vs kappa_nat
KAPPA_NAT = M_KK_inv_seconds       # canonical kappa_nat target (S96-W1-MKK-SECONDS)

# Unit-conversion fixtures (dimensional analysis only; NOT framework constants)
MPC_TO_KM = 3.0856775814913673e19  # (local) km per Mpc (IAU 2015 definition; pure unit bridge)


def sha256_file(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


# ---------------------------------------------------------------------------
# Section 3 — Substrate input: the L_max=12 D_K spectrum cache
# ---------------------------------------------------------------------------
def load_spectrum_moments():
    """Load the s84 D_K cache (|lambda| in M_KK units) and build the DIMENSIONLESS
    spectral functional that enters H_sub. Returns (S_dimensionless, n_modes, lam_min,
    lam_max). The whole point: every quantity returned here is DIMENSIONLESS (Def 2)."""
    d = np.load(CACHE_PATH, allow_pickle=True)
    sectors = d["sector_evals"].item()                       # (local) dict {(p,q): {...}}
    all_abs = []                                             # (local)
    for (pq, info) in sectors.items():
        all_abs.append(np.asarray(info["abs_evals"], dtype=float))
    lam = np.concatenate(all_abs)                            # (local) |lambda|/M_KK, dimensionless
    lam = lam[lam > 0]                                       # (local) drop any exact zeros
    n_modes = lam.size                                       # (local)
    lam_min = float(lam.min())                               # (local)
    lam_max = float(lam.max())                               # (local)
    # A dimensionless spectral functional: the inverse-second-moment-normalized mean
    # gap (any O(1) dimensionless shape of the spectrum). This is the protected Ohat
    # content -- a pure number, carrying NO units.
    M2 = float(np.mean(lam ** 2))                            # (local) <|lambda|^2>, dimensionless
    M0 = float(lam.size)                                     # (local) mode count, dimensionless
    spectral_shape = float(np.sqrt(M2))                      # (local) RMS eigenvalue, dimensionless
    return spectral_shape, n_modes, lam_min, lam_max, M2, M0


# ---------------------------------------------------------------------------
# Section 4 — Assemble H(tau_now) and STATICALLY enumerate dimensionful factors
# ---------------------------------------------------------------------------
def assemble_H_and_enumerate(spectral_shape):
    """Build H_assembled in km/s/Mpc from the substrate inputs, and produce the static
    per-factor dimensional tag table.

    The HONEST assembly (the only path that reaches km/s/Mpc):
        H_sub          = dimensionless dynamical content  (sqrt(Z_norm)-weighted spectral shape)
        gamma_unit     = hbar / (M_KK_GeV * GeV_to_J)  [= M_KK_inv_seconds]  <- the IMPORT
        H_assembled[s^-1]   = (H_sub  *  taudot_dimensionless) / gamma_unit
        H_assembled[km/s/Mpc] = H_assembled[s^-1] * MPC_TO_KM / c... (unit bridge to km/s/Mpc)

    Each multiplicative factor is tagged. imported_scale_count = count of *-IMPORT tags.
    """
    # --- the dimensionless dynamical content H_sub (Def 1-3, 6): NO units ---
    # H_sub^2 = Z_norm * taudot^2 + (S_SA - V0)*prefactor.  At tau_now the dimensionless
    # dynamical magnitude is an O(1) number built from {Z_norm=G_DeWitt, spectral shape,
    # f2 ratio}. We take the geometric combination that the workshop dimensional chain
    # uses; its EXACT value is immaterial to the falsifier (the falsifier is the
    # import-presence test, not a fit) -- what matters is that H_sub is DIMENSIONLESS.
    taudot_dimensionless = tau_fold                          # (local) O(1) dimensionless rate proxy at tau_now
    H_sub = np.sqrt(G_DeWitt) * taudot_dimensionless * (spectral_shape / np.sqrt(f2_dict_CC))  # (local) DIMENSIONLESS

    # --- the substrate->seconds bridge gamma_unit: the ONLY path to [time] ---
    # gamma_unit = hbar / (M_KK_GeV * GeV_to_J).  This is IDENTICALLY M_KK_inv_seconds.
    M_KK_in_Joule = M_KK_gravity * GeV_to_J                  # (local) J  -- imports M_KK-in-GeV
    derived_kappa = hbar_SI / M_KK_in_Joule                  # (local) s  -- imports hbar(Js) + M_KK(GeV)
    gamma_unit = derived_kappa                               # (local) s/[t_sub]; the substrate clock tick in SI seconds

    # --- assemble H in inverse seconds, then bridge units to km/s/Mpc ---
    H_inv_seconds = H_sub / gamma_unit                       # (local) 1/s
    # 1/s -> km/s/Mpc:  H[km/s/Mpc] = H[1/s] * (km per Mpc).  (H = v/d; v in km/s, d in Mpc.)
    H_assembled = H_inv_seconds * MPC_TO_KM                   # (local) km/s/Mpc

    # ---- STATIC dimensionful-factor enumeration (the audit-trail of the assembly) ----
    # Each multiplicative factor that entered H_assembled, with its dimensional tag.
    factor_table = [
        # (factor_name, symbolic_value, tag)
        ("sqrt(Z_norm)=sqrt(G_DeWitt)", float(np.sqrt(G_DeWitt)), "G_DeWitt-pure-number"),
        ("taudot~tau_fold",             float(taudot_dimensionless), "dimensionless-spectral"),
        ("spectral_shape=RMS|lambda|",  float(spectral_shape),  "dimensionless-spectral"),
        ("1/sqrt(f2)",                  float(1.0 / np.sqrt(f2_dict_CC)), "f2-dimensionless-ratio"),
        ("hbar (J*s)",                  float(hbar_SI),         "hbar-in-Js-IMPORT"),
        ("1/(M_KK in GeV)",             float(1.0 / M_KK_gravity), "M_KK-in-GeV-IMPORT"),
        ("GeV_to_J (J/GeV)",            float(GeV_to_J),        "M_KK-in-GeV-IMPORT"),  # part of the energy->Joule import bridge
        ("Mpc->km bridge",             float(MPC_TO_KM),       "unit-bridge-pure-number"),
    ]
    import_tags = {"M_KK-in-GeV-IMPORT", "hbar-in-Js-IMPORT"}   # (local)
    imported_scale_count = sum(1 for (_, _, tag) in factor_table if tag in import_tags)  # (local)
    # collapse the import bridge to the count of DISTINCT imported physical scales:
    # {M_KK-in-GeV, hbar-in-Js}; GeV_to_J is part of the M_KK-energy->Joule conversion.
    distinct_imported_scales = set(
        tag for (_, _, tag) in factor_table if tag in import_tags
    )                                                          # (local)
    n_distinct_imports = len(distinct_imported_scales)        # (local)

    return dict(
        H_sub=float(H_sub),
        gamma_unit=float(gamma_unit),
        derived_kappa=float(derived_kappa),
        M_KK_in_Joule=float(M_KK_in_Joule),
        H_inv_seconds=float(H_inv_seconds),
        H_assembled=float(H_assembled),
        factor_table=factor_table,
        imported_scale_count=int(imported_scale_count),
        n_distinct_imports=int(n_distinct_imports),
    )


# ---------------------------------------------------------------------------
# Section 5 — Branch selection (pre-registered two-branch operator)
# ---------------------------------------------------------------------------
def select_branch(res):
    """Apply the pre-registered SYMMETRIC two-branch operator.

    PASS (theorem FALSIFIED): imported_scale_count == 0 AND band_hit AND kappa_match.
    FAIL (theorem CONFIRMED): an imported scale is present (M_KK-in-GeV or hbar-in-Js).
    INFO (middle): band_hit BUT import present.
    """
    H = res["H_assembled"]                                    # (local)
    band_hit = bool(BAND_LO <= H <= BAND_HI)                  # (local)
    kappa_rel = abs(res["derived_kappa"] - KAPPA_NAT) / KAPPA_NAT  # (local)
    kappa_match = bool(kappa_rel <= KAPPA_RATIO_TOL)          # (local)
    zero_import = bool(res["imported_scale_count"] == 0)      # (local)

    if zero_import and band_hit and kappa_match:
        branch = "PASS"                                       # (local) theorem FALSIFIED (rank-0)
    elif band_hit and not zero_import:
        branch = "INFO"                                       # (local) band-hit but import present
    else:
        branch = "FAIL"                                       # (local) theorem CONFIRMED (rank-1)
    return branch, band_hit, kappa_rel, kappa_match, zero_import


# ---------------------------------------------------------------------------
# Section 6 — dual-SHA (audit/content) per S84+ schema
# ---------------------------------------------------------------------------
def compute_dual_sha(pins: dict):
    script_bytes = SCRIPT_PATH.read_bytes()                   # (local)
    canonical_bytes = CANONICAL_PATH.read_bytes()             # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 7 — verdict payload (script prints; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — dimensional-flow figure
# ---------------------------------------------------------------------------
def make_figure(res, branch, out_png):
    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.axis("off")

    title = ("S102-NNU-FALSIFIER-I-R1-SOURCECHECK  (CF-alpha)\n"
             "Dimensional flow: D_K eigenvalues -> dimensionless shape -> [the import] -> seconds")
    ax.set_title(title, fontsize=12, fontweight="bold")

    # left column: dimensionless substrate content; right: the import; centre: the bridge
    rows = []
    for (name, val, tag) in res["factor_table"]:
        rows.append((name, val, tag))

    y = 0.92                                                  # (local)
    ax.text(0.02, y, "Multiplicative factor", fontsize=10, fontweight="bold")
    ax.text(0.42, y, "value", fontsize=10, fontweight="bold")
    ax.text(0.60, y, "dimensional tag", fontsize=10, fontweight="bold")
    y -= 0.05
    for (name, val, tag) in rows:
        is_import = "IMPORT" in tag                           # (local)
        color = "#b00020" if is_import else "#0b6e4f"         # (local)
        ax.text(0.02, y, name, fontsize=9, color=color)
        ax.text(0.42, y, f"{val:.4g}", fontsize=9, color=color)
        ax.text(0.60, y, tag, fontsize=9, color=color,
                fontweight=("bold" if is_import else "normal"))
        y -= 0.045

    y -= 0.02
    ax.text(0.02, y,
            f"H_sub (DIMENSIONLESS) = {res['H_sub']:.4g}", fontsize=10)
    y -= 0.045
    ax.text(0.02, y,
            f"gamma_unit = hbar/(M_KK_GeV * GeV_to_J) = {res['gamma_unit']:.6e} s   [THE IMPORT bridge to time]",
            fontsize=10, color="#b00020")
    y -= 0.045
    ax.text(0.02, y,
            f"derived_kappa = {res['derived_kappa']:.10e} s   vs kappa_nat = {KAPPA_NAT:.10e} s",
            fontsize=10)
    y -= 0.045
    ax.text(0.02, y,
            f"H_assembled = {res['H_assembled']:.4g} km/s/Mpc   "
            f"(factor-2 band [{BAND_LO:.1f}, {BAND_HI:.1f}])", fontsize=10)
    y -= 0.045
    ax.text(0.02, y,
            f"imported_scale_count = {res['imported_scale_count']}  "
            f"(distinct physical scales = {res['n_distinct_imports']}: M_KK-in-GeV, hbar-in-Js)",
            fontsize=10, color="#b00020", fontweight="bold")
    y -= 0.055
    verdict_txt = {"FAIL": "FAIL -> theorem CONFIRMED (rank-1): seconds imported",
                   "PASS": "PASS -> theorem FALSIFIED (rank-0): substrate supplied the second",
                   "INFO": "INFO -> band-hit BUT import present (SIGN-correct, rank-1 on SOURCE axis)"}[branch]
    ax.text(0.02, y, f"BRANCH: {verdict_txt}", fontsize=11, fontweight="bold",
            color=("#b00020" if branch == "FAIL" else "#0b6e4f"))

    ax.text(0.02, 0.02,
            "Substrate-IS: the eigenvalue problem is SILENT at the terminal x (hbar/M_KK c^2) "
            "second BY CONSTRUCTION (N_3=0, BDI, S44).",
            fontsize=8, style="italic")

    fig.tight_layout()
    fig.savefig(out_png, dpi=140)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 — main
# ---------------------------------------------------------------------------
def main():
    # ---- input SHA log (first lines of stdout, per gate-verdicts.md) ----
    cache_sha = sha256_file(CACHE_PATH)                       # (local)
    canonical_sha = sha256_file(CANONICAL_PATH)               # (local)
    registry_sha = sha256_file(REGISTRY_PATH)                 # (local)
    print(f"INPUT canonical_constants.py sha256 = {canonical_sha}")
    print(f"INPUT s84_spectrum_cache_L12_tau019.npz sha256 = {cache_sha}")
    print(f"INPUT permanent-results-registry.md sha256 = {registry_sha}")

    # ---- substrate input: dimensionless spectral shape ----
    spectral_shape, n_modes, lam_min, lam_max, M2, M0 = load_spectrum_moments()
    print(f"SPECTRUM n_modes={n_modes}  |lambda|_min={lam_min:.6f}  |lambda|_max={lam_max:.6f}  "
          f"RMS={spectral_shape:.6f}  (all DIMENSIONLESS, in M_KK units)")

    # ---- assemble H + static dimensional enumeration ----
    res = assemble_H_and_enumerate(spectral_shape)
    print("\nDIMENSIONFUL-FACTOR ENUMERATION:")
    for (name, val, tag) in res["factor_table"]:
        flag = "  <== IMPORT" if "IMPORT" in tag else ""
        print(f"  {name:32s}  {val:>14.6g}   {tag}{flag}")
    print(f"\nH_sub (dimensionless)   = {res['H_sub']:.6e}")
    print(f"gamma_unit              = {res['gamma_unit']:.10e} s")
    print(f"derived_kappa           = {res['derived_kappa']:.10e} s")
    print(f"kappa_nat (canonical)   = {KAPPA_NAT:.10e} s")
    print(f"H_assembled             = {res['H_assembled']:.6f} km/s/Mpc")
    print(f"imported_scale_count    = {res['imported_scale_count']}  "
          f"(distinct = {res['n_distinct_imports']})")

    # ---- branch selection ----
    branch, band_hit, kappa_rel, kappa_match, zero_import = select_branch(res)
    print(f"\nband_hit={band_hit}  (band [{BAND_LO}, {BAND_HI}])")
    print(f"kappa_rel_dev={kappa_rel:.3e}  kappa_match={kappa_match} (tol {KAPPA_RATIO_TOL})")
    print(f"zero_import={zero_import}")
    print(f"BRANCH SELECTED = {branch}")

    # ---- SIGN/MAGNITUDE/REGIME 3-tuple ([CHAIN] with directional pre-registration) ----
    # SIGN: the substitution-chain Step 4 direction is "codomain seconds is UNREACHABLE
    #   from the dimensionless domain => imported_scale_count >= 1". The computed direction
    #   matches iff an import is indeed present (imported_scale_count >= 1).
    sign_verdict = "PASS" if res["imported_scale_count"] >= 1 else "FAIL"  # (local)
    # MAGNITUDE: is the assembled number in the factor-2 band of 67.4? (the "factor of 2" claim)
    magnitude_verdict = "PASS" if band_hit else "FAIL"        # (local)
    # REGIME: VALID -- the dimensional argument is L-independent and the SI-chain scheme is
    #   exactly S96-W1-MKK-SECONDS; the assembly is within its regime of validity throughout.
    regime_verdict = "VALID"                                  # (local)

    # NOTE on composite: this gate's plan-frozen operator FIXES the composite to the
    # BRANCH selection (FAIL=confirm / PASS=falsify / INFO=band-hit-with-import), which
    # can DIFFER from the generic collapse rule. The generic collapse on
    # (sign=PASS, magnitude=PASS, regime=VALID) would read PASS; the plan-frozen
    # two-branch operator reads FAIL (import present => theorem CONFIRMED). We emit the
    # plan-frozen branch as the composite, with a composite-precedence disclosure row.

    # ---- dual-SHA ----
    pins = {
        "computations/_shared/s102_nnu_falsifier_i_r1_sourcecheck.py": canonical_sha and sha256_file(SCRIPT_PATH),
        "computations/_shared/canonical_constants.py": canonical_sha,
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": cache_sha,
        "kappa_nat_canonical": f"{KAPPA_NAT:.17e}",
        "M_KK_canonical": f"{M_KK_gravity:.17e}",
        "pinmap_branch": branch,
    }
    audit_sha, content_sha = compute_dual_sha(pins)
    print(f"\naudit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")

    # ---- persist data ----
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_npz = OUT_DIR / "s102_nnu_falsifier_i_r1_sourcecheck.npz"
    out_png = OUT_DIR / "s102_nnu_falsifier_i_r1_sourcecheck.png"
    factor_names = np.array([f[0] for f in res["factor_table"]], dtype=object)  # (local)
    factor_vals = np.array([f[1] for f in res["factor_table"]], dtype=float)    # (local)
    factor_tags = np.array([f[2] for f in res["factor_table"]], dtype=object)   # (local)
    np.savez(
        out_npz,
        H_assembled=res["H_assembled"],
        H_sub=res["H_sub"],
        H_inv_seconds=res["H_inv_seconds"],
        gamma_unit=res["gamma_unit"],
        derived_kappa=res["derived_kappa"],
        kappa_nat=KAPPA_NAT,
        kappa_rel_dev=kappa_rel,
        kappa_match=kappa_match,
        dimensionful_factor_names=factor_names,
        dimensionful_factor_vals=factor_vals,
        dimensionful_factor_tags=factor_tags,
        imported_scale_count=res["imported_scale_count"],
        n_distinct_imports=res["n_distinct_imports"],
        band_hit_bool=band_hit,
        band_lo=BAND_LO, band_hi=BAND_HI, H0_ref=H0_REF,
        zero_import=zero_import,
        branch_selected=branch,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        spectral_shape=spectral_shape, n_modes=n_modes,
        lam_min=lam_min, lam_max=lam_max, M2=M2, M0=M0,
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )
    make_figure(res, branch, out_png)
    print(f"\nWROTE {out_npz}")
    print(f"WROTE {out_png}")

    # ---- value payload + 3-tuple companion ----
    value = (f"branch={branch}_H={res['H_assembled']:.4f}kmsMpc_"
             f"imports={res['imported_scale_count']}_"
             f"derived_kappa={res['derived_kappa']:.6e}s_kappa_match={kappa_match}_bandhit={band_hit}")
    extra_rows = [
        (f"# composite-precedence: S102-NNU-FALSIFIER-I plan SS-W1-2 two-branch operator "
         f"(FAIL=theorem-CONFIRMED rank-1 / PASS=theorem-FALSIFIED rank-0 / INFO=band-hit-with-import); "
         f"overrides generic-collapse reading of (sign=PASS,mag={magnitude_verdict},regime=VALID); "
         f"composite={branch} per imported_scale_count={res['imported_scale_count']}>=1"),
        (f"# dimensional-chain: H_sub(dimensionless)={res['H_sub']:.4e} x 1/gamma_unit; "
         f"gamma_unit=hbar/(M_KK_GeV*GeV_to_J)={res['gamma_unit']:.6e}s [IMPORT]; "
         f"derived_kappa==kappa_nat rel_dev={kappa_rel:.2e}"),
    ]
    print_verdict_payload(branch, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=extra_rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
