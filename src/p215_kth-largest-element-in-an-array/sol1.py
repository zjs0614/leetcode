import heapq

class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    """
    Args:
      - nums: list of integers [-10^4, 10^4]
      - k: [1, 10^4]
    Returns:
      k-th largest
    
    Analysis:
      - k-th largest: min-heap
    """
    if k == 0:
      return -1
    if k == 1:
      return max(nums)

    top_k_nums = []
    for num in nums:
      heapq.heappush(top_k_nums, num)
      while len(top_k_nums) > k:
        heapq.heappop(top_k_nums)
    return top_k_nums[0]
