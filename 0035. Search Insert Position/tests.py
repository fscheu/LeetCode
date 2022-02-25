import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        nums = [1,3,5,6]
        target = 5
        a = Solution()
        self.assertEqual(a.searchInsert(nums,target),2)
    
    def test_two(self):
        nums = [1,3,5,6]
        target = 2
        a = Solution()
        self.assertEqual(a.searchInsert(nums,target),1)

    def test_3(self):
        nums = [1,3,5,6]
        target = 7
        a = Solution()
        self.assertEqual(a.searchInsert(nums,target),4)


unittest.main()

#[-1,0,3,5,9,12]
#9