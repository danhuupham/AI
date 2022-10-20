from math import sqrt


def manhattan_distance(x1, x2):
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])


def euclidean_distance(x1, x2):
    return sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)
