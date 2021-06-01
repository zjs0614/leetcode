class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    """
    Args:
      - grid: list[list[str]], "1" or "0", size: [1, 300]
    Returns:
      - number of islands
    
    Analysis:
      - union find (merge)
      - return number of different roots
    """
    if len(grid) == 0 or len(grid[0]) == 0:
      return 0

    distinct_root = set()
    node_map = [[None] * len(grid[0]) for _ in range(0, len(grid))]

    for i, row in enumerate(grid):
      for j, val in enumerate(row):
        if val == "1":
          node_map[i][j] = MyNode(i, j)
          distinct_root.add(node_map[i][j].getKey())

          if i > 0 and grid[i-1][j] == "1":
            self.merge(node_map[i][j], node_map[i-1][j], distinct_root)
          if j > 0 and grid[i][j-1] == "1":
            self.merge(node_map[i][j], node_map[i][j-1], distinct_root)
    return len(distinct_root)


  def merge(self, n1, n2, distinct_root):
    if n1.root.getKey() != n2.root.getKey():
      if n1.root.getKey() in distinct_root:
        distinct_root.remove(n1.root.getKey())

      prev_children = n1.root.children
      n1.root.children = []
      for node in prev_children:
        node.root = n2.root
        n2.root.children.append(node)
    distinct_root.add(n2.root.getKey())


class MyNode:
    def __init__(self, row, col):
      self.row = row
      self.col = col
      self.root = self
      self.children = [self]

    def getKey(self):
      return f"{self.row}_{self.col}"