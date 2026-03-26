class Solution:
    # Okay, so we would normally do this as a line sweep for the target sum.
    # Issues: There are n*m different target sums, since we can adjust total sum

    # Example: total sum is 12, so we sweep until 6. 
    # But if we hit 7 | 5, and [2] is on the left, it is valid
    # Same if we hit 5 | 7 and [2] is on the right. 

    # SO - we should maintain a moving dict of valid sums, based on which values are left/right
    # Simpler approach: Just maintain valid sum based on sweeped values, and sweep both ways
    # Final wrinkle: If only one row/col - can't pick anything in the middle

    def addPossibleSum(self, validSums, targetSum, exclusion):
        optionalSum = targetSum + exclusion/2
        if optionalSum % 1 == 0:
            validSums.add(round(optionalSum))

    def sweepRows(self, grid, targetSum, rowRange):
        validSums = set()
        self.addPossibleSum(validSums, targetSum, 0)

        firstRow = True
        currentSum = 0
        ncol = len(grid[0])
        
        for row in rowRange:
            for col in range(ncol):
                currentSum += grid[row][col]
                if ncol > 1 and (not firstRow or col == 0 or col == ncol-1):
                    self.addPossibleSum(validSums, targetSum, grid[row][col])
            
            if currentSum in validSums:
                return True
            elif ncol == 1:
                if currentSum - grid[rowRange[0]][0] == targetSum - grid[rowRange[0]][0]/2:
                    return True
                elif currentSum - grid[row][0] == targetSum - grid[row][0]/2:
                    return True
            
            if ncol > 1 and firstRow:
                firstRow = False
                for col in range(1, ncol - 1):
                    self.addPossibleSum(validSums, targetSum, grid[row][col])

        return False


    
    def sweepCols(self, grid, targetSum, colRange):
        validSums = set()
        self.addPossibleSum(validSums, targetSum, 0)

        firstCol = True
        currentSum = 0
        nrow = len(grid)
        
        for col in colRange:
            for row in range(nrow):
                currentSum += grid[row][col]
                if nrow > 1 and (not firstCol or row == 0 or row == nrow-1):
                    self.addPossibleSum(validSums, targetSum, grid[row][col])
                
            if currentSum in validSums:
                return True
            elif nrow == 1:
                if currentSum - grid[0][colRange[0]] == targetSum - grid[0][colRange[0]]/2:
                    return True
                elif currentSum - grid[0][col] == targetSum - grid[0][col]/2:
                    return True
            
            if nrow > 1 and firstCol:
                firstCol = False
                for row in range(1, nrow - 1):
                    self.addPossibleSum(validSums, targetSum, grid[row][col])

        return False

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        totalSum = 0
        for row in grid:
            for val in row:
                totalSum += val
        
        targetSum = totalSum/2
        return any(
            [
                self.sweepRows(grid, targetSum, range(len(grid) - 1)),
                self.sweepRows(grid, targetSum, range(len(grid) - 1, 0, -1)),
                self.sweepCols(grid, targetSum, range(len(grid[0]) - 1)),
                self.sweepCols(grid, targetSum, range(len(grid[0]) - 1, 0, -1))
            ]
        )
        