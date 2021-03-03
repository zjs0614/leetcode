class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            loc = num-1 if num > 0 else -num-1
            new_num = nums[loc]
            if new_num < 0:
                res.append(loc + 1)
            else:
                nums[loc] *= -1
        return res
