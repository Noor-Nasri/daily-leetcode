class Solution:
    def isMagicSquare(self, grid, rowStart, colStart):
        seen = set()
        sumRows = [0, 0, 0]
        sumCols = [0, 0, 0]
        for i in range(3):
            row = rowStart + i
            for j in range(3):
                col = colStart + j
                if grid[row][col] in seen or not (1 <= grid[row][col] <= 9): return False
    
                sumRows[i] += grid[row][col]
                sumCols[j] += grid[row][col]
                seen.add(grid[row][col])

        d1 = grid[rowStart][colStart] + grid[rowStart + 1][colStart + 1] +  grid[rowStart + 2][colStart + 2]
        d2 = grid[rowStart][colStart + 2] + grid[rowStart + 1][colStart + 1] +  grid[rowStart + 2][colStart]
        return sumRows[0] == sumRows[1] == sumRows[2] == sumCols[0] == sumCols[1] == sumCols[2] == d1 == d2

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        curCount = 0

        for row in range(len(grid) - 2):
            for col in range(len(grid[0]) - 2):
                curCount += self.isMagicSquare(grid, row, col)


        return curCount
        