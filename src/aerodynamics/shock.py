from matplotlib.pyplot import subplots
from numpy import arccos, arctan, cos, degrees, pi, radians, sin, tan

from aerodynamics.plot_shock import plot_data_table, plot_shock

# Inputs
gamma = 1.4
M = 3.1  # Mach number
theta_deg = 28.53

# Angles in radians
theta = radians(theta_deg)

# Polar coefficients
A = (1 + (gamma + 1) / 2 * M**2) * tan(theta)
B = 1 - M**2
C = (1 + (gamma - 1) / 2 * M**2) * tan(theta)
D = (1.0 / 3.0) * ((A**2) / 3.0 - B)
E = (2.0 / 27.0) * A**3 - A * B / 3.0 + C

Delta = E**2 - 4 * D**3

print("=================================")

if Delta < 0:
    Phi_strong = arccos(-E / (2.0 * D ** (3.0 / 2.0))) + 4.0 * pi  # Strong shock solution
    Phi_weak = arccos(-E / (2.0 * D ** (3.0 / 2.0)))  # Weak shock solution

    F_weak = 2.0 * D ** (1.0 / 2.0) * cos(Phi_weak / 3.0) - A / 3.0
    F_strong = 2.0 * D ** (1.0 / 2.0) * cos(Phi_strong / 3.0) - A / 3.0

    sigma_weak = arctan(1.0 / F_weak)
    sigma_strong = arctan(1.0 / F_strong)
    sigma = sigma_weak
    sigma_deg = degrees(sigma)

    Mn0 = M * sin(sigma)  # Normal Mach (pre-shock)

    # Ratios (post/pre shock)
    p1_p0 = 2 * gamma / (gamma + 1) * Mn0**2 - (gamma - 1) / (gamma + 1)
    rho1_rho0 = 1 / (2 / ((gamma + 1) * Mn0**2) + (gamma - 1) / (gamma + 1))
    T1_T0 = p1_p0 / rho1_rho0
    pi1_pi0 = p1_p0 ** (-1 / (gamma - 1)) * rho1_rho0 ** (gamma / (gamma - 1))

    # Post-shock values
    Mn1 = ((1.0 + (gamma - 1.0) / 2.0 * Mn0**2.0) / (gamma * Mn0**2.0 - (gamma - 1.0) / 2.0)) ** (
        1.0 / 2.0
    )  # Normal Mach number (post-shock)
    M1 = Mn1 * sin(sigma - theta)  # Mach number (post-shock)
    Cp1 = (p1_p0 - 1) / (gamma / 2 * M**2)  # Pressure coefficient (post-shock)

    print("Weak shock solution : ")
    print(f"Phi_weak={Phi_weak} rad")
    print(f"F_weak={F_weak}")
    print(f"sigma_weak={sigma_weak} rad")
    print("_________________________________")
    print("Strong shock solution : ")
    print(f"Phi_strong={Phi_strong} rad")
    print(f"F_strong={F_strong}")
    print(f"sigma_strong={sigma_strong} rad")
    print("_________________________________")
    print("Weak shock solution is chosen as physical solution")
    fig, ax = subplots(1, 1)
    plot_shock(theta, sigma_weak, M, M1, ax)

else:
    print("No attached shock")

print("=================================")

table_data = [
    ["$\\theta$", str(round(theta_deg, 5)) + " deg = " + str(round(theta, 5)) + " rad"],
    ["$A$", str(round(A, 5))],
    ["$B$", str(round(B, 5))],
    ["$C$", str(round(C, 5))],
    ["$D$", str(round(D, 5))],
    ["$E$", str(round(E, 5))],
    ["$\\Delta$", str(round(Delta, 5))],
    ["$Mn_0$", str(round(Mn0, 5))],
    ["$Mn_1$", str(round(Mn1, 5))],
    ["$M_0$", str(round(M, 5))],
    ["$M_1$", str(round(M1, 5))],
    ["$Cp_1$", str(round(Cp1, 5))],
    ["$\\sigma$", str(round(sigma_deg, 5)) + " deg = " + str(round(sigma, 5)) + " rad"],
    ["$p_1/p_0$", str(round(p1_p0, 5))],
    ["$T_1/T_0$", str(round(T1_T0, 5))],
    ["$pi_1/pi_0$", str(round(pi1_pi0, 5))],
    ["$\\rho_1/\\rho_0$", str(round(rho1_rho0, 5))],
]
plot_data_table(table_data)

# Pre-shock ratios (Ideal homoentropic gas)
# omega_bar0 = (1+(gamma-1)/2*M**2)**(-gamma/(gamma-1))
# R0 =(1+(gamma-1)/2*M**2)**(-1/(gamma-1))
# Theta0 =(1+(gamma-1)/2*M**2)**-1
# Sigma0 =(2/(gamma+1))**((gamma+1)/(2*(gamma-1)))*1/Theta0*(1+(gamma-1)/2*M**2)**((gamma+1)/(2*(gamma-1)))
