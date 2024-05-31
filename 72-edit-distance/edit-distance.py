class Solution:
    def helper(self, word1: str, word2: str, ind1, ind2):
        if (ind1, ind2) in self.sols:
            return self.sols[(ind1, ind2)]
        
        if ind1 == len(word1): # Must add all remaining
            return len(word2) - ind2

        if ind2 == len(word2): # Must remove all extra
            return len(word1) - ind1

        # Replace or match the char
        option_match = self.helper(word1, word2, ind1 + 1, ind2 + 1)
        if word1[ind1] != word2[ind2]: option_match += 1

        # Delete cur or insert required char
        option_delete = 1 + self.helper(word1, word2, ind1 + 1, ind2)
        option_insert = 1 + self.helper(word1, word2, ind1, ind2 + 1)

        best = min(option_match, option_delete, option_insert)
        self.sols[(ind1, ind2)] = best
        return best


    def minDistance(self, word1: str, word2: str) -> int:
        self.sols = {}
        return self.helper(word1, word2, 0, 0)

        