class Solution:
    # We can start by solving the prefix sums for all the diagonals 
    # Then at each point, we can consider the possible rhombuses centered there
    # This means n^3, so 50^3 = 125k. No problems. 

    def considerSum(self, sumFound):
        if sumFound in self.topThree or sumFound < self.topThree[2]:
            return
        
        if sumFound > self.topThree[0]:
            self.topThree = [sumFound, self.topThree[0], self.topThree[1]]
        elif sumFound > self.topThree[1]:
            self.topThree = [self.topThree[0], sumFound, self.topThree[1]]
        else:
            self.topThree = [self.topThree[0], self.topThree[1], sumFound]


    def considerShape(self, row, col, size):
        if size == 0:
            return self.considerSum(self.grid[row][col])
        
        topLeft = self.sumFromPrevRowsPrevCols[row + size][col] - self.sumFromPrevRowsPrevCols[row][col - size]
        topRight = self.sumFromNextRowsPrevCols[row][col + size] - self.sumFromNextRowsPrevCols[row + size][col]
        bottomRight = self.sumFromNextRowsNextCols[row - size][col] - self.sumFromNextRowsNextCols[row][col + size]
        bottomLeft = self.sumFromPrevRowsNextCols[row][col - size] - self.sumFromPrevRowsNextCols[row - size][col]

        self.considerSum(topLeft + topRight + bottomRight + bottomLeft)

    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        nrow, ncol = len(grid), len(grid[0])
        self.grid = grid

        self.sumFromPrevRowsPrevCols = [[grid[r][c] for c in range(ncol)] for r in range(nrow)]
        self.sumFromPrevRowsNextCols = [[grid[r][c] for c in range(ncol)] for r in range(nrow)]
        self.sumFromNextRowsPrevCols = [[grid[r][c] for c in range(ncol)] for r in range(nrow)]
        self.sumFromNextRowsNextCols = [[grid[r][c] for c in range(ncol)] for r in range(nrow)]

        for row in range(1, nrow):
            for col in range(1, ncol):
                self.sumFromPrevRowsPrevCols[row][col] += self.sumFromPrevRowsPrevCols[row - 1][col - 1]

            for col in range(ncol - 2, -1, -1):
                self.sumFromPrevRowsNextCols[row][col] += self.sumFromPrevRowsNextCols[row - 1][col + 1]
        
        for row in range(nrow -2, -1, -1):
            for col in range(1, ncol):
                self.sumFromNextRowsPrevCols[row][col] += self.sumFromNextRowsPrevCols[row + 1][col - 1]

            for col in range(ncol - 2, -1, -1):
                self.sumFromNextRowsNextCols[row][col] += self.sumFromNextRowsNextCols[row + 1][col + 1]


        self.topThree = [-1, -2, -3]
        for row in range(nrow):
            for col in range(ncol):
                for sizeLen in range(min(row, col, nrow - row - 1, ncol - col - 1) + 1):
                    self.considerShape(row, col, sizeLen)

        return [e for e in self.topThree if e > 0]