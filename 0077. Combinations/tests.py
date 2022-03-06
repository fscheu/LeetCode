import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        n = 4
        k = 2
        target = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        a = Solution()
        self.assertEqual(a.combine(n,k),target)
    
    def test_two(self):
        n = 1
        k = 1
        target = [[1]]
        a = Solution()
        self.assertEqual(a.combine(n,k),target)

    def test_3(self):
        n = 5
        k = 2
        target = [[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
        a = Solution()
        self.assertEqual(a.combine(n,k),target)


unittest.main()

#[-1,0,3,5,9,12]
#9