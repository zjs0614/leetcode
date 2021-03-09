# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        res, prev, stop, current, last = head, None, None, head, None
        while current is not None:
            if current.val < x:
                if prev is None:
                    prev = current
                    res = current
                    if stop is not None:
                        last.next = current.next
                else:
                    prev.next = current
                    prev = current
                    if stop is not None:
                        last.next = current.next
            else:
                if stop is None:
                    stop = current
                last = current
            current = current.next
        if prev is not None:
            prev.next = stop
        return res