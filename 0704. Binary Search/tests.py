import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        nums = [-1,0,3,5,9,12]
        target = 2
        a = Solution()
        self.assertEqual(a.search(nums,target),-1)
    
    def test_two(self):
        nums = [-1,0,3,5,9,12]
        target = 9
        a = Solution()
        self.assertEqual(a.search(nums,target),4)


unittest.main()

#[-1,0,3,5,9,12]
#9