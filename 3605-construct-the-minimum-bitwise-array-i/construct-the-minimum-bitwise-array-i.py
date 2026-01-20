class Solution:
    # For each prime we need the x that can be OR'd with (x + 1) to make the prime
    # To do this, we find the first 1 in the chain of ending 1s and make it 0.
    # Because then the + 1 of that number would carry over to fill that 1 in the OR.
    # Since this is only primes, ending with 0 is only for 2. 

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num == 2:
                result.append(-1)
                continue
            
            binRep = list(str(bin(num))[2:])
            for ind in range(len(binRep) - 1, -2, -1):
                if ind == -1 or binRep[ind] == '0':
                    binRep[ind + 1] = "0"
                    fixedBin = "".join(binRep)
                    result.append(int(fixedBin, 2))
                    break
            
        return result

