class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0] = 1
        for i, num in enumerate(nums):
            new_dp = {}
            for n in dp:
                if n+num not in new_dp:
                    new_dp[n+num] = 0
                if n-num not in new_dp:
                    new_dp[n-num] = 0
                new_dp[n+num] += dp[n]
                new_dp[n-num] += dp[n]
            dp = new_dp
        return dp[target] if target in dp else 0