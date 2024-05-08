class Solution:
    def reverseBits(self, n: int) -> int:

        total = 0
        for i in range(32, -1, -1):
            val = 2**i
            if (n // val):
                n -= val
                total += 2**(32 - i - 1)
        
        return total
        