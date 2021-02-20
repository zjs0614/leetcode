class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) <= 2:
            return nums[0]
        low, high = 0, len(nums)-1
        res = 0
        while low <= high:
            mid = low + int((high-low) / 2)
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid - 1
                res = mid
        return res


