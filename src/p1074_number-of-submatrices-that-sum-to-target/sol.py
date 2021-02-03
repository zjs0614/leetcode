class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        num_row, num_col = len(matrix), len(matrix[0])
        for col in range(num_col):
            col_sum = 0
            for row in range(num_row):
                col_sum += matrix[row][col] 
                matrix[row][col] = col_sum
        res = 0
        for i in range(num_row):
            for j in range(i, num_row):
                cur = 0
                mem = {}
                for c in range(num_col):
                    prev = matrix[i-1][c] if i >= 1 else 0
                    cur += matrix[j][c] - prev
                    if cur == target:
                        res += 1
                    res += mem[cur - target] if (cur - target) in mem else 0
                    mem[cur] = mem[cur] + 1 if cur in mem else 1
        return res