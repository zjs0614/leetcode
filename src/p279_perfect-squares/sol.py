class Solution:
    def numSquares(self, n: int) -> int:
        '''
        n = sum(pi * qj * qj)
        res = sum(pi)
        qj in {1,2,3,4..100}
        to minimize res

        cases:
        1) 4 -> 1
        2) 5 -> 2
        3) 12 -> 1 * (3*3) + 3 * (1*1) | 3 * (2*2) -> 3
        '''
        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1,n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - (j*j)] + 1)
                j += 1
        return dp[-1]