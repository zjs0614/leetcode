class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    """
    Args:
    Returns:
    Constraints:
    Analysis:
      - dynamic programming
      - d[i][j] = d[i-1][j] + d[i][j-1]
    """
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
      for j in range(n):
        if i > 0 or j > 0:
          dp[i][j] = (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)
    return dp[-1][-1]