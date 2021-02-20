# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        a, b = self.max_rob(root)
        return max(a, b)
    
    def max_rob(self, root):
        left, left_next, right, right_next = 0, 0, 0, 0
        if root.left is not None:
            left, left_next = self.max_rob(root.left)
        if root.right is not None:
            right, right_next = self.max_rob(root.right)
        return root.val+left_next+right_next, max(left+right, left+right_next, left_next+right, left_next+right_next)