class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {}
        seen = set()

        for i in range(len(s)):
            if not s[i] in mappings:
                if t[i] in seen: return False
                mappings[s[i]] = t[i]
                seen.add(t[i])
                continue
            
            if mappings[s[i]] != t[i]:
                return False

        return True