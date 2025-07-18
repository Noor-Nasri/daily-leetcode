class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        
        for ind in range(max(len(word1), len(word2))):
            if ind < len(word1):
                result.append(word1[ind])
            if ind < len(word2):
                result.append(word2[ind])
        
        return "".join(result)