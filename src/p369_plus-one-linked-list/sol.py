# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        stack = []
        new_head = ListNode(0)
        new_head.next = head
        node = new_head
        while node is not None:
            if node.val != 9:
                stack = [node]
            else:
                stack.append(node)
            node = node.next
        while len(stack) > 1:
            node = stack.pop()
            node.val = 0
        first_node = stack.pop()
        first_node.val = first_node.val + 1
        if new_head.val == 1:
            return new_head
        else:
            return head