import shared.trees as trees

class Solution:
    def mergeTrees(self, root1: trees.TreeNode, root2: trees.TreeNode):
        
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            ret = trees.TreeNode(root1.val + root2.val)
            ret.left = self.mergeTrees(root1.left,root2.left)
            ret.right = self.mergeTrees(root1.right,root2.right)
            return ret