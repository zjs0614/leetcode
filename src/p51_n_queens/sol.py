class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.find(n, 0, [], result)
        return result
    
    def find(self, n: int, currentRow: int, data: List, result: List[List[str]]):
        if currentRow < n:
            for i in range(n):
                flag = True
                for index, j in enumerate(data):
                    if i == j or i - currentRow == j - index or i + currentRow == j + index:
                        flag = False
                        break
                if flag:
                    data.append(i)
                    self.find(n, currentRow + 1, data, result)
                    data.pop()
        else:
            strData = []
            for index, i in enumerate(data):
                strValue = "." * i
                strValue += "Q"
                strValue += "." * (n - i - 1)
                strData.append(strValue)
            result.append(strData)
