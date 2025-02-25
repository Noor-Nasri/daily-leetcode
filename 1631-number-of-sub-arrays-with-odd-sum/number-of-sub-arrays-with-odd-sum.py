class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Compute number of subarrays that end at [ind] where the sums are even/odd
        numOddSums = [0]
        numEvenSums = [0]
 
        for num in arr:
            if num % 2 == 1:
                # new number is odd, so to get odd sum we have [self] or [even array, self]
                numOdds = 1 + numEvenSums[-1]
                numEvens = numOddSums[-1] # to get even sum, we take [odd array, self]
            else:
                numOdds = numOddSums[-1]
                numEvens = 1 + numEvenSums[-1]
            
            numOddSums.append(numOdds)
            numEvenSums.append(numEvens)

        
        return sum(numOddSums) % (10**9 + 7)