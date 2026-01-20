class Solution:
    # Same solution as part 1 lol
    
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

