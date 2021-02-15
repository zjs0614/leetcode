class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        if len(nums) < 4:
            return []
        nums.sort()
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[i+1:]):
                left, right = i + j + 2, len(nums)-1
                while left < right:
                    sum = n1 + n2 + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        res.add((n1,n2,nums[left],nums[right]))
                        left += 1
                        right -= 1
        return list(res)