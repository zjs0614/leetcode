class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        dp = [1 for _ in nums]
        result = 0
        for index, num in enumerate(nums):
            value, i = 0, index - 1
            while i >= 0:
                if nums[i] < num:
                    value = dp[i] + 1
                elif nums[i] == num:
                    value = dp[i]
                if value > dp[index]:
                    dp[index] = value 
                if dp[index] > i:
                    break;
                i -= 1
            if dp[index] > result:
                result = dp[index]
        return result