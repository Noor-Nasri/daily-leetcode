from heapq import heappop, heappush
class Solution:
    def solveDistsInGrid(self, grid):
        n_row, n_col = len(grid), len(grid[0])
        distances = [[0 for i in range(n_col)] for row in range(n_row)]
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        options = [
            (grid[0][0] + 1, 0, 0)
        ]

        maxVal = 0

        while options:
            minDist, row, col = heappop(options)
            if distances[row][col] > 0: 
                continue
            distances[row][col] = minDist
            maxVal = max(maxVal, minDist)

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < n_row and 0 <= nc < n_col):
                    continue
                if distances[nr][nc] > 0:  
                    continue
                
                heappush(options, (
                    max(minDist, grid[nr][nc] + 1),
                    nr, 
                    nc
                ))
        return distances, maxVal


    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # Greedy ideas: Have each query take as much as possible
        # Need to re-arrange grid to be [row][col] = min val needed to reach
        # Then need to rearrange this to [val] = total points possible
        # Single pass through queries after this

        distances, maxVal = self.solveDistsInGrid(grid)
        pointDists = [0 for i in range(maxVal + 1)]
        for row in distances:
            for val in row:
                pointDists[val] += 1

        curTot = 0 # v = 3 can get all the nodes v = 2 gets
        for ind in range(len(pointDists)):
            pointDists[ind] += curTot
            curTot = pointDists[ind]
        
        points =[]
        for query in queries:
            points.append(pointDists[min(query, maxVal)])
        
        return points