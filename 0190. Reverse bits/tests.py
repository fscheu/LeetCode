import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        a = Solution()
        self.assertEqual(a.reverseBits(43261596),964176192)

    def test_two(self):
        a = Solution()
        self.assertEqual(a.reverseBits(4294967293),3221225471)


unittest.main()
