class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Store last index. Once we see it again, discard those indices
        # Thus O(n) going forward, and O(n) total of removals possible. Thus O(n)
    
        if len(s) == 0: return 0


        bestCount = 0
        curCount = 1
        seen = {s[0] : 0} # char -> index
        last_start = 0

        for i in range(1, len(s)):
            c = s[i]
            if not (c in seen):
                seen[c] = i
                curCount += 1
                print("Included", c, "now we have", curCount)
                continue

            # gredy: remove the ones that make including this impossible
            if curCount > bestCount:
                bestCount = curCount
            
            print("Prev index:", seen[c], "cur index:", i)
            prev_index = seen[c]
            curCount = i - prev_index
            for rem_i in range(last_start, prev_index):
                del seen[s[rem_i]]
            
            seen[c] = i
            last_start = prev_index + 1
            print("Reset by", c, "now we have", curCount)

        
        return max(curCount, bestCount)