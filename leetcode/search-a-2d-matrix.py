class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def convertPlace(ind):
            r = ind // len(matrix[0])
            c = ind % len(matrix[0])
            return r, c

        if len(matrix) == 1 and 1 == len(matrix[0]):
            return True if matrix[0][0] == target else False

        low = 0
        high = len(matrix) * len(matrix[0]) - 1
        mid = (low + high) // 2
        while low <= high:
            r, c = convertPlace(mid)
            print(matrix[r][c])
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) // 2
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        newMatrix = []
        for row in matrix:
            newMatrix.extend(row)
        
        low = 0
        high = len(newMatrix)
        while low < high:
            mid = (low + high) // 2
            if newMatrix[mid] == target:
                return True
            elif newMatrix[mid] > target:
                high = mid
            else:
                low = mid + 1
        return False