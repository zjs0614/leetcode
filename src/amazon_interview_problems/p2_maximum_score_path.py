import heapq
class Solution:
    def maximumMinimumPath(self, A) -> int:
        i, j = 0, 0
        current_min = A[i][j]
        queue = [(-current_min, (i, j))]
        visited = [[0] * len(A[0]) for _ in range(len(A))]
        visited[i][j] = 1
        while i < len(A) and j < len(A[0]):
            if i==0 and j==0:
                current_min = A[i][j]
            if i == len(A) - 1 and j == len(A[0])-1:
                return current_min
            next_cells = self.getNextCells(i, j, A, visited, current_min)
            for cell in next_cells:
                visited[cell[1][0]][cell[1][1]] = 1
                heapq.heappush(queue, cell)
            next_cell = heapq.heappop(queue)
            current_min = -next_cell[0]
            i = next_cell[1][0]
            j = next_cell[1][1]

            
    def getNextCells(self, i, j, A, visited, current_min):
        cells = []
        if i < len(A)-1 and visited[i+1][j] != 1:
            cells.append((max(-A[i+1][j], -current_min),(i+1, j)))
        if i > 0 and visited[i-1][j] != 1:
            cells.append((max(-A[i-1][j], -current_min),(i-1, j)))
        if j < len(A[0])-1 and visited[i][j+1] != 1:
            cells.append((max(-A[i][j+1], -current_min),(i, j+1)))
        if j > 0 and visited[i][j-1] != 1:
            cells.append((max(-A[i][j-1], -current_min),(i, j-1)))
        cells = sorted(cells, key=lambda x: x[0])
        return cells

sol = Solution()
print(sol.maximumMinimumPath([[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]))