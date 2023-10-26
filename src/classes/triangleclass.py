import tools
import itertools
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

class Triangle:
    """Class representing a triangle"""

    new_id = itertools.count()

    def __init__(self, node_a: tuple, node_b: tuple, node_c: tuple, display):
        self.node_a = node_a
        self.node_b = node_b
        self.node_c = node_c
        self.display = display

        self.id = next(self.new_id)
        self.circumcenter = tools.find_circumcenter([self.node_a, self.node_b, self.node_c])
        self.circum_circles_radius = tools.distance_between_points(
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

    def show_id(self):
        return self.id

    def show_edges(self):
        return self.triangle_edges

    def show_nodes(self):
        return self.nodes

    def circum_center(self):
        return self.circumcenter

    def cc_radius(self):
        return self.circum_circles_radius

    def plot(self):
        for edge in self.triangle_edges:
            pygame.draw.line(self.display, GREEN, edge[0], edge[1])

    def circum_circle(self):
        pygame.draw.circle(
            self.display, BLUE, self.circumcenter, radius=self.circum_circles_radius, width=2
        )
