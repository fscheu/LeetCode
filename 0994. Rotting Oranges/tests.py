import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        oranges = [[2,1,1],[1,1,0],[0,1,1]]
        target = 4
        a = Solution()
        self.assertEqual(a.orangesRotting(oranges),target)

    def test_two(self):
        oranges = [[2,1,1],[0,1,1],[1,0,1]]
        target = -1
        a = Solution()
        self.assertEqual(a.orangesRotting(oranges),target)

    def test_3(self):
        oranges = [[0,2]]
        target = 0
        a = Solution()
        self.assertEqual(a.orangesRotting(oranges),target)

    def test_4(self):
        oranges = [[0]]
        target = 0
        a = Solution()
        self.assertEqual(a.orangesRotting(oranges),target)



unittest.main()
