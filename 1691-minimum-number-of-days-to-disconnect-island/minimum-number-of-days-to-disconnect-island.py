class Solution:
    def countIslands(self, grid):
        seen = set()
        numParts = 0

        def floodfill(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])): return
            if (row, col) in seen or not grid[row][col]: return
            seen.add((row, col))
            floodfill(row - 1, col)
            floodfill(row + 1, col)
            floodfill(row, col - 1)
            floodfill(row, col + 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and not (row, col) in seen:
                    numParts += 1
                    floodfill(row, col)
        
        return numParts

    def minDays(self, grid: List[List[int]]) -> int:
        # the solution is either 0, 1, or 2
        # either already disconnected, or cut a central piece, or isolate a corner
        
        
        if self.countIslands(grid) != 1: 
            return 0 #nothing to change


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not grid[row][col]: continue

                grid[row][col] = 0
                if self.countIslands(grid) != 1:
                    return 1
                grid[row][col] = 1

        return 2

        