from matplotlib.pyplot import plot
from numpy import arctan, array, cos, degrees, pi, sqrt, tan

# c_r : root chord
# c_m
# phi : wing sweep
# b : wing span
# M : Mach number

def trapezoid_wing_points(c_r, c_m, b, phi):
    x = array([0., 0., b/2., b/2., 0.])
    y = array([0., c_r, -b*tan(phi)/2., -b*tan(phi)/2.-c_m, 0.])
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
    lam = trapezoid_wing_aspect_ratio(c_r, c_m, b) # Aspect ratio
    phi_half = trapezoid_wing_mid_chord_sweep(c_r, c_m, b, phi) # Mid-chord sweep
    Mn = M*cos(phi) # Normal Mach
    return pi*lam/(1.+sqrt(1.+(sqrt(1-Mn**2)*lam/(2*cos(phi_half)))**2))*trapezoid_wing_surface(c_r, c_m, b)

def trapezoid_wing_supersonic_lift_grad(c_r, c_m, b, phi, M):
    if(M**2-1./cos(phi)**2<0.):
        print("M**2-1./cos(phi)**2 = " + str(M**2-1./cos(phi)**2) + " M=" + str(M) + " phi (deg)=" + str(degrees(phi)) + " cos(phi)= " + str(cos(phi)))
    return 4./sqrt(abs(M**2-1./cos(phi)**2))*trapezoid_wing_surface(c_r, c_m, b)

def trapezoid_wing_lift_grad(c_r, c_m, b, phi, M):
    if(M<=1):
        return trapezoid_wing_subsonic_diedrich_lift_grad(c_r, c_m, b, phi, M)
    else:
        return trapezoid_wing_supersonic_lift_grad(c_r, c_m, b, phi, M)