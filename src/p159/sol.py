class Solution:

  def findMin(self, mem):
    min_pos, key = -1, ""
    for letter in mem:
      if min_pos == -1 or mem[letter] < min_pos:
        min_pos = mem[letter]
        key = letter
    return key, min_pos

  def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    """
      cases:
        1) eeaeeeeeea
    """
    size = 2
    mem = {}

    start = -1
    res = 0

    for i, letter in enumerate(s):
      mem[letter] = i
      if letter in mem:
        res = max(res, i-start)
      else:
        if len(mem) < size:
          res = max(res, i-start)
        else:
          pre_letter, pre_pos = self.findMin(mem)
          mem.pop(pre_letter)
          start = pre_pos
    return res
