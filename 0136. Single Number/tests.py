import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        a = Solution()
        self.assertEqual(a.singleNumber([2,2,1]),1)

    def test_two(self):
        a = Solution()
        self.assertEqual(a.singleNumber([4,1,2,1,2]),4)

    def test_3(self):
        a = Solution()
        self.assertEqual(a.singleNumber([1]),1)


unittest.main()
