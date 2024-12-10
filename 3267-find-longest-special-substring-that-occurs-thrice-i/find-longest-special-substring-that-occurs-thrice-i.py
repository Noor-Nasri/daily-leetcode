class Solution:
    def maximumLength(self, s: str) -> int:
        seen = {
            s[0] : 1
        }

        cur = s[0]
        freq = 1
        for ind in range(1, len(s)):
            if s[ind] == cur[0]:
                freq += 1
            else:
                cur = s[ind]
                freq = 1

            if not cur*freq in seen:
                seen[cur*freq] = 0
            
            for i in range(1, freq + 1):
                seen[cur*i] += 1
        
        for k in sorted(seen.keys(), key = len, reverse = True):
            if seen[k] >= 3:
                return len(k)
        
        return -1