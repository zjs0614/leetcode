class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        dp = [[False] * length for _ in range(length)]
        for i in range(length):
            dp[i][i] = True
        res = length
        for i in range(length):
            j = 0
            while j < i:
                if i == j + 1:
                    dp[j][i] = s[i] == s[j]
                else:
                    dp[j][i] = s[i] == s[j] and dp[j+1][i-1]
                res += 1 if dp[j][i] else 0
                j += 1
        return res
        
