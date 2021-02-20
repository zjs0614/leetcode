class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[index][have stock or not][cooldown_day_left]
        '''
        dp = [[([0] * 2) for _ in range(2)] for _ in prices]
        res = 0
        for i, price in enumerate(prices):
            if i == 0:
                dp[0][0][0] = 0
                dp[0][1][0] = -price
                dp[0][0][1] = float('-inf')
            else:
                dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1])
                dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0] - price)
                dp[i][0][1] = dp[i-1][1][0] + price
            res = max(res, dp[i][0][0], dp[i][0][1])
        
        return res
