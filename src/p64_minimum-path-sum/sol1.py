class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    """
    Args:
    Returns:
    Constraints:
    Analysis:
      - Optimal solution problem
      - Dynamic Programming: 递推
        - dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    """
    m, n = len(grid), len(grid[0])

    dp = [[0] * n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        if i == 0 and j == 0:
          dp[i][j] = grid[i][j]
        else:
          dp[i][j] = min(dp[i-1][j] if i > 0 else dp[i][j-1], \
                         dp[i][j-1] if j > 0 else dp[i-1][j]) \
                        + grid[i][j]
    return dp[-1][-1]