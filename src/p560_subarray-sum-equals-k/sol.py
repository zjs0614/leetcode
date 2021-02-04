class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, accum, mem = 0, 0, {}
        for index, num in enumerate(nums):
            accum += num
            if accum == k:
                res += 1
            if accum - k in mem:
                res += mem[accum - k]
            mem[accum] = mem[accum] + 1 if accum in mem else 1
        return res