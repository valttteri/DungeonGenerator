import unittest
from random import randint
from tools import generate_coordinates
from classes.roomclass import generate_rooms

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.DISPLAY_WIDTH = 900
        self.DISPLAY_HEIGHT = 500
    
    def test_generate_rooms(self):
        for i in range(500):
            node_count = randint(3, 12)
            coordinates = generate_coordinates(
            node_count,
            self.DISPLAY_WIDTH,
            self.DISPLAY_HEIGHT
        )
        rooms = generate_rooms(coordinates, 1)

        self.assertEqual(len(rooms), node_count)