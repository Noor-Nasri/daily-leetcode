class Solution:
    def populateIsland(self, grid, islands, row, col, newVal):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): return
        if not grid[row][col]: return
        if islands[row][col]: return

        islands[row][col] = newVal
        self.populateIsland(grid, islands, row + 1, col, newVal)
        self.populateIsland(grid, islands, row - 1, col, newVal)
        self.populateIsland(grid, islands, row, col + 1, newVal)
        self.populateIsland(grid, islands, row, col - 1, newVal)


    def solveIslands(self, grid):
        islands = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        curIslands = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] and not islands[row][col]:
                    curIslands += 1
                    self.populateIsland(grid, islands, row, col, curIslands)
        
        return islands
                    
    def floodfillComparison(self, expected1, expected2, row, col, visited):
        if row < 0 or row >= len(self.islands2) or col < 0 or col >= len(self.islands2[0]): return True
        if self.islands2[row][col] != expected2: return True
        
        if self.islands1[row][col] != expected1:
            # subgroup still going, but main group died off
            return False 
        
        visited.add((row, col))
        checks = []
        for nRow, nCol in [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]:
            if not (nRow, nCol) in visited:
                checks.append(
                    self.floodfillComparison( expected1, expected2, nRow, nCol, visited),
                )
            
        return all(checks)


    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        #self.islands1 = self.solveIslands(grid1)
        self.islands1 = grid1 # Turns out, no need to solve islands for grid1. Land is enough
        self.islands2 = self.solveIslands(grid2)

        checked = set()
        total = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[row])):
                if (self.islands2[row][col] > 0) and not (self.islands2[row][col] in checked):
                    expected2 = self.islands2[row][col]
                    checked.add(expected2)

                    if self.islands1[row][col] == 0: continue # island already broken
                    contained = self.floodfillComparison(self.islands1[row][col], self.islands2[row][col], row, col, set())
                    if contained:
                        total += 1
        
        return total

        