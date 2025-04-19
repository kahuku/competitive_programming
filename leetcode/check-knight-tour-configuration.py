class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        def valid_move(prev, cur):
            vd = abs(prev[0] - cur[0])
            hd = abs(prev[1] - cur[1])
            valid_delta = vd == 2 and hd == 1 or vd == 1 and hd == 2
            in_grid = 0 <= cur[0] <= len(grid) and 0 <= cur[1] <= len(grid[0])
            return valid_delta and in_grid
        

        ordered_moves = [0] * len(grid) * len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                move = (r, c)
                ordered_moves[grid[r][c]] = move
        
        if ordered_moves[0] != (0, 0):
            return False
        
        prev = (0, 0)
        visited = {prev}
        for i in range(1, len(ordered_moves)):
            if not valid_move(prev, ordered_moves[i]):
                return False
            prev = ordered_moves[i]
            visited.add(prev)

        return all([move in visited for move in ordered_moves])