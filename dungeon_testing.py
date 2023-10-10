"""This file is for testing the program"""

import sys
import pygame
from prim import prims_algorithm
from bowyerwatson import bowyer_watson
import tools
import plotting
from classes.roomclass import generate_rooms
from classes.hallwayclass import generate_hallways, plot_hallways

DISPLAY_WIDTH = 900
DISPLAY_HEIGHT = 500
"""NODE_COUNT equals to the number of nodes given to the algorithm"""
NODE_COUNT = 4
X_MIN = 100
X_MAX = DISPLAY_WIDTH - 100
Y_MIN = 50
Y_MAX = DISPLAY_HEIGHT - 50
display_center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

super_coordinates = [(-DISPLAY_WIDTH**2, -DISPLAY_HEIGHT**2), (DISPLAY_WIDTH**2, 0), (0, DISPLAY_HEIGHT**2)]

"""Hard coded coordinates for testing"""
        #coordinates = [
        #    (382, 214),
        #    (320, 74),
        #    (447, 292),
        #    (503, 58),
        #    (610, 279),
        #    (134, 118),
        #    (105, 271),
        #    (657, 133),
        #    (278, 199),
        #    (260, 341),
        #    (539, 161),
        #    (700, 340)
        #]

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

"""Visualising with pygame"""
def testing_generator():
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Welcome to the Dungeon")

    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                sys.exit()
        display.fill((0, 0, 0))

        """Create all essential components"""
        coordinates = tools.generate_coordinates(NODE_COUNT, DISPLAY_WIDTH, DISPLAY_HEIGHT)

        if coordinates == 1:
            print("")
            print("Couldn't find a spot for each room")
            print("Reduce the amount of rooms or increase the display size")
            sys.exit()

        triangulation = bowyer_watson(coordinates, super_coordinates, display)
        edges = tools.unique_edges(triangulation)

        minimum_spanning_tree = prims_algorithm(triangulation)
        removed_edges = tools.find_removed_edges(minimum_spanning_tree, edges)
        all_edges = minimum_spanning_tree + removed_edges
        dungeon_graph = tools.create_graph(all_edges)
        rooms = generate_rooms(coordinates, display)

        if rooms == 1:
            print("")
            print("Found a spot for each room but they do not fit")
            print("Reduce the amount of rooms or increase the display size")
            sys.exit()

        hallways = generate_hallways(dungeon_graph, rooms, display)

        """Start by plotting the coordinates"""
        for node in coordinates:
            pygame.draw.circle(display, BLUE, node, 4)

        #pygame.display.flip()
        #pygame.time.wait(500)

        for triangle in triangulation:
            triangle.plot()

        #pygame.display.flip()
        #pygame.time.wait(500)
        #display.fill((0, 0, 0))

        """Plot the minimum spanning tree"""
        for node in coordinates:
            pygame.draw.circle(display, BLUE, node, 4)
        plotting.plot_mst(minimum_spanning_tree, display, GREEN)

        #pygame.display.flip()
        #pygame.time.wait(500)

        """Plot the removed edges"""
        for edge in removed_edges:
            pygame.draw.line(display, GREEN, edge[0], edge[1])

        #pygame.display.flip()
        #pygame.time.wait(500)

        """Plot the rooms"""
        for room in rooms:
            room.plot()

        #pygame.display.flip()
        #pygame.time.wait(2000)
        display.fill((0, 0, 0))

        """Plot the hallways and then plot the rooms on top of them"""
        plot_hallways(display, hallways, rooms)
        for room in rooms:
            room.plot()

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    testing_generator()