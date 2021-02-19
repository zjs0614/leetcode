class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        mem = [0] * len(nums)
        for index, num in enumerate(nums):
            if index <= 1:
                mem[index] = num
            else:
                mem[index] = mem[index - 2] + num
            if index > 0 and mem[index] < mem[index - 1]:
                mem[index] = mem[index - 1]
        return mem[-1]