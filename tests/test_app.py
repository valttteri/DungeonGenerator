import unittest
import xmlrunner
import app

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

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'),
    failfast=False, buffer=False, catchbreak=False, exit=False)