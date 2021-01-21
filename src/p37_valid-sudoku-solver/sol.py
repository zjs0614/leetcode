class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        records = [[[0]*9, [0]*9, [0]*9] for _ in range(9)]
        for i, row in enumerate(board):
            for j, strValue in enumerate(row):
                if strValue != ".":
                    value = int(strValue)
                    part = (3 * int(i / 3)) + int(j/3)
                    if records[value - 1][0][i] == 1 or records[value - 1][1][j] == 1 or records[value - 1][2][part] == 1:
                        return False
                    records[value - 1][0][i] = 1
                    records[value - 1][1][j] = 1
                    records[value - 1][2][part] = 1
        self.find(board, records, 0, 0)
    
    def find(self, board, records, i, j):
        if i >= 9:
            return True
        if board[i][j] == ".":
            part = (3 * int(i / 3)) + int(j/3)
            for value in range(9):
                if records[value][0][i] == 1 or records[value][1][j] == 1 or records[value][2][part] == 1:
                    continue
                records[value][0][i] = 1
                records[value][1][j] = 1
                records[value][2][part] = 1
                board[i][j] = str(value+1)
                nextI = i if j < 8 else i + 1
                nextJ = j + 1 if j < 8 else 0
                result = self.find(board, records, nextI, nextJ)
                if not result:
                    records[value][0][i] = 0
                    records[value][1][j] = 0
                    records[value][2][part] = 0
                    board[i][j] = "."
                else:
                    return True
            return False
        else:
            nextI = i if j < 8 else i + 1
            nextJ = j + 1 if j < 8 else 0
            return self.find(board, records, nextI, nextJ)