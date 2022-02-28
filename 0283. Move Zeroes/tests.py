import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        nums = [1]
        target = [1]
        a = Solution()
        a.moveZeroes(nums)
        self.assertEqual(nums,target)
    
    def test_two(self):
        nums = [0,1,0,3,12]
        target = [1,3,12,0,0]
        a = Solution()
        a.moveZeroes(nums)
        self.assertEqual(nums,target)

    def test_3(self):
        nums = [0]
        target = [0]
        a = Solution()
        a.moveZeroes(nums)
        self.assertEqual(nums,target) 


unittest.main()

#[-1,0,3,5,9,12]
#9