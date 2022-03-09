import unittest
from solution import Solution
from shared import linked_list as ll

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        list1 = [1,2,3,4,5]
        target = [3,4,5]
        ll_1 = ll.to_linked_list(list1)
        ll_t = ll.to_linked_list(target)
        a = Solution()
        self.assertEqual(a.middleNode(ll_1),ll_t)
    
    def test_two(self):
        list1 = [1,2,3,4,5,6]
        target = [4,5,6]
        ll_1 = ll.to_linked_list(list1)
        ll_t = ll.to_linked_list(target)
        a = Solution()
        self.assertEqual(a.middleNode(ll_1),ll_t)
    
    def test_3(self):
        list1 = [1,2,3]
        target = [2,3]
        ll_1 = ll.to_linked_list(list1)
        ll_t = ll.to_linked_list(target)
        a = Solution()
        self.assertEqual(a.middleNode(ll_1),ll_t)

unittest.main()

#[-1,0,3,5,9,12]
#9