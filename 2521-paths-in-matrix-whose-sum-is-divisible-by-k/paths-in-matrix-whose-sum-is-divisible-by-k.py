class Solution:
    # Seems like basic DP. Each cell can go down and right, and we need the sum to reach remainder 0
    # So it's just O(m*n*k) which is 50*5*10^4

    def dpSolve(self, row, col, curRemainder):
        curRemainder = (curRemainder + self.grid[row][col]) % self.k
        if row == self.lastrow and col == self.lastcol:
            return int(curRemainder == 0)
        elif (row, col, curRemainder) in self.sols:
            return self.sols[(row, col, curRemainder)]
        
        numSolutions = 0
        if row < self.lastrow:
            numSolutions += self.dpSolve(row + 1, col, curRemainder)
        
        if col < self.lastcol:
            numSolutions += self.dpSolve(row, col + 1, curRemainder)

        self.sols[(row, col, curRemainder)] = numSolutions % (10**9 + 7)
        return self.sols[(row, col, curRemainder)]

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        self.grid = grid
        self.k = k
        self.sols = {}
        self.lastrow = len(grid) - 1
        self.lastcol = len(grid[0]) - 1
        return self.dpSolve(0, 0, 0)