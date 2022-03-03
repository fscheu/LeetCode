import unittest
from solution import Solution
import shared.trees as trees

class SolutionTestCase(unittest.TestCase):
    """ Tests for Solution """

    def test_one(self):
        t1 = trees.to_binary_tree([1,3,2,5])
        t2 = trees.to_binary_tree([2,1,3,None,4,None,7])
        target = trees.to_binary_tree([3,4,5,5,4,None,7])
        a = Solution()
        self.assertEqual(a.mergeTrees(t1,t2),target)

    def test_two(self):
        t1 = trees.to_binary_tree([1])
        t2 = trees.to_binary_tree([1,2])
        target = trees.to_binary_tree([2,2])
        a = Solution()
        self.assertEqual(a.mergeTrees(t1,t2),target)


unittest.main()

#[-1,0,3,5,9,12]
#9