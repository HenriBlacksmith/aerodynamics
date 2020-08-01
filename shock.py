from numpy import radians, sin, tan, cos, pi, arccos, arctan, array
from matplotlib.pyplot import plot, xlabel, ylabel, title, show, rc, gca, savefig, subplots, close

# Inputs
gamma = 1.4
M = 2.4 # Mach number
theta_deg = 28.53

# Angles in radians
theta = radians(theta_deg)

# Polar coefficients
A = (1+(gamma+1)/2*M**2)*tan(theta)
B = 1-M**2
C = (1+(gamma-1)/2*M**2)*tan(theta)
D = (1./3.)*((A**2)/3.-B)
E = (2./27.)*A**3-A*B/3.+C

Phi_strong = arccos(-E/(2.*D**(3./2.)))+4.*pi # Strong shock solution
Phi_weak = arccos(-E/(2.*D**(3./2.))) # Weak shock solution

F_weak = 2.*D**(1./2.)*cos(Phi_weak/3.)-A/3.
F_strong = 2.*D**(1./2.)*cos(Phi_strong/3.)-A/3.

sigma_weak = arctan(1./F_weak)
sigma_strong = arctan(1./F_strong)

print("=================================")
print("theta=" + str(theta) + " rad")
print("theta=" + str(theta_deg) + " deg")
print("_________________________________")
print("A=" + str(A))
print("B=" + str(B))
print("C=" + str(C))
print("D=" + str(D))
print("E=" + str(E))
print("_________________________________")
print("Weak shock solution : ")
print("Phi_weak=" + str(Phi_weak) + " rad")
print("F_weak=" + str(F_weak))
print("sigma_weak=" + str(sigma_weak) + " rad")
print("_________________________________")
print("Strong shock solution : ")
print("Phi_strong=" + str(Phi_strong) + " rad")
print("F_strong=" + str(F_strong))
print("sigma_strong=" + str(sigma_strong) + " rad")
print("=================================")

# Pre-shock ratios (Ideal homoentropic gas)
# omega_bar0 = (1+(gamma-1)/2*M**2)**(-gamma/(gamma-1))
# R0 =(1+(gamma-1)/2*M**2)**(-1/(gamma-1))
# Theta0 =(1+(gamma-1)/2*M**2)**-1
# Sigma0 =(2/(gamma+1))**((gamma+1)/(2*(gamma-1)))*1/Theta0*(1+(gamma-1)/2*M**2)**((gamma+1)/(2*(gamma-1)))

# Ratios (post/pre shock)
# p1_p0 = 2*gamma/(gamma+1)*Mn0**2-(gamma-1)/(gamma+1)
# rho1_rho0 = 1/(2/((gamma+1)*Mn0**2)+(gamma-1)/(gamma+1))
# T1_T0 = p1_p0/rho1_rho0
# pi1_pi0 = p1_p0**(-1/(gamma-1))*rho1_rho0**(gamma/(gamma-1))

# Post-shock values
# Mn1 =((1+(gamma-1)/2*Mn0**2)/(gamma*Mn0**2-(gamma-1)/2))**(1/2) # Normal Mach number (post-shock)
# M1 = Mn1*sin(sigma-theta) # Mach number (post-shock)
# Cp1 =(p1_p0-1)/(gamma/2*M**2) # Pressure coefficient (post-shock)

def wall_points(theta):
    x = array([-1., 0., 1.])
    y = array([0., 0., tan(theta)])
    return array([x,y])

def weak_shock_wave_points(sigma_weak):
    x = array([0., 1.])
    y = array([0., tan(sigma_weak)])
    return array([x,y])

def strong_shock_wave_points(sigma_strong):
    x = array([0., 1.])
    y = array([0., tan(sigma_strong)])
    return array([x,y])

def plot_shock(theta, sigma_weak, sigma_strong, ax):
    [wall_x, wall_y] = wall_points(theta)
    [weak_x, weak_y] = weak_shock_wave_points(sigma_weak)
    [strong_x, strong_y] = strong_shock_wave_points(sigma_strong)
    ax.plot(wall_x, wall_y, 'r')
    ax.plot(weak_x, weak_y, 'b')
    ax.plot(strong_x, strong_y, 'g')
    rc('text', usetex=True)
    gca().set_aspect('equal', adjustable='box')
    xlabel('$x$')
    ylabel('$y$')
    title('$Oblique shock$')
    savefig('shock.png', format='png')
    close('all')

fig, ax = subplots(1,1)
plot_shock(theta, sigma_weak, sigma_strong, ax)
