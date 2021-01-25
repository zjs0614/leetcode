class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        num_rows = len(triangle)
        scores = triangle[num_rows-1]
        for row in range(2, num_rows + 1):
            for index, value in enumerate(triangle[num_rows-row]):
                scores[index] = min(value + scores[index], value + scores[index+1])
        return scores[0]