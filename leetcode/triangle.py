class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        costs = [[float('inf')] * len(row) for row in triangle]
        costs[0][0] = triangle[0][0]
        for row_i in range(1, len(triangle)):
            costs[row_i][0] = costs[row_i - 1][0] + triangle[row_i][0]
            for col_i in range(1, len(triangle[row_i]) - 1):
                costs[row_i][col_i] = min(costs[row_i - 1][col_i], costs[row_i - 1][col_i - 1]) + triangle[row_i][col_i]
            costs[row_i][-1] = costs[row_i - 1][-1] + triangle[row_i][-1]
        return min(costs[-1])