# Computation Script Standards

## Canonical Constants (MANDATORY)

ALL scripts MUST `from canonical_constants import *` and use imported symbols. **Never hardcode framework constants.**

Examples of constants that MUST be imported: `M_KK`, `E_cond`, `tau_fold`, `Vol_SU3`, `Delta_BCS`, `rho_s`, `T_acoustic`, `J_C2`, `omega_L1`, `dS_fold`, `d2S_fold`, `S_fold`, `c_Gold`, `c_fabric`, `dt_transit`, `v_ew`, `m_H_obs`, `m_t_pole`, `alpha_s_MZ_obs`, `w0_FW`, `planck_ns`, and all others in `canonical_constants.py`.

If a constant you need isn't there, **ADD it to `canonical_constants.py` FIRST**, then import it in your script.

## Local Variable Tagging (MANDATORY)

Every variable that is a **computed intermediate value** (not a framework constant) must be tagged with `# (local)` at the end of its assignment line:

```python
E_kin = 0.5 * m * v**2          # (local)
R_ratio = a_2 / a_4             # (local)
delta_ns = ns_bare - ns_planck  # (local)
PASS_THRESH = 0.05              # (local) 5% gate threshold
omega_ref = 1.0                 # (local) M_KK^2 Fermi scale
```

The `# (local)` tag tells the `/weave --update` audit to skip this line. Without it, any assignment matching the potential-hardcode regex will be flagged.

### When to use `# (local)`
- Computed quantities derived from other variables
- Loop accumulators and initializers (`total = 0.0`)
- Gate thresholds specific to this script
- Scan parameters, window bounds, tolerance values
- Cross-reference values from prior sessions
- Fallback/default values in else branches

### When NOT to use `# (local)`
- Framework constants — import from `canonical_constants.py`
- Observational values (PDG, Planck, DESI) used in 2+ scripts — promote to `canonical_constants.py`
- Values that other scripts need — promote to `canonical_constants.py`

### Accepted tag formats
All of these are recognized by the audit:
- `# (local)` — minimal
- `# (local) description` — with explanation
- `# description (local)` — trailing
- `# (local, reason)` — with inline reason

## Windows 0KB Bash Bug

Bash output always shows 0KB on Windows. This is a known platform issue. **Do NOT retry commands that appear to produce empty output.** The script ran successfully. Check for output files (.npz, .png) instead of reading stdout.

## Script Execution

Always use the GPU venv: `"phonon-exflation-sim/.venv312/Scripts/python.exe" script.py`

## Audit

Run `/weave --update` to audit compliance. Target: **Violations = 0, Potential = 0.**