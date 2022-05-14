from matplotlib.pyplot import close, plot, rc, savefig, subplots, title, xlabel, ylabel
from numpy import array, linspace, radians, zeros
from scipy.optimize import least_squares

from aerodynamics.aerodynamics import TrapezoidWing


def parametric_objective_max_lift_grad(x, M):
    c_r = x[0]
    c_m = x[1]
    b = x[2]
    phi = x[3]
    return -TrapezoidWing(c_r, c_m, b, phi).lift_grad(M)


# Optimization (multipoint)
m_range = linspace(0.1, 1.5, 200)
lift_grad_vector = zeros(m_range.size)

fig, ax = subplots(1, 1)
for i, m in enumerate(m_range):

    def objective_max_lift_grad(x):
        return parametric_objective_max_lift_grad(x, m)

    x0 = array([0.1, 0.29, 0.42, 0.29])
    [c_r_0, c_m_0, b_0, phi_0] = x0
    TrapezoidWing(c_r_0, c_m_0, b_0, phi_0).plot(ax)
    res = least_squares(
        objective_max_lift_grad,
        x0,
        bounds=([1.0e-2, 1.0e-2, 1.0e-2, 0.0], [50.0, 50.0, 50.0, radians(80.0)]),
    )
    [c_r_res, c_m_res, b_res, phi_res] = res.x
    TrapezoidWing(c_r_res, c_m_res, b_res, phi_res).plot(ax)
    if res.success:
        lift_grad_vector[i] = res.fun
    else:
        lift_grad_vector[i] = float("nan")

# Plots
rc("text", usetex=True)
xlabel("$x$")
ylabel("$y$")
title("$Wings(M)$")
savefig("images/geoms.png", format="png")
close("all")

plot(m_range, lift_grad_vector)
rc("text", usetex=True)
xlabel("$M$")
ylabel("$Cl_a$")
title("$Cl_a(M)$")
savefig("images/lift_grad_mach.png", format="png")
close("all")
