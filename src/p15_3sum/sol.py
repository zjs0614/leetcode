class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = set()
        nums.sort()
        for index, x in enumerate(nums):
            triple = {}
            for y in nums[index+1:]:
                if -y in triple:
                    result.add((x, -y-x, y))
                else:
                    triple[x+y] = True
        return map(list, result)
