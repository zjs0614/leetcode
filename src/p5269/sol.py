class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        size = len(piles)
        presums = []
        for i, pile in enumerate(piles):
            presum = [0] * k
            for j in range(k):
                num = 0 if j >= len(pile) else pile[j]
                presum[j] = num + presum[j-1]
            presums.append(presum)

        dp = presums[0]
        for i in range(1, size):
            temp = [_ for _ in dp]
            for j in range(k):
                p = 0
                while p <= j and p < len(piles[i]):
                    new_presum = presums[i][p] + (dp[j-p-1] if j>p else 0)
                    temp[j] = max(temp[j], new_presum)
                    p += 1
            dp = temp
        return dp[-1]
