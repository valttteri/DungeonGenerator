import itertools
from random import randint
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

class Room:
    """Class for plotting a room"""

    new_id = itertools.count()

    def __init__(self, center: tuple, height: int, width: int, display):
        self.room_height = height
        self.room_width = width
        self.room_center = center
        self.room_id = next(self.new_id)
        self.display = display

        self.top_left = (self.room_center[0] - self.room_width, self.room_center[1] + self.room_height)
        self.bottom_left = (self.room_center[0] - self.room_width, self.room_center[1] - self.room_height)
        self.top_right = (self.room_center[0] + self.room_width, self.room_center[1] + self.room_height)
        self.bottom_right = (self.room_center[0] + self.room_width, self.room_center[1] - self.room_height)

        self.top = [self.top_left, self.top_right]
        self.bottom = [self.bottom_left, self.bottom_right]
        self.left = [self.top_left, self.bottom_left]
        self.right = [self.top_right, self.bottom_right]

    def __str__(self):
        return f"Room {self.room_id}, center at {self.room_center}"

    def __repr__(self):
        return f"Room {self.room_id}, center at {self.room_center}"
    
    def __eq__(self, other):
        return self.room_id == other.id_number()
    
    def id_number(self):
        return self.room_id

    def width(self):
        return self.room_width

    def height(self):
        return self.room_height

    def center(self):
        return self.room_center

    def plot(self):
        pygame.draw.polygon(self.display, LIGHTGRAY, [self.top_left, self.top_right, self.bottom_right, self.bottom_left])
        pygame.draw.line(self.display, GRAY, self.top[0], self.top[1], width=3)
        pygame.draw.line(self.display, GRAY, self.left[0], self.left[1], width=3)
        pygame.draw.line(self.display, GRAY, self.right[0], self.right[1], width=3)
        pygame.draw.line(self.display, GRAY, self.bottom[0], self.bottom[1], width=3)

def generate_rooms(coordinates: list, display):
    """Function for generating room objects"""
    room_list = []

    for coordinate in coordinates:
        counter = 0
        while True:

            if len(room_list) == 0:
                room_list.append(Room(coordinate, randint(15, 40), randint(15,50), display))
                break

            room_height = randint(20, 40)
            room_width = randint(20, 50)
            valid = True

            for room in room_list:
                if overlaps(room, coordinate, room_height, room_width):
                    valid = False
            if valid:
                new_room = Room(coordinate, room_height, room_width, display)
                room_list.append(new_room)
                break
            counter += 1
            if counter > 100:
                return 1

    return room_list

def overlaps(room: object, center: tuple, height: int, width: int):
    """Return True if two rooms overlap"""

    #vertical
    if room.center()[0] + room.width() + 10 < center[0] - width or center[0] + width + 10 < room.center()[0] - room.width():
        return False

    #horizontal
    if room.center()[1] + room.height() + 10 < center[1] - height or center[1] + height + 10 < room.center()[1] - room.height():
        return False

    return True
