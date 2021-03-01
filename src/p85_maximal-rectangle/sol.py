class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        col_sum = [0] * len(matrix[0])
        res = 0
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                col_sum[j] = (1 + col_sum[j]) if num == "1" else 0
            
            left, right = [0] * len(col_sum), [0] * len(col_sum)
            stack = []
            for j, num in enumerate(col_sum):
                l = j
                while len(stack) > 0 and col_sum[stack[-1]] >= num:
                    l = stack.pop()
                left[j] = left[l] if l < j else l
                stack.append(j)

            stack = []
            for j in range(len(col_sum)):
                index = len(col_sum) - j - 1
                l = index
                while len(stack) > 0 and col_sum[stack[-1]] >= col_sum[index]:
                    l = stack.pop()
                right[index] = right[l] if l > index else l
                stack.append(index)

            max_area = [0] * len(col_sum)
            for j in range(len(col_sum)):
                max_area[j] = col_sum[j] * (right[j] - left[j] + 1)
                if max_area[j] > res:
                    res = max_area[j]

        return res