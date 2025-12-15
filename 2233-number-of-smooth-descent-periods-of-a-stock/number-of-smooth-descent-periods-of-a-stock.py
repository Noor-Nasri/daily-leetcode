class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 0
        chainLen = 0
        lastNum = -1

        for num in prices:
            if num == lastNum - 1:
                chainLen += 1
            else:
                # If len = 5, then we get 5 (singles) + 4 (doubles) + 3 + 2 + 1
                total += chainLen * ((chainLen + 1)/2)
                chainLen = 1
            
            lastNum = num
        
        total += chainLen * ((chainLen + 1)/2)
        return int(total)