# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Analysis:
      - lowest ancestor
      - a node is ancestor of itself
      - return None if not exist p or q

      - recursively search p and q in root, left, and right
       - record current states:
        - found p in left, found p in right, found p in root
        - found q in left, found q in right, found q in root
        - 
    """
    res, state = self.lca_search(root, p, q)
    return res
  
  """
  Return:
    Node:
    States:
      - 0: found all
      - 1: found p
      - 2: found q
      - -1: nothing found
  """
  def lca_search(self, node, p, q):
    if node is None:
      return None, -1
    
    if p is not None and q is not None:
      if p == q:
        return p, 0
      
      if p == node or q == node:
        found_node, rest_node, state = (p, q, 1) if p == node else (q, p, 2)
        _, found1 = self.lca_search(node.left, rest_node, None)
        if found1 == 1:
          return node, 0
        _, found2 = self.lca_search(node.right, rest_node, None)
        if found2 == 1:
          return node, 0
        else:
          return node, state
      else:
        n1, found1 = self.lca_search(node.left, p, q)
        if found1 == 0:
          return n1, 0
        n2, found2 = self.lca_search(node.right, p, q)
        if found2 == 0:
          return n2, 0
        elif (found1 == 1 and found2 == 2) or (found1 == 2 and found2 == 1):
          return node, 0
        elif found1 > 0 and found2 < 0:
          return node, found1
        elif found2 > 0 and found1 < 0:
          return node, found2
    
    elif p is not None or q is not None:
      # only to return found or not True of False
      rest_node, state = (p, 1) if p is not None else (q, 2)
      if rest_node == node:
        return node, state
      else:
        n1, found1 = self.lca_search(node.left, rest_node, None)
        if found1 == 1:
          return node, state
        n2, found2 = self.lca_search(node.right, rest_node, None)
        if found2 == 1:
          return node, state
    return None, -1


