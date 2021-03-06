from gas_dynamics import sound_velocity, mach_angle, mayer_cv, mayer_cp, Theta, omega_bar, R, Sigma

# Inputs
M = 1.2
T = 273.15 # K
gamma = 1.4 

# Outputs
V = M*sound_velocity(T, gamma)
mu = mach_angle(M)

# Energy
u = mayer_cv(gamma)*T
h = mayer_cp(gamma)*T

# Ratios
T_Ti = Theta(gamma, M)
p_pi = omega_bar(gamma, M)
rho_rhoi = R(gamma, M)
A_Ac = Sigma(gamma, M)