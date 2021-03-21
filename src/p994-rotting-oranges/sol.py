class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        return self.dfs_sol(grid)

    def dfs_sol(self, grid):
        h, w = len(grid), len(grid[0])
        queue = []
        for i, row in enumerate(grid):
            for j, label in enumerate(row):
                if label == 2:
                    queue.append((i, j))
                    grid[i][j] = 1
                elif label == 0:
                    grid[i][j] = -1
                elif label == 1:
                    grid[i][j] = -2
        res = 0
        for pos in queue:
            self.dfs(grid, pos[0], pos[1], w, h, 0)
        
        for i, row in enumerate(grid):
            for j, label in enumerate(row):
                if label == -2:
                    return -1
                res = max(res, label)
        return res
    
    def dfs(self, grid, i, j, w, h, time):
        if i >= 0 and j >= 0 and i < h and j < w and (grid[i][j] > time or grid[i][j] == -2):
            grid[i][j] = time
            l1 = self.dfs(grid, i+1, j, w, h, time + 1)
            l2 = self.dfs(grid, i-1, j, w, h, time + 1)
            l3 = self.dfs(grid, i, j+1, w, h, time + 1)
            l4 = self.dfs(grid, i, j-1, w, h, time + 1)