class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = 0
        prevCharCount = 0
        charCount = 0
        curChar = '-1'

        for c in s:
            if c == curChar:
                charCount += 1
            else:
                prevCharCount = charCount
                charCount = 1
                curChar = c
            

            if charCount <= prevCharCount:
                total += 1

        return total