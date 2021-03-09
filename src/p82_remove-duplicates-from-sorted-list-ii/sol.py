# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        num_count = [0] * 201
        while head is not None:
            num_count[head.val + 100] += 1
            head = head.next
        res, node = None, None
        for i, count in enumerate(num_count):
            if count == 1:
                if res is None:
                    res = ListNode(i - 100)
                    node = res
                else:
                    node.next = ListNode(i - 100)
                    node = node.next
        return res