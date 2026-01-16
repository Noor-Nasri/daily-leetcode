class Solution:
    # For a square of size x to exist, we need to have fences at some [row, row + x] and [col, col + x]. 
    # Then rest of fences can be removed and square exists.
    # So we need largest val such that both [row, row + val] and [col, col + val] fences exist
    # We can start by computing the possible gaps in each of the fence axis, then find overlap
    # O(n^2 + m^2) which is ~720k
    
    def getAvailableGaps(self, fences):
        gaps = set()
        for ind1 in range(len(fences)):
            for ind2 in range(ind1 + 1, len(fences)):
                gaps.add(abs(fences[ind1] - fences[ind2]))

        return gaps

    def getLargestCommonGap(self, gaps1, gaps2):
        largest = -1
        for gap in gaps1:
            if gap in gaps2:
                largest = max(gap, largest)
        return largest

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences += [1, m]
        vFences += [1, n]
        gaps1, gaps2 = self.getAvailableGaps(hFences), self.getAvailableGaps(vFences) 
        best = self.getLargestCommonGap(gaps1, gaps2)

        if best == -1:
            return -1
        
        return pow(best, 2, 10**9 + 7)

