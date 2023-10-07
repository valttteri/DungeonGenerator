"""
This program generates a dungeon using Bowyer-Watson's and Prim's algorithms.
By default the program uses a 900px/500px display where it generates 12 rooms
connected by hallways. Rooms can't be generated within 80 pixels of each other and
therefore large inputs will cause an infinite loop. 

If you want to see how the program works with other inputs, you can change the variables
DISPLAY_WIDTH, DISPLAY_HEIGHT and NODE_COUNT.  
"""

from ctypes import WinDLL, wintypes
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
NODE_COUNT = 15
X_MIN = 100
X_MAX = DISPLAY_WIDTH - 100
Y_MIN = 50
Y_MAX = DISPLAY_HEIGHT - 50
display_center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
super_coordinates = [(-DISPLAY_WIDTH**2, -DISPLAY_HEIGHT**2), (DISPLAY_WIDTH**2, 0), (0, DISPLAY_HEIGHT**2)]


GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

"""Visualising with pygame"""

def main():
    while True:
        print("Welcome to the dungeon!")

        user_input = input("Generate a dungeon? (y/n)")

        if user_input not in ["y", "n"]:
            continue
        if user_input == "y":
            print("Press R key to generate a new dungeon")
            print("Press Q to quit")
            dungeon_generator()
        if user_input == "n":
            break

def dungeon_generator():
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Welcome to the Dungeon")
    clock = pygame.time.Clock()

    """The following forces the pygame window on top"""
    pin_window()

    display.fill((0, 0, 0))

    """Create all essential components"""
    coordinates = tools.generate_coordinates(NODE_COUNT, DISPLAY_WIDTH, DISPLAY_HEIGHT)
    triangulation = bowyer_watson(coordinates, super_coordinates, display)
    edges = tools.unique_edges(triangulation)

    minimum_spanning_tree = prims_algorithm(triangulation)
    removed_edges = tools.find_removed_edges(minimum_spanning_tree, edges)
    all_edges = minimum_spanning_tree + removed_edges

    dungeon_graph = tools.create_graph(all_edges)
    rooms = generate_rooms(coordinates, display)
    hallways = generate_hallways(dungeon_graph, rooms, display)

    """Start by plotting the coordinates"""
    for node in coordinates:
        pygame.draw.circle(display, BLUE, node, 4)

    pygame.display.flip()
    pygame.time.wait(500)

    """Plot Delaunay triangulation"""
    for triangle in triangulation:
        triangle.plot()

    pygame.display.flip()
    pygame.time.wait(500)
    display.fill((0, 0, 0))

    """Plot the minimum spanning tree"""
    for node in coordinates:
        pygame.draw.circle(display, BLUE, node, 4)
    plotting.plot_mst(minimum_spanning_tree, display, GREEN)

    pygame.display.flip()
    pygame.time.wait(500)

    """Plot the removed edges"""
    for edge in removed_edges:
        pygame.draw.line(display, GREEN, edge[0], edge[1])

    pygame.display.flip()
    pygame.time.wait(500)

    """Plot the rooms"""
    for room in rooms:
        room.plot()

    pygame.display.flip()
    pygame.time.wait(500)
    display.fill((0, 0, 0))

    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                sys.exit()
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_r:
                    dungeon_generator()
                if action.key == pygame.K_q:
                    sys.exit()

        """Plot the hallways and then plot the rooms on top of them"""
        plot_hallways(display, hallways, rooms)
        for room in rooms:
            room.plot()
        pygame.display.flip()
        clock.tick(10)

def pin_window():
    window = pygame.display.get_wm_info()['window']
    user32 = WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [
        wintypes.HWND,
        wintypes.HWND,
        wintypes.INT,
        wintypes.INT,
        wintypes.INT,
        wintypes.INT,
        wintypes.UINT
    ]
    user32.SetWindowPos(window, -1, 50, 50, 0, 0, 0x0001)

if __name__ == '__main__':
    main()
