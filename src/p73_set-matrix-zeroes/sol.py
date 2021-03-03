class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        isStartColZero = False
        for i, row in enumerate(matrix):
            foundZero = False
            for j, num in enumerate(row):
                if num == 0:
                    foundZero = True
                    if j == 0:
                        isStartColZero = True
                    break
            if foundZero:
                j = len(row) - 1
                last = len(row) - 1
                while j >= 0 or last >= 0:
                    if j >=0 and row[j] != 0:
                        matrix[i][last] = j+1
                        j -= 1
                        last -= 1
                    elif j >= 0 and row[j] == 0:
                        j -= 1
                    else:
                        matrix[i][last] = 0
                        last -= 1

        for i, row in enumerate(matrix):
            if row[0] == 0:
                col, start = 1, 1
                while col < len(row):
                    if start < len(row) and row[start] == col + 1:
                        col += 1
                        start += 1
                    elif start < len(row) and row[start] > col + 1:
                        self.updateZeroWithCol(matrix, col, i)
                        col += 1
                    elif start < len(row) and row[start] < col + 1:
                        start += 1
                    else:
                        self.updateZeroWithCol(matrix, col, i)
                        col += 1
                col = 1
                while col < len(row):
                    matrix[i][col] = 0
                    col += 1
            
        if isStartColZero:
            for i, row in enumerate(matrix):
                matrix[i][0] = 0
                

    
    def updateZeroWithCol(self, matrix, col, rowFrom):
        i = 0
        while i < len(matrix):
            if i != rowFrom:
                row = matrix[i]
                if row[0] != 0:
                    matrix[i][col] = 0
            i += 1