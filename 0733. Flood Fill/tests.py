import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1
        sc = 1
        newColor = 2
        target = [[2,2,2],[2,2,0],[2,0,1]]
        a = Solution()
        self.assertEqual(a.floodFill(image, sr, sc, newColor),target)
    
    def test_two(self):
        image = [[0,0,0],[0,0,0]]
        sr = 0
        sc = 0
        newColor = 2
        target = [[2,2,2],[2,2,2]]
        a = Solution()
        self.assertEqual(a.floodFill(image, sr, sc, newColor),target)

    def test_3(self):
        image = [[0,0,0],[0,1,1]]
        sr = 1
        sc = 1
        newColor = 1
        target = [[0,0,0],[0,1,1]]
        a = Solution()
        self.assertEqual(a.floodFill(image, sr, sc, newColor),target)  


unittest.main()

#[-1,0,3,5,9,12]
#9