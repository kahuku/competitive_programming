class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        if rowIndex == 0:
            triangle.append([1])
        if rowIndex > 0:
            triangle.append([1, 1])
        if rowIndex >= 1:
            for rowNum in range(1, rowIndex):
                row = [1]
                for i in range(1, len(triangle[rowNum - 1])):
                    row.append(triangle[rowNum - 1][i - 1] + triangle[rowNum - 1][i])
                row.append(1)
                triangle.append(row)
        return triangle[-1]
        