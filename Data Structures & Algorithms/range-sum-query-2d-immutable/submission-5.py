class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[] for i in range(rows)]

        for r in range(rows):
            total = 0
            for c in range(cols):
                total += matrix[r][c]
                self.prefix[r].append(total)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            left = self.prefix[i][col1 - 1] if col1 > 0 else 0
            total += self.prefix[i][col2] - left

        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)