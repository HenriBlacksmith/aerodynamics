from numpy import arctan, tan, array, linspace, sqrt, zeros, degrees
from matplotlib.pyplot import plot, xlabel, ylabel, title, show, rc, gca, savefig, subplots, close, arrow, annotate, table, grid
from scipy.optimize import newton

def prandtl_meyer_deg(M, gamma):
    return degrees(sqrt((gamma+1)/(gamma-1))*arctan(sqrt((gamma-1)/(gamma+1))*(M**2-1)) - arctan(M**2-1))

def prandtl_meyer(M, gamma):
    return sqrt((gamma+1)/(gamma-1))*arctan(sqrt((gamma-1)/(gamma+1))*(M**2-1)) - arctan(M**2-1)

def inverse_prandtl_meyer(nu_val):
    def objective(x):
        return prandtl_meyer(x, gamma)-nu_val
    res = newton(objective, 1.5)
    print(res)
    return res

# Plotting functions
def wall_points(theta):
    x = array([-1., 0., 1.])
    y = array([0., 0., -tan(theta)])
    return array([x,y])

def first_expansion_wave_points(mu):
    x = array([0., 1.])
    y = array([0., tan(mu)])
    return array([x,y])

def last_expansion_wave_points(mu1):
    x = array([0., 1.])
    y = array([0., tan(mu1)])
    return array([x,y])

def plot_data_table(data):
    fig, ax = subplots(1,1)
    rc('text', usetex=True)
    ax.axis('off')
    ax.table(cellText=data, loc='center')
    title('Oblique shock data')
    savefig('images/data.png', format='png')
    close('all')

def plot_expansion(theta, mu, mu1, M, M1, ax):
    [wall_x, wall_y] = wall_points(theta)
    [first_wave_x, first_wave_y] = first_expansion_wave_points(mu)
    [last_wave_x, last_wave_y] = last_expansion_wave_points(mu1)
    ax.plot(wall_x, wall_y, 'r')
    ax.plot(first_wave_x, first_wave_y, 'b')
    ax.plot(last_wave_x, last_wave_y, 'g')
    # Arrow representing pre-expansion velocity
    ax.annotate("", 
            xy=(-0.7, 0.2), 
            xytext=(-1, 0.2), 
            arrowprops=dict(arrowstyle="->"), 
            horizontalalignment='left',
            verticalalignment='bottom')
    ax.annotate("M=" + str(M), 
            xy=(-0.7, 0.25), 
            xytext=(-1, 0.25))
    # Arrow representing post-expansion velocity
    ax.annotate("", 
            xy=(0.6, 0.1-0.2*tan(theta)), 
            xytext=(0.4, 0.1), 
            arrowprops=dict(arrowstyle="->"), 
            horizontalalignment='left',
            verticalalignment='bottom')
    ax.annotate("$M_1=$" + str(round(M1,2)), 
            xy=(0.6, 0.1+0.2*tan(theta)), 
            xytext=(0.6, -0.1))
    rc('text', usetex=True)
    gca().set_aspect('equal', adjustable='box')
    xlabel('$x$')
    ylabel('$y$')
    title('Expansion fan')
    savefig('images/expansion.png', format='png')
    close('all')

def plot_prandtl_meyer(ax):
    m_vect = linspace(1., 10., 20)
    nu_vect = zeros(m_vect.size)
    for j, m in enumerate(m_vect):
        nu_vect[j] = prandtl_meyer_deg(m, 1.4)
    ax.plot(m_vect, nu_vect)
    rc('text', usetex=True)
    xlabel('$M$')
    ylabel('$\\nu (^{\circ})$')
    title("$\\nu(M)$ - Prandtl-Meyer function in degrees")
    ax.minorticks_on()
    # Major grid
    grid(which='major', linestyle='-', linewidth='0.5', color='black')
    # Minor grid
    grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    savefig('images/prandtl_meyer.png', format='png')
    close('all')

