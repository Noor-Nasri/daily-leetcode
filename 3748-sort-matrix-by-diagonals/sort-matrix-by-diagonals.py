class Solution:
    def sortDiag(self, grid, startRow, startCol, sortReverse):
        numbers = []
        numCells = min(len(grid) - startRow, len(grid[0]) - startCol)
        for i in range(numCells):
            row, col = startRow + i, startCol + i
            numbers.append(grid[row][col])
        
        numbers = sorted(numbers, reverse = sortReverse)
        for i in range(numCells):
            row, col = startRow + i, startCol + i
            grid[row][col] = numbers[i]


    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        for rowIndDec in range(len(grid)):
            self.sortDiag(grid, rowIndDec, 0, True)

        for colIndAsc in range(1, len(grid[0])):
            self.sortDiag(grid, 0, colIndAsc, False)
        
        return grid
