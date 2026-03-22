"""
Time-dependent parameter evolution for cosmological expansion.

In the comoving frame, the expansion enters through time-dependent
coupling g(t) and chemical potential mu(t):
    R(t) = R0 * (1 + t/tau_exp)^alpha
    g(t) = g0 / R(t)^2
    mu(t) = g(t) * n0

Phase 2 additions: freeze-out modes for gamma_eff(t) that model
BBN-analog decoupling, preventing total vortex annihilation.
"""

import numpy as np


class ExpansionLaw:
    """Parameterizes cosmological expansion of the superfluid substrate."""

    def __init__(self, tau_exp=1000.0, alpha=0.667, g0=1.0, n0=1.0,
                 gamma0=0.0, R_freeze=None, freeze_mode='boltzmann'):
        self.tau_exp = tau_exp
        self.alpha = alpha
        self.g0 = g0
        self.n0 = n0
        self.gamma0 = gamma0  # dissipation strength (K-compactification rate)
        self.R_freeze = R_freeze  # scale factor at freeze-out (None = no freeze-out)
        self.freeze_mode = freeze_mode  # 'exponential', 'step', 'boltzmann', or 'self_consistent'
        self._sc_frozen = False  # self-consistent freeze-out state flag
        self._sc_freeze_time = None  # time at which self-consistent freeze-out occurred

    def scale_factor(self, t):
        """R(t) = R0 * (1 + t/tau_exp)^alpha"""
        return (1.0 + t / self.tau_exp) ** self.alpha

    def hubble_rate(self, t):
        """H(t) = dR/dt / R = alpha / (tau_exp + t)"""
        return self.alpha / (self.tau_exp + t)

    def g_eff(self, t):
        """Effective coupling: g(t) = g0 / R(t)^2"""
        R = self.scale_factor(t)
        return self.g0 / R**2

    def mu_eff(self, t):
        """Effective chemical potential: mu(t) = g(t) * n0"""
        return self.g_eff(t) * self.n0

    def healing_length(self, t):
        """xi(t) = 1 / sqrt(g(t) * n0) = xi_0 * R(t)"""
        return 1.0 / np.sqrt(self.g_eff(t) * self.n0)

    def sound_speed(self, t):
        """c_s(t) = sqrt(g(t) * n0 / m) = c_s0 / R(t)"""
        return np.sqrt(self.g_eff(t) * self.n0)

    def gamma_eff(self, t):
        """Dissipation rate with optional freeze-out.

        Four freeze-out modes control how gamma decays after R_freeze:
          exponential:       gamma0 * R * exp(-R / R_freeze)  -- peaks at R=R_freeze
          step:              gamma0 * R * Theta(R_freeze - R)  -- hard cutoff
          boltzmann:         gamma0 * R / (1 + exp((R-R_f)/dR)) -- sigmoid (most physical)
          self_consistent:   gamma0 * R until is_frozen_out() triggers, then 0
                             (R_freeze is ignored; freeze-out determined dynamically)

        When R_freeze is None: legacy behavior (gamma = gamma0 * R, no freeze-out).
        """
        if self.gamma0 == 0:
            return 0.0

        # Self-consistent mode: once frozen, gamma stays at 0
        if self.freeze_mode == 'self_consistent':
            if self._sc_frozen:
                return 0.0
            R = self.scale_factor(t)
            return self.gamma0 * R

        R = self.scale_factor(t)

        if self.R_freeze is None:
            # Legacy: no freeze-out
            return self.gamma0 * R

        if self.freeze_mode == 'exponential':
            return self.gamma0 * R * np.exp(-R / self.R_freeze)

        elif self.freeze_mode == 'step':
            if R < self.R_freeze:
                return self.gamma0 * R
            return 0.0

        else:  # boltzmann (default)
            dR = 0.1 * self.R_freeze
            return self.gamma0 * R / (1.0 + np.exp((R - self.R_freeze) / dR))

    def freeze_out_time(self):
        """Return t where R(t) = R_freeze. None if no freeze-out set."""
        if self.R_freeze is None:
            return None
        # R_freeze = (1 + t_f/tau_exp)^alpha  =>  t_f = tau_exp * (R_f^(1/alpha) - 1)
        return self.tau_exp * (self.R_freeze ** (1.0 / self.alpha) - 1.0)

    def vortex_dynamics_rate(self, t, d_mean):
        """Vortex interaction rate: c_s(t) / d_mean."""
        if d_mean <= 0:
            return float('inf')
        return self.sound_speed(t) / d_mean

    def is_frozen_out(self, t, d_mean):
        """True when vortex dynamics rate < Hubble rate (decoupled).

        Physical criterion: vortex-antivortex pairs can no longer find
        each other and annihilate when the interaction rate c_s/d_mean
        drops below the expansion rate H = dR/dt / R.
        """
        return self.vortex_dynamics_rate(t, d_mean) < self.hubble_rate(t)

    def check_self_consistent_freeze(self, t, d_mean):
        """Check and trigger self-consistent freeze-out.

        For freeze_mode='self_consistent', this should be called at each
        measurement step with the current mean inter-vortex spacing.

        Returns True if freeze-out was just triggered (or was already triggered).
        """
        if self.freeze_mode != 'self_consistent':
            return False
        if self._sc_frozen:
            return True
        if self.is_frozen_out(t, d_mean):
            self._sc_frozen = True
            self._sc_freeze_time = t
            return True
        return False

    @property
    def sc_freeze_time(self):
        """Time at which self-consistent freeze-out occurred, or None."""
        return self._sc_freeze_time

    @property
    def sc_freeze_R(self):
        """Scale factor at self-consistent freeze-out, or None."""
        if self._sc_freeze_time is None:
            return None
        return self.scale_factor(self._sc_freeze_time)

    def self_consistent_R_freeze(self):
        """Estimate R_freeze from equating vortex interaction rate to Hubble rate.

        R_freeze ~ sqrt(g0 * n0 * tau_exp / alpha)
        """
        return np.sqrt(self.g0 * self.n0 * self.tau_exp / self.alpha)

    def strouhal_number(self, t):
        """St = f_internal * tau_exp where f_internal ~ c_s / xi"""
        f_int = self.sound_speed(t) / self.healing_length(t)
        return f_int * self.tau_exp
