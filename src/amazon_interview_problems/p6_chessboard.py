class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1.0

        dp = [[[0] * K for _ in range(N)] for _ in range(N)]
        for k in range(K):
            for i in range(N):
                for j in range(N):
                    if k == 0:
                        dp[i][j][k] = len(self.getNextMoves(N,i,j)) / 8
                    else:
                        next_moves = self.getNextMoves(N,i,j)
                        for next_move in next_moves:
                            dp[i][j][k] += (dp[next_move[0]][next_move[1]][k-1])/8
        return dp[r][c][K-1]



    def getNextMoves(self, N, r, c):
        possibilities = []
        for i in [-1, 1, -2, 2]:
            n_r = r + i
            n_c = c + 3-abs(i)
            if n_r >= 0 and n_r < N and n_c >= 0 and n_c < N:
                possibilities.append((n_r, n_c))
            n_c = c + abs(i)-3
            if n_r >= 0 and n_r < N and n_c >= 0 and n_c < N:
                possibilities.append((n_r, n_c))
        return possibilities