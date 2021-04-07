"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node:
            return self.dfsClone(node, {})
        else:
            return None

    def dfsClone(self, node, visited):
        if node.val in visited:
            return visited[node.val]
        node_cloned = Node(node.val)
        visited[node_cloned.val] = node_cloned
        neighbors = node.neighbors
        if neighbors:
            node_cloned.neighbors = []
            for neighbor in neighbors:
                node_cloned.neighbors.append(self.dfsClone(neighbor, visited))
        
        return node_cloned


