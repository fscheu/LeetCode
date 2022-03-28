import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        s = "ABAB"
        k = 2
        target = 4
        a = Solution()
        self.assertEqual(a.characterReplacement(s,k),target)
    
    def test_two(self):
        s = "AABABBA"
        k = 1
        target = 4
        a = Solution()
        self.assertEqual(a.characterReplacement(s,k),target)


unittest.main()
