class Solution:
    # Obviously needs BS, might be a bit annoying to implement BFS per BS
    # Should be O(r*c*log(r*c)) which is 20000log(20000, 2) < 300k
    def exploreNeighbours(self, visited, nextLayer, row, col):
        for dr, dc in self.connections:
            newRow, newCol = row + dr, col + dc
            newNode = (newRow, newCol)
            if not (1 <= newRow <= self.nrow and 1 <= newCol <= self.ncol) or newNode in visited:
                continue
            
            visited.add(newNode)
            nextLayer.append(newNode)
        
    def canReachBottom(self, curDay):
        #print("Going to try to reach bottom on day", curDay)
        visited = set()
        for day in range(curDay):
            visited.add(self.cells[day])
        
        layer = []
        for col in range(1, self.ncol + 1):
            node = (1, col)
            if node in visited:
                continue

            layer.append(node)
            visited.add(node)
        
        while layer:
            #print("Current layer:", layer)
            nextLayer = []
            for row, col in layer:
                if row == self.nrow:
                    #print("Found the last row!")
                    return True
                self.exploreNeighbours(visited, nextLayer, row, col)

            layer = nextLayer

        return False
        

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        self.cells = [tuple(e) for e in cells]
        self.nrow = row
        self.ncol = col
        self.connections = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]

        low = 0
        high = len(cells)
        best = 0

        while low <= high:
            mid = (low + high)//2
            if self.canReachBottom(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1

        return best