class Solution:
  def canJump(self, nums: List[int]) -> bool:
    end = 0
    for i, num in enumerate(nums):
      if end < i:
        break
      if end >= len(nums) - 1:
        return True
      end = max(end, num + i)
    return False
