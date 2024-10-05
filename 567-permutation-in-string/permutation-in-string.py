class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        letters = [0 for i in range(26)]
        for let in s1:
            letters[ord(let) - ord('a')] += 1
        
        ind = 0
        while (ind < len(s2)):
            let = s2[ind]
            letters[ord(let) - ord('a')] -= 1

            if ind >= len(s1): # shift the window
                old_let = s2[ind - len(s1)]
                letters[ord(old_let) - ord('a')] += 1

            if not any(letters):
                return True
            
            ind += 1

        return False
        