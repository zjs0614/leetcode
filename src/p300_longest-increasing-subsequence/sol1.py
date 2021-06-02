class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    """
    Args:
      - nums: list of integers, [1, 2500], [-10^4, 10^4]
    Returns:
      - int: longest increasing sequence
    
    Analysis:
      - sequential problem: order matters
      - longest increasing sequence
        - 9, 10, 1, 12, 13 -> 1 is not important in this case
        - 10, 1, 2, 12, 13 -> 1 is important in this case
      - mem_list: record cur_long at each i:
        mem_list[i] = max(mem_list[j]+1), where j is a set of all nums[j] < nums[i] and j < i
        else: mem_list[i] = 1
      - Complexity:
        - Time: O(n*n)
        - Space: O(n)
    """
    mem = [1] * len(nums)
    res = 1
    for i, num in enumerate(nums):
      for j in range(0, i):
        if nums[j] < num:
          mem[i] = max(mem[i], mem[j]+1)
      res = max(res, mem[i])
    return res