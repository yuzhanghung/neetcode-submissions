class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for i in range(ROWS):
            seen = set()
            for j in range(COLS):
                if board[i][j] in seen:
                    return False
                if board[i][j] == ".":
                    continue
                seen.add(board[i][j])
        
        
        for i in range(COLS):
            seen = set()
            for j in range(ROWS):
                if board[j][i] in seen:
                    return False
                if board[j][i] == ".":
                    continue
                seen.add(board[j][i])
        

        for i in range(0, ROWS, 3):
            for j in range(0, COLS, 3):
                seen = set()
                for start_row in range(i, i + 3):
                    for start_col in range(j, j + 3):
                        if board[start_row][start_col] in seen:
                            return False
                        if board[start_row][start_col] == ".":
                            continue
                        seen.add(board[start_row][start_col])
                

        return True
