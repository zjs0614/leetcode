"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        newRoot = Node(root.val)
        children = root.children
        if children is not None:
            newRoot.children = []
            for child in children:
                newRoot.children.append(self.cloneTree(child))
        return newRoot