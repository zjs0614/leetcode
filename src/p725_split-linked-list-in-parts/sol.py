# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        count = 0
        node = root
        while node is not None:
            node = node.next
            count += 1
        size = int(count / k)
        extra = count % k
        count = 0
        res = []
        node = root
        while node is not None:
            group_size = size + (1 if extra > 0 else 0)
            if count == 0:
                res.append(node)
            if count < group_size - 1:
                node = node.next
                count += 1
            if count == group_size - 1:
                count = 0
                next_node = node.next
                node.next = None
                node = next_node
                extra -= 1
        while len(res) < k:
            res.append(None)
        return res