class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    """
    Args:
      intervals: list[list[int]] inteval: [start, end], value: [0, 10^4], length: [1, 10^4]
    Returns:
      list[list[int]]: non-overlapping list ordered

    Analysis:
      - schedule problem
      - time range overlapping merging
      - sorting

      steps:
        1) sorting by: (start, end) O(n*logn)
        2) res = []
        3) for interval in intervals: O(n)
              merge interval with res[-1] else append
    """
    sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    res = []
    for interval in sorted_intervals:
      if len(res) == 0:
        res.append(interval)
      else:
        last_interval = res[-1]
        if interval[0] <= last_interval[1]:
          last_interval[1] = max(interval[1], last_interval[1])
        else:
          res.append(interval)
    return res