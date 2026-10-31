class Solution:
    # basic dp on (r, c, prevDir)
    # We can technically optimize to pure O(grid) by precomputing final chaining, but its fine.

    def solve(self, row, col, mode):
        # mode == 1 means we were going right, so mirror will send us down
        if row == self.nrow or col == self.ncol:
            return 0
        
        uid = (row, col, mode)
        if uid in self.sols:
            return self.sols[uid]
        elif row == self.nrow - 1 and col == self.ncol - 1:
            return 1
        
        sol = None
        if self.grid[row][col] == 1:
            sol = self.solve(row + mode, col + (1 - mode), 1 - mode)
        else:
            sol = (self.solve(row + 1, col, 0) + self.solve(row, col + 1, 1)) % (10**9 + 7)

        self.sols[uid] = sol
        return sol


    def uniquePaths(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.nrow = len(grid)
        self.ncol = len(grid[0])
        self.sols = {}

        return self.solve(0, 0, 0)