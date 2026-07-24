class Solution:
    # So based on num <= 1500 == (bin) 10111011100 -> max XOR is 11 ones, ie 2047
    # So my first instinct is to try and solve each value in O(n) or O(nlogn)

    # So given (chosen1, target), how can we solve for (chosen2, chosen3)?
    # We need two values which XOR to be the compliment. Ie, every mismatch is flipped
    # So why not just precompute all XORs, and store a few inds to avoid double selects?

    # I think there may be a more elegant approach, but this should work in O(n^2). 

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        numCounts = {}
        for num in nums:
            numCounts[num] = numCounts.get(num, 0) + 1

        xorPairsTotalCount = {} # [xorValue] = totalOccurances
        #xorPairsValCount = {} # [xorValue] = {[val]: numPairs in totalOccurances}

        for ind1 in range(len(nums)):
            val1 = nums[ind1]
            for ind2 in range(ind1 + 1, len(nums)):
                val2 = nums[ind2]
                pair = val1 ^ val2
                #if pair not in xorPairsValCount:
                #    xorPairsValCount[pair] = {}
                
                #xorPairsValCount[pair][val1] = xorPairsValCount[pair].get(val1, 0) + 1
                #xorPairsValCount[pair][val2] = xorPairsValCount[pair].get(val2, 0) + 1
                xorPairsTotalCount[pair] = xorPairsTotalCount.get(pair, 0) + 1
        
        total = 0
        maxTarget = 2 ** (1 + int(log(max(nums), 2)))
        for target in range(maxTarget):
            if target in numCounts:
                total += 1
                continue
            
            for initVal in numCounts:
                requiredPair = target^initVal
                pairsFound = xorPairsTotalCount.get(requiredPair, 0)

                if pairsFound: #and (numCounts[initVal] > 1 or pairsFound > xorPairsValCount[requiredPair].get(requiredPair, 0)):
                    total += 1
                    break

        return total