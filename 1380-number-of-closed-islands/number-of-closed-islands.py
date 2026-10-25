class Solution:
    # So we just do basic floodfill for islands, solve in O(n)
    # All we need to do is exclude islands that touch the borders

    def expand(self, row, col):
        if not (0 <= row < self.nrow and 0 <= col < self.ncol):
            self.contained = 0
        elif not (row, col) in self.seen and self.grid[row][col] == 0:
            self.seen.add((row, col))
            self.expand(row + 1, col)
            self.expand(row - 1, col)
            self.expand(row, col + 1)
            self.expand(row, col - 1)
        
    def closedIsland(self, grid: list[list[int]]) -> int:
        numIslands = 0
        self.grid = grid
        self.seen = set()
        self.nrow = len(grid)
        self.ncol = len(grid[0])

        for row in range(self.nrow):
            for col in range(self.ncol):
                if grid[row][col] == 0 and not (row, col) in self.seen:
                    self.contained = 1
                    self.expand(row, col)
                    numIslands += self.contained

        return numIslands