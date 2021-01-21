class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        return True