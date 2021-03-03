class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, t, r, b = 0, 0, len(matrix[0])-1, len(matrix)-1
        direction = 1
        x, y = 0, 0
        while True:
            if x > r or x < l or y > b or y < t:
                break
            res.append(matrix[y][x])
            if direction == 1:
                if x < r:
                    x += 1
                else:
                    t += 1
                    direction = 2
                    y += 1
            elif direction == 2:
                if y < b:
                    y += 1
                else:
                    r -= 1
                    direction = 3
                    x -= 1
            elif direction == 3:
                if x > l:
                    x -= 1
                else:
                    b -= 1
                    direction = 4
                    y -= 1
            elif direction == 4:
                if y > t:
                    y -= 1
                else:
                    l += 1
                    direction = 1
                    x += 1
        return res


