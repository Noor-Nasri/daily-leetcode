class Solution:
    # Why is this medium?
    # 1,000->999,999 have one
    # Then 1,000,0000->999,999,999 have two
    # We go until 1,000,000,000,000,000 which has 5.
    # So we just do powers of 1->4 and add i*[num vals in range]

    def countCommas(self, n: int) -> int:
        total = 0
        for numCommas in range(1, 6):
            initValue = 10**(3*numCommas)
            if n < initValue:
                break

            finalValue = min(n, initValue * 1000 - 1)
            total += (finalValue - initValue + 1) * numCommas
        
        return total