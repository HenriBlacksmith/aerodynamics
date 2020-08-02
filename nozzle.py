from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, title, show, rc, savefig, close, subplots, grid, gca

ps = 1.0
pi0 = 1.5

# shape is the ratio A(x)/A_throat
def divergent_shape(x):
    return 1 + 0.407*x**2*(3-2*x)

def convergent_shape(x):
    return 1 - 0.5*x

# Situations occuring while increasing pi0
# A - No Shock (one sonic section)
# AB - Shock in divergent
# B - Shock at the end of the divergent
# BC - Oblique Shock at the end of the divergent
# C - Fully sonic divergent

def plot_nozzle():
    fig, ax = subplots(1,1)
    divergent_geom_x = linspace(0., 1., 100)
    divergent_geom_y = divergent_shape(divergent_geom_x)
    ax.plot(divergent_geom_x, divergent_geom_y, 'r')
    ax.plot(divergent_geom_x, -divergent_geom_y, 'r')
    convergent_geom_x = linspace(-2., 0., 100)
    convergent_geom_y = convergent_shape(convergent_geom_x)
    ax.plot(convergent_geom_x, convergent_geom_y, 'r')
    ax.plot(convergent_geom_x, -convergent_geom_y, 'r')
    rc('text', usetex=True)
    gca().set_aspect('equal', adjustable='box')
    xlabel('$x$')
    ylabel('$y$')
    title('Nozzle')
    savefig('images/nozzle.png', format='png')
    close('all')

plot_nozzle()