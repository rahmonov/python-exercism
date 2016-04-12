SECONDS_IN_ONE_EARTH_YEAR = 31557600
MERCURY_AGE_COEFFICIENT = 0.2408467
VENUS_AGE_COEFFICIENT = 0.61519726
MARS_AGE_COEFFICIENT = 1.8808158
JUPITER_AGE_COEFFICIENT = 11.862615
SATURN_AGE_COEFFICIENT = 29.447498
URANUS_AGE_COEFFICIENT = 84.016846
NEPTUNE_AGE_COEFFICIENT = 164.79132


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_age = seconds / SECONDS_IN_ONE_EARTH_YEAR

    def on_earth(self):
        return round(self.earth_age, 2)

    def on_mercury(self):
        return round(self.earth_age / MERCURY_AGE_COEFFICIENT, 2)

    def on_venus(self):
        return round(self.earth_age / VENUS_AGE_COEFFICIENT, 2)

    def on_mars(self):
        return round(self.earth_age / MARS_AGE_COEFFICIENT, 2)

    def on_jupiter(self):
        return round(self.earth_age / JUPITER_AGE_COEFFICIENT, 2)

    def on_saturn(self):
        return round(self.earth_age / SATURN_AGE_COEFFICIENT, 2)

    def on_uranus(self):
        return round(self.earth_age / URANUS_AGE_COEFFICIENT, 2)

    def on_neptune(self):
        return round(self.earth_age / NEPTUNE_AGE_COEFFICIENT, 2)
