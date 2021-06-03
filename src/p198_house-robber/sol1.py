class Solution:
  def rob(self, nums: List[int]) -> int:
    """
    Args:
      - nums: list of integers [1, 100], values: [0, 400]
    Returns:
      - int: max money can be robbed
    Constraints:
      - no adjacent houses can be robbed
    
    Analysis：
      - max[0:n] = max(nums[0] + max[2:n], nums[1] + max[3:n])
      - dp[n] loop nums reversely
    """
    if not nums:
      return 0
    
    size = len(nums)
    if size <= 2:
      return max(nums)

    dp = [0] * len(nums)
    for i in range(size-1, -1, -1):
      if i == size - 1:
        dp[i] = nums[i]
      elif i == size - 2:
        dp[i] = max(nums[i], nums[i+1])
      else:
        dp[i] = max(nums[i] + dp[i+2], dp[i+1])
    
    return dp[0]
