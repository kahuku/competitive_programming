class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = [[float('inf')] * len(matrix[i]) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                self.pre[row][col] = matrix[row][col]
                self.pre[row][col] += self.pre[row-1][col] if row else 0
                self.pre[row][col] += self.pre[row][col - 1] if col else 0
                self.pre[row][col] -= self.pre[row-1][col-1] if row and col else 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not row1 and not col1:
            return self.pre[row2][col2]
        if not row1:
            return self.pre[row2][col2] - self.pre[row2][col1-1]
        if not col1:
            return self.pre[row2][col2] - self.pre[row1-1][col2]
        return self.pre[row2][col2] - self.pre[row2][col1-1] - self.pre[row1-1][col2] + self.pre[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)