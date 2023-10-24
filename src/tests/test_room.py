import unittest
from random import randint
from tools import generate_coordinates
from classes.roomclass import generate_rooms

class TestRoom(unittest.TestCase):
    """Test the room class"""
    def setUp(self):
        self.display_width = 900
        self.display_height = 500

    def test_generate_rooms(self):
        """Test the generate_rooms function"""
        for i in range(500):
            node_count = randint(3, 12)
            coordinates = generate_coordinates(
            node_count,
            self.display_width,
            self.display_height
        )
        rooms = generate_rooms(coordinates, 1)

        self.assertEqual(len(rooms), node_count)
