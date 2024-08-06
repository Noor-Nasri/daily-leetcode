class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = [0 for i in range(26)]
        for let in word:
            letter_counts[ord(let) - 97] += 1
        
        
        letter_counts = sorted(letter_counts, reverse = True)
        costs = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4]
        total_pushes = 0
        
        ind_cost = 0
        for ind in range(26):
            total_pushes += costs[ind]*letter_counts[ind]
        
        return total_pushes