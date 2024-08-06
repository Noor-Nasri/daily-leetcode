class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = Counter(word)
        key_order = sorted(letter_counts.keys(), reverse = True, key = lambda e : letter_counts[e])
        costs = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4]
        total_pushes = 0
        
        ind_cost = 0
        for key in key_order:
            total_pushes += costs[ind_cost]*letter_counts[key]
            ind_cost += 1
        
        return total_pushes