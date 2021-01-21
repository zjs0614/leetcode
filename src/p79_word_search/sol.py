class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or word == "":
            return False
        width = len(board[0])
        height = len(board)
        visited = [["0"] * width for _ in range(height)]
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                result = self.find(board, visited, word, i, j, 0, width, height)
                if result:
                    return True
        return False


    def find(self, board, visited, word, row, col, i, width, height):
        if i >= len(word):
            return True
        if col >= width or col < 0 or row >= height or row < 0:
            return False

        char = word[i]

        if board[row][col] == char and visited[row][col] == "0":
            visited[row][col] = "1"
            result = self.find(board, visited, word, row + 1, col, i+1, width, height) or \
                self.find(board, visited, word, row - 1, col, i+1, width, height) or \
                self.find(board, visited, word, row, col + 1, i+1, width, height) or \
                self.find(board, visited, word, row, col - 1, i+1, width, height)
            if not result:
                visited[row][col] = "0"
            return result
        else:
            return False
