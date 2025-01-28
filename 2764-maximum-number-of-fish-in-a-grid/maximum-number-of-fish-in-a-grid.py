class Solution:
    def floodfill(self, islands, grid, row, col):
        islands[row][col] = True
        total = grid[row][col]

        for dr, dc in self.adjacencies:
            nr, nc = row + dr, col + dc

            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) or not grid[nr][nc] or islands[nr][nc]:
                continue
            
            total += self.floodfill(islands, grid, nr, nc)
        
        return total


        
    
    def findMaxFish(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        self.adjacencies = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]
        islands = [[False for c in range(n_col)] for r in range(n_row)]
        maxCatch = 0

        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] and not islands[row][col]:
                    #print("Looking at island in", row, col)
                    option = self.floodfill(islands, grid, row, col)
                    #print(option)
                    maxCatch = max(maxCatch, option)
        
        return maxCatch

