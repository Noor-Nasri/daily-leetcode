class Solution:
    # Seems like simple greedy to me: One ind at a time, if any str is out of place we must remove the column
    # Caviat: If a prev ind is already strictly smaller, then next elements can be whatever they want

    def minDeletionSize(self, strs: List[str]) -> int:
        rowEqualToAbove = [True for i in range(len(strs))]
        rowEqualToAbove[0] = False
        numBroken = 0

        for charInd in range(len(strs[0])):
            rowsThatBecomeUnEqual = set()
            validCol = True
            last = ''
            for strInd in range(len(strs)):
                cur = strs[strInd][charInd]
                if rowEqualToAbove[strInd]:
                    if cur > last:
                        rowsThatBecomeUnEqual.add(strInd)
                    elif cur < last:
                        validCol = False
                        break
                last = cur

            if validCol:
                for rowInd in rowsThatBecomeUnEqual:
                    rowEqualToAbove[rowInd] = False
            else:
                numBroken += 1

        return numBroken
        