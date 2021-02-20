class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        cases:
        1) [0,100],[0,10],[10,20] -> 2
        2) [0,100],[90,110],[100,120] -> 2
        '''
        res = 0
        count = 0
        queue = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for interval in intervals:
            start, end = interval[0], interval[1]
            if len(queue) > 0:
                while start >= queue[0]:
                    count -= 1
                    heapq.heappop(queue)
                    if len(queue) == 0:
                        break
            count += 1
            if count > res:
                res = count
            heapq.heappush(queue, end)
        return res
