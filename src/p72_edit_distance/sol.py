class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[i+j for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i, w1 in enumerate(word1):
            for j, w2 in enumerate(word2):
                count = 0 if w1 == w2 else 1
                dp[i+1][j+1] = min(dp[i][j] + count, dp[i][j+1]+1, dp[i+1][j]+1)
        return dp[-1][-1]