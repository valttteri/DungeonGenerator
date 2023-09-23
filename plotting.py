import pygame
import tools

def plot_mst(coordinates: list, display, colour):
    """This function plots a minimum spanning tree"""

    for coordinate in coordinates:
        pygame.draw.line(display, colour, coordinate[0], coordinate[1])

def plot_circum_circle(coordinates: list, display, colour):
    """Plot a circumcircle of a triangle"""

    centerpoint = tools.find_circumcenter(coordinates)
    radius = tools.distance_between_points(centerpoint, coordinates[0])

    pygame.draw.circle(display, colour, centerpoint, radius=radius, width=2)