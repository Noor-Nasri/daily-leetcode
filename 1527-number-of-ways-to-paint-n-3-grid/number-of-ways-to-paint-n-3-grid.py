class Solution:
    # This feels like it has a closed math equation that allows backtracking but whatever
    # We can do DP: (rowInd, lastRowCols) and try all combinations for row
    # O(r * 12 * 27) which is just O(r) and ~1mil iterations

    def numCombosFromRow(self, rowInd, lastRow):
        if rowInd == self.n:
            return 1
        
        uid = (rowInd, lastRow)
        if uid in self.sols:
            return self.sols[uid]
        
        validCombos = 0
        for col1 in range(1, 4):
            if col1 == lastRow[0]:
                continue

            for col2 in range(1, 4):
                if col2 == col1 or col2 == lastRow[1]:
                    continue

                for col3 in range(1, 4):
                    if col3 == col2 or col3 == lastRow[2]:
                        continue
                    
                    newCombos = self.numCombosFromRow(rowInd + 1, (col1, col2, col3))
                    validCombos += newCombos
                    validCombos %= 10**9 + 7
        

        self.sols[uid] = validCombos
        return validCombos
        
    def numOfWays(self, n: int) -> int:
        self.n = n
        self.sols = {}
        return self.numCombosFromRow(0, (0,0,0))