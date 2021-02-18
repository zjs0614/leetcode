class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rgb_count = [0,0,0]
        for num in nums:
            rgb_count[num] += 1
        start = 0
        for index, count in enumerate(rgb_count):
            nums[start:start+count] = [index] * (count)
            start += count