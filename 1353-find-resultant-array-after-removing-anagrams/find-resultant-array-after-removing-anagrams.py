class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        finalWords = []
        lastWordCharCounts = None

        for word in words:
            charCount = [0 for i in range(26)]
            for char in word:
                charCount[ord(char) - 97] += 1
            
            if charCount == lastWordCharCounts:
                continue
            
            finalWords.append(word)
            lastWordCharCounts = charCount
        
        return finalWords