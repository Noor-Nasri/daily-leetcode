class Solution:
    def stripPattern(self, s, pattern, reward):
        result = []
        total = 0
        
        for c in s:
            result.append(c)

            while len(result) >= 2 and result[-2] == pattern[0] and result[-1] == pattern[1]:
                result.pop()
                result.pop()
                total += reward

        return result, total

    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Suppose x is more valuable: just take all the ab you can get in first pass.
        # then you will just have at most bbbbbaaaaa, which you can take as many as needed
        # To do one pass: have a stack for all chars so far, remove as needed
        # Q: Will taking ab ever result in us not taking [ba] x2. No! Because baba -> ba so we still get one of them
        patternOrder = ["ab", "ba"]
        if y > x:
            patternOrder = ["ba", "ab"]
        
        res1, tot1 = self.stripPattern(s, patternOrder[0], max(x, y))
        res2, tot2 = self.stripPattern(res1, patternOrder[1], min(x, y))
        return tot1 + tot2

        