# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        Input:
            - Binary Tree
            - Target Sum
        Output:
            - num of paths that sum to target
        
        Analysis:
            - pre order traverse
            - for each path, use presum with count_map:
                e.g. 
                    target: 4, 
                    paths:     1,3,-4,2,2,3,1
                    pre_sum: 0,1,4, 0,2,4,7,8
                    count:     0,1, 1,1,3,3,5
        """
        if root is None:
            return 0
        count_map = {}
        count_map[0] = 1
        return self.pathSumRec(root, targetSum, 0, count_map)
    
    def pathSumRec(self, node, target, pre_sum, count_map):
        cur_sum = pre_sum + node.val
        cur_res = count_map[cur_sum - target] if cur_sum - target in count_map else 0
        if cur_sum not in count_map:
            count_map[cur_sum] = 0
        count_map[cur_sum] += 1
        if node.left is not None:
            cur_res += self.pathSumRec(node.left, target, cur_sum, count_map)
        if node.right is not None:
            cur_res += self.pathSumRec(node.right, target, cur_sum, count_map)
        count_map[cur_sum] -= 1
        return cur_res











