class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.prefix = [[] for i in range(self.rows)]
        
        total = 0
        for i in range(self.rows):
            for j in range(self.cols):
                total += self.matrix[i][j]
                self.prefix[i].append(total)
            total = 0
            

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            L = self.prefix[i][col1 - 1] if (col1 > 0) else 0
            R = self.prefix[i][col2]
            total += R - L

        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)