class Solution:
    def reverseBits(self, n: int) -> int:

        total = 0
        for i in range(32, -1, -1):
            if (n // (2**i)):
                n -= 2**i
                total += 2**(32 - i - 1)
        
        return total
        