import unittest
from random import randint
from classes.hallwayclass import *
from classes.roomclass import Room

class TestHallway(unittest.TestCase):
    def test__room_overlap_horizontal(self):
        room = Room((100, 100), 50, 50, 1)

        for i in range(500):
            y_coordinate = randint(51, 149)
            start = (randint(0, 40), y_coordinate)
            end = (randint(160, 300), y_coordinate)

            self.assertTrue(room_overlap_horizontal(start, end, room))
    
    def test_room_overlap_vertical(self):
        room = Room((500, 500), 50, 50, 1)

        for i in range(500):
            x_coordinate = randint(451, 549)
            start = (x_coordinate, randint(0, 440))
            end = (x_coordinate, randint(560, 800))

            self.assertTrue(room_overlap_vertical(start, end, room))