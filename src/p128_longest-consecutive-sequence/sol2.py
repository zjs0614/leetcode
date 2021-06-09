class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    """
    Analysis:
      - mem: range[left, right]
      - link ranges, and record max length of range
    """
    if not nums:
      return 0
    left_mem, right_mem = {}, {}
    res = 1
    for num in nums:
      found_left, found_right = False, False
      if num not in left_mem and num not in right_mem:
        if num-1 in right_mem:
          right_mem[num] = right_mem[num-1]
          right_mem.pop(num-1)
          left_mem[right_mem[num]] = num
          found_left = True
          res = max(res, num - right_mem[num] + 1)
        if num+1 in left_mem:
          left_mem[num] = left_mem[num+1]
          left_mem.pop(num+1)
          right_mem[left_mem[num]] = num
          found_right = True
          res = max(res, left_mem[num] - num + 1)
        if found_left and found_right:
          left_mem[right_mem[num]], right_mem[left_mem[num]] = left_mem[num], right_mem[num]
          res = max(res, left_mem[num] - right_mem[num] + 1)
          left_mem.pop(num)
          right_mem.pop(num)
        elif not found_left and not found_right:
          left_mem[num] = num
          right_mem[num] = num
    return res