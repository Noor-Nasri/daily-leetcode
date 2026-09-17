class Solution:
    # Finding all subarrays == target can be done with a two pointers approach
    # We just expand till > target, then shrink, etc. When we find a match, we move both pointers 1 over
    # Once we have isolated (start, end) array, we need to compute a minArrayLenUntilInd[i]
    # Then we just compare each arr with the min prev.

    # So two pointer to build validArray[start] = end, then sweep to solve minPair

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        arrLenAtStartInd = [None for i in range(len(arr))]
        arrLenAtEndInd = [None for i in range(len(arr))]
        firstArrayEnd = None
        startInd = 0
        curSum = 0

        for curInd in range(len(arr)):
            curSum += arr[curInd]
            while curSum >= target:
                if curSum == target:
                    length = curInd - startInd + 1
                    arrLenAtStartInd[startInd] = length
                    arrLenAtEndInd[curInd] = length
                    if firstArrayEnd == None:
                        firstArrayEnd = curInd

                curSum -= arr[startInd]
                startInd += 1

        if firstArrayEnd == None:
            return -1

        minLenComplete = arrLenAtEndInd[firstArrayEnd]
        minPairFound = -1
        for startInd in range(firstArrayEnd + 1, len(arr)):
            if arrLenAtStartInd[startInd]:
                pairLen = minLenComplete + arrLenAtStartInd[startInd]
                if minPairFound == -1:
                    minPairFound = pairLen
                else:
                    minPairFound = min(minPairFound, pairLen)
                
            if arrLenAtEndInd[startInd]:
                minLenComplete = min(minLenComplete, arrLenAtEndInd[startInd])

        
        return minPairFound