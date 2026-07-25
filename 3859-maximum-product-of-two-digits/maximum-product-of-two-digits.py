class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(e) for e in str(n)]
        max1 = 0
        max2 = 0

        for dig in digits:
            if dig > max1:
                max1, max2 = dig, max1
            elif dig > max2:
                max2 = dig
        
        return max1*max2