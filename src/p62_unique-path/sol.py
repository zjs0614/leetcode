class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        total, short = m + n - 2, min(m, n) - 1
        res, count = 1, short
        while count >= 1:
            res, total, count = res * total, total - 1, count - 1
        while short >= 1:
            res, short = res / short, short - 1
        return int(res)