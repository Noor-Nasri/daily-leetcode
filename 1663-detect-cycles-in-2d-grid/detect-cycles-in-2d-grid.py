class Solution:
    # Simple graph traversal: DFS each node
    # If we end up at the same cell without moving backwards, theres a cycle.
    # All cycles are len >= 4 so we don't have to worry about anything else.
    # Since we ignore nodes if they got reached, the whole thing is O(N)

    def expand(self, grid, seen, prevPos, pos):
        if pos in seen:
            return True
        seen.add(pos)
        
        for dr, dc in self.connections:
            adj = (pos[0] + dr, pos[1] + dc)
            if adj == prevPos or not (0 <= adj[0] < self.nrow and 0 <= adj[1] < self.ncol):
                continue
            elif grid[adj[0]][adj[1]] == grid[pos[0]][pos[1]]:
                if self.expand(grid, seen, pos, adj):
                    return True
        
        return False


    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.nrow, self.ncol = len(grid), len(grid[0])
        self.connections = [
            [1, 0], [0, 1], [-1, 0], [0, -1]
        ]

        seen = set()
        for row in range(self.nrow):
            for col in range(self.ncol):
                if (row, col) in seen:
                    continue
                
                if self.expand(grid, seen, None, (row, col)):
                    return True
        
        return False