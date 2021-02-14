import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        queue = []
        for point in points:
            value = - (point[0] * point[0]) - (point[1] * point[1])
            heapq.heappush(queue, (value, point))
            if len(queue) > K:
                heapq.heappop(queue)
        res = []
        for _ in range(len(queue)):
            res.insert(0, heapq.heappop(queue)[1])
        return res
        