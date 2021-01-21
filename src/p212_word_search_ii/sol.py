class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        trie = {'flag': 0, 'value': {}}
        for word in words:
            node = trie
            for char in word:
                if char not in node['value']:
                    node['value'][char] = {'flag': 0, 'value': {}}
                node = node['value'][char]
            node['flag'] = 1
        height = len(board)
        width = len(board[0])
        visited = [[0] * width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                self.find(board, trie, visited, i, j, result, "", width, height)
        return list(result)
        
    def find(self, board, trie, visited, row, col, result, value, width, height):
        if row>=0 and row<height and col>=0 and col<width and visited[row][col] == 0:
            char = board[row][col]
            if char in trie['value']:
                trie = trie['value'][char]
                if trie['flag'] == 1:
                    result.add(value + char)
                visited[row][col] = 1
                self.find(board, trie, visited, row+1, col, result, value + char, width, height)
                self.find(board, trie, visited, row-1, col, result, value + char, width, height)
                self.find(board, trie, visited, row, col+1, result, value + char, width, height)
                self.find(board, trie, visited, row, col-1, result, value + char, width, height)
                visited[row][col] = 0


