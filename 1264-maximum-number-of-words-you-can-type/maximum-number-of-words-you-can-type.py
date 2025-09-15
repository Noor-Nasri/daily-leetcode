class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        restricted = set(brokenLetters)

        numValid = 0
        for word in words:
            valid = 1
            for c in word:
                if c in restricted:
                    valid = 0
                    break
            
            numValid += valid

        return numValid
        