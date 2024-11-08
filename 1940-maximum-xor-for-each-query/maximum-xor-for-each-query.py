class Solution:
    def getBestK(self, currentXOR):
        currentBits = int(math.log(currentXOR + 1, 2))
        while currentBits > self.maximumBit:
            #print("reducing", currentXOR, "by", 2 ** (currentBits - 1))
            currentXOR -= 2 ** (currentBits - 1)
            currentBits = int(math.log(currentXOR + 1, 2))
        
        # xor so that the last maximumBit bits all have 1s
        return self.maxAddon ^ currentXOR


    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        self.maximumBit = maximumBit
        self.maxAddon = 2 ** maximumBit - 1
        currentValue = 0
        results = []

        for val in nums:
            currentValue ^= val
            #print("current value", currentValue )
            bestK = self.getBestK(currentValue)
            results.append(bestK)
            #print(bestK)

        return results[::-1]