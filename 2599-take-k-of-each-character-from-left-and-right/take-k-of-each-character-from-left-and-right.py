class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: return 0

        # What we want is the earliest (i), latest (j) s.t [0, i] x [j, n] contain k of a, b, and c
        # What we can do is iterate while choosing (j), then do O(1) lookup for i.
        index_mapping = [{}, {}, {}]
        cur_forward = [0, 0, 0]
        for ind in range(len(s)):
            ind_char = ord(s[ind]) - ord('a')
            cur_forward[ind_char] += 1
            index_mapping[ind_char][cur_forward[ind_char]] = ind + 1
        
        for amount in cur_forward:
            if amount < k: return -1
        
        # solution exists. Now for every ending value, get the earliest cutoff we can do
        leastDelay = len(s)
        cur_backwards = [0, 0, 0]
        for ind in range(len(s) - 1, -1, -1):
            extraDelay = 0
            for ind_remaining in range(3):
                if cur_backwards[ind_remaining] >= k: continue
                extraDelay = max(extraDelay, index_mapping[ind_remaining][k - cur_backwards[ind_remaining]])
            
            option = len(s) - 1 - ind + extraDelay
            leastDelay = min(leastDelay, option)
    
            ind_char = ord(s[ind]) - ord('a')
            cur_backwards[ind_char] += 1
        
        return leastDelay