class Solution:
    digitCounts = {
        (0, 1, 0, 0, 0, 0, 0, 0, 0, 0)
    }
    pow2 = 1
    while pow2 < 10 ** 9:
        pow2 *= 2
        counts = [0 for i in range(10)]
        for dig in str(pow2):
            counts[int(dig)] += 1
        
        digitCounts.add(tuple(counts))

    def reorderedPowerOf2(self, n: int) -> bool:
        # 9! diff perms for a given n, which we can check against known powers of 2
        # Alternatively, we can just go through the powers of 2 and see if the num digits adds up
        seenCounts = [0 for i in range(10)]
        for dig in str(n):
            seenCounts[int(dig)] += 1
        
        seenCounts = tuple(seenCounts)
        return seenCounts in self.digitCounts

        