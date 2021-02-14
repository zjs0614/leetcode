class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left, right, res = 0, len(height) - 1, 0
        while left < right:
            value = min(height[left], height[right]) * (right - left)
            if value > res:
                res = value
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return res