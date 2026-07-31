# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupprev = dummy

        while True:
            kth = groupprev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
            
            if not kth:
                    break
            
            groupNext = kth.next

            prev = groupNext
            curr = groupprev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp
            
        return dummy.next

                                

