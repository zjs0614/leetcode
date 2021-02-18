class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        cost_grid = [[0 for _ in range(n)] for _ in range(2)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                right_cost = cost_grid[i%2][j+1] if j+1 < n else -1
                down_cost = cost_grid[(i+1)%2][j] if i+1 < m else -1
                if right_cost < 0 and down_cost > 0:
                    cost_grid[i%2][j] = grid[i][j] + down_cost
                elif down_cost < 0 and right_cost > 0:
                    cost_grid[i%2][j] = grid[i][j] + right_cost
                elif right_cost > 0 and down_cost > 0:
                    cost_grid[i%2][j] = grid[i][j] + min(right_cost, down_cost)
                else:
                    cost_grid[i%2][j] = grid[i][j]
        return cost_grid[0][0]