class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_max = 0
        for index, num in enumerate(nums):
            if index > current_max:
                break
            jump = index + num
            if jump > current_max:
                current_max = jump
            if current_max >= len(nums) - 1:
                return True
        return current_max >= len(nums) - 1