from numpy import arcsin, arctan, pi, tan

# Physical constants
M_AIR = 28.965338 / 1000.0  # kg/mol
N_AVOGADRO = 6.02214086e23  # 1/mol
K_BOLTZMANN = 1.38064852e-23  # J/K

# Perfect gas constants
R = K_BOLTZMANN * N_AVOGADRO  # J/K/mol
r = R / M_AIR  # J/K/kg


# Mayer relations
def mayer_cp(gamma):
    return r * gamma / (gamma - 1)  # J/K/kg


def mayer_cv(gamma):
    return r / (gamma - 1)  # J/K/kg


# Sound
def sound_velocity(T, gamma):  # m/s
    return (gamma * r * T) ** (1.0 / 2.0)


def mach_angle(M):  # rad
    return arcsin(1.0 / M)


# Ratios
def Theta(gamma, M):
    return (1.0 + M**2.0 * (gamma - 1.0) / 2.0) ** -1.0


def omega_bar(gamma, M):
    return Theta(gamma, M) ** (gamma / (gamma - 1.0))


def R_(gamma, M):
    return Theta(gamma, M) ** (1.0 / (gamma - 1.0))


def Sigma(gamma, M):
    return (2.0 * Theta(gamma, M) / (gamma + 1.0)) ** -(
        (gamma + 1.0) / (2.0 * (gamma - 1.0))
    ) / M


def phi(gamma, M):
    return omega_bar(gamma, M) * Sigma(gamma, M) * (1 + gamma * M**2)


def omega(gamma, M):  # rad
    return (
        mach_angle(M)
        + ((gamma + 1.0) / (gamma - 1.0)) ** (1.0 / 2.0)
        * arctan(1.0 / (tan(mach_angle(M)) * (gamma + 1.0) / (gamma - 1.0)))
        - pi / 2.0
    )
