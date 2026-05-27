class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        charToInds = {}
        for ind in range(len(word)):
            char = word[ind]
            if char not in charToInds:
                charToInds[char] = [ind]
            else:
                charToInds[char].append(ind)
        
        found = 0
        for i in range(26):
            lower, upper = chr(97 + i), chr(65 + i)
            if lower in charToInds and upper in charToInds:
                if charToInds[lower][-1] < charToInds[upper][0]:
                    found += 1

        return found