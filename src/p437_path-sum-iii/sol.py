# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.find(root, 0, {}, sum)
    
    def find(self, node, presum, presum_map, target):
        res = 0
        if node is None:
            return res
        cur_sum = presum + node.val
        if cur_sum - target in presum_map:
            res += presum_map[cur_sum - target]
        if cur_sum == target:
            res += 1
        if cur_sum in presum_map:
            presum_map[cur_sum] += 1
        else:
            presum_map[cur_sum] = 1
        res += self.find(node.left, cur_sum, presum_map, target)
        res += self.find(node.right, cur_sum, presum_map, target)
        presum_map[cur_sum] -= 1
        return res
        