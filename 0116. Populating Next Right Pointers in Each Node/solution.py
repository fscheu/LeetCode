
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node):
        
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