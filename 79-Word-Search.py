class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(i, j, w_ptr):
            if i >= rows or i < 0 or j >= cols or j < 0 or w_ptr >= len(word) or board[i][j] != word[w_ptr]:
                return False
            elif board[i][j] == word[w_ptr] and w_ptr == len(word) - 1:
                return True
            
            temp = board[i][j]
            board[i][j] = ''
            
            if dfs(i, j-1, w_ptr + 1) or dfs(i, j+1, w_ptr + 1) or dfs(i-1, j, w_ptr + 1) or dfs(i+1, j, w_ptr + 1):
                return True
            
            board[i][j] = temp
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False