class Solution:
    # This is tricky because if a char is out of place, you may want to get rid of the prev one instead
    # Can we do DP? Given cur ind and last included ind, return min num of inds to remove.
    # At each ind: If all rows still in order, we may keep it. Can always remove it.
    # O(strLen * strLen * n) .. 10^6 is okay

    def minRemovalsAfterIncludingInd(self, curInd, lastIncludedInd):
        uid = (curInd, lastIncludedInd)
        if uid in self.sols:
            return self.sols[uid]
        elif curInd == len(self.strs[0]):
            return 0
        
        bestOption = 1 + self.minRemovalsAfterIncludingInd(curInd + 1, lastIncludedInd)
        for rowInd in range(len(self.strs)):
            if lastIncludedInd >= 0 and self.strs[rowInd][curInd] < self.strs[rowInd][lastIncludedInd]:
                break
        else:
            bestOption = min(bestOption, self.minRemovalsAfterIncludingInd(curInd + 1, curInd))

        self.sols[uid] = bestOption
        return self.sols[uid]

    def minDeletionSize(self, strs: List[str]) -> int:
        self.strs = strs
        self.sols = {}
        ans = self.minRemovalsAfterIncludingInd(0, -1)
        return ans