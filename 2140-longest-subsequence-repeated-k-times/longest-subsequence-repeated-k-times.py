class Solution:
    # This question is really silly because it would be a good rolling hash for contigous sequences
    # Without contigous, there is no efficient solution. 
    # They just made the constraints weird to allow us to try all viable candidates instead.
    
    # required to repeat k times <--> string has < k * 8 chars. <--> max len of final str is 7, repeated k times.
    # For each k occurances of a char, count the char as a viable option.
    # We will have at most 7 viable options. 
    # We first try all combos of length 7, in order of best. --> 7!
    # Repeating this idea of lengths 6, etc ..
    # Each option can be verified in O(n) by just iterating the string
    
    def getViableChars(self, s, k):
        viableChars = []
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            if counts[c] >= k:
                viableChars.append(c)
                counts[c] -= k
        
        return viableChars
    
    def recurViableStrings(self, remChars, remLength):
        # Not that efficient but max is 7! so its okay
        if remLength == 1:
            return [ [c] for c in remChars ]
        
        allResults = []
        for c in remChars:
            nextRemChars = remChars[:]
            nextRemChars.remove(c)
            permuteResult = self.recurViableStrings(nextRemChars, remLength - 1)
            for res in permuteResult:
                res.append(c)
                allResults.append(res)
        
        return allResults


    def getAllViableStringsOfLength(self, viableChars, length):
        allStringLists = self.recurViableStrings(viableChars, length)
        viableStrings = {"".join(e) for e in allStringLists}
        return sorted(list(viableStrings), reverse = True)

    def isStringValidSol(self, fullStr, subStr, k):
        subInd = 0
        for c in fullStr:
            if subStr[subInd] == c:
                subInd += 1
                if subInd == len(subStr):
                    subInd = 0
                    k -= 1
                    if k == 0:
                        return True

        return False


    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        viableChars = self.getViableChars(s, k)
        for strLen in range(len(viableChars), 0, -1):
            options = self.getAllViableStringsOfLength(viableChars, strLen)
            for subStr in options:
                if self.isStringValidSol(s, subStr, k):
                    return subStr

        return ""
