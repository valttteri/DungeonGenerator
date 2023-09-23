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
        self.height = height
        self.width = width
        self.room_center = center
        self.room_id = next(self.new_id)
        self.display = display

        self.top_left = (self.room_center[0] - self.width, self.room_center[1] + self.height)
        self.bottom_left = (self.room_center[0] - self.width, self.room_center[1] - self.height)
        self.top_right = (self.room_center[0] + self.width, self.room_center[1] + self.height)
        self.bottom_right = (self.room_center[0] + self.width, self.room_center[1] - self.height)

        self.top = [self.top_left, self.top_right]
        self.bottom = [self.bottom_left, self.bottom_right]
        self.left = [self.top_left, self.bottom_left]
        self.right = [self.top_right, self.bottom_right]

    def __str__(self):
        return f"Room {self.room_id}, center at {self.room_center}"

    def __repr__(self):
        return f"Room {self.room_id}, center at {self.room_center}"

    def center(self):
        return self.room_center

    def plot(self):
        pygame.draw.polygon(self.display, LIGHTGRAY, [self.top_left, self.top_right, self.bottom_right, self.bottom_left])
        pygame.draw.line(self.display, GRAY, self.top[0], self.top[1])
        pygame.draw.line(self.display, GRAY, self.left[0], self.left[1])
        pygame.draw.line(self.display, GRAY, self.right[0], self.right[1])
        pygame.draw.line(self.display, GRAY, self.bottom[0], self.bottom[1])

def generate_rooms(coordinates: list, display):
    room_list = []

    for coordinate in coordinates:


        if len(room_list) == 0:
            room_list.append(Room(coordinate, randint(15, 45), randint(15, 60), display))
            continue
        #height_valid = True
        #width_valid = True
        room_height = randint(15, 45)
        room_width = randint(15, 60)
        new_room = Room(coordinate, room_height, room_width, display)
        room_list.append(new_room)
    
    return room_list