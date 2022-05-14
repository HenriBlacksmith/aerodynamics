from matplotlib.pyplot import close, gca, rc, savefig, subplots, title, xlabel, ylabel
from numpy import array, tan


# Plotting functions
def wall_points(theta):
    x = array([-1.0, 0.0, 1.0])
    y = array([0.0, 0.0, tan(theta)])
    return array([x, y])


def weak_shock_wave_points(sigma_weak):
    x = array([0.0, 1.0])
    y = array([0.0, tan(sigma_weak)])
    return array([x, y])


def strong_shock_wave_points(sigma_strong):
    x = array([0.0, 1.0])
    y = array([0.0, tan(sigma_strong)])
    return array([x, y])


def plot_data_table(data):
    _, ax = subplots(1, 1)
    rc("text", usetex=True)
    ax.axis("off")
    ax.table(cellText=data, loc="center")
    title("Oblique shock data")
    savefig("images/data.png", format="png")
    close("all")


def plot_shock(theta, sigma_weak, M, M1, ax):
    [wall_x, wall_y] = wall_points(theta)
    [weak_x, weak_y] = weak_shock_wave_points(sigma_weak)
    ax.plot(wall_x, wall_y, "r")
    ax.plot(weak_x, weak_y, "b")
    # Arrow representing pre-shock velocity
    ax.annotate(
        "",
        xy=(-0.7, 0.3),
        xytext=(-1, 0.3),
        arrowprops=dict(arrowstyle="->"),
        horizontalalignment="left",
        verticalalignment="bottom",
    )
    ax.annotate("M=" + str(M), xy=(-0.7, 0.35), xytext=(-1, 0.35))
    # Arrow representing post-shock velocity
    ax.annotate(
        "",
        xy=(0.6, 0.35 + 0.2 * tan(theta)),
        xytext=(0.4, 0.35),
        arrowprops=dict(arrowstyle="->"),
        horizontalalignment="left",
        verticalalignment="bottom",
    )
    ax.annotate(
        "$M_1=$" + str(round(M1, 2)),
        xy=(0.6, 0.6 + 0.2 * tan(theta)),
        xytext=(0.6, 0.4),
    )
    # ax.annotate("M_1=" + str(M1),
    #        xy=(0.6, 0.5),
    #        xytext=(0.4, 0.5))
    rc("text", usetex=True)
    gca().set_aspect("equal", adjustable="box")
    xlabel("$x$")
    ylabel("$y$")
    title("Oblique shock")
    savefig("images/shock.png", format="png")
    close("all")
