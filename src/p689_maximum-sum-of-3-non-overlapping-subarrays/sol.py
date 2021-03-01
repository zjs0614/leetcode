class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        pre_sum = [0] * (len(nums) - k + 1)
        for index, num in enumerate(nums):
            if index < k:
                pre_sum[0] += num
            else:
                pre_sum[index - k + 1] = num + pre_sum[index - k] - nums[index - k]
        
        post_max = [0] * (len(nums) - k + 1)
        pre_max = [0] * (len(nums) - k + 1)
        post_max_mem = pre_sum[-1]
        pre_max_mem = pre_sum[0]
        for i, num in enumerate(pre_sum):
            if i == 0:
                post_max[-1] = -1
                pre_max[0] = 0
            else:
                if pre_sum[-i-1] >= post_max_mem:
                    post_max_mem = pre_sum[-i-1]
                    post_max[-i-1] = -i-1
                else:
                    post_max[-i-1] = post_max[-i]

                if pre_sum[i] > pre_max_mem:
                    pre_max_mem = pre_sum[i]
                    pre_max[i] = i
                else:
                    pre_max[i] = pre_max[i-1]

        max_found = 0
        res = []
        middle = k
        while middle < len(pre_sum) - k:
            total = pre_sum[pre_max[middle - k]] + pre_sum[middle] + pre_sum[post_max[middle + k]]
            if total > max_found:
                res = [pre_max[middle - k], middle, post_max[middle + k] + len(pre_sum)]
                max_found = total
            middle += 1
        return res