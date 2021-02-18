class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, i = 0, len(nums) - 1, 0
        while i <= r:
            if nums[i] == 0:
                if nums[l] != 0:
                    nums[l], nums[i] = nums[i], nums[l]
            if nums[i] == 2:
                if nums[r] != 2:
                    nums[r], nums[i] = nums[i], nums[r]
            else:
                i = i + 1
            if nums[l] == 0:
                l += 1
            if nums[r] == 2:
                r -= 1
            if l > i:
                i = l