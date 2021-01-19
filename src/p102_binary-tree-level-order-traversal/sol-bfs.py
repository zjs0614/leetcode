# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            size = len(queue)
            result.append([])
            while size > 0:
                prevNode = queue.pop(0)
                result[-1].append(prevNode.val)
                size -= 1
                if prevNode.left is not None:
                    queue.append(prevNode.left)
                if prevNode.right is not None:
                    queue.append(prevNode.right)
        return result