class Solution:
    # Just go row by row then later col by col, and need sum to be half of total sum
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        totalSum = 0
        for row in grid:
            for val in row:
                totalSum += val
        targetSum = totalSum / 2

        sumFromRows = 0
        for row in range(len(grid) - 1):
            for col in range(len(grid[row])):
                sumFromRows += grid[row][col]
            
            if sumFromRows == targetSum:
                return True
            elif sumFromRows > targetSum:
                break
        
        sumFromCols = 0
        for col in range(len(grid[0]) - 1):
            for row in range(len(grid)):
                sumFromCols += grid[row][col]
            
            if sumFromCols == targetSum:
                return True
            elif sumFromCols > targetSum:
                break
        
        return False

        