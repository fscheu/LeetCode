import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        nums = [3,24,50,79,88,150,345]
        target = 200
        res = [3,6]
        a = Solution()
        self.assertEqual(a.twoSum(nums,target),res)
    
    def test_two(self):
        nums = [2,7,11,15]
        target = 9
        res = [1,2]
        a = Solution()
        self.assertEqual(a.twoSum(nums,target),res)

    def test_3(self):
        nums = [2,3,4]
        target = 6
        res = [1,3]
        a = Solution()
        self.assertEqual(a.twoSum(nums,target),res)

    def test_4(self):
        nums = [-1,0]
        target = -1
        res = [1,2]
        a = Solution()
        self.assertEqual(a.twoSum(nums,target),res)

    def test_5(self):
        nums = [1,2,3,4,4,9,56,90]
        target = 8
        res = [4,5]
        a = Solution()
        self.assertEqual(a.twoSum(nums,target),res)


unittest.main()

#[-1,0,3,5,9,12]
#9