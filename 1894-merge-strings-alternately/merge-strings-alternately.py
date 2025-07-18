class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        altLen = min(len(word1), len(word2))

        for ind in range(altLen):
            result.append(word1[ind])
            result.append(word2[ind])
        
        for ind in range(altLen, len(word1)):
            result.append(word1[ind])
            
        for ind in range(altLen, len(word2)):
            result.append(word2[ind])
        
        return "".join(result)