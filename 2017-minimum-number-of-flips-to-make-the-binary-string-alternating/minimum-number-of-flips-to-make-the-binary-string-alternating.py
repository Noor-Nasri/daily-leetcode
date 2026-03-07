class Solution:
    # Type 1 just means we can choose where we start, and it loops back to it funny
    # So if we do 5 appends, it means we need to know how to solve [5->n] as well as [0->5]
    # except that 0->5 is backwards because of the append order.
    # So we just need to do an O(n) sweep that knows the cost of each ind at O(1)

    def minFlips(self, s: str) -> int:
        costForwardFromStartValFromInd = [[0, 0] for i in range(len(s))]
        costBackwardFromStartValFromInd = [[0, 0] for i in range(len(s))]
        vals = [int(e) for e in s]
        
        for ind in range(len(vals) -1, -1, -1):
            costForwardFromStartValFromInd[ind][1 - vals[ind]] += 1
            if ind + 1 < len(vals):
                costForwardFromStartValFromInd[ind][0] += costForwardFromStartValFromInd[ind + 1][1]
                costForwardFromStartValFromInd[ind][1] += costForwardFromStartValFromInd[ind + 1][0]
        
        for ind in range(len(vals)):
            costBackwardFromStartValFromInd[ind][1 - vals[ind]] += 1
            if ind:
                costBackwardFromStartValFromInd[ind][0] += costBackwardFromStartValFromInd[ind - 1][1]
                costBackwardFromStartValFromInd[ind][1] += costBackwardFromStartValFromInd[ind - 1][0]

        
        minCost = len(s)
        for numAppends in range(len(vals)):
            for initVal in range(2):
                cost = costForwardFromStartValFromInd[numAppends][initVal]
                if numAppends:
                    if len(s) % 2 == 0:
                        lastVal = 1 - initVal
                    else:
                        lastVal = initVal

                    cost += costBackwardFromStartValFromInd[numAppends - 1][lastVal]
                if cost < minCost:
                    minCost = cost
                    
        
        return minCost

        
