class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        res = [1] * size
        zero_count, zero_index = 0, 0
        for index, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = index
                if zero_count >= 2:
                    return [0] * size
            if index > 0:
                res[size-index-1] = res[size-index] * nums[size-index-1]
            else:
                res[size-1] = nums[size-1]
        
        total = 1
        for index, num in enumerate(nums):
            if index < size - 1:
                res[index] = res[index+1] * total
                total *= num
            else:
                res[index] = total
        return res
        