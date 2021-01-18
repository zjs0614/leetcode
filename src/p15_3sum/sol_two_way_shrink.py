class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = set()
        nums.sort()
        for index, x in enumerate(nums):
            i = index + 1
            j = len(nums) - 1
            while i < j:
                value = nums[i] + nums[j] + x
                if value == 0:
                    result.add((x, nums[i], nums[j]))
                    i += 1
                    j -= 1
                elif value < 0:
                    i += 1
                else:
                    j -= 1     
        return map(list, result)
