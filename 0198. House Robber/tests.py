import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        nums = [1,2,3,1]
        target = 4
        a = Solution()
        self.assertEqual(a.rob(nums),target)
    
    def test_two(self):
        nums = [2,7,9,3,1]
        target = 12
        a = Solution()
        self.assertEqual(a.rob(nums),target)

    def test_3(self):
        nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112]
        target = 2791
        a = Solution()
        self.assertEqual(a.rob(nums),target)

unittest.main()

#[-1,0,3,5,9,12]
#9