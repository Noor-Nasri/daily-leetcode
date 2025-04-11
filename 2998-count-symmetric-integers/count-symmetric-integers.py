class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            numStr = str(num)
            if len(numStr) % 2 == 0:
                sumL = sum([int(numStr[i]) for i in range(len(numStr) // 2)])
                sumR = sum([int(numStr[i]) for i in range(len(numStr) // 2, len(numStr))])
                count += int(sumL == sumR)
        
        return count