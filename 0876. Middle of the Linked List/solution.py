from shared import linked_list as ll
class Solution:
    def middleNode(self, head: ll.ListNode) -> ll.ListNode:
        
        p = head
        l = []
        while p:
            l.append(p)
            p = p.next
        
        mid = len(l)//2
        return l[mid]