class Solution:
    # Seems like a simple question: Go through each node, figure out where it ends up, and copy it there
    # We can do this by stretching each perimeter to a line, ie pos 0 is first and 1 is the node to the right.
    # Then we just needo (p - k) % s and use helpers to convert positions

    def getPosFromFlat(self, layer, layerWidth, layerHeight, point):
        # Point 0 is at [layer, layer]
        # Incrementing point moves it clockwise across layerWidth x layerHeight
        startRow, startCol = layer, layer
        endRow, endCol = layer + layerHeight - 1, layer + layerWidth - 1

        if point < layerWidth:
            diff = point
            return (startRow, startCol + diff)
        
        elif point < layerWidth + layerHeight - 1:
            diff = point - layerWidth + 1
            return (startRow + diff, endCol)
        
        elif point < 2*layerWidth + layerHeight - 2:
            diff = point - (layerWidth + layerHeight) + 2
            return (endRow, endCol - diff)
        
        else:
            diff = point - (2*layerWidth + layerHeight) + 3
            return (endRow - diff, startCol)



    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nrow, ncol = len(grid), len(grid[0])
        finalGrid = [[0 for i in range(ncol)] for r in range(nrow)]
        numLayers = min(nrow, ncol) // 2

        for layer in range(numLayers):
            layerWidth = ncol - layer*2
            layerHeight = nrow - layer*2
            cycleSize = layerWidth * 2 + layerHeight * 2 - 4

            for point in range(cycleSize):
                shiftedPoint = (point - k) % cycleSize
                r1, c1 = self.getPosFromFlat(layer, layerWidth, layerHeight, point)
                r2, c2 = self.getPosFromFlat(layer, layerWidth, layerHeight, shiftedPoint)
                #print(f"Point {point} is at ({r1, c1}) which shifts to point {shiftedPoint} at ({r2, c2})")
                finalGrid[r2][c2] = grid[r1][c1]

        return finalGrid