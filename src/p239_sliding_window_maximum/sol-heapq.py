import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = []
        if nums is None:
            return result
        heapq.heapify(window)
        heapq._siftdown()
        for index, num in enumerate(nums):
            heapq.heappush(window, -num)
            if index >= k - 1:
                result.append(window[0])
                if index >= k:
                    heapq.heappop(window, -nums[index - k])
        return result
                