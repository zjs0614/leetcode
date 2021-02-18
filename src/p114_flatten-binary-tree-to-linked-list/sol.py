# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.flatten_next(root)
    
    def flatten_next(self, root):
        if root.right is None and root.left is None:
            return root
        original_right = root.right
        new_right = None
        if root.left is not None:
            new_right = self.flatten_next(root.left)
            root.right = root.left
            new_right.right = original_right
            root.left = None

        if original_right is not None:
            return self.flatten_next(original_right)
        else:
            return new_right