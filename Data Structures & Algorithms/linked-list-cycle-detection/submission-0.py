# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
            
        f = head.next
        s = head

        while f and f.next :
            if f.val == s.val:
                return True
            else:
                s = s.next
                f = f.next.next
        return False