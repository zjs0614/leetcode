class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    """
    Analysis:
      - stock transaction, max profit problem, with at least 1 cooldown (after sell, then wait at least 1 day to buy)
      - prices: 1, 2, 3, 0, 2
                b, s, c, b, s => 3
      - dynamic programming:
        dp[n][k]: 
              n-th transaction,
              k: 0 not hold stock and not in cool down period
                 1 not hold stock and in cool down period
                 2 hold stock

      - dp[n][0] = max(dp[n-1][1], dp[n-1][0])
        dp[n][1] = max(prices[n] - dp[n-1][2])
        dp[n][2] = max(dp[n-1][2], dp[n-1][0] - prices[n])
        return max(dp[-1][0], dp[-1][1])
    """
    if not prices or len(prices) == 1:
      return 0
    
    dp = [[0] * 3 for _ in range(len(prices))]
    for i, price in enumerate(prices):
      if i == 0:
        dp[i][0] = 0
        dp[i][1] = None
        dp[i][2] = -price
      else:
        dp[i][0] = max(dp[i-1][1] if dp[i-1][1] is not None else dp[i-1][0], dp[i-1][0])
        dp[i][1] = price + dp[i-1][2]
        dp[i][2] = max(dp[i-1][2] if dp[i-1][2] is not None else dp[i-1][0] - price, dp[i-1][0] - price)
    
    return max(dp[-1][1], dp[-1][0])