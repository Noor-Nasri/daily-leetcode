class Solution:
    # We can always make everything equal to limit+1 in n/2 moves
    # To beat that, we need to match an existing pair
    # The only computation is: for a pair and desired sum, is it 1 or 2 moves?
    # Then we need to apply that for all existing sums in just O(N)

    # So: Every time we consider a sum, we have a split for currentSum > or < desiredSum
    # For smaller pairs: 2 moves iff desiredSum > currentSum + (limit - minVal)
    # For larger pairs: 2 moves iff minVal > desiredSum - 1

    # Iterate on sum, track 2p for maxPotential < desiredSum and minVal > desiredSum

    def minMoves(self, nums: List[int], limit: int) -> int:
        # Since we will always look at non-overlapping sections, we can forget the actual pairs
        pairSumCounts = {}
        sortedMinVals = []
        sortedMaxReaches = []
        n = len(nums)

        for ind in range(n // 2):
            v1, v2 = nums[ind], nums[n - 1 - ind]
            currentSum = v1 + v2
            minVal = min(v1, v2)
            maxReach = currentSum + (limit - minVal)

            pairSumCounts[currentSum] = pairSumCounts.get(currentSum, 0) + 1
            sortedMinVals.append(minVal)
            sortedMaxReaches.append(maxReach)
            #print(v1, v2, "have total", currentSum, "and minVal", minVal, "with maxreach", maxReach)
        
        sortedSums = sorted(list(pairSumCounts.keys()))
        sortedMinVals = sorted(sortedMinVals)
        sortedMaxReaches = sorted(sortedMaxReaches)
        #print(pairSumCounts, sortedMinVals, sortedMaxReaches)

        best = n // 2
        indFirstPairIncreasable = 0 # First ind where maxPotential >= desiredSum
        indFirstPairNotDecreasable = 0 # First ind where minVal >= desiredSum
        for desiredSum in sortedSums:
            while sortedMaxReaches[indFirstPairIncreasable] < desiredSum:
                indFirstPairIncreasable += 1
            
            while indFirstPairNotDecreasable < len(sortedMinVals) and sortedMinVals[indFirstPairNotDecreasable] < desiredSum:
                indFirstPairNotDecreasable += 1

            nPairsNeedDoubleRaise = indFirstPairIncreasable
            nPairsNeedDoubleLower = len(sortedMinVals) - indFirstPairNotDecreasable
            totalMoves = n//2 - pairSumCounts[desiredSum] + nPairsNeedDoubleRaise + nPairsNeedDoubleLower
            best = min(best, totalMoves)

        return best

