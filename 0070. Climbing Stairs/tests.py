import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        n = 1
        target = 1
        a = Solution()
        self.assertEqual(a.climbStairs(n),target)
    
    def test_two(self):
        n = 2
        target = 2
        a = Solution()
        self.assertEqual(a.climbStairs(n),target)

    def test_3(self):
        n = 35
        target = 14930352
        a = Solution()
        self.assertEqual(a.climbStairs(n),target)

unittest.main()

#[-1,0,3,5,9,12]
#9