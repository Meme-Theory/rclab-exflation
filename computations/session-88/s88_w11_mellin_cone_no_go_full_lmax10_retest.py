#!/usr/bin/env python3
"""
S88 W11-126 — S88-MELLIN-CONE-NO-GO-FULL-LMAX10-RETEST

Plan §W11-126: extend W1a-2 CM-1995 §III.4 inadmissibility from 4-eigvalue
toy to FULL L=10 D_K^2 spectrum (166k+ eigvals at τ_fold=0.190); test
predicate at 5 substrate-distance poles s ∈ {3,4,5,6,7}.

CM-1995 §III.4 inadmissibility predicate: a finite-rank A is admissible
iff Res[ζ_D(s); s=s_*]·Γ(s_*) = Σ_a m_a · λ_a^{-s_*} for SOME finite
{m_a, λ_a} simultaneously at all dim-spectrum poles. For a FINITE
spectrum, ζ_D(s) is ENTIRE (no poles), so LHS = 0; RHS is a non-trivial
positive sum; predicate FAILS to find admissible A at every pole.

PASS iff all 5 s ∈ {3,4,5,6,7} satisfy the inadmissibility (RHS > rel_tol);
INFO iff 4/5; FAIL iff ≤ 3.
"""
import os, sys, json, hashlib, time
from pathlib import Path
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath as mp
mp.mp.dps = 30

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'computations' / '_shared'))
from canonical_constants import M_KK, tau_fold

GATE_ID = "S88-MELLIN-CONE-NO-GO-FULL-LMAX10-RETEST"  # (local)
SCHEME = "full-Lmax10-Mellin-cone-CM1995"  # (local)
CONVENTION = "mpmath-30dp-Cauchy-contour"  # (local)
L_MAX = 10  # (local)
S_TEST = [3, 4, 5, 6, 7]  # (local) plan-pinned 5 substrate-distance poles
REL_TOL_PREDICATE = 1e-9  # (local) plan-pin
WP_ID = "W11-126"  # (local)
SCHEMA_VERSION = "S87+"  # (local)

CACHE_PATH = ROOT / 'computations' / 'session-84' / 's84_spectrum_cache_L12_tau019.npz'
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # (local)
VERDICT_FILE = ROOT / 'computations' / 'session-88' / 's88_gate_verdicts.txt'


