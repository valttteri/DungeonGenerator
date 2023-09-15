import unittest
import xmlrunner
import app

'''
In order to run the tests, each line in app.py referring to pygame must be commented out
'''

class TestApp(unittest.TestCase):
    def test_findCircumCenter(self):
        self.assertEqual(app.findCircumcenter([(1,1), (3,5), (7,3)]), (4,2))
        result = app.findCircumcenter([(2,4), (3,-7), (7,-2)])
        x = float(str(result[0])[:5])
        y = float(str(result[1])[:7])
        self.assertEqual(x, 1.377)
        self.assertEqual(y, -1.602)
    
    def test_distanceBetweenPoints(self):
        self.assertEqual(app.distanceBetweenPoints((1, 1), (5, 1)), 4)
        self.assertEqual(app.distanceBetweenPoints((2, 3), (2, -2)), 5)
        self.assertEqual(round(app.distanceBetweenPoints((3, 5), (7, 3)), 6), 4.472136)
    
    def test_areEdgesEqual(self):
        self.assertTrue(app.areEdgesEqual([(3, 4), (7, 6)], [(3, 4), (7, 6)]))
        self.assertTrue(app.areEdgesEqual([(3, 4), (7, 6)], [(7, 6), (3, 4)]))
        self.assertFalse(app.areEdgesEqual([(3, 4), (7, 6)], [(3, 4), (7, 4)]))
        self.assertFalse(app.areEdgesEqual([(3, 4), (7, 6)], [(7, 6), (1, 1)]))

    def test_triangle_nodes(self):
        triangle = app.Triangle((1, 5), (4, 5), (7, 2))
        self.assertEqual(triangle.showNodes()[0], (1, 5))
        self.assertEqual(triangle.showNodes()[1], (4, 5))
        self.assertEqual(triangle.showNodes()[2], (7, 2))
    
    def test_triangle_edges(self):
        triangle = app.Triangle((1, 5), (4, 5), (7, 2))
        self.assertEqual(triangle.showEdges()[0][0], (1, 5))
        self.assertEqual(triangle.showEdges()[0][1], (4, 5))
        self.assertEqual(triangle.showEdges()[1][0], (4, 5))
        self.assertEqual(triangle.showEdges()[1][1], (7, 2))
        self.assertEqual(triangle.showEdges()[2][0], (7, 2))
        self.assertEqual(triangle.showEdges()[2][1], (1, 5))

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'),
    failfast=False, buffer=False, catchbreak=False, exit=False)