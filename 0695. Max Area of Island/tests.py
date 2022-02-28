import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        island = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        target = 6
        a = Solution()
        self.assertEqual(a.maxAreaOfIsland(island),target)
    
    def test_two(self):
        island = [[0,0,0,0,0,0,0,0]]
        target = 0
        a = Solution()
        self.assertEqual(a.maxAreaOfIsland(island),target)

    def test_3(self):
        island = [[1]]
        target = 1
        a = Solution()
        self.assertEqual(a.maxAreaOfIsland(island),target)


unittest.main()

#[-1,0,3,5,9,12]
#9