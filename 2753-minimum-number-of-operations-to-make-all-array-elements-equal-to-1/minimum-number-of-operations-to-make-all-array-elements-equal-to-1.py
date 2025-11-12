class Solution:
    # If we can make one value 1, we can propogate that everywhere. Is there ever a faster way?
    # No, because we always need to turn them into 1. So the first technique that gets a 1 only had n-1 moves left, but all others have >= n
    # Okay, so the real question is: What is the fastest way to get a 1 in the array?

    # Idea 1: BFS. I think it can work but its super annoying to write up.
    # For each ind, we can start with a bank of factors and do a BFS for removing factors.
    # Each layer can double but you can have at most log(nums[i]) layers. So its just O(nums[i] * costPerOp)
    # So we first precompute factors, then have 10^6 * 2 * log(10^6) from # factors, so nlogn

    # idea 2: Subarray selection. I think it works ..
    # Given a subarr with gcd = 1, we can achieve that result by gdc(a, gcd(b, gcd(c, ...))). I think ..
    # Okay, google confirmed that gcd property. So just precompute primes and gcd every subarr
    
    def minOperations(self, nums: List[int]) -> int:
        startingOnes = nums.count(1)
        if startingOnes:
            return len(nums) - startingOnes
            
        smallestSubarr = len(nums) + 1

        for start in range(len(nums)):
            curVal = nums[start]
            end = start + 1

            while curVal > 1 and end < len(nums) and (end - start) < smallestSubarr:
                curVal = math.gcd(curVal, nums[end])
                end += 1
            
            arrSize = end - start - 1
            if curVal == 1 and arrSize < smallestSubarr:
                smallestSubarr = arrSize
        
        if smallestSubarr > len(nums):
            return -1
        
        return smallestSubarr + len(nums) - 1


        