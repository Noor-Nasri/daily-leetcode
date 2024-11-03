class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for ind in range(len(s)):
            if s[ind:] + s[:ind] == goal:
                return True
        return False
        