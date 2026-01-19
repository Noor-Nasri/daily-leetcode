class Solution:
    # For each k (<= 50), we sweep the grid and track this at each point:
    # - Sum of k-window row, and the number of rows above that have the same sum.
    # - Same idea, but for columns
    # - The rolling sum for the diag
    # Then, as we sweep we simply have to look for the corner where everything is aligned. n^3

    def precomputeUpwardDiags(self, k):
        diagSumOfLastK = [[self.grid[r][c] for c in range(self.ncol)] for r in range(self.nrow)]
        for row in range(self.nrow - 2, -1, -1):
            for col in range(1, self.ncol):
                diagSumOfLastK[row][col] += diagSumOfLastK[row + 1][col - 1]
                if row + k < self.nrow and col >= k:
                    diagSumOfLastK[row][col] -= self.grid[row + k][col - k]

        return diagSumOfLastK

    def findSquare(self, k):
        rowSumOfLastK = [[self.grid[r][c] for c in range(self.ncol)] for r in range(self.nrow)]
        colSumOfLastK = [[self.grid[r][c] for c in range(self.ncol)] for r in range(self.nrow)]
        diagSumOfLastK = [[self.grid[r][c] for c in range(self.ncol)] for r in range(self.nrow)]
        sameSumChainLength = [[[1, 1] for i in range(self.ncol)] for j in range(self.nrow)]
        upwardDiagSumOfLastK = self.precomputeUpwardDiags(k)

        for row in range(self.nrow):
            for col in range(self.ncol):
                # Row sums
                if col:
                    rowSumOfLastK[row][col] += rowSumOfLastK[row][col - 1]
                    if col >= k:
                        rowSumOfLastK[row][col] -= self.grid[row][col - k]
            
                if row and rowSumOfLastK[row][col] == rowSumOfLastK[row - 1][col]:
                    sameSumChainLength[row][col][0] = sameSumChainLength[row - 1][col][0] + 1
                
                # Col sums
                if row:
                    colSumOfLastK[row][col] += colSumOfLastK[row - 1][col]
                    if row >= k:
                        colSumOfLastK[row][col] -= self.grid[row - k][col]

                if col and colSumOfLastK[row][col] == colSumOfLastK[row][col - 1]:
                    sameSumChainLength[row][col][1] = sameSumChainLength[row][col - 1][1] + 1

                # Diag sums
                if row and col:
                    diagSumOfLastK[row][col] += diagSumOfLastK[row - 1][col - 1]
                    if row >= k and col >= k:
                        diagSumOfLastK[row][col] -= self.grid[row - k][col - k]

                # Check if rows and cols all align, then traverse backwards for the diag
                if rowSumOfLastK[row][col] == colSumOfLastK[row][col] == diagSumOfLastK[row][col] == upwardDiagSumOfLastK[row - k + 1][col]:
                    if sameSumChainLength[row][col][0] >= k and sameSumChainLength[row][col][1] >= k:
                        return True

        return False



    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.nrow, self.ncol = len(grid), len(grid[0])

        for k in range(min(self.nrow, self.ncol), 1, -1):
            if self.findSquare(k):
                return k
        
        return 1
        