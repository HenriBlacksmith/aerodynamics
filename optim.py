from numpy import arctan, cos, tan, sqrt, pi, array, linspace, zeros
from matplotlib.pyplot import plot, xlabel, ylabel, title, show, rc, savefig, bar, subplots, scatter, close
from scipy.optimize import minimize, least_squares

# c_r : root chord
# c_m
# phi : wing sweep
# b : wing span
# M : Mach number

def trapezoid_wing_points(c_r, c_m, b, phi):
    x = array([0., 0., b/2., b/2., 0.])
    y = array([0., c_r, -b*tan(phi)/2., -b*tan(phi)/2.-c_m, 0.])
    print([x, y])
    return array([x, y])

def plot_trapezoid_wing(c_r, c_m, b, phi, ax):
    [x, y] = trapezoid_wing_points(c_r, c_m, b, phi)
    return ax.plot(x,y)

def trapezoid_wing_surface(c_r, c_m, b):
    return (c_m+c_r)*b/2.

def trapezoid_wing_aspect_ratio(c_r, c_m, b):
    return 2.*b/(c_m+c_r)

def trapezoid_wing_mid_chord_sweep(c_r, c_m, b, phi):
    return arctan(tan(phi) + (c_m-c_r)/b)

def trapezoid_wing_subsonic_diedrich_lift_grad(c_r, c_m, b, phi, M):
    lam = trapezoid_wing_aspect_ratio(c_r, c_m, b)
    phi_half = trapezoid_wing_mid_chord_sweep(c_r, c_m, b, phi)
    return pi*lam/(1+sqrt(1+(lam**2/4*cos(phi_half)**2)*(1-M**2*cos(phi)**2)))

def trapezoid_wing_supersonic_lift_grad(phi, M):
     return 4/sqrt(M**2-1/cos(phi)**2)

def trapezoid_wing_lift_grad(c_r, c_m, b, phi, M):
    if(M<=1):
        return trapezoid_wing_subsonic_diedrich_lift_grad(c_r, c_m, b, phi, M)
    else:
        return trapezoid_wing_supersonic_lift_grad(phi, M)

def parametric_objective_max_lift_grad(x, M):
    c_r =   x[0]
    c_m =   x[1]
    b   =   x[2]
    phi =   x[3]
    return -trapezoid_wing_lift_grad(c_r, c_m, b, phi, M)


# Optimization (multipoint)
m_range = linspace(0.1, 2., 10)
lift_grad_vector = zeros(m_range.size)

fig, ax = subplots(1,1)
for i,m in enumerate(m_range):
    def objective_max_lift_grad(x):
        M=3.
        return parametric_objective_max_lift_grad(x, M)
    x0 = array([.1,.29,.42,.29])
    [c_r, c_m, b, phi] = x0
    plot_trapezoid_wing(c_r, c_m, b, phi, ax)
    res = least_squares(objective_max_lift_grad, x0)
    [c_r, c_m, b, phi] = res.x
    plot_trapezoid_wing(c_r, c_m, b, phi, ax)
    # print(res)
    if res.success == True:
        lift_grad_vector[i] = res.fun
    else :
        lift_grad_vector[i] = float('nan')

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
