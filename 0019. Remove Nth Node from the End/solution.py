from shared import linked_list as ll

class Solution:
    def removeNthFromEnd(self, head: ll.ListNode, n: int) -> ll.ListNode:
        
        fast = slow = head
        ix = 0
        while fast.next:
            if ix == n:
                slow = slow.next
            else:
                ix = ix+1
            fast = fast.next
        
        #print(slow.val)
        if ix < n:
            head = head.next
        else:
            if slow.next:
                slow.next = slow.next.next
            else:
                head = None
            
        return head