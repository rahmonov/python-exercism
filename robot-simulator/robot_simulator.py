NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
X_MOVES = [0, 1, 0, -1]
Y_MOVES = [1, 0, -1, 0]


class Robot():
    def __init__(self, bearing=NORTH, x_cor=0, y_cor=0):
        self.bearing = bearing
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.movements = {
            'A': self.advance,
            'R': self.turn_right,
            'L': self.turn_left
        }

    @property
    def coordinates(self):
        return self.x_cor, self.y_cor

    def turn_right(self):
        self.bearing = (self.bearing + 1) % 4

    def turn_left(self):
        self.bearing = (self.bearing - 1) % 4

    def advance(self):
        self.x_cor += X_MOVES[self.bearing]
        self.y_cor += Y_MOVES[self.bearing]

    def simulate(self, directions):
        for direction in directions:
            self.movements[direction]()

