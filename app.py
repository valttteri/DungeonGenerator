"""
This program generates a dungeon using Bowyer-Watson's and Prim's algorithms.
By default the program uses a 800px/400px display where it generates 12 rooms
connected by hallways. Rooms can't be generated within 100 pixels of each other and
therefore inputs larger than 15 will most likely cause an infinite loop. 

If you want to see how the algorithm works on larger inputs, comment out lines 55-58 
in the tools.py file (the 100 pixel rule) and lines 122-123 & 131-132 (room plotting) 
in this file. Then you can play with the "NODE_COUNT" variable which equals to the 
number of nodes given to the algorithm.
"""

import sys
import pygame
from prim import prims_algorithm
from bowyerwatson import bowyer_watson
import tools
import plotting
from classes.triangleclass import Triangle
from classes.roomclass import generate_rooms
from classes.hallwayclass import generate_hallways, plot_hallways

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 400

"""NODE_COUNT equals to the number of nodes given to the algorithm"""
NODE_COUNT = 12
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

def dungeon_generator():
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
        triangulation = bowyer_watson(coordinates, display)
        edges = tools.unique_edges(triangulation)
        super_triangle = Triangle(super_coordinates[0], super_coordinates[1], super_coordinates[2], display)

        minimum_spanning_tree = prims_algorithm(triangulation)
        removed_edges = tools.find_removed_edges(minimum_spanning_tree, edges)
        all_edges = minimum_spanning_tree + removed_edges

        dungeon_graph = tools.create_graph(all_edges)
        rooms = generate_rooms(coordinates, display)
        hallways = generate_hallways(dungeon_graph, rooms, display)

        """Start by plotting the coordinates"""
        for node in coordinates:
            pygame.draw.circle(display, BLUE, node, 4)

        #pygame.display.flip()
        #pygame.time.wait(300)

        """Plot the super triangle and the Delaunay triangulation"""
        super_triangle.plot()
        for triangle in triangulation:
            triangle.plot()

        #pygame.display.flip()
        #pygame.time.wait(1000)
        #display.fill((0, 0, 0))

        """Plot the minimum spanning tree"""
        for node in coordinates:
            pygame.draw.circle(display, BLUE, node, 4)
        plotting.plot_mst(minimum_spanning_tree, display, GREEN)

        #pygame.display.flip()
        #pygame.time.wait(1000)

        """Plot the removed edges"""
        for edge in removed_edges:
            pygame.draw.line(display, GREEN, edge[0], edge[1])

        #pygame.display.flip()
        #pygame.time.wait(300)

        """Plot the rooms"""
        for room in rooms:
            room.plot()

        pygame.display.flip()
        pygame.time.wait(1000)
        display.fill((0, 0, 0))

        """Plot the hallways and then plot the rooms on top of them"""
        plot_hallways(display, hallways, rooms)
        for room in rooms:
            room.plot()

        pygame.display.flip()
        pygame.time.wait(300)

if __name__ == '__main__':
    dungeon_generator()
