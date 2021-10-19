"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:

  def treeToDoublyListProcess(self, node):
    left, right = node, node
    if node.left:
      _, prev = self.treeToDoublyListProcess(node.left)
      prev.right = node
      node.left = prev
      left = _
    if node.right:
      next, _ = self.treeToDoublyListProcess(node.right)
      next.left = node
      node.right = next
      right = _
    return left, right

  def treeToDoublyList(self, root: 'Node') -> 'Node':
    if not root:
      return None
    left, right = self.treeToDoublyListProcess(root)
    left.left = right
    right.right = left
    return left