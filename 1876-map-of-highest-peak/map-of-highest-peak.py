from collections import deque 

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # Start at all the waters, set their adjacencies to 1. Then 2 etc
        n_row, n_col = len(isWater), len(isWater[0])
        heights = [[-1 for col in range(n_col)] for row in range(n_row)]
        connections = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]
        nodes = deque()
        
        for row in range(n_row):
            for col in range(n_col):
                if isWater[row][col]:
                    nodes.append([row, col, 0])
        
        while nodes:
            row, col, curLevel = nodes.popleft()
            if heights[row][col] > -1: 
                continue
            heights[row][col] = curLevel

            for dr, dc in connections:
                nr, nc = row + dr, col + dc

                if not (0 <= nr < n_row and 0 <= nc < n_col) or heights[nr][nc] > -1:
                    continue
                
                nodes.append([nr, nc, curLevel + 1])


        
        return heights
