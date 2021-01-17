# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head != None and head.next != None:
            next_node = head.next
            end = self.reverseList(next_node)
            next_node.next = head
            head.next = None
            return end
        else:
            return head
        