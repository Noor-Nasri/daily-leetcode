class Solution:
    def valFromBits(self, curBitCounts):
        mult = 1
        tot = 0
        for i in range(64):
            if curBitCounts[i]:
                tot += mult 
            mult *= 2
        return tot
    
    def adjustNumBits(self, curBitCounts, num, adjustmentVal):
        # We could do it with some math but it should pass anyways
        bits = str(bin(num))[2:][::-1]
        for ind in range(len(bits)):
            if bits[ind] == '1':
                curBitCounts[ind] += adjustmentVal
                


    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Working backwards, we know the OR result of OR(i->n)
        # Working forward, if we solve the earliest j for ind0 (ie 0->j), the next ind can start from j
        maximalOR = 0
        indToMaxOR = [0 for i in range(len(nums))]
        for ind in range(len(nums) -1, -1, -1):
            maximalOR |= nums[ind]
            indToMaxOR[ind] = maximalOR
        
        solution = [-1 for i in range(len(nums))]
        curBitCounts = [0 for i in range(64)]
        curJ = -1 

        for ind in range(len(nums)):
            while curJ < ind or self.valFromBits(curBitCounts) < indToMaxOR[ind]:
                curJ += 1
                self.adjustNumBits(curBitCounts, nums[curJ], 1)

            solution[ind] = curJ - ind + 1
            self.adjustNumBits(curBitCounts, nums[ind], -1)
        
        return solution