from collections import deque 

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [
            [0, 1], [0, -1], [1, 0], [-1, 0], 
        ]
        
        seen = set()
        paths = deque([(0, 0, 0)])

        while paths:
            row, col, cost = paths.popleft()
            
            # skim unseen path as if same cost
            while (row, col) not in seen and (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                seen.add((row, col))
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return cost
                
                dr_free, dc_free = directions[grid[row][col] - 1]

                # add adjacents as a new branch
                for dr, dc in directions:
                    if dr == dr_free and dc == dc_free: continue

                    nr, nc = row + dr, col + dc
                    if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])) and (nr, nc) not in seen:
                        paths.append((nr, nc, cost + 1))

                row, col = row + dr_free, col + dc_free

        assert(False)
        return -1 