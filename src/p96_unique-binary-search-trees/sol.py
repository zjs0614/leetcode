class Solution:
    def numTrees(self, n: int) -> int:
        mem = [0] * (n+1)
        return self.find(n, mem)

    def find(self, n, mem):
        if n == 0 or n == 1:
            return 1
        if mem[n] > 0:
            return mem[n]
        res = 0
        for i in range(n):
            left = self.find(i, mem)
            right = self.find(n-i-1, mem)
            res += (left * right)
        mem[n] = res
        return res