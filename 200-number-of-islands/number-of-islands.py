class Solution:
    def floodfill(self, grid, row, col, newVal):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): return
        if grid[row][col] == 0 or grid[row][col] == newVal: return

        grid[row][col] = newVal
        self.floodfill(grid, row - 1, col, newVal)
        self.floodfill(grid, row + 1, col, newVal)
        self.floodfill(grid, row, col - 1, newVal)
        self.floodfill(grid, row, col + 1, newVal)


    def numIslands(self, grid: List[List[str]]) -> int:
        newGrid = [[int(e == "1") for e in lis] for lis in grid]

        found = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if newGrid[row][col] == 1:
                    found += 1
                    self.floodfill(newGrid, row, col, found + 1)
        
        return found

        