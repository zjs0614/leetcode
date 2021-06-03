# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isValidBST(self, root: TreeNode) -> bool:
    valid, mi, ma = self.isValidBSTCheck(root)
    return valid
  
  def isValidBSTCheck(self, root):
    res = True
    c_min, c_max = root.val, root.val
    if root.left:
      if root.left.val >= root.val:
        res = False
      else:
        isLeftValid, c_min, left_max = self.isValidBSTCheck(root.left)
        if not isLeftValid or root.val <= left_max:
          res = False
    if root.right:
      if root.right.val <= root.val:
        res = False
      else:
        isRightValid, right_min, c_max = self.isValidBSTCheck(root.right)
        if not isRightValid or root.val >= right_min:
          res = False
    return res, c_min, c_max




