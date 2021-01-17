import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = [] if nums is None else nums
        self.k = k
        heapq.heapify(self.data)
        while len(self.data) > k:
            heapq.heappop(self.data)

    def add(self, val: int) -> int:
        if len(self.data) < self.k:
            heapq.heappush(self.data, val)
            return self.data[0] if len(self.data) == self.k else None
        if val > self.data[0]:
            heapq.heappushpop(self.data, val)
        return self.data[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)