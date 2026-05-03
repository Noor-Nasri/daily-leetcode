class Solution:
    # At each column, we can choose tbe number of black rows (0->n)
    # Those decisions lead to a score - if we can contextualize this as DP it should work
    # The issue is that a column's value is based on BOTH prev and next
    # So at col=x, we pick numBlack=y. Then col x-1 is scored based on:
    # [numBlack_x, numBlack_(x-1), numBlack_(x-2)]. So stuck on n^4

    # BUT: we don't need both previous columns at once!
    # IF we have LESS black nodes than the last column, we only need to know prevBlack
    # IF we have MORE, then we actually care about firstViableInd, which is >= prevBlack
    
    # Thinking on this a lot: The best structure is to pre-determine colContributesToPrev
    # If YES: lastVal = max(col-1, col-2). Iterate on [lastVal + 1, n] and count last col value.
    # if NO: lastVal = col-1. Iterate across all n and count current col value.

    def solveMaxScore(self, curCol, colContributesToPrev, lastVal):
        uid = (curCol, colContributesToPrev, lastVal)
        if uid in self.sols:
            return self.sols[uid]
        elif curCol == self.ncol:
            return 0
        
        bestSolution = 0
        if colContributesToPrev:
            maxBlackInBothPrev = lastVal
            for numBlack in range(maxBlackInBothPrev + 1, self.nrow + 1):
                bonus = self.colSumGraph[numBlack - 1][curCol - 1]
                if maxBlackInBothPrev:
                    bonus -= self.colSumGraph[maxBlackInBothPrev - 1][curCol - 1]
                
                op1 = bonus + self.solveMaxScore(curCol + 1, True, numBlack)
                op2 = bonus + self.solveMaxScore(curCol + 1, False, numBlack)
                bestSolution = max(bestSolution, op1, op2)
        else:
            lastNumBlack = lastVal
            for numBlack in range(self.nrow + 1):
                bonus = 0
                if numBlack < lastNumBlack:
                    bonus = self.colSumGraph[lastNumBlack - 1][curCol]
                    if numBlack:
                        bonus -= self.colSumGraph[numBlack - 1][curCol]

                op1 = bonus + self.solveMaxScore(curCol + 1, True, max(lastNumBlack, numBlack))
                op2 = bonus + self.solveMaxScore(curCol + 1, False, numBlack)
                bestSolution = max(bestSolution, op1, op2)
        
        self.sols[uid] = bestSolution
        return bestSolution

    def maximumScore(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        colSumGraph = [[grid[row][col] for col in range(ncol)] for row in range(nrow)]
        for row in range(1, nrow):
            for col in range(ncol):
                colSumGraph[row][col] += colSumGraph[row - 1][col]
        
        self.nrow, self.ncol, self.sols, self.colSumGraph = nrow, ncol, {}, colSumGraph
        return self.solveMaxScore(0, False, 0)
        