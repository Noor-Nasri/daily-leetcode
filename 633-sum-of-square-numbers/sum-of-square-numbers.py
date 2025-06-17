class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cutoff = int(c ** 0.5)
        for a in range(0, cutoff + 1):
            a_sq = a ** 2
            b = (c - a_sq ) ** 0.5
            if b % 1 == 0:
                return True
        
        return False