class Solution:
    def numOnesInRect(self, minRow, minCol, maxRow, maxCol):
        numZeroToMax = self.prefixMatrix[maxRow][maxCol]
        numToLeft = minRow and self.prefixMatrix[minRow - 1][maxCol]
        numAbove = minCol and self.prefixMatrix[maxRow][minCol - 1]
        numTopLeftCorner = minRow and minCol and self.prefixMatrix[minRow - 1][minCol - 1]
        return numZeroToMax - numToLeft - numAbove + numTopLeftCorner

    def solveOneRect(self, minRow, minCol, maxRow, maxCol):
        # We just need to know the min/max row/col of all the 1s in this bbox.
        # We can do this with just O(rows + cols), by doing a simple loop and checking if the bbox to the left has all 0s or not
        if not (0 <= minRow <= maxRow < self.nrow and 0 <= minCol <= maxCol < self.ncol):
            return -1
        
        uid = (minRow, minCol, maxRow, maxCol)
        if uid in self.solOne:
            return self.solOne[uid]

        # Do I need to do binary search to pass TLE here ? Should be doable .. gonna memoize first
        for boundsLeft in range(minCol, maxCol + 1):
            if self.numOnesInRect(minRow, boundsLeft, maxRow, boundsLeft): break
        
        for boundsRight in range(maxCol, minCol - 1, -1):
            if self.numOnesInRect(minRow, boundsRight, maxRow, boundsRight): break
        
        for boundsTop in range(minRow, maxRow + 1):
            if self.numOnesInRect(boundsTop, minCol, boundsTop, maxCol): break

        for boundsBottom in range(maxRow, minRow -1, -1):
            if self.numOnesInRect(boundsBottom, minCol, boundsBottom, maxCol): break
        
        if boundsLeft > boundsRight or boundsTop > boundsBottom:
            self.solOne[uid] = -1
        else:
            self.solOne[uid] = int((boundsRight - boundsLeft + 1) * (boundsBottom - boundsTop + 1))
            
        return self.solOne[uid]

    def solveTwoRects(self, minRow, minCol, maxRow, maxCol):
        best = -1
        uid = (minRow, minCol, maxRow, maxCol)
        if uid in self.solTwo:
            return self.solTwo[uid]

        for row in range(self.nrow):
            for col in range(self.ncol):
                options = [
                    [ self.solveOneRect(minRow, minCol, row, maxCol), self.solveOneRect(row + 1, minCol, maxRow, maxCol) ],
                    [ self.solveOneRect(minRow, minCol, maxRow, col), self.solveOneRect(minRow, col + 1, maxRow, maxCol) ],
                ]

                for x, y in options:
                    if x != -1 and y != -1 and (best == -1 or x + y < best):
                        best = x + y

        self.solTwo[uid] = best
        return self.solTwo[uid]

    def minimumSum(self, grid: List[List[int]]) -> int:
        # We want to pick as few 0s as possible while selecting all the 1s with exactly (3) rects
        # For one rect, its an easy bbox.

        # Trying to force a cell to be the "bottom right" of a rect doesn't make finding the full rect easy, because there are many possible starts.
        # One thing I do notice: In any config, there will be a point where slicing horizontal or vertical will lead to two rects in one half and one rect in the other.
        # This will always happen because there is no overlap. Imagine one rect is there, and you need to put another somewhere. Obv a line between them. 
        # Then the third rect goes to the side or along the same line, and we can always slice it.

        # Meaning: For every point, we can consider the four configs: one rect up, two rects down, etc etc.
        # If a half has only one rect, we just find all boxes inside.
        # For the half with two rects, we do this same thing again. Every cell, etc. leading to two sections, each with one 

        # So, what we really need is: Given a BBox, whats the smallest rect that covers all points? We can use 2d prefix sums and binary search for the two corners.
        self.grid = grid
        self.nrow = len(grid)
        self.ncol = len(grid[0])
        self.prefixMatrix = [ [0 for _ in range(self.ncol)] for _ in range(self.nrow)]

        for row in range(self.nrow):
            numInRow = 0
            for col in range(self.ncol):
                numInRow += grid[row][col] 
                numOnes = numInRow + (row and self.prefixMatrix[row - 1][col])
                self.prefixMatrix[row][col] = numOnes

        self.solOne = {}
        self.solTwo = {}
        best = self.nrow * self.ncol
        
        for row in range(self.nrow):
            for col in range(self.ncol):
                options = [
                    [ self.solveOneRect(0, 0, row, self.ncol - 1), self.solveTwoRects(row + 1, 0, self.nrow - 1, self.ncol - 1) ],
                    [ self.solveTwoRects(0, 0, row, self.ncol - 1), self.solveOneRect(row + 1, 0, self.nrow - 1, self.ncol - 1) ],
                    [ self.solveOneRect(0, 0, self.nrow - 1, col), self.solveTwoRects(0, col + 1, self.nrow - 1, self.ncol - 1) ],
                    [ self.solveTwoRects(0, 0, self.nrow - 1, col), self.solveOneRect(0, col + 1, self.nrow - 1, self.ncol - 1) ],
                ]

                for x, y in options:
                    if x != -1 and y != -1 and x + y < best:
                        best = x + y
        
        return best
    