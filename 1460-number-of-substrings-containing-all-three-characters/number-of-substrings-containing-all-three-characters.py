class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0, 0, 0]
        totalCombos = 0
        ind_s = 0
        
        for ind_e in range(len(s)):
            letter = ord(s[ind_e]) - 97
            counts[letter] += 1

            while all(counts):
                totalCombos += len(s) - ind_e
                counts[ord(s[ind_s]) - 97] -= 1
                ind_s += 1
            


        return totalCombos
        