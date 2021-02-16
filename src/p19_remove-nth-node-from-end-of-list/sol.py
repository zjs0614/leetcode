# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        while fast.next is not None:
            fast = fast.next
            if n > 0:
                n -= 1
            else:
                slow = slow.next
        if n == 0:
            slow.next = slow.next.next
            return head
        elif n == 1:
            return slow.next
