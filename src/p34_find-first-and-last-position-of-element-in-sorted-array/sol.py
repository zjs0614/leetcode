class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        return self.find(nums, 0, len(nums)-1, target)

    def find(self, nums, left, right, target):
        if nums[left] > target or nums[right] < target:
            return [-1, -1]
        if nums[left] == target and nums[right] == target:
            return [left, right]
        mid = left + int((right-left)/2)
        left_range = self.find(nums, left, mid, target)
        right_range = self.find(nums, mid + 1, right, target)
        return [left_range[0] if left_range[0] >= 0 else right_range[0], 
                right_range[1] if right_range[1] >= 0 else left_range[1]]

        