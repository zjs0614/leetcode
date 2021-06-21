class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    """
    Analysis:
      - subset permutation
      - unique nums
      - unique subset
      - [] counts
    """
    return self.subsets_bit_manipulation(nums)

  def subsets_bit_manipulation(self, nums):
    size = 1 << len(nums)
    res = []
    for i in range(size):
      cur = []
      for j in range(len(nums)):
        if i >> j & 1:
          cur.append(nums[j])
      res.append(cur)
    return res 

  def subsets_backtracking(self, nums):
    if not nums:
      return []
    
    if len(nums) == 1:
      return [[], [nums[0]]]

    res = []
    next_res = self.subsets(nums[1:])
    for l in next_res:
      res.append(l)
      res.append(l+[nums[0]])
    return res