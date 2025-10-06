from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        curQueue = [(grid[0][0], 0, 0)]
        nrow, ncol = len(grid), len(grid[0])
        connections = [
            [0, 1], [0, -1], [1, 0], [-1, 0]
        ]
        seen = set()
        while curQueue:
            cost, row, col = heappop(curQueue)
            if row == nrow -1 and col == ncol - 1:
                return cost
            
            if (row, col) in seen:
                continue
            seen.add((row, col))
            
            for dr, dc in connections:
                nr, nc = row + dr, col + dc
                if 0 <= nr < nrow and 0 <= nc < ncol and (nr, nc) not in seen:
                    pathCost = max(cost, grid[nr][nc])
                    heappush(curQueue, (pathCost, nr, nc))
            
