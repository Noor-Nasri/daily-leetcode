class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        seen = []
        for c in s:
            if seen and seen[-1] == "(" and c == ")":
                seen.pop()
            else:
                seen.append(c)

        return len(seen) # ends up as )))...((( 
        