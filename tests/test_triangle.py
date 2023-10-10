import unittest
from classes.triangleclass import Triangle

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle_1 = Triangle((1, 5), (4, 5), (7, 2), 1)
        self.triangle_2 = Triangle((1, 5), (4, 5), (7, 2), 1)
        self.triangle_3 = Triangle((2, 6), (8, 10), (5, 16), 1)
        self.triangle_4 = Triangle((40, 50), (400, 300), (50, 200), 1)
        self.triangle_5 = Triangle((-20, -100), (300, -50), (300, 300), 1)
    
    def tearDown(self):
        del self.triangle_1
        del self.triangle_2
        del self.triangle_3
        del self.triangle_4
        del self.triangle_5

    def test_triangle_nodes(self):
        triangle = self.triangle_1
        self.assertEqual(triangle.show_nodes()[0], (1, 5))
        self.assertEqual(triangle.show_nodes()[1], (4, 5))
        self.assertEqual(triangle.show_nodes()[2], (7, 2))

    def test_triangle_edges(self):
        triangle = self.triangle_1
        self.assertEqual(triangle.show_edges()[0][0], (1, 5))
        self.assertEqual(triangle.show_edges()[0][1], (4, 5))
        self.assertEqual(triangle.show_edges()[1][0], (4, 5))
        self.assertEqual(triangle.show_edges()[1][1], (7, 2))
        self.assertEqual(triangle.show_edges()[2][0], (7, 2))
        self.assertEqual(triangle.show_edges()[2][1], (1, 5))
    
    def test_equality(self):
        self.assertEqual(self.triangle_1, self.triangle_1)
    
    def test_show_id(self):
        self.assertNotEqual(self.triangle_1.show_id(), self.triangle_2.show_id())
        self.assertNotEqual(self.triangle_2.show_id(), self.triangle_3.show_id())
    
    def test_circum_center(self):
        self.assertEqual(self.triangle_1.circum_center(), (2.5, 0.5))
        self.assertEqual(self.triangle_3.circum_center(), (2.875, 11.188))
        self.assertEqual(self.triangle_4.circum_center(), (264.903, 110.34))
        self.assertEqual(self.triangle_5.circum_center(), (108.75, 125))

    def test_cc_radius(self):
        self.assertEqual(self.triangle_1.cc_radius(), 4.743)
        self.assertEqual(self.triangle_3.cc_radius(), 5.261)
        self.assertEqual(self.triangle_4.cc_radius(), 232.857)
        self.assertEqual(self.triangle_5.cc_radius(), 259.233)