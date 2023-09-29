"""
At the moment this program visualises Delaunay triangulation with Bowyer-Watson algorithm.
The algorithm doesn't work if the the nodes end up forming an approximately straight line.
In this case it returns an empty list. I don't know if there is a way to fix this problem.
With larger inputs (about 10+ nodes) the algorithm appears to work 99% of the time.
The variable "NODE_COUNT" equals to the number of nodes given to the algorithm.
"""

import sys
import pygame
from prim import prims_algorithm
from bowyerwatson import bowyer_watson
import tools
import plotting
from classes.triangleclass import Triangle
from classes.roomclass import generate_rooms
from classes.hallwayclass import generate_hallways

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 400

""" NODE_COUNT equals to the number of nodes given to the algorithm"""
NODE_COUNT = 12
X_MIN = 100
X_MAX = DISPLAY_WIDTH - 100
Y_MIN = 50
Y_MAX = DISPLAY_HEIGHT - 50
display_center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

"""
Hard coded coordinates for the super triangle. I might add a function for randomly generating
a super triangle later.
"""
super_coordinates = [(-10, -400), (1500, 300), (-10, 1200)]

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

"""
visualising with pygame
"""

def dungeon_generator():
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Welcome to the Dungeon")
    font = pygame.font.SysFont("Arial", 16)

    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                sys.exit()

        display.fill((0, 0, 0))

        coordinates = [
            (382, 214),
            (320, 74),
            (447, 292),
            (503, 58),
            (610, 279),
            (134, 118),
            (105, 271),
            (657, 133),
            (278, 199),
            (260, 341),
            (539, 161),
            (700, 340)
        ]
        #coordinates = tools.generate_coordinates(NODE_COUNT, X_MIN, X_MAX, Y_MIN, Y_MAX)
        
        for c in coordinates:
            pygame.draw.circle(display, BLUE, c, 4)
            # text = font.render(f'{c}', True, GREEN)
            # display.blit(text, c)

        pygame.display.flip()
        pygame.time.wait(300)

        t = Triangle(super_coordinates[0], super_coordinates[1], super_coordinates[2], display)
        t.plot()

        triangulation = bowyer_watson(coordinates, display)
        edges = tools.unique_edges(triangulation)
        minimum_spanning_tree = prims_algorithm(triangulation)

        for triangle in triangulation:
            triangle.plot()

        #pygame.display.flip()
        #pygame.time.wait(300)

        display.fill((0, 0, 0))
        for c in coordinates:
            pygame.draw.circle(display, BLUE, c, 4)
            #print(c)

        plotting.plot_mst(minimum_spanning_tree, display, GREEN)
        removed_edges = tools.find_removed_edges(minimum_spanning_tree, edges)

        #pygame.display.flip()
        #pygame.time.wait(300)
        all_edges = minimum_spanning_tree
        for edge in removed_edges:
            all_edges.append(edge)
            pygame.draw.line(display, GREEN, edge[0], edge[1])

        dungeon_graph = tools.create_graph(all_edges)
        #for key, value in dungeon_graph.items():
        #    print(f"{key}: {value}")
        #    for each in value:
        #        pygame.draw.line(display, RED, key, each[0])

        #pygame.display.flip()
        #pygame.time.wait(300)

        rooms = generate_rooms(coordinates, display)
        for room in rooms:
            room.plot()

        pygame.display.flip()
        pygame.time.wait(3000)
        display.fill((0, 0, 0))

        hallways = generate_hallways(dungeon_graph, rooms, display)
        for h in hallways:
            h.plot()
            
        for room in rooms:
            room.plot()

        pygame.display.flip()
        pygame.time.wait(10000)
        break

if __name__ == '__main__':
    dungeon_generator()
