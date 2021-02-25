class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0
        total = sum(nums)
        if S > total or S < -total:
            return 0
        dp = [0] * (2 * total + 1)
        for index, num in enumerate(nums):
            new = [0] * (2 * total + 1)
            if index == 0:
                new[-num+total] += 1
                new[num+total] += 1
            else:
                for i in range(len(dp)):
                    if i >= num:
                        new[i-num]  += dp[i]
                    if i+num < len(new):
                        new[i+num]  += dp[i]
            dp = new
        return dp[S+total]
