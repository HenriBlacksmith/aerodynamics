# Prandtl-Meyer expansion fan

from matplotlib.pyplot import subplots
from numpy import arcsin, radians

from plot_expansion import (inverse_prandtl_meyer, plot_expansion,
                            plot_prandtl_meyer, prandtl_meyer)

# Inputs
GAMMA = 1.4
M = 2.0  # Mach number
THETA_DEG = 12.0

# Angles in radians
theta = radians(THETA_DEG)

# Mach lines

nu1 = theta + prandtl_meyer(M, GAMMA)
print(f"nu1={str(nu1)}")

mu = arcsin(1.0 / M)

M1 = inverse_prandtl_meyer(nu1, GAMMA)
mu1 = arcsin(1.0 / M1)
print(f"M1={str(M1)}\nmu1={str(mu1)}")

# After the expansion
_, ax = subplots(1, 1)
plot_expansion(theta, mu, mu1, M, M1, ax)

_, ax = subplots(1, 1)
plot_prandtl_meyer(ax)
