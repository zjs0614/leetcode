class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums):
            if (i - res) % 2 == 0 and i < len(nums) - 1 and num == nums[i + 1]:
                res += 1

        return res if (len(nums) - res) % 2 == 0 else res + 1