class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        charCountDiff = [[0 for i in range(26)] for parity in range(2)]
        for ind in range(len(s1)):
            charCountDiff[ind % 2][ord(s1[ind]) - 97] += 1
            charCountDiff[ind % 2][ord(s2[ind]) - 97] -= 1
        
        for parityCharDiffs in charCountDiff:
            for diff in parityCharDiffs:
                if diff != 0:
                    return False
        
        noDiff = [[0 for i in range(26)] for parity in range(2)]
        return charCountDiff == noDiff
        

        