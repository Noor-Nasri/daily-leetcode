class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastInd = - (k + 1)
        for ind in range(len(nums)):
            if nums[ind] == 1:
                if ind - lastInd <= k:
                    return False
                
                lastInd = ind

        return True
        