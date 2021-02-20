class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        zero_count, zero_index, total = 0, 0, 1
        for index, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = index
                if zero_count >= 2:
                    return [0] * len(nums)
            else:
                total *= num
        
        if zero_count == 1:
            res = [0] * len(nums)
            res[zero_index] = total
            return res
        else:
            res = []
            for num in nums:
                res.append(int(total / num))
            return res