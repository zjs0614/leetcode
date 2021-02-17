class Solution:

    def next_pos(self, pos, size):
        '''
        example: width 4, height 4
        1) 0,0 -> 0,3
        2) 0,2 -> 2,3
        3) 1,3 -> 3,2
        4) 2,2 -> 2,1
        new col = 3 - old row
        new row = old col
        '''
        return (pos[1], size - pos[0] - 1)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        size = len(matrix)
        for i, row in enumerate(matrix):
            for j, col in enumerate(row[:-i-1]):
                if j >= i:
                    tmp, next_pos = matrix[i][j], (i, j)
                    while True:
                        next_pos = self.next_pos(next_pos, size)
                        matrix[next_pos[0]][next_pos[1]], tmp = tmp, matrix[next_pos[0]][next_pos[1]]
                        if next_pos == (i, j):
                            break       
