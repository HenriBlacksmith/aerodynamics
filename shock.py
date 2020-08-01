from numpy import radians, sin, tan, cos, pi, arccos

# Inputs
gamma = 1.4
M = 1.2 # Mach number
theta_deg = 28.53
sigma_deg = 10.00

# Angles in radians
theta = radians(theta_deg)
sigma = radians(sigma_deg)

# Intermediate computations
Mn0 = M*sin(sigma) # Normal Mach number (pre-shock)

# Pre-shock ratios (Ideal homoentropic gas)
omega_bar0 = (1+(gamma-1)/2*M^2)**(-gamma/(gamma-1))
R0 =(1+(gamma-1)/2*M^2)**(-1/(gamma-1))
Theta0 =(1+(gamma-1)/2*M**2)**-1
Sigma0 =(2/(gamma+1))**((gamma+1)/(2*(gamma-1)))*1/B17*(1+(gamma-1)/2*M**2)**((gamma+1)/(2*(gamma-1)))

# Ratios (post/pre shock)
p1_p0 = 2*gamma/(gamma+1)*Mn0**2-(gamma-1)/(gamma+1)
rho1_rho0 = 1/(2/((gamma+1)*Mn0**2)+(gamma-1)/(gamma+1))
T1_T0 = p1_p0/rho1_rho0
pi1_pi0 = p1_p0**(-1/(gamma-1))*rho1_rho0**(gamma/(gamma-1))

# Post-shock values
Mn1 =((1+(gamma-1)/2*Mn0**2)/(gamma*Mn0**2-(gamma-1)/2))**(1/2) # Normal Mach number (post-shock)
M1 = Mn1*sin(sigma-theta) # Mach number (post-shock)
Cp1 =(p1_p0-1)/(gamma/2*M0**2) # Pressure coefficient (post-shock)

# Polar coefficients
A = (1+(gamma+1)/2*M**2)*tan(theta)
B = 1-M**2
C = (1+(gamma-1)/2*M**2)*tan(theta)
D = 1/3*(A^2/3-B)
E = 2/27*A^3-A*B/3+C

Phi_strong = arccos(-E/(2*D^(3/2)))+4*pi # Strong shock solution
Phi_weak = arccos(-E/(2*D^(3/2))) # Weak shock solution
Phi = Phi_strong

F = 2*D**(1/2)*cos(Phi/3)-A/3
