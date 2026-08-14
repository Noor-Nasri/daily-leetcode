class Solution:
    # Can do n^2 since its easy, but its also just a basic 2pointer

    def maximumLengthSubstring(self, s: str) -> int:
        counts = [0 for i in range(26)]
        maxFound = 0
        startInd = 0

        for endInd in range(len(s)):
            val = ord(s[endInd]) - 97
            counts[val] += 1

            while counts[val] > 2:
                counts[ord(s[startInd]) - 97] -= 1
                startInd += 1
            
            maxFound = max(maxFound, endInd - startInd + 1)
        
        return maxFound

