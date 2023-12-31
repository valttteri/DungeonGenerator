from math import sqrt
from random import randint
import pygame

DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 500

super_coordinates = [(-DISPLAY_WIDTH**2, -DISPLAY_HEIGHT**2), (DISPLAY_WIDTH**2, 0), (0, DISPLAY_HEIGHT**2)]

def find_circumcenter(coordinate_list: list):
    """Find cartesian coordinates of a triangle's circumcenter."""

    first_x = coordinate_list[0][0]
    first_y = coordinate_list[0][1]
    second_x = coordinate_list[1][0]
    second_y = coordinate_list[1][1]
    third_x = coordinate_list[2][0]
    third_y = coordinate_list[2][1]

    divider = 2 * (
        first_x * (second_y - third_y)
        + second_x * (third_y - first_y)
        + third_x * (first_y - second_y)
    )

    result_x = (
        (first_x * first_x + first_y * first_y) * (second_y - third_y)
        + (second_x * second_x + second_y * second_y) * (third_y - first_y)
        + (third_x * third_x + third_y * third_y) * (first_y - second_y)
    ) / divider

    result_y = (
        (first_x * first_x + first_y * first_y) * (third_x - second_x)
        + (second_x * second_x + second_y * second_y) * (first_x - third_x)
        + (third_x * third_x + third_y * third_y) * (second_x - first_x)
    ) / divider

    return round(result_x, 3), round(result_y, 3)

def distance_between_points(point_a: tuple, point_b: tuple):
    """Calculate the distance between two nodes"""

    distance = round(sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2), 3)
    return distance

def generate_coordinates(count: int, width: int, height: int):
    """Generate coordinates for the triangulation"""
    min_x = 100
    max_x = width - 100
    min_y = 50
    max_y = height - 50

    coordinate_list = []
    counter = 0
    while len(coordinate_list) < count:
        valid = True
        x_coordinate = randint(min_x, max_x)
        y_coordinate = randint(min_y, max_y)
        candidate = (x_coordinate, y_coordinate)

        if candidate in coordinate_list:
            valid = False

        if valid:
            for coordinate in coordinate_list:
                if distance_between_points(candidate, coordinate) < 100:
                    valid = False

        if valid:
            coordinate_list.append(candidate)
        counter += 1
        if counter > 1000:
            return 1

    return coordinate_list

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

def create_graph(edges: list):
    """This function creates a graph based on some edges. The graph's structure is
    basically {node coordinates: [neighbor1 coordinates, distance to neighbor], [n2, distance],...}
    
    Keyword arguments:
        edges (list) -- array of edges (tuple, tuple) found in a triangulation

    Returns
        graph (dict) -- a graph based on the edges
    """
    graph = {}

    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []

    for edge in edges:
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
