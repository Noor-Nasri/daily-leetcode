from heapq import heappush, heappop, heapify
class Solution:
    # My first thought is to use a priority queue here for every pair
    # When a pair is replaced by the sum, the pair is removed and the two adjacent pairs are adjusted
    # Simplest implementation is a lazy delete and re-add the new pairs. So 5 operations, each log(n)
    # Worst case is n replacements, so O(nlogn) with a 5 multiple

    # Stop condition: We need to maintain the number of active pairs that are decreasing.
    # When this hits 0, we stop and return the operation count

    # Question: How do we know their active indices and pick left-most in a tie?
    # We should maintain the leftInd for active nodes, based on original nums that merged into it.

    def minimumPairRemoval(self, nums: List[int]) -> int:
        pq = []
        numDecreasing = 0
        leftIndToPrev = {}
        leftIndToNext = {}

        for ind in range(len(nums) - 1):
            num1, num2 = nums[ind], nums[ind + 1]
            isDec = int(num2 < num1)
            numDecreasing += isDec
            data = [num1 + num2, ind, num1, num2, isDec]
            pq.append(data)
            
            if ind:
                leftIndToPrev[ind] = pq[ind - 1]
                leftIndToNext[ind - 1] = pq[ind]
            

        heapify(pq)
        numActions = 0
        while numDecreasing:
            if pq[0][-1] == -1:
                heappop(pq)
                continue

            mergedSum, leftInd, leftNum, rightNum, isDec = heappop(pq)
            #print("Merging:", leftNum, rightNum, "at left ind", leftInd)
            numDecreasing -= isDec
            
            prevExists = leftInd in leftIndToPrev
            nextExists = leftInd in leftIndToNext

            # Lazy delete then create new left node
            if prevExists:
                numDecreasing -= leftIndToPrev[leftInd][-1]
                leftIndToPrev[leftInd][-1] = -1

                _, leftPairLeftInd, leftPairLeftNum, _, _ = leftIndToPrev[leftInd]
                leftPairDec = int(mergedSum < leftPairLeftNum)
                numDecreasing += leftPairDec
                newLeftPairData = [leftPairLeftNum + mergedSum, leftPairLeftInd, leftPairLeftNum, mergedSum, leftPairDec]
                heappush(pq, newLeftPairData)

             # Create the right pair now
            if nextExists:
                numDecreasing -= leftIndToNext[leftInd][-1]
                leftIndToNext[leftInd][-1] = -1

                _, rightPairLeftInd, _, rightPairRightNum, _ = leftIndToNext[leftInd]
                rightPairDec = int(rightPairRightNum < mergedSum)
                numDecreasing += rightPairDec
                newRightPairData = [mergedSum + rightPairRightNum, rightPairLeftInd, mergedSum, rightPairRightNum, rightPairDec]
                heappush(pq, newRightPairData)

            # update lookups
            if prevExists:
                # Update the prev prev to point to the new prev
                if leftPairLeftInd in leftIndToPrev:
                    prevPrevInd = leftIndToPrev[leftPairLeftInd][1] 
                    leftIndToNext[prevPrevInd] = newLeftPairData

                # This new prev should point to the next thing
                if nextExists:
                    leftIndToNext[leftPairLeftInd] = newRightPairData
                else:
                    leftIndToNext.pop(leftPairLeftInd)
                    
                #print("Updated next link:", leftIndToNext)
            
            if nextExists:
                # Same logic
                if rightPairLeftInd in leftIndToNext:
                    nextNextInd = leftIndToNext[rightPairLeftInd][1] 
                    leftIndToPrev[nextNextInd] = newRightPairData

                if prevExists:
                    leftIndToPrev[rightPairLeftInd] = newLeftPairData
                else:
                    leftIndToPrev.pop(rightPairLeftInd)
                
                #print("Updated prev link:", leftIndToPrev)

            numActions += 1


        return numActions