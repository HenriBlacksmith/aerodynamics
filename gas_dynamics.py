
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