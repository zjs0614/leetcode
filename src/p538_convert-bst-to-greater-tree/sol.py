# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is not None:
            self.convert(root, 0)
        return root

    def convert(self, root, addition):
        right_sum, left_sum = 0, 0
        if root.right is not None:
            right_sum = self.convert(root.right, addition)
        if root.left is not None:
            left_sum = self.convert(root.left, root.val + addition + right_sum)

        total_sum = root.val + left_sum + right_sum
        root.val += addition + right_sum
        return total_sum