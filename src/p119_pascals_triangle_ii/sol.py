class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1] * (rowIndex)
        if rowIndex == 0:
            return [1]
        for i in range(rowIndex+1):
            for j in range(i-1, -1, -1):
                if j == i-1:
                    prev_row[j] = 1
                else:
                    prev_row[j] = prev_row[j] + (prev_row[j-1] if j > 0 else 1)
        return [1] + prev_row