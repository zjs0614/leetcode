class Solution:

    def locToPos(self, width, i, j):
        return (i * width + j) + 2
    
    def posToLoc(self, width, pos):
        pos = pos - 2
        return int(pos/width), pos%width

    def findParent(self, grid, width, i, j, rank):
        if grid[i][j] == self.locToPos(width,i,j):
            return grid[i][j], rank
        else:
            i, j = self.posToLoc(width, grid[i][j]) 
            return self.findParent(grid, width, i, j, rank+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        width = len(grid[0])
        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == "1":
                    if i > 0 and int(grid[i-1][j]) > 1 and j > 0 and int(grid[i][j-1]) > 1:
                        topParent, topRank = self.findParent(grid, width, i-1, j, 0)
                        leftParent, leftRank = self.findParent(grid, width, i, j-1, 0)
                        if topParent != leftParent:
                            pi, pj = self.posToLoc(width, topParent) if topRank < leftRank else self.posToLoc(width, leftParent)
                            grid[pi][pj] = leftParent if topRank < leftRank else topParent    
                        grid[i][j] = leftParent
                    elif i > 0 and int(grid[i-1][j]) > 1:
                        grid[i][j] = grid[i-1][j]
                    elif j > 0 and int(grid[i][j-1]) > 1:
                        grid[i][j] = grid[i][j-1]
                    else:
                        grid[i][j] = self.locToPos(width, i, j)

        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == self.locToPos(width, i, j):
                    count += 1
        return count