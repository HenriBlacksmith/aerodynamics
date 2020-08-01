from numpy import degrees, radians, sin, tan, cos, pi, arccos, arctan
from matplotlib.pyplot import subplots
from plot_shock import plot_shock
# Inputs
gamma = 1.4
M = 3.1 # Mach number
theta_deg = 28.53

# Angles in radians
theta = radians(theta_deg)

# Polar coefficients
A = (1+(gamma+1)/2*M**2)*tan(theta)
B = 1-M**2
C = (1+(gamma-1)/2*M**2)*tan(theta)
D = (1./3.)*((A**2)/3.-B)
E = (2./27.)*A**3-A*B/3.+C

Delta = E**2 - 4*D**3

print("=================================")
print("theta = " + str(theta) + " rad" + " = " + str(theta_deg) + " deg")
print("_________________________________")
print("A=" + str(A))
print("B=" + str(B))
print("C=" + str(C))
print("D=" + str(D))
print("E=" + str(E))
print("Delta=" + str(Delta))
print("_________________________________")

if (Delta < 0):   
    Phi_strong = arccos(-E/(2.*D**(3./2.)))+4.*pi # Strong shock solution
    Phi_weak = arccos(-E/(2.*D**(3./2.))) # Weak shock solution

    F_weak = 2.*D**(1./2.)*cos(Phi_weak/3.)-A/3.
    F_strong = 2.*D**(1./2.)*cos(Phi_strong/3.)-A/3.

    sigma_weak = arctan(1./F_weak)
    sigma_strong = arctan(1./F_strong)
    sigma = sigma_weak

    Mn0 = M*sin(sigma) # Normal Mach (pre-shock)

    # Ratios (post/pre shock)
    p1_p0 = 2*gamma/(gamma+1)*Mn0**2-(gamma-1)/(gamma+1)
    rho1_rho0 = 1/(2/((gamma+1)*Mn0**2)+(gamma-1)/(gamma+1))
    T1_T0 = p1_p0/rho1_rho0
    pi1_pi0 = p1_p0**(-1/(gamma-1))*rho1_rho0**(gamma/(gamma-1))

    # Post-shock values
    Mn1 =((1.+(gamma-1.)/2.*Mn0**2.)/(gamma*Mn0**2.-(gamma-1.)/2.))**(1./2.) # Normal Mach number (post-shock)
    M1 = Mn1*sin(sigma-theta) # Mach number (post-shock)
    Cp1 =(p1_p0-1)/(gamma/2*M**2) # Pressure coefficient (post-shock)

    print("Weak shock solution : ")
    print("Phi_weak=" + str(Phi_weak) + " rad")
    print("F_weak=" + str(F_weak))
    print("sigma_weak=" + str(sigma_weak) + " rad")
    print("_________________________________")
    print("Strong shock solution : ")
    print("Phi_strong=" + str(Phi_strong) + " rad")
    print("F_strong=" + str(F_strong))
    print("sigma_strong=" + str(sigma_strong) + " rad")
    print("_________________________________")
    print("Weak shock solution is chosen as physical solution : ")
    print("sigma=" + str(sigma) + " rad = " + str(degrees(sigma)) + " deg")
    print("Mn0=" + str(Mn0))
    print("Mn1=" + str(Mn1))
    print("M1=" + str(M1))
    print("Cp1=" + str(Cp1))
    print("_________________________________")
    print("Common ratios : ")
    print("p1_p0=" + str(p1_p0))
    print("rho1_rho0=" + str(rho1_rho0))
    print("T1_T0=" + str(T1_T0))
    print("pi1_pi0=" + str(pi1_pi0))
    fig, ax = subplots(1,1)
    plot_shock(theta, sigma_weak, M, M1, ax)
    
else : 
    print("No shock")

print("=================================")

# Pre-shock ratios (Ideal homoentropic gas)
# omega_bar0 = (1+(gamma-1)/2*M**2)**(-gamma/(gamma-1))
# R0 =(1+(gamma-1)/2*M**2)**(-1/(gamma-1))
# Theta0 =(1+(gamma-1)/2*M**2)**-1
# Sigma0 =(2/(gamma+1))**((gamma+1)/(2*(gamma-1)))*1/Theta0*(1+(gamma-1)/2*M**2)**((gamma+1)/(2*(gamma-1)))
