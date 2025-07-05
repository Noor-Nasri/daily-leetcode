class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        for n in arr:
            counts[n] = counts.get(n, 0) + 1
        
        best = -1
        for n in counts:
            if n > best and counts[n] == n:
                best = n
        
        return best