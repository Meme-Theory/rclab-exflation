# Transit-Dynamics-Theorist Memory (investigation-12)

## Project / derivation facts
- [Relic spectrum BdG dispersion](relic-spectrum-bdg-dispersion.md) — omega_k=sqrt((lambda_k-mu)^2+Delta_k^2), mu=0; S101 pair band [1.6395,10.8379]=2|lambda| edges (EXACT); plan's (lambda^2-mu^2)^2 is a transcription of (lambda-mu) BdG band energy

## Reference / infrastructure
- [Dirac-spectrum GPU eigvalsh](dirac-spectrum-gpu-eigvalsh.md) — ROCm build lacks MAGMA; use eigvalsh(i*D) (Hermitian) NOT eigvals; verified ==numpy|eig.imag| to 1e-14
