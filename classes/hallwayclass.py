import itertools
from random import randint
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

    def midpoint(self):
        return ((self.start[0]+self.end[0])//2, (self.start[1]+self.end[1])//2)

    def start_node(self):
        return self.start

    def end_node(self):
        return self.end

    def start_width(self):
        return self.start_room_width

    def start_height(self):
        return self.start_room_height

    def end_width(self):
        return self.end_room_width

    def end_height(self):
        return self.end_room_height

    def __str__(self):
        return f"Hallway between rooms {self.start_room.center()}, and {self.end_room.center()}"

    def __repr__(self):
        return f"Hallway between rooms {self.start_room.center()}, and {self.end_room.center()}"

def plot_hallways(display, hallways: list, rooms:list):
    """Function for plotting the hallways"""
    overlap = False
    horiz_change = False
    vert_change = False
    for hallway in hallways:
        start = hallway.start_node()
        end = hallway.end_node()
        start_width = hallway.start_width()
        start_height = hallway.start_height()
        end_width = hallway.end_width()
        end_height = hallway.end_height()
        midpoint = hallway.midpoint()

        #plot a vertical hallway
        if (
        start[0] - start_width < midpoint[0] < start[0] + start_width
        and end[0] - end_width < midpoint[0] < end[0] + end_width
        ):
            plot_vertical_hallway(hallway, rooms, display)
            continue

        #plot a horizontal hallway
        if (
            start[1] - start_height < midpoint[1] < start[1] + start_height
            and end[1] - end_height < midpoint[1] < end[1] + end_height
        ):
            plot_horizontal_hallway(hallway, rooms, display)
            continue
        
        #plot an L-shaped hallway
        plotted = False
        for room in rooms:
            if plotted:
                continue
            if room.center() == start or room.center() == end:
                continue
            if room_overlap_horizontal(start, end, room) or room_overlap_vertical(start, end, room):
                """
                If there's a room on the way, the hallway is plotted on the opposite side.
                In an unlucky case that might also lead to overlapping but it reduces 
                the chance of this happening
                """
                pygame.draw.line(display, LIGHTGRAY, start, (start[0], end[1]), width=4)
                pygame.draw.line(display, LIGHTGRAY, (start[0], end[1]), end, width=4)
                plotted = True
                overlap = True
            else:
                pygame.draw.line(display, LIGHTGRAY, start, (end[0], start[1]), width=4)
                pygame.draw.line(display, LIGHTGRAY, (end[0], start[1]), end, width=4)
                plotted = True
        if not plotted:
            pygame.draw.line(display, LIGHTGRAY, start, (end[0], start[1]), width=4)
            pygame.draw.line(display, LIGHTGRAY, (end[0], start[1]), end, width=4)
        
    return overlap, horiz_change, vert_change

def plot_vertical_hallway(hallway: object, rooms:list, display):
    #define the range of x-coordinates where a hallway can be generated
    start = hallway.start_node()
    end = hallway.end_node()
    start_width = hallway.start_width()
    end_width = hallway.end_width()

    possible_range = [max(start[0]-start_width, end[0]-end_width), min(start[0]+start_width, end[0]+end_width)]
    common_range = define_vertical_range(start, end, possible_range[0], possible_range[1], rooms)
    
    if start[0] in common_range and end[0] in common_range:
        pygame.draw.line(display, LIGHTGRAY, start, (start[0], end[1]), width=4)
        return

    if common_range[-1] - common_range[0] > 20:
        x_coordinate = randint(common_range[0]+6, common_range[1]-6)
    else:
        x_coordinate = (common_range[0] + common_range[1])//2

    pygame.draw.line(display, LIGHTGRAY, (x_coordinate, start[1]), (x_coordinate, end[1]), width=4)
    return

def plot_horizontal_hallway(hallway: object, rooms: list, display):
    """define the range of y-coordinates where a hallway can be generated"""
    start = hallway.start_node()
    end = hallway.end_node()
    start_height = hallway.start_height()
    end_height = hallway.end_height()

    possible_range = [max(start[1]-start_height, end[1]-end_height), min(start[1]+start_height, end[1]+end_height)]
    common_range = define_horizontal_range(start, end, possible_range[0], possible_range[1], rooms)

    if start[1] in common_range and end[1] in common_range:
        pygame.draw.line(display, LIGHTGRAY, start, (end[0], start[1]), width=4)
        return

    if common_range[-1] - common_range[0] > 20:
        y_coordinate = randint(common_range[0]+6, common_range[1]-6)
    else:
        y_coordinate = (common_range[0] + common_range[1])//2

    pygame.draw.line(display, LIGHTGRAY, (start[0], y_coordinate), (end[0], y_coordinate), width=4)
    return

def define_horizontal_range(start_xy: tuple, end_xy: tuple, min_value: int, max_value: int, rooms: object):
    """check if a horizontal hallway is possibly about to overlap with a room"""
    for room in rooms:
        if start_xy[0] < room.center()[0] < end_xy[0]:
            #the room is above the hallway
            if min_value < room.center()[1] + room.height() < max_value:
                min_value = room.center()[1] + room.height()
                return [min_value, max_value]
            
            #the room is below the hallway
            if min_value < room.center()[1] - room.height() < max_value:
                max_value = room.center()[1] - room.height()
                return [min_value, max_value]
    return [min_value, max_value]

def define_vertical_range(start_xy: tuple, end_xy: tuple, min_value: int, max_value: int, rooms: object):
    """check if a vertical hallway is possibly about to overlap with a room"""
    for room in rooms:
        if start_xy[1] < room.center()[1] < end_xy[1]:
            #the room is to the right of a hallway
            if min_value < room.center()[0] + room.width() < max_value:
                min_value = room.center()[0] + room.width()
                return [min_value, max_value]
            
            #the room is to the left of a hallway
            if min_value < room.center()[0] - room.width() < max_value:
                max_value = room.center()[0] - room.width()
                return [min_value, max_value]
    return [min_value, max_value]

        
def room_overlap_horizontal(start_xy: tuple, end_xy: tuple, room: object):
    """Check if a horizontal hallway goes through a room"""
    #room is in the same y-range
    if room.center()[1] - room.height() < start_xy[1] < room.center()[1] + room.height():
        #room is in the same x-range on the right side
        if room.center()[0] + room.width() > start_xy[0] and room.center()[0] - room.width() < end_xy[0]:
            return True
        #room is in the same x-range on the left side
        if room.center()[0] - room.width() < end_xy[0] and room.center()[0] + room.width() > start_xy[0]:
            return True
    return False

def room_overlap_vertical(start_xy: tuple, end_xy: tuple, room: object):
    """Check if a vertical hallway goes through a room"""
    #room is in the same x-range
    if room.center()[0] + room.width() > end_xy[0] > room.center()[0] - room.width():
        #whole room is above ending node
        if room.center()[1] + room.height() > start_xy[1] and room.center()[1] - room.height() < end_xy[1]:
            return True
        #whole room is below starting node
        if room.center()[1] - room.height() < end_xy[1] and room.center()[1] + room.height() > start_xy[1]:
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
