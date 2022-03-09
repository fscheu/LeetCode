import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        s = "abcabcbb"
        target = 3
        a = Solution()
        self.assertEqual(a.lengthOfLongestSubstring(s),target)
    
    def test_two(self):
        s = "bbbbb"
        target = 1
        a = Solution()
        self.assertEqual(a.lengthOfLongestSubstring(s),target)

    def test_3(self):
        s = "pwwkew"
        target = 3
        a = Solution()
        self.assertEqual(a.lengthOfLongestSubstring(s),target)

unittest.main()

#[-1,0,3,5,9,12]
#9