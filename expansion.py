# Prandtl-Meyer expansion fan

from matplotlib.pyplot import subplots
from numpy import arcsin, radians

from plot_expansion import (inverse_prandtl_meyer, plot_expansion,
                            plot_prandtl_meyer, prandtl_meyer)

# Inputs
gamma = 1.4
M = 2.0  # Mach number
theta_deg = 12.0

# Angles in radians
theta = radians(theta_deg)

# Mach lines

nu1 = theta + prandtl_meyer(M, gamma)
print("nu1=" + str(nu1))

mu = arcsin(1.0 / M)

M1 = inverse_prandtl_meyer(nu1, gamma)
mu1 = arcsin(1.0 / M1)
print("M1=" + str(M1))
print("mu1=" + str(mu1))
# After the expansion
fig, ax = subplots(1, 1)
plot_expansion(theta, mu, mu1, M, M1, ax)

fig, ax = subplots(1, 1)
plot_prandtl_meyer(ax)
