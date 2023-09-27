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
    return round(ux, 3), round(uy, 3)

# Calculate the distance between two points
def distance_between_points(point_a: tuple, point_b: tuple):
    """Calculate the distance between two nodes"""

    distance = round(sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2), 3)
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

def unique_edges(triangles: list):
    """Returns a list containing unique edges in a triangulation"""
    edge_list=set()

    for triangle in triangles:
        edges = triangle.show_edges()
        for edge in edges:
            if (edge[0], edge[1]) in edge_list or (edge[1], edge[0]) in edge_list:
                continue
            edge_list.add((edge[0], edge[1]))
    
    return edge_list

def create_graph(tuples: list):
    graph = {}

    for tuple in tuples:
        if tuple[0] not in graph:
            graph[tuple[0]] = []
        if tuple[1] not in graph:
            graph[tuple[1]] = []

    for edge in tuples:
        distance = distance_between_points(edge[1], edge[0])
        if len(graph[edge[0]]) == 0:
            graph[edge[0]].append([edge[1], distance])
        else:
            found = False
            for node in graph[edge[0]]:
                if node[0] == edge[1]:
                    found = True
            if not found:
                graph[edge[0]].append([edge[1], distance])

        if len(graph[edge[1]]) == 0:
            graph[edge[1]].append([edge[0], distance])
        else:
            found = False
            for node in graph[edge[1]]:
                if node[0] == edge[0]:
                    found = True
            if not found:
                graph[edge[1]].append([edge[0], distance])
    
    return graph

def find_minimum_edge(edges: dict):
    min_edge = None
    min_weight = 10**10
    for node in edges:
        if edges[node][1] < min_weight:
            min_edge = (edges[node][0], node)
            min_weight = edges[node][1]
    
    return min_edge

def find_removed_edges(minimum_spanning_tree: list, edges: list):
    removed = []

    for edge in edges:
        lottery_number = randint(0, 100)
        valid = True
        if edge in minimum_spanning_tree:
            valid = False
        if (edge[1], edge[0]) in minimum_spanning_tree:
            valid = False
        if lottery_number < 87:
            valid = False
        if valid:
            removed.append(edge)
    
    return removed