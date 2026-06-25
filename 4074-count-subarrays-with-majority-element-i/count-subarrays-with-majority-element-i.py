class Solution:
    # The obvious solution is just n^2 loop which should work here
    # The next question tomorrow will probably expect a better solution though
    # I think the optimization is by looking at just the list of inds, and some tricky 2-pointer
    # For now lets just so the easy solution cuz I barely slept.

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        totalFound = 0
        for st in range(len(nums)):
            count = 0
            for en in range(st, len(nums)):
                if nums[en] == target:
                    count += 1
                
                if count > (en - st + 1)/2:
                    totalFound += 1
        
        return totalFound