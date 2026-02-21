class Solution:
    # 10^6 is only 20 digits, so we just need to know the prime numbers from 1->20
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        found = 0

        for val in range(left, right + 1):
            numOnes = str(bin(val))[2:].count('1')
            if numOnes in primes:
                found += 1

        return found