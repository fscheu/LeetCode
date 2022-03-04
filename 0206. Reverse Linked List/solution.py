from shared import linked_list
class Solution:
    def reverseList(self, head: linked_list.ListNode):

        def revL(head: linked_list.ListNode, prev=None):
            
            if not head:
                return prev
            else:
                h = head.next
                head.next = prev
                return revL(h, head)
            
        return revL(head)
    
