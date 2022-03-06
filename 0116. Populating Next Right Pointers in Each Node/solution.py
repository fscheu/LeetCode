from shared import trees

class Solution:
    def connect(self, root: trees.Node):
        
        if root:
            queue = [root]
            while queue:
                node = queue.pop()
                if node.left:
                    node.left.next = node.right
                    if node.next:
                        node.right.next = node.next.left
                    queue.append(node.left)
                    queue.append(node.right)
        return root