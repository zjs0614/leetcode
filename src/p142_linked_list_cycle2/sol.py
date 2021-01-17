# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        n1 = head
        n2 = head.next if head != None else None
        while n1 is not None and n2 is not None and n1 != n2:
            n1 = n1.next
            n2 = n2.next.next if n2.next != None else None

        if n1 is None or n2 is None:
            return None

        n1 = head
        n2 = n2.next
        while n1 != n2:
            n1 = n1.next
            n2 = n2.next

        return n1