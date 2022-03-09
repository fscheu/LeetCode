import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        s = ["h","e","l","l","o"]
        target = ["o","l","l","e","h"]
        a = Solution()
        a.reverseString(s)
        self.assertEqual(s,target)
    
    def test_two(self):
        s = ["H","a","n","n","a","h"]
        target = ["h","a","n","n","a","H"]
        a = Solution()
        a.reverseString(s)
        self.assertEqual(s,target)


unittest.main()

#[-1,0,3,5,9,12]
#9