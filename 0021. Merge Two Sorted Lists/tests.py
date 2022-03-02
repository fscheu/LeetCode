import unittest
from solution import Solution

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):

        list1 = [1,2,4]
        list2 = [1,3,4]
        target = [1,1,2,3,4,4]
        a = Solution()
        self.assertEqual(a.mergeTwoLists(list1,list2),target)
    
    def test_two(self):
        list1 = []
        list2 = []
        target = []
        a = Solution()
        self.assertEqual(a.mergeTwoLists(list1,list2),target)

    def test_3(self):
        list1 = []
        list2 = [0]
        target = [0]
        a = Solution()
        self.assertEqual(a.mergeTwoLists(list1,list2),target)


unittest.main()

#[-1,0,3,5,9,12]
#9