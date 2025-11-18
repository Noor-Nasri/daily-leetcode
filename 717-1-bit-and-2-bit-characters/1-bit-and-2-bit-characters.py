class Solution:
    # Given bits made up of 0,10,11 that ends in a 0, return true if it must have come from '0' and not '10'.
    # We can just work forward: When we see a 1, the next character is included. 

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        isLoneBit = False
        nextBitAccountedFor = False
        for bit in bits:
            if nextBitAccountedFor:
                nextBitAccountedFor = False
                continue
            
            if bit:
                isLoneBit = False
                nextBitAccountedFor = True
            else:
                isLoneBit = True
                nextBitAccountedFor = False

        return isLoneBit
