from heapq import heappop, heappush
class Solution:
    # The first arr is 0->i-1 and the last array is j->n-1, with i and j being at most dist apart
    # So the moment we pick i, the min sum is from the k-2 elements between i+1 and i+dist.
    # This becomes a window problem: From ind 2 to n-dist, we maintain the sum of those k-2 numbers

    # We can do this with 2 heaps to maintain top k-2 and remaining. 
    # We maintain [ind] = isTopK and heaps of [val, ind]
    # Then when we remove an element within topK, we need to add another element in.
    # Whenever top of either heap is outside window, we can pop. 

    def createInitWindow(self, nums, k, dist):
        # Puts [1..dist+1] elements into the init window

        initVals = sorted([(nums[i], i) for i in range(1, dist + 2)])
        isBestK = {}
        for sortedInd in range(len(initVals)):
            _, origInd = initVals[sortedInd]
            isBestK[origInd] = sortedInd < k - 2

        minKElementsMaxHeap = [(-initVals[i][0], initVals[i][1]) for i in range(k - 3, -1, -1)]
        remainingElementsMinHeap = initVals[k-2:]

        return minKElementsMaxHeap, remainingElementsMinHeap, isBestK
    
    def cleanHeapThenPop(self, pq, curStartInd):
        while pq and pq[0][1] <= curStartInd:
            heappop(pq)
        return heappop(pq)
        
    def cleanPqs(self, pq1, pq2, curStartInd):
        while pq1 and pq1[0][1] <= curStartInd:
            heappop(pq1)

        while pq2 and pq2[0][1] <= curStartInd:
            heappop(pq2)

    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        minTotalSum = float('inf')
        minKElementsMaxHeap, remainingElementsMinHeap, isBestK = self.createInitWindow(nums, k, dist)
        curTopKSum = sum(-e[0] for e in minKElementsMaxHeap)

        for firstIndChoice in range(1, len(nums) - k + 2):
            #print("Exploring", firstIndChoice, "with init configs as", minKElementsMaxHeap, remainingElementsMinHeap, isBestK)
            # Step 1: Take first ind out of options, as its now forced
            if isBestK[firstIndChoice]:
                _, newMinIndex = self.cleanHeapThenPop(remainingElementsMinHeap, firstIndChoice)
                curTopKSum -= nums[firstIndChoice]
                curTopKSum += nums[newMinIndex]
                heappush(minKElementsMaxHeap, (-nums[newMinIndex], newMinIndex))
                isBestK[newMinIndex] = True
            
            # Step 2: Consider this ind and the next (k-2) options
            possibleSum = nums[0] + nums[firstIndChoice] + curTopKSum
            minTotalSum = min(minTotalSum,possibleSum)

            # Step 3: See if there is a new element that'll fit into window
            self.cleanPqs(minKElementsMaxHeap, remainingElementsMinHeap, firstIndChoice)
            nextDistantInd = firstIndChoice + dist + 1
            if nextDistantInd >= len(nums):
                continue
            
            if nums[nextDistantInd] < -minKElementsMaxHeap[0][0]:
                _, oldMinIndex = heappop(minKElementsMaxHeap)
                isBestK[oldMinIndex] = False
                curTopKSum -= nums[oldMinIndex]
                heappush(remainingElementsMinHeap, (nums[oldMinIndex], oldMinIndex))

                isBestK[nextDistantInd] = True
                curTopKSum += nums[nextDistantInd]
                heappush(minKElementsMaxHeap, (-nums[nextDistantInd], nextDistantInd))

            else:
                isBestK[nextDistantInd] = False
                heappush(remainingElementsMinHeap, (nums[nextDistantInd], nextDistantInd))

        return minTotalSum