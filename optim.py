from numpy import linspace, zeros, inf, array, pi, radians
from matplotlib.pyplot import plot, xlabel, ylabel, title, show, rc, savefig, subplots, close
from scipy.optimize import minimize, least_squares
from aerodynamics import trapezoid_wing_lift_grad, plot_trapezoid_wing

def parametric_objective_max_lift_grad(x, M):
    c_r =   x[0]
    c_m =   x[1]
    b   =   x[2]
    phi =   x[3]
    return -trapezoid_wing_lift_grad(c_r, c_m, b, phi, M)

# Optimization (multipoint)
m_range = linspace(0.1, 1.5, 200)
lift_grad_vector = zeros(m_range.size)

fig, ax = subplots(1,1)
for i,m in enumerate(m_range):
    def objective_max_lift_grad(x):
        return parametric_objective_max_lift_grad(x, m)
    x0 = array([.1,.29,.42,.29])
    [c_r, c_m, b, phi] = x0
    plot_trapezoid_wing(c_r, c_m, b, phi, ax)
    res = least_squares(objective_max_lift_grad, x0, bounds=([1.e-2, 1.e-2, 1.e-2, 0.], [50., 50., 50., radians(80.)]))
    [c_r, c_m, b, phi] = res.x
    plot_trapezoid_wing(c_r, c_m, b, phi, ax)
    if res.success == True:
        lift_grad_vector[i] = res.fun
    else :
        lift_grad_vector[i] = float('nan')

# Plots
rc('text', usetex=True)
xlabel('$x$')
ylabel('$y$')
title('$Wings(M)$')
savefig('geoms.png', format='png')
close('all')

plot(m_range, lift_grad_vector)
rc('text', usetex=True)
xlabel('$M$')
ylabel('$Cl_a$')
title('$Cl_a(M)$')
savefig('lift_grad_mach.png', format='png')
close('all')
