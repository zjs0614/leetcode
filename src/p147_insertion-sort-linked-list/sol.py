# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        new_head, head = head, head.next
        new_head.next = None
        while head is not None:
            next_node = head.next
            head.next = None

            if head.val <= new_head.val:
                head.next = new_head
                new_head = head
            else:    
                node = new_head
                while node.next is not None and head.val > node.next.val and head.val > node.val:
                    node = node.next
                node.next, head.next = head, node.next
            head = next_node
        return new_head