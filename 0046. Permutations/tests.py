import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        nums = [1,2,3]
        target = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        a = Solution()
        self.assertEqual(a.permute(nums),target)
    
    def test_two(self):
        nums = [0,1]
        target = [[0,1],[1,0]]
        a = Solution()
        self.assertEqual(a.permute(nums),target)

    def test_3(self):
        nums = [1]
        target = [[1]]
        a = Solution()
        self.assertEqual(a.permute(nums),target)

    def test_4(self):
        nums = [1,10,7,4]
        target = [[1,10,7,4],[1,10,4,7],[1,7,10,4],[1,7,4,10],[1,4,10,7],[1,4,7,10],
                [10,1,7,4],[10,1,4,7],[10,7,1,4],[10,7,4,1],[10,4,1,7],[10,4,7,1],
                [7,1,10,4],[7,1,4,10],[7,10,1,4],[7,10,4,1],[7,4,1,10],[7,4,10,1],
                [4,1,10,7],[4,1,7,10],[4,10,1,7],[4,10,7,1],[4,7,1,10],[4,7,10,1]]
        a = Solution()
        self.assertEqual(a.permute(nums),target)

unittest.main()

#[-1,0,3,5,9,12]
#9