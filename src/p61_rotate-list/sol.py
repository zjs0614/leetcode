# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        node = head
        original_k = k
        slow = head
        while k > 0 and node is not None:
            node = node.next
            k -= 1
        if k == 0 and node is None:
            return head
        elif node is None:
            size = original_k - k
            k = original_k % size
            node = head
            while k > 0:
                node = node.next
                k -= 1
        while node.next is not None:
            node = node.next
            slow = slow.next
            
        node.next = head
        head = slow.next
        slow.next = None
        return head
