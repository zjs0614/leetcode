# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        n1 = head
        n2 = head.next if head != None else None
        while n1 != None and n2 != None:
            if n1 == n2:
                return True
            n1 = n1.next
            n2 = n2.next.next if n2.next != None else None

        return False