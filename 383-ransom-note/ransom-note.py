class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = [0 for i in range(26)]
        for c in magazine:
            counts[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] < 0:
                return False
        
        return True


        