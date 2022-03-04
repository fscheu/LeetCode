from shared import linked_list

class Solution:
    def mergeTwoLists(self, l1: linked_list.ListNode, l2: linked_list.ListNode):
        
        if not l1 and not l2: return None
        
        res = linked_list.ListNode(None)
        seg = res
        while l1 and l2:
            if l1.val < l2.val:
                seg.next = l1
                l1 = l1.next
            else:
                seg.next = l2
                l2 = l2.next
            seg = seg.next
            
        if l1 or l2:
            seg.next = (l1 or l2)
        return res.next