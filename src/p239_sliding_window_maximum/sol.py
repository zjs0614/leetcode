class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        result = []
        for index, num in enumerate(nums):
            if len(window) > 0 and window[0] <= index - k:
                window.pop(0)
            while len(window) > 0 and nums[window[-1]] < num:
                window.pop()
            window.append(index)
            if index >= k - 1:
                result.append(nums[window[0]])
        return result