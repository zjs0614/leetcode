class Solution:
    def calcNumberOfSubarrays(self, A, anchor_points, start, end):
        if end == start + 1 or len(anchor_points) == 0:
            return 0
        res = 0
        for i, anchor_point in enumerate(anchor_points):
            next_point = end
            if i < len(anchor_points) - 1:
                next_point = anchor_points[i+1]
            left = anchor_point - start - 1
            right = next_point - anchor_point - 1
            res += (left+1)*(right+1)
        return res

    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        if R < L:
            return 0
        start = -1
        anchor_points = []
        res = 0
        for index, num in enumerate(A):
            if num >= L and num <= R:
                anchor_points.append(index)
            elif num > R:
                res += self.calcNumberOfSubarrays(A, anchor_points, start, index)
                start = index
                anchor_points = []
        if len(anchor_points) > 0:
            res += self.calcNumberOfSubarrays(A, anchor_points, start, len(A))
        return res