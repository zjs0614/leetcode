class Solution:
  def numTrees(self, n: int) -> int:
    """
    Analysis:
      - permutation problem
      - NOTE: BST not BT
      - back-tracking (left, right) child nodes
    """
    return self.numTreesWithMem(n, {})
  
  def numTreesWithMem(self, n, mem):
    if n == 2:
      return 2
    elif n <= 1:
      return 1
    if n in mem:
      return mem[n]
    res = 0
    for i in range(n):
      res += self.numTreesWithMem(i, mem) * self.numTreesWithMem(n-i-1, mem)
    mem[n] = res
    return res