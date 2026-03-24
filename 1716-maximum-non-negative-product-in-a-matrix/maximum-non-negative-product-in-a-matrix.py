class Solution:
    # Seems like classic DP: (row, col, lookForNegative). Small constraints too.

    def getMaximalProd(self, row, col, numNegative):
        uid = (row, col, numNegative)
        if uid in self.sols:
            return self.sols[uid]
        elif row >= self.nrow or col >= self.ncol:
            return -1
        
        val = self.grid[row][col]
        if val < 0:
            numNegative = (numNegative + 1) % 2

        if row == self.nrow - 1 and col == self.ncol - 1:
            if numNegative and val != 0:
                return -1

            return abs(val)
        
        maxRemainingProd = max(
            self.getMaximalProd(row + 1, col, numNegative),
            self.getMaximalProd(row, col + 1, numNegative),
        )

        if maxRemainingProd == -1 and val != 0:
            self.sols[uid] = -1
        else:
            self.sols[uid] = (maxRemainingProd * abs(val)) 

        return self.sols[uid]
        
    def maxProductPath(self, grid: List[List[int]]) -> int:
        self.sols = {}
        self.grid = grid
        self.nrow, self.ncol = len(grid), len(grid[0])

        maxVal = self.getMaximalProd(0, 0, 0) 
        if maxVal != -1:
            maxVal %= (10**9 + 7)
        return maxVal