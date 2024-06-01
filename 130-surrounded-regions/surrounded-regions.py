class Solution:
    def floodsearch(self, board, row, col):
        if (row, col) in self.finalized or board[row][col] == 'X': 
            return board[row][col]
        
        # Reached from borders, thus protected. See what else we can save.
        self.finalized.add((row, col)) 
        self.floodsearch(board, row - 1, col)
        self.floodsearch(board, row + 1, col)
        self.floodsearch(board, row, col - 1)
        self.floodsearch(board, row, col + 1)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nRow = len(board)
        nCol = len(board[0])
        if nRow <= 2 or nCol <= 2: return # all borders

        # Add borders as finalized, ie unchanging
        self.finalized = set()
        for col in range(nCol):
            self.finalized.add((0, col))
            self.finalized.add((nRow - 1, col))
        for row in range(nRow):
            self.finalized.add((row, 0))
            self.finalized.add((row, nCol - 1))
        
        # Figure out which are protected via floodfill
        for col in range(1, nCol - 1):
            if board[0][col] == 'O' and board[1][col] == 'O':
                self.floodsearch(board, 1, col)
            
            if board[nRow - 1][col] == 'O' and board[nRow - 2][col] == 'O':
                self.floodsearch(board, nRow - 2, col)
            
        for row in range(1, nRow - 1):
            if board[row][0] == 'O' and board[row][1] == 'O':
                self.floodsearch(board, row, 1)
            
            if board[row][nCol - 1] == 'O' and board[row][nCol - 2] == 'O':
                self.floodsearch(board, row, nCol - 2)


        # Now fix them all
        for row in range(1, nRow - 1):
            for col in range(1, nCol - 1):
                if board[row][col] == 'O' and not (row, col) in self.finalized:
                    board[row][col] = 'X'
        
        