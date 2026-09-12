class Solution:
    # The immediate thought is DP on (val, remaining) but val <= 10**9
    # But since n is 5 * 10^4, cant we just do (ind, remaining) on sorted vals?
    # Then choosing to include an ind just means jumping to first start > chosen end
    # Can jump with BS or precompute with a sweep + minheap

    # The only trick left is the tie breaker. Our DP needs to return
    # (max score, chosenInds) where inds are minimized. 
    # Should all be solvable, not that hard.

    def getBetter(self, score1, inds1, score2, inds2):
        # Want max score then tie breaker on min list
        if score1 > score2:
            return score1, inds1
        elif score1 < score2:
            return score2, inds2
        
        for ind in range(min(len(inds1), len(inds2))):
            if inds1[ind] < inds2[ind]:
                return score1, inds1
            elif inds1[ind] > inds2[ind]:
                return score2, inds2
        
        if len(inds1) < len(inds2):
            return score1, inds1
        else:
            return score2, inds2

    def solveBestIntervals(self, curInd, remainingCount):
        uid = (curInd, remainingCount)
        if remainingCount == 0 or curInd == self.n:
            return (0, [])
        elif uid in self.sols:
            return self.sols[uid]
        
        score1, inds1 = self.solveBestIntervals(curInd + 1, remainingCount)
        score2, inds2 = self.solveBestIntervals(self.earliestNextInd[curInd], remainingCount - 1)
        score2 += self.intervals[curInd][2]
        inds2 = sorted(inds2 + [self.intervals[curInd][3]])

        maxScore, inds = self.getBetter(score1, inds1, score2, inds2)
        self.sols[uid] = (maxScore, inds)
        return self.sols[uid]


    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sortedIntervals = sorted(
           [intervals[ind] + [ind] for ind in range(n)]
        )

        # first construct a next pointer for each ind
        earliestNextInd = [n for i in range(n)]
        curAvail = []
        for ind in range(n):
            l, r, _, _ = sortedIntervals[ind]
            while curAvail and l > curAvail[0][0]:
                _, prevInd = heappop(curAvail)
                earliestNextInd[prevInd] = ind
            
            heappush(curAvail, (r, ind))

        self.intervals = sortedIntervals
        self.earliestNextInd = earliestNextInd
        self.n = n
        self.sols = {}
        maxScore, inds = self.solveBestIntervals(0, 4)
        return inds