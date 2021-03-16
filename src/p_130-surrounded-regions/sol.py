class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return
        
        self.sol_bfs(board)
    

    def dfs(self, board, num_rows, num_cols, i, j):
        if i < 0 or j < 0 or i >= num_rows or j >= num_cols:
            return
        if board[i][j] != "O":
            return
        board[i][j] = "A"
        self.dfs(board, num_rows, num_cols, i-1, j)
        self.dfs(board, num_rows, num_cols, i+1, j)
        self.dfs(board, num_rows, num_cols, i, j+1)
        self.dfs(board, num_rows, num_cols, i, j-1)

    def sol_dfs(self, board):
        num_rows, num_cols = len(board), len(board[0])
        for i in range(num_rows):
            self.dfs(board, num_rows, num_cols, i, 0)
            self.dfs(board, num_rows, num_cols, i, num_cols-1)
        for i in range(num_cols):
            self.dfs(board, num_rows, num_cols, 0, i)
            self.dfs(board, num_rows, num_cols, num_rows-1, i)

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "A":
                    board[i][j] = "O"
                if cell == "O":
                    board[i][j] = "X"
        return board

    def sol_bfs(self, board):
        num_rows, num_cols = len(board), len(board[0])

        queue = []

        for i in range(num_rows):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][num_cols-1] == "O":
                queue.append((i, num_cols-1))
        for i in range(num_cols):
            if board[0][i] == "O":
                queue.append((0, i))
            if board[num_rows-1][i] == "O":
                queue.append((num_rows-1, i))

        while len(queue) > 0:
            i, j = queue.pop()
            board[i][j] = "A"
            if i+1 < num_rows and board[i+1][j] == "O":
                queue.append((i+1, j))
            if i-1 >= 0 and board[i-1][j] == "O":
                queue.append((i-1, j))
            if j+1 < num_cols and board[i][j+1] == "O":
                queue.append((i, j+1))
            if j-1 >= 0 and board[i][j-1] == "O":
                queue.append((i, j-1))

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "A":
                    board[i][j] = "O"
                if cell == "O":
                    board[i][j] = "X"
        return board
