class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        vals = list(counts.values())
        maxOdd = 0
        minEven = 10000
        for val in vals:
            if val % 2 == 1:
                maxOdd = max(maxOdd, val)
            else:
                minEven = min(minEven, val)

        return maxOdd - minEven