import unittest

from solution import Solution, Version

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        v = Version(4)
        n = 5
        a = Solution(v)
        self.assertEqual(a.firstBadVersion(n),4)
    
    def test_two(self):
        v = Version(1)
        n = 1
        a = Solution(v)
        self.assertEqual(a.firstBadVersion(n),1)

    def test_3(self):
        v = Version(2)
        n = 3
        a = Solution(v)
        self.assertEqual(a.firstBadVersion(n),2)


unittest.main()