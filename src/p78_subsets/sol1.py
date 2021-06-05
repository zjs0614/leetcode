class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    """
    Analysis:
      - subset permutation
      - unique nums
      - unique subset
      - [] counts
    """
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