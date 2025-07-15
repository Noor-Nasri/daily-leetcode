class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        acceptable = set(
            [str(i) for i in range(10)] +
            [chr(i) for i in range(ord('a'), ord('z') + 1)] +
            [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        )
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        hasV = False
        hasC = False

        for ch in word:
            if ch not in acceptable:
                return False
            
            if ch in vowels:
                hasV = True
            elif not ch.isdigit():

                hasC = True

        return hasV and hasC