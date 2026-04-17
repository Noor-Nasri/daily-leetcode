class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        refToInd = {}
        minDist = len(nums)
        for ind in range(len(nums)):
            val = nums[ind]
            rev = int(str(val)[::-1])

            if val in refToInd:
                minDist = min(minDist, ind - refToInd[val])
            
            refToInd[rev] = ind
        
        return minDist == len(nums) and -1 or minDist
