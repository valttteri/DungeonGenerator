"""
At the moment this program visualises Delaunay triangulation with Bowyer-Watson algorithm.
The algorithm doesn't work if the the nodes end up forming an approximately straight line.
In this case it returns an empty list. I don't know if there is a way to fix this problem.
With larger inputs (about 10+ nodes) the algorithm appears to work 99% of the time.
The variable "NODE_COUNT" equals to the number of nodes given to the algorithm.

In order to run the tests, comment out the three lines under the variable DISPLAY_HEIGHT
and the while-loop on the bottom of the file.
"""

import itertools
import sys
from random import randint
from math import sqrt
import pygame
from prim import primsAlgorithm, findRemovedEdges, uniqueEdges

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 400

# comment out the following three lines for testing
pygame.init()
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Welcome to the Dungeon")

# NODE_COUNT equals to the number of nodes given to the algorithm
NODE_COUNT = 10
X_MIN = 100
X_MAX = DISPLAY_WIDTH - 100
Y_MIN = 50
Y_MAX = DISPLAY_HEIGHT - 50
display_center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

font = pygame.font.SysFont("Arial", 16)

"""
Hard coded coordinates for the super triangle. I might add a function for randomly generating
a super triangle later.
"""
super_coordinates = [(-10, -400), (1500, 300), (-10, 1200)]

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Triangle:
    """Class representing a triangle"""

    new_id = itertools.count()

    def __init__(self, node_a: tuple, node_b: tuple, node_c: tuple):
        self.node_a = node_a
        self.node_b = node_b
        self.node_c = node_c

        self.id = next(self.new_id)
        self.circumcenter = find_circumcenter([self.node_a, self.node_b, self.node_c])
        self.circum_circles_radius = distance_between_points(
            self.circumcenter, self.node_a
        )

        self.nodes = [self.node_a, self.node_b, self.node_c]

        self.triangle_edges = [
            [self.node_a, self.node_b],
            [self.node_b, self.node_c],
            [self.node_c, self.node_a],
        ]

    def __str__(self):
        return f"Triangle with edges {self.triangle_edges}"

    def __repr__(self):
        return f"Triangle with edges {self.triangle_edges}"

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            return "triangles only"

        return self.id == other.id

    def show_ID(self):
        return self.id

    def showEdges(self):
        return self.triangle_edges

    def showNodes(self):
        return self.nodes

    def circumCenter(self):
        return self.circumcenter

    def ccRadius(self):
        return self.circum_circles_radius

    def plot(self):
        for edge in self.triangle_edges:
            pygame.draw.line(display, GREEN, edge[0], edge[1])

    def circumCircle(self):
        pygame.draw.circle(
            display, RED, self.circumcenter, radius=self.circum_circles_radius, width=2
        )


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


# Plot a triangle's circumcircle
def plot_circum_circle(coordinates: list):
    """Plot a circumcircle of a triangle"""

    centerpoint = find_circumcenter(coordinates)
    radius = distance_between_points(centerpoint, coordinates[0])

    pygame.draw.circle(display, RED, centerpoint, radius=radius, width=2)


# Calculate the distance between two points
def distance_between_points(point_a: tuple, point_b: tuple):
    """Calculate the distance between two nodes"""

    distance = sqrt((point_b[0] - point_a[0]) ** 2 + (point_b[1] - point_a[1]) ** 2)
    return distance


# Generate coordinates in a way to avoid duplicates
def generate_coordinates(count: int):
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

    # g=[
    #    (674, 166),
    #    (388, 324),
    #    (549, 268),
    #    (361, 223),
    #    (491, 173),
    #    (658, 185)
    # ]#
    return coordinate_list


# Check if two separate triangles have a common edge
def are_edges_equal(edge_1: list, edge_2: list):
    """Check if two separate edges are equal"""

    return (edge_1[0] == edge_2[0] and edge_1[1] == edge_2[1]) or (
        edge_1[0] == edge_2[1] and edge_1[1] == edge_2[0]
    )


