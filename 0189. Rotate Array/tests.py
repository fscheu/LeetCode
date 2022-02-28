import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        nums = [1,2]
        k = 3
        target = [2,1]
        a = Solution()
        a.rotate(nums,k)
        self.assertEqual(nums,target)
    
    def test_two(self):
        nums = [1,2,3,4,5,6,7]
        k = 3
        target = [5,6,7,1,2,3,4]
        a = Solution()
        a.rotate(nums,k)
        self.assertEqual(nums,target)

    def test_3(self):
        nums = [-1,-100,3,99]
        k = 2
        target = [3,99,-1,-100]
        a = Solution()
        a.rotate(nums,k)
        self.assertEqual(nums,target)   


unittest.main()

#[-1,0,3,5,9,12]
#9