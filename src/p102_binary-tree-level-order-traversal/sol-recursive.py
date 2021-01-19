# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.find(root, 0, result)
        return result
    def find(self, root: TreeNode, level: int, result: List):
        if root is None:
            return
        if len(result) <= level:
            result.append([root.val])
        else:
            result[level].append(root.val)
        self.find(root.left, level + 1, result)
        self.find(root.right, level + 1, result)