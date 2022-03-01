import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        mat = [[0,0,0],[0,1,0],[0,0,0]]
        target = [[0,0,0],[0,1,0],[0,0,0]]
        a = Solution()
        self.assertEqual(a.updateMatrix(mat),target)
    
    def test_two(self):
        mat = [[0,0,0],[0,1,0],[1,1,1]]
        target = [[0,0,0],[0,1,0],[1,2,1]]
        a = Solution()
        self.assertEqual(a.updateMatrix(mat),target)

    def test_3(self):
        mat = [[0,0,1,0,1,1,1,0,1,1],[1,1,1,1,0,1,1,1,1,1],[1,1,1,1,1,0,0,0,1,1],[1,0,1,0,1,1,1,0,1,1],[0,0,1,1,1,0,1,1,1,1],[1,0,1,1,1,1,1,1,1,1],[1,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,1,1],[1,1,1,0,1,1,0,1,0,1],[1,0,1,1,1,0,1,1,1,0]]
        target = [[0,0,1,0,1,2,1,0,1,2],[1,1,2,1,0,1,1,1,2,3],[2,1,2,1,1,0,0,0,1,2],[1,0,1,0,1,1,1,0,1,2],[0,0,1,1,1,0,1,1,2,3],[1,0,1,2,1,1,1,2,1,2],[1,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,1,2],[1,1,1,0,1,1,0,1,0,1],[1,0,1,1,1,0,1,2,1,0]]
        a = Solution()
        self.assertEqual(a.updateMatrix(mat),target)



unittest.main()
