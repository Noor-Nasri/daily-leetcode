class Solution:
    def concatenatedBinary(self, n: int) -> int:
        total = 0
        curDigVal = 1
        MODVAL = 10**9 + 7

        for val in range(n, 0, -1):
            while val:
                if val % 2:
                    total = (total + curDigVal) % MODVAL
                
                val //= 2
                curDigVal = (curDigVal * 2) % MODVAL
        
        return total