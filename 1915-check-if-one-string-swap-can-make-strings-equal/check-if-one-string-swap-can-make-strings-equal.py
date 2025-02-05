class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        # check if the strings are equal except at 2 indices that can be flipped
        numWrong = 0
        nonMatches = []
        for ind in range(len(s1)):
            if s1[ind] != s2[ind]:
                numWrong += 1
                nonMatches.append(s1[ind])
                nonMatches.append(s2[ind])
        
        if numWrong != 2:
            return False
        
        return nonMatches[0] == nonMatches[3] and nonMatches[1] == nonMatches[2]
            

        