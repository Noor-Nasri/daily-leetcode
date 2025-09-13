class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counts = {}
        most_vowel, most_cons = 0, 0

        for c in s:
            counts[c] = counts.get(c, 0) + 1
            if c in vowels and counts[c] > most_vowel:
                most_vowel = counts[c]
            elif c not in vowels and counts[c] > most_cons:
                most_cons = counts[c]
        
        return most_vowel + most_cons
        