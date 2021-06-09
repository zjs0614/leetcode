# Definition for a binary tree node.
# class c:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    """
    Analysis:
      - preorder: root -> left -> right
      - inorder: left -> root -> right
      - back-tracking
    """
    if not preorder:
      return None

    root = TreeNode(val=preorder[0])
    pos = 0
    while pos < len(inorder):
      if inorder[pos] == root.val:
        break
      pos += 1
    
    root.left = self.buildTree(preorder[1:pos+1], inorder[0:pos])
    root.right = self.buildTree(preorder[pos+1:], inorder[pos+1:])

    return root