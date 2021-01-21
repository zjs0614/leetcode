class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        self.find(n, 0, [], result)
        return len(result)
    
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
            result.append(1)
