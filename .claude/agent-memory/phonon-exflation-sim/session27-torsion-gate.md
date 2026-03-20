# Session 27: T-1 Torsion Gap Gate -- PASS

- Script: `s27_torsion_gap_gate.py`. Data: `.npz`, `.png`. Runtime: 1.3s.
- Canonical (Cartan-Schouten minus) connection: Gamma_can=0, T(X,Y)=-[X,Y]
- **Key identity**: K = -Gamma_LC at ALL tau (canonical always flat)
- D_can = D_K + Omega_T = D_K - Omega_LC = M_Lie
- Cross-checks: K=-Gamma_LC (0.0), Omega_T=-Omega_LC (0.0), D_can=M_Lie (1e-16)
- Torsion WEAKENS gap in ALL non-trivial sectors at ALL 21 tau values:
  - (1,0)/(0,1): gap_T/gap_K = 0.40 (tau=0) -> 0.22 (tau=0.50)
  - (1,1): gap_T/gap_K = 0.67 (tau=0) -> 0.35 (tau=0.50)
  - (0,0): gap_T=0 trivially (M_Lie=0 for singlet)
- Gap ratio monotonically decreasing with tau. BCS prerequisite confirmed.
