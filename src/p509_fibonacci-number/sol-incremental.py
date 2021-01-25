class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for _ in range(1, n):
            x, y = y, x+y
        return x if n == 0 else y