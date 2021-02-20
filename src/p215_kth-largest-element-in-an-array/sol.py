import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        for num in nums:
            heapq.heappush(queue, num)
            if len(queue) > k:
                heapq.heappop(queue)
        return queue[0]