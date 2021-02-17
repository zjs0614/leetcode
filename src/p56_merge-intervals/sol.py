class Solution:
    def merge_overlap(self, l1, l2):
        return [min(l1[0], l2[0]), max(l1[1], l2[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1] = self.merge_overlap(res[-1], interval)
            else:
                res.append(interval)
        return res
