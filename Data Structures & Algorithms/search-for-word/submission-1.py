class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r >= ROWS or 
                c >= COLS or 
                r < 0 or
                c < 0 or
                (r, c) in path or
                board[r][c] != word[i]):
                return False
                    
            i += 1
            
            
                
            path.add((r, c))
            result = (dfs(r + 1, c, i) or 
            dfs(r - 1, c, i) or 
            dfs(r, c + 1, i) or 
            dfs(r, c - 1, i))
            path.remove((r, c))

            return result

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
