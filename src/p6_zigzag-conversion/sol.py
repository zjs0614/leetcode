class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
            properties:
                row: 1 .. numRows
                isMiddle: True or False
                index: 0 .. len(s)-1
            
            nextIndex = 
                if row == 1 or row == numRows:
                    index + 2(numRows-1)
                else:
                    if isMiddle:
                        index + 2(row-1)
                    else:
                        index + 2(numRows - row)
            time:  O(n)
            space: O(1)
        '''
        if numRows == 1:
            return s
        result = ""
        for row in range(numRows):
            index = row
            isMiddle = False
            while index < len(s):
                result = result + s[index]
                if row == 0 or row == numRows - 1:
                    index = index + 2 * (numRows - 1)
                else:
                    index = (index + 2 * (row)) if isMiddle else (index + 2 * (numRows - row - 1))
                    isMiddle = not isMiddle
        return result
