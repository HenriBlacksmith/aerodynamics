from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, title, show, rc, savefig, close, subplots, grid, gca

ps = 1.0
pi0 = 1.5

# shape is the ratio A(x)/A_throat
def shape(x):
    return 1 + 0.407*x**2*(3-2*x)

# Situations occuring while increasing pi0
# A - No Shock (one sonic section)
# AB - Shock in divergent
# B - Shock at the end of the divergent
# BC - Oblique Shock at the end of the divergent
# C - Fully sonic divergent

def plot_nozzle():
    fig, ax = subplots(1,1)
    geom_x = linspace(0., 1., 100)
    geom_y = shape(geom_x)
    ax.plot(geom_x, geom_y, 'r')
    ax.plot(geom_x, -geom_y, 'r')
    rc('text', usetex=True)
    gca().set_aspect('equal', adjustable='box')
    xlabel('$x$')
    ylabel('$y$')
    title('Nozzle')
    savefig('images/nozzle.png', format='png')
    close('all')

plot_nozzle()