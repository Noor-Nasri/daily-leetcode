class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        orda, ordA = ord('a'), ord('A')
        seen = set(word)
        count = 0
        for i in range(26):
            lower, upper = chr(orda + i), chr(ordA + i)
            if lower in seen and upper in seen:
                count += 1

        return count