class Solution:
    # So, each number can be adjusted by up to k. The obvious start is to sort the numbers and some sort of sliding window
    # If we select a target value x, then we can do two binary searches to get the max frequency for that value
    # The problem is that the chosen value could be between different values, which in theory is n^2. How can we limit this?

    # The reason we would chose a non-seen value is because we can make two ends reach in the middle, as opposed to meeting at a given val
    # So for the lowest val v, if we were going to stretch to a non-existing value anyways, why not just go to v + k?
    # Wait this is actually really smart I think. Just add + k to all values as possible checkpoints, then we only have 2n values to check
    # This becomes 2n*(2logn) -> O(nlogn)

    # First val >= v - k
    def getSmallestIndOfValueGTEx(self, nums, x):
        low = 0
        high = len(nums) - 1
        best = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= x:
                best = mid
                high = mid -1 
            else:
                low = mid + 1
        
        return best
    
    # Last val <= v + k
    def getLargestIndOfValueSTEx(self, nums, x):
        low = 0
        high = len(nums) - 1
        best = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= x:
                best = mid
                low = mid + 1
            else:
                high = mid -1 
        
        return best

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums = sorted(nums)
        counters = {}
        for val in nums:
            counters[val] = counters.get(val, 0) + 1
            if k:
                counters[val + k] = 0
        

        maxCount = 0
        for chosenVal in counters:
            reachableRangeStart = self.getSmallestIndOfValueGTEx(nums, chosenVal - k)
            reachableRangeEnd = self.getLargestIndOfValueSTEx(nums, chosenVal + k)
            numInRange = reachableRangeEnd - reachableRangeStart + 1
            numExact = counters[chosenVal]
            possible = numExact + min(numOperations, numInRange - numExact)
            maxCount = max(maxCount, possible)


        return maxCount