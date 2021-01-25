class Solution:
    def fib(self, n: int) -> int:
        F = [-1] * (n+1)
        for index, value in enumerate(F):
            F[index] = index if index <= 1 else F[index - 1] + F[index - 2]
        return F[n]