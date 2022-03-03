# Definition for a Node with a pointer to other node.
from turtle import left


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left = None if self.left is None else self.left.val
        right = None if self.right is None else self.right.val
        return '(D:{}, L:{}, R:{})'.format(self.val, left, right)

    def __str__(self) -> str:
        return str(self.val)
    
    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.val == other.val and self.left == other.left and self.right == other.right

def to_binary_tree(items: list[int]) -> TreeNode:
    """Create BT from list of values."""
    n = len(items)
    if n == 0:
        return None

    def inner(index: int = 0) -> TreeNode:
        """Closure function using recursion bo build tree"""
        if n <= index or items[index] is None:
            return None

        node = TreeNode(items[index])
        node.left = inner(2 * index + 1)
        node.right = inner(2 * index + 2)
        return node

    return inner()