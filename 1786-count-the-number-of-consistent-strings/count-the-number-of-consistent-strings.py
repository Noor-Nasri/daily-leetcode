class Solution:
    def isValid(self, word):
        for letter in word:
            if letter not in self.allowed: return False
        return True

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        self.allowed = set(allowed)
        count = 0

        for word in words:
            if self.isValid(word):
                count += 1
        
        return count

        