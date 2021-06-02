# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    """
    Args:
      - root: tree
    Returns:
      - List[List[int]]: level order traversal
    
    Analysis:
      - bfs on tree
      - queue for each level
    """
    if root is None:
      return []

    res = []
    q_current, q_next = [root], []

    while len(q_current) > 0:
      cur_values = []
      for node in q_current:
        if node.left:
          q_next.append(node.left)
        if node.right:
          q_next.append(node.right)
        cur_values.append(node.val)
      res.append(cur_values)
      q_current, q_next = q_next, []
    
    return res
