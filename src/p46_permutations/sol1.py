class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    """
    Args:
      - nums: list of distinct integers
    Returns:
      - permutations of combination
    
    Analysis:
      - array generation problem
      - permutation
      - recursive and backtracking
      - if len(nums) == 1:
          return nums
      - elif len(nums) == 2:
          return [[nums[0], nums[1]], [nums[1], nums[0]]]
      - else:
          p = nums[0]
          sub_lists = permute(nums[1:])
          for sub_list in sub_lists:
            for i in range(0, len(sub_list)):
              insert p in i
    """
    if len(nums) == 0:
      return []
    if len(nums) == 1:
      return [nums]
    elif len(nums) == 2:
      return [[nums[0],nums[1]],[nums[1],nums[0]]]
    
    p = nums[0]
    sublists = self.permute(nums[1:])
    res = []
    for sublist in sublists:
      for i in range(0, len(sublist)+1):
        new_list = [0] * (len(sublist) + 1)
        new_list[i] = p
        new_list[0:i] = sublist[0:i]
        new_list[i+1:] = sublist[i:]
        res.append(new_list)
    return res