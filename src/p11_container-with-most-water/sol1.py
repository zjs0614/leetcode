class Solution:
  def maxArea(self, height: List[int]) -> int:
    """
    Args:
      - height: list of integers [0, 10^4], size: [2, 10^5]
    Returns:
      - int: max size, min(h[i], h[j])*(j-i)
    
    Analysis:
      - search problem:
        - have to scan all height
      - start from both side: left=0, right=len(h)-1
        - record cur size and reset max
        - if h[left] < h[right]:
            move left+1
          else：
            move right-1
          until left meets right
        - because if h[left] < h[right], cur size is the max for cur_left as left
    
    Complexity:
      - Time: O(n)
      - Space: O(1)
    """
    left, right = 0, len(height)-1
    res = 0
    while left < right:
      res = max(res, min(height[left], height[right]) * (right - left))
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
    return res



