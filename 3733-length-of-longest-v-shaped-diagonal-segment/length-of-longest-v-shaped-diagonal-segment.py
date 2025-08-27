class Solution:
    def solveMaxLen(self, row, col, dirInd, turnAlreadyUsed):
        uid = (row, col, dirInd, turnAlreadyUsed)
        if uid in self.sols:
            return self.sols[uid]
        
        extraLength = 0
        neededVal = self.nextVal[self.grid[row][col]]
        dr, dc = self.directions[dirInd]
        nr, nc = row + dr, col + dc
        if 0 <= nr < self.nrow and 0 <= nc < self.ncol and self.grid[nr][nc] == neededVal:
            extraLength = self.solveMaxLen(nr, nc, dirInd, turnAlreadyUsed)
        
        if not turnAlreadyUsed:
            # explore second option
            dirInd = (dirInd + 1) % 4
            dr, dc = self.directions[dirInd]
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.nrow and 0 <= nc < self.ncol and self.grid[nr][nc] == neededVal:
                op2 = self.solveMaxLen(nr, nc, dirInd, True)
                extraLength = max(extraLength, op2)
        
        self.sols[uid] = 1 + extraLength
        return self.sols[uid]

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # Cant we just start a DP call at every 1?
        # SolveMaxLength(pos, dir, desiredVal, turnUsed)
        # O(n * m * 2 * 2) to solve entire space, + O(m*n) to call it at each 1
        self.grid = grid
        self.nrow = len(self.grid)
        self.ncol = len(self.grid[0])
        self.sols = {}
        self.directions = [
            # Starting by pointing to top right, then clockwise
            [-1, 1],
            [1, 1],
            [1, -1],
            [-1, -1]
        ]
        self.nextVal = [2, 2, 0]

        maxDiag = 0
        for row in range(self.nrow):
            for col in range(self.ncol):
                if grid[row][col] != 1:
                    continue
                
                for dir_ind in range(4):
                    maxDiag = max(maxDiag, self.solveMaxLen(row, col, dir_ind, False))
        
        return maxDiag