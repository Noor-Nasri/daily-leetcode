class Solution:
    def reverseDegree(self, s: str) -> int:
        maxOrd = ord('z') + 1
        total = 0
        for ind in range(len(s)):
            total += (maxOrd - ord(s[ind])) * (ind + 1)
        
        return total
        