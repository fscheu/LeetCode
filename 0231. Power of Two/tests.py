import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        a = Solution()
        self.assertEqual(a.isPowerOfTwo(1),True)

    def test_two(self):
        a = Solution()
        self.assertEqual(a.isPowerOfTwo(16),True)

    def test_3(self):
        a = Solution()
        self.assertEqual(a.isPowerOfTwo(3),False)


unittest.main()
