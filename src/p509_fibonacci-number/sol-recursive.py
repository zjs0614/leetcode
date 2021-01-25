class Solution:
    def fib(self, n: int) -> int:
        memo = [-1] * (n+1)
        return self.find(n, memo)
        
    def find(self, n: int, memo: List) -> int:
        value = n if n <= 1 else (memo[n] if memo[n] > 0 else (self.find(n-1, memo) + self.find(n-2, memo)))
        memo[n] = value
        return value