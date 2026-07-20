class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        nrow, ncol = len(grid), len(grid[0])
        newArr = [[-1 for c in range(ncol)] for r in range(nrow)]

        for row in range(nrow):
            for col in range(ncol):
                shifted1D = (row * ncol + col + k) % (nrow * ncol) 
                shiftedRow = shifted1D // ncol
                shiftedCol = shifted1D % ncol
                
                newArr[shiftedRow][shiftedCol] = grid[row][col]
        
        return newArr