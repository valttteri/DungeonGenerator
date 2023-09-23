from math import sqrt
from random import randint

def find_circumcenter(coordinates: list):
    """Find cartesian coordinates of a triangle's circumcenter.
    I found the formula from this website: https://en.wikipedia.org/wiki/Circumcircle"""

    ax = coordinates[0][0]
    ay = coordinates[0][1]
    bx = coordinates[1][0]
    by = coordinates[1][1]
    cx = coordinates[2][0]
    cy = coordinates[2][1]

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = (
        (ax * ax + ay * ay) * (by - cy)
        + (bx * bx + by * by) * (cy - ay)
        + (cx * cx + cy * cy) * (ay - by)
    ) / d
    uy = (
        (ax * ax + ay * ay) * (cx - bx)
        + (bx * bx + by * by) * (ax - cx)
        + (cx * cx + cy * cy) * (bx - ax)
    ) / d
    return ux, uy

# Calculate the distance between two points
def distance_between_points(point_a: tuple, point_b: tuple):
    """Calculate the distance between two nodes"""

    distance = sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)
    return distance

# Generate coordinates in a way to avoid duplicates
def generate_coordinates(count: int, X_MIN: int, X_MAX: int, Y_MIN: int, Y_MAX: int):
    """Generate coordinates for the triangulation"""

    coordinate_list = []

    while len(coordinate_list) < count:
        valid = True
        x = randint(X_MIN, X_MAX)
        y = randint(Y_MIN, Y_MAX)
        candidate = (x, y)

        if candidate in coordinate_list:
            valid = False

        if valid:
            for coordinate in coordinate_list:
                if distance_between_points(candidate, coordinate) < 100:
                    valid = False

        if valid:
            coordinate_list.append(candidate)

    return coordinate_list

def are_edges_equal(edge_1: list, edge_2: list):
    """Check if two separate edges are equal"""

    return (edge_1[0] == edge_2[0] and edge_1[1] == edge_2[1]) or (
        edge_1[0] == edge_2[1] and edge_1[1] == edge_2[0]
    )