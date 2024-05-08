class Solution:
    def reverseBits(self, n: int) -> int:

        total = 0
        bit_power = 2**31
        reverse_power = 1
        for i in range(32):
            if (n // bit_power):
                n -= bit_power
                total += reverse_power
            bit_power /= 2
            reverse_power *= 2
        
        return total
        