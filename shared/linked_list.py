# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
    def __eq__(self,other):
        if self.val == other.val:
            if self.next and other.next:
                return self.next == other.next
            else:
                return True
        return False

def to_linked_list(l) -> ListNode:
    
    if not l: return None
    ret = ListNode(l[0], to_linked_list(l[1:]))
    return ret

    