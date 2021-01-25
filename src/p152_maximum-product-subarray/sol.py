class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_value, max_value, result = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            min_value, max_value = min_value * i, max_value * i
            min_value, max_value = min(min_value, max_value, i), max(min_value, max_value, i)
            result = result if result >= max_value else max_value
        return result
        