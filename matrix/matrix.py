

class Matrix:
    def __init__(self, matrix_string):
        parts = matrix_string.split("\n")

        self.rows = [list(map(int, part.split(' '))) for part in parts]
        self.columns = list(map(list, zip(*self.rows)))

