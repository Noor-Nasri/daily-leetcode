class Solution:
    def possibleStringCount(self, word: str) -> int:
        numWays = 1

        cur = "."  
        count = 1
        for char in word:
            if char == cur:
                count += 1
            else:
                numWays += count - 1
                cur = char
                count = 1
        
        numWays += count - 1
        return numWays
        