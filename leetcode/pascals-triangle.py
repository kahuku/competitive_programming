class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        if numRows > 0:
            triangle.append([1])
        if numRows > 1:
            triangle.append([1, 1])
        if numRows >= 2:
            for rowNum in range(2, numRows):
                row = [1]
                for i in range(1, len(triangle[rowNum - 1])):
                    row.append(triangle[rowNum - 1][i - 1] + triangle[rowNum - 1][i])
                row.append(1)
                triangle.append(row)
        return triangle
        