"""
This program generates a dungeon using Bowyer-Watson's and Prim's algorithms.
By default the program uses a 900px/500px display where it generates 12 rooms
connected by hallways. Rooms can't be generated within 80 pixels of each other and
therefore large inputs will cause an infinite loop. 
 
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

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

def main():
    print(
        "Welcome to the dungeon generator! Let's start by defining the size \n"
        "\n"
        "Recommendation: width - 900px, height - 500px, rooms - 15 \n"
        "Limits: width > 400px, height > 300px, rooms > 2 \n"
    )
    while True:

        width = int(input("Choose a width: "))

        if width < 400:
            print(f"{width} is too narrow")
            continue

        height = int(input("Choose a height: "))

        if height < 300:
            print(f"{height} is too low")
            continue

        nodes = int(input("How many rooms: "))

        if nodes < 3:
            print(f"{nodes} is not enough")
            continue

        print("")
        print("Press 1 to generate a new dungeon")
        print("Press 2 to give a new input")
        print("Press 3 to quit")
        
        program = dungeon_generator(nodes, width, height)
        if program == 1:
            continue

def dungeon_generator(NODE_COUNT: int, DISPLAY_WIDTH: int, DISPLAY_HEIGHT):
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Welcome to the Dungeon")
    clock = pygame.time.Clock()

    """The following forces the pygame window on top"""
    pin_window()

    display.fill((0, 0, 0))

    """Create all essential components"""
    super_coordinates = [(-DISPLAY_WIDTH**2, -DISPLAY_HEIGHT**2), (DISPLAY_WIDTH**2, 0), (0, DISPLAY_HEIGHT**2)]
    coordinates = tools.generate_coordinates(NODE_COUNT, DISPLAY_WIDTH, DISPLAY_HEIGHT)

    if coordinates == 1:
        print("")
        print("Couldn't find a spot for each room")
        print("Reduce the amount of rooms or increase the display size")
        print("")
        return 1

    triangulation = bowyer_watson(coordinates, super_coordinates, display)
    edges = tools.unique_edges(triangulation)

    minimum_spanning_tree = prims_algorithm(triangulation)
    removed_edges = tools.find_removed_edges(minimum_spanning_tree, edges)
    all_edges = minimum_spanning_tree + removed_edges

    dungeon_graph = tools.create_graph(all_edges)
    rooms = generate_rooms(coordinates, display)

    if rooms == 1:
        print("")
        print("Couldn't find a spot for each room")
        print("Reduce the amount of rooms or increase the display size")
        print("")
        return 1

    hallways = generate_hallways(dungeon_graph, rooms, display)

    """Start by plotting the coordinates"""
    for node in coordinates:
        pygame.draw.circle(display, BLUE, node, 4)

    pygame.display.flip()
    pygame.time.wait(1000)

    """Plot Delaunay triangulation"""
    for triangle in triangulation:
        triangle.plot()

    pygame.display.flip()
    pygame.time.wait(1000)
    display.fill((0, 0, 0))

    """Plot the minimum spanning tree"""
    for node in coordinates:
        pygame.draw.circle(display, BLUE, node, 4)
    plotting.plot_mst(minimum_spanning_tree, display, GREEN)

    pygame.display.flip()
    pygame.time.wait(1000)

    """Plot the removed edges"""
    if len(removed_edges) != 0:
        for edge in removed_edges:
            pygame.draw.line(display, GREEN, edge[0], edge[1])

        pygame.display.flip()
        pygame.time.wait(1000)

    """Plot the rooms"""
    for room in rooms:
        room.plot()

    pygame.display.flip()
    pygame.time.wait(1000)
    display.fill((0, 0, 0))

    """Plot the hallways"""
    plot_hallways(display, hallways, rooms)

    while True:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                sys.exit()
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_1:
                    dungeon_generator(NODE_COUNT, DISPLAY_WIDTH, DISPLAY_HEIGHT)
                if action.key == pygame.K_2:
                    main()
                if action.key == pygame.K_3:
                    sys.exit()

        """Plot the hallways and then plot the rooms on top of them"""
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
