class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        postfix_min, prefix_max = [None] * len(nums), [None] * len(nums)
        length = len(nums)
        for index in range(length):
            if index == 0:
                prefix_max[index] = nums[index]
                postfix_min[-1] = nums[-1]
            else:
                prefix_max[index] = max(nums[index], prefix_max[index-1])
                postfix_min[length - index - 1] = min(nums[length - index - 1], postfix_min[length - index])
        
        left, right = 0, length - 1
        while left < right:
            found = True
            if postfix_min[left] == nums[left]:
                left += 1
                found = False
            if prefix_max[right] == nums[right]:
                right -= 1
                found = False
            if found:
                return right - left + 1
        return 0