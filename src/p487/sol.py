class Solution:
  def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    start, zero = -1, -1
    res = 0

    for i, num in enumerate(nums):
      if num == 1:
        res = max(res, i - start)
      else:
        if zero >= 0:
          start = zero
        zero = i
        res = max(res, i - start)
    return res