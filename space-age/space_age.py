SECONDS_IN_ONE_EARTH_YEAR = 31557600
SECONDS_IN_ONE_MERCURY_YEAR = 7600530.24
SECONDS_IN_ONE_VENUS_YEAR = 19413907.2
SECONDS_IN_ONE_MARS_YEAR = 59354294.4
SECONDS_IN_ONE_JUPITER_YEAR = 374335776.0
SECONDS_IN_ONE_SATURN_YEAR = 929596608.0
SECONDS_IN_ONE_URANUS_YEAR = 2661041808.0
SECONDS_IN_ONE_NEPTUNE_YEAR = 5200418592.0


def convert_period(period_seconds):
    def inner(self):
        return round(self.seconds / period_seconds, 2)

    return inner


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    on_earth = convert_period(SECONDS_IN_ONE_EARTH_YEAR)
    on_mercury = convert_period(SECONDS_IN_ONE_MERCURY_YEAR)
    on_venus = convert_period(SECONDS_IN_ONE_VENUS_YEAR)
    on_mars = convert_period(SECONDS_IN_ONE_MARS_YEAR)
    on_jupiter = convert_period(SECONDS_IN_ONE_JUPITER_YEAR)
    on_saturn = convert_period(SECONDS_IN_ONE_SATURN_YEAR)
    on_uranus = convert_period(SECONDS_IN_ONE_URANUS_YEAR)
    on_neptune = convert_period(SECONDS_IN_ONE_NEPTUNE_YEAR)

