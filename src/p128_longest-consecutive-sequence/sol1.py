class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    """
    Constraints:
      - O(n) time
    Analysis:
      - map: range
        - if found 1,2,3,4 -> {1:4} {4:1}
        - keep extend and merge consecutive ranges
        - reset max range to res
    """
    if not nums:
      return 0

    res = 1
    range_map = {}
    for num in nums:
      if num not in range_map:
        if num-1 not in range_map and num+1 not in range_map:
          range_map[num] = num
        res = max(res, self.checkMerge(num, range_map), self.checkLinkDown(num, range_map), self.checkLinkUp(num, range_map))
    return res
  
  def checkMerge(self, num ,range_map):
    if num - 1 in range_map and num > range_map[num-1] and num + 1 in range_map and num < range_map[num+1]:
      start, end = range_map[num-1], range_map[num+1]
      range_map.pop(num-1)
      range_map.pop(num+1)
      range_map[start] = end
      range_map[end] = start
      return end - start + 1
    else:
      return 0

  def checkLinkDown(self, num, range_map):
    if num - 1 in range_map and num + 1 not in range_map and num > range_map[num-1]:
      self.replaceRangeItem(num, num-1, range_map)
      return num - range_map[num] + 1
    else:
      return 0
  
  def checkLinkUp(self, num, range_map):
    if num + 1 in range_map and num - 1 not in range_map and num < range_map[num+1]:
      self.replaceRangeItem(num, num+1, range_map)
      return range_map[num] - num + 1
    else:
      return 0

  def replaceRangeItem(self, n1, n2, range_map):
    range_map[n1] = range_map[n2]
    range_map[range_map[n2]] = n1
    if n2 != range_map[n1]:
      range_map.pop(n2)