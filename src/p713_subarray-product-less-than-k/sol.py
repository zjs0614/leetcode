class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        start, cur, total, res = 0, 0, 1, 0
        while cur < len(nums):
            if nums[cur] >= k:
                start, cur = cur + 1, cur + 1
                continue
            total *= nums[cur]
            if total < k:
                res += (cur - start + 1)
                cur += 1
            else:
                while start < cur:
                    total /= nums[start]
                    start += 1
                    if total < k:
                        res += (cur - start + 1)
                        cur += 1
                        break
        return res