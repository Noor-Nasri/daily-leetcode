class Solution:
    # We can do this by sweeping one row at a time, essentially scanning for the bottom right node
    # For each column, we consider the added sum of this new row so far, and if we can combine it with the previous rect sum.
    # If yes, then this node is a new bottom right corner. If not, theres no more sums to be achieved in this row.

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        sumOfRectUntilCol = [0 for i in range(len(grid[0]))]
        colLimit = len(grid[0])
        numMatrices = 0  

        for row in range(len(grid)):
            curSum = 0
            for col in range(colLimit):
                curSum +=  grid[row][col]
                if sumOfRectUntilCol[col] + curSum <= k:
                    sumOfRectUntilCol[col] += curSum
                    numMatrices += 1
                else:
                    colLimit = col
                    break


        return numMatrices