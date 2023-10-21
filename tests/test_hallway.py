import unittest
from random import randint
from classes.hallwayclass import Hallway, room_overlap_horizontal, room_overlap_vertical, generate_hallways
from classes.roomclass import Room, generate_rooms
from tools import generate_coordinates, create_graph, unique_edges
from bowyerwatson import bowyer_watson
from prim import prims_algorithm

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
    
    def test_generate_hallways(self):
        for i in range(500):
            node_count = randint(3, 12)
            height = 500
            width = 900
            coordinates, rooms = coordinates_and_rooms(1, node_count, width, height)
            super_coordinates = [
                (-width**2, -height**2),
                (width**2, 0), (0, height**2)
            ]

            triangulation = bowyer_watson(coordinates, super_coordinates, 1)
            minimum_spanning_tree = prims_algorithm(triangulation)

            dungeon_graph = create_graph(minimum_spanning_tree)
            hallways = generate_hallways(dungeon_graph, rooms, 1)

            self.assertEqual(len(minimum_spanning_tree), len(hallways))
    
    def test_define_vertical_range(self):
        room = Room((500, 500), 50, 50, 1)

def coordinates_and_rooms(display, NODE_COUNT: int, DISPLAY_WIDTH: int, DISPLAY_HEIGHT: int):
    """Make sure that the coordinates are valid for room generation"""
    while True:
        coordinates = generate_coordinates(NODE_COUNT, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        
        if coordinates == 1:
            continue

        rooms = generate_rooms(coordinates, display)

        if rooms == 1:
            continue

        return coordinates, rooms