def bowyer_watson(nodelist: list):
    """
    Bowyer-Watson algorithm for generating a Delaunay triangulation. Steps:

    1. Create an empty list for the triangulation. Create a 'super triangle'
    i.e. a triangle which is large enough to contain every single node inside it.
    Add the super triangle into the triangulation.

    2. Start the process of adding each node into the triangulation

    3. Check if the node is inside one or more circumcircles.
    All triangles which have a node inside their circumcircle are now 'bad' triangles.

    4. Go through each triangle in bad_triangles. If a triangle has an edge
    which is not shared with another triangle, add it to the list named "polygon".

    5. Remove each bad triangle from the triangulation.

    6. Create a new triangle between the node and every edge in the list polygon.

    7. Check if there are triangles in the triangulation that share a node
    or an edge with the original super triangle. If so, remove these triangles.
    """
    # Step 1.
    triangulation = []
    super_triangle = Triangle(
        super_coordinates[0], super_coordinates[1], super_coordinates[2]
    )
    super_triangle_nodes = []

    # super_triangle_edges = super_triangle.showEdges()
    super_triangle_nodes = super_triangle.showNodes()

    triangulation.append(super_triangle)

    # Step 2.
    for node in nodelist:
        bad_triangles = []

        # Step 3.
        for triangle in triangulation:
            circumcenter = triangle.circumCenter()
            circum_circles_radius = triangle.ccRadius()

            distance = distance_between_points(node, circumcenter)
            if distance <= circum_circles_radius:
                bad_triangles.append(triangle)

        polygon = []

        # Step 4.
        for bad_triangle in bad_triangles:
            edges = bad_triangle.showEdges()
            for edge in edges:
                found = False
                for other_triangle in bad_triangles:
                    other_triangles_edges = other_triangle.showEdges()
                    if bad_triangle == other_triangle:
                        continue

                    for other_edge in other_triangles_edges:
                        if are_edges_equal(other_edge, edge):
                            found = True
                if not found:
                    polygon.append(edge)

        # Step 5.
        for bad_triangle in bad_triangles:
            triangulation.remove(bad_triangle)

        # Step 6.
        for edge in polygon:
            new_triangle = Triangle(edge[0], edge[1], node)
            triangulation.append(new_triangle)

    # Step 7.
    remove_triangles = []
    for triangle in triangulation:
        nodes = triangle.showNodes()
        found = False
        for n in nodes:
            if found:
                continue
            if n in super_triangle_nodes:
                found = True
                remove_triangles.append(triangle)
    for triangle in remove_triangles:
        triangulation.remove(triangle)

    return triangulation


def plot_mst(coordinates: list):
    """This function plots a minimum spanning tree"""

    for coordinate in coordinates:
        pygame.draw.line(display, GREEN, coordinate[0], coordinate[1])


# visualising with pygame
# comment out the entire loop for testing

while True:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            sys.exit()

    display.fill((0, 0, 0))

    coordinates = generate_coordinates(NODE_COUNT)

    for c in coordinates:
        pygame.draw.circle(display, BLUE, c, 4)
        # text = font.render(f'{c}', True, GREEN)
        # display.blit(text, c)

    t = Triangle(super_coordinates[0], super_coordinates[1], super_coordinates[2])
    t.plot()

    triangulation = bowyer_watson(coordinates)
    unique_edges = uniqueEdges(triangulation)
    minimum_spanning_tree = primsAlgorithm(triangulation)

    for triangle in triangulation:
        triangle.plot()

    pygame.display.flip()
    pygame.time.wait(1000)

    display.fill((0, 0, 0))
    for c in coordinates:
        pygame.draw.circle(display, BLUE, c, 4)

    plot_mst(minimum_spanning_tree)
    removed_edges = findRemovedEdges(minimum_spanning_tree, unique_edges)
    for e in removed_edges:
        print(e)

    pygame.display.flip()
    pygame.time.wait(2000)

    for edge in removed_edges:
        pygame.draw.line(display, GREEN, edge[0], edge[1])

    # pygame.display.flip()
    # pygame.time.wait(10000)
    break
