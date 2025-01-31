class Solution:
    def markIsland(self, islands, row, col, curIsland):
        # Marks the island and returns number of marks made
        marked = 1
        islands[row][col] = curIsland

        for dr, dc in self.adjacencies:
            nr, nc = row + dr, col + dc
            if not (0 <= nr < len(islands) and 0 <= nc < len(islands[0])): continue
            if islands[nr][nc] != 0: continue
            marked += self.markIsland(islands, nr, nc, curIsland)

        return marked

    def largestIsland(self, grid: List[List[int]]) -> int:
        self.adjacencies = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]
        n_row, n_col = len(grid), len(grid[0])
        islands = [
            [grid[row][col]-1 for col in range(n_col)] for row in range(n_row)
        ]

        islandCounts = {}
        totalIslands = 0
        largestIsland = 0

        for row in range(n_row):
            for col in range(n_col):
                if islands[row][col] == 0:
                    totalIslands += 1
                    tot = self.markIsland(islands, row, col, totalIslands)
                    islandCounts[totalIslands] = tot
                    largestIsland = max(largestIsland, tot)

        for row in range(n_row):
            for col in range(n_col):
                if islands[row][col] != -1: continue
                connectedIslands = set()
                totalConnected = 1

                for dr, dc in self.adjacencies:
                    nr, nc = row + dr, col + dc
                    if not (0 <= nr < n_row and 0 <= nc < n_col): continue
                    if islands[nr][nc] == -1 or islands[nr][nc] in connectedIslands: continue
                    connectedIslands.add(islands[nr][nc])
                    totalConnected += islandCounts[islands[nr][nc]]

                largestIsland = max(largestIsland, totalConnected)

        return largestIsland

        

