class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            seen = set()
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        
        for c in range(COLS):
            seen = set()
            for r in range(ROWS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c]) 
        
        for i in range(0, ROWS, 3):
            for j in range(0, COLS, 3):
                seen = set()

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in seen:
                            return False
                        seen.add(board[r][c]) 
        return True
