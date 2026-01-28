class Solution:
    # Can we do DP [x, y, k] = cost to end, but in just O(xyk)?
    # To do this, we must reduce the TP option to just one node.
    # For example, [x, y, 1] means we can only TP once, so we'd need to presolve [k = 1, cost] = bestSpot 
    # We would do this by sorting on cell cost and solving: minPathCost[cellCost] = min(curMin, new node pathCosts) 
    # Complexity: k * [grid DP sweep + sort(grid costs) + cost DP sweep] = k*gridLog(grid) = ~800k

    def getMinPathCostsAfterOptimalTP(self, pathCosts):
        costAfterTP = [[0 for c in range(self.ncol)] for r in range(self.nrow)]
        minPathCost = float('inf')

        for cellCost in self.sortedCellCosts:
            for row, col in self.cellsWithCost[cellCost]:
                minPathCost = min(minPathCost, pathCosts[row][col])
            
            for row, col in self.cellsWithCost[cellCost]:
                costAfterTP[row][col] = minPathCost

        return costAfterTP


    def extendDPLayer(self, previousLayer):
        # previousLayer is a grid[row][col] = min cost to reach end
        # We will return nextLayer, which is an updated grid costbm after allowing 1 teleport
        costAfterTP = self.getMinPathCostsAfterOptimalTP(previousLayer)
        nextLayer = [[0 for c in range(self.ncol)] for r in range(self.nrow)]
        for row in range(self.nrow - 1, -1, -1):
            for col in range(self.ncol - 1, -1, -1):
                if row == self.nrow - 1 and col == self.ncol - 1:
                    continue
                
                options = []
                if row < self.nrow - 1:
                    options.append(self.initCosts[row + 1][col] + nextLayer[row + 1][col])
                if col < self.ncol - 1:
                    options.append(self.initCosts[row][col + 1] + nextLayer[row][col + 1])
                options.append(costAfterTP[row][col])
                nextLayer[row][col] = min(options)
        
        return nextLayer

    def minCost(self, grid: List[List[int]], k: int) -> int:
        self.initCosts = grid
        self.nrow, self.ncol = len(grid), len(grid[0])
        self.cellsWithCost = {}
        self.sortedCellCosts = []
        for row in range(self.nrow):
            for col in range(self.ncol):
                cost = grid[row][col]
                if cost not in self.cellsWithCost:
                    self.cellsWithCost[cost] = []
                    self.sortedCellCosts.append(cost)
                self.cellsWithCost[cost].append((row, col))

        self.sortedCellCosts = sorted(self.sortedCellCosts)
        minPathCosts = [[float('inf') for c in range(self.ncol)] for r in range(self.nrow)]
        for _ in range(k + 1): # At i = 0, we simply build the non-teleport costs
            minPathCosts = self.extendDPLayer(minPathCosts)
        
        return minPathCosts[0][0]