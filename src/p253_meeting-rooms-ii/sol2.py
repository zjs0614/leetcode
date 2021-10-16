import heapq

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    """
    Cases:
      1) [[0,10],[10,11]] -> 1
      2) [[0,10],[5,6]] -> 2
    
    Analysis:
      - 1st sort by start-end
      - min heap structure queue:
        - if empty: add
        - else 
          while cur.start >= queue[0]:
              - pop stack
            else
              - break
          add
    """
    count, queue, res = 0, [], 0

    for start, end in sorted(intervals, key=lambda x: x[0]):
      while queue and start >= queue[0]:
        heapq.heappop(queue)
        count -= 1
      heapq.heappush(queue, end)
      count += 1
      res = count if count > res else res

    return res