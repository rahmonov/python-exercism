def distance(strand1, strand2):
    return sum(1 for point1, point2 in zip(strand1, strand2) if point1 != point2)