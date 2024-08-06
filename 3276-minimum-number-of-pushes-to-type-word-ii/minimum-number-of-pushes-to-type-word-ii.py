class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = [0 for i in range(26)]
        for let in word:
            letter_counts[ord(let) - ord('a')] += 1
        
        
        letter_counts = sorted(letter_counts, reverse = True)
        costs = [1]*8 + [2]*8 + [3]*8 + [4]*2
        total_pushes = 0
        
        ind_cost = 0
        for ind in range(26):
            total_pushes += costs[ind]*letter_counts[ind]
        
        return total_pushes