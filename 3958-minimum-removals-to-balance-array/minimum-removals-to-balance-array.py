class Solution:
    # We can iterate on starting Ind, then use BS to find latest ind <= val*k
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        minRemovals = len(nums) - 1
        largestIndSmEqCutoff = 0

        for ind1 in range(len(nums)):
            low = max(ind1, largestIndSmEqCutoff)
            high = len(nums) - 1
            cutoff = nums[ind1] * k

            while low <= high:
                mid = (low + high)//2
                if nums[mid] <= cutoff:
                    largestIndSmEqCutoff = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            numRemovals = ind1 + len(nums) - 1 - largestIndSmEqCutoff 
            minRemovals = min(minRemovals, numRemovals)

            if largestIndSmEqCutoff == cutoff:
                break

        return minRemovals