from numpy import arcsin, arctan, pi, tan

# Physical constants
M_air = 28.965338/1000. # kg/mol
N_Avogadro = 6.02214086e23  # 1/mol
k_Boltzmann = 1.38064852e-23 # J/K

# Perfect gas constants
R = k_Boltzmann*N_Avogadro # J/K/mol
r = R/M_air # J/K/kg

# Mayer relations
def mayer_cp(gamma): 
    return r*gamma/(gamma-1) # J/K/kg

def mayer_cv(gamma):
    return r/(gamma-1) # J/K/kg

# Sound
def sound_velocity(T, gamma): # m/s
    return (gamma*r*T)**(1./2.)

def mach_angle(M): # rad
    return arcsin(1./M)

# Ratios
def Theta(gamma, M):
    return (1.+M**2.*(gamma-1.)/2.)**-1.

def omega_bar(gamma, M):
    return Theta(gamma, M)**(gamma/(gamma-1.))

def R(gamma, M):
    return Theta(gamma, M)**(1./(gamma-1.))

def Sigma(gamma, M):
    return (2.*Theta(gamma, M)/(gamma+1.))**-((gamma+1.)/(2.*(gamma-1.)))/M

def phi(gamma, M):
    return omega_bar(gamma, M)*Sigma(gamma, M)*(1+gamma*M**2)

def omega(gamma, M): # rad
    return mach_angle(M) + ((gamma+1.)/(gamma-1.))**(1./2.)*arctan(1./(tan(mach_angle(M))*(gamma+1.)/(gamma-1.)))-pi/2.