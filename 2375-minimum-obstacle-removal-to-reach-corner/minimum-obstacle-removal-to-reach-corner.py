from collections import deque
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        seen = {(0, 0)}
        seen_future = set()
        nextLayerObstacles = deque()
        numRemoved = 0
        current = deque([[0, 0]])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while True:
            if not current:
                numRemoved += 1
                while nextLayerObstacles:
                    row, col = nextLayerObstacles.popleft()
                    if (row, col) not in seen:
                        seen.add((row, col))
                        current.append([row, col])
            
            nextLvl = deque()
            while current:
                row, col = current.popleft()
                if row == len(grid) - 1 and col == len(grid[0]) - 1:
                    return numRemoved

                for row_diff, col_diff in dirs:
                    nr, nc = row + row_diff, col + col_diff
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            if (nr, nc) not in seen_future:
                                nextLayerObstacles.append([nr, nc])
                                seen_future.add((nr, nc))
                        elif (nr, nc) not in seen:
                            nextLvl.append([nr, nc])
                            seen.add((nr, nc))
            
            current = nextLvl
