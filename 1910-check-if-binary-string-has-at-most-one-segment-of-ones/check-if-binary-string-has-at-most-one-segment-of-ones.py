class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seenZero = False
        for c in s:
            if c == '0':
                seenZero = True
            elif seenZero:
                return False

        return True
        