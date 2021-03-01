class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0 or length == 1:
            return 0
        left, right, res = 0, length-1, 0
        left_max, right_max = height[left], height[right]

        while left <= right:
            if left_max < right_max:
                if height[left] < left_max:
                    res += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    res += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1
        return res