# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2
        carry = 0
        res = ListNode(0)
        curr = res
        while list1 is not None or list2 is not None:

            v1 = list1.val if list1 is not None else 0
            v2 = list2.val if list2 is not None else 0

            t_sum = v1 + v2 + carry
            carry = t_sum // 10

            curr.next = ListNode(t_sum % 10)
            curr = curr.next

            if list1 is not None:list1 = list1.next 
            if list2 is not None:list2 = list2.next 

        if carry > 0:
            curr.next = ListNode(carry)
        return res.next

