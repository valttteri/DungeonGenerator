import itertools
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

class Hallway:
    """Class for visualizing a hallway"""
    new_id = itertools.count()

    def __init__(self, start_room: object, end_room: object, display):
        self.start_room = start_room
        self.end_room = end_room
        self.display = display
        self.hallway_id = next(self.new_id)
        self.start = start_room.center()
        self.end = end_room.center()

        self.start_room_width = start_room.width()
        self.start_room_height = start_room.height()

        self.end_room_width = end_room.width()
        self.end_room_height = end_room.height()

    def start_node(self):
        return self.start
    
    def end_node(self):
        return self.end
        
    def __str__(self):
        return f"Hallway between rooms {self.start_room.center()}, and {self.end_room.center()}"

    def __repr__(self):
        return f"Hallway between rooms {self.start_room.center()}, and {self.end_room.center()}"

def plot_hallways(display, hallways: list, rooms:list):
    """
    Function for plotting the hallways. Right now I'm working on plotting the L-shaped hallways
    correctly. They shouldnät go through rooms
    """
    for hallway in hallways:
        start = hallway.start_node()
        end = hallway.end_node()
        overlap = False

        #plot a horizontal line
        if abs(start[0] - end[0]) < 20:
            pygame.draw.line(display, RED, start, (start[0], end[1]), width=4)
            continue
        #plot a vertical line
        if abs(start[1] - end[1]) < 20:
            pygame.draw.line(hallway.display, RED, start, (end[0], start[1]), width=4)
            continue
        
        for room in rooms:
            if room.center() == start or room.center() == end:
                continue
            if room_overlap(start, end, room):
                overlap = True
                
        if overlap:
            pygame.draw.line(display, RED, start, (start[0], end[1]), width=4)
            pygame.draw.line(display, RED, (start[0], end[1]), end, width=4)
            continue

        pygame.draw.line(display, RED, start, (end[0], start[1]), width=4)
        pygame.draw.line(display, RED, (end[0], start[1]), end, width=4)

def room_overlap(start_xy: tuple, end_xy: tuple, room: object):
    """Check if a hallway goes through a room"""
    #horizontal
    if (room.center()[1] - room.height() < start_xy[1] < room.center()[1] + room.height()
        and room.center()[0] + room.width() > start_xy[0]
        and room.center()[0] - room.width() < end_xy[0]
        or room.center()[0] - room.width() < end_xy[0]
        and room.center()[0] + room.width() > start_xy[0]
    ):
        return True

    #vertical
    if (room.center()[0] + room.width() > end_xy[0] > room.center()[0] - room.width()
        and room.center()[1] + room.height() > start_xy[1]
        and room.center()[1] - room.height() < end_xy[1]
        or room.center()[1] - room.height() < end_xy[1]
        and room.center()[1] + room.height() > start_xy[1] 
    ):
        return True

    return False

def generate_hallways(graph: dict, rooms: list, display):
    """Function for generating hallway objects"""
    used_nodes = set()
    hallways = []

    for start_node, end_nodes in graph.items():
        if start_node in used_nodes:
            continue
        for end_node in end_nodes:
            if end_node[0] in used_nodes:
                continue
            starting_room, ending_room = find_hallways_rooms(start_node, end_node[0], rooms)
            hallways.append(Hallway(starting_room, ending_room, display))
        used_nodes.add(start_node)

    return hallways

def find_hallways_rooms(start_node, end_node, rooms):
    """This function finds out which rooms are located at the ends of a hallway"""
    starting_room = None
    ending_room = None

    for room in rooms:
        if room.center() == start_node:
            starting_room = room
        elif room.center() == end_node:
            ending_room = room

    if starting_room is not None is not ending_room:
        return starting_room, ending_room
    return f"no hallway found between nodes {start_node} and {end_node}"
