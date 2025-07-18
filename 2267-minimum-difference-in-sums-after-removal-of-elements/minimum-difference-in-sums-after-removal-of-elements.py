from heapq import heapify, heappushpop

class Solution:
    # We dont actually care about which parts are removed. We just need:
    # [min k elements before i] - [max k elements after i]

    def createSumOfBestElementsArray(self, nums, initRange, heapRange, valMultiplier):
        # track first sum, then keep storing sum of min k elements.
        # Likewise, we can get the last n elements and work backwards for max k elements with a minheap
        # we'll just use negative values to turn minheap to maxheap for the forward case

        curNums = [nums[i] * valMultiplier for i in initRange]
        curSum = valMultiplier * sum(curNums)
        sumPrefixArray = [curSum]
        heapify(curNums)

        for numInd in heapRange:
            nextVal = nums[numInd] * valMultiplier
            if nextVal > curNums[0]: 
                oldVal = heappushpop(curNums, nextVal)
                realSumDiff = (nextVal - oldVal) * valMultiplier
                curSum += realSumDiff
            
            sumPrefixArray.append(curSum)

        return sumPrefixArray

    def minimumDifference(self, nums: List[int]) -> int:
        l = len(nums)
        n = l // 3
        sumOfMinKElements = self.createSumOfBestElementsArray(
            nums, range(n), range(n, n * 2), -1
        )

        sumOfMaxKElements = self.createSumOfBestElementsArray(
            nums, range(l - 1, l - 1 - n, -1), range(l - 1 - n, l - 1 - n * 2, -1), 1
        )[::-1]
        
        minDiff = float('inf')
        for ind in range(n + 1):
            diff = sumOfMinKElements[ind] - sumOfMaxKElements[ind]
            minDiff = min(minDiff, diff)
        
        return minDiff