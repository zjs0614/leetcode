class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_total, min_total, max_pre, min_pre, sum_total = A[0], A[0], A[0], A[0], A[0]
        for num in A[1:]:
            max_pre = max(max_pre+num, num)
            min_pre = min(min_pre+num, num)
            max_total = max(max_total, max_pre)
            min_total = min(min_total, min_pre)
            sum_total += num
        if max_total < 0:
            return max_total
        else:
            return max(max_total, sum_total-min_total)