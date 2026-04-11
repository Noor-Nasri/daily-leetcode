class Solution:
    # Say i < j < k, then we're looking for min(2k - 2i). Meaning we group the nearest inds.  
    # We're looking for equal elements, so we can just do this in O(n)
    # We group elements by value, and every new element considers the 2 inds before it.

    def minimumDistance(self, nums: List[int]) -> int:
        numToInds = {}
        maxDist = -1
        for ind in range(len(nums)):
            num = nums[ind]
            if num in numToInds:
                numToInds[num].append(ind)
            else:
                numToInds[num] = [ind]
            
            if len(numToInds[num]) >= 3:
                curDist = 2 * (numToInds[num][-1] - numToInds[num][-3])
                if maxDist == -1 or curDist < maxDist:
                    maxDist = curDist

        return maxDist