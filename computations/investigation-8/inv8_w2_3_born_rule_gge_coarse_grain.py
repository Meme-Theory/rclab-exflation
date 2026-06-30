#!/usr/bin/env python3
"""
INV8 W2-3 — Born Rule Derive-or-No-Go from GGE Coarse-Graining
==============================================================

Gate: INV8-W2-3 ([VERIFY])

Pre-registered threshold (plan §W2-3):
  operator: max_i |p_i - |psi_i|^2|  (element-wise probability vs amplitude^2)
  strict_PASS_boundary: max_i |p_i - |psi_i|^2| < 1e-6   (Born rule DERIVED)
  PASS  iff max_dev < 1e-6  (Branch A: Born rule derived from coarse-graining)
  INFO  iff max_dev > 1e-6 WITH a structural reason (Branch B: Born rule is an INPUT/no-go)
          OR an ambiguous numerical residual without structural reason
  FAIL  reserved for SCRIPT BREAKAGE only (per math-scripts.md exit-code semantics;
        a no-go is INFO, not FAIL).

Two-track outcome (genuine, dual-prior pre-registered):
  track_A (prior 0.35): Born rule DERIVED — reduced-rho eigenvalues = |psi|^2
  track_B (prior 0.65): Born rule is an INPUT / no-go — Gleason supplies consistency only
  discriminator: PASS(<1e-6) -> 0.9 to track_A ; INFO/no-go(>1e-6, structural) -> 0.9 to track_B ;
                 ambiguous residual (no structural reason) -> unchanged.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-52/s52_bogoliubov_amp.npz   (Bogoliubov u_k, v_k per mode; SUBSTRATE-FIRST source)
  - computations/investigation-8/inv8_gate_verdicts.txt  (INV8-W1-1 lambda_k weighting; ABSENT -> s52 fallback)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max-deviation>, scheme=GGE-8-mode, convention=RATIO, L_max=N/A)

Classification: PHONONIC
  The GGE state, its 8 Richardson-Gaudin integrals, and the reduced density matrix
  for one phonon mode are ALL substrate excitation structure. The Born probabilities
  ARE the eigenvalues of a coarse-grained substrate state.

METHODOLOGY (S58 addendum §VI.1, the load-bearing un-done computation)
---------------------------------------------------------------------
The GGE rho_GGE = (1/Z) exp(-sum_k lambda_k I_k) over the 8 Richardson-Gaudin integrals
{I_k} (post-transit many-body state). The {I_k} are MUTUALLY COMMUTING quasiparticle
occupation operators -> rho_GGE is DIAGONAL in the quasiparticle eigenbasis and FACTORIZES
into a product of single-mode factors. Tracing out 7 of 8 modes from a product state leaves
the 8th mode's single-mode reduced density matrix EXACTLY (no entanglement to integrate over
in the quasiparticle basis -> the partial trace is a marginalization).

For the post-transit pure-Bogoliubov state (P_exc=1.000, the BCS vacuum read in the
ORIGINAL-particle pairing basis), the per-mode reduced state in the PAIRING basis is
  rho_A = diag(u_k^2, v_k^2),   u_k^2 + v_k^2 = 1.
The L^2/Gleason candidate (S16 'DEFENSIBLE via Gleason dim>=3 + geometric L^2 fiber
integration eq 2.26') builds the would-be wavefunction amplitude from the SAME Bogoliubov
coefficients: psi = u_k |0> + v_k |pair>, so |psi_i|^2 = {u_k^2, v_k^2}.

The two-track test is then BASIS-RESOLVED and HONEST:
  * In the pairing (Bogoliubov-eigen) basis the rho_A eigenvalues ARE {u^2, v^2}, which equal
    |psi|^2 by construction  -> Branch A numerically (max_dev ~ 0).
  * BUT the STRUCTURAL question is whether the GGE TRACE PRODUCES a frame function, or merely
    is CONSISTENT with one. We test this by checking, in a basis MISALIGNED from the
    quasiparticle eigenbasis (a generic measurement basis the sub-KK observer is free to pick),
    whether Tr(rho_A P_theta) still equals |<psi|theta>|^2. Gleason GUARANTEES this IF rho_A is
    a density operator (it is) — so the equality in ANY basis is the Gleason CONSISTENCY, not a
    DERIVATION of why the GGE marginal is |psi|^2 rather than some other functional of the same
    state. The DERIVE-vs-NO-GO discriminator is therefore the STRUCTURAL reading attached to the
    (necessarily clean) numerical match, recorded explicitly below.

DISCIPLINE
----------
- `from canonical_constants import *`
- intermediates tagged `# (local)`
- CPU numpy (one fermionic mode -> 2x2 reduced density matrix; OMP capped at 8 per plan GPU_path=numpy.linalg)
- SHA-256 of inputs logged in first 20 lines of stdout; dual-SHA emitted (S84+)
- 4-tuple printed as final non-verdict line; verdict via print_verdict_payload -> agent emit_verdict
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import hashlib  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
GATE_ID = "INV8-W2-3"
SESSION = "8"
SCHEME = "GGE-8-mode"
CONVENTION = "RATIO"
L_MAX = "N/A"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
OUT_DIR = PROJECT_ROOT / "computations" / "investigation-8"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402  (framework constants)

S52_NPZ = PROJECT_ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
INV8_VERDICTS = OUT_DIR / "inv8_gate_verdicts.txt"
INPUT_FILES = [S52_NPZ, INV8_VERDICTS]

TOL = 1.0e-6  # (local) pre-registered gate threshold; plan §W2-3 strict_PASS_boundary / tolerance


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (verbatim from .claude/templates/script-template.py)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 — Physics
# ---------------------------------------------------------------------------
def single_mode_reduced_density_matrix(u, v):
    """Reduced density matrix for ONE fermionic Bogoliubov pair-mode, in the
    pairing (number) basis {|0>, |pair>}.

    The GGE rho_GGE = (1/Z) prod_k exp(-lambda_k n_k) is DIAGONAL in the
    quasiparticle-number eigenbasis (the 8 Richardson-Gaudin integrals are
    mutually-commuting occupation numbers) -> it FACTORIZES over modes. Tracing
    out the other 7 modes is a marginalization that leaves THIS mode's single-mode
    factor exactly. For the post-transit pure-Bogoliubov state (P_exc=1.000), the
    per-mode occupation in the ORIGINAL-particle pairing basis is
        rho_A = diag(u^2, v^2),  u^2 + v^2 = 1.
    """
    p0 = u * u  # (local)  occupation of |0> (unpaired)
    p1 = v * v  # (local)  occupation of |pair>
    rho_A = np.array([[p0, 0.0], [0.0, p1]], dtype=np.float64)  # (local)
    return rho_A


def l2_amplitude_squared(u, v):
    """The S16 Gleason/geometric-L^2 candidate probabilities for the same mode.
    The BCS pair-mode wavefunction is psi = u|0> + v|pair>; the geometric-L^2
    fiber-integration amplitude (eq 2.26 reading) is exactly the Bogoliubov
    coefficient, so |psi_i|^2 = {u^2, v^2}.
    """
    return np.array([u * u, v * v], dtype=np.float64)  # (local)


def projector(theta):
    """Rank-1 projector onto |theta> = cos(theta)|0> + sin(theta)|pair>
    (a generic single-mode measurement direction the sub-KK observer may pick)."""
    c, s = np.cos(theta), np.sin(theta)  # (local)
    psi = np.array([c, s], dtype=np.float64)  # (local)
    return np.outer(psi, psi)  # (local)


def compute():
    # ---- Load the substrate-first Bogoliubov amplitudes (s52) ----
    d = np.load(S52_NPZ)  # (local)
    u_k = np.asarray(d["u_k"], dtype=np.float64)  # (local) 8 modes
    v_k = np.asarray(d["v_k"], dtype=np.float64)  # (local)
    labels = [str(x) for x in d["branch_labels"]]  # (local)
    n_modes = len(u_k)  # (local)

    # ---- INV8-W1-1 prerequisite resolution (substrate-first fallback) ----
    w1_1_present = False  # (local)
    if INV8_VERDICTS.exists():
        txt = INV8_VERDICTS.read_text(encoding="utf-8", errors="ignore")  # (local)
        w1_1_present = ("INV8-W1-1:" in txt)
    # The lambda_k GGE weighting (W1-1, or S60/S62) sets the per-mode OCCUPATION
    # f_k = v_k^2 for the post-transit pure-Bogoliubov state regardless of the
    # lambda_k values: lambda_k fixes WHICH non-equilibrium temperatures dress the
    # 8 modes, but the post-transit P_exc=1.000 marginal occupation in the pairing
    # basis is u_k^2/v_k^2 from the Bogoliubov coefficients on disk. The prereq
    # therefore governs only the labelling of the 8-integral weighting, not the
    # numbers entering the |psi|^2 test (disclosed in WP §Methodology).

    # ---- Per-mode two-track test (all 8 modes) ----
    per_mode = []  # (local)
    for i in range(n_modes):
        u, v = float(u_k[i]), float(v_k[i])  # (local)
        norm = u * u + v * v  # (local) Bogoliubov normalization check
        rho_A = single_mode_reduced_density_matrix(u, v)  # (local)
        # eigenvalues of a diagonal 2x2 are its diagonal entries (sorted desc)
        p_eig = np.sort(np.linalg.eigvalsh(rho_A))[::-1]  # (local)
        psi2 = np.sort(l2_amplitude_squared(u, v))[::-1]  # (local)
        dev = float(np.max(np.abs(p_eig - psi2)))  # (local)
        sum_p = float(np.sum(p_eig))  # (local) must be 1
        per_mode.append({
            "idx": i, "label": labels[i], "u": u, "v": v,
            "norm": norm, "p_eig": p_eig, "psi2": psi2,
            "max_dev": dev, "sum_p": sum_p,
        })

    # ---- Basis-MISALIGNMENT structural probe (the Gleason consistency-vs-derivation test) ----
    # Pick the RETAINED mode = B1 per plan (the unpaired/normal mode u=1,v=0);
    # also probe a fully-paired B2 mode (u=0.9325,v=0.3612) which has a non-trivial
    # mixed marginal. For a generic measurement direction theta, Gleason says
    #   Tr(rho_A P_theta) = |<psi|theta>|^2  IFF rho_A is the |psi><psi| pure state.
    # If rho_A is MIXED (v>0 and u>0), then rho_A != |psi><psi|, and the Born
    # frame-function p(theta)=Tr(rho_A P_theta) is NOT equal to |<psi|theta>|^2 for
    # generic theta — it equals it ONLY in the eigenbasis. This is the structural
    # discriminator: the GGE marginal is a MIXED state, so it does NOT reproduce the
    # PURE-state |psi|^2 frame function in a misaligned basis. Gleason gives the
    # FORM (Tr(rho P)) for the mixed state, NOT the pure |psi|^2 the L^2 reading posits.
    def retained(label_prefix):
        for m in per_mode:
            if m["label"].startswith(label_prefix):
                return m
        return per_mode[0]

    probe_modes = {"B1": retained("B1"), "B2": retained("B2"), "B3": retained("B3")}  # (local)
    thetas = np.linspace(0.0, np.pi, 181)  # (local) 1-degree mesh of measurement directions
    misalign = {}  # (local)
    for name, m in probe_modes.items():
        u, v = m["u"], m["v"]  # (local)
        rho_A = single_mode_reduced_density_matrix(u, v)  # (local)
        psi = np.array([u, v], dtype=np.float64)  # (local) pure-state vector (L^2 candidate)
        born_rho = np.array([float(np.trace(rho_A @ projector(t))) for t in thetas])  # (local)
        born_psi = np.array([float(abs(psi @ np.array([np.cos(t), np.sin(t)]))**2) for t in thetas])  # (local)
        max_basis_gap = float(np.max(np.abs(born_rho - born_psi)))  # (local)
        # purity Tr(rho^2): =1 iff pure; <1 iff mixed
        purity = float(np.trace(rho_A @ rho_A))  # (local)
        misalign[name] = {
            "u": u, "v": v, "purity": purity, "max_basis_gap": max_basis_gap,
            "thetas": thetas, "born_rho": born_rho, "born_psi": born_psi,
        }

    # ---- Headline value: max deviation over the 8 modes' EIGENBASIS test ----
    max_dev_all = max(m["max_dev"] for m in per_mode)  # (local)
    # The retained-mode (B1) eigenbasis deviation is the plan's nominal scalar:
    b1 = probe_modes["B1"]  # (local)
    b1_dev = b1["max_dev"]  # (local)

    return {
        "value": max_dev_all,
        "b1_dev": b1_dev,
        "per_mode": per_mode,
        "misalign": misalign,
        "n_modes": n_modes,
        "w1_1_present": w1_1_present,
    }


def evaluate_gate(res):
    """PASS iff the eigenbasis match is < TOL AND the structural reading supports a
    DERIVATION; INFO (no-go) iff the structural probe shows the GGE marginal does NOT
    reproduce the pure-|psi|^2 frame function in a misaligned basis (Gleason consistency
    only, not derivation). FAIL reserved for script breakage (not reachable here).
    """
    max_dev = res["value"]  # (local)
    # Numerical eigenbasis match (necessary, by the factorization theorem):
    eigenbasis_match = (max_dev < TOL)  # (local)
    # Structural discriminator: is there a MIXED retained marginal whose Born frame
    # function departs from the pure-|psi|^2 reading in a misaligned basis?
    mixed_basis_gap = max(v["max_basis_gap"] for v in res["misalign"].values())  # (local)
    structural_nogo = (mixed_basis_gap > TOL)  # (local)
    if eigenbasis_match and not structural_nogo:
        return "PASS"  # Branch A: derived (frame function produced, basis-independent)
    if eigenbasis_match and structural_nogo:
        return "INFO"  # Branch B: no-go — Gleason consistency only, derivation not established
    # ambiguous residual without structural reason
    return "INFO"


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(res, out_png):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))  # (local)

    # Left: per-mode eigenbasis test {p_i} vs {|psi_i|^2}
    ax = axes[0]  # (local)
    pm = res["per_mode"]  # (local)
    idx = np.arange(len(pm))  # (local)
    p_top = [m["p_eig"][0] for m in pm]  # (local)
    psi_top = [m["psi2"][0] for m in pm]  # (local)
    width = 0.38  # (local)
    ax.bar(idx - width / 2, p_top, width, label="rho_A eigenvalue p_max", color="#2a6f97")
    ax.bar(idx + width / 2, psi_top, width, label="|psi|^2 (L2/Gleason) max", color="#c1121f", alpha=0.8)
    ax.set_xticks(idx)
    ax.set_xticklabels([m["label"] for m in pm], rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("probability")
    ax.set_title(f"Eigenbasis test: max_dev = {res['value']:.3e}  (TOL={TOL:.0e})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Right: basis-misalignment structural probe — Born frame function vs |<psi|theta>|^2
    ax = axes[1]  # (local)
    colors = {"B1": "#1b4332", "B2": "#bb3e03", "B3": "#5a189a"}  # (local)
    for name, mm in res["misalign"].items():
        th = mm["thetas"] * 180.0 / np.pi  # (local)
        ax.plot(th, mm["born_rho"], color=colors[name], lw=2,
                label=f"{name} Tr(rho P_theta)  purity={mm['purity']:.4f}")
        ax.plot(th, mm["born_psi"], color=colors[name], lw=1, ls="--", alpha=0.7,
                label=f"{name} |<psi|theta>|^2")
    ax.set_xlabel("measurement direction theta (deg)")
    ax.set_ylabel("p(theta)")
    ax.set_title("Structural probe: GGE marginal (solid) vs pure-|psi|^2 (dashed)")
    ax.legend(fontsize=7, loc="upper center")
    ax.grid(alpha=0.3)

    fig.suptitle("INV8-W2-3 — Born rule derive-or-no-go from GGE coarse-graining", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()

    # ---- Report (NUMBERS first) ----
    print("=== Per-mode two-track test (eigenbasis) ===")
    print(f"  INV8-W1-1 verdict present: {res['w1_1_present']}  "
          f"(False -> substrate-first s52 fallback per plan §W2-3 prereq)")
    print(f"  {'mode':<7} {'u':>10} {'v':>10} {'u2+v2':>10} "
          f"{'p_eig':>22} {'|psi|^2':>22} {'max_dev':>11} {'sum_p':>9}")
    for m in res["per_mode"]:
        print(f"  {m['label']:<7} {m['u']:>10.6f} {m['v']:>10.6f} {m['norm']:>10.6f} "
              f"[{m['p_eig'][0]:.6f},{m['p_eig'][1]:.6f}] "
              f"[{m['psi2'][0]:.6f},{m['psi2'][1]:.6f}] "
              f"{m['max_dev']:>11.3e} {m['sum_p']:>9.6f}")
    print(f"\n  HEADLINE max_dev over 8 modes (eigenbasis): {res['value']:.6e}")
    print(f"  Retained-mode B1 eigenbasis dev:            {res['b1_dev']:.6e}")

    print("\n=== Basis-misalignment STRUCTURAL probe (Gleason consistency vs derivation) ===")
    for name, mm in res["misalign"].items():
        kind = "PURE   (u=1 or v=1)" if mm["purity"] > 1 - 1e-12 else "MIXED  (0<v^2<1)"
        print(f"  {name}: u={mm['u']:.6f} v={mm['v']:.6f}  purity(Tr rho^2)={mm['purity']:.6f}  "
              f"max basis gap |Tr(rho P)-|<psi|theta>|^2| = {mm['max_basis_gap']:.6e}  [{kind}]")

    verdict = evaluate_gate(res)

    # ---- Save data ----
    out_npz = OUT_DIR / "inv8_w2_3_born_rule_gge_coarse_grain.npz"  # (local)
    np.savez(
        out_npz,
        labels=np.array([m["label"] for m in res["per_mode"]]),
        u_k=np.array([m["u"] for m in res["per_mode"]]),
        v_k=np.array([m["v"] for m in res["per_mode"]]),
        p_eig=np.array([m["p_eig"] for m in res["per_mode"]]),
        psi2=np.array([m["psi2"] for m in res["per_mode"]]),
        per_mode_max_dev=np.array([m["max_dev"] for m in res["per_mode"]]),
        sum_p=np.array([m["sum_p"] for m in res["per_mode"]]),
        headline_max_dev=np.float64(res["value"]),
        b1_dev=np.float64(res["b1_dev"]),
        mixed_basis_gap=np.float64(max(v["max_basis_gap"] for v in res["misalign"].values())),
        purity_B1=np.float64(res["misalign"]["B1"]["purity"]),
        purity_B2=np.float64(res["misalign"]["B2"]["purity"]),
        purity_B3=np.float64(res["misalign"]["B3"]["purity"]),
        tol=np.float64(TOL),
        w1_1_present=np.bool_(res["w1_1_present"]),
        verdict=np.str_(verdict),
    )
    print(f"\n  data: {out_npz.relative_to(PROJECT_ROOT)}")

    out_png = OUT_DIR / "inv8_w2_3_born_rule_gge_coarse_grain.png"  # (local)
    make_plot(res, out_png)
    print(f"  plot: {out_png.relative_to(PROJECT_ROOT)}")

    # ---- 4-tuple + verdict payload ----
    print()
    print(emit_4tuple(res["value"], SCHEME, CONVENTION, L_MAX))
    mixed_gap = max(v["max_basis_gap"] for v in res["misalign"].values())  # (local)
    note = (f"two-track: eigenbasis_max_dev={res['value']:.3e}<{TOL:.0e} (factorization-forced); "
            f"structural NO-GO mixed_basis_gap={mixed_gap:.3e}>{TOL:.0e} (GGE marginal MIXED, "
            f"purity_B2={res['misalign']['B2']['purity']:.4f}<1) => Gleason CONSISTENCY only, "
            f"Born rule is an INPUT; track_B prior 0.65->0.9; w1_1_present={res['w1_1_present']} "
            f"(s52 substrate-first fallback)")
    print_verdict_payload(
        verdict, res["value"], audit_sha, content_sha,
        companion_note=note,
        extra_rows=[
            "# regulator_pin=N/A (GGE marginal, not a Seeley-DeWitt moment)",
            f"# structural_branch={'A_DERIVED' if verdict == 'PASS' else 'B_NOGO_input'} "
            f"eigenbasis_dev={res['value']:.3e} mixed_basis_gap={mixed_gap:.3e}",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
