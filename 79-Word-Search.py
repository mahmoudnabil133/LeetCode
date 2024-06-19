class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(i, j, w_ptr, visited):
            if i >= rows or i < 0 or j >= cols or j < 0 or (i, j) in visited or w_ptr >= len(word) or board[i][j] != word[w_ptr]:
                return False
            elif board[i][j] == word[w_ptr] and w_ptr == len(word) - 1:
                return True
            visited.add((i, j))
            left = dfs(i, j-1, w_ptr + 1, visited.copy())
            right = dfs(i, j+1, w_ptr + 1, visited.copy())
            top = dfs(i-1, j, w_ptr + 1, visited.copy())
            down = dfs(i+1, j, w_ptr + 1, visited.copy())
            
            return left + right + top + down
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True
        return False