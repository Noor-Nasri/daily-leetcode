class Solution:
    def recurSolver(self, nRem, board, curRow, curCol, availRem):
        if nRem == 0:
            return 1
        if availRem <= 0:
            return 0

        if curCol == len(board):
            curCol = 0
            curRow += 1
        
        if board[curRow][curCol]: # Cant place here
            return self.recurSolver(nRem, board, curRow, curCol + 1, availRem)
        
        availRem -= 1 # This tile is no longer avail in the future
        # Case 1: Ignore this tile
        case1 = self.recurSolver(nRem, board, curRow, curCol + 1, availRem)

        # Case 2: put a queen here
        board2 = [e[:] for e in board]

        # Horizontal, Vertical, then Diagonal
        for newCol in range(curCol + 1, len(board)):
            if not board2[curRow][newCol]:
                board2[curRow][newCol] = 1
                availRem -= 1
        
        for newRow in range(curRow + 1, len(board)):
            if not board2[newRow][curCol]:
                board2[newRow][curCol] = 1
                availRem -= 1
        
        for diag in range(1, len(board) - curRow):
            if curCol + diag < len(board) and not board2[curRow + diag][curCol + diag]:
                board2[curRow + diag][curCol + diag] = 1
                availRem -= 1

            if curCol - diag >= 0 and not board2[curRow + diag][curCol - diag]:
                board2[curRow + diag][curCol - diag] = 1
                availRem -= 1
        
        board2[curRow][curCol] = 2
        case2 = self.recurSolver(nRem - 1, board2, curRow, curCol + 1, availRem)
        return case1 + case2


    def totalNQueens(self, n: int) -> int:
        return self.recurSolver(n, [[0 for i in range(n)] for e in range(n)], 0, 0, n**2)
        