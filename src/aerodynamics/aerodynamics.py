from numpy import arctan, array, cos, degrees, ndarray, pi, sqrt, tan

# c_r : root chord
# c_m
# phi : wing sweep
# b : wing span
# M : Mach number


class TrapezoidWing:
    """Object representing a trapezoid wing"""

    def __init__(self, c_r, c_m, b, phi) -> None:
        self.c_r = c_r
        self.c_m = c_m
        self.b = b
        self.phi = phi

    def wing_points(self) -> ndarray:
        x = array([0.0, 0.0, self.b / 2.0, self.b / 2.0, 0.0])
        y = array(
            [
                0.0,
                self.c_r,
                -self.b * tan(self.phi) / 2.0,
                -self.b * tan(self.phi) / 2.0 - self.c_m,
                0.0,
            ]
        )
        return array([x, y])

    def plot(self, ax):
        [x, y] = self.wing_points()
        return ax.plot(x, y)

    def surface(self):
        return (self.c_m + self.c_r) * self.b / 2.0

    def aspect_ratio(self):
        return 2.0 * self.b / (self.c_m + self.c_r)

    def mid_chord_sweep(self):
        return arctan(tan(self.phi) + (self.c_m - self.c_r) / self.b)

    def subsonic_diedrich_lift_grad(self, M):
        lam = self.aspect_ratio()  # Aspect ratio
        phi_half = self.mid_chord_sweep()  # Mid-chord sweep
        Mn = M * cos(self.phi)  # Normal Mach
        return pi * lam / (1.0 + sqrt(1.0 + (sqrt(1 - Mn**2) * lam / (2 * cos(phi_half))) ** 2)) * self.surface()

    def supersonic_lift_grad(self, M):
        if M**2 - 1.0 / cos(self.phi) ** 2 < 0.0:
            print(
                f"M**2-1./cos(phi)**2 = {str(M**2 - 1.0 / cos(self.phi) ** 2)}"
                + f" M={str(M)}"
                + f" phi (deg)={str(degrees(self.phi))}"
                + f" cos(phi)= {str(cos(self.phi))}"
            )
        return 4.0 / sqrt(abs(M**2 - 1.0 / cos(self.phi) ** 2)) * self.surface()

    def lift_grad(self, M):
        if M <= 1:
            return self.subsonic_diedrich_lift_grad(M)
        return self.supersonic_lift_grad(M)
