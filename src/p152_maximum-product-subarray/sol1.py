class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    """
    Args:
    Returns:
    Constraints:
    Analysis:
      e.g. 
        -          1,-2, 3,   4
        - cur_min: 1,-2,-6, -24
        - cur_max: 1,-2, 3,  12
      - iteration to check
        - cur_min = min(nums[i]*cur_min, nums[i]*cur_max, nums[i])
        - cur_max = max(nums[i]*cur_min, nums[i]*cur_max, nums[i])
        - res = max(res, cur_max)
    """
    cur_min, cur_max, res = nums[0], nums[0], nums[0]
    for num in nums[1:]:
      cur_min, cur_max = min(num, cur_min * num, cur_max * num), \
                  max(num, cur_min * num, cur_max * num)
      res = max(res, cur_max)
    return res


