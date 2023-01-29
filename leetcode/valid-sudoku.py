class Solution:
    def validRowWise(self, board):
        for row in board:
            s = set()
            for item in [x for x in row if x != '.']:
                if item in s:
                    return False
                else:
                    s.add(item)
        return True
    
    def validColWise(self, board):
        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] in s:
                    return False
                else:
                    if board[j][i] != '.':
                        s.add(board[j][i])
        return True 
    
    def validBoxWise(self, board):
        boxes = []
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                boxes.append([board[r+dr][c+dc] for dr in range(3) for dc in range(3)])
        return self.validRowWise(boxes)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # return self.validRowWise(board) and self.validColWise(board) and self.validBoxWise(board)
        return self.validRowWise(board) and self.validColWise(board) and self.validBoxWise(board)