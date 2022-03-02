# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: ListNode):

        def revL(head: ListNode, prev=None):
            
            if not head:
                return prev
            else:
                h = head.next
                head.next = prev
                return revL(h, head)
            
        return revL(head)
    
