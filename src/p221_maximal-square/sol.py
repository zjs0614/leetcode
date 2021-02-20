class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell == "0":
                    matrix[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        val = 1
                    else:
                        val = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+1)
                    matrix[i][j] = val
                    if val > res:
                        res = val
        return res ** 2