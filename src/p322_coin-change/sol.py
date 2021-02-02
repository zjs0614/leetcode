class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if coins is None or len(coins) == 0 or amount <= 0:
            return -1
        dp = [-1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(amount+1)[1:]:
            count = -1
            for coin in coins:
                if i-coin >= 0 and dp[i-coin] >= 0 and (count<0 or dp[i-coin] < count):
                    count = dp[i-coin]
            dp[i] = count + 1 if count >= 0 else -1
        return dp[-1]

sol = Solution()
print(sol.coinChange([186,419,83,408],6249))