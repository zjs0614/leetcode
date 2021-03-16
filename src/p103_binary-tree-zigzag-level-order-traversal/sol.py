# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue1, queue2 = [root], []

        while len(queue1) > 0 or len(queue2) > 0:
            current_list = []
            if len(queue1) > 0:
                while len(queue1) > 0:
                    node = queue1.pop()
                    current_list.append(node.val)
                    if node.left is not None:
                        queue2.append(node.left)
                    if node.right is not None:
                        queue2.append(node.right)
            elif len(queue2) > 0:
                while len(queue2) > 0:
                    node = queue2.pop()
                    current_list.append(node.val)
                    if node.right is not None:
                        queue1.append(node.right)
                    if node.left is not None:
                        queue1.append(node.left)
            res.append(current_list)
        return res
