import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        s = "a1b2"
        target = ["a1b2","a1B2","A1b2","A1B2"]
        a = Solution()
        self.assertEqual(a.letterCasePermutation(s),target)
    
    def test_two(self):
        s = "3z4"
        target = ["3z4","3Z4"]
        a = Solution()
        self.assertEqual(a.letterCasePermutation(s),target)

    def test_3(self):
        s = "chau"
        target = ["chau","chaU","chAu","chAU","cHau","cHaU","cHAu","cHAU","Chau"
            ,"ChaU","ChAu","ChAU","CHau","CHaU","CHAu","CHAU"]
        a = Solution()
        self.assertEqual(a.letterCasePermutation(s),target)

unittest.main()

#[-1,0,3,5,9,12]
#9