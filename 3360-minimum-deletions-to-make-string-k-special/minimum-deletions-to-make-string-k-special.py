class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        occurances = {}
        for c in word:
            occurances[c] = occurances.get(c, 0) + 1
        
        # If we stick to the min, its easy counting
        # But it might be better to remove the minfreq and utilize a higher freq as a min.
        # Easiest method is to reduce this to 26 elements and try every min.

        occur_counts = list(occurances.values())
        minMoves = float('inf')
        for chosen_min in occur_counts:
            # Sum of two ideas:
            # 1. num moves needed to reduce larger values to within bounds
            # 2. num moves needed to erase smaller values
            moves = 0 
            
            for other_freq in occur_counts:
                if other_freq < chosen_min:
                    moves += other_freq
                elif other_freq > chosen_min + k:
                    moves += other_freq - (chosen_min + k)


            minMoves = min(moves, minMoves)
        
        return minMoves