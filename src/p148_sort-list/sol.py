# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        length = 1
        while True:
            left, right = head, head
            prev_tail = None
            while True:
                for _ in range(length):
                    if right is None:
                        break
                    right = right.next
                if prev_tail is None and right is None:
                    return left
                root, tail, follow = self.merge(left, right, length)
                if prev_tail is not None:
                    prev_tail.next = root
                else:
                    head = root
                left, right, prev_tail = follow, follow, tail
                if left is None:
                    break
            length = length * 2
    
    def merge(self, left, right, length):
        left_count, right_count = 0,0
        root, cur = None, None
        while left_count < length or right_count < length:
            min_node, left_count, right_count, left, right = self.getMinNode(left, right, left_count, right_count, length)
            if min_node is not None:
                if root is None:
                    root = min_node
                    cur = min_node
                else:

                    cur.next, min_node.next = min_node, None
                    cur = cur.next
            else:
                break

        return root, cur, right

    def getMinNode(self, left, right, left_count, right_count, length):
        if left is None and right is None:
            return None, left_count + 1, right_count + 1, None, None
        if left_count < length and right_count < length:
            if right is None:
                return left, left_count + 1, right_count, left.next, None
            else:
                return (left, left_count + 1, right_count, left.next, right) if left.val < right.val else (right, left_count, right_count + 1, left, right.next)

        elif left_count >= length:
            if right is not None:
                return right, left_count, right_count + 1, None, right.next
            else:
                return None, left_count, right_count, None, None
        elif right_count >= length:
            return left, left_count + 1, right_count, left.next, right
            
