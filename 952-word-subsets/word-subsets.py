class Solution:
    def isUniversal(self, word, requiredLetterCounts):
        letters = [0 for i in range(26)]
        for let in word:
            letters[ord(let) - 97] += 1
        
        for ind in range(26):
            if letters[ind] < requiredLetterCounts[ind]:
                return False

        return True
    
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        requiredLetterCounts = [0 for i in range(26)]

        for word in words2:
            letters = [0 for i in range(26)]
            for let in word:
                letters[ord(let) - 97] += 1
            
            for ind in range(26):
                requiredLetterCounts[ind] = max(requiredLetterCounts[ind], letters[ind])
        
        universals = []
        for word in words1:
            if self.isUniversal(word, requiredLetterCounts):
                universals.append(word)
        
        return universals