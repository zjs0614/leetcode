import heapq
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    Args:
    Returns:
    Constraints:
      - nums: [1, 10^5]
      - k: [1, n]
      - time complexity better than O(n log(n))
    Analysis:
      - top k, sorting, min-heap
      - number count
      - Time Complexity O(n + m*log(k) + k)
    """
    counts = {}
    for num in nums:
      if num not in counts:
        counts[num] = 0
      counts[num] += 1
    
    top_k = []
    for num in counts:
      heapq.heappush(top_k, (counts[num], num))
      while len(top_k) > k:
        heapq.heappop(top_k)
    
    res = [0] * k
    count = k-1
    while len(top_k) > 0:
      res[count] = heapq.heappop(top_k)[1]
      count -= 1

    return res



