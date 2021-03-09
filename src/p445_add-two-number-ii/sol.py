# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1 is not None:
            s1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2.append(l2.val)
            l2 = l2.next
        last = None
        addition = False
        while len(s1) > 0 or len(s2) > 0:
            l1 = s1.pop() if len(s1) > 0 else 0
            l2 = s2.pop() if len(s2) > 0 else 0
            total = (l1 + l2) + (1 if addition else 0)
            node = ListNode(total % 10)
            addition = total >= 10
            node.next = last
            last = node
        if addition:
            node = ListNode(1)
            node.next = last
            last = node
        return last