class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left < right - 1:
            mid = left + ((right - left) >> 1)
            v_l, v_r, v_m = nums[left], nums[right], nums[mid]
            if v_l == target:
                return left
            if v_r == target:
                return right
            if v_m == target:
                return mid
            if v_r < v_l:
                if v_r < target and v_l > target:
                    return -1
                elif (v_r < target and v_m < target and v_m < v_r) or (v_m > target and v_r < target) or (v_r > target and v_m > target and v_m < v_r):
                    right = mid
                elif (v_m < target and v_r < target and v_m > v_r) or (v_r > target and v_m > target and v_m > v_r) or (v_r > target and v_m < target):
                    left = mid
            else:
                if v_l > target or v_r < target:
                    return -1
                elif v_m < target:
                    left = mid
                else:
                    right = mid
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1