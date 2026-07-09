class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixSum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                self.prefixSum[r][c] = (
                    matrix[r - 1][c - 1]
                    + self.prefixSum[r - 1][c]
                    + self.prefixSum[r][c - 1]
                    - self.prefixSum[r - 1][c - 1]
                )
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = (
            self.prefixSum[row2 + 1][col2 + 1]
            - self.prefixSum[row1][col2 + 1]
            - self.prefixSum[row2 + 1][col1]
            + self.prefixSum[row1][col1]
        )
        return answer