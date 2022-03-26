import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        s = "Let's take LeetCode contest"
        target = "s'teL ekat edoCteeL tsetnoc"
        a = Solution()
        self.assertEqual(a.reverseWords(s),target)
    
    def test_two(self):
        s = "God Ding"
        target = "doG gniD"
        a = Solution()
        self.assertEqual(a.reverseWords(s),target)


unittest.main()

