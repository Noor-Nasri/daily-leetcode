class Solution:
    # This is interesting. There needs to be some math trick that lets us do some window
    # Maybe binary search on the length, then O(n) slide to confirm if any XOR is >0?
    # NO: This is subsequence, not contigous. So it needs to be some sort of DP: Include or don't
    # But how can we do this with only (ind) input? The trick might be to focus on a single bit
    # If we can choose a single bit, then we just count the number of values with it.
    # We can include all values without it PLUS an odd number including it
    # The result will be non zero!

    # Cant believe I need to waste a time travel ticket on this. oh Well.
    def longestSubsequence(self, nums: List[int]) -> int:
        countOfNumsWithBitInd = [0 for i in range(30)]
        for num in nums:
            bitRep = [int(e) for e in str(bin(num))[2:][::-1]]
            for bitInd in range(len(bitRep)):
                countOfNumsWithBitInd[bitInd] +=  bitRep[bitInd]
        
        maxLength = 0
        for sigDig in range(30):
            if not countOfNumsWithBitInd[sigDig]:
                continue

            count = len(nums) - countOfNumsWithBitInd[sigDig]
            if countOfNumsWithBitInd[sigDig] % 2 == 0:
                count += countOfNumsWithBitInd[sigDig] - 1
            else:
                count += countOfNumsWithBitInd[sigDig]
            
            maxLength = max(maxLength, count)
        
        return maxLength

        