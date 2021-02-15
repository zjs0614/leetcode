class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
            Sort nums list first.
            loop num i from 0 to len(nums) - 2:
                pick left i+1 and right len(nums)-1
                if find closest combination of nums[i]
        '''
        if len(nums) < 3:
            return -1
        res_diff, res_sum = -1, -1
        nums.sort()
        for index, num in enumerate(nums[0:-2]):
            left, right, local_diff, local_sum = index + 1, len(nums) - 1, -1, 0
            while left < right:
                sum = num + nums[left] + nums[right]
                diff = abs(sum - target)
                if diff < local_diff or local_diff < 0:
                    local_diff = diff
                    local_sum = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return target
            if local_diff < res_diff or res_diff < 0:
                res_diff = local_diff
                res_sum = local_sum
        return res_sum

