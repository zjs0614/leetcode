# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head != None and head.next != None:
            next_node = head.next
            head.next = self.swapPairs(next_node.next)
            next_node.next = head
            return next_node
        else:
            return head