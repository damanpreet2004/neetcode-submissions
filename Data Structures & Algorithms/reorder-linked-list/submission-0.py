# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        l1 = head
        l2 = head
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        curr = l1.next
        l1.next = None 

        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        l = head
        m = prev
        while m:
            t1 = l.next
            t2 = m.next

            l.next = m
            m.next = t1

            l = t1
            m = t2

