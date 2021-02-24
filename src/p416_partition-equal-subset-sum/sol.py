class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2 != 0:
            return False
        total = int(total / 2)
        dp = [True] + [False] * total
        for i, num in enumerate(nums):
            for j in range(total, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        return dp[-1]
