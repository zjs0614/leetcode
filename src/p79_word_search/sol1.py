class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    """
    Args:
      - board: list[list[str]], letter 2d array
      - word: str, word to be searched
    Returns:
      - bool: if word can be found in board
    Constraints:
      - linked adjacent cells, only once per cell
      - m,n board size: [1, 6]
      - word.length: [1, 15]
      - board and word: lowercase and upper case en letters
    
    Analysis:
      - search problem
      - adjacent expansion with visited
      - dp[i][j][k] = 0 or 1, k is 0,1,..,or n, where n == len(word)-1, 
        - dp[i][j][k] means if cell at board[i][j] can make a word of word[k:]
      - dp[i][j][k] = (board[i][j] == word[k] and 
                        (dp[i-1][j][k+1] or dp[i+1][j][k+1] or
                          dp[i][j-1][k+1] or dp[i][j+1][k+1])
      - bfs or dfs
    """
    if not board or not(board[0]):
      return False
    if not word:
      return True
    m, n = len(board), len(board[0])
    visited = [[0] * n for _ in range(m)]

    for i in range(m):
      for j in range(n):
        if self.dfs_sol(board, word, 0, visited, i, j):
          return True
    return False
  
  def dfs_sol(self, board, word, index, visited, x, y):
    if not word or index >= len(word):
      return True
    if x >= len(visited) or x < 0 or y >= len(visited[0]) or y < 0 \
        or visited[x][y] == 1:
      return False
    else:
      visited[x][y] = 1
      check = board[x][y] == word[index] and \
          (self.dfs_sol(board, word, index+1, visited, x-1, y) or \
           self.dfs_sol(board, word, index+1, visited, x+1, y) or \
           self.dfs_sol(board, word, index+1, visited, x, y-1) or \
           self.dfs_sol(board, word, index+1, visited, x, y+1))
      visited[x][y] = 0
      return check


  
  def dp_sol(self, board, word):
    if not board or not(board[0]):
      return False
    if not word:
      return True
    
    m, n, size = len(board), len(board[0]), len(word)
    dp = [[[0] * size for _ in range(n)] for _ in range(m)]

    candidates = [(i, j) for j in range(n) for i in range(m)]
    visited = [[0] * n for _ in range(m)]

    # for k in range(size-1, -1, -1):
    #   for candidate in candidates:
    #     if candidate