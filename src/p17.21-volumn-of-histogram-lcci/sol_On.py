class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        leftMax, rightMax, res, i, j = height[0], height[-1], 0, 0, len(height)-1
        while i <= j:
            if leftMax < rightMax:
                if leftMax > height[i]:
                    res += leftMax - height[i]
                else:
                    leftMax = height[i]
                i += 1
            else:
                if rightMax > height[j]:
                    res += rightMax - height[j]
                else:
                    rightMax = height[j]
                j -= 1
        return res