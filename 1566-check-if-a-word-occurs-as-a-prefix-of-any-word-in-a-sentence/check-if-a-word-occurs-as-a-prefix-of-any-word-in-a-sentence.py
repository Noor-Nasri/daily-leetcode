class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for ind in range(len(words)):
            if len(words[ind]) >= len(searchWord) and words[ind][:len(searchWord)] == searchWord:
                return ind + 1
                
        return -1
        