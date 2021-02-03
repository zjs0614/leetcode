class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        height, width = len(A), len(A[0])
        res = [[0 for _ in range(height)] for _ in range(width)]
        if width >= height:
            for i, row in enumerate(A):
                res[i][i] = A[i][i]
                for j, value in enumerate(row[i+1:]):
                    col = j + i + 1
                    if col < height:
                        res[i][col] = A[col][i]
                    res[col][i] = A[i][col]
        else:
            for i, row in enumerate(res):
                res[i][i] = A[i][i]
                for j, value in enumerate(row[i+1:]):
                    col = j + i + 1
                    res[i][col] = A[col][i]
                    if col < width:
                        res[col][i] = A[i][col]
        return res