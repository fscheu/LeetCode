import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        nums = [-4,-1,0,3,10]
        target = [0,1,9,16,100]
        a = Solution()
        self.assertEqual(a.sortedSquares(nums),target)
    
    def test_two(self):
        nums = [-7,-3,2,3,11]
        target = [4,9,9,49,121]
        a = Solution()
        self.assertEqual(a.sortedSquares(nums),target)

    def test_3(self):
        nums = [1,3,5,6]
        target = [1,9,25,36]
        a = Solution()
        self.assertEqual(a.sortedSquares(nums),target)


unittest.main()

#[-1,0,3,5,9,12]
#9