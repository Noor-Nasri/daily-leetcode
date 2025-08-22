class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        firstRow = None
        firstCol = None
        lastRow = None
        lastCol = None
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0: continue
                
                if firstRow == None:
                    firstRow = row
                
                if firstCol == None or col < firstCol:
                    firstCol = col
                
                lastRow = row
                if lastCol == None or col > lastCol:
                    lastCol = col
        
        return (lastRow - firstRow + 1) * (lastCol - firstCol + 1)
                
                
                
        