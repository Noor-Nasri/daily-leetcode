class Solution:
    def binaryGap(self, n: int) -> int:
        st = str(bin(n))[2:]
        maxDist = 0
        curDist = -len(st)

        for c in st:
            curDist += 1
            if c == '1':
                maxDist = max(maxDist, curDist)
                curDist = 0
        
        return maxDist
        