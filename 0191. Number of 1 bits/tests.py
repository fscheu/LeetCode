import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        a = Solution()
        self.assertEqual(a.hammingWeight(11),3)

    def test_two(self):
        a = Solution()
        self.assertEqual(a.hammingWeight(128),1)

    def test_3(self):
        a = Solution()
        self.assertEqual(a.hammingWeight(4294967293),31)


unittest.main()
