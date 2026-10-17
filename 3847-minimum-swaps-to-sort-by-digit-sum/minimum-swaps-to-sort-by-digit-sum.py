class Solution:
    # So the first instinct is to just sort it first, then compare inds
    # If val[0] needs to go to [3], but the value there wants to go to [4]..
    # Is it okay to just immediately swap (0, 3) so that ind 3 is resolved?

    # Is there any other possible ordering that would resolve two in one go?
    # No, because any chain we want to start could just have started at [0], and we spend 1 more to finish 

    def minSwaps(self, nums: List[int]) -> int:
        # Phase 1: figure out desired order
        n = len(nums)
        orderedData = []
        for ind in range(n):
            val = nums[ind]
            digSum = sum([int(e) for e in str(val)])
            orderedData.append((digSum, val))
        orderedData = sorted(orderedData)

        expectedInds = {}
        for newInd in range(n):
            val = orderedData[newInd][1]
            expectedInds[val] = newInd
        
        # Phase 2: Compute swaps needed
        cost = 0
        for ind1 in range(n):
            while True:
                curVal = nums[ind1]
                ind2 = expectedInds[curVal]
                if ind1 == ind2:
                    break
                
                nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
                cost += 1
        
        return cost
