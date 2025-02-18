class Solution:
    def getAllCellsThatFlowIntoList(self, exploration):
        flowToBorder = set(exploration)
        
        while exploration:
            row, col = exploration.pop()
            
            for dr, dc in self.directions:
                nr, nc = row + dr, col + dc
                if not (0 <= nr < self.nrow and 0 <= nc < self.ncol):
                    continue
                if (nr, nc) in flowToBorder or self.heights[nr][nc] < self.heights[row][col]:
                    continue
                
                # This cell flows into our cell, so it also goes to ocean
                flowToBorder.add((nr, nc))
                exploration.append((nr, nc))

        return flowToBorder

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.nrow, self.ncol = len(heights), len(heights[0])
        self.directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1]
        ]
        
        pacficBorder = [
            (0, i) for i in range(self.ncol)
        ] + [(i, 0) for i in range(1, self.nrow)]

        atlanticBorder = [
            (self.nrow - 1, i) for i in range(self.ncol)
        ] + [(i, self.ncol - 1) for i in range(self.nrow - 1)]

        pacificFlow = self.getAllCellsThatFlowIntoList(pacficBorder)
        atlanticBorder = self.getAllCellsThatFlowIntoList(atlanticBorder)
        flowIntoBoth = pacificFlow.intersection(atlanticBorder)
        return list(flowIntoBoth)