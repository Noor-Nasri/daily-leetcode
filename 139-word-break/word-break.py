class Solution:
    def helper(self, s, ind, words):
        # returns True iff s[ind:] can be made with words
        if ind == len(s): return True
        if ind in self.sols: return self.sols[ind]

        for word_end in range(ind + 1, len(s) + 1):
            word = s[ind:word_end]
            if word in words:
                if self.helper(s, word_end, words):
                    self.sols[ind] = True
                    return True
        
        self.sols[ind] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.sols = {}
        return self.helper(s, 0, set(wordDict))
        