class Solution:
    # Obv we can just count, but we can really optimize this..
    # When a negative number shows up, it means all nums to the right corner are also negative.
    
    # To find (X, min Y), we can go to y/2 and look at the last number. If its >= 0, that means no number in top half is < 0
    # So we can actually find the earliest Y in log(rows), then do BS again to find the exact (X, Y).

    # The problem is that each row can introduce a single new element to the rectangle, like a staircase.
    # So we will need to loop on all rows anyways. We can either do BS per row, or just maintain the pointer.
    # So the overall complexity becomes the choice of O(n + m) or O(nlogm)

    # Cleanest solution: Start from last row, and add one row at a time with a pointer for column 

    def countNegatives(self, grid: List[List[int]]) -> int:
        numNegatives = 0
        firstNegativeColInd = 0
        for rowInd in range(len(grid) - 1, -1, -1):
            while firstNegativeColInd < len(grid[rowInd]) and grid[rowInd][firstNegativeColInd] >= 0:
                firstNegativeColInd += 1
            
            numNegatives += len(grid[rowInd]) - firstNegativeColInd
        
        return numNegatives