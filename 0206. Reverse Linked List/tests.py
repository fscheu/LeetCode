import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        list1 = [1,2,3,4,5]
        target = [5,4,3,2,1]
        a = Solution()
        self.assertEqual(a.reverseList(list1),target)
    
    def test_two(self):
        list1 = [1,2]
        target = [2,1]
        a = Solution()
        self.assertEqual(a.reverseList(list1),target)

    def test_3(self):
        list1 = []
        target = []
        a = Solution()
        self.assertEqual(a.reverseList(list1),target)


unittest.main()

#[-1,0,3,5,9,12]
#9