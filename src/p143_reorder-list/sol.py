# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack, node = [], head
        while node is not None:
            stack.append(node)
            node = node.next
        if len(stack) <= 2:
            return head
        res, pop_side_flag = None, True
        while len(stack) > 0:
            node = stack.pop(0) if pop_side_flag else stack.pop()
            pop_side_flag = not(pop_side_flag)
            if res is None:
                head = node
                res = node
            else:
                res.next = node
                res = node
        res.next = None
        return head