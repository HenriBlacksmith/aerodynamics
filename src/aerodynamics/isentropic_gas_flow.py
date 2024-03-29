from aerodynamics.gas_dynamics import (
    R_,
    Sigma,
    Theta,
    mach_angle,
    mayer_cp,
    mayer_cv,
    omega_bar,
    sound_velocity,
)

# Inputs
M = 1.2
T = 273.15  # K
gamma = 1.4

# Outputs
V = M * sound_velocity(T, gamma)
mu = mach_angle(M)

# Energy
u = mayer_cv(gamma) * T
h = mayer_cp(gamma) * T

# Ratios
T_Ti = Theta(gamma, M)
p_pi = omega_bar(gamma, M)
rho_rhoi = R_(gamma, M)
A_Ac = Sigma(gamma, M)
