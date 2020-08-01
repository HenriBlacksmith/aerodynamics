# Prandtl-Meyer expansion fan

from numpy import arcsin, radians, sqrt
from matplotlib.pyplot import subplots
from plot_expansion import plot_expansion, plot_prandtl_meyer, prandtl_meyer
from scipy.optimize import newton

# Inputs
gamma = 1.4
M = 1.2 # Mach number
theta_deg = 40.

# Angles in radians
theta = radians(theta_deg)

# Mach lines

nu1 = theta + prandtl_meyer(M, gamma)
print("nu1=" + str(nu1))

mu = arcsin(1./M)

def inverse_prandtl_meyer(nu_val):
    def objective(x):
        return prandtl_meyer(x, gamma)-nu_val
    res = newton(objective, 1.5)
    print(res)
    return res

M1=inverse_prandtl_meyer(nu1)
mu1 = arcsin(1./M1)
print("M1=" + str(M1))
print("mu1=" + str(mu1))
# After the expansion
fig, ax = subplots(1,1)
plot_expansion(theta, mu, mu1, M, M1, ax)

fig, ax = subplots(1,1)
plot_prandtl_meyer(ax)

