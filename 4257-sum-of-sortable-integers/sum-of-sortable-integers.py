class Solution:
    # Okay, so for a given k we can verify by checking that each group has at most 1 decrease
    # The problem is that we obviously cant test every k in O(n), so we need to either:
    # (a) Solve for a subset of k, maybe BS and infer the smaller values?
    # (b) Some form of DP that contracts this into an nlogn instead of n^2?
    # (c) Maybe can solve like n=2,3,5, etc primes, and somehow expand window sizes accordingly?

    # oh wait, isnt this easy actualyl? There cant be that many divisors in the first place for k.
    # So like, 50k only has 30 divisors. Thats essentially like log(n)
    
    def isSortable(self, nums, divisor):    
        # Ah, I misread the requirement as every subarray being sorted. 
        # Instead, we need to also check that groups are properly chained. Trivial.

        numGroups = len(nums) // divisor
        lastValue = 0
        for groupInd in range(numGroups):
            startInd = groupInd * divisor
            endInd = (groupInd + 1) * divisor - 1
            canShift = nums[endInd] <= nums[startInd]
            alreadyShifted = False

            for ind in range(startInd + 1, endInd + 1):
                if nums[ind] < nums[ind - 1]:
                    # This value must shift to the start, otherwise its decreasing
                    if canShift and not alreadyShifted:
                        alreadyShifted = True
                        startInd = ind
                        endInd = ind - 1
                    else:
                        return False
                        
            if nums[startInd] < lastValue:
                return False
                
            lastValue = nums[endInd]
            
        return True


    def sortableIntegers(self, nums: list[int]) -> int:
        divisors = []
        for i in range(1, len(nums) + 1):
            if len(nums) % i == 0:
                divisors.append(i)
        
        total = 0
        for divisor in divisors:
            if self.isSortable(nums, divisor):
                total += divisor
        
        return total