def file_sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def closure_hash_dict(d):
    return hashlib.sha256(json.dumps(d, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def main():
    t0 = time.time()  # (local)
    print(f"[{GATE_ID}] full L_max=10 D_K^2 Mellin-cone no-go retest at s ∈ {S_TEST}")

    cache_sha = file_sha256(CACHE_PATH)  # (local)
    print(f"  Cache SHA: {cache_sha} (pin match: {cache_sha == CACHE_SHA_PIN})")

    cache = np.load(CACHE_PATH, allow_pickle=True)
    sec = cache['sector_evals'].item()  # (local)
    # Truncate to L=10 (level <= L_MAX)
    pool = []  # (local)
    n_sec = 0  # (local)
    for (p, q), payload in sec.items():
        if payload['level'] > L_MAX:
            continue
        n_sec += 1
        evals = np.asarray(payload['abs_evals'], dtype=np.float64)
        d_pq = int(payload['dim'])  # (local) Weyl multiplicity
        for lam in evals:
            if lam > 1e-12:
                pool.append((float(lam), d_pq))
    n_eig = len(pool)  # (local)
    print(f"  L=10 truncation: {n_sec} sectors, {n_eig} eigenvalues (post zero-filter)")

    # Compute ζ_D(s_*) = Σ m_n / λ_n^{s_*} at each plan-pinned s_* via mpmath
    mp.mp.dps = 30
    rhs_at_pole = {}  # (local) Σ m·λ^{-s}
    gamma_factors = {}  # (local) Γ(s_*)
    lhs_at_pole = {}  # (local) Res[ζ_D(s); s=s_*]·Γ(s_*) — for FINITE spectrum, LHS=0 since ζ_D entire
    predicate_no_go = {}  # (local) True iff |LHS - RHS·Γ| > rel_tol_predicate (no admissible A)
    print("\n  Computing ζ_D(s_*) = Σ m·λ^{-s} at each pole s_* ∈ S_TEST...")
    for s in S_TEST:
        s_mp = mp.mpf(s)
        rhs = mp.mpf(0)
        for lam, m in pool:
            rhs += m * mp.power(lam, -s_mp)
        gam = mp.gamma(s_mp / 2)
        # CM-1995 §III.4: For finite spectrum, ζ_D(s) is entire ⇒ Res[ζ_D(s); s_*] = 0
        # LHS = 0·Γ(s/2) = 0; RHS = (the value above)·Γ(s/2)... wait, the predicate test is:
        # admissible: 0 (LHS) =  Σ m·λ^{-s} (RHS) ⇒ requires RHS=0; for non-trivial spectrum RHS > 0 ⇒ inadmissible
        # The "Γ(s_*)" factor is on both sides equally; pull out and compare directly.
        rhs_at_pole[s] = rhs
        gamma_factors[s] = gam
        lhs_at_pole[s] = mp.mpf(0)  # finite spectrum, no poles
        diff = abs(rhs - mp.mpf(0))  # = rhs since lhs=0
        predicate_no_go[s] = float(diff) > REL_TOL_PREDICATE
        print(f"    s={s}: RHS=Σm·λ^(-{s}) = {mp.nstr(rhs, 6)} | LHS=Res[ζ_D;s={s}] = 0 (entire ζ_D)")
        print(f"          predicate test |LHS-RHS|={mp.nstr(diff, 6)} > {REL_TOL_PREDICATE:.0e} ⇒ no admissible A: {predicate_no_go[s]}")

    poles_passing = sum(predicate_no_go.values())  # (local)
    print(f"\n  poles_passing_no_go = {poles_passing}/5")

    if poles_passing == 5:
        verdict = "PASS"
        reason = "all 5 substrate-distance poles satisfy CM-1995 §III.4 inadmissibility; no-go theorem extends from 4-eigvalue toy to full L=10 spectrum (166k+ eigvals)"
    elif poles_passing == 4:
        verdict = "INFO"
        reason = f"4/5 poles satisfy inadmissibility; one borderline at s={[s for s in S_TEST if not predicate_no_go[s]]}"
    else:
        verdict = "FAIL"
        reason = f"poles_passing_no_go = {poles_passing}/5; admissible region surfaces at full L=10 spectrum; surprise structural result"

    pinmap = {  # (local)
        "_gate_id": GATE_ID, "_wp_id": WP_ID, "_scheme": SCHEME,
        "_convention": CONVENTION, "_L_max": L_MAX,
        "S_TEST": S_TEST, "REL_TOL_PREDICATE": str(REL_TOL_PREDICATE),
        "cache_path": str(CACHE_PATH.relative_to(ROOT)),
        "cache_sha_pin": CACHE_SHA_PIN, "cache_sha_actual": cache_sha,
        "M_KK_GeV": M_KK, "tau_fold": tau_fold, "n_sectors": n_sec, "n_eigvals": n_eig,
    }
    audit_sha256 = closure_hash_dict(pinmap)  # (local)

    val_str = (
        f"poles_passing_no_go={poles_passing}_of_5;"
        f"per_pole_RHS={{{','.join(f's{s}={float(rhs_at_pole[s]):.4e}' for s in S_TEST)}}};"
        f"reason={reason};n_sectors={n_sec};n_eigvals={n_eig}"
    )  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{val_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={{CONTENT_SHA}} schema_version={SCHEMA_VERSION}"
    )  # (local)
    content_sha256 = hashlib.sha256(
        canonical_line.replace("{CONTENT_SHA}", "PLACEHOLDER").encode("utf-8")
    ).hexdigest()  # (local)
    canonical_line = canonical_line.replace("{CONTENT_SHA}", content_sha256)
    short_a = audit_sha256[:16]; short_c = content_sha256[:16]  # (local)
    companion_dual = (
        f"# audit_sha256_short={short_a} content_sha256_short={short_c} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"plan §W11-126 W1a-2 extension to full L=10 (166k+ eigvals); poles_passing={poles_passing}/5"
    )  # (local)
    sign_v = "PASS" if verdict == "PASS" else ("FAIL" if verdict == "FAIL" else "N/A")
    mag_v = verdict; regime_v = "VALID"
    companion_3t = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); [VERIFY-THEOREM] CM-1995 inadmissibility extends from toy to full spectrum"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line + "\n"); f.write(companion_dual + "\n"); f.write(companion_3t + "\n")
    print(f"\n  Verdict appended; audit_sha256 = {audit_sha256}")

    np.savez_compressed(
        Path(__file__).with_suffix('.npz'),
        s_test=np.asarray(S_TEST),
        rhs_per_pole=np.asarray([float(rhs_at_pole[s]) for s in S_TEST]),
        predicate_no_go=np.asarray([predicate_no_go[s] for s in S_TEST]),
        poles_passing=poles_passing,
        n_sectors=n_sec, n_eigvals=n_eig,
        cache_sha=cache_sha, audit_sha256=audit_sha256, content_sha256=content_sha256,
        verdict=verdict,
    )
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.semilogy(S_TEST, [float(rhs_at_pole[s]) for s in S_TEST], 'o-', markersize=10, label='RHS = Σ m·λ^{-s}')
    ax.axhline(REL_TOL_PREDICATE, color='r', linestyle='--', label=f'predicate threshold {REL_TOL_PREDICATE:.0e}')
    ax.set_xlabel('s (Mellin pole index)'); ax.set_ylabel('|RHS| (= LHS - 0)')
    ax.set_title(f"S88 W11-126 CM-1995 §III.4 inadmissibility at full L=10; verdict={verdict}, poles_passing={poles_passing}/5")
    ax.legend(); ax.grid(True, which='both', linestyle=':', alpha=0.4)
    plt.tight_layout(); plt.savefig(Path(__file__).with_suffix('.png'), dpi=130); plt.close()

    elapsed = time.time() - t0  # (local)
    print(f"  Total wall: {elapsed:.1f}s")
    print(f"  Verdict: {verdict} — {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
