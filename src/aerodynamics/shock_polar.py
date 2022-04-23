from matplotlib.pyplot import (close, grid, rc, savefig, subplots, title,
                               xlabel, ylabel)
from numpy import (arccos, arctan, array, cos, degrees, linspace, nan, pi,
                   radians, tan, zeros)


def shock_polar_deg(theta_deg, M):

    # Inputs
    gamma = 1.4

    # Angle in radians
    theta = radians(theta_deg)

    # Polar coefficients
    A = (1 + (gamma + 1) / 2 * M**2) * tan(theta)
    B = 1 - M**2
    C = (1 + (gamma - 1) / 2 * M**2) * tan(theta)
    D = (1.0 / 3.0) * ((A**2) / 3.0 - B)
    E = (2.0 / 27.0) * A**3 - A * B / 3.0 + C
    Delta = E**2 - 4 * D**3

    if Delta < 0:
        Phi_strong = (
            arccos(-E / (2.0 * D ** (3.0 / 2.0))) + 4.0 * pi
        )  # Strong shock solution
        Phi_weak = arccos(-E / (2.0 * D ** (3.0 / 2.0)))  # Weak shock solution

        F_weak = 2.0 * D ** (1.0 / 2.0) * cos(Phi_weak / 3.0) - A / 3.0
        F_strong = 2.0 * D ** (1.0 / 2.0) * cos(Phi_strong / 3.0) - A / 3.0

        sigma_weak = arctan(1.0 / F_weak)
        sigma_strong = arctan(1.0 / F_strong)
    else:
        sigma_weak = nan
        sigma_strong = nan

    sigma_weak_deg = degrees(sigma_weak)
    sigma_strong_deg = degrees(sigma_strong)

    return array([sigma_weak_deg, sigma_strong_deg])


m_vect = linspace(1.0, 10.0, 20)
theta_vect = linspace(1.0, 90.0, 1000)
sigma_weak_vect = zeros(theta_vect.size)
sigma_strong_vect = zeros(theta_vect.size)

fig, ax = subplots(1, 1)

for j, m in enumerate(m_vect):
    for i, theta in enumerate(theta_vect):
        [sigma_weak_vect[i], sigma_strong_vect[i]] = shock_polar_deg(theta, m)
    ax.plot(theta_vect, sigma_weak_vect, color="b")
    ax.plot(theta_vect, sigma_strong_vect, color="r")

rc("text", usetex=True)
xlabel("$\\theta$")
ylabel("$\sigma$")
title("$\sigma_M(\\theta)$ - Shock polar")
ax.minorticks_on()
# Major grid
grid(which="major", linestyle="-", linewidth="0.5", color="black")
# Minor grid
grid(which="minor", linestyle=":", linewidth="0.5", color="black")
savefig("images/polar.png", format="png")
close("all")
